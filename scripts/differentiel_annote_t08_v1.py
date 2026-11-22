#!/usr/bin/env python3
"""Différentiel annoté, ligne par ligne, entre les deux fichiers copiés de la chaîne de T0.8 et leurs modèles de la course de
confirmation (consigne de la chaîne de lancement, `722ceb5e…`, tenue en v3 `6f52c4db…` ; texte au brouillon 15 `8d68b7a0…`, § 4, dernier point). v1.

Pour chaque bloc de `diff -u` (modèle → copie), chaque ligne retirée (« − ») et ajoutée (« + ») est recopiée, numérotée, avec
la raison du bloc (`RAISONS`, écrites par le développeur de la chaîne ; elles renvoient aux points de la consigne, § 3.4 et
§ 3.5). Une ligne d'un bloc sans raison arrête le programme : aucune ligne changée n'est laissée sans raison.

    python3 -B scripts/differentiel_annote_t08_v1.py > docs/notes/t08-chaine-de-lancement-v1/differentiel-annote-v3.md
"""
from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
PAIRES = (("scripts/lancer_t06_v13.sh", "scripts/lancer_t08_v1.sh"),
          ("scripts/amorce_instance_t06_v11.sh", "scripts/amorce_instance_t08_v1.sh"))
L34 = "§ 3.4"
L35 = "§ 3.5"
RAISONS = {
    "scripts/lancer_t08_v1.sh": {
        1: f"{L34} : en-tête T0.8 ajouté (changements déclarés, usage) ; le texte de la v13 est conservé en dessous.",
        2: f"{L34} « les noms … la branche de sortie par défaut, la branche d'entrée, l'amorce citée » ; « la ligne de GO, "
           "toujours par la variable GO_ID » : identifiant de la course en dur retiré, lecture de la ligne d'épreuve de T0.6 "
           "(plafond_ligne_go) retirée ; module de session de T0.8 (prolongation, calendrier, vue de l'offre, compte rendu) ; "
           "programme de vérification de la branche d'entrée.",
        3: f"{L34} : `controles` — texte scellé sur main (S) et son sceau ; branche d'entrée relevée et vérifiée par programme "
           "(liste blanche, orpheline, empreintes) ; commit du code = COMMIT_CODE_T08, ancêtre de la branche du code ; amorce "
           "citée par son empreinte (ordre de course) et son compagnon ; GO, fin de validité et calendrier lus au registre ; "
           "vue de l'offre (bornes de « Machine ») ; plafond 120 et compte rendu 40 consignés. Les huit citations du texte de "
           "T0.6 n'ont pas d'équivalent dans le texte de T0.8 (retirées). `controles-epreuve` : refusée, code 2 (aucune "
           "épreuve à blanc dans l'ordre de course de T0.8). `creation` : carte `relance` refusée (aucune H200, ni automatique "
           "ni proposée) ; branche des épreuves retirée ; GO de l'environnement égal à celui des contrôles ; plafond 120 lu "
           "dans la configuration ; calendrier lu au registre ; simulation d'épuisement refusée ; GO revérifié au jour de la "
           "création ; bornes lues dans la vue de l'offre ; commande de création portant les variables de la branche "
           "d'entrée, du code et du GO, et le nom du lanceur de T0.8. Contre-lecture M-5 : échéance de la machine = heure du plafond restant par défaut, une échéance donnée ne peut que l'avancer (la v13 prenait la fin du GO).",
        4: f"{L34} « les noms » : le lanceur cité dans les messages d'après la création est celui de T0.8. Contre-lecture M-2 : l'étiquette du chemin « offre refusée » est lue dans la vue de l'offre.",
        5: f"{L34} : plafond de la surveillance lu dans lancement.txt, 120 exigé, sans valeur par défaut (la v13 prenait 200) ; "
           "seuil du compte rendu (40 USD) relu.",
        6: f"{L34} « les noms » : ligne d'en-tête de la surveillance ; alerte unique du compte rendu déclarée.",
        7: f"{L34} « compte rendu à 40 USD » : la décision vient du module de session de T0.8 (celle de la v3 plus l'alerte "
           "du compte rendu) ; deux heures sans progression : alerte sans arrêt, inchangé. Contre-lecture M-3 : la ligne « FIN » imprime la destruction par l'identifiant, non plus l'arrêt qui garde le disque.",
        8: f"{L34} « compte rendu à 40 USD » : l'alerte n'est écrite qu'une fois (fichier compte-rendu-alerte.txt) ; "
           "`--verifier-go-seulement` : vérifie la ligne GO_ID contre la configuration (prolongation, plafond), plus la ligne "
           "d'épreuve de T0.6 (premier argument : la configuration, non un plafond d'épreuve).",
    },
    "scripts/amorce_instance_t08_v1.sh": {
        1: f"{L35} : en-tête T0.8 ajouté (changements déclarés) ; le texte de la v11 est conservé en dessous.",
        2: f"{L35} « les noms » ; GO de la course reçu du lanceur (GO_ID_T08), jamais en dur.",
        3: f"{L35} « les noms » (fichiers de travail t08) ; minuterie : « montants de T0.8 » (120 USD) dans sa ligne de "
           "journal ; mécanisme inchangé. Contre-lecture M-3 : à l'heure du plafond restant, consignation puis destruction (plus de `PUT stopped`).",
        4: f"{L35} « les noms » (fichiers de travail, lignes « AMORCE T08 »).",
        5: f"{L35} « les noms » (fichiers de travail). Contre-lecture M-3 : fonction `versement_prouve` (tête distante = tête locale).",
        6: f"{L35} « les noms » ; « montants de T0.8 » (message de l'heure d'épuisement) ; variables de la branche d'entrée, "
           "du code et du GO exigées ; texte scellé et branche de sortie de T0.8 par défaut ; bloc des épreuves à blanc "
           "retiré (refus explicite) ; « le clonage » : code au commit cité, une seule branche, sans étiquettes, extraction "
           "limitée (12 motifs relevés en jouant la liste d'essais figée sur un clone réduit, `.gitignore` compris), branche "
           "d'entrée seule, fichiers recopiés à l'octet ; commit local de la course (consigne v3, § 3.5 : liste attendue "
           "écrite avant depuis la configuration, branche d'entrée égale à elle, chemins ajoutés aux motifs d'extraction, "
           "auteur et date fixés, seul parent COMMIT, rien de gelé) ; garde précoce sur le disque (aucun lecture-sondes-t06* "
           "ni resume.json), arbre propre exigé ; ajouts par `git add --sparse` (sorties hors des motifs) ; « les noms » (script de consignation) ; données légères : les sorties de la "
           "course de T0.8 seulement (jamais les entrées de 7b) ; morceaux d'activations retirés (bras propre à la course de "
           "confirmation). Contre-lecture M-5 : échéance ramenée à l'heure du plafond restant, plus à la fin du GO ; M-3 : second démarrage après une fin normale, destruction si le versement est prouvé.",
        7: f"{L35} « les noms » (messages de commit T0.8, verrou) ; GO lu au registre du commit par le module de T0.8 "
           "(prolongation comprise) au lieu des modules de T0.6 ; citations : la configuration et le texte scellé passés par "
           "le lanceur (le texte de T0.8 ne porte pas les citations de T0.6) ; calendrier lu au registre ; « le nombre "
           "attendu » d'essais ne vient plus du texte mais de l'amorce (bloc 9). Contre-lecture M-5 : le refus « échéance après la fin du GO » est retiré.",
        8: f"{L35} « les noms » (traces, verrou, fin anormale) ; « les bras propres à la course de confirmation (audit de "
           "fuite, sondes) sont retirés » : bras B retiré ; environnement Python hors du dépôt ($R/venv-t08) : la garde de "
           "l'instance parcourt tout le dépôt.",
        9: f"{L35} « avant tout calcul : exiger_instance_sans_interdits (garde resserrée du code aligné, run de 7b lu dans "
           "la configuration), le commit du code égal à celui du texte scellé (commit local : seul parent COMMIT = "
           "COMMIT_CODE_T08), le texte scellé intact » ; « la liste d'essais ciblée et figée de T0.8, dans un fichier à part, avec le nombre "
           "attendu » (empreinte et nombre écrits en dur).",
        10: f"{L35} : suite figée jouée sans l'essai du code aligné qui clone l'arbre entier du dépôt (désélection, comptée "
            "« 1 deselected ») ; « les modèles … chargés l'un après l'autre » (préchargés au cache local, la course les charge hors ligne) ; "
            "« la commande jouée : python -m controle_ia.t08.course_v1 --config … --run-id … --prereg …, une fois ».",
        11: f"{L35} : fin du run reconnue sur le résultat de la course de T0.8 (course-t08.json) et son arrêt de garde "
            "(« ARRÊT : … ») au lieu de resume.json et arret.json de T0.6.",
        12: f"{L35} « la fin » : message de commit T0.8 ; morceaux d'activations retirés ; « les noms ».",
        13: f"{L35} « la fin » : « les noms » ; bras B retiré de la fin normale. Contre-lecture M-3 : fin normale, destruction après le versement prouvé, sinon arrêt (disque gardé).",
    },
}


def blocs(modele: str, copie: str) -> list[dict]:
    d = subprocess.run(["diff", "-u", str(RACINE / modele), str(RACINE / copie)], capture_output=True, text=True).stdout
    out, cur = [], None
    for l in d.splitlines():
        m = re.match(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@", l)
        if m:
            cur = {"modele": int(m.group(1)), "copie": int(m.group(3)), "lignes": []}
            out.append(cur)
            lm, lc = cur["modele"], cur["copie"]
        elif cur is not None and l and l[0] in " -+" and not l.startswith(("---", "+++")):
            if l[0] == "-":
                cur["lignes"].append(("−", lm, l[1:]))
                lm += 1
            elif l[0] == "+":
                cur["lignes"].append(("+", lc, l[1:]))
                lc += 1
            else:
                lm += 1
                lc += 1
    return out


def main() -> int:
    print("# Différentiel annoté de la chaîne de lancement de T0.8 — v3\n")
    print("Engendré par `scripts/differentiel_annote_t08_v1.py`. Chaque ligne retirée (−, numéro dans le modèle) ou ajoutée "
          "(+, numéro dans la copie) porte la raison de son bloc. Lignes tronquées à 200 caractères ; le fichier entier fait foi.\n")
    for modele, copie in PAIRES:
        e = lambda p: hashlib.sha256((RACINE / p).read_bytes()).hexdigest()   # noqa: E731
        print(f"## `{copie}` (`{e(copie)}`) contre `{modele}` (`{e(modele)}`)\n")
        bs = blocs(modele, copie)
        nr = sum(1 for b in bs for x in b["lignes"] if x[0] == "−")
        na = sum(1 for b in bs for x in b["lignes"] if x[0] == "+")
        print(f"{len(bs)} blocs ; {nr} lignes retirées, {na} ajoutées.\n")
        for i, b in enumerate(bs, start=1):
            r = RAISONS.get(copie, {}).get(i)
            if not r:
                print(f"bloc {i} de {copie} sans raison : arrêt", file=sys.stderr)
                return 1
            print(f"### Bloc {i} (modèle l. {b['modele']}, copie l. {b['copie']})\n\n**Raison** : {r}\n")
            print("| | l. | ligne |\n|---|---|---|")
            for s, n, t in b["lignes"]:
                t = t.replace("|", "\\|").replace("`", "'")
                print(f"| {s} | {n} | `{t[:200]}{'…' if len(t) > 200 else ''}` |")
            print()
        if len(bs) != len(RAISONS.get(copie, {})):
            print(f"{copie} : {len(bs)} blocs, {len(RAISONS.get(copie, {}))} raisons : arrêt", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
