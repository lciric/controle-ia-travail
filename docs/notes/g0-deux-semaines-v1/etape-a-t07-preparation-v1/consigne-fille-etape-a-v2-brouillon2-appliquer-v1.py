"""Consigne de la session fille de l'étape A de T0.7, version 2, brouillon 2 : le brouillon 1 (`f24032e7…`, versé, gardé tel quel,
R12) plus les couples CF3-01 à CF3-05 — MA-2 de la contre-lecture des pièces de relance (R-2614, `703195e5…`) : la note pour la
mère renvoie à la suite unique de ses gestes, sans la redire ; m-1 : « les fichiers de `e3-ter-v1/` » — v1.

Préparateur (modèle A), sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-13. Bibliothèque standard
seulement. `<python du dépôt> -I -B <ce script> RACINE`. Couples défaits → brouillon 1 à l'octet ; aucun identifiant de modèle ;
six cases ⟦…⟧ dans le texte envoyé ; cible écrite (refus si elle existe). Code 0 et « TOUT PASSE », sinon code 1.
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

D = "docs/notes/g0-deux-semaines-v1/etape-a-t07-preparation-v1"
SOURCE = f"{D}/consigne-fille-etape-a-v2-brouillon1.md"
SHA_SOURCE = "f24032e7aa9f6fe9ccddbbb50a151ca3886728952c59edecd57854bcabfc16ba"
CIBLE = f"{D}/consigne-fille-etape-a-v2-brouillon2.md"
GESTES = f"{D}/relance-v2-preparation-v1/gestes-mere-relance-v2-v1.md"

ANCIENNE_NOTE = """> **Avant l'envoi** : (1) gestes de la relance (ordre v2, `docs/procedures/ordre-execution-etape-a-t07-v2-brouillon1.md`, § 0 septies) : contre-lecture (R2) de l'addendum de
> T0.7 (brouillon 2) et de l'ordre v2, scellement ; remplacement de la ligne `CODE-T07` par
> `scripts/remplacer_ligne_code_t07_v1.py` (trace scellée) ; marqueurs de l'ordre v2 remplis (`ID_SESSION_FILLE_V2`,
> `COMMIT_SCELLEMENT_T07_V2`, `ATT_C7_T07_V2`, `LIGNE_CODE_T07_V2`), ordre rempli scellé ; engagement neuf sous
> GO-2026-11-10-06 (`ANT0` = 0,43 USD) ; écrit daté de la relance (C7, S7, `SRC7` et P13 (iii), `ATT` avec le commit et les
> arbres de la mesure et `git diff --name-status C7 S7`, ligne `CODE-T07`, `ANT0`) ; l'essai neuf du remplacement entre dans
> `main` **après** S7 (ordre v2, P9) ; committer, pousser ; (2) session fille : la fille de la v1
> (`session_01QPDgKf6Rn3eTeuYMDCBiKA`, en attente depuis R-2592, crochet déjà éprouvé) ou une neuve **ouverte dans le dépôt**
> (crochet de garde, R-2545) ; (3) relire la liste des intouchables du § 3 contre l'inventaire du jour ; (4) remplacer
> chaque case `⟦…⟧` ci-dessous (**six cases, cinq valeurs** : chemin et empreinte de l'ordre v2 rempli, commit de remise
> (deux fois), écrits datés à recopier, ligne `CODE-T07` attendue ; aucune autre valeur à inventer) ; (5) envoyer le texte
> qui suit la ligne de séparation.
"""
NOUVELLE_NOTE = f"""> **Avant l'envoi (brouillon 2, MA-2 de la contre-lecture R-2614)** : jouer, dans l'ordre et sans rien y ajouter, la **suite
> unique des gestes de la mère**, `{GESTES}` (remplacement de la ligne `CODE-T07` par l'outil v2, recopie de la nouvelle ligne
> dans l'addendum, scellement de l'addendum, commit S7 sans rien sous `src/` ni `tests/`, vérifications, remplissage et
> scellement de l'ordre v2, engagement, écrit daté, remplissage des **six cases** `⟦…⟧` ci-dessous — cinq valeurs : chemin et
> empreinte de l'ordre v2 rempli, commit de remise (deux fois), écrits datés à recopier, ligne `CODE-T07` attendue —, session
> fille, envoi du texte qui suit la ligne de séparation). La liste (1) à (5) du brouillon 1 est remplacée par cette suite.
"""

COUPLES = [
    ("CF3-01", "(variante B) — v2, brouillon 1\n", "(variante B) — v2, brouillon 2\n", 1),
    ("CF3-02", "> reste égal à l'octet à la v1 (vérifié : couples défaits → v1). La note de la v1 qui suit est gardée pour mémoire.\n",
     "> reste égal à l'octet à la v1 (vérifié : couples défaits → v1). La note de la v1 qui suit est gardée pour mémoire.\n"
     "> **Brouillon 2** (2026-11-13, vers 23:50 UTC, même préparateur) = brouillon 1 (`f24032e7…`, versé, gardé tel quel) + les\n"
     f"> couples CF3-01 à CF3-05 de `{D}/consigne-fille-etape-a-v2-brouillon2-appliquer-v1.py` (couples défaits → brouillon 1).\n", 1),
    ("CF3-03", ANCIENNE_NOTE, NOUVELLE_NOTE, 1),
    ("CF3-04", "quatre fichiers dérivés de 7a en\n  réserve)", "les fichiers de `e3-ter-v1/`,\n  dérivés de 7a, en réserve)", 1),
    ("CF3-05", "   fais rien : c'est une réserve écrite, pas un geste.\n",
     "   fais rien : c'est une réserve écrite, pas un geste ; tu la recopies au compte rendu final (ordre v2, § 8).\n", 1),
]


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def appliquer(t, couples):
    for cid, a, n_, k in couples:
        if t.count(a) != k or t.count(n_) != 0:
            raise SystemExit(f"ÉCHEC {cid} : ancien {t.count(a)} (attendu {k}), nouveau {t.count(n_)}")
        t = t.replace(a, n_)
    return t


def defaire(t, couples):
    for cid, a, n_, k in reversed(couples):
        if t.count(n_) != k:
            raise SystemExit(f"ÉCHEC défaire {cid}")
        t = t.replace(n_, a)
    return t


def main(argv):
    r = Path(argv[0]) if argv else Path(".")
    s = (r / SOURCE).read_bytes()
    if sha(s) != SHA_SOURCE:
        raise SystemExit("ÉCHEC : empreinte de la source")
    b1 = s.decode("utf-8")
    b2 = appliquer(b1, COUPLES)
    if defaire(b2, COUPLES) != b1:
        raise SystemExit("ÉCHEC : couples défaits ≠ brouillon 1")
    for m in ("Claude", "claude-opus", "Opus 5", "Fable 5", "Sonnet", "Haiku"):
        if m in b2:
            raise SystemExit(f"ÉCHEC : identifiant de modèle « {m} »")
    if b2.split("\n---\n", 1)[1].count("⟦") != 6:
        raise SystemExit("ÉCHEC : six cases attendues dans le texte envoyé")
    c = r / CIBLE
    if c.exists():
        raise SystemExit("ÉCHEC : cible existante (R12)")
    c.write_bytes(b2.encode("utf-8"))
    print(f"TOUT PASSE : {CIBLE} écrit ({sha(b2.encode('utf-8'))}) ; {len(COUPLES)} couples")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
