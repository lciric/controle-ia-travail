# Fiche de réception du rejeu à graine (addendum v2 de R1) — v1

Écrite et scellée par conv-audit le 2 novembre 2026 à 16:45 UTC (heure relevée par `date -u`), **avant toute récupération et toute lecture** de la sortie. Aucune ligne de la sortie n'a été vue ; la branche `calcul/r1-resolution-graine-v1` n'a pas été récupérée (son nom seulement, par `git ls-remote`). Rien de l'analyse de R1 n'est ouvert par cette réception.

## 1. Ce qui a été lancé (n° 281 de session-depot, `69a960fa…`)
- Instance **58851293**, créée à 16:42:40 UTC ; offre 32744973 (A100-SXM4-80 Go, centre de données, Tchéquie, CUDA 13.0, 1,187 USD de l'heure), seule conforme aux filtres du texte scellé.
- `GO_ID=GO-2026-11-02-02` (plafond commun 25 USD), enveloppe relevée par **GO-2026-11-02-14** (accord de Lazar du devis révisé, 15:15 UTC ; pire cas écrit ≈ 6,25 USD, 268 min).
- Commit lancé `c2a8b6e1` ; amorce `dc8164e2…` ; plafond de l'amorce 235 min ; branche de sortie `calcul/r1-resolution-graine-v1`.

## 2. Textes qui encadrent la lecture (scellés avant le lancement)
- Addendum v2 : `prereg/R1-addendum-relance-v2.md`, sha256 `9d17d640509c9b5dd0285e90f3096145b82f2e0ea2e73e62725c0e0c8cb71059` (commit du texte `dfe05285`).
- Configuration : `prereg/R1-graine-config-v1.json`, `0f300925546d886b8408d137903e711af579abb0d5947b1b88a27da894c4070f`, empreinte canonique `f91716bf95c4c4ab07e4155c667539cee9baff38b7ca2639dff0dea167d44db2`.
- Table de tokenisation v2 : `prereg/R1-table-tokenisation-v2.json`, `5f6cf489…` (compagnon au commit `82a5ed18`).
- Code cité : commit `0e2a88718f4249e556e159f45f2df38ac304331e` (arbre gelé identique jusqu'à `c2a8b6e1`, vérifié par la concordance finale).
- Concordance finale (conv-audit) : `concordance-finale-addendum-r1-v2-scelle-v1.md`, `07ea87e0…`.

## 3. Voie de réception
- **(b), par défaut** : copie à l'octet, par session-depot, de la sortie scellée et de ses compagnons sur une branche du canal (comme pour la course d'attaque contre le juge), sans que conv-audit récupère `calcul/…`.
- (a) sinon : récupération de `calcul/r1-resolution-graine-v1` par refspec explicite, **seulement sur le mot de Lazar** (règle des branches `calcul/…`).

## 4. Contrôles à la réception, avant toute lecture (consignés)
1. Liste des fichiers ; chaque empreinte comparée à son compagnon ; aucune forme de clé.
2. Manifeste : commit `c2a8b6e1` et arbre gelé du code `0e2a8871` ; empreinte canonique de la configuration `f91716bf…` sous ses deux libellés ; table v2 `5f6cf489…` ; graines dérivées par `numpy.random.SeedSequence` et consignées (R9) ; `GO_ID` ; identifiant d'instance ; versions (torch 2.14.1, révision du tokeniseur) ; dernière ligne des essais « 71 passed ».
3. Code de sortie et étapes atteintes (0 validation, 1 résolution, cibles du lot, 1 bis lot fidèle, table) ; présence ou absence d'`arret.json` et sa cause ; durée de chaque étape ; dépense de l'instance (heures × 1,187 USD) et arrêt de l'instance par son identifiant (R10, chez session-depot).
4. Table v3 (`prereg/R1-table-tokenisation-v3.json`) : présente ou non, scellée ou non ; son empreinte.

## 5. Lecture (après les contrôles, une seule fois)
- Par un **lecteur neuf** (ni auteur du texte, du code, de la concordance, ni de cette fiche), qui applique **la section « Critères de lecture gelés » du texte scellé, telle qu'écrite** : règle unique « résolu si et seulement si l'empreinte de trajectoire égale celle de P3 » ; classe de la validation (« graines validées », « méthode transposée, graines non validées », « méthode non transposée ») ; lectures du lot (« fidèle » par cible, VI-09 ; « réserve lot non fidèle » ; « sans mesure ») ; résolution (7 sur 7 → table v3 complète ; k non résolus → table partielle et **liste à Lazar avant l'addendum v3**, avec la forme de chaque cible du lot) ; contrôle croisé (« non résolu » ou « contraire » → table non construite, audit).
- **Audit de symétrie (R4)**, déclencheurs écrits : accord non contraint égal à 1 exactement sur tous les pas des 147 ; aucune quasi-égalité ; durée cumulée des étapes 0 et 1 sous 5 min ; accord observé non distinct de l'accord attendu sous graine indépendante (VI-11). Un résultat trop propre reçoit le même audit qu'un résultat décevant.
- **Réserves portées par la concordance** (R-1258), à écrire au verdict : (1) **VI-09 est un relâchement non signalé** par le texte (ne peut jouer que pour `mention/2605.17899v2/e0`, seule cible déclarable non inversible, lot 5 à forme non prouvée) ; (2) le compte qui justifie le plafond de 16 balayages (2 pas sur le chemin canonique, `comptes_reels-sortie.txt`, `a2bd318f…`) n'est pas recopié près du seuil.
- Prédictions P-G1 à P-G4 : comparées aux valeurs observées, **descriptives** (elles ne décident rien ; R3 : rien n'est relancé pour les atteindre).

## 6. Ce qui suit
- Verdict scellé, puis soumis à Lazar ; si k ≥ 1 non résolus : liste à Lazar avant tout addendum v3.
- Addendum v3 (relance de R1 sur la table v3), écrit et scellé par session-depot, concordance de conv-audit ; les attentes de la procédure de réception de R1 (`reception-r1-relance-v1/`) sont à réécrire (empreinte de la table et liste des non résolus changent, m-8).
