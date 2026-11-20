# Contre-lecture des deux instruments de la mère — complément 1 : la preuve par le code que les deux fiches retenues sont absentes du fichier des cartes

Même contre-lecteur que la pièce `e76981b9…` (Claude Fable 5.2, `claude-fable-5-2`), 20 novembre 2026. Pièce de travail. Même mandat (`da74088f…`), mêmes règles, étendu par la mère aux trois fichiers nommés ci-dessous.

## Verdict : la preuve ne suffit pas

La thèse tient sur toutes les lignes que j'ai lues, et je n'y ai trouvé aucun chemin qui la contredise. Elle ne suffit pas comme preuve, parce que deux fichiers de la chaîne d'héritage de la génération jouée n'ont pas été lus, et parce que deux chemins de second classement ne sont pas fermés par les lignes lues. La vérification par programme demandée à l'organisme (intersection vide, sur les identifiants) reste nécessaire ; à défaut, la preuve se complète par trois lectures courtes, listées en fin de pièce.

## Ce que j'ai lu

Dépôt de l'orchestrateur au commit `a41b7b50…`, par plages de lignes (`git blame -s -L`, lecture seule) :
- `orchestrator/pole/noyau_v54.py`, l. 215 à 275 : l'aiguilleur de la version 54 (`AiguilleurV54`) ;
- `orchestrator/pole/course2_v54.py`, l. 140 à 220 et 395 à 410 : la fabrication des fiches, `_aiguiller`, ses appels ;
- `orchestrator/pole/course2_v56.py`, l. 225 à 268 et 340 à 370 : `lot_mesure` et l'écriture de `fiches.json`.

Plus une recherche de motifs bornée à ces trois fichiers, par leur chemin entier (appels de `_aiguiller` et de `classer`, écritures de `passeports`, écritures de `fiches.json`, lignes de classes et d'imports). Les empreintes `14f65569…` et `711a3267…` ne sont pas vérifiées, faute de commande simple sans écriture ; le commit l'est.

## Ce qui tient

1. **`fiches.json` est le lot de mesure.** `course2_v56.py` l. 354 : `lot = self.lot_mesure()` ; l. 366 à 367 : `fiches.json` est écrit à partir de `lot`, et de lui seul. `lot_mesure` (l. 264 à 268) ne garde que les fiches pour lesquelles `self.aiguilleur.a_passeport` est vrai, puis retire les fusions inachevées.
2. **Un passeport n'est donné qu'en un endroit.** Dans les trois fichiers, la seule écriture dans `passeports` est `noyau_v54.py` l. 249, dans `classer`, branche `niveau_methode`. L'autre branche (l. 250 à 253) écrit au journal. Les deux s'excluent pour un appel. `retirer` (l. 266 à 267) ne fait qu'ôter un passeport. `a_passeport` (l. 256 à 258) exige de plus l'empreinte recalculée.
3. **`classer` n'est appelé qu'en un endroit**, `_aiguiller` (`course2_v54.py` l. 169), lui-même appelé quatre fois dans ces fichiers, chaque fois sur des fiches qui viennent d'être fabriquées : première passe (l. 196), seconde passe (l. 216), fusions (v54 l. 405, v56 l. 232).
4. **`fiches.json` n'a pas d'autre écrivain dans ces trois fichiers** que l'ancien `executer` de la version 54 (l. 437), remplacé par celui de la version 56.
5. Le journal réel porte les huit clés qu'écrit `AiguilleurV54` (sans `passe`) : c'est bien cette classe, ou une classe fille, qui l'a écrit.

## Ce qui manque

1. **Deux fichiers de la chaîne ne sont pas lus.** La génération jouée est `GenerationV56(OrchestreV56, c55.GenerationV55)` (`course2_v56.py` l. 163) : elle hérite de `noyau_v56.py` et de `course2_v55.py`, et ses étapes sont celles de la version 55 (`ETAPES = c55.ETAPES`, l. 33). L'un ou l'autre peut redéfinir `_aiguiller`, une étape, l'aiguilleur lui-même, ou la manière de rejouer une étape. La thèse « chaque fiche n'est classée qu'une fois » et « aucun passeport ailleurs » n'est donc établie que pour trois fichiers sur cinq.
2. **Le rejeu d'une étape.** Les lignes lues parlent d'étapes « coupées par leur relais » et de « rejeu de la seule mesure non mesurée ». `jouer_etape` n'est pas dans les plages lues. Si l'étape d'aiguillage peut être rejouée sur la même liste, une fiche retenue au premier passage peut recevoir un passeport au second : elle serait alors au journal et dans `fiches.json`, sans doublon au journal.
3. **La collision d'identifiants.** L'identifiant d'une fiche est un jeton opaque de 6 signes (`course2_v54.py` l. 155), et `self.fiches[ident] = f` (l. 162) écrase sans contrôle. Deux fiches au même jeton, l'une retenue, l'autre passée, mettraient l'identifiant retenu dans `fiches.json`. C'est très peu probable pour une centaine de fiches, mais les lignes lues ne l'interdisent pas, et l'arithmétique 96 = 94 + 2 ne le voit pas.

## Remarque sur `cartes_attendues` = 94

Le nombre de cartes de `fiches.json` n'est pas le nombre de passeports : `lot_mesure` retire les fusions inachevées, et `retirer` ôte des passeports. Le « 94 » du manifeste doit être le compte des clés de `fiches.json`, obtenu par programme (un entier, sans lire une carte), et non déduit des passeports du journal. S'il vient déjà de ce compte, rien à changer.

## Pour fermer la preuve, au choix

- La voie directe, déjà demandée à l'organisme : un programme qui lit les seules clés de `fiches.json`, rend leur nombre et le booléen « les deux identifiants retenus en sont absents », et rien d'autre. Elle ferme les trois points d'un coup et remplace la preuve par le code.
- Ou, par le code seul : la même recherche de motifs sur `course2_v55.py` et `noyau_v56.py` (aucun autre appel de `classer` ou de `_aiguiller`, aucune écriture de `passeports`, aucun autre `fiches.json`), la lecture de `jouer_etape` (une étape jouée n'est jamais rejouée dans une même génération), et un contrôle que les identifiants fabriqués sont tous distincts (par exemple, le compte des fiches fabriquées égal au compte des identifiants). Sans le troisième contrôle, il reste le risque de collision, faible mais non nul.

## Ce que je n'ai pas fait

Rien ouvert sous `archives-reponses-modeles/`, ni `fiches.json`, ni aucune carte ; rien lu du dépôt de l'orchestrateur hors des trois fichiers nommés ; aucun identifiant de carte recopié ; aucun refus d'outil.
