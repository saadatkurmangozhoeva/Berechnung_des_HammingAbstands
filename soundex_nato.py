def hamming_distance(s1, s2):
    """Berechnet den Hamming-Abstand zwischen zwei Strings."""
    if len(s1) != len(s2):
        raise ValueError("Strings müssen gleiche Länge haben.")
    return sum(1 for x, y in zip(s1, s2) if x != y)

# Soundex-Codes für das NATO Alphabet
soundex_codes = {
    'Alfa': 'A410',
    'Bravo': 'B610',
    'Charlie': 'C640',
    'Delta': 'D430',
    'Echo': 'E200',
    'Foxtrot': 'F236',
    'Golf': 'G410',
    'Hotel': 'H340',
    'India': 'I530',
    'Juliett': 'J430',
    'Kilo': 'K400',
    'Lima': 'L500',
    'Mike': 'M200',
    'November': 'N151',
    'Oscar': 'O260',
    'Papa': 'P100',
    'Quebec': 'Q120',
    'Romeo': 'R500',
    'Sierra': 'S600',
    'Tango': 'T520',
    'Uniform': 'U516',
    'Victor': 'V236',
    'Whiskey': 'W200',
    'Xray': 'X600',
    'Yankee': 'Y520',
    'Zulu': 'Z400'
}

abstände = []  # Liste zur Speicherung aller Abständen
comparison_count = 1  # Zähler für die Anzahl der Vergleiche

# Erstellen Sie eine Wortliste, um den indexierten Zugriff zu erleichtern
wörter= list(soundex_codes.keys())

# Iterieren über jedes Codepaar und berechnen Sie Hamming-Abstände
for i in range(len(wörter)):
    for j in range(i+1, len(wörter)):
        wort1, code1 = wörter[i], soundex_codes[wörter[i]]
        wort2, code2 = wörter[j], soundex_codes[wörter[j]]
        distance = hamming_distance(code1, code2)
        abstände.append(distance)  # Store the distance
        print(f"{comparison_count}. Hamming distance between {wort1} ({code1}) and {wort2} ({code2}): {distance}")
        comparison_count += 1  # Increment the comparison counter

# Berechnung maximale, minimale und durchschnittliche Abstände
max_abstand = max(abstände)
min_abstand= min(abstände)
avg_abstand = sum(abstände) / len(abstände)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"\nMaximaler Hamming-Abstand: {max_abstand}")
print(f"Minimaler Hamming-Abstand: {min_abstand}")
print(f"Durchschnittlicher Hamming-Abstand: {avg_abstand:.2f}")
