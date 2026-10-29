# Proposition B — Tour III.1 — Règle de repli si la porte G0 n'est pas franchie

## 0. État des pièces et cadre

- **Pièce B coupée à la fin** (« … il est fini ») : je n'en reconstitue pas la suite.
- **Pièce C coupée** : elle commence en milieu de phrase, et sa numérotation saute de 11–14 à 2–5. Les sections 1 bis, 3, 8 et 9, citées, ne sont pas transmises.
- **Propositions A et C** : je ne les vois pas à ce tour. Il n'y a donc rien à attaquer ni à reprendre (B1).
- **Garde de sûreté** : rien ici ne touche une attaque, un interne de moniteur, la carte des hypothèses, le mode tenu à l'écart, les banques ou les textes d'actions. Toutes les expériences proposées portent sur des **documents de gouvernance**.
- **Statuts** : je note RAPPORTÉ (pièce X) ce que disent les pièces, que je n'ai pas audité. Je note HYPOTHÈSE ce que j'infère. Je note SUPPOSÉ ce qui ne figure pas dans les pièces, conformément à la consigne de la question. Les confiances sont des jugements de B, pas des faits.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition | Statut | Conséquence pour la règle |
|---|---|---|---|
| S1 | Le financement commence le 1er décembre « (pièce C) » | **SUPPOSÉ** : la partie transmise de la pièce C dit seulement « avant le début du financement », sans date | Les calculs de calendrier de G1 ci-dessous en dépendent |
| S2 | Le report est unique et borné au 31 janvier 2027, 23:59 UTC | RAPPORTÉ par la question seule ; aucune ligne de registre n'est transmise | Cette décision remplace en partie GO-2026-10-20-04 (« au plus tard fin novembre »). Sans ligne de registre empreintée (R6), la clause s'appuie sur une décision non traçable |
| S3 | « Une porte ne bouge pas (section 1 bis) » est compatible avec un report | RAPPORTÉ (pièce C) ; la section 1 bis est absente | La contradiction apparente doit être levée par écrit, sinon un lecteur peut invoquer la section 1 bis contre le report |
| S4 | « Verdict au 30 novembre » équivaut à « au plus tard fin novembre » (N-027) | SUPPOSÉ | Il faut distinguer **coupure des preuves** et **prononcé du verdict** (choix C1) |
| S5 | Deux critères sur huit sont prouvés (1 et 5) | RAPPORTÉ (pièce B) | Ces deux critères restent acquis seulement si leurs empreintes ne changent pas pendant le report (HYPOTHÈSE de règle, choix C9) |
| S6 | Chaque critère s'évalue indépendamment en trois issues | **HYPOTHÈSE, probablement fausse** | Le critère 3 exige des sondes sur les organismes (i) et (ii) : sans critère 2, il est indécidable. Le critère 4 tourne « sur le même jeu d'épisodes » ; sa dépendance aux organismes est SUPPOSÉE |
| S7 | « Non concluant » est définissable pour chaque critère | HYPOTHÈSE | Le critère 8 vise « aucun chiffre non vérifié dans un document du programme » (pièce A). Son périmètre (« document du programme ») n'est pas borné dans les pièces. C'est le critère le plus exposé à une réinterprétation lors de son application |
| S8 | Le report sert à finir le travail | HYPOTHÈSE | La pièce B dit qu'« aucun organisme saboté n'existe » et que le pilote peut conclure « absence de dose diffuse avec dommage = arrêt de la banque » (R-680, RAPPORTÉ). Un échec du critère 2 peut donc être un **résultat négatif**, pas un retard. Prolonger pour retenter toucherait R3 (« aucun run visant un signe positif ») |
| S9 | Du calcul est disponible pendant le report | RAPPORTÉ (pièce A bis) : GO-2026-10-04-08 échoit le 1er novembre ; sa prolongation est un nœud à soumettre avec le devis suivant | Sans ce nœud, le report n'a aucun calcul pour les critères 2 à 4 |
| S10 | Le budget couvre le report | RAPPORTÉ (pièce B) : 90 « accordés » ; banque complète de l'ordre de 300 à 1 400 USD | Le plafond du report doit être fixé hors de la banque de G1, qui est gelée |
| S11 | Le calendrier de G1 reste cohérent | RAPPORTÉ (pièce B) : G1 à la fin du mois 4 du plan financé, mais à la fin du mois 2 selon le programme interne (écart signalé) | Si S1 tient, la fin du mois 2 tombe vers le 31 janvier, le jour même du second verdict de G0 : c'est incompatible. La fin du mois 4 laisse environ deux mois pour au moins 288 unités par mode (calcul SUPPOSÉ sur S1) |
| S12 | Un horodatage prouve qu'une preuve était scellée avant la coupure | **SUPPOSÉ** | Une empreinte sha256 prouve l'**intégrité**, pas l'**antériorité**. Il faut un horodatage externe (choix C10) |
| S13 | Le financement dépend, ou non, de G0 | SUPPOSÉ ; la pièce C dit seulement « aucune règle de repli écrite sur le palier financé » | La phrase pour le financeur ne doit rien supposer sur ce lien |

---

## Point 1 — Déclencheur

### Table à trois issues par critère

Je dédouble « non tenu » en **NT-absent** (preuve non produite à la coupure) et **NT-réfuté** (preuve produite sous préenregistrement et contraire au critère). Ce dédoublement classe la *cause* de l'échec ; il ne touche aucun critère.

| Critère | Tenu (preuves) | Non tenu | Non concluant |
|---|---|---|---|
| 1 Harnais | Preuve existante (RAPPORTÉ), empreintes identiques à la coupure | Harnais modifié et non revalidé | Empreintes non vérifiables |
| 2 Organismes (i) et (ii) | Pour **chacun** : sabotage mesurable et dose-réponse, sous préenregistrement scellé et contre-lu (R1, R2) | NT-absent : un organisme manque. NT-réfuté : dose-réponse absente selon le plan scellé | Mesure faite mais préenregistrement non scellé, contre-lecture manquante ou antériorité non prouvée |
| 3 Sondes v0 | Au-dessus du plancher aléatoire apparié **sur (i) et sur (ii)**, selon le plan scellé | NT-absent : critère 2 non tenu (dépendance) ou mesure absente. NT-réfuté : pas au-dessus du plancher | Comparaison faite hors plan scellé |
| 4 Base boîte noire | Variantes par action et séquentielle exécutées sur le même jeu d'épisodes, journaux empreintés | Une variante absente, ou jeu d'épisodes différent | Identité du jeu d'épisodes non démontrable par empreinte |
| 5 Agrégateurs | Preuve existante (RAPPORTÉ), empreintes identiques | Code modifié et non revalidé | Empreintes non vérifiables |
| 6 Préenregistrement G1 | Scellé et contre-lu par une instance neuve, fichiers lus listés (R2) | Non scellé, par exemple parce que des nœuds restent ouverts : bris d'égalité d'office « non tranché », N2, N3 (RAPPORTÉ, pièce B) | Contre-lecture sans liste des fichiers lus (R2 : « sinon le signaler ») |
| 7 Préenregistrement papier C (HC1–HC3) | Idem | Idem | Idem |
| 8 État de l'art | Chaque chiffre du périmètre renvoie à un chemin et une empreinte (R6) ; pour l'état de l'art, à un PDF empreinté et une page (R7) | Au moins un chiffre non vérifié | Périmètre « document du programme » non fixé, ou document trouvé hors manifeste |

### Règle d'agrégation

**Options**

- (a) Franchie si les 8 critères sont tenus ; « non franchie » dès qu'un critère est non tenu (NT domine) ; « non concluante » s'il n'y a aucun NT et au moins un NC. Avantage : déterministe. Inconvénient : un NC masqué par un NT disparaît du verdict, d'où l'obligation de le consigner au rapport.
- (b) Tout NC rend la porte « non concluante ». Avantage : visibilité. Inconvénient : un échec net se transforme en zone grise.

**Recommandation : (a)**, avec le statut de chaque critère au rapport. Confiance 0,75.

### « Non franchie » et « non concluante » déclenchent-elles la même suite ?

**Options**

- (a) Même suite au 30 novembre : le report unique.
- (b) Une fenêtre courte de levée des NC, puis un nouveau verdict avant le report.
- (c) Même suite, **sauf NT-réfuté sur 2 ou 3 : G0 est non franchie sans report**.

**Analyse**

- (b) crée un troisième verdict ; elle viole « unique ».
- (a) permet de prolonger pour retenter une dose-réponse déjà réfutée, ce qui frôle R3 et contredit l'esprit de R-680.
- (c) : un résultat négatif scellé n'est pas un retard, et le report ne doit pas servir à le contourner.
- **Au 31 janvier**, en revanche, NC vaut non franchie (voir point 3).

**Recommandation : (c).** Borne : NT-réfuté sur 2 ou 3 au 30 novembre entraîne « G0 non franchie », sans report. Confiance 0,55 ; c'est le choix le plus discutable de cette proposition, d'où le choix C5.

### Qui prononce, sur quelles preuves

- **Qui** : un sous-agent neuf (R13), ni auteur du préenregistrement ni de l'analyse, identifié par son identifiant d'instance (esprit de R10).
- **Contre quoi** : un **préenregistrement du verdict**, scellé et contre-lu avant le 30 novembre (R1, R2). Ce document cite mot pour mot les huit critères, avec l'empreinte de la pièce A (`d5ac34db…`).
- **Ensuite** : le verdict est scellé, puis soumis au GO de Lazar.
- **Règle proposée pour le GO** : il **confirme ou suspend** le verdict, mais ne peut pas l'améliorer. Un critère NT ou NC ne devient pas tenu par décision.
- **Si aucun sous-agent neuf conforme n'est disponible**, la porte est « non concluante » (HYPOTHÈSE de règle).

**Preuves admissibles** : chemin, sha256 et horodatage externe antérieur à la coupure (S12). Rien de ce qui est daté après la coupure ne compte.

---

## Point 2 — Pendant le report (du 1er décembre au 31 janvier)

### Table de dépendance

| Critère | Continue sans dépense | Dépense, sur devis | Gelé |
|---|---|---|---|
| 2 | Écriture et scellement du préenregistrement dose-réponse (R1), avant tout run | Construction de (i) par consigne système et de (ii) par adaptateur ; mesure dose-réponse | Toute nouvelle tentative après un NT-réfuté |
| 3 | Code des sondes, run factice (`python -m controle_ia.run_factice`) | Ajustement des sondes v0 et du plancher apparié, **débloqué quand le dossier du critère 2 est scellé** (condition mécanique, pas un jugement du résultat) | Toute comparaison relevant de G1 (séquentielle contre bases) |
| 4 | Code des variantes, run factice | Exécution sur le jeu d'épisodes, même condition de déblocage | Banque complète (300–1 400 USD, RAPPORTÉ), qui appartient à G1 |
| 6 | Trancher les nœuds ouverts (N2, N3, bris d'égalité d'office), puis rédiger, sceller, faire contre-lire | Aucune | Lecture de f_A (P-9, RAPPORTÉ) ; toute expérience décisive de G1 |
| 7 | Rédiger, sceller, faire contre-lire HC1–HC3 | Aucune | Toute expérience décisive du papier C |
| 8 | Inventaire du manifeste ; vérification PDF et page (R7) | Aucune (achat d'articles éventuel : SUPPOSÉ) | — |
| 1, 5 | Aucune modification du harnais ni des agrégateurs, ou revalidation complète | Revalidation si modification | — |

### Règle de dépense bornée

**Options**

- (a) **Reliquat seul** des 90 accordés (RAPPORTÉ), sans dépense nouvelle. Avantage : aucun engagement. Inconvénient : probablement insuffisant pour (ii) et pour les critères 3 et 4 (HYPOTHÈSE), et le GO de calcul échoit le 1er novembre.
- (b) **Plafond absolu cumulé**, fixé avant le 30 novembre, séquencé : critère 2 d'abord, puis 3 et 4 après scellement du dossier du critère 2. Le dépassement arrête la tâche, sans rallonge ; le critère concerné sera NT-absent au 31 janvier. Avantage : borné et mécanique. Inconvénient : le montant est arbitraire.
- (c) **Part du budget financé** (illustratif : ≤ 10 %). Avantage : proportionnel. Inconvénient : le financement et ses conditions sont SUPPOSÉS, et dépenser les fonds d'un financeur avant G0 peut exiger son accord (SUPPOSÉ).

**Recommandation : (b).** Borne **illustrative** : 250 USD cumulés, dont au plus 150 USD (illustratif) pour le critère 2. Confiance 0,6 sur l'option, faible sur le montant.

Le plafond est une garde d'arrêt : elle doit être testée sur un cas sain et sur un artefact (R5 ; voir E4).

---

## Point 3 — Second verdict au 31 janvier 2027, 23:59 UTC

Coupure des preuves à cette heure ; prononcé dans un délai fixé d'avance (choix C1).

| Issue | Suite |
|---|---|
| **Franchie** | Les travaux de G1 commencent selon le préenregistrement scellé (critère 6). La date de G1 est fixée **dès maintenant** relativement à la date de franchissement, l'écart M2/M4 étant réconcilié (S11) |
| **Non franchie** | « G0 non franchie », définitif. Arrêt des dépenses de la piste G1 ; rapport rendu, résultats négatifs compris ; financeur informé. Toute reprise passe par un **nouveau brief, sous un nouveau nom** (R12), qui ne peut pas se présenter comme le franchissement de G0 |
| **Non concluante** | **Identique à « non franchie »**. Au second verdict, il n'existe pas de troisième voie |

**Options pour la suite de « non franchie »**

- (a) La suite ci-dessus, scellée.
- (b) Un nœud de réorientation, avec (a) comme défaut.

(b) laisse une décision au lecteur des résultats ; elle est donc « non scellable » selon les critères de lecture. **Recommandation : (a).** Confiance 0,6.

### Contenu minimal du rapport de porte scellé

1. Identifiant d'instance du sous-agent et attestation qu'il n'est l'auteur de rien (R13).
2. Chemin et empreinte du préenregistrement du verdict ; preuve que l'empreinte est **identique** à celle du 30 novembre.
3. Empreinte de la section G0 du brief, comparée à `d5ac34db…`.
4. Pour chaque critère : statut (T, NT-absent, NT-réfuté ou NC), preuves (chemin, sha256, horodatage externe), motif en une ligne.
5. Liste des documents modifiés depuis le 30 novembre.
6. Dépense cumulée, comparée au plafond, devis par devis.
7. Liste des préenregistrements et de leurs contre-lectures (R2).
8. Ligne du GO de Lazar, ou mention « suspendu ».

### Ce qui interdit un second report ou une réécriture déguisée

- **Gel par empreinte** : critères (pièce A) et préenregistrement du verdict. Toute nouvelle version porte un nouveau nom (R12) et ne s'applique pas à G0.
- **Un seul préenregistrement de verdict** pour les deux verdicts, scellé avant le 30 novembre. On ne précise pas après coup ce que veut dire « dose-réponse » ou « document du programme ».
- **Horodatage externe** : aucune preuve postérieure à la coupure n'est admise.
- **Équivalence NC = NT** au second verdict.
- **Abrogation explicite** : la règle ne peut pas empêcher une décision future du directeur, mais elle peut la rendre visible. Tout second report, ou tout changement de cette clause, s'inscrit au registre comme « abrogation de la clause de repli G0 » et est signalé au financeur. La clause ne prétend pas l'interdire matériellement, elle le rend coûteux et traçable.

---

## Point 4 — Clause scellable (≈ 147 mots)

> « Si le verdict de G0, prononcé selon R13 sur preuves scellées et horodatées au 30 novembre 2026, 23:59 UTC, puis confirmé par le directeur sans pouvoir l'améliorer, n'est pas « franchie », la porte est reportée une seule fois au 31 janvier 2027, 23:59 UTC, sur les huit critères et le préenregistrement de verdict inchangés (empreintes vérifiées), sauf si le critère 2 ou 3 est non tenu sur résultat négatif préenregistré, auquel cas G0 est non franchie sans report ; pendant le report, aucune expérience décisive de G1 ni du papier C n'est faite, et les dépenses passent sur devis dans un plafond cumulé fixé avant le 30 novembre, dont le dépassement arrête la tâche ; au 31 janvier, « franchie » ouvre G1, et tout autre verdict, « non concluante » compris, vaut définitivement « G0 non franchie », sans second report ; toute modification ultérieure de cette clause est consignée comme abrogation et signalée au financeur. »

## Point 5 — Phrase pour le financeur (40 mots)

> If our readiness gate (G0) is not passed on 30 November 2026, it is re-assessed at most once, on unchanged criteria, by 31 January 2027; no G1 experiment runs meanwhile, and any outcome other than 'passed' stands as 'not passed'.

La phrase ne promet ni résultat ni lien avec le financement (S13). « At most » couvre l'exception NT-réfuté.

## Point 6 — À décider maintenant (liste fermée)

| # | Choix | Recommandation de B | Confiance |
|---|---|---|---|
| C1 | Coupures : preuves à 23:59 UTC le 30 novembre et le 31 janvier ; délai de prononcé | Délai de prononcé fixe, illustratif : 3 jours | 0,6 |
| C2 | Inscrire au registre la décision du 29 octobre (report unique), en levant S2 et S3 | Oui, avec empreinte | 0,85 |
| C3 | Préenregistrement du verdict G0 : définitions T, NT-absent, NT-réfuté, NC ; scellé et contre-lu | Oui, avant le 30 novembre | 0,8 |
| C4 | Agrégation « NT domine » | Oui | 0,75 |
| C5 | NT-réfuté sur 2 ou 3 au 30 novembre : non franchie sans report | Oui | 0,55 |
| C6 | Périmètre du critère 8 : manifeste des documents du programme à la coupure ; document trouvé hors manifeste = NC. **Risque « hors cadre »** si le manifeste rétrécit le texte du critère : Lazar doit juger que c'est une procédure, pas une réécriture | Manifeste exhaustif tiré du dépôt, pas choisi à la main | 0,5 |
| C7 | Plafond de dépense : montant, source, séquençage ; prolongation de GO-2026-10-04-08 | Option (b) ; montant à fixer par Lazar | 0,6 |
| C8 | Rôle du GO : confirme ou suspend, n'améliore jamais ; défaut si le GO est absent au délai | Défaut = verdict tel quel | 0,65 |
| C9 | Sort des critères 1 et 5 en cas de modification du code | Revalidation complète obligatoire | 0,8 |
| C10 | Moyen d'horodatage externe des sceaux | À choisir ; SUPPOSÉ indisponible aujourd'hui | 0,7 |
| C11 | Suite de « non franchie » au 31 janvier : option (a) scellée | Oui | 0,6 |
| C12 | Date de G1 relative au franchissement ; réconciliation M2/M4 | Fixer un écart relatif ; trancher l'écart M2/M4 | 0,7 |
| C13 | Texte de la phrase au financeur | Point 5 | 0,7 |

---

## (b) Expériences décisives sur la règle elle-même

Tous les chiffres de cette section sont **illustratifs**.

### E1 — La règle est-elle univoque ?

- **H_A** : appliquées par des sous-agents neufs indépendants, la table et l'agrégation donnent la même issue.
- **H_B** : elles laissent une marge d'interprétation.
- **Protocole** : 40 dossiers de gouvernance synthétiques, dont 10 à la frontière T/NC/NT (par exemple une contre-lecture sans liste de fichiers). Trois sous-agents neufs par dossier.
- **Métrique** : accord exact sur l'issue de la porte et sur le statut de chaque critère.
- **Seuil** : 0,95 d'accord sur l'issue.
- **Contrôle négatif** : la même procédure avec une clause volontairement vague (« critère suffisamment avancé »). L'accord doit y chuter sous 0,7. Sinon, l'instrument est insensible : les agents convergent par a priori.
- **Issues** : un accord sous le seuil falsifie H_A, et la clause n'est pas scellable en l'état. Un accord au-dessus du seuil **et** un contrôle négatif bas falsifient H_B.

### E2 — La contre-lecture détecte-t-elle une réécriture déguisée ?

- **H_A** : la contre-lecture neuve (R2) détecte une réinterprétation plantée dans un brouillon de préenregistrement de verdict, mieux qu'une vérification mécanique.
- **H_B** : elle ne fait pas mieux que le diff mécanique.
- **Cas** : 20 brouillons honnêtes et 20 jumeaux identiques, sauf une réinterprétation (par exemple « dose-réponse » réduite à deux points, ou critère 8 réduit à l'état de l'art seul).
- **Vérification mécanique à battre** : un script qui contrôle que les huit critères sont cités mot pour mot avec l'empreinte de la pièce A.
- **Métrique** : détection sur les jumeaux et fausses alertes sur les brouillons honnêtes.
- **Seuils** : détection ≥ 0,9, fausses alertes ≤ 0,1, et un gain d'au moins 0,3 sur le script pour les réinterprétations *qui citent correctement le texte*.
- **Contrôle négatif** : les brouillons honnêtes.
- **Issues** : un gain inférieur à 0,3 falsifie H_A ; le script devient obligatoire et la contre-lecture ne compte plus comme garde contre la réécriture. Un gain supérieur ou égal à 0,3 falsifie H_B.

### E3 — Le report débloque-t-il un goulot d'argent ou d'attention ?

- **H_A** : le goulot est le calcul. Avec le plafond, des critères de dépense (2, 3, 4) passent à T au 31 janvier.
- **H_B** : le goulot est la capacité de travail. Les critères sans dépense (6, 7, 8) n'avancent pas plus que les autres.
- **Protocole** : prédiction scellée **maintenant** (R1) ; lecture au 31 janvier, sans effet sur la porte elle-même.
- **Métrique** : nombre de critères passés de NT ou NC à T, par groupe.
- **Contrôle négatif** : le groupe 6, 7, 8, qui ne reçoit aucun calcul.
- **Issues** : si le groupe 2, 3, 4 ne bouge pas alors que le groupe 6, 7, 8 bouge, H_A est falsifiée (l'argent n'était pas le frein). Si le groupe 6, 7, 8 ne bouge pas non plus, H_B est corroborée et le dimensionnement par devis était hors sujet. Cette expérience informe la gouvernance future, pas ce verdict.

### E4 — La garde de dépense arrête-t-elle quand il faut (R5) ?

- **H_A** : la garde arrête la tâche sur un artefact et laisse passer un cas sain.
- **H_B** : elle se trompe dans l'un des deux sens.
- **Cas sain** : un registre de devis conforme.
- **Artefacts** : devis compté deux fois, devis dans une autre devise, devis daté après la coupure.
- **Métrique** : nombre d'arrêts corrects. **Seuil** : 100 %, car l'instrument est mécanique.
- **Issues** : tout échec falsifie H_A, et la règle de dépense n'est pas scellable. Un succès complet falsifie H_B.

---

## (c) Instruments nommés dans la question : mesure minimale

| Instrument | Détection mesurée | Cas honnêtes appariés | Vérification mécanique à battre | Seuil (illustratif) |
|---|---|---|---|---|
| **Sous-agent de verdict (R13)** | Taux de NT ou NC rendus sur des dossiers à défaut unique : empreinte fausse, horodatage postérieur, critère 3 sur un seul organisme, chiffre sans page, contre-lecture sans liste | Jumeau identique sans le défaut ; le taux de NT ou NC rendus sur ces jumeaux mesure les fausses alertes | Script : sha256, champs présents, horodatages, présence de (i) **et** (ii) | Détection ≥ 0,95 et fausses alertes ≤ 0,05. Sur les défauts mécaniques, s'il ne bat pas le script, le script passe en premier étage obligatoire |
| **Sceau sha256** | Altération d'un octet : 100 % attendu | Fichier intact | — (mécanique pur) | 100 %. **Ne prouve pas l'antériorité** (S12) |
| **Horodatage externe** (à choisir, C10) | Rejet d'une preuve antidatée (une date de commit locale est modifiable) | Preuve horodatée correctement | Comparaison avec le registre externe | 100 % |
| **Contre-lecture (R2)** des préenregistrements (critères 6 et 7, verdict) | E2 | E2 | Script de citation mot pour mot | E2 |
| **Table à trois issues et agrégation** | E1 | E1 | Règle codée en script, appliquée aux mêmes dossiers : l'humain ou l'agent doit tomber d'accord avec le script | Accord ≥ 0,95 |
| **Plafond de dépense** | E4 | E4 | Somme automatique du registre | 100 % |
| **GO du directeur** | Non mesurable par ce protocole. Seule garde : la règle « n'améliore jamais » et la consignation | — | Comparaison du statut de chaque critère entre le verdict scellé et le GO : tout passage vers T est signalé | Tout passage NT/NC vers T sans nouveau verdict R13 = violation |

Les instruments scientifiques des critères 2 à 4 (sondes, plancher apparié, base boîte noire) sont **hors de cette cellule** au-delà de la vérification de leur scellement : la garde de sûreté exclut les internes de moniteurs.

---

## (d) Ancrage matériel

- **Modèle ouvert** : Llama-3.1-8B-Instruct (RAPPORTÉ, glossaire), pour les organismes (i) par consigne et (ii) par adaptateur de bas rang.
- **Calcul pour E1 à E4** : quelques centaines d'appels de sous-agents sur des documents courts. Coût illustratif : 5 à 30 USD. Le processeur suffit pour les scripts.
- **Calcul pour le critère 2 pendant le report** :
  - un GPU de 40 à 80 Go ;
  - adaptateur sur 8B : quelques heures-GPU par dose (illustratif) ;
  - mesure dose-réponse : inférence sur 8B, de l'ordre de quelques heures-GPU (illustratif) ;
  - captures d'activations pour le critère 3 : du même ordre (illustratif) ;
  - à 2 à 4 USD l'heure-GPU (illustratif), la fenêtre coûte environ 50 à 250 USD (illustratif). Cet ordre de grandeur fonde le plafond proposé au point 2, sans le valider.
- **Faits budgétaires** :
  - 90 « accordés » (RAPPORTÉ) ;
  - banque complète de G1 de 300 à 1 400 USD (RAPPORTÉ), **gelée pendant le report** ;
  - GO de calcul de la phase 0 échu le 1er novembre (RAPPORTÉ), d'où le choix C7.
- **Prérequis non financier** : un moyen d'horodatage externe (C10). Coût SUPPOSÉ faible ; disponibilité inconnue.

**Ce qui peut réfuter cette proposition** :
- E1 sous son seuil, et la clause n'est pas scellable ;
- E2 sans gain sur le script, et la garde contre la réécriture repose sur un instrument inopérant ;
- E4 en échec, et le plafond n'est pas une garde ;
- C6 jugé hors cadre, et le critère 8 reste indécidable sans réinterprétation, ce qui rendrait toute règle de repli fragile au point exact où elle doit tenir.

FIN-DE-CELLULE