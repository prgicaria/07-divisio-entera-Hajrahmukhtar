# Demanem a l'usuari els nombres
Dividend = int(input("Escriu el Dividend (nombre enter): "))
Divisó = int(input("Escriu el Divisó (nombre enter): "))

# Comprovem que el divisor no sigui zero
if Divisó == 0:
    print("Error: No es pot calcular la Divisió perquè el divisor no pot ser 0.")
else:
    # Calculem el Quocient i el Residu
    Quocient = Dividend // Divisó
    Residu = Dividend % Divisó

    # Mostrem els resultats
    print(f"La Divisió és: {Dividend}/{Divisó}")
    print(f"Quocient: {Quocient}")
    print(f"Residu: {Residu}")