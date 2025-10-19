# ascii_conversion.py

def texto_a_ascii(texto):
    """Convierte cada caracter de un texto a su código ASCII."""
    return [ord(c) for c in texto]

def ascii_a_texto(codigos):
    """Convierte una lista de códigos ASCII a texto."""
    return ''.join(chr(c) for c in codigos)

# Programa principal con menú
def main():
    while True:
        print("\n===== CONVERSIÓN ASCII =====")
        print("1. Texto → ASCII")
        print("2. ASCII → Texto")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            texto = input("Ingresa el texto: ")
            codigos = texto_a_ascii(texto)
            print(f"Códigos ASCII: {codigos}")
        elif opcion == '2':
            codigos_str = input("Ingresa los códigos ASCII separados por espacios: ")
            try:
                codigos = [int(c) for c in codigos_str.split()]
                texto = ascii_a_texto(codigos)
                print(f"Texto resultante: {texto}")
            except ValueError:
                print("Entrada inválida. Debes ingresar números separados por espacios.")
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
