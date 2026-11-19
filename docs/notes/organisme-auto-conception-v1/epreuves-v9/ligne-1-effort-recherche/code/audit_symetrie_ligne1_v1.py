"""Programme à part de l'audit de symétrie de la ligne 1 (banc A, code v2) — version 1.

Lancé **au geste 8, par l'agent de l'audit de symétrie**, après la course décisive, le rejeu et l'analyse. Il fait deux
calculs, exactement comme les fixe l'addendum 1 de la ligne 1 (version 2, `b5d76973…` ; la version 3, `fb48a8ab…`, ne
change pas ces passages), et rien d'autre :

1. **Complément du choix 5** (addendum, § 2, choix 5, « Complément retenu ») : les aires des traits seuls (identifiant,
   rang de la lignée, numéro au registre du premier essai de l'appel), étiquette d'effet, sous la convention
   « indéterminée comptée non vraie », par classe, avec leur intervalle à 95 % par rééchantillonnage des courses
   d'étalonnage : 1 000 rééchantillons, racine 2026111903, tâche `etalonnage|audit|classe=<classe>`. La dérivation est
   **celle de la porte de l'audit dans le code v2**, parce que le calcul est fait par la fonction même de la porte
   (`etalonnage_ligne1_v2.audit_generateur`), appelée sur les mêmes courses, avec la même racine et la même classe : les deux
   conventions sont lues sur les mêmes rééchantillons. Avant le complément, la porte est recalculée par le même appel sur la
   convention de la porte et comparée, au bit près, à la sortie scellée de l'étalonnage ; tout écart est un refus
   (`RecalculPorteDifferent`). Descriptif, sans porte : il n'arrête rien et ne remplit pas la ligne 0. Un intervalle tout
   entier hors de [0,45 ; 0,55] est nommé, sans autre suite dans le programme (la lecture le dit en tête, addendum, choix 5).
2. **Recoupement de M1-nul** (addendum, § 4.2) : pour les courses de rang 0, 300 et 599 de chaque classe (configuration,
   `audit_symetrie.courses`), M1-nul de chaque bras recalculé à partir des seules décisions de promotion et d'arrêt du
   journal décisif, et comparé à la valeur tirée de la sortie brute. Quatre lectures par bras : (i) journal, décisions
   d'arrêt (`rejouer_journal_ligne1_v2.m1_nul_depuis_journal`, reprise) ; (ii) journal, décisions de promotion (écrite ici) ;
   (iii) sortie brute, fonction de l'analyse (`analyse_ligne1_v2.mesures_course`, reprise) ; (iv) sortie brute, calcul
   direct écrit ici, indépendant de l'analyse (limite du recoupement du code v2 dite à l'addendum, § 4.2). Le programme écrit
   « concordant » ou « désaccord » et le détail du désaccord, **jamais de verdict**, et ne choisit jamais entre le journal et
   la sortie brute.

Empreintes (règle R6 ; mandat) : le préenregistrement (`banc_ligne1_v1.verifier_preenregistrement`) ; la configuration v2
contre l'empreinte de l'addendum, § 5.1 (mode réel) ; chaque fichier du code v2 contre la configuration v2
(`lancer_ligne1_v2.verifier_code_configuration`) et contre le manifeste décisif et la sortie de l'étalonnage ; les fichiers
de l'organisme (garde A1, `banc_ligne1_v1.charger_organisme`) ; le manifeste décisif contre l'empreinte donnée en argument
(celle du registre) ; la sortie de l'étalonnage contre le manifeste décisif ; chaque sortie d'étalonnage lue contre la sortie
scellée de l'étalonnage ; chaque journal et chaque sortie décisive lus contre le manifeste décisif ; chaque fichier contre
son compagnon `.sha256`. Une empreinte qui diffère : refus (`EmpreinteDifferente`), rien n'est calculé ni écrit.

Sorties : un compte rendu scellé (`audit-symetrie-ligne1-v1.json` + `.sha256`) et un manifeste de run scellé
(`manifeste-audit-symetrie-ligne1-v1.json` + `.sha256` ; règle R9 : configuration et empreinte, versions, graines dérivées
par racine et par tâche, commit), à des noms neufs (on n'écrase jamais, R12).

Graines : en mode réel, la seule racine dérivée est 2026111903 (racine de rééchantillonnage), par les tâches de la porte de
l'audit. En mode essai, la seule racine admise est celle des essais, 2026111900 ; toute autre est refusée avant tout calcul.

Aucun réseau (garde A2 installée par `charger_organisme`), aucun modèle, aucune clé, aucune dépense. Ne change aucun
fichier du banc ni du code v2 (import seul). Lancer avec `python3 -B` (`PYTHONDONTWRITEBYTECODE=1`) depuis `code/`.

Développeur : modèle L′.
"""

import argparse
import datetime
import os
import platform
import subprocess
import sys

import numpy as np

import banc_ligne1_v1 as B
import journal_ligne1_v1 as JL
import etalonnage_ligne1_v2 as E
import rejouer_journal_ligne1_v2 as RJ
import analyse_ligne1_v2 as AN
import lancer_ligne1_v2 as LA

VERSION = "audit-symetrie-ligne1-v1"
NOM_COMPTE_RENDU = "audit-symetrie-ligne1-v1.json"
NOM_MANIFESTE = "manifeste-audit-symetrie-ligne1-v1.json"
CONFIGURATION_SHA256 = "81f58ce5ca0a492ef231fa175303a21dfb21383a096fa71911b917923cc34f15"   # addendum v3, § 5.1
RACINE_ESSAIS = 2026111900
RACINE_REECHANTILLONNAGE_REEL = 2026111903
RACINES_DU_PREENREGISTREMENT_HORS_ESSAIS = (2026111901, 2026111902, 2026111903)
TRAITS_SEULS = ("identifiant", "rang_lignee", "premier_essai_appel")
CONVENTION_PORTE = "vraie contre fausse ; indéterminées hors des aires"
CONVENTION_COMPLEMENT = "indéterminée comptée non vraie"
MOT_CONCORDANT, MOT_DESACCORD = "concordant", "désaccord"


class RefusAuditSymetrie(B.ArretBanc):
    """Refus de calculer du programme de l'audit de symétrie (aucun verdict ; retour à la mère)."""


class EmpreinteDifferente(RefusAuditSymetrie):
    """Un fichier lu n'a pas l'empreinte du manifeste scellé qui le cite, ou de son compagnon."""


class RacineRefusee(RefusAuditSymetrie):
    """La racine de rééchantillonnage n'est pas celle que le mode exige."""


class RecalculPorteDifferent(RefusAuditSymetrie):
    """La porte de l'audit recalculée ne rend pas, au bit près, celle de la sortie scellée de l'étalonnage."""


class IncoherenceDesEntrees(RefusAuditSymetrie):
    """Manifeste, sortie de l'étalonnage et configuration ne parlent pas du même run."""


# --- empreintes ---------------------------------------------------------------------------------------------------------------
def verifier_fichier(chemin, attendue, quoi):
    """Le fichier existe, correspond à son compagnon `.sha256` et a l'empreinte `attendue` (celle du manifeste scellé qui
    le cite). Rend l'empreinte ; lève `EmpreinteDifferente` sinon."""
    if not os.path.isfile(chemin):
        raise EmpreinteDifferente(f"{quoi} : {chemin} absent : refus")
    reel = B.sha256_fichier(chemin)
    if not B.verifier_scelle_fichier(chemin):
        raise EmpreinteDifferente(f"{quoi} : {os.path.basename(chemin)} : empreinte {reel} ≠ son compagnon : refus")
    if reel != attendue:
        raise EmpreinteDifferente(f"{quoi} : {os.path.basename(chemin)} : empreinte {reel} ≠ {attendue} (manifeste) : refus")
    return reel


def verifier_mode(mode, config, sha_config):
    """Mode réel : configuration v2 à l'empreinte de l'addendum, racine de rééchantillonnage 2026111903. Mode essai : racine
    de rééchantillonnage 2026111900 (racine des essais) seule. Aucune graine n'est dérivée ici. Rend la racine."""
    racine_r = config["racines"]["reechantillonnage"]
    if mode == "reel":
        if sha_config != CONFIGURATION_SHA256:
            raise EmpreinteDifferente(f"configuration : empreinte {sha_config} ≠ {CONFIGURATION_SHA256} (addendum, § 5.1) : refus")
        if racine_r != RACINE_REECHANTILLONNAGE_REEL:
            raise RacineRefusee(f"mode réel : racine de rééchantillonnage {racine_r} ≠ {RACINE_REECHANTILLONNAGE_REEL} : refus")
    elif mode == "essai":
        if racine_r != RACINE_ESSAIS or racine_r in RACINES_DU_PREENREGISTREMENT_HORS_ESSAIS:
            raise RacineRefusee(f"mode essai : racine {racine_r} ; seule la racine des essais {RACINE_ESSAIS} est admise : refus")
    else:
        raise ValueError(f"mode inconnu : {mode!r}")
    return racine_r


def verifier_coherence(config, sha_config, manifeste, etal, sha_etal, code_sur_disque):
    """Manifeste décisif et sortie de l'étalonnage : même configuration, même code que celui qu'importe ce programme, même
    racine de rééchantillonnage, et la sortie de l'étalonnage est celle que cite le manifeste. Lève
    `IncoherenceDesEntrees` ou `EmpreinteDifferente`."""
    if manifeste.get("configuration_sha256") != sha_config:
        raise IncoherenceDesEntrees("manifeste décisif : configuration différente de celle chargée : refus")
    if etal.get("configuration_sha256") != sha_config:
        raise IncoherenceDesEntrees("sortie de l'étalonnage : configuration différente de celle chargée : refus")
    if (manifeste.get("etalonnage") or {}).get("sha256") != sha_etal:
        raise EmpreinteDifferente("sortie de l'étalonnage : empreinte différente de celle du manifeste décisif : refus")
    if manifeste.get("code") != code_sur_disque:
        raise EmpreinteDifferente("manifeste décisif : code différent de celui qu'importe ce programme : refus")
    if (etal.get("code") or {}).get("fichiers") != code_sur_disque:
        raise EmpreinteDifferente("sortie de l'étalonnage : code différent de celui qu'importe ce programme : refus")
    if (etal.get("racines") or {}).get("reechantillonnage") != config["racines"]["reechantillonnage"]:
        raise IncoherenceDesEntrees("sortie de l'étalonnage : racine de rééchantillonnage différente : refus")
    voulues = config["audit_symetrie"]["courses"]
    if not set(voulues) <= set(manifeste.get("courses", [])):
        raise IncoherenceDesEntrees(f"manifeste décisif : courses {voulues} de l'audit de symétrie absentes : refus")
    return True


def code_sur_disque():
    """Empreintes des fichiers du code v2 qu'importe ce programme (liste `etalonnage_ligne1_v2.FICHIERS_CODE`)."""
    return {n: B.sha256_fichier(os.path.join(B.DOSSIER_CODE, n)) for n in E.FICHIERS_CODE}


# --- 1. complément du choix 5 ---------------------------------------------------------------------------------------------------
def carte_deux_conventions(r, s, lign):
    """Pour une réception `transformee` d'une sortie d'étalonnage : (tuple de la porte, tuple du complément). Le tuple de la
    porte est celui de `etalonnage_ligne1_v2.lire_courses` (effet : 1 vraie, 0 fausse, None indéterminée ou non jugée) ;
    celui du complément ne diffère que pour une carte jugée indéterminée (effet 0 : comptée non vraie). Une carte non jugée
    reste hors de l'étiquette d'effet dans les deux conventions."""
    et = s["jugements"][r["id"]]["verite"]["etiquette"] if r["jugee"] else None
    effet_porte = None if et in (None, "indeterminee") else (1 if et == "vraie" else 0)
    effet_complement = None if et is None else (1 if et == "vraie" else 0)
    base = (s["course"], int(r["empreinte"][:8], 16), r["l"], r["premier_essai_appel"], 1 if lign[r["l"]]["a_effet"] else 0)
    return base + (effet_porte,), base + (effet_complement,), et


def lire_cartes_etalonnage(dossier_courses, n, classes, fichiers_attendus):
    """Lit les sorties scellées des courses d'étalonnage 0..n−1 (empreinte de chacune contre la sortie scellée de
    l'étalonnage et contre son compagnon ; garde A17 refaite) ; rend, par classe, les cartes `transformee` sous les deux
    conventions, dans l'ordre de `lire_courses`, et leurs comptes."""
    out = {k: {"porte": [], "complement": [], "comptes": {"transformee": 0, "jugees": 0, "vraies": 0, "fausses": 0,
                                                          "indeterminees": 0, "non_jugees": 0}} for k in classes}
    lus = {}
    for course in range(n):
        for k in classes:
            nom = f"sortie-c{course:04d}-{k}.json.xz"
            if nom not in fichiers_attendus:
                raise EmpreinteDifferente(f"{nom} absent de la liste scellée de l'étalonnage : refus")
            chemin = os.path.join(dossier_courses, nom)
            lus[nom] = verifier_fichier(chemin, fichiers_attendus[nom], "sortie d'étalonnage")
            s = B.lire_json_xz_verifie(chemin)
            E.verifier_sortie_sans_bras_interdit(s)
            if (s.get("course"), s.get("classe")) != (course, k):
                raise IncoherenceDesEntrees(f"{nom} : course ou classe de la sortie différente de son nom : refus")
            lign = {x["l"]: x for x in s["lignees"]}
            for r in s["receptions"]:
                if r["type"] != "transformee":
                    continue
                p, c, et = carte_deux_conventions(r, s, lign)
                out[k]["porte"].append(p)
                out[k]["complement"].append(c)
                cpt = out[k]["comptes"]
                cpt["transformee"] += 1
                if et is None:
                    cpt["non_jugees"] += 1
                else:
                    cpt["jugees"] += 1
                    cpt[{"vraie": "vraies", "fausse": "fausses", "indeterminee": "indeterminees"}[et]] += 1
    return out, lus


def aires_traits_seuls(audit):
    """Aires des traits seuls, étiquette d'effet, d'une sortie de `audit_generateur` (valeur et intervalle)."""
    return {t: {x: audit["aires"]["effet"][t][x] for x in ("valeur", "borne_basse", "borne_haute")} for t in TRAITS_SEULS}


def complement_choix_5(cartes, n, config, racine_r, classes, audit_scelle):
    """Pour chaque classe : la porte recalculée par `audit_generateur` sur la convention de la porte, comparée au bit près à
    la sortie scellée de l'étalonnage (`RecalculPorteDifferent` sinon) ; puis le complément, par le même appel (mêmes
    courses, même racine, même classe, donc même tâche et mêmes rééchantillons) sur la convention « indéterminée comptée
    non vraie ». Rend le compte rendu, sans porte."""
    plage = config["audit"]["plage"]
    courses = list(range(n))
    out = {}
    for k in classes:
        porte = E.audit_generateur(cartes[k]["porte"], courses, config, racine_r, k)
        scelle = audit_scelle.get(k)
        if scelle is None or JL.canonique(porte) != JL.canonique(scelle):
            raise RecalculPorteDifferent(f"classe {k} : la porte de l'audit recalculée diffère de la sortie scellée de "
                                         "l'étalonnage : les rééchantillons ou les cartes ne sont pas les mêmes : refus")
        comp = E.audit_generateur(cartes[k]["complement"], courses, config, racine_r, k)
        traits = aires_traits_seuls(comp)
        for t, v in traits.items():
            B.exiger_fini([v["valeur"], v["borne_basse"], v["borne_haute"]], f"complément du choix 5, {k} / {t}")
            v["intervalle_tout_entier_hors_plage"] = v["borne_haute"] < plage[0] or v["borne_basse"] > plage[1]
        out[k] = {"comptes": cartes[k]["comptes"], "convention": CONVENTION_COMPLEMENT, "traits_seuls": traits,
                  "porte_recalculee": {"convention": CONVENTION_PORTE, "traits_seuls": aires_traits_seuls(porte),
                                       "egale_a_la_sortie_scellee": True},
                  "tache_des_reechantillons": f"etalonnage|audit|classe={k}",
                  "intervalles_tout_entiers_hors_plage": [t for t, v in traits.items() if v["intervalle_tout_entier_hors_plage"]]}
    return {"racine": racine_r, "reechantillons": config["audit"]["reechantillons"], "plage": plage,
            "percentiles": config["audit"]["percentiles"], "courses": n, "par_classe": out,
            "note": ("descriptif, sans porte : n'arrête rien et ne remplit pas la ligne 0 (addendum 1, § 2, choix 5) ; "
                     "les aires de la régression sur les trois traits ne font pas partie du complément et ne sont pas "
                     "rapportées ; l'étiquette de conception ne dépend pas de la convention")}


# --- 2. recoupement de M1-nul ---------------------------------------------------------------------------------------------------
def _bras_de(partie):
    return partie.split("=", 1)[1] if partie.startswith("bras=") else None


def lignees_sans_effet_du_journal(objets, decisions):
    """Lignées des mondes sans effet, lues dans le journal : la loi du monde d'un jugement est de type « fixe » (même
    lecture que `rejouer_journal_ligne1_v2.m1_nul_depuis_journal`)."""
    lignee_de = {d["sortie"]["identifiant"]: d["entrees"]["lignee"] for d in decisions if d["mecanisme"] == "reception"}
    sans = set()
    for d in decisions:
        if d["mecanisme"] == "jugement" and objets[d["entrees"]["loi_monde"]]["type"] == "fixe":
            sans.add(lignee_de[d["entrees"]["identifiant"]])
    return lignee_de, sans


def m1_nul_depuis_promotions(objets, decisions):
    """M1-nul de chaque bras depuis les seules décisions de promotion du journal (règles e-BH, Bonferroni, seule ; bras c :
    carte choisie promue si la confirmation la promeut) ; lignée d'une carte par sa réception, effet par le type de la loi
    du monde de ses jugements. Rend {bras: (V, R)}."""
    lignee_de, sans = lignees_sans_effet_du_journal(objets, decisions)
    out, choisie = {}, {}
    for d in decisions:
        nom, mec = _bras_de(d["partie"]), d["mecanisme"]
        if nom is None:
            continue
        promues = None
        if mec in ("promotion_e_bh", "promotion_bonferroni", "promotion_seule"):
            promues = list(d["sortie"]["promues"])
        elif mec == "choix_c":
            choisie[nom] = d["sortie"]["choisie"]
            promues = []
        elif mec == "promotion_c":
            promues = [choisie.get(nom)] if d["sortie"]["promue"] else []
        if promues is None:
            continue
        V, R = out.get(nom, (0, 0))
        out[nom] = (V + sum(1 for i in promues if lignee_de.get(i) in sans), R + len(promues))
    return out


def m1_nul_sortie_directe(sortie, nom):
    """M1-nul d'un bras calculé directement sur la sortie brute, sans la fonction de l'analyse : promues de chaque
    génération du bras ; lignée par le jugement ; effet par la liste des lignées. Rend (V, R)."""
    sans = {x["l"] for x in sortie["lignees"] if not x["a_effet"]}
    promues = [i for g in sortie["bras"][nom]["generations"] for i in g["promues"]]
    return sum(1 for i in promues if sortie["jugements"][i]["l"] in sans), len(promues)


def _m1(vr):
    return None if vr is None else (vr[0] / vr[1] if vr[1] else 0.0)


def comparer_bras(nom, journal_arret, journal_promotion, sortie):
    """Quatre lectures de M1-nul d'un bras ; « concordant » si toutes existent et rendent le même (V, R) et le même M1-nul
    (égalité exacte) ; sinon « désaccord » et le détail. Aucun choix entre les lectures."""
    lectures = {"journal_decisions_d_arret": journal_arret.get(nom), "journal_decisions_de_promotion": journal_promotion.get(nom),
                "sortie_brute_fonction_de_l_analyse": None, "sortie_brute_calcul_direct": None}
    m1_analyse = None
    if nom in sortie.get("bras", {}):
        mc = AN.mesures_course(sortie, nom, 0.0)
        lectures["sortie_brute_fonction_de_l_analyse"] = (mc["fausses_nul"], mc["promotions"])
        m1_analyse = mc["M1_nul"]
        lectures["sortie_brute_calcul_direct"] = m1_nul_sortie_directe(sortie, nom)
    valeurs = {k: (None if v is None else {"V": v[0], "R": v[1], "M1_nul": _m1(v)}) for k, v in lectures.items()}
    if m1_analyse is not None:
        valeurs["sortie_brute_fonction_de_l_analyse"]["M1_nul"] = m1_analyse
    detail = [f"{k} : absente" for k, v in valeurs.items() if v is None]
    presentes = {k: v for k, v in valeurs.items() if v is not None}
    if len({(v["V"], v["R"]) for v in presentes.values()}) > 1:
        detail.append("(V, R) différents : " + " ; ".join(f"{k} = ({v['V']}, {v['R']})" for k, v in presentes.items()))
    if len({v["M1_nul"] for v in presentes.values()}) > 1:
        detail.append("M1-nul différents : " + " ; ".join(f"{k} = {v['M1_nul']!r}" for k, v in presentes.items()))
    return {"lectures": valeurs, "mot": MOT_DESACCORD if detail else MOT_CONCORDANT, "detail": detail}


def recouper_course(dossier_courses, course, classe, fichiers_attendus):
    """Recoupement d'une course et d'une classe décisives : journal et sortie brute vérifiés contre le manifeste scellé et
    leurs compagnons ; chaîne du journal vérifiée (`journal_ligne1_v1.lire`) ; M1-nul de chaque bras sous quatre
    lectures. Rend le compte rendu (mot, détail, valeurs)."""
    nj, ns = f"journal-c{course:04d}-{classe}.jsonl.xz", f"sortie-c{course:04d}-{classe}.json.xz"
    lus = {}
    for nom in (nj, ns):
        if nom not in fichiers_attendus:
            raise EmpreinteDifferente(f"{nom} absent du manifeste décisif : refus")
        lus[nom] = verifier_fichier(os.path.join(dossier_courses, nom), fichiers_attendus[nom]["sha256"], "course décisive")
    try:
        entete, objets, decisions = JL.lire(os.path.join(dossier_courses, nj))
    except JL.JournalRompu as e:
        raise EmpreinteDifferente(f"{nj} : {e} : refus") from e
    sortie = B.lire_json_xz_verifie(os.path.join(dossier_courses, ns))
    detail = []
    if (entete.get("course"), entete.get("classe")) != (course, classe):
        detail.append(f"en-tête du journal : course {entete.get('course')}, classe {entete.get('classe')}")
    if (sortie.get("course"), sortie.get("classe")) != (course, classe):
        detail.append(f"sortie brute : course {sortie.get('course')}, classe {sortie.get('classe')}")
    arret = RJ.m1_nul_depuis_journal(objets, decisions)
    promotion = m1_nul_depuis_promotions(objets, decisions)
    noms = sorted(set(arret) | set(promotion) | set(sortie.get("bras", {})))
    bras = {nom: comparer_bras(nom, arret, promotion, sortie) for nom in noms}
    for nom, b in bras.items():
        detail += [f"bras {nom} : {x}" for x in b["detail"]]
    return {"course": course, "classe": classe, "fichiers": lus, "bras": bras,
            "mot": MOT_DESACCORD if detail else MOT_CONCORDANT, "detail": detail}


def recoupement_m1_nul(dossier_courses, courses, classes, fichiers_attendus):
    par_course = [recouper_course(dossier_courses, c, k, fichiers_attendus) for c in courses for k in classes]
    desaccords = [{"course": r["course"], "classe": r["classe"], "detail": r["detail"]} for r in par_course
                  if r["mot"] == MOT_DESACCORD]
    return {"courses": list(courses), "classes": list(classes), "mot": MOT_DESACCORD if desaccords else MOT_CONCORDANT,
            "desaccords": desaccords, "par_course": par_course,
            "note": ("aucun verdict ; aucun choix entre le journal et la sortie brute ; tout désaccord va à Lazar par la "
                     "mère (addendum 1, § 4.2)")}


# --- graines consignées (R9) ------------------------------------------------------------------------------------------------------
class GrainesConsignees(B.Graines):
    """Même dérivation que `banc_ligne1_v1.GRAINES` (graine de tâche de l'organisme), qui consigne en plus chaque (racine,
    tâche, graine) dérivée pendant ce run ; posée à la place de `B.GRAINES` le temps du calcul."""

    def __init__(self, premieres):
        super().__init__()
        self.premieres = premieres
        self.derivees = []

    def __call__(self, racine, tache):
        g = super().__call__(racine, tache)
        if (racine, tache, g) not in self.derivees:
            self.derivees.append((racine, tache, g))
        return g


# --- run entier -----------------------------------------------------------------------------------------------------------------
def etat_depot():
    """Commit du dépôt du code et état de ce programme dans git (consignés, sans refus)."""
    def git(*args):
        r = subprocess.run(["git", "-C", B.DOSSIER_CODE, *args], capture_output=True, text=True)
        return r.stdout.strip() if r.returncode == 0 else None
    moi = os.path.abspath(__file__)
    return {"commit": git("rev-parse", "HEAD"), "programme_commis_et_propre": git("status", "--porcelain", "--", moi) == "",
            "programme_suivi": bool(git("ls-files", "--", moi))}


def executer(mode, config, sha_config, chemin_manifeste, manifeste_sha256, vers, chemin_etalonnage=None, prereg=None):
    """Le run entier, sur un organisme déjà chargé (A1, A2) : vérifications, complément du choix 5, recoupement de M1-nul ;
    écrit le compte rendu et le manifeste de run, scellés, dans `vers` (noms neufs). Rend (chemin du compte rendu, chemin du
    manifeste)."""
    if not B.ORGANISME:
        raise RefusAuditSymetrie("organisme non chargé (gardes A1 et A2) : refus")
    debut = B.horodatage()
    racine_r = verifier_mode(mode, config, sha_config)
    code = code_sur_disque()
    lus = {}
    lus[os.path.abspath(chemin_manifeste)] = verifier_fichier(chemin_manifeste, manifeste_sha256, "manifeste décisif")
    manifeste = B.lire_json_verifie(chemin_manifeste)
    chemin_etal = chemin_etalonnage or manifeste["etalonnage"]["chemin"]
    sha_etal = verifier_fichier(chemin_etal, manifeste["etalonnage"]["sha256"], "sortie de l'étalonnage")
    lus[os.path.abspath(chemin_etal)] = sha_etal
    etal = B.lire_json_verifie(chemin_etal)
    E.verifier_sortie_sans_bras_interdit(etal)
    verifier_coherence(config, sha_config, manifeste, etal, sha_etal, code)
    classes = tuple(config["proposeurs"]["engagements_par_appel"])
    for chemin in (os.path.join(vers, NOM_COMPTE_RENDU), os.path.join(vers, NOM_MANIFESTE)):
        if os.path.exists(chemin):
            raise FileExistsError(f"{chemin} déjà présent : on n'écrase jamais (R12)")
    # 2. recoupement (aucune graine)
    dossier_decisif = os.path.join(os.path.dirname(os.path.abspath(chemin_manifeste)), "courses")
    rec = recoupement_m1_nul(dossier_decisif, config["audit_symetrie"]["courses"], classes, manifeste["fichiers"])
    for r in rec["par_course"]:
        lus.update({os.path.join(dossier_decisif, n): s for n, s in r["fichiers"].items()})
    # 1. complément du choix 5 (racine de rééchantillonnage seule)
    n = etal["courses"]["par_classe"]
    dossier_etal = os.path.join(os.path.dirname(os.path.abspath(chemin_etal)), etal["courses"]["dossier"])
    cartes, lus_e = lire_cartes_etalonnage(dossier_etal, n, classes, etal["courses"]["fichiers"])
    lus.update({os.path.join(dossier_etal, k): v for k, v in lus_e.items()})
    ancien = B.GRAINES
    consigne = GrainesConsignees(ancien.premieres)
    B.GRAINES = consigne
    try:
        comp = complement_choix_5(cartes, n, config, racine_r, classes, etal.get("audit_generateur", {}))
    finally:
        B.GRAINES = ancien
    racines_derivees = sorted({r for r, _, _ in consigne.derivees})
    if mode == "essai" and set(racines_derivees) - {RACINE_ESSAIS}:
        raise RacineRefusee(f"mode essai : racine(s) {racines_derivees} dérivée(s) : refus")
    if mode == "reel" and set(racines_derivees) - {RACINE_REECHANTILLONNAGE_REEL}:
        raise RacineRefusee(f"mode réel : racine(s) {racines_derivees} dérivée(s) hors de la racine de rééchantillonnage : refus")
    compte_rendu = {"version": VERSION, "mode": mode, "signature": "développeur, modèle L′ (programme)",
                    "complement_choix_5": comp, "recoupement_m1_nul": rec,
                    "entrees": {"manifeste_decisif": {"chemin": os.path.abspath(chemin_manifeste), "sha256": lus[os.path.abspath(chemin_manifeste)]},
                                "sortie_etalonnage": {"chemin": os.path.abspath(chemin_etal), "sha256": sha_etal}},
                    "ce_que_le_programme_ne_fait_pas": ("aucun verdict, aucune ligne de la table, aucun arrêt de la lecture ; "
                                                        "aucun choix entre le journal et la sortie brute")}
    os.makedirs(vers, exist_ok=True)
    chemin_cr = os.path.join(vers, NOM_COMPTE_RENDU)
    sha_cr = B.ecrire_json_scelle(chemin_cr, compte_rendu)
    manifeste_run = {
        "version": VERSION, "mode": mode, "debut": debut, "fin": B.horodatage(),
        "configuration": {"chemin": os.path.abspath(E.CHEMIN_CONFIGURATION), "sha256": sha_config, "valeurs": config},
        "preenregistrement": prereg,
        "programme": {"chemin": os.path.abspath(__file__), "sha256": B.sha256_fichier(os.path.abspath(__file__))},
        "code_v2": code, "depot": etat_depot(),
        "organisme": {"fichiers": B.ORGANISME.get("fichiers"), "modules_charges": B.ORGANISME.get("modules_charges")},
        "versions": {"python": sys.version, "numpy": np.__version__, "plateforme": platform.platform()},
        "graines": {"methode": "boucle_fermee_v59.graine_de_tache : SeedSequence(racine, spawn_key=(clé de la tâche,))",
                    "derivees": [{"racine": r, "tache": t, "graine": g} for r, t, g in consigne.derivees],
                    "racines_derivees": racines_derivees,
                    "premieres_derivations": {str(k): v for k, v in B.GRAINES.premieres.items()}},
        "fichiers_lus": dict(sorted(lus.items())),
        "compte_rendu": {"chemin": os.path.abspath(chemin_cr), "sha256": sha_cr},
    }
    chemin_m = os.path.join(vers, NOM_MANIFESTE)
    B.ecrire_json_scelle(chemin_m, manifeste_run)
    return chemin_cr, chemin_m


def main(argv=None):
    p = argparse.ArgumentParser(description="Programme à part de l'audit de symétrie de la ligne 1 (geste 8) : complément du "
                                            "choix 5 et recoupement de M1-nul ; aucun verdict.")
    p.add_argument("--manifeste", required=True, help="manifeste-course-decisive-ligne1-v2.json (dossier decisive/)")
    p.add_argument("--manifeste-sha256", required=True, help="empreinte du manifeste décisif portée au registre")
    p.add_argument("--etalonnage", default=None, help="sortie-etalonnage-ligne1-v2.json, si elle a été déplacée "
                                                      "(empreinte toujours vérifiée contre le manifeste)")
    p.add_argument("--organisme", required=True, help="dossier orchestrator/ de l'organisme (lecture seule)")
    p.add_argument("--vers", required=True, help="dossier d'écriture du compte rendu et du manifeste de run (noms neufs)")
    a = p.parse_args(argv)
    prereg = B.verifier_preenregistrement()
    config, sha = B.charger_configuration(E.CHEMIN_CONFIGURATION)
    LA.verifier_code_configuration(config)
    verifier_mode("reel", config, sha)
    B.charger_organisme(a.organisme, config)
    chemin_cr, chemin_m = executer("reel", config, sha, a.manifeste, a.manifeste_sha256, a.vers, a.etalonnage, prereg)
    print(f"écrit : {chemin_cr} ; {chemin_m}")
    print(f"horodatage : {datetime.datetime.now(datetime.timezone.utc).isoformat()}")


if __name__ == "__main__":
    main()
