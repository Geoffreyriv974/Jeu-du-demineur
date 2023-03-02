import tkinter as tk
import easy_mode
import normal_mode
import hard_mode

easy = tk.PhotoImage(file="image/Pioche_facile.png")
normal = tk.PhotoImage(file="image/Pioche_normal.png")
hardcore = tk.PhotoImage(file="image/Pioche_difficile.png")

def choice_dif():
    dif_windows = tk.Toplevel(bg="#B1A8A8")
    dif_windows.attributes('-fullscreen', True)

    def mode1():
        easy_mode.easy()

    def mode2():
        normal_mode.normal()

    def mode3():
        hard_mode.hard()

    btn_easy = tk.Button(dif_windows, text="FACILE", relief="raised", bg="#B1A8A8", fg="blue", borderwidth=5, font=("Retro Gaming", 25), command=mode1)
    btn_easy.place(x=200, y=550)
    btn_normal = tk.Button(dif_windows, text="NORMAL", relief="raised", bg="#B1A8A8", fg="blue", borderwidth=5, font=("Retro Gaming", 25), command=mode2)
    btn_normal.place(x=670, y=550)
    btn_hard = tk.Button(dif_windows, text="DIFFICILE", pady=11, relief="raised", bg="#B1A8A8", fg="blue", borderwidth=5, font=("Retro Gaming", 17), command=mode3)
    btn_hard.place(x=1100, y=550)

    def exit_diff():
        dif_windows.destroy()

    btn_exit = tk.Button(dif_windows, text="QUITTER", relief="raised", pady=11, bg="#B1A8A8", fg="blue", borderwidth=5, font=("Retro Gaming", 18), command=exit_diff)
    btn_exit.place(x=680, y=700)

    pche = tk.Label(dif_windows, image=easy, bg="#B1A8A8")
    pche.place(x=100, y=100)

    pchn = tk.Label(dif_windows, image=normal, bg="#B1A8A8")
    pchn.place(x=550, y=100)

    pchd = tk.Label(dif_windows, image=hardcore, bg="#B1A8A8")
    pchd.place(x=1000, y=100)