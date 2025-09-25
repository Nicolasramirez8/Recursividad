# Recursividad
# Proyecto de Recursividad en Python

Este programa implementa dos algoritmos clásicos usando **recursividad**:

1. **Torres de Hanoi** → Mueve N discos entre tres torres siguiendo las reglas del juego.  
2. **Máximo Común Divisor (MCD)** → Calcula el MCD de dos números con el algoritmo de Euclides.  

---

## Torres de Hanoi
- El usuario ingresa el número de discos (1–20).  
- Se imprimen todos los pasos numerados hasta `2^N - 1`.  
- Al final se muestra el total de movimientos esperados.  

Ejemplo (N = 3):  
N = 1 → 1 movimiento
N = 2 → 3 movimientos
N = 3 → 7 movimientos
Total de movimientos: 7 (Esperado)

---

## MCD
- El usuario ingresa dos números enteros positivos.
- Se aplica recursividad con la fórmula:
  `MCD(a, b) = MCD(b, a % b)` hasta que `b = 0`.
- Devuelve el MCD de los dos números.

Ejemplo:  
Ingrese el primer número: 48
Ingrese el segundo número: 18
El MCD de 48 y 18 es: 6

Autor Nicolás Ramírez Montero
