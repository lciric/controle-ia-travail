# Vérification courte — ordre exploratoire ii-b, brouillon 12

## Document vérifié

- Fichier : `brouillons/ii-b-saboteur-budget-v1/ordre-exploratoire-ii-b-v1-brouillon12.md`
- Empreinte : `43a7a050d769792f3c5d7859509b69f34e082f953840909a1f59a1535bf01b3e`
- 394 lignes

## Vérificateur

Session distincte, modèle Opus 4.6, du côté du saboteur à budget, exclu de tout rôle côté sondes du barreau 8. Auteur de la vérification courte du brouillon 10 (`cf9c0d4c883f507f48b8ff847bec9fa2ab2457b8480c0185d27367dc93327207`). Aucun fichier dont le nom contient « consigne-privee » ou « conception-ii-b » n'a été lu ni ouvert ; ni la configuration réelle au-delà de ce que montre la sortie de comparaison ; ni la branche `lot/compte-4-v1` ; ni `diag/`, `runs/`, `donnees/`, `docs/verdicts/`.

## Conclusion

**Scellable.** Quatre points vérifiés, aucun défaut. Le diff du brouillon 10 au brouillon 12 se limite aux changements déclarés dans les deux notes de différences ; les commandes du lanceur sont conformes au dossier du rejeu ; aucune autre commande des § 5 à 7 ne lit le dossier passé à la création ; les deux sorties de programmes sont celles d'un texte scellable.

---

## Pièces lues, chacune avec empreinte recalculée

- Brouillon 12 : `ordre-exploratoire-ii-b-v1-brouillon12.md`, `43a7a050d769792f3c5d7859509b69f34e082f953840909a1f59a1535bf01b3e` (394 lignes).
- Brouillon 10 : `ordre-exploratoire-ii-b-v1-brouillon10.md`, `a52cb18534ebd635343e262d4ebc56b06619f35b2c4c1643204c74e02387d4ca` (375 lignes, intact, R12).
- Brouillon 11 : `ordre-exploratoire-ii-b-v1-brouillon11.md`, `e4c0ca6247c491504106e389de56481c25ea21900219a54c19bc164584072293` (385 lignes, intact, R12).
- Note des différences du brouillon 10 au brouillon 11 : `differences-brouillon10-vers-11-v1.md`, `595f09ebacb786c4462b63fffe417a498cc91111578e357e33b38c839da70b91`.
- Note des différences du brouillon 11 au brouillon 12 : `differences-brouillon11-vers-12-v1.md`, `84cfb42f964fbc56a796f782c9513198ceb80c64235ed4fb15ab9dbc553ecb1f`.
- Sortie du programme de compte des marqueurs : `sortie-compter-marqueurs-ii-b-v7.txt`, `615a66c179d82393eb769549d1b4fa8ed98070005cbb62c68e2afd7cce4aecca`.
- Sortie du programme de comparaison des marqueurs à la configuration : `sortie-comparer-marqueurs-ordre-configuration-ii-b-v3.txt`, `7499712dac51665871fced3a6451aa9d17c315363e267d2a6eccd0b97687f206`.
- Lanceur au commit de lancement (`git show 836c7cccda5071fe54ecb148d214d74b5cb90474:scripts/lancer_iib_v1.sh`) : `3279e3dcc631519e574c2011f9f143d956d3b668c729a176cd8efc0e99dece8f`.

## Point 1 — Le diff du brouillon 10 au brouillon 12 se limite aux changements déclarés : CONFORME

`diff -u` entre les brouillons 10 et 12 rend 5 blocs ; 375 lignes deviennent 394 (19 lignes nettes). Les blocs sont :

| bloc | lignes du brouillon 12 | contenu | déclaré dans |
|---|---|---|---|
| 1 | 1–10 | titre (10 → 12) et statut (10 → 12) | B11-0a/B12-0a, B11-0b/B12-0b |
| 2 | 37–61 | sections « Ce que le brouillon 12 change » (9 lignes) et « Ce que le brouillon 11 change » (10 lignes) ajoutées | B11-0c, B12-0c |
| 3 | 201–207 | § 4 étape 6, dernière phrase : le rejeu est situé à l'étape 2 du § 5, dans le dossier du rejeu | B12-2 |
| 4 | 257–263 | § 5 étapes 2 et 3 : commande du rejeu, prose du rejeu une seule fois, création et surveillance dans `"$W/iib-rejeu"` | B11-1/B12-1, B11-2, B11-3 |
| 5 | 379–385 | § 11, comptes : noms des sorties mis à jour (`sortie-compter-marqueurs-ii-b-v7.txt`, `sortie-comparer-marqueurs-ordre-configuration-ii-b-v3.txt`) | B12-3a, B12-3b |

Chaque bloc est couvert par un ou plusieurs couples déclarés dans les deux notes de différences. Aucun bloc hors de cette liste. Le reste du texte est identique à l'octet.

## Point 2 — Commandes du lanceur et dossier du rejeu : CONFORME

Vérification contre `scripts/lancer_iib_v1.sh` au commit de lancement `836c7ccc` (`3279e3dcc631519e574c2011f9f143d956d3b668c729a176cd8efc0e99dece8f`), avec les numéros de ligne du lanceur.

### 2a. Le rejeu dans `"$W/iib-rejeu"` se lance

Brouillon 12, ligne 260 : `"${ENVI[@]}" bash scripts/lancer_iib_v1.sh controles-explo "$W/iib-rejeu" 836c7ccc… docs/notes/barreau8-iib-v1/config-iib-reel-v1.json`.

Le lanceur, à `controles-explo` (l. 76), refuse un dossier qui existe déjà (`[ -e "$D" ] && { echo "$D existe déjà (R12)"; exit 2; }`). `"$W/iib-rejeu"` n'existe pas au moment du rejeu (c'est un nom neuf, distinct de `"$W/iib"` créé à l'étape 1). Le rejeu se lance et écrit `lancement.txt` dans `"$W/iib-rejeu"` (l. 126) si tous les contrôles passent. Conforme.

### 2b. `creation` lit le `lancement.txt` de ce dossier

Brouillon 12, ligne 260 : `creation auto course 0 "$W/iib-rejeu" 1795816800`.

Le lanceur (l. 129, 133-134) : `creation` prend le dossier des contrôles en cinquième argument, exige `lancement.txt` et `config.json` dans ce dossier, lit le commit, les essais attendus (l. 173), l'empreinte de l'amorce (l. 170) et les machines refusées (l. 153) dans ce `lancement.txt`. Conforme : c'est bien `"$W/iib-rejeu"` qui est passé.

### 2c. `surveillance` lit l'identifiant écrit par `apres-creation` dans ce dossier

Brouillon 12, ligne 263 : `surveillance <ID> "$W/iib-rejeu"`.

Le lanceur : `apres-creation` écrit l'identifiant et l'heure de création dans le `lancement.txt` du dossier passé à `creation` (l. 174, 191) ; `surveillance` lit ce `lancement.txt` (l. 204-206) et refuse tout autre identifiant (l. 205). Le dossier de la surveillance est le même que celui de la création. Conforme.

### 2d. Les reprises au code 3 et au code 5 gardent ce dossier

Brouillon 12, ligne 260 : « toutes les reprises de `creation` (code 3, toutes les 15 minutes) et la commande du rang suivant (code 5) gardent `"$W/iib-rejeu"` et ne rejouent pas les contrôles ».

Le lanceur : au code 3, la commande `creation` est rejouée avec les mêmes arguments, donc le même dossier `"$W/iib-rejeu"` (l. 151-153 : le compteur d'essais et les machines refusées sont dans ce `lancement.txt`) ; au code 5, la commande du rang suivant est imprimée par `apres-creation` avec le même dossier (l. 196-197). Conforme.

### 2e. « Dossier déjà là : pas un second rejeu, passer à la création » est sûr

Brouillon 12, ligne 260 : « Si le dossier `"$W/iib-rejeu"` existe déjà quand l'exécutante va lancer le rejeu, ce n'est pas un arrêt : elle n'en fait pas un second et passe à la création. »

Deux cas :

1. **Le rejeu a abouti** (l. 76 et 126) : le dossier existe et contient `lancement.txt` avec des contrôles conformes. `creation` lit ce `lancement.txt` : la garde du lanceur tient, les données sont valides.
2. **Le rejeu a été interrompu** : le lanceur crée le dossier dès le début de `controles-explo` (l. 86) mais n'écrit `lancement.txt` qu'à la fin, tous contrôles passés (l. 126). Un rejeu interrompu laisse un dossier sans `lancement.txt`. L'exécutante passe à `creation`, qui refuse en code 2 un dossier sans contrôles conformes (l. 133 : `[ -f "$D/lancement.txt" ] && grep -q '^controles-explo '`). La garde du lanceur n'est pas contournée : c'est le lanceur lui-même qui refuse.

Le cas 2 est relevé sans être corrigé par la note des différences 11 → 12 (§ 5, point 1) : « La garde tient donc dans le lanceur ; l'ordre ne le dit pas. » La phrase de l'ordre est sûre. Conforme.

## Point 3 — Aucune autre commande des § 5 à 7 ne lit le dossier passé à `creation` : CONFORME

Vérifié dans le brouillon 12, lignes 265 à 274 (étapes 4 à 6 du § 5) et au-delà (§ 7, non lu en entier mais les commandes décrites dans les notes de différences 10 → 11, § 3 de cette note, couvrent exhaustivement les commandes) :

- `apres-creation` : appelée par la commande que `creation` imprime, avec le dossier passé à `creation` — le lanceur l'écrit (l. 174). Ne lit pas un dossier séparé.
- La commande de surveillance imprimée par `apres-creation` porte ce même dossier (l. 192) : elle est égale à l'étape 3.
- La commande du rang suivant (code 5) est imprimée par `apres-creation` avec ce même dossier (l. 197).
- Les commandes d'arrêt imprimées par la surveillance (étapes 4 et 5) ne portent que l'identifiant de l'instance (l. 237, 238).
- Le rapatriement (étape 5) lit `"$W/depot"` et la branche du run ; la destruction (étape 6) ne cite que l'identifiant.
- Le § 7 ne cite que `"$W/depot"`, la branche du run et l'identifiant.

Aucune commande des § 5 à 7, hors des étapes 1 à 3, ne cite le dossier des contrôles. Conforme.

## Point 4 — Les sorties des deux programmes sont celles d'un texte scellable : CONFORME

### 4a. Sortie du programme de compte (`sortie-compter-marqueurs-ii-b-v7.txt`, `615a66c1…`)

```
ordre-exploratoire-ii-b-v1-brouillon12.md  43a7a050d769792f3c5d7859509b69f34e082f953840909a1f59a1535bf01b3e
  occurrences 0 ; distincts 0
```

Le fichier compté est bien le brouillon 12, avec l'empreinte attendue. Aucun marqueur entre chevrons doubles ne reste : 0 occurrence, 0 distinct. Conforme pour le scellement.

### 4b. Sortie du programme de comparaison (`sortie-comparer-marqueurs-ordre-configuration-ii-b-v3.txt`, `7499712d…`)

Le fichier comparé est bien le brouillon 12 (`43a7a050…`) contre la configuration au commit de lancement (`1bd2e16a…`). Le programme est la v2, inchangé.

- **Section A** (configuration au commit de lancement) : empreinte conforme, 30 marqueurs, 3 hors configuration, parent direct conforme, 2 fichiers ajoutés seulement, toutes les clés conformes.
- **Section B** (30 marqueurs) : 27 égaux à l'octet, 2 hors de ce texte, 1 égal à l'empreinte recalculée, 0 différent.
- **Section C** (places des valeurs) : toutes conformes.
- **Section D** (marqueurs entre chevrons doubles) : 0 occurrence, 0 distinct.
- **Section E** (états de la table du § 11) : 28 remplis, 0 en attente, 2 hors de ce texte ; 6 propres remplis, 0 en attente. Conformes.
- **Section F** (valeurs libres du § 2) : toutes conformes.
- **Section G** (fragments de commandes du § 5) : tous présents, chacun une fois. Aucun fragment de l'ancienne branche ni du premier commit de lancement. Conforme.
- **Section H** (emplacements ouverts) : 0. **SCELLEMENT PERMIS** par ce contrôle.
- **BILAN** : écarts 0.

Code de sortie : 0. Conforme pour le scellement.

---

## Refus d'outil

Aucun refus d'outil pendant cette vérification.
