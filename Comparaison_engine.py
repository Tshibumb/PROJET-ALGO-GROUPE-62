from difflib import SequenceMatcher
from collections import Counter

# Calcul du taux de similarité ligne par ligne (basé sur difflib)
def comparer_lignes(lignes1, lignes2):
    lignes_identiques = []
    lignes_diff = []
    total = max(len(lignes1), len(lignes2))
    total = total if total > 0 else 1  # éviter division par zéro

    # Comparaison ligne par ligne
    for i in range(total):
        l1 = lignes1[i] if i < len(lignes1) else ''
        l2 = lignes2[i] if i < len(lignes2) else ''
        if l1 == l2:
            lignes_identiques.append((i+1, l1))
        else:
            lignes_diff.append((i+1, l1, l2))

    nb_identiques = len(lignes_identiques)
    taux = round((nb_identiques / total) * 100, 2)
    return lignes_identiques, lignes_diff, taux

# Comparaison mot à mot (calcul de mots communs et uniques)
def comparer_mots(lignes1, lignes2):
    mots1 = Counter(" ".join(lignes1).split())
    mots2 = Counter(" ".join(lignes2).split())

    communs = set(mots1.keys()) & set(mots2.keys())
    uniques1 = set(mots1.keys()) - set(mots2.keys())
    uniques2 = set(mots2.keys()) - set(mots1.keys())

    return sorted(communs), sorted(uniques1), sorted(uniques2)

# Recherche d'un mot-clé dans un document
def rechercher_mot_cle(lignes, mot):
    texte = " ".join(lignes).lower()
    return texte.split().count(mot.lower())
