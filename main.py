from tkinter import *
from tkinter import messagebox as mb
import sys
import PIL
import customtkinter
from ctypes import *
from OpenFileDialoge import OpenFileDialog
from Quicksort import QuickSort
from stolbiki import Stolbiki


def SliderEvent(value):
    global q
    q = value


def kl():
    global z
    z1 = OpenFileDialog(NormalAnimateButton, path)
    if z1.return_path():
        z = z1


def value():
    if "q" in globals():
        return int(q)
    return 6


def PlayPause():
    if play_pause.cget("image") == pause:
        play_pause.configure(image=play)
        speed.configure(state="disabled")
        label_min.configure(state="disabled")
        label_max.configure(state="disabled")
        back.configure(state="normal")
        next.configure(state="normal")
    else:
        play_pause.configure(image=pause)
        speed.configure(state="normal")
        label_min.configure(state="normal")
        label_max.configure(state="normal")
        back.configure(state="disabled")
        next.configure(state="disabled")
        move()


def sled():
    global jk, hist
    if jk < len(hist):
        if jk == len(hist) - 2:
            jk += 1
            progress.set(jk / (len(hist) - 1))
            next.configure(state="disabled")
        else:
            jk += 1
            progress.set(jk / (len(hist) - 1))
        if jk == 1:
            back.configure(state="normal")
        canvas.delete("all")
        for id, el in enumerate(hist[jk]):
            x1 = round(width / len(hist[jk]) * id)
            y1 = round(height - el.return_number() / maxim * height)
            x2 = x1 + width / len(hist[jk])
            y2 = height - 1
            canvas.create_rectangle(x1, y1, x2, y2, fill="#d1d1d1")


def prev():
    global jk, hist
    if jk >= 0:
        if jk == 1:
            jk -= 1
            progress.set(jk / (len(hist) - 1))
            back.configure(state="disabled")
        else:
            jk -= 1
            progress.set(jk / (len(hist) - 1))
        if jk == len(hist) - 2:
            next.configure(state="normal")
        canvas.delete("all")
        for id, el in enumerate(hist[jk]):
            x1 = round(width / len(hist[jk]) * id)
            y1 = round(height - el.return_number() / maxim * height)
            x2 = x1 + width / len(hist[jk])
            y2 = height - 1
            canvas.create_rectangle(x1, y1, x2, y2, fill="#d1d1d1")


def Animate():
    m = z.return_path()
    m = str(m)[25:-29]
    f = open(m, encoding="utf-8")
    f = f.readlines()
    f = f[0].replace("\n", "")
    f = f.split(", ")
    if len(f) > windll.user32.GetSystemMetrics(0) // 2 - 1:
        mb.showerror(
            "Error",
            f"The maximum number of numbers in the file is {windll.user32.GetSystemMetrics(0) // 2 - 1}")
    elif len(f) < 2:
        mb.showerror(
            "Error",
            f"The minimum number of numbers in the file is 2")
    else:
        animate = Toplevel()
        animate.attributes("-fullscreen", True)
        animate.resizable = (False, False)
        animate.title("Quick sort animation")
        animate.configure(bg="#282C34")
        for i in range(15):
            animate.rowconfigure(i, weight=1)
        for i in range(10):
            animate.columnconfigure(i, weight=1)
        global next, back
        arrow_back = customtkinter.CTkImage(light_image=PIL.Image.open("arrow_back.png"),
                                            dark_image=PIL.Image.open("arrow_back.png"),
                                            size=(30, 55))
        arrow_forward = customtkinter.CTkImage(light_image=PIL.Image.open("arrow_forward.png"),
                                               dark_image=PIL.Image.open("arrow_forward.png"),
                                               size=(30, 55))
        next = customtkinter.CTkButton(animate, width=80, height=50, fg_color="#3E4149", corner_radius=12,
                                       text_color="#d1d1d1", hover_color='#31343A', hover=True, image=arrow_forward,
                                       text="", state="disabled", command=sled)
        back = customtkinter.CTkButton(animate, image=arrow_back, width=80, height=50, fg_color="#3E4149",
                                       corner_radius=12, text_color="#d1d1d1", hover_color='#31343A', hover=True,
                                       text="", state="disabled", command=prev)
        next.grid(row=15, column=7, pady=(0, 5), padx=(10, 0))
        back.grid(row=15, column=6, pady=(0, 5), padx=(20, 0))
        global close, progress
        close = customtkinter.CTkButton(animate, text="Close", font=("Comfortaa", 35),
                                        command=lambda: animate.destroy(), width=150, height=50, fg_color="#3E4149",
                                        corner_radius=12, text_color="#d1d1d1", hover_color='#31343A', hover=True)
        close.grid(row=15, column=10, pady=(0, 10), padx=(0, 10))
        global play
        play = customtkinter.CTkImage(light_image=PIL.Image.open("play.png"),
                                      dark_image=PIL.Image.open("play.png"),
                                      size=(65, 65))
        global pause
        pause = customtkinter.CTkImage(light_image=PIL.Image.open("pause.png"),
                                       dark_image=PIL.Image.open("pause.png"),
                                       size=(65, 65))
        global play_pause, speed, label_min, label_max, canvas
        play_pause = customtkinter.CTkButton(animate, width=80, height=50, fg_color="#3E4149", corner_radius=12,
                                             text_color="#d1d1d1", hover_color='#31343A', hover=True, text="",
                                             image=pause, command=PlayPause)
        play_pause.grid(row=15, column=3, pady=(0, 5))
        speed = customtkinter.CTkSlider(animate, from_=1, to=10, command=SliderEvent, number_of_steps=9,
                                        button_color="black", button_hover_color='#31343A')
        label_min = customtkinter.CTkLabel(animate, text="1", font=("Comfortaa", 20), text_color="#d1d1d1",
                                           bg_color="#282C34")
        label_max = customtkinter.CTkLabel(animate, text="10", font=("Comfortaa", 20), text_color="#d1d1d1",
                                           bg_color="#282C34")
        label_max.grid(row=15, column=4, sticky="ne", padx=(0, 30), pady=(0, 45))
        label_min.grid(row=15, column=4, sticky="nw", padx=(100, 0))
        speed.grid(row=15, column=4, sticky="s", pady=(0, 25), padx=(65, 0))
        podpis = customtkinter.CTkLabel(animate, text="Auto mode", font=("Comfortaa", 30), fg_color="#282C34",
                                        text_color="#d1d1d1")
        podpis.grid(row=15, column=1, pady=(0, 13), sticky="w", columnspan=10, padx=(20, 0))
        progress = customtkinter.CTkProgressBar(animate, width=animate.winfo_screenwidth(), progress_color="#d1d1d1", fg_color="#282C34")
        progress.set(0)
        global width, height, maxim
        progress.grid(row=0, column=0, columnspan=11, sticky='n')
        canvas = Canvas(animate, width=animate.winfo_screenwidth(), height=animate.winfo_screenheight() // 15 * 14 - 20,
                        bd=0, highlightthickness=0, relief='ridge', bg="#282C34")
        canvas.grid(column=0, row=0, columnspan=11, rowspan=14, sticky="n", pady=(10, 0))
        f = list(map(int, f))
        maxim = max(f)
        height = animate.winfo_screenheight() // 15 * 14 - 20
        width = animate.winfo_screenwidth()
        global stolbiki
        stolbiki = []
        for id, el in enumerate(f):
            x1 = round(width / len(f) * id)
            y1 = round(height - el / maxim * height)
            x2 = x1 + width / len(f)
            y2 = height - 1
            canvas.create_rectangle(x1, y1, x2, y2, fill="#d1d1d1")
            stolbiki.append(Stolbiki(id, el, x1, y1, x2, y2))
        global g, hist
        g = QuickSort(stolbiki)
        g.quick_sort(stolbiki)
        hist = g.return_history()
        global jk
        jk = 0
        hm = 0
        while hm < len(hist) - 1:
            zkl = [gm.return_number() for gm in hist[hm]]
            ckl = [gm.return_number() for gm in hist[hm + 1]]
            if ckl == zkl:
                hist.remove(hist[hm + 1])
            else:
                hm += 1
        global move

        def move():
            if play_pause.cget("image") == pause:
                global jk
                canvas.delete("all")
                for id, el in enumerate(hist[jk]):
                    x1 = round(width / len(hist[jk]) * id)
                    y1 = round(height - el.return_number() / maxim * height)
                    x2 = x1 + width / len(hist[jk])
                    y2 = height - 1
                    canvas.create_rectangle(x1, y1, x2, y2, fill="#d1d1d1")
                if jk < len(hist) - 1:
                    jk += 1
                    animate.after(int(((11 - value()) ** 2) * 5), move)
                else:
                    PlayPause()
                progress.set(jk / (len(hist) - 1))
        move()
        animate.mainloop()


def NormalAnimateButton():
    animate.configure(state="normal")


def DisableAnimateButton():
    animate.configure(state="disabled")


def Exit():
    sys.exit()


def About():
    about = Tk()
    about.geometry('900x650')
    about.resizable(False, False)
    about.title("About the developer")
    about.configure(bg="#282C34")
    about.columnconfigure(0, weight=1)
    label = Label(about, text="Made by a student of AltSTU", font=("Comfortaa", 30), bg="#282C34", fg="#d1d1d1")
    label1 = Label(about, text="PIE-21 groups", font=("Comfortaa", 30), bg="#282C34", fg="#d1d1d1")
    label2 = Label(about, text="Novoselov Petr", font=("Comfortaa", 30), bg="#282C34", fg="#d1d1d1")
    for i in range(7):
        about.rowconfigure(i, weight=1)
    label.grid(column=0, row=2, rowspan=1)
    label1.grid(column=0, row=3, rowspan=1)
    label2.grid(column=0, row=4, rowspan=1)
    about.mainloop()


window = Tk()
window.geometry('1200x400')
window.resizable(False, False)
window.title("Quick sort visualization")
window.configure(bg="#282C34")
for i in range(4):
    window.columnconfigure(i, weight=1)
for i in range(3):
    window.rowconfigure(i, weight=1)
window.rowconfigure(0, weight=1)
file = customtkinter.CTkButton(window, text="File", command=kl, font=("Comfortaa", 45), width=250, height=110,
                               fg_color="#3E4149", corner_radius=12, text_color="#d1d1d1", hover_color='#31343A',
                               hover=True)
animate = customtkinter.CTkButton(window, text="Animate", state="disabled", font=("Comfortaa", 45), command=Animate,
                                  width=250, height=110, fg_color="#3E4149", corner_radius=12, text_color="#d1d1d1",
                                  hover_color='#31343A', hover=True)
about = customtkinter.CTkButton(window, text="About", font=("Comfortaa", 45), command=About, width=250, height=110,
                                fg_color="#3E4149", corner_radius=12, text_color="#d1d1d1", hover_color='#31343A',
                                hover=True)
exit = customtkinter.CTkButton(window, text="Exit", font=("Comfortaa", 45), command=Exit, width=250, height=110,
                               fg_color="#3E4149", corner_radius=12, text_color="#d1d1d1", hover_color='#31343A',
                               hover=True)
file.grid(column=0, row=1, columnspan=1, pady=(35, 0), padx=(20, 0))
animate.grid(column=1, row=1, columnspan=1, pady=(35, 0))
about.grid(column=2, row=1, columnspan=1, pady=(35, 0))
exit.grid(column=3, row=1, columnspan=1, pady=(35, 0), padx=(0, 20))
path = Label(font=("Comfortaa", 15), bg="#282C34", fg="#d1d1d1", justify="center")
path.grid(row=2, columnspan=4)
window.mainloop()
