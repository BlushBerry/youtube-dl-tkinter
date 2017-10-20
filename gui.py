from tkinter import *
import os

#Initialize TK and set it as the root window
root = Tk()
root.title("youtube-dl-tkinter")

class App:
  url = Label(root, text="Youtube URL: ").grid(row=0)
  e1 = Entry(root)
  e1.grid(row=0, column=1)
  
  #Initialize
  def __init__(self, master):
    frame = Frame(master)
    frame.grid()
    
    #Create Download Button
    self.command = Button(frame,
                         text="Download",
                         command=self.download)
    self.command.grid(column=1, row=0)

  #This function uses youtube-dl to extract mp3 audio from a youtube url and formats in our entry text in e1
  def download(self):
    os.system("youtube-dl --extract-audio --audio-format mp3 {}".format(self.e1.get()))
    print(self.e1.get())

app = App(root)
root.mainloop()