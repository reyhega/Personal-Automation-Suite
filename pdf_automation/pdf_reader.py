import os
import argparse
from datetime import datetime
from PyPDF2 import PdfReader

def extract_text_from_pdf(filepath):
    if not os.path.exists(filepath):
        print(f"❌ ERROR! Invalid file path: {filepath}")
        return
    
    if not filepath.endswith(".pdf"):
        print(f"❌ ERROR! Invalid file type, file must be a PDF.")
        return

    reader = PdfReader(filepath)
    page = reader.pages[0]
    extracted_text = page.extract_text()
    extracted_txt_file = "resources/Extracted_text.txt"
    timestamp = datetime.now().strftime("%H:%M:%S|%m%d%Y")

    if os.path.exists(extracted_txt_file):
        extracted_txt_file = f"resources/Extracted_text_{timestamp}.txt"
    
    try:
        with open(extracted_txt_file, "w") as file:
            file.write(extracted_text)
            print(f"✅ Extracted text from {filepath} → {extracted_txt_file}")
    except Exception as e:
            print(f"❌ Failed to extract text from {filepath}: {e}")

    print(extracted_text)
    return extracted_text

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract text from PDF file')
    parser.add_argument('--filepath', required=True, help='Path to PDF file to extract text from')
    args = parser.parse_args()
    extract_text_from_pdf(args.filepath)