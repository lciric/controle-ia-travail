# Rapport du rédacteur — additif des interrupteurs de l'orchestrateur v69, version 2, et cadre de la v70, version 2 — v1

- Auteur : rédacteur neuf, modèle F (je n'ai écrit ni les pièces v1, ni les contre-lectures, ni aucun code). Écrit le 2026-11-20 ; relevés de `date -u` : 04:51:32Z après la lecture des pièces, 04:57:01Z après la production des deux pièces v2.
- Mandat : `docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v69/mandat-redacteur-additif-orchestrateur-v69-v2-v1.md` (`34a63552217626c8a3ec187dfbc6cf270352723cdcaa28a076c2ae60bc66d70d`, compagnon vérifié par `sha256sum -c`).
- Processeur seul. Aucune écriture dans le dépôt, aucun commit, aucun lancement de l'orchestrateur, du lanceur ni de l'organisme, aucun appel à un fournisseur, aucune dépense. **Je n'ai lu aucun fichier de code de l'orchestrateur** ; le seul code lu est l'outil de remplacement. Python : 3.13.18.
- Dossier des pièces rendues (noté D) : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-additif-orchestrateur-v69-v2/`. Dossier des pièces qui font foi (noté V69) : `docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v69/`.

## 0. Verdict

1. **L'additif v2 et le cadre v2 sont produits** par l'outil contre-lu, en un seul appel chacun, sans rejet d'ancre : 31 remplacements sur l'additif, 6 sur le cadre.
2. **Les corrections 2 à 12 sont appliquées à la lettre** ; la correction 1 l'est dans le texte que la contre-lecture v2 lui donne, reporté au § 3.3 de l'additif.
3. **Le § 1.2 est récrit selon (a′)** ; D1 (a′), D2 (a), D3 (a) sont marquées tranchées par le mot de Lazar, sous réserve de l'inscription de sa lecture par la mère. Rien n'accorde l'allumage.
4. **Deux incohérences induites par la correction 6 restent dans la v2**, non corrigées parce que hors de la lettre du mandat (§ 5). Elles sont à trancher avant scellement.

## 1. Sources vérifiées

Empreintes recalculées par `sha256sum`, compagnons vérifiés par `sha256sum -c` depuis V69.

| pièce | sha256 | lu |
|---|---|---|
| `V69/additif-interrupteurs-orchestrateur-v69-v1.md` | `aef8ff2f8eb3597c8405c765c3432ce791a34ab65b851a75ac223de875fbe158` | en entier |
| `V69/cadre-lecture-registre-orchestrateur-v70-v1.md` | `84651a4c658e88f0bca7d299746ae05c267ae7f9f2002d8371dd19fccef4a5ee` | en entier |
| `V69/rapport-redacteur-additif-orchestrateur-v69-v1.md` | `b97cbd188cf1cb2d7ccc252990bff19655a4799db4cc625023d1c3b52870a707` | en entier |
| `V69/contre-lecture-additif-orchestrateur-v69-v1.md` | `3ead148ac78ff02996b376930673b79d414716b44c4969fe9987fd085cfced12` | en entier |
| `V69/contre-lecture-additif-orchestrateur-v69-v2.md` | `137728d938a53d7ef1459e5ca2e654d1389460aca5449051c6d8dabb13b88e9d` | en entier |
| `scripts/remplacer_texte_exact_v1.py` | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` | en entier |

Les deux cibles ne portent ni espace insécable ni apostrophe courbe (recherche à l'octet sur chacune des deux, par son chemin).

## 2. Pièces rendues (dossier D, chacune avec son compagnon `.sha256`)

| fichier | sha256 |
|---|---|
| `additif-interrupteurs-orchestrateur-v69-v2.md` | `9d94d23fadfc961e1e3c71a743358d4d5a16a924267499b3a3f1028fee34e85f` |
| `cadre-lecture-registre-orchestrateur-v70-v2.md` | `216d9bcbc0276c79c5a86bcf835cd3d9d260d6e31e49c7f1250349530643fbeb` |
| `remplacements-additif-v1-vers-v2-v1.json` | `4a9e668f8a169774d2102d631969dde777b8e719f7119377d7b9aab5300e70ba` |
| `remplacements-cadre-v1-vers-v2-v1.json` | `225c64a430c233b6fe3113be933de0c0fd51aa2d40d82fc9fb5615c9fcf88882` |
| `additif-interrupteurs-orchestrateur-v69-v2.md.journal-remplacements-v1.json` | `d0e2bea21fdd8d12089826ae47f63f203c6a03b57a116816c4b7cedfcf28a72e` |
| `cadre-lecture-registre-orchestrateur-v70-v2.md.journal-remplacements-v1.json` | `458c9c20ea4f27a4c1a0b0edd39bdf72a1b3222c327510fc15a88d32ca6a9faa` |
| `differentiel-additif-interrupteurs-orchestrateur-v69-v1-v2.diff` | `93ed10d24eb51537c47bfa442ef0a31c79d4fe042994cf70978c0aee5146df0a` |
| `differentiel-cadre-lecture-registre-orchestrateur-v70-v1-v2.diff` | `dd7dac8d78a1d78c0c6e7a721a5c6bcfc35b9accb07729b068069198996c7417` |
| ce rapport, `rapport-redacteur-additif-orchestrateur-v69-v2-v1.md` | dans son compagnon |

Chaque ancre des deux JSON a été comptée avant l'appel par `grep -c -F -e` sur sa cible : 37 ancres, 37 fois le compte 1. Les différentiels sont des `diff -u` de la pièce v1 du dépôt vers la pièce v2 du dossier D.

## 3. Ce qui a été appliqué à l'additif

Le rang est celui du JSON.

| rang | lieu | origine |
|---|---|---|
| 1 | titre : « v1 » devient « v2 » | tenue |
| 2 à 6 | lignes d'en-tête : auteur, statut, mandat, sources, code non lu | tenue ; le statut porte les décisions tranchées sous réserve |
| 7 à 10 | § 1.2, récrit | mandat, option (a′) |
| 11 | § 2, ligne C4 | correction 2, à la lettre |
| 12 | § 2, ligne C5 : « étage par la chaîne du tour fermé » devient « étage par le sommet neuf de la v69, qui appelle les maillons et les fonctions du tour fermé » | conséquence de (a′), du rédacteur |
| 13, 14 | § 2, ligne C2 ; § 2.1, condition 8 | correction 3, à la lettre |
| 15 | § 6, garde 2, artefact | correction 4, à la lettre |
| 16 | § 3.3, ce que l'étage sert au lecteur témoin | correction 1 remplacée, point (c), en substance (contre-lecture v2, § 3.2 et § 2, point 3) |
| 17 | § 4.1, second point | correction 8, à la lettre |
| 18 | § 4.2, phrase d'introduction | correction 11, à la lettre |
| 19, 26 | § 4.2, dernier alinéa ; § 4.5, quatrième point | correction 5, à la lettre |
| 20 | § 4.3, introduction : la proposition est dite retenue par D2 (a) | décision marquée tranchée |
| 21, 23 | § 4.3, ligne 1 de la règle et alinéa qui suit la table | correction 6, à la lettre |
| 22, 24 | § 4.3, ligne 2 de la règle et phrase ajoutée à l'alinéa | correction 12, à la lettre |
| 25 | § 4.4, alinéa « Coût et effet », ajouté en paragraphe à part | correction 7, à la lettre |
| 27, 29 | § 5.1 ; § 6, garde 4 | correction 10, à la lettre |
| 28 | § 5.2, premier point | correction 9, à la lettre |
| 30 | § 9, réserve 1 | correction 1 telle que la contre-lecture v2 la remplace, à la lettre |
| 31 | § 9, réserve 6 récrite sous (a′) ; réserve 7 ajoutée (décisions, réserve d'inscription, allumage non accordé) | mandat |

**Report de la correction 1 au rapport.** Le rapport v1 n'est pas récrit (règle R12). Ce que la correction 1 demande d'y reporter est ici : le véhicule n'est plus « non établi » mais tranché sur le code contre l'option (a) (réponse (b2) contraire), et D1 est tranchée sur (a′) ; les « trois points à confirmer sur le code » du rapport v1, § 4, point 2, sont remplacés par le § 6 ci-dessous.

## 4. Ce qui a été appliqué au cadre

Aucune correction numérotée ne porte sur le cadre. Il est touché par D3 et par la tenue :

1. titre et lignes de version (auteur, statut, mandat) ;
2. § 3, point 1 : D3 (a) marquée tranchée sous réserve d'inscription — la réserve de `GO-2026-11-19-76`, point 2, tient ; la v70 se conçoit avec les deux formes ; le point 7 du palier 0b choisit ; l'allumage de la lecture reste un nœud ;
3. § 3, point 3 : la précision que la contre-lecture v1 dit facultative (§ 3, constat 6) — la liste de la garde est une valeur de configuration, les cinq mots sont ceux des essais. **Appliquée par mon choix** ; à retirer si la mère la juge hors mandat.

## 5. Écarts au mandat, et ce que je n'ai pas corrigé

1. **Aucun refus de permission, de classifieur ni de garde. Aucun rejet d'ancre par l'outil ; aucun JSON fautif.**
2. **Deux tentatives de recherche mal formées, sans effet** : `grep -c -P` avec un point de code a été refusé par `grep` (« character code point value … is too large ») sur chacune des deux cibles ; une forme avec des caractères tapés a rendu un compte sans valeur (178 et 40). La recherche a été refaite à l'octet, compte 0 sur les deux cibles.
3. **Trois modifications au-delà des corrections numérotées**, toutes déclarées : rang 12 de l'additif (ligne C5, conséquence de (a′)) ; rang 20 (D2 dite retenue au § 4.3) ; la précision facultative du cadre.
4. **Incohérences laissées dans l'additif v2, induites par la correction 6**, que je n'ai pas corrigées parce que le mandat demande les corrections à la lettre :
   - § 0, point 4 : « un verdict précis parmi quatre ». Depuis la correction 6, « confiné » n'est attribuable à aucune tentative ; trois verdicts restent possibles. Texte proposé : « un verdict précis parmi les trois attribuables à ce palier, des quatre mots de R-3209 ».
   - § 4.4, second alinéa : sans tranche de contrôle, « les verdicts possibles sont les trois autres ». Depuis la correction 6, il n'en reste que deux, « identique » et « portable ». Texte proposé : « les verdicts possibles sont « identique » et « portable » ».
   - De même, le rapport v1, § 0, point 3, liste encore quatre verdicts ; il n'est pas récrit.
5. **La correction 5 écrit « cette lecture est du rédacteur, posée avec D2 »** (classe d'une tentative refusée avant l'épreuve). Je l'ai laissée à la lettre. Le mot de Lazar tranche D2 (a) ; qu'il couvre aussi cette lecture, ajoutée par la contre-lecture après le rapport v1, n'est pas établi par les pièces. À dire à la mère avec l'inscription.
6. **Le texte de la correction 4 garde « la chaîne de la v69 »** : à la lettre ; le mot « chaîne » y désigne le chemin de la v69, non le tour fermé.

## 6. Ce qui reste à établir sur le code

Repris du § 1.2 de l'additif v2 ; je n'ai rien vérifié moi-même sur le code.

1. **Réponse (b3) : le lanceur réel.** `demonstrations/tour_ferme_v64.py`, qui construit les adaptateurs réels des relais, est absent de la copie que la contre-lecture v2 a lue. Leur construction est à reprendre de ce lanceur ou à écrire dans le lanceur version 11, et à contre-lire.
2. **Le sommet neuf de l'étage** : code neuf, jamais joué en réel ; l'appel de `jouer_etage_v57` avec `plafond_total_usd` et `plafond_externe_usd` est à éprouver en simulé, cas sain et artefact de la garde 6.
3. **Les fonctions reprises** (`carte_servie`, `test_de_mort_impose`, `contre_calculer`, `AdaptateurEtageV64`, `Compteur.verifier_parts_avant_etage`) : lues par parties par la contre-lecture. Qu'elles s'appellent depuis un fichier neuf sans rien prendre au corps de `jouer_etage`, et que `contre_calculer` reçoive de son appelant le chemin de la tranche, est **mon relevé, non un constat de la contre-lecture**.
4. **La tranche de contrôle** : que son recalcul passe par les mêmes fonctions.
5. Sans effet sur ce régime : la fabrication du rang par les juges de la course 2 (`course2_v56`, `noyau_v56`, absents de la copie).

## 7. Décisions

| décision | option | statut dans les pièces v2 |
|---|---|---|
| D1, le véhicule | (a′) | tranchée par le mot de Lazar du 2026-11-20 (« go reprise, go recos »), sous réserve de l'inscription de sa lecture par la mère |
| D2, les quatre verdicts précis et la tranche de contrôle | (a) | de même |
| D3, la v70 et le point 7 du palier 0b | (a) | de même |

Si la mère inscrit une autre lecture du mot, les deux pièces v2 changent. **L'allumage réel n'est accordé par rien de ce qui est écrit ici** : il demande le devis du palier 1 et une ligne d'accord de calcul qui nomme `tests_de_mort_reels` et porte le montant au pire (additif, § 5.1).

— rédacteur neuf, modèle F
