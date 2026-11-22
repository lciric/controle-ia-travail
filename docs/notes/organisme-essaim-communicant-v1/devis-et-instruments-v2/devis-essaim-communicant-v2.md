# Devis — expérience « essaim qui communique » — v2

- Pièce de préparation, **aucune dépense, aucun appel de modèle, aucun réseau**. Elle remplace la v1 sur les points D1 à D3 de la contre-lecture (`docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v1/contre-lecture-v1/contre-lecture-devis-instruments-essaim-v1.md`). La v1 reste intacte dans `../essaim-devis-instruments-v1/`.
- Le calcul se rejoue par `calcul_devis_essaim_v2.py`, qui écrit `calcul-devis-essaim-v2.json`. Les épreuves du contrôle des nombres sont dans `epreuves_devis_v2.py`, qui écrit `epreuves-devis-v2.json`. Les empreintes sont dans les compagnons `.sha256`.
- **Verdict d'abord.** Au cas attendu, l'estimation va de **2 809 USD** (Kimi) à **10 249 USD** (seconde espèce Claude, ou Astra). Le vrai pire du cas attendu va de **67 073 à 172 779 USD**. Au cas haut, le pire toutes espèces atteint **290 228 USD**. La v1 sous-estimait le pire d'un facteur 1,8 à 2,4. Ce devis n'est pas une base de demande : voir `devis-cout-reduit-essaim-v1.md` et `pilote-instrument-essaim-v1.md`.

## 1. Ce qui change depuis la v1

| défaut | correction |
|---|---|
| D1 : borne au pire d'un test, 1,50 et 0,80 USD au lieu de 1,60 et 0,90 | Les nombres sont **lus** dans `devis_multi_generations_v2.py` (`710954c7…`, l. 17-23), par analyse syntaxique, puis **utilisés**. La borne vaut `BORNE_TEST` + `VERIF_PIRE` lorsque la pièce donne une borne pour le même tarif : première espèce Claude 1,60 ; Kimi 0,90 ; tarif 10 / 50 3,50. Sinon on prend la formule de la pièce, 12 × (8 000 × entrée + 4 000 × sortie) arrondi au dixième au-dessus, plus 0,10 : Fable 2,80 ; Argon et Carbon 2,90. Le contrôle compare désormais les **nombres** lus aux valeurs recopiées, et il refuse sur cinq artefacts où un nombre diffère (§ 4). |
| D2 : un pire qui n'en était pas un | Proposeurs au **plafond de session** de 3,00 USD par appel. Aiguilleur à **0,25 USD** par appel. Messages bornés au plafond du proposeur (**supposé** : aucun plafond propre). Ajouts au pire : **tests des fausses lois et des copies** (8 par génération et par jeu), **objets de contrôle aiguillés** (13 + 8 par génération et par jeu), **relances** (marge de 10 % du devis d'affinage v5), **105 % de la section C.8**. Ajout à l'estimation : le **surcroît d'entrée du bras (a)**, soit 3 200 jetons par appel (**supposé** : trois messages relus de 400 jetons et un tableau partagé de 2 000). L'estimation et le pire sont rendus côte à côte. |
| D3 : nombres sans pièce | Chaque nombre lu est rendu avec chemin, empreinte et ligne (`provenance_des_nombres`). Plafond de l'aiguilleur : `calcul-devis-course-auto-conception-v1.py`, l. 40 (`8bd1e48a…`). Dénominateur du taux de promues : lu dans `monde_riche_v4.course` (`4b165847…`, l. 216-217 : 4 proposeurs × 6 cartes), soit 17,08 / 72 = **0,2372**. Les nombres sans pièce sont rangés sous `supposes`. |

## 2. Estimation et pire, par espèce et par cas (USD)

| espèce | bas : estimation | bas : pire | attendu : estimation | attendu : pire | haut : estimation | haut : pire |
|---|---|---|---|---|---|---|
| Kimi | 1 190 | 30 807 | **2 809** | 67 073 | 5 845 | 112 643 |
| première espèce Claude | 1 944 | 43 898 | **4 669** | 95 532 | 10 097 | 160 454 |
| Fable 5.2 | 3 453 | 66 340 | **8 389** | 144 320 | 18 601 | 242 417 |
| Argon, Carbon (borne haute) | 3 566 | 68 211 | **8 668** | 148 385 | 19 238 | 249 247 |
| seconde espèce Claude, Astra | 4 207 | 79 432 | **10 249** | 172 779 | 22 852 | **290 228** |

Instruments payants (pilote A/A et bras d'instrument), au cas attendu : de 956 (Kimi) à 3 490 USD (10 / 50) à l'estimation, et de 22 951 à 58 891 USD au pire.

Le pire est une **borne de construction**. Chaque appel y atteint son plafond, chaque carte et chaque objet de contrôle est testé au pire, les relances et le dépassement de C.8 sont comptés. Ce n'est pas une prévision. La contre-lecture trouvait 236 448 USD sans relances ni C.8 ; avec ces deux postes et l'aiguillage des objets de contrôle, on arrive à 290 228.

## 3. Ce qui reste supposé (et marqué dans la sortie)

- Surcroît d'entrée du bras (a) : 3 200 jetons par appel.
- Messages au pire bornés au plafond du proposeur.
- Deux jeux d'objets de contrôle par course de bras (lecture de C.7).
- Mêmes relances au pire qu'à l'estimation.
- Objets de contrôle aiguillés en nombre égal à l'estimation et au pire.
- Unités de la section D recopiées de la conception. Leur recalcul est cohérent avec ses tableaux, mais il ne prouve que la cohérence, non la provenance.
- Tarifs repris par citation : deux espèces Claude, Kimi, Astra (pièces primaires absentes pour trois d'entre eux) ; Carbon n'a qu'une borne haute.

## 4. Épreuves (`epreuves-devis-v2.json`, toutes tenues)

| épreuve | attendu | rendu |
|---|---|---|
| pièce saine | passe | passe |
| artefact : borne de la première espèce Claude 1,50 → 1,40 | refus | refus |
| artefact : vérificateur au pire 0,10 → 0,12 | refus | refus |
| artefact : fausses et copies 8 → 6 | refus | refus |
| artefact : tour central, sortie 2 000 → 3 000 | refus | refus |
| artefact : 12 → 10 tours dans le commentaire de la borne | refus | refus |
| plafonds de session sains ; artefact aiguilleur 0,25 → 0,30 | passe ; refus | passe ; refus |
| dénominateur 4 × 6 sain ; artefact 6 → 5 cartes | passe ; refus | passe ; refus |
| bornes au pire par test | 1,60 / 0,90 / 3,50 / 3,50 / 2,80 / 2,90 / 2,90 | identiques |
| totaux de la section D recalculés | 0 écart | 0 écart |
