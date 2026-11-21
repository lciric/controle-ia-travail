# Vérification du programme de vérification de la sortie des mondes, v5 — v1

- Auteur : vérificateur du programme de vérification de la sortie des mondes, modèle S. Écrit le 2026-11-21. Aucun appel, aucune clé, aucune dépense, aucun commit, aucun refus de permission.
- Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/verif-verification-sortie-mondes/` ; copie du livrable : `livrable5/` ; mes pièces : `mes_essais/` (`aires_independantes_v1.py`, `variantes_aire_v1.py`, `reseau_grossier_v1.py`, `variantes-aire/`, `sorties-v5/`).

## 0. Verdict : À corriger (deux corrections de texte au rapport, aucune du programme)

Le contrôle par l'aire suit l'arbitrage, ses aires sont justes, sa convention d'écart type est celle du programme de vérité, ses trois issues se comportent comme dites sur mes essais. Il reste deux corrections de texte, dont une que la mère doit connaître avant de dire la condition (d) remplie : **pour une famille G à grille grossière, le contrôle rendra presque sûrement « non lisible »** (§ 3), et le rapport ne le dit pas assez ; la factice a été changée de façon à ne pas le montrer. Et le rapport nomme le modèle de l'arbitre (§ 6).

## 1. Empreintes et essais

Table `f61642f4…` égale à son compagnon ; programme `23caecc2…`, essais, rapport `9613cd5c…`, fabrique, factices, entrées et comptes rendus, rejeu, différentiels : égaux à la table. L'arbitrage lu sur `origin/main` : `a8f8acfa…`, égal. **346 essais passés** sur ma copie, comme annoncé (2 min 48 s). Je n'ai pas relu les 119 mutations une à une.

## 2. Le contrôle suit-il l'arbitrage ?

Oui, point par point :
- **Lecture retenue** : le décalage est lu en écarts types de la loi honnête de la tranche entière, racine de la variance de `loi_honnete` (`controler_une_famille`, l. 1588 ; `lois` l. 1325 à 1550) : mélange par variance totale, réseau par les atomes, Student `echelle·√(ν/(ν−2))` pour ν > 2, Laplace `echelle·√2`, log-normale, normale, décalage par celle de sa base. Pas de repli sur un paramètre `sigma` ou `echelle`.
- **Diagnostic en unité brute** : calculé pour chaque tranche et chaque nombre, rendu au compte rendu (`aires_unite_brute`).
- **Trois issues** : (a) conforme si les trois aires sont à 0,005 près dans toutes les tranches, avec chaque écart de plus de 0,001 compté et nommé par observation (`O_SABOTEUR_ECART_D_AIRE_AU_DELA_DE_0_001`, chemin et rang de tranche) ; (b) `NC_SABOTEUR_EN_UNITE_BRUTE` pour T05, T07 et la grandeur `puissance`, avec `mot_de_la_mere_requis` vrai ; (c) non lisible, avec raison (« aucune_unite_ne_realise_les_aires », « ecart_type_indefini », « loi_hors_du_controle », « calcul_impossible »), sans repli, saboteur non converti. La sortie reste lisible, code inchangé ; les familles à l'écart sont contrôlées et désignées `a_l_ecart[i]`.
- **Ne lit que la loi et les nombres de l'auteur** : oui (aucune valeur de témoin, aucune issue). Le compte rendu porte des aires et des écarts types calculés sur les lois de l'auteur, y compris pour une famille à l'écart sous son étiquette `a_l_ecart[i]` : à détacher avec ce bloc, comme les lignes de table.
- **Essais de moi, programme sorti sur mes variantes** : la factice saine : dix familles conformes, aucune observation ; la factice d'essai : famille A en (b), les autres conformes ; Student à 2 degrés avec les décalages bruts qui réalisent les trois aires : **(b)** ; la même loi avec 0,1, 0,2 et 0,3 : **(c), « ecart_type_indefini »**.

## 3. Le calcul des aires, refait par une autre méthode

Ma méthode : intégrale ∫ F(x + d) f(x) dx par Simpson sur une **grille uniforme** de 400 000 pas (le programme emploie un changement de variable en sinus hyperbolique) et formes fermées de ma main ; aucun code du programme importé.

| famille de la factice saine | loi | écart type | aires pour les trois décalages | écarts aux aires dites |
|---|---|---|---|---|
| A | normale | 1 | 0,689990 ; 0,799994 ; 0,950002 | −1,0·10⁻⁵ ; −6·10⁻⁶ ; +2·10⁻⁶ |
| B | Laplace | √2 | 0,689998 ; 0,800008 ; 0,949999 | −2·10⁻⁶ ; +8·10⁻⁶ ; −1·10⁻⁶ |
| C | mélange | 1,023474 | 0,690006 ; 0,800010 ; 0,950003 | +6·10⁻⁶ ; +1,0·10⁻⁵ ; +3·10⁻⁶ |

Les écarts sont ceux de l'arrondi des décalages à quatre décimales. **Les trois aires sont justes à 10⁻⁵ près.** Contrôle d'une loi à queue lourde : Student à 2 degrés (cdf et densité fermées), mes décalages bruts 0,9786 ; 1,7606 ; 4,5652 donnent au programme les aires 0,689992 ; 0,8 ; 0,95 (compte rendu) : accord.

**Limite non dite : un réseau grossier ne réalise pas les aires.** Avec mes masses exactes pour une normale réduite arrondie au pas 0,5, l'aire en fonction du décalage ne prend, entre 0,70 et 0,90, que les valeurs 0,7557 et 0,8104 : l'intervalle [0,795 ; 0,805] n'est atteint par aucun décalage. Au pas 0,05, il l'est ; au pas 0,001 aussi. Conséquence : **une famille G dont l'auteur a choisi une grille grossière, ce qui est le sens de « scores à valeurs répétées », sera (c)** quel que soit le soin de l'auteur, et ses témoins à saboteur ne seront pas convertis. Le développeur a, pour la factice, ramené la grille de G de 0,5 à 0,001 : son rapport (§ 2) dit seulement que « un pas fin la rend capable d'approcher les aires dites » ; la remarque n'est pas dans la liste des choses que la lettre ne fixe pas (§ 6), et le rapport ne dit pas que la tolérance de 0,005 est inatteignable pour un pas grossier. Ce n'est pas un défaut du programme (il applique l'arbitrage), mais c'est un fait que la mère doit connaître : soit elle l'accepte, soit elle donne une tolérance propre aux réseaux (par exemple la hauteur maximale d'un palier).

## 4. Convention du programme de vérité, et loi sans variance finie

Réponse lue du développeur du programme de vérité (`ff1aad8b`, `reponse-constructeur-decalage-v1.md`) : l'écart type est celui de la loi écrite sous `loi`, prise entière, mélange compris (variance totale), réseau par les atomes de la loi arrondie ; Student à ν ≤ 2 sous un `decalage` : refus `ecart_type_indefini` (et `moyenne_indefinie` pour un mélange à ν ≤ 1). **Le contrôle suit la même convention** : même formule pour chaque loi (mélange, réseau, Student, Laplace, log-normale), et Student sans variance finie rend un écart type indéfini. Pour une telle loi, l'issue est **(c) quand l'unité brute ne réalise pas non plus les aires, et (b) quand elle les réalise** (mes deux essais ci-dessus), ce qui est ce que dit l'arbitrage ; dans les deux cas aucun décalage n'est envoyé au programme de vérité, qui, lui, refuserait sinon.

## 5. Les trois lois factices changées et le rejeu

- **B en Laplace, K en mélange, grille de G à 0,001** : légitimes comme factices de forme (ces lois ont une aire en forme fermée ou sommable, ce qui permet de fabriquer les décalages par un code indépendant du moteur), mais ils retirent de la factice saine la Student, la log-normale et le réseau grossier : la Student n'y est plus éprouvée par la factice (seulement par les essais du moteur contre des formes fermées, et par mon essai à 2 degrés), et le réseau grossier n'y est plus (§ 3). La factice saine est bien en (a) partout (dix familles) et la factice d'essai en (b) pour la famille A seulement.
- **Rejeu de mes 39 sorties** : résultats identiques à ceux de la v4 aux observations près ; **`O_SABOTEUR_NON_LISIBLE` paraît dans 34 d'entre elles, et c'est attendu** : mes décalages valent 0,1 ; 0,2 ; 0,3, qui ne réalisent pas les aires sous aucune unité ; les 5 autres sont illisibles au point 1 et le contrôle n'est pas joué. Aucune fuite dans les rapports.

## 6. Noms et clés

Aucun préfixe de clé en clair. **Un nom de modèle est présent : « Fable »**, six fois dans le rapport (la cause, le § 0 point 2, les factices, les remarques 1 et 7, et le nom de fichier de l'arbitrage cité en chemin) et une fois dans un commentaire du programme (le chemin du fichier de l'arbitrage). Les chemins cités sont des identifiants de fichier et peuvent rester ; les mentions « Fable, § 2 » du rapport nomment l'auteur de l'arbitrage : à remplacer par « l'arbitre », si la règle « aucun nom de modèle » s'applique au rapport que la mère cite.

## 7. Corrections demandées

- **C1 (rapport)** : ajouter aux remarques du § 6 que, pour un réseau à pas grossier, aucun décalage ne réalise les aires à 0,005 près (exemple : pas 0,5, aires atteintes 0,7557 puis 0,8104 autour de 0,80), donc que la famille G d'un auteur à grille grossière sera (c) ; dire que la factice a été changée pour ne pas montrer ce cas ; renvoyer au mot de la mère sur une tolérance propre aux réseaux.
- **C2 (rapport)** : remplacer « Fable » par « l'arbitre » dans le texte du rapport (hors chemins).

Sans correction du programme : conforme à l'arbitrage et à la convention du programme de vérité. Une version v6 du rapport suffit.

## 8. Réserves

1. Je n'ai pas relu les 119 mutations une à une. 2. La quadrature du programme n'est pas bornée rigoureusement (dit par le développeur) ; mon accord à 10⁻⁵ n'est pas une borne. 3. Student à plus de 2 degrés et log-normale ne sont éprouvées que par les essais du développeur contre des formes fermées (et, pour la Student, par mon cas à 2 degrés).

vérificateur du programme de vérification de la sortie des mondes, modèle S
