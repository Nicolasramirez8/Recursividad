def hanoi(n: int, origen: str, auxiliar: str, destino: str, paso: int = 1) -> int: 

    if n == 1:
        print(f"Paso {paso}: mover disco desde {origen} hacia {destino}")
        return paso + 1
    else:
        paso = hanoi(n - 1, origen, destino, auxiliar, paso)
        print(f"Paso {paso}: mover disco desde {origen} hacia {destino}")
        paso += 1
        paso = hanoi(n - 1, auxiliar, origen, destino, paso)
        return paso

def main():
    try:
        n = int(input("Ingrese el número de discos (1-20):"))
        if n < 1 or n > 20:
            raise ValueError("El número no está en el rango permitido")
        
        total = hanoi(n, "A", "B", "C", 1)
        esperado = 2 ** n - 1

    except ValueError as ve:
        print(f"[Error de valor] {ve}")
    except Exception as e:
        print(f"[Error inesperado] {e}")

if __name__ == "__main__":
    main()