# Croisement de cinq bilans « Regard ou raisons » — méthode v1

Écrite le 14 novembre 2026 à 10:37 UTC (heure relevée par `date -u`), avant l'ouverture d'aucun des cinq bilans, par un
lecteur neuf du dépôt qui n'a écrit aucun d'eux. Lus avant d'écrire : `../question-v1.md`, `../faits-v1.md` (seulement).
Demande du directeur : registre R-2679, R-2680, R-2705, R-2708. Aucun appel payant.

## 1. Sources (cinq, dans l'ordre de lecture)
S1 session mère (`../bilan-mere-v1.md`) ; S2 organisme d'idéation (36 fiches validées, course g1) ; S3 collisionneur à cinq
espèces (`../collisionneur-v1/run-e3-v1/`, étage III, trois tours) ; S4 consultation à part n° 1 ; S5 consultation à part n° 2.
Les étiquettes S1 à S5 ne sont visibles que dans `correspondance-sources-v1.json` (non montrée aux juges).

## 2. Extraction
Une fiche par unité, de trois genres :
- **R** explication rivale (famille a, b ou c de la question) ;
- **F** conseil de forme du papier ;
- **X** expérience décisive (duel, métrique, seuil, contrôle négatif, témoin).
Une explication rivale qui porte sa propre expérience reste une fiche R (l'expérience y figure) ; une fiche X n'est faite que pour
une expérience présentée comme décisive ou comme la moins chère du duel. Le point (1) « ce que la question suppose » et le
point (5) « ce qui ferait changer d'avis » ne donnent pas de fiche à part ; ils sont versés aux réserves s'ils portent une
idée absente des fiches. Pour S2, chaque fiche validée est lue comme une proposition ; S3 : on garde ce qui survit au dernier
tour, et ce qui est proposé aux tours antérieurs s'il n'est pas explicitement réfuté (les réfutations sont notées).

## 3. Fusion des doublons
Deux propositions fusionnent si elles ont **le même mécanisme et la même prédiction séparatrice** (même signe, même grandeur
observée). Même mécanisme mais prédiction différente : deux fiches, liées par un renvoi. Même étiquette mais mécanismes
différents : deux fiches. La fiche fusionnée garde la meilleure formulation de chaque champ (prédiction la plus précise, test
le moins cher) sans rien ajouter de mon cru. Chaque fusion est consignée dans la correspondance (fiche → sources → passages).

## 4. Anonymisation
Source retirée ; noms d'espèces, de modèles et d'outils retirés ; style normalisé en français sobre, champs fixes :
genre ; famille ; nom neutre ; mécanisme (2 phrases) ; prédiction séparatrice (contre « raisons » et contre « regard ») ; test le
moins cher (adaptateurs publiés, épisodes déjà joués ou non) ; contrôles positif et négatif ; coût. Longueur bornée (environ
120 mots par fiche R ou X, 60 par fiche F). Les références de la source ne sont pas montrées aux juges (la collision est jugée
par eux à partir de leur propre connaissance, puis vérifiée par moi pour les huit premières). Ordre des fiches tiré au hasard
(graine fixe consignée), identifiants neutres (P01…).

## 5. Idées témoins (écrites ici, avant toute lecture des bilans)
- **T-connue** (connue et publiée) : « Le gain disparaît quand on retire la direction interne de conscience d'évaluation ; on
  prédit que l'ablation de cette direction, construite par différence de moyennes sur des textes évaluation contre déploiement,
  fait remonter les actions nuisibles. » (Pilotage et ablation de la conscience d'évaluation déjà publiés, références [10] des
  faits et voisines ; c'est aussi la manipulation déjà préenregistrée par le projet : elle n'apporte rien de neuf.) Place
  attendue : importance moyenne à haute, collision haute, nouveauté nulle ; ne doit pas être au sommet.
- **T-fausse** (intestable) : « Les modèles formés à la spécification ont acquis une intention morale authentique inaccessible à
  toute mesure, comportementale ou interne ; cette intention, et non les raisons apprises, explique le gain. Prédiction : aucune
  différence observable ne la sépare de "raisons". » Place attendue : en bas.
- **T-banale** (sans prédiction séparatrice) : « Le juge peut se tromper ; il faudrait faire relire un échantillon par des
  humains pour vérifier que les taux d'actions nuisibles sont corrects. » (Bon usage, mais ne sépare ni de « raisons » ni de
  « regard ».) Place attendue : en bas pour la séparation, moyenne au total.
- **T-forme-banale** (témoin du genre F) : « Écrire clairement et soigner les figures. » Place attendue : dernier des conseils.
Les témoins reçoivent le même format et le même style que les fiches ; ils sont mêlés au hasard.

## 6. Critères (note de 1 à 5 chacun)
C1 importance pour l'affirmation « la bonne conduite tient parce qu'ils ont appris les raisons » ; C2 prédiction qui sépare à la
fois de « raisons » et de « regard » (5 : signes opposés énoncés pour les trois ; 1 : aucune) ; C3 test faisable avec les
adaptateurs publiés, peu cher (5 : sur les épisodes déjà joués) ; C4 contrôles positif et négatif présents et pertinents ;
C5 risque de collision avec un travail publié (5 : aucun connu ; 1 : déjà publié tel quel).
Score R/X = C1×2 + C2×2 + C3 + C4 + C5 (sur 35), rapporté sur 10. Fiches F : critères propres — F1 effet sur la portée et
l'impact, F2 fidélité (n'affirme rien au-delà du mesuré), F3 concrétude (actionnable) ; score = F1×2 + F2 + F3 (sur 20), sur 10.

## 7. Juges
Au moins deux juges neufs, à l'aveugle, de deux modèles différents (« modèle A », « modèle B »), appelés par l'outil en ligne de
commande local, sans outils, depuis un répertoire de brouillon (pas d'accès au dépôt). Chaque juge reçoit : la question,
les faits, la grille, les fiches anonymes mêlées aux témoins ; ni les sources, ni le nombre de sources, ni le mot « témoin ».
Sortie demandée en JSON (une ligne par fiche, notes et une phrase de motif). Si les fiches sont trop nombreuses pour un seul
appel, elles sont réparties en lots avec les témoins répétés dans chaque lot (contrôle de dérive entre lots). Si un appel
échoue ou rend un JSON invalide, il est rejoué une fois, et c'est consigné. Je ne note pas moi-même (auteur de l'extraction).

## 8. Agrégation et accord entre sources
Note d'une fiche = moyenne des juges (chacun sur 10). Désaccord = écart absolu entre juges ; écart > 3 signalé.
Accord de rangs entre juges : corrélation de Spearman sur les fiches R/X, rapportée. **Accord entre sources** = nombre de
sources distinctes (1 à 5) qui portent l'idée après fusion ; il est **rapporté à côté** de la note, jamais additionné à elle
(une idée portée par plusieurs sources n'est pas meilleure pour autant ; les sources partagent des modèles et les mêmes faits,
donc ne sont pas indépendantes au sens strict). À note égale (écart < 0,3), l'accord départage.

## 9. Fiabilité (témoins)
Notation déclarée **non fiable** si T-fausse ou T-banale finit dans la moitié haute des fiches R/X d'un juge ou de la moyenne,
ou si T-forme-banale n'est pas dans le dernier quart des F. T-connue au premier rang ou C5 de T-connue ≥ 4 : réserve sur la
détection de collision. Un juge qui échoue seul aux témoins est rapporté ; la synthèse s'appuie alors sur l'autre, en le disant.

## 10. Antériorité
Pour les huit premières propositions : recherche rapide (Web permise) ; référence attribuable (auteurs, titre, année, lien) ou
« à vérifier ». R8 : une zone non trouvée est une question, pas un trou. Aucun chiffre de l'état de l'art repris (R7).

## 11. Pièces
`methode-v1.md` (scellé avant lecture) ; `fiches-anonymes-v1.json` et `.md` ; `correspondance-sources-v1.json` ;
`notes-brutes-v1/` (entrées et sorties des juges) ; `agregation-v1.json` ; `synthese-croisement-v1.md` (scellée, 150 lignes au
plus). Aucun identifiant de modèle dans les pièces. Interdits respectés : rien des bras d'attaque, du mode tenu à l'écart,
T0.6, 7a, 7b, T0.7 ; aucune valeur de clé ; aucun commit.
