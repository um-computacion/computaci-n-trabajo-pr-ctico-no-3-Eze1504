from exceptions import ingrese_numero
from exceptions import NumeroDebeSerPositivo

def ingrese_numero():
    """
    Solicita al usuario ingresar un número y valida que sea positivo.
    
    Returns:
        int: El número ingresado si es válido.
        
    Raises:
        ValueError: Si la entrada no es un número válido.
        NumeroDebeSerPositivo: Si el número ingresado es negativo.
    """
    entrada = input("Ingrese un número: ")
    
    # Eliminar espacios en blanco al inicio y final
    entrada = entrada.strip()
    
    try:
        # Intentar convertir la entrada a un entero
        numero = int(entrada)
    except ValueError:
        # Si falla la conversión, lanzar ValueError
        raise ValueError("La entrada debe ser un número válido")
    
    # Verificar si el número es negativo
    if numero < 0:
        raise NumeroDebeSerPositivo("El número debe ser positivo")
    
    return numero

def main():
    """
    Programa principal que solicita números al usuario y muestra los resultados.
    """
    while True:
        try:
            numero = ingrese_numero()
            print(f"Número válido: {numero}")
        except ValueError as e:
            print(f"Error: {e}")
        except NumeroDebeSerPositivo as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nPrograma finalizado.")
            break

if __name__ == "__main__":
    main() 