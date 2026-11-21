# Vérification du programme des deux essais d'admission du bras A — livraison 8 (fichiers `_v7`) — v1

- **Vérificateur** : Claude Opus 5.5, contre-lecteur des livraisons 1 à 7, le 2026-11-21. Ni auteur de cette livraison, ni du devis.
- **Objet** : le commit `e67ffb731` et sa note `note-programme-essais-admission-bras-a-v7.md`, lue en entier. Les six fichiers `_v7` répondent « OK » à leur compagnon ; les outils de mutation version 3 sont versés.
- **Pièce réelle lue, et elle seule** : le relevé `runs/verification-cle-mistral-bras-a-v1/20261121-204032-verification-mistral-eu/releve-verification-v1.json`, qui répond « OK » à son compagnon. Il porte :
  - la ligne GO-2026-11-21-81, close ;
  - un seul appel, l'appel A, envoyé avec la température ;
  - le code 400 `invalid_request_greedy_sampling` ;
  - la ligne 13 du classement ;
  - une dépense comptée de 0,075988 USD ;
  - aucun envoi coupé.

  Je n'ai lu ni `envois/` ni les réponses brutes. Du registre à `origin/main`, je n'ai lu que les lignes de GO-81 et de GO-86, par une recherche de ligne.
- **Essais** :
  - la commande imposée, deux fois : **215 passés à chaque fois** ;
  - la campagne de mutations version 3 : **401 mutants, 401 tués, 0 erreur, code 0** ;
  - six essais jetables, hors du dépôt (`…/scratchpad/essais_jetables_l8/test_l8_jetable.py`) : tous passent.
- **Interdits tenus** : aucun réseau, aucun `git fetch`, aucune clé, `GO_ID` jamais fixé dans l'environnement. Rien écrit hors ce rapport, rien scellé.

## Verdict

**Engageable pour Mistral**, sous GO-2026-11-21-86, avec la configuration définitive de la note v7, une fois les pièces réelles faites et scellées :
- le constat de Mistral ;
- le fichier des règles ;
- la liste locale des interdits, toujours absente au chemin du gabarit (vérification 7, section 4).

## 1. La température retirée d'avance

- **Appel A sans température, sans appel A′.** Essai `test_appel_a_sans_temperature_sans_a_prime`, sur le faux fournisseur : deux appels envoyés, A puis B. Les deux corps portent exactement `model`, `messages`, `max_tokens`, `reasoning_effort` et `stream`. Il n'y a ni `temperature`, ni `top_p`, ni rien d'autre. Le relevé dit `temperature_envoyee: false`.
- **La file aussi** : `test_file_sans_temperature`, les vingt-quatre corps ont le même jeu de champs.
- **Corps fermé** : la garde 3 refuse un `top_p`, à 1 ou à 1,0, et une `temperature` ajoutée. C'est l'essai du dépôt `test_l8_le_corps_reste_ferme_aucun_top_p`.
- **Température refusée sous un retrait** : la vérification se ferme, nœud de Lazar, sans appel A′. C'est juste.

## 2. Champ absent ou mal formé

**Arrêt, sans envoi.**
- Mon essai `test_champ_absent_en_definitive` : une configuration définitive sans le champ est refusée dès les gardes d'avant le départ (« `temperature_retiree_d_avance` n'est pas inscrit »).
- Les formes mal écrites sont couvertes par l'essai du dépôt `test_l8_artefact_champ_absent_ou_mal_forme_rien_ne_part` : nul, vrai, « oui », objet vide, nœud vide, GO mal formé, clé de plus, GO d'une autre ligne.
- Les treize mutants de la fonction sont tués.

## 3. La ligne neuve après la ligne close

Éprouvé avec le **dossier clos réel recopié** dans un monde d'essai, et le **registre réel** de `origin/main` :
- **Sous GO-86, avec un retrait qui nomme GO-86** : la commande à blanc passe. L'état de la ligne est vierge (dépense comptée 0, trois appels). Aucune lecture de la console n'est due, puisque la ligne close n'a aucun envoi coupé. La garde 8 accepte la ligne GO-86 du registre réel (`test_go86_a_blanc_et_registre_reel`).
- **GO-81 réutilisé** : refusé, « la ligne … est close » (`test_go81_refuse`). C'est la garde C-1, qui lit l'état par GO dans tous les dossiers.
- **GO-86 sous un retrait qui nomme GO-81** : refusé (`test_go86_sous_retrait_de_go81_refuse`).
- **Les gardes qui lisent le dossier clos** :
  - C-1 ne ferme que son identifiant ;
  - la garde 13 ne vise que les files ;
  - le verrou est par fournisseur et rendu à la fin de chaque amorce ;
  - la garde 20 ne bloque pas à tort, la ligne close n'ayant aucun envoi coupé ; l'essai du dépôt montre qu'un envoi coupé de la ligne close bloquerait la ligne neuve.

  Rien ne bloque à tort, rien ne passe.
- **La dépense de 0,075988 USD est bien retirée** : sur un constat de 9,50 USD transcrit avant 20:40Z, le reste compté vaut 9,424012 USD (ligne GO-81 citée), au-dessus du seuil de 8,23.
- **Lecture du rédacteur à porter à la mère** : sous le seuil, la dépense est **dite, non refusée**. C'est acceptable, puisque refuser serait un seuil neuf. La conséquence concrète : avec « au moins 7,87 € » au taux de 1,105, sur un constat antérieur à 20:40Z, il reste 8,18 USD, sous 8,23. La ligne partirait avec un « À DIRE À LAZAR ». **Recommandation** : un constat neuf, transcrit après 20:40:36Z, qui porte le crédit vu après la dépense.

## 4. Campagne de mutations, version 3

Rejouée par la commande versée : règle Google 108, livraison 6 168, livraison 7 77, livraison 8 48. **401 tués sur 401, aucune erreur, code de sortie 0.**

## 5. La configuration définitive de la note v7

**Exacte et acceptée.** Je l'ai remplie à la lettre de la section 4 de la note, avec :
- `temperature_retiree_d_avance` = `{"noeud": "journal OD-329, mot de Lazar « a go »", "go": "GO-2026-11-21-86"}` ;
- `lignes.verification-mistral-eu.go` = GO-86 ;
- un constat de Mistral seul en dollars ;
- le fichier des règles d'essai scellé.

Elle passe toutes les gardes d'avant l'envoi à blanc, et la garde 8 contre le registre réel. Le faux fournisseur n'est pas joignable sous une configuration définitive : c'est la garde 14, et c'est voulu. L'envoi sans température est éprouvé sur une configuration d'essai (section 1).

Deux précisions pour la session :
- la configuration de la **file** porte `inscrit.temperature_envoyee: false`, et `temperature_retiree_d_avance` à `false` ou à l'objet de la vérification retenue ;
- pour la vérification globale, il faut une configuration propre, dont le retrait nomme son propre GO.

**Constat en passant** : `git status` ne montre plus les deux fichiers de m-7. Le mineur est clos, quelle qu'en soit la main.

## 6. Ce que j'ai ouvert

- La note de livraison 8, en entier.
- Le relevé réel nommé, et son compagnon. Les lignes GO-81 et GO-86 du registre à `origin/main`, et le registre entier par programme, dans l'essai de la garde 8, sans affichage.
- Le chef `_v7`, en-têtes de `temperature_retiree_d_avance` et de `depense_de_mistral_depuis_le_constat`. Le gabarit `_v7`, par programme. Les essais `_v7`, par recherche de lignes.
- `git log`, `git status`, `git ls-files` sur `tests/mutations_essais_admission_v3/`, et les empreintes chemin par chemin.
- Lus par programme pendant les essais et la campagne : le lot des entrées nommé par le devis, les consignes et les règles par empreinte, les modules du programme de forme.
- Aucun chemin interdit ouvert, listé ni empreinté.
