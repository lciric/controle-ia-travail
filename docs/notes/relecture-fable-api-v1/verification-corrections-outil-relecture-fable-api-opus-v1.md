# Vérification des corrections de l'outil de relecture d'une correction par Fable 5.2 appelé par l'interface d'Anthropic

Même contre-lecteur que la contre-lecture (`contre-lecture-outil-relecture-fable-api-opus-v1.md`, `99eb9fdc…`) : Claude
Opus 5.5, 21 novembre 2026. Pièce d'instrument, classe B (GO-2026-11-21-84). Aucun appel réel ; aucun fichier de la pièce
modifié ; mutations faites dans des copies du bloc-notes de la session.

## Verdict : **conforme**

La v2 est ma copie corrigée, octet pour octet, aux seuls changements de nom près. Les sept corrections C1 à C7 sont
portées et rien n'est ajouté au code ni aux essais. Les deux textes de remplacement du rapport sont repris mot pour mot.
Sur un dossier temporaire neuf, 76 essais passent, et chacune des six mutations que j'ai rejouées sur la v2 est tuée.

## Pièces vérifiées

| Pièce | Empreinte (compagnon vérifié par `sha256sum -c`) |
|---|---|
| `src/controle_ia/relecture_fable_api_v2.py` | `c8e8506f8d7cb9487173090aa9a000c1ab217377946f55cb338a45f07ca3d7f3` — OK |
| `tests/test_relecture_fable_api_v2.py` | `89f91fa2e90e4b27bfe51c270e2cd6be7ef280363e41db227bbb00aa91123b66` — OK |
| `docs/notes/relecture-fable-api-v1/rapport-developpeur-v2.md` | `0a3bd162d7a68ce84763770e306d70b2ec13ec0640a30bbc485c15d0fa7a4946` — OK |
| v1 gardée : module, essais | `056bc4ef…`, `a3f649cf…` (inchangés) |

## 1. Égalité à la copie corrigée (diff)

`diff` entre ma copie corrigée (module `acf9ddd2…`, essais `efa04f00…`) et la v2 :
- module : quatre lignes, toutes de nom : titre « version 1 » → « version 2 » (ligne 1), nom du module dans l'emploi
  (ligne 9), `VERSION = "relecture_fable_api_v2"` (ligne 75), `prog` de l'analyseur d'arguments (ligne 689) ;
- essais : deux lignes, toutes de nom : titre (ligne 1), importation `relecture_fable_api_v2 as rf` (ligne 12).

Les autres lignes sont identiques. Les corrections C1 à C7 sont donc portées telles que je les ai écrites, et rien
d'autre n'est ajouté.

## 2. Rapport du développeur (diff v1 → v2)

- § 2, point 6 : « si le comptage échoue, pour quelque raison que ce soit : refus (code 10), rien n'est envoyé ; »
  repris mot pour mot (seule la coupure des lignes change).
- § 6, réserve 1 : « **Comptage échoué : refus.** L'appel de fumée a donné 1,76 caractère par jeton (480 caractères, 273
  jetons) ; la borne de repli de 2,5 de la v1 sous-comptait l'entrée. La v2 refuse l'envoi si le comptage échoue, pour
  quelque raison que ce soit (code 10, ligne `refus_avant_envoi` à coût nul) ; il n'y a plus de borne de repli. » repris
  mot pour mot.
- Le reste ne fait que décrire la v2 : noms des fichiers, nombre d'essais, points 3, 4 et 8 du § 2, table des essais,
  appel de fumée dit fait avec la v1, réserves 4, 5 et 9 mises à jour, réserve 10 et § 7 neufs, qui reprennent ma
  contre-lecture. Rien n'y change le fond, et je l'ai trouvé exact :
  - la table des motifs compte 23 lignes, soit 18 + 5 ;
  - « 60 de la v1, dont un remplacé par deux, et 17 neufs en tout » donne bien 76 ;
  - « compte-rendu » est refusé (sonde sur la v2 : « terme « rendu » dans un chemin ou un nom ») ;
  - l'avertissement de C7 est dit dans le préambule des refus.

  Une seule imprécision, sans correction demandée : la note d'en-tête nomme les points 3, 4 et 8 du § 2, mais le
  préambule des refus (C7) est changé lui aussi.
- Les remarques de ma contre-lecture que je n'ai pas demandé de corriger (noms en cyrillique, `ANTHROPIC_CUSTOM_HEADERS`,
  journal qui échoue après un envoi payé, kit à inscrire dans `requirements-cpu.txt`, appel de fumée de la v2) sont dites
  non appliquées et laissées à la mère. C'est juste.

## 3. Essais rejoués

`PYTHONPATH=src .venv/bin/python -m pytest -q tests/test_relecture_fable_api_v2.py tests/test_relecture_fable_api_v1.py
-p no:cacheprovider --basetemp=<dossier neuf>` : **136 passés**, soit les 76 de la v2 et les 60 de la v1, intacte.
`python -m controle_ia.relecture_fable_api_v2 --help` affiche le bon nom de module.

## 4. Mutations rejouées sur la v2

Le module v2 et ses essais sont copiés à part, chaque mutant dans son dossier avec ses essais : la configuration du dépôt
ne réimporte donc pas l'original. Le disque avait assez de place, et aucune erreur de préparation n'est apparue.

| Mutation | Résultat | Essais qui la tuent |
|---|---|---|
| témoin sans mutation | 76 passés | — |
| M2 : branche « autre raison d'arrêt » supprimée | tuée (4 échecs) | `test_autre_raison_arret_est_un_defaut[…]` |
| M3 : journal écrit après la relecture | tuée (1) | `test_journal_ecrit_avant_toute_sortie` |
| M8 : borne de repli remise au comptage | tuée (3) | `test_comptage_impossible_refuse_sans_envoi[…]`, `test_chemin_reel_comptage_500_refuse_sans_envoi` |
| M9 : compagnons non contrôlés avant l'envoi | tuée (2) | `test_compagnon_orphelin_jamais_ecrase[…]` |
| M10 : identifiant UUID non cherché | tuée (1) | `test_garde_refuse_chaque_motif[dossier 2eb82089-…]` |
| M11 : interruption non consignée | tuée (2) | `test_interruption_pendant_envoi_comptee_au_pire`, `test_sigterm_pendant_envoi_compte_au_pire` |

## Reste à la mère (rien n'est demandé au développeur)

- Inscrire `anthropic==2.12.0` dans `requirements-cpu.txt`.
- Décider s'il faut un appel de fumée de la v2 (un appel, sous le même GO).
- Décider des remarques que j'ai laissées sans correction demandée.
