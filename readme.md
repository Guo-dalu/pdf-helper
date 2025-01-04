# PDF OCR Text Extraction

This Python script extracts text from image-based PDFs using Optical Character Recognition (OCR). It supports multiple languages (default: Simplified Chinese) and saves the extracted text as `.txt` files.

---

## Requirements

- Python 3.7+
- `pymupdf` (PyMuPDF)
- Tesseract OCR (installed separately)

### Installation

1. Install Python dependencies:

   ```bash
   pip install pymupdf
   ```

2. Install Tesseract OCR:

   - macOS (Homebrew):
     ```bash
     brew install tesseract
     ```
   - Linux (Debian/Ubuntu):
     ```bash
     sudo apt-get install tesseract-ocr
     ```

3. Download Tesseract language data (e.g., `chi_sim` for Simplified Chinese) and place it in the Tesseract `tessdata` directory.

---

## Usage

1. Place your PDF files in the input directory (default: `/Users/xxxx/Documents/pdfs`).
2. Run the script:
   ```bash
   python main.py
   ```
3. Extracted text will be saved in the output directory (default: `/Users/xxxx/Documents/ocr_output`).

---

## Customization

- Change input/output directories in `main.py`.
- Modify the `language` and `dpi` parameters in the `extract_text_with_ocr` function.

---

## Example

### Input Directory

```
/Users/xxxx/Documents/pdfs/
    document1.pdf
    document2.pdf
```

### Output Directory

```
/Users/xxxx/Documents/ocr_output/
    ocr_document1.txt
    ocr_document2.txt
```

---

## Notes

- Ensure input PDFs are image-based (scanned documents).
- Processing time depends on PDF size and system performance.
