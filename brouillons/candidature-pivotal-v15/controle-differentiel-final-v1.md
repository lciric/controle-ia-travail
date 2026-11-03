envoyable après remplacements (couples exacts)

# Contrôle du différentiel final, candidature Pivotal (v1)

- Lecteur neuf, 2 novembre 2026, de 07:18 à 07:26 UTC. Lecture seule : aucun commit, aucun `git fetch`, aucun appel de réseau ni de modèle. Un seul fichier écrit, celui-ci.
- État relu (sha256, 12 premiers caractères) :
  - CV `_v15_` : U `781724a4da32`, C `e96d14b0514d`, I `ffe97adcbc34`, S `e4d6ce546f79` ;
  - générateur `17cbffe652c6`, `variantes.json` `0c2728c445cc` ;
  - formulaire `e7acfed98200`, mémo v3 `3d23c4432bc1` ;
  - Kirchner v11 `103176b78985`, Jang et Feng v11 `dfbcda236d3b`.

## Ce qui bloque, et ce qui est recommandé

- **Bloquant : le paquet désigne encore le CV périmé.**
  - Le § 9 du formulaire nomme `Lazar_Ciric_CV_2026-11-02_v14_universel.pdf`. À la racine, ce fichier est la copie d'avant les corrections : il a la même empreinte que celle relue par la contre-lecture du CV (`547697b7e34c`), avec « stays diffuse » et sans réserve.
  - Le LISEZMOI (lignes 43 et 44) renvoie aussi aux CV `_v14_`.
  - Le zip `candidature-pivotal-v15.zip` (07:18:58 UTC) contient les quatre `_v14_` et **aucun** `_v15_`. Il ne faut pas l'envoyer tel quel : le refaire sous un nom neuf (R12).
  - Couples A et B.
- **Recommandé** :
  - « corrected replay under way » dans le CV, et « a corrected replay is under way, sealed before it runs » dans la lettre à Jang et Feng, disent plus que l'état. À 06:47 UTC (`registres/etat.md`, ligne 2), Lazar avait donné le GO de relance de R1, mais l'addendum est « en partie corrigé, non vérifié, rien de scellé ». La session de dépôt est interrompue, et rien ne part avant qu'elle soit relancée. Couples C et D.
  - Dans la lettre à Jang et Feng, « already shows why per-action monitoring is not enough here » interprète au-delà du verdict. Le verdict classe la dose comme « diffuse » selon le critère préenregistré, avec une réserve. Couple E.

## 1. CV `_v15_` (sortie du générateur actuel)

- **Couples 1 à 6 de la contre-lecture du CV** :
  - 1, 2, 5 et 6 : appliqués à l'identique ;
  - 3 : appliqué sous une forme plus courte, « underestimated power by up to 0.2 » ;
  - 4 : remplacé par le retrait de la phrase (a).
- **(a) Défenses** : conforme. Le verdict de réplication (l. 81-82) donne Δ(mélange, historique) = +0,1123 et +0,1255, « répliquée ». Retirer la phrase sur la défense figée est prudent. Le retrait de « (N = 100 per setting, five variants) » n'était pas annoncé, mais il est sans risque.
- **(b) Essaim** : conforme. HP.4 se trompe de 0,2 sous la sonde des enjeux. Pour HP.5a, la puissance observée est de 0,068 contre 0,032 modélisé, et le sens « sous-estimée » est juste partout (verdict, l. 91, 97 et 257). « up to » couvre donc les deux réfutations.
- **(c) Comparaison** :
  - « sealed before any data » est conforme : la passation de 06:05 (§ 4.2) et la concordance (§ 4) montrent les trois textes scellés.
  - « corrected replay under way » : le rejeu n'a pas commencé (voir plus haut). Couple C, recommandé.
- **(d) Boucle** : conforme. Le rapport de code dit « flèche … fermée dans le code v59 », avec un mode à blanc de deux générations par bras dans le vrai bac à sable (`bwrap`) et des agents scriptés. Le code est poussé (`7fadf96`).
- **Changements non annoncés, tous conformes** :
  - « 27% of sabotage actions » : le préenregistrement de la dose R4 (l. 33) dit « p = 1 : toutes les actions instruites » ;
  - « (preregistered; … ) » : « Meilleur » = rappel le plus haut, fixé d'avance (l. 87).
- **(e) Mise en page** :
  - Les quatre PDF font **deux pages** et finissent par « Spoken: French, English, Serbian ».
  - Bas de la page 2 : 799 pt pour U, C et I, 781 pt pour S, sous une limite de 819 pt.
  - L'en-tête « Geometry » de U et C reste seul en bas de la page 1. Ce défaut était déjà noté et n'est pas bloquant.
  - Je n'ai pas pu comparer le CSS avec l'état contre-lu : le générateur `2eb054e0b9d4` a été réécrit sous le même nom, contre R12.

## 2. Formulaire, § 10, et mémo v3

- Couple 7 : appliqué, dans sa variante claire, « (one reservation, on the controls) ».
- Remplacement 1 : appliqué à l'identique. Le § 9 nomme bien le mémo v3.
- « Under way this week, each to be sealed before it runs: … » : exact, lu comme un engagement.
  - Comparaison : « analyses already sealed » est vrai, et le GO de relance est donné.
  - Attaque de Goodhart : le brouillon 1 est public (`0e3588b`) et contre-lu (`9af524b`, « non scellable en l'état », un brouillon 2 suit). « under counter-reading » est acceptable.
  - Boucle : « code public » est vrai (`7fadf96`).
- Mémo v3 :
  - il reprend le § 10 mot pour mot, aux césures près ; le bloc de titre « Lazar Ciric · 2 November 2026 » est cosmétique ;
  - il fait **une page** A4, et le texte s'arrête à y = 622 pt sur 842.

## 3. Lettres aux mentors, v10 → v11

- **Kirchner** : le différentiel est exact, avec trois changements.
  - Remplacement 5 (« tested the judge on real traces ») et remplacement 3 : appliqués à l'identique.
  - Phrase ajoutée sur l'attaque de Goodhart : conforme au brouillon 1. On y trouve le proposeur avec retour, n ∈ {1, 4, 16}, le témoin sans retour, le nul v8 et l'ancien v7, et « aucune course réelle avant le scellement ». Pas de sur-énoncé.
- **Jang et Feng** :
  - « Last night » : exact.
  - La cause, « (some actions could not be re-tokenised exactly as generated) », est conforme au § 4.2 : découpage non canonique à température 1, et P3 n'a stocké que les textes.
  - « under way, sealed before it runs » : couple D.
  - Phrase sur R4 : les nombres sont conformes au n° 251, point 2 (0,269 ; juges ≤ 0,028 ; réserve sur les contrôles), et « the best of the preregistered » est exact (l. 87). Le cadre interprétatif relève du couple E.

## Couples exacts « remplacer : … / par : … »

**A. `reponses-formulaire-v14.md`, § 9** (bloquant ; une seule occurrence)
- remplacer : `Lazar_Ciric_CV_2026-11-02_v14_universel.pdf`
- par : `Lazar_Ciric_CV_2026-11-02_v15_universel.pdf`

**B. `LISEZMOI-candidature-pivotal-v15.md`, lignes 43 et 44** (bloquant pour le paquet ; deux occurrences)
- remplacer : `Lazar_Ciric_CV_2026-11-02_v14_`
- par : `Lazar_Ciric_CV_2026-11-02_v15_`
- Ensuite, refaire le zip avec les `_v15_`, sans les `_v14_`, sous un nom neuf.

**C. `cv-v14/construire_cv_v14.py`, l. 67** (recommandé ; 26 → 24 caractères, sans risque pour la pagination)
- remplacer : `corrected replay under way`
- par : `corrected replay pending`
- Puis régénérer les quatre PDF sous un nom neuf. Si les CV sont déjà téléversés, laisser tel quel.

**D. `mentors/mentor-6-jang-feng-v11.md`** (recommandé)
- remplacer : `a corrected replay is under way, sealed before it runs.`
- par : `a corrected replay is being prepared, to be sealed before it runs.`

**E. `mentors/mentor-6-jang-feng-v11.md`** (recommandé)
- remplacer : `A weaker-instruction run already shows why per-action monitoring is not enough here:`
- par : `A weaker-instruction run is already diffuse by its preregistered criterion:`
