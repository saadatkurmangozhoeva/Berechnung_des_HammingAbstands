def load_words_from_file(file_name):
    wörter = []
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()  # Leerzeichen am Anfang und Ende einer Zeile löschen
            if line:  # Überprüfen, ob der String nicht leer ist
                wörter.append(line)
    return wörter

def hamming_abstand(str1, str2):
    # Дополняем строки до одинаковой длины
    length_difference = abs(len(str1) - len(str2))
    if len(str1) < len(str2):
        str1 += " " * length_difference
    else:
        str2 += " " * length_difference

    # Вычисляем Хэммингово расстояние
    distance = sum(1 for x, y in zip(str1, str2) if x != y)
    return distance

def analyze_abstände(abstände):
    gesamt = sum(abstände)
    max_abstand = max(abstände)
    min_abstand = min(abstände)
    average_abstand = gesamt / len(abstände)

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Durchschnittlicher Hamming-Abstand: {average_abstand}")
    print(f"Maximaler Hamming-Abstand: {max_abstand}")
    print(f"Minimaler Hamming-Abstand: {min_abstand}")

# Wörter aus der Datei herunterladen
german_alphabet = load_words_from_file('germanAlphabet.txt')

abstände = []
calculation_count = 1

# Berechnung der Hamming-Abstände zwischen jedem Wortpaar
for i in range(len(german_alphabet)):
    for j in range(i + 1, len(german_alphabet)):
        abstand = hamming_abstand(german_alphabet[i], german_alphabet[j])
        abstände.append(abstand)
        print(f"{calculation_count}) Hamming Abstand zwischen '{german_alphabet[i]}' und '{german_alphabet[j]}' is: {abstand}")
        calculation_count += 1


analyze_abstände(abstände)

