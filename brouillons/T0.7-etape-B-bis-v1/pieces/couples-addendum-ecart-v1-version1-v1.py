"""Version 1 de l'addendum d'écart de B bis (texte à sceller) = brouillon 2 (32d91c4c…) + les couples ci-dessous : titre, date,
statut, les deux marqueurs remplis par les valeurs relevées par la mère (par les noms seulement) et la mesure de la quatrième passe
de répétition (sortie sur données synthétiques), et les phrases du § 4 et du § 5 qui disaient la passe en cours ou non mesurée.
Usage : python -I couples-addendum-ecart-v1-version1-v1.py DOSSIER_DES_BROUILLONS_DE_B_BIS
Arrêt (code 1) si l'empreinte du brouillon 2 n'est pas la bonne, si un « ancien » ne figure pas exactement une fois, si un des seize
blocs de texte change d'un octet, s'il reste un marqueur, ou si la cible existe déjà (R12)."""
import hashlib, re, sys
from pathlib import Path

DOSSIER = Path(sys.argv[1])
SOURCE = DOSSIER / "T0.7-etape-B-bis-v1-addendum-ecart-v1-brouillon2.md"
CIBLE = DOSSIER / "T0.7-etape-B-bis-v1-addendum-ecart-v1.md"
SHA_SOURCE = "32d91c4c6ec74ec52400e327c4196c0cc201c493c80aaa69592592ef2610b416"
BLOC = re.compile(r"```text\n(.*?)\n```", re.S)

def arret(motif):
    print("ARRET :", motif); sys.exit(1)

brut = SOURCE.read_bytes()
if hashlib.sha256(brut).hexdigest() != SHA_SOURCE:
    arret("empreinte du brouillon 2 inattendue")
if CIBLE.exists():
    arret(f"{CIBLE.name} existe déjà")
t = brut.decode("utf-8")
blocs_avant = BLOC.findall(t)
if len(blocs_avant) != 16:
    arret("seize blocs attendus")

COUPLES = [
("V-titre", "réserve R-PILE — v1 — brouillon 2\n", "réserve R-PILE — v1\n"),
("V-date", "  l'octet à ceux du brouillon 1 (vérifié par ce programme).\n",
 "  l'octet à ceux du brouillon 1 (vérifié par ce programme).\n"
 "- **Version 1** : même auteur, 2026-11-16, de 00:53 à 00:53 (`date -u`) = brouillon 2 (`32d91c4c…`, gardé tel quel, R12) + les\n"
 "  couples de `brouillons/T0.7-etape-B-bis-v1/pieces/couples-addendum-ecart-v1-version1-v1.py` (titre, date, statut, les deux\n"
 "  marqueurs remplis, et les phrases du § 4 et du § 5 sur la quatrième passe) ; seize blocs égaux à l'octet à ceux du brouillon 2,\n"
 "  donc du brouillon 1 (vérifié par ce programme).\n"),
("V-statut", "- **Statut** : brouillon 2. Il ne vaut addendum qu'après une contre-lecture par un sous-agent neuf (R2), son scellement sous",
 "- **Statut** : version 1, à sceller par la mère après la vérification éclair du différentiel brouillon 2 → cette version ;\n"
 "  contre-lu au brouillon 1 (R2 ; R-2956) ; les points P1 et P1 bis du § 7 sont remplis (§ 4 et § 5). Il ne vaut addendum qu'après son scellement sous"),
# § 4 : la quatrième passe a tourné
("V-par4-passe", "la passe tourne depuis 00:35 UTC (instance créée, R-2953), sur données synthétiques seulement ; sa mesure :\n  § 5, point 5 ;",
 "la passe a tourné ensuite, sur données synthétiques seulement (machine 60858032, créée à\n"
 "  00:35:00Z, détruite à 00:47:24Z, absence prouvée ; R-2953, R-2957) ; sa mesure : § 5, point 5 ;"),
# marqueur 1
("V-etat-B", "son état à l'heure du scellement\n  de cet addendum, et absence de la branche de données de B bis à la même heure : `<<ETAT_ETAPE_B_AU_SCELLEMENT_ADDENDUM>>`\n"
 "  (relevé par la mère, par les noms seulement ; point ouvert P1 du § 7).",
 "état relevé par la mère avant le\n"
 "  scellement de cet addendum, le 2026-11-16T00:51:45Z (`date -u`), par la même méthode, par les noms seulement (`git ls-tree -r\n"
 "  --name-only`, compte des chemins égaux au nom ou finissant par /nom, aucun fichier ouvert) : sur `main` au commit\n"
 "  `120d8dc2440ba896a77d771c6e68b2ee27dafd4c`, `lecture-t07.json` 0 et `arret-etape-b.json` 0 ; sur `donnees/t07-etape-a-v1` au\n"
 "  commit `0c176db582ec13705e8fb7cc2d281215e2766e42`, 0 et 0 : **absents, étape B non exécutée** ; à la même heure,\n"
 "  `git ls-remote --exit-code origin refs/heads/donnees/t07-etape-b-bis-v1` rend le code 2 (branche de données de B bis\n"
 "  absente) ; branches distantes dont le nom contient « t07 » : celles de `ABSENCE-B-BBIS`, plus `coffre/audit-fuites-t07-v1`,\n"
 "  `prep/t07bbis-code-v1`, `calcul/t07bbis-repetition-v1`, `-v2` et `-v4` (point P1 du § 7)."),
# § 5, point 5 et marqueur 2
("V-par5", "5. rien n'a encore été mesuré **sur carte** pour l'écart à 3 époques, l'égalité de deux lots construits sur la carte et le\n"
 "   déterminisme à 300 époques (contre-lecture du brouillon 6, § 7). Mesure de la quatrième passe de répétition (données synthétiques, R-2953 ; règle de\n"
 "   lecture du premier écart) : `<<MESURE_QUATRIEME_PASSE_REPETITION>>` (chemin et empreinte de la sortie poussée, écart de la\n"
 "   linéaire à 300 époques, écart de l'attention à 3 époques, déterminismes, lot reconstruit, issue de la règle de lecture ;\n"
 "   rempli par la mère avant le scellement).",
 "5. jusqu'à la quatrième passe de répétition, rien n'avait été mesuré **sur carte** pour l'écart à 3 époques, l'égalité de deux\n"
 "   lots construits sur la carte et le déterminisme à 300 époques (contre-lecture du brouillon 6, § 7). **Mesure de la quatrième\n"
 "   passe** (données synthétiques seulement ; R-2953, R-2957 ; règle de lecture du premier écart) : branche\n"
 "   `calcul/t07bbis-repetition-v4`, commit `75bc5b325c1668821f8626c5f415ea3e24c7feb6` (parent `ce470564`), fichier\n"
 "   `traces/bbis-t07-repetition-v4/repetition-carte.json`, `cbcaeb5242583d99d11c2c02a8dbfa559a0a9551887f816f7a47e643e63a35a4`\n"
 "   (par `git show`, recalculée par l'auteur) : code 0 ; essais sur la machine « 115 passed, 24 skipped »\n"
 "   (`traces/bbis-t07-repetition-v4/essais.txt`, `6fc36ceb73b92ad652667f1fe29a9877a1f7e5674c15b375609c5237ec317409`) ; carte A100\n"
 "   SXM4 80 Go, torch 2.14.1+cu130 ; fraction de la course 1,0 (640 actions, largeur 4 096) ; écart de la linéaire à 300 époques\n"
 "   1,954·10⁻⁸, de l'attention à 3 époques 1,486·10⁻⁸ (256 actions, tolérance 10⁻⁴) ; déterminisme vrai pour les deux familles ;\n"
 "   attention à 300 époques égale au bit près ; lot reconstruit égal au premier ; `lecture_de_la_passe` : compte, issue « la\n"
 "   course part sans nœud » (seuil 10⁻⁵) ; mémoire de carte au plus 10 361 273 856 octets. **Ce que la passe ne prouve pas** :\n"
 "   elle porte sur des données synthétiques sans signal apprenable, non sur les activations de 7b ; elle ne joue ni le tirage du\n"
 "   couple en fin d'apprentissage (`ControleCarte.jouer`), ni `marche_v3`, ni `lecture_v2`, ni la relecture ; un seul jeu de\n"
 "   réglages (couche 15, l2 = 10⁻³ au contrôle) ; elle ne dit rien d'une autre carte ni d'une autre pile."),
]
for nom, ancien, nouveau in COUPLES:
    n = t.count(ancien)
    if n != 1:
        arret(f"couple {nom} : « ancien » trouvé {n} fois")
    t = t.replace(ancien, nouveau)
if BLOC.findall(t) != blocs_avant:
    arret("un bloc de texte a changé")
if "<<" in t or ">>" in t:
    arret("un marqueur reste")
CIBLE.write_text(t, encoding="utf-8")
print(f"couples appliqués : {', '.join(c[0] for c in COUPLES)} ; seize blocs égaux ; aucun marqueur ; écrit {CIBLE.name}")
