"""Brouillon 3 du préenregistrement de la validation propre de l'allocation par blocs : applique au brouillon 2 les dix
couples « ancien → nouveau » de la contre-lecture 2 (rapport `contre-lecture-validation-blocs-tour2-v1.md`, § 5, C1 à C10),
tels quels, plus les couples du rédacteur déclarés ci-dessous (annexes A et B et leurs renvois, défauts M1' et M2' ; étage 1,
remarque m3' ; condition écrite d'avance si Q-1 est retenue, défaut M3' ; titre, ligne « Brouillon 3 », statut, section
« Contre-lecture »), et rien d'autre.

- vérifie l'empreinte du brouillon 2, celle du rapport et celles des quatre fichiers des comptes des annexes ;
- tire les dix couples du § 5 du rapport par programme (aucune recopie à la main de l'« ancien » ni du « nouveau ») ;
- exige que chaque « ancien » figure exactement une fois dans le brouillon 2 et qu'aucun couple n'en chevauche un autre ;
- recopie les deux sorties des comptes, lues sur disque, dans les annexes ;
- exige, après application, aucune ligne au format du lanceur (« empreinte, deux espaces, chemin ») et aucun nom de modèle ni
  lettre de modèle ;
- lit l'heure par `date -u` au moment de l'écriture (scellement juste après, par `controle_ia.scellement`) ;
- écrit le différentiel du brouillon 2 vers le brouillon 3 ;
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
SOURCE = DOSSIER / "prereg-validation-allocation-blocs-v1-brouillon2.md"
SHA_SOURCE = "51a8a3ab4091e27b94baad200fd7bc469f1b2b400e6346febb1471dab07a61be"
RAPPORT = DOSSIER / "contre-lecture-validation-blocs-tour2-v1.md"
SHA_RAPPORT = "ea84faa76b64379d93e58c242b09161bacfd2aeff0d5816c5a43ffcceb41319f"
COMPTES = {
    "compte-annexe-a-serrage-v1.py": "d5a65b27b2e1e3b33ec25c8c88d364fc79ac966f2b0d0ab7c040ec544e9aaddc",
    "sortie-compte-annexe-a-serrage-v1.txt": "bc45c3d317e205154834c0c8c363e981ffa7fba148857491786ab6cb740cfae9",
    "compte-annexe-b-doses-v1.py": "b1015bf3b4e8c77fc9785e1166bc8595850b684a21fb746fd81c1484a564a0b0",
    "sortie-compte-annexe-b-doses-v1.txt": "28dc1b056fe99af2c8ca8e9cf6ea83a147da284efa73727e249222529fbea788",
}
CIBLE = DOSSIER / "prereg-validation-allocation-blocs-v1-brouillon3.md"
DIFF = DOSSIER / "differentiel-prereg-validation-allocation-blocs-v1-brouillon2-vers-brouillon3.diff"
PROGRAMME = "appliquer-corrections-prereg-validation-allocation-blocs-v1-brouillon3.py"
MOTIF_LANCEUR = re.compile(r"^[0-9a-f]{64}  \S+\s*$", re.M)
# noms de familles de modèles écrits à l'envers, pour que ce fichier n'en contienne aucun en clair
_NOMS = [n[::-1] for n in ("edualc", "supo", "tennos", "ukiah", "elbaf")]
MOTIF_MODELE = re.compile(r"\b(?:" + "|".join(_NOMS) + r")\b|mod[eè]le [ABC]\b", re.I)
EXIGES = [f"C{i}" for i in range(1, 11)]


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
    arret("empreinte du brouillon 2 inattendue")
if h(b_rap) != SHA_RAPPORT:
    arret("empreinte du rapport de contre-lecture 2 inattendue")
for nom, sha in COMPTES.items():
    if h((DOSSIER / nom).read_bytes()) != sha:
        arret(f"empreinte inattendue : {nom}")
src, rap = b_src.decode("utf-8"), b_rap.decode("utf-8")
SORTIE_A = (DOSSIER / "sortie-compte-annexe-a-serrage-v1.txt").read_text(encoding="utf-8").rstrip("\n")
SORTIE_B = (DOSSIER / "sortie-compte-annexe-b-doses-v1.txt").read_text(encoding="utf-8").rstrip("\n")

# § 5 du rapport : couples, un « ancien » et un « nouveau » par ligne, entre trois accents graves
sec = rap[rap.index("## 5. Couples"):rap.index("## 6. Points pour la mère")]
motif = re.compile(r"^\*\*(?P<id>C\d+)\*\* \((?P<pt>m\d')\)\n- ancien : ```(?P<a>.*)```\n- nouveau : ```(?P<n>.*)```$", re.M)
couples = {}
for m in motif.finditer(sec):
    if m["id"] in couples:
        arret(f"couple {m['id']} tiré deux fois du rapport")
    couples[m["id"]] = [m["a"], m["n"]]
if sorted(couples) != sorted(EXIGES):
    arret(f"couples tirés du rapport : {sorted(couples)} ≠ {sorted(EXIGES)}")

heure = subprocess.run(["date", "-u", "+%Y-%m-%d %H:%M:%SZ"], capture_output=True, text=True, check=True).stdout.strip()
tete = subprocess.run(["git", "-C", "/home/user/controle-ia-travail", "rev-parse", "HEAD"], capture_output=True, text=True,
                      check=True).stdout.strip()

# ---------------------------------------------------------------------------------------------------------------------
# Couples du rédacteur
# ---------------------------------------------------------------------------------------------------------------------
REDACTEUR = {}

REDACTEUR["titre"] = ["sur données neuves et banc neuf — brouillon 2", "sur données neuves et banc neuf — brouillon 3"]

REDACTEUR["en-tete-brouillon-3"] = [
    "- **Commit du code d'analyse** :",
    "- **Brouillon 3** : @HEURE@ (`date -u`, au moment de l'écriture ; scellement aussitôt après, compagnon `.sha256`) ; "
    "corrections de la contre-lecture 2\n  appliquées par un rédacteur neuf, par programme, et annexes A et B écrites ; tête de "
    "`main` lue : `@TETE@` ; rien d'autre ne change (voir « Contre-lecture »).\n- **Commit du code d'analyse** :"]

REDACTEUR["en-tete-statut"] = [
    "**brouillon 2** (corrections de la contre-lecture 1 appliquées), pièce de travail scellée par son compagnon (R6). Il ne\n"
    "  fait pas foi. **Il n'est pas prêt pour la contre-lecture 2** tant que les annexes A (serrage) et B (dimensionnement des\n"
    "  doses) ne sont pas écrites et que la mère n'a pas tranché Q-1 et Q-2 (voir « Contre-lecture »). Il attend ensuite une\n"
    "  contre-lecture\n"
    "  par un sous-agent neuf d'un autre modèle (R2), les corrections, puis",
    "**brouillon 3** (corrections des contre-lectures 1 et 2 appliquées ; annexes A et B écrites), pièce de travail scellée par\n"
    "  son compagnon (R6). Il ne fait pas foi. **Il n'est pas scellable** tant que la mère n'a pas tranché Q-1, Q-2 et Q-3\n"
    "  (défaut M3' de la contre-lecture 2, voir « Contre-lecture ») et que les lignes qui en dépendent n'ont pas été retirées ou\n"
    "  gardées. Il attend la contre-lecture 3, limitée aux parties touchées et aux deux annexes, par un sous-agent neuf qui n'a\n"
    "  écrit ni les brouillons ni les rapports, d'un autre modèle que le rédacteur du brouillon 3 (R2), les corrections, puis"]

REDACTEUR["metrique-serrage"] = [
    "  mutation « la règle lit le bloc suivant avant de décider » jouée sur le même jeu. Les 24 cartes du monde jouet sont des\n"
    "  **voisines proches** (distance fixée **dans ce texte, par une annexe A à écrire avant la contre-lecture 2 : la distance, la "
    "variance attendue de Λ au plafond et la borne basse attendue de la mutation « bloc suivant », comptées sans donnée du juge**, "
    "pour que la variance de Λ au\n"
    "  plafond reste finie et lisible sur 20 000 générations) : la lecture demande des queues qui ne soient pas trop lourdes.",
    "  mutation « la règle lit le bloc suivant avant de décider » jouée sur le même jeu : **la règle G lit le bloc suivant**\n"
    "  (chaque bloc va à la carte dont log W **après** ce bloc sera la plus grande, comme la règle gloutonne qui anticipe du\n"
    "  programme de [CL], annexe A), Λ lu à son temps d'arrêt ; une mutation qui ne jouerait que sur les arrêts de A est sans\n"
    "  pouvoir sur ce jeu (annexe A) et n'y sert pas. Les 24 cartes du monde jouet sont des **voisines proches**, à la distance\n"
    "  fixée **dans ce texte, annexe A** : bruit d'amplitude ε_i de 0,01 à 0,03 (24 valeurs régulièrement espacées, au lieu de\n"
    "  0,10 à 0,30 dans le jeu de [T]), tout le reste du monde jouet inchangé. À cette distance, comptée sans donnée du juge, la\n"
    "  variance de Λ au plafond est finie et lisible (médiane 0,15, maximum 32 sur 480 000 cartes d'essai, contre une médiane de\n"
    "  6,4·10⁵ à la distance de [T]), la demi-largeur attendue de l'intervalle d'une règle saine est d'environ 0,0007 sur\n"
    "  20 000 générations et la moyenne attendue de la mutation d'environ 1,014 (borne basse attendue ≈ 1,013) : la lecture\n"
    "  demande des queues qui ne soient pas trop lourdes."]

REDACTEUR["banc-de-mutations"] = [
    "règle qui lit le bloc suivant (tuée par le serrage)",
    "règle G qui lit le bloc suivant (tuée par le serrage : Métrique, annexe A)"]

REDACTEUR["origine-P13"] = [
    "| [V] R-1 ; [CL] : 1,267 pour cette règle, cité par [T] l. 211-212 |",
    "| [V] R-1 ; [CL] : 1,267 pour cette règle à la distance de [T], cité par [T] l. 211-212 ; annexe A : ≈ 1,014 à la distance "
    "retenue, borne basse attendue ≈ 1,013 |"]

REDACTEUR["doses-annexe-B-1"] = [
    "**Compte de dimensionnement à écrire en annexe B avant la contre-lecture 2** (information en nats sur 200 épisodes des dix "
    "doses neuves, sans juge, ",
    "**Compte de dimensionnement, annexe B** (information en nats sur 200 épisodes des dix doses neuves, sans juge, "]

REDACTEUR["doses-annexe-B-2"] = [
    " et couverture attendue de F par famille qui en découle, pour que le risque « hors de la zone utile » soit chiffré avant "
    "le jeu : par interpolation, la dose 1,0 de V2, V3 et V5 vaut environ 13 nats pour 6,17 (log 480) nécessaires à une carte "
    "seule, donc proche du plafond pour F.",
    " et couverture attendue de F par famille qui en découle, pour que le risque « hors de la zone utile » soit chiffré avant "
    "le jeu : les doses neuves basses portent 4,9 à 6,0 nats, les doses neuves hautes 12,8 à 15,8 nats (dose 1,0 de V2, V3 et "
    "V5 : 13,5 à 14,2 nats, pour 6,17, log 480, nécessaires à une carte seule : cellules de dose haute proches du plafond pour "
    "F) ; sous l'hypothèse déclarée que la couverture de F croît avec la dose dans chaque type, la couverture attendue de F en "
    "« réplique » est entre 0,41 et 0,87 environ, et celle de « porteuse unique » au plus celle de « réplique » : sous le seuil de 0,95 que la contre-lecture 2 "
    "fixait pour revoir les doses. **Les doses sont gardées** ; P1, P2 et P9, relues avec ce compte, ne changent pas."]

REDACTEUR["etage-1-serrage"] = [
    " ou, au serrage (alors avant tout jeu : la liste d'arrêt dit « pas de jeu » et ce prononcé se rend sans lecture du jeu), "
    "une règle saine à borne basse > 1 |",
    " les alertes du serrage, jouées avant tout jeu, ne relèvent pas de cette table (liste d'arrêt : pas de jeu, aucun "
    "prononcé, audit écrit et nœud de la mère) |"]

REDACTEUR["Q-1-flux"] = [
    "naturel », m = 24), non celui de production. Recommandation du rédacteur : l'inclure (confiance 0,6).",
    "naturel », m = 24), non celui de production. Recommandation du rédacteur : l'inclure (confiance 0,6). **Condition écrite\n"
    "d'avance, valable seulement si la mère retient Q-1** (défaut M3' de la contre-lecture 2) : le juge candidat tire les issues\n"
    "de chaque carte bloc par bloc depuis le flux `(f, g, i, 2)` de la carte, par le même appel au générateur que le banc (même\n"
    "méthode, mêmes arguments, même ordre), de sorte que 32 tirages de 25 issues consomment le générateur exactement comme le\n"
    "tirage d'un coup des 800 issues du rejeu ; un essai le vérifie avant la concordance (cas sain : les 800 issues tirées par\n"
    "blocs égales, une à une, aux 800 tirées d'un coup ; artefact : un bloc tiré par une autre méthode est refusé) ; sinon arrêt,\n"
    "défaut de montage et non de l'allocation."]

SOUS_SECTION = """- **Contre-lecture 2** (R2) : **faite**, verdict « corrections » : trois défauts majeurs (M1' à M3'), neuf remarques
  mineures (m1' à m9', dont m9' facultative et non demandée) ; aucun « à refaire ». Lecteur : sous-agent neuf d'un autre
  modèle que le rédacteur des brouillons 1 et 2, qui n'a écrit ni les brouillons, ni le rapport du tour 1, ni [T], ni ses
  addendums, ni [V]. Brouillon relu : brouillon 2,
  `docs/notes/organisme-idees-juge-v1/validation-allocation-blocs-v1/prereg-validation-allocation-blocs-v1-brouillon2.md`
  (`@SHA_SOURCE@`). Rapport :
  `docs/notes/organisme-idees-juge-v1/validation-allocation-blocs-v1/contre-lecture-validation-blocs-tour2-v1.md`
  (`@SHA_RAPPORT@`). Il trouve les 29 corrections du tour 1 appliquées fidèlement et rien d'autre de changé (§ 1 du rapport).
- **Traitement, brouillon 3** : par un rédacteur neuf, sous-agent de la session mère, qui n'a écrit ni les brouillons 1 et 2,
  ni les rapports des tours 1 et 2, ni [T], ni ses addendums, ni [V] ; lettre de son modèle à inscrire par la mère au
  registre (il est du même modèle que le contre-lecteur 2). Les dix couples C1 à C10 du § 5 du rapport sont appliqués tels
  quels par le programme `@PROGRAMME@` (même dossier, scellé), qui vérifie les empreintes du brouillon 2, du rapport et des
  quatre fichiers des comptes des annexes, tire les couples du rapport par programme, exige que chaque « ancien » figure une
  seule fois dans le brouillon 2 et qu'aucun ne chevauche un autre, recopie les deux sorties des comptes lues sur disque, et
  refuse d'écraser. S'y ajoutent onze couples du rédacteur, déclarés au tableau : annexes A et B et leurs renvois (Métrique,
  banc de mutations, origine de P13, doses neuves : M1', M2') ; le serrage retiré de l'étage 1 (m3') ; la condition sur la
  consommation du flux si Q-1 est retenue (M3') ; titre, ligne « Brouillon 3 » et statut de l'en-tête ; cette section avec les
  deux annexes. Comptes des annexes, même dossier, scellés : `compte-annexe-a-serrage-v1.py` (`@SHA_CA@`) et sa sortie
  `sortie-compte-annexe-a-serrage-v1.txt` (`@SHA_SA@`) ; `compte-annexe-b-doses-v1.py` (`@SHA_CB@`) et sa sortie
  `sortie-compte-annexe-b-doses-v1.txt` (`@SHA_SB@`). Différentiel :
  `differentiel-prereg-validation-allocation-blocs-v1-brouillon2-vers-brouillon3.diff` (même dossier, scellé). Rien d'autre
  ne change ; les parties du brouillon 2 de cette section ci-dessus et la « Déclaration » finale du brouillon 1 restent telles
  quelles.

**Réponse point par point (contre-lecture 2).**

| point du rapport | couples | traitement |
|---|---|---|
| § 1 (fidélité des 29 corrections du tour 1) | — | constat du rapport ; rien à corriger |
| M1' (annexe A du serrage non écrite) | metrique-serrage, banc-de-mutations, origine-P13, annexe A | **appliqué**. Annexe A écrite : distance, variance de Λ au plafond, demi-largeur attendue d'une règle saine, borne basse attendue de la mutation et ce que le compte dit du pouvoir de la lecture (5), sans donnée du juge ; compte et sortie versés et scellés. Le compte oblige à nommer la mutation du serrage : **G lit le bloc suivant** (borne basse attendue ≈ 1,013) ; une mutation sur les seuls arrêts de A n'y est pas tuée (borne basse 0,9993). La Métrique, le banc de mutations de l'étape 0 et la colonne d'origine de P13 sont mis d'accord ; la prédiction P13 elle-même ne change pas. Vérification courte de l'annexe par un lecteur neuf : contre-lecture 3 |
| M2' (annexe B des doses non écrite) | doses-annexe-B-1, doses-annexe-B-2, annexe B | **appliqué**. Annexe B écrite : information des dix doses neuves, comptée sur les mêmes mondes que les doses de l'idée 1.2, et couverture attendue de F par famille : « réplique » entre 0,41 et 0,87 environ, « porteuse unique » au plus autant ; la règle « au-dessus de 0,95 en moyenne, doses à revoir » ne joue pas ; doses gardées ; P1, P2, P9 relues, inchangées. La borne basse de « porteuse unique » n'est pas établie par ce compte (dit dans l'annexe ; l'étage 2 couvre ce cas du côté sûr) |
| M3' (questions ouvertes dans un texte à sceller) | Q-1-flux | **non appliqué** : trancher Q-1, Q-2 et Q-3 est hors de la compétence de la rédaction (le rapport le dit) ; aucune décision de la mère sur ces questions n'était inscrite au registre à l'heure de ce brouillon. Seule la condition sur la consommation du flux par le juge candidat est écrite d'avance, valable si Q-1 est retenue. Le texte reste non scellable (statut de l'en-tête) |
| m1' (lecture (5) « sans pouvoir » et étage 1) | C1, C2 | **acceptés tels quels** |
| m2' (seuil des 12 heures) | C3 | **accepté tel quel** |
| m3' (prononcé manquant du serrage) | C4, etage-1-serrage | **C4 accepté tel quel**. Le rapport demande aussi « l'étage 1 gardant les défauts constatés sur le jeu » sans en donner le couple : la clause du serrage que m9 (tour 1) avait mise à l'étage 1 en est retirée par un couple du rédacteur, sans quoi la table dirait « garantie mise en défaut » là où la liste d'arrêt dit « aucun prononcé de la table » |
| m4' (borne de Markov de P14) | C5 | **accepté tel quel** |
| m5' (attribution de m7) | C6 | **accepté tel quel** |
| m6' (colonnes de réfutation de P7 et P8) | C7, C8 | **acceptés tels quels** |
| m7' (crédits et hors crédits) | C9 | **accepté tel quel** |
| m8' (renvoi non défini) | C10 | **accepté tel quel** ; l'annexe A de [T] reprend elle-même la construction de l'annexe A du banc B v1 ; l'annexe B de ce texte donne le chemin et l'empreinte des deux |
| m9' (essai à blanc et code ; facultative, non demandée) | — | **non appliquée** : le rapport la dit facultative et ne la demande pas ; aucun couple ; à la mère si elle la veut |
| § 2, réserve « sans conséquence » (phrase de répartition muette sur les copies par morceaux de « vide ») | — | **non appliquée** : le rapport ne demande rien |
| § 6, points pour la mère | — | **à la mère** : Q-1, Q-2, Q-3 ; lettres des modèles au registre ; tâche d'attente avant le jeu ; aucun mot de Lazar nécessaire pour ce texte |

**Remarques du rédacteur, sans effet sur le texte** (pour la mère et la contre-lecture 3). (1) Le compte de l'annexe A rend
plausible que la lecture (5) soit déclarée « sans pouvoir sur le banc réel » par sa propre règle (mutation sur les arrêts de A,
moyenne seule jugée, huit voisines par génération sur 500 générations) ; la règle écrite la range alors sans critère, du côté
sûr. Une lecture appariée (mutation moins règle saine, sur les mêmes trajectoires) ou la mutation « G lit le bloc suivant »
rejouée sur le bras G de la famille « nul » auraient plus de pouvoir ; ce serait un changement de conception, que ce tour ne
fait pas. (2) Dans la série d'essai de l'annexe A, la borne haute de F passe sous 1 : c'est un cas d'« audit écrit » du Seuil,
et l'audit fait dans l'annexe le range en écart d'échantillonnage ; au jeu, la même situation reste un audit, non un défaut.

**Ce qui reste avant le scellement** (remplace « Ce qui reste avant la contre-lecture 2 » ci-dessus) : réponses de la mère à
Q-1, Q-2 et Q-3, puis, par couples, les lignes qui en dépendent retirées ou gardées (ligne de la liste d'arrêt sur le juge
candidat et condition sur la consommation du flux, lignes du Coût, questions ouvertes ; couples M1-a et M1-b du tour 1 si Q-2
tranche pour 500 générations) ; contre-lecture 3, limitée aux parties touchées par ce brouillon et aux deux annexes, par un
sous-agent neuf qui n'a écrit ni les brouillons ni les rapports, d'un autre modèle que le rédacteur du brouillon 3, avec ce
brouillon, le rapport du tour 2, le différentiel, les deux comptes et leurs sorties, [T] (réserve (a) de la Métrique, annexe
A), le banc B v1 (annexe A), [V] (§ 1, § 3.5, § 4), le programme de [CL] et `synthetique_v1.py`.

**Déclaration du rédacteur du brouillon 3.** Heures (`date -u`) : début vers 01:53Z (premier relevé 01:54:26Z) ; comptes des
annexes de 02:07Z à 02:33Z ; écriture par le programme à @HEURE@, scellement aussitôt après (compagnon `.sha256`). Dépôt lu sur
`main`, tête `@TETE@` ; aucun commit, aucune poussée. Lu en entier : le rapport du tour 2 et le brouillon 2 ; lu en partie : [T]
(Garantie, Prédiction, Métrique, Seuil, banc B v2 et familles, bras, graines, étapes, annexes A et B), [V] (en-tête et § 1 à
4), le banc B v1 (banc B et annexe A), le programme de [CL] et sa sortie, `synthetique_v1.py`, les lignes d'import de trois
modules gelés, le programme du brouillon 2 (pour la forme), deux registres (recherche d'une décision de la mère sur Q-1 à
Q-3 : aucune), une recherche de mots dans quatre pièces voisines des cribles (i) et (ii) (forme d'une réponse sans couple),
l'état du dépôt (`git status`, noms de fichiers seulement). Comptes : processeur seul, `nice -n 19`, graines d'essai
seulement, interpréteur et bibliothèques du dépôt (Python 3.13.18, numpy 2.4.6) ; essais intermédiaires dans le bloc-notes
de la session, hors dépôt, dont aucun chiffre n'est cité ici que les comptes versés ne refassent. Jamais ouvert : rien sous
`diag/`, `runs/`, `donnees/` ; aucune branche `calcul/*` ni `donnees/*` ; rien de 7a, 7b, T0.6, T0.7, B bis, P3-bis, du bras
d'attaque, du pilote MR-2 ; aucun secret, aucune variable d'environnement affichée ; aucune machine, aucun appel réseau ;
aucun fichier existant modifié. Incidents : (a) une recherche dans `registres/etat.md` a affiché des lignes d'état qui nomment
d'autres travaux (B bis, T0.7, pilote MR-2) : aucune de leurs pièces n'a été ouverte, rien n'en est employé ; (b) la liste des
processus du conteneur a été lue (commandes seulement) pour mesurer la charge avant les comptes ; (c) une première série
d'essai de l'annexe A, de 4 000 générations, donnait pour F une moyenne de Λ nettement sous 1 : l'audit (variance exacte, dix
séries indépendantes, partie 3 du compte versé) la range en écart d'échantillonnage, et la série finale, de 20 000
générations, contient ces 4 000 premières ; rien n'en est caché dans l'annexe."""

ANNEXE_A = """## Annexe A — compte de dimensionnement du serrage (sans juge, sans nul de production)

Objet (défaut M1' de la contre-lecture 2) : fixer la distance des 24 cartes du monde jouet du serrage ; compter, sans donnée
du juge, la variance de Λ au plafond, la demi-largeur attendue de l'intervalle d'une règle saine et la borne basse attendue de
la mutation « la règle lit le bloc suivant » ; dire ce que ce compte apprend du pouvoir de la lecture (5).

Construction : le monde jouet du jeu synthétique de [T] (`src/controle_ia/organisme_idees_juge/synthetique_v1.py`,
`febe203ab27796ba573accea6e6fea5692bc2c776191254408ab07d3cc9815d7`), bâti comme le programme de [CL]
(`docs/notes/organisme-idees-juge-v1/contre-lecture-prereg-tirages-repartis-v1-outils/essai_validite_v1.py`,
`01c648a0f5a65a578e95f73836666d0e55d837ee72438e15b0d37443cbfff205`) : 3 issues, un trait binaire, nul composite à deux lois,
monde dans la classe, 24 cartes Q_i = softmax(log P + ε_i·N(0, 1)) hors de la classe, maximum de vraisemblance recalculé à
chaque instant, blocs de 25, plafond 800, budget 4 800, m = 24, lois et issues tirées par génération (écart E-2 de [AE]).
**Seule la distance change** : ε_i de 0,01 à 0,03 au lieu de 0,10 à 0,30. Règles F, A, G et règle gloutonne qui anticipe :
fonctions du programme de [CL], importées telles quelles après contrôle de son empreinte (règles simplifiées, qui suffisent à
un dimensionnement ; au jeu, les règles du serrage sont celles du rejeu gelé) ; la copie des tirages est contrôlée contre
`synthetique_v1.py` (partie 0 du compte). Λ est lu au temps d'arrêt de la règle (premier instant révélé où log W atteint
log(m/α), sinon dernier instant révélé). Graines d'essai `SeedSequence(entropy=20261117, spawn_key=(k, g))`, jamais `(97, g)`,
`(98, g)` ni la racine d'un texte. Compte : `compte-annexe-a-serrage-v1.py` (`@SHA_CA@`), sortie
`sortie-compte-annexe-a-serrage-v1.txt` (`@SHA_SA@`), même dossier, scellés ; processeur seul, Python 3.13.18 et numpy
2.4.6 du dépôt, trois minutes (de 02:30Z à 02:33Z). Sortie, recopiée en entier :

```
@SORTIE_A@
```

Lecture.

1. **Distance.** À la distance de [T], la variance de Λ au plafond est astronomique (médiane 6,4·10⁵, moyenne 1,5·10¹²⁵) : la
   moyenne de Λ sur 20 000 générations y serait faite d'événements jamais tirés, et la lecture serait sans objet. De 0,01 à
   0,05, la queue reste lourde (maximum 1,3·10⁴). **Distance retenue : ε_i de 0,01 à 0,03** (24 valeurs régulièrement
   espacées) : variance de Λ au plafond de médiane 0,146, de moyenne 0,262, de quantile 0,999 égal à 3,8 et de maximum 31,7 sur
   480 000 cartes d'essai.
2. **Règles saines.** Pour toute règle non anticipante, la variance de la moyenne des 24 Λ au temps d'arrêt est au plus la
   somme de leurs variances au plafond divisée par 24² (pour chaque carte, l'espérance du carré de Λ − 1 est la somme des
   carrés de ses accroissements, que l'arrêt ne fait qu'écourter ; les produits croisés de deux cartes sont d'espérance nulle,
   une seule carte avançant à chaque pas) : demi-largeur projetée au plus 0,0015 sur 20 000 générations, pour F-arrêt, P et P′
   comme pour les règles jouées ici. Sur la série d'essai de 20 000 générations, F, A et G donnent 0,9992, 0,9993 et 0,9998,
   chacune à ± 0,0007 ; aucune domination franchie ; aucun arrêt haut (les cartes sont trop proches du monde pour qu'une
   promotion arrive) ; les parts « bas » de F et de G sont des étiquettes, seule A s'arrête bas (5 % des cartes).
3. **Audit de la série d'essai (R4).** La borne haute de F y passe sous 1 (0,9999) : au jeu, ce serait un cas d'« audit écrit »
   du Seuil. L'espérance est exactement 1 par construction ; dix séries indépendantes de 4 000 générations donnent des écarts
   réduits de −1,68 à +0,96 (écart type 0,86), presque les mêmes par la variance exacte : écart d'échantillonnage, non biais. La
   probabilité de fausse alerte est celle que le Seuil écrit (jusqu'à environ 14 % pour six règles à 95 % ; de même pour une
   borne haute sous 1, qui ne demande qu'un audit écrit).
4. **Mutation.** « G lit le bloc suivant » (chaque bloc va à la carte dont log W après ce bloc sera la plus grande) : moyenne
   1,0142 ± 0,0007 ; différence appariée avec G sur les mêmes tirages +0,0144 ± 0,0004 ; **borne basse attendue sur 20 000
   générations ≈ 1,013**, soit une marge d'environ vingt demi-largeurs au-dessus de 1 : la mutation est tuée. C'est la mutation
   que le serrage joue (Métrique). Une mutation qui ne joue que sur les arrêts de A (A décide ses arrêts sur l'instant suivant,
   non révélé) n'est pas tuée par le critère « borne basse > 1 » (0,9999 ± 0,0006 ; effet apparié +0,0006 ± 0,0001) : là où
   les arrêts bas sont rares, elle ne change presque rien.
5. **Pouvoir de la lecture (5)** (Métrique : mutation rejouée sur le bras A de la famille « nul »). Ce compte ne dit rien du
   banc réel, où les voisines du monde s'arrêtent bas bien plus souvent sous A ([V] § 3.6, R-1 : moyenne des valeurs e 0,052
   sous A contre 0,089 sous F, l'arrêt bas gelant des valeurs e très petites) ; il montre seulement qu'une mutation qui ne joue
   que sur les arrêts de A a un effet petit, que la moyenne seule voit mal. Avec huit voisines par génération sur 500
   générations, l'issue « sans pouvoir sur le banc réel » est plausible ; la règle écrite la range alors sans critère, la
   réserve 3 de [V] restant portée par le serrage seul."""

ANNEXE_B = """## Annexe B — compte de dimensionnement des doses neuves (sans juge, sans nul)

Objet (défaut M2' de la contre-lecture 2, après m10 du tour 1) : information sur 200 épisodes des dix doses neuves et
couverture attendue de F par famille ; si la couverture attendue de F en « réplique » ou en « porteuse unique » dépassait 0,95
en moyenne, les doses seraient à revoir avant le scellement (règle du rapport, décision de la rédaction).

Construction : exactement celle des deux comptes publiés dont ce texte reprend la méthode, l'annexe A du banc B v1
(`docs/notes/organisme-idees-juge-v1/prereg-nul-par-morceaux-limite-v1.md`,
`46ef2b92119ee5dff05727b90ca8bdd3ba57b52f9c1c75893750c792a2abc089`, cité par [T] ; lignes V1 à V4, script
`c52b822296e2f4b5d0417e5400e99d5626217ebba667ab5ddfb990f9cf78ce93`) et l'annexe A de [T] (ligne V5, script
`ffa8d9b617b82e6de27165db07efc9beb89cd8e221d21f6bdabf13ea96f65274`) : information moyenne par épisode E_x KL(monde ‖ S1), 300
mondes, 4 000 instances par monde ; ici, pour chaque type, les deux doses de l'idée 1.2 et les deux doses neuves sont comptées
sur les **mêmes** 300 mondes. Contrôles : les deux scripts publiés, extraits de leurs textes (empreintes retrouvées) et
rejoués tels quels, rendent leurs sorties à l'octet près (empreintes publiées
`e8899d3fdf21640e7568e569091f0fef6d5376d4fab3240f0f5eac53f9d602d9` et
`bf2a94eb29a8d12130acbf2e0602802e801895783af8aa3dd7c68c3fbf4666cd` retrouvées) ; la fonction du compte, rejouée dans leur ordre
et sur leur graine, retrouve leurs quinze lignes (contrôle écrit dans le compte, qui s'arrête sinon). Graine d'essai
`SeedSequence(20261117)`. Compte : `compte-annexe-b-doses-v1.py` (`@SHA_CB@`), sortie `sortie-compte-annexe-b-doses-v1.txt`
(`@SHA_SB@`), même dossier, scellés ; processeur seul, Python 3.13.18 et numpy 2.4.6 du dépôt, vingt secondes. Sortie,
recopiée en entier :

```
@SORTIE_B@
```

Lecture.

1. **Information.** Doses neuves basses : 4,9 à 6,0 nats sur 200 épisodes (V1 5,9 ; V2 4,9 ; V3 4,9 ; V4 6,0 ; V5 5,3) ; doses
   neuves hautes : 12,8 à 15,8 nats (V1 15,8 ; V2 13,5 ; V3 13,8 ; V4 12,8 ; V5 14,2). Sur les mêmes mondes, les doses de l'idée
   1.2 portent 2,2 à 3,2 nats (basses) et 8,6 à 10,4 nats (hautes) : dans chaque type, la dose neuve basse tombe entre les deux
   doses de l'idée 1.2 et la dose neuve haute au-dessus de la haute. Part des mondes dont l'information sur 200 épisodes passe
   log 480 : 0,29 à 0,49 aux doses neuves basses, 0,76 à 0,94 aux hautes. La dose 1,0 de V2, V3 et V5 porte 13,5 à 14,2 nats
   pour 6,17 (log 480) nécessaires à une carte seule : les cellules de dose haute sont proches du plafond pour F, comme le
   texte le disait par interpolation (« environ 13 nats », que le compte remplace).
2. **Couverture attendue de F en « réplique »** (composition de la famille T de [V]). Hypothèse déclarée : dans chaque type, la
   couverture de F croît avec la dose (l'information croît sur les mêmes mondes ; [V] § 3.5 et § 4 : de 0,09 à 0,19 aux doses
   basses à 0,44 à 0,80 aux doses hautes). Alors chaque cellule neuve couvre au moins autant que la cellule de même type et de
   même rang de [V], et chaque cellule neuve de dose basse au plus autant que la cellule de dose haute de son type dans [V]. La
   couverture réunie étant la moyenne des dix cellules (75 générations chacune), elle est **au moins de 0,413** (celle de [V],
   § 1 : 310 générations sur 750) et **au plus d'environ 0,87** (somme des cinq cellules hautes de [V], plus 5, le tout divisé
   par 10 ; la somme des cinq cellules hautes vaut 4,13 moins celle des cinq basses, chacune d'au moins 0,09, § 3.5). Ces
   bornes portent sur l'espérance, à l'erreur d'estimation des chiffres de cellule de [V] près (quelques centièmes).
3. **« Porteuse unique ».** Sa porteuse est l'une des quatre constructions que « réplique » porte toutes (avec deux doublons) :
   sa couverture attendue est au plus celle de « réplique », donc au plus d'environ 0,87. Sa borne basse n'est **pas** établie
   par ce compte (il y faudrait le juge) ; si elle sortait à 0,05 ou moins, l'étage 2 rangerait la famille « hors de la zone
   utile », du côté sûr.
4. **« Dense »** : douze porteuses, couverture au moins de l'ordre de celle de « réplique », proche du plafond aux doses
   hautes ; aucune zone utile n'y est exigée (gain rapporté sans critère). **« Nul » et « vide »** : aucune porteuse, aucune
   couverture.
5. **Conclusion.** La règle de la contre-lecture 2 (doses à revoir si la couverture attendue de F dépasse 0,95 en moyenne en
   « réplique » ou en « porteuse unique ») **ne joue pas** : les doses sont gardées. P1, P2 et P9, relues avec ce compte, ne
   changent pas : le critère de P1 et de P2 (≥ +0,05, borne basse > 0) reste atteignable sur toute la plage (gain au plus
   1 − C_F, soit au moins 0,13) ; l'économie de P9 tient surtout aux non porteuses, que la dose touche peu (seules les fausses
   construites portent une composante de même dose)."""

for cle, val in (("@SHA_SOURCE@", SHA_SOURCE), ("@SHA_RAPPORT@", SHA_RAPPORT), ("@PROGRAMME@", PROGRAMME),
                 ("@SHA_CA@", COMPTES["compte-annexe-a-serrage-v1.py"]),
                 ("@SHA_SA@", COMPTES["sortie-compte-annexe-a-serrage-v1.txt"]),
                 ("@SHA_CB@", COMPTES["compte-annexe-b-doses-v1.py"]),
                 ("@SHA_SB@", COMPTES["sortie-compte-annexe-b-doses-v1.txt"]),
                 ("@HEURE@", heure), ("@TETE@", tete)):
    SOUS_SECTION = SOUS_SECTION.replace(cle, val)
    ANNEXE_A = ANNEXE_A.replace(cle, val)
    ANNEXE_B = ANNEXE_B.replace(cle, val)
ANNEXE_A = ANNEXE_A.replace("@SORTIE_A@", SORTIE_A)
ANNEXE_B = ANNEXE_B.replace("@SORTIE_B@", SORTIE_B)
for k in REDACTEUR:
    REDACTEUR[k][1] = REDACTEUR[k][1].replace("@HEURE@", heure).replace("@TETE@", tete)

REDACTEUR["contre-lecture-et-annexes"] = [
    "\n\n## Citations obligatoires (N-064, N-067)\n",
    "\n\n" + SOUS_SECTION + "\n\n" + ANNEXE_A + "\n\n" + ANNEXE_B + "\n\n## Citations obligatoires (N-064, N-067)\n"]

for k, v in REDACTEUR.items():
    if k in couples:
        arret(f"identifiant de couple en double : {k}")
    couples[k] = v
if any("@" in n and re.search(r"@[A-Z_]+@", n) for _a, n in couples.values()):
    arret("marque de remplacement restée dans un « nouveau »")

# Unicité et absence de chevauchement, puis application sur les positions du brouillon 2
spans = []
for k, (a, n) in couples.items():
    c = src.count(a)
    if c != 1:
        arret(f"couple {k} : « ancien » présent {c} fois dans le brouillon 2")
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
print(f"{len(couples)} couples appliqués ({len(EXIGES)} du rapport, tels quels ; {len(couples) - len(EXIGES)} du rédacteur : "
      f"{', '.join(REDACTEUR)}) ; heure {heure}")
print("cible", CIBLE.name, h(CIBLE.read_bytes()))
print("différentiel", DIFF.name, h(DIFF.read_bytes()))
