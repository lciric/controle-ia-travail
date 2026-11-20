"""Ordre des opérations, gelé (étapes 4 à 9) — l'enchaînement, sans rien lancer de lui-même.

- `plan_des_cases` : les cases des familles A à H de B8, à partir du fichier des réglages ; une cible non atteignable est
  écrite « non atteignable » et ne se tire pas.
- `etape_4` : la couche mécanique (24 sources par dose et par proposeur, réglages de l'étape 4 au milieu des plages), les
  fréquences M12, l'accord avec l'étage de l'organisme sur deux sources par dose et par proposeur, S8 (i). Bras 1 à 3 seuls.
- `etape_4_jeu_de_la_garde_27` (code v4) : à l'étape 4 aussi, le jeu de sources de la garde 27 (B7 bis : bras 1 à 3, puis 4a et
  4b sur les copies scellées de la source étrangère), à la dose `DOSE_JEU_GARDE_27` (0,25) et à elle seule ; le proposeur et le
  nombre de sources sont des paramètres sans défaut de cette fonction.
- `lancer_etape_4` (code v5, préenregistrement v11, « Ce qui demande un code v5 », point 5) : le programme de lancement de
  l'étape 4 ; il joue `etape_4`, puis, dans le même lancement, le jeu de la garde 27 avec le lecteur réglé pour la tenue (τ = 2)
  et trois sources (remarque 3 de l'annexe H, « Version 9 », tranchée par la mère, version 10).
- `etape_6_bis_et_7` : la couche mécanique rejouée aux réglages gelés sous des étiquettes disjointes, puis la garde S8 (ii).
- `etape_8` : les tirages décisifs de toutes les cases, en un seul lancement, aucune case lue avant que toutes soient
  écrites et scellées ; `cases_a_confirmer` et `etape_9` : la règle de C1 et de C4.

Les tailles et la couche de graines sont des paramètres : les essais du code les jouent réduites sous la couche « essai » ; les
valeurs gelées sont les défauts. Les couches « decisif » et « confirmation » exigent une autorisation (module `graines`).
"""

import os

import numpy as np

from . import equivalence as EQ
from . import frequences as FR
from . import mecanique as MC
from . import mondes as MO
from . import proposeurs as P
from .constantes import (DOSE_JEU_GARDE_27, DOSES, DOSES_NON_NULLES, FORCES_GENERALISTE, FORCES_SUIVEUR, FORCE_REFERENCE_SUIVEUR,
                         GRILLE_SOURCES, GRILLE_SOURCES_DOSE_NULLE, PROPOSEUR_JEU_GARDE_27, REGLAGES_ETAPE_4, REPERES_LECTURE,
                         SEUIL_DE_RETRAIT_SUR_10000, SOURCES_COUCHE_MECANIQUE, SOURCES_FAMILLES_GRANDES, SOURCES_JEU_GARDE_27,
                         SOURCES_SOUS_ENSEMBLE_ORGANISME, TAILLES,
                         TAILLE_REFERENCE, TAUX_ECHEC_DECISIF, TAUX_ECHEC_TOUS, TIRAGES_CONFIRMATION, TIRAGES_PAR_CASE)
from .statistique import simuler

PROPOSEURS_DE_L_ETAPE_4 = P.NOMS


class ArretEtapes(RuntimeError):
    pass


def _cle(*x):
    return "|".join(str(v) for v in x)


def plan_des_cases(reglages):
    """`reglages` : {"K": {(dose, taille): K ou None}, "tau": {(dose, taille): τ ou None}, "phi": {force: φ ou None},
    "gamma": {force: γ ou None}} (None : non atteignable). Rend (cases, non_atteignables). Chaque case porte sa famille, son
    proposeur, sa configuration, sa dose, son taux d'échec, sa taille ou sa force, ses bras, sa règle de retrait, son repère,
    le repli, et `tirages` (emboîtés) ou `sources` (écarts sur 200 000 sources)."""
    cases, non = [], []

    def ajouter(c):
        cases.append(c)

    for dose in DOSES_NON_NULLES:
        for taux in TAUX_ECHEC_TOUS:
            ajouter({"famille": "A", "proposeur": "sourd-egal", "config": P.configuration("sourd-egal"), "dose": dose, "taux": taux,
                     "bras": ("1", "2", "3"), "tirages": TIRAGES_PAR_CASE})
    for dose in DOSES_NON_NULLES:
        for nom, reglage in (("lecteur-heritage", "K"), ("lecteur-tenue", "tau")):
            for taille in TAILLES:
                for taux in ((0.0, 0.25, 0.5) if taille == TAILLE_REFERENCE else (0.25,)):
                    x = reglages[reglage].get((dose, taille))
                    c = {"famille": "B", "proposeur": nom, "dose": dose, "taux": taux, "taille": taille,
                         "bras": ("1", "2", "3"), "tirages": TIRAGES_PAR_CASE}
                    if x is None:
                        non.append(dict(c, statut="non atteignable"))
                        continue
                    ajouter(dict(c, config=P.configuration(nom, **{reglage: x})))
        k, tau = reglages["K"].get((dose, TAILLE_REFERENCE)), reglages["tau"].get((dose, TAILLE_REFERENCE))
        if k is not None and tau is not None:
            ajouter({"famille": "B", "proposeur": "lecteur-deux", "config": P.configuration("lecteur-deux", K=k, tau=tau),
                     "dose": dose, "taux": TAUX_ECHEC_DECISIF, "taille": TAILLE_REFERENCE, "bras": ("1", "2", "3"),
                     "tirages": TIRAGES_PAR_CASE})
    for nom in ("sourd-egal", "sourd-paie"):
        for taux in TAUX_ECHEC_TOUS:
            ajouter({"famille": "C", "proposeur": nom, "config": P.configuration(nom), "dose": 0.0, "taux": taux, "bras": ("2", "3"),
                     "tirages": TIRAGES_PAR_CASE})
    phi_ref = reglages["phi"].get(FORCE_REFERENCE_SUIVEUR)
    for force in FORCES_SUIVEUR:
        phi = reglages["phi"].get(force)
        for taux in (TAUX_ECHEC_TOUS if force == FORCE_REFERENCE_SUIVEUR else (TAUX_ECHEC_DECISIF,)):
            c = {"famille": "C", "proposeur": "suiveur", "dose": 0.0, "taux": taux, "force": force, "bras": ("2", "3"),
                 "tirages": TIRAGES_PAR_CASE}
            if phi is None:
                non.append(dict(c, statut="non atteignable"))
            else:
                ajouter(dict(c, config=P.configuration("suiveur", phi=phi)))
    if phi_ref is not None:
        ajouter({"famille": "C", "proposeur": "suiveur-lettre", "config": P.configuration("suiveur-lettre", phi=phi_ref),
                 "dose": 0.0, "taux": TAUX_ECHEC_DECISIF, "bras": ("2", "3"), "tirages": TIRAGES_PAR_CASE})
    for force in FORCES_GENERALISTE:
        g = reglages["gamma"].get(force)
        c = {"famille": "C", "proposeur": "generaliste", "dose": 0.0, "taux": TAUX_ECHEC_DECISIF, "force": force,
             "bras": ("2", "3"), "tirages": TIRAGES_PAR_CASE}
        if g is None:
            non.append(dict(c, statut="non atteignable"))
        else:
            ajouter(dict(c, config=P.configuration("generaliste", gamma=g)))
    k05 = reglages["K"].get((0.5, TAILLE_REFERENCE))
    if k05 is not None:
        ajouter({"famille": "C", "proposeur": "lecteur-heritage", "config": P.configuration("lecteur-heritage", K=k05),
                 "dose": 0.0, "taux": TAUX_ECHEC_DECISIF, "taille": TAILLE_REFERENCE, "bras": ("2", "3"),
                 "tirages": TIRAGES_PAR_CASE})
    for dose in DOSES_NON_NULLES:
        k = reglages["K"].get((dose, TAILLE_REFERENCE))
        if k is not None:
            for mode in ("tirages", "sources"):
                ajouter({"famille": "D", "proposeur": "lecteur-heritage", "config": P.configuration("lecteur-heritage", K=k),
                         "dose": dose, "taux": TAUX_ECHEC_DECISIF, "taille": TAILLE_REFERENCE, "bras": ("1", "2", "3"),
                         "repli": True, mode: TIRAGES_PAR_CASE if mode == "tirages" else SOURCES_FAMILLES_GRANDES})
    for dose in DOSES:
        for retrait in ("v2", "v1"):
            for repere in REPERES_LECTURE:
                ajouter({"famille": "E", "proposeur": "sourd-paie", "config": P.configuration("sourd-paie"), "dose": dose,
                         "taux": TAUX_ECHEC_DECISIF, "bras": ("2", "3"), "retrait": retrait, "repere": repere,
                         "sources": SOURCES_FAMILLES_GRANDES})
    if phi_ref is not None:
        ajouter({"famille": "F", "proposeur": "suiveur-lettre", "config": P.configuration("suiveur-lettre", phi=phi_ref),
                 "dose": 0.25, "taux": TAUX_ECHEC_DECISIF, "bras": ("1", "2", "3"), "tirages": TIRAGES_PAR_CASE})
    for dose in DOSES:
        ajouter({"famille": "G", "proposeur": "copieur", "config": P.configuration("copieur"), "dose": dose,
                 "taux": TAUX_ECHEC_DECISIF, "bras": ("1", "2", "3"), "tirages": TIRAGES_PAR_CASE})
    diag = [("suiveur-lettre", 0.25, {"phi": phi_ref}), ("sourd-paie", 0.25, {})]
    for dose in DOSES_NON_NULLES:
        diag += [("lecteur-heritage", dose, {"K": reglages["K"].get((dose, TAILLE_REFERENCE))}),
                 ("lecteur-tenue", dose, {"tau": reglages["tau"].get((dose, TAILLE_REFERENCE))})]
    for nom, dose, r in diag:
        if any(v is None for v in r.values()):
            non.append({"famille": "H", "proposeur": nom, "dose": dose, "statut": "non atteignable"})
            continue
        for mode in ("tirages", "sources"):
            ajouter({"famille": "H", "proposeur": nom, "config": P.configuration(nom, **r), "dose": dose,
                     "taux": TAUX_ECHEC_DECISIF, "bras": ("1", "2", "3", "4a", "4b"),
                     "taille": TAILLE_REFERENCE if nom.startswith("lecteur") else None,
                     mode: TIRAGES_PAR_CASE if mode == "tirages" else SOURCES_FAMILLES_GRANDES})
    for nom, reglage, forces in (("suiveur", "phi", reglages["phi"]), ("generaliste", "gamma", reglages["gamma"])):
        x = forces.get(FORCE_REFERENCE_SUIVEUR)
        if x is not None:  # point 6, rejoué à la dose 0,5 à la force de référence, sans critère
            ajouter({"famille": "point-6", "proposeur": nom, "config": P.configuration(nom, **{reglage: x}), "dose": 0.5,
                     "taux": TAUX_ECHEC_DECISIF, "force": FORCE_REFERENCE_SUIVEUR, "bras": ("1", "2", "3"),
                     "sources": SOURCES_FAMILLES_GRANDES})
    return cases, non


def cases_de_niveau(cases):
    """Les cases de C1 (famille A : 12 nombres × 2 doses × 3 taux = 72) et de C4 (famille C, les deux sourds : 12 × 2 × 3 = 72)."""
    c1 = [(k, c["dose"], c["taux"]) for c in cases if c["famille"] == "A" for k in GRILLE_SOURCES]
    c4 = [(k, c["proposeur"], c["taux"]) for c in cases if c["famille"] == "C" and c["proposeur"] in ("sourd-egal", "sourd-paie")
          for k in GRILLE_SOURCES_DOSE_NULLE]
    return c1, c4


def etape_4(graines, couche, dossier, doses=DOSES, proposeurs=PROPOSEURS_DE_L_ETAPE_4, sources=SOURCES_COUCHE_MECANIQUE,
            sous_ensemble=SOURCES_SOUS_ENSEMBLE_ORGANISME, organisme=None):
    """La couche mécanique de l'étape 4. `organisme` : un `organisme.EtageOrganisme` (garde 17) ; None : la garde n'est pas
    jouée, c'est dit, et l'issue est « suspendue ». Rend (fréquences, comptes, garde 17)."""
    freqs = MC.Frequences()
    vues = 0
    for nom in proposeurs:
        prop = P.configuration(nom, **REGLAGES_ETAPE_4)
        for dose in doses:
            for s in range(sources):
                org = organisme if (organisme is not None and s < sous_ensemble) else None
                ctx = MC.ContexteSource(graines, dict(couche=couche, famille="etape-4", proposeur=nom, dose=dose, source=s), prop,
                                        dose, TAUX_ECHEC_DECISIF, os.path.join(dossier, nom, str(dose), str(s)), organisme=org)
                out = MC.jouer_source(ctx)
                freqs.fusionner(out["frequences"])
                vues += ctx.tentatives_vues_par_l_organisme
    f = FR.frequences_gelees(freqs.comptes())
    FR.verifier_s8_i(f)
    garde_17 = None if organisme is None else {"tentatives_comparees": vues, "desaccords": 0}
    return f, freqs.comptes(), garde_17


def etape_4_jeu_de_la_garde_27(graines, couche, dossier, prop, sources, famille="etape-4-garde-27"):
    """Code v4 (« Ce qui demande un code v4 », point 5 ; B7 bis ; garde 27) : le jeu de sources de la garde 27 se joue à l'étape
    4, sur la couche mécanique, par cette fonction : `mondes.generer_jeu_avec_etrangeres` (marge face à la source étrangère
    construite) puis `mecanique.jouer_jeu_diagnostic` (bras 1, 2, 3, puis 4a et 4b), à la dose `DOSE_JEU_GARDE_27` = 0,25,
    fixée ici et vérifiée par les deux fonctions, qui arrêtent à toute autre dose ; taux d'échec de 0,25. `prop` (configuration
    du proposeur) et `sources` (au moins deux) : donnés par l'appelant, sans défaut ; le programme de lancement de l'étape 4
    (`lancer_etape_4`, code v5) les fixe au lecteur réglé pour la tenue, τ = 2, et à trois sources (version 10). Les
    contrôles de la garde 27 (registre servi au bras 4a, copie servie au bras 4b, aucun bras du critère ne la reçoit) se font
    en jouant. Rend {"dose", "sources", "proposeur", "suites", "premieres", "secondes"}."""
    if isinstance(sources, bool) or not isinstance(sources, int) or sources < 2:
        raise ArretEtapes(f"garde 27 : au moins deux sources (reçu {sources!r})")
    bases = [dict(couche=couche, famille=famille, proposeur=prop["nom"], dose=DOSE_JEU_GARDE_27, source=k)
             for k in range(sources)]
    suites = MO.generer_jeu_avec_etrangeres(graines, bases, DOSE_JEU_GARDE_27)
    premieres, secondes = MC.jouer_jeu_diagnostic(graines, bases, prop, DOSE_JEU_GARDE_27, TAUX_ECHEC_DECISIF, dossier, suites)
    return {"dose": DOSE_JEU_GARDE_27, "sources": sources, "proposeur": prop["nom"], "suites": suites, "premieres": premieres,
            "secondes": secondes}


def lancer_etape_4(graines, couche, dossier, doses=DOSES, proposeurs=PROPOSEURS_DE_L_ETAPE_4, sources=SOURCES_COUCHE_MECANIQUE,
                   sous_ensemble=SOURCES_SOUS_ENSEMBLE_ORGANISME, organisme=None):
    """Code v5 (« Ce qui demande un code v5 », point 5 ; B7 bis et garde 27, version 10, remarque 3 tranchée par la mère) : le
    programme de lancement de l'étape 4. Dans un même lancement (mêmes `graines`, même `couche`) : d'abord `etape_4` (la couche
    mécanique, bras 1 à 3), puis le jeu de la garde 27 (`etape_4_jeu_de_la_garde_27`), joué par le lecteur réglé pour la tenue,
    au réglage de l'étape 4 que B2 gèle (τ = 2, `REGLAGES_ETAPE_4`), sur trois sources (`SOURCES_JEU_GARDE_27`), à la dose
    0,25. Le proposeur et le nombre de sources du jeu ne sont pas des paramètres. Rend {"frequences", "comptes", "garde_17",
    "jeu_de_la_garde_27"}."""
    f, comptes, garde_17 = etape_4(graines, couche, os.path.join(dossier, "bras-1-a-3"), doses, proposeurs, sources,
                                   sous_ensemble, organisme)
    jeu = etape_4_jeu_de_la_garde_27(graines, couche, os.path.join(dossier, "jeu-de-la-garde-27"),
                                     P.configuration(PROPOSEUR_JEU_GARDE_27, **REGLAGES_ETAPE_4), SOURCES_JEU_GARDE_27)
    return {"frequences": f, "comptes": comptes, "garde_17": garde_17, "jeu_de_la_garde_27": jeu}


def etape_6_bis_et_7(graines, couche, dossier, f, configurations, sources_mecaniques=SOURCES_COUCHE_MECANIQUE,
                     sources_statistiques=20_000, bras=("1", "2", "3")):
    """`configurations` : {(proposeur, dose) : configuration aux réglages gelés}. Rejoue la couche mécanique (étiquettes
    disjointes de l'étape 4 : couche distincte), puis la couche statistique, et applique S8 (ii). Rend le détail."""
    moy, stat = {}, {}
    for (nom, dose), prop in sorted(configurations.items()):
        m1 = {b: [] for b in bras}
        for s in range(sources_mecaniques):
            ctx = MC.ContexteSource(graines, dict(couche=couche, famille="etape-6-bis", proposeur=nom, dose=dose, source=s), prop,
                                    dose, TAUX_ECHEC_DECISIF, os.path.join(dossier, nom, str(dose), str(s)))
            out = MC.jouer_source(ctx, bras)
            for b in bras:
                m1[b].append(out["bras"][b]["mesure"]["M1"])
        base = dict(couche=couche, famille="etape-7", proposeur=nom, dose=dose)
        r = simuler({b: graines.g(**base, bras=b, role="echantillonnage") for b in bras}, graines.g(**base, role="monde"),
                    graines.g(**base, role="source"), prop, dose, TAUX_ECHEC_DECISIF, f, sources_statistiques)
        for b in bras:
            moy[(nom, b, dose)] = (float(np.mean(m1[b])), sources_mecaniques)
            stat[(nom, b, dose)] = r["bras"][b]["M1"]
    return EQ.garde_equivalence(moy, stat, graines.g(couche=couche, famille="etape-7", role="intervalle"))


def cibles_d_etalonnage():
    """B7 : (proposeur, réglage, dose, cible) — K et τ à chaque dose non nulle et à chaque taille ; φ et γ à dose nulle, à
    chaque force (la force est la taille réduite visée du contraste de l'héritage, coût compris)."""
    c = [(nom, r, dose, taille) for dose in DOSES_NON_NULLES for taille in TAILLES
         for nom, r in (("lecteur-heritage", "K"), ("lecteur-tenue", "tau"))]
    c += [("suiveur", "phi", 0.0, force) for force in FORCES_SUIVEUR]
    c += [("generaliste", "gamma", 0.0, force) for force in FORCES_GENERALISTE]
    return c


def jumelles_sans_reglage():
    """Les proposeurs sans réglage, joués à l'étalonnage pour leur seul écart-type entre jumelles, à chaque dose et à chaque taux
    d'échec de leurs familles (A, C, E, G ; le suiveur à la lettre est joué une fois φ connu)."""
    out = [("sourd-egal", dose, taux, ("1", "2", "3"), "v2", None) for dose in DOSES_NON_NULLES for taux in TAUX_ECHEC_TOUS]
    out += [(nom, 0.0, taux, ("2", "3"), "v2", None) for nom in ("sourd-egal", "sourd-paie") for taux in TAUX_ECHEC_TOUS]
    out += [("sourd-paie", dose, TAUX_ECHEC_DECISIF, ("2", "3"), retrait, repere) for dose in DOSES
            for retrait in ("v2", "v1") for repere in REPERES_LECTURE]
    out += [("copieur", dose, TAUX_ECHEC_DECISIF, ("1", "2", "3"), "v2", None) for dose in DOSES]
    return out


def etape_6(graines, couche, f, sources, chemin_reglages=None, configuration=None):
    """Étape 6 : toutes les cibles (dichotomie), les écarts-types des proposeurs sans réglage, ceux des proposeurs réglés aux
    taux 0 et 0,5 à la taille de référence, et le suiveur à la lettre à la valeur de φ de la force de référence. Une cible « non
    convergée » arrête (aucun repli). Rend (lignes, réglages au format de `plan_des_cases`, empreinte du fichier gelé ou None)."""
    from . import etalonnage as ET
    lignes = []
    for nom, r, dose, cible in cibles_d_etalonnage():
        l = ET.etalonner(graines, couche, nom, lambda x, nom=nom, r=r: P.configuration(nom, **{r: x}), r, dose, cible, f, sources)
        if l["statut"] == "non convergé":
            raise ArretEtapes(f"étalonnage non convergé : {nom}, dose {dose}, cible {cible}")
        lignes.append(l)
    reglages = reglages_pour_le_plan(lignes)
    for nom, dose, taux, bras, retrait, repere in jumelles_sans_reglage():
        lignes.append(ET.ecart_type_sans_reglage(graines, couche, nom, P.configuration(nom), dose, taux, f, sources, bras,
                                                 repere or REPERES_LECTURE[1], retrait))
    for dose in DOSES_NON_NULLES:
        for nom, r in (("lecteur-heritage", "K"), ("lecteur-tenue", "tau")):
            x = reglages[r].get((dose, TAILLE_REFERENCE))
            if x is not None:
                for taux in (0.0, 0.5):
                    lignes.append(ET.ecart_type_sans_reglage(graines, couche, nom, P.configuration(nom, **{r: x}), dose, taux, f,
                                                             sources, ("1", "2", "3")))
    phi = reglages["phi"].get(FORCE_REFERENCE_SUIVEUR)
    if phi is not None:
        for taux in (0.0, 0.5):
            lignes.append(ET.ecart_type_sans_reglage(graines, couche, "suiveur", P.configuration("suiveur", phi=phi), 0.0, taux, f,
                                                     sources, ("2", "3")))
        for dose, bras in ((0.0, ("2", "3")), (0.25, ("1", "2", "3"))):
            lignes.append(ET.ecart_type_sans_reglage(graines, couche, "suiveur-lettre", P.configuration("suiveur-lettre", phi=phi),
                                                     dose, TAUX_ECHEC_DECISIF, f, sources, bras))
    sha = ET.geler_reglages(chemin_reglages, lignes, configuration or {}) if chemin_reglages else None
    return lignes, reglages, sha


def reglages_pour_le_plan(lignes):
    """Du fichier des réglages au format de `plan_des_cases` (None : non atteignable)."""
    out = {"K": {}, "tau": {}, "phi": {}, "gamma": {}}
    for l in lignes:
        r = l.get("nom_du_reglage")
        if r is None:
            continue
        cle = (l["dose"], l["cible"]) if r in ("K", "tau") else l["cible"]
        out[r][cle] = l["reglage"] if l["atteignable"] else None
    return out


def cases_a_confirmer(comptes_c1, comptes_c4):
    """C1 et C4 : les cases dont le taux observé dépasse 0,05 (plus de 500 rejets sur 10 000), à retirer une fois sur 100 000
    tirages de graines neuves (couche « confirmation »)."""
    return sorted([("C1",) + tuple(k) for k, v in comptes_c1.items() if v > SEUIL_DE_RETRAIT_SUR_10000] +
                  [("C4",) + tuple(k) for k, v in comptes_c4.items() if v > SEUIL_DE_RETRAIT_SUR_10000], key=str)


TIRAGES_DE_CONFIRMATION = TIRAGES_CONFIRMATION
