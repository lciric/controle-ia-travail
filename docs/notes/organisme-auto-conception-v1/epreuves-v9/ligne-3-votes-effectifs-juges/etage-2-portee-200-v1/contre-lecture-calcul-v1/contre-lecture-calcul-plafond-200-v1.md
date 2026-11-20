# Contre-lecture du calcul versionné des conditions du plafond de l'étage 2 à 200 témoins (ligne 3) — v1

Contre-lecteur, modèle S, neuf : je n'ai écrit ni le texte de la ligne 3, ni ses additifs, ni le devis, ni ce calcul. Pièce de travail (classe C) sur le mandat `mandat-contre-lecteur-calcul-plafond-200-v1.md` (empreinte contrôlée égale à son compagnon, `b9fa16db…`). Aucun appel payant, aucune écriture dans le dépôt.

## Verdict : Conforme

Le calcul rejoue à l'octet, ses 19 essais passent, et l'issue du pire cas à 200 est retrouvée par un programme à moi, sans emprunt au sien. Une correction de texte par erratum (sans effet sur un chiffre) et deux points à porter à la mère ; rien qui change la sortie.

## 1. Empreintes, rejeu, essais

- Compagnons égaux à leur empreinte : mandat du développeur (`10f22d1c…`), programme (`4814f314…`), sortie (`20ade9a3…`), essais (`2ebe71fd…`), rapport (`74fbafaa…`). Python 3.13.18.
- Rejeu deux fois (`env -C /home/user/controle-ia-travail python3 -I -B CHEMIN > FICHIER`) : les deux sorties valent `20ade9a3feae5b6c5dea3be61808dc71a656d81291857a13facd950baca44fc0`, égales entre elles et à la sortie du développeur, à l'octet.
- Essais rejoués sur une copie (programme et essais copiés dans mon dossier, `.venv/bin/python -B -m pytest -q -p no:cacheprovider`) : **19 passés** (2,69 s). Remarque : le fichier d'essais lit le devis v7 dans le bloc-notes du développeur (par empreinte, `382ea448…`) ; il a tourné parce que cette copie existe encore. Les essais ne se rejouent pas sans elle ; à noter au scellement.

## 2. Lecture du code

- **Fidélité au texte et au devis.** Règle de l. 382 : « aucun envoi ne part si le cumul compté plus cet engagement dépasse » ; le code laisse partir si `cumul + 0,60 <= plafond`, donc « dépasse » au sens strict (un envoi qui porte exactement à 88,36 part). Réserve et coût compté d'un envoi refusé : 60 centimes, jamais zéro (l. 193, 386). Plan P (2 témoins, 2 juges), A (200 × 2), B (Opus 1, Argon 2 par témoin, la moitié « lecture » d'abord, entrelacé par témoin : l. 268 à 271 relues sur le texte scellé) : conforme. Verdict de rang 1 si moins de 40 témoins complets dans la moitié « lecture » ou coupure avant la fin du bloc A : conforme à l. 337, 384 et 388 (voir point 2 des remarques).
- **Exactitude.** Entrées lues par empreinte (arrêt si elle diffère) ; `Decimal` du JSON converti en `Fraction` exacte ; plafond et réserve en centimes entiers, `centimes()` refuse flottant, booléen et `Decimal` ; `exacte()` refuse le flottant ; aucune comparaison de seuil par flottant ; sortie sans flottant (garde `verifier_sans_flottant`) ; arrondi au demi pair sur la fraction. Rien trouvé à reprendre.
- **Formule du devis.** `temoins_b_complets` : reste du disponible (plafond moins 0,60), moins les refus comptés, moins le coût de la plomberie et du bloc A, divisé par le coût du bloc B par témoin, plancher entier : prudente, comme le v3. Les deux lectures divergent seulement d'un envoi (le dernier du groupe) ; l'écart documenté (4,4045 contre 4,4102 au bloc A) est juste.
- **Contrôle à 100.** 83 clés recalculées et comparées en décimal exact à la sortie v3 ; arrêt à tout écart ; l'essai de garde fausse une clé (19 au lieu de 18) et voit exactement cette clé. Les chiffres du devis v7 sont retrouvés dans son texte scellé (essai à dix-sept fragments), dont « 18 témoins » et « non concluant par manque de témoins ». L'arrondi intermédiaire du v3 (plomberie, bloc A et totaux au cas haut lus à quatre décimales) est reproduit pour le contrôle seulement, déclaré, et les chiffres à 200 sont tout exacts : bien posé.
- **Gardes.** Un cas sain et un artefact pour chacune : empreinte, centimes, grandeur exacte, sortie sans flottant, coût relevé au-dessus de 0,60 (arrêt après le premier envoi), refus jamais compté zéro, frontière de facteur de part et d'autre, plan impair ou nul, aucun argument.

## 3. Pire cas refait indépendamment

Programme à moi : `refait_pire_cas_200.py` (listes de coûts, aucune importation du sien ; tarifs lus dans le manifeste de la course v9 ; sortie `sortie-refait-pire-cas-200.txt`). Facteur du pire 3431597/1739000 ; plan de 1 004 envois.

| grandeur | mon calcul | rapport |
|---|---|---|
| total du plan au pire | 88,3617 USD | 88,3617 |
| envois partis | 996 sur 1 004 | 996 |
| coupure | bloc B, témoin 198 (1-base), rendu 2 du juge Argon refusé par la règle | idem |
| dernier envoi parti | rendu 2 du juge Opus, témoin 198 ; cumul avant lui 87,6260 | idem |
| cumul compté à l'arrêt | 87,7701 USD (reste 0,5899 sous 88,36, moins que 0,60) | 87,7701 |
| complets | bloc A 200 ; bloc B 197, dont 100 de la moitié « lecture » | idem |
| refus, moitié « lecture » entière | jusqu'à 39 (39 : 102 témoins complets ; 40 : 99 dont 99 en lecture) | 39 |
| refus, au moins 40 témoins complets en lecture | jusqu'à 64 (64 : 41 ; 65 : 38) | 64 |
| refus, plomberie et bloc A complets | jusqu'à 80 | 80 |

Tout égal. Les frontières 88,91 / 88,92 (le pire passe entier à 88,92) tiennent à la main : 88,36167 − 0,05057 + 0,60 = 88,9111.

## 4. Les remarques du rapport

1. **Ordre des envois du bloc A : garder.** Le texte (l. 270, 268) ne dit pas « par témoin » ou « juge par juge ». Dans toute lecture où le juge Argon est le dernier envoi du bloc, le cumul avant le dernier envoi est le même : la frontière du bloc A ne bouge pas. Elle ne bougerait que si Argon passait avant Opus pour le dernier témoin. À porter à la mère comme hypothèse dite, pas comme erreur.
2. **Rendu isolé du témoin 198 : garder** (déposé, hors des témoins complets ; l. 388 : « lus sur les seuls témoins complets »). **À porter à la mère** : le calcul rend « coupe sans manque » (pas de rang 1) au pire cas ; la lettre de l. 337 écrit « dont le cas où le compteur d'arrêt a coupé le bloc B » sans seuil, ce que l. 388 précise (« s'il y en a au moins 40 dans la moitié "lecture" ; sinon … non concluant »). Le développeur lit l. 337 par l. 388 ; c'est la bonne lecture, mais l'additif 3 (§ 4.2, ligne l. 337) cite l. 337 sans cette clause. Au scellement de l'additif de code, citer l. 388, pas l. 337 seule.
3. **Plafond 88,36 sous le pire 88,3617 : garder, à porter à la mère** (décision de Lazar : GO-2026-11-20-26). Fait exact et vérifié : le plafond est sous le pire du devis, et la réserve fait couper huit envois avant la fin ; sans effet sur le rang (100 témoins de « lecture » complets).
4. **Coût moyen par appel : garder.** Hypothèse de modèle dite ; seule la règle du compteur est une garantie, l'issue écrite est une prévision.
5. **Double échec non modélisé : garder.** Dit au rapport ; les seuils de refus valent pour la forme « refus puis rejeu réussi ».
6. **Arrondi à quatre décimales du v3 : garder.** Reproduit pour le seul contrôle à 100, déclaré, sans effet à 200.
7. Remarques 7 (« dépasse » strict) et 8 (facteur du pire repris du devis) : gardées.

## 5. Correction (erratum, texte seulement)

**Lieu :** `calcul_conditions_plafond_200_ligne_3_v1.py`, docstring, lignes 40 à 42 (hypothèse « un envoi refusé (refusé, coupé par un délai, en erreur, sans coût lisible, engagement sans règlement) est compté 0,60 USD puis rejoué une fois »), et le texte `regle_du_compteur.texte` de la sortie (« rejeu unique »).

**Écart :** le texte scellé, l. 193, dit : « Un envoi refusé est rejoué une fois au plus ; un envoi revenu sans coût lisible n'est pas rejoué. » La description du modèle range le « sans coût lisible » parmi les envois rejoués. Aucun chiffre n'en dépend : le modèle ne joue que « refus puis rejeu réussi », et un « sans coût lisible » non rejoué coûterait moins (0,60 USD sans rejeu), ce qui ne ferait que desserrer les seuils de refus.

**Texte exact proposé :** « un envoi refusé (refusé, coupé par un délai, en erreur) est compté 0,60 USD puis rejoué une fois, avec succès, à son coût ; un envoi revenu sans coût lisible est compté 0,60 USD et n'est pas rejoué (texte l. 193) ; le modèle des refus ne joue que la première forme ». En erratum de classe B, la sortie changerait (le texte est dans le JSON) : le rejeu et l'empreinte se refont, les 19 essais n'y touchent pas.

Je ne l'ai pas exigé comme blocage : la lettre scellée est claire, le code n'est pas faux, sa description l'est à moitié.

## 6. Ce que j'ai fait

`sha256sum -c` de dix compagnons ; deux rejeux ; essais sur copie ; trois relectures de fichiers scellés par chemin (`git show origin/main:…` redirigé : texte v7 et additif 3 v3, dans mon dossier) ; un programme à moi, joué une fois. Aucun refus de permission, de classifieur ou de garde. Aucune écriture dans le dépôt.

Contre-lecteur, modèle S.
