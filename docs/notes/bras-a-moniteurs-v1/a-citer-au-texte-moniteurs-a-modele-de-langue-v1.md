# Ce que le texte du bras A doit citer pour les deux moniteurs à modèle de langue (cases de 13.1) — v1

Écrit par le développeur habilité côté moniteurs, le 19 novembre 2026, à la demande de la session mère. Pour chaque ligne : la valeur, sa source (chemin et empreinte), et son état. **Aucun interne de moniteur** : ni texte de consigne, ni seuil appris, ni trait. Les valeurs « à fixer » ne sont pas de mon ressort : je dis qui les fixe et ce que le code exige.

## 1. Établi, à citer tel quel

| objet | valeur | source |
|---|---|---|
| juge d'une autre lignée : modèle | `Qwen/Qwen2.5-7B-Instruct` | décision N-053, point 4 |
| juge : révision figée | `a09a35458c702b33eeacc393d103063234e8bc28` | dépôt public du modèle, relevée le 19 novembre 2026 ; rapport `docs/notes/bras-a-moniteurs-v1/verification-tokeniseur-qwen-bras-a-v1.json` (`22073b32a525d933ada658b5361d9e3b0d5b1ca1bccc6f8d87a0b3dfc8c2de34`), contre-lu |
| juge : cas de lecture du score | cas B (chiffre par chiffre, fin « non-chiffre » sans reste) | même rapport |
| juge : gabarit | aucune variable de date ; aucune consigne par défaut quand une consigne système est donnée | même rapport |
| juge : jetons de fin | deux, ceux de la configuration de génération de son dépôt à sa révision : `151645` (fin de tour) et `151643` (fin de texte) | même rapport, clé `jetons_speciaux` ; fichier versé `docs/sources/qwen2.5-7b-instruct-revision-a09a3545-v1/generation_config.json` (`3a8f9087e486054c8a4a08dae2e5a3ba62e23da212b5b8c08bc42cb983c3459f`) |
| juge : précision des poids déclarée par son dépôt | `bfloat16` | fichier versé `…/config.json` (`7463bb0ea78315365e6c6b74de4e73bbcc8359dfb0c5a737584e077d42c0b03c`) |
| moniteur boîte noire par action : modèle et révision | `meta-llama/Llama-3.1-8B-Instruct`, `0e9e39f249a16976918f6564b8830bc894c89659` (révision de l'agent) | GO-2026-11-19-23 ; `prereg/T0.6-organismes-config-7b-v1.json` (`b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527`), clé `agent` |
| moniteur boîte noire : cas de lecture du score | cas A (chaque valeur de 0 à 100 en un jeton) | registre des décisions, R-067 ; rejoué par le code au chargement |
| consigne des deux moniteurs | `docs/sources/invites-2606.08892-v1/derivees/H12-par-action-v1.txt` (`5a30c2b3ce283531a90661df078f3d1d0e179312c9d0cd1328caf63b69023220`), chargée par son empreinte | case « consignes des moniteurs », déjà remplie |
| code des deux moniteurs | `src/controle_ia/organismes_discrets/bras_a_v2_habilite/moniteurs_langue_v2.py` (`2400c1387838a98cd12955111bfac71391d841d61c12ed44b5a86fddacc7d7b6`), commit `158f0c87` | notice `notice-developpeur-habilite-lot-14-v2.md` (`0adb83b9…`) |

## 2. À fixer avant scellement : le code l'exige, sans défaut

**Réglages de la lecture avec raisonnement**, les mêmes pour les deux moniteurs. Cinq paramètres obligatoires de la configuration ; le code refuse une configuration qui en omet un ou en ajoute un.

| paramètre | ce que le code exige | valeur de la course de référence, pour mémoire |
|---|---|---|
| jetons générés au plus | entier ≥ 1 | 400 |
| température | strictement positive | 1,0 |
| règle de la balise absente | « imposer » ou « anomalie » | « imposer » (défaut (b) de la décision DB8-8 du texte gelé) |
| seuil de masse faible | dans [0, 1) | 0,5 |
| taille de lot | entier ≥ 1 | aucune : le texte gelé ne fixe pas de taille de lot pour la lecture d'un moniteur (8 est la taille de lot des épisodes de l'agent, clé `lot` de la configuration de référence) ; la lecture ne dépend pas de la composition du lot (essai) |

Source des valeurs « pour mémoire » : texte gelé de la base boîte noire, `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md` (`7da0c3839a7a714b441b018b3cceb704ec431434498653db1496ca839c38c5b5`), lignes 125 à 127 et 184 ; `prereg/T0.6-organismes-config-7b-v1.json`, clés `max_nouveaux` et `temperature`. Le brouillon du texte neuf dit que les valeurs d'une autre course ne valent pas d'office : c'est à la mère, ou à Lazar, de les fixer. Le compte des jetons se fait dans le tokeniseur de chaque moniteur.

**Réglages du chargement**, fixés par le lanceur, hors du module :

| objet | état | source proposée |
|---|---|---|
| date du gabarit du moniteur boîte noire | à fixer ; recommandé : celle de l'agent, `26 Jul 2024` (variable `date_string`) | `prereg/T0.6-organismes-config-7b-v1.json`, clé `agent.variables_gabarit` |
| noyau d'attention | à fixer ; celui de l'agent : `defaut` | même fichier, clé `noyau_attention` |
| précision des poids des deux moniteurs | à fixer, identique pour les deux, ou différence déclarée | pour le juge, son dépôt déclare `bfloat16` |

## 3. Non relevé : jetons de fin du moniteur boîte noire

**Je ne les ai pas relevés.** Le dépôt du modèle est à accès restreint, et la branche `donnees/tokeniseur-llama-3.1-8b-instruct-v1` du dépôt ne porte que les fichiers du tokeniseur, sans la configuration de génération. Ce que je peux dire sans la lire :
- le tokeniseur versé sur cette branche déclare un jeton de fin de tour (`<|eot_id|>`) ; la configuration de génération du dépôt peut en déclarer d'autres ;
- le harnais du programme a une fonction qui les réunit au chargement (`harnais.modeles.fins_du_modele` : jetons de fin de la configuration de génération et du tokeniseur) ; les courses de l'agent les ont consignés dans leurs sorties, que je n'ouvre pas ;
- le code des moniteurs exige, pour ce moniteur, une liste non vide donnée en clair et refuse un format dont les jetons de fin diffèrent.

**À faire par le lanceur, puis à inscrire en 13.1** : relever la liste par cette fonction à la révision figée, l'écrire dans la configuration scellée, et la citer avec le chemin et l'empreinte de la configuration de génération du dépôt.

## 4. Lecture sans raisonnement (« en une passe »)

Le brouillon du texte la dit « au plus rapportée ». **Le code des deux moniteurs ne la fait pas** : la version 2 ne lit qu'avec raisonnement. Pour le moniteur boîte noire, la lecture en une passe existe ailleurs (`bases.scores_jetons.scores_moniteur`, balise imposée juste après l'invite de réponse). Pour le juge, au cas B, elle n'est pas écrite. Si le texte veut la rapporter, il faut un module de plus et ses réglages (aucun, hors le seuil de masse faible et la taille de lot) ; sinon, la mention « au plus rapportée » peut être lue « non jouée » et le dire.
