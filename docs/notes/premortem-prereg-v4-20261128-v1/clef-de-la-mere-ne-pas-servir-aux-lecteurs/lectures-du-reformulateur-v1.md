# Lectures et calculs du reformulateur (pour `registres/qui-a-lu-quoi`) — 28 novembre 2026

Agent : Claude Fable 5.2 (`claude-fable-5-2`), agent neuf lancé par la session mère `session_01QPDgKfh86KrPUDxcz8M1GQ`. Rien écrit dans le dépôt, aucun commit.

## Lu en entier
- `CLAUDE.md`
- `registres/passations/passation-claude-session-mere-v4-20261128.md`
- `registres/contre-lectures/mandat-r2-et-pieces-auditees-20261128.md`
- `registres/contre-lectures/contre-lecture-r2-etages-1-2-20261128-v1.md` (sections 1 à 3 et début de la section 4 ; code de la section 4.2, seconde partie)
- `registres/contre-lectures/contre-epreuve-r2-volets-11-13-20261128-v1.md`
- `registres/contre-lectures/attestation-execution-r5-etages-1-2-20261128.md`
- `src/controle_ia/prereg.py` ; `prereg/gabarit-preregistrement-v1.md` ; `src/controle_ia/environnements/propositions.py`
- `docs/decisions/decision-N-054-v1.md`, `decision-N-055-v1.md`, `decision-N-056-v1.md`, `decision-N-062-v1.md`, `decision-N-063-v2.md`, `decision-N-060-v3.md` (début)
- `registres/go.md` : lignes GO-2026-11-28-01 à -03, GO-2026-11-05-07, GO-2026-11-18-48

## Lu en partie
- `registres/contre-lectures/verif-p8-hors-depot-20261128.txt` : titres des cinq sections et premières lignes
- `tests/test_oracles_r5_cloture_etages_1_2.py`, `tests/test_contre_epreuve_v4_r5.py` : imports, et le code recopié dans les deux rapports ; exécutés (18 essais passent en 4,24 s)
- `prereg/G0-critere-3-designation-course-v1.md` : en-tête, sections 0 à 2, « Hypothèse » à « Écarts déclarés »
- `prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md` : titres, lignes DR-6 et DR-11
- `brouillons/G1-preenregistrement-v1-brouillon6.md` : en-tête, table des treize décisions, résumé en dix lignes, titres
- `prereg/formulation-g1-simulation-v1.md` : en-tête, titres ; `docs/verdicts/verdict-formulation-g1-simulation-v1.md` : douze premières lignes
- `docs/decisions/decision-N-007-N-008-v1.md` (soixante premières lignes), `decision-N-074-v1-brouillon2.md` (seize premières lignes), `decision-N-076-assurance-par-audit-et-reference-honnete-v1.md` (en-tête, § 2)
- `docs/programme-controle-ia-v3.md` : § 5 (papier A), § 6, § 7, § 8, § 10 (phase 1), § 13
- `registres/etat.md` : trente premières lignes
- `src/controle_ia/t06/cout.py` : signatures et docstring
- Au commit `42cdfcf29`, par `git show` : `src/controle_ia/dose_reponse/conditions_v1.py` (docstring, signatures), `course_v3.py` (signatures), `prereg/T0.6-dose-reponse-configuration-course-v2.json` (clés, valeurs tronquées à 160 signes), `runs/20261125-093202-dose-reponse/manifeste.json` (clés, versions), `registres/dose-reponse-v1.md` (recherche de mots, rien affiché), les `textes.jsonl` et `mesures.jsonl` des 64 blocs (par programme ; un extrait de mesure et aucun texte d'action affiché en entier), `bloc.json` du bloc 0
- `diag/20261006-134235-t05-corpus/tirage.json` (clés, longueur, exemples d'identifiants) ; `taches-banque.json` de la branche `origin/banque/dose-reponse-consigne-cachee-v1` (identifiants, remplacements) ; `diag/20261126-082824-dose-reponse-lecture/lecture-cout-dose-reponse.json` (clés, table « manipulation » de quatre conditions)

## Calculé sur données réelles (course 20261125-093202-dose-reponse, textes et mesures seulement)
- `sondage_validateur_v2.py` (`e7d864d0…`) → `sondage_validateur_v2-sortie.json` (`d7111e51…`) : acceptation au premier tirage du validateur d'action de la contre-épreuve (volet 12, § 1), avec le vrai `propositions.appliquer`, par condition, tâche, pas et prédicat.
- `formes_cout.py` : formes du champ de coût (chiffres remplacés) et mots interdits du champ de prédiction, pour `honnete`, `consigne_neutre`, `gonfle_5`.
- `verif_sondage.py` : contrôle du sondage sur les actions honnêtes rejetées (première ligne, motif d'invalidité).
- `temoins.py` : recalcul des parts de `mention_texte_prive` et des effectifs, comparés à `lecture-cout-dose-reponse.json`.
- Rangs de `taches-banque.json` dans `tirage.json` : rangs 126 à 211 (base 1), 22 rangs examinés non retenus, premier rang libre 212.

## Jamais ouvert
Aucun `*.npz`, aucun `*.safetensors`, aucun poids, score, plancher ni verdict de sonde ; aucune consigne privée (`consignes-privees-*.json`, `prereg/P3-consignes-v1.md`, `brouillons/ii-b-saboteur-budget-v1/`) ; rien du commit `5817bb0a5` ; aucune pièce d'un mode tenu à l'écart.

## Complément
- `temoin_illisibles.py` : le témoin T1 est bien posé — `cout_lisible` (de `src/controle_ia/t06/cout.py`, lignes 41 à 58 lues) appliqué au champ `cout` de `mesures.jsonl` rend 257 (`honnete`), 268 (`consigne_neutre`), 227 (`gonfle_3`), 211 (`gonfle_5`), comme le résultat scellé ; le compte naïf « coût absent » rend 247 et 264.
- Les décisions N-054, N-056, N-062, N-063 v2 ont été lues avec des lignes tronquées à 2 200 ou 3 000 signes à l'affichage ; N-060 v3 : quarante premières lignes.
- Noms de fichiers listés sans ouverture : `brouillons/`, `docs/decisions/` (extraits), `docs/verdicts/` au commit `42cdfcf29`, `registres/contre-lectures/`.

## Après le complément 2 de la mère (pièces versées au commit `e702bf76f`)
- Lu en entier : `brouillons/prereg-v4-c-furtif-g1/G0-critere-3-additif-c-furtif-v1-brouillon-gemini-1.md` (`94913179…`), `G1-architecture-h1-h2-v1-brouillon-gemini-1.md` (`887795c4…`), `arbitrages-GO-2026-11-28-01-a-03-texte-gemini-v1.md` (`14e52399…`) ; empreintes égales aux compagnons.
- `versement-gemini-non-commis-20261128-v1.md` : 600 premiers octets et titres seulement.
- `LISEZMOI-versement-gemini-v1.md` : **non ouvert** (réservé à la mère) ; je n'en connais que les deux constats cités par son message.
- Programmes : `controle_ia.prereg.problemes` sur les deux brouillons (rend `[]` pour chacun) ; `empreintes_citees.py` (44 chaînes hexadécimales distinctes dans les trois pièces ; 42 de 64 signes, dont 41 retrouvées ailleurs dans le dépôt comme chaînes et une absente, `59a2a571…` ; une de 40 signes ; une de 65 signes, `76cdeace…`, dans le brouillon de la porte de fin de phase 1) ; contrôle que les expressions régulières du validateur du brouillon de l'additif sont, signe pour signe, celles de mon sondage.
- Recherche de mots dans les trois pièces : aucune mention de DG1, GO-2026-11-05, GO-2026-11-18, N-007, N-008, N-055, N-060, N-062, N-074 à N-077, « programme », « flou », « pari », « toujours valide » ; décisions citées : N-026, N-029, N-053, N-054, N-056, N-063.
- Fichiers de ce sous-dossier : `clef-v1.md` (clef des témoins et sondage), `sondage_validateur_v2.py` et sa sortie, `formes_cout.py`, `verif_sondage.py`, `temoins.py`, `temoin_illisibles.py`, `empreintes_citees.py` et `motifs-empreintes.txt`.
