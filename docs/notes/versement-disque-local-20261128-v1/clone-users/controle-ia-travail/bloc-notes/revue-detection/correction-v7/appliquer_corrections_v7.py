"""Différentiel v6 → v7 de la synthèse « comment détecter » (correcteur v7). Rejouable.

- v6 et rapport VV6 contrôlés par empreinte complète (constante et compagnon).
- Textes des constats VV6-fidelite-01 à 04 : extraits du rapport par analyse (« remplacer « … » par « … » », guillemets
  imbriqués comptés), jamais recopiés à la main.
- Remarques non comptées du rapport : trois remplacements du correcteur (textes ci-dessous, déclarés au traitement).
- Chaque ancien texte doit être trouvé exactement une fois dans le texte courant (blancs ramenés à « au moins un
  blanc ») ; sinon ARRÊT, rien n'est écrit.
- Mise en forme : seules les lignes touchées de plus de 120 caractères sont repliées (jamais une ligne de table ni un
  titre) ; une coupure qui ferait commencer une ligne par une marque de bloc Markdown est refusée.
Usage : PYTHONDONTWRITEBYTECODE=1 python3 -I -B appliquer_corrections_v7.py SORTIE.md [--json CORRECTIONS.json]
"""
import hashlib
import json
import re
import sys
import textwrap
from pathlib import Path

RD = Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection")
V6 = RD / "synthese-comment-detecter-v6.md"
V6_SHA = "124d06f821f5780dbc810d710d08a3d00239ae34e8545fe69c3ea683177511e8"
VV6 = RD / "verification-v6-fidelite/verification-v6-fidelite-v1.md"
VV6_SHA = "30c79b0f708e92553acb0cce788bb84141a1be817a13463e3bae64cd8fcc6d39"
LARGEUR = 120
MARQUE = re.compile(r"^([-*+]|\d+[.)]|#+|>|\|)$")
LIE = "\x00"  # espace insécable le temps du repli (typographie française : « x », x :, x ;, ≈ x)
LIENS = [(" " + c, LIE + c) for c in ":;»?!%"] + [("« ", "«" + LIE), ("≈ ", "≈" + LIE)]

# ---------- remarques non comptées (plus petite correction, consigne point 2) ----------
REMARQUES = [
    ("remarque N-030",
     "- **N-030** (l. 396 ; nœud, non tranché) :",
     "- **N-030** (l. 396 ; nœud, non tranché ; **[Décision de Lazar en attente : N-030]**) :"),
    ("remarque Revendication",
     "- **Revendication et voie de R-262 (2)** (proposition) :",
     "- **Revendication et voie de R-262 (2)** (proposition ; "
     "**[Décision de Lazar en attente : nœud « Revendication »]**) :"),
    ("remarque P-017 en-tête",
     "; options (A), (B), (C), (C') de P-017 (**[Décision de Lazar en attente : P-017]**).",
     "; (C') et la mise en options de P-017 (**[Décision de Lazar en attente : P-017]**) ; les options (A), (B) et (C) "
     "sont celles de P-017 (`registres/decisions.md` l. 394)."),
]


def lire_controle(p, attendu):
    b = p.read_bytes()
    h = hashlib.sha256(b).hexdigest()
    comp = (p.parent / (p.name + ".sha256")).read_text(encoding="utf-8").split()
    if h != attendu or comp[0] != attendu or comp[1] != p.name:
        raise SystemExit(f"ARRÊT : {p.name} : empreinte {h}, compagnon {comp}, attendue {attendu}")
    return b.decode("utf-8")


def guillemets(s, i):
    """s[i] == '«' ; rend (contenu, fin) du texte entre guillemets équilibrés."""
    if s[i] != "«":
        raise SystemExit(f"ARRÊT : « attendu à {i} : {s[i:i + 40]!r}")
    p = 0
    for j in range(i, len(s)):
        if s[j] == "«":
            p += 1
        elif s[j] == "»":
            p -= 1
            if p == 0:
                return s[i + 1:j].strip(), j + 1
    raise SystemExit("ARRÊT : guillemets non équilibrés")


def extraire(rapport):
    lignes = rapport.split("\n")
    debuts = [i for i, l in enumerate(lignes) if re.match(r"\*\*VV6-fidelite-0\d — ", l)]
    if len(debuts) != 4:
        raise SystemExit(f"ARRÊT : {len(debuts)} constats trouvés, 4 attendus")
    out = []
    for k, d in enumerate(debuts):
        etiq = re.match(r"\*\*(VV6-fidelite-0\d)", lignes[d]).group(1)
        f = debuts[k + 1] if k + 1 < len(debuts) else next(
            i for i in range(d + 1, len(lignes)) if lignes[i].startswith("## "))
        bloc = lignes[d:f]
        c = [i for i, l in enumerate(bloc) if l.startswith("- **Correction (mots exacts).**")]
        if len(c) != 1:
            raise SystemExit(f"ARRÊT : {etiq} : {len(c)} puces « Correction »")
        puce = [bloc[c[0]]]
        for l in bloc[c[0] + 1:]:
            if l.startswith("- ") or not l.strip() or l.startswith("**") or l.startswith("#"):
                break
            puce.append(l)
        t = " ".join(x.strip() for x in puce)
        if t.count("remplacer «") != 1:
            raise SystemExit(f"ARRÊT : {etiq} : « remplacer « » trouvé {t.count('remplacer «')} fois")
        i = t.index("remplacer «") + len("remplacer ")
        ancien, j = guillemets(t, i)
        if not t[j:].startswith(" par «"):
            raise SystemExit(f"ARRÊT : {etiq} : « par « » attendu après l'ancien texte")
        nouveau, j2 = guillemets(t, j + len(" par "))
        if t[j2:].strip() != ".":
            raise SystemExit(f"ARRÊT : {etiq} : texte inattendu après le nouveau : {t[j2:]!r}")
        out.append((etiq, ancien, nouveau))
    return out


def replie(ligne):
    if len(ligne) <= LARGEUR or ligne.lstrip().startswith(("|", "#")):
        return [ligne]
    ind = ligne[:len(ligne) - len(ligne.lstrip())]
    m = re.match(r"\s*(?:[-*+]|\d+[.)]) ", ligne)
    suite = " " * len(m.group(0)) if m else ind
    corps = ligne.strip()
    for x, y in LIENS:
        corps = corps.replace(x, y)
    for larg in range(LARGEUR, LARGEUR - 30, -1):
        w = textwrap.TextWrapper(width=larg, initial_indent=ind, subsequent_indent=suite, break_long_words=False,
                                 break_on_hyphens=False)
        out = [l.replace(LIE, " ") for l in w.wrap(corps)]
        if all(not MARQUE.match(l.split()[0]) for l in out[1:]):
            return out
    raise SystemExit(f"ARRÊT : repli impossible : {ligne[:80]!r}")


def appliquer(texte, E):
    journal = []
    for etiq, a, b in E:
        motif = r"\s+".join(re.escape(t) for t in a.split())
        trouves = list(re.finditer(motif, texte))
        if len(trouves) != 1:
            raise SystemExit(f"ARRÊT : « {etiq} » : ancien texte trouvé {len(trouves)} fois : {a[:100]!r}")
        m = trouves[0]
        texte = texte[:m.start()] + b + texte[m.end():]
        d = texte.rfind("\n", 0, m.start()) + 1
        f = texte.find("\n", m.start() + len(b))
        f = len(texte) if f < 0 else f
        neuf = [x for l in texte[d:f].split("\n") for x in replie(l)]
        texte = texte[:d] + "\n".join(neuf) + texte[f:]
        l0 = texte.count("\n", 0, d) + 1
        journal.append(f"appliqué | {etiq} | lignes {l0}-{l0 + len(neuf) - 1} de la v7 | {len(a)} → {len(b)} car.")
    return texte, journal


def main():
    sortie = Path(sys.argv[1])
    if sortie.exists():
        raise SystemExit(f"ARRÊT : {sortie} existe déjà (R12 : on n'écrase jamais)")
    v6 = lire_controle(V6, V6_SHA)
    E = extraire(lire_controle(VV6, VV6_SHA)) + REMARQUES
    texte, journal = appliquer(v6, E)
    if "--json" in sys.argv:
        pj = Path(sys.argv[sys.argv.index("--json") + 1])
        if pj.exists():
            raise SystemExit(f"ARRÊT : {pj} existe déjà")
        pj.write_text(json.dumps([{"etiquette": e, "ancien": a, "nouveau": b} for e, a, b in E], ensure_ascii=False,
                                 indent=1) + "\n", encoding="utf-8")
    sortie.write_text(texte, encoding="utf-8")
    for l in journal:
        print(l)
    print(f"{len(E)} remplacements appliqués ; sortie {hashlib.sha256(texte.encode('utf-8')).hexdigest()}")


if __name__ == "__main__":
    main()
