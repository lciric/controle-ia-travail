# Protocole de construction de la base de ponts d'E1′ (duel 1) — v1 — brouillon 1

**Statut : brouillon 1, non scellé ; contre-lecture par un modèle autre qu'Opus ; décisions de Lazar ; rien n'est collecté avant scellement.**

- Auteur : sous-agent neuf Opus 5.5 (`claude-opus-5-5`), lignée conv-audit, 31 octobre 2026 (relevé `date -u` : 11:07 UTC en cours de rédaction), sur le mot direct de Lazar (31 octobre 2026, 10:57 UTC) : « Lancer la base de ponts d'E1′ : processeur, sans dépense — go ».
- Pièce compagne : `prereg/brouillons/preenregistrement-E1-base-de-ponts-v1-brouillon1.md` (même date). Ce protocole est **la section exécutable** de son « Plan d'analyse », étapes C0 à C12 : en cas de divergence, le préenregistrement prime et la divergence est un écart (R1).
- Ce que l'auteur a fait : rien lu de réel. Aucune requête à OpenAlex, aucun fichier sous `donnees/`, aucune moisson, aucun pont, aucune liste de rapprochements datés. Le protocole est écrit **avant** toute collecte.
- Ce qu'il exige de la session qui l'appliquera : qu'elle soit **distincte** de la session qui calcule les prédicteurs et de celle qui analyse ; qu'elle **ne calcule ni ne voie jamais** le profil Π, la structure commune S, le canal C, la distance D, la popularité P ni l'attachement préférentiel PA d'aucune paire ; qu'elle ne commence qu'après le scellement du préenregistrement (empreinte citée au manifeste de construction).

## 0. Vocabulaire

- **Niche** : une revue (« source » de type revue dans OpenAlex) de l'échantillon scellé. Option retenue à titre de recommandation (décision DE-1 du préenregistrement) ; si Lazar choisit les catégories d'arXiv, les étapes C1 à C3 sont remplacées par l'annexe A, le reste est inchangé.
- **Paire** : deux niches distinctes de la même moitié, non ordonnées.
- **Date de coupure** t : le 1er janvier d'une année. Moitié E₁ : t ∈ {2009, 2011, 2013} ; moitié E₂ : t ∈ {2017, 2019, 2021} (seuil S9 du préenregistrement, à geler).
- **Fenêtre d'étiquette** w_lab = 4 ans ; **horizon** h = 3 ans (S7, S8, à geler).
- **Fenêtre d'événement** [a, b) : prospective [t, t + h) ; rétrodite [t − w_lab − h, t − w_lab).
- **Termes caractéristiques** T_i[a] : groupes de deux ou trois mots propres à la niche i, calculés sur [a − w_lab, a) seulement.
- **Candidat** : œuvre publiée dans j pendant [a, b) dont le titre ou le résumé contient au moins un terme de T_i[a] **absent de toutes les œuvres de j publiées avant a** (et symétriquement de j vers i).
- **Pont validé** (étiquette) : candidat lu « oui » par les deux lecteurs isolés. **Date du pont** = date de publication (`publication_date` d'OpenAlex) du premier candidat validé de la paire dans la fenêtre.
- **Lexique de structure** L_S : liste fermée d'objets mathématiques et de méthodes, scellée avant le préenregistrement (dépendance Dp-3). La construction ne s'en sert **que pour l'exclure** des termes caractéristiques (disjonction entre l'étiquette et la mesure de structure).

## C0. Préconditions (avant la première requête)

1. `sha256sum -c` sur le préenregistrement scellé, ce protocole scellé, L_S scellé, la liste fermée de mots vides et de formules génériques scellée (Dp-4), le gabarit des paquets de lecture scellé (C8). Toute empreinte fausse : arrêt.
2. Vérifier la présence de la clé d'interface d'OpenAlex **par son nom seulement** (`test -n "$OPENALEX_API_KEY"`) ; ne jamais l'imprimer. Absente : arrêt, demande à Lazar.
3. Relever le solde de l'allocation gratuite d'OpenAlex au début (en-têtes de réponse d'une requête minimale, ou page du compte si elle existe) ; estimer le coût de C3 (nombre de pages) ; **si l'estimation dépasse l'allocation gratuite cumulée sur la durée prévue, arrêt : nœud de dépense, devis à Lazar** (R-863 : la moisson de 197 681 œuvres a consommé 0,99 USD de crédits gratuits ; C3 porte sur 300 revues × 30 ans × environ 200 œuvres par an, soit de l'ordre de 1,8 million d'œuvres, 5 à 10 fois plus, SUPPOSÉ, à étaler sur plusieurs jours ou à soumettre en devis).
4. `numpy >= 1.25`, versions de toutes les bibliothèques consignées au manifeste de construction (`src/controle_ia/manifeste.py`).
5. Racine des graines : `numpy.random.SeedSequence(RACINE_CONSTRUCTION)`, entier écrit au préenregistrement scellé ; un enfant par tâche, clé de tâche écrite au manifeste (R9) : `(1,)` tirage des revues ; `(2,)` coupe en moitiés ; `(3,)` ordre de la file des cas ; `(4, d)` tirage des témoins à la date d ; `(5,)` entrelacement de la file de lecture ; `(6,)` lot d'étalonnage des lecteurs ; `(7,)` candidats lus d'un témoin plafonné.

## C1. Cadre des revues (règle scellée, appliquée sans voir aucune œuvre)

1. Requête unique sur les sources d'OpenAlex : `type = journal`, comptes par année (`counts_by_year`) disponibles. Enregistrer la réponse brute, son heure et son empreinte.
2. Règle d'activité (S10, S11) : au moins 60 œuvres par an chaque année de 1995 à 2024 (SUPPOSÉ ; recommandation). Si `counts_by_year` ne couvre pas toutes ces années (sa profondeur est SUPPOSÉ, non vérifiée), les comptes manquants viennent de requêtes de groupement par année filtrées sur la source. Cette règle lit des comptes de la source, jamais une œuvre. Conséquence déclarée : les revues fondées après 1995 sont exclues ; la nouveauté d'un terme (C6) n'est vérifiée qu'en remontant jusqu'à 1995.
3. Strates : domaine dominant de la source selon OpenAlex (quatre domaines) — **sert seulement à équilibrer le tirage**, jamais à définir une niche ni une paire.
4. Tirage de 300 revues (enfant `(1,)`), proportionnel à la taille des strates, en ordre aléatoire scellé ; liste d'attente : la suite de l'ordre.

## C2. Exclusion des revues pluridisciplinaires et coupe en moitiés

1. Deux lecteurs isolés (mêmes lecteurs que C8, consigne scellée) reçoivent le seul nom de chaque revue tirée et répondent « pluridisciplinaire : oui / non ». Une revue « oui » chez au moins un lecteur est remplacée par la suivante de la liste d'attente. Rapporter les remplacements.
2. Coupe en deux moitiés 𝒜 et ℬ de 150 revues, au hasard (enfant `(2,)`), stratifiée par domaine. Sceller la liste, l'ordre et la coupe **avant C3**. E₁ = paires internes à 𝒜 ; E₂ = paires internes à ℬ ; paires qui traversent : jamais construites.

## C3. Moisson (une seule extraction, figée)

1. Pour chaque revue : toutes les œuvres de `publication_date` du 1er janvier 1995 au 31 décembre 2024, tri `publication_date:asc` (leçon de R-863 : le tri par pertinence saute des œuvres), pagination par curseur. Champs : `id`, `doi`, `publication_date`, `publication_year`, `type`, `language`, `is_retracted`, `title`, `abstract_inverted_index`, `referenced_works`, `primary_location.source.id`, `updated_date`.
2. Journal de requêtes (adresse sans la clé, heure, statut, nombre de résultats annoncé, empreinte de la page) ; fichiers bruts compressés par revue ; empreinte de chacun.
3. Contrôle de complétude : somme des pages = nombre annoncé par la première page, à l'unité, par revue ; sinon reprise de la revue entière (jamais de recollage partiel), consignée.
4. Pas de deuxième extraction mêlée à la première. Une reprise complète crée une version nouvelle (R12). **Dérive d'OpenAlex** : la date d'extraction est la référence ; aucun complément ultérieur n'est fusionné.
5. Filtres scellés : `type` ∈ {article, review} ; `is_retracted` faux ; titre non vide. Une œuvre sans résumé reste dans la base (elle compte pour l'activité) mais ne peut être ni candidate ni contexte de terme ; part des œuvres sans résumé rapportée par revue et par année.
6. Règle de couverture (S12) : une revue dont la part d'œuvres avec résumé est inférieure à 0,5 sur une fenêtre de calcul est **inactive** pour les dates qui utilisent cette fenêtre. Règle appliquée par le code, résultat consigné, jamais ajusté à la main.

## C4. Texte normalisé

Titre + résumé reconstruit depuis l'index inversé ; minuscules ; normalisation Unicode NFKC ; découpage en mots par l'expression scellée `[a-z0-9]+(?:-[a-z0-9]+)*` ; suppression des mots vides (liste fermée scellée, Dp-4) ; groupes de deux et trois mots consécutifs. Œuvres non anglaises (`language` ≠ `en`) : exclues du texte, gardées pour l'activité.

## C5. Termes caractéristiques T_i[a]

Pour chaque niche i et chaque début de fenêtre a nécessaire (prospectif : a = t ; rétrodit : a = t − w_lab − h) :
1. Corpus de i sur [a − w_lab, a) ; fréquence documentaire f_i(g) de chaque groupe g ; même calcul sur toutes les niches de la **même moitié** (F(g)).
2. Retenus : f_i(g) ≥ max(5 œuvres ; 1 % des œuvres de i) ; spécificité f_i(g) / F(g) ≥ 10 × (taille de i / taille de la moitié) ; classés par f_i(g) × log(spécificité) ; les 200 premiers (S13).
3. Retirés : tout groupe qui contient un mot de L_S ou un groupe de L_S ; tout groupe de la liste scellée des formules génériques (« results show », « paper proposes »…).
4. Aucun calcul n'utilise une œuvre publiée à partir de a (garde G-C1).

## C6. Ensemble à risque et candidats

1. Une paire est **à risque** à la date t si ses deux niches sont actives sur [t − w_lab, t) (C3.6). Pour la fenêtre rétrodite, actives sur [t − 2w_lab − h, t − w_lab − h).
2. Candidats de (i → j) dans [a, b) : œuvres de j publiées dans [a, b) contenant au moins un groupe de T_i[a] absent de toutes les œuvres de j publiées avant a. Idem (j → i). Candidats de la paire = union. Consigner pour chaque candidat : œuvre, sens, groupes trouvés.
3. Paire **signalée** : au moins un candidat. Le signalement est une donnée de construction, non une étiquette.
4. Comptes rapportés par moitié et par date : paires à risque, paires signalées, candidats. **Jamais** croisés avec un prédicteur.

## C7. Files de lecture (cas et témoins), à l'aveugle

1. **File des cas**, par portion (E₁ prospective, E₂ prospective, E₂ rétrodite) : toutes les paires signalées de la portion, dans un ordre aléatoire scellé (enfant `(3,)`). Pour une paire, ses candidats sont lus **dans l'ordre chronologique** jusqu'au premier pont validé (C9) ; la paire devient un cas, de date celle de ce candidat ; sinon (tous lus, aucun validé) elle est « signalée non validée ».
2. **Témoins** : pour chaque cas de la date d, K = 5 paires tirées uniformément parmi les paires à risque de la même date et de la même portion (enfant `(4, d)`), sans remise. Témoin non signalé : non-pont sans lecture. Témoin signalé : ses candidats sont lus (au plus 20, tirés par l'enfant `(7,)` s'il en a plus ; le plafond est consigné) ; un candidat validé l'écarte des témoins (il est remplacé par le tirage suivant) et il est compté dans « ponts trouvés parmi les témoins ».
3. **Entrelacement** (enfant `(5,)`) : les candidats des cas et des témoins sont mêlés dans une seule file par lecteur ; le paquet de lecture ne dit jamais d'où vient l'œuvre (cas ou témoin, portion, date de coupure).
4. **Quotas** (S2, à geler d'après le calcul de puissance) : M₂ ponts validés en E₂ prospective ; M₂ en E₂ rétrodite ; M₁ = ⌈M₂ / 2⌉ en E₁ prospective. La lecture d'une portion s'arrête quand son quota est atteint **et** que les témoins de tous ses cas sont étiquetés. File épuisée avant le quota : la portion est close, son compte est consigné ; la règle M_min du préenregistrement décide.

## C8. Paquet de lecture et lecteurs

1. **Paquet** (gabarit scellé) : titre et résumé de l'œuvre ; nom de la revue où elle paraît (j) ; nom de la revue d'origine supposée (i) ; le ou les groupes de mots détectés ; trois titres de i (fenêtre [a − w_lab, a), tirés au hasard parmi ceux qui contiennent le groupe) pour donner le sens du terme dans i. **Rien d'autre** : aucun score, aucun compte de citations, aucune date de coupure, aucun statut cas ou témoin.
2. **Question scellée** : « Cette œuvre, publiée dans j, reprend-elle une méthode, un objet mathématique, un modèle ou un résultat propre à la communauté de i, et l'emploie-t-elle pour une question de j ? Répondre oui, non ou indécidable, puis une phrase de justification. Une simple coïncidence de mots, un usage générique ou un usage déjà courant dans j est « non ». »
3. **Lecteurs** : deux lecteurs isolés de familles différentes (décision DE-3 ; recommandation : deux sous-agents de session, un Sonnet 5.5 et un Fable 5.1, chacun dans un appel neuf, sans contexte partagé, sans accès au dépôt ni au réseau, recevant seulement des lots de paquets). Toute lecture par un modèle appelé par une interface payante est une **dépense** : nœud, devis et GO.
4. Lots de 50 paquets au plus par appel ; l'ordre des paquets dans un lot suit la file entrelacée ; chaque réponse est enregistrée avec l'identifiant du paquet, l'identifiant du lecteur, l'heure, l'empreinte du paquet.
5. Un lecteur ne voit jamais la réponse de l'autre.

## C9. Étalonnage, accord et règle d'étiquette

1. **Lot d'étalonnage** : 100 paquets tirés (enfant `(6,)`) parmi les candidats de la portion E₁ prospective, lus par les deux lecteurs avant tout le reste. Kappa de Cohen sur trois modalités (oui / non / indécidable) et sur deux (oui / autre).
2. Kappa à deux modalités ≥ S1 (recommandé 0,60) : on continue. Sinon : **une** révision de la consigne (version 2, scellée, motif écrit), nouveau lot de 100 paquets frais ; si encore sous S1 : **arrêt** (étiquette non fiable ; liste d'arrêt).
3. Kappa recalculé sur toute la base à la fin, par portion ; rapporté.
4. **Pont validé** = « oui » chez les deux lecteurs. « Oui » chez un seul : **contesté** — compte comme non-pont pour la règle principale ; variante de sensibilité où il compte comme pont. « Indécidable » chez les deux : non-pont, compté à part.
5. Lecture d'audit : 30 ponts validés et 30 candidats rejetés, tirés au hasard, relus par un troisième lecteur (humain si Lazar le veut ; sinon un troisième sous-agent d'une famille différente) ; accord rapporté, aucune correction de la base.

## C10. Gardes de construction (chacune testée sur un cas sain et sur un artefact, R5, avant C3)

| Garde | Cas sain | Artefact (doit être refusé) |
|---|---|---|
| G-C1 fuite temporelle des termes | T_i[a] identiques quand on retire de la base toutes les œuvres ≥ a | code qui lit une œuvre de l'année a : T_i[a] change, refus |
| G-C2 nouveauté | groupe présent dans j avant a : jamais candidat | groupe présent dans j avant a passé comme candidat : refus |
| G-C3 disjonction avec L_S | aucun groupe de T_i contient un mot de L_S | groupe contenant un mot de L_S injecté : refus |
| G-C4 complétude de la moisson | somme des pages = compte annoncé | une page retirée : écart détecté, reprise exigée |
| G-C5 aveugle des paquets | paquet conforme au gabarit | paquet qui contient un champ nommé score, citation, coupure, cas, témoin, S, C, D, P, PA ou Π : refus avant envoi |
| G-C6 aucun prédicteur | le code de construction n'importe aucun module de prédicteurs | import du module de prédicteurs : refus (balayage statique) |
| G-C7 entrelacement | file mêlée, test de séquences sur le statut caché non significatif | file triée cas puis témoins : détectée |
| G-C8 kappa | kappa sur table jouet = calcul à la main | fonction qui rend la part d'accord brute : refusée |
| G-C9 règle d'étiquette | (oui, oui) → pont ; (oui, non) → contesté | règle « au moins un oui » en principal : refusée |
| G-C10 témoins | témoins tirés à la même date, sans remise | témoin d'une autre date ou tiré deux fois : refus |
| G-C11 plafond | témoin à 35 candidats : 20 lus, plafond consigné | 35 lus sans consigne, ou choix non aléatoire : refus |
| G-C12 doublons | une œuvre présente dans deux revues (même DOI) : comptée une fois, signalée | doublon compté deux fois : détecté |
| G-C13 aucun repli silencieux | toute exception arrête la construction | `except` qui rend une valeur par défaut : balayage statique, refus |
| G-C14 clé | clé jamais imprimée ni écrite | journal qui contient la valeur de la clé : détecté par recherche de motif avant écriture, refus |

## C11. Ce qui est scellé, dans quel ordre (empreintes à produire, R6)

Chaque fichier reçoit un compagnon `.sha256` ; le manifeste de construction les liste tous avec leur empreinte, le commit du code de construction, les versions, les graines.

1. `cadre-revues-v1.json` (réponse brute des sources, heure) ; `revues-tirees-v1.tsv` (ordre, strate, remplacements) ; `moities-v1.tsv` — **avant C3**.
2. `moisson/<revue>.jsonl.gz` ; `journal-requetes-v1.jsonl` ; `complétude-v1.tsv` ; `manifeste-moisson-v1.json` — à la fin de C3, **avant C5**.
3. `termes-caracteristiques-v1.jsonl` (par niche et par a) ; `a-risque-v1.tsv` ; `candidats-v1.jsonl` ; `signalements-v1.tsv` — à la fin de C6, **avant toute lecture**.
4. `file-lecture-v1.jsonl` (ordre entrelacé, identifiants de paquets, empreintes des paquets) ; `consigne-lecteurs-v1.md` (et v2 si révisée) — avant C9.
5. `reponses-lecteur-A-v1.jsonl`, `reponses-lecteur-B-v1.jsonl` ; `etalonnage-v1.json` (kappa).
6. `base-ponts-E1-v1.tsv` : une ligne par (paire, date de coupure, portion) étiquetée — statut (cas, témoin, signalée non validée, contestée), date du pont, nombre de candidats lus, plafond. `audit-tiers-v1.json`.
7. `manifeste-construction-v1.json` scellé **en dernier** ; versé sur la branche de données `donnees/base-ponts-E1-v1` du dépôt de travail (jamais sur `lciric/controle-ia`).

## C12. Quarantaine et passage de relais

1. La session de construction remet : la moisson, les termes, les signalements et candidats (sans étiquette) à la **session des prédicteurs** ; la base étiquetée scellée à la **session d'analyse**, et à elle seule.
2. La session des prédicteurs calcule S, C, D, P, PA et Π pour **toutes** les paires à risque de toutes les dates (y compris celles qui ne seront jamais tirées), scelle sa table, puis seulement reçoit l'autorisation de jointure. Elle ne lit jamais `base-ponts-E1-v1.tsv` ni les réponses des lecteurs (garde : le fichier n'est pas dans son arbre de travail ; contrôle d'accès consigné).
3. La session d'analyse joint les deux tables scellées par identifiants, applique le plan d'analyse scellé, sans modifier aucun paramètre.
4. Chaque session écrit sa passation (R14) avec la liste des fichiers lus.

## Annexe A. Variante « catégories d'arXiv » (si DE-1 = option b)

C1–C3 deviennent : métadonnées d'arXiv (instantané public, versions datées) ; niche = catégorie principale choisie par l'auteur au dépôt ; date = date de la version 1 ; références et citations jointes par identifiant d'arXiv ou DOI dans OpenAlex (pour le canal seulement, jamais pour l'étiquette). Accès à vérifier : `arxiv.org` et `export.arxiv.org` ont été refusés par le mandataire d'un environnement (R-625) ; un autre chemin d'accès est une dépendance (Dp-1b).

## Dépendances

Dp-1 accès à OpenAlex par une session qui possède la clé (et, en option b, aux métadonnées d'arXiv) ; Dp-2 lecteurs (DE-3) ; Dp-3 lexique L_S scellé ; Dp-4 listes fermées (mots vides, formules génériques) scellées ; Dp-5 gabarit des paquets scellé ; Dp-6 trois sessions distinctes (construction, prédicteurs, analyse) ; Dp-7 temps de lecture (préenregistrement, Plan § 7 et sortie du calcul de puissance, § 7).
