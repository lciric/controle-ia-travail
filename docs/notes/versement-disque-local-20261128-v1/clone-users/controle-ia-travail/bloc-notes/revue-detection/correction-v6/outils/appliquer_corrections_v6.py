"""Différentiel v5 → v6 de la synthèse « comment détecter » (correcteur v6). Rejouable.

- v5 contrôlée par empreinte complète.
- Textes des rapports : extraits par extraire_corrections.py (rapports contrôlés par empreinte), jamais recopiés à la main.
- Chaque ancien texte doit être trouvé exactement une fois dans le texte courant (blancs ramenés à « au moins un blanc ») ;
  sinon ARRÊT, rien n'est écrit.
- Écarts aux mots exacts : seulement ceux de la liste ECARTS ci-dessous, chacun déclaré au traitement.
- Mise en forme : seules les lignes touchées de plus de 120 caractères sont repliées (jamais une ligne de table ni un
  titre) ; une coupure qui ferait commencer une ligne par une marque de bloc Markdown est refusée.
Usage : python3 -I -B appliquer_corrections_v6.py SORTIE.md
"""
import hashlib
import os
import re
import sys
import textwrap
from pathlib import Path

ICI = Path(os.path.abspath(__file__)).parent
sys.path.insert(0, str(ICI))
import extraire_corrections as ex  # noqa: E402

RD = ex.RD
V5 = RD / "synthese-comment-detecter-v5.md"
V5_SHA = "17069e06f2f4d1a50f556c097a9278af3b2fc0d951b4d4cdd754998db3ab413d"
LARGEUR = 120
ATT_P015_T06 = "**[Décision de Lazar en attente : P-015, et ajout d'une condition à T0.6 (nœud)]**"
ATT_P017 = "**[Décision de Lazar en attente : P-017]**"
ATT_N030 = "**[Décision de Lazar en attente : N-030]**"
ATT_REV = "**[Décision de Lazar en attente : nœud « Revendication »]**"


def corrections():
    """Rejoue l'extraction (mêmes contrôles d'empreinte) et rend {constat: [[ancien, nouveau], ...]}."""
    import io
    import json
    from contextlib import redirect_stdout
    f = io.StringIO()
    with redirect_stdout(f):
        ex.main()
    return json.loads(f.getvalue())


def remplace_dans(s, a, b):
    if s.count(a) != 1:
        raise SystemExit(f"ARRÊT : écart non applicable, « {a[:60]} » trouvé {s.count(a)} fois")
    return s.replace(a, b)


# ---------- textes neufs du correcteur v6 (déclarés au traitement) ----------
ENTETE_V6 = (
    "- **v6 (correcteur, tour 5).** Correcteur neuf de la session 16 : je n'ai écrit ni la v1, ni la v2, ni la v3, ni la v4, "
    "ni la v5, ni les extractions, ni les vérifications, ni les traitements. 2026-10-21, à partir de 00:05 UTC environ. Part "
    "de la v5 (`17069e06…`) et traite les 22 constats des deux vérifications du tour 4 : fidélité, VV5-fidelite-01 à 08 "
    "(`…/revue-detection/verification-v5-fidelite/verification-v5-fidelite-v1.md`, `05472092…`, « conforme après "
    "corrections ») ; sens, VV5-sens-01 à 14 (`…/revue-detection/verification-v5-sens/verification-v5-sens-v1.md`, "
    "`e3e4a650…`, « conforme après corrections »). 20 sont appliqués ici, en mots exacts des rapports, extraits par script ; "
    "deux visent un autre fichier (VV5-fidelite-08 : le traitement de la v5 ; VV5-sens-14 : le registre) et sont consignés "
    "au traitement, qui déclare aussi chaque écart aux mots exacts : "
    "`…/revue-detection/traitement-verifications-v5-par-correcteur-v1.md`. Les propositions du vérificateur « sens » "
    "restent les siennes : (b') pour E2 (" + ATT_P015_T06 + ") ; options (A), (B), (C), (C') de P-017 (" + ATT_P017 + "). "
    "Les dix PDF de `[N]` et `[X]` sont retéléchargés d'arxiv.org, égaux octet pour octet à ceux de la v1 ; les contrôles "
    "qui en dépendaient sont refaits sur PDF (ligne R7). Registres non relus au-delà des versions que cite la v5 (tête "
    "`9ecd952`), sauf les lignes que citent les constats. Différentiel : "
    "`…/revue-detection/correction-v6/outils/appliquer_corrections_v6.py`. Le fond change en sections 1 (point 1 : sujet de "
    "la question confondu dans le contre-cas de [DYL]), 2.1 (lignes [BX] et "
    "[DYL] ; « Aussi »), 3 (rangs 2 et 4), 4 (règles communes : T4 résiduel ; tables E1, E2 et E3), 5 (recommandation (3), "
    "confiance, nœud E2) et « Décisions prises depuis la v4 » ; aucun pouvoir changé ; la confiance de 15 à 25 % vaut pour "
    "une condition flagrante comme P3, sans chiffre pour les doses diffuses.\n"
)

SOURCES_V6 = (
    "  v6 : lignes que citent les constats, relues à la source par script, empreinte complète d'abord "
    "(`…/revue-detection/correction-v6/sortie-controles-v6.txt`, section F) : document de P-015 (`6e74c6cb…`) ; brouillon "
    "de T0.6 (`e212fb35…`) ; `docs/decisions/proposition-P-011-T0.7-sondes-v1.md` (`64afff19…`) ; [P] (`d975e981…`) ; "
    "`registres/decisions.md` et `registres/go.md` à `9ecd952` (`e8b73c64…`, `1a392407…`, par `git show`, lecture seule) ; "
    "`…/brainstorm-outils-p3/reponse-claude-prompt-unique-v1.md` (`f9aa1655…`) ; "
    "`…/p3b/consigne-redacteur-P3b-brouillon1-v1.md` (`f8305c0e…`) ; `…/p3b/a-transmettre-contre-lecture-P3b-v1.md` "
    "(`23c742be…`) ; `…/p3b/consigne-contre-lecture-R2-P3b-brouillon1-v1.md` (`138b3afd…`, sans compagnon). Convention "
    "(VV5-fidelite-06) : « P-015 l. N » ou « P-015, l. N » renvoie partout, section « Décisions prises depuis la v4 » "
    "comprise, au document de P-015 (`6e74c6cb…`) ; la ligne de P-015 au registre est dite « l. 392 » dans la puce "
    "**P-015** de cette section, ou « `registres/decisions.md` l. 392 ».\n"
)


def r7_v6(n):
    return (
        " v6 : les dix PDF de `[N]` et `[X]` (MA, BU, LIAR, FQ, K, LB, AU, DYL, RH, CC) sont retéléchargés le 2026-10-21 "
        "depuis `https://arxiv.org/pdf/<identifiant et version>` dans `[C6]` (section 6) ; empreinte complète égale, pour "
        "chacun, à celle de la table des clés et de `citations-synthese-v1.json` (`21868605…`) ; compagnon `.sha256` à "
        "côté. Rejoués sur PDF empreinté, sans aucun extrait texte (`…/revue-detection/correction-v6/outils/controles_v6.py`, "
        "outil `pagev6.py`, sortie `…/revue-detection/correction-v6/sortie-controles-v6.txt`) : les "
        f"{n['A']} contrôles du correcteur v5 (dont {n['A_txt']} lus jusque-là sur extraits texte) ; les {n['B']} du "
        f"vérificateur « fidélité » (dont {n['B_txt']} sur DYL, LB, BU et AU) ; les {n['C']} du vérificateur « sens » sur "
        f"[DYL] (p. 7, p. 11) ; les {n['D']} citations de la v1 ; {n['E']} contrôles des phrases neuves de la v6 qui citent "
        f"une page ; {n['F']} renvois de ligne neufs (dépôt et bloc-notes) : tous trouvés à la page ou à la ligne citée. "
        f"Épreuve R5 : {n['R5']} artefacts (chiffre changé, mot changé, page ou ligne voisine, colonnes permutées, mauvaise "
        "clé), tous rejetés ; garde d'empreinte : copie saine acceptée, trois artefacts (compagnon faux, octets ajoutés, "
        "compagnon absent) arrêtés."
    )


SECTION6_V6 = (
    " v6 : `[C6]` = `…/revue-detection/correction-v6/pdf/` ; les dix PDF de `[N]` et `[X]` y sont relus, à "
    "`[C6]<identifiant et version>/<identifiant et version>.pdf` (par exemple `[C6]2606.12618v2/2606.12618v2.pdf` pour "
    "DYL), téléchargés le 2026-10-21 depuis `https://arxiv.org/pdf/<identifiant et version>` ; empreinte complète égale à "
    "celle de la table pour chacun ; compagnon `.sha256` à côté de chacun. `[N]` (`pdf-nouveaux/`, avec "
    "`provenance-nouveaux-v1.md`) n'existe plus dans le bloc-notes restauré (vérifié sur disque, R11) ; les chemins `[N]` "
    "et `[X]` de la table restent ceux de la v1."
)

FICHIERS_V6 = (
    " v6 (`…/revue-detection/correction-v6/`) : `outils/extraire_corrections.py` (corrections des deux rapports du tour 4, "
    "extraites par script ; sortie `corrections-v5-extraites.json`) ; `outils/appliquer_corrections_v6.py` (le "
    "différentiel, v5 → v6 : remplacements trouvés une seule fois, blancs normalisés, lignes touchées repliées à 120 "
    "caractères) ; `outils/pagev6.py` (une page d'une source, sur PDF empreinté seulement) ; `outils/controles_v6.py` et "
    "`sortie-controles-v6.txt` (contrôles à la page et à la ligne, épreuve R5) ; `outils/verifier_v6.py` et "
    "`sortie-verifier-v6.txt` (mots exacts présents dans la v6, anciens textes absents, rien d'autre de changé que les "
    "blancs) ; `pdf/` (les dix PDF retéléchargés, avec leurs compagnons). PDF de `[N]` et `[X]` retrouvés : empreintes "
    "égales, compagnons faits ; aucun versement au dépôt."
)


def entrees(cor, n):
    """Liste ordonnée : (étiquette, ancien, nouveau). Les écarts aux mots exacts sont faits ici et seulement ici."""
    E = []

    def rap(c, i, etiq=None, nouveau=None, ancien=None):
        a, b = cor[c][i]
        E.append((etiq or f"{c} ({i + 1})", ancien if ancien is not None else a, nouveau if nouveau is not None else b))

    # --- fidélité ---
    rap("VV5-fidelite-01", 0)
    # VV5-fidelite-02 : fusionné dans VV5-sens-06 (même passage ; le texte de VV5-sens-06 contient la correction de 02).
    rap("VV5-fidelite-03", 0)
    rap("VV5-fidelite-04", 0)
    rap("VV5-fidelite-05", 0)
    rap("VV5-fidelite-06", 0)
    rap("VV5-fidelite-06", 1)
    a, b = cor["VV5-fidelite-07"][0]
    assert b.endswith(")")
    rap("VV5-fidelite-07", 0, "VV5-fidelite-07 (1), complété v6",
        nouveau=b[:-1] + " ; v6 : les 22, ceux de `[N]` et `[X]` retéléchargés)")
    a, b = cor["VV5-fidelite-07"][1]
    rap("VV5-fidelite-07", 1, "VV5-fidelite-07 (2), corrigé sur disque (R11)",
        nouveau="Compagnons `.sha256` (R6) : présents pour `[D]` ; pour MA, présent "
                "(`[X]pdf-anthropic/2503.10965/2503.10965v2.pdf.sha256`, vérifié sur disque le 2026-10-21, R11), son PDF "
                "absent du bloc-notes restauré à la v5 ;")
    # --- sens ---
    rap("VV5-sens-01", 0)
    a, b = cor["VV5-sens-01"][1]
    rap("VV5-sens-01", 1, "VV5-sens-01 (2), mention d'attente", nouveau=b + " " + ATT_P015_T06)
    a, b = cor["VV5-sens-01"][2]
    pivot = "(b'), confiance ≈ 55 %.**"
    rap("VV5-sens-01", 2, "VV5-sens-01 (3), mention d'attente", nouveau=remplace_dans(b, pivot, pivot + " " + ATT_P015_T06))
    for i in range(3):
        rap("VV5-sens-02", i)
    rap("VV5-sens-03", 0)
    a, b = cor["VV5-sens-03"][1]
    rap("VV5-sens-03", 1, "VV5-sens-03 (2), mention d'attente",
        nouveau=remplace_dans(b, "Options : (A) défaut", ATT_P017 + " Options : (A) défaut"))
    rap("VV5-sens-03", 2)
    rap("VV5-sens-03", 3)
    rap("VV5-sens-04", 0)
    rap("VV5-sens-04", 1)
    rap("VV5-sens-05", 0)
    rap("VV5-sens-05", 1)
    rap("VV5-sens-06", 0, "VV5-sens-06 (1), avec VV5-fidelite-02")
    a, b = cor["VV5-sens-07"][0]
    rap("VV5-sens-07", 0, "VV5-sens-07 (1), mention d'attente", nouveau=b + " " + ATT_N030)
    rap("VV5-sens-07", 1)
    rap("VV5-sens-07", 2)
    for i in range(7):
        rap("VV5-sens-08", i)
    a, b = cor["VV5-sens-08"][7]
    fin = " **Ce qu'a fait Anthropic.**"
    assert a.endswith(fin) and b.endswith(fin)
    rap("VV5-sens-08", 7, "VV5-sens-08 (8), saut de paragraphe gardé", ancien=a[:-len(fin)], nouveau=b[:-len(fin)])
    rap("VV5-sens-09", 0)
    rap("VV5-sens-10", 0)
    rap("VV5-sens-11", 0)
    rap("VV5-sens-12", 0)
    rap("VV5-sens-12", 1)
    rap("VV5-sens-13", 0)
    # --- correcteur v6 : en-tête, sources, R7, section 3, R8, mentions d'attente, section 6, fichiers ---
    E += [
        ("v6 : titre", "ce qu'ont fait Anthropic et les autres — synthèse v5",
         "ce qu'ont fait Anthropic et les autres — synthèse v6"),
        ("v6 : en-tête, puce v6", "- **Sources.** Cinq extractions neuves sous",
         ENTETE_V6 + "- **Sources.** Cinq extractions neuves sous"),
        ("v6 : sources", "(`6e74c6cb…`, compagnon égal). `…/` = `/tmp/",
         "(`6e74c6cb…`, compagnon égal).\n" + SOURCES_V6 + "  `…/` = `/tmp/"),
        ("v6 : R7", "`…/revue-detection/extraction/txt-representations/`), sans empreinte du PDF.",
         "`…/revue-detection/extraction/txt-representations/`), sans empreinte du PDF." + r7_v6(n)),
        ("v6 : section 3, en-tête", "v5 : rangs 2 à 6 et 9 annotés, pouvoirs inchangés (constats VV4) ;",
         "v5 : rangs 2 à 6 et 9 annotés, pouvoirs inchangés (constats VV4) ; v6 : rangs 2 et 4 annotés (VV5-sens-10, 12), "
         "rang 8 en forme R8, pouvoirs inchangés ;"),
        ("v6 : section 3, ce qui a changé", "« au-dessus » qui lirait la consigne, au lieu d'un « faux positif ».",
         "« au-dessus » qui lirait la consigne, au lieu d'un « faux positif ». v6 : aucun pouvoir changé ; rang 2 : "
         "hypothèse d'Apollo pour la sonde Instructed-Pairs avancée contre le témoin, transposée à P3-P3 ; rang 4 : "
         "« Backdoors » contre le maximum, sujet de la question confondu dans le contre-cas de [DYL] ; rang 8 : « des "
         "sources lues » (R8)."),
        ("v6 : rang 8, R8 (remarque de la vérification « fidélité »)",
         "notre 0,57 ne se compare à aucun chiffre publié", "notre 0,57 ne se compare à aucun chiffre des sources lues"),
        ("v6 : recommandation (2), mention d'attente", "(option (a) du nœud « Revendication » ci-dessous)",
         "(option (a) du nœud « Revendication » ci-dessous ; " + ATT_REV + ")"),
        ("v6 : E1, quoi, mention d'attente", "lus comme diagnostic de l'instrument, jamais comme détection.",
         "lus comme diagnostic de l'instrument, jamais comme détection (" + ATT_REV + ", option (a))."),
        ("v6 : E1, tranche, mention d'attente", "T4 au champ et (v) répondent ; jamais une détection.",
         "T4 au champ et (v) répondent ; jamais une détection (" + ATT_REV + ")."),
        ("v6 : nœud E2, manipulation, mention d'attente", "confiance ≈ 50 % (v3 : 60 %). Pas de défaut",
         "confiance ≈ 50 % (v3 : 60 %) ; elle diverge de la recommandation de la session sur P-017 (section « Décisions "
         "prises depuis la v4 ») " + ATT_P017 + ". Pas de défaut"),
        ("v6 : section 6, [N] et [X]", "`[N]provenance-nouveaux-v1.md` : à créer avant tout versement au dépôt.",
         "`[N]provenance-nouveaux-v1.md` : à créer avant tout versement au dépôt." + SECTION6_V6),
        ("v6 : « Décisions », lecture « double comptabilité », jonction avec VV5-sens-08",
         "est élargi de cette lecture ; la table E1 ne l'a pas.",
         "est élargi de cette lecture ; la table E1 l'a depuis la v6 (E1 (vi), VV5-sens-08)."),
        ("v6 : fichiers", "empreintes et compagnons à refaire avant tout versement au dépôt (R6).",
         "empreintes et compagnons à refaire avant tout versement au dépôt (R6)." + FICHIERS_V6),
    ]
    return E


MARQUE = re.compile(r"^([-*+>|]|#{1,6}|\d+[.)])$")
ITEM = re.compile(r"^(\s*)([-*+]|\d+\.)\s+")


LIE = "\ue000"  # espace insécable de travail : jamais de coupure avant « ; : ? ! » % », après « « » ou « ≈ », ni dans « l. 12 »
LIENS = [(re.compile(r" (?=[;:?!»%])"), LIE), (re.compile(r"(?<=«) "), LIE), (re.compile(r"(?<=≈) "), LIE),
         (re.compile(r"(?<=\b[lp]\.) (?=\d)"), LIE)]


def replie(ligne):
    if len(ligne) <= LARGEUR or ligne.lstrip().startswith(("|", "#")):
        return [ligne]
    if LIE in ligne:
        raise SystemExit("ARRÊT : caractère de travail déjà présent dans le texte")
    ind = ligne[:len(ligne) - len(ligne.lstrip())]
    m = ITEM.match(ligne)
    suite = " " * len(m.group(0)) if m else ind
    corps = ligne.strip()
    for motif, r in LIENS:
        corps = motif.sub(r, corps)
    for larg in range(LARGEUR, LARGEUR - 30, -1):
        w = textwrap.TextWrapper(width=larg, initial_indent=ind, subsequent_indent=suite, break_long_words=False,
                                 break_on_hyphens=False)
        out = [l.replace(LIE, " ") for l in w.wrap(corps)]
        if all(not MARQUE.match(l.split()[0]) for l in out[1:]):
            return out
    return [ligne]


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
        bloc = texte[d:f].split("\n")
        neuf = [x for l in bloc for x in replie(l)]
        texte = texte[:d] + "\n".join(neuf) + texte[f:]
        journal.append(f"appliqué | {etiq} | ligne de départ {texte.count(chr(10), 0, d) + 1} | {len(a)} → {len(b)} car.")
    return texte, journal


def comptes():
    """Nombres de la ligne R7, lus dans la sortie des contrôles (contrôlée par son compagnon)."""
    s = RD / "correction-v6/sortie-controles-v6.txt"
    comp = (s.parent / (s.name + ".sha256")).read_text().split()[0]
    b = s.read_bytes()
    if hashlib.sha256(b).hexdigest() != comp:
        raise SystemExit("ARRÊT : sortie-controles-v6.txt différente de son compagnon")
    t = b.decode("utf-8").splitlines()
    sec = lambda x: [l for l in t if l.startswith(("TROUVÉ", "ABSENT")) and f"| {x} |" in l]
    n = {k: len(sec(k)) for k in "ABCDEF"}
    n["A_txt"] = sum("[C6]" in l for l in sec("A"))
    n["B_txt"] = sum("[C6]" in l for l in sec("B"))
    n["R5"] = sum(l.startswith(("rejeté", "ACCEPTÉ")) for l in t)
    if any(l.startswith(("ABSENT", "ACCEPTÉ")) for l in t) or "gardes conformes" not in t[-1]:
        raise SystemExit("ARRÊT : les contrôles ne sont pas tous conformes")
    return n


def main():
    sortie = Path(sys.argv[1])
    b = V5.read_bytes()
    h = hashlib.sha256(b).hexdigest()
    if h != V5_SHA:
        raise SystemExit(f"ARRÊT : v5 a l'empreinte {h}, attendue {V5_SHA}")
    if sortie.exists():
        raise SystemExit(f"ARRÊT : {sortie} existe déjà (R12 : on n'écrase jamais)")
    cor = corrections()
    E = entrees(cor, comptes())
    texte, journal = appliquer(b.decode("utf-8"), E)
    sortie.write_text(texte, encoding="utf-8")
    for l in journal:
        print(l)
    print(f"{len(E)} remplacements appliqués ; sortie {hashlib.sha256(texte.encode('utf-8')).hexdigest()}")


if __name__ == "__main__":
    main()
