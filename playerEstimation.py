import sys
import gui
import tkinter as tk


def main():

    root = tk.Tk()
    app = gui.App(master=root)
    root.title("playerEstimation")
    root.geometry("580x580")

    app.mainloop()
    root.destroy()


if __name__ == "__main__":
    main()