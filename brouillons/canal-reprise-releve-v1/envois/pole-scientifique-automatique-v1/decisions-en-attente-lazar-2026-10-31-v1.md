# Décisions en attente de Lazar — 31 octobre 2026, matin — v1

conv-audit (Fable 5.1), rédigé pendant l'autonomie de nuit (R-644), à partir des registres R-647 à R-682. Aucune porte franchie, aucun nœud tranché, aucune dépense. Tout ce qui touche un préenregistrement ou une porte : **aucun défaut à 48 heures**. Les décisions proposées par session-depot sont rappelées en § 6 avec leurs défauts à elle.

## Verdict (trois lignes)

1. **Bisociation à deux espaces v2 : NON CONCLUANT** (verdict R13 scellé, R-660) — la validation du générateur échoue sur V5 par un défaut de **définition** du critère, pas du code (diagnostic R-661). Nœud : nouvelle version du préenregistrement, options ci-dessous.
2. **Pré-pilote de la course 2 : brouillon 7 présentable** (R-668), quatre contre-lectures ; porte entière d'emblée 0,16, nœud 0,66, coût 30,6 USD en configuration recommandée ; **S1 à S31, D-e à D-j, L1 à L7 à geler** ; S17 : 45 / 40 (brouillon) contre 50 / 45 souple (devis v6 de session-depot).
3. **Orchestrateur v53 → v54 (→ v55 en cours)** : lançable après corrections pour une génération de la course 2 (CL18, CL19) ; **une question de principe (A21) à trancher**. Semi-réel : brouillon 3 (DL-1 à DL-9), bloqué par le verdict du collisionneur sur la question 6 (Kimi coupé cinq fois).

## 1. Bisociation à deux espaces (nœud, R-660, R-661)

**Décision** : quelle version 3 du préenregistrement, sachant que V5 (écart maximal entre moyennes par statut d'étiquette ≤ 0,5) ne peut pas passer par le générateur permis.
**Enjeu** : V5 vaut 2,87 en M_bien ; la cause est que les statuts à étiquette d'opérateur (vrai d'opérateur, surface) suivent la loi de v1 qu'aucune règle n'égalise ; aucune variante du générateur permise par S16a ne descend sous 0,5 (meilleure : 1,29) ; le seuil 0,5 est du niveau du bruit entre statuts (erreur type 0,3–0,6). Toute option change un critère gelé **après lecture** de la validation (pas des contrastes de décision, qui n'existent pas).
- (A) v3 : V5 redéfinie (fréquence de l'étiquette du concept rare planté, vue des deux côtés : 0,137 / 0,134 sur mondes d'essai) ; avantage : passe ; inconvénient : contrôle presque acquis par construction, ne dit plus rien de l'étiquette que voient les bras.
- (B) = A + ancienne grandeur rapportée sans seuil, écart déclaré en toutes lettres, graines de validation nouvelles (les indices 0–299 ont été lus) ; avantage : trace honnête, le lecteur voit l'ancienne mesure ; inconvénient : une version de plus.
- (C) corriger le générateur seul : **insuffisant**, écarté par le diagnostic.
- (D) restreindre V5 aux trois statuts rares : passe M_bien (0,33), échoue M_moyen (0,83).
**Recommandation : (B), confiance 0,6.** Coût : processeur seul ; brouillon → contre-lecture (modèle ≠ auteur) → gel ≈ une demi-journée. Pièces : `experience-v2/lancement-v2/verdict-validation-v1.md` (`f5bf86b9…`), `lecture-validation-v1.md`, `diagnostic-v5-v1/`.

## 2. Pré-pilote de la course 2 — brouillon 7 (R-668)

Fichier : `pre-pilote-course-2-v1/preenregistrement-pre-pilote-course-2-brouillon7.md` (`799b9ca9…`), section « Décisions à Lazar » (table complète S1–S31, D-e à D-j, L1–L7 avec recommandation, confiance et alternative). Ici les seules qui changent le plan :
- **S17 plafond ; arrêt d'étape** : brouillon 7 recommande **45 ; 40** (0,65) ; **devis v6 de session-depot recommande 50 ; 45 avec plafonds de relais rendus souples** (R-866, R-868 : à 45 dur, une étape protégée bute avec 0,99 ; souple : sacrifice 0,17, coupure 0,063, médiane 40,6). Les deux lectures sont compatibles (le brouillon 7 a retenu « plafond de relais = réservation, S17 seul plafond qui coupe », CP5-09, DEP4). **Ma recommandation révisée : 50 ; 45 souple (devis v6), confiance 0,6** — le brouillon 7 passe à 50 ; 45 par une ligne, les probabilités sont à rejouer (script v6 → v7).
- **D-g** antériorité non citée : (a) vide déclaré / (b) 4 fiches M6b, S30 = 3 sur 4, étape protégée hors porte, ≈ 1,6 USD. Reco (b), 0,6.
- **D-h** gel : (a) attendre l'annexe scellée du bras méta / (b) geler à deux bras (C12 0,86, porte 0,14). Reco (a), 0,55 — **mais voir § 3 : l'annexe a un problème de fond (CA1-05)**.
- **D-i** fonds : (1) 28 uniques / (2) 28 + 4 rendus appariés pour la mémoire anti-redite seule (+0,5 USD) / (3) 24 dont 4 doublés. Reco (2), 0,6 ; lecture de « dix fonds écrits deux fois retirés » (R-634) à confirmer.
- **D-j** Gu-Krenn sans condition de reproduction (R-635 était une recommandation, pas une décision) : oui / non. Reco oui, 0,7 — **mais R-873 : leur graphe ne contient pas le vocabulaire du contrôle des IA** (probe, steering, monitoring, alignment n'existent qu'au sens physique) : le substitut S31 ne peut pas s'appuyer sur leur graphe pour notre sous-domaine ; il faut une source de « jamais reliés » propre à nous (moisson OpenAlex, R-863) — S31 à geler avec cette source.
- **L1 à L7** (lectures de l'auteur) : au format de décision dans le brouillon ; confiances posées par l'auteur du brouillon 7 (0,6–0,7).
- Chiffres (sortie v6) : texte de base porte d'emblée 0,16, nœud 0,67, total 0,20, coût 28,4 ; configuration recommandée (D-g b, D-i 2) 0,16 / 0,66 / 0,20, coût 30,6, médiane 38,7.

## 3. Annexe des paramètres du bras méta v1 — brouillon 1 (R-672, R-675)

Fichier : `pre-pilote-course-2-v1/annexe-bras-meta-v1-brouillon1.md` (`3a2e8dc2…`), contre-lecture Sonnet « soumettable après corrections ».
- **CA1-05 (majeur, nœud)** : avec la grille de 6 niches, la bande d'éloignement [2 ; 3] et « canal faible » ≤ 1, **4 paires de niches sur 15** sont dans le profil → **zéro paire dans le profil avec 0,59–0,67 à 6 fiches, 0,25–0,36 à 10 fiches** : le pré-pilote n'éprouverait souvent que le repli. Élargir la bande à [2 ; 4] n'aide presque pas. Options : (a) accepter le repli comme mesure du bras méta au pré-pilote (la course, à plus de fiches, éprouvera le profil) ; (b) 15 fiches au pré-pilote (zéro avec 0,06 ; sur devis, + ≈ 5 fiches × trois juges) ; (c) toucher R-638 (profil moins strict). **Reco (a) avec journal du nombre de paires dans le profil, confiance 0,5** ; (b) si tu veux que le pré-pilote éprouve le profil lui-même.
- **CA1-04** : l'annexe exclut les **jeux de données** du compte de « structure commune forte » alors que R-638 les nomme (raison : le texte I impose presque les mêmes à toutes les fiches). À trancher : garder R-638 à la lettre ou accepter l'exclusion.
- CA1-01 (paire n1–n2, fusionnées par le programme, dans le profil) et CA1-03 (niche « bornes et théorie » dans aucune paire du profil) : corrections de grille au brouillon 2, sans décision.
- Approbation finale de l'annexe = toi, après brouillon 2 et contre-lecture (A20 : sans annexe scellée, bras méta non lancé).

## 4. Épreuve semi-réelle des méthodes d'identification — brouillon 3 (R-676)

Fichier : `prereg/brouillons/preenregistrement-identification-semi-reel-v1-brouillon3.md` (`1a229998…`). Neuf décisions DL-1 à DL-9 (toutes au format, aucun défaut), dont : DL-1 volet B dans le théorème de Khemakhem (B-θ décide, B-hors descriptif ; reco option 2, 0,65) ; DL-2 5 graines par réseau, budget ≈ 111–140 h de processeur (reco 0,55 ; calendrier avant G0 incertain) ; DL-4 CITRIS en gradation 3 (0,85) ; DL-6 PDF à obtenir avant gel (Runge 2019 PCMCI ; Peters-Bühlmann-Meinshausen 2016 ; Reisach 2023 ; Shimizu 2006/2011) ; DL-9 témoin T2b redéfini sur la règle d'orientation de chaîne de Reisach ou retiré (reco redéfini, 0,55). **Bloqué** par la section « verdict du collisionneur sur la question 6 » : tour à 7 cellules sur 12 (Kimi coupé cinq fois, R-871) → décision de session-depot à toi : absence de Kimi ou reprise de jour.

## 5. Orchestrateur v53 → v54 (→ v55) (R-670, R-673, R-677, R-679)

- v54 : lançable après corrections pour une génération de la course 2 ; non lançable pour le pré-pilote complet (pièces manquantes : analyseur de l'étage 1, résultats externes scellés, consignes figées, fiches d'antériorité, source S31, annexe approuvée, DEP4, ligne de GO). v55 (corrections CL19 sans décision) en cours.
- **CL19-03 (principe, A21)** : le code lit par programme la clé des classes **avant la fin d'É9** (É5 : témoins ambigus S20/A6, contrôles S19 ; É9 : strates de réduction). Le brouillon 7 se contredit : É5 est impossible sans la classe des témoins. Options : (a) amender A21 et la ligne 30 : lecture par programme permise, journalisée au coffre (horodatage, rôle, comptes seuls), aucune lecture humaine ni par un modèle ; en É9, liste de réduction scellée sans lecture de la clé d'antériorité (c'est ce que fait la v55) ; (b) A21 à la lettre : déplacer É5 après É9 (les témoins ambigus ne seraient plus retirés avant les juges : change M1). **Reco (a), confiance 0,7.**
- Choix de code à confirmer (LISEZMOI v54, CL19 G) : 1 (portée du plafond S17 par génération, ligne de GO ≥ N × S17), 4 (appel au-delà de son délai jamais lu), 5 (garde de Kimi au pré-pilote = mesure après É9, pas arrêt en route), 8 (adjudicateur en É7a seul), 10 (S18/S19 à geler au préenregistrement, pas dans le code). Tous rendus configurables « À REMPLIR » ; recommandations dans le LISEZMOI.

## 6. Décisions proposées par session-depot (ses défauts, pour mémoire)

- **Synthèse du collisionneur, lot bisociation** (R-867) : 1 six garde-fous obligatoires (défaut (a) 2 nov. ≈ 00:30 UTC) ; 2 ordre de départ (c) base de ponts et Gu-Krenn en parallèle (défaut) ; 3 devis carte graphique Gu-Krenn (aucun défaut : dépense) ; **4 nœud : « transition de phase » retiré des préenregistrements sur littérature réelle jusqu'à E2′** (aucun défaut : énoncé) ; 5 G close par lecture (défaut (a)) ; 6 erratum (défaut (a)) ; 7 pas de devis d'essaim maintenant. Mon avis : d'accord sur 1, 2, 4 (c), 5, 6 ; mes réponses v2 (R-671) les appliquent déjà.
- **Devis v6** (R-868) : pré-pilote 50 / 45 souple ; course 2 plafond total 160 USD séquencé ; 24 fusions — dépenses sans défaut.
- **Machine jetable v3** (R-868) : GO proposé 10 USD, location = nœud (compte, machine).
- **Absence de Kimi** aux tours 6 et 7 ou reprise de jour (R-871).
- **D-GK-1** (R-873) : fenêtre du test B de la reproduction Gu-Krenn.
- Messages n° 214 à 217 de session-depot « à conv-audit » : **introuvables** sur main et sur sa branche (R-682) ; demandés (n° 271).

## 7. Prononcés et errata de la nuit (pour information)

- « Bettencourt allumage » : le mot « ignition » n'existe pas dans arXiv 1504.00319 (transition topologique de connectivité des coauteurs, présentée prudemment) ; R0 > 1 est dans physics/0502067 (invasion d'une idée). **« Allumage » reste ta métaphore** (R-671).
- Khemakhem : nk + 1 valeurs de la variable auxiliaire (la relecture 6 et Fable disaient 2k + 1 : faux, R-650).
- Fiches : Iaria −0,217 colonne (1) ; Azoulay 8,2 % avec −0,086 (erratum scellé, R-664).
- Ton projet « origines de la vie et allumage » : non reçu cette nuit ; dossier à part prévu, lecteur neuf.
