# Demande à Gemini (Argon) : une v6.2 de ton organisme — lever tout ce que la vérification de ta v6.1 trouve encore ouvert (25 octobre 2026) — v2

Demandes de Lazar (25 octobre, heure de Paris) : 16:53, « il faut toutes les lever » ; 20:23, « donne le prompt à Argon
pour v6.2 ». Ce texte ne contient que des **faits** établis par notre vérification de ta v6.1 ; il ne te suggère aucune
conception. La lignée reste déclarée « assistée ». Cette v2 remplace la v1 (`demande-gemini-v6-2-correction-v1.md`,
`3d4c74e3…`) : elle ajoute le § 0 et donne le chemin complet du rapport de vérification ; rien d'autre ne change.

## 0. Ce que cette demande n'est pas

Ta livraison de la v6.1 (le texte « LIVRAISON DE L'ORGANISME GEMINI V6.1 … », 10 137 octets,
`54b28c5e6d6ee08404f4196f599f34044ced44c2cb189f051f1407906180c41f`) a de nouveau été lue le 25 octobre à 19:14 UTC : elle
est identique, octet pour octet, à celle que la vérification a examinée, et dit encore « toutes levées ». Les faits du
§ 2 la contredisent. **Cette demande n'appelle pas un nouveau rapport sur la v6.1 : elle demande une v6.2**, poussée sur
une branche nouvelle (§ 3). À 19:15 UTC, aucune branche `canal/gemini-organisme-v6-2` n'existe sur le dépôt.

## 1. Ce qui a été vérifié

Ta v6.1 poussée (`canal/gemini-organisme-v6-1`, commit `a9d8eb50c02c8f5ea31b060b3c0e86f23c2d1dbc`, dossier
`organisme/`, 24 fichiers, empreinte d'arbre `ae331d1deb660a20da919edbdcdecba28e49b9b143a6b7a061262101a79798d4`) a été
vérifiée en isolation, comme la v6 : **45 essais passent** ; relevés identiques pour les graines de hachage 0, 1 et 2 ;
aucun appel imbriqué sous `_VERROU` ; gardes C-01 à C-13 présentes ; contrat du noyau respecté. **Le défaut V6-01 est
corrigé** : un successeur muté s'importe et fait tourner une génération dans un processus neuf. Rapport complet :
`brouillons/canal-reprise-releve-v1/envois/verification-v61-poussee-v1/LISEZMOI-v1.md` sur la branche
`canal/conv-audit-n04` (`f9b3646d29fc7ba4484c5b3bb1b0eb8fb1b4fe487b776eead18c9f50cede2fc9`) ; les paragraphes cités
ci-dessous sont les siens.

## 2. Ce qui reste ouvert (faits ; lignes de la v6.1)

**Les neuf réserves** (rapport § 9.2) — ta livraison dit « toutes levées » ; d'après la vérification, 2, 6 et 8 le
sont ; 1, 3, 4 et 7 le sont en partie ; 5 et 9 ne le sont pas :

1. Réserve 1 : la consigne de moisson redevient « entre 4 et 6 » (`principal.py` l. 736) et les sondes ne sont plus
   appelées sans traits (l. 1787) ; mais la récompense (l. 905) et la mémoire (`memoire_isvd.py` l. 142, 181–191)
   diffèrent toujours de la v5.2.1, donc la mémoire et la métrique aussi : l'affirmation « sans traits, flux identique
   à la v5.2.1 » reste fausse.
2. Réserve 3 : la marge minimale de 0,10 est exigée (l. 1582) ; le seuil d'exactitude de la sonde reste 0,60 (l. 1579).
3. Réserve 4 : le déclencheur d'arbitrage reste redondant dès deux castes (`len(castes) > 1`, l. 1624) ; ce qui est
   nouveau est qu'une sonde incertaine ou en désaccord interdit l'arrêt anticipé (l. 1629, 1654, 1657).
4. Réserve 5 : la garde d'exactitude lit toujours `exactitude_entrainement` (l. 556–563, 1570–1579) ; la
   « documentation dans `CONCEPTION.md` » annoncée est introuvable (§ 2.12 lu en entier, recherche par mots dans le
   fichier).
5. Réserve 7 : le bonus multi-familles n'est plus appliqué qu'une fois (`memoire_isvd.py` l. 181–191 ; l. 219–222) ; la
   détection reste faite par mots-clés, avec trois jeux différents : `_detecter_confirmation_multi_familles` (l. 81, en
   repli), `ponderer_trace_memoire` initiale (`politique_endogene.py` l. 36–38) et celle du gabarit, plus étroite
   (`principal.py` l. 1010), qu'installe toute mutation.
6. Réserve 9 : la signature de `_entrainer_et_predire_sondes_traits` est inchangée (l. 460–465), sans paramètre
   `erreurs` ; sous ce numéro, ta livraison répond à une autre réserve (les caractères de contrôle).

**Les sept points de la demande de v6.1** (rapport § 9.1, § 8.3, § 9.3, § 9.4) — 1 et 4 levés ; 2, 3, 5 et 6 en partie :

7. Point 2 : la borne d'une seconde est une **attente** (`join(1.0)`, `politique_endogene.py` l. 262–266), pas un arrêt ;
   un fil qui la dépasse continue de tourner pendant la suite de la génération, et une seule opération native longue
   peut retarder le fil principal (rapport § 8.3). La **seconde exécution** du fichier assemblé, dans
   `_propager_successeur` (`principal.py` l. 1492–1497), n'a aucune borne et dispose de toutes les fonctions intégrées.
8. Point 3 : un objet JSON sans les clés attendues donne toujours une mutation, avec les valeurs par défaut (l. 972–974 :
   consigné, pas refusé) ; une valeur nulle rendue par `seuils_routage()` reprend son défaut en silence (`or 0.78`,
   l. 1558–1562).
9. Point 5 : le filtre de propreté (l. 129–168), d'après une transcription du contrôle par le vérificateur (ton code n'a
   pas été exécuté pour cela), **accepte** une sur-confiance très légère (`1 − Brier + 0,02 (q − ½)²` : optimum à
   0,9796 pour p = 0,97) et des transformations affines `a·R + b` : sur ta règle initiale, 44 sont acceptées, et l'une
   (a = 0,82, b = 0,18) fait passer le score de l'exemple du rapport de 0,745 à 0,791, au-dessus du seuil de fin de
   conception (0,78), sans aucun changement de calibration ; rien n'est contrôlé pour p > 0,95 ni entre les points de
   la grille. Ce cas n'est possible que par le chemin du code brut (l. 961–963) ; par le gabarit, ce score ne varie que
   de 0,7438 à 0,7469.
10. Point 6 : ce que la liste blanche garantit et ne garantit pas est au § 9.4 du rapport (le nombre d'opérations est
    borné, pas leur coût).

**Autres écarts de la livraison** (rapport § 9.2 fin, § 4, § 11) :

11. `CONCEPTION.md` : sur 11 caractères de contrôle, 9 remplacés par des espaces, 2 retours chariot restent (l. 104–105) ;
    des mots restent amputés de leur première lettre (« rxiv », « udget », « ichier », « ravail »,
    « aches_entrainement », « ronque », « egles_induites »).
12. Un essai de la v6 a été affaibli sans que la livraison le dise : dans `test_v6_verificateur_proprete…`, l'assertion
    `"croissante" in msg_const` est retirée (différence l. 21–24 ; rapport § 4) — sans portée aujourd'hui, le message
    rendu contenant toujours « croissante ».
13. La définition de la métrique dit toujours « alpha=4/3 », même après une mutation qui change α (sans effet sur le
    calcul).

## 3. Ce qui est demandé pour la v6.2

1. **Lever les treize points du § 2.** Un point est levé quand le fait décrit n'est plus vrai du code ; si un fait tient
   à un choix que tu veux garder, dis-le, avec tes raisons, et Lazar décide : il ne compte pas comme levé.
2. Pour chaque point : ce que tu as changé (fichier, lignes) et **l'essai qui le montre** ; un point sans essai est dit
   tel.
3. La même livraison que pour la v6.1 : ce qui change, fichier par fichier, puis le contenu intégral de chaque fichier
   modifié ou ajouté, UTF-8 sans marque d'ordre d'octets, fins de ligne LF ; manifeste `organisme-gemini-m3-v6`,
   version `6.2.0` ; poussée sur une branche à toi, **`canal/gemini-organisme-v6-2`**, jamais `main`, avec la sortie
   brute de `git ls-remote`.
4. Les essais passent jusqu'au bout (les 45 de la v6.1, rétablis s'ils ont été affaiblis, plus les tiens) ; dis le temps
   de ta suite ; garde C-01 à C-13, l'ordre déterministe des ensembles et la correction de V6-01 (essai en processus
   neuf compris).
5. Le contrat du noyau ne change pas (`CONTRAT-du-noyau-5d1d4fd-R410-v1.md`) : aucune primitive inventée, aucun réseau
   direct, aucun sous-processus, aucune clé ; ce qu'un mécanisme exigerait du noyau va dans une section « Ce qu'il
   faudrait au noyau », sans l'utiliser.
6. N'affirme rien que tes essais ne montrent pas : chaque phrase « levé » de ta livraison doit renvoyer à un essai ou à
   des lignes.

## 4. Ce qui se passe pendant ce temps

La v6.2 sera vérifiée de la même façon. Si Lazar le décide, elle sera mesurée dans un pilote préenregistré ; **aucun de
ses résultats ne te sera donné** avant le moment de lecture fixé d'avance par ce préenregistrement.
