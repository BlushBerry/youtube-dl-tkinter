from tkinter import *

import os

root = Tk()
root.title("youtube-dl-tkinter")

class App:
  url = Label(root, text="Youtube URL: ").grid(row=0)
  e1 = Entry(root)
  e1.grid(row=0, column=1)
  def __init__(self, master):
    frame = Frame(master)
    frame.grid()

    self.command = Button(frame,
                         text="Download",
                         command=self.download)
    self.command.grid(column=1, row=0)

  def download(self):
    os.system("youtube-dl --extract-audio --audio-format mp3 {}".format(self.e1.get()))
    print(self.e1.get())

app = App(root)
root.mainloop()