# P3-bis, écart 1 — lanceur d'écart v2 (corrections C1 et C2 de la contre-lecture) : rapport du développeur, v2

Écrit le 2026-11-11 vers 23:54 UTC (heure relevée par `date -u`) par le développeur du v1 (Claude Opus 5.5), sur le message de la mère qui suit la contre-lecture `brouillons/P3-bis-temoin-positif-v1/P3-bis-ecart1-contre-lecture-v1.md` (`9b1013dbfe479a7b1cbcbe36fe88598b68037c24657f8d2f577789a908a9f33e`, vérifiée, lue en entier ; Claude Fable 5.2, « scellable après corrections »). Aucune lecture de T0.7, aucun appel à l'outil de location réel, aucune dépense. Le rapport v1 (`rapport-ecart1-lanceur-v1.md`) reste tel quel (R12).

**Verdict** : lanceur v2 écrit ; il ne diffère du v1 que par C1, C2 et l'en-tête (avec l'usage sous le nom neuf) ; essais v2 conformes (15 cas, 0 non conforme) ; témoin négatif : les mêmes essais joués sur le v1 reproduisent C1.

## Branche et commit
Branche `prep/p3bis-ecart1-credit-v1`, commit au-dessus de `e13df72b94510fba947a2262fa2274624bef7da4` (celui qui ajoute ce rapport ; son identifiant est dans le rapport à la mère). Ajouts seulement ; le v1 et ses essais ne sont pas touchés.

## Lanceur v2
`docs/procedures/P3-bis-temoin-positif-v1/lancer_p3bis_v2_ecart1_v2.sh`, sha256 `2e294e5a64086806591cdd0724561d7a8d7fdaab464705c22f9b92687d6607fb` (compagnon `.sha256`). Le v1 (`dc33635f…`) reste tel quel ; il n'est jamais joué pour une création.

`diff lancer_p3bis_v2_ecart1_v1.sh lancer_p3bis_v2_ecart1_v2.sh` (5 lignes retirées, 8 ajoutées) :

| Bloc | Objet | Changement |
|---|---|---|
| `2,3c2,6` | en-tête | « lanceur d'écart v2 », heure d'écriture, v1 gardé et jamais joué pour une création, C1 et C2 cités avec la contre-lecture |
| `53c56`, `59c62` | usage | nom neuf `lancer_p3bis_v2_ecart1_v2.sh` (comme la contre-lecture le demande, l. 2, 53 et 59 du v1) |
| `210c213` | **C1** | la ligne `if [ "$c" = 0 ] && [ "$cu" != 0 ]; then c=$cu; fi …` est remplacée exactement par le couple de la contre-lecture : outil de location en échec, la ligne officielle est écrite puis « crédit illisible (show user, outil en échec, code N) : pas de création », code 2, même si la réponse se lit |
| `227c230` | **C2** | `sys.exit(0 if v > 0 else 3)'` devient `sys.exit(0 if round(v, 2) > 0 else 3)'` (crédit relu au centime, comme le module commun) |

Contre le lanceur d'origine à S, toutes les autres lignes sont celles du v1 : contrôle de soi sur `$H/lancer_p3bis_v2.sh`, ligne officielle toujours écrite, ligne d'écart fixe, et le reste octet pour octet à l'identique de S. L'aval est inchangé : le constat du rapport v1 et de la contre-lecture vaut aussi pour le v2, puisque les traces écrites dans `lancement.txt` sont les mêmes.

## Essais v2
Script `docs/notes/g0-deux-semaines-v1/p3bis-ecart1-v1/essais_ecart1_lanceur_p3bis_v2.sh` (`e9a8dc69f39aa41e69209136db97aa9c2a1ab00400ca947c804934eabdaf0762`) : c'est le script v1 qui joue le v2. La dernière ligne attendue de E5 change, et deux cas s'ajoutent, E14 et E15, joués avant la création saine. Journal `essais-ecart1-lanceur-p3bis-v2.log` (`5ee8246ebfee9b6a71676ad06d5a330db4bdc24a1af81a9e7eb08fa651e98952`), joué de 23:50:35 à 23:53:47 UTC (relevées par `date -u`) ; sa dernière ligne est « ESSAIS DU LANCEUR D'ÉCART 1 DE P3-BIS : CONFORMES ». Les sorties sont dans `sorties-essais-v2/` : consoles des 15 cas, `lancement.txt` de E1, E5, E9, E13, E14 et E15, contrôle à cinq minutes de E9. Le bac à sable est le même que pour le v1 (faux outil de location, dépôt synthétique, ligne de GO factice GO-2026-11-11-90, minimum officiel 31 USD).

| Cas | Attendu | Obtenu |
|---|---|---|
| E1 crédit 0 | code 3, ligne officielle puis ligne d'écart, aucune création | conforme |
| E2 crédit −2,5 | code 3 | conforme |
| E3 « six » | code 2, aucune ligne d'écart | conforme |
| E4 réponse non JSON | code 2 | conforme |
| E5 outil en échec sans réponse | code 2 ; **dernière ligne changée** : « crédit illisible (show user, outil en échec, code 1) : pas de création » (v1 : « crédit illisible (show user, code 2) : pas de création ») | conforme |
| **E14 (C1)** `{"credit": 6.0}`, outil code 1 | code 2, ligne officielle écrite (6,00 contre 31,00), aucune ligne d'écart, aucune création | conforme |
| **E15 (C2)** crédit 0,004 | code 3 ; ligne officielle « crédit 0.00 USD » puis ligne d'écart ; aucune création | conforme |
| E6, E7 lanceur d'origine absent, puis modifié | code 2 au contrôle de soi | conformes |
| E8 témoin (origine, 6 USD) | code 3 « crédit insuffisant » | conforme |
| E9 cas sain (v2, 6 USD) | code 0, création factice 77777771, ligne d'écart, empreinte du v2 joué | conforme |
| E10, E11, E12 | contrôle à cinq minutes conforme, FIN et arrêt par l'identifiant, destruction (rapport de récupération factice, déclaré) | conformes |
| E13 crédit 50 USD | code 0, création 77777772 | conforme |

Aucune création de E1 à E8, ni en E14 et E15 ; deux créations en tout (E9 et E13) ; aucun jeton factice dans les consoles.

**Témoin négatif (R4, R5)** : `sorties-essais-v2/temoin-essais-v2-sur-lanceur-v1.sh` (`b6dbc70c…`) est le script v2 dont seule la ligne `LE=` désigne le v1 ; son journal est `temoin-essais-v2-sur-lanceur-v1.log`. Sur le v1, E5 n'est pas conforme (ancienne dernière ligne) et **E14 crée** (code 0, instance 77777771) : C1 est reproduit, l'essai le détecte. Les cas suivants échouent ensuite en cascade, parce que l'instance créée par E14 est sur le compte factice (« instances : non tolérée(s) »). E15 est donc masqué sur le v1 par cette cascade : C2 sur le v1 reste éprouvé par la contre-lecture (X7), pas ici. Verdict du témoin : 15 non conformes, code 1, comme attendu.

## Incident à signaler (sans effet sur les pièces)
Un premier lancement des essais v2, mal composé (le `cd` et la variable du dossier sont restés dans une tâche de fond), a écrit un fichier parasite de 68 octets à la racine du système : `/essais-ecart1-lanceur-p3bis-v2.log`, qui contient un seul message d'erreur de `bash`. Le contrôle de sécurité de l'outil a refusé sa suppression (« Dangerous rm operation detected ») ; je ne l'ai pas contournée. Il faut supprimer ce fichier à la main. Le journal versé est celui du second lancement, propre.

## Points ouverts
1. L'addendum doit reprendre le nom, l'empreinte et les essais du v2 (A1 à A3 de la contre-lecture) ; ce n'est pas mon mandat.
2. Les conditions d'emploi du rapport v1 tiennent : le lanceur v2 n'est à aucun commit scellé et ne vérifie pas sa propre empreinte ; la session la compare à `2e294e5a…` avant de le jouer, depuis le dossier où `lancer_p3bis_v2.sh` est égal à S.
