try:
    a = input("Enetr the number 1: ")
    b = input("Enetr the number 2: ")
    print(int(a)/int(b))
except ValueError:
    print("Give the Numbers as a input") 
expect ZeroDivisionError:
    print("Cannot Divide by Zero")  