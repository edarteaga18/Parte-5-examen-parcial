print("Comienzo del programa")

while True:
        NumEnPosi = int(input("Por favor ingresa un número entero positivo: "))
        if NumEnPosi <= 0: 
            print("El valor ingresado es incorrecto. Por favor intenta nuevamente.")

suma = 0
for i in range(1, NumEnPosi+1):
    suma += 1/i

print("El resultado de la serie es:", suma)
