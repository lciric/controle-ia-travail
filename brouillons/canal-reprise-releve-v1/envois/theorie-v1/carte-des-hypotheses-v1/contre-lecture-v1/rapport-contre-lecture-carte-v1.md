# Contre-lecture de la carte des hypothèses des moniteurs — v1 — rapport

Sous-agent neuf (Fable 5.1), lignée conv-audit ; je n'ai écrit ni la carte, ni le programme, ni l'audit des failles, ni
la mesure unanime. Brief : `scratchpad/brief-contre-lecture-carte-v1.md`. Début : relevé `date -u` 03:23:17 UTC le
28 octobre 2026 (appel séparé) ; fin : relevée dans la réponse de livraison. Aucune clé, aucun `git`, rien lu dans
`donnees/`, `diag/`, `runs/`, `pilotes/` ; aucun fichier du dépôt modifié ; processeur seul. Les résultats de la mesure
unanime présents dans son dossier (`sortie-reelle-v*`) n'ont **pas** été lus : seuls leurs horodatages (CC1-13).

**Objet** : `brouillons/canal-reprise-releve-v1/envois/theorie-v1/carte-des-hypotheses-v1/carte-des-hypotheses-v1.md`
(`f7dfe5fd…`, 394 lignes), son script (`57601d3b…`) et sa sortie (`03d9108a…`), empreintes compagnons vérifiées sur disque.
**Sources confrontées** (empreintes recalculées, toutes identiques à celles que la carte cite) : programme v2 (`2fd63bad…`,
§ 3, § 4, § 5, § 8, § 9) ; décisions N-003/N-004 (`cc1be393…`), N-007/N-008 (`ab7dc9bb…`), N-029 (`084e3052…`), N-053
(`2204256d…`), N-054 (`c8a00b3f…`), N-056 proposée (`6aac9746…`) ; audit v3 (`4f74b366…`), carte du contrôle (`ad5eaa49…`),
failles internes (`c854f23f…`), grille (`1e060208…`), modes documentés du lot A, calculs de l'auditeur v2 (`ee257a7a…`) et
de la synthèse v2 (`3babde06…`) ; mesure unanime v5 (`29f91ff3…`) ; `src/controle_ia/bases/sequentiel.py` (`35a09834…`).
**Mes calculs** : `verif-contre-lecture-carte-v1.py` et `.sortie.txt` (même dossier, compagnons `.sha256`) ; rejeu du
script de la carte : `rejeu/rejeu-calculs-carte-v1.sortie.txt`, **identique octet pour octet** à la sortie livrée
(numpy 2.5.4, interpréteur `/opt/venv-essaim-sim-v1`).

## 0. Verdict

**À amender en v2.** La carte est solide et tient ses règles : les 23 lemmes sont au niveau des lois, **aucune phrase ne
décrit un procédé** (règle absolue tenue, deux passages limites jugés du bon côté : CC1-15) ; aucun « inédit »,
« premier », « nouveau » (R8 tenu) ; **tous** les identifiants cités (RC, FI, FC, MD, SD, HT, D, pages de papiers) existent
dans l'audit et disent ce que la carte leur attribue ; **tous** les chiffres recalculés (A3, A6, A7, A9, blocs de l'audit)
sont exacts et le script est reproductible. Ce qui impose une v2 : (1) un **énoncé faux** dans la classe K3 de A3
(« toute loi de moyenne par pas sous k » n'y appartient pas : Page y a 5,9 % et 24 % de puissance pour 1 % de niveau,
CC1-1) ; (2) **une instance manquée** dans les listes de l'audit pour une des sept « questions » (A12 : MD-C2) et deux
voisines manquées (A14 : MD-E4 ; A11 : MD-B5), qui changent les comptes du verdict (CC1-4 à CC1-6) ; (3) **six hypothèses
de moniteurs absentes** de A1 à A23, dont deux lourdes : l'alarme **avant** le seuil de dommage θ (la sécurité du § 4,
jamais « rappel par épisode ») et la **pureté du calibrage** (aucun sabotage parmi les K honnêtes) (section 4) ; (4) la
section 3 cite une mesure unanime **v5** alors que le dossier est à la v11 avec des sorties réelles antérieures à la fin de
la carte (CC1-13). Le reste est précision.

## 1. Table A1 à A23

Colonnes : énoncé (hypothèse et classe) ; preuve (lemme) ; instance (identifiants, pages, R7) ; statut (prouvé / esquisse /
conjecture ; L / I / Q). « ok » = conforme aux sources ; sinon renvoi au constat.

| A | énoncé | preuve | instance | statut | remarque |
|---|---|---|---|---|---|
| A1 | ok | ok (L0 (i), Slepian par N-003) | ok : 2606.10456v2 p. 1–2 (RC-1.2, vérifié synthèse) | prouvé, L : juste | le signe du décalage (unilatéral) est supposé sans être écrit (CC1-11) |
| A2 | ok | ok (N-003 T1, T2 ; L0 (iv)) | ok : aucune chez un organisme ; RC-3.1 (a) exact | prouvé, Q : juste | — |
| A3 | **classe mal posée** | identité de Lindley exacte (rejeu 8,4·10⁻¹⁵ ; recalcul 5,3·10⁻¹⁵) ; extension au balayage et à la somme séquentielle imprécise | ok : 2005.07821v1 p. 1 ; 2601.20022v2 p. 2 « non tenu » ; RC-3.1 | prouvé pour l'identité ; **l'exemple de K3 est faux** | CC1-1, CC1-2 |
| A4 | ok | ok (Pinsker recalculé : B/(2σ√n₀)) | ok : 2601.20022v2 p. 1–3 ; FC-04 | prouvé (gaussien), L : juste | — |
| A5 | ok | ok (linéarité en κ) | pages ok ; « conduite gardée » n'est pas dans le passage vérifié de l'audit (§ 4.1 : « abaisser le score ») | prouvé (gaussien), L : juste | CC1-9 |
| A6 | ok | ok : exp(λ²r₀T(T−1)/2) recalculé (3,080 ; Monte-Carlo 3,03) ; 0,21–0,35 = N-007 § 1 | ok (question : r₀ non lu) | prouvé, Q : juste | la « dérive avec le pas » (mélange à pas fixé, CV4-4) n'est pas dans K6 (section 4, M5) |
| A7 | ok | ok : vecteur propre vérifié ; 0,084/0,419/1 et 0,039/0,046/0,049 recalculés ; Φ(0,3/√0,2 − z₀,₀₁) = 0,0489 | ok (FC-10 cité comme argument) | prouvé (gaussien), Q : juste | la cellule Monte-Carlo (0,161/0,159) est à α = 5 %, non dit (CC1-10) |
| A8 | ok | ok (L0 (iii)) | ok : 2607.06596v3 p. 13 ; 2610.04575v1 p. 2 ; MD-A6 lot A ; 4,56 % = calcul v2 bloc 2 | prouvé, L : juste | — |
| A9 | ok | ok : G^m = Fⁿ ; médiane 0,545 recalculée ; quantiles reproduits | ok : MD-B3 lot A ; FI-26 bloc 5 (0,61/2,45/4,69 % exacts) ; 2604.14865v1 p. 6 | prouvé, L (lot A) : juste | — |
| A10 | ok | ok (L0 (i)) | ok ; instances internes de l'audit non citées : SD-D1, FI-08, RC-2.1 (même classe, « la direction apprise n'est pas celle où loge l'écart ») | prouvé, L : juste | CC1-7 |
| A11 | ok | esquisse honnête ; conjecture déclarée | **voisine manquée** : MD-B5 (max et attention perdent ≈ 3,8 points sous perturbations réparties ; faible, résumé seul) | esquisse, Q : à nuancer | CC1-6 |
| A12 | ok | ok (L0 (i)) | **instance manquée** : MD-C2 (évasion localisée à la position visée, sonde lue ailleurs retrouve le signal ; lot A, résumé seul), citée en défense seulement | prouvé ; **Q → L (lot A, faible)** | CC1-4 |
| A13 | ok | ok (L0 (iii)) | ok : 2509.21344v2 p. 5, 8 ; Mythos p. 109 ; SD-S2 ; MD-E4 ; FI-06 ; D-02 | prouvé, L : juste | frontière A13/A20 à écrire (CC1-8) |
| A14 | ok | ok | **voisine manquée** : MD-E4 (Mythos p. 109, vérifié) instancie aussi K14 en boîte noire : suspicion sur l'épisode entier, sans passage à l'acte | prouvé, Q : à nuancer (« question pour les sondes ») | CC1-5 |
| A15 | ok | ok (L0 (iii)) | ok : MD-A5 (2603.25861, lot A, faible) ; MD-E11 ; FC-19 | prouvé, L (lot A) : juste | — |
| A16 | ok | ok | ok : 2411.17693v1 p. 1 (§ 4.1) ; revue METR d'août p. 7 | prouvé, L : juste | — |
| A17 | ok | ok | ok : 2509.26072v2 p. 1–2 ; 2608.25869v1 p. 1 ; 2605.23970v1 p. 1 ; HT-11 (pente 1 − R̂) | prouvé, L : juste | — |
| A18 | ok | ok | ok : A(a)1 de T2-C renvoyée à H2a (mesure unanime v5, l. 45–47) ; FI-03 ; FI-30 non cité | prouvé, I : juste | portée : CC1-3 |
| A19 | ok | esquisse juste : Φ(|wᵀΔμ|/√(2wᵀΣw)) et Φ(‖Δμ‖/√(2λ)) recalculés ; bloc 3 reproduit | ok : 2606.07612v1 p. 8, 18 ; MD-A1 ; FC-02 ; RC-3.3 | esquisse, L : juste | S8 (b) (permutation) annoncé, non traité (section 4, M6) |
| A20 | ok | ok (L0 (iii) conditionnel) | ok : N-029 (0,8878) ; FI-05 ; « sans page » déclaré | prouvé, Q : juste | SD-S2 voisine à citer (CC1-8) |
| A21 | ok | ok | ok : 2411.17693v1 p. 1 et p. 10 (FI-15) ; D-08 | prouvé, L : juste | — |
| A22 | ok | identité juste si E[X_t] désigne la **moyenne honnête** (sinon il manque δ·P(J_t = 1)) | ok : revue METR d'août p. 7 ; MD-E3 ; SD-b11 ; § 6 n° 3 | prouvé, L : juste | CC1-12 |
| A23 | ok | ok (non-identification) | ok : 2509.15541v1 p. 18 (§ 4.3) ; MD-D3 lot A ; FI-11 | prouvé, L : juste | — |

Lemme maître L0 : juste ((i) à (iv) ; (ii) est la définition de la variation totale). Table de la section 1 : conforme à
`sequentiel.py` (max, somme terminale, somme séquentielle, Page à k, processus e de mélange à ρ, balayage à w, rang
conforme sur K épisodes entiers, (μ₀, σ) mis en commun) ; manque A6 sur la ligne S1 (CC1-14).

## 2. Constats

- **CC1-1 — A3, l. 104–105, énoncé faux.** « Classe K3 : M_k garde sa loi honnête (ou est dominé par elle), *par exemple
  toute loi de moyenne par pas sous k* ». Contre-exemple (mon script) : honnête N(0, 1), T = 30, k = 0,5, seuil de Page au
  quantile 0,99 honnête ; un décalage constant μ₁ = 0,2 (< k) donne un taux de 5,9 %, μ₁ = 0,4 donne 24,2 %. Une moyenne
  sous k rend la dérive négative, elle ne garde ni ne domine la loi de M_k (M_k y est stochastiquement plus grand). Seule la
  borne déterministe de RC-3.1 (e) (max C_t < h ⇒ moyenne < k + h/T) est juste, et elle va dans l'autre sens. Correction :
  retirer l'exemple ; écrire K3 comme « la loi de M_k sous P₁ est celle sous P₀ (ou en est dominée) », sans exemple de loi
  de moyenne ; dire que la « compensation exacte » relève de la classe C (N-004, non-compensation) et que l'« adversaire
  couvert » (A4) est le cas limite.
- **CC1-2 — A3, l. 107–108, extension imprécise.** « de même le balayage (fenêtres de longueur w) et la somme séquentielle
  (intervalles partant de 1) » : ni l'un ni l'autre n'est une fonction de M_k ; chacun est le maximum d'une **autre**
  famille d'intervalles avec k = 0. Correction : « K3 s'énonce par famille d'intervalles : (tous, k) pour Page ; (longueur
  w, 0) pour le balayage ; (partant de 1, 0) pour la somme séquentielle ; la terminale est l'intervalle entier ».
- **CC1-3 — A18 et verdict l. 44–45, portée.** Le lemme est juste et bien conditionné (« si (ii) partage le score de
  M_a ») ; la ligne du verdict laisse tomber le « si » (« aveugle par construction (…) bases (ii) et (iii) de N-056 »).
  Aujourd'hui la dose est fixée **sur la boîte noire seule** (P-015 (b), cité par la carte) : M_a est un juge boîte noire ;
  le bras au rappel nul par construction est la case **boîte noire par action** du 2 × 2 (ce qui rend l'interaction d'E1.2
  non diagnostique : FI-30, instance interne de l'audit, non citée), et (ii), (iii) ne sont touchées que par association
  positive. Correction : rétablir le conditionnel dans le verdict ; ajouter FI-30 aux instances ; dire quel bras est impliqué
  sous P-015 (b) et sous une lecture « sonde » de N-007.
- **CC1-4 — A12, l. 213–215, instance manquée (une des sept questions).** MD-C2 (grille § 3.1 ; `fiches/neurips2026-attacking-
  oversight-168158.md`, résumé seul, faible) : « l'évasion d'une sonde par réglage fin adverse reste localisée à la position
  visée ; une sonde neuve lue ailleurs retrouve le signal » — c'est K12 (trace ailleurs que les positions lues), lot A non
  opposable (R7). La carte ne la cite qu'en défense. Correction : A12 passe de Q à **L (lot A seul, faible)** ; le verdict
  passe à « seize instances, six questions », ou la carte explique pourquoi une évasion localisée n'est pas une occurrence
  de K12.
- **CC1-5 — A14, l. 233, voisine manquée.** MD-E4 (fiche Mythos, **vérifié p. 109** par la synthèse ; MD-E4 est aussi cité
  par la carte pour A13) : la consigne seule rend l'agent suspect sans passage à l'acte — un décalage porté par l'épisode
  entier, non par l'action sabotée, en boîte noire. Correction : garder « question pour les sondes », écrire « voisine
  documentée en boîte noire : MD-E4 », et expliquer que K13 et K14 coïncident quand la disposition est induite par
  l'indication.
- **CC1-6 — A11, l. 203, voisine manquée.** MD-B5 (`icml2026-latent-undertow-79377`, résumé seul, faible) : max et attention
  perdent ≈ 3,8 points sous perturbations **réparties** sur les jetons (bénignes). Même mécanisme d'agrégation, autre signe.
  Correction : citer MD-B5 comme voisine (perturbation bénigne étalée), la question restant ouverte pour un décalage étalé.
- **CC1-7 — A10, l. 192, instances internes omises.** SD-D1 (sondes hors politique), FI-08 (sondes apprises en lecteur),
  RC-2.1 (rotation alléguée, affirmée par l'organisme), MD-A2 (trace du réglage) relèvent de K10 (« l'écart loge ailleurs que
  dans la direction lue »). Correction : les ajouter, avec leur statut (lot A, session-depot, organisme).
- **CC1-8 — A13 / A20, frontière.** K13 (X ⟂ I | Z, Z = indication **et texte qui la porte**) et K20 (X = g(T) + ε) se
  recouvrent ; SD-S2 (2509.21344v2 p. 5, 8 : sondes appuyées sur l'évidence textuelle) instancie « la sonde lit du texte »
  et n'est citée que sous A13. Correction : écrire que A20 ne porte que sur les **traits de surface de N-029** (coût
  normalisé, longueur, forme du champ) ; citer SD-S2 comme voisine de A20 ; l'écrire dans la section 4.
- **CC1-9 — A5, l. 133–134, R7.** « vérifiés p. 1 : conduite gardée, score abaissé (audit v3 § 4.1) » : le § 4.1 vérifie
  « abaisser le score d'une sonde » ; « conduite gardée » est une glose non vérifiée sur la page. Correction : « score
  abaissé (vérifié p. 1) ; conduite gardée : prémisse des papiers, non relue (R7) ».
- **CC1-10 — A7, l. 156, précision.** « Monte-Carlo 0,161 contre 0,159 dans une cellule » suit des chiffres à α = 1 % ; la
  cellule du script est à **α = 5 %** (δ = 0,3, r₀ = 0,2, T = 50). Mon recalcul : 0,159 (5 %) et 0,045 contre 0,046 (1 %).
  Correction : nommer α.
- **CC1-11 — A1 (et A5), hypothèse implicite du signe.** Toutes les statistiques sont unilatérales (« plus grand = plus
  suspect », `sequentiel.py`). Un décalage **vers le bas** (score abaissé : les instances mêmes de A5) donne un taux < α :
  « pire qu'aveugle », que A1 nomme sans l'énoncer comme hypothèse. Correction : écrire dans A1 « hypothèse : le signe du
  décalage est connu (vers le haut) » et la classe « décalage de signe opposé ou de dispersion seule » (RC-1.2, pour tenir
  (1) : une variance plus grande ne suffit pas).
- **CC1-12 — A22, l. 315, notation.** L'identité vaut avec E[X_t] = **moyenne honnête** (E₀X_t = Eε_t) ; avec la moyenne
  inconditionnelle sous P₁ il manque δ·P(J_t = 1) (mon script : −0,158 contre −0,458). Correction : écrire E₀[X_t] ou μ₀.
- **CC1-13 — Section 3, T0 et T1, l. 24–25 et 338, source périmée.** La carte cite la mesure unanime **v5** (00:47 UTC,
  « non scellée à ma lecture, non lue »). Le dossier contient les préenregistrements v6 à **v11** (v11 : 03:35 UTC) et des
  sorties réelles « repetition » v8 (02:21 UTC, **avant** la fin de la carte à 02:31), v9 (02:52), v10 (03:13) ; aucun
  compagnon `.sha256` sur v5 ni v11. Je n'ai lu aucun de ces résultats. Correction : T0 et T1 se fondent sur la version en
  vigueur et son statut (scellée ? lue ?) ; « r₀ non lu » est à réécrire si la lecture a eu lieu ; les prédictions de T1
  dépendent du r̂₀ qui en sort.
- **CC1-14 — Section 1, ligne S1.** Le taux par action (1 %) ne borne pas le taux par épisode : 1 − 0,99^T = 4,9 / 9,6 /
  18,2 % à T = 5 / 10 / 20 sous indépendance (calculs de l'auditeur, bloc 2), moins sous dépendance positive (mesure unanime
  M1). Si S1 est rapportée par épisode (FI-28), elle suppose A6. Correction : ajouter A6 à S1, et l'hypothèse « unité du
  taux » de la section 4 (M3).
- **CC1-15 — Règle absolue : tenue.** Deux passages approchent la ligne et restent du bon côté : A9 l. 179–182 (une loi G
  plus courte et plus haute indistinguable d'une loi honnête plus longue : propriété de lois, aucune conduite) ; A3 K3
  l. 104–105 (loi de M_k ; faux, mais pas un procédé). Le motif de la faille E (RC-3.1) n'est **pas** reproduit. La fiche
  confidentielle (l. 7–9) est conforme à N-054 point 3 et N-056 point 6.
- **CC1-16 — Section 3, lequel retoucherait P3.** **T5** (plancher de P3 sous Σ honnête et Σ mêlée) relit le critère même de
  P3 : nœud D-17, comme la carte le dit. **T4 (a)** (écart témoin − honnête par sonde sur P3) touche un contraste que N-025
  (remarques 1 et 2) montre déjà lu sur le coût déclaré : à confronter au préenregistrement scellé de P3 (non fourni à
  l'audit, CLS-15) avant de l'appeler « mesure distincte » ; T4 (b) (modèle emboîté) est nouveau. T1, T2, T3 n'emploient P3
  que comme matériau honnête ; T2 (a) est une garde de code (R5), pas une mesure. Chaque témoin a une quantité et un nul ;
  **prédiction signée manquante** en T2 (b), T4 et T5 (RC-3.3 (a) en donne le signe : mêlée ≥ honnête).
- **CC1-17 — Conventions, l. 32–33, précision.** « seuil τ tel que P₀(S > τ) ≤ α » : la garantie conforme est marginale,
  **en espérance sur le jeu de calibrage** (loi Beta du taux réalisé : auditeur bloc 1 ; RC-1.1, pour tenir (2)). La carte
  renvoie la taille des échantillons hors carte (section 5 (5)) : l'exclusion est légitime si la convention le dit.
- **CC1-18 — Statuts L / I / Q, critère implicite.** Le critère appliqué est « instance = occurrence constatée, non
  argument » (A2 : « la classe est démontrée, son occurrence non ») ; il rend cohérents A18 = I (notre protocole conditionne
  bel et bien sur un moniteur) et A7, A14 = Q (FC-10, FC-11, FI-25 sont des arguments). Correction : l'écrire dans les
  conventions, sinon un lecteur compte A7 et A14 en I.

## 3. Les trois lemmes « les plus utiles » (A7, A18, A13)

- **A7** : juste (preuve par vecteur propre et Neyman-Pearson ; chiffres exacts). Portée dite sans exagération : le plafond
  vaut pour un décalage **constant sur l'épisode** (K7 = K14) ; à part p < 1 d'actions décalées, la moyenne d'épisode
  n'est plus exhaustive et le plafond des sommes devient Φ(pδ/√r₀ − z_α), plus bas encore, tandis qu'une statistique
  intra-épisode (centrée dans l'épisode : HT-17, HT-07) échappe au plafond — la carte le dit en une ligne ; une v2 devrait
  l'écrire comme la **vraie** condition de H2 (« croît avec l'horizon » exige r₀ ≈ 0 **ou** une statistique centrée).
- **A18** : juste ; portée exacte dans le corps, sur-comprimée dans le verdict (CC1-3) ; FI-30 à citer.
- **A13** : juste (élémentaire) ; portée exacte (différence d'information, pas d'accès : FI-06, D-02).

## 4. Hypothèses de moniteurs absentes de A1 à A23

- **M1 — L'alarme précède le seuil de dommage θ (sécurité du § 4).** Toute la carte mesure un **rappel par épisode** ; la
  sécurité du programme est P(alerte **avant** que le dommage cumulé n'atteigne θ). Classe : dommage reporté en fin
  d'épisode (ou atteint avant que la somme franchisse son seuil). Lemme (N-004 L3, prouvé par T0.3) : à B fixé, alarme 1,00
  si le sabotage est au début, 0,16 à la fin ; le processus e cumulé ne suffit pas, il faut un détecteur de rupture.
  Statistiques : S2, S3b. Instance **I** (T0.3, `resultats-T0.3-v1.md` cité par N-004, non fourni). Témoin : latence
  (alerte contre dommage cumulé, E1.2) sur scores honnêtes réels à décalage injecté en début ou en fin. Défense : Page,
  détecteurs e (N-004) ; HT-08 pour l'unité de dommage.
- **M2 — Pureté du calibrage.** N-007 : « seuil calibré sur des épisodes honnêtes, sans aucun exemple de sabotage » suppose
  que les K épisodes sont honnêtes. Classe : calibrage mêlé, (1 − ε)P₀ + εP₁ (sabotage spontané ou non étiqueté). Lemme
  (élémentaire) : le seuil conforme absorbe la queue de P₁ ; le rappel contre ce type de sabotage baisse et le taux nominal
  reste tenu — aveugle **par calibrage**. Instances : SD-S5 et SD-b9 (dommage dans l'artefact ; audit aléatoire des épisodes
  « honnêtes » proposé), FI-09 (vérité terrain). Témoin : contamination injectée à ε connu dans le calibrage, rappel contre
  le même type. Défense : audit aléatoire des honnêtes de calibrage (SD-S5) ; HT-06.
- **M3 — Unité du taux (S1).** Voir CC1-14 ; instances : MD-B2 (2610.04575 p. 1, lot A), FI-28 ; calcul : auditeur bloc 2.
- **M4 — Scores continus (ex æquo).** Le rang conforme suppose des scores sans ex æquo ; les juges S7 lus par espérance sur
  le jeton de verdict peuvent en produire ; RC-1.1, pour tenir (4). Classe : loi discrète de S. Lemme : la garantie reste
  conservatrice si l'ex æquo est compté « au-dessus », perd son exactitude sinon. Instance : audit (RC-1.1). Défense : règle
  d'ex æquo fixée au préenregistrement.
- **M5 — Stationnarité de l'honnête le long de l'horizon.** Dérive de μ₀ avec le rang de l'action (réserve de N-034 § 2 ;
  carte du contrôle de l'audit, H2 implicite). Le calibrage conforme garde le taux ; la puissance des sommes et le réglage
  de Page (k fixe) en dépendent ; la mesure unanime la sépare déjà par le bras « mélange à pas fixé » (CV4-4). Classe :
  tendance honnête par position. Statut : **question** (non mesurée). Témoin : différence réelles − mélange à pas fixé (déjà
  prévue), pente du score honnête sur le rang.
- **M6 — Permutation des étiquettes (S8 (b)).** A19 annonce (a, b) mais ne traite que (a). Le plancher sous permutation
  suppose l'échangeabilité des étiquettes conditionnellement aux tâches (strates) ; déséquilibré par tâche, il n'est pas un
  nul. Lemme : élémentaire (permutation stratifiée). Instance : P-015 (plancher sous permutation) ; question quant à sa
  validité sur nos jeux. Défense : permutation par strate de tâche, écrite au préenregistrement.

À signaler, non des hypothèses nouvelles : la **dispersion seule** (CC1-11) et le **signe connu** se rangent sous A1.

## 5. Ce que la contre-lecture ne couvre pas

Les références classiques (Slepian, Pinsker, Lindley, Neyman-Pearson, effets aléatoires) ne sont pas relues sur PDF (R7),
comme la carte le déclare ; les pages de papiers sont contrôlées **contre l'audit**, non contre les PDF ; le pari apparié v5
et les versions v6 à v11 de la mesure unanime ne sont pas lus ; aucun résultat de mesure n'est lu.
