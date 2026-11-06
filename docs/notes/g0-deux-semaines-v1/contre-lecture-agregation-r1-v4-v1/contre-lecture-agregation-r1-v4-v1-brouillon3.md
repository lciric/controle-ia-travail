# Contre-lecture neuve (R2) du préenregistrement « agrégateurs sur les scores réels de R1 v4 » — vérification du delta : brouillon 3 et code `1fcb23d7` — v1

**Verdict : scellable après un couple résiduel** (`couples-contre-lecture-agregation-r1-v4-v1-brouillon3.json`, borne d'union). Le code v3 fait Q1 à Q4 ; les artefacts R5 « non scellé » et « arbre sale » sont éprouvés. 41 essais sur 41 passent. Opposabilité tenue.

- Lecteur : fille 9 (lignée Claude Opus 5.5, même modèle que l'autrice). 6 novembre 2026, de 12:36 à 12:41 UTC (`date -u`). Aucune sortie de R1 ou R2 lue ; rien sous `runs/`, `diag/`, `donnees/`.
- Pièces : branche `prep/fille-11-agregation-v1` à `3a575d1c`. Empreintes recalculées et égales à celles de la consigne : brouillon 3 `24802894…`, couples `3049c681…`, rapport `4b67b462…`, `analyse_v3.py` `75c0d219…` (commit `1fcb23d7`).
- Ce rapport complète les deux précédents (`contre-lecture-agregation-r1-v4-v1.md`, `…-brouillon2.md`), qui restent tels quels.

## 1. Mes 12 couples sur le brouillon 2 (`eb8ff666…`) : sont-ils dans le brouillon 3 ?

Vérifié par script (texte « nouveau » cherché mot pour mot), puis à la main pour les écarts.

| couple | objet | brouillon 3 |
|---|---|---|
| 1 | δ_k ≥ 0 est une hypothèse | présent |
| 2 | transposition « budget, puissance » → « décalage, aire » | présent |
| 3 | plage de C3 (a_W ≥ 0,75) | présent |
| 4 | plage de C2 (a_W ≥ 0,9) | présent |
| 5 | conduite au plafond | présent (l. 164), et la règle de lecture le reprend (l. 327, appliquée par `lire_hag`) |
| 6 | trou de la table des issues | présent |
| 7 | « appui partiel » accordé à `lire_hag` | présent |
| 8 | appariement des hybrides, dépendance intra-épisode | **différent, contenu présent ailleurs** : 9 actions sur 10 partagées (l. 123, « ne teste pas ») ; appariement par tâche (Plan, point 6, l. 267-269) ; aire d'épisode des hybrides non lue comme détection (l. 206, 269) ; « ne sépare pas la classe M d'une dépendance intra-épisode » (ligne de C3, l. 152). Rien à ajouter. |
| 9 | borne d'union à titre d'information | **différent, incomplet** : « à titre d'information seulement » est présent, mais la parenthèse « elle reste soumise au contre-lecteur » subsiste, et la condition de validité ne dit pas comment chaque texte contrôle son taux. **Couple résiduel 1.** |
| 10 | non-convergence → nœud | présent |
| 11 | rapport aux verrous des textes scellés | présent |
| 12 | GO relu dans `registres/go.md` | présent |

Les sept couples d'auteur (13, 15 à 19, 21 de la table de l'autrice ; 20 est ma règle du plafond) sont justes : titre, commit `1fcb23d7`, commande `analyse_v3`, gardes Q1 à Q4 dans la liste d'arrêt, phrase sur les scores recalculés. La table du code cité (21 lignes) est égale, empreinte par empreinte, aux fichiers du commit `1fcb23d7` (`sha256sum -c` : 21 OK).

Après le couple résiduel, `controle_ia.prereg.problemes` ne rend que les deux lignes attendues d'un brouillon (entrée de contre-lecture, marqueur `<<CONTRE_LECTURE_1>>`).

## 2. Code v3 (`1fcb23d7`)

- **41 passed** en 67,01 s (25 de la v1, 6 de la v2, 10 de la v3 ; une suite à la fois, `--basetemp` propre, supprimé).
- `analyse_v3` = `analyse_v2` (recette de W inchangée) plus les gardes, toutes **avant** le manifeste et tout chargement, dans cet ordre :
  - Q2 : chemin imposé `prereg/agregation-r1-v4-v1.md`, résolu dans le dépôt — **fait** ;
  - scellé et conforme (`exiger_prereg_scelle`) — **fait** ;
  - Q4 : tout manifeste sous `runs/` dont le préenregistrement a ce chemin ou cette empreinte arrête, code de fin 3 ; un manifeste illisible arrête aussi — **fait** ;
  - Q1 : chaque fichier de la liste fermée doit figurer dans la table du texte scellé avec l'empreinte du fichier ; une empreinte citée deux fois avec deux valeurs arrête ; un essai vérifie que la liste est égale aux modules importés — **fait** ;
  - Q3 : noms de la fiche v4 ; `scores-p3.npz` = `968414fc…` ; activations égales à leur compagnon `.sha256` (`verifier`) — **fait, avec la réserve ci-dessous** ;
  - arbre propre : par `creer_manifeste`, avant tout chargement.
- Artefacts R5 éprouvés, chacun avec son cas sain : non scellé (refus, aucun `runs/` créé) ; arbre sale (fichier non suivi, refus, aucun `diag/`) ; second passage (premier passage sain, puis refus) ; liste fermée altérée et ligne manquante ; empreinte de `scores-p3.npz` fausse ; compagnon d'activations faux ; noms d'entrée ; plafond.
- **Réserve Q3 (note, non bloquante)** : le compagnon et le fichier sont versés ensemble par la réception v4. L'égalité au compagnon prouve l'intégrité depuis la réception, pas l'identité avec ce que la réception a consigné. Option : avant scellement, recopier dans le texte les deux empreintes des compagnons, et les exiger comme `scores-p3.npz`. Ce sont des empreintes de fichiers, pas des résultats : les recopier ne rompt pas l'opposabilité. Le lecteur ne les a pas lues (`donnees/` interdit).

## 3. Verdict

**Scellable après le couple résiduel 1.** Le code v3 n'appelle aucune correction. Recommandé, sans bloquer : la réserve Q3.
