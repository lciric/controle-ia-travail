# P3-bis, écart 1 — lanceur dont la seule garde du crédit change (R-2399) : rapport du développeur, v1

Écrit le 2026-11-11 vers 23:31 UTC (heure relevée par `date -u`) par un développeur neuf (Claude Opus 5.5), qui n'a écrit ni P3-bis, ni sa chaîne, ni les bancs ; aucune lecture de T0.7 ; aucun appel à l'outil de location réel, aucune dépense. Consigne : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-ecart1-lanceur-credit-p3bis-v1.md` (`f8dfb4759523e9e88108c2ed353099fdf606ca1592de1e794edcfa464c6c21af`, vérifiée).

**Verdict** : lanceur d'écart écrit, seules les trois zones permises changent ; aval inchangé et compatible ; essais R5 conformes (13 cas, 0 non conforme).

## Branche et commit
- Branche `prep/p3bis-ecart1-credit-v1`, partie de S `8f8df8b2726a69568b4d4a54bae16188e7f1b3d0` (`origin/scellement/p3bis-v2`, récupérée par une refspec explicite) ; arbre de travail à moi, en extraction partielle (`docs/notes/bras-attaque/`, `diag/`, `runs/`, `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*` jamais extraits).
- Commit : celui qui ajoute ce rapport (un seul commit au-dessus de S ; son identifiant est dans le rapport à la mère).

## Lanceur d'écart
`docs/procedures/P3-bis-temoin-positif-v1/lancer_p3bis_v2_ecart1_v1.sh`, sha256 `dc33635ff01c90326044ae17471e2bbaeccf424975dcb34b21e0ae83921ad1ea` (compagnon `.sha256`). Copie de `lancer_p3bis_v2.sh` à S (`029bdb5c114a6166a21fa93724d71a2bf6158dc9686993424f6fbe8462352b08`, laissé tel quel dans le dossier).

### Lignes changées (`diff lancer_p3bis_v2.sh lancer_p3bis_v2_ecart1_v1.sh` : 10 lignes retirées, 45 ajoutées)
| Bloc du diff | Zone de la consigne | Ce qui change |
|---|---|---|
| `1a2,15` | (c) en-tête | note d'écart (R-2399, addendum 1, mot de Lazar, empreintes de S et du lanceur d'origine, liste des trois changements) ; aucune ligne d'origine retirée |
| `39c53` | (c) usage | « Usage : lancer_p3bis_v2_ecart1_v1.sh … (joué depuis le dossier où lancer_p3bis_v2.sh est resté) » |
| `45c59` | (c) usage | message d'usage sous le nom neuf |
| `94,95c108,109` | (a) contrôle de soi | commentaire du bloc 2 ; `"lancer_p3bis_v2.sh=$0"` devient `"lancer_p3bis_v2.sh=$H/lancer_p3bis_v2.sh"` : le lanceur d'origine resté dans le dossier est comparé à sa copie versée à S, comme les 14 autres scripts de `CHAINE` |
| `189,192c203,210`, `194a213,229`, `196,197c231,232` | (b) garde du crédit, bloc 9 | voir ci-dessous |

Bloc 9 sous l'écart : la réponse de `show user --raw` est gardée en mémoire (variable, jamais écrite ni affichée, effacée par `unset`) ; elle est passée au module commun (`verifications_p3bis_v2.py credit "$SOMME"`), dont la ligne officielle est **toujours** écrite au journal et dans `lancement.txt` ; un outil en échec avec un module à 0 prend le code de l'outil (comme le tube d'origine sous `pipefail`). Codes du module : 0 ou 3 → suite ; tout autre → « crédit illisible (show user, code N) : pas de création », code 2. Puis la ligne fixe `écart 1 (R-2399) : garde du crédit remplacée par la recharge automatique du compte (mot de Lazar) ; crédit présent > 0 exigé` est écrite (journal et `lancement.txt`) ; un programme `python3 -I` relit `credit` dans la même réponse (nombre fini, non booléen ; aucune valeur insérée dans du code) : > 0 → suite ; ≤ 0 → « crédit nul ou négatif : pas de création », code 3 ; illisible → code 2. Rien d'autre ne change (offres, instances, GO, dates, garde de calcul, création, étiquette `lanceur p3bis v2` de `lancement.txt` : l'empreinte qu'elle porte est celle du lanceur exécuté, donc du lanceur d'écart).

Choix déclarés : (1) la ligne d'écart est écrite dès que la réponse est lisible (codes 0 et 3 du module), avant la relecture, pour que la garde appliquée soit tracée aussi sur un refus à crédit nul ; (2) le crédit relu est celui de la même réponse que la ligne officielle (une seule interrogation de l'outil, comme l'origine) ; (3) la branche « illisible à la relecture alors que le module l'a lue » est défensive et inatteignable avec le module actuel (même critère de nombre) : non éprouvée.

## Aval (aucun autre script changé)
Relu dans `controle_cinq_minutes_p3bis_v2.sh`, `surveiller_p3bis_v2.sh`, `recuperation_p3bis_v2.sh`, `detruire_p3bis_v2.sh` et le module commun : **aucun ne relit l'empreinte du lanceur ni l'étiquette « lanceur p3bis v2 »** de `lancement.txt`. Ce qu'ils relisent :
- contrôle à cinq minutes : lignes uniques `commit`, `branche`, `creation`, `etiquette` (fonction `une`, motif `^clé valeur$`), `offre choisie : …`, `instance <id>` (module, `identifiant`), `prereg-S.md`, `offre.json` ;
- surveillance : `creation`, `offre choisie`, `instance <id>` ;
- destruction : `instance <id>`, `branche calcul/p3bis-reel-vN` ;
- récupération : ne lit pas les traces du lanceur (arguments S et BRANCHE).
La ligne d'écart (`écart 1 (R-2399) : …`) ne répond à aucun de ces motifs ; la ligne officielle du crédit est inchangée. Les contrôles avant dépense jouent sur un clone de S (constantes de la chaîne versée, où le lanceur d'écart n'est pas) : non touchés. Il n'y a rien à changer en aval.

Condition d'emploi : le lanceur d'écart se joue depuis le dossier de la chaîne (`$H`), où `lancer_p3bis_v2.sh` doit rester égal à sa copie de S. Il ne vérifie pas sa propre empreinte (rien de tel n'était demandé) : la session la compare à `dc33635f…` avant de le lancer.

## Essais R5
Script : `docs/notes/g0-deux-semaines-v1/p3bis-ecart1-v1/essais_ecart1_lanceur_p3bis_v1.sh` (`acf6f7c800894d8b67a922490e7fdf8707290ecbaf7d208933f4e4aa0a23eb47`) ; journal : `essais-ecart1-lanceur-p3bis-v1.log` (joué de 23:27:41 à 23:30:52 UTC, relevées par `date -u`), dernière ligne « ESSAIS DU LANCEUR D'ÉCART 1 DE P3-BIS : CONFORMES » ; sorties choisies dans `sorties-essais-v1/` (consoles des 13 cas, `lancement.txt` de E1, E9 et E13, rapport du contrôle à cinq minutes de E9). Bac à sable déclaré : faux outil de location (repris de la répétition jouet, sans construction de branche), dépôt synthétique et dépôt nu local, contrôles avant dépense en bouchon, journaux de preuve factices à la forme du module, texte factice, registre des GO temporaire (en-tête et ligne GO-2026-11-10-02 recopiés de `main` ; ligne **factice** GO-2026-11-11-90 pour l'instance nommée en marche 12345678 à 1,10 USD/h, donc minimum officiel 31 USD). Copies jouées des deux lanceurs : 3 lignes changées chacune (DEPOT, DEPOT_URL, INTERVALLE_OFFRE_S), écart entre copies égal à l'écart entre lanceurs.

| Cas | Attendu | Obtenu |
|---|---|---|
| E1 crédit 0 | code 3, « crédit nul ou négatif » ; ligne officielle puis ligne d'écart ; aucune création | conforme |
| E2 crédit −2,5 | code 3 | conforme |
| E3 crédit illisible (« six ») | code 2 ; aucune ligne d'écart | conforme |
| E4 réponse non JSON | code 2 | conforme |
| E5 outil en échec, sans réponse | code 2 | conforme |
| E6 lanceur d'origine absent du dossier | code 2, « lancer_p3bis_v2.sh exécuté ≠ copie versée au commit S » | conforme |
| E7 lanceur d'origine modifié | code 2, même refus | conforme |
| E8 témoin : lanceur d'ORIGINE, crédit 6 USD | code 3, « crédit insuffisant » | conforme |
| E9 cas sain : lanceur d'écart, crédit 6 USD | code 0, création factice 77777771 ; ligne officielle (6,00 contre 31,00), ligne d'écart, empreinte du lanceur d'écart joué | conforme |
| E10 contrôle à cinq minutes (création + 181 s) | « CONTRÔLE À CINQ MINUTES : CONFORME » | conforme |
| E11 surveillance (INTERVALLE=1) | FIN, arrêt par l'identifiant | conforme |
| E12 destruction (rapport de récupération FACTICE, déclaré) | détruite par l'identifiant | conforme |
| E13 crédit 50 USD (module à 0) | code 0, création 77777772 ; ligne d'écart écrite aussi | conforme |

Aucune création demandée au faux outil de E1 à E8 ; deux en tout (E9, E13) ; aucun jeton factice dans les consoles. Audit de symétrie (R4) : traces de E1, E6 et E9 relues à la main ; E6 et E7 refusent avant tout appel à l'outil ; E1 à E5 et E8 refusent après la relecture des instances, au bloc 9.

## Points ouverts
1. Le lanceur d'écart n'est à aucun commit scellé : sa seule ancre est le compagnon et ce commit ; la session compare son empreinte avant de le jouer.
2. La recharge automatique « constatée par Lazar » n'est pas vérifiable par le lanceur ; elle reste un fait déclaré (mot de Lazar).
3. L'addendum 1 au texte scellé est cité, pas écrit ici (hors mandat).
