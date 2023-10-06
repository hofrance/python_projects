from tkinter import *






#je definis notre fenetre principale
notreFenetre=Tk()
leCanva = Canvas(notreFenetre,bg='grey',height=500,width=500)

leCanva.pack(side=TOP)
#la route qui est representer par le grand rectangle
leCanva.create_rectangle(50,50,450,400,width=2,fill='black' ,)


#creation des passage piettons
leCanva.create_rectangle(100,100,150,300,width=2,fill='yellow')
leCanva.create_rectangle(200,100,250,300,width=2,fill='yellow')
leCanva.create_rectangle(300,100,350,300,width=2,fill='yellow')
leCanva.create_rectangle(400,100,450,300,width=2,fill='yellow')
leCanva.create_rectangle(600,100,500,300,width=2,fill='yellow')

coul1 = 'red'
coul2 = 'green'



def creeFeuCouleur():


    #premier feu: en haut a gauche
    leCanva.create_oval(10,10,30,30,outline=coul1,fill=coul1)
    #second feu :en haut a droite
    leCanva.create_oval(480,10,500,30,outline=coul2,fill=coul2)

    #troisiemme feu: en bas a gauche
    leCanva.create_oval(10,480,30,500,outline=coul2,fill=coul2)

    #quattriemme feu: en bas a droite
    leCanva.create_oval(480,480,500,500,outline=coul1,fill=coul1)


def echangeCouleur():
    global coul1, coul2

    if(coul1=='red'):
        coul1 = 'green'
        coul2 = 'red'

        creeFeuCouleur()
    else:
        coul1 = 'red'
        coul2 = 'green'
        creeFeuCouleur()

creeFeuCouleur()
monBouton = Button(notreFenetre,text='changer la couleur',command=echangeCouleur)
monBouton.pack()


nombreDeRectangle=7




notreFenetre.mainloop()