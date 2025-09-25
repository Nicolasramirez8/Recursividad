def mcd(a, b):

    if b == 0:
        return a
    else:
        return mcd(b, a % b)

if __name__ == "__main__":
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    print(f"El MCD de {a} y {b} es: {mcd(a, b)}")