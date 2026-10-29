# Contre-lecture (R2) de la table de dépendance « critères de G0 → travaux », v4

**Déclaration.** Je n'ai écrit ni la v4 ni son script, ni aucune version antérieure, ni aucune contre-lecture de cette lignée. Modèle : Sonnet 5.5 (sous-agent neuf),
**même famille que l'auteur de la v4 (Sonnet 5.5) et que le contre-lecteur de la v3** ; Fable indisponible : des erreurs corrélées sont possibles et le classement à
l'aveugle ci-dessous ne les exclut pas. `date -u` : début 2026-10-29 22:23:02 UTC ; relevé avant l'écriture du rapport 22:34:15 UTC. Interdits tenus : rien lu sous
`donnees/`, ni `prereg/P3-consignes-v1.md`, ni `diag/*/traces` ; aucune branche ; aucune commande git (le script n'en appelle aucune) ; aucune dépense ; aucun fichier
existant modifié ; rien scellé (ce rapport n'a pas de compagnon `.sha256`) ; le dossier `cl-table-v4/` d'un autre contre-lecteur n'a pas été ouvert ; travail dans
`…/scratchpad/cl-table-v4-c/`.
**Empreintes vérifiées** (compagnon = recalcul) : table v4 `8226dd55562351ae8dcb641962df1e2d397c0371e5aeeac3db5dd0e7f2d6d12c` OK ; script
`11a814bbefeadca6269cd243d6ca8a5d17df929bd5f7b68d052b190bc92ab746` OK ; table v1 `e2480618…` OK ; contre-lecture v3 OK. Pièces recalculées, conformes à l'en-tête de la v4
: grille `320af9b0…`, brief `9261932a…`, T7 `a292088c…`, DP `255a364e…`, SY `527f5853…`, `R-765-R-776.md` `f6e454f3…`, `go-29-octobre.md` `9c1c7bc2…`, `CLAUDE.md`
`a2aabda8…`, P-040 `b44bf8a0…`. Mes pièces : `classement-aveugle.json` `fb2c799a59cf3661…`, `concordance-sortie.txt` `76cd1609e21bc8b2…`, `essais-sortie.txt`
`cdd9376d6172db0e…` (dossier `cl-table-v4-c/`).

## Appel correct du script
`python3 -I SCRIPT aveugle TABLE` (2 arguments) ; `python3 -I SCRIPT concordance TABLE FICHIER` ; `python3 -I SCRIPT verifier TABLE_V4 TABLE_V1 DEC` avec **DEC = fichiers
de décisions séparés par des virgules** (ici `registres/decisions.md,…/R-765-R-776.md`) et V1 = `table-dependance-criteres-G0-travaux-v1.md`. L'appel `verifier TABLE .`
n'a que deux arguments : « arguments : D V1 DEC … » est le refus voulu (pas un défaut). Sortie obtenue : `OK 58 lignes dérivées vérifiées une à une, 50 lignes de travaux
contrôlées, 19 produits`.

## 1. Classement à l'aveugle
**Protocole et réserve.** J'ai classé les 50 lignes depuis la sortie du mode `aveugle` (jetons `[H]`, `[REJEU]`, `[IND]`, d1, d2, préalable retirés), le brief l. 106-201
et 214-249, la grille, T7, P-040, la décision de pilote, N-025, N-028, N-035 et R-262/R-268/R-450/R-453/R-462/R-478, avant de lancer `concordance`. **Mon aveugle est
entaché** : un premier `grep` sur la table a affiché les 90 premiers caractères des lignes `| W` et `| P-` ; j'ai ainsi vu la classe de W26 et W27 (F), les produits de
W21 et W33, le début de ceux de W20, la colonne « producteur » du § 3 et le premier consommateur de plusieurs produits. J'ai ensuite lu le § 2 (définitions) et la colonne
« chemin » pour connaître le vocabulaire des produits. Les produits sont donc la mesure la moins indépendante ; classe et « sert » le sont davantage (sauf W26, W27, W33).
**Taux de concordance** (`concordance`, 50 réponses, 19 écarts) : **31/50 lignes identiques = 62 %**. Par dimension : classe 43/50 (86 %), « sert » 46/50 (92 %), produits
34/50 (68 %). Sans les arêtes † vers P-T04 (déduites « non écrites par une source », donc non reproductibles à l'aveugle par construction) : 42/50 = 84 %. Les 10 lignes
datées du 29 octobre ouvertes par défaut (W03, W22, W34, W35, W36, W42, W43, W44, W45, W49) sont toutes classées I par moi aussi : le soupçon « ouvertes faute de source »
n'est pas confirmé par ce test (réserve : même famille de modèle, descriptions seules).
**Écarts, ligne par ligne, et qui a raison selon la source.**
| lignes | moi / table | raison |
|---|---|---|
| W08 | sert 5 / « — » | table : B l.144 dit « première brique du papier A », G l.458 ne range pas la note parmi les preuves du critère 5 (A2) |
| W15 | + P-7 / sans | table : G l.235, l.477-478 lient P-7 au run des épisodes ; W15 n'en lit pas (mon ajout est une inférence) |
| W20, W21 | + P-T04 / sans | table : B l.141 et PG n'écrivent que les agrégateurs (P-T03†) |
| W22, W42, W23 (sert) | sert 6 / « — » | table : PG l.1-7 est une « proposition pour le brouillon 4 », pas une preuve du critère 6 (A2) ; L9 compense |
| W28, W29 | I / K (P-T03, P-NM, P-EA ; P-EA) | table : B l.335 « travaux connexes uniquement à partir de l'état de l'art vérifié », B l.144 note = première brique du papier A |
| W11, W46, W47, W51 | I / K P-T04† | arête † : défendable pour W11 (E l.44 : pilote « en préparation », donc un run) ; pour W46 et W47 la source (P-040 l.15-16 : A « rejoue des épisodes publiés », B « en lecture seule ») ne dit rien du harnais |
| W14, W16, W17, W19, W23, W48 | sans P-T04 / avec † | idem ; douteux pour W19 (bases boîte noire sur des épisodes existants) et W14 (« boîte noire seule ») |
| W24 | K P-PIL / F (d1) | **non tranché** : DP l.43 ne dit pas que la banque cite un préenregistrement de G1 ou du papier C ; la source PC n'a pas été relue par l'auteur (CT4-07) |
Bilan : table juste sur la source pour 8 lignes (W08, W15, W20, W21, W22, W28, W29, W42), défendable par la règle † pour 10, non démontrée pour 1 (W24). Treize des seize
écarts de produits touchent la seule arête P-T04† (14 lignes la portent ; sans effet tant que P-T04 est présent et « établi », fermeture seulement si une version nouvelle
devenait négative).

## 2. Constats CT3-01 à CT3-12 : traités comme déclaré ?
Oui pour les douze, vérifié dans le texte, par `verifier` et par mes altérations. CT3-01 : L2bis et scénarios 6-7 (réserve en CT4-09). CT3-02 : L9 et § 9 (3) (réserve
CT4-02). CT3-03 : § 6.5 ; les dix lignes de GO recopiées sont identiques à `go-29-octobre.md` (plafonds, échéances 2026-11-05, GO-11 au 29 octobre). CT3-04 : voir CT4-01.
CT3-05 : ‡ sur P-V6 pour W16, W19, W21, présent aussi dans les cellules produits ; l'altération « ‡ retiré » est détectée. CT3-06 : W18 « scellement », P-6 défini, règle
« chemin non nommé ou introuvable = absent », motif par version `v*` ; `tester` rend aujourd'hui `abs=` de 16 produits sur 19 (P-T04, P-T03, P-NM présents). CT3-07 :
`feuille` appelle `verifier` ; producteur altéré, ligne `k:9` parasite, citation changée sont maintenant détectés. CT3-08 : partielle (voir § 1 et § 7 de la table ; ma
classification à l'aveugle est la pièce qui manquait). CT3-09 : chaîne W13 → W14 → W50 → W41 présente dans les cellules et dans la feuille de l'état actuel (W14, W50, W41
fermées tant que P-6a, P-6a-res, P-6 sont absents). CT3-10 : P7-P8 dans W16, P5-P6-P9-P10 dans W17 ; les numéros de ligne de T7 (l.65-68, l.71-72, l.69-70, l.73-74)
correspondent. CT3-11 : liste fermée des dépenses, étape définie par le parent du commit, format fermé du constat (5 refus testés), objet du GO copié. CT3-12 : § 8 (2).

## 3. Constats de la v4
**CT4-01 — Clause du § 0 : conforme, avec trois imprécisions. Gravité : à corriger (texte).** Comparée par `difflib` au bloc `>` de SY § 5 : **identique mot pour mot**
(diff vide). La variante R-765/modèle B est fidèle à R-765 (« jamais retenté », « statut reporté tel quel », « ne ferme pas la porte »). Mais : (1) « Texte que la table
applique : le même, sauf le point (a) » est inexact : la table applique aussi (b) en « absent » (et non « négatif ») et (c) sans plafond, comme ses propres puces et le §
8 (3) le disent ; (2) la clause est dite « 150 mots » : 168 mots comptés (le chiffre vient de SY) ; (3) la citation de Lazar est tronquée : R-765 écrit « gèle-t-il
seulement ce critère », le § 0 « gèle seulement ce critère » entre guillemets.
**CT4-02 — § 9 (3) : le défaut ne tient pas sa promesse. Gravité : à corriger.** L'enjeu dit que sans remède le critère 6 est « inatteignable par construction » et le
défaut (1) (L9) « garde la porte atteignable ». Or L9 ne donne qu'un droit de devis ; § 6.5 (ii) exige un plafond fixé d'avance (choix n° 5 de SY, non tranché) et § 8
(10) écrit « aucune dépense du report ne passe » sans lui. Avec le seul défaut (1), W23 ne peut donc pas dépenser et W21 reste fermée. **Correction** : dire que (1) ne
vaut qu'avec le choix n° 5, ou lier les deux nœuds.
**CT4-03 — § 9 (2) : défaut conditionnel = latitude. Gravité : à corriger.** « (b), sous la condition qu'aucune lecture d'un résultat des critères 2 à 4 n'ait lieu avant
» : si la condition échoue, aucun défaut n'est écrit, et qui constate la condition n'est pas dit. Le brief demande un défaut sans latitude. **Correction** : un défaut
inconditionnel, ou une date butoir pour le mot de Lazar. À confirmer par Lazar : D-TD-2 et la date de scellement touchent la lecture de la porte ; CLAUDE.md range « porte
» parmi les nœuds sans défaut, la lignée applique pourtant un défaut à 48 heures (R-503) ; la table ne le dit pas.
**CT4-04 — § 9 (1) : le défaut (a) est une suspension sans échéance. Gravité : à corriger.** « Cesser jusqu'à ton mot ; la levée de la cause reprend la même lecture » :
aucune borne ni définition de la « levée de la cause ». SY § 2 pt 5 (« aucun état suspendu », 3/3) et sa liste « non scellable » (GO qui suspend sans échéance) vont
contre ; l'option (b) est écartée sur G l.421-424 sans dire que SY § 2 pt 2 (modèles B et C) la soutient. L'enjeu écrit lui-même qu'un arrêt « peut servir de second
report de fait » : (a) en est un. **Correction** : borner (a) par une date ou signaler l'écart à SY.
**CT4-05 — P-EA : producteur inexact, W28 et W29 fermées trop loin. Gravité : à corriger.** P-EA a quatre chemins dont `controle-tracabilite-v*.md`, produit par W05 et
W06 (colonne « fournit » : « — »), qui exigent P-G1 et P-C scellés ; le producteur déclaré est W04 seul. Conséquence : W28 et W29 (B l.335 : état de l'art vérifié)
attendent un contrôle de traçabilité de textes de G1 et du papier C que la source ne demande pas pour rédiger un papier. `tester` rend P-EA absent aujourd'hui (table des
chiffres absente) ; la rédaction des papiers A et B reste fermée jusqu'à la fin du critère 8. Resserrement non listé au § 7. **Correction** : scinder P-EA (états de l'art
+ table) du contrôle, ou justifier.
**CT4-06 — États « non concluant » et « invalide » : verrou possible, hors § 9. Gravité : à signaler.** L8 refuse gel, constat et droit de devis à C et V. Vérifié par
`feuille "A=3,4;C=2;…"` : W41 et W50 s'ouvrent sans droit de devis, W16, W19 restent fermées (‡) ; le critère 2 « non concluant » à V1 ne peut plus être repris sur devis.
SY T3-A traite « non concluant » comme provisoire. Le § 8 (7) le signale ; le § 9 n'en fait pas un nœud. **Correction** : une cinquième décision avec défaut.
**CT4-07 — W24 classée F par d1 sans source lue. Gravité : à corriger.** Les sources citées (DP l.43 : sentinelle « engageable seulement dans une campagne sous devis » ;
PC l.99, non relue) n'écrivent pas que la banque cite un préenregistrement de G1 ou du papier C. A3 n'autorise F que si d1 ou d2 « s'applique » ; ma classification donne
K (P-PIL). Effet : W24 ne s'ouvre jamais (L1) ; sens resserrant. Source à donner ou classe à revoir.
**CT4-08 — Arêtes † P-T04 : rien ne les borne. Gravité : remarque.** 14 lignes, dont W33 (N-028 : « sans nouvelle génération d'épisodes »), W47 (« en lecture seule »),
W19, W14. Toutes resserrent ; aucune déduction n'assouplit. L'audit § 7 compte 18 †, mais pas le critère qui les arrête.
**CT4-09 — Gel : critères 4, 6, 7, 8 sans classe lue. Gravité : remarque.** La grille connaît « non tenu — négatif » pour 7 et 8 (G l.343-344, l.375-376), pas pour 4 ;
L2bis ne lit que 1, 2, 3 et 5. Choix défendable (une pièce manquante se reprend en version nouvelle), non dit.
**CT4-10 — W12 (P4-instrument) : droit de devis sans « 2 tenu ». Gravité : remarque.** « sert » 3, donc devis direct (scénario `sc:abs=P-V6,P-L7;A=2,3`) alors que SY
place la dépense du critère 3 « après 2 tenu ». Justifiable (P-015 (b), G l.237 : P4 précède toute sonde, sans organisme) ; ni dit ni listé en « Assouplis ».
**CT4-11 — Script. Gravité : à corriger (mineur).** (a) Gardes rejouées : `essais` sans dépôt 46 gardes, avec dépôt **48 gardes, 0 manquante**, 27/27 altérations
détectées, code 0 ; `artefact` détecté ; `verifier` OK. Mes onze altérations propres : 8 détectées (retrait d'un †, « sert » ajouté, citation changée, F → I avec jeton
retiré, H → I, ‡ retiré, produit retiré) ; **3 non détectées** : clause (b) changée, date du 31 janvier changée, motif de chemin changé — le script ne garde ni le § 0, ni
les dates, ni les chemins ; la conformité « mot pour mot » n'est mécanisée nulle part (je l'ai faite par diff). (b) L'annexe annonce « 11 refus de `feuille` (dont 1 sur
table altérée) » : la sortie en compte **12** (11 + 1). (c) T2 est réimplémenté (`t2`) au lieu d'appeler `scellement.verifier` ; équivalent aujourd'hui, divergence
possible demain ; « dans le même commit » et la coupure M-0.6 ne sont pas testées (pas de git) : le lecteur doit fournir le dépôt à `C`. (d) La déclaration de tête dit «
ni cette table ni le script n'ont de compagnon » : ils en ont maintenant (R6).
**CT4-12 — Sources citées par abréviation. Gravité : à corriger (R6).** DP seul a son empreinte (en-tête) ; PG, PC, P40, MO, TC, DV, MSG216 n'ont ni chemin ni empreinte.
J'ai retrouvé P40 = `docs/decisions/proposition-P-040-ressources-publiques-T07-T08-v1.md` (lignes 15, 16, 17, 21-22 exactes) et PG =
`…/couche-2-conv-audit-v1/parametres-garde-delta-pour-G1-v1.md` ; PC, MO, TC, DV restent non relues par l'auteur et par moi (16 lignes du 29 octobre, dont 10 en I par
défaut).

## 4. Autres contrôles demandés
- **Quatre décisions du § 9** : toutes ont décision, enjeu, 2 ou 3 options avec avantage et inconvénient, recommandation, confiance, défaut ; (4) D-G0-8 est sans latitude
  ; (1) à (3) : CT4-02 à CT4-04.
- **Taillage sur l'état (R4)** : pas de règle trouvée taillée sur l'état du 29 octobre, hors L9 et le marquage † de P-PIL, tous deux déclarés et soumis à Lazar (§ 9 (3)).
  Contrefactuel du § 7 refait par `verifier` (aud:retrait-diff 3, tous liés à P-PIL) ; mon classement à l'aveugle confirme les 10 lignes I du 29 octobre. Les
  resserrements (†, ‡, L2 plus strict que SY sur 2 et 8) sont déclarés.
- **État actuel** (`feuille`, A = 2, 3, 4, 6, 7, 8, produits absents rendus par `tester`) : 29 ouvertes, 20 fermées, 1 à Lazar, 9 avec droit de devis ; la chaîne T0.6
  démarre par W13 seule (devis).

## Conclusion
**Scellable après corrections de texte (CT4-01 à CT4-05, puis CT4-07, 11, 12) ; aucun bloquant ; concordance à l'aveugle 31/50 = 62 % (84 % hors arêtes † vers P-T04) ;
les douze constats de la v3 sont traités ; Lazar tranche en plus CT4-06.**
