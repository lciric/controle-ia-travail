# Mandat du rédacteur — critères de choix des cartes v4, programmes d'assemblage, de masque de style et de lecture par programme, note sur le juge v4 — v1

Pièce de travail (classe C). Donné par la session du compte organisme, le 2026-11-19 vers 15:08Z, sur le mot de Lazar : « reprends la file de conception dans l'ordre de la passation (…, critères v4 et note v4 du juge, …) ; rédaction par Fable 5.2, contre-lecture par Opus 5.5 ».

## Règle d'or

Les critères v4 et les programmes sont **scellés avant toute lecture de carte** de ce cycle. Tu n'ouvres aucune carte, aucun fichier de cartes, rien sous `archives-reponses-modeles/`. Tu peux lire les rejeux v2 et l'audit déjà versés ; déclare en tête ce que tu en as vu. Tu ne lis jamais l'espèce d'une carte, ni le champ `meta`.

## Ce que tu fais

1. **Critères v4** (`criteres-choix-cartes-v9-v4.md`) : les critères v3 (`1ce41903…`) restent scellés, non réécrits (R12) ; la v4 applique les huit constats de la contre-lecture `contre-lecture-criteres-v3-note-v3-v1.md` (`cce1a8f4…`) :
   - constat 1 : les deux gardes de l'échelle fine définies d'avance par une statistique et un seuil ; retour à Lazar avant adoption si l'audit de la règle R4 se déclenche, pour toute espèce et dans les deux sens ; l'option (iii) posée à Lazar comme option, non comme réglage ;
   - constat 2 : l'axe A dit « voisin » de la définition scellée de GO-2026-11-19-60 ;
   - constat 3 : la part de chaque voie dans chaque tiers de l'ordre de passage ;
   - constat 4 : tous les cas d'assemblage tranchés par écrit, dont le départage circulaire du porteur d'une fusion (permuter les cartes, non les lignes, ou autre règle non circulaire) ;
   - constats 5 et 6 : kappa rapporté à côté de l'accord brut ; clé 7 comptée ;
   - **consigne R-3876** : compter le nombre réel de cartes sauvées (lecteurs titulaires compris) et fixer une limite de veto qui tient au nombre visé ; **GO-2026-11-19-68** : comparer deux et trois vetos par juge, dire ce que la limite change ; **GO-2026-11-19-69** : le coût écrit à côté, n'élimine aucune carte, ne sert qu'à ordonner ; question neuve ≠ zéro.
2. **Recommandations de l'audit de symétrie** (`audit-symetrie-rejeu-v2-v1.md`, `ff814fc9…`), acceptées par la mère (R-3883) :
   - le critère D rétabli comme dans les critères v3 ;
   - **limite écrite en tête** : aucun lecteur d'une autre famille sans dépense ; le signal « famille des lecteurs » (11 sur 16 contre 1 sur 46) écrit en tête de tout assemblage qui emploie la v2 ;
   - un **lecteur par programme**, sans famille, scellé avant, avec un témoin pour le critère D et pour la voie ;
   - un **programme de masque de style** : longueur plafonnée par champ, gras et intertitres retirés, formules récitées retirées, ordre des champs fixe ;
   - veto filtré par famille ou compté par famille, à toi de choisir et motiver ;
   - la statistique de famille déjà scellée (`statistique-famille-rejeu-v3-v1.md`, `bb2fa4a8…`, programme `statistique_famille_rejeu_v3_v1.py`, `298dde07…`, contre-lue « scellable », `e10aa0ed…`) : **confirme ou change, motivé**, ses trois choix (seuil 0,05, minimum 3, correction de Holm). Tu ne la réécris pas ; un changement passe par une pièce neuve.
3. **Programmes** (Python, bibliothèque standard ou numpy, graines par `numpy.random.SeedSequence`, R9) : `assemblage_selection_v4_v1.py`, `masque_style_cartes_v1.py`, `lecteur_par_programme_cartes_v1.py`, chacun avec ses essais (`essais_…_v1.py`) sur des **cartes synthétiques que tu inventes**, jamais sur les vraies ; un cas sain et un artefact pour chaque garde (R5) ; aucun repli silencieux. Lance les essais toi-même et verse leur sortie.
4. **Note v4** (`note-conception-juge-selection-cartes-ecartees-v4.md`) : constats 7 et 8 (défaut écrit pour chacune des six confirmations : tel qu'écrit dans les critères, pour le rejeu seulement) ; la fiche des décisions de Lazar mise à jour, au format : décision en une phrase ; enjeu ; deux ou trois options (avantage, inconvénient) ; recommandation et confiance ; défaut sous 48 heures. Décisions déjà posées le 19 vers 14:41Z, sans réponse, défauts non échus : rejeu à blanc d'abord (défaut : rejeu seul) ; veto (défaut : pour le rejeu seulement) ; lignée reconnue déclarée (défaut : non). Écris des critères qui marchent sous chaque option.
5. Rappel de fond, à tenir partout : « ce sont les essais avec experiences qui doivent trancher in fine les cartes et les tetss de mort » (Lazar) ; N-058 : un juge ne tranche jamais, il ne fait que choisir ce qui va à l'épreuve ; exclusion « un modèle décide » à l'intérieur de l'organisme ; R8 : rien de neuf sans citer la note de littérature (main, `docs/notes/organisme-auto-conception-v1/juge/litterature-juges-preference-pour-soi-v1.md`, `bb54b685…`).

## Ce que tu lis

`CLAUDE.md` ; dans `docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/` : critères v2 et v3, notes v1 à v3, les trois contre-lectures, l'audit et son programme, les rejeux v2 (notes seulement, pas les fichiers de sélection si tu peux t'en passer), la statistique de famille et sa contre-lecture ; `registres-provisoires/consignes-mere-epreuves-v9-compte-organisme-2026-11-19-v1.md` (GO-68, R-3854, GO-69, R-3876, audit R4) ; `docs/notes/organisme-auto-conception-v1/epreuves-v9/ordre-de-passage-epreuves-v9-v3.md` ; sur main (`git show origin/main:CHEMIN`) : `registres/go.md` (GO-2026-11-19-55 à -74), la note de littérature. Vérifie chaque empreinte avant de citer (R6, R11).

## Ce que tu rends

Dans ton bloc-notes seulement (la session verse et scelle) : les pièces nommées ci-dessus, les sorties d'essais, et `rapport-redacteur-criteres-v4-note-v4-v1.md` (constat par constat ; ce que tu n'as pas pu faire ; les points pour Lazar ; ce que tu as vu des rejeux). En-tête : « Auteur : rédacteur neuf, modèle F » ; aucun identifiant de modèle ; heure par `date -u`.

## Interdits

Aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun réseau sauf `git fetch`/`git show` du dépôt. Aucun commit, aucune poussée, aucune écriture dans le dépôt. Jamais de heredoc. Aucune valeur de clé. Aucun fichier « consigne-privee » ni « conception-ii-b », ni `brouillons/ii-b-saboteur-budget-v1/`, ni la branche `lot/compte-4-v1`, ni la ligne R-2059, ni `/root/.claude/`. Aucun chiffre sans chemin et empreinte. Français, termes développés, choses nommées par ce qu'elles font. Au premier refus d'un outil : arrête-toi et dis-le dans ton rapport.
