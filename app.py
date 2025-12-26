from textual import on, work
from textual.app import App, ComposeResult
from textual.containers import Center
from textual.widgets import Button, Label
from textual.reactive import reactive

from textual_fspicker import FileOpen, SelectDirectory

from create_pdf import PDFCreator

class TestMakerApp(App[None]):
    CSS_PATH = "styles.css"
    selected_file = reactive("")
    output_dir = reactive("")
    
    def compose(self) -> ComposeResult:
        
        with Center():
            yield Label("JP Test Maker", id="title")
            
            yield Button("Press to open a file", id="open")
            yield Label(id="file_label")
            
            yield Button("Select Output Directory", id="dir")
            yield Label(id="dir_label")
            
            yield Button("Create PDF", id="create_pdf")
    
        
    def watch_selected_file(self, value: str) -> None:
        self.query_one("#file_label", Label).update(value)
    
    def watch_output_dir(self, value: str) -> None:
        self.query_one("#dir_label", Label).update(value)

    @on(Button.Pressed, "#open")
    @work
    async def open_a_file(self) -> None:
        if opened := await self.push_screen_wait(FileOpen(must_exist=True)):
            self.selected_file = str(opened)
            
    @on(Button.Pressed, "#dir")
    @work
    async def pick_a_directory(self) -> None:
        if opened := await self.push_screen_wait(SelectDirectory()):
            self.query_one("#dir_label", Label).update(str(opened))
            
    @on(Button.Pressed, "#create_pdf")
    @work
    async def create_pdf(self) -> None:
        pdf_creator = PDFCreator()
        pdf_creator.create_pdf(self.selected_file, self.output_dir)
        self.notify(f"Successfully created", title="SUCCESS")
            
if __name__ == "__main__":
    app = TestMakerApp().run()
