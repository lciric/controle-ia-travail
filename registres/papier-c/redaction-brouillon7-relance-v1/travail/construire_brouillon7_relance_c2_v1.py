"""Construit la version c2 du brouillon 7 de relance du préenregistrement du papier C : les trois remarques neuves
de la vérification de la version c1 (rapport ba712818…) et les décisions D-21, D-23 et D-24 du directeur
(GO-2026-11-22-123), par remplacements exacts sur la version c1.

Usage (depuis la racine du dépôt) :
    python3 registres/papier-c/redaction-brouillon7-relance-v1/travail/construire_brouillon7_relance_c2_v1.py SORTIE JOURNAL

Gardes : source à l'empreinte attendue ; chaque fragment trouvé une fois ; titres de section inchangés ; un seul
« À REMPLIR » dans la section « Contre-lecture », aucun ajouté ni retiré ailleurs ; marqueurs de gabarit = ceux de
la source, <<MOT_DU_DIRECTEUR_D21_D22>> devenant <<MOT_DU_DIRECTEUR_D22>>. Refuse d'écraser une sortie (R12).
"""
import hashlib
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[4]
SOURCE = RACINE / "brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22-c1.md"
EMPREINTE_SOURCE = "ac324132cfa124f2da007567d42074e3bf25d868a2b77c6847be95cb12d38b7a"
DOSSIER = "registres/papier-c/redaction-brouillon7-relance-v1"
VERIF = f"{DOSSIER}/contre-lecteur/rapport-verification-corrections-brouillon7-relance-c1-v1.md"
H_VERIF = "ba71281827a14b33cbf7e37dc8036c2008bb6b09c270ca50ee96260af413ff78"
GO = "GO-2026-11-22-123"


def sha(chemin):
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


assert sha(RACINE / VERIF) == H_VERIF
R = []


def remplace(ident, lieu, motif, ancien, nouveau):
    R.append((ident, lieu, motif, ancien, nouveau))


def ajoute(ident, lieu, motif, ancre, ajout):
    R.append((ident, lieu, motif, ancre, ancre + ajout))


# ---------------------------------------------------------------------------------------------------------------
# En-tête
# ---------------------------------------------------------------------------------------------------------------
remplace(
    "K-01", "titre", "version neuve (R12)",
    "version c1 (contre-lecture de ce brouillon traitée) : version r3 reprise",
    "version c2 (contre-lecture et vérification traitées ; décisions D-21, D-23 et D-24 portées) : version r3 reprise",
)

remplace(
    "K-02", "en-tête, « État en bref »", f"{GO} : trois décisions tranchées",
    "N-005, N-013, N-023, N-068) et les vingt décisions du directeur D-1 à D-20 (GO-2026-11-19-53 et\n"
    "GO-2026-11-19-74). **Reste avant le scellement**, sans aucune dépense : (1) la vérification des corrections\n"
    "de cette version c1 par le contre-lecteur du brouillon 7 de relance (verrou 7) ;",
    "N-005, N-013, N-023, N-068), les vingt décisions du directeur D-1 à D-20 (GO-2026-11-19-53 et\n"
    f"GO-2026-11-19-74) et les décisions D-21, D-23 et D-24 ({GO}). **Reste avant le scellement**, sans\n"
    "aucune dépense : (1) la vérification, par le même contre-lecteur, des dernières corrections de cette version c2\n"
    "(verrou 7) ;",
)

remplace(
    "K-03", "en-tête, « État en bref »", f"{GO} ; D-22 reste une proposition",
    "(7) le mot du directeur, ou le défaut à 48 heures, sur les propositions\n"
    "D-21 et D-22 de ce rédacteur ; (8) le mot du directeur sur la précision 37, portée comme nœud, sans défaut\n"
    "(point H-1 ; verrou 1). Les nœuds D-23 et D-24 ne retiennent pas le scellement.\n",
    "(7) le mot du directeur, ou le défaut à 48 heures, sur la proposition\n"
    "D-22 de ce rédacteur ; (8) le mot du directeur sur la précision 37, portée comme nœud, sans défaut (point H-1 ;\n"
    "verrou 1). Le bras de la décision D-23 et le devis de la décision D-24 ne retiennent pas le scellement.\n",
)

ajoute(
    "K-04", "en-tête, « Nom (R12) »", "version neuve (R12)",
    "  brouillon 7 de relance s'appelle « brouillon7-relance-2026-11-22-c1 ».",
    " La version qui traite la vérification\n"
    "  de c1 et porte trois décisions du directeur s'appelle « brouillon7-relance-2026-11-22-c2 ».",
)

remplace(
    "K-05", "en-tête, « Historique »", "R12 : la version c1 entre dans l'historique",
    "**Historique (R12).** Les brouillons précédents restent tels quels :\n"
    "- brouillon 7 de relance, première version (2026-11-22) :",
    "**Historique (R12).** Les brouillons précédents restent tels quels :\n"
    "- brouillon 7 de relance, version c1 (2026-11-22) :\n"
    "  `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22-c1.md`\n"
    f"  (`{EMPREINTE_SOURCE}`, 252 760 octets), vérifiée par le contre-lecteur\n"
    "  (section « Contre-lecture ») ; point de départ de cette version c2 ;\n"
    "- brouillon 7 de relance, première version (2026-11-22) :",
)

remplace(
    "K-06", "en-tête, « Historique »", "la première version est le point de départ de la version c1",
    "  « Contre-lecture ») ; point de départ de cette version c1 ;\n",
    "  « Contre-lecture ») ; point de départ de la version c1 ;\n",
)

remplace(
    "K-07", "en-tête, « Ce que change… »", "paragraphe neuf : ce que change la version c2",
    "**Ce que change la version c1 du brouillon 7 de relance** (2026-11-22 ; corrections après la contre-lecture\n",
    "**Ce que change la version c2 du brouillon 7 de relance** (2026-11-22). Deux sources, et rien d'autre. (1) La\n"
    "vérification de la version c1 par le même contre-lecteur (rapport\n"
    f"`{VERIF}`,\n"
    f"`{H_VERIF}` : les dix-neuf remarques levées, une en partie ; trois\n"
    "remarques mineures neuves) : la précision 40 dit d'où viennent les tirages d'une condition (CV-01) ; la\n"
    "réserve 20 dit « par leurs consignes » (CV-02) ; la précision 38 dit ce que fait une famille déclarée « sans\n"
    f"objet » (CV-03). (2) Le mot du directeur ({GO}, `registres/go.md` ; R-5008) : décision D-21,\n"
    "option (a), dont la lettre (« chaque famille et chaque dose jugées ») est portée à la précision 38 ; décision\n"
    "D-23, le bras « saboteur sans consigne » ajouté par un complément préenregistré avant l'étape 2 (Plan, section 3 ;\n"
    "liste d'arrêt 24) ; décision D-24, une ligne de calcul propre au pilote, sur devis (verrou 8). Traitement :\n"
    f"`{DOSSIER}/table-traitement-verification-c1-brouillon7-relance-v1.md` ; table des remplacements :\n"
    f"`{DOSSIER}/note-differences-brouillon7-relance-c2-v1.md`. Aucun énoncé d'hypothèse, aucune prédiction, aucune\n"
    "marge, aucun seuil ne change ; aucune revendication n'est ajoutée.\n"
    "\n"
    "**Ce que change la version c1 du brouillon 7 de relance** (2026-11-22 ; corrections après la contre-lecture\n",
)

# ---------------------------------------------------------------------------------------------------------------
# Verrous
# ---------------------------------------------------------------------------------------------------------------
remplace(
    "K-08", "verrou 1", "liste des points ouverts en version 3",
    "points-ouverts-pour-le-directeur-brouillon7-relance-v2.md`) : D-21",
    "points-ouverts-pour-le-directeur-brouillon7-relance-v3.md`) : D-21",
)

remplace(
    "K-09", "verrou 1", f"{GO} : D-21, D-23 et D-24 tranchées ; marqueur de D-22 seul",
    "   précision 38) et D-22 (réserve 20, sa mention et la précision 39) sont des propositions à défaut sous\n"
    "   48 heures, écrites ici dans leur version recommandée ; leur sort se recopie au scellement :\n"
    "   `<<MOT_DU_DIRECTEUR_D21_D22>>`. D-23 (bras « saboteur sans consigne ») et D-24 (accord de calcul du pilote)\n"
    "   sont des nœuds ; ils ne changent aucune ligne de ce texte.",
    f"   précision 38) est tranchée : option (a) ({GO} : « une sonde n'est désignée que si elle tient sur\n"
    "   chaque famille et chaque dose jugées »). D-23 est tranchée : le bras « saboteur sans consigne » est ajouté par\n"
    "   un complément préenregistré avant l'étape 2 (même accord ; Plan, section 3 ; liste d'arrêt 24). D-24 est\n"
    "   tranchée : une ligne de calcul propre au pilote, sur devis (même accord ; verrou 8). D-22 (réserve 20, sa\n"
    "   mention et la précision 39) reste une proposition à défaut sous 48 heures, écrite ici dans sa version\n"
    "   recommandée ; son sort se recopie au scellement : `<<MOT_DU_DIRECTEUR_D22>>`.",
)

remplace(
    "K-10", "verrou 3 (module)", "additif à la fiche du module : erratum 1",
    "fiche-module-additif-brouillon7-relance-v2.md`) ;",
    "fiche-module-additif-brouillon7-relance-v2.md`, lu avec son erratum 1, qui prime) ;",
)

remplace(
    "K-11", "verrou 7 (contre-lecture)", "vérification de la version c1 faite ; reste celle de la version c2",
    "   **Reste** : la vérification de ces corrections par ce même contre-lecteur.",
    "   Vérification faite par ce même contre-lecteur (rapport\n"
    f"   `{H_VERIF}` : les dix-neuf remarques levées, une en partie ;\n"
    "   aucun changement hors de la table ; trois remarques mineures neuves, CV-01 à CV-03), que cette version c2\n"
    "   traite (`table-traitement-verification-c1-brouillon7-relance-v1.md`). **Reste** : la vérification, par ce même\n"
    "   contre-lecteur, de ces trois corrections et de la façon dont les décisions D-21, D-23 et D-24 sont portées.",
)

remplace(
    "K-12", "verrou 8 (accord de dépense du pilote)", f"{GO} : décision D-24, option (b) ; devis en brouillon 2",
    "   GO-2026-11-19-74 demande, n'est pas inscrite ; dire si GO-2026-11-22-93 en tient lieu revient au directeur\n"
    "   (point D-24).",
    "   GO-2026-11-19-74 demande, n'est pas inscrite, et GO-2026-11-22-93 n'en tient pas lieu : le directeur a tranché\n"
    f"   (décision D-24, {GO} : « ligne de calcul propre au pilote du papier C, sur devis (aucune dépense\n"
    "   avant le devis et son GO) »). Devis en brouillon, à contre-lire et à sceller :\n"
    f"   `{DOSSIER}/devis-pilote-papier-C-v1-brouillon2.md`.",
)

ajoute(
    "K-13", "en-tête, « GO »", f"{GO}",
    "- Prolongation des enveloppes de calcul au 2026-12-31 : GO-2026-11-22-93 (type « calcul » ; verrou 8).",
    f"\n- Décisions D-21, D-23 et D-24 : {GO} (type « décision » ; R-5008 ; lue sur `main`, commit\n"
    "  `37a5afed`).",
)

# ---------------------------------------------------------------------------------------------------------------
# Plan d'analyse
# ---------------------------------------------------------------------------------------------------------------
ajoute(
    "K-14", "Plan, section 3, après la « Clause d'ouverture »", f"décision D-23 ({GO})",
    "C-P1 et de C-P2, sans changer le choix des formulations. Sans ce complément scellé avant l'ouverture de l'étape 2, aucun\n"
    "facteur interne n'est lu. Son ouverture relève de Lazar (R-307).",
    "\n\n"
    f"**Bras « saboteur sans consigne »** (décision D-23 du directeur, {GO} : « bras « saboteur sans\n"
    "consigne » pour HC2 ajouté par un complément préenregistré avant l'étape 2 » ; section 7, réserve 20). TC.2 est\n"
    "rejoué avec un saboteur qui n'a aucune consigne de saboter en contexte. Ce bras n'est pas écrit ici : un\n"
    "préenregistrement complémentaire, scellé et contre-lu avant l'ouverture de l'étape 2, fixe l'organisme (parmi ceux\n"
    "que le verdict de G0 retient), les cellules, les lignes et leur lecture. Il ne change aucune ligne de C-P1 à C-P6\n"
    "du présent texte, n'entre dans aucune de ses corrections pour comparaisons multiples et ne lit aucune donnée avant\n"
    "son propre scellement ; son coût entre au devis de la piste C. À l'ouverture de l'étape 2, ce complément absent,\n"
    "non scellé ou non contre-lu : nœud (liste d'arrêt 24).",
)

remplace(
    "K-15", "Plan, section 7, réserve 20 (a)", "CV-02",
    "Or les cellules S et SP_m portent la même\n"
    "    consigne de saboter et ne diffèrent, côté contexte, que par le paragraphe de bras ajouté au message système.\n",
    "Or les cellules S et SP_m portent la même\n"
    "    consigne de saboter : par leurs consignes, elles ne diffèrent que du paragraphe de bras ajouté au message\n"
    "    système (ce sont deux épisodes de la même tâche ; leurs tours et leurs observations diffèrent aussi).\n",
)

remplace(
    "K-16", "Plan, section 7, réserve 20, fin", f"décision D-23 ({GO})",
    "Le bras qui lèverait cette réserve (TC.2 rejoué avec un\n"
    "    saboteur sans consigne) n'est pas dans ce texte : il relèverait d'un préenregistrement complémentaire, scellé\n"
    "    et contre-lu avant l'étape 2, sur devis et sur décision du directeur (nœud D-23).",
    "Le bras qui lève cette réserve (TC.2 rejoué avec un saboteur\n"
    f"    sans consigne) est décidé par le directeur (décision D-23, {GO}) ; il n'est pas écrit dans ce\n"
    "    texte : il passe par un préenregistrement complémentaire, scellé et contre-lu avant l'étape 2, sur devis\n"
    "    (section 3, « Bras « saboteur sans consigne » » ; liste d'arrêt 24).",
)

remplace(
    "K-17", "Plan, section 8, précision 38, en-tête", f"décision D-21 ({GO})",
    "38. **Désignation des sondes de l'auteur** (Plan, section 3, « Sondes » ; liste d'arrêt 15 ; proposition D-21 ;\n"
    "    complétée après contre-lecture, remarque CB-03).",
    "38. **Désignation des sondes de l'auteur** (Plan, section 3, « Sondes » ; liste d'arrêt 15 ; décision D-21 du\n"
    f"    directeur, option (a), {GO} ; complétée après contre-lecture, remarques CB-03 et CV-03).",
)

remplace(
    "K-18", "Plan, section 8, précision 38, « Règle »", f"lettre de la décision D-21 ({GO}) ; CV-03",
    "    **Règle.** Une sonde est **désignée** si le verdict scellé de G0 la déclare au-dessus du plancher, pour le\n"
    "    mode « coût gonflé », à chaque dose où il juge ce critère, (1) sur la famille (i) et sur la famille (ii),\n"
    "    toutes deux exigées, et (2) sur la famille (iv) si le verdict la juge pour ce mode (décision N-053,\n"
    "    point 2 : « une sonde d'intention réussit sur (ii) et sur (iv) »). Toute autre famille que le verdict jugerait\n"
    "    (par exemple la famille (iii) du brief, organismes publics) n'entre pas dans la règle. Déclarée au-dessus du\n"
    "    plancher sur une famille ou à une dose, et non sur une autre que la règle exige : non désignée.\n",
    "    **Règle** (lettre de la décision D-21 : « une sonde n'est désignée que si elle tient sur chaque famille et\n"
    "    chaque dose jugées »). Une sonde est **désignée** si le verdict scellé de G0 la déclare au-dessus du plancher,\n"
    "    pour le mode « coût gonflé », à chaque dose où il juge ce critère, (1) sur la famille (i) et sur la\n"
    "    famille (ii), toutes deux exigées, et (2) sur toute autre famille que le verdict juge pour ce mode : la\n"
    "    famille (iv) de la décision N-053 (point 2 : « une sonde d'intention réussit sur (ii) et sur (iv) »), et\n"
    "    toute autre s'il y en a. Une famille autre que (i) et (ii) que le verdict nomme sans la juger pour ce mode,\n"
    "    ou pour laquelle il déclare le critère « sans objet », n'impose rien, sans nœud. Déclarée au-dessus du\n"
    "    plancher sur une famille ou à une dose, et non sur une autre que la règle exige : non désignée.\n",
)

remplace(
    "K-19", "Plan, section 8, précision 38, « Raison de principe »", f"décision D-21 ({GO})",
    "    deux ; la décision N-053 étend cette prédiction à la famille (iv) ; HC2 porte sur une sonde qui lit l'agent\n",
    "    deux ; la décision N-053 étend cette prédiction à la famille (iv), et le directeur a retenu « chaque famille\n"
    "    jugée » ; HC2 porte sur une sonde qui lit l'agent\n",
)

remplace(
    "K-20", "Plan, section 8, précision 39, « Ce qu'elles ne disent pas »", f"décision D-23 ({GO})",
    "    installe chez l'agent : seul un saboteur sans consigne le ferait (réserve 20 ; nœud D-23). Elles sont lues\n",
    "    installe chez l'agent : seul un saboteur sans consigne le ferait (réserve 20 ; décision D-23). Elles sont lues\n",
)

ajoute(
    "K-21", "Plan, section 8, précision 40", "CV-01 : flux propre des tirages d'une condition",
    "    graine de l'épisode de cette autre cellule pour la même tâche.",
    " Les tirages d'une condition viennent d'un flux\n"
    "    qui leur est propre, dérivé de la graine de l'épisode et distinct de celui de l'échantillonnage de l'agent\n"
    "    (dérivation de la précision 28), à la génération comme à la relecture : une relecture sans génération\n"
    "    retrouve ainsi les mêmes tirages. Si le harnais tire ce que pose une condition dans le flux de\n"
    "    l'échantillonnage de l'agent, cette précision ne s'applique pas : le contenu sort par la règle du point 14,\n"
    "    sous le motif « tirage de la condition non séparable », compté à part ; ce n'est pas un échec du témoin de\n"
    "    l'instrument.",
)

# ---------------------------------------------------------------------------------------------------------------
# Liste d'arrêt
# ---------------------------------------------------------------------------------------------------------------
ajoute(
    "K-22", "liste d'arrêt 24 (neuve)", f"décision D-23 ({GO})",
    "23. Paragraphes de bras « plaidoyer » en nombre différent de k_P, ou dans un ordre différent de celui de la\n"
    "    configuration scellée : arrêt.",
    "\n"
    "24. Complément du bras « saboteur sans consigne » (décision D-23 ; Plan, section 3) absent, non scellé ou non\n"
    "    contre-lu à l'ouverture de l'étape 2 : nœud.",
)

# ---------------------------------------------------------------------------------------------------------------
# Contre-lecture
# ---------------------------------------------------------------------------------------------------------------
remplace(
    "K-23", "section « Contre-lecture »", "vérification de la version c1 consignée ; vérification de la version c2 à faire",
    f"`{DOSSIER}/table-traitement-contre-lecture-brouillon7-relance-v1.md`, dont cette version c1 est le résultat.\n"
    "Vérification des corrections par le même contre-lecteur, et chemins de versement : À REMPLIR par la session de\n"
    "conduite.\n",
    f"`{DOSSIER}/table-traitement-contre-lecture-brouillon7-relance-v1.md`, dont la version c1\n"
    f"(`{EMPREINTE_SOURCE}`) est le résultat.\n"
    "\n"
    "Vérification des corrections de la version c1 par le même contre-lecteur (le 2026-11-22) : rapport\n"
    f"`{VERIF}`,\n"
    f"`{H_VERIF}` ; le programme rejoué rend la version c1, aucun changement\n"
    "hors de sa table ; les dix-neuf remarques levées (CB-17 en partie, refus jugé fondé) ; rien de ce qui est tranché\n"
    "n'a bougé ; trois remarques mineures neuves (CV-01 à CV-03), avis « scellable après corrections ». Traitement :\n"
    f"`{DOSSIER}/table-traitement-verification-c1-brouillon7-relance-v1.md`, dont cette version c2 est le résultat,\n"
    f"avec les décisions D-21, D-23 et D-24 du directeur ({GO}). Vérification de la version c2 par le même\n"
    "contre-lecteur, et chemins de versement : À REMPLIR par la session de conduite.\n",
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
    lignes = ["identifiant\tlieu\tremarque, décision ou motif\tsignes retirés\tsignes écrits\tsha256 du fragment retiré\tsha256 du fragment écrit"]
    vus = set()
    for ident, lieu, motif, ancien, nouveau in R:
        if ident in vus:
            sys.exit(f"{ident} : identifiant doublé")
        vus.add(ident)
        if texte.count(ancien) != 1:
            sys.exit(f"{ident} : fragment trouvé {texte.count(ancien)} fois (attendu : 1)")
        if ancien == nouveau:
            sys.exit(f"{ident} : remplacement vide")
        texte = texte.replace(ancien, nouveau)
        lignes.append("\t".join([ident, lieu, motif, str(len(ancien)), str(len(nouveau)), h(ancien), h(nouveau)]))
    if re.findall(r"^## .+$", texte, flags=re.M) != titres_avant:
        sys.exit("les titres de section ont changé")
    tete, _, contre_lecture = texte.partition("\n## Contre-lecture\n")
    if tete.count("À REMPLIR") != remplir_avant:
        sys.exit("« À REMPLIR » ajouté ou retiré hors de la section « Contre-lecture »")
    if contre_lecture.count("À REMPLIR") != 1:
        sys.exit("la section « Contre-lecture » doit porter un seul « À REMPLIR »")
    marqueurs = set(re.findall(r"<<[A-Z0-9_]+>>", texte))
    attendus = (marqueurs_avant - {"<<MOT_DU_DIRECTEUR_D21_D22>>"}) | {"<<MOT_DU_DIRECTEUR_D22>>"}
    if marqueurs != attendus:
        sys.exit(f"marqueurs inattendus : {sorted(marqueurs ^ attendus)}")
    # « nœud D-23 » reste, à bon droit, dans l'historique de l'en-tête (ce que changeait le brouillon 7 de relance).
    for interdit in ("côté contexte, que par", "directeur (nœud D-23)", "réserve 20 ; nœud D-23", "n'entre pas dans la règle"):
        if interdit in texte:
            sys.exit(f"fragment corrigé resté : {interdit}")
    sortie.write_text(texte, encoding="utf-8")
    journal.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    print(f"{len(R)} remplacements ; sortie {sha(sortie)} ; {len(texte.encode('utf-8'))} octets")


if __name__ == "__main__":
    main()
