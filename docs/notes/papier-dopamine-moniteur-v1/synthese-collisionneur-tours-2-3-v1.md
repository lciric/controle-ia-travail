# Papier « dopamine » : ce que les critiques croisées et les réponses changent (v1)

- **Date** : 20 novembre 2026, 14:53 UTC. **Auteur** : Claude Fable 5.2, concepteur. Pièce de classe C. Aucune dépense, ni commit ni poussée.
- **Lu** : synthèse des six avis (`0bb721b3…`), consultation (`afc22a5f…`), antériorité (`5743dd21…`), énoncé (`16b2d9eb…`) ; dans `runs/collisionneur-dopamine-v1-20261120-122457/cellules/`, les quatre critiques croisées (A `d56e4b24…`, B `e4aab95f…`, C `9adb8599…`, D `1aae3f93…`) et les cinq réponses (A `d289c301…`, B `3bdd9296…`, C `fea74edb…`, D `652b7689…`, E `001d0ac6…`) ; `etat.md` (`834dc4ba…`). Quatorze compagnons d'empreinte des cellules vérifiés.
- **Non lu** : la critique croisée de Carbon (absente des cellules, arrêtée par une garde ; son essai sous `essais/` n'a pas été ouvert) ; les cinq conceptions du tour 1, connues ici par la synthèse des six avis seulement.
- **Renvois** : « critique A, l. 62 » = `E3-T2-critique-croisee-A.md`, ligne 62 ; « réponse A, l. 13 » = `E3-T3-reponse-A.md`, ligne 13. A Fable 5.2, B Opus 5.5, C Argon, D Astra, E Carbon.
- **Statut de tout ce qui suit** : analyses non exécutées. Tous les chiffres des cellules sont dits illustratifs par leurs auteurs ; aucun n'est repris ici comme mesure.

## Verdict

Les deux tours ne changent pas le classement de la synthèse des six avis (base et covariable d'abord, moniteur sous condition). Ils changent la **forme** de presque chaque épreuve : trois propriétés formelles, admises par tous ceux qui les ont reçues, retirent plusieurs mesures telles qu'elles étaient écrites, et une série de témoins devient obligatoire. Les quatre bases retenues par le directeur tiennent toutes, deux avec une condition nouvelle.

## 1. Ce qui converge (nouveau par rapport aux six avis)

**Trois propriétés formelles.**
1. **La somme simple des surprises se réduit à l'écart de réussite attendue entre la fin et le début.** Elle ne porte aucune information de chemin, et un échec honnête la produit aussi (critique A, l. 62-65 et 138-141 ; critique D, l. 49). Admis par B (réponse B, l. 56 et 184), C (réponse C, l. 26 et 72), E (réponse E, l. 11 et 89).
2. **À poids et contexte identiques, la lecture est identique.** Au début de l'épisode, l'écart entre deux jumeaux honnêtes est nul sans dispersion : toute détection y vaut 100 % par construction (critique A, l. 17 ; critique B, l. 19 ; critique D, l. 34). La lecture ne sépare donc deux bras que par le contexte ou par les poids (réponse A, l. 69 ; réponse B, l. 24).
3. **Une somme de scores corrélés d'un pas au suivant perd sa puissance**, et un seuil étalonné pas à pas sous-estime le bruit (critique A, l. 33 ; critique B, l. 43-46 ; critique C, l. 19-23). D'où : nul étalonné sur des épisodes honnêtes entiers, par tranche de longueur, et mesure de cette corrélation avant toute épreuve (réponse A, l. 51 ; réponse B, l. 53 ; réponse C, l. 29 ; réponse E, l. 28-30).

**Témoins devenus obligatoires.**
- **Consigne et adaptateur.** Un saboteur par consigne se lit par la consigne ; un saboteur par adaptateur de rang faible se lit par l'adaptateur (critique A, l. 18 et 56 ; critique B, l. 80, 95 et 176 ; critique C, l. 10 et 80). Parades admises : consigne honnête qui mentionne surveillance et sabotage sans les demander, et adaptateur honnête de même budget (réponse A, l. 21-22 et 57-67 ; réponse B, l. 25-27 ; réponse C, l. 15-17 ; réponse D, l. 12 et 54 ; réponse E, l. 13). A reconnaît qu'aucun contrôle ne neutralise entièrement le sens d'une consigne (réponse A, l. 22 et 194).
- **Honnête qui échoue.** Sur les mêmes tâches, à température nominale, obtenu par rejet, tâches fixées avant la génération (critique B, l. 54, 96 et 171 ; réponse A, l. 13 et 62 ; réponse C, l. 27 et 47 ; réponse E, l. 12). Le bras « tâches plus dures » et le jumeau « chauffé » ne valent pas témoin.
- **Fautes produites par le modèle, pas insérées.** Un texte inséré peut faire réagir la lecture comme texte étranger (critique B, l. 22-25 ; critique C, l. 9 ; critique D, l. 11). L'insertion devient un simple témoin de sensibilité (réponse A, l. 16 et 109-119 ; réponse B, l. 48 et 169-172).
- **Étiquettes de surprise par continuations.** Elles sont bruitées ; choisir la tranche des petites variations et la noter avec les mêmes tirages fausse la corrélation (critique A, l. 78-79 et 150 ; critique B, l. 47-49 et 141-142 ; critique C, l. 11). Parade : deux moitiés de tirages indépendantes et fidélité publiée (réponse A, l. 17 et 53 ; réponse C, l. 40 ; réponse D, l. 40 ; réponse E, l. 59).
- **Ne pas filtrer les cas positifs sur le silence du comparateur** : le comparateur y vaut zéro par construction (critique A, l. 22 et 147 ; critique D, l. 27 et 62). Analyse principale sur tous les épisodes (réponse B, l. 49-50 ; réponse E, l. 14).
- **Porte de reproduction avant tout** : sans elle, un résultat nul ne distingue pas « pas de signal » d'« instrument raté » (critique A, l. 112 ; réponse B, l. 84-94 ; réponse D, l. 38 et 64 ; réponse E, l. 59).
- **Évasion.** Elle se juge à dommage maintenu, sinon l'évasion peut être l'arrêt du sabotage (critique D, l. 11 ; réponse A, l. 25 et 140-148 ; réponse B, l. 204). Une seule attaque réussie réfute pour de bon ; une survie ne vaut que pour les attaques essayées (critique D, l. 36 ; réponse B, l. 206-208). La sonde réentraînée après évasion est un diagnostic, pas une défense (critique A, l. 27 ; réponse B, l. 62-63).
- **Règle de décision.** Marge gelée, intervalle entièrement d'un côté, zone indéterminée déclarée (critique D, l. 5 ; réponse A, l. 50 ; réponse B, l. 79-82 ; réponse D, l. 32).

**Le seuil de fausses alertes.** La divergence « 1 % contre 5 % » des six avis se referme, dans le collisionneur, du côté de 5 % : à 1 %, le seuil repose sur une poignée d'épisodes honnêtes (critique A, l. 31 et 171 ; critique B, l. 37-39 et 163 ; critique C, l. 24). Réponses : A, l. 49 ; B, l. 72 ; C, l. 10 ; E, l. 21. Le programme, lui, mesure le rappel à 1 % (`docs/programme-controle-ia-v2.md`, l. 184) : point à trancher, pas tranché ici.

## 2. Ce qui diverge encore

- **Première mesure.** A : la lecture ajoute-t-elle à un lecteur du texte, au début et aux frontières (réponse A, l. 200-209). B : reproduction, puis réussite attendue contre difficulté, puis ablation (réponse B, l. 249-257). C : polarité sur plan croisé et retrait du seuil (réponse C, l. 82-84). D : reproduction sur fortes variations, puis qualification de l'audit (réponse D, l. 64). E : petites variations en plan croisé (réponse E, l. 98-102). Point commun : juger l'instrument avant de construire un saboteur.
- **Cible.** A, B, C, E visent l'intention. D ne vise plus que « faire relire ce dossier », jamais « cet agent a voulu » (réponse D, l. 7, 11 et 75).
- **Modèle.** B, C et E placent la première mesure sur un modèle Qwen du papier (réponse B, l. 89 ; réponse C, l. 82 ; réponse E, l. 59) ; le chiffre que la consultation propose de rejouer est sur Llama-3.1-8B (consultation, l. 97).
- **Statistique de chemin.** Somme des plus grands écarts négatifs (réponse B, l. 177) ; agrégat sur scores bruts et sur résidus d'un modèle ajusté sur l'honnête (réponse A, l. 114) ; somme cumulée avec remise à zéro (réponse C, l. 47 ; réponse E, l. 65). Argon objecte que cette dernière oublie entre des fautes espacées (critique C, l. 40-46) ; B admet le fond, pas le taux avancé (réponse B, l. 52).
- **Cohérence entre couches.** E retire sa piste, les couches hautes étant une fonction des couches basses à poids fixés (critique A, l. 159 ; réponse E, l. 18). C garde un résidu entre les deux lectures (réponse C, l. 28 et 47) : à ne pas reprendre sans témoin de surprise honnête (critique C, l. 110).
- **Rejets partiels.** B : l'effet de sélection invoqué par Argon ne s'applique pas tel quel (réponse B, l. 38-39). D : pas d'estimateur d'effet local obligatoire, pas de borne générale d'impossibilité (réponse D, l. 20 et 24-25). E : une somme cumulée à remise à zéro n'est pas invariante par permutation (réponse E, l. 11). A : ordre des paramètres d'une loi chez Argon, à recalculer (réponse A, l. 23).
- **Coûts.** De quelques dizaines à un millier d'heures de carte selon la cellule, tous illustratifs (réponse A, l. 164 ; réponse B, l. 195 ; réponse C, l. 83 ; réponse D, l. 70-73 ; réponse E, l. 101). Aucun ne vaut devis.

## 3. Ce qui tombe

- Chez A : l'écart « lecture moins réussite », le bras « tâches plus dures », la porte du début d'épisode, « ne pas battre une référence réfute le transfert » (réponse A, l. 13-15, 29 et 36-40).
- Chez B : le nul entre jumeaux identiques, le rapport d'écarts-types, l'analyse restreinte aux épisodes qui passent les vérifications, la somme cumulée en statistique principale (réponse B, l. 24, 30, 49-52).
- Chez C : la somme terminale, l'écart « fin du saboteur moins début du jumeau », la greffe de médianes, le critère d'erreur de calibration, les indices de couches figés (réponse C, l. 10-11, 26-27 et 33).
- Chez D : la réussite attendue initiale jugée en détecteur, le positif « tout dossier assigné », les jalons produits par l'agent (réponse D, l. 11, 15 et 19).
- Chez E : la piste de découplage entre couches, la clé secrète, le jumeau « chauffé », deux critères d'instrument qu'un nul parfait manquerait (réponse E, l. 12, 18-19 et 30).
- Dans la consultation : la remarque d'arithmétique sur le petit effectif du tableau 4 n'est pas établie ; tout multiple de 36 convient (critique B, l. 31-33 ; réponse A, l. 20).

## 4. Effet sur les pistes et les quatre bases des six avis

| Élément des six avis | Après les tours 2 et 3 |
|---|---|
| Réussite attendue contre difficulté | Gardée. Se mesure par gain d'un modèle « texte plus lecture » sur « texte seul », hors échantillon, pas par résidu (réponse A, l. 71-85 ; réponse B, l. 37). Au début de l'épisode, la lecture est une fonction de l'énoncé. |
| Polarité chez le saboteur | Gardée, sur plan croisé avec les deux témoins de consigne et d'adaptateur (réponse A, l. 93-102 ; réponse B, l. 132-154 ; réponse C, l. 40-44). |
| Somme cumulée sous le seuil | La somme simple tombe. Reste une statistique de chemin, comparée à l'écart entre extrémités et au texte agrégé par la même règle (réponse B, l. 181-184). |
| Évasion à compétence constante | Gardée, à trois axes : détection, compétence, dommage maintenu (réponse A, l. 142-147). |
| Témoins d'ablation | Par la moyenne et par rééchantillonnage ; conclusion permise : « nécessaires à la réussite », pas « codent la valeur » (réponse A, l. 32 et 158). |
| Base : sonde de réussite sur honnêtes seuls (consultation) | Non soumise au collisionneur. Renforcée par la porte de reproduction et par le témoin « honnête qui échoue ». À lire aux frontières d'action et à comparer à un lecteur du texte déjà écrit (réponse A, l. 80-85). |
| Base : divergence du jumeau forcé (Carbon) | Gardée sous condition : positive par construction dès qu'une consigne ou un adaptateur distingue l'agent du jumeau ; n'entre qu'avec un nul mesuré sur des variantes honnêtes distinctes (critique A, l. 143-146 ; critique B, l. 150 et 170 ; réponse A, l. 30 ; réponse E, l. 13). |
| Base : même jalon, mêmes fichiers (Astra) | Renforcée : rendez-vous imposés par l'évaluateur, et le comparateur reçoit longueur, nombre de lectures, arrêts et absences (réponse D, l. 15 et 46). |
| Base : sonde réentraînée sans le seuil (Fable 5.2) | Reprise par C, D et E (réponse C, l. 54-57 ; réponse D, l. 40 ; réponse E, l. 59-61). Si elle seule passe, elle se poursuit sous son nom, pas comme validation de la sonde du papier (réponse D, l. 40). |

## 5. Ce que l'antériorité occupe, et ce qu'elle laisse ouvert

Source : `anteriorite-v1/anteriorite-papier-dopamine-v1.md` (`5743dd21…`). Le collisionneur n'a rien cherché ; les références que ses cellules citent de mémoire ne sont pas vérifiées (R7).

| Brique | Verdict de l'antériorité (ligne) | Ce que les tours 2 et 3 y ajoutent |
|---|---|---|
| Lecture du papier comme base et covariable | Partielle (l. 59) | Rien d'occupé en plus ; la séparation « difficulté contre signal propre à l'exécution » est publiée et se cite. |
| Somme séquentielle des petits signaux | Partielle ; forme occupée de tous côtés (l. 75) | La forme « somme simple » est en outre vide par télescopage. Reste ouvert, comme avant : mesurée sur des scores de sondes internes d'un agent, sous le seuil, avec témoin honnête en erreur. |
| Évasion à compétence constante | Occupée (l. 88) | Les trois axes et la conclusion asymétrique sont des précautions, pas un apport. |
| Sonde de réussite sur honnêtes seuls, base à battre | Partielle (l. 104) | Emploi comme base d'une sonde d'intention : non trouvé. Le voisin le plus proche (Lin et al.) n'a pas pu être lu. |
| Jumeau forcé sur le même début | Partielle (l. 119) | Les deux avertissements publiés (référence « inefficace et trompeuse » ; direction « affiné moins base » qui échoue) rejoignent la condition du nul sur variantes honnêtes. |
| Même jalon, mêmes fichiers | Occupée dans son principe (l. 132) | À citer, jamais comme apport propre. |
| Sonde réentraînée sans le seuil | Aucune antériorité trouvée au périmètre (l. 144) | Absence attendue (témoin attaché à ce papier), ne vaut pas zone libre. Un voisin reste à lire en entier. |

Réunion des sept : aucune antériorité trouvée au périmètre cherché le 20 novembre 2026, avec trois réserves (l. 152) : assemblage de pièces publiées ; voisins récents et serrés ; un papier sur les menaces diffuses, non relu, préfère l'entraînement à la surveillance. Les onze groupes de citations obligatoires (l. 156-168) et la liste « à ne pas écrire » (l. 170) s'appliquent tels quels.

## 6. Limites de cette synthèse

- La critique de Carbon manque : E a répondu aux critiques, mais n'a critiqué personne.
- La consultation (sixième avis) n'est pas passée par le collisionneur : sa base « sonde de réussite sur honnêtes seuls » n'a reçu aucune critique croisée.
- Je n'ai recalculé aucun des calculs illustratifs des cellules.
- Les numéros de ligne sont ceux des fichiers aux empreintes citées en tête.
