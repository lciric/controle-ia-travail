# Préenregistrement — nul par morceaux limité aux conditions de l'archive, contre le nul v9, sur un banc de cartes écrites par programme — v1

- Auteur : concepteur neuf (modèle A au sens de R-2851), sous-agent de la session mère ; je n'ai écrit ni le relevé, ni les
  fiches, ni le juge, ni les nuls v8 et v9.
- Date (UTC) : 2026-11-15, rédaction à partir de 08:21 (`date -u`) ; dépôt lu sur `main` (tête `ff85c5f0` au début ; aucun commit).
- Commit du code d'analyse : **aucun à ce jour**. Le code du banc s'écrit **après** la contre-lecture et le scellement de la
  version qui fera foi ; ses empreintes entrent dans un **addendum d'empreintes** scellé avant tout jeu (Plan d'analyse,
  étape 0), qui ne peut rien changer d'autre que remplir la liste des fichiers gelés.
- Documents qui font foi (chemin + empreinte) :
  - preuve de validité, scellée avant ce texte : `docs/notes/organisme-idees-juge-v1/preuve-validite-nul-limite-v1.md`
    (`44f249409193778ccbaaa12b6c5e74d64434dfb87be77382d8bb9438459281b2`) — ci-dessous **[PREUVE]** ;
  - relevé d'idées, § 1.1 et § 7 : `docs/notes/organisme-conception-propre-v1/relecture-exploratoire-v2/releve-idees-reutilisables-v1.md`
    (`bd253b6c68f6baada0e61b5381f029b52838ca34aa092502e55253c662451c6c`) ;
  - fiches (argon-p1-01, argon-p2-01, opus-p1-05, fable-p1-05) :
    `runs/course-ideation-conception-propre-v1/20261113-235541-course-ideation-conception-propre-v1-g1/copies/sortie--fiches-validees.json`
    (`a9f9594e2dc3a7a553c54577202817758e3f7ef231445f1a48d500fc647389d5`) ;
  - code du juge, copie empreintée au commit `94bfd92` : `docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/`
    (liste `empreintes-copie-v1.txt`, `0153e02d4522fe21eb1cf52985574eba38b5f260f7a3a08183d63589f29f32df`, 53 fichiers conformes le
    15 novembre) : `pole/selection_pari.py` (`35992811…`), `pole/nul_filles_v2.py` (`0ed9b4ad…`), `pole/nul_v8.py` (`cc452aaf…`),
    `pole/cycle.py` (`798f0390…`), `pole/a_blanc_v59.py` (`606aa8b4…`), `pole/outils.py` (`966d9553…`) ;
  - nul v9 : `orchestrator/pole/nul_v9.py` (`7ae450df2482246122bf9fbcf0fa5ef30b4a7e4c6f0d09531e83af048e46ee95`), **absent de ce
    dépôt**, à verser en copie empreintée (préalable 1) ; sa description publique :
    `livrables/page-publique-organisme-2026-11-10-v1/resultats/attaque-goodhart-v2/README.md` (`c549a31b…`, l. 64) ; le verdict
    recalculé de sa validation : `docs/notes/ideation-organisme-v1/validation-nul-v9-v1/audit-verdict-validation-nul-v9-v1.md`
    (`9086a420a082ed8fd7d76dc666ef5ef336a9f6842be8ff90e4aca7db0d72f7c8`) ;
  - registre : R-1779 (nœud ouvert « accepter le prix du v9 ou chercher un nul moins coûteux »), R-2851 (mot de Lazar) ;
  - gabarit `prereg/gabarit-preregistrement-v1.md` (`8cad4371…`) et validateur `src/controle_ia/prereg.py` (`3b2e3ee5…`).

**Statut.** Version 1, **scellée par empreinte (R6) mais non contre-lue** : elle ne vaut pas préenregistrement au sens de R1.
Elle le devient sous un nom neuf (v2 ou plus), après la contre-lecture par un sous-agent neuf d'un autre modèle (R2, section
« Contre-lecture »), les corrections portées, et un scellement par `controle_ia.prereg.sceller_prereg`. **Aucun jeu avant.**
Le jeu se fait sur processeur, sans dépense (R-2851). Aucun chiffre ci-dessous n'est un résultat du banc : le banc n'existe
pas ; les seuls calculs faits sont la preuve et le compte de dimensionnement des doses (annexe A), qui ne fait intervenir ni
juge, ni nul, ni promotion.

## Hypothèse

**Contexte.** Le nul v9 ferme le trou par morceaux du v8 en ajoutant au nul toutes les recombinaisons à un niveau des lois
connues, par sous-population ou de part et d'autre de **tout seuil réel** d'un trait (page publique, l. 64). Sa validation
décisive a rendu « puissance perdue » : perte appariée de 0,105 sur la ligne d'interaction faible I02, borne de
Clopper-Pearson unilatérale à 95 % [0,0894 ; 0,1223] (audit `9086a420…`, § 2.2). Le nœud R-1779 demande s'il existe un nul
moins coûteux. L'idée 1.1 du relevé (variante (c), fiches argon-p1-01 et argon-p2-01) : ne mettre au nul que les recollages
coupés aux **conditions que l'archive a déjà isolées**. La partie « poids appris en ligne » de ces fiches n'est pas valide
([PREUVE], § 8) : elle n'est pas éprouvée. Ce qui l'est : la **restriction de la liste des partitions**, sous la
construction existante du juge (maximum de vraisemblance certifié sur les tirages mêmes).

**H-1.1 (principale).** Sur un banc de mondes et de cartes écrits par programme, dans la classe de mondes du banc des
tricheurs (3 issues, 2 traits, 2 sous-populations), un nul limité aux partitions que l'archive a isolées **recouvre au moins
la moitié** de la puissance que le v9 perd par rapport au v8 sur de vraies découvertes, tout en gardant sa taille α sur sa
propre classe ; il le paie en laissant passer les copies coupées ailleurs.

**Sous-hypothèses de travail** (chacune lue à part, section « Critères de lecture gelés ») :
- **H-a (garde, par construction)** : chaque nul garde une taille au plus α sur sa classe ([PREUVE], théorème 1) ; une carte
  qui est un membre de la classe n'est jamais promue (W ≤ 1 à chaque tirage, [PREUVE], § 4, remarque ii).
- **H-b (prix du v9 sur ce banc)** : le v9 perd de la puissance contre le v8 sur une partie des lignes de vraies découvertes.
- **H-c (origine du prix)** : une part importante du prix du v9 vient de la **recherche sur tous les seuils** (surajustement du
  maximum sur des centaines de coupures), non des seules coupures où vit la structure ; c'est ce que sépare la comparaison
  des bras La (coupures de l'archive) et Ld (coupures de l'archive plus partitions déclarées : sous-population et signe de
  chaque trait).
- **H-d (prix de la restriction)** : les copies coupées hors des conditions retenues passent, à des taux voisins de ceux du v8.

**Renvois.** Organisme d'idéation, second terrain du papier C et atelier d'idées (N-065) ; garde contre les copies (faits du
collisionneur, `d19b5400…`, § 1) ; bornes 7 et 9 du recoupement (`eecd98fa…`) ; J6 (valeur e par supremum sur un nul composite
explicite, « maintenue sous double condition » : supremum majoré de façon démontrée, puissance vérifiée sur une carte
réellement additionnelle) — ce banc vérifie les deux conditions pour La, La2 et Ld.

## Prédiction chiffrée et signe attendu

Toutes écrites avant tout jeu, sans pilote. Cellule = (ligne, bras) ; taux = part des 1 000 répétitions où la carte seule est
promue. Bras et lignes : section « Plan d'analyse ».

| # | prédiction | signe | chiffre | ce qui la réfute | confiance |
|---|---|---|---|---|---|
| P1 | cellules « fatales » (carte = membre exact de la classe du bras, 15 cellules) : aucune promotion ; log W maximal ≤ 10⁻⁶ | nul | 0 sur 1 000 par cellule | une seule promotion, ou un log W > 10⁻⁶ (défaut de code ou de certificat) | 0,97 |
| P2 | cellules de taille Q7 (monde dans la classe, carte hors classe, 4 cellules) | sous α | taux ≤ 0,02 | taux > 0,05 avec borne basse de Clopper-Pearson > 0,05 | 0,8 |
| P3 | dents : J8 promeut les copies Q2, Q3, Q4, Q5 ; J9 promeut la copie à deux niveaux Q6 | + | J8 ≥ 0,90 sur chacune ; J9 ≥ 0,80 sur Q6 | une borne basse de Clopper-Pearson ≤ 0,5 | 0,75 |
| P4 | trous rouverts : La promeut Q3, Q4, Q5 ; Ld promeut Q5 ; La, Ld promeuvent Q6 | + | La ≥ 0,85 sur Q3, Q4, Q5 ; Ld ≥ 0,60 sur Q5 ; La, Ld ≥ 0,80 sur Q6 | La < 0,5 sur Q3 ou Q4 (la restriction fermerait plus que sa classe : à auditer) | 0,7 |
| P5 | prix du v9 sur ce banc : J9 perd contre J8 | J9 < J8 | lignes informatives (perte appariée à borne basse ≥ 0,02) : au moins 4 des 12 lignes V, surtout aux doses moyennes | moins de 2 lignes informatives | 0,65 |
| P6 | **principale** : part recouvrée par La | + | ρ_La ≥ 0,5 en borne basse (estimation ponctuelle attendue 0,6 à 0,9) | borne haute < 0,25 | 0,65 |
| P7 | part recouvrée par Ld | + faible | ρ_Ld ponctuelle dans [0,2 ; 0,6], **pas** « recouvre » ; sur les lignes V2 et V4 informatives, Ld recouvre au plus 0,3 de la perte de J9 (ses partitions sont celles où vivent ces structures) | borne basse de ρ_Ld ≥ 0,5 (bonne nouvelle : un nul moins coûteux qui ferme aussi les copies déclarées) | 0,5 |
| P8 | La2 (intersections de deux conditions) contre La | − ou 0 | ρ_La2 ≤ ρ_La ; écart ponctuel ≥ 0,05 | ρ_La2 > ρ_La + 0,05 | 0,55 |
| P9 | ligne V3 (coupure décentrée hors de C) : La et Ld recouvrent | + | sur chaque ligne V3 informative, gain apparié de La et de Ld ≥ la moitié de la perte de J9 | gain < un quart de la perte sur toutes les lignes V3 informatives | 0,55 |
| P10 | contrôle sans coupure : sur V1 (effet neuf global), Ld et La ne font pas pire que J9 | ≥ 0 | par construction (nichage, [PREUVE] § 6 (b)) ; écart attendu ≥ 0 sur chaque ligne | toute perte appariée de La ou Ld sous J9 au-delà de 10⁻⁴ nat de certificat (arrêt, liste d'arrêt) | 0,97 |

**Ce que serait chaque issue.** P6 vraie et P7 fausse dans le sens « Ld recouvre » : un nul moins coûteux qui ferme encore la
forme de W2 existe (meilleur cas). P6 vraie, P7 vraie : un nul moins coûteux n'existe qu'en rouvrant la forme de W2.
P6 fausse (borne haute < 0,25) : le prix du v9 ne tient pas au nombre de coupures ; la restriction ne sert pas.

## Métrique

- **Promotion d'une carte seule** : il existe t ∈ T = {25, 50, …, 200} avec log W_t ≥ log(1/α), α = 0,05 (règle de
  `nul_filles_v2.evaluer_v2`, sans marge des filles : cartes fraîches).
- **Taux d'une cellule** : promotions / 1 000 ; intervalle de Clopper-Pearson (bilatéral à 95 % pour le rapport ; unilatéral
  à 95 % pour les seuils, comme la validation du v9).
- **Perte appariée du v9 sur une ligne ℓ** : δ₉(ℓ) = (1/R)·Σ_r (a_r − b_r), avec a_r = 1[J8 promeut], b_r = 1[J9 promeut]
  à la répétition r. Par monotonie ([PREUVE], § 6 (a), le v9 contenant le v8), b_r ≤ a_r : δ₉ est la part des paires
  discordantes ; borne basse de Clopper-Pearson unilatérale à 95 % sur cette part.
- **Gain apparié d'un bras X sur J9** : Δ_X(ℓ) = (1/R)·Σ_r (c_r − b_r), c_r = 1[X promeut] ; test exact de McNemar par ligne
  (rapport).
- **Ligne informative** : borne basse de δ₉(ℓ) ≥ 0,02. L'ensemble I des lignes informatives est fixé par J8 et J9 seuls,
  jamais par les bras limités.
- **Part recouvrée (principale)** : ρ_X = Σ_{ℓ ∈ I} Δ_X(ℓ) / Σ_{ℓ ∈ I} δ₉(ℓ). Intervalle par rééchantillonnage des
  répétitions à l'intérieur de chaque ligne (triplets (a, b, c) appariés), 10 000 rééchantillons, graines dérivées de la
  racine (Plan d'analyse) ; quantiles 1,25 % et 98,75 % (Bonferroni pour deux bras primaires, La et Ld). Un rééchantillon de
  dénominateur nul est écarté et compté.
- **Faux positifs sur les copies** : taux des cellules Q2 à Q6 pour les bras dont la classe ne contient pas le monde (trous
  rouverts, mesurés) ; pour les bras dont la classe le contient, ce sont des cellules de taille.
- **Mesures descriptives** (aucun critère) : log W maximal et médian par cellule ; membre dominant final (`membre_dominant_final`)
  par cellule ; écart de certificat des membres par morceaux (médiane, maximum) ; temps par évaluation ; perte appariée de La2.
- Aucune moyenne ni médiane sur des jetons : il n'y en a pas ici.

## Seuil

- **Niveau du juge** : α = 0,05 ; instants T = {25, …, 200} ; n = 200 tirages frais ; marginale d'entraînement sur 100 instances
  (comme `a_blanc_v59.juger_carte`).
- **Cellules de taille** (15 fatales + 4 de Q7 = 19) : « tenue » si le test binomial exact de H₀ « taux ≥ α » est rejeté au
  niveau de Holm 0,05 sur la famille des 19 ; « non tenue » si H₀ « taux ≤ α » est rejeté au même niveau ; sinon « non
  jugeable ». En plus, pour les 15 fatales : **toute** promotion ou tout log W > 10⁻⁶ déclenche l'audit A1 (une carte membre
  ne peut pas être promue).
- **Dents** : borne basse de Clopper-Pearson unilatérale à 95 % > 0,5 pour J8 sur Q2, Q3, Q4, Q5 et pour J9 sur Q6.
- **Ligne informative** : borne basse unilatérale à 95 % de δ₉(ℓ) ≥ 0,02.
- **Part recouvrée** : « recouvre » si la borne basse (quantile 1,25 %) de ρ_X ≥ 0,5 ; « ne recouvre pas » si la borne haute
  (quantile 98,75 %) < 0,25 ; sinon « partiel ». Au moins 2 lignes informatives sont exigées pour lire ρ (sinon « sans
  objet »).
- **Tolérances numériques** : arrêt de l'optimiseur des membres par morceaux à un écart de certificat ≤ 10⁻⁴ nat ou au nombre
  maximal de pas du code du v9 ; nichage vérifié à g_max + 10⁻⁶ nat ; monotonie vérifiée à 10⁻⁶ nat.

## Plan d'analyse

### Banc B (partagé avec le préenregistrement de l'idée 1.2)

**Espace.** K = 3 issues ; D = 2 traits ; G = 2 sous-populations. Instance : z_j ~ N(0, 1) indépendants, arrondis à six
décimales ; g uniforme sur {0, 1} (comme `selection_pari.tirer_instances`, mais tirés par le générateur numpy de la graine
de la répétition). **Loi softmax aléatoire** : poids w_{k,j} ~ N(0 ; 1,5²), biais b_k ~ N(0 ; 0,3²), arrondis à six décimales
(comme `loi_softmax_aleatoire`, force 1,5). Toute loi du banc est une loi de la grammaire du juge, vérifiée par
`selection_pari.valider_loi` avant usage.

**Archive A2** (toutes les lignes) : S1, S2 softmax aléatoires ; S3 = `si_sinon`({z_{jA} > s_A}, U1, U2) ;
S4 = `si_sinon`({z_{1−jA} > s_B}, U3, U4) ; U1 à U4 softmax aléatoires ; jA uniforme sur {0, 1} ; s_A, s_B ~ U[−1 ; 1]
arrondis au centième, retirés tant que |s| < 0,05 (aucune coupure de l'archive ne se confond avec un signe déclaré : l'appartenance
aux classes du tableau ci-dessous ne dépend donc pas du tirage). Donc C_arch = {z_{jA} > s_A ; z_{1−jA} > s_B}, disjoint de C_decl.
C_decl = {sous-population ; z₀ > 0 ; z₁ > 0}. **Archive A0** ({S1, S2}) : seulement pour l'essai d'égalité E0 (étape 2),
jamais lu.

**Lignes** (M : loi du monde ; Q : loi de la carte ; cut(j) : seuil de l'archive sur le trait j) :

| ligne | monde M | carte Q | classes qui contiennent M |
|---|---|---|---|
| Q1 mélange de l'archive | `melange`([S1, S2, S3, S4, uniforme fixe], poids ~ Dirichlet(1, …, 1), arrondis et renormalisés) | Q = M | toutes |
| Q2 copie à une coupure de l'archive | `si_sinon`({z_{jA} > s_A}, S1, S2) | Q = M | J9, La, La2, Ld |
| Q3 copie par sous-population (forme de W2) | `par_sous_population`({"0": S1, "1": S2}) | Q = M | J9, Ld |
| Q4 copie au signe d'un trait | `si_sinon`({z_j > 0}, S1, S2), j uniforme | Q = M | J9, Ld |
| Q5 copie à une coupure hors de C | `si_sinon`({z_j > s}, S1, S2), j uniforme, s = ±U[0,3 ; 1,0] au centième, retiré tant que \|s − cut(j)\| < 0,3 | Q = M | J9 |
| Q6 copie à deux niveaux sur C_arch | `si_sinon`({z_{jA} > s_A}, `si_sinon`({z_{1−jA} > s_B}, S1, S2), `si_sinon`({z_{1−jA} > s_B}, S2, S1)) | Q = M | La2 |
| Q7 monde copie, carte hors classe | M de Q2 | `si_sinon`({z_{jA} > s_A}, S1′, S2), S1′ = softmax(W1 + 0,25·Δ, b1), Δ ~ N(0, 1) centrée par colonne | J9, La, La2, Ld (pour M) |
| V1(δ) effet neuf global, δ ∈ {0,25 ; 0,50 ; 0,75} | softmax(W1 + δ·Δ, b1), Δ ~ N(0, 1) centrée par colonne sur les issues | Q = M | aucune |
| V2(γ) composante conditionnelle au signe, γ ∈ {0,4 ; 0,8 ; 1,2} | `si_sinon`({z_j > 0}, softmax(W1 + γE, b1), softmax(W1 − γE, b1)), j uniforme, E nulle sauf la colonne du trait 1 − j égale à u (u ~ N(0, I₃) centré, normé) | Q = M | aucune |
| V3(γ) conditionnelle à seuil décentré, γ ∈ {0,4 ; 0,8 ; 1,2} | comme V2 avec le seuil c = ±U[0,3 ; 0,8] au centième, retiré tant que \|c − cut(j)\| < 0,3 | Q = M | aucune |
| V4(λ) loi neuve sur une sous-population, λ ∈ {0,1 ; 0,2 ; 0,3} | `par_sous_population`({"0": S1, "1": `melange`([S1, N], [1 − λ, λ])}), N softmax aléatoire | Q = M | aucune |

19 lignes de lecture (Q1 à Q7, V1 à V4 à trois doses). Les grilles de doses sont placées par le compte de l'annexe A
(information de 2 à 23 nats sur 200 épisodes), sans aucun jugement.

**Bras** (même plan, mêmes issues fraîches, mêmes instants pour tous) :
- **J8** : nul de production, `nul_v8.membres_archive_v8` sur l'archive, bibliothèque standard et marginale d'entraînement,
  comme `a_blanc_v59.juger_carte` ;
- **J9** : nul v9, **code original** `nul_v9.py` (`7ae450df…`), construit pour une carte fraîche comme le banc de sa
  validation le fait (entrée à relever sur la copie, `banc_tricheurs_v9.py`, `7e4bff59…`) ;
- **La**, **La2**, **Ld** : nuls limités de [PREUVE], § 3 — le module du v9, **copié sous un nom neuf** (R12), dont le seul
  changement est que la liste des partitions devient un paramètre : 𝒫₁(C_arch), 𝒫₂(C_arch), 𝒫₁(C_arch ∪ C_decl).
  Différentiel lu par le contre-lecteur du code ; tout autre changement est un écart (nœud). Si le code du v9 ne traite que des
  partitions à deux cellules, l'extension à quatre cellules exigée par La2 est un second changement, déclaré, essayé (cas sain :
  une partition à quatre cellules dont deux sont vides donne la valeur de la partition à deux cellules correspondante) et lu par
  le contre-lecteur ; s'il n'est pas sûr, La2 est retiré du jeu (rapporté, sans effet sur les bras primaires La et Ld).

**Répétitions et appariement.** R = 1 000 répétitions par ligne. À chaque répétition, le banc tire une fois l'archive, les
paramètres de la ligne, 100 instances d'entraînement et leurs issues, le plan de 200 instances et les 200 issues fraîches
(dans l'ordre du plan : les mondes du banc ne lisent pas l'historique, l'ordre d'exécution est indifférent, [PREUVE] H6).
Chaque bras construit son engagement (`nul_filles_v2.construire_engagement_v2`, plan d'exécution « ordre_naturel »), le
gèle, et reçoit **les mêmes issues** dans un dictionnaire de tirages lié à **son** empreinte ; il est évalué par la fonction
d'évaluation de son nul (`evaluer_v2` pour J8 ; celle du v9 pour J9, La, La2, Ld). Essai à blanc fait le 15 novembre sur la
copie `94bfd92` (hors banc, annexe B) : `evaluer_v2` accepte ce montage, et la trajectoire d'un plan de 800 tronquée à 200 est
égale, valeur pour valeur, à celle d'un plan de 200 (préfixe), en 0,02 à 0,03 s par évaluation à 200 tirages.

**Graines (R9).** Racine : l'entier de l'empreinte sha256 du texte qui fera foi (comme la validation du v9,
`audit-verdict…`, § 1, ligne 5). Générateur `numpy.random.default_rng(numpy.random.SeedSequence(entropy=racine,
spawn_key=(i_ligne, r)))` par répétition ; `spawn_key=(99, b)` pour le rééchantillonnage ; numpy ≥ 1.25. Manifeste du run
(`src/controle_ia/manifeste.py`) : configuration et empreinte, versions de Python et numpy, graines, commit, empreintes des
fichiers gelés.

### Étapes

0. **Préalables et gel.** (a) Copie empreintée de `nul_v9.py` versée (préalable 1, section « Écarts, nœuds… ») et égale à
   `7ae450df…` ; (b) code du banc écrit sous des noms neufs dans `docs/notes/organisme-idees-juge-v1/code-v1/` :
   `nul_limite_v1.py` (copie renommée du v9, liste de partitions en paramètre, extraction de C_arch et C_decl),
   `banc_nul_limite_v1.py` (lignes, bras, évaluation, sortie), `lire_banc_nul_limite_v1.py` (lecture gelée : la table des
   critères écrite en code) ; (c) essais (R5 : cas sain et artefact pour chaque garde) et banc de mutations (au moins : écart de
   certificat retiré ; partition fausse ; C calculé sur les issues fraîches ; tirages différents d'un bras à l'autre ; lecture
   d'un instant hors de T ; seuil d'informativité choisi sur La ; mauvais bras au numérateur de ρ) : toutes tuées pour la
   raison attendue ; (d) contre-lecture du code par un autre modèle ; (e) **addendum d'empreintes** scellé.
1. **Contrôles avant jeu** : empreintes des fichiers gelés conformes ; essais et mutations rejoués ; aucune sortie existante.
2. **Essai d'égalité E0** (100 répétitions, archive A0, ligne Q1) : La ≡ J8 valeur pour valeur, à 10⁻¹² nat près (aucune
   condition, aucun membre ajouté) ;
   sinon arrêt. Non lu au-delà de cette égalité.
3. **Jeu** : 19 lignes × 1 000 répétitions × 5 bras, `nice -n 10`, deux processus au plus ; gardes de la liste d'arrêt
   actives à chaque évaluation.
4. **Scellement de la sortie** avant toute lecture (compagnon `.sha256`) ; sortie sous `diag/organisme-idees-juge-v1/`.
5. **Lecture** : par la lecture gelée, puis par un lecteur neuf (R13) qui recalcule l'issue de façon indépendante ; audit de
   symétrie (R4) écrit avant le prononcé.
6. **Rapport** à la mère : issue, réserves, nœud.

### Comparaisons et corrections

Famille de taille : Holm sur 19 cellules. Deux bras primaires (La, Ld) : intervalles de ρ ajustés de Bonferroni. Lignes par
lignes, gains appariés et McNemar : rapportés sans correction, **aucun critère** n'en dépend sauf P9 (secondaire, lu à part).
Contrôles appariés : toutes les comparaisons sont sur les mêmes issues ; le bras J8 sert de témoin des dents ; la ligne Q1 et
l'essai E0 de cas sains ; Q6 de témoin positif du trou à deux niveaux du v9.

## Critères de lecture gelés

Lecture dans cet ordre ; un étage non franchi arrête la lecture des suivants.

| étage | observé | verdict |
|---|---|---|
| 1 | une cellule de taille « non tenue » (Holm), **ou** une promotion sur une cellule fatale, **ou** un log W > 10⁻⁶ sur une cellule fatale | **« trou »** : défaut de code, de certificat ou de preuve ; rien d'autre n'est lu ; audit écrit ; nœud |
| 2 | dents non tenues (J8 sur Q2 à Q5, J9 sur Q6) | **« banc sans dents »** (non concluant) |
| 3 | moins de 2 lignes informatives | **« prix du v9 non reproduit sur ce banc »** (non concluant sur H-1.1) ; P5 réfutée |
| 4 | pour X ∈ {La, Ld} : borne basse de ρ_X ≥ 0,5 / borne haute < 0,25 / autre | « X recouvre » / « X ne recouvre pas » / « X recouvre en partie » |
| 5 | taux de La sur Q3, Q4, Q5 ; de Ld sur Q5 ; de La et Ld sur Q6 | rapportés (prix de la restriction), sans verdict |

**Issue rendue pour le nœud R-1779** (si les étages 1 à 3 sont franchis) :
- **(A)** « Ld recouvre » : un nul moins coûteux qui ferme encore les copies par sous-population et au signe d'un trait existe
  sur ce banc ; candidat à une version neuve du nul, **à valider à part** (nœud de Lazar).
- **(B)** « La recouvre », Ld non : un nul moins coûteux n'existe sur ce banc **qu'en rouvrant** la forme de W2 ; la décision
  dépend de la question de sens (R-1768, R-1779), ouverte.
- **(C)** ni La ni Ld ne recouvrent (bornes hautes < 0,25) : le prix du v9 ne vient pas du nombre de coupures ; pas de nul moins
  coûteux dans cette famille ; le nœud se réduit à « accepter le prix » ou à un autre dessin.
- **(D)** autre combinaison : « non tranché », avec les estimations ponctuelles.
- P8 et P9 sont lues à part (secondaires), sans changer l'issue.

**Audit de symétrie (R4)**, écrit avant le prononcé, pour **toute** issue : membres dominants par cellule (sur Q2 à Q6, le
membre par morceaux attendu doit dominer dans la majorité des répétitions refusées) ; distribution des écarts de certificat ;
comptes des vérifications de nichage et de monotonie ; décomposition de ρ ligne par ligne ; « trop propre » : une part
recouvrée ≥ 0,95 sur toutes les lignes, ou ≤ 0,05 sur toutes, ou toutes les prédictions vraies, déclenche une relecture
écrite du code d'évaluation (règle « trop beau = réserve »).

## Liste d'arrêt

| condition | action |
|---|---|
| copie de `nul_v9.py` absente, ou empreinte ≠ `7ae450df…` | pas de jeu (préalable 1) |
| un fichier gelé diffère de l'addendum, un essai échoue, une mutation survit | pas de jeu |
| essai E0 : La ≠ J8 (au-delà de 10⁻¹² nat) sur une archive sans condition | arrêt avant le jeu ; défaut |
| une exception dans une évaluation | arrêt du run entier ; aucune lecture partielle ; relance seulement sous un texte ou un addendum neuf (aucun repli silencieux, R5) |
| un log W non fini | arrêt ; défaut |
| monotonie violée : log W de J9, La, La2 ou Ld > log W de J8 + 10⁻⁶ à un instant | arrêt ; défaut de code |
| nichage violé : log W de La ou Ld < log W de J9 − g_max − 10⁻⁶ | arrêt ; défaut de code, ou famille du v9 différente de [PREUVE] § 3 : audit, nœud |
| plus de 1 % des évaluations avec un écart de certificat > 10⁻⁴ nat | rapporté (la validité tient ; la puissance des bras limités est sous-estimée) ; le nichage se vérifie avec l'écart réel |
| durée murale > 48 h | arrêt ; run invalide, aucune lecture |
| une lecture avant le scellement de la sortie | run invalide |
| toute demande d'instance payante ou d'appel de modèle | interdit (R-2851 : processeur, sans dépense) |

## Coût

**Processeur seul, 0 dollar.** Temps d'évaluation : J8 ≈ 0,02 à 0,03 s à 200 tirages (essai à blanc du 15 novembre, annexe B) ;
J9 ≈ 0,25 s (« 0,25 à 0,29 s mesurées » par évaluation appariée v8 et v9, note W2, `4d3a6d1c…`, tableau de la section 2) ;
bras limités ≈ 0,05 à 0,3 s (estimation : 2 à 5 partitions au lieu de plusieurs centaines). Par répétition ≈ 0,4 à 0,9 s pour
les cinq bras ; 19 000 répétitions ≈ 2 à 5 heures d'un cœur, 1 à 3 heures sur deux processus ; borne dure 48 heures. Écriture
du code, essais, mutations, contre-lectures : temps d'agents de la session, sans dépense. Aucune machine louée.

## Écarts, nœuds et ce que l'essai ne décide pas

- **Préalable 1 (décision de la mère ou mot de Lazar)** : verser une copie empreintée de `orchestrator/pole/nul_v9.py`
  (`7ae450df…`), et, pour lecture seulement, de `orchestrator/demonstrations/banc_tricheurs_v9.py` (`7e4bff59…`) et de
  `orchestrator/prereg/rapport-redaction-nul-v9.md`, depuis le dépôt public `lciric/ideation-organism`, en lecture seule, sur le
  modèle de R-2148. Je ne l'ai pas fait.
- **Le banc** ne s'écarte d'aucune conception scellée : il ne touche ni le juge de production (v8), ni le v9, ni la boucle.
- **Nœud de Lazar** : adopter La, La2 ou Ld comme nul du juge serait une version neuve du nul, donc une modification du juge
  (option « chercher un nul moins coûteux » de R-1779), avec sa propre validation scellée.
- **Variante des fiches écartée** : poids appris en ligne ou sur une moitié des tirages : non valides ([PREUVE], § 8) ; non jouées.
  La correction est à porter au relevé.
- **Ne décide pas** : la question de sens (une copie par sous-population est-elle une découverte ?) ; la puissance sur les
  mondes riches à 8 traits (classe différente : C_arch y grandit avec l'archive, et le prix en puissance avec lui) ; le contrôle
  d'erreur entre générations ; la réserve log-linéaire du v8 ; toute revendication publique (clause de N-067 sur le nul formé des
  lois connues).

## Contre-lecture

Aucune à ce jour : ce texte v1 est le brouillon soumis à la contre-lecture (R2). À confier à un sous-agent neuf d'un autre
modèle que l'auteur (modèle B, R-2851), qui n'a écrit ni ce texte, ni [PREUVE], ni le juge. **Fichiers à lui donner
explicitement** : ce texte ; [PREUVE] (`44f24940…`) ; la copie `94bfd92` : `pole/selection_pari.py`, `pole/nul_filles_v2.py`,
`pole/nul_v8.py`, `pole/cycle.py`, `pole/a_blanc_v59.py` ; le relevé (`bd253b6c…`, § 1.1) ; les fiches n° 0, 9, 13, 14 de
`sortie--fiches-validees.json` ; l'audit du verdict du v9 (`9086a420…`) ; la note W2 (`4d3a6d1c…`, sections 2 et 3) ; la page
publique (`c549a31b…`, l. 55 à 66) ; et `nul_v9.py` dès qu'il est versé. Questions à trancher : définitions des lignes
(appartenance aux classes du tableau) ; montage « mêmes issues, empreintes différentes » ; règle d'informativité ; statistique
ρ et son intervalle ; liste d'arrêt. Chaque remarque reçoit un traitement écrit (acceptée, refusée et pourquoi) dans la
version suivante, avec l'empreinte du brouillon relu et celle du rapport.

## Annexe A — compte de dimensionnement des doses (sans juge, sans nul)

Information moyenne par épisode E_x KL(M ‖ S1) des lignes V, sur 300 mondes par dose et 4 000 instances par monde, mêmes
familles que le banc. Elle ne dit rien d'une promotion : elle place les doses autour du seuil log 20 ≈ 3 nats sur 200 épisodes.
Sortie (script `c52b822296e2f4b5d0417e5400e99d5626217ebba667ab5ddfb990f9cf78ce93`, sortie
`e8899d3fdf21640e7568e569091f0fef6d5376d4fab3240f0f5eac53f9d602d9`, dossier de travail de la session ; recopiés en entier) :

```
V1 effet neuf global                   dose 0.25 : médiane 0.0112 nat/épisode [quartiles 0.0062 ; 0.0208] ; sur 200 épisodes : 2.2 nat
V1 effet neuf global                   dose 0.50 : médiane 0.0611 nat/épisode [quartiles 0.0283 ; 0.0993] ; sur 200 épisodes : 12.2 nat
V1 effet neuf global                   dose 0.75 : médiane 0.1143 nat/épisode [quartiles 0.0564 ; 0.1988] ; sur 200 épisodes : 22.9 nat
V2 conditionnelle au signe             dose 0.40 : médiane 0.0107 nat/épisode [quartiles 0.0078 ; 0.0148] ; sur 200 épisodes : 2.1 nat
V2 conditionnelle au signe             dose 0.80 : médiane 0.0441 nat/épisode [quartiles 0.0318 ; 0.0586] ; sur 200 épisodes : 8.8 nat
V2 conditionnelle au signe             dose 1.20 : médiane 0.1011 nat/épisode [quartiles 0.0718 ; 0.1271] ; sur 200 épisodes : 20.2 nat
V3 conditionnelle à seuil décentré     dose 0.40 : médiane 0.0122 nat/épisode [quartiles 0.0085 ; 0.0158] ; sur 200 épisodes : 2.4 nat
V3 conditionnelle à seuil décentré     dose 0.80 : médiane 0.0429 nat/épisode [quartiles 0.0290 ; 0.0555] ; sur 200 épisodes : 8.6 nat
V3 conditionnelle à seuil décentré     dose 1.20 : médiane 0.0993 nat/épisode [quartiles 0.0675 ; 0.1319] ; sur 200 épisodes : 19.9 nat
V4 loi neuve sur une sous-population   dose 0.10 : médiane 0.0151 nat/épisode [quartiles 0.0079 ; 0.0303] ; sur 200 épisodes : 3.0 nat
V4 loi neuve sur une sous-population   dose 0.20 : médiane 0.0491 nat/épisode [quartiles 0.0214 ; 0.0830] ; sur 200 épisodes : 9.8 nat
V4 loi neuve sur une sous-population   dose 0.30 : médiane 0.0890 nat/épisode [quartiles 0.0426 ; 0.1559] ; sur 200 épisodes : 17.8 nat
```

```python
"""Compte de dimensionnement des doses du banc B (processeur seul ; aucun juge, aucun nul, aucune issue jugée) :
information moyenne par épisode E_x KL(monde || S1), en nat, des lignes de puissance V1 à V4 telles que définies au
préenregistrement (familles du banc, 300 mondes par dose, 4 000 instances par monde). Ne mesure aucune promotion."""
import numpy as np

K, D = 3, 2

def soft(rng):
    return np.round(rng.normal(0, 1.5, size=(K, D)), 6), np.round(rng.normal(0, 0.3, size=K), 6)

def p_soft(W, b, z):
    s = z @ W.T + b
    s -= s.max(axis=1, keepdims=True)
    e = np.exp(s)
    return e / e.sum(axis=1, keepdims=True)

def kl(p, q):
    return float(np.mean(np.sum(p * (np.log(p) - np.log(q)), axis=1)))

def u_centre(rng):
    u = rng.normal(size=K); u -= u.mean(); return u / np.linalg.norm(u)

racine = np.random.SeedSequence(20261115)
for nom, doses in (("V1 effet neuf global", (0.25, 0.5, 0.75)), ("V2 conditionnelle au signe", (0.4, 0.8, 1.2)),
                   ("V3 conditionnelle à seuil décentré", (0.4, 0.8, 1.2)), ("V4 loi neuve sur une sous-population", (0.1, 0.2, 0.3))):
    for dose in doses:
        v = []
        for s in racine.spawn(300):
            rng = np.random.default_rng(s)
            W1, b1 = soft(rng)
            z = rng.normal(size=(4000, D)); g = rng.integers(0, 2, size=4000)
            p1 = p_soft(W1, b1, z)
            if nom.startswith("V1"):
                Wn = rng.normal(size=(K, D)); Wn -= Wn.mean(axis=0)
                pm = p_soft(W1 + dose * Wn, b1, z)
            elif nom.startswith(("V2", "V3")):
                j = int(rng.integers(0, 2)); t = 1 - j
                c = 0.0 if nom.startswith("V2") else float(rng.choice([-1, 1]) * rng.uniform(0.3, 0.8))
                E = np.zeros((K, D)); E[:, t] = u_centre(rng)
                pm = np.where((z[:, j] > c)[:, None], p_soft(W1 + dose * E, b1, z), p_soft(W1 - dose * E, b1, z))
            else:
                Wn, bn = soft(rng)
                pm = np.where((g == 1)[:, None], (1 - dose) * p1 + dose * p_soft(Wn, bn, z), p1)
            v.append(kl(pm, p1))
        v = np.array(v)
        print(f"{nom:38s} dose {dose:4.2f} : médiane {np.median(v):.4f} nat/épisode [quartiles {np.quantile(v, .25):.4f} ; {np.quantile(v, .75):.4f}] ; sur 200 épisodes : {200 * np.median(v):.1f} nat")
```

## Annexe B — essai à blanc du montage d'évaluation (copie `94bfd92`, hors banc)

Fait pour vérifier deux affirmations du plan d'analyse (le montage « mêmes issues, empreinte de chaque bras » passe les gardes
de `evaluer_v2` ; la trajectoire ne dépend, à l'instant t, que des t premières issues) et pour mesurer un temps. Il juge une seule
carte, copie à un seuil (z₀ > 0,3) de deux lois d'archive, sous le nul v8 : promue (log W = 32,9 à 200 tirages), ce qui est le
trou connu du v8 (validation du v9 : M01 et M02 promus à 0,986 et 0,972 sous le v8 apparié, audit `9086a420…`, § 3, point 2) ;
**déclaré** : la prédiction P3 a été écrite après cet essai, mais repose sur ces chiffres publiés de la validation du v9. Script
(`d024f09b4995c16bdb044cf45d33520fedd66a1b78d4a89794125302540c5dc2`) et sortie
(`26a67c1766d9c74e375731e580615deeb906c325f1f317eecb553cb469533a68`, second passage ; le premier donnait 0,12 s et 0,03 s),
recopiés en entier :

```
instants 25..200 égaux après changement des issues 201..800 : True
trajectoire sur un plan de 800 tronquée à 200 = trajectoire sur un plan de 200 : True
log W aux 8 premiers instants : [5.987282, 9.679428, 13.150506, 16.621681, 18.320322, 24.068355, 27.864485, 32.891102]
temps : 800 tirages, 32 instants 0.20 s ; 200 tirages, 8 instants 0.02 s ; membres du nul 7 d'archive
```

```python
"""Essai à blanc (processeur seul) sur la copie empreintée du code du juge (commit 94bfd92) : (1) la trajectoire de
richesse lue par `nul_filles_v2.evaluer_v2` à un instant t ne dépend que des t premières issues (propriété de préfixe,
sur laquelle repose le rejeu de l'allocation) ; (2) temps d'une évaluation sous le nul v8 à 200 et 800 tirages."""
import random, sys, time
sys.path.insert(0, "/home/user/controle-ia-travail/docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator")
from pole import selection_pari as sp, nul_filles_v2 as nf, nul_v8, cycle  # noqa: E402

K, DIM = 3, 2
rng = random.Random(11)
S1, S2 = sp.loi_softmax_aleatoire(rng), sp.loi_softmax_aleatoire(rng)
monde = {"type": "si_sinon", "condition": {"indice": 0, "seuil": 0.3}, "si": S1, "sinon": S2}
carte = monde
archive = {"S1": S1, "S2": S2}

def evaluer(n, issues, instances):
    entr = sp.tirer_instances(random.Random(5), 100, DIM)
    q = [1.0 / K] * K
    biblio = list(sp.BIBLIOTHEQUE_STANDARD) + [{"nom": "marginale_entrainement", "type": "fixe", "probas": q}]
    biblio += nul_v8.membres_archive_v8(dict(archive), None, K, DIM)
    e = nf.construire_engagement_v2("f", carte, instances, K, 0.05, biblio, 0, None,
                                    cycle.instants_reguliers(n, n // 25), plan_execution="ordre_naturel")
    g = sp.geler_engagement(e)
    t = {"empreinte_engagement": g.empreinte, "issues": issues, "plan_execution": "ordre_naturel"}
    return nf.evaluer_v2(g, t)

inst = sp.tirer_instances(random.Random(3), 800, DIM)
r2 = random.Random(4)
issues = [sp.tirer_categorie(r2, sp.proba(monde, x, [], 0)) for x in inst]
issues_b = issues[:200] + [(y + 1) % K for y in issues[200:]]
t0 = time.time(); a = evaluer(800, issues, inst); t1 = time.time(); b = evaluer(800, issues_b, inst); t2 = time.time()
c = evaluer(200, issues[:200], inst[:200]); t3 = time.time()
print("instants 25..200 égaux après changement des issues 201..800 :", a["trajectoire_log_w"][:8] == b["trajectoire_log_w"][:8])
print("trajectoire sur un plan de 800 tronquée à 200 = trajectoire sur un plan de 200 :", a["trajectoire_log_w"][:8] == c["trajectoire_log_w"])
print("log W aux 8 premiers instants :", a["trajectoire_log_w"][:8])
print(f"temps : 800 tirages, 32 instants {t1 - t0:.2f} s ; 200 tirages, 8 instants {t3 - t2:.2f} s ; membres du nul {len(nul_v8.membres_archive_v8(dict(archive), None, K, DIM))} d'archive")
```

## Citations obligatoires (N-064, N-067)

POPPER (Huang et al., ICML 2025 ; `a3c4b370…`) ; Dwork et al., arXiv 1506.02629 (`dcfbb9aa…`) ; Blum et Hardt, « The Ladder »,
arXiv 1502.04585 (`957ef473…`) ; Co-Scientist (Gottweis et al., Nature 655, p. 487-496, 2026 ; `351f49d8…`) ; et la liste de
`docs/decisions/decision-N-067-v1.md`, section 6 (chemins et empreintes dans [PREUVE], dernière section). Aucune revendication
n'est faite ici.
