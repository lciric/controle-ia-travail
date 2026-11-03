# Audit A9 — A1-v3, première course (GO-2026-11-02-21), état interrompu — v1

Auditeur neuf (n'a écrit ni le texte scellé, ni le code, ni le lanceur, ni le rapport de la fille). Écrit le 3 novembre 2026,
commencé à 08:19:28 UTC, rédigé à 08:22 UTC (heures relevées par `date -u`). Aucun réseau, aucun modèle, aucun fichier existant
modifié, aucun commit ; calculs par `nice -n 10 python3 -I -B`.

## 0. Pièces et contrôles d'intégrité

- État interrompu : `/tmp/a1-etat/brouillons/canal-reprise-releve-v1/envois/session-depot/a1-v3-etat-interrompu-v1/` (abrégé `E/`).
  `sha256sum -c LISTE-COPIE-v1.txt` : 38 fichiers sur 38 conformes. Chaque compagnon `.sha256` conforme à son fichier.
- `sha256sum -c EMPREINTES-etat-interrompu-a1-v3-v1.txt` (liste `04cf5d1b…`) : 17 entrées sur 18 conformes ; seule
  `journal-lancement-a1-v3-v1.log` diffère (écart déclaré, section 5).
- Texte scellé : `orchestrator/prereg/preenregistrement-attaque-goodhart-v3-v1.md`, sha256 recalculé
  `898d5be414f1472dc5beb9c9e8d377698c6b1744e9b95bd188de5a157426a23e` ; égal à celui du manifeste de départ.
- Code : arbre `/home/claude/wt/a1-v3-seconde/orchestrator/` (tête `eaa74ca` ; `9776ed0` et `ba4edfe` sont ses ancêtres ;
  `ba4edfe..eaa74ca` n'ajoute que deux fichiers de contre-lecture d'un autre texte). Les 73 empreintes `code_sha256` du manifeste de
  départ sont égales aux fichiers de `ba4edfe` et à ceux de l'arbre ; le manifeste porte `depot = {commit ba4edfe…, arbre_modifie: false}`.
- Faits de session-depot : `/tmp/sd-n305.md`, `/tmp/sd-n306.md`.

## 1. Chronologie (UTC, 3 novembre 2026)

Sources : journal de lancement (JL), journal du relais (JR, une ligne par appel, heure de fin), registre de dépense cumulée de la
sortie (RD, lignes `debut`/`fin` écrites par la commande d'Argon, enfant de la course), journal du guetteur (JG).

| Heure | Source | Fait |
|---|---|---|
| 06:15:58 | JL | `ideation-organism` tête `ba4edfe`, `git status --porcelain` vide |
| 06:16:22 | JL | 10 empreintes de la section 2 « égal » |
| 06:16:28 | JL | `registre-go.md` sha256 `53985197…` = attendu ; ligne GO-2026-11-02-21 présente (l. 67 ; recalculé : `E/registre-go.md` = `53985197…`) |
| 06:16:55–06:17:12 | JL, `relais-argon-stdout` | relais 8805 démarré, PID 1011 ; `/relais/etat` : 0 appel, plafond 410 USD, 9000 appels, clé présente (booléen) |
| 06:17:18–06:17:19 | JL, `verifier-seulement` | `--verifier-seulement` : code 0, « conforme », aucune écriture, aucun appel |
| 06:17:41 | JL | course lancée, PID 1251 (`/proc/1251/cmdline` à 06:17:43 : `python3 -I -B demonstrations/attaque_goodhart_v3.py …` : le PID est bien le processus Python, la chaîne `nohup setsid env nice` ayant fait `exec`) |
| 06:17:42.56 | RD | premier `debut` (appel 1) |
| 06:17:51 | JR, RD | appel 1 OK/STOP |
| 06:18:23 | JG | guetteur démarré (son propre PID 1405), course 1251 et relais 1011 vivants |
| 06:18:24 | JL | « guetteur démarré PID 1403 » (voir réserve R3) |
| 06:18:29 | JG, JR | `/relais/etat` : 6 appels, 0,35281 USD = cumul de l'appel 6 au JR (06:18:29) |
| 06:18:53 | JL | relève horaire planifiée (minute 18, liée à la session fille) |
| 06:20:35 | JL | dernière ligne de la fille avant le silence (note sur le code de sortie) ; session-depot : session inactive « vers 06:20 » |
| 06:17:51–06:22:53 | JR, RD | appels 1 à 40 : tous OK, fin STOP, code 0, coût à l'usage ; durées 4,0 à 13,0 s ; entre la fin d'un appel et le `debut` du suivant : 0,10 à 0,30 s |
| 06:22:53.22 | RD | fin de l'appel 40 (dernier succès) ; cumul 2,63156 USD |
| 06:22:53.41 | RD | `debut` de l'appel 41 |
| 06:23:29 | JG | dernier passage du guetteur : relais et course vivants |
| 06:25:32 | JR | appel 41 : ECHEC, 158,7 s, « connexion : RemoteDisconnected : Remote end closed connection without response », `cout_origine` pire_cas 1,614193 USD, cumul 4,245753 USD |
| 06:25:32.11 | RD | `fin` de l'appel 41 : code 3, statut « echec », pire cas ; **dernière écriture de tout l'état par un processus de la course** |
| ≈ 06:25:47 | code | instant où la course aurait écrit le `debut` de l'appel 42 (voir section 2) : **jamais écrit** |
| 06:28:29 | JG | passage attendu du guetteur : **jamais écrit** |
| 06:25:32 → 07:18:50 | toutes | silence complet : aucune ligne dans aucun journal |
| 07:18:50 | JL (07:19:36) | redémarrage du conteneur constaté (uptime 22 s à 07:19:07), à la relève horaire ; course, relais, guetteur absents |
| 07:19:36 | JL | relevés de la fille (dernier appel, dépense, cause probable) ; rien relancé, rien lu |
| 07:20:01 | JL | « alerte envoyée » (ligne de l'écart déclaré) |
| 07:22:40 → 07:33 | n° 305, 306 | mot de session-depot (sceller tel quel, ne rien relancer) ; état versé (commit `c293e914…`) |

Cohérence des quatre sources : les 41 appels du JR s'apparient un à un aux 41 couples `debut`/`fin` du RD (même coût, même pire
cas, même origine du coût ; écart d'horodatage ≤ 0,97 s) ; le relevé du guetteur à 06:18:29 égale le JR ; les heures de la fille
(06:17:41, 06:23:29, 06:25:32, 158,7 s, 4,25 USD) et celles de session-depot (n° 305) égalent les journaux. Aucune contradiction.

## 2. Nature de l'arrêt

- **Aucun code de sortie, aucune `nature_de_l_arret`.** Les trois fins prévues du lanceur écrivent toutes sur la sortie d'erreur,
  redirigée vers `course-stdout-a1-v3.log` : code 2 (`refus : …`, `demonstrations/attaque_goodhart_v3.py:562-566`), code 3
  (résumé JSON avec `nature_de_l_arret`, `:619-620`, et `attaque-goodhart-v3.json` scellé, `:618`), code 0 (résumé, `:640-648`, et
  le fichier de résultat). Une exception non rattrapée écrirait une trace. Or `course-stdout-a1-v3.log` fait **0 octet**
  (`e3b0c442…`) et `attaque-goodhart-v3.json` est **absent**. Aucune de ces fins n'a eu lieu.
- **Le manifeste est un manifeste de départ seul** : il est écrit à `:592`, avant `jouer_tout` ; ses clés (`version_pole`, `python`,
  `plateforme`, `code_sha256`, `regle_*`, `reglages` : attaque, mode « reel (decisif, course) », plan, devis, préenregistrement,
  configuration, dépôt, graines) ne contiennent aucune clé de fin (`fin_utc`, `arret`, `nature_de_l_arret`, `duree_s`,
  `depense_usd`, `lecture`, `issues`, `tentatives` : absentes ; les seules clés `rejeux`/`suites` trouvées sont des réglages du plan
  et de la description du cœur).
- **L'échec de l'appel 41 n'est pas la cause de l'arrêt.** Sous v3.1, un code 3 au pire cas est une cause « relais » : tentative non
  consommée, attente de 15 s (`ATTENTES_RELAIS_S[0]`), puis nouvel appel (`pole/attaque_goodhart_v3.py:417-431`) ; avec
  `relais_perdu_h: aucun`, `attendre_relais` ne lève jamais d'arrêt (`:256-270`). La course aurait donc écrit un `debut` d'appel 42
  vers 06:25:47 ; il n'existe pas. La course était morte (ou gelée) entre 06:25:32,11 et ≈ 06:25:47.
- **Les trois processus ont disparu ensemble, et le conteneur a redémarré.** Le guetteur, processus indépendant qui ne s'arrête que
  sur la disparition de la course en l'écrivant (`scripts/guetteur_a1_v3_v1.py`, branche « disparu »), n'a écrit ni son passage
  de 06:28:29 ni cette ligne de disparition ; le relais n'a plus rien écrit ; à 07:19 les trois PID étaient absents et le
  processus 1 avait 22 s d'âge. Une mort de la seule course (exception, mémoire) aurait laissé le guetteur l'écrire à 06:28:29.
- Aucun acteur n'a envoyé de signal : le guetteur ne contient aucun envoi de signal ; le journal de lancement n'a aucune ligne entre
  06:20:35 et 07:19:36 ; aucune trace d'arrêt décidé (R10) ni de mot de Lazar.

**Conclusion : arrêt du lanceur hors de ses codes 0, 2 et 3**, par disparition du processus avec le conteneur (signal ou gel
d'infrastructure, sans qu'on puisse dire lequel), au sens de la section 8 du texte scellé (l. 1114-1115).

## 3. Dépense

- 41 appels ; 4,245753 USD au relais (`depense_cumulee_usd` de la dernière ligne, et somme des `cout_usd` du JR) ; somme des `fin` du
  RD : 4,245753 USD ; égalité appel par appel (section 1).
- Appels 1 à 40 : 2,63156 USD à l'usage. Appel 41 : 1,614193 USD au **pire cas** (`cout_origine` pire_cas au JR, code 3 au RD,
  usage 0/0) : compté au pire cas comme le veut la règle ; son coût réel est inconnu (au plus ce montant).
- Aucun `depassement_reserve` ; plafond du relais 410 USD, plafond d'étape 400 USD : loin.
- **Aucun appel après la reprise** : dernière ligne du JR 06:25:32Z, dernière du RD 06:25:32.11Z ; à 07:19 relais absent, rien
  relancé (JL 07:19:36) ; le guetteur, seule voie de relance, était mort.

## 4. Lecture utile : aucune

- La sortie ne contient que `manifeste.json` (+ compagnon), `registre-depense-cumulee-v1.jsonl` (+ compagnon) et le verrou vide.
  **Aucun fichier de résultat** ; aucune réponse de modèle sur disque (0 fichier, 0 octet) : les textes ne vivent qu'en mémoire
  (`pole/attaque_goodhart_v3.py:381`, C10) et sont morts avec le processus.
- Aucun taux, aucune richesse, aucune carte, aucune tentative jugée n'est écrite. Les seules données par appel (JR et RD) sont des
  métadonnées d'infrastructure : statut, fin, durée, jetons d'entrée et de sortie, longueur en caractères, coût, modèle servi —
  aucune évaluation du juge n'y figure, donc aucune issue n'en est calculable. Je n'ai fait sur elles aucun calcul autre que les
  contrôles de dépense et de chronologie ci-dessus.
- Le manifeste ne contient que des réglages (section 2).

## 5. Écart déclaré (ligne ajoutée au journal de lancement)

- Ligne : `2026-11-03T07:20:01Z alerte envoyée à session-depot (course morte avec le conteneur ; options (a) sceller et verser l'état
  interrompu, (b) reprise sur ordre) ; relève horaire désactivée ; liste d'empreintes locale 04cf5d1b…` — dernière ligne du fichier.
- Vérifié : le journal privé de cette seule dernière ligne a pour sha256 `778fab67…ddd190e`, exactement l'entrée de la liste ; le
  journal entier a `16eab4af6bc14dc678b647d006bc2f729251582df2e90f0a8986725a2cd4ba8b`, égal à son compagnon et à
  `LISTE-COPIE-v1.txt`.
- Contenu : une note d'action de la fille, postérieure au constat, sans chiffre de résultat. **Ne change rien** à l'audit : aucune
  autre ligne n'a bougé, et la ligne est d'après coup.

## 6. Gardes

- **Lanceur et barrages de départ** : ont fait ce que le texte prévoyait (tête et arbre propres, empreintes, registre des GO par
  empreinte, relais relevé, `--verifier-seulement` en code 0, manifeste de départ scellé avec le texte `898d5be4…`).
- **Guetteur** : a fait ce que le texte prévoyait (section 13, l. 1047 : relancer, jamais arrêter) — deux passages, relevé exact,
  aucun signal. Il n'a pas pu signaler l'échec de l'appel 41 (`alertes-a1-v3-v1.log` absent : son passage suivant n'a jamais eu
  lieu). Par construction, il vit dans le même conteneur et meurt avec lui.
- **Relève horaire** : prévue par la fille, pas par le texte ; a fonctionné à son heure (07:18:51) et a constaté la perte. Le
  redémarrage du conteneur (07:18:50) coïncide à la seconde près avec son déclenchement : c'est vraisemblablement elle qui a
  réveillé le conteneur (constat d'horaire, non prouvé).
- **Harnais** : aucun processus n'était suivi par le harnais ; la course était détachée (`nohup setsid … &`).
- **Ce que le texte ne prévoyait pas** : la reprise du conteneur pour inactivité de la session. Le texte gère la panne du relais
  (attente, guetteur) mais pas la disparition de l'hôte ; ce n'est la faute de personne : le cas était inconnu avant cette nuit.

## 7. Conclusion

1. **Cause d'infrastructure établie : oui.** Preuve la plus forte : course, relais et guetteur ont disparu ensemble et le conteneur a
   redémarré (processus 1 âgé de 22 s à 07:19:07), sans aucune des sorties que les codes 0, 2 et 3 écrivent toujours
   (`course-stdout` vide, pas de `attaque-goodhart-v3.json`), et la course n'a jamais écrit l'appel 42 que le code aurait lancé
   15 s après l'échec de l'appel 41 : arrêt hors des codes 0, 2 et 3 (section 8, l. 1114-1115).
2. **Lecture utile : aucune** (pas de fichier de résultat, pas de réponse sur disque, ni taux, ni richesse, ni carte).
3. Dépense : 41 appels, 4,245753 USD, dont 1,614193 USD au pire cas pour l'appel 41 ; aucun appel après la reprise.

## 8. Ce que la seconde course doit prévoir (faits)

1. **Survie de l'hôte.** Fait : la session est devenue inactive vers 06:20 ; la course était morte entre 06:25:32 et ≈ 06:25:47,
   soit environ 5 min plus tard ; la relève était horaire. Un processus détaché ne garde pas le conteneur en vie. Durée attendue de
   la course : ≈ 25 h (session-depot, n° 305), durée maximale du texte 72 h. Il faut un mécanisme qui garde la session active sans
   interruption de plus de quelques minutes pendant toute la course, de période nettement inférieure à 5 min d'inactivité.
2. **Observation hors du conteneur.** Fait : le guetteur et le relais meurent avec le conteneur ; la perte a été vue 53 min après par
   la relève. Seul un observateur hors du conteneur (le harnais ou session-depot) peut voir une perte d'hôte.
3. **Trace d'une fin brutale.** Fait : le code n'écrit la trace (suites, journaux d'appels) qu'à la fin ou sur `ArretAttaque` ; une
   mort par signal perd tout : ici 40 appels réussis (2,63 USD) ne laissent rien d'auditable au-delà des métadonnées. Le code de
   sortie n'est capté par personne (lancement détaché, enveloppe absente). Si le texte neuf veut un arrêt brutal auditable, il doit
   le dire (changement d'instrument, donc hors de « même instrument ») ou accepter ce fait.
4. **Sortie neuve.** Fait : le lanceur refuse un dossier de sortie non vide (`demonstrations/attaque_goodhart_v3.py:504-505`,
   code 2) ; l'ancien dossier contient le manifeste de départ.
5. **Dépense comptée.** Fait : le registre de dépense cumulée et le relais comptent par chemin et par processus ; une sortie neuve et
   un relais neuf repartent de 0 USD. Les 4,245753 USD de la première course ne seront vus par aucune garde de la seconde : le texte
   neuf doit dire s'ils s'imputent sur le plafond de 400 USD du GO-2026-11-03-01.
6. **PID du guetteur.** Fait : `guetteur.pid` porte 1403, le guetteur lui-même écrit 1405 ; le fichier de PID n'est pas celui du
   processus. Pour un arrêt par identifiant (R10), le PID doit venir du processus lui-même.
7. **Hôte nommé.** Fait : la ligne GO-2026-11-02-21 dit « course chez session-depot » ; la course a tourné dans la session fille.
   Le texte neuf doit nommer l'hôte.

## 9. Réserves

- R1. L'âge du processus 1 (22 s à 07:19:07) et l'absence des PID à 07:19 ne sont attestés que par le journal de la fille ; je n'ai pas
  accès au conteneur. Ils sont corroborés par l'absence de la ligne de 06:28:29 du guetteur et de l'appel 42.
- R2. Signal ou gel, et instant exact de la mort du relais (seulement borné par 06:25:32 et 07:18:50) : indéterminés ; sans effet sur
  la conclusion (hors des codes 0, 2 et 3 dans tous les cas).
- R3. Écart de PID du guetteur (1403 au journal de lancement et au fichier, 1405 au journal du guetteur et au rapport de la fille) :
  sans effet ici, aucun arrêt par PID n'a eu lieu.
- R4. L'échec « RemoteDisconnected » de l'appel 41 (158,7 s, contre 13 s au plus pour les 40 autres) peut être un symptôme de la
  reprise du conteneur ou une panne distincte de l'interface : indéterminé ; dans les deux cas une cause d'infrastructure, et le code
  l'aurait attendue, non transformée en arrêt.
- R5. Le coût réel de l'appel 41 est inconnu (compté au pire cas, 1,614193 USD) ; seule la facturation du fournisseur le dirait.
- R6. Je n'ai pas vérifié le commit `c293e914…` de la branche `donnees/…` (interdit de toucher `donnees/` et `git fetch`) : l'audit
  porte sur la copie `E/`, conforme à `LISTE-COPIE-v1.txt`, et sur les empreintes données par la fille et session-depot.
