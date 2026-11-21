# Manifeste de l'exécutant — étage 2 à 200 de la ligne 3, partie 1 — v1

Mandat : `/home/user/controle-ia-travail-organisme/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/etage-2-portee-200-v1/mandat-executant-etage-2-partie-1-v3.md`, sha256 `76becd61d1ee60366acd3e31fe14ffc17f88edeeb243313d251c50e5b543382e`, égal à son compagnon (relevé 2026-11-21 vers 06:09Z).
Mot de la mère : R-4348, sous GO-2026-11-21-04 et GO-2026-11-20-68 ; gestes 0 à 6, sans appel payant. Geste 0 fait par un autre agent neuf (06:07:57Z et 06:08:10Z, codes 0 et 0, d'après la session) ; non touché par moi.
Notations : `R` = `/home/user/controle-ia-travail` ; `E` = `R/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/etage-2-portee-200-v1` ; `X` = `E/execution-v1` ; `CHEMIN` = `R/prereg/organisme-auto-conception-v9/additif-6-code-etage-2-preenregistrement-ligne-3-v2.md`.

Heure de première commande : 2026-11-21T06:09:19Z (`date -u`).

## Avant tout geste (relevé entre 06:09:19Z et 06:09:57Z)

| commande | code | sortie retenue |
|---|---|---|
| `git -C R rev-parse HEAD` | 0 | `544369e3feede23081c9a901515b7c7a76f84154` |
| `git -C R merge-base --is-ancestor b3b221914b7d9adfa0e84d3ed31c7bbe580e6fd5 HEAD` | 0 | descendant |
| `git -C R rev-parse --abbrev-ref HEAD` | 0 | `prep/ligne-3-etage-2-execution-v1` |
| `git -C R status --porcelain --untracked-files=no` | 0 | vide (propre) |
| `sha256sum CHEMIN` ; `cat CHEMIN.sha256` | 0 ; 0 | égaux : `HEX` = `e2afc7b987ab64dfc270c6c20d49ef5e0d8eaf603ffb2f647a0ea0dee6ca4f01` |
| `env -C E/generateur-v3 sha256sum -c table-empreintes-generateur-v3.txt` | 0 | six lignes OK |
| `env -C E/code-appel-v4 sha256sum -c table-empreintes-code-appel-v4.txt` | 0 | six lignes OK |
| `env -C E/etalonnage-lecture-v3 sha256sum -c table-empreintes-etalonnage-lecture-v3.txt` | 0 | seize lignes OK |
| `env -C E sha256sum` des quatre programmes (§ 2.1), des quatre pièces du § 2.2 et des trois tables | 0 | onze empreintes, chacune égale à celle de l'additif (§ 2.1, § 2.2, § 2.3) |
| `/usr/local/bin/python3 --version` | 0 | `Python 3.13.18` |
| `/usr/local/bin/python3 -I -B -m pip list` | 0 | numpy 2.5.3 |

Point 4 : aucun contrôle de ma part sur le fichier des cartes.
Remarque : les pièces du § 2.2 (fragments v3, pièce du (4) v3, calcul du plafond et sa sortie) ne figurent dans aucune des trois tables ; elles sont contrôlées par empreinte directe contre l'additif.

## Geste 1 (06:10:19Z à 06:10:41Z)

| commande | code | sortie retenue |
|---|---|---|
| `git -C R fetch origin main prep/ligne-3-etage-2-execution-v1` (forme dite par la mère) | 0 | `origin/main` avancé de `741c79af7` à `a659641cc` ; branche `prep/…` inchangée |
| `/usr/local/bin/python3 -I -B E/generateur-v3/generer_temoins_ligne_3_v3.py creer-journal-rejeux` (06:10:19Z) | 0 | `{"journal": "créé vide"}` |
| `git -C R add` des trois chemins du geste 1, nommés un par un | 0 | index : les trois chemins seuls (`git diff --cached --name-only`) |
| `git -C R diff --cached > MON_DOSSIER/diff-indexe-geste-1.txt` puis `grep -c -E '…'` | 0 ; 1 | compte 0 (code 1 de grep : aucune ligne, attendu) |
| `git -C R commit -m "Ligne 3, étage 2 : journal des rejeux de la garde de recouvrement créé vide, et son manifeste"` (avec les lignes d'attribution) | 0 | commit `f6cb2ff66f1bfc83a3e65f530d2e2ced24fa1425` |
| `git -C R push origin prep/ligne-3-etage-2-execution-v1` | 0 | `544369e3f..f6cb2ff66` |

## Geste 2 (06:10:41Z à 06:10:54Z)

| commande | code | sortie retenue |
|---|---|---|
| `mkdir X` | 0 | — |
| `/usr/local/bin/python3 -I -B E/generateur-v3/generer_temoins_ligne_3_v3.py composer --fragments E/fragments-v3/fragments-etage-2-ligne-3-v3.json --empreinte-fragments 23be8dae1839eab72979b794371a7fb0bce38bcd41b8309cc79386fc233c50fb --sortie X/composition --autorisation-additif CHEMIN --empreinte-additif e2afc7b987ab64dfc270c6c20d49ef5e0d8eaf603ffb2f647a0ea0dee6ca4f01` (chemins complets) | **2** | `{"refus": "Refus", "motif": "configuration des juges : illisible"}` |
| `ls -la X` | 0 | `X` vide : aucun dossier `composition/` écrit |

**Refus (code 2) : arrêt, retour à la mère** (mandat, geste 2 ; additif, § 6). Aucun argument changé, aucun rejeu, aucune recherche de cause. `HEX_BANQUE` et `HEX_JOURNAL` : inexistants. `X` reste, vide, sur disque, non commité.

## Geste 3

Non atteint.
