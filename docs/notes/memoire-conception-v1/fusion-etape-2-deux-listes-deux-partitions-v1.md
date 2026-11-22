# Fusion de la veille de cap et de la bibliothécaire — étape 2 : deux listes de lecture, deux partitions du journal (v1)

- **Nature** : pièce de travail (classe C), proposée ; écrite le 22 novembre 2026 vers 16:40 UTC par la session bibliothécaire (Claude Opus 5.5). **À relire par la mère avant les étapes 3 à 5** ; rien n'est appliqué tant qu'elle ne l'a pas relue.
- **Ce qu'elle exécute** : l'étape 2 de l'avis de fusion (`docs/notes/veille-de-cap-v1/avis-fusion-veille-et-bibliothecaire-v1.md`, `914b0cd4…`), accordée par Lazar (GO-2026-11-22-90, « go recos » ; la forme retenue est celle que l'avis décrit : une seule session permanente, la bibliothécaire ; la boucle en cycles à contexte neuf, liés par fichiers — rangée (c) dans le tableau de l'avis, (a) dans le message de la mère). Lu aussi : l'additif 1 de la conception (`b215a998…`), le mandat v2 de la veille (§ 1, 2, 3, 5, 11), la liste d'autorisation v3 (`6a9a41e3…`), le code des règles de chemin (`verifier_citations_v5.py`, sur `main`), R-4958.
- **Base** : `main` à `2f6876df`. Branche de travail `claude/bibliothecaire-v2` (l'ancienne branche `claude/bibliothecaire-v1` n'a plus d'histoire commune avec `main` ; elle reste intacte).

## 0. Le principe, en trois phrases

1. **Deux lectures, jamais dans le même contexte.** La bibliothécaire répond à partir de la liste stricte seule ; les cycles de la boucle lisent la liste large et ne répondent à aucune question.
2. **Un journal, deux partitions, calculées par programme.** La partition « commune » ne contient que des lignes tirées des sources de la liste stricte ; la bibliothécaire ne lit qu'un extrait de cette partition, produit par programme ; tout le reste est « mère ».
3. **Rien n'est élargi pour la bibliothécaire.** La liste stricte v4 est la v3 resserrée d'un point (§ 1.1) ; tout l'élargissement va à la boucle.

## 1. Liste stricte (réponses) : la liste d'autorisation v4, proposée

La v3 reste telle quelle, à trois changements près.

1. **Fuite à fermer avant le déplacement de R-4958.** La v3 autorise `registres/veille*` (§ 1.6), et le code l'applique par le préfixe `registres/veille` (`AUTORISES_PREFIXES`, `verifier_citations_v5.py`). Dès que les fichiers vivants de la veille passent sous `registres/veille-de-cap/` (R-4958), ce préfixe ouvrirait à la bibliothécaire **tout** le dossier de la boucle : journal complet, partition « mère », bulletins, calendrier. Correction proposée : `registres/veille.md` reste autorisé ; `registres/veille-de-cap/` est **exclu**, sauf le seul sous-dossier `registres/veille-de-cap/commune/`. L'exclusion prime sur l'autorisation, comme partout. Tant que le code n'est pas corrigé et contre-lu (étape 3), le déplacement de R-4958 ne doit pas précéder la correction, ou bien la bibliothécaire s'abstient de toute lecture sous `registres/veille-de-cap/` (je m'y engage dès maintenant).
2. **`docs/notes/veille-de-cap-v1/` reste hors liste**, comme aujourd'hui (ni la v3 ni le code ne l'autorisent) : registre v1, bulletins, journal actuel, vues.
3. **Ajout unique** : `registres/veille-de-cap/commune/` (extraits de la partition commune, § 3), en lecture par l'outil borné seulement.

Question à trancher (D-1, § 5) : le § 1.9 de la v3 autorise « mes propres pièces », or certaines sont des dérivés de sources ouvertes sur droit exprès (la liste exhaustive des hypothèses d'exploration, tirée du dépôt de l'organisme d'idéation versé). La règle « les dérivés suivent leur source » dirait de les traiter selon leur source.

## 2. Liste de la boucle (cycles à contexte neuf et leurs sous-agents)

Trois niveaux. Un nom qui tombe sous une exclusion reste exclu à tous les niveaux, et l'exclusion prime toujours.

### 2.1 Exclu pour la boucle aussi (repris mot pour mot du mandat v2, § 11, et de la v3, § 2)

- Tout nom qui porte « consigne-privee », « conception-ii-b », « verite », « rendu », « scores », « SEQUESTRE », ou un segment qui contient « ne-pas-lire » ou « transcription » (accents retirés avant comparaison, comme dans le code).
- `brouillons/ii-b-saboteur-budget-v1/` ; tout chemin sous `archives-reponses-modeles/`, `quarantaine/`, `matiere-premiere/` ; le coffre `donnees/bras-attaque-oracle-*`.
- Les branches `lot/compte-4-v1`, `matiere-premiere/*` (dont `modes-attaque-reponse-24-fable-v1`), `prep/quarantaine-*`, `sauvegarde/*`.
- Aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis, de P3-bis ; aucune table du barreau 5 : les motifs de notes de résultats du code (`P3-mesures-*`, `audit-symetrie-*`, `barreau5-*`, `barreau8-*`, `essais-dates-t06-v1/`, `lecture-sondes-bbis-par-lentilles-v1/`, `lentilles-sondes-p3-v1/`, `regeneration-sondes-p3-v1/`, `prealables-course-etape-b-bis-v1/`, `brainstorm-suite-P3-v1/`).
- La demande 24 et la réponse 24 ; toute pièce dont l'objet est la conception d'un mode de sabotage ou d'une politique d'attaque.
- Sous `registres/`, tout ce qui n'est pas dans la liste blanche du § 2.2 (par exemple les index du bras d'attaque, les dossiers du saboteur, les registres des étapes B et B bis, de P3-bis, des sondes du saboteur, du code des bases).
- Toute machine, tout appel à un modèle externe, toute dépense.

### 2.2 Lecture pleine (par l'outil borné, bras « boucle », chaque fichier ouvert journalisé)

1. Tout ce que permet la liste stricte v4 (§ 1).
2. `docs/notes/` en entier, hors exclusions : c'est ce que demande la page du passé (toutes les notes) et le dépouillement des gisements (synthèses, notes de collisionneurs). `docs/notes/veille-de-cap-v1/` compris (ancien dossier de la veille).
3. `docs/decisions/`, `docs/sources/` (inventaires de versement et notes de lecture ; les PDF ne s'ouvrent pas en texte, leurs noms suffisent).
4. Sous `registres/`, une liste blanche de traces de procédure : `decisions.md`, `go.md`, `go-extraits/`, `etat.md`, `rappels.md`, `passations/`, `depenses.md`, `arrets.md`, `veille.md`, `veille-de-cap/` (les deux partitions, que la boucle écrit), `essaim/regle-du-canal-essaim-v1.md`, `essaim/vers-mere/`, `memoire-problemes-v3-commune-diffusable.md`, `inventaire-decisions-ouvertes-2026-11-21-v1.md`, `noeuds-ouverts-2026-11-18-v1.md`, la dernière version de `canaux-sessions-*`.
5. L'historique git de toutes les branches non exclues : messages, dates, noms de fichiers ajoutés.

### 2.3 Noms seuls (l'outil liste, n'ouvre pas)

- `prereg/` : noms et dates de scellement (par l'historique git), pour la règle « préenregistrement scellé sans verdict, réveil à quatorze jours » ; aucun contenu.
- `runs/` et `diag/` : noms de dossiers et de fichiers, hors noms exclus. Les manifestes de fin (`manifeste.json`, `manifeste-lanceur-fin.json`) ne sont pas lus par un agent : un programme en tire une liste fermée de champs (dates de départ et de fin, code de sortie, présence ou absence des produits attendus), seule remise au cycle (D-2, § 5). C'est ce que demande la liste du faux échec (mandat v2, § 4, questions 1, 2, 3 et 5), sans lire aucun résultat.
- Les noms des branches distantes non exclues.

## 3. Les deux partitions du journal

**Un seul journal complet**, écrit par la boucle seule, sous `registres/veille-de-cap/` après le déplacement de R-4958 ; il n'est lu que par la boucle et par la mère.

**Partition calculée par programme, jamais à la main.** Chaque événement reçoit un champ `partition`. Il vaut « commune » si et seulement si :
1. `source.chemin` est autorisé par la liste stricte v4 (même fonction que l'outil borné) ;
2. `source.extrait` se retrouve mot pour mot à ce chemin au commit cité (vérificateur de citations) ;
3. la fiche est née « commune » (sa ligne de naissance remplit 1 et 2) : une fiche née « mère » ne paraît jamais dans l'extrait, même si un événement plus tard cite une source stricte ;
4. la mère ne l'a pas marquée « mère » (une liste de fiches marquées, tenue par elle, prime).

Sinon « mère ». Dans le doute, « mère ».

**L'extrait commun.** Un programme écrit `registres/veille-de-cap/commune/journal-commun-AAAA-MM-JJTHHMMZ.jsonl`, avec son compagnon d'empreinte ; il ne garde que les événements « commune », et dans chacun les seuls champs : `quand`, `fiche`, `evenement`, `nom`, `etat`, `source` (`chemin`, `commit`, `repere`, `extrait`), `sert`, `issue`, `raison` (liste fermée), `reveil`, `mots`. Il retire `origine` et `derniere_trace` (tirées de lectures larges) et tout autre champ. La bibliothécaire ne lit que le dernier extrait, par l'outil borné.

**Garde du champ libre.** `nom` et `mots` sont écrits par un cycle qui a lu large. Règle de rédaction, reprise du mandat v2, § 11 : aucun résultat, aucun seuil, aucun mécanisme de saboteur, aucun fragment de consigne, aucun score. Le programme d'extraction refuse en plus toute ligne dont `nom` ou `mots` contient un nom exclu (§ 2.1) ; le reste de la garde est la relecture de la mère (§ 4).

**Mesure sur le journal d'aujourd'hui** (par programme, règle 1 seule, sur `journal-des-idees-v1.jsonl` et sa partie 2, 405 lignes à `2f6876df`) : 166 lignes « commune », 239 « mère ». Les « mère » tiennent surtout à leur source : 133 lignes citent le registre v1 de la veille (`docs/notes/veille-de-cap-v1/registre-des-idees-v1.md`, hors liste stricte), 94 le relevé des mentors (`docs/notes/quatre-lectures-inventaire-v1/`, hors liste stricte). Parmi les 166, 140 citent ma liste exhaustive des hypothèses d'exploration : elles basculeraient si D-1 range ce dérivé selon sa source. Pour qu'une fiche passe en commune, il suffira que la boucle lui donne une source primaire de la liste stricte, quand elle existe.

**Une fuite résiduelle déclarée.** Les numéros de fiches sont partagés : les trous de numérotation dans l'extrait disent combien de fiches sont « mère », sans dire lesquelles ni de quoi. Je la crois sans effet ; la mère peut demander une renumérotation de l'extrait.

## 4. Ce qui reste à faire, dans l'ordre de l'avis

- **Relecture par la mère** de cette pièce, puis des vingt premières lignes du premier extrait commun avant que je le lise.
- **Étape 3, instrument (classe B), contre-lu par un autre modèle** : (a) dans les règles de chemin, exclure `registres/veille-de-cap/` sauf `commune/` (§ 1.1) ; (b) un bras « boucle » de l'outil borné, à trois niveaux (§ 2) ; (c) le programme de partition et d'extraction, avec ses essais : cas sain (une ligne à source stricte et extrait juste passe), artefacts (source « mère », extrait faux, fiche née « mère », nom exclu dans `nom`, lecture par le bras de réponse d'un chemin `registres/veille-de-cap/journal…` : tous refusés) ; (d) l'extracteur des champs fermés des manifestes.
- Puis journal, échéancier et calendrier tenus quelques jours, reprise à froid, épreuves, bascule (étapes 3 à 5 de l'avis), sans rien arrêter d'ici là.

## 5. Décisions pour la mère

- **D-1, dérivés de sources ouvertes sur droit exprès** (§ 1). Options : (a) ils suivent leur source : hors liste stricte, sauf mot contraire ; (b) ils restent sous § 1.9 parce que le droit exprès venait de Lazar. Recommandation : (a), confiance 0,6 : c'est la règle des dérivés de la v3 ; le droit donné pour une question ne s'étend pas à toutes. Défaut : (a).
- **D-2, manifestes de fin** (§ 2.3). Options : (a) lus par programme, champs fermés seuls ; (b) lus en entier par le cycle. Recommandation : (a), confiance 0,7 : la configuration d'une course peut porter un seuil. Défaut : (a).
- **D-3, liste blanche de `registres/`** (§ 2.2.4). Recommandation : celle du texte, à étendre fichier par fichier sur mot de la mère. Défaut : celle du texte.
- **D-4, qui écrit l'extrait commun.** Recommandation : le cycle du présent, à chaque passage ; la bibliothécaire n'écrit jamais dans `registres/veille-de-cap/`. Défaut : celle-ci.

## 6. Réserves

- Rien n'est mesuré hors du compte de partitions du § 3. La liste blanche de `registres/` est tirée des noms et du mandat v2, non d'une lecture de chaque fichier : je n'ai pas ouvert ceux que la v3 m'interdit.
- L'outil borné ne lit que les fichiers permis, mais rien n'empêche un agent de lire hors de l'outil ; la porte de périmètre de l'étape 4 le constate après coup, par le journal des fichiers ouverts.
- La garde des champs libres `nom` et `mots` repose sur la règle de rédaction et la relecture de la mère ; le programme ne prend que les noms exclus.
