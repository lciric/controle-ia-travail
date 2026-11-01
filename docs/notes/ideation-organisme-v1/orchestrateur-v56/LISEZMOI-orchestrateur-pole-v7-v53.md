# Orchestrateur du pôle, v7 — version 53 : course 2 et son pré-pilote (R-630 à R-643, R-640)

- Date : 2026-10-31. Auteur : sous-agent neuf de la lignée conv-audit (Claude Opus 5.5), branche `canal/conv-audit-n04`.
  **Non contre-lue** (R2 : à faire par un sous-agent neuf avant tout lancement réel).
- Base : la v52b telle quelle (`../EMPREINTES-orchestrateur-v52b.txt`, 339 empreintes, vérifiées avant la copie). **Aucun
  fichier de la v52b n'est modifié** (R12) : l'arbre v52b est copié, 18 fichiers nouveaux et ce LISEZMOI sont ajoutés
  (vérifié par l'essai `TestR12` : chaque empreinte de la liste v52b tient sur l'arbre v53).
- Aucun appel payant, aucune clé lue, aucun réseau : essais joués sous `unshare -n` (seule la boucle locale est levée, pour
  le faux relais Kimi et les relais d'essai déjà présents) ; moteur simulé et faux relais seulement. Rien lu sous `donnees/`.
- Spécification : préenregistrement du pré-pilote, **brouillon 6, non gelé** (`brouillons/…/pre-pilote-course-2-v1/
  preenregistrement-pre-pilote-course-2-brouillon6.md`, `sha256sum -c` OK). **Aucun seuil n'est fixé dans le code** : tout
  passe par un fichier de configuration JSON, refusé avant tout appel si un paramètre manque ou porte « À REMPLIR ».

## Ce qui change (les neuf points de la mission)

| point | où | ce qui est fait |
|---|---|---|
| 1. Kimi K3.1 Pro proposeur, voie protocole | `pole/adaptateur_kimi_v53.py` | `AdaptateurKimiProtocole` : même contrat `lancer(...) -> Resultat` ; parle directement au relais Kimi v4 de session-depot (`POST /v1/chat/completions` sans flux, `GET /relais/etat`), boucle locale seule, sans mandataire, sans en-tête d'autorisation, sans `tools`. Garde du pire cas avant envoi (règle de `commande_kimi_v1.py`). Prix, sortie maximale et minimale, délai : **injectés, aucun défaut**. Refus (R-764) : modèle servi autre, 502 « modèle servi différent », 403, `content_filter` ; erreur : vide, tronqué, usage absent (pire cas compté) |
| 1 bis. Garde de niveau méthode chez Kimi | `pole/aiguilleur_v53.py` (`GardeKimi`) | chaque fiche de Kimi passe l'aiguilleur ; « concret » = refus + journal scellé sans contenu ; taux lu contre S12 injecté ; au-dessus : arrêt du rôle proposeur de Kimi (et de Kimi metteur en fusion), nœud consigné |
| 2. Notation croisée | `pole/juges_croises_v53.py` | chaque fiche jugée par chaque juge (Kimi, Argon, Opus 5.5), un appel par fiche et par juge, consigne figée + la seule fiche sous un identifiant opaque propre au juge : aucun juge ne voit les notes des autres. Items injectés (k) ; X = part des items vrais ; « notable » = tous vrais. **Agrégation par configuration** : `au_moins` (q injecté), `unanimite`, `majorite_stricte`. A2 : version servie d'un juge changée → arrêt. Étalonnage M1 (rappel P, spécificité, exactitude équilibrée, kappa de Fleiss, kappa de Cohen par couple) contre S1 à S4 injectés |
| 3. Aiguilleur avant les juges, jamais sacrifié | `pole/aiguilleur_v53.py` | trois classes (`niveau_methode`, `a_corriger`, `concret`) ; seul `niveau_methode` reçoit un **passeport** (identifiant + empreinte du contenu exact) ; juge, tableau, lecteur d'étiquettes et bisociateur l'exigent (A17) ; refus ou réponse illisible = aiguillage ; journal scellé sans contenu ; étalonnage M4 contre S10, S11 injectés. La configuration refuse une étape d'aiguillage non protégée |
| 4. Tableau minimal | `pole/tableau_v53.py` | programme : titre + résumé d'une ligne (champ injecté), longueurs S21 injectées, même case seulement, passeport exigé ; `verifier_tableau` (A18) avant de servir ; passe « tableau » après la passe 1 (sacrifiable) |
| 5. Mémoire anti-redite | `pole/memoire_v53.py` | bardeaux de mots (taille et seuil t* injectés) ; paires intra-lot, inter-fournisseurs et contre les générations précédentes ; « plongement » accepté seulement si une fonction nommée est injectée (sinon refus) |
| 6. Bisociateur à trois bras | `pole/bisociateur_v53.py` | bras méta (annexe scellée + empreinte injectée, sinon « non produit (annexe non conforme) », A20 ; désaccord hors score, garde à É0) ; substitut inspiré de Gu et Krenn (source S31 + empreinte injectées, sinon « non produit (source absente) », A19 ; seul le mode « substitut » est branché) ; bras basique (exposant et décalage injectés). Règle des paires n < 2 / n = 2 / n ≥ 3, paires distinctes, ordre de priorité et ordre des fusions tirés (SeedSequence, R9), fusion aveugle (consigne commune, aucun nom de bras), fusions comptées à part, étiquetées exploratoires au registre, clé des bras au coffre ; pas de bras hasard |
| 7. Règle de non-lecture | `pole/coffre_v53.py` | verdicts et clés déposés scellés ; `ouvrir` avant la fin de la phase de mesure = incident consigné + arrêt ; consommations lues à part ; la règle d'A1 ne reçoit que des montants (`budget_v53.rejouer`) |
| 8. Étage de tests de mort dans la course | `pole/etage_entre_generations_v53.py` | l'étage **inchangé** (`tests_de_mort_v3.executer_tests_de_mort`) joué entre deux générations sur les fiches les mieux classées ; refusé sans `POLE_MACHINE_JETABLE_V53=1` ou si un **nom** de variable de clé est présent (aucune valeur lue) ; projection des fiches du texte I sur les champs de l'étage par une correspondance injectée |
| 9. Plafonds, arrêts, A15 | `pole/budget_v53.py`, `pole/configuration_v53.py` | règle d'A1 du brouillon 6 jouée mot pour mot (projection, arrêt d'étape, plafond, coupure à S17 ; réservation de relais = réservation ; étape réductible jamais retirée entière ; hors porte) ; S17 et arrêt injectés, aucun défaut ; A15 : `GO_ID` + ligne de `registres/go.md` lue comme la garde du dépôt (calcul, Lazar, validité, révocation) **et** plafond de la ligne ≥ somme des plafonds de la course |
| orchestration | `pole/course2_v53.py`, `demonstrations/ideation_v5.py` | une génération : proposition → aiguillage → juges → passe « tableau » → étiquettes → fusions → mémoire → fin de mesure → classement ; `executer_course` enchaîne les générations (héritage : titres, résumés, verdict agrégé) et l'étage entre elles. Lanceur v5 : sans `--course-2`, rend la main au lanceur v4 (mêmes sorties) |

## Fichiers nouveaux (rôle, empreinte)

| fichier | rôle | SHA-256 |
|---|---|---|
| `pole/adaptateur_kimi_v53.py` | Kimi par voie protocole | `09a46515ff30a99f360fcbc7d4c613c35cb511439a5b6c249327e477fdee4ada` |
| `pole/aiguilleur_v53.py` | aiguilleur, passeports, garde de Kimi, étalonnage M4 | `a856cdaa37e8fb1f3b873ef2c0d9aa439ee0a8838f5ee9a2910cb3c0dcf8007f` |
| `pole/bisociateur_v53.py` | trois bras, paires, fusion aveugle | `962eb8ce22d5af1bf59970e9ef9cab15620edef4d5e9746161bc302e97c2af02` |
| `pole/budget_v53.py` | S17, arrêt d'étape, règle d'A1 | `cefc7e76322b8f8266ec77f31ecb06bf1ea21633ab5dec1e1b91dc62e4374345` |
| `pole/coffre_v53.py` | non-lecture (A21) | `f8a70c8f71c380689b2979e3c212d09379ceee1973465b2b207b493cbd73c380` |
| `pole/configuration_v53.py` | paramètres injectés, refus de partir, A15 | `ef72ffbf6b5ba546fb5e509502b59f0d9ac4f78772dcb9570ef36086639f4a78` |
| `pole/course2_v53.py` | génération et course | `8f2d035828df913d8fa92e1b7d0c8e41ac73e8416e60f3b674753c27f5c61237` |
| `pole/etage_entre_generations_v53.py` | étage v3 entre générations, machine jetable | `d568d25bf7d96011cfdcda12e7bc2c1933a61827b237f8c8c363b4055122ad4b` |
| `pole/fiches_v53.py` | fiches du texte I, métadonnées à part, garde A4 | `7cfcf8329c66c7a37ceb2992cc96e21aedbfa0a10525467672794090a128eda6` |
| `pole/graines_v53.py` | SeedSequence par tâche (R9), `cle_de_tache` du dépôt | `7eb838958b28c7b7a5ee20177dfc3d0c194002b99b2382e019fe7d91c3090dc0` |
| `pole/juges_croises_v53.py` | notation croisée, agrégation, étalonnage M1 | `c4c6ab12dc471eef078c116a4205a22d9b498da720ce71e37a0a6edae6c4239b` |
| `pole/memoire_v53.py` | anti-redite | `43b01b43b1ec347ff02b456975d74c17e7a0e974e9b95e9ba4935bdb895f31a0` |
| `pole/simulation_v53.py` | moteur simulé (aucun appel) | `27129c62498e3d5b801eb4d882b8abb7db2c3a0bfb2205829a62d7f0c69a353c` |
| `pole/tableau_v53.py` | tableau minimal, garde A18 | `1a8267fea6d147b070d697ccd2c9d33f2514be6fcba106dca8ca123be1cb7403` |
| `demonstrations/ideation_v5.py` | lanceur | `1894f250264eaaccbf891dfa255e71dc587fe415c8d21e283391203a2fe73444` |
| `essais/aides_v53.py` | pièces et configuration d'essai (valeurs d'essai, aucune recommandée) | `4aaddd698fe1400430e59d5449541acde8f7a6346169a1978d533e948b79c51e` |
| `essais/test_v53_instruments.py` | 39 essais | `bfa43ce0800ce9c591673611b0eb08c15f77be7842d8a226abb5857cf09d6114` |
| `essais/test_v53_course2.py` | 17 essais | `3466c06031d3244c6e29fca352f0925830683daaf14565d10338a8f2d06a4d7d` |

Liste complète : `EMPREINTES-orchestrateur-pole-v7-v53.txt` (tout l'arbre sauf elle-même et son compagnon). Code :
`CODE-orchestrateur-pole-v7-v53.zip` (mêmes dossiers que les archives précédentes : `conception-v7-v1.md`, `demonstrations/`,
`essais/`, `exemples/`, `pole/`). La suite se joue **dans le dossier de livraison** (l'essai R12 lit
`../EMPREINTES-orchestrateur-v52b.txt` ; CL17 avait relevé la même dépendance pour quatre essais anciens).

## Lancement

```
python -I -B demonstrations/ideation_v5.py --course-2 CONF.json SORTIE_NEUVE --generations N --verifier-seulement
python -I -B demonstrations/ideation_v5.py --course-2 CONF.json SORTIE_NEUVE --generations N --moteur simule
GO_ID=GO-AAAA-MM-JJ-NN python -I -B demonstrations/ideation_v5.py --course-2 CONF.json SORTIE_NEUVE --generations N \
    --moteur reel --registre-go registres/go.md --confirmer-moteur-reel
```

Clés de configuration (forme complète dans `essais/aides_v53.py`, valeurs d'essai seulement) : `racine_graines`,
`champs_fiche`, `champ_titre`, `champ_axe`, `budget` (`plafond_usd`, `arret_etape_usd` ou « sans », `etapes` : les six étapes
de la génération dans l'ordre, rôle, rang, réduite), `juges`, `items_juge`, `agregation`, `aiguilleur` (dont `fournisseur`),
`garde_kimi.debordement_max`, `tableau`, `memoire`, `bisociateur` (bras, `k_paires`, `meta.annexe`, `gu_krenn` (S31),
`basique`, consignes de fusion et de lecture, `metteur_fusion`), `proposeurs`, `cases`, `plafonds_session`,
`etiquettes_interdites`, `lecteurs_etiquettes`, `pieces` (chemin + empreinte), `fournisseurs` (moteur réel :
`kimi_protocole`, `commande_externe`, `claude_sdk`), `simulation.cout_par_appel_usd` (moteur simulé), `etage_tests_de_mort`
(facultatif).

## Essais

Commande : `unshare -n` (boucle locale levée), `env -i PATH=/usr/bin:/bin HOME=/tmp LANG=C.UTF-8 python3 -B -m pytest essais -q`.

- **v53 seule** (`test_v53_*`) : **56 essais, 56 OK** (31 sous-essais).
- **Suite entière, sans variable** (comme la commande de la mission) : **607 essais : 594 OK, 13 en échec**. Les 13 sont
  exactement ceux de la v52b sur cette machine, qui **n'a pas `bwrap`** : essais réels du bac (`test_v51_01, 02, 04, 05, 06, 08,
  11, 12`, `test_v52b_02`, `test_v48_22`, `test_v49_19`, `test_v50_15`, `test_v50_16`), qui échouent exprès sans bac réel
  (CL15-04). Témoin : la v52b seule, même machine, même commande : **551 essais, 538 OK, mêmes 13 échecs**.
- **Avec `POLE_ESSAI_BAC_REEL_NON_JOUE=1`**, deux passes : **594 OK, 12 ignorés (« ESSAI RÉEL NON JOUÉ »), 1 échec**, chaque
  fois : `test_v51_06_programme_du_filtre_d_appels_systeme`, qui attend le motif « architecture 'riscv64' » de
  `verifier_outils` mais reçoit « bwrap absent » (le contrôle de `bwrap` passe avant celui de l'architecture) ; il ne passe
  pas par le décorateur d'essai réel. **Déterministe sur une machine sans `bwrap`, préexistant (v51), non aléatoire.**
- **Échec aléatoire préexistant de la v51** : non reproduit (cinq exécutions complètes : deux de la v52b, trois de la v53) et
  non nommé dans les registres (R-665 dit seulement « 1 échec aléatoire préexistant »). Hypothèses : soit `test_v51_06`
  ci-dessus (selon que `bwrap` est présent), soit l'essai connu pour être intermittent sous charge
  (`test_v6_relais_reel::RelaisEnProcessus::test_artefact_plafond_atteint`, LISEZMOI v11 et v15). **Non identifié avec
  certitude** ; il n'a pas reparu.

Gardes nouvelles, cas sain et artefact (R5) : configuration (manques, « À REMPLIR », pièce altérée, bras sans paramètre) ;
A15 (sans `GO_ID`, absent, plafond insuffisant, type, échéance, révocation ; lanceur réel refusé avant tout appel) ; A1
(retrait, réduction puis lancement, réduite qui ne tient pas jamais retirée, protégée non lancée, coupure à S17, arrêt d'étape,
hors porte, rejeu sur consommations, verdict refusé par le budget) ; A21 (lecture avant la fin, consommation portant un
verdict, lecture fautive dans une génération) ; R9 (SeedSequence, numpy < 1,25 refusé) ; Kimi (cas sain, huit artefacts,
pire cas sans envoi, réglages sans défaut, adresse non locale) ; aiguilleur (concret, refus, A17, contenu modifié après
passage, S12, étalonnage) ; A4 ; juges (aveugles, A2, agrégations, étalonnage) ; A18 ; mémoire ; paires (n, gardes) ; A20 ;
désaccord hors score ; S31 ; basique ; fusion aveugle ; étage (machine non jetable, nom de clé, intégration avec l'étage v3
réel et l'exécuteur factice, lanceur qui construit l'étage) ; génération entière (cas sain, A4, débordement de Kimi sans copie
du contenu nulle part, A19, A20, budget bas, aiguilleur sacrifiable refusé, A2 entre lots) ; R12.

## Choix de code (pris seuls ; à confirmer)

1. **S17 par génération** : le plan, son plafond et la règle d'A1 s'appliquent à chaque génération ; la ligne de GO doit couvrir
   N × S17 + (N − 1) × plafond de l'étage.
2. Les six étapes de la génération et leur ordre sont fixés par le code ; la configuration doit les nommer toutes, dans cet
   ordre, sans étape en plus (les étapes propres au pré-pilote ne sont pas jouées par la v53) ; aiguillage, proposition et
   juges doivent être protégés.
3. Classement : notable agrégé, puis nombre de juges notables, puis **somme** des X, puis identifiant.
4. Juge absent (refus, réponse illisible) : jamais notable ; fait tomber l'unanimité ; `majorite_stricte` se lit sur les présents.
5. Fiche « à corriger » : retenue, comptée, servie à personne (aucune correction automatique).
6. Refus de l'aiguilleur sur une fiche de Kimi compté comme débordement (côté prudent).
7. Débordement de Kimi : arrêt de Kimi proposeur **et** metteur en fusion. Le fournisseur Kimi est désigné par la clé `kimi`.
8. Rôles du kit : aiguilleur, lecteurs et juges en `juge_ideation` (aucun outil) ; proposeurs et fusion en `proposeur_ideation`.
9. Paire unique (n = 2) : au premier bras dans l'ordre tiré **qui peut la noter** (le brouillon dit « bras de priorité 1 »).
10. Bras méta : niche retenue seulement si les deux lecteurs s'accordent ; structures = union des deux lecteurs ; repli connu :
    `indicateurs_puis_structure` seul (autre règle d'annexe refusée).
11. Passe « tableau » : ses fiches sont aussi jugées (course) ; mémoire : compte les redites, ne les retire pas.
12. Étage joué après chaque génération sauf la dernière.
13. Machine jetable : `POLE_MACHINE_JETABLE_V53=1` et refus si un nom de variable finit par `_API_KEY`, `_TOKEN`, `_SECRET`
    (ou figure dans la liste du relais, plus `KIMI_API_KEY`, `MOONSHOT_API_KEY`).
14. A15 : plafond de la ligne de GO lu comme le plus grand montant « … USD » de la cellule, exigé ≥ somme des plafonds.
15. Étiquettes interdites (A4) : liste injectée, mot entier après normalisation, sur la fiche servie.

## Réserves

- **Non contre-lue (R2).** **Jamais lancée sur moteur réel** : la forme des réponses de Kimi, d'Argon et d'Opus aux consignes
  figées (blocs `{"fiches"}`, `{"classe"}`, `{"items"}`, `{"etiquettes"}`, `{"niche"}`) est un contrat que les consignes
  figées devront écrire ; non éprouvé.
- Les consignes figées, l'annexe du bras méta, la source de S31, la liste fermée des concepts et la grille des niches
  **n'existent pas encore** : la v53 les exige par empreinte et refuse sans elles.
- Vocabulaire de S31 servi en entier aux lecteurs : taille non bornée (une moisson OpenAlex peut le rendre très long).
- Désaccord des paires du bras méta : **non lu** en v53 (consigné comme tel ; il n'entre jamais dans le score).
- Le relais Kimi doit accepter une réservation dépassée jusqu'à S17 − cumul (DEP4, SUPPOSÉ) ; la v53 borne chaque session à
  min(plafond de session, reste avant S17).
- L'adaptateur Claude (kit) peut écrire ses propres traces dans le dossier de session ; la règle « contenu concret jamais
  copié » est vérifiée pour le noyau v53 et le moteur simulé seulement.
- Commit non lu au manifeste (arbre hors dépôt) : à porter au registre du run.

## Ce qui reste

1. Contre-lecture R2 de la v53 (modules nouveaux et lanceur).
2. Étapes propres au **pré-pilote** non jouées par la v53 : rédacteur, rendus et contrôle d'ancres (S6), relecteur et témoins
   ambigus (S20), contrôles de forme S18/S19, étage 1 (analyseur), antériorité M6 (réductible : le moteur de budget la sait
   traiter) et M6b, axe 7 (table seule, bardeaux des huit questions), second lecteur et adjudicateur de M5, lecture des
   classes plantées (clé des classes). Les fonctions d'étalonnage M1 et M4 existent ; leur chaîne avec les témoins, non.
3. Mode « modèle » du bras Gu et Krenn ; plongement figé de M3 ; lecture du désaccord par paire.
4. Consignes figées (juges, aiguilleur, proposeur, passe « tableau », fusion, lecteurs) au contrat de sortie ci-dessus.
5. Étage réel sur la machine jetable : rejouer `test_v52b_02` et la suite sous vrai `bwrap` là-bas.
6. Seuils et décisions du brouillon 6 (S1 à S31, D-e à D-j, L1 à L7) à geler par Lazar, puis configuration réelle, ligne de GO
   au plafond, devis.
