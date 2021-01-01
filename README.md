# Image2Text
The program extracts texts from an image and writes the excracted text into a file.

## Library Used
- [pytesseract](https://pypi.org/project/pytesseract/)
- [Pillow](https://pypi.org/project/Pillow/)
- [terresact-ocr](https://tesseract-ocr.github.io/tessdoc/Downloads.html)

## Usage
* Install the [`tesseract-ocr`](https://tesseract-ocr.github.io/tessdoc/Downloads.html) from the given location
* set the tesseract_cmd from the installed location
* in my case
  - pytesseract.pytesseract.tesseract_cmd = C:\Program Files (x86)\Tesseract-OCR\tesseract.exe
    
* run the program and choose an image file containing text
* the text will be extracted and stored in a **.txt** file

## Issues
Unable to extract imoji characters