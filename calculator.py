import tkinter as tk
from tkinter import *
import math

root = tk.Tk()
root.geometry("400x395")  
root.title("Калькулятор")
root.minsize(400, 395)
root.maxsize(400, 395)
root.configure(bg="#000814")

inp = Entry(root, width=30, borderwidth=0, relief=RIDGE, bg="#001d3d", fg="white")
inp.grid(pady=20, column=0, row=0, columnspan=5, padx=30, sticky='w')
inp.config(font=("Arial", 11))  
ans_value = "" 

def clear_input(event):
    inp.delete(0, END)


inp.bind("<Key>", clear_input)

def delete_last_character():
    current_expression = inp.get()
    inp.delete(0, END)
    inp.insert(0, current_expression[:-1])

# <Далі буде функції кнопочок>

def result():
    global ans_value
    try:
        expression = inp.get()
        if '!' in expression:
            expression = expression.replace('!', '')
            res = math.factorial(int(expression))
            inp.delete(0, END)
            inp.insert("end", res) 
            ans_value = res 
        elif '√' in expression:
            expression = expression.replace('√', 'math.sqrt(') + ')'
            res = evaluate_expression(expression)
            inp.delete(0, END)
            inp.insert("end", res)
            ans_value = res
        else:
            if expression == "":
                inp.insert("end", "error")
            elif expression[0] == "0":
                inp.delete(0, "end")
                inp.insert("end", "error")
            else:
                if "Ans" in expression:
                    expression = expression.replace('Ans', str(ans_value))
                res = evaluate_expression(expression)
                ans_value = res  
                inp.delete(0, END)
                inp.insert("end", res)  
    except Exception as e:
        inp.delete(0, "end")
        inp.insert("end", "invalid input")

def evaluate_expression(expression):
    return eval(expression)

# <Далі робимо кнопочки і їх вигляд⬇️>
# lambda дуже зручна доречі для кнопочок)

clear = Button(root, text="C", width=8, command=lambda: inp.delete(0, "end"), bg="#001d3d", fg="white", relief=FLAT, bd=0, highlightthickness=0, padx=10, pady=5, borderwidth=0, highlightcolor="#000814", highlightbackground="#000814") 
clear.grid(row=1, column=0, pady=10, padx=10)  

left_parenthesis = Button(root, text="(", width=8, command=lambda: inp.insert("end", "("), relief=FLAT, bg="#001d3d", fg="white", bd=0, highlightthickness=0, padx=10, pady=5, borderwidth=0, highlightcolor="#000814", highlightbackground="#000814")  
left_parenthesis.grid(row=1, column=1, pady=10, padx=10)  

right_parenthesis = Button(root, text=")", width=8, command=lambda: inp.insert("end", ")"), relief=FLAT, bg="#001d3d", fg="white", bd=0, highlightthickness=0, padx=10, pady=5, borderwidth=0, highlightcolor="#000814", highlightbackground="#000814")  
right_parenthesis.grid(row=1, column=2, pady=10, padx=10)  

ans = Button(root, text="Ans", width=8, command=lambda: inp.insert("end", "Ans"), relief=FLAT, bg="#ffc300", fg="black", bd=0, highlightthickness=0, padx=10, pady=5, borderwidth=0, highlightcolor="#000814", highlightbackground="#000814")  
ans.grid(row=6, column=3, pady=10, padx=10)  

seven = Button(root, text="7", width=8, command=lambda: inp.insert("end", "7"), relief=FLAT, bg="#001d3d", fg="white", bd=0, highlightthickness=0, padx=10, pady=5, borderwidth=0, highlightcolor="#000814", highlightbackground="#000814")  
seven.grid(row=2, column=0, pady=10, padx=10)  

eight = Button(root, text="8", width=8, command=lambda: inp.insert("end", "8"), relief=FLAT, bg="#001d3d", fg="white", bd=0, highlightthickness=0, padx=10, pady=5, borderwidth=0, highlightcolor="#000814", highlightbackground="#000814")  
eight.grid(row=2, column=1, pady=10, padx=10)  

nine = Button(root, text="9", width=8, command=lambda: inp.insert("end", "9"), relief=FLAT, bg="#001d3d", fg="white", bd=0, highlightthickness=0, padx=10, pady=5, borderwidth=0, highlightcolor="#000814", highlightbackground="#000814")  
nine.grid(row=2, column=2, pady=10, padx=10)  

plus = Button(root, text="+", width=8, command=lambda: inp.insert("end", "+"), relief=FLAT, bg="#001d3d", fg="white", bd=0, highlightthickness=0, padx=10, pady=5, borderwidth=0, highlightcolor="#000814", highlightbackground="#000814")  
plus.grid(row=2, column=3, pady=10, padx=10)  

four = Button(root, text="4", width=8, command=lambda: inp.insert("end", "4"), relief=FLAT, bg="#001d3d", fg="white", bd=0, highlightthickness=0, padx=10, pady=5, borderwidth=0, highlightcolor="#000814", highlightbackground="#000814")  
four.grid(row=3, column=0, pady=10, padx=10)  

five = Button(root, text="5", width=8, command=lambda: inp.insert("end", "5"), relief=FLAT, bg="#001d3d", fg="white", bd=0, highlightthickness=0, padx=10, pady=5, borderwidth=0, highlightcolor="#000814", highlightbackground="#000814")  
five.grid(row=3, column=1, pady=10, padx=10)  

six = Button(root, text="6", width=8, command=lambda: inp.insert("end", "6"), relief=FLAT, bg="#001d3d", fg="white", bd=0, highlightthickness=0, padx=10, pady=5, borderwidth=0, highlightcolor="#000814", highlightbackground="#000814")  
six.grid(row=3, column=2, pady=10, padx=10)  

minus = Button(root, text="-", width=8, command=lambda: inp.insert("end", "-"), relief=FLAT, bg="#001d3d", fg="white", bd=0, highlightthickness=0, padx=10, pady=5, borderwidth=0, highlightcolor="#000814", highlightbackground="#000814")  
minus.grid(row=3, column=3, pady=10, padx=10)  

one = Button(root, text="1", width=8, command=lambda: inp.insert("end", "1"), relief=FLAT, bg="#001d3d", fg="white", bd=0, highlightthickness=0, padx=10, pady=5, borderwidth=0, highlightcolor="#000814", highlightbackground="#000814")  
one.grid(row=4, column=0, pady=10, padx=10)  

two = Button(root, text="2", width=8, command=lambda: inp.insert("end", "2"), relief=FLAT, bg="#001d3d", fg="white", bd=0, highlightthickness=0, padx=10, pady=5, borderwidth=0, highlightcolor="#000814", highlightbackground="#000814")  
two.grid(row=4, column=1, pady=10, padx=10)  

three = Button(root, text="3", width=8, command=lambda: inp.insert("end", "3"), relief=FLAT, bg="#001d3d", fg="white", bd=0, highlightthickness=0, padx=10, pady=5, borderwidth=0, highlightcolor="#000814", highlightbackground="#000814")  
three.grid(row=4, column=2, pady=10, padx=10)  

multiply = Button(root, text="*", width=8, command=lambda: inp.insert("end", "*"), relief=FLAT, bg="#001d3d", fg="white", bd=0, highlightthickness=0, padx=10, pady=5, borderwidth=0, highlightcolor="#000814", highlightbackground="#000814")  
multiply.grid(row=4, column=3, pady=10, padx=10)  

pi = Button(root, text="π", width=8, command=lambda: inp.insert("end", '3.14'), relief=FLAT, bg="#001d3d", fg="white", bd=0, highlightthickness=0, padx=10, pady=5, borderwidth=0, highlightcolor="#000814", highlightbackground="#000814")  
pi.grid(row=5, column=0, pady=10, padx=10)  

zero = Button(root, text="0", width=8, command=lambda: inp.insert("end", "0"), relief=FLAT, bg="#001d3d", fg="white", bd=0, highlightthickness=0, padx=10, pady=5, borderwidth=0, highlightcolor="#000814", highlightbackground="#000814")  
zero.grid(row=5, column=1, pady=10, padx=10)  

dot = Button(root, text=".", width=8, command=lambda: inp.insert("end", "."), relief=FLAT, bg="#001d3d", fg="white", bd=0, highlightthickness=0, padx=10, pady=5, borderwidth=0, highlightcolor="#000814", highlightbackground="#000814")  
dot.grid(row=5, column=2, pady=10, padx=10)  

divide = Button(root, text="/", width=8, command=lambda: inp.insert("end", "/"), relief=FLAT, bg="#001d3d", fg="white", bd=0, highlightthickness=0, padx=10, pady=5, borderwidth=0, highlightcolor="#000814", highlightbackground="#000814")  
divide.grid(row=5, column=3, pady=10, padx=10)  

sqrt = Button(root, text="√ ", width=8, command=lambda: inp.insert("end", "√"), relief=FLAT, bg="#001d3d", fg="white", bd=0, highlightthickness=0, padx=10, pady=5, borderwidth=0, highlightcolor="#000814", highlightbackground="#000814")  
sqrt.grid(row=6, column=0, pady=10, padx=10)  

exponentiation = Button(root, text="^", width=8, command=lambda: inp.insert("end", "**"), relief=FLAT, bg="#001d3d", fg="white", bd=0, highlightthickness=0, padx=10, pady=5, borderwidth=0, highlightcolor="#000814", highlightbackground="#000814")  
exponentiation.grid(row=6, column=1, pady=10, padx=10)  

factorial = Button(root, text="!", width=8, command=lambda: inp.insert("end", "!"), relief=FLAT, bg="#001d3d", fg="white", bd=0, highlightthickness=0, padx=10, pady=5, borderwidth=0, highlightcolor="#000814", highlightbackground="#000814")  
factorial.grid(row=6, column=2, pady=10, padx=10)

delete_last = Button(root, text="Delete", width=8, command=delete_last_character, relief=FLAT, bg="#ffc300", fg="black", bd=0, highlightthickness=0, padx=10, pady=5, borderwidth=0, highlightcolor="#000814", highlightbackground="#000814")  
delete_last.grid(row=1, column=3, pady=10, padx=10)  

resul = Button(root, text="=", width=8, command=result, bg="#ffc300", fg="black", relief=FLAT, bd=0, highlightthickness=0, padx=10, pady=5, borderwidth=0, highlightcolor="#000814", highlightbackground="#000814")  
resul.grid(row=7, column=3, pady=10, padx=10)  

ans = Button(root, text="Ans", width=8, command=lambda: inp.insert("end", "Ans"), relief=FLAT, bg="#ffc300", fg="black", bd=0, highlightthickness=0, padx=10, pady=5, borderwidth=0, highlightcolor="#000814", highlightbackground="#000814")  
ans.grid(row=6, column=3, pady=10, padx=10)  

root.mainloop()
