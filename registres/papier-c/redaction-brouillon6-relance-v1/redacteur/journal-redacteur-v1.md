# Journal du rédacteur du brouillon 6 de relance du préenregistrement du papier C — v1

Rédacteur neuf (sous-agent, Claude Fable 5.2), sous le mandat `cfe4a3c3…` et la consigne
`bloc-notes/mere/consigne-redacteur-brouillon6-relance-v1.md`. Heures UTC relevées par `date -u`, le 2026-11-19.
Aucun écrit hors de `bloc-notes/redacteur/`. Dépôt intact (`git status` vide en fin de travail). Aucun refus de
permission. Aucune dépense, aucun appel à un modèle, aucun autre agent, aucune suite d'essais lancée.

## Déroulé
- 11:04 — consigne, mandat, gabarit, validateur lus ; empreinte du brouillon 5 conforme (`9d55160f…`, 97 194 octets).
- 11:04 à 11:12 — décisions lues, chacune égale à son compagnon ; registres lus par lignes ciblées (ligne R-2059
  filtrée par le programme `travail/chercher_v1.py`) ; archive lue par l'inventaire, puis les tables de traitement ;
  état de l'art de niveau 3, section 4 à 7 ; quatre rapports de lecteurs lus sur leurs branches (`git fetch`, puis
  `git show`, sans changer de branche).
- 11:12 à 11:25 — en-tête et 65 changements du corps écrits ; texte construit par programme, premier passage sans
  échec d'ancre ; validateur lancé.
- 11:25 à 11:30 — note des différences, liste des décisions, ce journal.

## Pièces lues (empreintes recalculées)
- `registres/papier-c/mandat-redaction-preenregistrement-papier-c-v1.md` `cfe4a3c3…` ; `CLAUDE.md` `5978d409…`.
- `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md` `9d55160f…` (en entier).
- `prereg/gabarit-preregistrement-v1.md` `8cad4371…` ; `src/controle_ia/prereg.py` `3b2e3ee5…`.
- `docs/decisions/` : N-005 et N-006 `cd49afbc…`, N-013 `157d388e…`, N-053 `2204256d…`, N-064 `387c9d4e…`, N-065
  `f820e90d…`, N-066 `21e83ed5…`, N-068 `ba6b2db3…` (en entier). N-023 `1297f509…`, N-067 `966dd9dc…`, N-071
  `9700fe6f…`, N-073 `b95688df…` et ses compléments : empreintes vérifiées, lus par recherche des passages qui nomment
  le papier C ou un préenregistrement, pas en entier.
- `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md` `e30a013d…` (en-tête, sections 1, 4, 5, 6, 7).
- `docs/programme-controle-ia-v2.md` et `docs/brief-claude-code-programme-complet-v2.md` : empreintes de lancement
  conformes ; lus par les lignes qui nomment le papier C, HC1 à HC6, EC, TC, GC, T0.9, G0.
- Branches : `rapport-lot1-HC2-mirage-karne-v1.md` `9996f40c…` (§ 1.5, § 3) ; `rapport-lot3A-…` `64b728d6…` (§ 5, § 7,
  § 10.5) ; `rapport-lot7C-…` `2b03ede0…` (§ 7) ; `rapport-C9-…` `23ec1f6e…` (§ 3.6, § 6). Copies sous
  `travail/lus-sur-branches/`.
- Registres, lignes ciblées : `registres/decisions.md` `8a46e225…` (P-019 à P-022, R-307 à R-309, R-312, R-316, R-326,
  R-2180, R-2553 à R-2555, R-2571) ; `registres/go.md` `d061f9fa…` (GO-2026-10-04-08, -10-17-01, -10-20-06, -07, -09,
  -11-18-01, -11-19-41) ; `registres/etat.md` (lignes qui nomment P-020 à P-022).
- Archive de la session 16 (matière première) : inventaire ; `traitement-contre-lectures-brouillon5-papier-C-v1.md` ;
  tables de traitement des brouillons 6 (`74b5ae16…`) et 7 (`351ab375…`) ; brouillon 7 (`541f1511…`) lu par sa
  différence avec le brouillon 5 (`travail/diff-b5-b7-corps.txt`, 63 blocs) et par ses sections « Prédiction » et
  « Métrique » ; plan de la contre-lecture « méthode » du brouillon 5 (`0c492f02…`, titres des constats seulement).
- `brouillons/papier-C-config-v1-brouillon2.json` `77252564…` : clés, fentes et longueurs seulement ; aucun texte de
  consigne affiché ; `prereg/T0.5-pilote-8B-v1.md` : recherche des mots « outil » et « tool » seulement.

## Ce que je n'ai pas lu ou pas pu lire
- Rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; rien de nommé « consigne-privee » ou « conception-ii-b » ;
  pas la branche `lot/compte-4-v1` ; pas la ligne R-2059.
- Le brouillon 6 de l'archive (lu par sa table seulement) ; la configuration brouillon 4 de l'archive ; les notes de
  voisins de l'archive ; les sorties des simulations T2 à T5 et U1 à U3 ; la contre-lecture « texte » du brouillon 5
  (absente de l'extrait, présente dans l'archive du 20 octobre).
- Aucun PDF. Les pages citées viennent de N-068, de l'état de l'art de niveau 3 et des quatre rapports nommés.
- La note de recentrage du papier C sur l'opposition juge contre sonde (R-2555, option D) : non trouvée au dépôt.
- `prereg/P3-consignes-v1.md` : cité, non lu (comme au brouillon 5).

## Doutes
1. Les taux simulés cités d'après les deux contre-lectures de méthode de l'archive (0,081 à 0,136 ; 0,243, 0,117,
   0,028 ; etc.) sont recopiés du brouillon 7, non rejoués et non relus sur leurs sorties.
2. La ligne C-P4c, l'audit A9, le témoin lexical, le masque de la lecture filtrée et le seuil « moitié » de la réserve
   de contrôlabilité sont de ma conception : aucune mesure de puissance ni simulation ne les appuie.
3. Le témoin lexical suppose qu'une relecture forcée dans le contexte honnête est possible avec les sondes en ligne
   de P3 ; je n'ai pas lu le harnais.
4. « Aucun outil dans l'environnement (a) » repose sur une recherche de deux mots dans un seul fichier.
5. La moyenne glissante sur 5 jetons en bras de diagnostic : N-026 permet un bras « moyenne » ; j'étends cette
   permission à un maximum de moyennes glissantes. À confirmer (D-14).
6. Avec k_P niveaux, la moyenne Ḡ_P peut masquer un déplacement au niveau le plus fort ; j'ai mis une réserve, pas un
   critère.
7. Les empreintes abrégées reprises du brouillon 5 pour des pièces non versées (mesures, simulations S0 à S8) n'ont
   pas été recalculées : les fichiers ne sont pas dans l'extrait.
8. Le texte fait 150 891 octets, contre 97 194 : l'en-tête (verrous, documents) en porte une grande part.
