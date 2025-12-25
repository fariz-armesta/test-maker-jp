import subprocess
import os
import sys

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    subprocess.Popen(
        [
            "wt",
            "cmd",
            "/k",
            f'cd /d "{base_dir}" && '
            'title JP Test Maker && '
            'python app.py'
        ]
    )


if __name__ == "__main__":
    main()
    sys.exit()