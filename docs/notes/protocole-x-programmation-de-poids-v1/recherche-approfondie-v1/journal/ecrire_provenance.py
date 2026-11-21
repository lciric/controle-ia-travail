#!/usr/bin/env python3
"""Écrit la table de provenance des sources versées (par programme : pdfinfo, empreinte recalculée,
tampon de la première page comparé au nom du fichier, titre et auteurs repris des réponses brutes d'arXiv)."""
import glob, hashlib, os, re, subprocess, sys, datetime
import xml.etree.ElementTree as ET
NS = {"a": "http://www.w3.org/2005/Atom"}
meta = {}
for f in sorted(glob.glob("journal/brut/*-arxiv.xml")):
    try: root = ET.parse(f).getroot()
    except Exception: continue
    for e in root.findall("a:entry", NS):
        ident = e.find("a:id", NS).text.rsplit("/abs/", 1)[-1]
        base = re.sub(r"v\d+$", "", ident)
        title = re.sub(r"\s+", " ", e.find("a:title", NS).text).strip()
        auts = [a.find("a:name", NS).text.strip() for a in e.findall("a:author", NS)]
        meta[base] = (title, auts, ident)
lus = {
 "2611.19216v1": ("1 à 16 en entier ; 17 à 20 dans la limite de 9 000 signes par page ; 24 à 28 survolées (2 600 signes par page) ; 21 à 23 non lues ; tableaux 3 et 4 relus en colonnes", "verdict 1 à 3 ; sections 3 à 5"),
 "2606.15980v2": ("1 à 9 (texte en entier ; références des p. 8 et 9 tronquées)", "verdict 1 ; sections 3 et 4"),
 "2610.28366v1": ("1 ; recherche de motifs sur tout le texte (mises à jour, adaptateurs, quantification)", "section 3"),
 "2606.08106v1": ("1, 2", "section 3"),
 "2611.21885v2": ("1, 2 ; recherche de motifs de sécurité sur tout le texte", "verdict 5 ; section 2"),
 "2611.13232v1": ("1, 2", "section 2"),
 "2611.23880v1": ("1, 2", "section 3"),
 "2610.04575v1": ("1, 2", "section 3"),
 "2607.02510v1": ("1, 2", "section 3"),
 "2606.15474v1": ("1, par motifs (quatre phrases contrôlées)", "section 3"),
 "2611.04192v1": ("1, par motifs (cinq phrases et chiffres contrôlés)", "section 3"),
 "2609.17560v1": ("1, par motifs (quatre phrases et chiffres contrôlés)", "section 3"),
 "2507.21509v3": ("6 et 7, par motifs ; fin de la p. 7 lue", "section 3"),
 "2604.12359v1": ("1, par motifs", "section 2"),
 "2609.36490v1": ("aucune (versé ; cité d'après la description qu'en donnent Shire et Kim, p. 3)", "section 3"),
 "2611.24330v1": ("1, par motifs", "section 2"),
 "2611.07847v2": ("1", "section 2"),
}
out = []
out.append("# Provenance des sources — recherche approfondie sur la programmation de poids (v1)\n")
out.append("- **Pour** : la note `reponse-fable-programmation-de-poids-approfondie-v1.md`, même dossier parent. Pièce de travail (classe C).")
out.append("- **Téléchargés** le 2026-11-21 entre 18:13 et 18:25 UTC, sans compte ni clé, par un client générique (`generic-research-client/1.0`), depuis `export.arxiv.org/pdf/<identifiant>` ; heures et codes dans `journal/journal-des-versements-v1.tsv`.")
out.append("- **Écart déclaré au préambule** : les sources sont versées ici, sous le dossier de la note, et non sous `docs/sources/pdf/` : le mandat calculé dit « n'écris nulle part ailleurs ».")
out.append("- **Table écrite par programme** (`journal/ecrire_provenance.py`) le %s : pages par `pdfinfo`, empreinte recalculée et comparée au compagnon `.sha256` (assertion), tampon d'arXiv lu sur la première page et comparé au nom du fichier (assertion), titre et auteurs repris des réponses brutes de l'interface d'arXiv (`journal/brut/`)." % datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%SZ"))
out.append("- **« Pages lues »** : rang de la page dans le fichier, texte extrait par `pdftotext` ; aucune figure regardée ; « par motifs » = phrases cherchées et relues, non la page entière. Seules les phrases et chiffres cités dans la note, à la page dite, sont opposables (R7).\n")
out.append("## PDF versés\n")
out.append("| fichier | pages | octets | SHA-256 | titre ; auteurs | tampon de la p. 1 | pages lues | emploi |")
out.append("|---|---|---|---|---|---|---|---|")
for f in sorted(glob.glob("sources/*.pdf")):
    name = os.path.basename(f); ident = name[:-4]; base = re.sub(r"v\d+$", "", ident)
    h = hashlib.sha256(open(f, "rb").read()).hexdigest()
    comp = open(f + ".sha256").read().split()[0]
    assert h == comp, name
    pages = re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", f], capture_output=True).stdout.decode()).group(1)
    p1 = subprocess.run(["pdftotext", "-f", "1", "-l", "1", f, "-"], capture_output=True).stdout.decode("utf-8", "replace")
    m = re.search(r"arXiv:(\d{4}\.\d{4,5}v\d+)\s*\[[^\]]+\]\s*(\d{1,2} \w{3} \d{4})", p1)
    assert m and m.group(1) == ident, (name, m.group(1) if m else None)
    title, auts, _ = meta.get(base, ("(titre non relevé)", [], ""))
    a = ", ".join(auts[:6]) + (" et al." if len(auts) > 6 else "")
    pl, emploi = lus[ident]
    out.append("| `%s` | %s | %d | `%s` | %s ; %s | arXiv:%s, %s | %s | %s |" % (name, pages, os.path.getsize(f), h, title, a, m.group(1), m.group(2), pl, emploi))
out.append("\n## Copies de pages web (empreintées, non opposables au sens de R7 sauf mention)\n")
out.append("| fichier | octets | SHA-256 | ce que c'est |")
out.append("|---|---|---|---|")
web = {
 "billet-origine-programmation-de-poids-releve-2026-11-21.html": "le billet du 2 novembre 2026 qui nomme la programmation de poids (quatre auteurs d'un laboratoire universitaire), relevé à son adresse publique ; lu par extraction du texte et par motifs de sécurité",
 "liste-publique-principale-releve-2026-11-21.md": "la liste publique principale, tenue par un tiers et mise à jour chaque jour (664 entrées au relevé) ; mise en table par programme (`journal/liste-publique-principale.tsv`)",
 "liste-publique-seconde-releve-2026-11-21.md": "une seconde liste publique, non dépouillée (69 identifiants d'arXiv distincts)",
}
for n, d in web.items():
    f = "sources/" + n
    h = hashlib.sha256(open(f, "rb").read()).hexdigest()
    assert h == open(f + ".sha256").read().split()[0]
    out.append("| `%s` | %d | `%s` | %s |" % (n, os.path.getsize(f), h, d))
out.append("\n## Pièce du dépôt relue (non reversée)\n")
out.append("- `docs/sources/pdf/2602.15515v2.pdf` (Taufeeque et al., « The Obfuscation Atlas », 30 pages, empreinte égale à celle de la table de provenance de la note v2) : p. 25 (annexe P, lue) et p. 28 (début, tableau non extrait) ; recherche de motifs sur tout le texte.\n")
out.append("## Connus sans PDF (aucun chiffre opposable)\n")
out.append("- **Soumissions anonymes à des conférences** (dépôt de relectures ; résumés lus dans la réponse brute de son interface, empreintée dans `journal/brut/` ; le téléchargement des PDF demande une vérification humaine, refusée à mon client) : « Fighting the Drift: Probe Transfer Across Post-Training Stages » (forum LHVG1HENCR) ; « Rankings Survive, Scales Drift: Hidden-State Error Estimation Across Post-Training » (6c789WUOjg) ; « Frozen Input-Harm Probes under Compression » (Y8x0hfaJmc) ; « SAVER: Sequential Anytime-Valid Editing Risk-control in Large Language Models » (ElpQeeyTLm) ; « Statistical Rank Transport for Efficient Conformal Recalibration After Model Updates » (gxTTerbmox) ; « Continual Calibration: Stale Conformal Thresholds Fail Under Lifelong LLM Fine-Tuning » (vTEaDFYVQC, retirée) ; « Learning to Test: Sequential Monitoring of Generative Models and Agents » (Xbj61gw8Zb) ; « How Much Must We Test After an Agent Update? » (BITzeyyfel, atelier). « The base case: Safety probes trained on the base model best withstand post-training and fine-tuning » (5FjW0gaVe9) n'est connue que par la description de Shire et Kim, p. 3.")
out.append("- **Billets de forum** (corps lu dans la réponse brute de la recherche du forum, empreintée) : « Continual learning might make your blocking monitors nearly useless » (24 septembre 2026, forum d'alignement) ; « Held-out Monitors Sometimes Degrade, Even When Not Trained Against » (29 juillet 2026) ; « An overview of frontier AI company monitoring practices in mid 2026 » (7 octobre 2026) ; cinq billets sur la programmation de poids (5 au 17 novembre 2026).")
out.append("- **Résumés d'arXiv seuls** (réponses brutes empreintées) : les 33 notices qui portent l'expression exacte et une vingtaine de notices voisines ; liste dans la note, annexe.")
out.append("- **Noms de fichiers d'un autre dossier** (`opus-max-v1/sources/`, vus en listant le dossier de la note, jamais ouverts) : 28 identifiants ; titres relevés par une requête à l'interface d'arXiv (`journal/brut/`, dernière réponse d'arXiv).")
open("sources/provenance-recherche-approfondie-programmation-de-poids-v1.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
print("écrit :", len(glob.glob("sources/*.pdf")), "PDF")
