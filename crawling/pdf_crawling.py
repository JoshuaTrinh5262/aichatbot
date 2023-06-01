from pdfquery import PDFQuery

pdf = PDFQuery('./crawling/data/gold-price.pdf')
pdf.load()

# Use CSS-like selectors to locate the elements
text_elements = pdf.pq('LTTextLineHorizontal')

# Extract the text from the elements
text = [t.text for t in text_elements]

with open("./crawling/data/gold-price.txt", "a", encoding="utf-8") as file:
    for line in text:
        file.write(line + "\n")

print(text)