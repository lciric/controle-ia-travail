"""Remplit, par recopie de faits deja etablis, les cinq marqueurs du brouillon 3 du texte neuf de la premiere lecture du
barreau 5, corrige le titre et le statut, cite le devis brouillon 3, et retire la table des marqueurs ; ecrit la version a
sceller sous son nom definitif. N'imprime que des comptes et des empreintes, jamais le texte.
Usage : python3 -I -B remplir-marqueurs-premiere-lecture-v1.py <racine du depot>
"""
import hashlib
import sys
from pathlib import Path

R = Path(sys.argv[1]).resolve()
SRC = R / "prereg/validite-adaptateur-sondes-apprises-sur-la-tache-v1-brouillon3.md"
DST = R / "prereg/validite-adaptateur-sondes-apprises-sur-la-tache-v1.md"
ATTENDU_SRC = "f7ee33bff87ac56359eefaea154633b8a7a357b3012159725ef218f0eb2c0a91"
DEVIS = "docs/notes/barreau5-resolution-v1/premiere-lecture/devis-relecture-meme-chemin-v1-brouillon3.md"
H_DEVIS = "e6dfc452869b5cb45b1e88de30a9dfab0f57a86262c41a5238cb5a17b44cbaea"

COUPLES = [
    ("titre", " — v1 — brouillon 2\n", " — v1\n"),
    ("statut",
     "- **Statut** : **brouillon 2, scellé comme brouillon** : le brouillon 1 (`c5cd92596af8083c5643d1877a9e1a5eed8c3ea77b926b03303f0db263306d43`) a été contre-lu, ses corrections sont appliquées ici, leur vérification reste à faire (section « Contre-lecture ») ; non scellable : il porte des marqueurs (table en fin de texte). Chemin visé au scellement : `prereg/validite-adaptateur-sondes-apprises-sur-la-tache-v1.md`. Rien lancé, rien dépensé, rien commis ; aucun score ouvert ; aucun refus d'outil.",
     "- **Statut** : **version scellée**, `prereg/validite-adaptateur-sondes-apprises-sur-la-tache-v1.md`, scellée par la session mère `session_01XJ6Mgr8BN6UanALsQatc5E` le 19 novembre 2026, à l'heure de la ligne `SCELLEMENT-VSAT` du registre propre. C'est le brouillon 3 (`" + ATTENDU_SRC + "` : le brouillon 2 et les 17 couples de sa vérification, appliqués par programme), dont la session mère a rempli les marqueurs et retiré la table des marqueurs, en recopie de faits déjà établis (écart déclaré : la session mère, non le rédacteur, écrit ces remplissages). Le brouillon 1 a été contre-lu et le brouillon 2 vérifié (section « Contre-lecture »). Rien lancé, rien dépensé ; aucun score ouvert ; aucun refus d'outil."),
    ("code",
     "- **Commit du code d'analyse** : `<<COMMIT_CODE_VSAT>>`.",
     "- **Commit du code d'analyse** : écart au gabarit accordé par Lazar (`GO-2026-11-19-91`, nœud 5). Le code de lecture n'est ni écrit ni contre-lu au scellement ; il est cité, après le scellement et avant toute exécution, par la ligne `CODE-VSAT` du registre propre (commit, empreintes des fichiers, entropie des graines), comme pour l'étape B bis."),
    ("devis-entete",
     "  - brouillon de devis de la relecture : `docs/notes/barreau5-resolution-v1/premiere-lecture/devis-relecture-meme-chemin-v1-brouillon2.md`, `35eb699660fed749870505fdd660ca6d94d3ad739edcc81b9034a2311943fb90` (brouillon 2 ; le brouillon 1, `d4694c11a7c4bad9772a968f1f69751e4740ebe5d16fbffb3645d3afebaa2f3d`, est remplacé) ;",
     "  - devis de la relecture, brouillon 3 scellé : `" + DEVIS + "`, `" + H_DEVIS + "` (le brouillon 2, `35eb699660fed749870505fdd660ca6d94d3ad739edcc81b9034a2311943fb90`, et les quatre couples de la vérification ; le brouillon 1, `d4694c11a7c4bad9772a968f1f69751e4740ebe5d16fbffb3645d3afebaa2f3d`, est remplacé) ; ligne d'accord de calcul `GO-2026-11-19-90` ;"),
    ("pieces",
     "à verser par la session mère (`<<PIECES_PLANIFICATION_VERSEES>>`)",
     "versées par la session mère dans `docs/notes/barreau5-resolution-v1/premiere-lecture/pieces/`, empreintes inchangées"),
    ("decision-9",
     "À trancher avant le scellement (`<<DECISION_9_MOT>>`) ; après, par addendum.",
     "Mot de Lazar : option c (`GO-2026-11-19-91`, 19 novembre 2026, vers 22:46Z) ; aucune qualification ne s'ajoute ; tout changement, par addendum."),
    ("devis-relecture",
     "**Aucune dépense sans le devis scellé et une ligne d'accord de calcul neuve** (`<<DEVIS_RELECTURE>>`).",
     "**Aucune dépense sans le devis scellé et une ligne d'accord de calcul neuve** : devis scellé `" + DEVIS + "` (`" + H_DEVIS + "`) ; ligne d'accord `GO-2026-11-19-90` (coupure de 8,5 USD ; accord du 10 novembre reporté), que la ligne `GO-RELECTURE-VSAT` du registre propre citera."),
    ("contre-lecture",
     "**La vérification des corrections reste à faire.** Écart déclaré à la règle « vérification par le même contre-lecteur » : le contre-lecteur d'origine est resté sur un autre compte et n'est pas joignable ; un agent neuf du même modèle (Claude Opus 5.5) vérifiera à partir de la table, du rapport et de la différence entre les deux brouillons. L'entrée de contre-lecture au format du validateur (deux empreintes entières, table de traitement) reste à écrire par la session mère : `<<CONTRE_LECTURE_1>>`.",
     "**Vérification des corrections.** Écart déclaré à la règle « vérification par le même contre-lecteur » : le contre-lecteur d'origine est resté sur un autre compte et n'était pas joignable ; un agent neuf du même modèle (Claude Opus 5.5) a vérifié le 19 novembre 2026, à partir de la table, du rapport et de la différence entre les deux brouillons. Rapport : `docs/notes/barreau5-resolution-v1/premiere-lecture/verification-corrections-brouillon2-v1.md` ; conclusion « scellable après 17 couples exacts » ; les 17 couples sont appliqués par programme au brouillon 3 (recopie pure par la session mère, écart déclaré, R-3955). Entrées au format du validateur : contre-lecture 1, brouillon relu `c5cd92596af8083c5643d1877a9e1a5eed8c3ea77b926b03303f0db263306d43`, rapport `13bde37898a0a6f6f71aab4bffc6142df8af71691277e8f923925942a374239c` ; vérification, brouillon vérifié `b346d5bd432a798cafd454d2dbec8fda52c98a43ef6108877d0ea04f5947d5d1`, rapport `a7298fd265a2b960b93afa625c08b416a3a445e4799333d7ec93fc994ff67760` ; table de traitement `docs/notes/barreau5-resolution-v1/premiere-lecture/table-corrections-brouillon2-v1.md`, `d4d6c9c8635574a62ed713954e17b8591d351441bea9035e81839be74fd049b6`."),
]
SECTION_RETIREE = "\n## Marqueurs à remplir avant le scellement\n"


def h(b):
    return hashlib.sha256(b).hexdigest()


if DST.exists():
    sys.exit("ARRET : la version a sceller existe deja ; on n'ecrase jamais (R12)")
octets = SRC.read_bytes()
if h(octets) != ATTENDU_SRC:
    sys.exit("ARRET : brouillon 3 d'une autre empreinte")
if h((R / DEVIS).read_bytes()) != H_DEVIS:
    sys.exit("ARRET : devis brouillon 3 d'une autre empreinte")
t = octets.decode("utf-8")
for nom, avant, apres in COUPLES:
    n = t.count(avant)
    if n != 1:
        sys.exit(f"ARRET : {nom} « avant » trouve {n} fois")
    t = t.replace(avant, apres, 1)
    print(f"  {nom:16s} avant 1 -> apres {t.count(apres)}")
i = t.find(SECTION_RETIREE)
if i < 0 or t.count(SECTION_RETIREE) != 1:
    sys.exit("ARRET : section des marqueurs introuvable ou multiple")
retire = t[i:]
t = t[:i].rstrip("\n") + "\n"
print(f"  section retiree : {retire.count(chr(10))} lignes, {len(retire)} signes")
if "<<" in t or "À REMPLIR" in t:
    sys.exit("ARRET : un marqueur reste")
b = t.encode("utf-8")
DST.write_bytes(b)
print(f"ecrit {DST.name} sha256 {h(b)} ({len(b)} octets)")
