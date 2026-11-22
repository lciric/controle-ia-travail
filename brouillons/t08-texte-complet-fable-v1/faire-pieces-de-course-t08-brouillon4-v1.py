#!/usr/bin/env python3
"""Écrit le brouillon 4 de l'ordre de course et de la consigne du lecteur de la base boîte noire (T0.8), à partir de
leurs brouillons 3, par opérations déclarées. Cause unique : le rendu du développeur de la chaîne de lancement
(rapport v2), qui donne les commandes exactes, le chemin du fichier d'échantillon et dix réserves.
La consigne du juge de verdict reste au brouillon 3.
Règles : empreinte de chaque entrée exigée ; chaque texte ancien trouvé exactement une fois ; rien n'est écrasé (R12).
Usage, depuis la racine du dépôt : python3 brouillons/t08-texte-complet-fable-v1/faire-pieces-de-course-t08-brouillon4-v1.py
"""
import hashlib
import sys
from pathlib import Path

DOSSIER = Path("docs/procedures/t08-course-v1")
ORDRE_3 = ("ordre-course-t08-v1-brouillon3.md", "6922ada9651f4bbcb9d9347dff105c003c136c702a63b79cc3e5a4f7ae6d01e8")
LECTEUR_3 = ("consigne-lecteur-t08-v1-brouillon3.md", "6a39a5d9aa1dc0e289494c0fea0828fdc8216f866f0358b08446605881c89cdf")
RAPPORT = ("`docs/notes/t08-chaine-de-lancement-v1/rapport-chaine-de-lancement-t08-v2.md` "
           "(`47da96229401335b5b87b32111b4df1d56bb7da15a33c94fd21288d33aaf13b7`, branche `t08/chaine-de-lancement-v1`, "
           "commit `12eb328a6bf84960116e4b26bbad332f0df0f257`)")
VERIF = ("`prereg/contre-lectures/T0.8-pieces-de-course-v1-brouillon2-verification-cl1.md` "
         "(`4440161d1fbc9150a6b0aca0c40ef9f314d2e0608db7813e4f892f52e310614b`) et `…-brouillon3-verification-cl1.md` "
         "(`d24b216b752b80e16133232ae9779bbd890c13d2a962d8a50a40a98fd03428bd`)")

SECTION_13 = "\n".join([
    "",
    "",
    "## 13. Commandes exactes",
    "",
    "Source : rapport du développeur de la chaîne de lancement, § 8, " + RAPPORT + ". Elles sont recopiées, non "
    "réécrites. **Elles ne valent qu'au commit `C` que cite `CODE-T08`**, après la contre-lecture de la chaîne "
    "(préalable P7) : si cette contre-lecture change une commande, cet ordre change par un brouillon neuf.",
    "",
    "**Valeurs données par la session mère au scellement**, écrites au journal de l'exécutante avant l'étape 2 : `S`, "
    "commit de `main` qui ajoute le texte scellé ; `C`, commit du code (marqueur `COMMIT_CODE_T08`), qui porte le code "
    "aligné et la chaîne de lancement ; `BC`, branche qui porte `C` ; `EA`, empreinte de "
    "`scripts/amorce_instance_t08_v1.sh` au commit `C` ; `GO`, `GO-2026-11-10-12` jusqu'au 30 novembre, "
    "`GO-2026-11-22-79` à partir du 1er décembre ; `ANT`, dépense antérieure sous cet accord. `D` est le dossier de "
    "travail neuf ; `ID`, l'identifiant de la machine, lu dans `$D/lancement.txt`. Branche d'entrée : "
    "`entree/t08-course-v1` ; branche de sortie : `calcul/t08-course-v1`. Crédit exigé au préalable P9 : au moins 57 "
    "USD, pire cas d'une tentative (section 6).",
    "",
    "**Toutes les commandes se lancent depuis un clone de `main` à jour** : sur une branche dont le registre des "
    "accords porte une ligne illisible, la garde de calcul refuse toute commande de lancement (rapport, réserve 3).",
    "",
    "Avant l'étape 2, par la session mère, au scellement (rappel ; ce n'est pas un geste de l'exécutante) : la "
    "configuration réelle de la course (`scripts/ecrire_configuration_course_t08_v1.py`), puis la branche d'entrée "
    "(`scripts/construire_branche_entree_t08_v1.py construire`), aux commandes du rapport, § 8.",
    "",
    "- **P1** : `sha256sum prereg/T0.8-bases-boite-noire-v0-v1.md && cat prereg/T0.8-bases-boite-noire-v0-v1.md.sha256 "
    "&& grep '^| SCELLEMENT-T08 ' registres/scellements-v1.md`, puis `PYTHONPATH=src python3 -c 'import sys; from "
    "controle_ia.prereg import problemes; p = problemes(\"prereg/T0.8-bases-boite-noire-v0-v1.md\"); print(p); "
    "sys.exit(1 if p else 0)'`.",
    "- **P2** : `grep '^| CODE-T08 ' registres/scellements-v1.md && git merge-base --is-ancestor $C origin/$BC`.",
    "- **P3** : `PYTHONPATH=src python3 -m controle_ia.t08.passage_a_blanc_v1 --config "
    "prereg/T0.8-configuration-course-v1.json --registre registres/scellements-v1.md --prereg "
    "prereg/T0.8-bases-boite-noire-v0-v1.md --racine-piece .` (code 0 exigé) ; essai de la garde : `PYTHONPATH=src "
    "python3 -m pytest -q tests/test_t08_chaine_lecture_v1.py -k passage_a_blanc`.",
    "- **P4** : `GO_ID=$GO bash scripts/lancer_t08_v1.sh --verifier-go-seulement "
    "prereg/T0.8-configuration-course-v1.json $ANT` ; garde à blanc et dates simulées : `PYTHONPATH=src python3 -m "
    "pytest -q tests/test_t08_chaine_lancement_v1.py -k \"garde_de_calcul or accord_prolonge or "
    "sans_identifiant_echu\"`.",
    "- **P6** : `python3 -I -B scripts/construire_branche_entree_t08_v1.py verifier --depot . --ref "
    "refs/remotes/origin/entree/t08-course-v1 --commit-texte $S --texte prereg/T0.8-bases-boite-noire-v0-v1.md "
    "--config prereg/T0.8-configuration-course-v1.json`.",
    "- **P7** : `sha256sum scripts/amorce_instance_t08_v1.sh scripts/lancer_t08_v1.sh "
    "scripts/construire_branche_entree_t08_v1.py scripts/tests-cibles-t08-v1.txt`, à comparer au rapport de "
    "contre-lecture de la chaîne ; puis, dans la session, l'essai que l'amorce écarte de la machine : `PYTHONPATH=src "
    "python3 -m pytest -q \"tests/test_t08_entrees_rendu_v1.py::test_amorce_instance_clone_de_l_arbre_aligne\"`.",
    "- **P8** : `PYTHONPATH=src python3 -m pytest -q tests/test_t08_chaine_lancement_v1.py -k \"minuterie or "
    "plafond_restant or deux_heures\"`.",
    "- **Étape 3** : `GO_ID=$GO T08_BRANCHE_ENTREE=entree/t08-course-v1 T08_BRANCHE_CODE=$BC T08_AMORCE_SHA256=$EA bash "
    "scripts/lancer_t08_v1.sh controles $D`. Code 0 exigé ; clés `HF_TOKEN` et `CONTROLE_IA_GITHUB_TOKEN` présentes "
    "par leur nom.",
    "- **Étapes 4 et 5** : `GO_ID=$GO bash scripts/lancer_t08_v1.sh creation auto course $ANT $D` ; la commande de "
    "création est imprimée, non exécutée. À relire : carte, prix, `--disk 100`, amorce, `BRANCHE_ENTREE` et "
    "`ENTREE_COMMIT`, `COMMIT=$C`, `GO_ID=$GO`, et `DEPENSE_EPUISEE_UTC_S`, l'heure du plafond restant. Codes : 0, "
    "commande imprimée ; 2, échec ; 3, nœud (aucune offre conforme, machine déjà présente, reste nul).",
    "- **Étape 6** : exécuter la commande imprimée, telle quelle. Code 5 : offre retirée ; rejouer `creation` comme "
    "imprimé, trois essais au plus, puis nœud.",
    "- **Étape 8** : `INTERVALLE=1800 bash scripts/lancer_t08_v1.sh surveillance $ID $D`. Codes : 0, fin ; 3, arrêt ; "
    "4, refus de l'amorce.",
    "- **Étape 9** : `git fetch origin refs/heads/calcul/t08-course-v1:refs/remotes/origin/calcul/t08-course-v1 && git "
    "ls-tree -r -l refs/remotes/origin/calcul/t08-course-v1 -- runs diag donnees traces` ; empreinte du résultat : `git "
    "show refs/remotes/origin/calcul/t08-course-v1:diag/<run>/course-t08.json | sha256sum`, à comparer au compagnon ; "
    "commit du manifeste : `PYTHONPATH=src python3 -I -B -c \"import sys; sys.path.insert(0, 'src'); from "
    "controle_ia.lancement_t08 import commit_local_v1 as c; sys.exit(c.main(sys.argv[1:]))\" verifier-distant . "
    "refs/remotes/origin/calcul/t08-course-v1 $C refs/remotes/origin/entree/t08-course-v1` (code 0 exigé).",
    "- **Étape 11** : `vastai destroy instance $ID`, puis `vastai show instances --raw`. L'amorce laisse la machine à "
    "l'état arrêté en fin de course ; elle n'est détruite que par ce geste, après l'étape 9.",
    "",
    "**Deux différences avec la consigne de la chaîne, déclarées par le développeur et acceptées ici** : (1) l'heure "
    "du plafond restant retranche aussi le forfait de téléchargement (environ 2 USD), comme la chaîne de la course de "
    "confirmation — la minuterie tombe un peu plus tôt, jamais plus tard ; (2) un essai du code aligné, qui clone "
    "l'arbre entier, est écarté de la suite jouée sur la machine et joué dans la session (P7).",
    "",
    "**Jamais joué avant la course** (rapport, réserve 6) : le mode réel sur une carte, le vrai loueur, la poussée vers "
    "le dépôt distant depuis un clone partiel. Une panne à l'un de ces points relève de la section 9.",
    "",
])

OPS_ORDRE = [
    ("renvoi", "sur une machine louée — v1 — brouillon 3", "sur une machine louée — v1 — brouillon 4"),
    ("commandes",
     "- **Statut** : **brouillon 3**, pièce de classe A, **non exécutable** : la chaîne de lancement n'existe pas "
     "encore (section 3, préalable P7). Il inscrit au brouillon 2",
     "- **Statut** : **brouillon 4**, pièce de classe A : **le brouillon des commandes**. Il ajoute au brouillon 3 (`"
     + ORDRE_3[1] + "`) les commandes exactes rendues par le développeur de la chaîne de lancement (section 13), et "
     "ce que son rapport demande à l'ordre (P7, étape 9) ; opérations : `journal-pieces-de-course-t08-brouillon4-v1.md`. "
     "**Il n'est exécutable qu'une fois la chaîne contre-lue et les préalables P1 à P10 tenus.** Le brouillon 3 "
     "inscrivait au brouillon 2"),
    ("commandes",
     "; le brouillon des commandes y portera les commandes exactes, quand la chaîne sera écrite et contre-lue. Aucune "
     "machine ne se crée sur ce brouillon.",
     "; ce brouillon 4 y porte les commandes exactes. Aucune machine ne se crée tant qu'un préalable manque."),
    ("renvoi", "les corrections des brouillons 2 et 3 sont à vérifier par le même contre-lecteur.",
     "les brouillons 2 et 3 ont été vérifiés conformes par le même contre-lecteur (" + VERIF + ") ; la différence de "
     "ce brouillon 4 est à vérifier de même."),
    ("commandes", "leurs empreintes sont celles de cet ordre (brouillon des commandes) |",
     "leurs empreintes au commit `C` sont celles du rapport de contre-lecture de la chaîne ; l'essai du code aligné "
     "que l'amorce écarte de la machine est joué dans la session au commit `C`, réussi (section 13) |"),
    ("renvoi", "Les commandes exactes sont au brouillon des commandes.", "Les commandes exactes sont en section 13."),
    ("commandes",
     "Un écart : c'est le quatrième arrêt de la section 7, et l'étape 10 bis.",
     "Un écart : c'est le quatrième arrêt de la section 7, et l'étape 10 bis. **Fin en anomalie de taille** (rapport de "
     "la chaîne, réserve 5 : un fichier de plus de 90 Mo est retiré du commit et reste sur la machine) : aucune "
     "destruction, aucune ligne `COURSE-T08` ; nœud pour la session mère, qui décide du versement (section 8)."),
    ("renvoi", "sous sa consigne (`consigne-lecteur-t08-v1-brouillon3.md`)",
     "sous sa consigne (`consigne-lecteur-t08-v1-brouillon4.md`)"),
    ("renvoi", "## 12. À écrire au brouillon des commandes", "## 12. Ce qui était à écrire, et qui l'est en section 13"),
    ("commandes", "l'identifiant de la session exécutante.",
     "l'identifiant de la session exécutante (donné par la session mère)." + SECTION_13.rstrip("\n")),
]

OPS_LECTEUR = [
    ("renvoi", "jouer la lecture sur processeur — v1 — brouillon 3", "jouer la lecture sur processeur — v1 — brouillon 4"),
    ("commandes",
     "- **Statut** : brouillon 3. Il inscrit au brouillon 2",
     "- **Statut** : brouillon 4, **le brouillon des commandes**. Il ajoute au brouillon 3 (`" + LECTEUR_3[1] + "`) "
     "les commandes de la lecture, le chemin du fichier d'échantillon et la règle des messages d'arrêt, d'après le "
     "rapport du développeur de la chaîne de lancement, " + RAPPORT + " ; différence à vérifier par le même "
     "contre-lecteur. Le brouillon 3 inscrivait au brouillon 2"),
    ("commandes",
     "La commande exacte de la lecture vient au brouillon des commandes, quand l'entrée en ligne de commande existera "
     "(consigne de la chaîne de lancement, § 3.3).",
     "Les commandes exactes sont au § 5 ; elles ne valent qu'au commit que cite `CODE-T08`, après la contre-lecture de "
     "la chaîne de lancement."),
    ("arrêts",
     "les messages d'arrêt et les lignes de progression du programme, qui ne portent que des noms d'étape et d'état "
     "(consigne de la chaîne de lancement, § 3.3).",
     "les lignes de progression du programme, qui ne portent que des noms d'étape et d'état, et ses messages d'arrêt, "
     "dont cinq peuvent porter un nombre tiré des données (rapport de la chaîne de lancement, réserve 9) : tu ne les "
     "transmets pas (§ 5)."),
    ("commandes", "Tu joues **une fois** la commande de la lecture (brouillon des commandes),",
     "Tu écris la configuration de la lecture, puis tu joues **une fois** la commande de la lecture (les deux "
     "ci-dessous),"),
    ("commandes",
     "et s'arrête sur toute ligne de la liste d'arrêt.",
     "et s'arrête sur toute ligne de la liste d'arrêt.\n\n"
     "- Configuration : `PYTHONPATH=src python3 -B scripts/ecrire_configuration_lecture_t08_v1.py --texte "
     "prereg/T0.8-bases-boite-noire-v0-v1.md --config-course prereg/T0.8-configuration-course-v1.json --registre "
     "registres/scellements-v1.md [--hd <chemins de la pièce HD>] --sortie prereg/T0.8-configuration-lecture-v1.json` ; "
     "l'option entre crochets ne se passe que si la session mère t'a donné la ligne de journal du préalable 6.\n"
     "- Lecture : `PYTHONPATH=src python3 -m controle_ia.t08.lire_v1 --config "
     "prereg/T0.8-configuration-lecture-v1.json --run-id <AAAAMMJJ-HHMMSS>-t08-lecture --prereg "
     "prereg/T0.8-bases-boite-noire-v0-v1.md`. Sa sortie ne porte que des chemins et des empreintes.\n"),
    ("arrêts",
     "Tu recopies le message d'arrêt tel quel et tu le rends à la session mère.",
     "Tu ne recopies pas le message d'arrêt à la session mère, qui ne doit recevoir aucun nombre tiré des résultats "
     "(§ 7) : tu lui rends le fait de l'arrêt, avec le chemin et l'empreinte de `arret-lecture-t08.json`, que tu scelles "
     "et pousses avec ce que le programme a écrit ; le juge de verdict le lira."),
    ("commandes", "brouillon des commandes : chemin du fichier d'échantillon",
     "fichier `diag/<run de la lecture>/echantillon-audit-r4-t08.json`, dont le programme imprime le chemin et "
     "l'empreinte, ou `null` si l'audit n'est pas déclenché"),
    ("arrêts", "- Tout message d'arrêt, tel quel ; tout refus d'outil ;",
     "- Tout arrêt, par le chemin et l'empreinte de `arret-lecture-t08.json`, jamais par son texte ; tout refus "
     "d'outil ;"),
]

PIECES = [(ORDRE_3, "ordre-course-t08-v1-brouillon4.md", OPS_ORDRE),
          (LECTEUR_3, "consigne-lecteur-t08-v1-brouillon4.md", OPS_LECTEUR)]
JOURNAL = "journal-pieces-de-course-t08-brouillon4-v1.md"


def sha(o: bytes) -> str:
    return hashlib.sha256(o).hexdigest()


def debut(t: str) -> str:
    t = t.replace("\n", " ⏎ ").replace("|", "¦")
    return t if len(t) <= 110 else t[:110] + "…"


def main() -> int:
    sorties = [DOSSIER / n for _, n, _ in PIECES] + [DOSSIER / JOURNAL]
    if any(p.exists() for p in sorties):
        print("ARRET : sortie déjà là, rien n'est écrasé (R12)", file=sys.stderr)
        return 2
    lignes = ["# Journal — brouillons 4 de l'ordre de course et de la consigne du lecteur (T0.8)", "",
              "Écrit par `brouillons/t08-texte-complet-fable-v1/faire-pieces-de-course-t08-brouillon4-v1.py`. Cause "
              "unique : le rendu du développeur de la chaîne de lancement, " + RAPPORT + ". « commandes » : ce que ce "
              "rapport donne ou demande ; « arrêts » : sa réserve 9 (messages d'arrêt qui portent un nombre) ; "
              "« renvoi » : renvoi d'un brouillon à l'autre. La consigne du juge de verdict reste au brouillon 3.", ""]
    ecrits = []
    for (entree, s), sortie, ops in PIECES:
        o = (DOSSIER / entree).read_bytes()
        if sha(o) != s:
            print(f"ARRET : {entree} : empreinte différente", file=sys.stderr)
            return 2
        t = o.decode("utf-8")
        lignes += [f"## `{entree}` → `{sortie}`", "", "| n° | cause | ancien (début) | nouveau (début) |", "|---|---|---|---|"]
        for n, (cause, a, b) in enumerate(ops, 1):
            if t.count(a) != 1:
                print(f"ARRET : {entree}, opération {n} ({cause}) : texte ancien trouvé {t.count(a)} fois", file=sys.stderr)
                return 2
            t = t.replace(a, b)
            lignes.append(f"| {n} | {cause} | {debut(a)} | {debut(b)} |")
        ecrits.append((sortie, t))
        lignes += ["", f"Entrée : `{s}`. Sortie : `{sha(t.encode('utf-8'))}`. Opérations : {len(ops)}.", ""]
    for sortie, t in ecrits:
        (DOSSIER / sortie).write_text(t, encoding="utf-8")
    (DOSSIER / JOURNAL).write_text("\n".join(lignes) + "\n", encoding="utf-8")
    for p in sorties:
        print(f"{sha(p.read_bytes())}  {p}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
