# Préenregistrement — E1′ / duel 1 : le profil « trou à structure commune » prédit-il les ponts futurs mieux que la distance seule et la popularité seule ? — v1 — BROUILLON 1 (non scellé)

**Statut : brouillon 1, non scellé ; contre-lecture par un modèle autre qu'Opus ; décisions de Lazar ; rien n'est collecté avant scellement.**

- Auteur : sous-agent neuf Opus 5.5 (`claude-opus-5-5`), lignée conv-audit, branche locale `canal/conv-audit-n04` (HEAD `050cd4e4…`), `origin/main` lu à `8c0f6f4b…`. Date (UTC) : 31 octobre 2026, rédaction commencée vers 10:58, relevé `date -u` 11:07 en cours de rédaction.
- Commande : mot direct de Lazar (31 octobre 2026, 10:57 UTC) : « Lancer la base de ponts d'E1′ : processeur, sans dépense — go ». Décisions applicables : R-878 (Bisociation, points 1 et 2 : gabarit des six garde-fous obligatoire ; base de ponts et Gu-Krenn en parallèle, sur processeur).
- Commit du code d'analyse : aucun. Le code de construction, de prédicteurs et d'analyse sera écrit, testé (gardes de la Liste d'arrêt, cas sain et artefact), commité et son commit inscrit ici **avant** le scellement.
- Nature : expérience décisive sur littérature réelle au sens de R1 ; pas une porte du programme. Elle décide d'une hypothèse de conception du bisociateur (le profil remplace-t-il la distance seule ?), non d'une hypothèse du programme.
- **Ce que l'auteur n'a pas fait** : aucune requête à OpenAlex ; rien lu sous `donnees/` ; aucune moisson, aucun pont, aucune liste de rapprochements datés lus ; aucun `git fetch`. Les seuls nombres calculés sont ceux du calcul de puissance sur données **synthétiques** (script et sortie ci-dessous).
- **Convention des chiffres.** « SUPPOSÉ » = valeur posée par l'auteur, sans appui publié vérifié ; « (calcul § k) » = paragraphe k de la sortie du calcul de puissance ; « (synthèse § x) » = section x de la synthèse v2 du lot bisociation ; « (Q6 § x) », « (Q7 § x) » = synthèses v2 des questions 6 et 7. Toutes les références de ces synthèses sont SUPPOSÉES (R7) : un emprunt y est un emprunt de raisonnement, jamais un chiffre opposable.
- Documents qui font foi ou lus (chemin, empreinte complète) :
  - synthèse v2 du lot bisociation : `docs/notes/bisociation-litterature-reelle-v1/collisionneur-bisociation-lot-v1/synthese-bisociation-lot-v2.md` `23c2888ddd924b85a0bbd0009a17f64723399d69ffd17669f56c4fddf7d18a86` (compagnon conforme) ;
  - synthèse v2 de la question 6 (sur `origin/main`) : `…/collisionneur-question-6-v1/synthese-question-6-v2.md` `ff3b19e3fb21a24329cd403efdf57db22423ce8630386425e3ac07c1207f05cf` ;
  - synthèse v2 de la question 7 (sur `origin/main`) : `…/collisionneur-question-7-v1/synthese-question-7-v2.md` `0ced3b28fa5cf1c2bc439fa4006a9a207dc9b3e69322c8709b4269c01d0352b0` ;
  - `registres/decisions.md` de `origin/main` (lignes R-878 et R-884) : contenu `0edd2154db8665ca91b84442cb0d20db21f44c86e993ae689be675a74d23c92f` ;
  - préenregistrement semi-réel, brouillon 4 : `prereg/brouillons/preenregistrement-identification-semi-reel-v1-brouillon4.md` `30f45ac5af140913bdd3fa34af3bdd2322850f6e052e5d856f5c1ce9e35081d3` (forme des six garde-fous et des moitiés disjointes ; aucun brouillon 5 n'existait localement ni sur `origin/main` à la lecture, vers 11:00 UTC ; un script `calcul-regles-identification-semi-reel-v1-brouillon5.py` est apparu depuis, non lu) ;
  - préenregistrement Gu-Krenn v2 (sur `origin/main`) : `docs/notes/gu-krenn-v1/prereg-gu-krenn-reproduction-et-hors-echantillon-v2.md` `7f32c4e0f841fe670b00bd726198770731a8edd4e09be54a4d302e035404a77b` (paires non reliées, appariement degré et âge, témoins attachement préférentiel et Simpson, dérive d'OpenAlex) ;
  - bras « trou à structure commune » : R-638 et R-672 de `registres/decisions.md` (branche locale) ; annexe du bras méta `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pre-pilote-course-2-v1/annexe-bras-meta-v1-brouillon1.md` `3a2e8dc2f8d764674941498ab0da9a977e7cbbd1478d868428efb8d1ca3441a0` et sa contre-lecture `…/contre-lecture-annexe-bras-meta-v1-brouillon1.md` `db249b9356f8d19cd8c9811c3db184b0d7587eba97ed8386501e146434e24f1d` ;
  - gabarit `prereg/gabarit-preregistrement-v1.md` `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e` ; validateur `src/controle_ia/prereg.py` `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306`.
  - Pièces compagnes de ce brouillon : calcul `prereg/brouillons/calcul-puissance-E1-base-de-ponts-v1-brouillon1.py` et sa sortie `….sortie.txt` ; protocole `prereg/brouillons/protocole-construction-base-de-ponts-E1-v1-brouillon1.md` (empreintes dans la passation qui les verse ; aucun compagnon `.sha256` écrit par l'auteur).

## Résumé en dix lignes pour Lazar

1. **Question** : sur la littérature réelle, une paire de niches (ici, deux revues) dont la communication est faible et la structure commune forte reçoit-elle plus souvent, dans les trois ans, un pont réel daté que ne le prédisent sa distance, sa popularité et l'attachement préférentiel ?
2. **Pont** : une œuvre parue dans une revue j qui reprend une méthode, un objet mathématique, un modèle ou un résultat propre à la revue i, détectée par un filtre de termes **sans aucune citation**, puis validée « oui » par **deux lecteurs isolés** (accord minimal kappa ≥ 0,60, à geler) ; date = date de publication de la première œuvre validée.
3. **Profil** calculé sur le seul passé de chaque date, sur un corpus **amputé** des œuvres qui parlent déjà la langue de l'autre niche ; l'étiquette exclut par construction le lexique de structure (disjonction).
4. **Règle principale** : coefficient β₂ du profil, ajusté sur distance, popularité et attachement préférentiel, borne basse de l'intervalle à 90 % > 0.
5. **Rétrodiction inversée obligatoire** : le même profil « prédit »-il les ponts d'avant sa fenêtre de calcul ? Si oui, suspension.
6. **Moitiés disjointes** par niche et par période : E₁ (revues 𝒜, dates 2009–2013) pour l'étalonnage et le choix parmi quatre variantes scellées ; E₂ (revues ℬ, dates 2017–2021) pour la seule décision.
7. **Puissance** (données synthétiques) : 30 à 50 ponts ne suffisent pas (puissance 0,63 à 50 ponts contre un rapport de cotes de 1,5) ; recommandation : **500 ponts validés** (200 en E₂ prospective, 200 en E₂ rétrodite, 100 en E₁) ; la règle de rétrodiction de la synthèse (δ₀ = 0,03) suspendrait presque toujours un vrai effet : règle (c) proposée.
8. **Construction** par une session distincte, aveugle au profil ; protocole pas à pas dans la pièce compagne.
9. **Coût** : processeur ; OpenAlex dans l'allocation gratuite ou devis ; lecteurs = sous-agents de session (sans dépense) ou devis.
10. **Pour geler** : seuils S1 à S16 et décisions DE-1 à DE-8 (toutes « À REMPLIR ») ; contre-lecture par un modèle autre qu'Opus.

## Décisions à soumettre à Lazar (DE-1 à DE-8)

Format : décision ; enjeu ; options (avantage, inconvénient) ; recommandation et confiance. **Aucune ne prend de défaut à 48 heures** : elles se gèlent avec le préenregistrement (R1). Confiance ≤ 0,6 : « option : demander au collisionneur ».

- **DE-1 — Qu'est-ce qu'une niche ?** État : À REMPLIR.
  - Enjeu : la partition doit être extérieure au graphe des ponts et datée (synthèse § A : « une partition calculée sans la couche des équations » ; le modèle de blocs « regroupe les adversaires qui se citent »).
  - (a) **Revues d'OpenAlex** (échantillon scellé de 300). Avantage : entité datée et extérieure (une œuvre appartient à sa revue dès sa parution), tout dans OpenAlex. Inconvénient : une revue n'est pas une communauté ; revues pluridisciplinaires à exclure.
  - (b) **Catégories d'arXiv** (catégorie principale choisie par l'auteur au dépôt). Avantage : choisie par l'auteur à la date du dépôt, champ où « même objet mathématique » a un sens. Inconvénient : couverture limitée à arXiv ; accès à vérifier (arxiv.org refusé dans un environnement, R-625) ; catégories grossières (environ 150).
  - (c) **Sujets (« topics ») d'OpenAlex**. Avantage : fin, prêt. Inconvénient : SUPPOSÉ à vérifier dans la documentation d'OpenAlex — créés en 2024 par regroupement d'un graphe de citations et attribués par un classeur qui lit aussi les références : la partition connaîtrait l'avenir des dates antérieures à 2024 et toucherait le canal.
  - (d) Communautés calculées à chaque date sur le passé. Inconvénient : circularité de partition (les communautés minimisent par construction le canal entre elles).
  - **Recommandation : (a), confiance 0,55** — option : demander au collisionneur.
- **DE-2 — Forme de la règle principale.** État : À REMPLIR.
  - (a) **Incrément** : β₂ > 0 à distance, popularité et attachement préférentiel contrôlés (forme de l'espèce A, T3-A, synthèse § (iii)). Avantage : dit ce qui sert au bisociateur (le profil apporte-t-il quelque chose de plus ?). Inconvénient : la lettre « mieux que » est un duel.
  - (b) **Duel** : aire du profil seul > max(aire de chaque témoin seul), borne basse > 0 (forme de B-iii chez Gu-Krenn). Avantage : lettre de la question. Inconvénient : un profil corrélé à la distance peut gagner le duel sans rien ajouter.
  - (c) Les deux, conjonctifs. Inconvénient : puissance plus basse.
  - **Recommandation : (a) décisive, (b) rapportée avec signe prédit, confiance 0,6** — option : demander au collisionneur.
- **DE-3 — Qui lit ?** État : À REMPLIR.
  - (a) **Deux sous-agents de session de familles différentes** (Sonnet 5.5 et Fable 5.1), appels neufs et isolés. Avantage : sans dépense, rapide. Inconvénient : deux familles d'un même fournisseur ; mémoire possible des œuvres célèbres (elle touche le jugement du texte, pas la prédiction).
  - (b) Modèles payants de deux fournisseurs (par exemple un Claude et Kimi). Avantage : indépendance de lignée. Inconvénient : dépense (devis, GO).
  - (c) Lecteurs humains. Avantage : référence. Inconvénient : contact externe (nœud), plusieurs milliers de lectures (calcul § 7).
  - **Recommandation : (a), plus un audit de 60 lectures par un troisième lecteur (humain si possible), confiance 0,6** — option : demander au collisionneur.
- **DE-4 — Contre quelle alternative la puissance est-elle calculée (fixe M) ?** État : À REMPLIR. Options : rapport de cotes 2,0 par écart type (M plus petit) ; 1,5 (recommandé) ; 1,25 (M au-delà de ce que la population offre probablement). **Recommandation : 1,5, confiance 0,5** — option : demander au collisionneur. Voir « Taille de base ».
- **DE-5 — Rôle de la moitié E₁.** État : À REMPLIR. (a) **Étalonnage des lecteurs et choix d'une variante parmi quatre, scellées, par une règle scellée** ; E₂ décide seule. Avantage : l'instrument est jeune (C place le goulot dans la validité de l'observable, synthèse § Verdict 3). Inconvénient : E₁ n'est pas une réplication. (b) Variante unique gelée, E₁ = réplication conjonctive. Inconvénient : il faut M ponts dans chaque moitié (le double de lectures). **Recommandation : (a), confiance 0,6** — option : demander au collisionneur.
- **DE-6 — Règle de rétrodiction inversée.** État : À REMPLIR. (a) Lettre de la synthèse : gain d'aire rétrodit ≥ gain d'aire prospectif − δ₀, δ₀ = 0,03. (b) Même forme, δ₀ = 0,01. (c) **β₂ rétrodit estimé ≥ moitié du β₂ prospectif estimé.** Le calcul (§ 5) montre que (a) suspend presque toujours, même quand le profil anticipe vraiment : le gain d'aire d'un rapport de cotes de 1,5 est de l'ordre de 0,01 à 0,02, sous δ₀. **Recommandation : (c) décisive, (a) rapportée, confiance 0,55** — option : demander au collisionneur. C'est un écart à la lettre de la synthèse (T3-B), écrit comme tel.
- **DE-7 — La structure commune compte-t-elle les jeux de données ?** État : À REMPLIR. R-638 nomme « objet mathématique, méthode, jeu de données » ; l'annexe du bras méta les lit sans les compter, et sa contre-lecture (CA1-04) note que le même argument vaut pour toute structure quasi universelle. Ici : (a) **objets mathématiques et méthodes seulement, pondérés par la rareté** (la pondération retire d'elle-même les structures quasi universelles) ; (b) les trois types. **Recommandation : (a), confiance 0,55** — option : demander au collisionneur.
- **DE-8 — Où vit la session de construction ?** État : À REMPLIR. Elle doit posséder la clé d'OpenAlex (`OPENALEX_API_KEY`, présente dans l'environnement de session-depot selon R-849) et n'avoir jamais vu de prédicteur. (a) **Une instance neuve de session-depot** ; (b) conv-audit (nouvelle instance). **Recommandation : (a), confiance 0,7.**

## Taille de base : divergence 30–50 contre « plus » tranchée par le calcul

Calcul sur données synthétiques (`calcul-puissance-E1-base-de-ponts-v1-brouillon1.py`, sortie rejouée deux fois à l'octet près), modèle génératif décrit en tête du script (corrélation −0,5 entre profil et distance, effets propres de la distance, de la popularité et de l'attachement préférentiel, propension de niche, plan cas-témoins à K = 5 témoins par cas, erreur type robuste à deux voies par niche). Tout est SUPPOSÉ : la structure du calcul est opposable, ses entrées non.

Empreintes : script `db04ebbbdfd1fb3f75044e16587e7e580a43ee4572f64df7bf44229c4d3e42ed`, sortie `d0af5c92da31b90c3e531673b96bad369616b1c41fdef9051f5361a593418453` (deux exécutions `python3 -I` depuis deux dossiers temporaires vides, sorties identiques à l'octet ; numpy 2.5.3, Python 3.13.18 ; 7 min 47 s de temps mural).

Puissance de la règle principale (borne basse à 90 % de β₂ > 0), 400 répétitions par case (calcul § 1) ; M = ponts validés de la portion de décision, K = 5 témoins par cas :

| Rapport de cotes par écart type de Π \ M | 30 | 50 | 100 | 200 | 300 | 500 | 800 |
|---|---|---|---|---|---|---|---|
| 1,00 (fausse alarme) | 0,033 | 0,043 | 0,068 | 0,060 | 0,080 | 0,068 | 0,080 |
| 1,25 | 0,280 | 0,328 | 0,475 | 0,680 | 0,787 | 0,927 | 0,975 |
| 1,50 | 0,537 | 0,632 | 0,855 | 0,980 | 1,000 | 1,000 | 1,000 |
| 2,00 | 0,815 | 0,948 | 0,995 | 1,000 | 1,000 | 1,000 | 1,000 |
| 3,00 | 0,980 | 0,998 | 1,000 | 1,000 | 1,000 | 1,000 | 1,000 |

Autres caractéristiques (calcul § 3 à § 5) :
- **Équivalence** sous β₂ = 0 (intervalle à 90 % dans ± marge) : marge log 1,25 → 0,458 à M = 200, 0,880 à M = 500 ; marge log 1,5 → 0,983 à M = 200. Une marge log 1,10 est inatteignable dans la grille.
- **Bruit d'étiquette** (rapport de cotes 1,5) : à M = 200, 20 % de faux ponts font passer la puissance de 0,980 à 0,925.
- **Rétrodiction** (rapport de cotes 1,5, 300 répétitions) — probabilité de suspension :

| Monde | M | gain d'aire prospectif | règle (a) δ₀ = 0,03 | règle (b) δ₀ = 0,01 | règle (c) β̂₂⁻ ≥ β̂₂⁺/2 | P(confirmé), règle (c) |
|---|---|---|---|---|---|---|
| anticipation (β₂⁻ = 0) | 100 | +0,013 | 0,867 | 0,393 | 0,080 | 0,807 |
| anticipation | 200 | +0,014 | 0,960 | 0,307 | 0,053 | 0,937 |
| moitié (β₂⁻ = β₂/2) | 200 | +0,012 | 0,987 | 0,600 | 0,537 | 0,463 |
| statique (β₂⁻ = β₂) | 100 | +0,013 | 0,977 | 0,757 | 0,910 | 0,087 |
| statique | 200 | +0,012 | 1,000 | 0,820 | 0,957 | 0,040 |

  À rapport de cotes 2,0, la règle (a) suspend encore environ une fois sur deux en monde d'anticipation (0,457 à 0,517).
- **Disponibilité** (calcul § 6, arithmétique) : 150 revues par moitié donnent 33 525 paires × dates ; à un taux de base de ponts validés de 0,5 % / 1 % / 2 % par paire et par fenêtre de 3 ans, 168 / 335 / 670 ponts au plus. Le taux réel est inconnu.
- **Lectures** (calcul § 7) : 2 200 à 5 000 lectures pour une portion de 200 ponts (q = 0,4 à 0,2 de précision du filtre, SUPPOSÉ).

**Conclusion.** **30 à 50 ponts ne suffisent pas** sauf si l'effet est fort : à 50 ponts, la puissance vaut 0,63 contre un rapport de cotes de 1,5 et 0,33 contre 1,25 ; elle n'atteint 0,80 qu'à partir d'un rapport de cotes de 2,0 (0,815 à 30, 0,948 à 50) ; et l'équivalence (« pas d'effet utile ») n'est presque jamais démontrable sous 100 ponts (≤ 0,35). La position de A et D (« une base assez grande pour avoir de la puissance ») est retenue. **Recommandation (S2) : M₂ = 200 ponts validés en E₂ prospective, 200 en E₂ rétrodite, 100 en E₁, soit 500 ponts validés au total.** À 200, contre un rapport de cotes de 1,5 : puissance 0,980, probabilité de confirmation avec la règle (c) de rétrodiction 0,937 en monde d'anticipation, suspension 0,957 en monde statique, marge contre 20 % de faux ponts. **M_min (S3) = 100** (puissance 0,855 ; confirmation 0,807). Deux constats chiffrés : (1) **la règle de la synthèse (δ₀ = 0,03 sur l'aire) est inutilisable** à ces tailles d'effet : elle suspend 0,96 fois sur 1 un profil qui anticipe vraiment (DE-6) ; (2) **la règle principale est un peu anti-conservatrice** : fausse alarme 0,060 à 0,080 pour M ≥ 100 au lieu de 0,05 (erreur de Monte-Carlo ± 0,013) ; correction à fixer au brouillon 2, avant gel (S4).

## Six garde-fous de R-878 (obligatoires dans tout préenregistrement sur littérature réelle)

R-878, point 1 (Bisociation), rend obligatoire le gabarit de la synthèse v2 (§ (iv), décision 1 : « sinon, le résultat positif est acquis par construction »). Ici les garde-fous gardent **exactement** ce pour quoi ils ont été écrits : la vérité est une étiquette lue dans la littérature réelle.

| GF | Garde-fou | Ce qu'il ferme ici | Application concrète | Où |
|---|---|---|---|---|
| GF1 | **Étiquette de pont indépendante du canal** | La circularité relevée par D (T2-D : « le critère de pont risque d'être circulaire ») et l'artefact A0 (un trou lu dans le flux de citations prédit mécaniquement une hausse du flux). | Le pont n'utilise **aucune citation** : filtre de termes caractéristiques de i nouveaux dans j, puis validation par deux lecteurs qui ne voient ni citation ni score. Le canal C est mesuré par les citations, l'étiquette jamais. Disjonction supplémentaire avec la structure : les termes du lexique L_S sont retirés du filtre (G-C3). Forme retenue parmi les trois de la synthèse (§ A) : la « reprise traversante validée » de D, sans exiger la tierce niche de A (variante tierce niche rapportée). | Définition du pont ; protocole C5–C9 |
| GF2 | **Rétrodiction inversée** | A0 (symétrique dans le temps) et toute association statique entre le profil et les ponts (propension durable de la paire, empreinte d'anciens ponts). | Même profil calculé sur [t − w, t), confronté aux ponts de la fenêtre [t − w − h, t − w), **antérieure** à sa fenêtre de calcul, même plan cas-témoins, même M ; règle de suspension DE-6 (S5). Lue avant la règle principale. | Métrique ; Seuil S5 ; Critères, ligne 2 |
| GF3 | **Graphe amputé des ponts** | L'empreinte mécanique des ponts passés sur le score (un pont ajoute des citations, donc du canal, et des termes, donc de la structure) et la circularité de la partition. | (a) Niches = revues, entité extérieure au graphe des ponts (DE-1). (b) Pour la paire (i, j), S, C et D sont calculés **sans** les œuvres de i (resp. j) qui contiennent un terme caractéristique de j (resp. i) : corpus amputé, défini par le texte seul, sans étiquette. (c) Variante non amputée rapportée. | Métrique ; Plan § 4 |
| GF4 | **Bras « popularité seule »** | Un profil qui ne fait que retrouver les grosses revues. | P (taille des deux niches) et PA (attachement préférentiel, produit des degrés dans le graphe des niches) entrent dans le modèle de la règle principale et sont rapportés comme classeurs seuls (aires). | Métrique ; Critères |
| GF5 | **Jeux disjoints par niche et par période** | Une association persistante d'une niche ou commune à une période prise pour une prédiction. | Revues coupées au hasard en 𝒜 et ℬ ; E₁ = paires internes à 𝒜 aux dates 2009, 2011, 2013 (événements jusqu'en 2015) ; E₂ = paires internes à ℬ aux dates 2017, 2019, 2021 (événements de 2017 à 2023) ; aucune niche, aucune paire, aucune année d'événement prospectif commune ; les fenêtres de calcul et rétrodites de E₂ partagent des années civiles avec E₁, **sur des niches disjointes** (écrit). Choix de variante sur E₁ seule ; décision sur E₂ seule. | Plan § 2, § 6 |
| GF6 | **Calcul de puissance préalable** | Une règle impossible à tenir ou à manquer. | Calcul sur données synthétiques : M pour 0,80 de puissance contre une alternative nommée (DE-4), fausse alarme, bande d'équivalence atteignable, bruit d'étiquette, caractéristiques opératoires des trois règles de rétrodiction (calcul § 1 à § 7). N et seuil gelés ensemble (Q6 § (d), « Puissance »). | Taille de base ; Seuil |

## Hypothèse

**H-E1 (bisociateur, hypothèse de conception ; R-638, synthèse § (iii) 1).** Pour une paire de niches (i, j) à la date t, le profil « trou à structure commune » Π_ij(t) — structure commune forte et canal faible, mesurés sur le seul passé de t — augmente la probabilité qu'un **pont validé** apparaisse entre i et j dans [t, t + h), **au-delà** de ce que prédisent la distance D_ij(t), la popularité P_ij(t) et l'attachement préférentiel PA_ij(t).

- Hypothèse de travail : les ponts validés sont une mesure (bruitée) des rapprochements réels entre niches ; la validité de cette mesure est elle-même éprouvée seulement par l'accord des lecteurs et l'audit (non par une vérité extérieure).
- **Hypothèses rivales gelées** :
  - **HR-1 « distance seule suffit »** : la structure commune n'est que l'envers de la distance ; une fois D dans le modèle, β₂ ≈ 0.
  - **HR-2 « les trous restent des trous »** (barrière) : un canal faible signale un obstacle durable ; β₂ < 0.
  - **HR-3 « association statique »** : le profil marque des paires durablement propices, sans rien anticiper ; il « prédit » autant les ponts passés que les futurs (rétrodiction ≈ prospection).
  - **HR-4 « popularité »** : le profil retrouve les grosses revues ; son effet disparaît avec P et PA.
- **Ce que l'épreuve n'autorise pas** (écrit d'avance) : aucune affirmation de causalité (le profil ne « crée » pas les ponts) ; aucune affirmation sur la fertilité d'une paire au sens des courses ; aucun mot de « transition de phase », « criticité » ou « allumage » (R-878, point 4 : suspendu jusqu'à E2′) ; aucune extension à d'autres partitions que celle de DE-1 ; aucune généralisation hors des domaines des revues tirées.
- Ce que l'épreuve **n'est pas** : un test de Gu-Krenn (chantier parallèle, R-878 point 2), ni un test de la règle basique « loin en domaine, proche en concept ».

## Prédiction chiffrée et signe attendu

- **Sous H-E1** : β₂ > 0 ; rapport de cotes par écart type de Π entre 1,2 et 2,0 (SUPPOSÉ, aucun appui publié) ; gain d'aire en validation croisée entre +0,005 et +0,04 (calcul § 5, ordre de grandeur de ce que donne un tel rapport de cotes) ; rétrodiction : β₂ rétrodit nettement plus petit que β₂ prospectif (moins de la moitié).
- **Si H-E1 est fausse, signe attendu** :
  - sous HR-1 : β₂ ≈ 0 (intervalle à 90 % dans la bande d'équivalence S6 si M suffit) ;
  - sous HR-2 : β₂ < 0 (borne haute de l'intervalle à 90 % < 0) ;
  - sous HR-3 : β₂ prospectif > 0 **et** β₂ rétrodit ≥ moitié du prospectif → suspension ;
  - sous HR-4 : β₂ ≈ 0 avec P et PA, alors que l'aire de Π seul dépasse 0,5.
- **Duel (rapporté, DE-2)** : signe prédit sous H-E1 : aire(Π) > max(aire(−D), aire(P), aire(PA)) ; sous HR-1 : aire(Π) ≤ aire(−D).
- **Variante tierce niche** (rapportée) : même signe que la règle principale, effet plus petit.
- Ce qui compte comme réfutation : lignes 4 et 5 des critères de lecture.
- **R3** : aucun signe n'est visé. Les issues « réfuté », « réfuté avec signe inverse » et « suspendu » sont des issues de plein droit, qui décident autant que « non réfuté » de la place du profil dans le bisociateur (R-638 : le bras méta resterait étiqueté exploratoire).

## Métrique

**Unité** : (paire de niches non ordonnée, date de coupure t), dans une portion (E₁ prospective, E₂ prospective, E₂ rétrodite).

**Issue** Y = 1 si au moins un pont validé dans la fenêtre d'événement de la portion (prospective [t, t + h) ; rétrodite [t − w_lab − h, t − w_lab)), 0 sinon. Définition opérationnelle du pont (protocole C5–C9, résumé) :
1. *Candidat* : œuvre de j publiée dans la fenêtre, dont le titre ou le résumé contient au moins un groupe de deux ou trois mots **caractéristique de i** (calculé sur les w_lab ans qui précèdent la fenêtre) et **absent de toutes les œuvres de j antérieures** à la fenêtre ; symétriquement de j vers i ; tout groupe qui touche le lexique de structure L_S est retiré.
2. *Lecture* : deux lecteurs isolés, aveugles au score, au statut cas ou témoin, à la date de coupure, répondent à la question scellée (oui / non / indécidable).
3. *Pont validé* : « oui » chez les deux. *Date* : `publication_date` du premier candidat validé. *Source* : moisson OpenAlex unique et figée (empreintes du manifeste de construction).
4. *Accord minimal* : kappa de Cohen (oui contre autre) ≥ S1 sur le lot d'étalonnage de 100 paquets ; une seule révision de consigne permise ; sinon arrêt.

**Prédicteurs** (session des prédicteurs, sur le corpus amputé de GF3, fenêtre de calcul [t − w_s, t), w_s selon la variante ; standardisés à chaque date) :
- **S (structure commune)** : S_ij = Σ_{o ∈ L_S} min(f_i(o), f_j(o)) · log(N / n_o), où f_i(o) = part des œuvres de i qui mentionnent o, N = nombre de niches de la moitié, n_o = nombre de niches où f(o) ≥ 1 % (pondération par la rareté ; DE-7).
- **C (canal)** : C_ij = log((F_ij + 0,5) / (E_ij + 0,5)), F_ij = citations de i vers j et de j vers i par des œuvres publiées dans la fenêtre, E_ij = (s_i^out s_j^in + s_j^out s_i^in) / T, marges calculées dans la moitié (valeur attendue à marges conservées).
- **Π (profil)**, quatre variantes scellées : V1 = Φ(S) · (1 − Φ(C)) (produit des rangs centiles à la date, forme de R-638) et V2 = Φ(S) − Φ(C) (forme additive), chacune à w_s = 3 et w_s = 5 ans. Choix sur E₁ (Plan § 6).
- **D (distance seule)** : 1 − cosinus des vecteurs de fréquences pondérées (inverse de la fréquence documentaire) de tous les mots et groupes de deux mots des deux corpus.
- **P (popularité seule)** : log n_i + log n_j (œuvres avec résumé dans la fenêtre).
- **PA (attachement préférentiel)** : log(1 + k_i) + log(1 + k_j), k = nombre de niches de la moitié avec lesquelles la niche échange au moins 3 citations dans la fenêtre.

**Statistique principale** : β₂ = coefficient de z(Π) dans la régression logistique Y ~ indicatrices de date + z(D) + z(P) + z(PA) + z(Π), sur les cas et témoins de E₂ prospective. Intervalle à 90 % par erreur type robuste à deux voies par niche (appartenance multiple ; intersection = paire ; correction G/(G − 1)). Sensibilité : bootstrap par niches, 2 000 rééchantillons (synthèse § (iii) 1, T3-A).

**Rétrodiction** : β₂⁻ et gain d'aire⁻, même modèle, sur E₂ rétrodite. **Gain d'aire** : aire (Mann-Whitney) des prédictions en validation croisée à 5 plis par paire du modèle complet moins celle du modèle sans Π.

**Rapportés sans verdict** : aires de Π, −D, P, PA seuls ; décomposition (S seul, C seul, interaction) ; variante non amputée ; variante « contesté = pont » ; variante tierce niche (œuvre d'une troisième revue k qui reprend à la fois un terme de i et un terme de j, nouveaux pour k) ; kappa par portion ; précision du filtre (part des candidats validés) ; ponts trouvés parmi les témoins ; concentration des ponts par revue.

## Seuil

Chaque seuil est **À REMPLIR** (gel par Lazar), avec la recommandation de l'auteur et sa confiance. Confiance ≤ 0,6 : option, demander au collisionneur.

| Seuil | Objet | Recommandation | Confiance | État |
|---|---|---|---|---|
| S1 | Kappa minimal (oui contre autre), étalonnage et base | 0,60 | 0,6 (option : collisionneur) | À REMPLIR |
| S2 | M₂ = ponts validés en E₂ prospective (= en E₂ rétrodite) ; M₁ = ⌈M₂/2⌉ en E₁ | M₂ = 200 (E₂ prospective) = 200 (E₂ rétrodite) ; M₁ = 100 ; total 500 | 0,5 (option : collisionneur) | À REMPLIR |
| S3 | M_min : sous ce nombre en E₂ prospective, « non concluant (base insuffisante) » | 100 | 0,5 (option : collisionneur) | À REMPLIR |
| S4 | Niveau : borne basse unilatérale à 95 % (intervalle bilatéral à 90 %) ; **correction de la fausse alarme** (0,060 à 0,080 observée pour M ≥ 100, calcul § 1) | 0,05 unilatéral, valeur critique étalonnée par simulation du nul sur le plan réel (permutation de Π entre paires d'une même date, 1 000 tirages, enfant `(3,)` de RACINE_ANALYSE), à écrire et éprouver au brouillon 2 | 0,5 (option : collisionneur) | À REMPLIR |
| S5 | Règle de rétrodiction (DE-6) | β̂₂⁻ ≥ β̂₂⁺ / 2 → suspension | 0,55 (option : collisionneur) | À REMPLIR |
| S6 | Bande d'équivalence de β₂ | ± log 1,25 | 0,5 (option : collisionneur) | À REMPLIR |
| S7 | Horizon h | 3 ans | 0,6 (option : collisionneur) | À REMPLIR |
| S8 | Fenêtre d'étiquette w_lab | 4 ans | 0,6 (option : collisionneur) | À REMPLIR |
| S9 | Dates de coupure | E₁ : 2009, 2011, 2013 ; E₂ : 2017, 2019, 2021 | 0,6 (option : collisionneur) | À REMPLIR |
| S10 | Revues tirées | 300 (150 par moitié) | 0,55 (option : collisionneur) | À REMPLIR |
| S11 | Activité d'une revue | ≥ 60 œuvres par an, 1995–2024 | 0,5 (option : collisionneur) | À REMPLIR |
| S12 | Couverture des résumés | ≥ 0,5 par fenêtre | 0,5 (option : collisionneur) | À REMPLIR |
| S13 | Termes caractéristiques | 200 par niche et par fenêtre ; spécificité ≥ 10 ; fréquence ≥ max(5 ; 1 %) | 0,45 (option : collisionneur) | À REMPLIR |
| S14 | Témoins | K = 5 par cas ; plafond de 20 candidats lus par témoin signalé | 0,65 | À REMPLIR |
| S15 | Déclencheurs de l'audit de symétrie (R4) | liste des Critères | 0,6 (option : collisionneur) | À REMPLIR |
| S16 | Règle de choix de variante sur E₁ | plus grand z = β̂₂ / erreur type ; égalité : V1 à w_s = 5 | 0,6 (option : collisionneur) | À REMPLIR |

Tests : la décision porte sur un seul test (β₂ de la variante choisie sur E₂) ; le choix parmi quatre variantes se fait sur E₁, disjointe : aucune correction de multiplicité n'est requise pour la règle principale. La rétrodiction est une condition de lecture, non un second test d'hypothèse. Tout le reste est rapporté sans verdict.

## Plan d'analyse

**§ 1. Données.** Moisson OpenAlex unique et figée (protocole C3), revues tirées (C1–C2), base étiquetée (C9–C11). Accès : session qui possède la clé (DE-8), allocation gratuite ou devis.

**§ 2. Moitiés.** Coupe aléatoire des revues en 𝒜 et ℬ, stratifiée par domaine, scellée avant la moisson. E₁ = paires internes à 𝒜 ; E₂ = paires internes à ℬ ; paires traversantes jamais construites.

**§ 3. Construction de la base** (session distincte, aveugle au profil) : protocole C0 à C12. Quotas M₁, M₂, M₂ (S2). Cas tirés dans un ordre aléatoire parmi les paires signalées ; témoins tirés uniformément parmi les paires à risque de la même date (K = 5) ; file de lecture entrelacée.

**§ 4. Prédicteurs** (session distincte, sans étiquette) : S, C, Π (quatre variantes), D, P, PA pour **toutes** les paires à risque de toutes les dates, sur corpus amputé (GF3) et non amputé ; table scellée avant la jointure.

**§ 5. Jointure et analyse** (session d'analyse) : jointure par identifiants des deux tables scellées ; aucun paramètre modifié.

**§ 6. Ordre de lecture.**
1. Préconditions : kappa ≥ S1 ; M₂ prospective ≥ M_min et M₂ rétrodite ≥ M_min ; gardes vertes.
2. **E₁** : β₂ des quatre variantes ; choix par S16 ; variante choisie scellée (fichier et empreinte) **avant** toute lecture de E₂.
3. **E₂ rétrodite** : β₂⁻ et gain d'aire⁻ de la variante choisie.
4. **E₂ prospective** : β₂⁺, intervalle, gain d'aire⁺ ; règle de rétrodiction S5 ; critères de lecture.
5. Rapportés.

**§ 7. Graines (R9)** : `numpy.random.SeedSequence` (numpy ≥ 1.25), deux racines distinctes écrites au scellement — RACINE_CONSTRUCTION (enfants du protocole, C0.5) et RACINE_ANALYSE (enfants : `(1,)` plis de validation croisée, `(2,)` bootstrap par niches) ; consignées au manifeste de chaque session avec configuration, empreintes, versions, commit.

**§ 8. Taille et justification** : M₂ fixé par le calcul de puissance contre l'alternative de DE-4 (section « Taille de base »). Charge de lecture (calcul § 7) : de l'ordre de 2 lectures × (M / q + K × M × f × c) par portion, q, f, c SUPPOSÉS ; mesurés sur E₁ et rapportés avant E₂ ; si la charge réelle rend la base impossible dans le délai, arrêt et version nouvelle (jamais d'abaissement silencieux de M).

**§ 9. Temps et coût.** Processeur. OpenAlex : ordre de 1,8 million d'œuvres (SUPPOSÉ), à étaler dans l'allocation gratuite ou à soumettre en devis (protocole C0.3). Aucun calcul sur carte graphique. Lecteurs : DE-3.

## Critères de lecture gelés

Table appliquée dans l'ordre ; la première ligne vraie décide.

| # | Issue observée | Verdict |
|---|---|---|
| 0 | Une garde de la Liste d'arrêt a sonné, ou kappa < S1 après révision, ou M₂ (prospective ou rétrodite) < M_min | **non concluant** (cause nommée) |
| 1 | Déclencheur R4 (S15) non rendu | **non concluant** tant que l'audit n'est pas rendu |
| 2 | Règle de rétrodiction S5 vraie (β̂₂⁻ ≥ β̂₂⁺ / 2, β̂₂⁺ > 0) | **suspendu** : le profil n'est pas distingué d'une association statique (HR-3) ; aucune lecture de β₂⁺ comme prédiction |
| 3 | Borne basse à 90 % de β₂⁺ > 0, ligne 2 fausse | **H-E1 non réfutée** sur cette partition et ces dates ; le profil est admis comme hypothèse de travail du bras méta (toujours exploratoire) |
| 4 | Intervalle à 90 % de β₂⁺ contenu dans ± S6 | **réfuté** (aucun effet utile au-delà des témoins ; HR-1 ou HR-4) |
| 5 | Borne haute à 90 % de β₂⁺ < 0 | **réfuté, signe inverse** (HR-2) |
| 6 | Autre cas | **non concluant (puissance)** ; estimation et intervalle rapportés |

Lectures croisées (rapportées, sans changer le verdict) : ligne 3 avec duel perdu → « le profil ajoute à la distance sans la battre seul » ; ligne 3 et variante non amputée seule positive → réserve sur la dépendance à l'amputation ; ligne 3 et variante tierce niche négative → réserve sur l'étiquette.

**R4 — même audit dans les deux sens** (S15). Déclencheurs : rapport de cotes de Π ≥ 3 **ou** ≤ 1/3 ; aire de Π seul ≥ 0,85 **ou** ≤ 0,15 ; kappa ≥ 0,95 **ou** précision du filtre ≥ 0,9 ou ≤ 0,05 ; β₂⁻ et β₂⁺ égaux à 0,01 près ; plus de la moitié des ponts dans 5 revues ; plus de 80 % des ponts à une seule date. Audit : fuite temporelle (prédicteur recalculé sur base tronquée en t), fuite d'étiquette (accès de la session des prédicteurs), aveugle des paquets, amputation, doublons ; rendu par un sous-agent neuf, scellé, avant tout verdict.

**Verdict prononcé par un sous-agent neuf** (ni auteur du préenregistrement ni de l'analyse), qui applique cette table ; scellé ; soumis à Lazar.

## Liste d'arrêt

| Condition | Action |
|---|---|
| Lecture d'une donnée réelle (moisson, pont, liste de rapprochements) avant le scellement de ce texte | arrêt ; écart consigné (R1) ; base reconstruite par une autre session |
| Préenregistrement, protocole, L_S, listes fermées ou gabarit des paquets d'empreinte fausse | arrêt avant la première requête |
| Clé d'OpenAlex imprimée ou écrite | arrêt ; clé à renouveler par Lazar |
| Estimation de coût d'OpenAlex au-delà de l'allocation gratuite ; tout appel payant (modèle, machine) | arrêt ; devis et GO |
| Moisson incomplète (G-C4) ; deuxième extraction mêlée à la première | arrêt de la revue ; reprise complète (R12) |
| Fuite temporelle : terme, prédicteur ou ensemble à risque qui lit une œuvre ≥ début de fenêtre | arrêt ; code refusé |
| Session de construction qui calcule ou lit un prédicteur ; session des prédicteurs qui lit une étiquette | arrêt ; base ou table refaite par une autre session ; audit R4 |
| Paquet de lecture qui contient un champ interdit (G-C5) ; file non entrelacée (G-C7) | arrêt de la lecture ; paquets refaits |
| Kappa < S1 après une révision | arrêt : non concluant (étiquette non fiable) |
| Quota non atteint, file épuisée | portion close ; M_min décide (ligne 0) |
| Paramètre modifié après lecture d'une étiquette ou d'un prédicteur joint | arrêt ; écart consigné |
| Variante choisie autrement que par S16, ou après lecture de E₂ | arrêt ; verdict non concluant |
| Niche, paire ou année d'événement prospectif commune à E₁ et E₂ | arrêt (GF5) |
| `except` qui rend une valeur par défaut ; numpy < 1.25 ; graine hors racine | arrêt (R5, R9) |
| Variance robuste non positive | repli sur le bootstrap par niches, consigné (jamais silencieux) |
| Déclencheur R4 | audit ; ligne 1 |

**Gardes testées sur un cas sain et sur un artefact (R5)**, sur base jouet synthétique, avant toute requête : les quatorze gardes de construction G-C1 à G-C14 (protocole C10), plus :
- **G-A1 prédicteurs sans futur** : prédicteurs recalculés sur la base tronquée en t identiques (sain) ; prédicteur qui lit une citation de l'année t : écart détecté (artefact) ;
- **G-A2 amputation** : une œuvre qui contient un terme caractéristique de j est absente du corpus de (i, j) (sain) ; amputation désactivée en principal : refusée (artefact) ;
- **G-A3 erreur type à deux voies** : base jouet à corrélation de niche connue, erreur type égale au calcul à la main (sain) ; erreur type naïve à la place : plus petite, détectée (artefact) ;
- **G-A4 règle de rétrodiction** : base jouet où le profil n'agit que sur le futur : pas de suspension (sain) ; même base où l'issue rétrodite est recopiée de l'issue prospective : suspension (artefact) ;
- **G-A5 choix de variante** : choix par S16 sur une table jouet égal au calcul à la main (sain) ; fonction qui lit E₂ : refusée (artefact) ;
- **G-A6 étanchéité des sessions** : l'arbre de travail de la session des prédicteurs ne contient aucun fichier d'étiquette (sain) ; présence du fichier : refus de démarrer (artefact) ;
- **G-A7 calcul de puissance rejoué** : sortie identique à l'octet (sain) ; racine changée : sortie différente, détectée (artefact).

## Dépendances

- **Dp-1 accès à OpenAlex** : une session qui possède `OPENALEX_API_KEY` (R-849 la signale dans l'environnement de session-depot) ; allocation gratuite épuisée par la moisson de R-863 ce jour-là, à surveiller ; option b de DE-1 : accès aux métadonnées d'arXiv (refusé par le mandataire dans un environnement, R-625).
- **Dp-2 lecteurs** (DE-3) ; troisième lecteur d'audit.
- **Dp-3 lexique L_S** : liste fermée d'objets mathématiques et de méthodes, construite **sans aucune donnée** (par exemple à partir des intitulés de la classification des sujets mathématiques de 2020, filtrés par une règle écrite), par un sous-agent neuf, contre-lue, scellée avant ce préenregistrement. Pas encore écrite.
- **Dp-4 listes fermées** : mots vides, formules génériques ; scellées avant.
- **Dp-5 gabarit des paquets et consigne des lecteurs** : scellés avant.
- **Dp-6 quarantaine** : trois sessions distinctes (construction, prédicteurs, analyse), étanchéité éprouvée (G-A6) ; la moisson OpenAlex de R-863 (`donnees/moisson-openalex-v1/`) **n'est pas réutilisée** (autre requête, autre but ; l'auteur ne l'a pas lue).
- **Dp-7 code** : construction, prédicteurs, analyse, gardes ; commit inscrit avant scellement.
- **Dp-8 temps** : charge de lecture (calcul § 7) ; la base n'est pas sur le chemin de la porte G0.

## Réserves de l'auteur

- Le modèle génératif du calcul de puissance est SUPPOSÉ de bout en bout (corrélations, effets, propension de niche, taux de base) ; seule sa structure (plan cas-témoins, erreur type à deux voies, règles comparées) est opposable. Le vrai taux de base des ponts validés est inconnu : la disponibilité de M ponts dans une moitié (calcul § 6) est le premier risque.
- Le filtre de termes caractéristiques est mécaniquement lié à la distance (plus deux revues sont loin, plus les termes de i sont nouveaux pour j) : cela favorise le témoin « distance », non le profil ; rapporté.
- L'étiquette mesure une reprise **textuelle** validée, non un rapprochement durable des communautés ; la validité de construit n'a pas de vérité extérieure.
- Une paire à structure commune peut rendre une reprise plus facile à reconnaître par les lecteurs (lien relevé par la contre-lecture de l'annexe, CA1-08, dans un autre cadre) ; les lecteurs ne voient pas la structure, mais le risque n'est pas nul.
- La règle principale, telle que simulée, est un peu anti-conservatrice (fausse alarme 0,060 à 0,080 au lieu de 0,05 pour M ≥ 100) ; la cause n'est pas établie (erreur type robuste à deux voies avec 150 grappes, propension de niche omise du modèle ajusté : hypothèses de l'auteur). La correction (S4) n'est pas encore écrite ni éprouvée.
- Le calcul ne simule ni le choix de variante sur E₁ (il suppose la variante juste), ni l'amputation, ni la dépendance du filtre à la distance.
- L'auteur est de la lignée conv-audit, comme les pièces du bras méta ; la contre-lecture doit venir d'un modèle autre qu'Opus.

## Contre-lecture

- **Contre-lecture 1** — À REMPLIR — par un sous-agent neuf **d'un modèle autre qu'Opus** (Sonnet 5.5 de préférence ; Fable 5.1 a écrit la synthèse v2 de la question 6 : réserve d'indépendance), non-auteur de ce brouillon, du protocole, du calcul et des pièces du bras méta. Fichiers à lui donner explicitement : ce brouillon ; le protocole ; le script et sa sortie (à rejouer deux fois à l'octet avec `python3 -I` depuis un dossier vide) ; la synthèse v2 du lot bisociation (§ A, § (iii), § (iv)) ; les lignes R-878 et R-884 de `registres/decisions.md` de main ; le préenregistrement Gu-Krenn v2 ; le brouillon 4 du semi-réel (section des six garde-fous) ; R-638, R-672, l'annexe du bras méta et sa contre-lecture ; le gabarit et `src/controle_ia/prereg.py` ; rien de `donnees/`. Points à attaquer : (1) l'étiquette est-elle vraiment indépendante du canal et de la structure, ou le filtre de termes la relie-t-il mécaniquement à S ou à D ? (2) la règle de rétrodiction (c) est-elle un écart acceptable à la lettre de la synthèse ? (3) l'amputation retire-t-elle trop (ou pas assez) ? (4) le modèle génératif du calcul est-il trop favorable ? (5) le choix des revues comme niches ; (6) la charge de lecture est-elle tenable ? Entrée à écrire ensuite : identifiant du sous-agent, empreinte du brouillon relu, chemin et empreinte de son rapport, traitement de chaque remarque (accepté, refusé et pourquoi).
