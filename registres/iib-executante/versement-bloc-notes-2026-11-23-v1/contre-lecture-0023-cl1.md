# Contre-lecture du correctif 0023 : lanceur du saboteur à budget, coupure effective de la machine (classe B, premier contre-lecteur)

Contre-lecteur neuf (Opus 5.5). Il n'a écrit ni le correctif ni ses essais. Base 4f538eef (correctif 0022), correctif 9b03d0ea (arbre ce3e51ca…), lus dans un worktree à part (`scratchpad/cl-0023`) et, pour les comptes, dans `scratchpad/cl-0023-base`.

## Verdict

**Autorisable après corrections.** La règle codée est bien celle de la décision GO-2026-11-22-77 (option (b)) : la configuration doit rester sous la ligne, la dépense antérieure strictement sous la ligne, et le plafond total vaut min(ligne, configuration + antérieure). Tous les chemins du lanceur sont branchés comme il faut. Il reste un point majeur : la sortie de `plafond-total` arrondit à 6 chiffres significatifs, parfois vers le haut. La machine peut alors dépenser un peu plus que le plafond scellé de 55 USD. L'écart est infime, mais c'est un élargissement silencieux. La correction tient en une ligne.

## Points

### Bloquant
Aucun.

### Majeur
**M1. Arrondi vers le haut du plafond total** (`src/controle_ia/iib/session_v5.py:174`).
`print(f"{float(r['plafond_total_usd']):g}")` ne garde que 6 chiffres significatifs. Mesuré avec le chemin `python3 -I -B` du système :
- configuration 55, antérieure 3.123456 : sortie `58.1235` au lieu de 58.123456, donc 55.000044 pour la machine ;
- antérieure 1.2345678 : sortie `56.2346`, donc 55.0000322 pour la machine ;
- antérieure 4.9999999 : sortie `60`, donc 55.0000001 pour la machine.

Les deux écarts sont sous 0.0001 USD. La valeur sortie peut quand même dépasser configuration + antérieure. L'invariant « machine ≤ configuration » est alors franchi, et c'est un arrondi silencieux (R5). L'expression régulière du lanceur accepte des décimales sans borne (`^[0-9]+([.][0-9]+)?$`), donc rien ne bloque ce cas en amont.

Correction exacte : `print(_d(r["plafond_total_usd"]))`. On obtient l'écriture décimale exacte, et `session_v3 depense` la lit sans peine. Il faut aussi ajouter un essai artefact : `plafond-total … 55 3.123456` doit donner exactement `58.123456`, et `Decimal(sortie) − Decimal(antérieure) ≤ 55` doit tenir sur un jeu de valeurs à nombreuses décimales (3.123456, 1.2345678, 4.9999999). Autre option, plus étroite encore : borner la dépense antérieure aux centimes dans le lanceur (`^[0-9]+([.][0-9]{1,2})?$`, lignes 217, 228 et 278) et dans `coupure_effective`, qui refuserait tout le reste. La première correction suffit.

### Mineur
- m1 (`tests/test_iib_garde_depense_0023.py:61`, `_py`). L'essai dit que le chemin `python3 -I -B` du système reste en bibliothèque standard. Il ne le prouve pas : le Python du système a numpy 2.5.3. Je l'ai vérifié à part en bloquant numpy, scipy, pandas et torch à l'import. `go`, `plafond-total` et `plafond-ligne` passent bien, donc le code est conforme. Il manque seulement l'essai. Proposition : dans `_py`, préfixer le programme d'un bloqueur d'import (`builtins.__import__` qui lève `ImportError` pour numpy), ou bien poser un `numpy.py` qui lève l'erreur dans un dossier mis en tête de `sys.path`.
- m2 (`session_v5.py:109` et `:111`). Les messages de refus affichent `limite` brut (« plafond de la ligne 60.0 »), alors que le message de succès passe par `_d` (« 60 »). Correction : `{_d(limite)}` dans les deux messages. Seul l'affichage change.
- m3 (`scripts/lancer_iib_v3.sh:410`). « la coupure de la ligne ($PLC USD) reste » : `$PLC` est désormais le plafond total de la création. Ce n'est plus le plafond de la ligne dès que l'antérieure est sous ligne − configuration (par exemple 55 contre 60). Correction : « la coupure du plafond total de la création ($PLC USD) reste ». Une ligne de plus change dans le décompte borné de `test_iib_lanceur_v5.py:438` : il faut y ajouter le motif.
- m4, pour mémoire, sans correction ici puisque les amorces ne doivent pas changer : le message de `scripts/amorce_instance_iib_course_v5.sh:194` dit « heure d'épuisement du plafond de la configuration ». C'est maintenant celle du plafond total. À noter au journal du correctif.
- m5, pour mémoire. Le plan interne de la machine (`branches_v5.py:83`, entrées scellées : plafond 45, dépense passée) ne connaît pas la dépense antérieure vraie. Au-delà de 5 USD d'antérieure, la coupure par l'heure d'épuisement peut tomber avant la fin du plan. C'est voulu par la décision : la coupure est plus stricte, jamais plus large. À signaler à la lecture.

## Vérifications faites (point 1 du mandat)
- Règle comparée à l'ancienne `session_v12.verifier_plafond_epreuve`. Même lecture et même jugement de la ligne (`ligne_go_calcul`), mêmes refus pour une valeur illisible, non finie, négative ou nulle. Seul le test « p + a ≤ ligne » est remplacé, par « p ≤ ligne et a < ligne », plus T = min(ligne, p + a). La garde redondante `machine ≤ 0` lève une erreur et ne sert jamais de repli. Pas d'élargissement, hors M1.
- `--verifier-go-seulement` (l. 218) et `controles-explo` (l. 239) appellent `go` avec la nouvelle règle. `creation` (l. 285 à 287) appelle `go`, puis `plafond-total`, et tout refus arrête avant la création. `session_v3 depense` reçoit `$PTOT` (l. 317). Le champ `plafond_creation` reçoit `$PTOT` (l. 335).
- Relance après une offre refusée (l. 382). Elle relit `champ anterieure` (inchangé, `tail -1`) et rejoue `creation`, qui recalcule `PTOT`. C'est cohérent. Un refus ne dépense rien.
- `surveillance` (l. 393 et 429) lit `plafond_creation`, c'est-à-dire T, puis appelle `session_v3 surveillance`, qui compte instance + antérieure + téléchargement contre T. Le total reste donc sous la ligne et la machine sous T − antérieure − téléchargement, donc sous la configuration. Un ancien `lancement.txt` (plafond_creation = 55) garde l'ancienne règle, plus stricte.
- `DEPENSE_EPUISEE_UTC_S` vient de `depense $PTOT`. Elle donne l'heure d'épuisement au plafond total, ce qui tient les deux bornes, hors M1.
- `session_v5` : `go` et `plafond-total` priment. `plafond-ligne`, `variante`, `carte`, `creation-7b`, `instances` et `config` passent toujours par `session_v1` ou le reste du module. Seul `lancer_iib_v3.sh` appelle `iib.session_v5` : les lanceurs v1 et v2 gardent `session_v1`, donc l'ancienne règle, sans incohérence avec leur appel à `depense $PLC`.
- Bibliothèque standard seule sur ce chemin (`decimal`, `datetime`, `t06.session_v12`, `t06.session`). Vérifié en bloquant numpy (voir m1).
- Amorces inchangées : `amorce_instance_iib_v5.sh` a71baeaa5930c8d8…, `amorce_instance_iib_course_v5.sh` 03962c29b04bfcbe…. Le diff ne touche ni `scripts/amorce_*` ni les listes figées.

## Essais (point 2)
R5 est tenu pour `coupure_effective`, la ligne de commande et `--verifier-go-seulement` : chacun a des cas sains et des artefacts. Essais manquants proposés :
1. Un artefact d'arrondi, voir M1.
2. Une preuve « sans numpy », voir m1.
3. `controles-explo` de bout en bout avec une antérieure de 9.65 acceptée et de 60 refusée. Seul `--verifier-go-seulement` est joué aujourd'hui.
4. Une surveillance dynamique : `session_v3 surveillance` lancée avec la valeur `plafond_creation` écrite par la création doit répondre ARRET quand antérieure + téléchargement + instance atteint T. L'essai actuel ne fait que chercher le texte du script.

## Listes figées (point 3)
Les deux fichiers sont inchangés par le diff. Aucune fonction d'essai n'est ajoutée ni retirée dans `test_iib_lanceur_v5.py`, seule une assertion change. Le nouveau fichier d'essais n'est dans aucune des deux listes. Comptes collectés identiques à la base et au correctif.

## Commandes jouées et comptes
- `git worktree add …/scratchpad/cl-0023 9b03d0ea…` ; `git worktree add --detach …/scratchpad/cl-0023-base 4f538eef…`
- `git diff --stat 4f538eef 9b03d0ea` : 4 fichiers, 189 lignes ajoutées, 6 retirées.
- `PYTHONPATH=src venv/bin/python -m pytest -q tests/test_iib_garde_depense_0023.py` : **26 passed**.
- `… pytest -q tests/test_iib_lanceur_v5.py tests/test_iib_scripts_v1.py tests/test_iib_environnement_machine_v5.py` : **76 passed** (102 s).
- `pytest --collect-only -q` sur `scripts/tests-cibles-iib-v5-v7.txt` : base **311**, correctif **311**.
- `pytest --collect-only -q` sur `scripts/tests-cibles-iib-course-v5-v2.txt` : base **313**, correctif **313**.
- `python3 -I -B -c <session_v5 avec numpy bloqué> go|plafond-total|plafond-ligne` sur un registre d'essai (ligne de 60 USD), Python 3.13.18 avec numpy 2.5.3 présent mais bloqué. `go 55 9.65` : code 0, coupure de la machine 50.35. `plafond-total 55 9.65` : `60`. `go 55 60` : code 1, refus. Sondes d'arrondi : voir M1.
- `sha256sum` des deux amorces : conformes aux empreintes attendues.

Aucune dépense, aucun loueur, aucun modèle externe appelé, rien poussé. Aucun fichier interdit n'a été ouvert.
