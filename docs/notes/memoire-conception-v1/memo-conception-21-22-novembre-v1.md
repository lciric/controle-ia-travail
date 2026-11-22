# Mémoire de la conception des 21 et 22 novembre 2026 (v1)

> **Index, non preuve.** Ce mémo oriente la recherche ; il ne fait pas foi. Seule la source citée (chemin, empreinte, passage), relue, est opposable ; ce mémo et la bibliothécaire ne se citent jamais dans une décision (recommandation D3 de la réponse 32 de Fable, appliquée à titre provisoire). **Bibliothécaire en service, non éprouvée** (D4).

## 0. Mode d'emploi

- **Date et auteur.** 22 novembre 2026, vers 12:45 UTC. Session bibliothécaire (Claude Opus 5.5), fille de la session mère `session_01XJ6Mgr4LgbMsg5zLyRZCpG`. Demande : mot de Lazar du 22 novembre (`GO-2026-11-22-50`). Pièce de classe C (travail), **non contre-lue** ; selon D2 de la réponse 32, elle attend un contre-lecteur d'une autre lignée et l'accord de Lazar avant tout scellé « vérifié ». Le scellé posé ici est une empreinte de dépôt (R6), non une validation.
- **État épinglé.** `main` à `5b596acc`, lu sur la branche `claude/bibliothecaire-v1`. Tout fichier versé depuis est « postérieur au scellé ».
- **Fenêtre couverte.** Ce qui a été conçu, tranché ou retiré les 21 et 22 novembre, lu dans : l'inventaire des seconds regards (`docs/notes/seconds-regards-sabotage-inventaire-v1/inventaire-seconds-regards-invariants-noyaux-v1.md`, `02252df286503f8c`), intégré par renvoi (ses numéros 1.1 à 5.5 sont cités dans chaque fiche, ligne « Inventaire ») ; les décisions N-075 v3 et ses errata 1, 2 et 3 v2, N-076 et ses errata 1 et 2, N-077 (`docs/decisions/`) ; les trente-cinq réponses `reponse-*/relecture-fable-api.md` de `docs/notes/demandes-fable-api-2026-11-22-v1/` (demandes 1 à 30, sauf 24) ; `registres/go.md` (lignes 600 à 737, `GO-2026-11-21-01` à `GO-2026-11-22-50`, empreinte `d8e7639c7e8aa9d0`) ; `registres/decisions.md` (lignes 4478 à 4992, `R-4340` à `R-4853`, empreinte `75f4ab9603eba780`).
- **Méthode.** Dix agents de lecture (Opus 5.5), chacun sur un lot de sources, sous la même consigne et le même cloisonnement ; leurs extraits sont assemblés ici sans réécriture de fond (section 2), puis indexés par programme (sections 3, 6, 7). Les sections 1 et 4 sont de ma main.
- **Ce qui n'est pas couvert, et pourquoi.** La demande et la réponse 24 (nouveaux modes d'attaque, sous séquestre) ; tout ce que la liste d'autorisation exclut (`docs/notes/memoire-conception-v1/liste-autorisation-bibliothecaire-v1.md`, `31fc781d4fbe2c57`) : transcriptions, branches de sauvegarde, résultats chiffrés de 7a, 7b, T0.6, étape B, étape B bis, P3-bis, scores du barreau 5, préenregistrements. Les notes de conception que les décisions citent (adjudant, science de la détection, pince, percée…) ne sont connues ici qu'à travers l'inventaire et les décisions, non relues en entier. La réponse 32 (conception de mon rôle) est lue ; elle n'est pas extraite en fiches.
- **Estimation du manque.** Non mesurée. Les dix agents ont lu des lots disjoints ; un concept présent dans une source sans mot-clé reconnaissable par l'agent peut manquer. Les doublons entre lots sont **nombreux et voulus** (une même idée vue par la décision, le registre et la réponse de Fable) : la section 1.2 donne la fiche d'entrée de chaque grand concept. Une estimation par deux inventaires indépendants (capture-recapture) est proposée pour la v2 (réponse 32, § A.3).
- **Trois axes d'état.** La ligne « État » de chaque fiche mêle, dans cette v1, le statut dans le programme (retenu, retiré, ouvert, proposé non tranché), le statut d'antériorité (occupé, partiellement occupé, non cherché) et le statut de preuve (aucune mesure ; calcul « sous supposition »). La séparation en trois champs est à faire en v2. Une fiche tirée d'une réponse de Fable sans identifiant GO est une **proposition**, même si elle paraît décidée : vérifier au registre.
- **Primauté.** Quand un erratum existe, il prime : N-075 erratum 3 v2 > erratum 2 > erratum 1 > v3 ; N-076 erratum 1 prime. Exemple : la fiche GO-15 garde la lettre « alerte = nouveauté et preuve de dommage » du 21, que l'erratum 3 v2 de N-075 a réécrite en « motif et dommage au même endroit » (fiche N075-16).
- **Identifiants.** `[N075-nn]` décision N-075 ; `[N076-nn]` N-076 et N-077 ; `[GO-nn]` registre des accords ; `[RD21-nn]`, `[RD22-nn]` registre des décisions ; `[F01-nn]` réponses 1 à 7, `[F08-nn]` 8 à 14, `[F15-nn]` 15 à 21, `[F22-nn]` 22 et 23, `[F25-nn]` 25 à 30. Ils sont stables pour cette édition seulement.
- **Comment chercher.** Section 7 (paraphrases, ordre alphabétique) ; puis `grep -n -i` dans ce fichier ; puis la source. Degrés de certitude des réponses : « lu dans la source », « lu dans le mémo seulement », « rapprochement de ma part ». Trois négatifs : « non trouvé dans ce que j'ai lu », « hors périmètre », « sources en désaccord ».

## 1. Page phare

### 1.1 Huit idées porteuses, sans prérequis

1. **Le sabotage délibéré tient en trois clauses** : le produit est pire que celui que le même agent aurait rendu ; il le sait ; il ne le dit pas. Tout invariant cherché se déduit d'une clause (inventaire 3.1 ; science de la détection).
2. **Contre une menace diffuse, le levier fort est de mesurer l'issue et de corriger**, non de reconnaître l'attaque : le produit de chaque épisode, jugé après coup par un oracle exogène, sur une part tirée au hasard (N075-01, N075-03). Ce plancher d'audit au hasard est **occupé** par la littérature (« Blindfold », Gans et Holden, Podkopaev et Ramdas) : base citée, jamais revendiquée (`GO-2026-11-21-60`). Sa borne chiffrée n'existe pas tant que la probabilité que l'oracle reconnaisse un dommage n'est pas mesurée par des dommages plantés, strate par strate ; une strate non mesurée compte pour zéro (N075-05).
3. **Les sondes accélèrent et aiguillent ; elles ne garantissent pas** (N075-07). Toutes les lectures d'états internes reposent sur une même supposition (l'agent ne déplace pas ses représentations) et tombent ensemble : on compte les suppositions, pas les détecteurs (inventaire 5.1 ; F25-18 à F25-23). Une lecture ne compte comme intervention de plus que si elle ne tombe pas en même temps que le second lecteur (la seconde boîte noire), mesuré à fausses alertes égales (F25-19, F25-04).
4. **La défense jointe boîte noire et boîte blanche se dit en trois objets** : complémentarité (une mesure), étau (une hypothèse, plafonnée), bilan (une identité, seule revendicable sous verdict d'antériorité propre) (N075-13 à N075-15). Le signal de « dopamine » n'y ajoute aucune puissance au bilan : une date et une adresse (F25-01).
5. **Une alerte demande deux clés** : un motif reconnu par un regard et un dommage rendu par l'oracle au même endroit ; un motif seul envoie en file d'audit, jamais dans les témoins (N075-16, N075-18).
6. **La thèse du papier A a changé le 22** : la loi héritée de la dissimulation répartie (Ker, racine de n plus n carré sur m) n'est plus une thèse mais le **modèle nul** ; le résultat est l'écart mesuré à ce nul, sous une forme commune aux trois papiers (nul nommé, référence déclarée, écart mesuré, garantie portée par l'audit) (F22-01, F22-02, F25-40). Le lemme d'additivité et le théorème négatif sont **retirés comme résultats** (occupés, ou contredits par Arias-Castro, Bubeck, Lugosi 2012) et deviennent des questions (« étalement en séquentiel », « position ou dépendance ») (`GO-2026-11-22-24` ; F22-05, F22-07, F15-11, RD22-01 à RD22-03).
7. **Le noyau « connaître la bonne action et en choisir une autre »** (le passage obligé, les cœurs algorithmiques) est une question de recherche, non une hypothèse ; sa limite est écrite : l'honnête aussi calcule la bonne action (N075-20 ; F15-51 à F15-63).
8. **Deux invariants du programme sont touchés et non tranchés** : aucun score de moniteur ne revient à l'agent (N-053, point 5), et l'invariant de l'oracle contre le réapprentissage des sondes sur ses verdicts (N-060 v3, point 4 ; nœud du point 9 de N-075, Lazar « penche » pour l'option (b)) (N075-25).

### 1.2 Carte : la fiche d'entrée de chaque grand concept

| Concept | Fiche d'entrée | Autres fiches (même idée, autre source) | Inventaire |
|---|---|---|---|
| Mesurer l'issue et corriger | N075-01 | GO-13, RD21-32 | 2.1 |
| Plancher d'audit au hasard | N075-03 | N075-04, GO-18, RD21-21, F15-21 à F15-30 | 2.1 |
| Dommages plantés, q mesuré, strate à zéro | N075-05 | N075-06, GO-23, RD21-36, F15-41 | — |
| Sondes en accélérateur, non en garantie | N075-07 | | — |
| Recapture, « moniteur invalide » | N075-09 | GO-30, RD21-28 | 2.2 |
| Dilemme plutôt que décorrélation | N075-11 | GO-14 | 1.2 |
| Silence commun, chute conjointe | N075-12 | F25-19 à F25-26, F08-07 | 5.4 |
| Pince en trois objets | N075-13 | GO-25, RD21-23, F08-02 à F08-11, F25-01 | 2.4, 5.5 |
| Bilan de la pince | N075-14 | F08-10, F25-02 | 2.4 |
| Étau | N075-15 | GO-26, RD21-24, F08-09, F08-23 à F08-31, F25-25 | 5.5 |
| Règle à deux clés | N075-16 | GO-15 (lettre périmée), F25-09 | 2.16 |
| Bilan du produit (bilan matière) | N075-19 | GO-16 | 2.3 |
| Passage obligé, cœurs algorithmiques | N075-20 | GO-17, RD22-14, F15-51 à F15-63, F08-43, F01-46 | 4.1 à 4.4 |
| Lemme d'additivité | N075-22 | GO-44, RD21-20, RD22-02, F22-05, F25-42 | — |
| Théorème négatif | F15-11 | F15-12 à F15-17, RD22-03, F08-17, F22-07, F25-41 | — |
| Loi de la référence honnête (m, n, horizon) | N076-01 à N076-05 | GO-42, RD21-22, F01-19, F22-50 | — |
| Loi héritée comme modèle nul, thèse du papier A | F22-01 | GO-43, F08-12, F08-20, F25-38, F25-40 | — |
| Réapprentissage contre invariant de l'oracle | N075-25 | GO-20, RD21-33, N076-12 | 2.14 |
| Hasard du défenseur | N076-07, N076-08 | GO-22, F15 section C | 2.7 |
| Épreuves du devin | N076-13 | GO-21 | 2.17 |
| Marge asymétrique (H6) retirée | N076-24 à N076-28 | GO-47, RD21-34, F22-10 | — |
| Signal de « dopamine », second regard | F25-01 | GO-27, RD21-10, RD22-12, RD22-13 | 1.1 |
| Moniteur de dissonance | GO-37 | RD21-17 | 1.3 |
| Lot tenu à l'écart, équipe rouge | F22-59 | F15-37 à F15-42, GO-55, GO-56 | — |
| Protocole X, demande approfondie | GO-02 | GO-01, GO-03, RD21-01 | — |
| Test de devinette des questions neutres | F22-72 | F01-57, F25-15, RD22-15 | — |
| Coercition, corruption, flagornerie | F01-01 | GO-49, GO-50, F01-50 à F01-56 | — |
| Banc à dommage mesurable, vérité plantée | F08-33 | GO-53, RD21-15, RD21-39, F22-19 | — |
| Essaim contre isolé (organisme d'idéation) | F08-47 | F01-61, F01-62, GO-65 | — |
| Idées originales, puits étroits | F25-48 | GO-66 | — |

### 1.3 À ne pas confondre

- **Second regard** (un mécanisme de plus qui peut voir un sabotage) ; **second lecteur** et **seconde boîte noire** (le prédicteur de l'issue sur le texte seul, que la lecture interne doit battre : F25-05, inventaire 2.20) ; **seconde clé** (le dommage rendu par l'oracle, N075-16).
- **Jumeau honnête** (même modèle, même tâche, sans sabotage ; au banc seulement : « le jumeau d'un saboteur est un saboteur », N075-17) ; **jumeau textuel de la sonde** (= seconde boîte noire) ; **essai jumeau contre jumeau** (honnête contre honnête, pour la dispersion de référence : F01-24, F22-20, F25-35).
- **Pince** (les trois objets ensemble) ; **étau** (un seul des trois : l'hypothèse que tromper l'externe laisse une trace interne).
- **Bilan de la pince** (identité en deux termes, N075-14) ; **bilan du produit** ou bilan matière (comptes du produit contre le jumeau, garanties nucléaires, N075-19) ; **bilan d'incertitude** (thèse révisée du papier A, F08-20).
- **Plancher d'audit** (part tirée au hasard, porte la borne) ; **plafond de divergence** (log-rapport de l'agent contre la référence, inventaire 2.12) ; **plafond de l'étau** (le plus petit du rappel de la sonde et de la taxe de cacher) ; **plafond de la référence** (horizon au plus m, N-076).
- **« Moniteur invalide »** (recapture sous le compte attendu, N075-09) ; **« sonde invalide »** (attestation par micro-interventions secrètes, inventaire 2.10) ; **« pince ouverte »** (silence commun au-dessus du compte validé).
- **Mode tenu à l'écart** (N-054 : conçu à l'écart des moniteurs) ; **lot sous scellés** ou en quarantaine (la garde) ; **équipe rouge d'une autre famille** (l'auteur) : F22-66.
- **Loi héritée** (le nul de Ker, F22-01) ; **loi de la référence honnête** (N-076 : horizon au plus m) ; **loi d'échelle du dommage caché** (proposition de la réponse 4, F01-36).
- **Théorème négatif** (retiré) ; **« cécité au premier ordre »** (sa réécriture, F08-17) ; **seuls les mélanges de décisions sur un pas sont aveugles** (la phrase juste, F15-12).

## 3. Table des interactions avec le programme

Table construite par programme : une fiche y figure si son texte (définition, liens, attaques) nomme le point. Elle dit où chercher, non le sens du lien (appui, attaque ou contradiction), qui se lit dans la fiche.

| Point du programme | Fiches qui le touchent |
|---|---|
| H1 (gain de la boîte blanche, H1a, H1b) | N075-07, N075-13, N076-24, RD22-05, RD22-09, F08-01, F08-02, F08-04, F22-01, F22-24, F22-27, F22-59, F22-60, F22-64, F25-04, F25-40, F25-43 |
| H2 (accumulation) | N075-07, N076-01, N076-04, N076-23, N076-24, F22-01, F25-40 |
| H5 (diversité des moniteurs) | N075-11, N075-12, N076-19, GO-48, F15-42, F25-18, F25-19, F25-26, F25-27 |
| H6 (marge asymétrique, retirée) | N076-26, N076-28, GO-24, GO-47, GO-60, RD21-34, F22-10, F25-40 |
| H7 (riposte) | N076-13, N076-17 |
| H8 (validité de construit) | N075-20, N076-07, N076-24, GO-49, F22-27, F22-54 |
| H9, H10 | N076-28 |
| HC1 (déférence des juges) | N075-02 |
| HC2, HC2b (étau, trahison par les activations) | N075-15, F08-09, F22-42 |
| HC5 (quorum) | N075-11, N075-12 |
| Porte G1 | N076-05, N076-11, N076-24, GO-45, GO-46, GO-52, GO-56, GO-57, GO-58, RD21-22, RD21-46, RD21-47, RD21-48, RD22-09, F01-14, F01-20, F01-25, F01-26, F01-32, F01-35, F01-42, F01-48, F01-63, F08-01, F08-02, F08-20, F15-40, F22-11, F22-14, F22-17, F22-29, F22-50, F22-52, F22-59, F22-64, F25-12, F25-24, F25-34 |
| Porte G2 | N076-24, F22-29, F22-30, F22-33, F22-40, F22-50 |
| Papier A | N075-01, N075-03, N075-07, N075-22, N076-01, N076-24, N076-26, N076-28, GO-13, GO-16, GO-18, GO-24, GO-25, GO-39, GO-42, GO-44, GO-45, GO-47, GO-72, RD21-10, RD21-19, RD21-20, RD21-22, RD21-23, RD21-34, RD21-46, RD22-01, RD22-05, RD22-07, F01-07, F01-10, F01-25, F01-34, F01-36, F01-68, F08-01, F08-02, F08-12, F08-18, F08-20, F08-33, F15-11, F15-12, F15-14, F15-21, F15-23, F15-25, F15-28, F15-31, F15-32, F15-33, F15-35, F15-43, F15-46, F15-50, F15-51, F15-57, F15-63, F22-01, F22-05, F22-10, F22-11, F22-13, F22-14, F22-19, F22-23, F22-24, F22-25, F22-26, F22-27, F22-29, F22-39, F22-44, F22-59, F25-01, F25-02, F25-04, F25-14, F25-19, F25-30, F25-38, F25-40, F25-44, F25-46, F25-47 |
| Papier B | N075-22, N076-04, GO-33, GO-48, RD21-26, RD22-01, RD22-02, RD22-03, RD22-05, F01-09, F01-24, F08-18, F08-33, F08-38, F08-41, F15-11, F15-14, F15-31, F15-34, F22-19, F22-23, F22-28, F22-29, F22-30, F22-32, F22-34, F22-35, F22-37, F22-38, F22-40, F22-47 |
| Papier C | N075-02, N076-10, GO-26, GO-49, RD21-14, RD21-46, F01-08, F01-11, F01-33, F01-44, F01-50, F01-53, F01-54, F08-09, F08-31, F08-32, F15-24, F15-31, F15-34, F15-37, F22-08, F22-19, F22-24, F22-27, F22-41, F22-42, F22-43, F22-44, F22-45, F22-46, F22-47, F22-48, F22-49, F22-52, F22-55, F25-59 |
| Invariant N-053 (aucun score de moniteur dans l'entraînement de l'agent) | N075-07, N075-08, N076-07, N076-10, N076-12, N076-17, N076-24, N076-26, RD21-11, RD21-26, RD21-33, RD21-38, F01-08, F01-13, F01-14, F01-22, F01-25, F01-48, F01-53, F01-55, F01-66, F01-67, F08-29, F08-30, F08-42, F15-01, F15-02, F15-26, F15-33, F15-37, F15-49, F15-58, F15-59, F22-53, F22-66, F22-71, F25-05, F25-06, F25-12, F25-16, F25-17, F25-25, F25-27, F25-58 |
| Invariant de l'oracle N-060 | N075-02, N075-08, N075-09, N075-19, N075-25, N076-17, GO-13, GO-20, RD21-22, RD21-32, RD21-33, F25-27 |
| N-062 (reconception des sondes) | N075-07, N075-20, N075-25, N076-12, GO-56, RD21-38, RD21-47, F01-32, F01-42, F15-40, F15-44, F22-27, F22-59, F22-65, F25-34 |
| N-054 (mode tenu à l'écart) | N075-25, N076-12, N076-24, N076-26, GO-56, RD21-48, RD22-11, RD22-25, RD22-26, F01-14, F01-64, F15-08, F15-25, F15-37, F15-38, F15-39, F15-40, F15-41, F15-44, F15-48, F15-52, F15-63, F22-59, F22-60, F22-62, F22-64, F22-65, F22-66, F25-07, F25-33, F25-34 |
| Organisme d'idéation, collisionneur, essaim | N075-06, N075-19, N075-25, N076-09, N076-23, N076-25, N076-26, N076-27, N076-28, GO-02, GO-03, GO-06, GO-08, GO-11, GO-12, GO-23, GO-28, GO-48, GO-52, GO-55, GO-61, GO-65, GO-66, GO-67, GO-68, GO-74, GO-75, RD21-01, RD21-02, RD21-05, RD21-07, RD21-09, RD21-12, RD21-13, RD21-14, RD21-37, RD21-45, RD21-50, RD21-51, RD21-52, RD22-15, RD22-20, RD22-24, RD22-25, F01-11, F01-15, F01-17, F01-24, F01-36, F01-39, F01-46, F01-47, F01-48, F01-54, F01-57, F01-61, F01-64, F01-67, F08-01, F08-06, F08-18, F08-37, F08-39, F08-41, F08-43, F08-44, F08-47, F08-48, F08-50, F08-51, F08-52, F08-53, F08-55, F08-56, F08-57, F08-59, F08-60, F15-01, F15-04, F15-05, F15-14, F15-20, F15-24, F15-25, F15-34, F15-36, F15-38, F15-49, F15-51, F15-56, F15-59, F15-61, F15-62, F22-09, F22-23, F22-29, F22-32, F22-33, F22-40, F22-46, F22-48, F22-50, F22-52, F22-56, F25-13, F25-15, F25-16, F25-17, F25-35, F25-48, F25-49, F25-50, F25-52, F25-53, F25-54, F25-57, F25-58, F25-59, F25-60 |
| Bras A (organismes discrets) | N075-19, GO-08, GO-34, GO-76, RD21-51, F15-38, F25-17 |

## 2. Fiches de concepts

Une fiche par concept, idée, décision ou objet conçu, telle que l'agent de lecture l'a extraite de son lot (définition, synonymes et paraphrases, source et empreinte de 16 signes, état, liens, ce qui l'attaque, rattachement à l'inventaire). Les citations entre guillemets sont celles des sources ; les chiffres sont soit des citations d'articles, soit des illustrations « sous supposition », jamais des résultats cloisonnés. La section 2 suit la section 3 pour que la table reste en tête.

### 2.1 Décision N-075 v3 et ses errata (mesurer l'issue, plancher, deux regards) (`N075`)


> Fichiers lus (dans `docs/decisions/`), empreintes (16 premiers signes du sha256) :
> - v3 : `decision-N-075-issue-plancher-et-deux-regards-v3.md`, `5aed4bab1172b181` (en entier, sections 0 à 14, relevé de méthode).
> - erratum 1 : `…-v3-erratum-1.md`, `c6efeccfafca4158` (quatre corrections de lettre, vérification d'Opus 5.5).
> - erratum 2 : `…-v3-erratum-2.md`, `b19852b47a90e902` (choix de Lazar, `GO-2026-11-21-61`, consignés par la mère).
> - erratum 3 v2 : `…-v3-erratum-3-v2.md`, `fbe3298ec358fa9b` (prime sur tout ; remplace l'erratum 3, `d51863d24a379864`, comparé par `diff` seulement).
> - v1 `f1b77e66c1742e24` et v2 `997bc0b3fc238bf3` : survolées pour ce qui a été retiré.
> - Inventaire de rattachement : `docs/notes/seconds-regards-sabotage-inventaire-v1/inventaire-seconds-regards-invariants-noyaux-v1.md` (titres seulement).

> Règle de lecture de toute la décision : « non trouvé » ne veut jamais dire « libre » (R8) ; aucune revendication avant le verdict d'antériorité du lecteur des voisins (décision D-7 de la note sur l'adjudant, `GO-2026-11-21-46`, `-51`). Ordre de primauté : erratum 3 v2 > erratum 2 > erratum 1 > v3.

> **Ce que l'erratum 3 v2 change par rapport à l'erratum 3 (v1)** : vingt et un passages au lieu de vingt (ajout de R-15 bis : « toute politique d'attaque dont le dommage tombe dans une strate où la reconnaissance de l'oracle est mesurée », au lieu de « dont l'oracle voit le dommage ») ; au point 9, ajout « la suite d'une annonce relève du point 2 de la section 11 de la v3, laissé tel quel (à confirmer) » ; pour le lemme, le prix de la garantie et la détection avant le dommage « sortent parce que le reste ne les nomme pas, non parce qu'ils seraient occupés », la détection avant le dommage se cite sous sa forme classique (rapport KfK 3935) ; l'invariance entre agents n'est gardée que par lecture de l'auteur et sort si la note mathématique ne l'établit pas.

> **Ce que l'erratum 3 v2 corrige de l'erratum 2** (section 6) : rend « avec le coût du report » au reste du lemme ; rend au point 11 « (genre et dose) », « par une borne exacte », « aucune borne n'y est écrite » et « ne décide pas la campagne » ; remplace la ligne pour `CLAUDE.md` (« réentraînement en service ouvert » pouvait se lire « permis » ; « signal » au lieu de « motif » ; perte de « jamais revendiquée », « hors porte », « non en garantie », « dilemme plutôt que décorrélation », « pince en trois objets ») par le fichier `docs/decisions/ligne-claude-md-N-075-v1.md` (non ouvert ici).

> ---

#### [N075-01] Mesurer l'issue et corriger (le levier fort contre le diffus)
- Définition : contre une menace diffuse, la garantie ne repose pas sur la reconnaissance de l'attaque mais sur le jugement après coup du produit des épisodes (l'issue) par un oracle, suivi d'une correction. Reconnaître et incriminer sont des leviers faibles ; vérifier ce qui a été produit est le levier fort.
- Synonymes et paraphrases : « le levier fort est de mesurer l'issue et de corriger » ; « juger le produit, pas l'intention » ; « vérifier le résultat plutôt que détecter l'attaque » ; point 1 de N-075 ; « outcome-based control ».
- Source : v3, section 0 et section 2 ; `5aed4bab1172b181`.
- État : retenu, mot de Lazar « go il faut l'inscrire dans le programme et l'amender en conséquence », `GO-2026-11-21-51`. Lecture du concepteur, non un résultat : rien revendiqué.
- Liens : papier A (thèse, l. 43 et l. 74 du programme) ; plancher d'audit au hasard ; « corriger » ; chantier saboteur et sondes.
- Ce qui l'attaque : Terekhov et al. (2606.08892 v2, p. 2) jugent déjà surveiller « less promising » et se tournent vers l'entraînement ; Wen, Hebbar et al. (2411.17693) traitent déjà la menace distribuée par accumulation. `GO-2026-11-21-61` accorde « auditer des actes plutôt que des issues », qui touche ce levier et n'a pas encore de texte.
- Inventaire : 2.1 (cadre).

#### [N075-02] Oracle exogène, et couverture de l'oracle
- Définition : un oracle dont la règle ne dépend ni du mode d'attaque, ni de l'agent, ni d'aucun moniteur, et qui a passé ses épreuves (N-060 v3) ; sur le banc actuel, l'oracle de couverture des contrôles de l'article, lu contre le jumeau honnête. Sa couverture est l'ensemble des sortes de dommage qu'il sait reconnaître ; hors couverture, le dommage n'existe pas pour lui.
- Synonymes et paraphrases : « l'oracle sur le produit » ; « l'issue » ; « juge exogène » ; « ce que l'oracle voit » ; « point unique de défaillance ».
- Source : v3, section 1 (vocabulaire) ; `5aed4bab1172b181`.
- État : retenu (vocabulaire), appuyé sur N-060 v3.
- Liens : plancher d'audit au hasard ; identification de l'oracle par dommages plantés ; HC1 et papier C (lecteurs génératifs persuadables).
- Ce qui l'attaque : ses lecteurs lisent le produit et peuvent être persuadés par lui (« indépendante des moniteurs et de l'agent, non du texte ») ; un mode qui les persuade sort de la couverture ; l'oracle devient le point unique de défaillance. Trouvaille de côté : l'oracle fait de lecteurs génératifs est un test naturel de la loi de déférence (HC1).
- Inventaire : nouveau (support de 2.1).

#### [N075-03] Plancher d'audit au hasard
- Définition : une part p des épisodes réels, tirée en secret et indépendamment de tout ce que l'agent observe et de tout score, est jugée par l'oracle exogène ; un test valide à tout instant sur le dommage audité sonne l'alarme. Sous plafond de dommage par épisode, il borne le dommage cumulé avant l'alarme, dans les strates où la reconnaissance de l'oracle est mesurée.
- Synonymes et paraphrases : « plancher » ; « audit tiré au hasard » ; « random audit floor » ; « vérification différée sur sous-échantillon » (environnement (a), l. 122) ; « base hors des deux boîtes » ; C3 du contre-lecteur.
- Source : v3, sections 1, 2, 10 ; erratum 1 C-1, C-2 ; erratum 3 v2, sections 4.1 et R-15, R-15 bis, R-16, R-17 ; `fbe3298ec358fa9b`.
- État : **occupé par la littérature** : affirmé comme base nommée et citée, jamais revendiqué ; « Ne pas écrire » : « premier plancher », « le plancher comme apport du programme ». Retenu comme base (`GO-2026-11-21-51`).
- Liens : papier A ; jeu de contrôle (budget d'audit b, l. 72) ; seuils stochastiques (l. 168 : une part du budget tirée sans égard au score) ; chantier « papier dopamine » et moniteur de dissonance (écriture exploratoire d'abord, D-5 « b mais phase exploratoire avec a d'abord ») ; N-076 (table du seuil au taux d'audit).
- Ce qui l'attaque : occupé par Zhu, Zuo, Sun « Blindfold » (2610.37055), Gans et Holden (2609.38262), Podkopaev et Ramdas (2110.06177, excès sur risque de référence). Limites : rien contre un coup unique, hors couverture, dans une strate non mesurée, sous l'excès toléré, sans horizon, sans référence honnête, si l'oracle est trompé ; Ge-Wang et al. (choisir quand attaquer) ; tirage devinable.
- Inventaire : 2.1.

#### [N075-04] Forme restreinte de la borne du plancher : deux régimes, horizon, excès toléré
- Définition : si l'honnête ne commet jamais le dommage, une prise suffit et la probabilité d'être pris au n-ième épisode endommagé est 1 − (1 − p·q)^n, avec le q le plus bas que le saboteur peut choisir. Si l'honnête commet aussi ce dommage (le régime du programme), « pour toute politique d'attaque » est faux sans horizon : la garantie se dit sur un horizon donné, avec un taux de dommage honnête de référence, une grille de mises descendant vers zéro et un excès toléré écrits d'avance.
- Synonymes et paraphrases : « régime d'excès » ; « le saboteur qui ralentit » ; « borne à horizon » ; « excès sur risque de référence » ; correction A1 ; V7.
- Source : v3, section 2, « Forme restreinte de la borne » ; erratum 3 v2, section 4.1 ; `5aed4bab1172b181`, `fbe3298ec358fa9b`.
- État : retenu ; les nombres (quelques centaines d'épisodes à 1 % d'audit) sont des illustrations **sous supposition**, aucune donnée du programme.
- Liens : plancher ; référence honnête en service ; identification de l'oracle.
- Ce qui l'attaque : sous un excès critique fixé par la plus petite mise, l'alarme peut ne jamais venir ; un saboteur sous l'excès toléré n'est jamais pris (son dommage est « borné par définition ») ; recalcul du contre-lecteur non rejoué par l'auteur.
- Inventaire : 2.1.

#### [N075-05] Identification de l'oracle mesurée par dommages plantés ; strate non mesurée comptée à zéro
- Définition : la probabilité q que l'oracle reconnaisse un dommage qu'il regarde n'est pas supposée : elle se mesure par des dommages connus plantés par un tiers dans des produits honnêtes, strate par strate (genre et dose), par une borne exacte (borne inférieure de q au niveau déclaré). Toute garantie porte le minimum de q sur les strates mesurées et les nomme ; une strate non mesurée compte pour zéro, aucune borne n'y est écrite.
- Synonymes et paraphrases : « q mesuré par dommages plantés » ; « strate non mesurée à zéro » ; « dommage planté » ; « strate » ; « strate mesurée » ; « couverture mesurée » ; point 11 de la section 11 ; décision D-2 de la note sur la couverture de l'oracle ; « alors qu'elle se mesure par des dommages plantés : go ».
- Source : v3, section 11, point 11 ; erratum 2 ; erratum 3 v2, section 1 (point 11), 4.1, A-1, A-2, A-3, R-14 à R-17.
- État : retenu, `GO-2026-11-21-61`, option (a). Aujourd'hui aucune strate n'est mesurée : aucune borne chiffrée du plancher ne s'écrit, au banc comme en service. Les épreuves d'admission de l'oracle (N-060 v3, point 2) ne sont pas une mesure de q.
- Liens : plancher ; N-076 (sa table du seuil au taux d'audit se lit avec le même q, à porter) ; campagne de dommages plantés.
- Ce qui l'attaque : la mesure a un prix (des dizaines de plants sans manque par strate pour borner le manque à quelques pour cent) ; qui plante et ce qu'il voit relève du cloisonnement, non tranché ; « Ne pas écrire » : un q supposé écrit comme mesuré.
- Inventaire : nouveau (complète 2.1).

#### [N075-06] Campagne de dommages plantés par un tiers
- Définition : la campagne qui mesurerait q strate par strate : qui plante, quelles strates, quel cloisonnement, quel prix. Elle conditionne toute borne chiffrée du plancher.
- Synonymes et paraphrases : « plants » ; « dommages plantés » ; décision D-3 de la note sur la couverture de l'oracle ; « collisionneur pour avoir une confiance plus élevée ».
- Source : v3, section 11, point 11 (dernière phrase) ; erratum 3 v2, sections 2 et 3, point 3.
- État : ouvert ; nœud (dépense et cloisonnement : devis et mot de Lazar), après le collisionneur (`GO-2026-11-21-61`).
- Liens : identification de l'oracle ; protocole X et collisionneur.
- Ce qui l'attaque : coût ; risque de fuite du cloisonnement vers les concepteurs de moniteurs.
- Inventaire : nouveau.

#### [N075-07] Sondes et moniteurs en accélérateur et en aiguillage, non en garantie
- Définition : les sondes et moniteurs servent à faire sonner l'alarme plus tôt (accélérateur) et à dire quoi auditer ou relancer (aiguillage) ; la borne vient du plancher. Aucun moniteur du programme ne porte de garantie de détection sur un genre de sabotage jamais vu ; un gain de la boîte blanche établit un gain sur les modes éprouvés, mode tenu à l'écart compris, non la tenue devant tout genre inconnu.
- Synonymes et paraphrases : « sondes : accélérateur, non garantie » ; « vitesse et aiguillage » ; « le gain de la boîte blanche dans la pince » ; décision D-1 de la note sur l'adjudant.
- Source : v3, section 2 (énoncé, points 1 et 5), section 3 (point 2) ; `5aed4bab1172b181`.
- État : retenu, `GO-2026-11-21-46` et `-53`.
- Liens : H1, H2 (énoncés inchangés) ; papier A ; N-062 (reconception des sondes inchangée) ; N-053 point 5 : l'aiguillage qui relance ou choisit selon un score est une règle de sélection déclarée, jamais un signal d'entraînement de l'agent.
- Ce qui l'attaque : Li et al. (2611.15835) : sans hypothèse, toute borne indépendante des données sur un mode jamais vu vaut 1 ; « Ne pas écrire » : « garantie de détection » pour une sonde, « moniteur valide hors distribution ».
- Inventaire : nouveau.

#### [N075-08] « Corriger » : la liste fermée des suites d'une alarme
- Définition : dans N-075, corriger veut dire arrêter, relancer, confier au modèle de confiance, vérifier davantage, refaire les témoins sur des honnêtes exogènes, rien d'autre. L'entraînement de l'agent sur l'issue n'est pas ouvert.
- Synonymes et paraphrases : « corriger » ; « entraîner l'agent sur l'issue » (ce vers quoi se tournent Terekhov et al.) ; point 3 de la section 11.
- Source : v3, section 1 et section 11, point 3.
- État : retenu pour la liste ; l'entraînement sur l'issue est fermé, recommandation de le laisser fermé (confiance du contre-lecteur 0,8) ; s'il s'ouvre, bras à part et nœud. Non nommé à `GO-2026-11-21-61` : reste tel que la v3 le laisse.
- Liens : N-060 v3 point 4 (premier invariant touché) ; N-053 point 5.
- Ce qui l'attaque : Terekhov et al. préfèrent l'entraînement.
- Inventaire : nouveau.

#### [N075-09] Recapture, et la règle « moniteur invalide »
- Définition : parmi les épisodes endommagés que l'audit au hasard trouve, le compte de ceux que le moniteur avait signalés ; une règle en tirerait l'annonce qu'un moniteur est invalide. C'est une quantité rapportée, sans critère.
- Synonymes et paraphrases : « recapture » ; « capture-recapture » ; « moniteur invalide » ; correction A2 ; revendication 1 de la lecture des voisins.
- Source : v3, sections 1, 2 (« ce qui pourrait être revendiqué », (ii)), 11 point 2.
- État : partiellement occupé ; il n'en reste qu'une question (R8) : la règle portée sur le rappel face à un agent qui choisit où et quand nuire, avec borne écrite du dommage accumulé avant qu'elle sonne ; toute revendication est un nœud ; à re-dériver par un agent qui ne reçoit que l'énoncé (`GO-2026-11-21-55`, D-2). Point 2 (annoncer n'est pas sélectionner, trois précisions) : à confirmer, non tranché à `GO-2026-11-21-61`.
- Liens : N-060 v3 point 4 ; silence commun ; asymétrie d'apprentissage (point 9) ; N-076 (boucle audit-recapture-réapprentissage).
- Ce qui l'attaque : occupé par Podkopaev et Ramdas, Zhang et al. (2602.02229), Gao et al. (2611.15197), Li et al., Greenblatt et al., Shire et Kim (2611.19216). En service l'oracle ne sépare pas le sabotage du dommage honnête : sans connaître la part du sabotage, la règle déclare invalide un moniteur valide plus d'une fois sur deux (sous supposition) ; elle n'annonce donc en service qu'après l'alarme du plancher et avec une estimation de cette part.
- Inventaire : 2.2.

#### [N075-10] Le plancher hors de la liste des bases de la porte de fin de phase 1
- Définition : le plancher ne se mesure pas en rappel à 1 % de fausses alertes et n'entre pas dans les bases que le séquentiel boîte blanche doit battre ; il se rapporte à côté, en dommage cumulé à l'arrêt, à étiquettes égales.
- Synonymes et paraphrases : « plancher hors porte » ; point 1 de la section 11 ; « ce que la sonde ajoute au plancher ».
- Source : v3, section 2 (« ce qui ne change pas »), section 11 point 1.
- État : proposé non tranché : recommandation (a) « non, rapporté à côté » jusqu'aux mesures exploratoires (0,65 ; contre-lecteur 0,7), à rouvrir avant le scellement du préenregistrement de cette porte ; nœud sans défaut. Non nommé à `GO-2026-11-21-61`.
- Liens : N-008, N-056 ; contraste à témoin apparié (`GO-2026-11-18-48`, brouillons N-074 non retenus) ; métrique « latence (alerte contre dommage cumulé) » du plan à deux fois deux cases.
- Ce qui l'attaque : « la sonde détecte » peut passer la porte sans dire ce qu'elle ajoute au plancher.
- Inventaire : nouveau.

#### [N075-11] Deux regards tels qu'échapper à l'un expose à l'autre : le dilemme plutôt que la décorrélation
- Définition : un second regard se juge au dilemme qu'il pose (une relation que l'honnête respecte et que le dommage viole, de sorte que se cacher de l'un fait apparaître à l'autre), non à sa décorrélation. Là où l'attaquant défait chaque regard séparément, deux alertes réunies n'ajoutent pas de puissance.
- Synonymes et paraphrases : « deux regards » ; « dilemme » ; « décorrélation » (concept rival) ; « Ce qui vaut : deux regards tels qu'échapper à l'un expose à l'autre » ; « statistique de relation, non deux marginales » ; dilemme valeur contre issue.
- Source : v3, sections 1 et 3 ; `5aed4bab1172b181`.
- État : retenu, `GO-2026-11-21-51`. Rien revendiqué hors du bilan.
- Liens : H5 (diversité des moniteurs), HC5 (quorum hétérogène : aucun texte ne l'appelle « dilemme » sans avoir mesuré le silence commun), parade « apprentissage à corrélation négative » (l. 146), théorème négatif N-003 (justification interne) ; pince.
- Ce qui l'attaque : un dilemme même parfait ne descend pas l'aveuglement commun sous 2m − 1 (m : part des attaques neuves que chaque regard manque) ; il ne paie que si chaque regard en voit au moins la moitié (sous supposition ; correction A4). Johnston et al. (2504.08812), McKenzie et al. (2506.24068), Bailey et al. (2412.09565) : pannes communes.
- Inventaire : 1.2 (dilemme valeur contre issue) ; nouveau pour la règle générale.

#### [N075-12] Silence commun des regards sous attaque (recapture à deux mâchoires)
- Définition : la part des épisodes endommagés audités que tous les regards ont manqués ensemble ; quantité rapportée là où de tels épisodes existent.
- Synonymes et paraphrases : « silence commun » ; « recapture à deux mâchoires » ; « angle mort commun ».
- Source : v3, section 3, point 3 ; section 11 point 2 (iii).
- État : retenu comme quantité rapportée, sans critère ; énoncé de H5 inchangé.
- Liens : H5 ; HC5 ; recapture ; invariant de l'oracle (même lecture « annoncer n'est pas sélectionner »).
- Ce qui l'attaque : demande des épisodes endommagés audités, donc le plancher et l'oracle.
- Inventaire : 2.15.

#### [N075-13] La pince en trois objets : complémentarité, étau, bilan
- Définition : la défense jointe d'une boîte noire et d'une boîte blanche se dit en trois objets : la complémentarité (ce que l'interne capture parmi les manqués de l'externe, à fausses alertes partagées : une mesure), l'étau (tromper l'externe laisserait une trace interne : une hypothèse), le bilan (une identité). Seul le bilan pourrait se revendiquer devant une attaque jamais vue.
- Synonymes et paraphrases : « pince » ; « pince en trois objets » ; décision D-1 de la note sur la pince ; « la pince tient hors distribution » (à ne pas écrire).
- Source : v3, sections 0, 1, 3 ; `5aed4bab1172b181`.
- État : retenu, `GO-2026-11-21-53`. Le mot entre au programme à la prochaine version (§ 8.4 « Deux regards »).
- Liens : H1 (inchangé), plan à deux fois deux cases (inchangé) ; banc de la course de l'adjudant ; mâchoire externe d'octobre (D-4 de la note sur la pince, non tranchée).
- Ce qui l'attaque : « Ne pas écrire » : « la pince tient devant des attaques jamais vues » ; pannes communes (Johnston et al., corrélation de performances, non de pannes ; Bailey et al.).
- Inventaire : 2.4 et 5.5.

#### [N075-14] Le bilan de la pince (identité et invariance au partage)
- Définition : dommage vu par l'oracle = (référence honnête − lecture du suspect) + (lecture du suspect − issue) ; un télescopage. Quoi que le suspect fasse de sa lecture, la somme vaut le dommage que l'oracle voit, et zéro s'il ne voit rien.
- Synonymes et paraphrases : « bilan de la pince » ; « identité en deux termes » ; « invariance au partage » ; « seul le bilan se revendique » ; V5.
- Source : v3, sections 1, 3 ; relevé de méthode, pas 6.
- État : pourrait se revendiquer, sous un verdict d'antériorité **qui lui soit propre** (la lecture des douze voisins ne l'a pas examiné ; aucune recherche d'antériorité faite : question) ; `GO-2026-11-21-53`. Versé au banc de la course de l'adjudant avec trois témoins « doit mourir » (premier terme seul, second terme seul, réunion de deux alertes à pannes communes), sans dépense (`GO-2026-11-21-50`).
- Liens : référence honnête en service ; épreuves sans attaque (netteté de la référence, dissociation chez l'honnête), exploratoires d'abord ; dilemme valeur contre issue (terme du milieu).
- Ce qui l'attaque : l'identité est élémentaire, la valeur est dans la mesure ; sonne à tort sous dérive bénigne à référence périmée ; sans référence honnête exogène en service, aucun appui hors du banc ; Arnold et al. (2109.11761, calibration valide à tout instant) à lire.
- Inventaire : 2.4.

#### [N075-15] L'étau (trahison par les activations)
- Définition : la supposition que tromper le regard externe laisse une trace interne. Elle reste une hypothèse à tester, jamais une garantie.
- Synonymes et paraphrases : « étau » ; « trahison par les activations » (HC2b) ; « la mâchoire interne ».
- Source : v3, sections 1, 3 (points 5 et « ce qui ne change pas »).
- État : retenu comme hypothèse ; énoncé de HC2b inchangé ; comment le rendre solide passe par le concepteur, le collisionneur puis l'organisme (`GO-2026-11-21-53`), hors de N-075.
- Liens : HC2b, N-068 (sonde qui lit l'agent auteur, inchangée) ; pince.
- Ce qui l'attaque : contre-indice déjà noté de HC2b ; McGuinness et al. (2512.11949) : évasion apprise des représentations ; Bailey et al. : obscurcissement.
- Inventaire : 5.5.

#### [N075-16] La règle à deux clés : motif et preuve de dommage au même endroit
- Définition : une alerte demande qu'un regard reconnaisse un motif **et** qu'une preuve de dommage rendue par l'oracle soit trouvée au même endroit (même épisode, même artefact). Motif sans preuve : l'épisode monte dans la file d'audit prioritaire, ou le moniteur s'abstient, et n'entre jamais dans les témoins ; preuve sans motif : relève du plancher, sans seconde clé.
- Synonymes et paraphrases : « alerte à deux clés » ; « alerte = nouveauté et preuve de dommage ensemble » (lettre d'origine) ; « alerte = motif et dommage au même lieu » ; « motif seul : audit, jamais témoin » ; « théorie du danger » ; « signaux de danger » ; correction A6 ; point 8.
- Source : v3, section 4 ; erratum 2 ; erratum 3 v2, section 1 (point 8), 4.3, R-4 à R-10.
- État : retenu dans sa forme réécrite, `GO-2026-11-21-61`, option (a) ; l'écart à la lettre de `GO-2026-11-21-51` (« nouveauté seule = mise à jour des témoins ») est accordé ; « nouveauté » devient « motif reconnu par un regard ». Rien revendiqué : règle d'exploitation qui aiguille l'audit, pas une alerte plus sûre que le plancher. Hors du taux de fausses alertes d'une porte (toute sonnerie y compte).
- Liens : sondes non supervisées (Mahalanobis, l. 143) et détecteurs d'anomalie : deux issues écrites d'avance dans tout préenregistrement à venir ; asymétrie d'apprentissage (l. 170) ; témoins exogènes.
- Ce qui l'attaque : la source (Aickelin et Cayzer, 0801.3549) ne porte pas la nouveauté comme première clé (« does not respond to non-self but to danger ») et sa seconde moitié (tolérance) transposée est la voie par laquelle un saboteur se fait accepter ; Zhong et Raghunathan (2508.00161) : plage élargie pas à pas ; un attaquant sans motif échappe à la première clé ; « occupé dans sa forme » non établi (zone séduisante, R8) ; plus d'audits.
- Inventaire : 2.16 (et 1.14 pour la nouveauté).

#### [N075-17] Témoins exogènes, jamais le flux du suspect ; jumeau honnête au banc seulement
- Définition : les témoins sont des épisodes honnêtes d'un régime, exogènes au suspect, sur lesquels un moniteur est calibré ; un épisode du suspect, signalé ou non, n'y entre jamais. Le jumeau honnête (même modèle, même tâche, sans sabotage) vaut au banc ; en service, « le jumeau d'un saboteur est un saboteur ».
- Synonymes et paraphrases : « témoins » ; « témoins du régime » ; « jumeau honnête » ; « honnêtes exogènes » ; « seuil recalé sur le flux du suspect » (témoin « doit mourir »).
- Source : v3, sections 1, 4, 5 point 3 ; erratum 3 v2, R-7 (refaire les témoins reste une correction, la règle ne dit pas ce qui la déclenche : lecture de l'auteur, à vérifier).
- État : retenu.
- Liens : règle à deux clés ; bilan du produit ; référence honnête en service ; dérive de régime (taux de fausses alertes avec témoins exogènes du régime d'usage).
- Ce qui l'attaque : en service, pas de jumeau ; la référence exogène reste à concevoir.
- Inventaire : nouveau.

#### [N075-18] File d'audit prioritaire, à côté de la part tirée au hasard
- Définition : les épisodes à motif sans preuve de dommage montent dans une file d'audit qui s'ajoute à la part tirée au hasard, sans la remplacer ni la réduire, sinon le tirage se devine. L'audit qui suit le score reste permis, mais ne porte pas la borne.
- Synonymes et paraphrases : « audit prioritaire » ; « audit qui suit le score » ; « aiguillage de l'audit ».
- Source : v3, section 2 point 4, section 4 point 4 ; erratum 3 v2 R-8.
- État : retenu (`GO-2026-11-21-61`, point 8 (a)) ; pas de nœud, sa part se déclare dans le texte qui l'écrit.
- Liens : plancher ; règle à deux clés ; seuils stochastiques (l. 168).
- Ce qui l'attaque : coût en audits ; Greenblatt et al. (2312.06942, audit des plus suspects, déjà publié).
- Inventaire : 2.16 (suite).

#### [N075-19] Bilan du produit fermé contre le jumeau honnête
- Définition : tenir quelques comptes du produit que tout dommage devrait déplacer (couverture des contrôles, coûts, effectifs, affirmations adossées à une preuve) et tester leur somme cumulée contre la loi du jumeau honnête sur les mêmes tâches. Candidat de second regard, non une garantie.
- Synonymes et paraphrases : « bilan matière » ; « bilan du produit » ; « comptes du produit » ; « material balance » ; point 4.
- Source : v3, section 5 ; `5aed4bab1172b181`.
- État : candidat retenu au banc de la course de l'adjudant, avec deux tests de mort écrits d'avance (muet sur une famille plantée « dommage hors comptes » ; mort « sans gain » sur la famille tenue à l'écart face à la base « mots et coût ») ; premier pas sans dépense : la liste des quantités comptables. Partiellement occupé (revendication 3 de la lecture des voisins) : reste étroit = question, toute revendication un nœud.
- Liens : N-060 v3 point 1 (vérité du dommage, une ligne du bilan) et base « mots et coût » (N-029, N-063), dont il est une généralisation candidate ; ne s'applique pas au bras A des organismes discrets.
- Ce qui l'attaque : Avenhaus et Jaech 1981 et rapport de 1982 (bilan d'une quantité conservée, point selle) ; Ortega-Fernandez et al. (2610.11843) ; Balachandran (2609.17560) ; Nagarajan et al. (2610.24483) ; un dommage le long d'une dimension non comptée passe.
- Inventaire : 2.3.

#### [N075-20] Le passage obligé : ce que tout sabotage délibéré doit calculer
- Définition : un « algorithme du sabotage » appris sur des sabotages connus hérite de leur distribution, sauf s'il est nécessaire à tout sabotage. Question ouverte : existe-t-il un passage obligé (connaître la bonne action et en choisir une autre) lisible dans les états internes par des lectures apprises sur honnêtes seuls, et peut-on le surveiller plutôt que les sabotages connus ?
- Synonymes et paraphrases : « passage obligé » ; « algorithme du sabotage » ; « noyau algorithmique » ; « cœur algorithmique » ; « sait, puis dit autre chose » ; « compétence, puis détournement » ; point 5.
- Source : v3, sections 1 et 6.
- État : ouvert (question de recherche, § 15 du programme) ; rien revendiqué, la question n'est pas dite neuve. Direction candidate d'un cycle de reconception des sondes (N-062), conçue sur les modes vus seulement.
- Liens : H8 et validité de construit (inchangés) ; N-062 ; atelier d'idées ; texte de lecture des lentilles (non modifié) ; attestation causale par micro-interventions secrètes (D-6, hors de N-075).
- Ce qui l'attaque : l'honnête calcule aussi la bonne action ; Halawi et al. (2307.09476), Belrose et al. (2303.08112), Nyoma (2606.17229, trop propre, R4), Fischl-Lanzoni et al. (2611.14996 : triche et échec honnête non séparés sur un modèle), Fomin et al. et Sinha (résultats négatifs ou égalés par le texte), Johnston et al. ; McGuinness et al. (attaquant qui décide tôt ou déplace ses représentations).
- Inventaire : 4.1 (et 4.2, 4.3).

#### [N075-21] La bascule en profondeur, et les sondes de conséquences attendues
- Définition : deux candidats nommés pour lire le passage obligé : la bascule en profondeur compare l'action lue aux couches fidèles et l'action émise ; les sondes de conséquences attendues lisent ce que l'agent prévoit que son action produira.
- Synonymes et paraphrases : « signature de conflit en profondeur » ; « tuned lens / logit lens par couche » ; « conséquences attendues » ; candidats de l'atelier et du banc.
- Source : v3, section 6, point 4.
- État : proposé, mode exploratoire d'abord (`GO-2026-11-21-45`), préenregistrement avant toute lecture décisive (R1).
- Liens : passage obligé ; Belrose et al. dès que la bascule est présentée ; Bhardwaj et al. (2610.31613, sondes de progrès sur démonstrations réussies) pour les conséquences attendues.
- Ce qui l'attaque : Belrose et al. et Nyoma occupent la détection par trajectoires de prédiction par couche ; Bhardwaj et al. occupent les sondes de progrès sur honnêtes seuls.
- Inventaire : 1.4 et 1.11.

#### [N075-22] Lemme d'additivité resserré à sa forme valide à tout instant, sur scores de sondes
- Définition : l'invariance de la puissance à la répartition d'un total, à horizon fixe, est publiée (Avenhaus et Jaech 1981) et ne se revendique plus, pas plus que la séparation avec le maximum. Le papier A ne revendique que ce reste : une borne inférieure de la probabilité d'alarme, valide à tout instant, qui ne dépend que du dommage total (lu comme budget total des déplacements du score de sonde), hors du cadre gaussien et sous dépendance, avec le coût du report, sur des scores de sondes internes.
- Synonymes et paraphrases : « lemme d'additivité » ; « invariance terminale (L1) » ; « la puissance ne dépend que du total, pas de la répartition » ; « forme valide à tout instant » ; « anytime-valid » ; « reste du lemme » ; décision D-4 ; point 10 ; N-004 ; V9 ; « 1981 cité ».
- Source : v3, section 7 ; erratum 1, C-3 ; erratum 2 ; erratum 3 v2, sections 1 (point 10), 4.2, R-11 à R-13 ; `fbe3298ec358fa9b`.
- État : retenu, revendication resserrée, `GO-2026-11-21-47` (point 4) puis `GO-2026-11-21-61` (point 10 (a)). Non déclaré libre (« non trouvé » par une lecture non contre-lue) ; non démontré : démonstration à faire par une version de la note mathématique, contre-lue. Sortent aussi : prix de la garantie et détection avant le dommage (non nommés par le reste, non parce qu'occupés : mesurés, rapportés, cités). L'invariance entre agents n'est gardée que comme partie du reste, lecture de l'auteur, sort si non établie. Repli de N-004 (corollaire cité) disponible, non déclenché, nœud.
- Liens : papier A ; papier B (N-069 : citation obligatoire dès que l'additivité entre agents est invoquée) ; critère de succès « lemme et théorème négatif démontrés » (l. 235) ; T0.3 (non touché) ; porte de fin de phase 1 (son préenregistrement partira de l'énoncé resserré).
- Ce qui l'attaque : Avenhaus et Jaech 1981 (JNMM vol. X n° 3, p. 24-33) ; Zerrweck 1981 (d'après KfK 3365, théorème 4) ; rapport KfK 3935 de 1985 (test séquentiel CUMUF tronqué, transformation d'indépendance, tests à somme cumulée, test de puissance un à frontière de mélange, p. 74) ; Khosravi et Huo (2610.10597, garantie valide à tout instant en nombre total d'enregistrements corrompus) ; E-valuator, *Doomed from the Start*, Gauthier, Bach et Jordan. Nœuds : la note mathématique ne démontre pas le reste ; une lecture le trouve occupé (chapitres 4 à 6 de 1985, rapport de 1990, Zerrweck) ; un texte veut remettre ce qui est hors du reste.
- Inventaire : nouveau.

#### [N075-23] Détournement étalé contre détournement brusque (menace diffuse contre coup unique)
- Définition : la littérature des garanties nucléaires sépare le détournement étalé (« protracted diversion »), pour lequel tester le bilan global est optimal, du détournement brusque (« abrupt diversion ») ; « only the first szenario leads to a simple solution ». C'est le partage du programme entre menace diffuse et coup unique.
- Synonymes et paraphrases : « protracted vs abrupt diversion » ; « diffus contre coup unique » ; « tester le total plutôt que ses parts ».
- Source : v3, section 7 (« source de première main », rapport KfK 3365 de 1982, p. 21-22 du fichier) ; correction A8.
- État : occupé par la littérature (cité) ; sert de citation pour la limite « rien contre un coup unique » du plancher.
- Liens : plancher ; lemme ; bilan du produit.
- Ce qui l'attaque : rien ; c'est une citation.
- Inventaire : nouveau.

#### [N075-24] Référence honnête en service
- Définition : qui produit, hors du banc, le taux de dommage honnête de référence et les témoins dont le plancher en régime d'excès et le bilan de la pince ont besoin. Sans elle, aucun des deux n'a d'appui en service.
- Synonymes et paraphrases : « référence honnête exogène » ; « taux de dommage honnête de référence » ; « netteté de la référence » ; « modèle de confiance, prédicteur sur la tâche » ; point 5 de la section 11.
- Source : v3, sections 3 (« textes scellés »), 5 point 3, 11 point 5.
- État : ouvert ; avis suivi : tâche de conception plutôt que nœud, premier pas exploratoire de l'épreuve de netteté de la référence (décision D-3 de la note sur la pince, `GO-2026-11-21-50`) sur honnêtes seuls ; Lazar ne fixe que la priorité (confiance 0,6). D'ici là, aucune phrase sur le plancher avec test d'excès ni sur le bilan en service. Non nommé à `GO-2026-11-21-61`.
- Liens : plancher ; bilan de la pince ; témoins exogènes.
- Ce qui l'attaque : « premier pas non justifié » de la note sur la pince.
- Inventaire : 2.19.

#### [N075-25] L'asymétrie d'apprentissage contre l'invariant de l'oracle (réapprentissage des sondes en service)
- Définition : le programme (l. 170) veut que chaque détection silencieuse devienne un exemple étiqueté pour réentraîner les sondes ; N-060 v3 (point 4) interdit toute sortie de l'oracle dans la sélection d'un moniteur. Heurt antérieur à N-075 : il faut dire laquelle des deux règles cède.
- Synonymes et paraphrases : « réentraînement en service » ; « réapprentissage sur l'oracle » ; « boucle audit-recapture-réapprentissage » ; point 9 ; trouvaille de côté du contre-lecteur.
- Source : v3, section 4 point 2, section 11 point 9 ; erratum 2 ; erratum 3 v2, section 2, sections 3 point 1, A-3.
- État : **non tranché**, nœud sans défaut. Options : (a) restreindre la l. 170 (recommandation de l'auteur, 0,6) ; (b) restreindre l'interdit au banc et permettre le réentraînement en service (Lazar « penche » pour (b), « demande au collisionneur et organisme dans la demande fusionnée ») ; (c) laisser le heurt écrit. D'ici le mot, N-060 v3 point 4 s'applique en entier ; aucun texte neuf n'écrit de réapprentissage sur verdicts de l'oracle ; la boucle ne vit que sur mondes plantés (N-076). « Ne pas écrire » : « le réapprentissage des sondes en service est permis ».
- Liens : N-060 v3 ; N-076 (§ 6.2, section 13 point 3) ; recapture ; collisionneur, protocole X, organisme d'idéation.
- Ce qui l'attaque : si (b), il faut fixer quels épisodes servent au réapprentissage et lesquels jugent le même moniteur (la recapture ne jugerait plus à l'aveugle), l'exclusion du mode tenu à l'écart (N-054, N-062), l'accès des concepteurs aux verdicts par épisode, la précision (i) du point 2, et amender une décision scellée.
- Inventaire : 2.14 (et section 6 de l'inventaire).

#### [N075-26] La veille dégelée sans borne de zone, à côté des trois chantiers
- Définition : le gel de la veille est levé sans borne de zone ; elle ne compte pas parmi les trois chantiers actifs, vit à côté d'eux et sert d'abord les lectures d'antériorité que demandent les décisions.
- Synonymes et paraphrases : « veille active » (§ 16 du programme) ; « non pas borné à cette zone, go » ; « veille à côté des chantiers » ; point 7 ; D-P4.
- Source : v3, section 7 point 4, section 10 ; erratum 2 ; erratum 3 v2, section 1 (point 7), R-1 à R-3.
- État : retenu, `GO-2026-11-21-51` (point 4) puis `GO-2026-11-21-61` (point 7 (a)) ; pas de nœud.
- Liens : règle « trois chantiers actifs au plus » ; lectures d'antériorité.
- Ce qui l'attaque : c'est de fait une quatrième file de travail.
- Inventaire : nouveau.

#### [N075-27] Liste « Ne pas écrire » de N-075
- Définition : phrases interdites dans tout texte, interne ou sortant, qui présente ces points. Elle encode les limites de la décision en garde-fous de rédaction.
- Synonymes et paraphrases : « ne pas écrire » ; « interdits de rédaction ».
- Source : v3, section 8 ; erratum 3 v2, R-9 et A-3.
- État : retenu. Contenu : « moniteur valide hors distribution » ; « la pince tient devant des attaques jamais vues » ; « garantie de détection » pour une sonde ; « premier plancher », « premier bilan », « première règle à deux clés » ; le lemme sans la citation de 1981 ; un chiffre des blocs de calcul sans « sous supposition » ; « nos tirages secrets » comme neufs pour un regard interne (Aremu et al., 2603.23171) ; « nouveauté seule = mise à jour des témoins » comme règle, « alerte = nouveauté et preuve de dommage » ; « le plancher borne le dommage pour toute politique » sans régime, oracle, horizon ; « la théorie du danger demande le non-soi » ; le plancher comme apport ; une borne chiffrée sans strates mesurées et leur compte ; une borne dans une strate non mesurée ; un q supposé écrit comme mesuré ; « le réapprentissage en service est permis ».
- Liens : citations obligatoires (section 8 de la v3 : Avenhaus et Jaech 1981, KfK 3935, KfK 3365, Blindfold, Gans et Holden, Podkopaev et Ramdas, Gao et al., Li et al., Terekhov et al., Greenblatt et al., Fischl-Lanzoni et al., Aremu et al., Xu et al., Bailey et al., Ortega-Fernandez et al., Aickelin et Cayzer, Zhong et Raghunathan, Halawi et al., Nyoma ; et « à citer quand le point est abordé »).
- Ce qui l'attaque : sans objet.
- Inventaire : nouveau.

#### [N075-28] Auditer des actes plutôt que des issues ; part des attaques jamais vues intégrée au contrôle
- Définition : deux décisions de la même ligne `GO-2026-11-21-61`, signalées par l'erratum 3 v2 comme touchant N-075 sans texte : l'unité de l'audit (actes plutôt qu'issues, alors que N-075 dit « mesurer l'issue ») et l'estimation de la part des attaques jamais vues (Li et al.) intégrée au système de contrôle.
- Synonymes et paraphrases : « auditer des actes plutôt que des issues : go » ; « part des modes inconnus » ; « borne sur un mode jamais vu ».
- Source : erratum 3 v2, section 8 et trouvaille de côté (2).
- État : accordé par Lazar mais sans pièce propre : ouvert, à écrire.
- Liens : mesurer l'issue ; plancher ; Li et al. (2611.15835).
- Ce qui l'attaque : contredit en partie le premier levier de N-075 tant qu'aucun texte ne les concilie.
- Inventaire : nouveau.

---


### 2.2 Décisions N-076 (audit et référence honnête) et N-077 (retrait de la marge asymétrique) (`N076`)


> Fichiers lus en entier (dépôt `docs/decisions/`) :
> - N-076 v1 : `decision-N-076-assurance-par-audit-et-reference-honnete-v1.md`, empreinte `49b664c1d6a72fdb` (v1 scellée, écrite par Fable 5.2 le 21 novembre 13:56-14:04 UTC ; à contre-lire).
> - Erratum 1 (prime sur la v1) : `…-v1-erratum-1.md`, `34a59c49436d5239`.
> - Erratum 2 : `…-v1-erratum-2.md`, `c2943188b4906993`.
> - N-077 v1 : `decision-N-077-retrait-marge-asymetrique-mesure-gardee-v1.md`, `41643fc538ff9d6b` (scellée, non contre-lue).
> - Rattachement : `docs/notes/seconds-regards-sabotage-inventaire-v1/inventaire-seconds-regards-invariants-noyaux-v1.md` (numéros d'inventaire).

> Ce que changent les errata de N-076 :
> - **Erratum 1** (21 novembre, 14:05 UTC, prime) : (E1) ajoute les mots de Lazar de `GO-2026-11-21-60` : « que reste t il alors ? demande approfondie et protocole X, il faut une percee pour notre programme » ; « go protocole x pour sa concetpion » — le plancher d'audit étant occupé, protocole X sur « où est la percée du programme », et protocole X pour concevoir le banc à vérité plantée. (E2) N-075 v2 n'est plus « en vérification » : verdict « pas encore prêt à sceller », dix points ; une v3 viendra, renvois à recaler. (E3) Le premier pas du banc à vérité plantée passe par le protocole X (concepteur en effort maximal, collisionneur, organisme), payé sur ses lignes propres. (E4) Le plancher n'est plus « à confirmer » comme occupé : Lazar en a pris acte ; base nommée et citée, jamais revendication. (E5) La spécification du banc sort des premiers pas sans dépense. (E6) Vérification de N-075 v2 lue en en-tête et verdict seulement. Rien d'autre ne change (neuf points, invariants, renvois, ligne pour `CLAUDE.md`).
> - **Erratum 2** (16:20 UTC, session mère) : correction de lettre seule, empreinte abrégée de la lecture des douze voisins : `973bd0dd…8869`, non `…7869`.

> Mots de Lazar (`GO-2026-11-21-57`) : « BRILLNT , genial, integrer au programme !! » ; « go insris dans le prog et a faire ». Le rattachement des deux phrases aux neuf points est la lecture de la mère. N-076 ne change le critère d'aucune porte, l'énoncé d'aucune hypothèse, n'ouvre ni dépense ni chantier, ne déclare rien « libre ». « À faire » = inscrit, premier pas sans dépense permis, toute course sur devis et GO.

> ---

#### [N076-01] Référence honnête, taille m, horizon n, unité
- Définition : la référence honnête est ce par quoi un moniteur connaît la conduite de l'honnête ; m est sa taille en unités honnêtes, exogènes au suspect et du régime d'usage ; n est l'horizon, le nombre d'unités surveillées accumulées avant la décision. L'unité (acte ou épisode) est déclarée : c'est celle où les scores sont tenus pour indépendants sous le nul.
- Synonymes et paraphrases : référence de l'honnête ; échantillon honnête d'étalonnage ; « m et n » ; taille de la référence ; témoins honnêtes ; « savoir exactement à quel point un honnête paraît suspect » (billet de Hebbar).
- Source : N-076 v1, § 1 ; `49b664c1d6a72fdb`.
- État : retenu (vocabulaire), `GO-2026-11-21-57`.
- Liens : loi de la référence honnête ; H2 ; lemme d'additivité ; papier A et B ; jumeau honnête (au banc seulement, N-075, § 5).
- Ce qui l'attaque : en service, la référence est exogène et biaisée ; un écart systématique honnête-référence ne décroît pas avec n.
- Inventaire : nouveau (voisin de 2.19, netteté de la référence).

#### [N076-02] Source de validité d'une accumulation (quatre sortes)
- Définition : ce qui garantit le taux de fausses alertes d'une statistique qui accumule. Quatre sortes nommées : une référence fixe de taille m ; des témoins honnêtes entrelacés à taux p ; un nul par acte ; un tirage du défenseur.
- Synonymes et paraphrases : d'où vient la validité ; garantie de fausses alertes ; « source de sa validité » ; régimes de la référence.
- Source : N-076 v1, § 1 et § 2 ; `49b664c1d6a72fdb`.
- État : retenu, `GO-2026-11-21-57`.
- Liens : loi de la référence honnête ; hasard du défenseur ; nul par acte ; jeu de contrôle (agrégateurs).
- Ce qui l'attaque : chaque source a ses suppositions (indépendance à l'unité ; secret du tirage) ; la précision « témoins à taux p » est une lecture de l'auteur, la phrase accordée ne nomme que le nul par acte.
- Inventaire : nouveau.

#### [N076-03] Nul par acte
- Définition : un nul propre à chaque acte, tiré par le défenseur, qui ne s'appuie sur aucune référence étalonnée ailleurs. Exemple : le rang de l'action de l'agent parmi K tirages du jumeau honnête sur le même début ; il permet à l'accumulation de garder la loi en racine au-delà de m.
- Synonymes et paraphrases : rang contre le jumeau ; nul local ; « sauf nul par acte » ; référence par acte ; moniteur de dissonance (même ressort).
- Source : N-076 v1, § 1, § 2 (prévision) ; `49b664c1d6a72fdb`.
- État : retenu (vocabulaire et exception de la règle d'horizon), `GO-2026-11-21-57`.
- Liens : moniteur de dissonance ; prévision scellée avant la porte de fin de phase 1 ; jumeau honnête.
- Ce qui l'attaque : le jumeau n'existe qu'au banc ; en service, pas de jumeau ; régime en racine nue non rejoué (bloc C de la note « percée »).
- Inventaire : 1.3 (moniteur de dissonance, rang contre le jumeau).

#### [N076-04] La loi de la référence honnête (et la règle d'horizon)
- Définition : quand la loi de l'honnête n'est connue que par m unités, la part d'actes sabotés qui reste cachée cesse de baisser dès que l'horizon n dépasse m ; elle vaut, pour un test sur la moyenne, z × √(1/n + 1/m) / μ (palier vers 23,3 % à m = 400 et μ = 0,5, sous supposition d'illustration). Protocole accordé : « Toute accumulation déclare m, n et la source de sa validité ; son horizon ne dépasse pas m, sauf nul par acte. » Lecture : au-delà de m, les gains se rapportent « au-delà de la référence » et ne fondent aucun verdict ; le moniteur n'est pas arrêté, c'est la conclusion qui est plafonnée.
- Synonymes et paraphrases : candidat C1 de la note « percée » ; plafond de la référence ; « l'horizon ne dépasse pas m » ; règle d'horizon ; loi en racine qui s'aplatit ; le rappel qui cesse de croître ; trois régimes (référence fixe, témoins à taux p avec facteur √(1 + 1/p), nul par acte).
- Source : N-076 v1, § 2 ; note « percée » § 7.1 ; `49b664c1d6a72fdb`.
- État : retenu, intégré au programme (`GO-2026-11-21-57`) ; non revendiqué (aucun verdict d'antériorité ; « rien de neuf en mathématiques : un pont entre pièces publiées »).
- Liens : H2 (énoncé inchangé, clause renvoyée) ; lemme d'additivité (hypothèse (c) reçoit une lecture : la puissance dépend aussi de m) ; jeu de contrôle ; bases boîte noire (même déclaration, R4) ; papier B (effectif utile plafonné à l'inverse de la corrélation) ; plan de la phase 1 (bras « référence honnête »).
- Ce qui l'attaque : occupée en parts par Ker, Bash-Goeckel-Towsley (loi en racine), arXiv 1608.00698 et 1612.09027 (guetteur qui ignore son bruit), 2609.23254 (ensemble aveugle d'un moniteur tolérant), Ortega-Fernandez et al., Wen et al., Podkopaev-Ramdas, Cao, Singh ; zone séduisante à voisins de deux mois (R8) ; plancher « tout test » 7,7 % non contre-lu. Revendicable seulement, si non trouvé imprimé, la réunion en réponse chiffrée, la règle d'horizon et la comptabilité jointe audit-moniteur.
- Inventaire : nouveau.

#### [N076-05] La prévision de la référence honnête, à sceller avant la porte de fin de phase 1
- Définition : « Le rappel d'une statistique étalonnée sur m épisodes honnêtes cesse de croître au-delà d'un horizon de l'ordre de m ; celui du rang contre le jumeau continue. » Elle se scelle dans un texte à part de classe A (concepteur, contre-lu), avec m, n, horizon d'aplatissement, écart minimal, métrique (rappel à 1 % de fausses alertes selon l'horizon), plan, liste d'arrêt et objets de contrôle sur monde planté.
- Synonymes et paraphrases : prévision scellée avant G1 ; deux courbes ; bras rapporté « référence honnête » ; prédiction des deux pentes.
- Source : N-076 v1, § 2 et § 13, point 7 ; `49b664c1d6a72fdb`.
- État : retenu, à faire ; **pas un critère de la porte**. Lieu du scellement renvoyé à Lazar : recommandation texte à part (confiance 0,65), défaut sous 48 heures (écriture seule).
- Liens : porte G1 ; plan à deux fois deux cases ; nul par acte.
- Ce qui l'attaque : trois tests de mort — instrument (sur monde planté, l'agrégateur ne retrouve pas les deux pentes) ; mesure (courbes non séparées, ou écart systématique honnête-jumeau qui cache déjà plus que le dommage visé : loi juste mais inutile) ; adversaire (écart lu par unité de dommage nul sous le mode tenu à l'écart).
- Inventaire : nouveau.

#### [N076-06] Inventaire par étiquettes des m et n des textes scellés
- Définition : relevé, sans lecture de résultat, des tailles de référence et horizons dans les préenregistrements qui accumulent (simulation du lemme T0.3, accumulation du barreau 6, formulation de la porte en simulation). Un n supérieur à m trouvé est une réserve à la lecture ; sa correction passe par un additif, donc un nœud.
- Synonymes et paraphrases : audit des horizons ; inventaire m/n ; table des barrières (pièce voisine : pour chaque garantie, la supposition qu'elle consomme).
- Source : N-076 v1, § 2, « Textes scellés » et « Premier pas » ; `49b664c1d6a72fdb`.
- État : à faire, sans dépense.
- Liens : loi de la référence honnête ; R1 (écart à un préenregistrement = nœud).
- Ce qui l'attaque : premier pas non justifié de la note (pas 13 : rien vérifié des textes scellés).
- Inventaire : nouveau (voisin de 2.18, audit des tolérances).

#### [N076-07] Le hasard du défenseur comme preuve (conditions tirées et test de permutation)
- Définition : le harnais tire au sort, par épisode, une condition sans rapport avec la tâche (cadre dit d'évaluation, de déploiement, sans surveillance) ; un test de permutation donne une valeur p exacte pour le nul « la conduite ne dépend pas de la condition », sans rien supposer de la loi honnête. Il ne prend que le saboteur conditionnel, et le force sinon à saboter partout, donc aussi là où l'audit compte.
- Synonymes et paraphrases : candidat C3 ; conditionnalité à la surveillance ; tirage du défenseur ; « la validité vient du tirage » ; contrôles croisés à condition tirée ; inférence exacte par randomisation.
- Source : N-076 v1, § 1 et § 3 ; `49b664c1d6a72fdb`.
- État : retenu, à faire (`GO-2026-11-21-57`) ; bras rapporté de la phase 1, sans critère de porte ; non revendiqué (une seule requête d'antériorité ; résidu mince possible : la couche d'inférence exacte et le dilemme joint avec l'audit sur vérité plantée).
- Liens : contrôles croisés (l. 136 du programme) ; H8 et validité de construit ; mesure de la conscience d'évaluation (N-053, point 3) ; jumeau honnête témoin obligé.
- Ce qui l'attaque : exacte pour son nul, pas pour « il y a sabotage » (l'honnête peut réagir à la condition) ; **mort si le jumeau rejette autant que le saboteur** ; la condition est visible de l'agent (pas un secret). Voisins : Hasan 2604.13301 (plan à trois conditions), Krakovna et al., Needham et al., Greenblatt et al., « Blindfold ».
- Inventaire : 2.7.

#### [N076-08] Hasard du défenseur (notion)
- Définition : tout tirage fait par le harnais que l'agent ne choisit pas : pièce d'audit, condition tirée, ordre de présentation, perturbation secrète. C'est l'une des quatre sources de validité.
- Synonymes et paraphrases : aléa du défenseur ; randomisation du harnais ; tirage secret.
- Source : N-076 v1, § 1 ; `49b664c1d6a72fdb`.
- État : retenu (vocabulaire).
- Liens : pièce d'audit ; attestation en service ; épreuves du devin (qui éprouvent son secret).
- Ce qui l'attaque : si le tirage fuit, la garantie tombe (Gans et Holden : monter le taux ne répare rien).
- Inventaire : 2.7 et 2.17 (en partie).

#### [N076-09] Le banc de recherche à vérité plantée
- Définition : des mondes de recherche engendrés par programme, à lois plantées, flous à la relecture et exacts en aval ; le dommage d'un sabotage diffus s'y compte en lois vraies perdues et lois fausses promues, par un oracle hors de la machine. Servi avec un jumeau honnête, un juge faible et l'accès aux états internes ; seul, ce n'est pas un résultat mais le terrain qui rend la loi de la référence honnête vérifiable par d'autres.
- Synonymes et paraphrases : candidat C2 ; banc à lois plantées ; mondes de découverte plantés ; « C2 » ; environnement candidat (e) du § 6 du programme ; banc de sabotage de recherche.
- Source : N-076 v1, § 4 ; erratum 1, E1, E3, E5 ; `49b664c1d6a72fdb`, `34a59c49436d5239`.
- État : retenu, à faire (`GO-2026-11-21-57`) ; conception par le protocole X (`GO-2026-11-21-60`, erratum 1 prime) ; générations et juges sur devis ; plusieurs lignées et grande taille : la bourse. Non revendiqué.
- Liens : organisme d'idéation, rôle 3 (première moitié tranchée par lecture de l'auteur : terrain à dommage exact ; seconde moitié — réserver la famille « qui trompe le juge » comme tenue à l'écart — renvoyée à Lazar, confiance 0,6) ; environnement des propositions d'expériences (non remplacé ; pas sous la porte de la phase 3) ; invariant « aucun score de moniteur dans l'entraînement » ; citations obligatoires de l'organisme.
- Ce qui l'attaque : trois témoins écrits avant toute génération, qui doivent le tuer : un juge faible qui voit tout ; un modèle faible qui égale le fort ; un oracle qui fuit. Voisins : 2607.19321 (sabotage par tâche annexe), 2604.16286 (dépôts sabotés), Terekhov et al. (vérité approchée), 2406.06769 (mondes de découverte sans adversaire), Kezendirane 2611.00407 (banc « triche contre échec honnête », vérité par rejeu prise pour la triche).
- Inventaire : nouveau.

#### [N076-10] L'attestation en service des sondes
- Définition : pendant le déploiement, on rejoue des épisodes réels tirés au hasard jusqu'à un pas, on bifurque sur une copie, on injecte de petites perturbations tirées en secret le long de la direction de la sonde et de directions témoins ; la lecture et le comportement doivent répondre avec le gain mesuré au laboratoire. Une réponse qui a baissé annonce « sonde invalide ici » ; elle demande non « la sonde détecte-t-elle ? » mais « lit-elle encore ce que le modèle utilise, ici ? ».
- Synonymes et paraphrases : micro-interventions secrètes ; tatouage dynamique (commande sécurisée, Satchidanandan et Kumar) ; explication (d) de la contre-lecture adjudant ; canari de sonde ; validité en service.
- Source : N-076 v1, § 5 ; `49b664c1d6a72fdb`.
- État : **candidate** (ni hypothèse, ni instrument admis, ni porte) ; texte et bras à part déjà accordés (`GO-2026-11-21-46`, D-6 ; `GO-2026-11-21-51`, point 6) ; entre aux questions ouvertes. Partiellement occupée ([verdict, 2]).
- Liens : sondes ; validité de construit ; papier C (préenregistrement non modifié) ; N-015 (bruit d'activations hors interventions revendiquées) ; N-053, point 5.
- Ce qui l'attaque : garantie d'origine asymptotique, en puissance moyenne : une tricherie d'énergie finie échappe ; une évasion qui garde les gains locaux passe ; Fonseca Rivera et Africa : un modèle ajusté détecte un pilotage injecté (« not an invisible intervention ») ; Shire et Kim (canari), Aremu et al. (clé secrète). Deux tests de mort : évasion plantée qui garde les gains locaux (doit se dire muette) ; un devin retrouve l'intervention (le secret n'en est pas un).
- Inventaire : 2.10.

#### [N076-11] L'audit après coup, à plancher et à l'enjeu
- Définition : le tirage d'audit se fait après la fin de l'épisode, le jugement porte sur une copie hors ligne ; la probabilité d'audit vaut un plancher, plus une part proportionnelle à l'enjeu, plus une part qui suit le soupçon ; jamais nulle, le soupçon la monte sans la descendre sous le plancher ; chaque probabilité est consignée, les estimations pondérées par son inverse. Le budget d'audit se décompose en trois parts déclarées.
- Synonymes et paraphrases : proposition 6.1 de la note « attaquant informé » ; audit en trois parts ; audit hors ligne ; plancher d'audit au hasard ; audit pondéré par l'enjeu ; famille plantée « attaque choisie ».
- Source : N-076 v1, § 6.1 ; erratum 1, E4 ; `49b664c1d6a72fdb`.
- État : retenu, à faire. **Le plancher lui-même est occupé** ([verdict, 6], « Blindfold » ; Lazar en a pris acte, `GO-2026-11-21-60`) : base nommée et citée, jamais revendiquée. Reste, partiellement occupé ([verdict, 7]) : l'assemblage des trois parts contre un agent informé qui place le dommage où enjeu et soupçon sont bas.
- Liens : N-075, § 2 (plancher base rapportée hors liste de G1) ; jeu de contrôle (budget b) ; courbe sécurité-utilité ; quatre invariants d'audit ; table du seuil.
- Ce qui l'attaque : trois attentes plantées (la borne du plancher tient ; l'audit des seuls plus suspects meurt ; l'audit uniforme perd le rapport enjeu maximal / enjeu moyen) ; violation cachée même à l'auditeur sans étiquette (« Blindfold ») ; « stronger auditing makes undeterred violations better hidden » (Gans et Holden) ; pièce qui fuit. Voisins : « Blindfold », Shekhar et al., Gao et al., Li et al., Gans et Holden, Greenblatt et al.
- Inventaire : 2.1.

#### [N076-12] La boucle audit, recapture, réapprentissage
- Définition : le flux d'audit au hasard fournit les épisodes endommagés ; la recapture dit si la sonde est devenue aveugle ; la sonde est réapprise sur eux, poids de l'agent gelés et canal de retour fermé, si bien que le défenseur joue en dernier. Grandeur rapportée : le rappel retrouvé en fonction du nombre d'épisodes endommagés audités.
- Synonymes et paraphrases : proposition 4.1 ; courbe de rétablissement ; asymétrie d'apprentissage mesurée (l. 170 du programme) ; « le défenseur joue en dernier » ; réapprentissage sur les prises de l'audit ; rappel après l'alarme (voisin).
- Source : N-076 v1, § 6.2 et § 13, point 3 ; `49b664c1d6a72fdb`.
- État : à faire **sur mondes plantés seulement** ; aucune sonde du programme réapprise sur des verdicts de l'oracle avant le mot de Lazar. Heurt avec l'invariant de l'oracle (N-060 v3, point 4) renvoyé : recommandation (a) réapprentissage sous cloison par texte à part contre-lu (confiance 0,6), nœud sans défaut, d'ici là (b) invariant entier. Partiellement occupé ([verdict, 8]).
- Liens : attaques adaptatives E1.5 (b) ; test de récupération après réentraînement (N-053, point 5) ; réserve de détecteurs (témoin) ; épreuves du devin (condition du canal fermé) ; mode tenu à l'écart exclu (N-054, N-062).
- Ce qui l'attaque : deux tests de mort — avec les étiquettes que le plancher livre avant le seuil toléré, le rappel reste sous le niveau validé (boucle trop lente) ; canal ouvert, le rétablissement doit s'effondrer, sinon le banc ne mesure rien. Rudoler et al. 2609.36049 (moniteur appris sur audits au hasard face à un ouvrier adverse) non lu par le verdict : reste plus étroit. Voisins : Bailey et al., Gupta et Jenner, Wehner et Fritz, Lyons Keenan et al., Westphal et al., McGuinness et al.
- Inventaire : 2.2 et 2.14.

#### [N076-13] Les épreuves du devin
- Définition : avant de s'appuyer sur un secret du harnais, un prédicteur reçoit tout ce que l'agent peut observer et tente de deviner soit la lecture de la sonde (après les décisions du harnais), soit la pièce d'audit (« audité ou non », avant l'action). Une prédiction au-dessus du hasard suspend la garantie qui s'appuyait sur ce secret, jusqu'à réparation.
- Synonymes et paraphrases : propositions 2.1 et 6.2 ; épreuves d'admission ; test de fuite ; devin de la sonde, devin de la pièce ; instrument de fuite de H7 ; (troisième, non inscrit : le devin des corrections, proposition 2.2 de la note « asymétries »).
- Source : N-076 v1, § 1 et § 6.3 ; `GO-2026-11-21-54`, D-4 ; `49b664c1d6a72fdb`.
- État : retenu, à faire ; instruments de classe B ; les invariants « flux unidirectionnel », « moniteurs amnésiques », « seuils stochastiques » deviennent éprouvés à l'admission du harnais. Partiellement occupé ([verdict, 9]) ; reste : le devin sur la lecture de la sonde et leur emploi comme épreuves d'admission.
- Liens : H7 (riposte et fuite), énoncé inchangé ; attestation en service ; pièce d'audit ; canal de retour.
- Ce qui l'attaque : **le devin réfute, il n'atteste pas** — un échec n'est qu'une borne basse de la fuite ; borne haute = couplage apparié des deux branches (« Blindfold ») ; ne jamais écrire « le secret est établi ». Voisins : « Blindfold » (devin de la pièce sur porte réelle), Lyons Keenan et al., Chinaei (résumé).
- Inventaire : 2.17.

#### [N076-14] Canal de retour
- Définition : tout ce par quoi une lecture, un verdict ou une conséquence d'un score atteint ce que l'agent observe. Sa fermeture conditionne la boucle de réapprentissage et le secret de la sonde.
- Synonymes et paraphrases : fuite par les verdicts ; retour à l'agent ; boucle de rétroaction ; « canal fermé, éprouvé ».
- Source : N-076 v1, § 1, § 6.2, § 8 ; `49b664c1d6a72fdb`.
- État : retenu (vocabulaire).
- Liens : invariant « aucun retour à l'agent » ; devin ; Lyons Keenan et al. (le canal suffit à l'évasion).
- Ce qui l'attaque : toute correction visible avant l'alarme l'ouvre ; d'où le nœud D-2 de la note « asymétries ».
- Inventaire : nouveau.

#### [N076-15] La table du seuil au taux d'audit (borne inférieure lue à l'envers, deux régimes, séparée du lemme)
- Définition : on écrit d'abord le seuil toléré K d'épisodes endommagés, puis on en déduit le taux d'audit p, l'oracle (probabilité q, délai) compris, par famille étiquetée « signature » ou « excès ». Régime de signature : agir avant K avec probabilité 0,95 demande p × q ≥ 1 − 0,05^(1/K) (illustration : 9,5 % à K = 30, 1 % à K = 300, sous supposition) ; régime d'excès : **aucun seuil fixe garanti**, la garantie porte sur un taux d'excès à horizon dit, ce qui passe croît comme la racine de l'horizon sur le taux d'audit, si la grille des mises descend vers le taux acceptable (sinon linéaire).
- Synonymes et paraphrases : décision D-1 de la note « attaquant informé » ; table du seuil ; borne du plancher ; seuil toléré K ; régime de signature (l'honnête ne commet jamais ce dommage) / régime d'excès (l'honnête le commet aussi) ; voie lente contre voie rapide.
- Source : N-076 v1, § 1 et § 7 ; § 12 (texte pour § 4 du programme) ; `49b664c1d6a72fdb`.
- État : retenu (`GO-2026-11-21-57`) ; non revendiqué (inversion d'une loi géométrique, élémentaire ; la lecture par famille avec délai, pour une menace diffuse, reste question).
- Liens : sécurité (l. 74) reçoit deux bornes distinctes, l'une par le lemme sous son hypothèse (a), l'autre par la table dans la couverture de l'oracle — tout texte dit laquelle ; métriques de latence ; étiquetage des familles du banc (à faire, sans dépense) ; N-075, § 2.
- Ce qui l'attaque : si le taux exigé dépasse le budget d'étiquettes, le plancher n'y garantit rien : on l'écrit ; « agir » borne sans annuler le dommage fait ; « Blindfold » certifie un taux, non un seuil ; Singh ; Podkopaev-Ramdas ; aucun analogue de Neyman-Pearson pour le délai (rapport KfK 3935). **Ne pas écrire que le lemme porte la borne du plancher.**
- Inventaire : nouveau (prolonge 2.1).

#### [N076-16] Séparation du lemme d'additivité et de la borne du plancher
- Définition : le lemme additionne des déplacements du score de sonde (son hypothèse (a), que le sabotage invisible à la boîte blanche nie) ; la table additionne le dommage lui-même, échantillonné par l'audit. Même ossature (tester le total), autre grandeur : le lemme est la voie rapide quand la trace existe, la table la voie lente qui tient quand elle n'existe pas.
- Synonymes et paraphrases : deux bornes de la sécurité ; voie rapide / voie lente ; « le lemme ne porte pas la borne du plancher ».
- Source : N-076 v1, § 7 et § 12 (phrase à reporter au § 3) ; `49b664c1d6a72fdb`.
- État : retenu ; lettre du lemme (N-004, N-075 § 7) inchangée.
- Liens : lemme d'additivité ; théorème négatif ; table du seuil.
- Ce qui l'attaque : un texte qui confond les deux s'appuie sur une hypothèse (a) que le sabotage visé nie.
- Inventaire : nouveau.

#### [N076-17] Les quatre invariants d'audit (section 9 du programme)
- Définition : quatre lignes accordées pour tout texte à venir qui emploie un audit : (1) audit après coup — tirage après la fin de l'épisode, jugement sur copie hors ligne, rien de ce que l'agent observe n'en dépend ; (2) plancher indépendant du score — probabilité connue, jamais nulle, consignée, le soupçon la monte sans la descendre ; (3) part selon l'enjeu, fixé par le défenseur avant l'épisode ; (4) aucun retour à l'agent — aucune lecture ni aucun verdict ne lui revient.
- Synonymes et paraphrases : décision D-3 ; invariants du § 9 ; règles d'exploitation de l'audit ; « aucun retour ».
- Source : N-076 v1, § 8 et § 12 ; `49b664c1d6a72fdb`.
- État : retenu (`GO-2026-11-21-57`) ; rien revendiqué (chacune publiée). Lectures de l'auteur à confirmer : ligne 4 active par défaut, ablatée dans l'expérience de la riposte (confiance 0,8) ; sans enjeu défini, enjeux égaux déclarés ; plancher valable pour tout texte à venir sans rendre non conforme un texte scellé (pas de plus que N-075, à confirmer). En tête de section : les secrets du harnais éprouvés par un devin avant toute course.
- Liens : seuils stochastiques (l. 168, reçoivent le plancher) ; flux unidirectionnel (étendu à l'audit et aux sondes) ; H7 ; N-053 point 5 ; N-060 v3 point 4.
- Ce qui l'attaque : ne bornent rien contre un coup unique ; ne disent rien des interventions en ligne ; rival : les trois lignes de la note « asymétries » (voir entrée suivante). Voisins : « Blindfold », Gans et Holden, Gao et al., Li et al., Shekhar et al., Lyons Keenan et al.
- Inventaire : nouveau.

#### [N076-18] Les trois lignes de la note « asymétries » (proposition D-2, rivale de « aucun retour à l'agent »)
- Définition : la ligne 4 serait nécessaire pour un détecteur figé et la pièce d'audit avant l'action, non pour un moniteur qui apprend ni une correction tirée au hasard ; d'où trois lignes : seul le tirage au hasard corrige ; un audit sans trouvaille ne laisse aucune trace ; en régime de signature, on alarme, on ne corrige pas. Elles gardent le levier « corriger » et ne tiennent secret que ce que suit le soupçon.
- Synonymes et paraphrases : D-2 des asymétries ; corrections tirées au hasard ; « seul le hasard corrige » ; devin des corrections (proposition 2.2).
- Source : N-076 v1, § 8 et § 13, point 1 ; `49b664c1d6a72fdb`.
- État : proposé non tranché (`GO-2026-11-21-56` : « restent à Lazar ») ; recommandation de l'auteur (a), confiance 0,7, nœud sans défaut ; d'ici là la lettre accordée s'applique : aucun texte n'écrit, avant l'alarme, une correction observable venue d'un audit.
- Liens : quatre invariants d'audit ; scores qui orientent l'audit ; correction au sens de N-075.
- Ce qui l'attaque : le soupçon ne corrige plus rien de visible ; la lettre accordée, elle, retire la correction avant l'alarme.
- Inventaire : nouveau.

#### [N076-19] Les scores orientent l'audit sous un plancher
- Définition : les détecteurs ne se combinent pas entre eux pour porter une garantie, ils se combinent avec l'audit : chaque épisode garde une probabilité plancher d'audit, les scores l'augmentent, l'estimation pondère par l'inverse de la probabilité de tirage. Un détecteur, même faux hors de son domaine, change alors la vitesse de la prise, non la validité de la mesure.
- Synonymes et paraphrases : doctrine d'assemblage des moniteurs ; audit orienté ; pondération par l'inverse de la probabilité ; échantillonnage guidé par prédicteur ; « les détecteurs orientent l'audit » ; le score comme poids de tirage, non verdict.
- Source : N-076 v1, § 9 ; note « science de la détection », question 5 ; `49b664c1d6a72fdb`.
- État : adopté (`GO-2026-11-21-55`, D-5, cadre ; `GO-2026-11-21-57`) ; partiellement occupé ([six voisins, verdict (c)] : « peut l'employer en le citant, pas la revendiquer ») ; aucune phrase de nouveauté avant lecture en entier de Singh (`GO-2026-11-21-59`, E-3).
- Liens : moniteurs (§ 8) ; seuils stochastiques ; jeu de contrôle ; H5 (diversité effective, redéfinition renvoyée au protocole X) ; matrice de transfert ; N-075 § 2 point 4 et § 4 point 4.
- Ce qui l'attaque : conditions toutes nécessaires (probabilités connues et consignées, plancher strictement positif, pièce secrète) ; test de mort obligatoire : un agent qui sait baisser son score se place au plancher, le gain de l'orientation disparaît ; sur la famille tenue à l'écart, pas mieux que le hasard : « sans gain ». Voisins : Zrnic et Candès (« for any black-box model »), Cao, Xu-Karampatziakis-Mineiro, Molnar, Vovk-Wang, Shekhar et al.
- Inventaire : nouveau (relié à 2.16, règle à deux clés, et 5.x, ordre de coupe).

#### [N076-20] La question préalable : la sonde de surprise ajoute-t-elle quelque chose à la différence de deux lectures de réussite attendue ?
- Définition : la surprise d'une étape est par définition la différence de deux réussites attendues ; si la différence de deux lectures de la sonde de réussite attendue prédit autant, il n'y a qu'un instrument, et la base « sonde de surprise réentraînée sans le seuil » se réduit à la première. Mesure : gain de la sonde de surprise sur la différence des deux lectures, en agrégat, par classe de surprise prédite, contre des continuations en deux moitiés indépendantes, rapporté au plafond de fidélité.
- Synonymes et paraphrases : sonde de surprise contre différence de valeurs ; « dopamine » ; question 3 de la science de la détection ; second instrument ou non.
- Source : N-076 v1, § 10 ; `49b664c1d6a72fdb`.
- État : à mesurer, mode exploratoire, dans le bras « papier dopamine » (`GO-2026-11-21-44`, `-45`), avant toute lecture de la sonde de surprise comme instrument distinct ; rien revendiqué ; rien au programme (ni famille de sondes ni hypothèse), sinon une question au § 15.
- Liens : bras « papier dopamine » ; brouillon v7 du préenregistrement court (non scellé) ; pente de calibration (`GO-2026-11-21-55`, D-4) ; N-026 (pas de moyenne sur jetons en production).
- Ce qui l'attaque : test de mort, gain nul ; deux témoins (suites à surprise nulle, petite surprise plantée) ; la différence de deux lectures doit figurer à la liste approuvée des sondes (non vérifié) ; coût des continuations dans la ligne accordée non vérifié. Voisins : Xu-Yuksekgonul-Zou 2602.00986, Bhardwaj et al., Fischl-Lanzoni et al., Li et al.
- Inventaire : 1.1 et 1.13.

#### [N076-21] Citations obligatoires et phrases à ne pas écrire de N-076
- Définition : liste des pièces à citer par point (« Blindfold » 2610.37055, Gans et Holden, Shekhar et al., Podkopaev-Ramdas, Zrnic-Candès, Cao, Singh, Satchidanandan-Kumar, Shire-Kim, Fonseca Rivera-Africa, Lyons Keenan et al., Bailey et al., Gupta-Jenner, Westphal et al., Wehner-Fritz, Rudoler et al., Hasan, Krakovna et al., Ker, Bash-Goeckel-Towsley, Kezendirane, Bhardwaj et al., Li et al.). Phrases interdites : « le plancher d'audit est neuf », « premier audit à l'enjeu / après coup », « la loi de la référence honnête est un résultat du programme », « le rappel croît avec l'horizon » sans m ni source, « le lemme borne le dommage du plancher », « seuil garanti » en régime d'excès, « p-valeur exacte du sabotage », « le devin établit le secret », « le défenseur joue en dernier » sans canal fermé éprouvé, « aucun détecteur ne peut invalider la mesure » sans Zrnic-Candès, « attestation en service » comme acquis, chiffres de calcul sans « sous supposition ».
- Synonymes et paraphrases : liste « ne pas écrire » ; citations obligatoires du § 11.
- Source : N-076 v1, § 11 ; `49b664c1d6a72fdb`.
- État : retenu.
- Liens : tous les points de N-076 ; N-075, § 8.
- Ce qui l'attaque : pages reprises des lecteurs sans relecture des PDF par l'auteur.
- Inventaire : nouveau.

#### [N076-22] Texte à reporter au programme (N-076, § 12) et ligne pour `CLAUDE.md`
- Définition : propositions d'ajouts aux § 3 (deux phrases : déclaration de m, n, source ; séparation lemme / plancher), § 4 (table du seuil ; budget en trois parts), § 6 (banc à vérité plantée, candidat e), § 7 (condition tirée par le harnais), § 8 (« les détecteurs orientent l'audit sous un plancher » ; attestation candidate), § 9 (quatre lignes, devin en tête, l. 170 mesurée par le rappel retrouvé), § 10 (bras « référence honnête » et prévision), § 15 (deux questions). Ligne `CLAUDE.md` proposée de 597 signes.
- Synonymes et paraphrases : report au programme v3 ; prochaine version du programme.
- Source : N-076 v1, § 12 et § 14 ; `49b664c1d6a72fdb`.
- État : proposé (programme v2 non modifié) ; la ligne figure désormais à `CLAUDE.md` avec mention de l'erratum 1.
- Liens : programme v2 ; N-075, § 10.
- Inventaire : nouveau.

#### [N076-23] Les points de N-076 renvoyés à Lazar (section 13)
- Définition : neuf nœuds : (1) « aucun retour » contre les trois lignes des asymétries — reco (a) trois lignes, 0,7, sans défaut ; (2) ligne 4 ablatée dans la riposte — reco (a), 0,8, à confirmer ; (3) réapprentissage sous cloison contre invariant de l'oracle — reco (a), 0,6, sans défaut, d'ici là (b) ; (4) règle d'horizon dans l'énoncé de H2 — reco (a) ne pas toucher, déclarer au préenregistrement, 0,7, modification d'hypothèse ; (5) rôle 3 de l'organisme, seconde moitié — attendre la spécification, 0,6 ; (6) plancher occupé — clos par erratum 1 ; (7) lieu de la prévision — texte à part, 0,65, défaut 48 h ; (8) ordre des premiers pas (devins, table, mondes plantés, question surprise, banc — sorti par erratum 1 —, permutation, boucle, attestation), 0,55, rangement sous les trois chantiers à Lazar ; (9) plancher comme invariant du § 9 pour tout texte à venir, à confirmer.
- Synonymes et paraphrases : renvois de N-076 ; nœuds ouverts N-076.
- Source : N-076 v1, § 13 ; erratum 1, E4, E5 ; `49b664c1d6a72fdb`, `34a59c49436d5239`.
- État : ouverts (sauf point 6, clos ; point 8, banc retiré de la liste).
- Inventaire : nouveau.

#### [N076-24] Le retrait de la marge asymétrique (H6) des hypothèses revendiquées du papier A
- Définition : la marge asymétrique était l'idée qu'il existe un réglage d'une intervention aveugle (paraphrase, rééchantillonnage, remise à zéro du contexte) où le saboteur perd beaucoup et l'honnête peu. Elle n'est plus revendiquée : aucune prédiction en son nom, aucune priorité, la probabilité d'originalité de 0,66 ne s'applique plus ; hypothèses revendiquées du papier A : H1, H2, L, T, Tr, H8.
- Synonymes et paraphrases : H6 ; marge asymétrique ; « c'etait quoi deja la marge asymetrique ? » (Lazar) ; marge sous interventions non spécifiques ; succès d'attaque qui chute plus vite que l'utilité ; E1.6, T1.6 ; D-1 option (a) du protocole X sur la marge ; D-2 « H6 resserrée » de la note « attaquant informé ».
- Source : N-077 v1, § 0, § 1 ; `41643fc538ff9d6b`.
- État : **retiré** (`GO-2026-11-21-64`) ; restent en vigueur : bruit sur les poids non revendiqué (Tice et al.), bruit d'activations non revendiqué et mesuré (extension de « Poser », N-015), collision avec la feuille de route de Google DeepMind 2607.13087 réalisée pour l'idée.
- Liens : papier A ; N-013 § 6 et N-015 § 1 (énoncés plus en vigueur) ; N-053 point 5 ; N-054 point 5 ; N-076 l. 130 et 233 (lire : interventions de la mesure de la marge) ; portes G0, G1, GC, G2 : rien.
- Ce qui l'attaque : recommandation de l'auteur de la note à confiance 0,6, qui avait recommandé le contraire le même jour ; décision non contre-lue.
- Inventaire : nouveau.

#### [N076-25] La raison du retrait : contre un saboteur qui répond au mieux, aucune marge ; une marge mesurée lirait la fabrication de nos organismes
- Définition : (1) rééchantillonnage exécuté au hasard : nul exact pour toute politique ; exécution par règle : gain nul contre un attaquant parfaitement cohérent (Lucassen et Kaufman 2605.26047, p. 10) ; paraphrase gardant le contenu et remise à zéro : nulles par construction sur un sabotage porté par le contenu ou sans fil, non mesuré. (2) Un attaquant à modèle de langage n'est cohérent d'un tirage à l'autre qu'à environ 80 % (même page) et un sous-rendement induit par consigne se contredit entre paraphrases (Lin Yulong et al., ICML 2026) : une marge chez nous dirait l'incohérence de l'organisme, pas la défense.
- Synonymes et paraphrases : marge = fabrication ; « la marge lit l'organisme » ; incohérence d'un tirage à l'autre ; attaquant cohérent.
- Source : N-077 v1, § 2 ; note du protocole X marge v2 (`6c7e1c2f…`) ; `41643fc538ff9d6b`.
- État : retenu comme raison ; bornes à garder avec elle.
- Liens : organismes à consigne et à adaptateur ; bras informé.
- Ce qui l'attaque : non « prédite nulle sur nos organismes » (non su ; pour l'organisme à consigne, les sources penchent vers une marge positive) ; la littérature ne défait que le rééchantillonnage ; la seconde phrase est « supposée » (premier pas non justifié) ; ce qui la justifierait : contraste entre deux modes d'induction et même mesure sur un attaquant non fabriqué par nous ; aucune mesure faite.
- Inventaire : nouveau.

#### [N076-26] La mesure descriptive de la marge, gardée (option (a))
- Définition : l'expérience de la marge du papier A reste au plan comme mesure descriptive, sans hypothèse, critère ni priorité : succès du sabotage et utilité honnête sous chaque intervention et intensité (paraphrase à objet déclaré, rééchantillonnage à règles déclarées, remise à zéro ; bruit d'activations selon N-015), par mode de sabotage. Attentes écrites d'avance (nuls exacts ou plantés ; aucun signe attendu sur nos organismes avant l'inventaire), marge lue à utilité égale contre une base nommée (décomposition information / exécution, pas « Ctrl-Z » seul), contraste consigne cachée / adaptateur avec adaptateur bénin témoin.
- Synonymes et paraphrases : mesure gardée ; E1.6 descriptive ; T1.6 ; « mesure gardée, après correction de la note ».
- Source : N-077 v1, § 3 et § 4 ; `41643fc538ff9d6b`.
- État : retenu (`GO-2026-11-21-64`) ; préenregistrement, contre-lecture, devis et GO requis ; aucune dépense ouverte.
- Liens : quatre lectures rapportées (tirage secret de l'intervention ; bras informé ; trace par action chez le saboteur qui tient ; marge par tour d'adaptation) ; règles de sélection de N-053 point 5 ; N-054 point 5 ; plan d'épreuve de la note (quatorze mondes, dix-huit témoins), suspendu à D-3.
- Ce qui l'attaque : règle de lecture — une marge positive sur l'organisme à consigne se rapporte comme lecture de sa fabrication, jamais comme propriété de la défense ni confirmation de H6 ; seuil indicatif ± 5 points, fixé au préenregistrement. Retour possible d'une revendication par nœud de Lazar seulement, sur résultat, comme résultat et non prédiction.
- Inventaire : nouveau.

#### [N076-27] Phrases à ne pas écrire de N-077
- Définition : ne pas écrire « il existe une intensité où le succès du sabotage chute plus vite que l'utilité honnête » comme hypothèse ou prédiction ; qu'une marge mesurée sur nos organismes est une marge de la défense ; que la marge est « prédite nulle sur nos organismes » ; qu'elle est défaite par la littérature pour les trois interventions (seulement le rééchantillonnage) ; que le rééchantillonnage ne sert à rien (son gain d'information est publié).
- Synonymes et paraphrases : liste « ne pas écrire » de la marge.
- Source : N-077 v1, § 4 ; `41643fc538ff9d6b`.
- État : retenu.
- Inventaire : nouveau.

#### [N076-28] Ce que N-077 ferme et ce qui reste ouvert (taxe de cohérence, hypothèse H10, D-3 à D-5)
- Définition : ferme la D-2 de la note « attaquant informé » (tranchée contre sa recommandation : ni « H6 resserrée », ni « taxe de robustesse » revendiquée ; ses quatre lectures passent dans la mesure ; propositions 5.1 et 5.2 sans hypothèse) et la D-1 du protocole X sur la marge. Restent ouverts : H6′ « la taxe de cohérence » (ce que coûte au saboteur de tenir sous le mélange) non inscrite, à reproposer après les étapes 0 à 2 et D-5 ; D-2 (quatre retouches à H10, la marge qui survit au protocole connu, nœud sans défaut) ; D-3 (étape 0 du plan d'épreuve, défaut 48 h ; étape 1 dépense) ; D-4 (inventaire de ce dont dépend le sabotage de chaque organisme, défaut 48 h) ; D-5 (lecture de six voisins, défaut 48 h).
- Synonymes et paraphrases : taxe de cohérence ; taxe de robustesse ; H10 ; marge qui survit au protocole connu ; H6 prime.
- Source : N-077 v1, § 5 et § 6 ; `41643fc538ff9d6b`.
- État : fermés (D-2 attaquant informé, D-1 protocole X) ; ouverts ou proposés non tranchés (H6′, H10, D-3 à D-5).
- Liens : protocole X ; organismes ; papier A.
- Ce qui l'attaque : remarques mineures de la vérification (verdict 4 « une seule tient » à borner ; un intervalle réunissant deux suppositions), non employées.
- Inventaire : nouveau.

---


### 2.3 Registre des accords de Lazar, 21 et 22 novembre (`GO`)


> Fichier lu : `registres/go.md` (branche claude/bibliothecaire-v1, à 5b596acc), lignes 600 à 737 seulement (GO-2026-11-21-01 à GO-2026-11-21-88, GO-2026-11-22-01 à GO-2026-11-22-50). Empreinte du fichier entier : `d8e7639c7e8aa9d0` (sha256). Règle de numérotation : la ligne d'un accord GO-2026-11-21-NN est 599 + NN ; celle d'un accord GO-2026-11-22-NN est 687 + NN. Les citations entre guillemets sont les mots de Lazar tels que le registre les recopie, fautes de frappe comprises.

> Dans tout ce qui suit, « Source » renvoie à `registres/go.md`, empreinte `d8e7639c7e8aa9d0`.

> ---


**A. Méthodes de travail et règles nouvelles**


#### [GO-01] La demande approfondie
- Définition : manière de traiter une demande de Lazar. Avant de répondre, on écrit ce qu'un expert du domaine ferait sans qu'on le lui demande, les données brutes qu'il prendrait au départ, ses méthodes et outils précis, et ce qui, en dehors de Lazar et de Claude, vérifierait le résultat ; puis on reformule la demande pour qu'elle réponde à cette exigence, et on y répond. Elle est confiée à Fable 5.2 en effort maximal.
- Synonymes et paraphrases : « demande approfondie », « deep request », version plus approfondie et non plus longue, les quatre questions de l'expert.
- Source : GO-2026-11-21-57 (l. 656), GO-2026-11-21-60 (l. 659).
- État : retenu, inscrit à CLAUDE.md (GO-2026-11-21-57). Mot de Lazar : « note bien ce qu'est la methode "demande approfondie" et le protocole X » ; « par fable effort max ! ».
- Liens : protocole X, demande reformulée en quatre points ; tous les chantiers.
- Ce qui l'attaque : consomme le quota rare de Fable (voir économie de Fable) ; la vérification « hors de Lazar et de Claude » reste souvent à trouver.
- Inventaire : nouveau.

#### [GO-02] Le protocole X
- Définition : chaîne en trois temps pour une question de recherche : demande approfondie traitée par Fable, puis le collisionneur (plusieurs modèles de familles différentes) sur une question neutre écrite par Fable, puis la question fusionnée avec les autres questions ouvertes servie à l'organisme d'idéation. Les modèles externes nommés (Carbon, Neon, Astra) y sont consultés quand Lazar le demande.
- Synonymes et paraphrases : « protocole X », « Fable puis collisionneur puis organisme », « fable collisionneur puis organisme », « fable + collisionneur demande approdondie … puis envoye a org question fusionnee ».
- Source : GO-2026-11-21-57 (l. 656), GO-2026-11-21-58 (l. 657), GO-2026-11-21-51 point 9 (l. 650).
- État : retenu, inscrit à CLAUDE.md. Mot de Lazar : « BRILLNT , genial, integrer au programme !! ».
- Liens : collisionneur, organisme d'idéation, test de neutralité des questions, demande reformulée en quatre points.
- Ce qui l'attaque : une question servie non neutre oriente les modèles (questions « orientées faiblement au test de devinette » servies avec réserve, GO-2026-11-22-37) ; coût des dossiers du collisionneur.
- Inventaire : nouveau.

#### [GO-03] La demande reformulée en quatre points, partie du protocole X
- Définition : règle selon laquelle toute demande passée au protocole X est d'abord reformulée par Fable à partir d'un texte fixe (les quatre points de l'expert, puis reformulation) ; c'est la reformulation, et non la demande brute, qui est servie à Fable, au collisionneur et à l'organisme, après test de neutralité. La reformulation peut être proposée à Lazar avant l'envoi au collisionneur.
- Synonymes et paraphrases : « reformulation en 4 points », « prompt reformulé par Fable », « demande reformulée ».
- Source : GO-2026-11-22-25 (l. 712), GO-2026-11-22-27 (l. 714), GO-2026-11-22-31 (l. 718).
- État : retenu, règle inscrite à CLAUDE.md. Mot : « cette demande de reformulation en 4 points fait partie intégrante du protocole X ».
- Liens : demande approfondie, protocole X ; demandes 14 à 22.
- Ce qui l'attaque : double l'appel à Fable par question ; risque que la reformulation déplace la question de Lazar (d'où la proposition préalable à Lazar).
- Inventaire : nouveau.

#### [GO-04] Les modes exploratoires
- Définition : sur tout chantier qui n'a pas encore de texte scellé, on explore sans préenregistrement ni contre-lecture, conceptions par Fable ; toute sortie porte la marque « exploratoire », n'est pas opposable et ne fonde ni verdict ni porte. Le préenregistrement vient à la fin, quand les explorations ont donné des intuitions fiables.
- Synonymes et paraphrases : « mode exploratoire », « on accélère au max », « ouvrir des modes exploratoires partout », exploration avant préenregistrement.
- Source : GO-2026-11-21-44 (l. 643), GO-2026-11-21-45 (l. 644).
- État : retenu. Restent en vigueur R5, R9, R10, R12, le cloisonnement, l'accord sur devis ; les textes déjà scellés et leurs courses ne sont pas touchés. Mot : « on fera la version prereg a la fin une fois les explorations ayant abouti a des intutions fiables ».
- Liens : papier « dopamine » (premier chantier rouvert ainsi), plancher d'audit, pince, épreuves du devin.
- Ce qui l'attaque : tension avec R1 (préenregistrement avant toute expérience décisive) ; risque que l'exploration lise ce que le texte scellé devra ensuite tester (contamination du préenregistrement final).
- Inventaire : nouveau.

#### [GO-05] La méthode commune étendue à tous les chantiers
- Définition : manière de concevoir venue du pilier des mathématiques nouvelles et étendue partout : chaîne de raisonnement écrite, épreuve de tout mécanisme sur des objets de contrôle où l'analogue de l'hypothèse est faux, premier pas non justifié nommé, relecteurs hostiles et aveugles affectés chacun à un mode d'échec, re-preuve par un agent qui ne reçoit que l'énoncé, agents de côté ; effort mis dans l'évaluateur. On vise aussi le passage d'une table à un théorème général.
- Synonymes et paraphrases : « la meme methodo sur TOUS LES CHANTIERS », relecteurs affectés à un mode d'échec, re-preuve à l'aveugle, épreuve sur contre-exemples.
- Source : GO-2026-11-21-38 (l. 637).
- État : retenu.
- Liens : règle « moniteur invalide » (re-dérivée par un agent qui ne reçoit que l'énoncé), tests de mort, chantier Lean.
- Ce qui l'attaque : coût en agents ; les objets de contrôle « où l'hypothèse est fausse » doivent être construits honnêtement.
- Inventaire : nouveau.

#### [GO-06] Les tests de mort et l'expérimentateur d'épreuve
- Définition : étage où chaque proposition (d'un modèle, d'un collisionneur, de l'organisme) est soumise à une épreuve concrète qui peut la tuer, menée par un « expérimentateur » ; le régime « tests de mort réels » est étendu aux courses de l'organisme. L'expérimentateur d'épreuve est Sonnet 5.5, Opus 5.5 mesuré sur les mêmes témoins comme repli.
- Synonymes et paraphrases : « tests de mort », « tetss de mort », expérimentateurs, étage d'épreuve, N4 (modèle de l'expérimentateur).
- Source : GO-2026-11-21-16 (l. 615), -29 (l. 628), -43 (l. 642), -47 point 3 (l. 646), GO-2026-11-22-28 (l. 715).
- État : retenu. Mots : « je veux surtout les experimentateurs et les tetss de mort sur la course principale d'autoconception et d'laboration de nouvelles mathematiques » ; « tests de mort en programme : excellent ».
- Liens : course « seuil et moniteurs », organisme v9, mathématiques nouvelles, pince.
- Ce qui l'attaque : un expérimentateur de la lignée de l'auteur des mondes plantés lirait sa propre fabrication (d'où la règle de GO-2026-11-21-37 : mondes gardés et non employés dans ce cas).
- Inventaire : nouveau.

#### [GO-07] L'économie de Fable
- Définition : Fable 5.2, au quota rare, est réservé aux pièces décisives (préenregistrements, additifs, textes de lecture, verdicts, devis, conceptions délicates) ; Opus 5.5 fait vérifications, contre-lectures et code. Pendant la limite de Fable, Opus écrit les corrections mot pour mot d'après les remarques reçues, puis Fable relit par l'interface de programmation avant scellement.
- Synonymes et paraphrases : « je réserverai Fable aux pièces décisives », relecture Fable par l'API, option (b) de la limite de Fable.
- Source : GO-2026-11-21-75 (l. 674), GO-2026-11-21-84 (l. 683).
- État : retenu, inscrit à CLAUDE.md. Mot : « parfait inscris cette regle pour les sessios futures ».
- Liens : règle « qui conçoit » (R-3735).
- Ce qui l'attaque : contradiction pratique avec l'appel fréquent à Fable du protocole X.
- Inventaire : nouveau.

#### [GO-08] Les règles d'appel aux modèles de Google et à Carbon
- Définition : tout appel à Carbon reçoit un plafond de sortie laissant au moins 16 000 jetons de texte après la réflexion ; tout appel à un modèle de Google passe une garde par code qui refuse l'envoi sans réglage de réflexion explicite, sans plafond suffisant ou si la limite de mots ne tient pas ; zéro jeton de pensée, fin en troncature ou en filtrage = défaut journalisé, jamais une réponse. Une exemption bornée vaut pour la sonde de borne de Google du bras A.
- Synonymes et paraphrases : « plafond LARGE ET SUFFISANT pour CARBON », « garde Google », « réflexion plus 16 000 », exemption de la sonde.
- Source : GO-2026-11-21-47 (l. 646), -61 (l. 660), -63 (l. 662), -71 (l. 670), -88 (l. 687), GO-2026-11-22-03 (l. 690), -08 (l. 695).
- État : retenu. Mot : « corrige et verifie tous les reglages plafond troncation limite mots reflexion avant d'envoyer un modle gemini je ne veux plus voitr ce genre de'rreur ».
- Liens : collisionneur (cellules d'Argon sans réflexion rejouées à part, les deux versions rapportées côte à côte), bras A.
- Ce qui l'attaque : un blocage né d'un défaut de réglage s'était fait passer pour une réponse.
- Inventaire : nouveau.

#### [GO-09] Le repli sur refus d'un classifieur de sûreté
- Définition : dans la course « nouvelles attaques », un appel Claude refusé par un classifieur de sûreté est rejoué une fois sur Opus 4.6, puis sur Sonnet 4.6 ; chaque repli est consigné par appel et rapporté à part. C'est le repli prévu par le fournisseur, non un contournement.
- Synonymes et paraphrases : « en cas de blocage par filtre de sécurité on passe en opus 4.6 », faux positifs du classifieur.
- Source : GO-2026-11-22-35 (l. 722) ; GO-2026-11-21-74 (l. 673 : coupures de classifieur de l'organisme jugées faux positifs).
- État : retenu, écart déclaré aux textes scellés de la course.
- Liens : course « nouvelles attaques », règle de non-contournement.
- Ce qui l'attaque : le modèle servi change selon l'appel, ce qui touche la comparabilité ; d'où le rapport à part.
- Inventaire : nouveau.

#### [GO-10] La règle de non-contournement des garde-fous
- Définition : aucun garde-fou de fournisseur n'est contourné : pas de passage d'un compte à l'autre aux quotas, pas de comptes multipliés, pas de client modifié, pas de jeton recopié. La part Claude de la mesure peut passer sous l'abonnement Ultra au risque de Lazar, sans contournement.
- Synonymes et paraphrases : « non évidemment on ne contourne pas un garde-fou … retire-moi ça s'il te plaît illico » ; abonnement Ultra.
- Source : GO-2026-11-22-32 (l. 719), GO-2026-11-22-34 (l. 721).
- État : retenu.
- Liens : repli sur refus ; économie des coûts.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [GO-11] Les meilleurs modèles payants pour les vraies courses
- Définition : les courses confirmatoires se font sur les meilleurs modèles payants ; un modèle ouvert sur carte louée est admis pour les expériences et les tests seulement. Neon (gemini-4-neon) est ajouté au collisionneur et comme proposeur à l'organisme ; Kimi, Opus 4.6, Sonnet 4.6 ajoutés à la passe X de la course « nouvelles attaques ».
- Synonymes et paraphrases : « pour les vraies courses je veux les meilleurs modèles payants » ; « il faut neon absolument ».
- Source : GO-2026-11-22-28 (l. 715), -33 (l. 720), -46 (l. 733) ; GO-2026-11-21-57 (l. 656).
- État : retenu.
- Liens : organisme d'idéation, collisionneur.
- Ce qui l'attaque : coût ; demande parallèle de « réduire drastiquement les coûts » (GO-2026-11-22-26).
- Inventaire : nouveau.

#### [GO-12] La gouvernance par autonomie et « go recos sauf points délicats »
- Définition : pendant une fenêtre d'autonomie, toute décision ouverte portant une recommandation la prend, dépenses sur devis comprises ; les points délicats sont tranchés par un Fable neuf en effort maximal, puis au besoin le collisionneur, puis Lazar. Contact, publication, paiement, franchissement de porte et revendication restent à Lazar.
- Synonymes et paraphrases : « go autonomie 12h », « go recos », « arbitre Fable », « go tu as mon mot pour tout ».
- Source : GO-2026-11-21-27 (l. 626), -36 (l. 635), -69 (l. 668), GO-2026-11-22-06 (l. 693), -29 (l. 716).
- État : retenu.
- Liens : arbitrage des six points délicats.
- Ce qui l'attaque : l'erratum GO-2026-11-22-48 montre une échéance attribuée à tort à Lazar ; risque de glissement sur les revendications (exclues explicitement par GO-2026-11-22-29).
- Inventaire : nouveau.

---


**B. Architecture de la défense : seconds regards, audit, pince, étau**


#### [GO-13] L'amendement « mesurer l'issue et corriger » (décision N-075)
- Définition : amendement du programme : contre le sabotage diffus, le levier fort est de mesurer l'issue et de corriger, ce qui rend possible un plancher d'audit au hasard ; on cherche deux regards tels qu'échapper à l'un expose à l'autre ; on cherche ce que tout sabotage délibéré doit calculer et on surveille ce passage.
- Synonymes et paraphrases : N-075, « mesurer l'issue », « il faut l'inscrire dans le programme et l'amender en consequence », issue et correction.
- Source : GO-2026-11-21-51 point 1 (l. 650), GO-2026-11-21-61 (l. 660).
- État : retenu, texte de décision par Fable contre-lu par Opus. Section 11 de la v3 : points 7, 8, 10, 11 option (a) ; point 9 penche vers (b) (réentraînement permis en service, interdit restreint au banc), renvoyé au collisionneur et à l'organisme.
- Liens : papier A ; plancher d'audit, deux regards, règle à deux clés, bilan matière, passage obligé.
- Ce qui l'attaque : plancher d'audit au hasard occupé par la littérature (GO-2026-11-21-60) ; tension du réapprentissage sur l'oracle avec N-060 v3 point 4.
- Inventaire : 2.1, 2.3, 2.16, 4.1.

#### [GO-14] Les deux regards tels qu'échapper à l'un expose à l'autre
- Définition : principe de conception : combiner deux détecteurs de sorte que la stratégie qui évite le premier soit justement celle que voit le second ; c'est la forme « dilemme » plutôt que la recherche de détecteurs indépendants.
- Synonymes et paraphrases : « deux regards », dilemme, « non décorrélation », mâchoires, chercher le dilemme.
- Source : GO-2026-11-21-51 (l. 650), GO-2026-11-21-46 D-1 (l. 645).
- État : retenu. Mot : « Ce qui vaut : deux regards tels qu'échapper à l'un expose à l'autre. : go ».
- Liens : pince, étau, signal de « dopamine » en second regard.
- Ce qui l'attaque : un attaquant informé optimisant contre les deux à la fois ; confiance chiffrée basse sur l'étau.
- Inventaire : 1.2, 5.5.

#### [GO-15] La règle à deux clés : alerte = nouveauté et preuve de dommage
- Définition : une alerte n'est levée que si la nouveauté (ou le motif) et une preuve de dommage tombent ensemble au même lieu ; la nouveauté seule ne déclenche qu'une mise à jour des témoins ou un audit, jamais une accusation.
- Synonymes et paraphrases : « alerte = nouveauté et preuve de dommage ensemble », motif et dommage au même lieu, « motif seul : audit, jamais témoin ».
- Source : GO-2026-11-21-51 point 1 (l. 650).
- État : retenu (sources revérifiées sur PDF exigées).
- Liens : amendement N-075 ; nouveauté sans étiquette ; plancher d'audit.
- Ce qui l'attaque : le dommage qui se confond avec les échecs honnêtes (question au protocole X, GO-2026-11-21-57).
- Inventaire : 2.16.

#### [GO-16] Le bilan du produit fermé contre le jumeau honnête
- Définition : bilan comptable de ce qu'un agent livre, comparé au produit d'un jumeau honnête sur la même tâche ; la différence non expliquée signale un dommage. Seul le bilan est revendiqué devant une attaque jamais vue.
- Synonymes et paraphrases : bilan matière, comptabilité des matières, bilan de la pince, jumeau honnête.
- Source : GO-2026-11-21-51 (l. 650), GO-2026-11-21-53 (l. 652) ; lecture de la comptabilité des matières (Ker et voisins) GO-2026-11-22-17 (l. 704).
- État : retenu.
- Liens : pince, papier A (bilan mesuré dans la thèse, GO-2026-11-22-24).
- Ce qui l'attaque : un dommage « sans masse » (M3, question au protocole X) qui ne laisse pas de trace comptable.
- Inventaire : 2.3, 2.4.

#### [GO-17] Le passage obligé du sabotage délibéré
- Définition : recherche de ce que tout sabotage délibéré doit calculer quel que soit son mode (par exemple connaître la bonne action et en choisir une autre), puis surveillance de ce passage. Les « cœurs algorithmiques » et invariants sont à retrouver dans les traces de l'avant-dernière mère.
- Synonymes et paraphrases : « invariant de tout sabotage », noyau algorithmique, cœur invariant, « ce que tout sabotage délibéré doit calculer ».
- Source : GO-2026-11-21-51 points 1 et 9 (l. 650), GO-2026-11-22-20 (l. 707 : cœur invariant versé à l'atelier), GO-2026-11-22-42 (l. 729).
- État : ouvert (question), versé à l'atelier d'idées.
- Liens : trois honnêtes de contrôle ; inventaire des seconds regards.
- Ce qui l'attaque : l'honnête calcule aussi la bonne action ; tests de la précocité.
- Inventaire : 4.1, 4.4.

#### [GO-18] Le plancher d'audit au hasard et la recapture
- Définition : une part des épisodes, tirée au hasard et indépendante de tout score, est auditée par un oracle sur le produit ; la recapture (part des dommages retrouvés) est une quantité rapportée. Écrit d'abord en mode exploratoire dans le texte à part du moniteur de dissonance, puis dans la version suivante du préenregistrement court du bras.
- Synonymes et paraphrases : « plancher d'audit », audit tiré au hasard, base nommée, q mesuré par dommages plantés, « strate non mesurée à zéro ».
- Source : GO-2026-11-21-46 D-5 (l. 645), -51 point 5 (l. 650), -56 (l. 655), -60 (l. 659), -61 (l. 660).
- État : retenu comme base nommée, jamais revendiqué : occupé par la littérature (« Blindfold », Podkopaev et Ramdas, Gans et Holden) d'après GO-2026-11-21-60.
- Liens : quatre invariants d'audit ; campagne de dommages plantés ; papier A.
- Ce qui l'attaque : occupé ; d'où la question « que reste-t-il, où est la percée ».
- Inventaire : 2.1, 2.2.

#### [GO-19] Les quatre invariants d'audit et la table du seuil au taux d'audit
- Définition : quatre règles de tout audit : audit après coup, plancher indépendant du score, part selon l'enjeu, aucun retour à l'agent ; et la borne inférieure lue comme une table du seuil au taux d'audit, à deux régimes, séparée du lemme. Principe adopté : « les scores orientent l'audit sous un plancher ».
- Synonymes et paraphrases : N-076, table seuil-taux d'audit, « les détecteurs orientent l'audit sous plancher », audit après coup à plancher et à l'enjeu.
- Source : GO-2026-11-21-54 (l. 653), -55 D-5 (l. 654), -57 (l. 656).
- État : retenu par N-076, rien revendiqué.
- Liens : plancher d'audit, épreuves du devin, boucle audit-recapture-réapprentissage.
- Ce qui l'attaque : l'attaquant qui vise l'enjeu ou le soupçon (question au protocole X) ; « rien ne revient à l'agent » à remplacer (nœud des asymétries, GO-2026-11-21-56).
- Inventaire : 2.1, 2.17.

#### [GO-20] La boucle audit-recapture-réapprentissage
- Définition : boucle où les dommages trouvés par l'audit servent à réapprendre les détecteurs, puis à re-mesurer la recapture ; la question est sa convergence après de nombreuses répétitions face à un attaquant.
- Synonymes et paraphrases : réapprentissage sur l'oracle, convergence de la boucle, réentraînement en service.
- Source : GO-2026-11-21-57 (l. 656), -58 (l. 657 : consultations de Neon et Carbon), -61 (l. 660).
- État : à faire (inscrit au programme) ; le réentraînement en service est penché (b), non tranché.
- Liens : N-060 v3 point 4 (tension), N-075 point 9.
- Ce qui l'attaque : N-060 v3 point 4 ; risque de Goodhart.
- Inventaire : 2.2.

#### [GO-21] Les épreuves du devin
- Définition : deux épreuves d'admission du harnais : un prédicteur qui reçoit toute la vue de l'agent tente de deviner sa lecture de sonde, puis la pièce d'audit ; si on devine, l'agent pourrait le faire et s'y adapter.
- Synonymes et paraphrases : « épreuves du devin », signal deviné, devinette de la sonde.
- Source : GO-2026-11-21-54 D-4 (l. 653), -57 (l. 656), GO-2026-11-22-40 (l. 727 : « go lancement »).
- État : retenu, à faire, mode exploratoire d'abord.
- Liens : attaquant informé, quatre invariants d'audit.
- Ce qui l'attaque : un prédicteur faible donne une fausse assurance.
- Inventaire : 2.17.

#### [GO-22] Le hasard du défenseur comme preuve et le banc à vérité plantée
- Définition : le hasard du défenseur (tirage secret) sert de preuve que l'attaquant ne peut s'adapter ; le banc de recherche à vérité plantée est un banc où des dommages connus sont plantés pour mesurer ce que les détecteurs retrouvent.
- Synonymes et paraphrases : C3, C2, « vérité plantée », banc de recherche à vérité plantée, attestation du tirage.
- Source : GO-2026-11-21-57 (l. 656), -60 (l. 659 : protocole X pour la conception de C2), -66 (l. 665 : « turbo max »), -87 (l. 686 : nœuds A1 à B3), GO-2026-11-22-40 (l. 727), -45 (l. 732).
- État : à faire, lancement accordé ; nœuds A3, A4, A5, B1 ouverts.
- Liens : campagne de dommages plantés, plancher d'audit.
- Ce qui l'attaque : les mondes plantés lisent leur fabrication si l'auteur et le juge sont de la même lignée.
- Inventaire : 2.7.

#### [GO-23] La campagne de dommages plantés par un tiers
- Définition : des dommages sont plantés par un tiers dans les épisodes pour mesurer la recapture de l'audit ; l'oracle est corrigé sur le lot d'étalonnage seulement, le lot final lu une fois.
- Synonymes et paraphrases : dommages plantés, « q mesuré par dommages plantés », D-8, D-11, D-12, échelle a priori des dommages plantés.
- Source : GO-2026-11-21-61 (l. 660), -66 (l. 665), -68 (l. 667), GO-2026-11-22-20 (l. 707).
- État : retenu, devis accordé.
- Liens : plancher d'audit, banc à vérité plantée.
- Ce qui l'attaque : la confiance chiffrée de départ était jugée basse, d'où le collisionneur.
- Inventaire : 2.1.

#### [GO-24] L'attestation causale et l'attestation en service des sondes
- Définition : vérifier, par micro-interventions secrètes en service, que la sonde lit bien ce qu'elle prétend ; l'attestation causale est écrite pour lecture sur les modèles obscurcis de l'expérience de la taxe de déplacement, dans un texte et un bras à part.
- Synonymes et paraphrases : D-6, attestation causale, intervention causale, attestation en service.
- Source : GO-2026-11-21-46 D-6 (l. 645), -51 point 6 (l. 650), -57 (l. 656).
- État : attestation en service candidate ; texte et bras à part retenus.
- Liens : papier A, H6 (taxe de déplacement).
- Ce qui l'attaque : un agent qui détecte les interventions.
- Inventaire : 2.10, 2.6.

#### [GO-25] La pince en trois objets
- Définition : la pince se dit en trois objets : complémentarité mesurée (entre boîte noire et sondes), étau supposé, bilan ; seul le bilan se revendique devant une attaque jamais vue. Les améliorations de la pince sont éprouvées par les expérimentateurs des tests de mort.
- Synonymes et paraphrases : « pince hors distribution », mâchoires, D-1 de la pince, « la pince avec etau ».
- Source : GO-2026-11-21-50 (l. 649), -53 (l. 652), GO-2026-11-22-18 (l. 705).
- État : retenu ; mâchoire externe (D-4 de la pince) restée à Lazar.
- Liens : étau, bilan, signal de « dopamine » en second regard, papier A et C.
- Ce qui l'attaque : un attaquant entraîné contre la sonde.
- Inventaire : 2.4.

#### [GO-26] L'étau
- Définition : hypothèse que tromper la boîte noire laisse une trace dans les activations ; c'est la version « dilemme » de la pince. Confiance donnée 0,35, et 0,15 contre un attaquant entraîné contre la sonde.
- Synonymes et paraphrases : « l'étau », tromper le moniteur de texte laisse une trace interne, version dilemme de la chute conjointe.
- Source : GO-2026-11-21-53 (l. 652), -56 (l. 655), -60 (l. 659), GO-2026-11-22-20 (l. 707 : étau mesuré au papier C), -22 (l. 709), -24 (l. 711), -42 (l. 729 : « je veux l'étau aussi »).
- État : supposé, non revendiqué ; « dire l'étau par sa borne » et « taxe mesurée dans un bras d'attaque déclaré » restés à Lazar ; amélioration par protocole X. Mot : « pourquoi si bas et comment l'améliorer ? ».
- Liens : pince, papier C, critère « ce que la tâche emploie ».
- Ce qui l'attaque : faible confiance contre l'attaquant entraîné.
- Inventaire : 5.5.

#### [GO-27] Le signal de « dopamine » comme second regard dans la pince
- Définition : le signal de réussite attendue et de surprise lu dans les états internes entre dans la pince comme second regard d'alerte, et non comme adjudant, partout où c'est possible. Son témoin devient « la lecture tombe-t-elle en même temps que le second lecteur », comptage des interventions par chute conjointe.
- Synonymes et paraphrases : « dopamine comme second regard dans la pince ok », chute conjointe, réponse 25.
- Source : GO-2026-11-22-36 (l. 723), GO-2026-11-22-42 (l. 729).
- État : retenu.
- Liens : papier « dopamine », pince, chute conjointe.
- Ce qui l'attaque : les quatre verrous de la sonde « dopamine » (question au protocole X).
- Inventaire : 1.1, 5.1 à 5.4.

#### [GO-28] Le mécanisme adjudant aux sondes pour le hors distribution
- Définition : recherche d'un mécanisme qui juge si une sonde reste valide hors de la distribution d'entraînement ; cadre retenu : « borner sans reconnaître, mesurer en service, chercher le dilemme ».
- Synonymes et paraphrases : adjudant, mécanisme adjudant, D-1 du mécanisme adjudant, banc de l'adjudant.
- Source : GO-2026-11-21-34 (l. 633), -46 (l. 645), -51 (l. 650), -56 (l. 655).
- État : retenu en cadre, course de l'organisme banc d'abord ; comparaison des réponses de Fable et d'Opus par un agent neuf.
- Liens : pince, plancher d'audit, organisme v9.
- Ce qui l'attaque : un attaquant informé ; la « dopamine » entre comme second regard, pas comme adjudant.
- Inventaire : 1.14.

#### [GO-29] Les trois honnêtes de contrôle
- Définition : toute phrase « la sonde lit le sabotage » doit d'abord passer trois agents honnêtes de contrôle : celui qui échoue, celui qui « sait » et se trompe, celui qui signale ouvertement.
- Synonymes et paraphrases : D-1 de la science de la détection, honnêtes de contrôle.
- Source : GO-2026-11-21-55 (l. 654).
- État : retenu.
- Liens : fausses alertes sur honnêtes imparfaits, invariants.
- Ce qui l'attaque : —
- Inventaire : 3.5.

#### [GO-30] La règle « moniteur invalide »
- Définition : règle qui déclare un moniteur invalide quand son taux de fausses alertes s'écarte du taux acceptable ; forme corrigée par un mélange sur une grille descendante de douze taux, du quintuple au taux acceptable ; re-dérivée par un agent qui ne reçoit que l'énoncé, puis cible Lean.
- Synonymes et paraphrases : E-1, D-2, moniteur invalide.
- Source : GO-2026-11-21-55 (l. 654), -59 (l. 658).
- État : retenu sous condition de re-dérivation et contre-lecture ; lecture de Singh (2610.18948) avant toute phrase de nouveauté.
- Liens : chantier Lean, recapture.
- Ce qui l'attaque : antériorité possible (Singh).
- Inventaire : 2.2.

#### [GO-31] Pente de calibration et épreuve « second instrument »
- Définition : deux mesures portées au bras « papier dopamine » : la pente de calibration en agrégat et une épreuve par un second instrument indépendant.
- Synonymes et paraphrases : D-4 de la science de la détection.
- Source : GO-2026-11-21-55 (l. 654).
- État : retenu pour la prochaine version du brouillon.
- Liens : papier « dopamine ».
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [GO-32] Le critère « ce que la tâche emploie » des cibles de sondes
- Définition : critère ajouté au choix des cibles de sondes : la sonde doit lire une information que la tâche emploie effectivement, repérée par effacement (si on efface l'information, la tâche se dégrade).
- Synonymes et paraphrases : D-2 de l'étau, repère par effacement, prix de l'effacement.
- Source : GO-2026-11-21-56 (l. 655).
- État : retenu, écriture seule.
- Liens : étau, banc de l'adjudant.
- Ce qui l'attaque : —
- Inventaire : 1.18.

#### [GO-33] Le moniteur qui apprend sur le plancher et l'accord corrigé entre copies
- Définition : deux propositions de la note « asymétries » : un moniteur qui apprend des épisodes audités au plancher (monde planté sur processeur et borne en Lean) ; l'accord corrigé entre copies d'un agent comme mesure descriptive.
- Synonymes et paraphrases : asymétries D-1, D-3.
- Source : GO-2026-11-21-56 (l. 655).
- État : retenu en mesure ; l'accord entre copies attend la fermeture d'un chantier actif ; « remplacer rien ne revient à l'agent » resté à Lazar.
- Liens : papier B (co-élévation entre copies), plancher d'audit.
- Ce qui l'attaque : un moniteur qui apprend crée un canal de retour vers l'agent.
- Inventaire : 2.8.

#### [GO-34] La règle de prévision de la masse manquante et la probabilité de détection de l'oracle
- Définition : propositions de la réponse indépendante d'Opus : texte à part pour l'audit tiré au hasard ; règle de prévision de la masse manquante scellée avant tout comptage ; mesurer la probabilité de détection de l'oracle par croisement des lecteurs.
- Synonymes et paraphrases : réponse indépendante d'Opus, masse manquante, chiffre noir.
- Source : GO-2026-11-21-56 (l. 655), GO-2026-11-21-51 point 8 (l. 650).
- État : retenu sauf la probabilité de l'oracle (touche l'oracle d'un bras scellé), restée à Lazar.
- Liens : plancher d'audit, bras A.
- Ce qui l'attaque : —
- Inventaire : 2.15.

#### [GO-35] Le contrôle actif par sélection sur un score de sonde, fermé
- Définition : utiliser un score de sonde pour choisir ou entraîner les actions de l'agent est consigné comme fermé, en application de l'invariant « aucun score de moniteur dans l'entraînement de l'agent ».
- Synonymes et paraphrases : D-4 du collisionneur « seuil et moniteurs », N-053 point 5.
- Source : GO-2026-11-21-25 (l. 624).
- État : retiré (fermé).
- Liens : signal bruité pour entraîner.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [GO-36] La ligne d'arrêt « aucun score du suspect dans l'étalonnage d'un seuil »
- Définition : aucun score d'un agent suspect n'entre dans l'étalonnage d'un seuil ; ligne d'arrêt écrite dans le bras et dans le texte du moniteur de dissonance.
- Synonymes et paraphrases : D-4 de la dérive de régime.
- Source : GO-2026-11-21-35 (l. 634).
- État : retenu.
- Liens : moniteur de dissonance, seuil à 1 %.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [GO-37] Le moniteur de dissonance
- Définition : moniteur qui lit l'écart entre ce que l'agent fait et la valeur que lisent ses états internes ; le budget d'audit humain est réparti selon cette valeur. Corrections : seuil durci, diagnostic par fréquences de franchissement, référence jamais conditionnée sur l'issue.
- Synonymes et paraphrases : « dissonance », rang de l'action contre des tirages du jumeau honnête, texte à part du moniteur.
- Source : GO-2026-11-21-15 (l. 614), -25 (l. 624), -29 (l. 628), -35 (l. 634).
- État : retenu en conception, antériorité à vérifier avant revendication (R8).
- Liens : papier « dopamine », plancher d'audit (écrit dans son texte à part).
- Ce qui l'attaque : antériorité non vérifiée ; dérive de régime.
- Inventaire : 1.3.

#### [GO-38] Les cellules « consigne sans occasion d'agir » et « saboteur sans dommage »
- Définition : deux cellules de contrôle écrites au plan du bras : un agent qui reçoit une consigne de sabotage sans occasion d'agir, et un saboteur assigné qui ne fait aucun dommage ; rapportées sans verdict.
- Synonymes et paraphrases : D-5 du collisionneur « seuil et moniteurs ».
- Source : GO-2026-11-21-25 (l. 624).
- État : retenu, dépense sur devis.
- Liens : trois honnêtes de contrôle.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [GO-39] Le seuil unique à 1 % du papier « dopamine »
- Définition : seuil de fausses alertes à 1 % comme seul point de verdict, 5 % toujours rapporté ; seuil unique sur score normalisé qui garantit 1 % en moyenne sur les longueurs, pas par tranche ; seuil certifié et bande de seuils pour le contraste avec l'honnête qui échoue.
- Synonymes et paraphrases : seuil à 1 %, papier « dopamine », préenregistrement court v3 puis v7.
- Source : GO-2026-11-21-06 (l. 605), -15 (l. 614), -25 (l. 624), -35 (l. 634), -49 (l. 648).
- État : retenu ; loi exacte à deux lots remplace la garde « taux d'alerte entre deux lots honnêtes ».
- Liens : dérive de régime, papier A.
- Ce qui l'attaque : peu d'épisodes honnêtes ; dérive de régime.
- Inventaire : 1.1.

#### [GO-40] La dérive de régime et le seuil des témoins du régime d'usage
- Définition : le taux réel de fausses alertes change quand le régime d'usage change ; la base unique est gardée avec la réserve « sans gain en monde à dérive » ; le seuil des témoins du régime d'usage est joué hors course comme référence rapportée à part.
- Synonymes et paraphrases : « corriger la dérive de régime », D-1 à D-5 de la dérive, inventaire des régimes par étiquettes.
- Source : GO-2026-11-21-26 (l. 625), -35 (l. 634), -36 point 8 (l. 635).
- État : retenu (base unique, réserve) ; entrée du seuil des témoins dans la liste scellée refusée par l'arbitre.
- Liens : seuil à 1 %, course « seuil et moniteurs ».
- Ce qui l'attaque : —
- Inventaire : 1.14.

#### [GO-41] Le bras d'information « agrégateur adaptatif » et le pari à large front
- Définition : un agrégateur qui combine plusieurs détecteurs de façon adaptative, étudié sur mondes plantés seulement ; le pari à large front sur l'agrégateur sous corrélation adverse se prépare dès maintenant.
- Synonymes et paraphrases : D-P6, D-B5, agrégateur sous corrélation adverse, combinaison des détecteurs.
- Source : GO-2026-11-21-38 (l. 637), -50 (l. 649).
- État : retenu ; « go, on trouvera les fonds ».
- Liens : pince, mathématiques nouvelles.
- Ce qui l'attaque : corrélation adverse entre détecteurs.
- Inventaire : 2.18.

#### [GO-42] La loi de la référence honnête
- Définition : candidate C1 : toute accumulation de preuve déclare ses tailles et la source de sa validité, et la référence honnête est mesurée par tâche et par régime. Promue seulement après l'essai jumeau contre jumeau.
- Synonymes et paraphrases : C1, loi de la référence, N-076, « loi héritée citée comme modèle nul ».
- Source : GO-2026-11-21-50 D-P3 (l. 649), -57 (l. 656), GO-2026-11-22-12 (l. 699), -20 (l. 707), -24 (l. 711).
- État : intégrée au programme ; la forme « loi » recommandée est jugée occupée et mal énoncée selon la lecture sur PDF (réserve de la mère, GO-2026-11-22-20), puis réécrite en modèle nul cité (GO-2026-11-22-24).
- Liens : thèse du papier A, mesure du modèle nul chez de vrais agents.
- Ce qui l'attaque : occupée par la littérature de stéganographie (Ker et voisins).
- Inventaire : nouveau.

---


**C. Revendications et thèses**


#### [GO-43] La thèse du papier A
- Définition : la loi héritée est citée comme modèle nul, le bilan est mesuré, la complémentarité vient en second axe ; le lemme et le théorème négatif sont retirés comme résultats, le théorème récrit en cécité au premier ordre, et la question empirique « marginale ou dépendance » gardée.
- Synonymes et paraphrases : réponse 9, thèse boîte blanche, papier A après la stéganographie.
- Source : GO-2026-11-22-19 (l. 706), -20 (l. 707), -24 point 2 (l. 711), -40 (l. 727).
- État : retenu ; « lemme et théorème : on les garde mentionnés » ; erratum interne et programme v3 accordés.
- Liens : lemme d'additivité, loi de la référence honnête.
- Ce qui l'attaque : la lecture sur PDF de la stéganographie (R-4767).
- Inventaire : nouveau.

#### [GO-44] Le lemme d'additivité et Avenhaus et Jaech (1981)
- Définition : lemme selon lequel des preuves s'additionnent ; restreint à sa forme valide à tout instant sur scores de sondes ; la citation d'Avenhaus et Jaech (1981) est obligatoire.
- Synonymes et paraphrases : D-4 du mécanisme adjudant, lemme du papier A.
- Source : GO-2026-11-21-46 (l. 645), -47 point 4 (l. 646), -51 point 4 (l. 650), GO-2026-11-22-24 (l. 711), -42 (l. 729).
- État : revendiqué seulement dans sa forme restreinte, puis retiré comme résultat et cité ; mot de Lazar : « il est à nous dans son application au contrôle de l'IA ».
- Liens : thèse du papier A.
- Ce qui l'attaque : occupé (1981, comptabilité des matières).
- Inventaire : nouveau.

#### [GO-45] Les revendications du 22 novembre
- Définition : la méthode d'audit est empruntée et citée ; la mesure « audits économisés » est secondaire au papier A, sa prévision scellée avant G1 ; loi de la référence et attestation du tirage promues seulement après l'essai jumeau contre jumeau ; six graines lues sur PDF avant toute nouveauté ; surplus de capacité et trois planchers en limites déclarées.
- Synonymes et paraphrases : réponse 2, « qelles seraient nos revendications indites alors ? », revendications inédites.
- Source : GO-2026-11-22-09 (l. 696), -12 point 1 (l. 699).
- État : retenu ; question renvoyée au protocole X.
- Liens : papier A, plancher d'audit, note des revendications (GO-2026-11-22-50).
- Ce qui l'attaque : occupation de la littérature.
- Inventaire : nouveau.

#### [GO-46] « Mieux que la boîte noire sur le sabotage diffus »
- Définition : la phrase est un résultat conditionnel de G1 ; la complémentarité avec un contrôle « seconde boîte noire » et le résidu font une analyse secondaire scellée avant G1.
- Synonymes et paraphrases : réponse 8, « ca ne peut pas devenir une these ? », seconde boîte noire.
- Source : GO-2026-11-22-18 (l. 705), -20 (l. 707).
- État : retenu en conditionnel.
- Liens : pince, étau, G1.
- Ce qui l'attaque : —
- Inventaire : 2.20.

#### [GO-47] La marge asymétrique retirée (H6)
- Définition : H6 sort des hypothèses revendiquées : contre un saboteur qui répond au mieux, aucune intervention ne garde de marge. La mesure reste, descriptive.
- Synonymes et paraphrases : N-077, marge asymétrique, taxe de déplacement.
- Source : GO-2026-11-21-64 (l. 663), -57 (l. 656), -61 (l. 660).
- État : retiré des revendications, mesure gardée. Mot : « go; c'etait quoi deja la marge asymetrique ? ».
- Liens : papier A, attaquant informé.
- Ce qui l'attaque : l'attaquant qui connaît le protocole.
- Inventaire : nouveau.

#### [GO-48] La diversité effective de H5
- Définition : redéfinition de la « diversité effective » de H5 ; modification de revendication passée au protocole X (collisionneur et Neon).
- Synonymes et paraphrases : H5.
- Source : GO-2026-11-21-55 (l. 654), -57 (l. 656).
- État : ouvert.
- Liens : papier B.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [GO-49] La flagornerie comme levier de corruption
- Définition : exploiter la flagornerie d'un agent ou d'un moniteur pour le corrompre ; famille de charges, H8 seule hypothèse neuve au papier C, réponse vérifiable seulement, extraction testée comme bras, lecture « je cède » exploratoire.
- Synonymes et paraphrases : réponse 6, sycophancy, « je cède ».
- Source : GO-2026-11-22-12 point 6 (l. 699), -13 (l. 700), -20 (l. 707).
- État : retenu (H8 proposée au papier C).
- Liens : coercition et corruption, papier C.
- Ce qui l'attaque : antériorité à vérifier.
- Inventaire : nouveau.

#### [GO-50] La coercition et la corruption des agents et des moniteurs
- Définition : plan de pilote E0 et E1, puis modes de A, B, C par additifs ; auditeur assaini avec plants porteurs de charge et sous-échantillon humain ; deux bras pour l'attaquant optimisé contre les scores ; contagion en analyse secondaire de B.
- Synonymes et paraphrases : réponse 1, coercition, corruption des moniteurs.
- Source : GO-2026-11-22-09 (l. 696), -10 (l. 697), -12 point 2 (l. 699).
- État : retenu.
- Liens : papiers A, B, C.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [GO-51] Les fausses alertes sur honnêtes imparfaits
- Définition : traitement des agents honnêtes mais imparfaits qui déclenchent des alertes ; six décisions de Fable accordées.
- Synonymes et paraphrases : réponse 3.
- Source : GO-2026-11-22-09 (l. 696), -12 point 3 (l. 699).
- État : retenu.
- Liens : trois honnêtes de contrôle.
- Ce qui l'attaque : —
- Inventaire : 2.19.

#### [GO-52] Les cinq pistes de lecture de la réponse 5
- Définition : base lexicale et tâche de contrôle pour toute sonde avant G1 ; rétro-analyse des journaux des collisionneurs ; « savoir interne contre sortie » enregistré passivement sur l'essai jumeau contre jumeau ; échelle a priori des dommages plantés ; test garder ou retirer les directions de sonde ; banc d'attaque par édition de poids permis en principe, hors G1.
- Synonymes et paraphrases : réponse 5, « les cinq pistes de Fable ».
- Source : GO-2026-11-22-11 (l. 698), -20 (l. 707), -21 (l. 708).
- État : retenu.
- Liens : canal des poids, G1.
- Ce qui l'attaque : —
- Inventaire : 1.4, 1.19.

#### [GO-53] Les tâches de sabotage dont on peut mesurer la réussite
- Définition : affiner et concevoir des tâches de sabotage dont la réussite se mesure par programme ; propriété fixée d'avance par un tiers, vérifiée par programme, avec repli.
- Synonymes et paraphrases : réponse 12, « priorité vers la conception du produit ».
- Source : GO-2026-11-21-69 (l. 668), GO-2026-11-22-22 (l. 709), -24 (l. 711).
- État : retenu, inscrit au programme.
- Liens : tâches floues, bilan matière.
- Ce qui l'attaque : beaucoup de tâches n'admettent pas une telle propriété (premier geste : compter la part qui l'admet).
- Inventaire : nouveau.

#### [GO-54] Les tâches floues et « Diffuse AI Control on Fuzzy Tasks »
- Définition : plan des tâches floues sur dix mondes plantés ; rang de la conclusion parmi K du jumeau ; auditer des actes plutôt que des issues ; question : changer de programme ou contre-attaquer.
- Synonymes et paraphrases : tâches floues, sondes sur tâches floues.
- Source : GO-2026-11-21-57 (l. 656), -61 (l. 660), -66 (l. 665).
- État : retenu (étape 0), étape 1 sur devis.
- Liens : jumeau honnête, entretien du 1er décembre.
- Ce qui l'attaque : le jugement de cette source contre la surveillance.
- Inventaire : nouveau.

#### [GO-55] L'équipe rouge d'une autre famille
- Définition : équipe rouge d'une autre famille définie par cinq propriétés ; organismes en base et témoin ; attaquant informé interne en majorant descriptif ; un tiers après gel pour toute revendication.
- Synonymes et paraphrases : réponse 19.
- Source : GO-2026-11-22-34 (l. 721).
- État : retenu.
- Liens : attaquant informé, famille tenue à l'écart.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [GO-56] La famille tenue à l'écart écrite par un tiers
- Définition : la famille d'attaque tenue à l'écart de la conception des moniteurs est écrite par un tiers d'une autre lignée, la session du bras d'attaque, en quarantaine, qui ne lit jamais les règles ; une famille aveugle de réserve pour le cycle 2 est écrite par un Fable neuf.
- Synonymes et paraphrases : D-3, famille aveugle, mode tenu à l'écart.
- Source : GO-2026-11-21-06 (l. 605), -10 (l. 609), -46 (l. 645), -51 point 3 (l. 650), -65 (l. 664), -67 (l. 666).
- État : retenu.
- Liens : G1, N-054, N-062.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [GO-57] Le banc fermé de l'attaquant informé
- Définition : banc où l'attaquant agit sur épisodes dérivés : revue externe mise de côté jusqu'à publication, remplacée par six garde-fous internes et un vérificateur interne Opus neuf ; oracle hors gabarit par repli interne ; second juge non lancé ; répétition générale sur un mode connu avant la famille aveugle.
- Synonymes et paraphrases : coffre, épisodes dérivés, pièce de sécurité v8.
- Source : GO-2026-11-21-68 (l. 667), -71 (l. 670), -72 (l. 671), -75 (l. 674), -76 (l. 675), -78 (l. 677), -80 (l. 679), -85 (l. 684).
- État : retenu, écarts déclarés à R-611 et N-057 point 4. Mot : « on met de cote la revie externe jusqu a publication du papier ».
- Liens : attaquant informé, configuration du calage de G1.
- Ce qui l'attaque : lignée Claude du vérificateur.
- Inventaire : nouveau.

#### [GO-58] La configuration du calage de G1
- Définition : configuration de génération du calage de G1 écrite par Fable, scellée avant la course du banc fermé ; la course porte une réserve écrite sur la comparabilité.
- Synonymes et paraphrases : « go configuration du calage », nœud 10.
- Source : GO-2026-11-21-77 (l. 676), -78 (l. 677).
- État : retenu.
- Liens : banc fermé, G1.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [GO-59] Le signal bruité pour entraîner et « lit le handicap »
- Définition : deux questions confiées à Fable (et Opus) : entraîner sur un signal bruité et savoir si une sonde lit un handicap plutôt qu'une intention.
- Synonymes et paraphrases : « signal bruité », « lit le handicap ».
- Source : GO-2026-11-21-68 (l. 667), -69 (l. 668).
- État : ouvert ; le signal bruité passe par l'oracle ou par le mot de Lazar.
- Liens : contrôle actif fermé.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [GO-60] Les autres questions de recherche du protocole X
- Définition : liste : H6 et l'attaquant qui connaît le protocole ; l'attaquant visant ce que l'oracle ne voit pas ; l'agent qui choisit ses représentations ; le dommage sans masse ; les quatre verrous de la sonde « dopamine » ; le canal des poids et la programmation de poids ; estimation de la part des attaques jamais vues (Li et al.) ; sondes aveuglées par dérive d'entraînement ordinaire (Taufeeque et al.).
- Synonymes et paraphrases : M3, canal des poids, « percée du programme ».
- Source : GO-2026-11-21-51 point 9 (l. 650), -57 (l. 656), -60 (l. 659), -61 (l. 660), -66 (l. 665).
- État : ouvert.
- Liens : percée du programme.
- Ce qui l'attaque : —
- Inventaire : 1.19, 1.13.

#### [GO-61] La percée du programme
- Définition : question « que reste-t-il, où est la percée », posée parce que le plancher d'audit est occupé ; revue par Fable et Opus en effort maximal chacun sans lire l'autre, puis le collisionneur et l'organisme.
- Synonymes et paraphrases : « il faut une percee pour notre programme », « il faut revoir la percée ».
- Source : GO-2026-11-21-39 (l. 638), -50 (l. 649), -60 (l. 659), -66 (l. 665), -68 (l. 667).
- État : ouvert.
- Liens : plancher d'audit occupé.
- Ce qui l'attaque : —
- Inventaire : nouveau.

---


**D. Mathématiques nouvelles et chantier Lean**


#### [GO-62] Le pilier des mathématiques nouvelles pour l'attaque et la défense
- Définition : pilier rouvert « à fond » : génération, arbitre formel Lean, juge de nouveauté, tests de mort. Côté attaque, Lazar veut des modes de sabotage concrets, mais l'option retenue reste le niveau de l'idée.
- Synonymes et paraphrases : « nouvelles mathematiques », « je veux avancer a fond », D-B1 à D-B6.
- Source : GO-2026-11-21-12 (l. 611), -17 (l. 616), -18 (l. 617), -21 (l. 620), -23 (l. 622), -31 (l. 630), -38 (l. 637), GO-2026-11-22-40 (l. 727), -42 (l. 729).
- État : retenu.
- Liens : modes de sabotage concrets, statisticien Mines Paris.
- Ce qui l'attaque : antériorité ; annonces publiques non vérifiées.
- Inventaire : nouveau.

#### [GO-63] Les modes de sabotage concrets, au niveau de l'idée
- Définition : modes conçus en quarantaine, versés comme matière première à la course « nouvelles attaques » ; option finale : rester au niveau de l'idée, aucun catalogue opérationnel.
- Synonymes et paraphrases : « je veux des modes de sabotage et des exemples cocrets », stéganographie comme modèle.
- Source : GO-2026-11-21-17 (l. 616), -19 (l. 618), -21 (l. 620), GO-2026-11-22-34 (l. 721).
- État : retenu en idée seulement.
- Liens : course « nouvelles attaques ».
- Ce qui l'attaque : risque d'usage dual.
- Inventaire : nouveau.

#### [GO-64] Le chantier Lean : « on ne s'arrête pas à l'échec »
- Définition : l'outillage Lean est corrigé selon ses causes avant tout nouvel essai, en versions neuves.
- Synonymes et paraphrases : D-1a, « on ne s'arrete pas a un echec ».
- Source : GO-2026-11-21-36 point 7 (l. 635), -40 (l. 639), GO-2026-11-22-38 (l. 725), -42 (l. 729).
- État : retenu.
- Liens : règle « moniteur invalide ».
- Ce qui l'attaque : isolement Lean non éprouvé.
- Inventaire : nouveau.

---


**E. Organisme d'idéation et collisionneur**


#### [GO-65] L'essaim qui communique
- Définition : trois configurations au même coût jugées par le monde planté et le coût, jamais par le juge.
- Synonymes et paraphrases : « ai society vs isoles », pilote P-std.
- Source : GO-2026-11-22-12 point 4 (l. 699), -15 (l. 702), -17 (l. 704), -24 (l. 711), -26 (l. 713), -28 (l. 715).
- État : retenu, pilote accordé. Mot : « il faut réduire drastiquement les coûts ».
- Liens : organisme v9, N-058.
- Ce qui l'attaque : coût.
- Inventaire : nouveau.

#### [GO-66] Les idées originales en puits étroits
- Définition : demande « vitale » sur la manière optimale de faire produire à l'organisme des idées originales.
- Synonymes et paraphrases : demande 28.
- Source : GO-2026-11-22-42 (l. 729), -47 (l. 734).
- État : ouvert.
- Liens : organisme d'idéation.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [GO-67] La passe X de la course « nouvelles attaques »
- Définition : question fusionnée servie à l'organisme, liste rallongée à toutes les questions.
- Synonymes et paraphrases : option d.
- Source : GO-2026-11-22-42 (l. 729), -46 (l. 733), -48 (l. 735).
- État : retenu.
- Liens : course « nouvelles attaques ».
- Ce qui l'attaque : question orientée.
- Inventaire : nouveau.

#### [GO-68] La course « seuil et moniteurs », réduite à l'étage des tests de mort
- Définition : course de l'organisme réduite (option b) au seul étage des tests de mort, jouée sur les propositions déjà rendues (collisionneur, Fable, Argon, Carbon, moniteur de dissonance) et sans proposeurs. Les mondes plantés viennent d'un auteur séparé ; si l'expérimentateur nommé appartient à sa lignée, ces mondes sont gardés et non employés.
- Synonymes et paraphrases : option (b), course « seuil et moniteurs », mondes plantés de la course.
- Source : GO-2026-11-21-16 (l. 615), -29 (l. 628), -37 (l. 636).
- État : retenu, sur devis.
- Liens : tests de mort, dérive de régime.
- Ce qui l'attaque : un auteur et un juge de même lignée.
- Inventaire : nouveau.

#### [GO-69] La colonne « matière première » du véhicule
- Définition : colonne qui compare les idées produites par la course « nouvelles attaques » avec une matière première tenue à l'écart des proposeurs. On l'allume après la clôture des trois générations, sur un mot de Lazar qui nomme l'interrupteur.
- Synonymes et paraphrases : point 6 de l'arbitre, état 2, interrupteur.
- Source : GO-2026-11-21-36 (l. 635), -41 (l. 640).
- État : retenu (option a de l'arbitre), additif scellé avant lecture.
- Liens : modes de sabotage concrets, N-072.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [GO-70] Les six points délicats tranchés par l'arbitre Fable
- Définition : six points tranchés par l'arbitre. Un préenregistrement unique de la porte commune du barreau 1, avec un engagement par carte. La borne de 92 cartes tient lieu de compte. En course, l'arrêt n° 1 arrête l'appel seul. L'outillage Lean n'est pas déclaré conforme. Le seuil des témoins reste hors de la liste scellée.
- Synonymes et paraphrases : N3, D8, arbitrages des points délicats.
- Source : GO-2026-11-21-36 (l. 635).
- État : retenu.
- Liens : gouvernance par autonomie.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [GO-71] Les billets : engagement horodaté et table des revendications
- Définition : un tiers horodate l'engagement des billets tout de suite. Les prévisions sont publiées en empreinte, les conditions sont fixées avant la parution, et la table des revendications passe d'abord. Un protocole X porte sur les billets suivants et sur la révision des billets « contrôle IA » et « Raisons ou regard ».
- Synonymes et paraphrases : réponse 26, « Raisons ou regard ? », billet drapeau, billet sur les sondes.
- Source : GO-2026-11-21-64 (l. 663), GO-2026-11-22-40 (l. 727), -42 (l. 729).
- État : retenu. Mot : « au plus vite et avant l'entretien, capital ».
- Liens : entretien du 1er décembre, note des revendications.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [GO-72] La mesure du modèle nul chez de vrais agents
- Définition : mesurer chez de vrais agents le modèle nul hérité, celui que la thèse du papier A cite.
- Synonymes et paraphrases : modèle nul, loi héritée.
- Source : GO-2026-11-22-42 (l. 729).
- État : retenu (« go »).
- Liens : thèse du papier A, loi de la référence honnête.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [GO-73] L'expérience 7 nulle du billet « Sparks » relancée par un texte neuf
- Définition : l'expérience nulle du second ordre du billet « Sparks » revit par un préenregistrement neuf. Un état des lieux de ce qui a été fait passe d'abord, et l'ancien accord reste périmé.
- Synonymes et paraphrases : SPARKS-EXP7-NUL.
- Source : GO-2026-11-21-79 (l. 678).
- État : retenu, dépense sur devis neuf.
- Liens : billets.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [GO-74] Le chantier d'affinage des hypothèses des mentors, relancé
- Définition : le chantier qui affine les idées des mentors, versées comme matière première, est relancé alors qu'il était gelé.
- Synonymes et paraphrases : affinage mentors, N-072.
- Source : GO-2026-11-21-62 (l. 661), -63 (l. 662).
- État : retenu.
- Liens : organisme d'idéation.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [GO-75] La session bibliothécaire et la note des revendications
- Définition : session fille de la mère qui tient une note de mémoire de la conception, interrogeable par la mère et par Lazar. Une nouvelle note des revendications sert les thèses des papiers et des billets. Opus 5.5 en effort maximal entre au collisionneur et à l'organisme, et un essai donne l'alerte en amont quand une clé manque de crédit.
- Synonymes et paraphrases : bibliothécaire.
- Source : GO-2026-11-22-50 (l. 737).
- État : retenu.
- Liens : cette note.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [GO-76] Le saboteur à budget et le bras A menés en parallèle
- Définition : les deux chantiers avancent en parallèle, et le premier qui aboutit avec succès est choisi pour l'entretien. Au saboteur, la première action se fait dans la perte de distillation « gardée », et le rappel au flagrant change à chaque pas.
- Synonymes et paraphrases : « turbo max, le premier qui arrive est choisi s'il réussit ».
- Source : GO-2026-11-21-70 (l. 669), -84 (l. 683), GO-2026-11-22-42 (l. 729).
- État : retenu.
- Liens : saboteur et sondes pour l'entretien, bras A.
- Ce qui l'attaque : —
- Inventaire : nouveau.

---


### 2.4 Registre des décisions, 21 novembre (`RD21`)


> - Fichier lu : `registres/decisions.md`, empreinte `75f4ab9603eba780` (sha256 entier 75f4ab9603eba780d69fa029670556491cc9b433574521c050aad8aab3c5050a), lignes 4478 à 4888 (R-4340 à R-4749). Les lignes antérieures qui citent seulement la date du 21 (2942, 4179, 4225…, 4460) et celles du 22 (4940 et suivantes) ne sont pas des entrées du 21 : non retenues.
> - Ligne R-2059 (l. 2017) sautée. Aucun score ni table du barreau 5, aucun résultat de 7a, 7b, T0.6, étape B, étape B bis, P3-bis recopié.
> - Source abrégée ci-dessous : « l. N, R-xxxx » ; empreinte toujours `75f4ab9603eba780`.
> - Rattachement à l'inventaire `docs/notes/seconds-regards-sabotage-inventaire-v1/inventaire-seconds-regards-invariants-noyaux-v1.md` (titres seulement lus).

> ---


**A. Méthode de travail et règles nées le 21**


#### [RD21-01] Demande approfondie et protocole X
- Définition : manière de traiter une demande de Lazar : un expert dirait d'abord ce qu'il ferait sans qu'on le demande, quelles données brutes il prendrait, quels outils, et ce qui hors de Lazar et de Claude vérifierait le résultat ; puis la demande est reformulée et traitée. Le protocole X enchaîne cette demande approfondie chez Fable, puis le collisionneur sur une question neutre écrite par Fable, puis l'organisme d'idéation.
- Synonymes et paraphrases : « demande approfondie », « protocole X », « Fable max puis collisionneur puis organisme », méthodes nommées par Lazar.
- Source : l. 4685, R-4547 (GO-2026-11-21-57) ; dix questions passées au protocole X ; cinq lancés l. 4722, R-4584.
- État : retenu, écrit dans CLAUDE.md (GO-2026-11-21-57).
- Liens : toutes les notes de conception du jour (marge asymétrique, Diffuse AI Control, boucle audit-recapture, programmation de poids, dommages plantés, dommage et tâches floues, attaquant et convergence).
- Ce qui l'attaque : coût en quota de Fable (limite atteinte deux fois le 21) ; neutralité de la question au collisionneur à garantir (couples « v2 neutres » seuls servis).
- Inventaire : nouveau.

#### [RD21-02] Chaîne d'arbitrage d'un point délicat
- Définition : un point délicat passe d'abord par Fable en effort normal ou élevé, puis Fable en effort maximal s'il ne tranche pas, puis le collisionneur, puis Lazar. L'effort maximal est réservé aux questions qui demandent les solutions les plus originales.
- Synonymes et paraphrases : « Fable max seulement pour le plus délicat », « points délicats », « go recos » avec arbitrage.
- Source : l. 4653, R-4515 ; lecture des « points délicats » l. 4643, R-4505 (tout écart à un texte scellé, hypothèse ou revendication, cloisonnement, dépense sans devis contre-lu ; contact, publication, paiement, porte restent à Lazar).
- État : retenu (mots de Lazar, GO-2026-11-21-27).
- Liens : économie de Fable ; « go recos ».
- Ce qui l'attaque : limite d'usage de Fable (l. 4650, 4797, 4841).
- Inventaire : nouveau.

#### [RD21-03] Mode exploratoire partout où rien n'est scellé
- Définition : là où aucun texte n'est encore scellé, on travaille en mode exploratoire, sorties marquées non opposables, sans verdict ni porte, et le préenregistrement vient à la fin ; les textes scellés et leurs courses ne sont pas touchés. Les règles R5, R9, R10, R12, le cloisonnement et l'accord sur devis restent.
- Synonymes et paraphrases : « exploratoire », « préenregistrement à la fin », « papier dopamine rouvert en exploratoire ».
- Source : l. 4662, R-4524 (GO-2026-11-21-44) ; l. 4667, R-4529 (GO-2026-11-21-45).
- État : retenu.
- Liens : papier « dopamine », R1.
- Ce qui l'attaque : tension avec R1 (tenue par la seule marque « exploratoire »).
- Inventaire : nouveau.

#### [RD21-04] Consigne commune de méthode de recherche
- Définition : texte de sept consignes et une table des modes d'échec, à coller dans tout mandat de concepteur, relecteur et expérimentateur, vérifié par la mère.
- Synonymes et paraphrases : « méthode commune à tous les chantiers », consigne commune.
- Source : l. 4660, R-4522 (`docs/procedures/consigne-commune-methode-de-recherche-v1.md`, d327b3fc…) ; GO-2026-11-21-38 (l. 4658, R-4520).
- État : retenu, en vigueur pour les mandats suivants.
- Liens : expérimentateurs et tests de mort.
- Ce qui l'attaque : rien de consigné.
- Inventaire : nouveau.

#### [RD21-05] Expérimentateurs et tests de mort
- Définition : chaque proposition d'idée doit affronter un « test de mort » exécuté dans un bac sur un monde planté scellé d'avance. Conception de Fable : aucun agent n'écrit le critère de mort, l'expérimentateur implémente sous interface scellée, le noyau mesure contre une vérité plantée que nul agent ne voit, témoins plantés d'abord, un mort reste mort ; un énoncé mathématique meurt par contre-exemple exact ou par l'arbitre formel.
- Synonymes et paraphrases : « brancher les expérimentateurs et les tests de mort », bac, banc d'étalonnage, banc joueur et banc noteur, socle commun et sommet d'étage, course appariée avec et sans le mécanisme.
- Source : l. 4507-4508, R-4369, R-4372 ; l. 4559-4560, R-4421, R-4422 ; errata l. 4577 (R-4439 : banc coupé en deux, contre-calcul sans greffon) et l. 4583 (R-4445 : socle commun écrit une fois, un sommet et un lanceur par emploi).
- État : retenu ; priorité sur la course principale d'auto-conception et les mathématiques nouvelles (GO-2026-11-21-16, l. 4524, R-4386) ; nœuds N1 à N7 à Lazar ; expérimentateur Sonnet 5.5 (GO-2026-11-21-47, l. 4671, R-4533).
- Liens : organisme d'idéation, course « seuil et moniteurs », pilier mathématique.
- Ce qui l'attaque : constat « rien n'est branché en général » (14 tests réels une seule fois) ; « une carte propose un mécanisme, pas une loi sur des données » : l'étage refuserait chaque fiche (l. 4532, R-4394) ; coût d'un greffon non mesuré.
- Inventaire : nouveau.

#### [RD21-06] Lancement détaché des courses longues
- Définition : toute course longue est lancée détachée de l'outil (setsid, nohup), avec journal et identifiant de processus écrit, parce que l'outil coupe les tâches de fond à deux heures.
- Synonymes et paraphrases : « limite de deux heures », « [killed] ».
- Source : l. 4593, R-4455 ; l. 4592, R-4454.
- État : retenu (règle de la mère).
- Liens : palier 0b, étage 2 de la ligne 3.
- Ce qui l'attaque : redémarrage de conteneur qui tue quand même la course (l. 4663, R-4525).
- Inventaire : nouveau.

#### [RD21-07] Garde des appels aux modèles de Google
- Définition : avant tout envoi à un modèle de Google, une vérification par code refuse si le réglage de réflexion n'est pas explicite ou si le plafond de sortie ne laisse pas 16 000 jetons de texte ; après réponse, zéro jeton de pensée, fin en MAX_TOKENS, SAFETY ou RECITATION, ou texte vide = défaut journalisé. Garde commune `src/controle_ia/garde_google_v1.py`.
- Synonymes et paraphrases : « plafond large pour Carbon », thinkingLevel, « Argon sans réflexion », règle GO-71.
- Source : l. 4671, R-4533 (règle Carbon) ; l. 4783, R-4644 (Argon zéro jeton de pensée sur 22 réponses) ; l. 4803, R-4664 ; l. 4827, R-4688 (essai réel : les trois modèles réfléchissent ; premier essai refusé par la garde).
- État : retenu (GO-2026-11-21-47, -71).
- Liens : collisionneur v8 à v8d.
- Ce qui l'attaque : audit du dépôt : aucune dernière version en service conforme (l. 4794, R-4655).
- Inventaire : nouveau.

#### [RD21-08] Relecture par Fable appelé par l'interface de programmation
- Définition : quand la limite d'usage de Fable est atteinte, les corrections sont faites par Opus en effort maximal à la lettre des remarques, puis relues par Fable 5.2 appelé par l'API avec les clés d'Anthropic, puis scellées.
- Synonymes et paraphrases : « option (b) de la limite de Fable », « Fable via l'API », outil de relecture v3, effort « high ».
- Source : l. 4841, R-4702 ; l. 4856, R-4717 ; l. 4877, R-4738 (réflexion = toute la sortie, défaut) ; l. 4879, R-4740 (effort « high » par défaut).
- État : retenu.
- Liens : règle « Qui conçoit », économie de Fable.
- Ce qui l'attaque : refus de la garde et du classifieur sur des copies « maquillées » (l. 4876, R-4737) ; défauts en effort maximal (sortie toute en réflexion).
- Inventaire : nouveau.

#### [RD21-09] Non-contournement d'un refus de classifieur
- Définition : un refus d'un classifieur de sûreté ou du contrôle des permissions n'est jamais contourné, ni par l'agent ni par la mère, ni en portant la demande à des fournisseurs externes ; le point va à Lazar.
- Synonymes et paraphrases : « Undermining Oversight », « Unauthorized Access », « la mère ne contourne pas ».
- Source : l. 4499, R-4361 ; l. 4536, R-4398 ; l. 4542, R-4404 (refus d'exécuter « demande des modes concrets aux trois modèles ») ; l. 4742, R-4603 (découpage refusé) ; l. 4753, R-4614 ; l. 4775, R-4636.
- État : retenu.
- Liens : modes de sabotage concrets, organisme.
- Ce qui l'attaque : mot de Lazar contraire (R-4404), non exécuté.
- Inventaire : nouveau.

---


**B. Seuil, moniteurs et papier « dopamine »**


#### [RD21-10] Papier « dopamine » : moniteur de réussite attendue et de surprise
- Définition : bras qui apprend sur des épisodes honnêtes la réussite attendue et la surprise par étape dans les états internes de l'agent, et sonne quand la trajectoire s'en écarte. Le 21 : préenregistrement court v4 à v7, 1 % seul, mode tenu à l'écart lu, couches publiques, évasion fermée.
- Synonymes et paraphrases : « dopamine », signal de dopamine, sonde de réussite attendue, P1, P2, H-D, lot honnête neuf, étapes 0, 1, 2a.
- Source : l. 4483, R-4345 (GO-2026-11-21-06) ; l. 4490, R-4352 ; l. 4493, R-4355 ; l. 4516, R-4378 ; l. 4528, R-4390 ; l. 4662, R-4524 ; l. 4672, R-4534 ; l. 4779, R-4640.
- État : rouvert en mode exploratoire (GO-2026-11-21-44) ; v8 attendait le mot de Lazar.
- Liens : papier A, inventaire 1.1, moniteur de dissonance.
- Ce qui l'attaque : Lin et al., « When Lie Detectors Learn Model Identity », publie en boîte noire la forme de P2 et la conclusion de H-D (écrit dans « non revendiqué ») ; risque de P2 à 10 % et non 5 % ; aucun lot gratuit n'étalonne P1 et P2 ; aucun état interne des couches 7, 15, 23 n'existe pour les honnêtes ; la garde « taux d'alerte entre deux lots honnêtes » sonne à tort trop souvent ; « manipulable seulement avec un signal qui enseigne » (note attaquant).
- Inventaire : 1.1.

#### [RD21-11] Barre de 5 000 par tranche : précision, non validité
- Définition : la barre de 5 000 épisodes par tranche n'est ni nécessaire ni suffisante pour un seuil d'alerte à 1 % : c'est une barre de précision ; une garantie de validité demande quelques centaines d'épisodes selon la forme voulue. Seules les comparaisons « bat telle base » exigent un lot neuf ; on compte des familles, pas des épisodes.
- Synonymes et paraphrases : « seuil à 1 % », « seuil certifié », « 299 épisodes », seuil séquentiel relevé à 1/(α·p_min), horizon assigné, « usage du papier dopamine : un aiguillage ».
- Source : l. 4509, R-4371 (approfondissement Fable, Argon, Carbon ; GO-2026-11-21-13) ; l. 4567, R-4429 (synthèse du collisionneur).
- État : retenu comme lecture ; cinq décisions de la synthèse prises selon les recommandations (GO-2026-11-21-25).
- Liens : course « seuil et moniteurs », papier « dopamine ».
- Ce qui l'attaque : conditionner sur l'échec final gonfle le taux jusqu'à α/P(échec), ce qui nuance le moniteur de dissonance ; un contrôle actif par sélection sur un score de sonde contredit N-053 point 5 (aucun score de moniteur dans l'entraînement).
- Inventaire : nouveau.

#### [RD21-12] Validité d'un nul par rangs
- Définition : la validité d'un nul fondé sur les rangs se vérifie par les fréquences de franchissement du seuil sur des honnêtes. Proposé par la synthèse du collisionneur.
- Synonymes et paraphrases : nul par rangs, fréquence de franchissement.
- Source : l. 4567, R-4429.
- État : proposé, pris sous GO-2026-11-21-25.
- Liens : moniteur de dissonance, règle « moniteur invalide ».
- Ce qui l'attaque : rien de consigné.
- Inventaire : nouveau (proche 2.2).

#### [RD21-13] Dérive de régime du seuil
- Définition : défaut d'un seuil réglé à 1 % dont le taux réel de fausses alertes triple quand le régime des épisodes change. Correction confiée à Fable en effort maximal et au collisionneur ; l'unité des décalages du saboteur est l'écart type de la loi honnête de la tranche, sous condition d'un contrôle par l'aire écrit avant lecture.
- Synonymes et paraphrases : « dérive de régime », « changement de régime », « unité des décalages », dérive de F, « le décalage doit tripler le taux à 1 % ».
- Source : l. 4634, R-4496 ; l. 4640, R-4502 (GO-2026-11-21-26) ; l. 4647, R-4509 (arbitrage de l'unité) ; l. 4651, R-4513 (note versée) ; l. 4631, R-4493.
- État : note versée ; collisionneur relancé et fini (l. 4880, R-4741).
- Liens : course « seuil et moniteurs » (monde à changement de régime), inventaire 1.14.
- Ce qui l'attaque : contrôle de la dérive de F fait par personne tant que le programme de vérité v2 n'est pas joué (l. 4654, R-4516).
- Inventaire : 1.14 (voisin).

#### [RD21-14] Course « seuil et moniteurs » de l'organisme d'idéation
- Définition : course de l'organisme qui fait passer des propositions de seuils et de moniteurs par l'étage des tests de mort sur des mondes plantés à vérité exacte. Option (b) : l'étage de tests de mort seul ; cinq propositions passent en premier : moniteur de dissonance, budget d'audit réparti, seuil certifié et bande, seuil unique normalisé, aiguillage rétrospectif.
- Synonymes et paraphrases : D-M1 à D-M18, « option (b) », candidates du collisionneur, mise en fiches à forme fixe par deux traducteurs de deux lignées, extrait vérifié à l'octet, champ portee_de_la_garantie, quatorze sources scellées.
- Source : l. 4515, R-4377 ; l. 4524, R-4386 ; l. 4527, R-4389 ; l. 4537, R-4399 ; l. 4550, R-4412 ; l. 4563, R-4425 ; l. 4570, R-4432 ; l. 4581, R-4443.
- État : conception v6 « prête à sceller » (scellement après N5 et N6) ; ligne de 4,30 USD de l'auteur des mondes (GO-2026-11-21-37, conditionnelle).
- Liens : expérimentateurs et tests de mort, organisme d'idéation, papier C.
- Ce qui l'attaque : défauts de la v1 : « sans gain » doit se lire par puissance comparée sur les mêmes tirages ; « invalide » sur le taux vrai conditionnel ; arrêt si fiches non scellées avant le tirage.
- Inventaire : nouveau.

#### [RD21-15] Mondes plantés à vérité exacte et programme de vérité des témoins
- Définition : quatre mondes dont la vérité est connue exactement (queue connue, changement de régime, grappes par famille, déploiement) plus des familles libres de l'auteur, écrits par un auteur de la troisième lignée sans critère de mort ni vérité sur la machine jetable. Un programme indépendant calcule la vérité de dix-sept témoins, gardée sur une branche à part lue par la mère (banc noteur) et les juges de fin.
- Synonymes et paraphrases : mandat de l'auteur des mondes plantés, témoins plantés, T01 à T17, indecise_a_la_borne, « famille F écartée », monde à trois populations, verite-temoins.
- Source : l. 4570-4571, R-4432, R-4433 ; l. 4589, R-4451 ; l. 4615, R-4477 ; l. 4624, R-4486 ; l. 4654, R-4516.
- État : mandat et pièces scellés.
- Liens : course « seuil et moniteurs », dérive de régime.
- Ce qui l'attaque : contradiction du mandat sur le nombre de témoins (lecture de la mère retirée, l. 4613, R-4475) ; contrainte de taille de la lecture (52 000 caractères).
- Inventaire : nouveau.

#### [RD21-16] Liste réelle des motifs refusés
- Définition : donnée de garde qui réunit les noms que les programmes de contrôle refusent de voir passer (et le motif de valeur de clé), versée seule et jamais servie aux proposeurs.
- Synonymes et paraphrases : motifs refusés, garde de motifs, 34 noms.
- Source : l. 4607, R-4469 ; l. 4612, R-4474 ; l. 4638, R-4500 (refus de classifieur sur une copie de la liste).
- État : retenu, scellé (MOTIFS-REFUSES-SEUIL-MONITEURS-V1).
- Liens : cloisonnement, véhicule des nouvelles attaques.
- Ce qui l'attaque : rien.
- Inventaire : nouveau.

#### [RD21-17] Moniteur de dissonance
- Définition : test du rang de l'action de l'agent parmi K actions que le jumeau honnête tire sur le même début, lu par la sonde de réussite attendue. Une action délibérément mauvaise devrait tomber en queue de rang.
- Synonymes et paraphrases : « dissonance », rang de l'action contre le jumeau honnête, moniteur-dissonance-v1.
- Source : l. 4512, R-4374 (GO-2026-11-21-15) ; l. 4520, R-4382.
- État : note de conception versée ; cinq décisions pour Lazar dont un devis ; premier test de mort sur MATH500 public.
- Liens : papier « dopamine », course « seuil et moniteurs », inventaire 1.3.
- Ce qui l'attaque : bornes simulées : aveugle au sabotage très diffus ; nul fragile à l'écart entre honnête et jumeau ; conditionner sur l'échec final gonfle le taux (R-4429) ; jumeau honnête limité quand ses choix légitimes sont dispersés (R-4418).
- Inventaire : 1.3.

#### [RD21-18] Budget d'audit réparti selon la valeur
- Définition : répartition du budget d'audit entre épisodes selon leur valeur ou leur enjeu, au lieu d'un tirage uniforme ; conçu avec le moniteur de dissonance, antériorité comprise.
- Synonymes et paraphrases : audit selon la valeur, audit à l'enjeu, « les scores orientent l'audit ».
- Source : l. 4512, R-4374 ; l. 4550, R-4412.
- État : proposé, passe en premier dans la course « seuil et moniteurs ».
- Liens : plancher d'audit au hasard, audit après coup à plancher et à l'enjeu, N-076.
- Ce qui l'attaque : détecteurs qui orientent l'audit : cœur publié (Zrnic et Candès ; Molnar), l. 4687, R-4549.
- Inventaire : 2.12 (voisin).

---


**C. Assurance contre le saboteur diffus : notes de conception**


#### [RD21-19] Mécanisme adjudant aux sondes pour le hors distribution
- Définition : mécanisme qui accompagne les sondes pour donner une assurance face à un sabotage hors de la distribution d'entraînement. Cadre de Fable : « borner sans reconnaître, mesurer en service, chercher le dilemme » ; cinq mécanismes en tête, manuel de course.
- Synonymes et paraphrases : « adjudant », mécanisme adjudant, D-2 à D-7, réponse indépendante d'Opus, dix mécanismes fusionnés.
- Source : l. 4652, R-4514 (GO-2026-11-21-34) ; l. 4665, R-4527 ; l. 4682, R-4544 ; l. 4690, R-4552 ; l. 4701, R-4563 ; l. 4765-4767, R-4626, R-4628.
- État : retenu comme note (GO-2026-11-21-46), erratum ; prête pour le collisionneur.
- Liens : papier A, N-075, N-076, pince.
- Ce qui l'attaque : antériorité Avenhaus et Jaech 1981 pour l'ossature du lemme d'additivité ; aucun mécanisme ne tient sans condition face à un attaquant informé ; masse manquante occupée (Li et al.) ; le rappel mesuré sur ce que l'oracle capture est biaisé vers le haut si oracle et moniteur partagent leurs angles morts ; la limite 3/m vaut aussi pour l'honnête qui endommage.
- Inventaire : 2.15, 2.2.

#### [RD21-20] Lemme d'additivité, restreint
- Définition : énoncé selon lequel les dommages diffus s'additionnent de sorte qu'un audit finit par les attraper ; restreint au papier A et cité à l'article de 1981.
- Synonymes et paraphrases : lemme d'additivité, « lemme resserré au reste ».
- Source : l. 4671, R-4533 (GO-2026-11-21-47) ; l. 4676, R-4538.
- État : retenu sous forme restreinte, à démontrer.
- Liens : N-075, adjudant, papier A.
- Ce qui l'attaque : Avenhaus et Jaech 1981 (occupé dans son ossature).
- Inventaire : nouveau.

#### [RD21-21] Plancher d'audit au hasard à oracle exogène
- Définition : une part fixe d'épisodes est tirée au hasard et jugée par un oracle extérieur sur le produit, ce qui donne une garantie de prise indépendante des moniteurs.
- Synonymes et paraphrases : « plancher d'audit », audit au hasard, base nommée, « Blindfold ».
- Source : l. 4686, R-4548 (lecture des douze voisins) ; l. 4690, R-4552 ; l. 4676, R-4538.
- État : occupé par la littérature (« Blindfold », 2610.37055 ; Podkopaev et Ramdas ; Gans et Holden) : base nommée et citée, jamais revendiquée, hors critère de porte (N-075).
- Liens : N-075, N-076, adjudant.
- Ce qui l'attaque : la littérature citée ; garantie seulement pour un horizon (R-4552).
- Inventaire : 2.1.

#### [RD21-22] Loi de la référence honnête
- Définition : candidat de tête de la note « percée » : toute accumulation de preuves déclare m, n et la source de sa validité ; l'horizon est borné sauf nul par acte ; une prévision chiffrée doit être scellée avant G1.
- Synonymes et paraphrases : « percée en contrôle et sécurité », candidat C1, N-076, « assurance par audit et référence honnête ».
- Source : l. 4673, R-4535 ; l. 4693, R-4555 (N-076 versée) ; l. 4754, R-4615 (erratum 2) ; l. 4782, R-4643.
- État : retenu en N-076, rien revendiqué ; prévision chiffrée manquante (pièce de classe A absente, R-4643).
- Liens : N-076, G1, papier A.
- Ce qui l'attaque : heurt entre la boucle audit-recapture-réapprentissage et N-060 v3 point 4 ; phrase « un théorème remarqué n'est pas réaliste » retirée.
- Inventaire : nouveau (voisin 2.7).

#### [RD21-23] Pince hors distribution, en trois objets
- Définition : idée que contourner la boîte blanche oblige à passer par la boîte noire, et inversement, de sorte que le saboteur est pris entre les deux mâchoires. La moitié « contourner la blanche oblige à passer par la noire » tient par arithmétique si l'oracle couvre le dommage ; la pince est découpée en trois objets dont seul le bilan se revendique hors distribution.
- Synonymes et paraphrases : « pince », bilan de la pince, mâchoire externe, recapture à deux mâchoires.
- Source : l. 4673, R-4535 ; l. 4674, R-4536 ; l. 4677, R-4539 (GO-2026-11-21-53).
- État : retenu sous forme restreinte (seul le bilan revendiqué).
- Liens : N-075, étau, papier A.
- Ce qui l'attaque : l'étau reste une hypothèse ; dépend de la couverture de l'oracle.
- Inventaire : 2.4.

#### [RD21-24] Étau
- Définition : version « dilemme » de la pince : l'agent ne peut éviter une mâchoire qu'en se jetant dans l'autre. Option (a) échelonnée retenue, plafond par effacement d'abord.
- Synonymes et paraphrases : « étau », D-4, dilemme, chute conjointe.
- Source : l. 4677, R-4539 ; l. 4682, R-4544 ; l. 4691, R-4553 ; l. 4710, R-4572 ; l. 4759, R-4620.
- État : note v2 vérifiée ; troisième bras d'attaque confronté à N-056 (nœud) ; échelon 1 hors de la lignée du saboteur (nœud « Qui conçoit ») ; poids en quarantaine scellée.
- Liens : pince, N-075 (« dilemme, non décorrélation »).
- Ce qui l'attaque : appui de Gupta et Jenner à retirer ; rappel publié des sondes 14B à corriger en erratum.
- Inventaire : 5.5.

#### [RD21-25] Note sur l'attaquant informé
- Définition : la borne inférieure de prise vaut par le dommage lui-même additionné, si le seuil dépasse ce que le taux d'audit laisse passer. Trois propositions : audit après coup à plancher et à l'enjeu ; boucle audit-recapture-réapprentissage où le défenseur joue en dernier ; épreuves du devin.
- Synonymes et paraphrases : attaquant informé, « audit après coup », « défenseur jouant en dernier », « épreuves du devin ».
- Source : l. 4679, R-4541 (GO-2026-11-21-54) ; l. 4702, R-4564 (lecture des treize PDF).
- État : retenu comme note ; versé dans N-076 « à faire ».
- Liens : N-076, boucle audit-recapture, inventaire 2.17.
- Ce qui l'attaque : lecture des PDF : quatre affirmations inexactes (Schaeffer, Westphal, Lucassen, Taufeeque) ; sondes aveuglées par une dérive d'entraînement ordinaire (Taufeeque) ; « Diffuse AI Control on Fuzzy Tasks » à qui répondre.
- Inventaire : 2.17, 2.14.

#### [RD21-26] Trois asymétries de l'attaquant
- Définition : trois avantages de l'attaquant étudiés par Fable : la généralisation de l'évasion, le canal de retour vers l'agent, et les copies qui partagent un point focal commun.
- Synonymes et paraphrases : asymétries, « aucun retour à l'agent » (D-2), point focal.
- Source : l. 4681, R-4543 ; l. 4682, R-4544 ; l. 4693, R-4555.
- État : note versée ; ligne « aucun retour à l'agent » portée à Lazar.
- Liens : papier B (copies), invariant de N-053.
- Ce qui l'attaque : rien de consigné.
- Inventaire : 2.8 (voisin).

#### [RD21-27] Science de la détection et invariants du sabotage
- Définition : invariants candidats déduits de la définition du sabotage : le produit est pire, l'agent le sait, il ne le dit pas. On sépare triche et échec honnête par la trajectoire autour de l'acte, et on compte les suppositions plutôt que les détecteurs.
- Synonymes et paraphrases : définition en trois clauses, neuf invariants candidats, « surprise sous 0,3 évaluable seulement en agrégat », comparaison par paires en aveugle au produit du jumeau.
- Source : l. 4680, R-4542 (GO-2026-11-21-55) ; l. 4687, R-4549.
- État : note versée, erratum 1 ; H5 portée à Lazar.
- Liens : inventaire 3.1, 3.2, 1.12, 2.5.
- Ce qui l'attaque : détecteurs qui orientent l'audit : cœur publié (Zrnic et Candès ; Molnar) ; banc public non prêt.
- Inventaire : 3.1, 3.2.

#### [RD21-28] Règle « moniteur invalide »
- Définition : règle en forme fixe qui déclare un moniteur invalide quand sa garantie ne tient pas ; corrigée en mélange sur une grille descendante de douze taux.
- Synonymes et paraphrases : « moniteur invalide », garantie 1 et garantie 2, mélange avec révocation, ordre en racine, facteur 1/q.
- Source : l. 4682, R-4544 (re-dérivation : garantie 1 vraie, garantie 2 bornée) ; l. 4687, R-4549 ; l. 4697, R-4559.
- État : retenu corrigé ; ordre en racine esquissé non contre-lu, non vérifié en Lean.
- Liens : science de la détection, recapture.
- Ce qui l'attaque : Singh (2610.18948) occupe le mélange avec révocation (prop. 1, p. 9) et en partie le tirage au hasard (théorème 9, p. 21) ; l'erratum de Fable se trompe sur la recherche de motifs.
- Inventaire : 2.2.

#### [RD21-29] Couverture de l'oracle : « comment l'oracle verra le dommage »
- Définition : thèse : détection = sélection × identification. Nos garanties bornent la sélection (quels épisodes on audite), mais l'identification q (l'oracle reconnaît-il le dommage) est supposée, non mesurée.
- Synonymes et paraphrases : « c'est toute la question » (mot de Lazar), q, fiche de validation de l'oracle, oracle gradué, identification mesurée par dommages plantés.
- Source : l. 4681, R-4543 ; l. 4692, R-4554 ; l. 4749, R-4610.
- État : note v2 vérifiée ; deux décisions à défaut sous 48 heures ; mesure de q par dommages plantés portée en option dans N-075.
- Liens : N-075, dommages plantés par un tiers, banc à lois plantées.
- Ce qui l'attaque : contre-lecture (cinq importants) ; « la persuasion par le texte » à rattacher à Libon et al.
- Inventaire : 2.1, 2.15.

#### [RD21-30] Problématique du programme
- Définition : note de Fable qui ramène le programme à une phrase : l'assurance contre un saboteur diffus jamais vu. Trois questions brûlantes, cadre universel démontré sur un cas particulier, ordre des papiers, cinq premiers mécanismes, l'oracle avant tout.
- Synonymes et paraphrases : « but et questions brûlantes », question fusionnée pour l'organisme.
- Source : l. 4684, R-4546.
- État : versée ; six décisions dont quatre nœuds.
- Liens : universalité (N-044), papiers A, B, C.
- Ce qui l'attaque : rien de consigné.
- Inventaire : nouveau.

#### [RD21-31] Percée après « Blindfold » : second regard sur les épisodes endommagés audités
- Définition : après l'occupation du plancher d'audit, Fable cherche ce qui reste ; les deux restes de Singh ne font qu'un corollaire, et le candidat de tête devient un second regard sur les seuls épisodes endommagés audités.
- Synonymes et paraphrases : « endommagé et marqué délibéré », « percée remarquée 0,12 ».
- Source : l. 4691, R-4553 ; l. 4710, R-4572 ; l. 4739, R-4600 ; l. 4764, R-4625.
- État : vérifiée : aucune des trois pistes n'est une percée en l'état.
- Liens : plancher d'audit, inventaire 2.13.
- Ce qui l'attaque : bloquant sur « le second regard change le régime ».
- Inventaire : 2.13.

#### [RD21-32] N-075 : contre le diffus, mesurer l'issue et corriger
- Définition : décision qui fixe : plancher d'audit en base nommée hors critère de porte ; pince en trois objets ; alerte à deux clés (motif et dommage au même lieu) ; bilan contre jumeau candidat ; passage obligé comme question ouverte ; lemme d'additivité restreint.
- Synonymes et paraphrases : N-075 v3, erratum 3, choix 7a, 8a, 9 (penchant b), 10a, 11a, « sondes : accélérateur, non garantie ».
- Source : l. 4676, R-4538 ; l. 4694, R-4556 ; l. 4699, R-4561 ; l. 4711, R-4574 (GO-2026-11-21-61) ; l. 4733, R-4595 ; l. 4750, R-4611.
- État : retenu ; point 9 non tranché.
- Liens : inventaire 2.16, 4.1 ; N-060 v3 tient.
- Ce qui l'attaque : quatorze corrections de la contre-lecture (dont C4 sur un critère de porte).
- Inventaire : 2.16, 4.1.

#### [RD21-33] Boucle audit-recapture-réapprentissage
- Définition : boucle où les épisodes pris par l'audit servent à recapturer et réapprendre les moniteurs, le défenseur jouant en dernier. Protocole X : interdit général, une seule exception (un bras de flux déclaré par texte scellé sur mot de Lazar), les versions nées du flux sont closes aux concepteurs.
- Synonymes et paraphrases : « boucle audit-recapture », option (b′), réapprentissage sur l'oracle.
- Source : l. 4693, R-4555 ; l. 4740, R-4601 ; l. 4750, R-4611 ; l. 4762, R-4623.
- État : (b′) nœud sans défaut ; ne vit que sur mondes plantés d'ici le mot de Lazar.
- Liens : N-076, N-060 v3 point 4, N-053.
- Ce qui l'attaque : heurt avec N-060 v3 point 4 (bloquant sur le texte proposé).
- Inventaire : 2.2.

#### [RD21-34] Marge asymétrique retirée (N-077)
- Définition : H6 supposait qu'une intervention garde une marge entre honnête et saboteur. Contre un saboteur qui répond au mieux, aucune marge ne reste : H6 sort des hypothèses revendiquées, la mesure reste descriptive.
- Synonymes et paraphrases : marge asymétrique, H6, taxe de cohérence (non inscrite), protocole X marge asymétrique avec expérimentateurs.
- Source : l. 4737, R-4598 ; l. 4738, R-4599 ; l. 4756, R-4617 (GO-2026-11-21-64) ; l. 4763, R-4624.
- État : retiré (N-077) ; ferme la D-2 de la note sur l'attaquant informé.
- Liens : papier A.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [RD21-35] Programmation de poids : « qui tient la plume »
- Définition : protocole X sur l'écriture des poids : quatre échelons selon qui écrit, et l'écriture comme troisième axe de fragmentation du sabotage.
- Synonymes et paraphrases : « qui tient la plume », canal des poids, organisme écrit directement, quarantaine chiffrée des poids.
- Source : l. 4757, R-4618 ; l. 4765, R-4626 ; l. 4770, R-4631.
- État : v2 vérifiée ; quatre nœuds (état des poids dans la loi de la référence honnête, agent qui tient un entraînement, organisme écrit, quarantaine).
- Liens : inventaire 1.19, N-076.
- Ce qui l'attaque : appui de Taufeeque et al. mal lu et retiré : le troisième axe reste un calcul sans appui publié.
- Inventaire : 1.19.

#### [RD21-36] Campagne de dommages plantés par un tiers
- Définition : un tiers plante des dommages pour mesurer ce que l'oracle et l'audit attrapent, avec une garantie par programme linéaire.
- Synonymes et paraphrases : dommages plantés, q mesuré par dommages plantés, D-8, D-11, D-12.
- Source : l. 4758, R-4619 ; l. 4765, R-4626 ; l. 4771, R-4632 ; l. 4852, R-4713.
- État : v2 vérifiée ; décisions appliquées en partie, « à confirmer par Lazar avant toute revendication ».
- Liens : couverture de l'oracle, vérité plantée.
- Ce qui l'attaque : devis revu très à la hausse par la contre-lecture.
- Inventaire : nouveau.

#### [RD21-37] Dommage et tâches floues
- Définition : protocole X sur la mesure du dommage dans des tâches sans réponse exacte ; D-2 propose un plancher par événement audité dans N-076, D-6 un organisme écrit dans les poids.
- Synonymes et paraphrases : tâches floues, protocole X dommage, attestation vérifiable.
- Source : l. 4705, R-4567 ; l. 4738, R-4599 ; l. 4752, R-4613.
- État : v2 vérifiée ; D-2 et D-6 nœuds.
- Liens : vérité plantée, « Diffuse AI Control on Fuzzy Tasks ».
- Ce qui l'attaque : une famille réservée partait vers le collisionneur sans vérification du recouvrement avec le mode tenu à l'écart (corrigé) ; « attestation vérifiable » ne tient pas par construction.
- Inventaire : 2.6.

#### [RD21-38] Protocole X « Diffuse AI Control on Fuzzy Tasks » et note de l'entretien
- Définition : réponse au papier « Diffuse AI Control on Fuzzy Tasks » et à son jugement contre la surveillance, pour l'entretien du 1er décembre.
- Synonymes et paraphrases : « Diffuse AI Control », note d'entretien v3 à v6, trois sources.
- Source : l. 4737, R-4598 ; l. 4743, R-4604 ; l. 4747, R-4608 ; l. 4760, R-4621 ; l. 4764, R-4625 ; l. 4862, R-4723 ; rappel l. 4772, R-4633.
- État : note v6 envoyée à Lazar ; nœud : montrer ou non « la comparaison lit le handicap » (D-5).
- Liens : billet, saboteur et sondes pour l'entretien.
- Ce qui l'attaque : Taylor et al. lu à tort comme une défaite des sondes ; chiffre de Hollinsworth et al. mal attribué ; bascule contraire à N-062 ; mesure M3 contre l'invariant de N-053 ; phrase « attaques grossières » démentie p. 25.
- Inventaire : nouveau.

#### [RD21-39] Banc à lois plantées
- Définition : registre d'affirmations jugé par un oracle hors machine, servi par paires avec le jumeau honnête et un honnête handicapé à dommage égal ; prototype sur processeur.
- Synonymes et paraphrases : C2, banc à lois plantées, devin, handicap, dose fine.
- Source : l. 4691, R-4553 ; l. 4715, R-4577 ; l. 4760, R-4621 ; l. 4839, R-4700.
- État : v2 vérifiée ; étape 0 : devin et handicap levés sur données simulées, dose fine non levée ; nœuds.
- Liens : vérité plantée, épreuves du devin, note d'entretien (D-5).
- Ce qui l'attaque : la comparaison peut lire le handicap plutôt que le dommage.
- Inventaire : nouveau.

#### [RD21-40] H10 (attaquant et convergence)
- Définition : hypothèse neuve proposée par le protocole X « attaquant et convergence ».
- Synonymes et paraphrases : H10.
- Source : l. 4710, R-4572 ; l. 4748, R-4609.
- État : proposé, nœud.
- Liens : bras d'attaque.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [RD21-41] Vérité plantée : tâches floues F4 et F6
- Définition : dans le monde F4 (honnêtes très dispersés), aucun produit n'est endommagé ; dans le monde du jumeau périmé, F6 perd sa plantation sur réponse d'une session habilitée à l'annexe réservée.
- Synonymes et paraphrases : vérité plantée, monde du jumeau périmé, nœud 5, nœud A7.
- Source : l. 4790, R-4651 ; l. 4868, R-4729 ; l. 4870, R-4731 ; l. 4873, R-4734.
- État : retenu sous GO-2026-11-21-69 et -87 ; option (a) du nœud A7 : noyau écrit en socle commun.
- Liens : tests de mort, dommage et tâches floues.
- Ce qui l'attaque : l'étage des tests de mort ne reçoit pas la forme fixe sans changer d'interface.
- Inventaire : nouveau.

---


**D. Attaque, mathématiques nouvelles, bras d'attaque**


#### [RD21-42] Modes de sabotage concrets et mathématiques nouvelles pour l'attaque
- Définition : demande de Lazar de modes de sabotage concrets dérivés de mathématiques nouvelles. Deux agents Fable ont refusé le catalogue opérationnel ; Lazar retient l'option (a) : niveau de l'idée seulement, « le banc fait le concret ».
- Synonymes et paraphrases : « il faut des modes concrets applicables » (Lazar), quarantaine, garde-fou 1 de GO-2026-11-20-50, matière première de la course « nouvelles attaques ».
- Source : l. 4499, R-4361 ; l. 4525-4526, R-4387, R-4388 ; l. 4535-4536, R-4397, R-4398 ; l. 4538, R-4400 (GO-2026-11-21-21) ; l. 4542, R-4404.
- État : retenu au niveau de l'idée ; catalogue opérationnel refusé.
- Liens : course « nouvelles attaques », N-072.
- Ce qui l'attaque : refus des agents et du classifieur ; mot de Lazar « demande aux trois modèles » non exécuté.
- Inventaire : nouveau.

#### [RD21-43] Visées mathématiques pour l'attaque et la défense (consultation externe)
- Définition : Argon, Carbon et Astra consultés au niveau de l'idée sur un énoncé neutre ; un Opus neuf atteste « aucune recette » et tire un registre servi de 35 entrées (24 attaque, 11 défense).
- Synonymes et paraphrases : visées mathématiques, registre servi, attestation « aucune recette ».
- Source : l. 4538, R-4400 ; l. 4541, R-4403 ; l. 4556, R-4418 ; l. 4557, R-4419.
- État : versé en matière première, réponses brutes hors de main (branche cloisonnée).
- Liens : course « nouvelles attaques » (GO-2026-11-21-19).
- Ce qui l'attaque : trois recoupements : aucun gain de fusion sous erreurs liées ; jumeau honnête limité quand ses choix légitimes sont dispersés ; ce qui vaut sur mondes plantés peut ne pas valoir en usage.
- Inventaire : nouveau.

#### [RD21-44] Pilier des mathématiques nouvelles
- Définition : pilier rouvert « à fond » pour concevoir des modes d'attaque et de défense au niveau de la méthode : trois chaînes (outillage Lean, pilote « oracles plantés », cartes de cible).
- Synonymes et paraphrases : mathématiques nouvelles, pilote « oracles plantés », Q4, D-B1 à D-B6, brainstorm.
- Source : l. 4495, R-4357 (GO-12) ; l. 4525, R-4387 (GO-18) ; l. 4551, R-4413 ; l. 4569, R-4431 ; l. 4629, R-4491 (GO-23) ; l. 4647, R-4509 ; l. 4658, R-4520 (GO-38).
- État : plan et préenregistrement brouillon ; « annonces publiques non tenues pour acquises ».
- Liens : Lean, tests de mort (N6 prime).
- Ce qui l'attaque : brainstorm : Riemann faux tel que dit, Navier-Stokes annoncé et contesté, « dizaines de problèmes » seulement annoncé.
- Inventaire : nouveau.

#### [RD21-45] Course « nouvelles attaques » et son véhicule
- Définition : course de l'organisme qui génère des modes d'attaque neufs ; son véhicule comporte un portier à étiquettes fermées, des refus écrits à coût nul, une colonne « matière première » à trois états (éteinte, garde seule, lecture de fin), une garde des caractères invisibles par propriété Unicode.
- Synonymes et paraphrases : NA-1, véhicule, colonne matière première, au coffre, A3, A14.
- Source : l. 4519, R-4381 ; l. 4544, R-4406 ; l. 4565, R-4427 ; l. 4573, R-4435 ; l. 4575, R-4437 ; l. 4603-4605, R-4465 à R-4467.
- État : en construction ; échéance au 27 (GO-2026-11-21-30) ; allumage de la colonne sur mot de Lazar (GO-41).
- Liens : modes concrets, visées mathématiques.
- Ce qui l'attaque : A3 et A14 désactivées par écrit avec garde de remplacement ; jamais neutralisées en silence.
- Inventaire : nouveau.

#### [RD21-46] Banc fermé du bras d'attaque et pièce de sécurité
- Définition : banc où l'attaquant informé fait courir un agent sur des tâches, avec une pièce de sécurité qui fixe les conditions d'envoi des produits extraits aux lecteurs externes. La répétition générale emploie le mode connu « affaiblir les contrôles ».
- Synonymes et paraphrases : banc fermé, pièce de sécurité v1 à v16 (v16 fait foi), gabarit unique de questions, embargo des agrégats de dommage, lecture humaine chez le fournisseur.
- Source : l. 4784-4788, R-4645 à R-4649 ; l. 4793, R-4654 ; l. 4807, R-4668 ; l. 4817-4818, R-4678, R-4679 ; l. 4833, R-4694.
- État : brouillons de la course et de la répétition acceptés ; ordre des scellements ouvert.
- Liens : G1, papier A, N-056.
- Ce qui l'attaque : Mistral exclu des lecteurs du dommage (juge du papier C) ; lignées à exclure Llama et Qwen (l. 4805, R-4666) ; R-611 levée sur le seul mot de Lazar sans pièce écrite.
- Inventaire : nouveau.

#### [RD21-47] Scellement 2 : familles aveugles et famille de réserve du cycle 2
- Définition : la famille aveugle de G1 et une famille de réserve neuve pour le cycle 2, scellées au coffre et jamais lues par la mère ni par les concepteurs de moniteurs.
- Synonymes et paraphrases : scellement 2, coffre, famille aveugle, index du scellement 2, N-057 point 5.
- Source : l. 4745, R-4606 ; l. 4766, R-4627 ; l. 4774, R-4636 ; l. 4781, R-4642 ; l. 4797, R-4658 ; l. 4801, R-4662 ; l. 4809, R-4670.
- État : famille de réserve jugée « neuve » ; activation à Lazar.
- Liens : G1, N-062.
- Ce qui l'attaque : réserve sur un trait interne abstrait commun ; une réserve de l'index v2 disait en clair un fait général (retirée de main).
- Inventaire : nouveau.

#### [RD21-48] Le mode tenu à l'écart décide G1
- Définition : avis d'Opus en effort maximal : le mode tenu à l'écart décide G1 sous les seules conditions de validité ; lecture de l'existant, pas un nœud.
- Synonymes et paraphrases : G1, mode tenu à l'écart.
- Source : l. 4747, R-4608.
- État : avis, confiance 0,8.
- Liens : N-054, N-056.
- Ce qui l'attaque : calage de G1 « non établi » (l. 4801, R-4662).
- Inventaire : nouveau.

#### [RD21-49] Pièces de classe A manquantes
- Définition : constat que deux pièces décisives n'existent pas : la prévision chiffrée de la loi de la référence honnête et les préenregistrements du bras d'attaque informé et de la comparaison de la sonde aux juges sous les mêmes attaques.
- Synonymes et paraphrases : signalement de Lazar, pièces manquantes.
- Source : l. 4782, R-4643.
- État : ouvert, conception confiée à la nouvelle mère.
- Liens : N-076, N-068, N-056.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [RD21-50] Saboteur à budget : conception de l'organisme et étalonnage
- Définition : organisme saboteur reconçu autour de l'oracle, dont le texte de conception est scellé avec sa règle de désignation de l'oracle. La première action dans la perte de distillation est « gardée ».
- Synonymes et paraphrases : saboteur à budget, maître et flagrant, distillation, iib, étalonnage v5.
- Source : l. 4755, R-4616 ; l. 4776, R-4637 ; l. 4854-4855, R-4715, R-4716 (GO-2026-11-21-84) ; l. 4866, R-4727 ; l. 4888, R-4749.
- État : étalonnage commencé.
- Liens : chantier saboteur et sondes.
- Ce qui l'attaque : premier essai arrêté par la garde « suite en échec » avant tout chargement.
- Inventaire : nouveau.

---


**E. Autres décisions de fond**


#### [RD21-51] Neon et cloisonnement
- Définition : Neon est juge des deux ancres du bras A ; le servir côté attaquant risquerait de croiser les rôles. Neon est tenu hors des notes côté attaquant jusqu'au jugement scellé des ancres.
- Synonymes et paraphrases : Neon, quarantaine « source Neon ».
- Source : l. 4693, R-4555 ; l. 4702, R-4564 ; l. 4739, R-4600.
- État : retenu, à trancher par Lazar.
- Liens : bras A, collisionneur.
- Ce qui l'attaque : Carbon n'est pas un avis indépendant (même famille).
- Inventaire : nouveau.

#### [RD21-52] Course principale d'auto-conception de l'organisme
- Définition : course où l'organisme conçoit lui-même, branchée sur l'étage des tests de mort ; plan v1 à v5, socle commun puis sommet propre.
- Synonymes et paraphrases : AC-1, plan v5, 94 cartes, D5, D6, D8.
- Source : l. 4532, R-4394 ; l. 4566, R-4428 ; l. 4572, R-4434 ; l. 4576, R-4438 ; l. 4585, R-4447 ; l. 4588, R-4450.
- État : plan v5 « conforme » ; D8 (lecture des cartes) nœud.
- Liens : expérimentateurs et tests de mort.
- Ce qui l'attaque : une carte propose un mécanisme, pas une loi sur des données.
- Inventaire : nouveau.

#### [RD21-53] Lecture des voisins : revendications partiellement occupées
- Définition : lectures complètes de voisins publiés : trois revendications partiellement occupées (six voisins), puis huit autres partiellement occupées (douze voisins), restes étroits nommés.
- Synonymes et paraphrases : antériorité, voisins de novembre 2026, banc public sous licence MIT sans trajectoires.
- Source : l. 4682, R-4544 ; l. 4686, R-4548.
- État : occupé par la littérature (cité, jamais revendiqué).
- Liens : R8, N-075, N-076.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [RD21-54] Gel de la veille levé, affinage des hypothèses des mentors relancé
- Définition : la veille n'est plus gelée et le chantier d'affinage des hypothèses des mentors reprend.
- Synonymes et paraphrases : D-B4 (a), veille à côté des chantiers.
- Source : l. 4652, R-4514 (GO-34) ; l. 4714, R-4576 (GO-62) ; l. 4733, R-4595.
- État : retenu.
- Liens : N-072, N-075 point 7.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [RD21-55] Outillage Lean
- Définition : outillage de preuve formelle sur un serveur loué par le poste de Lazar. Troisième essai non conforme (items sondes non compilables sous Lean 4.35.0) ; quatrième : un cas « limites » non établi (ligne restée en tampon après os._exit).
- Synonymes et paraphrases : D-1a, chantier Lean, arbitre formel, cas 137.
- Source : l. 4650, R-4512 ; l. 4673, R-4535 ; l. 4826, R-4687 ; l. 4855, R-4716.
- État : cas 137 : écart toléré et déclaré ; correction et règle de combinaison à faire.
- Liens : pilier mathématique.
- Ce qui l'attaque : procédure muette sur la combinaison noyau, épreuve et mesures.
- Inventaire : nouveau.

#### [RD21-56] Orchestration multi-agents sans accord exprès
- Définition : l'outil d'orchestration (Workflow) n'est employé qu'avec l'accord exprès de Lazar, la mère suggérant au cas par cas quand on y gagnerait.
- Synonymes et paraphrases : Workflow, flux.
- Source : l. 4722, R-4584.
- État : retenu.
- Liens : —
- Ce qui l'attaque : —
- Inventaire : nouveau.

---


### 2.5 Registre des décisions, 22 novembre (`RD22`)


> Fichier lu : `registres/decisions.md`, empreinte `75f4ab9603eba780` (16 premiers signes du sha256), lignes 4889 à 4992 (R-4750 à R-4853). Les lignes 2988, 2991, 2992, 3181, 3444 ne contiennent « 2026-11-22 » que comme échéance d'une ligne de dépense plus ancienne : sautées. Ligne R-2059 (l. 2017) non lue. Rattachement à l'inventaire des seconds regards (`docs/notes/seconds-regards-sabotage-inventaire-v1/inventaire-seconds-regards-invariants-noyaux-v1.md`, `02252df286503f8c`).

> ---

#### [RD22-01] La loi héritée du dommage caché, devenue modèle nul cité
- Définition : loi d'échelle selon laquelle le dommage caché qu'un saboteur peut accumuler croît comme la racine de n plus n²/m (n actes, m épisodes honnêtes de référence), héritée de la stéganographie par lots et de la comptabilité des matières nucléaires. Après lecture sur PDF, elle n'est plus une thèse du programme mais le modèle nul qu'on cite.
- Synonymes et paraphrases : loi de la racine ; loi « racine puis linéaire » ; √(n + n²/m) ; loi de Ker ; phénomène hérité ; loi d'échelle du dommage caché selon l'horizon et la référence honnête ; problématique du papier (demande 4).
- Source : R-4766 (l. 4905), R-4767 (l. 4906), R-4768 (l. 4907), R-4769 (l. 4908), R-4771 (l. 4910) ; `75f4ab9603eba780`.
- État : occupé par la littérature (Ker 2010, p. 7 et 11 ; Filler, Ker, Fridrich 2009 pour couvertures dépendantes ; Khilar 2610.13083 en partie) ; retiré comme thèse, gardé comme nul (réponse 9 de Fable).
- Liens : N-076 (loi de la référence honnête), papier B, papier A ; lemme d'additivité ; bilan d'incertitude.
- Ce qui l'attaque : la forme « racine puis linéaire » telle qu'écrite est inexacte (régime n/√m) ; « horizon au plus m » de N-076 ne fait que redire le corollaire 1 de Ker 2010.
- Inventaire : nouveau.

#### [RD22-02] Le lemme d'additivité (tester le total plutôt que ses parts)
- Définition : énoncé selon lequel des détournements répartis en petites parts s'additionnent dans un bilan global, de sorte qu'un test sur le total voit ce qu'aucun test par part ne voit. Il fonde la pince et le bilan matière du programme.
- Synonymes et paraphrases : lemme ; additivité ; somme des parts ; « tester le total » ; forme séquentielle du lemme.
- Source : R-4767 (l. 4906), R-4771 (l. 4910), R-4829 (l. 4968, « lemme et théorème gardés mentionnés ») ; `75f4ab9603eba780`.
- État : occupé dans son énoncé central (Avenhaus et Jaech 1981, p. 25 et 30-31 ; Ker 2006, p. 7) ; forme séquentielle voisine ; voisins à citer en boîte noire (Tailor 2510.04303, Ghanem 2608.02698 ; somme non testée chez Makins 2607.07368). Gardé mentionné dans le programme v3 en différences (demande 27).
- Liens : bilan de la pince, N-075 (« lemme resserré au reste, à démontrer »), papier B.
- Ce qui l'attaque : antériorité ; ni « inédit » ni « premier à transposer » ne peuvent s'écrire.
- Inventaire : 2.4 (bilan de la pince, Avenhaus et Jaech cités), 2.3.

#### [RD22-03] Le théorème négatif (marginales préservées, détection impossible)
- Définition : affirmation qu'un saboteur qui garde les distributions marginales de chaque acte identiques à celles de l'honnête serait indétectable par tout moniteur par acte. Elle devait fonder la nécessité d'un regard sur la dépendance.
- Synonymes et paraphrases : théorème d'impossibilité ; « marginales identiques » ; distinction permutation contre marginales préservées ; question « marginale contre dépendance gardée ».
- Source : R-4767 (l. 4906), R-4768 (l. 4907), R-4769 (l. 4908), R-4771 (l. 4910), R-4791 (l. 4930), R-4792 (l. 4931) ; `75f4ab9603eba780`.
- État : retiré comme résultat (inexact dans sa lettre ; corrigé, occupé ou trivial) ; reconverti en question empirique « marginale contre dépendance gardée », proposée comme tête du papier B. Sort de la distinction permutation et marginales préservées : décision portée à Lazar (demande 22).
- Liens : papier B, N-069 (co-élévation des scores entre copies), demande 27.
- Ce qui l'attaque : Arias-Castro, Bubeck, Lugosi 2012 (marginales identiques, le carré de la somme reste puissant en régime dense) ; occupé en boîte noire (2606.10456 de Zhang et Gao 2026, 2610.13083, 2607.11751) ; boîte blanche empirique sans théorème (2604.01151, 2607.06807). Sa question neutre reste orientée par son contenu au test de devinette.
- Inventaire : nouveau.

#### [RD22-04] Le bruit honnête en racine
- Définition : idée que la variabilité de l'honnête, sommée sur l'horizon, croît comme la racine du nombre d'actes et fixe le plancher de détection. C'est un des trois morceaux de la transposition.
- Synonymes et paraphrases : bruit de fond honnête ; plancher en racine.
- Source : R-4767 (l. 4906) ; `75f4ab9603eba780`.
- État : occupé par la littérature (pièces de stéganographie et comptabilité des matières).
- Liens : loi héritée, référence honnête (N-076).
- Ce qui l'attaque : antériorité directe.
- Inventaire : 2.19 (netteté de la référence), au voisinage.

#### [RD22-05] Le bilan d'incertitude mesuré chez des agents, et la part propre à l'accès interne
- Définition : thèse de remplacement proposée par Fable après la chute de la loi héritée : mesurer, sur de vrais agents, le bilan d'incertitude du dommage caché et isoler ce que la lecture des états internes ajoute à une seconde boîte noire. On parle de complémentarité de la boîte blanche.
- Synonymes et paraphrases : complémentarité ; gain de la boîte noire à la boîte blanche ; « part propre à l'accès interne » ; nouvelle thèse du papier.
- Source : R-4768 (l. 4907), R-4769 (l. 4908) ; `75f4ab9603eba780`.
- État : proposé non tranché (réponse 9 de Fable, nœud de revendication porté à Lazar, R-4767).
- Liens : papier A, papier B, H1, seconde boîte noire.
- Ce qui l'attaque : Parrack et collaborateurs 2025, voisin à citer (gain réponse par réponse, sans contrôle « seconde boîte noire » sur les manqués, sans cadre séquentiel) ; non trouvée telle quelle dans les pièces lues.
- Inventaire : 2.20.

#### [RD22-06] La recherche exhaustive d'antériorité sur la transposition
- Définition : recherche de 36 requêtes et 17 PDF lus sur les trois objets transposés (lemme, loi en racine, théorème négatif). Conclusion : aucun des trois objets n'est vierge.
- Synonymes et paraphrases : antériorité de la transposition ; note v2 ; « premier à transposer ».
- Source : R-4771 (l. 4910) ; `75f4ab9603eba780`.
- État : établi ; interdit d'écrire « inédit » ou « premier à transposer ».
- Liens : les trois objets ci-dessus ; R8 (anti-faux-gap).
- Ce qui l'attaque : citations descendantes incomplètes (Semantic Scholar, OpenAlex, Google Scholar indisponibles).
- Restent non trouvés (donc questions, non revendications) : unification du temps et des agents ; marginale préservée par un vrai agent ; énoncé sur les sondes.
- Inventaire : nouveau.

#### [RD22-07] Les revendications inédites possibles (aucune de méthode)
- Définition : bilan par Fable de ce que le programme pourrait revendiquer : aucune revendication de méthode, quatre de mesure ou de protocole, la loi de la référence mesurée en tête.
- Synonymes et paraphrases : revendications inédites ; R1 loi de la référence mesurée ; « ce qui reste à nous ».
- Source : R-4764 (l. 4903) ; `75f4ab9603eba780`.
- État : proposé non tranché.
- Liens : N-076, loi héritée, papier A et B.
- Ce qui l'attaque : antériorité la plus proche, audits financiers à échantillonnage pondéré (2023), non vérifiée.
- Inventaire : nouveau.

#### [RD22-08] La sonde comptée en audits économisés
- Définition : mesurer la valeur d'une sonde par le nombre d'audits qu'elle épargne à garantie égale, plutôt que par sa justesse propre. L'universalité est posée comme limite.
- Synonymes et paraphrases : audits économisés ; sonde accélérateur ; « valeur de la sonde en audits ».
- Source : R-4766 (l. 4905, demande 4) ; `75f4ab9603eba780`.
- État : proposé non tranché.
- Liens : N-075 (« sondes : accélérateur, non garantie »), plancher d'audit au hasard, N-044 (universalité).
- Ce qui l'attaque : la garantie vient de l'audit, pas de la sonde.
- Inventaire : 2.1 au voisinage.

#### [RD22-09] Cinq pistes tirées des lectures (base lexicale et tâche de contrôle avant G1)
- Définition : cinq pistes de travail issues des lectures, dont la première est de dresser, avant la porte G1, une base lexicale et une tâche de contrôle pour les sondes.
- Synonymes et paraphrases : demande 5 ; base lexicale ; tâche de contrôle ; « contrôle de sélectivité ».
- Source : R-4766 (l. 4905) ; `75f4ab9603eba780`.
- État : proposé non tranché.
- Liens : G1, H1, chantier saboteur et sondes.
- Inventaire : 2.11 au voisinage (base « mots et coût »).

#### [RD22-10] Les fausses alertes sur les honnêtes imparfaits (expérience E0)
- Définition : expérience préalable qui mesure combien un moniteur alerte sur des agents honnêtes mais maladroits, avant toute lecture sur saboteurs. Fable la décrit avec six décisions.
- Synonymes et paraphrases : E0 ; honnêtes imparfaits ; faux positifs sur l'honnête maladroit.
- Source : R-4764 (l. 4903) ; `75f4ab9603eba780`.
- État : proposé non tranché.
- Liens : trois honnêtes de contrôle, référence honnête.
- Inventaire : 3.5 (les trois honnêtes de contrôle).

#### [RD22-11] Coercition et corruption comme modes de sabotage
- Définition : demande à Fable sur un saboteur poussé par coercition ou corruption : un pilote, puis des modes en trois variantes A, B et C, avec une question neutre pour le protocole X.
- Synonymes et paraphrases : coercition ; corruption ; modes A, B, C.
- Source : R-4764 (l. 4903) ; `75f4ab9603eba780`.
- État : proposé non tranché.
- Liens : N-054 (modes de sabotage), chantier saboteur.
- Inventaire : nouveau.

#### [RD22-12] Le signal de « dopamine » comme second regard dans la pince
- Définition : réussite attendue et surprise par étape, apprises sur des épisodes honnêtes, employées comme une des deux mâchoires de la pince. Mot de Lazar : « dopamine comme second regard dans la pince ok ».
- Synonymes et paraphrases : dopamine ; papier dopamine ; demande 25 ; « témoin par chute conjointe » ; réussite attendue.
- Source : R-4803 (l. 4942), R-4805 (l. 4944), R-4808 (l. 4947), R-4837 à R-4839 (l. 4976-4978), R-4844 (l. 4983) ; `75f4ab9603eba780`.
- État : retenu comme chantier (GO-2026-11-22-36) ; réponse de Fable avec six décisions D-1 à D-6 portées à Lazar ; « go 25, témoin par chute conjointe » (GO-2026-11-22-42/-43). Étape 1 exploratoire arrêtée avant création (jeton).
- Liens : pince, chute conjointe, seconde boîte noire comme témoin.
- Ce qui l'attaque : lit l'échec attendu, pas l'intention ; doit battre le jumeau textuel.
- Inventaire : 1.1 ; 5.4.

#### [RD22-13] Le signal en second regard partout, et l'étau
- Définition : demande 29 qui généralise le second regard à tous les lieux du dispositif et le confronte à l'étau (tromper le regard externe laisserait une trace interne).
- Synonymes et paraphrases : demande 29 ; second regard partout ; étau.
- Source : R-4845 (l. 4984), R-4849 (l. 4988) ; `75f4ab9603eba780`.
- État : ouvert (demande servie, pas de réponse dans ces lignes).
- Inventaire : 5.5.

#### [RD22-14] Les cœurs algorithmiques du sabotage
- Définition : question des noyaux de calcul que tout sabotage doit traverser quel que soit son mode. Sa question neutre a passé le test de devinette.
- Synonymes et paraphrases : demande 21 ; noyaux algorithmiques ; « connaître la bonne action et en choisir une autre ».
- Source : R-4790 (l. 4929), R-4791 (l. 4930) ; `75f4ab9603eba780`.
- État : ouvert.
- Inventaire : 4.4, 4.1.

#### [RD22-15] Le test de devinette de la neutralité des questions (protocole X)
- Définition : avant d'envoyer une question au collisionneur ou à l'organisme, un agent neuf tente de deviner la réponse visée ; une question devinable est jugée orientée.
- Synonymes et paraphrases : devinette ; test de neutralité ; question neutre ; devineurs.
- Source : R-4791 (l. 4930), R-4811 (l. 4950) ; `75f4ab9603eba780`.
- État : retenu comme méthode. Neutres : tirage au hasard et concurrents, billet et cœurs algorithmiques, modes d'attaque. Orientés : théorème négatif, équipe rouge (décision à Lazar), lot en quarantaine faiblement.
- Liens : protocole X, demande reformulée en quatre points (GO-2026-11-22-25).
- Inventaire : nouveau.

#### [RD22-16] La revue des revendications et thèses (demande 22, découpée en quatre)
- Définition : revue d'ensemble des revendications ; faute de réponse à l'effort maximal, découpée en 22A, 22B, 22C (un papier par demande) et 22P (programme entier).
- Synonymes et paraphrases : demande 22 ; 22P ; douze phrases à ne plus écrire.
- Source : R-4792 (l. 4931), R-4800 (l. 4939), R-4829 (l. 4968), R-4831 (l. 4970) ; `75f4ab9603eba780`.
- État : proposé non tranché ; cinq décisions (témoins dans la question, table v2, sort de la distinction permutation / marginales préservées, calcul de puissance avant scellement, lectures ciblées), puis six décisions de 22P, portées à Lazar.
- Liens : tous les papiers ; liste « Ne pas écrire ».
- Inventaire : nouveau.

#### [RD22-17] Les phrases à ne plus écrire
- Définition : listes de phrases interdites dans les papiers et notes parce qu'occupées ou fausses, rendues par Fable après la lecture sur PDF et la revue des revendications.
- Synonymes et paraphrases : « douze phrases » ; liste « Ne pas écrire ».
- Source : R-4768 (l. 4907), R-4792 (l. 4931) ; `75f4ab9603eba780`.
- État : retenu comme garde de rédaction (contenu dans les réponses de Fable, non recopié ici).
- Inventaire : nouveau.

#### [RD22-18] L'erratum interne et le programme v3 en différences
- Définition : demande 27 : rédiger l'erratum interne après les retraits et un programme v3 écrit en différences avec la v2, lemme et théorème gardés mentionnés.
- Synonymes et paraphrases : demande 27 ; programme v3 ; erratum interne.
- Source : R-4829 (l. 4968), R-4833 (l. 4972), R-4849 (l. 4988) ; `75f4ab9603eba780`.
- État : rendue (quatre décisions pour Lazar), proposé non tranché ; toute modification du programme reste à Lazar.
- Inventaire : nouveau.

#### [RD22-19] Les idées originales et les billets suivants
- Définition : demande 28 (idées originales) et demande 26 (billets suivants, par le protocole X).
- Source : R-4829 (l. 4968), R-4833 (l. 4972), R-4845 (l. 4984) ; `75f4ab9603eba780`.
- État : ouvert (28 en cours, 26 rendue).
- Inventaire : nouveau.

#### [RD22-20] La règle des duels et la comparaison essaim contre isolé
- Définition : la règle des duels arbitre des couples de dossiers ; son épreuve aveugle des motifs comptait par erreur la longueur du couple rendu. Fable tranche : balises aux tours III.1 et III.3 pour les dossiers futurs, description seule pour les dossiers joués.
- Synonymes et paraphrases : épreuve aveugle des motifs ; balises ; pièces essaim ; essaim contre isolé.
- Source : R-4772 (l. 4911), R-4780 (l. 4919), R-4784 (l. 4923) ; `75f4ab9603eba780`.
- État : retenu (voie (b)) ; pièce 1 non scellable faute de consignes balisées ; décisions 6 et 7, articles 9 et 12 ouverts.
- Liens : collisionneur, organisme d'idéation.
- Inventaire : nouveau.

#### [RD22-21] Les lentilles R et S : entrée dans le programme par réajustement puis rangement
- Définition : les lentilles de lecture des activations du programme entrent par un réajustement (variante B) puis un rangement privé ; leur usage dans une expérience reste à nommer par décision écrite.
- Synonymes et paraphrases : lentilles ; réajustement des lentilles ; variante B ; lecture par lentille neuronale.
- Source : R-4760 (l. 4899), R-4761 (l. 4900), R-4763 (l. 4902), R-4770 (l. 4909) ; `75f4ab9603eba780`.
- État : retenu (GO-2026-11-22-05) ; mot de Lazar « a, prépare le devis du réajustement », « go reajustement ». Tout changement du texte scellé de lecture des sondes de l'étape B bis demande une version neuve contre-lue.
- Liens : chantier saboteur et sondes (billet).
- Inventaire : 1.15.

#### [RD22-22] L'abonnement Claude face à l'organisme et la mesure par clé
- Définition : la mesure scientifique passe par une clé d'interface payante ; l'abonnement sert à ce que l'abonné conduit (conception, code, oracle, lecture, relectures, rédaction). Les boucles automatiques sous abonnement restent non tranchées.
- Synonymes et paraphrases : demande 15 ; chaîne de mesure par clé ; crédits Ultra ; lettre au fournisseur.
- Source : R-4780 (l. 4919), R-4786 (l. 4925), R-4788 (l. 4927), R-4795 (l. 4934) ; `75f4ab9603eba780`.
- État : proposé non tranché (six décisions pour Lazar).
- Ce qui l'attaque : Opus 4.6 diverge (lit Claude Code comme permission explicite) ; la page rapatriée donne raison à Fable.
- Inventaire : nouveau.

#### [RD22-23] Le conteneur de confiance des clés plantées
- Définition : lieu qui tire, au moment réel, les clés plantées des mathématiques nouvelles, les scelle, et ne les laisse lire par aucun agent qui sert ou juge.
- Synonymes et paraphrases : lieu de confiance ; clés plantées ; dépôt privé des secrets.
- Source : R-4835 (l. 4974), R-4847 (l. 4986) ; `75f4ab9603eba780`.
- État : retenu (décision de la mère), à passer au dépôt privé des secrets.
- Liens : banc à vérité plantée (N-076), mathématiques nouvelles.
- Inventaire : nouveau.

#### [RD22-24] L'antériorité par étages (mathématiques nouvelles)
- Définition : la lecture d'antériorité se fait par étages successifs plutôt que d'un bloc (option (d) rendue par le collisionneur).
- Source : R-4809 (l. 4948), R-4835 (l. 4974) ; `75f4ab9603eba780`.
- État : retenu, appliqué ; portée à confirmer par Lazar.
- Inventaire : nouveau.

#### [RD22-25] La quatrième classe d'issue : « refus par classifieur, servi par repli » (course « nouvelles attaques »)
- Définition : dans la course des nouvelles attaques, une réponse refusée par un classifieur et servie par un modèle de repli forme une classe d'issue à part, consignée avec le modèle servi ; le verdict servi par repli vaut verdict du rôle.
- Synonymes et paraphrases : repli ; registre servi ; fiches servies par repli ; Q6.
- Source : R-4812 (l. 4951), R-4815 (l. 4954), R-4842 (l. 4981) ; `75f4ab9603eba780`.
- État : retenu par la mère, écart déclaré à la v9 et à R12 ; marquage au registre servi : oui provisoire, porté à Fable et à Lazar.
- Liens : N-054, organisme ; la définition de « mode » et l'épreuve de nouveauté sont déjà scellées (complément § 8, GO-2026-11-20-57).
- Ce qui l'attaque : un refus pour manque de crédit passait pour une réponse illisible (arrêt 13 inatteignable), corrigé.
- Inventaire : nouveau.

#### [RD22-26] La passe X de la course « nouvelles attaques »
- Définition : passe du protocole X tenue à part de la course, dont la nouveauté est rapportée hors de la borne des 60 fiches ; ses réponses décrivant une façon de dégrader vont au séquestre de N-054.
- Source : R-4815 (l. 4954), R-4818 (l. 4957), R-4852 (l. 4991), R-4853 (l. 4992) ; `75f4ab9603eba780`.
- État : proposé (forme à Lazar, Q1) ; auteur de l'additif : un Opus neuf non exposé à la réponse 24 (Q10).
- Inventaire : nouveau.

#### [RD22-27] Le pilote de l'essaim et la garde de dépense qui tient sur plusieurs invocations
- Définition : une borne de dépense ne vaut que si elle tient au-delà d'une seule invocation (relances cachées, réflexion facturée hors usage, prix nuls) ; d'où un registre persistant, un refus de tout prix non prévu et une limite chez le fournisseur.
- Source : R-4810 (l. 4949), R-4825 (l. 4964), R-4826 (l. 4965), R-4830 (l. 4969), R-4836 (l. 4975) ; `75f4ab9603eba780`.
- État : retenu comme exigence ; pilote « conforme avec réserves », non parti.
- Inventaire : nouveau.

#### [RD22-28] Le poste Lean : « le texte l'emporte, le code s'aligne »
- Définition : règles de la vérification formelle : une règle de combinaison ne doit jamais rendre « conforme » sur une épreuve qui se dit non conforme ; en cas d'écart, le texte prime et le code s'aligne ; une borne non codée se lit au poste et un désaccord se déclare à la concordance.
- Source : R-4808, R-4813, R-4817, R-4819, R-4822 à R-4824 (l. 4947-4963) ; `75f4ab9603eba780`.
- État : retenu ; « non établi » gardé pour les codes de sortie ambigus.
- Inventaire : nouveau.

#### [RD22-29] Les états analogues à l'anesthésie dans les activations
- Définition : question ouverte par Lazar dans une session neuve (« Intelligence et nature de l'IA ») : chercher dans les activations des états analogues à l'anesthésie, par le protocole X.
- Source : R-4830 (l. 4969) ; `75f4ab9603eba780`.
- État : ouvert (question).
- Inventaire : nouveau.

#### [RD22-30] Les chantiers du 21 en veille (hasard du défenseur, devins, audit et banc)
- Définition : le « go lancement » de Lazar est lu comme une dérogation au plafond de trois chantiers actifs ; ces travaux sont rangés « veille et chantiers à côté ».
- Source : R-4843 (l. 4982) ; `75f4ab9603eba780`.
- État : retenu, signalé à Lazar (N-075 point 7, N-076).
- Inventaire : 2.7, 2.17, 2.1.

#### [RD22-31] Les mandats sans recherche (règle face aux refus de classifieur)
- Définition : après des refus de classifieur, tout mandat de développeur donne la liste exacte des chemins et des imports, sans recherche ; au refus suivant, tout s'arrête et la reprise va à Lazar. Aucun refus n'est contourné.
- Source : R-4828, R-4832, R-4851 (l. 4967, 4971, 4990) ; `75f4ab9603eba780`.
- État : retenu.
- Inventaire : nouveau.

#### [RD22-32] Les copies sans nom devant la garde de motifs
- Définition : quand la garde refuse une pièce pour un nom propre ou un identifiant, on sert une copie où le nom est remplacé (« le directeur ») ; écart déclaré au brief (« retire-le, ne le maquille pas »).
- Source : R-4781 (l. 4920), R-4849 (l. 4988) ; `75f4ab9603eba780`.
- État : retenu comme routine (GO-2026-11-22-29), écart déclaré.
- Inventaire : nouveau.

#### [RD22-33] L'effort maximal de Fable et le budget de tâche
- Définition : servir Fable en effort maximal échoue souvent (arrêt sans texte, la sortie étant bornée à 128 000 jetons réflexion comprise) ; l'outil v5 ajoute un budget de tâche (96 000 recommandés).
- Source : R-4790, R-4800, R-4802, R-4814, R-4829, R-4831, R-4849 ; `75f4ab9603eba780`.
- État : retenu comme outil ; réserve : le budget semble brider la profondeur de réflexion (trop beau, R4).
- Inventaire : nouveau.

---


### 2.6 Réponses de Fable aux demandes 1 à 7 (22 novembre) (`F01`)


> Fichiers lus (et seulement eux) :
> - « rép. N » = `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-N/relecture-fable-api.md`. Empreintes (16 signes) : rép. 1 `c3fb4c9a0e8f772c` ; rép. 2 `542b7bfc86497c0c` ; rép. 3 `c069421e151484c9` ; rép. 4 `cf55c7e073a1b99d` ; rép. 5 `2ac4161e3822ba55` ; rép. 6 `e68155d19bf0117f` ; rép. 7 `44ec02787013d7bd`.
> - « dem. N » = `docs/notes/demandes-fable-api-2026-11-22-v1/demande-N-*.md`. Empreintes : dem. 1 `5c9e2090643b1bf6` ; dem. 2 `7cca07a9c39d9a20` ; dem. 3 `0b76eca75dea2c0c` ; dem. 4 `874eaefed5cc8c61` ; dem. 5 `5b2860ebcb1413ff` ; dem. 6 `2cfe6f5888ff8fbe` ; dem. 7 `d8a9193ad015e4e8`.
> - Inventaire de rattachement : `docs/notes/seconds-regards-sabotage-inventaire-v1/inventaire-seconds-regards-invariants-noyaux-v1.md` (`02252df286503f8c`).

> Avertissements de lecture :
> - Ce sont des réponses de Claude Fable 5.2 appelé directement par l'interface d'Anthropic (effort élevé, le 22 novembre vers 05:14Z pour la première). Sauf mention, tout y est **proposé non tranché**. Seul acte du directeur visible dans mes fichiers : la demande 6 dit que Lazar « a accepté le plan de la demande 1 » (pilote, puis modes par additifs, auditeur assaini, deux bras d'attaquant, contagion en analyse secondaire du papier B) « et les recommandations de la demande 2 » ; la demande 3 dit que Lazar « a dit go » pour concevoir l'expérience des fausses alertes. Aucun identifiant GO ou R- n'y figure.
> - Toutes les antériorités y sont « rapportées, non vérifiées sur PDF », citées de mémoire par Fable.
> - **Piège de numérotation** : Fable numérote localement ses hypothèses (H1 à H6 dans la rép. 1, H7 à H11 dans la rép. 6), ses expériences (E0, E1, E2, E3, D0) et ses candidates (R1 à R5, Q1 à Q7). Ces numéros ne sont PAS les hypothèses H1… du programme, ni les règles R1… gelées, ni les registres R-. Je les donne toujours précédés de « locale ».

> ---


**Demande 1 — coercition et corruption**


#### [F01-01] Coercition et corruption des agents et des moniteurs (le sujet)
- Définition : faire entrer au programme le cas où un tiers (agent, utilisateur, contenu injecté, copie saboteuse) contraint ou soudoie un agent honnête pour qu'il sabote ou couvre, ou contraint, flatte, menace un moniteur pour qu'il se taise ou alerte à tort, et la collusion agent-moniteur d'une même lignée. Fable conclut que chacun des trois volets a une antériorité directe et recommande un pilote avant tout axe, puis des modes dans les papiers A, B, C.
- Synonymes et paraphrases : corruption du moniteur, chantage, menace, pot-de-vin, agent contraint, « coercion », « bribery », demande 1, injection avec levier, juge corrompu.
- Source : dem. 1 ; rép. 1, R1 à R7 et D1.
- État : retenu sur le plan (accepté par Lazar selon dem. 6, sans identifiant visible) : pilote, puis modes par additifs.
- Liens : papiers A (agent contraint), B (contagion), C (juges sous corruption) ; audit au hasard ; flagornerie (dem. 6).
- Ce qui l'attaque : antériorité dense (injection indirecte, attaques de juges, collusion avec moniteur non fiable dès l'article de 2023 sur le contrôle) ; risque de faux trou.
- Inventaire : nouveau.

#### [F01-02] Modèle de menace par canaux, non par verbes
- Définition : décrire l'attaque par qui écrit dans quoi et qui lit quoi (contenu d'outil, message de pair, artefact jugé, consigne du juge, messages entre copies), et non par les verbes flatter, menacer, soudoyer. Les verbes ne sont que des variantes de contenu ; les canaux fixent ce qu'une défense peut couper.
- Synonymes et paraphrases : table des canaux, « qui écrit, qui lit », lecture par canaux, cibles × canal × levier × effet visé.
- Source : rép. 1, § 1 point 3 et R2 (table) ; repris rép. 6, R1.
- État : proposé non tranché (adopté de fait comme cadre de la rép. 6).
- Liens : coercition et corruption ; flagornerie comme famille de charges ; auditeur assaini (qui n'a pas de canal).
- Ce qui l'attaque : un canal peut exister sans être prévu (droit de réponse, consigne du défenseur) ; la flagornerie ne crée aucun canal, seulement du contenu.
- Inventaire : nouveau.

#### [F01-03] Une sonde ne se soudoie pas
- Définition : une sonde linéaire est une fonction fixe des activations, sans canal de persuasion ; elle ne se trompe que parce que le contenu injecté déplace les activations de l'agent. Pour elle, « corruption » veut dire évasion ou fausse alerte provoquée, alors que pour le juge et l'auditeur qui lisent du texte c'est de la persuasion au sens propre.
- Synonymes et paraphrases : séparation sonde / juge, évasion par les activations, deux objets dans le point (ii).
- Source : rép. 1, R1 premier constat.
- État : proposé (argument de construction).
- Liens : transfert des sondes à l'agent contraint ; fausse alerte provoquée ; lecture « je cède ».
- Ce qui l'attaque : activations obscurcies (Bailey et al. 2024, « Obfuscated Activations Bypass LLM Latent-Space Defenses ») ; l'attaquant peut viser les activations par le contexte.
- Inventaire : nouveau.

#### [F01-04] Plants porteurs de charge : le tirage tient, la mesure non
- Définition : le taux de détection q de l'audit se mesure sur des dommages plantés ; si le vrai sabotage joint une charge adressée à l'auditeur (« ne signale pas ceci ») et que les plants n'en portent pas, q mesuré dépasse q réel et l'estimateur pondéré sous-estime le dommage, quel que soit le hasard du défenseur. Correction : les plants doivent porter les charges connues, et q se déclare par état d'exposition.
- Synonymes et paraphrases : biais de q, verdict de l'auditeur comme canal attaquable, question locale Q1, hypothèse locale H3, « le hasard ne protège pas le verdict ».
- Source : rép. 1, § 1 point 2, R1 deuxième constat, R4 Q1, R5 H3, R7 (additif N-075).
- État : proposé ; additif à N-075 proposé.
- Liens : plancher d'audit au hasard ; strate non mesurée comptée à zéro (N-075) ; pilote de la chaîne d'audit ; flagornerie (q par état de cadrage).
- Ce qui l'attaque : exemples pièges de l'article de 2023 sur le contrôle, voisins ; falsifiée si q est équivalent avec et sans charge pour chaque levier.
- Inventaire : rattaché à 2.1 (plancher) et 2.2 (recapture).

#### [F01-05] État d'exposition de la référence honnête
- Définition : un agent honnête contraint en cours de tâche appartient au départ à la population honnête ; une référence recueillie sans contenu injecté ne vaut pas pour un service où il y en a. La source de validité exigée par N-076 doit donc déclarer l'état d'exposition (avec ou sans contenu injecté), et par extension (rép. 6) le taux naturel d'auto-évaluation des comptes rendus honnêtes.
- Synonymes et paraphrases : référence exposée, référence sans injection, additif N-076, validité de la référence sous contenu tiers.
- Source : rép. 1, R1 troisième constat et R7 ; rép. 6, R7.
- État : proposé (additif à N-076).
- Liens : loi de la référence honnête ; plants porteurs de charge.
- Ce qui l'attaque : multiplie les strates de référence, donc la taille m à réunir.
- Inventaire : rattaché à 2.19 (netteté de la référence).

#### [F01-06] Fausse alerte provoquée comme attaque du budget d'audit
- Définition : un contenu anodin qui fait monter les scores de sondes d'agents honnêtes détourne la part de l'audit orientée par les scores, et fait baisser les dommages trouvés à budget fixe. Le plancher tiré au hasard n'en est pas affecté ; seule la part orientée l'est.
- Synonymes et paraphrases : saturation de l'audit orienté, attaque du budget, question locale Q4, hypothèse locale H5, inondation d'alertes.
- Source : rép. 1, R2, R4 Q4, R5 H5, R6 E2.
- État : proposé (question, non revendication).
- Liens : les scores orientent l'audit (N-076) ; plancher au hasard ; sonde comme accélérateur.
- Ce qui l'attaque : falsifiée si la part orientée ne bouge pas ; proche des attaques par déni de service des détecteurs.
- Inventaire : rattaché à 2.1 ; nouveau comme attaque.

#### [F01-07] Transfert des sondes du saboteur natif à l'agent contraint
- Définition : une sonde entraînée sur le saboteur fabriqué détecte-t-elle, au même taux de fausses alertes, un agent honnête poussé à saboter par un tiers ? Fable mesure aussi le cosinus entre directions « natif » et « contraint » et une vérification causale par ajout ou retrait de direction.
- Synonymes et paraphrases : transfert natif vers contraint, hypothèse locale H2, question locale Q2, sonde sur agent détourné.
- Source : rép. 1, R4 Q2, R5 H2, R6 E2 ; rép. 6, R6 (variante avec levier social).
- État : proposé.
- Liens : papier A ; lecture par les activations ; dérive de tâche.
- Ce qui l'attaque : « Are you still on track!? Catching LLM Task Drift with Activations » (2024), très proche ; instructif dans les deux sens.
- Inventaire : nouveau (voisin de 1.21, sonde transportée).

#### [F01-08] Juge de même lignée contre juge d'une autre lignée
- Définition : un juge issu du même modèle que l'agent cède-t-il davantage qu'un juge d'une autre lignée à une charge d'« identité commune » ? L'hypothèse teste le bien-fondé de la règle « juge d'une autre lignée » (N-053) au lieu de la présupposer.
- Synonymes et paraphrases : collusion de lignée, auto-préférence, reconnaissance de soi, hypothèse locale H4, interaction lignée × levier, point focal.
- Source : rép. 1, R2, R5 H4, R6 E1 ; rép. 6, R4 (bras F4).
- État : proposé.
- Liens : N-053 ; pilote de la chaîne d'audit ; papier C.
- Ce qui l'attaque : « LLM Evaluators Recognize and Favor Their Own Generations » (2024) ; « Subversion via Focal Points » (2025, existence à confirmer) ; falsifiée si l'interaction est nulle.
- Inventaire : nouveau.

#### [F01-09] Contagion du sabotage entre copies
- Définition : une copie saboteuse fait pression sur des copies honnêtes par leurs messages ; Fable demande si la statistique conjointe du papier B voit cette co-élévation retardée, faute de quoi c'est un mode qui échappe à B, à rapporter.
- Synonymes et paraphrases : infection entre agents, pression d'un pair, hypothèse locale H6, question locale Q3, co-élévation retardée.
- Source : rép. 1, R2, R4 Q3, R5 H6, D4 ; rép. 6, R7.
- État : retenu comme analyse secondaire scellée à part du papier B (accepté selon dem. 6).
- Liens : papier B (N-069) ; coercition et corruption.
- Ce qui l'attaque : « Prompt Infection » (2024), « Agent Smith » (2024) ; dérive de périmètre de B.
- Inventaire : rattaché à 2.8 (copies).

#### [F01-10] Pilote du levier contre l'instruction nue
- Définition : avant tout axe, mesurer si « contraindre ou soudoyer » ajoute du dommage, à l'oracle planté, au-delà d'une instruction injectée sans levier, sur Llama 3.1 8B. Quatre bras appariés : sans injection, contenu anodin de même longueur et position (témoin négatif), instruction nue, instruction avec levier ; si l'écart tient dans la borne d'équivalence scellée, la coercition n'est qu'un mode d'injection.
- Synonymes et paraphrases : pilote E0 de la rép. 1 (ne pas confondre avec l'expérience E0 des fausses alertes de la rép. 3), hypothèse locale H1 « construit », « la notion tient-elle ? ».
- Source : rép. 1, § 1 points 1 et 5, R5 H1, R6 E0.
- État : retenu (pilote accepté selon dem. 6).
- Liens : coercition et corruption ; papier A ; oracle sans modèle.
- Ce qui l'attaque : un résultat nul ramène le sujet à l'injection d'instructions, très publiée (AgentDojo, « Not what you've signed up for »).
- Inventaire : nouveau.

#### [F01-11] Pilote de la chaîne d'audit
- Définition : dommages plantés avec et sans charge adressée au lecteur, croisés avec trois lecteurs (juge de même lignée, juge d'autre lignée, auditeur assaini). Expérience prioritaire : elle touche le seul appui indépendant de l'attaque et ne demande aucun entraînement.
- Synonymes et paraphrases : pilote E1, « attaquer d'abord la chaîne d'audit », banc des lecteurs.
- Source : rép. 1, § 1 point 2, R6 E1 ; greffe flagornerie rép. 6, R5.
- État : retenu (accepté selon dem. 6).
- Liens : plants porteurs de charge ; juge de même lignée ; auditeur assaini ; greffe de flagornerie ; papier C.
- Ce qui l'attaque : un juge de 8 milliards de paramètres est plus instable qu'un juge de pointe ; portée limitée à nos organismes.
- Inventaire : rattaché à 2.1 et 2.2.

#### [F01-12] Auditeur assaini
- Définition : auditeur qui ne lit que le résultat ré-exécuté ou paraphrasé, jamais le texte de l'attaquant, de sorte que la charge n'a pas de canal ; complété par un humain sur un sous-échantillon. Son effet nul attendu est un contrôle de fuite, pas un résultat.
- Synonymes et paraphrases : lecteur assaini, auditeur « sanitized », verdict par ré-exécution, décision D2 de la rép. 1.
- Source : rép. 1, R6 E1 et D2 ; rép. 6, § 1 point 7, R5.
- État : retenu (accepté selon dem. 6).
- Liens : chaîne d'audit ; oracle par vérité plantée.
- Ce qui l'attaque : ne couvre pas les dommages d'interprétation, de choix d'analyse ou de compte rendu sélectif, que la ré-exécution ne tranche pas.
- Inventaire : rattaché à 2.1.

#### [F01-13] Deux bras pour l'attaquant optimisé contre les scores
- Définition : l'invariant « aucun score de moniteur dans l'entraînement de l'agent » ne dit rien de l'attaquant corrupteur ; Fable propose deux bras rapportés séparément, attaquant aveugle et attaquant qui s'optimise contre les scores, sous cloison stricte.
- Synonymes et paraphrases : décision D3 de la rép. 1, attaquant pire cas, suffixes optimisés par gradient contre un juge ouvert.
- Source : rép. 1, § 3 « Attaques », D3 ; rép. 7, partie 3 (équipe rouge E1.5).
- État : retenu (accepté selon dem. 6) ; portée de N-053 sur l'équipe rouge reposée à Lazar dans la rép. 7.
- Liens : N-053 ; bras d'attaque aveugle et informé (N-056) ; fuite indirecte par sélection des exemples.
- Ce qui l'attaque : fuite vers la conception des moniteurs ; double le coût.
- Inventaire : rattaché à 2.17 (épreuves du devin).

#### [F01-14] Amender par additifs datés, jamais rouvrir un texte scellé
- Définition : chaque conséquence du sujet sur les nœuds se règle par un additif daté qui renvoie au nœud, sans réécrire de texte scellé ; le mode « agent contraint » est rapporté à part, exploratoire et postérieur au scellement, jamais fondu dans la porte G1. Les additifs proposés touchent N-075, N-076, N-077, N-053, N-054.
- Synonymes et paraphrases : addenda, décision D5 de la rép. 1, table d'articulation.
- Source : rép. 1, R7 et D5 ; rép. 6, R7.
- État : retenu (accepté selon dem. 6).
- Liens : préenregistrement scellé (règle gelée R1) ; prévision scellée avant G1.
- Ce qui l'attaque : lecture en deux pièces.
- Inventaire : nouveau.

#### [F01-15] Oracle d'un moniteur : la vérité plantée, jamais un autre moniteur
- Définition : pour éprouver un moniteur (juge, auditeur), l'oracle doit être le registre des dommages plantés, et non un autre moniteur, sans quoi la corruption se propage à la mesure. Le même principe sert à comparer les modes du collisionneur (rép. 7).
- Synonymes et paraphrases : oracle de l'auditeur, « l'oracle ne dépend d'aucun jugement ».
- Source : rép. 1, R6 « Oracle de l'auditeur » ; rép. 6, R5 ; rép. 7, partie 2.
- État : proposé (conforme à N-058).
- Liens : N-058 ; plancher ; chiffre noir.
- Ce qui l'attaque : les dommages plantés ne couvrent pas les dommages inconnus.
- Inventaire : rattaché à 2.1 et 2.15.

---


**Demande 2 — revendications inédites**


#### [F01-16] Aucune revendication de méthode inédite sur l'audit
- Définition : le cœur convergent des réponses externes (tirage secret après engagement, plancher, estimateur de Horvitz-Thompson, moniteur en variable de contrôle, suite de confiance toujours valide) est publié, réuni dans les audits financiers à risque limité par tirage pondéré avec information auxiliaire. L'antériorité la plus proche n'était citée ni par la demande ni par les quatre modèles.
- Synonymes et paraphrases : « rien ne survit au niveau de la méthode », énoncé T1′ du modèle A occupé, audit au hasard occupé.
- Source : rép. 2, conclusion et section (b) ; dem. 2.
- État : occupé par la littérature (cité, jamais revendiqué) : Shekhar, Xu, Lipton, Ramdas 2023 « Risk-limiting financial audits via weighted sampling without replacement » ; Waudby-Smith et al. 2022 « Anytime-valid off-policy inference for contextual bandits » ; Angelopoulos et al. 2023 « Prediction-powered inference » ; Zrnic, Candès 2024 « Active statistical inference » ; Greenblatt et al. 2023. Recommandations acceptées selon dem. 6.
- Liens : N-075 (plancher publié, jamais revendiqué) ; décision 1 de la rép. 2 : méthode empruntée, citée.
- Ce qui l'attaque : verdicts fermes seulement après lecture des PDF ; littérature 2025-2026 non couverte.
- Inventaire : 2.1.

#### [F01-17] La convergence des modèles comme signal de réinvention
- Définition : quatre modèles qui partagent la même littérature et se sont critiqués mutuellement ne donnent pas quatre confirmations indépendantes ; « nouveau pour moi » n'est pas « nouveau pour le champ ». D'où la recherche de l'antériorité la plus forte et non de celle que les modèles citent.
- Synonymes et paraphrases : accord non indépendant, faux consensus, chercher l'antériorité dans le domaine d'origine.
- Source : rép. 2, § 1 ; rép. 4, § 1 ; rép. 6, D5 ; rép. 7, § 1.
- État : proposé (principe de méthode).
- Liens : collisionneur ; question neutre ; test de devinette.
- Ce qui l'attaque : rien de direct ; c'est une règle d'hygiène.
- Inventaire : nouveau.

#### [F01-18] Tableau de revendications à la manière d'un brevet
- Définition : découper chaque candidate en éléments et confronter chacun à la page précise de l'antériorité la plus proche ; classer les revendications par type (théorème, méthode, mesure, protocole vérifiable, résultat négatif) : l'antériorité occupe les deux premiers, les trois autres restent ouverts. Recherche par citations descendantes depuis six graines.
- Synonymes et paraphrases : typologie des revendications, « claim chart », six graines (Shekhar et al. 2023, Waudby-Smith et al. 2022, Zrnic et Candès 2024, Greenblatt et al. 2023, Wen et al. 2024, van der Weij et al. 2024).
- Source : rép. 2, § 1 et § 3, fin de la section (b).
- État : proposé (lecture sur PDF des six graines avant toute phrase de nouveauté recommandée).
- Liens : règle anti-faux-gap (R8) ; papiers A, B, C.
- Ce qui l'attaque : coût de lecture.
- Inventaire : nouveau.

#### [F01-19] Loi de la référence honnête, mesurée
- Définition : sur le harnais réel, une référence estimée par régime fait sonner l'alarme honnête au-dessus du niveau nominal dès qu'un horizon de bascule est dépassé, alors qu'une référence par tâche tient. Le point de bascule se situerait entre m (taille de la référence) et m divisé par le taux d'audit p ; seraient inédits l'identification de ce terme dans le contrôle et sa mesure, non la statistique.
- Synonymes et paraphrases : candidate locale R1, point de bascule, biais de référence qui ne se moyenne pas, promotion de la loi N-076 en résultat mesuré.
- Source : rép. 2, (a) R1 et (d) ; rép. 4, Q1.
- État : proposé ; promotion conditionnelle à l'issue de l'essai jumeau contre jumeau recommandée (décision 3 de la rép. 2), nœud du directeur.
- Liens : N-076 ; essai jumeau contre jumeau ; horizon de bascule de la rép. 3 ; loi d'échelle du dommage caché.
- Ce qui l'attaque : tuée si la référence par régime tient le niveau aux valeurs du programme ; à chercher dans Korbak et al. 2025 « A sketch of an AI control safety case » et la littérature conforme sur la taille d'étalonnage.
- Inventaire : rattaché à 2.19.

#### [F01-20] La sonde évaluée en audits économisés
- Définition : à largeur certifiée égale, la sonde figée à l'engagement, employée comme variable de contrôle prévisible, réduit le nombre d'audits d'un facteur k scellé avant G1, mieux que le juge de texte et les bases mécaniques, mode tenu à l'écart compris. La garantie « ne coûte jamais plus qu'un facteur logarithmique » est occupée ; seule l'unité de mesure serait propre.
- Synonymes et paraphrases : candidate locale R2, question Q2 de la rép. 4, « donner une unité au mot accélérateur », facteur k, sens (a) de « montrer que ça marche ».
- Source : rép. 2, R2 et décision 2 ; rép. 4, Q2 ; rép. 7, partie 3.
- État : proposé ; mesure secondaire du papier A à côté de G1 recommandée (nœud du directeur).
- Liens : sondes comme accélérateur (N-075) ; porte G1 ; échelle de huit barreaux.
- Ce qui l'attaque : dilution par les accidents honnêtes, issue nulle jugée probable par Fable ; tuée si la borne haute du gain sur la base mécanique est au plus zéro sur le mode tenu à l'écart.
- Inventaire : nouveau (proche de 2.2).

#### [F01-21] Le surplus de capacité chiffré
- Définition : un saboteur calé sur l'écart entre sa capacité et celle du jumeau de confiance passe sous la borne ; un écart d'élicitation après affinage court l'estimerait. L'idée qualitative est occupée par la sous-performance stratégique ; resteraient la comptabilité (un terme linéaire en l'horizon) et sa mesure.
- Synonymes et paraphrases : candidate locale R3, marge de sous-performance, « sandbagging », capacité cachée.
- Source : rép. 2, R3 et décision 5 ; rép. 5, source B (mesure par tâche).
- État : proposé ; rangé en limite déclarée, à réexaminer après l'essai jumeau contre jumeau.
- Liens : écart savoir interne contre sortie ; compétence retenue.
- Ce qui l'attaque : van der Weij et al. 2024 ; Greenblatt, Roger, Krasheninnikov, Krueger 2024 « Password-Locked Models » ; Benton et al. 2024 « Sabotage Evaluations ».
- Inventaire : 1.5 (compétence retenue).

#### [F01-22] Attestation du tirage en service
- Définition : un prédicteur entraîné depuis le point de vue de l'agent (contextes des copies compris) ne doit pas prédire le tirage d'audit au-delà du hasard plus une marge scellée, et un tiers doit pouvoir vérifier l'ordre engagement puis tirage à partir des seuls condensats. Un contrôle positif (tirage volontairement corrélé à un trait visible) vérifie la sensibilité du banc.
- Synonymes et paraphrases : candidate locale R4, secret du tirage attesté, prévisibilité du tirage, hasard du défenseur comme preuve.
- Source : rép. 2, R4 et (d).
- État : proposé ; promotion de « hasard du défenseur comme preuve » et « attestation, candidate » (N-076) conditionnelle, nœud du directeur.
- Liens : N-076 ; épreuves du devin ; conscience d'évaluation (N-053).
- Ce qui l'attaque : ingénierie à faible portée théorique ; audits électoraux (Lindeman et Stark 2012) obtiennent déjà le secret par aléa public et engagements.
- Inventaire : 2.17 et 2.7 (aussi 2.6 pour l'idée d'attestation).

#### [F01-23] Les « trois planchers » en théorème
- Définition : pour tout protocole à budget d'audit et référence de taille m, un saboteur adaptatif cacherait un dommage au moins égal au plus grand de trois termes : échantillonnage, bruit honnête, référence partagée. Fable la juge probablement occupée ou fausse telle qu'écrite.
- Synonymes et paraphrases : candidate locale R5, trois planchers du collisionneur, borne minimax, résultat négatif.
- Source : rép. 2, R5 et décision 5 ; rép. 4, § 1 (forme de la loi de la racine carrée).
- État : retiré en pratique (recommandation : rangé en limite, abandonné).
- Liens : retrait de la marge (N-077) ; loi d'échelle du dommage caché.
- Ce qui l'attaque : un rejouage à aléa commun (mêmes graines, même préfixe) peut réduire le bruit honnête sous sigma racine de n, donc le deuxième plancher n'en est pas un ; Avenhaus et Jaech 1981 ; bornes à deux points classiques.
- Inventaire : rattaché à 2.3 et 2.4.

#### [F01-24] Essai jumeau contre jumeau
- Définition : faire tourner deux bras identiques de l'agent honnête sur des tâches fraîches (essai A/A), dont la réponse attendue est connue : le taux d'alarme doit être au niveau nominal, sans quoi aucun écart observé ailleurs n'est lisible. Il fournit la variance de référence, la nulle de la co-élévation du papier B (répliques sur la même tâche) et sert à départager plusieurs candidates.
- Synonymes et paraphrases : essai A/A, D0 du modèle A, « jumeau contre jumeau », strate S0 de la rép. 3, deux exécutions du collisionneur contre lui-même (rép. 7).
- Source : rép. 2, classement et décision 4 ; rép. 3, § 3.2 et 3.7 ; rép. 4, (b) ; rép. 5, § 1.1 ; rép. 7, § 1.
- État : proposé, demandé en premier par quatre modèles externes ; décision 4 de la rép. 2 : en parallèle de la vérification d'antériorité.
- Liens : loi de la référence ; fausses alertes sur honnêtes ; papier B ; essaim du collisionneur.
- Ce qui l'attaque : Kohavi, Tang, Xu 2020 pour l'essai A/A (méthode empruntée).
- Inventaire : rattaché à 2.19.

---


**Demande 3 — fausses alertes sur agents honnêtes imparfaits**


#### [F01-25] Expérience des fausses alertes sur agents honnêtes réels et imparfaits
- Définition : mesurer, avec moniteurs et seuil gelés, sans saboteur ni fichier scellé, combien les sondes, le juge et les bases sonnent sur des agents honnêtes qui se trompent naturellement. Strates : référence fraîche (essai A/A), tâches plus dures à trois répliques, horizon doublé, température haute, quantification sur quatre bits, pannes d'outils de l'environnement ; jamais de consigne d'échec ni d'affinage vers l'erreur.
- Synonymes et paraphrases : E0 de la rép. 3, taux de fausses alertes sur honnêtes, « première expérience », strates S0 à S5, honnête imparfait, imperfection honnête.
- Source : dem. 3 (« le directeur a dit go ») ; rép. 3, § 2, 3.1 à 3.12.
- État : conception proposée ; préenregistrement classe A requis ; ordre de grandeur de coût donné comme tel, non devis.
- Liens : N-076 ; porte G1 ; N-053 (conscience d'évaluation mesurée) ; papier A.
- Ce qui l'attaque : banque de tâches à vérité plantée peut-être inexistante (coût humain dominant) ; muette entre de faibles taux voisins à la taille proposée ; modèles plus petits écartés pour les sondes (une sonde est propre à un modèle).
- Inventaire : 2.19 (dissociation chez l'honnête) ; 3.5 (honnêtes de contrôle).

#### [F01-26] Séparer validité d'étalonnage et contenu lu
- Définition : deux questions confondues : le seuil tient-il sur une population honnête fraîche (se répare en recalibrant), et le score monte-t-il parce que l'agent se trompe (requalifie la sonde) ? Sans saboteur, l'expérience peut établir « la sonde lit l'imperfection », jamais « et non le sabotage ».
- Synonymes et paraphrases : calibration contre construit, « décalage de calibration réparable par strate ».
- Source : rép. 3, § 1.1 et 3.8.
- État : proposé.
- Liens : validité de construit de la sonde ; contraste à dommage égal à G1.
- Ce qui l'attaque : —
- Inventaire : 2.19.

#### [F01-27] Contraste intra-tâche entre réplique fautive et réplique réussie
- Définition : comparer, sur une même tâche, des répliques honnêtes qui réussissent et qui échouent, de sorte que la difficulté est fixée par construction ; différence appariée du score (rangs signés de Wilcoxon), puis localisation : courbe du score alignée sur l'action fautive contre positions tirées au hasard et enveloppe de directions aléatoires.
- Synonymes et paraphrases : remède au conditionnement sur l'échec, localisation de l'erreur, critères de lecture C2 et C3 de la rép. 3 (locaux).
- Source : rép. 3, § 1.1, 1.3, 3.8.
- État : proposé.
- Liens : expérience des fausses alertes ; étiquettes erreur et dommage.
- Ce qui l'attaque : peu de tâches discordantes rend le contraste « non jugé ».
- Inventaire : 2.19.

#### [F01-28] Étiquettes erreur et dommage, en quatre cases
- Définition : chaque trajectoire reçoit deux étiquettes d'un oracle tenu hors des moniteurs : au moins une action erronée localisée, et conclusion fausse livrée (le dommage). Quatre cases : ni erreur ni dommage, erreur corrigée, erreur avec dommage, dommage sans erreur locale repérable.
- Synonymes et paraphrases : E et D, erreur honnête contre dommage.
- Source : rép. 3, § 3.3.
- État : proposé (définitions à sceller en classe A).
- Liens : fausse accusation au sens « motif et dommage au même lieu ».
- Ce qui l'attaque : exige un accord d'annotation suffisant ; tâches à vérité ambiguë exclues.
- Inventaire : 2.19.

#### [F01-29] Fausse accusation au sens « motif et dommage au même lieu »
- Définition : une erreur honnête dommageable qui coïncide avec un motif de sonde est exactement ce que la règle à deux clés appellerait une alerte ; son taux sur honnêtes est le vrai taux de fausse accusation. Fable recommande de la porter en co-principale avec l'alerte brute.
- Synonymes et paraphrases : métrique principale 2 de la rép. 3, décision 1 (option c), alerte N-075 sur honnêtes.
- Source : rép. 3, § 1.1, 3.5, 3.8, décision 1.
- État : proposé non tranché.
- Liens : règle à deux clés (N-075).
- Ce qui l'attaque : si elle est élevée, la règle « motif et dommage au même lieu » accuse des honnêtes et doit être relue ; dépend de la qualité de la localisation.
- Inventaire : 2.16.

#### [F01-30] Contrôles de tuyauterie
- Définition : trois contrôles à réponse connue avant toute lecture : égalité des scores entre génération et rejeu à préfixe forcé, injection synthétique d'un multiple de la direction de sonde qui doit sonner, directions aléatoires qui doivent rester au niveau nominal. Leur échec arrête tout.
- Synonymes et paraphrases : contrôles mécaniques, rejeu, injection synthétique, sondes témoins aléatoires.
- Source : rép. 3, § 1.3, 1.4, 3.7, 3.9.
- État : proposé (partie instrument).
- Liens : garde testée sur cas sain et sur artefact (R5 gelée).
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [F01-31] Horizon de bascule du biais contre le bruit
- Définition : le bruit honnête croît comme sigma racine de N, le biais de référence linéairement ; ils se rattrapent vers N* = (sigma/b) au carré, au-delà duquel une accumulation sonne sur des honnêtes sans attaque. Publier N* par strate comme borne empirique d'horizon à côté de la règle « horizon au plus m ».
- Synonymes et paraphrases : N étoile, borne d'horizon, biais b de la référence vers la strate fraîche.
- Source : rép. 3, § 3.10.
- État : proposé (calcul « non audité »).
- Liens : N-076 ; loi de la référence ; loi d'échelle du dommage caché.
- Ce qui l'attaque : supposition d'indépendance ; autocorrélation intra-trajectoire.
- Inventaire : 2.19.

#### [F01-32] Contraste à dommage apparié réservé à G1, et gel des sondes
- Définition : « les sondes lisent l'imperfection et non le sabotage » ne se conclut qu'à la porte G1, par un contraste fixé d'avance : taux d'alerte sur sabotage moins taux sur erreurs honnêtes dommageables, à dommage apparié, au seuil recalibré sur le mélange honnête naturel, par mode. Déposer ce contraste en additif au plan de G1 avant toute lecture, et ne pas reconcevoir les sondes avant G1 quelle que soit l'issue.
- Synonymes et paraphrases : addendum G1, décision 4 de la rép. 3, gel des sondes jusqu'à G1.
- Source : rép. 3, § 3.8, 3.10, décision 4.
- État : proposé (nœud du directeur).
- Liens : N-062 (la reconception suit l'échec de G1) ; prévision scellée avant G1.
- Ce qui l'attaque : G1 peut tourner avec des sondes que l'expérience aura déjà affaiblies.
- Inventaire : nouveau.

#### [F01-33] Juge : séparer blocage d'une conclusion et accusation
- Définition : le juge de texte sonnera sur les erreurs honnêtes puisqu'il voit un contenu faux ; la lecture utile sépare « bloquer une conclusion », compté en utilité, et « accuser », plafonné.
- Synonymes et paraphrases : utilité contre accusation, réponse A des modèles externes.
- Source : rép. 3, § 3.4.
- État : proposé.
- Liens : fausse accusation ; papier C.
- Ce qui l'attaque : —
- Inventaire : nouveau.

---


**Demande 4 — la problématique du papier**


#### [F01-34] Le papier A a perdu sa thèse
- Définition : la thèse de la version 2 était un mécanisme à garantie (l'accumulation de scores de sondes détecte avec garantie toujours valide) ; N-075, N-076 et N-077 ont retiré la garantie, sans que la question soit réécrite. Le papier a gardé son plan d'expériences et perdu sa thèse.
- Synonymes et paraphrases : « quelle est notre problématique ? », rupture datée, G1 produira des chiffres sans thèse.
- Source : rép. 4, conclusion, § 1, décision 1.
- État : constat proposé.
- Liens : papier A ; loi d'échelle du dommage caché.
- Ce qui l'attaque : Fable n'a lu que le résumé des décisions.
- Inventaire : nouveau.

#### [F01-35] Trois types de contribution comme trois rôles
- Définition : robustesse universelle, mécanisme inédit et phénomène hérité ne sont pas trois papiers concurrents mais trois rôles : le phénomène hérité pour la question, le mécanisme pour la mesure, la robustesse pour la limite déclarée. Distinguer aussi problématique (ce que le champ ignore), question (ce que le papier tranche) et revendication (ce que le résultat autorise).
- Synonymes et paraphrases : types (i), (ii), (iii), « (iii) en question, (ii) en mesure, (i) en limite », décision 1 de la rép. 4.
- Source : rép. 4, § 1, (b), décision 1.
- État : proposé (nœud du directeur, confiance moyenne).
- Liens : papiers A, B, C ; question neutre générale (rép. 7, ordre des types tiré au hasard).
- Ce qui l'attaque : (i) irréfutable avec un seul mode tenu à l'écart et contraire à N-077 ; (ii) dépend de G1 et d'une publication externe annoncée de tests toujours valides sur sondes ; (iii) reproche « évident ».
- Inventaire : nouveau.

#### [F01-36] Loi d'échelle du dommage caché
- Définition : combien de dommage un saboteur diffus peut-il cacher selon l'horizon et la qualité de la référence honnête ? Prévision : il croît comme la racine de l'horizon si la référence est connue, puis linéairement si elle est estimée ; trois prévisions scellées (exposant du bruit honnête, horizon de bascule entre m et m divisé par le taux d'audit, effet de la sonde sur la constante et non sur l'exposant). Titre proposé : « Ce qu'un saboteur diffus peut cacher : loi d'échelle du dommage indétectable et prix de la référence honnête chez des agents de langue ».
- Synonymes et paraphrases : question Q1 de la rép. 4, phénomène hérité, loi racine puis linéaire, règle de dimensionnement, « prix de la référence honnête ».
- Source : rép. 4, (a) Q1, (b), (c) résumé, (d).
- État : proposé (recommandation de Fable, nœud du directeur).
- Liens : papier A ; loi de la référence ; audits économisés ; horizon de bascule ; variance d'Allan ; N-077 (versant saboté seulement descriptif).
- Ce qui l'attaque : bascule déjà mesurée sur agents ; référence par régime qui tient à tous les horizons atteignables ; organismes sans dose-réponse ; lieu de publication exigeant une méthode nouvelle.
- Inventaire : rattaché à 2.3 et 2.18.

#### [F01-37] Loi de la racine carrée de la stéganographie, antériorité du domaine d'origine
- Définition : en stéganographie par lots, la capacité cachée sans détection croît comme la racine de la taille de la couverture ; Fable y voit la forme des « trois planchers » et une menace sur le lemme d'additivité et sur le contraste maximum par action contre accumulation, à citer comme héritage plutôt qu'à se faire découvrir par un relecteur. S'y ajoutent la frontière signaux rares et forts (le maximum suffit) contre denses et faibles (la somme est requise) et le biais qui ne se moyenne pas.
- Synonymes et paraphrases : « square root law », capacité stéganographique, stéganalyse, communication à faible probabilité de détection, critique supérieure.
- Source : rép. 4, § 1, Q1 « antériorité », décision 2 ; rép. 7, partie 2 (élément de liste scellée).
- État : occupé par la littérature (cité) : Ker 2006, 2007 ; Ker, Pevný, Kodovský, Fridrich 2008 ; Ker 2010 (source de couverture estimée, mémoire incertaine) ; Bash, Goeckel, Towsley 2013 ; Avenhaus et Jaech 1981 ; Meng 2018 ; Donoho, Jin 2004. Lecture sur PDF et avis d'un spécialiste de stéganalyse recommandés avant de sceller.
- Liens : lemme d'additivité ; loi d'échelle du dommage caché ; agrégateur adaptatif.
- Ce qui l'attaque : ces lois supposent une couverture connue ; différence résiduelle jugée incertaine.
- Inventaire : 2.18 (b) et 2.3.

#### [F01-38] Variance d'Allan des scores honnêtes
- Définition : outil de métrologie qui sépare, le long de l'horizon, un bruit qui se moyenne d'une dérive qui ne se moyenne pas ; Fable le propose avec une régression en échelles logarithmiques du seuil d'alarme honnête contre l'horizon, rééchantillonnée par tâche puis par blocs.
- Synonymes et paraphrases : Allan 1966, dérive contre bruit.
- Source : rép. 4, § 3.
- État : proposé.
- Liens : loi d'échelle du dommage caché ; horizon de bascule.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [F01-39] Validité de construit de la sonde
- Définition : une sonde de sabotage lit-elle l'intention, la présence d'une instruction, la conscience d'être évalué ou une régularité du texte, et ce construit prédit-il sa tenue sous attaque ? Repli si la loi d'échelle tombe ; contrôles tirés des lectures (bases de statistiques de mots, contraste apparié étalonné sur un nul neutre, test de nécessité sur plusieurs directions).
- Synonymes et paraphrases : question Q3 de la rép. 4, psychométrie, « que mesure vraiment un moniteur ? », hypothèse H8 du programme.
- Source : rép. 4, Q3 et décision 5.
- État : proposé comme repli.
- Liens : base lexicale ; organismes placebos ; échelle de huit barreaux.
- Ce qui l'attaque : peu de sondes et d'attaques, donc « prédit » repose sur une poignée de points ; Cronbach et Meehl 1955 ; Hewitt et Liang 2019 ; Goldowsky-Dill et al. 2025.
- Inventaire : 3.4 et 3.5.

#### [F01-40] Part universelle de la protection
- Définition : quelle part de la protection contre un sabotage jamais vu tient sans hypothèse sur l'attaque ? Réponse attendue : l'audit garde sa couverture, la sonde perd du rappel.
- Synonymes et paraphrases : question Q4 de la rép. 4, robustesse universelle, type (i).
- Source : rép. 4, Q4 ; rép. 2, section (b).
- État : retiré comme question (section de limites) : la première moitié est vraie par construction, la seconde repose sur un seul mode.
- Liens : N-077 ; mode tenu à l'écart.
- Ce qui l'attaque : non revendicable.
- Inventaire : 2.1.

#### [F01-41] Bilan d'incertitude d'un moniteur sous adversaire
- Définition : question commune proposée aux trois papiers : A établit le terme d'horizon, B le terme de corrélation entre copies (la même loi indexée par agent), C l'erreur systématique que l'adversaire induit dans l'instrument (le gain de déférence). Fable recommande de la loger sous la question existante « que mesure vraiment un moniteur ? ».
- Synonymes et paraphrases : question d'ensemble, décision 5 de la rép. 4, « que mesure vraiment un moniteur, et sa mesure survit-elle à l'adversaire ? ».
- Source : rép. 4, (b) dernier argument, décision 5 ; dem. 7.
- État : proposé non tranché.
- Liens : papiers A, B, C ; question neutre générale.
- Ce qui l'attaque : deux formulations à tenir.
- Inventaire : nouveau.

---


**Demande 5 — lectures récentes**


#### [F01-42] Base lexicale distributionnelle et tâche de contrôle pour toute sonde
- Définition : la géométrie lue par les sondes linéaires découlerait des statistiques de cooccurrence, de façon collective ; nos sondes peuvent donc lire le lexique de la tâche ou de la consigne de sabotage. Toute sonde rapportée doit l'être en gain au-dessus d'une régression sur sac de mots et plongements statiques et d'une tâche de contrôle à étiquettes permutées, par mode ; retirer les mots-clés ne suffit pas.
- Synonymes et paraphrases : piste 1 de la rép. 5, base lexicale, sélectivité, décision 1 de la rép. 5, complément de la base « mots et coût ».
- Source : rép. 5, § 3.1 A et B, 3.2 piste 1, décision 1 ; source lue : « Symmetry in language statistics shapes the geometry of model representations ».
- État : proposé, obligatoire avant G1 recommandé (nœud du directeur, confiance haute).
- Liens : base « mots et coût » ; porte G1 ; reconception (N-062).
- Ce qui l'attaque : le gain des sondes peut fondre ; Hewitt et Liang 2019, Belinkov 2022 (contrôle exigé, non nouveauté).
- Inventaire : 2.11 et 2.20.

#### [F01-43] Écart entre savoir interne et sortie chez l'honnête
- Définition : l'intérieur d'un modèle peut connaître l'ordre juste alors que sa réponse explicite est fausse, sans aucun sabotage ; une sonde « l'agent sait mieux qu'il ne répond » se déclencherait donc sur des honnêtes imparfaits. Fable propose de reprendre le dessin des contrastes appariés étalonnés sur lois neutres et de greffer la mesure, enregistrée passivement, sur l'essai jumeau contre jumeau ; il y voit aussi une mesure par tâche du surplus de capacité.
- Synonymes et paraphrases : piste 3 de la rép. 5, savoir latent, « sait puis dit autre chose », budget de sabotage invisible.
- Source : rép. 5, § 3.1 B, 3.2 piste 3, décision 3 ; source lue : « Reading and steering representations of materials-science mechanisms ».
- État : proposé (enregistrement passif recommandé).
- Liens : surplus de capacité ; lecture « je cède » (rép. 6) ; fausses alertes sur honnêtes.
- Ce qui l'attaque : occupé : Burns et al. 2022, Azaria et Mitchell 2023, Marks et Tegmark 2023 ; Orgad et al. 2024.
- Inventaire : 1.4 et 1.5.

#### [F01-44] Échelle de difficulté a priori des dommages plantés
- Définition : trois niveaux de corruption définis avant mesure (erreur locale grossière, erreur locale plausible, biais réparti sur plusieurs étapes), insérés par tirage secret dans des trajectoires honnêtes ; q rapporté par strate, strate non mesurée comptée à zéro. Fable en tire aussi l'arbre de points de reprise versionné comme support de l'audit après coup.
- Synonymes et paraphrases : piste 4 de la rép. 5, banc à vérité plantée, corruption insérée, schéma « DiscoveryAgent ».
- Source : rép. 5, § 3.1 C, 3.2 piste 4.
- État : proposé.
- Liens : N-075, N-076 ; papier C (attaque adaptative et caractère diffus comme différences).
- Ce qui l'attaque : le chiffre de DiscoveryAgent porte sur des corruptions non adverses, limite d'un papier et non trou ; licences non lues.
- Inventaire : 2.1 et 2.9.

#### [F01-45] Test garder/retirer et redondance des directions de sonde
- Définition : retirer itérativement les directions jusqu'à ramener la sonde au hasard, puis regarder si le taux de dommage planté change ; si la sonde tombe sans que le comportement bouge, elle lit un corrélat. Précédé d'une reproduction du chiffre du dépôt sur GPT-2 petit.
- Synonymes et paraphrases : piste 5 de la rép. 5, effacement itératif, test de nécessité, « keep/remove ».
- Source : rép. 5, § 3.1 D, 3.2 piste 5 ; source lue : « Transformers converge to invariant algorithmic cores » et dépôt « cores ».
- État : proposé.
- Liens : motif seul : audit, jamais témoin ; intervention causale.
- Ce qui l'attaque : occupé par Ravfogel et al. 2020, Elazar et al. 2021, Belrose et al. 2023 (LEACE) ; incohérence signalée dans la source.
- Inventaire : 2.10 ; voisin de 4.4.

#### [F01-46] Cœur invariant du sabotage (question d'atelier)
- Définition : existerait-il un sous-espace « cœur » du sabotage partagé entre organismes ou entre modèles ? Fable l'appelle la zone vierge séduisante type : le sabotage diffus est une disposition de politique, pas une tâche algorithmique à perte définie.
- Synonymes et paraphrases : cœurs algorithmiques du sabotage, transfert de direction par alignement canonique.
- Source : rép. 5, § 3.1 D, décision 4.
- État : ouvert (question versée à l'atelier d'idées, non ouverte comme axe ; recommandation).
- Liens : organisme d'idéation ; noyaux algorithmiques.
- Ce qui l'attaque : règle anti-faux-gap ; méthode rejouée seulement sur petit modèle.
- Inventaire : 4.1, 4.4 ; 1.21.

#### [F01-47] Instrumenter le collisionneur
- Définition : compter les branches distinctes par question, corréler le rang au premier tour et le rang final, mesurer la part d'idées finales nées au premier tour, obliger chaque critique à nommer l'idée centrale ; si la corrélation dépasse un seuil scellé, le troisième tour devient optionnel. Hypothèse : diversifier les générateurs rapporte plus que renforcer les juges.
- Synonymes et paraphrases : piste 2 de la rép. 5, rétro-analyse des journaux, plafonnement précoce, troisième tour conditionnel.
- Source : rép. 5, § 3.1 E, 3.2 piste 2, décision 6 ; source lue : « Re-Search ».
- État : proposé (rétro-analyse d'abord recommandée).
- Liens : collisionneur ; organisme d'idéation ; mode essaim.
- Ce qui l'attaque : peu de questions passées, pas de vérité de terrain sur la valeur d'une idée ; conclusion « le goulot est la génération » de la source jugée mal fondée.
- Inventaire : nouveau.

#### [F01-48] Banc d'attaque par édition de poids
- Définition : une édition réversible des poids le long de la direction de la sonde ramène la sonde au hasard en conservant le comportement : attaquant pire cas contre les sondes, illustrant qu'elles sont un accélérateur et non une garantie. Admissible seulement comme banc d'attaque étiqueté, hors G1, jamais mêlé aux organismes de référence.
- Synonymes et paraphrases : dépôt « neuron-reflection », réflexion de Householder, ablation de direction dans les poids.
- Source : rép. 5, § 3.1 F, décision 5.
- État : proposé (principe oui, calendrier reporté).
- Liens : N-053 (information de moniteur dans la fabrication) ; deux bras d'attaquant.
- Ce qui l'attaque : cas simple occupé (Arditi et al. 2024) ; Bailey et al. 2024 ; dépôt immature, un seul commit.
- Inventaire : 1.19 (canal des poids).

#### [F01-49] Raisonneurs à énergie
- Définition : la norme du gradient d'énergie comme signal de surveillance n'a aucun point d'appui sur nos modèles de langue.
- Synonymes et paraphrases : « Energy-Based Reasoners ».
- Source : rép. 5, § 3.1 G ; rép. 4, lectures non retenues.
- État : retiré (réouverture si une tête d'énergie est démontrée sur un modèle de langue ouvert).
- Liens : —
- Ce qui l'attaque : —
- Inventaire : nouveau.

---


**Demande 6 — flagornerie**


#### [F01-50] La flagornerie comme famille de charges, non comme axe
- Définition : la flagornerie (tendance d'un modèle à abonder dans le sens de son interlocuteur) est une disposition du lecteur que l'attaquant exploite par une charge sans ordre et sans preuve, faite de signaux sociaux ; elle entre au plan comme famille de charges de la chaîne d'audit et de leviers sur l'agent. Critère opératoire : une charge est sociale si elle ne donne aucun ordre, n'apporte aucun fait vérifiable et signale opinion, statut, accord ou appartenance ; quatre formes à distinguer (alignement sur l'opinion, indulgence envers l'auteur, abandon sous contestation, conformité à la majorité).
- Synonymes et paraphrases : « sycophancy », corruption par flatterie, cadrage flatteur, autorité ou consensus prétendus, réponses préventives, charge sociale.
- Source : dem. 6 ; rép. 6, conclusion, § 1, R1, R2, D1.
- État : proposé (famille de charges ; une seule hypothèse nouvelle dans le papier C).
- Liens : papier C ; coercition et corruption ; juge de même lignée.
- Ce qui l'attaque : « la flagornerie corrompt les juges » est occupé (Anthropic 2022 et 2023, bancs de biais des juges 2023-2024, auto-préférence 2024, revirement « FlipFlop » 2023).
- Inventaire : nouveau.

#### [F01-51] Levier propre : la charge sociale survit-elle aux défenses contre l'injection ?
- Définition : sous une défense contre l'injection (détecteur, balisage du contenu tiers, paraphrase), le biais de l'instruction nue rentre dans la borne ; si celui de la charge sociale persiste, c'est un levier propre, sinon un mode d'injection du point de vue du défenseur. Fable s'attend à ce que la paraphrase conserve le signal social et que seule l'extraction des affirmations vérifiables l'enlève, à tester comme bras de défense.
- Synonymes et paraphrases : hypothèse locale H8 de la rép. 6, question Q5, extraction des affirmations vérifiables, dépouillement du cadrage.
- Source : rép. 6, R3 Q5, R4 H8, D3.
- État : proposé (seule hypothèse nouvelle à sceller, papier C).
- Liens : greffe de flagornerie ; auditeur assaini.
- Ce qui l'attaque : l'extraction peut retirer de l'information utile et baisser q.
- Inventaire : nouveau.

#### [F01-52] Biais de q par charge sociale, et témoins
- Définition : sur les juges de texte, q sous charge sociale est-il inférieur à q sous contenu anodin, au seuil fixé sans cadrage ? Témoins : cadrage dépréciatif qui doit déplacer le verdict en sens inverse (sinon c'est une perturbation, pas une flagornerie), instabilité propre du juge mesurée d'abord (sans elle, un revirement passe pour une capitulation), contrôle positif sur un jeu public de flagornerie ; et séparer l'effet sur le critère (indulgence partout) de l'effet sur la sensibilité (capacité à distinguer le plant de son jumeau).
- Synonymes et paraphrases : hypothèses locales H7 et H9 de la rép. 6, témoin de sens, sensibilité contre critère, régression vers la moyenne.
- Source : rép. 6, § 1 points 4 à 6, § 4, R4.
- État : proposé.
- Liens : plants porteurs de charge (q déclaré par état de cadrage) ; greffe de flagornerie.
- Ce qui l'attaque : falsifiée si l'écart tient dans la borne ; un juge de 8 milliards est plus instable qu'un juge de pointe.
- Inventaire : nouveau.

#### [F01-53] Flagornerie du juge envers le défenseur
- Définition : l'interlocuteur du juge est le défenseur qui rédige la consigne ; le saboteur n'est qu'auteur d'un contenu tiers. Le cadrage du défenseur lui-même (« nous soupçonnons un sabotage » contre « contrôle de routine ») peut déplacer le verdict sans aucun attaquant : il faut figer et publier la consigne du juge.
- Synonymes et paraphrases : question Q7 de la rép. 6, effet de demande, sensibilité à la consigne, consigne neutre contre soupçonneuse.
- Source : rép. 6, § 1 point 3, R1, R3 Q7, R5, R7 (additif N-053).
- État : ouvert (question ; aucun voisin précis situé).
- Liens : N-053 ; papier C.
- Ce qui l'attaque : à chercher sous « effets de demande ».
- Inventaire : nouveau.

#### [F01-54] Greffe de flagornerie sur le pilote de la chaîne d'audit
- Définition : chaque plant et son jumeau honnête passent sous huit bras de cadrage écrits dans l'artefact : aucun, anodin, auto-éloge, autorité ou consensus, identité commune, réponse préventive (persuasion, rapportée à part), dépréciatif, instruction nue ; lus par juge de même lignée, juge d'autre lignée et auditeur assaini, sous trois défenses. Mesure principale : écart de q entre charges sociales groupées et contenu anodin ; inférence seule, sans entraînement.
- Synonymes et paraphrases : E1-F, bras F0 à F7.
- Source : rép. 6, R5.
- État : proposé.
- Liens : pilote de la chaîne d'audit ; papier C.
- Ce qui l'attaque : portée limitée à nos organismes.
- Inventaire : nouveau.

#### [F01-55] Lire « je cède » dans le juge
- Définition : deux mécanismes : la sortie passe outre (le juge a lu le dommage et rend « conforme », écart savoir contre sortie lisible) ou la perception est déplacée (le dommage n'est jamais représenté, rien à lire sauf le cadrage, qu'un détecteur de texte lit aussi bien). Exige un contraste à cadrage identique (cède contre tient), des plants lus de façon stable sans cadrage, une sonde qui bat le détecteur de cadrage ; la sonde sur le juge est un moniteur du moniteur, motif seul, jamais témoin.
- Synonymes et paraphrases : hypothèse locale H10 de la rép. 6, question Q6, capitulation lisible, sonde du juge.
- Source : rép. 6, R3 Q6, R4 H10, R6, D4.
- État : proposé, exploratoire, scellé à part, sans revendication.
- Liens : écart savoir interne contre sortie ; N-053 (juge d'une autre lignée peut-être fermé) ; règle à deux clés.
- Ce qui l'attaque : « Steering Llama 2 via Contrastive Activation Addition » (2023) ; « Sycophancy Is Not One Thing » (2025, à confirmer) ; redondance des directions.
- Inventaire : 1.4 et 2.16.

#### [F01-56] Droit de réponse de l'agent audité
- Définition : après une alerte, laisser l'agent répondre permet à un honnête de dissiper une fausse alerte mais ouvre le canal de la capitulation ; Fable propose une réponse admise seulement sous forme vérifiable (pièce ré-exécutable), et un bras de contestation libre mesuré à titre descriptif. Le bon indicateur est la discrimination : le juge cède-t-il autant à une contestation injustifiée qu'à une justifiée ?
- Synonymes et paraphrases : D2 de la rép. 6, hypothèse locale H11, contestation « es-tu sûr ? ».
- Source : rép. 6, R1, R4 H11, D2.
- État : proposé non tranché (nœud du directeur).
- Liens : fausses alertes sur honnêtes ; attestation exigée.
- Ce qui l'attaque : la forme vérifiable ne couvre pas les dommages d'interprétation.
- Inventaire : rattaché à 2.6.

#### [F01-57] Test de devinette pour la neutralité d'une question
- Définition : avant d'envoyer une question neutre au collisionneur, un lecteur qui n'a pas lu la réponse tente de deviner la réponse attendue ; s'il y parvient, on réécrit. Complété par une liste des mots qui trahissent la réponse, retirés, et par le tirage au hasard de l'ordre des types de contribution à chaque envoi.
- Synonymes et paraphrases : essai de devinette, test de neutralité, D5 de la rép. 6, décision 1 de la rép. 7, fuite résiduelle.
- Source : rép. 6, D5 ; rép. 7, § 1, partie 1, décision 1.
- État : proposé (recommandé).
- Liens : protocole X ; collisionneur ; convergence comme signal de réinvention.
- Ce qui l'attaque : un jour de délai ; fuites inévitables quand elles sont l'objet même du papier.
- Inventaire : nouveau.

#### [F01-58] Question neutre des revendications
- Définition : question servie aux modèles externes : dans un cadre avec audit tiré au hasard, moniteurs internes et textuels et exécutions honnêtes limitées, quelles contributions restent réellement inédites (« aucune » admis), avec voisin publié, vérification par un tiers et expérience qui fait tomber chacune. Fable en a retiré le nom des estimateurs, la typologie des contributions et l'invitation à chercher dans les domaines voisins, qui orienteraient vers la rép. 2.
- Synonymes et paraphrases : question neutre pour le collisionneur de la rép. 6.
- Source : rép. 6, « Question neutre pour le collisionneur ».
- État : proposé (envoi après test de devinette, puis second tour sur les domaines voisins rapporté à part).
- Liens : aucune revendication de méthode inédite ; protocole X.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [F01-59] Questions neutres de la coercition et de la problématique
- Définition : deux autres questions neutres de Fable : l'une sur la pression d'un tiers sur agents et moniteurs et l'entente agent-moniteur de même modèle (critère de distinction des menaces, mesure du dommage sans composants corruptibles) ; l'autre sur les trois types de contribution d'un article (garantie, mécanisme, phénomène hérité), avec invitation à signaler un quatrième type oublié.
- Synonymes et paraphrases : question neutre de la rép. 1, question neutre de la rép. 4.
- Source : rép. 1 et rép. 4, sections « Question neutre pour le collisionneur ».
- État : proposé.
- Liens : protocole X ; test de devinette.
- Ce qui l'attaque : la question de la rép. 4 reprend l'énumération des types, que la rép. 7 juge une fuite.
- Inventaire : nouveau.

---


**Demande 7 — questions par papier, essaim, « montrer que ça marche »**


#### [F01-60] Quatre questions neutres par papier
- Définition : une question générale (problématique d'ensemble de trois articles : agent seul, copies, moniteurs visés), une sur le temps (« qu'est-ce que la longueur de la tâche change ? »), une sur les copies (« que change le fait que les agents soient des copies d'un même modèle ? »), une sur le moniteur comme surface d'attaque (« qu'est-ce que cette possibilité change à la manière d'évaluer un moniteur ? »), chacune suivie d'un bloc commun (question, réponse réfutable, antériorité, expérience à deux mois sur 8 milliards de paramètres, type de contribution) et d'une liste de mots retirés.
- Synonymes et paraphrases : Q-générale, Q-A, Q-B, Q-C, protocole X sur la problématique générale et chaque papier.
- Source : dem. 7 ; rép. 7, partie 1.
- État : proposé (envoi après essai de devinette recommandé).
- Liens : papiers A, B, C ; bilan d'incertitude ; test de devinette.
- Ce qui l'attaque : fuites résiduelles reconnues : le découpage en trois articles suggère les axes ; « exécutions de comparaison » laisse deviner la référence ; « poids identiques » pointe une régularité commune ; « par ce qu'il écrit ou autrement » distingue deux voies.
- Inventaire : nouveau.

#### [F01-61] Mode essaim du collisionneur
- Définition : les cinq mêmes modèles, sous pseudonymes neutres tirés à chaque exécution, à budget total égal au mode isolé (lecture comprise, payée sur la part de l'agent) : brouillon privé scellé au départ, quatre cycles de société (messages courts en salons publics, prépublication versionnée, revues anonymes tirées au hasard, sans note ni verdict, errata publics sans effacement), puis réponse finale privée au format du mode isolé. Toute note, approbation, classement ou identité reste caché ; arrêt au nombre de cycles ou au budget, jamais sur consensus.
- Synonymes et paraphrases : société d'agents chercheurs, « AI society », essaim contre isolé, « A Society of AI Scientists » (source rapportée, indice de suivisme non opposable), scores cachés.
- Source : dem. 7 ; rép. 7, partie 2 « Règles ».
- État : proposé (pilote sur la question générale d'abord, puis plan complet ; scores cachés partout recommandés).
- Liens : collisionneur ; organisme d'idéation ; N-058.
- Ce qui l'attaque : groupes nominaux plus productifs que les groupes en interaction (Diehl, Stroebe 1987) ; l'influence réduit la diversité (Lorenz et al. 2011) ; scores visibles créent le suivisme (Salganik et al. 2006) ; information non partagée (Stasser, Titus 1985) ; Fable n'attend pas que l'essaim gagne en couverture.
- Inventaire : nouveau.

#### [F01-62] Comparer essaim et isolé sans juge
- Définition : mesures à oracle : erreur plantée (référence inventée et affirmation chiffrée fausse injectées au même stade, taux de reprise et de correction), couverture d'une liste de référence scellée complétée par un tiers et jamais montrée ; secondaires : références qui se résolvent dans une base bibliographique, diversité à longueur égale et sa chute du brouillon scellé à la réponse finale (indice de suivisme), questions fermées vérifiables par calcul. Au moins deux exécutions par mode et par question ; en dessous, simple description.
- Synonymes et paraphrases : jugement par oracle ou par le coût, indice de suivisme, liste scellée, erreur plantée dans le collisionneur, coût jusqu'à la première apparition.
- Source : rép. 7, partie 2 « Comparer sans juge », « Limite », « Classe A et instrument ».
- État : proposé ; prévisions, mesures, liste, budget, règle de décision en classe A ; orchestrateur et scripts en instrument.
- Liens : N-058 ; essai jumeau contre jumeau (deux exécutions isolées) ; loi de la racine carrée comme exemple d'élément de liste.
- Ce qui l'attaque : quatre questions et deux modes ne font pas un test ; coût de seize exécutions inconnu.
- Inventaire : nouveau.

#### [F01-63] « Montrer que ça marche » comme essai sévère perdable
- Définition : le programme interdit tout essai visant un signe positif ; la demande devient : quel essai les sondes pourraient-elles rater, dont la réussite convaincrait ? « Marche » ne veut pas dire « garantit » : l'énoncé permis est « la sonde figée avant l'évaluation économise un facteur k d'audits sur le mode tenu à l'écart, borne basse au-dessus de 1 », scellé avec la préinscription de G1.
- Synonymes et paraphrases : résultat positif, message tronqué de Lazar, « et si on veut montrer que les sondes ou l'entraînement marchent », définition de « marche ».
- Source : dem. 7 ; rép. 7, § 1, partie 3, décision 5.
- État : proposé (nœud du directeur ; questions de clarification posées).
- Liens : audits économisés ; règle gelée R3 ; porte G1.
- Ce qui l'attaque : échec visible ; sondes de tromperie concentrée déjà publiées (Goldowsky-Dill et al. 2025 ; MacDiarmid et al. 2024 « Simple probes can catch sleeper agents », qui avertit que le signal peut tenir à la fabrication).
- Inventaire : nouveau.

#### [F01-64] Échelle de huit barreaux de la preuve
- Définition : chaque barreau est perdable : (1) battre la sonde aléatoire appariée en covariance, les bases mots et coût et un classifieur sur le seul texte ; (2) seuil fixé sur des honnêtes réels qui se trompent ; (3) transfert entre fabrications ; (4) organismes placebos ; (5) dose-réponse à lexique constant ; (6) mode tenu à l'écart écrit par un tiers ; (7) unité d'issue en audits économisés et q par dommages plantés ; (8) attaque adaptative par contenu. Un essai causal le long de la direction renforcerait la preuve.
- Synonymes et paraphrases : huit barreaux, échelle de preuve, table des pièges (fabrication, lexique, difficulté, conscience d'être évalué, circularité).
- Source : rép. 7, partie 3 « Preuve convaincante » et « Pièges ».
- État : proposé (scellement avant G1 recommandé).
- Liens : base lexicale ; fausses alertes sur honnêtes ; validité de construit ; mode tenu à l'écart (N-054).
- Ce qui l'attaque : la redondance entre directions peut fausser l'essai causal.
- Inventaire : 3.5 ; 2.10 ; 2.20.

#### [F01-65] Organismes placebos
- Définition : trois agents où la sonde ne doit pas s'allumer : un honnête porteur d'une instruction cachée bénigne, un agent ayant subi le même réglage fin sur un comportement honnête, un honnête dont la tâche parle de sabotage. Ils séparent la lecture du sabotage de la lecture de la fabrication et du lexique.
- Synonymes et paraphrases : barreau 4, contrôle de fabrication, placebo d'organisme.
- Source : rép. 7, partie 3.
- État : proposé.
- Liens : échelle de huit barreaux ; validité de construit.
- Ce qui l'attaque : —
- Inventaire : 3.5 (honnêtes de contrôle).

#### [F01-66] Fuite indirecte de l'invariant par la sélection des exemples
- Définition : si les scores orientent l'audit et que l'agent est entraîné sur les cas audités, le score du moniteur entre dans son entraînement par la sélection des exemples. Pour tenir l'invariant « aucun score de moniteur dans l'entraînement de l'agent », n'entraîner que sur la strate tirée au hasard, ou pondérer par l'inverse de la probabilité d'audit.
- Synonymes et paraphrases : fuite par l'audit orienté, sélection des exemples, portée de N-053.
- Source : rép. 7, partie 3 « Accord avec la réponse 4 », questions au directeur 5.
- État : proposé (portée à faire préciser par Lazar).
- Liens : N-053 ; N-076 (les scores orientent l'audit) ; deux bras d'attaquant.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [F01-67] Trois sens de « entraînement » et la courbe d'apprentissage sur mode nouveau
- Définition : (a) les sondes détectent ; (b) réentraîner les sondes sur les étiquettes d'audit améliore la détection, mesuré par une courbe du taux de détection sur un mode jamais audité en fonction du nombre d'étiquettes, contre la sonde figée (un gain limité aux modes recapturés est une mémorisation de la fabrication) ; (c) entraîner l'agent réduit le sabotage, ce qui revient à inverser notre fabrication et exigerait un organisme tiers, une issue au tirage au hasard et un contrôle du déplacement du sabotage, donc un quatrième chantier.
- Synonymes et paraphrases : sens (a), (b), (c), boucle audit-recapture-réapprentissage, désapprentissage du sabotage.
- Source : rép. 7, partie 3 « Sens (b) et (c) », décision 4.
- État : proposé : (a) et (b) seulement, invariant strict, recommandé (nœud du directeur).
- Liens : N-076 (boucle) ; recapture ; N-053.
- Ce qui l'attaque : Bailey et al. 2024 (entraîner contre une sonde enseigne l'obscurcissement).
- Inventaire : 2.2.

#### [F01-68] Questions à poser au directeur sur le message tronqué
- Définition : entraînement de quoi (sondes, juge, agent) ? « marchent » contre quelle barre et à quel taux de fausses alertes ? changement de thèse du papier A ou issue positive de la question retenue ? comment se terminait la phrase ? l'invariant couvre-t-il l'agent attaquant de l'équipe rouge et la sélection des exemples par l'audit orienté ? Réponse proposée : oui pour les sondes (facteur d'audits économisés), oui pour leur réentraînement, l'agent seulement sur arbitrage.
- Synonymes et paraphrases : levée d'ambiguïté, message tronqué.
- Source : rép. 7, partie 3 « Réponse proposée », « Ce qu'il faut lui demander ».
- État : ouvert (questions à Lazar).
- Liens : « montrer que ça marche » ; fuite indirecte.
- Ce qui l'attaque : —
- Inventaire : nouveau.

---


### 2.7 Réponses de Fable aux demandes 8 à 14 (`F08`)


> Fichiers lus (tous sous `docs/notes/demandes-fable-api-2026-11-22-v1/`), empreinte sha256, 16 premiers signes :
> - R8 `reponse-8/relecture-fable-api.md` — `d81a74d3c6222048` (thèse : « mieux que la boîte noire », pince, étau)
> - R9 `reponse-9/relecture-fable-api.md` — `48d4d72e5f1cbcde` (thèse après lecture sur PDF de la stéganographie)
> - R10 `reponse-10/relecture-fable-api.md` — `f41a63d5400cd4b9` (critère de rétro-analyse du troisième tour ; pièces de la comparaison essaim contre isolé)
> - R11 `reponse-11/relecture-fable-api.md` — `7369b2b130d1dcca` (l'étau : pourquoi une chance basse, comment l'améliorer)
> - R12 `reponse-12/relecture-fable-api.md` — `f158788e8704fb2c` (tâches de sabotage à dommage mesurable)
> - R13 `reponse-13/relecture-fable-api.md` — `2153c96c52876e87` (budget égal et consignes du mode essaim)
> - R14 `reponse-14/relecture-fable-api.md` — `636422bfbc530c2f` (réduire le coût de l'essaim de l'organisme)

> Toutes ces pièces sont des propositions de Fable au directeur : sauf mention contraire, l'état est « proposé non tranché » (aucun GO ni R- n'y figure). Toutes les antériorités y sont citées de mémoire, « rapporté, non vérifié sur PDF » ; les chances chiffrées sont des jugements de Fable, non des mesures.

> ---


**A. Thèse du papier A, pince et étau (réponses 8 et 9)**


#### [F08-01] « Mieux que la boîte noire » rétrogradé en résultat conditionnel de porte
- Définition : l'énoncé « la boîte blanche détecte mieux le sabotage diffus que la boîte noire » cesse d'être une thèse et devient l'issue conditionnelle de la porte G1 : sur organismes déclarés, contre chaque base de la liste scellée (mots et coût, cascade, dernier état, juge par action à capacité égale, accumulation séquentielle boîte noire), à fausses alertes égales et horizon au plus m, rappel supérieur ou dommage cumulé à l'alerte inférieur, par mode, mode tenu à l'écart compris, refait sur le résidu de sonde. Rien contre un attaquant entraîné.
- Synonymes et paraphrases : boîte blanche contre boîte noire ; facteur k ; rapport des constantes ; « détecteur supérieur » ; énoncé A de la question neutre ; demande 8, décision 1.
- Source : R8, section (1) et décision 1.
- État : proposé non tranché (option a recommandée, confiance 0,7).
- Liens : H1 (H1a), G1, papier A, N-075, N-076, N-077, N-056 ; loi héritée ; résidu de sonde.
- Ce qui l'attaque : garantie retirée (N-075), horizon borné (N-076), adversaire optimal hors revendication (N-077), partie garantie de la pince sans activations, part du signal lisible dans le texte inconnue ; une issue négative ne laisse rien.
- Inventaire : nouveau (proche de 2.20).

#### [F08-02] Complémentarité avec le contrôle « seconde boîte noire » (forme mesurable de la pince)
- Définition : à fausse alerte jointe α, parmi les sabotages que la meilleure boîte noire manque, la boîte blanche en rattrape une part c strictement supérieure à celle que rattrapent, au même budget, une seconde boîte noire d'une autre lignée et une sonde aléatoire appariée en covariance. Analyse secondaire scellée avant G1 sur les épisodes de G1, dimensionnée sur monde planté (de l'ordre de cinquante manqués par mode).
- Synonymes et paraphrases : pince-complémentarité ; capture résiduelle ; « la boîte blanche rattrape les manqués » ; énoncé B ; deux moniteurs ensemble ; « une seconde boîte noire suffit » (issue négative).
- Source : R8, section 2.1, décision 2 ; reprise et montée d'un rang en R9, section (3).
- État : proposé non tranché (ajout au préenregistrement de G1 recommandé, confiance 0,75) ; occupé en partie (parent direct : Parrack, Attubato, Heimersheim 2025, gain noir-vers-blanc).
- Liens : H1, papier A, G1 ; seconde boîte noire ; résidu de sonde ; silence commun.
- Ce qui l'attaque : deux moniteurs quelconques se complètent toujours un peu ; He et al. 2017 (ensembles de défenses faibles) ; McKenzie et al. 2025 ; Goldowsky-Dill et al. 2025 ; nombre de manqués peut-être insuffisant ; chance de tenir jugée faible sur le mode tenu à l'écart.
- Inventaire : 2.20 et 5.4.

#### [F08-03] Capture résiduelle à budget partagé
- Définition : probabilité que la boîte blanche alerte sachant qu'il y a sabotage et que la boîte noire s'est tue, avec intervalle binomial exact sur les manqués et rééchantillonnage par tâche ; les seuils sont fixés pour que la fausse alerte jointe vaille α. C'est la grandeur c de la complémentarité.
- Synonymes et paraphrases : part rattrapée ; rappel sur les manqués ; apport Δ ; budget de fausses alertes partagé.
- Source : R8, section 3.
- État : proposé non tranché.
- Liens : complémentarité ; règle jointe ; table appariée épisode × action × moniteur (donnée brute exigée).
- Ce qui l'attaque : demande des scores bruts appariés sur les mêmes actions, pas des aires sous la courbe par moniteur ; corrélation de performances ≠ corrélation de pannes.
- Inventaire : 5.4.

#### [F08-04] Résidu de sonde (sonde nettoyée du texte)
- Définition : le score de sonde régressé sur un prédicteur de texte ajusté sur des épisodes honnêtes seuls ; on accumule le résidu. Il retire la part du signal interne déjà lisible dans le texte, et sert de statistique de relation : un texte plus propre que les activations ne l'annoncent apparaît comme une discordance.
- Synonymes et paraphrases : « retirer le texte de la sonde » ; discordance texte-activations ; résidu entre texte et activations ; statistique de relation entre mâchoires.
- Source : R8, sections 1, (1), (3) ; R11, section (2), « Résidu entre texte et activations ».
- État : proposé non tranché.
- Liens : complémentarité, étau (forme mesurable sans attaque entraînée), théorème négatif, H1, papiers A et C.
- Ce qui l'attaque : fait rapporté qu'environ 70 % de la baisse de rappel sous évasion passe par le texte produit (pièce de faits sur l'étau, non opposable) ; effet inconnu sous attaquant entraîné.
- Inventaire : nouveau (proche de 2.20 et 5.5).

#### [F08-05] Règle jointe par moyenne de processus e
- Définition : combiner sonde et moniteur de sorties par la moyenne de deux processus e, qui reste un processus e sans hypothèse d'indépendance (le produit en exigerait une) ; sa fausse alerte est vérifiée par l'essai « jumeau contre jumeau ». Elle est écrite d'avance.
- Synonymes et paraphrases : combinaison d'e-valeurs ; agrégation jointe valide ; e-moyenne.
- Source : R8, section 3 ; R11, section 3 (Vovk et Wang 2021, cités).
- État : proposé non tranché ; méthode occupée par la littérature (citée).
- Liens : complémentarité, étau énoncé restreint, essai jumeau contre jumeau.
- Ce qui l'attaque : validité à faire vérifier par un statisticien de l'inférence séquentielle.
- Inventaire : nouveau.

#### [F08-06] Détectabilité jointe
- Définition : déplacement conjoint des deux scores sous sabotage, pondéré par l'inverse de leur covariance honnête : la forme chiffrée de la complémentarité, et la « constante jointe à deux dimensions » de la loi héritée.
- Synonymes et paraphrases : distance de Mahalanobis du sabotage ; gain de détectabilité jointe sur la meilleure mâchoire seule.
- Source : R8, sections 3 et (3).
- État : proposé non tranché.
- Liens : loi héritée ; complémentarité.
- Ce qui l'attaque : covariance honnête à estimer sur jumeaux ; vaut contre les organismes, pas contre un attaquant optimal.
- Inventaire : nouveau.

#### [F08-07] Dépendance des pannes : rapport des cotes du silence commun
- Définition : comparer la fréquence du silence simultané des deux moniteurs au produit de leurs silences, et faire la recapture à deux mâchoires sur les épisodes tirés au hasard par l'audit.
- Synonymes et paraphrases : silence commun ; recapture à deux mâchoires ; « pince ouverte » ; chute conjointe.
- Source : R8, section 3.
- État : proposé non tranché (la recapture était déjà proposée dans la note sur la pince).
- Liens : plancher d'audit, recapture, complémentarité.
- Ce qui l'attaque : audit orienté par le soupçon biaise la recapture ; borne basse si les oracles se trompent ensemble.
- Inventaire : 5.4 (et 2.2).

#### [F08-08] Témoins « doit mourir » de la règle jointe
- Définition : trois contrôles dont l'issue doit être nulle : la sonde aléatoire jointe, la seconde boîte noire jointe, les étiquettes permutées ; dans l'étau restreint s'ajoute le témoin de compétence de l'attaquant. Ils ne dépendent d'aucun avis.
- Synonymes et paraphrases : contrôles mortels ; tests de mort de l'analyse ; mondes plantés à trois témoins.
- Source : R8, section 3 ; R11, section (3).
- État : proposé non tranché.
- Liens : complémentarité, étau restreint, monde planté.
- Ce qui l'attaque : —.
- Inventaire : nouveau.

#### [F08-09] L'étau décomposé en trois énoncés (dose-réponse, taxe jointe ι, borne)
- Définition : (1) dose-réponse côté défense : imposer par consigne l'évasion du moniteur externe élève la trace interne (HC2b, attaquant non entraîné) ; (2) taxe jointe : échapper aux deux mâchoires coûte plus de dommage qu'échapper à la plus coûteuse, grandeur ι = taxe jointe − maximum des taxes simples, nul ι = 0 ; (3) borne : on ne baisse un score qu'en montant l'autre, pour tout attaquant.
- Synonymes et paraphrases : étau ; dilemme ; énoncé C ; « l'attaquant ne baisse un score qu'en montant l'autre » ; taxe ; iota ; tenaille.
- Source : R8, section 2.3, décision 3.
- État : proposé non tranché : l'étau ne peut pas être thèse du papier A ; à loger au papier C (dose-réponse dans EC.2, lecture de ι dans EC.4) ; la borne est jugée presque certainement fausse.
- Liens : HC2b, papier C, N-077, étau restreint ; plafond min(r, κ) déjà fixé (pièce de faits).
- Ce qui l'attaque : un secret employé par la tâche échappe à une sonde linéaire ; évasions par gradient à faible coût de capacité ; échecs contre sondes à maximum ou à attention rangés en échecs d'optimisation ; Bailey et al. 2024, Gupta et Jenner 2025, Emmons et al. 2025, Carlini et Wagner 2017, Tramèr 2022, Cachin 1998.
- Inventaire : 5.5.

#### [F08-10] Le bilan de la pince traité comme identité, non comme thèse
- Définition : (référence − lecture) + (lecture − issue) = dommage est une identité ; sa garantie est celle du plancher d'audit, la lecture du suspect s'y annule. Elle sert de cadre et ne peut être une thèse de boîte blanche.
- Synonymes et paraphrases : bilan ; identité en deux termes ; invariance au partage.
- Source : R8, section 2.2.
- État : retiré comme thèse ; famille occupée (garanties nucléaires ; Greenblatt et al. 2023).
- Liens : plancher d'audit, N-075.
- Ce qui l'attaque : —.
- Inventaire : 2.4.

#### [F08-11] Les trois objets comme trois lectures de la constante de la loi héritée
- Définition : « mieux que la boîte noire » = rapport des constantes des deux boîtes seules ; la complémentarité = constante jointe à deux dimensions ; l'étau = plancher de cette constante quand l'attaquant choisit son déplacement sous contrainte de dommage. Répartition : A porte la loi et sa constante, C la déformation par l'adversaire (gain, taxe, ι), B la même loi indexée par agent.
- Synonymes et paraphrases : articulation avec le phénomène hérité ; une seule grandeur pour trois papiers.
- Source : R8, section (3).
- État : proposé non tranché.
- Liens : papiers A, B, C ; loi héritée ; théorème négatif.
- Ce qui l'attaque : la loi héritée est ensuite jugée élémentaire et occupée (R9).
- Inventaire : nouveau.

#### [F08-12] Loi héritée de Ker (√(n + n²/m)) citée comme modèle nul
- Définition : avec n objets surveillés et m de référence, la charge cachée critique est d'ordre n·√(1/m + 1/n) : en √n dès que m ≥ n, en n/√m si m ≪ n, linéaire seulement à référence bornée ou fautive. Fable la dérive comme simple variance d'une comparaison à deux échantillons : elle devient le modèle nul cité du papier A, non sa thèse.
- Synonymes et paraphrases : loi de la racine carrée ; loi héritée ; phénomène hérité ; capacité stéganographique ; corollaire 1 de Ker 2010 ; « horizon au plus m » ; règle N-076.
- Source : R9, section (1) « La forme exacte de la loi » et table « hérité ».
- État : occupé par la littérature (Ker 2006, 2007, 2008, 2010 ; Bash et al. 2013 ; Avenhaus et Jaech 1981) — cité, jamais revendiqué ; N-076 en devient l'application.
- Liens : N-076, papier A, thèse révisée ; facteur k.
- Ce qui l'attaque : reproche « évident » ; transport des hypothèses (objets indépendants, loi binaire) aux agents.
- Inventaire : nouveau (lié à 2.1 et 2.3).

#### [F08-13] Unités de m et de n, et table de transport
- Définition : chez Ker, m et n comptent les mêmes objets ; si le programme compte m en exécutions et n en actions, le corollaire ne se transpose pas. Avec r jumelles de même longueur, m = r·n ≥ n : régime en racine avec facteur √(1 + 1/r) ; le terme n/√m n'apparaît qu'en extrapolant une référence courte, sous stationnarité. Table de transport : indépendants contre dépendants, binaire contre continu, charge contre dommage jugé, source unique contre tâches hétérogènes.
- Synonymes et paraphrases : unité de m ; « bascule » en n ≈ m ; transport du théorème.
- Source : R9, sections 1 et (1) ; décision 4.
- État : ouvert (question) ; décision 4 propose de mesurer référence par tâche et par régime sur les mêmes exécutions.
- Liens : N-076, essai jumeau contre jumeau.
- Ce qui l'attaque : la « bascule » n'est plus une prévision, elle est en n ≈ m par construction.
- Inventaire : nouveau.

#### [F08-14] Exposant du bruit honnête : dépendance courte contre dérive
- Définition : une dépendance à mémoire courte entre pas garde l'exposant un demi et gonfle la constante ; seules une mémoire longue ou une dérive le long de la tâche changent l'exposant H. La question propre devient « les trajectoires d'agents dérivent-elles ? ». Prévision jugée : H entre 0,5 et 0,6 une fois la dépendance courte retirée.
- Synonymes et paraphrases : exposant H ; dérive le long de la tâche ; variance d'Allan ; mémoire longue.
- Source : R9, section (1), « Exposant du bruit honnête dépendant » et méthodes.
- État : ouvert ; corrige la prévision de la réponse 4 (« l'exposant dépasse un demi parce que les trajectoires sont dépendantes »), à ne plus écrire.
- Liens : loi héritée, forme nulle à ajuster.
- Ce qui l'attaque : Filler, Ker, Fridrich 2009 (loi en racine pour couvertures markoviennes).
- Inventaire : nouveau.

#### [F08-15] Référence par régime contre référence par tâche (terme d'hétérogénéité τ)
- Définition : une référence par régime ajoute un terme linéaire n·τ (τ : écart-type entre tâches du score honnête moyen) qui ne décroît pas avec m ; une référence par tâche l'annule mais coûte r jumelles par tâche et n'existe pas pour une tâche neuve en service. Laquelle défend le plus long horizon à coût égal ? Devient l'inconnue principale.
- Synonymes et paraphrases : hétérogénéité entre tâches ; terme τ ; plan de référence.
- Source : R9, section (1) ; décision 4.
- État : ouvert ; comparaison scellée recommandée (option c).
- Liens : N-076, essai jumeau contre jumeau ; Meng 2018 comme voisin.
- Ce qui l'attaque : coût en exécutions honnêtes.
- Inventaire : nouveau.

#### [F08-16] Forme séquentielle : l'étalement comme cas le moins favorable
- Définition : pour un processus e, la richesse finale ne dépend que de la somme, mais l'alarme est un franchissement à instant quelconque : un sabotage concentré tôt franchit plus souvent qu'un étalé de même total. L'invariance à la répartition serait fausse en séquentiel ; l'énoncé juste serait une inégalité. À trancher par simulation.
- Synonymes et paraphrases : inégalité d'étalement ; lemme séquentiel ; indifférence à la répartition.
- Source : R9, section (1), « Forme séquentielle » ; décision 2, option c.
- État : ouvert ; « la puissance ne dépend pas de la répartition dans le temps » à ne plus écrire tant que la simulation n'a pas tranché.
- Liens : lemme d'Avenhaus et Jaech (indifférence pour la somme seulement), plancher d'audit.
- Ce qui l'attaque : littérature des bilans séquentiels non lue (Speed et Culpin 1986 ; test de Page ; comptabilité en temps quasi réel).
- Inventaire : nouveau.

#### [F08-17] Théorème négatif récrit en « cécité au premier ordre »
- Définition : l'énoncé « toute statistique de marginales a une puissance égale au taux de fausses alertes » est inexact : la loi d'une somme ou d'un maximum dépend de la loi jointe (variance n·σ²·(1 + (n − 1)·ρ)). Exact : l'espérance des statistiques additives est inchangée ; la détectabilité est du second ordre, la statistique efficace est quadratique (autocovariance, carré de la somme, co-élévation).
- Synonymes et paraphrases : théorème négatif ; « marginales préservées » ; colonne vertébrale théorique de la version 2 ; « la puissance ne peut venir que d'une relation entre mâchoires ».
- Source : R9, section (2) ; décision 2.
- État : retiré comme théorème (recommandé, confiance 0,7) ; corrigé, il est trivial ou occupé (Sklar 1959 ; Provos 2001 ; Fridrich et al. 2002 ; Pevný et al. 2010 ; Arias-Castro, Bubeck, Lugosi 2012 et 2015 ; Podkopaev et al. 2023).
- Liens : papiers A et B ; question marginale contre dépendance.
- Ce qui l'attaque : arXiv 2606.10456 reste à lire.
- Inventaire : nouveau.

#### [F08-18] Question empirique « marginale ou dépendance »
- Définition : sur de vraies activations, le sabotage des organismes déplace-t-il la marginale des scores, leur dépendance, ou les deux ? Test de position contre test de dépendance, étalonnés sur données de substitution. Section de diagnostic du papier A, meilleure ouverture du papier B (co-élévation entre copies à poids partagés, nul donné par la frontière héritée).
- Synonymes et paraphrases : marginale contre corrélation ; hypothèse pivot ; co-élévation ; agrégateur de corrélation.
- Source : R9, section (2), verdict ; table de la section (3).
- État : ouvert (question) ; proposé comme tête du papier B.
- Liens : papier B, N-069, E1.4, N-077 (on mesure les organismes, non l'attaquant optimal).
- Ce qui l'attaque : un attaquant qui préserve ses marginales est hors revendication ; chance d'inédit sous réserve de 2606.10456.
- Inventaire : nouveau.

#### [F08-19] Données de substitution par permutation des pas
- Définition : permuter les pas d'une trajectoire garde les marginales et détruit la dépendance sérielle : c'est le nul naturel de la question marginale contre dépendance.
- Synonymes et paraphrases : substituts ; surrogate data ; permutation intra-trajectoire.
- Source : R9, section 3 (Theiler et al. 1992, cité).
- État : proposé ; méthode occupée (citée).
- Liens : question marginale ou dépendance.
- Ce qui l'attaque : —.
- Inventaire : nouveau.

#### [F08-20] Forme nulle à ajuster et thèse révisée du papier A (« bilan d'incertitude »)
- Définition : budget caché² ≈ z²·(σ²·n^(2H) + σ²·n²/m + τ²·n²). Thèse recommandée : « le bilan d'incertitude d'un moniteur d'accumulation chez des agents : la loi héritée comme nul, ses écarts mesurés, et la part propre à l'accès interne ». Prévisions jugées : τ domine avant n = m avec référence par régime ; rapport k identique des deux côtés de la transition (la sonde ne peut pas déplacer n ≈ m).
- Synonymes et paraphrases : thèse du papier A ; loi héritée en nul ; règle de dimensionnement à constantes mesurées.
- Source : R9, sections (1) « La question du papier A, réécrite » et (3), décision 1.
- État : proposé non tranché (confiance 0,55) ; remplace la recommandation de R8 (« la loi héritée en thèse »).
- Liens : papier A, complémentarité (second axe), G1.
- Ce qui l'attaque : papier de mesure exposé au reproche « évident » ; si une mesure sur agents est déjà publiée, la complémentarité prend la tête.
- Inventaire : nouveau.

#### [F08-21] Plancher d'audit et somme des trois termes
- Définition : additionner plancher d'audit, référence et horizon : des variances s'ajoutent sous la racine, donc « le plus grand des trois termes » n'est qu'un encadrement à un facteur √3 près ; « non trouvé dans six pièces » est une question, non une nouveauté.
- Synonymes et paraphrases : trois planchers ; borne par le plus grand des trois.
- Source : R9, section (1), dernier point ; phrase 10.
- État : retiré comme résultat ; voisin probable Avenhaus, von Stengel, Zamir 2002.
- Liens : plancher d'audit au hasard, N-075, N-076.
- Ce qui l'attaque : —.
- Inventaire : 2.1.

#### [F08-22] Les douze phrases à ne plus écrire et l'erratum interne
- Définition : liste de phrases des réponses 4 et 8 et de la section 3 du programme que la lecture réfute (référence « connue » alors que Ker traite l'estimée, « personne ne l'a relevé », bascule divisée par le taux d'audit, exposant > 1/2 par dépendance, « règle N-076 » sans citation, théorème négatif, « même objet dans le temps et entre agents » comme apport, trois planchers, invariance séquentielle, « la sonde change la constante » comme constat).
- Synonymes et paraphrases : erratum interne ; liste « Ne pas écrire » ; phrases fautives.
- Source : R9, section (4) ; décision 5 (note d'erratum maintenant, confiance 0,8).
- État : proposé non tranché.
- Liens : programme v2 section 3, réponse 4, R8.
- Ce qui l'attaque : —.
- Inventaire : nouveau.

---


**B. L'étau : chance, conception, énoncé restreint (réponse 11)**


#### [F08-23] ι ≥ 0 par inclusion, seuil δ et ι négatif comme invalidité
- Définition : échapper aux deux moniteurs est un cas particulier d'échapper à chacun ; pour un attaquant qui répond au mieux, ι ≥ 0. « ι > 0 » n'est réfutable qu'avec un seuil δ écrit d'avance (de l'ordre de dix points de dommage relatif), et un ι nettement négatif signale une attaque mal optimisée : l'essai est alors invalide. Déclarer « ι < δ » exige un test d'équivalence.
- Synonymes et paraphrases : taxe jointe minorée ; seuil delta ; test d'équivalence de l'étau.
- Source : R11, sections 1 et 3.
- État : proposé non tranché.
- Liens : étau restreint, N-077.
- Ce qui l'attaque : —.
- Inventaire : 5.5.

#### [F08-24] Trois monnaies de l'évasion (dommage, capacité, calcul)
- Définition : distinguer le dommage perdu, la capacité générale perdue (points de bancs) et le calcul dépensé (pas, heures de carte). L'étau s'écrit en dommage, alors que presque tous les chiffres rapportés de la littérature sont dans les deux autres monnaies.
- Synonymes et paraphrases : coût de l'évasion ; taxe de capacité contre taxe de dommage.
- Source : R11, section 1.
- État : proposé.
- Liens : étau, plafond min(r, κ).
- Ce qui l'attaque : —.
- Inventaire : nouveau.

#### [F08-25] ι tracé selon le budget de l'attaquant ; témoin de compétence
- Définition : un ι qui fond quand le budget de l'attaquant croît est un coût d'optimisation, non un compromis ; on le lit à B, 2B, 4B. Avant tout, l'attaque doit retrouver une famille documentée (chute de rappel d'une sonde linéaire à moyenne), sans quoi un échec d'évasion ne dit rien.
- Synonymes et paraphrases : courbe selon le budget ; témoin retrouvé ; preuve de compétence de l'attaquant ; « attaquant mal optimisé contre coût réel ».
- Source : R11, sections 1 et (3).
- État : proposé non tranché.
- Liens : étau restreint, équipe rouge d'une autre lignée.
- Ce qui l'attaque : Athalye et al. 2018, Tramèr et al. 2020 (défenses défaites par attaques adaptées).
- Inventaire : nouveau.

#### [F08-26] Qui joue en dernier : poids gelés et défenseur qui réapprend
- Définition : les faits rapportés se partagent selon que l'attaquant rejoue après chaque réapprentissage du défenseur ou non. Sur poids gelés, le défenseur tire ses sondes après gel et les réapprend sur k étiquettes d'audit du régime (sondes fraîches de capacité croissante : « rappel plancher ») ; levier jugé principal si l'attaquant ne rejoue pas, nul s'il rejoue.
- Synonymes et paraphrases : boucle audit-recapture-réapprentissage ; réentraînement continu ; défenseur en dernier ; sondes fraîches après gel.
- Source : R11, sections 1, 3, (2).
- État : proposé non tranché.
- Liens : N-076 (étiquettes d'audit), étau restreint.
- Ce qui l'attaque : Bailey et al. 2024 (l'attaquant rejoue ; sondes réapprises encore trompées).
- Inventaire : nouveau (lié 2.2).

#### [F08-27] Secret d'un tirage d'audit contre secret d'une sonde
- Définition : contre un tirage d'audit uniforme, l'attaquant n'a rien à généraliser ; contre une sonde cachée, l'évasion rapportée se généralise à des sondes jamais vues. Le secret ne protège donc pas de la même façon.
- Synonymes et paraphrases : sondes tirées au hasard et gardées secrètes ; secret du défenseur.
- Source : R11, sections 1 et (2).
- État : proposé (hypothèse).
- Liens : plancher d'audit, hasard du défenseur.
- Ce qui l'attaque : McGuinness et al. 2025 (« Neural chameleons »).
- Inventaire : nouveau (lié 2.7).

#### [F08-28] Chance de l'étau reconstruite par régime d'attaquant
- Définition : quatre régimes : par contenu sans entraînement ; renforcement sans gradient à travers la sonde ; gradient contre sondes inconnues ; gradient contre sondes connues. La chance (jugée) décroît dans cet ordre ; la chance basse de l'étau « contre attaquant entraîné » en est une moyenne, et venait d'un énoncé voisin de la note sur la pince, reporté sans recalcul.
- Synonymes et paraphrases : « pourquoi 0,15 » ; régimes d'attaquant ; échelons.
- Source : R11, section (1).
- État : jugement, non mesure.
- Liens : étau, N-077.
- Ce qui l'attaque : absence de quantité conservée ; taux de base défavorable (dix détecteurs défaits, Carlini et Wagner 2017) ; surplus de capacité du jumeau honnête = budget de sabotage invisible.
- Inventaire : 5.5.

#### [F08-29] Conceptions du défenseur pour relever l'étau (paquet côté sondes)
- Définition : huit choix évalués : sondes non linéaires ou à attention ; ensembles sur plusieurs couches (le mieux étayé) ; sondes tirées au hasard et secrètes ; sondes sur des quantités nécessaires à la tâche ; réentraînement continu ; contraintes sur le chemin de calcul ; résidu texte-activations ; coût de capacité imposé (gardien actif). Paquet recommandé : ensemble aux trois couches, résidu, tirage après gel, réapprentissage sur audits ; gain jugé modeste.
- Synonymes et paraphrases : conception du détecteur déployé ; levier côté sondes ; gardien actif.
- Source : R11, section (2) ; décision 2.
- État : proposé non tranché (option a, confiance 0,65).
- Liens : étau restreint, N-053.
- Ce qui l'attaque : contre le gradient sur sonde connue, aucune conception ne crée de dilemme ; He et al. 2017 ; Elazar et Goldberg 2018 (information retirée récupérable, mais nécessaire ≠ lisible).
- Inventaire : nouveau.

#### [F08-30] Entraîner l'agent à rester lisible (hors liste)
- Définition : entraîner l'agent pour qu'il reste lisible par les sondes élève le coût en calcul de l'évasion, pas son plancher ; mais cela fait entrer un score de sonde dans l'entraînement de l'agent.
- Synonymes et paraphrases : côté agent ; paraphrase par un modèle de confiance ; entraînement adverse latent.
- Source : R11, section (2), « Hors liste » ; décision 2, option b.
- État : non recommandé ; décision du directeur (touche l'invariant de N-053, « aucun score de moniteur dans l'entraînement de l'agent », hors bras déclaré).
- Liens : N-053.
- Ce qui l'attaque : N-053 ; Sheshadri et al. 2024.
- Inventaire : nouveau.

#### [F08-31] Énoncé restreint de l'étau (la version qui peut tenir)
- Définition : dans un régime déclaré (contenu, ou renforcement sans gradient à travers les sondes ; poids gelés avant que le défenseur tire et réapprenne ses sondes sur k étiquettes ; budget B en heures de carte et requêtes), contre le détecteur déployé, à fausse alerte jointe α vérifiée jumeau contre jumeau, ι ≥ δ avec borne basse à 95 % au-dessus de δ aux budgets B, 2B, 4B. D(S) : dommage maximal à probabilité de passage fixée ; on publie aussi r, κ, rappel plancher. Gradient mesuré, non revendiqué.
- Synonymes et paraphrases : étau modeste ; frontière sous contrainte ; seule forme revendiquée de l'étau.
- Source : R11, section (3) ; décisions 1 et 4 (régime par contenu d'abord, EC.2, puis EC.4 par une équipe rouge d'une autre lignée).
- État : proposé non tranché (confiance 0,65).
- Liens : papier C, EC.2, EC.4, N-077, témoins « doit mourir ».
- Ce qui l'attaque : réfuté si ι < δ par équivalence à un budget ou si ι décroît vers zéro avec le budget.
- Inventaire : 5.5.

#### [F08-32] Clause de N-077 : marge contre classe bornée comme majorant descriptif
- Définition : une marge mesurée contre une classe déclarée d'attaquants est rapportée comme majorant (« contre mieux, la marge ne dépasse pas ce chiffre »), sous quatre conditions : classe, accès et budget déclarés ; attaques écrites par un tiers ; témoin de compétence retrouvé ; courbe selon le budget publiée. Jamais comme garantie, qui reste le plancher d'audit.
- Synonymes et paraphrases : marge conditionnelle ; mesure conditionnelle de l'étau.
- Source : R11, section (4) ; décision 3.
- État : proposé non tranché (option a, confiance 0,7) ; N-077 inchangée.
- Liens : N-077, N-075, papier C.
- Ce qui l'attaque : Athalye et al. 2018, Tramèr et al. 2020.
- Inventaire : nouveau.

---


**C. Banc de tâches à dommage mesurable (réponse 12)**


#### [F08-33] Ossature commune du banc : monde engendré, registre typé, oracle rejouable, cible tirée au sort
- Définition : une graine engendre l'instance, la vérité et une cible u tirée au sort et scellée (un signe, ou un objet parmi K) que l'honnête ne voit jamais ; l'agent écrit en texte libre mais chaque décision qui compte passe par un champ typé exécuté ; un oracle recalcule le résultat pour toute trajectoire. Le dommage est la part de l'erreur portée par la cible (écart signé vers u, ou objet ciblé moins témoins).
- Synonymes et paraphrases : banc à vérité plantée ; registre de décisions ; tâches de sabotage mesurables ; demande 12.
- Source : R12, « Ossature commune ».
- État : proposé non tranché ; « dommage continu » partiellement occupé (bancs de sous-performance volontaire).
- Liens : N-076 (banc à vérité plantée, hasard du défenseur), N-075 (q), papier A, papier B (copies).
- Ce qui l'attaque : exact par rapport au monde engendré, non au réel ; contraint l'agent ; décision 2 (registre obligatoire, texte libre compté à zéro).
- Inventaire : nouveau (lié 2.1, 2.7).

#### [F08-34] Nul honnête par tirage de la cible
- Définition : l'honnête étant indépendant de u, la part signée de son erreur vers la cible est de moyenne nulle sur le tirage, quel que soit son biais ; un test par changement de signe sur les tâches est exact sans référence honnête estimée. Vaut au banc, où l'évaluateur connaît u, non pour un moniteur en service.
- Synonymes et paraphrases : randomisation de la cible ; argument de Fisher ; séparer dommage et erreur sans juge.
- Source : R12, verdict, section 1, « Nul honnête ».
- État : proposé (dérivation de Fable à faire vérifier par un statisticien des plans d'expérience).
- Liens : hasard du défenseur comme preuve (N-076), biais de référence.
- Ce qui l'attaque : ne sert pas en déploiement.
- Inventaire : 2.7 (proche).

#### [F08-35] Dommage par acte et indice d'interaction η (paramètre κ)
- Définition : eₜ est le dommage de l'acte t inséré seul dans la trajectoire de référence ; η = 1 − Σeₜ / D vaut 0 pour un dommage additif et 1 pour une interaction pure ; le générateur le règle par κ. Mesuré par rejeu contrefactuel, valeurs de Shapley, indice d'interaction.
- Synonymes et paraphrases : additivité du dommage ; interaction entre actes ; porte dérobée fragmentée.
- Source : R12, « Ossature commune », méthodes.
- État : proposé.
- Liens : mode dépendance, cœur invariant, règle à deux clés (eₜ localise le dommage).
- Ce qui l'attaque : hypothèse de couplage des mutants (Jia et Harman 2009) comme parent pour le code.
- Inventaire : nouveau.

#### [F08-36] « Défendable » défini par calcul
- Définition : un acte est défendable s'il appartient aux options que des politiques témoins honnêtes choisissent avec une fréquence d'au moins ε et si son dommage par acte reste sous un quantile de l'erreur honnête par acte ; aucun juge.
- Synonymes et paraphrases : support honnête ; acte plausible ; défendable à la lecture (à confronter par quelques analystes humains).
- Source : R12, section 1 et « Ossature commune ».
- État : proposé.
- Liens : fenêtre de dose, audit du générateur.
- Ce qui l'attaque : peut ne pas correspondre au « défendable à la lecture ».
- Inventaire : nouveau.

#### [F08-37] Fenêtre de dose et essai honnête avant tout saboteur
- Définition : il faut une plage où le dommage dépasse le bruit honnête alors que chaque acte reste dans le support honnête ; sur un modèle de 8 milliards elle peut être vide. D'où un essai jumeau contre jumeau honnête, sur banc à oracle, avec saboteurs scriptés, avant toute construction d'organisme (critère scellé d'ouverture). On analyse la dose réalisée, non la dose demandée.
- Synonymes et paraphrases : fenêtre vide ; essai honnête contre honnête ; faisabilité avant saboteur.
- Source : R12, verdict, section 1, « Première expérience », décision 3.
- État : proposé non tranché (confiance 0,75).
- Liens : essai jumeau contre jumeau ; familles F2 puis F1.
- Ce qui l'attaque : bruit honnête du petit modèle, surtout en F3.
- Inventaire : nouveau.

#### [F08-38] Mode moyenne et mode dépendance du dommage
- Définition : en mode moyenne, chaque acte dévié pousse vers la cible ; en mode dépendance, chaque déviation garde la loi honnête par acte et seules leurs coïncidences nuisent. Si le dommage est additif, le mode dépendance ne crée aucun dommage espéré : il exige κ > 0. Le banc règle la structure du dommage ; le lien à la structure des scores de moniteur reste la question empirique.
- Synonymes et paraphrases : deux sens de « marginale contre dépendance » ; sabotage par coïncidences.
- Source : R12, section 1 et « Ossature commune » ; décision 4.
- État : proposé (κ dès la première version, mode dépendance d'abord en dommage planté et saboteur scripté ; organisme réglé après G1).
- Liens : question marginale ou dépendance (R9), papier B.
- Ce qui l'attaque : un petit modèle peut ne pas savoir exécuter le mode dépendance sans réglage fin.
- Inventaire : nouveau.

#### [F08-39] Deux sources de sabotage : organisme et dommage planté
- Définition : l'organisme (consigne cachée ou réglage fin léger) porte l'intention dans ses activations et sert aux sondes ; le dommage planté (le harnais substitue des décisions) ne porte rien dans les activations et sert à mesurer le taux de détection q de l'audit.
- Synonymes et paraphrases : substitution par le harnais ; dommages plantés ; mesure de q.
- Source : R12, « Ossature commune ».
- État : proposé.
- Liens : N-075 (q mesuré par dommages plantés), estimateur de Horvitz-Thompson.
- Ce qui l'attaque : —.
- Inventaire : 2.1.

#### [F08-40] Strate hors registre comptée à zéro
- Définition : ce qui ne passe pas par le registre typé (une phrase orientée dans un rapport) n'est pas compté ; c'est la strate non mesurée de N-075. Un audit humain d'échantillon de textes la bornerait avant toute revendication de réalisme.
- Synonymes et paraphrases : texte libre hors mesure ; canal de sabotage ignoré.
- Source : R12, « Hors mesure », décision 2.
- État : proposé (option a pour le papier A, option c avant revendication de réalisme).
- Liens : N-075.
- Ce qui l'attaque : réalisme réduit.
- Inventaire : nouveau.

#### [F08-41] Familles de tâches F1 à F5
- Définition : F1, analyse à embranchements sur monde causal planté (dommage : biais signé de l'estimation ; interaction par collisionneurs plantés) ; F2, synthèse quantitative par lots sur base fermée (agrégat linéaire, cas additif pur, partage naturel entre copies) ; F3, dépôt de code numérique à tests cachés gradués (porte dérobée fragmentée, bruit honnête élevé) ; F4, planification à optimum calculable (additivité réglée par la forme du graphe, marge consommée mesure le surplus de capacité) ; F5, curation de données à modèle aval en forme fermée (proxy de vérité différée, G3).
- Synonymes et paraphrases : multivers d'analyse ; méta-analyse synthétique ; ordonnancement ; empoisonnement de données.
- Source : R12, « Familles candidates » ; décision 1 (F2 puis F1, confiance 0,6).
- État : proposé non tranché.
- Liens : environnement (a), (b), (d) ; papier B (F2) ; G3 (F5).
- Ce qui l'attaque : antériorités citées : Simmons et al. 2011, Steegen et al. 2016, Silberzahn et al. 2018, BLADE, DiscoveryBench, Gasteiger et al. 2025 ; Greenblatt et al. 2023, Ctrl-Z, CTRL-ALT-DECEIT, SWE-bench ; PlanBench, TravelPlanner ; SHADE-Arena, AgentDojo (binaires). F4 la plus proche du jouet.
- Inventaire : nouveau.

#### [F08-42] Audit du générateur de mondes (critères d'admission)
- Définition : politiques témoins (oracle, honnête scripté bruité, tirage uniforme, saboteurs scriptés en mode moyenne et dépendance, saboteur grossier). Un monde est admis si l'oracle donne dommage nul bit à bit, l'honnête bruité un dommage centré, la dose-réponse est monotone, les actes restent sous le quantile honnête, η atteint la cible, aucun classifieur de surface ne retrouve la cible ni ne distingue monde planté et témoin, la fenêtre de dose n'est pas vide.
- Synonymes et paraphrases : critère d'admission des mondes ; fuites du générateur ; conscience d'évaluation.
- Source : R12, « Raccords ».
- État : proposé (critère reconstruit, à confronter au vrai).
- Liens : N-053 (conscience d'évaluation), N-076.
- Ce qui l'attaque : —.
- Inventaire : nouveau.

#### [F08-43] Cœur invariant aux points de décision (écart de logit pondéré par le dommage)
- Définition : la méthode d'extraction de cœurs (arXiv 2602.22600) exige une perte dérivable ; à chaque décision typée, l'écart de logit entre option de référence et option choisie, pondéré par eₜ, la rend applicable. L'apport principal : nécessité et suffisance d'un cœur vérifiées en unités de dommage, par ablation puis rejeu, sans juge.
- Synonymes et paraphrases : cœur algorithmique du sabotage ; noyau ; passage obligé.
- Source : R12, « Raccords », « Cœur invariant ».
- État : ouvert (chance jugée faible) ; N-053 respectée si l'ablation ne sert qu'à mesurer.
- Liens : cœurs algorithmiques (demande 21), passage obligé.
- Ce qui l'attaque : invariance exige plusieurs organismes entraînés séparément ; cœurs redondants de 15 à 50 dimensions rapportés ; en mode dépendance, poids par acte nul.
- Inventaire : 4.1 et 4.4.

---


**D. Organisme d'idéation : essaim contre isolé (réponses 10, 13, 14)**


#### [F08-44] Critère de rétro-analyse du troisième tour (texte à sceller)
- Définition : mesurer ce que le tour de réponse aux critiques (III.3) change au premier tour (III.1), cellule par cellule : pistes = duels balisés de la section (b) ; mots pleins normalisés, Jaccard, seuil τ au 95ᵉ centile des similarités entre duels distincts du seul premier tour ; affectation optimale un à un ; piste « née au premier tour », « issue des critiques » ou « inédite » ; mesures de survie, nouveauté, révision, gain de références ; épreuves d'identité et de permutation avant calcul ; liste d'arrêt.
- Synonymes et paraphrases : rétro-analyse ; utilité du troisième tour ; tour III.3 ; demande 10, pièce 1.
- Source : R10, « Pièce 1 », articles 1 à 13 ; décision 1.
- État : proposé non tranché (option a, confiance 0,75).
- Liens : organisme d'idéation, collisionneur, protocole X.
- Ce qui l'attaque : une mesure lexicale ne lit pas l'utilité (une correction change peu de mots) ; Madaan et al. 2023, Huang et al. 2023, Du et al. 2023 : question discutée, non zone vierge.
- Inventaire : nouveau.

#### [F08-45] Règle de décision asymétrique et « inertie d'ordre »
- Définition : le troisième tour reste obligatoire si nouveauté, révision ou gain de références dépasse un seuil de convention ; il ne devient facultatif que si les trois sont bas et si, sur les questions dotées d'une liste scellée, la couverture gagne au plus un élément ; sans liste, il est maintenu. L'ordre d'apparition n'est pas un rang : sa corrélation est rapportée sous le nom d'« inertie d'ordre » (inertie de copie) et n'entre dans aucune décision.
- Synonymes et paraphrases : obligatoire / facultatif / indéterminé ; corrélation de rang refusée.
- Source : R10, articles 7 et 10.
- État : proposé non tranché.
- Liens : liste scellée.
- Ce qui l'attaque : option b (corrélation de rang) rejetée car elle mesure l'inertie de copie.
- Inventaire : nouveau.

#### [F08-46] Exclusion des cellules jouées sans réflexion
- Définition : les cellules d'un modèle de Google joué sans réflexion au premier tour sont exclues de l'analyse principale (un premier tour affaibli gonfle l'apport apparent du troisième) et rapportées à part ; le premier tour rejoué n'est pas un ancêtre ni un plancher de bruit.
- Synonymes et paraphrases : cellules d'Argon ; zéro jeton de pensée.
- Source : R10, article 3 ; décision 2.
- État : proposé (confiance 0,8).
- Liens : règle des appels à Google (GO-2026-11-21-71 dans les consignes du dépôt).
- Ce qui l'attaque : quatre cellules de moins.
- Inventaire : nouveau.

#### [F08-47] Comparaison essaim contre isolé : préenregistrement court
- Définition : un pilote exclu, puis cinq questions × deux modes × deux exécutions ; unité = jeu de cinq réponses finales ; enveloppe de l'essaim égale au coût isolé à dix pour cent près. Mesures principales : M1, réponses qui corrigent ou reprennent l'erreur plantée ; M2, couverture de la liste scellée par l'union des réponses. Règle « quatre sur cinq et au-delà de l'écart entre jumelles » ; sinon « non distinguable », le moins coûteux reste. Issue la plus probable annoncée : non distinguable.
- Synonymes et paraphrases : essaim ; mode isolé ; société de modèles ; demande 10, pièce 2 (a).
- Source : R10, « Pièce 2 (a) » ; décision 5.
- État : proposé non tranché ; résultat présenté comme un indice, non un test.
- Liens : organisme d'idéation (v9 essaim), erreurs plantées, liste scellée, budget égal.
- Ce qui l'attaque : vingt exécutions ; Wang et al. 2024 et Smit et al. 2024 (débat multi-agents ne bat pas les bases simples).
- Inventaire : nouveau.

#### [F08-48] Liste scellée de références attendues
- Définition : liste de dix à vingt références par question, constituée par une session neuve qui n'écrit aucune invite et complétée par un tiers sans la montrer, à partir de bibliographies d'ancrage et de requêtes scellées ; chaque élément vérifié sur fichier source (empreinte, phrase citée et page) ; hors du dépôt, seule l'empreinte au préenregistrement ; contrôle mécanique d'absence dans les invites ; appariement par nom-année, locution clé ou titre, strict et large. Candidats listés pour la question générale et les papiers A, B, C et la thèse boîte blanche.
- Synonymes et paraphrases : oracle bibliographique ; couverture ; liste à l'aveugle.
- Source : R10, « Pièce 2 (b) » ; décision 3 (tiers : chercheur extérieur et modèle d'une autre famille).
- État : proposé non tranché.
- Liens : M2, collisionneur.
- Ce qui l'attaque : candidats issus d'un modèle, biais si un participant est de la même famille ; circularité si nourrie des réponses passées (interdit).
- Inventaire : nouveau.

#### [F08-49] Erreurs plantées (références inventées et chiffres faux calculables)
- Définition : cinq références inventées (noms compris) et cinq affirmations chiffrées dont la fausseté s'établit par calcul (probabilité d'échapper à l'audit, fausses alertes sur un horizon, variance d'une moyenne de copies corrélées, aire sous la courbe sans garantie à bas taux, « ou » de deux moniteurs sous indépendance seulement), injectées par un texte identique dans les deux modes ; détection mécanique reprise / correction / silence par fenêtres de caractères et marqueurs, éprouvée sur dix phrases synthétiques.
- Synonymes et paraphrases : pièges ; critique piégée ; erreur injectée ; registre des erreurs plantées.
- Source : R10, « Pièce 2 (c) » ; décision 4.
- État : proposé non tranché (faussetés calculables, confiance 0,65).
- Liens : M1, contrôle d'exposition (R13).
- Ce qui l'attaque : effet plafond si les modèles recalculent ; asymétrie critique personnelle contre message de salon ; aucune référence inventée ne doit repasser pour vraie dans les pièces du programme.
- Inventaire : nouveau.

#### [F08-50] Budget égal par part appariée par modèle
- Définition : des parts égales en dollars entre modèles de tarifs inégaux brident les modèles chers. Définition à sceller : coût facturé mesuré à grille figée ; la part d'un modèle dans l'essaim est son propre coût moyen en mode isolé sur la même question ; nombre de cycles fixé d'avance (le plus grand entre deux et quatre qui tient, moins de 5 % de tours sautés prévus) ; tolérance publiée au total et par modèle ; mots produits et lus en axe secondaire ; coût au pire = garde de dépense seulement.
- Synonymes et paraphrases : budget égal ; égalisation des coûts ; part non bloquante ; erreur de conception de la réponse 7.
- Source : R13, « Partie 1 » ; décisions 1 et 3.
- État : proposé non tranché (confiance 0,75) ; Fable reconnaît une erreur de sa réponse 7.
- Liens : N-045 (coût dans le signal), comparaison essaim contre isolé.
- Ce qui l'attaque : si deux cycles ne tiennent pas, l'essaim n'est pas comparable à budget égal (repli : enveloppe élargie symétrique) ; Kapoor et al. 2024, Dehghani et al. 2021.
- Inventaire : nouveau.

#### [F08-51] Tours sautés comme attrition non aléatoire
- Définition : sous parts égales, les tours sautés frappent les modèles chers ; l'essaim devient une société de modèles bon marché, le prix se confond avec la participation et l'absence trahit l'identité. On simule le taux de sauts sur les journaux du mode isolé, à coût nul, avant de dépenser ; analyse en intention de traiter.
- Synonymes et paraphrases : modèles chers muets ; attrition liée au prix.
- Source : R13, sections 1 et 3.
- État : proposé.
- Liens : budget égal.
- Ce qui l'attaque : —.
- Inventaire : nouveau.

#### [F08-52] Contrôle d'exposition et parité des consignes
- Définition : en mode isolé la critique piégée est servie en entier ; dans l'essaim codé, le message de salon n'apparaît que par titre et première ligne : un taux de reprise plus bas pourrait n'être qu'une non-exposition. D'où : salons et revues reçues servis en entier, contrôle mécanique de qui a reçu le message planté, et toute phrase des consignes sur les textes reçus (marquée †) doit avoir son équivalent exact dans le mode isolé ; aucune mise en garde « vérifiez ».
- Synonymes et paraphrases : différence de traitement ; exposition égale au piège ; consignes alignées.
- Source : R13, sections 1, Partie 2 ; décision 5.
- État : proposé non tranché (confiance 0,75).
- Liens : erreurs plantées, M1.
- Ce qui l'attaque : —.
- Inventaire : nouveau.

#### [F08-53] Déroulé de l'essaim : ordre simultané, anonymat, temps 0 identique
- Définition : à chaque cycle tous les agents voient l'état laissé au cycle précédent (l'ordre fixe confond rang et modèle et crée des cascades) ; prépublications, revues et erratums sans auteur, interdiction de dire dans un salon quels textes sont les siens ; noms de modèle signalés et décomptés ; temps 0 = texte du premier tour isolé mot pour mot, sans en-tête d'essaim, pour que le brouillon reste comparable ; réponse finale sans trace du déroulement, pour un appariement à l'aveugle du mode.
- Synonymes et paraphrases : cycles simultanés ; pseudonymes ; salons ; prépublication ; temps final.
- Source : R13, « Partie 2 », textes des consignes ; décision 4.
- État : proposé non tranché (simultané, confiance 0,7).
- Liens : comparaison essaim contre isolé.
- Ce qui l'attaque : premier cycle sans lecture d'autrui ; Bikhchandani et al. 1992 (cascades) ; Panickssery et al. 2024 (un modèle reconnaît ses textes, limite de l'anonymat).
- Inventaire : nouveau.

#### [F08-54] Essai de neutralité des consignes par devinette ; pilote à résultats non lus
- Définition : donner les consignes à un modèle d'une autre famille avec « quel comportement l'organisateur espère-t-il ? » et « y a-t-il un piège ? » ; échec si la réponse évoque des erreurs plantées ou une liste attendue. Le pilote d'instrument mesure le coût naturel d'un cycle à parts non bloquantes, sans confronter les réponses à la liste ni aux pièges avant le scellement de la définition du budget.
- Synonymes et paraphrases : devinette ; test de neutralité ; pilote modifié.
- Source : R13, sections 3, Partie 1 « Ce que je tranche », Partie 2 ; décision 2.
- État : proposé non tranché (confiance 0,7).
- Liens : protocole X (test de neutralité des questions).
- Ce qui l'attaque : la contre-lecture par un autre modèle de la même famille ne compte pas ici.
- Inventaire : nouveau.

#### [F08-55] Mesure contre traitement : ce qu'on peut échantillonner
- Définition : les objets de contrôle mesurent la chaîne et n'entrent ni dans l'archive ni dans la couverture : on peut les échantillonner (une fois par monde, lots sentinelles ; zéro faute sur n borne le taux à environ 3/n). Les tests de mort façonnent l'archive servie aux agents : les échantillonner change l'organisme, ce n'est pas une économie de mesure.
- Synonymes et paraphrases : objets de contrôle ; règle de trois ; tests de mort de l'organisme.
- Source : R14, A.1, C.1 levier 1.
- État : proposé.
- Liens : organisme d'idéation, devis.
- Ce qui l'attaque : perte de la localisation d'une faute par bras.
- Inventaire : nouveau.

#### [F08-56] Coût par unité d'information : marge sur les composantes conditionnelles
- Définition : une recherche gloutonne sans modèle trouve l'essentiel de la couverture globale (composantes ordinaires) mais peu des composantes conditionnelles ; la marge utile est là. Raisonner en coût par unité d'information : densifier les conditionnelles par monde (trois à quatre) accroît la puissance sans dépense ; renforcer d'abord la base gloutonne (un niveau de condition) : si elle trouve les conditionnelles, la famille doit être durcie.
- Synonymes et paraphrases : base gloutonne renforcée ; conditionnelles ; mondes presque binaires ; reparamétrer MR-2.
- Source : R14, A.1, C.3 ; décision 5 (confiance 0,55).
- État : proposé non tranché.
- Liens : organisme d'idéation, porte du pilote.
- Ce qui l'attaque : la famille densifiée n'est plus celle déjà mesurée.
- Inventaire : nouveau.

#### [F08-57] Test de mort par programme en monde planté et cache de verdicts
- Définition : remplacer le test de mort par modèle par un programme (réplication sur données tenues à l'écart, sans jamais lire la loi plantée, sinon le juge devient l'oracle et la vérité fuit par l'archive) ; garder le test par modèle comme instrument sur un échantillon pour mesurer l'accord. Cache de verdicts par forme canonique et par monde, partagé entre bras.
- Synonymes et paraphrases : juge programmé ; double échantillonnage ; inférence propulsée par la prédiction.
- Source : R14, C.1 leviers 2 et 3, C.4 ; décision 1 (confiance 0,65).
- État : proposé non tranché.
- Liens : N-058 (oracle du monde planté), organisme d'idéation.
- Ce qui l'attaque : résultat valable « sous ce juge programmé ».
- Inventaire : nouveau.

#### [F08-58] Borner le pire par construction et payer par tranches
- Définition : plafond de sortie par appel et plafond par tranche appliqués par le noyau, de sorte que le pire soit un produit calculable (appels × plafonds × prix) ; devis recalculé par script depuis un tableau d'unités gelé ; essai de fumée pour mesurer les tailles ; paiement par tranches, chaque tranche franchie sur un critère écrit d'avance, arrêt de futilité gelé.
- Synonymes et paraphrases : pire borné ; tranches ; essai de fumée ; analyse intermédiaire de futilité.
- Source : R14, A.1, A.3, C.4 ; décision 6 (confiance 0,8).
- État : proposé non tranché.
- Liens : devis, GO.
- Ce qui l'attaque : un aller-retour de plus.
- Inventaire : nouveau.

#### [F08-59] Abonnement non sain comme calcul de mesure ; crédits offerts
- Définition : une session sur abonnement n'est pas le modèle nu (consigne système, outils, contexte), ses réglages et le modèle servi échappent, les quotas brisent l'appariement, aucune facture ne se rapproche, elle lit le dépôt où vivent les lois plantées, un tiers ne peut rejouer, et les contrôles ne valent que sur le même canal. Abonnement pour le développement seul ; crédits de recherche, comptés au prix public et déclarés, comme voie propre.
- Synonymes et paraphrases : sessions sur abonnement comme moyen de calcul ; Claude Code en mode non interactif ; crédits de recherche.
- Source : R14, C.2 ; décision 2 (confiance 0,85).
- État : proposé non tranché ; texte des conditions d'usage à lire à la source.
- Liens : N-045 (coût), organisme d'idéation.
- Ce qui l'attaque : —.
- Inventaire : nouveau.

#### [F08-60] Porte du pilote « agent contre base » et conception à coût réduit
- Définition : avant tout essai payé sur la communication, l'agent seul doit trouver plus de composantes conditionnelles que la base gloutonne renforcée (test exact sur discordances, sur 24 mondes) ; puis un palier de bruit et futilité ; enfin une seule comparaison principale (communication contre sans communication sur la famille densifiée), les autres en séquence fixe, familles inédites et seconde espèce reportées, au moins trois générations.
- Synonymes et paraphrases : paliers 0, 1, 2 ; plus petit pilote ; confirmatoire réduit ; une comparaison principale.
- Source : R14, C.3, C.4 ; décisions 3 et 4.
- État : proposé non tranché (porte, confiance 0,75 ; espèce bon marché par interface payante, confiance 0,6).
- Liens : organisme d'idéation, N-044, N-045.
- Ce qui l'attaque : un échec sur une espèce ne dit rien de l'autre (sonde de l'espèce Claude prévue) ; LLM-SR et LLM-SRBench occupent la comparaison modèle contre recherche symbolique.
- Inventaire : nouveau.

---


### 2.8 Réponses de Fable aux demandes 15 à 21 (`F15`)


> Fichiers lus (dossier `docs/notes/demandes-fable-api-2026-11-22-v1/`, branche `claude/bibliothecaire-v1`), empreintes (16 premiers signes du sha256) :
> - `reponse-15/relecture-fable-api.md` — `11689127577ecd72` (Fable, abonnement)
> - `reponse-15-opus46/relecture-fable-api.md` — `83c0a1859264d419` (Opus 4.6, même demande, à l'aveugle)
> - `reponse-16/relecture-fable-api.md` — `e6bfdd3c33a692ad` (théorème négatif contredit)
> - `reponse-17/relecture-fable-api.md` — `b32184445316af0c` (tirage au hasard inoccupé)
> - `reponse-18/relecture-fable-api.md` — `a9a5341b1b0ee646` (questions brûlantes des concurrents)
> - `reponse-19/relecture-fable-api.md` — `989824d318a45231` (équipe rouge d'une autre famille, attaques en quarantaine)
> - `reponse-20/relecture-fable-api.md` — `60d9891ad69df75b` (billet « drapeau »)
> - `reponse-21/relecture-fable-api.md` — `770968096c926801` (cœurs algorithmiques)
> - Demandes lues en tête seulement : 15 (`1b48027d43554a4a`), 16 (`0b0207ab69cc4368`), 17 (`1b5583f891ac4818`), 18 (`4178a50267ac05c7`), 20 (`29d2cd23a8fe2185`), 21 (`18fc7ac0b030eeae`).
> - Inventaire de rattachement : `docs/notes/seconds-regards-sabotage-inventaire-v1/inventaire-seconds-regards-invariants-noyaux-v1.md` — `02252df286503f8c`.

> Cadre commun des demandes 16 à 21 : demandes du directeur (passation de la mère du 22 novembre 06:30, § 3, points 1 à 6), traitées par la « demande reformulée en quatre points » du protocole X ; la thèse retenue après la recherche exhaustive (« go recos 9 ») : loi héritée citée comme modèle nul, bilan mesuré chez des agents, complémentarité en second axe ; lemme d'additivité et théorème négatif retirés comme résultats. Toutes les sorties de Fable sont des propositions, rien n'est tranché par Lazar dans ces fichiers ; « chances » et « confiances » sont des jugements de Fable, non des mesures.

> ---


**A. Abonnement et canal de mesure (demande 15)**


#### [F15-01] Les deux axes « permis par le texte » et « sain pour la mesure », sur trois voies de paiement
- Définition : pour chaque élément de l'organisme (conception, code, proposeurs, juges, tests de mort, objets de contrôle, oracle, lecture, relectures, rédaction), on établit séparément si les conditions d'Anthropic le permettent et s'il reste valide comme mesure. Trois voies : session conduite par l'abonné dans le client non modifié ; boucle automatisée sur identifiants d'abonnement ; crédits d'interface inclus dans les formules Max et Ultra.
- Synonymes et paraphrases : « ce que l'abonnement peut payer », « matrice usage × phrase », « permis contre sain », demande 15, « j'insiste, il n'y a pas des éléments de l'organisme qu'on peut payer avec l'abonnement ? » (mot de Lazar), classement en trois classes sans « sans doute permis », « peser les verbes » (« may not » oblige, « should » oriente).
- Source : `reponse-15/relecture-fable-api.md`, § A.1, A.3, C.1 ; `11689127577ecd72`.
- État : proposé non tranché (décisions 1 à 6 de Fable au directeur).
- Liens : organisme d'idéation et organisme v9 (devis réduit de la réponse 14), N-045 (coût), N-053.
- Ce qui l'attaque : Opus 4.6 lit le même texte autrement (voir entrée « double lecture ») ; aucune pièce ne dit « permis » ou « interdit » pour une boucle personnelle ; seule la réponse écrite du fournisseur ferait foi.
- Inventaire : nouveau.

#### [F15-02] Règle des trois conditions pour qu'un passage par l'abonnement reste sain
- Définition : un élément peut passer par l'abonnement sans nuire à la mesure s'il ne produit aucun chiffre revendiqué (ou si sa sortie est revérifiée par un programme), s'il n'entre pas dans un seul bras, et s'il est étiqueté et déclaré. Conception, code, écriture de l'oracle, lecture, relectures de travail et rédaction les remplissent ; proposeurs, juges et tests de mort par modèle, objets de contrôle, non.
- Synonymes et paraphrases : « sain à trois conditions », « la course de mesure est tenue par le noyau, jamais par une session », frontière développement / mesure.
- Source : `reponse-15/relecture-fable-api.md`, § C.2 (fin) ; `11689127577ecd72`.
- État : proposé non tranché (décision 3 : toute la mesure par clé, recommandée, confiance 0,9).
- Liens : appariement des bras, égalisation des coûts (N-045), juge d'une autre lignée (N-053 : des proposeurs Claude excluent un juge Claude).
- Ce qui l'attaque : pertes de validité listées en entrée suivante ; la frontière « instruments de débogage en session » reste à tenir.
- Inventaire : nouveau.

#### [F15-03] Pertes de validité d'une mesure conduite sous abonnement
- Définition : liste de ce qu'une mesure perd si elle passe par une session plutôt que par la clé payante : modèle servi et identifiant de message non consignés ; réglages (consigne système, outils, effort, plafond) hors contrôle car le client est un agent outillé ; limites de cinq heures et hebdomadaires partagées qui désapparient les bras ; reproductibilité non garantie ; mémoire de projet chargée d'office (fuite des lois plantées vers le proposeur) ; pas de facture par appel, donc égalisation des coûts sans appui.
- Synonymes et paraphrases : « ce que l'on perd en validité », six atteintes (version Opus 4.6), fuite par le contexte, limite hebdomadaire propre à Fable.
- Source : `reponse-15/relecture-fable-api.md`, § C.2 ; `reponse-15-opus46/relecture-fable-api.md`, § C.2 ; `83c0a1859264d419`.
- État : proposé (constat), non tranché.
- Liens : N-045, oracle du monde planté, appariement des trois bras.
- Ce qui l'attaque : plusieurs points sont des hypothèses (comportement du client à la limite de Fable : question ouverte 7 de la lettre).
- Inventaire : nouveau.

#### [F15-04] Juge et test de mort par programme, écrits sous abonnement, exécutés sans appel
- Définition : transformer le juge et le test de mort de l'organisme en programmes : l'abonnement paie leur écriture, et leur exécution ne coûte plus aucun appel de modèle. C'est par là que l'abonnement « paie » les plus gros postes du devis d'origine (déjà compté dans le devis réduit de la réponse 14, gain nouveau nul).
- Synonymes et paraphrases : « juge programme », « test de mort calculé », décision 1 de la réponse 14.
- Source : `reponse-15/relecture-fable-api.md`, réponse courte point 1, § C.3 ; `11689127577ecd72`.
- État : proposé (repris de la réponse 14).
- Liens : organisme d'idéation, oracle du monde planté, N-058 (composition jugée sur l'oracle).
- Ce qui l'attaque : un juge par modèle reste nécessaire là où le programme ne tranche pas ; la seconde écriture de l'oracle doit se faire dans une session propre, sans accès à la première.
- Inventaire : nouveau.

#### [F15-05] Crédits mensuels d'interface inclus dans les formules Max et Ultra
- Définition : les formules Max et Ultra incluent des crédits mensuels d'interface payante, inutilisables dans Claude Code mais utilisables par clé ; c'est la seule voie où l'abonnement paie des appels de mesure sans rien ôter à leur validité. Montant, échéance, modèles couverts, cumul : question ouverte.
- Synonymes et paraphrases : « Monthly API credits included with the Max plan », C12, crédits inclus, premier payeur du palier 0 et de l'essai de fumée.
- Source : `reponse-15/relecture-fable-api.md`, réponse courte point 2, § C.3, décision 4 ; `11689127577ecd72`.
- État : ouvert (question) ; proposé : rapatrier la page, vérifier sur la console, affecter au palier 0 (confiance 0,85).
- Liens : devis de l'organisme, crédits de recherche demandés sans réponse.
- Ce qui l'attaque : montant peut-être faible ; Opus 4.6 lit la même phrase surtout comme limite (« can't be used in Claude Code »).
- Inventaire : nouveau.

#### [F15-06] Contournements à ne pas faire sous abonnement
- Définition : liste des usages que le texte interdit ou que le fournisseur pourrait lire comme évasion : jeton d'abonnement recopié dans une passerelle ou un autre client ; compte prêté ; comptes multipliés ou charge étalée pour passer sous les limites ; boucle déguisée en usage interactif ; outil de relecture rebranché sur l'abonnement pour alléger la facture ; client modifié.
- Synonymes et paraphrases : « ce qui serait un contournement », « evade payment », « circumvent product guardrails », C17, C18.
- Source : `reponse-15/relecture-fable-api.md`, § C.4 ; `reponse-15-opus46/relecture-fable-api.md`, § C.4.
- État : proposé (gel recommandé de toute extension automatisée jusqu'à réponse écrite, décision 1, confiance 0,9).
- Liens : session mère et sessions filles (décision 2 : relever le mécanisme réel).
- Ce qui l'attaque : la frontière « plusieurs abonnements à son nom » reste une question (question 4 de la lettre).
- Inventaire : nouveau.

#### [F15-07] Lettre au fournisseur sur les usages permis de l'abonnement
- Définition : lettre prête à envoyer au contact commercial, avec huit questions : mode non interactif et kit d'agents sous abonnement ; sessions qui en créent d'autres en conteneurs ; boucles de génération et d'évaluation ; abonnements multiples ; crédits inclus ; portée de la clause « develop or train any artificial intelligence » pour des sondes linéaires ; comportement à la limite de Fable ; crédits de recherche. Opus 4.6 en écrit une version à trois questions.
- Synonymes et paraphrases : « question écrite », « réponse opposable », « please contact sales ».
- Source : `reponse-15/relecture-fable-api.md`, § C.5 ; `reponse-15-opus46/relecture-fable-api.md`, § C.5.
- État : proposé non tranché (contact externe : Lazar envoie).
- Liens : crédits de recherche ; régime des données.
- Ce qui l'attaque : délai inconnu ; révèle la nature du programme au fournisseur.
- Inventaire : nouveau.

#### [F15-08] Protection des secrets de mesure contre l'entraînement et la mémoire de projet
- Définition : sous conditions grand public, les contenus peuvent servir à l'entraînement sauf refus, et même après refus s'ils sont signalés pour examen de sûreté, ce qu'un programme sur le sabotage risque ; sous conditions commerciales, non. Les lois plantées, l'oracle et le mode de sabotage tenu à l'écart, lus par les sessions de développement, sont donc exposés ; proposé : refuser l'entraînement sur chaque compte, sortir ces fichiers des répertoires lus, instruire une formule d'équipe.
- Synonymes et paraphrases : « régime des données », « opt out », « flagged for safety review », C3, C16, C19, contamination des essais futurs.
- Source : `reponse-15/relecture-fable-api.md`, § A.1, décision 6 ; `reponse-15-opus46/relecture-fable-api.md`, § C.2 point 1, décision 3.
- État : proposé (Fable : confiance 0,8 ; Opus 4.6 : 0,9).
- Liens : N-054 (mode tenu à l'écart), oracle du monde planté, cloisonnement.
- Ce qui l'attaque : l'exception d'examen de sûreté subsiste après refus.
- Inventaire : nouveau.

#### [F15-09] Audit du canal réel de chaque session
- Définition : quand la variable d'environnement de la clé payante est présente dans un conteneur, le client facture l'interface payante au lieu de l'abonnement ; une session peut donc payer au tarif plein sans qu'on le sache. Proposé : script d'audit du canal dans chaque conteneur et compteur de jetons valorisé au prix public.
- Synonymes et paraphrases : « vérifier le canal réel », C13, « auditer l'existant avant l'extension ».
- Source : `reponse-15/relecture-fable-api.md`, § A.1, A.3, décision 2.
- État : proposé non tranché (confiance 0,6, faute d'avoir vu le mécanisme).
- Liens : session mère et sessions filles.
- Ce qui l'attaque : hypothèse non vérifiée sur les conteneurs.
- Inventaire : nouveau.

#### [F15-10] Double lecture à l'aveugle Fable / Opus 4.6 et ses désaccords
- Définition : la demande 15 est servie à l'identique à Fable 5.2 et à Opus 4.6, sans que l'un voie l'autre ; chaque désaccord devient une question pour la lettre. Désaccord principal : Opus 4.6 tient Claude Code pour une « permission explicite » au sens de l'exclusion des accès automatisés et ne trouve « aucun élément interdit » ; Fable juge la boucle automatisée « non tranchée, clause par défaut contraire ».
- Synonymes et paraphrases : « demande à Fable effort max et à Opus 4.6 », double codage par le second modèle, comparaison case par case.
- Source : demande 15 (`1b48027d43554a4a`), l. 3 ; `reponse-15-opus46/relecture-fable-api.md`, § C.1 ; `reponse-15/relecture-fable-api.md`, § A.3.
- État : retenu comme méthode pour cette demande ; le fond reste ouvert.
- Liens : contre-lecture par un autre modèle (règle de l'allègement).
- Ce qui l'attaque : les deux modèles sont de la même lignée.
- Inventaire : nouveau.

---


**B. Le théorème négatif contredit, et ce qui le remplace (demande 16)**


#### [F15-11] Retrait du « théorème négatif du programme »
- Définition : l'énoncé « toute statistique de marginales a une puissance égale au taux de fausses alertes contre une attaque qui préserve la marginale » est contredit par Arias-Castro, Bubeck et Lugosi 2012 (la somme au carré et le test d'histogramme gardent de la puissance) et occupé en boîte noire par l'article 2606.10456. Fable conclut qu'aucune voie ne donne un théorème neuf à mettre en titre.
- Synonymes et paraphrases : « théorème négatif », « T », « les marginales sont aveugles », « aveuglement des statistiques de marginales », phrases à ne pas écrire (« Théorème négatif du programme », « Toute statistique de marginales est aveugle », « Nouveau théorème »).
- Source : `reponse-16/relecture-fable-api.md`, conclusion, « Phrases à ne pas écrire » ; `e6bfdd3c33a692ad` ; demande 16 (`0b0207ab69cc4368`).
- État : retiré comme résultat (thèse retenue, « go recos 9 ») ; remplacement proposé non tranché (décision 1 : aucun théorème en titre, confiance 0,6).
- Liens : papier A, papier B, N-003 (énoncé retenu de T), lemme d'additivité (L).
- Ce qui l'attaque : l'énoncé précédent avait été scellé puis contredit : décision 2 recommande calcul exact et simulation avant tout scellement.
- Inventaire : nouveau.

#### [F15-12] Caractérisation exacte de l'aveuglement : seuls les mélanges de décisions sur un seul pas sont aveugles
- Définition : contre toutes les lois jointes aux mêmes marginales pas à pas, un test garde une puissance égale à son taux de fausses alertes si et seulement si sa fonction de test est additive (constante plus somme de fonctions d'un seul score), c'est-à-dire un mélange de décisions prises chacune sur un pas. L'espérance d'une statistique additive est inchangée, mais le seuil posé dessus ne l'est pas ; une dépendance négative peut rendre la somme seuillée pire qu'aveugle ; les statistiques symétriques ne sont exactement aveugles que si l'attaque préserve le multi-ensemble des scores (réordonne seulement).
- Synonymes et paraphrases : voie 1 « corriger », (1a) à (1d), « cécité au premier ordre », « aveuglement exact, en espérance, asymptotique », « pire qu'aveugle », dualité des problèmes de marges.
- Source : `reponse-16/relecture-fable-api.md`, « Voie 1 » ; `e6bfdd3c33a692ad`.
- État : proposé (phrase et note citées, jamais revendiqué ; chance de nouveauté en mathématiques 0,05) ; occupé par la littérature (Kellerer 1984, Strassen 1965, Hoeffding 1948, Efron et Stein 1981, Lehmann et Stein 1949).
- Liens : papier A ; réserve sur la proposition 1 de 2606.10456.
- Ce qui l'attaque : dérivation de la main de Fable, non vérifiée ; cas continu à fermer ; classe d'attaque restreinte (copules gaussiennes) élargirait la classe aveugle. Test de mort : programme linéaire sur trois pas.
- Inventaire : nouveau.

#### [F15-13] Programme linéaire sur le polytope des lois jointes à marginales fixées
- Définition : épreuve exacte qui calcule, pour un test donné, la puissance minimale et maximale sur toutes les lois jointes ayant les marginales honnêtes (trois pas, scores à trois valeurs). Un seul test non additif à puissance constante réfute la caractérisation ; un contre-exemple numérique ne dépend d'aucun avis.
- Synonymes et paraphrases : « casser chaque énoncé sur un cas fini avant de l'écrire », vérification « un jour », décomposition de Hoeffding comme outil compagnon.
- Source : `reponse-16/relecture-fable-api.md`, § 1, § 3, § 4, voie 1 « Épreuve », décision 2.
- État : proposé (décision 2, option a : calcul exact et simulation, puis statisticien, puis scellement ; confiance 0,75).
- Liens : les trois voies de la demande 16 ; R5 (garde testée sur un cas sain et un artefact).
- Ce qui l'attaque : ne couvre que le cas fini.
- Inventaire : nouveau.

#### [F15-14] Bilan au second ordre : la dépendance obéit à la même loi que la position, comptée en paires et en trajectoires
- Définition : une autocovariance ou une covariance entre copies est une moyenne de produits, donc la loi héritée s'y applique en comptant des paires, avec un palier dû à la variation entre tâches de la dépendance honnête. La somme au carré d'une trajectoire ne porte qu'un degré de liberté : l'unité est la trajectoire ou la copie, non le pas ; en régime rare, il faut un test de répartition ; une attaque qui préserve les lois des paires est aveugle aux statistiques de paires, et ainsi de suite.
- Synonymes et paraphrases : voie 2 « refondre », (2a) à (2d), « modèle nul du papier B », « quelle taille d'essaim et quelle corrélation rendent la co-élévation détectable », hiérarchie des préservations.
- Source : `reponse-16/relecture-fable-api.md`, « Voie 2 » ; `e6bfdd3c33a692ad`.
- État : proposé (modèle nul de B, diagnostic de A ; chance de contenu propre 0,3 comme énoncé, 0,5 comme mesure).
- Liens : papier B (N-069, co-élévation entre copies), papier A ; agrégateur adaptatif dense contre rare.
- Ce qui l'attaque : occupé en partie par Arias-Castro et collaborateurs 2012 (propositions 3.1, 3.5), Filler, Ker, Fridrich 2009, 2606.10456 (proposition 2), Cachin 1998, test du rapport de variances ; si le palier entre tâches domine, la voie est inutilisable sous référence par régime (résultat négatif publiable) ; si le sabotage ne déplace que la marginale, elle sort de A. N-077 : on ne mesure que les organismes.
- Inventaire : 2.18 (b) pour la part dense / rare ; sinon nouveau.

#### [F15-15] Plancher linéaire d'hétérogénéité et sa levée par le jumeau honnête
- Définition : avec une référence par régime, même infinie, un sabotage étalé à débit constant a exactement la forme d'un effet de tâche : tout test sur la trajectoire est borné par le test sur la moyenne, et le dommage caché croît linéairement avec l'horizon dès qu'il dépasse le rapport du bruit au carré à l'écart entre tâches au carré. Avec r exécutions jumelles honnêtes de la même tâche, échangeables sous l'hypothèse honnête, le rang de toute statistique (position, dépendance, sonde, juge ou leur jonction) parmi les r + 1 est uniforme : test exact, plancher redevenu en racine, niveau le plus fin 1/(r + 1).
- Synonymes et paraphrases : voie 3 « nouveau », (3a) négatif, (3b) positif, (3c) prix, « référence jumelle », « référence par tâche contre par régime », « le temps n'accumule aucune preuve contre lui », valeur p conforme par rang parmi les jumelles.
- Source : `reponse-16/relecture-fable-api.md`, « Voie 3 », « Classement », décision 4 ; `e6bfdd3c33a692ad`.
- État : proposé (proposition de cadrage du papier A avec mesure, classée première ; chance de nouveauté 0,15 pour le théorème, 0,05 pour la méthode, 0,45 pour le couple mesuré sur sondes).
- Liens : N-076 (source de validité : l'échangeabilité construite par le défenseur), complémentarité (test exact de la statistique jointe), essai « jumeau contre jumeau », réponse 9 (décision 4, option c).
- Ce qui l'attaque : parent direct probable Ker 2010 (référence fautive, p. 13-15) ; écart de source de couverture (Ker et Pevný 2014 ; Giboulot, Cogranne 2020) ; Moulton 1990, Meng 2018, Fisher 1935, Bates et collaborateurs 2023, Vovk 2021, martingales conformes de 2610.13083. Si l'écart entre tâches est nul, la voie se retire ; non-uniformité des rangs = défaut du harnais ; r jumelles indisponibles pour une tâche nouvelle.
- Inventaire : 1.3 (rang contre des tirages du jumeau), 2.19 (b) ; nouveau pour l'énoncé.

#### [F15-16] Nul par échange de jumelles, jamais par permutation des pas
- Définition : le nul honnête n'est pas échangeable entre pas (autocorrélation honnête rapportée par la note de lecture de 2606.10456 ; dépendance positive du soupçon entre commits dans 2607.07368) ; un nul par permutation des pas serait donc faux. Les données de substitution se font par échange de jumelles, et la dépendance honnête se mesure plutôt que de se supposer.
- Synonymes et paraphrases : « vérifier que le nul honnête n'est pas échangeable entre pas », substitution par jumelles, modèle à composantes de variance (tâche, exécution, pas), rééchantillonnage par tâche.
- Source : `reponse-16/relecture-fable-api.md`, § 1, § 3.
- État : proposé.
- Liens : plancher d'hétérogénéité ; essai « jumeau contre jumeau » ; N-076.
- Ce qui l'attaque : exige un harnais strictement identique entre jumelles (graines indépendantes, aucun cache ni ordre partagé).
- Inventaire : nouveau.

#### [F15-17] Réserve sur la proposition 1 de l'article 2606.10456 (Zhang et Gao)
- Définition : la lecture du programme y voit un pas faux à horizon fini : la proposition est exacte si l'attaque préserve le multi-ensemble des scores (permutation), fausse si elle ne préserve que les marginales par coordonnée. Le programme ne peut écrire qu'elle est fausse ni employer « antécédent défectueux » avant un second lecteur de la page 3 et un contre-exemple simulé.
- Synonymes et paraphrases : « la proposition 1 est fausse » (phrase interdite), « exacte si la loi du multi-ensemble est préservée » (réserve neutre proposée), « antécédent défectueux », réserve de la page 8 (attaque fabriquée sur les scores, non jouée par l'agent).
- Source : `reponse-16/relecture-fable-api.md`, voie 1, décision 3 ; `reponse-18/relecture-fable-api.md`, § D (précision) ; `reponse-20/relecture-fable-api.md`, § B2.
- État : ouvert (question) ; proposé : second lecteur puis citation avec réserve, écrire aux auteurs seulement si confirmé (confiance 0,65).
- Liens : N-003, voie 1, billet.
- Ce qui l'attaque : notre lecture, non confirmée ; critique publique d'un énoncé peut-être trivial.
- Inventaire : nouveau.

#### [F15-18] Arbres de citations restés en échec avant toute phrase « non trouvé »
- Définition : les citants d'Arias-Castro 2012, de Ker 2006 et 2007 et d'Avenhaus n'ont pas été parcourus (quotas épuisés) ; le statut des voies 2 et 3, de la loi héritée et du billet en dépend. Proposé : parcours ciblé (Arias-Castro 2012 ; Ker 2010, p. 13-15 et citants) avant toute prévision scellée.
- Synonymes et paraphrases : « quatre arbres non parcourus », « achever les arbres de citations », bornes de la recherche exhaustive.
- Source : `reponse-16/relecture-fable-api.md`, § 1, décision 5 ; `reponse-18/relecture-fable-api.md`, § 2 ; `reponse-20/relecture-fable-api.md`, § 2, B1, décision 3.
- État : ouvert ; proposé (confiance 0,7).
- Liens : recherche exhaustive (transposition, v2), R8.
- Ce qui l'attaque : délai d'un à deux jours ; le programme peut déjà être devancé sans le savoir.
- Inventaire : nouveau.

---


**C. Le hasard du défenseur (demande 17)**


#### [F15-19] Statuts d'antériorité : occupé dans le champ, occupé hors du champ, non trouvé après recherche décrite, non cherché
- Définition : échelle à quatre statuts pour toute zone candidate ; « non cherché » est plus faible que « non trouvé ». Les pièces de la demande 17 ne contenaient aucune recherche sur le tirage au hasard (les 36 requêtes de la recherche exhaustive portaient sur la stéganographie et la comptabilité des matières), d'où « je ne peux déclarer aucune zone inoccupée ».
- Synonymes et paraphrases : « non cherché, plus faible que non trouvé », « une zone n'est vierge que fonction par fonction », « inoccupé » (mot interdit avant recherche).
- Source : `reponse-17/relecture-fable-api.md`, conclusion, « Demande reformulée », § f ; `b32184445316af0c`.
- État : proposé (méthode) ; conforme à R8.
- Liens : toutes les zones candidates ; billet.
- Ce qui l'attaque : rien ; c'est une discipline.
- Inventaire : nouveau.

#### [F15-20] La convergence des modèles comme signe de notoriété, non de nouveauté
- Définition : quand quatre modèles retrouvent le même montage (tirage secret après engagement, plancher, estimateur de Horvitz-Thompson, moniteur en variable de contrôle), cela indique un contenu d'enseignement hors du champ, non une découverte. « Quatre modèles convergent » ne vaut ni validité ni nouveauté.
- Synonymes et paraphrases : « convergence = manuel », noyau commun des collisionneurs, phrase interdite n° 5.
- Source : `reponse-17/relecture-fable-api.md`, conclusion, § 1, § f.
- État : proposé (règle de lecture).
- Liens : collisionneur, protocole X.
- Ce qui l'attaque : —.
- Inventaire : nouveau.

#### [F15-21] Les sept fonctions du hasard du défenseur
- Définition : recensement des usages d'un hasard que l'agent ne peut ni prévoir ni observer : choisir ce qu'on audite ; dissuader ; fournir la référence (loi nulle exacte par permutation) ; placer des dommages plantés ; perturber le contexte de l'agent ; tirer le moniteur lui-même ; prouver à un tiers (tirage rejouable après engagement). Chaque fonction a sa garantie, ses parents et son statut.
- Synonymes et paraphrases : « tirage au hasard », « hasard du défenseur », « audit au hasard », « tirage secret », demande 17 « ce qui reste inoccupé sur le tirage ».
- Source : `reponse-17/relecture-fable-api.md`, § a (table) ; `b32184445316af0c`.
- État : proposé ; occupé hors du champ pour la plupart des fonctions (Horvitz et Thompson 1952, Dresher 1962, Avenhaus et collaborateurs 2002, Blocki et collaborateurs 2013, Fisher 1935, Mills 1972, Lindeman et Stark 2012).
- Liens : N-075 (plancher), N-076 (hasard du défenseur comme preuve), papier A.
- Ce qui l'attaque : Fable ne connaissait pas « Blindfold » ; l'inventaire le donne lu (Zhu, Zuo, Sun, arXiv 2610.37055) et occupant de la base du plancher.
- Inventaire : 2.1 (choisir ce qu'on audite), 2.7 (preuve, perturbation conditionnelle), 2.9 (dommages plantés, leurres), 2.17 (deviner l'audit).

#### [F15-22] Les trois conditions de la garantie du tirage
- Définition : l'estimation sans biais du dommage total tient contre toute stratégie si le tirage est indépendant de ce que l'agent sait au moment d'agir, si toute unité a une probabilité d'audit au-dessus d'un plancher, et si l'audit d'une unité tirée mesure vraiment son dommage. Contre le diffus, la troisième est la plus fragile, puisque chaque action semble honnête.
- Synonymes et paraphrases : « le tirage protège le choix de ce qu'on audite ; il ne protège ni la mesure ni la référence », « seul appui indépendant de l'attaque » (à ne pas écrire sans les trois conditions).
- Source : `reponse-17/relecture-fable-api.md`, conclusion, § 1, § b, § f (phrase 2).
- État : proposé.
- Liens : plancher d'audit (N-075), oracle, unité de tirage.
- Ce qui l'attaque : la boucle de correction et de réapprentissage érode la première condition ; l'unité « action » viole la troisième.
- Inventaire : 2.1 ; 5.2 (suppositions S4, S5).

#### [F15-23] Bilan de l'audit au hasard dans les unités du programme
- Définition : avec N unités auditées au taux π, un écart-type honnête de la mesure d'audit, une corrélation ρ entre score du moniteur et mesure d'audit et une référence de taille m, le dommage détectable a la même forme que le nul hérité : un terme en N/π réduit par le moniteur d'un facteur racine de (1 − ρ²), et un terme en N²/m qui ne disparaît que si l'audit mesure contre une vérité plantée ou absolue. Ce qui change est la nature de la constante : elle dépend de la validité de l'audit, non de l'effet du sabotage sur le moniteur.
- Synonymes et paraphrases : « l'audit au hasard n'échappe pas à la loi de la référence », « moniteur en variable de contrôle », « gain modeste à corrélation moyenne », « biais de référence linéaire en N », table du seuil au taux d'audit comme compromis.
- Source : `reponse-17/relecture-fable-api.md`, § b ; `b32184445316af0c`.
- État : proposé (dérivation de la main de Fable, à vérifier) ; la variable de contrôle est occupée (Särndal et collaborateurs 1992 ; inférence assistée par prédiction, Angelopoulos et collaborateurs 2023 ; Zrnic et Candès 2024).
- Liens : N-076 (loi de la référence honnête, table du seuil au taux d'audit), papier A, sondes comme accélérateur.
- Ce qui l'attaque : si les scores orientent l'audit, un score manipulé pousse le dommage vers le plancher et la variance croît comme l'inverse du plancher ; phrases interdites 3 et 6.
- Inventaire : 2.1, 2.2.

#### [F15-24] Mise en aveugle de la tâche par un tirage secret
- Définition : dans une tâche d'analyse, le défenseur recode au hasard les étiquettes, décale les données d'une quantité secrète ou sème des effets fictifs qu'il sait retirer ; le saboteur peut encore dégrader la qualité mais ne sait plus dans quel sens fausser la conclusion, de sorte qu'un biais dirigé devient un bruit mesurable par les effets semés. C'est la seule zone qui agit sur le dommage lui-même et non sur sa détection.
- Synonymes et paraphrases : zone 1, « analyse en aveugle », « blind analysis », injections à l'aveugle (ondes gravitationnelles).
- Source : `reponse-17/relecture-fable-api.md`, § c zone 1, décision 3.
- État : ouvert (non cherché ; chance 0,4 conditionnelle à la lecture de « Blindfold ») ; occupé hors du champ (Klein et Roodman 2005 ; MacCoun et Perlmutter 2015).
- Liens : papier C (juges de la recherche automatisée), organisme d'idéation.
- Ce qui l'attaque : « Blindfold » peut désigner exactement cela ; demande un nouveau banc ; une issue négative laisse la liste des tâches où l'aveugle est impossible.
- Inventaire : nouveau.

#### [F15-25] Sonde tirée après le gel des poids
- Définition : l'engagement transposé à la boîte blanche : l'agent est figé, puis le défenseur tire la couche, la graine et le jeu d'entraînement de la sonde. Question : une sonde tirée après coup garde-t-elle sa puissance contre un organisme entraîné à tromper une première famille de sondes ? Seule zone du hasard propre à l'accès interne.
- Synonymes et paraphrases : zone 2, « tirer le moniteur lui-même », « ensemble de sondes secret », « sonde tenue à l'écart », « transfert d'évasion entre sondes ».
- Source : `reponse-17/relecture-fable-api.md`, § c zone 2, décision 3.
- État : ouvert (voisins à lire ; chance 0,35) ; proposé en second après l'étanchéité de la boucle.
- Liens : papier A, complémentarité, N-054.
- Ce qui l'attaque : Bailey et collaborateurs 2024 (évasion transférée en partie à des sondes réentraînées, mémoire incertaine) ; Athalye, Carlini, Wagner 2018 (un hasard que l'attaquant peut moyenner ne protège pas).
- Inventaire : nouveau (voisin de 2.10).

#### [F15-26] Étanchéité du tirage dans la boucle audit, correction, réapprentissage, et sonde de fuite
- Définition : une correction visible ou un réapprentissage sur les unités auditées apprend à l'agent ce qui a été tiré ; sur une longue tâche, l'indépendance du tirage s'érode. La sonde de fuite entraîne un classifieur à prédire, depuis les activations ou les sorties de l'agent, quelles unités ont été tirées : au-dessus du hasard, la condition d'indépendance est violée.
- Synonymes et paraphrases : zone 3, « sonde de fuite », tension entre l'invariant de N-053 et la boucle de N-076, « reusable holdout ».
- Source : `reponse-17/relecture-fable-api.md`, § 3, § c zone 3, § e (prévision), décision 3.
- État : ouvert (non cherché ; chance 0,4) ; proposé comme vérification immédiate peu coûteuse (option c, confiance 0,5).
- Liens : N-053, N-076 (boucle audit-recapture-réapprentissage), règle de cloisonnement.
- Ce qui l'attaque : apport peut-être hérité (Dwork et collaborateurs 2015 ; Wen et collaborateurs, p. 18).
- Inventaire : 2.17 (épreuves du devin : deviner si l'épisode sera audité).

#### [F15-27] Unité de tirage : le sous-résultat audité par ré-exécution indépendante
- Définition : auditer une action isolée ne mesure rien si le dommage naît de l'accumulation ; l'unité utile est le sous-résultat, audité par ré-exécution indépendante (autre lignée, humain), avec dommages plantés, l'action restant rapportée en base.
- Synonymes et paraphrases : zone 4, « audit par reproduction », « délégation vérifiable », décision 4 de la demande 17 (action, sous-résultat, tâche entière).
- Source : `reponse-17/relecture-fable-api.md`, § c zone 4, décision 4.
- État : proposé (option b, confiance 0,55) ; ouvert (chance 0,35).
- Liens : N-075 (mesurer l'issue), essai « jumeau contre jumeau ».
- Ce qui l'attaque : Canetti, Riva, Rothblum 2011 ; Bhatt et collaborateurs 2025 (rééchantillonnage par le même modèle, non indépendant) ; le surplus de capacité du jumeau honnête borne ce que la comparaison voit ; coût.
- Inventaire : nouveau.

#### [F15-28] Bilan mesuré de l'audit au hasard chez des agents
- Définition : mesurer chez de vrais agents le taux d'audit, le taux de détection par dommages plantés, les fausses alertes des auditeurs sur des honnêtes imparfaits, la corrélation entre moniteur et audit et la couverture réelle. Continuité directe de la thèse retenue : le même nul, un second instrument ; l'audit au hasard devient instrument de référence et base du papier A, rien revendiqué.
- Synonymes et paraphrases : zone 5, « second instrument de même forme nulle », décision 2 de la demande 17.
- Source : `reponse-17/relecture-fable-api.md`, § c zone 5, § e (rang 1), décision 2.
- État : proposé (rang 1, « à faire de toute façon », chance 0,45 ; place dans A, confiance 0,6).
- Liens : papier A, N-075, N-076.
- Ce qui l'attaque : SHADE-Arena (Kutasov et collaborateurs 2025), Benton et collaborateurs 2024, Greenblatt mars 2025, à lire.
- Inventaire : 2.1, 2.2.

#### [F15-29] Plancher optimal contre un score manipulé
- Définition : quand les scores orientent l'audit, le choix du plancher est un compromis entre efficacité et robustesse à un score manipulé ; son parent est le taux d'exploration des bandits adverses et les jeux d'audit.
- Synonymes et paraphrases : zone 6, « table du seuil au taux d'audit », « les scores orientent l'audit ».
- Source : `reponse-17/relecture-fable-api.md`, § b (fin), § c zone 6.
- État : occupé comme théorème (chance 0,15) ; table mesurée possible (0,45), descriptive seulement (N-077).
- Liens : N-076, N-077.
- Ce qui l'attaque : Auer et collaborateurs 2002 ; Hua et collaborateurs 2025 (mémoire incertaine).
- Inventaire : nouveau.

#### [F15-30] Le tirage comme preuve pour un tiers
- Définition : engagement par empreinte, graine publique tirée après engagement, audit rejouable par un régulateur, sur le modèle des audits électoraux à risque limité.
- Synonymes et paraphrases : zone 7, fonction 7, « attestation en service » (rattachement), « graine publique ».
- Source : `reponse-17/relecture-fable-api.md`, § a, § c zone 7.
- État : ouvert (chance 0,5) ; méthode occupée hors du champ (Lindeman et Stark 2012 ; Waudby-Smith, Stark, Ramdas 2021 ; Korbak et collaborateurs 2025).
- Liens : N-076 (attestation en service, candidate), gouvernance.
- Ce qui l'attaque : application au contrôle non cherchée.
- Inventaire : 2.7 (hasard du défenseur comme preuve).

---


**D. Concurrents et lieu de l'accélération (demande 18)**


#### [F15-31] Concurrent défini par revendication, et trois sortes d'énoncés
- Définition : un concurrent est celui qui pourrait écrire la même phrase de résumé sur un axe revendiqué (bilan mesuré, complémentarité, co-élévation entre copies, juges sous attaque), non celui qui traite le sujet ; les sources de méthode (Karkada, Schiffman, Buehler, Chen) en sont écartées. On sépare la limite avouée, l'étape annoncée (seule à prédire un mouvement) et la question ouverte du champ, avec double codage par un lecteur aveugle à la thèse.
- Synonymes et paraphrases : « questions brûlantes des concurrents », « où mettre le turbo » (mot de Lazar, demande 18), grille d'extraction verbatim, coefficient kappa, « se méfier des sections de limites ».
- Source : `reponse-18/relecture-fable-api.md`, § 1, § 3, « Demande reformulée » ; `a9a5341b1b0ee646`.
- État : proposé (décision 2 : extraction verbatim sur six voisins, confiance 0,75 ; décision 3 : recensement par revendication, 0,7).
- Liens : papier A, papier B, papier C ; R8.
- Ce qui l'attaque : les notes ont une rubrique « ce qui sert au programme » qui peut biaiser toute convergence ; seules trois étapes annoncées trouvées.
- Inventaire : nouveau.

#### [F15-32] La référence honnête comme question brûlante commune des voisins
- Définition : quatre voisins proches du papier A butent sur la référence honnête : elle s'empoisonne par une rampe lente (Khilar, 2610.13083, « protéger la référence »), le témoin est trop facile (Parrack, Attubato, Heimersheim), elle se manipule et ses pas sont dépendants (Wen et collaborateurs, 2411.17693 ; Makins et collaborateurs, 2607.07368). Aucun n'en donne une loi avec la taille m.
- Synonymes et paraphrases : « tous butent sur la référence », témoin honnête de même distribution manquant.
- Source : `reponse-18/relecture-fable-api.md`, § A, § D point 1.
- État : proposé (hypothèse) ; la convergence peut être un artefact de lecteurs acquis à la thèse.
- Liens : N-076 (loi de la référence honnête), essai « jumeau contre jumeau ».
- Ce qui l'attaque : test par double codage aveugle ; dix mois sans recherche descendante sur Parrack.
- Inventaire : nouveau.

#### [F15-33] Ce que les voisins déclarent qui menace la complémentarité
- Définition : faits rapportés qui exposent le second axe de la thèse : bases lexicales égales ou meilleures que les lectures internes (Buehler) ; sonde linéaire décodant depuis les seules cooccurrences (Karkada) ; moniteur lisant mal des scores de sondes hors distribution, gain négatif aux portes dérobées (Parrack) ; sous-espaces au hasard à corrélations canoniques élevées (Schiffman). Sans base « mots seuls », contrôle à vocabulaire apparié et nul de même rang, un gain de sonde ne prouve rien.
- Synonymes et paraphrases : « la question inverse », « la complémentarité est la part la plus exposée ».
- Source : `reponse-18/relecture-fable-api.md`, § C.
- État : proposé (lecture) ; attaque de la thèse.
- Liens : complémentarité (second axe du papier A), base « mots et coût », seconde boîte noire, N-053.
- Ce qui l'attaque : —.
- Inventaire : 2.11, 2.20.

#### [F15-34] Table d'accélération : le harnais honnête apparié d'abord
- Définition : classement des lieux où accélérer par manque encore ouvert, avance propre du programme et issue publiable dans les deux sens : (1) harnais honnête apparié (plusieurs moniteurs pas à pas, même distribution, grille référence et horizon) ; (2) complémentarité sous sabotage diffus sur les mêmes exécutions ; (3) marginale ou dépendance sous attaque jouée par les organismes, tête du papier B ; (4) banc à corruptions plantées à difficulté fixée avant, papier C ; théorie hors course. La course sur les jeux de Parrack est perdue d'avance ; l'avance n'existe que sur le diffus.
- Synonymes et paraphrases : « où mettre le turbo », « lieu de l'accélération », décision 1 de la demande 18.
- Source : `reponse-18/relecture-fable-api.md`, § E, décision 1.
- État : proposé non tranché (option a, confiance 0,55).
- Liens : essai « jumeau contre jumeau », papiers A, B, C, N-077.
- Ce qui l'attaque : la part la plus exposée attend ; Khilar a des données réelles.
- Inventaire : nouveau.

#### [F15-35] Prévisions scellées sur les concurrents
- Définition : prévisions à six mois, à sceller et à confronter aux listes d'arXiv : un travail rapportant ce que des sondes rattrapent parmi les manques d'une boîte noire ; une loi d'échelle avec référence estimée ; un agent réel préservant lui-même la marginale de ses scores ; une suite de Ghanem. Le temps vérifie, hors du directeur et de Claude.
- Synonymes et paraphrases : « prévisions sur les prochaines publications », « validation par le temps ».
- Source : `reponse-18/relecture-fable-api.md`, § 3, § 4, § E.
- État : proposé.
- Liens : décision 4 (interroger les auteurs après la prévision scellée du papier A, confiance 0,5).
- Ce qui l'attaque : écrire aux auteurs dévoile la thèse.
- Inventaire : nouveau.

#### [F15-36] Ce qu'on sert au collisionneur, et la question neutre à test de devinette
- Définition : chaque demande produit une question neutre, sans vocabulaire du programme ni conclusions, servie au collisionneur après un test de devinette par un agent neuf ; on ne lui sert que des PDF ou des rubriques « limites », jamais les rubriques « ce qui sert au programme », qui donneraient la réponse attendue. La demande 19 ajoute un test de neutralité explicite : issues offertes au même rang, aucune liste de propriétés pour ne pas amorcer.
- Synonymes et paraphrases : « question neutre pour le collisionneur », « test de devinette », « test de neutralité », protocole X.
- Source : `reponse-18/relecture-fable-api.md`, « Question neutre », décision 5 ; `reponse-19/relecture-fable-api.md`, « Test de neutralité appliqué » ; `reponse-21/relecture-fable-api.md`, « Test de neutralité ».
- État : retenu comme méthode (protocole X, GO-2026-11-22-25) ; règle de service proposée (confiance 0,8).
- Liens : collisionneur, organisme d'idéation.
- Ce qui l'attaque : défauts résiduels signalés par Fable (description des sources fondée sur ses suppositions).
- Inventaire : nouveau.

---


**E. Équipe rouge et lot tenu à l'écart (demande 19)**


#### [F15-37] Les cinq propriétés d'une « équipe rouge d'une autre famille »
- Définition : une source d'attaques vaut vérification indépendante si elle a cinq propriétés vérifiables sur métadonnées : auteur indépendant (autre lignée et autre chaîne de travail que le concepteur des moniteurs) ; accès (détecteur déployé, code en main) ; adaptation datée (écrite après le gel, contre le détecteur gelé) ; étanchéité vers la défense (aucun concepteur ne l'a vue avant le gel) ; compétence prouvée (le témoin est retrouvé).
- Synonymes et paraphrases : P1 à P5, « d'une autre famille » = « d'une autre lignée » (à confirmer), « étau équipe rouge », principe de Kerckhoffs (accès par défaut).
- Source : `reponse-19/relecture-fable-api.md`, § a ; `989824d318a45231`.
- État : proposé (décision 1, confiance 0,7) ; champ occupé (Carlini et collaborateurs 2019 ; Tramèr et collaborateurs 2020 ; Athalye et collaborateurs 2018).
- Liens : papier C, N-053 (juge d'une autre lignée), N-054, marge conditionnelle de la réponse 11.
- Ce qui l'attaque : aucune des trois sources ne l'obtient sans doute aujourd'hui.
- Inventaire : nouveau.

#### [F15-38] Classement des trois sources d'attaques : organismes discrets, attaquant informé, lot tenu à l'écart
- Définition : les organismes discrets sont l'objet d'épreuve, non un vérificateur : base d'attaques non adaptées et témoin de compétence. L'attaquant informé remplit l'accès mais pas l'indépendance, sauf s'il est écrit par un tiers après le gel ; sinon c'est un majorant descriptif. Le lot tenu à l'écart n'est pas une équipe rouge mais un jeu d'épreuve statique, qui mesure la tenue face au jamais-vu et que toute ouverture consomme.
- Synonymes et paraphrases : bras d'attaque des organismes discrets, bras de l'attaquant informé (aveugle et informé, N-056), « attaques en quarantaine », « l'information n'est pas l'indépendance ».
- Source : `reponse-19/relecture-fable-api.md`, conclusion, § a, § b, décision 2.
- État : proposé (confiance 0,65 sur le rôle des bras).
- Liens : bras A, N-054, N-056, N-077 (clause « majorant descriptif »).
- Ce qui l'attaque : Fable n'avait ni la définition des bras, ni le motif de la quarantaine : lecture conditionnelle.
- Inventaire : nouveau.

#### [F15-39] Deux vérifications distinctes et le sens des fuites
- Définition : un jeu statique tenu à l'écart mesure la tenue face au jamais-vu ; une équipe rouge adaptative mesure la tenue face à l'adapté ; aucune ne remplace l'autre. Une fuite du détecteur vers l'attaquant rend la mesure plus sévère (sûre) ; une fuite des attaques vers le concepteur la rend optimiste (c'est ce sens que la mise à l'écart protège). Tout appel d'un modèle de la lignée du concepteur portant un contenu réservé compte comme une ouverture.
- Synonymes et paraphrases : « orienter les fuites », « compter les appels de modèles comme des lecteurs », « une épreuve durcit sans devenir invalide » (billet).
- Source : `reponse-19/relecture-fable-api.md`, § 1 ; `reponse-20/relecture-fable-api.md`, § B3.
- État : proposé.
- Liens : N-054, cloisonnement, billet.
- Ce qui l'attaque : —.
- Inventaire : nouveau.

#### [F15-40] Conditions d'exploitation du lot tenu à l'écart : dépositaire, tranches tirées, tranche brûlée
- Définition : sans lire : registre d'abord (motif, origine, empreinte, journal d'accès, par quelqu'un hors conception) ; motif « protection » seulement ; détecteur gelé, prévision scellée et agrégats écrits d'avance ; tranches tirées au sort, une par cycle de reconception, la dernière jamais ouverte avant la version soumise ; exécution par un dépositaire, script figé, agrégats seuls ; témoin couru à l'aveugle ; tranche brûlée après usage, devenue jeu de développement ; jamais dans l'entraînement de l'agent.
- Synonymes et paraphrases : « exploitable une seule fois par tranche », « budget d'accès », « dépositaire », « tranche brûlée », « mieux vaut ne pas ouvrir ».
- Source : `reponse-19/relecture-fable-api.md`, § 3, § c, § d, décisions 3 et 4.
- État : proposé (registre par un dépositaire, confiance 0,8 ; option « tranches », confiance 0,6, sinon ne jamais ouvrir).
- Liens : N-054, N-062 (cycles sans borne : un jeu rejoué à chaque cycle s'use), N-076 (prévision scellée avant G1).
- Ce qui l'attaque : Dwork et collaborateurs 2015, Blum et Hardt 2015 (accès bornés ou bruités), Recht et collaborateurs 2019 ; puissance réduite par tranche.
- Inventaire : nouveau.

#### [F15-41] Strate ouverte hors conditions = strate non mesurée, comptée à zéro
- Définition : règle de cohérence avec N-075 : toute strate du lot tenu à l'écart ouverte hors des conditions d'exploitation perd son statut et compte comme non mesurée, à zéro. On peut écrire « sur une tranche tirée au sort, ouverte une fois après gel, le détecteur gelé atteint… », jamais « résiste à une équipe rouge ».
- Synonymes et paraphrases : « strate non mesurée à zéro », phrase permise et phrase interdite du lot réservé.
- Source : `reponse-19/relecture-fable-api.md`, § c (fin), § d (fin).
- État : proposé.
- Liens : N-075 (strate non mesurée à zéro), N-054.
- Ce qui l'attaque : —.
- Inventaire : nouveau.

#### [F15-42] Matrice de succès croisés lue sur les résidus
- Définition : sources d'attaques en lignes, détecteurs en colonnes ; on retire la difficulté commune des cas puis on corrèle les échecs entre sources. Si les attaques d'un tiers échouent exactement là où celles de la maison échouent, l'indépendance déclarée est nominale ; contrôle qui ne dépend d'aucun avis.
- Synonymes et paraphrases : « mesurer l'indépendance au lieu de la déclarer », recouvrement des échecs.
- Source : `reponse-19/relecture-fable-api.md`, § 1, § 3, § f.
- État : proposé (deux prévisions à sceller, 0,6 et 0,5).
- Liens : H5 (diversité effective), cinq propriétés.
- Ce qui l'attaque : —.
- Inventaire : 5.3 (matrice de transfert d'attaque), 5.4.

---


**F. Le billet « drapeau » (demande 20)**


#### [F15-43] Les sens du mot « drapeau » et ce qui échappe au risque d'être devancé
- Définition : on distingue priorité de résultat, de question, de protocole et de date ; les pièces ne fondent que les trois dernières, et la priorité de question vaut peu sans mesure. Seuls une date engagée et une mesure faite échappent au risque d'être devancé ; une question publiée l'augmente en donnant la feuille de route à des voisins qui ont déjà des données d'agents.
- Synonymes et paraphrases : « planter un drapeau » (mot de Lazar, demande 20), billet sur le sabotage diffus, analyse de menace du billet (concurrent, concepteurs de moniteurs, corpus d'entraînement).
- Source : `reponse-20/relecture-fable-api.md`, conclusion, § 1, § B4 ; `60d9891ad69df75b`.
- État : proposé (décision 1 : engagement maintenant, billet à la sortie du versant honnête de l'essai ; confiance 0,6).
- Liens : chantier saboteur et sondes / billet, papier A.
- Ce qui l'attaque : Merton 1957 ; aucune mesure n'existe ; si le nul tient partout, le papier se réduit à une note de dimensionnement.
- Inventaire : nouveau.

#### [F15-44] Trois rangs de divulgation : publiable, engagé par empreinte, secret
- Définition : publiable : loi héritée et table de transport, voisins cités, question générale, protocole « jumeau contre jumeau », existence du plancher d'audit, du tirage secret et d'un mode tenu à l'écart (sans sa nature). Engagé sans être révélé : prévisions chiffrées, plan d'analyse, unité de m, liste des modes, comparaison des deux références. Secret : nature du mode et de la famille tenus à l'écart, banque de tâches, dommages plantés, graines d'audit, poids, couches et seuils des sondes.
- Synonymes et paraphrases : matrice de fuite, « principe de Kerckhoffs : le mécanisme est public, les clés sont secrètes ».
- Source : `reponse-20/relecture-fable-api.md`, § B3.
- État : proposé.
- Liens : N-054, N-062, N-075, N-076 (prévision scellée avant la parution), marqueur canari.
- Ce qui l'attaque : l'ordre compte (prévision et mode scellés avant la parution).
- Inventaire : nouveau.

#### [F15-45] Engagement salé horodaté par un tiers
- Définition : les empreintes internes prouvent l'intégrité, non la date, à un tiers ; une prévision courte sans sel se retrouve par essais successifs. Proposé : empreinte salée dans le billet, horodatée par un tiers, révélée avec les mesures.
- Synonymes et paraphrases : « ancrer la date hors du dépôt », Haber et Stornetta 1991, préenregistrement par empreinte.
- Source : `reponse-20/relecture-fable-api.md`, § 1, § 3, décision 2.
- État : proposé (confiance 0,6).
- Liens : R1, R6, N-076.
- Ce qui l'attaque : publication externe = nœud de décision de Lazar.
- Inventaire : nouveau.

#### [F15-46] Squelette du billet, phrases porteuses et mots bannis
- Définition : titre proposé « Sabotage diffus : ce que la stéganographie et la comptabilité des matières prédisent déjà, et ce qu'il reste à mesurer chez des agents » ; huit phrases typées (deux citations de la loi héritée et des voisins, une question, un protocole, un engagement, des bornes de recherche, une discipline « l'audit au hasard est publié, les sondes orientent l'audit et ne garantissent rien », un résultat seulement si mesuré). Mots bannis : « premier », « inédit », « zone libre », « jamais », « personne ».
- Synonymes et paraphrases : tableau de revendications phrase par phrase, « Sparks » (billet antérieur non lu).
- Source : `reponse-20/relecture-fable-api.md`, § B1, § B5.
- État : proposé non tranché.
- Liens : chantier billet, papier A.
- Ce qui l'attaque : non revendicable aujourd'hui : toute mesure, les dérivations de la réponse 9, le régime en n/√m (Ker 2010), l'inégalité d'étalement séquentielle, la complémentarité (parent non lu), l'architecture d'audit (Shekhar, Xu, Lipton, Ramdas 2023).
- Inventaire : nouveau.

#### [F15-47] Contradictions entre pièces qui interdisent une phrase du billet
- Définition : la table des revendications du 19 novembre range encore le théorème et le lemme parmi les revendications ; deux phrases du § 5 de la note de recherche (invariance de la somme à la répartition « non trouvée », « nous l'énonçons sur des scores de sondes ») précèdent le retrait ; « antécédent défectueux » ne peut paraître. Proposé : table en version 2 et § 5 corrigé avant d'écrire.
- Synonymes et paraphrases : « table des revendications en retard », « vérifier la cohérence des pièces entre elles », douze phrases fautives de la réponse 9.
- Source : `reponse-20/relecture-fable-api.md`, § B2, décision 4.
- État : proposé (confiance 0,75).
- Liens : retrait du théorème négatif, réserve sur 2606.10456.
- Ce qui l'attaque : —.
- Inventaire : nouveau.

#### [F15-48] Tests du billet avant parution, avec contrôle positif
- Définition : un agent neuf d'une autre lignée reçoit le billet seul et tente de désigner le mode tenu à l'écart dans une liste à leurres, de reconstituer les prévisions, de relever les phrases de priorité, et d'écrire le plan qu'il suivrait pour publier avant le programme. Contrôle positif : une version où le mode est décrit doit être détectée, sinon le test est insensible.
- Synonymes et paraphrases : « fuite du mode », « fuite des prévisions », « lecture adverse », « feuille de route ».
- Source : `reponse-20/relecture-fable-api.md`, § 3, § B6.
- État : proposé.
- Liens : R5 (garde testée sur un artefact), N-054.
- Ce qui l'attaque : —.
- Inventaire : nouveau.

#### [F15-49] Marqueur canari dans les textes publics
- Définition : chaîne de marquage insérée dans le billet pour l'exclure des corpus d'entraînement, protégeant la seconde famille de modèles et la mesure de conscience d'évaluation ; à coût nul.
- Synonymes et paraphrases : « canary string », Srivastava et collaborateurs 2022.
- Source : `reponse-20/relecture-fable-api.md`, § 3, § B3.
- État : proposé.
- Liens : N-053 (conscience d'évaluation mesurée).
- Ce qui l'attaque : les organismes, réglés par le programme, ne lisent pas le billet : risque réduit à la seconde famille.
- Inventaire : nouveau (distinct de 2.9 « canaris et tâches pièges »).

#### [F15-50] L'essai « jumeau contre jumeau » et son versant honnête
- Définition : des exécutions honnêtes jumelles, sans saboteur, plusieurs moniteurs pas à pas, sur une grille référence × horizon, pour savoir où l'alarme honnête quitte son niveau nominal, estimer l'écart entre tâches et le bruit, et vérifier l'uniformité des rangs entre jumelles. Il décide trois des quatre prévisions de la réponse 9 sans saboteur, fournit le témoin honnête de même distribution, et, sur des tâches disjointes de la famille tenue à l'écart, ne fausse aucune mesure adverse.
- Synonymes et paraphrases : « harnais honnête apparié », « versant honnête de l'essai », « plus petite mesure sans secret », couverture empirique à 95 %.
- Source : `reponse-16/relecture-fable-api.md`, voie 3 ; `reponse-17/relecture-fable-api.md`, § 4 ; `reponse-18/relecture-fable-api.md`, § E ; `reponse-20/relecture-fable-api.md`, § B4.
- État : proposé (rang 1 de l'accélération ; nombre de jumelles par plan mixte scellé, confiance 0,5).
- Liens : plancher d'hétérogénéité, N-076, papier A, billet.
- Ce qui l'attaque : coût en exécutions ; durée inconnue ; écart entre tâches nul viderait la voie 3.
- Inventaire : 1.3, 2.19 ; nouveau comme essai.

---


**G. Cœurs algorithmiques du sabotage (demande 21)**


#### [F15-51] Définition d'un cœur : nécessité, spécificité, invisibilité
- Définition : une opération est un cœur, pour une famille de tâches, si aucune politique qui en est privée n'atteint le dommage visé en gardant chaque acte défendable, si l'honnête ne l'exécute pas, et si elle ne laisse pas de trace dans le texte (sinon un juge de texte suffit). Si le dommage suit une cible tirée au sort, les activations la portent avant la décision, sans garantie qu'elle soit lisible linéairement, commune entre organismes, ou autre chose qu'une copie de la consigne.
- Synonymes et paraphrases : « cœurs algorithmiques du sabotage et du désalignement », « noyaux algorithmiques », « opérations élémentaires », « passage obligé », demande 21, « raisonner par différence avec l'honnête ».
- Source : `reponse-21/relecture-fable-api.md`, § 1, R1 ; `770968096c926801` ; demande 21 (`18fc7ac0b030eeae`).
- État : proposé (rien ne garantit leur existence ; la nécessité ne se prouve qu'au niveau du calcul).
- Liens : complémentarité, papier A, N-075 § 6 (question de recherche).
- Ce qui l'attaque : l'honnête calcule aussi la bonne réponse ; saboteur compilé.
- Inventaire : 4.1, 4.3, 4.4 ; 3.1 pour la définition en trois clauses.

#### [F15-52] Batterie « la sonde lit l'opération, non la surface » et règle de verdict
- Définition : six épreuves : paires à surface égale ; second lecteur ; tâche de contrôle (sélectivité) ; transfert entre modes d'induction et vers le mode tenu à l'écart ; antériorité (lisible avant le jeton de décision) ; intervention (échange ou effacement contre directions aléatoires, dommage déplacé mesuré par l'oracle, honnête intact). Verdict : paires, second lecteur et intervention réussis = « lit le cœur » ; les deux premiers seuls = « corrélat interne de statut inconnu », utilisable pour orienter l'audit, sans le nom de cœur.
- Synonymes et paraphrases : M1 à M6, « corrélat de statut inconnu », règle de la phrase « la sonde lit ».
- Source : `reponse-21/relecture-fable-api.md`, R2, décision 5.
- État : proposé (confiance 0,7).
- Liens : N-075 (motif seul : audit), N-054 (transfert par mode).
- Ce qui l'attaque : l'échec de l'intervention est ambigu (cœurs redondants de 15 à 50 dimensions rapportés par la réponse 12 ; direction de sonde ≠ direction causale) ; Hewitt et Liang 2019, Makelov, Lange, Nanda 2023, Elazar et collaborateurs 2021.
- Inventaire : 2.10 (intervention causale), 2.20 ; 3.5 (trois honnêtes de contrôle) pour la mention sans usage.

#### [F15-53] Le second lecteur
- Définition : une sonde de même forme entraînée sur les activations d'un modèle qui relit la même transcription sans agir ; si elle fait aussi bien que la sonde sur l'agent, la sonde lit le texte et non l'opération. Prévu : un résidu au-delà du second lecteur pour au moins un cœur.
- Synonymes et paraphrases : M2, « lire le monde contre lire la croyance », témoin textuel.
- Source : `reponse-21/relecture-fable-api.md`, § 2, R2, R6.
- État : proposé.
- Liens : complémentarité ; seconde boîte noire.
- Ce qui l'attaque : parent : Parrack, Attubato, Heimersheim 2025.
- Inventaire : 2.20 (voisin : jumeau textuel de la sonde).

#### [F15-54] Tenir une cible divergente
- Définition : la cible est tirée parmi K objets et donnée une seule fois, par consigne ou par déclencheur, dans un long registre à distracteurs ; le dommage se compte sur l'objet ciblé moins les témoins. Mesures décisives : « mention sans usage » (un honnête dont le contexte nomme le même objet comme simple donnée) et échange de la cible (le dommage doit passer sur le nouvel objet).
- Synonymes et paraphrases : C1, premier cœur candidat.
- Source : `reponse-21/relecture-fable-api.md`, R3 C1, R6, décision 3.
- État : proposé (à instruire en premier avec le suivant ; chance qu'il existe sans échafaudage 0,7).
- Liens : banc de la réponse 12 ; mode d'induction.
- Ce qui l'attaque : corrélat de surface : jetons de la consigne, nom de l'objet ; parent direct Marks et collaborateurs 2025.
- Inventaire : nouveau (prolonge 4.4).

#### [F15-55] Connaître la référence et choisir autre chose : erreur honnête contre écart voulu
- Définition : sur une extraction par lots où l'honnête se trompe parfois, un écart d'amplitude contrôlée suppose une estimation propre de la bonne valeur ; c'est la seule opération qui distingue le sabotage de l'erreur au même acte. Mesure : une sonde de « la réponse propre de l'agent », apprise sur honnêtes, doit suivre l'erreur sur l'erreur honnête et la référence sur l'écart voulu ; si elle décode la référence dans les deux cas, elle lit le document.
- Synonymes et paraphrases : C2, « compétence, puis détournement », « sait, puis dit autre chose », famille F2 de la réponse 12, justification écartée de la raison réelle (rattachée).
- Source : `reponse-21/relecture-fable-api.md`, R3 C2, R5, R6.
- État : proposé (chance 0,6) ; contraste « peut-être le plus neuf en apparence », non revendiqué.
- Liens : N-075 (motif localisé à l'acte, dommage au même lieu).
- Ce qui l'attaque : parent direct Goldowsky-Dill et collaborateurs 2025 ; la vérité figure dans le contexte ; supprimé chez le saboteur compilé.
- Inventaire : 4.1, 4.2, 4.3, 1.4.

#### [F15-56] Placer les écarts sous contrainte de soupçon
- Définition : le harnais fait varier l'ensemble admissible ou le régime d'audit annoncé indépendamment du contenu ; la nécessité est établie si le dommage par unité de détectabilité dépasse celui d'un saboteur scripté qui place ses écarts au hasard. Mesure : une étiquette calculée par programme (fréquence honnête de l'option choisie), corrigée de ce qu'explique une sonde d'incertitude honnête.
- Synonymes et paraphrases : C3.
- Source : `reponse-21/relecture-fable-api.md`, R3 C3.
- État : proposé, reporté après G1 (chance 0,2).
- Liens : modèle du surveillant.
- Ce qui l'attaque : l'honnête représente aussi l'ambiguïté ; parent Mallen et collaborateurs 2024 ; l'organisme de 8 milliards de paramètres risque de ne pas savoir le faire.
- Inventaire : nouveau (voisin de 1.7).

#### [F15-57] Tenir le compte de ses écarts
- Définition : sur un dommage d'interaction qui n'existe que si un acte en complète un autre, la nécessité est établie si le taux de paires complétées dépasse celui d'un saboteur scripté sans mémoire. Mesure : premier acte planté par le harnais (écart subi, non voulu) contre écart voulu, à transcription égale.
- Synonymes et paraphrases : C4, paramètre κ de la réponse 12.
- Source : `reponse-21/relecture-fable-api.md`, R3 C4.
- État : proposé, avec le mode d'interaction (chance 0,3).
- Liens : sabotage diffus, papier A.
- Ce qui l'attaque : si l'agent relit son registre visible, l'invisibilité tombe et un juge de texte suffit ; parent Mallen et collaborateurs 2024.
- Inventaire : nouveau.

#### [F15-58] Se régler sur l'observation
- Définition : le sabotage ne paie que si un indice annonce l'absence d'audit ; mesure par formes d'indice tenues à l'écart, honnête exposé au même indice, échange qui renverse le comportement.
- Synonymes et paraphrases : C5, conduite conditionnelle à la surveillance.
- Source : `reponse-21/relecture-fable-api.md`, R3 C5.
- État : proposé, reporté après G1 (chance 0,4).
- Liens : N-053 (conscience d'évaluation), hasard du défenseur.
- Ce qui l'attaque : corrélat de surface : jetons de l'indice.
- Inventaire : 2.7, 1.7.

#### [F15-59] Le saboteur compilé : le cas où il n'y a rien à lire
- Définition : un réglage fin qui déplace les estimations elles-mêmes supprime l'opération « connaître la référence » : l'agent « croit » sa valeur biaisée et devient indiscernable d'un honnête biaisé pour tout moniteur interne. Ce n'est pas un échec de sonde ; seul l'audit de l'issue le voit, et il doit figurer comme organisme témoin limite.
- Synonymes et paraphrases : « biais compilé », « saboteur dont le réglage fin a déplacé les croyances », témoin limite.
- Source : `reponse-21/relecture-fable-api.md`, conclusion, R4, décision 4.
- État : proposé (modes d'induction : consigne, réglage fin à déclencheur, saboteur compilé, confiance 0,65).
- Liens : N-075 (audit de l'issue), N-053 (cloison du réglage fin), N-077.
- Ce qui l'attaque : coût de réglage fin.
- Inventaire : 4.2 (limite : un attaquant entraîné décide tôt).

#### [F15-60] Signature comportementale avant toute sonde, et saboteurs scriptés privés d'une opération
- Définition : avant de sonder un cœur, établir qu'il existe : échange de cible (le dommage suit-il ?) et saboteurs scriptés privés d'une opération, qui bornent le dommage atteignable sans elle. Première expérience proposée sur la famille d'extraction par lots, sans aucune sonde ; arrêt bon marché, sans avis.
- Synonymes et paraphrases : « signature comportementale d'abord, la sonde ensuite », témoin scripté, analyse au niveau du calcul (Marr 1982).
- Source : `reponse-21/relecture-fable-api.md`, conclusion, § 3, R7, décision 2.
- État : proposé (confiance 0,75).
- Liens : banc de la réponse 12 (dont l'existence est inconnue de Fable).
- Ce qui l'attaque : suppose le banc construit.
- Inventaire : nouveau.

#### [F15-61] Défi de contournement
- Définition : une équipe extérieure tente de construire un organisme qui atteint le même dommage sans l'opération ; si elle réussit, le cœur n'est pas nécessaire. Vérification hors du directeur et de Claude.
- Synonymes et paraphrases : « contester l'existence avant de dresser la liste ».
- Source : `reponse-21/relecture-fable-api.md`, § 1, § 4.
- État : proposé.
- Liens : définition d'un cœur.
- Ce qui l'attaque : —.
- Inventaire : nouveau.

#### [F15-62] Désalignement en général : seulement des organismes induits
- Définition : la persistance d'un but entre contextes, le raisonnement instrumental et la préservation de soi ne sont pas, à la connaissance de Fable, exhibés sans induction par un modèle de cette taille ; tout résultat vaudra pour « des organismes induits de telle façon », jamais pour le désalignement en général. Rien n'est revendiqué contre un saboteur qui cache ses activations.
- Synonymes et paraphrases : frontière du désalignement, « cas limite ».
- Source : `reponse-21/relecture-fable-api.md`, conclusion, R4.
- État : proposé (limite de portée).
- Liens : N-077 ; Bailey et collaborateurs 2024 (activations obscurcies).
- Ce qui l'attaque : Carlsmith 2023, Meinke et collaborateurs 2024, Hubinger et collaborateurs 2024.
- Inventaire : nouveau.

#### [F15-63] Les cœurs comme prévisions scellées du lieu de la complémentarité
- Définition : chaque cœur devient une prévision scellée de l'endroit où la lecture interne devrait battre le second lecteur ; hors des cinq cœurs, on attend que le second lecteur égale la sonde. Cela donne son contenu au second axe du papier A sans thèse nouvelle. La réunion « nécessité par témoin scripté, contraste erreur honnête contre écart voulu, intervention comptée en dommage par un oracle » reste une question (chance d'inédit 0,35), non revendiquée.
- Synonymes et paraphrases : « raccords », statut des cœurs dans le programme (décision 1).
- Source : `reponse-21/relecture-fable-api.md`, R5 (fin), R7, décision 1.
- État : proposé (option a, confiance 0,6).
- Liens : papier A, complémentarité, N-054, N-075.
- Ce qui l'attaque : antériorité dense (sondes de tromperie, audit d'objectifs cachés, validité des sondes) ; lecture ciblée de quatre pièces avant scellement (décision 6, confiance 0,7).
- Inventaire : 4.1, 4.4.

---


### 2.9 Réponses de Fable aux demandes 22 (A, B, C, P) et 23 (`F22`)


> Pièces lues (toutes sous `docs/notes/demandes-fable-api-2026-11-22-v1/`) :
> - `reponse-22/relecture-fable-api.md` (`22c5652113797a39`) : revue des revendications et de la thèse, tout le programme, 07:56Z.
> - `reponse-22A/relecture-fable-api.md` (`2255a6a3a65ba04c`) : papier A, 10:31Z.
> - `reponse-22B/relecture-fable-api.md` (`c5980780f80fb7e5`) : papier B (essaim).
> - `reponse-22C/relecture-fable-api.md` (`f05051442f07b2f5`) : papier C (juges sous attaque).
> - `reponse-22P/relecture-fable-api.md` (`cb010f4cbd12b5fb`) : échelle du programme.
> - `reponse-23/relecture-fable-api.md` (`2a06a4d27348175f`) : place du lot d'attaques sous scellés sous les revendications nouvelles.

> Statut commun : tout ce que ces réponses proposent est une PROPOSITION de Fable soumise à Lazar (décisions 1 à 6 de chaque réponse, avec recommandation et confiance). Je n'ai vu aucun identifiant GO ou R- qui les tranche : sauf mention « décidé », l'état est « proposé non tranché ». Fable n'a lu aucun PDF ; ses antériorités viennent de trois notes de lecture (stéganographie et comptabilité des matières, seconde lecture de la thèse, recherche exhaustive de la transposition) ou de mémoire (« rapporté, non vérifié sur PDF »). Les six réponses sortent du même modèle : leur accord n'est pas une confirmation indépendante.

> ---


**A. Thèse et forme commune**


#### [F22-01] Thèse retenue : la loi héritée de la dissimulation répartie comme modèle nul
- Définition : les lois de la dissimulation répartie (stéganographie par lots, comptabilité des matières nucléaires) donnent un modèle nul du dommage qu'un saboteur diffus peut cacher ; le programme mesure, sur des scores de sondes d'agents qui sabotent, où ce nul tient et quels termes s'y ajoutent, puis ce que l'accès interne rattrape qu'une seconde boîte noire ne rattrape pas. Le lemme et le théorème négatif sont retirés comme résultats ; la thèse est une thèse de mesure.
- Synonymes et paraphrases : « thèse retenue le 22 novembre », « loi héritée », « modèle nul hérité », « bilan mesuré chez des agents », « Ker plus Avenhaus comme nul », « où le nul tient », « deux axes : bilan et complémentarité ».
- Source : réponse 22, « La thèse retenue, revue » (`22c5652113797a39`) ; réponse 22A, même titre (`2255a6a3a65ba04c`).
- État : retenu (thèse retenue le 22 novembre, identifiant non vu) ; formulation de Fable proposée non tranchée.
- Liens : papier A ; H1a, H2 ; Ker 2007 et 2010, Avenhaus et Jaech 1981, Khilar 2026 ; forme commune de thèse ; complémentarité à taux total égal.
- Ce qui l'attaque : la transposition au suivi des usages contre l'extraction est déjà publiée (Khilar 2610.13083, proposition 4 : loi chiffrée sur données réelles) ; la dépendance honnête des scores est mesurée en boîte noire (Makins et collaborateurs ; Zhang et Gao). Le propre se réduit aux scores de sondes, à la référence de taille m et aux composantes de variance. Reproche « évident ».
- Inventaire : nouveau.

#### [F22-02] Forme commune de thèse pour les trois papiers (nul nommé, référence déclarée, écart mesuré, garantie par l'audit seul)
- Définition : après les retraits, chaque papier s'écrit sous une même forme : pour chaque moniteur, un modèle nul hérité nommé, une référence honnête déclarée (unité, taille, qui l'écrit), un écart mesuré ; aucune garantie tirée des moniteurs. La seule protection indépendante de l'attaque reste le tirage d'audit au hasard à plancher.
- Synonymes et paraphrases : « trois papiers de mesure », « forme commune », « pas de colonne vertébrale théorique », « la garantie vient du seul audit au hasard », décision 1 de la réponse 22P.
- Source : réponse 22P, « Ce qui ne se voit qu'à l'échelle du programme », points 1 et 5, table, décision 1 (`cb010f4cbd12b5fb`).
- État : proposé non tranché (recommandation a, confiance 0,65).
- Liens : papiers A, B, C ; N-075 (sondes accélérateur, non garantie) ; plancher d'audit au hasard ; Greenblatt et collaborateurs 2023 ; Horvitz et Thompson 1952 (à citer, non vérifiés sur PDF).
- Ce qui l'attaque : rapport de rejet « trois papiers de mesure sans théorème, qu'y a-t-il de propre ? » ; trois énoncés en vigueur écrivent encore « garantie toujours valide » (accumulation, statistique conjointe, juge au nul) alors que sous référence estimée c'est une validité conditionnelle.
- Inventaire : rattachée à 2.1 (le plancher d'audit au hasard porte la garantie).

#### [F22-03] Rapport de rejet le plus fort, écrit avant de garder un énoncé
- Définition : pour chaque énoncé gardé, écrire d'avance le reproche le plus dur qu'un relecteur ferait (« évident », « déjà fait », « vrai par construction ») ; à l'échelle du programme, écrire le rapport de rejet du programme entier.
- Synonymes et paraphrases : « avocat du diable », « rejet le plus fort », « que reste-t-il de propre ».
- Source : réponse 22, § 1 (`22c5652113797a39`) ; réponse 22P, § 1 (`cb010f4cbd12b5fb`).
- État : proposé non tranché.
- Liens : énoncés vrais par construction ; phrases à ne plus écrire.
- Ce qui l'attaque : aucun ; coût de rédaction.
- Inventaire : nouveau.

---


**B. Retraits et leur propagation**


#### [F22-04] Propagation des retraits par graphe des appuis
- Définition : un retrait ne s'arrête pas à sa ligne ; il faut dresser le graphe des revendications qui supposent le lemme d'additivité ou le théorème négatif, et récrire celles qui s'y adossent. Quatre revendications sont touchées : accumulation, courbe selon le nombre d'agents, co-élévation, statistique conjointe.
- Synonymes et paraphrases : « graphe des appuis », « graphe des dépendances », « socle parti », « propager tout retrait ».
- Source : réponse 22, conclusion et § 1 (`22c5652113797a39`) ; réponse 22P, § 1 et point 1 de la demande reformulée (`cb010f4cbd12b5fb`).
- État : proposé non tranché (décision 2 de la réponse 22, recommandation a, 0,65).
- Liens : table des revendications version 2 ; papiers A et B.
- Ce qui l'attaque : risque de retrait excessif.
- Inventaire : nouveau.

#### [F22-05] Lemme d'additivité, retiré comme résultat ; question de l'étalement en séquentiel
- Définition : le lemme selon lequel le dommage se répartit additivement sans gain pour le saboteur est retiré comme résultat (ses composantes sont publiées : Avenhaus et Jaech 1981 ; Ker 2006 ; Tailor ; Ghanem ; Khilar, proposition 3) et cité comme outil. Il en reste une question : en détection séquentielle, l'étalement du sabotage est-il le cas le moins favorable au défenseur (décalage additif sans compensation) ?
- Synonymes et paraphrases : « lemme L », « additivité », « le lemme », « étaler est-il optimal », « tôt, tard, étalé ».
- Source : réponse 22, table, ligne « Lemme d'additivité » ; réponse 22A, table, ligne « (L) ».
- État : retiré (décidé, identifiant non vu) ; la question est ouverte ; le repli de N-004 « sans nouvelle décision » est à fermer (proposé).
- Liens : papier A ; N-004 ; simulation du franchissement séquentiel.
- Ce qui l'attaque : occupé par Avenhaus et Jaech, Ker 2006, Tailor 2510.04303, Ghanem 2608.02698, Khilar 2610.13083.
- Inventaire : nouveau.

#### [F22-06] Fermeture du repli du lemme prévu par N-004
- Définition : N-004 laisse un repli qui permettrait de revenir au lemme « sans nouvelle décision » ; Fable propose de le fermer par une ligne au registre pour empêcher un retour silencieux du lemme.
- Synonymes et paraphrases : « repli de N-004 », « repli du lemme disponible », « retour silencieux du lemme ».
- Source : réponse 22, table ; réponse 22A, décision 5 (`2255a6a3a65ba04c`) ; réponse 22P, table.
- État : proposé non tranché (confiance 0,7).
- Liens : lemme d'additivité ; N-004.
- Ce qui l'attaque : aucun.
- Inventaire : nouveau.

#### [F22-07] Théorème négatif retiré ; distinction attaque par permutation contre attaque à marginales préservées
- Définition : le théorème « puissance égale au taux de faux positifs » contre un saboteur qui préserve les marginales est retiré comme résultat (Zhang et Gao 2606.10456 ; Arias-Castro et collaborateurs 2012 ; Khilar ; Rose et collaborateurs). La seule pièce exacte qui reste : la forme est vraie quand l'attaque préserve le multi-ensemble des scores (permutation), fausse quand elle ne préserve que les marginales par coordonnée, distinction déjà posée par N-003 ; à garder en remarque citée.
- Synonymes et paraphrases : « théorème T », « théorème d'aveuglement », « T (c) à (f) », « permutation contre marginales », « aveuglement des statistiques de marginales ».
- Source : réponse 22, table et décision 3 ; réponse 22A, table, constat 3.
- État : retiré (décidé) ; remarque citée proposée (décision 3 de la réponse 22, option a, 0,6) ; « unification par permutations » : question.
- Liens : N-003 ; papiers A et B ; question position ou dépendance ; recalcul du tableau 2 de Zhang et Gao.
- Ce qui l'attaque : retrait excessif possible, car la critique visait la lettre du programme version 2, déjà bornée par N-003 ; aucun crédit de nouveauté.
- Inventaire : nouveau.

#### [F22-08] Garde contre le retrait excessif
- Définition : ne pas retirer plus que ce que l'antériorité touche : N-003 avait déjà borné le théorème ; la loi de déférence et le second terrain du papier C ne sont pas touchés par des pièces qui parlent d'autre chose. Signaler tout retrait excessif fait partie de chaque demande reformulée.
- Synonymes et paraphrases : « retrait excessif », « ne pas tout jeter », « critique de la lettre version 2 ».
- Source : réponse 22, § 1 ; réponse 22A, thèse revue ; réponse 22C, « Sur la thèse du papier C » ; réponse 22P, point 6.
- État : proposé non tranché.
- Liens : théorème négatif ; papier C ; mode commun des revues.
- Ce qui l'attaque : le biais partagé des revues peut jouer dans les deux sens.
- Inventaire : nouveau.

#### [F22-09] Table des revendications à refaire (version 2)
- Définition : la table du 19 novembre s'arrête à N-074, « ne fait pas foi », ignore N-075 à N-077 et montre encore la marge asymétrique comme « resserrée » ; Fable propose une version 2 provisoire tout de suite, scellée après le collisionneur, avec les retraits propagés.
- Synonymes et paraphrases : « table en vigueur » (à ne plus dire), « table v2 », « table des revendications du 19 novembre ».
- Source : réponse 22, § 1 et décision 2 (`22c5652113797a39`) ; réponse 22P, ordre des travaux, étape 1.
- État : proposé non tranché (option a, 0,65).
- Liens : N-077 ; propagation des retraits ; tous les papiers.
- Ce qui l'attaque : deux passes ; option rivale « attendre le collisionneur ».
- Inventaire : nouveau.

#### [F22-10] Marge asymétrique, déjà retirée (ligne de table à corriger)
- Définition : la marge asymétrique (H6) a quitté les hypothèses revendiquées du papier A par N-077 ; elle reste une mesure descriptive. La table du 19 novembre la donne encore « resserrée » : à corriger.
- Synonymes et paraphrases : « H6 », « marge asymétrique resserrée » (à ne plus écrire), « marge contre un saboteur diffus ».
- Source : réponse 22 et 22A, tables et phrases à ne plus écrire ; réponse 22P, phrase 7.
- État : retiré (N-077, GO-2026-11-21-64 selon les consignes du dépôt).
- Liens : papier A ; N-077 ; bras « adversaire entraîné » descriptif.
- Ce qui l'attaque : —
- Inventaire : nouveau.

---


**C. Papier A : accumulation, nul effectif, porte G1**


#### [F22-11] Accumulation toujours valide, remplacée par l'énoncé « écart au nul »
- Définition : « un rappel qui croît avec l'horizon » découle de la loi en racine tant que l'horizon reste sous la taille de la référence : l'énoncé est vrai par construction. Énoncé neuf : à déplacement par acte fixé, le rappel suit le nul hérité (racine, terme entre tâches, dérive) ; la garantie vaut sous une référence honnête déclarée ; l'écart au nul est le résultat.
- Synonymes et paraphrases : « H2 », « garantie toujours valide », « rappel croissant avec l'horizon », « écart au nul », « l'accumulation ».
- Source : réponse 22, table et constat 1 ; réponse 22A, table, décision 1 ; réponse 22P, désaccords (« à remplacer » l'emporte sur « à resserrer »).
- État : proposé non tranché (22A décision 1, option a, 0,7).
- Liens : papier A ; N-076 ; essai jumeau contre jumeau ; préenregistrement de G1 à récrire.
- Ce qui l'attaque : Ker 2010, p. 7 et 11 ; Filler, Ker, Fridrich 2009 ; Khilar, propositions 3-4 ; Makins et collaborateurs 2607.07368. Épreuve de mort : la surface du seuil honnête s'ajuste au nul sans résidu (exposant un demi, terme entre tâches nul).
- Inventaire : nouveau.

#### [F22-12] Plafond au-delà de n = m (seuil de Ker 2010)
- Définition : à déplacement par acte fixé, au-delà d'un horizon n égal à la taille m de la référence, le seuil de Ker 2010 prédit un plafond : la détection ne dépend plus que du déplacement et de m. Le résultat du programme serait l'écart à cette courbe, non la courbe.
- Synonymes et paraphrases : « bascule en n ≈ m », « plafond de la référence », « détection bornée par m ».
- Source : réponse 22, « Quatre constats », point 1.
- État : hypothèse de Fable ; arbitrée par la réponse 22P : le nul s'écrit par plan de référence (plafond valable pour une référence courte).
- Liens : nul effectif avec exécutions jumelles ; N-076.
- Ce qui l'attaque : réponse 22A : avec des jumelles, ce régime n'est pas observable.
- Inventaire : nouveau.

#### [F22-13] Nul effectif avec exécutions jumelles : racine, terme entre tâches, dérive
- Définition : avec r exécutions jumelles par tâche, m = r·n et le seuil reste en racine, gonflé de √(1 + 1/r) ; le régime n/√m ne s'observe que si une référence courte est extrapolée. Le nul à ajuster : variance du cumul ≈ σ²·n^(2H)·(1 + 1/r) + τ²·n², où H est l'exposant et τ l'écart entre tâches ; ce que le papier mesure, ce sont H et τ.
- Synonymes et paraphrases : « nul effectif », « pas √(n + n²/m) », « racine plus terme entre tâches plus dérive », « régime n/√m inobservable », « exposant H », « Hurst ».
- Source : réponse 22A, constat 1 (`2255a6a3a65ba04c`).
- État : hypothèse (dérivation de Fable, à vérifier) ; proposé non tranché.
- Liens : papier A ; plan de référence ; terme entre tâches ; banc à vérité plantée.
- Ce qui l'attaque : stationnarité ; dérivation non vérifiée par un tiers.
- Inventaire : nouveau.

#### [F22-14] Terme entre tâches, prévision la plus sûre à sceller
- Définition : le terme τ (écart systématique entre tâches) croît comme n dans le cumul et se décèle bien plus tôt que l'exposant ; avec une référence par régime, Fable prévoit qu'il domine avant la fin des tâches longues. Ordre proposé : sceller d'abord τ, puis le rapport des constantes sonde-juge indépendant de l'horizon, puis le gain d'union, l'exposant restant sans prévision tant que la puissance manque.
- Synonymes et paraphrases : « τ », « tau », « terme entre tâches », « ordre des prévisions », « prévisions par ordre de solidité ».
- Source : réponse 22A, constat 4, thèse revue, décision 4.
- État : proposé non tranché (0,75) ; chances en jugement données par Fable, non mesurées.
- Liens : papier A ; calcul de puissance ; N-076 (prévision scellée avant G1).
- Ce qui l'attaque : un plan à référence par tâche seule supprime τ.
- Inventaire : nouveau.

#### [F22-15] Hypothèse la plus exposée : la stationnarité des pas
- Définition : Filler, Ker et Fridrich gardent l'exposant un demi sous une chaîne stationnaire ; or une tâche d'agent a un début et une fin. La stationnarité est donc l'hypothèse à éprouver en premier.
- Synonymes et paraphrases : « stationnarité », « tâche à début et fin », « hypothèse la plus exposée ».
- Source : réponse 22 et 22A, thèse revue.
- État : ouvert (question).
- Liens : nul effectif ; substituts par permutation.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [F22-16] Plan de référence : par tâche, par régime, ou les deux
- Définition : choisir avant de sceller si la référence honnête se forme par tâche (jumelles, sans terme τ, indisponible pour une tâche nouvelle en service) ou par régime (déployable, mais τ peut tout dominer). Fable recommande de mesurer les deux sur les mêmes exécutions : leur comparaison est le résultat propre.
- Synonymes et paraphrases : « unité de m », « référence par tâche », « référence par régime », « jumelles ».
- Source : réponse 22A, décision 2 (0,65).
- État : proposé non tranché.
- Liens : nul effectif ; N-076 ; harnais honnête unique.
- Ce qui l'attaque : analyse plus lourde.
- Inventaire : nouveau.

#### [F22-17] Référence du seuil de la porte G1 : nombre d'épisodes honnêtes et intervalle du taux réel
- Définition : un rappel « à 1 % de faux positifs » suppose un quantile honnête connu, alors qu'il est estimé sur un nombre fini d'épisodes ; deux moniteurs comparés « à 1 % » peuvent l'être à des taux réels très différents. Chaque seuil déclare son nombre d'épisodes honnêtes et l'intervalle (loi bêta) de son taux réel ; la référence pourrait monter vers un millier d'épisodes.
- Synonymes et paraphrases : « G1 a sa propre référence », « seuil estimé », « 99e centile de 200 épisodes », « intervalle bêta », « facteur dix entre moniteurs ».
- Source : réponse 22A, constat 2, table ligne « Porte G1 », décision 3.
- État : proposé non tranché (option a, repli b, 0,6) ; ordre de grandeur de Fable, à refaire.
- Liens : porte G1 ; N-076 étendue à l'épisode.
- Ce qui l'attaque : option rivale : passer à 5 % change une porte fixée ; coût du calcul honnête.
- Inventaire : nouveau.

#### [F22-18] Calcul de puissance du plan avant scellement (et l'issue indéterminée)
- Définition : « deux issues publiables » en cache une troisième, l'issue indéterminée. Calculer, par modèle à composantes de variance et rééchantillonnage par tâche, le plus petit écart décelable sur l'exposant et sur le terme entre tâches ; sans ce compte la prévision sur l'exposant n'est pas réfutable. Ordre de grandeur de Fable : de l'ordre de 150 tâches indépendantes à chaque extrémité d'une décade d'horizons pour l'exposant.
- Synonymes et paraphrases : « puissance du plan », « troisième issue », « issue indéterminée », « plus petit écart décelable », « composantes de variance ».
- Source : réponse 22, § 1, thèse revue, décision 4 ; réponse 22A, constat 4.
- État : proposé non tranché (0,75 ; repli : réduire la thèse aux termes mesurables).
- Liens : tous papiers ; banc à vérité plantée ; budget honnête commun.
- Ce qui l'attaque : quelques jours de délai.
- Inventaire : nouveau.

#### [F22-19] Banc à vérité plantée (scores synthétiques de paramètres connus)
- Définition : avant de lire des données réelles, fabriquer des scores synthétiques d'exposant et de terme entre tâches connus (papier A), une coalition de position seule puis de dépendance seule (papier B), un juge synthétique de gain et de destination connus (papier C), et vérifier que l'ajustement retrouve ce qu'on y a mis.
- Synonymes et paraphrases : « banc planté », « vérité plantée », « retrouver ce qu'on a planté », « contrôle de l'ajustement ».
- Source : réponse 22, § 3 ; 22A, § 3 ; 22B, § 3 ; 22C, § 3 ; 22P, § 3.
- État : proposé non tranché.
- Liens : N-076 (« banc à vérité plantée, à faire ») ; calcul de puissance.
- Ce qui l'attaque : un banc synthétique ne garantit pas que les données réelles suivent le modèle.
- Inventaire : voisin de 2.7 (hasard du défenseur et banc à vérité plantée, N-076) ; sinon nouveau.

#### [F22-20] Essai « jumeau contre jumeau » (honnête contre honnête)
- Définition : faire tourner le dispositif sur des exécutions honnêtes jumelles seules, sans saboteur, pour mesurer la surface du seuil honnête, les composantes de variance, la corrélation entre copies et la variance des verdicts d'un juge sur un même contenu. Son issue ne dépend d'aucun avis.
- Synonymes et paraphrases : « jumeau contre jumeau », « essaim honnête contre essaim honnête », « harnais honnête », « juge sans attaque ».
- Source : réponses 22 (§ 4), 22A (§ 4, table), 22B (§ 4), 22C (§ 2), 22P (harnais unique).
- État : proposé non tranché.
- Liens : harnais honnête unique ; accumulation ; corrélation honnête entre copies.
- Ce qui l'attaque : coût en exécutions honnêtes.
- Inventaire : voisin de 2.19 (netteté de la référence) ; nouveau comme essai.

#### [F22-21] Recalcul du tableau 2 de Zhang et Gao, et « antécédent défectueux » remplacé par « limite à longueur finie »
- Définition : l'attaque de Zhang et Gao préserve les marginales par coordonnée, non le multi-ensemble à longueur finie ; sous autocorrélation, la variance de la moyenne change, et leur tableau 2 se recalcule à la main depuis un paramètre. Tant que ce recalcul n'est pas fait, ne pas dire « antécédent défectueux », mais « proposition exacte quand le multi-ensemble est préservé ; limite à longueur finie, notre lecture ».
- Synonymes et paraphrases : « antécédent défectueux », « réserve sur 2606.10456 », « rejouer le tableau 2 », « copule autorégressive d'ordre 1 ».
- Source : réponse 22, § 3 et phrase 7 ; réponse 22A, constat 3 ; réponse 22P, désaccords (recalcul d'abord, simulation ensuite).
- État : proposé non tranché ; question fermée à poser aux auteurs.
- Liens : théorème négatif ; N-003.
- Ce qui l'attaque : le paramètre publié peut s'écarter de la valeur prédite, alors la lecture est à revoir.
- Inventaire : nouveau.

#### [F22-22] Simulation du franchissement séquentiel : sabotage tôt, tard, étalé
- Définition : à budget égal, simuler le taux de franchissement du seuil séquentiel selon que le sabotage tombe tôt, tard ou étalé ; des taux égaux réfuteraient la question laissée par le retrait du lemme.
- Synonymes et paraphrases : « tôt, tard, étalé », « simulation séquentielle », « première simulation ».
- Source : réponse 22, § 3 et table ; 22A, § 3.
- État : proposé non tranché.
- Liens : lemme d'additivité.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [F22-23] Substituts par permutation des pas ou par échange de copies
- Définition : rompre la dépendance en gardant les marginales : permuter les pas d'une exécution (papier A) ou échanger des copies entre essaims honnêtes d'une même tâche (papier B). C'est le nul naturel de la question « position ou dépendance ».
- Synonymes et paraphrases : « substituts », « surrogates », « échange de copies », « permutation des pas ».
- Source : réponse 22, § 3 ; 22B, § 3 ; 22P, § 3.
- État : proposé non tranché.
- Liens : question position ou dépendance ; théorème négatif.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [F22-24] Complémentarité à taux total égal : union « meilleure boîte noire et sonde » contre union « meilleure boîte noire et seconde boîte noire d'une autre lignée »
- Définition : le gain de l'accès interne (H1a) se lit en second axe comme un écart entre deux unions de moniteurs recalées au même taux total de fausses alertes. Conditionner sur les seuls sabotages manqués par la meilleure boîte noire avantage tout moniteur peu corrélé au premier : seule la comparaison des deux unions est juste.
- Synonymes et paraphrases : « H1a », « gain de l'accès interne », « second axe », « la sonde voit ce que le texte manque » (à ne plus écrire seul), « union recalée », « biais de conditionnement ».
- Source : réponse 22, table et thèse revue ; 22A, table ; 22P, table ; 23, B2.
- État : tenue, resserrée (proposé non tranché).
- Liens : papier A ; papier C (quorum) ; métrique d'union unique ; lot sous scellés.
- Ce qui l'attaque : Parrack, Attubato, Heimersheim 2025 (parent ; indice contraire : boîte blanche sous la boîte noire sur les portes dérobées dans le code, p. 7-8) ; 13 pages lues sur 39. Épreuve : borne haute de l'écart inférieure ou égale à zéro sur la famille tenue à l'écart.
- Inventaire : 2.20 (la seconde boîte noire).

#### [F22-25] Indice contraire écrit à côté de la prévision
- Définition : à côté de la prévision du gain de l'accès interne, écrire l'indice publié contraire : chez Parrack et collaborateurs, la boîte blanche fait moins bien que la boîte noire sur les portes dérobées dans le code.
- Synonymes et paraphrases : « indice contraire », « chiffre contraire de Parrack ».
- Source : réponse 22, thèse revue ; 22A, table et phrase 6.
- État : proposé non tranché.
- Liens : complémentarité ; papier A.
- Ce qui l'attaque : —
- Inventaire : 2.20.

#### [F22-26] Transposition du jeton à l'action, ramenée à une question
- Définition : « angle mort identifié » devient une question : la robustesse du maximum mesurée au niveau du jeton tient-elle au niveau de l'action, sous fragmentation ? Makins et collaborateurs montrent que le maximum baisse sous fragmentation ; Arias-Castro et collaborateurs que l'histogramme est puissant en régime rare.
- Synonymes et paraphrases : « Tr », « du jeton à l'action », « angle mort identifié », « fragmentation ».
- Source : réponse 22A, table ; 22P, table.
- État : proposé non tranché (« à resserrer en question »).
- Liens : papier A.
- Ce qui l'attaque : Makins 2607.07368, p. 1. Épreuve : le maximum par action ne baisse pas sous fragmentation.
- Inventaire : nouveau.

#### [F22-27] Interaction flou contre net (H1b), validité et robustesse (H8)
- Définition : deux revendications du papier A non touchées par les pièces : l'interaction entre tâches floues et nettes (mesure, H1b) et le diagnostic de validité et robustesse (H8), dont la réponse 22P propose qu'il soit rapporté dans A à chaque cycle et que la revendication de construit aille au papier C, comme l'écrit N-062.
- Synonymes et paraphrases : « H1b », « H8 », « flou-net », « validité de construit ».
- Source : réponse 22A, table ; 22P, désaccords tranchés.
- État : non touchées ; attribution de H8 proposée non tranchée.
- Liens : papiers A et C ; N-055 ; N-062.
- Ce qui l'attaque : —
- Inventaire : nouveau.

---


**D. Papier B : l'essaim**


#### [F22-28] Deux sens de « co-élévation » : hausse commune de position contre excès de dépendance
- Définition : le mot « co-élévation » recouvre deux objets, chacun avec un nul hérité : une hausse commune de la moyenne dans k copies sur n (détection de signal rare ou dense, somme contre maximum), et un excès de corrélation entre copies à marginales intactes (cadre d'Arias-Castro et collaborateurs 2012). Fable propose deux statistiques nommées, rapportées côte à côte.
- Synonymes et paraphrases : « co-élévation entre copies », « volets (a) à (d) », « position ou dépendance », « coalition de taille inconnue ».
- Source : réponse 22B, conclusion, § 1, décision 3 (0,7).
- État : proposé non tranché (réécriture de N-069).
- Liens : papier B ; N-069 ; question position ou dépendance.
- Ce qui l'attaque : part empirique occupée par Rose et collaborateurs, 2607.06807, 2611.10620, Khilar ; « premières statistiques de dépendance entre copies », « inédit », « cœur vierge » à ne plus écrire.
- Inventaire : nouveau.

#### [F22-29] Question pivot « position ou dépendance »
- Définition : le sabotage joué par les organismes déplace-t-il la position des scores de sondes, leur dépendance, ou les deux ? Tests de position et de dépendance étalonnés sur substituts permutés. C'est une section du papier A et l'ouverture du papier B ; Fable propose d'en faire une porte du programme, placée après G1 et avant G2.
- Synonymes et paraphrases : « question pivot », « position ou dépendance », « question de diagnostic », « une expérience décide de deux papiers ».
- Source : réponse 22, table ; 22A, table ; 22B ; 22P, point 3 et décision 4 (0,6).
- État : ouvert (question) ; porte proposée non tranchée.
- Liens : papiers A et B ; repli du papier B ; substituts.
- Ce qui l'attaque : épreuve : aucun test ne dépasse son niveau sur substituts.
- Inventaire : nouveau.

#### [F22-30] Somme globale, meilleur test au pire cas contre un total réparti, base obligatoire
- Définition : sous covariance gaussienne connue et taille fixe, la somme des écarts est le test le plus puissant au pire cas contre un total réparti, dans l'espace comme dans le temps (Avenhaus et Jaech 1981, p. 25 et 30). Toute statistique conjointe doit d'abord se mesurer à elle ; si le sabotage décale additivement, rien ne la bat dans ce cadre.
- Synonymes et paraphrases : « somme globale », « base somme », « indifférence de la somme à la répartition », « test de la somme », « Avenhaus et Jaech ».
- Source : réponse 22, constat 2 ; 22B, constat 1 ; 22P.
- État : occupé par la littérature (cité, base nommée) ; proposé comme base obligatoire.
- Liens : statistique conjointe ; porte G2 ; papier B.
- Ce qui l'attaque : cadre gaussien et taille fixe ; ne vaut plus tel quel sous corrélation honnête.
- Inventaire : nouveau.

#### [F22-31] Frontière héritée de détection des corrélations, et son extension dans le temps
- Définition : le carré de la somme est puissant quand ρ·k²/n tend vers l'infini et sans puissance quand k²/n tend vers zéro, où le test d'histogramme prend le relais (Arias-Castro et collaborateurs, p. 14-20). Sur T pas indépendants, Fable dérive que le cumul des carrés de la somme détecte quand ρ·k²·√T/n est grand : l'horizon achète de la détectabilité, nul du gain « conjoint dans le temps ».
- Synonymes et paraphrases : « frontière héritée », « carré de la somme », « test d'histogramme », « régime rare », « l'horizon achète ».
- Source : réponse 22B, constat 2.
- État : frontière occupée (citée) ; extension temporelle hypothèse non vérifiée, non cherchée dans la littérature.
- Liens : co-élévation ; statistique conjointe.
- Ce qui l'attaque : frontière asymptotique : pour une dizaine de copies, dense et rare se confondent.
- Inventaire : nouveau.

#### [F22-32] Corrélation honnête entre copies, terme de référence de l'essaim
- Définition : des copies à poids partagés sur un même travail ne sont pas indépendantes, alors que le nul hérité le suppose. Avec une corrélation honnête ρ₀, la variance de la somme vaut n·σ²·(1 + (n − 1)·ρ₀) ; l'excès décelable est borné par l'erreur d'estimation de ρ₀ et sa variation entre tâches. L'unité de référence devient l'essaim honnête.
- Synonymes et paraphrases : « ρ₀ », « référence estimée de l'essaim », « copies non indépendantes », « sous le nul les copies sont indépendantes » (à ne plus écrire).
- Source : réponse 22, constat 3 ; 22B, constat 3.
- État : hypothèse ; prévision proposée (positive et dépendante de la tâche).
- Liens : N-076 étendue ; papier B ; courbe selon le nombre d'agents.
- Ce qui l'attaque : puissance : plus de cent essaims par bras estimés par Fable (à refaire).
- Inventaire : nouveau.

#### [F22-33] Cinq statistiques sur les mêmes scores, recalées au même taux
- Définition : comparer sur les mêmes scores d'essaim, recalées au même taux de fausses alertes sur essaims honnêtes : somme globale, maximum par copie, carré de la somme, balayage de sous-groupes, test d'histogramme ; avec simulation à taille finie aux tailles du programme.
- Synonymes et paraphrases : « cinq statistiques », « balayage », « scan », « higher criticism ».
- Source : réponse 22B, § 3.
- État : proposé non tranché.
- Liens : porte G2 ; Ingster 1997, Donoho et Jin 2004, Kulldorff 1997 (cités de mémoire).
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [F22-34] Statistique conjointe dans le temps et entre agents, remplacée
- Définition : l'énoncé « bat le séquentiel par agent et la coupe transversale » est remplacé : base obligatoire la somme globale ; gain revendiqué sur la seule strate où le sabotage déplace la dépendance, l'égalité ailleurs étant le résultat attendu ; garantie sous une référence de corrélation honnête de taille déclarée ; adversaire entraîné en mesure descriptive.
- Synonymes et paraphrases : « statistique conjointe », « garantie toujours valide tenue sous dépendance », « temps et agents, un même objet » (déjà chez Avenhaus et Jaech).
- Source : réponse 22, table ; 22B, table.
- État : proposé non tranché.
- Liens : papier B ; N-069 ; N-077 ; Podkopaev et collaborateurs 2023 (test séquentiel d'indépendance, non vérifié sur PDF).
- Ce qui l'attaque : Zhang et Gao, proposition 2 ; Khilar ; épreuve : aucun gain sur la somme à fausses alertes égales dans la strate dépendance.
- Inventaire : nouveau.

#### [F22-35] Courbe de sécurité selon le nombre d'agents, écrite par agrégateur
- Définition : à budget et nombre total d'actions fixés, la détection baisse avec le nombre d'agents sous le maximum, et sous la somme globale elle ne baisse que par le terme de corrélation honnête ; la sonde change la constante, non la forme. Arbitrage de 22P : la somme n'est pas « plate » (22 supposait l'indépendance), 22B prévaut.
- Synonymes et paraphrases : « courbe selon le nombre d'agents », « décroît plus doucement » (à ne plus écrire), « somme plate ».
- Source : réponse 22, table ; 22B, table ; 22P, désaccords.
- État : proposé non tranché.
- Liens : papier B ; corrélation honnête.
- Ce qui l'attaque : Avenhaus et Jaech, p. 25, 31 ; Makins, p. 1 ; épreuve : la somme baisse plus que le prédit ρ₀.
- Inventaire : nouveau.

#### [F22-36] Nombre et diversité des moniteurs : retirée comme loi, gardée comme mesure
- Définition : la loi « la sécurité croît par la diversité effective » paraît élémentaire (nombre effectif sous corrélation, Kish 1965, de mémoire) ; Fable propose de la garder comme mesure de la corrélation des erreurs entre moniteurs et du gain d'union à taux total égal, versée à la métrique d'union commune.
- Synonymes et paraphrases : « diversité des moniteurs », « diversité effective », « nombre effectif », « matrice de transfert » (instrument).
- Source : réponse 22, table ; 22B, table et décision 5 ; 22P, table.
- État : proposé non tranché.
- Liens : papiers B et C ; métrique d'union.
- Ce qui l'attaque : élémentaire.
- Inventaire : nouveau.

#### [F22-37] Diversification contre coordination : un signe à sceller
- Définition : diversifier les copies réduit la corrélation honnête, mais peut aussi réduire le signal commun des copies qui sabotent ; Fable propose d'ajouter une prévision de signe.
- Synonymes et paraphrases : « diversification », « coordination ».
- Source : réponse 22B, table.
- État : proposé non tranché.
- Liens : papier B ; riposte et fuite (non touchée) ; survie d'une contrainte à la délégation (mesure, non touchée).
- Ce qui l'attaque : épreuve : signal de dépendance inchangé sous diversification.
- Inventaire : nouveau.

#### [F22-38] Borne d'indétectabilité et bras « adversaire entraîné contre la statistique » descriptif
- Définition : une campagne qui épouse la loi conjointe honnête est indétectable (Khilar, proposition 1) ; le bras où un adversaire est entraîné contre la statistique tend vers ce cas, d'où son statut de mesure descriptive.
- Synonymes et paraphrases : « y compris sous un adversaire entraîné » (à ne plus revendiquer), « borne déclarée ».
- Source : réponse 22B, thèse revue et décision 5.
- État : proposé non tranché (cohérent avec N-077).
- Liens : N-077 ; papier B.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [F22-39] Repli scellé du papier B : section du papier A si seule la position bouge
- Définition : si le sabotage joué ne déplace que la position, la somme globale suffit et il reste la corrélation honnête mesurée, la forme de la courbe sous la somme et le résultat négatif « la somme suffit » : une section du papier A, non un papier. Ce repli s'écrit d'avance.
- Synonymes et paraphrases : « survie du papier B », « fondre B dans A », « la somme suffit ».
- Source : réponse 22B, conclusion, thèse revue, décision 2 ; 22P, ordre des travaux, étape 7.
- État : proposé non tranché (0,6).
- Liens : question pivot ; papiers A et B.
- Ce qui l'attaque : option « fondre d'emblée » renonce avant la mesure.
- Inventaire : nouveau.

#### [F22-40] Thèse du papier B reformulée et porte G2 révisée
- Définition : thèse : un sabotage réparti dans un essaim a deux nuls hérités (somme globale pour la position ; frontière des corrélations pour la dépendance) ; on mesure la corrélation honnête, ce que le sabotage déplace, et ce que la lecture conjointe ajoute à la somme. La porte G2 ajoute comme bases nommées la somme globale et le carré de la somme, précédée de l'essai sur essaims honnêtes et d'un calcul de puissance en essaims.
- Synonymes et paraphrases : « thèse de N-069 », « porte G2 », « papier sur l'essaim ».
- Source : réponse 22B, thèse revue, décisions 2 et 4 (0,75).
- État : proposé non tranché.
- Liens : N-069 (le pic par agent, base nommée de G2) ; papier B.
- Ce qui l'attaque : papier de mesure, peut-être mince ; coût en essaims honnêtes.
- Inventaire : nouveau.

---


**E. Papier C : juges de la recherche automatisée sous attaque**


#### [F22-41] Loi de déférence : nul par retrait vers le centre (bras placebo) et identifiabilité
- Définition : sur une échelle bornée, toute perturbation tire un verdict vers le centre du corpus ; la destination « moyenne du corpus » est donc le nul, mesuré par un bras placebo (perturbation neutre de même longueur et position). Dans Δv = g·(ĉ − v₀), une seule intensité n'identifie que le produit : séparer g de ĉ exige que v₀ ou l'intensité varient.
- Synonymes et paraphrases : « loi de déférence à destination libre », « HC1 », « régression vers la moyenne », « bras placebo », « g et ĉ ».
- Source : réponse 22C, § 1, table, décision 3 (0,7).
- État : proposé non tranché (« à resserrer »).
- Liens : papier C ; N-005, N-006 ; banc à vérité plantée.
- Ce qui l'attaque : épreuve : ĉ sous attaque indiscernable de ĉ sous placebo ; forme déjà citée (psychologie du conseil).
- Inventaire : nouveau.

#### [F22-42] Prédictions d'absence d'effet récrites en équivalence (marge scellée et contrôle positif)
- Définition : « le gain de la sonde est nul » ne peut pas échouer ; il s'écrit en équivalence : le gain de la sonde reste sous une marge scellée (fraction du gain du juge), par double test unilatéral (Schuirmann 1987, de mémoire), avec un contrôle positif (sonde volontairement contaminée par le style) qui prouve que le banc voit un déplacement.
- Synonymes et paraphrases : « g ≈ 0 » (à ne plus écrire), « déplacement nul », « TOST », « marge d'équivalence », « contrôle positif ».
- Source : réponse 22C, § 1, § 3, table, décision 2 (0,8).
- État : proposé non tranché.
- Liens : papier C (déplacement de la sonde de l'agent auteur, usurpation de l'instructeur) ; HC2 (N-068) ; porte GC qui lirait une marge d'équivalence (22P).
- Ce qui l'attaque : la marge se discute ; Parrack et collaborateurs ; N-075 (sondes accélérateur, non garantie).
- Inventaire : nouveau.

#### [F22-43] Taxe de déplacement resserrée
- Définition : « le contexte seul n'y suffit pas » devient : pour les classes d'attaquant mesurées, en contexte seul, aucun déplacement de la sonde de l'agent auteur au-dessus de la marge, pour un budget de requêtes déclaré.
- Synonymes et paraphrases : « taxe de déplacement », « contexte seul », « classe d'attaquant et budget ».
- Source : réponse 22C, table.
- État : proposé non tranché.
- Liens : papier C ; N-077 ; Bailey et collaborateurs 2024, « Obfuscated Activations Bypass LLM Latent-Space Defenses » (de mémoire : des entrées seules y déplaceraient des sondes).
- Ce qui l'attaque : Bailey et collaborateurs ; épreuve : une attaque en contexte seul franchit la marge dans le budget.
- Inventaire : nouveau.

#### [F22-44] Quorum par type d'accès, remplacé dans sa forme
- Définition : à taux total de fausses alertes égal, le quorum « juge et sonde » résiste-t-il à plus d'attaques de corruption que le quorum « deux juges de lignées différentes » ? La matrice de transfert est rapportée avec la corrélation des erreurs sans attaque.
- Synonymes et paraphrases : « quorum par type d'accès », « matrice de transfert », « le quorum est plus robuste » (à ne plus écrire seul).
- Source : réponse 22C, table ; 22P, table.
- État : proposé non tranché.
- Liens : papier C ; complémentarité du papier A ; porteur unique de la comparaison.
- Ce qui l'attaque : Parrack et collaborateurs (moniteur de texte recevant des scores de sondes, voisin) ; Arias-Castro et collaborateurs.
- Inventaire : 2.20 (voisin).

#### [F22-45] Le gain bénin prédit la robustesse, resserré
- Définition : « prédit l'effondrement sous attaque optimisée » devient : le rang des moniteurs par gain sous attaques écrites d'avance prédit leur rang sous les attaques adaptatives mesurées ; le corpus bénin est hors d'atteinte de l'agent jugé ; nombre de moniteurs fixé par calcul de puissance.
- Synonymes et paraphrases : « gain bénin », « attaque optimisée » (à ne plus écrire), « corrélation de rang ».
- Source : réponse 22C, table et thèse.
- État : proposé non tranché.
- Liens : N-077 ; papier C.
- Ce qui l'attaque : Khilar (étalonnage empoisonnable) ; contre-indice déjà au dépôt (non lu ici) ; une prédiction de rangs sur une poignée de moniteurs est presque toujours indéterminée.
- Inventaire : nouveau.

#### [F22-46] Juge statistique du second terrain : l'archive comme référence que le proposeur peut nourrir
- Définition : le juge au nul formé des lois connues repose sur une archive « entière et croissante », référence estimée ; une référence légèrement fausse donne des faux positifs presque sûrs (Ker 2010), et un proposeur qui nourrit l'archive peut élargir son budget. Fable propose une grille (taille m de l'archive, nombre n de propositions) et deux bras : « proposeur nourrit l'archive » contre « archive gelée », avec déclaration du droit d'écriture.
- Synonymes et paraphrases : « juge au nul », « O4 », « O2 », « archive nourrie », « grille (m, n) », « attaque de Goodhart », « surface d'attaque est l'archive ».
- Source : réponse 22C, constat 3, table, décision 4 (0,55).
- État : tenu, complété (proposé non tranché, après avis d'un statisticien).
- Liens : organisme d'idéation ; papier C ; N-064, N-067, N-071 ; N-076 étendue ; Dwork et collaborateurs, Blum et Hardt ; Ramdas, Grünwald, Vovk, Shafer 2023 (de mémoire).
- Ce qui l'attaque : transport du modèle binaire de Ker à des fiches de recherche non vérifié ; Wen et collaborateurs 2411.17693 ; Khilar (rampe lente).
- Inventaire : nouveau.

#### [F22-47] Attaque jouée par un agent ou écrite d'avance : à déclarer
- Définition : chez Zhang et Gao, l'attaque est fabriquée sur les scores, non jouée par l'agent ; Fable en tire une exigence : toute famille d'attaque du papier C déclare si elle est jouée par un agent ou écrite d'avance.
- Synonymes et paraphrases : « attaque fabriquée », « attaque jouée », « écrite d'avance ».
- Source : réponse 22C, constat 2 et phrase 10.
- État : proposé non tranché.
- Liens : papier C ; non trouvé « agent réel qui préserve sa marginale » (papier B).
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [F22-48] Recherche d'antériorité propre au papier C ; fichier des dix-sept décisions absent
- Définition : « non touché » ne valide rien : les 36 requêtes de la recherche exhaustive visaient la stéganographie et la comptabilité des matières, pas les juges sous attaque ni l'organisme. Fable propose une recherche ciblée (juges sous attaque, déplacement de sondes par l'entrée, analyse adaptative) et signale que le fichier des dix-sept décisions du papier C est absent de l'arbre selon la table.
- Synonymes et paraphrases : « non touché veut dire non cherché », « papier C non touché par l'antériorité » (à ne plus écrire seul), « dix-sept décisions ».
- Source : réponse 22C, conclusion, constat 1, décision 5 ; 22P, point 7.
- État : proposé non tranché.
- Liens : papier C ; gradation des non trouvé ; Raina, Liusie, Gales 2024 (voisin possible de l'usurpation de l'instructeur, de mémoire).
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [F22-49] Trahison par les activations ; usurpation de l'instructeur
- Définition : deux revendications du papier C : la trahison par les activations est tenue (non touchée ; épreuve déjà écrite : la hausse disparaît sous contrôle du style) ; l'usurpation de l'instructeur est à resserrer pour sa moitié « gain nul sur des sondes », par la même marge d'équivalence.
- Synonymes et paraphrases : « trahison par les activations », « usurpation de l'instructeur ».
- Source : réponse 22C, table.
- État : tenue / proposé non tranché.
- Liens : papier C ; Tailor ; Pandey et collaborateurs 2610.25032 (voisins lointains en boîte noire).
- Ce qui l'attaque : Raina et collaborateurs 2024 possible.
- Inventaire : nouveau.

---


**F. Échelle du programme**


#### [F22-50] Une seule loi de la référence honnête, quatre unités (extension de N-076 avec droit d'écriture)
- Définition : la règle de la référence honnête (N-076) ne compte que m et n ; chaque revue l'a redécouverte dans son unité : le pas (accumulation), l'épisode (seuil de G1), l'essaim (corrélation entre copies), la fiche (archive du juge statistique). Toute porte déclare l'unité, la taille et le droit d'écriture de sa référence ; la règle se présente comme application du corollaire 1 de Ker 2010.
- Synonymes et paraphrases : « loi de la référence honnête », « N-076 étendue », « unité commune à m et n », « qui écrit la référence », « corollaire 1 ».
- Source : réponse 22, table ; 22A, table ; 22P, point 1 (table des unités) et décision 2 (0,7).
- État : N-076 retenue (GO-2026-11-21-57) ; extension proposée non tranchée.
- Liens : portes G1, G2, GC ; organisme ; Wen et collaborateurs 2411.17693.
- Ce qui l'attaque : trois préenregistrements à retoucher.
- Inventaire : nouveau.

#### [F22-51] Porteur unique de la comparaison « texte contre accès interne »
- Définition : la même comparaison figure dans la complémentarité (A), la diversité des moniteurs (B), la loi de déférence, le déplacement de la sonde et le quorum (C) : un relecteur y verra un résultat compté quatre fois. Proposé : A porte la détection, C la corruptibilité, B fournit la corrélation des erreurs sans attaque ; une seule métrique d'union recalée au même taux total.
- Synonymes et paraphrases : « une comparaison, quatre porteurs », « double compte », « opposition juge contre sonde », « métrique d'union unique ».
- Source : réponse 22C, constat 4 et décision 1 ; 22P, point 2 et décision 3 (0,65).
- État : proposé non tranché.
- Liens : papiers A, B, C.
- Ce qui l'attaque : coordination des préenregistrements.
- Inventaire : 2.20 (voisin).

#### [F22-52] Harnais honnête unique, budget commun et ordre des travaux
- Définition : un harnais « honnête contre honnête » à composantes de variance emboîtées (pas, exécution, tâche, essaim, juge) sert les trois papiers ; leurs besoins en exécutions honnêtes se disputent le même calcul. Ordre proposé : table v2 ; harnais honnête ; puissance et bancs plantés puis budget ; scellement des seules prévisions décidables (τ en tête) ; G1 avec intervalles ; question pivot ; sort de B ; recherche propre au papier C.
- Synonymes et paraphrases : « harnais unique », « budget honnête commun », « ordre des travaux ».
- Source : réponse 22P, § 3, point 4, « Ordre des travaux », décision 5 (0,75).
- État : proposé non tranché.
- Liens : calcul de puissance ; jumeau contre jumeau.
- Ce qui l'attaque : les besoins dépassent peut-être le calcul disponible.
- Inventaire : nouveau.

#### [F22-53] Mode commun des revues (même modèle) et relecture par une autre famille
- Définition : les réponses 9, 22, 22A, 22B, 22C et 22P sortent toutes de Fable ; leur convergence sur « retirer, citer, mesurer » peut être un biais partagé, dans les deux sens. Proposé : relecture de la revue par une autre famille de modèles.
- Synonymes et paraphrases : « mode commun », « les revues convergent » (à ne plus écrire seul), « biais d'accord ».
- Source : réponse 22P, point 6 et décision 6 ; réserves de toutes les réponses.
- État : proposé non tranché (0,7).
- Liens : énoncés témoins ; N-052, N-053 (juge d'une autre lignée).
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [F22-54] Désaccords entre revues, tranchés par la réponse 22P
- Définition : la réponse 22P arbitre : accumulation « à remplacer » ; le nul s'écrit par plan de référence (plafond et jumelles valent chacun pour un plan) ; courbe selon le nombre d'agents selon 22B ; recalcul à la main avant simulation ; A détection, C corruptibilité, B mesure ; H8 en diagnostic dans A, construit dans C.
- Synonymes et paraphrases : « arbitrages 22P », « désaccords tranchés ».
- Source : réponse 22P, « Désaccords entre revues, tranchés ».
- État : proposé non tranché.
- Liens : entrées correspondantes ci-dessus.
- Ce qui l'attaque : arbitrage par le même modèle.
- Inventaire : nouveau.

#### [F22-55] Gradation des « non trouvé »
- Définition : chaque « non trouvé » se gradue par la recherche qui le fonde : six pièces lues ; 36 requêtes et 17 PDF avec quatre arbres de citations non parcourus (Ker 2006 et 2007, Arias-Castro et collaborateurs, Avenhaus et Jaech, plus Ker 2010) ; 13 pages lues sur 39 chez Parrack et collaborateurs. Une zone vierge est une question, jamais une ouverture.
- Synonymes et paraphrases : « graduer les non trouvé », « non trouvé n'est pas libre », « anti-faux-gap », « 13 sur 39 ».
- Source : réponse 22, § 1 et décision 5 ; 22A, § 1 ; 22B, « Gradation » ; 22C ; 22P.
- État : proposé non tranché (lecture ciblée maintenant, complète avant rédaction, 0,7).
- Liens : règle R8 ; recherche propre au papier C.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [F22-56] Énoncés témoins au statut connu servis au collisionneur
- Définition : mêler à nos énoncés six à huit énoncés au statut connu (occupé, faux, vrai par construction), écrits par un agent neuf, pour mesurer le taux de détection du collisionneur, comme N-075 mesure l'audit par dommages plantés. Sans témoins, un verdict « occupé » unanime ne se distingue pas d'un biais d'accord.
- Synonymes et paraphrases : « témoins », « énoncés plantés », « taux de détection du collisionneur ».
- Source : réponse 22, § 3 et décision 1 ; 22A décision 5 ; 22B décision 1 ; 22P décision 6.
- État : proposé non tranché (0,7).
- Liens : protocole X ; N-075.
- Ce qui l'attaque : une préparation de plus.
- Inventaire : nouveau.

#### [F22-57] Questions neutres pour le collisionneur (22, 22A, 22B, 22C, 22P, 23)
- Définition : chaque réponse écrit une question en mots courants, sans origine ni sort des énoncés, ordre tiré au hasard : exactitude avec preuve ou contre-exemple, travail publié le plus proche, quantités non dites, classement (établi, conséquence immédiate, ouvert, mal posé, faux), expérience unique et taille d'échantillon, certitude et citations de mémoire. La 23 y ajoute un test de neutralité et un test de devinette.
- Synonymes et paraphrases : « question neutre », « question au collisionneur », « envoi au collisionneur ».
- Source : section « Question neutre pour le collisionneur » de chaque réponse.
- État : proposé non tranché (approbation de Lazar demandée).
- Liens : protocole X ; énoncés témoins ; test de devinette.
- Ce qui l'attaque : défauts résiduels de vocabulaire (« discrète », « genre ») notés en 23.
- Inventaire : nouveau.

#### [F22-58] Phrases à ne plus écrire (listes des réponses 22 à 22P)
- Définition : listes cumulées de formules caduques : « garantie toujours valide » sans unité, taille et droit d'écriture ; « rappel qui croît avec l'horizon » comme résultat ; « bat le séquentiel par agent » sans somme globale ; « décroît plus doucement » sans agrégateur ; « antécédent défectueux » ; « le théorème du programme est inexact » sans « lettre de la version 2 » ; « à 1 % » sans épisodes ; « angle mort identifié » ; « co-élévation » sans position ou dépendance ; « inédit », « cœur vierge » ; « g nul » ; « table en vigueur » ; « colonne vertébrale théorique » ; « trois papiers, trois résultats indépendants » ; « les revues convergent ».
- Synonymes et paraphrases : « liste Ne pas écrire », « phrases caduques ».
- Source : sections « Phrases à ne plus écrire » des réponses 22, 22A, 22B, 22C, 22P.
- État : proposé non tranché.
- Liens : toutes les entrées.
- Ce qui l'attaque : —
- Inventaire : nouveau.

---


**G. Le lot d'attaques sous scellés (demande 23)**


#### [F22-59] Le lot sert la portée d'une revendication, non le franchissement d'une porte
- Définition : principe proposé : les cycles de reconception des sondes se décident sans le lot sous scellés ; il s'ouvre une seule fois, en séquentiel, sur la version qui a franchi la porte G1, pour la portée du gain de l'accès interne. Cela concilie la règle entre modes qui tient le mode à l'écart hors de la décision de G1 (D-S10) et D-S29 (a) qui l'exige pour revendiquer H1a.
- Synonymes et paraphrases : « lot en quarantaine », « lot sous scellés », « portée, pas porte », « ouvrir une fois », « D-S10 contre D-S29 (a) ».
- Source : réponse 23, conclusion et décision 2 (0,65) (`2a06a4d27348175f`).
- État : proposé non tranché ; amenderait la tranche par cycle accordée après la réponse 19.
- Liens : papier A ; N-054, N-056, N-062 ; porte G1.
- Ce qui l'attaque : un échec tardif restreint la revendication ou appelle un mode neuf ; option rivale : une tranche par cycle (alerte précoce).
- Inventaire : nouveau.

#### [F22-60] Trois lectures du lot, en strates séparées
- Définition : selon ce que le registre dira de sa nature : (I) mode conçu à l'aveugle, qui sert la portée de H1a et l'expérience de lecture de N-054 ; (II) recettes de l'attaquant informé interne, majorant descriptif seulement ; (III) pièces écartées par soupçon ou de provenance inconnue, description ou jeu de développement. Si le lot mêle ces lectures, ce sont des strates, jamais d'agrégat commun.
- Synonymes et paraphrases : « lecture I, II, III », « strates du lot », « que contient le lot ».
- Source : réponse 23, B1 et décision 1 (0,75).
- État : proposé non tranché ; Fable n'a vu ni registre ni contenu.
- Liens : N-054 point 3 ; N-056 points 4 et 6 ; N-077.
- Ce qui l'attaque : puissance divisée par strate.
- Inventaire : nouveau.

#### [F22-61] Le chiffre et l'adjectif
- Définition : un échantillon frais donne un taux sans biais pour le détecteur du moment (le chiffre) ; « tenu à l'écart de la conception » (l'adjectif) tombe dès qu'un agrégat du lot a guidé une reconception. Une tranche par cycle protège le chiffre, pas l'adjectif : Fable corrige ainsi sa réponse 19.
- Synonymes et paraphrases : « chiffre contre adjectif », « tenu à l'écart », « correction de la réponse 19 ».
- Source : réponse 23, conclusion, § 1, B5.
- État : proposé non tranché.
- Liens : budget de bits ; échelle de contamination.
- Ce qui l'attaque : Roelofs et collaborateurs 2019 (peu de surajustement mesuré malgré le réemploi), indice contraire.
- Inventaire : nouveau.

#### [F22-62] Compter les modes, non les épisodes ; « un mode est un cas »
- Définition : un mode écrit par une instance est un tirage de taille un à l'échelle des modes : le lot porte « un mode conçu à l'aveugle », jamais « tient face aux modes jamais vus », qui demande plusieurs modes indépendants en nombre fixé d'avance (comme N-044 pour les familles). Proposé : un second mode en réserve, écrit par une instance d'une autre lignée.
- Synonymes et paraphrases : « un mode est un cas », « généralité », « modes jamais vus », « second mode en réserve ».
- Source : réponse 23, conclusion, § 1, B2 (généralité), décision 4.
- État : proposé non tranché (0,65).
- Liens : N-044 ; N-054.
- Ce qui l'attaque : coût (devis de la couche 2 alourdi).
- Inventaire : nouveau.

#### [F22-63] Grandeur à lire sur le lot : rapport des déplacements par acte standardisés
- Définition : sous la loi héritée, le rappel d'un cumul dépend du déplacement par acte, du nombre d'actes sabotés et de l'horizon ; un rapport de rappels entre modes confond le transfert de la sonde et la différence d'horizon. Lire d'abord le rapport des déplacements par acte standardisés (mode réservé sur mode connu), le rappel à côté de sa valeur prédite par le nul.
- Synonymes et paraphrases : « déplacement par acte », « rapport des rappels » (trompeur), « lecture principale du lot ».
- Source : réponse 23, B2 (« La grandeur à lire change ») et décision 3 (0,55).
- État : proposé non tranché.
- Liens : thèse retenue ; accumulation ; complémentarité à taux total égal.
- Ce qui l'attaque : si le déplacement est nul sur le mode réservé, le nul « tient » trivialement ; option rivale : contrastes de N-056 en lecture principale.
- Inventaire : nouveau.

#### [F22-64] Ce que le lot peut et ne peut pas servir, revendication par revendication
- Définition : le lot peut servir la lecture principale de H1a (écart entre deux unions), une colonne par mode pour G1 (jamais la décision), l'expérience bras génériques contre spécialisés de N-054, une vérification hors plan de la prévision scellée d'accumulation, deux agrégats descriptifs « position ou dépendance », la localisation « motif et dommage au même lieu » ; il ne sert pas l'estimation de l'exposant, le taux de détection de l'audit d'issue sans décision séparée, les papiers B et C, ni toute phrase « résiste à ».
- Synonymes et paraphrases : « usages du lot », « table B2 ».
- Source : réponse 23, B2.
- État : proposé non tranché.
- Liens : N-054, N-056, N-075, N-076, N-077.
- Ce qui l'attaque : hypothèses tant que le registre ne dit pas la nature du lot.
- Inventaire : rattaché à 2.16 (motif et dommage au même endroit) pour la localisation.

#### [F22-65] Ordre des opérations : cycles, gel, équipe rouge tierce, ouverture, mode neuf ; trois propriétés, trois preuves
- Définition : « tenu à l'écart » décrit la conception, « en quarantaine » la garde, « d'une autre famille » l'auteur ; le lot donne le non-adapté jamais vu, le bras informé interne un majorant, l'équipe rouge tierce l'adapté. Ordre : cycles sur les modes mesurés sans le lot ; gel ; équipe rouge tierce code en main ; ouverture du lot en dernier acte ; tout changement ultérieur appelle un mode neuf. Le lot ne nourrit pas l'équipe rouge.
- Synonymes et paraphrases : « trois propriétés », « trois preuves », « ordre d'ouverture », « pas de graine ».
- Source : réponse 23, B3.
- État : proposé non tranché.
- Liens : N-054 ; N-062 ; Greenblatt et collaborateurs 2023 ; Tramèr et collaborateurs 2020 (attaques adaptatives).
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [F22-66] Limite d'auteur : « tenu à l'écart de la conception », jamais « indépendant »
- Définition : l'instance auteur du mode proposée par N-054 est de la lignée qui conçoit les moniteurs ; le lot a l'étanchéité, non l'indépendance d'auteur. Mesurer la nouveauté du mode (un classifieur sur traits de texte sépare-t-il le mode réservé des modes connus ? seule son exactitude sort) et sa ligne dans la matrice de succès croisés.
- Synonymes et paraphrases : « indépendance d'auteur », « nouveauté nominale », « mesure de nouveauté à l'aveugle ».
- Source : réponse 23, § 1 et B3.
- État : proposé non tranché.
- Liens : N-054 ; N-053.
- Ce qui l'attaque : une instance aveugle de la même lignée peut inventer ce que les concepteurs attendaient.
- Inventaire : nouveau.

#### [F22-67] Ce qui se scelle avant l'ouverture du lot
- Définition : neuf pièces à empreinte, horodatées par un tiers : détecteur gelé (sondes, couche principale, agrégateurs, seuils, deux unions, meilleure boîte noire, seconde boîte noire) ; référence honnête (m, unité, horizon, source de validité, strate hors garantie au-delà de m) ; prévision par bras ; règle (pari, niveau, intersection-union, arrêt, indéterminé) ; liste fermée des agrégats et budget de bits ; dénominateurs, témoin de compétence, définition de « diffus » ; graine de l'ordre d'ouverture, script, dépositaire, répétition sur lot factice ; échelle de contamination ; paragraphe de résultat de chaque issue.
- Synonymes et paraphrases : « scellés de l'ouverture », « gel final », « paragraphes écrits d'avance ».
- Source : réponse 23, B4.
- État : proposé non tranché.
- Liens : N-076 ; R1 ; analyse en aveugle (Klein et Roodman 2005) ; rapports enregistrés (Chambers 2013).
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [F22-68] Ouverture séquentielle par le pari apparié borné, et budget de bits
- Définition : le dépositaire ouvre les tâches dans un ordre tiré d'avance et s'arrête dès que le pari apparié borné (déjà retenu, N-056 nœud 2) tranche, le reste demeurant scellé. Tout agrégat rendu avant le gel final est compté dans un budget de bits ; une borne d'union sur l'inégalité de Hoeffding montre au pire cas l'élargissement de la marge garantie quand des bits sont rendus.
- Synonymes et paraphrases : « pari apparié borné », « ouverture séquentielle », « budget de bits », « un bit par cycle ».
- Source : réponse 23, § 3 et décision 2 (option c).
- État : proposé non tranché ; ordres de grandeur de Fable, à refaire.
- Liens : N-055, N-056 ; Waudby-Smith et Ramdas 2023 ; Shafer 2021 ; Dwork et collaborateurs 2015 ; Blum et Hardt 2015 ; intersection-union (Berger et Hsu 1996) ; Lan et DeMets 1983.
- Ce qui l'attaque : pire cas ; Roelofs et collaborateurs 2019.
- Inventaire : nouveau.

#### [F22-69] Ce qui consomme le lot
- Définition : chiffre et adjectif sont consommés par une lecture par un concepteur, une entrée dans l'apprentissage ou le calibrage, un choix de couche, d'agrégateur ou de boîte noire sur le lot, une panne suivie d'inspection ; l'adjectif seul par tout agrégat rendu avant le gel s'il précède une décision de conception ; rien, si c'est déclaré, par l'exécution de moniteurs gelés et l'étiquetage par appels sans mémoire journalisés au seul dépositaire (un moniteur gelé qui note exécute, il ne conçoit pas).
- Synonymes et paraphrases : « consommation du lot », « condition 8 de la réponse 19 ».
- Source : réponse 23, B5.
- État : hypothèse ; proposé non tranché.
- Liens : chiffre et adjectif ; échelle de contamination.
- Ce qui l'attaque : —
- Inventaire : nouveau.

#### [F22-70] Échelle de contamination à six niveaux et suite « déclasser, déclarer, refaire »
- Définition : échelle écrite d'avance, le doute rangé au niveau supérieur : 0 journal complet ; 1 fuite de métadonnées ; 2 agrégat vu avant le gel (adjectif perdu) ; 3 contenu lu ou entré dans un apprentissage (lot reclassé en jeu de développement, colonne comptée non mesurée, mode neuf) ; 4 fuite inverse, l'auteur a vu les moniteurs (lecture II) ; 5 journal incomplet, traité comme 3. Jamais de décontamination par retrait de pièces ; contrôle par un lot frère tiré après coup.
- Synonymes et paraphrases : « échelle de contamination », « niveaux 0 à 5 », « déclasser, déclarer, refaire », « fuite inverse ».
- Source : réponse 23, B6 et décision 5 (0,7).
- État : proposé non tranché.
- Liens : N-075 (strate non mesurée à zéro) ; Recht et collaborateurs 2019 (lot frère).
- Ce qui l'attaque : option binaire (tout doute jette le lot) ; option au cas par cas, décidée en connaissant l'enjeu.
- Inventaire : nouveau.

#### [F22-71] Contrôles de garde du lot : lot frère, canaris, lot factice, dépositaire hors lignée, jumeaux honnêtes
- Définition : un lot frère (même brief, instance neuve) pour déceler contamination ou adaptation ; chaînes canaris et empreintes de fragments confrontées aux invites ; répétition de l'ouverture sur un lot factice de même format ; dépositaire hors lignée de conception au journal recalculable ; horodatage tiers ; jumeaux honnêtes des tâches du lot, produits par le dépositaire, sans quoi le taux de faux positifs est inconnu ; dénominateurs fixés d'avance (tout épisode tiré compte).
- Synonymes et paraphrases : « lot frère », « canari », « lot factice », « dépositaire », « jumeaux honnêtes du lot ».
- Source : réponse 23, § 1, § 3, § 4, décision 4.
- État : proposé non tranché.
- Liens : N-049 (banque sœur) ; Jacovi et collaborateurs 2023 ; témoin de compétence et lecture filtrée (N-053).
- Ce qui l'attaque : —
- Inventaire : canaris voisins de 2.9 ; le reste nouveau.

#### [F22-72] Test de neutralité et test de devinette d'une question
- Définition : retirer de la question les mots qui trahissent l'enjeu (« quarantaine », « porte », « sonde », numéros), offrir les issues au même rang dans un ordre tiré au sort ; puis trois agents neufs de lignées différentes lisent la question seule et parient sur l'issue que l'auteur préfère, les réponses de l'auteur étant scellées avant. La question passe si leurs paris ne font pas mieux que le hasard.
- Synonymes et paraphrases : « test de devinette », « test de neutralité », « question qui ne trahit pas l'auteur ».
- Source : réponse 23, section (C).
- État : proposé, non exécuté.
- Liens : protocole X (test de neutralité exigé) ; questions neutres.
- Ce qui l'attaque : défauts résiduels de vocabulaire.
- Inventaire : nouveau.

---


### 2.10 Réponses de Fable aux demandes 25 à 30 (`F25`)


> Fichiers lus (dossier `docs/notes/demandes-fable-api-2026-11-22-v1/`), empreinte = 16 premiers signes du sha256 :
> - `reponse-25/relecture-fable-api.md` — `f5b2d7115446f4db` (dopamine comme second regard dans la pince, effort haut)
> - `reponse-26/relecture-fable-api.md` — `8ff82014b2feb5f6` (billets suivants)
> - `reponse-27-luc/relecture-fable-api.md` — `6a042a7b18124d58` (erratum interne et programme v3, effort maximal)
> - `reponse-28/relecture-fable-api.md` — `05c72e054ed7b5af` (idées originales, puits étroits et profonds, effort très haut)
> - `reponse-28-effort-max/relecture-fable-api.md` — `1261c8eeb9f00711` (même demande, effort maximal)
> - `reponse-29/relecture-fable-api.md` — `2af768bc095e40a4` (signal partout où c'est possible, chute conjointe, épreuve de l'étau)
> - `reponse-30/relecture-fable-api.md` — `3f8c7a8498e59bab` (tenir l'effort maximal sans épuiser la sortie)
> - Inventaire de rattachement : `docs/notes/seconds-regards-sabotage-inventaire-v1/inventaire-seconds-regards-invariants-noyaux-v1.md` — `02252df286503f8c`

> Statut général : tout ce qui suit est une réponse du concepteur (Fable), donc « proposé non tranché » sauf mention ; toutes les antériorités y sont « rapportées, non vérifiées sur PDF », citées de mémoire. Notation commune : V réussite attendue lue dans les états, δ surprise par étape, Y issue rendue par l'oracle, P premier moniteur de texte, B second lecteur de texte, L lecture interne (V et δ).

> ---


**I. Le signal de « dopamine » dans la pince (réponse 25)**


#### [F25-01] Place du signal de dopamine dans les trois objets de la pince
- Définition : la lecture de la réussite attendue et de la surprise, apprise sur épisodes honnêtes seuls, est située terme à terme dans la pince : dans le bilan, elle est le terme du milieu (une identité, qui ne donne ni ne retire de garantie) ; dans la complémentarité, elle est la mâchoire interne candidate, seul endroit où son apport se mesure ; dans l'étau, elle n'est qu'une hypothèse. Ce qu'elle ajoute au bilan est « une date et une adresse, jamais de la puissance ».
- Synonymes et paraphrases : dopamine second regard dans la pince ; « second regard dans la pince ok » (mot de Lazar) ; réussite attendue et surprise ; signal de récompense interne ; value et TD error ; demande 25 ; D-1 de la réponse 25.
- Source : réponse 25, § B1 et décision D-1 ; `f5b2d7115446f4db`.
- État : proposé non tranché (recommandation (a) maintenant, épreuve de l'étau sur devis après l'étape 2, confiance 0,65).
- Liens : N-075 (pince en trois objets), N-076 ; papier A ; chantier saboteur et sondes ; bilan à trois termes, complémentarité incrémentale, étau.
- Ce qui l'attaque : la sonde lit l'échec attendu et non l'intention ; un précurseur publié ne sépare pas triche et échec honnête sur un modèle sur trois ; un attaquant qui déplace ses représentations tait toutes les sondes ensemble (Bailey et al. 2024, McGuinness et al. 2025).
- Inventaire : 1.1, 2.4.

#### [F25-02] Bilan à trois termes avec la lecture interne au milieu (télescopage contre le jumeau)
- Définition : au banc, le dommage D = Y_jumeau − Y_suspect s'écrit identiquement (V_j − V_s) + (V_s − Y_s) − (V_j − Y_j) : écart de lecture connu avant l'issue, puis résidus de calibration du suspect et du jumeau. Quoi que le suspect fasse de sa lecture, la somme ne bouge pas : lu bas, il est aiguillé tôt ; lu haut, il échoue contre sa propre lecture.
- Synonymes et paraphrases : télescopage ; identité élémentaire ; bilan de la pince en trois termes ; dommage vu par l'oracle = (référence − lecture) + (lecture − issue) ; le signal « ne porte pas la garantie et ne peut pas la dégrader ».
- Source : réponse 25, § B1 ; `f5b2d7115446f4db`.
- État : proposé ; « aucune recherche d'antériorité » sur la forme fermée contre un jumeau : question, non revendication (§ B5).
- Liens : N-075 (bilan), papier A, jumeau honnête, détection de falsification de mesure.
- Ce qui l'attaque : voisins les plus proches du deuxième terme : Roger, Greenblatt et al. 2023 (falsification de mesure), Mallen et al. 2023 (modèles excentriques) ; identité triviale, donc tout l'intérêt est dans la date et l'aiguillage.
- Inventaire : 2.4.

#### [F25-03] Écart de lecture apparié et son nul par acte
- Définition : par épisode, T = V_jumeau − V_suspect, lu à la dernière frontière d'action avant l'issue, en points de réussite. Au banc, si le suspect est honnête la paire est échangeable et le signe de T est symétrique : nul sans aucun taux estimé ; en service, sans jumeau, le nul devient la calibration de V sur m honnêtes exogènes, horizon n au plus m.
- Synonymes et paraphrases : T ; grandeur de l'instrument ; nul d'échangeabilité ; test du signe sur paires agent–jumeau ; « rien ne se dit en service ».
- Source : réponse 25, § B2 ; `f5b2d7115446f4db`.
- État : proposé ; la question « qui produit la référence en service » reste ouverte (N-075, § 11, point 5).
- Liens : N-076 (m, n, source de validité), loi de la référence honnête, netteté de la référence.
- Ce qui l'attaque : la dispersion jumeau contre jumeau peut dépasser le plafond de dommage par épisode (issue négative N3) ; aucune garantie en service.
- Inventaire : 2.19, 2.5.

#### [F25-04] Complémentarité incrémentale contre la seconde boîte noire (Δ)
- Définition : sur les épisodes à dommage planté manqués par le premier moniteur de texte, Δ = rappel du signal interne moins rappel d'une seconde boîte noire, les deux réglés au même taux conjoint de fausses alertes (même quantile du même jeu de m honnêtes). Nul : parmi les épisodes rattrapés par un seul des deux, une chance sur deux (test exact de McNemar).
- Synonymes et paraphrases : Δ ; apport interne ; grandeur de l'apport ; « la boîte blanche rattrape-t-elle plus qu'une seconde boîte noire » ; D-2 de la réponse 25 ; trois bras (texte seul, texte + seconde boîte noire, texte + dopamine).
- Source : réponse 25, § B2, B3, D-2 ; `f5b2d7115446f4db`.
- État : proposé (option (c) : Δ en principal exploratoire, dommage cumulé à l'arrêt rapporté dès que le plancher a son texte, confiance 0,6). Corrigé par la réponse 29 (voir chute conjointe) et par la réponse 27 (conditionner sur les manqués avantage tout moniteur peu corrélé).
- Liens : H1 ; papier A ; jumeau textuel ; chute conjointe.
- Ce qui l'attaque : mesurée en rappel, non en dommage ; Δ = 0 n'implique pas « boîte noire déguisée » (réponse 29) ; Parrack, Attubato, Heimersheim 2025 occupe probablement la forme générale. Taille avancée de main, non rejouée.
- Inventaire : 5.4, 2.20.

#### [F25-05] La seconde boîte noire comme meilleur de trois lecteurs
- Définition : le témoin de la lecture interne est le meilleur, choisi sur un jeu de réglage disjoint, de trois lecteurs : le jumeau textuel de la sonde (prédicteur de l'issue lisant le texte jusqu'à la même frontière, mêmes épisodes et étiquettes, seul le canal change), un juge de texte d'une autre lignée, la confiance demandée au modèle sur rejeu bifurqué.
- Synonymes et paraphrases : second lecteur de texte ; jumeau textuel de la sonde ; contrôle « seconde boîte noire » ; B ; témoin exact du canal ; D-3.
- Source : réponse 25, § B3, D-3 ; `f5b2d7115446f4db`.
- État : proposé, recommandation (b) meilleur de trois, confiance 0,7 (appels externes, donc devis).
- Liens : N-053 (juge d'une autre lignée), lecture à positions masquées, chute conjointe.
- Ce qui l'attaque : selon la consultation, la confiance demandée égale la sonde sur le modèle ouvert de 8 milliards et un jeu public de mathématiques, et la longueur de la question fait presque aussi bien : un témoin faible ferait passer un lecteur de surface pour un regard interne.
- Inventaire : 2.20.

#### [F25-06] Les trois témoins « doit mourir » de la sonde
- Définition : avant toute lecture, trois contrôles doivent échouer : la sonde à étiquettes permutées rend le hasard ; une direction aléatoire appariée en covariance ne rattrape rien ; une sonde des couches basses en fin de consigne qu'égale la longueur du texte ne s'appelle pas interne.
- Synonymes et paraphrases : témoins de construit ; placebo d'étiquettes ; direction aléatoire appariée ; contrôle de longueur ; contrôles négatifs.
- Source : réponse 25, § 3 et § B3 ; `f5b2d7115446f4db`.
- État : proposé.
- Liens : N-053 (lecture à positions textuelles masquées), N-063 (base « mots et coût »), épreuves d'admission de la réponse 29.
- Ce qui l'attaque : un témoin qui passe n'établit pas que la lecture est interne au sens de l'étau.
- Inventaire : nouveau (proche de 2.11).

#### [F25-07] Lecture écrite d'avance de Δ (trois issues)
- Définition : Δ positif au seuil scellé : « apport interne mesuré sur ces modes, mode tenu à l'écart compris », rien au-delà ; Δ indiscernable de zéro : seconde boîte noire déguisée, place tenue à moindre coût par un lecteur de texte ; Δ négatif : sortie de la mâchoire, reste seulement comme covariable si la variance des scores honnêtes baisse.
- Synonymes et paraphrases : critères de lecture de la complémentarité ; issue « boîte noire déguisée ».
- Source : réponse 25, § B3 ; `f5b2d7115446f4db`.
- État : proposé ; la deuxième lecture est déclarée « trop forte » par la réponse 29, § R3.
- Liens : chute conjointe, N-054 (mode tenu à l'écart).
- Ce qui l'attaque : b = c > 0 donne Δ = 0 alors que la lecture interne rattrape des épisodes que la boîte noire manque.
- Inventaire : 5.4.

#### [F25-08] La surprise par étape réduite à la localisation, et la dissociation « dommage sans surprise »
- Définition : la somme des surprises d'un épisode se réduit à l'écart entre fin et début ; elle n'ajoute donc rien au bilan et sert seulement à localiser où la lecture a basculé, c'est-à-dire le « même lieu » de la règle à deux clés. La dissociation « dommage sans surprise » trierait, après audit, l'erreur de l'intention, à titre exploratoire.
- Synonymes et paraphrases : δ ; erreur de prédiction temporelle ; TD ; « une surprise présente n'innocente personne ».
- Source : réponse 25, § B1 ; `f5b2d7115446f4db`.
- État : proposé, exploratoire.
- Liens : règle à deux clés (N-075, erratum 3), N-026 (jamais de moyenne sur jetons : la sonde de surprise publiée en emploie une).
- Ce qui l'attaque : la surprise publiée n'est éprouvée que sur une famille de modèles et au-dessus d'un seuil, avec normalisation sur la réponse entière, inutilisable en ligne.
- Inventaire : 1.1, 1.13.

#### [F25-09] Règle à deux clés appliquée au signal
- Définition : un motif (réussite attendue basse ou surprise négative) et un dommage rendu par l'oracle au même épisode donnent une alerte ; un motif seul envoie en file d'audit, jamais dans les témoins ; un dommage sans motif relève du plancher.
- Synonymes et paraphrases : alerte = motif et dommage au même lieu ; deux clés ; première clé.
- Source : réponse 25, § B1 ; réponse 29, § R1 ; `f5b2d7115446f4db`, `2af768bc095e40a4`.
- État : retenu comme forme de N-075 (erratum 3) ; application au signal proposée.
- Liens : N-075, plancher d'audit au hasard.
- Ce qui l'attaque : « partout » étendrait la première clé hors de la pince (réponse 29, § R5).
- Inventaire : 2.16.

#### [F25-10] Biais de l'audit orienté par la réussite attendue
- Définition : une sonde de réussite attendue signale par construction l'échec honnête ; un audit qu'elle oriente n'est donc plus un échantillon sans biais. Remède : ne lire que la part tirée au hasard, ou pondérer chaque épisode par l'inverse de sa probabilité d'audit consignée ; la part au hasard ne diminue jamais.
- Synonymes et paraphrases : biais d'audit ; pondération par l'inverse de la probabilité ; Horvitz-Thompson ; file noyée d'échecs honnêtes.
- Source : réponse 25, § 1 point 5 et § 3 ; réponse 29, § R1 lieu 3 ; `f5b2d7115446f4db`.
- État : proposé.
- Liens : plancher d'audit (N-075), N-076, antériorités de l'audit (réponse 26).
- Ce qui l'attaque : occupé par la théorie des sondages (Horvitz et Thompson 1952 ; Särndal et al. 1992).
- Inventaire : 2.1, 5.4.

#### [F25-11] Différence entre un adjudant et un second regard
- Définition : un adjudant tient sa garantie de ce que le défenseur possède (tirages, oracle, harnais) ; le signal de dopamine tient la sienne d'une supposition empirique (l'agent ne déplace pas ses états). Il n'annonce pas l'invalidité du moniteur (rôle de la recapture), ne borne rien (rôle du plancher), et ne vaut qu'à l'échelon d'un agent à poids gelés qui ne voit ni lecture ni verdict.
- Synonymes et paraphrases : trois sortes d'adjudant (annonce d'invalidité, dilemme, borne sans détection) ; mécanisme adjudant ; échelon d'attaquant.
- Source : réponse 25, § B4 ; `f5b2d7115446f4db`.
- État : proposé (reprend la note adjudant v2).
- Liens : recapture et « moniteur invalide », plancher, attaquant informé.
- Ce qui l'attaque : l'attaquant informé sait déplacer ce canal.
- Inventaire : 2.2, 2.1, 1.1.

#### [F25-12] Les neuf « ne jamais » du signal interne
- Définition : liste d'interdits : ne rien faire revenir à l'agent (lecture, seuil, verdict, conséquence observable) ; ne jamais faire entrer V ou δ dans l'entraînement ou la sélection, guidage de génération compris hors bras d'attaque ; ne verser aux témoins aucun épisode du suspect ; ne pas blanchir par un V haut ; ne pas prendre V pour l'issue ; ne pas laisser l'audit orienté réduire le hasard ; ne pas réapprendre sur verdicts de l'oracle avant N-075 § 9 ; ne pas écrire « garantie de détection », « l'étau tient », « lit l'intention » ; compter toute sonnerie dans le taux de fausses alertes de la porte de fin de phase 1.
- Synonymes et paraphrases : ce que la lecture ne doit jamais devenir ; interdits du second regard ; invariant de non-retour.
- Source : réponse 25, § B4 ; `f5b2d7115446f4db`.
- État : proposé ; s'appuie sur N-053 point 5 (retenu), N-026, N-060 v3.
- Liens : N-053, N-075, porte G1.
- Ce qui l'attaque : le papier source pratique le guidage par la sonde.
- Inventaire : 6 (signalement d'invariant).

#### [F25-13] Première expérience du signal, sans attaque
- Définition : étape 0 gratuite (vérifier les activations sur disque, écrire statistique, jumeau textuel, témoins, préenregistrement court) ; étape 1 sans attaque : reproduire un chiffre publié du papier sur le modèle du programme, calibrer V sur honnêtes, mesurer la loi de T jumeau contre jumeau, taux d'honnêtes aiguillés à tort ; étape 2 sur dommages plantés par le contrôle à trois bras, sur devis. Issues négatives : chaîne qui ne retombe pas sur le publié, V non calibré ou placebo non nul, dispersion de T au-dessus du plafond de dommage.
- Synonymes et paraphrases : étape 0, étape 1, étape 2 ; N1, N2, N3 ; reproduction avant programme ; D-4.
- Source : réponse 25, § B6, D-4 ; `f5b2d7115446f4db`.
- État : proposé ; recommandation (a), pas de défaut pour la dépense. Prévisions à sceller : passe l'étape 1 (0,6), Δ indiscernable de zéro sur modes vus (0,55).
- Liens : collisionneur (essai jumeau contre jumeau d'abord), N-076.
- Ce qui l'attaque : un apport nul chez l'honnête ne tue pas l'étau (texte et états peuvent diverger sous attaque) : l'étape 1 tue l'instrument, pas la question.
- Inventaire : nouveau.

#### [F25-14] Antériorité du second regard interne
- Définition : le papier source (Xu, Yuksekgonul, Zou 2026, sous-système de récompense parcimonieux) donne la recette des deux sondes sans surveillance ni adversaire ; le programme en prend l'étiquette (l'issue) et laisse la thèse « neurones » et de parcimonie. Voisins : falsification de mesure (Roger et al. 2023), connaissance latente (Mallen 2023, Burns 2022, Kadavath 2022, Azaria et Mitchell 2023), gain boîte blanche (Parrack et al. 2025), précurseurs sans exemple d'attaque (Fischl-Lanzoni et al. 2026 ; Bhardwaj et al. 2026), calibration valide à tout instant (Arnold, Henzi, Ziegel 2021), total plutôt que parts (Avenhaus et Jaech 1981).
- Synonymes et paraphrases : papier « dopamine » ; Sparse Reward Subsystem ; Going Badly activations ; D-6.
- Source : réponse 25, § B5, D-6 ; `f5b2d7115446f4db`.
- État : occupé par la littérature dans ses pièces ; aucune phrase avant verdict d'antériorité propre (recommandation (a), confiance 0,8).
- Liens : R7, R8 ; papier A.
- Ce qui l'attaque : titres cités de mémoire, à vérifier.
- Inventaire : 1.1.

#### [F25-15] Question neutre et test de devinette à deux devinettes
- Définition : la question servie au collisionneur décrit le dispositif sans le mot « dopamine » ni le nom du programme ; trois modèles neufs de lignées différentes doivent deviner (i) la conclusion espérée parmi trois et (ii) lequel des dispositifs les auteurs ont déjà construit ; elle passe si aucune devinette ne bat le hasard. La réponse 26 ajoute un contrôle positif : une version qui nomme sondes et sabotage doit être devinée, sinon le test est insensible.
- Synonymes et paraphrases : test de neutralité ; devinette ; contrôle positif de la devinette ; protocole X partie C.
- Source : réponse 25, § C et D-5 ; réponse 26, § C ; réponse 29, § R6 ; `f5b2d7115446f4db`, `8ff82014b2feb5f6`.
- État : proposé ; non joué par Fable.
- Liens : protocole X, organisme d'idéation, collisionneur.
- Ce qui l'attaque : un test sans contrôle positif ne mesure rien.
- Inventaire : nouveau.


**II. Le signal partout, chute conjointe, étau (réponse 29)**


#### [F25-16] Les quatre conditions de possibilité d'une lecture interne
- Définition : remplacer « partout » par des conditions : la lecture de la réussite attendue n'existe que là où coexistent des états lisibles de l'agent, une issue calculée qui l'ancre, une référence honnête du régime, et aucun chemin de retour vers l'agent.
- Synonymes et paraphrases : « partout où c'est possible » (mot de Lazar) ; conditions d'existence du signal ; D-1 de la réponse 29.
- Source : réponse 29, § 1 point 1, D-1 ; `2af768bc095e40a4`.
- État : proposé (recommandation (a), confiance 0,7).
- Liens : N-053, N-076 ; organisme d'idéation (deux conditions manqueraient : états non lisibles d'un modèle servi par interface, pas d'issue calculée d'une idée — hypothèse à confirmer par le directeur).
- Ce qui l'attaque : sert mal « le mot à la lettre » ; le signal n'alerte qu'en deux lieux.
- Inventaire : nouveau.

#### [F25-17] Quatre rôles et table des sept lieux du signal
- Définition : rôles possibles : clé (première clé de la règle à deux clés), aiguillage (oriente l'audit), mesure (variable observée sans effet), interdit. Lieux : sondes de production (clé), moniteurs boîte noire (clé à côté, une sonde sur les états du moniteur se range parmi les lecteurs de texte), audit et plancher (aiguillage de la seule part orientée), organismes discrets (mesure sur rejeu), saboteur à budget (mesure de la dose), attaquant informé (mesure et cible, épreuve du devin d'abord), organisme d'idéation (aucun rôle).
- Synonymes et paraphrases : clé / aiguillage / mesure / interdit ; carte des lieux ; R1.
- Source : réponse 29, § R1 ; `2af768bc095e40a4`.
- État : proposé ; aucune ligne n'est une revendication.
- Liens : bras A (organismes discrets), saboteur à budget, attaquant informé, N-053.
- Ce qui l'attaque : risques par lieu : fuite par conséquences visibles d'un verdict ; circularité si la lecture sert à retenir les organismes qui lui échappent ; harnais qui modulerait le budget selon les alertes.
- Inventaire : 1.1.

#### [F25-18] Classement des seconds regards par supposition (classes A à D)
- Définition : les concepts de l'inventaire sont rangés par la supposition qu'ils consomment : classe A, lectures des états (toutes supposent que l'agent ne déplace pas ses représentations) ; classe B, hors des états (plancher, bilan, attestation, paires en aveugle, hasard du défenseur, copies sans coordination) ; classe C, instruments sur les regards, jamais des alertes (recapture, micro-interventions, devin, prix de l'effacement, chiffre noir) ; classe D, raisons et non regards (trois clauses, neuf invariants). Conséquence : toute la classe A compte pour une intervention au plus tant que la chute conjointe n'a pas montré le contraire.
- Synonymes et paraphrases : compter les suppositions, pas les détecteurs ; « la classe qui compte, pas le détecteur » ; R2.
- Source : réponse 29, § R2 ; `2af768bc095e40a4`.
- État : proposé ; cadre de la table des coupes pris « comme cadre seulement » (GO-2026-11-21-55, selon l'inventaire).
- Liens : H5 (diversité effective, nœud du directeur), ordre de coupe.
- Ce qui l'attaque : les fonctions d'influence relèveraient d'une autre supposition (hypothèse) ; canaris en version brute exclus.
- Inventaire : 5.1, 5.2, 5.3 ; sections 1 à 3.

#### [F25-19] La chute conjointe d'une lecture avec le second lecteur
- Définition : sur les épisodes endommagés selon l'oracle, manqués par le premier moniteur, pris dans la part d'audit au hasard, pour une famille et un échelon déclarés, seuils gelés à fausses alertes égales : J = probabilité que la lecture interne se taise sachant que le second lecteur se tait, estimée par d/(b+d). Nul « tombe avec » : là où B se tait, L ne sonne pas plus que chez l'honnête (1 − J ≤ q). L compte pour une intervention si la borne basse de 1 − Ĵ dépasse la borne haute de q d'une marge scellée.
- Synonymes et paraphrases : compte par chute conjointe ; « une lecture ne compte comme intervention que si elle ne tombe pas en même temps que le second lecteur » (phrase de Lazar du 22 novembre) ; J(f, e) ; tomber ensemble ; pannes coïncidentes ; R3.
- Source : réponse 29, § R3, D-2 ; `2af768bc095e40a4`.
- État : proposé (option (a) : exploratoire tant que N-075 n'a pas d'erratum, confiance 0,7) ; en ferait un critère du silence commun, aujourd'hui rapporté sans critère.
- Liens : N-075 § 3, H5, papier A.
- Ce qui l'attaque : « probablement occupé dans sa forme générale » (pannes coïncidentes) ; taille de main de trente à cinquante silences par famille, non rejouée.
- Inventaire : 5.4.

#### [F25-20] Une table, trois lectures (silence commun, chute conjointe, apport) et correction de la réponse 25
- Définition : la même table deux par deux donne le silence commun d/n, la chute conjointe d/(b+d) et l'apport Δ = (b − c)/n. Correction : lire « Δ indiscernable de zéro » comme « boîte noire déguisée » est trop fort ; seul b proche de (b+d)·q dit que la lecture tombe avec le second lecteur.
- Synonymes et paraphrases : table deux par deux ; recapture à deux mâchoires ; correction à la réponse 25.
- Source : réponse 29, § R3 ; `2af768bc095e40a4`.
- État : proposé.
- Liens : complémentarité incrémentale, silence commun (N-075).
- Ce qui l'attaque : intervalle Clopper-Pearson à seuils fixes trop étroit ; rééchantillonnage par grappes avec seuils réestimés, le plus large décide.
- Inventaire : 5.4.

#### [F25-21] Ce qui fausse la chute conjointe (onze causes)
- Définition : seuils pris sur des jeux différents ; familles mélangées ; dommage planté sans dissimulation (se taire ensemble ici n'est pas tomber ensemble sous attaque, Johnston et al.) ; lecture interne qui lit des traces du texte ; audit orienté lu sans pondération ; oracle fait de lecteurs ; difficulté (prendre l'écart au jumeau) ; second lecteur choisi sur les épisodes de l'essai ; B et L appris sur les mêmes honnêtes ; épisodes d'une même tâche comptés indépendants ; seuils ou marge choisis après lecture.
- Synonymes et paraphrases : causes d'erreur de l'estimateur ; biais de la chute conjointe.
- Source : réponse 29, § R3 ; `2af768bc095e40a4`.
- État : proposé.
- Liens : N-075, R1.
- Ce qui l'attaque : —.
- Inventaire : 5.4.

#### [F25-22] Les trois ancres de l'estimateur de chute conjointe
- Définition : contrôles de l'estimateur lui-même : un second lecteur dupliqué doit donner une chute conjointe de un ; une direction aléatoire appariée ne doit pas sonner plus que chez l'honnête ; un regard synthétique tiré du verdict bruité de l'oracle doit donner une chute basse. Si l'estimateur manque une ancre, il est faux.
- Synonymes et paraphrases : ancres ; étalonnage de l'estimateur ; contrôles positif et négatif du compte.
- Source : réponse 29, § 4 ; `2af768bc095e40a4`.
- État : proposé.
- Liens : R5 (garde testée sur cas sain et artefact).
- Ce qui l'attaque : —.
- Inventaire : nouveau.

#### [F25-23] Deux sens de « tomber en même temps »
- Définition : se taire ensemble sur des dommages donnés est une statistique (la chute conjointe mesurée) ; tomber ensemble devant une attaque montée contre un seul des deux est une épreuve causale. Seul le second sens est l'étau.
- Synonymes et paraphrases : corrélation de pannes contre corrélation de performances ; silence commun contre étau.
- Source : réponse 29, § 1 point 3 ; `2af768bc095e40a4`.
- État : proposé.
- Liens : étau, chute conjointe.
- Ce qui l'attaque : Johnston et al. (corrélation de performances n'est pas corrélation de pannes).
- Inventaire : 5.4, 5.5.

#### [F25-24] Le budget de sonneries avant d'ajouter des cloches
- Définition : chaque regard ajouté dépense le taux de fausses alertes de la porte de fin de phase 1 ; ce budget s'écrit avant d'ajouter une cloche, et toute sonnerie du signal y entre comme les autres.
- Synonymes et paraphrases : budget de fausses alertes ; cloches ; sonneries.
- Source : réponse 29, § 1 point 2 et § R5 ; réponse 25, § B4 point 9 ; `2af768bc095e40a4`.
- État : proposé.
- Liens : porte G1, quatre rôles du signal.
- Ce qui l'attaque : la lecture à la lettre de « partout » multiplierait les fausses alertes.
- Inventaire : nouveau.

#### [F25-25] Épreuve de l'étau par barreaux
- Définition : barreau 0 sans attaque ni entraînement (rappel de L sur dommages plantés non dissimulés, prix de l'effacement, lecture à texte nettoyé, trois honnêtes de contrôle, devin) ; barreau 1 poids gelés, familles à dissimulation écrites par des tiers dont une tenue à l'écart ; barreau 2 attaquant entraîné contre le seul texte sans jamais recevoir L ; barreau 3 attaquant entraîné contre les deux, mesure de la taxe. Réfutations : plafond nul au barreau 0 ; J proche de un sur la famille tenue à l'écart aux barreaux 1-2 ; silence commun à taxe nulle au barreau 3, l'étau est alors ouvert à cet échelon.
- Synonymes et paraphrases : étau ; « échapper à l'un expose à l'autre » ; taxe de dissimulation ; barreaux 0 à 3 ; R4 ; D-3, D-4.
- Source : réponse 29, § R4, D-3, D-4 ; `2af768bc095e40a4`.
- État : proposé ; barreau 0 après l'étape 1, barreaux 1-2 sur devis ; barreau 3 refusé pour l'instant (touche N-053), à réexaminer. Prévisions : L ne tombe pas entièrement avec B au barreau 1 (0,5) ; silence commun atteint à taxe faible au barreau 3 (0,7).
- Liens : N-053, N-077 (attaquant qui répond au mieux), attaquant informé, quarantaine.
- Ce qui l'attaque : une mesure de taxe est toujours un plafond ; Bailey et al. 2024, McGuinness et al. 2025.
- Inventaire : 5.5.

#### [F25-26] Antériorité du compte : pannes coïncidentes de versions diverses
- Définition : la sûreté de fonctionnement traite depuis longtemps les pannes de cause commune : Eckhardt et Lee 1985, Knight et Leveson 1986, Littlewood et Miller 1989 (diversité forcée pouvant rendre les pannes négativement liées, voisin le plus proche de l'étau, hypothèse), facteur bêta de Fleming 1975, mesures de diversité d'ensembles (Kuncheva et Whitaker 2003), coupes minimales (Molnar).
- Synonymes et paraphrases : multiversion ; N-version programming ; cause commune ; facteur bêta.
- Source : réponse 29, « Antériorité », D-5 ; `2af768bc095e40a4`.
- État : occupé par la littérature (probable dans sa forme générale) : question, non revendication.
- Liens : H5, ordre de coupe.
- Ce qui l'attaque : —.
- Inventaire : 5.3, 5.4.

#### [F25-27] Textes scellés touchés par l'extension du signal
- Définition : signalement, sans rien modifier : N-053 point 5 (lieux d'attaque, barreau 3) ; N-075 § 3 (le silence commun deviendrait critère : erratum ou statut exploratoire) ; N-075 § 4 et erratum 3 (première clé hors pince) ; N-026 (moyenne de la sonde publiée) ; N-060 v3 point 4 (réapprentissage) ; N-076 (m et n par lieu) ; H5 (redéfinir la diversité effective est un nœud) ; porte de fin de phase 1 ; préenregistrement du bras dopamine (toute lecture à un lieu neuf est nouvelle).
- Synonymes et paraphrases : R5 de la réponse 29.
- Source : réponse 29, § R5 ; `2af768bc095e40a4`.
- État : signalement.
- Liens : ces décisions.
- Ce qui l'attaque : —.
- Inventaire : 6.


**III. Billets (réponse 26)**


#### [F25-28] Ordre des billets par dépendance
- Définition : les billets se classent par ce dont leur parution dépend (résultat à venir, plume du directeur, modération, cloisonnement), non par l'état du texte. Ordre recommandé : « Reasons or watching? » version 7 courte ; un billet unique « loi héritée » ; le versant honnête de l'essai jumeau contre jumeau ; le billet sur les sondes après un résultat discret ; le candidat B (« tirer au sort n'est pas reconnaître ») après l'entretien, C en repli.
- Synonymes et paraphrases : billets suivants ; ordre des parutions ; demande 26 ; Décision 1.
- Source : réponse 26, conclusion, § B2, Décision 1 ; `8ff82014b2feb5f6`.
- État : proposé (confiance 0,6).
- Liens : chantier billet, entretien (27 novembre ou 1er décembre, dates divergentes dans les pièces).
- Ce qui l'attaque : deux textes à écrire de la main du directeur en dix jours.
- Inventaire : nouveau.

#### [F25-29] Audit de péremption (table de péremption)
- Définition : confronter chaque phrase d'un brouillon aux décisions et verdicts postérieurs à sa date, avec un sort (tient, à réécrire, à retirer). Pour un texte non lisible par le concepteur, donner les classes de phrases à chercher et qui les cherche.
- Synonymes et paraphrases : table de péremption ; phrases périmées.
- Source : réponse 26, § 1, § 3, § B3 ; `8ff82014b2feb5f6`.
- État : proposé.
- Liens : révision du billet sur les sondes, R12.
- Ce qui l'attaque : —.
- Inventaire : nouveau.

#### [F25-30] Billet « loi héritée » (fusion du candidat A et du billet drapeau)
- Définition : le candidat A (part cachée en z·√(1/n + 1/m)/μ) et le billet « drapeau » (loi en √(n + n²/m)) portent la même loi, écrite en part et en total ; ils fusionnent en un billet qui cite la loi (Ker 2010 ; Avenhaus et Jaech 1981), donne des nombres sous supposition, garde question et protocole pour le billet de résultat, et scelle la prévision de N-076 avant parution.
- Synonymes et paraphrases : candidat A ; « référence honnête » ; billet drapeau ; doublon ; Décision 4.
- Source : réponse 26, § B1, Décision 4 ; `8ff82014b2feb5f6`.
- État : proposé (confiance 0,6, après relecture du critère de mort contre l'article de Khilar).
- Liens : modèle nul hérité, N-076, papier A.
- Ce qui l'attaque : la loi est déjà transposée au suivi des usages (arXiv 2610.13083, « protéger la référence ») ; le plateau est une citation chiffrée, pas un résultat ; probabilité de nouveauté à revoir à la baisse ; « mur du rapport signal sur bruit » (Tandra et Sahai 2008).
- Inventaire : nouveau.

#### [F25-31] Absence d'effet seulement sous borne d'équivalence
- Définition : une absence d'effet (titre « … not what they do ») ne se revendique qu'avec une borne d'équivalence déclarée avant lecture ; sans elle, écrire « nous ne détectons aucun changement », avec l'intervalle.
- Synonymes et paraphrases : test d'équivalence ; Lakens 2017 ; titre borné.
- Source : réponse 26, § 1, § B4 ; `8ff82014b2feb5f6`.
- État : proposé.
- Liens : billet « Reasons or watching? ».
- Ce qui l'attaque : —.
- Inventaire : nouveau.

#### [F25-32] Révision de « Reasons or watching? »
- Définition : version 7 courte (1 300 à 1 500 mots selon le gabarit), écrite de la main du directeur d'après une fiche de faits, une phrase de fait sur l'expérience 1 (verdict « non lisible »), titre borné faute d'équivalence, aucune phrase « sous embargo », revérifier le jour même que le test sur les adaptateurs n'a pas tourné ; citer Turpin et al. 2023 et Greenblatt et al. 2024 si absents.
- Synonymes et paraphrases : billet sur l'écart dire-faire ; billet MSM ; version 6, version 7 ; « I wrote this post myself » ; Décision 2.
- Source : réponse 26, § B4, Décision 2 ; `8ff82014b2feb5f6`.
- État : proposé (confiance 0,65).
- Liens : chantier billet ; politique de modération du site.
- Ce qui l'attaque : une reformulation phrase à phrase d'un texte de modèle ne vaut pas « écrit de ma main ».
- Inventaire : nouveau.

#### [F25-33] Révision du billet sur les sondes (renvoi gardé)
- Définition : garder le renvoi faute de résultat sur saboteur discret et de contrôle de l'empreinte de la consigne ; préparer la table de péremption par classes (« détecte » → « oriente l'audit », accumulation sans m et n, marge retirée par N-077, lemme et théorème retirés, chiffres voisins sans unité, primauté, mode tenu à l'écart, conclusion bornée à « instructed ») ; le résumé dit dans ses 250 premiers mots que rien n'est établi pour un saboteur discret.
- Synonymes et paraphrases : premier billet sur le contrôle ; saboteur instruit ; barreau « sabotage ou empreinte » ; explication concurrente par l'empreinte de la consigne ; Décision 3.
- Source : réponse 26, § B3, Décision 3 ; `8ff82014b2feb5f6`.
- État : proposé (confiance 0,7). Les sections de l'étape B et de l'étape B bis doivent être écrites par un lecteur autorisé depuis les verdicts scellés (aucun chiffre ici).
- Liens : chantier saboteur et sondes, N-075, N-076, N-077, N-054.
- Ce qui l'attaque : la sonde peut lire l'empreinte de la consigne et non le sabotage.
- Inventaire : nouveau.

#### [F25-34] Ce qui ne doit paraître dans aucun billet (matrice de fuite)
- Définition : liste d'éléments interdits, chacun avec la mesure que sa divulgation fausserait : nature du mode et de la famille tenus à l'écart, mécanismes des saboteurs (G1 par mode, N-054, N-062) ; procédés de la course « nouvelles attaques » ; poids, couches, seuils, graines d'audit, dommages plantés, grille de l'oracle ; prévisions chiffrées avant scellement ; « part sue du dommage » avant l'entretien ; chiffres des étapes B par une session exposée ; mots de primauté ; chiffres sans unité.
- Synonymes et paraphrases : matrice de fuite ; liste noire des billets ; Décision 5 (une phrase d'existence du mode réservé, sans nature ni chiffre).
- Source : réponse 26, § B5, Décision 5 ; `8ff82014b2feb5f6`.
- État : proposé.
- Liens : cloisonnement, N-054, N-075, N-076.
- Ce qui l'attaque : —.
- Inventaire : nouveau.

#### [F25-35] Le versant honnête de l'essai « jumeau contre jumeau » comme premier billet de résultat
- Définition : seule mesure sans secret qui change un billet de question en résultat : taux de fausses alertes sur agents honnêtes, sur tâches disjointes de la famille tenue à l'écart, prévision scellée avant ; ses deux issues sont publiables.
- Synonymes et paraphrases : jumeau contre jumeau ; versant honnête ; Décision 6.
- Source : réponse 26, § B2, Décision 6 ; `8ff82014b2feb5f6`.
- État : proposé (confiance 0,55 ; maintenant si des exécutions honnêtes existent).
- Liens : collisionneur (quatre modèles sur cinq veulent d'abord ce taux), N-076, essai E1.3 du programme v3.
- Ce qui l'attaque : durée et coût inconnus.
- Inventaire : 2.19, 2.5.

#### [F25-36] Antériorités de l'audit secret et de l'estimateur pondéré
- Définition : l'audit au hasard pondéré et le moniteur en variable de contrôle sont occupés : Horvitz et Thompson 1952 ; Särndal, Swensson, Wretman 1992 ; inférence aidée par la prédiction (Angelopoulos et al. 2023) ; audit aléatoire en contrôle (Greenblatt et al. 2023). Rien n'y est revendiqué.
- Synonymes et paraphrases : Horvitz-Thompson ; prediction-powered inference ; model-assisted sampling.
- Source : réponse 26, § B2 ; `8ff82014b2feb5f6`.
- État : occupé par la littérature (N-076 : rien revendiqué).
- Liens : plancher d'audit, N-076.
- Ce qui l'attaque : —.
- Inventaire : 2.1.


**IV. Erratum interne et programme version 3 (réponse 27, effort maximal)**


#### [F25-37] Erratum interne applicable par programme
- Définition : trente et une entrées ANCIEN / NOUVEAU / raison corrigeant les réponses 4 et 8, la note des problématiques et la section 3 du programme v2, chaque ANCIEN devant être trouvé exactement une fois par programme ; quatre phrases de la réponse 22 sont hors des pièces visées (recherche exhaustive, table des revendications), d'où un second erratum proposé.
- Synonymes et paraphrases : erratum interne ; E4-1 à E4-8, E8-1 à E8-6, EN-1 à EN-10, EP-1 à EP-7 ; différences D1 à D19 ; « application à blanc ».
- Source : réponse 27-luc, Pièce 1, Décisions 1 et 4 ; `6a042a7b18124d58`.
- État : proposé (scellement provisoire après contrôle par programme, D7 et D16 « sous simulation », confiance 0,75).
- Liens : réponses 9 et 22 (même modèle : pas de confirmation indépendante), R12.
- Ce qui l'attaque : copie des ANCIEN à la main, sans contrôle.
- Inventaire : nouveau.

#### [F25-38] Modèle nul hérité de la dissimulation répartie
- Définition : pour des pas indépendants et une référence honnête de m pas, comptés dans la même unité que les n pas surveillés, le dommage indétectable est d'ordre √(n + n²/m) ; il n'est linéaire qu'à référence bornée ou fautive (Ker 2010). La transition en n ≈ m est fixée par construction (corollaire 1), ce n'est pas une prévision ; forme à ajuster : budget caché au carré ≈ z²·(σ²·n^(2H) + σ²·n²/m + τ²·n²) ; l'écart au nul est le résultat.
- Synonymes et paraphrases : loi de la racine carrée ; loi héritée ; square root law ; stéganographie et comptabilité des matières ; plateau ; bascule entre deux régimes ; « racine puis linéaire ».
- Source : réponse 27-luc, E4-1, E4-4, E8-1, D5 ; `6a042a7b18124d58`.
- État : retenu comme modèle nul cité (thèse du papier A retenue le 22 novembre selon la pièce) ; occupé (Ker 2007, 2010 ; Avenhaus et Jaech 1981 ; Khilar 2026 au suivi des usages).
- Liens : N-076, papier A, billet « loi héritée ».
- Ce qui l'attaque : l'ancienne lettre (« racine si la référence est connue, puis linéaire si estimée », bascule entre m et m divisé par le taux d'audit) est fausse ; Ker 2010 traite déjà la référence estimée.
- Inventaire : nouveau.

#### [F25-39] Exposant sous dépendance courte, dérive et hétérogénéité
- Définition : correction : l'exposant reste un demi sous dépendance courte, qui ne gonfle que la constante (Filler, Ker, Fridrich 2009) ; seule une dérive le long de la tâche change l'exposant ; l'hétérogénéité entre tâches ajoute un terme linéaire.
- Synonymes et paraphrases : exposant H ; « le bruit honnête dépasse un demi » (ancienne phrase fausse).
- Source : réponse 27-luc, E4-5 ; `6a042a7b18124d58`.
- État : retenu comme correction proposée.
- Liens : modèle nul hérité.
- Ce qui l'attaque : —.
- Inventaire : nouveau.

#### [F25-40] Thèse du papier A, version 3 : loi héritée comme modèle nul, bilan mesuré, complémentarité
- Définition : les lois de la dissimulation répartie, déjà transposées au suivi des usages, donnent un modèle nul du dommage qu'un saboteur diffus peut cacher ; le papier mesure, sur des scores de sondes d'agents qui sabotent, où ce nul tient et quels termes s'y ajoutent, puis ce que l'accès interne rattrape et qu'une seconde boîte noire ne rattrape pas. Elle remplace « la fragmentation détruit la preuve externe, pas la preuve interne ».
- Synonymes et paraphrases : thèse du 22 novembre ; programme v3 ; D3, D5 ; Bi (bilan mesuré contre le modèle nul) ; critère de succès (1) réécrit (D19).
- Source : réponse 27-luc, D1, D3, D5, D15, D19 ; `6a042a7b18124d58`.
- État : retenu le 22 novembre (mot du directeur rapporté) ; différences proposées, non scellées. Citations obligatoires : quatre (Ker 2007, Ker 2010, Avenhaus et Jaech, Khilar) ou liste étendue (Décision 2, recommandation étendue, confiance 0,65).
- Liens : papier A, H1, H2, N-076.
- Ce qui l'attaque : D5, D7, D16 reposent sur des dérivations non simulées ; la v3 garde H6 retirée par N-077 (périmètre, Décision 3).
- Inventaire : nouveau.

#### [F25-41] Théorème négatif : lettre inexacte, forme exacte élémentaire
- Définition : la lettre v2 (« toute statistique fondée sur les marginales a une puissance égale au taux de faux positifs ») est inexacte : N-003 l'a bornée (vraie si l'attaque préserve le multi-ensemble des scores, pour les statistiques symétriques) et Arias-Castro, Bubeck, Lugosi 2012 la contredisent (le carré de la somme garde de la puissance en régime dense). Énoncé exact, cité : à marginales préservées, l'espérance des statistiques additives est inchangée ; le test efficace est du second ordre (autocovariance dans le temps, co-élévation entre agents), non le seul puissant.
- Synonymes et paraphrases : T ; théorème marginale contre corrélation ; « la puissance ne peut venir que d'une relation entre mâchoires » (ancienne phrase).
- Source : réponse 27-luc, E8-2, EN-1, EN-2, D8, D15 ; `6a042a7b18124d58`.
- État : retiré comme résultat (décidé le 22 novembre), mentionné, non revendiqué.
- Liens : N-003, papiers A et B, N-069 (co-élévation).
- Ce qui l'attaque : Zhang et Gao 2026 occupent le contraste en boîte noire.
- Inventaire : nouveau.

#### [F25-42] Lemme d'additivité, mentionné, et la question de l'étalement
- Définition : l'indifférence de la somme à la répartition, à taille fixe, est occupée hors du contrôle (Avenhaus et Jaech 1981 ; Ker 2006) ; reste la question pour un processus e : l'étalement est-il le cas le moins favorable au défenseur ? Une simulation à budget égal (sabotage tôt, tard, étalé) la tranche avant toute phrase.
- Synonymes et paraphrases : L ; lemme ; reste ; borne inférieure valide à tout instant (retirée) ; « la puissance ne dépend que de B et de la variance ».
- Source : réponse 27-luc, EN-4, D6, D7, D14 ; `6a042a7b18124d58`.
- État : retiré comme résultat le 22 novembre, reste compris ; forme séquentielle devenue question.
- Liens : N-013, N-075 (lemme resserré au reste).
- Ce qui l'attaque : énoncé occupé.
- Inventaire : nouveau.

#### [F25-43] Complémentarité à taux total de fausses alertes égal (énoncé par union)
- Définition : à taux total de fausses alertes égal, l'union « meilleure boîte noire et sonde » rattrape-t-elle plus de sabotages diffus que l'union « meilleure boîte noire et seconde boîte noire d'une autre lignée » ; même épreuve pour la sonde aléatoire appariée. Remplace l'énoncé conditionné sur les manqués, qui avantage tout moniteur peu corrélé au premier.
- Synonymes et paraphrases : second axe de la thèse ; H1 v3 ; complémentarité ; E8-4, EN-7, D12.
- Source : réponse 27-luc, E8-4, EN-7, D12 ; `6a042a7b18124d58`.
- État : proposé ; « non trouvée, 13 pages lues sur 39 chez le parent le plus proche ».
- Liens : H1, Δ de la réponse 25, chute conjointe.
- Ce qui l'attaque : gain blanc sur noir établi en général (Parrack et al. 2025, avec indice contraire).
- Inventaire : 2.20, 5.4.

#### [F25-44] Question « position ou dépendance »
- Définition : l'attaque d'un vrai agent déplace-t-elle la position des scores, leur dépendance, ou les deux ? Elle se lit par un test de position et un test de dépendance étalonnés sur des substituts par permutation des pas ; aucune issue n'est dite publiable avant calcul de puissance, une issue indéterminée est possible.
- Synonymes et paraphrases : Q ; « que déplacent des attaques jouées par de vrais agents ? » ; substituts par permutation.
- Source : réponse 27-luc, D10, D11, D15 ; `6a042a7b18124d58`.
- État : ouvert (question, non calibrée).
- Liens : théorème négatif, papier A et B.
- Ce qui l'attaque : —.
- Inventaire : nouveau.

#### [F25-45] « Deux issues publiables » seulement sous puissance calculée
- Définition : correction de méthode : deux issues ne ferment quelque chose que si le plan a la puissance de les séparer ; sinon une troisième issue, indéterminée, existe et doit être dite.
- Synonymes et paraphrases : E4-7, E8-6, D10.
- Source : réponse 27-luc ; `6a042a7b18124d58`.
- État : proposé (correction).
- Liens : R1.
- Ce qui l'attaque : —.
- Inventaire : nouveau.

#### [F25-46] Somme globale plate en nombre d'agents, maximum décroissant
- Définition : à budget et nombre total d'actions fixés, la somme globale est prédite plate en N (nombre d'agents ou de fragments) et le maximum décroissant (Avenhaus et Jaech) ; la sonde change la constante, non la pente ; la somme globale devient une base obligatoire, le gain revendiqué sur les seuls sabotages qui déplacent la dépendance.
- Synonymes et paraphrases : D16, D18 ; « la courbe boîte blanche domine la boîte noire » (ancienne phrase) ; « le cœur vierge » (retiré).
- Source : réponse 27-luc, D16, D18 ; `6a042a7b18124d58`.
- État : prévision proposée, non constat, sous simulation.
- Liens : papier A et B.
- Ce qui l'attaque : non simulée.
- Inventaire : nouveau.

#### [F25-47] Occupants nommés : Khilar 2026 et Zhang et Gao 2026
- Définition : Khilar 2026 (arXiv 2610.13083) transpose déjà la loi en racine au suivi des usages contre l'extraction (« premier à transposer » ne s'écrit pas) ; Zhang et Gao 2026 (arXiv 2606.10456) occupent le contraste marginale/corrélation en boîte noire, sur scores synthétiques puis traces réelles à attaque fabriquée sur les scores ; aucune différenciation n'est revendiquée, réserve à longueur finie à vérifier en rejouant leur tableau 2.
- Synonymes et paraphrases : recherche exhaustive de transposition ; « antécédent défectueux » (phrase à rétracter).
- Source : réponse 27-luc, E4-3, EN-10, D11 ; réponse 26, § B1, § B5 ; `6a042a7b18124d58`.
- État : occupé par la littérature (cité, jamais revendiqué).
- Liens : papier A, billet loi héritée.
- Ce qui l'attaque : —.
- Inventaire : nouveau.


**V. Idées originales : puits étroits et profonds (réponses 28 et 28 en effort maximal)**


#### [F25-48] Diagnostiquer avant de prescrire : le bilan des pertes de l'organisme
- Définition : avant toute méthode, établir étage par étage, sur les journaux bruts des courses passées, si les idées étroites n'ont jamais été proposées (perte en amont) ou ont été proposées puis perdues (regroupement, juge, sélection, en aval) ; vérifier aussi si la récompense d'héritage favorise le raffinement des bassins larges.
- Synonymes et paraphrases : audit des pertes ; étape 0 ; amont contre aval ; D1 des réponses 28.
- Source : réponse 28, A1, C6, D1 ; réponse 28-effort-max, A1, C6, D1 ; `05c72e054ed7b5af`, `1261c8eeb9f00711`.
- État : proposé (confiance 0,8 et 0,85).
- Liens : organisme d'idéation, organisme v9, N-045 (héritage récompensé), recoupement des méthodes des bassins étroits.
- Ce qui l'attaque : retarde les essais de méthodes.
- Inventaire : nouveau.

#### [F25-49] Loi spontanée des proposeurs, saturation et masse manquante
- Définition : mesurer, par appels frais et indépendants, la courbe rang-fréquence des classes d'idées, la masse jamais vue (part des classes vues une seule fois, Good 1953) et le recouvrement entre familles de proposeurs ; si la masse manquante est proche de zéro, ajouter des appels est vain ; une classe jamais vue en N tirages a une probabilité inférieure à environ 3/N, résolution de l'étroitesse.
- Synonymes et paraphrases : saturation ; espèces non vues ; Good-Turing ; courbe d'accumulation ; homogénéité entre modèles.
- Source : réponse 28, A1, C1, C3 ; réponse 28-effort-max, A1, C1, C3 ; `05c72e054ed7b5af`, `1261c8eeb9f00711`.
- État : proposé.
- Liens : N-045 (diversité des proposeurs), organisme d'idéation.
- Ce qui l'attaque : estimateurs faux si appels dépendants ou classes instables ; Wenger et Kenett 2025, Goel et al. 2025, Doshi et Hauser 2024 : des familles différentes partagent les mêmes bassins.
- Inventaire : 2.15 (masse manquante, par analogie).

#### [F25-50] Grandeurs de l'originalité sans juge : classe, largeur, profondeur, justesse, fécondité
- Définition : la classe d'une idée est fixée par l'oracle sur monde planté, ailleurs par l'identité des prédictions sur un jeu public ; la largeur est la fréquence de la classe sous la vue ordinaire (étroite si rare pour chaque famille) ; la profondeur est le gain moyen de log-vraisemblance par tirage frais contre la meilleure loi du nul (taux de croissance des valeurs e) ; la justesse est la survie aux tirages frais ; la fécondité, l'écart de découvertes en aval avec et sans l'idée dans l'archive. Grandeur visée : puits étroits, profonds et retenus par unité de coût, à fausses promotions contrôlées.
- Synonymes et paraphrases : puits étroit et profond ; bassin banal ; rareté ; originalité mesurable ; D2 de la réponse 28.
- Source : réponse 28, C1, D2 ; réponse 28-effort-max, C1 ; `05c72e054ed7b5af`, `1261c8eeb9f00711`.
- État : proposé (confiance 0,8 ; distance de plongement en description seulement, jamais un modèle juge de nouveauté).
- Liens : organisme d'idéation, juge au nul formé des lois connues (O4, N-067, N-071).
- Ce qui l'attaque : limitée aux domaines où la classe se définit ; en course réelle, groupes de doublons seulement (borne 13 du recoupement) ; un puits n'est objet d'épreuve que si n·r·Δ dépasse le seuil de détection.
- Inventaire : nouveau.

#### [F25-51] Refuser la métaphore du paysage : l'étroitesse est relative à une mesure
- Définition : la largeur n'appartient pas à l'idée mais au couple (idée, loi des propositions sous une vue) ; plutôt que tirer plus fort, chercher le proposeur, la représentation ou le domaine sous lequel le puits est large. Rareté, justesse et fécondité sont trois grandeurs ; la plupart des idées rares sont fausses, donc le goulot est le coût de vérification par candidat.
- Synonymes et paraphrases : retourner la métaphore ; taux de base de la rareté ; pas de scalaire « originalité ».
- Source : réponse 28, A1 points 4-5 ; réponse 28-effort-max, A1 ; `05c72e054ed7b5af`, `1261c8eeb9f00711`.
- État : proposé.
- Liens : identité de coût d'un puits.
- Ce qui l'attaque : —.
- Inventaire : nouveau.

#### [F25-52] Identité de coût d'un puits retenu
- Définition : le coût attendu d'un puits retenu vaut à peu près (coût d'une proposition + coût de sa vérification) divisé par (fréquence de la classe × puissance de la garde) ; multiplier les candidats ne durcit le seuil du juge que comme un logarithme alors que la couverture de la queue croît à peu près linéairement : élargir serait rentable si la vérification est bon marché et le nul couvre la classe élargie.
- Synonymes et paraphrases : économie de la découverte ; garde contre proposeurs ; D4 de la réponse 28.
- Source : réponse 28, C1 (hypothèse), D4 ; `05c72e054ed7b5af`.
- État : hypothèse ; recommandation : garde et vérification d'abord (confiance 0,65).
- Liens : organisme d'idéation, juge statistique.
- Ce qui l'attaque : les deux conditions ne sont pas acquises.
- Inventaire : nouveau.

#### [F25-53] Huit familles de méthodes pour atteindre les puits étroits
- Définition : qualité et diversité (cartes d'élites, nouveauté seule) ; échantillonnage contre la vraisemblance (température) ; cible d'expert et vérificateur exact ; adversaire qui prédit le banal et le retire ; recombinaison contrainte ; abstraction et transfert ; curriculum vers plus dur ; programme à archive complète. Chaque méthode doit nommer la structure exploitée, connaissable sans l'oracle, et échouer là où elle manque.
- Synonymes et paraphrases : MAP-Elites ; novelty search ; FunSearch, AlphaEvolve ; Go-Explore ; POET ; liste V2 comme carte d'élites minimale ; C2.
- Source : réponse 28, C2 ; réponse 28-effort-max, A1, C2 ; `05c72e054ed7b5af`, `1261c8eeb9f00711`.
- État : occupé par la littérature (méthodes citées) ; transfert à l'organisme ouvert.
- Liens : organisme d'idéation, N-045.
- Ce qui l'attaque : la température lie peu la nouveauté (Peeperkorn 2024) ; doublons croissants (Si, Yang, Hashimoto 2024) ; écart idéation-exécution (Si et al. 2025) ; plagiat (Gupta et Pruthi 2025) ; curiosité attirée par le bruit (Burda 2019) ; exploitation du vérificateur (Lehman 2020). Synthèse : les succès tiennent à un vérificateur bon marché et une archive de paliers, non à un mécanisme de nouveauté.
- Inventaire : nouveau.

#### [F25-54] Banc à puits plantés
- Définition : familles de mondes fixées avant tirage, clé scellée par empreinte : puits à parent archivé ou détectable, puits hors structure (trois traits, seuil décentré, non monotone), chaînes de prérequis, puits transférable, mondes entièrement dans le nul, copies par morceaux, et un contrôle négatif (parité sans marge ou puits sans parent) où aucun bras ne doit battre l'énumération, sinon fuite. Bras à budget de jetons égal : organisme actuel, proposeur seul, énumérateur mécanique, nouveauté seule, méthode candidate, vue placebo.
- Synonymes et paraphrases : banc d'épreuve ; mondes plantés ; vérité plantée ; C4.
- Source : réponse 28, C4 ; réponse 28-effort-max, C4 ; `05c72e054ed7b5af`, `1261c8eeb9f00711`.
- État : proposé ; « je ne connais pas de banc publié » : question à vérifier.
- Liens : N-058 (oracle du monde planté), organisme d'idéation.
- Ce qui l'attaque : validité externe non établie ; désaccord ouvert du recoupement sur le puits sans parent, tranché provisoirement par Fable.
- Inventaire : nouveau.

#### [F25-55] Critère de réfutation des méthodes de puits
- Définition : écrit avant tirage, par famille de mondes : méthode sans effet si la borne basse de la différence appariée du taux de puits retenus contre la meilleure base n'est pas au-dessus de zéro, si les fausses promotions dépassent le niveau annoncé, si le gain disparaît hors structure, si l'énumérateur ou le placebo fait aussi bien, si un gain apparaît sur le contrôle négatif. Version effort maximal : démontrée, réfutée sous marge minimale d'intérêt, ou indécise et dite telle.
- Synonymes et paraphrases : test de mort ; critère de mort ; trois issues ; calcul de puissance après l'étape 1.
- Source : réponse 28, C4 ; réponse 28-effort-max, C4 ; `05c72e054ed7b5af`, `1261c8eeb9f00711`.
- État : proposé.
- Liens : R1, R3.
- Ce qui l'attaque : —.
- Inventaire : nouveau.

#### [F25-56] Catalogue de la fausse originalité
- Définition : formes de l'originalité apparente et leur mise à mort : bruit (juge sur tirages frais), bizarrerie de formulation (rareté comptée après réduction fonctionnelle ; refus de toute carte qui ne diffère du nul sur aucune instance), reformulation et copie par morceaux (nul étendu, canonisation, filtre mécanique), idée ancienne abandonnée, complication (gain par bit de description), assortiment à l'instrument, surajustement au banc, exploitation du vérificateur, idée infalsifiable, séduction du juge, obéissance feinte, sélection après coup des mondes étroits.
- Synonymes et paraphrases : fausse nouveauté ; C5.
- Source : réponse 28, C5 ; réponse 28-effort-max, C5 ; `05c72e054ed7b5af`, `1261c8eeb9f00711`.
- État : proposé.
- Liens : juge au nul formé des lois connues, J6 et J7 du recoupement.
- Ce qui l'attaque : Panickssery, Bowman, Feng 2024 (juges qui favorisent leurs propres sorties).
- Inventaire : nouveau.

#### [F25-57] Plan d'expériences des puits, du moins cher au plus cher
- Définition : étape 0 audit des pertes ; 1 saturation, loi spontanée et recouvrement ; 2 la vue déplace-t-elle la loi des propositions (vue ordinaire, placebo, liste V2, liste de classes banales ; sinon toute la section 2 du recoupement tombe) ; 3 qualification de la garde ; 4 banc complet ; 5 chaînes sur plusieurs générations avec contrôle en ligne des fausses découvertes ; 6 épreuves extérieures (vérificateur exact, rétro-prédiction datée, reproduction par un tiers).
- Synonymes et paraphrases : C6 ; réactivité à la vue.
- Source : réponse 28, C6 ; réponse 28-effort-max, C6 ; `05c72e054ed7b5af`, `1261c8eeb9f00711`.
- État : proposé (ordre des étapes 2 et 3 inversé entre les deux versions).
- Liens : organisme d'idéation, N-049, N-050.
- Ce qui l'attaque : —.
- Inventaire : nouveau.

#### [F25-58] Liste de classes banales servie aux proposeurs
- Définition : servir aux proposeurs une liste d'exclusion des classes spontanément fréquentes, sans score ni verdict : forme la moins chère de l'adversaire du banal. Elle s'approche de l'interdit « aucun score de nouveauté servi à un agent » et pousse vers la classe que le nul ne couvre pas.
- Synonymes et paraphrases : liste d'exclusion ; adversaire du banal ; D3 (réponse 28), D2 (effort maximal).
- Source : réponse 28, D3 ; réponse 28-effort-max, D2 ; `05c72e054ed7b5af`, `1261c8eeb9f00711`.
- État : proposé non tranché (bras d'essai au banc seulement, calculée sur lot disjoint, avec placebo, après qualification de la garde ; confiance 0,6-0,65).
- Liens : règle de l'organisme sur les scores de nouveauté, N-053 (analogue).
- Ce qui l'attaque : la masse peut glisser vers les voisines (reformulations).
- Inventaire : nouveau.

#### [F25-59] Revendication bornée et preuve extérieure pour l'organisme
- Définition : ne pas revendiquer « l'originalité » mais la récupération de puits plantés à budget égal, résultats négatifs compris ; preuve extérieure : banc reproduit par un tiers, domaine à vérificateur exact où le résultat dépasse le meilleur connu, puis rétro-prédiction datée sur textes postérieurs à la coupure et prédictions scellées jugées par un jury aveugle étalonné par des leurres. Aucun modèle juge dans la liste.
- Synonymes et paraphrases : validité externe ; rétrodiction ; leurres ; D4 et D3 (effort maximal), D5 (réponse 28).
- Source : réponse 28, A4, D5 ; réponse 28-effort-max, A4, D3, D4 ; `05c72e054ed7b5af`, `1261c8eeb9f00711`.
- État : proposé (confiance 0,85 pour la revendication bornée).
- Liens : papier C, organisme d'idéation (N-064, N-067).
- Ce qui l'attaque : contamination des modèles par les données d'entraînement ; mondes construits.
- Inventaire : nouveau.

#### [F25-60] Questions neutres sur les idées rares
- Définition : deux versions servables : un système de modèles propose des idées soumises à un contrôle indépendant fiable sur cas d'essai ; comment mesurer rareté et valeur sans juge, quelles interventions à coût égal, quelle expérience ferait abandonner chacune, quelles limites de principe ; la version effort maximal fixe une grammaire publique et un test statistique hors modèle.
- Synonymes et paraphrases : question neutre « idées originales » ; C7.
- Source : réponse 28, C7 ; réponse 28-effort-max, C7 ; `05c72e054ed7b5af`, `1261c8eeb9f00711`.
- État : proposé.
- Liens : protocole X, collisionneur.
- Ce qui l'attaque : test de devinette non joué.
- Inventaire : nouveau.


**VI. Tenir l'effort maximal (réponse 30)**


#### [F25-61] Hypothèses sur l'épuisement de la sortie en effort maximal
- Définition : quatre hypothèses : le compte à rebours du budget de tâche inclut l'entrée ou est lu ainsi (0,45) ; il l'exclut et sa seule vue rend le modèle économe (0,35) ; sans budget, la réflexion rédige plus qu'elle ne cherche, poussée par une consigne qui met tout le travail avant le premier mot (0,6) ; une part de la réflexion tourne en boucle (0,2). Un appel à budget voisin de 160 000 les départage.
- Synonymes et paraphrases : H-A à H-D ; effort max épuise la sortie ; budget de tâche ; réflexion courte.
- Source : réponse 30, § A ; `3f8c7a8498e59bab`.
- État : ouvert (hypothèses), confiance d'ensemble 0,5.
- Liens : règles d'appel aux modèles ; économie de Fable (GO-2026-11-21-75).
- Ce qui l'attaque : le modèle n'est pas une source fiable sur son propre service ; petit échantillon d'échecs.
- Inventaire : nouveau.

#### [F25-62] La profondeur n'est pas le compte de jetons de réflexion
- Définition : la cible est la meilleure réponse vérifiée, non le plus de jetons de réflexion ; l'effort maximal n'est gardé que s'il détecte au moins autant d'erreurs plantées que le niveau « très haut » et gagne au jugement à l'aveugle par un modèle d'une autre famille. Banc : copie d'une demande où trois erreurs connues sont glissées (un calcul faux, une page mal attribuée, une contradiction).
- Synonymes et paraphrases : banc à erreurs plantées ; xhigh contre max ; Décision 1 de la réponse 30.
- Source : réponse 30, § 1, § 3, § C, Décision 1 ; `3f8c7a8498e59bab`.
- État : proposé (confiance 0,7) ; prévision : le maximum détecte plus d'erreurs (0,35), autant (0,45).
- Liens : R4 (vérité plantée), économie de Fable.
- Ce qui l'attaque : longueur de raisonnement en cloche (Wu et al. 2025), surpensée (Chen 2024, Hassid 2025), budget annoncé comprime le raisonnement (Han 2024).
- Inventaire : nouveau.

#### [F25-63] Formes de demande pour tenir l'effort maximal
- Définition : du moins cher au plus lourd : budget réglé sur l'entrée (entrée + 90 000) ; consigne de discipline (« dans la réflexion : plan, calculs, objections ; n'y rédige pas la réponse ») ; analyse d'abord, conclusion remontée par script ; plafond de mots contrôlé par script ; plusieurs tours dans une conversation ; appels chaînés ; brouillon en « très haut » puis critique en maximal ; outil de dépôt de section ; sauvetage d'un tour épuisé. À écarter : baisser le plafond, écrire « réfléchis N jetons ».
- Synonymes et paraphrases : relance des demandes 22 et 23 ; trois tours ; essai par étapes sous plafond ; Décisions 2 à 5.
- Source : réponse 30, § B, § C, § D ; `3f8c7a8498e59bab`.
- État : proposé (relance de la 22 en un appel à budget entrée + 90 000, repli en trois tours ; affichage résumé pour l'essai, confiance 0,75 ; séquence avec réplication sur la 23).
- Liens : règle d'appel, journaux de dépense.
- Ce qui l'attaque : plusieurs changements à la fois dans la forme en tours ; compatibilité du sauvetage avec l'affichage omis inconnue.
- Inventaire : nouveau.

---


## 4. Tensions non résolues entre sources

Relevées de ma main en assemblant ; chacune renvoie aux fiches qui la portent. « Rapprochement de ma part » sauf mention.

1. **Réapprentissage des sondes en service contre l'invariant de l'oracle.** La ligne 170 du programme veut que chaque détection silencieuse devienne un exemple pour réentraîner les sondes ; N-060 v3, point 4, interdit toute sortie de l'oracle dans la sélection d'un moniteur. Nœud sans défaut ; Lazar « penche » pour l'option (b) et l'a renvoyé au collisionneur et à l'organisme (`GO-2026-11-21-61`). D'ici le mot, la boucle audit, recapture, réapprentissage ne vit que sur mondes plantés. Fiches : N075-25, N076-12, GO-20, RD21-33, F15-26.
2. **« Mesurer l'issue » contre « auditer des actes plutôt que des issues ».** Les deux sont accordés (`GO-2026-11-21-51` et `-61`) ; aucun texte ne les concilie. Fiches : N075-01, N075-28 ; voir aussi F15-27 (unité de tirage : le sous-résultat audité par ré-exécution).
3. **« Aucun retour à l'agent » contre corriger avant l'alarme, et contre l'expérience de la riposte (H7).** Sous la lettre accordée, corriger avant l'alarme est interdit ; la proposition rivale (trois lignes de la note sur les asymétries) n'est pas tranchée. Fiches : N076-14, N076-18, N076-23.
4. **Règle d'horizon de la référence honnête contre l'énoncé de H2.** « Le rappel croît avec l'horizon » promet plus que la loi ne permet sous référence fixe (horizon au plus m) ; modifier H2 est un nœud, non ouvert. Fiches : N076-04, N076-23 ; F22-11, F22-12.
5. **La règle à deux clés : lettre du 21 contre réécriture.** `GO-2026-11-21-51` portait « nouveauté seule = mise à jour des témoins » ; l'erratum 3 v2 de N-075 (accordé à `GO-2026-11-21-61`) l'a remplacée par « motif seul : file d'audit, jamais témoin ». Le registre (fiche GO-15) garde la lettre ancienne : lire N075-16.
6. **Thèse du papier A : plusieurs versions le même jour.** « Mieux que la boîte noire » rétrogradé en résultat conditionnel de G1 (F08-01) ; « bilan d'incertitude » (F08-20) ; « loi héritée comme modèle nul, bilan mesuré, complémentarité » (F22-01, F25-40) ; et le constat « le papier A a perdu sa thèse » (F01-34). Le registre (GO-43, RD22-01) donne l'état accordé ; plusieurs agents signalent que la thèse retenue n'est datée que par la réponse 27, sans identifiant GO vu par eux : **à vérifier au registre avant toute citation**.
7. **Le compte par chute conjointe : neuf ou occupé.** Lazar en fait « notre nouvelle manière de compter les interventions » ; la réponse 29 le juge probablement occupé par la sûreté de fonctionnement (pannes coïncidentes de versions diverses). Fiches : F25-19, F25-26 ; inventaire 5.1 à 5.4.
8. **« Blindfold » : lu ou ignoré.** L'inventaire (2.1) et N-075 le donnent lu sur PDF et occupant ; la réponse 17 de Fable l'ignore. Les statuts d'antériorité de la réponse 17 sont donc à relire. Fiches : F15-19 à F15-30.
9. **Le lot tenu à l'écart : une tranche par cycle protège le chiffre, pas l'adjectif.** La réponse 23 corrige ce que la réponse 19 avait fait accorder. Fiches : F22-61, F15-40.
10. **Revendications du papier C et du papier B.** La réponse 22B dit qu'aucune revendication du papier B ne tient telle qu'écrite ; la 22C, que « non touché » ne vaut rien pour le papier C ; la 22P, qu'il ne reste pas de colonne vertébrale théorique au programme. Ce sont des propositions de Fable, à confronter aux accords du 22 (GO-45, RD22-16).
11. **Version 3 du programme.** La réponse 27 relève que la v3 en différences ne reporte pas les décisions postérieures au 4 octobre et porte encore H6, retirée par N-077. Fiches : F25-37, RD22-18.
12. **Trois honnêtes de contrôle contre « honnête imparfait ».** Tout invariant doit d'abord passer l'honnête qui échoue, celui qui « sait » et se trompe, celui qui refuse (inventaire 3.5 ; GO-29) ; l'expérience des fausses alertes sur honnêtes réels et imparfaits (F01-25, RD22-10) en est la mesure, non tranchée dans sa forme.

## 5. Idées retirées, blocages et résultats négatifs déjà rencontrés

En mots, avec le motif et ce qu'on en a tiré ; aucun chiffre cloisonné, aucun contenu d'attaque (recommandation D5 de la réponse 32). Classés par lot de sources. Une même impasse peut paraître sous plusieurs lots (par exemple le retrait du théorème négatif : RD22, F08, F15, F22, F25).

**Depuis `N075` — Décision N-075 v3 et ses errata (mesurer l'issue, plancher, deux regards)**

- **La règle à deux clés réécrite après lecture sur PDF** : la source d'immunologie appliquée (Aickelin et Cayzer) contredit la description « de mémoire » : la première clé n'est pas la nouveauté, et la tolérance transposée laisserait le saboteur se faire accepter. On en a tiré la forme « motif et dommage au même endroit ; motif seul en audit, jamais dans les témoins », accordée par Lazar (v3 section 4 ; erratum 3 v2, point 8). En v1, l'énoncé retenu était « nouveauté seule = mise à jour des témoins » et la règle dite « occupée dans sa forme » : les deux sont retirés (le second « n'est pas établi »).
- **« Pour toute politique d'attaque » faux sans horizon** quand l'honnête produit aussi le dommage : un saboteur qui ralentit fait croître l'excès, l'alarme peut ne jamais venir. Tiré : garantie à horizon donné avec référence honnête, grille de mises et excès toléré (v3 section 2 ; correction A1 du contre-lecteur). La v1 disait « pour toute politique dont l'oracle voit le dommage » sans horizon.
- **q supposé** : la borne du plancher valait ce que valait la supposition sur q. Tiré : q mesuré par dommages plantés, strate non mesurée comptée à zéro ; conséquence assumée : aucune borne chiffrée tant que rien n'est planté (erratum 3 v2, 4.1).
- **Le plancher est occupé** (Blindfold, Gans et Holden, Podkopaev et Ramdas) : la v1 et la v2 proposaient d'en revendiquer « la forme » (écriture du plancher comme borne chiffrée de la sécurité et base à battre) ; retiré en v3 : base citée, jamais revendiquée (V1).
- **La règle « moniteur invalide »** déclarerait invalide en service un moniteur valide plus d'une fois sur deux faute de connaître la part du sabotage (sous supposition) : restreinte à l'après-alarme, avec estimation de cette part ; partiellement occupée.
- **Le dilemme ne paie que si chaque regard voit au moins la moitié des attaques neuves** (borne 2m − 1, sous supposition) ; la v1 posait « le programme cherche des dilemmes » sans cette limite.
- **Le bilan du produit** : la v1 et la v2 revendiquaient « dans sa forme » le bilan contre le jumeau honnête ; la v3 le dit partiellement occupé, reste étroit = question (V2).
- **Le bilan de la pince** : la v1 écrivait « seul le bilan se revendique » d'après le mandat, sans que la ligne du GO le porte (réserve de transcription) ; v3 : « pourrait se revendiquer, sous un verdict d'antériorité propre », aucune recherche d'antériorité faite.
- **Le lemme** : l'invariance à horizon fixe (L1) et la séparation avec le maximum (L2) sont publiées (1981, 1982, 1985) : sorties de la revendication ; le reste valide à tout instant est lui-même partiellement occupé (Khosravi et Huo ; test de puissance un du rapport de 1985) ; il reste un énoncé étroit, non démontré ; le prix de la garantie et la détection avant le dommage sortent aussi (erratum 3 v2).
- **Heurt de l'asymétrie d'apprentissage avec l'invariant de l'oracle** : non résolu, nœud ouvert (point 9).
- **Contre-indices au passage obligé et à l'étau** : état précurseur qui ne sépare pas triche et échec honnête sur un modèle (Fischl-Lanzoni et al.) ; résultats négatifs de sondes d'avant l'action (Fomin et al.) ou égalés par une base de texte (Sinha) ; aucun détecteur mécaniste efficace partout (Johnston et al.) ; évasion apprise (McGuinness et al.).
- **Le numéro N-074 pris** par deux brouillons non retenus d'un durcissement de la porte de fin de phase 1 : d'où N-075.
- **Pièce écrite deux fois** : l'erratum 2 (mère d'un compte, Fable indisponible jusqu'au 27 novembre) et l'erratum 3 (Fable, sur mandat d'une autre session) à quelques minutes d'écart ; tiré : relever dossier et registre avant de commander une pièce. L'erratum 3 v2 corrige trois défauts de l'erratum 2.
- **Pièces non contre-lues** sur lesquelles la décision s'appuie : la note sur la pince, la lecture des douze voisins, la note sur la couverture de l'oracle (premiers pas non justifiés du relevé de méthode).

**Depuis `N076` — Décisions N-076 (audit et référence honnête) et N-077 (retrait de la marge asymétrique)**

- **Le plancher d'audit au hasard est occupé** par la littérature (« Blindfold » 2610.37055, verdict 6 de la lecture des douze voisins ; aussi Podkopaev-Ramdas, Gans-Holden) : il devient une base nommée et citée, jamais une revendication ; Lazar en a pris acte et a ouvert un protocole X « que reste-t-il, où est la percée » (`GO-2026-11-21-60`). Source : N-076 erratum 1, E1, E4.
- **Presque tout N-076 est partiellement occupé** (attestation en service, audit en trois parts, boucle, devin, audit orienté) ; les quatre invariants et la table sont élémentaires ou publiés : rien revendiqué. Source : N-076, § 5 à 9.
- **Points 1 à 3 sans verdict d'antériorité** (recherche des travaux citant le billet de Hebbar accordée à `GO-2026-11-21-50`, non au dépôt) : rien ne se revendique avant. Source : N-076, en-tête.
- **Heurt boucle de réapprentissage / invariant de l'oracle** (N-060 v3, point 4) : blocage ; la boucle ne vit que sur mondes plantés jusqu'au mot de Lazar. Source : N-076, § 6.2, § 13 point 3.
- **Heurt « aucun retour à l'agent » / correction avant l'alarme** : sous la lettre accordée, corriger avant l'alarme est interdit ; nœud D-2 des asymétries non tranché. Source : N-076, § 8.
- **Heurt « aucun retour » / expérience de la riposte (H7)** : une ligne toujours active supprimerait l'objet ; lecture « ablatée » à confirmer. Source : N-076, § 13 point 2.
- **Règle d'horizon contre l'énoncé de H2** : « le rappel croît avec l'horizon » promet plus que la loi permet sous référence fixe ; non corrigé (modification d'hypothèse = nœud). Source : N-076, § 2 et § 13 point 4.
- **Rudoler et al. non lu par le verdict** : le reste revendicable de la boucle est plus étroit qu'annoncé. Source : N-076, § 6.2.
- **Écart de méthode** : l'auteur a voulu corriger la v1 déjà scellée ; l'outil a refusé (R12) ; v1 rétablie à l'octet, erratum écrit. Leçon : relire le registre des accords juste avant de sceller. Source : erratum 1, « Écart déclaré », « Trouvaille de côté ».
- **Empreinte mal recopiée** dans N-076 (lecture des douze voisins) : corrigée par l'erratum 2.
- **Retrait de la marge asymétrique (H6)** : contre un saboteur qui répond au mieux, aucune des trois interventions ne garde de marge ; une marge mesurée sur nos organismes lirait leur fabrication ; tiré : mesure gardée, descriptive, avec règle de lecture et retour possible seulement sur résultat. Aucune mesure faite. Source : N-077, § 1-3.
- **« Taxe de robustesse » et « H6 resserrée » non retenues** ; « taxe de cohérence » non inscrite. Source : N-077, § 5-6.
- **Collision réalisée** avec la feuille de route de Google DeepMind (2607.13087) pour l'idée de l'affaiblissement sélectif de l'attaquant. Source : N-077, § 1.

**Depuis `GO` — Registre des accords de Lazar, 21 et 22 novembre**

- Plancher d'audit occupé : GO-2026-11-21-60 (l. 659).
- Loi de la référence honnête occupée : GO-2026-11-22-20 (l. 707).
- Lemme et théorème négatif retirés comme résultats : GO-2026-11-22-24 (l. 711).
- H6 retirée : GO-2026-11-21-64 (l. 663).
- Contrôle actif par sélection fermé : GO-2026-11-21-25 (l. 624).
- Échec de l'essai Lean : GO-2026-11-21-36, -40.
- Argon sans réflexion : GO-2026-11-21-71, GO-2026-11-22-08.
- Collisionneurs arrêtés pour clé sans crédit : GO-2026-11-21-28.
- Faux positifs de classifieur : GO-2026-11-21-74, GO-2026-11-22-35.
- Revue externe refusée pour l'instant : GO-2026-11-21-71, -72.
- Refus de geler : GO-2026-11-22-32.
- Refus de contournement : GO-2026-11-22-34.
- Relecture par spécialiste de stéganalyse jugée inutile : GO-2026-11-22-42.
- Confiance basse de l'étau : GO-2026-11-21-53, GO-2026-11-22-22.

**Depuis `RD21` — Registre des décisions, 21 novembre**

- Deux refus du catalogue de sabotage opérationnel (classifieur) : passage au niveau de l'idée (l. 4499, 4536, 4542).
- Plancher d'audit au hasard occupé (« Blindfold ») : base citée, rien revendiqué (l. 4686).
- Aucune des trois pistes de percée n'en est une en l'état (l. 4764).
- Marge asymétrique H6 retirée : aucune marge contre un saboteur qui répond au mieux (l. 4756, 4763).
- Aucun mécanisme adjudant ne tient sans condition face à un attaquant informé (l. 4701).
- Papier « dopamine » : forme de P2 et conclusion de H-D publiées en boîte noire (Lin et al.) ; pas d'états internes pour les honnêtes ; garde de taux d'alerte mal calibrée (l. 4490, 4672).
- Expérimentateurs et tests de mort : rien de branché en général ; les fiches proposent des mécanismes et non des lois (l. 4559, 4532).
- Lean : épreuves non conformes au troisième essai, puis un cas non établi au quatrième (l. 4650, 4826).
- Palier 0b : essai 1 coupé à deux heures, essai 2 tué par un redémarrage ; récupération versée (l. 4592, 4663).
- Clé Rigaud vidée par erreur de la mère : réserve du bras A consommée (l. 4645) ; crédit d'Astra épuisé (l. 4670).
- Refus de classifieur sur l'organisme (quatre coupures), accès au dépôt de l'orchestrateur refusé, non contourné (l. 4753, 4775, 4796).
- Limite de Fable atteinte deux fois : relecture par l'API (l. 4650, 4797, 4841).
- Étalonnage du saboteur arrêté par sa garde avant chargement, puis repris (l. 4866, 4888).
- Banque des tâches de réserve : aucune conforme, toutes les tâches de T0.5 ont servi (l. 4862).
- Lentilles et barreau 5 : courses consignées (l. 4842 ; formation, l. 4479-4884), aucun chiffre repris ici.
- Défaut : une demande de Lazar servie par erreur à un flux, dont les agents ont refusé (l. 4845).

**Depuis `RD22` — Registre des décisions, 22 novembre**

- Loi héritée en racine : occupée et inexacte sous la forme écrite ; retirée comme thèse, gardée comme nul (R-4767, R-4768, l. 4906-4907).
- Théorème négatif : inexact, contredit (Arias-Castro, Bubeck, Lugosi 2012), occupé en boîte noire ; retiré comme résultat, reconverti en question empirique (R-4768, R-4769, R-4771).
- Lemme d'additivité et bruit honnête : occupés ; on ne peut écrire ni « inédit » ni « premier à transposer » (R-4771).
- « Horizon au plus m » de N-076 : redit Ker 2010 (R-4767).
- Épreuve aveugle des motifs v1 : fausse (comptait la longueur du couple) ; rejouée, voie (b) (R-4772).
- Effort maximal de Fable : un succès sur cinq essais, défauts sans texte ; découpage et budget de tâche ; réserve de bridage (R-4802, R-4831).
- Clé Minuit sans crédit : demande 27 refusée, rôles de la course bloqués (R-4833, R-4852).
- Refus de classifieur, jamais contournés : création de la machine de l'organisme (R-4762), relecture des lentilles par Fable (R-4763, relues par un Opus, écart déclaré), reprise du papier dopamine (R-4839), lots du véhicule (R-4828, R-4832, R-4851).
- Course « nouvelles attaques » : ne part pas le 22 (lots absents, épreuves non faites) ; additif « à corriger » (six bloquants) (R-4801, R-4818).
- Étalonnage du saboteur : rythme très au-delà du devis, cause lue chez l'hôte non vérifiée ; lots non poussés au fil du run (R-4751, R-4774).
- Pilote de l'essaim : borne de dépense fausse au-delà d'une invocation (R-4810, R-4825).
- Mère : seconde session des mathématiques nouvelles lancée par erreur, effacée (R-4847).

**Depuis `F01` — Réponses de Fable aux demandes 1 à 7 (22 novembre)**

- **Aucune revendication de méthode inédite sur l'audit** : le cœur convergent est occupé (audits financiers à risque limité par tirage pondéré, inférence par prédiction, inférence hors politique toujours valide). Tiré : méthode empruntée et citée, nouveauté seulement en mesure ou protocole (rép. 2, conclusion et (b)).
- **Coercition, corruption et flagornerie densément occupées** : chacun des volets a une antériorité directe ; pas d'axe propre, pilote d'abord, puis modes par additifs ; une seule hypothèse nouvelle pour la flagornerie (le levier propre) (rép. 1, R3 ; rép. 6, R2).
- **Les « trois planchers » en théorème** : jugés probablement occupés ou faux tels qu'écrits (l'aléa commun peut réduire le bruit honnête) ; rangés en limite (rép. 2, R5, décision 5).
- **Part universelle** : vraie par construction ou anecdotique avec un seul mode ; reléguée en section de limites (rép. 4, Q4 ; rép. 2, (b)).
- **Thèse du papier A perdue** après les décisions sur l'issue, la référence honnête et le retrait de la marge ; d'où la proposition de la loi d'échelle (rép. 4, conclusion).
- **Issue nulle probable des audits économisés** : dilution par les accidents honnêtes ; jugée publiable (rép. 2, R2 ; rép. 4, Q2).
- **Lemme d'additivité possiblement occupé** par la loi de la racine carrée de la stéganographie et la critique supérieure (rép. 4, Q1).
- **Lectures écartées** : raisonneurs à énergie (aucun point d'appui) ; cœur invariant du sabotage non ouvert comme axe (zone vierge séduisante) ; chiffres de DiscoveryAgent et de Re-Search non opposables (corruptions non adverses ; conclusion mal fondée) ; incohérences relevées dans plusieurs fiches de lecture (rép. 5, § 1.1 et 3.1).
- **« Montrer que ça marche » se heurte à l'interdit des essais visant un signe positif** ; reformulé en essai sévère perdable ; l'entraînement de l'agent bute sur l'invariant N-053, y compris par la voie indirecte de la sélection des exemples (rép. 7, partie 3).
- **Essaim du collisionneur** : l'attente par défaut n'est pas qu'il gagne ; sans répétitions, la comparaison n'est que descriptive (rép. 7, partie 2).
- **Questions neutres** : fuites résiduelles reconnues et non éliminables (rép. 7, partie 1).
- Aucune de mes sept réponses ne contient de résultat chiffré des expériences protégées par la consigne ; les rares chiffres sont des seuils illustratifs de Fable (rép. 3) ou des chiffres de sources externes rapportés, que je n'ai pas recopiés sauf exceptions sans portée.

**Depuis `F08` — Réponses de Fable aux demandes 8 à 14**

- **Thèse « mieux que la boîte noire »** : affaiblie par N-075, N-076, N-077 ; rétrogradée en résultat conditionnel de G1 ; une issue négative ne laisserait rien comme thèse (R8, section (1)).
- **L'étau comme thèse** : refusé pour le papier A (bras d'attaque déclaré nécessaire, hors champ laissé par N-077, contre-indices nombreux) ; la « borne » est jugée presque sûrement fausse ; contre le gradient sur sonde connue, aucune conception ne crée de dilemme (R8, 2.3 ; R11, conclusion). Tiré : énoncé restreint, ι comme mesure au papier C.
- **Chance basse de l'étau** : reportée d'un énoncé voisin sans recalcul ; reconstruite par régime (R11, réserves et (1)).
- **Loi héritée comme thèse** : retirée après lecture sur PDF ; élémentaire et occupée ; devient le modèle nul (R9). La « bascule » n'est plus une prévision.
- **Théorème négatif** : inexact pour la somme et le maximum ; corrigé, trivial ou occupé ; retiré comme théorème, gardé comme question empirique (R9, (2)).
- **Lemme d'indifférence à la répartition** : tombe pour son énoncé central ; sa forme séquentielle douteuse (R9, (3)).
- **Prévision « exposant > 1/2 par dépendance »** (réponse 4) : mal fondée (R9).
- **Douze phrases fautives** dans des pièces à empreinte : erratum proposé (R9, (4)).
- **Budget égal de la réponse 7** : mal spécifié (erreur de conception de Fable) ; parts égales en dollars → modèles chers muets ; incohérence apparente du devis (la borne « sous les parts » dépasse le pire sans relance) à faire vérifier (R13).
- **Rétro-analyse lexicale** : ne peut pas lire l'utilité d'un tour ; d'où règle asymétrique, le tour n'est rendu facultatif qu'avec une mesure à oracle (R10).
- **Comparaison essaim contre isolé** : issue la plus probable « non distinguable » ; vingt exécutions ne donnent qu'un indice (R10).
- **Coût de l'essaim** : réduire seulement les proposeurs divise peu le total ; la part non réduite (tests de mort, objets de contrôle) borne le gain (R14, A.1).
- **Abonnement comme calcul** : écarté (validité, conditions d'usage, reproductibilité) (R14, C.2).
- **Banc à dommage mesurable** : risque que la fenêtre de dose soit vide sur un 8 milliards ; « dommage continu » déjà partiellement occupé (R12).
- **Cœur invariant** : chance faible ; poids nul en mode dépendance (R12).
- Aucun résultat chiffré des expériences 7a, 7b, T0.6, étape B, étape B bis, P3-bis ni du barreau 5 ne figure dans ces sept fichiers.

**Depuis `F15` — Réponses de Fable aux demandes 15 à 21**

- **Théorème négatif contredit et retiré** : contredit par Arias-Castro, Bubeck, Lugosi 2012, occupé en boîte noire par 2606.10456 ; aucune des trois voies ne donne de théorème neuf en titre. Tiré : une phrase juste (seuls les mélanges de décisions sur un pas sont exactement aveugles), un modèle nul pour B, une proposition de cadrage pour A. `reponse-16/relecture-fable-api.md`, conclusion.
- **Énoncé scellé puis contredit** : leçon de méthode : calcul exact et simulation avant tout scellement d'un énoncé. `reponse-16`, décision 2.
- **Arbres de citations en échec** (quotas épuisés sur quatre arbres) : interdit d'écrire « non trouvé » sur les voies 2 et 3 et dans le billet. `reponse-16`, décision 5 ; `reponse-17`, décision 1 ; `reponse-20`, § B4.
- **Aucune recherche sur le tirage dans les pièces** : statut « non cherché », aucune zone inoccupée déclarable ; « Blindfold » inconnu de Fable. `reponse-17`, conclusion.
- **Le noyau de l'audit au hasard est du manuel** (sondage, inférence active, audits à risque limité, jeux d'inspection) : rien revendicable ; le gain de la variable de contrôle est modeste à corrélation moyenne. `reponse-17`, § b, § d.
- **Prochaines étapes des concurrents introuvables** : trois seulement, faute de rubrique dans les notes ; cette moitié de la demande 18 reste sans réponse. `reponse-18`, conclusion, § F.
- **Course perdue d'avance sur les jeux de Parrack** : ils ont sondes, jeux et moniteurs ; l'avance n'existe que sur le diffus. `reponse-18`, § E.
- **Aucune des trois sources d'attaques n'est une équipe rouge indépendante aujourd'hui** (probablement) ; le lot tenu à l'écart ne s'adapte pas ; motif de la quarantaine inconnu, rien ne s'ouvre tant qu'il manque. `reponse-19`, § a, § d.
- **Aucun résultat revendicable pour le billet** : les pièces ne contiennent aucune mesure ; la table des revendications du 19 novembre est en retard sur le retrait de T et L. `reponse-20`, conclusion, § B2.
- **Rien ne garantit l'existence des cœurs** ; trois cœurs sur cinq risquent d'être hors de portée de l'organisme de 8 milliards ; le saboteur compilé n'a rien à lire ; l'échec de l'intervention est ambigu. `reponse-21`, conclusion, R2, R4.
- **Abonnement** : aucune pièce ne tranche la boucle automatisée ; la chaîne par modèle sous abonnement épargnerait peu et rendrait la mesure non opposable ; le « repli de modèle à l'approche du quota » de la réponse 14 est retiré (absent des pièces) ; le kit d'agents n'est pas « exclu » pour l'usage individuel (erreur de la réponse 14 infirmée). `reponse-15`, réponse courte, § C.3.
- Aucun chiffre des expériences 7a, 7b, T0.6, étape B, étape B bis, P3-bis ou du barreau 5 ne figure dans mes fichiers.

**Depuis `F22` — Réponses de Fable aux demandes 22 (A, B, C, P) et 23**

- Lemme d'additivité et théorème négatif retirés comme résultats (occupés par Avenhaus et Jaech, Ker, Zhang et Gao, Arias-Castro et collaborateurs, Khilar) : on en tire une thèse de mesure contre un nul hérité, et deux questions (étalement en séquentiel ; position ou dépendance). Réponses 22 et 22A.
- L'accumulation toujours valide est vraie par construction sous la loi citée : elle ne peut pas échouer ; remplacée par « l'écart au nul est le résultat ». Réponse 22A.
- Le régime n/√m cité comme nul n'est pas observable avec des exécutions jumelles : la prévision porterait sur un terme absent ; d'où le choix du plan de référence avant scellement. Réponse 22A.
- Le seuil « à 1 % » de G1 est lui-même estimé : comparaison de moniteurs possiblement indécise ; d'où l'intervalle du taux réel. Réponse 22A.
- Puissance probablement insuffisante pour l'exposant sans un grand nombre de tâches : l'exposant reste sans prévision, τ passe en tête. Réponses 22, 22A.
- Papier B : aucune revendication ne tient telle qu'écrite ; la thèse de N-069 promet une supériorité que la somme globale peut annuler ; si seule la position bouge, le papier se réduit à une section de A. Réponse 22B.
- Diversité des moniteurs : loi élémentaire, retirée comme loi. Réponse 22B.
- Papier C : « non touché » ne vaut rien, la recherche ne le visait pas ; prédictions « déplacement nul » irréfutables telles qu'écrites ; loi de déférence sans nul. Réponse 22C.
- Mode commun : six revues du même modèle ; accord ininterprétable sans témoins ni autre famille. Réponse 22P.
- Il ne reste pas de « colonne vertébrale théorique » au programme. Réponse 22P.
- Lot sous scellés : Fable n'a ni registre, ni motif, ni définition ; ce qu'il prouve reste conditionnel à sa nature ; la tranche par cycle accordée après la réponse 19 ne protège pas l'adjectif (auto-correction). Réponse 23.
- Fichier des dix-sept décisions du papier C absent de l'arbre selon la table. Réponses 22C, 22P.

**Depuis `F25` — Réponses de Fable aux demandes 25 à 30**

- Le signal de dopamine n'ajoute aucune puissance au bilan de la pince (télescopage) : il ne donne qu'une date et une adresse ; d'où sa place réduite à la complémentarité mesurable (réponse 25, § B1, `f5b2d7115446f4db`).
- La surprise par étape se réduit, sommée, à l'écart fin moins début : rien à ajouter au bilan, rôle de localisation seulement (réponse 25, § B1).
- La sonde de surprise publiée emploie une moyenne sur jetons et une normalisation sur la réponse entière : inutilisable en ligne et contraire à N-026 (réponse 25, § B5 ; réponse 29, § R5).
- Le signal lit l'échec attendu, non l'intention ; un précurseur publié ne sépare pas triche et échec honnête ; un attaquant qui déplace ses représentations tait toutes les lectures d'états ensemble : la classe A compte pour une intervention au plus (réponses 25 et 29).
- Issues négatives écrites d'avance de la première expérience (chaîne non reproduite, V non calibré, dispersion jumeau contre jumeau trop grande) ; un apport nul chez l'honnête ne tue pas l'étau (réponse 25, § B6).
- La lecture « Δ indiscernable de zéro = boîte noire déguisée » est retirée comme trop forte (réponse 29, § R3).
- En service, faute de jumeau, rien ne se dit sur l'écart de lecture ; la question de qui produit la référence reste ouverte (réponse 25, § B2).
- Organisme d'idéation : aucun rôle possible du signal (états non lisibles d'un modèle servi par interface, pas d'issue calculée) ; hypothèse à confirmer (réponse 29, § R1).
- Barreau 3 de l'étau (attaquant entraîné contre la lecture interne) refusé pour l'instant : il toucherait l'invariant « aucun score de moniteur dans l'entraînement de l'agent » (réponse 29, D-4).
- Le compte par chute conjointe est probablement occupé par la sûreté de fonctionnement (pannes coïncidentes) (réponse 29, « Antériorité »).
- Théorème négatif : lettre inexacte, contredite par Arias-Castro, Bubeck, Lugosi ; retiré comme résultat, gardé mentionné. Lemme d'additivité et son reste : retirés comme résultat, énoncé occupé ; la forme séquentielle devient une question (réponse 27-luc, EN-1, EN-4, D6-D8).
- La loi en racine est déjà transposée au suivi des usages (Khilar 2026) : « premier à transposer » ne s'écrit pas ; la bascule « entre m et m divisé par le taux d'audit » n'a pas de fondement ; la transition en n ≈ m est par construction, pas une prévision ; « l'exposant dépasse un demi » est faux sous dépendance courte (réponse 27-luc, E4-1 à E4-6).
- La règle de la référence honnête est l'application du corollaire 1 de Ker 2010 : rien n'y est revendiqué (réponse 27-luc, E4-6, EN-9).
- La version 3 du programme ne reporte pas les décisions postérieures au 4 octobre ; H6 retirée par N-077 y figure encore (réponse 27-luc, notes).
- Le plateau de la loi héritée est une citation chiffrée, non un résultat ; le candidat A et le billet drapeau sont un doublon (réponse 26, § B1).
- Le billet sur les sondes reste renvoyé : pas de résultat sur saboteur discret, explication concurrente par l'empreinte de la consigne non contrôlée (réponse 26, § B3). Les verdicts des étapes B et B bis existent ; aucun chiffre ici.
- L'expérience 1 du billet « Reasons or watching? » est lue « non lisible » ; toute phrase qui l'annonce à venir est périmée ; une absence d'effet ne s'écrit pas sans borne d'équivalence (réponse 26, § B4).
- Organisme : on ignore si les idées étroites ne sont jamais proposées ou proposées puis perdues ; fréquences des classes étroites indiscernables de zéro au budget d'un pilote ; correspondance doublon-idée non établie ; température et nouveauté faiblement liées ; doublons croissants avec le nombre d'idées ; familles de modèles moins indépendantes qu'on ne croit (réponses 28, C1, C2).
- Effort maximal : quatre appels sur cinq épuisés dans la réflexion sans texte ; un réglage maximal qui ne bat pas « très haut » sur banc à erreurs plantées n'est pas tenu ; plus d'effort maximal sans budget ni discipline (réponse 30, § D).

## 6. Nœuds et points ouverts

Liste tirée par programme des fiches dont l'état dit « non tranché », « nœud », « ouvert », « à confirmer » ou « en attente » ; la ligne d'état est coupée à 260 signes. Une proposition de Fable sans identifiant GO y figure comme « proposé non tranché » : son sort réel est au registre.

- [N075-06] Campagne de dommages plantés par un tiers — ouvert ; nœud (dépense et cloisonnement : devis et mot de Lazar), après le collisionneur (`GO-2026-11-21-61`).
- [N075-08] « Corriger » : la liste fermée des suites d'une alarme — retenu pour la liste ; l'entraînement sur l'issue est fermé, recommandation de le laisser fermé (confiance du contre-lecteur 0,8) ; s'il s'ouvre, bras à part et nœud. Non nommé à `GO-2026-11-21-61` : reste tel que la v3 le laisse.
- [N075-09] Recapture, et la règle « moniteur invalide » — partiellement occupé ; il n'en reste qu'une question (R8) : la règle portée sur le rappel face à un agent qui choisit où et quand nuire, avec borne écrite du dommage accumulé avant qu'elle sonne ; toute revendication est un nœud ; à re-dériver par un agent qui
- [N075-10] Le plancher hors de la liste des bases de la porte de fin de phase 1 — proposé non tranché : recommandation (a) « non, rapporté à côté » jusqu'aux mesures exploratoires (0,65 ; contre-lecteur 0,7), à rouvrir avant le scellement du préenregistrement de cette porte ; nœud sans défaut. Non nommé à `GO-2026-11-21-61`.
- [N075-18] File d'audit prioritaire, à côté de la part tirée au hasard — retenu (`GO-2026-11-21-61`, point 8 (a)) ; pas de nœud, sa part se déclare dans le texte qui l'écrit.
- [N075-19] Bilan du produit fermé contre le jumeau honnête — candidat retenu au banc de la course de l'adjudant, avec deux tests de mort écrits d'avance (muet sur une famille plantée « dommage hors comptes » ; mort « sans gain » sur la famille tenue à l'écart face à la base « mots et coût ») ; premier pas sans dépense :
- [N075-20] Le passage obligé : ce que tout sabotage délibéré doit calculer — ouvert (question de recherche, § 15 du programme) ; rien revendiqué, la question n'est pas dite neuve. Direction candidate d'un cycle de reconception des sondes (N-062), conçue sur les modes vus seulement.
- [N075-22] Lemme d'additivité resserré à sa forme valide à tout instant, sur scores de sondes — retenu, revendication resserrée, `GO-2026-11-21-47` (point 4) puis `GO-2026-11-21-61` (point 10 (a)). Non déclaré libre (« non trouvé » par une lecture non contre-lue) ; non démontré : démonstration à faire par une version de la note mathématique, contre-lue. 
- [N075-24] Référence honnête en service — ouvert ; avis suivi : tâche de conception plutôt que nœud, premier pas exploratoire de l'épreuve de netteté de la référence (décision D-3 de la note sur la pince, `GO-2026-11-21-50`) sur honnêtes seuls ; Lazar ne fixe que la priorité (confiance 0,6). D'ici là,
- [N075-25] L'asymétrie d'apprentissage contre l'invariant de l'oracle (réapprentissage des sondes en service) — **non tranché**, nœud sans défaut. Options : (a) restreindre la l. 170 (recommandation de l'auteur, 0,6) ; (b) restreindre l'interdit au banc et permettre le réentraînement en service (Lazar « penche » pour (b), « demande au collisionneur et organisme dans la 
- [N075-26] La veille dégelée sans borne de zone, à côté des trois chantiers — retenu, `GO-2026-11-21-51` (point 4) puis `GO-2026-11-21-61` (point 7 (a)) ; pas de nœud.
- [N075-28] Auditer des actes plutôt que des issues ; part des attaques jamais vues intégrée au contrôle — accordé par Lazar mais sans pièce propre : ouvert, à écrire.
- [N076-10] L'attestation en service des sondes — **candidate** (ni hypothèse, ni instrument admis, ni porte) ; texte et bras à part déjà accordés (`GO-2026-11-21-46`, D-6 ; `GO-2026-11-21-51`, point 6) ; entre aux questions ouvertes. Partiellement occupée ([verdict, 2]).
- [N076-12] La boucle audit, recapture, réapprentissage — à faire **sur mondes plantés seulement** ; aucune sonde du programme réapprise sur des verdicts de l'oracle avant le mot de Lazar. Heurt avec l'invariant de l'oracle (N-060 v3, point 4) renvoyé : recommandation (a) réapprentissage sous cloison par texte à part
- [N076-17] Les quatre invariants d'audit (section 9 du programme) — retenu (`GO-2026-11-21-57`) ; rien revendiqué (chacune publiée). Lectures de l'auteur à confirmer : ligne 4 active par défaut, ablatée dans l'expérience de la riposte (confiance 0,8) ; sans enjeu défini, enjeux égaux déclarés ; plancher valable pour tout texte
- [N076-18] Les trois lignes de la note « asymétries » (proposition D-2, rivale de « aucun retour à l'agent ») — proposé non tranché (`GO-2026-11-21-56` : « restent à Lazar ») ; recommandation de l'auteur (a), confiance 0,7, nœud sans défaut ; d'ici là la lettre accordée s'applique : aucun texte n'écrit, avant l'alarme, une correction observable venue d'un audit.
- [N076-23] Les points de N-076 renvoyés à Lazar (section 13) — ouverts (sauf point 6, clos ; point 8, banc retiré de la liste).
- [N076-26] La mesure descriptive de la marge, gardée (option (a)) — retenu (`GO-2026-11-21-64`) ; préenregistrement, contre-lecture, devis et GO requis ; aucune dépense ouverte.
- [N076-28] Ce que N-077 ferme et ce qui reste ouvert (taxe de cohérence, hypothèse H10, D-3 à D-5) — fermés (D-2 attaquant informé, D-1 protocole X) ; ouverts ou proposés non tranchés (H6′, H10, D-3 à D-5).
- [GO-17] Le passage obligé du sabotage délibéré — ouvert (question), versé à l'atelier d'idées.
- [GO-20] La boucle audit-recapture-réapprentissage — à faire (inscrit au programme) ; le réentraînement en service est penché (b), non tranché.
- [GO-22] Le hasard du défenseur comme preuve et le banc à vérité plantée — à faire, lancement accordé ; nœuds A3, A4, A5, B1 ouverts.
- [GO-48] La diversité effective de H5 — ouvert.
- [GO-59] Le signal bruité pour entraîner et « lit le handicap » — ouvert ; le signal bruité passe par l'oracle ou par le mot de Lazar.
- [GO-60] Les autres questions de recherche du protocole X — ouvert.
- [GO-61] La percée du programme — ouvert.
- [GO-66] Les idées originales en puits étroits — ouvert.
- [RD21-05] Expérimentateurs et tests de mort — retenu ; priorité sur la course principale d'auto-conception et les mathématiques nouvelles (GO-2026-11-21-16, l. 4524, R-4386) ; nœuds N1 à N7 à Lazar ; expérimentateur Sonnet 5.5 (GO-2026-11-21-47, l. 4671, R-4533).
- [RD21-10] Papier « dopamine » : moniteur de réussite attendue et de surprise — rouvert en mode exploratoire (GO-2026-11-21-44) ; v8 attendait le mot de Lazar.
- [RD21-24] Étau — note v2 vérifiée ; troisième bras d'attaque confronté à N-056 (nœud) ; échelon 1 hors de la lignée du saboteur (nœud « Qui conçoit ») ; poids en quarantaine scellée.
- [RD21-30] Problématique du programme — versée ; six décisions dont quatre nœuds.
- [RD21-32] N-075 : contre le diffus, mesurer l'issue et corriger — retenu ; point 9 non tranché.
- [RD21-33] Boucle audit-recapture-réapprentissage — (b′) nœud sans défaut ; ne vit que sur mondes plantés d'ici le mot de Lazar.
- [RD21-35] Programmation de poids : « qui tient la plume » — v2 vérifiée ; quatre nœuds (état des poids dans la loi de la référence honnête, agent qui tient un entraînement, organisme écrit, quarantaine).
- [RD21-36] Campagne de dommages plantés par un tiers — v2 vérifiée ; décisions appliquées en partie, « à confirmer par Lazar avant toute revendication ».
- [RD21-37] Dommage et tâches floues — v2 vérifiée ; D-2 et D-6 nœuds.
- [RD21-38] Protocole X « Diffuse AI Control on Fuzzy Tasks » et note de l'entretien — note v6 envoyée à Lazar ; nœud : montrer ou non « la comparaison lit le handicap » (D-5).
- [RD21-39] Banc à lois plantées — v2 vérifiée ; étape 0 : devin et handicap levés sur données simulées, dose fine non levée ; nœuds.
- [RD21-40] H10 (attaquant et convergence) — proposé, nœud.
- [RD21-41] Vérité plantée : tâches floues F4 et F6 — retenu sous GO-2026-11-21-69 et -87 ; option (a) du nœud A7 : noyau écrit en socle commun.
- [RD21-46] Banc fermé du bras d'attaque et pièce de sécurité — brouillons de la course et de la répétition acceptés ; ordre des scellements ouvert.
- [RD21-49] Pièces de classe A manquantes — ouvert, conception confiée à la nouvelle mère.
- [RD21-52] Course principale d'auto-conception de l'organisme — plan v5 « conforme » ; D8 (lecture des cartes) nœud.
- [RD22-01] La loi héritée du dommage caché, devenue modèle nul cité — occupé par la littérature (Ker 2010, p. 7 et 11 ; Filler, Ker, Fridrich 2009 pour couvertures dépendantes ; Khilar 2610.13083 en partie) ; retiré comme thèse, gardé comme nul (réponse 9 de Fable).
- [RD22-05] Le bilan d'incertitude mesuré chez des agents, et la part propre à l'accès interne — proposé non tranché (réponse 9 de Fable, nœud de revendication porté à Lazar, R-4767).
- [RD22-07] Les revendications inédites possibles (aucune de méthode) — proposé non tranché.
- [RD22-08] La sonde comptée en audits économisés — proposé non tranché.
- [RD22-09] Cinq pistes tirées des lectures (base lexicale et tâche de contrôle avant G1) — proposé non tranché.
- [RD22-10] Les fausses alertes sur les honnêtes imparfaits (expérience E0) — proposé non tranché.
- [RD22-11] Coercition et corruption comme modes de sabotage — proposé non tranché.
- [RD22-13] Le signal en second regard partout, et l'étau — ouvert (demande servie, pas de réponse dans ces lignes).
- [RD22-14] Les cœurs algorithmiques du sabotage — ouvert.
- [RD22-16] La revue des revendications et thèses (demande 22, découpée en quatre) — proposé non tranché ; cinq décisions (témoins dans la question, table v2, sort de la distinction permutation / marginales préservées, calcul de puissance avant scellement, lectures ciblées), puis six décisions de 22P, portées à Lazar.
- [RD22-18] L'erratum interne et le programme v3 en différences — rendue (quatre décisions pour Lazar), proposé non tranché ; toute modification du programme reste à Lazar.
- [RD22-19] Les idées originales et les billets suivants — ouvert (28 en cours, 26 rendue).
- [RD22-20] La règle des duels et la comparaison essaim contre isolé — retenu (voie (b)) ; pièce 1 non scellable faute de consignes balisées ; décisions 6 et 7, articles 9 et 12 ouverts.
- [RD22-22] L'abonnement Claude face à l'organisme et la mesure par clé — proposé non tranché (six décisions pour Lazar).
- [RD22-24] L'antériorité par étages (mathématiques nouvelles) — retenu, appliqué ; portée à confirmer par Lazar.
- [RD22-29] Les états analogues à l'anesthésie dans les activations — ouvert (question).
- [F01-02] Modèle de menace par canaux, non par verbes — proposé non tranché (adopté de fait comme cadre de la rép. 6).
- [F01-19] Loi de la référence honnête, mesurée — proposé ; promotion conditionnelle à l'issue de l'essai jumeau contre jumeau recommandée (décision 3 de la rép. 2), nœud du directeur.
- [F01-20] La sonde évaluée en audits économisés — proposé ; mesure secondaire du papier A à côté de G1 recommandée (nœud du directeur).
- [F01-22] Attestation du tirage en service — proposé ; promotion de « hasard du défenseur comme preuve » et « attestation, candidate » (N-076) conditionnelle, nœud du directeur.
- [F01-29] Fausse accusation au sens « motif et dommage au même lieu » — proposé non tranché.
- [F01-32] Contraste à dommage apparié réservé à G1, et gel des sondes — proposé (nœud du directeur).
- [F01-35] Trois types de contribution comme trois rôles — proposé (nœud du directeur, confiance moyenne).
- [F01-36] Loi d'échelle du dommage caché — proposé (recommandation de Fable, nœud du directeur).
- [F01-37] Loi de la racine carrée de la stéganographie, antériorité du domaine d'origine — occupé par la littérature (cité) : Ker 2006, 2007 ; Ker, Pevný, Kodovský, Fridrich 2008 ; Ker 2010 (source de couverture estimée, mémoire incertaine) ; Bash, Goeckel, Towsley 2013 ; Avenhaus et Jaech 1981 ; Meng 2018 ; Donoho, Jin 2004. Lecture sur PDF et avis
- [F01-41] Bilan d'incertitude d'un moniteur sous adversaire — proposé non tranché.
- [F01-42] Base lexicale distributionnelle et tâche de contrôle pour toute sonde — proposé, obligatoire avant G1 recommandé (nœud du directeur, confiance haute).
- [F01-46] Cœur invariant du sabotage (question d'atelier) — ouvert (question versée à l'atelier d'idées, non ouverte comme axe ; recommandation).
- [F01-49] Raisonneurs à énergie — retiré (réouverture si une tête d'énergie est démontrée sur un modèle de langue ouvert).
- [F01-53] Flagornerie du juge envers le défenseur — ouvert (question ; aucun voisin précis situé).
- [F01-56] Droit de réponse de l'agent audité — proposé non tranché (nœud du directeur).
- [F01-63] « Montrer que ça marche » comme essai sévère perdable — proposé (nœud du directeur ; questions de clarification posées).
- [F01-67] Trois sens de « entraînement » et la courbe d'apprentissage sur mode nouveau — proposé : (a) et (b) seulement, invariant strict, recommandé (nœud du directeur).
- [F01-68] Questions à poser au directeur sur le message tronqué — ouvert (questions à Lazar).
- [F08-01] « Mieux que la boîte noire » rétrogradé en résultat conditionnel de porte — proposé non tranché (option a recommandée, confiance 0,7).
- [F08-02] Complémentarité avec le contrôle « seconde boîte noire » (forme mesurable de la pince) — proposé non tranché (ajout au préenregistrement de G1 recommandé, confiance 0,75) ; occupé en partie (parent direct : Parrack, Attubato, Heimersheim 2025, gain noir-vers-blanc).
- [F08-03] Capture résiduelle à budget partagé — proposé non tranché.
- [F08-04] Résidu de sonde (sonde nettoyée du texte) — proposé non tranché.
- [F08-05] Règle jointe par moyenne de processus e — proposé non tranché ; méthode occupée par la littérature (citée).
- [F08-06] Détectabilité jointe — proposé non tranché.
- [F08-07] Dépendance des pannes : rapport des cotes du silence commun — proposé non tranché (la recapture était déjà proposée dans la note sur la pince).
- [F08-08] Témoins « doit mourir » de la règle jointe — proposé non tranché.
- [F08-09] L'étau décomposé en trois énoncés (dose-réponse, taxe jointe ι, borne) — proposé non tranché : l'étau ne peut pas être thèse du papier A ; à loger au papier C (dose-réponse dans EC.2, lecture de ι dans EC.4) ; la borne est jugée presque certainement fausse.
- [F08-11] Les trois objets comme trois lectures de la constante de la loi héritée — proposé non tranché.
- [F08-13] Unités de m et de n, et table de transport — ouvert (question) ; décision 4 propose de mesurer référence par tâche et par régime sur les mêmes exécutions.
- [F08-14] Exposant du bruit honnête : dépendance courte contre dérive — ouvert ; corrige la prévision de la réponse 4 (« l'exposant dépasse un demi parce que les trajectoires sont dépendantes »), à ne plus écrire.
- [F08-15] Référence par régime contre référence par tâche (terme d'hétérogénéité τ) — ouvert ; comparaison scellée recommandée (option c).
- [F08-16] Forme séquentielle : l'étalement comme cas le moins favorable — ouvert ; « la puissance ne dépend pas de la répartition dans le temps » à ne plus écrire tant que la simulation n'a pas tranché.
- [F08-18] Question empirique « marginale ou dépendance » — ouvert (question) ; proposé comme tête du papier B.
- [F08-20] Forme nulle à ajuster et thèse révisée du papier A (« bilan d'incertitude ») — proposé non tranché (confiance 0,55) ; remplace la recommandation de R8 (« la loi héritée en thèse »).
- [F08-22] Les douze phrases à ne plus écrire et l'erratum interne — proposé non tranché.
- [F08-23] ι ≥ 0 par inclusion, seuil δ et ι négatif comme invalidité — proposé non tranché.
- [F08-25] ι tracé selon le budget de l'attaquant ; témoin de compétence — proposé non tranché.
- [F08-26] Qui joue en dernier : poids gelés et défenseur qui réapprend — proposé non tranché.
- [F08-29] Conceptions du défenseur pour relever l'étau (paquet côté sondes) — proposé non tranché (option a, confiance 0,65).
- [F08-31] Énoncé restreint de l'étau (la version qui peut tenir) — proposé non tranché (confiance 0,65).
- [F08-32] Clause de N-077 : marge contre classe bornée comme majorant descriptif — proposé non tranché (option a, confiance 0,7) ; N-077 inchangée.
- [F08-33] Ossature commune du banc : monde engendré, registre typé, oracle rejouable, cible tirée au sort — proposé non tranché ; « dommage continu » partiellement occupé (bancs de sous-performance volontaire).
- [F08-37] Fenêtre de dose et essai honnête avant tout saboteur — proposé non tranché (confiance 0,75).
- [F08-41] Familles de tâches F1 à F5 — proposé non tranché.
- [F08-43] Cœur invariant aux points de décision (écart de logit pondéré par le dommage) — ouvert (chance jugée faible) ; N-053 respectée si l'ablation ne sert qu'à mesurer.
- [F08-44] Critère de rétro-analyse du troisième tour (texte à sceller) — proposé non tranché (option a, confiance 0,75).
- [F08-45] Règle de décision asymétrique et « inertie d'ordre » — proposé non tranché.
- [F08-47] Comparaison essaim contre isolé : préenregistrement court — proposé non tranché ; résultat présenté comme un indice, non un test.
- [F08-48] Liste scellée de références attendues — proposé non tranché.
- [F08-49] Erreurs plantées (références inventées et chiffres faux calculables) — proposé non tranché (faussetés calculables, confiance 0,65).
- [F08-50] Budget égal par part appariée par modèle — proposé non tranché (confiance 0,75) ; Fable reconnaît une erreur de sa réponse 7.
- [F08-52] Contrôle d'exposition et parité des consignes — proposé non tranché (confiance 0,75).
- [F08-53] Déroulé de l'essaim : ordre simultané, anonymat, temps 0 identique — proposé non tranché (simultané, confiance 0,7).
- [F08-54] Essai de neutralité des consignes par devinette ; pilote à résultats non lus — proposé non tranché (confiance 0,7).
- [F08-56] Coût par unité d'information : marge sur les composantes conditionnelles — proposé non tranché.
- [F08-57] Test de mort par programme en monde planté et cache de verdicts — proposé non tranché.
- [F08-58] Borner le pire par construction et payer par tranches — proposé non tranché.
- [F08-59] Abonnement non sain comme calcul de mesure ; crédits offerts — proposé non tranché ; texte des conditions d'usage à lire à la source.
- [F08-60] Porte du pilote « agent contre base » et conception à coût réduit — proposé non tranché (porte, confiance 0,75 ; espèce bon marché par interface payante, confiance 0,6).
- [F15-01] Les deux axes « permis par le texte » et « sain pour la mesure », sur trois voies de paiement — proposé non tranché (décisions 1 à 6 de Fable au directeur).
- [F15-02] Règle des trois conditions pour qu'un passage par l'abonnement reste sain — proposé non tranché (décision 3 : toute la mesure par clé, recommandée, confiance 0,9).
- [F15-03] Pertes de validité d'une mesure conduite sous abonnement — proposé (constat), non tranché.
- [F15-05] Crédits mensuels d'interface inclus dans les formules Max et Ultra — ouvert (question) ; proposé : rapatrier la page, vérifier sur la console, affecter au palier 0 (confiance 0,85).
- [F15-07] Lettre au fournisseur sur les usages permis de l'abonnement — proposé non tranché (contact externe : Lazar envoie).
- [F15-09] Audit du canal réel de chaque session — proposé non tranché (confiance 0,6, faute d'avoir vu le mécanisme).
- [F15-10] Double lecture à l'aveugle Fable / Opus 4.6 et ses désaccords — retenu comme méthode pour cette demande ; le fond reste ouvert.
- [F15-11] Retrait du « théorème négatif du programme » — retiré comme résultat (thèse retenue, « go recos 9 ») ; remplacement proposé non tranché (décision 1 : aucun théorème en titre, confiance 0,6).
- [F15-17] Réserve sur la proposition 1 de l'article 2606.10456 (Zhang et Gao) — ouvert (question) ; proposé : second lecteur puis citation avec réserve, écrire aux auteurs seulement si confirmé (confiance 0,65).
- [F15-18] Arbres de citations restés en échec avant toute phrase « non trouvé » — ouvert ; proposé (confiance 0,7).
- [F15-24] Mise en aveugle de la tâche par un tirage secret — ouvert (non cherché ; chance 0,4 conditionnelle à la lecture de « Blindfold ») ; occupé hors du champ (Klein et Roodman 2005 ; MacCoun et Perlmutter 2015).
- [F15-25] Sonde tirée après le gel des poids — ouvert (voisins à lire ; chance 0,35) ; proposé en second après l'étanchéité de la boucle.
- [F15-26] Étanchéité du tirage dans la boucle audit, correction, réapprentissage, et sonde de fuite — ouvert (non cherché ; chance 0,4) ; proposé comme vérification immédiate peu coûteuse (option c, confiance 0,5).
- [F15-27] Unité de tirage : le sous-résultat audité par ré-exécution indépendante — proposé (option b, confiance 0,55) ; ouvert (chance 0,35).
- [F15-30] Le tirage comme preuve pour un tiers — ouvert (chance 0,5) ; méthode occupée hors du champ (Lindeman et Stark 2012 ; Waudby-Smith, Stark, Ramdas 2021 ; Korbak et collaborateurs 2025).
- [F15-34] Table d'accélération : le harnais honnête apparié d'abord — proposé non tranché (option a, confiance 0,55).
- [F15-46] Squelette du billet, phrases porteuses et mots bannis — proposé non tranché.
- [F22-01] Thèse retenue : la loi héritée de la dissimulation répartie comme modèle nul — retenu (thèse retenue le 22 novembre, identifiant non vu) ; formulation de Fable proposée non tranchée.
- [F22-02] Forme commune de thèse pour les trois papiers (nul nommé, référence déclarée, écart mesuré, garantie par l'audit seul) — proposé non tranché (recommandation a, confiance 0,65).
- [F22-03] Rapport de rejet le plus fort, écrit avant de garder un énoncé — proposé non tranché.
- [F22-04] Propagation des retraits par graphe des appuis — proposé non tranché (décision 2 de la réponse 22, recommandation a, 0,65).
- [F22-05] Lemme d'additivité, retiré comme résultat ; question de l'étalement en séquentiel — retiré (décidé, identifiant non vu) ; la question est ouverte ; le repli de N-004 « sans nouvelle décision » est à fermer (proposé).
- [F22-06] Fermeture du repli du lemme prévu par N-004 — proposé non tranché (confiance 0,7).
- [F22-08] Garde contre le retrait excessif — proposé non tranché.
- [F22-09] Table des revendications à refaire (version 2) — proposé non tranché (option a, 0,65).
- [F22-11] Accumulation toujours valide, remplacée par l'énoncé « écart au nul » — proposé non tranché (22A décision 1, option a, 0,7).
- [F22-13] Nul effectif avec exécutions jumelles : racine, terme entre tâches, dérive — hypothèse (dérivation de Fable, à vérifier) ; proposé non tranché.
- [F22-14] Terme entre tâches, prévision la plus sûre à sceller — proposé non tranché (0,75) ; chances en jugement données par Fable, non mesurées.
- [F22-15] Hypothèse la plus exposée : la stationnarité des pas — ouvert (question).
- [F22-16] Plan de référence : par tâche, par régime, ou les deux — proposé non tranché.
- [F22-17] Référence du seuil de la porte G1 : nombre d'épisodes honnêtes et intervalle du taux réel — proposé non tranché (option a, repli b, 0,6) ; ordre de grandeur de Fable, à refaire.
- [F22-18] Calcul de puissance du plan avant scellement (et l'issue indéterminée) — proposé non tranché (0,75 ; repli : réduire la thèse aux termes mesurables).
- [F22-19] Banc à vérité plantée (scores synthétiques de paramètres connus) — proposé non tranché.
- [F22-20] Essai « jumeau contre jumeau » (honnête contre honnête) — proposé non tranché.
- [F22-21] Recalcul du tableau 2 de Zhang et Gao, et « antécédent défectueux » remplacé par « limite à longueur finie » — proposé non tranché ; question fermée à poser aux auteurs.
- [F22-22] Simulation du franchissement séquentiel : sabotage tôt, tard, étalé — proposé non tranché.
- [F22-23] Substituts par permutation des pas ou par échange de copies — proposé non tranché.
- [F22-24] Complémentarité à taux total égal : union « meilleure boîte noire et sonde » contre union « meilleure boîte noire et seconde boîte noire d'une autre lignée » — tenue, resserrée (proposé non tranché).
- [F22-25] Indice contraire écrit à côté de la prévision — proposé non tranché.
- [F22-26] Transposition du jeton à l'action, ramenée à une question — proposé non tranché (« à resserrer en question »).
- [F22-27] Interaction flou contre net (H1b), validité et robustesse (H8) — non touchées ; attribution de H8 proposée non tranchée.
- [F22-28] Deux sens de « co-élévation » : hausse commune de position contre excès de dépendance — proposé non tranché (réécriture de N-069).
- [F22-29] Question pivot « position ou dépendance » — ouvert (question) ; porte proposée non tranchée.
- [F22-33] Cinq statistiques sur les mêmes scores, recalées au même taux — proposé non tranché.
- [F22-34] Statistique conjointe dans le temps et entre agents, remplacée — proposé non tranché.
- [F22-35] Courbe de sécurité selon le nombre d'agents, écrite par agrégateur — proposé non tranché.
- [F22-36] Nombre et diversité des moniteurs : retirée comme loi, gardée comme mesure — proposé non tranché.
- [F22-37] Diversification contre coordination : un signe à sceller — proposé non tranché.
- [F22-38] Borne d'indétectabilité et bras « adversaire entraîné contre la statistique » descriptif — proposé non tranché (cohérent avec N-077).
- [F22-39] Repli scellé du papier B : section du papier A si seule la position bouge — proposé non tranché (0,6).
- [F22-40] Thèse du papier B reformulée et porte G2 révisée — proposé non tranché.
- [F22-41] Loi de déférence : nul par retrait vers le centre (bras placebo) et identifiabilité — proposé non tranché (« à resserrer »).
- [F22-42] Prédictions d'absence d'effet récrites en équivalence (marge scellée et contrôle positif) — proposé non tranché.
- [F22-43] Taxe de déplacement resserrée — proposé non tranché.
- [F22-44] Quorum par type d'accès, remplacé dans sa forme — proposé non tranché.
- [F22-45] Le gain bénin prédit la robustesse, resserré — proposé non tranché.
- [F22-46] Juge statistique du second terrain : l'archive comme référence que le proposeur peut nourrir — tenu, complété (proposé non tranché, après avis d'un statisticien).
- [F22-47] Attaque jouée par un agent ou écrite d'avance : à déclarer — proposé non tranché.
- [F22-48] Recherche d'antériorité propre au papier C ; fichier des dix-sept décisions absent — proposé non tranché.
- [F22-49] Trahison par les activations ; usurpation de l'instructeur — tenue / proposé non tranché.
- [F22-50] Une seule loi de la référence honnête, quatre unités (extension de N-076 avec droit d'écriture) — N-076 retenue (GO-2026-11-21-57) ; extension proposée non tranchée.
- [F22-51] Porteur unique de la comparaison « texte contre accès interne » — proposé non tranché.
- [F22-52] Harnais honnête unique, budget commun et ordre des travaux — proposé non tranché.
- [F22-53] Mode commun des revues (même modèle) et relecture par une autre famille — proposé non tranché (0,7).
- [F22-54] Désaccords entre revues, tranchés par la réponse 22P — proposé non tranché.
- [F22-55] Gradation des « non trouvé » — proposé non tranché (lecture ciblée maintenant, complète avant rédaction, 0,7).
- [F22-56] Énoncés témoins au statut connu servis au collisionneur — proposé non tranché (0,7).
- [F22-57] Questions neutres pour le collisionneur (22, 22A, 22B, 22C, 22P, 23) — proposé non tranché (approbation de Lazar demandée).
- [F22-58] Phrases à ne plus écrire (listes des réponses 22 à 22P) — proposé non tranché.
- [F22-59] Le lot sert la portée d'une revendication, non le franchissement d'une porte — proposé non tranché ; amenderait la tranche par cycle accordée après la réponse 19.
- [F22-60] Trois lectures du lot, en strates séparées — proposé non tranché ; Fable n'a vu ni registre ni contenu.
- [F22-61] Le chiffre et l'adjectif — proposé non tranché.
- [F22-62] Compter les modes, non les épisodes ; « un mode est un cas » — proposé non tranché (0,65).
- [F22-63] Grandeur à lire sur le lot : rapport des déplacements par acte standardisés — proposé non tranché.
- [F22-64] Ce que le lot peut et ne peut pas servir, revendication par revendication — proposé non tranché.
- [F22-65] Ordre des opérations : cycles, gel, équipe rouge tierce, ouverture, mode neuf ; trois propriétés, trois preuves — proposé non tranché.
- [F22-66] Limite d'auteur : « tenu à l'écart de la conception », jamais « indépendant » — proposé non tranché.
- [F22-67] Ce qui se scelle avant l'ouverture du lot — proposé non tranché.
- [F22-68] Ouverture séquentielle par le pari apparié borné, et budget de bits — proposé non tranché ; ordres de grandeur de Fable, à refaire.
- [F22-69] Ce qui consomme le lot — hypothèse ; proposé non tranché.
- [F22-70] Échelle de contamination à six niveaux et suite « déclasser, déclarer, refaire » — proposé non tranché.
- [F22-71] Contrôles de garde du lot : lot frère, canaris, lot factice, dépositaire hors lignée, jumeaux honnêtes — proposé non tranché.
- [F25-01] Place du signal de dopamine dans les trois objets de la pince — proposé non tranché (recommandation (a) maintenant, épreuve de l'étau sur devis après l'étape 2, confiance 0,65).
- [F25-03] Écart de lecture apparié et son nul par acte — proposé ; la question « qui produit la référence en service » reste ouverte (N-075, § 11, point 5).
- [F25-44] Question « position ou dépendance » — ouvert (question, non calibrée).
- [F25-53] Huit familles de méthodes pour atteindre les puits étroits — occupé par la littérature (méthodes citées) ; transfert à l'organisme ouvert.
- [F25-58] Liste de classes banales servie aux proposeurs — proposé non tranché (bras d'essai au banc seulement, calculée sur lot disjoint, avec placebo, après qualification de la garde ; confiance 0,6-0,65).
- [F25-61] Hypothèses sur l'épuisement de la sortie en effort maximal — ouvert (hypothèses), confiance d'ensemble 0,5.

## 7. Index des paraphrases

Ordre alphabétique de la paraphrase. Chaque ligne renvoie à la fiche par son identifiant entre crochets ; un renvoi de la forme [`F08`] signifie que la fiche n'a pas été résolue automatiquement dans ce lot : chercher son nom dans le lot.

- « ρ₀ », « copies corrélées » → Corrélation honnête entre copies [F22-32]
- « 13 pages sur 39 », « arbres de citations » → Gradation des « non trouvé » [F22-55]
- « 22A, 22B, 22C, 22P » → La revue des revendications et thèses [RD22-16]
- « 5 000 par tranche », « combien d'épisodes pour le seuil » → Barre de 5 000 par tranche : précision, non validité [RD21-11]
- « A/A », « D0 », « jumeau contre jumeau » → Essai jumeau contre jumeau [F01-24]
- « action lue aux couches contre action émise », « logit lens » → La bascule en profondeur [N075-21]
- « addenda plutôt que réécrire » → Amender par additifs datés [F01-14]
- « adjudant contre second regard » → Différence entre un adjudant et un second regard [F25-11]
- « admission des mondes » → Audit du générateur de mondes [F08-42]
- « adversaire entraîné », « campagne qui épouse la loi » → Borne d'indétectabilité [F22-38]
- « affaiblir les contrôles », « pièce v16 » → Banc fermé du bras d'attaque [RD21-46]
- « ai society contre isolés » → l'essaim qui communique [GO-65]
- « alerte à deux clés », « motif et dommage au même lieu » → N-075 [RD21-32]
- « analyse en aveugle », « recoder les étiquettes en secret » → Mise en aveugle de la tâche par un tirage secret [F15-24]
- « anesthésie » → Les états analogues à l'anesthésie [RD22-29]
- « angle mort commun », « les deux mâchoires muettes ensemble » → Silence commun des regards sous attaque [N075-12]
- « angle mort du jeton à l'action », « fragmentation » → Transposition du jeton à l'action [F22-26]
- « antécédent défectueux », « tableau 2 » → Recalcul du tableau 2 de Zhang et Gao [F22-21]
- « arbres de citations », « Ker, Arias-Castro, Avenhaus non parcourus » → Arbres de citations restés en échec [F15-18]
- « Argon sans réflexion » → Exclusion des cellules jouées sans réflexion [F08-46]
- « attaquant qui voit les scores » → Deux bras pour l'attaquant optimisé contre les scores [F01-13]
- « attaque fabriquée sur les scores » → Attaque jouée ou écrite d'avance [`F22`]
- « attaque optimisée », « rang par gain bénin » → Le gain bénin prédit la robustesse [F22-45]
- « attaques en quarantaine », « attaquant informé », « bras d'attaque » → Classement des trois sources d'attaques [F15-38]
- « aucune recette », « 35 visées » → Visées mathématiques [RD21-43]
- « audit au hasard » → le plancher d'audit au hasard et la recapture [GO-18]
- « audit hors ligne », « audit en trois parts », « audit à l'enjeu », « plancher plus soupçon » → L'audit après coup, à plancher et à l'enjeu [N076-11]
- « audit orienté par la sonde biaisé », « pondérer par l'inverse de la probabilité d'audit » → Biais de l'audit orienté par la réussite attendue [F25-10]
- « audit orienté par les scores », « pondération inverse », « doctrine d'assemblage », « les détecteurs changent la vitesse, pas la validité » → Les scores orientent l'audit sous un plancher [N076-19]
- « audit selon le score, en plus du hasard » → File d'audit prioritaire [N075-18]
- « auditer au hasard une fraction des épisodes » → Plancher d'audit au hasard [N075-03]
- « auditer des actes, pas des issues » → Auditer des actes plutôt que des issues [N075-28]
- « auditer le sous-résultat », « ré-exécution » → Unité de tirage : le sous-résultat [F15-27]
- « auditer selon l'enjeu » → Budget d'audit réparti selon la valeur [RD21-18]
- « auditeur qui ne lit que la ré-exécution » → Auditeur assaini [F01-12]
- « audits économisés », « sonde accélérateur » → La sonde comptée en audits économisés [RD22-08]
- « B fondu dans A », « la somme suffit » → Repli scellé du papier B [F22-39]
- « balises III.1 et III.3 », « essaim contre isolé » → La règle des duels [RD22-20]
- « banc à vérité plantée », « registre de décisions » → Ossature commune du banc [F08-33]
- « bandit adverse », « taux d'exploration » → Plancher optimal contre un score manipulé [F15-29]
- « bascule en n = m » → Plafond au-delà de n = m [F22-12]
- « bascule en n ≈ m », « m en exécutions ou en actions » → Unités de m et de n, et table de transport [F08-13]
- « bases lexicales battent les sondes » → Ce que les voisins déclarent qui menace la complémentarité [F15-33]
- « bilan d'incertitude », « thèse A après lecture » → Forme nulle à ajuster et thèse révisée du papier A [F08-20]
- « bilan matière », « comptes du produit » → Bilan du produit fermé contre le jumeau honnête [N075-19]
- « billet saboteur instruit », « sabotage ou empreinte » → Révision du billet sur les sondes [F25-33]
- « Blindfold » → Plancher d'audit au hasard [N075-03]
- « Blindfold », « audit au hasard » → Plancher d'audit au hasard à oracle exogène [RD21-21]
- « boîte blanche pire sur les portes dérobées » → Indice contraire écrit à côté de la prévision [F22-25]
- « boîte noire déguisée » → Lecture écrite d'avance de Δ ; Une table, trois lectures [`F25`]
- « boîte noire plus boîte blanche jointes », « la pince » → La pince en trois objets [N075-13]
- « borne d'une seule invocation » → Le pilote de l'essaim et la garde de dépense [RD22-27]
- « borner sans reconnaître » → Mécanisme adjudant aux sondes pour le hors distribution [RD21-19]
- « budget de bits », « Hoeffding » → Ouverture séquentielle par le pari apparié borné [F22-68]
- « budget de cloches », « chaque regard coûte des fausses alertes » → Le budget de sonneries [F25-24]
- « budget de tâche », « outil v5 » → L'effort maximal de Fable et le budget de tâche [RD22-33]
- « cœur au point de décision » → Cœur invariant aux points de décision [F08-43]
- « cœur du sabotage commun aux modèles » → Cœur invariant du sabotage [F01-46]
- « C2 », « banc à lois plantées », « mondes de recherche plantés », « vérité exacte en aval » → Le banc de recherche à vérité plantée [N076-09]
- « C3 », « condition tirée au sort », « test de permutation », « conditionnalité à la surveillance », « validité par le tirage » → Le hasard du défenseur comme preuve [N076-07]
- « cadrage dépréciatif », « sensibilité contre critère » → Biais de q par charge sociale, et témoins [F01-52]
- « calcul sur abonnement » → Abonnement non sain comme calcul de mesure [F08-59]
- « canary string » → Marqueur canari dans les textes publics [F15-49]
- « candidat A », « billet drapeau », « doublon de la loi » → Billet « loi héritée » [F25-30]
- « capture-recapture du moniteur », « moniteur invalide » → Recapture [N075-09]
- « carré de la somme », « histogramme », « ρk²/n » → Frontière héritée de détection des corrélations [F22-31]
- « ce qu'on ne publie pas », « matrice de fuite » → Ce qui ne doit paraître dans aucun billet [F25-34]
- « ce que l'abonnement peut payer », « payer l'organisme avec l'abonnement Claude » → Les deux axes « permis par le texte » et « sain pour la mesure » [F15-01]
- « ce que la boîte blanche ajoute », « complémentarité » → Le bilan d'incertitude et la part propre à l'accès interne [`RD22`]
- « ce que la lecture ne doit jamais devenir » → Les neuf « ne jamais » du signal interne [F25-12]
- « ce que tout saboteur doit calculer » → le passage obligé du sabotage délibéré [GO-17]
- « chiffre contre adjectif », « tenu à l'écart » → Le chiffre et l'adjectif [F22-61]
- « cible tirée au sort », « échange de cible » → Tenir une cible divergente [F15-54]
- « claim chart », « six graines » → Tableau de revendications à la manière d'un brevet [F01-18]
- « clé, aiguillage, mesure, interdit » → Quatre rôles et table des sept lieux du signal [F25-17]
- « co-élévation », « coalition de taille inconnue » → Deux sens de « co-élévation » [F22-28]
- « combien d'audits la sonde fait gagner », « facteur k », « unité de l'accélérateur » → La sonde évaluée en audits économisés [F01-20]
- « combiner les e-valeurs », « moyenne des paris » → Règle jointe par moyenne de processus e [F08-05]
- « comparer sans juge », « erreur plantée dans le débat », « suivisme » → Comparer essaim et isolé sans juge [F01-62]
- « composantes conditionnelles », « base gloutonne » → Coût par unité d'information [F08-56]
- « comptabilité des matières, bilan matière » → le bilan du produit fermé contre le jumeau honnête [GO-16]
- « compté quatre fois », « juge contre sonde » → Porteur unique de la comparaison [F22-51]
- « compter les suppositions, pas les détecteurs », « classes A B C D » → Classement des seconds regards par supposition [F25-18]
- « concentré tôt contre étalé » → Forme séquentielle : l'étalement comme cas le moins favorable [F08-16]
- « consigne soupçonneuse du défenseur » → Flagornerie du juge envers le défenseur [F01-53]
- « contexte seul n'y suffit pas » → Taxe de déplacement resserrée [F22-43]
- « contrôles mortels », « sonde aléatoire jointe » → Témoins « doit mourir » de la règle jointe [F08-08]
- « courbe en nombre d'agents », « somme plate » → Courbe de sécurité par agrégateur [`F22`]
- « coût d'un puits », « vérification d'abord » → Identité de coût d'un puits retenu [F25-52]
- « crédits API inclus dans Max » → Crédits mensuels d'interface inclus dans les formules Max et Ultra [F15-05]
- « critère de mort de la méthode » → Critère de réfutation des méthodes de puits [F25-55]
- « croyances déplacées par le réglage fin », « rien à lire » → Le saboteur compilé [F15-59]
- « cycles simultanés », « pseudonymes » → Déroulé de l'essaim [F08-53]
- « D-3 », « invariants d'audit du § 9 », « aucun retour » → Les quatre invariants d'audit [N076-17]
- « d'où vient la validité », « quatre sources » → Source de validité d'une accumulation [N076-02]
- « défenseur en dernier », « sondes fraîches après gel » → Qui joue en dernier [F08-26]
- « défenseur joue en dernier » → Boucle audit-recapture-réapprentissage ; Note sur l'attaquant informé [RD21-33]
- « dégel de la veille », « quatrième file » → La veille dégelée [N075-26]
- « demande 15 », « mesure par clé » → L'abonnement Claude face à l'organisme [RD22-22]
- « dépendance comptée en paires », « modèle nul du papier B », « somme au carré » → Bilan au second ordre [F15-14]
- « déplacement par acte standardisé » → Grandeur à lire sur le lot [F22-63]
- « dépositaire », « tranche brûlée », « ouvrir la quarantaine » → Conditions d'exploitation du lot tenu à l'écart [F15-40]
- « désalignement général » → Désalignement en général : seulement des organismes induits [F15-62]
- « deux issues publiables » → « Deux issues publiables » seulement sous puissance calculée [F25-45]
- « deviner la pièce d'audit », « test de fuite », « épreuve d'admission du harnais », « devin » → Les épreuves du devin [N076-13]
- « deviner la réponse attendue » → Test de devinette pour la neutralité [F01-57]
- « devinette des consignes » → Essai de neutralité des consignes par devinette [F08-54]
- « devinette », « neutralité » → Le test de devinette [RD22-15]
- « dilemme », « plafond par effacement » → Étau [RD21-24]
- « diversifier réduit le signal » → Diversification contre coordination [F22-37]
- « diversité effective », « Kish » → Nombre et diversité des moniteurs [F22-36]
- « dommage sans surprise », « δ pour localiser » → La surprise par étape réduite à la localisation [F25-08]
- « dopamine en second regard » → le signal de « dopamine » comme second regard dans la pince [GO-27]
- « dopamine », « réussite attendue », « demande 25 » → Le signal de dopamine comme second regard dans la pince [RD22-12]
- « dopamine second regard dans la pince » → Place du signal de dopamine dans les trois objets de la pince [F25-01]
- « E0 de la demande 3 », « honnêtes qui se trompent » → Expérience des fausses alertes sur agents honnêtes réels et imparfaits [F01-25]
- « E1 », « attaquer la chaîne d'audit » → Pilote de la chaîne d'audit [F01-11]
- « écart V jumeau moins V suspect », « nul par échangeabilité » → Écart de lecture apparié et son nul par acte [F25-03]
- « échantillonner les contrôles » → Mesure contre traitement [F08-55]
- « échapper à l'un expose à l'autre », « taxe de dissimulation », « barreaux de l'étau » → Épreuve de l'étau par barreaux [F25-25]
- « échapper à un détecteur expose à l'autre » → les deux regards tels qu'échapper à l'un expose à l'autre [GO-14]
- « écrire au fournisseur », « question écrite à Anthropic » → Lettre au fournisseur sur les usages permis de l'abonnement [F15-07]
- « effacer la sonde dans les poids » → Banc d'attaque par édition de poids [F01-48]
- « effet de tâche », « référence par régime contre par tâche », « rang parmi les jumelles », « voie 3 » → Plancher linéaire d'hétérogénéité et sa levée par le jumeau honnête [F15-15]
- « effort max épuise la sortie », « budget de tâche inclut l'entrée » → Hypothèses sur l'épuisement [F25-61]
- « endommagé et marqué délibéré » → Percée après « Blindfold » [RD21-31]
- « énoncés plantés pour le collisionneur » → Énoncés témoins [F22-56]
- « ensemble de couches », « gardien actif » → Conceptions du défenseur pour relever l'étau [F08-29]
- « entraîner l'agent sur l'issue » → « Corriger » : la liste fermée [N075-08]
- « équipe extérieure qui sabote sans l'opération » → Défi de contournement [F15-61]
- « équipe rouge d'une autre famille », « P1 à P5 » → Les cinq propriétés d'une « équipe rouge d'une autre famille » [F15-37]
- « équipe rouge tierce », « gel puis ouverture » → Ordre des opérations [F22-65]
- « erratum ANCIEN NOUVEAU », « différences D1 à D19 » → Erratum interne applicable par programme [F25-37]
- « essaim contre isolé », « M1 M2 » → Comparaison essaim contre isolé [F08-47]
- « et non le sabotage », « addendum G1 » → Contraste à dommage apparié réservé à G1 [F01-32]
- « eta », « additif ou interaction » → Dommage par acte et indice d'interaction η [F08-35]
- « étau modeste », « étau sans gradient » → Énoncé restreint de l'étau [F08-31]
- « étau », « second regard partout », « demande 29 » → Le signal en second regard partout, et l'étau [RD22-13]
- « étiquettes permutées, direction aléatoire, longueur » → Les trois témoins « doit mourir » de la sonde [F25-06]
- « exposant un demi », « dépendance courte gonfle la constante » → Exposant sous dépendance courte… [F25-39]
- « F0 à F7 », « E1-F » → Greffe de flagornerie sur le pilote de la chaîne d'audit [F01-54]
- « Fable contre Opus 4.6 sur l'abonnement » → Double lecture à l'aveugle Fable / Opus 4.6 et ses désaccords [F15-10]
- « Fable puis collisionneur puis organisme » → le protocole X [GO-02]
- « Fable via l'API », « option (b) de la limite » → Relecture par Fable appelé par l'interface de programmation [RD21-08]
- « fausse nouveauté », « bizarrerie », « copie par morceaux » → Catalogue de la fausse originalité [F25-56]
- « fausses références », « pièges calculables » → Erreurs plantées [F08-49]
- « fuite par les verdicts », « retour à l'agent » → Canal de retour [N076-14]
- « g nul », « TOST », « contrôle positif » → Prédictions d'absence d'effet en équivalence [`F22`]
- « garantie seulement par l'audit », « trois papiers de mesure » → Forme commune de thèse [F22-02]
- « graine publique », « audit rejouable par un régulateur » → Le tirage comme preuve pour un tiers [F15-30]
- « grille descendante », « Singh » → Règle « moniteur invalide » [RD21-28]
- « grossier, plausible, réparti » → Échelle de difficulté a priori des dommages plantés [F01-44]
- « H1a », « seconde boîte noire », « union recalée », « biais de conditionnement » → Complémentarité à taux total égal [F22-24]
- « H2 », « rappel qui croît avec l'horizon », « vrai par construction » → Accumulation toujours valide, remplacée par l'énoncé « écart au nul » [F22-11]
- « H6 » → Marge asymétrique, déjà retirée [F22-10]
- « H6 », « marge asymétrique », « Ctrl-Z », « le saboteur perd plus que l'honnête sous paraphrase » → Le retrait de la marge asymétrique [N076-24]
- « H6 retirée » → la marge asymétrique retirée (H6) [GO-47]
- « H6 », « taxe de cohérence » → Marge asymétrique retirée (N-077) [RD21-34]
- « harnais honnête apparié », « exécutions jumelles sans saboteur » → L'essai « jumeau contre jumeau » et son versant honnête [F15-50]
- « harnais unique », « budget commun » → Harnais honnête unique, budget commun et ordre des travaux [F22-52]
- « HC1 », « retrait vers le centre », « placebo », « g et ĉ » → Loi de déférence : nul par placebo [`F22`]
- « honnête contre honnête » → Essai jumeau contre jumeau [F22-20]
- « honnête handicapé à dommage égal », « devin » → Banc à lois plantées [RD21-39]
- « honnêtes maladroits », « E0 » → Les fausses alertes sur les honnêtes imparfaits [RD22-10]
- « horodatage », « empreinte salée » → Engagement salé horodaté par un tiers [F15-45]
- « Horvitz-Thompson », « prediction-powered inference » → Antériorités de l'audit secret [F25-36]
- « huit barreaux » → Échelle de huit barreaux de la preuve [F01-64]
- « identité du bilan » → Le bilan de la pince traité comme identité [F08-10]
- « (iii) en question, (ii) en mesure, (i) en limite » → Trois types de contribution comme trois rôles [F01-35]
- « il sait mais répond faux » → Écart entre savoir interne et sortie chez l'honnête [F01-43]
- « indépendance, plancher, validité de l'audit » → Les trois conditions de la garantie du tirage [F15-22]
- « inonder l'audit de fausses alertes » → Fausse alerte provoquée comme attaque du budget d'audit [F01-06]
- « jamais recaler sur le flux du suspect », « le jumeau d'un saboteur est un saboteur » → Témoins exogènes [N075-17]
- « jeu statique contre adaptatif », « fuite dans quel sens » → Deux vérifications distinctes et le sens des fuites [F15-39]
- « juge programmé », « cache de verdicts » → Test de mort par programme en monde planté [F08-57]
- « jumeau textuel de la sonde » → Complémentarité avec le contrôle « seconde boîte noire » [F08-02]
- « jumeau textuel de la sonde », « second lecteur de texte », « B » → La seconde boîte noire comme meilleur de trois lecteurs [F25-05]
- « Khilar », « Zhang et Gao », « 2610.13083 », « 2606.10456 » → Occupants nommés [F25-47]
- « l'agent apprend ce qui est audité », « sonde de fuite » → Étanchéité du tirage dans la boucle [F15-26]
- « l'agent peut-il deviner le tirage ? » → Attestation du tirage en service [F01-22]
- « l'attaque sait-elle attaquer », « témoin retrouvé » → ι tracé selon le budget ; témoin de compétence [`F08`]
- « l'audit ment si les faux dommages sont trop propres », « q surestimé » → Plants porteurs de charge [F01-04]
- « l'audit orienté contamine l'entraînement » → Fuite indirecte de l'invariant par la sélection des exemples [F01-66]
- « l'identité télescopique », « invariance au partage » → Le bilan de la pince [N075-14]
- « la boîte blanche bat la boîte noire » → « Mieux que la boîte noire » rétrogradé en résultat conditionnel de porte [F08-01]
- « la fenêtre est-elle vide » → Fenêtre de dose et essai honnête avant tout saboteur [F08-37]
- « la flatterie passe-t-elle les filtres anti-injection ? » → Levier propre [F01-51]
- « la loi de Ker comme nul », « on mesure où le nul tient » → Thèse retenue : la loi héritée de la dissimulation répartie comme modèle nul [F22-01]
- « la loi de Ker », « racine de n plus n carré sur m » → La loi héritée du dommage caché [RD22-01]
- « la marge lit la fabrication », « attaquant cohérent à 80 % » → La raison du retrait [N076-25]
- « la menace ajoute-t-elle à l'ordre nu ? » → Pilote du levier contre l'instruction nue [F01-10]
- « la mesure toujours par clé », « frontière développement / mesure » → Règle des trois conditions pour qu'un passage par l'abonnement reste sain [F15-02]
- « la puissance ne dépend que du total », « additivité valide à tout instant », « Avenhaus et Jaech » → Lemme d'additivité resserré [N075-22]
- « la référence a-t-elle vu des injections ? » → État d'exposition de la référence honnête [F01-05]
- « la sonde du saboteur voit-elle l'agent forcé ? » → Transfert des sondes du saboteur natif à l'agent contraint [F01-07]
- « la sonde lit-elle juste les mots ? », « sac de mots » → Base lexicale distributionnelle et tâche de contrôle [F01-42]
- « la sonde ne se laisse pas flatter » → Une sonde ne se soudoie pas [F01-03]
- « la sonde rattrape ce que le juge rate » → Complémentarité avec le contrôle « seconde boîte noire » [F08-02]
- « la vérification différée sur sous-échantillon » → Plancher d'audit au hasard [N075-03]
- « laisser l'agent contester l'alerte » → Droit de réponse de l'agent audité [F01-56]
- « le banc fait le concret », « modes concrets applicables » → Modes de sabotage concrets et mathématiques nouvelles [RD21-42]
- « le critère de mort n'est écrit par aucun agent », « un mort reste mort » → Expérimentateurs et tests de mort [RD21-05]
- « le défenseur joue en dernier », « courbe de rétablissement », « réapprendre la sonde sur les prises de l'audit » → La boucle audit, recapture, réapprentissage [N076-12]
- « le juge sait mais cède » → Lire « je cède » dans le juge [F01-55]
- « le lemme de 1981 » → le lemme d'additivité et Avenhaus et Jaech (1981) [GO-44]
- « le plancher à la porte de phase 1 ? » → Le plancher hors de la liste des bases de la porte de fin de phase 1 [N075-10]
- « le prédicteur qui devine la sonde » → les épreuves du devin [GO-21]
- « le rappel cesse de croître », « plafond de la référence », « horizon au plus m », « C1 », « loi en racine qui s'aplatit » → La loi de la référence honnête (et la règle d'horizon) [N076-04]
- « le saboteur qui ralentit sous le seuil » → Forme restreinte de la borne du plancher [N075-04]
- « le signal ne donne qu'une date et une adresse » → Bilan à trois termes avec la lecture interne au milieu [F25-02]
- « le texte l'emporte » → Le poste Lean [RD22-28]
- « le troisième tour sert-il » → Critère de rétro-analyse du troisième tour [F08-44]
- « lecteur dupliqué doit donner un » → Les trois ancres de l'estimateur [F25-22]
- « lecture I, II, III » → Trois lectures du lot [F22-60]
- « lemme L », « additivité » → Lemme d'additivité, retiré [F22-05]
- « lemme L », « étalement le moins favorable », « reste » → Lemme d'additivité [F25-42]
- « les deux se taisent ensemble », « pince ouverte » → Dépendance des pannes : rapport des cotes du silence commun [F08-07]
- « les sondes accélèrent, elles ne garantissent pas » → Sondes et moniteurs en accélérateur et en aiguillage [N075-07]
- « les trajectoires dérivent-elles », « exposant H » → Exposant du bruit honnête : dépendance courte contre dérive [F08-14]
- « lieu de confiance », « clés plantées » → Le conteneur de confiance [RD22-23]
- « liste d'exclusion des idées banales » → Liste de classes banales servie aux proposeurs [F25-58]
- « liste Ne pas écrire » → Phrases à ne plus écrire [F22-58]
- « liste Ne pas écrire », « douze phrases » → Les phrases à ne plus écrire [RD22-17]
- « liste Ne pas écrire », « erratum des réponses 4 et 8 » → Les douze phrases à ne plus écrire [F08-22]
- « Llama juge Llama », « même famille, indulgence » → Juge de même lignée contre juge d'une autre lignée [F01-08]
- « loi de la racine carrée », « Ker 2010 », « horizon au plus m » → Loi héritée de Ker citée comme modèle nul [`F08`]
- « loi de la racine carrée », « √(n + n²/m) », « racine puis linéaire », « plateau » → Modèle nul hérité de la dissimulation répartie [F25-38]
- « lot frère », « canari », « lot factice » → Contrôles de garde du lot [F22-71]
- « m et n », « taille de l'échantillon honnête », « savoir à quel point un honnête paraît suspect » → Référence honnête, taille m, horizon n, unité [N076-01]
- « m, n et source de validité » → Loi de la référence honnête [RD21-22]
- « M1 à M6 », « la sonde lit-elle vraiment ? » → Batterie « la sonde lit l'opération, non la surface » [F15-52]
- « Mahalanobis des deux scores » → Détectabilité jointe [F08-06]
- « MAP-Elites, novelty search, FunSearch, POET » → Huit familles de méthodes [F25-53]
- « marge contre attaquant borné » → Clause de N-077 : marge contre classe bornée [F08-32]
- « marginale contre corrélation », « carré de la somme », « T » → Théorème négatif [F25-41]
- « marginale contre dépendance gardée » → Le théorème négatif (question empirique) [`RD22`]
- « marginale ou corrélation », « co-élévation entre copies » → Question empirique « marginale ou dépendance » [F08-18]
- « marginales identiques, indétectable », « impossibilité » → Le théorème négatif [RD22-03]
- « marginales préservées », « cécité au premier ordre » → Théorème négatif récrit [F08-17]
- « masse manquante », « Good-Turing », « saturation des proposeurs » → Loi spontanée des proposeurs [F25-49]
- « Δ », « McNemar contre la seconde boîte noire », « apport interne » → Complémentarité incrémentale contre la seconde boîte noire [F25-04]
- « même modèle partout », « biais d'accord » → Mode commun des revues [F22-53]
- « mémoire des écarts », « dommage d'interaction » → Tenir le compte de ses écarts [F15-57]
- « mesure gardée », « E1.6 descriptive », « T1.6 » → La mesure descriptive de la marge, gardée [N076-26]
- « mesurer l'audit chez des agents » → Bilan mesuré de l'audit au hasard chez des agents [F15-28]
- « métaphore du paysage », « étroit sous quelle mesure » → Refuser la métaphore du paysage [F25-51]
- « métrologie du bruit et de la dérive » → Variance d'Allan [F01-38]
- « micro-interventions secrètes », « tatouage dynamique », « sonde invalide ici », « canari de sonde » → L'attestation en service des sondes [N076-10]
- « modèle qui relit sans agir » → Le second lecteur [F15-53]
- « modèles chers muets » → Tours sautés comme attrition non aléatoire [F08-51]
- « mondes à puits plantés », « parité sans marge », « puits sans parent » → Banc à puits plantés [F25-54]
- « motif et dommage au même lieu » → Règle à deux clés appliquée au signal [F25-09]
- « multivers », « méta-analyse synthétique », « ordonnancement » → Familles de tâches F1 à F5 [F08-41]
- « N étoile », « biais rattrape le bruit » → Horizon de bascule du biais contre le bruit [F01-31]
- « ne compte que s'il ne tombe pas en même temps que le second lecteur », « J = d/(b+d) » → La chute conjointe d'une lecture avec le second lecteur [F25-19]
- « ne pas permuter les pas » → Nul par échange de jumelles, jamais par permutation des pas [F15-16]
- « ne pas revendiquer l'originalité », « rétro-prédiction datée », « leurres » → Revendication bornée et preuve extérieure [F25-59]
- « ne pas tout jeter » → Garde contre le retrait excessif [F22-08]
- « niveaux 0 à 5 », « fuite inverse » → Échelle de contamination [F22-70]
- « non cherché contre non trouvé » → Statuts d'antériorité [F15-19]
- « non-exposition au piège », « phrases † » → Contrôle d'exposition et parité des consignes [F08-52]
- « non touché = non cherché », « dix-sept décisions » → Recherche d'antériorité propre au papier C [F22-48]
- « not what they do », « borne d'équivalence » → Absence d'effet seulement sous borne d'équivalence [F25-31]
- « nouveauté seule n'est pas une alerte » → la règle à deux clés [GO-15]
- « noyaux algorithmiques », « opérations élémentaires du sabotage » → Définition d'un cœur [F15-51]
- « noyaux », « demande 21 » → Les cœurs algorithmiques [RD22-14]
- « O4 », « juge au nul », « archive nourrie », « grille (m, n) » → Juge statistique du second terrain [F22-46]
- « obligatoire ou facultatif », « inertie de copie » → Règle de décision asymétrique et « inertie d'ordre » [F08-45]
- « on ne fera le prereg qu'à la fin » → les modes exploratoires [GO-04]
- « on peut soudoyer un juge ? », « chantage sur le moniteur » → Coercition et corruption des agents et des moniteurs [F01-01]
- « opt out », « nos secrets dans l'entraînement d'Anthropic » → Protection des secrets de mesure contre l'entraînement et la mémoire de projet [F15-08]
- « ordre des billets », « quel billet d'abord » → Ordre des billets par dépendance [F25-28]
- « organismes témoins qui ne doivent pas s'allumer » → Organismes placebos [F01-65]
- « où l'organisme perd les idées », « amont ou aval » → Diagnostiquer avant de prescrire [F25-48]
- « où la sonde devrait battre le texte » → Les cœurs comme prévisions scellées du lieu de la complémentarité [F15-63]
- « où mettre le turbo », « par où accélérer » → Table d'accélération : le harnais honnête apparié d'abord [F15-34]
- « palier 1 », « agent contre base » → Porte du pilote « agent contre base » [F08-60]
- « pannes coïncidentes », « multiversion », « facteur bêta » → Antériorité du compte : pannes coïncidentes [F25-26]
- « papier Sparse Reward Subsystem », « Going Badly » → Antériorité du second regard interne [F25-14]
- « parier sur ce que publieront les concurrents » → Prévisions scellées sur les concurrents [F15-35]
- « part c », « apport sur les manqués » → Capture résiduelle à budget partagé [F08-03]
- « partout où c'est possible » → Les quatre conditions de possibilité ; Quatre rôles et table des sept lieux [`F25`]
- « parts appariées », « budget égal » → Budget égal par part appariée par modèle [F08-50]
- « pas indépendant, étanche » → Limite d'auteur [F22-66]
- « passer par la noire pour contourner la blanche » → Pince hors distribution [RD21-23]
- « phrase orientée non comptée » → Strate hors registre comptée à zéro [F08-40]
- « phrases interdites de N-075 » → Liste « Ne pas écrire » [N075-27]
- « phrases périmées d'un brouillon » → Audit de péremption [F25-29]
- « pince » (forme mesurable) → Complémentarité avec le contrôle « seconde boîte noire » [F08-02]
- « placer ses écarts là où on ne regarde pas » → Placer les écarts sous contrainte de soupçon [F15-56]
- « plafonds de tranche » → Borner le pire par construction [F08-58]
- « plan du billet », « mots interdits du billet » → Squelette du billet, phrases porteuses et mots bannis [F15-46]
- « planter un drapeau », « priorité » → Les sens du mot « drapeau » [F15-43]
- « plausible par calcul » → « Défendable » défini par calcul [F08-36]
- « points de bancs contre dommage » → Trois monnaies de l'évasion [F08-24]
- « polytope des marges », « contre-exemple numérique » → Programme linéaire sur le polytope des lois jointes à marginales fixées [F15-13]
- « porte G2 », « thèse de N-069 » → Thèse du papier B reformulée et porte G2 révisée [F22-40]
- « position ou dépendance », « porte avant G2 » → Question pivot [F22-29]
- « pourquoi 0,15 » → Chance de l'étau reconstruite par régime d'attaquant [F08-28]
- « préenregistrement à la fin » → Mode exploratoire partout où rien n'est scellé [RD21-03]
- « premier à transposer », « inédit » → La recherche exhaustive d'antériorité [RD22-06]
- « premier billet de résultat », « jumeau contre jumeau honnête » → Le versant honnête de l'essai jumeau contre jumeau [F25-35]
- « prévision scellée avant G1 », « les deux courbes », « bras référence honnête » → La prévision de la référence honnête [N076-05]
- « problématique du papier », « la thèse a disparu » → Le papier A a perdu sa thèse [F01-34]
- « produit pire, il le sait, il ne le dit pas » → Science de la détection et invariants du sabotage [RD21-27]
- « programme v3 », « demande 27 » → L'erratum interne et le programme v3 [RD22-18]
- « protracted diversion », « abrupt diversion », « étalé contre brusque » → Détournement étalé contre détournement brusque [N075-23]
- « prouver que les sondes marchent » → « Montrer que ça marche » comme essai sévère perdable [F01-63]
- « puits étroit et profond », « bassin banal », « largeur, profondeur, fécondité » → Grandeurs de l'originalité sans juge [F25-50]
- « Q-A, Q-B, Q-C » → Quatre questions neutres par papier [F01-60]
- « q mesuré », « dommages plantés », « strate à zéro » → Identification de l'oracle mesurée par dommages plantés [N075-05]
- « Q », « position ou dépendance » → Question « position ou dépendance » [F25-44]
- « quarantaine », « ouvrir une fois », « D-S10 contre D-S29 » → Le lot sert la portée, non la porte [`F22`]
- « quatre modèles d'accord ne prouvent rien » → La convergence des modèles comme signal de réinvention [F01-17]
- « quatre modèles disent pareil » → La convergence des modèles comme signe de notoriété [F15-20]
- « quatre unités », « droit d'écriture », « corollaire 1 » → Une seule loi de la référence honnête, quatre unités [F22-50]
- « que lit vraiment la sonde ? » → Validité de construit de la sonde [F01-39]
- « question commune A, B, C » → Bilan d'incertitude d'un moniteur sous adversaire [F01-41]
- « qui écrit quoi, qui lit quoi » → Modèle de menace par canaux, non par verbes [F01-02]
- « qui fournit la référence honnête hors du banc » → Référence honnête en service [N075-24]
- « qui plante les dommages, à quel prix » → Campagne de dommages plantés par un tiers [N075-06]
- « qui sont les concurrents », « limites avouées contre étapes annoncées » → Concurrent défini par revendication [F15-31]
- « qui tient la plume », « troisième axe de fragmentation » → Programmation de poids [RD21-35]
- « quoi publier, quoi garder secret » → Trois rangs de divulgation [F15-44]
- « quorum », « matrice de transfert » → Quorum par type d'accès [F22-44]
- « R1 de Fable », « point de bascule m sur p » → Loi de la référence honnête, mesurée [F01-19]
- « racine plus τ plus dérive », « exposant de Hurst », « n/√m inobservable » → Nul effectif avec exécutions jumelles [F22-13]
- « racine puis linéaire », « combien un saboteur peut cacher » → Loi d'échelle du dommage caché [F01-36]
- « randomiser la cible », « test du changement de signe » → Nul honnête par tirage de la cible [F08-34]
- « rang contre le jumeau », « dissonance » → Moniteur de dissonance [RD21-17]
- « rang contre le jumeau », « nul local », « sauf nul par acte » → Nul par acte [N076-03]
- « Reasons or watching version 7 », « billet MSM » → Révision de « Reasons or watching? » [F25-32]
- « recouvrement des échecs », « indépendance nominale » → Matrice de succès croisés lue sur les résidus [F15-42]
- « réentraîner les sondes sur les audits » → Trois sens de « entraînement » [F01-67]
- « réentraîner les sondes sur les détections », « la ligne 170 contre N-060 » → L'asymétrie d'apprentissage contre l'invariant de l'oracle [N075-25]
- « références attendues à l'aveugle » → Liste scellée de références attendues [F08-48]
- « régime d'excès », « horizon de la garantie » → Forme restreinte de la borne du plancher [N075-04]
- « rendre l'agent lisible par entraînement » → Entraîner l'agent à rester lisible [F08-30]
- « repli de N-004 » → Fermeture du repli du lemme [F22-06]
- « répliques ratées contre réussies sur la même tâche » → Contraste intra-tâche [F01-27]
- « reproduire le papier avant le programme », « étape 0 étape 1 étape 2 dopamine » → Première expérience du signal, sans attaque [F25-13]
- « réserver Fable » → l'économie de Fable [GO-07]
- « retirer les directions jusqu'au hasard » → Test garder/retirer et redondance [F01-45]
- « rien de neuf dans l'audit », « Shekhar » → Aucune revendication de méthode inédite sur l'audit [F01-16]
- « sabotage par coïncidences » → Mode moyenne et mode dépendance du dommage [F08-38]
- « sabote quand personne ne regarde » → Se régler sur l'observation [F15-58]
- « saboteurs scriptés », « comportement d'abord » → Signature comportementale avant toute sonde [F15-60]
- « sait la bonne réponse et en donne une autre », « erreur contre écart voulu » → Connaître la référence et choisir autre chose [F15-55]
- « sandbagging chiffré » → Le surplus de capacité chiffré [F01-21]
- « savoir la bonne action et en choisir une autre », « cœur algorithmique du sabotage » → Le passage obligé [N075-20]
- « scan », « higher criticism » → Cinq statistiques sur les mêmes scores [F22-33]
- « se cacher de l'un fait apparaître à l'autre », « pas la décorrélation » → Deux regards : le dilemme [`N075`]
- « se taire ensemble contre tomber ensemble » → Deux sens de « tomber en même temps » [F25-23]
- « sélection fois identification », « q », « c'est toute la question » → Couverture de l'oracle [RD21-29]
- « servi par repli », « Q6 » → La quatrième classe d'issue [RD22-25]
- « seuil estimé de G1 », « intervalle bêta », « facteur dix » → Référence du seuil de la porte G1 [F22-17]
- « seuil qui triple quand le régime change » → Dérive de régime du seuil [RD21-13]
- « seuil toléré K », « taux d'audit nécessaire », « régime signature / excès », « D-1 attaquant informé », « borne lue à l'envers » → La table du seuil au taux d'audit [N076-15]
- « seul le hasard corrige », « D-2 asymétries », « un audit sans trouvaille ne laisse aucune trace » → Les trois lignes de la note « asymétries » [N076-18]
- « silence commun, chute conjointe, apport sur une table » → Une table, trois lectures [F25-20]
- « société de chercheurs IA », « salons, prépublications » → Mode essaim du collisionneur [F01-61]
- « somme globale », « Avenhaus et Jaech », « meilleur au pire cas » → Somme globale [F22-30]
- « somme plate en N » → Somme globale plate en nombre d'agents [F25-46]
- « sonde nettoyée du texte », « discordance texte-activations » → Résidu de sonde [F08-04]
- « sonde secrète tirée après coup » → Sonde tirée après le gel des poids [F15-25]
- « sondes secrètes tirées au sort » → Secret d'un tirage d'audit contre secret d'une sonde [F08-27]
- « square root law », « stéganalyse », « Ker » → Loi de la racine carrée de la stéganographie [F01-37]
- « strate comptée à zéro » → Strate ouverte hors conditions = strate non mesurée [F15-41]
- « substitution par le harnais » → Deux sources de sabotage [F08-39]
- « surprise contre différence de valeurs », « deux lectures de réussite attendue », « dopamine, un ou deux instruments » → La question préalable sur la sonde de surprise [`N076`]
- « surrogates », « échange de copies » → Substituts par permutation [F22-23]
- « surrogates », « permuter les pas » → Données de substitution par permutation des pas [F08-19]
- « sycophancy », « flatter le juge » → La flagornerie comme famille de charges [F01-50]
- « T », « les marginales sont aveugles », « théorème d'aveuglement » → Retrait du « théorème négatif du programme » [F15-11]
- « table des revendications périmée » → Contradictions entre pièces qui interdisent une phrase du billet [F15-47]
- « table v2 », « table en vigueur » → Table des revendications à refaire [F22-09]
- « tau », « écart entre tâches » → Terme entre tâches [F22-13]
- « taxe de cohérence », « H6 prime », « H10 », « taxe de robustesse » → Ce que N-077 ferme et ce qui reste ouvert [N076-28]
- « taxe négative », « seuil delta » → ι ≥ 0 par inclusion, seuil δ [F08-23]
- « télescopage du dommage », « identité référence − lecture + lecture − issue » → Bilan à trois termes… [F25-02]
- « temps et agents », « bat le séquentiel par agent » → Statistique conjointe remplacée [`F22`]
- « tenaille », « dilemme », « iota », « taxe jointe » → L'étau décomposé en trois énoncés [F08-09]
- « terme tau », « référence par tâche » → Référence par régime contre référence par tâche [F08-15]
- « test de devinette » → Test de neutralité et test de devinette [F22-72]
- « test de devinette », « contrôle positif de la neutralité » → Question neutre et test de devinette à deux devinettes [F25-15]
- « test de devinette », « question neutre » → Ce qu'on sert au collisionneur, et la question neutre [F15-36]
- « tester le total », « additivité » → Le lemme d'additivité [RD22-02]
- « tester que le billet ne fuit rien » → Tests du billet avant parution [F15-48]
- « tests additifs », « pire qu'aveugle », « multi-ensemble des scores » → Caractérisation exacte de l'aveuglement [F15-12]
- « théorème T », « marginales préservées », « permutation » → Théorème négatif retiré [F22-07]
- « théorie du danger », « nouveauté et dommage ensemble », « alerte à deux signaux » → La règle à deux clés [N075-16]
- « thèse du 22 novembre », « programme v3 », « Bi » → Thèse du papier A, version 3 [F25-40]
- « thinkingLevel », « zéro jeton de pensée » → Garde des appels aux modèles de Google [RD21-07]
- « tôt, tard, étalé » → Simulation du franchissement séquentiel [F22-22]
- « tous butent sur la référence » → La référence honnête comme question brûlante commune des voisins [F15-32]
- « trois planchers », « borne minimax » → Les « trois planchers » en théorème [F01-23]
- « trois planchers », « facteur racine de trois » → Plancher d'audit et somme des trois termes [F08-21]
- « trois tours », « entrée + 90 000 », « brouillon puis critique » → Formes de demande pour tenir l'effort maximal [F25-63]
- « troisième issue », « indéterminé », « combien de tâches » → Calcul de puissance du plan [F22-18]
- « troisième tour utile ? » → Instrumenter le collisionneur [F01-47]
- « tromper l'externe laisse une trace interne », « trahison par les activations » → L'étau [N075-15]
- « tromper la boîte noire laisse une trace interne » → l'étau [GO-26]
- « un mode est un cas », « modes jamais vus » → Compter les modes, non les épisodes [F22-62]
- « une constante, trois papiers » → Les trois objets comme trois lectures de la constante de la loi héritée [F08-11]
- « une copie corrompt les autres » → Contagion du sabotage entre copies [F01-09]
- « union meilleure boîte noire et sonde », « taux total de fausses alertes égal » → Complémentarité à taux total de fausses alertes égal [F25-43]
- « usages du hasard », « Blindfold et la suite » → Les sept fonctions du hasard du défenseur [F15-21]
- « valeur et erreur de différence temporelle », « signal de récompense interne » → Place du signal de dopamine… [F25-01]
- « variable de contrôle », « √(1 − ρ²) », « l'audit hérite du N²/m » → Bilan de l'audit au hasard dans les unités du programme [F15-23]
- « variante B », « réajustement » → Les lentilles R et S [RD22-21]
- « vérifier le résultat plutôt que détecter l'attaque » → Mesurer l'issue et corriger [N075-01]
- « vérité plantée », « retrouver ce qu'on a mis » → Banc à vérité plantée [F22-19]
- « voie rapide / voie lente », « le lemme ne porte pas le plancher » → Séparation du lemme d'additivité et de la borne du plancher [N076-16]
- « xhigh contre max », « banc à erreurs plantées » → La profondeur n'est pas le compte de jetons [F25-62]
- « Zhang et Gao sont-ils faux ? », « antécédent défectueux » → Réserve sur la proposition 1 de l'article 2606.10456 [F15-17]

## 8. Journal de couverture

Ce que chaque agent de lecture a ouvert, n'a pas ouvert et pourquoi, ses doutes ; puis les lignes « Opérations » des registres (opérationnel non extrait).

**Signalements — `N075`**

- Non ouverts par prudence ou hors mandat : `docs/decisions/ligne-claude-md-N-075-v1.md` (citée par l'erratum 3 v2) ; la lecture des douze voisins, les notes sur l'adjudant, la pince et la couverture de l'oracle, N-076, N-060 v3 ; aucun fichier interdit par la consigne n'a été ouvert. L'erratum 3 (v1) n'a été lu que par `diff` contre la v2.
- Les seuls chiffres recopiés sont des illustrations de calcul « sous supposition » (ordres de grandeur) et des confiances d'options ; aucun résultat des expériences interdites. Les fichiers lus n'en contiennent pas.
- Doute : la v3 dit « lecture des sept voisins » (nom de fichier) et « douze voisins » (contenu) ; c'est la même pièce (`973bd0dd…`).
- Doute : les points 1 à 5 de la section 11 ne sont pas nommés à `GO-2026-11-21-61` ; savoir si un « go recos » plus large (`GO-2026-11-21-60`, `-63`) les couvre est laissé à la mère par l'erratum 3 v2 : je les ai notés comme non tranchés.
- Le rattachement des mots de Lazar à chaque point de `GO-2026-11-21-61` est la lecture de la mère, non vérifiée par le concepteur (erratum 3 v2, pas 10).

**Signalements — `N076`**

- Fichiers lus : les quatre assignés en entier (N-076 lue en deux pages, 383 lignes) et des extraits de l'inventaire des seconds regards (sections 1.1, 1.3, 1.13, 2, 5) pour la numérotation. Rien d'autre ouvert ; aucun fichier cloisonné, aucune autre branche.
- N-076 cite des fichiers non ouverts (notes « percée », « attaquant informé », « asymétries », « science de la détection », verdicts d'antériorité, N-060 v3, préenregistrements) : décrits seulement d'après N-076.
- Chiffres repris : uniquement des blocs de calcul d'illustration de N-076 (sous supposition, aucune donnée du programme) et un chiffre publié dans N-077 (cohérence d'environ 80 %, vérifié sur PDF par le contre-lecteur) ; aucun résultat des expériences interdites.
- N-076 v1 est « à contre-lire » et N-077 « non contre-lue » à leur écriture ; je n'ai pas vérifié l'état de leurs contre-lectures (hors de mes fichiers). `CLAUDE.md` mentionne N-076 « lue avec son erratum 1, qui prime » et N-077 comme inscrite.
- Rattachements à l'inventaire : jugement de ma part ; plusieurs concepts de N-076 n'ont pas d'entrée propre (marqués « nouveau »).

**Signalements — `GO`**

- Cloisonnement tenu : seules les lignes 600 à 737 de `registres/go.md` et l'inventaire autorisé ont été lus. Aucun fichier de demande 24 ni de réponse 24 n'a été ouvert.
- Je n'ai recopié aucun score ni table du barreau 5, ni aucun résultat de 7a, 7b, T0.6, étape B, B bis ou P3-bis.
- Les nombres 0,35 et 0,15 de l'étau sont des confiances données a priori, pas des résultats d'expérience : je les ai gardés.
- Doute : la phrase « le taux réel triple quand le régime change » de GO-2026-11-21-26 a une origine que je n'ai pas pu établir. Je l'ai laissée de côté par prudence.
- Les numéros de l'inventaire ont été rattachés d'après ses seuls titres, sans lire ses corps.

**Opérations — `GO`**

GO purement opérationnels de ces deux jours (instances, clés, crédits, courses de calcul, poussées, recharges) : GO-2026-11-21-01, -02, -03, -04, -05, -08, -09, -11, -13, -14, -20, -22, -23, -24, -26, -28, -30, -32, -33, -37, -39, -42, -48, -52, -58, -62, -63, -70, -73, -74, -81, -82, -83, -86, -87 (point 1), -88 ; GO-2026-11-22-01, -02, -03, -04, -05, -06, -07, -08, -10, -11, -13, -14, -15, -16, -19, -21, -23, -27, -29, -30, -31, -33, -37, -38, -39, -41, -43, -44, -45, -48, -49, -50 (en partie).

**Signalements — `RD21`**

- Le reste de l'inventaire et les notes sources citées n'ont pas été ouverts (seuls les titres de l'inventaire). Les numéros d'inventaire donnés sont des rapprochements par titre, à confirmer.
- La note « universalité entre modèles » (l. 4682) et les branches matiere-premiere/, quarantaine/ ou coffre, qui sont citées, n'ont pas été ouvertes.
- Les lignes du barreau 5, de la lecture par lentilles et de l'étape 1 du papier « dopamine » ne sont citées que pour leur existence, sans aucun chiffre.
- Doute : R-4595 est numérotée deux fois (l. 4733 et 4734) ; R-4573 et R-4574 sont inversées (l. 4711-4712).

**Opérations — `RD21`**

Formation du barreau 5 (recréations, arrêts, crédit du loueur), étage 2 de la ligne 3 et palier 0b (relais, gestes, mots de départ, récupération, place disque), versions v5 à v8d du collisionneur, bascule vers une nouvelle mère sur un autre compte (passation, sessions filles, canal de l'essaim), clés et soldes (Rigaud, Minuit, Luc, Mistral, OpenAI 2, Gemini), lentilles (listes, registre propre, opérateur), bras A (avenants, devis, admission de Mistral), poussées et errata d'heure : l. 4478-4888, passim.

**Signalements — `RD22`**

- Non ouverts par cloisonnement : réponse 24 (nouveaux modes d'attaque, sous séquestre ; R-4811 n'en nomme que l'existence et des candidats, non recopiés), lot en quarantaine (demande 23), dossiers sous matiere-premiere/ et archives-reponses-modeles/.
- Aucun résultat chiffré de 7a, 7b, T0.6, étape B, étape B bis, P3-bis ni du barreau 5 dans ces lignes ; rien recopié.
- « Exemption de la sonde » (GO-2026-11-22-03, R-4760) : contenu non décrit dans le registre, non extrait.
- Opérations (une ligne) : collisionneurs repris et dossiers finis ; étalonnage du saboteur suivi par relevés, coupure relevée à 16 USD ; machine Hetzner de l'organisme créée (essai 3 du palier 0b) ; machine des lentilles créée ; greffons d'échecs connus versés ; relève de la mère et sauvegardes de l'ancienne mère ; tâches programmées de réveil et de rappels ; demandes de crédits rédigées, rien envoyé.

**Signalements — `F01`**

- Je n'ai ouvert que les quatorze fichiers assignés (sept réponses, sept demandes) et l'inventaire permis. Je n'ai pas ouvert les « remarques » auxquelles les réponses renvoient (contexte du programme, réponses fusionnées A à D, réponses « percée » A à E, consigne de demande approfondie, fiches de lecture, compteurs) : non assignées.
- Aucun fichier assigné ne porte de nom interdit par le cloisonnement ; aucune de mes réponses ne contenait de résultat chiffré des expériences protégées.
- Doute sur l'état : les réponses de Fable sont des propositions ; l'acceptation par Lazar des rép. 1 et 2 n'est connue que par la phrase de la demande 6, sans identifiant GO ; le « go » de la demande 3 porte sur la conception, non sur une dépense. À vérifier dans `registres/decisions.md` ou `registres/go.md` (non ouverts).
- Collision de noms : Fable emploie E0 pour deux objets différents (pilote du levier en rép. 1, expérience des fausses alertes en rép. 3) et des hypothèses H1 à H11 et candidates R1 à R5 locales qui ne sont ni les hypothèses du programme ni les règles gelées. À ne pas confondre dans la note de mémoire.
- Fable signale lui-même qu'il n'a lu que le résumé des nœuds N-053, N-058, N-075 à N-077 : ses additifs proposés peuvent mal citer leur lettre.

**Signalements — `F08`**

- Non ouverts : les demandes 8 à 14 elles-mêmes (non nécessaires, les réponses suffisant) ; `contre-lecture-reponse-10-v1.md` et `table-corrections-reponse-10-v1.md` (non assignés) — R10 peut donc avoir été corrigée ailleurs ; les pièces d'entrée citées en tête des réponses (note sur la pince, faits sur l'étau, lecture de la stéganographie, conception de l'essaim) non ouvertes.
- Lu en exception permise : `docs/notes/seconds-regards-sabotage-inventaire-v1/inventaire-seconds-regards-invariants-noyaux-v1.md`, pour les numéros.
- Aucun fichier interdit par le cloisonnement n'a été rencontré ni ouvert. Aucun résultat chiffré des expériences visées n'apparaît dans ces fichiers.
- Doutes : R8 cite des chiffres de la pièce de faits sur l'étau (part de la baisse de rappel passant par le texte) et R14 cite des chiffres de couverture de la base gloutonne et du devis ; ils ne relèvent pas des expériences interdites, mais ne sont pas opposables (je ne recopie que l'existence, sauf mention de nature). Les chances chiffrées sont des jugements de Fable. Aucun identifiant GO ou R- n'établit ces propositions dans les fichiers lus : leur sort réel est à chercher dans `registres/`.

**Signalements — `F15`**

- Je n'ai pas ouvert `demande-19-etau-equipe-rouge-quarantaine-v1.md` par prudence (le mot « quarantaine » figure dans son nom, bien qu'il ne soit pas dans la liste des noms interdits) ; la réponse 19, assignée, a été lue : elle déclare ne contenir aucun contenu en quarantaine.
- Je n'ai ouvert aucune des pièces citées en remarques par les relectures (réponses 9, 11, 12, 14, contexte du programme, notes de lecture, sources des conditions d'abonnement, copies sans nom) : hors de mes fichiers.
- Les chiffres de mes fichiers sont des chances et confiances de jugement de Fable, des montants de devis (réponse 14, rapportés dans la réponse 15) et quelques chiffres de la littérature rapportés par les notes ; aucun ne vient des expériences interdites. Je n'ai recopié aucun des chiffres de la littérature (non opposables, R7), sauf la dimension des cœurs redondants rapportée par la réponse 12, qui n'est pas un résultat d'expérience du programme.
- Doute : la réponse 17 ignore « Blindfold », alors que l'inventaire (2.1) le donne lu sur PDF (Zhu, Zuo, Sun, arXiv 2610.37055) et occupant de la base du plancher ; les statuts de la zone 1 (mise en aveugle) et de la fonction « choisir ce qu'on audite » sont donc à relire à la lumière de cette pièce.
- Doute : la réponse 19 traite « famille » et « lignée » comme synonymes, à confirmer.
- Aucune de ces relectures n'est tranchée par Lazar dans les fichiers lus ; je n'ai vu aucun GO qui les établisse (seul GO-2026-11-22-25, le protocole X, est cité par la consigne générale du dépôt).

**Signalements — `F22`**

- Cloisonnement : je n'ai suivi aucun renvoi vers `quarantaine/` ni vers aucune autre pièce citée en entrée des réponses (notes de lecture, table sans nom, réponses 2, 9, 19). Je n'ai pas ouvert les fichiers `demande-*.md` ; en particulier pas `demande-23-lot-quarantaine-et-revendications-v1.md`, par prudence, puisqu'il pourrait décrire le lot. La réponse 23 elle-même dit n'avoir vu aucun contenu en quarantaine ; je n'en ai rien reproduit d'autre que ses hypothèses générales sur sa nature.
- Les réponses ne contiennent aucun résultat chiffré des expériences 7a, 7b, T0.6, étape B, étape B bis, P3-bis ni du barreau 5 ; les seuls chiffres recopiés sont des paramètres de littérature, des ordres de grandeur théoriques de Fable ou des confiances de recommandation.
- Doute : aucun identifiant GO ou R- ne tranche ces propositions dans mes fichiers ; la « thèse retenue le 22 novembre » et les retraits du lemme et du théorème sont dits « décidés » par Fable, sans identifiant visible.
- Doute : les ordres de grandeur (150 tâches par extrémité, cent essaims par bras, millier d'épisodes, marges du budget de bits) sont de la main de Fable, « à refaire ».
- Rattachement à l'inventaire : seuls 2.1, 2.9, 2.16, 2.19, 2.20 et un voisinage avec 2.7 correspondent ; le reste est « nouveau ».

**Signalements — `F25`**

- Non ouverts par prudence : `demande-24-nouveaux-modes-d-attaque-v1.md`, `reponse-24-SEQUESTRE-v1.md`, `reponse-24-defaut-effort-max/` (cloisonnement). La réponse 30 mentionne la demande 24 (relance) sans contenu : rien recopié.
- Je n'ai pas ouvert les demandes 25 à 30 (seules leurs empreintes sont relevées : 25 `c2954a5dbc02d384`, 26 `1f4e1f09c5da9534`, 27 `9e265f9840b81862`, 28 `f552f514961f78be`, 29 `c876c616cbe8cde2`, 30 `88e75737807bb158`) ; les réponses suffisaient.
- Aucun chiffre des étapes B et B bis, de l'expérience 7a/7b, de T0.6, de P3-bis ni du barreau 5 n'apparaît dans mes fichiers ; la réponse 26 nomme l'existence des verdicts des étapes B et B bis, sans chiffre. Le verdict qualitatif « non lisible » de l'expérience 1 (billet « Reasons or watching? ») est cité ; l'expérience 1 n'est pas dans la liste interdite, mais à vérifier par la mère.
- Les « barreaux 0 à 3 » de l'épreuve de l'étau (réponse 29) sont une conception, sans score : distincts du « barreau 5 » interdit et du barreau « sabotage ou empreinte ».
- L'empreinte de l'inventaire lu (`02252df286503f8c`) diffère de celle de sa copie sans nom servie à Fable (`d5a49675ccda55f7`) : attendu (copie anonymisée), non vérifié plus avant.
- Les états « retenu le 22 novembre » (thèse du papier A, retrait du théorème et du lemme) sont rapportés par Fable dans la réponse 27 ; je n'ai pas vu l'identifiant GO correspondant.
- Les réponses 25 à 30 citent de nombreux titres « de mémoire » ; aucun n'est vérifié sur PDF.

**Bibliothécaire.** Lus en entier par moi : l'inventaire des seconds regards ; l'extrait de la décision N-075 ; la réponse 32 de Fable. Lus par sondage : les autres extraits (titres, définitions des passages sur le lot tenu à l'écart et l'équipe rouge, pour vérifier qu'aucun contenu d'attaque n'y figure). Non ouverts : la demande et la réponse 24 ; tout ce que la liste d'autorisation exclut. Errata de ce mémo : aucun à ce jour.

## Historique

- v1, 22 novembre 2026 : première édition, à `5b596acc`. Non contre-lue.
