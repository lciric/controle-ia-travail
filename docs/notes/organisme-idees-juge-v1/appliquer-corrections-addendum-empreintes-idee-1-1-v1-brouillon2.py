"""Brouillon 2 de l'addendum d'empreintes de l'idée 1.1 (poids du nul) : applique au brouillon 1 les couples
« ancien → nouveau » exigés par la contre-lecture, tour 1 (`contre-lecture-addendum-empreintes-idee-1-1-tour1-v1.md`),
plus quatre couples du rédacteur (en-tête : version ; en-tête : ligne du brouillon 2 ; section « Contre-lecture » ;
déclaration d'exclusion du brouillon 2), et rien d'autre.

- vérifie l'empreinte du brouillon 1 et celle du rapport de contre-lecture ;
- vérifie que chaque « ancien » et chaque « nouveau » des couples exigés figure mot pour mot dans le rapport (m6 : ses
  deux morceaux, le rapport le donnant en deux lignes) ;
- exige que chaque « ancien » figure exactement une fois dans le brouillon 1 et qu'aucun couple n'en chevauche un autre ;
- exige, après application, les 46 mêmes lignes au format du lanceur (« empreinte, deux espaces, chemin »), le bloc
  programme inchangé à l'octet, une seule occurrence du jeton du mot de Lazar et aucun nom de modèle ;
- refuse d'écraser la cible.
L'heure de l'en-tête est lue par `date -u` au moment de l'écriture ; le scellement suit aussitôt.
Lancé par `python3 -I -B` ; aucun calcul lourd.
"""
import hashlib
import re
import subprocess
import sys
from pathlib import Path

DOSSIER = Path("/home/user/controle-ia-travail/docs/notes/organisme-idees-juge-v1")
SOURCE = DOSSIER / "addendum-empreintes-idee-1-1-v1-brouillon1.md"
SHA_SOURCE = "6bab777fd312efe921f2183508069aa12fb8aedc5b8b410fdd415dca91f4c7d9"
RAPPORT = DOSSIER / "contre-lecture-addendum-empreintes-idee-1-1-tour1-v1.md"
SHA_RAPPORT = "78ced47dfa2d6a0841a4a597ff8b516ccae35d8fa7ec157ce4b53157c052bb64"
CIBLE = DOSSIER / "addendum-empreintes-idee-1-1-v1-brouillon2.md"
MOTIF_LANCEUR = re.compile(r"^[0-9a-f]{64}  \S+\s*$", re.M)
DEBUT, FIN = "<!-- programme-du-jeu-idee-1-1 -->", "<!-- fin-programme-du-jeu-idee-1-1 -->"
JETON = "ACCORD-D5-A-REMPLIR"
HEURE_DEBUT = "14:01"


def h(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def arret(msg: str):
    print("ARRÊT :", msg, file=sys.stderr)
    sys.exit(1)


if CIBLE.exists():
    arret(f"{CIBLE.name} existe déjà : R12 interdit d'écraser")
octets = SOURCE.read_bytes()
if h(octets) != SHA_SOURCE:
    arret("brouillon 1 différent de l'empreinte attendue")
if (DOSSIER / (SOURCE.name + ".sha256")).read_text(encoding="utf-8").split()[0] != SHA_SOURCE:
    arret("compagnon du brouillon 1 différent")
octets_r = RAPPORT.read_bytes()
if h(octets_r) != SHA_RAPPORT:
    arret("rapport de contre-lecture différent de l'empreinte attendue")
texte = octets.decode("utf-8")
rapport = octets_r.decode("utf-8")

# --- couples exigés par le rapport (§ 2), recopiés du rapport et vérifiés contre lui ------------------------------
M1_ANCIEN = "`arret.json` présent interdit la reprise."
M1_NOUVEAU = (
    "`arret.json` présent interdit la reprise. **Ce que la reprise ne rejoue pas** : les essais, les dix-sept mutations "
    "et les essais d'égalité E0, E9, EP, ED ne sont rejoués qu'au premier départ (la branche de reprise du lanceur n'en "
    "rejoue aucun ; manifeste et `depart.json` du premier départ gardés) ; sont revérifiés à chaque reprise : "
    "préenregistrement, arbre propre hors des dossiers du run repris, addendum et fichiers gelés, copies du juge et du "
    "v9, noms empruntés. **Classement** : [T] l. 620 interdit la relance après une exception ou un log W non fini, donc "
    "après `arret.json` ; une reprise sans `arret.json` n'en est pas une, une tranche perdue est rejouée aux mêmes "
    "graines `(i_ligne, r, …)` de ses répétitions, aucune réduction n'est ajoutée, aucune graine n'est rejouée après un "
    "échec de garde. Cette lecture est celle du rédacteur et n'est couverte par aucun mot de Lazar ; si la mère la juge "
    "écart de lettre à [T] étape 1, elle l'inscrit ici sous le nom D6 et le porte à Lazar avec D5. Une tranche à moitié "
    "écrite par une mort brutale (fichier sans compagnon) fait échouer la reprise elle-même, qui consigne alors "
    "`arret.json` : run invalide."
)
M6_ANCIEN = "3. Copie propre du commit qui porte la version scellée"
M6_PART1 = (
    "3. Avant le départ, à la main : `sha256sum` de "
    "`docs/notes/organisme-idees-juge-v1/correction-poids-v1/projection/essai_projection_cas_v1.py`, égal à "
    "`539f6a6cfce71eaab9010fa9cd16a2607a0bf9faf9499286bcb6fb7f25bda837` (bloc § 2, m10) : le code ne compare cette "
    "empreinte qu'à son compagnon, non à l'addendum."
)
M6_PART2 = "4. Copie propre du commit qui porte la version scellée"
EXIGES = [
    ("M1", M1_ANCIEN, M1_NOUVEAU),
    ("m1", "(à la place de `ACCORD-D5-A-REMPLIR`)", "(sur la ligne « Mot de Lazar »)"),
    ("m2", "(R-2976, R-2979), et un cœur reste aux travaux de la session.",
     "(R-2979), et un cœur reste aux travaux du billet (R-2976)."),
    ("m3", "- **Statut** : décision de la mère (R-2984) :",
     "- **Statut** : code v5 rendu sous R-2978 ; décision de la mère (R-2984) :"),
    ("m4a", "arbre propre ; aucune sortie ni manifeste antérieur de ce",
     "arbre propre ; addendum lu (§ 1 et § 2) ; copies du juge et du v9 vérifiées ; noms empruntés ; aucune sortie ni "
     "manifeste antérieur de ce"),
    ("m4b", "jeu (noms v1 à v5) ; addendum lu (§ 1 et § 2) ; copies du juge et du v9 vérifiées ; noms empruntés ; essais rejoués ;",
     "jeu (noms v1 à v5) ; essais rejoués ;"),
    ("m5", "log W non fini, exception)",
     "log W non fini là où le banc le contrôle (§ 4.2 dit ce qu'il ne contrôle pas), exception)"),
    ("m6", M6_ANCIEN, M6_PART1 + "\n" + M6_PART2),
    ("m7", "Somme sur les 30 lignes : **112,806 s par répétition**",
     "Les zéros des cinq lignes H en J9-P et La-P viennent de ce que le code range tout temps non nommé par un groupe "
     "dans « base » ; [T] l. 527 et 640 dit « temps de chaque bras » : le découpage en quatre groupes est celui du code, "
     "et aucune réduction n'étant appliquée, D n'en dépend pas. Somme sur les 30 lignes : **112,806 s par répétition**"),
]
for nom, ancien, nouveau in EXIGES:
    if ancien not in rapport:
        arret(f"{nom} : « ancien » absent du rapport")
    morceaux = [M6_PART1, M6_PART2] if nom == "m6" else [nouveau]
    for mc in morceaux:
        if mc not in rapport:
            arret(f"{nom} : « nouveau » absent du rapport : {mc[:60]}…")

# --- couples du rédacteur ------------------------------------------------------------------------------------------
heure = subprocess.run(["date", "-u", "+%H:%M"], capture_output=True, text=True, check=True).stdout.strip()
jour = subprocess.run(["date", "-u", "+%Y-%m-%d"], capture_output=True, text=True, check=True).stdout.strip()
NOM_RAPPORT = "docs/notes/organisme-idees-juge-v1/contre-lecture-addendum-empreintes-idee-1-1-tour1-v1.md"
NOM_PROG = "docs/notes/organisme-idees-juge-v1/" + Path(__file__).name
REDACTEUR = [
    ("en-tête, version",
     "# Addendum d'empreintes au préenregistrement de l'idée 1.1 (poids du nul) — v1, brouillon 1",
     "# Addendum d'empreintes au préenregistrement de l'idée 1.1 (poids du nul) — v1, brouillon 2"),
    ("en-tête, brouillon 2",
     "  **Aucun jeu ; aucun résultat du jeu n'existe.**\n",
     "  **Aucun jeu ; aucun résultat du jeu n'existe.**\n"
     f"- **Brouillon 2** : corrections de la contre-lecture, tour 1 (`{NOM_RAPPORT}`, `{SHA_RAPPORT}`), appliquées au\n"
     f"  brouillon 1 (`{SHA_SOURCE}`, gardé intact) par un rédacteur neuf, lettre C, au moyen du programme de couples\n"
     f"  `{NOM_PROG}` ; date (UTC, `date -u`) : {jour}, scellement à {heure}. Rien d'autre ne change (§ 7).\n"),
    ("§ 7, contre-lecture",
     "## 7. Contre-lecture\n\n*(à remplir)*\n",
     "## 7. Contre-lecture\n\n"
     f"**Tour 1.** Rapport : `{NOM_RAPPORT}` (`{SHA_RAPPORT}`, égal à son compagnon), contre-lecteur neuf, lettre C, sur\n"
     "le brouillon 1 (`6bab777f…`). Verdict : corrections (une majeure, sept mineures, une facultative) ; rien ne met la\n"
     "conception en cause ; empreintes, bloc programme et chiffres trouvés exacts (rapport § 1).\n\n"
     "Réponse point par point (couples appliqués par programme ; chaque « ancien » trouvé une seule fois dans le brouillon 1 ;\n"
     "chaque « ancien » et chaque « nouveau » trouvé mot pour mot dans le rapport) :\n\n"
     "- **M1** (reprise) — appliquée, § 5, puce « Reprise ». Vérifié dans `scripts/jouer_idee_1_1_v5.py` (`jeu_decisif`) : la\n"
     "  branche de reprise ne rejoue ni les essais, ni les mutations, ni les essais d'égalité, et relit le `depart.json` du\n"
     "  premier départ. Le classement (écart ou non, nom D6) reste à la mère, comme le rapport le demande.\n"
     "- **m1** (jeton en double) — appliquée, § 6, point 2 : le jeton du mot de Lazar ne figure plus qu'au § 4.4, tel quel.\n"
     "- **m2** (raison des deux processus) — appliquée, § 4.3.\n"
     "- **m3** (renvoi à R-2978) — appliquée, § 4.4, « Statut ».\n"
     "- **m4** (ordre du lanceur, deux couples liés) — appliquée, § 5 ; conforme au code (`exiger_sortie_absente` vient après\n"
     "  la lecture de l'addendum, les copies et les noms empruntés, avant les essais).\n"
     "- **m5** (« log W non fini ») — appliquée, § 5.\n"
     "- **m6** (`essai_projection_cas_v1.py`) — appliquée, § 6 : point 3 neuf, l'ancien point 3 devient le point 4, sa suite\n"
     "  inchangée. Vérifié : `FICHIERS_EP` de `etape0_idee_1_1_v5.py` porte `None` pour ce fichier ; son empreinte recalculée\n"
     "  est égale à `539f6a6c…` et à son compagnon.\n"
     "- **m7** (chronométrage par groupe) — appliquée, § 3.\n"
     "- **Facultatif** (PID du parent noté au registre) — non appliqué : le rapport ne l'exige pas, et ce tour n'applique que\n"
     "  les corrections exigées.\n"
     "- Rapport § 3 (fils oisif, TERM au parent, mort brutale en pleine écriture) : rien à corriger ; la mort brutale est\n"
     "  couverte par la dernière phrase de M1.\n\n"
     "Inchangés : les 46 lignes du § 1, le bloc programme du § 2 (à l'octet), les tableaux et toute autre phrase.\n"),
    ("§ 8, brouillon 2",
     "- Incidents : aucun. Une première commande groupée de lecture a rendu un code de sortie non nul à cause d'un `ls` sur un nom encore absent (cette pièce), sans autre effet.\n",
     "- Incidents : aucun. Une première commande groupée de lecture a rendu un code de sortie non nul à cause d'un `ls` sur un nom encore absent (cette pièce), sans autre effet.\n"
     "- **Brouillon 2** — rôle : rédacteur neuf des corrections du tour 1, lettre C. Je n'ai écrit ni [T], ni le brouillon 1,\n"
     "  ni sa contre-lecture, ni le code, ni l'étape 0.\n"
     f"  Heures (UTC, `date -u`) : {jour}, de {HEURE_DEBUT} à {heure} (scellement).\n"
     "  Pièces lues : le brouillon 1 et le rapport du tour 1, en entier (empreintes recalculées) ; `scripts/jouer_idee_1_1_v5.py`\n"
     "  (`jeu_decisif`) ; `execution_idee_1_1_v5.lire_addendum` ; `execution_v1.verifier_addendum` ; `FICHIERS_EP` des modules\n"
     "  d'étape 0 ; l'empreinte de `essai_projection_cas_v1.py` et son compagnon ; le programme de couples de l'addendum de\n"
     "  relance de l'idée 1.2 (forme).\n"
     "  Calculs de ma main : le programme de couples ci-dessus ; un appel de `lire_addendum` sur cette pièce scellée. Aucun\n"
     "  jeu, aucun essai, aucun `pytest`.\n"
     "  Jamais ouverts : rien sous `diag/`, `runs/`, `donnees/` ; rien de 7a, 7b, T0.6, T0.7, P3-bis ni du bras d'attaque ;\n"
     "  rien écrit dans `/home/user/jeu-idee-1-2-copie` ni `/home/user/etape0-idee-1-1-copie-v5` ; aucune valeur de clé ; ni\n"
     "  `env` ni `printenv` ; aucun appel réseau ; aucun git de ma main ; aucun commit ; aucun fichier existant modifié.\n"
     "  Incidents : aucun.\n"),
]

COUPLES = EXIGES + REDACTEUR
positions = []
for nom, ancien, nouveau in COUPLES:
    n = texte.count(ancien)
    if n != 1:
        arret(f"{nom} : « ancien » trouvé {n} fois (une seule exigée)")
    i = texte.index(ancien)
    positions.append((i, i + len(ancien), nom))
positions.sort()
for (a0, a1, n0), (b0, b1, n1) in zip(positions, positions[1:]):
    if b0 < a1:
        arret(f"couples qui se chevauchent : {n0} et {n1}")

neuf = texte
for nom, ancien, nouveau in COUPLES:
    neuf = neuf.replace(ancien, nouveau, 1)


def bloc(t: str) -> str:
    return t[t.index(DEBUT):t.index(FIN) + len(FIN)]


if MOTIF_LANCEUR.findall(neuf) != MOTIF_LANCEUR.findall(texte) or len(MOTIF_LANCEUR.findall(neuf)) != 46:
    arret("lignes au format du lanceur changées")
if bloc(neuf) != bloc(texte) or neuf.count(DEBUT) != 1 or neuf.count(FIN) != 1:
    arret("bloc programme changé")
if neuf.count(JETON) != 1:
    arret(f"jeton du mot de Lazar : {neuf.count(JETON)} occurrences (une exigée)")
if re.search(r"opus|fable|sonnet|haiku|claude", neuf, flags=re.I):
    arret("nom de modèle dans la pièce")

with open(CIBLE, "x", encoding="utf-8") as f:
    f.write(neuf)
print(f"écrit {CIBLE} ({len(neuf.splitlines())} lignes), {len(COUPLES)} couples, scellement à {heure}")
print(h(neuf.encode("utf-8")))
