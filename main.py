# This is a sample Python script.
from tkinter import *
from tkinter import filedialog
from PIL import Image
import pytesseract
from pytesseract import image_to_string


def convert(img_path):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
    txt = image_to_string(Image.open(img_path))
    filename = img_path.split('/')[-1].split('.')[0]
    f = open(str(filename)+'.txt', "w+", encoding="utf-8")
    f.write(txt)
    f.close()


def browse_files():
    try:
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=(("PNG files",
                                                          "*.png*"),
                                                         ("All files",
                                                          "*.*")))

        label_file_explorer.configure(text="File Opened: " + filename)
        convert(filename)

    except ValueError:
        print('Some Error Occurred...')


if __name__ == '__main__':
    window = Tk()
    window.title('File Explorer')
    window.geometry("700x200")
    window.config(background="white")
    label_file_explorer = Label(window,
                                text="File Explorer using Tkinter",
                                width=100, height=4,
                                fg="blue")
    button_explore = Button(window,
                            text="Browse Files",
                            command=browse_files)
    button_exit = Button(window,
                         text="Exit",
                         command=exit)
    label_file_explorer.grid(column=1, row=1)
    button_explore.grid(column=1, row=2)
    button_exit.grid(column=1, row=3)
    window.mainloop()
