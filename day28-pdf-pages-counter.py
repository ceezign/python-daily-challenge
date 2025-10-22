## PDF Page Counter
# it reads the pdf pages in your root directory

import os
from PyPDF2 import PdfReader

def count_pdf_pages():
    # Use the current directory (where the script is located)
    folder_path = os.getcwd()
    total_pages = 0

    print(f"\n📂 Scanning current directory: {folder_path}\n")

    # Loop through all PDF files in the current directory
    pdf_files = [file for file in os.listdir(folder_path) if file.lower().endswith(".pdf")]

    if not pdf_files:
        print("⚠️ No PDF files found in this directory.")
        return

    for filename in pdf_files:
        file_path = os.path.join(folder_path, filename)
        try:
            with open(file_path, "rb") as pdf_file:
                reader = PdfReader(pdf_file)
                num_pages = len(reader.pages)
                total_pages += num_pages
                print(f"📘 {filename}: {num_pages} pages")
        except Exception as e:
            print(f"⚠️ Could not read {filename}: {e}")

    print("\n---------------------------------")
    print(f"📊 Total pages across all PDFs: {total_pages}")
    print("---------------------------------\n")


if __name__ == "__main__":
    count_pdf_pages()