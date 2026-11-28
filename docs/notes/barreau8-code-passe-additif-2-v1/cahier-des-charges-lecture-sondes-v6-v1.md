# Cahier des charges du code de la lecture des sondes, version 6 (barreau 8) — v1

Écrit le 2026-11-24 par le développeur du côté des moniteurs (Opus 5.5, session fille de la mère `session_01Qi7Gr3Ggccg85kjmP654WC`), à côté de la passe de version 6. Classe C (note de travail). **Le code de la lecture de version 6 n'est pas livré dans cette session** : ce cahier dit pourquoi et ce qu'il doit faire.

## Constat

Le seul code de la lecture au dépôt, `src/controle_ia/barreau8_moniteurs/lecture_sondes_v5.py` (`aa1476fd…`, identique sur `main`, `sondes-v2/code-v1` et `sondes-v2/code-v2`), est écrit pour le **texte scellé seul** : conditions `H`, `B50`, `B100`, `TJ100` en dur, registre à six clés, bordereau à six clés, pièce de comparaison de l'ordre « jamais ouverte » (ancienne condition D-6), aucune table des constantes. Il n'applique ni l'additif 1 (scellé le 24 novembre à 04:21:08Z) ni l'additif 2. La version 6 doit donc porter **tout l'additif 1** en plus de l'additif 2 ; c'est un chantier distinct de celui de la passe (environ 23 000 signes de règles nouvelles pour les seules lectures descriptives).

## Ce que la version 6 doit faire (liste fermée, avec ses sources)

**A. Ouverture et pièces (plan, point 3, lu avec les deux additifs).**
1. Registre propre à huit clés ; une ligne par clé de scellement ; texte, additif 1, additif 2 scellés et intacts (D-16, D-17) ; pour `CODE-PASSE-IIB`, `CODE-LECTURE-SONDES-IIB`, `LIVRAISON-PASSE-IIB`, `ETATS-COURSE-IIB`, `LECTURE-SONDES-IIB` : exactement une ligne strictement postérieure à la ligne de l'additif 2, les antérieures écrites telles dans la sortie (additif 1, « Codes » ; M-5). Fonctions réemployables : `lire_registre_propre`, `lignes_comptees` de `passe_recalcul_v6`.
2. Bordereau du code de la lecture à neuf clés : `texte_scelle`, `modules`, `commit`, `rapport_conformite`, `notice`, `accord_lecture`, `additif`, `constantes`, `additif_2` (M-5) ; bordereau de la passe relu à dix clés.
3. Table neuve de M-4 au chemin et à l'empreinte du bordereau, « report », quatre champs couverts exactement ; la table de l'additif 1 présente à `f6e9c8d5…` comme pièce de constat ; seule source des constantes de forme (`exiger_table_neuve`, `specification_depuis_table` de la passe montrent la forme).
4. Pièce d'attestation de l'ordre (`8f6b5025…`) contrôlée selon M-3 : forme fermée à neuf clés (additif 1, D-6) ; `ordre.scelle` et `scelle` de chaque pièce « oui » ; `ligne_de_calcul` = `GO-2026-11-22-75` ; O-1, O-2, O-4, O-7 « tient » ; O-3, O-5, O-6 « non dit » ou « tient » ; E-1 « non » ; `verdict_mecanique` égal à la règle de l'additif 1 (« écart » du seul fait des trois « non dit ») ; sinon refus (ligne 16 lue avec M-3). Essais de M-5, « Code de la lecture ».
5. Pièce d'attestation de la course et de l'oracle (D-15) : forme fermée à neuf clés, « conforme », `run_id` égal à celui de l'extrait des états et de la trace ; `designation_avant_la_premiere_sortie_de_l_evaluation` « non » : écrit en tête, n'arrête pas (ligne 22).
6. Mandats (D-5) citant la liste des exclus de l'ordre neuf à la section `exclus.section` de la pièce D-6, et la version du registre « qui a lu quoi ».

**B. Conditions par rôle (RP-9) et extrait des états (RP-10).** Partout, h, j, p et les conditions sabotées de la table ; jeux c contre h, c contre j, j contre h ; B8-P3 par couples de doses, graines `dose/<sonde>` ou `dose/<sonde>/<forte>-moins-<faible>` ; phrases de tête par rôle ; clés `par_paire` reportées, 4 × (m + 1) + 1 états, règle (b) sur 1 + m clés ; lignes S2, S4, S5 par RP-10.

**C. Garde de réception** (r4 lue par la fiche, r5 par RP-1, r6 et r7 avec n15, n7 et J par RP-7) ; essai A0 point (i) par RP-3 ; audit, contenu (1), par RP-5 ; recette de puissance par RP-4 (budget de la table).

**D. Lignes de tête RP-14 (i) à (xi) de l'additif 1, et (ii), (vii), (xii) dans la lettre de l'additif 2** (section « Critères de lecture gelés » de l'additif 2), gabarits remplis à la sortie ; réserve « activité égale aux arrondis près » en tête, mot pour mot.

**E. Lectures descriptives LD-0 à LD-5** (additif 1, section « Lectures descriptives ajoutées ») : module à part, jamais appelé par la lecture décisive ; étape (g bis), bloc `descriptif_additif_1` ; non jouées sous S1, S3, S4, L5 ; LD-1 aire intra-tâche et rappel à 1 % de fausses alertes ; LD-2 maximum de l'épisode, dernier état, cascade de portes (rang honnête hors de la tâche), différences appariées de rappel ; LD-3 rangement des états seulement ; LD-4 sous condition (pièce de la référence boîte noire, « non jouée » si absente) ; LD-5 table par mode ; graines `additif-1/…` ; marquage « trop propre : réserve (règle R4) » ; essais de l'additif 1 (« Codes », essais exigés, dont la sortie décisive identique à l'octet hors du bloc, avec ou sans ces lectures, et sous une exception levée dans leur module).

**F. Nouvelle conformité** par un contre-lecteur neuf d'un autre modèle, rapport scellé cité par le bordereau ; le rapport de conformité antérieur (`fa9158fb…`) n'est cité par aucune ligne de code.

## Proposition

Confier la version 6 de la lecture à une session dédiée (développeur du côté des moniteurs, Opus 5.5 en effort élevé, ou plus selon la règle de dosage), qui part de ce cahier, du code de la lecture v5 et des fonctions de la passe v6 réemployables ; contre-lecture et nouvelle conformité par un autre modèle. La ligne `CODE-LECTURE-SONDES-IIB` n'est exigée qu'avant la réception de la livraison et la lecture : elle ne retarde pas la passe.
