"""Candidat 2 de T0.6 = candidat 1 + les 12 couples de la contre-lecture du lanceur v3 (fille 9, lignée Opus 5.5 ; liste nue,
copiée à l'octet dans ce dossier, numérotés 1 à 12 dans l'ordre), appliqués dans l'ordre, puis les substitutions D01 et suivantes
(`substitutions-candidat2-v1.json` : lanceur v4, décisions de Lazar du 6 novembre 2026, valeurs connaissables). Chaque « ancien » doit
apparaître exactement le nombre de fois attendu (1 par défaut) au moment de son application ; sinon arrêt, rien d'écrit.
Valeurs calculées ici, jamais saisies à la main : {HEURE} (`date -u`), {ENTROPIE} (`numpy.random.SeedSequence().entropy`, tirée une
fois, R9, sans lecture de données), {SHA_CL3}, {SHA_COUPLES}, {SHA_CORR4} (empreintes des pièces sur disque, préfixes vérifiés),
{SHA_TACHES_E}, {SHA_TACHES_D}, {SHA_CONSIGNES} (empreintes relevées sur les fichiers cités, égales à celles de la configuration du
brouillon 4), {CHEMIN_*} (chemins de cette configuration), {RAPPORTS} (empreintes des rapports du développeur v1 à v4, relevées dans l'arbre du code).
Bibliothèque standard + numpy ; aucun réseau, aucune clé. Journal écrit à côté (`journal-candidat2-v1.md`).

    python3 -I -B appliquer-candidat2-v1.py RACINE_DU_DEPOT RACINE_DU_CODE
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ICI = Path(__file__).resolve().parent
CANDIDAT1 = "brouillons/T0.6-organismes-v0-v1-candidat1.md"
SHA_CANDIDAT1 = "4c27a254ef6ec255d3abf43a4fd6c9a0b6ffd0d24e9513ae28b0a3af6b91d8b3"
CANDIDAT2 = "brouillons/T0.6-organismes-v0-v1-candidat2.md"
NOTES = "docs/notes/g0-deux-semaines-v1"
CL3 = f"{NOTES}/contre-lecture-lanceur-T0.6-v3/contre-lecture-lanceur-T0.6-v3.md"
CORR4 = f"{NOTES}/contre-lecture-lanceur-T0.6-v3/corrections-code-lanceur-T0.6-v4.md"
COUPLES_NOM = "couples-candidat1-vers-candidat2-T0.6-v1.json"
COUPLES_SRC = f"{NOTES}/contre-lecture-lanceur-T0.6-v3/{COUPLES_NOM}"
PREFIXES = {"cl3": "b338a812", "couples": "2880c1a6", "corr4": "65259028"}
CONFIG_B4 = f"{NOTES}/config-t06-reel-v1-brouillon4.json"
MARQUEUR = re.compile(r"<<[A-Z0-9_]+>>")
MARQUEURS_ATTENDUS = {"COMMIT_CODE_T06", "EMPREINTES_CODE_T06", "EMPREINTE_AMORCE_T06", "EMPREINTE_PREREG_P3BIS", "EMPREINTE_PREREG_T07",
                      "LONGUEURS_TEXTES_P3", "SCRIPT_PUISSANCE_V3", "TESTS_ATTENDUS_T06", "VALEURS_CITEES_T06"}
CLES = ["Entropie", "Commit du code d'analyse", "Configuration de T0.6 (empreinte canonique)", "Tâches d'évaluation de T0.6", "Tests attendus",
        "Chemin de la configuration de T0.6", "Chemin des tâches d'évaluation de T0.6", "Chemin des tâches de distillation de T0.6", "Chemin des consignes de P3"]
FORME_AMORCE = "`scripts/amorce_instance_t06_v4.sh` (`"


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def appliquer(texte: str, ident: str, ancien: str, nouveau: str, attendu: int, journal: list) -> str:
    n = texte.count(ancien)
    if n != attendu:
        raise SystemExit(f"{ident} : « ancien » trouvé {n} fois, {attendu} attendu : arrêt, rien d'écrit")
    journal.append(f"| {ident} | {texte[: texte.index(ancien)].count(chr(10)) + 1} | {attendu} | {len(ancien)} | {len(nouveau)} |")
    return texte.replace(ancien, nouveau)


def main(racine: Path, code: Path) -> int:
    c1 = racine / CANDIDAT1
    if sha(c1) != SHA_CANDIDAT1:
        raise SystemExit("candidat 1 : empreinte non conforme")
    sortie = racine / CANDIDAT2
    if sortie.exists():
        raise SystemExit(f"{sortie} existe déjà : rien d'écrasé (R12)")
    sha_cl3, sha_corr4, sha_couples = sha(racine / CL3), sha(racine / CORR4), sha(racine / COUPLES_SRC)
    for cle, valeur in (("cl3", sha_cl3), ("corr4", sha_corr4), ("couples", sha_couples)):
        if not valeur.startswith(PREFIXES[cle]):
            raise SystemExit(f"{cle} : empreinte {valeur[:12]}… ≠ préfixe attendu {PREFIXES[cle]}")
    if (ICI / COUPLES_NOM).read_bytes() != (racine / COUPLES_SRC).read_bytes():
        raise SystemExit("copie des couples non égale à l'octet à la source")
    couples = json.loads((ICI / COUPLES_NOM).read_text(encoding="utf-8"))
    if not (isinstance(couples, list) and len(couples) == 12):
        raise SystemExit("couples : liste nue de 12 couples attendue")
    subs_p = ICI / "substitutions-candidat2-v1.json"
    subs = json.loads(subs_p.read_text(encoding="utf-8"))["substitutions"]
    # valeurs calculées
    cfg = json.loads((code / CONFIG_B4).read_text(encoding="utf-8"))
    sources = []
    def fichier_cite(cle_cfg: str, sha_cle: str | None):
        if sha_cle is None:
            chemin, attendu = cfg[cle_cfg]["chemin"], cfg[cle_cfg]["sha256"]
        else:
            chemin, attendu = cfg[cle_cfg], cfg[sha_cle]
        f = racine / chemin
        if not f.is_file() or not (racine / (chemin + ".sha256")).is_file():
            raise SystemExit(f"{chemin} ou son sceau absent")
        if sha(f) != attendu:
            raise SystemExit(f"{chemin} : empreinte {sha(f)[:12]}… ≠ celle de la configuration du brouillon 4 ({attendu[:12]}…)")
        sources.append(f"- `{chemin}` : `{attendu}` (sceau `{chemin}.sha256` présent ; égale à la configuration `{CONFIG_B4}` de l'arbre du code)")
        return chemin, attendu
    chemin_e, sha_e = fichier_cite("taches_evaluation", None)
    chemin_d, sha_d = fichier_cite("taches_distillation", None)
    chemin_c, sha_c = fichier_cite("chemin_consignes", "consignes_sha256")
    rapports = []
    for v in (1, 2, 3, 4):
        r = code / NOTES / f"rapport-developpeur-lanceur-T0.6-v{v}.md"
        if not r.is_file():
            raise SystemExit(f"{r} absent de l'arbre du code")
        rapports.append(f"v{v} `{sha(r)}`")
    import numpy as np
    entropie = int(np.random.SeedSequence().entropy)
    maintenant = datetime.now(timezone.utc)
    heure = maintenant.strftime("%H:%M")
    rempl = {"{HEURE}": heure, "{ENTROPIE}": str(entropie), "{SHA_CL3}": sha_cl3, "{SHA_COUPLES}": sha_couples, "{SHA_CORR4}": sha_corr4,
             "{SHA_TACHES_E}": sha_e, "{SHA_TACHES_D}": sha_d, "{SHA_CONSIGNES}": sha_c, "{CHEMIN_TACHES_E}": chemin_e,
             "{CHEMIN_TACHES_D}": chemin_d, "{CHEMIN_CONSIGNES}": chemin_c, "{RAPPORTS}": ", ".join(rapports)}
    texte = c1.read_text(encoding="utf-8")
    journal = ["| couple ou substitution | ligne (au moment de l'application) | occurrences | longueur ancien | longueur nouveau |", "|---|---|---|---|---|"]
    for i, c in enumerate(couples, 1):
        texte = appliquer(texte, f"couple {i}", c["ancien"], c["nouveau"], 1, journal)
    for s in subs:
        ancien, nouveau = s["ancien"], s["nouveau"]
        for k, v in rempl.items():
            ancien, nouveau = ancien.replace(k, v), nouveau.replace(k, v)
        texte = appliquer(texte, s["id"], ancien, nouveau, int(s.get("occurrences", 1)), journal)
    # vérifications du résultat (arrêt, rien d'écrit, si l'une échoue)
    restes = re.findall(r"\{[A-Z_0-9]+\}", texte)
    if restes:
        raise SystemExit(f"accolades non résolues : {sorted(set(restes))}")
    marqueurs = sorted({m.strip("<>") for m in MARQUEUR.findall(texte)})
    if set(marqueurs) != MARQUEURS_ATTENDUS:
        raise SystemExit(f"marqueurs : {marqueurs}, attendus : {sorted(MARQUEURS_ATTENDUS)}")
    comptes_m = {m: texte.count(f"<<{m}>>") for m in marqueurs}
    lignes = texte.split("\n")
    comptes_c = {k: sum(1 for l in lignes if f"{k} : `" in l) for k in CLES}
    if comptes_c["Tests attendus"] != 1 or any(n > 1 for n in comptes_c.values()):
        raise SystemExit(f"clés lues par la chaîne : {comptes_c}")
    if comptes_c["Entropie"] != 1 or comptes_c["Tâches d'évaluation de T0.6"] != 1 or comptes_c["Chemin des consignes de P3"] != 1:
        raise SystemExit(f"clés remplies absentes : {comptes_c}")
    if texte.count(FORME_AMORCE) != 1:
        raise SystemExit(f"forme de citation de l'amorce {FORME_AMORCE!r} : {texte.count(FORME_AMORCE)} ≠ 1")
    if "`à remplir au candidat 2`" in texte:
        raise SystemExit("valeur « à remplir au candidat 2 » en accents graves restante")
    sortie.write_text(texte, encoding="utf-8")
    restes_v3 = [(i, l[:100]) for i, l in enumerate(lignes, 1) if "lancer_t06_v3" in l or "amorce_instance_t06_v3" in l]
    j = [f"# Journal du candidat 2 de T0.6 — {maintenant.strftime('%Y-%m-%dT%H:%M:%SZ')} (`date -u`)", "",
         f"- candidat 1 : `{CANDIDAT1}`, `{SHA_CANDIDAT1}` (empreinte vérifiée avant tout)",
         f"- contre-lecture du lanceur v3 : `{CL3}`, `{sha_cl3}` ; corrections de code v4 : `{CORR4}`, `{sha_corr4}`",
         f"- couples : `{COUPLES_NOM}` (copie à l'octet dans ce dossier, comparée à `{COUPLES_SRC}`), `{sha_couples}`, 12 couples, appliqués dans l'ordre",
         f"- substitutions : `substitutions-candidat2-v1.json`, `{sha(subs_p)}`, {len(subs)} substitutions, appliquées après les couples",
         f"- script : `appliquer-candidat2-v1.py`, `{sha(Path(__file__).resolve())}`", "",
         f"Valeurs connaissables remplies, avec leur source :", "", f"- entropie `{entropie}` : `numpy.random.SeedSequence().entropy` (numpy {np.__version__}), tirée une fois à {maintenant.strftime('%H:%M:%S')} UTC, aucune donnée lue (R9)",
         *sources, *[f"- rapport du développeur {r} (arbre du code : `{code}`)" for r in rapports], "", *journal, "",
         f"Marqueurs du candidat 2 (`<<[A-Z0-9_]+>>`), {len(marqueurs)} distincts (occurrences) :", "", *[f"- `{m}` : {n}" for m, n in comptes_m.items()], "",
         "Marqueurs remplis par rapport au candidat 1 : `MOT_LAZAR_DT` (mots de Lazar du 6 novembre, R-1623 et R-1624), `ENTROPIE_T06`, `EMPREINTE_RAPPORT_LANCEUR_T06`.",
         "Marqueurs restants et pourquoi : `COMMIT_CODE_T06`, `EMPREINTES_CODE_T06`, `EMPREINTE_AMORCE_T06` (commit du code de la course, après fusion et contre-lecture) ;",
         "`EMPREINTE_PREREG_T07`, `EMPREINTE_PREREG_P3BIS` (aucun préenregistrement scellé de T0.7 « coût » ni de P3-bis sous `prereg/` au 6 novembre) ;",
         "`LONGUEURS_TEXTES_P3`, `SCRIPT_PUISSANCE_V3` (pas de sortie des longueurs IA/IT/IM ni de script de puissance v3 dans le dépôt) ; `TESTS_ATTENDUS_T06` (rempli par E3) ;",
         "`VALEURS_CITEES_T06` : deux valeurs restent (empreinte canonique de la configuration réelle scellée, chemin de la configuration copiée sous `prereg/`).", "",
         "Clés lues par la chaîne (lignes qui portent « clé : » suivi d'un accent grave ; « Tests attendus » exactement 1, les autres au plus 1) :", "",
         *[f"- « {k} : ` » : {n}" for k, n in comptes_c.items()], "", f"- forme de citation de l'amorce « {FORME_AMORCE} » : 1", "",
         f"- mentions restantes de `lancer_t06_v3` ou `amorce_instance_t06_v3` ({len(restes_v3)}, historiques : statut antérieur, point 8 du candidat 1, traitement) :",
         *[f"  - ligne {i} : {t}" for i, t in restes_v3], "",
         f"- résultat : `{CANDIDAT2}`, `{sha(sortie)}`, {texte.count(chr(10)) + 1} lignes"]
    (ICI / "journal-candidat2-v1.md").write_text("\n".join(j) + "\n", encoding="utf-8")
    print("\n".join(j))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()))
