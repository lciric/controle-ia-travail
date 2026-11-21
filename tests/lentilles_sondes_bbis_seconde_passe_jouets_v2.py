"""Monde miniature de la seconde passe, pour le lanceur `lanceur_seconde_passe_v1` : le monde de la première passe
(`lentilles_sondes_bbis_jouets_v7.monde` : Llama miniature, fausse lentille publique, faux voisin, réseau simulé, sondes
jouets, registres) auquel s'ajoutent de faux fichiers d'ajustement R et S écrits par `torch.save`, la fiche de rangement, la
pièce de `GO-LENTILLES-BBIS-V2`, la fiche du code de la seconde passe et les lignes de la v2 au registre propre.
Aucune donnée du programme, aucun modèle réel, aucune lentille réelle, aucun réseau."""
from __future__ import annotations

import dataclasses
import json
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import torch

import lentilles_sondes_bbis_jouets_v7 as J7
import lentilles_sondes_bbis_seconde_passe_jouets_v1 as J1
from controle_ia.lentilles_sondes_bbis import constantes_v1 as K
from controle_ia.lentilles_sondes_bbis import constantes_v2 as K2
from controle_ia.lentilles_sondes_bbis import lanceur_seconde_passe_v1 as la
from controle_ia.lentilles_sondes_bbis import lanceur_v7 as l7
from controle_ia.lentilles_sondes_bbis import montage_v1 as mo

RUN = "20261123-000000-jouet-seconde-passe"
OUTILS = "docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/outils"
ESSAI_ARCHIVE = (f"{OUTILS}/essai-forme-archive-torch-save-v1.py", f"{OUTILS}/sortie-essai-forme-archive-torch-save-v1.txt")
PIECE_META_S = "pieces-jouets/b-beta-ajustement-S.json"
FICHE_CODE = "registres/code-lentilles-bbis/CODE-LENTILLES-BBIS-V2-jouet.json"
M_JOUET, TEMOINS_ISOTROPES, TEMOINS_PAR_VECTEUR = 240, 120, 60


def sommes(lettre: str, largeur: int = J7.LARGEUR) -> dict:
    """`sums` d'un faux fichier d'ajustement de la taille du Llama miniature : cible `out` de 31 couches pour R, 32 pour S."""
    g = J1.rng(f"bout-en-bout-{lettre}")
    n = K2.N_COUCHES_OUT[lettre]
    base = (3 * np.eye(largeur) if lettre == "R" else 0) + g.standard_normal((n, largeur, largeur))
    out = [torch.from_numpy((base + 0.3 * g.standard_normal((n, largeur, largeur))).astype(np.float32)) for _ in (0, 1)]
    mid = [torch.from_numpy(g.standard_normal((2, largeur, largeur)).astype(np.float32)) for _ in (0, 1)]
    cibles = ("out", "mid") if lettre == "R" else ("mid", "out")
    return {(c, h): (out if c == "out" else mid)[h] for c in cibles for h in (0, 1)}


def ecrire_fiche_code(depot: Path, **plus) -> str:
    """Fiche jouet du code de la seconde passe, aux empreintes réelles du paquet et de l'essai opposable de l'archive."""
    paquet = J7.RACINE / "src" / "controle_ia" / "lentilles_sondes_bbis"
    essai = {}
    for quoi, chemin in zip(("script", "sortie"), ESSAI_ARCHIVE):
        essai[quoi] = {"chemin": chemin, "sha256": J1.ecrire(depot, chemin, (J7.RACINE / chemin).read_bytes())}
    fiche = {"commit": "0" * 40, "contre_lecture": {"chemin": "docs/jouet.md", "sha256": "5" * 64}, "essais": {},
             "addendum_concentration": dict(la.ADDENDUM),
             "code_de_lecture_different_de_la_premiere_passe": list(la.MODULES_DIFFERENTS),
             "essai_de_la_forme_de_l_archive": essai,
             "fichiers": {f"{la.CHEMIN_PAQUET}/{f.name}": J1.sha(f.read_bytes()) for f in sorted(paquet.glob("*.py"))}} | plus
    return J1.ecrire(depot, FICHE_CODE, json.dumps(fiche, indent=1, sort_keys=True))


def ajouter_lignes(propre: Path, lignes: list) -> None:
    with open(propre, "a", encoding="utf-8") as f:
        for c, h, ch, s in lignes:
            f.write(f"| {c} | {h} | {ch} | {s} |\n")


def monde(tmp: Path, monkeypatch, r: str = "p1", s: str = "p1", variante: str = K2.VARIANTE_AJUSTEMENT_SEUL, seconde_course=None,
          plus: tuple = (), premiere_passe: str = "jamais", fiche_plus: dict | None = None, **monde_v7) -> SimpleNamespace:
    """Le monde de la seconde passe. `r`, `s` : « p1 », « p2 », « autre » (verdict « différente ») ou « sans » (lentille sans
    verdict) ; `plus` : lignes de registre ajoutées (noms courts de `jouets_v1.monde` ou lignes entières) ; `premiere_passe` :
    « jamais » (jamais lancée), « entrees » (lancée et non achevée) ou « faite » (jouée ici par `lanceur_v7`, tables inscrites).
    Les empreintes du 18 novembre sont remplacées, pour la durée de l'essai, par celles des faux fichiers (`monkeypatch`)."""
    m = J7.monde(tmp, **monde_v7)
    depot, propre = m.voisin.depot, m.registre_propre
    base = dataclasses.replace(m.reglages, m=M_JOUET, n_temoins_isotrope=TEMOINS_ISOTROPES, n_temoins_par_vecteur=TEMOINS_PAR_VECTEUR)
    m.ctx.reglages = base
    octets = {l: J1.ecrire_ajustement(tmp / "ajustements" / K2.FICHIER_AJUSTEMENT[l], l, sommes(l)) for l in K2.NOS_LENTILLES}
    for l in K2.NOS_LENTILLES:
        monkeypatch.setitem(K2.EMPREINTE_18_NOVEMBRE, l, J1.sha(octets[l]))
    verdicts = {"p1": K2.PALIER_1, "p2": K2.PALIER_2, "autre": K2.DIFFERENTE, "sans": None}
    lentilles = {}
    for l, sorte in (("R", r), ("S", s)):
        e = J1.sha(octets[l])
        lentilles[l] = J1.lentille(l, verdict=verdicts[sorte], taille=len(octets[l]), sha256_avant_envoi=e, sha256_relecture=e)
    fiche = J1.fiche(r=lentilles["R"], s=lentilles["S"], variante=variante, seconde_course=seconde_course,
                     lecture_seconde_course={"chemin": "docs/l2.md", "sha256": "8" * 64, "ligne_d_ensemble": "« partiel », seconde course"})
    fiche |= fiche_plus or {}
    for l in K2.NOS_LENTILLES:
        url = mo.url_fichier(lentilles[l]["depot"], lentilles[l]["revision"], lentilles[l]["chemin"])
        m.transport.fichiers[url] = octets[l]
        m.transport.a_porte.add(url)
    piece_s = J1.ecrire(depot, PIECE_META_S, json.dumps({"fichier": "s.pt", "meta": J1.meta_jouet("S")}))
    H = J1.H
    lignes = [(K2.CLE_SCELLEMENT_V2, H["scellement_v2"], K2.TEXTE_V2, K2.EMPREINTE_TEXTE_V2),
              (K2.CLE_GO_V2, H["go_v2"], J1.PIECE_GO, J1.ecrire(depot, J1.PIECE_GO, f"# Pièce jouet\n\n{J1.N12_SAINE}\n\n{J1.N17_SAINE}\n")),
              (K2.CLE_CODE_V2, H["code_v2"], FICHE_CODE, ecrire_fiche_code(depot)),
              (K2.CLE_RANGEMENT, H["rangement"], J1.FICHE, J1.ecrire(depot, J1.FICHE, json.dumps(fiche, ensure_ascii=False, indent=1)))]
    courtes = {"avertissement": (K2.CLE_AVERTISSEMENT, H["avertissement"], "docs/avertissement-jouet.md", "7" * 64),
               "lecture_seconde_course": (K2.CLE_LECTURE_SECONDE_COURSE, H["lecture_seconde_course"], "docs/lecture-2.md", "8" * 64)}
    lignes += [courtes[p] if isinstance(p, str) else p for p in plus]
    ajouter_lignes(propre, lignes)
    premiere = None
    if premiere_passe == "entrees":
        ajouter_lignes(propre, [(K2.CLE_ENTREES_V1, H["entrees_v1"], "diag/x/entrees-lentilles-bbis.json", "9" * 64)])
    elif premiere_passe == "faite":
        l7.monter(m.ctx)
        rendu = l7.calculer(m.ctx, m.entrees, m.registre_bbis)
        with open(propre, "a", encoding="utf-8") as f:
            f.write("\n".join(rendu["lignes_proposees"]) + "\n")
        premiere = m.ctx.sortie
    r2 = la.Reglages(**{f.name: getattr(base, f.name) for f in dataclasses.fields(l7.Reglages)})
    r2 = dataclasses.replace(
        r2, disque_depart=1, forme_plongements=(J7.VOCABULAIRE, J7.LARGEUR), piece_meta_s=PIECE_META_S, sha256_piece_meta_s=piece_s,
        cibles_corpus=mo.cibles_corpus,      # jouet : l'arbre simulé tient en une page ; la version paginée se branche ici
        lentilles={l: {"n_couches": K2.N_COUCHES_OUT[l], "largeur": J7.LARGEUR, "couches": K.COUCHES, "n_docs": (3, 3), "next_doc": 6,
                       "meta": {c: J1.meta_jouet("R").get(c) for c in K2.CHAMPS_META} if l == "R" else None} for l in K2.NOS_LENTILLES})
    ctx = la.Contexte(tmp / "travail-seconde-passe", tmp / "sortie-seconde-passe", RUN, depot, propre, r2, m.transport,
                      {K.NOM_CLE: J7.FAUSSE_CLE})
    return SimpleNamespace(ctx=ctx, reglages=r2, transport=m.transport, registre_bbis=m.registre_bbis, registre_propre=propre,
                           entrees=m.entrees, depot=depot, premiere_passe=premiere, fiche=fiche, octets=octets, v7=m, tmp=tmp,
                           lentilles=lentilles)


def jouer(m: SimpleNamespace, nettoyage: bool = True) -> SimpleNamespace:
    """Montage, calcul et phrases de la seconde passe sur le monde miniature."""
    montage = la.monter(m.ctx)
    rendu = la.calculer(m.ctx, m.entrees, m.registre_bbis, m.premiere_passe, nettoyage=nettoyage)
    tables = json.loads((m.ctx.sortie / rendu["tables"]["chemin"]).read_text(encoding="utf-8"))
    return SimpleNamespace(montage=json.loads(Path(montage["chemin"]).read_text(encoding="utf-8")), ligne_montage=montage["ligne_proposee"],
                           rendu=rendu, tables=tables, phrases=la.rendre_phrases(tables), monde=m)
