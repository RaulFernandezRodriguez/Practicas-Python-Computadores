
class pares():
    def imprime_pares_intervalos(num1, num2):
        while num1 < num2:
            if (num2 % 2) == 0:
                print(num2)
                print("")
            num2 -1
    num1 = int(input("Introduce un numero inicial:"))
    num2 = int(input("Introduce un numero limite:"))
    if(num2 < num1):
        while num2 < num1:
            print("Error, reintroduce los valores")
            num1 = int(input("Introduce un numero inicial:"))
            num2 = int(input("Introduce un numero limite:"))
        imprime_pares_intervalos(num1, num2)
    else:
        imprime_pares_intervalos(num1, num2)