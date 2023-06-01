import random
import string

usuarios = [
    "Alicia",
    "Blanca",
    "Carlos",
    "Daria",
    "Enrique",
    "Felipe",
    "Gloria",
    "Héctor",
    "Ignacio",
    "Juana",
]

cuentas_usuarios = {}

def generar_contrasena():
    """Genera una contraseña aleatoria y que contiene al menos un numero,
    una letra mayúscula y una letra minúscula.

    Retorna: La contraseña generada como un string.    
    """
    # Elegir la cantidad de cada tipo de caracter en la contraseña
    cantidad_numeros = random.randint(1, 5)
    cantidad_mayusculas = random.randint(1, 5)
    cantidad_minusculas = 11 - cantidad_numeros - cantidad_mayusculas

    caracteres = []

    # Generar digitos aleatorios que pueden repetirse
    for n in range(cantidad_numeros):
        caracteres.append(random.choice(string.digits))

    # Generar letras mayúsculas aleatorias que pueden repetirse
    for n in range(cantidad_mayusculas):
        caracteres.append(random.choice(string.ascii_uppercase))

    # Generar letras minúsculas aleatorias que pueden repetirse
    for n in range(cantidad_minusculas):
        caracteres.append(random.choice(string.ascii_lowercase))

    # Los caracteres están agrupados en orden asi que usamos shuffle()
    # para desordenarlos antes de retornar la contraseña.
    random.shuffle(caracteres)
    return ''.join(caracteres)


def crear_cuenta(usuario):
    """Crea una cuenta para un usuario dado.

    Argumentos:
        usuario: Un string con el nombre de usuario de la cuenta.

    Retorna: None
    """
    cuentas_usuarios[usuario] = {"contraseña": generar_contrasena()}

# Creación de cuentas con contraseña
for usuario in usuarios:
    crear_cuenta(usuario)

# Pedir numeros telefónicos
for usuario in cuentas_usuarios.keys():
    while True:
        telefono = input(f"{usuario}, Ingresa tu numero telefónico: ")
        if len(telefono) == 8 and telefono.isdecimal():
            cuentas_usuarios[usuario]["teléfono"] = telefono
            break
        else:
            print("El numero telefónico debe contener 8 numeros")