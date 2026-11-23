# Consigne du concepteur de l'erratum de chaîne de la relecture décisive du barreau 5 — v1 (préparée, non lancée)

Écrite le 22 novembre 2026 vers 22:20Z par le conducteur de la lecture du barreau 5 (`session_013QMayjM1PQPWkLifMw9HDR`), à la demande de la mère. Le concepteur est **Opus 5.5 en effort maximal** : le quota de Fable est épuisé jusqu'au 29 (GO-2026-11-22-145). Sa pièce sera contre-lue par un Opus neuf, puis vérifiée par le même contre-lecteur. La consigne ne part qu'au mot de la mère, une fois le mot de Lazar reçu sur la relance et sur le traitement de la branche de sortie.

## Qui tu es
Tu es un concepteur neuf. Tu n'as aucun rôle dans le barreau 5 : ni rédacteur, ni contre-lecteur, ni vérificateur du texte scellé ; ni développeur du code ; ni session de formation ou de lecture ; ni ouvreur, ni juge. **Aucun résultat de ce plan n'existe** : la relecture décisive est tombée avant sa marche. Tu ne lis rien qui puisse en porter.
- Interdits : `donnees/*`, `formation-b5f/*`, `course/*` (sauf la branche de commande nommée ci-dessous), `traces/*`, `diag/`, `docs/verdicts/`, `registres/etat.md`, `registres/decisions.md`, les passations.
- Dans le texte scellé, interdite aussi la section « Ce que le rédacteur savait avant d'écrire » (l. 53 à 77).

## Le fait
- La relecture décisive (instance 62047649, 22:13Z) est tombée avant sa marche. Journal : « ARRET : commit des entrées f6e2072d… introuvable » ; journal brut : « could not read Username for 'https://github.com' », puis « could not fetch … from promisor remote ».
- Cause, dans `scripts/amorce_b5f_lecture_v1.sh` au commit `c76e79169` :
  - l. 326 et 327 : le clone du code reçoit l'aide d'identification par `-c`, puis l'inscrit dans sa configuration ;
  - l. 362 à 364 : le clone des entrées, partiel (`--filter=blob:none --no-checkout`), ne la reçoit que par `-c`, et ne l'inscrit pas ;
  - au `checkout`, le téléchargement différé des fichiers n'a donc pas d'identifiants, et le dépôt privé refuse.
- La répétition générale (plan sans entrées) est allée au bout, et l'épreuve à vérité plantée (au processeur) ne passe pas par ce chemin.
- La branche de sortie `donnees/barreau5-familles-jumelles-v1-lecture` existe désormais, avec trois fichiers de traces (commit `254f9280`). L'amorce figée refuse toute branche de sortie présente (R12), et ce nom est écrit en dur à deux endroits : l. 101 à 106 de l'amorce, et l. 961 de `relecture_v1.py`.

## Ce que tu dois concevoir (une pièce, classe A pour la règle et classe B pour le code)
1. **La correction minimale**, ligne par ligne : au moins l'inscription de l'aide dans le clone des entrées. Ajoute ce que le mot de Lazar retient pour la branche de sortie : soit une exception à R12 (copie à l'octet des traces sur `traces/barreau5-lecture-tentative-1`, puis suppression), soit un nom neuf `…-lecture-r1`, qui touche l'amorce et `relecture_v1.py`. Rien d'autre ne change.
2. **Son admission par les gardes figées.**
   - `verifier` et `commande` comparent l'arbre gelé du commit de la marche à celui de `CODE-LECTURE-B5F` (`CHEMINS_GELES`, `harnais/validation_reelle.py`).
   - Le registre propre refuse toute clé inconnue ou en double ; `CODE-LECTURE-B5F` existe déjà.
   - Conçois la voie la plus étroite qui fasse admettre le code corrigé sans affaiblir aucune garde. Exemples : un module de commande v3, sur le modèle de la commande de lecture v2 (`course/barreau5-commande-lecture-v2`, `5402367e`), qui vérifie que le commit de la marche ne diffère de `c76e7916` que par une liste fermée de différences ; ou une ligne de texte libre sous la table, citée par `GO-LECTURE-B5F`. Pèse chaque voie et choisis-en une.
   - Dis ce que le texte scellé permet à la lettre (point 18 (a) : « erreur de chaîne, seule suite permise : un erratum contre-lu » ; et le mandat de la session de lecture, § 5.3 et § 9 point 5) et ce qui reste un écart, à déclarer et à soumettre à Lazar.
3. **L'essai qui aurait vu le défaut** (R5), écrit avant le code :
   - un dépôt git local servi par HTTP, qui exige une identification ;
   - un clone partiel des entrées ;
   - cas sain : extraction réussie avec l'aide inscrite ;
   - artefact : échec avec le code actuel, « commit des entrées introuvable ».

   Ajoute les essais existants à rejouer, sur l'arbre figé et sur l'arbre de commande.
4. **Ce qui ne change pas**, dit explicitement : texte scellé, engagement, entrées, code de lecture (`lecture_v1.py`), sondes, notation, coupure (14 USD), garde (`une_sur_dix`), règle des scores fermés.
5. **La relance** : ce que la session de lecture fait de neuf (commit de la marche, commande, ligne `GO-LECTURE-B5F` inchangée ou non), et ce qui reste à inscrire au registre propre et au registre des accords.

## Ce que tu lis (extractions bornées)
- `CLAUDE.md`.
- Le texte scellé, seulement les lignes 35, 151 à 179, 217 à 233, 257 à 261 et 345 à 448.
- `scripts/amorce_b5f_lecture_v1.sh`, `scripts/lancer_b5f_lecture_v1.sh`, `src/controle_ia/barreau5_familles/relecture_v1.py`, `src/controle_ia/harnais/validation_reelle.py` et `tests/test_amorce_b5f_lecture_v1.py` au commit `c76e79169`.
- La commande v2 au commit `5402367e`, avec son rapport de vérification (`docs/notes/…/lecture/signal-conducteur-v1/verification-corrections-commande-lecture-v2-v1.md`).
- Le mandat de la session de lecture v2 et ses errata 1 à 3.
- `docs/notes/…/lecture/format-activations-gardees-relecture-b5f-v1.md`.

## Ce que tu rends
La pièce, scellée, sous `docs/notes/barreau5-resolution-v1/plan-avant-entretien/lecture/erratum-chaine-relecture-decisive-b5f-v1.md`, avec :
- les différences exactes ;
- la voie d'admission choisie et ses raisons ;
- les essais ;
- les écarts à déclarer ;
- les nœuds pour Lazar.

Tu n'écris pas le code toi-même : un développeur Opus neuf l'écrira sur ta pièce. Aucun geste payant, aucun commit, aucune poussée.
