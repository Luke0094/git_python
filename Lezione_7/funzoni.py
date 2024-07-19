import random

def hello(name, surname): #definizione della funzione hello
    print("Hello" , name, surname)

def somma(num1, num2):
    print(num1 + num2)


hello("Mattia", "Folcarelli") # chiamata della funzione hello
hello("mat", "folca") # chiamata della funzione hello
somma(3,4)

array = [1,2,3,4,5]
print(random.shuffle(array))