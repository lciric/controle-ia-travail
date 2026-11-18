# Contre-lecture de l'enveloppe Carbon par lot v3 et du lanceur v12 — version 1

18 novembre 2026. Contre-lecteur neuf : je n'ai écrit aucune des pièces lues. Aucun appel réseau vers un fournisseur ; aucun
port de 8787 à 8792 touché ; aucune fiche ni réponse de juge lue ; aucun cache d'octets créé (vérifié dans le dépôt et dans le
clone de l'orchestrateur).

## Verdicts

- **Enveloppe de gemini-4-carbon par lot** (`rapports/organismes-discrets-v1/enveloppes-v1/appel-carbon-v3.sh`, `9ef03f80…`,
  égale à son compagnon) : **autorisable**. Trois constats mineurs.
- **Lanceur de la troisième course Carbon par lot** (`scripts/lancer_course_ideation_organismes_discrets_v12.py`, `4d7cee15…`,
  non scellé) : **à corriger**. Un constat significatif (la commande épinglée n'est pas celle qui tourne), quatre mineurs.
  Une fois le constat significatif corrigé, autorisable sans autre lecture.

## Ce qui a été vérifié

- Empreintes : commande par lot `commande_gemini_lot_v1.py` `9484dce0…` et relais Gemini v4 `relais_gemini_v4.py` `543e728d…`,
  égales à leurs compagnons ; le lanceur v10 est égal à son compagnon (`c3abd573…`) ; l'arbre de `orchestrator/` au commit
  `a41b7b50` est `ee84d6ec…`, celui que le lanceur épingle.
- Le diff du code entre le v10 et le v12 (corps hors docstring) ne touche que : `VERSION`, les témoins v6 (`07c80a23…`),
  l'enveloppe v3 (`9ef03f80…`), `DELAIS_PAR_LIGNEE["carbon"]`, `DECISION`, et les trois noms de série v12. Rien d'autre.
- Essais : `tests/test_lancer_course_ideation_organismes_discrets_v12.py`, 7 réussis ; essais de la commande par lot
  (`test_commande_gemini_lot_v1.py`), 40 réussis (venv `.venv`, `-B`, `-p no:cacheprovider`).
- Épreuve à sec, par les fonctions du lanceur, sans appel (dossier de travail dans le dossier temporaire de la session) :
  `construire_liste_blanche` (liste écrite et scellée par l'orchestrateur, égale aux trois pièces attendues),
  `commande_mesure` puis `mesurer_consignes` (`sans_appel` vrai), `gardes_de_taille`, `commande_course` et `garde_sommes`.
  Consignes : passe 1 = 11 085 caractères, contrôle externe = 11 560, consigne de juge maximale = 556 213. Toutes les gardes
  tiennent (marges 228 440 et 348 915 caractères ; plancher de la commande externe 0,54 USD au contrôle comme en passe 1,
  sous 1,7 et 1,5). Sommes : Claude 4,2 ≤ 6,0 ; externe 5,9 ≤ 6,5 ; exposition externe d'une course 3,2. La commande de course
  finit par `--delai-commande-s 3600 --delai-session-s 3900`.
- Admission par l'orchestrateur (`verifier_commande_externe_reelle`, `demonstrations/ideation_v2.py` l. 751-783) : le lanceur
  passe `--modele-commande-externe gemini-4-carbon --commande-externe-lit-modele` ; tous les rôles externes (proposeur
  `carbon`, juge différé `carbon-juge`) sont sur `gemini-4-carbon` : aucun écart, admis. La commande par lot lit bien
  `MODELE_DEMANDE_POLE` (l. 147-149) : posé et différent de `--modele`, code 2, rien envoyé. Le contrôle externe passe sous
  `proposeur_ideation` (`pole/ideation_v2.py`, contrôle), rôle admis par le `--roles` par défaut de la commande.
- `--delai-commande-s 3600` et `--delai-session-s 3900` : admis (seule exigence de l'orchestrateur : strictement positifs,
  `ideation_v2.py` l. 1130-1133). Le premier borne `AdaptateurCommandeExterne.lancer` (`pole/adaptateurs.py`,
  `communicate(timeout=…)`, puis SIGKILL du groupe ; sans ligne JSON, le plafond de session est compté).

## Garde du pire cas de la commande sous les plafonds (prix comptés 8,3 / 41,5 USD par million)

Formule de la commande (l. 165-171) : entrée gardée = ⌈max(compte, caractères / 3) × 1,05⌉ ; `maxOutputTokens` =
min(32 768, ⌊(plafond − entrée × 8,3e-6) / 41,5e-6 − 8 192⌋) ; refus sous 4 096. Avec les consignes mesurées (compte supposé
≤ caractères / 3) :

| session | plafond | entrée gardée | `maxOutputTokens` | pire cas |
|---|---|---|---|---|
| proposeur externe | 1,5 | 3 880 | 27 176 | 1,49998 |
| contrôle externe | 1,7 | 4 047 | 31 962 | 1,69998 |
| juge externe différé (consigne maximale) | 2,5 | 194 675 | 13 113 | 2,49996 |

La garde tient sous les trois plafonds ; à 1,5 USD, l'entrée admise va jusqu'à 119 282 jetons. Le coût rendu sur un échec
après création du lot est ce pire cas (≤ plafond) ; sur le code 7 (pensée au-delà de la provision), le coût lu sur l'usage
peut le dépasser : risque déjà déclaré par la commande, identique à celui d'Argon à 8 192.

## Délais

Commande : la boucle teste le délai global avant chaque relevé ; dernier test à 3 300 s au plus, puis attente 30 s, relevé
≤ 120 s, test, annulation ≤ 120 s : **3 570 s au plus**, `countTokens` et création du lot comptés dedans (l'horloge part avant).
Le délai de 120 s par requête est par opération de socket, mais le relais n'écrit au client qu'après avoir lu l'amont : un
relevé muet est coupé à 120 s. Enveloppe : SIGTERM à 3 590 s, SIGKILL à 3 595 s. Orchestrateur : 3 600 s. L'ordre
commande < enveloppe < orchestrateur tient (marges 20 s puis 5 s). Le relais n'a pas de `--delai-amont-s` dans la ligne de
lancement annoncée (défaut 1 800 s) : sans effet ici, chaque requête de la commande étant brève et bornée à 120 s côté client.

## Constats

### Lanceur v12

1. **Significatif — la commande externe épinglée n'est pas celle qui tourne** (l. 207-208, 218, 224). `COMMANDE_GEMINI` reste
   `commande_argon_v3e.py` (`e94ecd46…`) et `LIGNEES_EXTERNES["carbon"]["commande"]` la reprend : `verifier_pieces` vérifie
   l'empreinte d'une commande que l'enveloppe v3 ne lance plus, et le manifeste pré-départ écrira
   `pieces.commande_externe = commande_argon_v3e.py`, ce qui est faux. La commande réellement lancée,
   `commande_gemini_lot_v1.py`, n'est épinglée par **personne** au lancement : l'enveloppe ne vérifie pas son empreinte (comme
   les v1 et v2), et `AdaptateurCommandeExterne.description()` n'empreinte que les arguments qui sont des fichiers (`bash`
   n'en est pas un ; seule l'enveloppe l'est). Provenance trouée (R6, R11). Correction : une constante
   `COMMANDE_GEMINI_LOT = ("docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_gemini_lot_v1.py", "9484dce066514185dc1155d5c8dcff44b256fdf835b371b59ebdffa1d50bad75")`
   pour la lignée Carbon, et un essai qui exige que la commande épinglée soit celle que nomme l'enveloppe. Les gardes de
   taille n'en sont pas faussées : la formule de `plancher_gemini` (l. 753-756) est celle de la commande par lot (mêmes prix,
   marge 1,05, 3 caractères par jeton, 4 096 + 8 192 jetons ; `⌈⌈c/3⌉ × 1,05⌉` ≥ `⌈c/3 × 1,05⌉`, donc plancher prudent), à la
   seule condition, déjà connue, que `countTokens` ne dépasse pas caractères / 3.
2. Mineur — `--delai-session-s 3900` (l. 255-256) est sans effet sur la commande externe : il ne borne que les sessions Claude
   (`AdaptateurClaudeSDK`) et les passes par protocole (`dossier_ferme`, absent ici). La justification « le lot peut durer »
   est donc fausse ; l'effet (sessions Opus bornées à 3 900 s au lieu de 3 600) est sans conséquence d'argent. Le garder par
   symétrie avec Kimi ou le retirer ; dire lequel.
3. Mineur — l. 256 porte deux commentaires collés (`# v12 : … # v9 (…)`) ; docstring l. 126 et docstring de
   `plancher_gemini` (l. 754) parlent encore de la « commande d'Argon » / `commande_argon_v3e.py`.
4. Mineur — l'essai `test_code_egal_au_v10_hors_des_lignes_annoncees` permet toute ligne contenant « enveloppe » : filtre
   large ; il n'aurait pas vu un changement de `COMMANDE_GEMINI` (ni son absence, ce qui est le constat 1).
5. Mineur — `relance_permise` et `garde_cumul` ne lisent que la série v12 ; le cumul avec les courses Carbon des lanceurs
   précédents repose sur le plafond de la ligne de GO neuve (déjà le cas au v10). Aucune ligne « lignée carbon » n'est encore
   au registre des GO : le lanceur refusera tant que la mère ne l'a pas écrite, comme prévu.

### Enveloppe v3

1. Mineur — « Tout est figé après "$@" » (l. 14-15) n'est pas littéral : `--roles`, `--caracteres-par-jeton` et
   `--marge-entree` ne sont pas reposés après `"$@"`. Inatteignable en production (l'orchestrateur lance `bash <enveloppe>` sans
   argument) et leurs défauts (rôles proposeur et juge, 3,0, 0,05) sont ceux que la garde du lanceur suppose ; mais une
   prochaine version devrait les figer aussi.
2. Mineur — l'enveloppe ne vérifie pas l'empreinte de la commande qu'elle lance (comme v1 et v2) ; c'est ce qui rend le
   constat 1 du lanceur significatif.
3. Mineur — marge de 5 s entre le SIGKILL de l'enveloppe (3 595 s) et celui de l'orchestrateur (3 600 s) : suffisante, mais
   un arrêt par l'enveloppe ne laisse aucune ligne JSON (plafond compté) et n'annule pas le lot ; il n'arrive que si la
   commande dépasse sa propre borne de 3 570 s.

Information (non constat) : si `maxOutputTokens` compte la pensée chez Gemini, le texte visible du proposeur dispose de
27 176 − 8 192 ≈ 19 000 jetons ; une sortie tronquée rend le code 5 au coût du pire cas, dans le plafond.
