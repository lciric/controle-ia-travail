# Code de l'instrument et de l'analyse du bras A des organismes discrets, version 13 — note du rédacteur — v1

Un seul changement, demandé par Lazar comme le dernier avant de cesser de durcir le code.

- **Rédacteur** : Claude Fable 5.2 (`claude-fable-5-2`). À contre-lire par un autre modèle.
- **Référence** : la vérification du code de la version 12 (`16820e4d5383cfbcf9a11e25de8fa9a4f633ec612554e3c627add33be0f76091`), partie 3, choix 1. Le brouillon 35 reste le texte de référence des modules (`e62b4caec484f53c2afde2c7361136434eaa15ddb15b2f0e609c64edc3f757a2`) ; le brouillon 36 est en cours d'écriture.
- **Interdits tenus** : aucun interne de moniteur ouvert ; aucune fiche de l'organisme d'idéation ; aucune réponse de l'essai de mesure ; aucune clé ; aucun appel réseau ni appel de modèle ; aucun sous-agent ; aucune dépense. `registres/`, `.claude/`, le journal et `prereg/` non touchés. Rien de committé. Aucun fichier existant modifié.
- **Heure** : 2026-11-20, 05:00Z.

## 1. Le changement

Dans la reprise de l'étape (n), **les vingt lectures de la sortie refaite sont confrontées à celles d'origine avant l'acte de reprise** (`ouvrir_la_reprise_de_l_etape_n`), comme les gardes du rangement et de la provenance.

- Une sortie refaite incohérente scelle son constat d'écart, puis la fonction s'arrête par une garde ordinaire : ni acte, ni événement, ni fichier d'arrêt.
- **La ligne de GO n'est pas dépensée.** Elle attend une sortie refaite cohérente, et l'acte lie la première.
- Une autre sortie cohérente donnée ensuite sous la même ligne est refusée : une ligne n'ouvre qu'une reprise.
- Le constat d'écart reste scellé et compté au rapport.
- À la version 12, la confrontation venait après l'acte : une seule sortie fautive dépensait la ligne et fermait l'étape (n) de la course sans retour.

Rien d'autre ne change dans le code.

## 2. Fichiers

Tous neufs, scellés, non suivis par git.

| fichier | empreinte | ce qui change |
|---|---|---|
| `src/controle_ia/organismes_discrets/analyse_bras_a_v13.py` | `a7ebf29f653d417a4f211f9809576a0e70b91ae7840759607c6f3cb7f84946cf` | le changement |
| `src/controle_ia/organismes_discrets/verdicts_bras_a_v13.py` | `ae6562893d9d709ce386538d8fbe2d1d1600f7e93ae9bcfbed33841aee2e8920` | le seul module d'analyse importé |
| `src/controle_ia/organismes_discrets/cloisonnement_bras_a_v13.py` | `fa915de2a81b27751860479d2cfe6472dabb004d4790dafd186210aacd0604d6` | l'analyse et la garde de la version 13 rejoignent les programmes autorisés |
| `tests/aide_bras_a_v13.py` | `cb1a0d03a77db2b7fd86e3ed3b954ed03b64f1d7acaed9da72fe0da87075c2dc` | le module d'analyse importé |
| `tests/test_analyse_bras_a_v13.py` | `41faec7afaa51a51fcd811e5137eea4b2fd672f4168e6e907d3f666de099d5a4` | 74 essais ; un essai récrit pour le changement |
| `tests/test_verdicts_bras_a_v13.py` | `88e0912b12336b6a6eafde0482eaa9fd489aed5a993ebd96d25dd303adb07bf9` | 27 essais ; les modules importés |
| `tests/test_cloisonnement_bras_a_v13.py` | `f72341457e7fad35faad84b205499834d9d8bebf8201ed3a2d01151a17f7cbda` | 62 essais ; les noms des programmes autorisés |

**Pourquoi trois modules et non un.** Les verdicts importent l'analyse : sans version 13, ils auraient tourné sur l'analyse de la version 12, à côté de celle de la version 13. La garde statique porte la liste des programmes autorisés à lire le fichier des scores : l'analyse de la version 13 devait y entrer.

**Modules qui restent en version 12, importés tels quels** : `arrets_bras_a_v12.py`, `configuration_bras_a_v12.py`, `depots_bras_a_v12.py`, `graines_bras_a_v12.py`, `mesures_bras_a_v12.py`, `permutation_etiquettes_bras_a_v12.py`. Le programme du constat reste `scripts/constat_de_lancement_discretion_bras_a_v5.py`, à la même empreinte (`fd5fddcd893e2cee91765ced911948009eb09ebd3b2382bc585fb7e4700ce290`). Leurs essais restent ceux de la version 12.

## 3. Essais

- **331 essais passent, en 78 secondes** : 74, 27 et 62 dans les trois fichiers de la version 13 ; 110, 9 et 9 dans les fichiers de la version 12 gardés ; 36 et 4 dans les deux fichiers nommés.
- **Commande** :
  `PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_analyse_bras_a_v13.py tests/test_verdicts_bras_a_v13.py tests/test_graines_bras_a_v12.py tests/test_cloisonnement_bras_a_v13.py tests/test_permutation_etiquettes_bras_a_v12.py tests/test_mesures_bras_a_v12.py tests/test_reponses_lecteurs_v5.py tests/test_epreuves_couverture_bras_a_v3.py`
- Le dernier passage a été fait après le scellement des trois modules.
- **L'essai du changement** (`test_les_vingt_lectures_refaites_confrontees_a_celles_d_origine_en_fractions_exactes`) :
  1. une sortie refaite incohérente, d'un écart que la virgule flottante ne voit pas : refusée, constat scellé, aucun acte ;
  2. la même, redonnée : même refus, rien n'est réécrit ;
  3. une seconde sortie incohérente sous la même ligne : son constat, toujours aucun acte ;
  4. **une sortie cohérente sous la même ligne : l'acte la lie**, et l'étape (n) se joue sur elle ;
  5. une autre sortie cohérente sous la même ligne : refusée ;
  6. l'issue de la livraison d'origine reste « non rapportées : livraison refusée » tant qu'aucune reprise n'aboutit.

## 4. À regarder

- **Une branche devenue sans objet, laissée telle quelle.** Le libellé « non rapportées : livraison refaite incohérente » n'est plus dit par aucun chemin ordinaire : une sortie incohérente n'a pas d'acte, et `issues` refuse une pièce qui n'a rien ouvert. La branche reste dans le code, comme demandé. Relevé, point 1.
- **L'analyse de la version 12 reste autorisée par la garde statique**, comme toutes les versions antérieures. C'est au texte de nommer la version 13 et son empreinte. Relevé, point 2.

## 5. Portée de mes lectures et méthode

- **Lu** : la vérification du code de la version 12, partie 3 ; mes fichiers de la version 12.
- **Non lu** : les autres parties de cette vérification, le brouillon 36, les registres, tout chemin cloisonné.
- **Méthode** : copie mécanique des sept fichiers touchés, puis remplacements exacts par programme. Rien n'a été scellé avant le passage des essais.
