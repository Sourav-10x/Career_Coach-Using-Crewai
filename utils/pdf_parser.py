def extract_text_from_pdf(file_path):
    import fitz  # PyMuPDF
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        page_text = page.get_text()
        print(" PAGE TEXT:\n", page_text[:300])  # ✅ Add this line
        text += page_text
    return text

