"""Jouets des essais de la seconde passe (texte de lecture v2, « Code neuf ») : registre propre jouet, pièce jouet de
`GO-LENTILLES-BBIS-V2`, fiche de rangement jouet, faux fichiers d'ajustement écrits par `torch.save` (petites dimensions, mêmes
clés), faux transport. Aucune donnée, aucun modèle, aucune lentille réelle, aucun réseau.
Graines : `numpy.random.SeedSequence`, clés `lentilles-bbis-v2/essai/<garde>`."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

import numpy as np

from controle_ia.lentilles_sondes_bbis import constantes_v1 as K
from controle_ia.lentilles_sondes_bbis import constantes_v2 as K2
from controle_ia.lentilles_sondes_bbis import nos_lentilles_v1 as nl
from controle_ia.lentilles_sondes_bbis import nuls_v1 as nu

RACINE = Path(__file__).resolve().parents[1]
REGISTRE = "registres/lecture-sondes-bbis-par-lentilles-v1.md"
PIECE_GO = "registres/go-extraits/GO-LENTILLES-BBIS-V2-jouet.md"
FICHE = "docs/fiche-de-rangement-jouet-v1.json"
H = {"absence": "2026-11-18T19:05:35Z", "addendum": "2026-11-19T16:35:35Z", "accord": "2026-11-20T05:34:13Z",
     "scellement_v2": "2026-11-20T10:39:17Z", "go_v2": "2026-11-20T10:39:19Z", "code_v1": "2026-11-21T16:02:40Z",
     "code_v2": "2026-11-22T08:00:00Z", "rangement": "2026-11-22T09:00:00Z", "avertissement": "2026-11-22T10:00:00Z",
     "lecture_seconde_course": "2026-11-22T11:00:00Z", "noeud": "2026-11-22T12:00:00Z", "entrees_v1": "2026-11-22T13:00:00Z",
     "tables_v1": "2026-11-22T14:00:00Z"}
N12_SAINE = f"N12 : option (a) ; ligne d'accord GO-2026-11-20-18, {H['accord']}"
N17_SAINE = f"N17 : option (a) au premier palier ; option (a) au deuxième palier ; ligne d'accord GO-2026-11-20-18, {H['accord']}"
D, COUCHES_JOUET = 12, (1, 2, 3)        # largeur jouet ; couches jouets à la place de 7, 15 et 23


def rng(garde: str) -> np.random.Generator:
    return nu.Graines().rng(f"lentilles-bbis-v2/essai/{garde}")


def sha(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def ecrire(racine: Path, chemin: str, contenu) -> str:
    """Écrit un fichier sous `racine` (texte ou octets) et rend son SHA-256."""
    p = Path(racine) / chemin
    p.parent.mkdir(parents=True, exist_ok=True)
    octets = contenu.encode("utf-8") if isinstance(contenu, str) else contenu
    p.write_bytes(octets)
    return sha(octets)


# --- fiche de rangement jouet -----------------------------------------------------------------------------------------------------------
def sortie_du_programme(lettre: str, declencheurs=(), **plus) -> dict:
    s = {"chemin": f"diag/jouet/comparaison-{lettre}.json", "sha256": "a" * 64, "critere": "critère d'identité (v5 à l'écriture)",
         "ecart_max_abs_diffs_float64": 3.5e-5, "ecart_max_abs_diffs": 4.0e-5, "declencheurs": list(declencheurs),
         "audit_requis": bool(declencheurs)}
    if lettre == "R":
        s["series_export_R_sans_critere"] = {"npR_notre_R": {"ecart_max_abs": 1.5e-4, "ref_min": 0.069, "ref_max": 0.9},
                                             "identite_notre_R": {"ecart_max_abs": 2.5e-4, "ref_min": 0.1, "ref_max": 1.2}}
        s["matrices_moities_egales"] = {"couches_egales": 0, "couches_ref": 31}
    return s | plus


AUDIT = {"chemin": "docs/audit-jouet.md", "sha256": "b" * 64, "controles_manques": 0}
VERDICT_SCELLE = {"chemin": "docs/verdict-identite-jouet.md", "sha256": "c" * 64}


def lentille(lettre: str, verdict: str | None = K2.PALIER_1, audit=AUDIT, declencheurs=None, **plus) -> dict:
    """Entrée d'une lentille dans la fiche jouet. Au premier palier, l'empreinte est celle du 18 novembre."""
    premier = isinstance(verdict, str) and verdict.startswith(K2.PALIER_1)
    if declencheurs is None:
        declencheurs = ["(i) palier 1 obtenu"] if premier else []
    empreinte = K2.EMPREINTE_18_NOVEMBRE[lettre] if premier else ("d" if lettre == "R" else "e") * 64
    l = {"depot": "compte/rangement-jouet", "revision": "0123456789abcdef0123456789abcdef01234567",
         "chemin": K2.FICHIER_AJUSTEMENT[lettre], "taille": K2.TAILLE_18_NOVEMBRE[lettre] if premier else 4321,
         "sha256_avant_envoi": empreinte, "sha256_relecture": empreinte, "verdict_identite": verdict, "reprise": False,
         "verdict_scelle": dict(VERDICT_SCELLE), "sortie_du_programme": sortie_du_programme(lettre, declencheurs),
         "audit": copy.deepcopy(audit),
         "diffs_out": {"ajustement_du_18_novembre": {"7": 0.0652, "15": 0.0295, "23": 0.0143},
                       "reajustement": {"7": 0.0652, "15": 0.0295, "23": 0.0143}},
         "seconde_course_par_couche": {str(c): {"limite": K2.AUCUNE_LIMITE, "ecartee": False} for c in K.COUCHES}}
    if lettre == "R":
        l["phrase_du_declencheur_vi"] = K2.AUCUNE
    return l | plus


def fiche(r: dict | None = None, s: dict | None = None, variante: str = K2.VARIANTE_AJUSTEMENT_SEUL, seconde_course=None,
          **plus) -> dict:
    f = {"critere_identite": {"chemin": K2.CRITERE_IDENTITE, "sha256": K2.EMPREINTE_CRITERE_IDENTITE},
         "variante_de_la_course": variante, "seconde_course": seconde_course,
         "avertissement_palier_2": None, "lecture_seconde_course": None,
         "lentilles": {"R": lentille("R") if r is None else r, "S": lentille("S") if s is None else s}}
    return f | plus


# --- registre propre jouet -----------------------------------------------------------------------------------------------------------------
def monde(racine: Path, fiche_jouet: dict | None = None, piece_go: str | None = None, plus: tuple = (), sans: tuple = (),
          remplace: dict | None = None) -> Path:
    """Écrit sous `racine` un dépôt jouet : pièce de `GO-LENTILLES-BBIS-V2`, fiche de rangement, registre propre. `plus` :
    lignes ajoutées en fin de registre, `(clé, heure, chemin, sha256)` ou nom court (`avertissement`, `lecture_seconde_course`,
    `entrees_v1`, `tables_v1`) ; `sans` : clés retirées ; `remplace` : clé → ligne. Rend le chemin du registre."""
    racine = Path(racine)
    go = ecrire(racine, PIECE_GO, piece_go if piece_go is not None else f"# Pièce jouet\n\n{N12_SAINE}\n\n{N17_SAINE}\n")
    f = ecrire(racine, FICHE, json.dumps(fiche() if fiche_jouet is None else fiche_jouet, ensure_ascii=False, indent=1))
    lignes = [("ABSENCE-VERDICT-LENTILLES-BBIS", H["absence"], "registres/t07-etape-b-bis-v1.md", "5" * 64),
              ("SCELLEMENT-LENTILLES-BBIS", H["absence"], K.TEXTE, K.EMPREINTE_TEXTE),
              (K2.CLE_ADDENDUM, H["addendum"], K2.ADDENDUM, K2.EMPREINTE_ADDENDUM),
              (K2.CLE_SCELLEMENT_V2, H["scellement_v2"], K2.TEXTE_V2, K2.EMPREINTE_TEXTE_V2),
              (K2.CLE_GO_V2, H["go_v2"], PIECE_GO, go),
              ("GO-LENTILLES-BBIS", H["code_v1"], "registres/go-extraits/jouet.md", "4" * 64),
              ("CODE-LENTILLES-BBIS", H["code_v1"], "docs/fiche-code-jouet.json", "4" * 64),
              (K2.CLE_CODE_V2, H["code_v2"], "docs/fiche-code-v2-jouet.json", "6" * 64),
              (K2.CLE_RANGEMENT, H["rangement"], FICHE, f)]
    courtes = {"avertissement": (K2.CLE_AVERTISSEMENT, H["avertissement"], "docs/avertissement-jouet.md", "7" * 64),
               "lecture_seconde_course": (K2.CLE_LECTURE_SECONDE_COURSE, H["lecture_seconde_course"], "docs/lecture-2.md", "8" * 64),
               "entrees_v1": (K2.CLE_ENTREES_V1, H["entrees_v1"], "diag/x/entrees-lentilles-bbis.json", "9" * 64),
               "tables_v1": (K2.CLE_TABLES_V1, H["tables_v1"], "diag/x/tables-lentilles-bbis.json", "1" * 64)}
    lignes = [(remplace or {}).get(l[0], l) for l in lignes if l[0] not in sans]
    lignes += [courtes[p] if isinstance(p, str) else p for p in plus]
    texte = "# Registre propre jouet\n\n" + "".join(f"| {c} | {h} | {ch} | {s} |\n" for c, h, ch, s in lignes)
    ecrire(racine, REGISTRE, texte)
    return racine / REGISTRE


def ligne_du_noeud(racine: Path, lentilles: str = "R", heure: str | None = None) -> tuple:
    """Pièce jouet du mot de Lazar et sa ligne `NOEUD-PALIER-2-AJUSTEMENT-SEUL-LENTILLES-BBIS`."""
    mot = "Lentilles nommées : R et S" if lentilles == "R et S" else f"Lentille nommée : {lentilles}"
    chemin = f"docs/mot-lazar-noeud-jouet-{lentilles.replace(' ', '-')}.md"
    s = ecrire(racine, chemin, f"# Mot de Lazar (jouet)\n\n- {mot}\n")
    return (K2.CLE_NOEUD_AJUSTEMENT_SEUL, heure or H["noeud"], chemin, s)


def condition(racine: Path, fiche_jouet: dict, plus: tuple = (), **monde_plus) -> dict:
    registre = monde(racine, fiche_jouet, plus=plus, **monde_plus)
    etat = nl.exiger_registre_v2(registre)
    return nl.condition_de_lecture(nl.lire_fiche(racine, etat), etat, racine)


# --- faux fichiers d'ajustement --------------------------------------------------------------------------------------------------------------
META_JOUET = {"lens": "R", "model": "meta-llama/Llama-3.1-8B-Instruct", "layers": 5, "model_layers": 5, "targets": ["out", "mid"],
              "rows_sha256": "a6" * 32, "docs": 6, "seq_len": 128, "full_length": True, "basis": None, "modality": "text",
              "corpus_spec": "file:dclm.jsonl", "dtype": "bfloat16", "rules": {"r": 1}}


def meta_jouet(lettre: str) -> dict:
    return META_JOUET | ({"lens": "S", "targets": ["mid", "out"]} if lettre == "S" else {})


def attendu(lettre: str, **plus) -> nl.Attendu:
    base = dict(lettre=lettre, n_couches=4 if lettre == "R" else 5, largeur=D, couches=COUCHES_JOUET, n_docs=(3, 3), next_doc=6,
                meta={c: meta_jouet(lettre).get(c) for c in K2.CHAMPS_META})
    return nl.Attendu(**(base | plus))


def sommes_jouet(lettre: str, garde: str = "ajustement", d: int = D) -> dict:
    """`sums` d'un faux fichier d'ajustement : cible `out` de 4 couches pour R, 5 pour S ; cible `mid` à côté."""
    import torch
    g = rng(f"{garde}-{lettre}")
    n = 4 if lettre == "R" else 5
    out = [torch.from_numpy((3 * np.eye(d) + g.standard_normal((n, d, d))).astype(np.float32)) for _ in (0, 1)]
    mid = [torch.from_numpy(g.standard_normal((5, d, d)).astype(np.float32)) for _ in (0, 1)]
    cibles = ("out", "mid") if lettre == "R" else ("mid", "out")
    return {(c, h): (out if c == "out" else mid)[h] for c in cibles for h in (0, 1)}


def ecrire_ajustement(chemin: Path, lettre: str, sommes: dict | None = None, meta: dict | None = None, n_docs=(3, 3), next_doc=6,
                      **plus) -> bytes:
    """Écrit un faux fichier d'ajustement par `torch.save` (mêmes clés que le voisin) et rend ses octets."""
    import torch
    objet = {"meta": meta_jouet(lettre) if meta is None else meta,
             "state": {"n_docs": list(n_docs), "next_doc": next_doc, "sums": sommes_jouet(lettre) if sommes is None else sommes}}
    Path(chemin).parent.mkdir(parents=True, exist_ok=True)
    torch.save(objet | plus, chemin)
    return Path(chemin).read_bytes()


class TransportJouet:
    """Transport en mémoire : `fichiers` : url → octets ; `refus` : urls refusées ; `demandes` : ce qui a été demandé."""

    def __init__(self, fichiers: dict, refus: tuple = (), bloc: int = 1000):
        self.fichiers, self.refus, self.bloc, self.demandes = dict(fichiers), set(refus), bloc, []

    def octets(self, url, cle=None, debut=None, fin=None):
        from controle_ia.lentilles_sondes_bbis.montage_v1 import RefusReseau
        self.demandes.append(("octets", url, cle is not None))
        if url in self.refus or url not in self.fichiers:
            raise RefusReseau(f"refus simulé ({url.rsplit('/', 1)[-1]})")
        return self.fichiers[url][debut or 0:(fin if fin is not None else len(self.fichiers[url]) - 1) + 1]

    def flux(self, url, cle=None, debut=0):
        from controle_ia.lentilles_sondes_bbis.montage_v1 import RefusReseau
        self.demandes.append(("flux", url, cle is not None))
        if url in self.refus or url not in self.fichiers:
            raise RefusReseau(f"refus simulé ({url.rsplit('/', 1)[-1]})")
        o = self.fichiers[url]
        for i in range(debut, len(o), self.bloc):
            yield o[i:i + self.bloc]


def extraire(octets: bytes, lettre: str, dossier: Path, bloc: int = 997, **plus) -> dict:
    """Passe des octets par l'extracteur, bloc par bloc, et conclut sur leur taille et leur empreinte."""
    ex = nl.ExtracteurAjustement(attendu(lettre, **plus), dossier)
    for i in range(0, len(octets), bloc):
        ex.recevoir(octets[i:i + bloc])
    return ex.conclure(len(octets), sha(octets))
