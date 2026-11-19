"""Couples exacts du devis v9 (vérification du critère v8 et du devis v8), appliqués au devis v8 pour en tirer le texte attendu de
la v9, puis contrôlés. Usage : python3 -I couples_devis_v9_v1.py <devis v8> <sortie : devis v9 attendu> [--minimal]

Le texte attendu porte trois champs à remplir par le rédacteur, entre crochets : [rédacteur], [heure], [empreinte du rapport].
Option --minimal : seulement la tête (point 2 réduit), le point 5 j et le point 6. Sans elle : l'option complète, recommandée.
"""
import hashlib
import re
import sys

V8 = "0fa54bb4664ad7a91c61e26bb825c4634d4cc119d0d72ea48de0ce2c6ecf33fe"
TETE_V8 = "2b47349f9d89c9aac20e0ecda4201144f5b8d98ab1b93f982f95ecc4c1deccb0"   # lignes 1 à 32 du devis v8, fin de ligne comprise
REJEU = ("`docs/notes/neuron-lens-v1/devis-reajustement/banc-programme-v4/sortie-essais-programme-v4-20261119T124303Z-v1.txt`,\n"
         "   `5cf86e2849969f502b30bc58394be2f705c50a5470bade79fbd7a056780e9fa9`")

POINT_2_COMPLET = (
    "2. Le critère d'identité nommé est sa version finale, la v8, et elle seule, hors l'historique du § 0 et des § 9 à 12 : les\n"
    "   renvois des § 1 à 8 aux versions antérieures du critère deviennent des renvois au critère v8, aux mêmes paragraphes, le\n"
    "   critère v8 gardant la numérotation de ses versions antérieures ; la règle de lecture du § 4 est récrite en conséquence ; la\n"
    "   ligne « Statut » ne parle plus du marqueur d'une version antérieure de ce devis.\n")
POINT_2_MINIMAL = (
    "2. § 5, point 5 j : le renvoi devient un renvoi au critère v8, § 4. Les autres renvois du corps à une version antérieure du\n"
    "   critère restent, lus par la règle du § 4 dans la version finale.\n")


def tete(point_2: str) -> str:
    return (
        "# Devis du réajustement de nos lentilles R et S (lecture par lentille neuronale, Llama 3.1 8B Instruct), pour les ranger et les "
        "faire entrer dans le programme — v9\n"
        "\n"
        "**Version 9 — différences avec la v8.** Rédacteur de la v9 : [rédacteur]. Heure (`date -u`) : [heure]. Origine : la v8\n"
        f"(`devis-reajustement-lentilles-b-beta-v8.md`, `{V8}`), gardée octet pour octet hors\n"
        "ce bloc et les couples de la vérification du critère v8 et du devis v8 par le contre-lecteur\n"
        "(`docs/notes/neuron-lens-v1/verification-critere-v8-devis-v8-v1.md`, [empreinte du rapport]) ; elle reste archivée sans\n"
        "modification, comme la v7 (`devis-reajustement-lentilles-b-beta-v7.md`,\n"
        "`c187546226d61cf4cd8153a7d7b3add79e29eaa1a31a58daacd661f48b452451`) : leurs blocs de tête, retirés ici, disent leurs différences\n"
        "avec la version qui les précède.\n"
        "1. Titre : « v8 » devient « v9 » ; les blocs « Version 8 » et « Version 7 » sont remplacés par ce bloc.\n"
        + point_2 +
        "3. § 5, point 6 : les 311 essais du programme de comparaison v4 sont cités par leur rejeu scellé, et le critère qui le cite est\n"
        "   la v8.\n"
        "\n"
        "**Rien d'autre ne change** : aucun chiffre de durée, de prix ni de plafond, aucune variante, aucune recommandation, aucune\n"
        "décision. Les lignes « Auteur », « Origine » et « Heure » ci-dessous sont celles de la v6 et décrivent son rédacteur. Le § 0\n"
        "et le § 12 sont ceux de la v6 : là où ils disent la version finale du critère « à porter » ou le programme v4 « en cours\n"
        "d'écriture », c'est fait (critère v8, § 0.1 : couples 1 à 6 portés, le couple 7 tombe).\n")


# (nom, avant exact dans le devis v8, après) — l'avant doit s'y trouver une fois et une seule
COMMUNS = [
    ("point 5 j",
     "(préalables « K2 : … » du programme de comparaison, critère v6, § 4 ;",
     "(préalables « K2 : … » du programme de comparaison, critère v8, § 4 ;"),
    ("point 6, essais",
     "rejoués\n   par le rédacteur du critère v6 : 311 passés, ligne non opposable ;",
     "rejoués avant la création, sortie scellée\n   (" + REJEU + ", versée au commit `952fb75c` : arbre `9b6a35c1`,\n"
     "   empreintes du programme et des essais égales à celles ci-dessus, « 311 passed », code de sortie 0) ;"),
    ("point 6, critère",
     "   Le critère v6 la cite, elle seule,",
     "   Le critère v8 la cite, elle seule,"),
]
COMPLETS = [
    ("Statut",
     "**Le marqueur que portait la v6 est remplacé** (§ 4) par le chemin et l'empreinte de\n  la version finale du critère d'identité, la v8",
     "Le critère d'identité qui fait foi (§ 4) est sa **version finale, la v8**"),
    ("§ 1", "avec audit**\n  (critère v5, § 4).", "avec audit**\n  (critère v8, § 4)."),
    ("§ 2, variante A, comparaison", "comparaison selon le critère d'identité v5 ;", "comparaison selon le critère d'identité v8 ;"),
    ("§ 2, variante A, lecture", "dans aucune lecture sans nœud de Lazar (critère v5, § 5).",
     "dans aucune lecture sans nœud de Lazar (critère v8, § 5)."),
    ("§ 2, seconde course incomplète", "traitée comme en variante A (critère v5, § 5).", "traitée comme en variante A (critère v8, § 5)."),
    ("§ 3, aucune relance", "mot de Lazar (critère\nv5, § 6).", "mot de Lazar (critère\nv8, § 6)."),
    ("§ 4, règle de lecture",
     "Les renvois « critère v5, § … » de ce devis gardent les numéros de paragraphe de la version 5\n"
     "(`critere-identite-reajustement-lentilles-v5.md`, `50657b8929ab29ff5b09012b31cfe2a150f7815916b538acdba133f7042e24b6`) ; ils se lisent\n"
     "comme la règle de même objet dans la version finale, qui prime en cas d'écart (hors le § 0, le point 6 du § 5 et les § 9 à 12, où\n"
     "« critère v5 » nomme la version 5 elle-même).",
     "Les mentions de versions antérieures du critère, au § 0 et aux § 9 à 12, sont l'historique de ce devis et nomment ces\n"
     "versions elles-mêmes ; partout ailleurs, ce devis ne renvoie qu'à la version finale."),
    ("§ 4, contrôles à la main", "(critère v5, § 7, K1 à K5)", "(critère v8, § 7, K1 à K5)"),
    ("§ 5, point 3, perte", "« S non réajustée », critère v5, § 4)", "« S non réajustée », critère v8, § 4)"),
    ("§ 5, point 5 g, matériel", "contrôle K3 du critère v5)", "contrôle K3 du critère v8)"),
    ("§ 5, point 5 g, versions", "(critère v5, § 2 et § 4 : même", "(critère v8, § 2 et § 4 : même"),
    ("§ 6", "au lieu de rangement (critère v5, § 5).", "au lieu de rangement (critère v8, § 5)."),
    ("§ 7, décision 1", "Le critère v5 en garde la règle", "Le critère v8 en garde la règle"),
]


def appliquer(texte: str, minimal: bool) -> str:
    assert hashlib.sha256(texte.encode("utf-8")).hexdigest() == V8, "ce n'est pas le devis v8"
    lignes = texte.split("\n")
    bloc = "\n".join(lignes[:32]) + "\n"
    assert hashlib.sha256(bloc.encode("utf-8")).hexdigest() == TETE_V8, "les lignes 1 à 32 ne sont pas celles attendues"
    reste = "\n".join(lignes[32:])
    texte = tete(POINT_2_MINIMAL if minimal else POINT_2_COMPLET) + reste
    for nom, avant, apres in COMMUNS + ([] if minimal else COMPLETS):
        n = texte.count(avant)
        assert n == 1, f"couple « {nom} » : l'avant se trouve {n} fois"
        texte = texte.replace(avant, apres)
    return texte


def controler(v8: str, v9: str, minimal: bool) -> None:
    def sec(t, n):
        m = re.search(r"\n## %d\..*?(?=\n## )" % n, t, re.S)
        return m.group(0)
    corps = v9[v9.index("\n## 1. "):v9.index("\n## 9. ")]          # § 1 à § 8
    mentions = re.findall(r"crit[eè]re(?:\s+d'identité)?\s+v([0-9])|critere-identite-reajustement-lentilles-v([0-9])", v9)
    print("versions du critère nommées dans tout le texte :", sorted({a or b for a, b in mentions}))
    hors_histoire = re.findall(r"crit[eè]re(?:\s+d'identité)?\s+v([0-9])|critere-identite-reajustement-lentilles-v([0-9])",
                               v9[:v9.index("\n## 0. ")] + corps)
    print("versions du critère nommées hors l'historique (tête, § 1 à § 8) :", sorted({a or b for a, b in hors_histoire}))
    print("« critère v6 » encore présent :", bool(re.search(r"crit[eè]res?(?:\s+d'identité)?\s+(?:v5 et )?v6", v9)))
    print("« non opposable » encore présent :", "non opposable" in v9, "; rejeu cité :", "5cf86e2849969f502b30bc58394be2f705c50a5470bade79fbd7a056780e9fa9" in v9)
    print("§ 3 identique à la v8 :", sec(v8, 3).replace("critère\nv5, § 6)", "critère\nv8, § 6)") == sec(v9, 3) or sec(v8, 3) == sec(v9, 3))
    num = lambda t: re.findall(r"\d+(?:[ ,.]\d+)*", re.sub(r"`[0-9a-f]{8,}…?`|v[0-9]\b|§ ?[0-9]+", "", t))
    a, b = num(v8[v8.index("\n## 1. "):]), num(v9[v9.index("\n## 1. "):])
    import collections
    ajout = collections.Counter(b) - collections.Counter(a); retrait = collections.Counter(a) - collections.Counter(b)
    print("nombres du corps ajoutés :", dict(ajout), "; retirés :", dict(retrait))


if __name__ == "__main__":
    minimal = "--minimal" in sys.argv
    v8 = open(sys.argv[1], encoding="utf-8").read()
    v9 = appliquer(v8, minimal)
    with open(sys.argv[2], "x", encoding="utf-8") as f:
        f.write(v9)
    print("option :", "minimale" if minimal else "complète", "; couples appliqués :", 1 + len(COMMUNS) + (0 if minimal else len(COMPLETS)))
    controler(v8, v9, minimal)
    print("empreinte du texte attendu (champs entre crochets non remplis) :", hashlib.sha256(v9.encode("utf-8")).hexdigest())
