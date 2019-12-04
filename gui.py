import tkinter as tk
import fileRead
from sklearn.linear_model import LinearRegression

class App(tk.Frame):

    def estimate_gk(self):
        self.gk_diving = int(self.gk_diving_entry.get())
        self.gk_handling = int(self.gk_handling_entry.get())
        self.gk_kicking = int(self.gk_kicking_entry.get())
        self.gk_reflexes = int(self.gk_reflexes_entry.get())
        self.gk_speed = int(self.gk_speed_entry.get())
        self.gk_positioning = int(self.gk_positioning_entry.get())

        if ((self.gk_diving > 0 and self.gk_diving < 100) and
            (self.gk_handling > 0 and self.gk_handling < 100) and
            (self.gk_kicking > 0 and self.gk_kicking < 100) and
            (self.gk_reflexes > 0 and self.gk_reflexes < 100) and
            (self.gk_speed > 0 and self.gk_speed < 100) and
            (self.gk_positioning > 0 and self.gk_positioning < 100)):

                self.entered_values = [[self.gk_diving, self.gk_handling, self.gk_kicking, self.gk_reflexes,
                                        self.gk_speed, self.gk_positioning]]

                self.overall_predictor = LinearRegression(n_jobs=-1)
                self.value_predictor = LinearRegression(n_jobs=-1)

                self.overall_predictor.fit(X=self.fifa20.goalkeepers, y=self.fifa20.goalkeepers_overalls)
                self.value_predictor.fit(X=self.fifa20.goalkeepers, y=self.fifa20.goalkeepers_values)

                self.estimated_overall = self.overall_predictor.predict(X=self.entered_values)
                self.estimated_value = self.value_predictor.predict(X=self.entered_values)

                self.estimated_overall_label = tk.Label(text="Estimated overall rate: {}".format(int(self.estimated_overall))).grid(row=10, column=1)
                self.estimated_value_label = tk.Label(text="Estimated player value (in EUR): {}".format(int(self.estimated_value))).grid(row=11, column=1)

        else:
            self.new_window = tk.Toplevel(master=self)
            self.new_window.geometry("300x300")
            self.new_window.title("ERROR!!!")

            self.error_label = tk.Label(master=self.new_window, text='Entered value must be in range 1 to 99!').grid(row=0, column=0)
            self.quit_button = tk.Button(master=self.new_window, text='Close window', command=self.new_window.destroy).grid(row=1, column=0)

    def estimate_fp(self):
        self.fp_pace = int(self.fp_pace_entry.get())
        self.fp_shooting = int(self.fp_shooting_entry.get())
        self.fp_passing = int(self.fp_passing_entry.get())
        self.fp_dribbling = int(self.fp_dribbling_entry.get())
        self.fp_defending = int(self.fp_defending_entry.get())
        self.fp_physic = int(self.fp_physic_entry.get())

        if ((self.fp_pace > 0 and self.fp_pace < 100) and
                (self.fp_shooting > 0 and self.fp_shooting < 100) and
                (self.fp_passing > 0 and self.fp_passing < 100) and
                (self.fp_dribbling > 0 and self.fp_dribbling < 100) and
                (self.fp_defending > 0 and self.fp_defending < 100) and
                (self.fp_physic > 0 and self.fp_physic < 100)):

            self.entered_values = [[self.fp_pace, self.fp_shooting, self.fp_passing, self.fp_dribbling,
                                    self.fp_defending, self.fp_physic]]

            self.overall_predictor = LinearRegression(n_jobs=-1)
            self.value_predictor = LinearRegression(n_jobs=-1)

            self.overall_predictor.fit(X=self.fifa20.field_players, y=self.fifa20.field_players_overalls)
            self.value_predictor.fit(X=self.fifa20.field_players, y=self.fifa20.field_players_values)

            self.estimated_overall = self.overall_predictor.predict(X=self.entered_values)
            self.estimated_value = self.value_predictor.predict(X=self.entered_values)

            self.estimated_overall_label = tk.Label(
                text="Estimated overall rate: {}".format(int(self.estimated_overall))).grid(row=10, column=1)
            self.estimated_value_label = tk.Label(
                text="Estimated player value (in EUR): {}".format(int(self.estimated_value))).grid(row=11, column=1)

        else:
            self.new_window = tk.Toplevel(master=self)
            self.new_window.geometry("300x300")
            self.new_window.title("ERROR!!!")

            self.error_label = tk.Label(master=self.new_window, text='Entered value must be in range 1 to 99!').grid(
                row=0, column=0)
            self.quit_button = tk.Button(master=self.new_window, text='Close window',
                                         command=self.new_window.destroy).grid(row=1, column=0)

    def create_widgets_for_gk(self):
        self.dummy_space3 = tk.Label(text='  ').grid(row=2, column=0)

        self.gk_diving_label = tk.Label(text='Goalkeeper diving: ', height=0, width=20).grid(row=3, column=1)
        self.gk_diving_entry = tk.Entry()
        self.gk_diving_entry.grid(row=3, column=2)

        self.gk_handling_label = tk.Label(text='Goalkeeper handling: ', height=0, width=20).grid(row=4, column=1)
        self.gk_handling_entry = tk.Entry()
        self.gk_handling_entry.grid(row=4, column=2)

        self.gk_kicking_label = tk.Label(text='Goalkeeper kicking: ', height=0, width=20).grid(row=5, column=1)
        self.gk_kicking_entry = tk.Entry()
        self.gk_kicking_entry.grid(row=5, column=2)

        self.gk_reflexes_label = tk.Label(text='Goalkeeper reflexes: ', height=0, width=20).grid(row=6, column=1)
        self.gk_reflexes_entry = tk.Entry()
        self.gk_reflexes_entry.grid(row=6, column=2)

        self.gk_speed_label = tk.Label(text='Goalkeeper speed: ', height=0, width=20).grid(row=7, column=1)
        self.gk_speed_entry = tk.Entry()
        self.gk_speed_entry.grid(row=7, column=2)

        self.gk_positioning_label = tk.Label(text='Goalkeeper positioning: ', height=0, width=20).grid(row=8, column=1)
        self.gk_positioning_entry = tk.Entry()
        self.gk_positioning_entry.grid(row=8, column=2)

        self.estimate_button = tk.Button(text="Estimate!", command=self.estimate_gk, height=0, width=15).grid(row=9,
                                                                                                              column=2)

    def create_widgets_for_fp(self):
        self.dummy_space3 = tk.Label(text='  ').grid(row=2, column=0)

        self.fp_pace_label = tk.Label(text='Player pace: ', height=0, width=20).grid(row=3, column=1)
        self.fp_pace_entry = tk.Entry()
        self.fp_pace_entry.grid(row=3, column=2)

        self.fp_shooting_label = tk.Label(text='Player shooting: ', height=0, width=20).grid(row=4, column=1)
        self.fp_shooting_entry = tk.Entry()
        self.fp_shooting_entry.grid(row=4, column=2)

        self.fp_passing_label = tk.Label(text='Player passing: ', height=0, width=20).grid(row=5, column=1)
        self.fp_passing_entry = tk.Entry()
        self.fp_passing_entry.grid(row=5, column=2)

        self.fp_dribbling_label = tk.Label(text='Player dribbling: ', height=0, width=20).grid(row=6, column=1)
        self.fp_dribbling_entry = tk.Entry()
        self.fp_dribbling_entry.grid(row=6, column=2)

        self.fp_defending_label = tk.Label(text='Player defending: ', height=0, width=20).grid(row=7, column=1)
        self.fp_defending_entry = tk.Entry()
        self.fp_defending_entry.grid(row=7, column=2)

        self.fp_physic_label = tk.Label(text='Player physic: ', height=0, width=20).grid(row=8, column=1)
        self.fp_physic_entry = tk.Entry()
        self.fp_physic_entry.grid(row=8, column=2)

        self.estimate_button = tk.Button(text="Estimate!", command=self.estimate_fp, height=0, width=15).grid(row=9,
                                                                                                              column=2)


    def create_widgets(self):
        self.dummy_space1 = tk.Label(text='  ').grid(row=1, column=0)
        self.dummy_space2 = tk.Label(text='     ').grid(row=1, column=3)

        self.est_rate_buttton = tk.Button(text="Estimate goalkeeper",
                                          command=self.create_widgets_for_gk, height=0, width=15).grid(row=1, column=1)
        self.est_price_buttton = tk.Button(text="Estimate field player",
                                           command=self.create_widgets_for_fp, height=0, width=15).grid(row=1, column=4)

    def ask_quit(self):
        self.root.quit()

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master
        self.root.protocol("WM_DELETE_WINDOW", self.ask_quit)

        self.fifa20 = fileRead.fileRead()

        self.create_widgets()


