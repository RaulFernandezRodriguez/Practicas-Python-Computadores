
class Calcular_nota():
    def calcular_nota(nota):
        if nota<5:
            (print ("Suspenso"))
        elif nota == 5 or nota == 6:
            (print ("Aprobado"))
        elif nota == 7 or nota == 8:
            (print ("Notable"))
        elif nota == 9 or nota == 10:
            (print ("Sobresaliente"))
    nota = int(input("Cual es tu nota:"))
    calcular_nota(nota)