class suma_n_numeros():
    def calcular_n_primeros_nums(num):
        total = 0
        while num>0:
            total = total + num
            num = num -1
        print(total)
    num = int(input("Introduce un numero para calcular:"))
    if num<0 or num==0:
        while num<0 or num==0:
            print("Error, intentalo otra vez")
            num = int(input("Introduce un numero para calcular:"))
        calcular_n_primeros_nums(num)
    else: 
        calcular_n_primeros_nums(num)