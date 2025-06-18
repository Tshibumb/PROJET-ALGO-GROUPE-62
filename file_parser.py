import os
import fitz  # PyMuPDF

# Lire le contenu d'un fichier texte

def lire_fichier_txt(chemin):
    try:
        with open(chemin, 'r', encoding='utf-8') as f:
            return f.readlines()
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier texte : {e}")
        return []

# Extraire le texte d'un fichier PDF ligne par ligne

def lire_fichier_pdf(chemin):
    try:
        texte = ""
        with fitz.open(chemin) as doc:
            for page in doc:
                texte += page.get_text()
        return texte.splitlines()
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier PDF : {e}")
        return []

# Lire un fichier quel que soit son type

def lire_fichier(chemin):
    if not os.path.exists(chemin):
        print(f"Fichier introuvable : {chemin}")
        return []
    if chemin.lower().endswith(".txt"):
        return lire_fichier_txt(chemin)
    elif chemin.lower().endswith(".pdf"):
        return lire_fichier_pdf(chemin)
    else:
        print("Format de fichier non supporté. Utilisez .txt ou .pdf")
        return []



