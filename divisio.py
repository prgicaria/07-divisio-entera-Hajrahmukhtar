# Demanem a l'usuari els nombres
dividend = int(input("Escriu el dividend (nombre enter): "))
divisor = int(input("Escriu el divisor (nombre enter): "))

# Comprovem que el divisor no sigui zero
if divisor == 0:
    print("Error: No es pot calcular la divisió perquè el divisor no pot ser 0.")
else:
    # Calculem el quocient i el residu
    quocient = dividend // divisor
    residu = dividend % divisor

    # Mostrem els resultats
    print(f"La divisió és: {dividend / divisor}")
    print(f"Quocient: {quocient}")
    print(f"Residu: {residu}")
