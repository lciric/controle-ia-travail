# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v3` (empreinte du module 95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChGrz1BL2vR2izpSLGVnY`
- Heure (UTC) : 2026-11-21T22:36:51Z
- Réglages : effort `high`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/relecture-fable-api-v1/envois/5-prevision-reference-honnete/consigne-relecture-v2.md` — sha256 a93fd166e65956f0089bc47c4de5c4c949f1fb4f6393d747707259861d46e616 (compagnon : vérifié)
  - correction : `docs/notes/relecture-fable-api-v1/envois/5-prevision-reference-honnete/brouillon-1-v2.md` — sha256 ee79275dde5fc4ebb4a7b7b0bc60bb26ad11fdb6900589185339bd74a3255278 (compagnon : vérifié)
  - correction : `docs/notes/relecture-fable-api-v1/envois/5-prevision-reference-honnete/calculs-brouillon-1-v2.py` — sha256 b350d4270db7ab91e5342b8cc3b68a1e471a10b5b1802e1f34f2fb7602b5cb7a (compagnon : vérifié)
  - correction : `docs/notes/relecture-fable-api-v1/envois/5-prevision-reference-honnete/calculs-brouillon-1-v2.txt` — sha256 c6f426299b553366af8341ddfe68a11d4e1815f7fb152b72047c7a1bf39b4733 (compagnon : vérifié)
  - remarques : `docs/notes/relecture-fable-api-v1/envois/5-prevision-reference-honnete/contre-lecture-brouillon-1-opus-v1.md` — sha256 8deb8d3effc7c6ab5f695f8efd1e2546d6b141348bd9c12f392b4004237fc1b2 (compagnon : vérifié)
- Empreinte de l'invite envoyée : 6d215782ac9ab117fd24cbb561a1818a1ae5b11b24b3e489c1ea281a92d1b62d
- Jetons : entrée 66114, sortie 50085 (dont réflexion 45712), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 2.532312 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
**à corriger**

Les douze remarques sont portées et tous les chiffres que j'ai refaits tombent juste, à une exception près. Restent à corriger : deux chiffres de risque de l'étape 0 sous-estimés, des choix de conception faits pour le constat 6 sans être mis au nœud, et quatre points de détail. La divergence du constat 5 est fondée selon ma re-dérivation, mais je suis le même modèle que l'auteur de la version 1 : mon accord ne remplace pas la vérification par le contre-lecteur.

## Remarque par remarque

| constat | portée ? | note |
|---|---|---|
| 1 | oui | Hors pièce ; dit en tête et en fin. |
| 2 | oui | L12 a options et recommandation ; la lecture est citée juste après l'énoncé. L'ajout au § 0 n'était pas demandé ; il est déclaré. |
| 3 | oui | § 0, L13, L5 et table des seuils ; la ligne 133 est citée sans être adoptée. La glose « elle ne fixe aucun dommage visé » est du correcteur ; je ne peux pas la vérifier. |
| 4 | oui | Tirage sans remise, condition écrite, remise permise entre configurations. La table dit « rejoués » sans dire que la contre-lecture écrivait 99,5 % et 3,4 % (correction 4). |
| 5 | en partie | Les deux lectures sont calculées et L3 est marquée « à revoir ». Le rattachement du bloc L à la lecture attestée est refusé, avec sa raison, en gras. |
| 6 | à corriger | Lois, tailles d'effet, configurations et trois erreurs types sont écrits ; la règle de rejeu est au nœud. Deux défauts : corrections 1 à 3. |
| 7 | oui | Chiffré, deux voies au nœud L16. Ce blanc ne porte pas le marqueur (correction 6). |
| 8 | oui | Retiré de L11 et de B3 ; le choix des rangs simples est dit, L17 ouvert. |
| 9 | oui | Table des seuils, L3, L4. |
| 10 | oui | Les trois doses sont définies. La phrase « s fois cette part » est un ajout, juste. |
| 11 | oui | Écrit sous le tableau de déclaration, avec renvoi à L2. |
| 12 a | oui | Tables et convention de tête ; dans la prose, la mention ne tient que par la convention. |
| 12 b | oui | « Seule sa règle l'est » va au-delà de la remarque. |
| 12 c | oui | Non vérifiable ici. |
| 12 d | oui | Bornes justes ; l'extension à ρ₁ est déclarée. |
| 12 e | oui | Le marqueur est posé ; le comportement du validateur n'est pas vérifiable ici. |

**Constat 5, la divergence.** J'ai redérivé le pas 14 et je retrouve les deux formes : (n/(z²W))(K + 2(1 − c + c²))/(K + 2) en lecture principale, et c²(n/(z²W)) × 2/(K + 2) en lecture attestée. La dérive du vivier entre bien dans la lecture principale par les unités honnêtes des flux, et s'annule en lecture attestée. Sous les suppositions écrites, le bloc L est donc celui de la lecture principale.

## Ajouts hors des remarques

- **L18** : nœud neuf, déclaré comme conséquence du constat 4. Le fond est juste (médianes refaites), et le laisser ouvert est la bonne conduite.
- **Arrêt 7** : garde neuve « n_max supérieur à W − m ». Elle est déclarée, mais doit être éprouvée sur cas sain et artefact comme les autres (R5).
- **Étape 0** : la taille d'effet c₁(m) = 0,60, la loi commune, le vivier partagé et la règle « tolérance de la version 1 si elle est plus large » sont des choix du correcteur. Ils sont absents de L15 (correction 2).
- **Pas 14** : la forme est dite « écrite de façon indépendante » dans le fichier interrompu de l'auteur, que le correcteur déclare avoir lu « comme matière » (correction 5).
- **Variante « bruit identique » du bloc R5** et cinq lignes ajoutées aux documents qui font foi : sans effet sur le fond.

## Calculs refaits

- **Blocs A à L** : tous justes.
- **R4** : 99,6 % et 3,3 % ; médianes 0,80 %, 0,52 % et 0,00 %. Justes.
- **R5** : réglage A en entier, réglage B en lecture principale, 53,2 %. Justes.
- **R6** : contrôle de la contre-lecture (0,222 point ; 17,8 % ; 62,4 % ; 22,1 %), compte des 28 contrôles, 7,29 % et 0,177 % comme arithmétique, et les lignes du réglage A reportées dans la table sauf la taille utile. Justes, à une exception près : la part de la dérive du vivier du jumeau faussé vaut 1,32 point, non 1,33 (1,329 est l'erreur type totale à 20 000 configurations).
- **R7, R9, R12 d** et, pour R8, les rangs simples : justes.
- **Non refaits** : l'intégrale du score normal (R8), l'erreur type de la taille utile, les réglages B et C de R6.

Les 7,3 % et 0,18 % sont des minorants sous les suppositions mêmes de la pièce. Le taux du rang n'a pas une loi symétrique entre viviers (le bloc R4 le montre : médiane 0,80 % pour une moyenne de 1 %). Par la forme non linéaire, le seul taux à n_max sort par le haut environ 3 fois sur cent à trois erreurs types et 1,4 fois à quatre, pour chacun des deux objets qui le lisent. Le risque d'ensemble est de l'ordre de 10 % et de 3 %. Ce sont mes calculs à la main, à rejouer dans le programme.

Deux autres conséquences :
- La tolérance du jumeau faussé (0,77 % à 9,2 %) contient le taux d'un jumeau exact.
- À la taille d'effet choisie, c₁(m/4) vaut 0,95 et c₂(m/4) 1,03. L'estimation de c₁(m/4) dépasse 100 % environ une fois sur onze, et la taille utile ne se lit alors plus sur cinq points.

## Nœuds ouverts : recommandation et confiance, sans trancher

- **L12** : (a), lecture déclarée et soumise au directeur ; (b) serait plus propre si l'énoncé doit être cité dehors. Confiance 0,65.
- **L13** : (c). La clause de la lettre ne coûte rien à garder, et sous (a) un écart du jumeau détecté entre m et n_max ne donne que « non concluante ». Confiance 0,55. Aucune valeur recommandée pour la dose visée ; l'objet « organisme au repos » reste inconstructible tant qu'elle manque.
- **L14** : (a), la lecture principale, avec la qualification « attestée » ou « tenue par construction ». Sous (b), le verdict dépendrait d'une attestation obtenue 53 fois sur cent avec un jumeau exact. Confiance 0,6, sous réserve de la vérification de la divergence.
- **L3** : (A) tient si L14 = (a), les chances passant de 91 à 89-90. Confiance 0,55. Sous (b), W/60 ne suffit pas : attester la validité jusqu'à 4m neuf fois sur dix demande environ W ≥ 173 m (mon calcul, même forme que R5).
- **L15** : 20 000 configurations, quatre erreurs types, un seul rejeu rapporté avec le premier. Borner les taux du rang sur le rang centré moyen du vivier, dont la loi est normale, plutôt que par une erreur type linéarisée. Confiance 0,5.
- **L16** : (c), tailles propres et objet rapporté, non éliminatoire. Il sert une lecture hors verdict, et sa tolérance (± 1,62 sur 10,05) sépare peu. Confiance 0,65.
- **L17** : (a), rangs simples. Sous supposition normale ils sont plus efficaces (0,798 contre 0,757) et leur loi nulle est exacte. Confiance 0,75.
- **L18** : (a), avec le taux par configurations rapporté à côté. C'est la forme qui a dimensionné les seuils de 2 % et 3 %. Les croisements à 50 % ne bougent pas au premier ordre, donc ρ et κ ne sont pas touchés. Confiance 0,6.

## Ce qui ne se juge pas sans la version 1

- Que le texte non marqué soit resté mot pour mot celui de la version 1.
- Les tolérances « v1 » du bloc R6, hors les quatre que cite la contre-lecture.
- La formulation d'origine de « Pourquoi W/60 ».
- Hors version 1 : les empreintes, les lignes citées des pièces non jointes, et l'affirmation que rien n'est repris des fichiers interrompus.

## Corrections

1. **Étape 0, phrase « Risque ».** Remplacer « 28 contrôles supposés indépendants » par « 28 contrôles supposés indépendants et normaux », puis ajouter après « (bloc R6). » :
   > Ces deux chiffres sont des minorants : pour les taux du rang, l'erreur type est linéarisée, alors que la loi du taux entre viviers est dissymétrique (médiane 0,80 % pour une moyenne de 1 % à n_max, bloc R4). Par la forme non linéaire, le seul taux à n_max sort par le haut environ 3 fois sur cent à trois erreurs types et 1,4 fois sur cent à quatre, pour chacun des deux objets qui le lisent ; le risque d'ensemble est de l'ordre de 10 % et de 3 % (calcul de la relecture, à rejouer). La borne basse de ces tolérances est négative dès n = m, donc sans effet.

2. **L15.** Remplacer « Recommandation : au concepteur. À fixer par le directeur avant le scellement : pas de défaut. » par :
   > Entrent aussi dans ce nœud, choisis par le correcteur pour porter le constat 6 : la taille d'effet plantée (c₁(m) = 0,60, qui met c₁(m/4) à 0,95 et c₂(m/4) à 1,03, au bord et hors de la plage), la loi commune, le vivier partagé, la règle « tolérance de la version 1 si elle est plus large », et la façon de borner les taux du rang (multiple d'une erreur type linéarisée, ou bornes sur le rang centré moyen du vivier). Les risques ci-dessus sont des minorants (voir l'étape 0). Recommandation : au concepteur. À fixer par le directeur avant le scellement : pas de défaut.

3. **Ligne « jumeau faussé ».** Remplacer « (1,41 point, dont 1,33 de la dérive du vivier) » par :
   > (1,41 point, dont 1,32 de la dérive du vivier ; cette tolérance contient le taux d'un jumeau exact, 1 % : seule la garde sépare alors les deux objets)

4. **Table des remarques, constat 4.** Remplacer « Chiffres de la contre-lecture rejoués (99,6 % et 3,3 %, bloc R4). » par :
   > Chiffres de la contre-lecture rejoués : 99,6 % et 3,3 % (bloc R4), là où elle écrivait 99,5 % et 3,4 %.

5. **Pas 14, dernière phrase.** Remplacer par :
   > La même forme figure dans le fichier interrompu de l'auteur (bloc P1 de sa sortie), que le correcteur a lu comme matière : l'accord des deux formes ne vaut ni dérivation indépendante ni contre-lecture.

6. **Marqueurs manquants.** Ligne « témoins à taux p » : « **statut au point L16** » devient « **statut au point L16, À REMPLIR** ». Paragraphe *Tirages* : « Effet de ce tirage sur le taux réalisé du rang : point L18. » devient « Effet de ce tirage sur le taux réalisé du rang : point L18, À REMPLIR. »
