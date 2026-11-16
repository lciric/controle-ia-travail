"""Brouillon 3 (mise au propre) de l'addendum d'empreintes de l'idée 1.1 (poids du nul) : applique au brouillon 2
(jugé scellable au tour 2 de sa contre-lecture, `cc93ae32…`) les seuls changements décidés par la mère et par Lazar :

(1) le jeton du mot de Lazar (§ 4.4) remplacé par le mot de Lazar sur D5 (GO-2026-11-16-07, point 2) ;
(2) la reprise d'un jeu interrompu interdite (R-2988, point 1) : § 4.3, § 5 (durée, puce « Reprise »), § 7 (deux renvois) ;
(3) la lettre du rédacteur des corrections du brouillon 2 corrigée de « C » en « A » (R-2992, point 0) : en-tête et § 8 ;
(4) l'en-tête : version, heure (`date -u`), état.

- vérifie l'empreinte du brouillon 2 et celle du rapport du tour 2 ;
- vérifie par clé que les lignes GO-2026-11-16-07, R-2988 et R-2992 existent et portent ce qu'on en cite ;
- exige que chaque « ancien » figure exactement une fois dans le brouillon 2 et qu'aucun couple n'en chevauche un autre ;
- exige, après application, les 46 mêmes lignes au format du lanceur (« empreinte, deux espaces, chemin »), le bloc
  programme inchangé à l'octet, aucun jeton restant, aucune lettre « C » de rédacteur et aucun nom de modèle ;
- refuse d'écraser la cible.
L'heure de l'en-tête est lue par `date -u` au moment de l'écriture ; le scellement suit aussitôt.
Lancé par `python3 -I -B` ; aucun calcul lourd.
"""
import hashlib
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path("/home/user/controle-ia-travail")
DOSSIER = RACINE / "docs/notes/organisme-idees-juge-v1"
SOURCE = DOSSIER / "addendum-empreintes-idee-1-1-v1-brouillon2.md"
SHA_SOURCE = "d2b20dee4feecc73d3d4be8f409bc9569bd29c30d320f5e4c7d536d45ca504ce"
RAPPORT = DOSSIER / "contre-lecture-addendum-empreintes-idee-1-1-tour2-v1.md"
SHA_RAPPORT = "cc93ae325350c636b3d8292e251f0c7bfaed0f3b979fe37b7839f42bd0d11ebc"
CIBLE = DOSSIER / "addendum-empreintes-idee-1-1-v1-brouillon3.md"
PROGRAMME = "docs/notes/organisme-idees-juge-v1/appliquer-mise-au-propre-addendum-empreintes-idee-1-1-v1-brouillon3.py"
MOTIF_LANCEUR = re.compile(r"^[0-9a-f]{64}  \S+\s*$", re.M)
DEBUT, FIN = "<!-- programme-du-jeu-idee-1-1 -->", "<!-- fin-programme-du-jeu-idee-1-1 -->"
JETON = "ACCORD-D5-A-REMPLIR"
HEURE_DEBUT = "17:08"
MOT_LAZAR = ("D5 accepté par Lazar, GO-2026-11-16-07, point 2 (`grep '^| GO-2026-11-16-07 |' registres/go.md` : "
             "verbatim « go recos »)")


def h(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def arret(msg: str):
    print("ARRÊT :", msg, file=sys.stderr)
    sys.exit(1)


def ligne_par_cle(fichier: Path, cle: str) -> str:
    lignes = [l for l in fichier.read_text(encoding="utf-8").splitlines() if l.startswith(f"| {cle} |")]
    if len(lignes) != 1:
        arret(f"{cle} : {len(lignes)} lignes dans {fichier.name}")
    return lignes[0]


def couples(heure_fin: str) -> list:
    return [
        # (4) en-tête : version
        ("# Addendum d'empreintes au préenregistrement de l'idée 1.1 (poids du nul) — v1, brouillon 2\n",
         "# Addendum d'empreintes au préenregistrement de l'idée 1.1 (poids du nul) — v1, brouillon 3\n"),
        # (3) lettre du rédacteur des corrections du brouillon 2, en-tête
        ("gardé intact) par un rédacteur neuf, lettre C, au moyen du programme de couples",
         "gardé intact) par un rédacteur neuf, lettre A, au moyen du programme de couples"),
        # (4) en-tête : puce du brouillon 3 et état
        ("scellement à 14:02. Rien d'autre ne change (§ 7).\n- Pièces (empreintes recalculées",
         "scellement à 14:02. Rien d'autre ne change (§ 7).\n"
         "- **Brouillon 3** (mise au propre ; version 1, brouillon 3) : tiré du brouillon 2 "
         "(`d2b20dee4feecc73d3d4be8f409bc9569bd29c30d320f5e4c7d536d45ca504ce`, gardé intact), jugé scellable au tour 2 de sa\n"
         "  contre-lecture (`docs/notes/organisme-idees-juge-v1/contre-lecture-addendum-empreintes-idee-1-1-tour2-v1.md`, "
         "`cc93ae325350c636b3d8292e251f0c7bfaed0f3b979fe37b7839f42bd0d11ebc`),\n"
         f"  par un rédacteur neuf, lettre A, au moyen du programme de couples `{PROGRAMME}` ;\n"
         f"  date (UTC, `date -u`) : 2026-11-16, de {HEURE_DEBUT} à {heure_fin} (écriture), scellement aussitôt après. "
         "Quatre changements seulement, décidés par la mère\n"
         "  et par Lazar : (1) mot de Lazar sur D5 au § 4.4 (GO-2026-11-16-07, point 2) ; (2) **reprise d'un jeu interrompu "
         "interdite** (R-2988, point 1) :\n"
         "  § 4.3, § 5 (durée, puce « Reprise interdite ») et deux renvois du § 7 ; (3) lettre du rédacteur des corrections "
         "du brouillon 2 corrigée de\n"
         "  « C » en « A » (R-2992, point 0), ci-dessus et au § 8 ; (4) cet en-tête. Rien d'autre ne change : les 46 lignes "
         "du § 1, le bloc programme du § 2\n"
         "  (à l'octet), les tableaux et toute autre phrase.\n"
         "- **État** : **en vigueur une fois recopié sous `prereg/organisme-idee-1-1-poids-du-nul-v2-addendum-empreintes-v1.md`** "
         "(avec son compagnon),\n"
         "  après le contrôle différentiel d'un lecteur neuf (R-2988) ; jusque-là, brouillon sans effet.\n"
         "- Pièces (empreintes recalculées"),
        # (2) § 4.3
        ("refuse plus de trois, et refuse une reprise à un autre nombre ou à d'autres réductions (`jouer_idee_1_1_v5.py`).",
         "refuse plus de trois (`jouer_idee_1_1_v5.py`) ; aucune reprise n'est permise (§ 5, puce « Reprise interdite »)."),
        # (1) § 4.4
        ("- **Mot de Lazar** : " + JETON, "- **Mot de Lazar** : " + MOT_LAZAR),
        # (2) § 5, durée
        ("comptée par le code depuis le **premier** départ (`depart.json`), reprise comprise ; au-delà : arrêt,",
         "comptée par le code depuis le départ (`depart.json`) ; au-delà : arrêt,"),
        # (2) § 5, puce « Reprise »
        ("- **Reprise** (code, non écrite dans [T]) : un run interrompu **sans** `arret.json` (machine arrêtée, conteneur repris sans\n"
         "  signal reçu) se reprend sous le même identifiant par\n"
         "  `.venv/bin/python -I -B scripts/jouer_idee_1_1_v5.py --addendum <même chemin> --reprendre <RUN_ID>` : tranches déjà écrites\n"
         "  vérifiées par leur compagnon et sautées, mêmes processus et réductions exigés, borne de 48 heures inchangée. Un\n"
         "  `arret.json` présent interdit la reprise. **Ce que la reprise ne rejoue pas** : les essais, les dix-sept mutations et "
         "les essais d'égalité E0, E9, EP, ED ne sont rejoués qu'au premier départ (la branche de reprise du lanceur n'en rejoue "
         "aucun ; manifeste et `depart.json` du premier départ gardés) ; sont revérifiés à chaque reprise : préenregistrement, "
         "arbre propre hors des dossiers du run repris, addendum et fichiers gelés, copies du juge et du v9, noms empruntés. "
         "**Classement** : [T] l. 620 interdit la relance après une exception ou un log W non fini, donc après `arret.json` ; "
         "une reprise sans `arret.json` n'en est pas une, une tranche perdue est rejouée aux mêmes graines `(i_ligne, r, …)` de "
         "ses répétitions, aucune réduction n'est ajoutée, aucune graine n'est rejouée après un échec de garde. Cette lecture "
         "est celle du rédacteur et n'est couverte par aucun mot de Lazar ; si la mère la juge écart de lettre à [T] étape 1, "
         "elle l'inscrit ici sous le nom D6 et le porte à Lazar avec D5. Une tranche à moitié écrite par une mort brutale "
         "(fichier sans compagnon) fait échouer la reprise elle-même, qui consigne alors `arret.json` : run invalide.\n",
         "- **Reprise interdite** (décision de la mère, R-2988, point 1 : `grep '^| R-2988 |' registres/decisions.md`) : toute\n"
         "  interruption du jeu, avec ou sans `arret.json` (machine arrêtée, conteneur repris, processus tué, signal reçu, tranche\n"
         "  à moitié écrite), rend le run **invalide**, sans aucune lecture de ses tranches ; la relance se fait seulement sous un\n"
         "  **addendum neuf**, comme pour l'idée 1.2 (`prereg/organisme-idee-1-2-tirages-repartis-arret-anticipe-v4-addendum-relance-v1.md`),\n"
         "  par un départ neuf, qui rejoue tous les contrôles avant le jeu (essais, dix-sept mutations, essais d'égalité E0, E9,\n"
         "  EP, ED). L'option `--reprendre <RUN_ID>` du lanceur (code, non écrite dans [T]) n'est pas une voie permise pour ce\n"
         "  jeu et ne s'emploie pas : sa branche ne rejoue ni les essais, ni les mutations, ni les essais d'égalité, que l'étape 1\n"
         "  de [T] veut rejoués avant le jeu (R-2988). Cette règle est plus stricte que le code et ne s'écarte pas de [T] : aucun\n"
         "  écart D6 n'est déclaré. La commande du jeu (ci-dessus) ne change pas.\n"),
        # (2) § 7, M1
        ("premier départ. Le classement (écart ou non, nom D6) reste à la mère, comme le rapport le demande.",
         "premier départ. Le classement (écart ou non, nom D6) reste à la mère, comme le rapport le demande. Tranché depuis\n"
         "  par la mère (R-2988, point 1 ; brouillon 3) : aucune reprise permise, aucun D6 (§ 5, puce « Reprise interdite »)."),
        # (2) § 7, rapport § 3
        ("la mort brutale est\n  couverte par la dernière phrase de M1.",
         "la mort brutale est\n  couverte par le § 5 (puce « Reprise interdite », brouillon 3 : toute interruption rend le run invalide)."),
        # (3) § 8
        ("- **Brouillon 2** — rôle : rédacteur neuf des corrections du tour 1, lettre C.",
         "- **Brouillon 2** — rôle : rédacteur neuf des corrections du tour 1, lettre A."),
    ]


def main():
    if CIBLE.exists() or Path(str(CIBLE) + ".sha256").exists():
        arret(f"cible déjà présente : {CIBLE} (jamais écrasée)")
    brut = SOURCE.read_bytes()
    if h(brut) != SHA_SOURCE:
        arret("empreinte du brouillon 2 différente")
    if h(RAPPORT.read_bytes()) != SHA_RAPPORT:
        arret("empreinte du rapport du tour 2 différente")
    go = ligne_par_cle(RACINE / "registres/go.md", "GO-2026-11-16-07")
    if "« go recos »" not in go or "**D5**" not in go:
        arret("GO-2026-11-16-07 ne porte pas ce qu'on en cite")
    r2988 = ligne_par_cle(RACINE / "registres/decisions.md", "R-2988")
    if "interdit toute reprise" not in r2988 or "addendum neuf" not in r2988:
        arret("R-2988 ne porte pas ce qu'on en cite")
    r2992 = ligne_par_cle(RACINE / "registres/decisions.md", "R-2992")
    if "rédacteur lettre C" not in r2992 or "modèle A" not in r2992:
        arret("R-2992 ne porte pas ce qu'on en cite")

    texte = brut.decode("utf-8")
    heure_fin = subprocess.run(["date", "-u", "+%H:%M"], capture_output=True, text=True, check=True).stdout.strip()
    cs = couples(heure_fin)
    places = []
    for anc, nouv in cs:
        n = texte.count(anc)
        if n != 1:
            arret(f"« ancien » trouvé {n} fois : {anc[:70]!r}")
        i = texte.index(anc)
        places.append((i, i + len(anc), nouv))
    places.sort()
    for (a1, b1, _), (a2, _, _) in zip(places, places[1:]):
        if a2 < b1:
            arret("deux couples se chevauchent")
    sortie, pos = [], 0
    for a, b, nouv in places:
        sortie.append(texte[pos:a])
        sortie.append(nouv)
        pos = b
    sortie.append(texte[pos:])
    neuf = "".join(sortie)

    if MOTIF_LANCEUR.findall(texte) != MOTIF_LANCEUR.findall(neuf) or len(MOTIF_LANCEUR.findall(neuf)) != 46:
        arret("lignes au format du lanceur changées ou pas 46")
    bloc = lambda t: t[t.index(DEBUT):t.index(FIN) + len(FIN)]
    if bloc(texte) != bloc(neuf) or neuf.count(DEBUT) != 1 or neuf.count(FIN) != 1:
        arret("bloc programme changé")
    if JETON in neuf or "A-REMPLIR" in neuf:
        arret("jeton restant")
    if neuf.count(MOT_LAZAR) != 1:
        arret("mot de Lazar absent ou en double")
    if re.search(r"rédacteur neuf[^.\n]*lettre C", neuf) or "tour 1, lettre C" in neuf:
        arret("lettre « C » de rédacteur restante")
    if re.search(r"(?i)claude|opus|sonnet|haiku|fable|gpt|gemini", neuf):
        arret("nom de modèle dans la pièce")
    for l in neuf.splitlines():
        if "--reprendre" in l and "n'est pas une voie permise" not in l and "§ 5" not in l:
            arret(f"--reprendre hors de la puce d'interdiction : {l[:80]!r}")
    with open(CIBLE, "x", encoding="utf-8") as f:
        f.write(neuf)
    print("écrit :", CIBLE, h(neuf.encode("utf-8")), "couples :", len(cs), "heure :", heure_fin)


if __name__ == "__main__":
    main()
