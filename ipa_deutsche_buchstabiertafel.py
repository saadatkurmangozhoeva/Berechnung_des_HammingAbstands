import panphon.distance
dist = panphon.distance.Distance()

ipa_transkriptionen = [
    'ˈantoːn', 'ˈbɛʁta', 'ˈt͡sɛːzaʁ', 'ˈdoːʁa', 'eˈmiːl',
    'ˈfʁiːdʁɪç', 'ˈɡʊstaːf', 'ˈhaɪ̯nʁɪç', 'ˈiːda', 'ˈjuːliʊs',
    'ˈkaʊ̯fman', 'ˈluːtvɪç', 'ˈmaʁta', 'ˈnɔʁtpoːl', 'ˈɔto',
    'ˈpaʊ̯la', 'ˈkvɛlə', 'ˈʁɪçaʁt', 'ˈziːkfʁiːt', 'teˈoːdoʁ',
    'ˈʊlʁɪç', 'ˈvɪktoːʁ', 'ˈvɪlhɛlm', 'ˈksantɪpə', 'ˈʏpsilɔn',
    't͡saˈkaːʁi̯as', 'ˈɛʁɡɐ', 'økoˈnoːm', 'ˈyːbɐmuːt', 'ɛsˈt͡sɛt'
]


abstände = []
comparison_count = 1

# Hamming-Abstände berechnen und Ergebnisse sammeln
for i, wort1 in enumerate(ipa_transkriptionen):
    for wort2 in ipa_transkriptionen[i+1:]:
        astand = dist.hamming_feature_edit_distance(wort1, wort2)
        abstände.append(astand)
        print(f"{comparison_count}) Hamming Abstand zwischen '[{wort1}]' und '[{wort2}]': {astand}")
        comparison_count += 1


min_abstand = min(abstände)
max_abstand = max(abstände)
average_abstand = sum(abstände) / len(abstände)
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(f"\nMinimaler Hamming-Abstand: {min_abstand}")
print(f"Maximaler Hamming-Abstand: {max_abstand}")
print(f"Durchschnittlicher Hamming-Abstand: {average_abstand}")

