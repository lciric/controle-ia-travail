# Vérification du code de l'instrument et de l'analyse du bras A, version 13 — v1

- **Contre-lecteur** : Claude Opus 5.5 (`claude-opus-5-5`), qui n'a écrit ni le code ni le texte. Rédacteur du code : Claude Fable 5.2.
- **Date** : 2026-11-20. Arbre au commit `7a9248f39`. Je n'ai modifié aucun fichier hors celui-ci.
- **Objet** : le seul changement que prévoyait la condition 4 de ma vérification de la version 12 (`16820e4d5383cfbcf9a11e25de8fa9a4f633ec612554e3c627add33be0f76091`). Dans la reprise de l'étape (n), les lectures refaites sont maintenant confrontées à celles d'origine **avant** l'acte de reprise. Mot de Lazar « a a » : on cesse de durcir le code après ce changement.
- **Pièces, conformes à leur compagnon** :
  - analyse, version 13 : `a7ebf29f653d417a4f211f9809576a0e70b91ae7840759607c6f3cb7f84946cf` ;
  - verdicts, version 13 : `ae6562893d9d709ce386538d8fbe2d1d1600f7e93ae9bcfbed33841aee2e8920` ;
  - garde statique du cloisonnement, version 13 : `fa915de2a81b27751860479d2cfe6472dabb004d4790dafd186210aacd0604d6` ;
  - aide des essais : `cb1a0d03a77db2b7…` ; essais de l'analyse : `41faec7afaa51a51…` ; essais des verdicts : `88e0912b12336b6a…` ; essais du cloisonnement : `f72341457e7fad35…` ;
  - les neuf modules de la version 12 répondent toujours à leurs empreintes, et le programme du constat en version 5 aussi (`fd5fddcd893e2cee…`).
- **Interdits tenus** :
  - je n'ai ouvert ni empreinté aucun interne de moniteur ni aucun chemin cloisonné ; la garde statique n'a tourné, de ma main, que sur un faux dépôt ;
  - je n'ai lu ni les fichiers d'essais neufs étrangers au bras A (`test_t06_*`, `test_lancer_course_ideation_*`), ni aucune fiche de l'organisme d'idéation, ni aucune réponse de l'essai de mesure, ni le registre ;
  - aucune clé, aucun appel réseau ni de modèle, aucun sous-agent, aucune dépense ;
  - j'ai écrit un seul fichier, celui-ci, et rien n'est committé.

## Verdict

**Le changement est juste, et rien d'autre n'a changé : la version 13 est engageable.** Une sortie refaite incohérente scelle son constat d'écart et n'ouvre rien : ni acte, ni événement, ni fichier d'arrêt. La ligne de GO n'est pas dépensée. Sous la même ligne, l'acte lie la première sortie refaite cohérente, et une autre sortie cohérente est ensuite refusée. J'ai aussi vérifié qu'**un même arrêt n'ouvre jamais deux reprises** : une ligne restée inutilisée ne rouvre rien une fois qu'une autre ligne, sur le même arrêt, a écrit son acte.

**L'ordre des gardes est sans danger.** Un constat d'écart peut se sceller sous un contrôle de lancement malsain, mais il ne dit rien, ne dépense rien et n'ouvre rien. Les autres points du relevé sont des précisions au texte ; aucun ne demande de code.

| question | réponse |
|---|---|
| 1. Le changement est-il juste ? | **oui** (partie 1) |
| 2. Rien d'autre n'a-t-il changé ? | **oui**, comparaison par programme (partie 2) |
| 3. Les essais d'attaque de la version 12 | **même issue partout**, sauf aux trois endroits que le changement visait (partie 3) |
| 4. Essais de la commande de la note | **331 passent**, en 78,3 secondes |
| 5. Les points du relevé, dont l'ordre des gardes | **sans danger** ; précisions au texte (partie 4) |

## 1. Le changement est-il juste ?

Pièces : `verification-code-v13/attaques5_v13.py` (`14e483537bf83a25…`), sortie `193073bd4d3905f7…` ; `verification-code-v13/ordre_v13.py` (`615c8de52491819d…`), sortie `25581b4275ffb6c7…`. Tout est dans le bloc-notes de la session ; données et registres fabriqués.

**Ce que fait le code** (`ouvrir_la_reprise_de_l_etape_n`). La confrontation est placée après la reconnaissance de la sortie d'origine et avant les contrôles de lancement et l'acte. Une sortie incohérente lève une garde ordinaire, qui n'est pas l'événement d'arrêt. Le retour, pour une sortie cohérente, porte toujours `lectures_refaites_coherentes` vrai et `grandeurs_de_l_etape_n` `None`.

| essai | résultat |
|---|---|
| Sortie refaite incohérente, d'un écart que la virgule flottante ne voit pas | refusée ; 1 constat d'écart, **0 acte** |
| La même, redonnée | même refus ; rien n'est réécrit |
| Issue de la livraison d'origine pendant ce temps | « non rapportées : livraison refusée (garde : fichier des scores par unité) » |
| Sortie cohérente sous la même ligne | **l'acte la lie** ; l'étape (n) se joue sur elle |
| L'incohérente, redonnée après l'acte | refusée (« ligne déjà portée par un acte de reprise ») |
| **Une autre sortie cohérente sous la même ligne** | **refusée** (essai de la suite et essai d'attaque de la version 12, partie 4) |
| Ligne 1 non dépensée (sortie incohérente), puis ligne 2 sur le même arrêt, qui ouvre ; puis la ligne 1 avec une autre sortie cohérente | ligne 2 : ouvre ; **ligne 1 : refusée** (« la ligne ne cite pas le fichier d'arrêt de la livraison refusée à reprendre ») ; le fichier des scores de la troisième sortie n'est pas lu |
| Deux lignes inscrites ensemble sur le même arrêt, deux sorties cohérentes | la première ouvre ; **la seconde est refusée** |
| Constat d'écart planté à la main pour une sortie **cohérente** | refusée (« constats incohérents ») : on ne bloque une reprise qu'en falsifiant le dossier, et le blocage reste fermé |
| Fichier de l'étape (m) d'origine | intact dans tous les essais |

Une ligne restée inutilisée devient sans objet dès qu'un acte reprend l'arrêt qu'elle cite. Il n'y a donc pas deux résultats de l'étape (n) pour un arrêt.

## 2. Rien d'autre n'a-t-il changé ?

J'ai comparé chaque fichier de la version 13 à celui de la version 12, après avoir remplacé `_v12` par `_v13` dans ce dernier.

- **Analyse** :
  - imports : configuration, dépôts, graines, permutation des étiquettes et arrêts restent en version 12 ;
  - documentation : la tête du module, un commentaire, la documentation de `ouvrir_la_reprise_de_l_etape_n` ;
  - code : **trois changements, tous dans `ouvrir_la_reprise_de_l_etape_n`** — la confrontation déplacée avant le bloc de l'acte, avec sa garde ordinaire ; la ligne de la version 12 qui confrontait après l'acte, retirée ; les deux champs du retour, fixés à vrai et à `None`.
- **Verdicts** : la tête du module et les imports (analyse en version 13 ; configuration, dépôts et arrêts en version 12). Aucun autre écart.
- **Garde statique** : la tête du module, et les deux listes des programmes autorisés, qui gagnent `analyse_bras_a_v13.py` et `cloisonnement_bras_a_v13.py`. Aucun autre écart, aucune expression régulière changée.
- **Aide des essais** : la tête et les imports.
- **Essais des verdicts** : la tête et les imports.
- **Essais du cloisonnement** :
  - les noms des modules attendus ;
  - la liste des autorisés, renommée `…_VERSION_13`, qui garde graines et arrêts en version 12 ;
  - l'ensemble des modules ouverts attendu.
- **Essais de l'analyse** : la tête, les imports, et le seul essai de la confrontation, récrit dans le sens du changement (partie 1).
- **Modules de la version 12 et programme du constat** : empreintes inchangées.

## 3. Les essais d'attaque de la version 12

J'ai rejoué les huit pièces de la version 12, recâblées sur l'analyse, les verdicts, l'aide et la garde statique de la version 13 (le reste en version 12), et comparé les sorties, chemins temporaires et empreintes masqués.

- **Identiques** :
  - les autres voies vers deux résultats (copie de configuration, effacements, révocation d'une configuration lue, second fichier des grandeurs, rejeu de l'étape (n)) ;
  - la garde du registre au constat ;
  - les formes des « mêmes lectures » ;
  - la garde statique sur faux dépôt, sous crochet d'audit : sortie au même octet, `c5ffaaace864d5bd…`, aucune ouverture sous un chemin cloisonné ;
  - les vingt-quatre modules plantés ;
  - la fouille de quatre cents livraisons : sortie au même octet, `bc078c811e7e1e46…`.
- **Changées, exactement là où le changement le voulait** :
  - `attaques_v13` : la sortie incohérente est refusée sans acte (0 acte, 1 constat), puis la sortie cohérente **s'ouvre sous la même ligne** ; `issues` sur l'incohérente est refusée (« ni une livraison refusée, ni une livraison refaite lue »), au lieu de dire « non rapportées : livraison refaite incohérente » ;
  - `attaques3_v13` : l'ouverture incohérente est refusée ; la lecture du fichier des scores sous elle est refusée plus tôt, par le constat de lancement, puisqu'aucun acte ne la porte ; la ligne neuve qui cite l'arrêt d'origine **ouvre** maintenant, puisque l'arrêt n'est porté par aucun acte.

Les pièces sont dans `verification-code-v13/`. Scripts : `attaques_v13.py` `63744c3d…`, `attaques2_v13.py` `2b968a58…`, `attaques3_v13.py` `337c81fa…`, `attaques4_v13.py` `e4e76f5c…`, `abandon_v13.py` `f078007a…`, `audit_cloisonnement_v13.py` `93e97d7b…`, `attaques_cloisonnement_v13.py` `bc6dbd63…`, `fuzz_livraison_v13.py` `6cb8a466…`. Sorties : `623a8654…`, `48ea11dd…`, `41f82550…`, `aa115c77…`, `78318c94…`, `c5ffaaac…`, `060e09fb…`, `bc078c81…`.

## 4. Les points du relevé, et l'ordre des gardes

| point du relevé | jugement |
|---|---|
| 1. Le libellé « non rapportées : livraison refaite incohérente » n'a plus d'objet | Confirmé par essai : `issues` refuse la sortie incohérente, et l'issue reste celle de l'arrêt d'origine. Laisser la branche est sans danger : elle ne jouerait que si une pièce scellée changeait après son acte, et elle refuse alors. **Précision au texte**, dans les mots du relevé : une sortie refaite incohérente n'est ni refusée ni reprise, elle laisse un constat scellé, compté au rapport, et aucune issue ne se dit sur elle. |
| 2. Le texte doit nommer l'analyse de la version 13 | Juste. La configuration épingle le module du côté habilité et le programme du constat, **pas le module d'analyse**, et la garde statique autorise encore la version 12. Quelle version tourne relève donc de la procédure : le texte nomme les trois modules de la version 13, les six de la version 12 et le programme du constat en version 5, avec leurs empreintes ; le manifeste de la course consigne l'empreinte du module d'analyse employé, et la contre-lecture du manifeste la vérifie. **Garde de procédure, à dire comme telle.** |
| 3. Ordre des gardes : un constat d'écart peut se sceller sous un contrôle malsain | **Sans danger**, voir ci-dessous. Précision au texte. |
| 4. Aucun plafond au nombre de sorties incohérentes sous une ligne | Sans danger : une sortie incohérente ne fait lire aucun fichier des scores, son constat ne porte que quatre empreintes, et la confrontation ne dépend que des octets de deux pièces déjà scellées. Aucune pêche n'est possible. Le rapport les compte ; le texte peut dire qu'un compte non nul est une réserve du rapport, signe d'un défaut du côté habilité. |
| 5. Ce que rend l'ouverture (deux champs devenus constants) | Sans danger ; à dire au texte ou à laisser. |
| 6. Configuration copiée dans un autre dossier de course | Hors du changement ; elle relève de la procédure du brouillon 36, comme je l'ai jugé à la version 12. |

**L'ordre des gardes, éprouvé.** Le code joue, dans cet ordre : le constat de lancement, le rangement, la ligne de GO dans l'état figé, la provenance, la sortie d'origine, la confrontation, les contrôles de lancement, puis l'acte. Essai (`ordre_v13`) :

1. un contrôle de lancement malsain : la ligne de GO employée est révoquée au registre courant ;
2. une sortie incohérente : son constat d'écart est scellé, 0 acte ;
3. une sortie cohérente sous ce contrôle : **refusée** par le contrôle, 0 acte ;
4. `issues` : rien sur l'incohérente, et la livraison d'origine reste « non rapportées : livraison refusée » ;
5. un contrôle refait et sain : la cohérente ouvre.

Dans l'essai, le registre fabriqué du second contrôle ne porte plus la révocation. Dans la vraie procédure, une ligne révoquée le reste, et la reprise demanderait une ligne neuve.

Pourquoi c'est sans danger :

- **Rien ne s'écrit sans un accord donné d'avance.** Un constat d'écart ne se scelle qu'après le constat de lancement sain et une ligne de reprise valide dans l'état figé.
- **Le constat ne dit rien.** Il porte quatre empreintes et le nom de l'événement ; il ne lit aucun fichier des scores et ne range aucune lecture dans un cas. Les vingt lectures confrontées sont déjà connues et scellées à l'étape (m).
- **Il ne dépense rien et n'ouvre rien** : il ne compte ni comme ouverture, ni comme acte, ni comme arrêt. Il ne change pas l'issue de la livraison d'origine.
- **Un faux ne laisse rien passer.** Planté à tort pour une sortie cohérente, il bloque, par une garde ordinaire.
- **La trace est plutôt un bien** : une sortie refaite donnée sous une ligne ensuite révoquée laisse un constat dans le dossier des arrêts.

Une seule chose à écrire : la confrontation n'est pas une lecture de la discrétion au sens de « si une révocation est entrée, la lecture ne part pas », et le rapport compte tous les constats d'écart, y compris ceux scellés sous un contrôle malsain. Déplacer les contrôles avant la confrontation serait possible mais n'apporterait rien ; je ne le recommande pas, puisque le code est figé.

## 5. Essais de la commande de la note

`PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_analyse_bras_a_v13.py tests/test_verdicts_bras_a_v13.py tests/test_graines_bras_a_v12.py tests/test_cloisonnement_bras_a_v13.py tests/test_permutation_etiquettes_bras_a_v12.py tests/test_mesures_bras_a_v12.py tests/test_reponses_lecteurs_v5.py tests/test_epreuves_couverture_bras_a_v3.py`

- **331 passent, en 78,3 secondes.**
- Sortie : `verification-code-v13/essais.sortie.txt` (`82d635d04deec847…`).
- La suite entière du dépôt n'a pas été lancée.

## 6. Ce qui reste

- **Pour le brouillon 36** :
  - nommer les modules de la version 13 et leurs empreintes ;
  - dire que le manifeste consigne l'empreinte du module d'analyse employé ;
  - le statut de la sortie refaite incohérente : ni refusée ni reprise, un constat, aucune issue, compté au rapport ;
  - l'ordre des gardes, dit tel quel, et la précision sur la révocation ;
  - l'absence de plafond.
- **Pour le code** : rien. Je ne recommande aucun changement.
- **Non vérifié ici** : le brouillon 36 lui-même.
