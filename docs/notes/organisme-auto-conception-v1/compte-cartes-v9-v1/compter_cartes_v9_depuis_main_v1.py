"""Premier compte des 94 cartes de la course d'auto-conception v9 — v1.

Lit deux pièces seules, données en arguments :
  1. proposition-cartes-a-eprouver-v9-v1.md (sha256 a2cd45ad...)
  2. lecture-course-v9-v1.md               (sha256 0306adf7...)
Rend un JSON sur la sortie standard : comptes, source exacte (fichier,
ligne), recouvrement dit. Aucun texte de carte (ni titre, ni identifiant).
Aucun accès réseau, aucune autre lecture.

Usage : python -I compter_cartes_v9_depuis_main_v1.py PROPOSITION LECTURE
"""
import hashlib
import json
import os
import re
import sys

EMPREINTE_PROPOSITION = "a2cd45adf7c49a909ad14be378b75b3233eae198b7f51cc416450f4cd878d856"
EMPREINTE_LECTURE = "0306adf74d321cfa933e047adff28324092787f870a2bf97bafd9d52bd5ffddb"
MOTS_NOMBRES = {"treize": 13}


def lire(chemin, attendue):
    with open(chemin, "rb") as f:
        brut = f.read()
    empreinte = hashlib.sha256(brut).hexdigest()
    if empreinte != attendue:
        raise SystemExit(f"empreinte inattendue pour {os.path.basename(chemin)} : {empreinte}")
    return brut.decode("utf-8").split("\n"), empreinte


def ligne_unique(lignes, motif, nom):
    trouvees = [i for i, l in enumerate(lignes, 1) if re.search(motif, l)]
    if len(trouvees) != 1:
        raise SystemExit(f"{nom} : {len(trouvees)} lignes trouvées, une attendue")
    return trouvees[0]


def entier(motif, texte, nom):
    m = re.search(motif, texte)
    if not m:
        raise SystemExit(f"{nom} : motif absent")
    return m


def main(chemin_prop, chemin_lect):
    prop, emp_prop = lire(chemin_prop, EMPREINTE_PROPOSITION)
    lect, emp_lect = lire(chemin_lect, EMPREINTE_LECTURE)
    f_prop = os.path.basename(chemin_prop)
    f_lect = os.path.basename(chemin_lect)

    # --- Proposition : total, exclusions, plancher, lignes, dessous.
    l_total = ligne_unique(prop, r"Les 94 cartes à passeport lues", "total")
    total = int(entier(r"Les (\d+) cartes à passeport", prop[l_total - 1], "total").group(1))

    l_excl = ligne_unique(prop, r"^- \*\*Exclusions\.\*\*", "exclusions")
    texte_excl = prop[l_excl - 1]
    # Cartes exclues nommées par X1 et X2 (identifiants entre accents graves) ;
    # X6 désigne les deux cartes retenues, hors des 94 (l. du total).
    exclues = len(re.findall(r"`f[0-9a-f]{12}`", texte_excl))

    l_plancher = ligne_unique(prop, r"^- \*\*Au plancher ou au-dessus\*\*", "plancher")
    t = prop[l_plancher - 1]
    m = entier(r"Au plancher ou au-dessus\*\* : (\d+) cartes, en (\w+) lignes", t, "plancher")
    au_plancher = int(m.group(1))
    mot_lignes = m.group(2)
    lignes_texte = int(mot_lignes) if mot_lignes.isdigit() else MOTS_NOMBRES[mot_lignes]
    dessous = int(entier(r"Sous le plancher\*\* : (\d+) cartes", t, "dessous").group(1))

    l_entete = ligne_unique(prop, r"^\| ligne \| porteuse \|", "table des lignes")
    rangs = []
    i = l_entete + 1  # ligne de séparation |---|
    while i < len(prop) and prop[i].startswith("|"):
        rangs.append(i + 1)
        i += 1
    lignes_table = len(rangs)

    # --- Lecture : cartes rendues (l. 38) et mentions par module (l. 99).
    l_rendues = ligne_unique(lect, r"^\*\*Cartes rendues\*\*", "cartes rendues")
    m = entier(r"(\d+) = (\d+) à passeport \+ (\d+) retenues", lect[l_rendues - 1], "rendues")
    rendues, passeport, retenues = (int(m.group(k)) for k in (1, 2, 3))

    l_mod = ligne_unique(lect, r"modules nommés dans le champ `module_change`", "modules")
    t = lect[l_mod - 1]
    corps = t.split(" : ", 1)[1].rstrip(".")
    mentions = {}
    for morceau in corps.split(", "):
        nom, n = morceau.rsplit(" ", 1)
        mentions[nom] = int(n)
    trois = {k: mentions[k] for k in ("tests de mort", "témoins plantés", "proposeurs")}
    somme_trois = sum(trois.values())
    somme_toutes = sum(mentions.values())

    controles = {
        "exclues + plancher + dessous = total": exclues + au_plancher + dessous == total,
        "lignes dites (texte) = rangs de la table": lignes_texte == lignes_table,
        "total de la proposition = cartes à passeport de la lecture": total == passeport,
        "passeport + retenues = rendues": passeport + retenues == rendues,
    }
    if not all(controles.values()):
        raise SystemExit(f"contrôle en échec : {controles}")

    src = lambda f, l: {"fichier": f, "ligne": l}
    return {
        "version": "compte-cartes-v9-depuis-main-v1",
        "pieces": [
            {"fichier": f_prop, "sha256": emp_prop},
            {"fichier": f_lect, "sha256": emp_lect},
        ],
        "rangement_des_94": {
            "total_cartes_a_passeport": {"valeur": total, "source": src(f_prop, l_total)},
            "exclues": {"valeur": exclues, "source": src(f_prop, l_excl),
                        "note": "une par X1, une par X2 ; X6 vise les deux cartes retenues, hors des 94"},
            "au_plancher_ou_au_dessus": {"valeur": au_plancher, "source": src(f_prop, l_plancher)},
            "lignes_apres_fusion": {"valeur": lignes_table, "source": src(f_prop, l_plancher),
                                    "rangs_de_table": {"fichier": f_prop, "lignes": [rangs[0], rangs[-1]]}},
            "sous_le_plancher": {"valeur": dessous, "source": src(f_prop, l_plancher)},
            "cartes_rendues_en_tout": {"valeur": rendues, "passeport": passeport, "retenues": retenues,
                                       "source": src(f_lect, l_rendues)},
        },
        "mentions_par_module": {
            "source": src(f_lect, l_mod),
            "valeurs": trois,
            "somme_des_trois": somme_trois,
            "somme_des_treize_modules": somme_toutes,
            "recouvrement": (
                "Une carte peut nommer plusieurs modules : la somme des trois "
                f"({somme_trois}) et celle des treize modules ({somme_toutes}) dépassent "
                f"{total}. Ces nombres sont des mentions, pas des cartes ; une mention "
                "n'est pas un changement (même ligne). Le nombre de cartes nommant au "
                f"moins un des trois modules est seulement borné : au moins {max(trois.values())}, "
                f"au plus min({somme_trois}, base). La base de la ligne (94 à passeport ou "
                f"{rendues} rendues) n'y est pas écrite."
            ),
        },
        "controles": controles,
        "ce_que_ce_compte_n_est_pas": [
            "pas le compte de la note (les mentions se recouvrent)",
            "pas un classement par barreau (aucune des deux pièces ne classe par barreau)",
            "une borne pour le devis des cartes, rien de plus",
        ],
    }


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("usage : compter_cartes_v9_depuis_main_v1.py PROPOSITION LECTURE")
    sortie = main(sys.argv[1], sys.argv[2])
    sys.stdout.write(json.dumps(sortie, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
