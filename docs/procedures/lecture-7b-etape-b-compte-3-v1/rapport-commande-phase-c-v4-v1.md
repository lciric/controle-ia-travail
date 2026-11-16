# Rapport du rédacteur — commande de la phase C du compte 3, version 4, brouillon 1 — v1

- **Rédacteur** : sous-agent neuf, modèle B, de la session mère `session_016QhUrtmLyFWJP6Cy7rgfXH` ; du 2026-11-16T12:58:48Z au 2026-11-16T13:02:46Z
  (`date -u`). Tâche bornée par la décision de la mère R-2980 (registre des décisions, ligne lue par sa clé).
- **Verdict** : brouillon 1 écrit par programme, répété de bout en bout sur dépôts jouets, **54 conformes sur 54, tout conforme** ;
  différentiel et filtres contrôlés par programme, tout conforme. Rien n'est committé. Pas encore en vigueur : contre-lecture (R2) à venir,
  puis copie à l'octet sous le nom définitif `commande-compte-3-phase-c-v4.md`.

## 1. Pièces neuves (même dossier, chacune scellée)

| pièce | empreinte | rôle |
|---|---|---|
| `commande-compte-3-phase-c-v4-brouillon1.md` | `f4bcf4064e7ab7d53538ce998c2d4745a1ac4387443505d82e8f7a01aec7c755` | la pièce : v3 plus `diag/$R7/sondes-t07.json` et son compagnon au bloc C5 |
| `couples_commande_phase_c_v4_brouillon1_v1.py` | `496602b34b4612ce50c19be3574cf7af195c962c535791a0ff47d7f6b610e21b` | neuf couples « ancien → nouveau » ; empreinte de la v3 vérifiée, chaque « ancien » une seule fois, cible jamais écrasée (relance : arrêt, code 1, constaté) |
| `repetition_phase_c_jouet_v4.sh` | `96f888e9c6db79e126b045983f0cbb0b59fddb63e32fc2bc7dbe93cc09de715a` | répétition v4 : commande en troisième argument, placée sous le nom définitif, bordereau de 29 fichiers, `sondes-t07.json` et compagnon exigés |
| `repetition-phase-c-jouet-v4-sortie-brouillon1-v1.txt` | `e208b48bf6a86b6e3591dd646d8ea05abc5e3f283e4bc36a920c162fd9066114` | sortie de la répétition jouée sur le brouillon 1 |
| `controle_commande_phase_c_v4_brouillon1_v1.py` | `4c21f3aea9e9ee27a68bd402f791d0a1e8a5947ac36a4f4e88ad17ac936d0948` | différentiel v3 → v4 et contrôle des filtres, par programme |
| `controle-commande-phase-c-v4-brouillon1-sortie-v1.txt` | `072571fcea372ec29142db442fe4b90bc9935dfc90251b9b7490927c2981ef5c` | sa sortie (code 0) |

Gardées intactes (R12), empreintes revérifiées : `commande-compte-3-phase-c-v3.md` (`9d7889198238c171447a06f56f1a37beb4190572c3a9ceceb18144541c258d2e`),
`repetition_phase_c_jouet_v3.sh` (`8be57168fe40b27ad7ac2bd0c1e3908733c316b53e00a2bab883653c67a081ee`).

## 2. Différentiel v3 → v4 (sortie du contrôle, § 1 ; texte entier des lignes dans la sortie scellée)

568 lignes → 581 ; **9 plages, 7 lignes ôtées, 20 ajoutées, 561 lignes de la v3 gardées à l'octet**. Une plage par couple :

| n° | v3 | v4 | changement |
|---|---|---|---|
| 1 | l. 1 | l. 1 | titre : « v3 » → « v4 » |
| 2 | avant l. 7 | l. 7-15 | puce « Version 4 » (v3 et son empreinte, gardée ; le seul changement ; raisons ; R-2980) |
| 3 | après l. 25 | l. 35-36 | puce « Rédacteur » complétée pour la v4 |
| 4 | l. 37 | l. 48-49 | table des pièces : répétition v4 et sa sortie ; ligne de la v3 gardée |
| 5 | l. 118 | l. 130 | bloc 0b-C : `sha256sum` sur `commande-compte-3-phase-c-v4.md` (nom définitif) |
| 6 | l. 380 | l. 392 | bloc C5 : `"diag/$R7/sondes-t07.json"` ajouté à la boucle des pièces |
| 7 | l. 396 | l. 408 | bloc C5 : « attendu » → quatorze fichiers et leurs compagnons, plus l'extrait (29 fichiers) |
| 8 | l. 484 | l. 496 | bloc F-C : le journal provisoire écrit « commande phase C v4 » (la v3 écrivait encore « v2 ») |
| 9 | l. 561 | l. 573-574 | annexe d'essais : répétition v4 et sa sortie |

Seize blocs bash dans les deux versions ; **seuls 0b-C, C5 et F-C diffèrent**. Même nombre d'occurrences, v3 et v4, du bac
(`bac-etape-b-compte-3-v2`, 15), de `variables-v2.sh` (20), du fichier de marque `appel-etape-b-lance-v2.txt` (6), du bordereau
(`bordereau-remise-v2.txt`, 8), de la branche `verdict/t07-etape-b-compte-3-v1` (4), de la commande de la phase A (1) et des marqueurs
« << » (49). Le nom de brouillon ne figure nulle part dans la commande.

## 3. Contrôle des filtres du bloc 1C (sortie du contrôle, § 2)

Motifs lus dans le bloc 1C du brouillon, égaux à ceux de la v3, joués par `grep -i -E` comme au bloc C5 : `INTERDITS_NOMS_B` et
`INTERDITS_CONTENU_B` donnent **0 ligne** sur `diag/20261114-001352-t07-lecture-reel/sondes-t07.json`, sur son compagnon et sur leur
forme au bordereau (`./diag/…`). Témoins (R5) : `INTERDITS_NOMS_B` arrête `lecture-sondes-t06.json` et `sondes-neuves-t07.npz` ;
`INTERDITS_CONTENU_B` arrête « plan de l'étape B bis ». Dans la répétition, le bloc C5 entier (filtre de noms sur le bordereau de
29 fichiers) passe avec la pièce ajoutée.

## 4. Répétition (sortie `repetition-phase-c-jouet-v4-sortie-brouillon1-v1.txt`)

- Du 2026-11-16T13:00:40Z au 13:01:23Z ; commande répétée `f4bcf406…` (égale au brouillon 1), 16 blocs ; blocs mis bout à bout
  `28aab2d13a543970b64b141310db413c8c9d0f754254675c4eb41996cf07e074`.
- **BILAN : 54 conformes sur 54 ; « RÉPÉTITION DE LA PHASE C : TOUT CONFORME »** : les 53 épreuves de la v3 (bordereau attendu passé
  de 27 à 29 fichiers), plus une épreuve neuve : `sondes-t07.json`, égal à la ligne `SONDES-T07` jouet, et son compagnon figurent au bordereau.
- Différence entre les scripts v3 et v4 : dix couples (en-tête, usage, troisième argument, commande placée dans le main jouet sous le nom
  définitif, motif attendu du bloc 0b-C, bordereau de 29 fichiers, épreuve neuve) ; rien d'autre.
- Dépôts jouets seulement, sous le dossier de travail jetable ; tête du dépôt principal inchangée, aucun fichier suivi modifié.

## 5. Points pour la mère

1. **Couple 8 (bloc F-C)** : la v3 écrivait « commande phase C v2 » au journal provisoire (reste de la v2). Passé à « v4 » comme
   auto-référence de version ; les noms de fichiers en « -v2 » sont inchangés. À confirmer ou à retirer par la contre-lecture.
2. **Nom définitif** : copier le brouillon retenu **à l'octet** sous `commande-compte-3-phase-c-v4.md` ; l'empreinte reste alors
   `f4bcf406…`, celle que la répétition a jouée. La table des pièces et l'annexe citent la sortie « brouillon1 » : vrai tant que le
   brouillon 1 est retenu ; un brouillon 2 demande une répétition neuve et un couple de plus.
3. **Appel réseau dans la répétition** : le bloc 2C lit l'en-tête de date de `pypi.org` (horloge de référence) ; joué trois fois ici,
   comme dans la répétition v3 ; aucune donnée du projet dans la requête. La consigne disait « aucun appel réseau » : déclaré.
4. Le bloc C5 vérifie le compagnon de `sondes-t07.json` ; l'égalité à la ligne `SONDES-T07` reste vérifiée au bloc C2 seulement (inchangé).
5. Lecture du texte scellé : pour lire l. 1539 et l. 2659, les plages l. 1535-1541 et l. 2655-2661 ont été affichées (plus larges que les
   deux lignes demandées).
6. Contre-lecture (R2) du brouillon 1 par un sous-agent qui ne l'a pas écrit : à faire, avec ces six pièces et la v3.

## 6. Déclaration d'exclusion

Rôle : rédacteur de la commande phase C v4 ; modèle B. A lu : la commande v3 (`9d788919…`), la répétition v3 (`8be57168…`) et le début
et la fin de sa sortie, les lignes 1535-1541 et 2655-2661 du texte scellé `prereg/T0.7-sondes-v0-v1.md`
(`d7d180eccbbce8ff2e370f82957543c28f1e564c872f981c7ada403949baade5`), la ligne R-2980 du registre des décisions (par sa clé). **Exclu**
des lecteurs de P3-bis, du rôle de lecteur B de l'étape B, de toute lecture de l'étape B bis et de tout verdict de G0. Jamais ouvert :
aucun fichier de `diag/`, `runs/` ou `donnees/` du dépôt principal, aucun fichier de `docs/verdicts/`, rien de l'étape B bis, rien de
7a, aucune valeur de clé. Aucun commit, aucune poussée, aucune récupération sur le dépôt principal.
