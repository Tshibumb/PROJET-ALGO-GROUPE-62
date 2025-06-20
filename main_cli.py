from file_parser import lire_fichier
from text_preprocessor import pretraiter_texte
from comparison_engine import comparer_lignes, comparer_mots, rechercher_mot_cle
from report_generator import afficher_resultats, exporter_rapport

def main():
    f1 = input("Chemin du premier fichier (.txt ou .pdf) : ")
    f2 = input("Chemin du deuxième fichier (.txt ou .pdf) : ")

    lignes1 = lire_fichier(f1)
    lignes2 = lire_fichier(f2)

    mode_strict = input("Mode strict ? (o/n) : ").lower() == 'o'

    lignes1 = pretraiter_texte(lignes1, mode_strict)
    lignes2 = pretraiter_texte(lignes2, mode_strict)

    lignes_identiques, lignes_diff, taux = comparer_lignes(lignes1, lignes2)
    communs, uniques1, uniques2 = comparer_mots(lignes1, lignes2)

    afficher_resultats(lignes_identiques, lignes_diff, taux, communs, uniques1, uniques2, f1, f2)

    mot = input("Saisir un mot à rechercher : ")
    freq1 = rechercher_mot_cle(lignes1, mot)
    freq2 = rechercher_mot_cle(lignes2, mot)
    print(f"\nMot '{mot}' - Présence dans {f1}: {freq1} fois, dans {f2}: {freq2} fois")

    exporter_rapport("rapport_comparaison.txt", lignes_identiques, lignes_diff, taux, communs, uniques1, uniques2)
    print("\nRapport exporté dans 'rapport_comparaison.txt'")
    
main()

