# Rapport — devis et instruments de l'essaim — v3

- Sous-agent auteur (Claude Opus 5.5), 22 novembre 2026. **Aucune dépense, aucun appel de modèle, aucun réseau, aucun commit.** Rien n'a été modifié dans le dépôt.
- Les pièces sont écrites dans un bloc-notes, pour être versées sous `docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v3/`.
- Pièces corrigées : vérification de la v2, `docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v2/verification-v1/verification-devis-instruments-essaim-v2-v1.md` (réserves R1 à R6 et « comparaison non équitable ») ; réponse 14 de Fable (`origin/main:docs/notes/demandes-fable-api-2026-11-22-v1/reponse-14/relecture-fable-api.md`).
- Le dossier inachevé `docs/notes/organisme-essaim-communicant-v1/en-cours-inacheve-2026-11-22-0700/` est **repris**, après examen. Le § 7 dit ce qui est repris, ce qui est remplacé et pourquoi.
- Python 3.13.18, numpy 2.4.6. Graines par `SeedSequence`, données dans chaque sortie.
- Aucun refus de permission, de classifieur ou de garde n'a été rencontré.

## Verdict

**Les réserves R1, R2, R4, R5 et R6 sont corrigées et éprouvées.** R3 reste ouverte.

- **Vrai pire du pilote P-std sur Kimi sous les gardes du lanceur : 203,94 USD.**
  - C'est un plafond appliqué avant chaque appel, et non plus un pire conditionnel.
  - Il tient sous quatre hypothèses de facturation (H1 à H4), dont deux sont contrôlées après chaque appel.
- **Barre du pilote**, sur l'information servie (case de 9 000 jetons) et sur les composantes conditionnelles : la base gloutonne renforcée, **10 conditionnelles sur 14 (0,714)** sur les 12 mondes de calibration.
  - La base gloutonne simple n'en couvre que 6 sur 14 (0,429).
  - En couverture globale, la plus forte est la base simple (médiane 0,667 ; renforcée 0,571).

## 1. Réserve par réserve

| réserve | état | ce qui est fait | preuve |
|---|---|---|---|
| R1 : deux scripts lisaient `../essaim-devis-instruments-v1/` | **corrigée** | (1) `racine_depot_v1.py` : la racine est le premier parent qui contient `docs/sha256sums-lancement-v2.txt`, sinon `DEPOT_CONTROLE_IA`, sinon refus (jamais de chemin deviné). (2) Tous les chemins de pièces sont relatifs à la racine. (3) Les modules scellés qui portent un chemin absolu (`bases_sans_modele_v1.py`, `base_gloutonne_renforcee_v1.py`, `test_de_mort_programme_v1.py`) sont chargés **relogés** : empreinte de la source vérifiée, une seule ligne remplacée, et un remplacement non unique fait refuser. Aucune pièce v3 ne cite le bloc-notes | `rejouer_v3.sh` : rejoue depuis le commit (racine trouvée au-dessus) ou depuis le bloc-notes (`DEPOT_CONTROLE_IA=… bash rejouer_v3.sh DOSSIER_NEUF [--long]`) ; sans racine, refus vérifié (code de `RacineIntrouvable`) |
| R2 : 3 artefacts passaient le contrôle des nombres | **corrigée** (code du dossier inachevé, repris à l'octet) | analyse de toutes les affectations, définition multiple refusée ; marge, majoration et plafond C.8 lus, non écrits en dur ; ligne ajoutée refusée | `epreuves-devis-v3.json` : 25 / 25 tenues (5 sains, 20 artefacts) ; outil du relecteur rejoué tel quel : 10 / 10 tenues, dont R2, R6 et R9 (`artefacts-relecteur-sur-devis-v3.txt`) |
| R3 : l'oracle v2 laisse passer un verdict sous une clé de `lois` ou dans l'identifiant | **ouverte** | constat seulement (§ 6) | `artefacts-relecteur-sur-oracle-v3.txt` |
| R4 : « facteur 1,8 à 2,4 » | **corrigée** | rapport calculé par le script, lu dans la sortie v1 à son empreinte : **1,819 à 3,228** (Kimi de 3,11 à 3,23) | `calcul-devis-essaim-v3.json`, `rapport_pire_v3_sur_pire_v1` ; `devis-essaim-communicant-v3.md` |
| R5 : « autres leviers 1,1 à 2,5 » ; « / 5 » caché | **corrigée** | (1) facteurs calculés par levier, (a) « tout » de ×2,25 à ×8,20 ; (2) la division par 5 est **retirée** (aucune pièce ne la justifie) ; mise en route entière, 10 h et 30 h ; (3) messages comptés à leur propre sortie | `calcul-devis-cout-reduit-v2.json`, `facteurs_par_levier` et `pilote_P_std_modele_ouvert` ; `devis-cout-reduit-essaim-v2.md` |
| R6 : pire de 204 USD conditionnel à quatre gardes inexistantes | **corrigée** | lanceur et module de garde écrits, chaque garde éprouvée sur un cas sain et sur un artefact (§ 2) | `epreuves-gardes-pilote-v1.json` : 23 / 23 ; `test-gardes-pilote-v1-pytest.txt` : 23 tests passés |
| comparaison non équitable (B3 sur 2 000 instances) | **corrigée sur la calibration** | bases recalculées sur la case servie ; base renforcée ajoutée ; barre fixée (§ 3) | `bases-case-servie-v1-sortie.json` |
| trouvaille de côté : majoration de 25 % (affinage, l. 44) | rapportée | colonne à part, **non ajoutée** au pire de référence : au directeur | `calcul-devis-essaim-v3.json`, `pire_avec_majoration_affinage` |
| trouvaille de côté : troncature `int` (P-2gen) | corrigée | appels comptés sur le plan | `calcul-pilote-essaim-v2.json` |

## 2. Lanceur et gardes (R6)

### 2.1 Les fichiers

- `garde_pilote_essaim_v1.py` porte le plan gelé de P-std (744 appels : 12 mondes ; (a) 24 appels de proposeur et 12 messages ; (c) 26 appels de proposeur) et la classe `Garde`.
- `lanceur_pilote_essaim_v1.py` ne contient **aucun client de fournisseur**.
  - La couche d'appel est injectée.
  - Une exécution directe est refusée (code 20).
  - Chaque appel passe par `Garde.avant`, puis par `Garde.apres` ou `Garde.echec`.

### 2.2 Les gardes

Une garde franchie arrête la course. Elle laisse une ligne `{"evenement": "arret", "code", "garde", "detail"}` dans le journal, ouvert en création exclusive. Il n'y a aucun repli.

| code | garde | avant l'appel | après l'appel |
|---|---|---|---|
| 10 | sortie | `max_tokens` ≤ 24 000 (proposeur), ≤ 2 000 (message) | sortie rendue ≤ plafond |
| 11 | entrée | octets ≤ plafond × 2,8 (64 960 ; 16 800) | entrée rendue ≤ 23 200 / 6 000 jetons |
| 12 | messages | ≤ 12 par monde, ≤ 144 en tout | — |
| 13 | relances | ≤ ⌊10 % × 744⌋ = 74 | — |
| 14 | dépense | cumul + réserve dure ≤ plafond (203,94 USD) | cumul ≤ plafond |
| 15 | plan | appel suivant du plan, jamais rejoué hors relance | — |
| 16 | facturation hors borne | — | sortie ≤ `max_tokens` envoyé ; entrée ≤ octets + 256 ; usage complet |
| 17 | erreur inattendue du client | — | — |
| 20 | aucun client injecté | — | — |

- La réserve dure d'un appel vaut (octets + 256) × prix d'entrée + `max_tokens` × prix de sortie.
- Un appel échoué est compté à sa réserve entière.

### 2.3 Les épreuves

Faux client local, `SeedSequence(20261124)`.

- **Cas sains** (code 0) :
  - P-std réaliste : 64,00 USD ;
  - tout au plafond de jetons : 176,45 USD ;
  - 74 relances ;
  - pire extrême, tout au plafond et 74 échecs comptés à la réserve dure : **198,80 USD, sous la borne** ;
  - appel suivant du plan.
- **Artefacts**, chacun arrêté au code attendu, sans dépense au-delà du plafond :

| garde | artefacts |
|---|---|
| sortie (10) | `max_tokens` de 24 001 (proposeur) ou de 2 001 (message) ; sortie rendue de 24 001 ; message rendu de 2 001 |
| entrée (11) | 64 961 octets ; 23 201 jetons rendus |
| messages (12) | 13ᵉ message d'un monde |
| relances (13) | 75 relances ; un appel qui échoue sans fin |
| dépense (14) | plafond abaissé à 50 USD, arrêt à 49,74 USD |
| plan (15) | appel sauté ; appel rejoué ; identifiant inventé |
| facturation hors borne (16) | usage sans sortie ; 5 000 jetons pour 1 000 octets ; sortie au-delà de `max_tokens` |
| erreur inattendue (17) | erreur du client |
| aucun client (20) | absence de client |

- pytest rejoue les mêmes cas et vérifie trois choses de plus : la borne est bien le produit annoncé ; un journal existant n'est jamais écrasé ; l'exécution directe est refusée.

### 2.4 Le vrai pire

Source : `calcul-pilote-essaim-v2.json`, `couts_usd.P-std.kimi.decomposition_vrai_pire`.

| poste | USD |
|---|---|
| 744 appels aux plafonds de jetons | 176,448 |
| 74 relances à la réserve dure maximale (0,37043) | 27,412 |
| excès d'un seul appel au-delà du plafond d'entrée, avant l'arrêt au code 11 | 0,084 |
| **total** | **203,94** |

Autres espèces : première espèce Claude 407,89 ; Fable 5.2 815,78 ; seconde espèce Claude 1 019,72.

### 2.5 Hypothèses sous lesquelles le pire tient

- H1 : facture ≤ usage rendu.
- **H2 : la sortie, réflexion comprise, ne dépasse pas `max_tokens`.** C'est le point à vérifier chez le fournisseur de Kimi avant le GO.
- H3 : un jeton couvre au moins un octet.
- H4 : un appel échoué coûte au plus sa réserve.
- H2 et H3 sont contrôlées après chaque appel (code 16). H1 et H4 se contrôlent seulement sur la facture.

## 3. Bases équitables et barre du pilote (comparaison non équitable ; réponse 14, C.3)

### 3.1 Le dessin

- `bases_case_servie_v1.py` donne aux bases la même information que la case servie aux proposeurs. Il réutilise le code de la v1 et celui de la base renforcée du dossier inachevé, sans les changer.
- **HYPOTHÈSE déclarée** : la case est un CSV d'instances.
  - On garde les k premières des données servies de la v1, traits arrondis comme écrits.
  - Le budget est de jetons × 3,3 octets (pièce : `docs/notes/organisme-auto-conception-v1/devis-course-auto-conception-v1.md`, l. 40, `50e7d2f1…`, vérifiée par le script).
- Mondes : les **12 mondes MR-2 de développement (calibration)**. Aucun monde neuf du pilote n'est engendré ni lu.
- Règle de la barre, écrite avant la course :
  - par variante, la base la plus forte est celle qui couvre le plus de conditionnelles sur les 12 mondes, la couverture globale départageant les égalités ;
  - elle est choisie sur la calibration et gelée.
- Contrôle : B3 sur les 2 000 instances égale la sortie scellée de la v1 (`controle_B3_reference_egale_v1_scellee: true`).
- La base renforcée sur les 2 000 instances retrouve aussi les chiffres du dossier inachevé (13 / 14 ; médiane 0,7738). C'est un rejeu de ce dossier.

### 3.2 Les résultats

| variante (lignes de la case) | base | couverture globale, médiane (moyenne) | conditionnelles | ordinaires | formes fausses distinctes, médiane |
|---|---|---|---|---|---|
| **case-9000-3d (529-530), principale** | B3 | **0,667** (0,643) | 6 / 14 | 46 / 68 | 10,5 |
| | **B3R** | 0,571 (0,615) | **10 / 14** | 40 / 68 | 4 |
| case-6000-3d (352-353) | B3 | 0,571 (0,603) | 7 / 14 | 42 / 68 | 12,5 |
| | B3R | 0,667 (0,641) | 11 / 14 | 41 / 68 | 4,5 |
| case-9000-repr (374-375) | B3 | 0,667 (0,662) | 6 / 14 | 48 / 68 | 13 |
| | B3R | 0,708 (0,701) | 10 / 14 | 47 / 68 | 9,5 |
| référence, 2 000 instances brutes | B3 | 0,690 (0,688) | 3 / 14 | 53 / 68 | 4 |
| | B3R | 0,774 (0,750) | 13 / 14 | 48 / 68 | 0 |

### 3.3 La barre retenue

- **B3R sur la case de 9 000 jetons.** Couverture conditionnelle de 10 sur 14 (0,714).
- Par monde : 1 ; 0,5 ; 1 ; 1 ; 0 ; 1 ; 1 ; 1 ; 0 ; 1 ; 0,5 ; 1 (`resume.case-9000-3d.B3R.couverture_conditionnelle_par_monde`).
- Discordances appariées entre les deux bases, sur les conditionnelles : 5 composantes couvertes par B3R seule, contre 1 par B3 seule.
- Sur la couverture globale, la plus forte des deux est B3 : médiane 0,667. Elle est rapportée à côté.
- Au pilote, la barre se recalcule **par monde** sur les mondes neufs, avec ce code gelé et la case réellement servie.

### 3.4 Réserves sur les bases (R4, « trop étrange » vaut audit)

1. **Sur une case plus petite, B3 couvre plus de conditionnelles qu'avec les 2 000 instances** (6 ou 7 sur 14, contre 3), et produit deux à trois fois plus de formes fausses distinctes (10,5 à 13, contre 4).
   - C'est contre-intuitif. Hypothèse non vérifiée : avec moins de données, la recherche gloutonne prend des additions plus bruitées, dont certaines captent une conditionnelle par hasard.
   - À auditer avant que cette barre ne serve à une décision. Pistes : la couverture conditionnelle de cartes au hasard sur la même case, et la garde des formes fausses.
2. La forme de la case est une HYPOTHÈSE : aucune pièce lue ne fixe le contenu de la case de matière de MR-2.
   - Elle doit être gelée au préenregistrement, et la base doit recevoir exactement la case servie.
   - Si les proposeurs reçoivent aussi un résumé ou un outil, il faut refaire ce calcul.
3. La couverture n'est comptée que par des cartes « vraies ». Ces définitions restent « à préenregistrer » (`bases-sans-modele-v2.md`, D5).
4. Il n'y a que 14 conditionnelles sur 12 mondes, soit des mondes presque binaires (réponse 14, A.1). La densification (réponse 14, décision 5) reste au directeur.
5. Un essai sur le monde 1 seul a été fait avant la course complète, pour mesurer la durée. Aucune règle n'a été changée après cet essai.

## 4. Test de mort par programme (« excellent » ; réponse 14, levier 2)

### 4.1 La définition

`test_de_mort_programme_v2.py` et `juge_test_de_mort_isole_v1.py` (`f505a30f…`).

- Le juge tourne dans un **processus Python neuf** (`-I`). Il ne reçoit que deux fichiers : les cartes et les tranches tenues à l'écart (épisodes z, g, y), plus l'empreinte des tranches.
- La loi plantée n'existe pas dans ce processus. Il n'y a qu'une **réplication sur données tenues à l'écart**, selon la règle gelée de `M.test_de_mort` : 400 épisodes ; s = moyenne de log p_carte(y) − log m̂(y) ; « survit » si s ≥ 0,02.
- Le fournisseur de tranches, côté noyau, est le seul à lire le monde.
- Garde interne du juge :
  - ouvertures limitées aux deux entrées et au code ;
  - imports des modules du monde refusés ;
  - sous-processus, exécution et réseau refusés.
- Le parent vérifie l'empreinte du juge (compagnon) et refuse tout argument en plus.

### 4.2 Les épreuves, sur les 12 mondes de calibration

- **Équivalence exacte** avec `M.test_de_mort` sur les mêmes épisodes : écart maximal 0,0 ; 202 verdicts égaux sur 202.
- **Cas sains** :
  - loi du monde : survit 240 fois sur 240 ;
  - trois fausses : éliminées 240 fois sur 240 chacune ;
  - copie de K1 : survit 240 fois sur 240, comme attendu contre la marginale ;
  - juge gelé : aucun refus.
- **Artefacts**, refusés dans les 12 mondes et chacun par le motif de sa garde (un plantage ne compte pas) :
  - A : juge muté qui ouvre la partie scellée du monde ;
  - B : juge muté qui importe le générateur ;
  - C : juge muté qui appelle `os.system` ;
  - D : carte en forme de devis de monde ;
  - E : juge d'empreinte différente ;
  - F : argument en plus ;
  - G : empreinte de tranche fausse.
- **Constat (E5)** : le juge fautif « fermeture sur la loi du monde déjà en mémoire » **passe la garde de la v1** dans les 12 mondes. C'est la raison de la v2 : ce canal n'existe plus quand le juge est un processus neuf.

### 4.3 Réserves sur le test de mort

- **Accord avec l'oracle de 4 040 sur 4 040 : trop beau.** Les cartes du jeu sont loin du seuil. La sonde près du seuil du dossier inachevé (`sonde_seuil_test_de_mort_v1.py`, non revérifiée ici) montre une survie graduelle sous le juge de la v1 : 0 sur 240 à un gain de 0,015 ; 17 sur 240 à 0,020 ; 203 sur 240 à 0,025 ; 240 sur 240 à 0,040. Elle n'a pas été rejouée sous le juge isolé.
- Le verdict vaut « contre la marginale » et non « au-delà de l'archive » : une copie de K1 survit, et c'est au juge de l'archive de l'écarter.
- La garde interne ne peut pas séparer un verdict codé dans le contenu d'une carte. Seul le canal (deux fichiers) est fermé.

## 5. Coût

| | référence | lecture |
|---|---|---|
| devis v3 | `devis-essaim-communicant-v3.md` | montants de la v2 retrouvés ; pire v3 / pire v1 de 1,819 à 3,228 ; colonne de majoration de 25 % |
| coût réduit v2 | `devis-cout-reduit-essaim-v2.md` | pilote P-std sur Kimi : estimation **57,29 / 102,17 USD**, vrai pire **203,94 USD** ; pilote d'abord, ×20,1 à ×49,0 à espèce égale ; modèle ouvert 24,88 / 33,61 USD, pire 338,97 USD, non borné par les gardes |

## 6. Ce qui reste ouvert ou douteux

1. **R3, ouverte.**
   - L'oracle v3 du dossier inachevé (`oracle_toutes_cartes_v67_v3.py`, `0aeeb27d…`) refuse bien les artefacts E1, E2 et E3 du relecteur ; E4 passe, comme prévu.
   - **Mais il refuse aussi le jeu sain de l'auteur** (`a1.json` et `a2-permutes.json`, code 3). Ce jeu contient une carte malformée, `{"type": "inconnu", "x": 1}`, que la règle classe « rien ».
   - La correction n'est donc pas triviale : refuser tout type inconnu porteur de clés contredit la règle « malformée ⇒ rien ». Je ne l'ai pas reprise ; elle est à trancher.
   - La garantie réelle reste l'invariance de la classe.
2. **H2 chez Kimi** : la réflexion est-elle comptée dans `max_tokens` ? À établir avant le GO.
3. Le tarif de Kimi est repris par citation (`91f5cf8f…`) ; sa pièce primaire n'a pas été relue.
4. Anomalie des bases sur la case (§ 3.4, point 1) : audit à faire avant de geler la barre.
5. Majoration de 25 % : s'applique-t-elle ? Au directeur.
6. Graines des 12 mondes neufs du pilote : non engendrées, non lues, à sceller plus tard. Le préenregistrement du pilote n'est pas conçu ici.
7. Les tranches des épreuves du test de mort et les journaux des gardes ne sont pas versés. Ils se régénèrent par les graines, et leurs empreintes sont dans les sorties.

8. Rejeu fait depuis le bloc-notes, dans des dossiers neufs, par l'auteur seul (pas de rejeu indépendant) :
   - `rejouer_v3.sh` sans `--long` : tenu ; devis, épreuves du devis, pilote et coût réduit à l'octet ; gardes égales hors horodatages ; 23 tests pytest passés ;
   - test de mort v2 : égal hors horodatages ;
   - bases sur la case : **non rejouées** (environ 20 minutes).
   - Le rejeu depuis le commit, une fois versé, reste à faire par un relecteur neuf (R2 du programme).

## 7. Le dossier inachevé : repris ou non

| pièce | décision | raison |
|---|---|---|
| `calcul_devis_essaim_v3.py`, `epreuves_devis_v3.py` | **repris à l'octet** | rejoués : sorties identiques à l'octet ; outil du relecteur 10 / 10 tenues. Leur racine (`DEPOT_CONTROLE_IA`, sinon le chemin historique) échoue bruyamment, jamais en silence |
| `base_gloutonne_renforcee_v1.py` | **repris, importé relogé, inchangé** | la règle est écrite avant la course ; deux mondes de contrôle tenus ; le résultat sur les 2 000 instances est retrouvé |
| `test_de_mort_programme_v1.py` | **remplacé par la v2** | la règle est bonne et gardée (équivalence exacte) ; la garde dans le même processus est contournable (E5) |
| `sonde_seuil_test_de_mort_v1.py` | cité, non rejoué | voir § 4.3 |
| `oracle_toutes_cartes_v67_v3.py` | **non repris** | refuse le jeu sain (§ 6, point 1) |

## 8. Fichiers et empreintes (sha256)

| fichier | sha256 |
|---|---|
| `artefacts-relecteur-sur-devis-v3.txt` | `696c3ff297538cc14fe5a6cd0ab878b554adf9879a57687b7856e0919d653bdf` |
| `artefacts-relecteur-sur-oracle-v3.txt` | `646505fea6d8dfa9427c0bb366f8bd1693b3a39786ce0d6163ae8d6c5098aa12` |
| `bases-case-servie-v1-sortie.json` | `6c319f23e0ff96a3b9f37167fd98a81a8abee4a93c18e4b90eaf40da43c245bd` |
| `bases-case-servie-v1-sortie.stdout` | `b1eab1e7034bf9224935207d0d6df6ec6a1daafb83e42b08c43606bbb6705aac` |
| `bases_case_servie_v1.py` | `0658b3a2aa0b0cb94ff036c40f2fe7db0ac4b7a31c24e846bada9bbae6e6d119` |
| `calcul-devis-cout-reduit-v2.json` | `78647c5157638514e640ec04a31303ca3df892e461b594e2a69d43eb65e7eb48` |
| `calcul-devis-essaim-v3.json` | `35bf1757d4b068ef25ce5031bc240375e9f8259967682ae9fd5b3290e385d96d` |
| `calcul-pilote-essaim-v2.json` | `74f193e1dc09369204d427e44ecff76594e143e139902c914992eb846e15e10d` |
| `calcul_devis_cout_reduit_v2.py` | `d8d8c15743c55bc434fab6e7689038d7d125108d4da0c36296112ea69333ee45` |
| `calcul_devis_essaim_v3.py` | `934e550c79cf8e7d7c5a30b2bd342c0909f9868c7f82f5a51abb68f049d40d15` |
| `calcul_pilote_essaim_v2.py` | `9b45c3a4afd46831070d366831e46785406ac309b07cb654bb7c7f42ae6bcf5e` |
| `compagnons_v3.sh` | `2c850743bcf6ae6d90dac7d91bbb3bed94901103d7feba779012959e1d267ca9` |
| `comparer_hors_horodatages_v1.py` | `3b64ed68a6af80b81443b4fdae3814751854661b785402a679c2d0d110e45d97` |
| `devis-cout-reduit-essaim-v2.md` | `df84e67ee719b533b2abbaf5e5a9eda77e212f2af367fc990b2644500cbf0864` |
| `devis-essaim-communicant-v3.md` | `0eb84d1a61a047bdaa9b69c99b381539f96fae8d4a100900df12a8c477776ff1` |
| `epreuves-devis-v3.json` | `a13082a641d2394fbb12dc568aaf87e2f68e32c107e65f422acab7427a00c869` |
| `epreuves-gardes-pilote-v1.json` | `f8ea194cad437e386bf8e388574831d4c6e45c63ad05a67aa37f21d8ad650811` |
| `epreuves-gardes-pilote-v1.stdout` | `fba592092f0a3086b46568cd02c1dbaf1708098159e572e8d2332b4ee68580bf` |
| `epreuves_devis_v3.py` | `b9df50cf782416ecda4ee1a481ef00755506354088fb9f27ed8a1898543c8043` |
| `epreuves_gardes_pilote_v1.py` | `384045c3727ee37bc206276f4897be20912bf6e83706fe013cb253c4d41e3a19` |
| `garde_pilote_essaim_v1.py` | `f5b815c335cfec79303038e983e6ad81b40ba8383d7d9eef5e2eb05151b35aeb` |
| `juge_test_de_mort_isole_v1.py` | `f505a30fc7cbc38987ba36ad185d51b821f38e7bc8abbf841ec2e9c2ca2f380a` |
| `lanceur_pilote_essaim_v1.py` | `4a696e157ae7746ff19d2b76ed21855c6cba0d0da58671154599226eb06a6723` |
| `racine_depot_v1.py` | `3a5acf778146dc7df43716c082dc629f0251b8920a150940315863f235f0cccc` |
| `rejouer_v3.sh` | `c9612674afa886534668284d7ec9e2f860edea8d6ae65cf223933dd102911558` |
| `test-de-mort-programme-v2-sortie.json` | `3c537143fd6201b896227db582dca3b5a66724b6d728023251481d9be1c1e3d0` |
| `test-de-mort-programme-v2-sortie.stdout` | `2404343d1441137279ce0d38c8f06be65bc71332d24c51d65516936e7220004c` |
| `test-gardes-pilote-v1-pytest.txt` | `55c37935cbdee6a5dea2a79901ee76e81985b8a09807f0fc427af71c3dcd1839` |
| `test_de_mort_programme_v2.py` | `adfb3ef473d9ffd1e52b91154e35b34ef73c16aaf824115149d22df3cc2e5924` |
| `test_gardes_pilote_essaim_v1.py` | `65d707960d2d82bd9e53c3b5f167212a492e8e6a721e1ba650b00b5819c6c09c` |
| `rapport-devis-instruments-essaim-v3.md` | dans son compagnon `.sha256` (un fichier ne peut porter sa propre empreinte) |

Chaque fichier a son compagnon `.sha256` (format `empreinte  nom`, écrit par `compagnons_v3.sh`).
