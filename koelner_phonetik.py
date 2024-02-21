def hamming_abstand(s1, s2):
    "Berechnet den Hamming-Abstand zwischen zwei Strings."
    if len(s1) != len(s2):
        raise ValueError("Strings müssen gleiche Länge haben.")
    return sum(1 for x, y in zip(s1, s2) if x != y)


phonetic_codes = {
    'Anton': '0626',
    'Ärger': '0747',
    'Berta': '172',
    'Cäsar': '887',
    'Dora': '27',
    'Emil': '065',
    'Friedrich': '37274',
    'Gustav': '4823',
    'Heinrich': '0674',
    'Ida': '02',
    'Julius': '058',
    'Kaufmann': '4366',
    'Ludwig': '5234',
    'Martha': '672',
    'Nordpol': '67215',
    'Otto': '02',
    'Ökonom': '0466',
    'Paula': '15',
    'Quelle': '45',
    'Richard': '7472',
    'Samuel': '865',
    'Theodor': '227',
    'Ulrich': '0574',
    'Übermut': '01762',
    'Viktor': '3427',
    'Wilhelm': '3556',
    'Xanthippe': '48621',
    'Ypsilon': '01856',
    'Zacharias': '8478'
}

abstände = []  #Liste zur Speicherung aller Abständen
comparison_count = 1  # Zähler für die Anzahl der Vergleiche

# Erstellen Sie eine Wortliste, um den indexierten Zugriff zu erleichtern
wörter = list(phonetic_codes.keys())

# Iterieren über jedes Codepaar und berechnen Sie Hamming-Abstände
for i in range(len(wörter)):
    for j in range(i+1, len(wörter)):
        wort1, code1 = wörter[i], phonetic_codes[wörter[i]]
        wort2, code2 = wörter[j], phonetic_codes[wörter[j]]
        max_len = max(len(code1), len(code2))
        code1, code2 = code1.zfill(max_len), code2.zfill(max_len)
        distance = hamming_abstand(code1, code2)
        abstände.append(distance)  # Speicherung von Abständen
        print(f"{comparison_count}. Hamming distance between {wort1} ({code1}) and {wort2} ({code2}): {distance}")
        comparison_count += 1  # Increment des Vergleichszählers

# Berechnung maximale, minimale und durchschnittliche Abstände
max_hamming_abstand = max(abstände)
min_hamming_abstand = min(abstände)
durch_hamming_abstand = sum(abstände) / len(abstände)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"\nMaximaler Hamming-Abstand: {max_hamming_abstand}")
print(f"Minimaler Hamming-Abstand: {min_hamming_abstand}")
print(f"Durchschnittlicher Hamming-Abstand:: {durch_hamming_abstand:.2f}")
