"""Vérification indépendante de la partie servie de la question v5 — contre-lecture v1.

Écrit sans reprendre le code du dériveur. Lit la question v5 (copie tirée de
origin/main), le gabarit et le journal rendus par le dériveur, et le gabarit
rejoué. Refait l'extraction par une autre voie (découpage des lignes par
splitlines, retrait de colonne par découpage des cellules), compare à l'octet,
vérifie l'emplacement de case et l'absence d'accolade, rapporte chaque ligne
du gabarit à sa ligne de la source, calcule le repli sans légende, fait un
relevé de motifs à soi (sur le gabarit et sur la requête assemblée pour chaque
case de la légende), compte à part les rouages de la course nommés dans le
texte servi. Écrit un seul fichier de sortie. Bibliothèque standard seule.
Aucun argument. Le prénom et le nom du directeur ne sont jamais écrits dans la
sortie : seuls les noms de motifs et les comptes y sont.

Signé : contre-lecteur neuf, modèle O.
"""

import hashlib
import json
import platform
import re
import sys
import unicodedata

RACINE = (
    "/tmp/claude-0/-home-user-controle-ia-travail/"
    "16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/"
    "contre-lecture-partie-servie-v5/"
)
SOURCE = RACINE + "sources/question-v5.md"
GABARIT_REJOUE = RACINE + "partie-servie-question-v5-v1.md"
P = (
    "/home/user/controle-ia-travail/docs/notes/"
    "ideation-nouvelles-attaques-v1/partie-servie-v5/"
)
GABARIT_RENDU = P + "partie-servie-question-v5-v1.md"
JOURNAL_RENDU = P + "journal-derivation-partie-servie-v5-v1.json"
SORTIE = RACINE + "verification-partie-servie-v5-v1.json"

SHA_SOURCE = "eaf5db8a558547aa8f5df45008a34eebf4cb7a163e12ca400176401de6f5ce0f"
SHA_GABARIT = "4cd360baea1076ec2b19b2c7ba85675e739bc3104c709d4fd57c0769975b1cf1"

CASE = b"{{CASE}}\n"
LIGNES_TABLE = (56, 60)


def sha(octets):
    return hashlib.sha256(octets).hexdigest()


def lire(chemin):
    with open(chemin, "rb") as flux:
        return flux.read()


def lignes_de(source, debut, fin):
    toutes = source.splitlines(keepends=True)
    return toutes[debut - 1 : fin]


def retirer_troisieme_colonne(ligne):
    """Découpe en cellules par la barre ; garde les deux premières."""
    corps = ligne[:-1] if ligne.endswith(b"\n") else ligne
    cellules = corps.split(b"|")
    # forme attendue : ['', c1, c2, c3, '']
    if len(cellules) != 5 or cellules[0] != b"" or cellules[4] != b"":
        raise ValueError("forme de ligne de table inattendue")
    gardee = b"|".join(cellules[:3]) + b"|\n"
    return gardee, cellules[1], cellules[2], cellules[3]


def plier(texte):
    d = unicodedata.normalize("NFKD", texte)
    d = "".join(c for c in d if not unicodedata.combining(c))
    return d.casefold().replace("’", "'").replace("ʼ", "'")


# (nom, expression sur le texte plié sauf si brut=True, témoin positif, brut)
MOTIFS_INTERNES = (
    ("prénom du directeur", r"lazar", "mot de L" + "azar", False),
    ("nom du directeur", r"ciric", "L. Ćirić", False),
    ("directeur nommé par sa fonction", r"directeur", "le directeur du programme", False),
    ("la mère (session)", r"\bmere\b", "la mère scelle", False),
    ("identifiant de session", r"session_", "session_01X", False),
    ("arobase", r"@", "a@b", True),
    ("R- ou N- suivi de chiffres", r"\b[rn]-\d", "R-3661, N-060", False),
    ("règle Rn sans tiret", r"\br\d{1,3}\b", "règle R8", False),
    ("identifiant GO-", r"\bgo-", "GO-2026-11-20-46", False),
    ("compte distant", r"lciric", "lciric/x", False),
    ("github", r"github", "GitHub", False),
    ("nom du dépôt", r"controle[-_]ia", "controle_ia", False),
    ("dépôt", r"\bdepot", "pièces du dépôt", False),
    ("chemin docs/", r"docs/", "docs/x", False),
    ("chemin prereg/", r"prereg/", "prereg/x", False),
    ("chemin registres/", r"registres/", "registres/go.md", False),
    ("chemin donnees/", r"donnees/", "données/x", False),
    ("chemin scripts/ ou src/", r"\b(?:scripts|src)/", "scripts/x.py", False),
    ("extension de fichier", r"\.(?:md|py|json|txt|sha256)\b", "note-v3.md", False),
    ("chaîne hexadécimale de 8 et plus", r"[0-9a-f]{8,}", "eaf5db8a", False),
    ("fichier des consignes permanentes", r"claude\.md", "CLAUDE.md", False),
    ("nom de clé _key ou _token", r"_(?:key|token)\b", "HCLOUD_TOKEN", False),
    ("signe de section", r"§", "§ 5", True),
    ("tenue à l'écart", r"tenu(?:e|es|s)? a l'ecart", "famille tenue à l’écart", False),
    ("à l'écart", r"a l'ecart", "mise à l'écart", False),
    ("source", r"source", "| source |", False),
    ("provenance", r"provenance", "sa provenance", False),
    ("compte des cases : 120", r"\b120\b", "120 cases", True),
    ("compte des cases : produit", r"\d\s*[x×*]\s*\d", "6 × 5", True),
    ("compte des cases : nombre et « cases »", r"\d+\s+cases\b", "20 cases", False),
    ("tirage", r"tirage", "le tirage", False),
    ("génération", r"generation", "par génération", False),
    ("ordre de course", r"ordre de course", "ordre de course v3", False),
    ("préenregistrement", r"preenregistrement", "préenregistrement court", False),
    ("devis", r"\bdevis\b", "le devis", False),
    ("décision du programme", r"\bdecision", "décision du programme", False),
    ("hypothèses du programme", r"hypotheses? du programme", "hypothèses du programme", False),
    ("consignes permanentes", r"consignes? permanentes?", "consignes permanentes", False),
    ("version de pièce vN", r"\bv\d\b", "question v5", False),
    ("nom de maison ou de modèle",
     r"\b(?:claude|anthropic|fable|opus|sonnet|haiku|gpt|openai|gemini|llama|mistral|qwen|deepseek|grok)\b",
     "Opus", False),
    ("accolade", r"[{}]", "{", True),
)

# Rouages de la course nommés dans le texte servi : compte informatif, sans attente.
ROUAGES = (
    ("portier", r"\bportier\b"),
    ("coffre", r"\bcoffre\b"),
    ("classe « hors case »", r"hors case"),
    ("registre servi", r"registre servi"),
    ("glisse vers le concret", r"glisse vers le concret"),
    ("pièce produite publique ou scellée", r"piece_produite"),
    ("monde planté", r"monde plante"),
    ("oracle", r"\boracle\b"),
)

INVISIBLES = ("​", "‌", "‍", "‎", "‏", "⁠", "﻿", "­")


def compter(expression, texte, brut):
    return len(re.findall(expression, texte if brut else plier(texte)))


def releve(texte):
    lignes = []
    total = 0
    muets = 0
    for nom, expr, temoin, brut in MOTIFS_INTERNES:
        n = compter(expr, texte, brut)
        mord = compter(expr, temoin, brut) > 0
        total += n
        muets += 0 if mord else 1
        lignes.append({"motif": nom, "occurrences": n, "temoin_mord": mord})
    return lignes, total, muets


def main():
    echecs = []

    def exiger(condition, message):
        if not condition:
            echecs.append(message)

    source = lire(SOURCE)
    exiger(sha(source) == SHA_SOURCE, "empreinte de la source")
    toutes = source.splitlines(keepends=True)
    exiger(len(toutes) == 74, "74 lignes dans la source")

    rendu = lire(GABARIT_RENDU)
    rejoue = lire(GABARIT_REJOUE)
    exiger(sha(rendu) == SHA_GABARIT, "empreinte du gabarit rendu")
    exiger(rendu == rejoue, "gabarit rejoué égal au rendu")

    # Accolades dans la source.
    accolades_source = source.count(b"{") + source.count(b"}")
    exiger(accolades_source == 0, "aucune accolade dans la v5")

    # Extraction indépendante.
    zones = {
        "question": lignes_de(source, 42, 51),
        "vide_55": lignes_de(source, 55, 55),
        "table": lignes_de(source, 56, 60),
        "vide_61": lignes_de(source, 61, 61),
        "champs": lignes_de(source, 64, 66),
    }
    table_servie = []
    colonnes = []
    for rang, ligne in enumerate(zones["table"]):
        gardee, c1, c2, c3 = retirer_troisieme_colonne(ligne)
        exiger(ligne.startswith(gardee[:-1]), "colonnes gardées égales à l'octet, ligne %d" % (56 + rang))
        exiger(ligne[len(gardee) - 1 :] == c3 + b"|\n", "seule la troisième cellule est retirée, ligne %d" % (56 + rang))
        table_servie.append(gardee)
        colonnes.append((c1, c2, c3))
    exiger(colonnes[0][2].strip() == b"source", "la cellule retirée de l'en-tête est « source »")
    exiger(set(colonnes[1][2]) <= set(b"-"), "la cellule retirée du séparateur n'est que des tirets")

    mien = (
        b"".join(zones["question"])
        + CASE
        + b"".join(zones["vide_55"])
        + b"".join(table_servie)
        + b"".join(zones["vide_61"])
        + b"".join(zones["champs"])
    )
    exiger(mien == rendu, "extraction indépendante égale au gabarit rendu")

    # Empreintes de zones contre le journal.
    journal = json.loads(lire(JOURNAL_RENDU).decode("utf-8"))
    attendu = {
        (42, 51): (b"".join(zones["question"]), b"".join(zones["question"])),
        (55, 55): (b"".join(zones["vide_55"]), b"".join(zones["vide_55"])),
        (56, 60): (b"".join(zones["table"]), b"".join(table_servie)),
        (61, 61): (b"".join(zones["vide_61"]), b"".join(zones["vide_61"])),
        (64, 66): (b"".join(zones["champs"]), b"".join(zones["champs"])),
    }
    comparaison_journal = []
    for piece in journal["pieces_dans_l_ordre"]:
        if piece["nature"] != "zone":
            exiger(piece["sha256"] == sha(CASE), "empreinte de l'emplacement au journal")
            continue
        cle = (piece["ligne_debut"], piece["ligne_fin"])
        extrait, servi = attendu[cle]
        ok = piece["sha256_extrait"] == sha(extrait) and piece["sha256_servi"] == sha(servi)
        exiger(ok, "empreintes de la zone %d-%d au journal" % cle)
        comparaison_journal.append(
            {"lignes": "%d-%d" % cle, "sha256_extrait": sha(extrait), "sha256_servi": sha(servi), "egal_au_journal": ok}
        )
    exiger(journal["sortie"]["sha256"] == SHA_GABARIT, "empreinte de sortie au journal")

    # Chaque ligne du gabarit rapportée à sa ligne de source.
    correspondance = []
    for ligne in rendu.splitlines(keepends=True):
        if ligne == CASE:
            correspondance.append("emplacement")
            continue
        exacts = [i + 1 for i, s in enumerate(toutes) if s == ligne]
        if exacts:
            correspondance.append(exacts)
            continue
        tronques = [i + 1 for i, s in enumerate(toutes) if i + 1 in range(56, 61) and s.startswith(ligne[:-1])]
        correspondance.append(["tronquée de"] + tronques)
    exiger(rendu.count(b"{{CASE}}") == 1, "un seul {{CASE}}")
    exiger(rendu.count(b"{") == 2 and rendu.count(b"}") == 2, "quatre accolades en tout")
    exiger(b"\n" + CASE in rendu, "emplacement sur une ligne propre")

    # Contrôles de forme du texte servi.
    texte = rendu.decode("utf-8")
    exiger("\r" not in texte, "aucun retour chariot")
    controles = [c for c in texte if unicodedata.category(c) == "Cc" and c != "\n"]
    exiger(not controles, "aucun caractère de contrôle")
    invisibles = sum(texte.count(c) for c in INVISIBLES)
    exiger(invisibles == 0, "aucun caractère invisible")
    espaces_insecables = texte.count(" ") + texte.count(" ")

    # Relevé à soi, sur le gabarit sans la ligne de l'emplacement.
    sans_case = texte.replace("{{CASE}}\n", "\n")
    lignes_releve, total, muets = releve(sans_case)
    exiger(total == 0, "relevé interne à 0 sur le gabarit")
    exiger(muets == 0, "tous les témoins mordent")
    rouages = [{"rouage": n, "occurrences": compter(e, sans_case, False)} for n, e in ROUAGES]

    # Valeurs de la légende et requête assemblée pour chaque case.
    axes = []
    for c1, c2, _ in colonnes[2:]:
        valeurs = c2.strip().decode("utf-8").split(" ; ")
        axes.append((c1.strip().decode("utf-8"), valeurs))
    n_cases = 1
    for _, valeurs in axes:
        n_cases *= len(valeurs)
    pires = 0
    assemblees = 0
    for a in axes[0][1]:
        for b in axes[1][1]:
            for c in axes[2][1]:
                ligne = "case servie : %s / %s / %s\n" % (a, b, c)
                requete = texte.replace("{{CASE}}\n", ligne)
                _, t, _ = releve(requete)
                assemblees += 1
                pires = max(pires, t)
    exiger(assemblees == n_cases, "toutes les cases assemblées")
    exiger(pires == 0, "relevé interne à 0 sur chaque requête assemblée (forme d'essai)")

    # Repli sans légende (lignes 55 à 60 retirées, sans transformation).
    repli = b"".join(zones["question"]) + CASE + b"".join(zones["vide_61"]) + b"".join(zones["champs"])

    resultat = {
        "piece": "vérification indépendante de la partie servie de la question v5 — contre-lecture v1",
        "signe": "contre-lecteur neuf, modèle O",
        "python": platform.python_version(),
        "source": {"sha256": sha(source), "lignes": len(toutes), "taille_octets": len(source), "accolades": accolades_source},
        "gabarit_rendu": {"sha256": sha(rendu), "taille_octets": len(rendu), "lignes": len(rendu.splitlines())},
        "gabarit_rejoue_egal_au_rendu": rendu == rejoue,
        "extraction_independante_egale_au_rendu": mien == rendu,
        "zones_contre_le_journal": comparaison_journal,
        "ligne_du_gabarit_vers_ligne_de_la_source": correspondance,
        "retrait_de_colonne": {
            "cellule_retiree_en_tete": colonnes[0][2].strip().decode("utf-8"),
            "octets_retires": len(b"".join(zones["table"])) - len(b"".join(table_servie)),
            "colonnes_gardees_egales_a_l_octet": all(
                zones["table"][i].startswith(table_servie[i][:-1]) for i in range(5)
            ),
        },
        "emplacement": {
            "occurrences": rendu.count(b"{{CASE}}"),
            "ligne_du_gabarit": rendu[: rendu.index(CASE)].count(b"\n") + 1,
            "accolades_ouvrantes": rendu.count(b"{"),
            "accolades_fermantes": rendu.count(b"}"),
        },
        "forme": {"caracteres_de_controle": len(controles), "invisibles": invisibles, "espaces_insecables": espaces_insecables},
        "releve_interne": {"motifs": lignes_releve, "total": total, "attendu": 0, "temoins_muets": muets},
        "rouages_nommes_compte_informatif": rouages,
        "legende": {"valeurs_par_axe": [len(v) for _, v in axes]},
        "requetes_assemblees": {
            "forme_d_essai": "case servie : <valeur 1> / <valeur 2> / <valeur 3>",
            "nombre": assemblees,
            "pire_total_interne": pires,
        },
        "repli_sans_legende": {"sha256": sha(repli), "taille_octets": len(repli), "lignes": len(repli.splitlines())},
        "echecs": echecs,
        "conforme": not echecs,
    }
    with open(SORTIE, "wb") as flux:
        flux.write((json.dumps(resultat, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
    if echecs:
        sys.stderr.write("ÉCHECS : " + " ; ".join(echecs) + "\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
