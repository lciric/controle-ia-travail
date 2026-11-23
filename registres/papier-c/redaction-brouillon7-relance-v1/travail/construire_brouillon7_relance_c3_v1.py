"""Construit la version c3 du brouillon 7 de relance du préenregistrement du papier C : les trois remarques de la
vérification de la version c2 (rapport 52b9ce5f…, CW-01 à CW-03), par remplacements exacts sur la version c2.

Usage (depuis la racine du dépôt) :
    python3 registres/papier-c/redaction-brouillon7-relance-v1/travail/construire_brouillon7_relance_c3_v1.py SORTIE JOURNAL

Gardes : source à l'empreinte attendue ; chaque fragment trouvé une fois (un bloc : début trouvé une fois, fin une
fois après lui) ; titres de section inchangés ; un seul « À REMPLIR » dans la section « Contre-lecture », aucun
ajouté ni retiré ailleurs ; marqueurs de gabarit inchangés. Refuse d'écraser une sortie (R12).
"""
import hashlib
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[4]
SOURCE = RACINE / "brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22-c2.md"
EMPREINTE_SOURCE = "b375e6e7f0633c8433b9b5f095a7b95906e3930bd046d19c535e68e153c2c682"
DOSSIER = "registres/papier-c/redaction-brouillon7-relance-v1"
VERIF = f"{DOSSIER}/contre-lecteur/rapport-verification-c2-et-contre-lecture-devis-v1.md"
H_VERIF = "52b9ce5fab520e5117149e9a32ec8f3fa3d757734a1bb3cb6b4f744290fd961e"
H_POINTS_V1 = "ab1a9b8a15b8a41ff3c2308df73f1847913610c275b5d2461b630baae02251b5"
GO = "GO-2026-11-22-123"


def sha(chemin):
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


assert sha(RACINE / VERIF) == H_VERIF
assert sha(RACINE / DOSSIER / "points-ouverts-pour-le-directeur-brouillon7-relance-v1.md") == H_POINTS_V1
R = []


def remplace(ident, lieu, motif, ancien, nouveau):
    R.append((ident, lieu, motif, "fragment", ancien, None, nouveau))


def ajoute(ident, lieu, motif, ancre, ajout):
    R.append((ident, lieu, motif, "fragment", ancre, None, ancre + ajout))


def bloc(ident, lieu, motif, debut, fin, nouveau):
    R.append((ident, lieu, motif, "bloc", debut, fin, nouveau))


remplace(
    "L-01", "titre", "version neuve (R12)",
    "version c2 (contre-lecture et vérification traitées ; décisions D-21, D-23 et D-24 portées) : version r3 reprise",
    "version c3 (contre-lecture et deux vérifications traitées ; décisions D-21, D-23 et D-24 portées) : version r3 "
    "reprise",
)

remplace(
    "L-02", "en-tête, « État en bref »", "état après la vérification de la version c2",
    "aucune dépense : (1) la vérification, par le même contre-lecteur, des dernières corrections de cette version c2\n"
    "(verrou 7) ;",
    "aucune dépense : (1) la vérification, par le même contre-lecteur, des dernières corrections de cette version c3\n"
    "(verrou 7) ;",
)

ajoute(
    "L-03", "en-tête, « Nom (R12) »", "version neuve (R12)",
    "  de c1 et porte trois décisions du directeur s'appelle « brouillon7-relance-2026-11-22-c2 ».",
    " La version qui traite la\n"
    "  vérification de c2 s'appelle « brouillon7-relance-2026-11-22-c3 ».",
)

remplace(
    "L-04", "en-tête, « Historique »", "R12 : la version c2 entre dans l'historique",
    "**Historique (R12).** Les brouillons précédents restent tels quels :\n"
    "- brouillon 7 de relance, version c1 (2026-11-22) :",
    "**Historique (R12).** Les brouillons précédents restent tels quels :\n"
    "- brouillon 7 de relance, version c2 (2026-11-22) :\n"
    "  `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22-c2.md`\n"
    f"  (`{EMPREINTE_SOURCE}`, 259 068 octets), vérifiée par le contre-lecteur\n"
    "  (section « Contre-lecture ») ; point de départ de cette version c3 ;\n"
    "- brouillon 7 de relance, version c1 (2026-11-22) :",
)

remplace(
    "L-05", "en-tête, « Historique »", "la version c1 est le point de départ de la version c2",
    "  (section « Contre-lecture ») ; point de départ de cette version c2 ;\n",
    "  (section « Contre-lecture ») ; point de départ de la version c2 ;\n",
)

remplace(
    "L-06", "en-tête, « Ce que change… »", "paragraphe neuf : ce que change la version c3",
    "**Ce que change la version c2 du brouillon 7 de relance** (2026-11-22). Deux sources, et rien d'autre.",
    "**Ce que change la version c3 du brouillon 7 de relance** (2026-11-22). Une source : la vérification de la\n"
    f"version c2 par le même contre-lecteur (rapport `{VERIF}`,\n"
    f"`{H_VERIF}` : CV-01 à CV-03 levées ; aucun changement hors table ;\n"
    "une remarque majeure et deux mineures neuves). Le cadre du bras « saboteur sans consigne » que le directeur a\n"
    "retenu est écrit dans ce texte, le complément ne fixant que ce qui dépend du verdict de G0 (CW-03) ; sans ce\n"
    "complément, l'étape 2 ne s'ouvre pas, et c'est un nœud, dit aux « Préalables » et aux gardes 2 et 24 (CW-02) ;\n"
    "la précision 38 dit d'où vient la lettre de la décision D-21 qu'elle suit (CW-01 : la règle n'est pas changée).\n"
    f"Traitement : `{DOSSIER}/table-traitement-verification-c2-brouillon7-relance-v1.md` ; table des remplacements :\n"
    f"`{DOSSIER}/note-differences-brouillon7-relance-c3-v1.md`. Aucun énoncé d'hypothèse, aucune prédiction, aucune\n"
    "marge, aucun seuil ne change ; aucune revendication n'est ajoutée.\n"
    "\n"
    "**Ce que change la version c2 du brouillon 7 de relance** (2026-11-22). Deux sources, et rien d'autre.",
)

remplace(
    "L-07", "verrou 7 (contre-lecture)", "vérification de la version c2 faite ; reste celle de la version c3",
    "**Reste** : la vérification, par ce même\n"
    "   contre-lecteur, de ces trois corrections et de la façon dont les décisions D-21, D-23 et D-24 sont portées.",
    "Vérification de la version c2 faite par ce\n"
    f"   même contre-lecteur (rapport `{H_VERIF}` : CV-01 à CV-03\n"
    "   levées ; une majeure et deux mineures neuves, CW-01 à CW-03), que cette version c3 traite\n"
    "   (`table-traitement-verification-c2-brouillon7-relance-v1.md`). **Reste** : la vérification de ces trois\n"
    "   corrections par ce même contre-lecteur, et la confirmation par la session de conduite de la lettre de la\n"
    "   décision D-21 (précision 38).",
)

remplace(
    "L-08", "verrou 8 (accord de dépense du pilote)", "devis en brouillon 3",
    f"   `{DOSSIER}/devis-pilote-papier-C-v1-brouillon2.md`.",
    f"   `{DOSSIER}/devis-pilote-papier-C-v1-brouillon3.md`.",
)

ajoute(
    "L-09", "Plan, section 3, « Préalables » de l'étape 2", "CW-02",
    "empreintes des contenus de l'étape 2 disjointes de celles du calibrage (garde).",
    " S'y ajoute le complément scellé et\n"
    "contre-lu du bras « saboteur sans consigne » (décision D-23, ci-dessous) : sans lui, l'étape 2 ne s'ouvre pas, et\n"
    "c'est un nœud (liste d'arrêt 24).",
)

bloc(
    "L-10", "Plan, section 3, « Bras « saboteur sans consigne » »", "CW-03 : cadre retenu écrit ; CW-02",
    f"**Bras « saboteur sans consigne »** (décision D-23 du directeur, {GO} : « bras « saboteur sans\n",
    "non scellé ou non contre-lu : nœud (liste d'arrêt 24).",
    f"**Bras « saboteur sans consigne »** (décision D-23 du directeur, {GO} : « bras « saboteur sans\n"
    "consigne » pour HC2 ajouté par un complément préenregistré avant l'étape 2 » ; la recommandation retenue est\n"
    "l'option (a) de la liste des points ouverts, et l'option (c) en plus si la famille (iv) existe à l'ouverture de\n"
    "l'étape 2 ; section 7, réserve 20). TC.2 est rejoué avec un saboteur qui n'a aucune consigne de saboter en\n"
    "contexte.\n"
    "- **Cadre fixé dès maintenant**, que le complément ne peut pas changer : mêmes tâches que TC.2 et mêmes niveaux\n"
    "  du plaidoyer (k_P) ; saboteur : l'organisme de la famille (ii) du mode « coût gonflé » que le verdict de G0\n"
    "  retient, sans consigne de saboter en contexte, et de même l'organisme de la famille (iv) s'il existe à\n"
    "  l'ouverture de l'étape 2 ; honnête : le modèle de base, par les cellules H et HP_m du présent texte ; cellules\n"
    "  de plus, par organisme : S et SP_m, soit (n/2) × (1 + k_P) épisodes ; mêmes sondes désignées (section 8,\n"
    "  précision 38) ; gains d'écart de la sonde et des juges calculés par les définitions du point 13 de la\n"
    "  « Métrique », lecture principale sur les champs seuls ; lignes rapportées par mode d'induction, celles du\n"
    "  présent texte gardant leurs critères et leurs verdicts.\n"
    "- **Ce que fixe le complément**, préenregistrement scellé et contre-lu avant l'ouverture de l'étape 2 : ce qui\n"
    "  dépend du verdict de G0 (l'organisme retenu et son empreinte ; plusieurs organismes ou plusieurs doses retenus :\n"
    "  une règle écrite au complément avant toute lecture ; aucun : nœud), les critères de lecture des lignes de ce\n"
    "  bras, ses gardes et son devis.\n"
    "Ce bras ne change aucune ligne de C-P1 à C-P6 du présent texte, n'entre dans aucune de ses corrections pour\n"
    "comparaisons multiples et ne lit aucune donnée avant le scellement de son complément ; son coût entre au devis de\n"
    "la piste C. Sans ce complément scellé et contre-lu, l'étape 2 ne s'ouvre pas : nœud (liste d'arrêt 24).",
)

remplace(
    "L-11", "Plan, section 8, précision 38, « Règle »", "CW-01 : source de la lettre suivie",
    "    **Règle** (lettre de la décision D-21 : « une sonde n'est désignée que si elle tient sur chaque famille et\n"
    "    chaque dose jugées »). Une sonde est **désignée**",
    "    **Règle** (lettre de la décision D-21, telle que la ligne d'accord l'écrit : « une sonde n'est désignée que si\n"
    "    elle tient sur chaque famille et chaque dose jugées » ; c'est l'option (a) soumise au directeur avant son mot,\n"
    "    liste des points ouverts v1,\n"
    f"    `{H_POINTS_V1}` : « au-dessus du plancher sur chaque\n"
    "    famille et à chaque dose que le verdict juge » ; la version 2 de cette liste, plus étroite, a été rendue\n"
    "    après ce mot et ne l'a pas remplacé). Une sonde est **désignée**",
)

remplace(
    "L-12", "liste d'arrêt 2", "CW-02 : renvoi à la garde 24",
    "   G0, GO de Lazar, GO sur le devis, ou addendum scellé et contre-lu : arrêt.",
    "   G0, GO de Lazar, GO sur le devis, ou addendum scellé et contre-lu : arrêt (complément du bras « saboteur sans\n"
    "   consigne » : garde 24).",
)

remplace(
    "L-13", "liste d'arrêt 24", "CW-02 : l'étape 2 ne s'ouvre pas",
    "    contre-lu à l'ouverture de l'étape 2 : nœud.",
    "    contre-lu à l'ouverture de l'étape 2 : l'étape 2 ne s'ouvre pas ; nœud (le directeur dit si elle s'ouvre sans\n"
    "    ce bras).",
)

remplace(
    "L-14", "section « Contre-lecture »", "vérification de la version c2 consignée ; vérification de la version c3 à faire",
    f"`{DOSSIER}/table-traitement-verification-c1-brouillon7-relance-v1.md`, dont cette version c2 est le résultat,\n"
    f"avec les décisions D-21, D-23 et D-24 du directeur ({GO}). Vérification de la version c2 par le même\n"
    "contre-lecteur, et chemins de versement : À REMPLIR par la session de conduite.\n",
    f"`{DOSSIER}/table-traitement-verification-c1-brouillon7-relance-v1.md`, dont la version c2\n"
    f"(`{EMPREINTE_SOURCE}`) est le résultat, avec les décisions D-21, D-23\n"
    f"et D-24 du directeur ({GO}).\n"
    "\n"
    "Vérification de la version c2 par le même contre-lecteur (le 2026-11-22) : rapport\n"
    f"`{VERIF}`,\n"
    f"`{H_VERIF}` ; le programme rejoué rend la version c2, aucun changement\n"
    "hors de sa table ; CV-01 à CV-03 levées ; rien de ce qui est tranché n'a bougé ; trois remarques neuves (CW-01,\n"
    "majeure ; CW-02 et CW-03, mineures), avis « scellable après corrections ». Traitement :\n"
    f"`{DOSSIER}/table-traitement-verification-c2-brouillon7-relance-v1.md`, dont cette version c3 est le résultat.\n"
    "Vérification de la version c3 par le même contre-lecteur, confirmation par la session de conduite de la lettre\n"
    "de la décision D-21, et chemins de versement : À REMPLIR par la session de conduite.\n",
)


def main():
    sortie, journal = Path(sys.argv[1]), Path(sys.argv[2])
    for p in (sortie, journal):
        if p.exists():
            sys.exit(f"refus d'écraser {p} (R12)")
    if sha(SOURCE) != EMPREINTE_SOURCE:
        sys.exit("source : empreinte inattendue")
    texte = SOURCE.read_text(encoding="utf-8")
    titres_avant = re.findall(r"^## .+$", texte, flags=re.M)
    marqueurs_avant = set(re.findall(r"<<[A-Z0-9_]+>>", texte))
    remplir_avant = texte.partition("\n## Contre-lecture\n")[0].count("À REMPLIR")
    h = lambda s: hashlib.sha256(s.encode("utf-8")).hexdigest()
    lignes = ["identifiant\tlieu\tremarque ou motif\tforme\tsignes retirés\tsignes écrits\tsha256 du fragment retiré\tsha256 du fragment écrit"]
    vus = set()
    for ident, lieu, motif, forme, a, b, nouveau in R:
        if ident in vus:
            sys.exit(f"{ident} : identifiant doublé")
        vus.add(ident)
        if texte.count(a) != 1:
            sys.exit(f"{ident} : début ou fragment trouvé {texte.count(a)} fois (attendu : 1)")
        if forme == "fragment":
            ancien = a
        else:
            i = texte.index(a)
            if texte.count(b, i) != 1:
                sys.exit(f"{ident} : fin trouvée {texte.count(b, i)} fois après le début (attendu : 1)")
            ancien = texte[i:texte.index(b, i) + len(b)]
        if ancien == nouveau:
            sys.exit(f"{ident} : remplacement vide")
        texte = texte.replace(ancien, nouveau, 1)
        lignes.append("\t".join([ident, lieu, motif, forme, str(len(ancien)), str(len(nouveau)), h(ancien), h(nouveau)]))
    if re.findall(r"^## .+$", texte, flags=re.M) != titres_avant:
        sys.exit("les titres de section ont changé")
    tete, _, contre_lecture = texte.partition("\n## Contre-lecture\n")
    if tete.count("À REMPLIR") != remplir_avant:
        sys.exit("« À REMPLIR » ajouté ou retiré hors de la section « Contre-lecture »")
    if contre_lecture.count("À REMPLIR") != 1:
        sys.exit("la section « Contre-lecture » doit porter un seul « À REMPLIR »")
    if set(re.findall(r"<<[A-Z0-9_]+>>", texte)) != marqueurs_avant:
        sys.exit("les marqueurs de gabarit ont changé")
    sortie.write_text(texte, encoding="utf-8")
    journal.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    print(f"{len(R)} remplacements ; sortie {sha(sortie)} ; {len(texte.encode('utf-8'))} octets")


if __name__ == "__main__":
    main()
