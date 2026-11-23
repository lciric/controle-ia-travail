"""Construit la version c4 du brouillon 7 de relance du préenregistrement du papier C : les deux remarques de la
vérification de la version c3 (rapport 265f62e7…, CX-01 et CX-02), par remplacements exacts sur la version c3.

Usage (depuis la racine du dépôt) :
    python3 registres/papier-c/redaction-brouillon7-relance-v1/travail/construire_brouillon7_relance_c4_v1.py SORTIE JOURNAL

Gardes : source à l'empreinte attendue ; chaque fragment trouvé une fois ; titres de section inchangés ; un seul
« À REMPLIR » dans la section « Contre-lecture », aucun ajouté ni retiré ailleurs ; marqueurs de gabarit inchangés.
Refuse d'écraser une sortie (R12).
"""
import hashlib
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[4]
SOURCE = RACINE / "brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22-c3.md"
EMPREINTE_SOURCE = "1da47502c8e49e3eb1078cd3cb0b31f035240d3f422a501557f8a3e5b6baf00c"
DOSSIER = "registres/papier-c/redaction-brouillon7-relance-v1"
VERIF = f"{DOSSIER}/contre-lecteur/rapport-verification-c3-et-devis-brouillon3-v1.md"
H_VERIF = "265f62e7cfada908e93aa0d1da3e1e7e90583107a04da46b23eab378cfc55b6e"


def sha(chemin):
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


assert sha(RACINE / VERIF) == H_VERIF
R = []


def remplace(ident, lieu, motif, ancien, nouveau):
    R.append((ident, lieu, motif, ancien, nouveau))


def ajoute(ident, lieu, motif, ancre, ajout):
    R.append((ident, lieu, motif, ancre, ancre + ajout))


remplace(
    "M-01", "titre", "version neuve (R12)",
    "version c3 (contre-lecture et deux vérifications traitées ; décisions D-21, D-23 et D-24 portées) : version r3 "
    "reprise",
    "version c4 (contre-lecture et trois vérifications traitées ; décisions D-21, D-23 et D-24 portées) : version r3 "
    "reprise",
)

remplace(
    "M-02", "en-tête, « État en bref »", "état après la vérification de la version c3",
    "aucune dépense : (1) la vérification, par le même contre-lecteur, des dernières corrections de cette version c3\n"
    "(verrou 7) ;",
    "aucune dépense : (1) la vérification, par le même contre-lecteur, des dernières corrections de cette version c4\n"
    "(verrou 7) ;",
)

ajoute(
    "M-03", "en-tête, « Nom (R12) »", "version neuve (R12)",
    "  vérification de c2 s'appelle « brouillon7-relance-2026-11-22-c3 ».",
    " La version qui traite la vérification de\n"
    "  c3 s'appelle « brouillon7-relance-2026-11-22-c4 ».",
)

remplace(
    "M-04", "en-tête, « Historique »", "R12 : la version c3 entre dans l'historique",
    "**Historique (R12).** Les brouillons précédents restent tels quels :\n"
    "- brouillon 7 de relance, version c2 (2026-11-22) :",
    "**Historique (R12).** Les brouillons précédents restent tels quels :\n"
    "- brouillon 7 de relance, version c3 (2026-11-22) :\n"
    "  `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22-c3.md`\n"
    f"  (`{EMPREINTE_SOURCE}`, 263 817 octets), vérifiée par le contre-lecteur\n"
    "  (section « Contre-lecture ») ; point de départ de cette version c4 ;\n"
    "- brouillon 7 de relance, version c2 (2026-11-22) :",
)

remplace(
    "M-05", "en-tête, « Historique »", "la version c2 est le point de départ de la version c3",
    "  (section « Contre-lecture ») ; point de départ de cette version c3 ;\n",
    "  (section « Contre-lecture ») ; point de départ de la version c3 ;\n",
)

remplace(
    "M-06", "en-tête, « Ce que change… »", "paragraphe neuf : ce que change la version c4",
    "**Ce que change la version c3 du brouillon 7 de relance** (2026-11-22). Une source :",
    "**Ce que change la version c4 du brouillon 7 de relance** (2026-11-22). Une source : la vérification de la\n"
    f"version c3 par le même contre-lecteur (rapport `{VERIF}`,\n"
    f"`{H_VERIF}` : CW-01 à CW-03 levées ; aucun changement hors table ;\n"
    "une remarque majeure et une mineure neuves, toutes deux sur le cadre du bras « saboteur sans consigne »). Ce\n"
    "cadre exige maintenant le même contexte des deux côtés du bras, consigne privée comprise, et laisse au complément\n"
    "le choix des cellules honnêtes qui le tiennent (CX-01) ; il demande au complément de dire ce qu'il fait de la\n"
    "différence qui reste, celle du modèle (ajout du rédacteur, à vérifier) ; il dit que les lignes de ce bras ne\n"
    "confirment ni ne réfutent rien au titre du présent texte, et ce que le complément peut en faire (CX-02). La\n"
    "session de conduite a confirmé la lettre de la décision D-21 que la précision 38 suit. Traitement :\n"
    f"`{DOSSIER}/table-traitement-verification-c3-brouillon7-relance-v1.md` ; table des remplacements :\n"
    f"`{DOSSIER}/note-differences-brouillon7-relance-c4-v1.md`. Aucun énoncé d'hypothèse, aucune prédiction, aucune\n"
    "marge, aucun seuil ne change ; aucune revendication n'est ajoutée.\n"
    "\n"
    "**Ce que change la version c3 du brouillon 7 de relance** (2026-11-22). Une source :",
)

remplace(
    "M-07", "verrou 1", "liste des points ouverts : erratum 1 (contexte égal du bras, coût possible)",
    "points-ouverts-pour-le-directeur-brouillon7-relance-v3.md`) : D-21",
    "points-ouverts-pour-le-directeur-brouillon7-relance-v3.md`, lue avec son erratum 1) : D-21",
)

remplace(
    "M-08", "verrou 7 (contre-lecture)", "vérification de la version c3 faite ; lettre de D-21 confirmée ; reste la vérification de c4",
    "**Reste** : la vérification de ces trois\n"
    "   corrections par ce même contre-lecteur, et la confirmation par la session de conduite de la lettre de la\n"
    "   décision D-21 (précision 38).",
    "Vérification de la version c3 faite par ce même contre-lecteur (rapport\n"
    f"   `{H_VERIF}` : CW-01 à CW-03 levées ; une majeure et une\n"
    "   mineure neuves, CX-01 et CX-02), que cette version c4 traite\n"
    "   (`table-traitement-verification-c3-brouillon7-relance-v1.md`). La session de conduite a confirmé la lettre de\n"
    "   la décision D-21 (message du 2026-11-22 à 19:29Z à la session du rédacteur : ce qui a été montré au directeur\n"
    "   est, mot pour mot, l'option (a) de la liste v1 ; à consigner à son registre). **Reste** : la vérification de\n"
    "   ces deux corrections par ce même contre-lecteur.",
)

remplace(
    "M-09", "verrou 8 (accord de dépense du pilote)", "devis en brouillon 4",
    f"   `{DOSSIER}/devis-pilote-papier-C-v1-brouillon3.md`.",
    f"   `{DOSSIER}/devis-pilote-papier-C-v1-brouillon4.md`.",
)

remplace(
    "M-10", "Plan, section 3, bras « saboteur sans consigne », cadre", "CX-01 : même contexte des deux côtés ; CX-02 : statut des lignes",
    "  l'ouverture de l'étape 2 ; honnête : le modèle de base, par les cellules H et HP_m du présent texte ; cellules\n"
    "  de plus, par organisme : S et SP_m, soit (n/2) × (1 + k_P) épisodes ; mêmes sondes désignées (section 8,\n"
    "  précision 38) ; gains d'écart de la sonde et des juges calculés par les définitions du point 13 de la\n"
    "  « Métrique », lecture principale sur les champs seuls ; lignes rapportées par mode d'induction, celles du\n"
    "  présent texte gardant leurs critères et leurs verdicts.\n",
    "  l'ouverture de l'étape 2 ; honnête : le modèle de base ; **même contexte des deux côtés** : dans ce bras, une\n"
    "  cellule honnête et la cellule du saboteur qui lui répond ont les mêmes consignes, consigne privée comprise, et\n"
    "  ne diffèrent que par le modèle qui écrit (sans cela une sonde pourrait lire une différence de consigne : le\n"
    "  défaut de la réserve 20, de l'autre côté) ; si l'organisme se lit sous la condition honnête du présent texte,\n"
    "  les cellules honnêtes sont H et HP_m, et les cellules de plus, par organisme, sont S et SP_m, soit\n"
    "  (n/2) × (1 + k_P) épisodes ; s'il ne se lit que sous un autre contexte (par exemple sans aucune consigne\n"
    "  privée), les cellules honnêtes sont générées sous ce contexte elles aussi : s'y ajoutent, une fois par\n"
    "  contexte, (n/2) × (1 + k_P) épisodes honnêtes ; mêmes sondes désignées (section 8, précision 38) ; gains\n"
    "  d'écart de la sonde et des juges calculés par les définitions du point 13 de la « Métrique », lecture\n"
    "  principale sur les champs seuls ; lignes rapportées par mode d'induction : au titre du présent texte, elles ne\n"
    "  confirment ni ne réfutent rien, et les lignes du présent texte gardent leurs critères et leurs verdicts.\n",
)

remplace(
    "M-11", "Plan, section 3, bras « saboteur sans consigne », ce que fixe le complément", "CX-01, CX-02 ; ajout du rédacteur : différence de modèle",
    "  une règle écrite au complément avant toute lecture ; aucun : nœud), les critères de lecture des lignes de ce\n"
    "  bras, ses gardes et son devis.\n",
    "  une règle écrite au complément avant toute lecture ; aucun : nœud) ; le contexte commun aux deux côtés du bras,\n"
    "  donc les cellules honnêtes (celles du présent texte, ou des cellules neuves) ; ce qu'il fait de la différence\n"
    "  qui reste entre les deux côtés, celle du modèle, qui porte à la fois le sabotage et l'entraînement de\n"
    "  l'organisme (un modèle honnête entraîné de la même façon, s'il en existe un, lu à côté ; sinon une réserve\n"
    "  écrite sur ces lignes) ; ses gardes et son devis ; et, s'il leur en donne, des critères de lecture propres aux\n"
    "  lignes de ce bras, dont l'issue s'écrit alors « sur saboteur sans consigne » et ne remplace jamais une ligne du\n"
    "  présent texte.\n",
)

remplace(
    "M-12", "section « Contre-lecture »", "vérification de la version c3 consignée ; vérification de la version c4 à faire",
    f"`{DOSSIER}/table-traitement-verification-c2-brouillon7-relance-v1.md`, dont cette version c3 est le résultat.\n"
    "Vérification de la version c3 par le même contre-lecteur, confirmation par la session de conduite de la lettre\n"
    "de la décision D-21, et chemins de versement : À REMPLIR par la session de conduite.\n",
    f"`{DOSSIER}/table-traitement-verification-c2-brouillon7-relance-v1.md`, dont la version c3\n"
    f"(`{EMPREINTE_SOURCE}`) est le résultat.\n"
    "\n"
    "Vérification de la version c3 par le même contre-lecteur (le 2026-11-22) : rapport\n"
    f"`{VERIF}`,\n"
    f"`{H_VERIF}` ; le programme rejoué rend la version c3, aucun changement\n"
    "hors de sa table ; CW-01 à CW-03 levées (pour CW-01 : la lettre de la décision D-21 suivie par le texte est celle\n"
    "de la ligne d'accord, confirmée par la session de conduite) ; rien de ce qui est tranché n'a bougé ; deux\n"
    "remarques neuves (CX-01, majeure ; CX-02, mineure), avis « scellable après corrections ». Traitement :\n"
    f"`{DOSSIER}/table-traitement-verification-c3-brouillon7-relance-v1.md`, dont cette version c4 est le résultat.\n"
    "Vérification de la version c4 par le même contre-lecteur, et chemins de versement : À REMPLIR par la session de\n"
    "conduite.\n",
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
    lignes = ["identifiant\tlieu\tremarque ou motif\tsignes retirés\tsignes écrits\tsha256 du fragment retiré\tsha256 du fragment écrit"]
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
    if set(re.findall(r"<<[A-Z0-9_]+>>", texte)) != marqueurs_avant:
        sys.exit("les marqueurs de gabarit ont changé")
    sortie.write_text(texte, encoding="utf-8")
    journal.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    print(f"{len(R)} remplacements ; sortie {sha(sortie)} ; {len(texte.encode('utf-8'))} octets")


if __name__ == "__main__":
    main()
