import tkinter.filedialog

class OpenFileDialog:
    def __init__(self, funk, path):
        self.p = tkinter.filedialog.askopenfile()
        self.funk = funk
        self.path = path
        if self.p:
            self.funk()
            put = str(self.p)[25:-29]
            path.configure(text=put)


    def return_path(self):
        return self.p
