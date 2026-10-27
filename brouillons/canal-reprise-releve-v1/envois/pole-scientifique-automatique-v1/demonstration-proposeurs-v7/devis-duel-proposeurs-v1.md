# Duel des proposeurs : un proposeur à modèle contre les références gratuites, sur des mondes hors de l'espace du chercheur mécanique — proposition et devis v1

Lignée conv-audit (instance du 27 octobre 2026, Fable 5.1), écrit vers 17:18 UTC (heure de fichier ; mes deux premiers en-têtes disaient 17:24 puis 17:22, estimées — leçon : lire `date -u` avant d'écrire, pas après). Suite des lectures v1
(`884548b0…`) et v2 (`cfba47ab…`) de la démonstration des proposeurs, et de l'option 3 du collisionneur « proposeur
enfichable » (`0a209c33…`). **Rien n'est dépensé ici** : le duel est une dépense, donc un nœud de décision (devis, GO,
lancement chez session-depot). Exploratoire (R-546) : lecture fixée ici avant la course, pas de préenregistrement scellé.

## Verdict

1. **Ce que le duel mesure** : si un proposeur à modèle (Opus 5.5, avec ou sans la partie de développement) retrouve des
   structures qu'aucune référence gratuite ne retrouve — sur les deux formes où le chercheur mécanique est hors de son
   espace (« trois traits » : 0 sur 14 ; « seuil décalé » : 5 sur 21 en v2). Si oui, la prise « proposeur » (et, avec le
   développement, la prise « exploration ») a une valeur mesurée ; sinon, le mécanique suffit et l'on ne paie plus de
   proposeur à modèle sur ce genre de monde.
2. **Dépense** : 20 mondes × 2 sessions utiles de proposeur × 2 bras à modèle = **80 sessions**, de 0,2 à 1,0 USD chacune
   (plafond 1,5 USD par session, 15 tours) ; **attendu 30 à 60 USD, plafond 100 USD**. Tout le reste (juge, témoins,
   expérimentateurs et vérificateurs simulés par l'adaptateur mixte de v7 version 9, références) est gratuit.
3. **Plomberie** : v7 version 9 (`d81deef`, 202 essais) ; chemin répété sans dépense (`demonstrations/repetition_duel_v7.py`,
   cinq vérifications tenues) ; bac à sable exigé ; seul le proposeur passe par le relais.

## 1. Plan

- **Mondes** : grammaire v2, structures imposées « trois_traits » et « seuil_decale » (deux moniteurs de chaque, ou tirage
  parmi les deux), graines 20261201 à 20261220 ; parties calibrage, développement, épreuve ; témoins vrais exacts.
- **Bras** (mêmes mondes, même population initiale aléatoire, mêmes témoins, même juge : v1 sans urne, nul informé, nul
  d'archive ajusté, e-BH, témoins sans agents, 3 générations, 12 propositions par génération) :
  - M-expl : proposeur Opus 5.5 **avec** la partie de développement (`--proposeur agent --exploration-developpement
    --roles-reels proposeur`) ;
  - M-aveugle : proposeur Opus 5.5 **sans** la partie de développement ;
  - mécanique (avec développement) et aléatoire : références gratuites, rejouées sur les mêmes mondes (0 USD).
- **Modèle** : Opus 5.5 seul (décision du 27 octobre, 14:17) ; Fable 5.1 en second duel seulement si Opus apporte quelque
  chose (même devis).

## 2. Lecture (fixée avant la course)

Pour chaque monde et chaque bras : le nombre de structures retrouvées (au moins une fiche non témoin promue dont la loi
emploie exactement les traits de la structure), les témoins faux promus, les promues sans lien.

- **L1** (validité) : témoins faux promus ≤ α dans chaque bras ; promues sans lien rapportées (attendu : 0).
- **L2** (apport de l'exploration, la question principale) : contraste par monde v = [structures(M-expl) −
  structures(mécanique)] / nombre de moniteurs du monde ∈ [−1 ; 1] ; **pari apparié borné** (conception
  `../pari-de-signe/conception-pari-de-signe-v1.md`, forme mélange, Λ = {0,1 ; 0,3 ; 0,6 ; 0,9}, α = 0,05) sur les 20
  mondes dans l'ordre des graines : promu = « l'exploration par Opus apporte au-delà du mécanique » ; non promu =
  « non démontré à 20 mondes » (pas « réfuté »).
- **L3** (apport du modèle à l'aveugle) : même pari, M-aveugle contre aléatoire.
- **L4** (ce que coûte l'exploration) : M-expl contre M-aveugle, même pari.
- **L5** (coût) : USD par structure retrouvée, par bras, rapporté — jamais un critère (métrique rejetée par le
  collisionneur).
- Arrêt : après 10 mondes, si M-expl n'a retrouvé aucune structure (0 sur ≈ 30 moniteurs), la suite est annulée (la
  moitié de la dépense économisée) et la lecture est « pas d'apport à 10 mondes ».

Prédiction (à contester) : L2 promu avec une confiance de 0,4 ; L3 non promu (0,7) ; L4 promu (0,6).

## 3. Devis

| poste | nombre | plafond unitaire | plafond |
|---|---|---|---|
| sessions de proposeur, M-expl (2 utiles par monde) | 40 | 1,5 USD | 60 |
| sessions de proposeur, M-aveugle | 40 | 1,0 USD | 40 |
| **total** | 80 | | **100 USD** (attendu 30 à 60) |

Relais à 100 USD, réserve 0,40 par appel ; `--budget-usd` 110 par course de 20 mondes ; proposeur `plafond_proposeur_usd`
1,5 et `max_tours_proposeur` 15. Durée : 2 à 4 heures (sessions séquentielles par monde, mondes en parallèle par deux).

## 4. Ce que session-depot devra faire (sur le mot de Lazar)

- Comme (a) bis : relais avec la clé dans son seul environnement ; `env -i … python -I -B pole --moteur claude-sdk
  --confirmer-moteur-reel --roles-reels proposeur --monde-banque <banque du monde> --sans-urne --temoins-sans-agent
  --temoins-par-generation 2 --propositions-par-generation 12 --proposeur agent --modele-proposeur claude-opus-5-5
  [--exploration-developpement] --generations 3 --sortie …` par monde (script d'enchaînement à écrire chez moi avant le
  GO : `demonstrations/duel_proposeurs_v7.py`, qui génère les mondes, lance les bras et lit L1 à L5).
- Verser la sortie sur `donnees/duel-proposeurs-v1` ; je lis dans les deux sens.

## 5. Ce que le duel ne dira pas

Rien sur un chercheur de la littérature (il faudrait sa traduction texte → loi, question du collisionneur) ; rien sur
une banque réelle (grammaire écrite par moi, limite déclarée) ; rien de décisif (20 mondes, exploratoire).
