def hanoi(n, origen="O", auxiliar="A", destino="D"):
    if n > 0:
        # Paso 1: trasladar n-1 discos de la torre de origen a la auxiliar
        hanoi(n - 1, origen, destino, auxiliar)

        # Paso 2: mover el disco mayor hacia la torre de destino
        print(f" Mover disco {n} desde {origen} hasta {destino}")

        # Paso 3: trasladar los n-1 discos restantes hacia la torre destino
        hanoi(n - 1, auxiliar, origen, destino)


try:
    # Solicitar número de discos al usuario
    discos = int(input("Digite la cantidad de discos a usar (mínimo 1 y máximo 10): "))

    # Validaciones de rango
    if discos < 1:
        print("No se permiten menos de 1 disco.")
    elif discos > 10:
        print(" El límite de discos permitido es 10.")
    else:
        print(f"\n Iniciando simulación con {discos} discos:\n")
        hanoi(discos)
        print(f"\n Número mínimo de movimientos necesarios: {2**discos - 1}")

except ValueError:
    # Si el usuario no escribe un número entero válido
    print(" Entrada inválida: debe ingresar un número entero dentro del rango.")
except Exception as e:
    # Para cualquier error no previsto
    print(f" Error inesperado detectado: {e}")
