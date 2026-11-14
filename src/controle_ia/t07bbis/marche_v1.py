"""Marche de l'étape B bis sur l'instance (`prereg/T0.7-etape-B-bis-v1.md`, plan, points 3 à 8 ; « Données gardées »), v1.

Une instance, une marche, dans l'ordre du texte, chaque étape écrite avant la suivante :
1. manifeste de la marche (`runs/<run-bbis>/manifeste.json`, préenregistrement scellé cité en marche réelle) ; empreinte du
   manifeste de 7b égale à la ligne `RUN-CONFIRMATION-T06` du registre partagé (lu seulement) ;
2. **relecture** : série O par `t07.repli_recalcul_v1.recalculer` (réutilisé sans modification ; garde d'équivalence) ;
   chargement à état imposé (`etat_impose_v1.charger` : contrôle d'identité à dose 0 et artefact à dose 1) ; **chemin de
   l'état imposé éprouvé** (`eprouver_chemin`) ; séries J_d, J_instruit, A_d, A_T ; `diag/<run-bbis>/relecture-bbis.json`
   (passes, gardes, contrôles d'égalité ; **aucun score**) ;
3. **apprentissage et notation** (`validation_imbriquee_v1.apprendre_source`, cinq sources plafond × deux plis ; garde de
   débit) ; contrôle carte-processeur (`controle_a_la_marche`) ;
4. **fichiers fermés** (`ecrire_fermes`) : `donnees/<run-bbis>/scores-bbis-NNN.npz` (morceaux de moins de 90 Mo, clés
   `<source>__e<k>__<tableau>`), `sondes-bbis.npz` (poids des sondes finales et d'ENC ; deux premières directions en double
   précision), `planchers-bbis-NNN.npz` (directions en simple précision) ; `diag/<run-bbis>/sondes-bbis.json` (réglages
   retenus, empreintes des sondes et des deux premières directions, graines, fichiers et empreintes ; **aucune aire**) ; tous
   scellés. La ligne `SCORES-BBIS` cite `sondes-bbis.json` (qui porte l'empreinte de chaque fichier de scores : déclaré).

**Aucune aire, aucun état, aucun résumé de score n'est calculé ni écrit** sur l'instance (les seules aires sont celles de
validation interne, jamais écrites) ; le journal ne porte que des durées. La poussée vers la branche
`donnees/t07-etape-b-bis-v1` est faite par `scripts/lancer_bbis_v1.sh`, jamais par ce module.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from ..scellement import sceller
from .commun_v1 import (N_DIRECTIONS, N_PLIS_INTERNES, N_REETIQUETAGES, TEXTE, FAMILLES, Graines, cellules, grille,
                        plan_doses_couches, series_imposees)

LIMITE_MORCEAU = 90_000_000
CLES_FIXES = ("bbis/interne/e0", "bbis/interne/e1", "bbis/egalite-carte", "bbis/chemin-impose")


class ActivationsDisque:
    """Activations relues (une série par dossier `ActivationsDemi`), interface de `validation_imbriquee_v1.Activations`."""

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


def _morceaux(tableaux: list, prefixe: Path, limite: int = LIMITE_MORCEAU) -> list:
    """Écrit des npz de moins de `limite` octets (une entrée n'est jamais coupée) ; rend [{fichier, sha256, sources}]."""
    sortie, courant, taille, sources = [], {}, 0, set()

    def vider():
        if not courant:
            return
        chemin = Path(f"{prefixe}-{len(sortie):03d}.npz")
        if chemin.exists():
            raise GardeArret(f"{chemin} existe déjà (R12)")
        np.savez(chemin, **courant)
        sortie.append({"fichier": chemin, "sha256": sceller(chemin), "sources": sorted(sources)})

    for source, nom, a in tableaux:
        if taille + a.nbytes > limite and courant:
            vider()
            courant, taille, sources = {}, 0, set()
        courant[nom] = a
        taille += a.nbytes
        sources.add(source)
    vider()
    return sortie


def ecrire_fermes(racine: Path, run_bbis: str, sources: dict, graines: Graines, extra: dict) -> dict:
    """Fichiers fermés de la marche (docstring du module) ; rend le contenu de `sondes-bbis.json`."""
    from .lecture_v1 import nom_tableau
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
            W = np.stack([p.w for p in res["plancher"]], axis=1).astype(np.float32)
            planchers.append((src, nom_tableau(src, k, "plancher_W"), W))
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
           "graines_derivees": graines.derivees, "aucune_aire": True, **extra}
    g = racine / "diag" / run_bbis
    g.mkdir(parents=True, exist_ok=True)
    chemin = g / "sondes-bbis.json"
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà (R12)")
    texte = json.dumps(doc, indent=1, ensure_ascii=False, sort_keys=True, default=str)
    if '"aire' in texte:
        raise GardeArret("sondes-bbis.json porterait une aire : refus (liste d'arrêt)")
    chemin.write_text(texte + "\n", encoding="utf-8")
    doc["sondes_bbis_sha256"] = sceller(chemin)
    return doc


def _empreinte_run_confirmation(racine: Path) -> str | None:
    from ..t07 import registre_v1 as rg
    reg = Path(racine) / "registres" / "scellements-v1.md"
    if not reg.is_file():
        return None
    for l in reg.read_text(encoding="utf-8").splitlines():
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if c and c[0] == rg.RUN_CONFIRMATION_T06 and len(c) == 4:
            return c[3]
    return None


def marche(racine: Path, run_7b: str, run_bbis: str, entropie: int, dossier_travail: Path, appareil: str = "cuda",
           essai: dict | None = None) -> dict:
    """La marche complète (points 1 à 4 du docstring). `essai` (jouet seulement) : `epoques`, `n_plis_internes`,
    `n_directions`, `n_reetiquetages`, `familles`, `n_controle`."""
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
    if reelle and _empreinte_run_confirmation(racine) != sha_m7b:
        raise GardeArret("manifeste de 7b : empreinte ≠ ligne RUN-CONFIRMATION-T06 (R11) : arrêt")
    config = m7b["config"]
    doses, couches = plan_doses_couches(config)
    familles = tuple(essai.get("familles", FAMILLES))
    n_dir = int(essai.get("n_directions", N_DIRECTIONS))
    n_reet = int(essai.get("n_reetiquetages", N_REETIQUETAGES))
    n_int = int(essai.get("n_plis_internes", N_PLIS_INTERNES))
    config_marche = {"texte": TEXTE, "run_7b": run_7b, "manifeste_7b_sha256": sha_m7b, "appareil": appareil,
                     "familles": list(familles), "n_directions": n_dir, "n_reetiquetages": n_reet, "n_plis_internes": n_int,
                     "epoques": int(essai.get("epoques", 300)), "essai": not reelle}
    chemin_m, _ = creer_manifeste(racine, run_bbis, config_marche, list(CLES_FIXES), entropie=int(entropie), decisif=reelle,
                                  prereg=(racine / TEXTE) if reelle else None, autoriser_depot_sale=not reelle,
                                  commande="scripts/amorce_bbis_v1.py")
    dossier = Path(dossier_travail)
    rapport_o = rr.recalculer(racine, run_7b, dossier / "O")
    ch = ei.charger(racine, run_7b)
    chemin = ei.eprouver_chemin(ch, dossier / "O", graines.rng("bbis/chemin-impose"))
    passes = []
    for s in series_imposees(doses):
        act = ActivationsDemi(dossier / s["serie"], couches)
        passes.append(ei.relire_serie(ch, s, act.ecrire))
    relecture = {"serie_O": {k: rapport_o[k] for k in ("identite_dose_0", "adaptateurs", "rejeu", "garde_equivalence")},
                 "identite_etat_impose": ch["identite"], "chemin_impose": chemin, "series": passes, "aucun_score": True}
    ecrire_resultat(racine, chemin_m, "relecture-bbis", relecture)
    tok = ch["fmt"].tok
    del ch
    z = np.load(racine / "donnees" / run_7b / "mesures-t06.npz", allow_pickle=False)
    cle_tache = {str(c): str(t) for c, t in zip(z["cle"], z["tache"])}
    textes = {}
    for l in (racine / "donnees" / run_7b / "textes-actions-t06.jsonl").read_text(encoding="utf-8").splitlines():
        if l.strip():
            x = json.loads(l)
            textes[str(x["cle"])] = x
    dossiers = {"O": dossier / "O", **{s["serie"]: dossier / s["serie"] for s in series_imposees(doses)}}
    acts = ActivationsDisque(dossiers, cle_tache, textes, tok, couches[0])
    plis = partition_plis(list(z["tache"]), graine_entiere(m7b["graines"]["partition-taches"]))
    taches_triees = sorted(plis)
    specs = cellules(doses)["plafond"]
    total = vi.apprentissages_prevus(len(specs), len(grille(couches, familles)), n_int, n_reet)
    ctx = vi.Contexte(acts, graines, couches, appareil, debit=vi.GardeDebit(total, debut), familles=familles,
                      reelle=reelle, epoques=int(essai.get("epoques", 300)), n_plis_internes=n_int)
    sources = {}
    try:
        for nom, spec in specs.items():
            plan = vi.plan_de_notation(nom, spec["positifs"], doses)
            for k in (0, 1):
                sources[(nom, k)] = (spec["positifs"], vi.apprendre_source(ctx, nom, spec["positifs"], plan, k, plis,
                                                                           taches_triees, n_reet, n_dir))
    except vi.ArretDebit as e:
        return {"arret_debit": str(e), "journal": ctx.debit.journal, "relecture": "diag/" + run_bbis + "/relecture-bbis.json",
                "scores_ecrits": False}
    controle = vi.controle_a_la_marche(ctx, sources, plis, n_actions=int(essai.get("n_controle", 256)))
    doc = ecrire_fermes(racine, run_bbis, sources, graines,
                        {"controle_carte_processeur": controle, "journal": ctx.debit.journal,
                         "manifeste": {"chemin": str(chemin_m.relative_to(racine)),
                                       "sha256": Path(str(chemin_m) + ".sha256").read_text(encoding="utf-8").split()[0]},
                         "duree_s": time.time() - debut})
    return {"sondes_bbis": f"diag/{run_bbis}/sondes-bbis.json", "sondes_bbis_sha256": doc["sondes_bbis_sha256"],
            "fichiers_scores": doc["fichiers_scores"], "scores_ecrits": True}


__all__ = ["ActivationsDisque", "ecrire_fermes", "marche", "LIMITE_MORCEAU"]
