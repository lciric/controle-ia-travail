# Corrections du contrôle carte-processeur de la famille « attention » (option 1 ; brouillon 4 du texte de B bis), v1

**Déclaration** : même développeur que `diagnostic-ecart-attention-carte-v1.md` et `diagnostic-stabilite-aires-attention-v1.md` ;
commande de la mère après R-2917 (option 1, couples a1 à a4, b1, b2) ; **processeur seulement**, aucune machine, aucun appel
payant, aucune dépense ; aucune donnée ni entrée de 7a, 7b, T0.7 ou P3-bis ; rien sous `diag/`, `donnees/`, `docs/verdicts/` ;
**aucun fichier existant modifié** (R12 : versions neuves seulement ; la tolérance 10⁻⁴, la grille, les familles, les seuils et
`MIN_ESSAIS` = 87 sont inchangés). **Date (UTC)** : 2026-11-15. **Branche** : `prep/t07bbis-code-v1`, commit du code et du
brouillon 4 : `a36d4f0d` (parent `6b4a213e`) ; ce rapport : commit suivant.

## Verdict

1. **Brouillon 4 écrit et scellé** : `brouillons/T0.7-etape-B-bis-v1/T0.7-etape-B-bis-v1-brouillon4.md`,
   `af612cbc02a9dd5781eb1d405f3408bf6ad1bd47103641665c2153a7d0c23676`. Le corps après les six couples a **exactement**
   l'empreinte calculée (`a7a0315b…`) ; le fichier final en diffère par trois couples de forme déclarés (titre, ligne de statut,
   tableau du différentiel en tête, demandé), et le programme vérifie qu'en les retirant on retrouve ce corps au bit près.
2. **Code v2** : `validation_imbriquee_v2` (contrôle linéaire à 300 époques, attention à 3 époques, seuil 10⁻⁴ ; déterminisme de
   l'attention à 300 époques réapprise sur la carte ; arrêt « erreur de chaîne » sinon) et ses appelants en versions neuves
   (`marche_v2`, amorce et lanceur de la course v2 ; script, amorce et lanceur de la répétition v2). Chaque v2 (hors le module
   neuf) est la v1 plus un différentiel déclaré, refait et comparé par les essais.
3. **Essais** : suite de B bis **155 passés**, 0 échec, 0 sauté (138 avant ; 17 neufs) ; arbre de l'instance simulé par les
   motifs de l'amorce v2 : **99 passés, 23 sautés** (sautés nommés : chaîne de T0.6 et pièce « mots et coût » absentes de l'extraction, dont la marche v2 de bout en bout) (minimum de la course 87).

## 1. Brouillon 4

- Programme : `brouillons/T0.7-etape-B-bis-v1/pieces/couples-brouillon4-v1.py`
  (`51135f43e1d921fa18cf20527295627d5550109807a274d8b2ffc67ba9f45012`), dans la forme des couples du brouillon 3 : il vérifie
  l'empreinte du brouillon 3 (`f104917f…`) et celle du programme des couples du diagnostic (`bd8d3948…`), applique ses six couples
  tels quels (même code, lu par `runpy`), exige le corps `a7a0315b…`, puis les trois couples de forme, et refuse d'écraser un
  brouillon 4 existant (R12).
- Tableau en tête : décision R-2917, diagnostic R-2902, les deux rapports par chemin et empreinte entière, une ligne par couple
  (lieu, changement). Validateur `prereg.problemes` : mêmes quatre marqueurs restants qu'au brouillon 3 (`<<CODE_BBIS>>`,
  `<<CODE_MOTS_ET_COUT_T06>>`, `<<ENTROPIE_BBIS>>`, `<<EPREUVE_NIVEAU_DEUX_PLIS>>`), rien d'autre.
- **Point laissé à la mère (non appliqué, « exactement tes couples »)** : la section « Code neuf » du texte nomme encore
  « scripts `scripts/lancer_bbis_v1.sh` et son amorce » ; la course doit désormais passer par `scripts/lancer_bbis_v2.sh`
  (`marche_v2`). Couple a5 proposé : « scripts `scripts/lancer_bbis_v1.sh` et son amorce » → « scripts `scripts/lancer_bbis_v2.sh`
  et son amorce (marche `marche_v2` ; les v1 restent, R12) ».

## 2. Différentiel déclaré, fichier par fichier

| fichier (neuf) | nature | différentiel | essais |
|---|---|---|---|
| `src/controle_ia/t07bbis/validation_imbriquee_v2.py` | module neuf (132 lignes) | importe la v1 **sans modification** (tous ses noms) ; ajoute `controle_deux_horizons` et `ControleCarte` (sous-classe de la v1 : même tirage du couple, puis des 256 actions, même générateur) ; horizon de l'attention `EPOQUES_CONTROLE_ATTENTION = 3` ; graines des réglages par la forme de clé du texte `bbis/entrainement/sonde/<cellule>/e<k>/<réglage>` (celle de la sonde finale pour la famille retenue) ; la sonde finale est réutilisée pour sa famille ; variante (r1) : linéaire seule ; sonde de contrôle en échec : « sans objet » écrit, sans arrêt | `tests/test_t07bbis_controle_v2.py` |
| `src/controle_ia/t07bbis/marche_v2.py` | v1 + 6 couples | en-tête ; `validation_imbriquee_v2` au lieu de la v1 (import, mentions) ; `scripts/amorce_bbis_v2.sh` (3 mentions) ; commande du manifeste et du mode d'emploi `marche_v2` | égalité au différentiel ; marche de bout en bout en mode jouet (contrôle aux deux horizons écrit dans `sondes-bbis.json`) |
| `scripts/amorce_bbis_v2.sh` | v1 + 6 couples | en-tête ; lanceur v2 ; marche `marche_v2` (commentaire et commande) ; motifs d'extraction : `/scripts/amorce_bbis_v2.sh*` et `/scripts/lancer_bbis_v2.sh*` **ajoutés** (les v1 restent extraites : leurs essais tournent sur l'instance) ; blocs marqués inchangés ; `MIN_ESSAIS=87` inchangé | égalité au différentiel ; motifs ; les essais de la v1 valent pour les blocs |
| `scripts/lancer_bbis_v2.sh` | v1 + 3 couples | en-tête ; `amorce_bbis_v2.sh` (7 mentions, base64 et empreinte de la commande comprises) ; `lancer_bbis_v2.sh` (3 mentions) | égalité au différentiel |
| `scripts/repetition_carte_bbis_v2.py` | v1 + 7 couples | en-tête et docstring ; `validation_imbriquee_v2` ; bloc du contrôle remplacé par `controle_deux_horizons` (la fonction de la course, premier réglage de chaque famille, couche 15) ; sortie `controle_carte_processeur` = {linéaire, attention, déterminisme (écart nul)} + `controle_parametres`, lisible par le résumé de l'amorce | égalité au différentiel ; partie carte sur processeur : cas sain (code 0, résumé de l'amorce v2 sans erreur) ; artefacts poids altérés de 1 %, autre graine, non-déterminisme (code 9, motif écrit) |
| `scripts/amorce_repetition_bbis_v2.sh` | v1 + 7 couples | en-tête ; lanceur v2 ; **branche de sortie `calcul/t07bbis-repetition-v3`** (la v2 porte la troisième passe) ; dossier des traces `traces/bbis-t07-repetition-v2` ; script `repetition_carte_bbis_v2.py` ; amorce de la course lue : `scripts/amorce_bbis_v2.sh` (motifs, `MIN_ESSAIS`) | égalité au différentiel ; branche de sortie et noms |
| `scripts/lancer_repetition_bbis_v2.sh` | v1 + 5 couples | en-tête ; `repetition_carte_bbis_v2.py` (2), `amorce_repetition_bbis_v2.sh` (8), `scripts/amorce_bbis_v2.sh` (1), `lancer_repetition_bbis_v2.sh` (3) | égalité au différentiel |
| `tests/test_t07bbis_controle_v2.py` | essais neufs (dans l'ensemble de la course : joués sur l'instance) | 11 essais | — |
| `tests/test_repetition_bbis_v2.py` | essais neufs (hors de l'ensemble de la course) | 6 essais | — |
| `brouillons/T0.7-etape-B-bis-v1/code/fichiers-fiche-code-bbis-v2.txt` | liste de la fiche de `CODE-BBIS` | v1 (90 chemins) + les cinq fichiers neufs de la course (amorce et lanceur v2, `marche_v2`, `validation_imbriquee_v2`, essais v2) = 95 chemins, tous dans les motifs de l'amorce v2 ; `0ece847b11331100012f0387ac4a3ac2fd01361515d4102f0298bee8eab7cae3` | chemins présents |

Les couples de chaque v2 sont écrits dans les essais (`COUPLES`, ancien, nouveau, nombre d'occurrences exigé) ; l'essai refait la
v2 depuis la v1 et exige l'égalité exacte : hors de ces lignes, les essais de la v1 (blocs marqués et faux outils de
`test_t07bbis_chaine_instance_v1.py` et `test_repetition_bbis_v1.py`, gardes de la marche) valent pour la v2.

**Coût du contrôle** : sur la carte, au plus une linéaire de 300 époques (≈ 1,7 s à la répétition), une attention de 3 époques et
deux de 300 (≈ 3,5 s chacune) ; sur le processeur de l'instance, une linéaire de 300 époques (≈ 199 s à la répétition) et une
attention de 3 époques, au lieu de 300 époques de la famille retenue (≈ 388 s pour l'attention). Un lot de plus sur la carte pour
le couple (≈ 4,7 Go en double précision, sur 80 Go). Les apprentissages du contrôle ne comptent pas dans la garde de débit (comme
en v1).

## 3. Essais

- Suite de B bis (`tests/test_t07bbis_*.py`, `tests/test_repetition_bbis_v1.py`, `tests/test_repetition_bbis_v2.py`) :
  **155 passés**, 0 échec, 0 sauté, en 656 s (`essais-sortie-corrections-controle-attention-v1.txt`). Les 138 essais d'avant
  passent inchangés.
- Essais neufs du contrôle (R5) : cas sain (deux familles ; linéaire à l'horizon de la marche, écart ≤ 10⁻⁹ sur jouet ; attention à
  3 époques ; déterminisme) ; **artefacts** : autre graine entre carte et processeur (arrêt), poids altérés de 1 % sur la
  linéaire puis sur l'attention à 3 époques (arrêt nommant la famille et l'horizon), non-déterminisme simulé (un arrondi sur la
  seconde sonde « attention » de 300 époques : arrêt, avec et sans sonde fournie) ; variante (r1) ; horizon hors bornes (0, 40, 41
  pour 40 époques) et famille inconnue (refus) ; sonde de contrôle en échec (« sans objet », la linéaire contrôlée) ; même tirage
  du couple et des actions que la v1 sur jouet ; marche v2 de bout en bout en mode jouet.
- **Arbre de l'instance simulé** (extraction partielle réelle par les motifs de l'amorce v2 au commit `a36d4f0d`, commande des
  essais de la course) : **99 passés, 23 sautés** (sautés nommés : chaîne de T0.6 et pièce « mots et coût » absentes de l'extraction, dont la marche v2 de bout en bout) ; minimum de la course 87.

## 4. Ce qui reste non éprouvé sans carte

- L'écart carte-processeur à 3 époques de l'attention sur la carte : sur processeur, entre deux piles, 2,9·10⁻⁷ à 5,9·10⁻⁷
  (marge de plus de deux ordres sous 10⁻⁴) ; sur la carte, inconnu.
- Le déterminisme au bit près de l'attention de 300 époques sur la carte dans la marche (vrai à la répétition, deux familles).
- Le lot reconstruit sur la carte pour le contrôle (mémoire, durée) et la durée de la linéaire de 300 époques sur le processeur de
  l'instance de la course.
- Les amorces et lanceurs v2 n'ont jamais tourné sur une machine : ils ne diffèrent des v1 (éprouvées par faux outils et, pour la
  répétition, par trois passes) que par les lignes déclarées.
- De vraies activations : rien n'est mesuré dessus (interdit ici).

## 5. Pour la mère

- **La course doit passer par `scripts/lancer_bbis_v2.sh`** (amorce v2, `marche_v2`) : la v1 jouerait l'ancien contrôle. La fiche de
  `CODE-BBIS` cite `fichiers-fiche-code-bbis-v2.txt` (95 chemins) ; le commit cité doit contenir le brouillon 4 scellé (ou le texte
  scellé qui en sortira).
- Couple a5 proposé au § 1 (nom du lanceur dans « Code neuf »), à trancher avant le scellement.
- **Quatrième passe sur carte** (si la mère la commande, sous sa ligne de dépense) : `scripts/lancer_repetition_bbis_v2.sh`,
  branche de sortie `calcul/t07bbis-repetition-v3` (absente du dépôt distant à ce jour, à revérifier par la garde du lanceur),
  traces sous `traces/bbis-t07-repetition-v2/`. Elle devrait montrer : code 0 ; essais de l'arbre de l'instance au moins 87 ;
  linéaire à 300 époques ≈ 2·10⁻⁸ ; attention à 3 époques ≤ 10⁻⁴ (de l'ordre de 10⁻⁷ attendu) ; déterminisme vrai pour les deux
  familles et pour l'attention du contrôle ; ligne de résumé « écarts carte-processeur {lineaire : …, attention : …,
  determinisme_attention : 0.0} ».

## 6. Empreintes

Au commit `a36d4f0d` (code, brouillon 4, liste de la fiche) et au commit de ce rapport (sortie des essais, rapport) ; le
brouillon 4, son programme, la liste de la fiche et la sortie des essais ont leur compagnon `.sha256` :

| fichier | sha256 |
|---|---|
| `brouillons/T0.7-etape-B-bis-v1/T0.7-etape-B-bis-v1-brouillon4.md` | `af612cbc02a9dd5781eb1d405f3408bf6ad1bd47103641665c2153a7d0c23676` |
| `brouillons/T0.7-etape-B-bis-v1/pieces/couples-brouillon4-v1.py` | `51135f43e1d921fa18cf20527295627d5550109807a274d8b2ffc67ba9f45012` |
| `src/controle_ia/t07bbis/validation_imbriquee_v2.py` | `1e3fa4bc50d0026d2e99ba71d77c3fec1024c5c8dcbb3511aeabb82d295ba2cb` |
| `src/controle_ia/t07bbis/marche_v2.py` | `77a09bc0dfd8be67de6078d2c6db74ddf3cd4c5ed970fe36b43cf800085b62e2` |
| `scripts/amorce_bbis_v2.sh` | `1f9f6a624805db0bcadaf586b73e74fdf36a29b0a3bfb9481876c0c8b2127215` |
| `scripts/lancer_bbis_v2.sh` | `d18d7a8546c9eee67672a34506f5acbb3bca6738518acbd6a9517ceafb58ddb4` |
| `scripts/repetition_carte_bbis_v2.py` | `1b5289f0ffefbdef18ac93b6de4123c8a19da8b0745d644cdff504eee6655591` |
| `scripts/amorce_repetition_bbis_v2.sh` | `a9209b33d8a4be743289a511175d7e3b0e8ff33dd890adb5c6cc6bff85566bf4` |
| `scripts/lancer_repetition_bbis_v2.sh` | `b5a93e63c207b0d3208ebe38dbc956ef1f34c993e12fb2985b275441b9d6fc3e` |
| `tests/test_t07bbis_controle_v2.py` | `2a2e3d03ba7ad6d4d4871db6d9696468fd7d4958ff72bdbf827d1e8c8e49d1cd` |
| `tests/test_repetition_bbis_v2.py` | `ef2b9e58358ea5014006d67828df8033fa56cc68ccf750595edc8bb988a98db4` |
| `brouillons/T0.7-etape-B-bis-v1/code/fichiers-fiche-code-bbis-v2.txt` | `0ece847b11331100012f0387ac4a3ac2fd01361515d4102f0298bee8eab7cae3` |
| `brouillons/T0.7-etape-B-bis-v1/code/essais-sortie-corrections-controle-attention-v1.txt` | `2d225d623bc60a82e10cde4b736e6f64769ece322971e89a62209132211839be` |
| ce rapport | son compagnon `corrections-controle-attention-v1.md.sha256` |
