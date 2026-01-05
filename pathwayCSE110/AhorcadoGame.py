"""""
Perfecto — te dejo un programa en Python que implementa exactamente las reglas que describes:

muestra guiones bajos al inicio,

solicita intentos al usuario,

si la longitud del intento no coincide con la palabra secreta muestra un mensaje y no da pista ni cuenta el intento,

para generar la pista: letra correcta en su posición → MAYÚSCULA, letra presente en otra posición → minúscula, letra no presente → _,

gestiona correctamente letras repetidas (no marca más ocurrencias que las que hay en la palabra secreta),

al acertar muestra el número de intentos usados.


Copia y pega esto en un archivo ahorcado_pistas.py o ejecútalo en tu REPL:

"""

# ahorcado_pistas.py
import getpass

def generar_pista(secret: str, guess: str) -> str:
    """
    Devuelve la pista para 'guess' respecto a 'secret' siguiendo las reglas:
    - letra en posición exacta -> MAYÚSCULA
    - letra presente en otra posición -> minúscula
    - letra no presente -> _
    Maneja correctamente letras repetidas.
    """
    secret = secret.lower()
    guess = guess.lower()
    n = len(secret)

    # Paso 1: calcular coincidencias exactas
    result = [''] * n
    secret_unmatched = []
    guess_unmatched_indices = []

    for i in range(n):
        if guess[i] == secret[i]:
            # Marca exacta (temporalmente guardamos la letra en mayúscula)
            result[i] = guess[i].upper()
        else:
            # Guardamos para procesamiento posterior
            secret_unmatched.append(secret[i])
            guess_unmatched_indices.append(i)

    # Convertimos lista a contador (frecuencias) para las letras no emparejadas del secreto
    from collections import Counter
    freq_secret_unmatched = Counter(secret_unmatched)

    # Paso 2: para cada letra no emparejada del intento, ver si aparece en el secreto sin emparejar
    for i in guess_unmatched_indices:
        ch = guess[i]
        if freq_secret_unmatched.get(ch, 0) > 0:
            # letra existe en otra posición -> minúscula
            result[i] = ch.lower()
            freq_secret_unmatched[ch] -= 1
        else:
            # letra no existe -> guion bajo
            result[i] = '_'

    # Devolvemos la pista como cadena
    return ''.join(result)


def jugar(secret: str):
    secret = secret.strip()
    if not secret:
        print("La palabra secreta no puede estar vacía.")
        return

    secret_len = len(secret)
    print("Tu hint is: " + ' '.join(['_'] * secret_len))  # inicial
    intentos = 0

    while True:
        guess = input(f"\nIntroduce una palabra de {secret_len} letras: ").strip()
        if len(guess) != secret_len:
            print(f"La respuesta debe tener exactamente {secret_len} letras. Intenta de nuevo (no se contará como intento).")
            continue

        intentos += 1

        if guess.lower() == secret.lower():
            print(f"¡Correcto! La palabra era '{secret}'. Has necesitado {intentos} intento(s).")
            break

        pista = generar_pista(secret, guess)
        # Mostrar con espacios para mayor legibilidad
        print("Pista:", ' '.join(pista))


if name == "_main_":
    print("### Juego de palabra secreta con pistas especiales ###")
    # Pedimos la palabra secreta sin mostrarla en pantalla (si el terminal lo soporta)
    try:
        secret_word = getpass.getpass("Introduce la palabra secreta (no se mostrará): ")
        if not secret_word:
            # Si el usuario pulsó enter vacío, pedimos normalmente
            secret_word = input("Palabra secreta (visible): ").strip()
    except Exception:
        # En algunos entornos (ej. algunos IDEs online) getpass falla: usar input normal
        secret_word = input("Introduce la palabra secreta: ").strip()

    jugar(secret_word)
"""
Notas y consejos:

Uso getpass.getpass para que la palabra secreta no se muestre en pantalla (útil si alguien más está viendo).

El programa es insensible a mayúsculas (compara en minúsculas), pero muestra las letras del intento transformadas a mayúsculas/minúsculas según la regla.

Si quieres que el intento con longitud equivocada cuente como intento, cambia dónde incrementas intentos.


¿Quieres que lo adapte para:

tomar la palabra secreta aleatoriamente de una lista,

límite de intentos,

interfaz gráfica simple (tkinter) o mostrar colores en terminal (verde/amarillo/gris)?
"""