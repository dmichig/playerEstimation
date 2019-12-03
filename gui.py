import tkinter as tk
import os
import sys

class App(tk.Frame):


    def get_value(self):

        self.first_team = self.first_team_entry.get()
        self.second_team = self.second_team_entry.get()


    def estimate_rate(self):
        pass


    def estimate_price(self):
        pass

    def create_widgets_for_gk(self):
        pass



    def create_widgets(self):
        self.est_rate_buttton = tk.Button(text="Estimate overall rate", command=self.estimate_rate, height=0, width=15).grid(row=0, column=0)
        self.est_price_buttton = tk.Button(text="Estimate price", command=self.estimate_price, height=0, width=15).grid(row=0, column=1)

        self.place_label = tk.Label(text="Miejsce").grid(row=1, column=0)
        self.player_label = tk.Label(text="Gracz").grid(row=1, column=1)
        self.points_label = tk.Label(text="Punkty").grid(row=1, column=2)
        self.win_label = tk.Label(text="Wygrane").grid(row=1, column=3)
        self.draw_label = tk.Label(text="Remisy").grid(row=1, column=4)
        self.lose_label = tk.Label(text="Przegrane").grid(row=1, column=5)
        self.goals_ad_label = tk.Label(text="Gole zd.").grid(row=1, column=6)
        self.goals_lo_label = tk.Label(text="Gole st.").grid(row=1, column=7)

    def ask_quit(self):
        self.root.quit()

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master
        self.root.protocol("WM_DELETE_WINDOW", self.ask_quit)

        self.create_widgets()


