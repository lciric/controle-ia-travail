# Contre-lecture — masque de style v2, rejeu du juge de sélection — v1

Contre-lecteur, modèle S (neuf : n'a écrit ni le masque v1 ou v2, ni la configuration A, ni les critères). Écrit le 2026-11-20. Python 3.13.18. Processeur seul, aucune dépense, aucun appel de modèle. Aucune carte ouverte, rien sous `archives-reponses-modeles/`, aucune écriture dans le dépôt. Mandat : `mandat-contre-lecteur-masque-v2-v1.md` (`9f6169bb…`, empreinte vérifiée).

## Verdict : Conforme

Aucune correction exigée. Quelques remarques facultatives en fin de pièce.

## Empreintes vérifiées contre leur compagnon (toutes OK)

Mandat contre-lecteur ; mandat développeur (`93bc98d6…`) ; masque v2 (`769aace5b64c697799b76a0120a5c2926c75798a388c93fa00ddc93224401c01`) ; essais v2 (`7c84260f3fabe5ebcf7a9ea8447cf94dd462710755055026a44194282be14b71`) ; différentiel (`efb1c82b…`) ; rapport du développeur (`92c9f0b8…`) ; masque v1 (`07ed87256ba6f2ca510dfd462733190566343ed09e485cb1b638e0314780823e`) et ses essais ; configuration A v2 (`a6c5d87bf73ebcae10ff7cf87390dd4827431ce0480bbf008df755d59b3b7f54`) ; proposition ; lecteur par programme v2 (`de99117b…`). Mes copies de travail du v1 et du v2 ont les mêmes empreintes.

## 1. Différentiel

Refait par `diff -u` sur copies vérifiées : identique à celui du développeur, aux deux lignes d'en-tête près (dates). Rien ne change hors de ce que le mandat permet : docstring et `VERSION`, constante `CLE_RETIREES`, `valider_configuration` (huitième clé), `extraire_contenus` (paramètre facultatif, retrait, garde du compte), `main` (appel, troisième ligne d'en-tête), description de la ligne de commande. Pas de constante d'empreinte de configuration dans le v1, aucune n'est ajoutée : conforme.

## 2. Code, les quatre exigences et les gardes

- Huitième clé : l'ensemble des clés vaut les sept ou les sept plus `cles_hors_champs_retirees` (l. 73) ; toute autre clé neuve reste un refus. Objet non vide, noms textes non vides, aucun nom dans `champs`, ni `meta`, ni `empreinte`, valeurs entiers ≥ 1 hors booléens (l. 80-87) : conforme au mandat.
- Retrait avant le contrôle « clé hors des champs » (l. 124-128) : présence seule par `nom in contenu` ; le nouvel objet est fait des clés non retirées ; aucune valeur retirée lue, copiée, écrite ni affichée ; le `contenu` d'origine n'est pas modifié. Toute autre clé hors champs reste un refus (l. 128-130), champ manquant et champ non texte aussi.
- Garde du nombre (l. 141-145) : refus si un nombre de cartes porteuses diffère de l'attendu ; le message ne porte que le nom, le trouvé et l'attendu (aucun identifiant ni valeur) ; placée après la boucle, rien n'est écrit (la sortie n'est écrite qu'à la fin de `main`). Pas de repli silencieux (R5).
- Compte par clé en troisième ligne d'`en_tete`, avec l'empreinte de la configuration (déjà vérifiée égale au fichier par `lire_json_verifie`) ; aucun identifiant de carte ; clés de sortie inchangées.
- Sans la huitième clé : `retirees` vide, `if retirees:` faux, boucle du v1 intacte ; `en_tete` égal à `EN_TETE`. Conduite égale au v1 aux deux valeurs par nature près (nom de la pièce, empreinte du programme) : je lis la règle « à l'octet » comme le développeur (remarque 1), c'est la seule lecture possible.
- Cas limite vérifié à la lecture : `hors_choix` : une carte non ouverte n'est pas comptée, conforme à la remarque 3.

## 3. Essais rejoués

Sur copies vérifiées dans mon dossier, commande du mandat : `55 passed in 0.18s`. Identique au rapport.

Ce qui manque aux essais (aucun point bloquant) :
- Aucun essai ne pose en même temps un refus de compte et un autre refus (ordre des refus) : sans conséquence, tout refus rend 2 et n'écrit rien.
- Pas d'essai d'un nom retiré non ASCII (tri par octets en UTF-8 de l'en-tête) ni d'un nom retiré qui serait un champ d'une autre configuration : sans conséquence pour la configuration A v2.
- L'espion ne couvre pas `in`/itération des noms (permis par le mandat) : le test affirme justement que seuls les dix champs sont lus ; suffisant.
- Les essais ne lancent pas le lecteur par programme sur la sortie du v2 (lecture seule demandée, point 4).

## 4. Lecteur par programme v2

Il accepte la sortie du masque v2 en forme « masque » : `extraire` ne lit que `donnees["cartes"]` (liste), chaque carte doit avoir exactement les clés `id` et `champs` (c'est la forme que `verifier_sortie` garantit) ; `en_tete`, `rapport`, `empreintes` ne sont pas lus. La troisième ligne d'en-tête est donc ignorée sans refus. Lu seulement, jamais lancé. La réserve 1 de la proposition (forme « fiches » qui lit les trois clés) tient et n'est pas touchée par le masque.

## 5. Les six remarques du § 6 du rapport du développeur

1. « À l'octet » : garder. Le scellement doit écrire la lecture (égalité aux deux valeurs par nature près).
2. Forme de l'en-tête : garder ; vérifié au point 4, le lecteur ne le lit pas.
3. Compte porté sur les cartes ouvertes : garder ; la configuration A v2 a `hors_choix` vide, donc 94 cartes ouvertes.
4. Objet vide refusé : garder.
5. Message du refus de compte (nom, trouvé, attendu) : garder ; ce sont des comptes par clé, jamais par carte. À porter à la mère seulement pour confirmer que la lettre de GO-2026-11-20-28 le couvre (je n'ai pas ce texte en main).
6. Valeurs de tout type non regardées : garder.

## 6. Configuration A v2

Programme `valider_conf_a_v2.py`, écrit dans mon dossier et lancé par son chemin, sur la configuration seule (empreinte vérifiée `a6c5d87b…`) : `valider_configuration` du v2 **passe** ; celle du v1 refuse (« clés attendues champs, formules, hors_choix, intertitres, minimum_formule_recitee, plafond, seuil_formule_recitee »), comme attendu.

## Remarques facultatives (pas des corrections)

- Le message de refus « clés attendues … » liste les sept clés et ne nomme pas la huitième facultative. Le garder identique au v1 est ce que le mandat et les essais exigent ; si un v3 est un jour écrit, le dire.
- Le masque peut encore refuser sur les vraies cartes pour un champ manquant ou non texte (réserve 3 de la proposition) : à dire dans le scellement.
- Commande de jeu du rapport (§ 5) : conforme, l'empreinte entière des fiches reste à fournir par la mère.

Aucun refus de permission, de classifieur ni de garde. Aucune commande de liste, aucun heredoc, aucun code en ligne.

*contre-lecteur, modèle S*
