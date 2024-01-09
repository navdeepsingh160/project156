from tkinter import *
from PIL import ImageTk, Image
root=Tk()

root.title("pokemon Game")
root.geometry("600x400")

root.configure(background="yellow2")

pikachu=ImageTk.PhotoImage(Image.open ("pikachu.jpg"))
bulbasour=ImageTk.PhotoImage(Image.open ("bulbasour.jpg"))
charmender=ImageTk.PhotoImage(Image.open ("charmender.jpg"))
squirtle=ImageTk.PhotoImage(Image.open ("squirtle.jpg"))
ratata=ImageTk.PhotoImage(Image.open ("ratata.jpg"))
nidoking=ImageTk.PhotoImage(Image.open ("nidoking.jpg"))
jigglypuff=ImageTk.PhotoImage(Image.open ("jigglypuff.jpg"))
meowth=ImageTk.PhotoImage(Image.open ("meowth.jpg"))
persion=ImageTk.PhotoImage(Image.open ("persion.jpg"))
abra=ImageTk.PhotoImage(Image.open ("abra.jpg"))
kadabra=ImageTk.PhotoImage(Image.open ("kadabra.jpg"))
Iyvasour=ImageTk.PhotoImage(Image.open ("Iyvasour.jpg"))

player1 = Label(root, text = "Player 1", bg = "royal blue", fg ="white" )
player1.place(relx = 0.1, rely = 0.3, anchor = CENTER)


player2 = Label(root, text = "Player 2", bg = "royal blue", fg ="white" )
player2.place(relx = 0.9, rely = 0.3, anchor = CENTER)


player1_score_label = Label(root,  bg = "royal blue", fg ="white" )
player1_score_label.place(relx = 0.1, rely = 0.4, anchor = CENTER)


player2_score_label = Label(root,  bg = "royal blue", fg ="white" )
player2_score_label.place(relx = 0.9, rely = 0.4, anchor = CENTER)


random_dice_label = Label(root,  bg = "chocolate1", fg ="white" )
random_dice_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)


root.mainloop()