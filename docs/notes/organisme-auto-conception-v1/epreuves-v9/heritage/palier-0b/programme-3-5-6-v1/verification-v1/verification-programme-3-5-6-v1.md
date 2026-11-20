# Vérification du programme des étapes 3, 4, 5 et 6 du palier 0b — v1

Vérificateur neuf, modèle S (n'a écrit ni le programme, ni le code v6, ni leurs textes). 2026-11-20. Pièce de travail (classe C). Rien n'est lancé en vrai, aucune graine décisive, aucune écriture dans le dépôt.

## Verdict : **À corriger** (un seul point, sans code v7)

La condition 5 de la liste d'arrêt n'est appliquée par aucun programme ni par le code v6 (§ 4). Tout le reste est conforme.

## 1. Empreintes et table
Mandat `59370f4a…`, programme `6fc6fa3f…`, essais `018060cf…`, rapport `ef1196cd…`, table `c160ad8e…` : égaux à ceux annoncés ; compagnons OK ; table du sous-dossier (4 lignes) : 4 OK. Copie du code v6 utilisée : table `639335b9…`, 0 écart.

## 2. Essais rejoués
Sur copie, avec le code v6, `PYTHONPATH=src`, `HERITAGE_DEPOT`, `HERITAGE_COPIE_ORGANISME` (dossier `orchestrator/` du code de l'organisme au commit du palier 0a ; la garde 17 est jouée dessus, `tentatives_comparees` > 0) : fichier d'essais du programme plus l'essai final « aucune graine décisive » du code v6 : **22 passés, 0 échoué (841 s)**. Couche « essai-de-forme » seule ; seules les étiquettes de cette couche sont dérivées (essai final du fichier).

Essais à moi (fichier `essais_verificateur_3_5_6.py`, rapides, fonctions du code v6 remplacées le temps d'un essai, rien de tiré) : (a) l'arrêt de l'étape 4 planté pour chacune des cinq classes nommées (`ArretMecanique`, `ArretFrequences`, `DesaccordOrganisme`, `ArretGenerateur`, `ArretEtapes`) : cause et manifeste « arrêt » écrits et scellés, étapes 5 et 6 non jouées : **5 sur 5 passés** ; (b) une classe non nommée (`OrganismeIndisponible` en cours d'étape 4) se propage sans rien écrire (silence n° 6 du rapport, conforme) : passé ; (c) condition 5 de la liste d'arrêt : **échec**, voir § 4.

## 3. Seules fonctions du code v6
`lancer_etapes_3_5_6_v1.py` : `GR.Autorisation` l. 77 ; `GR.verifier_scelle` l. 79 ; `GR.Graines` l. 142, 151, 183, 194 ; `OR.EtageOrganisme` l. 143 ; `MO.audit_du_generateur` l. 155 ; `EP.lancer_etape_4` l. 169 ; `FR.geler` l. 184 et `FR.lire_gelees` l. 186 ; `EP.etape_6` l. 199 (qui appelle `etalonnage.geler_reglages`) ; `TI.ecrire_manifeste` l. 112 ; constantes `K.*` (`SUITES_AUDIT_PAR_DOSE` 50, `PERMUTATIONS_AUDIT` 1 000, `SOURCES_ETALONNAGE` 200 000, `DOSES`) l. 152-153, 196. Code propre sans calcul : empreinte du programme, vérification de la pièce de contrôle (l. 74-86), écritures scellées (l. 95-106), dispatch des arrêts (l. 57-59, 115-122). Signatures vérifiées contre `mondes.py:624`, `etapes.py:215, 273`, `frequences.py:101, 113`. Aucune fonction neuve requise.

## 4. Lettre du texte, étapes 3 à 6
- Ordre (v13:387, v15:395) : 3 audit (50 suites par dose, couche « audit », 1 000 permutations ; générateurs des plis et des permutations dérivés par le code), 4 couche mécanique par `lancer_etape_4` (valeurs gelées, garde 17 sur la copie, jeu de la garde 27, S8 (i)), 5 gel des fréquences puis relecture sous empreinte, 6 étalonnage (200 000 sources) et gel des réglages. L'étape 4 entre 3 et 5 est bien celle du texte (« 4. Couche mécanique : … fréquences M12 … » ; B7 bis, version 12 nomme `lancer_etape_4`). Couches « audit », « mecanique », « etalonnage » disjointes (B8), racine gelée.
- Liste d'arrêt, point 2 (audit) : arrêt écrit avec le rapport joint (`mondes.py:615-620`), chaîne arrêtée ; point 4 (S8 (i), strate vide) et garde 17 : par l'étape 4 ; points 10 et 11 : dossier neuf, écritures exclusives ; point 8 : un manifeste par étape.
- **Écart : liste d'arrêt, point 5** (v13:428 = v15:436, inchangé) : « la taille de référence n'est atteignable, pour un contraste, à aucune dose non nulle ; ou la force de référence du suiveur de forme n'est pas atteignable → arrêt ». `etape_6` rend ses réglages (`EP.etape_6`, 2e valeur) ; le programme les écarte (l. 199, `_, _, sha_r`) et ne contrôle rien ; `plan_des_cases` et `etalonnage` rangent seulement « non atteignable » (grep sur tout `src/` : aucune application du point 5). Mon essai (c) plante des réglages dont K et τ de référence sont non atteignables aux deux doses et dont φ de référence l'est : la chaîne finit « tenue ». Le texte ne limite pas ce point à une étape ; il suit l'étape 6 qui en produit la donnée.
  **Correction demandée (sans code v7, sans fonction neuve)** : après `EP.etape_6`, tester sur ses réglages (K à la taille 1 aux deux doses, τ aux deux doses, φ à la force 1) la condition du point 5 ; si elle est vraie, écrire l'arrêt (cause scellée, manifeste « arrêt » de l'étape 6, avec les réglages déjà gelés inscrits), puis arrêter le programme, par le chemin `_arreter` existant ; un essai cas sain et artefact (R5). Variante, à la mère : si elle préfère que ce point soit lu à l'étape 8 ou à l'analyse, le dire à la v15 ; en l'état aucun texte ni code ne l'applique.

## 5. Gardes
Verrou du code v6 exigé avant tout geste ; pièce de contrôle présente, scellée, portant commit et empreinte du programme ; couche limitée (« essai-de-forme » pour les essais, couches des étapes sinon, refus avant tout geste, aucun refus consigné) ; tailles réduites et paramètres inconnus refusés sous les couches des étapes ; dossier neuf ; copie de l'organisme absente ou altérée (une empreinte du palier 0a) : `OrganismeIndisponible` avant toute étape, aucun dossier ; fréquences relues par empreinte et compagnon ; arrêts écrits aux étapes 3, 5, 6 (essais du développeur) et 4 (mes essais). Chaque garde a un cas sain et un artefact.

**Arrêt de l'étape 4 sans essai propre : suffisant ?** Oui quant au chemin d'écriture et à la liste des classes (mes cinq essais le montrent) ; ses gardes (S8 (i), garde 17, garde 27) ont leurs essais dans le code v6 (117 passés, 147 défauts vus). Je recommande d'ajouter mes cinq cas au fichier d'essais en même temps que la correction du § 4.

## 6. Les dix silences
1. Un programme, un manifeste par étape, arrêt qui arrête la chaîne : **juste**.
2. Garde 17 toujours jouée, chemin « non jouée, issue suspendue » non offert : **à la mère, recommandation : accepter, pas un écart bloquant**. Le texte (B2) permet de ne pas jouer la garde si la copie manque, mais alors C6 est « non établi » et l'issue ne peut pas être « lisible » ; le programme, plus strict, n'écrit rien et s'arrête avant toute étape. Aucun tirage décisif n'en dépend. À dire en v15 ; un lancement sans la garde serait un autre programme.
3. Racine et tâche de l'organisme (`mecanique|organisme|racine`, `palier-0b|etape-4`) : **juste**, à inscrire (la racine est dérivée, étiquette déterministe).
4. Ce que les étapes écrivent : **juste**.
5. Lieu des sorties (`<racine>/diag/heritage-palier-0b-v1/etapes-3-a-6/`) : **à la mère, recommandation : accepter** (conforme à l'annexe C, `diag/heritage-palier-0b-v1/`) ; le programme ne l'impose pas (dossier donné par l'appelant), la pièce de contrôle le fixe : c'est elle qui doit le dire.
6. Arrêts nommés écrits, autres exceptions propagées sans manifeste : **juste**, à dire en v15 ; dossier partiel à inventorier (R11).
7. Verrou et pièce de contrôle avant l'étape 3 : **juste** (règle de la mère de 18:08Z), à inscrire ; la pièce est lue par recherche de sous-chaînes (commit et empreinte), comme au programme 6 bis et 7.
8. Commit du manifeste pris de l'autorisation : **juste**.
9. Lieu du programme : **juste**.
10. Enchaînement : **juste**, vérifié (§ 7).

## 7. Ordre des trois programmes et passage des gelés
Ordre : 3–6, puis 6 bis–7, puis 8–9, cohérent avec l'ordre du texte (v13:387). Le programme 3–6 imprime « fréquences gelées : chemin empreinte » et « réglages gelés : chemin empreinte » (l. 214-215) ; les programmes 6 bis–7 et 8–9 prennent, dans cet ordre, `FREQUENCES SHA_FREQUENCES REGLAGES SHA_REGLAGES` : même ordre, même sens. Les compagnons écrits par `frequences.geler` et `etalonnage.geler_reglages` (« <empreinte>  <nom de base> ») sont exactement ceux que relisent `relire_fichiers_geles` (6 bis–7 l. 125, 8–9) ; la pièce de contrôle de la mère doit recopier ces quatre valeurs entre les lancements. Rien d'autre ne passe de l'un à l'autre.

## 8. Écarts à mon mandat
Aucun refus de permission, de classifieur ni de garde. Aucune liste de processus ni commande d'arrêt, aucun appel à un fournisseur, aucune écriture dans le dépôt. Un fichier d'essais à moi, dans mon dossier, sans code en ligne.

Signé : vérificateur, modèle S.
