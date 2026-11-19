# Note de clôture de la confirmation du témoin de Bailey (addendum 7, § 3)

- Heure UTC d'écriture : 2026-11-19T11:51Z (2026-11-19T11:51:59Z).
- Session `session_01XJ6MgnEhQMZteN9F8a1BST` (attaquant informé) ; branche `claude/compassionate-meitner-d4ryyk` ; tête du
  dépôt à l'écriture : `18c87bda48d38a3839c496b5b6f667090ed22c04`. Clôture demandée par Lazar (19 novembre, vers 11:47Z,
  verbatim) : « Clôture du témoin de Bailey maintenant : écris la note de clôture scellée, joue à l'aveugle
  lecture_scellee_v3 (attendus, essai factice, lire), puis lance les deux lecteurs neufs selon le § 3 de l'addendum 7 ».
- L'arbre `src/` est gelé au commit `a904aa391cdcf2650b747fe64e48caa0ec8c5849` jusqu'au dernier contrôle final.
- Aucune note du témoin n'a été lue avant cette clôture ; les deux verdicts sont lus ensuite (addendum 7, § 1 et § 3).
  Seuls des champs techniques ont été lus (tours complets, durées comptées en lignes, gardes par leur nom et leur état,
  transferts, destructions). Pour information : sur l'ordre de Lazar du 19 novembre (« avant toute destruction, inventaire
  et versement scellé de tout ce qui reste sur la machine »), des copies de fichiers de l'instance de la relance
  (61170458) ont été prises sans être ouvertes. Elles sont sur le disque du poste d'inventaire v2 et dans son instantané,
  et seuls leurs noms, tailles et empreintes sont sur la branche. Aucune n'a été lue, et aucune n'entre dans un dossier
  donné à une lecture.

## 1. Cas de clôture

- [x] **(i)** Les journaux de l'exécution qui porte le verdict sont transférés et scellés ; run fini.
  - **Exécution qui porte le verdict :** `principal-relance`. C'est la relance de la l. 371, jouée par le chemin de
    l'addendum 5 (relance seule, conduite v16, poste Hetzner v14, instance 61170458), avec le plafond de coût de
    l'addendum 8, option B (`44326b34…`).
  - **Pourquoi une relance :** la première exécution (conduite v15, instance 61049303) s'est interrompue le 17 novembre
    vers 17:12Z (instance arrêtée par Vast, compte sans crédit). La reprise de la lecture 38 (poste de reprise v5) a
    établi 17 tours complets, sous 20 : une seule relance entière.
  - **Tours complets de la relance :** 72, soit K = 72 (champ `relance_seule.K` du bilan). Le journal des durées
    transféré compte 72 lignes, tours 0 à 71, sans double, empreinte conforme.
  - **Bilan scellé** `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/sortie-conduite-v16/bilan-conduite-v5.json` : `transfert_complet` vrai, `marque_rapatrie`
    vrai, `detruite` vrai. Transferts en foi « transfert-1 » pour `mise-en-place`, `controle-juge` et `principal-relance`.
    Journal du chien de garde « non transféré (CalledProcessError) », rapporté.
  - **Fin de la conduite** : 2026-11-19T10:09:50Z (poste v14).
  - **Reprise de la lecture 38** : oui pour la première exécution
    (`/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/sortie-conduite-v15/reprise-v10-2/`, poste de reprise v5) ; non pour la relance.
  - **Relance de la l. 371** : oui.
- **Suites laissées à la décision de Lazar** : aucune suite ouverte ; note écrite dès le constat.
- **Relance par le chemin de l'addendum 5** : assemblage de la première exécution reprise et de la relance, joué
  par `lanceur_v21.assembler_lecture`. Exécution qui a abouti : cible `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/confirmation-assemblee-v1`, trace scellée
  `assemblage-v1.json`, empreinte `91745b3e11ac8c88d7c4b40c8f553efbd0f1f956ad68ff336b766a49c3f55f84`. Une seule
  exécution, aboutie.
- Après la clôture, rien n'est ajouté à la confirmation.

## 2. Postes arrêtés et branche récupérée

| Poste | Dossier produit | Marque de fin (commit) | Destruction de l'instance de calcul | Serveur du poste |
|---|---|---|---|---|
| v13 (Hetzner 176451822) | `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/sortie-conduite-v15` | `poste-fini-v13.json`, fini 2026-11-17T17:44:19Z (`9a3faf1f`) | 61049303 détruite par la reprise v5, 2026-11-18T02:38:27Z (bilan scellé `sortie-conduite-v15/reprise-v10-2/bilan-reprise-v10.json`) | détruit par identifiant, 2026-11-17T17:49:13Z (`registres/arrets.md`) |
| reprise v5 (Hetzner 176573083) | `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/sortie-conduite-v15/reprise-v10-2` | `poste-fini-reprise-v5.json`, fini 2026-11-18T02:46:06Z, code 0 (`0b7b2b33`) | même instance, détruite par cette reprise à 02:38:27Z | détruit par identifiant, 2026-11-18T02:47:01Z |
| v14, relance (Hetzner 176575468) | `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/sortie-conduite-v16` | `poste-fini-v14.json`, fini 2026-11-19T10:09:58Z (`b3326f23`) | 61170458 détruite par la conduite, 2026-11-19T10:09:26Z (bilan scellé ; absente de l'inventaire Vast à 10:11Z) | éteint à 10:26:01Z, instantané protégé 458234516, non détruit (inventaire avant destruction, mot de Lazar) |

Le poste de reprise v4 (Hetzner 176569589, redémarrage refusé) a écrit `sortie-conduite-v15/reprise-v10`, qui n'est ni
lu ni assemblé. Ce serveur a été détruit le 18 novembre à 02:15:28Z.

**Heures, recopiées du journal de consignation** :
- `2026-11-19T11:48:41Z e0 : branche claude/compassionate-meitner-d4ryyk récupérée, tête 18c87bda48d38a3839c496b5b6f667090ed22c04`
- `2026-11-19T11:48:45Z e1 : repertoires-sortie-conduite-v15-v1.txt : OK (371e16ce98051a3ea7af3eaef8b87d69033154fb5bb33da349d611f0fae061d6)`
- `2026-11-19T11:48:45Z e1 : repertoires-sortie-conduite-v15-v1.txt : répertoires créés sous /home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/sortie-conduite-v15 (1 entrées)`
- `2026-11-19T11:48:45Z e1 : repertoires-sortie-conduite-v15--reprise-v10-2-v1.txt : OK (138ce693a1c2598939993ac6d3f9ccf9664261083e8c42064c34aecde498b87e)`
- `2026-11-19T11:48:45Z e1 : repertoires-sortie-conduite-v15--reprise-v10-2-v1.txt : répertoires créés sous /home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/sortie-conduite-v15/reprise-v10-2 (12 entrées)`
- `2026-11-19T11:48:45Z e1 : repertoires-sortie-conduite-v16-v1.txt : OK (ea584389bed15281438eba10273559b7e1bedde1225f3b55511a4427e6863b62)`
- `2026-11-19T11:48:45Z e1 : repertoires-sortie-conduite-v16-v1.txt : répertoires créés sous /home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/sortie-conduite-v16 (8 entrées)`
- `2026-11-19T11:48:56Z assemblage : lancé : lanceur_v21.assembler_lecture(/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/sortie-conduite-v15/reprise-v10-2, /home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/sortie-conduite-v16, /home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/confirmation-assemblee-v1) ; PYTHONPATH=src, python -B -P`
- `2026-11-19T11:49:01Z assemblage : aboutie ; clés de la trace : fichiers_scelles_verifies,manifeste_regle_sha256,manifeste_relance_sha256,premiere,relance`
- `2026-11-19T11:49:07Z e2 : vérification des chemins : conforme`
- Premier `--calculer-attendu` : `2026-11-19T11:49:18Z e3 : attendu a : {"attendu": "/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/attendu-a-v1.json", "empreinte_attendu": "63249a7c14b0a6c36c73d37cc98599469a8d17adfa74536b3da59ff06cf69c80"}`.

**Suites permises avant la clôture** :
- seconde tentative du § 2.3 : sans objet ; la garde de durée du pilote n'est pas tombée (t = 1 265,0215 s, au plus
  1 800 s) ;
- mise en place refaite : sans objet ; la mise en place et le contrôle du juge de chaque instance ont abouti, code 0 ;
- relance par le chemin de l'addendum 5 : jouée, poste arrêté (v14) ;
- reprise de la lecture 38 : jouée (reprise v5), poste arrêté.

## 3. Listes des répertoires

| Dossier que nomme la liste | Liste | Empreinte | `sha256sum -c` | Création |
|---|---|---|---|---|
| `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/sortie-conduite-v15` | `repertoires-sortie-conduite-v15-v1.txt` | `371e16ce98051a3ea7af3eaef8b87d69033154fb5bb33da349d611f0fae061d6` | OK | 1 entrée, `mkdir -p` |
| `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/sortie-conduite-v15/reprise-v10-2` | `repertoires-sortie-conduite-v15--reprise-v10-2-v1.txt` | `138ce693a1c2598939993ac6d3f9ccf9664261083e8c42064c34aecde498b87e` | OK | 12 entrées, `mkdir -p` |
| `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/sortie-conduite-v16` | `repertoires-sortie-conduite-v16-v1.txt` | `ea584389bed15281438eba10273559b7e1bedde1225f3b55511a4427e6863b62` | OK | 8 entrées, `mkdir -p` |

État de `lecture-assemblee-v1` : lu dans l'état du dossier dans l'arbre principal au calcul de l'attendu, rapporté tel
quel. Les répertoires que git n'a pas portés depuis les postes des séries 1 à 3 et de la relance ne sont pas connus.

## 4. Pour chaque verdict à lire

**Verdict a, run à 36 tours (`lecture-assemblee-v1`)**

| Champ | Valeur |
|---|---|
| Dossier donné à la lecture | `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/lecture-assemblee-v1` |
| Commit du code | `a904aa391cdcf2650b747fe64e48caa0ec8c5849` |
| Fichier des empreintes attendues | `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/attendu-a-v1.json`, empreinte `63249a7c14b0a6c36c73d37cc98599469a8d17adfa74536b3da59ff06cf69c80` ; ligne rendue : `{"attendu": "/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/attendu-a-v1.json", "empreinte_attendu": "63249a7c14b0a6c36c73d37cc98599469a8d17adfa74536b3da59ff06cf69c80"}` |
| Chemin de la sortie | `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/sortie-a-v1.json` (absent à l'écriture de cette note) |
| Attendu recalculé | aucun |

**Verdict b, confirmation (dossier assemblé)**

| Champ | Valeur |
|---|---|
| Dossier donné à la lecture | `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/confirmation-assemblee-v1` |
| Commit du code | `a904aa391cdcf2650b747fe64e48caa0ec8c5849` |
| Fichier des empreintes attendues | `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/attendu-b-v1.json`, empreinte `ed46761b6183e3ad7f4c9d41ae18cd1e15e4c8b3da602df8af201e97be3d5805` ; ligne rendue : `{"attendu": "/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/attendu-b-v1.json", "empreinte_attendu": "ed46761b6183e3ad7f4c9d41ae18cd1e15e4c8b3da602df8af201e97be3d5805"}` |
| Chemin de la sortie | `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/sortie-b-v1.json` (absent à l'écriture de cette note) |
| Attendu recalculé | aucun |

## 5. Commande exacte

Recopiée telle que jouée (lignes « commande : » du journal de consignation) :

```
PYTHONPATH=/home/user/controle-ia-travail/src PYTHONPYCACHEPREFIX=/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/cache-p /home/user/controle-ia-travail/.venv/bin/python -B -P -m controle_ia.temoin_bailey.lecture_scellee_v3 --calculer-attendu /home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/lecture-assemblee-v1 --commit a904aa391cdcf2650b747fe64e48caa0ec8c5849 --vers /home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/attendu-a-v1.json
PYTHONPATH=/home/user/controle-ia-travail/src PYTHONPYCACHEPREFIX=/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/cache-p /home/user/controle-ia-travail/.venv/bin/python -B -P -m controle_ia.temoin_bailey.lecture_scellee_v3 --calculer-attendu /home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/confirmation-assemblee-v1 --commit a904aa391cdcf2650b747fe64e48caa0ec8c5849 --vers /home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/attendu-b-v1.json
PYTHONPATH=/home/user/controle-ia-travail/src PYTHONPYCACHEPREFIX=/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/cache-p /home/user/controle-ia-travail/.venv/bin/python -B -P -m controle_ia.temoin_bailey.lecture_scellee_v3 --calculer-attendu /home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/factice/sortie --commit a904aa391cdcf2650b747fe64e48caa0ec8c5849 --vers /home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/attendu-factice-v1.json
PYTHONPATH=/home/user/controle-ia-travail/src PYTHONPYCACHEPREFIX=/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/cache-p /home/user/controle-ia-travail/.venv/bin/python -B -P -m controle_ia.temoin_bailey.lecture_scellee_v3 --dossier /home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/factice/sortie --sortie /home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/sortie-factice-v1.json --attendu /home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/attendu-factice-v1.json
PYTHONPATH=/home/user/controle-ia-travail/src PYTHONPYCACHEPREFIX=/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/cache-p /home/user/controle-ia-travail/.venv/bin/python -B -P -m controle_ia.temoin_bailey.lecture_scellee_v3 --controler /home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/sortie-factice-v1.json --attendu /home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/attendu-factice-v1.json --dossier /home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/factice/sortie --empreinte 1c5788293a7fb911bfc2c29f31f30ed2ad1a7dd9c6131cd1523db8243effa50d
```

- `<racine>` : `/home/user/controle-ia-travail`. `<P>` : `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/cache-p`, absent au premier `--calculer-attendu` (et après). Répertoire courant des
  exécutions : `/home/user/controle-ia-travail`, sans effet (`-P`).
- Aucune commande corrigée : la commande a abouti au premier essai factice.

## 6. Vérification des chemins

- Script `/home/user/controle-ia-travail/docs/notes/reproduction-attaque-publiee-v1/gabarits-cloture-v4/verifier_chemins_cloture_v4.py`,
  empreinte `2560a78ae15477afb91de3ee91dfbf256b84d23a4bc550165265b9b1cd50922e`. Il est joué par l'étape `e2-chemins`
  des commandes remplies (`python -I -B`, arguments `--racine`, `--dossier-lu` a et b, `--attendu`, `--sortie`,
  `--cache-p`, `--factice-dossier`, `--factice-attendu`, `--factice-sortie`, `--note`, `--autre` pour le journal, le
  répertoire factice et les rapports des lecteurs, `--pousse`), avec `git check-ignore` sur les chemins poussés.
- Résultats : `2026-11-19T11:49:07Z e2 : vérification des chemins : conforme` (avant le premier `--calculer-attendu`), puis la même
  vérification, conforme, avant chaque attendu et avant l'essai factice.
- Chemins vérifiés : voir § 7. Aucun chemin neuf pris ensuite.

## 7. Chemins absolus

| Rôle | Chemin absolu |
|---|---|
| Dossier lu a | `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/lecture-assemblee-v1` |
| Dossier lu b | `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/confirmation-assemblee-v1` |
| Attendu a / b | `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/attendu-a-v1.json` / `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/attendu-b-v1.json` |
| Sortie a / b | `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/sortie-a-v1.json` / `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/sortie-b-v1.json` |
| Cache `<P>` | `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/cache-p` |
| Dossier factice / attendu factice / sortie factice | `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/factice/sortie` / `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/attendu-factice-v1.json` / `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/sortie-factice-v1.json` |
| Note de clôture (ce fichier) | `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/note-cloture-confirmation-bailey-v1.md` |
| Rapport du lecteur a / b | `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/rapport-lecteur-a-v1.md` / `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/rapport-lecteur-b-v1.md` |
| Journal de consignation | `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/journal-cloture-v1.txt` |

## 8. Essai factice

- Dossier factice `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/factice/sortie`, construit par programme sans aucune pièce réelle : `poste_local` des essais du
  § 4, 21 tours (`tests/test_temoin_bailey_condition6_v3.py`).
- Attendu factice `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/attendu-factice-v1.json`, empreinte
  `0bbe0909ac51c9788ef63116734ed7fc6fdaa36be217f6cf6f1d1dd788ac1ac7`. Ses champs `commit`, `code` et `environnement`
  sont égaux à ceux des attendus réels a et b (`2026-11-19T11:50:28Z e4 : champs commit, code, environnement de l'attendu factice et des attendus réels : égaux`).
- Lecture factice : `2026-11-19T11:50:31Z e4 : lecture factice : {"empreinte_sortie": "1c5788293a7fb911bfc2c29f31f30ed2ad1a7dd9c6131cd1523db8243effa50d", "issue": "aboutie"}`. Issue « aboutie ». Contrôle factice : `2026-11-19T11:50:31Z e4 : contrôle factice : {"controle": "conforme"}`.
- Ordre : attendus réels à 11:49:18Z, essai factice de 11:49:25Z à 11:50:31Z, cette note ensuite.

## 9. Suite fixée

- **Lecture** : une fois par verdict, dans les 24 h qui suivent cette note, par la commande du § 5 (étape
  `e6-lecture a`, puis `e6-lecture b`). L'empreinte et l'issue rendues sont consignées sans ouvrir la sortie : ligne
  « lancée », puis ligne rendue et code de retour. Une seconde lecture du même verdict est refusée. Une exécution sans
  sortie scellée est rejouée une fois par `e6-rejeu`.
- **Lecteurs** : deux lecteurs neufs distincts, lancés ensemble dans les 24 h qui suivent la dernière sortie consignée,
  sur `/home/user/controle-ia-travail/docs/notes/reproduction-attaque-publiee-v1/gabarits-cloture-v4/consigne-lecteur-bailey-v4.md`, empreinte
  `a1c94f30ae4112d9d9575f62f9d5e0197be012fee03ec952bb45bb396f6a2546` (gabarit v4, avant remplissage). La consigne
  remplie de chaque lecteur, chemin absolu et empreinte, est consignée au lancement.
- **Commandes** : `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/commandes-cloture-bailey-v4-rempli.sh`, empreinte
  `9fc3adae40d17c5d14750c8e4f14568ce82b061d37639b825ed5a4e3fd408cc7`. C'est le gabarit scellé `d7fb9df4…` dont seules
  les 16 lignes de paramètres sont remplies. Journal de consignation : `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/journal-cloture-v1.txt`.
- **Contrôle final** : `--controler` pour chaque sortie, avec l'attendu et le dossier nommés ici et l'empreinte
  consignée. Une fois par sortie ; une commande qui ne démarre pas vaut « écart ». Joué dans un seul arbre ;
  `e6-pousser` est rejoué avant tout changement d'arbre ; une ligne e8 « lancé » sans ligne de résultat vaut « écart ».
  L'environnement du contrôle final (e7) n'est recréé qu'après la dernière commande sur un dossier réel.
- **Poussée refusée en non-fast-forward** (`e6-pousser`) : ni pull ni merge. Voie fixée ici, avant la poussée : le
  contrôle final est joué dans l'arbre principal, sans branche neuve (la session ne pousse que sur sa branche) ; le
  refus, s'il arrive, est consigné au journal.
