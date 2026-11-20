# Compte rendu de l'exécution de la mesure « portée à 200 » de la ligne 3 — chronométrage puis mesure — v1

Pièce de travail (classe C), écrite le 2026-11-20 par l'exécutant neuf, sur le mandat `mandat-executant-portee-200-v1.md` (`6e7988a24342eefcaf87b3551b4ec3dd12f6c2799c021618d5dde8bcd745ff89`) et son erratum 1 `mandat-executant-portee-200-v1-erratum-1.md` (`34a3c5d28392d789139fdcf24b3bbad36d3a885364bb602955aaaaacaa0e7baf`), les deux empreintes recalculées et égales à celles données, les deux lus en entier. Ce qui fait foi : l'additif 5 scellé, lu en entier.

**Aucune valeur de mesure ici.** Je n'ai ouvert ni le fichier de résultat, ni le manifeste de la mesure, ni le manifeste du chronométrage, ni le journal d'écran de la mesure. Je n'ai rien lu de l'étage 1. Aucun commit, aucune poussée, aucun appel de modèle, aucune dépense.

## 1. Vérification de l'environnement (point 1)

- 11:36:20Z — `python3 -B /home/user/controle-ia-travail/scripts/verifier_environnement_agent_v1.py` : code 0 ; `anomalies` vide ; `statut` « lu » ; `programme_sha256` `9714a00f05b66b6f0f3c901fc700ea30b07cb3c3fda302947f276dca5fea4d74` ; Python 3.13.18, `/usr/local/bin/python3`, pas d'environnement virtuel.

## 2. Vérifications avant lancement (point 2), entre 11:36:20Z et 11:37:18Z

| vérification | commande | résultat |
|---|---|---|
| compagnon de l'additif 5 | `env -C /home/user/controle-ia-travail/prereg/organisme-auto-conception-v9 sha256sum -c additif-5-code-preenregistrement-ligne-3-portee-200-v2.md.sha256` | OK ; empreinte du compagnon `581e97e5fb6d390378ce94f32f0057b55afa77ce1831d480f4b317c1c0eaa34c`, égale à HEX |
| tête du dépôt | `git -C /home/user/controle-ia-travail rev-parse HEAD` | `5c6ea3010e4f31a0428a96eb70c369b4a2ddd222` |
| commit du code dans la tête | `git -C /home/user/controle-ia-travail merge-base --is-ancestor cce6f2341eb74b5730f4a9aaf77266b139a3e20b HEAD` | code 0 |
| dix fichiers à la racine du dossier du code | `env -C DOSSIER_DU_CODE sha256sum -c F.sha256`, un appel par fichier | dix fois OK |
| quatre fichiers de `differentiels-v3-v4/` (erratum 1) | `env -C DOSSIER_DU_CODE/differentiels-v3-v4 sha256sum -c G.sha256`, un appel par fichier | quatre fois OK |
| égalité à la table de l'additif 5 (§ 2.1 à 2.3) | `env -C DOSSIER_DU_CODE sha256sum` sur les quatorze fichiers nommés | quatorze empreintes égales à la table, une à une |
| dossier du code sans modification non commitée | `git -C DOSSIER_DU_CODE status --porcelain .` | vide |
| interpréteur | `command -v python3` ; `python3 --version` | `/usr/local/bin/python3` ; `Python 3.13.18` |
| numpy | `python3 -m pip show numpy` | `Version: 2.5.3` |
| dossiers de sortie absents | `test -e` sur `DOSSIER`, `DOSSIER_NEUF`, parent `execution-portee-200-v1` | voir la réserve 1 ; absence confirmée par `stat` du parent : « No such file or directory » |
| variables de chemin | `printenv BANC_LIGNE_3_CHEMIN` ; `printenv CHRONOMETRAGE_LIGNE_3_CHEMIN` | code 1 pour chacune, sortie vide : non posées |

`DOSSIER_DU_CODE` = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/code-portee-200-v4`.

Aucun écart.

## 3. Chronométrage (point 3)

- Heure : 11:37:18Z (`date -u` juste avant) ; fin relevée à 11:37:23Z.
- Commande exacte :

```
env -C /home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/code-portee-200-v4 -u BANC_LIGNE_3_CHEMIN -u CHRONOMETRAGE_LIGNE_3_CHEMIN PYTHONDONTWRITEBYTECODE=1 python3 -B chronometrer_portee_200_ligne_3_v1.py --autorisation-additif /home/user/controle-ia-travail/prereg/organisme-auto-conception-v9/additif-5-code-preenregistrement-ligne-3-portee-200-v2.md --empreinte-additif 581e97e5fb6d390378ce94f32f0057b55afa77ce1831d480f4b317c1c0eaa34c --manifeste /home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/execution-portee-200-v1/chronometrage
```

- Code de retour : 0.
- Sortie d'écran, recopiée en entier :

```
duree_mesuree_du_chronometrage_secondes: 0.170
duree_mesuree_d_une_cellule_echantillon_secondes: 0.129
duree_estimee_monde_de_puissance_portee_200_secondes: 631.502
```

- Manifeste : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/execution-portee-200-v1/chronometrage/manifeste-chronometrage-portee-200-ligne-3-v1.json`, sha256 `9819b671c9e495cbb2252f3a56860b4dcdb1351b41b4f42403e8f73b92fe02e6` ; `sha256sum -c` de son compagnon : OK.

## 4. Mesure (point 4)

- Heure de lancement : 11:37:53Z (`date -u` juste avant ; même heure dans le fichier de fin).
- Commande exacte, à la lettre de l'additif 5, § 4 :

```
env -C /home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/code-portee-200-v4 -u BANC_LIGNE_3_CHEMIN -u CHRONOMETRAGE_LIGNE_3_CHEMIN PYTHONDONTWRITEBYTECODE=1 python3 -B banc_juges_scriptes_ligne_3_v4.py --portee-200 --autorisation-additif /home/user/controle-ia-travail/prereg/organisme-auto-conception-v9/additif-5-code-preenregistrement-ligne-3-portee-200-v2.md --empreinte-additif 581e97e5fb6d390378ce94f32f0057b55afa77ce1831d480f4b317c1c0eaa34c --sortie /home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/execution-portee-200-v1/mesure
```

- Mode de lancement (réserve 2) : cette commande est placée telle quelle dans un lanceur du bloc-notes, `/tmp/claude-0/-home-user-controle-ia-travail/fc9e4fb9-7931-58b9-a66b-caf66718eee3/scratchpad/portee-200/lancer_mesure_portee_200.sh`. Le lanceur n'ajoute que l'heure de début, l'heure de fin et le code de retour, qu'il écrit dans le fichier de fin. Il est lancé détaché par `nohup bash LANCEUR > JOURNAL 2>&1 &`. Le journal d'écran est `/tmp/claude-0/-home-user-controle-ia-travail/fc9e4fb9-7931-58b9-a66b-caf66718eee3/scratchpad/portee-200/journal-mesure-portee-200.txt` (je ne l'ai pas ouvert). Le fichier de fin est `/tmp/claude-0/-home-user-controle-ia-travail/fc9e4fb9-7931-58b9-a66b-caf66718eee3/scratchpad/portee-200/fin-mesure-portee-200.txt`.
- Fichier de fin, lu par moi : `debut_utc=2026-11-20T11:37:53Z`, `fin_utc=2026-11-20T11:41:50Z`, `code_retour=0`.
- Sorties, empreintes prises à 11:42:09Z par `sha256sum` sur les fichiers, sans les ouvrir :

| sortie | sha256 | `sha256sum -c` du compagnon |
|---|---|---|
| `…/execution-portee-200-v1/mesure/resultat-portee-200-ligne-3-v1.json` | `afcb453acbb7dd883f040ce6e4b11cd83d2f86facf17a976621249ab31d2d174` | OK |
| `…/execution-portee-200-v1/mesure/manifeste-portee-200-ligne-3-v1.json` | `da6a9300fb56754e8dd8baad243ab5f5fdab87a51d7fa2ccf08ab8bf51ccfbbd` | OK |

Chemin complet du dossier `…` : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges`.

## 5. Les trois sorties

| sortie | sha256 |
|---|---|
| manifeste du chronométrage | `9819b671c9e495cbb2252f3a56860b4dcdb1351b41b4f42403e8f73b92fe02e6` |
| résultat de la mesure | `afcb453acbb7dd883f040ce6e4b11cd83d2f86facf17a976621249ab31d2d174` |
| manifeste de la mesure | `da6a9300fb56754e8dd8baad243ab5f5fdab87a51d7fa2ccf08ab8bf51ccfbbd` |

Aucun refus, aucune interruption, rien n'a été relancé. Le contrôle du manifeste avant toute lecture du résultat (additif 3, § 6, point 3) revient à la mère.

## 6. Réserves et écarts de forme

1. Les trois `test -e` du point 2 ont rendu une sortie vide. L'outil ne marque pas en erreur le code 1 de `test`, alors qu'il marque en erreur celui de `printenv` : le retour était donc ambigu. J'ai confirmé l'absence par un seul `stat` sur le parent `execution-portee-200-v1`, qui a rendu « No such file or directory ». Si le parent est absent, ses deux sous-dossiers le sont aussi. Le chronométrage a ensuite créé ce dossier, et il refuse un dossier déjà présent.
2. Le mandat demande d'attendre la fin de la mesure par l'outil de tâches. Sur la consigne de la mère, je l'ai lancée détachée par `nohup`, à travers le lanceur décrit au § 4, et j'ai rendu la main sans attendre. C'est la mère qui m'a annoncé la fin ; je l'ai vérifiée sur le fichier de fin. Le lanceur et ses deux fichiers sont dans le bloc-notes de la session, et non dans le dépôt.
3. J'ai écrit hors du dépôt le lanceur, le journal et le fichier de fin, et dans le dépôt seulement ce compte rendu et son compagnon. Je n'ai rien écrit dans le dossier du code.

Exécutant neuf.
