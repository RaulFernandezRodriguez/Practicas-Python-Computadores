class potencia():
    def potencia(base, expo):
        total = 1
        for n in range(expo):
            total = total * base
        print(total)
    base = int(input("Introduce una base para la potencia:"))
    expo = int(input("Introduce un exponente para tu base:"))
    if base<0 or base==0 or expo<0 or expo==0:
        while base<0 or base==0 or expo<0 or expo==0:
            print("Error, intentalo otra vez")
            base = int(input("Introduce una base para la potencia:"))
            expo = int(input("Introduce un exponente para tu base:"))
        potencia(base, expo)
    else: 
        potencia(base, expo)