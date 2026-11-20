# Rapport du rédacteur — additif des interrupteurs de l'orchestrateur v69, version 4 — v1

- Rédacteur neuf, modèle F. Écrit le 2026-11-20 ; relevé de `date -u` avant l'écriture des pièces : 06:05:45Z. Python 3.13.18.
- Mandat : `docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v69/mandat-redacteur-additif-orchestrateur-v69-v4-v1.md` (`3163abf1db7ff2210a70e7595f483c69be1e0a09403593b61d7a6f021b08f2d2`, compagnon vérifié par `env -C` et `sha256sum -c` avant tout autre geste). V69 désigne ce dossier.
- Dossier de travail (noté D) : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-additif-orchestrateur-v69-v4/`.
- Processeur seul. Aucune écriture dans le dépôt, aucun commit, aucun lancement de l'orchestrateur, du lanceur ni de l'organisme, aucune dépense, aucun appel à un fournisseur de modèles. **Aucun refus de permission, de classifieur ni de garde.** Aucun allumage n'est accordé par cette pièce. Aucun identifiant de modèle.

## 0. Verdict

Les cinq corrections du contrôle v2 → v3 (1, 2, 3, 3 bis et 4) sont portées à la lettre, par l'outil, dans une pièce neuve : additif v4, 9 remplacements (5 corrections, 4 de tenue). La v3 est intacte. Le cadre ne change pas. Aucun écart au texte des corrections. La v4 n'est pas contre-lue : son différentiel avec la v3 est à contrôler par un lecteur qui ne l'a pas écrite (règle R2).

## 1. Ce qui a été vérifié avant d'écrire

| pièce | sha256 | vérification |
|---|---|---|
| `V69/controle-differentiel-additif-orchestrateur-v69-v2-v3-v1.md` | `12bbec8ded9c0e22eb257ebc03e193a7ec02d4cab2294c3fda036a5e904f7a4c` | `sha256sum -c` du compagnon : OK ; lu en entier |
| `V69/additif-interrupteurs-orchestrateur-v69-v3.md` | `f71e3a551c820ccabf5e7540dba8b4c1d1569386e069e94f0a710bf9d7ce9cba` | `sha256sum -c` du compagnon : OK ; lu en entier |
| `V69/rapport-redacteur-additif-orchestrateur-v69-v3-v1.md` | `4446464deb60787d8d2b3544e29824ece1914ace7b0c89841c51fddeedf9da3a` | `sha256sum -c` du compagnon : OK ; lu en entier |
| `scripts/remplacer_texte_exact_v1.py` | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` | recalculée ; outil lu en entier avant l'appel |

Chacun des neuf textes anciens du JSON a été compté sur la v3 par `grep -c -F -e` avant l'appel : 1 pour chacun (règle R-4067). L'outil a rendu « FAIT : 9 remplacement(s) », sans avertissement.

## 2. Pièces rendues (toutes dans D, chacune avec son compagnon `.sha256`)

| fichier | sha256 |
|---|---|
| `additif-interrupteurs-orchestrateur-v69-v4.md` | `cb352811f0202aa530fa4fd94de1d7ed4e6a8d589584c06c24c915e3c73bb578` |
| `remplacements-additif-v3-vers-v4-v1.json` | dans son compagnon |
| `additif-interrupteurs-orchestrateur-v69-v4.md.journal-remplacements-v1.json` | dans son compagnon (écrit par l'outil) |
| `differentiel-additif-v3-vers-v4-v1.diff` (`diff -u`, v3 → v4) | dans son compagnon |
| ce rapport | dans son compagnon |

Le différentiel a été relu en entier : quatre blocs, neuf zones sur sept lignes, et rien d'autre.

## 3. Les 9 remplacements

| rang du JSON | nature | lieu | ancre comptée |
|---|---|---|---|
| 1 | tenue | titre : « v3 » devient « v4 » | 1 |
| 2 | tenue | ligne de version : mention de la version 4 (quatrième rédacteur, relevé d'heure), la v3 nommée avec son empreinte | 1 |
| 3 | tenue | ligne « Statut », partie en gras : le différentiel de la v3 contrôlé (à corriger, cinq corrections), « cette v4 ne l'est pas » | 1 |
| 4 | tenue | ligne « Statut » : ce que la v4 porte (les cinq corrections du contrôle v2 → v3, nommé avec son empreinte), son différentiel avec la v3 à contre-lire | 1 |
| 5 | correction 1, à la lettre | ligne « Statut » : « cet additif change » | 1 |
| 6 | correction 2, à la lettre | § 1.2, dernier alinéa : « dans une version neuve » | 1 |
| 7 | correction 3, à la lettre | § 1.2, « Ce que (a′) lève » | 1 |
| 8 | correction 3 bis, à la lettre | tête de l'additif : « Aucun des trois rédacteurs (v1, v2, v3) » | 1 |
| 9 | correction 4, à la lettre | § 6, garde 6, artefact | 1 |

## 4. Écarts et points laissés tels quels, à trancher par le contrôle

Aucun écart au texte des corrections ni à la tenue que le mandat nomme. Trois points signalés, laissés tels quels :

1. **« Aucun des trois rédacteurs (v1, v2, v3) »**, dans une v4. La correction 3 bis est portée à la lettre. Il y a maintenant un quatrième rédacteur, et je n'ai pas lu le code non plus. La phrase reste vraie de ceux qu'elle nomme, mais ne dit rien du quatrième ; c'est le même défaut de tenue que le point 7 du rapport de la v3.
2. **La ligne « Mandat » ne cite pas le mandat de la v4.** Le mandat borne la tenue au titre, à la ligne de version et au statut ; je n'ai pas touché cette ligne. Le mandat de la v4 n'est donc nommé nulle part dans la pièce ; il l'est ici, avec son empreinte.
3. **Dans la ligne « Statut », le remplacement de rang 4 remplace « Son différentiel avec la v2 est à contre-lire »** : la phrase de la v3 sur son propre différentiel disparaît, puisque ce différentiel a été contrôlé (dit dans la partie en gras, rang 3) ; la phrase neuve vise le différentiel de la v4 avec la v3.

Les points jugés « non exigé » par le contrôle (quatre mentions de la réserve d'inscription, `GO-2026-11-20-11` sur la seule ligne « Mandat », § 9, réserve 1, (b), deux parenthèses au § 5.2) n'ont pas été touchés. La proposition de la correction 5 (§ 5 du rapport de la v3) n'est pas réécrite.

## 5. Ce que je n'ai pas fait

- Je n'ai lu ni le code de l'orchestrateur, ni le cadre v3, ni le registre des accords, ni les pièces citées par l'additif : seulement le mandat, le contrôle, l'additif v3, le rapport de la v3 et l'outil.
- Je n'ai pas rejoué l'outil une seconde fois pour comparer à l'octet.
- Rien n'est copié dans V69 : la pose de la pièce, son contrôle et son scellement sont à la session qui m'a mandaté.

— rédacteur neuf, modèle F
