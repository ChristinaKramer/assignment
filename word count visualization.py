# This is a small program for counting and visualizing words per page in a PDF.
# Programmer: Christina Kramer and ChatGPT
# Date: From 2025-01-02 until 2025-01-10

import PyPDF2 # install and import PyPDF2 to process PDFs
import matplotlib.pyplot as plt # install and import matplotlib.pyplot to visualize word count

# -----------------------------
# function counting words
# -----------------------------

def count_word_in_pdf(pdf_path, keyword):
    word_counts = []  # array to store word counts for each page
    try:
        with open(pdf_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            for page_num, page in enumerate(reader.pages, start=1):  # loop to search every page
                text = page.extract_text() or ""
                word_count = text.lower().count(keyword.lower())
                word_counts.append(word_count)  # add count to array
                print(f"Page {page_num}: {word_count} occurrence(s)")  # inform user if count > 0
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return word_counts

#--------------------------------
# function visualization
#---------------------------------

def visualize_word_counts(word_counts, keyword):
    if not word_counts: 
        print(f"No occurrences of '{keyword}' found in the document.")
        return
    
    pages = range(1, len(word_counts) + 1)
    plt.figure(figsize=(10, 6))
    plt.bar(pages, word_counts, color='skyblue', width=0.6)
    plt.xlabel("Page Number")
    plt.ylabel("Word Count")
    plt.title(f"Occurrences of '{keyword}' Per Page")
    plt.xticks(pages, rotation=45)
    plt.tight_layout()
    plt.show()

# ----------------
# main program
# ----------------

def main():
    while True:  # loop to allow retrying if inputs are invalid
        pdf_path = input("Enter the path to the PDF file: ").strip()
        keyword = input("Enter the word to search: ").strip()
        
        if not pdf_path or not keyword:  
            print("Please provide both the PDF path and a keyword.")
            continue
        
        print("Processing the PDF...")
        word_counts = count_word_in_pdf(pdf_path, keyword)  # funtcion call
        
        if not word_counts:  # handle cases where the PDF might be invalid
            print("Failed to process the PDF. Please try again.")
            continue
        
        # function call to visualize results
        visualize_word_counts(word_counts, keyword)

        # end of program
