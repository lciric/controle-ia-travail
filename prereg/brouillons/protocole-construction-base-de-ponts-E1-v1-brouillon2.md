# Protocole de construction de la base de ponts d'E1′ (duel 1) — v1 — brouillon 2

**Statut : brouillon 2, non scellé ; contre-lecture 2 à faire par un modèle autre qu'Opus ; décisions de Lazar ; rien n'est collecté avant scellement.**

- Rédacteur : sous-agent neuf Opus 5.5 (`claude-opus-5-5`), lignée conv-audit, branche locale `canal/conv-audit-n04` (HEAD `f260a66f`), 31 octobre 2026 (relevé `date -u` : 11:35 UTC au début de la rédaction). Le rédacteur n'a écrit aucune pièce du brouillon 1.
- Pièce compagne : `prereg/brouillons/preenregistrement-E1-base-de-ponts-v1-brouillon2.md`. Ce protocole est la section exécutable de son « Plan d'analyse » (étapes C0 à C12) ; en cas de divergence, le préenregistrement prime et la divergence est un écart (R1).
- Remplace, sans le modifier, `protocole-construction-base-de-ponts-E1-v1-brouillon1.md` (`60fa75472c7304754a3a6ecde590314d12973dfaf8a1c6ce4c90b65ba62f5592`). Constats traités : contre-lecture `contre-lecture-E1-base-de-ponts-v1-brouillon1.md` (`836b8c190e7fea6d469204ff7b4f0f307586591b0a896d1172cca8daae1f95eb`) ; la table de traitement est dans le préenregistrement.
- Ce que le rédacteur a fait : rien lu de réel. Aucune requête à OpenAlex, aucun fichier sous `donnees/`, aucune moisson, aucun pont, aucun `git fetch`. Les tailles de l'instantané d'OpenAlex viennent du manifeste versé sur `origin/main` (lu par `git show`, sans téléchargement).
- Ce qu'il exige de la session qui l'appliquera : qu'elle soit **distincte** de la session des prédicteurs et de celle d'analyse ; qu'elle **ne calcule ni ne voie jamais** Π, S, C, D, P ou PA d'aucune paire, et que son arbre de travail ne contienne **aucun** module, table ou sortie de prédicteurs (garde G-C15) ; qu'elle ne commence qu'après le scellement du préenregistrement et l'inscription du GO de la moisson (`registres/go.md`).

## Ce qui change par rapport au brouillon 1

| Point | Brouillon 1 | Brouillon 2 | Constat |
|---|---|---|---|
| Fenêtre rétrodite | [t − w_lab − h, t − w_lab) = [t − 7, t − 4) : recouvre d'un an le calcul du profil à w_s = 5 | [t − g − h, t − g) avec **g = max(w_s) = 5**, soit [t − 8, t − 5) ; garde G-C18 (même fonction que le § 0 du calcul) | CE1-01 |
| Historique de nouveauté | « avant a », jusqu'à 1995 (14 ans en prospectif, 6 en rétrodit) | **h_nov = 6 ans** pour toutes les portions | CE1-11 |
| Lexique de structure | retiré des termes caractéristiques | **autorisé** dans l'étiquette (disjonction par période, DE-9) ; part des ponts validés par un groupe qui touche L_S rapportée ; variante sans eux | CE1-03 |
| Domaines | quatre domaines d'OpenAlex | **sciences physiques** seulement si DE-10 = (a) | CE1-04 |
| Cadre des revues | activité ≥ 60 œuvres par an de 1995 à 2024 | activité **de 1995 à 2008 seulement** (aucune année postérieure à la première date de coupure), plafond de 2 000 œuvres par an ; à risque à chaque date sur le seul passé | CE1-13, CE1-07 |
| Taille | 300 revues | **500 revues** (250 par moitié) + deux paliers d'extension de 100 (50 par moitié), tirés et coupés d'avance | CE1-07 |
| Lecture | candidats des cas lus sans plafond ; témoins plafonnés à 20 | **plafond commun de 10** candidats par paire, cas et témoins ; échantillon aléatoire scellé, lu en ordre chronologique | CE1-06 |
| File | « file scellée » | **règle déterministe** scellée (blocs, tours, arrêt, remplacement) ; garde de rejeu G-C16 | CE1-12 |
| Date d'appariement | ambiguë (date du pont) | **date de coupure t** ; la date du pont n'intervient que dans la fenêtre d'événement | CE1-12 |
| Étalonnage | 100 paquets | **200 paquets**, kappa ponctuel et intervalle rapporté ; lot exclu des files | CE1-16 |
| Amputation | non opérationnalisée | étape **C5 bis** : termes, fenêtre, corpus ; D non amputé en principal | CE1-09 |
| Couverture des résumés | par fenêtre de calcul | aussi sur l'**historique de nouveauté** ; longueur moyenne des résumés transmise comme covariable | CE1-10 |
| Gardes | G-C1 à G-C14 | + G-C15 (arbre de construction), G-C16 (rejeu de file), G-C17 (plafond commun), G-C18 (fenêtres), G-C19 (dépense), G-C20 (activité sur le passé) ; G-C7 avec test et seuil écrits | CE1-14, CE1-20 |
| Moisson | API, « allocation gratuite ou devis » | devis séparé (`devis-moisson-openalex-E1-v1.md`) ; pilote de coût ; garde de dépense sur le champ `cost_usd` | CE1-07, R-729 |

## 0. Vocabulaire

- **Niche** : une revue (source de type `journal` dans OpenAlex) de l'échantillon scellé (DE-1 = (a)). Si DE-1 = (b), les étapes C1 à C3 sont remplacées par l'annexe A.
- **Paire** : deux niches distinctes de la même moitié, non ordonnées. **Unité** : (paire, date de coupure t, portion).
- **Date de coupure** t : 1er janvier. E₁ : t ∈ {2009, 2011, 2013} ; E₂ : t ∈ {2017, 2019, 2021} (S9).
- **Constantes** (à geler, S7, S8, S8 bis) : horizon h = 3 ; fenêtre des termes w_lab = 4 ; **décalage rétrodit g = 5** (= la plus longue fenêtre de calcul du profil, w_s ∈ {3, 5}) ; historique de nouveauté h_nov = 6.
- **Fenêtres d'une date t** (années civiles, [début, fin)) :

| Fenêtre | Prospective | Rétrodite |
|---|---|---|
| événement [a, b) | [t, t + 3) | [t − 8, t − 5) |
| termes caractéristiques T_i[a] | [t − 4, t) | [t − 12, t − 8) |
| historique de nouveauté | [t − 6, t) | [t − 14, t − 8) |
| calcul du profil (session des prédicteurs, pour mémoire) | [t − w_s, t), w_s ∈ {3, 5} | même profil, calculé en t |

  Exemples : t = 2009 → événement rétrodit [2001, 2004), profil [2004, 2009) ; t = 2021 → événement prospectif [2021, 2024), rétrodit [2013, 2016). Moisson nécessaire : années de publication 1995 à 2023. Les années d'événement prospectif de E₁ ([2009, 2016)) et de E₂ ([2017, 2024)) sont disjointes (GF5).
- **Candidat** (i → j) d'une fenêtre d'événement [a, b) : œuvre de j publiée dans [a, b) dont le titre ou le résumé contient au moins un groupe de T_i[a] **absent de toutes les œuvres de j de l'historique de nouveauté** [a − 6, a). Symétriquement (j → i). Candidats de la paire = union.
- **Pont validé** : candidat lu « oui » par les deux lecteurs isolés. **Date du pont** = `publication_date` du premier candidat validé parmi ceux qui ont été lus (rapportée ; elle n'apparie rien).
- **Lexique de structure** L_S : liste fermée d'objets mathématiques et de méthodes (Dp-3), scellée avant le préenregistrement. Si DE-9 = (b) (recommandé), la construction ne s'en sert **que pour marquer** les candidats dont un groupe touche L_S (variante rapportée) ; si DE-9 = (a), elle les exclut (règle du brouillon 1).

## C0. Préconditions (avant la première requête)

1. `sha256sum -c` sur : préenregistrement scellé ; ce protocole scellé ; L_S ; listes fermées de mots vides et de formules génériques (Dp-4) ; gabarit des paquets et consigne des lecteurs (Dp-5) ; devis de la moisson et ligne de GO correspondante. Toute empreinte fausse : arrêt.
2. Clé d'OpenAlex vérifiée par son nom seulement (`test -n "$OPENALEX_API_KEY"`), jamais imprimée. Absente : arrêt, demande à Lazar.
3. **Coût.** (a) Les comptes par revue et par année issus de C1 donnent, avant toute moisson, le nombre exact de pages de C3 (somme des ⌈n/100⌉ par revue et par tranche de pagination) ; (b) **pilote** : moisson complète de la première revue de l'ordre tiré, coût lu dans le champ `meta.cost_usd` de chaque réponse ; (c) projection = pages × coût mesuré par page ; **si la projection dépasse le plafond du GO, arrêt** et devis nouveau. Pendant C3, la garde G-C19 additionne `cost_usd` et arrête à 95 % du plafond.
4. `numpy >= 1.25` ; versions consignées au manifeste de construction (`src/controle_ia/manifeste.py`).
5. Graines : `numpy.random.SeedSequence(RACINE_CONSTRUCTION)`, entier écrit au préenregistrement scellé ; enfants : `(1,)` ordre des revues candidates ; `(2,)` coupe en moitiés ; `(3, portion, palier)` ordre de la file des cas ; `(4, portion, t)` tirage des témoins ; `(5,)` entrelacement ; `(6,)` lot d'étalonnage ; `(7, portion, t, paire)` candidats retenus sous le plafond ; `(8,)` lot du test de masquage ; `(9,)` lot d'audit.

## C1. Cadre des revues (règle scellée, appliquée sans voir aucune œuvre)

1. Liste des sources `type = journal` (requête de liste paginée, ou entité `sources` de l'instantané selon la voie du devis). Réponse brute, heure, empreinte.
2. **Périmètre** (DE-10) : si (a), domaine dominant de la source = sciences physiques selon OpenAlex. Le domaine sert seulement à restreindre et à stratifier, jamais à définir une niche ni une paire (réserve : le classement des sources d'OpenAlex est postérieur aux dates ; il ne sert qu'au cadre).
3. Préfiltre sur le compte total d'œuvres de la source (≥ 14 × 60 = 840) ; candidates mises dans un **ordre aléatoire scellé** (enfant `(1,)`), stratifié par sous-domaine.
4. **Activité** (S11), contrôlée dans l'ordre par une requête de groupement par année par revue (`group_by=publication_year`, `type` ∈ {article, review}) : au moins 60 et au plus 2 000 œuvres chaque année de **1995 à 2008**. Aucune année postérieure à 2008 n'est lue à cette étape (garde G-C20). On s'arrête à **700 revues acceptées** (500 + deux paliers de 100). Conséquence déclarée : revues fondées après 1995 et très grandes revues exclues ; aucune condition de survie après 2008.
5. Les comptes par année de 1995 à 2023 des 700 revues retenues sont alors relevés (une requête de groupement par revue) : ils servent au seul calcul du coût (C0.3) et aux contrôles de complétude (C3.3), jamais à une règle de sélection.

## C2. Exclusion des revues pluridisciplinaires, paliers et coupe en moitiés

1. Deux lecteurs isolés (mêmes familles que C8, consigne scellée) reçoivent le seul nom de chaque revue acceptée ; « pluridisciplinaire : oui » chez au moins un lecteur → remplacée par la suivante de l'ordre (C1.4). Remplacements rapportés.
2. **Paliers** : les 500 premières revues de l'ordre = palier 1 ; les 100 suivantes = palier 2 ; les 100 suivantes = palier 3.
3. **Coupe** en 𝒜 et ℬ (enfant `(2,)`), stratifiée par sous-domaine et **par palier** (250 + 50 + 50 par moitié). Liste, ordre, paliers et coupe scellés **avant C3**. E₁ = paires internes à 𝒜 ; E₂ = paires internes à ℬ ; paires traversantes jamais construites.

## C3. Moisson (une seule extraction, figée)

1. Pour chacune des 700 revues : toutes les œuvres de `publication_date` du 1er janvier 1995 au 31 décembre 2023, tri `publication_date:asc`, pagination par curseur, `per_page=100`. Champs (`select`) : `id`, `doi`, `publication_date`, `publication_year`, `type`, `language`, `is_retracted`, `title`, `abstract_inverted_index`, `referenced_works`, `primary_location`, `updated_date`.
2. Journal de requêtes (adresse sans la clé, heure, statut, compte annoncé, `cost_usd`, empreinte de la page) ; fichiers bruts compressés par revue ; empreinte de chacun.
3. Complétude (G-C4) : somme des œuvres reçues = compte annoncé par la première page, à l'unité, par revue ; et écart au compte de C1.5 rapporté. Sinon reprise de la revue entière (jamais de recollage partiel), consignée.
4. Pas de deuxième extraction mêlée à la première ; une reprise complète crée une version nouvelle (R12). La date d'extraction est la référence (dérive d'OpenAlex) ; voie « instantané » : la date de version (`2026-10-14` ou suivante) et le manifeste en tiennent lieu.
5. Filtres scellés : `type` ∈ {article, review} ; `is_retracted` faux ; titre non vide ; doublons par DOI (G-C12). Œuvre sans résumé : gardée pour l'activité, jamais candidate ni contexte de terme.
6. **Couverture** (S12) : une revue est **inactive** pour une portion d'une date si sa part d'œuvres avec résumé est < 0,5 sur la fenêtre des termes, sur l'historique de nouveauté **ou** sur la fenêtre d'événement de cette portion. Règle appliquée par le code, jamais ajustée à la main. La part et la longueur moyenne des résumés (en groupes de mots) par revue et par fenêtre sont écrites dans `couverture-v1.tsv` (transmis à la session des prédicteurs comme covariables, CE1-10).

## C4. Texte normalisé

Titre + résumé reconstruit depuis l'index inversé ; minuscules ; Unicode NFKC ; découpage par l'expression scellée `[a-z0-9]+(?:-[a-z0-9]+)*` ; suppression des mots vides (liste scellée) ; groupes de deux et trois mots consécutifs. Œuvres `language` ≠ `en` : exclues du texte, gardées pour l'activité.

## C5. Termes caractéristiques T_i[a]

Pour chaque niche i et chaque début d'événement a (prospectif a = t ; rétrodit a = t − 8) :
1. Corpus de i sur [a − 4, a) ; fréquence documentaire f_i(g) ; même calcul sur toutes les niches **actives de la même moitié** (F(g)).
2. Retenus : f_i(g) ≥ max(5 œuvres ; 1 % des œuvres de i) ; spécificité f_i(g) / F(g) ≥ 10 × (taille de i / taille de la moitié) ; classement par f_i(g) × log(spécificité) ; les 200 premiers (S13).
3. Retirés : groupes de la liste scellée des formules génériques. Si DE-9 = (a) seulement : groupes qui contiennent un mot ou un groupe de L_S. Si DE-9 = (b) : ces groupes sont gardés et **marqués** `touche_LS`.
4. Aucun calcul n'utilise une œuvre publiée à partir de a (G-C1).

## C5 bis. Listes d'amputation (remises à la session des prédicteurs ; GF3, CE1-09)

La construction ne calcule aucun prédicteur ; elle remet la liste des œuvres à retirer. Pour une paire (i, j) et une date t :
- A_i|j(t) = œuvres de i publiées dans [t − 5, t) qui contiennent un groupe de **T_j[t] ∪ T_j[t − 8]** ; symétriquement A_j|i(t). L'union des deux ensembles de termes garantit que le même profil (calculé en t) sert aux deux portions et que l'empreinte des reprises de la fenêtre rétrodite est retirée aussi.
- Usage par la session des prédicteurs (écrit au préenregistrement) : S et C calculés sur les corpus amputés ; **D non amputé** en principal (témoin le plus dur) ; variantes rapportées : tout non amputé, D amputé.
- Fichier `amputation-v1.jsonl` : (i, j, t, liste d'identifiants d'œuvres, empreinte).

## C6. Ensemble à risque, candidats, signalements

1. Paire **à risque** pour la portion prospective de t : ses deux niches actives (C3.6) sur [t − 6, t). Pour la portion rétrodite de t : actives sur [t − 14, t − 8) et sur [t − 6, t) (le profil se calcule en t). Aucune activité n'est exigée pendant la fenêtre d'événement (sauf la couverture des résumés de C3.6, identique pour cas et témoins).
2. Candidats (i → j) et (j → i) selon le vocabulaire ; pour chaque candidat : œuvre, sens, groupes trouvés, marque `touche_LS`.
3. Paire **signalée** : au moins un candidat. Le signalement est une donnée de construction, non une étiquette.
4. Comptes rapportés par moitié, palier, date et portion : paires à risque, paires signalées, candidats par paire (distribution). **Jamais** croisés avec un prédicteur.

## C7. Lecture : règle déterministe scellée (pas une file figée ; CE1-06, CE1-12)

1. **Plafond commun** (S14) : pour toute paire lue — cas potentiel ou témoin —, au plus **10** candidats, tirés au hasard (enfant `(7, portion, t, paire)`) s'il y en a plus, puis lus dans l'ordre chronologique ; la lecture de la paire s'arrête au premier candidat « oui-oui ». Le nombre de candidats non lus est consigné.
2. **File des cas** d'une portion : paires signalées du palier 1, dans un ordre aléatoire scellé (enfant `(3, portion, 1)`), traitées par **blocs de 100 paires**. Dans un bloc, tours successifs : au tour k, chaque paire non résolue envoie son k-ième candidat. Après chaque bloc, compte des paires validées. La file s'arrête à la fin du bloc où le quota (S2) est atteint ; tous les validés de ce bloc sont des cas (M effectif ≥ quota). Date d'appariement d'un cas = sa **date de coupure t**.
3. **Extension** (CE1-07) : file du palier 1 épuisée avant le quota → paires signalées nouvelles du palier 2 (paires qui touchent une revue du palier 2 de la moitié), ordre `(3, portion, 2)`, puis palier 3. Au-delà, portion close, M_min décide. Toute extension est consignée ; l'analyse ajoute alors l'indicatrice « paire d'un palier d'extension » au modèle (écrit au préenregistrement).
4. **Témoins** : pour chaque cas de date t, K = 5 paires tirées uniformément, sans remise, parmi les paires à risque de la même portion et de la même date dans l'ensemble des paliers ouverts à ce moment (enfant `(4, portion, t)`). Témoin non signalé : non-pont sans lecture. Témoin signalé : lu sous le même plafond (C7.1) ; s'il est validé, il est remplacé par le tirage suivant et compté dans « ponts parmi les témoins ».
5. **Entrelacement** (enfant `(5,)`) : à chaque tour, les paquets des cas potentiels et des témoins, toutes portions confondues, sont mêlés dans des lots de 50 ; **les deux lecteurs reçoivent les mêmes paquets dans les mêmes lots**.
6. **Rejeu** (G-C16) : la suite des lots est une fonction déterministe des graines et des réponses ; rejouée à partir des réponses enregistrées, elle redonne la même suite à l'octet.
7. **Quotas** (S2) : M₂ en E₂ prospective, M₂ en E₂ rétrodite, M₁ en E₁ prospective. La lecture d'une portion s'arrête quand son quota est atteint et que ses témoins sont étiquetés.
8. **Plafond de lectures** (S17) : après E₁, la session mesure le rendement des paires signalées et les paquets lus par cas, et projette la charge de E₂ ; si la projection ou le compte courant dépasse le plafond, **arrêt** : version nouvelle (jamais d'abaissement silencieux de M).

## C8. Paquet de lecture et lecteurs

1. **Paquet** (gabarit scellé) : titre et résumé de l'œuvre ; nom de la revue où elle paraît (j) ; nom de la revue d'origine supposée (i) ; le ou les groupes détectés ; trois titres de i tirés dans [a − 4, a) parmi ceux qui contiennent le groupe. Rien d'autre : ni score, ni compte de citations, ni date de coupure, ni année de l'œuvre, ni statut, ni marque `touche_LS`.
2. **Question scellée** : « Cette œuvre, publiée dans j, reprend-elle une méthode, un objet mathématique, un modèle ou un résultat propre à la communauté de i, et l'emploie-t-elle pour une question de j ? Répondre oui, non ou indécidable, puis une phrase de justification. Une simple coïncidence de mots, un usage générique ou un usage déjà courant dans j est « non ». » (Avec DE-9 = (b), le filtre laisse passer les méthodes et objets nommés : la question et le filtre sont alignés.)
3. **Lecteurs** (DE-3) : deux sous-agents de familles différentes, appels neufs et isolés, sans accès au dépôt ni au réseau, recevant seulement des lots. Tout appel payant : nœud, devis, GO.
4. Chaque réponse est enregistrée avec l'identifiant du paquet, du lecteur, du lot, l'heure et l'empreinte du paquet. Un lecteur ne voit jamais la réponse de l'autre.
5. **Test de masquage** (CE1-19) : 30 paquets tirés (enfant `(8,)`) parmi ceux de l'étalonnage, relus par les deux lecteurs avec les noms de revues remplacés par « revue A » et « revue B » ; accord comparé à celui des mêmes paquets non masqués, rapporté.

## C9. Étalonnage, accord, étiquette, audit

1. **Lot d'étalonnage** : 200 paquets (enfant `(6,)`) parmi les candidats de E₁ prospective ; lus avant tout le reste ; les paires d'où ils viennent sont **retirées de toutes les files** (ni cas ni témoins).
2. Kappa de Cohen (oui contre autre) **ponctuel ≥ S1** (0,60) : on continue ; intervalle à 95 % (bootstrap sur les paquets), accord brut et accord positif rapportés. Sinon : une révision de consigne (version 2, scellée, motif écrit), nouveau lot de 200 ; encore sous S1 : arrêt.
3. Kappa recalculé par portion, par année de publication et par paire proche ou lointaine (selon un compte de termes partagés, jamais selon D) ; rapporté.
4. **Pont validé** = « oui » chez les deux. « Oui » chez un seul : contesté, non-pont en principal, pont dans une variante. « Indécidable » chez les deux : non-pont, compté à part.
5. **Audit** : 30 ponts validés et 30 candidats rejetés (enfant `(9,)`), relus par un troisième lecteur (humain si Lazar le veut) ; accord rapporté, aucune correction de la base.

## C10. Gardes de construction (chacune testée sur un cas sain et sur un artefact, R5, sur base jouet, avant C3)

| Garde | Cas sain | Artefact (doit être refusé) |
|---|---|---|
| G-C1 fuite temporelle des termes | T_i[a] identiques sans les œuvres ≥ a | code qui lit une œuvre de l'année a |
| G-C2 nouveauté | groupe présent dans j dans [a − 6, a) : jamais candidat | un tel groupe passé comme candidat |
| G-C3 lexique | DE-9 (b) : marque `touche_LS` exacte ; (a) : aucun groupe de L_S | marque absente, ou groupe de L_S gardé sous (a) |
| G-C4 complétude | somme des pages = compte annoncé | une page retirée : écart détecté, reprise exigée |
| G-C5 aveugle des paquets | paquet conforme au gabarit | champ score, citation, coupure, année, cas, témoin, S, C, D, P, PA, Π ou `touche_LS` |
| G-C6 aucun prédicteur | aucun import de module de prédicteurs | import présent (balayage statique) |
| G-C7 entrelacement | test des séquences de Wald et Wolfowitz sur le statut caché, p ≥ 0,01 | file triée cas puis témoins : p < 0,01, refus |
| G-C8 kappa | kappa jouet = calcul à la main | fonction qui rend l'accord brut |
| G-C9 règle d'étiquette | (oui, oui) → pont ; (oui, non) → contesté | « au moins un oui » en principal |
| G-C10 témoins | même portion, même date t, sans remise | autre date, ou tiré deux fois |
| G-C11 plafond | paire à 35 candidats : 10 tirés au hasard, plafond consigné | 35 lus, ou 10 premiers chronologiques |
| G-C12 doublons | même DOI dans deux revues : compté une fois, signalé | doublon compté deux fois |
| G-C13 aucun repli silencieux | toute exception arrête | `except` qui rend une valeur par défaut |
| G-C14 clé | clé jamais imprimée ni écrite | journal qui contient la valeur de la clé |
| G-C15 arbre de construction | arbre sans module, table ni sortie de prédicteurs : démarrage | une table de prédicteurs présente : refus de démarrer |
| G-C16 rejeu de la file | rejeu depuis les réponses : même suite de lots, octet pour octet | une réponse modifiée sans nouvelle version : suite différente, détectée |
| G-C17 plafond commun | même plafond appliqué aux cas et aux témoins | plafond levé pour les cas seulement |
| G-C18 fenêtres | g = 5, w_s ∈ {3, 5} : accepté | g = 4 avec w_s = 5 ; w_s = 6 ; date de E₂ dont l'événement recouvre E₁ : refusés (fonction du § 0 du calcul) |
| G-C19 dépense | somme des `cost_usd` < 95 % du plafond : continue | somme simulée ≥ 95 % : arrêt avant la requête suivante |
| G-C20 activité sur le passé | règle d'activité lit 1995–2008 seulement | règle qui lit un compte de 2009 ou après |

## C11. Ce qui est scellé, dans quel ordre (R6)

Chaque fichier reçoit un compagnon `.sha256` ; le manifeste de construction les liste tous avec le commit du code, les versions et les graines.

1. `cadre-revues-v1.json`, `revues-candidates-ordre-v1.tsv`, `activite-1995-2008-v1.tsv`, `revues-retenues-v1.tsv` (ordre, palier, sous-domaine, remplacements), `moities-v1.tsv`, `comptes-1995-2023-v1.tsv`, `projection-cout-v1.json` — **avant C3**.
2. `moisson/<revue>.jsonl.gz`, `journal-requetes-v1.jsonl`, `completude-v1.tsv`, `couverture-v1.tsv`, `manifeste-moisson-v1.json` — fin de C3, **avant C5**.
3. `termes-caracteristiques-v1.jsonl`, `amputation-v1.jsonl`, `a-risque-v1.tsv`, `candidats-v1.jsonl`, `signalements-v1.tsv` — fin de C6, **avant toute lecture**.
4. `regle-lecture-v1.json` (graines, tailles de bloc et de lot, plafonds), `consigne-lecteurs-v1.md` (et v2 si révisée) — avant C9.
5. `lots-v1.jsonl` (suite des lots, au fil de l'eau), `reponses-lecteur-A-v1.jsonl`, `reponses-lecteur-B-v1.jsonl`, `etalonnage-v1.json`, `masquage-v1.json`, `charge-E1-v1.json` (rendement et projection, C7.8).
6. `base-ponts-E1-v1.tsv` : une ligne par (paire, t, portion) étiquetée — statut, palier, date du pont, candidats lus et non lus, `touche_LS` du candidat validant ; `audit-tiers-v1.json`.
7. `manifeste-construction-v1.json` scellé **en dernier** ; versé sur la branche de données `donnees/base-ponts-E1-v1` du dépôt de travail (jamais sur `lciric/controle-ia`).

## C12. Quarantaine et passage de relais

1. La session de construction remet à la **session des prédicteurs** : la moisson, `couverture-v1.tsv`, les termes, `amputation-v1.jsonl`, `a-risque-v1.tsv` (sans étiquette). Les signalements et candidats ne lui sont **pas** remis (ils ne servent à aucun prédicteur ; écrit pour fermer CE1-14). Elle remet la base étiquetée scellée à la **session d'analyse**, et à elle seule.
2. La session des prédicteurs calcule S, C, D, P, PA, Π et les covariables de couverture pour **toutes** les paires à risque de toutes les dates et portions, scelle sa table, puis seulement reçoit l'autorisation de jointure. Son arbre ne contient jamais `base-ponts-E1-v1.tsv` ni les réponses (G-A6).
3. La session d'analyse joint les deux tables scellées par identifiants et applique le plan scellé sans modifier aucun paramètre.
4. Chaque session écrit sa passation (R14) avec la liste des fichiers lus.

## Annexe A. Variante « catégories d'arXiv » (si DE-1 = option b)

C1–C3 deviennent : métadonnées d'arXiv (versions datées) ; niche = catégorie principale choisie au dépôt ; date = version 1 ; références jointes par identifiant d'arXiv ou DOI dans OpenAlex (pour le canal seulement). Accès à vérifier (`arxiv.org` refusé par le mandataire d'un environnement, R-625).

## Dépendances

Dp-1 accès à OpenAlex (voie et plafond : devis, GO) ; Dp-2 lecteurs (DE-3) ; Dp-3 L_S scellé ; Dp-4 listes fermées ; Dp-5 gabarit et consigne ; Dp-6 trois sessions distinctes ; Dp-7 charge de lecture (calcul, § 6 ; plafond S17).
