from tkinter import *
import random
from tkinter import simpledialog, messagebox

class DevinetteGUI:
    niv = 100

    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fenetre.title("Jeu de devinette")

        # Couleur d'arrière-plan de la fenêtre
        self.fenetre.configure(bg="pink")

        # Titre du jeu avec une couleur
        self.label_titre = Label(fenetre, text="Jeu de devinette", fg="blue", font=("Arial", 16, "bold"), bg="pink")
        self.label_titre.pack(side=TOP, pady=20)

        self.label_niveau = Label(fenetre, text="Niveau de difficulté :", font=("Arial", 12), bg="pink")
        self.choix_niveau = IntVar()

        # Cadre pour les boutons radio
        cadre_niveaux = Frame(fenetre, bg="pink")
        cadre_niveaux.pack(side=TOP, padx=10, pady=10)

        self.radio_facile = Radiobutton(cadre_niveaux, text="Facile", variable=self.choix_niveau, value=1, font=("Arial", 12), bg="pink")
        self.radio_moyen = Radiobutton(cadre_niveaux, text="Moyen", variable=self.choix_niveau, value=2, font=("Arial", 12), bg="pink")
        self.radio_difficile = Radiobutton(cadre_niveaux, text="Difficile", variable=self.choix_niveau, value=3, font=("Arial", 12), bg="pink")

        self.label_nb_coups = Label(fenetre, text="Nombre de coups :", font=("Arial", 12), bg="pink")
        self.entry_nb_coups = Entry(fenetre, font=("Arial", 12))
        self.bouton_jouer = Button(fenetre, text="Jouer", command=self.jouer, font=("Arial", 14, "bold"), bg="#4CAF50", fg="white")

        self.label_niveau.pack(side=TOP, padx=10, pady=10)
        self.radio_facile.pack(side=LEFT, padx=10)
        self.radio_moyen.pack(side=LEFT, padx=10)
        self.radio_difficile.pack(side=LEFT, padx=10)

        self.label_nb_coups.pack(side=TOP, padx=10, pady=10)
        self.entry_nb_coups.pack(side=TOP, padx=10, pady=10)
        self.bouton_jouer.pack(side=TOP, padx=10, pady=10)

    def devinette(self, niveau, nb_coups, nombre_aleatoire):
        global niv
        if niveau == 1:
            niv = 10
        elif niveau == 2:
            niv = 100
        else:
            niv = 1000
        nombre_essais = 0
        victoire = False
        while nombre_essais < nb_coups and not victoire:
            try:
                nombre_saisi = int(
                    simpledialog.askstring("Saisissez un nombre", "Entrez un nombre entre 0 et {} :".format(niv)))
                nombre_essais += 1
                if nombre_saisi == nombre_aleatoire:
                    victoire = True
                else:
                    if nombre_saisi < nombre_aleatoire:
                        messagebox.showinfo("Résultat", "Le nombre saisi est trop petit.")
                    else:
                        messagebox.showinfo("Résultat", "Le nombre saisi est trop grand.")
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")
        if victoire:
            messagebox.showinfo("Résultat", "Vous avez gagné !")
        else:
            messagebox.showinfo("Résultat", "Vous avez perdu. Le nombre mystère était {}.".format(nombre_aleatoire))

        # Demander si le joueur souhaite rejouer
        rejouer = messagebox.askyesno("Rejouer ?", "Voulez-vous rejouer ?")
        if rejouer:
            self.jouer()
        else:
            self.fenetre.quit()

    def jouer(self):
        niveau = self.choix_niveau.get()
        if niveau == 1:
            nombre_aleatoire = random.randrange(10)
        elif niveau == 2:
            nombre_aleatoire = random.randrange(100)
        else:
            nombre_aleatoire = random.randrange(1000)
        nb_coups = int(self.entry_nb_coups.get())
        if nb_coups is not None:
            self.devinette(niveau, nb_coups, nombre_aleatoire)

if __name__ == "__main__":
    fenetre = Tk()
    app = DevinetteGUI(fenetre)
    fenetre.mainloop()
