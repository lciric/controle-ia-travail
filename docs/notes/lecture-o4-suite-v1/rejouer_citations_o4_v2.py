"""Rejeu indépendant des citations de la note de lecture O4 (v2, écrit par le contre-lecteur).

N'importe rien de l'outil de l'auteur (verifier_citations_o4_v1.py). Pour chaque citation de la liste :
  1. l'empreinte du PDF est recalculée et comparée à son compagnon .sha256 ;
  2. la page indiquée est extraite seule par « pdftotext -f P -l P », avec puis sans -layout ;
  3. texte et citation sont normalisés (NFKC : ligatures fi/fl ; guillemets et tirets typographiques ;
     césures de fin de ligne ; espaces) ;
  4. la citation est cherchée sur la page ; trois niveaux, du plus strict au plus lâche :
       « stricte »       : sous-chaîne, espaces réduits, césures laissées telles quelles ;
       « cesure »        : sous-chaîne après recollage des mots coupés en fin de ligne ;
       « sans_espaces »  : sous-chaîne après suppression de tous les espaces (signalée comme plus faible) ;
  5. si elle manque sur la page indiquée, toutes les pages sont parcourues et les pages où elle figure sont rendues.
Contrôle annexe (option --note) : chaque citation « [CLÉ p. N] « … » » de la note figure-t-elle dans la liste,
à la même page, et réciproquement.

Usage : python3 -I rejouer_citations_o4_v2.py RACINE_PIECES LISTE.json SORTIE.json [--note NOTE.md]
L'heure du rejeu est prise par « date -u », jamais écrite à la main.
"""
import hashlib
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

TRADUCTION = {
    "‘": "'", "’": "'", "‚": "'", "‛": "'", "′": "'",
    "“": '"', "”": '"', "„": '"', "«": '"', "»": '"',
    "‐": "-", "‑": "-", "‒": "-", "–": "-", "—": "-", "−": "-",
    "­": "", " ": " ", " ": " ",
}


def base(s):
    s = unicodedata.normalize("NFKC", s)
    return "".join(TRADUCTION.get(ch, ch) for ch in s)


def formes(s):
    """Rend les trois formes normalisées d'un texte."""
    b = base(s)
    stricte = re.sub(r"\s+", " ", b).strip()
    recolle = re.sub(r"(\w)-[ \t]*\n\s*(\w)", r"\1\2", b)
    cesure = re.sub(r"\s+", " ", recolle).strip()
    sans = re.sub(r"\s+", "", recolle)
    return stricte, cesure, sans


def niveau(citation, page_texte):
    cs, cc, cx = formes(citation)
    ps, pc, px = formes(page_texte)
    if cs in ps:
        return "stricte"
    if cc in pc or cs in pc:
        return "cesure"
    if cx in px or cx.replace("-", "") in px.replace("-", ""):
        return "sans_espaces"
    return None


def extraire(pdf, page, layout):
    cmd = ["pdftotext", "-f", str(page), "-l", str(page)] + (["-layout"] if layout else []) + [str(pdf), "-"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"pdftotext a échoué sur {pdf} p. {page} : {r.stderr.strip()}")
    return r.stdout


def nombre_pages(pdf):
    r = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True)
    m = re.search(r"^Pages:\s+(\d+)", r.stdout, re.M)
    if not m:
        raise RuntimeError(f"pdfinfo ne rend pas le nombre de pages de {pdf}")
    return int(m.group(1))


def controle_empreinte(pdf):
    reelle = hashlib.sha256(pdf.read_bytes()).hexdigest()
    comp = Path(str(pdf) + ".sha256")
    if not comp.is_file():
        return reelle, None, False
    attendue = comp.read_text(encoding="utf-8").split()[0]
    return reelle, attendue, reelle == attendue


def citations_de_la_note(chemin):
    texte = Path(chemin).read_text(encoding="utf-8")
    motif = re.compile(r"\[([A-Z]+) p\. (\d+)(?: \((\d+)\))?\] « (.+?) »")
    return [{"cle": m.group(1), "page": int(m.group(2)), "texte": m.group(4)} for m in motif.finditer(texte)]


def main(argv):
    note = None
    if "--note" in argv:
        i = argv.index("--note")
        note = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]
    racine, liste, sortie = Path(argv[1]), Path(argv[2]), Path(argv[3])
    citations = json.loads(liste.read_text(encoding="utf-8"))
    heure = subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True).stdout.strip()
    version = subprocess.run(["pdftotext", "-v"], capture_output=True, text=True).stderr.splitlines()[0]
    empreintes, pages_cache, resultats = {}, {}, []

    def page(pdf, p, layout):
        k = (pdf, p, layout)
        if k not in pages_cache:
            pages_cache[k] = extraire(pdf, p, layout)
        return pages_cache[k]

    for n, c in enumerate(citations, 1):
        pdf = racine / c["pdf"]
        if pdf not in empreintes:
            empreintes[pdf] = controle_empreinte(pdf) + (nombre_pages(pdf),)
        reelle, attendue, conforme, npages = empreintes[pdf]
        p = c["page"]
        n_layout = niveau(c["texte"], page(pdf, p, True)) if 1 <= p <= npages else None
        n_brut = niveau(c["texte"], page(pdf, p, False)) if 1 <= p <= npages else None
        ailleurs = []
        if not (n_layout or n_brut):
            for q in range(1, npages + 1):
                if q != p and (niveau(c["texte"], page(pdf, q, False)) or niveau(c["texte"], page(pdf, q, True))):
                    ailleurs.append(q)
        ordre = ["stricte", "cesure", "sans_espaces"]
        trouves = [x for x in (n_layout, n_brut) if x]
        resultats.append({
            "numero": n, "cle": c["cle"], "pdf": c["pdf"], "page": p, "texte": c["texte"],
            "sha256_pdf": reelle, "sha256_compagnon": attendue, "empreinte_conforme": conforme,
            "pages_du_pdf": npages,
            "niveau_avec_layout": n_layout, "niveau_sans_layout": n_brut,
            "meilleur_niveau": min(trouves, key=ordre.index) if trouves else None,
            "trouvee_sur_la_page": bool(trouves),
            "pages_ou_trouvee_si_ailleurs": ailleurs,
        })

    total = len(resultats)
    ok = sum(r["trouvee_sur_la_page"] for r in resultats)
    bilan = {
        "heure_du_rejeu_utc": heure, "outil_d_extraction": version,
        "liste": str(liste), "sha256_liste": hashlib.sha256(liste.read_bytes()).hexdigest(),
        "citations": total, "trouvees_sur_la_page_indiquee": ok,
        "resultat": f"{ok} sur {total}",
        "par_niveau": {k: sum(r["meilleur_niveau"] == k for r in resultats) for k in ("stricte", "cesure", "sans_espaces")},
        "trouvees_avec_layout": sum(bool(r["niveau_avec_layout"]) for r in resultats),
        "trouvees_sans_layout": sum(bool(r["niveau_sans_layout"]) for r in resultats),
        "pdf_distincts": len(empreintes),
        "pdf_empreinte_conforme": sum(v[2] for v in empreintes.values()),
    }
    if note:
        dans_note = citations_de_la_note(note)
        cle_liste = {(c["cle"], c["page"], formes(c["texte"])[0]) for c in citations}
        cle_note = {(c["cle"], c["page"], formes(c["texte"])[0]) for c in dans_note}
        bilan["note"] = {
            "chemin": str(note), "sha256": hashlib.sha256(Path(note).read_bytes()).hexdigest(),
            "citations_relevees_dans_la_note": len(dans_note), "distinctes": len(cle_note),
            "dans_la_note_absentes_de_la_liste": sorted([list(x) for x in cle_note - cle_liste]),
            "dans_la_liste_absentes_de_la_note": sorted([list(x) for x in cle_liste - cle_note]),
        }
    sortie.write_text(json.dumps({"bilan": bilan, "citations": resultats}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(bilan, ensure_ascii=False, indent=1))
    for r in resultats:
        if not r["trouvee_sur_la_page"] or r["meilleur_niveau"] != "stricte" or not r["empreinte_conforme"]:
            print("À VOIR", r["numero"], r["cle"], r["page"], r["meilleur_niveau"], r["pages_ou_trouvee_si_ailleurs"], r["texte"][:70])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
