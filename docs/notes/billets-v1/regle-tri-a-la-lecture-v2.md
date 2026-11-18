# Règle de tri à la lecture des billets — v2

Écrite et scellée **avant** toute lecture de texte de billet (mandat `mandat-corpus-v2-tri-a-la-lecture-v1.md`, tâche 3), le 2026-11-18. Remplace, pour le tri, `regle-classement-et-appariement-v1.md` (qui reste archivée, non modifiée). Avant ce scellement, seules ont été ouvertes les métadonnées (titre, votes, étiquettes, longueur, relations étiquette-billet) et les scripts de la v1. Les textes de la v1 ont été copiés sous `/home/user/billets-corpus-v2/` sans être ouverts.

## 1. Étiquettes retenues (neuf)
Les sept de la v1 (contrôle de l'IA, surveillance non fiable, interprétabilité, tromperie, alignement trompeur, extraction du savoir latent, sous-performance délibérée) plus **autoencodeurs épars** (« Sparse Autoencoders (SAEs) », `9LYbEZSAi8kq83DGF`) et **ingénierie des activations** (« Activation Engineering », `QdTRKbR4MJSz4JWvn`). Ni « évaluations » ni « alignement de la chaîne de raisonnement ». Le site n'a aucune étiquette « sondes ». Les billets rejetés par la modération du site n'apparaissent pas dans les vues publiques et ne font pas partie du corpus (voir le rapport).

## 2. Définition du billet de résultats empiriques
Est « billet de résultats empiriques » un billet dont **l'objet principal est de rapporter une expérience des auteurs**, avec **au moins un chiffre ou une figure de résultat**.
- *Expérience des auteurs* : mesure, entraînement, évaluation, ablation, analyse de données ou étude auprès de personnes faites par les auteurs du billet (ou leur équipe), y compris sur un banc d'autrui, y compris un résultat nul ou négatif.
- *Chiffre ou figure de résultat* : nombre, tableau ou graphique produit par cette expérience (pas un chiffre de contexte, ni un graphique d'autrui, ni un schéma conceptuel).
- *Objet principal* : le titre, le résumé ou plus de la moitié du corps porte sur l'expérience et ses résultats ; un billet dont l'expérience n'est qu'une illustration d'un argument est écarté.
- La décision est binaire (oui / non). Un cas serré est tranché par les règles ci-dessous, puis marqué « limite » dans le motif ; il n'est jamais mis en réserve.

## 3. Cas limites, dits d'avance
| Cas | Décision |
|---|---|
| Essai d'opinion ou de programme de recherche avec une figure (graphique d'autrui, schéma, courbe illustrative) | non |
| Essai dont une section centrale rapporte une expérience des auteurs avec chiffre, et dont le reste est argumentatif | oui seulement si cette section est plus de la moitié du billet ou le résumé en tête ; sinon non |
| Annonce d'article (résumé d'un article des auteurs) | oui si le billet reprend des résultats chiffrés ou des figures de l'expérience ; non s'il ne donne que le thème, un lien, un appel ou des résultats sans aucun chiffre |
| Réplication (des auteurs, d'un résultat d'autrui) | oui si les auteurs rapportent leurs propres chiffres ; non si le billet discute sans rejouer |
| Exposé théorique avec simulation | oui seulement si la simulation ou l'expérience numérique est le cœur du billet et donne des chiffres de résultat ; non si elle illustre un argument |
| Exemple jouet, expérience de pensée, dialogue fictif, scénario | non |
| Analyse empirique originale de données publiques (traces, sondages, bancs, journaux d'incidents) faite par les auteurs | oui |
| Revue de littérature, synthèse de résultats d'autrui, liste de ressources | non |
| Bilan d'un projet, d'un atelier ou d'un stage | oui seulement s'il rapporte des chiffres ou figures de résultat des auteurs comme objet principal |
| Guide, tutoriel, mode d'emploi d'un outil, épisode de podcast, transcription, débat, question, événement | non |
| Étude de cas qualitative sans mesure (transcriptions de conversations avec un modèle) | non, sauf décompte ou taux rapporté comme résultat principal |
| Billet entièrement ou principalement sur du code ou une proposition de méthode sans résultat chiffré | non |

## 4. Candidats et écartés mécaniquement
Par année civile de 2022 à 2026 (2026 jusqu'au 18 novembre), les candidats sont les billets portant au moins une des neuf étiquettes. Sont écartés **sans lecture** (comptés à part, jamais dans le taux « écartés à la lecture ») : questions, événements, brouillons, billets de moins de 300 mots (compte du site, ou compte du texte à défaut).

## 5. Lecture
Lecture structurée par un seul agent (le trieur), non intégrale : titre, nombre de mots, nombre d'images, en-tête (premiers 1 500 caractères environ), tous les intertitres, passages à nombres de résultat, et, si cela ne suffit pas, passages choisis du corps. L'agent ne lit pas les commentaires pour trier. Chaque décision de tri est consignée en une ligne (identifiant, décision, motif en dix mots au plus). Limite assumée : un seul lecteur, lecture non intégrale, aucune seconde lecture.

## 6. Billets bien notés
Par année, les candidats sont lus **par score décroissant du site** (`baseScore` ; à égalité, identifiant par ordre lexical). On retient les **15 premiers dont la décision est « oui »**. Si l'année épuise ses candidats avant 15, on retient ce qu'il y a et on le dit.

## 7. Apparié peu noté
Pour chaque billet bien noté retenu, dans l'ordre de leur rang :
- Vivier : billets de la **même année**, candidats au sens du point 4, dans le **tiers bas** des scores de l'année (seuil = score du billet au rang du tiers inférieur parmi **tous** les billets de l'année portant une des neuf étiquettes, comme en v1), partageant **au moins une** étiquette retenue avec le bien noté (« mêmes étiquettes » = recouvrement maximal, comme en v1), de rapport de longueur (mots du site) de **0,67 à 1,5**, non déjà apparié, non déjà lu et jugé « non ».
- Ordre de lecture : d'abord les candidats que le classement automatique de la v1 (script `classer_et_apparier_v1.py`, repris tel quel) rangeait « résultats » — **ordre de lecture seulement, jamais décision** ; puis le plus grand indice de Jaccard des étiquettes retenues, puis le plus petit écart de longueur en logarithme, puis l'identifiant.
- On lit dans cet ordre jusqu'au premier « oui » ; **trois essais au plus** (un essai = un candidat lu pour ce bien noté ; un candidat déjà jugé « non » pour un autre bien noté est sauté sans coûter d'essai). Aucun « oui » en trois essais : le bien noté est **gardé et marqué « sans apparié »**.
- Un candidat jugé « oui » mais non pris reste disponible pour les billets suivants.

## 8. Commentaires
Pour chaque billet bien noté : les dix commentaires au plus haut score (vue `postCommentsTop`), réponses comprises, texte hors dépôt.

## 9. Partage
Graine neuve consignée ici avant le tirage : `numpy.random.SeedSequence(0x7A1C0DE2_2026_1118_0B2)`, un enfant par année (`spawn`), `default_rng` ; unité de partage = la paire (bien noté, apparié, commentaires) ; strates = année × (avec apparié / sans apparié), donc stratifié par année et par classe ; chaque strate coupée en deux moitiés, la moitié en plus d'une strate impaire tirée au hasard. Moitié « développement » et moitié « tenue à l'écart » ; le dossier de la seconde est rendu illisible (`chmod 000`) après le partage et n'est plus ouvert par le trieur. Limite : sous le compte administrateur du conteneur, `chmod` n'est qu'une barrière de convention, pas une garantie technique.

## 10. Mesures rapportées
Décomptes par année ; candidats écartés mécaniquement ; candidats lus et écartés à la lecture (taux = « non » sur lus) ; billets sans apparié ; essais d'appariement ; limites.
