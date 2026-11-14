# Rapport du développeur — codes v72 et v73 du pilote MR-2 (configuration v12, sonde qui fait réfléchir, bloc gelé par clés, sonde d'un seul relais) — v1

- **Développeur** : modèle A (session du compte organisme, brief `brief-compte-organisme-v2.md`, `fc0229ad…`, tâche 1). Je n'ai
  écrit aucun des codes v65 à v71 ni leurs contre-lectures.
- **Mandat** : R-2621, nœud 2 (« pour Argon, une sonde neuve avec une consigne qui fait réfléchir, donc une configuration v12 et un
  code qui la nomme ») ; R-2690 (décision de la mère sur PO-015 : « code v73 dont le bloc gelé nomme les relais par leurs clés,
  aucun identifiant de modèle Claude dans les pièces ») ; GO-2026-11-14-02 et R-2700 (sonde du seul relais Astra, sous-commande
  `sonde-un` du lanceur v73 admise). **Ajouts seuls** : aucun fichier des versions v65 à v71 modifié.
- **Dépense** : une seule, la sonde du seul relais Astra (GO-2026-11-14-02, R-2700), 0,0167 USD calculés (section 6). Aucune autre
  invocation payante, aucune machine, aucune clé affichée.

## 0. Verdict

Code v73 écrit, essayé, contre-lu deux fois par un autre modèle que le mien, paquet scellé contre `e7daf32`. **Essais : 138 passés
(v73), et les 115 de la v71 passent sur la même tête. Bancs : v72, 72 mutations sur 73 tuées pour la raison attendue (N18 survit :
son essai visé était trop faible) ; v73, 35 sur 35, dont B03 au second passage après reciblage (son premier essai visé ne pouvait
pas la voir) et N18b (N18 reciblée) tuée.** Le bloc gelé ne porte aucun identifiant de modèle. La sonde du seul relais Astra a
tourné une fois : toutes ses conclusions vraies, crédit du fournisseur vérifié. **Reste avant le scellement du texte du pilote** : la
sonde complète des quatre relais sous la configuration v12 (deux lignes neuves, section 7), dont le relevé seul fait le bloc gelé
définitif.

## 1. Arbre, branches, jalons

- Arbre reconstruit hors du dépôt de travail : clone en lecture seule du dépôt public (`94bfd92`, tête v67 `ab53b7f` dans
  l'historique), puis paquets v68 à v71 de `prep/pilote-mr2-v1` (`a5fdfcdf`), chacun égal à son compagnon et vérifié : tête v71
  `e7daf32fd090ec6be8331ee1216cec3f061e5f93`.
- Branche de l'organisme `prep/organisme-v73-pilote-mr2-compte-organisme-v1` (tête `ce8c6967e59f6ebbfa7b30654bde04fba716c70c`),
  jalons : `85167d3` (v72, jalon 1) ; `e6a3a11` (v72, jalon 2 : corrections de la contre-lecture v72) ; `b3a83da` (v73 : bloc par
  clés, `sonde-un`) ; `de6dde5` (jalon 4 : essais et banc v73 après la contre-lecture v73) ; `ce8c696` (jalon 5 : B03 reciblée).
- Paquet `organisme-v73-pilote-mr2-compte-organisme-v1.bundle` (`2b4017c7a4d675cde73b2e0bf9abc6e6c455f4854668f591668c1d2bba293b6e`),
  prérequis `e7daf32`, `git bundle verify` conforme. Liste des ajouts avec leurs empreintes : `ajouts-organisme-v73-contre-e7daf32.txt`. **Le patch textuel complet contre
  `e7daf32` n'est pas versé** : il recopierait la configuration et des essais qui portent les identifiants des modèles des
  proposeurs (R-2690 : aucun dans une pièce versée) ; le code entier est au paquet. Différentiel par paires (sans identifiant) :
  `differentiel-v71-v73.patch` (`b1f6cfa3…`).
- **Ajouts seuls** (`git diff --name-status e7daf32 ce8c696` : neuf « A ») :

| fichier (`orchestrator/`) | sha256 | rôle |
|---|---|---|
| `exemples/pilote-mr2-v70/configuration-pilote-mr2-v12.json` | `f69503dd4ba5e57a8bde230b3861571549d9598382808a8f3c0f4fa664ea818b` | v11 hormis version, `_lisez_moi` et les deux consignes de la sonde |
| `pole/proposeurs_pilote_v72.py` | `de6bc923271a60ccdf96d2bd2d053be05c13170625bec993a42f24ccca93180d` | lecture de la v70 recopiée, version v12 exigée |
| `pole/sonde_pilote_v72.py` | `636d5a958cc1ca1ed384876c4be84c3c39e4c40338888a7d8205e0b3255b1df5` | `reflexion_observee`, `motif_reflexion_absente` (refus nommé seulement pour un appel abouti à usage entier), relevé v72 |
| `demonstrations/pilote_mr2_v72.py` | `a2bfce454e0bdbdc3d31f6182c2fc8210fe916334558b80536394195d0cb2d1c` | lanceur v72 (gardé ; remplacé par le v73) |
| `demonstrations/pilote_mr2_v73.py` | `88f997666bd31a44a3aa0138edbebbaa11ddefabdf407db031030a898ae8df1d` | **lanceur gelé** : bloc par clés ; sous-commande `sonde-un` |
| `essais/test_pilote_mr2_v72.py`, `essais/test_pilote_mr2_v73.py` | `336b420b…`, `cdeb1e6a…` | essais |
| `essais/mutations_pilote_mr2_v72.py`, `essais/mutations_pilote_mr2_v73.py` | `dc80183f…`, `ca126619…` | bancs |

Outils de génération (versés, chacun n'écrit qu'un fichier neuf par remplacements comptés) : `faire_proposeurs_v72.py`,
`faire_lanceur_v72.py`, `faire_lanceur_v73.py`, `faire_essais_v72.py`, `faire_essais_v73.py`, `faire_banc_v72.py`,
`faire_banc_v73.py` ; essai à sec `essai_a_sec_sonde_v72.py`.

## 2. Ce qui change, et pourquoi

1. **Configuration v12** : consignes de la sonde écrites pour faire réfléchir (relevé v71 `bd0a2dab…` : Argon sans
   `thoughtsTokenCount` aux deux appels) : borne gelée « Combien d'entiers de 1 à 10000 sont divisibles par 7 ou 11, mais pas par 13 ?
   Le seul nombre. » (94 octets) ; borne courte « Énumère un à un les nombres premiers entre 1000 et 1200, en justifiant chacun par
   ses divisions. » (99 octets). Tout le reste égal à la v11 (essai). Pire cas inchangé (consigne de 100 octets).
2. **`reflexion_observee`** (Argon, Astra) : champ de réflexion brut présent, entier, > 0 à l'un des deux appels ; exigée. Elle
   **ne durcit rien** (contre-lecture v72 : elle est impliquée par `verdict_egal_a_la_regle`, 4 800 cas, aucun contre-exemple) :
   elle nomme le refus « champ de réflexion absent », et seulement pour un appel abouti à usage entier (jalon 2) ; un appel en échec
   en amont (Astra 429 de la v71) garde le motif général.
3. **Bloc gelé v73** : lignes « borne-de-sortie » par clé de configuration, ligne « identite-des-proposeurs » (l'identité reste
   gelée par l'empreinte du fichier de configuration, au bloc) ; aucun identifiant de modèle (essai ; mutations B01, B02).
4. **`sonde-un`** (v73) : sonde d'un seul relais sous une ligne à part, montant exact écrit au code (`SONDE_UN` : Astra, 2 USD,
   « sonde » et « seul relais Astra » au périmètre) ; un relais (plafond : sa part de sonde, 1,84) ; deux appels ; registre des
   lancements ; relevé propre (`releve-sonde-un-relais-v73.json`) que le mode réel ne lit pas.

## 3. Essais

- v73 : **138 passés, 220 sous-essais** (journal `essais-pilote-v73.txt`, tête `de6dde5` puis `ce8c696`, essais inchangés entre les
  deux) : les 129 de la v72 portés sur le lanceur v73, et `V73` (2), `SondeUnRelais` (3), `SondeUnFonctions` (2), `SondeUnArrets` (2).
- v71 sur la tête v73 : **115 passés, 195 sous-essais** (`essais-pilote-v71-sur-la-tete-v73.txt`).
- v72 au jalon 2 : 129 passés (`essais-pilote-v72-jalon2.txt`).

## 4. Bancs de mutations

- **v72 (jalon 2)** : 73 mutations (46 de la v71 reciblées, N01 à N27) ; **72 tuées pour la raison attendue, N18 survit** (son essai
  visé ne vérifiait que la différence des consignes v11 et v12, et la seconde consigne différait encore) ; corrigé : l'essai
  `test_consignes_v12_mot_pour_mot` et la mutation N18b, tuée au banc v73. Journal `mutations-pilote-v72-jalon2-journal.txt`.
- **v73** : 35 mutations visant le lanceur v73 (17 du banc v72 reciblées, B01 à B03, U01 à U13, U15, N18b) ; premier passage **34
  tuées, B03 survit** (son essai visé, `test_fermeture_des_imports`, exécute le lanceur sans l'importer et ne pouvait pas voir son
  retrait de la liste gelée) ; B03 reciblée sur `test_lanceur_v72`, qui affirme le lanceur v73 dans la liste, puis rejouée seule :
  **tuée** (`mutations-pilote-v73-B03-rejeu-journal.txt`). Les modules de lecture et de sonde, inchangés depuis la v72, sont jugés
  par le banc v72.
- Non couvert par une mutation, dit : U14 (refus après un envoi sans relevé) : aucun artefact atteignable depuis la doublure.

## 5. Contre-lectures (autre modèle que le mien)

- **v72** (`contre-lecture-code-pilote-v72-v1.md`, `a4420d6b…`) : « autorisable après corrections » ; bloquant hors code (Astra
  jamais sondé) ; majeurs 2 et 3 corrigés au jalon 2 ; mutations N21 à N27 reprises.
- **v73 et jalon 2** (`contre-lecture-code-pilote-v73-v1.md`, `aa53683e…`) : « autorisable pour la sonde d'Astra » ; conditions de
  lancement tenues (registre des GO lu sur `main`, journaux v73 versés avant l'appel, noms non vides, une invocation sans
  `--reprise`) ; N18 et mutations U09 à U15 reprises ; réserve : `--reprise` relancerait un relais neuf à 1,84 sans déduire la
  dépense antérieure (la commande ne l'emploie pas ; à refuser dans un code futur).

## 6. Sonde du seul relais Astra (GO-2026-11-14-02, R-2700)

Une invocation, 2026-11-14 10:40:47Z → 10:40:57Z, code 0, par la commande versée avant l'appel (`112d9a37` du lot) ; relevé
`40eb7b325da757c2ef7ec87afed0ce8ee6b89d8b973cf9201c63b406b7c6f599`, complet. Borne gelée : 200, complet, 4 octets visibles, 64 jetons
de sortie dont 53 de réflexion ; borne courte : 200, tronqué, 256 dont 256 de réflexion. Toutes les conclusions vraies, verdict
« comprise » égal à la règle gelée. **Dépense calculée 0,0167 USD** (prix standard lu, R-2677). Dossier entier versé sur
`lot/compte-organisme-v1` (`994b8fda`).

## 7. Sonde complète des quatre relais (à faire avant le scellement) : commande, devis, lignes

Le mode réel exige le relevé de la sonde complète (version `releve-sonde-pilote-v72`) fait **sous ce code et cette configuration**
(empreintes au relevé) : le relevé v71 et celui de `sonde-un` ne le remplacent pas. Pièce à part :
`devis-et-lignes-sonde-complete-v73-v1.md` (même dossier).

## 8. Écarts et limites, dits

1. Les consignes v12 ne garantissent pas qu'Argon réfléchisse (confiance d'environ 60 % selon la contre-lecture v72) ; s'il ne
   réfléchit pas, la sonde complète refuse sous le motif nommé, et une voie nouvelle sera un nœud (réglage de réflexion envoyé).
2. Le pire cas d'Argon n'est borné par la borne gelée que si son plafond de sortie couvre la réflexion ; sinon le dépassement est
   constaté après coup (arrêt, relevé partiel, Astra non sondé car appelé après).
3. Le registre des lancements de la sonde vit dans un fichier hors dépôt de ce conteneur ; sa copie est versée après chaque sonde.
4. Le relevé de la sonde et les pièces brutes portent l'identifiant **servi** des modèles (`modele_servi`), et le paquet (binaire)
   contient la configuration qui les nomme : point porté à la mère (R-2690).
5. Le crochet de garde du dépôt n'était pas chargé dans cette session (PO-001) au moment de la sonde d'Astra.
