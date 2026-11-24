# Contre-lecture de l'ordre de la passe du versant honnête (Opus 5.5 neuf) — v1

**Attestation** (`date -u` : Tue Nov 24 16:49:11 UTC 2026). Je n'ai lu aucun épisode, score, sortie de course, diagnostic, verdict ni lecture. Rien sous `coffre/`. Fiche des sondes non ouverte. Je n'ai écrit aucune des pièces. Aucun fichier du dépôt modifié. Pièce : `f6d7f0c2…`, égale à son compagnon.

## Verdict : lançable après corrections (et remplissage des trois marqueurs)

**Valeurs conformes** à leur source et à leur ligne : machine, filtre, coupure 11 (arrêt à 10,60), horloge 6 h 15, plafond 12, relance si d ≤ 5,5, comptes, clé `garde-1/tirage`, entropie, tolérance 0,2, réglages.

**Empreintes recalculées, toutes égales** : texte, errata, réglages, `activations.py` (trois commits), entrées sur leurs branches, attestation de séparation. `origin/main` a avancé (789f6de2) sans les changer.

## Défauts

1. **Majeur (§ 2.2, § 5.4).** « À la barrière : versement, destruction » contredit « versement non relu : instance non détruite ». À 11 dollars, l'exécutante n'a pas de règle.
   - Correction : le code ne garde aucune activation brute hors de la garde (donc pas de lot lourd). Le lot léger est versé et relu dès la fin du pas H.
   - Sinon, la mère ou Lazar tranche : arrêt sans destruction, ou dépassement dans le cumul de 12.
2. **Moyen (§ 2.2).** Aucun mécanisme de surveillance : si la session qui pilote s'interrompt, aucune barrière ne joue.
   - Correction : surveillance en arrière-plan qui détruit par identifiant, plus un réveil programmé.
3. **Moyen (§ 1.5).** Le décodage avant création, sur processeur, exige le jetoniseur, donc le jeton d'accès, que le devis (ligne 35) ne loge que sur l'instance.
   - La mère décide où le loger ; ajouter la garde « versions-jetonisation » de la note de forme.
4. **Moyen (§ 6.5).** Au commit 8e074634, `analyser` exige `--liste-blanche`, `--entropie` et `--sortie`. Il prend aussi `--point-4`, `--etape0` et `--passe-non-livree`.
   - Correction : fixer `--entropie 332543941018745695594892624416682421756`, `--point-4 a` (texte, ligne 16), `--etape0 tenue` ; interdire `--reduit` ; sortie hors de l'arbre ; donner la commande du repli (ligne V1).
5. **Moyen (§ 1.1).** Deux prérequis du devis ne sont pas vérifiés : le devis v2 et son erratum scellés (§ 4, point 5) ; le texte des sondes lu (§ 4, point 2).
6. **Moyen (§ 4 et § 4.1).** « Trace sans texte », mais les actions régénérées, du texte, sont versées.
   - Correction : verser ces actions, et les scores non livrés du § 4.5, sur une branche distincte.
7. **Mineur.** « Session qui pilote » et « exécutante » : l'ordre ne dit pas si c'est la même session. À nommer.
8. **Mineur (§ 1.2).** Le marqueur des tables porte aussi la sortie scellée de l'étape 0, postérieure au scellement, à graines neuves.

## Marqueurs

- **`TABLES_ETAPE0_VH`** : bien posé (texte, lignes 205, 296, 307 et 308).
- **`CODE_PASSE_VH`** : bien posé. Ajouter : persistance et taille des activations, versions du jetoniseur, surveillance de la dépense.
- **`PREPARATION_LECTURE_VH`** : fondé. Le texte, ligne 192, nomme une préparation des quatre entrées ; le code d'analyse n'a que `factice`, `analyser` et `etape0`. Il bloque la lecture, pas la création.

## Tri des dix-huit points ouverts

| catégorie | points |
|---|---|
| bloquent la création | 1, 2, 8 (10 avec lui), 7 ; 3 et 16 tant qu'ils ne sont pas au marqueur |
| décisions de la mère | 5 (commit de lancement issu d'`origin/main` ; étiqueter 8e074634), 6, 7, 9, 11, 12, 17 |
| décision de Lazar | 8, si la coupure ou le cumul change |
| se règlent par le code de la passe | 2, 3, 10, 13, 14, 15, 16 |
| bloque la lecture seulement | 4 |
| à faire par l'exécutante | 18 |

**Barrière de dépense avant la fin du versement** : supprimer le lot lourd plutôt qu'arrêter l'instance sans la détruire. Non vérifié : ce que le loueur facture sur une instance arrêtée.

**Scores restés sur disque quand une garde tardive échoue** : le versement à part concilie « récupérer ce qui est récupérable » et « aucune livraison », à trois conditions : une branche distincte, le refus de ces fichiers par la liste blanche, une décision de la mère consignée.

Mieux : exiger le pas G (sur les 192 actions) avant le pas F, si G ne compare pas aux scores de mesure.

## Brouillon homonyme

**Le constat est exact.**
- À 8e074634 et en tête de la branche de travail, `prereg/versant-honnete-jumeau-v3.md` est le brouillon `40a7c6ac…`, sans compagnon.
- Sur `origin/main`, le texte scellé est `a505fa4e…`, avec son compagnon.
- À 8e074634, les réglages sont absents.
- 8e074634 n'est pas dans `origin/main`.

**L'arrêt suffit, mais arrêterait aussi un lancement correct.** Le pas 1.1 doit dire de lire le texte sur `origin/main` et nommer `40a7c6ac…` comme le brouillon connu ; le § 6, de même pour le sous-agent du verdict.

## Qui a lu quoi

> 2026-11-24, 16:49Z, Opus 5.5, contre-lecteur neuf.
> - **Lu** : consigne et ordre, en entier ; texte scellé, lignes 1–30, 137–143, 174–226, 290–311 et 363–381, plus sa différence avec le brouillon ; errata 1 et 2 ; réglages ; devis v2 et son erratum ; pièce des empreintes v6 ; note de forme et son erratum (forme seule) ; `CLAUDE.md` ; code v6, lignes 1934–1956 (options) et deux lignes `__file__`.
> - **Noms et empreintes seulement** : entrées sur leurs branches, attestation de séparation.
> - **Rien d'autre** : ni registre, ni fiche des sondes, ni `coffre/`, ni aucun résultat.
