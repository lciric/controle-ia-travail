# Papier C — vérification de la version c2 du préenregistrement et contre-lecture du devis du pilote — v1

- Contre-lecteur : le même qu'aux deux premières passes (sous-agent Opus 5.5, `claude-opus-5-5`), le 2026-11-22.
  Branche courante, commit `c5d943392`.
- Pièces : texte c2, `b375e6e7f0633c8433b9b5f095a7b95906e3930bd046d19c535e68e153c2c682` (égale à son compagnon et à
  l'attendu) ; devis, `devis-pilote-papier-C-v1-brouillon2.md`,
  `4006973287456463d7311a7f3c28e4e03ad19d9c5c57cf0f1193ef5816a1acb9` (égale à son compagnon).
- Interdits tenus : rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; aucun nom interdit ; dans
  `registres/depenses.md`, seules les lignes de prix nommées (instances 54183350, 54298522, 61276240, 61414494, lignes
  d'octobre portant un prix horaire d'A100). Aucune dépense ; aucun refus de permission ; écrit dans ce seul dossier.

**Décompte.** Partie A (texte c2) : 0 bloquante, 1 majeure, 2 mineures (CW-01 à CW-03). Partie B (devis) :
0 bloquante, 2 majeures, 4 mineures (CD-01 à CD-06).
**Avis.** Texte c2 : **scellable après corrections** (CW-01 demande un mot de la conduite ; puis verrous restants).
Devis : **scellable après corrections**.

# Partie A — version c2

## A.1 Différentiel
Programme `travail/construire_brouillon7_relance_c2_v1.py` rejoué : sortie `b375e6e7…` (259 068 octets), journal
identique octet pour octet ; le programme ne fait que des remplacements exacts, avec gardes. `diff` c1 → c2 relu
en entier (169 lignes) : chaque bloc répond à CV-01, CV-02, CV-03, à une des trois décisions, ou à la mise à jour
d'état qu'elles entraînent (titre, état en bref, historique, verrous 1, 3, 7, 8, « GO », « Contre-lecture »).
**Aucun changement hors de la table.**

## A.2 Remarques de la vérification de c1

| Remarque | État | Lieu |
|---|---|---|
| CV-01, flux des tirages d'une condition | **levée** | précision 40 : flux propre, dérivé de la graine de l'épisode (précision 28), distinct de l'échantillonnage, à la génération comme à la relecture ; sinon sortie par la règle du point 14, motif « tirage de la condition non séparable », compté à part, non un échec du témoin |
| CV-02, « côté contexte » | **levée** | réserve 20 (a) : « par leurs consignes … (ce sont deux épisodes de la même tâche ; leurs tours et leurs observations diffèrent aussi) » |
| CV-03, famille « sans objet » | **levée** | précision 38 : une famille autre que (i) et (ii), nommée sans être jugée pour ce mode ou « sans objet », n'impose rien, sans nœud ; (i) ou (ii) non jugée reste un cas de nœud |

## A.3 Décisions portées (GO-2026-11-22-123, lu sur `origin/main` ; R-5008 : « go recos »)
- **D-21** : portée, mais au-delà de l'option recommandée : CW-01.
- **D-23** : portée à la lettre de la ligne (paragraphe neuf, Plan, section 3 ; garde 24 ; réserve 20 et précision 39
  mises à jour) ; moins que la recommandation : CW-03 ; garde 24 : CW-02.
- **D-24** : portée fidèlement au verrou 8 (« GO-2026-11-22-93 n'en tient pas lieu » ; devis en brouillon cité) ; le
  texte ne nomme toujours aucun identifiant (D-18).
- **D-22** reste une proposition à défaut ; marqueur renommé `<<MOT_DU_DIRECTEUR_D22>>`, cohérent au verrou 1 et dans
  l'état en bref.

### CW-01 — majeure — D-21 : la règle suit le résumé de la ligne d'accord, non l'option approuvée
- **Lieu** : Plan, section 8, précision 38, « Règle » ; verrou 1 ; table de traitement, section 2.
- **Citation** : « (2) sur toute autre famille que le verdict juge pour ce mode : la famille (iv) … et toute autre
  s'il y en a ».
- **Pièces** : R-5008 et GO-2026-11-22-123 : le mot de Lazar est « go recos » ; la recommandation approuvée est
  l'option (a) de `points-ouverts-pour-le-directeur-brouillon7-relance-v2.md` : « Désignée seulement si elle est
  au-dessus du plancher, à chaque dose jugée, sur (i) et sur (ii), et sur (iv) si le verdict la juge ». La phrase
  « chaque famille et chaque dose jugées » de la ligne GO est le résumé qu'en fait la mère.
- **Constat** : la version c2 prend le résumé pour la lettre et élargit la règle à toute famille jugée pour ce mode
  (par exemple (iii)). L'option que le directeur a approuvée est plus étroite. Effet pratique probablement nul (la
  famille (iii), organismes publics, n'a sans doute pas de mode « coût gonflé »), et l'élargissement est plus sévère
  pour la confirmation ; mais c'est la lettre d'une décision du directeur, et deux pièces du dépôt la disent
  différemment.
- **Correction demandée** : soit revenir au texte de l'option (a) recommandée, soit faire confirmer par la conduite
  (et consigner) que la lettre retenue est « toute famille jugée » ; dans les deux cas, aligner la ligne GO ou la
  table de traitement pour qu'une seule lettre reste.

### CW-02 — mineure — garde 24 : « nœud » ne dit pas si l'étape 2 s'ouvre
- **Lieu** : liste d'arrêt 24 ; Plan, section 3, « Bras « saboteur sans consigne » » et « Préalables » ; liste
  d'arrêt 2.
- **Citation** : « Complément du bras « saboteur sans consigne » … absent, non scellé ou non contre-lu à l'ouverture de
  l'étape 2 : nœud. »
- **Constat** : deux lectures : l'étape 2 ne s'ouvre pas (TC.1 à TC.3 attendent), ou elle s'ouvre sans ce bras et le
  nœud porte sur le seul bras. Les « Préalables » de la section 3 et la garde 2 ne nomment pas le complément.
- **Correction demandée** : écrire l'une des deux (par exemple « l'étape 2 ne s'ouvre pas ; nœud ») et l'aligner dans
  les « Préalables » et la garde 2.

### CW-03 — mineure — D-23 : le cadre recommandé du complément n'est pas porté
- **Lieu** : Plan, section 3, « Bras « saboteur sans consigne » ».
- **Citation** : « un préenregistrement complémentaire … fixe l'organisme (parmi ceux que le verdict de G0 retient),
  les cellules, les lignes et leur lecture ».
- **Pièces** : points ouverts v2 (et v1), D-23, recommandation « (a), et (c) en plus si la famille (iv) existe » :
  saboteur = organisme de la famille (ii) du mode « coût gonflé » retenu par G0, honnête = modèle de base, mêmes
  tâches et niveaux, cellules S et SP_m, HC2 et C-P4c rapportées par mode d'induction.
- **Constat** : le texte laisse au complément tout ce que la recommandation approuvée fixait ; un complément écrit
  après le verdict de G0 pourrait choisir autrement, après avoir vu les sondes.
- **Correction demandée** : écrire ce cadre dans le paragraphe (organisme de la famille (ii), et (iv) si elle existe ;
  mêmes tâches et niveaux ; cellules ; lignes rapportées par mode d'induction), le complément ne fixant que ce qui
  dépend du verdict.

## A.4 Le reste
- Aucun autre défaut, contradiction ou revendication neuve ; aucune phrase qui vise un signe. Le paragraphe du bras
  ne change aucune ligne de C-P1 à C-P6 et n'entre dans aucune correction.
- **Rien de ce qui est tranché n'a bougé** : énoncés, prédictions, marges, seuils, D-1 à D-20 intacts au `diff` ;
  changent la précision 38 (décision D-21), la précision 40 (CV-01), la réserve 20 (CV-02, D-23), le verrou 8 (D-24).
- **Validateur** : section « Contre-lecture » à remplir et dix-sept marqueurs, `<<MOT_DU_DIRECTEUR_D22>>` à la place
  de `<<MOT_DU_DIRECTEUR_D21_D22>>`, `<<MOT_DU_DIRECTEUR_H1>>` présent. Conforme.

# Partie B — devis du pilote (brouillon 2)

## B.1 Ce qui est juste
- **Décomptes** (contrôlés sur le Plan, section 1, du texte c2) : 1.2, 30 × 3 conditions × 3 juges = 270 par réponse
  imposée ; 1.3, consignes A et B : sans insertion + indices 1, 8, 16 des cinq familles + deux témoins = 18 chacune,
  alarme : 1 + famille 5 aux trois indices + famille 4 à l'indice 8 + deux témoins = 7, d'où 20 × 3 × 43 = 2 580 par
  variante ; 1.4, 60 × (1 + 80 + 16 + constat nu) × 3 = 17 640 au plus ; 1.5, 10 × 6 × 3 = 180. Justes.
- **Sources** : GO-2026-10-17-01 (« 4 heures de carte (≈ 6 USD), dans les 150 USD de GO-2026-10-04-08 », accord par
  lancement) ; GO-2026-10-20-06 et -07 ; GO-2026-11-19-74 ; GO-2026-11-22-93 ; GO-2026-11-22-123 : conformes à ce
  que le devis leur fait dire, sauf CD-02. Devis de la phase 0 (`16d71feb…`), « Instance de référence » : A100 80 Go,
  0,80 à 1,30 USD/h, central 1,00 : conforme. `registres/depenses.md` : 54298522, A100 SXM4 à 1,093 USD/h, modèle ≈ 16 Go,
  conforme ; prix d'octobre 1,08 à 1,2133 USD/h, conforme ; 61276240, 1,1833 USD/h relu, conforme ; 61414494, 1,22
  USD/h stockage compris et 0,026 USD/Go, conforme ; 54183350, 0,038 USD/Go : conforme, mais c'est une offre H100
  (CD-05).
- La ligne du § 4 suit la lettre de D-24 (ligne propre, sur devis, rien avant le GO) et garde les préalables du texte
  (scellements, addendum de lancement de D-20, accord du jour).

### CD-01 — majeure — le plafond de 10 USD « tout compris » n'est pas tenu par les arrêts du § 5
- **Lieu** : § 3 (« reste pour le réseau et le disque … 4,00 USD ») ; § 4 (« plafond 10 USD, tout compris ») ; § 5,
  troisième et quatrième puces ; texte c2, Plan, point 1.6, et liste d'arrêt 3.
- **Citations** : « réseau estimé (taille des trois modèles … × prix au gigaoctet de l'offre) plus disque au-dessus de
  4,00 USD : pas de création » ; « durée = min(4 heures moins les heures déjà consommées, ce que le reste du plafond
  permet au prix relu) » ; texte : « min(4 heures moins les heures déjà consommées, 10 USD / prix horaire de
  l'offre), strictement sous 10 USD » (par lancement, carte seule).
- **Constat** : (a) l'épreuve avant création compare à 4,00 USD fixes, non au reste du plafond : un second lancement
  retélécharge les modèles et peut porter le total au-dessus de 10 USD (6 de carte au pire, plus deux descentes et
  deux disques). (b) L'estimation du réseau oublie l'image et les roues (la ligne du 2026-10-05 les compte) et la
  remontée des sorties. (c) La règle du lanceur que le texte scelle est par lancement et sur la carte seule ; celle
  du devis est cumulative et tout compris : le lanceur scellé appliquera la première. Cas sain : un lancement à
  1,2 USD/h tient ; cas d'un prix à la borne avec un second lancement, ou d'un réseau cher : le plafond peut être
  dépassé sans qu'aucun arrêt écrit ne joue.
- **Correction demandée** : une seule règle cumulative, avant chaque création : dépensé jusque-là (relevé du crédit du
  loueur) + heures restantes × prix relu + réseau estimé (modèles, image, roues, sorties) + disque jusqu'à la
  destruction ≤ 10 USD, sinon pas de création ; pendant la marche, durée bornée par le même reste ; dire que cette
  règle est écrite dans l'addendum de lancement (qui prime pour le pilote sur la formule du point 1.6), ou demander
  la correction du texte.

### CD-02 — majeure — le § 4 dit « sans le changer » ce qu'il change
- **Lieu** : § 4, paragraphe qui suit la ligne proposée.
- **Citation** : « Ce que cette ligne reprend sans le changer : … les 10 USD au plus par lancement de la délégation
  GO-2026-10-20-07, qui deviennent ici un plafond pour le pilote entier ».
- **Constat** : changent, par rapport aux accords repris : (1) les 10 USD par lancement deviennent 10 USD pour le
  pilote entier, alors que GO-2026-10-17-01 chiffrait le pilote à « ≈ 6 USD » (le plafond du pilote monte donc, en
  montant, de ≈ 6 à 10 USD) ; (2) deux lancements au plus (absent des accords) ; (3) un plafond de prix de 1,50 USD/h,
  dérivé de « ≈ 6 USD » pour 4 heures (une approximation devenue une borne) ; (4) le compte hors des 150 USD de la
  phase 0, contraire à la lettre de GO-2026-10-04-08 (« à l'intérieur de ce plafond ») et de GO-2026-10-17-01 (« dans
  les 150 USD ») ; (5) l'échéance propre. Le directeur ne voit pas d'un coup d'œil ce qu'il accorde de neuf.
- **Correction demandée** : une table « accord d'origine → ligne proposée » pour la durée, le montant, le nombre de
  lancements, le prix horaire, l'enveloppe et l'échéance ; dire « dérivé » pour 1,50 USD/h ; garder la question de
  l'enveloppe comme une option posée au directeur, avec la lettre actuelle en regard.

### CD-03 — mineure — une instance arrêtée continue de coûter
- **Lieu** : § 5, « l'instance s'arrête par son identifiant » ; « Récupération avant destruction ».
- **Pièce** : `registres/depenses.md`, instances 54183350 et 54298522 : disque d'une instance arrêtée facturé (≈ 0,074
  et ≈ 0,027 USD/h) tant qu'elle existe.
- **Correction demandée** : un délai maximal entre l'arrêt et la destruction (après le versement scellé), compté dans
  le plafond de CD-01.

### CD-04 — mineure — aucune durée attendue, alors que des débits existent peut-être au dépôt
- **Lieu** : § 3, « heures de carte, attendu » ; § 8.
- **Constat** : le brouillon 1 renvoyait aux débits de lecture de P3 et des notations de T0.5 cités par
  `registres/depenses.md` ; le brouillon 2 dit qu'aucun débit n'est lisible. Les descentes (trois modèles, ≈ 45 Go)
  se comptent aussi dans les 4 heures. Sans attendu, un directeur ne sait pas si 4 heures suffisent ou si un second
  lancement est probable.
- **Correction demandée** : un ordre de grandeur sourcé (ou dire où il manque), et une garde de projection : après les
  N premières lectures du point 1.4, si la durée projetée dépasse les heures restantes, arrêt avant de dépenser plus,
  et nœud.

### CD-05 — mineure — « offre conforme » n'est pas défini
- **Lieu** : § 2, « la moins chère des offres conformes ».
- **Constat** : ni taille de disque (trois modèles ≈ 45 Go, plus image et sorties), ni type exact (A100 80 Go, SXM4
  ou PCIe), ni critère de fiabilité. Le relevé 0,038 USD/Go du 2026-10-04 vient d'une offre H100 (54183350), non A100.
- **Correction demandée** : définir la conformité (carte, mémoire, disque minimal, fiabilité minimale) ; dire de quelle
  offre vient chaque relevé.

### CD-06 — mineure — le prix relu ne suffit pas à suivre la dépense
- **Lieu** : § 5, « Prix relu après création au-dessus du plafond de prix : destruction ».
- **Constat** : le réseau et le stockage ne se voient qu'à la facture ; `registres/depenses.md` écrit « aucune facture
  lue » pour 61414494.
- **Correction demandée** : relever le crédit du loueur avant la création et après la destruction (et, si possible,
  en marche), consigner l'écart comme dépense du pilote ; un crédit qui baisse plus que le reste du plafond : arrêt.

## B.2 Ce qui manque pour dire oui ou non
CD-02 (ce qui est accordé de neuf), CD-01 (une règle qui tient le plafond), CD-04 (un attendu). Le reste est sourcé.

# Ce que j'ai lu, en fait
Le message de la session ; `diff` c1 → c2 complet ; programme c2 (fonction principale ; exécuté) et son journal
(comparaison) ; table de traitement de la vérification de c1 (en entier) ; points ouverts v2 (D-21, options et
recommandation ; D-23 lu à la première passe dans la v1 et ses lignes ici) ; sortie du validateur rejouée ;
`origin/main:registres/go.md`, ligne GO-2026-11-22-123 ; `origin/main:registres/decisions.md`, ligne R-5008 ; le devis
brouillon 2 (en entier) ; le devis brouillon 1 (80 premières lignes, `git show` de la branche du 19 novembre) ;
`registres/go.md`, lignes GO-2026-10-04-08 et GO-2026-10-17-01 (les autres lues aux passes précédentes) ;
`livrables/premier-rendu-v1/devis-v1.md`, ligne « Instance de référence » et empreinte ; `registres/depenses.md`, les
seules lignes de prix nommées. Le Plan, section 1, du texte (lu en entier à la première passe ; non modifié par c1 ni
c2 au `diff`). Non lus : la note des différences c2 au-delà de son nom, les additifs et le journal v3 du rédacteur,
les points ouverts v3, le contrôle des empreintes c2.

# Avis d'ensemble
- **Texte c2** : CV-01 à CV-03 levées ; D-23 et D-24 portées à la lettre de la ligne, D-21 au-delà de l'option
  approuvée. **Scellable après corrections** (CW-01 tranchée par la conduite, CW-02 et CW-03), puis les verrous
  restants.
- **Devis** : décomptes et sources justes. **Scellable après corrections** de CD-01 et CD-02, et des mineures ou leur
  refus écrit.
