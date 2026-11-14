"""Marche de l'étape B bis sur l'instance (`prereg/T0.7-etape-B-bis-v1.md`, plan, points 1 à 8 et 12 ; « Données gardées »), v1.

Une instance, une marche, dans l'ordre du texte, chaque étape écrite avant la suivante :
0. **gardes d'entrée** (marche réelle) : fiche de `CODE-BBIS` lue au registre propre et scellée, commit du dépôt égal à celui de
   la fiche, empreinte de chaque fichier du code cité égale à celle de la fiche (R11) ; `SCELLEMENT-BBIS` et `GO-BBIS` présentes ;
   aucune clé de B bis dans `registres/scellements-v1.md` ; empreinte du manifeste de 7b égale à la ligne `RUN-CONFIRMATION-T06`
   (lue seulement) ; aucun fichier de la liste « Jamais » sur le disque pour le run de 7b ; variable `BBIS_INSTANCE` posée ;
1. manifeste de la marche (`runs/<run-bbis>/manifeste.json`, préenregistrement scellé cité en marche réelle) ;
2. **relecture** : série O par `t07.repli_recalcul_v1.recalculer` (réutilisé sans modification ; garde d'équivalence) ;
   chargement à état imposé (`etat_impose_v1.charger` : contrôle d'identité à dose 0 et artefact à dose 1) ; **chemin de l'état
   imposé éprouvé** (`eprouver_chemin`) ; séries J_d, J_instruit, A_d, A_T ; `diag/<run-bbis>/relecture-bbis.json` (passes,
   gardes, contrôles d'égalité ; **aucun score**) ;
3. **apprentissage et notation** (`validation_imbriquee_v1.apprendre_source`, cinq sources plafond × deux plis ; garde de débit ;
   contrôle carte-processeur sur le couple tiré d'avance, joué dès qu'il est appris) ; garde de débit déclenchée : arrêt de
   l'apprentissage, `diag/<run-bbis>/arret-debit-bbis.json` (journal des durées ; aucun score), retour « arrêt de débit » ;
4. **fichiers fermés** (`ecrire_fermes`) : `donnees/<run-bbis>/scores-bbis-NNN.npz` (morceaux de moins de 90 Mo, clés
   `<source>__e<k>__<tableau>`), `sondes-bbis.npz` (poids des sondes finales et d'ENC ; deux premières directions en double
   précision), `planchers-bbis-NNN.npz` (directions en simple précision) ; `diag/<run-bbis>/sondes-bbis.json` (réglages retenus,
   empreintes des sondes et des deux premières directions, graines, fichiers et empreintes ; **aucune aire**) ; tous scellés. La
   ligne `SCORES-BBIS` cite `sondes-bbis.json` (qui porte l'empreinte de chaque fichier de scores : déclaré).

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


def _sans_aire(doc) -> None:
    """Garde de la liste d'arrêt : aucune clé d'aire dans un fichier écrit sur l'instance."""
    if isinstance(doc, dict):
        for k, v in doc.items():
            if str(k).startswith("aire"):
                raise GardeArret(f"clé {k!r} : une aire serait écrite sur l'instance : refus (liste d'arrêt)")
            _sans_aire(v)
    elif isinstance(doc, list):
        for v in doc:
            _sans_aire(v)


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
    from .registre_bbis_v1 import REGISTRE_PARTAGE, REGISTRE_PROPRE, exiger_partage_sans_bbis, lire_fiche_code
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
    tete = subprocess.run(["git", "-C", str(racine), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    if tete != fiche["commit"]:
        raise GardeArret(f"commit du dépôt {tete[:12]} ≠ commit de CODE-BBIS {fiche['commit'][:12]} : arrêt (R11)")
    for chemin, sha in fiche["fichiers"].items():
        if rg.sha256_de(racine / chemin) != sha:
            raise GardeArret(f"{chemin} : empreinte ≠ fiche de CODE-BBIS : arrêt (R11)")
    for gabarit in JAMAIS_7B:
        if (racine / gabarit.format(run=run_7b)).exists():
            raise GardeArret(f"{gabarit.format(run=run_7b)} présent sur l'instance (liste « Jamais ») : arrêt")
    return {"fiche": fiche, "lignes": lignes}


def marche(racine: Path, run_7b: str, run_bbis: str, entropie: int, dossier_travail: Path, appareil: str = "cuda",
           essai: dict | None = None) -> dict:
    """La marche complète (points 0 à 4 du docstring). `essai` (jouet seulement ; jamais en marche réelle) : `epoques`,
    `n_plis_internes`, `n_directions`, `n_reetiquetages`, `familles`, `n_controle`, `n_chemin`."""
    from ..harnais.run_harnais_factice import graine_entiere
    from ..manifeste import creer_manifeste, ecrire_resultat, lire_manifeste
    from ..t06.lanceur_v2 import ActivationsDemi
    from ..t06.test_croise import partition_plis
    from ..t07 import repli_recalcul_v1 as rr
    from . import etat_impose_v1 as ei
    from . import validation_imbriquee_v1 as vi
    debut = time.time()
    racine, reelle = Path(racine), essai is None
    essai = dict(essai or {})
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
                     "epoques": epoques, "essai": not reelle}
    dossier = Path(dossier_travail)
    if dossier.exists():
        raise GardeArret(f"{dossier} existe déjà (R12)")
    chemin_m, _ = creer_manifeste(racine, run_bbis, config_marche, list(CLES_FIXES), entropie=int(entropie), decisif=reelle,
                                  prereg=(racine / TEXTE) if reelle else None, autoriser_depot_sale=not reelle,
                                  commande="python -m controle_ia.t07bbis.marche_v1")
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
    controle = vi.ControleCarte(graines, [(n, k) for n in specs for k in (0, 1)],
                                int(essai.get("n_controle", N_ACTIONS_CONTROLE_CARTE)))
    sources = {}
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
    ecrit = ecrire_fermes(racine, run_bbis, sources, graines,
                          {"controle_carte_processeur": controle.resultat, "couple_controle": list(controle.couple),
                           "journal": ctx.debit.journal, "doses": list(doses), "couches": list(couches),
                           "plis": plis, "manifeste": {"chemin": str(chemin_m.relative_to(racine)),
                                                       "sha256": Path(str(chemin_m) + ".sha256").read_text(
                                                           encoding="utf-8").split()[0]},
                           "duree_s": time.time() - debut})
    return {"sondes_bbis": ecrit["chemin"], "sondes_bbis_sha256": ecrit["sha256"],
            "fichiers_scores": ecrit["doc"]["fichiers_scores"], "scores_ecrits": True}


def main(argv=None) -> int:
    """`python -m controle_ia.t07bbis.marche_v1 --racine R --run-7b RUN --run-bbis RUNB --travail DOSSIER` (marche réelle : la
    fiche de `CODE-BBIS` fournit l'entropie ; jamais de mode d'essai en ligne de commande). Codes : 0 scores écrits ; 3 arrêt de
    débit ; 2 refus d'une garde ; 1 autre erreur."""
    ap = argparse.ArgumentParser(description="marche de l'étape B bis (instance)")
    ap.add_argument("--racine", required=True)
    ap.add_argument("--run-7b", required=True)
    ap.add_argument("--run-bbis", required=True)
    ap.add_argument("--travail", required=True)
    a = ap.parse_args(argv)
    try:
        g = gardes_d_entree(Path(a.racine), a.run_7b)
        r = marche(Path(a.racine), a.run_7b, a.run_bbis, g["fiche"]["entropie"], Path(a.travail), "cuda")
    except GardeArret as e:
        print(f"BBIS ARRET : {e}")
        return 2
    print(json.dumps({k: v for k, v in r.items() if k != "journal"}, ensure_ascii=False, default=str))
    return 0 if r.get("scores_ecrits") else 3


__all__ = ["ActivationsDisque", "nom_tableau", "ecrire_fermes", "gardes_d_entree", "marche", "main", "LIMITE_MORCEAU"]

if __name__ == "__main__":
    sys.exit(main())
