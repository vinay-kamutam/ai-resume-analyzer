from PyPDF2 import PdfReader


def extract_resume_data(pdf_path: str):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return {
        "pages": len(reader.pages),
        "characters": len(text),
        "resume_text": text
    }