"""Épreuve de forme v11 — artefact « valeur p hors du demi-pas » — v1.

L'artefact « valeur p arrondie » de l'épreuve de forme v11 (valeur p haute du juge à la dose ½, arrondie à quatre
décimales) reste à moins d'un demi-pas de sa formule : il est refusé par l'égalité exacte de la valeur de la famille,
non par la condition (α) du demi-pas. Cet artefact-ci, construit sur la sortie saine du cas A (synthétique), écarte la
même valeur p haute de sa formule de **plus d'un demi-pas**, sans franchir aucun des quinze niveaux de Holm, et donne
la même écriture à la valeur de la famille : seule la condition (α) doit le refuser.

Rejoué par la règle de discrétion de l'analyse de la relance, version 13 (branche `claude/pensive-bardeen-1fv7hw`),
sous une configuration et un constat de lancement fabriqués par l'aide des essais de la v13, dans un dossier temporaire :
1. cas sain (la sortie du cas A, octet pour octet) : lu ;
2. artefact : arrêt de la lecture de la discrétion, garde de forme, champ de la valeur p haute, cas A, juge, dose ½ ;
   la fonction de l'écart (i) a rendu « alpha » pour cette lecture, et « beta » pour aucune ;
3. retrait : le demi-pas remplacé par 1 (la condition (α) ne peut plus mordre) : l'artefact est lu en entier — aucune
   autre garde ne le refuse.

Les chaînes du module que la configuration inscrit sont celles des essais de la v13, sauf la clé du module, la
statistique de l'agrégateur et la déclaration du schéma, prises de la sortie elle-même : seul le cas A est joué, aucun
motif n'est lu. Aucune donnée réelle : seize tâches factices, scores tirés par l'épreuve de forme.

    python -B artefact_demi_pas_v1.py <arbre de la relance> <sortie saine du cas A> <dossier neuf>
"""
from __future__ import annotations

import json
import sys
import tempfile
from fractions import Fraction
from pathlib import Path

ARBRE, SAINE, SORTIE = (Path(a).resolve() for a in sys.argv[1:4])
sys.path[:0] = [str(ARBRE / "src"), str(ARBRE / "tests")]

import aide_bras_a_v13 as h                                                       # noqa: E402
from controle_ia.organismes_discrets import analyse_bras_a_v13 as an               # noqa: E402
from controle_ia.organismes_discrets import arrets_bras_a_v12 as ar                # noqa: E402
from controle_ia.organismes_discrets import configuration_bras_a_v12 as cf         # noqa: E402
from controle_ia.scellement import sceller                                         # noqa: E402

NOM = "lecture-commune-moniteurs-bras-a.json"
MONITEUR, DOSE, CHAMP = "juge", "dose-0.50", "valeur_p_haut"
ECRITURE = "0.001"                       # valeur p haute et valeur de la famille de l'artefact, même écriture


def configuration_pour(tmp: Path, sortie: dict) -> Path:
    r = sortie["reglages"]
    chaines = {cf.CHAINE_DE_LA_CLE_DU_MODULE: "sha256", "statistique_agregateur": r["statistique_agregateur"],
               "declarations_du_schema": {cf.SCHEMA_ECHANGE: {"permutation": r["permutation"],
                                                              "unite_de_la_permutation": r["unite_de_la_permutation"]}}}
    c = h.fichier_de_configuration(tmp, pieces={cf.MODULE_DU_COTE_HABILITE: sortie["piece_source"]["sha256"]}, **chaines)
    assert h.constat(tmp, c)[1] is not None, "constat de lancement malsain"
    return c


def lire(tmp: Path, texte: str) -> dict:
    sortie = json.loads(texte)
    c = configuration_pour(tmp, sortie)
    piece = h.ecrire_scelle(h.nouveau_dossier(tmp, "livraison") / NOM, texte)
    try:
        r = an.regle_de_discretion(piece, c, go_de_la_reprise=None, registre_fige=None)
        return {"issue": "lue", "etats": {d: dict(m) for d, m in r["etats"].items()}}
    except ar.ArretDeLaLectureDeLaDiscretion as e:
        return {"issue": "arret", "constat": e.constat()}


def main() -> None:
    if SORTIE.exists():
        raise SystemExit(f"{SORTIE} existe déjà : on n'écrase jamais (R12)")
    texte_sain = SAINE.read_text(encoding="utf-8")
    s = json.loads(texte_sain)
    x = s["lectures"][DOSE][MONITEUR]
    grille, numerateur = x["n_permutations"], 1 + x["au_moins_egales"] + x["permutations_degenerees"]
    formule, rendue = Fraction(numerateur, 1 + grille), Fraction(ECRITURE)
    assert abs(rendue - formule) >= an.demi_pas_de_la_grille(grille), "l'artefact doit sortir du demi-pas"
    assert all((rendue <= n) == (formule <= n) for n in an.NIVEAUX_DE_HOLM), "aucun niveau de Holm franchi"
    assert x["valeur_p_pour_la_famille"] == x[CHAMP], "cas sain : valeur de la famille égale à la valeur p haute"
    # Écriture de l'artefact sur le texte même de la sortie saine : deux lignes changées, dans la seule lecture visée.
    ancienne = json.dumps(x[CHAMP])
    lignes = texte_sain.split("\n")
    debut = next(i for i, l in enumerate(lignes)
                 if l.strip() == f'"moniteur": "{MONITEUR}",' and lignes[i + 1].strip() == f'"dose": "{DOSE}",')
    changees = 0
    for i in range(debut, len(lignes)):
        for champ in (CHAMP, "valeur_p_pour_la_famille"):
            for fin_de_ligne in (",", ""):
                if lignes[i].strip() == f'"{champ}": {ancienne}{fin_de_ligne}':
                    lignes[i] = lignes[i].replace(f'"{champ}": {ancienne}', f'"{champ}": {ECRITURE}')
                    changees += 1
        if lignes[i].strip().startswith('"valeur_p_pour_la_famille"'):
            break
    assert changees == 2
    texte_artefact = "\n".join(lignes)
    a = json.loads(texte_artefact)
    a_x = a["lectures"][DOSE][MONITEUR]
    assert a_x[CHAMP] == a_x["valeur_p_pour_la_famille"] == float(ECRITURE)
    a_x2 = dict(a_x, **{CHAMP: x[CHAMP], "valeur_p_pour_la_famille": x["valeur_p_pour_la_famille"]})
    assert dict(a, lectures={**a["lectures"], DOSE: {**a["lectures"][DOSE], MONITEUR: a_x2}}) == s, "deux champs changés, rien d'autre"

    rendus = []
    original = an.valeur_p_qui_ne_repond_pas_a_ses_comptes

    def espion(champ, rendue_, numerateur_, grille_):
        r = original(champ, rendue_, numerateur_, grille_)
        rendus.append((champ, r))
        return r

    an.valeur_p_qui_ne_repond_pas_a_ses_comptes = espion
    with tempfile.TemporaryDirectory(prefix="artefact-demi-pas-") as t:
        tmp = Path(t)
        rendus.clear()
        sain = lire(tmp, texte_sain)
        conditions_sain = sorted({r for _, r in rendus}, key=str)
        rendus.clear()
        artefact = lire(tmp, texte_artefact)
        conditions_artefact = [r for _, r in rendus if r is not None]
        demi_pas = an.demi_pas_de_la_grille
        an.demi_pas_de_la_grille = lambda n: Fraction(1)
        try:
            retrait = lire(tmp, texte_artefact)
        finally:
            an.demi_pas_de_la_grille = demi_pas
    an.valeur_p_qui_ne_repond_pas_a_ses_comptes = original

    attendu = {"garde": ar.GARDE_FORME, "champ": CHAMP, "cas": "A", "moniteur": MONITEUR, "dose": DOSE}
    bilan = {
        "cas_sain": {"issue": sain["issue"], "conditions_de_l_ecart_i": [str(c) for c in conditions_sain]},
        "artefact": {"issue": artefact["issue"], "constat": artefact.get("constat"),
                     "conditions_de_l_ecart_i_en_defaut": conditions_artefact},
        "retrait_du_demi_pas": {"issue": retrait["issue"], "constat": retrait.get("constat")},
    }
    ok = (sain["issue"] == "lue" and conditions_sain == [None]
          and artefact["issue"] == "arret" and all(artefact["constat"].get(k) == v for k, v in attendu.items())
          and conditions_artefact == ["alpha"] and retrait["issue"] == "lue")
    bilan["verdict"] = "seule la condition du demi-pas refuse l'artefact ; le cas sain est lu" if ok else "NON CONFORME"

    dossier = SORTIE / "artefact-cas-a-valeur-p-hors-du-demi-pas"
    dossier.mkdir(parents=True)
    (dossier / NOM).write_text(texte_artefact, encoding="utf-8")
    sceller(dossier / NOM)
    releve = SORTIE / "releve-rejeu-artefact-demi-pas-et-cas-sain.json"
    releve.write_text(json.dumps(bilan, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    sceller(releve)
    print(json.dumps(bilan, ensure_ascii=False, indent=1))
    if not ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
