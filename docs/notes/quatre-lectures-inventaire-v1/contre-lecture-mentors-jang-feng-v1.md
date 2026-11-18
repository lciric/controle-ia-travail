# Contre-lecture du relevé d'idées de la course de l'organisme d'idéation sur la question des mentors Jang et Feng (3 novembre) — v1

- **Écrit** le 18 novembre 2026 vers 05:45 UTC (`date -u` à 05:41:50) par un sous-agent neuf (Claude Opus 5.5), qui n'a pas écrit la note (règle R2), sous l'autonomie GO-2026-11-18-05 et le « go » de Lazar aux quatre lectures sans dépense de l'inventaire (R-3168, R-3170). Inventaire : `docs/notes/inventaire-collisionneurs-organismes-v1/inventaire-v1.md` (`b49dc246…`, recalculée), § A, B et E.
- **Note contre-lue** : `docs/notes/quatre-lectures-inventaire-v1/mentors-jang-feng-v1.md`, empreinte `9d7bf9c257f8ec90eb687fb54a132a0406059b5bda91edebcb620e58165fbde0` (recalculée, égale à son compagnon), 186 lignes. Non modifiée.
- **Sources rouvertes** : la seule branche `donnees/course-jang-feng-v1-run`, commit `8904d60`, extraite seule dans le bloc-notes de la session (`…/scratchpad/quatre-lectures/extrait/course-jang-feng-v1-run/`, 167 fichiers) ; mêmes abréviations que la note (F, FI, K, P, AI, MD, MF, TR, BI, ML, RC, RK, RA, JP). Empreintes recalculées égales à leurs compagnons pour F (`d2f1d74a…`), FI (`e6a4f1a2…`), MF (`66f60741…`), TR (`fb4c9f55…`), RA (`e04f56b0…`). Au dépôt : `registres/decisions.md` (R-1131, R-1157, R-1162, R-1163, R-1166, R-1172, R-1451, R-1455), `registres/go.md` (`dd4526c4…`, l. 230-235), `registres/depenses.md` (`a467ba68…`, l. 345-353, et son historique git), l'inventaire (l. 93, 119, 136, 145-149, 162), `inventaire-idees-organisme-v7.md` (`056adb7f…`, l. 504), `sorties-non-lues-v2.md` (`2fb208d4…`, l. 28).
- **Cadre tenu** : lecture seule ; aucune dépense, aucun appel de modèle, aucune clé lue ni affichée, aucun commit, aucune poussée, aucun `git fetch`, aucune branche ouverte hors de l'extrait ; rien lu sous `diag/` ; aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni du premier test boîte blanche bis. Pour les trois fiches exclues, je n'ai lu que l'identifiant, la ligne de départ, les métadonnées (proposeur, origine, case) et la taille : ni titre, ni axe, ni contenu. Je n'ai ouvert ni `classement.json`, ni les verdicts, ni les lectures d'étiquettes, ni les clés du coffre (sauf `jf1-cle-bras.json` et `jf1-paires-par-bras.json`, que la note cite).

## Verdict

**À corriger.** Les dix corrections ci-dessous sont toutes de fait : citations fausses, oublis, attributions non sourcées. Je n'ai trouvé ni résumé infidèle d'une fiche, ni résumé d'une pièce d'une famille exclue, ni résultat sous embargo. J'écris donc la version 2 (`mentors-jang-feng-v2.md`, même dossier). Elle dit en tête qu'elle est du contre-lecteur et ce qu'elle change ; la v1 n'est pas touchée.

## Corrections (liste exacte)

1. **L'usage hors programme repose sur une citation fausse** (§ 4.5 ; point 10 du rendu). La note dit que R-1451 rapporte une réponse « collée par Lazar après soumission ». R-1451 (`registres/decisions.md` l. 1409) parle du collage de **00:49 UTC**, alors que Lazar dit avoir soumis « vers 01:28 UTC » : ce collage est donc **antérieur** à la soumission. Le constat sur la soumission elle-même vient de **R-1455** (l. 1413, 02:00 UTC) : « le collage de Lazar de 01:57 UTC est celui de 00:49 sans le choix des mentors ». R-1451 dit aussi que des versions v8, v9 et v10 de la réponse « Feng et Jang », postérieures à la course, ont été vérifiées ou préparées, et que la version envoyée reste « à confirmer ». La conclusion prudente de la note (« je n'établis pas… ») tient, mais sa prémisse est mal sourcée. La v2 cite les deux lignes et ne conclut dans aucun sens.
2. **Des noms d'auteurs sont attribués aux proposeurs à tort** (§ 1, l. 39 ; exclusions, l. 29). La note écrit « macro-protocole adaptatif de Wen et al., 2411.17693 », « sondes de Feng et al. […] 2409.12822 », « Jang et al., 2604.28182 », puis « Toutes ces attributions sont celles des proposeurs ». Une recherche sur les 26 fiches lues et les deux fusions inachevées ne trouve **aucune** occurrence de « Wen » ni de « Feng et al. ». Seules y figurent « organismes de Jang » (`f728f1b425b25`, `ff51aac4334a8`) et « étudiées par Feng » (`fa09be50c2b3f`, `ff51aac4334a8`). « Wen et al. » est donc un ajout du rédacteur, présenté comme l'avis des proposeurs et non vérifié. La v2 le retire.
3. **Un oubli de cloisonnement : trois fiches voisines de la famille 1 ne sont pas signalées** (réserves, point 1). La note signale cinq fiches qui reconstruisent des organismes d'après 2604.28182. Elle omet trois fiches qui reposent sur des **organismes de sous-performance qui ne verbalisent pas**, à construire ou à reproduire d'après des travaux publiés : `fe2f9cb3b665c` (Fable, F:l.535, « deux organismes selon la recette de 2509.21344 (verbalisant, non verbalisant) »), `feee16a806f32` (Opus, F:l.605, organismes « sur le modèle des organismes non verbalisants de 2509.21344 ») et `f527257af5a2d` (Argon, F:l.142, protocole de 2604.28182 reproduit sur Gemma 2 9B avec une condition de non-verbalisation). `fc0b7405de5e0` et `fa06492536a80` prennent en outre un « organisme non verbalisant » comme cible de transfert. Un organisme qui sous-performe sans le dire est plus proche de la famille 1 (organismes saboteurs discrets) que les cinq fiches signalées. L'épreuve de `f527257af5a2d` nomme en une proposition un moyen d'obtenir la non-verbalisation ; je ne le reprends ni ne le reformule. Les résumés de la note ne le reprennent pas non plus : rien n'a fui, mais le signalement manque. La v2 ajoute un point 5 aux réserves ; elle n'exclut aucune fiche de plus, puisque leur objet est le détecteur, et la mère peut resserrer.
4. **Les cases d'axe sont comptées sur les 29 fiches** (§ 1, l. 39 : 11, 10, 8). Sur les 26 fiches lues, je compte : valeur pour l'audit 8, limite actuelle 10, comparaison à la boîte noire 8. Le compte « sur les 29 » suppose que les trois fiches exclues portent toutes l'axe « valeur pour l'audit ». La note dit les avoir classées sur leur titre seul ; ce compte en lit donc au moins un champ de plus. Je ne l'ai pas vérifié, pour ne pas ouvrir ces fiches. La v2 donne 8, 10 et 8 sur les 26.
5. **Le nombre de verdicts est faux** (l. 13). La note écrit « les 29 + 7 verdicts ». Le coffre contient 24 `verdicts-passe1-*.json` et 7 `verdicts-fusions-*.json`, hors compagnons, soit 31 = 24 + 7.
6. **Trois renvois de lignes du rapport de la fille sont faux** (§ 4.4). Le total réglé de 8,737566 USD est à **RA l. 39**, non aux l. 36-37, qui portent les lignes d'Astra et d'Argon. Les montants par espèce et par relais sont aux **l. 34-38**, non aux l. 31-35. Les valeurs elles-mêmes sont exactes.
7. **La nature de l'erreur d'Astra est omise** (§ 4.3). L'« erreur » du juge Astra sur une fusion (MF, événement n° 19) est, au journal du relais d'Astra (`relais-astra-journal.jsonl`, appel 80, 15:57:35 UTC), une **erreur de serveur du fournisseur (HTTP 500)**, et non un refus. La note dit avoir lu les quatre journaux de relais, mais elle ne cite que celui de Claude.
8. **Des citations entre guillemets ne sont pas littérales.** FI l. 4 et MF événement n° 17 portent « non écrite (sortie inexploitable : sortie inexploitable (statut refus)) », et non « non écrite (sortie inexploitable (statut refus)) ». FI l. 10 et 26 portent « jugée en partie (1 verdict(s) sur 2) », et non « (1 verdict sur 2) ». Enfin, la phrase attribuée à MD et MF ensemble (« hors scénario B … aucun appel, rien d'écrit ») est celle de MD (l. 315) ; MF dit « scénario B : passe « tableau » retirée par conception, aucun appel » (événement n° 12).
9. **L'inventaire des pièces lues est incomplet** (« Ce que j'ai lu »). Plusieurs pièces de l'extrait ne figurent dans aucune liste, ni « lu », ni « non lu », ni « absent » : les cinq journaux `verifier-*.log`, `verification-avant-lancement.json`, `manifeste-depart-lanceur-jangfeng-v1.json`, les cinq `controle-*.json`, `etat-final-relais-*.json` et `relais-*.log`, `registre-depense-cumulee-v1.jsonl`, `empreintes-sortie.txt`, `coffre/jf1-emplacement-sessions.json`, `lanceur.pid`, `run.chemin`, et un journal de démarrage vide. Aucune ne contient de fiche ; je les ai parcourues par leurs métadonnées seulement (statuts, montants, versions).
10. **Deux formulations dépassent ce que la note a lu** (§ 2.4 et § 5). « La moins chère des fiches » (`f90d3ad8cf1d7`) ne vaut que pour les 26 fiches lues : le coût des trois exclues n'a pas été lu. Par ailleurs, « aucune fiche ne relève d'un essai sans dépense de carte, sauf peut-être le rejeu de `f90d3ad8cf1d7` » se contredit : son proposeur le chiffre à « 8 heures de carte GPU » (F:l.373, champ coût).

## (1) Citations rouvertes

Toutes les lignes de départ et toutes les espèces des 29 fiches de F ont été recalculées par programme : la ligne où commence chaque clé, et `meta.proposeur` ou `meta.origine`. **Les 29 sont exactes**, comme les parents et les bras des 7 fusions (K) et les 8 paires (P). Parmi les citations rouvertes à la main, avec contrôle du résumé contre le texte :

| n° | citation de la note | espèce dite | constat |
|---|---|---|---|
| 1 | `f5354e2a27e2d`, F:l.165 | Argon | exacte ; tiers central des couches, injection ponctuelle, « nos résultats » § 7 : conformes |
| 2 | `fcf6183f07281`, F:l.512 | Fable | exacte ; témoin affiné sur démonstrations de qualité réduite, apparié à ± 2 points ; contrôle sur la courbe entière : conformes |
| 3 | `f09d98550d211`, F:l.2 | fusion, parents Argon et Astra | exacte (K : `f5354e2a27e2d`, `ff1d608f2a1f8`, bras Gu-Krenn) ; « Zone apparemment vierge, donc question » : conforme (R8) |
| 4 | `f09dc8b003e59`, F:l.26 | Opus | exacte ; 1, 4 et 16 démonstrations sur 10 pas ; courbe en nombre de démonstrations : conformes |
| 5 | `f8c41d345523a`, F:l.327 | Argon | exacte ; 3 instances verrouillées à graines différentes et 3 bénignes : conforme |
| 6 | `f90d3ad8cf1d7`, F:l.373 | Argon | exacte ; séquences de 40 actions ; 2 j, 8 h : conformes (voir correction 10) |
| 7 | `f555bcc122938`, F:l.188 | Opus | exacte ; organisme d'« insertion occasionnelle d'actions nuisibles » ; seuil sur 1 000 épisodes honnêtes entiers : conformes |
| 8 | `f73c2faaf531a`, F:l.304 | Astra | exacte ; citation « sans modifier les comportements pour viser le moniteur » littérale |
| 9 | `feee16a806f32`, F:l.605 | Opus | exacte ; la contradiction résumé / page 8 de 2509.21344 est bien dans la fiche (champ prédiction) ; présentée comme avis, non vérifiée (R7) |
| 10 | `f527257af5a2d`, F:l.142 | Argon | exacte ; Gemma 2 9B ; garde sur la persistance de la baisse d'exploration : conforme (voir correction 3) |
| 11 | `ff1d608f2a1f8`, F:l.628 | Astra | exacte ; organisme public lié au genre de l'utilisateur ; 2602.08877 : conforme |
| 12 | `ff51aac4334a8`, F:l.651 | Astra | exacte ; sycophancie sous pression sociale ; sous-ensemble défini avant les scores : conforme |
| 13 | `f0f64c6f5580b`, F:l.49 | Fable | exacte ; déclencheur paraphrasé, lecture après le déclencheur, plancher de 200 sondes : conformes |
| 14 | `f250e6dabc94a`, F:l.72 | Opus | exacte ; matrice 2 × 2, organisme bénin par recette, coût « 40 heures sinon » rendu par « 40 h si poids publiés » : fidèle |
| 15 | `f56722e76da87`, F:l.234 | Argon | exacte ; lecture au dernier jeton de l'invite : conforme |
| 16 | `f8ce47471e2c2`, F:l.350 | Astra | exacte ; référence étrangère, aucun positif de la recette cible, tâches non dangereuses : conformes |
| 17 | `f728f1b425b25`, F:l.281 | Astra | exacte ; organismes tenus entiers hors de la sélection du score : conforme |
| 18 | `fe2f9cb3b665c`, F:l.535 | Fable | exacte (voir correction 3) |
| 19 | `fc0b7405de5e0`, F:l.489 | Opus | exacte ; réplication scellée avant toute notation : conforme |
| 20 | `f6d460fb7cee9`, F:l.257 | fusion, parents Opus et Astra | exacte ; cinq bras par sens ; « au moins la moitié » ; antériorité « non tranchée » : conformes |
| 21 | FI l. 3-8, 9-24, 25-40 | — | lignes exactes ; citations non littérales (correction 8) |
| 22 | MF l. 694-741 (Kimi, n° 2 à 7) ; l. 764-842 ; l. 1791 | — | exactes : six « champs obligatoires manquants : axe », `prop-kimi` ; juges absents Opus 2, Astra 1 |
| 23 | RK ligne 2 | Kimi | exacte : 776,407 s, 23 346 jetons de sortie, 92 542 octets, 15:28:33 UTC |
| 24 | RC appels 45, 78, 105, 116 | Opus, Opus, Fable, Opus | exacte : statut REFUS à 15:37:57, 15:44:18, 15:52:36, 15:56:00 |
| 25 | RA l. 20-21, 24, 27-29 | — | exactes ; l. 31-35 et 36-37 fausses (correction 6) |
| 26 | ML l. 291-292 ; JP l. 5 ; MD l. 225, 154-161, 314-315, 349, 352, 368 | — | exactes : consigne de l'aiguilleur `f1cd9072…` ; « conforme : 60 pièces gelées » ; `aiguilleur_v53.py` `a856cdaa…` ; 67 concepts, 67 termes, source `0bac0776…` |
| 27 | `registres/go.md` l. 232-234 ; `registres/depenses.md` l. 351-352 | — | exactes. L'empreinte de `depenses.md` citée (`5af5646a…`) est celle de la version du commit `3ea4a963` (04:08 UTC) ; le registre a changé depuis (`244c4f7a`, 05:12 UTC, `a467ba68…`), mais ses lignes du 3 novembre sont inchangées et ne comptent toujours aucune ligne « Jang », « Feng » ni « GO-2026-11-03-12 » |
| 28 | R-1157, R-1162, R-1163, R-1166 | — | exactes ; R-1451 mal lue (correction 1) |
| 29 | inventaire l. 93, 119, 136, 162 ; inventaire v7 l. 504 | — | exactes |

Les montants sont tous exacts. Total réglé : 8,737566 USD pour 207 appels. Trace : 8,734978 USD. Écart de 0,002588 USD : le coût des cinq appels de contrôle (journal de lancement l. 11). Montants par espèce et par relais conformes à TR, et 8,74 USD au registre des décisions (R-1166). Les tailles des trois fiches exclues (2 135, 2 825 et 2 084 octets) sont celles de leur contenu en JSON compact, encodé en UTF-8 ; la fiche entière fait 2 298, 2 984 et 2 262 caractères.

## (2) Avis et faits ; règles R7 et R8

- Chaque résumé est présenté comme « avis du proposeur ». Les prédictions et les coûts sont dits « supposés » par le proposeur. Les doublons, les thèmes et les rapprochements avec les décisions du programme sont dits jugements du rédacteur. Je n'ai pas trouvé d'avis de modèle présenté comme un fait, hors l'attribution d'auteurs de la correction 2.
- **R7** : aucun chiffre d'article n'est repris comme vérifié. Les rares mentions (2609.36490, la contradiction de 2509.21344) portent « non vérifié ». Les chiffres repris dans les résumés (200 sondes aléatoires, 40 actions, 1, 4 et 16 démonstrations) décrivent l'épreuve proposée, non l'état de l'art.
- **R8** : les cinq fusions complètes (`f09d98550d211`, `fe71601aaae24`, `f2f4680f62e71`, `fa06492536a80`, `f6d460fb7cee9`) posent leur antériorité en question dans leur texte, et la note le rapporte ainsi. Le constat « aucune idée ne porte sur les juges de la recherche automatisée » est dit « mon constat » ; c'est une lecture de thème, pas une zone vierge.

## (3) Cloisonnement

- **Famille 2** (évasion des moniteurs et bras d'attaque). Trois fiches sont exclues : `f36047fc09df5` (Fable, F l. 119-141, 2 135 octets de contenu), `fb575dee72657` (Argon, F l. 466-488, 2 825 octets) et `fb2189e28d97b` (Fable, F l. 443-465, 2 084 octets). S'y ajoute le compagnon orphelin `docs/notes/ideation-organisme-v1/question-mere-reponses/consigne-argon-question-mere-v3.txt.sha256` (102 octets), conforme à l'inventaire, § C (question-mère de la course 2). Je n'ai pas lu ces fiches et ne peux donc pas juger leur classement. La note n'en résume rien, et déclare la vue partielle de `fb2189e28d97b`. Les noms de code (module du bras d'attaque, « A1-bis » dans RA l. 10 et dans les noms de version des relais) sont relevés comme noms seuls.
- **Famille 1** (organismes saboteurs discrets) : aucune exclusion. Il manque un signalement (correction 3). Les résumés ne reprennent aucun moyen de rendre un organisme discret.
- **Embargo** : aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni du premier test boîte blanche bis n'est cité. Les renvois à « nos résultats », § 6 et § 7, sont ceux des fiches, et la note n'en reprend aucun chiffre.
- **Classement non lu** : la note ne dit aucune fiche notable. Elle ne reprend pas non plus le compte « 2 notables » de BI, de TR et de RA ; c'est un choix déclaré, pas un oubli.

## (4) Oublis

- **Fiches** : les 26 fiches gardées sont toutes relevées, comme les deux fusions inachevées à contenu et l'entrée vide du rang 4. Rien ne manque.
- **Espèces** : les cinq espèces sont relevées (Kimi absent des fiches, motif établi). Les rôles, les juges, les lecteurs, l'aiguilleur et le metteur sont conformes à MF, au suivi des rôles et à TR (`par_role`).
- **Cellules** : il n'y a aucune cellule de collisionneur, faute de tour. R-1157 dit qu'« Opus propose sans tour préalable du collisionneur sur cette question », ce qui est conforme.
- **Pièces** : voir les corrections 7 et 9.
- **Déduction sur le juge** : celle de la note est cohérente avec le suivi des rôles de MF. Le juge Opus a un appel inexploitable à l'étape des juges (24 propositions) et un aux fusions ; le juge Astra en a un aux fusions. Une proposition a donc été classée sur le seul verdict d'Astra, et les deux fusions « jugées en partie » correspondent aux deux absences de l'étape des fusions.

## Limites

- Je n'ai lu ni le classement, ni les verdicts, ni les étiquettes, ni les trois fiches exclues. Je ne juge donc ni la valeur des fiches, ni le classement des exclues.
- Les résumés ont été comparés au titre, à l'hypothèse, à l'épreuve, au contrôle et au coût, pour 20 fiches lues en entier ou en grande partie. Pour les autres, la comparaison porte sur le titre, l'hypothèse et le coût.
- Le classement « voisine de la famille 1 » de la correction 3 est un jugement de lecture, comme celui de la note.
