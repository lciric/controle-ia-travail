"""Version 10 (18 novembre 2026, R-3178) : v9 + trois retraits par nom décidés par la mère, même mécanique (contenu
jamais lu, comptes seulement dans `EXPURGE.md`). (1) Autre projet (R-2679) : tout chemin dont un segment normalisé (comme
en v9 : accents, casse, séparateurs) porte « regard-ou-raisons », sous `DOSSIERS_AUTRE_PROJET` (runs, docs, brouillons,
scripts, tests, src, livrables) — dont `runs/course-ideation-regard-ou-raisons-v1/` (36 chemins) et les lanceurs et essais
à tiret bas (4) ; ailleurs, un tel nom arrête, qu'il soit gardé ou retiré avec liste (`registres/**` : son chemin
paraîtrait dans `EXPURGE.md`). `pain-axis` est lu sous la même normalisation pour cette garde. (2) Copies par
identifiant d'objet git : un fichier non retiré par nom dont l'identifiant (lu dans l'arbre, contenu jamais lu) est
celui d'un fichier retiré par nom est retiré à son tour, avec son compagnon `.sha256`, et compté (`RAISON_COPIE`) —
au lieu d'arrêter le script — quand tous les fichiers de cet identifiant sont des retraits par nom ordinaires
(brouillons `pain-axis-*`, autre projet). Quand l'identifiant est aussi celui d'un fichier SOUS EMBARGO ou en retrait
PERMANENT sensible, le script arrête toujours, sauf si le chemin est nommé un à un dans
`RETRAITS_PAR_IDENTIFIANT_EXPLICITES` ; un nom de cette liste présent dans l'arbre mais qui n'est plus une copie arrête
aussi. Raison : une copie d'un fichier sensible sous un nom anodin dit que le filtre par nom a un trou (le contenu d'une
famille sensible vit sous un nom qu'il ne voit pas, et des fichiers voisins, non identiques, peuvent l'accompagner) ; la
retirer en silence cacherait ce trou (R5) ; seul un regard humain sur les noms, consigné dans la liste, peut dire que la
coïncidence est sans objet. Les identifiants des fichiers seulement sous embargo sont désormais pris (la v9 les
écartait). (3) Fragments permanents ajoutés : « attaquant-informe », « saboteur », « equipe-rouge », et des formes
fléchies (« organisme-discret », « bras-attaques », « attaquants-informes », « saboteuse », « equipes-rouges »,
« attaques-publiees ») ; « bras-attaques » est déjà couvert par « bras-attaque », gardé pour la lettre de la consigne.
Version 9 (18 novembre 2026, contre-lecture de la v8, `docs/notes/copie-publique-v8/`) : v8 + trois corrections.
(1) Le nom est normalisé avant la comparaison aux fragments permanents : accents ôtés, minuscules, toute suite de
caractères autres que lettres et chiffres lue comme un tiret, puis aussi sans aucun séparateur ; la v8 comparait à la
lettre et gardait donc les noms à tiret bas (`scripts/lancer_…_organismes_discrets_v1.py`, `…_pilier_attaque_…` : 30
chemins suivis le 18 novembre). (2) Dans une archive gardée, les noms des membres sont examinés avant toute lecture de
contenu : un membre au nom sensible arrête sans être lu (la v8 lisait son contenu, pour l'empreinte et les gardes, avant
de regarder son nom) ; le message donne l'archive et un compte, pas les noms. (3) Mode à blanc : une archive gardée
non examinée arrête (plus de verdict « passeraient » sur une archive non ouverte).
Version 8 (18 novembre 2026, R-3174) : v7 + retrait PERMANENT par nom, qui ne se lève pas avec l'embargo, du bras
d'attaque et des familles sensibles (conception d'organismes saboteurs discrets, évasion des moniteurs) : tout chemin
dont un segment porte un des fragments de `FRAGMENTS_PERMANENTS`, sous un des dossiers de `DOSSIERS_PERMANENTS`. Même
mécanique que les retraits par nom de la v7 : contenu jamais lu, ni empreinte ni taille, `EXPURGE.md` n'en donne que le
compte. Le retrait permanent passe avant l'embargo et avant les retraits listés (`registres/**` compris) : un chemin
sensible n'est jamais listé par chemin. Garde : tout chemin qui porte un de ces fragments hors des dossiers visés arrête
le script sans être lu (aucune exception nommée, aucun repli silencieux, R5) ; un fichier gardé ou un membre d'archive
gardée qui porte un de ces fragments, ou qui a l'identifiant d'objet git d'un fichier sensible, l'arrête aussi. Mode à
blanc (`--a-blanc`) : comptes par motif, tirés des seuls noms de l'arbre du commit (et des noms des membres des
archives gardées), rien n'est écrit, aucun chemin sensible n'est imprimé.
Version 7 (14 novembre 2026, R-2672, R-2679) : v6 + retraits par nom, jamais lus et comptés sans chemin dans
`EXPURGE.md` : `brouillons/pain-axis-*` (dossiers, fichiers et compagnons ; R-173, R-209 : exclus de toute copie
publique) et, par précaution, `docs/notes/regard-ou-raisons-*` et `docs/notes/collisionneur-regard-ou-raisons-*`
(autre projet de Lazar, non publié). Trois gardes neuves, chacune arrête sans écrire de paquet : un fichier gardé, ou
un membre d'une archive gardée, qui a l'identifiant d'objet git d'un fichier retiré par nom (identifiants lus dans
l'arbre du commit, contenu jamais lu) ; un membre d'archive dont le chemin porte un des noms retirés ; un chemin
gardé dont le nom porte un de ces noms hors des dossiers visés et hors de la liste nommée `GARDES_SIGNALES`.
Version 6 (12 novembre 2026, R-2433) : v5 + chemins sous embargo jusqu'au verdict scellé de P3-bis (filtrés par nom
seulement, jamais lus ; comptés sans chemin dans `EXPURGE.md`), textes de tiers hors `docs/sources/pdf/` (PDF et pages
de Nature, pages de sites), candidature de Lazar au TAIF (curriculum vitae), formes de clés élargies (`sk-…`, `AKIA…`),
garde des données personnelles (adresses électroniques hors liste blanche, adresses IP publiques, chemins personnels),
README public fourni par `--readme`. Version 5 (5 novembre 2026, R-1577) : v4 avec des motifs nommés pour les journaux de la racine (le motif « *.log » visait aussi des membres d'archives gardées). Version 4 (R-1576) : v3 + archives tar compressées par gzip examinées, journaux et rapport de la relève de Gemini à la racine retirés. Version 3 (R-1575) : v2 + motif des archives élargi (v49 et antérieures). Version 2 (R-1574) : v1 + retrait des essais de l'orchestrateur portant des clés factices.

Copie expurgée du dépôt, à montrer à des évaluateurs (décision de Lazar, R-104).

Un seul commit, reproductible, tiré d'un commit cité du dépôt : sans les textes de tiers dont le code n'a pas besoin
(PDF d'arXiv, pages extraites par les lecteurs, texte complet ou extrait d'un papier, pages des cartes de modèles,
fichiers de travail des relecteurs de l'extraction, sorties de l'extraction), sans la candidature à un autre fonds.
Les empreintes des fichiers retirés restent, et `EXPURGE.md` les liste. Les invites transcrites ou adaptées que le
code et ses tests chargent restent, avec leur source : le README de la copie le dit. Avant d'écrire le paquet, le
script vérifie qu'aucun fichier retiré ne survit dans une archive gardée (zip, tar ou paquet git, à toute profondeur,
par empreinte et par chemin) ; une archive d'un format qu'il n'examine pas l'arrête. Garde des secrets (R-349) : il
s'arrête aussi si un fichier gardé, ou un membre d'une archive gardée, contient la valeur d'une clé de l'environnement
ou un jeton d'une forme connue ; il ne dit que le chemin et le nom de la variable ou de la forme, jamais la valeur.
Depuis R-351 (interdit des clés `RR_*` levé par Lazar), leurs valeurs sont comparées comme les autres.

Rien n'est poussé : le paquet git est écrit dans SORTIE. Sa mise en ligne sur un dépôt distant demande un GO de Lazar.
Le script n'écrit que dans SORTIE, qui ne doit pas exister ; il ne touche pas au dépôt.

    .venv/bin/python scripts/depot_expurge_v10.py COMMIT SORTIE [--readme README_PUBLIC]
    .venv/bin/python scripts/depot_expurge_v10.py COMMIT --a-blanc
"""
from __future__ import annotations

import fnmatch
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tarfile
import tempfile
import unicodedata
import zipfile
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]

# (motif sur le chemin suivi, motif du retrait) ; un fichier `.sha256` compagnon reste, sauf s'il est lui-même visé.
# Un `*` ne traverse pas les dossiers ; un motif qui finit par `/**` vise tout le dossier, à toute profondeur.
RETRAITS = [
    ("docs/sources/pdf/*.pdf", "copie d'un PDF d'arXiv de tiers"),
    ("docs/sources/pdf/**/*.pdf", "copie d'un PDF de tiers (sous-dossier ; bisociation, R-590 de conv-audit)"),
    ("docs/sources/lecture-pdf-niveau1/*.tar", "fichiers de travail d'un lecteur : pages extraites des PDF de tiers"),
    ("docs/sources/lecture-pdf-niveau2/*.tar", "fichiers de travail d'un lecteur : pages extraites des PDF de tiers"),
    ("docs/sources/invites-2606.08892-v1/extrait.tar", "texte complet extrait d'un papier de tiers"),
    ("docs/sources/invites-2606.07054-v1/*.tar", "texte extrait d'un papier de tiers"),
    ("docs/sources/invites-2606.07054-v1/derivees/contre-verification-v1/*.tar",
     "fichiers de travail d'une contre-vérification : texte extrait d'un papier de tiers"),
    ("docs/sources/cartes-modeles-20261006/*.html", "page d'une carte de modèle (site tiers)"),
    ("docs/procedures/T0.5-extraction-v1/contre-lecture/*.tar", "fichiers de travail des relecteurs de l'extraction"),
    ("prereg/contre-lectures/T0.5-pilote-contre-lecture-1-verifications-v1.tar",
     "fichiers de travail d'un relecteur : pages extraites d'un PDF de tiers"),
    ("donnees/**", "sortie de l'extraction : texte dérivé de papiers de tiers"),
    ("livrables/candidature-ea-funds-v1/**", "candidature à un autre fonds, confidentielle"),
    ("livrables/candidature-ea-funds-v1.zip", "candidature à un autre fonds, confidentielle"),
    ("livrables/candidature-ea-funds-v1.zip.sha256", "candidature à un autre fonds, confidentielle"),
    ("registres/**", "registres de travail : messages de Lazar cités mot pour mot, montants, instances (R-116)"),
    ("gemini/**", "travaux de la relève de Gemini, non audités ; un fichier y porte une clé en clair (R-333, N-038, R-348)"),
    ("DAEMON_NOCTURNE_*.log", "journal de la relève de Gemini à la racine, non audité (R-1576)"),
    ("NODE_*.log", "journaux de la relève de Gemini à la racine, non audités (R-1576)"),
    ("RAPPORT_COMPLET_DECOUVERTES_ET_BILAN_TAIF.md", "rapport de la relève de Gemini à la racine, non audité (R-1576)"),
    ("docs/notes/ideation-organisme-v1/orchestrateur-v5*/essais/test_*.py",
     "essais de l'orchestrateur de l'organisme : clés factices de la forme d'une clé Anthropic (préfixe FAUX) que la garde des secrets refuse ; le code est public dans lciric/ideation-organism (R-1574)"),
    ("docs/notes/ideation-organisme-v1/orchestrateur-v5*/CODE-orchestrateur-pole-v7-v*.zip",
     "archive des mêmes essais (clés factices) ; code public dans lciric/ideation-organism (R-1574)"),
    ("livrables/reponse-amitie-v1/**", "textes d'une candidature (séminaire AFFINE), privés (R-116)"),
    ("livrables/reponse-amitie-v1.zip", "textes d'une candidature (séminaire AFFINE), privés (R-116)"),
    ("livrables/reponse-amitie-v1.zip.sha256", "textes d'une candidature (séminaire AFFINE), privés (R-116)"),
    ("livrables/anteriorite-niveau1-v1/decisions-v2.md", "copie du registre des décisions (R-116)"),
    ("livrables/premier-rendu-v1/decisions-v1.md", "copie du registre des décisions (R-116)"),
    ("livrables/anteriorite-niveau1-v1.zip", "archive qui contient les registres de travail (R-116)"),
    ("livrables/premier-rendu-v1.zip", "archive qui contient les registres de travail (R-116)"),
    ("livrables/controle-ia-v1.bundle", "paquet git qui contient les registres de travail (R-116)"),
    ("brouillons/**/corpus-primaire-*/**", "corpus intégral des idées : ne quitte jamais le dépôt privé"),
    ("livrables/lot-ideation-tournoi-*.zip", "lot de l'orchestrateur avec le corpus des idées : ne quitte jamais le dépôt privé"),
    ("brouillons/canal-reprise-releve-v1/envois/candidature-pivotal-v1/**",
     "candidature personnelle de Lazar au Pivotal Research Fellowship, privée (n° 322 de conv-audit, R-984)"),
]
# v6 (R-2433) : textes de tiers hors de `docs/sources/pdf/`, données personnelles.
RETRAITS += [
    ("docs/sources/co-scientist-v1/*.pdf", "PDF d'un article de tiers (Nature, arXiv), sous droit d'auteur (R-2433)"),
    ("docs/sources/co-scientist-v1/*-pages.txt", "pages extraites d'un article de tiers (R-2433)"),
    ("docs/sources/co-scientist-v1/conditions-google-labs-lu-*/*-texte-v1.txt", "texte de pages d'un site de tiers (R-2433)"),
    ("docs/sources/co-scientist-v1/conditions-google-labs-lu-*/labs-google-robots-txt-decompresse-v1.txt",
     "fichier d'un site de tiers (R-2433)"),
    ("docs/sources/co-scientist-v1/conditions-google-labs-lu-*/pages-brutes-*.tar.gz", "pages brutes d'un site de tiers (R-2433)"),
    ("docs/sources/web-openai-rapport-surveillance-20261022/page-*", "page d'un site de tiers (R-2433)"),
    ("docs/sources/prix/*.html", "page d'un site de tiers (R-2433)"),
    ("docs/notes/ideation-organisme-v1/machine-jetable-v1/sources-*/*.html", "page d'un site de tiers (R-2433)"),
    ("docs/notes/ideation-organisme-v1/relais-kimi-v1/doc-moonshot-lue-*/*.html", "page d'un site de tiers (R-2433)"),
    ("docs/notes/ideation-organisme-v1/course-2/pieces/helios-*-pages-*.txt", "pages extraites d'un papier de tiers (R-2433)"),
    ("brouillons/pain-axis-programme-fusionne-v1/travail/voisin-where-empathy/extrait-texte-v1.txt",
     "texte extrait d'un papier de tiers (R-2433)"),
    ("docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/commit-public-code-v5-a1-v4-v*.bundle",
     "paquet git incrémental (prérequis absents) du code publié dans lciric/ideation-organism : non examinable seul (R-2433)"),
    ("docs/notes/organisme-boucle-reelle-v1/**/organisme-v6*-boucle-reelle-v*.bundle",
     "paquet git incrémental (prérequis absents) du code publié dans lciric/ideation-organism : non examinable seul (R-2433)"),
    ("docs/sources/lecture-pdf-niveau1/TRACE-AcMAS/*_pages.txt", "pages extraites d'un papier de tiers (R-2433)"),
    ("docs/notes/ideation-organisme-v1/machine-jetable-v1/sources-*/*.json", "copie d'un document d'un site de tiers (R-2433)"),
    ("docs/notes/ideation-organisme-v1/machine-jetable-v1/sources-documentation-*/apparmor-journal-modifications-*-v1.txt",
     "copie d'un document de tiers (journal des modifications d'un paquet, avec les adresses de ses auteurs) (R-2433)"),
    ("livrables/readme-v3/README-v3.md", "ancienne version du README : adresse électronique de Lazar (R-2433)"),
    ("livrables/readme-v3.zip", "archive d'une ancienne version du README : adresse électronique de Lazar (R-2433)"),
    ("livrables/readme-v4/README-v4.md", "ancienne version du README : adresse électronique de Lazar (R-2433)"),
    ("livrables/readme-v4.zip", "archive d'une ancienne version du README : adresse électronique de Lazar (R-2433)"),
    ("livrables/page-publique-organisme-2026-11-10-v1/README.md",
     "brouillon de la page publique de l'organisme : adresse électronique de Lazar ; la page est publiée dans lciric/ideation-organism (R-2433)"),
    ("docs/procedures/ordre-fille-neuve-2026-11-04-v1.md", "adresse électronique de Lazar (R-2433)"),
    ("docs/notes/audit-dossier17-essaim-m3-2026-10-24-v1.md", "chemin personnel d'un poste de Lazar (R-2433)"),
    ("docs/sources/ressources-P1-loi-attraction-v1.md", "chemin personnel d'un poste de Lazar (R-2433)"),
    ("docs/notes/organisme-boucle-reelle-v1/course-v66/journal-operateur-course-v66-v1.md",
     "adresse IP d'un serveur loué (R-2433)"),
    ("docs/notes/organisme-boucle-reelle-v1/course-v66/rapport-arret-operateur-course-v66-v1.md",
     "adresse IP d'un serveur loué (R-2433)"),
    ("docs/sources/candidature-taif-2026-10-07/**",
     "candidature personnelle de Lazar (curriculum vitae, budget) : données personnelles (R-2433)"),
]

# v6 (R-2433) : chemins sous embargo jusqu'au verdict scellé de P3-bis. Filtrés par nom seulement : le script ne lit
# jamais leur contenu (ni empreinte, ni taille, ni garde des secrets), et `EXPURGE.md` n'en donne que le compte.
EMBARGO_FRAGMENTS = ("bras-attaque", "mode-tenu-a-l-ecart", "anteriorite-bras-informe", "index-bras-attaque",
                     "lecture-b-7a", "lecture-b-7b", "lecture-7a", "lecture-7b", "mesure-unanime-v15-sortie",
                     "etiqueteur-v2-lecture-interrompue", "lecture-sondes-t06", "audit-ecart-dt4-7a")
EMBARGO_MOTIFS = ("diag/*7a*/**", "diag/*7b*/**", "runs/*7a*/**", "runs/*7b*/**", "diag/*t06*/**", "runs/*t06*/**",
                  "diag/*T0.6*/**", "runs/*T0.6*/**")
RAISON_EMBARGO = "sous embargo jusqu'au verdict scellé de P3-bis (R-2433) : filtré par nom, contenu jamais lu"


def sous_embargo(chemin: str) -> bool:
    bas = chemin.lower()
    return any(f in bas for f in EMBARGO_FRAGMENTS) or any(_segments(chemin.split("/"), m.split("/")) for m in EMBARGO_MOTIFS)

# v7 (R-2672, R-2679) : retraits par nom. Comme l'embargo, ces chemins ne sont jamais lus (ni contenu, ni empreinte,
# ni taille) et `EXPURGE.md` n'en donne que le compte, par motif : ni chemin, ni empreinte. Un motif sans `/**` vise le
# fichier ou le compagnon posé directement dans le dossier parent ; le même motif suivi de `/**` vise le dossier entier.
RAISON_PAIN_AXIS = ("brouillons `brouillons/pain-axis-*` : restent dans le dépôt privé, exclus de toute copie publique "
                    "(R-173, R-209) : filtrés par nom, contenu jamais lu")
RAISON_AUTRE_PROJET = "notes d'un autre projet, non publié (R-2679) : filtrées par nom, contenu jamais lu"
RETRAITS_PAR_NOM = [
    ("brouillons/pain-axis-*", RAISON_PAIN_AXIS),
    ("brouillons/pain-axis-*/**", RAISON_PAIN_AXIS),
    ("docs/notes/regard-ou-raisons-*", RAISON_AUTRE_PROJET),
    ("docs/notes/regard-ou-raisons-*/**", RAISON_AUTRE_PROJET),
    ("docs/notes/collisionneur-regard-ou-raisons-*", RAISON_AUTRE_PROJET),
    ("docs/notes/collisionneur-regard-ou-raisons-*/**", RAISON_AUTRE_PROJET),
]
RAISONS_PAR_NOM = frozenset(r for _, r in RETRAITS_PAR_NOM)
# Noms qui ne doivent paraître dans aucun chemin gardé ni dans aucun membre d'archive gardée (comparés en minuscules).
FRAGMENTS_PAR_NOM = ("pain-axis", "regard-ou-raisons")
# Chemins gardés dont le nom porte un de ces fragments hors des dossiers visés : nommés un à un, rapportés dans le
# bilan. Tout autre chemin de ce genre arrête le script (aucun repli silencieux, R5). Le 14 novembre 2026 : la
# proposition P-013 (document de décision du programme, publique depuis le 12 novembre), gardée faute de mot de Lazar
# sur son retrait ; signalée au rapport du 14 novembre.
GARDES_SIGNALES = ("docs/decisions/proposition-P-013-T0.7-temoins-pain-axis-v1.md",
                   "docs/decisions/proposition-P-013-T0.7-temoins-pain-axis-v1.md.sha256")
BLOB_VIDE = "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391"

# v8 (R-3174) : retrait PERMANENT par nom. Il ne dépend pas de l'embargo (vider `EMBARGO_FRAGMENTS` et
# `EMBARGO_MOTIFS` au verdict de P3-bis ne le lève pas) ; seul un mot exprès de Lazar, et une version neuve du script,
# le lèvent. Un chemin est visé quand un de ses segments porte un des fragments (en minuscules) et que son premier
# segment est un des dossiers visés : dossier entier à toute profondeur, fichier posé dans un dossier, compagnon `.sha256`.
# Hors de ces dossiers (racine, `livrables/`, `gemini/`…), un chemin qui porte un fragment arrête le script sans être lu.
# `registres` et `rapports` : ajoutés aux neuf dossiers de la consigne le 18 novembre 2026, parce que la liste
# `git ls-files` du commit e87fb6ce y porte des chemins sensibles (noms seulement ; comptes au rapport de l'agent) ; sans
# eux, `registres/**` les aurait listés par chemin et par empreinte dans `EXPURGE.md`, et `rapports/` les aurait gardés.
FRAGMENTS_PERMANENTS = ("bras-attaque", "bras-informe", "verification-externe-bras", "evasion-moniteurs",
                        "4-familles-evasion", "pilier-attaque", "attaque-publiee", "organismes-discrets",
                        "mode-tenu-a-l-ecart")
# v10 (R-3178, contre-lecture de la v8, « Ce qui reste », point 2) : noms voisins (brief de la session de l'attaquant
# informé, brouillons et proposition du saboteur diffus, notes de l'affinage de l'équipe rouge) et formes fléchies. Ajoutés
# après les neuf de la v8, pour que les comptes par fragment de la v9 restent lisibles (premier fragment trouvé).
FRAGMENTS_PERMANENTS += ("attaquant-informe", "saboteur", "equipe-rouge",
                         "organisme-discret", "bras-attaques", "attaquants-informes", "saboteuse", "equipes-rouges",
                         "attaques-publiees")
DOSSIERS_PERMANENTS = ("docs", "prereg", "brouillons", "src", "scripts", "tests", "donnees", "runs", "diag",
                       "registres", "rapports")
RAISON_PERMANENTE = ("bras d'attaque et familles sensibles (conception d'organismes saboteurs discrets, évasion des "
                     "moniteurs) : exclus de toute copie publique sans mot exprès de Lazar ; filtrés par nom, contenu "
                     "jamais lu")
RAISONS_PAR_NOM = RAISONS_PAR_NOM | {RAISON_PERMANENTE}
FRAGMENTS_PAR_NOM = FRAGMENTS_PAR_NOM + FRAGMENTS_PERMANENTS


def _normalise(segment: str) -> str:
    """v9 : accents ôtés, minuscules, toute suite de caractères autres que lettres et chiffres ASCII rendue par un tiret."""
    sans = "".join(c for c in unicodedata.normalize("NFKD", segment) if not unicodedata.combining(c)).lower()
    return re.sub(r"[^a-z0-9]+", "-", sans)


def _premier_fragment(chemin: str, fragments: tuple[str, ...]) -> str | None:
    """v10 : premier des fragments porté par un segment normalisé du chemin (comparaison de la v9, mise en commun)."""
    for segment in chemin.replace("\\", "/").split("/"):
        norme = _normalise(segment)
        colle = norme.replace("-", "")
        for f in fragments:
            if f in norme or f.replace("-", "") in colle:
                return f
    return None


def fragment_sensible(chemin: str) -> str | None:
    """Premier fragment permanent porté par un segment du chemin, ou None. v9 : comparaison sur le segment normalisé
    (casse, accents, séparateurs : `bras_attaque`, `Bras Attaque`, `bras.attaque`), puis sans aucun séparateur
    (`brasAttaque`). Une barre oblique inverse (membre d'archive) sépare aussi les segments."""
    return _premier_fragment(chemin, FRAGMENTS_PERMANENTS)


# v10 (R-3178, R-2679) : l'autre projet, retiré par nom normalisé sous ces dossiers (dont `runs/` : 36 chemins de
# `runs/course-ideation-regard-ou-raisons-v1/` ; `scripts/` et `tests/` : lanceurs et essais à tiret bas). Ailleurs, le
# nom arrête le script (garde des noms non prévus de la v7, lue ici sous la même normalisation).
FRAGMENTS_AUTRE_PROJET = ("regard-ou-raisons",)
DOSSIERS_AUTRE_PROJET = ("runs", "docs", "brouillons", "scripts", "tests", "src", "livrables")
# Fragments des retraits par nom ordinaires (v7), lus sous la normalisation de la v9 par la garde des noms non prévus.
FRAGMENTS_ORDINAIRES = ("pain-axis",) + FRAGMENTS_AUTRE_PROJET


def retrait_autre_projet(chemin: str) -> bool:
    """v10 : vrai si un segment normalisé porte un fragment de l'autre projet, sous un des dossiers visés."""
    segments = chemin.split("/")
    return (len(segments) > 1 and segments[0] in DOSSIERS_AUTRE_PROJET
            and _premier_fragment(chemin, FRAGMENTS_AUTRE_PROJET) is not None)


def porte_un_fragment_par_nom(chemin: str) -> bool:
    """v10 : vrai si le chemin porte un des fragments des retraits par nom (ordinaires ou permanents), à la lettre en
    minuscules (v7) ou sous la normalisation de la v9."""
    bas = chemin.lower()
    return (any(f in bas for f in FRAGMENTS_PAR_NOM) or _premier_fragment(chemin, FRAGMENTS_ORDINAIRES) is not None
            or fragment_sensible(chemin) is not None)


def retrait_permanent(chemin: str) -> bool:
    """Vrai si le chemin porte un fragment permanent sous un des dossiers visés (au moins un segment sous le dossier)."""
    segments = chemin.split("/")
    return len(segments) > 1 and segments[0] in DOSSIERS_PERMANENTS and fragment_sensible(chemin) is not None


def sensible_hors_dossiers(chemin: str) -> bool:
    """Vrai si le chemin porte un fragment permanent hors des dossiers visés : il arrête le script, sans être lu."""
    return fragment_sensible(chemin) is not None and not retrait_permanent(chemin)


def retire_par_nom(chemin: str) -> str | None:
    """Raison du retrait par nom, ou None. v8 : le retrait permanent passe d'abord. Appariement par segment
    (`_segments`, comme l'embargo) : `correspond` lit à la lettre le préfixe d'un motif qui finit par `/**`, et ne
    verrait pas l'étoile de `pain-axis-*/**`."""
    if retrait_permanent(chemin):
        return RAISON_PERMANENTE
    if retrait_autre_projet(chemin):            # v10 : nom normalisé, sous les dossiers de `DOSSIERS_AUTRE_PROJET`
        return RAISON_AUTRE_PROJET
    segments = chemin.split("/")
    for motif, raison in RETRAITS_PAR_NOM:
        if _segments(segments, motif.split("/")):
            return raison
    return None


def porte_un_nom_retire(chemin: str) -> bool:
    """Vrai si le chemin est visé par un retrait par nom ou porte un des fragments, où qu'il soit (membre d'archive)."""
    return retire_par_nom(chemin) is not None or porte_un_fragment_par_nom(chemin)       # v10 : normalisé


def identifiant_git(contenu: bytes) -> str:
    """Identifiant d'objet git (SHA-1) d'un contenu : celui que `git ls-tree` donne sans lire le fichier."""
    return hashlib.sha1(b"blob %d\0" % len(contenu) + contenu).hexdigest()


def _entrees(commit: str) -> list[tuple[str, str, str, str]]:
    """(mode, type, identifiant, chemin) de chaque entrée de l'arbre du commit : noms et identifiants, aucun contenu."""
    entrees = []
    for ligne in _git("ls-tree", "-r", "-z", commit).decode().split("\0"):
        if ligne:
            meta, chemin = ligne.split("\t", 1)
            mode, type_, sha = meta.split()
            entrees.append((mode, type_, sha, chemin))
    return entrees


def classes_d_identifiants(entrees: list[tuple[str, str, str, str]]) -> dict[str, frozenset[str]]:
    """v10 : identifiant d'objet git -> classes des fichiers retirés par nom qui le portent : « sensible » (retrait
    permanent), « embargo » (sous embargo, sans retrait permanent), « ordinaire » (autre retrait par nom). Lus dans
    l'arbre : aucun contenu n'est lu. L'objet vide n'est jamais pris (fichiers vides, sans contenu à protéger)."""
    classes: dict[str, set[str]] = {}
    for _, type_, sha, chemin in entrees:
        if type_ != "blob" or sha == BLOB_VIDE:
            continue
        if retrait_permanent(chemin):
            c = "sensible"
        elif sous_embargo(chemin):
            c = "embargo"
        elif retire_par_nom(chemin):
            c = "ordinaire"
        else:
            continue
        classes.setdefault(sha, set()).add(c)
    return {k: frozenset(v) for k, v in classes.items()}


def identifiants_par_nom(commit: str) -> frozenset[str]:
    """Identifiants d'objets git des fichiers retirés par nom au commit, lus dans l'arbre : aucun contenu n'est lu.
    v10 : les fichiers seulement sous embargo sont pris aussi (la v8 et la v9 les écartaient)."""
    return frozenset(classes_d_identifiants(_entrees(commit)))


# v10 (R-3178) : copies par identifiant. Chemins nommés un à un, après un regard humain sur les noms (jamais sur le
# contenu), dont l'identifiant d'objet git est celui d'un fichier sensible ou sous embargo et dont la coïncidence est
# sans objet : ils sont retirés et comptés au lieu d'arrêter. Le 18 novembre 2026 (arbre du commit 1e90d43d) : un
# compagnon `.sha256` dont le fichier est vide (objet vide) ; son contenu est l'empreinte de la chaîne vide suivie du nom
# du fichier, qu'il partage avec le compagnon d'un fichier vide de même nom dans un dossier retiré à titre permanent.
RETRAITS_PAR_IDENTIFIANT_EXPLICITES = (
    "docs/notes/collisionneur-experimentateur-v1/run-e3-v1/essais/E3-T1-conception-D.essai1.reponse.md.sha256",
)
RAISON_COPIE = ("même identifiant d'objet git qu'un fichier retiré par nom (copie sous un autre nom), ou son compagnon "
                "`.sha256` : filtré par identifiant, contenu jamais lu (R-3178)")


def copies_par_identifiant(entrees: list[tuple[str, str, str, str]], classes: dict[str, frozenset[str]]
                           ) -> tuple[frozenset[str], list[str], list[str]]:
    """v10 : (chemins retirés comme copies, avec leurs compagnons ; copies qui arrêtent ; noms de
    `RETRAITS_PAR_IDENTIFIANT_EXPLICITES` présents dans l'arbre qui ne sont pas des copies, et qui arrêtent aussi).
    Ne considère que les fichiers que ni le retrait permanent, ni l'embargo, ni un retrait par nom n'écartent déjà
    (gardés, ou retirés avec liste : leur empreinte serait publiée). Une copie d'un fichier chargé par le code arrête.
    Rien n'est lu : noms et identifiants de l'arbre seulement."""
    retirees, arrets, explicites_vus = set(), [], set()
    blobs = {}
    for mode, type_, sha, chemin in entrees:
        if type_ != "blob" or mode == "120000" or sensible_hors_dossiers(chemin):
            continue
        raison = motif_de(chemin)
        if raison == RAISON_EMBARGO or raison in RAISONS_PAR_NOM:
            continue
        blobs[chemin] = sha
        if chemin in RETRAITS_PAR_IDENTIFIANT_EXPLICITES:
            explicites_vus.add(chemin)
        if sha not in classes:
            continue
        if any(correspond(chemin, g) for g in GARDES):
            arrets.append(chemin)
        elif classes[sha] & {"sensible", "embargo"} and chemin not in RETRAITS_PAR_IDENTIFIANT_EXPLICITES:
            arrets.append(chemin)
        else:
            retirees.add(chemin)
    sans_objet = sorted(c for c in explicites_vus if blobs[c] not in classes)
    compagnons = {c + ".sha256" for c in retirees} & set(blobs)
    return frozenset(retirees | compagnons), sorted(arrets), sans_objet


# L'ancien paquet git (`livrables/controle-ia-v1.bundle`, cinq commits du 2026-10-04, recopié dans
# `livrables/premier-rendu-v1.zip`) reste : aucun fichier de son historique n'est visé ici (garde des archives).

# Paragraphe du README v3 et v4 sur les textes de tiers (R-112, R-113), remplacé dans la copie.
PARAGRAPHE_README = ("This repository holds copies of third-party material: arXiv PDFs (`docs/sources/pdf/`); working "
                     "files of the reader agents with pages extracted from those PDFs; the full text of arXiv 2606.08892 "
                     "and an extract of arXiv 2606.07054 (`extrait.tar` in `docs/sources/invites-2606.08892-v1/` and "
                     "`docs/sources/invites-2606.07054-v1/`); two model-card pages (`docs/sources/cartes-modeles-20261006/`); "
                     "and task-extraction outputs that contain text derived from the papers (`donnees/`). They remain under "
                     "their authors' licences: please do not reuse them.")
REMPLACEMENT_README = ("This copy omits the third-party material: the arXiv PDFs, the reader agents' working files with "
                       "pages extracted from them, the full text of arXiv 2606.08892 and the extract of arXiv 2606.07054, "
                       "the model-card pages and the task-extraction outputs; their SHA-256 hashes remain, and "
                       "`EXPURGE.md` lists every omitted file. It keeps the short prompt texts transcribed or adapted from "
                       "those two papers, because the code and its tests load them; they are attributed to their sources "
                       "and remain under their authors' licences.")

# Renvois du README vers les registres, absents de la copie (R-116) : remplacés s'ils sont présents.
REMPLACEMENTS_FACULTATIFS = [
    ("(my attestation: R-114 in `registres/decisions.md`)",
     "(my attestation, R-114, is recorded in the working registers, which this copy omits)"),
    ("4. The decision log and my approvals: `registres/decisions.md`, `registres/go.md`.",
     "4. The decision log and my approvals are kept in the working registers (`registres/`), which this copy omits."),
    ('Decisions are logged with their dates in `registres/decisions.md`, and my approvals in `registres/go.md`. Every working session ends with a sealed hand-over note in `registres/passations/`.',
     'Decisions are logged with their dates in the working registers (`registres/`), together with my approvals and a sealed hand-over note for every working session; this copy omits them.'),
    ('| `registres/` | Living registers: state, decisions, approvals, compute spending, instance stops, session hand-overs |',
     '| `registres/` | Living registers: state, decisions, approvals, compute spending, instance stops, session hand-overs (omitted from this copy) |'),
]


def _git(*args: str, cwd: Path | None = None, env: dict | None = None, entree: bytes | None = None) -> bytes:
    return subprocess.run(["git", *args], cwd=cwd or RACINE, env=env, input=entree, capture_output=True,
                          check=True).stdout


# fichiers que le code charge : jamais retirés (garde du script et de ses tests)
GARDES = ("docs/sources/invites-2606.08892-v1/invites/*.txt", "docs/sources/invites-2606.08892-v1/index.json",
          "docs/sources/invites-2606.07054-v1/invites/*.txt", "docs/sources/invites-2606.07054-v1/index.json",
          "docs/sources/invites-2606.07054-v1/derivees/*.txt", "docs/sources/invites-2606.07054-v1/derivees/index-v1.json")


def correspond(chemin: str, motif: str) -> bool:
    """Appariement par segment : `*` ne traverse pas les dossiers ; `/**` final vise tout le dossier ; un segment `**`
    au milieu vaut zéro, un ou plusieurs dossiers."""
    if motif.endswith("/**") and "**" not in motif[:-3]:
        return chemin.startswith(motif[:-2])
    return _segments(chemin.split("/"), motif.split("/"))


def _segments(c: list[str], m: list[str]) -> bool:
    if not m:
        return not c
    if m[0] == "**":
        if len(m) == 1:
            return bool(c)                      # `/**` final : au moins un segment sous le dossier
        return any(_segments(c[i:], m[1:]) for i in range(len(c) + 1))
    return bool(c) and fnmatch.fnmatchcase(c[0], m[0]) and _segments(c[1:], m[1:])


def motif_de(chemin: str) -> str | None:
    if sensible_hors_dossiers(chemin):           # v8 : jamais lu, jamais listé, jamais gardé
        raise SystemExit(f"{chemin} : porte un nom sensible ({fragment_sensible(chemin)}) hors des dossiers visés : "
                         "arrêt (aucun paquet écrit)")
    if retrait_permanent(chemin):                # v8 : avant l'embargo, qui se lèvera, et avant RETRAITS
        if any(correspond(chemin, g) for g in GARDES):
            raise SystemExit(f"{chemin} : retiré par nom (permanent) mais chargé par le code : arrêt (aucun paquet écrit)")
        return RAISON_PERMANENTE
    if sous_embargo(chemin):
        if any(correspond(chemin, g) for g in GARDES):
            raise SystemExit(f"{chemin} : sous embargo mais chargé par le code : arrêt (aucun paquet écrit)")
        return RAISON_EMBARGO
    par_nom = retire_par_nom(chemin)
    if par_nom:                                 # v7 : avant RETRAITS, pour que le fichier ne soit jamais lu
        if any(correspond(chemin, g) for g in GARDES):
            raise SystemExit(f"{chemin} : retiré par nom mais chargé par le code : arrêt (aucun paquet écrit)")
        return par_nom
    for motif, raison in RETRAITS:
        if correspond(chemin, motif):
            if any(correspond(chemin, g) for g in GARDES):
                raise SystemExit(f"{chemin} : visé par « {motif} » mais chargé par le code : arrêt (aucun paquet écrit)")
            return raison
    return None


COMPRESSIONS_NON_EXAMINEES = (b"\x1f\x8b", b"BZh", b"\xfd7zXZ\x00", b"7z\xbc\xaf\x27\x1c", b"Rar!", b"\x28\xb5\x2f\xfd")


def est_archive(data: bytes) -> bool:
    return (data[:4] == b"PK\x03\x04" or data[257:262] == b"ustar"
            or data.startswith((b"# v2 git bundle", b"# v3 git bundle")))


def _membres_paquet(data: bytes, nom: str = "paquet git") -> list[tuple[str, bytes]]:
    """(chemin, contenu) de chaque fichier de chaque commit d'un paquet git, historique compris."""
    with tempfile.TemporaryDirectory() as d:
        paquet, depot = Path(d) / "paquet.bundle", Path(d) / "depot.git"
        paquet.write_bytes(data)
        entete = data.split(b"\n\n", 1)[0]
        if any(l.startswith(b"-") for l in entete.split(b"\n")[1:]):   # v6 : paquet incrémental
            raise SystemExit("paquet git incrémental (prérequis absents) : format non examiné : arrêt (aucun paquet écrit)")
        _git("init", "-q", "--bare", str(depot), cwd=Path(d))
        tetes = [l.split()[0] for l in _git("bundle", "unbundle", str(paquet), cwd=depot).decode().splitlines() if l]
        paires = set()
        for commit in _git("rev-list", *tetes, cwd=depot).decode().split():
            for ligne in _git("ls-tree", "-r", "-z", commit, cwd=depot).decode().split("\0"):
                if ligne:
                    meta, chemin = ligne.split("\t", 1)
                    if meta.split()[1] == "blob":
                        paires.add((chemin, meta.split()[2]))
        _noms_d_abord(nom, sorted({chemin for chemin, _ in paires}))            # v9 : avant `cat-file`
        objets = sorted({sha for _, sha in paires})
        sortie, contenus, i = _git("cat-file", "--batch", cwd=depot, entree="\n".join(objets).encode() + b"\n"), {}, 0
        for sha in objets:
            fin = sortie.index(b"\n", i)
            taille = int(sortie[i:fin].split()[2])
            contenus[sha] = sortie[fin + 1:fin + 1 + taille]
            i = fin + 1 + taille + 1
        return sorted((chemin, contenus[sha]) for chemin, sha in paires)


def _noms_d_abord(nom: str, noms: list[str]) -> None:
    """v9 : les noms des membres d'une archive gardée sont examinés avant toute lecture de contenu ; un membre (fichier,
    dossier ou lien) au nom sensible arrête, sans être lu. Le message donne l'archive et un compte, jamais les noms."""
    n = sum(1 for x in noms if fragment_sensible(x))
    if n:
        raise SystemExit(f"{nom} : {n} membre(s) de cette archive gardée portent un nom sensible : jamais lus : "
                         "arrêt (aucun paquet écrit)")


def _membres(nom: str, data: bytes) -> list[tuple[str, bytes]]:
    if data[:4] == b"PK\x03\x04":
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            _noms_d_abord(nom, [i.filename for i in z.infolist()])
            membres = [(i.filename, z.read(i)) for i in z.infolist() if not i.is_dir()]
    elif data[257:262] == b"ustar":
        with tarfile.open(fileobj=io.BytesIO(data)) as t:
            _noms_d_abord(nom, [m.name for m in t.getmembers()])
            membres = [(m.name, t.extractfile(m).read()) for m in t.getmembers() if m.isfile()]
    elif data[:2] == b"\x1f\x8b":  # v4 : archive tar compressée par gzip (.tar.gz, .tgz), examinée comme un tar
        try:
            with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as t:
                _noms_d_abord(nom, [m.name for m in t.getmembers()])
                membres = [(m.name, t.extractfile(m).read()) for m in t.getmembers() if m.isfile()]
        except tarfile.TarError:
            raise SystemExit(f"{nom} : gzip qui n'est pas un tar : format non examiné : arrêt (aucun paquet écrit)")
    elif data.startswith((b"# v2 git bundle", b"# v3 git bundle")):
        membres = _membres_paquet(data, nom)
    elif data.startswith(COMPRESSIONS_NON_EXAMINEES):
        raise SystemExit(f"{nom} : archive d'un format non examiné : arrêt (aucun paquet écrit)")
    else:
        return []
    return [(m[2:] if m.startswith("./") else m, c) for m, c in membres]


def survivants(nom: str, data: bytes, empreintes: set[str], identifiants: frozenset[str] = frozenset()) -> list[str]:
    """Fichiers retirés qui survivent dans une archive gardée (zip, tar ou paquet git, à toute profondeur) : même
    empreinte qu'un fichier retiré, chemin visé par un retrait, ou (v7) chemin qui porte un nom retiré, ou identifiant
    d'objet git d'un fichier retiré par nom."""
    trouves = []
    for membre, contenu in _membres(nom, data):
        chemin = f"{nom}!{membre}"
        if (contenu and hashlib.sha256(contenu).hexdigest() in empreintes) or sous_embargo(membre) or any(
                correspond(membre, motif) for motif, _ in RETRAITS) or porte_un_nom_retire(membre) or (
                contenu and identifiant_git(contenu) in identifiants):
            trouves.append(chemin)
        trouves += survivants(chemin, contenu, empreintes, identifiants)
    return trouves


# Garde des secrets (R-349, demande de Lazar après N-038 (c)). Variables lues : celles dont le nom évoque une clé, `RR_*`
# comprises depuis R-351, sauf les noms en `_FILE` (des chemins) ; valeurs retenues : 20 caractères au moins, sans
# espace, hors chemin, avec des lettres et des chiffres. Formes : jetons des fournisseurs connus.
NOMS_DE_CLES = re.compile(r"(API_KEY|_KEY$|TOKEN|SECRET|PASSWORD|PASSWD|CREDENTIAL|GIT_CONFIG_VALUE)", re.I)
FORMES_DE_CLES = [
    ("clé Anthropic", re.compile(rb"sk-ant-[A-Za-z0-9_\-]{20,}")),
    ("clé Google", re.compile(rb"AIza[0-9A-Za-z_\-]{35}")),
    ("jeton Hugging Face", re.compile(rb"hf_[A-Za-z0-9]{30,}")),
    ("jeton GitHub", re.compile(rb"gh[pousr]_[A-Za-z0-9]{36,}")),
    ("clé dans une adresse", re.compile(rb"api_key=[0-9A-Fa-f]{32,}")),
    ("clé de la forme sk-", re.compile(rb"(?<![A-Za-z0-9_\-])sk-(?!ant-)[A-Za-z0-9_\-]{20,}")),   # v6 : OpenAI, Moonshot, etc.
    ("clé AWS", re.compile(rb"(?<![A-Z0-9])AKIA[0-9A-Z]{16}(?![A-Z0-9])")),
]

# v6 : la forme large `sk-…` attrape aussi les clés factices des essais ; un jeton de cette forme qui porte une marque
# de clé factice (FAUX, FACTICE, essai, fake) n'arrête pas. La comparaison aux valeurs de l'environnement reste entière.
FORMES_FACTICES_PERMISES = {"clé de la forme sk-"}
MARQUE_FACTICE = re.compile(rb"faux|factice|essai|fake|cle-fa", re.I)

# v6 (R-2433) : garde des données personnelles. Adresses électroniques hors liste blanche (adresses génériques ou
# factices), adresses IPv4 publiques, chemins personnels hors des dossiers génériques ; on ne dit que le chemin et la
# nature, jamais la valeur. Courriels : la garde arrête sur une adresse de Lazar ; les adresses de tiers déjà publiées
# (auteurs de papiers, mainteneurs de paquets) sont comptées dans le bilan, pas retirées. Adresses IP : arrêt sur toute
# adresse publique hors de la liste des valeurs relevées le 12 novembre 2026 (numéros de version de paquets, adresses
# de documentation ou de résolveurs publics). Chemins : arrêt sur tout dossier personnel hors des comptes techniques.
COURRIEL = re.compile(rb"[A-Za-z0-9._%+\-]+@[A-Za-z0-9\-]+(?:\.[A-Za-z0-9\-]+)*\.[A-Za-z]{2,}")
COURRIEL_DE_LAZAR = re.compile(rb"(?<![A-Za-z0-9._%+\-])(?:l\.?ciric|lazar\.?ciric|ciric\.?lazar)[A-Za-z0-9._%+\-]*@", re.I)
IPV4 = re.compile(rb"(?<![0-9.])((?:25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])(?:\.(?:25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])){3})(?![0-9.])")
IP_PERMISES = {
    b"1.1.1.1", b"1.2.3.4", b"93.184.215.14",                                           # résolveur, documentation, example.com
    b"1.13.1.3", b"1.15.1.6", b"1.8.0.0", b"11.3.3.83", b"11.7.3.90", b"12.0.0.61", b"12.0.4.66", b"12.5.8.93",
    b"12.6.3.3", b"12.8.4.1", b"13.0.3.0", b"13.1.1.3", b"3.7.3.0", b"4.6.0.1", b"9.19.0.56", b"9.24.0.43",  # versions
}
CHEMIN_PERSONNEL = re.compile(rb"(/Users/[A-Za-z][A-Za-z0-9._\-]+|[A-Za-z]:\\{1,2}Users\\{1,2}[A-Za-z][A-Za-z0-9._\-]+"
                              rb"|/home/[A-Za-z][A-Za-z0-9._\-]+)")
CHEMINS_PERMIS = re.compile(rb"^(/home/(user|ubuntu|runner|vscode|claude|argon|mitmproxy|agent-home)"
                            rb"|(/Users/|/home/|[A-Za-z]:\\{1,2}Users\\{1,2})(alice|bob|example|exemple|nom|name|username|USERNAME|you))$")   # comptes techniques, noms d'exemple


def _ip_publique(ip: bytes) -> bool:
    import ipaddress
    try:
        return ipaddress.ip_address(ip.decode()).is_global
    except ValueError:
        return False


def personnelles_dans(nom: str, contenu: bytes, exempter_courriel: bool = False) -> list[str]:
    """Données personnelles d'un fichier gardé, et des membres de ses archives : chemin et nature seulement."""
    trouves = []
    if not exempter_courriel and COURRIEL_DE_LAZAR.search(contenu):
        trouves.append(f"{nom} : adresse électronique de Lazar")
    if any(_ip_publique(m.group(1)) and m.group(1) not in IP_PERMISES for m in IPV4.finditer(contenu)):
        trouves.append(f"{nom} : adresse IP publique")
    if any(not CHEMINS_PERMIS.match(m.group(0)) for m in CHEMIN_PERSONNEL.finditer(contenu)):
        trouves.append(f"{nom} : chemin personnel")
    if est_archive(contenu):
        for membre, c in _membres(nom, contenu):
            trouves += personnelles_dans(f"{nom}!{membre}", c)
    return trouves


def valeurs_secretes(environ=None) -> dict[str, bytes]:
    env = os.environ if environ is None else environ
    sortie = {}
    for nom, valeur in env.items():
        v = str(valeur or "").strip()
        if nom.upper().endswith("_FILE") or not NOMS_DE_CLES.search(nom):
            continue
        if len(v) < 20 or v.startswith("/") or any(c.isspace() for c in v) \
                or not (re.search(r"[A-Za-z]", v) and re.search(r"[0-9]", v)):
            continue
        sortie[nom] = v.encode("utf-8")
    return sortie


def secrets_dans(nom: str, contenu: bytes, valeurs: dict[str, bytes]) -> list[str]:
    """Secrets d'un fichier gardé, et des membres de ses archives à toute profondeur : chemin et nature seulement."""
    trouves = [f"{nom} : valeur de {var}" for var, v in valeurs.items() if v and v in contenu]
    trouves += [f"{nom} : {forme}" for forme, motif in FORMES_DE_CLES
                if any(not (forme in FORMES_FACTICES_PERMISES and MARQUE_FACTICE.search(m.group(0)))
                       for m in motif.finditer(contenu))]
    if est_archive(contenu):
        for membre, c in _membres(nom, contenu):
            trouves += secrets_dans(f"{nom}!{membre}", c, valeurs)
    return trouves


def courriels_de_tiers(contenu: bytes) -> int:
    return sum(1 for m in COURRIEL.finditer(contenu)
               if not re.search(rb"(\.invalide?$|@localhost$|@(example|exemple|pytest|README)\.|noreply)", m.group(0), re.I))


EXTENSIONS_D_ARCHIVES = (".zip", ".tar", ".tar.gz", ".tgz", ".bundle")


def _noms_des_membres(nom: str, data: bytes) -> list[str] | None:
    """v8, mode à blanc : noms des membres d'une archive gardée (premier niveau), sans lire leur contenu ; None si
    le format n'est pas examiné ici. Paquet git : noms de l'arbre de chaque commit, aucun objet de fichier lu."""
    try:
        if data[:4] == b"PK\x03\x04":
            with zipfile.ZipFile(io.BytesIO(data)) as z:
                return [i.filename for i in z.infolist() if not i.is_dir()]
        if data[257:262] == b"ustar" or data[:2] == b"\x1f\x8b":
            with tarfile.open(fileobj=io.BytesIO(data), mode="r:*") as t:
                return [m.name[2:] if m.name.startswith("./") else m.name for m in t.getmembers() if m.isfile()]
        if data.startswith((b"# v2 git bundle", b"# v3 git bundle")):
            entete = data.split(b"\n\n", 1)[0]
            if any(l.startswith(b"-") for l in entete.split(b"\n")[1:]):
                return None                                                     # paquet incrémental
            with tempfile.TemporaryDirectory() as d:
                paquet, depot = Path(d) / "paquet.bundle", Path(d) / "depot.git"
                paquet.write_bytes(data)
                _git("init", "-q", "--bare", str(depot), cwd=Path(d))
                tetes = [l.split()[0] for l in _git("bundle", "unbundle", str(paquet), cwd=depot).decode().splitlines() if l]
                noms = set()
                for c in _git("rev-list", *tetes, cwd=depot).decode().split():
                    noms.update(n for n in _git("ls-tree", "-r", "-z", "--name-only", c, cwd=depot).decode().split("\0") if n)
                return sorted(noms)
    except (zipfile.BadZipFile, tarfile.TarError, subprocess.CalledProcessError):
        return None
    return None


def a_blanc(commit: str) -> int:
    """v8 : mode à blanc (v10 : copies par identifiant retirées ou qui arrêtent, comptées). Comptes par motif tirés des noms de l'arbre du commit ; aucun fichier retiré, sous embargo ou
    sensible n'est lu ; seules les archives gardées sont ouvertes, pour les noms de leurs membres. Rien n'est écrit ;
    aucun chemin n'est imprimé, seulement des comptes. Code 0 si les gardes de nom passeraient, 1 sinon."""
    entrees = _entrees(commit)
    classes = classes_d_identifiants(entrees)
    ids_par_nom = frozenset(classes)
    copies_retirees, copies_arret, explicites_sans_objet = copies_par_identifiant(entrees, classes)   # v10
    comptes: dict[str, int] = {}
    par_fragment: dict[str, int] = {f: 0 for f in FRAGMENTS_PERMANENTS}
    par_dossier: dict[str, int] = {}
    hors, gardes, copies, signales, noms_non_prevus, archives, membres_sensibles, membres_retires, non_examinees = (
        0, 0, 0, 0, 0, 0, 0, 0, 0)
    noms_listes_non_prevus = 0                                                  # v10
    for mode, type_, sha, chemin in entrees:
        f = fragment_sensible(chemin)
        if f:
            par_fragment[f] += 1
        if sensible_hors_dossiers(chemin):
            hors += 1
            continue
        if type_ != "blob" or mode == "120000":                                 # lien ou sous-module : non copié
            continue
        raison = motif_de(chemin)
        if raison == RAISON_PERMANENTE:
            par_dossier[chemin.split("/")[0]] = par_dossier.get(chemin.split("/")[0], 0) + 1
        if raison == RAISON_EMBARGO or raison in RAISONS_PAR_NOM:
            comptes[raison] = comptes.get(raison, 0) + 1
            continue
        if chemin in copies_retirees:                                           # v10 : avant la liste ordinaire
            comptes[RAISON_COPIE] = comptes.get(RAISON_COPIE, 0) + 1
            continue
        if raison:
            comptes[raison] = comptes.get(raison, 0) + 1
            if porte_un_fragment_par_nom(chemin) and chemin not in GARDES_SIGNALES:   # v10 : son nom serait listé
                noms_listes_non_prevus += 1
            continue
        gardes += 1
        if porte_un_fragment_par_nom(chemin):                                   # v10 : normalisé
            if chemin in GARDES_SIGNALES:
                signales += 1
            else:
                noms_non_prevus += 1
        if sha in ids_par_nom:
            copies += 1
        if chemin.lower().endswith(EXTENSIONS_D_ARCHIVES):
            archives += 1
            noms = _noms_des_membres(chemin, _git("cat-file", "blob", sha))
            if noms is None:
                non_examinees += 1
                continue
            membres_sensibles += sum(1 for n in noms if fragment_sensible(n))
            membres_retires += sum(1 for n in noms if porte_un_nom_retire(n) or sous_embargo(n)
                                   or any(correspond(n, m) for m, _ in RETRAITS))
    arret = bool(hors or noms_non_prevus or copies or membres_retires or non_examinees   # v9 : non examinée = arrêt
                 or copies_arret or explicites_sans_objet or noms_listes_non_prevus)       # v10
    bilan = {"mode": "à blanc (noms seulement, rien d'écrit)", "commit_source": commit, "chemins_de_l_arbre": len(entrees),
             "fichiers_gardes": gardes, "retraits_par_motif": dict(sorted(comptes.items(), key=lambda x: -x[1])),
             "fichiers_retires_permanents": comptes.get(RAISON_PERMANENTE, 0),
             "chemins_sensibles_par_fragment": par_fragment, "retraits_permanents_par_dossier": par_dossier,
             "chemins_sensibles_hors_dossiers_vises": hors, "chemins_gardes_portant_un_nom_retire_non_prevus": noms_non_prevus,
             "chemins_gardes_signales": signales, "identifiants_git_retires_par_nom": len(ids_par_nom),
             "fichiers_gardes_meme_identifiant_qu_un_retire_par_nom": copies,
             "copies_retirees_par_identifiant_avec_compagnons": len(copies_retirees),
             "copies_d_un_fichier_sensible_ou_sous_embargo_qui_arretent": len(copies_arret),
             "retraits_par_identifiant_explicites_presents": sum(
                 1 for _, _, _, c in entrees if c in RETRAITS_PAR_IDENTIFIANT_EXPLICITES),
             "retraits_par_identifiant_explicites_sans_objet": len(explicites_sans_objet),
             "chemins_retires_avec_liste_portant_un_nom_retire_non_prevus": noms_listes_non_prevus,
             "archives_gardees_par_extension": archives, "archives_non_examinees_ici": non_examinees,
             "membres_d_archive_portant_un_nom_sensible": membres_sensibles,
             "membres_d_archive_qui_arreteraient_par_nom": membres_retires,
             "verdict": "arrêt" if arret else "les gardes de nom passeraient (gardes de contenu non jouées)"}
    print(json.dumps(bilan, ensure_ascii=False, indent=1))
    return 1 if arret else 0


def main(argv: list[str]) -> int:
    if len(argv) == 2 and argv[1] == "--a-blanc":
        return a_blanc(_git("rev-parse", "--verify", argv[0] + "^{commit}").decode().strip())
    readme_public = None
    if len(argv) == 4 and argv[2] == "--readme":
        readme_public = Path(argv[3]).read_text(encoding="utf-8")
        argv = argv[:2]
    if len(argv) != 2:
        print(__doc__)
        return 2
    commit = _git("rev-parse", "--verify", argv[0] + "^{commit}").decode().strip()
    sortie = Path(argv[1]).resolve()
    if sortie.exists():
        print(f"{sortie} existe déjà : on n'écrase jamais (R12)", file=sys.stderr)
        return 2
    if RACINE.resolve() in (sortie, *sortie.parents):
        print("SORTIE ne doit pas être dans le dépôt", file=sys.stderr)
        return 2
    entrees = _entrees(commit)                   # v10 : copies par identifiant, jugées sur l'arbre avant toute lecture
    classes = classes_d_identifiants(entrees)
    copies_retirees, copies_arret, explicites_sans_objet = copies_par_identifiant(entrees, classes)
    if copies_arret:
        print("fichiers non retirés par nom qui ont l'identifiant d'objet git d'un fichier sous embargo, retiré à titre "
              "permanent ou chargé par le code, sans retrait explicite (RETRAITS_PAR_IDENTIFIANT_EXPLICITES) : jamais "
              "lus ; arrêt (aucun paquet écrit)\n  " + "\n  ".join(copies_arret), file=sys.stderr)
        return 1
    if explicites_sans_objet:
        print("RETRAITS_PAR_IDENTIFIANT_EXPLICITES nomme des chemins de l'arbre qui ne sont plus des copies d'un fichier "
              "retiré par nom : liste à revoir ; arrêt (aucun paquet écrit)\n  " + "\n  ".join(explicites_sans_objet),
              file=sys.stderr)
        return 1
    arbre = sortie / "controle-ia-expurge"
    arbre.mkdir(parents=True)
    retraits, embargo, gardes, archives, empreintes_gardees = [], [], 0, [], set()
    valeurs, secrets, personnelles, tiers = valeurs_secretes(), [], [], 0
    par_nom: dict[str, int] = {}                 # v7 : raison -> nombre ; jamais de chemin
    identifiants = frozenset(classes)            # v7 : lus dans l'arbre, sans lire les fichiers (v10 : embargo compris)
    copies, noms_non_prevus, signales = [], [], []
    noms_listes_non_prevus = []                  # v10 : retirés avec liste, dont le nom porte un nom retiré
    hors_dossiers = []                           # v8 : chemins sensibles hors des dossiers visés, jamais lus
    with tarfile.open(fileobj=io.BytesIO(_git("archive", "--format=tar", commit))) as tar:
        for membre in tar.getmembers():
            if sensible_hors_dossiers(membre.name):     # v8 : avant tout le reste, liens et dossiers compris
                hors_dossiers.append(membre.name)
                continue
            if not membre.isfile():
                continue
            raison = motif_de(membre.name)
            if raison == RAISON_EMBARGO:            # jamais lu : ni contenu, ni empreinte, ni taille
                embargo.append(membre.name)
                continue
            if raison in RAISONS_PAR_NOM:           # v7 : jamais lu : ni contenu, ni empreinte, ni taille
                par_nom[raison] = par_nom.get(raison, 0) + 1
                continue
            if membre.name in copies_retirees:      # v10 : copie d'un fichier retiré par nom : jamais lue, comptée
                par_nom[RAISON_COPIE] = par_nom.get(RAISON_COPIE, 0) + 1
                continue
            if raison and porte_un_fragment_par_nom(membre.name) and membre.name not in GARDES_SIGNALES:
                noms_listes_non_prevus.append(membre.name)     # v10 : son chemin serait listé dans EXPURGE.md
                continue
            contenu = tar.extractfile(membre).read()
            if raison:
                retraits.append({"chemin": membre.name, "sha256": hashlib.sha256(contenu).hexdigest(),
                                 "octets": len(contenu), "motif": raison})
                continue
            if fragment_sensible(membre.name):          # v8 : garde redondante ; aucune exception nommée
                noms_non_prevus.append(membre.name)
            elif porte_un_fragment_par_nom(membre.name):  # v7 : nom retiré hors des dossiers visés (v10 : normalisé)
                (signales if membre.name in GARDES_SIGNALES else noms_non_prevus).append(membre.name)
            if contenu and identifiant_git(contenu) in identifiants:           # v7 : copie d'un fichier retiré par nom
                copies.append(membre.name)
            cible = arbre / membre.name
            cible.parent.mkdir(parents=True, exist_ok=True)
            cible.write_bytes(contenu)
            os.chmod(cible, membre.mode & 0o777)
            gardes += 1
            empreintes_gardees.add(hashlib.sha256(contenu).hexdigest())
            secrets += secrets_dans(membre.name, contenu, valeurs)
            # le README du dépôt privé est remplacé par le README public (`--readme`) : il n'est pas publié
            personnelles += personnelles_dans(membre.name, contenu,
                                              exempter_courriel=(readme_public is not None and membre.name == "README.md"))
            tiers += courriels_de_tiers(contenu)
            if est_archive(contenu) or contenu.startswith(COMPRESSIONS_NON_EXAMINEES):
                archives.append((membre.name, contenu))
    if hors_dossiers:
        print("chemins dont un segment porte un nom sensible (" + ", ".join(FRAGMENTS_PERMANENTS) + ") hors des "
              "dossiers visés (" + ", ".join(DOSSIERS_PERMANENTS) + ") : jamais lus ; arrêt (aucun paquet écrit)\n  "
              + "\n  ".join(hors_dossiers), file=sys.stderr)
        return 1
    if noms_non_prevus:
        print("chemins gardés dont le nom porte un nom retiré (" + ", ".join(FRAGMENTS_PAR_NOM) + ") hors des dossiers "
              "visés et hors de GARDES_SIGNALES : arrêt (aucun paquet écrit)\n  " + "\n  ".join(noms_non_prevus),
              file=sys.stderr)
        return 1
    if noms_listes_non_prevus:
        print("chemins retirés avec liste dont le nom porte un nom retiré (" + ", ".join(FRAGMENTS_PAR_NOM) + ") : leur "
              "chemin paraîtrait dans EXPURGE.md ; arrêt (aucun paquet écrit)\n  " + "\n  ".join(noms_listes_non_prevus),
              file=sys.stderr)
        return 1
    if copies:
        print("fichiers gardés qui ont l'identifiant d'objet git d'un fichier retiré par nom : arrêt (aucun paquet écrit)"
              "\n  " + "\n  ".join(copies), file=sys.stderr)
        return 1
    if secrets:
        print("secrets dans des fichiers gardés : arrêt (aucun paquet écrit)\n  " + "\n  ".join(secrets), file=sys.stderr)
        return 1
    if personnelles:
        print("données personnelles dans des fichiers gardés : arrêt (aucun paquet écrit)\n  " + "\n  ".join(personnelles),
              file=sys.stderr)
        return 1
    empreintes = {r["sha256"] for r in retraits if r["octets"]} - empreintes_gardees
    trouves = [t for nom, contenu in archives for t in survivants(nom, contenu, empreintes, identifiants)]
    if trouves:
        print("fichiers retirés qui survivent dans une archive gardée : arrêt (aucun paquet écrit)\n  "
              + "\n  ".join(trouves), file=sys.stderr)
        return 1
    readme = arbre / "README.md"
    if readme_public is not None:
        # README public fourni (R-2433) : la garde des secrets s'y applique ; l'adresse de contact que Lazar y a choisie
        # est publiée depuis le 9 octobre et reste.
        s = secrets_dans("README.md (public)", readme_public.encode("utf-8"), valeurs)
        p = [x for x in personnelles_dans("README.md (public)", readme_public.encode("utf-8"), exempter_courriel=True)]
        if s or p:
            print("README public : " + "; ".join(s + p) + " : arrêt (aucun paquet écrit)", file=sys.stderr)
            return 1
        readme.write_text(readme_public, encoding="utf-8")
    else:
        texte = readme.read_text(encoding="utf-8")
        if texte.count(PARAGRAPHE_README) != 1:
            print("paragraphe du README introuvable : arrêt (aucun paquet écrit)", file=sys.stderr)
            return 1
        texte = texte.replace(PARAGRAPHE_README, REMPLACEMENT_README)
        for avant, apres in REMPLACEMENTS_FACULTATIFS:
            if texte.count(avant) > 1:
                print(f"renvoi du README ambigu : {avant!r} : arrêt (aucun paquet écrit)", file=sys.stderr)
                return 1
            texte = texte.replace(avant, apres)
        readme.write_text(texte, encoding="utf-8")
    pdf = sorted(r["chemin"] for r in retraits if r["chemin"].startswith("docs/sources/pdf/") and r["chemin"].endswith(".pdf"))
    comptes: dict[str, int] = {}
    for r in retraits:
        comptes[r["motif"]] = comptes.get(r["motif"], 0) + 1
    if embargo:
        comptes[RAISON_EMBARGO] = len(embargo)
    comptes.update(par_nom)
    n_par_nom = sum(par_nom.values())
    moi = Path(__file__).resolve()
    ici = "scripts/" + moi.name
    try:                                         # v7 : le script peut être postérieur au commit source
        au_commit = _git("rev-parse", "--verify", "-q", f"{commit}:{ici}").decode().strip()
    except subprocess.CalledProcessError:
        au_commit = ""
    origine = "(same commit)" if au_commit == identifiant_git(moi.read_bytes()) else (
        f"(written after that commit, so absent from this copy; SHA-256 `{hashlib.sha256(moi.read_bytes()).hexdigest()}`)")
    lignes = ["# What this copy omits", "",
              f"Copy of the private working repository `controle-ia-travail` at commit `{commit}`, made by "
              f"`{ici}` {origine}. Omitted: third-party texts that the code does not need "
              "(paper PDFs and extracted pages, copies of web pages), applications to funders and personal data, "
              "the working registers (`registres/`), and the paths under embargo until the sealed verdict of the "
              "P3-bis experiment (raw outputs of runs 7a and 7b, their readings, and one labeller run), which "
              "protect the validity of gates G1 and P3-bis and will be published after that verdict. Also omitted, "
              "by name and without being read: drafts that stay in the private repository "
              "(`brouillons/pain-axis-*`), notes of another project, and, permanently (not lifted with the embargo), "
              "the attack arm, the held-out sabotage mode and the sensitive families (design of covert sabotage "
              "organisms, monitor evasion, red-team and saboteur design notes), with their companion hash files; "
              "and kept-looking files that are byte-identical copies of a file withheld by name (same git object "
              "identifier), with their companion hash files. The SHA-256 hashes of the "
              "omitted files remain (companion `.sha256` files, and the table below), except for the embargoed paths "
              "and the paths withheld by name, which are counted only. Before writing the copy, the "
              f"script checked that no omitted file survives inside a kept archive ({len(archives)} files in zip, "
              "tar or git bundle format, searched at any depth, by hash and by path), that no kept file holds a key "
              "or token, that no kept file holds a personal address, path or public IP address, that no kept "
              "file or archive member is a copy of a file withheld by name (same git object identifier), and that "
              "no kept path or archive member carries a name withheld permanently.", "",
              "`python -m controle_ia.scellement verifier-arbre .` reports each omitted sealed file as an orphan "
              "hash; that is expected.", "",
              f"- Files kept: {gardes}. Files omitted: {len(retraits) + len(embargo) + n_par_nom} "
              f"({len(retraits)} listed below, {len(embargo)} under embargo, counted only, "
              f"{n_par_nom} withheld by name, counted only).",
              "- Kept on purpose: the prompt texts transcribed from arXiv 2606.08892 "
              "(`docs/sources/invites-2606.08892-v1/invites/`) and from arXiv 2606.07054 "
              "(`docs/sources/invites-2606.07054-v1/invites/`), and the templates adapted from the latter "
              "(`docs/sources/invites-2606.07054-v1/derivees/`): the code and its tests load them after checking "
              "their hashes.", "",
              "## Omitted files by reason", "", "| reason (in French) | files |", "|---|---|"]
    lignes += [f"| {m} | {n} |" for m, n in sorted(comptes.items(), key=lambda x: -x[1])]
    lignes += ["", "## arXiv papers whose PDF copies are omitted", ""]
    lignes += [f"- [{Path(p).stem}](https://arxiv.org/abs/{Path(p).stem})" for p in pdf
               if re.fullmatch(r"\d{4}\.\d{4,5}(v\d+)?", Path(p).stem)]
    lignes += ["", "## Omitted files (embargoed paths and paths withheld by name excepted)", "", "| path | SHA-256 | reason (in French) |", "|---|---|---|"]
    lignes += [f"| `{r['chemin']}` | `{r['sha256']}` | {r['motif']} |" for r in retraits]
    (arbre / "EXPURGE.md").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    date = _git("show", "-s", "--format=%cI", commit).decode().strip()
    env = dict(os.environ, GIT_AUTHOR_NAME="controle-ia (copie expurgée)", GIT_AUTHOR_EMAIL="copie-expurgee@invalid",
               GIT_COMMITTER_NAME="controle-ia (copie expurgée)", GIT_COMMITTER_EMAIL="copie-expurgee@invalid",
               GIT_AUTHOR_DATE=date, GIT_COMMITTER_DATE=date)
    _git("init", "-q", "-b", "main", cwd=arbre, env=env)
    _git("add", "-A", cwd=arbre, env=env)
    _git("-c", "commit.gpgsign=false", "commit", "-q", "-m",
         f"Copie expurgée de controle-ia-travail au commit {commit} (voir EXPURGE.md)", cwd=arbre, env=env)
    copie = _git("rev-parse", "HEAD", cwd=arbre).decode().strip()
    paquet = sortie / f"controle-ia-expurge-{commit[:7]}.bundle"
    _git("bundle", "create", "-q", str(paquet), "HEAD", "main", cwd=arbre, env=env)
    bilan = {"commit_source": commit, "commit_copie": copie, "fichiers_gardes": gardes,
             "fichiers_retires": len(retraits), "fichiers_sous_embargo": len(embargo),
             "fichiers_retires_par_nom": n_par_nom, "retraits_par_nom_par_motif": par_nom,
             "identifiants_git_retires_par_nom": len(identifiants), "chemins_gardes_signales": signales,
             "copies_retirees_par_identifiant_avec_compagnons": par_nom.get(RAISON_COPIE, 0),
             "script": ici, "script_sha256": hashlib.sha256(moi.read_bytes()).hexdigest(),
             "archives_examinees": len(archives),
             "courriels_de_tiers_gardes": tiers, "retraits_par_motif": comptes,
             "paquet": paquet.name, "paquet_sha256": hashlib.sha256(paquet.read_bytes()).hexdigest(),
             "retraits": retraits}
    (sortie / "bilan.json").write_text(json.dumps(bilan, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in bilan.items() if k != "retraits"}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
