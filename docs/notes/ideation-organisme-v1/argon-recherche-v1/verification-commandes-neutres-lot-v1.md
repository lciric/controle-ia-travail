# Vérification des corrections : la commande Gemini par lot v1 et le relais Gemini v4 — v1

Contre-lecteur neuf (R2). Je n'ai écrit aucune des pièces lues, ni la contre-lecture qui les a demandées. Date : 18 novembre 2026.
Aucun appel réseau vers un fournisseur. Aucun port de 8787 à 8792 touché : tous les essais et toutes les sondes ont tourné sur des
ports libres de la boucle locale, devant de faux amonts. Tout a tourné avec `PYTHONDONTWRITEBYTECODE=1`, `python -B` et
`-p no:cacheprovider` (interpréteur du `.venv` du dépôt). Aucun dossier `__pycache__` neuf, ni dans ce dépôt ni dans le clone de
l'orchestrateur (inventaire avant et après identique). Vérification courte : je n'ai relu que ce que les constats bloquant et
significatifs de la contre-lecture visaient.

## Verdicts

| Pièce | Verdict |
|---|---|
| La commande Gemini par lot v1 (`commande_gemini_lot_v1.py`) et ses essais | **autorisable** : le constat bloquant et les trois significatifs sont corrigés ; il reste des mineurs |
| Le relais Gemini v4 (`relais_gemini_v4.py`) et ses essais | **à corriger** : un constat significatif neuf, étroit et bon marché (V-1) ; les trois significatifs de la contre-lecture sont corrigés |

## Pièces lues (sha256 relevées pendant la lecture)

| Fichier (dossier `argon-recherche-v1/`) | Empreinte |
|---|---|
| `contre-lecture-commandes-neutres-lot-et-astra-v1.md` (conforme à son `.sha256`) | `9887e9e1d7baab53446001f955a1201923556b15b6b81297090748181909da9c` |
| `commande_gemini_lot_v1.py` (non scellé) | `e57d4011f0319063e16dce9cc6e5d626ed2c609f9e5b3e385e599f0e7b92846d` |
| `relais_gemini_v4.py` (non scellé) | `60dc814ee9d267c3fe229b919e61bf1354576fcf13c4b0b683b435f2dd68affc` |
| `test_commande_gemini_lot_v1.py` (non scellé) | `4118bb722d4857ffaf22af6a290addab92c4efc25c696ce1519572f9e6145461` |
| `test_relais_gemini_v4_suite_v2.py` (non scellé) | `40f92629c9c2a5795121ef5d8039bd6028dd935591f3643e492f67592598034d` |
| `commande_argon_v3e.py`, l. 255-330 (référence du code 7 et de l'avertissement d'entrée) | lu tel quel |
| `organismes-discrets-v1/organisme-ideation-v1/epreuve-lot-carbon-v1/resultat-lot.json` | conforme à son `.sha256` |
| Orchestrateur `pole/adaptateurs.py` l. 622, `pole/adaptateur_commande_v67.py` (garde 24) | commit `a41b7b50…`, arbre propre |

## Ce qui a tourné

1. **Les essais de la commande par lot** (`test_commande_gemini_lot_v1.py`) : **29 réussis**, aucun échec.
2. **La suite du relais v2 rejouée contre le v4** (`test_relais_gemini_v4_suite_v2.py`) : **49 réussis**, aucun échec. Le
   différentiel avec `test_relais_gemini_v2.py` passé par la même substitution ne touche que le texte : une docstring d'en-tête
   ajoutée, et une ligne de l'ancienne docstring qui dit encore « relais-gemini-v2 » (mineur, M-6). Le code est identique.
3. **Mes sondes** (dossier de travail temporaire, hors dépôt), devant le faux amont des essais et le vrai relais v4 en
   processus : contenu d'un lot par des formes détournées, ligne du code 7, relevés refusés par la borne, relevés en 403,
   annulation à `Content-Length` non entier. Résultats ci-dessous.

## La commande Gemini par lot v1 — autorisable

### Constats de la contre-lecture, un par un

- **C-1 (bloquant) — corrigé.** Après un lot réussi, l'usage est lu **avant** la lecture de la réponse (l. 208-220) : une pensée
  au-delà de la provision rend le **code 7**, texte vide, coût réel compté sur l'usage, et le code 7 prime sur le code 5. Le coût
  rendu est le plus grand du coût réel et du pire cas réservé (l. 240), ce qui est prudent. Une entrée facturée au-delà de
  l'entrée gardée est rendue en avertissement (l. 215-217), comme dans la commande d'Argon v3e (l. 329 de son en-tête :
  « sinon avertissement au journal »). Essais : `test_pensee_au_dela_de_la_provision_code_7_cout_reel` (coût exact),
  `test_pensee_prime_sur_la_troncature`, `test_entree_facturee_au_dela_avertie`. Sonde : code 7, `cout_origine` = `usage`,
  1,6627 USD pour 40 000 jetons de pensée.
- **C-2 (significatif) — corrigé.** L'issue de l'annulation est dite dans la ligne : « annulation acceptée », ou « ANNULATION EN
  ÉCHEC (motif) : le lot peut tourner encore » (l. 190-196). Les relevés en erreur sont comptés (`releves_manques`) et rendus
  dans la ligne, en succès comme en échec. Essais : `test_delai_annule_le_lot` et `test_annulation_en_echec_dite` (relais à
  `--max-annulations 0` : l'amont ne reçoit rien, la ligne le dit). Sondes : relevés refusés par `--max-releves 2` → 3 comptés,
  annulation acceptée par sa borne propre ; relevés en 403 (lot inconnu d'un relais redémarré) → 50 comptés, annulation en échec
  dite. La proposition « s'arrêter tôt sur un 403 » n'est pas reprise : voir M-2.
- **C-3 (significatif) — corrigé.** Délai par défaut 1 500 s. La durée la plus longue est `--delai-s` + `--intervalle-s` + 2 ×
  `--delai-requete-s` = 1 770 s, sous les 1 800 s de l'adaptateur (`pole/adaptateurs.py` l. 622). Je confirme ce calcul : le
  temps du comptage et de la création est pris dans `--delai-s`, car l'horloge part avant eux (l. 139) ; le pire chemin est un
  contrôle juste sous le délai, puis une attente, un relevé et une annulation, chacun au plus un délai de requête. Le compte de la
  contre-lecture (4 délais de requête) était plus prudent que nécessaire. La condition est écrite dans l'en-tête (l. 39-42) et
  dans l'aide de `--delai-s`. L'option `--delai-commande-s` qu'elle nomme existe bien (lanceurs de l'organisme, par exemple
  `orchestrateur-v52b/demonstrations/ideation_v2.py` l. 616). Réserve mineure M-3 sur la garde 24 de l'orchestrateur v67.
- **C-4 (significatif) — corrigé.** Les essais demandés existent et passent :
  - forme réelle versée : `test_lecture_de_la_forme_reelle_versee` lit `resultat-lot.json` (scellé, conforme), texte, `STOP`,
    `gemini-4-carbon`, 844 jetons de pensée, et l'usage lu par la garde après coup est le même ;
  - pensée au-delà de la provision, et sa priorité sur la troncature (deux essais) ;
  - annulation en échec (`test_annulation_en_echec_dite`) ;
  - pire cas à l'égalité : `test_pire_cas_egal_et_sous_le_plafond` recalcule le pire cas et vérifie l'égalité et `≤ 1,5`.
    Le cas joué est au bord du plafond (sortie 27 931 jetons, sous la sortie maximale) : il éprouve bien la garde ;
  - nom du lot en métadonnées seulement (`test_nom_du_lot_en_metadonnees_seulement`).

### Constats restants (tous mineurs)

- **M-1 — la ligne du code 7 ne porte ni l'avertissement d'entrée ni le modèle servi** (l. 229-241). Sonde : code 7 avec une
  entrée facturée au-delà de la gardée → ni `avertissements`, ni `modele_servi` dans la ligne. Sans effet sur l'argent (coût réel
  compté, échec). Mais si le modèle servi est autre et que la pensée dépasse, la ligne ne dit pas le modèle. Correction : porter
  `avertissements` dans toute ligne, et `modele_servi` dans la ligne du code 7 quand il est connu.
- **M-2 — un relevé en 403 ne fait pas arrêter tôt** (l. 198-202). La commande attend jusqu'au délai (1 500 s), puis l'annulation
  échoue et la ligne le dit. C'est borné et dit, donc pas un repli silencieux ; c'est seulement du temps perdu.
- **M-3 — garde 24 de l'orchestrateur v67** (`adaptateur_commande_v67.py`) : elle n'exige que 30 s entre le délai de la commande
  et celui de l'adaptateur. Cette commande peut déborder son `--delai-s` de 270 s (réglages par défaut). Sous la garde 24, c'est
  donc la condition de l'en-tête de la commande qui tient, pas la garde. À rappeler dans toute configuration qui l'emploie.
- **M-4 — pas d'essai sur le compte des relevés manqués**, ni sur la lecture par la seule copie `metadata.output` de la forme réelle.
  Mes sondes montrent que les deux marchent.
- **M-5 — mineurs de la contre-lecture non repris** : C-5 (adresse non restreinte à la boucle locale ; port par défaut 8792
  contre 8788 pour le relais), C-6 (`--facteur-lot` supérieur à 1 accepté), C-7, C-8, C-9, C-10. Ils restent mineurs.

## Le relais Gemini v4 — à corriger

### Constats de la contre-lecture, un par un

- **R-1 (significatif) — corrigé.** L'annulation a sa propre borne `--max-annulations` (défaut 16), séparée des relevés
  (l. 228-244). Essai `test_relais_annulation_possible_releves_epuises` : avec `--max-releves 0`, le relevé reçoit 429 et
  l'annulation passe (200, reçue par l'amont). Ce qui manque encore : l'en-tête ne dit pas que les lots retenus vivent en mémoire
  et ne survivent pas à un redémarrage (mineur, M-7).
- **R-2 (significatif) — corrigé pour un client honnête, mais contournable : voir V-1.** `motif_contenu_lot` (l. 297-317) refuse
  sans envoi un lot de plus de `--max-requetes-par-lot` requêtes, une requête dont `model` nomme un autre modèle, et une requête
  qui déclare `tools`, `toolConfig` ou `tool_config`. Essai paramétré `test_relais_borne_le_contenu_d_un_lot` (2 requêtes, autre
  modèle, outils, corps illisible : 403, rien envoyé). La taille du corps est vérifiée avant sa lecture (l. 470) : essai
  `test_relais_corps_trop_gros_refuse_sans_lecture` (429, rien envoyé).
- **R-3 (significatif) — corrigé.** Les gardes neuves sont essayées :
  - annulation étrangère : `test_relais_annulation_etrangere_refusee` (403, rien envoyé) ;
  - relevés épuisés : voir R-1 ;
  - masquage de la clé dans un relevé, dans le corps relayé et au journal : `test_relais_masque_la_cle_dans_un_releve` ;
  - nom en métadonnées seulement : essai de la commande (la création passe par le relais) ;
  - le rejeu de la suite v2 est versé : `test_relais_gemini_v4_suite_v2.py`, 49 réussis.
  
  Reste non essayé : `?key=` sur un relevé (le chemin de relevé est reconstruit sans requête, l. 173, donc la garde tient par
  construction). Mineur.

### Constat neuf

- **V-1 — significatif (étroit) — la garde du contenu d'un lot vérifie l'objet que Python lit, pas les octets envoyés.**
  - Où : `relais_gemini_v4.py` l. 469-483. Le corps est lu, analysé par `json.loads`, vérifié, puis **relayé tel que reçu**
    (`corps_lu`).
  - Démontré par sonde, relais v4 réel devant le faux amont : chacun de ces corps reçoit **200** et part à l'amont tel quel.
    - **Clé JSON en double** : un premier `input_config` porte 3 requêtes, dont une qui nomme `models/autre`, et un second
      `input_config` en porte une seule. `json.loads` garde le dernier, donc la garde voit une seule requête propre.
    - **Nom de champ en casse « chameau »** : `input_config` porte une requête propre, et `inputConfig` à côté porte 3 requêtes
      avec `tools`. La garde ne lit que `input_config`.
    - **Champ `model` au niveau du lot** (`batch.model` étranger) : il n'est pas vérifié.
  - Ce que l'amont ferait de ces corps (dernière clé, première clé, refus, lecture des noms en casse « chameau ») **n'est pas
    vérifié**. Je n'affirme pas qu'il générerait plusieurs fois ou sur un autre modèle (R8).
  - Pourquoi c'est significatif malgré cela : l'en-tête du v4 (point 5) promet que le contenu est « borné avant l'envoi ». Or la
    garde ne porte pas sur ce qui est envoyé. La commande par lot construit elle-même un corps propre, et la consigne n'y entre que
    comme texte échappé. Donc rien ne l'exploite dans l'usage prévu. Mais la pièce se dit réutilisable, et cette garde existe
    justement pour un client qui se trompe.
  - Correction (quelques lignes) :
    - relayer `json.dumps(objet vérifié)`, et non les octets reçus : ce qui est vérifié devient ce qui part ;
    - refuser toute clé hors d'une liste blanche à chaque niveau : `batch` (`display_name`, `input_config`),
      `input_config` (`requests`), chaque entrée (`request`, `metadata`), et `request` (`contents`, `generationConfig`,
      `systemInstruction`, `safetySettings`, `model` égal au chemin) ;
    - ajouter un essai par forme détournée.
  - Également à fermer par cette liste blanche, sans être neuf : `generationConfig.candidateCount` multiplie les sorties d'une
    même requête, et `cachedContent` charge un contenu en cache. Tous deux passent (200, sonde). `candidateCount` passait déjà en
    v2 sur `generateContent`.

### Constats restants (mineurs)

- **M-7** — l'en-tête ne dit pas que les lots retenus ne survivent pas à un redémarrage (demandé par R-1).
- **M-8 — R-4 à R-7 de la contre-lecture, non repris.**
  - R-4 : une place de lot est encore consommée quand `--max-appels` refuse (l. 477-478).
  - R-5 : le corps d'une annulation est lu sans borne. Un `Content-Length` non entier lève `ValueError` dans le gestionnaire,
    et la connexion tombe sans réponse JSON. Sonde : `RemoteDisconnected`. Le compteur d'annulations a déjà été incrémenté
    (1 compté, rien envoyé).
  - R-6 : un relevé trop grand n'est pas journalisé.
  - R-7 : le message d'erreur des bornes ne nomme ni `--max-lots`, ni `--max-releves`, ni les deux nouvelles bornes (l. 623).
- **M-6** — dans la copie de la suite v2 :
  - la docstring héritée dit encore « relais-gemini-v2 » (l. 10) ;
  - elle renvoie à un fichier `test_relais_gemini_v4.py` qui n'existe pas (l. 12) ;
  - le nouvel en-tête dit pourtant « engendrée par sed, rien d'autre ne change ».

  Texte seulement : le code est identique.

## Ce qu'il faut avant le scellement

1. **La commande par lot** peut être scellée telle quelle. Corriger M-1 avant est recommandé (deux lignes), mais pas exigé.
2. **Le relais v4** : corriger V-1 (relayer l'objet vérifié, ré-encodé ; liste blanche des clés ; un essai par forme détournée).
   Dire M-7 dans l'en-tête. R-5 peut être fermé au passage (borne et `try` sur le corps de l'annulation).
3. Le différentiel de V-1 est petit. Une vérification courte par un sous-agent neuf suffit : il relit `motif_contenu_lot` et
   l'envoi, et rejoue les 29 + 49 essais et les nouveaux.

Ce rapport ne modifie aucune pièce. Le seul fichier écrit dans le dépôt est celui-ci.
