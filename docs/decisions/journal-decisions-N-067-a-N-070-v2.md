# Journal de rédaction des décisions N-067 à N-070 (brouillons 2) — v2

Rédacteur des brouillons 1 (sous-agent, Claude Opus 5.5), relancé par la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`. Travail du 13 novembre 2026, de 18:53 à 19:00 UTC environ (heures relevées par `date -u` ; voir l'erratum de la section 6). Le journal v1 (`journal-decisions-N-067-a-N-070-v1.md`, `be45f8c5…`) reste intact (R12).

**Commande de la mère** : écrire les brouillons 2 sur la contre-lecture `docs/decisions/contre-lecture-decisions-N-067-a-N-070-v1.md` (`db44d99516973d18b64713c9b5cc7e0bb3e9f54e7944a86ba2f619caf765314d`, R-2565, conforme à son compagnon) ; appliquer tous les couples, majeurs et mineurs, ou les écarter avec raison, couple par couple ; pour les onze points de la section 6 de la contre-lecture, ne pas trancher, mais écrire dans chaque décision un encadré « En attente du mot de Lazar » au format de décision et garder dans l'énoncé la lecture la moins revendicatrice ; pour O4, écrire la clause d'usage public ; sceller ; aucune écriture git.

## 1. Fichiers

| fichier | SHA-256 | base |
|---|---|---|
| `docs/decisions/decision-N-067-v1-brouillon2.md` | `cb3f37195997c320749d8b1578315e71fc9f51cf1395ddfb3876d58a84edfac1` | brouillon 1 `d83d067c…` |
| `docs/decisions/decision-N-068-v1-brouillon2.md` | `414fc6b40c0a1a882e78426d506093c4bd5658982b960098fb74657d514e8869` | brouillon 1 `76be8b44…` |
| `docs/decisions/decision-N-069-v1-brouillon2.md` | `69f8f699096277bbbe47de8a77ba709fbaadd253d27359770b93e426234ad362` | brouillon 1 `823a3c35…` |
| `docs/decisions/decision-N-070-v1-brouillon2.md` | `a7eeb395218920d40cca94e6fc6c9fda89f36ab0b18548290e70ffcd5ab4996e` | brouillon 1 `8b52e368…` |

Les brouillons 2 sont des copies des brouillons 1, modifiées par remplacements exacts (chaque texte « actuel » de la contre-lecture retrouvé une fois et une seule, contrôle par programme). Les quatre brouillons 1 restent intacts : `sha256sum -c` conforme pour chacun après l'écriture des brouillons 2.

## 2. Couples de la contre-lecture, un par un

**Aucun couple n'est écarté.** Tous sont appliqués, mot pour mot sauf mention.

| couple | gravité | sort | où | remarque |
|---|---|---|---|---|
| 67-1 | majeur | appliqué | N-067, § 3 (ligne O12) et § 4, point 3 | J'ajoute à la fin du point 3 la lecture d'attente du point 1 de l'encadré. |
| 67-2 | majeur | appliqué | N-067, § 3 (ligne O2 (c)) | Mot pour mot. |
| 67-3 | majeur | appliqué, **sous la forme prescrite par la mère** | N-067, § 4, point 2 (clause d'usage public) ; § 10 ; encadré, point 4 | Clause : O4, et l'énoncé retenu de O2, ne sont déclarés libres publiquement qu'après lecture de SSRN 6569258 sur PDF, sinon avec la réserve écrite (texte de la réserve donné). J'y nomme l'enregistrement figé **sous embargo** de R-2563, qui remplace sur ce point le dépôt en clair de R-2555 (option C). |
| 67-4 | mineur | appliqué | N-067, § 4, phrase pour un lecteur extérieur | J'ajoute que cette phrase ne sort du dépôt que sous la clause d'usage public et après le mot de Lazar sur O12. |
| 67-5 | mineur | appliqué | N-067, § 9 | Renvoi à l'encadré, point 5a, ajouté. |
| 67-6 | mineur | appliqué | N-067, § 4, point 1 | Mot pour mot. |
| 67-7 | mineur | appliqué | N-067, § 4, point 4 | Renvoi à l'encadré, point 3, ajouté. |
| 67-8 | mineur | appliqué | N-067, § 3 (ligne O2 (b)) | Mot pour mot. |
| 68-1 | majeur | appliqué | N-068, § 4 (« ce qui est propre ») ; § 6 (ligne ajoutée après Mohsin, Rahman ; dernier paragraphe) | Le chemin `…/lot6/` est ajouté à la phrase qui situe les PDF. |
| 68-2 | mineur | appliqué | N-068, § 6 | Mot pour mot. |
| 68-3 | mineur | appliqué | N-068, § 6 | Mot pour mot. |
| 68-4 | mineur | appliqué | N-068, § 4, énoncé retenu | C'est un qualificatif qui resserre ; il attend le mot de Lazar (encadré, point 6) et s'applique d'ici là, comme lecture la moins revendicatrice. |
| 68-5 | mineur | appliqué | N-068, § 7 | J'ajoute R-2553 à la source (« aucune sonde » y est dit aussi). |
| 69-1 | majeur | appliqué | N-069, § 7 (après la ligne sur J-PACT) ; § 4, renvoi | Les aires 0,87, 0,81, 0,86 et 0,61, 0,61, 0,58 sont attribuées à la lecture du PDF par la contre-lecture (constat 69-1), que je n'ai pas refaite ligne à ligne ; j'ai retrouvé sur le PDF la phrase « more visible in the relative pattern » (p. 7). |
| 69-2 | mineur | appliqué | N-069, § 7 | Passage retrouvé sur le PDF (2607.24893 v2, p. 8) ; empreinte du PDF conforme (`504d82ab525be78b…`). |
| 69-3 | mineur | appliqué | N-069, § 7 | Mot pour mot. |
| 69-4 | mineur | appliqué | N-069, § 8 (« ce qui ne change pas ») | Mot pour mot. |
| 70-1 | majeur | appliqué | N-070, § 3 | La lettre corrigée est conforme au lot 12, § 4, relu. |
| 70-2 | mineur pour la contre-lecture, majeur pour la mère | appliqué | N-070, en-tête, « Portée » | Mot pour mot. |
| 70-3 | mineur | appliqué | N-070, § 6, « Coût du moniteur » | Mot pour mot. |
| 70-4 | mineur | appliqué | N-070, § 3 | Mot pour mot. |
| 70-5 | mineur | appliqué | N-070, § 5 | Mot pour mot. |

## 3. Les onze points pour Lazar : où ils sont posés, et ce qui tient en attendant

Chaque point est posé au format de décision (décision en une phrase ; enjeu ; options avec avantage et inconvénient ; recommandation et confiance), dans un encadré en tête de la décision (section 0). Ce sont des nœuds : aucun défaut à 48 heures ; la lecture « en attendant » tient jusqu'au mot.

| point de la contre-lecture (§ 6) | décision | recommandation, confiance | en attendant |
|---|---|---|---|
| 1. Forme de O12 requalifiée et resserrée | N-067, point 1 | confirmer, 0,75 | forme écrite pour être jugée, revendiquée dans aucun texte qui sort du dépôt |
| 2. O1, O3 (sceau), O17 cessent d'être revendiquées | N-067, point 2 | confirmer, 0,85 | non revendiquées |
| 3. Quatre « non trouvés » sans revendication | N-067, point 3 | les garder ainsi, 0,7 | sans revendication |
| 4. Usage public de O4 | N-067, point 4 | lire SSRN 6569258 d'abord, 0,8 | clause d'usage public (§ 4, point 2) |
| 5. Statuts hors périmètre ; 2611.00643 ; page publique | N-067, points 5a, 5b, 5c | adopter les statuts durs, 0,7 ; citer comme antécédent, 0,8 ; corriger la page après retenue, 0,8 | aucun de ces statuts présenté comme libre ; 2611.00643 cité comme antécédent ; rien publié |
| 6. HC2 : plan apparié, intensité, Kale et Vishwanath | N-068, point 6 | confirmer, 0,85 | ajustements appliqués (ils revendiquent moins) |
| 7. HC2 : poids 0,65 | N-068, point 7 | revoir au préenregistrement du papier C, 0,6 | 0,65 jamais cité sans les contre-indices |
| 8. HC4 (lettre de N-013) ; HC2b (sources du style) | N-068, points 8a, 8b | restreindre HC4, 0,7 (décision à part) ; ajouter les sources, 0,85 | lettre de HC4 jamais citée sans ses contre-résultats ; sources citées comme voisines |
| 9. Bascule ; critère de G2 ; mot « co-élévation » | N-069, points 9a, 9b, 9c | non déclenchée, veille, 0,7 ; pic comme base, 0,8 ; garder « co-élévation » et l'écart comme base, 0,75 | bascule non déclenchée, « cœur vierge » retiré ; critère inchangé ; « co-élévation » |
| 10. H9 : contenu de la mesure descriptive | N-070, point 10 | rang de relais, avec et sans moniteur, en description, 0,6 | contenu non fixé ; aucun préenregistrement ; bras moniteur non annoncé |
| 11. Journal `NODE_C_VOLETS_III_IV_H9.log` | N-070, point 11 | provenance établie par la mère avant retenue, 0,6 | rien n'en est cité |

## 4. Changements de ma main, hors des couples

- Chaque encadré et chaque renvoi « (encadré, point n) » dans le corps des décisions, pour que la lecture d'attente soit lisible là où l'énoncé se trouve.
- N-067, § 4, point 3 : la phrase « En attente du mot de Lazar (encadré, point 1) : d'ici là, cette forme n'est revendiquée dans aucun texte qui sort du dépôt ». C'est la lecture la moins revendicatrice : entre confirmer la forme resserrée et ne rien revendiquer, la seconde l'est moins.
- N-069, § 4 : une puce qui garde « co-élévation » en attendant le mot (point 9c) ; § 5 : le renvoi de G2 à l'encadré (point 9b) remplace « proposition, à décider au préenregistrement ».
- N-069, encadré, point 9a : l'enjeu nomme 2611.04556 (sans sonde, mais signé par un auteur de NARCBench et l'institut britannique ; synthèse finale, section 6, relue ici).
- N-070, § 4, point 2, et § 5 : la mesure descriptive est dite « contenu en attente » et l'option (a) de l'encadré conditionnelle au mot de Lazar.
- En-tête de chaque décision : statut « brouillon 2 », base et contre-lecture nommées avec leurs empreintes.

## 5. Contrôles faits

- Empreintes : contre-lecture conforme ; brouillons 1 conformes après l'écriture des brouillons 2 ; PDF 2607.24893 v2 (`lot5/`, branche des pièces) conforme ; PDF 2609.03035 v2 (`lot6/`) déjà vérifié au v1 (`bccdbe1b…`).
- Passages retrouvés sur PDF (`pdftotext`, page seule) : 2607.24893 v2, p. 8 (« mostly because the injected text makes an observation longer, not because it puts evidence together across agents ») ; 2609.03035 v2, p. 7 (« more visible in the relative pattern »).
- Synthèse finale de niveau 3 (`e30a013d…`), section 6 : « 2611.04556 n'a aucune sonde », relu pour 68-5 et 9a.
- Sceaux des quatre brouillons 2 : `verifier` conforme.

## 6. Erratum et refus du sceau

- **Heures d'écriture fausses dans deux en-têtes.** Les brouillons 2 de N-069 et N-070 disent « vers 19:00 UTC » et « vers 19:02 UTC » : je les ai écrites d'avance, avant que l'horloge n'y arrive. `date -u` donnait **18:58:49 UTC** au scellement des quatre. Celles de N-067 (« vers 18:56 ») et N-068 (« vers 18:58 ») sont justes à la minute près. Heure à retenir pour les quatre : **écrits entre 18:54 et 18:59 UTC**.
- **Refus du sceau, rapporté tel quel.** J'ai voulu corriger ces heures et resceller. L'outil `controle_ia.scellement sceller` a refusé, pour chacun des quatre fichiers, par sa garde R12. Texte rendu pour le premier : « ARRÊT : docs/decisions/decision-N-067-v1-brouillon2.md est déjà scellé avec une autre empreinte (cb3f37195997…) : R12 interdit d'écraser — une nouvelle version prend un nouveau nom ». Les trois autres sont identiques au nom et à l'empreinte près. Je n'ai pas contourné la garde : j'ai remis les quatre fichiers à leur contenu scellé, et `verifier` est conforme pour les quatre. La correction des heures se fera à la recopie sous `-v1.md`, ou dans un brouillon 3 si la mère le préfère.

## 7. Interdits

Aucune écriture git ; aucun registre modifié ; aucune dépense ; aucun appel hors du conteneur (les branches étaient déjà récupérées) ; aucune valeur de clé lue ; chemins interdits non ouverts ; aucune recherche récursive. Les PDF ont été copiés dans le dossier de travail temporaire et lus par `pdftotext` ; les scripts de modification vivent dans un autre dossier et tournent par `python3 -I`.

Version 2 ; jamais réécrite (R12).
