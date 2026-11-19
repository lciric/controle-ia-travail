# Rapport de recopie — erratum 1 à l'addendum scellé de la ligne 1, version 2 → version 3 — v1

Agent de recopie, modèle L′, écart déclaré à R-3735 sur le précédent de R-3791 (version 3). Date (temps universel, `date -u`) : 2026-11-19, vers 23:35. Rien lancé ; aucune graine dérivée ; aucun appel à un fournisseur de modèles ; aucune dépense ; aucune écriture dans le dépôt ; aucun commit ; rien touché sous `archives-reponses-modeles/` ; aucun refus d'outil.

## Pièces lues (empreintes recalculées par `sha256sum`)

| pièce | sha256 |
|---|---|
| erratum, version 2 (`docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-1-effort-recherche/erratum-1-addendum-1-preenregistrement-ligne-1-effort-recherche-v5-v4-v2.md`, branche `lot/compte-organisme-v1`) | `f66c3ce8682ef1dd9ced3227378eb18041cff41bea76edfeb2c6373d56d1fcf3` (intacte) |
| contrôle `controle-differentiel-erratum-1-addendum-ligne-1-v2-v1.md` (même dossier) | `1c0d43204e6013f162ca7571b099834d8f97ce4531bd936aca02d9a6508c5109` |

## Méthode

Textes exacts tirés du § 4 du contrôle par lecture du fichier ; liste des remplacements écrite avec l'outil d'écriture ; application par `python3 -B scripts/remplacer_texte_exact_v1.py` (sortie « FAIT : 6 remplacement(s) », aucun refus, aucun avertissement) ; différentiel par `diff -u`.

## Remplacements (six)

1. Correction 1 du contrôle, chapeau : « et porte une seule précision de lecture (§ 3). » → « et porte deux précisions de lecture (§ 3). »
2. Correction 2 du contrôle, titre du § 3 : « ## 3. Précision de lecture au § 9, point 5 — aucune règle changée » → « ## 3. Précisions de lecture (§ 9, point 5 ; phrase de statut de la copie scellée) — aucune règle changée »
3. Tenue, titre : « — v2 » → « — v3 ».
4. Tenue, statut : « version 2, non scellée » → « version 3, non scellée ».
5. Tenue, auteur : ligne neuve « Auteur : agent de recopie, modèle L′, écart déclaré sur le précédent de R-3791 (version 3) », qui cite le contrôle (chemin et empreinte) et la version 2 intacte (R12) ; l'ancienne ligne d'auteur devient « Auteur de la version 2 », le reste de son texte inchangé.
6. Tenue, date : « ; version 3 écrite vers 23:35 » ajouté après l'heure de la version 2.

Rien d'autre ne change (différentiel : deux blocs, ces seules lignes).

## Fichiers écrits (bloc-notes `recopie-erratum-ligne-1-v3/`)

| fichier | sha256 |
|---|---|
| `erratum-1-addendum-1-preenregistrement-ligne-1-effort-recherche-v5-v4-v3.md` (avec compagnon `.sha256` écrit par l'outil) | `ab98317d5e809d53eb5af88f17dd1f4e3683a16a1a21c699c9823538f84f1bd4` |
| `….md.journal-remplacements-v1.json` (avec compagnon `.sha256`) | `9ac3beea761e50ddc06ce81cbf6e1a36c296b2838ee933ea40ef18e11719b995` |
| `remplacements-erratum-1-addendum-ligne-1-v3-v1.json` | `fd5f08e8ad1a76f61143a98203c68b77231c444fdee2aaf2330484a991fca392` |
| `differentiel-erratum-1-addendum-ligne-1-v2-v3.diff` | `15e665c106a4d3c65a293e6aebcc11aeeec0680ff7b2623996fd7e22277e974a` |

## Écarts et choix

- Aucun mandat écrit n'est cité pour la version 3 : la consigne n'en nomme aucun ; la ligne d'auteur cite le contrôle seul.
- Le contrôle est cité dans la ligne d'auteur seulement ; aucune ligne n'est ajoutée à la table du § 1 (la consigne dit « rien d'autre »). À trancher par la mère si elle veut cette ligne.
- Les en-têtes du différentiel portent les chemins absolus et les horodatages des fichiers, comme `diff -u` les écrit.
