

def main():
    numero = int(input("Escribe un numero : "))
    #escribe tu código abajo de esta línea
    r=1
    while r**2<=numero:
        r +=1
    print(r)

if __name__=='__main__':
    main()
