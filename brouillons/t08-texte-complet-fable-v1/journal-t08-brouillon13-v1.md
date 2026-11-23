# Journal du brouillon 13 du texte de la base boîte noire (T0.8) — v1

- **Nature** : pièce de travail (classe C). **Auteur** : session `session_013QMayo5SNVbiUW6hGnPrCo` (modèle B), rédacteur des brouillons 11 à 13.
- **Heures (UTC, `date -u`)** : message de la session mère lu à 19:14 ; brouillon 13 produit vers 19:20 ; journal clos à 19:17, le 2026-11-22.
- **Ce que la session rend** : le brouillon 13 (candidat 4), `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon13.md`. Il remplace le brouillon 12 comme objet de la vérification du contre-lecteur 8. Cinq marqueurs restent.

## 1. Ce qui a déclenché ce brouillon

Lazar a tranché le 22 novembre vers 19:11 UTC la question de la garde d'antériorité du texte et du code sur la course : option (a), la garder dans le code et la déclarer, sans l'écrire dans la liste d'arrêt gelée. La session mère l'a inscrit : `GO-2026-11-22-122`, `registres/go.md`, commit `37a5afed2838b69aad63333a5f79c7443080c6af` de `main`. J'ai relu la ligne sur `main` avant d'écrire ; elle dit ce que dit le message.

## 2. Ce que le brouillon 13 fait (12 opérations, aucune dans une section gelée)

- Section « Gardes de code » : la recommandation devient une décision, citée ; la table des quatre gardes nomme la décision comme source de la quatrième.
- Liste laissée à Lazar : le point 1 est dit tranché.
- Calendrier : la ligne « au plus tard le 25 » ne porte plus de question à Lazar ; il reste à la mère la confirmation des trois autres gardes.
- Table des marqueurs : le marqueur de la ligne du registre recevra R-2657, `GO-2026-11-22-122` et la ligne de confirmation de la mère.
- En-tête (titre, statut, auteurs, date), déclaration de vue, relecture exigée, vérification des marqueurs.

Détail : `couples-t08-brouillon13-v1.json` ; résumé : `differentiel-gel-t08-brouillon13-v1.md`, section 3.

## 3. Programmes

- `faire-t08-brouillon13-v1.py` : même construction que celui du brouillon 12, écrite pour un numéro de brouillon donné ; même contrôle du gel (`controle_gel_t08_v1.py`, inchangé).
- `finaliser-t08-scellement-v3.py` : la version 2, à une différence près — la valeur du marqueur de la ligne du registre cite `GO-2026-11-22-122`. **C'est la version à employer au scellement** ; les versions 1 et 2 restent telles quelles et ne servent plus.
- `essais-controle-gel-t08-v2.py` : les essais de la version 1, sur le brouillon 13 et le programme de scellement en version 3 : 27 conformes sur 27.

## 4. Vérifications

- `--verifier` reproduit le brouillon 13 à l'octet ; contrôle du gel tenu ; phrase T5-19 épinglée.
- Validateur de préenregistrement : seuls les cinq marqueurs restent.
- Suite d'essais du dépôt : toujours non jouable dans ce conteneur ; aucun fichier de `src/` ni de `tests/` n'est touché.

## 5. Écarts et accès

- Lu en plus : la ligne `GO-2026-11-22-122` sur `main`, et le message de la mère. Rien d'autre.
- Le contre-lecteur 8 avait reçu le brouillon 12 à vérifier à 19:13 ; il reçoit le brouillon 13 à sa place, avec la liste des 12 opérations qui les séparent. S'il a déjà vérifié le brouillon 12, il lui reste ce différentiel.
- Aucun refus d'outil. Aucun registre écrit. Aucun résultat lu.
