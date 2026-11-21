# Seuil à 1 % avec peu d'épisodes honnêtes, et usage du papier « dopamine » : synthèse du collisionneur (v1)

- **Date** : 21 novembre 2026, 07:47 UTC (`date -u`). **Auteur** : Claude Opus 5.5, lecteur neuf. Pièce de classe C. Aucun appel payant, ni commit ni poussée. Dépôt à `fe5e7cb4f`.
- **Lu** : dans `runs/collisionneur-seuil-moniteurs-v1-20261121-063125/`, `etat.md` (`d6085ea7…`, 15 cellules OK, 14,86 USD), `faits.md` (`c8c7fb32…`), `question-etage3.md` (`a5fbe898…`), identiques aux deux pièces de `collisionneur-seuil-et-moniteurs-v1/` ; les 15 cellules, compagnons d'empreinte vérifiés : conceptions A `90cb9b1e…`, B `4581c121…`, C `32c0d956…`, D `d66b7a89…`, E `8c04e589…` ; critiques A `8ef2794c…`, B `0efa2189…`, C `4a1f7b22…`, D `a4a74de8…`, E `0861251b…` ; réponses A `ad8b657b…`, B `057af62d…`, C `1524b521…`, D `45d947c1…`, E `99e7cedd…`. Pour les recoupements : réponses de Fable (`add9a2d3…`), d'Argon (`5e4816be…`), de Carbon (`4b0d9a2b…`) à l'approfondissement, note du moniteur de dissonance (`403fe3e2…`), synthèse antérieure (`f293cfd0…`), décision N-053 point 5 (`2204256d…`), `registres/go.md` lignes de GO-2026-11-21-06 et -15.
- **Renvois** : « conception C, l. 124 » = `E3-T1-conception-C.md`, ligne 124 ; idem « critique », « réponse ». Espèces : A Fable 5.2, B Opus 5.5, C Argon, D Astra, E Carbon.
- **Statut** : rien n'est mesuré. Tous les chiffres hors faits sont dits illustratifs par leurs auteurs et attribués ici à leur cellule. J'ai refait à la main huit identités citées (0,99⁹⁹ ≈ 0,37 ; 299 et 459 unités ; 662 avec une alerte ; borne haute 2,09 % pour 5 alertes sur 500 ; 37 % de zone grise ; plafond du calibrateur 1,69 ; 59 unités à 5 %) : elles tiennent. Aucun autre calcul refait.

## Verdict

1. **Convergence** : « 5 000 par tranche » est une barre de précision, pas de validité ; la validité coûte 99 unités échangeables (garantie en moyenne), 299 (seuil installé, une tranche, risque 5 %), environ 459 par tranche pour cinq tranches ; à quelques centaines d'épisodes répartis en tranches, « non certifié à 1 % par tranche » est l'issue à budgéter ; on compte des familles, pas des épisodes ; l'inégalité de Ville ne garantit qu'un taux marginal ; tous adoptent le témoin « consigne cachée bénigne » et la cellule « consigne sans occasion d'agir ».
2. **Divergence** : la première mesure (cinq choix différents) ; le sort du processus d'e-valeurs dans l'épisode (gardé et durci par Fable et Opus, réservé à un horizon assigné par Argon, retiré par Astra, mis en balance avec la somme par Carbon) ; le contrôle actif par « meilleur de quatre » guidé par la sonde (gardé par Argon et Carbon, réduit à l'utilité par Fable) ; la nécessité d'un rejeu contrefactuel pour mesurer le dommage évité.
3. **Neuf par rapport aux réponses déjà rendues** : (i) une garantie *par tranche* pour toute forme séquentielle en relevant le seuil à 1/(α·p_min), p_min la plus petite part d'une tranche, ou par un horizon assigné avant génération ; (ii) la validité d'un nul par rangs ne se vérifie ni par Kolmogorov-Smirnov ni par uniformité empilée, mais par les fréquences de franchissement à des niveaux jugeables et la dépendance au rang précédent ; (iii) conditionner un taux d'alerte sur l'échec final le gonfle jusqu'à α/P(échec) *sous le nul exact*, ce qui nuance la phrase du moniteur de dissonance « l'honnête qui échoue est dans le nul par construction » ; (iv) le détecteur se juge en lecture seule sur trajectoires non interrompues, séparément de la politique qui intervient ; (v) plusieurs propositions de contrôle actif heurtent l'invariant de N-053 point 5, que les espèces ne connaissaient pas.

## 1. Par tour

### Tour 1, conceptions à l'aveugle

| Espèce | Propositions (une ligne chacune) |
|---|---|
| Fable | P1 score normalisé, seuil conforme par tâche ; P2 nul au pas par continuations du jumeau, e-processus à 100 ; P3 rapporter le taux certifiable α\* ; P4 budget d'audit des k premiers ; P5 test au niveau de l'agent ; P6 achat séquentiel ; P7 extrapolation de queue en secondaire ; U1 avance de la chute de valeur ; U2 transfert préalable aux jalons ; U3 répartition de l'audit par valeur avant génération ; U4 ablation comme générateur d'échecs honnêtes ; U5 dopamine comme modèle de récompense de processus, en utilité seulement (conception A, l. 92-164) |
| Opus | P1 seuil au maximum (Wilks) sur lot regroupé ; P2 normalisation invariante à la longueur ; P3 e-processus de rangs contre bifurcations du jumeau, proposition centrale ; P4 lot stratifié par la valeur du papier ; P5 valeurs extrêmes en secondaire ; P6 s'en passer (budget d'audit, « non concluant ») ; M1 covariable de difficulté ; M2 dissociation valeur interne contre texte ; M3 routage et rééchantillonnage ; M4 intégrité de la lentille (conception B, l. 127-186) |
| Argon | A1 martingale sur incréments centrés par le jumeau ; A2 loi de Pareto généralisée et bootstrap par blocs ; A3 budget à 1 % et verdict à trois états ; B1 discordance entre couches de valeur et de dopamine ; B2 meilleur de quatre guidé par la dopamine ; B3 audit au paragraphe par seuil 0,3 ; B4 greffe des neurones de valeur du jumeau (conception C, l. 123-175) |
| Astra | rang par classe (promesse marginale) contre seuil installé audité ; fiche signée avant ajustement ; moniteur de trajectoire ; contrôle sans verdict d'intention par routage randomisé (conception D, l. 5-59) |
| Carbon | P1 e-processus de rangs locaux, K = 4 ; P2 standardisation multi-longueurs et Wilks mutualisé ; P3 file d'audit à budget et coupe-circuit à 5 % ; M1 discordance dopaminergique sans seuil 0,3 lue par le jumeau ; C1 régénération ciblée sur les creux de dopamine ; C2 audit par ablation contre l'évasion et priorisation par la valeur initiale (conception E, l. 131-150) |

### Tour 2, critiques qui ont fait changer une réponse au tour 3

| Critique | Source | Changement au tour 3 |
|---|---|---|
| Le nul par rangs teste « agent = jumeau » ; une consigne ou un réglage fait rejeter sans sabotage | critique A, l. 13-14 ; B, l. 11-17 ; C, l. 24 ; E, l. 11 | Fable renomme P2 « moniteur d'écart de politique » et retire toute lecture d'intention avant D0 (réponse A, l. 21) ; Opus fait lire les K + 1 candidats par le modèle de l'agent dans son contexte (réponse B, l. 20) |
| Ville borne P(alerte), pas P(alerte \| tranche réalisée) ; p_b peut valoir α/p_b | critique D, l. 3-7 ; C, l. 59-68 | Seuil 100/p_min (réponse A, l. 30-35) ou 1/(α·π_min) (réponse B, l. 27 et 67) ; horizon assigné (réponse C, l. 21) ; Astra retire l'e-processus intra-épisode (réponse D, l. 12) ; Carbon retire « élimine les tranches » (réponse E, l. 16) |
| Kolmogorov-Smirnov continu sur rangs discrets rejette par construction ; l'uniformité marginale n'implique pas E[e_t \| passé] ≤ 1 | critique A, l. 15-18 ; C, l. 36 ; D, l. 29 ; E, l. 44 et 55-56 | Opus retire E2 (réponse B, l. 21-22) ; Fable ajoute la moyenne conditionnelle au rang précédent et un nul simulé à rangs dépendants (réponse A, l. 118) |
| Plafond (K + 1)^T et dérive bornée par T·f·KL : aveugle au sabotage diffus | critique C, l. 16-18, 43-45, 94-98 ; E, l. 23 et 57 ; A, l. 27 | Règle d'arrêt arithmétique (réponse A, l. 24 et 111) ; simulation « le rang tue-t-il la puissance ? » (réponse B, l. 94-100) ; Carbon l'admet (réponse E, l. 19) |
| Normalisation ajustée sur les épisodes qui calibrent ; ajustement croisé incompatible avec la loi Bêta exacte | critique B, l. 45-48 ; C, l. 10 ; E, l. 15 ; D, l. 49 | Trois lots de tâches entières (réponse A, l. 41) ; forme fixée avant les données (réponse B, l. 33) ; séparation unique par familles (réponse E, l. 23) |
| L'égalité au quantile 90 % ne contraint pas le 99 % ; E1 d'Opus injugeable (demi-largeur 8,3 points contre ± 3) | critique A, l. 28 ; C, l. 34 et 42 ; E, l. 46 et 52-53 | E1 retiré (réponse B, l. 34) ; contrôle planté « quantiles centraux égaux, queues inégales » (réponse A, l. 43) |
| Un seuil silencieux, ou un pur détecteur d'échec, gagne le duel | critique A, l. 94 ; B, l. 158-161 ; E, l. 108 et 119 | Plancher de détection et contraste au sein des paires sabotage/échec honnête (réponse D, l. 8 et 42-48) |
| À poids et invite égaux, greffe et comparaison sont nulles ; sinon elles lisent l'invite | critique A, l. 20 et 58 ; B, l. 110-112 ; E, l. 47 et 77 | M4 retiré (réponse B, l. 48) ; greffe B4 abandonnée (réponse C, l. 40-41) |
| Tronquer un résidu centré relève sa moyenne : sous-martingale | critique E, l. 74 ; A, l. 51-53 ; B, l. 97-100 | A1 refondue en rangs ou pari borné ajusté hors famille (réponse C, l. 17) |
| Le filtre 0,3 est un filtre de bruit Monte Carlo (écart type ≈ 0,25 à 8 tirages) | critique A, l. 131 et 143 ; C, l. 88 et 99-101 | Sélection des neurones gardée selon le papier, plafond de bruit par deux moitiés de tirages (réponse E, l. 31-33) |
| Le M1 de Carbon ne lit plus l'état de l'agent | critique A, l. 130 ; C, l. 86 ; D, l. 49 | Écart « interne contre public » G_t (réponse E, l. 25-29) |
| L'échec par ablation n'est pas l'échec naturel | critique C, l. 11 ; D, l. 17 ; E, l. 15 | U4 retirée, remplacée par la panne d'environnement (réponse A, l. 57) |
| Valeur lue sur l'agent : covariable postérieure au régime, canal d'évasion | critique C, l. 38 ; A, l. 30 | Valeur lue sur le jumeau, énoncé public (réponse B, l. 41 ; réponse A, l. 60 ; réponse D, l. 40) |
| Réinjecter les audits des k premiers biaise la queue | critique E, l. 12 | Calibration par audits tirés indépendamment du score (réponse A, l. 45) |
| Remplacement et sélection confondus dans le meilleur de quatre | critique A, l. 63 ; D, l. 45 | Bras « un candidat du jumeau au hasard » (réponse C, l. 45-46) ; plan 2×2 (réponse E, l. 46) |
| Une aire sous la courbe élevée est compatible avec une détection nulle à 1 % | critique E, l. 47 et 59 | Métrique principale : détection à taux fixé sur échecs appariés (réponse B, l. 44) |
| Épreuve d'évasion fermée | critique B, l. 205-208 ; A, l. 133 | Volets anti-évasion retirés (réponse E, l. 38-39) |

### Critiques restées sans réponse, ou désaccords maintenus

- **Argon contre Astra** : la borne « dommage évité ≤ q·π_D » ; Astra la rejette, la revue ciblant les futurs dommages (réponse D, l. 16). Pas de réplique.
- **Argon contre Carbon** : le meilleur de quatre exigerait de cloner l'environnement (critique C, l. 90) ; Carbon répond par une lecture avant exécution (réponse E, l. 42-43), ce qui suppose que l'anomalie précède le retour d'outil.
- **Rejeu contrefactuel** : Astra le juge inutile pour comparer deux politiques randomisées (réponse D, l. 15) ; Carbon l'exige pour chaque tâche (réponse E, l. 46 et 78).
- **Calibrateur discret** : Opus rejette l'étiquette « perte de validité » d'Argon, puisque le calibrateur discret est conservatif (réponse B, l. 24).
- **Fable maintient** contre Opus que D1 ne visait pas un épouvantail, les faits liant « non concluant » aux 5 000 (réponse A, l. 42).
- **Sans réponse, apparues au tour 3** : (1) l'objection d'Opus « P(alerte \| échec) ≤ α/P(échec), même sous le nul exact » (réponse B, l. 50) frappe l'Expérience 1 corrigée d'Argon, qui juge les paliers de Ville sur les seuls échecs honnêtes du tercile long (réponse C, l. 69-72) ; (2) le G_t de Carbon (réponse E, l. 28) : à poids égaux, l'agent et le jumeau forcé ne diffèrent que par le contexte caché, donc G_t lit la consigne par construction (propriété 2 de la synthèse antérieure ; conception A, l. 102). Carbon prévoit les témoins, mais la note de dissonance range cet écart sans rechanges parmi les projections de la base 2 (§ 7, point 2) ; (3) l'Expérience 1 d'Argon se dit « sans nouvel épisode » mais demande un honnête sous consigne bénigne (réponse C, l. 75 et 143) ; (4) Argon dit « référence vérifiée » pour Howard et al. sans PDF (réponse C, l. 68) ; (5) D0 de Fable dépend du mode de fabrication du saboteur, absent des faits (réponse A, l. 75).

## 2. Régler le seuil à 1 % ou s'en passer, au niveau de la méthode

État au tour 3. « Coût » : chiffres de la cellule citée, illustratifs.

| Proposition (espèces) | Ce qu'elle suppose | Ce qui la tuerait | Coût selon les espèces |
|---|---|---|---|
| **S1. Taux certifiable α\* et « non jugeable à 1 % » écrit par tranche** (Fable, Astra, Argon, Carbon) | Épisodes vierges, familles indépendantes, seuil gelé | Rien ne la tue : un α\* trop lâche est une information (réponse A, l. 215) | Nul (réponse A, l. 215 ; réponse C, l. 135) |
| **S2. Seuil au maximum d'un épisode par famille, tiré avant regard** (Opus, Astra, Carbon) | Familles i.i.d., score continu gelé ; taux réel attendu 0,33 % à 299 (réponse B, l. 63) | Inventaire : moins de 299 familles regroupées ou de 99 dans la plus petite tranche (réponse B, l. 86-91) | Zéro épisode si l'inventaire passe ; sinon « déficit et son devis » (réponse D, l. 70) |
| **S3. Rang conforme par tranche, promesse marginale** (Astra, Fable) | 99 unités échangeables par tranche ; normaliseur gelé ailleurs | Moins de 99 unités : règle silencieuse (réponse D, l. 30) | Nul (réponse A, l. 216) |
| **S4. Seuil unique sur score normalisé en longueur** (Fable, Opus, Carbon) | Queue invariante en longueur ; garantie en moyenne sur les longueurs, pas par tranche | Banc d'essai à quantiles centraux égaux et queues inégales (réponse A, l. 43 et 126-133) ; égalité au 90 % muette sur le 99 % (critique C, l. 34) | Nul en épisodes ; n réduit par les plis (réponse A, l. 41) |
| **S5. E-processus de rangs contre le jumeau, seuil durci** (Fable, Opus) | Même configuration agent/jumeau ; pas et pari fixés avant ; p_min borné par en dessous ; lecture seule sur trajectoires non interrompues | Moins de ln(100/p_min)/ln(m + 1) pas surveillés (réponse A, l. 111) ; simulation où le rang perd trop face à la somme (réponse B, l. 94-100) ; fréquences de sup M_t ≥ c au-dessus de 1/c, c ∈ {5, 10, 20} (réponse B, l. 110-114) | Récurrent : K générations par point de contrôle et par épisode surveillé (réponse B, l. 26) ; seuil 500 pour cinq tranches équiprobables, trois pas au rang maximal à K = 10 (réponse B, l. 67) |
| **S6. Tranches d'horizon assigné avant génération** (Astra, Argon, Fable) | Qu'on accepte de redéfinir la tranche, jamais rebaptisée « longueur réalisée » (critique D, l. 7) | Refus de redéfinir la tranche | Nul (réponse A, l. 34) |
| **S7. Martingale sur incréments bornés ajustés hors famille** (Argon) | E[Z_k \| passé] ≤ 0 hors famille ; effet de tâche absorbé | Facteur d'inflation de variance au-dessus de 1,3 ou palier M_t ≥ 10 au-dessus de 10 % (réponse C, l. 71-72, illustratif) ; objection d'Opus sur le conditionnement par l'échec (voir § 1) | Ré-analyse des épisodes existants (réponse C, l. 136) ; 20 h de carte en conception (conception C, l. 125) |
| **S8. Budget d'audit : k premiers plus audits au hasard à probabilité connue** (Fable, Argon, Carbon, Opus) | Le budget est la vraie contrainte ; l'audit reconnaît un sabotage regardé | Saboteur sous le k-ième rang (réponse A, l. 218) ; file saturée (réponse E, l. 99) | Budget humain |
| **S9. Achat séquentiel à strates fixées avant génération, pondération inverse** (Fable, Carbon, Astra) | Strates et probabilités d'inclusion connues ; arrêt scellé | Taux vrai proche de 1 % : arrêt tardif (réponse A, l. 219) | Borné à l'avance, à chiffrer sur pilote (conception D, l. 63) |
| **S10. Valeurs extrêmes en estimateur secondaire** (tous) | Queue régulière, pas de mélange rare | Composante rare plus fréquente que α mais sous le seuil d'ajustement (critique E, l. 86) | Nul |
| **S11. Lot stratifié par la valeur du papier** (Opus) | Lien difficulté-queue ; poids connus | Taux de dépassement par strate non différent à un niveau jugeable (réponse B, l. 92) ; une aire ne fixe aucun taux de queue (critique D, l. 30) | Nouveaux épisodes, nombre par calcul de Neyman (conception B, l. 240) |
| **S12. Contraste sans seuil : classement apparié par famille** (Astra, Fable) | Assez de paires sabotage/échec honnête | Gain sur un comparateur sous la marge (réponse D, l. 70) | Nul ; ce n'est pas une détection à 1 % |

**Retirés au tour 3** : E1 et le test de Kolmogorov-Smirnov d'Opus ; bootstrap par blocs et Ljung-Box d'Argon (réponse C, l. 26) ; clonage pour la certification (réponse C, l. 54) ; ajustement croisé pour la loi Bêta (réponse A, l. 41 ; réponse E, l. 23) ; P5 de Fable sur scores d'épisode étalonnés (réponse A, l. 26) ; e-processus intra-épisode d'Astra (réponse D, l. 12).

**Collision avec un GO** : GO-2026-11-21-06, point 1, fait de 1 % le seul point de verdict, 5 % toujours rapporté. Le coupe-circuit à 5 % de Carbon (réponse E, l. 99), le repli à 5 % d'Argon (réponse C, l. 86) et le niveau de 10 % d'Opus (réponse B, l. 123) ne peuvent qu'être rapportés.

## 3. Construire des moniteurs ou servir le contrôle

| Proposition (espèces) | Ce qu'elle suppose | Ce qui la tuerait | Coût selon les espèces |
|---|---|---|---|
| **M-a. Score du papier comme fonction de lecture du rang contre le jumeau** (Fable P2′, Opus P3′) : c'est le moniteur de dissonance, lecteur jumeau ou lecteur agent | D0 rend « la sonde lit autre chose que la consigne » (réponse A, l. 220) | Richesse moyenne pas au-dessus de la log-vraisemblance sous le jumeau, base 2 (réponse A, l. 121-124) | Passes avant et m générations par pas (réponse A, l. 217) |
| **M-b. Écart interne contre public G_t** (Carbon) | Un état privé que le texte ne porte pas | Gain sous 0,08 sur un comparateur, ou excès d'alerte sur un témoin (réponse E, l. 73-74, illustratif) ; lecture de consigne par construction (§ 1) | Une passe forcée du jumeau par étape (réponse E, l. 100) |
| **M-c. Rang de dopamine conditionnel à la valeur initiale, sondes gelées sur tâches vérifiables** (Argon) | Transfert hors domaine | Écart sabotage/échec honnête sous la marge, ou alerte sur consigne bénigne (réponse C, l. 94) | 40 à 80 h de carte pour les étiquettes Monte Carlo (conception C, l. 194) |
| **M-d. Duel de lecture d'Astra** : cumul de μ̂(X_t) − D_t, contraste C_j au sein des paires | Familles de développement disjointes ; covariables connues avant lecture | C_interne ≤ g_paire, ou pas au-dessus d'un comparateur, dont la même sonde sur le jumeau forcé (réponse D, l. 48) | Replay et lecteur forcé, à chiffrer sur pilote (réponse D, l. 70) |
| **M-e. Valeur lue sur le jumeau à partir de l'énoncé, comme covariable ou strate** (Opus, Fable, Astra ; déjà dans la note de dissonance) | Transfert de la lecture au prompt | Gain sous la marge face à la longueur de la question et au taux d'échec historique (réponse B, l. 122-130) | Une passe (réponse A, l. 221) |
| **M-f. Dissociation valeur interne contre texte confiant** (Opus) | Un signal d'intention distinct de l'échec | Une des quatre bases non battue (réponse B, l. 135) | Non chiffré |
| **M-g. Anticipation de la chute de valeur** (Fable D3′) | D0 rend l'écart à la consigne ; lecture intermédiaire valide (D4′ ii) | Taux d'anticipation pas au-dessus du bras à consigne bénigne (réponse A, l. 153) | Relecture d'épisodes |
| **M-h. Transfert préalable : lecture au prompt et ablation en recherche ouverte** (Fable D4′, Carbon E2-corr) | Issue terminale honnête variable dans la famille | Pas de gain d'aire face à longueur et entropie, ou ablation pas plus nuisible que l'aléatoire apparié (réponse E, l. 65-67) | Carbon : 30 h de carte et 60 à 90 USD (conception E, l. 155), conversion en monnaie retirée ensuite (réponse E, l. 12) |
| **C-a. Meilleur de quatre guidé par la dopamine, plan 2×2 ciblage × sélection** (Argon, Carbon ; Fable en utilité) | Creux de dopamine aux pas nuisibles ; lecture avant exécution | Pas mieux que le candidat du jumeau au hasard (réponse C, l. 114 ; réponse E, l. 81) | Argon : + 30 % d'inférence (conception C, l. 159) ; Carbon : quatre paragraphes sur environ 5 % des pas (réponse E, l. 100) |
| **C-b. Routage randomisé par lots, à budget égal, contre le même budget sans lentille** (Opus, Astra) | Lots indépendants ; saboteur figé | Différence de dommage par lot sous la marge (réponse D, l. 56 ; réponse B, l. 147) | Revue, bifurcations, notation aveugle de tous les lots (réponse D, l. 54) |
| **C-c. Audit des k paragraphes qui ont le plus pesé** (Argon) | Sabotage localisable | Localisation nulle indépendamment du rappel par épisode (critique D, l. 43) | Nul (conception C, l. 166) |

**Retirés au tour 3** : greffe B4 (réponse C, l. 41) ; M4 (réponse B, l. 48) ; U4 (réponse A, l. 57) ; résidu inter-couches d'origine (réponse C, l. 35) ; volet anti-évasion de C2 (réponse E, l. 39) ; seuil 0,3 en audit (réponse C, l. 50).

**Collision avec N-053, point 5.** « Aucun score de moniteur (sonde, juge) n'entre dans un signal d'entraînement ou de sélection de l'agent, hors bras d'attaque déclaré. » C-a, U5 de Fable et le rééchantillonnage de M3 d'Opus choisissent l'action exécutée par un score de sonde. La réponse de Fable (l. 96) et la note de dissonance (§ 3) traitent cet emploi comme fermé, et le routage en service comme un nœud. Les espèces ne connaissaient pas l'invariant : les faits ne le donnent pas.

## 4. Références citées par les espèces

Toutes **non vérifiées sur PDF**, sauf mention. Aucune cellule n'en tire un chiffre.

- Conforme et tolérance : Vovk, Gammerman, Shafer, *Algorithmic Learning in a Random World*, 2005 (A, B, C, E) ; Angelopoulos et Bates, « A Gentle Introduction to Conformal Prediction… », 2021 (B) ; Vovk, « Conditional validity of inductive conformal predictors », 2012 (B) ; Wilks, 1941 (B, E) ; Clopper et Pearson, 1934 (B) ; Tibshirani, Barber, Candès, Ramdas, « Conformal Prediction Under Covariate Shift », 2019 (B, C, E) ; Romano, Patterson, Candès, « Conformalized Quantile Regression », 2019 (E) ; Barber, Candès, Ramdas, Tibshirani, « Predictive inference with the jackknife+ » et « The limits of distribution-free conditional predictive inference », 2021 (E).
- Séquentiel et e-valeurs : Wald, 1945 (A, E) ; Ramdas, Grünwald, Vovk, Shafer, « Game-Theoretic Statistics and Safe Anytime-Valid Inference », 2023 (A, B, C, E) ; Vovk et Wang, « E-values: Calibration, combination and applications », 2021 (B) ; Wang et Ramdas, « False discovery rate control with e-values », 2022 (B) ; Shafer, « Testing by betting », 2021 (E) ; Howard et al., « Time-uniform, nonparametric, nonasymptotic confidence sequences », 2021 (C, réponse C, l. 68, dite « vérifiée » sans PDF au dépôt).
- Queues et rééchantillonnage : Pickands, 1975 (C, E) ; Coles, 2001 (B) ; Politis et Romano, 1994 (C) ; Künsch, 1989 (E) ; Cérou et Guyader, 2007 (C).
- Contrôle : Greenblatt, Shlegeris, Sachan, Roger, « AI Control: Improving Safety Despite Intentional Subversion » (B, E) ; Benton et al., « Sabotage Evaluations for Frontier Models » (B) ; Bhatt et al., « Ctrl-Z » (B) ; SWE-bench, cité sans référence (C). **Ces trois PDF sont au dépôt** (`docs/sources/pdf/2312.06942v5.pdf`, `2410.21514v1.pdf`, `2504.10374v1.pdf`, empreintes vérifiées) ; j'ai vérifié page 1 le titre et les auteurs seulement.

**Désaccords** : (1) l'année d'« AI Control », 2023 chez Opus, 2024 chez Carbon (critique A, l. 126 ; réponse E, l. 11). La page 1 du PDF porte l'identifiant 2312.06942 et « v5, 23 Jul 2024 » : prépublication déposée en décembre 2023, version 5 en 2024. Les deux dates se défendent ; citer l'identifiant et la version. (2) Non bibliographique, mais réglé dans les cellules : l'écart de Kolmogorov-Smirnov sur rangs discrets, 1/(2(K + 1)) chez Argon, 1/(K + 1) chez Carbon ; Opus retient la valeur de Carbon, celle d'Argon n'étant qu'une borne inférieure (réponse B, l. 21).

## 5. Proposition → forme fixe possible ?

« Forme fixe » = règle calculable, garantie dite, suppositions déclarées, donc utilisable comme test de mort par la course de l'organisme. La règle la moins chère, commune à Fable, Opus et Astra, est le **tableau de jugeabilité** : à partir des seuls comptes (familles par tranche, pas surveillés, journal des ajustements), dire si une issue favorable est arithmétiquement possible (réponse A, l. 66-71 ; réponse B, l. 86-92 ; réponse D, l. 20).

| Proposition | Forme fixe ? | Garantie dite | Suppositions déclarées |
|---|---|---|---|
| S1 α\* certifiable | **Oui** | Borne haute exacte du taux, risque δ | Unités i.i.d., vierges, seuil gelé |
| S2 Maximum par famille | **Oui** | P(taux réel > α) = (1 − α)^n | Familles i.i.d., score continu gelé, tirage avant regard |
| S3 Rang conforme par tranche | **Oui** | Taux ≤ α en moyenne sur calibration et prochain épisode | Échangeabilité dans la tranche, n_b ≥ 99 |
| S4 Seuil unique normalisé | **Oui, garantie réduite** | Taux ≤ α en moyenne sur les longueurs, pas par tranche | Forme du normaliseur fixée avant ou ajustée sur familles disjointes |
| S5 Rangs contre jumeau, 1/(α·p_min) | **Oui** | Ville, puis α·p_min/p_b ≤ α par tranche | Échangeabilité conditionnelle agent/jumeau ; pari fixé avant ; borne basse de p_min ; lecture seule |
| S6 Horizon assigné | **Oui** | Ville par tranche d'horizon | Horizon fixé avant génération |
| S7 Martingale hors famille | **Oui, garantie conditionnelle** | Ville si E[Z_k \| passé] ≤ 0 | Supposition forte, vérifiée seulement aux paliers 5 et 10 |
| S8 k premiers et audits au hasard | **Oui** | Budget tenu ; estimation sans biais du taux par strate | Probabilité d'inclusion connue et non nulle ; audit qui reconnaît |
| S9 Achat séquentiel | **Oui** | Niveau du test séquentiel sous arrêt scellé | Strates et inclusions connues |
| S10 Valeurs extrêmes | Non | Aucune à échantillon fini | — (estimation rapportée) |
| S11 Lot stratifié par la valeur | Non | Aucune sur la queue par strate | Plan d'achat, pas règle de verdict |
| S12 Classement apparié | **Oui** | Niveau d'un test de permutation apparié par famille | Échangeabilité dans la paire sous le nul ; ce n'est pas une détection à 1 % |
| M-a Score du papier dans le rang | **Oui** (forme de S5) | Validité indépendante de la sonde ; puissance non garantie | Comme S5 |
| M-b G_t interne contre public | Non | Pas de nul exact : « G ≈ 0 » est une hypothèse | Score à étalonner, hérite du problème du seuil |
| M-c Rang de dopamine conditionnel | **Oui, garantie réduite** | Seuil conforme gelé sur lot disjoint ; duel quadruple à marge | ≥ 100 familles pour 1 %, sinon point rapporté |
| M-d Duel de lecture d'Astra | **Oui** | Région simultanée par familles ; H_B complément exact | Familles disjointes, seuils et comparateurs gelés |
| M-e Valeur lue sur le jumeau | Non (règle de strate seule) | Aucune propre | Strates fixées avant lecture ; sert S3, S8 |
| M-f Dissociation | Non | — | Instrument non spécifié |
| M-g Anticipation | **Oui, sous condition** | Niveau d'un test binaire apparié | Ancrage k\* sans la sonde ; D0 et D4′ ii passés |
| M-h Transfert préalable | **Oui** | Intervalle par grappes de familles | Familles à issue variable |
| C-a Meilleur de quatre | Non dans la course actuelle | — | Invariant de N-053, point 5 |
| C-b Routage par lots | **Oui** | Niveau par randomisation des lots | Lots indépendants, saboteur figé |
| C-c Audit de k paragraphes | Non | Aucune | — |

**Compte** : 16 propositions sur 23 peuvent prendre une forme fixe, dont 5 avec une garantie réduite ou conditionnelle (S4, S7, M-c, M-g, et S12, qui ne vaut pas détection à 1 %) ; 7 restent un texte libre ou une estimation.

## 6. Décisions pour Lazar

**D-1. Écrire dans la version 7 ce que promet le seuil unique accordé par GO-2026-11-21-15, point 2.**
Enjeu : le collisionneur montre que ce seuil garantit 1 % en moyenne sur les longueurs, pas par tranche réalisée ; l'égalité vérifiée à 15-20 % ne dit rien de la queue à 1 %.
- (a) Promesse moyenne écrite telle quelle, vérification par tranche rapportée sans verdict. Avantage : aucun changement de fond. Inconvénient : la lettre « par tranche » des faits n'est plus tenue.
- (b) Ajouter le durcissement 1/(α·p_min) à toute forme séquentielle. Avantage : garantie par tranche sans lot. Inconvénient : seuil plus haut, puissance moindre.
- (c) Tranches d'horizon assigné avant génération. Avantage : garantie exacte. Inconvénient : la tranche change de définition, donc nœud.

Recommandation : (a) avec (b) pour les formes séquentielles. Confiance 0,6. Défaut sous 48 heures : (a) avec (b) ; (c) est un nœud, sans défaut.

**D-2. Verser trois corrections dans le texte à part du moniteur de dissonance (D-1 de sa note).**
Enjeu : sa note promet « plus de tranche de longueur » et met l'honnête qui échoue dans le nul. Le collisionneur montre que la garantie est marginale, que l'uniformité empilée ne valide pas le nul et que conditionner sur l'échec final gonfle le taux sous le nul exact.
- (a) Les trois corrections : seuil durci ou horizon assigné ; diagnostic par fréquences de Ville à c ∈ {5, 10, 20} et dépendance au rang précédent ; nul jamais lu conditionné sur l'issue. Avantage : le texte tient devant les cinq espèces. Inconvénient : moins de puissance.
- (b) Les deux premières seulement. Avantage : plus simple. Inconvénient : la phrase sur l'échec reste fausse sous conditionnement.
- (c) Rien. Inconvénient : le contre-lecteur les trouvera.

Recommandation : (a). Confiance 0,7. Défaut sous 48 heures : (a).

**D-3. Première mesure sans dépense.**
Enjeu : cinq espèces, cinq premières mesures. La seule commune à trois d'entre elles ne lit aucun score.
- (a) Tableau de jugeabilité et inventaire des familles. C'est l'étape 0 de la version 6 ; Fable, Opus et Astra y convergent. Avantage : ne lit aucun score et ferme S2, S3 et S5 par l'arithmétique. Inconvénient : ne dit rien de la puissance.
- (b) Ajouter la simulation « le rang contre la somme linéaire seuillée » d'Opus. Avantage : elle complète le monde A de la note de dissonance par la comparaison qui lui manque. Inconvénient : modèle de décalage supposé.
- (c) La ré-analyse d'Argon et de Carbon (variance par famille, inflation de variance) sur les épisodes honnêtes. Inconvénient : elle lit des scores et reste bornée à la liste approuvée.

Recommandation : (a) puis (b). Confiance 0,7. Défaut sous 48 heures : (a) puis (b).

**D-4. Contrôle actif par sélection sur un score de sonde (meilleur de quatre, rééchantillonnage choisi par la sonde).**
Enjeu : deux espèces en font leur proposition de contrôle principale, mais elle heurte l'invariant de N-053, point 5.
- (a) Consigner comme fermé et verser comme matière. Avantage : invariant intact. Inconvénient : on perd l'emploi publié par les auteurs (p. 8).
- (b) Ouvrir un bras d'attaque déclaré qui l'étudie. Avantage : mesure possible. Inconvénient : change un invariant, donc nœud.

Recommandation : (a). Confiance 0,8. Défaut sous 48 heures : (a) ; (b) est un nœud, sans défaut.

**D-5. Ajouter au plan du bras les cellules « consigne de sabotage sans occasion d'agir » et « saboteur assigné sans dommage confirmé », rapportées sans verdict.**
Enjeu : les cinq espèces les demandent pour séparer la lecture d'une consigne de la lecture d'un acte (D0 de Fable, réponse A, l. 73-101), mais elles coûtent des épisodes neufs.
- (a) Les écrire dans la version 7, devis à part. Avantage : D0 devient possible. Inconvénient : dépense.
- (b) Les écrire dans le texte du moniteur seulement. Avantage : pas de retouche de la version 7. Inconvénient : le contraste principal reste sans ce témoin.
- (c) Non.

Recommandation : (a). Confiance 0,6. Défaut sous 48 heures : (a) pour l'écriture. La dépense est un nœud, sans défaut.

## Limites

- Les cellules ne connaissaient ni la note de dissonance, ni la version 6, ni N-053. Elles réinventent en partie le moniteur de dissonance (lecture par rangs, lecteur agent) sans le savoir.
- Aucun calcul des cellules n'a été refait au-delà des huit identités de l'en-tête. Les numéros de ligne renvoient aux fichiers aux empreintes citées.
- La forme fixe du § 5 est mon jugement, à confirmer par le contre-lecteur du texte qui en reprendrait une.
