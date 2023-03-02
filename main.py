import tkinter as tk
import pygame

pygame.mixer.init()
pygame.mixer.music.load("musique_de_fond.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

root = tk.Tk()
root.attributes('-fullscreen', True)
root.config(bg="#B1A8A8")

pioche_droite = tk.PhotoImage(file="image/Pioche_en_diamant_droite.png")
pioche_gauche = tk.PhotoImage(file="image/Pioche_en_diamant_gauche.png")

pchd = tk.Label(root, image=pioche_droite, bg="#B1A8A8")
pchd.place(x=1000, y=100)

pchg = tk.Label(root, image=pioche_gauche, bg="#B1A8A8")
pchg.place(x=100, y=100)

def exit():
    root.destroy()

def display_rules():
    import rules
    rules.rules()

def start_diff():
    import difficulty
    difficulty.choice_dif()

name = tk.Label(root, text="DEMINEUR", fg="blue", bg="#B1A8A8", font=("Retro Gaming", 50))
name.pack(anchor="s", ipady=100)

btn_game = tk.Button(root, text="JOUER", relief="raised", bg="#B1A8A8", fg="blue", borderwidth=5, font=("Retro Gaming", 25), command=start_diff)
btn_game.place(x=585, y=310)

btn_exit = tk.Button(root, text="QUITTER", pady=11, relief="raised", bg="#B1A8A8", fg="blue", borderwidth=5, font=("Retro Gaming", 18), command=exit)
btn_exit.place(x=750, y=310)

btn_rules = tk.Button(root, text="RÉGLES", relief="raised", bg="#B1A8A8", fg="blue", borderwidth=5, font=("Retro Gaming", 25), command=display_rules)
btn_rules.place(x=655, y=388)

sign = tk.Label(root, text="By : Geoffrey Riviere", bg="#B1A8A8", fg="white", font=("retro Gaming", 10))
sign.place(x=670, y=700)

def activate():
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
    act.config(relief="sunken")
    desact.config(relief="raised")

def desactivate():
    pygame.mixer.music.stop()
    act.config(relief="raised")
    desact.config(relief="sunken")

photo_activate = tk.PhotoImage(file="image/activer.png")
photo_desactivate = tk.PhotoImage(file="image/desactiver.png")

frame = tk.Frame(root, bg="#B1A8A8")
frame.pack(pady=250, ipadx=17)

act = tk.Button(frame, relief="sunken", bg="#B1A8A8", fg="blue", borderwidth=5, padx=20, pady=13, image=photo_activate, command=activate)
act.pack(side=tk.LEFT)
desact = tk.Button(frame, relief="raised", bg="#B1A8A8", fg="blue", borderwidth=5, padx=20, pady=13, image=photo_desactivate, command=desactivate)
desact.pack(side=tk.LEFT)

root.mainloop()