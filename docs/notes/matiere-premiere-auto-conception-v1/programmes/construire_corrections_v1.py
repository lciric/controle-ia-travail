#!/usr/bin/env python3
"""Construit programmes/corrections-v1.json : la table explicite des corrections 2 à 10 de la
contre-lecture (docs/notes/matiere-premiere-auto-conception-v1/contre-lecture-matiere-premiere-v1.md, section 6).
Chaque ligne : indice, mecanisme (position dans le lot d'origine, ou null pour un champ de l'entrée),
operation, champ, avant, apres, raison, correction (numéro de la section 6). Les « avant » sont
revérifiés par fusionner_v1.py (arrêt si un « avant » ne correspond pas : R5).
Usage (depuis docs/notes/matiere-premiere-auto-conception-v1) : python programmes/construire_corrections_v1.py"""
import glob, hashlib, json, re
from pathlib import Path

RACINE = Path(__file__).resolve().parents[4]
LOTS = []
for f in sorted(glob.glob("lots/lot-*.json")):
    if f.endswith("lot-21.json"):
        continue  # le lot 21 applique les corrections d'emblée
    LOTS += json.loads(Path(f).read_text(encoding="utf-8"))
TABLE = json.loads((RACINE / "docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json").read_text(encoding="utf-8"))["travaux"]
R = {r["indice"]: r for r in LOTS}
C = []

def ligne(corr, i, pos, op, champ, avant, apres, raison):
    C.append(dict(correction=corr, indice=i, mecanisme=pos, operation=op, champ=champ, avant=avant, apres=apres, raison=raison))

def sha(chemin):
    return hashlib.sha256((RACINE / chemin).read_bytes()).hexdigest()

# ---- 2 : profondeur de lecture -------------------------------------------------------------
for r in LOTS:
    lu = re.sub(r"\s*\(.*\)", "", TABLE[r["indice"]]["lu"])
    if lu == "résumé ou page" and r["profondeur_de_lecture"] == "notice seule":
        ligne(2, r["indice"], None, "modifier", "profondeur_de_lecture", "notice seule", "page ou résumé",
              "la table note l'entrée « résumé ou page » ; l'étiquette « notice seule » est réservée aux entrées dont la table ne porte que le titre")
r = R[258]
ligne(2, 258, None, "modifier", "profondeur_de_lecture", "lecture approfondie sur PDF", "page ou résumé",
      "la précision du lot dit « pages 1 à 3 relues, aucune note de lecture approfondie au dépôt » : page ou résumé, PDF public pages 1 à 3 ; la pièce privée n'est pas citée")

# ---- 3 : mécanismes suggérés par le titre ----------------------------------------------------
RX = re.compile(r"seul titre|d.après le titre|suggér", re.I)
for r in LOTS:
    for k, m in enumerate(r["mecanismes"]):
        if RX.search(m["mecanisme_en_une_phrase"]):
            ligne(3, r["indice"], k, "ajouter_champ", "suggere_par_le_titre", None, True,
                  "le texte du mécanisme dit qu'il est suggéré par le seul titre ou d'après le titre : à compter à part, jamais additionné aux mécanismes décrits")

# ---- 4 : familles « autre » reclassées ou justifiées ----------------------------------------
RECLASSE = {  # (indice, position): (famille après, raison)
    (48, 1): ("exploration", "composition de l'organisme comme variable de la diversité des propositions (diversité d'exploration)"),
    (105, 0): ("exploration", "modèles du monde co-évoluant avec la recherche pour anticiper : orientation de l'exploration"),
    (146, 0): ("exploration", "modèle des trajectoires réelles d'idéation : description du cheminement d'exploration des idées"),
    (186, 1): ("épreuve", "stabilité d'un run à l'autre : axe d'évaluation, donc mesure de l'épreuve"),
    (485, 0): ("jugement", "affirmation sur ce qu'un juge ou un sélecteur d'idées peut porter d'un domaine à un autre : jugement du goût"),
    (509, 0): ("exploration", "modèle de la dynamique d'exploration d'un collectif d'agents"),
    (535, 0): ("exploration", "guidage de la boucle de recherche par les comportements en tension"),
    (543, 2): ("exploration", "nombre et isolement des états de recherche comme variables de la diversité d'exploration"),
    (570, 1): ("jugement", "mesure de l'homogénéité d'un collège de juges modèles"),
}
JUSTIF = {
    "gouvernance": "reste « autre » : organisation et gouvernance d'un collectif, texte de position sans mécanisme d'idéation, d'épreuve ou de jugement",
    "integrite": "reste « autre » : intégrité ou traçabilité du compte rendu (provenance des nombres, audit), hors des huit familles de recherche, de jugement et d'épreuve des idées",
    "entrainement": "reste « autre » : entraînement des agents (récompense, terrain d'entraînement), ni l'épreuve des idées ni leur sélection",
    "bibliographie": "reste « autre » : porte d'entrée bibliographique, vocabulaire ou cartographie, aucun mécanisme propre",
    "diagnostic": "reste « autre » : diagnostic ou mesure descriptive sur des agents de recherche, pas un mécanisme que l'organisme assemble",
    "systeme": "reste « autre » : système complet dont la notice ne précise pas le mécanisme ; classé d'après le titre ; famille non déterminable",
    "environnement": "reste « autre » : aménagement de l'environnement de l'agent, dont la notice ne précise pas le contenu",
    "representation": "reste « autre » : représentation ou prédiction des idées et découvertes, lien aux huit familles non confirmé (titre seul)",
    "supervision": "reste « autre » : supervision humaine d'un système autonome (tableau de bord), hors des huit familles",
    "redaction": "reste « autre » : rédaction automatique, séparée de la découverte",
    "agregation": "reste « autre » : agrégation statistique de modèles candidats, lien à l'idéation indirect selon le lot",
}
GRP = {132: "gouvernance", 153: "integrite", 175: "entrainement", 201: "integrite", 202: "integrite", 203: "integrite",
       207: "entrainement", 219: "bibliographie", 221: "bibliographie", 225: "environnement", 226: "bibliographie",
       266: "systeme", 267: "systeme", 268: "systeme", 269: "systeme", 335: "systeme", 336: "systeme", 337: "systeme",
       346: "diagnostic", 348: "supervision", 352: "systeme", 359: "diagnostic", 364: "representation", 387: "representation",
       394: "redaction", 451: "agregation", 457: "bibliographie", 465: "bibliographie", 489: "integrite", 519: "entrainement"}
for r in LOTS:
    for k, m in enumerate(r["mecanismes"]):
        if m["famille"] != "autre":
            continue
        cle = (r["indice"], k)
        if cle in RECLASSE:
            ligne(4, r["indice"], k, "modifier", "famille", "autre", RECLASSE[cle][0], RECLASSE[cle][1])
        elif r["indice"] == 259 and k == 4:
            ligne(4, 259, 4, "retirer_mecanisme", "mecanisme", m["mecanisme_en_une_phrase"], None,
                  "la ligne signale des « triches à la récompense » dont le contenu relève de la famille cloisonnée (attaque du juge) : retirée, notée « exclue » seulement (voir correction 6)")
        else:
            ligne(4, r["indice"], k, "ajouter_champ", "justification_autre", None, JUSTIF[GRP[r["indice"]]],
                  "famille « autre » conservée avec justification explicite")

# ---- 5 : gloses non sourcées -------------------------------------------------------------------
def txt(i, k):
    return R[i]["mecanismes"][k]["mecanisme_en_une_phrase"]
a = txt(45, 0)
ligne(5, 45, 0, "modifier", "mecanisme_en_une_phrase", a, a.replace(", non d'un manque de température", ""),
      "« non d'un manque de température » n'est ni dans l'entrée de la table ni dans les lignes de veille citées")
a = txt(173, 0)
ligne(5, 173, 0, "modifier", "mecanisme_en_une_phrase", a,
      "Découverte active de lois d'échelle par agents, seconde version d'un banc existant (d'après le titre et la notice de la table) ; le choix des mesures demandées avant d'énoncer la loi est une lecture du mot « active » du titre, non une affirmation de la notice ; notation non précisée par la notice.",
      "la phrase d'origine présentait comme description un contenu tiré du titre")
ligne(5, 173, 0, "ajouter_champ", "suggere_par_le_titre", None, True, "contenu tiré du titre")
a = txt(173, 1)
ligne(5, 173, 1, "modifier", "mecanisme_en_une_phrase", a,
      "Lecture du relevé d'après le titre (« active ») : un banc actif laisserait supposer une économie de mesures ; la notice ne précise ni budget ni mécanisme de coût.",
      "la phrase d'origine présentait une déduction du titre comme description")
ligne(5, 173, 1, "ajouter_champ", "suggere_par_le_titre", None, True, "contenu tiré du titre")
a = txt(403, 0)
ligne(5, 403, 0, "modifier", "mecanisme_en_une_phrase", a,
      a.replace("; argument pour des proposeurs hétérogènes.", "(lecture du relevé, non affirmation des auteurs : ce résultat plaiderait pour des proposeurs hétérogènes)."),
      "« argument pour des proposeurs hétérogènes » est une lecture du relevé, à marquer comme telle")
a = txt(439, 0)
ligne(5, 439, 0, "modifier", "mecanisme_en_une_phrase", a, a.replace("; la correction est appliquée après coup (", " (", 1),
      "« la correction est appliquée après coup » n'est dans aucune source citée")
a = txt(85, 2)
ligne(5, 85, 2, "modifier", "mecanisme_en_une_phrase", a,
      a.replace("(tous à p ajustée ≥ 0,56)", "(selon les auteurs, tous à p ajustée ≥ 0,56 ; non vérifié par le programme)"),
      "chiffre sans marque d'attribution : à écrire « selon les auteurs »")

# ---- 6 : ligne de 57 qui reprend la famille cloisonnée -----------------------------------------
a = txt(57, 6)
ligne(6, 57, 6, "retirer_mecanisme", "mecanisme", a, None,
      "reprend la perte de précision d'un harnais optimisé pour la note d'un juge, facette de la famille exclue (attaque de Goodhart du juge) : la ligne est retirée, le catalogue ne la porte pas ; la facette est notée « exclue » seulement")
ligne(6, 57, None, "ajouter_champ", "facette_exclue", None,
      "facette « optimisation d'un harnais contre un juge » : exclue (voir docs/notes/veille-exploration-idees-v1/lecture-03-v1.md, section non ouverte) ; aucun contenu retenu",
      "noter « exclue » seulement")

# ---- 7 : mécanismes oubliés -----------------------------------------------------------------------
V = "docs/notes/veille-exploration-idees-v1/"
def pdf_de(i):
    for m in R[i]["mecanismes"]:
        x = re.search(r"docs/sources/pdf/[^ ,;()]+\.pdf", m["source_dans_le_depot"])
        if x:
            return x.group(0)
def src(lecture, details, i, pdf=None, pages=None, lignes=None):
    s = f"{V}{lecture} (empreinte {sha(V + lecture)}), {details}"
    if pdf:
        s += f" ; PDF {pdf} (empreinte {sha(pdf)}), {pages}"
    s += f" ; {V}table-fusionnee-v1.json (empreinte {sha(V + 'table-fusionnee-v1.json')}), travaux[{i}]"
    if lignes:
        s += " ; " + lignes
    return s
def ajout(i, fam, txt_, ep, source):
    ligne(7, i, None, "ajouter_mecanisme", "mecanisme", None,
          dict(famille=fam, mecanisme_en_une_phrase=txt_, eprouve_contre_le_reel=ep, source_dans_le_depot=source, suggere_par_le_titre=False),
          "mécanisme oublié par le lot d'origine, relevé par la contre-lecture (section 4) d'après la lecture approfondie citée")
p08 = pdf_de(112)
ajout(112, "épreuve", "Le signal public vu par l'agent de la boucle intérieure est séparé de la note privée sur laquelle la solution rendue est notée et retenue ; un relecteur modèle, dans chaque agent, lit les sorties d'exécution pour en extraire le score public (selon la lecture 08, p. 4 du PDF ; affirmation des auteurs, composant sans ablation).", "inconnu",
      src("lecture-08-v1.md", "section 2", 112, p08, "p. 4"))
ajout(112, "auto-conception", "Les agents découverts portent une politique de recherche par bandit, une compression du contexte et des garde-fous, décrits sans ablation : les auteurs écrivent qu'on ne sait pas quels composants portent la performance et lesquels sont inutilisés (selon la lecture 08, p. 13 du PDF).", "inconnu",
      src("lecture-08-v1.md", "sections 3 et 6", 112, p08, "p. 13"))
ajout(112, "sélection", "La diversité du banc de sélection (trois familles de tâches) est posée comme le moteur de la généralité des mécanismes découverts : choix de conception affirmé par les auteurs, non testé (selon la lecture 08, p. 3 du PDF).", "non",
      src("lecture-08-v1.md", "section 3.1", 112, p08, "p. 3"))
p02 = pdf_de(450)
ajout(450, "épreuve", "Engagement préalable de l'agent : il consigne son verdict et sa probabilité a priori avant tout accès aux données (p. 5 du PDF) ; selon la lecture 02, cet engagement n'entre dans aucune statistique de décision.", "inconnu",
      src("lecture-02-v1.md", "protocole de l'agent", 450, p02, "p. 5"))
ajout(450, "jugement", "Les trois modèles commerciaux testés affirment exactement quand leur probabilité déclarée atteint un demi, dans 3 990 lancements sur 3 990 (p. 18 du PDF) : résultat exploratoire de l'auteur, selon la lecture 02.", "oui, mesuré",
      src("lecture-02-v1.md", "résultats exploratoires", 450, p02, "p. 18"))
p05 = "docs/sources/pdf/veille-exploration-idees-v1/machine-huxley-godel-2510.21614/arxiv-2510.21614v3.pdf"
ajout(593, "épreuve", "Le juge est constitué des tests exécutables des bancs, sans modèle de langue ; le transfert est mesuré sur 207 tâches inédites de SWE-bench Lite, absentes de SWE-bench Verified (donc de la même famille), et sur un autre modèle, jamais sur une famille inédite (tables 3 et 4, p. 9 à 10 ; selon les lectures 05 et Huxley-Gödel v2).", "oui, mesuré",
      src("lecture-05-v1.md", "section « mesuré »", 593, p05, "p. 9-10"))
ajout(593, "coût", "Resserrement des lois bêta quand le budget s'épuise et exécution asynchrone (une itération par processeur disponible) : mécanismes décrits, confondus avec l'agrégat de lignée dans la comparaison aux deux autres méthodes (table 5, p. 20), aucune ablation selon la lecture ; coût déclaré d'environ 5 000 dollars pour les trois méthodes (p. 18).", "inconnu",
      src("lecture-05-v1.md", "usage et réserves 1", 593, p05, "p. 7, 17, 18, 20", lignes=f"{V}lecture-huxley-godel-v2.md (empreinte {sha(V + 'lecture-huxley-godel-v2.md')}), tables et section sur l'exécution"))
p12 = pdf_de(98)
ajout(98, "épreuve", "Les jeux publics sont servis aux agents sous des noms neutres (p. 13 du PDF) ; la lecture 12 ne donne pas le motif de ce choix (la protection contre la mémorisation ou la contamination est une lecture plausible du relevé, non affirmée).", "inconnu",
      src("lecture-12-v1.md", "section 2 (les tâches)", 98, p12, "p. 13"))
p09 = pdf_de(456)
ajout(456, "mémoire", "Rotation de la fenêtre d'échecs montrée au proposeur : les cas résolus en sortent et de nouveaux échecs y entrent (fenêtre de quatre) ; c'est l'un des trois mécanismes de l'effet de l'héritage du parent que les auteurs nomment sans les séparer (p. 4 du PDF, selon la lecture 09).", "oui, mesuré",
      src("lecture-09-v1.md", "question « qu'est-ce qui s'hérite »", 456, p09, "p. 4, 13"))
ajout(456, "épreuve", "Réplique sur un second modèle (claude-haiku-5-5, cinq tâches) et avec un proposeur plus gros (gpt-4.1, trois tâches) du plan croisé lignée contre retour montré (p. 2 et 8 du PDF, selon la lecture 09).", "oui, mesuré",
      src("lecture-09-v1.md", "section « modèles »", 456, p09, "p. 2, 8"))

# ---- 8 : empreintes du lot 04, précisions de lecture des lots 04 et 20 -----------------------------
CHEM = re.compile(r"(docs/[^\s,;():]+\.(?:md|json|pdf))(:\d+)?")
def avec_empreintes(s):
    def f(m):
        p = m.group(1)
        return p + (m.group(2) or "") + f" (empreinte {sha(p)})"
    return CHEM.sub(f, s)
for r in LOTS:
    if 90 <= r["indice"] <= 119:
        for k, m in enumerate(r["mecanismes"]):
            nouveau = avec_empreintes(m["source_dans_le_depot"])
            assert nouveau != m["source_dans_le_depot"]
            ligne(8, r["indice"], k, "modifier", "source_dans_le_depot", m["source_dans_le_depot"], nouveau,
                  "R6 : chaque chemin cité reçoit son empreinte (sha256 recalculée sur disque)")
    if 90 <= r["indice"] <= 119 or 570 <= r["indice"] <= 599:
        if "precision_de_lecture" not in r:
            if r["profondeur_de_lecture"] == "lecture approfondie sur PDF":
                p = "lecture approfondie du dépôt relue (voir la source de chaque mécanisme) ; affirmations des auteurs selon la lecture, non opposables (R7)"
            else:
                p = "résumé ou page lus par la veille, d'après la table ; affirmations des auteurs, non opposables (R7)"
            ligne(8, r["indice"], None, "ajouter_champ", "precision_de_lecture", None, p,
                  "le lot d'origine ne portait pas de précision de lecture au niveau de l'entrée")
        if "mesure_selon_la_table" not in r:
            ligne(8, r["indice"], None, "ajouter_champ", "mesure_selon_la_table", None, TABLE[r["indice"]]["mesure"],
                  "le lot d'origine ne portait pas la mesure selon la table au niveau de l'entrée")

# ---- 10 : statut des entrées sans mécanisme ni statut -----------------------------------------------
STAT = {216: ("exclue", "déjà marquée « exclue » dans un champ à part du lot (attaque du juge) : le statut est ajouté pour que le compte se ferme"),
        263: ("liste sans mécanisme", "liste d'articles, sans mécanisme propre"), 264: ("liste sans mécanisme", "liste d'articles, sans mécanisme propre"),
        265: ("liste sans mécanisme", "liste d'articles, sans mécanisme propre"),
        282: ("notice muette", "le titre n'annonce qu'un système général, sans dire comment les idées sont cherchées, éprouvées ou jugées"),
        297: ("hors sujet", "article de position sur des institutions, sans mécanisme d'exploration ni d'épreuve (d'après le titre ; non opposable)"),
        306: ("notice muette", "titre seul, aucun mécanisme relevable"),
        354: ("hors sujet", "d'après le seul titre ; jugement non opposable (R7)"), 356: ("hors sujet", "d'après le seul titre ; jugement non opposable (R7)"),
        477: ("hors sujet", "opinion rapportée par un agrégateur, aucun mécanisme"), 478: ("notice muette", "titre seul, non lu"),
        479: ("hors sujet", "plaidoyer, aucun mécanisme d'idéation ou d'épreuve décrit")}
for i, (s, raison) in STAT.items():
    assert not R[i]["mecanismes"] and "statut" not in R[i]
    ligne(10, i, None, "ajouter_champ", "statut", None, s, raison)

REGLES = {
    "normalisation_des_familles": {"epreuve": "épreuve", "selection": "sélection", "memoire": "mémoire", "cout": "coût",
                                    "originalité": "originalité", "exploration": "exploration", "jugement": "jugement",
                                    "auto-conception": "auto-conception", "autre": "autre"},
    "correction": 4, "raison": "écriture des familles à unifier avant tout compte : les lots écrivent « originalité » avec accent et les autres familles sans",
    "champ_par_defaut": {"suggere_par_le_titre": False}}
sortie = dict(version="v1", contre_lecture="docs/notes/matiere-premiere-auto-conception-v1/contre-lecture-matiere-premiere-v1.md",
              correction_1="réalisée par lots/lot-21.json (indices 600 à 629)", regles_globales=REGLES, corrections=C)
Path("programmes/corrections-v1.json").write_text(json.dumps(sortie, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
import collections
print(len(C), "lignes", dict(collections.Counter(c["correction"] for c in C)), dict(collections.Counter(c["operation"] for c in C)))
