import re
import string
from PyPDF2 import PdfReader

def read_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def read_pdf(file_path):
    text = ""
    reader = PdfReader(file_path)
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def clean_text(text):
    # enlève ponctuation, espaces multiples, passe en minuscules
    text = text.lower()
    text = re.sub(rf'[{re.escape(string.punctuation)}]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def compare_texts(text1, text2, ignore_case=True, clean=False, mode='strict', keyword=""):
    if clean:
        text1 = clean_text(text1)
        text2 = clean_text(text2)
    elif ignore_case:
        text1 = text1.lower()
        text2 = text2.lower()

    lines1 = text1.splitlines()
    lines2 = text2.splitlines()
    max_len = max(len(lines1), len(lines2))

    identical = 0
    diff = 0
    only_1 = 0
    only_2 = 0
    detailed_diff = []

    for i in range(max_len):
        l1 = lines1[i] if i < len(lines1) else ""
        l2 = lines2[i] if i < len(lines2) else ""

        if l1 == l2:
            identical += 1
            detailed_diff.append("  " + l1)
        elif l1 and not l2:
            only_1 += 1
            detailed_diff.append("- " + l1)
        elif not l1 and l2:
            only_2 += 1
            detailed_diff.append("+ " + l2)
        else:
            diff += 1
            if mode == 'souple':
                # dans le mode souple on peut essayer de nettoyer et comparer mot à mot
                # mais ici on affiche juste les deux lignes avec indicateurs
                detailed_diff.append("- " + l1)
                detailed_diff.append("+ " + l2)
            else:
                detailed_diff.append("- " + l1)
                detailed_diff.append("+ " + l2)

    words1 = set(text1.split())
    words2 = set(text2.split())

    unique_1 = words1 - words2
    unique_2 = words2 - words1

    total_lines = max_len
    similarity = (identical / total_lines) * 100 if total_lines > 0 else 0

    keyword = keyword.lower()
    kw_count1 = len(re.findall(r'\b' + re.escape(keyword) + r'\b', text1)) if keyword else 0
    kw_count2 = len(re.findall(r'\b' + re.escape(keyword) + r'\b', text2)) if keyword else 0

    return {
        "total_lines": total_lines,
        "identical": identical,
        "diff": diff,
        "only_1": only_1,
        "only_2": only_2,
        "similarity": similarity,
        "unique_1": unique_1,
        "unique_2": unique_2,
        "keyword": keyword,
        "kw_count1": kw_count1,
        "kw_count2": kw_count2,
        "detailed_diff": detailed_diff
    }

def generate_report(res):
    lines = []
    lines.append(f"Total lignes comparées : {res['total_lines']}")
    lines.append(f"Lignes identiques : {res['identical']}")
    lines.append(f"Lignes différentes : {res['diff']}")
    lines.append(f"Lignes seulement dans fichier 1 : {res['only_1']}")
    lines.append(f"Lignes seulement dans fichier 2 : {res['only_2']}")
    lines.append(f"Taux de similarité : {res['similarity']:.2f} %\n")

    lines.append(f"Mots présents uniquement dans fichier 1 ({len(res['unique_1'])}):")
    lines.append(", ".join(sorted(res['unique_1'])) + "\n")

    lines.append(f"Mots présents uniquement dans fichier 2 ({len(res['unique_2'])}):")
    lines.append(", ".join(sorted(res['unique_2'])) + "\n")

    if res['keyword']:
        lines.append(f'Mot-clé "{res["keyword"]}" trouvé {res["kw_count1"]} fois dans fichier 1, {res["kw_count2"]} fois dans fichier 2.\n')

    lines.append("Différences ligne par ligne :")
    lines.extend(res['detailed_diff'])

    return "\n".join(lines)

def main():
    print("=== Comparateur de fichiers TXT/PDF ===")
    f1 = input("Chemin fichier 1 (.txt ou .pdf) : ").strip()
    f2 = input("Chemin fichier 2 (.txt ou .pdf) : ").strip()

    # Lecture fichiers
    def read_file(path):
        if path.lower().endswith(".pdf"):
            return read_pdf(path)
        else:
            return read_txt(path)

    try:
        text1 = read_file(f1)
        text2 = read_file(f2)
    except Exception as e:
        print("Erreur lecture fichiers :", e)
        return

    # Options utilisateur
    ic = input("Ignorer la casse ? (O/n) : ").strip().lower() != 'n'
    clean = input("Nettoyer ponctuation et espaces ? (O/n) : ").strip().lower() != 'n'
    mode = input("Mode (strict/souple) [strict] : ").strip().lower()
    if mode not in ['strict', 'souple']:
        mode = 'strict'
    keyword = input("Mot-clé à rechercher (laisser vide si aucun) : ").strip()

    res = compare_texts(text1, text2, ignore_case=ic, clean=clean, mode=mode, keyword=keyword)

    report = generate_report(res)
    print("\n=== Rapport de comparaison ===\n")
    print(report)

    save = input("\nSauvegarder le rapport dans 'rapport_comparaison.txt' ? (O/n) : ").strip().lower() != 'n'
    if save:
        with open("rapport_comparaison.txt", "w", encoding="utf-8") as f:
            f.write(report)
        print("Rapport sauvegardé dans 'rapport_comparaison.txt'.")

if __name__ == "__main__":
    main()

