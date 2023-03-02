import tkinter as tk

pioche_droite = tk.PhotoImage(file="image/pioche_en_or_rules1.png")
pioche_gauche = tk.PhotoImage(file="image/pioche_en_or_rules.png")

def rules():

    windows_rules = tk.Toplevel(bg="#B1A8A8")
    windows_rules.attributes('-fullscreen', True)

    def exit_rules():
        windows_rules.destroy()

    #bouton pour fermer la page des règles
    btn_exit = tk.Button(windows_rules, text="QUITTER", relief="raised", bg="#B1A8A8", fg="blue", borderwidth=5, font=("Retro Gaming", 25), command=exit_rules)
    btn_exit.place(x=630, y=650)

    pchd = tk.Label(windows_rules, image=pioche_droite, bg="#B1A8A8")
    pchd.place(x=1000, y=100)

    pchg = tk.Label(windows_rules, image=pioche_gauche, bg="#B1A8A8")
    pchg.place(x=100, y=100)

    display_rulees = tk.Text(windows_rules, width=25, height=15, bg="#B1A8A8", relief="sunken", borderwidth=10, font=("Retro Gaming", 15))
    display_rulees.insert(tk.INSERT, "Le démineur consiste à \ndétruire les cases du jeux en évitant de détruire les mines \ncachées.")
    display_rulees.insert(tk.INSERT, "\nA chaque fois que le \njoueur clique sur une case \nnon minée, soit la case et vide et donc cela signifie qu'il n'y a aucune bombe au alentour,")
    display_rulees.insert(tk.INSERT, "\nsoit des chiffres \napparaissent en fonction du \nnombre de bombe présente \nautour de la case.")
    display_rulees.insert(tk.INSERT, "\nLes nombres peuvent allez de 1 (une bombe autour de \nla case), à 8 (huit bombes \nautour de la case)")
    display_rulees.insert(tk.INSERT, "Le joueur a aussi la possibilité de marquer la case désirée avec un point d'interrogation (le joueur \na des soupçons sur \ncette case mais n'est pas \nsûr),")
    display_rulees.insert(tk.INSERT, "  pour l'utiliser le joueur doit faire un clic droit sur la souris.")
    display_rulees.insert(tk.INSERT, "\nEnsuite le joueur a la \npossibilté de placer un \ndrapeau sur la \ncase de son choix en fonction du nombre de mines cachées.")
    display_rulees.insert(tk.INSERT, "\nCes drapeaux servent à \nlocaliser les mines, à chaque \nfois que le joueur à trouver \nune mine il peut placer un \ndrapeau dessus.")
    display_rulees.insert(tk.INSERT, "\nPour l'utiliser il suffit de faire un double clic droit sur la \ncase voulue.")
    display_rulees.insert(tk.INSERT, "\nPour supprimer le drapeau \nou le point d'interrogation, il \nsuffit de faire un control-clic droit dessus.")
    display_rulees.insert(tk.INSERT, "\nLe jeu prend fin une fois que toute les cases non minée on était découverte (GAGNER!),")
    display_rulees.insert(tk.INSERT, "\nou alors que le joueur à \nactivé une mine (PERDU!).")
    display_rulees.place(x=550, y=200)