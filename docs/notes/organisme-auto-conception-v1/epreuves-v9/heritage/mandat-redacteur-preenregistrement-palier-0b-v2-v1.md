# Mandat du rédacteur — épreuve sur l'héritage, préenregistrement du palier 0b, version 2 — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-19 vers 16:35Z. Mandats : GO-2026-11-19-71, -75, -76 et -77 (main, `registres/go.md`, commit `2ec5da6c` ou suivant) ; mot de la mère vers 16:33Z sur deux ajouts.

## Ce que tu fais

Tu écris la version 2 du préenregistrement de l'étage sur processeur (palier 0b). La version 1 reste intacte (R12). La version 2 se vérifie sur son différentiel.

1. **Les onze corrections** de la contre-lecture `heritage/palier-0b/contre-lecture-preenregistrement-palier-0b-v1-v1.md` (`127aa59f…`), toutes, et ses points de forme. Les deux majeures d'abord :
   - la part de l'écart portée par les lois dépendantes, M10, devient D / (D + max(I, 0)), et le pronostic du point 6 suit ;
   - le repli du point 7 se mesure à effort égal : un nombre fixe K de paires examinées par génération, le même au repli ; rapporter le facteur d'enrichissement ; dire que R est une propriété du banc ; la ligne « tenue sous le repli » est retirée parce qu'elle est sans objet par construction.
   Si un calcul change, écris un calcul versionné neuf (`calcul_ordres_de_grandeur_palier_0b_v2.py`), joue-le deux fois et compare les sorties à l'octet.
2. **Les trois décisions de Lazar sur ce palier** (GO-2026-11-19-77, option (a) chaque fois) : lecteur témoin réel au seul palier 1, puis décision, sans dépense engagée ici ; une tenue « établie » se dit « servir un registre tenu, forme comprise » ; engagements à forme imposée aux paliers payants. Ajoute les deux phrases du contre-lecteur sur la décision 3 : avec la forme imposée, la loi est dans le texte du test, donc la raison du plan pour servir la description tombe ; et l'expérimentateur modèle gardé par GO-2026-11-19-75 n'a plus qu'un script fixe à lancer. Dis ce que cela change, sans revenir sur GO-75.
3. **Deux ajouts accordés par la mère** :
   - le bras de diagnostic « registre d'une autre source » (plan v5, § 9), joué sur processeur contre le suiveur de forme à la lettre, **rapporté sans critère** ;
   - la puissance du seul contraste de l'héritage, **rapportée comme information, sans critère**, sans toucher à la décision du nœud 4 (deux contrastes décisifs). Écris d'avance la condition du devis v5 (§ 9, nœud 4) qui ferait changer cette recommandation : une table du palier 0b où deux contrastes demandent beaucoup plus de sources qu'un seul. Chiffre « beaucoup plus » avant tout tirage. Si la table remplit cette condition, la mère repose le nœud 4 à Lazar ; sinon, rien ne change.
4. **Information pour Lazar**, à écrire : le suiveur de forme qui répond à la taille du registre est un écart à la lettre du plan, nécessaire, sans effet sur hypothèse ni revendication.

## Ce que tu lis

`CLAUDE.md` ; dans `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/` : le mandat v1 (`e8eff361…`), le dossier `palier-0b/` (préenregistrement v1 `a7189bbb…`, rapport du rédacteur v1, calcul et sortie, contre-lecture `127aa59f…`, vérifications à la main), le plan v5 (`9085bbe9…`), le devis v5 (`30c87fa6…`), le dossier `palier-0a/` ; sur main : `registres/go.md` (GO-2026-11-19-71 à -77). Vérifie chaque empreinte avant de citer (R6, R11). Aucune carte, rien sous `archives-reponses-modeles/`.

## Ce que tu rends

Dans ton bloc-notes seulement : `preenregistrement-heritage-palier-0b-etage-processeur-v2.md`, le calcul v2 et sa sortie s'il y a lieu, et `rapport-redacteur-palier-0b-v2-v1.md` (correction par correction : où et comment ; les deux ajouts ; ce que tu n'as pas pu faire ; toute décision neuve pour Lazar au format habituel). En-tête : « Auteur : rédacteur neuf, modèle F » ; aucun identifiant de modèle ; heure par `date -u`.

## Interdits

Aucun tirage décisif, aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun réseau sauf `git fetch`/`git show` du dépôt. Aucun commit, aucune poussée, aucune écriture dans le dépôt. Jamais de heredoc. Aucune valeur de clé. Ni « consigne-privee », ni « conception-ii-b », ni `brouillons/ii-b-saboteur-budget-v1/`, ni `lot/compte-4-v1`, ni R-2059, ni `/root/.claude/`. N'écris jamais le nom d'une commande d'arrêt par motif dans une commande : la garde du dépôt la refuse. Au premier refus d'un outil : arrête-toi et dis-le.
