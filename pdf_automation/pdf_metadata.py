import os
import argparse
from datetime import datetime
from PyPDF2 import PdfReader, PdfWriter


"""def read_metadata(filepath):
    reader = PdfReader(filepath)

    meta = reader.metadata
    num_pages = len(reader.pages)

    print(f"Number of pages: {num_pages}")

    # All of the following could be None:
    print(f"Author: {meta.author}")
    print(f"Creator: {meta.creator}")
    print(f"Producer: {meta.producer}")
    print(f"Subject: {meta.subject}")
    print(f"Title: {meta.title}")
"""

def add_metadata(filepath):
    reader = PdfReader(filepath)
    writer = PdfWriter()
    meta = reader.metadata
    old_meta = {
        "num_pages": len(reader.pages),
        "author": meta.author,
        "creator": meta.creator,
        "producer": meta.producer,
        "subject": meta.subject,
        "title": meta.title,
    }
    
    # Add pages to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Add the metadata
    writer.add_metadata(
        {
            "/Author": "Rey HeGa",
            "/Creator": "Rey Hdz",
        }
    )

    # Save the new PDF to a file
    new_file = "resources/meta-pdf.pdf"
    with open(new_file, "wb") as f:
        writer.write(f)

    new_reader = PdfReader(new_file)
    new_meta = new_reader.metadata
    new_file_meta = {
        "num_pages": len(new_reader.pages),
        "author": new_meta.author,
        "creator": new_meta.creator,
        "producer": new_meta.producer,
        "subject": new_meta.subject,
        "title": new_meta.title,
    }

    print(f"✅ Succesfully created copy of file with following metadata:")
    for key in old_meta:
        old_value = old_meta[key]
        new_value = new_file_meta[key]
        print(f"☑️ Changed {key} from '{old_value}' → '{new_value}'")


"""if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract text from PDF file')
    parser.add_argument('--filepath', required=True, help='Path to PDF file to extract text from')
    args = parser.parse_args()
    extract_text_from_pdf(args.filepath)"""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Read and modify PDF metadata')
    parser.add_argument('--filepath', required=True, help='Path to PDF file')
    args = parser.parse_args()
    add_metadata(args.filepath)