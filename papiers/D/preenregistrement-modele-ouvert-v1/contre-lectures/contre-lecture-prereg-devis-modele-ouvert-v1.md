# Contre-lecture (R2) — préenregistrement et devis de l'expérience sur modèle ouvert du papier D, v1

Contre-lecteur neuf : Opus 5.5, 24 novembre 2026, lecture seule. Empreintes des quatre pièces vérifiées, ainsi que celles citées dans le préenregistrement ; le commit `e1dd2d68` existe. Le validateur ne signale qu'un manque : les deux empreintes de contre-lecture. Le script rejoué redonne tous les chiffres du devis, et l'exemple de la note est reproduit (354, 597, 519 ; 586, 132).

## Préenregistrement

1. **Documents qui font foi — bloquant.** Plusieurs pièces sont seulement annoncées : la consigne « gelée », l'invite du juge, le lexique, le programme de mutation, les trois détecteurs et leurs cas plantés, la licence et les comptes d'EvalPlus. Les décisions de Lazar manquent aussi : écarts 1 à 3, modèle d'audit, avec un repli si Llama est refusé. *Correction* : écrire chaque pièce et la citer par chemin et empreinte, citer la référence du GO, nommer le moniteur d'audit de repli.

2. **Fiche de prédictions — bloquant : le risque de bifurcation est réel.** Les règles existent, mais cinq choix libres déterminent le signe prédit et n :
   - la valeur de γ du pilote n'est pas fixée ;
   - on ne sait pas si les masses et survies des quatre graines du pilote sont mises en commun ou prises graine par graine ;
   - la loi simulée pour la puissance, le nombre de tirages et sa graine ne sont pas donnés ;
   - la méthode de la « borne haute à 80 % » n'est pas donnée ;
   - l'ordre de mise à jour de la loi factorisée (simultané ou successif) n'est pas donné.

   Le code d'analyse qui calcule H1 à H3 à partir des sorties n'existe pas encore. *Correction* :
   - sceller avec le texte un script `fiche_calc` déterministe, éprouvé à blanc ;
   - l'ordre est : masses du tour 0, puis γ, puis pilote à ce γ, puis écart-type, puis n ;
   - l'additif ne recopie que la sortie et l'empreinte de ce script ; tout choix à la main est un écart ;
   - le script de lecture des contrastes est scellé avant l'étage 2.

3. **Survies constantes par strate (prédiction) — majeur.** Le calcul de m_i avec β_i moyen est biaisé dès que β(x) varie dans une strate, par l'inégalité de Jensen. Exemple : β_f valant 0,5 ou 1 donne un m_f sous R 1,68 fois plus grand au niveau de l'épisode. Le signe peut basculer. *Correction* : calculer deux bornes, l'une par strate, l'autre par épisode (moyenne de β(x)^K, moyenne de exp(Kγ r̄(x))). Exiger le même signe des deux bornes, sinon « jamais parti ». τ est rapporté pour les deux.

4. **Nombre de paires et famille sous Holm — majeur.** Le premier seuil de Holm à quatre tests vaut 0,0125. Le plus petit p atteignable vaut 0,031 à n = 6 et 0,0156 à n = 7 : la famille secondaire ne peut rien rejeter sous n = 8. À n = 9, il faut 9 graines sur 9 aux trois premiers rangs, et 8 sur 9 pour H1. *Correction* : n entre 8 et 12, ou une famille réduite et fixée dans la fiche. Déclarer que « non concluant » est l'issue attendue pour la famille secondaire. La taille de la famille, si H2 n'est pas lancée, est fixée avant l'étage 2.

5. **Critères de lecture — majeur.**
   - La table de H1 n'est pas exclusive : « p ≤ 0,05, médiane sous 30 » et « toutes les différences dans ±30 » peuvent valoir ensemble. *Correction* : la première ligne vérifiée l'emporte, dans l'ordre écrit.
   - « Même table » pour H3 est inapplicable, les seuils étant en pour mille. *Correction* : pour H3, 0,03 d'aire sous la courbe et bande ±0,03.
   - Pour H2, « ne monte pas » n'est pas défini. *Correction* : médiane sous +30 ou baisse significative.
   - « Significatif » ne précise pas l'ajustement. *Correction* : « après Holm ».
   - P1 met τ dans la prédiction, mais aucun verdict ne l'emploie. *Correction* : τ descriptif ; dire si la différence prédite est celle de la graine ou celle de la fiche.

6. **Admissibilité — majeur.** Une graine dont la sonde a une aire sous la courbe inférieure à 0,70 est remplacée : un critère propre à H3 modifie l'échantillon de H1. *Correction* : la graine reste pour H1 et H3 est déclarée « non évaluable » pour elle. Préciser aussi deux points : à quelles doses s'applique la part de triche ajustée, et ce que deviennent H2 et les doses si l'on part sans amorçage.

7. **Vérité de la triche sur les tâches mutées — majeur.** Toute réussite visible n'est une triche que si aucune solution honnête ne satisfait l'assertion mutée. Or une mutation du type « valeur plus un » est exactement ce que produit une erreur d'une unité. Les négatifs « solutions de référence » sont triviaux. *Correction* :
   - Négatifs naturels, avec règle d'exclusion avant scellement. Négatifs pris parmi les échantillons du modèle de base sur la tâche non mutée, réussis comme ratés aux tests cachés. Toute tâche où l'un d'eux passe l'assertion mutée est exclue avant scellement.
   - L'assertion mutée ne doit pas reprendre un exemple de la docstring.
   - Le harnais exige un témoin d'exécution de toutes les assertions. Il est éprouvé sur un cas sain et sur des artefacts : `sys.exit(0)`, objet toujours égal.
   - Fixer `advantage_task` et `impossible_task` par type de tâche.
   - Récompense des tâches témoins à écrire.
   - Contamination probable d'EvalPlus dans Qwen2.5 : limite déclarée.
   - « 475 tâches disponibles » n'est pas vérifié et égale exactement la somme exigée. Écrire la règle si le nombre est moindre : réduction proportionnelle ou « jamais parti ».
   - « Neuf sur dix » est incalculable avec 8 épisodes : en exiger 10.

8. **Épisodes illisibles — majeur.** Ni définition ni plafond de longueur générée. Exclure ces épisodes cacherait un obscurcissement par chaîne dégradée. *Correction* : fixer le nombre maximal de jetons. Est « illisible » le seul épisode sans code extractible. Les autres restent au dénominateur de U, la vérité restant fixée par programme. La part tronquée est rapportée par bras.

9. **Moniteur en boucle = modèle de base gelé — majeur.**
   - Circularité : la politique partage ses poids avec le juge. Garde : juge appelé adaptateur désactivé, contrôlé à chaque tour par des scores identiques sur 50 textes fixes, éprouvée sur un cas sain et sur un artefact (adaptateur actif).
   - Préciser le jeton et la normalisation (« OUI » contre « NON »).
   - Biais d'autopréférence : à déclarer.
   - Le lexique validé sur des cas plantés ne garantit pas la séparation v/f sur de vrais épisodes. *Correction* : revalider sur un échantillon tiré au sort des tricheurs des tours 0 et K, par deux lecteurs, avant lecture.

10. **H2 et opérateur B — majeur, puis mineur.**
    - Le bras P est bien l'opérateur B, r̄_C = βR − (1−β)C, par la règle multiplicative sans ancrage, limite η → ∞ du `thm:dynamics-tabular` (a1). La forme factorisée est `eq:two-channel-flow` avec η → ∞ et κ = 0. La reformulation est fidèle à `rem:mean-field`.
    - Mais, au premier ordre en γ, les deux lois donnent la même variation de logit(q), soit γ(A₀ + D·s). Elles ne se séparent que par la vitesse de croissance de la part sans mention parmi les tricheurs : γD dans la loi jointe, γDq dans la loi factorisée.
    - *Correction (majeur)* : préenregistrer cette trajectoire comme observable descriptive de discrimination ; nommer la dérive non spécifique (oubli de l'amorçage) comme explication rivale d'une baisse de q.
    - *Correction (mineur)* : déclarer que P emploie la survie attendue β(x) et R une interception tirée, et que P4, P5, P2 (devenue descriptive) et P3 (bistabilité) de la carte sont retirés. Mettre dans le texte la table de correspondance avec la carte, aujourd'hui dans la seule note.

11. **H3 — mineur.** `thm:geometry-training` porte sur le gradient d'une perte de filtre ; ici, il n'y a que sélection. Le signe est une conjecture : le dire. Ajouter une sonde témoin sur un trait sans rapport, pour séparer la dérive générique de la dégradation ciblée.

12. **Taille minimale d'intérêt — mineur.** « Deux écarts-types » ignore la grappe de 16 épisodes par tâche et la variance d'entraînement entre graines. *Correction* : présenter 30 comme une convention, non comme une dérivation.

13. **Gardes de la chaîne — mineur.**
    - Défauts du code `max_false=0.05`, `max_mention=0.01` : écrire que 0,01 et 0,03 sont passés explicitement.
    - Zéro faux positif sur 300 cas borne le taux à environ 1 % seulement. Il faut 1 000 négatifs pour une borne et non un point.
    - Seuil de 0,05 du terme de sélection sous H : préciser l'unité (probabilité de survie). Dire ce que devient une graine qui lève `GuardError`.

14. **Graines — mineur.**
    - La racine 2026112404 diffère de `ROOT_ENTROPY = 20261124` de la chaîne. Dire laquelle régit le tirage des interceptions et le rééchantillonnage.
    - Les épisodes du tour 0 doivent avoir une clé sans le bras.
    - Donner la table qui convertit les noms en entiers.

15. **Lecteurs de l'audit de symétrie — mineur.** Ils risquent de contredire « aucun appel d'interface payant ». Trancher (agents ou personnes) avant scellement.

## Devis

1. **Plafond de l'étage 1 — majeur.** Dans le cas lent, 46,3 h plus 25 % font 57,9 h, au-dessus de 50 h. La phrase « la marge est dans le plafond » est donc fausse. De plus, le pilote vient en dernier dans l'ordre de priorité alors que la fiche ne peut se faire sans lui. *Correction* : plafond de 58 h, ou règle écrite d'un pilote réduit compatible avec la fiche.

2. **Exécution des tests dans le bac à sable — majeur.** L'exécution des tests (environ 7 800 épisodes par bras et par graine, avec délais d'expiration) n'est pas chiffrée. La carte est facturée pendant qu'elle attend. *Correction* : ajouter une hypothèse de débit (épisodes par seconde, nombre de cœurs) et le recouvrement avec la génération, puis la mesurer à l'étage 1.

3. **Charges omises ou non documentées — mineur.**
   - Le supplément de 0,2 à 0,5 h du témoin positif n'est pas expliqué.
   - L'installation de l'étage 2 n'est pas comptée dans les totaux.
   - Les remplacements de graines (jusqu'à trois départs par dose, soit au plus 5,7 h) ne sont pas comptés.
   - Démonstrations réemployées entre graines ou régénérées : à écrire.
   - Pas de temps fixe pour les phases « masses » et « démonstrations ».
   - 950 jetons lus par épisode pour les sondes : absent du § 2.
   - Les épisodes du témoin positif manquent dans le compte de 426 600.
   - Les négatifs naturels du point 7 du préenregistrement demandent une génération sur carte à l'étage 1.

4. **Débits — mineur.** Sur 24 Go, l'affinage à 2 000 jetons par seconde au moins est optimiste ; génération et affinage ne tiennent pas ensemble en mémoire (rechargement à chaque phase). Un passage à 48 Go change le prix et peut-être les heures.

5. **Tenue du plafond — mineur.** Aucun mécanisme écrit. *Correction* : compteur d'heures lu par l'interface du fournisseur, garde éprouvée sur un cas sain et sur un artefact.

6. **Prix — conforme.** Le GO devra dater le prix, le fournisseur, la carte, le plafond en euros, le disque et le stockage durable des adaptateurs.

## Verdicts

- **Préenregistrement : SCELLABLE APRÈS CORRECTIONS.** Lever d'abord les points 1 et 2 (bloquants), corriger les majeurs 3 à 10, puis faire vérifier les corrections par le même contre-lecteur.
- **Devis : SCELLABLE APRÈS CORRECTIONS** (points 1 et 2 ; chiffres conformes au script).
