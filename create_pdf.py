from fpdf import FPDF
from get_data import GetData  

class PDFCreator(FPDF):
    def __init__(self):
        super().__init__()
        self.source_file = ""
        self.add_font(
            "NotoSansJP",
            "",
            r"NotoSansJP-VariableFont_wght.ttf",
            uni=True
        )
        
        self.add_font(
            "NotoSansJP",
            "B",
            r"noto-sans-jp-bold.ttf",
            uni=True
        )
    
    def create_pdf(self, source_file:str):
        self.source_file = source_file
        
        data = GetData(self.source_file)
        df_data = data.give_data()
        
        self.add_page()
        self.set_font("NotoSansJP", "", 12)
        question_counter = 1
        
        for i in range(len(df_data)):
            row = df_data.iloc[i]
            if row["type"] == "案内":
                if question_counter != 1:
                    self.ln(10)
                self.set_font("NotoSansJP", "B", 12)
                self.cell(0, 10, f"{row['Text']}", new_x="LMARGIN", new_y="NEXT")
            if row["type"] == "漢字":
                self.set_font("NotoSansJP", "", 12)
                self.cell(0, 10, f"{question_counter} {row['Text']} ", new_x="LMARGIN", new_y="NEXT")
                usable_width = self.w - self.l_margin - self.r_margin
                cell_width = usable_width / 4
                cell_height = 10
                
                self.cell(cell_width, cell_height, f"A. {row['A']}", align="L")
                self.cell(cell_width, cell_height, f"B. {row['B']}", align="L")
                self.cell(cell_width, cell_height, f"C. {row['C']}", align="L")
                self.cell(cell_width, cell_height, f"D. {row['D']}", new_x="LMARGIN", new_y="NEXT", align="L")
                question_counter += 1
                if i == len(df_data) -1:
                    self.ln(15)

        self.output("C:\\Users\\Fariz Armesta\\Documents\\GitHub\\test-maker-jp\\test.pdf")
    
    def header(self):
        self.image("ARMESTA2.png", x=10, y=8, w=26, h=26)
        self.set_font("helvetica", style="B", size=15)
        self.cell(0, 10, "JAPANESE N5 TEST REVIEW", new_x="LMARGIN", new_y="NEXT", align="C")
        self.cell(0, 10, "Review Minna no Nihonggo bab 1-6", new_x="LMARGIN", new_y="NEXT", align="C")
        self.set_font("NotoSansJP", "", 12)
        self.cell(0, 10, "文字・語彙・文法", new_x="LMARGIN", new_y="NEXT", align="R")
        
        self.ln(5)
        y= self.get_y()
        self.line(self.l_margin, y, self.w - self.r_margin, y)
        
        self.ln(10)

    def footer(self):
        self.set_y(-20)
        self.set_font("helvetica", style="I", size=8)
        self.cell(0, 5, "Copyright AISOU JAPANESE COURSE @ 2025", new_x="LMARGIN", new_y="NEXT", align="C")
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")
        
        
