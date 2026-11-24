# Audit du protocole X comme instrument — complément v2 : ensemble des dossiers, branches de données comprises

Session fille d'audit (Claude Opus 5.5), même mandat que la v1 (règle 9 du protocole X v2, GO-2026-11-24-44), étendu par le mot de la mère du 24 novembre vers 18:57Z et 19:30Z : branches `donnees/collisionneur-*` permises, seulement pour les cellules, questions servies, journaux et notes, avec le même test d'exclusion sur les noms et les en-têtes avant toute lecture ; rien d'autre sous `donnees/` ; branches `coffre/*` toujours fermées. Écrit le 24 novembre 2026 vers 19:50Z. Le rapport v1 (`rapport-audit-protocole-x-v1.md`) reste intact ; ce complément refait ses chiffres sur l'ensemble, avec les mêmes méthodes (scripts `*_v2.py`, sorties `*-v2.json`). Aucune dépense, aucun modèle appelé.

## Verdict en trois lignes

1. **Rendement nul, confirmé sur l'ensemble (mesure).** 99 courses du collisionneur du 24 octobre au 24 novembre, 882,61 dollars comptés ; 218 éléments retenus par 31 notes et synthèses (130 propositions, 88 clauses de texte ou verdicts de lecture) ; une seule proposition tentée (non évaluable), aucune survivante ; 104 des 130 propositions n'ont aucune trace de suite, 16 ont été adoptées dans une décision sans épreuve, 9 sont en préparation.
2. **Modèles d'un même fournisseur non indépendants (mesure).** Au tour 1, la similarité moyenne des paires d'un même fournisseur est 0,37 contre 0,27 entre fournisseurs (76 courses, permutation, p ≈ 0,0001) ; même sens pour l'« expérience à faire en premier » (62 courses, p ≈ 0,0001) et, désormais significatif, pour le co-soutien des retenues (20 courses, p ≈ 0,03). La paire la plus proche est Fable 5.1–Opus 5.5 (0,43) : la parenté tient d'une génération à l'autre.
3. **Les tours de critique concèdent presque tout (mesure).** 7 248 lignes de décision au tour 3 : 97 % de critiques acceptées au moins en partie ; aucune déférence au même fournisseur (p = 0,95) ; aucune différence selon une trace de calcul (96,9 % contre 97,2 %).

**Confiance** : 0,85 ; 0,8 (plus de courses, mais la similarité de mots mêle style et fond) ; 0,8.

## Branches ouvertes et dossiers exclus

**Branches de données ouvertes** (62) : toutes les branches `donnees/collisionneur-*` sauf deux, soit `agents-noyau-methodo-v1`, `agents-noyau-v1`, `agents-outilles-methodo-v1`, `agents-outilles-v1`, `allocation-v1`, `already-clean-v1`, `audit-controle-v1`, `audit-controle-v2`, `bisociation-v1`, `boucle-d-or-v1`, `comparaison-v1`, `couche-2-cinq-divergences-v1`, `emprunts-v1`, `escalier-methodo-v1`, `escalier-v1`, `financement-v1`, `format-methodo-v1`, `format-v1`, `garde-delta-P-26-v1`, `graines-pilote4-v1`, `lecture-pilote-v1`, `litterature-boucles-v1`, `lot3-etage3-v1`, `memoire-encodage-v1`, `mesures-fortes-v1`, `neuron-explorer-v1`, `nuit-31-oct-v1`, `pari-de-signe-v1`, `pilote-complement-v1`, `pilote-couche-2-v1`, `pole-scientifique-v1`, `proposeur-enfichable-v1`, `publication-methodo-v1`, `publication-v1`, `question-mere-v2`, `questions-fortes-v1`, `rapport-consolide-v1`, `recombinaison-v1`, `reecriture-v1`, `repli-g0-v1`, `structure-v1`, `suite-HM1-v1`, `test-M-v1`, `texte-III-v1`, `v8-runs-v2`, `v9-brainstorm-v1`, `v9-brainstorm-v1-suite`, `v9-colognese-ward-q2-v1`, `v9-colognese-ward-q2-v1-run`, `v9-colognese-ward-q2-v1-suite`, `v9-conception-organisme-v1`, `v9-ibrahim-q1-v1`, `v9-ibrahim-q1-v1-run`, `v9-ibrahim-q1-v1-suite`, `v9-kirchner-q2-v1`, `v9-kirchner-q2-v1-run`, `v9-kirchner-q2-v1-suite`, `v9-scheurer-v1`, `v9-scheurer-v1-run`, `v9-scheurer-v1-suite`, `v9-sparks-v1`, `v9-sparks-v1-run` (préfixe `donnees/collisionneur-` omis). Seuls les cellules, questions, faits et journaux des courses y ont été lus ; aucun fichier d'activations, de scores, de sondes ni de tâches de sabotage.

**Exclus avant lecture, en plus de la liste de la v1** :

- branche `donnees/collisionneur-evasion-moniteurs-v1` entière (cinq courses : tours 1, 2, 2 bis, 2 « r609 », 3) : évasion des moniteurs, attaque contre les moniteurs ;
- branche `donnees/collisionneur-verite-dommage-v1` entière : vérité du dommage des modes non chiffrés (doute) ;
- `collisionneur-questions-fortes/run-questions-fortes-e3-v1` et `donnees/collisionneur-tableau-partage-v1/run-tableau-partage-e3-v1` : une marque de cloisonnement dans les quinze premières lignes de leur question ou de leurs faits (test par programme ; contenu non affiché).

**Doublons** : cinq copies moins complètes des courses v9 (« -run » contre « -suite », Colognese et Ward, Ibrahim, Kirchner, Scheurer, Brainstorm), en plus des deux de la v1.

## 1. Inventaire (mesure)

`sorties/inventaire-v2.json` et `.csv` :

- **99 courses incluses** (57 de plus que la v1), 949 cellules : 72 à trois tours, 8 à deux tours, 19 à un tour ; plus 9 dossiers de première étape (inchangés).
- **Espèces** : Opus 5.5 (85 courses), Argon (84), Fable 5.1 (61), Astra (43), Carbon (37), Fable 5.2 (33), Kimi (18), Opus 4.6 (15), Neon (13) ; une lettre sans espèce identifiable dans 10 courses.
- **Coût compté** : 882,61 dollars (journaux de toutes les courses) ; **payé au pire** : 917,08 dollars, connu seulement pour les courses récentes (les journaux d'octobre ne portent pas ce plafond).
- **Pannes** : 99 appels non conformes, dont 32 interrompus, **25 refus** (surtout en octobre), 18 échecs, 15 tronqués.
- **Notes de sélection** : 31 notes et synthèses rattachées à 34 courses ; **65 courses sans note de sélection trouvée**.

## 2. Jeu des propositions (mesure)

`sorties/jeu-des-propositions-v2.json` et `.csv` : 361 éléments, 218 retenus (130 propositions ; 88 clauses de texte ou verdicts de lecture, dans les synthèses de conception sur la lecture tôt du témoin positif, le repli de la porte G0, le pilote de la couche 2 et la lecture des nœuds N12 et N13), 20 « à reprendre », 123 non retenus. Unités de dernier tour : 1 629 dans 348 cellules (précision mesurée en v1 : 0,96 hors rejeux ; non remesurée sur les cellules d'octobre).

Devenir codé (sources dans le fichier) : synthèse de l'audit défensif versée dans la décision N-053 et synthèse du pari de signe dans la décision N-055, « adoptées sans épreuve » ; pas d'autre suite trouvée pour les dossiers d'octobre.

| devenir des 130 propositions retenues | nombre |
|---|---|
| jamais éprouvée — aucune trace | 104 |
| jamais éprouvée — adoptée sans épreuve | 16 |
| jamais éprouvée — en préparation | 9 |
| non évaluable | 1 |
| éprouvée (survivante ou tombée) | 0 |

## 3. Mesures refaites sur l'ensemble

### 3.1 Rendement (mesure)

Part éprouvée : 1/218 éléments (0,5 %), 1/130 propositions ; part survivante : 0 ; coût par survivante non défini ; coût par élément retenu : 1,82 dollar (396,25 dollars sur les courses à note). Les retenues restent des consensus : sur les éléments à porteurs déclarés, 101 sur 133 sont portés par au moins deux fournisseurs. Part des retenues portées, là où l'espèce était présente : Fable 5.2 0,90 ; Carbon 0,88 ; Neon 0,84 ; Opus 5.5 0,84 ; Fable 5.1 0,73 ; Astra 0,71 ; Argon 0,69 ; Opus 4.6 0,59 ; Kimi 0,40.

### 3.2 Erreurs (mesure)

- **« VÉRIFIÉ » non fondés** (taux codés en v1 appliqués aux signalements v2) : Argon environ 16 % des étiquettes (1 749 étiquettes), Neon 16 %, Opus 5.5 10 %, Carbon 4 %, Fable 5.2 et Astra ≈ 0. Non codés faute d'échantillon : Fable 5.1 (13 signalées sur 139), Opus 4.6 (9 sur 62), Kimi (5 sur 20).
- **Calculs rejoués** : 212 calculs simples ; 23 signalés par l'analyseur, tous relus à la main : aucun faux (morceaux d'expressions, préfacteurs, pourcentages, millions, étiquettes de tableau ; `codage-calculs-v2.json`).
- **Références arXiv** : 315 citations, aucune de forme impossible, 192 vers un PDF du dépôt ; 24 jugeables par l'auteur cité, 8 signalées, toutes relues : auteur voisin d'une autre citation, **aucune fausse confirmée**.

### 3.3 Accords et indépendance (mesure)

| mesure | même fournisseur | fournisseurs différents | courses | p unilatérale |
|---|---|---|---|---|
| conceptions du tour 1 | 0,374 | 0,269 | 76 | 0,0001 |
| « expérience à faire en premier » | 0,099 | 0,074 | 62 | 0,0001 |
| co-soutien des retenues | 0,860 | 0,754 | 20 | 0,03 |

Paires les plus proches au tour 1 (au moins 8 dossiers communs) : Fable 5.1–Opus 5.5 0,43 ; Fable 5.1–Opus 4.6 0,41 ; Argon–Opus 4.6 0,39 ; Argon–Fable 5.1 0,38 ; Argon–Carbon 0,36 ; Carbon–Neon 0,35 ; Fable 5.2–Opus 5.5 0,35. Astra reste le plus éloigné de tous (0,17 à 0,26). **Argument** : les deux générations d'Anthropic forment une même famille de réponses ; la règle 6 vaut aussi entre générations. Les paires d'Argon avec les anciens modèles sont hautes aussi : les courses d'octobre posaient des questions plus courtes et plus semblables entre elles, ce que la permutation à l'intérieur de chaque course neutralise pour le test, pas pour la matrice brute.

### 3.4 Suivisme (mesure)

7 248 lignes de décision : 6 053 acceptées, 985 partielles, 210 rejetées (2,9 %). Part non rejetée par répondant : de 95,5 % (Neon) à 98,7 % (Kimi) ; par critique, de 95,0 % (Opus 4.6) à 98,3 % (Kimi). Déférence au même fournisseur : écart −0,010 (p = 0,95). Selon une trace de calcul : 96,9 % contre 97,2 %.

### 3.5 Fidélité (mesure)

Inchangée en substance : les cinq rejeux d'Argon ressemblent plus à leur origine (0,39 à 0,56) qu'à toute autre espèce de la même course (10 sur 10). Les bras jumeau et témoin donnent 0,28 contre 0,18, et 0,24 contre 0,18. Les relances d'octobre (proposeur enfichable v1 et v2, repli de la porte G0 v1 et v2) changent la question : ce ne sont pas des rejeux.

## 4. Ce qui change par rapport à la v1

- Les chiffres doublent d'échelle sans changer de sens : rendement nul, dépendance par fournisseur, concession quasi totale.
- Le co-soutien des retenues devient significatif (p ≈ 0,03 contre 0,06).
- Les refus des modèles pèsent en octobre (25 sur 99 pannes).
- Le plan d'ablation de la v1 (§ 5) n'est pas modifié. La phase 0 rétrospective peut porter sur les 72 courses à trois tours au lieu de 33 : le nombre de 52 dossiers appariés est atteignable sans dépense pour le critère J1.

## 5. Réserves

- Les mêmes que la v1 : codages non aveugles, un seul codeur, rappel non mesuré.
- Taux de « VÉRIFIÉ » non fondés repris des échantillons v1 : non recodés sur les cellules d'octobre.
- Correspondance entre notes et courses en octobre établie à la main (11 notes), avec des règles de section propres à chaque note (`retenues_v2.py`). Les lectures des nœuds N12 et N13 sont classées en verdicts, non en propositions.
- Les courses sans note (65) ne comptent pas dans le rendement : il est calculé sur les seules courses où une sélection a été écrite.

## 6. Fichiers

Scripts : `inventaire_v2.py`, `audit_commun_v3.py`, `unites_v2.py`, `retenues_v2.py`, `devenir_v2.py`, `cellules_v2.py`, `erreurs_v2.py`, `accords_v2.py`, `suivisme_v2.py`, `fidelite_v2.py`, `rendement_v2.py`. Sorties : `inventaire-v2`, `unites-v2`, `retenues-v2`, `jeu-des-propositions-v2` (JSON et CSV), `erreurs-v2`, `codage-calculs-v2`, `accords-v2`, `suivisme-v2`, `fidelite-v2`, `rendement-v2`. Chaque fichier a son compagnon d'empreinte.
