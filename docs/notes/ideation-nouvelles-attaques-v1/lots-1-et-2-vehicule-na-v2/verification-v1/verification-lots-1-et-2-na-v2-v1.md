# Vérification des lots 1 et 2 du véhicule NA-1, livrable v2 — v1

Vérificateur des lots 1 et 2 du véhicule NA-1, modèle S. Pièce de travail (classe C). Processeur seul : aucun appel, aucune clé, aucune dépense, aucune écriture dans un dépôt. Données factices seules (le tirage réel n'est pas joué).

## Verdict

**Conforme. Le lot 3 peut partir.** Les neuf survivantes de ma première vérification sont tuées ; les comptes rejoués sont égaux à ceux du développeur ; rien n'est tranché à tort ; l'interface est complète. Cinq points restent à porter à l'additif du véhicule, aucun ne bloque.

Un incident : pendant la première passe, j'ai tenté une commande de liste sur un dossier hors du périmètre du mandat ; le classifieur l'a refusée ; je me suis arrêté et l'ai dit ; la mère a consigné ce refus sans effet et m'a fait reprendre. Je n'ai rien contourné.

## 1. Empreintes

| pièce | sha256 | état |
|---|---|---|
| mandat du vérificateur | `e2843d22…` | égal à son compagnon |
| table d'empreintes du livrable v2 | `4ba408af7d9e362c885c7b741db47860c16b6ee9a60216a778d752dbc00dedac` | égale à l'annonce ; les 13 fichiers vérifiés OK par `sha256sum -c` |
| rapport v2 | `21676fada803abc65f76814dcce5de9d9f9b2b870884203c6ff5370f7c378943` | égal à l'annonce, compagnon OK |
| contrôle de la v5 | `4b369004…` | égal à son compagnon (OK) |
| orchestrateur | commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb` | égal |
| V9 et additif 1 (tirés de `origin/main`, redirigés vers mon dossier) | V9 `864f39a7…` | égale à celle citée par le développeur |

## 2. Essais et mutations rejoués

Copie neuve de `orchestrator/` (sans `.git`), paquet v2 appliqué par son programme (copie de 8 fichiers, empreintes relues), essais joués sous le `conftest.py` de l'orchestrateur.

| | annoncé | rejoué |
|---|---|---|
| essais | 92 passés (lot 1 : 61 ; lot 2 : 31) | **92 passés**, 0 échec |
| mutations | 77 tuées sur 77 (42 du développeur, 35 du vérificateur) | **77 tuées sur 77** (42 + 35) ; témoin non muté : passe ; témoin inerte : survit |
| non tuées | aucune | aucune |

Mes 35 mutations (X-01 à X-35) sont rejouées avec leurs lettres d'origine, sauf X-30 et X-32 (voir § 3). X-35 est jouée à la lettre. Deux mutations (X-12 et X-13) et la mutation L2-01 sont tuées par erreur de préparation de classe et non par un échec d'essai : preuve plus faible, mais la garde retirée rend bien le code inutilisable. Je ne l'exige pas.

Les neuf survivantes de ma première passe (X-03, X-05, X-07, X-08, X-11, X-20, X-30, X-32, X-33) : les sept portées par un essai neuf (X-03, X-05, X-07, X-08, X-11, X-20, X-33) sont tuées à leur lettre ; X-30 et X-32 sont traitées au § 3.

## 3. Les adaptations X-30b et X-32b sont-elles justes ?

Oui, toutes deux.

- **X-30 sans objet.** Le diff v1 → v2 de `garde_motifs` montre que la ligne `verifier_avant_envoi(rg, rg.octets)` est retirée de `envoyer_apres_garde` : elle comparait la copie à elle-même et ne pouvait jamais échouer. C'est exactement ce que X-30 retirait. Sa disparition est la bonne réponse.
- **X-30b** retire le seul test d'égalité qui reste, `if hashlib.sha256(bytes(octets_a_envoyer)).hexdigest() != requete_gardee.sha256:` dans `verifier_avant_envoi`. Elle est tuée par 2 essais. Elle éprouve la garde là où elle a un objet. L'essai `test_x30_l_egalite_a_un_objet_au_lot_4` refuse un octet de plus, un de moins, une casse changée et une chaîne non binaire.
- **X-32b** vise la nouvelle ligne `empreinte = hashlib.sha256(octets).hexdigest()` et la remplace par une seconde lecture du tampon de l'appelant (`bytes(requete)`). C'est la même idée que X-32. Elle est tuée. L'essai `test_x32_…` ne dépend pas du temps : il passe un tampon (`TamponQuiChange`, sous-classe de `bytearray` avec `__bytes__`) dont la seconde lecture rend d'autres octets. Il prouve donc « une seule lecture, l'empreinte est celle de la copie ». L'équivalence quasi parfaite que je signalais en v1 est levée.

Diff v1 → v2 : seuls `garde_motifs_na_v2.py` (X-30, X-32 et l'en-tête) et les noms de version/import de `tirage_na_v2.py` changent. Aucune règle de tirage ne change. `identifiants_na_v1.py` et la liste d'essai sont repris à l'octet. Mes sondes de la v1 (gabarit réel, 216 000 mots, encodage aux bornes) restent donc valables ; je ne les ai pas rejouées sur les noms v2.

## 4. Exigences du mandat, une à une (état v2)

| exigence | faite | où | essai qui échoue sans la garde |
|---|---|---|---|
| tirage rejoué égal à l'octet (clés 0, 1, 2, 3) | oui | `tirage_na_v2.py` : `_rng` (une fois par clé), `serialiser` (clés triées, aucune heure) | `test_rejoue_deux_fois…`, `…_deux_processus…` (graines de hachage différentes) ; X-19 tuée ; vérifié aussi sur le gabarit servi réel, racine factice |
| clés n° 30 et n° 40 au même geste, consignées | oui | `TirageNA.jouer` : clés 0, 1, 2, 3, 30, 40 dans l'ordre ; sortie `cles` | `test_cles_30_et_40_au_meme_geste_et_consignees` ; X-15, X-16 tuées |
| clé n° 30 : aucune case de sabotage, rien n'est tiré ; second tirage refusé | oui | `tirer_cle_30` | L1-09, L1-10, L1-11 tuées ; **X-03 tuée (nouveau)** |
| clé n° 40 : mot refusé par la garde, tirage arrêté sans second tirage | oui | `tirer_identifiants` | L1-12, L1-13 tuées ; X-14 tuée |
| encodage dans les deux sens, alphabet, base 60 à longueur fixe (18 et 14), refus hors alphabet, aucune suite de huit chiffres hexadécimaux | oui | `identifiants_na_v1.py` | L1-21 à L1-25, X-21 à X-24 tuées ; 216 000 mots de case sans anomalie (vérifié par moi) |
| arrêt n° 10 (premier temps) | oui, dont génération hors de 1 à 3 | `garde_disjonction` | L1-06 à L1-08, X-09, X-10, **X-11 (nouveau)** tuées |
| ligne de case et son contrôle (valeurs à l'octet, identifiants distincts, hexadécimal, chiffre, borne 256, fin de ligne, préfixe) | oui | `controler_ligne_de_case`, `sortie` | L1-14 à L1-19, **X-05, X-07, X-08 (nouveau)** tuées |
| arrêt n° 16 par famille, cas sain et artefact | oui | `GardeMotifs.examiner`, `garder_requete` | `TestArret16ParFamille` ; L2-07, L2-08 ; **X-33 (nouveau : ordre famille puis rang)** |
| aucun octet changé après la garde ; empreinte journalisée = celle de ce qu'elle a lu | oui | `garder_requete` : une copie, une empreinte, objet figé | L2-10b, X-31, X-32b tuées |
| ligne « envoi » écrite avant l'envoi ; « non envoyé » | oui | `envoyer_apres_garde` | L2-15b, L2-16 tuées |
| refus d'écrasement (R12) de la sortie et du manifeste | oui | `main` | **X-20 tuée (nouveau)** |
| aucun identifiant de modèle, clé ou recette | oui | grep du livrable v1, fichiers repris à l'octet ; v2 : les fichiers neufs ne contiennent que des noms de version | — |

## 5. Les douze points « que la lettre ne fixe pas »

Aucun n'est tranché à tort, aucun ne contredit la conception v5. Le § 5 du rapport v2 les cite sans les trancher. À porter à l'additif du véhicule :

1. **Définition de « caractère invisible »** (point 6 du rapport v1) : la garde retire la catégorie Unicode « Cf » seule. U+FE0F, U+034F, U+3164 et U+2800 coupent un motif sans être retirés (sondes de ma première passe). À définir ; je recommande les caractères ignorables par défaut d'Unicode en plus de « Cf ». Risque pratique faible.
2. **Espace et tiret** : lus comme deux formes. « graine-factice » ne mord pas sur « graine factice ». Choix pour la mère : une seule forme, ou deux (une expression régulière de la liste peut toujours les unir).
3. **Texte trouvé** : écrit au journal de la ligne « non envoyé », dans le dossier de sortie, pris dans le texte normalisé. C'est la lettre du § 2.7 de la conception (« le texte trouvé dedans ») et de V9, l. 387. Le mandat vérificateur disait « sans recopier le texte trouvé » : la formule vise le message de l'arrêt et l'écran, qui ne le portent pas (vérifié : ni `str`, ni `repr`, ni `args`). À écrire noir sur blanc.
4. **Valeurs du concepteur à fixer** : écriture d'un rang en mot de trois syllabes ; ordre des onze cases d'une génération (celui du tirage) ; « cases servies » et rang de la menace « sabotage » pour la clé n° 30 ; forme de la ligne de case (`case : <id> ; <v1> ; <v2> ; <v3>`) ; format de la liste des motifs (`liste-motifs-na-v1`), que la rédaction de la liste réelle doit suivre.
5. **Lot 4** : appeler `garde_motifs_na_v2.verifier_avant_envoi(requete_gardee, octets)` sur les octets remis à `super().appel`. La consigne du noyau est une chaîne : l'encodage UTF-8 doit se faire une seule fois, et c'est cette suite d'octets que la garde lit, que le journal décrit et que l'égalité compare. À écrire au mandat du lot 4.

Les autres remarques (1, 9, 10, 11, 12, 13 du rapport v1) tiennent. Le point 10 (clé 20, pour n ≤ 60 tous les rangs sans tirage) est cohérent avec V9, l. 309. Le point 1 (le réencodage est écrit au lot 1 alors que la conception le range au lot 5) est sans conséquence : module séparé, importé par le lot 5. Constat positif sur le point 11 : le gabarit servi réel, empreinte `4cd360ba…`, est lu correctement par `lire_legende` (6, 5 et 4 valeurs ; « autre, à nommer » au rang 5 ; sabotage au rang 0 de l'axe 1) ; la plus longue ligne possible fait 131 octets.

## 6. Interface des lots 3, 5 et 6 comparée au § 5.1 de la v5

| module (§ 5.1) | entrées / sorties de la ligne | offert par le livrable | écart |
|---|---|---|---|
| `tirage` | entrées : gabarit (empreinte), racine, clés ; sorties : fichier du tirage, table des identifiants ; lu par `requete`, `course`, `mesures`, lanceur, témoins | `TirageNA(gabarit, empreinte, racine)` → `jouer(garde)` → `serialiser` ; sortie : `generations`, `reserve` (dont `premiere`, la case des témoins), `cle_30`, `identifiants`, `legende`, `controles_C1` ; `lignes_du_tirage`, `ligne_de_case`, `controler_lignes_de_case`, `garde_disjonction`, `permutation_registre` (clés 12, 13), `part_anteriorite` (clé 20), `main` + manifeste | aucun |
| `garde_motifs` | entrées : octets, liste scellée ; sorties : « passe », ou famille et rang, texte trouvé vers le journal ; lu par la surcharge d'`appel`, le départ, les épreuves | `charger_liste_motifs(chemin, empreinte)` → `GardeMotifs` (témoins rejoués à la construction) ; `garder_requete(octets)` → `RequeteGardee` ou `ArretMotifInterdit(famille, rang, texte_trouve)` ; `examiner`, `garder_texte` ; `verifier_avant_envoi` ; `envoyer_apres_garde` ; `empreinte_programme` (pour l'arrêt n° 14) | aucun |
| `identifiants` (lot 5) | entrées : octets ; sorties : un mot de syllabes, et l'inverse | `encoder_octets`, `encoder_identifiant_fiche` (18 lettres), `encoder_identifiant_juge` (14), `decoder_octets` (refus nommé), `reencoder_jeton_noyau`, `mot_de_case`, `rang_du_mot_de_case`, `porte_suite_hexadecimale` | optionnel : l'inverse « mot vers jeton du noyau » (préfixe + octets en hexadécimal) n'existe pas ; le lot 5 le compose avec `decoder_octets` |
| lignes du § 2.2, § 6.2 (lot 3) | trente-trois lignes et celle de la réserve contrôlées | `controler_lignes_de_case` | aucun |
| arrêt n° 10 rejoué au départ de chaque génération (lot 6) | contre le tirage scellé | `garde_disjonction(tirage_json, generation, cases_a_servir)` | aucun |

Complète et cohérente. La seule consigne neuve est celle du point 5 du § 5.

## 7. Ce que le contrôle de la v5 change pour les lots 1 et 2

Rien. Son verdict est « Conforme, le lot 6 peut partir » ; la retouche qu'il demande (sixième ligne de la pièce de relevés) touche les lots 8 et 10 a. Son différentiel (§ 5 du contrôle) ne touche ni le § 2.1, ni le § 5.2, ni les lots 1 et 2 du § 7. Mon propre diff v4 → v5 le confirme : les hunks portent sur le § 0, le § 0 bis, le § 2.13, le § 2.14, le § 5.3, le § 6.2 (lignes A3 et A14, lot 6), le § 7 (lots 6 et 10 a), le § 8 et le § 9. La v4 sur laquelle le développeur a travaillé reste donc valable pour les lots 1 et 2.

## 8. Ce que je n'ai pas fait

Je n'ai pas rejoué mes sondes de la v1 (gabarit réel, 216 000 mots) sur les noms v2 : le diff v1 → v2 montre qu'aucune règle de tirage ni d'encodage n'a changé. Je n'ai pas joué le tirage réel.

— vérificateur des lots 1 et 2 du véhicule NA-1, modèle S
