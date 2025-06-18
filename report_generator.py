# report_generator.py

def afficher_resultats(lignes_identiques, lignes_diff, taux_similarite, communs, uniques1, uniques2, fichier1, fichier2):
    print("\n===== Résumé de la comparaison =====\n")
    print(f"Fichiers comparés : '{fichier1}' et '{fichier2}'")
    print(f"Taux de similarité : {taux_similarite}%")
    print(f"Nombre de lignes identiques : {len(lignes_identiques)}")
    print(f"Nombre de lignes différentes : {len(lignes_diff)}\n")

    print("Lignes identiques (numéro de ligne et contenu) :")
    for num, contenu in lignes_identiques:
        print(f"  Ligne {num}: {contenu}")

    print("\nLignes différentes (numéro de ligne, fichier1, fichier2) :")
    for num, ligne1, ligne2 in lignes_diff:
        print(f"  Ligne {num}:")
        print(f"    - {fichier1}: {ligne1 if ligne1 else '<aucune ligne>'}")
        print(f"    + {fichier2}: {ligne2 if ligne2 else '<aucune ligne>'}")

    print("\nMots communs dans les deux fichiers :")
    print(", ".join(communs) if communs else "<Aucun mot commun>")

    print("\nMots uniques à", fichier1, ":")
    print(", ".join(uniques1) if uniques1 else "<Aucun mot unique>")

    print("\nMots uniques à", fichier2, ":")
    print(", ".join(uniques2) if uniques2 else "<Aucun mot unique>")

def exporter_rapport(nom_fichier, lignes_identiques, lignes_diff, taux_similarite, communs, uniques1, uniques2):
    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write("===== Rapport de comparaison =====\n\n")
        f.write(f"Taux de similarité : {taux_similarite}%\n")
        f.write(f"Nombre de lignes identiques : {len(lignes_identiques)}\n")
        f.write(f"Nombre de lignes différentes : {len(lignes_diff)}\n\n")

        f.write("Lignes identiques (numéro de ligne et contenu) :\n")
        for num, contenu in lignes_identiques:
            f.write(f"  Ligne {num}: {contenu}\n")

        f.write("\nLignes différentes (numéro de ligne, fichier1, fichier2) :\n")
        for num, ligne1, ligne2 in lignes_diff:
            f.write(f"  Ligne {num}:\n")
            f.write(f"    - Fichier 1: {ligne1 if ligne1 else '<aucune ligne>'}\n")
            f.write(f"    + Fichier 2: {ligne2 if ligne2 else '<aucune ligne>'}\n")

        f.write("\nMots communs dans les deux fichiers :\n")
        f.write(", ".join(communs) + "\n" if communs else "<Aucun mot commun>\n")

        f.write("\nMots uniques au fichier 1 :\n")
        f.write(", ".join(uniques1) + "\n" if uniques1 else "<Aucun mot unique>\n")

        f.write("\nMots uniques au fichier 2 :\n")
        f.write(", ".join(uniques2) + "\n" if uniques2 else "<Aucun mot unique>\n")

