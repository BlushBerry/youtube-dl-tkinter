from tkinter import *
import os
from tkinter.filedialog import askdirectory

# Initialize TK and set it as the root window
root = Tk()
root.title("youtube-dl-tkinter")


class App:
    url = Label(root, text="Youtube URL: ").grid(row=2)
    path = Label(root, text="Download Path: ").grid(row=1)
    chosenfolder = StringVar()
    e1 = Entry(root)
    e1.grid(row=2, column=1)
    e2 = Entry(root, textvariable=chosenfolder)
    e2.grid(row=1, column=1)
    queue = Listbox(root)
    downloadqueue = []

    # Initialize
    def __init__(self, master):

        # frame = Frame(master)
        # frame.grid()

        self.queue.grid(column=0, row=0, columnspan=3, sticky=W+E)
        #queue.grid(fill=BOTH, expand=1)

        # Create Add Button
        self.command = Button(master, text="Add", command=self.add)
        self.command.grid(column=2, row=2)

        # Create File Path Button :v
        self.command = Button(master, text="...", command=self.pickfolder)
        self.command.grid(column=2, row=1)

        # Create Download Button
        self.command = Button(master,
                              text="Download",
                              command=self.download)
        self.command.grid(column=1, row=3)


    # This function uses youtube-dl to extract mp3 audio from a youtube url and formats in our entry text in e1
    def pickfolder(self):
        print("youtube-dl-tkinter: Choosing File Destination")
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        filename = askdirectory()  # show an "Open" dialog box and return the path to the selected file
        self.chosenfolder.set(filename)

    def download(self):
        print("youtube-dl-tkinter: Initializing download of url {} to destination {}".format(self.e1.get(),
                                                                                             self.chosenfolder.get()))
        while not self.downloadqueue == [] :
            os.system(
                "youtube-dl -o '{}/%(title)s.%(ext)s' --extract-audio --audio-format mp3 {}".format(self.chosenfolder.get(),
                                                                                                self.downloadqueue.pop()))
    def add(self):
        print("youtube-dl-tkinter: Youtube Url {} Added to queue!".format(self.e1.get()))
        self.queue.insert(END, self.e1.get())
        self.downloadqueue.append(self.e1.get())

app = App(root)
root.mainloop()
