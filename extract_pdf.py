import subprocess
import sys
import os

def install_and_extract():
    try:
        import pypdf
    except ImportError:
        print("Installing pypdf...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pypdf"])
        import pypdf

    print("Extracting text from WENYAN_HU.pdf...")
    reader = pypdf.PdfReader('WENYAN_HU.pdf')
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"

    with open("resume_text.txt", "w", encoding="utf-8") as f:
        f.write(text)
    
    print("Successfully extracted to resume_text.txt")

if __name__ == "__main__":
    install_and_extract()
