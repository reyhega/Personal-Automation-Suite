import os
import argparse
from datetime import datetime
from PyPDF2 import PdfReader, PdfWriter


def read_metadata(filepath):
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


def add_metadata(filepath, author, creator, producer, subject, title):
    reader = PdfReader(filepath)
    writer = PdfWriter()
    meta = reader.metadata
    num_pages = len(reader.pages)
    old_meta = {
        # "num_pages": len(reader.pages),
        "Author": meta.author,
        "Creator": meta.creator,
        "Producer": meta.producer,
        "Subject": meta.subject,
        "Title": meta.title,
    }
    
    # Add pages to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Add the metadata
    writer.add_metadata(
        {
            "/Author": author,
            "/Creator": creator,
            "/Producer": producer,
            "/Subject": subject,
            "/Title": title,
        }
    )

    # Save the new PDF to a file
    new_file = "resources/meta-pdf.pdf"
    with open(new_file, "wb") as f:
        writer.write(f)

    new_reader = PdfReader(new_file)
    new_meta = new_reader.metadata
    new_file_meta = {
        # "num_pages": len(new_reader.pages),
        "Author": new_meta.author,
        "Creator": new_meta.creator,
        "Producer": new_meta.producer,
        "Subject": new_meta.subject,
        "Title": new_meta.title,
    }

    print(f"✅ Succesfully created copy of file with following metadata:")
    print("---------------------------------------------------------------------------------------")
    print(f"Number of pages: {num_pages}")
    for key in old_meta:
        old_value = old_meta[key]
        new_value = new_file_meta[key]
        print(f"☑️ Set '{key}' from:  '{old_value}'   →   '{new_value}'")
    print("---------------------------------------------------------------------------------------")
    print(f"📁 File saved at location: '{new_file}'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Read and modify PDF metadata')
    parser.add_argument('--filepath', required=True, help='Path to PDF file')
    parser.add_argument('--read', action='store_const', const=read_metadata, help='Read metadata of PDF file')
    parser.add_argument('--add', action='store_const', const=add_metadata, help='Modify metadata of PDF file')
    args = parser.parse_args()

    if args.read:
        print("=======================================================================================")
        print(f"🔎 Here's the file's metadata:")
        print("---------------------------------------------------------------------------------------")
        read_metadata(args.filepath)
        print("---------------------------------------------------------------------------------------")
    elif args.add:
        print("=======================================================================================")
        print("📝 Please provide the following info (can be 'None')")
        print("---------------------------------------------------------------------------------------")
        i_author = input("Author: ")
        i_creator = input("Creator: ")
        i_producer = input("Producer: ")
        i_subject = input("Subject: ")
        i_title = input("Title: ")
        print("---------------------------------------------------------------------------------------")
        add_metadata(args.filepath, i_author, i_creator, i_producer, i_subject, i_title)
        print("---------------------------------------------------------------------------------------")