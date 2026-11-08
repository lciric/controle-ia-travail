# Validation scellée du nul v9 de l'organisme — sortie brute — v1

Déposé par la session mère `session_016QhUrsAjLE7txxBLhnMnyM` (lanceuse) le 8 novembre 2026, à 09:47 UTC (`date -u`). **Aucun fichier de résultat n'a été ouvert par la lanceuse** : ni `sortie/banc-tricheurs-v9.json`, ni `journaux/console-validation-v9-v1.log`. Seuls ont été lus, avant le lancement, les journaux des contrôles (`essais-nul-v9-v1.log`, `mutations-nul-v9-v1.log`), puis le code de fin.

- **Texte scellé** : `orchestrator/prereg/preenregistrement-validation-nul-v9-v1.md` du dépôt public `lciric/ideation-organism`, sha256 `54c5713d07f61b7f2bb3dd8218f4bca881a044a2b11508015db5e727d62c18fb`, commit `66dbcf1960dff4370a44e5f90d5ecc216f5b60cb`.
- **Arbre** : arbre détaché à ce commit ; après la course, seul le dossier de sortie y est nouveau (`git status` : `?? resultats/banc-tricheurs-v9-validation-v1/`).
- **Contrôles avant lancement** (ceux que demande le texte scellé) : 14 fichiers gelés conformes à sa liste d'empreintes ; `essais/test_nul_v9.py` : 37 essais et 35 sous-essais réussis ; `essais/mutations_nul_v9.py` : 43 mutations tuées pour la raison attendue sur 43, témoin 26 essais sans échec après restauration.
- **Commande** (depuis `orchestrator/`) : `/home/user/controle-ia-travail/.venv/bin/python -I -B demonstrations/banc_tricheurs_v9.py ../resultats/banc-tricheurs-v9-validation-v1 --preenregistrement prereg/preenregistrement-validation-nul-v9-v1.md --repetitions 1000 --processus 2` (Python 3.13.18, numpy 2.4.6).
- **Heures** : lancement 2026-11-08T08:16:01Z, processus 16565 ; fin relevée à 09:46:43Z (code de fin écrit à 09:46:43Z) ; **code 0**.
- **Dépense** : 0 dollar (processeur seulement).

| fichier | sha256 |
|---|---|
| `sortie/banc-tricheurs-v9.json` | `be22bf67dcbe118f05269cafda40ded31cf7003141d07a7e9131d3d0597043d7` (compagnon écrit par le banc) |
| `sortie/manifeste.json` | `84559597b8bd316d37e51f6ed56d4338d8d629b077b45e5ebdc6e7b6f7334afc` (compagnon écrit par le banc) |
| `journaux/console-validation-v9-v1.log` | `8ab0c5a80d7a587f9438a296c364ae2e26c98bab7d201241afd254e41a08582f` |
| `journaux/code-validation-v9-v1.txt` | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` |
| `journaux/essais-nul-v9-v1.log` | `15838aa66e7c9200a349de11e8252226e068d63a8afb82424bfbd01a4aef2286` |
| `journaux/mutations-nul-v9-v1.log` | `76e93dd2c56684e9e3c37446ad349a715617d31b38ad2884c2601e5844067e13` |
| `journaux/lancement-utc.txt` | `52456468f2adbbd00e41b0b0b42e5333dede74fb44c70faffe42ce667f17663a` |
| `journaux/debut-essais.txt` | `89c3bb9aa7edbb1c971deda7e0e07cf05dd81f8204dd9840ff5e852b7656441c` |

**Suite** : verdict par un lecteur neuf (ni auteur du texte, ni lanceur), selon les critères gelés du texte scellé ; verdict scellé, puis soumis à Lazar. Publication sur le dépôt public : nœud de Lazar.
