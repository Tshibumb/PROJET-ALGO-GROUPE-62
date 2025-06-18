import re

def nettoyer_ligne(ligne, ignorer_casse=True, supprimer_ponctuation=True):
    if ignorer_casse:
        ligne = ligne.lower()
    if supprimer_ponctuation:
        ligne = re.sub(r'[\W_]+', ' ', ligne)
    ligne = ligne.strip()
    return ligne

def pretraiter_texte(lignes, mode_strict=False):
    if mode_strict:
        return [ligne.strip() for ligne in lignes]
    else:
        return [nettoyer_ligne(ligne) for ligne in lignes]
