"""NON LANCÉ — EN ATTENTE DU MOT DE LAZAR. Programme qui enchaîne les étapes 3, 4, 5 et 6 du palier 0b (code v6), version 2,
écrit à part du paquet, sur le modèle de `lancer_etapes_6bis_et_7_v1.py` ; il n'a été exécuté que par ses essais, sous la couche
« essai-de-forme », sur une racine factice.

Ordre des opérations (v13:387 ; brouillon v15:395) : « 3. Audit du générateur (B1 : marges sur chaque monde ; présentation sur
50 suites par dose de la couche « audit »). 4. Couche mécanique : gardes de C6, fréquences M12, accord avec l'étage de
l'organisme. 5. Gel par programme du fichier des fréquences. 6. Étalonnage des réglages (B7) et gel de leur fichier. » L'étape 4
est entre 3 et 5, et l'étape 5 gèle ce qu'elle mesure : le programme la joue, par `etapes.lancer_etape_4`, le programme de
lancement de l'étape 4 que le texte nomme (B7 bis, « Version 12 »). Il n'appelle que des fonctions du code v6 :
1. le verrou : `graines.Autorisation(texte, racine)`, puis la pièce de contrôle de la mère, scellée (`graines.verifier_scelle`),
   qui doit porter le commit du code et l'empreinte de ce programme (PROPOSITION, comme pour le programme des étapes 6 bis et 7) ;
2. la copie du code de l'organisme (garde 17) : `organisme.EtageOrganisme`, qui la vérifie, construite avant toute étape ;
3. étape 3 : `mondes.audit_du_generateur` (couche « audit », 50 suites par dose, trois doses, 1 000 permutations) ; rapport
   écrit et scellé ; un arrêt (liste d'arrêt, point 2) est écrit et scellé, et la chaîne s'arrête ;
4. étape 4 : `etapes.lancer_etape_4` (couche « mecanique » ; valeurs gelées par défaut : neuf proposeurs, trois doses, 24
   sources, sous-ensemble de deux sources pour la garde 17 ; jeu de la garde 27) ; S8 (i) et la garde 17 y arrêtent ;
5. étape 5 : `frequences.geler` (fichier des fréquences M12 et son compagnon), puis relecture sous contrôle de son empreinte
   (`frequences.lire_gelees`) ;
6. étape 6 : `etapes.etape_6` (couche « etalonnage », 200 000 sources d'étalonnage), sur les fréquences relues ; elle gèle le
   fichier des réglages (`etalonnage.geler_reglages`, appelée par elle) ; puis (version 2) la condition 5 de la liste d'arrêt
   (v13:428, v15:436), lue à la lettre sur les réglages que rend `etape_6` (`liste_d_arret_point_5`) ;
et, pour chaque étape, un manifeste (`tirages.ecrire_manifeste`, règle R9) dans son dossier. Un arrêt d'une étape est écrit et
scellé avec son manifeste ; les étapes suivantes ne se jouent pas ; le programme s'arrête avec un code non nul.

Version 2 (vérification du programme v1, `5dae3b94…`, « À corriger », § 4) : la condition 5 de la liste d'arrêt, qu'aucun
programme ni le code v6 n'appliquait — « la taille de référence n'est atteignable, pour un contraste, à aucune dose non nulle ;
ou la force de référence du suiveur de forme n'est pas atteignable » → « arrêt : le banc ne sait pas planter l'effet de
référence » — est testée après l'étape 6, par une comparaison des réglages rendus (contraste de l'héritage : K à la taille 1 ;
contraste de la tenue : τ à la taille 1 ; aux deux doses non nulles ; φ à la force 1), sans calcul ; si elle est vraie, l'arrêt
est écrit par le même chemin que les autres (cause scellée, manifeste de l'étape 6 « arrêt », qui inscrit le fichier des réglages
déjà gelé) et le programme s'arrête. Rien d'autre ne change.

Usage, dossier courant : le dossier du code (celui qui porte `src/`), `PYTHONPATH=src` seul, interpréteur avec `-B` :

    python -B <chemin>/lancer_etapes_3_5_6_v2.py TEXTE RACINE COPIE_DE_L_ORGANISME DOSSIER

Ni couche ni taille sur la ligne de commande : couches « audit », « mecanique », « etalonnage », valeurs gelées du code v6. La
fonction `lancer` accepte la couche « essai-de-forme » (une seule pour les quatre étapes) et des tailles réduites pour ses seuls
essais ; toute autre couche est refusée avant tout geste.
"""

import hashlib
import json
import os
import sys

from controle_ia.heritage_etage_processeur_v1 import constantes as K
from controle_ia.heritage_etage_processeur_v1 import etalonnage as ET
from controle_ia.heritage_etage_processeur_v1 import etapes as EP
from controle_ia.heritage_etage_processeur_v1 import frequences as FR
from controle_ia.heritage_etage_processeur_v1 import graines as GR
from controle_ia.heritage_etage_processeur_v1 import mecanique as MC
from controle_ia.heritage_etage_processeur_v1 import mondes as MO
from controle_ia.heritage_etage_processeur_v1 import organisme as OR
from controle_ia.heritage_etage_processeur_v1 import tirages as TI

# couches des étapes (graines.py, l. 6 : « audit » (étape 3), « mecanique » (étape 4), « etalonnage ») ; l'étape 5 ne dérive rien
COUCHES_DES_ETAPES = {"3": "audit", "4": "mecanique", "6": "etalonnage"}
COUCHE_DES_ESSAIS = "essai-de-forme"
CHEMIN_PIECE_DE_CONTROLE = ("docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/"
                            "controle-lancement-palier-0b-par-la-mere-v1.md")
TACHE_DE_L_ORGANISME = "palier-0b|etape-4"  # PROPOSITION (silence : la tâche servie à l'organisme pour la garde 17)
FICHIER_DES_FREQUENCES = "frequences-m12-v1.json"
FICHIER_DES_REGLAGES = "reglages-v1.json"
# les arrêts nommés de chaque étape (liste d'arrêt) ; toute autre exception se propage sans être écrite
ARRETS = {"3": (MO.ArretGenerateur,),
          "4": (MC.ArretMecanique, FR.ArretFrequences, OR.DesaccordOrganisme, MO.ArretGenerateur, EP.ArretEtapes),
          "6": (EP.ArretEtapes, ET.ArretEtalonnage, FR.ArretFrequences)}
# tailles réduites que les essais peuvent donner (sous « essai-de-forme » seulement)
TAILLES_DES_ESSAIS = ("suites_par_dose", "permutations", "doses_etape_4", "proposeurs", "sources_etape_4", "sous_ensemble",
                      "sources_etalonnage")


class ArretProgramme(RuntimeError):
    pass


class ArretListeDArretPoint5(RuntimeError):
    """Version 2 : liste d'arrêt, point 5 (v13:428, v15:436)."""


def liste_d_arret_point_5(reglages):
    """Version 2 : la condition 5 de la liste d'arrêt, à la lettre, sur les réglages que rend `etapes.etape_6` (au format de
    `etapes.reglages_pour_le_plan` : None pour une cible non atteignable ; une cible absente compte comme non atteignable) —
    « la taille de référence n'est atteignable, pour un contraste, à aucune dose non nulle » (contraste de l'héritage : K, du
    lecteur réglé pour l'héritage ; contraste de la tenue : τ, du lecteur réglé pour la tenue ; B7) « ; ou la force de référence
    du suiveur de forme n'est pas atteignable » (φ à la force 1). Une comparaison, aucun calcul. Rend la liste des causes (vide si
    la condition est fausse)."""
    causes = []
    for contraste, reglage in (("héritage", "K"), ("tenue", "tau")):
        if all(reglages.get(reglage, {}).get((dose, K.TAILLE_REFERENCE)) is None for dose in K.DOSES_NON_NULLES):
            causes.append(f"taille de référence non atteignable pour le contraste de la {contraste} ({reglage}) à toutes les "
                          f"doses non nulles {list(K.DOSES_NON_NULLES)}")
    if reglages.get("phi", {}).get(K.FORCE_REFERENCE_SUIVEUR) is None:
        causes.append(f"force de référence du suiveur de forme ({K.FORCE_REFERENCE_SUIVEUR}) non atteignable")
    return causes


def empreinte_du_programme():
    with open(os.path.abspath(__file__), "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def verifier_pieces(texte, racine):
    """Le verrou du code v6, puis la pièce de contrôle de la mère : scellée sous la racine, portant le commit du code (celui de
    la pièce d'autorisation) et l'empreinte de ce programme (PROPOSITION). Rend l'autorisation."""
    a = GR.Autorisation(texte, racine)
    piece = os.path.join(os.path.abspath(racine), CHEMIN_PIECE_DE_CONTROLE)
    GR.verifier_scelle(piece)
    with open(piece, encoding="utf-8") as fh:
        contenu = fh.read()
    if a.commit not in contenu:
        raise ArretProgramme("la pièce de contrôle de la mère ne porte pas le commit du code de la pièce d'autorisation : arrêt")
    if empreinte_du_programme() not in contenu:
        raise ArretProgramme("la pièce de contrôle de la mère ne porte pas l'empreinte de ce programme : arrêt")
    return a


def _json(o):
    if hasattr(o, "tolist"):
        return o.tolist()
    raise TypeError(f"valeur non sérialisable : {type(o).__name__}")


def _ecrire_scelle(chemin, texte):
    octets = texte.encode("utf-8")
    with open(chemin, "xb") as fh:
        fh.write(octets)
    sha = hashlib.sha256(octets).hexdigest()
    with open(chemin + ".sha256", "x", encoding="ascii") as fh:
        fh.write(f"{sha}  {os.path.basename(chemin)}\n")
    return sha


def _ecrire_json(chemin, objet):
    return _ecrire_scelle(chemin, json.dumps(objet, ensure_ascii=False, sort_keys=True, indent=1, default=_json) + "\n")


def _clore(dossier, etape, couche, graines, commit, fichiers_geles, configuration, issue):
    """Le manifeste d'une étape (règle R9), scellé ; rend son empreinte."""
    conf = {"etape": etape, "couche": couche, "programme_sha256": empreinte_du_programme(), "issue": issue, **configuration}
    return TI.ecrire_manifeste(os.path.join(dossier, "manifeste.json"), conf, graines, commit, fichiers_geles)


def _arreter(dossier, etape, couche, graines, commit, fichiers_geles, configuration, e):
    """Un arrêt nommé : sa cause (et le rapport qui lui est joint, s'il y en a un) écrite et scellée, le manifeste de l'étape
    « arrêt », puis l'arrêt du programme ; les étapes suivantes ne se jouent pas."""
    _ecrire_scelle(os.path.join(dossier, "arret.txt"), f"{type(e).__name__} : {e}\n")
    if getattr(e, "rapport", None) is not None:
        _ecrire_json(os.path.join(dossier, "rapport-joint-a-l-arret.json"), e.rapport)
    _clore(dossier, etape, couche, graines, commit, fichiers_geles, configuration, "arrêt")
    raise ArretProgramme(f"étape {etape} arrêtée (liste d'arrêt) : {type(e).__name__} : {e}") from e


def lancer(texte, racine, copie_organisme, dossier, couche=None, **reduit):
    """Les étapes 3, 4, 5 et 6, dans cet ordre. `couche` (« essai-de-forme » seulement, une pour toutes les étapes) et les
    tailles réduites (`TAILLES_DES_ESSAIS`) ne servent qu'aux essais ; par défaut, les couches des étapes et les valeurs gelées
    du code v6. Rend {"dossier", "frequences", "reglages", "manifestes"}."""
    if couche is not None and couche != COUCHE_DES_ESSAIS:
        raise ArretProgramme(f"couche {couche!r} interdite : les couches des étapes {sorted(set(COUCHES_DES_ETAPES.values()))} "
                             f"sont fixées, et seule {COUCHE_DES_ESSAIS!r} est permise aux essais : arrêt avant tout geste")
    inconnues = sorted(set(reduit) - set(TAILLES_DES_ESSAIS))
    if inconnues:
        raise ArretProgramme(f"paramètres inconnus : {inconnues} : arrêt avant tout geste")
    if couche is None and reduit:
        raise ArretProgramme("sous les couches des étapes, aucune taille réduite : arrêt avant tout geste")
    if os.path.exists(dossier):
        raise ArretProgramme(f"dossier déjà présent : {dossier} (un dossier neuf est exigé) : arrêt avant tout geste")
    couches = {e: (couche or c) for e, c in COUCHES_DES_ETAPES.items()}
    a = verifier_pieces(texte, racine)
    commit = a.commit
    g4 = GR.Graines(K.RACINE_GRAINES, autorisation=a)
    organisme = OR.EtageOrganisme(copie_organisme, g4.e(couche=couches["4"], famille="organisme", role="racine"),
                                  TACHE_DE_L_ORGANISME)
    os.makedirs(dossier)
    manifestes = {}

    # étape 3 — audit du générateur
    d3 = os.path.join(dossier, "etape-3")
    os.makedirs(d3)
    g3 = GR.Graines(K.RACINE_GRAINES, autorisation=a)
    conf3 = {"doses": list(K.DOSES), "suites_par_dose": reduit.get("suites_par_dose", K.SUITES_AUDIT_PAR_DOSE),
             "permutations": reduit.get("permutations", K.PERMUTATIONS_AUDIT)}
    try:
        rapport = MO.audit_du_generateur(g3, K.DOSES, conf3["suites_par_dose"], conf3["permutations"], couches["3"])
    except ARRETS["3"] as e:
        _arreter(d3, "3", couches["3"], g3, commit, {}, conf3, e)
    _ecrire_json(os.path.join(d3, "rapport-audit-du-generateur.json"), rapport)
    manifestes["3"] = _clore(d3, "3", couches["3"], g3, commit, {}, conf3, "tenue")

    # étape 4 — couche mécanique, fréquences M12, gardes 17 et 27, S8 (i)
    d4 = os.path.join(dossier, "etape-4")
    os.makedirs(d4)
    kw4 = {k: reduit[c] for k, c in (("doses", "doses_etape_4"), ("proposeurs", "proposeurs"), ("sources", "sources_etape_4"),
                                      ("sous_ensemble", "sous_ensemble")) if c in reduit}
    conf4 = {"parametres": kw4 or "valeurs gelées du code v6", "tache_de_l_organisme": TACHE_DE_L_ORGANISME,
             "manifeste_de_l_etape_3_sha256": manifestes["3"]}
    try:
        r4 = EP.lancer_etape_4(g4, couches["4"], os.path.join(d4, "couche-mecanique"), organisme=organisme, **kw4)
    except ARRETS["4"] as e:
        _arreter(d4, "4", couches["4"], g4, commit, {}, conf4, e)
    jeu = r4["jeu_de_la_garde_27"]
    _ecrire_json(os.path.join(d4, "resultat-etape-4.json"),
                 {"frequences": r4["frequences"], "comptes": r4["comptes"], "garde_17": r4["garde_17"],
                  "jeu_de_la_garde_27": {"dose": jeu["dose"], "sources": jeu["sources"], "proposeur": jeu["proposeur"]}})
    manifestes["4"] = _clore(d4, "4", couches["4"], g4, commit, {}, conf4, "tenue")

    # étape 5 — gel par programme du fichier des fréquences, puis relecture sous contrôle de son empreinte
    d5 = os.path.join(dossier, "etape-5")
    os.makedirs(d5)
    chemin_f = os.path.join(d5, FICHIER_DES_FREQUENCES)
    conf5 = {"manifeste_de_l_etape_4_sha256": manifestes["4"], "couche_de_l_etape_4": couches["4"]}
    g5 = GR.Graines(K.RACINE_GRAINES, autorisation=a)
    sha_f = FR.geler(chemin_f, r4["frequences"], r4["comptes"], conf5)
    try:
        f = FR.lire_gelees(chemin_f, sha_f)
    except FR.ArretFrequences as e:
        _arreter(d5, "5", None, g5, commit, {}, conf5, e)
    manifestes["5"] = _clore(d5, "5", None, g5, commit, {"frequences": sha_f}, conf5, "tenue")

    # étape 6 — étalonnage des réglages et gel de leur fichier, sur les fréquences relues
    d6 = os.path.join(dossier, "etape-6")
    os.makedirs(d6)
    g6 = GR.Graines(K.RACINE_GRAINES, autorisation=a)
    chemin_r = os.path.join(d6, FICHIER_DES_REGLAGES)
    sources6 = reduit.get("sources_etalonnage", K.SOURCES_ETALONNAGE)
    conf6 = {"sources": sources6, "frequences_sha256": sha_f, "manifeste_de_l_etape_5_sha256": manifestes["5"]}
    try:
        _, reglages, sha_r = EP.etape_6(g6, couches["6"], f, sources6, chemin_r, conf6)
    except ARRETS["6"] as e:
        _arreter(d6, "6", couches["6"], g6, commit, {"frequences": sha_f}, conf6, e)
    # version 2 : liste d'arrêt, point 5, lue sur les réglages rendus (le fichier des réglages, déjà gelé, est inscrit)
    causes = liste_d_arret_point_5(reglages)
    if causes:
        _arreter(d6, "6", couches["6"], g6, commit, {"frequences": sha_f}, dict(conf6, reglages_sha256=sha_r),
                 ArretListeDArretPoint5("liste d'arrêt, point 5 : " + " ; ".join(causes)
                                        + " : arrêt, le banc ne sait pas planter l'effet de référence"))
    manifestes["6"] = _clore(d6, "6", couches["6"], g6, commit, {"frequences": sha_f}, dict(conf6, reglages_sha256=sha_r),
                             "tenue")
    return {"dossier": dossier, "frequences": (chemin_f, sha_f), "reglages": (chemin_r, sha_r), "manifestes": manifestes}


def main(arguments):
    if len(arguments) != 4:
        raise SystemExit(__doc__)
    texte, racine, copie_organisme, dossier = arguments
    r = lancer(texte, racine, copie_organisme, dossier)
    for e, sha in sorted(r["manifestes"].items()):
        print(f"étape {e} : manifeste {sha}", flush=True)
    print("fréquences gelées :", *r["frequences"], flush=True)
    print("réglages gelés :", *r["reglages"], flush=True)


if __name__ == "__main__":
    main(sys.argv[1:])
