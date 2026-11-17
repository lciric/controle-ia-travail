"""Brouillon 2 du préenregistrement de la validation propre de l'allocation par blocs : applique au brouillon 1 les
couples « ancien → nouveau » de la contre-lecture 1 (rapport `contre-lecture-validation-blocs-tour1-v1.md`, § 4), plus
quatre couples du rédacteur (titre ; en-tête : ligne « Brouillon 2 » ; en-tête : statut ; section « Contre-lecture »),
et rien d'autre.

- vérifie l'empreinte du brouillon 1 et celle du rapport ;
- tire les 29 couples du § 4 du rapport par programme (aucune recopie à la main de l'« ancien ») ;
- remplace le « nouveau » de quatre couples par une reformulation déclarée (M1-a, M4-a, m4, m7 : raisons dans
  REFORMULES et dans la section « Contre-lecture » de la cible) ;
- exige que chaque « ancien » figure exactement une fois dans le brouillon 1 et qu'aucun couple n'en chevauche un autre ;
- exige, après application, aucune ligne au format du lanceur (« empreinte, deux espaces, chemin ») et aucun nom de
  modèle ni lettre de modèle ;
- lit l'heure par `date -u` au moment de l'écriture (scellement juste après, par `controle_ia.scellement`) ;
- écrit le différentiel du brouillon 1 vers le brouillon 2 ;
- refuse d'écraser la cible ou le différentiel.
Lancé par `python3 -I -B` ; aucun fichier sous `diag/`, `runs/`, `donnees/` n'est ouvert.
"""
import difflib
import hashlib
import re
import subprocess
import sys
from pathlib import Path

DOSSIER = Path("/home/user/controle-ia-travail/docs/notes/organisme-idees-juge-v1/validation-allocation-blocs-v1")
SOURCE = DOSSIER / "prereg-validation-allocation-blocs-v1-brouillon1.md"
SHA_SOURCE = "95f34a756c61b1f73df88cfa99350f9ffb741ad872a6afea90406e1f1acd6011"
RAPPORT = DOSSIER / "contre-lecture-validation-blocs-tour1-v1.md"
SHA_RAPPORT = "c06813086fb63910cd240e1018fde7960d165f373cee5ff081d6228741cd4d3c"
CIBLE = DOSSIER / "prereg-validation-allocation-blocs-v1-brouillon2.md"
DIFF = DOSSIER / "differentiel-prereg-validation-allocation-blocs-v1-brouillon1-vers-brouillon2.diff"
PROGRAMME = "appliquer-corrections-prereg-validation-allocation-blocs-v1-brouillon2.py"
MOTIF_LANCEUR = re.compile(r"^[0-9a-f]{64}  \S+\s*$", re.M)
MOTIF_MODELE = re.compile(r"\b(?:claude|opus|sonnet|haiku|fable)\b|mod[eè]le [ABC]\b", re.I)
EXIGES = (["M1-a", "M1-b"] + [f"M2-{x}" for x in "abcdef"] + ["M3", "M4-a", "M4-b", "M5"]
          + [f"m1-{x}" for x in "abcd"] + ["m2-a", "m2-b", "m3", "m4", "m5", "m6-a", "m6-b", "m6-c",
                                           "m7", "m8", "m9", "m10", "m11"])


def h(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def arret(msg: str):
    print("ARRÊT :", msg, file=sys.stderr)
    sys.exit(1)


for p in (CIBLE, DIFF):
    if p.exists():
        arret(f"{p.name} existe déjà : R12 interdit d'écraser")
b_src, b_rap = SOURCE.read_bytes(), RAPPORT.read_bytes()
if h(b_src) != SHA_SOURCE:
    arret("empreinte du brouillon 1 inattendue")
if h(b_rap) != SHA_RAPPORT:
    arret("empreinte du rapport de contre-lecture inattendue")
src, rap = b_src.decode("utf-8"), b_rap.decode("utf-8")

# § 4 du rapport : couples, un « ancien » et un « nouveau » par ligne, entre trois accents graves
sec = rap[rap.index("## 4. Couples"):rap.index("## 5. Ce qui est bon")]
motif = re.compile(r"^\*\*(?P<id>[Mm]\d+(?:-[a-f])?)\*\*\n\n- ancien : ```(?P<a>.*)```\n- nouveau : ```(?P<n>.*)```$", re.M)
couples = {}
for m in motif.finditer(sec):
    if m["id"] in couples:
        arret(f"couple {m['id']} tiré deux fois du rapport")
    couples[m["id"]] = [m["a"], m["n"]]
if sorted(couples) != sorted(EXIGES):
    arret(f"couples tirés du rapport : {sorted(couples)} ≠ {sorted(EXIGES)}")

# Reformulations déclarées (le rapport : « le rédacteur peut reformuler, mais pas omettre ce que le couple exige »)
REFORMULES = {
    # réserve du § 1 (4) du rapport : la durée du serrage n'est pas mesurée ; la règle compte la mesure si elle est plus grande
    "M1-a": (
        "à leurs 500 premières générations (g de 0 à 499, 50 par cellule ; mêmes tirages que les 500 premières des 750, les "
        "clés étant par génération). **Règle écrite ici, avant tout tirage du jeu** : durée projetée = somme, sur les cinq "
        "familles, du nombre de générations multiplié par la durée moyenne mesurée par génération de la famille (bras, rejeu "
        "et oracle compris), plus la durée des contrôles, de l'essai E1, du jeu synthétique et du serrage, mesurée ou "
        "extrapolée par l'essai à blanc, et comptée pour au moins 1 heure ; la décision ne dépend que de cette durée, se "
        "consigne au registre avant le jeu et ne change aucun seuil ni aucun critère. L'essai à blanc se joue **après** le "
        "scellement de ce texte et de l'addendum d'empreintes (le code n'existe qu'à partir de là, voir l'en-tête) et avant "
        "le jeu, jamais avant le scellement."
    ),
    # un texte gelé ne laisse aucune autre répartition ouverte : la proposition est retenue telle quelle
    "M4-a": couples["M4-a"][1].replace(
        "(proposition du contre-lecteur ; toute autre répartition doit être écrite de la même façon)",
        "(proposée par la contre-lecture 1 et retenue telle quelle ; aucune autre répartition n'est permise)"),
    # m8, appliquée, ajoute une lecture « nuisible » dans « dense » et une dans « vide » : douze, non dix
    "m4": "(jusqu'à douze intervalles sur quatre familles : 4 + 3 + 5)",
    # deux parenthèses de suite écrites en phrase ; R_A − R_F n'existe qu'en « dense » (« vide » n'a pas de porteuse)
    "m7": (
        "Le gain y est rapporté, sans critère, avec les bornes basses de C_A − C_F et, pour « dense », de R_A − R_F ; "
        "« pas nuisible » y veut dire « tort non établi », non « innocuité établie à une marge près » : aucune marge de "
        "non-infériorité n'est écrite, c'est dit et lu ainsi au prononcé (la couverture de « dense » risque le plafond ; "
        "celle de « vide »"
    ),
}
if "proposée par la contre-lecture 1" not in REFORMULES["M4-a"]:
    arret("reformulation de M4-a sans effet")
for k, v in REFORMULES.items():
    couples[k][1] = v

# Couples du rédacteur
heure = subprocess.run(["date", "-u", "+%Y-%m-%d %H:%M:%SZ"], capture_output=True, text=True, check=True).stdout.strip()
tete = subprocess.run(["git", "-C", "/home/user/controle-ia-travail", "rev-parse", "HEAD"], capture_output=True, text=True,
                      check=True).stdout.strip()
debut_cl = src.index("## Contre-lecture\n\n") + len("## Contre-lecture\n\n")
fin_cl = src.index("\n\n## Citations obligatoires")
ancien_cl = src[debut_cl:fin_cl]
if not ancien_cl.startswith("- **Contre-lecture 1** (R2) : **à venir**."):
    arret("section « Contre-lecture » du brouillon 1 inattendue")

NOUVEAU_CL = f"""- **Contre-lecture 1** (R2) : **faite**, verdict « corrections » : cinq défauts majeurs (M1 à M5), onze remarques mineures
  (m1 à m11, dont m5 et m8 facultatives et recommandées) ; aucun « à refaire ». Lecteur : sous-agent neuf d'un autre modèle que
  le rédacteur du brouillon 1, qui n'a écrit ni ce brouillon, ni [T], ni ses addendums, ni [V]. Brouillon relu : brouillon 1,
  `docs/notes/organisme-idees-juge-v1/validation-allocation-blocs-v1/prereg-validation-allocation-blocs-v1-brouillon1.md`
  (`{SHA_SOURCE}`). Rapport :
  `docs/notes/organisme-idees-juge-v1/validation-allocation-blocs-v1/contre-lecture-validation-blocs-tour1-v1.md`
  (`{SHA_RAPPORT}`).
- **Traitement, brouillon 2** : par un rédacteur neuf, sous-agent de la session mère, qui n'a écrit ni le brouillon 1, ni le
  rapport, ni [T], ni ses addendums, ni [V] ; lettre de son modèle à inscrire par la mère au registre (il est du même modèle
  que le contre-lecteur 1). Les 29 couples du § 4 du rapport sont appliqués par le programme `{PROGRAMME}` (même dossier,
  scellé), qui vérifie les deux empreintes ci-dessus, tire les couples du rapport par programme, exige que chaque « ancien »
  figure une seule fois et qu'aucun ne chevauche un autre, et refuse d'écraser ; quatre couples du rédacteur s'y ajoutent
  (titre, ligne « Brouillon 2 » et statut de l'en-tête, cette section). Différentiel :
  `differentiel-prereg-validation-allocation-blocs-v1-brouillon1-vers-brouillon2.diff` (même dossier, scellé). Rien d'autre
  ne change ; la « Déclaration » finale reste celle du rédacteur du brouillon 1.

**Réponse point par point.**

| point du rapport | couples | traitement |
|---|---|---|
| M1 (ordre : code, essai à blanc, scellement) | M1-a, M1-b | **acceptés**. M1-a reformulé : la durée projetée compte aussi les contrôles, l'essai E1, le jeu synthétique et le serrage, mesurés ou extrapolés par l'essai à blanc, pour au moins 1 heure (réserve du § 1 (4) du rapport : le serrage n'est pas chronométré). Si la mère tranche Q-2 pour 500 générations tout de suite, ces deux couples tombent et le texte dit 500 |
| M2 (lecture (5) sans pouvoir toutes cartes réunies) | M2-a à M2-f | **acceptés tels quels** (variante principale du rapport : jugée sur la sorte « voisines du monde », pouvoir rejoué après le jeu par la mutation « bloc suivant » sur le bras A de la famille « nul ») |
| M3 (« hors de la zone utile » masquait un tort) | M3 | **accepté tel quel** |
| M4 (compositions non gelées) | M4-a, M4-b | **acceptés**. La répartition proposée est retenue telle quelle ; la parenthèse « proposition du contre-lecteur ; toute autre répartition doit être écrite de la même façon » devient « proposée par la contre-lecture 1 et retenue telle quelle ; aucune autre répartition n'est permise », un texte gelé ne pouvant laisser une autre répartition ouverte. Vérifiée contre [T] (famille T : quatre fausses sous la règle du cosinus, deux opposées à force × 1 et × 0,5 ; pour V4, toutes sous la règle du cosinus ; quatre constructions de copies par morceaux) |
| M5 (annexe du serrage non écrite) | M5 | **couple accepté tel quel** ; **l'annexe A elle-même n'est pas écrite dans ce brouillon** : elle demande un compte (distance des voisines du monde jouet, variance attendue de Λ au plafond, borne basse attendue de la mutation « bloc suivant ») qui dépasse l'application de corrections ; à écrire dans un brouillon suivant, avant la contre-lecture 2, comme le couple le dit |
| m1 (garde de chemin trop étroite) | m1-a à m1-d | **acceptés tels quels** |
| m2 (dénominateur de P3) | m2-a, m2-b | **acceptés tels quels** |
| m3 (citation de § 4) | m3 | **accepté tel quel** |
| m4 (compte des intervalles « nuisible ») | m4 | **accepté, compte mis à jour** : m8, appliquée, ajoute une lecture « nuisible » en « dense » et une en « vide » ; le total devient douze (principales 4, par carte 3, « dense » 3, « vide » 2 : 4 + 3 + 5) au lieu des dix du couple |
| m5, facultative (fausse alerte du serrage et reprise) | m5 | **acceptée telle quelle** |
| m6 (grille de sensibilité) | m6-a à m6-c | **acceptés tels quels** |
| m7 (« ne nuit pas » sans marge) | m7 | **accepté, reformulé** : les deux parenthèses de suite sont écrites en phrase ; les bornes de R_A − R_F ne valent que pour « dense » (« vide » n'a pas de porteuse) |
| m8, facultative (décuplement des fausses promotions) | m8 | **acceptée telle quelle** |
| m9 (serrage et étage 1) | m9 | **accepté tel quel** |
| m10 (doses neuves non chiffrées) | m10 | **couple accepté tel quel** ; **l'annexe B n'est pas écrite dans ce brouillon** (même raison que l'annexe A) ; à écrire avant la contre-lecture 2 |
| m11 (seuils de réfutation de P10) | m11 | **accepté tel quel** |
| § 6 du rapport, points pour la mère | — | **non tranchés ici** (ils sont à la mère) : Q-1 et Q-2 à trancher avant le scellement, la ligne de la liste d'arrêt sur le juge candidat, les lignes du Coût et les questions ouvertes étant retirées ou gardées selon la réponse ; si Q-1 est retenue, écrire comment le juge candidat consomme le flux de chaque carte ; lettres des modèles à inscrire ; tâche d'attente prévue avant le lancement |

**Ce qui reste avant la contre-lecture 2** : annexe A (M5) ; annexe B (m10) ; réponses de la mère à Q-1 et Q-2 ; puis contre-lecture
par un sous-agent neuf qui n'a écrit ni ce texte ni le rapport, avec ce brouillon, le rapport, [V], [T], [AR] et [AE].

**Déclaration du rédacteur du brouillon 2.** Heures (`date -u`) : début 01:33Z ; écriture par le programme à {heure}, scellement
aussitôt après (compagnon `.sha256`). Dépôt lu sur `main`, tête `{tete}` ; aucun commit, aucune poussée. Lu en entier : le
brouillon 1 et le rapport ; lu en partie : [T] (familles T et N, pour vérifier M4-a), en-tête et fonction `problemes` du
validateur, un programme de correction voisin (pour la forme). Jamais ouvert : rien sous `diag/`, `runs/`, `donnees/` ; aucune
branche `calcul/*` ni `donnees/*` ; rien de 7a, 7b, T0.6, T0.7, B bis, P3-bis, du bras d'attaque, du pilote MR-2 ; aucun secret,
aucune variable d'environnement affichée ; aucune machine, aucun appel réseau ; aucun fichier existant modifié."""

couples["en-tete-titre"] = ["sur données neuves et banc neuf — brouillon 1", "sur données neuves et banc neuf — brouillon 2"]
couples["en-tete-brouillon-2"] = [
    "- **Commit du code d'analyse** :",
    f"- **Brouillon 2** : {heure} (`date -u`, au moment de l'écriture ; scellement aussitôt après, compagnon `.sha256`) ; "
    f"corrections de la contre-lecture 1\n  appliquées par un rédacteur neuf, par programme ; tête de `main` lue : `{tete}` ; "
    "rien d'autre ne change (voir « Contre-lecture »).\n- **Commit du code d'analyse** :"]
couples["en-tete-statut"] = [
    "**brouillon 1**, pièce de travail scellée par son compagnon (R6). Il ne fait pas foi. Il attend une contre-lecture",
    "**brouillon 2** (corrections de la contre-lecture 1 appliquées), pièce de travail scellée par son compagnon (R6). Il ne\n"
    "  fait pas foi. **Il n'est pas prêt pour la contre-lecture 2** tant que les annexes A (serrage) et B (dimensionnement des\n"
    "  doses) ne sont pas écrites et que la mère n'a pas tranché Q-1 et Q-2 (voir « Contre-lecture »). Il attend ensuite une\n"
    "  contre-lecture"]
couples["contre-lecture"] = [ancien_cl, NOUVEAU_CL]

# Unicité et absence de chevauchement, puis application sur les positions du brouillon 1
spans = []
for k, (a, n) in couples.items():
    c = src.count(a)
    if c != 1:
        arret(f"couple {k} : « ancien » présent {c} fois dans le brouillon 1")
    i = src.index(a)
    spans.append((i, i + len(a), k, n))
spans.sort()
for (d1, f1, k1, _), (d2, f2, k2, _) in zip(spans, spans[1:]):
    if d2 < f1:
        arret(f"couples {k1} et {k2} se chevauchent")
morceaux, pos = [], 0
for d, f, k, n in spans:
    morceaux += [src[pos:d], n]
    pos = f
morceaux.append(src[pos:])
cible = "".join(morceaux)

if MOTIF_LANCEUR.search(cible):
    arret("ligne au format du lanceur dans la cible")
if MOTIF_MODELE.search(cible):
    arret(f"nom ou lettre de modèle dans la cible : {MOTIF_MODELE.search(cible).group(0)!r}")
for k, (a, n) in couples.items():
    if n not in cible:
        arret(f"couple {k} : « nouveau » absent de la cible")

diff = "".join(difflib.unified_diff(src.splitlines(keepends=True), cible.splitlines(keepends=True),
                                    fromfile=SOURCE.name, tofile=CIBLE.name))
with open(CIBLE, "x", encoding="utf-8") as fh:
    fh.write(cible)
with open(DIFF, "x", encoding="utf-8") as fh:
    fh.write(diff)
print(f"{len(couples)} couples appliqués ({len(EXIGES)} du rapport, {len(couples) - len(EXIGES)} du rédacteur) ; "
      f"reformulés : {sorted(REFORMULES)} ; heure {heure}")
print("cible", CIBLE.name, h(CIBLE.read_bytes()))
print("différentiel", DIFF.name, h(DIFF.read_bytes()))
