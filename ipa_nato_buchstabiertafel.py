import panphon.distance
dist = panphon.distance.Distance()

ipa_transkriptionen = [
    'ˈælfə', 'ˈbrɑː.voʊ', 'ˈtʃɑːr.li', 'ˈdeltə', 'ˈekoʊ',
    'ˈfɒkstrɒt', 'ɡɒlf', 'hoʊˈtel', 'ˈɪndi.ə', 'ˈdʒuːli.ɛt',
    'ˈkiː.loʊ', 'ˈliːmə', 'maɪk', 'noʊˈvembər', 'ˈɒskər',
    'pəˈpɑː', 'kwɪˈbek', 'ˈroʊ.mi.oʊ', 'siˈɛrə', 'ˈtæŋɡoʊ',
    'ˈjuː.nɪ.fɔːrm', 'ˈvɪktər', 'ˈwɪski', 'ˈɛks reɪ', 'ˈjæŋki', 'ˈzuːluː'
]
abstände= []
comparison_count = 1

# Hamming-Abstände berechnen und Ergebnisse sammeln
for i, wort1 in enumerate(ipa_transkriptionen):
    for wort2 in ipa_transkriptionen[i+1:]:
        abstand = dist.hamming_feature_edit_distance(wort1, wort2)
        abstände.append(abstand)
        print(f"{comparison_count}) Hamming Abstand zwischen '[{wort1}]' und '[{wort2}]': {abstand}")
        comparison_count += 1


min_abstand = min(abstände)
max_abstand = max(abstände)
average_abstand = sum(abstände) / len(abstände)

print(f"\nMinimaler Hamming-Abstand: {min_abstand}")
print(f"Maximaler Hamming-Abstand: {max_abstand}")
print(f"Durchschnittlicher Hamming-Abstand: {average_abstand}")
