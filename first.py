from pdf2docx import Converter

pdf="pdf-file.pdf"
word="file.docx"

cv=Converter(pdf)
cv.convert(word)

cv.close()


#pip install pdf2docx