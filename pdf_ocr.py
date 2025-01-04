import os
import pymupdf
from pathlib import Path

def extract_text_with_ocr(input_path, output_path, language="chi_sim", dpi=300):
    """Perform OCR on an image-only PDF and save the extracted text.
    
    Args:
        input_path (str): Path to input PDF file
        output_path (str): Path to save OCR output
        language (str): OCR language (default: chi_sim for Simplified Chinese)
        dpi (int): Resolution for OCR processing
    """
    try:
        # Get and print original file size
        original_size = os.path.getsize(input_path)
        print(f"\nProcessing: {input_path}")
        print(f"Original size: {original_size/1024:.1f}KB")
        
        # Open the original PDF
        doc = pymupdf.open(input_path)
        
        # Create a text file or new PDF for OCR output
        if output_path.endswith(".txt"):
            text_output = ""
        else:
            new_doc = pymupdf.open()
        
        # Iterate through each page
        for page_num in range(len(doc)):
            print(f"Processing page {page_num + 1}...")
            page = doc.load_page(page_num)
            
            try:
                textpage = page.get_textpage_ocr(
                    flags=3, 
                    language=language, 
                    dpi=dpi, 
                    full=False, 
                    tessdata="/usr/local/Cellar/tesseract/5.5.0/share/tessdata"
                )
                ocr_text = textpage.extractText()
                print(f"OCR completed for page {page_num + 1}.")
            except Exception as e:
                print(f"Error performing OCR on page {page_num + 1}: {str(e)}")
                continue
            
            if output_path.endswith(".txt"):
                # Append OCR text to the output
                text_output += ocr_text + "\n"
            else:
                # Create a new page in the new PDF
                new_page = new_doc.new_page(width=page.rect.width, height=page.rect.height)
                
                # Insert OCR text into the new page
                new_page.insert_text((50, 50), ocr_text, fontsize=12, fontname="helv")
        
        # Save the OCR output
        if output_path.endswith(".txt"):
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(text_output)
        else:
            new_doc.save(output_path)
            new_doc.close()
        
        # Close the original document
        doc.close()
        
        # Get OCR output size and calculate ratio
        ocr_size = os.path.getsize(output_path)
        ratio = (1 - ocr_size / original_size) * 100
        
        print(f"OCR output size: {ocr_size/1024:.1f}KB")
        print(f"Compression ratio: {ratio:.1f}%")
        
        return True
        
    except Exception as e:
        print(f"Error performing OCR on {input_path}: {str(e)}")
        return False
    