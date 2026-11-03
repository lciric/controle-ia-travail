# Classement K — question 2 de Jan Hendrik Kirchner — classeur neuf D, v1

Classeur neuf (Claude), sans recherche, aveugle à la provenance et aux témoins ; début 12:46:28, notes écrites 12:58:01, jugements 13:02:22 à 13:04:40, script lancé 13:07:45 (heures UTC, temps universel coordonné, toutes par `date -u`). Consigne `prompts-sous-agents/kirchner-classeur-D-v1.md` (`01087807…87777`, vérifiée avant lecture). Protocole Kirchner v1 (`68919ec9…0a781`), sections 0, 2, 3 ; protocole Heimersheim v1 (`942b9324…`), section 5 ; Heimersheim v2 (`cfff33cf…`) lue pour vérifier qu'elle ne touche pas l'étape D (elle ne la touche pas). Entrées vérifiées : fiches `41a5b0b5…802b6` (16 fiches), moisson `79ca608e…a151e` (16 entrées), pièce Kirchner v2 `6e7fb1c5…203f5`. Non ouverts : le manifeste du mélange (il pourrait porter la permutation ou les témoins), les moitiés de moisson, et tout ce que la consigne interdit.

Question gelée des comparaisons : « laquelle ferait une réponse à cette question de Kirchner plus juste, plus originale et plus mémorable pour lui, sur ces quatre critères ? »

## 1. Ordre final (forces de Bradley-Terry, estimation régularisée déclarée, α = 0,5)

| Rang | Fiche | Victoires sur 22 | Log-force | Force | Notes (sous-estimé / lien Kirchner / faisable / résultat d'avance) | Somme | Rang par somme | Drapeau devant Kirchner |
|---|---|---|---|---|---|---|---|---|
| 1 | KM-15 | 22 | 1,730 | 5,642 | 2 / 3 / 2 / 3 | 10 | 1 | non |
| 2 | KM-03 | 20 | 1,352 | 3,864 | 1 / 3 / 2 / 3 | 9 | 6 | **oui** |
| 3 | KM-11 | 18 | 1,018 | 2,768 | 1 / 3 / 2 / 3 | 9 | 7 | non (réfutation partielle proposée, en attente) |
| 4 | KM-13 | 16 | 0,712 | 2,037 | 2 / 3 / 2 / 0 | 7 | 11 | non |
| 5 | KM-05 | 13 | 0,280 | 1,323 | 1 / 3 / 3 / 3 | 10 | 2 | **oui** |
| 6 | KM-07 | 13 | 0,280 | 1,323 | 2 / 1 / 3 / 3 | 9 | 4 | non |
| 7 | KM-02 | 10 | −0,139 | 0,870 | 2 / 1 / 3 / 3 | 9 | 3 | non |
| 8 | KM-12 | 8 | −0,421 | 0,656 | 2 / 1 / 3 / 3 | 9 | 5 | non |
| 9 | KM-01 | 6 | −0,711 | 0,491 | 1 / 3 / 1 / 2 | 7 | 12 | **oui** |
| 10 | KM-16 | 4 | −1,018 | 0,361 | 0 / 3 / 3 / 3 | 9 | 8 | non (réfutation partielle proposée, en attente) |
| 11 | KM-14 | 2 | −1,352 | 0,259 | 1 / 1 / 3 / 3 | 8 | 9 | **oui** (réfutation partielle proposée, en attente) |
| 12 | KM-08 | 0 | −1,730 | 0,177 | 0 / 2 / 3 / 3 | 8 | 10 | **oui** |

KM-05 et KM-07 sont à égalité exacte (13 victoires, même force) : départagées par la règle déclarée avant le calcul (ordre des sommes : somme, puis premier critère, puis deuxième), KM-05 avant KM-07. Hors des douze (classées, non comparées) : KM-04 et KM-06 (somme 6), KM-09 et KM-10 (somme 5).

Ce que les paires changent à l'ordre des sommes : les deux fiches « déjà fait » et les analogies sur l'organisme reculent (KM-16 de 8 à 10, KM-02 de 3 à 7, KM-12 de 5 à 8) ; les fiches qui mesurent un instrument de Kirchner montent (KM-03 de 6 à 2, KM-11 de 7 à 3, KM-13 de 11 à 4, malgré son manque) ; KM-05, deuxième par somme, tombe à 5 (prémisse que son texte désamorce).

## 2. Cohérence et contrôles

- **Cohérence : 65 paires sur 66 concordent dans les deux ordres, soit 0,985.** Seule discordante : KM-05 contre KM-07 (rang 19 : KM-05 présentée en premier, gagne ; rang 66 : KM-07 présentée en premier, gagne) — les deux fois le premier présenté, signe de primauté sur la paire la plus serrée.
- **Réserve (consigne) : cohérence presque parfaite d'un juge unique.** Les deux ordres n'ont pas été jugés à l'aveugle l'un de l'autre : j'ai préparé les 132 jugements dans ma réflexion, dans l'ordre tiré, avant d'écrire le premier lot, puis je les ai écrits en 11 lots de 12 (13:02:22 à 13:04:40) ; « au fur et à mesure » vaut donc au grain du lot. La cohérence mesure ici la stabilité de mes préférences, pas l'absence de biais d'ordre.
- Biais de position : 67 victoires sur 132 pour le premier présenté (0,508) ; l'écart à 66 vient tout entier de la paire discordante.
- Aucune triade cyclique dans la relation de majorité.
- Maximum de vraisemblance simple **inexistant** (KM-15 gagne ses 22 jugements, KM-08 les perd tous ; composantes fortes : onze singletons et {KM-05, KM-07}) : les forces rapportées sont l'estimation régularisée déclarée d'avance (0,5 victoire fictive par sens et par paire). Leur ampleur dépend de α (log-force de KM-15 : 4,37 à α = 0,1 ; 1,73 à 0,5 ; 1,09 à 1) ; seul l'ordre est solide. Plan équilibré : l'ordre des forces suit exactement celui des victoires (garde vérifiée par le script).
- **Défaut du contrôle de sensibilité de la v1** : la sortie dit « ordre identique pour tous les alpha : faux ». Vérifié à part (calcul non écrit) : le seul écart est l'interversion de KM-05 et KM-07 à α = 0,1, à l'intérieur de leur égalité exacte (différence de log-force de 6,7 × 10⁻¹⁶) ; hors de cette égalité, l'ordre est identique pour α = 0,1, 0,5 et 1. Le contrôle comparait des tris bruts sans tolérance ; à corriger dans une v2 s'il est gardé (comparer à égalité de victoires près).
- Gardes du script éprouvées avant tout calcul (16 épreuves, toutes tenues) : cas sain simulé (corrélation de rang 0,832 avec les forces vraies, maximum de vraisemblance trouvé en 96 itérations) ; deux cas connus (rapport 3 pour 3 victoires contre 1 ; forces égales sur un cycle symétrique) ; artefacts arrêtés : ligne manquante, ligne en double, lignes interverties, gagnant hors de la paire, paire deux fois dans le même ordre, position du gagnant fausse, coupure dans une égalité, séparation parfaite sans régularisation, non-convergence, empreinte fausse, note hors de 0 à 3.

## 3. Porte et manques

- Les seize fiches sont dans le sujet (section 2 du protocole) : douze portent sur un instrument de Kirchner (classement, moniteur de triche, banc tenu à l'écart, garde de capacité, Petri, forum, remède déclaré) ; quatre (KM-02, KM-07, KM-12, KM-14) répondent à la question par analogie sur l'organisme. Aucune hors sujet.
- Aucune réfutée. Trois portent une **proposition de réfutation partielle laissée au directeur** par la moisson : KM-11 (arXiv:2608.16190, « Pretraining lineage … does not pay »), KM-14 (Roelofs et coll. 2019 ; arXiv:2603.26499), KM-16 (billet LessWrong qnrjAhiqire7JeoN2, validité de la mesure). Gardées et classées ; si KM-11 tombe, le rang 3 se libère.
- Manque commun, de forme : aucune fiche ne dit en propre pourquoi son problème serait sous-estimé (l'étape A n'a pas ce champ) ; le premier critère, tiré de la moisson, en tient lieu.
- Résultat qui ferait changer d'avis **absent** (champ vide) : KM-04, KM-06, KM-09, KM-10, KM-13 ; noté 0, jamais complété. Seule KM-13 est dans les douze (rang 4).
- Autres manques : KM-01 n'a pas de première expérience unique (une liste d'épreuves) et ne donne le résultat qui la ferait changer d'avis que pour quelques instruments ; KM-04 et KM-06 sans durée ni coût ; KM-09 sans durée ; KM-10 sans seuil, durée ni coût ; KM-13 sans seuil, protocole non réécrit en entier.

## 4. Notes des seize fiches (raisons ligne à ligne dans `notes-K-v1.json`)

| Rang par somme | Fiche | Moisson | Sous-estimé | Lien Kirchner | Faisable en jours | Résultat d'avance | Somme |
|---|---|---|---|---|---|---|---|
| 1 | KM-15 | voisin lointain, compte 0 | 2 | 3 | 2 | 3 | 10 |
| 2 | KM-05 | voisin proche, compte 1 | 1 | 3 | 3 | 3 | 10 |
| 3 | KM-02 | voisin lointain, compte 0 | 2 | 1 | 3 | 3 | 9 |
| 4 | KM-07 | voisin lointain, compte 0 | 2 | 1 | 3 | 3 | 9 |
| 5 | KM-12 | voisin lointain, compte 0 | 2 | 1 | 3 | 3 | 9 |
| 6 | KM-03 | voisin proche, compte 0 | 1 | 3 | 2 | 3 | 9 |
| 7 | KM-11 | voisin proche, compte 1 | 1 | 3 | 2 | 3 | 9 |
| 8 | KM-16 | déjà fait (arXiv:2510.20270), compte 2 | 0 | 3 | 3 | 3 | 9 |
| 9 | KM-14 | voisin proche, compte 2 | 1 | 1 | 3 | 3 | 8 |
| 10 | KM-08 | déjà fait (arXiv:2603.04582), compte 1 | 0 | 2 | 3 | 3 | 8 |
| 11 | KM-13 | voisin lointain, compte 0 | 2 | 3 | 2 | 0 | 7 |
| 12 | KM-01 | voisin proche, compte 2 | 1 | 3 | 1 | 2 | 7 |
| 13 | KM-04 | voisin proche, compte 0 | 1 | 3 | 2 | 0 | 6 |
| 14 | KM-06 | voisin proche, compte 0 | 1 | 3 | 2 | 0 | 6 |
| 15 | KM-09 | voisin proche, compte 1 | 1 | 3 | 1 | 0 | 5 |
| 16 | KM-10 | voisin proche, compte 1 | 1 | 3 | 1 | 0 | 5 |

Égalités départagées par le premier critère, puis le deuxième. La coupure des douze tombe entre 7 et 6, hors de toute égalité ; les égalités restantes (KM-02, KM-07, KM-12 ; KM-03, KM-11 ; KM-04, KM-06 ; KM-09, KM-10) ne sont départagées ni par le premier ni par le deuxième critère, ni même par les deux autres : elles sont rangées par identifiant, sans portée, puisque l'ordre final vient des paires. Aucune fiche n'a 3 au premier critère (aucune « ouverte » après moisson).

## 5. Drapeaux de risque devant Kirchner (affirmation qu'il pourrait contredire de ses propres textes)

Appuis : la pièce servie et les lectures de 2608.28945 rapportées par la moisson, toutes non opposables (lecture par questions ciblées, annexes F et G non lues) ; chaque drapeau est à revérifier sur la source avant d'écrire.

- **KM-03 — oui.** La fiche dit son remède « contredit par simple sélection » en cas d'absence de transfert ; or le remède est intitulé « Training AARs to be more monitorable » : il peut répondre de son texte qu'il parle d'entraînement, que la fiche laisse elle-même à tester. L'expérience reste bonne ; c'est la conclusion qu'il faut borner.
- **KM-05 — oui.** Le mécanisme s'appuie sur les 26 relances sur 39 signalements, que son texte décrit comme des triches prises par son moniteur après coup et visant un score chanceux, non la garde ; et sa garde est dite faite pour « rule out a collapse rather than certifying that capability is unchanged ».
- **KM-01 — oui.** « Validité non mesurée » pour chaque instrument : son article rapporte la généralisation des gagnants au banc tenu à l'écart, à Petri et à des modèles plus grands, et le lien classement-Petri de l'annexe D.3 ; la garde n'est pas faite pour des baisses de 2 points ; le banc tenu à l'écart est isolé « by the operating system rather than by trust ».
- **KM-14 — oui.** Le mécanisme suppose un proposeur qui choisit d'après les verdicts du banc fixe ; son banc tenu à l'écart « is never shown to the AAR » et sert une fois à « pick the one that scores highest » : la réutilisation adaptative par les agents est exclue par construction (reste la multiplicité du choix final). L'analogie irait mieux à son chercheur faible-vers-fort d'avril (soumissions illimitées à un service distant qui renvoie la fraction d'écart comblé).
- **KM-08 — oui.** Son moniteur avant exécution « reads the actual code » et la relecture après coup lit chaque trajectoire signalée en entier : aucun ne juge l'action comme son propre tour ; l'effet mesuré ne touche pas son dispositif actuel (la fiche le limite elle-même à un contrôle placé dans la boucle de l'agent). De plus, déjà publié (Khullar, Hopkins, Wang, Roger).
- Non, avec une note : KM-15 (conteste sa lecture de « Only one reached the top three » sans la déformer) ; KM-11 (rien dans ses textes, mais réfutation partielle en attente) ; KM-13 (prémisse tirée de son texte ; les « environ 200 exemples par banc » viennent d'un lecteur précédent) ; KM-16 (vérifier que le harnais ouvert faible-vers-fort a des tâches de code à tests unitaires) ; KM-12 (ses agents doivent connaître les interdits : le bras « opaque » n'a pas d'équivalent direct) ; KM-02 (son harnais n'a ni nulle ni juge statistique) ; KM-10 (annexes F et G non lues) ; KM-04, KM-06, KM-07, KM-09.

## 6. Règles de lecture fixées avant de noter (détail dans `notes-K-v1.json`)

1. Premier critère tiré de la seule moisson (classe, distance, compte) ; aucune connaissance propre du classeur, pour ne pas fausser le contrôle par les témoins.
2. Deuxième critère : 3 = mesure neuve d'un instrument de Kirchner, ou d'une réplique qui le reproduit, absente de ses textes ; 2 = se sert d'un tel instrument sans mesure neuve de l'instrument tel qu'il est construit ; 1 = cite, ou transpose par analogie sur l'organisme ; 0 = sans lien.
3. Troisième critère : la version décisive fait la note quand une fiche fusionne des versions de coûts très différents.
4. Quatrième critère : seul le champ « résultat qui ferait changer d'avis » ; vide = 0, la mesure qui tue n'est pas substituée.

## 7. Réserves

1. **Juge unique, cohérence presque parfaite (0,985)** : voir section 2 ; les deux ordres ne sont pas indépendants.
2. **Lecture du quatrième critère** : la lecture inverse (mesure qui tue à la place d'un champ vide) change la composition des douze : KM-04 et KM-06 entreraient, KM-01 et KM-08 sortiraient (dix sur douze communes). Le bas de l'ordre final est sa partie la plus fragile.
3. **Troisième critère de KM-04 et KM-06** : notés 2 ; à 3, la coupure des douze tomberait dans une égalité (KM-01, KM-04, KM-06 à somme, premier et deuxième critères égaux) que le protocole ne départage pas.
4. **Premier critère hérité de la moisson** : métadonnées et résumés seulement, non opposable ; OpenAlex refusé pour toute la session de moisson ; pour KM-15, le billet le plus proche par le titre (LessWrong moDKmh4GerCjfB5mM) n'a pas pu être ouvert ; pour KM-03, le moissonneur laisse au directeur une lecture « voisin lointain » (somme 10, sans effet sur la composition ni, vraisemblablement, sur le rang 2).
5. **Analogies notées 1 au deuxième critère** (KM-02, KM-07, KM-12, KM-14) : à 2, aucune entrée ni sortie des douze.
6. **Forces** : ampleur dépendante de α ; seul l'ordre est à lire. Contrôle de sensibilité de la v1 défectueux (section 2), sans effet sur l'ordre.
7. **Drapeaux** fondés sur des lectures non opposables de ses textes (R7) : à vérifier en source primaire, page citée, avant toute phrase de Lazar.

## 8. Fichiers (dossier `/home/claude/scratch/kirchner-rapport/classement-D/`)

| Fichier | sha256 |
|---|---|
| `notes-K-v1.json` | `2a96d25fd5d1f6928c979bd738eb8bb5162acc5b70186995f11a681182643ccb` |
| `paires-K-v1.jsonl` (132 jugements, ordre du tirage, e = 4730381279323388710) | `3177697a574de1fa51bd3ec812cbc5090a7384c22fd4d9859a94c46f037c480c` |
| `bradley_terry_kirchner_v1.py` | `40785df9dd663d14008f60631c7ebe595218cc6157b491fe688bee7edce068e3` |
| `bradley_terry_kirchner_v1-sortie.json` (Python 3.13.18, numpy 2.5.3) | `7b11edb4c65a8163f70e50fedbc736856048b1aeb46450aa9afba60f50250eb7` |
| `classement-K-v1.md` (ce fichier) | donnée dans la réponse du classeur |

Aucun compagnon `.sha256` écrit (interdit par la consigne) ; aucun fichier existant modifié ; aucun `git`, aucune recherche, aucun appel de modèle.
