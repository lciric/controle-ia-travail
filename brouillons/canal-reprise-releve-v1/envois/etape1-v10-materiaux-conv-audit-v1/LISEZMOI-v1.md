# Étape 1 v10 — ce qu'il faut, et ce qui décide de la dépense des traits — rapport v1

Sous-agent neuf de la lignée conv-audit. **Début : 2026-10-25 23:53:04 UTC** (lu sur `date -u`). **En-tête écrit à
2026-10-26 00:10:44 UTC** (lu sur `date -u` juste avant d'écrire). Aucune commande git, aucun réseau, aucun sous-agent,
aucune dépense ; écrit seulement sous `/var/tmp/etape1-v10-v1/`. Aucun score de course lu ; aucune valeur de clé vue.

## Verdict — ce qui bloque la v10

1. **Bloquent : trois défauts de code toujours présents à `3ea95fd` (BC5-01 garde des traits, R-441 amorçage vide,
   BC5-02 séparation) et le texte v10 à écrire, contre-lire, sceller** ; aucun n'exige de dépense ; correctifs BC5-01 et
   R-441 prêts ici (différences, 5 essais ; 148 essais passent ; contre-épreuve : 4 échouent sur le code d'origine).
2. **Les traits ne sont pas à réextraire** : l'entrée du modèle à l'extraction ne portait ni l'identifiant v1 ni
   aucune marque de vérité, et les 176 textes de la v5 sont ceux de la v1 à l'octet près ; un dossier dérivé suffit.
3. **Le plan v9 ne peut pas trancher +0,10 sur la v5** (écart détectable 0,33 pour une course par bras, 0,135 à six
   paires supposées indépendantes) ; il manque une porte 0 sans dépense (sonde témoin contre les références) et un
   plancher de bruit mesuré : trois décisions reviennent à Lazar, plus une de dépense.

## Pièces, écarts et réserves

- **Message n° 52 de session-depot absent** : ni sous le nom donné, ni ailleurs sur le disque (recherche de tout fichier
  `session-depot*` sur le système de fichiers, R11 ; seule une copie du n° 45 existe ; le n° 52 du dossier est celui de
  conv-audit, 13:55 UTC, sans objet ici ; une branche `canal/session-depot-reprise-n52` n'existe que dans `.git`, que je
  n'ai pas lu). Sa liste « § 2 » est reconstituée depuis le brief (§ Contexte), R-441, R-443, R-444 et les n° 59, 61, 62.
- **Écart, déclaré** : une recherche `grep -rl` lancée sur `/home/claude/canal-conv-audit-n04` a parcouru `donnees/` et
  `diag/` ; elle a affiché des noms de fichiers correspondants, sans que j'ouvre aucun de ces fichiers et sans que j'en
  recopie un nom ici. Toutes les recherches suivantes excluent ces dossiers et les noms interdits.
- La banque v1 (`f1387a20…`) et la v5 (`28e3c728…`) ont été lues par mes scripts (`outils/`), qui n'impriment que des
  noms de champs et des comptes : aucun texte, aucun identifiant, aucune vérité n'est sorti.
- La routine de reprise du dépôt (R14 de `CLAUDE.md`) n'est pas appliquée : le brief interdit git, le réseau et toute
  écriture hors de ce dossier ; il prime pour ce travail.
- Un fait d'interface n'est pas vérifiable sans réseau : si 128 000 jetons suffisent à Fable et Opus pour rendre un texte
  à l'amorçage (point 3). Je ne l'affirme pas.

## 1. Ce qu'il faut pour la v10, point par point

Effort : heures de travail de la lignée, hors attente. « Vérifié » = lu par moi sur les copies citées.

| n° | ce qu'il faut | fait vérifié (fichier, lignes) | qui | effort |
|---|---|---|---|---|
| 1 | **Épingler la banque v5** `28e3c728…` et refuser toute autre | lanceur v6 `docs/procedures/gradient-etape1-v6/lancer_courses_etape1_v6.sh` l. 74 (`E_BANQUE=f1387a20…`), l. 158-159 (banque v1 tirée de `bffe03c`), l. 170 ; `essaim_m3/banque.py` l. 202-237 : `verifier_banque` n'épingle aucune empreinte (toute banque bien formée passe, BC2-02) | session-depot (lanceur v7) | 0,5 h |
| 2 | **Traits dérivés**, pas réextraits (point 2) : 176 vecteurs rangés par identifiant v5, aucun identifiant v1, manifeste à l'empreinte v5 | lanceur v6 l. 75 (`E_TRAITS`), l. 160 (archive `6479769`), l. 171-173, l. 265 (`--traits …/traits-16384`) ; `noyau/cli.py` l. 205 : en mode dossier, `sha256_banque` du manifeste doit égaler la banque de la course — un manifeste neuf est donc obligatoire ; brouillon `brouillons/deriver_traits_v5_v1.py` (essai : sain accepté, deux artefacts refusés) | session-depot (seule à ouvrir `donnees/`) | 1 à 1,5 h ; aucune dépense |
| 3 | **BC5-01** : égalité des identifiants traits = banque, dans les deux modes ; fichier `.npz` servi seulement s'il est décrit par un manifeste à l'empreinte de la banque | `noyau/cli.py` l. 188-190 (seuls les manquants sont refusés), l. 193-195 (mode fichier sans contrôle de banque) ; `noyau/entrainement.py` l. 403-422 (`predire` répond pour tout identifiant présent ; avec l'égalité, il ne peut plus servir que la banque) ; correctif et essais : `brouillons/correctif-noyau-bc5-01-r441-v1.diff` (cas c4 de la contre-lecture : sain accepté, « espace v3 » et « v5 + 24 » refusés ; fichier nu et autre banque refusés) | session-depot | 0,5 à 1 h |
| 4 | **R-441, amorçage vide** : une relance au plafond de relance ; plafond d'amorçage relevé | point 3 ci-dessous ; correctif et 3 essais dans la même différence | session-depot ; plafond : Lazar (D2) | 1 h |
| 5 | **BC5-04, exemples d'amorçage** : règle écrite d'avance, équilibrée par famille et par classe | `noyau/boucle.py` l. 509 (`banque["train"][:6]`), `noyau/contrat.py` l. 175 (exemples servis avec leur vérité) ; sur la v5 : 1 délégation honnête, 5 consciences (LISEZMOI-v9 l. 45-49) ; règle proposée : `brouillons/paragraphes-texte-v10-v1.md`, P3 | session-depot | 0,5 à 1 h (ou 0,2 h si composition consignée) |
| 6 | **BC5-02, séparation** en code et essayée | `--depuis` exige déjà la même banque (`noyau/cli.py` l. 272-275) ; aucun contrôle de banque pour les organismes imposés (`cli.py` l. 65-97, absents de la v9 depuis R-370) ni pour le vivier (`--pool-conception`, lanceur l. 146-174 : seule son empreinte est vérifiée) ; les parts de la v5 sont des sous-ensembles des mêmes parts de la v1 (`sorties/parts-v5-dans-parts-v1-v1.txt`) : si la disjonction du vivier `32f4b534…` a été calculée contre les 120 textes de test de la v1, elle couvre les 96 de la v5 et les 24 jumelles (à vérifier, non lu ici) | session-depot (code) ; conv-audit peut rédiger les essais | 0,5 à 1 h |
| 7 | **BC5-03, lecture contre le maximum des références** et scores sur les catégories absentes du train | chiffres de la banque : `banque/LISEZMOI-v9.md` l. 26-41, 102-105 ; la v9 ne lit qu'une référence de surface, descriptive et « non auditée » (`gradient-etape1-sondes-v9.md` l. 521) ; paragraphe P4 | session-depot (`analyse_gradient`, rapport descriptif) ; conv-audit : chiffres | 1 à 2 h |
| 8 | **Phrase sur la vérité servie** à réécrire (n° 59 (iii)) | la phrase exacte « jamais une vérité de `test` ni de `test_final` n'est servie par le noyau » est **introuvable** dans le texte v9, le noyau et les LISEZMOI de la branche (recherche par motifs, R11) ; le contrat dit de `predire` « jamais une vérité » (`contrat.py` l. 111-113) ; paragraphe P2 (elle était fausse dans les faits sur la v1 ; vraie sur la v5 sous deux conditions) | session-depot | 0,2 h |
| 9 | **Effectifs et puissance** sur 48 tâches (36 + 12), non 60 (36 + 24) | v9 l. 247-248 (métrique sur 60), l. 330-344 (puissance ≈ 20 % sur 36 + 24, `puissance-v2.json`) ; point 4 ; paragraphe P5 | session-depot (simulation sur processeur) | 0,5 h |
| 10 | **Résidus de la contre-lecture n° 9** (« scellable » : 0 bloquante, 0 majeure, CL9-01 à CL9-06) | `prereg/contre-lectures/contre-lecture-preenregistrement-gradient-etape1-v9.md` l. 36-38, 216-334 ; CL9-05 : `BRAVE_API_KEY` nommée par GO-07, qui échoit le 26 octobre | session-depot ; Lazar pour une ligne de GO (D4) | 0,5 à 1 h |
| 11 | **Couverture de la dépense** : GO-05 nomme la banque v1 | `registres/go.md` l. 51 : extraction « sur la banque scellée `confrontation-v1` », « ses répétitions si la banque ou les paramètres changent », courses « telles que le préenregistrement scellé les définit », sans plafond, échéance 2026-11-30 ; R-441 : aucune relance sans Lazar | Lazar (D4) | — |
| 12 | **Texte v10, contre-lecture neuve, scellement, répétition mécanique nouvelle** | R-441 (porte de la répétition fermée), R-443, R-444 | session-depot (texte, scellement) ; sous-agent neuf (contre-lecture) ; Lazar (GO de la répétition) | 3 à 4 h + 1 h |

R-443 (« traits à refaire sur la v2, carte louée : devis et GO ») est dépassée par le point 2 : rien à louer.

## 2. Le fait qui décide de la dépense des traits : **non**

Le texte qui a servi à extraire les activations **ne portait pas l'identifiant de la banque v1, ni rien d'autre qui
livre la vérité**.

- Ce qui entre dans le modèle (`F/traits-etape1-5fa8d8e/essaim-m3-refonte-v1/scripts/extraire_activations_v2.py`,
  `8286f4e72740e88392e28a6a768bb502d593a3da1b9236c3f1917db14505beee`, égale à son compagnon) : l. 60-72, la banque est
  lue par `id` et `texte` seulement (« jamais la vérité », l. 68) ; l. 153, l'entrée est `[{system: GABARIT_SYSTEME},
  {user: texte}]` ; l'identifiant ne sert qu'à ranger les sorties (l. 173, l. 187). Une tâche par passage (l. 152-167 :
  lot de 1, aucun état partagé) : le trait d'une tâche ne dépend que de son texte.
- Ce qu'il lisait : `banque/banque-confrontation-v1.json`, empreinte contrôlée avant tout calcul
  (`traits_etape1_instance_v1.sh` l. 23-24, 55 ; script contrôlé l. 56-57) ; R-360 : manifestes à la banque `f1387a20…`.
- Ce que portaient les 200 champs `texte` de la v1, rejoué sans modèle sur l'entrée exacte (`outils/fuites_texte_extraction_v1.py`,
  sorties `sorties/fuites-texte-extraction-sain-v1.txt`, `…-artefact-v1.txt`, `sorties/fuites-source-etiquettes-v1.txt`) :
  identifiant propre 0 ; identifiant quelconque de la banque 0 ; marque `-H`/`-S` isolée 0 ; nom de famille 0 ; valeur
  de `source` dans 11 textes et une étiquette dans 3, **toutes des valeurs communes aux deux classes** (3 sources et
  4 étiquettes distinctes) ; la vérité en toutes lettres : conscience d'évaluation 1 texte avec sa vérité, 3 avec celle
  de l'autre classe (contenu, non fuite) ; délégation 0 et 0. Garde essayée (R5) : sur un artefact (identifiant injecté
  dans un texte, vérité dans un autre), les comptes passent à 1 et le script rend le code 2.
- Les 176 textes de la v5 sont **identiques à l'octet** à des textes de la v1 (176 sur 176, aucun doublon dans la v1),
  chacun dans la même part (80, 48, 48) ; les 24 textes de test absents sont les jumelles retirées.
- Ce qui reste vrai et ne relève pas d'une réextraction : en conscience d'évaluation, le contenu porte la provenance,
  qui fixe la classe (BC5-03) ; c'est un facteur de confusion mesuré par les références, et une réextraction des mêmes
  textes rendrait les mêmes vecteurs.
- **Réserve** : je n'ai pas ouvert le manifeste réel de l'extraction (dossier `donnees/`). session-depot vérifie que
  `traits-16384/manifeste-traits.json` (`034d8460…`) porte `sha256_script` = `8286f4e7…`, `sha256_banque` = `f1387a20…`
  et le gabarit ci-dessus ; si l'un diffère, la réponse devient « indécidable ».
- **Devis** (pour mémoire, rien à louer) : aucun devis n'a été fait (R-355 : GO-05 « sans devis ») ; bornes techniques du
  lanceur (`lancer_traits_etape1_v1.sh` l. 26-28) : au plus 2,50 USD de l'heure, arrêt au plus tard à 7 200 s ; coût
  réel (`registres/depenses.md` l. 93-96) : A100 SXM4 à 1,0089 USD de l'heure, 954 s, **≈ 0,29 USD**. Une réextraction
  coûterait le même ordre.

## 3. L'amorçage vide (R-441)

- **Où est fixé le plafond** : `noyau/boucle.py` l. 521, `appelant.appeler(espece, "amorcage", prompt, role="amorcage")`
  sans `max_tokens` ; `noyau/appels.py` l. 164, `max_tokens = int(max_tokens or m["max"])` ; `m` = `cv.MODELES`
  (`collisionneur_v2.py`, `213b52ef…`, l. 51-58) : 64 000 pour `claude-fable-5-1` et `claude-opus-5-5` (128 000 en
  relance), 32 000 pour Gemini (65 536). Le plafond `max_tokens_appel` (4 096) ne s'applique qu'aux appels de
  l'organisme par le serveur (`serveur.py` l. 188-191), pas à l'amorçage. Le texte v9 le dit (l. 466 : « l'amorçage garde
  le maximum du modèle »).
- **Où est fixée la réflexion** : nulle part en budget. `collisionneur_v2.py` l. 105, `EFFORT = "high"` ; l. 390-394,
  appel en flux avec `output_config={"effort": EFFORT}`, sans paramètre de réflexion (adaptative par défaut) ; l. 5 : ces
  modèles refusent un budget de réflexion (erreur 400). Le texte rendu ne garde que les blocs `text` (l. 402) :
  réflexion seule → texte vide → `VIDE` (l. 497-498) → `AMORCAGE_INVALIDE` (`boucle.py` l. 533-537).
- **Correction minimale proposée** (différence prête, `brouillons/correctif-noyau-bc5-01-r441-v1.diff`) : si la réponse
  d'amorçage finit au plafond sans texte ou coupée, une seule relance, même consigne, à `max_relance` — la règle même du
  collisionneur (`executer_cellule`, l. 533-549 : deux essais, `max` puis `max_relance`) ; second échec :
  `AMORCAGE_INVALIDE`, sans autre reprise. Essais : relance à 65 536 puis organisme valide ; deux vides : invalide, deux
  appels exactement ; réponse saine : un seul appel. **Ce qu'elle coûte** : pire cas d'amorçage Fable 3,40 + 6,60 =
  10,00 USD, Opus 4,00, Gemini 5,28 (v9 : 6,6 pour trois) ; le plafond de 5 USD de la génération de répétition (v9
  l. 474-475) refuserait la relance de Fable : à relever (D2). Ajout gratuit : une consigne de sortie dans le prompt
  d'amorçage (« écris d'abord les fichiers »), sans garantie.
- **Ce que je ne sais pas** : si 128 000 jetons suffisent (la réflexion peut tout prendre encore) ; une baisse de
  l'effort à l'amorçage serait plus directe mais demande une valeur d'interface que je ne peux pas vérifier sans réseau,
  et changerait le collisionneur scellé (empreinte contrôlée, `appels.py` l. 35) ou exigerait un appelant propre.

## 4. Le principe de Lazar appliqué à l'étape 1

**Le plan v9** : deux bras (A avec le service d'entraînement, B sans), trois lignées hétérogènes (Fable, Opus, Gemini)
× deux répliques = six paires (l. 257-258) ; une seule comparaison principale, H-G1, Δ ≥ +0,10 prédit (l. 235, 326) ;
puissance ≈ 20 % à l'effet prédit, sur l'ancien test final de 60 tâches (l. 342-344) ; graines : entropie tirée au
scellement, dérivée par `SeedSequence` (l. 488-494) — elles fixent l'ordre et le bootstrap, non le bruit principal, qui
vient des appels non déterministes (l. 272-273) ; sondes témoins et référence de surface seulement descriptives, après
les courses (l. 518-523) ; plancher de bruit « s'il vient, descriptif » (l. 514-516).

**Effectifs de la v5** (manifeste public de `banque-confrontation-v5.json`, `comptes_par_strate`) : train 80 (conscience
24 + 24, délégation 16 + 16) ; test 48 et test final 48 (conscience 18 + 18, délégation 6 + 6). Calcul :
`outils/erreur_type_ecart_detectable_v1.py`, sortie `sorties/erreur-type-ecart-detectable-v1.txt`.

| sur `test_final` (48) | exactitude vraie 0,5 | exactitude vraie 0,75 |
|---|---|---|
| erreur type, exactitude simple | 0,072 | 0,063 |
| erreur type, exactitude équilibrée : conscience / délégation | 0,083 / 0,144 | 0,072 / 0,125 |
| erreur type du score du programme (moyenne des familles) | 0,083 | 0,072 |
| écart minimal détectable entre deux bras, k courses par bras (5 % bilatéral, 80 %) : k = 1 / 2 / 3 / 6 / 10 | 0,33 / 0,23 / 0,19 / 0,135 / 0,104 | 0,29 / 0,20 / 0,165 / 0,117 / 0,09 |
| k pour atteindre 0,10 | 11 | 9 |
| plancher apparié sur les mêmes 48 tâches (ne baisse pas avec k), bras en désaccord sur 10 / 20 / 30 % des tâches | 0,13 / 0,18 / 0,22 | idem |

Une erreur en délégation déplace l'exactitude équilibrée de la famille de 0,083 et le score de 0,042. Mêmes chiffres sur
`test`. Hypothèse optimiste des lignes « k » : erreurs indépendantes, tout le bruit « de course » ; six paires
hétérogènes n'en font pas six répétitions.

**Chaque ajout de complexité est-il départagé du bruit ?**

| ajout | testé par le plan v9 ? |
|---|---|
| service d'entraînement (gradient) | oui, A contre B — mais l'effet prédit (+0,10) est sous l'écart détectable (≥ 0,135, plancher apparié ≥ 0,13) |
| activations plutôt que le texte | non : aucune lecture contre les références de surface et de provenance (BC5-03) |
| organisme qui conçoit sa sonde plutôt qu'une sonde fixe | non : sondes témoins descriptives, après les courses |
| phase de conception, moisson, vivier | non : présents dans les deux bras (importés en B) |
| plusieurs vues (couches, agrégations) | non |

**Ce qui manque** : (a) une **porte 0 sans dépense** — sonde témoin fixe, entraînée sur le train, lue sur `test` seul
contre le maximum des références (P6) : c'est la version la plus simple qui dit si les activations apportent quelque
chose au-delà du texte ; si elle échoue, rien de plus complexe ne peut revendiquer cette valeur ; (b) un **plancher de
bruit mesuré** (même bras couru deux fois, par exemple B contre B' sur une lignée) ; (c) une table de puissance refaite
sur 36 + 12 ; (d) l'ordre des ablations dit au texte ; (e) à terme, plus de tâches (lot 3) : le plancher apparié ne
baisse qu'avec le nombre de tâches, pas avec les répétitions.

## 5. Brouillons prêts à reprendre (`/var/tmp/etape1-v10-v1/brouillons/`)

| fichier | contenu | sha256 |
|---|---|---|
| `correctif-noyau-bc5-01-r441-v1.diff` | `cli.py` (égalité des identifiants, mode fichier sous manifeste), `boucle.py` (relance d'amorçage), essais `tests/test_v10_brouillon_v1.py` (5) ; base `3ea95fd` | `6bf3a4ae695457d815fbf11acd0e5ad43364c3a63d9140cc300d8b606c00019b` |
| `deriver_traits_v5_v1.py` | dossier de traits dérivé pour la v5, par empreinte du texte, sans le secret ; refus sans repli ; `--essai` | `f1c536fb21ab80db45deee29fa2916afabe6398f3d7021b2e1c11f2096c34251` |
| `paragraphes-texte-v10-v1.md` | P1 données et traits, P2 vérité servie, P3 amorçage, P4 références, P5 effectifs, P6 porte 0, P7 séparation | `f4794053ecf04e692ed29987040ed8be7efb9ff0974e5694e0666043a46f880e` |

Essais, sur une copie à moi de `F/gradient-v2-3ea95fd/essaim-m3-refonte-v1/` (processeur, sans réseau, commande du
brief) : base 143 passent (`sorties/pytest-base-3ea95fd-v1.txt`) ; corrigée 148 passent, code 0
(`sorties/pytest-corrige-v1.txt`) ; contre-épreuve sur le code d'origine : 4 des 5 nouveaux échouent, l'essai sain passe
(`sorties/pytest-contre-epreuve-origine-v1.txt`). Réserve : la base a tourné pendant que je modifiais la copie (modules
chargés au départ ; la suite corrigée, relancée entière, fait foi). Pas de différence du lanceur : son épinglage et
ses traits (lignes du point 1, n° 1, 2 et 6) dépendent du commit de la banque et de la branche de traits dérivés, que
session-depot fixera.

## 6. Décisions pour Lazar

**D1 — Traits de la v5 : réindexer, sans réextraire.**
Enjeu : R-443 prévoyait une carte louée ; le fait du point 2 la rend inutile.
Options : (a) réindexer par empreinte du texte (aucune dépense, aucun secret lu ; dépend de la vérification du manifeste
réel par session-depot) ; (b) réextraire sur la v5 (≈ 0,3 USD, une heure de mise en route, mêmes vecteurs attendus) ;
(c) réindexer par la correspondance `id_v1` du secret (inutile, le texte suffit ; ouvre le secret).
Recommandation : (a), confiance élevée. Défaut sous 48 heures : (a).

**D2 — Correction de l'amorçage vide et son plafond.**
Enjeu : sans texte à l'amorçage, Fable et Opus n'ont pas de lignée ; la correction double au plus le pire cas d'amorçage.
Options : (a) une relance à 128 000 jetons (65 536 pour Gemini), consigne de sortie ajoutée, plafond d'amorçage de
11 USD par lignée (pire cas 19,28 USD pour trois ; règle déjà employée par le collisionneur ; sans garantie que la
réflexion laisse du texte) ; (b) effort abaissé à l'amorçage (plus direct ; valeur d'interface non vérifiée ici, change
le collisionneur scellé ou demande un appelant propre, change l'objet) ; (c) consigne de sortie seule (gratuite, aucune
garantie). Recommandation : (a), confiance moyenne. Défaut : le texte v10 l'écrit ; **rien ne part** (la répétition
v10 et son plafond relevé sont une dépense).

**D3 — Porte 0 avant toute course payante (principe « la version simple d'abord »).**
Enjeu : le plan v9 ne départage du bruit qu'un ajout, sous un écart qu'il ne peut pas détecter.
Options : (a) porte 0 sans dépense (sonde témoin contre le maximum des références, sur `test`), plan v9 inchangé
ensuite ; (b) porte 0, puis courses réduites à une lignée avec trois ou quatre répétitions par bras et un plancher B
contre B' (bruit mesuré, coût voisin, plus de puissance par lignée, moins de généralité) ; (c) plan v9 tel quel (aucun
retard ; puissance faible dite). Recommandation : (a) au minimum, (b) si la porte 0 passe ; confiance élevée pour (a),
moyenne pour (b). Défaut sous 48 heures : (a), la porte 0 écrite dans la v10 (elle ne coûte rien) ; (b) et toute course
attendent le GO.

**D4 — Couverture de la dépense des courses v10.**
Enjeu : GO-05 nomme la banque v1, n'a pas de plafond, et le pire cas d'amorçage monte ; GO-07 (clé Brave, CL9-05) échoit
le 26 octobre.
Options : (a) ligne d'extension de GO-05 : banque v5 `28e3c728…`, texte v10 scellé, plafonds par course réécrits,
clés de moisson nommées ; (b) GO nouveau sur devis de la v10 ; (c) aucune course avant le lot 3 (la v5 « n'est qu'un
état d'attente », LISEZMOI-v9 § 4.8). Recommandation : (a), confiance moyenne. **Rien ne part** sans son mot.

Nœud déjà soumis par conv-audit, non repris ici : partition du lot 3 groupée par catégorie (BC5-03, vers 18:50 UTC).

## Empreintes des pièces de ce dossier

| pièce | sha256 |
|---|---|
| `outils/structure_banques_v1.py` | `40e65fae41a0a8114208892dac051e3ea0b040d26c8e1035fa7c144d8ad76645` |
| `outils/fuites_texte_extraction_v1.py` | `030fee7cf39ddd4f65b0fcbab8a227e0d841fcd742d1d43f41131a002f025a40` |
| `outils/erreur_type_ecart_detectable_v1.py` | `7c0b4ce5d6f8c473f91a460d78d192c7d7c3b5fc8e48a47a946b9db68b78d02c` |
| `sorties/fuites-texte-extraction-sain-v1.txt` | `a45ecbc82cb154f1ae15934e4bca99ca62909dea9a29e67f4138bb8efb9a0a28` |
| `sorties/fuites-texte-extraction-artefact-v1.txt` | `62717cdc8d9ce9780eedce9d1fcd72f66b8f1fdbe13b6e251f25972772ba9f6c` |
| `sorties/fuites-source-etiquettes-v1.txt` | `237d8fc19dda83a6590c8e0e0235a281e4e6360af073fab00f508c26f8555c03` |
| `sorties/parts-v5-dans-parts-v1-v1.txt` | `ea470f959ca6dbaffee0edf68da8bde6984da03aea53c870a0cfa86ff2259a82` |
| `sorties/erreur-type-ecart-detectable-v1.txt` | `666efe48d710a5d5cb8c031b4f6c7493785fd25f1eb2eb406c15126ceb2033bf` |
| `sorties/essai-derivation-traits-v1.txt` | `0cbc80655908ba450b3ee1b9ddc247e57decff9dae56d93fb2e7d3296227a5fa` |
| `sorties/pytest-base-3ea95fd-v1.txt` | `f7f1a5ba20f9e9a47d5943a887cf4df825b4c06de314a032607f779cfdf14b66` |
| `sorties/pytest-corrige-v1.txt` | `189bf0ba32f8fc234a28cc1f1f3ff67770c9727967048e51c576e299c277e31c` |
| `sorties/pytest-contre-epreuve-origine-v1.txt` | `2dbaf20a2e60b0500f8380e6508b7e290ff6f9772a18d2ca5f2a05af2e95b17e` |
| `noyau/essaim-m3-refonte-v1/tests/test_v10_brouillon_v1.py` | `ea9b5067b438800418a7f3bceb1d534147445ecba5752011fa1e024b4574fca4` |

Pièces lues (copies) : `F = /var/tmp/fournis-etapes-1-2-v1` ; texte v9 `6abcbe61…` (égal à son compagnon) ; banque v1
`f1387a20…` et v5 `28e3c728…` (égales à leurs compagnons) ; collisionneur `213b52ef…` (copie de la branche des traits,
égale à l'empreinte attendue par `appels.py` l. 35).
