# Essais à blanc de l'amorce sans ssh du pilote MR-2 — v2 (procédure v12)

Compte organisme, modèle A. **Aucun appel à un fournisseur, aucune clé réelle, aucun réseau extérieur, aucune dépense.** Joués sur un
dossier jetable de la session (hors de tout dépôt), le 2026-11-15 (11:55Z). La v1 (`../../sans-ssh-v1/essais/`) reste en place.

## Ce qui est joué

- **Dépôt distant** : un dépôt nu local (`file://`, filtres et envois par empreinte permis, comme le dépôt distant), avec un crochet de
  réception qui refuse une branche tant qu'un drapeau existe (scénario « poussee-finale-reprise », M4). Il porte trois branches
  synthétiques aux mêmes chemins que le dépôt de travail : `lot/compte-organisme-v1` (le vrai paquet de l'arbre `e3d83e47…` et le vrai
  dossier de la sonde v74, **lus par `git show` à la branche distante du lot du dépôt donné par `ESSAI_DEPOT`**, m12 ; les pièces de
  `sans-ssh-v2/`), `prep/pilote-mr2-compte-organisme-v1` (le vrai texte scellé `8aa33014…`), `main` (le vrai `registres/go.md`). La mère
  du banc y inscrit les empreintes (fichier `registres-essai/inscriptions.md` du `main` synthétique) avant chaque feu.
- **Loueur** : `doublure_vast_v1.py` (inchangée). **Lanceur** : `doublure_lanceur_v1.py` (inchangée ; `bloc` et `secret` délégués au
  vrai lanceur) ; le scénario `sain-integral` joue le **vrai lanceur v74** de bout en bout, le pilote « réel » en mode à blanc.
- **Mère** : jouée par `essai_amorce_v2.py` au moyen de l'outil de la session v2 ; deux feux faux écrits sans l'outil.
- **Clés** : valeurs factices ; après chaque scénario, toute la branche de sortie (tous ses commits) est fouillée pour les quatre
  valeurs factices (brutes et en base64), le secret tiré et la phrase de répétition, et pour les noms interdits.
- Les processus d'un scénario sont arrêtés à sa fin par l'identifiant du groupe de processus créé par le banc (R10), aussi sur une
  exception du banc.

## Rejouer

```
cd sans-ssh-v2/essais
ESSAI_DEPOT=/chemin/du/depot/de/travail python3 -B essai_amorce_v2.py DOSSIER_JETABLE resultats.json                 # scénarios rapides
ESSAI_DEPOT=/chemin/du/depot/de/travail python3 -B essai_amorce_v2.py DOSSIER_JETABLE resultats.json sain-integral   # vrai lanceur
ESSAI_DEPOT=/chemin/du/depot/de/travail python3 -B essai_outil_session_v2.py DOSSIER_JETABLE resultats.json           # outil
```

(`ESSAI_DEPOT` : un dépôt qui porte `refs/remotes/origin/lot/compte-organisme-v1` et `…/prep/pilote-mr2-compte-organisme-v1`,
`…/main` ; défaut `/home/user/controle-ia-travail`.) Environnement : Python 3.13.18, numpy 2.5.3, git version 2.43.0, OpenSSL 3.0.13 30 Jan 2024, bash 5.2, 4 processeurs.

## Résultats (scellés, à côté)

| essai | résultat | pièce |
|---|---|---|
| arret-pendant-jouer | conforme : arret (A) | `resultats-essai-amorce-v2.json` |
| budget | conforme : arret (A) | `resultats-essai-amorce-v2.json` |
| code3 | conforme : arret (A) | `resultats-essai-amorce-v2.json` |
| comptes-faux | conforme : noeud, machine gardee | `resultats-essai-amorce-v2.json` |
| entree-presente | conforme : arret (A) | `resultats-essai-amorce-v2.json` |
| feu1-faux | conforme : arret (A) | `resultats-essai-amorce-v2.json` |
| fuite-cle | conforme : fini | `resultats-essai-amorce-v2.json` |
| mesure-code2 | conforme : noeud, machine gardee | `resultats-essai-amorce-v2.json` |
| minuterie | conforme : sans état final (attendu) | `resultats-essai-amorce-v2.json` |
| phrase-alteree | conforme : arret (A) | `resultats-essai-amorce-v2.json` |
| poussee-finale-reprise | conforme : fini | `resultats-essai-amorce-v2.json` |
| refus-arguments | conforme : sortie de l'amorce | `resultats-essai-amorce-v2.json` |
| relance-conteneur | conforme : arret (A) | `resultats-essai-amorce-v2.json` |
| relance-deux-fois | conforme : arret (A) | `resultats-essai-amorce-v2.json` |
| relance-ok | conforme : fini | `resultats-essai-amorce-v2.json` |
| sain | conforme : fini | `resultats-essai-amorce-v2.json` |
| sortie-presente | conforme : sans état final (attendu) | `resultats-essai-amorce-v2.json` |
| sain-integral | conforme : fini, 1080 s | `resultats-essai-amorce-integral-v2.json` |
| outil de la session | 36/36 cas conformes | `resultats-essai-outil-session-v2.json` |

## Ce que les essais ne prouvent pas

La création chez le loueur et sa lecture réelle de `--env` et de `--args` (la commande imprimée par l'outil v2 a été jouée sur une
doublure de l'outil du loueur, qui a reçu `--env` en treize affectations et l'amorce égale à l'octet après décodage, lue par
`$(cat …)`) ; l'interface d'autodestruction du loueur ; le clonage par jeton depuis la machine et la poussée de la branche de sortie sur
le dépôt distant ; la poussée de la branche d'entrée depuis la session (à éprouver avant la création, `essai-poussee`) ; l'image
`python:3.13-bookworm` ; les appels réels ; le pire cas de durée.

Note : les cinq pièces de `sans-ssh-v2/` jouées par chaque essai sont celles de ce dossier (empreintes portées dans chaque fichier de
résultats). Le scénario `sain-integral` a été joué avec le banc avant deux changements du banc, sans effet sur lui : la cause du feu
d'arrêt du scénario « arret-pendant-jouer » écrite sans accent (l'outil v2 refuse désormais une cause accentuée, M3 : le banc s'est
arrêté sur ce refus) et le refus du scénario « poussee-finale-reprise » porté de 100 à 240 s (à 100 s, il pouvait prendre fin avant la
poussée finale, et la reprise n'était alors pas exercée). Les scénarios rapides et l'essai de l'outil ont été rejoués après ces deux
changements.
