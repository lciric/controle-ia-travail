"""Marche de l'étape B bis sur l'instance (`prereg/T0.7-etape-B-bis-v1.md`, plan, points 1 à 8 et 12 ; « Données gardées »), v1.

Une instance, une marche, dans l'ordre du texte, chaque étape écrite avant la suivante :
0. **gardes d'entrée** (marche réelle) : fiche de `CODE-BBIS` lue au registre propre et scellée, commit de la fiche **ancêtre** de
   la tête du dépôt (correction B1 : la tête porte les lignes du registre propre et, sur l'instance, le commit local des entrées),
   empreinte de chaque fichier du code cité égale à celle de la fiche (R11) ; `SCELLEMENT-BBIS` et `GO-BBIS` présentes ;
   aucune clé de B bis dans `registres/scellements-v1.md` ; empreinte du manifeste de 7b égale à la ligne `RUN-CONFIRMATION-T06`
   (lue seulement) ; aucun fichier de la liste « Jamais » sur le disque pour le run de 7b ; variable `BBIS_INSTANCE` posée ;
1. manifeste de la marche (`runs/<run-bbis>/manifeste.json`, préenregistrement scellé cité en marche réelle ; arbre propre exigé
   en marche réelle) ; il cite la tête (commit local des entrées de 7b fait par l'amorce, jamais poussé) et, dans sa
   configuration (`entrees_locales`), son parent (commit du code extrait) et les fichiers ajoutés avec leur identifiant d'objet
   git (vérifiables contre la branche de 7b ; correction M1) ;
2. **relecture** : série O par `t07.repli_recalcul_v1.recalculer` (réutilisé sans modification ; garde d'équivalence) ;
   chargement à état imposé (`etat_impose_v1.charger` : contrôle d'identité à dose 0 et artefact à dose 1) ; **chemin de l'état
   imposé éprouvé** (`eprouver_chemin`) ; séries J_d, J_instruit, A_d, A_T ; `diag/<run-bbis>/relecture-bbis.json` (passes,
   gardes, contrôles d'égalité ; **aucun score**) ;
3. **apprentissage et notation** (`validation_imbriquee_v1.apprendre_source`, cinq sources plafond × deux plis ; garde de débit ;
   contrôle carte-processeur sur le couple tiré d'avance, joué dès que l'apprentissage de ce couple est **complet** : sonde finale,
   directions du plancher, sondes du nul et ENC ; interprétation 19) ; garde de débit déclenchée : arrêt de
   l'apprentissage, `diag/<run-bbis>/arret-debit-bbis.json` (journal des durées ; aucun score), retour « arrêt de débit » ;
4. **fichiers fermés** (`ecrire_fermes`) : `donnees/<run-bbis>/scores-bbis-NNN.npz` (morceaux de moins de 90 Mo, clés
   `<source>__e<k>__<tableau>`), `sondes-bbis.npz` (poids des sondes finales et d'ENC ; deux premières directions en double
   précision), `planchers-bbis-NNN.npz` (directions en simple précision) ; `diag/<run-bbis>/sondes-bbis.json` (réglages retenus,
   empreintes des sondes et des deux premières directions, graines, fichiers et empreintes ; **aucune aire**) ; tous scellés. La
   ligne `SCORES-BBIS` cite `sondes-bbis.json` (qui porte l'empreinte de chaque fichier de scores : déclaré).

**Arrêt écrit** (correction M2) : toute erreur levée après la création du manifeste (relecture, apprentissage sur la carte — une
`RuntimeError` de torch comprise —, contrôle carte-processeur, écriture des fichiers fermés), hors garde de débit, écrit
`diag/<run-bbis>/arret-marche-bbis.json` (étape, type, motif, fin de la pile, journal des durées ; aucun score) et rend le code
fermé 4 ; jamais de chute silencieuse ni de repli.

**Aucune aire, aucun état, aucun résumé de score n'est calculé ni écrit** sur l'instance (les seules aires sont celles de
validation interne, jamais écrites) ; le journal ne porte que des durées. La poussée vers la branche `donnees/t07-etape-b-bis-v1`
est faite par `scripts/amorce_bbis_v1.sh`, jamais par ce module.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from ..scellement import sceller
from .commun_v1 import (EPOQUES, FAMILLES, N_ACTIONS_CONTROLE_CARTE, N_DIRECTIONS, N_PLIS_INTERNES, N_REETIQUETAGES, TEXTE,
                        Graines, cellules, grille, plan_doses_couches, series_imposees)

LIMITE_MORCEAU = 90_000_000
CLES_FIXES = ("bbis/interne/e0", "bbis/interne/e1", "bbis/egalite-carte", "bbis/chemin-impose")
JAMAIS_7B = ("diag/{run}/lecture-sondes-t06.json", "diag/{run}/resume.json")


class ActivationsDisque:
    """Activations relues (une série par dossier `ActivationsDemi`), interface lue par `validation_imbriquee_v1` : `cles(serie,
    condition)` (actions notées, ordre stable), `tache(cle)`, `lire(serie, cle, couche)`, `texte(cle)`, `ids(cle)`, `tokeniseur`."""

    def __init__(self, dossiers: dict, cle_tache: dict, textes: dict, tokeniseur, couche_index: int):
        self.dossiers, self.cle_tache, self._textes, self.tokeniseur = dossiers, cle_tache, textes, tokeniseur
        self._index = {s: sorted(p.stem for p in (Path(d) / f"c{int(couche_index)}").glob("*.npy")) for s, d in dossiers.items()}

    def cles(self, serie: str, condition: str) -> list:
        return [k for k in self._index[serie] if k.split("__t")[0] == condition]

    def tache(self, cle: str) -> str:
        return str(self.cle_tache[cle])

    def lire(self, serie: str, cle: str, couche: int) -> np.ndarray:
        return np.load(Path(self.dossiers[serie]) / f"c{int(couche)}" / f"{cle}.npy").astype(np.float32)

    def texte(self, cle: str) -> str:
        return self._textes[cle]["texte"]

    def ids(self, cle: str) -> list:
        return self._textes[cle]["ids"]


def nom_tableau(source: str, k: int, nom: str) -> str:
    return f"{source}__e{int(k)}__{nom}"


def _morceaux(tableaux: list, prefixe: Path, limite: int = LIMITE_MORCEAU) -> list:
    """Écrit des npz de moins de `limite` octets (une entrée n'est jamais coupée ; une entrée plus grande que la limite arrête) ;
    rend [{fichier, sha256, sources}]."""
    sortie, courant, taille, sources = [], {}, 0, set()

    def vider():
        if not courant:
            return
        chemin = Path(f"{prefixe}-{len(sortie):03d}.npz")
        if chemin.exists():
            raise GardeArret(f"{chemin} existe déjà (R12)")
        np.savez(chemin, **courant)
        if chemin.stat().st_size >= 95_000_000:
            raise GardeArret(f"{chemin} : {chemin.stat().st_size} octets ≥ 95 Mo : arrêt")
        sortie.append({"fichier": chemin, "sha256": sceller(chemin), "sources": sorted(sources)})

    for source, nom, a in tableaux:
        if a.nbytes >= limite:
            raise GardeArret(f"tableau {nom} de {a.nbytes} octets ≥ {limite} : arrêt (une entrée n'est jamais coupée)")
        if taille + a.nbytes > limite and courant:
            vider()
            courant, taille, sources = {}, 0, set()
        courant[nom] = a
        taille += a.nbytes
        sources.add(source)
    vider()
    return sortie


def _sans_aire(doc, _haut: bool = True) -> None:
    """Garde de la liste d'arrêt : aucune clé d'aire dans un fichier écrit sur l'instance. Correction m2 : au premier niveau, les
    clés du dictionnaire `plis` sont des identifiants de tâches de 7b (tâche → pli), jamais des aires ; elles ne sont pas lues
    comme des clés d'aire, et ses valeurs doivent être des plis (entiers 0 ou 1)."""
    if isinstance(doc, dict):
        for k, v in doc.items():
            if str(k).startswith("aire"):
                raise GardeArret(f"clé {k!r} : une aire serait écrite sur l'instance : refus (liste d'arrêt)")
            if _haut and k == "plis" and isinstance(v, dict):
                if any(isinstance(p, bool) or p not in (0, 1) for p in v.values()):
                    raise GardeArret("plis : tâche → pli 0 ou 1 attendu : refus (liste d'arrêt)")
                continue
            _sans_aire(v, False)
    elif isinstance(doc, list):
        for v in doc:
            _sans_aire(v, False)


def ecrire_fermes(racine: Path, run_bbis: str, sources: dict, graines: Graines, extra: dict) -> dict:
    """Fichiers fermés de la marche (docstring du module) ; rend le contenu de `sondes-bbis.json` et son empreinte."""
    racine = Path(racine)
    d = racine / "donnees" / run_bbis
    if d.exists():
        raise GardeArret(f"{d} existe déjà (R12)")
    d.mkdir(parents=True)
    tab, sondes, planchers, meta = [], {}, [], {}
    for (src, k), (_, res) in sorted(sources.items()):
        meta.setdefault(src, {})[f"e{k}"] = res["meta"]
        for nom, a in sorted(res.get("tableaux", {}).items()):
            tab.append((src, nom_tableau(src, k, nom), np.asarray(a)))
        if "sonde" in res:
            s = res["sonde"]
            sondes[nom_tableau(src, k, "sonde_w")] = s.w
            sondes[nom_tableau(src, k, "sonde_b")] = np.array([s.b])
            if s.q is not None:
                sondes[nom_tableau(src, k, "sonde_q")] = s.q
            for j, p in enumerate(res["plancher"][:2]):
                sondes[nom_tableau(src, k, f"direction{j}_w")] = p.w
                sondes[nom_tableau(src, k, f"direction{j}_b")] = np.array([p.b])
                if p.q is not None:
                    sondes[nom_tableau(src, k, f"direction{j}_q")] = p.q
            planchers.append((src, nom_tableau(src, k, "plancher_W"),
                              np.stack([p.w for p in res["plancher"]], axis=1).astype(np.float32)))
            planchers.append((src, nom_tableau(src, k, "plancher_b"), np.array([p.b for p in res["plancher"]], np.float32)))
            if res["plancher"][0].q is not None:
                planchers.append((src, nom_tableau(src, k, "plancher_Q"),
                                  np.stack([p.q for p in res["plancher"]], axis=1).astype(np.float32)))
        if res.get("enc_sonde") is not None:
            e = res["enc_sonde"]
            sondes[nom_tableau(src, k, "enc_w")] = e.w
            sondes[nom_tableau(src, k, "enc_b")] = np.array([e.b])
            if e.q is not None:
                sondes[nom_tableau(src, k, "enc_q")] = e.q
    fs = _morceaux(tab, d / "scores-bbis")
    fp = _morceaux(planchers, d / "planchers-bbis")
    chemin_sondes = d / "sondes-bbis.npz"
    np.savez(chemin_sondes, **sondes)
    rel = lambda p: str(Path(p).relative_to(racine))
    doc = {"run_id": run_bbis, "texte": TEXTE, "sources": meta,
           "fichiers_scores": [{**f, "fichier": rel(f["fichier"])} for f in fs],
           "fichiers_planchers": [{**f, "fichier": rel(f["fichier"])} for f in fp],
           "fichier_sondes": {"fichier": rel(chemin_sondes), "sha256": sceller(chemin_sondes)},
           "graines_derivees": graines.derivees, "sans_aucune_aire": True, **extra}
    _sans_aire(doc)
    g = racine / "diag" / run_bbis
    g.mkdir(parents=True, exist_ok=True)
    chemin = g / "sondes-bbis.json"
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà (R12)")
    chemin.write_text(json.dumps(doc, indent=1, ensure_ascii=False, sort_keys=True, default=str) + "\n", encoding="utf-8")
    return {"doc": doc, "sha256": sceller(chemin), "chemin": rel(chemin)}


def _ligne_partagee(racine: Path, cle: str) -> dict | None:
    reg = Path(racine) / "registres" / "scellements-v1.md"
    if not reg.is_file():
        return None
    for l in reg.read_text(encoding="utf-8").splitlines():
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if c and c[0] == cle and len(c) == 4:
            return {"date": c[1], "chemin": c[2], "sha256": c[3]}
    return None


def gardes_d_entree(racine: Path, run_7b: str) -> dict:
    """Gardes 0 du docstring (marche réelle) ; rend la fiche de `CODE-BBIS` lue (entropie, niveau)."""
    from ..t07 import registre_v1 as rg
    from .lecture_v1 import CLES_PROPRES, RefusLecture, lire_lignes
    from .registre_bbis_v1 import (REGISTRE_PARTAGE, REGISTRE_PROPRE, exiger_ancetre, exiger_partage_sans_bbis,
                                   lire_fiche_code)
    racine = Path(racine)
    if not os.environ.get("BBIS_INSTANCE"):
        raise GardeArret("marche réelle hors de l'instance (BBIS_INSTANCE absente, posée par scripts/amorce_bbis_v1.sh) : refus")
    exiger_partage_sans_bbis(racine / REGISTRE_PARTAGE)
    try:
        tout = lire_lignes(racine / REGISTRE_PROPRE, CLES_PROPRES, ("SCELLEMENT-BBIS", "CODE-BBIS", "GO-BBIS"), propre=True)
        deja = [k for k in ("SCORES-BBIS", "LECTURE-BBIS", "VERDICT-BBIS", "CONJOINTE-BBIS") if k in tout]
        if deja:
            raise RefusLecture(f"ligne(s) {deja} déjà inscrite(s) : la marche est déjà jouée")
        lignes = {k: tout[k] for k in ("SCELLEMENT-BBIS", "CODE-BBIS", "GO-BBIS")}
    except RefusLecture as e:
        raise GardeArret(f"marche : registre propre : {e}") from None
    for k, x in lignes.items():
        rg.sceau_conforme(racine / x["chemin"], x["sha256"])
    fiche = lire_fiche_code(racine / lignes["CODE-BBIS"]["chemin"])
    tete = exiger_ancetre(racine, fiche["commit"], "HEAD")               # B1 : ancêtre de la tête, jamais l'égalité exigée
    for chemin, sha in fiche["fichiers"].items():
        if not (racine / chemin).is_file():
            raise GardeArret(f"{chemin} : fichier du code cité par la fiche de CODE-BBIS absent : arrêt (R11)")
        if rg.sha256_de(racine / chemin) != sha:
            raise GardeArret(f"{chemin} : empreinte ≠ fiche de CODE-BBIS : arrêt (R11)")
    for gabarit in JAMAIS_7B:
        if (racine / gabarit.format(run=run_7b)).exists():
            raise GardeArret(f"{gabarit.format(run=run_7b)} présent sur l'instance (liste « Jamais ») : arrêt")
    return {"fiche": fiche, "lignes": lignes, "tete": tete}


def entrees_locales(racine: Path, exiger: bool) -> dict | None:
    """Correction M1 : tête du dépôt (commit local des entrées fait par `scripts/amorce_bbis_v1.sh`, jamais poussé), son parent
    (commit du code extrait) et les fichiers que ce commit ajoute ou change, avec leur identifiant d'objet git (vérifiables contre
    la branche de 7b sans pousser le commit local). `exiger` (marche réelle) : tête ou parent illisible → arrêt ; sinon `None`."""
    def git(*a):
        r = subprocess.run(["git", "-C", str(racine), *a], capture_output=True, text=True)
        return r.stdout.strip() if r.returncode == 0 else None

    tete = git("rev-parse", "--verify", "-q", "HEAD^{commit}")
    parent = git("rev-parse", "--verify", "-q", "HEAD^1^{commit}")
    if not tete or not parent:
        if exiger:
            raise GardeArret("commit local des entrées (tête) ou son parent illisible (amorce, M1) : arrêt")
        return None
    sortie = git("diff-tree", "-r", "--no-commit-id", "--no-renames", parent, tete)
    if sortie is None:
        raise GardeArret("git diff-tree du commit local des entrées a échoué : arrêt")
    fichiers = {}
    for l in sortie.splitlines():
        meta, _, chemin = l.partition("\t")
        champs = meta.split()
        if len(champs) == 5 and chemin:
            fichiers[chemin] = {"objet": champs[3], "etat": champs[4]}
    return {"commit": tete, "parent": parent, "fichiers": dict(sorted(fichiers.items()))}


def marche(racine: Path, run_7b: str, run_bbis: str, entropie: int, dossier_travail: Path, appareil: str = "cuda",
           essai: dict | None = None, variante: str | None = None, decision: str | None = None) -> dict:
    """La marche complète (points 0 à 4 du docstring). `essai` (jouet seulement ; jamais en marche réelle) : `epoques`,
    `n_plis_internes`, `n_directions`, `n_reetiquetages`, `familles`, `n_controle`, `n_chemin`. `variante` « r1 » (garde de
    débit, nœud de Lazar ; `decision` : la ligne du registre des décisions qui la retient, exigée) : famille linéaire seule et 50
    réétiquetages, écrits au manifeste et dans `sondes-bbis.json`."""
    from .commun_v1 import VARIANTES
    if variante not in VARIANTES:
        raise GardeArret(f"variante {variante!r} inconnue : (r1) seulement, sur le mot de Lazar")
    if variante is not None and not (isinstance(decision, str) and decision.startswith("R-")):
        raise GardeArret("variante (r1) sans la ligne de décision de Lazar (R-…) : refus")
    if variante is not None and essai is not None and ("familles" in essai or "n_reetiquetages" in essai):
        raise GardeArret("variante et réglages d'essai des familles ou des réétiquetages à la fois : refus")
    if variante is not None:
        essai_v = dict(essai or {})
        essai_v.update({"familles": VARIANTES[variante]["familles"], "n_reetiquetages": VARIANTES[variante]["n_reetiquetages"]})
    else:
        essai_v = essai
    from ..manifeste import creer_manifeste, ecrire_resultat, lire_manifeste
    debut = time.time()
    racine, reelle = Path(racine), essai is None
    essai = dict(essai_v or {})
    graines = Graines(int(entropie), reelle=reelle)
    m7b, sha_m7b = lire_manifeste(racine / "runs" / run_7b / "manifeste.json")
    if reelle:
        ligne = _ligne_partagee(racine, "RUN-CONFIRMATION-T06")
        if ligne is None or ligne["sha256"] != sha_m7b or ligne["chemin"] != f"runs/{run_7b}/manifeste.json":
            raise GardeArret("manifeste de 7b : empreinte ou chemin ≠ ligne RUN-CONFIRMATION-T06 (R11) : arrêt")
    config = m7b["config"]
    if reelle and config.get("mode") != "reel":
        raise GardeArret("marche réelle sur une course qui n'est pas réelle : arrêt")
    doses, couches = plan_doses_couches(config)
    familles = tuple(essai.get("familles", FAMILLES))
    n_dir = int(essai.get("n_directions", N_DIRECTIONS))
    n_reet = int(essai.get("n_reetiquetages", N_REETIQUETAGES))
    n_int = int(essai.get("n_plis_internes", N_PLIS_INTERNES))
    epoques = int(essai.get("epoques", EPOQUES))
    config_marche = {"texte": TEXTE, "run_7b": run_7b, "manifeste_7b_sha256": sha_m7b, "appareil": appareil,
                     "familles": list(familles), "n_directions": n_dir, "n_reetiquetages": n_reet, "n_plis_internes": n_int,
                     "epoques": epoques, "essai": not reelle, "variante": variante, "decision_variante": decision,
                     "entrees_locales": entrees_locales(racine, exiger=reelle)}
    dossier = Path(dossier_travail)
    if dossier.exists():
        raise GardeArret(f"{dossier} existe déjà (R12)")
    chemin_m, _ = creer_manifeste(racine, run_bbis, config_marche, list(CLES_FIXES), entropie=int(entropie), decisif=reelle,
                                  prereg=(racine / TEXTE) if reelle else None, autoriser_depot_sale=not reelle,
                                  commande="python -m controle_ia.t07bbis.marche_v1")
    etape = {"nom": "relecture", "ctx": None}
    try:
        return _apres_manifeste(racine, run_7b, run_bbis, dossier, chemin_m, m7b, graines, essai, doses, couches, familles,
                                n_dir, n_reet, n_int, epoques, appareil, reelle, variante, decision, debut, etape)
    except Exception as e:                          # M2 : toute erreur (torch compris) devient un arrêt écrit, code fermé 4 ;
        # la garde de débit a son chemin propre dans `_apres_manifeste` (arret-debit-bbis.json, code 3)
        import traceback
        journal = etape["ctx"].debit.journal if etape["ctx"] is not None else None
        pile = traceback.format_exception(type(e), e, e.__traceback__)
        arret = ecrire_resultat(racine, chemin_m, "arret-marche-bbis",
                                {"arret_marche": f"{type(e).__name__}: {e}"[:4000], "etape": etape["nom"],
                                 "type": type(e).__name__, "garde": isinstance(e, GardeArret),
                                 "pile": "".join(pile)[-6000:], "journal": journal, "scores_ecrits": False})
        return {"arret_marche": f"{type(e).__name__}: {e}"[:4000], "etape": etape["nom"],
                "arret": str(arret.relative_to(racine)), "journal": journal, "scores_ecrits": False}


def _apres_manifeste(racine, run_7b, run_bbis, dossier, chemin_m, m7b, graines, essai, doses, couches, familles, n_dir, n_reet,
                     n_int, epoques, appareil, reelle, variante, decision, debut, etape) -> dict:
    """Points 2 à 4 du docstring (relecture, apprentissage et notation, fichiers fermés) ; `etape` est tenu à jour pour l'arrêt
    écrit (M2)."""
    from ..harnais.run_harnais_factice import graine_entiere
    from ..manifeste import ecrire_resultat
    from ..t06.lanceur_v2 import ActivationsDemi
    from ..t06.test_croise import partition_plis
    from ..t07 import repli_recalcul_v1 as rr
    from . import etat_impose_v1 as ei
    from . import validation_imbriquee_v1 as vi
    rapport_o = rr.recalculer(racine, run_7b, dossier / "O")
    ch = ei.charger(racine, run_7b)
    chemin = ei.eprouver_chemin(ch, dossier / "O", graines.rng("bbis/chemin-impose"), n=int(essai.get("n_chemin", 8)))
    passes = []
    for s in series_imposees(doses):
        act = ActivationsDemi(dossier / s["serie"], couches)
        passes.append(ei.relire_serie(ch, s, act.ecrire))
    relecture = {"serie_O": {k: rapport_o[k] for k in ("identite_dose_0", "adaptateurs", "rejeu", "garde_equivalence")},
                 "identite_etat_impose": ch["identite"], "chemin_impose": chemin, "series": passes, "aucun_score": True}
    ecrire_resultat(racine, chemin_m, "relecture-bbis", relecture)
    etape["nom"] = "préparation de l'apprentissage"
    tok = ch["fmt"].tok
    del ch
    with np.load(racine / "donnees" / run_7b / "mesures-t06.npz", allow_pickle=False) as z:
        cle_tache = {str(c): str(t) for c, t in zip(z["cle"], z["tache"])}
        taches_mesures = [str(t) for t in z["tache"]]
    textes = {}
    for l in (racine / "donnees" / run_7b / "textes-actions-t06.jsonl").read_text(encoding="utf-8").splitlines():
        if l.strip():
            x = json.loads(l)
            textes[str(x["cle"])] = x
    dossiers = {"O": dossier / "O", **{s["serie"]: dossier / s["serie"] for s in series_imposees(doses)}}
    acts = ActivationsDisque(dossiers, cle_tache, textes, tok, couches[0])
    plis = partition_plis(taches_mesures, graine_entiere(m7b["graines"]["partition-taches"]))
    taches_triees = sorted(plis)
    specs = cellules(doses)["plafond"]
    total = vi.apprentissages_prevus(len(specs), len(grille(couches, familles)), n_int, n_reet)
    ctx = vi.Contexte(acts, graines, couches, appareil, debit=vi.GardeDebit(total, debut), familles=familles,
                      reelle=reelle, epoques=epoques, n_plis_internes=n_int)
    etape["ctx"] = ctx
    controle = vi.ControleCarte(graines, [(n, k) for n in specs for k in (0, 1)],
                                int(essai.get("n_controle", N_ACTIONS_CONTROLE_CARTE)))
    sources = {}
    etape["nom"] = "apprentissage et notation"
    try:
        for nom, spec in specs.items():
            plan = vi.plan_de_notation(spec["positifs"], doses)
            for k in (0, 1):
                res = vi.apprendre_source(ctx, nom, spec["positifs"], plan, k, plis, taches_triees, n_reet, n_dir)
                sources[(nom, k)] = (spec["positifs"], res)
                controle.apres(ctx, nom, k, spec["positifs"], res, plis)
    except vi.ArretDebit as e:
        arret = ecrire_resultat(racine, chemin_m, "arret-debit-bbis",
                                {"arret_debit": str(e), "journal": ctx.debit.journal, "scores_ecrits": False})
        return {"arret_debit": str(e), "journal": ctx.debit.journal, "arret": str(arret.relative_to(racine)),
                "relecture": f"diag/{run_bbis}/relecture-bbis.json", "scores_ecrits": False}
    if controle.resultat is None:
        raise GardeArret("contrôle carte-processeur non joué (couple tiré absent des sources) : arrêt")
    etape["nom"] = "écriture des fichiers fermés"
    ecrit = ecrire_fermes(racine, run_bbis, sources, graines,
                          {"controle_carte_processeur": controle.resultat, "couple_controle": list(controle.couple),
                           "journal": ctx.debit.journal, "variante": variante, "decision_variante": decision,
                           "doses": list(doses), "couches": list(couches),
                           "plis": plis, "manifeste": {"chemin": str(chemin_m.relative_to(racine)),
                                                       "sha256": Path(str(chemin_m) + ".sha256").read_text(
                                                           encoding="utf-8").split()[0]},
                           "duree_s": time.time() - debut})
    return {"sondes_bbis": ecrit["chemin"], "sondes_bbis_sha256": ecrit["sha256"],
            "fichiers_scores": ecrit["doc"]["fichiers_scores"], "scores_ecrits": True}


def main(argv=None) -> int:
    """`python -m controle_ia.t07bbis.marche_v1 --racine R --run-7b RUN --run-bbis RUNB --travail DOSSIER` (marche réelle : la
    fiche de `CODE-BBIS` fournit l'entropie ; jamais de mode d'essai en ligne de commande). Codes (fermés) : 0 scores écrits ;
    3 arrêt de débit (`arret-debit-bbis.json`) ; 4 arrêt écrit après la création du manifeste (`arret-marche-bbis.json`, M2) ;
    2 refus d'une garde avant le manifeste ; 1 autre erreur avant le manifeste."""
    ap = argparse.ArgumentParser(description="marche de l'étape B bis (instance)")
    ap.add_argument("--racine", required=True)
    ap.add_argument("--run-7b", required=True)
    ap.add_argument("--run-bbis", required=True)
    ap.add_argument("--travail", required=True)
    ap.add_argument("--variante", default=None, choices=["r1"])
    ap.add_argument("--decision", default=None, help="ligne R-… du registre des décisions qui retient la variante (r1)")
    a = ap.parse_args(argv)
    try:
        g = gardes_d_entree(Path(a.racine), a.run_7b)
        r = marche(Path(a.racine), a.run_7b, a.run_bbis, g["fiche"]["entropie"], Path(a.travail), "cuda", variante=a.variante,
                   decision=a.decision)
    except GardeArret as e:
        print(f"BBIS ARRET : {e}")
        return 2
    print(json.dumps({k: v for k, v in r.items() if k != "journal"}, ensure_ascii=False, default=str))
    if r.get("scores_ecrits"):
        return 0
    return 4 if "arret_marche" in r else 3


__all__ = ["ActivationsDisque", "nom_tableau", "ecrire_fermes", "gardes_d_entree", "entrees_locales", "marche", "main",
           "LIMITE_MORCEAU"]

if __name__ == "__main__":
    sys.exit(main())
