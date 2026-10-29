# Table de dépendance « critères de G0 → travaux du programme » — v2 — BROUILLON (non contre-lu, non scellé)

**Déclaration.** Je n'ai écrit ni la v1 (`e2480618…`) ni sa contre-lecture (`3c5c51bc…`). Modèle : Sonnet 5.5 (sous-agent neuf). Heure `date -u` au début : 2026-10-29 10:29:46 UTC. Interdits tenus : rien lu sous `donnees/`, `prereg/P3-consignes-v1.md`, `diag/*/traces` ; aucune branche ; aucun git ; aucune dépense ; aucun fichier existant modifié ; rien scellé. La v1 demeure telle quelle (R12).
**Empreintes (`sha256sum`) des fichiers lus.** Table v1 `e2480618816d6bcbea77654fe805b82a8e1333cddc428ea1ce6c03e75e6fe4f5` ; contre-lecture `3c5c51bcdb40ba55f7672f72e8f18f09a3e9ff06881a6bc0daca4057f6b9d22c` ; avis sur le repli `62cc6fbf4793d477cd9ca22a168febe3abc5ee3887fcd78db4d31b891dc50aab` ; grille (copie `/tmp/claude-0/-home-claude/be74bc5f-030c-58ad-8f83-cdf5edf47ca3/scratchpad/grille-G0-v1.md`) `320af9b0b367c08ddcb08d39979ca9c014157d14701b107369b760be48a76a34` ; brief v2 `9261932a11f29e8643175bc6e150d5455067f58a3cb1e57dca99e02cb17aa3b2` (l. 86-284 et 332-374 lues) ; `registres/decisions.md` `58330f90323e83b6e950909b68bab49c5f6293aecdfc99fc4ce0ad1dd48a7977` (fichier vivant : les lignes citées valent à 10:29 UTC ; ligne 462 = N-027).
Lus en plus (16 premiers caractères) : note moissonneur `87d36ce3336d63b3`, note tour (c) `ad33007204aa0ecc`, devis v7 nonies `4b6a7d95b6466018`, programme de conception de l'organisme v2 `353515fffa33bb93`, décision pilote couche 2 v5 `255a364e710cd713`, paramètres de la garde δ `db6037507f23d1ee`, brouillon 4 de T0.7 `a292088ca6e7f593`, `registres/etat.md` `54d7bb738a71b569`, `CLAUDE.md` `a2aabda8a181d46d`.
**Avant usage** : contre-lecture R2 par un sous-agent neuf ; mot de Lazar sur D-TD-1 (§ 5) ; scellement avant le verdict de G0 (date : § 8.2). La table n'a d'effet que si le verdict R13 de G0 rend autre chose que « franchie ».

## 1. Constats de la contre-lecture v1 → traitement

| constat | traitement dans la v2 |
|---|---|
| CT-01 cellules non tranchées | **Accepté.** Moissonneur, tour (c) et course reclassés sans cellule provisoire (W34 à W36), sur les notes `87d36ce3…` et `ad330072…` ; classes « à confirmer » et « non établi » supprimées ; cas C1 à C9 supprimés, leur justification est dans la colonne « source ». |
| CT-02 organisme / T0.6 ; « sert » inventés | **Accepté.** § 2 sépare « l'organisme » (pôle scientifique automatique) des organismes de T0.6. « Sert » de la course, du tour (c) et du moissonneur = — (aucune source ne les relie à un critère) ; moissonneur : première moisson réelle sur GO (W36) ; course : dépense sur GO (W34) ; l'argument « évite de perdre un mois » est retiré. |
| CT-03 W10, W12 | **Accepté.** W10 scindée : apprentissage (W15, dépend 1) ; lectures sur les épisodes de T0.6 (W16, W17, dépendent 1 et 2). Run des bases sur ces épisodes (W19) : dépend 1, 2 et 3 (grille l. 468 ; le brief est muet sur 3 : § 8.5). |
| CT-04 N figé | **Accepté comme nœud, non tranché** : § 5 (D-TD-1). Chaque ligne conditionnelle porte les deux colonnes (critères, produits) : la table fonctionne sous (a), (b) et (c). |
| CT-05 lignes manquantes | **Accepté.** Ajoutés : P4-instrument (W12), simulations de la garde δ (W22), pilote de la couche 2 (W23), banque pleine (W24), P3b et addendum 2 (W32, W33), phases 2 et 3 (W31), pièces du pôle (W34 à W37), nœuds (W38). Liste dressée sur `registres/etat.md` l. 36-50, le brief § 7 à 14 et R-436 à R-458 ; identifiant de registre dans la colonne « source ». |
| CT-06 couche 2 | **Accepté.** « Couche 2 » = banque avec sabotage (programme de conception l. 99) : W22, W23, W24 ; G1 : W20, W21, W30. Dépendance « 5 » de la couche 2 retirée (aucune source). |
| CT-07 W14 | **Accepté.** Rédaction de G1 (W20) dépend de 5 ; scellement (W21) de 2, 3, 4, 5 (grille l. 468-469 et brief l. 214-217). Point signalé : § 8.4. |
| CT-08 critère 8 | **Accepté.** Règle de contenu unique pour les quatre textes (G1, papier C, papiers A et B : § 2, « règle des chiffres ») ; papiers A et B dépendent de 8 (brief l. 336) ; « sert 8 » mort retiré de W28, W29 ; références (W04) séparées de la traçabilité (W05, W06), qui suit les textes scellés. |
| CT-09 latitude | **Accepté.** Mots « transversal », « reste », « éventuelle », « honnêtement », « tant qu'il reste ouvert » retirés ; « décisive » défini (§ 2) ; rejeu de T0.3 = classe R (W09) ; lignes « 1 à 6 », « 7 et suivants » retirées. |
| CT-10 taillage | **Accepté** : § 7 (règle d'affectation, test de retrait, sens de chaque changement). |
| CT-11 « décisive » | **Accepté** : définition mécanique (d1, d2) ; liste par numéro : W24, W26, W27, W30, W31 ; P3 éclatée (W32, W33), P4-instrument en W12. |
| CT-12 application | **Accepté** : § 6. Date limite d'une version suivante : non fixée ici, renvoyée à Lazar (§ 8.2). |
| CT-13 forme | **Accepté** : seconde table inverse (droits de devis, § 4) ; provenance corrigée ; collisionneur sans « sert 8 » (W03). **Refusé ici** : correction de R-454 (je ne modifie aucun fichier existant ; R-458 porte déjà la rectification, R12). |

## 2. Définitions (mécaniques ; aucun jugement après le verdict)

- **N** : ensemble des critères de 1 à 8 que le verdict R13 de G0 ne déclare pas « tenu » (« non franchie » et « non concluante » comptent pareil : avis l. 23-25 ; états de la grille l. 68-77).
- **Colonne « dépend : critères »** : critères dont le brief, la grille ou une décision citée écrit que le travail lit un produit ou en exige l'existence. **Colonne « dépend : produits »** : produit qui prouve chacun de ces critères, plus les pièces propres au travail. **Produit scellé** : fichier committé sur `main` avant l'usage, dont `python -m controle_ia.scellement verifier` rend OK et qui contient la ligne citée (un verdict scellé par sous-agent neuf compte). Critère → produit : 1 `P-T04` ; 2 `P-V6` ; 3 `P-L7` ; 4 `P-B4` ; 5 `P-T03` ; 6 `P-G1` ; 7 `P-C` ; 8 `P-EA`.
- **Colonne « sert »** : critères dont la grille ou le brief écrit que le travail produit une preuve ; sans source écrite : —.
- **Classes.** **F** fermé. **K** conditionnel : ouvert si sa condition est remplie (L2). **R** rattrapage : second jeu de preuve d'un critère, ouvert seulement si ce critère est dans N. **I** indépendant : ni critère ni produit. **H** hors clause : décision de Lazar dans tous les cas, ni ouvert ni fermé par la table.
- **Dépense externe** : toute dépense d'argent ou de crédit (instance payante, interface de programmation de modèle, session de modèle facturée) et tout accès au réseau sortant du dépôt. Le travail sur processeur local, la lecture des fichiers du dépôt, la rédaction et les essais ne sont pas des dépenses externes (brief l. 366-367).
- **Expérience « décisive »** : tout run, simulation comprise, qui (d1) cite dans son manifeste (R9) l'empreinte d'un préenregistrement scellé de G1 ou du papier C, ou (d2) lit un résultat de G1, de la porte GC ou des phases 1 à 3. Un run qui n'est ni d1 ni d2 (simulations de la garde δ, pilote de la couche 2) n'est pas décisif, même s'il alimente un paramètre.
- **Règle des chiffres (CT-08)** : un texte à sceller (G1, papier C) ou à rédiger (papiers A, B) ne cite comme chiffre de littérature que ceux de la table des chiffres de T0.2 au statut confirmé ou corrigé ; un chiffre introuvable s'emploie sous la forme « l'article imprime X » avec sa réserve (grille l. 364-365). Contrôle au scellement, pour les quatre textes ; il ne change aucune classe.

## 3. Table des travaux

`B` brief v2 ; `G` grille ; `A` avis sur le repli ; `D` `registres/decisions.md` ; `E` `registres/etat.md` ; `T7` `brouillons/T0.7-sondes-v0-v1-brouillon4.md` ; `PC` programme de conception de l'organisme v2 ; `DP` décision pilote couche 2 v5 ; `PG` paramètres de la garde δ ; `MO` note moissonneur ; `TC` note tour (c) ; `DV` devis v7 nonies (les trois derniers sous `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/`). Produits : `P-T04` verdict `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` ; `P-T03` `diag/20261004-080257-t03/lecture.json` ; `P-NM` `docs/notes/note-mathematique-lemme-theoreme-v3.md` ; `P-EA` rapports de niveaux 1 et 2 de T0.2 (`docs/etat-de-l-art/`) ; `P-6`, `P-7`, `P-8` préenregistrements de T0.6, T0.7, T0.8 scellés et contre-lus ; `P-V6` verdict scellé de T0.6, ligne « établi » pour la famille lue ; `P-EP` épisodes de T0.6 empreintés avec manifeste ; `P-P4` verdict de P4-instrument ; `P-L7` lectures de T0.7 sur (i) et (ii), liste d'épisodes empreintée ; `P-B4` sorties scellées de T0.8 ; `P-G1`, `P-C` textes scellés et contre-lus de G1 et du papier C ; `P-PIL` fichier réel du pilote de la couche 2 ; `P-ARR` règles d'arrêt P-14 et mode tenu à l'écart P-11 scellés (DP l. 89-92).

| réf | travail (v1) | critères | produits | sert | cl. | source (chemin, ligne) |
|---|---|---|---|---|---|---|
| W01 | T0.1 : socle, registres, passations, rapport de porte, verdicts de porte (W1) | — | — | — | I | B l.108-124 ; G l.409-411 |
| W02 | Veille hebdomadaire, lecture des pistes signalées (W3) | — | — | — | I | B l.346-348 |
| W03 | Collisionneur : rédaction des questions ; lancement = dépense sur GO (W4) | — | — | — | I | D l.664 (GO-07, 15 USD) |
| W04 | T0.2 références : PDF, empreintes, statuts, table des chiffres, script sain et artefact, documents hors arXiv (Panin, PDF attendu de Lazar), références entrées depuis le niveau 2 (W2) | — | — | 8 | I | B l.126-135 ; G l.356-362, l.484-486 ; E l.41 |
| W05 | T0.2 contrôle de traçabilité par sous-agent neuf, texte scellé de G1 (W2) | 6 | P-G1 | 8 | K | G l.358-359, l.485 ; E l.41 |
| W06 | T0.2 contrôle de traçabilité par sous-agent neuf, texte scellé du papier C (W2) | 7 | P-C | 8 | K | G l.358-359, l.485 |
| W07 | T0.2 : rédaction du message de demande d'accès à FakeLab ; l'envoi est W38 (W2) | — | — | — | I | B l.133 ; CLAUDE.md « contact externe » |
| W08 | T0.3 : note mathématique et figures tirées de la lecture scellée du run `20261004-080257-t03` (W6) | 5 | P-T03 | — | K | B l.144 ; G l.458 |
| W09 | T0.3 : tout nouveau run ou rejeu de simulation, toute modification du code des agrégateurs (W6) | — | — | 5 | R | G l.303-306 ; D l.34 (R-025 : un rejeu change la preuve) |
| W10 | T0.4 : revalidation du harnais sur modèle réel, version nouvelle de préenregistrement (W7) | — | — | 1 | R | B l.146-152 ; G l.163-181 ; E l.43 |
| W11 | T0.5 : lecture et verdict du pilote 8B, vérité terrain, plan B de rubrique (W8) | 1 | P-T04 | — | K | B l.154-158 ; E l.44 |
| W12 | P4-instrument : contrôle positif de l'instrument, ≈ 1,5 à 1,8 USD (nouveau) | 1 | P-T04 | 3 | K | G l.236-237 ; D l.464, l.471 (R-262, R-268) |
| W13 | T0.6 : rédaction, contre-lecture, scellement du préenregistrement ; consignes ; données de distillation (W9) | — | — | 2 | I | B l.160-164 ; G l.196-201 ; E l.45 |
| W14 | T0.6 : runs de (i), (ii), contrôles croisés, recherche de dose, dose-réponse (W9) | 1 | P-T04, P-6 | 2 | K | B l.160-164 ; G l.474-476 |
| W15 | T0.7 : apprentissage des sondes sur données génériques, choix sur validation générique, témoin lexical (W10) | 1 | P-T04 | 3 | K | B l.166-173 ; T7 l.9-12, l.65 |
| W16 | T0.7 : lectures du critère 3 (T7-P1 à P4) sur (i-a), (ii), témoin instruit, par famille (W10, W11) | 1, 2 | P-T04, P-V6, P-7, P-P4, P-EP | 3 | K | G l.235-238 ; T7 l.65-68 |
| W17 | T0.7 : lectures descriptives (T7-P5 à P10) sur les épisodes de T0.6 (W11) | 1, 2 | P-T04, P-V6, P-7, P-EP | — | K | T7 l.4, l.69-74 (« sans effet sur le critère 3 ») |
| W18 | T0.8 : invites, planchers, TRACE-lite, préenregistrement (traits fixés avant lecture) : rédaction et contre-lecture (W12) | — | — | 4 | I | B l.175-178 ; G l.261-268 ; E l.48 |
| W19 | T0.8 : run des bases sur les épisodes de T0.6, liste d'identifiants identique à celle de T0.7 (W12) | 1, 2, 3 | P-T04, P-V6, P-L7, P-8, P-EP | 4 | K | G l.270-272, l.468 ; B l.175-178 |
| W20 | G1 : rédaction et contre-lecture du préenregistrement, sans scellement (W14) | 5 | P-T03 | 6 | K | B l.141 et l.214-217 (déduit : les bras séquentiels emploient les agrégateurs de T0.3) ; G l.482-483 ; PG l.1-4 |
| W21 | G1 : scellement du préenregistrement (W14) | 2, 3, 4, 5 | P-V6, P-L7, P-B4, P-T03, P-PIL | 6 | K | G l.468-469 ; B l.214-217 ; PG l.20 |
| W22 | Couche 2 : conception, code, banc synthétique, simulations de la garde δ (rapports v1 à v6), dimensionnement (W15) | — | — | 6 | I | PC l.99 ; PG l.1-4 ; D l.667 (R-453 (3)) |
| W23 | Couche 2 : pilote réel sur seize tâches de réserve, tranche 0 puis pilote, devis P-27 (nouveau) | 1 | P-T04, P-ARR | 6 | K | DP l.40, l.89-92, l.128 ; PG l.20 |
| W24 | Couche 2 : banque pleine, sentinelle GO-03 (W22) | — | — | — | F | DP l.40 ; PC l.99 ; R1 (d1 : la fabrication cite le préenregistrement de G1) |
| W25 | Papier C : préenregistrement de HC1 à HC3 — rédaction, lecture de Panin, contre-lecture, scellement (W17) | — | — | 7 | I | B l.180-188 ; G l.339-343 ; E l.49 |
| W26 | Papier C : pilote, GO-2026-10-17-01 (W18) | — | — | — | F | E l.49 ; B l.180 (d1 : manifeste citant le préenregistrement) |
| W27 | Papier C : TC.1 à TC.6, porte GC (W24) | — | — | — | F | B l.252-284 (d1, d2) |
| W28 | Papier A : cadre, énoncés, travaux connexes, hors résultats de la phase 1 (W19) | 5, 8 | P-T03, P-NM, P-EA | — | K | B l.144, l.335-336 |
| W29 | Papier B : conception et rédaction hors expérience, dont H9 sous réserve d'antériorité (W20) | 8 | P-EA | — | K | B l.336 ; D l.530 (N-035) |
| W30 | G1 : T1.2, lecture, porte G1 ; phase 1 : T1.1 à T1.7 (W22, W23) | — | — | — | F | B l.207, l.214-219, l.241-246 (d2) |
| W31 | Phases 2 et 3, G2, G3, papier B : toute expérience (W25) | — | — | — | F | B l.288, l.310 (d2) |
| W32 | P3 : addendum 2 (N-025), lentilles sur les sondes de P3 : analyses de pièces déjà scellées (W13) | — | — | — | I | D l.457, l.652, l.664 ; G l.455 |
| W33 | P3b : nouveau run (R-262 (2)) (W13) | 1 | P-T04 | — | K | D l.464, l.473 |
| W34 | Pôle (l'organisme), course d'idéation : code, devis, essais hors ligne (v44 à v46) ; course réelle = dépense sur GO, § 8.1 (W16) | — | — | — | I | DV l.1-5 ; D l.663, l.665, l.669 |
| W35 | Pôle, tour (c) « outils clôturés » : code v46, essais hors ligne ; épreuve réelle courte = dépense sur GO (W21) | — | — | — | I | TC l.143 ; D l.646, l.671 (R-432, R-457) |
| W36 | Pôle, moissonneur : conception, code, essais hors ligne ; première moisson réelle sur GO, jetons ≈ 0,4 USD par course (W5) | — | — | — | I | MO l.116-118, l.156-160, l.178 ; D l.650-651, l.656 |
| W37 | Pôle, autres pièces : corpus primaire v5, orchestrateur, mesures de convergence, garde de sûreté, squelette H-E13 ; documents demandés par Lazar hors phase (candidature, entretien du fonds) | — | — | — | I | D l.645, l.653, l.659, l.661-662 ; E l.85-95 |
| W38 | Soumission, publication, contact externe (envoi FakeLab), libération, dépôt public | — | — | — | H | B l.340-342 ; CLAUDE.md « nœuds de décision » |
| W39 | Tout travail absent de cette table (W26) | — | — | — | F | L7 |

## 4. Règle de lecture mécanique (v1 § 4 gardée, étendue aux classes R et N)

- **L1** Une ligne F est fermée. **L2** Une ligne K est ouverte si sa condition est remplie : option (a), aucun critère de sa colonne « critères » n'est dans N ; options (b) et (c), tous les produits de sa colonne « produits » existent à la date d'usage ; sinon fermée. **L3** Une ligne R est ouverte si au moins un critère de « sert » est dans N ; sinon fermée. **L4** Une ligne I est ouverte.
- **L5** Toute ligne ouverte travaille sur processeur local, sans dépense externe. Elle peut demander un devis (nœud de dépense, GO de Lazar) seulement si « sert » contient un critère de N. **L6** Toute dépense externe d'une ligne ouverte dont « sert » ne contient aucun critère de N est un nœud : la clause ne la permet pas. Tout lancement qui exige déjà un GO (première moisson réelle, épreuve réelle du tour (c), course sur devis) l'exige encore. **L7** Une ligne H est décidée par Lazar ; un travail absent de la table est F ; aucun reclassement après le verdict ; deux critères dans N : union des fermetures.

Lecture inverse, pour contrôle (recalculée par script sur le présent fichier, ligne à ligne : les 39 lignes ont été relues, aucune divergence).

| critère dans N | lignes K fermées (option (a)) | lignes R ouvertes | lignes qui peuvent demander un devis (si leur condition est remplie) |
|---|---|---|---|
| 1 | W11, W12, W14, W15, W16, W17, W19, W23, W33 | W10 | W10 |
| 2 | W16, W17, W19, W21 | aucune | W13, W14 |
| 3 | W19, W21 | aucune | W12, W15, W16 |
| 4 | W21 | aucune | W18, W19 |
| 5 | W08, W20, W21, W28 | W09 | W09 |
| 6 | W05 | aucune | W20, W21, W22, W23 |
| 7 | W06 | aucune | W25 |
| 8 | W28, W29 | aucune | W04, W05, W06 |

Options (b) et (c) : même calcul sur la colonne « produits » (un produit absent ferme les lignes K qui le citent ; `P-T04` ferme les mêmes neuf lignes que le critère 1). Cas cumulés (union, L7) : N = {2, 3, 4} ferme W16, W17, W19, W21 ; N = {2, 6} ferme W05, W16, W17, W19, W21. Les lignes F (W24, W26, W27, W30, W31, W39) et H (W38) ne bougent pas. Script : `/tmp/claude-0/-home-claude/be74bc5f-030c-58ad-8f83-cdf5edf47ca3/scratchpad/td2/inverse.py` (lit ce fichier, vérifie aussi que chaque critère cité a son produit dans la colonne « produits » et que les colonnes concordent avec la classe).

## 5. Décision pour Lazar (D-TD-1) — nœud : elle fixe la mécanique de la clause

**Décision.** Pendant le report, un travail conditionnel s'ouvre-t-il selon les critères non tenus au verdict du 30 novembre (N figé), ou selon l'existence des produits scellés dont il dépend, et N est-il relu une fois à mi-report ?
**Enjeu.** Sous (a), dès que deux critères de la chaîne 2, 3, 4, 6 sont dans N, le second verdict ne peut pas être « franchie » : le plus tardif des deux a une ligne de travail fermée jusqu'au 31 janvier (W16 pour 3, W19 pour 4, W21 pour 6). C'est une propriété de l'ordre 2 → 3 → 4 → 6 (grille l. 468-469), non un défaut de rédaction. Au 29 octobre, ces quatre critères sont ouverts (E l. 36-50).
**Options.**
- **(a) N figé ; dépendances sur critères.** Avantage : une seule lecture de la porte, aucun test de produit, table et porte ne divergent jamais. Inconvénient : la chaîne 2 → 3 → 4 est bloquée pendant tout le report ; le report ne sert que 2 et les critères sans chaîne (5 à 8).
- **(b) Dépendances sur produits scellés ; N relu une fois au 31 décembre 2026** (lecture R13 partielle, critères de N seulement, sur GO). Avantage : la chaîne avance dès que le verdict scellé de T0.6 existe ; les droits de devis se resserrent sur les critères encore non tenus. Inconvénient : seconde lecture de la porte alors que la grille n'en prévoit qu'une (l. 89-94), donc risque de « G0 bis » ; coûte un verdict et un GO ; la table suit le produit même si le lecteur de G0 a jugé le critère non tenu.
- **(c) Dépendances sur produits scellés ; N figé.** Avantage : comme (b), sans seconde lecture. Inconvénient : des droits de devis demeurent attachés à un critère devenu tenu (chaque dépense demeure un GO de Lazar) ; même divergence possible entre table et porte.
**Recommandation.** (c), confiance 0,5 : ne pas rouvrir la lecture de la porte ; la divergence est signalée au verdict sans rien fermer. Confiance basse parce que le test « verdict de T0.6 établi, par famille » suppose D-G0-8 (verdict scellé par critère empirique, grille l. 149-153), non décidé.
**Défaut sous 48 heures** (≈ 31 octobre 2026, 12:00 UTC) : (c) comme version de travail seulement ; la table n'est scellée qu'avec le mot de Lazar.

## 6. Application

- **6.1 Qui applique.** Le sous-agent de verdict R13 de G0, dans le même verdict scellé : à la « Forme du verdict » (grille l. 409-411) s'ajoute une feuille de repli (option retenue, N, puis une ligne par réf. : ouvert, fermé ou droit de devis, avec le critère qui le fonde). Calcul par un script de lecture de la table, à écrire avec essais sain et artefact (R5) : il n'existe pas à cette v2. Le lecteur copie le calcul, ne classe rien. Lazar donne le GO du verdict (avis l. 26).
- **6.2 Verdict interrompu.** Si la lecture s'arrête sur la liste d'arrêt (grille l. 413-424), il n'y a ni verdict ni N : la table n'est pas appliquée (« un arrêt n'est pas une lecture », l. 424) ; les lignes F demeurent fermées, les autres ne sont ni ouvertes ni fermées par la table. Cas non traité : § 8.3.
- **6.3 Dépenses pendant le report.** Règle unique L5-L6, alignée sur l'avis (l. 42-46) : seules les tâches qui servent un critère de N demandent un devis, chacune sur GO ; les travaux indépendants continuent sur processeur ; une dépense pour un travail indépendant est un nœud. La table ne crée aucun GO ; un GO consigné avant le verdict garde son objet et son plafond (§ 8.1).
- **6.4 Pendant le report.** Aucune ligne n'est reclassée ; une pièce nouvelle (R12) appartient à la ligne de la pièce dont elle est une version ; un travail sans ligne est F ; pas de second report.
- **6.5 Clôture au 31 janvier 2027, 23:59 UTC.** Second verdict R13. « Franchie » : la table cesse de s'appliquer, la phase 1 ne s'ouvre que sur GO. Sinon, phase 0 close « non franchie » : toute ligne cesse, sauf (i) W01 limitée au rapport de porte scellé, à la passation et à l'état (R14) ; (ii) l'arrêt par identifiant des instances en marche et sa consignation (R10). « Cesser » = aucun nouveau run, aucune session de modèle, aucun nouveau scellement hors (i). Les pièces scellées demeurent ; toute reprise passe par une version nouvelle du programme (nœud, avis l. 45-46).

## 7. Audit de symétrie R4 (CT-10)

- **Règle d'affectation, la même pour toute ligne.** (A1) « critères » : seulement si une source citée écrit que le travail lit ou exige un produit du critère ; (A2) « sert » : seulement si une source citée écrit qu'il produit une preuve du critère ; (A3) F seulement si le brief écrit un préalable « G0 franchie » / « G1 prononcée » / « G2 franchie » (l. 207, 288, 310) ou si d1 ou d2 s'applique ; K si « critères » est non vide ; R pour un second jeu de preuve ; I sinon ; (A4) ni la date de création ni l'état d'avancement d'un travail n'entrent dans l'affectation. Chaque cellule non vide renvoie à une source (colonne « source »). Deux cellules sont des déductions et le disent : « critères 1 » (le harnais de T0.4 produit les épisodes et les activations de tout run ultérieur, B l. 146-152) et « critères 5 » de W20.
- **Test de retrait.** Sans les travaux du 29 octobre (W03, W22, W23, W32 pour les lentilles, W34 à W37), les autres lignes ont les mêmes classes : chaque ligne ne dépend que de ses sources, jamais des autres lignes. Seule exception : W21, dont le produit `P-PIL` vient de `PG` (29 octobre) ; sans lui W21 garde ses critères 2, 3, 4, 5 (G l. 468-469) et sa classe K. Réciproquement, ces lignes reçoivent par (A1)-(A4) « critères — » et, sauf W22 et W23 (« sert 6 » : source `PG` l. 1-4 et l. 20, datée du 29 octobre), « sert — » : leur continuité est donc sans droit de devis.
- **Sens des changements v1 → v2** (numéros de la v1 entre parenthèses dans la colonne « travail »). Resserrés, douze : « sert » sans source retiré pour v1-W5, v1-W16, v1-W19, v1-W20, v1-W9 (3, 4) et v1-W1 ; critère 2 ajouté à v1-W10 ; 2 et 3 à v1-W12 ; 2, 3, 4 au scellement de G1 (v1-W14) ; 6 et 7 à la traçabilité (v1-W2) ; rejeu de T0.3 passé en R (v1-W6) ; pilote du papier C passé en F (v1-W18). Assouplis, trois : tour (c) (fermé par défaut → I, sur `TC` et `D` l. 646) ; P3 (« dépend 3 » retiré, W33) ; couche 2 (« dépend 5 » retiré, aucune source). Tous sourcés.
- **Contrôle « trop propre ».** La v1 laissait le travail courant presque intact (v1 § 6). En v2, sous (a), N = {2} ferme W16, W17, W19, W21 ; N = {1} ferme les 9 lignes qui citent 1 ; les travaux du pôle (W34 à W37) continuent dans tous les cas mais ne gagnent aucun droit de devis. L'audit ne cherche pas l'équilibre, il vérifie que chaque affectation a sa source et que l'effet est lisible dans le § 4.

## 8. Contradictions et points restants (signalés, non masqués)

1. **GO antérieurs.** L'avis (l. 42-44) dit que « seules » les tâches des critères non tenus peuvent dépenser ; la course d'idéation (W34) a des GO déjà consignés (D l. 669) pour 52,8 USD. La v2 les laisse valides jusqu'à leur plafond (6.3) ; toute dépense nouvelle de W34 à W37 après le verdict est un nœud. Si la clause veut plus strict, elle doit le dire.
2. **Date de scellement.** L'avis (l. 55) interdit toute modification de la clause après le 1er novembre ; la grille propose le 15 novembre pour elle-même (D-G0-1). La date limite de la dernière version de la table n'est pas fixée ici.
3. **Arrêt non levé au 30 novembre.** Ni verdict ni N : la clause se tait sur le déclenchement. Décision de Lazar (elle modifie la clause).
4. **W21 (scellement de G1).** Le brief ne demande pas 2, 3, 4 pour sceller (critère 6 : « scellé et contre-lu ») ; la grille (l. 468-469) les place avant « si G1 cite les instruments », ce que B l. 214-217 fait. Conséquence : sous (a), critère 6 inatteignable si 2, 3 ou 4 est dans N. Variante possible : produits `P-6`, `P-7`, `P-8`, `P-PIL` seulement.
5. **W19 (« 3 avant 4 »)** vient de la grille (l. 468, avis Fable, pièce non lue ici) ; le brief est muet. Variante : critères 1, 2 seulement.
6. **W26 (pilote du papier C)** est fermé par d1 bien que le brief le nomme « pilote sur GO » (l. 180). Variante : ouvert si 1 et 7 sont tenus. Le choix change la clause (« aucune expérience décisive du papier C »).
7. **Lien non établi** entre le pilote de la couche 2 (W23) et l'étape 1 de P-015 (recherche de dose, G l. 474-475) : si c'est le même travail, W23 gagne « sert 2 ».
8. **Date du report.** L'avis écrit 31 décembre ; R-452 (D l. 666) fixe le 31 janvier 2027 ; la v2 applique le 31 janvier. L'avis n'a pas été réécrit.
9. **Script de lecture** (6.1) inexistant ; les tables du § 4 ont été recalculées par un script jetable du bloc-notes, non versé.
