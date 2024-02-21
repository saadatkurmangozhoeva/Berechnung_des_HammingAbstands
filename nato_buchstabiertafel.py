def load_words_from_file(file_path):
    words = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                words.append(line)
    return words

# Funktion zur Berechnung des Hamming-Abstands
def hamming_abstand(str1, str2):
    length_difference = abs(len(str1) - len(str2))
    if len(str1) < len(str2):
        str1 += " " * length_difference
    else:
        str2 += " " * length_difference

    abstand= sum(1 for x, y in zip(str1, str2) if x != y)
    return abstand

# Функция для анализа расстояний
def analyze_distances(abstände):
    gesamt= sum(abstände)
    max_abstand = max(abstände)
    min_abstand = min(abstände)
    average_abstand = gesamt / len(abstände)


    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(f"Durchschnittlicher Hamming-Abstand: {average_abstand}")
    print(f"Maximaler Hamming-Abstand: {max_abstand}")
    print(f"Minimaler Hamming-Abstand: {min_abstand}")


file_path = 'nato_buchstabiertafel.txt'


ipa_alphabet = load_words_from_file(file_path)

# Berechnung der Hamming-Abstands zwischen jedem Wortpaar
abstände = []
calculation_count = 1

for i in range(len(ipa_alphabet)):
    for j in range(i + 1, len(ipa_alphabet)):
        abstand = hamming_abstand(ipa_alphabet[i], ipa_alphabet[j])
        print(f"{calculation_count}) Hamming distance between '{ipa_alphabet[i]}' and '{ipa_alphabet[j]}' is: {abstand}")
        abstände.append(abstand)
        calculation_count += 1


analyze_distances(abstände)
