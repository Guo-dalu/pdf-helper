from pathlib import Path
from pdf_ocr import extract_text_with_ocr

def main():
    # Specify the input directory
    input_dir = Path("/Users/xxxx/Documents/pdfs")
    output_dir = Path("/Users/xxxx/Documents/ocr_output")
    output_dir.mkdir(exist_ok=True)
    
    # Get all PDF files
    pdf_files = list(input_dir.glob("*.pdf"))
    
    if not pdf_files:
        print("No PDF files found in the specified directory.")
        return
    
    print(f"Found {len(pdf_files)} PDF files to process.\n")
    
    # Process each PDF file
    successful = 0
    for pdf_file in pdf_files:
        output_path = output_dir / f"ocr_{pdf_file.stem}.txt"
        if extract_text_with_ocr(str(pdf_file), str(output_path), language="chi_sim", dpi=300):
            successful += 1
            
    print(f"\nOCR completed!")
    print(f"Successfully processed {successful} out of {len(pdf_files)} files")
    print(f"OCR output files are saved in: {output_dir}")

if __name__ == "__main__":
    main() 