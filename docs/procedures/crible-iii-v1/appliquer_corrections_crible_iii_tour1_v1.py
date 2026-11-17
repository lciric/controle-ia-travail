#!/usr/bin/env python3
"""Applique au code de lancement du crible (iii) v1 les corrections du tour 1 de sa contre-lecture
(`contre-lecture-code-crible-iii-tour1-v1.md`, `c0c66dd5…`) : versions v2 neuves, dans le même dossier (R12 ; les v1 restent).

Usage : python3 -I -B appliquer_corrections_crible_iii_tour1_v1.py code [--dossier D]
        python3 -I -B appliquer_corrections_crible_iii_tour1_v1.py pieces HEURE_UTC [--dossier D]
- `code` : écrit les dix fichiers de code v2 (noyau, lanceur, amorce, programme machine et son aide, outil de la session, répétition,
  essais, banc de mutations, essai à blanc), chacun par ses couples « ancien → nouveau » appliqués à sa source v1 ;
- `pieces` : refait en mémoire chaque fichier de code v2 et exige qu'il soit égal, à l'octet, à celui du dossier et à son compagnon
  `.sha256` ; exige les sorties gardées de la v2 égales à leurs compagnons ; puis écrit le rapport v2 et la procédure v2
  (HEURE_UTC : `date -u +%FT%TZ` lu au moment du scellement).
Chaque source doit avoir son empreinte attendue (v1 scellée) ; le rapport du tour 1 doit avoir la sienne ; chaque « ancien » doit
figurer exactement une fois au moment de son couple ; aucune cible n'est écrasée (ouverture exclusive). Bibliothèque standard
seule ; aucun accès réseau ; aucune pièce existante modifiée. Aucun identifiant de modèle (lettres A, B, C).
"""
import hashlib
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
NOM_TOUR1 = "contre-lecture-code-crible-iii-tour1-v1.md"
EMPREINTE_TOUR1 = "c0c66dd585585257bb3fa18c6aff66d298b93d09ccce5536423362e14d5a0f80"

SOURCES = {
    "crible_iii_v1.py": "b163e4c6d8070ec40c544c4519143711fbb8d9ec3d6f9a6a931152b0d265a156",
    "lanceur_crible_iii_v1.py": "20cff93d6e22a0cad695e42d6a90510d0fb54bb148f988ae588ac86bfff549e1",
    "amorce_crible_iii_v1.sh": "7f589103b64ab36813ea8a3e17efded5ca73b7279d987d78a134a3f7f167f730",
    "machine_crible_iii_v1.sh": "cdc2420b879d80e773cb0ae1764f44b3d0b22308cff3a79c7962a8e87c9f2002",
    "machine_crible_iii_v1.py": "5dc046c2940b8feaf1ed8b595918b19a8ad76a657170015df06e27e1a109b669",
    "session_crible_iii_v1.sh": "89ed262b7f490b51f67d7aad72d745f8d096050412c7e010b3e4681e11284a3a",
    "repetition_machine_crible_iii_v1.sh": "a72ca88d28547827d172adf40c39e53aea76405613fe52b5453e160bdb9bf32c",
    "essais_crible_iii_v1.py": "04153eb16fb2fb931dc87d3a8c5bb94dde26ce59c0a9d7c648718af1ca089708",
    "mutations_crible_iii_v1.py": "8c77eae8c3970ccc51d20c0fa41f5e5a6ef45e55cb202ce77d425d88eed0d36a",
    "essai_a_blanc_crible_iii_v1.py": "7878813196515006cf9e4dfd7a4ee23a1879ab1f600588b7378eee4d09d5a9ef",
    "rapport-crible-iii-v1.md": "aac9c95c31999f7368a536bbf5c28da7c3cfe0932d1fb92572b2dc5011692d33",
    "procedure-machine-crible-iii-v1.md": "d753c35a6d1958b8b3a4ea8a5c542de2819c337b087dcbe9dc90eeb1cb50c787",
}

SIX = ('"crible_iii_v1.py", "crible_iii_v2.py", "lanceur_crible_iii_v2.py", "mesure_crible_iii_v1.py",\n'
       '                      "lire_crible_iii_v1.py", "relais_factice_crible_iii_v1.py")')

# --- noyau : M1 (deux couples du rapport, plus le complément : fils d'appel attendus), m3 (quatre couples du rapport) ------------
COUPLES_NOYAU = [
    ("\"\"\"Noyau du crible (iii) de l'organisme d'idéation — v1 (fichier neuf ; pièce qui fera foi :\n",
     "\"\"\"Noyau du crible (iii) de l'organisme d'idéation — v2 (fichier neuf ; suit `crible_iii_v1.py`, gardé tel quel et encore\n"
     "importé par la mesure ; corrections M1 et m3 du tour 1 de la contre-lecture du code, `contre-lecture-code-crible-iii-tour1-v1.md` :\n"
     "une exception du gardien ou d'un monde arrête le crible (code 3) sans perdre d'appel ; un arrêt réel survenu après la ligne du\n"
     "minimum la remplace ; pièce qui fera foi :\n"),
    # M1, couple 1 (rapport du tour 1, recopié)
    ("        if r_appel.get(\"etat\") in (\"complet\", \"tronque\") and bras != \"P1\":\n"
     "            cs, lecture = gardien(r, bras, p, r_appel.get(\"texte\") or \"\")\n",
     "        if r_appel.get(\"etat\") in (\"complet\", \"tronque\") and bras != \"P1\":\n"
     "            try:\n"
     "                cs, lecture = gardien(r, bras, p, r_appel.get(\"texte\") or \"\")\n"
     "            except Exception as e:  # noqa: BLE001 — jamais un repli silencieux : arrêt (code 3), l'appel reste au relevé\n"
     "                c.arreter(\"exception du gardien\", f\"monde {r}, {bras} : {type(e).__name__} : {e}\", 3)\n"
     "                cs, lecture = [], f\"gardien en exception : {type(e).__name__}\"\n"),
    # M1, couple 2 (rapport du tour 1, recopié)
    ("            jouer_monde(r, file)\n",
     "            try:\n"
     "                jouer_monde(r, file)\n"
     "            except Exception as e:  # noqa: BLE001 — jamais un repli silencieux : arrêt (code 3), monde compté incomplet\n"
     "                c.arreter(\"exception d'un monde\", f\"monde {r} : {type(e).__name__} : {e}\", 3)\n"
     "                with c.verrou:\n"
     "                    c.mondes[r] = \"incomplet\"\n"
     "                return\n"),
    # complément du couple 2 de M1 : un monde en exception laisse ses fils d'appel en vol ; ils sont attendus avant le relevé
    ("    appels, cartes, ensembles = [], [], {}\n    verrou_listes = threading.Lock()\n",
     "    appels, cartes, ensembles = [], [], {}\n    verrou_listes = threading.Lock()\n"
     "    fils_d_appel = []   # fils d'appel lancés ; tous attendus avant le relevé (complément de M1, couple 2, tour 1)\n"),
    ("                 threading.Thread(target=lancer, args=(\"H\", texte_g2(s[\"g0\"], s[\"h\"])))]\n",
     "                 threading.Thread(target=lancer, args=(\"H\", texte_g2(s[\"g0\"], s[\"h\"])))]\n"
     "        with verrou_listes:\n"
     "            fils_d_appel.extend(tours)\n"),
    ("                d2 = [threading.Thread(target=lancer, args=(\"D\", td)), threading.Thread(target=lancer, args=(\"B\", tb))]\n",
     "                d2 = [threading.Thread(target=lancer, args=(\"D\", td)), threading.Thread(target=lancer, args=(\"B\", tb))]\n"
     "                with verrou_listes:\n"
     "                    fils_d_appel.extend(d2)\n"),
    ("    for t in fils:\n        t.join()\n    arret = c.arret\n",
     "    for t in fils:\n        t.join()\n"
     "    for t in fils_d_appel:  # un monde en exception laisse ses appels en vol : ils finissent et sont listés avant le relevé\n"
     "        if t.ident is not None:\n"
     "            t.join()\n"
     "    arret = c.arret\n"),
    # m3 (rapport du tour 1, quatre couples recopiés)
    ("            if arret is not None and c.arret is None:\n",
     "            if arret is not None and (c.arret is None or c.arret.get(\"ligne\") == \"minimum\"):\n"),
    ("            if n >= APPELS_MIN_LIMITE and k / n > TAUX_LIMITE_DEBIT and c.arret is None:\n",
     "            if n >= APPELS_MIN_LIMITE and k / n > TAUX_LIMITE_DEBIT and (c.arret is None or c.arret.get(\"ligne\") == \"minimum\"):\n"),
    ("            if c.regle[p] >= c.parts[p] - EPS and c.arret is None:\n",
     "            if c.regle[p] >= c.parts[p] - EPS and (c.arret is None or c.arret.get(\"ligne\") == \"minimum\"):\n"),
    ("        with self.verrou:\n            if self.arret is None:\n                self.arret = {\"ligne\": ligne, \"motif\": motif, \"code\": code}\n",
     "        with self.verrou:\n"
     "            if self.arret is None or (self.arret.get(\"ligne\") == \"minimum\" and ligne != \"minimum\"):\n"
     "                self.arret = {\"ligne\": ligne, \"motif\": motif, \"code\": code}\n"),
]

# --- lanceur : M2 (couple du rapport, recopié) ; noms neufs (noyau v2, six fichiers du crible) ----------------------------------
COUPLES_LANCEUR = [
    ("\"\"\"Lanceur du crible (iii) — v1 (fichier neuf ; dérivé du lanceur v74",
     "\"\"\"Lanceur du crible (iii) — v2 (fichier neuf ; suit `lanceur_crible_iii_v1.py`, gardé tel quel : noyau v2 et correction M2\n"
     "du tour 1 de la contre-lecture du code, un appel de la sonde sous G2 non rendu ou sans carte admise déclenche la règle ; dérivé\n"
     "du lanceur v74"),
    ("« Métrique », « Plan d'analyse », « Liste d'arrêt » ; noyau : `crible_iii_v1.py` (même dossier).",
     "« Métrique », « Plan d'analyse », « Liste d'arrêt » ; noyau : `crible_iii_v2.py` (même dossier ; la mesure importe encore\n"
     "`crible_iii_v1.py`, dont elle ne lit que des parties inchangées en v2)."),
    ("import crible_iii_v1 as N  # noqa: E402\n", "import crible_iii_v2 as N  # noqa: E402\n"),
    ("VERSION = \"lanceur-crible-iii-v1\"\n", "VERSION = \"lanceur-crible-iii-v2\"\n"),
    ("FICHIERS_DU_CRIBLE = (\"crible_iii_v1.py\", \"lanceur_crible_iii_v1.py\", \"mesure_crible_iii_v1.py\", \"lire_crible_iii_v1.py\",\n"
     "                      \"relais_factice_crible_iii_v1.py\")\n",
     "FICHIERS_DU_CRIBLE = (" + SIX + "   # v2 : le noyau v1 reste, importé par la mesure\n"),
    ("                r = un(bras, t2)\n"
     "                if r.get(\"etat\") == \"tronque\":\n"
     "                    regles.append(f\"appel sous G2 tronqué ({bras}) : gabarit réécrit, crible non lancé\")\n",
     "                r = un(bras, t2)\n"
     "                if r.get(\"etat\") == \"tronque\":\n"
     "                    regles.append(f\"appel sous G2 tronqué ({bras}) : gabarit réécrit, crible non lancé\")\n"
     "                elif r.get(\"etat\") != \"complet\":\n"
     "                    regles.append(f\"appel sous G2 non rendu ({bras}, état {r.get('etat')}) : G2 non éprouvé, sonde à refaire, crible non lancé\")\n"
     "                elif appels[-1][\"cartes_admises\"] == 0:\n"
     "                    regles.append(f\"aucune carte admise sous G2 ({bras}) : G2 non éprouvé, sonde à refaire, crible non lancé\")\n"),
    ("    p = argparse.ArgumentParser(prog=\"lanceur_crible_iii_v1.py\")\n",
     "    p = argparse.ArgumentParser(prog=\"lanceur_crible_iii_v2.py\")\n"),
]

# --- programme machine et aide, amorce, outil de la session, répétition : noms neufs seulement --------------------------------------
COUPLES_MACHINE_SH = [
    ("# Programme machine du crible (iii) — v1 (procédure `procedure-machine-crible-iii-v1.md`, même dossier). Dérivé du programme\n",
     "# Programme machine du crible (iii) — v2 (procédure `procedure-machine-crible-iii-v2.md`, même dossier ; suit le programme v1,\n"
     "# gardé tel quel : lanceur v2, aide v2, six fichiers du crible, tour 1 de la contre-lecture du code). Dérivé du programme\n"),
    ("AIDE=\"$T/machine_crible_iii_v1.py\"\n", "AIDE=\"$T/machine_crible_iii_v2.py\"\n"),
    ("O() { env -i PATH=\"$PX\" HOME=/root python3 -I -B \"${ESSAI_LANCEUR:-$C/lanceur_crible_iii_v1.py}\" \"$@\"; }\n",
     "O() { env -i PATH=\"$PX\" HOME=/root python3 -I -B \"${ESSAI_LANCEUR:-$C/lanceur_crible_iii_v2.py}\" \"$@\"; }\n"),
    ("for f in crible_iii_v1.py lanceur_crible_iii_v1.py mesure_crible_iii_v1.py lire_crible_iii_v1.py relais_factice_crible_iii_v1.py; do\n",
     "for f in crible_iii_v1.py crible_iii_v2.py lanceur_crible_iii_v2.py mesure_crible_iii_v1.py lire_crible_iii_v1.py \\\n"
     "    relais_factice_crible_iii_v1.py; do\n"),
    ("RR_ANTHROPIC_API_KEY_RIGAUD=\"$KA\" python3 -I -B \"${ESSAI_LANCEUR:-$C/lanceur_crible_iii_v1.py}\" jouer \\\n",
     "RR_ANTHROPIC_API_KEY_RIGAUD=\"$KA\" python3 -I -B \"${ESSAI_LANCEUR:-$C/lanceur_crible_iii_v2.py}\" jouer \\\n"),
    ("\"${ESSAI_LANCEUR:-$C/lanceur_crible_iii_v1.py}\" jouer --mode a_blanc --arbre \"$ARBRE\" \\\n",
     "\"${ESSAI_LANCEUR:-$C/lanceur_crible_iii_v2.py}\" jouer --mode a_blanc --arbre \"$ARBRE\" \\\n"),
]

COUPLES_MACHINE_PY = [
    ("\"\"\"Aide du programme machine du crible (iii) — v1 (dérivée de",
     "\"\"\"Aide du programme machine du crible (iii) — v2 (suit l'aide v1, gardée telle quelle : six fichiers du crible, tour 1 de la\n"
     "contre-lecture du code ; dérivée de"),
    ("procédure `procedure-machine-crible-iii-v1.md`, 2 sinon", "procédure `procedure-machine-crible-iii-v2.md`, 2 sinon"),
    ("FICHIERS_DU_CRIBLE = (\"crible_iii_v1.py\", \"lanceur_crible_iii_v1.py\", \"mesure_crible_iii_v1.py\", \"lire_crible_iii_v1.py\",\n"
     "                      \"relais_factice_crible_iii_v1.py\")\n",
     "FICHIERS_DU_CRIBLE = (" + SIX + "\n"),
]

COUPLES_AMORCE = [
    ("# Amorce du crible (iii) sur la machine jetable, sans ssh — v1 (procédure `procedure-machine-crible-iii-v1.md`, même dossier).\n",
     "# Amorce du crible (iii) sur la machine jetable, sans ssh — v2 (procédure `procedure-machine-crible-iii-v2.md`, même dossier ;\n"
     "# suit l'amorce v1, gardée telle quelle : programme machine v2 et son aide v2, tour 1 de la contre-lecture du code).\n"),
    ("(ligne imprimée par `session_crible_iii_v1.sh commande`)", "(ligne imprimée par `session_crible_iii_v2.sh commande`)"),
    ("M=\"$T/machine_crible_iii_v1.sh\"; H=\"$T/machine_crible_iii_v1.py\"\n", "M=\"$T/machine_crible_iii_v2.sh\"; H=\"$T/machine_crible_iii_v2.py\"\n"),
    ("git -C \"$D\" show \"$COMMIT_MAIN:$DOSSIER_CODE/machine_crible_iii_v1.sh\" > \"$M.neuf\"",
     "git -C \"$D\" show \"$COMMIT_MAIN:$DOSSIER_CODE/machine_crible_iii_v2.sh\" > \"$M.neuf\""),
    ("git -C \"$D\" show \"$COMMIT_MAIN:$DOSSIER_CODE/machine_crible_iii_v1.py\" > \"$H.neuf\"",
     "git -C \"$D\" show \"$COMMIT_MAIN:$DOSSIER_CODE/machine_crible_iii_v2.py\" > \"$H.neuf\""),
]

COUPLES_SESSION = [
    ("# Outil de la session qui lance le crible (iii) sans ssh — v1 (procédure `procedure-machine-crible-iii-v1.md`, même dossier ; dérivé de\n",
     "# Outil de la session qui lance le crible (iii) sans ssh — v2 (procédure `procedure-machine-crible-iii-v2.md`, même dossier ; suit\n"
     "# l'outil v1, gardé tel quel : amorce v2 et programme machine v2, tour 1 de la contre-lecture du code ; dérivé de\n"),
    ("AMORCE=\"$ICI/amorce_crible_iii_v1.sh\"\n", "AMORCE=\"$ICI/amorce_crible_iii_v2.sh\"\n"),
    ("\"$CM:$DOSSIER_CODE/amorce_crible_iii_v1.sh\" | cmp -s - \"$AMORCE\"", "\"$CM:$DOSSIER_CODE/amorce_crible_iii_v2.sh\" | cmp -s - \"$AMORCE\""),
    ("SH=$(git -C \"$W\" show \"$CM:$DOSSIER_CODE/machine_crible_iii_v1.sh\"", "SH=$(git -C \"$W\" show \"$CM:$DOSSIER_CODE/machine_crible_iii_v2.sh\""),
    ("AH=$(git -C \"$W\" show \"$CM:$DOSSIER_CODE/machine_crible_iii_v1.py\"", "AH=$(git -C \"$W\" show \"$CM:$DOSSIER_CODE/machine_crible_iii_v2.py\""),
    ("gunzip > /root/amorce_crible_iii_v1.sh && bash /root/amorce_crible_iii_v1.sh", "gunzip > /root/amorce_crible_iii_v2.sh && bash /root/amorce_crible_iii_v2.sh"),
]

COUPLES_REPETITION = [
    ("# Répétition locale de la machine du crible (iii) — v1 : l'amorce et le programme machine réels,",
     "# Répétition locale de la machine du crible (iii) — v2 (suit la répétition v1, gardée telle quelle : amorce, programme machine,\n"
     "# aide et outil de la session v2, six fichiers du crible ; tour 1 de la contre-lecture du code) :\n"
     "# l'amorce et le programme machine réels,"),
    ("(`session_crible_iii_v1.sh`) contre le dépôt jouet.", "(`session_crible_iii_v2.sh`) contre le dépôt jouet."),
    ("# Usage : bash repetition_machine_crible_iii_v1.sh PYTHON", "# Usage : bash repetition_machine_crible_iii_v2.sh PYTHON"),
    ("for f in crible_iii_v1.py lanceur_crible_iii_v1.py mesure_crible_iii_v1.py lire_crible_iii_v1.py relais_factice_crible_iii_v1.py \\\n"
     "    machine_crible_iii_v1.sh machine_crible_iii_v1.py amorce_crible_iii_v1.sh; do cp \"$ICI/$f\" \"$DC/\"; done\n",
     "for f in crible_iii_v1.py crible_iii_v2.py lanceur_crible_iii_v2.py mesure_crible_iii_v1.py lire_crible_iii_v1.py \\\n"
     "    relais_factice_crible_iii_v1.py machine_crible_iii_v2.sh machine_crible_iii_v2.py amorce_crible_iii_v2.sh; do cp \"$ICI/$f\" \"$DC/\"; done\n"),
    ("for f in crible_iii_v1.py lanceur_crible_iii_v1.py mesure_crible_iii_v1.py lire_crible_iii_v1.py \\\n"
     "    relais_factice_crible_iii_v1.py; do echo",
     "for f in crible_iii_v1.py crible_iii_v2.py lanceur_crible_iii_v2.py \\\n"
     "    mesure_crible_iii_v1.py lire_crible_iii_v1.py relais_factice_crible_iii_v1.py; do echo"),
    ("SH=$(sha256sum < \"$DC/machine_crible_iii_v1.sh\" | cut -d' ' -f1); AH=$(sha256sum < \"$DC/machine_crible_iii_v1.py\" | cut -d' ' -f1)\n",
     "SH=$(sha256sum < \"$DC/machine_crible_iii_v2.sh\" | cut -d' ' -f1); AH=$(sha256sum < \"$DC/machine_crible_iii_v2.py\" | cut -d' ' -f1)\n"),
    ("bash $ICI/session_crible_iii_v1.sh\"\n", "bash $ICI/session_crible_iii_v2.sh\"\n"),
    ("        bash \"$ICI/amorce_crible_iii_v1.sh\" > \"$1.log\" 2>&1 < /dev/null &\n",
     "        bash \"$ICI/amorce_crible_iii_v2.sh\" > \"$1.log\" 2>&1 < /dev/null &\n"),
    ("COMMIT_LOT=\"$CM\" bash \"$ICI/amorce_crible_iii_v1.sh\" > \"$R/m4.log\" 2>&1; c=$?\n",
     "COMMIT_LOT=\"$CM\" bash \"$ICI/amorce_crible_iii_v2.sh\" > \"$R/m4.log\" 2>&1; c=$?\n"),
    ("= \"$(sha256sum < \"$ICI/amorce_crible_iii_v1.sh\" | cut -d' ' -f1)\" ]; then\n",
     "= \"$(sha256sum < \"$ICI/amorce_crible_iii_v2.sh\" | cut -d' ' -f1)\" ]; then\n"),
]

# --- essais du niveau A : cas neufs de M1 (gardien, monde), de son complément et de m3 ; niveau B de m4 (K1, arbre réel) ----------
ESSAIS_AIDES = r'''

def gardien_qui_leve(cible):
    """Gardien qui lève une exception sur le seul appel `cible` = (monde, bras), le gardien factice ailleurs (tour 1, M1)."""
    def g(r, bras, nom, texte):
        if (r, bras) == cible:
            raise ValueError("gardien en panne (essai)")
        return gardien_factice(r, bras, nom, texte)
    return g


def jouer_t1(N, scripte, gardien=None, traits_faux=None):
    """Comme `jouer`, avec un gardien et des traits d'archive au choix (essais du tour 1)."""
    servis, traits = servis_factices(N)
    traits.update(traits_faux or {})
    return N.jouer_crible(servis, scripte, gardien or gardien_factice, time.time, time.time() + 10 ** 6, {N.PR4: 3.0, N.PR2: 2.0},
                          N.PARTS_USD, BORNES_RAPIDES, "a_blanc", RACINE_ESSAI, traits)


def tous_listes(rel):
    """Chaque appel fait (réservé puis appelé) est au relevé : aucun n'est perdu."""
    return sum(rel["appels_faits"].values()) == sum(1 for a in rel["appels"] if a.get("appele"))


class EnVol:
    """Appeler scripté dont l'appel `cible`, encore en vol quand la ligne du minimum se déclenche, rend une `Arret` après 0,3 s."""

    def __init__(self, N, base, cible):
        self.N, self.base, self.cible = N, base, cible

    def __call__(self, bras, nom, texte, r, delai):
        if (r, bras) == self.cible:
            time.sleep(0.3)
            raise self.N.Arret("réponse brute ou témoin d'isolement absent", "témoin supprimé après la ligne du minimum (essai)")
        return self.base(bras, nom, texte, r, delai)
'''

ESSAIS_CAS = r'''    # tour 1 de la contre-lecture du code : M1 (exception du gardien, exception d'un monde, appels en vol), m3 (après le minimum)
    rel_ok = jouer_t1(N, Scripte(N))
    rel = jouer_t1(N, Scripte(N), gardien=gardien_qui_leve((3, "H")))
    h3 = [x for x in rel["appels"] if x["monde"] == 3 and x["bras"] == "H"]
    note("liste d'arrêt : exception du gardien (arrêt, code 3 ; l'appel reste au relevé, sa dépense comptée)",
         rel_ok["arret"] is None and rel_ok["complets"] == 20 and tous_listes(rel_ok),
         rel["arret"] is not None and rel["arret"]["ligne"] == "exception du gardien" and rel["arret"]["code"] == 3
         and len(h3) == 1 and h3[0]["appele"] and float(h3[0].get("cout_usd") or 0) > 0 and tous_listes(rel),
         f"{rel['arret']} ; {sum(rel['appels_faits'].values())} appels faits, {sum(1 for x in rel['appels'] if x.get('appele'))} listés")
    rel = jouer_t1(N, Scripte(N, {(3, "S"): "lent-0.3"}), traits_faux={3: [["x"]]})
    s3 = [x for x in rel["appels"] if x["monde"] == 3 and x["bras"] == "S"]
    note("liste d'arrêt : exception dans un monde (filtre qui lève : arrêt, code 3 ; aucune file muette ; appel en vol listé)",
         rel_ok["arret"] is None and all(v == "complet" for v in rel_ok["mondes"].values()),
         rel["arret"] is not None and rel["arret"]["ligne"] == "exception d'un monde" and rel["arret"]["code"] == 3
         and rel["mondes"]["3"] == "incomplet" and all(v != "en cours" for v in rel["mondes"].values())
         and len(s3) == 1 and s3[0]["appele"] and tous_listes(rel),
         f"{rel['arret']} ; appel S du monde 3 {'listé' if s3 else 'absent du relevé'}")
    panne = {(r, "P1"): "panne" for r in (1, 2, 3, 4, 6)}
    rel_s = jouer_t1(N, Scripte(N, {**panne, (5, "S"): "lent-0.3"}))
    rel_a = jouer_t1(N, EnVol(N, Scripte(N, panne), (5, "S")))
    rel_g = jouer_t1(N, Scripte(N, {**panne, (5, "S"): "lent-0.3"}), gardien=gardien_qui_leve((5, "S")))
    note("liste d'arrêt : arrêt réel d'un appel en vol après la ligne du minimum (il la remplace : code 3)",
         rel_s["arret"] is not None and rel_s["arret"]["ligne"] == "minimum" and rel_s["arret"]["code"] == 0,
         rel_a["arret"] is not None and rel_a["arret"]["ligne"] == "réponse brute ou témoin d'isolement absent"
         and rel_a["arret"]["code"] == 3 and rel_g["arret"] is not None and rel_g["arret"]["ligne"] == "exception du gardien"
         and rel_g["arret"]["code"] == 3,
         f"sain : {rel_s['arret']} ; témoin : {rel_a['arret']} ; gardien : {rel_g['arret']}")
'''

ESSAIS_ARBRE = r'''

def controle_k1(pm, porte_k1):
    """Composantes comptées d'un monde préparé par la mesure (définition de la pièce) : ni l'effet de K1, ni ce que K1 servie porte
    à elle seule, et toutes certifiées. Rend la liste des écarts (vide si conforme)."""
    comptees, certifiees = set(pm["comptees"]), set(pm["certifiees"])
    ecarts = []
    if pm["eid_k1"] in comptees:
        ecarts.append("effet de K1 compté")
    if comptees & set(porte_k1):
        ecarts.append("composante portée par K1 comptée")
    if not comptees <= certifiees:
        ecarts.append("composante non certifiée comptée")
    return ecarts


def essais_arbre_k1(ME, arbre, mondes):
    """Niveau B (tour 1, m4) : la préparation réelle des mondes (`OutilsMR2.preparer`, arbre réel, mondes de développement) retire
    des composantes comptées l'effet de K1 et ce que K1 porte ; sain sur chaque monde distinct, artefact sur un monde préparé puis
    faussé (effet de K1 remis). Aucun coefficient imprimé : écarts et drapeaux seulement."""
    R = []
    outils = ME.OutilsMR2(arbre)
    distincts, vus = [], set()
    for w in mondes:
        if w["spec_sha256"] not in vus:
            vus.add(w["spec_sha256"])
            distincts.append(w)
    outils.precalculer_c8(distincts)
    ecarts, drapeaux, pm, porte = {}, {}, None, []
    for w in distincts:
        pm = outils.preparer(w)
        porte = sorted(outils.porte(pm, pm["k1"])[0])
        ecarts[w["monde"]] = controle_k1(pm, porte)
        drapeaux[w["monde"]] = {"k1_certifie": pm["eid_k1"] in pm["certifiees"],
                                "porte_par_k1_certifie": bool(set(porte) & set(pm["certifiees"]))}
    faux = dict(pm, comptees=sorted(set(pm["comptees"]) | {pm["eid_k1"]})) if pm is not None else None
    R.append({"essai": "mesure, arbre réel : composantes comptées hors de l'effet de K1 et de ce que K1 porte, toutes certifiées",
              "sain": bool(distincts) and all(not e for e in ecarts.values()),
              "artefact": faux is not None and bool(controle_k1(faux, porte)),
              "detail": json.dumps({"mondes_distincts": len(distincts), "ecarts": ecarts, "drapeaux": drapeaux}, ensure_ascii=False,
                                   sort_keys=True)})
    return R


def main_arbre(ME, argv):
    """Niveau B seul : `--arbre ORCHESTRATEUR --mondes MONDES.json --mondes-sha256 H` (mondes de développement à graine publique)."""
    import argparse
    import hashlib
    p = argparse.ArgumentParser(prog="essais_crible_iii_v2.py")
    for o in ("--arbre", "--mondes", "--mondes-sha256"):
        p.add_argument(o, required=True)
    a = p.parse_args(argv)
    with open(a.mondes, "rb") as f:
        b = f.read()
    if hashlib.sha256(b).hexdigest() != a.mondes_sha256:
        print("ESSAI ÉCHEC | niveau B | fichier des mondes : empreinte différente")
        return 1
    try:
        R = essais_arbre_k1(ME, a.arbre, json.loads(b)["mondes"])
    except Exception as e:  # noqa: BLE001 — une exception des essais est un échec, jamais un succès
        print(f"ESSAI ÉCHEC | exception des essais (niveau B) | {type(e).__name__} : {e}")
        return 1
    return imprimer(R)'''

COUPLES_ESSAIS = [
    ("\"\"\"Essais du crible (iii) — v1 : cas sain et artefact",
     "\"\"\"Essais du crible (iii) — v2 (suit les essais v1, gardés tels quels : noyau v2 ; cas du tour 1 de la contre-lecture du code :\n"
     "exception du gardien, exception d'un monde, arrêt réel après la ligne du minimum ; niveau B : préparation réelle des mondes et\n"
     "effet de K1) : cas sain et artefact"),
    ("Niveau B (`essais_arbre`, joué par `essai_a_blanc_crible_iii_v1.py`) : chaîne du pilote (commande,\n"
     "relais factice, gardien) sur des mondes de développement à graine publique.\n",
     "Niveau B (`essai_a_blanc_crible_iii_v2.py`) : chaîne du pilote (commande,\n"
     "relais factice, gardien) sur des mondes de développement à graine publique ; son cas `essais_arbre_k1` (préparation réelle\n"
     "des mondes) est dans ce fichier, joué aussi par le banc de mutations.\n"),
    ("Usage : python3 -I -B essais_crible_iii_v1.py            (niveau A ; code 0 si tous les essais passent)\n"
     "Le banc de mutations (`mutations_crible_iii_v1.py`) rejoue `essais_noyau` sur des copies mutées des modules.\n",
     "Usage : python3 -I -B essais_crible_iii_v2.py            (niveau A ; code 0 si tous les essais passent)\n"
     "        python3 -I -B essais_crible_iii_v2.py --arbre ORCHESTRATEUR --mondes MONDES.json --mondes-sha256 H   (niveau B, K1)\n"
     "Le banc de mutations (`mutations_crible_iii_v2.py`) rejoue ces essais sur des copies mutées des modules.\n"),
    ("\"a_blanc\", RACINE_ESSAI, traits)\n\n\ndef refuse(f, *a, exc=Exception):\n",
     "\"a_blanc\", RACINE_ESSAI, traits)\n" + ESSAIS_AIDES + "\n\ndef refuse(f, *a, exc=Exception):\n"),
    ("    # mesure, sur des mondes synthétiques (outils factices)\n    R += essais_mesure(N, ME)\n",
     ESSAIS_CAS + "    # mesure, sur des mondes synthétiques (outils factices)\n    R += essais_mesure(N, ME)\n"),
    ("    return 0 if not ko else 1\n\n\ndef main():\n    import crible_iii_v1 as N\n    import lire_crible_iii_v1 as L\n"
     "    import mesure_crible_iii_v1 as ME\n    try:\n",
     "    return 0 if not ko else 1\n" + ESSAIS_ARBRE + "\n\n\ndef main(argv=None):\n    argv = sys.argv[1:] if argv is None else argv\n"
     "    import crible_iii_v2 as N\n    import lire_crible_iii_v1 as L\n    import mesure_crible_iii_v1 as ME\n"
     "    if argv:\n        return main_arbre(ME, argv)\n    try:\n"),
]

# --- banc de mutations : noyau v2 ; mutations neuves de M1, du complément et de m3 ; niveau B (m4) ----------------------------------
NOMS_DU_NOYAU = [
    "le filtre lit le monde ou l'oracle (garde des entrées retirée)", "égalités rompues par l'ordre du proposeur",
    "égalités rompues au hasard", "ensemble de l'archive gardé", "distance de Jaccard minimax au lieu de maximin",
    "H tiré d'une graine qui ne dépend pas de la racine (hasard du système)", "H tiré du secret (garde de la graine retirée)",
    "B servi d'autres ensembles que D", "garde du texte de B retirée", "réponse brute de la passe 1 servie à la passe 2",
    "garde du texte de passe 2 retirée", "D et B lancés après une passe 1 tronquée", "plus de vingt ensembles gardés",
    "borne de 53 000 octets relâchée", "garde de départ retirée", "minuterie au départ d'un monde retirée", "borne par appel ignorée",
    "ligne du minimum retirée", "limite de débit à 50 % au lieu de 5 %", "part d'un relais non gardée", "témoin absent sans arrêt",
    "affectation des mondes aux files décalée", "bornes réduites admises en mode réel", "ligne de GO sans l'enveloppe GO-2026-11-15-06",
]

MUTATIONS_NEUVES = r'''    # tour 1 de la contre-lecture du code (M1, complément du couple 2 de M1, m3)
    ("exception du gardien avalée (try du gardien retiré)", "crible_iii_v2.py",
     "            try:\n                cs, lecture = gardien(r, bras, p, r_appel.get(\"texte\") or \"\")\n"
     "            except Exception as e:  # noqa: BLE001 — jamais un repli silencieux : arrêt (code 3), l'appel reste au relevé\n"
     "                c.arreter(\"exception du gardien\", f\"monde {r}, {bras} : {type(e).__name__} : {e}\", 3)\n"
     "                cs, lecture = [], f\"gardien en exception : {type(e).__name__}\"\n",
     "            cs, lecture = gardien(r, bras, p, r_appel.get(\"texte\") or \"\")\n", "exception du gardien"),
    ("exception d'un monde avalée (try du monde retiré)", "crible_iii_v2.py",
     "            try:\n                jouer_monde(r, file)\n"
     "            except Exception as e:  # noqa: BLE001 — jamais un repli silencieux : arrêt (code 3), monde compté incomplet\n"
     "                c.arreter(\"exception d'un monde\", f\"monde {r} : {type(e).__name__} : {e}\", 3)\n"
     "                with c.verrou:\n                    c.mondes[r] = \"incomplet\"\n                return\n",
     "            jouer_monde(r, file)\n", "exception dans un monde"),
    ("appels en vol d'un monde en exception non attendus (complément retiré)", "crible_iii_v2.py",
     "    for t in fils_d_appel:  # un monde en exception laisse ses appels en vol : ils finissent et sont listés avant le relevé\n"
     "        if t.ident is not None:\n            t.join()\n", "", "exception dans un monde"),
    ("arrêt réel d'un appel après la ligne du minimum perdu", "crible_iii_v2.py",
     "            if arret is not None and (c.arret is None or c.arret.get(\"ligne\") == \"minimum\"):\n",
     "            if arret is not None and c.arret is None:\n", "après la ligne du minimum"),
    ("arrêt nommé après la ligne du minimum perdu (Commun.arreter)", "crible_iii_v2.py",
     "            if self.arret is None or (self.arret.get(\"ligne\") == \"minimum\" and ligne != \"minimum\"):\n",
     "            if self.arret is None:\n", "après la ligne du minimum"),
]

# mutations de niveau B (tour 1, m4) : jouées sur l'arbre réel et les mondes de développement (--arbre, --mondes, --mondes-sha256)
MUTATIONS_ARBRE = [
    ("effet de K1 compté à la préparation réelle des mondes (« - {eid_k1} - k1_tau » retiré)", "mesure_crible_iii_v1.py",
     "comptees=sorted(certifiees - {eid_k1} - k1_tau)", "comptees=sorted(certifiees)", "hors de l'effet de K1"),
]
'''

MUTATIONS_MAIN_V1 = r'''def jouer_essais(dossier):
    r = subprocess.run([sys.executable, "-I", "-B", os.path.join(dossier, "essais_crible_iii_v1.py")], capture_output=True,
                       text=True, encoding="utf-8", timeout=600)
    echecs = [l for l in r.stdout.splitlines() if l.startswith("ESSAI ÉCHEC")]
    return r.returncode, echecs, r.stdout + r.stderr[-2000:]


def main():
    lignes, defauts = [], 0
    with tempfile.TemporaryDirectory() as d:
        for m in MODULES:
            shutil.copy2(os.path.join(ICI, m), os.path.join(d, m))
        code, echecs, _ = jouer_essais(d)
        lignes.append(f"ORIGINAL : code {code}, {len(echecs)} échec(s)")
        if code != 0 or echecs:
            defauts += 1
        for nom, fichier, ancien, nouveau, attendu in MUTATIONS:
            with tempfile.TemporaryDirectory() as dm:
                for m in MODULES:
                    shutil.copy2(os.path.join(ICI, m), os.path.join(dm, m))
                with open(os.path.join(dm, fichier), encoding="utf-8") as f:
                    t = f.read()
                if t.count(ancien) != 1:
                    lignes.append(f"MUTATION NON APPLICABLE | {nom} | « ancien » trouvé {t.count(ancien)} fois")
                    defauts += 1
                    continue
                with open(os.path.join(dm, fichier), "w", encoding="utf-8") as f:
                    f.write(t.replace(ancien, nouveau))
                code, echecs, sortie = jouer_essais(dm)
                tuee = code != 0 and (any(attendu in e for e in echecs) or (not echecs and "Traceback" in sortie and False))
                raison = "; ".join(e.split(" | ")[1] for e in echecs[:3]) if echecs else (sortie.strip().splitlines() or [""])[-1][:160]
                lignes.append(f"MUTATION {'TUÉE' if tuee else 'SURVIVANTE'} | {nom} | {fichier} | code {code} | attendu « {attendu} » "
                              f"| échecs : {raison}")
                defauts += 0 if tuee else 1
    for l in lignes:
        print(l)
    print(f"MUTATIONS : {len(MUTATIONS)}, tuées pour la raison attendue {sum(1 for l in lignes if l.startswith('MUTATION TUÉE'))}, "
          f"défauts {defauts}")
    return 0 if defauts == 0 else 1
'''

MUTATIONS_MAIN = r'''def jouer_essais(dossier, args=()):
    r = subprocess.run([sys.executable, "-I", "-B", os.path.join(dossier, "essais_crible_iii_v2.py"), *args], capture_output=True,
                       text=True, encoding="utf-8", timeout=600 if not args else 7200)
    echecs = [l for l in r.stdout.splitlines() if l.startswith("ESSAI ÉCHEC")]
    return r.returncode, echecs, r.stdout + r.stderr[-2000:]


def jouer_mutations(liste, args, lignes, niveau):
    """Chaque mutation sur une copie neuve des modules ; rend le nombre de défauts (survivante, tuée par une autre cause, ou non
    applicable)."""
    defauts = 0
    for nom, fichier, ancien, nouveau, attendu in liste:
        with tempfile.TemporaryDirectory() as dm:
            for m in MODULES:
                shutil.copy2(os.path.join(ICI, m), os.path.join(dm, m))
            with open(os.path.join(dm, fichier), encoding="utf-8") as f:
                t = f.read()
            if t.count(ancien) != 1:
                lignes.append(f"MUTATION NON APPLICABLE | {nom} | « ancien » trouvé {t.count(ancien)} fois")
                defauts += 1
                continue
            with open(os.path.join(dm, fichier), "w", encoding="utf-8") as f:
                f.write(t.replace(ancien, nouveau))
            code, echecs, sortie = jouer_essais(dm, args)
            tuee = code != 0 and (any(attendu in e for e in echecs) or (not echecs and "Traceback" in sortie and False))
            raison = "; ".join(e.split(" | ")[1] for e in echecs[:3]) if echecs else (sortie.strip().splitlines() or [""])[-1][:160]
            lignes.append(f"MUTATION {'TUÉE' if tuee else 'SURVIVANTE'} | {nom} | {fichier} | niveau {niveau} | code {code} | "
                          f"attendu « {attendu} » | échecs : {raison}")
            defauts += 0 if tuee else 1
    return defauts


def main(argv=None):
    import argparse
    p = argparse.ArgumentParser(prog="mutations_crible_iii_v2.py")
    for o in ("--arbre", "--mondes", "--mondes-sha256"):
        p.add_argument(o)
    a = p.parse_args(sys.argv[1:] if argv is None else argv)
    arbre = (["--arbre", a.arbre, "--mondes", a.mondes, "--mondes-sha256", a.mondes_sha256]
             if a.arbre and a.mondes and a.mondes_sha256 else None)
    lignes, defauts = [], 0
    with tempfile.TemporaryDirectory() as d:
        for m in MODULES:
            shutil.copy2(os.path.join(ICI, m), os.path.join(d, m))
        code, echecs, _ = jouer_essais(d)
        lignes.append(f"ORIGINAL (niveau A) : code {code}, {len(echecs)} échec(s)")
        if code != 0 or echecs:
            defauts += 1
        if arbre is not None:
            code, echecs, _ = jouer_essais(d, arbre)
            lignes.append(f"ORIGINAL (niveau B) : code {code}, {len(echecs)} échec(s)")
            if code != 0 or echecs:
                defauts += 1
    defauts += jouer_mutations(MUTATIONS, (), lignes, "A")
    if arbre is None:
        lignes.append(f"NIVEAU B NON JOUÉ | {len(MUTATIONS_ARBRE)} mutation(s) : --arbre, --mondes et --mondes-sha256 exigés")
        defauts += len(MUTATIONS_ARBRE)
    else:
        defauts += jouer_mutations(MUTATIONS_ARBRE, arbre, lignes, "B")
    for l in lignes:
        print(l)
    n = len(MUTATIONS) + len(MUTATIONS_ARBRE)
    print(f"MUTATIONS : {n} ({len(MUTATIONS)} au niveau A, {len(MUTATIONS_ARBRE)} au niveau B), tuées pour la raison attendue "
          f"{sum(1 for l in lignes if l.startswith('MUTATION TUÉE'))}, défauts {defauts}")
    return 0 if defauts == 0 else 1
'''

COUPLES_MUTATIONS = [
    ("\"\"\"Banc de mutations du crible (iii) — v1 (pièce qui fera foi, section « Étapes », point 0 : « toutes tuées pour la raison attendue »).\n",
     "\"\"\"Banc de mutations du crible (iii) — v2 (pièce qui fera foi, section « Étapes », point 0 : « toutes tuées pour la raison attendue ») ;\n"
     "suit le banc v1, gardé tel quel : noyau v2, mutations neuves du tour 1 de la contre-lecture du code (M1, son complément, m3) et\n"
     "une mutation de niveau B (m4 : préparation réelle des mondes, arbre réel et mondes de développement).\n"),
    ("une seule fois) ; les essais du niveau A (`essais_crible_iii_v1.py`) sont rejoués sur la copie, dans un processus neuf\n",
     "une seule fois) ; les essais (`essais_crible_iii_v2.py` : niveau A, ou niveau B avec l'arbre) sont rejoués sur la copie, dans un processus neuf\n"),
    ("Usage : python3 -I -B mutations_crible_iii_v1.py      (code 0 si toutes les mutations sont tuées pour la raison attendue)\n",
     "Usage : python3 -I -B mutations_crible_iii_v2.py --arbre ORCHESTRATEUR --mondes MONDES.json --mondes-sha256 H\n"
     "        (code 0 si toutes les mutations sont tuées pour la raison attendue ; sans l'arbre, le niveau B compte en défaut)\n"
     "Une mutation que les essais « tuent » par une exception, et non par l'échec de l'essai attendu, compte comme survivante.\n"),
    ("MODULES = (\"crible_iii_v1.py\", \"mesure_crible_iii_v1.py\", \"lire_crible_iii_v1.py\", \"essais_crible_iii_v1.py\")\n",
     "MODULES = (\"crible_iii_v1.py\", \"crible_iii_v2.py\", \"mesure_crible_iii_v1.py\", \"lire_crible_iii_v1.py\", \"essais_crible_iii_v2.py\")\n"
     "# crible_iii_v1.py : copié sans mutation (la mesure l'importe) ; le noyau muté est crible_iii_v2.py\n"),
] + [(f"    (\"{nom}\", \"crible_iii_v1.py\",", f"    (\"{nom}\", \"crible_iii_v2.py\",") for nom in NOMS_DU_NOYAU] + [
    ("     \"    if arret is not None and arret.get(\\\"ligne\\\") != \\\"minimum\\\":\", \"    if False:\", \"étage 0\"),\n]\n",
     "     \"    if arret is not None and arret.get(\\\"ligne\\\") != \\\"minimum\\\":\", \"    if False:\", \"étage 0\"),\n"
     + MUTATIONS_NEUVES),
    (MUTATIONS_MAIN_V1, MUTATIONS_MAIN),
]

# --- essai à blanc : noyau et lanceur v2 ; cas neufs de M2 (sonde : D en panne, B illisible) et de m4 (K1, arbre réel) ------------
ESSAI_BLANC_CAS = r'''    # tour 1 de la contre-lecture du code, M2 : un appel sous G2 non rendu, ou sans carte admise, déclenche la règle (G2 non éprouvé)
    code, rs = sonde("sonde-d-en-panne", {"*|D": "panne"})
    rd = rs.get("regles_d_avance") or {}
    cas("sonde des gabarits : un appel sous G2 non rendu (D en panne) déclenche la règle « G2 non éprouvé » (tour 1, M2)",
        code == 0 and rd.get("declenchee") is True and any("non rendu (D" in m and "G2 non éprouvé" in m for m in rd.get("motifs", [])),
        {"code": code, "regles": rd, "appels": [(x.get("bras"), x.get("etat"), x.get("cartes_admises")) for x in rs.get("appels", [])]})
    code, rs = sonde("sonde-b-illisible", {"*|B": "illisible"})
    rd = rs.get("regles_d_avance") or {}
    cas("sonde des gabarits : aucune carte admise sous G2 (B illisible) déclenche la règle « G2 non éprouvé » (tour 1, M2)",
        code == 0 and rd.get("declenchee") is True and any("aucune carte admise sous G2 (B)" in m for m in rd.get("motifs", [])),
        {"code": code, "regles": rd, "appels": [(x.get("bras"), x.get("etat"), x.get("cartes_admises")) for x in rs.get("appels", [])]})
    # tour 1, m4 : préparation réelle des mondes (arbre réel) : l'effet de K1 et ce que K1 porte hors des composantes comptées
    with open(a.mondes, encoding="utf-8") as f:
        rk = ES.essais_arbre_k1(ME, a.arbre, json.load(f)["mondes"])[0]
    cas("mesure, arbre réel : composantes comptées hors de l'effet de K1 et de ce que K1 porte, toutes certifiées (tour 1, m4)",
        rk["sain"] and rk["artefact"], json.loads(rk["detail"]))
'''

COUPLES_ESSAI_BLANC = [
    ("\"\"\"Essai à blanc complet du crible (iii) — v1 (niveau B des essais) :",
     "\"\"\"Essai à blanc complet du crible (iii) — v2 (niveau B des essais ; suit l'essai v1, gardé tel quel : noyau et lanceur v2 ; cas\n"
     "neufs du tour 1 de la contre-lecture du code : sonde des gabarits avec D en panne et avec B illisible, préparation réelle des\n"
     "mondes et effet de K1) :"),
    ("Usage : python3 -I -B essai_a_blanc_crible_iii_v1.py --arbre", "Usage : python3 -I -B essai_a_blanc_crible_iii_v2.py --arbre"),
    ("import crible_iii_v1 as N  # noqa: E402\nimport lanceur_crible_iii_v1 as LA  # noqa: E402\n",
     "import crible_iii_v2 as N  # noqa: E402\nimport lanceur_crible_iii_v2 as LA  # noqa: E402\n"
     "import essais_crible_iii_v2 as ES  # noqa: E402\nimport mesure_crible_iii_v1 as ME  # noqa: E402\n"),
    ("len(rs[\"appels\"]) == 1, {\"regles\": rs.get(\"regles_d_avance\")})\n",
     "len(rs[\"appels\"]) == 1, {\"regles\": rs.get(\"regles_d_avance\")})\n" + ESSAI_BLANC_CAS),
    ("import crible_iii_v1 as N, lanceur_crible_iii_v1 as LA\n", "import crible_iii_v2 as N, lanceur_crible_iii_v2 as LA\n"),
]

CODE = [
    ("crible_iii_v1.py", "crible_iii_v2.py", COUPLES_NOYAU),
    ("lanceur_crible_iii_v1.py", "lanceur_crible_iii_v2.py", COUPLES_LANCEUR),
    ("amorce_crible_iii_v1.sh", "amorce_crible_iii_v2.sh", COUPLES_AMORCE),
    ("machine_crible_iii_v1.sh", "machine_crible_iii_v2.sh", COUPLES_MACHINE_SH),
    ("machine_crible_iii_v1.py", "machine_crible_iii_v2.py", COUPLES_MACHINE_PY),
    ("session_crible_iii_v1.sh", "session_crible_iii_v2.sh", COUPLES_SESSION),
    ("repetition_machine_crible_iii_v1.sh", "repetition_machine_crible_iii_v2.sh", COUPLES_REPETITION),
    ("essais_crible_iii_v1.py", "essais_crible_iii_v2.py", COUPLES_ESSAIS),
    ("mutations_crible_iii_v1.py", "mutations_crible_iii_v2.py", COUPLES_MUTATIONS),
    ("essai_a_blanc_crible_iii_v1.py", "essai_a_blanc_crible_iii_v2.py", COUPLES_ESSAI_BLANC),
]


class Refus(Exception):
    pass


def sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def lire_source(dossier, nom):
    c = os.path.join(dossier, nom)
    if sha(c) != SOURCES[nom]:
        raise Refus(f"{nom} : empreinte différente de la v1 scellée")
    with open(c, encoding="utf-8") as f:
        return f.read()


def appliquer(texte, couples, quoi):
    for i, (ancien, nouveau) in enumerate(couples, 1):
        n = texte.count(ancien)
        if n != 1:
            raise Refus(f"{quoi}, couple {i} : « ancien » trouvé {n} fois ({ancien[:70]!r})")
        texte = texte.replace(ancien, nouveau)
    return texte


def ecrire_neuf(chemin, texte):
    with open(chemin, "x", encoding="utf-8") as f:   # R12 : jamais écrasé
        f.write(texte)


def exiger_tour1(dossier):
    if sha(os.path.join(dossier, NOM_TOUR1)) != EMPREINTE_TOUR1:
        raise Refus("rapport du tour 1 : empreinte différente")


def faire_code(dossier):
    textes = {cible: appliquer(lire_source(dossier, source), couples, cible) for source, cible, couples in CODE}
    return textes


def c_code(dossier):
    exiger_tour1(dossier)
    textes = faire_code(dossier)
    deja = [c for c in textes if os.path.exists(os.path.join(dossier, c))]
    if deja:
        raise Refus(f"cibles déjà présentes (jamais écrasées) : {deja}")
    for cible, t in textes.items():
        ecrire_neuf(os.path.join(dossier, cible), t)
        print(f"écrit {cible} : {hashlib.sha256(t.encode('utf-8')).hexdigest()}")
    return 0


def main(argv):
    dossier = ICI
    if "--dossier" in argv:
        i = argv.index("--dossier")
        dossier, argv = os.path.abspath(argv[i + 1]), argv[:i] + argv[i + 2:]
    try:
        if argv[:1] == ["code"] and len(argv) == 1:
            return c_code(dossier)
        if argv[:1] == ["pieces"] and len(argv) == 2:
            return c_pieces(dossier, argv[1])
        raise Refus("usage : code | pieces HEURE_UTC [--dossier D]")
    except Refus as e:
        print(f"REFUS : {e}")
        return 2


# --- pièces : rapport v2 et procédure v2 --------------------------------------------------------------------------------------------
NOM_PROGRAMME = "appliquer_corrections_crible_iii_tour1_v1.py"

# (pièce, rôle) de la table v2 ; l'empreinte est lue sur le disque et exigée égale au compagnon (sauf ce programme, scellé après)
TABLE_V2 = [
    ("crible_iii_v2.py", "noyau v2 : analyseur, filtre, tirage de H, gabarits G1 et G2, files, bornes, gardes, lignes de GO ; M1 et "
                         "m3 du tour 1 (exceptions du gardien et d'un monde arrêtées, appels en vol attendus, arrêt réel après le minimum)"),
    ("crible_iii_v1.py", "noyau v1, gardé : importé par la mesure seule (constantes, `racine_graines`, `traits_employes`, inchangés "
                         "en v2) ; son ordonnanceur n'est plus joué"),
    ("lanceur_crible_iii_v2.py", "lanceur v2 : secret, mondes, préparation, crible (à blanc, réel), sonde des gabarits (M2 : appel "
                                 "sous G2 non rendu ou sans carte admise), rapatriement, empreintes"),
    ("mesure_crible_iii_v1.py", "mesure gelée (nom réservé par la pièce), une seule fois ; inchangée"),
    ("lire_crible_iii_v1.py", "lecture gelée (nom réservé par la pièce), étages 0 à 7 ; inchangée"),
    ("relais_factice_crible_iii_v1.py", "relais factice (relais du pilote, amont scripté) : essais à blanc seulement ; inchangé"),
    ("amorce_crible_iii_v2.sh", "amorce de la machine v2 (prend le programme machine v2 et son aide)"),
    ("machine_crible_iii_v2.sh", "programme machine v2 (lanceur v2, six fichiers du crible)"),
    ("machine_crible_iii_v2.py", "aide du programme machine v2 (six fichiers du crible à l'addendum)"),
    ("session_crible_iii_v2.sh", "outil de la session v2 (amorce et programme machine v2)"),
    ("garde_session_crible_iii_v1.py", "gardes de la session ; inchangées (le lecteur des lignes de GO qu'elles prennent au noyau v1 "
                                       "est inchangé en v2)"),
    ("essais_crible_iii_v2.py", "essais R5 du niveau A (@@ESSAIS_N@@ cas) et cas `essais_arbre_k1` du niveau B (m4)"),
    ("mutations_crible_iii_v2.py", "banc de mutations v2 (@@MUT_A@@ au niveau A, @@MUT_B@@ au niveau B)"),
    ("essai_a_blanc_crible_iii_v2.py", "essai à blanc complet v2, chaîne réelle, relais factices (niveau B)"),
    ("repetition_machine_crible_iii_v2.sh", "répétition locale de la machine v2 (dépôt jouet, doublures)"),
    ("doublures_repetition_crible_iii_v1.py", "doublures de la répétition ; inchangées"),
    ("sortie-essais-crible-iii-v2.txt", "sortie gardée des essais v2"),
    ("sortie-mutations-crible-iii-v2.txt", "sortie gardée du banc de mutations v2"),
    ("sortie-essai-a-blanc-crible-iii-v2.txt", "sortie gardée de l'essai à blanc complet v2"),
    ("sortie-repetition-machine-crible-iii-v2.txt", "sortie gardée de la répétition de la machine v2"),
    ("devis-machine-crible-iii-v1.md", "devis de la machine (κiii2) ; inchangé"),
    (NOM_PROGRAMME, "programme de couples du tour 1 (code v2, puis ce rapport et la procédure v2)"),
    (NOM_TOUR1, "rapport du tour 1 de la contre-lecture du code"),
]

SORTIES = {
    "essais": ("sortie-essais-crible-iii-v2.txt", r"^ESSAIS : (\d+) cas, (\d+) passés, (\d+) échecs$"),
    "mutations": ("sortie-mutations-crible-iii-v2.txt",
                  r"^MUTATIONS : (\d+) \((\d+) au niveau A, (\d+) au niveau B\), tuées pour la raison attendue (\d+), défauts (\d+)$"),
    "blanc": ("sortie-essai-a-blanc-crible-iii-v2.txt", r"^ESSAI A BLANC : (\d+) cas, (\d+) conformes, (\d+) écarts ; durée (\d+) s$"),
    "repetition": ("sortie-repetition-machine-crible-iii-v2.txt", r"^RÉPÉTITION : (\d+) cas, (\d+) conformes, (\d+) écarts ; "),
}


def compagnon_egal(dossier, nom):
    c = os.path.join(dossier, nom + ".sha256")
    if not os.path.isfile(c):
        raise Refus(f"{nom} : compagnon absent (sceller d'abord)")
    with open(c, encoding="utf-8") as f:
        attendu = f.read().split()[0]
    h = sha(os.path.join(dossier, nom))
    if h != attendu:
        raise Refus(f"{nom} : différent de son compagnon")
    return h


def lire_sorties(dossier):
    """Comptes des jeux de la v2, lus dans leurs sorties gardées (scellées) ; tout écart, ou un code autre que 0, refuse."""
    out = {}
    for cle, (nom, motif) in SORTIES.items():
        compagnon_egal(dossier, nom)
        with open(os.path.join(dossier, nom), encoding="utf-8") as f:
            lignes = f.read().splitlines()
        if not lignes or not lignes[0].startswith("# date -u : ") or lignes[-1] != "code 0":
            raise Refus(f"{nom} : en-tête « # date -u : » et dernière ligne « code 0 » attendus")
        m = [re.match(motif, l) for l in lignes]
        m = [x for x in m if x]
        if len(m) != 1:
            raise Refus(f"{nom} : ligne de bilan introuvable ou en double")
        g = [int(x) for x in m[0].groups()]
        out[cle] = g
        out[cle + "_date"] = lignes[0][len("# date -u : "):].split(" ")[0]
    e, mu, b, r = out["essais"], out["mutations"], out["blanc"], out["repetition"]
    if not (e[0] == e[1] and e[2] == 0 and mu[0] == mu[1] + mu[2] == mu[3] and mu[4] == 0 and b[0] == b[1] and b[2] == 0
            and r[0] == r[1] and r[2] == 0):
        raise Refus(f"jeux de la v2 non tous conformes : {e}, {mu}, {b}, {r}")
    return out


def table(lignes_table, h, s, indent="  "):
    t = [f"{indent}| pièce | rôle | empreinte |", f"{indent}|---|---|---|"]
    for nom, role in lignes_table:
        role = (role.replace("@@ESSAIS_N@@", str(s["essais"][0])).replace("@@MUT_A@@", str(s["mutations"][1]))
                .replace("@@MUT_B@@", str(s["mutations"][2])))
        t.append(f"{indent}| `{nom}` | {role} | " + (f"`{h[nom]}`" if nom in h else "son compagnon") + " |")
    return "\n".join(t) + "\n"


def remplir(texte, valeurs):
    for k, v in valeurs.items():
        texte = texte.replace(f"@@{k}@@", str(v))
    if "@@" in texte:
        raise Refus(f"valeur non remplie : {texte[texte.index('@@'):texte.index('@@') + 30]!r}")
    return texte


def c_pieces(dossier, heure):
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", heure):
        raise Refus("HEURE_UTC : AAAA-MM-JJTHH:MM:SSZ (date -u +%FT%TZ)")
    exiger_tour1(dossier)
    for cible, t in faire_code(dossier).items():   # le code v2 du dossier est celui que `code` écrit, et il est scellé
        with open(os.path.join(dossier, cible), encoding="utf-8") as f:
            if f.read() != t:
                raise Refus(f"{cible} : différent de ce que les couples du code écrivent")
        compagnon_egal(dossier, cible)
    s = lire_sorties(dossier)
    ecarts = {k: s[k][0] for k, n in ATTENDUS_V2.items() if s[k][0] != n}
    if ecarts:
        raise Refus(f"comptes des jeux différents de ceux que le texte affirme : {ecarts} (attendus {ATTENDUS_V2})")
    h = {nom: (sha(os.path.join(dossier, nom)) if nom == NOM_PROGRAMME else compagnon_egal(dossier, nom)) for nom, _ in TABLE_V2}
    v = {"HEURE": heure, "PROG": h[NOM_PROGRAMME], "ESSAIS_N": s["essais"][0], "MUT_N": s["mutations"][0], "MUT_A": s["mutations"][1],
         "MUT_B": s["mutations"][2], "BLANC_N": s["blanc"][0], "BLANC_S": s["blanc"][3], "REP_N": s["repetition"][0],
         "D_ESSAIS": s["essais_date"], "D_MUT": s["mutations_date"], "D_BLANC": s["blanc_date"], "D_REP": s["repetition_date"]}
    for nom, cle in (("sortie-essais-crible-iii-v2.txt", "H_ESSAIS"), ("sortie-mutations-crible-iii-v2.txt", "H_MUT"),
                     ("sortie-essai-a-blanc-crible-iii-v2.txt", "H_BLANC"), ("sortie-repetition-machine-crible-iii-v2.txt", "H_REP")):
        v[cle] = h[nom]
    t2 = table(TABLE_V2, h, s)
    rapport = appliquer(lire_source(dossier, "rapport-crible-iii-v1.md"),
                        [(a, remplir(n, v)) for a, n in couples_rapport(t2)], "rapport v2")
    t2p = table(TABLE_V2 + [("rapport-crible-iii-v2.md", "rapport v2 (ce qui reste avant le feu ; réponse au tour 1, § 7)")], h, s)
    procedure = appliquer(lire_source(dossier, "procedure-machine-crible-iii-v1.md"),
                          [(a, remplir(n, v)) for a, n in couples_procedure(t2p)], "procédure v2")
    for nom, t in (("rapport-crible-iii-v2.md", rapport), ("procedure-machine-crible-iii-v2.md", procedure)):
        if os.path.exists(os.path.join(dossier, nom)):
            raise Refus(f"{nom} existe déjà (jamais écrasé)")
    for nom, t in (("rapport-crible-iii-v2.md", rapport), ("procedure-machine-crible-iii-v2.md", procedure)):
        ecrire_neuf(os.path.join(dossier, nom), t)
        print(f"écrit {nom} : {hashlib.sha256(t.encode('utf-8')).hexdigest()}")
    return 0


ATTENDUS_V2 = {"essais": 45, "mutations": 41, "blanc": 28, "repetition": 14}   # comptes que le texte ci-dessous affirme

VERSION_RAPPORT = r'''- **Version** : v2, scellée à @@HEURE@@ (`date -u`) ; suit la v1 (`aac9c95c…`, gardée telle quelle). Corrections du tour 1 de la
  contre-lecture du code (`contre-lecture-code-crible-iii-tour1-v1.md`, `c0c66dd5…`, verdict « corrections » : deux majeures,
  quatre mineures) appliquées par un rédacteur neuf du modèle C, qui n'a écrit ni la pièce, ni le code v1, ni ce rapport en v1, ni
  le rapport du tour 1, par le programme de couples `appliquer_corrections_crible_iii_tour1_v1.py` (`@@PROG@@`) ; réponse point
  par point au § 7. Ne change que ce que ces corrections et les noms neufs qu'elles entraînent (R12) exigent : en tête (titre,
  cette puce), § 1 (table v2 ajoutée), § 2 (noyau, lanceur, machine), § 3 (jeux de la v2 ajoutés), § 4 (points 1, 2 et 4, chemin
  court), § 6 (une réserve levée), § 7 (neuf). Aucune machine, aucun appel, aucune clé, aucune dépense ; rien de committé.
'''

JEUX_V2 = r'''Interpréteur `/usr/bin/python3` (3.13.18, numpy 2.5.3, celui qu'exige la configuration v12) ; arbre 605e0f6 dépaqueté du paquet
`e3d83e47…` dans un dossier jetable ; mondes de développement `4036f512…` (quatre mondes à graine publique, chacun servi cinq
fois) ; relevé de la sonde v74 `f56d9c0e…` ; conteneur chargé par d'autres sessions (charge de 8 à 14 sur quatre cœurs), jeux
sous `nice`.

- **Essais du niveau A** (`essais_crible_iii_v2.py`, @@D_ESSAIS@@) : **@@ESSAIS_N@@ cas, @@ESSAIS_N@@ passés** : les 42 de la v1 et trois du
  tour 1 : « exception du gardien » (sain : gardien conforme, 20 mondes complets, chaque appel fait listé ; artefact : gardien qui
  lève sur l'appel H du monde 3 → arrêt « exception du gardien », code 3, l'appel au relevé, sa dépense comptée) ; « exception dans
  un monde » (filtre qui lève au monde 3 pendant que son appel S est en vol → arrêt « exception d'un monde », code 3, monde
  incomplet, aucun monde « en cours », l'appel S au relevé) ; « arrêt réel d'un appel en vol après la ligne du minimum » (cinq
  mondes sans passe 1 déclenchent le minimum pendant que l'appel S du monde 5 est en vol ; sain : il revient, « minimum », code 0 ;
  artefacts : il revient sans témoin, ou son gardien lève → l'arrêt réel remplace le minimum, code 3) ; sortie
  `sortie-essais-crible-iii-v2.txt` (`@@H_ESSAIS@@`).
- **Banc de mutations** (`mutations_crible_iii_v2.py --arbre … --mondes … --mondes-sha256 …`, @@D_MUT@@) : original sans échec aux
  niveaux A et B ; **@@MUT_N@@ mutations, @@MUT_N@@ tuées pour la raison attendue** : les 35 de la v1 (les 24 du noyau portées sur
  `crible_iii_v2.py`) ; cinq du tour 1 au niveau A (`try` du gardien retiré, `try` du monde retiré, appels en vol non attendus,
  arrêt réel après le minimum perdu dans l'appel et dans `Commun.arreter`) ; une au niveau B (m4 : « - {eid_k1} - k1_tau » retiré
  de `OutilsMR2.preparer`, sur une copie de la mesure, tuée par le cas `essais_arbre_k1`). Une mutation que les essais « tuent »
  par une exception, et non par l'échec de l'essai attendu, compte comme survivante : c'est le bon sens du refus (m6 du tour 1 ; le
  contre-lecteur l'a vu quand le disque du conteneur était plein) ; sortie `sortie-mutations-crible-iii-v2.txt` (`@@H_MUT@@`).
- **Essai à blanc complet** (`essai_a_blanc_crible_iii_v2.py`, @@D_BLANC@@) : **@@BLANC_N@@ cas, @@BLANC_N@@ conformes** en @@BLANC_S@@ s : les
  25 de la v1 et trois du tour 1 : sonde des gabarits avec D en panne (appel sous G2 en échec → « appel sous G2 non rendu (D, état
  echec) : G2 non éprouvé ») et avec B illisible (aucune carte admise → « aucune carte admise sous G2 (B) ») ; préparation réelle
  des mondes (quatre mondes distincts : l'effet de K1 et ce que K1 porte hors des composantes comptées, toutes certifiées ;
  artefact refusé) ; sortie `sortie-essai-a-blanc-crible-iii-v2.txt` (`@@H_BLANC@@`).
- **Répétition de la machine** (`repetition_machine_crible_iii_v2.sh`, @@D_REP@@) : **@@REP_N@@ cas, @@REP_N@@ conformes** (les cas de la
  v1, sur l'amorce, le programme machine, l'aide et l'outil de la session v2 et les six fichiers du crible) ; sortie
  `sortie-repetition-machine-crible-iii-v2.txt` (`@@H_REP@@`).
'''

SECTION_7 = r'''
## 7. Contre-lecture

- **Rapport** : `contre-lecture-code-crible-iii-tour1-v1.md`
  (`c0c66dd585585257bb3fa18c6aff66d298b93d09ccce5536423362e14d5a0f80`), tour 1, lecteur C, sous-agent neuf ; verdict
  **« corrections »** (deux majeures, quatre mineures ; aucune ne met la conception en cause) ; ses rejeux (niveau A 42 sur 42, banc
  35 sur 35 au second passage, essai à blanc 25 sur 25) confirmaient ceux de la v1.
- **Application** : par un rédacteur neuf du modèle C, avec `appliquer_corrections_crible_iii_tour1_v1.py` (`@@PROG@@`) : il exige
  l'empreinte de chaque source v1 et celle du rapport du tour 1, chaque « ancien » une seule fois au moment de son couple, et
  n'écrase aucune cible ; `code` écrit les dix fichiers de code v2 ; `pieces` refait ces dix fichiers en mémoire, les exige égaux à
  ceux du dossier et à leurs compagnons, lit les bilans des sorties gardées de la v2 (tout conforme exigé), puis écrit ce rapport
  et la procédure v2. Les jeux du § 3 (v2) sont rejoués après les couples.

**Réponse point par point** :

1. **Majeure 1** (exception avalée dans un fil : appel perdu du relevé, aucun arrêt) : **appliquée**. Les deux couples du rapport
   sont recopiés tels quels dans `crible_iii_v2.py`. **Complément déclaré**, hors de leur lettre : un monde en exception laisse
   ses fils d'appel en vol (S et H, ou D et B), que rien n'attendait ; tous les fils d'appel lancés sont désormais attendus avant que
   le relevé ne soit bâti (`fils_d_appel`), sans quoi un appel en vol au moment de l'exception pouvait encore manquer au relevé, le
   défaut même que la majeure exclut. Essais ajoutés au niveau A : « exception du gardien » et « exception dans un monde » (§ 3).
   L'attendu « 100 appels listés » du rapport est lu « chaque appel fait est listé » : l'arrêt arrête les files, les mondes
   suivants ne sont pas commencés et les 100 appels ne sont pas faits. Mutations ajoutées : chacun des deux `try` retiré, et le
   complément retiré ; toutes tuées pour la raison attendue.
2. **Majeure 2** (sonde « saine » quand un appel sous G2 n'a rien rendu) : **appliquée**. Couple du rapport recopié dans
   `lanceur_crible_iii_v2.py` ; couple de la procédure recopié (attendu du geste 0) ; la procédure v2 dit aussi la règle au § 2,
   point 3. Ce n'est pas une quatrième règle d'avance de la pièce (G1 et G2 ne sont pas réécrits) : c'est la garde de validité de
   la sonde ; une sonde à refaire demande une ligne neuve (une seule exécution par ligne) : décision de la mère. Essais ajoutés au
   niveau B (essai à blanc) : D en panne, B illisible ; sain : le cas existant. Aucune mutation demandée, aucune ajoutée (le
   lanceur n'est pas au banc ; les deux artefacts refusés et le cas sain tiennent lieu de R5).
3. **Mineure 3** (arrêt réel perdu derrière la ligne du minimum) : **appliquée** ; les quatre couples du rapport recopiés. Essai
   ajouté au niveau A, avec un second artefact (gardien qui lève sur l'appel en vol), pour éprouver aussi le couple de
   `Commun.arreter`. Mutations : couple de l'appel et couple de `Commun.arreter` remis à l'ancien, tuées ; les couples de la limite
   de débit et de la part, de même forme, ne sont pas éprouvés à part (réserve).
4. **Mineure 4** (préparation réelle des mondes hors du banc) : **appliquée**. Cas `essais_arbre_k1` dans `essais_crible_iii_v2.py`,
   joué par l'essai à blanc et par le banc (`--arbre`) : pour chaque monde de développement distinct, `eid_k1 ∉ comptees`,
   `comptees ∩ k1_tau = ∅`, `comptees ⊆ certifiees` ; un monde préparé puis faussé (effet de K1 remis) est refusé. La mutation de
   niveau B (« - {eid_k1} - k1_tau » retiré, sur une copie de la mesure) est tuée par ce cas. La mesure n'est pas changée.
5. **Mineure 5** (garde du texte de passe 2 tautologique) : **appliquée par la phrase**, le choix étant laissé à la mère : la phrase
   du § 2 est le plus petit changement ; la comparaison de l'octet envoyé au relais dans `fabriquer_appeler` demanderait du code et
   des essais neufs, sans être exigée. Le texte de H n'est contrôlé que par son empreinte au relevé : dit au § 2.
6. **Mineure 6** (deux phrases) : **appliquée** : § 3 (une mutation « tuée » par une exception compte comme survivante ; dit aussi
   dans l'aide du banc v2) ; procédure v2, § 2 point 6 et § 5 (la concurrence réelle non éprouvée est dite à Lazar dans le préavis).

**Remarques facultatives** (aucune n'est une correction) :
- L'analyseur accepte aussi un objet `{"ensembles": […]}`, plus large que « liste JSON de listes d'entiers » de la pièce : gelé tel
  quel, sans conséquence, **dit ici**.
- Second appel de Pr-4 sous G2 à la sonde (au plus 3 USD de plus, plafond κiii0 porté à 10 USD) : **non appliqué** ; c'est un
  changement de forme de la sonde et de sa ligne : à proposer à Lazar par la mère, comme le lecteur l'écrit.
- Choix déclarés du § 5 (modèle servi différent → code 3, aucune relance sur un code 2, aucun abandon de proposeur, cartes au-delà
  du k-ième ensemble), procédure tapable, aucune valeur de clé ni identifiant de modèle : validés par le lecteur ; rien à changer.

**Pour la mère** (rapport du tour 1, § 4) : point 1 (ligne du minimum presque sûre au taux du pilote) inchangé, déjà au § 4,
point 9 ; point 2 fait (v2 et ce rapport) ; point 3 fait (§ 3) ; point 4 inchangé (§ 4) ; point 5 : le disque était encore à 97 %
(1,3 à 1,5 Go libres) pendant les jeux de la v2 ; aucun jeu n'a échoué pour cette cause.

**Conséquences des noms neufs** (R12), déclarées : le noyau v2 impose un lanceur neuf (il importe le noyau), donc une aide et un
programme machine neufs (ils nomment le lanceur et les fichiers du crible), une amorce neuve (elle prend le programme machine et
son aide par leurs noms), un outil de la session neuf (il nomme l'amorce et le programme machine) et une répétition neuve ; les
essais, le banc et l'essai à blanc suivent. La mesure et la lecture (noms réservés par la pièce), le relais factice, les gardes de
la session, les doublures et le devis ne changent pas. `crible_iii_v1.py` reste au jeu des fichiers du crible parce que la mesure
l'importe (constantes, `racine_graines`, `traits_employes`, inchangés en v2) : **six fichiers** à l'addendum au lieu de cinq.
`VERSION` du lanceur devient `lanceur-crible-iii-v2` ; celle du noyau (`crible-iii-v1`, nom du crible), l'étiquette des graines
et l'étiquette de la machine (`crible-iii-v1-AAAAMMJJ`) ne changent pas.

**Tour suivant** : tour différentiel sur la v2 (ce programme de couples, les dix fichiers de code v2 contre leurs v1, ce rapport,
la procédure v2, les sorties v2), par un sous-agent neuf d'un autre modèle que les auteurs du code v1 (A) et des couples (C), R2.
Rien n'a changé dans la pièce qui fait foi ni dans ses prédictions.

**Incidents de ma main** :
@@INCIDENTS@@
'''

SECTION_6_PROCEDURE = r'''- **Tour 1** (code et procédure v1) : `contre-lecture-code-crible-iii-tour1-v1.md` (`c0c66dd5…`), lecteur C ; verdict
  « corrections » (deux majeures, quatre mineures), appliquées en v2 par un rédacteur neuf du modèle C ; réponse point par point
  au § 7 du rapport v2. En bref : M1 appliquée (noyau v2, avec un complément déclaré : appels en vol attendus) ; M2 appliquée
  (lanceur v2 ; ici, attendu du geste 0 recopié et règle dite au § 2, point 3) ; m3 appliquée (noyau v2) ; m4 appliquée (cas du
  niveau B et mutation) ; m5 appliquée par la phrase du rapport ; m6 appliquée (rapport, § 3 ; ici, § 2 point 6 et § 5) ; second
  appel de Pr-4 sous G2 à la sonde (remarque facultative) non appliqué, à proposer à Lazar.
- **À faire (R2)** : un tour différentiel sur la v2, par un sous-agent neuf d'un autre modèle que les auteurs du code v1 (A) et des
  couples (C) ; fichiers à lui donner : la pièce qui fera foi et son dernier rapport de contre-lecture ; ce dossier entier (v2 et
  v1 gardées : code, essais, sorties gardées, devis, rapports, programme de couples) ; le rapport du tour 1 ; la procédure v14 du
  pilote et ses pièces `sans-ssh-v2/`, `sans-ssh-v3/`, `sans-ssh-v4/` (branche `lot/compte-organisme-v1`) ; la procédure v6 de
  l'idée 1.1 et son dossier.
'''

VERSION_PROCEDURE = r'''- **Version** : v2, scellée à @@HEURE@@ (`date -u`) ; suit la v1 (`d753c35a…`, gardée telle quelle) ; corrections du tour 1 de la
  contre-lecture du code (`contre-lecture-code-crible-iii-tour1-v1.md`, `c0c66dd5…`) appliquées par un rédacteur neuf du modèle C,
  par `appliquer_corrections_crible_iii_tour1_v1.py` (`@@PROG@@`). Ne changent que : en tête (titre, statut, cette puce, pièces),
  § 1 points 0 et 2 (amorce v2, six fichiers), § 2 points 2, 3 et 6 (six fichiers et tour différentiel, règle neuve de la sonde,
  préavis), § 4 (constantes, geste 0 et son attendu), § 5 (concurrence dite à Lazar), § 6 (contre-lecture).
'''

INCIDENTS = r'''- Un programme d'essai jetable de ma main (dans le dossier de session, pour voir l'effet de K1 sur les mondes de développement)
  n'avait pas la garde `if __name__ == "__main__"` : chaque processus de son pool relançait le programme, et le pool les remplaçait
  sans fin pendant environ 22 minutes, sur un conteneur déjà chargé ; arrêté par son PID (R10), ses enfants avec lui ; rien d'autre
  touché. Le cas `essais_arbre_k1` du dossier, lui, est sous cette garde.
- Lectures seules dans le dossier de session de la mère : le paquet `e3d83e47…` (dépaqueté dans mon propre dossier jetable, tête
  605e0f6, propre), les mondes de développement `4036f512…` et le dossier du relevé de la sonde v74 `f56d9c0e…` (copiés chez moi
  après contrôle des empreintes). Un `git branch -a` filtré (seule la ligne `lot/compte-organisme-v1` affichée) ; aucune branche
  `calcul/pilote-mr2-v74-entree-*` ouverte ; aucun fetch, aucun commit.
- Les relais factices ont occupé les ports 8811 et 8812 pendant la mise au point de la sonde et l'essai à blanc, arrêtés par le
  lanceur ; des processus d'autres sessions tournaient en même temps (charge de 8 à 14), non touchés.
- Disque du conteneur à 97 % (1,3 à 1,5 Go libres) pendant tout le travail ; fichiers de travail dans mon dossier jetable seulement.
'''


def couples_rapport(t2):
    return [
        ("# Rapport — code neuf de lancement du crible (iii), v1\n", "# Rapport — code neuf de lancement du crible (iii), v2\n"),
        ("- **Pièce qui fait foi** : `docs/notes/", VERSION_RAPPORT + "- **Pièce qui fait foi** : `docs/notes/"),
        ("## 1. Pièces écrites (toutes neuves, scellées par compagnon)\n\n  | pièce | rôle | empreinte |\n",
         "## 1. Pièces (v2 : neuves, ou gardées de la v1 ; chacune scellée par compagnon)\n\n" + t2
         + "\n  Pièces de la v1, gardées telles quelles (R12) ; celles que la v2 remplace (lanceur, amorce, programme machine et aide,\n"
         "  outil de la session, répétition, essais, banc, essai à blanc, leurs sorties) ne sont plus employées, et le noyau v1 ne l'est\n"
         "  plus que par la mesure :\n\n  | pièce | rôle | empreinte |\n"),
        ("- **Noyau** (`crible_iii_v1.py`) :", "- **Noyau** (`crible_iii_v2.py` ; le v1, gardé, n'est plus importé que par la mesure) :"),
        ("textes de passe 2 et de B contrôlés à l'octet avant l'appel ;",
         "textes de passe 2 et de B bâtis par la même fonction puis comparés à l'octet avant l'appel (garde qui ne peut pas échouer\n"
         "  en production et ne compare pas le texte de H : elle ne sert qu'aux essais qui forcent un texte ; la défense réelle est\n"
         "  l'empreinte `texte_servi_sha256` de chaque appel au relevé, audit R4, et la relecture des corps des relais à l'essai à blanc ;\n"
         "  m5 du tour 1) ;"),
        ("  plafonds exacts 260 et 3 USD).\n",
         "  plafonds exacts 260 et 3 USD). En v2 (tour 1) : une exception du gardien arrête le crible (code 3, « exception du\n"
         "  gardien »), l'appel restant au relevé avec sa dépense ; une exception dans un monde (analyseur, filtre, textes) l'arrête aussi\n"
         "  (code 3, « exception d'un monde »), le monde compté incomplet ; tous les fils d'appel lancés sont attendus avant que le relevé\n"
         "  ne soit bâti ; un arrêt réel (témoin absent, coût au-dessus du pire cas, part atteinte, limite de débit, exception) survenu\n"
         "  après la ligne du minimum la remplace (code 3 : « non jugeable (arrêt) » à l'étage 0 de la lecture, et non « non concluant »).\n"),
        ("- **Lanceur** (`lanceur_crible_iii_v1.py`) :", "- **Lanceur** (`lanceur_crible_iii_v2.py`) :"),
        ("`sonde-gabarits` (κiii0 : trois appels, règles d'avance, III-7 par sa règle)",
         "`sonde-gabarits` (κiii0 : trois appels, règles d'avance, III-7 par sa règle ; en v2, M2 du tour 1 : un appel sous G2 non\n"
         "  rendu, ou complet sans carte admise, déclenche aussi la règle, « G2 non éprouvé, sonde à refaire, crible non lancé »)"),
        ("- **Machine et session** : amorce,",
         "- **Machine et session** (v2 : noms neufs seulement ; six fichiers du crible à l'addendum) : amorce,"),
        ("## 3. Essais joués (sorties gardées dans ce dossier)\n\n",
         "## 3. Essais joués (sorties gardées dans ce dossier)\n\n### Jeux de la v2, rejoués après les couples du tour 1\n\n" + JEUX_V2
         + "\n### Jeux de la v1, gardés tels quels\n\n"),
        ("1. **Contre-lecture du code** (pièce, Étapes, point 0) : un sous-agent neuf **d'un autre modèle**, sur ce dossier entier et la\n"
         "   procédure (§ 6 de la procédure : fichiers à lui donner).",
         "1. **Contre-lecture du code** (pièce, Étapes, point 0) : tour 1 fait (`contre-lecture-code-crible-iii-tour1-v1.md`,\n"
         "   « corrections », appliquées en v2 : § 7) ; reste un **tour différentiel** sur la v2, par un sous-agent neuf d'un autre modèle\n"
         "   que les auteurs du code v1 (A) et des couples (C), sur ce dossier entier et la procédure v2 (§ 6 de la procédure : fichiers à\n"
         "   lui donner)."),
        ("si une règle d'avance se déclenche, gabarit\n   réécrit, nouvelle sonde, crible non lancé ;",
         "si une règle d'avance se déclenche, gabarit\n   réécrit, nouvelle sonde, crible non lancé (en v2, M2 : un appel sous G2 non rendu ou sans carte admise déclenche aussi\n"
         "   la règle : G2 non éprouvé, sonde à refaire sur une ligne neuve) ;"),
        ("les cinq fichiers du crible (empreintes du § 1, ou celles de la\n   version contre-lue)",
         "les **six** fichiers du crible en v2 (`crible_iii_v1.py`, que la\n   mesure importe, `crible_iii_v2.py`,"
         " `lanceur_crible_iii_v2.py`, `mesure_crible_iii_v1.py`, `lire_crible_iii_v1.py`,\n   `relais_factice_crible_iii_v1.py` :"
         " empreintes du § 1, ou celles de la version que le tour différentiel rendra scellable)"),
        ("le chemin court est : contre-lecture du code → sonde des gabarits →",
         "le chemin court est : tour différentiel du code v2 → sonde des gabarits →"),
        ("  factices) : à relire par le contre-lecteur.\n",
         "  factices) : à relire par le contre-lecteur (levée en v2 : cas du niveau B et mutation, m4 ; § 3 et § 7).\n"),
        ("  être affichées) ; les sorties des relais (corps, réponses brutes), qui en portent, sont restées dans le dossier jetable.\n",
         "  être affichées) ; les sorties des relais (corps, réponses brutes), qui en portent, sont restées dans le dossier jetable.\n"
         + SECTION_7.replace("@@INCIDENTS@@\n", INCIDENTS)),
    ]


def couples_procedure(t2p):
    return [
        ("# Procédure de la machine louée du crible (iii) — v1\n", "# Procédure de la machine louée du crible (iii) — v2\n"),
        ("**ne part pas au feu** avant les préalables du § 2 (contre-lecture du code et de cette procédure par un\n"
         "  sous-agent neuf d'un autre modèle, R2 ;",
         "**ne part pas au feu** avant les préalables du § 2 (contre-lecture du code et de cette procédure : tour 1\n"
         "  rendu « corrections », appliquées en v2 ; reste le tour différentiel sur la v2, R2 ;"),
        ("- **Pièces** (dossier `docs/procedures/crible-iii-v1/`, chacune avec son compagnon `.sha256`) :\n\n  | pièce | rôle | empreinte |\n",
         VERSION_PROCEDURE + "- **Pièces** (dossier `docs/procedures/crible-iii-v1/`, chacune avec son compagnon `.sha256`) ; en v2 :\n\n" + t2p
         + "\n  En v1 (gardées telles quelles ; celles que la v2 remplace ne sont plus employées, et le noyau v1 ne l'est plus que par la\n"
         "  mesure) :\n\n  | pièce | rôle | empreinte |\n"),
        ("0. **Amorce** (`amorce_crible_iii_v1.sh`, passée compressée", "0. **Amorce** (`amorce_crible_iii_v2.sh`, passée compressée"),
        ("code du crible **égal à l'addendum** (cinq fichiers, ligne « empreinte  chemin »)",
         "code du crible **égal à l'addendum** (six fichiers, ligne « empreinte  chemin »)"),
        ("2. **Contre-lecture du code** (les cinq fichiers du crible, la machine, la session, cette procédure, les essais et leurs sorties) par\n"
         "   un sous-agent neuf **d'un autre modèle** (pièce, Étapes, point 0) ;",
         "2. **Contre-lecture du code** (les six fichiers du crible, la machine, la session, cette procédure, les essais et leurs sorties) par\n"
         "   un sous-agent neuf **d'un autre modèle** (pièce, Étapes, point 0) : tour 1 fait (« corrections », appliquées en v2), tour\n"
         "   différentiel à faire sur la v2, par un sous-agent neuf d'un autre modèle que les auteurs du code v1 (A) et des couples (C) ;"),
        ("pour chacun des cinq fichiers du crible, l'empreinte du texte",
         "pour chacun des six fichiers du crible (`crible_iii_v1.py`,\n   `crible_iii_v2.py`, `lanceur_crible_iii_v2.py`,"
         " `mesure_crible_iii_v1.py`, `lire_crible_iii_v1.py`, `relais_factice_crible_iii_v1.py`), l'empreinte du texte"),
        ("   (gabarit réécrit, nouvelle sonde sur nouvelle ligne, crible non lancé).\n",
         "   (gabarit réécrit, nouvelle sonde sur nouvelle ligne, crible non lancé). En v2 (M2 du tour 1), un appel sous G2 non rendu, ou\n"
         "   complet sans carte admise, déclenche aussi la règle : G2 non éprouvé, sonde à refaire sur une ligne neuve, crible non lancé.\n"),
        ("**préavis** à Lazar avant l'impression (création imminente, échéance à\n"
         "   17 h, exposition de la clé dans la configuration de l'instance jusqu'à la destruction).",
         "**préavis** à Lazar avant l'impression (création imminente, échéance à\n"
         "   17 h, exposition de la clé dans la configuration de l'instance jusqu'à la destruction, et concurrence réelle chez le\n"
         "   fournisseur, vingt sessions à la fois, non éprouvée : § 5)."),
        ("OUTIL=\"env W=$W ENVP=$ENVP bash $DC/session_crible_iii_v1.sh\"", "OUTIL=\"env W=$W ENVP=$ENVP bash $DC/session_crible_iii_v2.sh\""),
        ("`python3 -I -B $DC/lanceur_crible_iii_v1.py generer --public", "`python3 -I -B $DC/lanceur_crible_iii_v2.py generer --public"),
        ("`GO_ID=<κiii0> python3 -I -B $DC/lanceur_crible_iii_v1.py sonde-gabarits",
         "`GO_ID=<κiii0> python3 -I -B $DC/lanceur_crible_iii_v2.py sonde-gabarits"),
        ("Attendu :\n   `regles_d_avance` non déclenchée, trois appels.",
         "Attendu :\n   `regles_d_avance` non déclenchée, trois appels tous à l'état `complet`, des cartes admises sous chacun des deux appels sous G2."),
        ("  la limite réelle ; la ligne « limite de débit » de la liste d'arrêt la garde au premier tour des files.\n",
         "  la limite réelle ; la ligne « limite de débit » de la liste d'arrêt la garde au premier tour des files ; dit à Lazar dans le\n"
         "  préavis (§ 2, point 6 ; m6 du tour 1).\n"),
        ("À faire (R2) : un sous-agent neuf **d'un autre modèle** que l'auteur, qui n'a écrit ni la pièce ni ce code ; fichiers à lui donner :\n"
         "la pièce qui fera foi et son dernier rapport de contre-lecture ; ce dossier entier (code, essais, sorties gardées, devis, rapport) ;\n"
         "la procédure v14 du pilote et ses pièces `sans-ssh-v2/`, `sans-ssh-v3/`, `sans-ssh-v4/` (branche `lot/compte-organisme-v1`) ; la\n"
         "procédure v6 de l'idée 1.1 et son dossier.\n",
         SECTION_6_PROCEDURE),
    ]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
