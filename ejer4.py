class volumen():
    def volumen_cono(self, altura, radio):
        result = altura * radio * radio * 3.14 / 3
        return result
    def volumen_ortoedro(self, altura, lado1, lado2):
        result = altura * lado1 * lado2
        return result
    def menu(self):
        print("1-Cono\n")
        print("2-Ortoedro\n")
        print("3-Salir\n")
        select = int(input("Elige que figura quieres calcular su volumen: "))
        if select<=0 or select > 3:
            while select<=0 or select > 3:
              select = int(input("Elige que figura quieres calcular su volumen: "))
        else:
            if select == 1:
                radio = float(input("Escribe el radio del cono: "))
                altura = float(input("Escribe la altura del cono: "))
                result = self.volumen_cono(altura, radio)
                print(result)
            elif select == 2:
                lado1 = float(input("Escribe un lado del ortoedro: "))
                lado2 = float(input("Escribe el otro: "))
                altura = float(input("Escribe tambien la altura del ortoedro: "))
                result = self.volumen_ortoedro(altura, lado1, lado2) 
                print(result)
            elif select == 3:
                print("Saliste del programa")
volumen_obj = volumen()
volumen_obj.menu()