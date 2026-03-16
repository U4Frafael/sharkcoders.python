import tkinter as tk

ronda = 1

def lalterar_texto(btn):
    global ronda
    if ronda % 2 == 0:
        btn.config(text="0")
    else:
        btn.config(text="X")
    ronda += 1
        
    if verificar_vitoria():
            print("Fim de jogo.")
            return

root = tk.Tk()
root.geometry('550x300')
root.wm_resizable(width=False, height=False)


btn1 = tk.Button(root, text=" ", width=25, height=6, command= lambda : lalterar_texto(btn1))
btn1.grid(row=0, column=0)

btn2 = tk.Button(root, text=" ", width=25, height=6, command= lambda : lalterar_texto(btn2))
btn2.grid(row=0, column=1)

btn3 = tk.Button(root, text=" ", width=25, height=6, command= lambda : lalterar_texto(btn3))
btn3.grid(row=0, column=2)

btn4 = tk.Button(root, text=" ", width=25, height=6, command= lambda : lalterar_texto(btn4))
btn4.grid(row=1, column=0)

btn5 = tk.Button(root, text=" ", width=25, height=6, command= lambda : lalterar_texto(btn5))
btn5.grid(row=1, column=1)

btn6 = tk.Button(root, text=" ", width=25, height=6, command= lambda : lalterar_texto(btn6))
btn6.grid(row=1, column=2)

btn7 = tk.Button(root, text=" ", width=25, height=6, command= lambda : lalterar_texto(btn7))
btn7.grid(row=2, column=0)

btn8 = tk.Button(root, text=" ", width=25, height=6, command= lambda : lalterar_texto(btn8))
btn8.grid(row=2, column=1)

btn9 = tk.Button(root, text=" ", width=25, height=6, command= lambda : lalterar_texto(btn9))
btn9.grid(row=2, column=2)

def verificar_vitoria():
    if btn1["text"] == btn2["text"] == btn3["text"] != "":
        return True
    if btn4["text"] == btn5["text"] == btn6["text"] != " ":
        return True
    if btn7["text"] == btn8["text"] == btn9["text"] != " ":
        return True
    if btn1["text"] == btn4["text"] == btn7["text"] != " ":
        return True
    if btn2["text"] == btn5["text"] == btn8["text"] != " ":
        return True
    if btn3["text"] == btn6["text"] == btn9["text"] != " ":
        return True
    if btn1["text"] == btn5["text"] == btn9["text"] != " ":
        return True
    if btn3["text"] == btn5["text"] == btn7["text"] != " ":
        return True
    return False

root.mainloop()