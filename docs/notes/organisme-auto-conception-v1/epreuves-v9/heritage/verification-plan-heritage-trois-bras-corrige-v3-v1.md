# Vérification de la version 3 du plan à trois bras corrigé de l'héritage et de son devis — v1

## En-tête

- **Vérificateur** : modèle O, auteur de la vérification de la version 2 (`verification-plan-heritage-trois-bras-corrige-v2-v1.md`, `792d5f394d032327e26ad8f940ebc1fd36c0b703971f9294b2eaa2bfe6c91e9f`), relue en entier, et de la contre-lecture de la version 1. Il n'a écrit ni le plan, ni le devis, ni leur programme de calcul. Rédacteur des pièces vérifiées : modèle F.
- **Objet** : les seuls neuf constats de la vérification de la version 2, et le différentiel v2 → v3, pour dire si un autre changement demande une contre-lecture complète.
- **Heures** (`date -u`) : début de lecture 2026-11-19T13:54:39Z ; début d'écriture 2026-11-19T13:56:20Z.
- **Commits lus** : branche `lot/compte-organisme-v1` à `15de5fbbca620594824326adcbd3a17335f6b196` (tête locale égale à la tête distante ; la version 3 y est versée par `c3b777540a7c3f2d997d4caad61f323cb320ca2b`) ; `main` lu à `18936bdb1ded4031439087de80d0ad6583f94b82`.
- **Empreintes vérifiées** (contenu lu, et compagnon `.sha256` quand il existe ; toutes conformes) :
  - `plan-heritage-trois-bras-corrige-v3.md` : `ad1226f6954f7af7c29759ce2f459a1753e65ba38fd8b1f75c56eb3281f400ee` ;
  - `devis-heritage-trois-bras-v3.md` : `d58584273bf6ea8cd0b5128452aac67dc96219d208cdaaf51949a919774d807c` ;
  - inchangés, contre leur compagnon : plan v2 (`ae819696…`), devis v2 (`988da4d1…`), plan v1, devis v1, `calcul_devis_heritage_v2.py` (`5d21b393f03f3e859241d97dea8347937596422c42f6b9f3cc4e5f5661b1a1c9`), `calcul-devis-heritage-v2.json` (`132a07649dd6d572ad50e5bc6c41a73fee9d54a8bcceef996192fb886b1dca6b`), contre-lecture v1 (`124767e4…`) ;
  - ordre de passage version 3 (`docs/notes/organisme-auto-conception-v1/epreuves-v9/ordre-de-passage-epreuves-v9-v3.md`, sur la branche) : `b19f550b525fe5696321167bd43a35fa5ece180fd2f97dad5dfc6e970a8c0f67`, conforme au plan ;
  - manifeste de fin du lanceur de la course v9 (`runs/20261119-094145-course-auto-conception-v9/manifeste-lanceur-fin.json`) : `28bc36df390d8481fb5bd9118cf764843ffea60856412d825ecbf08e7cee5be7`, conforme au devis.
- **Autres lectures** : `registres/go.md` sur `main` (`cbc3acd63edd04620713d8d19755c228e083201b210083133fb88eca62d0d90b` ; `main` a avancé depuis la lecture du rédacteur), lignes `GO-2026-11-19-55`, `-60` et `-67` ; du manifeste de fin, les seuls champs `cout_reel.par_role_usd` et `cout_reel.appels_par_role`, lus par programme pour vérifier la numérotation des espèces sans l'écrire.
- **Différentiel** : `git diff --no-index` du plan et du devis, v2 contre v3, mot à mot, lu en entier.
- **Recherche « Ne pas écrire » refaite** avec mon programme de la vérification précédente, hors du dépôt (il contient les formules), sur les deux textes de la v3 et, pour comparaison, de la v2.
- **Cartes** : aucune ouverte. **Non lus** : le code de l'organisme ; tout dossier interdit par le mandat.
- Aucun appel à un fournisseur de modèles, aucune dépense, aucun refus d'outil.

## Table des neuf constats

| n° | gravité | constat | appliqué | où, et remarque |
|---|---|---|---|---|
| 1 | B | tranche d'épreuve non dite cachée au proposeur | **oui** | § 3.0, ligne « données » : jamais servie au proposeur, d'aucune génération, dans aucun bras ; « part servie » nommée ; raison dite ; garde sur cas sain et artefact (une ligne de la tranche dans ce qui est servi arrête la génération). § 6 : le proposeur de la génération finale ne voit que la part servie. § 7 : l'exécuteur simulé tient la même séparation, monde final compris ; point 5 l'éprouve |
| 2 | M | l'expérimentateur, modèle qui écrit le script, absent de l'invariant et de la garde | **oui** | § 3.0 : deux acteurs, l'expérimentateur nommé, ni juge ni proposeur, même modèle, même consigne, même plafond dans les trois bras ; ligne neuve « ce que l'expérimentateur reçoit » (engagement scellé entre balises de donnée, part de données gelée ; jamais justification, prédiction, registre ni retour) ; garde d'entrée sur cas sain et artefact. § 3.1 : entrées de la fonction, invariant et essai le nomment. § 1 : ligne de c.8 complétée. § 7 : taux d'échec de l'expérimentateur nommé, gelé, le même dans les trois bras ; nommé au préenregistrement de l'étage sur processeur. Question 8 restée ouverte. Une précision de forme : constat neuf 1 |
| 3 | M | test de mort sur le monde final, contradiction avec le § 3.0 ; asymétrie | **oui** | § 3.0 : exception écrite. § 6 : mécanique (après la génération finale, mesure seulement, tranche d'épreuve du monde final de même proportion, graine par source commune aux trois bras, jamais servie, rien écrit ni rendu). § 2, règle 4 : paiement hors du budget égal, à l'identique, recommandé et à geler. Devis § 6, point 1 : déjà compté par la sensibilité sur 349 générations de bras, finales comprises (exact). Asymétrie dite ; lois fausses engagées et lois vraies engagées et tenues rapportées sans seuil (§ 6, § 8.3). Une ligne non reprise : constat neuf 2 |
| 4 | m | lecture des lignes 55 et 60 | **oui** | En-tête du plan et du devis : « la préparation reste sans dépense (ligne 55) ». La question 4 redevient nœud (§ 12 ; devis § 8 « nœud ouvert », § 9 « cinq nœuds »). La v3 ne garde pas la formule « sous réserve de la question 9 » : elle rapporte comme fait transmis par le mandat que la ligne 60 s'applique à l'héritage, et dit à la réserve 10 qu'elle ne l'a pas lu au registre. **Constaté** : sur `main`, la ligne `GO-2026-11-19-60` vise le critère de coût des cartes et ne nomme pas l'héritage ; la ligne `GO-2026-11-19-67` nomme l'héritage parmi les devis présentés tôt. La réserve 10 est donc exacte ; voir le verdict |
| 5 | m | règle 6, deux définitions du retrait | **oui** | § 2, règle 6 : une seule définition (retrait un à un dans l'ordre de la permutation semée jusqu'à ce que le coût prévu tienne ; arrêt au premier appel qui suffit) ; l'ancienne formule dite retirée. Devis § 2 bis : ordre de grandeur à coût d'appel uniforme, dit |
| 6 | m | table des issues, deux trous | **oui** | § 7 : grille à part des sources à dose nulle (5 à 16, proposée) ; maximum de la grille étendue (48, proposé, sans appui mesuré, réserve 11) ; « non lisible » prononçable ; C3 et C4 portés sur la grille à dose nulle, C1 sur celle à dose non nulle ; le suiveur de forme et le généraliste paient leur lecture ; § 8.0 borné au même maximum |
| 7 | m | formule de majoration | **oui** | § 8.0 : entier supérieur de (nombre lu ÷ (1 − part de différences nulles)) ; cas « part égale à un » dit ; réserve 6 complétée (trois sources, variances, khi-deux) |
| 8 | m | signe de la table de lecture ; non éprouvée faute de budget | **oui** | § 8.3 : signe de la somme des rangs signés de Pratt, médiane rapportée à côté, égalité rapportée telle quelle. § 3.0 : statut « non éprouvée (budget) », hors classe d'issue, non gardée, hors du score de justesse et du taux de base, dit tel quel dans le retour ; repris au § 1, § 2 (règle 3) et § 3.2, nombre rapporté par bras |
| 9 | m | citations de N-067, section 6 | **oui** | § 11 : obligatoires sans condition pour tout texte sortant tiré du plan qui décrit l'épreuve ; N-071, point 5, sous sa condition écrite ; § 3.0 renvoie |

**Les neuf constats sont appliqués fidèlement.**

## Le reste du différentiel

- **Plan** : tous les morceaux changés relèvent des neuf constats ou de l'en-tête, comme le disent le § 17 et le § 18. Les § 3.3, 4, 5, 9 et 10 sont inchangés à l'octet ; aucun chiffre du § 3.3 ne bouge. Le titre du § 12 et le point 5 du § 0 ne parlent plus de « la mère » : forme, sans effet. Les phrases sur la ligne 67 et sur le mot de Lazar sont ajoutées à l'en-tête, sans effet sur le dessin.
- **Devis** : aucun chiffre ne change ; le calcul de la v2 reste la source, sans version neuve, ce qui est permis puisque rien n'est recalculé. **Numérotation des espèces** : vérifiée par programme sur le manifeste de fin : cinq rôles de proposeur à onze appels, de coûts distincts 4,17, 4,75, 7,43, 17,58 et 24,72 USD, rangés par coût croissant ; les deux juges renvoient bien aux espèces 3 et 1 (6,86 et 2,41 USD) ; les compositions B (espèces 1, 2, 3) et C (espèces 1, 2) sont les mêmes qu'à la v2. Aucun nom d'espèce n'est écrit dans les deux textes ; les deux fichiers de calcul, déjà versés, gardent les noms de rôle, et le devis le dit.
- **Listes « Ne pas écrire »** : ma recherche rend sur la v3 les douze mêmes occurrences bénignes qu'à la v2 (sujets désignés au § 14, « aucune priorité » du § 10, « bras de diagnostic seulement », montant 72,50) ; les quatre occurrences d'identifiant de modèle du devis v2 ont disparu. Aucune formule interdite, aucun identifiant ni nom de famille de modèles.
- **Mot de Lazar** (« ce sont les essais avec experiences qui doivent trancher in fine les cartes et les tetss de mort ») : tenu dans les deux textes. Aucun critère, aucune garde, aucun champ, aucun chiffre ni aucune composition ne dépend du verdict d'un juge (N-058, erratum 1) ; ce qui tranche est l'épreuve exécutée et l'oracle du monde planté ; le lecteur témoin ne pèse pas.
- **Rien d'autre ne demande une contre-lecture complète** : aucune hypothèse, aucune revendication, aucun seuil ni aucun chiffre ne change hors des neuf constats.

## Constats neufs

Gravité : **m** = mineur, à reprendre au préenregistrement de l'étage sur processeur, sans version neuve du plan.

### 1. (m) L'engagement et la description de la tentative

Le champ `tentative` porte « l'engagement éprouvé […] et une description bornée » (§ 1). L'expérimentateur reçoit « l'engagement scellé » et sa garde arrête l'étage sur « un champ du registre autre que l'engagement » (§ 3.0). Il n'est pas dit si la description bornée lui est servie ; or il en a sans doute besoin pour écrire un script qui calcule ce que la loi affirme, et la garde doit savoir ce qu'elle refuse. **Correction** : au préenregistrement, nommer exactement ce que l'expérimentateur reçoit du champ `tentative` (l'engagement seul, ou l'engagement et la description bornée, entre balises de donnée), et éprouver la garde sur cette liste.

### 2. (m) Ligne « coût » du § 3.0

« Payé sur le budget du bras, dans les trois bras à l'identique » ne reprend pas l'exception écrite au § 2 (règle 4) et au § 6. **Correction** : ajouter « hors le test de mort de la génération finale, payé à part (§ 6) ».

### 3. (m) Deux renvois inexacts

- § 17, constat 4 : « devis, […] § 0 » ; le § 0 du devis n'a pas changé, et il n'en avait pas besoin.
- En-tête du plan et du devis : la ligne 67 est bien « lue sur `main` », mais l'ordre de passage version 3 qu'elle cite est sur la branche `lot/compte-organisme-v1` (`7e140479`), non sur `main` ; dire la branche à côté du chemin (règle R6).

### 4. (m) Activation du branchement, dite nœud par la ligne 67

La ligne `GO-2026-11-19-67` écrit que le branchement de la lecture entre générations et des tests de mort réels est écrit en parallèle, « éteint par défaut, son activation restant un nœud ». Le § 8.1, condition 2, demande ce branchement sans dire que son activation est un nœud de Lazar. **Correction** : l'ajouter à la condition 2 et à la question 1 du § 12.

## Verdict

Scellable.

Les neuf constats de la vérification de la version 2 sont appliqués fidèlement, sans dégât : la tranche d'épreuve n'est jamais servie au proposeur, avec sa garde et sa simulation ; l'expérimentateur est nommé, borné et pris dans l'invariant ; le test de mort sur le monde final est une exception écrite, à mécanique et paiement dits ; les six constats de forme sont fermés. Aucun chiffre ne change, la numérotation des espèces du devis est juste, les listes « Ne pas écrire » restent tenues, et le mot de Lazar et N-058 le sont aussi : aucun verdict de juge ne tranche. Rien d'autre n'a changé qui demande une contre-lecture complète. Les quatre constats neufs sont des précisions de forme, à reprendre au préenregistrement de l'étage sur processeur ; aucun ne demande une version 4. **Un point pour la mère, non pour le rédacteur** : que la ligne 60 s'applique à l'héritage n'est écrit à ce jour dans aucune ligne de `registres/go.md` sur `main` ; la v3 le rapporte comme fait transmis par son mandat et le dit (réserve 10) ; s'il vient d'un mot de Lazar, l'inscrire au registre. Les cinq nœuds du § 12 et la recommandation du devis restent à Lazar.
