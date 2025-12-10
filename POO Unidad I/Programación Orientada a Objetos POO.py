
# Programa: Promedio semanal del clima
# Paradigma: Programación Orientada a Objetos (POO)
# Descripción: Este programa utiliza una clase para gestionar
#              temperaturas semanales aplicando principios
#              de encapsulamiento y métodos.
#Elaborado por: Leiber Correa

class ClimaSemanal:

    # Método constructor (__init__)
    # Objetivo: Inicializar el objeto creando el atributo
    #           privado que almacenará las temperaturas.

    def __init__(self):
        self.__temperaturas = []  # Atributo encapsulado (privado)


    # Método: ingresar_temperaturas
    # Objetivo: Solicitar al usuario la temperatura de cada
    #           día de la semana y guardarlas en la lista.

    def ingresar_temperaturas(self):
        print("Ingrese la temperatura de cada día de la semana:\n")

        # Bucle para ingresar las 7 temperaturas
        for i in range(7):
            temp = float(input(f"Día {i + 1}: "))  # Se convierte a float
            self.__temperaturas.append(temp)  # Se guarda en la lista privada

    # Método: calcular_promedio
    # Objetivo: Calcular el promedio de las temperaturas
    #           almacenadas en el atributo privado.
    # Retorna: Promedio numérico o 0 si no hay datos.

    def calcular_promedio(self):
        # Evita división entre cero si la lista está vacía
        if len(self.__temperaturas) == 0:
            return 0

        # Cálculo del promedio
        return sum(self.__temperaturas) / len(self.__temperaturas)

    # Método: mostrar_promedio
    # Objetivo: Mostrar el promedio calculado con formato.
    # -----------------------------------------------------
    def mostrar_promedio(self):
        promedio = self.calcular_promedio()  # Llama al método de cálculo
        print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")



# Bloque principal del programa
# Objetivo: Crear un objeto de la clase e iniciar el proceso

if __name__ == "__main__":
    print("=== PROMEDIO SEMANAL DEL CLIMA (POO) ===")

    clima = ClimaSemanal()  # Se crea una instancia (objeto) de la clase

    clima.ingresar_temperaturas()  # Llamada para ingresar datos
    clima.mostrar_promedio()  # Muestra el resultado final
