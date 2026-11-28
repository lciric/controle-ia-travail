# Vérification neuve — lentille « empreintes » — textes et gabarit de P1 (c2a, c2b)

Vérificateur neuf : je n'ai pas écrit l'extraction. Je n'ai importé aucun code de l'extracteur. J'ai lu ses sorties comme des données, et j'ai tout recalculé depuis les sources.
Date : 2026-10-20. Lecture seule. Aucun réseau. `python3 -I` partout. J'ai écrit uniquement dans ce dossier.

## Verdict

**Confirmé, avec réserves.** Toutes les empreintes annoncées par l'extracteur se retrouvent : sources, trois corps de fonctions, 30 textes, 90 prompts.
Il y a un gain que l'extracteur n'avait pas vu. Le **prompt neutre** de c2a et de c2b n'est plus seulement reconstruit : une génération plus tardive (bloc C) l'a envoyé au modèle. Ses empreintes concordent à 600 sur 600. Avec les mêmes graines, elle redonne les sorties de c2a et de c2b au caractère près dans 487 cas sur 600.
Les prompts **critique** et **éloge** restent des reconstructions. Leur règle est attestée par des générations plus tardives, mais aucune empreinte de c2a ou de c2b ne les couvre.

## Méthode et pièces

- Script principal : `verifier_empreintes_p1_v1.py` (empreinte 9e9c17db03fcf6620a84c29a2ddfb4d60273ad838bc531f84d7e7ec51ff3b3e9). Journal : `journal-verif-empreintes-p1-v1.txt` (7c053afc792ca70f6ae83c9ede355c40c2f7811ea741d983e032ef6faa9863e3). Table de mes empreintes : `empreintes-recalculees-p1-v1.json` (11480178800a9e829a5aecbca72b84719c70303c80fece8f5605ab0040116125).
- Témoin par les sorties : `temoin_sorties_v1.py` (b426f78f66190bd5e1232b5a862b351ea9a784e2d70c1c97e6800d747727b20f). Journal : `journal-temoin-sorties-v1.txt` (bdd81aa3f3b926f6b009b6ea7b2fe94d3c53b5a9c3bc62da058b5effbc1f6588).
- Balayage par empreinte de fichiers (14 232 fichiers hachés) : `balayage_empreintes_v1.py` (e2e3ce93…), sortie `sortie-balayage-empreintes-v1.txt` (40dbc62e74fd694dc455d61c48178fc0901cd216af6c121f4253e15f46f27e47).
- Recherche de mes 120 empreintes dans toutes les sources : `recherche_mes_empreintes_v1.py` (95d3c3f1…), sortie `sortie-recherche-mes-empreintes-v1.txt` (08b1a591f638c86068028d1a72771d99d1a862a9d849330ae3b0d4bf65565fe0).
- Inventaire des clés d'empreinte de prompt dans les fichiers de données : `inventaire_cles_prompt_v1.py` (9119da9f…).
- Auto-test de la convention et des extracteurs de corps : vert, 8 sur 8. Il a d'abord échoué une fois sur une attente mal écrite de ma part (ligne vide finale). Je l'ai corrigée avant toute lecture des sources.
- Les fichiers interdits (`prereg/P3-consignes-v1.md`, `textes-actions-*`) sont exclus par leur nom, sans être ouverts, dans tous mes parcours.

## (a) Empreintes des sources

Toutes conformes (journal principal, section a) :
- n200 `64894c21…a7b759e9`, b2_neu `b8818b84…e348d3`, cahier expurgé `b8c81895…52e989`.
- c2a_generations `a7c85816…6189a`, c2b_generations `ec2f7ca5…586c2`, c2a_results `6ad1a718…`, c2b_results `ae097f3d…`. Les quatre compagnons `.sha256` de `controle-ia-travail/donnees/P1-loi-attraction-v1/` concordent.
- x_common.py `ca58b557…`, c2f_prompts_effectifs `51e5ba1b…`.
- Les cinq sorties de l'extracteur portent bien les empreintes annoncées (items 4cb5fe98…, gabarit e666e5de…, prompts ab4b12a8…, script 331c73e6…, journal 3d3e35e7…).

## (b) Convention defs_sha et corps des trois fonctions

J'ai réécrit la convention depuis son énoncé dans `defs_sha_reconciliation.py` : premiers 16 caractères du sha256 du corps sans indentation commune, sans blancs aux bords, sans blancs en fin de ligne.
J'ai isolé les corps par **deux méthodes** à moi : un découpage par lignes (de `def NOM(` jusqu'à la ligne suivante en colonne 0) et un découpage par arbre syntaxique.

| Fonction | Scellé | Cellules du cahier (toutes égales, deux méthodes) |
|---|---|---|
| manual_generate | 93a2fa00e1a611ba | 0 et 6 |
| format_neutral | 38a4f0ce9b744738 | 0, 3 et 6 |
| build_eval_prompt | 11c5055abd1f7066 | 121 |

- La normalisation des blancs de fin de ligne est **inerte** : sans elle, on obtient les mêmes empreintes. Aucune ligne des corps n'a de blanc final, aucun triple guillemet, aucune tabulation.
- Les trois corps de `gabarit-p1-v1.py` sont des chaînes **identiques** aux corps du cahier, et non seulement de même empreinte.

## (c) L'expurgation n'a pas touché les corps

- La marque `<<CLE_API_EXPURGEE_PAR_ccGit_2026-08-23>>` est sur les lignes brutes 13843, 22403 et 23105, comme le dit le README de l'archive. Elle est dans les cellules **1, 35 et 37**. Les corps sont dans les cellules 0, 3, 6 et 121. L'intersection est vide.
- Les tailles concordent. L'original fait 2 453 096 octets (EXCLUSIONS.tsv, et INVENTAIRE.md du 2026-08-08), le dérivé 2 452 895 (MANIFEST.tsv). L'écart est de 201 octets, soit 3 fois 67 : chaque clé de 108 caractères est remplacée par une marque de 41.
- **Argument décisif : les sceaux sont antérieurs à l'expurgation.** 93a2fa00… et 38a4f0ce… sont dans la méta de c2a, datée du 2026-07-31. 11c5055a… apparaît dans `code/x2/x2_b0.py`, daté du 2026-08-05 au MANIFEST. L'expurgation date du 2026-08-23. Les corps du dérivé retrouvent ces sceaux : ils sont donc ceux qui ont été hachés avant l'expurgation.
- Aucun motif de clé ne reste dans le dérivé. Je n'ai fait que compter, sans jamais lire de valeur.
- `chaine_gensha_v2.tsv` ne parle pas de l'expurgation. Il porte la chaîne « résultats → générations ». Je l'ai vérifiée : `meta.gen_sha` de c2a_results et de c2b_results égale l'empreinte de leur fichier de générations.
- Le MANIFEST (183830b9…) est celui du bordereau d'horodatage du 2026-08-24. Je n'ai pas vérifié la preuve OpenTimestamps, faute de réseau.
- Limite : l'original (d85cb96f…) n'est nulle part sur disque. Je ne peux donc pas comparer les trois lignes elles-mêmes. Pour les corps, les sceaux suffisent.

## (d) Textes et prompts, recalculés

J'ai extrait les textes de b2_neu avec mon propre motif. J'ai construit les prompts de deux façons : en exécutant les corps certifiés du cahier, et avec un enrobage que j'ai écrit à la main. Les deux concordent.

Résultats, tous 30 sur 30 :
- Le texte extrait de b2_neu égale `n200["texts"][i]`.
- Texte, empreinte du texte, indice et indices égaux : identiques aux valeurs de l'extracteur.
- Prompts neutre, critique et éloge : chaînes et empreintes identiques à celles de l'extracteur. Ses chaînes hachées redonnent les empreintes qu'il déclare.
- 30 empreintes distinctes pour chaque type. Aucun texte n'a de blanc au bord ni de guillemet droit intérieur.
- Doublon confirmé : l'item 27 est aussi à l'indice 59 de n200.
- Les graines suivent 9000+100i+k (c2a) et 9500+100i+k (c2b), sur 600 lignes chacune.
- Les métas de c2a et de c2b ne portent **aucune** empreinte de prompt.

## (e) Empreintes de prompt déjà stockées : ce que chacune couvre

| Empreinte stockée | Où | Ce qu'elle couvre | Confrontation |
|---|---|---|---|
| `tour0.sha256_invite` (600) | p1-auto/actes/ccA/RELEVE_ccA_blocC_2026-08-24.json (a6f12432…) | Le prompt **neutre**, envoyé au modèle par le bloc C (24 août), avec les graines de c2a et de c2b | **600/600** égales à mes prompts neutres, et chaque fois au bon item (30 valeurs distinctes) |
| `tour1.sha256_invite` (600) | même fichier | Une conversation à deux tours. Le dernier message est le noyau d'instruction, deux sauts de ligne, puis la phrase **exacte** de c2a ou de c2b, lue dans leurs métas | **600/600** reconstruits |
| `sha256_prompt` (1200) | RELEVE_ccA_blocB_2026-08-23.json (ea32bcf2…) | La règle de build_eval_prompt, avec des phrases **variantes** (« this text », « your writing ») | **1200/1200** avec format_neutral(noyau + deux sauts + phrase) |
| `sha256_prompt` (40 + 20), `sha256_invite` (1) | trace_blocB_avorte/*, CONTROLE_ccA_ordre_2026-08-23.json | Des prompts envoyés **sans** noyau d'instruction : un défaut du projet précédent | 0/60 avec le noyau, 60/60 et 1/1 avec « texte nu + phrase ». Témoin négatif : l'empreinte discrimine |
| `sha256_entree_tour1`, `sha256_prompt` (150 + 150) | RELEVE_ccA_PROG6_critique.json (16109827…), _elogieux.json (0f04766d…) | Le tour 2 de PROG-6 : format_neutral(réponse de c2a ou de c2b + deux sauts + phrase), **sans** noyau | 300/300 entrées et 300/300 prompts. Ce qui est attesté : l'enrobage format_neutral et les deux phrases exactes |
| préfixe `a73200add04e5532…` (489 octets) | ARRET_ccA_blocB_instruction_absente_2026-08-22.md (02c4d2f1…) | Le prompt **critique** de l'item 0, appelé « référence certifiée » : une reconstruction de la même lignée | Égal à mon prompt critique de l'item 0, longueur comprise. C'est **la seule** empreinte stockée d'un prompt critique de c2a |
| `prompts` (texte en clair) | c2f_prompts_effectifs_2026-08-10.json (51e5ba1b…) | Les prompts I2 critique et éloge, pour 12 items. C'est un texte écrit avant génération | 12/12 et 12/12. Les générations C2F ont d'autres graines (0/120 en commun), donc aucun test par les sorties n'est possible |
| `meta.prompt_sha` 6c95c1c0… | c2a_results, c2b_results (et d'autres fichiers « polarity ») | Le prompt du **juge** (diag/prompt_polarity.txt, même empreinte), pas un prompt de génération | Aucune de mes 90 empreintes |
| `instruction_sha256` 7375d631…, `suffixe_sha256` 28fe439f… et 00aa0bd9… | métas des blocs B et C, de PROG-6 | La phrase d'instruction, et les phrases de c2a (press) et de c2b (praise) | Égales |
| `gabarit_sha256` 5c361d7f… | métas des blocs B et C, de PROG-6 | Le fichier code/x/nuit_generation_neutre.py : une **recopie** de format_neutral, pas le corps certifié | Mêmes chaînes rendues que le corps certifié. Son empreinte de corps propre est 6c7287097e84f029, différente du sceau |
| préfixe 726fbb9c48f952a13d78 | items_sha_depuis_la_source.py | La valeur « texts » de n200 en JSON compact | Reproduit |
| `sha_invites` ff82d099… | inputs/D14_rapatriement/d14_generations.json | Les items 145 à 169 | Hors champ |

Ma recherche des 120 empreintes (30 textes et 90 prompts) dans toutes les sources ne trouve rien d'autre. Seules apparaissent les 600 + 1 empreintes neutres du bloc C et le préfixe de l'item 0 dans la note d'arrêt.
Aucune table d'empreintes de **textes** n'a survécu : ITEMS_SHA et la pièce 4b58df74 sont absentes.

## Témoin par les sorties (hors empreintes, décisif pour le neutre)

Le bloc C a envoyé au même modèle le prompt neutre reconstruit, avec les graines lues sur les lignes de c2a et de c2b. Ses sorties sont identiques au caractère près :
- avec les réponses neutres de c2a dans **240/300** cellules (296/300 sur les 50 premiers caractères) ;
- avec celles de c2b dans **247/300** cellules (293/300 sur les 50 premiers caractères).

Les divergences arrivent tard : médiane à 421 et 343 caractères. C'est la signature d'un bruit numérique (cartes A100 de 40 et de 80 gigaoctets), pas celle d'un autre prompt.
Ce résultat atteste par le comportement trois choses pour le neutre de c2a et de c2b : la suite de jetons d'entrée, l'ordre des items i → n200[i], et la voie de découpage en jetons (double jeton de début compris). C'est compatible, sans être une preuve formelle.

Témoin auxiliaire : « good » ou « bad » apparaît dans les 400 premiers caractères de 209/300 réponses neutres de c2a et de 213/300 de c2b. Il apparaît dans 0/40 réponses du bloc B lancé sans instruction. C'est cohérent avec la présence de « Is it good or bad? » dans les prompts.

## Écarts avec le rapport de l'extracteur

1. **Sous-estimation, côté neutre.** L'extracteur écrit que « la chaîne réellement envoyée au modèle n'est pas observée ». C'est faux pour le neutre : le bloc C l'a envoyée et hachée (600/600), et il reproduit les sorties de c2a et de c2b. Pour le critique et l'éloge, sa réserve tient.
2. **Recoupement plus fort, côté éloge.** L'extracteur recoupe l'éloge avec c2f, qui est un texte écrit. Le tour 1 du bloc C, qui est une génération observée, recoupe aussi la règle « noyau + deux sauts + phrase exacte de c2b » (600/600). Ce recoupement porte sur une conversation à deux tours, pas sur le prompt d'un seul tour de c2b.
3. **Réserve omise.** Le préenregistrement de c2b (empreinte 14e27578…, déclarée par c2b meta.prereg_sha) n'est nulle part sur disque. La composition de c2b n'est donc pas attestée par son préenregistrement. Celle de c2a l'est en partie : pred_c2a.md écrit « format_neutral, CORE, PRESS ».
4. **Précision.** Le relevé `RELEVE_ccG_deux_jointures_2026-08-22.json` (b7c38c28…) libelle sa composition « gabarit + réponse + phrase ». La composition qui concorde à 150/150 est **sans** gabarit. Avec gabarit, on obtient 0/150 (vérifié). Son libellé est inexact, son chiffre est juste.
5. Le reste concorde. Sorties antérieures absentes : aucun des préfixes b4eb5b81, edc00910, 10471f30, 4b58df74, d7af3962, f1e249d7, e3542ad8, 56638ec7, a3f52dd5, 2c6e7ca1 (c2full.py), d85cb96f (original du cahier) n'existe parmi les 14 232 fichiers hachés. Les trois relevés de p1-auto (4d184fe2…, f0192e4d…, 0a6d22f7…) existent bien, mais ne citent que des chemins de Downloads.

## Réserves qui restent

- Les prompts critique (c2a) et éloge (c2b) sont des reconstructions. Aucune méta de c2a ni de c2b ne les empreinte. build_eval_prompt n'est pas déclaré par c2a ni par c2b : son sceau vient de x2_b0.py (5 août), calculé sur le cahier. La branche éloge n'existe dans aucun corps certifié.
- Le dérivé expurgé ne peut pas attester l'original. Les corps sont couverts par les sceaux antérieurs, pas les autres cellules.
- La suite de jetons des prompts critique et éloge n'est pas vérifiée (pas de découpeur en jetons sans réseau).
- Les pièces d'archive n'ont pas de compagnon d'origine : le MANIFEST atteste leur état au 23 août 2026.
- Recommandation pour le papier C : garder comme garde, en tête de pilote, l'égalité des empreintes de prompts neutres avec `tour0.sha256_invite` du bloc C. Pour la pression, garder la règle et la déclarer reconstruite. Le projet précédent a lui-même deux fois envoyé des prompts sans noyau (bloc B avorté, et PROG-6 par construction).

## Règles

Aucune écriture hors de ce dossier, chaque fichier y a son compagnon `.sha256`. Aucune commande git qui écrit. Aucun réseau. Aucune clé ni aucun jeton affiché. Aucun processus arrêté.
