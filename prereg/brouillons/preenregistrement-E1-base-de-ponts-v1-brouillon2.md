# Préenregistrement — E1′ / duel 1 : le profil « trou à structure commune » prédit-il les ponts futurs au-delà de la distance, de la popularité et de la distance sociale ? — v1 — BROUILLON 2 (non scellé)

**Statut : brouillon 2, non scellé ; contre-lecture 2 par un modèle autre qu'Opus ; décisions de Lazar ; rien n'est collecté avant scellement.**

- Auteur : sous-agent neuf Opus 5.5 (`claude-opus-5-5`), lignée conv-audit, **rédacteur de reprise** : il n'a écrit ni le brouillon 1, ni sa contre-lecture, ni les trois pièces laissées par le premier rédacteur du brouillon 2. Branche locale `canal/conv-audit-n04` (HEAD `021031d6…` à la reprise, `f65feb1a…` à l'écriture des pièces), `origin/main` lu à `8c0f6f4b028dd1acc83850acce082da0e51e01bd`. Date (UTC) : 31 octobre 2026, reprise vers 12:30 (relevé `date -u` 12:33), écriture jusque vers 13:15.
- Commande : consigne de reprise de conv-audit (31 octobre 2026, ≈ 12:45 UTC) : relire les pièces du premier rédacteur, exécuter le script deux fois, adopter ou corriger, écrire ce brouillon. Décisions applicables : R-878 (Bisociation, points 1 et 2 : six garde-fous obligatoires ; base de ponts et Gu-Krenn en parallèle, sur processeur) ; R-729 (accord de principe sur une dépense de moisson, devis à écrire) ; **R-735 (décision de Lazar, 11:51 UTC : la distance sociale entre dans E1′ comme témoin, calculée sur le seul passé de chaque date ; champs d'auteurs au devis)** ; R-734 (antériorité pra2.1298).
- Commit du code d'analyse : aucun. Le code de construction, de prédicteurs et d'analyse sera écrit, testé (gardes de la Liste d'arrêt, cas sain et artefact), commité et son commit inscrit ici **avant** le scellement.
- Nature : expérience décisive sur littérature réelle au sens de R1 ; pas une porte du programme. Elle décide d'une hypothèse de conception du bisociateur (le profil remplace-t-il la distance seule ?), non d'une hypothèse du programme.
- **Ce que l'auteur n'a pas fait** : aucune requête à l'interface d'OpenAlex ; rien lu sous `donnees/` ; aucune moisson, aucun pont, aucune liste de rapprochements datés lus ; aucun `git fetch` ; aucun commit ; aucun `.sha256` écrit ; aucun fichier existant modifié. Lus sur le Web : trois pages de documentation d'OpenAlex (prix, authentification, téléchargement de l'instantané) et la page HTML d'arXiv 2512.16434 (couverture des résumés), sans aucune donnée. Les seuls nombres calculés sont ceux du calcul de puissance sur données **synthétiques** et un calcul déterministe d'inflation de variance sur ses paramètres (§ « Taille de base »).
- **Convention des chiffres.** « SUPPOSÉ » = valeur posée par un rédacteur, sans appui publié vérifié ; « (calcul § k) » = paragraphe k de la sortie `calcul-puissance-E1-base-de-ponts-v1-brouillon2.sortie.txt` ; « (synthèse § x) » = section x de la synthèse v2 du lot bisociation. Toutes les références de la synthèse et la fiche pra2.1298 sont non opposables (R7) : un emprunt y est un emprunt de raisonnement, jamais un chiffre opposable.
- Documents lus (chemin, empreinte complète) :
  - synthèse v2 du lot bisociation : `docs/notes/bisociation-litterature-reelle-v1/collisionneur-bisociation-lot-v1/synthese-bisociation-lot-v2.md` `23c2888ddd924b85a0bbd0009a17f64723399d69ffd17669f56c4fddf7d18a86` (compagnon conforme) ;
  - brouillon 1 : `prereg/brouillons/preenregistrement-E1-base-de-ponts-v1-brouillon1.md` `a22a211f48f7393bedea5ed88cf6699fe7ac97d87d9086d9dfd1c5f8f2989771` ; protocole v1 `…/protocole-construction-base-de-ponts-E1-v1-brouillon1.md` `60fa75472c7304754a3a6ecde590314d12973dfaf8a1c6ce4c90b65ba62f5592` ; script v1 `db04ebbbdfd1fb3f75044e16587e7e580a43ee4572f64df7bf44229c4d3e42ed` et sa sortie `d0af5c92da31b90c3e531673b96bad369616b1c41fdef9051f5361a593418453` ;
  - contre-lecture 1 : `prereg/brouillons/contre-lecture-E1-base-de-ponts-v1-brouillon1.md` `836b8c190e7fea6d469204ff7b4f0f307586591b0a896d1172cca8daae1f95eb` ;
  - pièces du premier rédacteur du brouillon 2 : protocole `…-brouillon2.md` `2ceb34df4e059e97da3ca243c9f31917422c6ca344a1e8b7ce4bdcd4ead3df4f` ; devis `devis-moisson-openalex-E1-v1.md` `36153c96912e8b9cfef314534182e62233a05c3cfd9efe9dfd2726b00103f7da` ; script `calcul-puissance-E1-base-de-ponts-v1-brouillon2.py` `4e87c110d492524d19fc6ccbcf2fb7d1db44cbad4e4d724f47171ab68e590dc8` (identiques à leur état commité en `db0d7389`) ;
  - fiche de l'antériorité pra2.1298 : `docs/sources/captures/asist-2025-pra2-1298-v1/fiche-captures-pra2-1298-v1.md` `a1e9a9da1a06d9b980ab10c035e5f25c9a46b64558826a0e59f8f3402c04c0a7` (compagnon conforme ; captures, pas de PDF : non opposable) ;
  - `registres/decisions.md` de `origin/main` (R-849, R-863, R-878, R-884) `d85a0e243edfbf6388c4da3b3623b1b49ff8ff72af92a7dcc68cd7b41fcc93e1` ; `registres/decisions.md` local (R-729 à R-740) `73177497128ebf35ea803813aeb498d558e9c781dbb76f51366f25e676b5a21a` ;
  - métadonnées de l'instantané d'OpenAlex sur `origin/main` (`docs/notes/gu-krenn-v1/sources-amont-v1/openalex-instantane-metadonnees-v1/`) : README `266047b6956f6dc3af4fb972ed1750345832de67769e43fed3c3f1b4da096fa3`, manifeste JSON Lines `2b3d611b3ec93912b7b655ee139310936048a689c0f3508052a73af03a6c453f`, manifeste Parquet `5abb166c4ae115f8aac56021dbc1eed823e044b48406af146537485fba7f03cc`, notes de version `a6e5083e10f0992f357ae5eeff338c423dfaed106c024160fe9f6db8df247b93` (compagnons conformes) ;
  - gabarit `prereg/gabarit-preregistrement-v1.md` `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e` ; validateur `src/controle_ia/prereg.py` `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306`.

## Pièces compagnes et sort des pièces du premier rédacteur

Le premier rédacteur du brouillon 2 (Opus neuf, consigne reçue vers 11:20 UTC, puis R-735 et R-734, interrompu à 12:09 UTC) a laissé trois pièces non scellées et non relues, sans préenregistrement. L'auteur les a relues en entier.

| Pièce | Sort | Pourquoi | Pièce compagne de ce brouillon (empreinte) |
|---|---|---|---|
| Script `calcul-puissance-E1-base-de-ponts-v1-brouillon2.py` (`4e87c110…`) | **adopté tel quel** | Code relu ligne à ligne : gardes des fenêtres (§ 0), valeur critique fixe éprouvée sur 2 000 répétitions dans quatre configurations du nul (§ 1), puissance et sensibilité dont la distance sociale (§ 2), équivalence sous le nul et à la borne (§ 3), règle de rétrodiction à la lettre de la synthèse et tableau de lecture entier dans onze mondes (§ 4), disponibilité (§ 5), charge par paire (§ 6), kappa (§ 7), convergence comptée (§ 8). Aucune erreur trouvée ; la distance sociale y figure (cinquième prédicteur, effet propre, corrélations éprouvées). | lui-même ; sortie **`calcul-puissance-E1-base-de-ponts-v1-brouillon2.sortie.txt`** `e99582ef4d4e6aac39abbd962720ffbbe59514b40f0ab9704acdc3a63a38b8f9` : deux exécutions `python3 -I` depuis deux dossiers temporaires vides, en parallèle, sorties identiques à l'octet (965 s et 970 s de temps mural, machine partagée) ; numpy 2.5.3, Python 3.13.18 ; dossiers restés vides |
| Protocole `…-brouillon2.md` (`2ceb34df…`) | **corrigé** → `protocole-construction-base-de-ponts-E1-v1-brouillon2b.md` | (1) aucun filtre de couverture des résumés au cadre : plusieurs grands éditeurs des sciences physiques ne déposent pas de résumés (source non opposable), une part inconnue des 500 revues serait inactive à toutes les dates et la disponibilité (CE1-07) serait surestimée ; (2) la définition (b) de DE-9 laisse un lien mécanique possible **en faveur** de H-E1 (groupe nouveau contenant un objet déjà partagé) sans moyen de le mesurer (R4) : marque `LS_partage` ajoutée ; (3) la distance sociale manquait aux listes de C5 bis et C12.2 ; (4) trois imprécisions (strates, fenêtre vide, « après E₁ »). Tout le reste est repris mot pour mot. | `b6b7c38f29df6a55a70d446b6ee8ff7b589a5e407035cbcb35f7e7f62ba289b6` |
| Devis `devis-moisson-openalex-E1-v1.md` (`36153c96…`) | **corrigé** → `devis-moisson-openalex-E1-v2.md` | prix relus et concordants ; mais (1) le cadre du protocole 2b coûte une requête de plus par revue candidate ; (2) la charge de lecture doit couvrir les deux tailles de DE-4 (500 et 750 ponts) ; (3) seuil de rendement imprécis. Plafond inchangé (35 USD). | `f24872741836201a7b25262a5c1700e4a544d2bd3359a3c8d35a05578506a0b2` |

## Ce qui change par rapport au brouillon 1

| Point | Brouillon 1 | Brouillon 2 | Constat |
|---|---|---|---|
| Témoins | distance, popularité, attachement préférentiel | **+ distance sociale SOC** (réseau de cosignature, critère de pra2.1298), calculée sur [t − 5, t), non amputée ; hypothèse rivale HR-5 | R-735 |
| Fenêtre rétrodite | [t − 7, t − 4), recouvre d'un an le calcul du profil à w_s = 5 | **[t − 8, t − 5)** (décalage g = 5 = la plus longue fenêtre de calcul) ; **toutes** les fenêtres de calcul (profil, témoins, covariables) ⊂ [t − 5, t) ; essai § 0 du calcul ; gardes G-C18 et G-A8 | CE1-01 (bloquant) |
| Règle de rétrodiction | règle (c) sur β₂ (écart à la synthèse) | **lettre de la synthèse**, « score » lu comme l'aire du profil seul : suspension si aire⁻(Π) ≥ aire⁺(Π) − 0,03 ; règle (c) rapportée ; écart retiré | CE1-02 |
| Niveau de la règle principale | 1,645, fausses alarmes 0,060 à 0,080 ; correction par permutation | **valeur critique fixe 1,96** : fausses alarmes 0,027 à 0,043 (2 000 répétitions, quatre configurations du nul) ; permutation abandonnée | CE1-05 |
| Ordre du tableau de lecture | suspension avant équivalence, en estimations ponctuelles | équivalence, puis signe inverse, puis suspension (seulement si la borne basse > 0), puis « non réfutée » ; caractéristiques opératoires du tableau entier simulées | CE1-08 |
| Bande d'équivalence et prédiction | ± log 1,25 ; prédiction 1,2 à 2,0 (en partie dans la bande) | **± log 1,5** recommandée (seuil d'utilité) ; prédiction ≥ 1,5 | CE1-08 |
| Taille | 500 ponts (200 + 200 + 100), puissance 0,98 annoncée | **750 ponts (300 + 300 + 150)** recommandés (DE-4) ; puissance réelle déclarée, 0,92 au cas de base et 0,67 à 0,83 sous les lignes défavorables | CE1-07, CE1-15 |
| Revues | 300 | 500 (250 par moitié) + deux paliers de 100, sciences physiques (DE-10), couverture des résumés au cadre | CE1-04, CE1-07 |
| Lexique de structure | retiré de l'étiquette | trois définitions (DE-9) : (a) retiré ; (b) autorisé et marqué ; (b′) autorisé si ses objets sont nouveaux pour j | CE1-03 |
| Charge de lecture | 2 200 à 5 000 lectures par portion | modèle par paire : 19 132 à 93 268 lectures pour 500 ponts, ≈ 28 700 à 139 900 pour 750 ; plafond S17 | CE1-06 |
| Fuites temporelles | inverse de fréquence, marges, N et n_o sans fenêtre | toutes les fenêtres écrites ; G-A1 étendue | CE1-13 |
| Kappa | 100 paquets | 200 paquets ; intervalle rapporté | CE1-16 |
| Moisson | « allocation gratuite ou devis » | devis chiffré, plafond 35 USD (décision DE-12) | R-729 |

## Résumé en dix lignes pour Lazar

1. **Question** : sur la littérature réelle, une paire de revues dont la communication est faible et la structure commune forte reçoit-elle plus souvent, dans les trois ans, un pont réel daté que ne le prédisent sa distance, sa popularité, l'attachement préférentiel **et sa distance sociale** (R-735) ? La règle décisive est un **incrément** (le profil ajoute-t-il aux témoins ?) ; le duel « mieux que la distance seule » est rapporté.
2. **Pont** : une œuvre de la revue j qui reprend une méthode, un objet mathématique, un modèle ou un résultat propre à la revue i, détectée par un filtre de termes **sans aucune citation**, validée « oui » par **deux lecteurs isolés** (kappa ≥ 0,60 sur 200 paquets).
3. **Profil** sur le seul passé de chaque date ([t − w_s, t), w_s = 3 ou 5), sur un corpus **amputé** des œuvres qui parlent déjà la langue de l'autre revue ; témoins sur [t − 5, t), non amputés.
4. **Règle principale** : coefficient β₂ du profil, ajusté sur les quatre témoins et la couverture des résumés ; borne basse β̂₂ − 1,96 × erreur type > 0 (valeur critique fixe : fausses alarmes 0,027 à 0,043).
5. **Rétrodiction** (lettre de la synthèse) : si l'aire du profil seul sur les ponts **antérieurs** à toute fenêtre de calcul ([t − 8, t − 5)) atteint l'aire prospective − 0,03 : suspension. Bloquant de la contre-lecture levé (fenêtres disjointes partout, essai vérifié).
6. **Moitiés disjointes** : E₁ (revues 𝒜, 2009–2013) étalonne et choisit une variante parmi quatre ; E₂ (revues ℬ, 2017–2021) décide seule.
7. **Taille recommandée** : 300 ponts en E₂ prospective, 300 en E₂ rétrodite, 150 en E₁. Sous le nul, « réfuté » 0,87 ; sous un effet de rapport de cotes 1,5 qui anticipe vraiment, « non réfutée » 0,94 ; sous une association statique, « non réfutée » à tort 0,10 (calcul § 4) ; puissance seule 0,92, mais 0,67 si les revues sont très hétérogènes.
8. **Construction** par une session distincte, aveugle au profil (protocole 2b) : 500 revues de sciences physiques + deux paliers, plafond de 10 candidats lus par paire.
9. **Coût** : moisson ≈ 6 USD attendus, **plafond 35 USD** (devis v2, nœud) ; lecteurs : ≈ 610 à 2 840 appels de sous-agent (sans dépense en dollars si DE-3 (a)).
10. **Pour geler** : seuils S1 à S19 et décisions DE-1 à DE-12 ; contre-lecture 2 par un modèle autre qu'Opus.

## Décisions à soumettre à Lazar (DE-1 à DE-12)

Format : décision ; enjeu ; options (avantage, inconvénient) ; recommandation et confiance. **Aucune ne prend de défaut à 48 heures** : elles se gèlent avec le préenregistrement (R1), ou sont des nœuds de dépense. Confiance ≤ 0,6 : « option : demander au collisionneur ».

- **DE-1 — Qu'est-ce qu'une niche ?** État : À REMPLIR.
  - Décision : l'entité dont les paires sont étudiées.
  - Enjeu : la partition doit être extérieure au graphe des ponts et datée (synthèse § A : « une partition calculée sans la couche des équations » ; le modèle de blocs « regroupe les adversaires qui se citent ») ; une partition qui lit l'avenir ou le canal fausse GF1, GF3 et GF5.
  - (a) **Revues d'OpenAlex** (500 + deux paliers de 100). Avantage : entité datée et extérieure (une œuvre appartient à sa revue dès sa parution) ; une seule moisson. Inconvénient : une revue n'est pas une communauté ; revues pluridisciplinaires à exclure (protocole C2.1).
  - (b) **Catégories d'arXiv** (catégorie principale choisie au dépôt). Avantage : choisie par l'auteur à la date ; « même objet mathématique » y a un sens. Inconvénient : couverture limitée à arXiv ; accès refusé par le mandataire dans un environnement (R-625) ; ≈ 150 catégories grossières.
  - (c) **Sujets (« topics ») d'OpenAlex**. Avantage : fins, prêts. Inconvénient : SUPPOSÉ à vérifier — créés en 2024 par regroupement d'un graphe de citations et attribués par un classeur qui lit les références : la partition connaîtrait l'avenir des dates et toucherait le canal. (Des communautés calculées à chaque date sur le passé sont écartées d'emblée : elles minimisent le canal entre elles par construction.)
  - **Recommandation : (a), confiance 0,55** — option : demander au collisionneur.
- **DE-2 — Forme de la règle principale.** État : À REMPLIR.
  - Décision : ce que « mieux que » veut dire pour la décision.
  - Enjeu : le bisociateur a besoin de savoir si le profil ajoute quelque chose aux témoins ; la lettre de la question est un duel.
  - (a) **Incrément** : β₂ > 0 à distance, popularité, attachement préférentiel et distance sociale contrôlés (T3-A ; R-735). Avantage : dit ce qui sert au bisociateur. Inconvénient : ne dit pas si le profil seul bat la distance seule.
  - (b) **Duel** : aire du profil seul > max(aire de chaque témoin seul), borne basse > 0. Avantage : lettre de la question. Inconvénient : un profil corrélé à la distance peut gagner le duel sans rien ajouter.
  - (c) Les deux, conjonctifs. Avantage : les deux sens à la fois. Inconvénient : puissance plus basse.
  - **Recommandation : (a) décisive, (b) rapportée avec signe prédit ; confiance 0,6** — option : demander au collisionneur.
- **DE-3 — Qui lit ?** État : À REMPLIR.
  - Décision : les deux lecteurs isolés de l'étiquette et le troisième lecteur de l'audit.
  - Enjeu : la validité de l'étiquette (C place le goulot dans la validité de l'observable, synthèse verdict 3) et la charge : ≈ 610 à 2 840 appels de sous-agent pour 750 ponts, ≈ 420 à 1 910 pour 500 (devis v2, d'après le calcul § 6).
  - (a) **Deux sous-agents de session de familles différentes** (Sonnet 5.5 et Fable 5.1), appels neufs et isolés, plus un audit de 60 lectures par un troisième lecteur. Avantage : sans dépense en dollars, rapide. Inconvénient : deux familles d'un même fournisseur ; Sonnet 5.5 est aussi la famille du contre-lecteur 1, Fable 5.1 celle de la synthèse de la question 6 (CE1-19) ; mémoire possible des œuvres célèbres ; si les appels touchent un quota ou un coût, c'est une dépense (nœud).
  - (b) **Modèles payants de deux fournisseurs**. Avantage : indépendance de lignée. Inconvénient : dépense ≈ 75 à 347 USD pour 750 ponts (prix SUPPOSÉS, devis v2) ; devis séparé et GO.
  - (c) **Lecteurs humains**. Avantage : référence. Inconvénient : contact externe (nœud) ; des dizaines de milliers de lectures.
  - **Recommandation : (a), confiance 0,6** — option : demander au collisionneur.
- **DE-4 — Taille de la base et bande d'équivalence (fixe S2, S3, S6, S17).** État : À REMPLIR.
  - Décision : combien de ponts validés par portion, et quel est le plus petit effet utile.
  - Enjeu : la synthèse (T3-D) dit que seule l'équivalence « tue une décision de conception » ; au brouillon 1, l'équivalence n'était presque jamais démontrable (CE1-08) et la puissance de 0,98 n'était qu'un plafond (CE1-15). Avec la valeur critique 1,96 et la distance sociale, la bande ± log 1,25 n'est jamais atteinte (probabilité 0,007 à M = 200, 0,081 à M = 300, calcul § 3).
  - (a) **M₂ = 300, M₁ = 150 (750 ponts), bande ± log 1,5, M_min = 150, plafond de lectures 90 000.** Avantage : tableau entier symétrique (calcul § 4, M = 300) : sous le nul, « réfuté » 0,873 ; sous un effet de rapport de cotes 1,5 qui anticipe, « non réfutée » 0,938 ; sous une association statique, « non réfutée » à tort 0,098 ; puissance seule 0,917, 0,670 à 0,828 sous les lignes défavorables (calcul § 2). Inconvénient : ≈ 28 700 à 139 900 lectures (+ 50 %) ; à un taux de base de 0,25 %, 250 revues par moitié n'offrent que 233 ponts par portion : palier d'extension probable (300 revues : 336) ; un effet de rapport de cotes 1,25 est classé « réfuté » 0,415 fois.
  - (b) **M₂ = 200, M₁ = 100 (500 ponts), bande ± log 1,5, M_min = 100, plafond 60 000.** Avantage : charge 19 132 à 93 268 lectures ; disponibilité assurée à 250 revues dès 0,25 % (calcul § 5 : 0,997). Inconvénient : « réfuté » sous le nul 0,738, « non réfutée » sous l'effet 1,5 0,797, faux « non réfutée » statique 0,168 ; puissance 0,552 à 0,645 sous les lignes défavorables.
  - (c) **M₂ = 300, bande ± log 1,33.** Avantage : un effet de 1,25 n'est classé « réfuté » que 0,110 fois. Inconvénient : sous le nul, « réfuté » seulement 0,393 : le résultat le plus probable si H-E1 est fausse redevient « non concluant » (asymétrie que CE1-08 reprochait).
  - **Recommandation : (a), confiance 0,55** — option : demander au collisionneur. Le seuil d'utilité « rapport de cotes 1,5 par écart type » est un jugement de l'auteur (un incrément plus petit au-delà de quatre témoins ajoute peu à un classement de paires) : SUPPOSÉ, à confirmer par Lazar.
- **DE-5 — Rôle de la moitié E₁.** État : À REMPLIR.
  - Décision : ce que fait E₁ avant la décision sur E₂.
  - Enjeu : l'instrument est jeune ; une réplication conjonctive coûte le double de lectures.
  - (a) **Étalonnage des lecteurs et choix d'une variante parmi quatre, scellées, par une règle scellée (S16)** ; E₂ décide seule. Avantage : l'instrument est réglé sur des données disjointes. Inconvénient : E₁ n'est pas une réplication.
  - (b) **Variante unique gelée, E₁ = réplication conjonctive.** Avantage : deux décisions concordantes exigées. Inconvénient : M₂ ponts dans chaque moitié (≈ deux fois les lectures), puissance conjointe plus basse.
  - **Recommandation : (a), confiance 0,6** — option : demander au collisionneur.
- **DE-6 — Lecture du mot « score » dans la règle de rétrodiction de la synthèse.** État : À REMPLIR.
  - Décision : comment lire « si la rétrodiction inversée atteint le score prospectif − δ₀, suspension » (synthèse § (iii) 1, T3-B, δ₀ = 0,03 ; « les seuils sont illustratifs selon leurs auteurs »).
  - Enjeu : c'est la seule protection contre l'association statique (HR-3) ; une lecture vide la rend décorative, une lecture trop sévère suspend les vrais effets. Au brouillon 1, la règle de la synthèse était déclarée « inutilisable » sur la seule lecture « gain d'aire » ; la contre-lecture (CE1-02) a montré qu'elle fonctionne sous la lecture « aire du profil seul ». Le calcul § 4 (400 répétitions par monde) le confirme.
  - (a) **Lettre, « score » = aire du profil seul** : suspension si aire⁻(Π) ≥ aire⁺(Π) − 0,03. Avantage : aucun écart à la synthèse ; suspension à tort sous anticipation de rapport de cotes 1,5 : 0,005 (M = 200), 0,003 (M = 300) ; suspension d'une association statique : 0,825 et 0,902. Inconvénient : non ajustée sur les témoins ; faible contre une association statique **atténuée** (atténuation 0,6 : suspension 0,345 et 0,310 seulement) ; suspend à tort 0,182 et 0,120 un effet de 1,25 qui anticipe.
  - (a′) **Lettre, « score » = gain d'aire** du modèle complet sur le modèle sans profil. Avantage : ajustée. Inconvénient : vide à ces tailles d'effet : suspension 1,000 dans les trois mondes simulés, nul, anticipation et statique (calcul § 4, M = 200).
  - (c) **Règle sur β₂** : β̂₂⁻ ≥ β̂₂⁺ / 2 et β̂₂⁺ > 0. Avantage : ajustée ; meilleure contre l'atténuation (0,568 et 0,578 à 0,6). Inconvénient : écart à la lettre ; « la moitié » n'est justifiée par rien ; suspend à tort 0,085 (M = 200) un effet de 1,5 qui anticipe.
  - **Recommandation : (a) décisive (S5), (c) rapportée en lecture croisée (réserve écrite si elle diverge) ; confiance 0,6** — option : demander au collisionneur. Aucune lecture ne domine l'autre dans tous les mondes : la lettre l'emporte faute de démonstration contraire.
- **DE-7 — La structure commune compte-t-elle les jeux de données ?** État : À REMPLIR.
  - Décision : le contenu du lexique L_S.
  - Enjeu : R-638 nomme « objet mathématique, méthode, jeu de données » ; une structure quasi universelle gonfle S partout (CA1-04 de la contre-lecture de l'annexe du bras méta).
  - (a) **Objets mathématiques et méthodes seulement, pondérés par la rareté.** Avantage : la pondération retire d'elle-même les structures quasi universelles ; L_S constructible sans données. Inconvénient : s'écarte de la lettre de R-638.
  - (b) **Les trois types.** Avantage : lettre de R-638. Inconvénient : liste fermée et datée de jeux de données à construire sans données ; risque de structures quasi universelles.
  - **Recommandation : (a), confiance 0,55** — option : demander au collisionneur.
- **DE-8 — Où vit la session de construction ?** État : À REMPLIR.
  - Décision : quelle session applique le protocole, moisson comprise.
  - Enjeu : elle doit porter la clé d'OpenAlex (R-849) et n'avoir jamais vu de prédicteur (G-C15) ; session-depot est inactive depuis ≈ 08:50 UTC (R-740).
  - (a) **Une instance neuve de session-depot.** Avantage : la clé y est ; code de la moisson de R-863 réutilisable. Inconvénient : dépend du retour de session-depot.
  - (b) **Une instance neuve de conv-audit.** Avantage : disponible. Inconvénient : présence de la clé à vérifier par son nom ; même lignée que l'auteur.
  - **Recommandation : (a), confiance 0,65.**
- **DE-9 — Disjonction entre l'étiquette et la structure commune (CE1-03).** État : À REMPLIR.
  - Décision : comment empêcher l'étiquette de recompter S sans lui interdire les méthodes et objets.
  - Enjeu : au brouillon 1, l'exclusion de L_S écartait les ponts typiques de H-E1 (biais contre H-E1, en faveur de la distance) tout en demandant aux lecteurs si l'œuvre reprend une méthode. Mais autoriser L_S sans précaution ouvre un lien inverse : un groupe nouveau pour j qui contient un objet **déjà partagé** par i et j (« wavelet » partagé, « wavelet shrinkage » nouveau) est plus fréquent dans les paires à S élevé (continuité de vocabulaire, en faveur de H-E1).
  - (a) **Disjonction par lexique** : tout groupe qui touche L_S est retiré du filtre (brouillon 1). Avantage : aucune trace de L_S dans l'étiquette. Inconvénient : biais contre H-E1 ; question et filtre désalignés.
  - (b) **Disjonction par période au niveau du groupe** : L_S autorisé ; le groupe déclencheur doit être absent de j sur [a − 6, a) ; marques `touche_LS` et `LS_partage` (protocole 2b). Avantage : question et filtre alignés ; les ponts de méthode et d'objet comptent. Inconvénient : lien mécanique positif possible par les objets partagés (mesuré par la variante (b′)).
  - (b′) **Disjonction par période au niveau de l'objet** : comme (b), mais un candidat dont un objet de L_S figure déjà dans j sur [a − 6, a) ne compte pas (marque `LS_partage`) ; pour la portion prospective, l'objet transféré a alors f_j = 0 sur la fenêtre de S. Avantage : ferme le lien positif. Inconvénient : lien négatif symétrique possible (les paires à S élevé ont plus de groupes à objet partagé, donc moins de candidats comptés) ; lecture un peu plus longue (un « oui-oui » `LS_partage` n'arrête pas la paire).
  - (Disjonction par corpus — S sur résumés, étiquette sur les sections de méthodes du texte intégral — écartée : texte intégral absent de la moisson.)
  - **Recommandation : (b) principale, (b′) et (a) rapportées en variantes, lecture croisée écrite ; confiance 0,5** — option : demander au collisionneur.
- **DE-10 — Périmètre disciplinaire (CE1-04).** État : À REMPLIR.
  - Décision : les domaines d'où sont tirées les revues.
  - Enjeu : S est sommé sur des objets mathématiques et des méthodes ; hors des domaines où ils ont un sens, S serait nul pour la plupart des paires et la statistique reposerait sur une sous-population implicite.
  - (a) **Sciences physiques seulement** (domaine « Physical Sciences » d'OpenAlex : mathématiques, physique, informatique, chimie, ingénierie, sciences de la Terre…). Avantage : L_S y a un sens partout. Inconvénient : généralisation limitée à ce domaine.
  - (b) **Quatre domaines, un L_S par domaine** (méthodes statistiques et expérimentales comprises). Avantage : portée large. Inconvénient : quatre listes fermées à construire sans données, comparabilité de S entre domaines douteuse.
  - (c) **Quatre domaines, un seul L_S, garde sur la part de S nul (S18).** Avantage : simple. Inconvénient : garde probablement déclenchée, base perdue.
  - **Recommandation : (a), confiance 0,6** — option : demander au collisionneur.
- **DE-11 — Règle de niveau de la règle principale (CE1-05).** État : À REMPLIR.
  - Décision : la valeur critique de la borne basse de β₂.
  - Enjeu : à 1,645, la règle sonne à tort 0,052 à 0,071 fois (calcul § 1) ; l'étalonnage par permutation proposé au brouillon 1 détruit la dépendance de niche et la corrélation avec la distance (CE1-05).
  - (a) **Valeur critique fixe 1,96**, écrite avant tout calcul (script du premier rédacteur). Avantage : fausses alarmes 0,027 à 0,043 dans les quatre configurations du nul et les trois tailles (2 000 répétitions chacune) ; simple. Inconvénient : coûte quelques points de puissance ; reste un peu au-dessus du nominal bilatéral (P(|z| > 1,96) jusqu'à 0,088 à σ_U = 1,2).
  - (b) **1,645 sans correction.** Avantage : puissance maximale. Inconvénient : niveau réel ≈ 0,06 à 0,07, anticonservateur en faveur de H-E1 (R4).
  - (c) **Bootstrap par niches (« sauvage » par niche) comme règle principale.** Avantage : ne dépend pas de la formule d'erreur type. Inconvénient : non éprouvé par le calcul ; plus lourd.
  - **Recommandation : (a), confiance 0,75.**
- **DE-12 — Voie et plafond de la moisson (nœud de dépense).** État : À REMPLIR.
  - Décision, enjeu, options et recommandation : `devis-moisson-openalex-E1-v2.md` (`f2487274…`). En bref : (A1) interface avec clé et solde prépayé, ≈ 5,9 USD attendus, plafond 35 USD ; (A0) allocation gratuite seule, 5 à 13 jours ; (B) instantané S3, 675 Go, machine louée probable. **Recommandation : A1, plafond 35 USD, confiance 0,65.** Aucune moisson avant le scellement de ce texte et la ligne de GO.

## Taille de base et puissance (calcul sur données synthétiques)

Calcul : `calcul-puissance-E1-base-de-ponts-v1-brouillon2.py` (`4e87c110…`, écrit par le premier rédacteur, adopté tel quel) ; sortie `….sortie.txt` (`e99582ef…`), rejouée deux fois à l'octet près. Modèle génératif en tête du script : 250 revues par moitié, trois dates, cinq prédicteurs standardisés (D, P, PA, SOC, Π) à composantes de revue, de paire et de date ; corrélations Π–D −0,5, Π–SOC +0,3, D–SOC +0,4 ; effets propres des témoins −0,5, +0,4, +0,3, −0,3 ; propension de revue σ_U = 0,4 ; taux de base 1 % par paire et par date ; plan cas-témoins à K = 5 témoins par cas, même date ; erreur type robuste à deux voies par revue. **Tout est SUPPOSÉ** : la structure du calcul est opposable, ses entrées non.

**§ 0 — fenêtres (bloquant CE1-01).** Configuration principale (w_s ∈ {3, 5}, g = 5, h = 3, w_lab = 4, h_nov = 6, moisson [1995, 2024)) acceptée ; quatre artefacts refusés : g = 4 avec w_s = 5 (le brouillon 1 : calcul [2004, 2009) contre événement rétrodit [2002, 2005)), w_s = 6, une date de E₂ (2015) dont l'événement recouvre E₁, une date de E₁ (2007) dont les fenêtres sortent de la moisson. Le script s'arrête en échec si une garde ne refuse pas son artefact.

**§ 1 — fausses alarmes de la règle principale (2 000 répétitions par case ; erreur de Monte-Carlo ± 0,005).**

| Configuration du nul | valeur critique | M = 100 | M = 200 | M = 300 |
|---|---|---|---|---|
| base | 1,645 | 0,056 | 0,057 | 0,052 |
| base | **1,96** | **0,034** | **0,031** | **0,027** |
| revues hétérogènes (σ_U = 1,2) | 1,96 | 0,043 | 0,034 | 0,040 |
| Π proche de la distance (corrélation −0,8) | 1,96 | 0,031 | 0,039 | 0,036 |
| Π proche de la distance sociale (+0,6) | 1,96 | 0,030 | 0,031 | 0,034 |

**§ 2 — puissance (borne basse > 0 à 1,96 ; 400 répétitions ; erreur ≤ 0,025).**

| Rapport de cotes par écart type de Π \ M | 100 | 150 | 200 | 300 | 400 |
|---|---|---|---|---|---|
| 1,25 | 0,235 | 0,310 | 0,362 | 0,490 | 0,635 |
| 1,33 | 0,333 | 0,445 | 0,573 | 0,705 | 0,795 |
| **1,50** | 0,555 | 0,705 | **0,823** | **0,917** | 0,963 |
| 2,00 | 0,930 | 0,993 | 1,000 | 1,000 | 1,000 |
| 1,50, revues hétérogènes (σ_U = 1,2) | 0,422 | 0,555 | 0,595 | 0,670 | 0,733 |
| 1,50, Π–D à −0,8 | 0,355 | 0,497 | 0,552 | 0,745 | 0,807 |
| 1,50, Π–SOC à +0,6 | 0,443 | 0,517 | 0,645 | 0,807 | 0,870 |

- 20 % de faux ponts (rapport de cotes 1,5) : M = 200, 0,625 (non différentiels) et 0,627 (liés à la distance) ; M = 300, 0,828 et 0,792.
- **Distance sociale.** Sans SOC dans le modèle ajusté, la puissance s'effondre (rapport de cotes 1,5, M = 300 : 0,672 au lieu de 0,917 ; 1,25 : 0,045 au lieu de 0,490) : dans ce modèle génératif, SOC a un effet propre négatif et Π lui est corrélé positivement, l'omettre biaise β₂ vers le bas. Avec SOC, la baisse par rapport au brouillon 1 (0,98 à M = 200, valeur critique 1,645) s'explique pour l'essentiel par l'inflation de variance : la part de variance de Π expliquée par les témoins passe de 0,265 (D, P, PA) à 0,589 (avec SOC), l'erreur type est multipliée par 1,337 (calcul déterministe sur les corrélations effectives du modèle, R × (√(a_k a_l) + √(b_k b_l) + √(c_k c_l)), sans graine ; parts de variance a, b, c du script).
- **La puissance de 0,92 est un plafond** : elle tombe à 0,67 à 0,83 sous les lignes défavorables plausibles (CE1-15) ; sous des revues très hétérogènes, elle plafonne vers 0,7 quel que soit M (le nombre de revues, non de ponts, limite).

**§ 3 — équivalence (intervalle β̂₂ ± 1,96 × erreur type dans la bande).**

| Bande \ M (probabilité sous le nul ; 2 000 répétitions) | 100 | 200 | 300 |
|---|---|---|---|
| ± log 1,25 | 0,000 | 0,007 | 0,081 |
| ± log 1,33 | 0,004 | 0,152 | 0,431 |
| **± log 1,5** | 0,175 | **0,690** | **0,897** |

Fausse alarme de « réfuté » à la borne de la bande : 0,000 à 0,035 (400 répétitions). Avec ± log 1,5, un effet de 1,25 (sous la bande) est jugé équivalent 0,265 (M = 200) et 0,388 (M = 300) fois.

**§ 4 — rétrodiction : probabilité de suspension (inconditionnelle), 400 répétitions par monde.**

| Monde (rapport de cotes prospectif ; rétrodit) | règle (a), M = 200 | (a), M = 300 | (c), M = 200 | (c), M = 300 |
|---|---|---|---|---|
| anticipation 1,25 ; 1 | 0,182 | 0,120 | 0,210 | 0,177 |
| anticipation 1,5 ; 1 | **0,005** | **0,003** | 0,085 | 0,037 |
| anticipation 2,0 ; 1 | 0,000 | 0,000 | 0,007 | 0,003 |
| moitié 1,5 ; 1,5^0,5 | 0,225 | 0,220 | 0,468 | 0,505 |
| statique atténuée 0,6 | 0,345 | 0,310 | 0,568 | 0,578 |
| statique atténuée 0,8 | 0,675 | 0,660 | 0,838 | 0,845 |
| statique 1,5 ; 1,5 | **0,825** | **0,902** | 0,900 | 0,950 |
| statique, témoins du passé × 0,7 | 0,642 | 0,720 | 0,907 | 0,948 |
| anticipation, témoins du passé × 1,3 | 0,035 | 0,005 | 0,083 | 0,058 |

Règle (a′) (gain d'aire) : 1,000 dans les mondes nul, anticipation 1,5 et statique (M = 200) : vide. Aires du profil seul (M = 200) : 0,568 (nul) ; 0,673 prospective contre 0,568 rétrodite (anticipation 1,5) ; 0,675 contre 0,674 (statique).

**Tableau de lecture entier (lignes 2 à 6 ; lignes 0 et 1 non simulées), bande ± log 1,5, règle (a).**

| Monde | M | réfuté | réfuté, signe inverse | suspendu | non réfutée | non concluant |
|---|---|---|---|---|---|---|
| nul | 300 | **0,873** | 0,050 | 0,013 | 0,010 | 0,055 |
| barrière (1/1,5 partout) | 300 | 0,022 | **0,943** | 0,000 | 0,000 | 0,035 |
| anticipation 1,25 | 300 | 0,415 | 0,000 | 0,020 | 0,425 | 0,140 |
| anticipation 1,5 | 300 | 0,025 | 0,000 | 0,003 | **0,938** | 0,035 |
| moitié | 300 | 0,028 | 0,000 | 0,203 | 0,735 | 0,035 |
| statique atténuée 0,6 | 300 | 0,028 | 0,000 | 0,282 | 0,667 | 0,022 |
| statique | 300 | 0,033 | 0,000 | **0,843** | 0,098 | 0,028 |
| statique, témoins du passé × 0,7 | 300 | 0,033 | 0,000 | 0,652 | 0,273 | 0,043 |
| nul | 200 | 0,738 | 0,013 | 0,010 | 0,013 | 0,228 |
| anticipation 1,25 | 200 | 0,268 | 0,000 | 0,028 | 0,360 | 0,345 |
| anticipation 1,5 | 200 | 0,037 | 0,000 | 0,003 | 0,797 | 0,163 |
| statique | 200 | 0,022 | 0,000 | 0,680 | 0,168 | 0,130 |

Revues hétérogènes (σ_U = 1,2, bande ± log 1,33, 300 répétitions, M = 300) : « non réfutée » 0,657 sous anticipation 1,5 ; 0,073 à tort sous statique ; « réfuté » 0,103 sous le nul. Le « signe inverse » à tort sous le nul vaut 0,050 à M = 300 (400 répétitions ; ≈ 0,03 attendu d'après le § 1) : bruit de Monte-Carlo probable, à surveiller.

**§ 5 — disponibilité.** Ponts attendus par portion (paires × 3 dates × taux de base) : 250 revues par moitié → 233 (0,25 %), 467 (0,5 %), 934 (1 %) ; 300 revues → 336, 673, 1 346 ; 350 revues → 458, 916, 1 832. Pour un quota de 200, 250 revues suffisent dès 0,25 % (P(M ≥ 200) = 0,997) ; pour 300, il faut 0,5 % à 250 revues, ou le palier 2 à 0,25 %. Ces comptes supposent toutes les revues actives : la condition de couverture au cadre (protocole 2b, C1.4) sert à ce que ce soit à peu près vrai.

**§ 6 — charge de lecture** (modèle par paire, SUPPOSÉ, plafond 10) : 19 132 à 93 268 lectures pour 500 ponts (382 à 1 865 appels hors lectures fixes) ; ≈ 28 700 à 139 900 pour 750, par proportionnalité. Les mondes où une paire signalée porte une vraie reprise une fois sur dix ou plus tiennent sous le plafond S17 ; ceux à 3 % non — et, dans le modèle, la majorité de leurs ponts validés seraient de faux « oui-oui ».

**§ 7 — kappa** (prévalence 0,3) : écart type du kappa estimé 0,056 à 0,068 sur 200 paquets (0,080 à 0,094 sur 100) ; un accord vrai de 0,65 échoue le seuil 0,60 une fois sur cinq (0,201), un accord de 0,70 une fois sur 23 (0,043).

**§ 8** : 82 392 ajustements, aucune non-convergence, aucun repli de l'erreur type.

**Conclusion.** (1) Le bloquant est levé : fenêtres disjointes pour toutes les variantes, essai vérifié. (2) La règle de rétrodiction de la synthèse, lue sur l'aire du profil seul, fonctionne (0,003 à 0,005 de suspension à tort, 0,83 à 0,90 de suspension d'une association statique) : écart DE-6 retiré. (3) La valeur critique 1,96 tient le niveau (≤ 0,043). (4) **Recommandation (S2, DE-4 (a)) : 300 ponts validés en E₂ prospective, 300 en E₂ rétrodite, 150 en E₁, soit 750**, bande ± log 1,5 ; puissance réelle déclarée : 0,92 au cas de base, 0,67 à 0,83 sous les lignes défavorables ; « réfuté » sous le nul 0,87. (5) Deux faiblesses écrites : une association statique atténuée (0,6) passe pour une anticipation deux fois sur trois (règles (a) comme (c), à des degrés divers) ; la qualité de l'étiquette (part de faux ponts) gouverne tout et n'est mesurée que par l'audit.

## Six garde-fous de R-878 (obligatoires dans tout préenregistrement sur littérature réelle)

R-878, point 1 (Bisociation), rend obligatoire le gabarit de la synthèse v2 (§ (iv), décision 1 : « sinon, le résultat positif est acquis par construction »).

| GF | Garde-fou | Ce qu'il ferme ici | Application concrète | Où |
|---|---|---|---|---|
| GF1 | **Étiquette de pont indépendante du canal** | La circularité relevée par D (T2-D) et l'artefact A0 (un trou lu dans le flux de citations prédit mécaniquement une hausse du flux). | Le pont n'utilise **aucune citation** : filtre de termes caractéristiques de i nouveaux dans j sur six ans, puis deux lecteurs qui ne voient ni citation, ni score, ni année, ni auteur. Disjonction avec la structure : DE-9 ((b) principale ; (b′) et (a) en variantes ; marques `touche_LS`, `LS_partage`). Forme retenue : la « reprise traversante validée » de D ; variante tierce niche rapportée. | Métrique ; protocole C5–C9 |
| GF2 | **Rétrodiction inversée** | A0 et toute association statique entre profil et ponts. | Même profil, calculé en t sur [t − w_s, t), confronté aux ponts de [t − 8, t − 5), **antérieure à toutes les fenêtres de calcul** (profil, témoins, covariables ⊂ [t − 5, t)), pour les deux longueurs w_s ; règle de la synthèse (S5) ; essai § 0 ; gardes G-C18 et G-A8. | Métrique ; S5, S8 bis ; Critères, ligne 4 |
| GF3 | **Graphe amputé des ponts** | L'empreinte des ponts passés sur le score et la circularité de la partition. | (a) Niches = revues, extérieures au graphe des ponts (DE-1). (b) S et C sur des corpus amputés des œuvres de i (resp. j) qui contiennent un terme caractéristique de j (resp. i) aux deux dates t et t − 8 (protocole C5 bis) : l'empreinte des ponts rétrodits est retirée aussi. (c) Témoins non amputés (les plus durs) ; variante non amputée rapportée. | Métrique ; Plan § 4 |
| GF4 | **Bras « popularité seule »** | Un profil qui ne fait que retrouver les grosses revues. | P et PA dans le modèle et en classeurs seuls ; **SOC** (R-735) en plus. | Métrique ; Critères |
| GF5 | **Jeux disjoints par niche et par période** | Une association propre à une revue ou à une période prise pour une prédiction. | Revues coupées au hasard en 𝒜 et ℬ ; E₁ = paires de 𝒜, dates 2009, 2011, 2013 (événements 2009–2015) ; E₂ = paires de ℬ, dates 2017, 2019, 2021 (événements prospectifs 2017–2023) ; aucune revue, paire ni année d'événement prospectif commune ; les événements rétrodits de E₂ (2009–2015) partagent des années civiles avec E₁, **sur des revues disjointes** (écrit). Choix de variante sur E₁ seule ; décision sur E₂ seule. | Plan § 2, § 6 |
| GF6 | **Calcul de puissance préalable** | Une règle impossible à tenir ou à manquer. | Calcul § 0 à § 8 : fenêtres, niveau, puissance et sensibilité, équivalence, rétrodiction, tableau entier, disponibilité, charge, kappa. Taille et seuils gelés ensemble. | Taille de base ; Seuil |

## Hypothèse

**H-E1 (bisociateur, hypothèse de conception ; R-638, synthèse § (iii) 1 ; R-735).** Pour une paire de revues (i, j) à la date t, le profil « trou à structure commune » Π_ij(t) — structure commune forte et canal faible, mesurés sur le seul passé de t — augmente la probabilité qu'un **pont validé** apparaisse entre i et j dans [t, t + 3), **au-delà** de ce que prédisent la distance D_ij(t), la popularité P_ij(t), l'attachement préférentiel PA_ij(t) et la distance sociale SOC_ij(t), d'au moins le seuil d'utilité de S6 (recommandé : rapport de cotes 1,5 par écart type de Π).

- Hypothèse de travail : les ponts validés sont une mesure bruitée des rapprochements réels entre revues ; la validité de cette mesure n'est éprouvée que par l'accord des lecteurs, le test de masquage et l'audit (aucune vérité extérieure).
- **Hypothèses rivales gelées** :
  - **HR-1 « distance seule suffit »** : la structure commune n'est que l'envers de la distance ; une fois D dans le modèle, β₂ ≈ 0.
  - **HR-2 « les trous restent des trous »** (barrière) : un canal faible signale un obstacle durable ; β₂ < 0.
  - **HR-3 « association statique »** : le profil marque des paires durablement propices sans rien anticiper ; il « prédit » autant les ponts passés que les futurs.
  - **HR-4 « popularité »** : le profil retrouve les grosses revues ; son effet disparaît avec P et PA.
  - **HR-5 « le trou est social »** (d'après le critère de pra2.1298, non opposable : distance de connaissance grande et distance sociale petite) : Π n'est qu'un indicateur de la distance sociale ; une fois SOC dans le modèle, β₂ ≈ 0.
- **Ce que l'épreuve n'autorise pas** (écrit d'avance) : aucune affirmation de causalité ; aucune affirmation sur la fertilité d'une paire au sens des courses ; aucun mot de « transition de phase », « criticité » ou « allumage » (R-878, point 4) ; aucune extension à une autre partition que celle de DE-1, ni hors des sciences physiques si DE-10 (a), ni hors des revues dont les résumés sont dans OpenAlex ; **un « réfuté » ne réfute que cette épreuve** (étiquette textuelle, revues, 1995–2023), pas l'idée du bisociateur (CE1-03) ; aucune lecture du coefficient de SOC comme confirmation ou réfutation de pra2.1298 (rapporté, non éprouvé).
- Ce que l'épreuve **n'est pas** : un test de Gu-Krenn (chantier parallèle, R-878 point 2), ni un test de la règle « loin en domaine, proche en concept ».

## Prédiction chiffrée et signe attendu

- **Sous H-E1** : β₂ > 0 ; rapport de cotes par écart type de Π d'au moins 1,5 (seuil d'utilité), ordre de grandeur 1,5 à 2,5 (SUPPOSÉ, aucun appui publié) ; aire du profil seul en prospective supérieure de plus de 0,03 à l'aire rétrodite (calcul § 4 : ≈ 0,10 d'écart sous un effet de 1,5 qui anticipe) ; coefficient de SOC négatif (rapporté).
- **Si H-E1 est fausse, signe attendu** :
  - sous HR-1, HR-4 ou HR-5 : β₂ ≈ 0, intervalle dans la bande S6 (ligne 2) ; si seule la variante sans SOC est positive, HR-5 est désignée (lecture croisée) ;
  - sous HR-2 : β₂ < 0 (borne haute < 0, ligne 3) ;
  - sous HR-3 : β₂ prospectif > 0 et aire rétrodite ≥ aire prospective − 0,03 (ligne 4).
- **Duel (rapporté, DE-2)** : sous H-E1, aire(Π) > max(aire(−D), aire(P), aire(PA), aire(−SOC)) ; sous HR-1, aire(Π) ≤ aire(−D).
- **Variante tierce niche** (rapportée) : même signe que la règle principale, effet plus petit.
- Ce qui compte comme réfutation : lignes 2 et 3 des critères de lecture.
- **R3** : aucun signe n'est visé. « Réfuté », « réfuté, signe inverse » et « suspendu » sont des issues de plein droit, qui décident autant que « non réfutée » de la place du profil dans le bisociateur (R-638 : le bras méta resterait étiqueté exploratoire).

## Métrique

**Unité** : (paire de revues non ordonnée, date de coupure t), dans une portion (E₁ prospective, E₂ prospective, E₂ rétrodite).

**Issue** Y = 1 si au moins un pont validé dans la fenêtre d'événement de la portion — prospective [t, t + 3) ; rétrodite [t − 8, t − 5) — 0 sinon. Définition opérationnelle (protocole 2b, C5 à C9) :
1. *Candidat* : œuvre de j publiée dans la fenêtre, dont le titre ou le résumé contient au moins un groupe de deux ou trois mots caractéristique de i (calculé sur les quatre ans qui précèdent la fenêtre) et absent de toutes les œuvres de j des six ans qui la précèdent ; symétriquement de j vers i. Groupes qui touchent L_S : selon DE-9.
2. *Lecture* : deux lecteurs isolés, aveugles au score, au statut, à la date de coupure, à l'année et aux auteurs, répondent à la question scellée (oui / non / indécidable) ; au plus 10 candidats lus par paire, cas et témoins.
3. *Pont validé* : « oui » chez les deux, sur un candidat qui compte pour la définition principale de DE-9. *Date* : `publication_date` du premier candidat validé lu. *Source* : moisson OpenAlex unique et figée.
4. *Accord* : kappa de Cohen (oui contre autre) ponctuel ≥ S1 sur le lot d'étalonnage de 200 paquets, intervalle à 95 % rapporté ; une seule révision de consigne ; sinon arrêt.

**Prédicteurs** (session des prédicteurs, table scellée avant toute jointure ; **toutes** les fenêtres ⊂ [t − 5, t), donc disjointes des deux fenêtres d'événement, GF2) :
- **S (structure commune)**, corpus amputés (C5 bis), fenêtre [t − w_s, t) : S_ij = Σ_{o ∈ L_S} min(f_i(o), f_j(o)) · log(N / n_o), où f_i(o) = part des œuvres de i (avec résumé, en anglais) qui mentionnent o dans la fenêtre ; N = nombre de revues actives de la moitié (trois paliers) en t ; n_o = nombre de ces revues où f(o) ≥ 1 % **dans la même fenêtre** (CE1-13).
- **C (canal)**, corpus amputés, fenêtre [t − w_s, t) : C_ij = log((F_ij + 0,5) / (E_ij + 0,5)), F_ij = citations de i vers j et de j vers i par des œuvres publiées dans la fenêtre ; E_ij = (s_i^out s_j^in + s_j^out s_i^in) / T, où s^out, s^in et T sont les citations sortantes, entrantes et totales **entre revues de la moitié**, par des œuvres de la même fenêtre (CE1-13).
- **Π (profil)**, quatre variantes scellées : V1 = Φ(S) · (1 − Φ(C)) (forme de R-638) et V2 = Φ(S) − Φ(C), chacune à w_s = 3 et w_s = 5 ; Φ = rang centile parmi les paires à risque de la moitié en t. Choix sur E₁ (Plan § 6).
- **D (distance)**, corpus **non amputés**, fenêtre [t − 5, t) : 1 − cosinus des vecteurs de fréquences des mots et groupes de deux mots, pondérées par l'inverse de la fréquence documentaire calculée sur les œuvres de la moitié de la **même fenêtre** (CE1-13).
- **P (popularité)** : log n_i + log n_j, œuvres avec résumé dans [t − 5, t).
- **PA (attachement préférentiel)** : log(1 + k_i) + log(1 + k_j), k = nombre de revues de la moitié avec lesquelles la revue échange au moins 3 citations dans [t − 5, t).
- **SOC (distance sociale, R-735 ; critère de pra2.1298 : plus court chemin moyen entre chercheurs des deux thèmes)** : graphe de cosignature G_t dont les nœuds sont les identifiants d'auteurs d'OpenAlex et les arêtes les cosignatures d'au moins une œuvre des revues de la moitié publiée dans **[t − 5, t)** (œuvres d'au plus 25 auteurs, S19) ; auteurs d'une revue = auteurs d'au moins une de ses œuvres de la fenêtre ; SOC_ij = moyenne de d(a, b) sur les couples (a, b), a parmi 20 auteurs tirés chez i, b parmi 20 tirés chez j (tous s'ils sont moins de 20 ; enfants `(1, moitié, t, revue)` de RACINE_PREDICTEURS), d = 0 si a = b, d = d_max + 1 si a et b ne sont pas reliés (d_max = plus grande distance finie de la moitié en t). **Non amputée.** Jamais cumulée depuis 1995 (elle recouvrirait la fenêtre rétrodite : garde G-A8). Variante rapportée : 1 − indice de Jaccard des ensembles d'auteurs. Signe attendu de son coefficient : négatif.
- **Covariables de mesure** (CE1-10) : moyenne des parts d'œuvres avec résumé des deux revues sur [t − 5, t) ; moyenne de leurs longueurs moyennes de résumé (en groupes de mots) sur [t − 5, t) ; moyenne de leurs parts d'œuvres avec résumé sur l'historique de nouveauté de la portion. Indicatrice « paire d'un palier d'extension » si un palier est ouvert.
- Toutes les variables continues sont standardisées à chaque date parmi les paires à risque de la portion.

**Statistique principale** : β₂ = coefficient de z(Π) dans la régression logistique Y ~ indicatrices de date + z(D) + z(P) + z(PA) + z(SOC) + covariables de mesure [+ indicatrice de palier] + z(Π), sur les cas et témoins de E₂ prospective. Erreur type robuste à deux voies par revue (appartenance multiple ; paire comptée une fois ; correction G/(G − 1)). Règle : borne basse β̂₂ − 1,96 × erreur type > 0 (S4). Intervalle de lecture : β̂₂ ± 1,96 × erreur type. Sensibilité : bootstrap par revues, 2 000 rééchantillons (enfant `(2,)` de RACINE_ANALYSE).

**Rétrodiction** : aire⁺(Π) et aire⁻(Π) = aires (Mann-Whitney) de z(Π) seul, variante choisie, sur les cas et témoins de E₂ prospective et de E₂ rétrodite ; suspension si aire⁻ ≥ aire⁺ − 0,03 (S5), appliquée seulement quand la borne basse de β₂⁺ est > 0. Rapportés : β̂₂⁻ et la règle (c) ; gains d'aire en validation croisée à 5 plis par paire (enfant `(1,)` de RACINE_ANALYSE).

**Rapportés sans verdict** : aires de Π, −D, P, PA, −SOC seuls (duel) ; coefficient de SOC ; modèle sans SOC ; modèle sans covariables de mesure ; décomposition (S seul, C seul, interaction) ; variante non amputée ; D amputé ; SOC par Jaccard ; variantes de DE-9 ; « contesté = pont » ; tierce niche (œuvre d'une troisième revue k qui reprend à la fois un terme de i et un terme de j, nouveaux pour k) ; kappa par portion, par année et par proximité ; test de masquage ; précision du filtre ; ponts parmi les témoins ; concentration des ponts par revue ; part de paires à S nul ; aires du profil seul par date.

## Seuil

Chaque seuil est **à geler par Lazar**, avec la recommandation de l'auteur et sa confiance. Confiance ≤ 0,6 : option, demander au collisionneur.

| Seuil | Objet | Recommandation | Confiance | État |
|---|---|---|---|---|
| S1 | Kappa minimal (oui contre autre), étalonnage et base | 0,60, valeur ponctuelle sur 200 paquets ; intervalle rapporté | 0,6 (option : collisionneur) | À REMPLIR |
| S2 | Quotas de ponts validés | M₂ = 300 (E₂ prospective) = 300 (E₂ rétrodite) ; M₁ = 150 (E₁) ; total 750 (DE-4 (a)) ; 200 / 200 / 100 si DE-4 (b) | 0,55 (option : collisionneur) | À REMPLIR |
| S3 | M_min : sous ce nombre en E₂ prospective ou rétrodite, « non concluant (base insuffisante) » | 150 (100 si DE-4 (b)) | 0,55 (option : collisionneur) | À REMPLIR |
| S4 | Valeur critique de la règle principale (DE-11) | 1,96, fixe | 0,75 | À REMPLIR |
| S5 | Règle de rétrodiction (DE-6) | aire⁻(Π) ≥ aire⁺(Π) − 0,03 → suspension | 0,6 (option : collisionneur) | À REMPLIR |
| S6 | Bande d'équivalence de β₂ (seuil d'utilité) | ± log 1,5 | 0,55 (option : collisionneur) | À REMPLIR |
| S7 | Horizon h | 3 ans | 0,6 (option : collisionneur) | À REMPLIR |
| S8 | Fenêtre des termes w_lab | 4 ans | 0,6 (option : collisionneur) | À REMPLIR |
| S8 bis | Décalage rétrodit g ; historique de nouveauté h_nov | g = max(w_s) = 5 ; h_nov = 6 ans | 0,7 | À REMPLIR |
| S9 | Dates de coupure | E₁ : 2009, 2011, 2013 ; E₂ : 2017, 2019, 2021 | 0,6 (option : collisionneur) | À REMPLIR |
| S10 | Revues | 500 (250 par moitié) + deux paliers de 100 (50 par moitié), sciences physiques si DE-10 (a) | 0,55 (option : collisionneur) | À REMPLIR |
| S11 | Activité d'une revue au cadre | 60 à 2 000 œuvres chaque année de 1995 à 2008 | 0,5 (option : collisionneur) | À REMPLIR |
| S12 | Couverture des résumés | ≥ 0,5 sur 2003–2008 au cadre ; ≥ 0,5 sur chaque fenêtre utilisée (protocole C3.6) | 0,55 (option : collisionneur) | À REMPLIR |
| S13 | Termes caractéristiques | 200 par revue et par fenêtre ; spécificité ≥ 10 ; fréquence ≥ max(5 ; 1 %) | 0,45 (option : collisionneur) | À REMPLIR |
| S14 | Témoins et plafond | K = 5 par cas ; plafond commun de 10 candidats lus par paire | 0,65 | À REMPLIR |
| S15 | Déclencheurs de l'audit de symétrie (R4) | liste des Critères | 0,6 (option : collisionneur) | À REMPLIR |
| S16 | Règle de choix de variante sur E₁ | plus grand z = β̂₂ / erreur type ; égalité à 0,01 près : V1 à w_s = 5 | 0,6 (option : collisionneur) | À REMPLIR |
| S17 | Plafond de lectures (deux lecteurs, base, hors fixes) | 90 000 (60 000 si DE-4 (b)) ; au-delà, arrêt et version nouvelle | 0,55 (option : collisionneur) | À REMPLIR |
| S18 | Garde de dégénérescence de S | part des paires à S nul parmi les cas et témoins de E₂ prospective > 0,5 → non concluant | 0,5 (option : collisionneur) | À REMPLIR |
| S19 | Paramètres de SOC | fenêtre [t − 5, t) ; œuvres d'au plus 25 auteurs ; 20 auteurs tirés par revue ; non reliés à d_max + 1 | 0,5 (option : collisionneur) | À REMPLIR |

Tests : la décision porte sur un seul test (β₂ de la variante choisie sur E₂ prospective) ; le choix parmi quatre variantes se fait sur E₁, disjointe : aucune correction de multiplicité n'est requise pour la règle principale. La rétrodiction est une condition de lecture, non un second test d'hypothèse. Tout le reste est rapporté sans verdict.

## Plan d'analyse

**§ 1. Données.** Moisson OpenAlex unique et figée (protocole 2b, C3 ; voie et plafond : DE-12, devis v2), revues tirées (C1–C2), base étiquetée (C9–C11). Session de construction : DE-8.

**§ 2. Moitiés.** Coupe aléatoire des revues en 𝒜 et ℬ, stratifiée par champ et par palier, scellée avant la moisson. E₁ = paires internes à 𝒜 ; E₂ = paires internes à ℬ ; paires traversantes jamais construites.

**§ 3. Construction de la base** (session distincte, aveugle au profil) : protocole 2b, C0 à C12. Quotas S2 ; plafond commun S14 ; plafond de lectures S17 ; extension par paliers (C7.3) ; règle de lecture déterministe et rejouable (C7.6).

**§ 4. Prédicteurs** (session distincte, sans étiquette) : S, C, Π (quatre variantes), D, P, PA, SOC, covariables, pour **toutes** les paires à risque de toutes les dates et portions, sur corpus amputés (S, C) et non amputés (tous, pour les variantes) ; table scellée avant la jointure. Temps processeur de SOC : quelques heures (parcours en largeur depuis ≈ 7 000 auteurs tirés par moitié et par date ; SUPPOSÉ).

**§ 5. Jointure et analyse** (session d'analyse) : jointure par identifiants des deux tables scellées ; aucun paramètre modifié.

**§ 6. Ordre de lecture.**
1. Préconditions : kappa ≥ S1 ; M₂ prospective et rétrodite ≥ M_min ; part de S nul ≤ S18 ; gardes vertes ; convergence.
2. **E₁** : β₂ des quatre variantes ; choix par S16 ; variante choisie scellée (fichier et empreinte) **avant** toute lecture de E₂.
3. **E₂ rétrodite** : aire⁻(Π) et β̂₂⁻ de la variante choisie.
4. **E₂ prospective** : β̂₂⁺, intervalle, aire⁺(Π) ; règle S5 ; critères de lecture.
5. Rapportés, lectures croisées.

**§ 7. Graines (R9)** : `numpy.random.SeedSequence` (numpy ≥ 1.25), trois racines distinctes écrites au scellement — RACINE_CONSTRUCTION (enfants du protocole, C0.5), RACINE_PREDICTEURS (enfants `(1, moitié, t, revue)` : auteurs tirés pour SOC) et RACINE_ANALYSE (enfants `(1,)` plis de validation croisée, `(2,)` bootstrap par revues) ; consignées au manifeste de chaque session avec configuration, empreintes, versions, commit. Le calcul de puissance a sa propre racine (20261031113500), sans lien avec ces trois.

**§ 8. Taille et justification** : S2 fixé par le calcul (section « Taille de base ») contre le tableau entier, non contre la seule puissance. Charge de lecture mesurée au moment où le quota de E₁ est atteint et projetée (protocole C7.8) ; si la projection dépasse S17, arrêt et version nouvelle (jamais d'abaissement silencieux de M).

**§ 9. Temps et coût.** Processeur seulement. Moisson : ≈ 5,9 USD attendus, plafond 35 USD (DE-12) ; aucune moisson sans ligne de GO. Lecteurs : DE-3 ; ≈ 610 à 2 840 appels pour 750 ponts. Aucun calcul sur carte graphique.

## Critères de lecture gelés

Table appliquée dans l'ordre ; la première ligne vraie décide.

| # | Issue observée | Verdict |
|---|---|---|
| 0 | Une garde de la Liste d'arrêt a sonné ; ou kappa < S1 après révision ; ou M₂ (prospective ou rétrodite) < M_min ; ou part de S nul > S18 ; ou régression non convergente | **non concluant** (cause nommée) |
| 1 | Déclencheur R4 (S15) dont l'audit n'est pas rendu | **non concluant** tant que l'audit n'est pas rendu |
| 2 | Intervalle β̂₂⁺ ± 1,96 × erreur type contenu dans ± S6 | **réfuté** : aucun effet utile au-delà des témoins (HR-1, HR-4 ou HR-5) |
| 3 | Borne haute β̂₂⁺ + 1,96 × erreur type < 0 | **réfuté, signe inverse** (HR-2) |
| 4 | Borne basse > 0 **et** aire⁻(Π) ≥ aire⁺(Π) − 0,03 | **suspendu** : le profil n'est pas distingué d'une association statique (HR-3) ; aucune lecture de β₂⁺ comme prédiction |
| 5 | Borne basse > 0, ligne 4 fausse | **H-E1 non réfutée** sur cette partition, ce domaine et ces dates ; le profil est admis comme hypothèse de travail du bras méta (toujours exploratoire) |
| 6 | Autre cas | **non concluant (puissance)** ; estimation et intervalle rapportés |

Caractéristiques opératoires (calcul § 4, M = 300, bande ± log 1,5) : sous le nul, ligne 2 à 0,873 ; sous un effet de 1,5 qui anticipe, ligne 5 à 0,938 ; sous une association statique, ligne 4 à 0,843 et ligne 5 à tort à 0,098 ; sous la barrière, ligne 3 à 0,943.

**Lectures croisées** (rapportées, sans changer le verdict) :
- ligne 5 avec duel perdu → « le profil ajoute aux témoins sans battre seul la distance » ;
- ligne 5 et règle (c) vraie (β̂₂⁻ ≥ β̂₂⁺ / 2) → réserve « association statique atténuée possible » (CE1-11) ;
- ligne 5 et variante (b′) de DE-9 non positive → réserve « dépend des groupes à objet partagé (continuité de vocabulaire) » ;
- ligne 5 et variante non amputée seule positive → réserve sur la dépendance à l'amputation ;
- ligne 5 et variante tierce niche négative → réserve sur l'étiquette ;
- ligne 2 et modèle sans SOC positif → « l'effet apparent du profil passe par la distance sociale » (HR-5 désignée) ;
- coefficient de SOC de signe positif → rapporté comme contraire au critère de pra2.1298 (sans verdict).

**R4 — même audit dans les deux sens** (S15). Déclencheurs, côté effet : rapport de cotes de Π ≥ 3 ; aire de Π seul ≥ 0,85 ; kappa ≥ 0,95 ; précision du filtre ≥ 0,9 ; plus de la moitié des ponts dans 5 revues ; plus de 80 % des ponts à une seule date. Côté nul (CE1-17) : rapport de cotes ≤ 1/3 ; aire de Π seul ≤ 0,15 ; |corrélation| de Π avec D ou avec SOC ≥ 0,9 parmi les paires à risque ; Π brut à moins de 10 valeurs distinctes à une date ; |β̂₂| < 0,001 ; erreur type robuste < 0,7 × erreur type naïve ; aires⁺ et ⁻ égales à 0,001 près ; précision du filtre ≤ 0,05. Qualité de l'étiquette : au moins 40 % des 30 ponts validés audités jugés « non » par le troisième lecteur. Audit : fuite temporelle (prédicteurs recalculés sur base tronquée en t, fenêtre de SOC), fuite d'étiquette (accès de la session des prédicteurs), aveugle des paquets, amputation, doublons, fenêtres (G-A8) ; rendu par un sous-agent neuf, scellé, avant tout verdict.

**Verdict prononcé par un sous-agent neuf** (ni auteur du préenregistrement ni de l'analyse), qui applique cette table ; scellé ; soumis à Lazar.

## Liste d'arrêt

| Condition | Action |
|---|---|
| Lecture d'une donnée réelle (moisson, pont, liste de rapprochements) avant le scellement de ce texte | arrêt ; écart consigné (R1) ; base reconstruite par une autre session |
| Préenregistrement, protocole 2b, L_S, listes fermées, gabarit des paquets ou ligne de GO d'empreinte fausse ou absente | arrêt avant la première requête |
| Clé d'OpenAlex imprimée ou écrite | arrêt ; clé à renouveler par Lazar |
| Projection du coût de la moisson au-delà du plafond du GO ; somme des `cost_usd` ≥ 95 % du plafond ; tout appel payant non couvert (modèle, machine) | arrêt ; devis nouveau et GO |
| Filtre de présence d'un résumé introuvable dans la documentation (protocole C0.6) | arrêt ; version nouvelle de C1.4 |
| Moisson incomplète (G-C4) ; deuxième extraction mêlée à la première | arrêt de la revue ; reprise complète (R12) |
| Fuite temporelle : terme, prédicteur, inverse de fréquence, marge, N, n_o, graphe de cosignature ou ensemble à risque qui lit une œuvre postérieure à sa fenêtre ; fenêtre de calcul qui recouvre une fenêtre d'événement | arrêt ; code refusé |
| Session de construction qui calcule ou lit un prédicteur ; session des prédicteurs qui lit une étiquette | arrêt ; base ou table refaite par une autre session ; audit R4 |
| Paquet qui contient un champ interdit (G-C5) ; lots non entrelacés (G-C7) ; rejeu de la file différent (G-C16) | arrêt de la lecture ; paquets refaits |
| Kappa < S1 après une révision | arrêt : non concluant (étiquette non fiable) |
| Projection ou compte de lectures > S17 | arrêt ; version nouvelle |
| Quota non atteint après les deux paliers | portion close ; M_min décide (ligne 0) |
| Paramètre modifié après lecture d'une étiquette ou d'un prédicteur joint | arrêt ; écart consigné |
| Variante choisie autrement que par S16, ou après lecture de E₂ | arrêt ; verdict non concluant |
| Revue, paire ou année d'événement prospectif commune à E₁ et E₂ | arrêt (GF5) |
| `except` qui rend une valeur par défaut ; numpy < 1.25 ; graine hors racine | arrêt (R5, R9) |
| Régression non convergente | arrêt de la lecture ; non concluant (cause numérique), jamais de repli silencieux |
| Variance robuste non positive | repli sur le bootstrap par revues, consigné (jamais silencieux) |
| Déclencheur R4 | audit ; ligne 1 |

**Gardes testées sur un cas sain et sur un artefact (R5)**, sur base jouet synthétique, avant toute requête : les vingt et une gardes de construction G-C1 à G-C21 (protocole 2b, C10), plus :
- **G-A1 prédicteurs sans futur** : S, C, D, P, PA, SOC, inverse de fréquence, marges, N, n_o recalculés sur la base tronquée en t identiques (sain) ; prédicteur qui lit une citation ou une cosignature de l'année t : écart détecté (artefact) ;
- **G-A2 amputation** : une œuvre de i qui contient un terme de T_j[t] **ou** de T_j[t − 8] est absente du corpus de (i, j) (sain) ; amputation désactivée en principal, ou limitée à T_j[t] : refusée (artefact) ;
- **G-A3 erreur type à deux voies** : base jouet à corrélation de revue connue, erreur type égale au calcul à la main (sain) ; erreur type naïve à la place : plus petite, détectée (artefact) ;
- **G-A4 règle de rétrodiction** : base jouet où le profil n'agit que sur le futur : pas de suspension (sain) ; même base où l'issue rétrodite est recopiée de l'issue prospective : suspension (artefact) ; la règle n'est appliquée que si la borne basse > 0 ;
- **G-A5 choix de variante** : choix par S16 sur une table jouet égal au calcul à la main (sain) ; fonction qui lit E₂ : refusée (artefact) ;
- **G-A6 étanchéité de la session des prédicteurs** : son arbre ne contient aucun fichier d'étiquette (sain) ; présence du fichier : refus de démarrer (artefact) ;
- **G-A7 calcul de puissance rejoué** : sortie identique à l'octet (sain) ; racine changée : sortie différente, détectée (artefact) ;
- **G-A8 fenêtres de calcul (GF2 partout)** : toutes les fenêtres de calcul (profil, témoins, covariables, graphe de SOC) ⊂ [t − 5, t) et disjointes des fenêtres d'événement (sain, même fonction que le § 0 du calcul) ; SOC sur le graphe cumulé depuis 1995, w_s = 6, g = 4 : refusés (artefacts) ;
- **G-A9 convergence** : base jouet ordinaire, convergence déclarée (sain) ; base jouet séparable : non-convergence détectée, arrêt (artefact).

## Dépendances

- **Dp-1 accès à OpenAlex** : session qui porte `OPENALEX_API_KEY` (R-849) ; voie et plafond : DE-12 et ligne de GO ; nom du filtre de résumé à vérifier (protocole C0.6) ; option b de DE-1 : accès aux métadonnées d'arXiv (refusé par le mandataire dans un environnement, R-625).
- **Dp-2 lecteurs** (DE-3) ; troisième lecteur d'audit.
- **Dp-3 lexique L_S** : liste fermée d'objets mathématiques et de méthodes du domaine retenu (DE-7, DE-10), construite **sans aucune donnée** par un sous-agent neuf à partir de classifications publiques (par exemple les intitulés de la classification des sujets mathématiques de 2020 et une liste de méthodes des sciences physiques), par une règle écrite, contre-lue et scellée avant ce préenregistrement. Pas encore écrite.
- **Dp-4 listes fermées** : mots vides, formules génériques ; scellées avant.
- **Dp-5 gabarit des paquets et consigne des lecteurs** : scellés avant.
- **Dp-6 quarantaine** : trois sessions distinctes (construction, prédicteurs, analyse), étanchéité éprouvée (G-C15, G-A6) ; la moisson de R-863 (`donnees/moisson-openalex-v1/`) **n'est pas réutilisée** (autre requête ; l'auteur ne l'a pas lue).
- **Dp-7 code** : construction, prédicteurs (dont SOC), analyse, gardes ; commit inscrit avant scellement.
- **Dp-8 temps** : charge de lecture (calcul § 6, S17) ; la base n'est pas sur le chemin de la porte G0.
- **Dp-9 GO de la moisson** (devis v2) ; **Dp-10 session-depot** active si DE-8 (a).

## Réserves de l'auteur

- Le modèle génératif du calcul est SUPPOSÉ de bout en bout ; la puissance dépend fortement de deux entrées non mesurées : la structure de corrélation de SOC avec Π et D (inflation de l'erreur type de 1,34) et l'hétérogénéité des revues (σ_U = 1,2 : 0,67 à M = 300). La puissance de 0,92 est un plafond.
- La règle de rétrodiction de la synthèse, non ajustée sur les témoins, laisse passer une association statique atténuée (atténuation 0,6 : « non réfutée » à tort 0,667 à M = 300) ; la règle (c) ferait mieux sans tout fermer ; la lecture croisée le signale sans changer le verdict.
- La qualité de l'étiquette gouverne tout : 20 % de faux ponts font passer la puissance de 0,917 à 0,79–0,83 (M = 300) ; le modèle de charge (§ 6) implique, si une paire signalée ne porte une vraie reprise que 3 fois sur 100, que la majorité des ponts validés seraient faux ; seuls l'audit (60 lectures), le test de masquage et le plafond S17 le surveillent.
- Le filtre de termes caractéristiques est lié à la distance (plus deux revues sont loin, plus les termes de i sont nouveaux pour j) : cela favorise le témoin D. Selon DE-9, un lien positif (b) ou négatif (b′) avec S reste possible ; les deux variantes sont rapportées.
- Le cadre ne garde que les revues dont les résumés sont dans OpenAlex sur 2003–2008 : sélection par éditeur (source non opposable sur les éditeurs sans résumés) ; généralisation limitée en conséquence.
- SOC est calculée sur les seules revues de la moitié (réseau tronqué) et sur des identifiants d'auteurs fusionnés ou scindés en 2026 (notes de version) ; la règle des 25 auteurs au plus est SUPPOSÉE.
- Le calcul ne simule ni le choix de variante sur E₁, ni l'amputation, ni les covariables de mesure, ni l'indicatrice de palier ; la charge pour 750 ponts est obtenue par proportionnalité.
- Les événements rétrodits de E₂ (2009–2015) et les événements prospectifs de E₁ partagent des années civiles sur des revues disjointes : un effet de période commun au choix de variante et à la rétrodiction est possible (il irait plutôt vers la suspension).
- Le seuil d'utilité (rapport de cotes 1,5) est un jugement de l'auteur, non un chiffre publié.
- Le « signe inverse » à tort sous le nul vaut 0,050 à M = 300 dans le § 4 (400 répétitions), contre ≈ 0,03 attendu : probablement du bruit.
- L'auteur est de la lignée conv-audit, comme le premier rédacteur et les pièces du bras méta ; la contre-lecture 2 doit venir d'un modèle autre qu'Opus.

## Contre-lecture

- **Contre-lecture 1** — sous-agent neuf Sonnet 5.5 (`claude-sonnet-5-5`), non auteur, 31 octobre 2026. Brouillon relu : `preenregistrement-E1-base-de-ponts-v1-brouillon1.md` `a22a211f48f7393bedea5ed88cf6699fe7ac97d87d9086d9dfd1c5f8f2989771`. Rapport : `prereg/brouillons/contre-lecture-E1-base-de-ponts-v1-brouillon1.md` `836b8c190e7fea6d469204ff7b4f0f307586591b0a896d1172cca8daae1f95eb`. Verdict du rapport : « présentable après corrections » (1 bloquant, 7 majeurs, 8 moyens, 4 mineurs). Traitement :

| Constat | Sort | Traitement (où) |
|---|---|---|
| CE1-01 bloquant — fenêtre rétrodite qui recouvre le calcul du profil à w_s = 5 | accepté | g = 5, fenêtre rétrodite [t − 8, t − 5) ; toutes les fenêtres de calcul ⊂ [t − 5, t) ; SOC jamais cumulée ; essai § 0 (sain accepté, quatre artefacts refusés) ; gardes G-C18, G-A8 ; moisson 1995–2023 vérifiée (Métrique ; S8 bis ; protocole 2b, § 0) |
| CE1-02 — « score » lu comme gain d'aire ; la lettre fonctionne sur l'aire du profil seul | accepté | règle de la synthèse rétablie (S5) ; « inutilisable » retiré ; DE-6 reformulée en trois lectures ; caractéristiques refaites à 400 répétitions (0,005 et 0,825 à M = 200) |
| CE1-03 — l'étiquette retire L_S alors que S s'en sert | accepté | DE-9 : (b) principale, (b′) et (a) en variantes ; marques `touche_LS`, `LS_partage` (protocole 2b) ; question alignée ; réserve et phrase « n'autorise pas » écrites ; option « texte intégral » refusée (absent de la moisson) |
| CE1-04 — L_S absent ; S presque nul hors des mathématiques | accepté | DE-10 (sciences physiques) ; Dp-3 précisée ; garde S18 ; part de S nul rapportée |
| CE1-05 — règle anticonservatrice ; permutation invalide | accepté | valeur critique fixe 1,96 (S4, DE-11), éprouvée sur 2 000 répétitions dans quatre configurations du nul (0,027 à 0,043) ; permutation abandonnée ; fausse alarme de l'équivalence rapportée (§ 3) |
| CE1-06 — charge de lecture sous-estimée | accepté | modèle par paire (§ 6) ; plafond commun de 10 (S14) ; plafond S17 ; mesure et projection au quota de E₁ ; arrêt si dépassé |
| CE1-07 — 200 ponts par moitié non garantis | accepté | 250 revues par moitié + deux paliers tirés d'avance ; plafond de 2 000 œuvres par an ; couverture des résumés au cadre ; § 5 ; devis v2 |
| CE1-08 — ordre des lignes, puissance de l'équivalence, cohérence | accepté | ordre refait (équivalence, signe inverse, suspension conditionnée à la borne basse, non réfutée) ; bande ± log 1,5 et prédiction ≥ 1,5 alignées ; tableau entier simulé ; probabilités côte à côte (DE-4) |
| CE1-09 — amputation non opérationnalisée | accepté | protocole C5 bis (termes des deux dates) ; témoins non amputés en principal ; G-A2 étendue |
| CE1-10 — résumés communs à S et à l'étiquette | accepté | trois covariables de mesure dans le modèle principal ; couverture sur l'historique ; modèle sans covariables rapporté |
| CE1-11 — association statique atténuée | accepté en partie | mondes atténués 0,6 et 0,8 simulés ; lecture croisée par la règle (c) et réserve écrite ; la tendance selon l'écart n'est pas estimable (g fixe) : aires par date rapportées à la place |
| CE1-12 — file scellée incompatible avec une lecture adaptative ; date d'appariement | accepté | règle déterministe et rejouable (C7, G-C16) ; date d'appariement = t |
| CE1-13 — fuites temporelles (inverse de fréquence, marges, N, n_o ; survie jusqu'en 2024) | accepté | fenêtres écrites pour chaque quantité ; G-A1 étendue ; activité sur 1995–2008 seulement (G-C20) |
| CE1-14 — garde de la session de construction plus faible | accepté | G-C15 ; signalements et candidats non remis aux prédicteurs |
| CE1-15 — modèle génératif favorable | accepté | grille de sensibilité (§ 1, § 2) ; taille choisie sur le tableau entier ; puissance déclarée comme plafond, lignes défavorables écrites |
| CE1-16 — kappa sans incertitude | accepté | 200 paquets ; intervalle rapporté ; lot exclu des quotas ; § 7 |
| CE1-17 — pôle « trop propre côté nul » | accepté | déclencheurs côté nul ajoutés (S15) |
| CE1-18 — format des décisions ; marqueur dans la prose | accepté | DE complètes (enjeu, deux ou trois options avec avantage et inconvénient) ; marqueur réservé aux états ouverts ; DE-9, DE-10, DE-11 ajoutées |
| CE1-19 — aveugle des lecteurs (revues, date) | accepté | test de masquage ; année et auteurs hors des paquets ; accord par année et par proximité ; recouvrement des familles noté (DE-3) |
| CE1-20 — divers | accepté | phrase de lecture « incrément » dans le résumé ; règle (c) avec β̂₂⁺ > 0 dans le calcul ; drapeau de convergence compté (0 sur 82 392) ; test des séquences avec seuil 0,01 (G-C7) |

- **Contre-lecture 2** — À REMPLIR — par un sous-agent neuf **d'un modèle autre qu'Opus**, non auteur de ce brouillon, du brouillon 1, des pièces du premier rédacteur ni des pièces du bras méta (Sonnet 5.5 a écrit la contre-lecture 1 : un autre lecteur Sonnet neuf convient, ou Fable 5.1 avec la réserve de la question 6). Fichiers à lui donner explicitement : ce brouillon ; le protocole 2b et le protocole 2 (pour le différentiel) ; le script et sa sortie (à rejouer deux fois à l'octet avec `python3 -I` depuis un dossier vide, ≈ 16 minutes chacune) ; le devis v2 et le devis v1 ; la contre-lecture 1 ; la synthèse v2 du lot bisociation (§ A, § (iii), § (iv)) ; les lignes R-878 et R-884 de `registres/decisions.md` de main, R-729 à R-735 de la branche ; la fiche pra2.1298 ; le gabarit et `src/controle_ia/prereg.py` ; rien de `donnees/`. Points à attaquer : (1) la règle de rétrodiction (a) et sa faiblesse devant l'atténuation ; (2) le seuil d'utilité 1,5 et la taille de 750 ponts ; (3) la définition et la fenêtre de SOC, la règle des 25 auteurs ; (4) DE-9 : les liens mécaniques positifs et négatifs ; (5) la condition de couverture au cadre et la sélection par éditeur ; (6) la charge de lecture et la qualité de l'étiquette ; (7) le modèle génératif (corrélations de SOC). Entrée à écrire ensuite : identifiant du sous-agent, empreinte du brouillon relu, chemin et empreinte de son rapport, traitement de chaque remarque.
