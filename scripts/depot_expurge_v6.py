"""Version 6 (12 novembre 2026, R-2433) : v5 + chemins sous embargo jusqu'au verdict scellé de P3-bis (filtrés par nom
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

    .venv/bin/python scripts/depot_expurge_v6.py COMMIT SORTIE [--readme README_PUBLIC]
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
    if sous_embargo(chemin):
        if any(correspond(chemin, g) for g in GARDES):
            raise SystemExit(f"{chemin} : sous embargo mais chargé par le code : arrêt (aucun paquet écrit)")
        return RAISON_EMBARGO
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


def _membres_paquet(data: bytes) -> list[tuple[str, bytes]]:
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
        objets = sorted({sha for _, sha in paires})
        sortie, contenus, i = _git("cat-file", "--batch", cwd=depot, entree="\n".join(objets).encode() + b"\n"), {}, 0
        for sha in objets:
            fin = sortie.index(b"\n", i)
            taille = int(sortie[i:fin].split()[2])
            contenus[sha] = sortie[fin + 1:fin + 1 + taille]
            i = fin + 1 + taille + 1
        return sorted((chemin, contenus[sha]) for chemin, sha in paires)


def _membres(nom: str, data: bytes) -> list[tuple[str, bytes]]:
    if data[:4] == b"PK\x03\x04":
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            membres = [(i.filename, z.read(i)) for i in z.infolist() if not i.is_dir()]
    elif data[257:262] == b"ustar":
        with tarfile.open(fileobj=io.BytesIO(data)) as t:
            membres = [(m.name, t.extractfile(m).read()) for m in t.getmembers() if m.isfile()]
    elif data[:2] == b"\x1f\x8b":  # v4 : archive tar compressée par gzip (.tar.gz, .tgz), examinée comme un tar
        try:
            with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as t:
                membres = [(m.name, t.extractfile(m).read()) for m in t.getmembers() if m.isfile()]
        except tarfile.TarError:
            raise SystemExit(f"{nom} : gzip qui n'est pas un tar : format non examiné : arrêt (aucun paquet écrit)")
    elif data.startswith((b"# v2 git bundle", b"# v3 git bundle")):
        membres = _membres_paquet(data)
    elif data.startswith(COMPRESSIONS_NON_EXAMINEES):
        raise SystemExit(f"{nom} : archive d'un format non examiné : arrêt (aucun paquet écrit)")
    else:
        return []
    return [(m[2:] if m.startswith("./") else m, c) for m, c in membres]


def survivants(nom: str, data: bytes, empreintes: set[str]) -> list[str]:
    """Fichiers retirés qui survivent dans une archive gardée (zip, tar ou paquet git, à toute profondeur) : même
    empreinte qu'un fichier retiré, ou chemin visé par un retrait."""
    trouves = []
    for membre, contenu in _membres(nom, data):
        chemin = f"{nom}!{membre}"
        if (contenu and hashlib.sha256(contenu).hexdigest() in empreintes) or sous_embargo(membre) or any(
                correspond(membre, motif) for motif, _ in RETRAITS):
            trouves.append(chemin)
        trouves += survivants(chemin, contenu, empreintes)
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


def main(argv: list[str]) -> int:
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
    arbre = sortie / "controle-ia-expurge"
    arbre.mkdir(parents=True)
    retraits, embargo, gardes, archives, empreintes_gardees = [], [], 0, [], set()
    valeurs, secrets, personnelles, tiers = valeurs_secretes(), [], [], 0
    with tarfile.open(fileobj=io.BytesIO(_git("archive", "--format=tar", commit))) as tar:
        for membre in tar.getmembers():
            if not membre.isfile():
                continue
            raison = motif_de(membre.name)
            if raison == RAISON_EMBARGO:            # jamais lu : ni contenu, ni empreinte, ni taille
                embargo.append(membre.name)
                continue
            contenu = tar.extractfile(membre).read()
            if raison:
                retraits.append({"chemin": membre.name, "sha256": hashlib.sha256(contenu).hexdigest(),
                                 "octets": len(contenu), "motif": raison})
                continue
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
    if secrets:
        print("secrets dans des fichiers gardés : arrêt (aucun paquet écrit)\n  " + "\n  ".join(secrets), file=sys.stderr)
        return 1
    if personnelles:
        print("données personnelles dans des fichiers gardés : arrêt (aucun paquet écrit)\n  " + "\n  ".join(personnelles),
              file=sys.stderr)
        return 1
    empreintes = {r["sha256"] for r in retraits if r["octets"]} - empreintes_gardees
    trouves = [t for nom, contenu in archives for t in survivants(nom, contenu, empreintes)]
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
    lignes = ["# What this copy omits", "",
              f"Copy of the private working repository `controle-ia-travail` at commit `{commit}`, made by "
              "`scripts/depot_expurge_v6.py` (same commit). Omitted: third-party texts that the code does not need "
              "(paper PDFs and extracted pages, copies of web pages), applications to funders and personal data, "
              "the working registers (`registres/`), and the paths under embargo until the sealed verdict of the "
              "P3-bis experiment (attack arm, held-out sabotage mode, raw outputs of runs 7a and 7b, their readings, "
              "and one labeller run), which protect the validity of gates G1 and P3-bis and will be published after "
              "that verdict. The SHA-256 hashes of the omitted files remain (companion `.sha256` files, and the "
              "table below), except for the embargoed paths, which are counted only. Before writing the copy, the "
              f"script checked that no omitted file survives inside a kept archive ({len(archives)} files in zip, "
              "tar or git bundle format, searched at any depth, by hash and by path), that no kept file holds a key "
              "or token, and that no kept file holds a personal address, path or public IP address.", "",
              "`python -m controle_ia.scellement verifier-arbre .` reports each omitted sealed file as an orphan "
              "hash; that is expected.", "",
              f"- Files kept: {gardes}. Files omitted: {len(retraits) + len(embargo)} "
              f"({len(retraits)} listed below, {len(embargo)} under embargo, counted only).",
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
    lignes += ["", "## Omitted files (embargoed paths excepted)", "", "| path | SHA-256 | reason (in French) |", "|---|---|---|"]
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
             "fichiers_retires": len(retraits), "fichiers_sous_embargo": len(embargo), "archives_examinees": len(archives),
             "courriels_de_tiers_gardes": tiers, "retraits_par_motif": comptes,
             "paquet": paquet.name, "paquet_sha256": hashlib.sha256(paquet.read_bytes()).hexdigest(),
             "retraits": retraits}
    (sortie / "bilan.json").write_text(json.dumps(bilan, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in bilan.items() if k != "retraits"}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
