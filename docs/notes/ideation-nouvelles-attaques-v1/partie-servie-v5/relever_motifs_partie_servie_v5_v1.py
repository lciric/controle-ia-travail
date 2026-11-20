"""Relevé des motifs internes sur le gabarit de la partie servie de la question v5 — v1.

Lit le gabarit, compte chaque motif, éprouve chaque motif sur un témoin
positif, écrit le relevé. Aucune autre opération. Le relevé ne porte que des
noms de motifs et des comptes : ni le prénom ni le nom du directeur n'y sont
écrits. Bibliothèque standard seule. Aucun argument.

Signé : dériveur neuf, modèle F.
"""

import hashlib
import json
import re
import sys
import unicodedata

DOSSIER = (
    "/tmp/claude-0/-home-user-controle-ia-travail/"
    "16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/"
    "derivation-partie-servie-v5/"
)
GABARIT = DOSSIER + "partie-servie-question-v5-v1.md"
RELEVE = DOSSIER + "releve-motifs-partie-servie-v5-v1.json"

BRUT = "texte brut"
PLIE = "casse repliée, accents retirés, apostrophes unifiées"

# (nom affiché, forme lue, expression, témoin positif)
MOTIFS = (
    ("prénom du directeur", PLIE, r"\blazar\b", "mot de Lazar"),
    ("nom du directeur", PLIE, r"ciric", "L. Ćirić"),
    ("identifiant de session", PLIE, r"session_", "session_01ABC"),
    ("arobase", BRUT, r"@", "a@b.c"),
    ("R- ou N- suivi de chiffres", BRUT, r"\b[RN]-\d", "voir R-3661 et N-060"),
    ("identifiant d'accord GO-20", PLIE, r"go-20", "GO-2026-11-20-44"),
    ("nom du compte distant", PLIE, r"lciric", "lciric/x"),
    ("github", PLIE, r"github", "https://GitHub.com"),
    ("nom du dépôt", PLIE, r"controle-ia", "contrôle-ia-travail"),
    ("chemin docs/", PLIE, r"docs/", "docs/notes"),
    ("chemin prereg/", PLIE, r"prereg/", "prereg/x.md"),
    ("chemin registres/", PLIE, r"registres/", "registres/go.md"),
    ("chemin donnees/", PLIE, r"donnees/", "données/x"),
    ("chaîne hexadécimale de 16 caractères et plus", BRUT, r"[0-9a-fA-F]{16,}", "eaf5db8a558547aa"),
    ("fichier des consignes permanentes", PLIE, r"claude\.md", "CLAUDE.md"),
    ("nom de clé en _KEY", PLIE, r"_key", "X_API_KEY"),
    ("nom de clé en _TOKEN", PLIE, r"_token", "HCLOUD_TOKEN"),
    ("famille tenue à l'écart", PLIE, r"famille(?: de cases)? tenue a l'ecart", "la famille de cases tenue à l’écart"),
    ("tenue à l'écart", PLIE, r"tenu(?:e|es|s)? a l'ecart", "un mode tenu à l'écart"),
    ("à l'écart", PLIE, r"a l'ecart", "mise à l'écart"),
    ("source", PLIE, r"source", "| Source |"),
    ("compte des cases : 120", BRUT, r"\b120\b", "Soit 120 cases"),
    ("compte des cases : produit", BRUT, r"\d\s*[×x*]\s*\d", "6 × 5 × 4"),
    ("compte des cases : nombre suivi de « cases »", PLIE, r"\d+\s+cases\b", "20 cases"),
    ("accolades hors de l'emplacement de case", BRUT, r"[{}]", "{"),
)

EMPLACEMENT = "{{CASE}}\n"


def plier(texte):
    decompose = unicodedata.normalize("NFKD", texte)
    sans_accents = "".join(c for c in decompose if not unicodedata.combining(c))
    return sans_accents.casefold().replace("’", "'").replace("ʼ", "'")


def compter(expression, forme, texte):
    lu = plier(texte) if forme == PLIE else texte
    return len(re.findall(expression, lu))


def main():
    with open(GABARIT, "rb") as flux:
        octets = flux.read()
    texte = octets.decode("utf-8")
    if texte.count(EMPLACEMENT) != 1:
        sys.stderr.write("ARRÊT : emplacement de case absent ou répété\n")
        sys.exit(1)
    sans_emplacement = texte.replace(EMPLACEMENT, "\n")

    lignes = []
    total = 0
    temoins_muets = 0
    for nom, forme, expression, temoin in MOTIFS:
        compte = compter(expression, forme, sans_emplacement)
        mord = compter(expression, forme, temoin) > 0
        total += compte
        if not mord:
            temoins_muets += 1
        lignes.append(
            {
                "motif": nom,
                "forme_lue": forme,
                "occurrences": compte,
                "temoin_positif_mord": mord,
            }
        )

    releve = {
        "piece": "relevé des motifs internes sur le gabarit de la partie servie de la question v5 — v1",
        "signe": "dériveur neuf, modèle F",
        "gabarit": {
            "chemin": GABARIT,
            "sha256": hashlib.sha256(octets).hexdigest(),
            "taille_octets": len(octets),
        },
        "lu_sans": "la ligne de l'emplacement de case, comptée à part",
        "emplacement_de_case_occurrences": texte.count("{{CASE}}"),
        "motifs": lignes,
        "total_occurrences": total,
        "attendu": 0,
        "temoins_positifs_muets": temoins_muets,
        "conforme": total == 0 and temoins_muets == 0,
    }
    sortie = json.dumps(releve, ensure_ascii=False, indent=2) + "\n"
    with open(RELEVE, "wb") as flux:
        flux.write(sortie.encode("utf-8"))
    if not releve["conforme"]:
        sys.stderr.write("ARRÊT : relevé non conforme, voir le fichier écrit\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
