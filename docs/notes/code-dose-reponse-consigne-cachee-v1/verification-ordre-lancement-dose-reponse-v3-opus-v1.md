# Vérification des corrections de l'ordre de lancement de la course de dose–réponse, v3

Contre-lecteur : le même que celui de la v2 (Opus 5.5, sous-agent). Pièce vérifiée : `docs/notes/code-dose-reponse-consigne-cachee-v1/ordre-de-lancement-propose-dose-reponse-v3.md`, arbre au commit 7a13b153.

## Verdict

**Scellable après une seule correction, N1**, donnée mot pour mot ci-dessous, et sous réserve du mot de Lazar sur B1.

Les quinze défauts de la v2 sont corrigés, dont un autrement de façon acceptable (m8).

Les deux branches de B1 sont écrites :
- **(a)**, lancer sans désignation : jouable telle quelle par cet ordre ;
- **(b)**, attendre la désignation : écrite comme le chemin qu'il faudra suivre (amorce v3, essai, commit, ligne CODE et ordre v4). Elle n'est pas jouable avec le code a02b6540, et l'ordre le dit en clair. C'est la seule forme honnête possible.

Contrôles faits :
- empreinte de la v3 : `9e065fdf…c2ee1be`, conforme à son compagnon ;
- `git diff a02b6540 7a13b153 -- src scripts tests .claude pyproject.toml requirements-*.txt` : vide, le code est inchangé.

## État de chaque défaut de la v2

| défaut | état | preuve (lignes de la v3) |
|---|---|---|
| B1, désignation pour le critère 3 | corrigé | l. 20-27 : deux branches au mot de Lazar ; (a) jouable sans `--designation` ; (b) renvoie à une amorce v3 et à un ordre v4, et dit que a02b6540 ne peut pas jouer une course désignée, avec la cause |
| B2, déclaration de la session de lancement | corrigé, avec un garde-fou ajouté | l. 11-16 : pièce et ligne `DECLARATION-LANCEMENT-DOSE-REPONSE-CONSIGNE-CACHEE` ; vérification à la main par `grep` (l. 47). Ce `grep` ne stoppe rien en l'état : voir N1 |
| M1, jeton GitHub `_3`, repli `_2` | corrigé | l. 58, 62, 66, 78 : export en tête de chaque appel ; repli décrit |
| M2, lecture des sorties de la surveillance, arrêt, versement, destruction | corrigé | l. 86-93 : les trois cas, redémarrage pour récupérer, nœud au bout de 6 heures, destruction par l'identifiant après le versement prouvé, registre des arrêts et des dépenses |
| M3, tenue de la surveillance sur 24 heures | corrigé | l. 84 |
| M4, commandes à trous | corrigé | l. 44-49 : branche et chemin de la banque écrits ; empreinte attendue (l. 18, 54) |
| m1, classe de la pièce | corrigé | l. 5 : classe A |
| m2, paquets de la session | corrigé | l. 31 |
| m3, arbre de travail dédié | corrigé | l. 39, 42-43 |
| m4, fin de l'accord de dépense | corrigé | l. 33 |
| m5, dépassement du plafond | corrigé | l. 95 |
| m6, douze recherches d'offre | corrigé | l. 72 |
| m7, reprise | corrigé | l. 99 |
| m8, `--dossier` en reprise | corrigé autrement, acceptable | voir ci-dessous |
| m9, appels du terminal sans état | corrigé | l. 35, et les blocs des sections 2 et 3 |

**Pourquoi m8 est acceptable.** Je l'ai vérifié dans le code :
- `course_v2.reprendre` (l. 282-308) recopie chaque bloc scellé de la tentative antérieure dans `<dossier neuf>/blocs/`, puis contrôle la copie à l'octet. Le dossier de la dernière tentative porte donc tous les blocs, y compris ceux d'une chaîne de reprises.
- `lecture_v2.charger_course` (l. 495-516) lève « bloc … en double » si le même nom de bloc apparaît dans deux dossiers. Répéter `--dossier`, comme je le proposais, aurait arrêté la lecture.
- Ma correction était fausse ; celle de l'auteur est la bonne. `--resultat-course` de la dernière tentative est cohérent.

## Défauts neufs

**N1 (majeur) : le garde-fou de la déclaration ne stoppe pas le bloc de commandes.**

Passage (l. 47) : `grep -q '^| DECLARATION-LANCEMENT-DOSE-REPONSE-CONSIGNE-CACHEE ' registres/scellements-v1.md || { echo "préalable 1 bis absent : aucune création"; false; }   # arrêt : ne rien jouer de plus`.

Joué dans un seul appel du terminal, sans `set -e`, `false` n'interrompt rien. Le script de configuration, le commit et la poussée de la branche de lancement s'exécuteraient quand même. Une commande qui échoue plus haut, un `git fetch` par exemple, passerait aussi sans arrêt.

C'est le seul garde d'une condition d'arrêt du texte scellé que le code ne contrôle pas.

Correction mot pour mot :
1. Insérer en première ligne du bloc de la section 1 : `set -euo pipefail`.
2. Remplacer `false; }` par `exit 1; }` à la ligne 47.
3. Ajouter, en tête des deux appels de la section 2, juste après `cd <bloc-notes>/lancement-dr` : `&& grep -q '^| DECLARATION-LANCEMENT-DOSE-REPONSE-CONSIGNE-CACHEE ' registres/scellements-v1.md`.

**N2 (mineur) : attendre la destruction avant de rejouer la création.**

Après un refus de l'amorce (clonage ou poussée), l'ordre dit de rejouer `creation`. Or le lanceur refuse, en nœud, toute création tant qu'une instance porte l'étiquette du programme (`instances`, l. 147 du lanceur).

Ajouter à la l. 58, après « se détruit seule en 3 minutes environ » : « ; attendre que `timeout -k 5 120 vastai show instances` ne la liste plus (au plus 40 minutes, sinon destruction par l'identifiant après relevé de la branche), avant de rejouer `creation` ».

**N3 (mineur) : le versement du résultat de la lecture n'est pas écrit.**

La section 5 écrit le résultat dans l'arbre de travail de la branche de sortie, sans dire où il est committé, scellé et poussé.

Ajouter après le bloc de la section 5 : « Le résultat `diag/<run lecture>/` (manifeste et `lecture-cout-dose-reponse.json`, scellés) est committé et poussé sur la branche de sortie de la dernière tentative, puis versé sur main par la mère ; aucune seconde lecture. »

**N4 (mineur, aucune action exigée) : chemin de l'environnement.**

`<chemin de l'environnement>` reste un trou : le préalable 5 crée `.venv` sans dire dans quel dossier. Suggestion : « `<bloc-notes>/venv-dr` », créé une fois au préalable 5.

## Cloisonnement

Je n'ai ouvert aucune pièce privée et lu aucune sortie de course, aucun score, aucun verdict. Rien n'est modifié, poussé, lancé ni loué.
