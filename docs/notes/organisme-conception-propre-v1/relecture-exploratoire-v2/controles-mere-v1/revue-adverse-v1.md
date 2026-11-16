# Revue adverse de la marche du § 6 — relecture exploratoire v2 (règle v2.1, outil v3.2.1) — v1

Début : 2026-11-14 22:35:21 UTC. Fin : 2026-11-14 22:41:28 UTC (`date -u`, relevée juste avant le scellement).
Contrôleur neuf (modèle C pour la lecture), sous-agent de la session mère. Chemins relatifs à
`docs/notes/organisme-conception-propre-v1/` ; `RE/` = `relecture-exploratoire-v2/` ; `OUT/` = `RE/lecture-classement-v3-2/`.

## Verdict

**Go avec réserves.** Je n'ai pas réussi à réfuter que la marche est sûre sur l'argent, la clé et le classement : aucun
bloquant. Deux défauts majeurs d'exécution (M1 : durée du point 7 contre le plafond de temps d'une commande ; M2 : essais
rejoués ici, un écart de compte) et plusieurs mineurs sont à lever ou à décider **avant** le point 6. Rien n'a été envoyé.

## Ce que j'ai fait, et pas fait

- Lu : `rapport-v1.md` (§ 4 à § 7), `regle-v2-1.md`, la contre-lecture, les deux notes de corrections, la relecture courte,
  l'outil v3.2.1 (préparer, envoyer, bilan, verifier, garde) et le classement v3.2.1 en entier, le devis, le registre
  (R-2726, R-2759, R-2804), le journal de dépense de la première lecture (heures, coûts, jetons : aucun texte).
- **Joué sous `unshare -n`** (basetemp dans le dossier temporaire de la session, aucun octet écrit dans le dépôt hors ce
  rapport) : `essais_lecture_classement_v3_2_1.py` et `outils/essais_temoins_et_hasard_v2_1.py` : **246 passés, 1 ignoré**
  (voir M2), en 44,6 s. Recalcul par programme de la table de puissance (loi hypergéométrique exacte) : **identique à celle
  de la règle** (§ 6.7).
- Empreintes : outil, classement, essais, règle, témoins du lecteur, hasard v2.1, devis, rapport : `OK` (K1 rejoué). Dossier
  `lecture-g1-v3-2` : **absent** avant et après. Arbre git : seul `controles-mere-v1/` est non suivi.
- Jamais fait : `envoyer`, appel réseau, lecture ou affichage de la valeur de la clé (j'ai seulement testé par
  `[ -n "${v+x}" ]` que `HTTPS_PROXY`, `https_proxy`, `SSL_CERT_FILE` et `OPENAI_API_KEY` sont **définies** dans cette
  session : valeur jamais lue), lecture du texte des fiches ou d'un envoi. J'ai lu `/root/.ccr/README.md` (documentation du
  mandataire). Aucune permission ni aucun classifieur ne m'a refusé de geste.

## Constats

### Bloquant

Aucun.

### Majeur

**M1. Le point 7 (17 appels d'un seul tenant) frôle, et peut dépasser, le plafond de 600 s d'une commande ; une commande
tuée en vol détruit le dossier unique.**
- Preuve : à la première lecture (même outil, même palier, même effort), les 17 appels ont pris de 10:38:35 à 10:48:13, soit
  **578 s** (journal `lecture-g1-v3-1/envois/journal-depense-v3-1.jsonl` : appels de 22 à 63 s, moyenne ≈ 33 s). La pile
  servie est ici plus lourde de 11,6 % en octets (devis v2) : la durée attendue est de 560 à 650 s. Un appel de premier plan
  est tué à 120 s par défaut et à 600 s au plus.
- Effet (outil, `envoyer` et `lire_journal`) : un processus tué entre « envoi » et « clos » laisse un appel « en vol » :
  compté au pire cas (≈ 1,09 USD), **plus aucun envoi** (« aucune reprise »), la réponse payée éventuellement perdue ;
  seconde préparation = nœud (r6). L'argent n'est pas dépassé, mais la lecture est perdue pour un détail d'exécution.
- Le § 6 ne dit rien de la durée ni de la manière de lancer (arrière-plan, tranches).
- Correction : écrire au point 7 soit un lancement en arrière-plan avec attente du code de sortie, soit des tranches
  `--envois-max 6` (trois commandes d'environ 3,5 minutes, la clé relue à chaque fois), avec `bilan` entre chaque ; et pour
  le point 6 un délai d'au moins 300 s.

**M2. Les essais ne donnent pas « 247 passés » ici : 246 passés et 1 ignoré.**
- Cause : `test_normalisation_egale_a_celle_de_l_orchestrateur` s'ignore si le clone de l'orchestrateur est absent (essais,
  ligne 489 et suivantes) ; ce clone manque dans cette session. Ce n'est pas un défaut de l'outil, mais le critère du
  point 3 (« → 247 passés ») est faux dans une session sans le clone, et un opérateur pourrait y lire un échec ou, pire,
  s'habituer à passer outre un écart de compte.
- Correction : dire « 247 passés, ou 246 passés et 1 ignoré si le clone de l'orchestrateur est absent » ; ou rejouer ce seul
  test dans une session qui a le clone (l'égalité de la normalisation typographique est celle qui fixe la vue servie).

### Mineur

**m1. Question (a) : la garde de dépense tient ; trois écarts bornés.** Le plafond est vérifié avant chaque appel, un à la
fois, sur la dépense relue du journal (coupure, statut non 200, usage absent ou incohérent : pire cas ; cache, raisonnement et
excédent de total comptés) ; le plafond du manifeste est borné par 11,65 moins la dépense antérieure et revérifié à l'envoi ;
la dépense de la première lecture (2,556635) est bien celle du relevé épinglé et du registre (cumul 9,347722 sur 21).
Dépassement possible seulement dans ces cas :
- (i) **palier servi autre** (le fournisseur répond « default » à une demande Flex) : l'appel est compté au prix Flex alors
  qu'il est facturé au standard (jusqu'à deux fois) ; l'anomalie arrête tout après cet appel : écart borné à un appel
  (au plus ≈ 2,2 USD au pire cas standard, ≈ 0,15 attendu). À corriger au registre à la main si cela arrive ;
- (ii) **reprise par le mandataire ou le réseau** d'un POST non vu de l'outil : non comptée ; aucune preuve ici, à dire ;
- (iii) **seuil du premier appel** : « ≤ 0,33 » est le seuil de bout en bout du devis (6,5 − 1,117) / 16,2, valable si les
  appels suivants coûtent autant ; la garde peut arrêter avant le dix-huitième appel si la moyenne dépasse ≈ 0,32 : arrêt
  net, non silencieux, lecture incomplète (E2 v2).
Le prix lui-même (Flex 5 / 0,5 / 25) vient de `prix-astra-v2.md` (empreinte épinglée) : non revérifié auprès du fournisseur
(R7 du programme : rien ici ne l'établit).

**m2. Question (b) : tous les arrêts sont bruyants ; ce qu'il reste.**
- Refus du palier Flex (429 « ressource indisponible », 400, 403 du mandataire), coupure, délai, lecture partielle d'un
  corps (`IncompleteRead`) : l'envoi est écrit au journal **avant** l'appel ; l'issue est close au pire cas
  (`transport_echec` ou `statut_non_200`, corps jamais écrit, fichier d'erreur scellé), code 3, relevé scellé ; tout
  `envoyer` suivant refuse (« lecture déjà arrêtée »). Une réponse 200 est écrite brute et scellée **avant** analyse ; une fin
  autre que `stop`, un usage incohérent, un modèle ou un palier autre gardent la réponse payée et arrêtent.
- Reste : journal chaîné, relevé, fichier d'erreur ou réponses déjà reçues, corps non envoyés ; `verifier` et le classement
  rendent « E2 v2, lecture incomplète » (réponses absentes = anomalie bloquante, jamais une valeur inventée). Perdus : le
  droit d'envoyer (dossier unique), et la réponse d'un appel coupé en vol. **Pas de perte silencieuse.**
- Réserves : (i) un refus Flex est compté au pire cas (≈ 1,09 USD) alors qu'il n'est sans doute pas facturé : la somme à
  déclarer en `--depense-anterieure-usd` d'une seconde préparation est surestimée (sans danger) ; (ii) la seconde préparation
  repose sur la déclaration de l'opérateur : l'outil ne peut pas vérifier cette somme, et « supprimer le dossier » (m7 de la
  contre-lecture) contredit R12 : écrire plutôt « déplacer hors de `docs/` et `runs/` », sous nœud de Lazar ;
  (iii) une réponse de plus d'un million d'octets serait payée et non gardée (anomalie, corps non écrit) : irréaliste
  (moins de 200 ko).

**m3. Question (c) : la clé n'apparaît ni dans un fichier, ni dans une sortie, ni dans une ligne de commande de la marche.**
Lue par `lire_cle` par son nom, retirée de l'environnement du processus, refusée si hors ASCII imprimable ; l'en-tête n'est
en mémoire que dans `envoyer` ; journal, réponses, erreurs, relevé passent par `expurger` (six formes) ; une réponse qui la
porte est une anomalie bloquante ; le message d'une exception de transport n'est jamais écrit (le type seul) ; les erreurs
imprimées sont des textes fixes. Le point 6 ne la met pas en argument (variable d'environnement gardée par son nom). Réserves :
- **K6 est joué trop tôt** (point 9, avant le point 10) : les fichiers du `verifier` et du classement, qui reprennent des
  passages des réponses, ne sont jamais balayés ; le registre de dépenses et le rapport de l'opérateur non plus. Rejouer K6
  après le point 10, sur `lecture-g1-v3-2` entier, et sur les sorties capturées par l'opérateur s'il en garde.
- La façon dont l'opérateur obtient la clé dans son environnement n'est pas écrite (le § 6 dit « lue par son nom ») : à dire
  (jamais `export OPENAI_API_KEY=…` dans une commande).
- **Le commentaire de `transport_reel` est faux dans cette session** : « en HTTPS, l'en-tête d'autorisation passe dans le
  tunnel, jamais au mandataire ». Le mandataire de la session **re-termine TLS** (`/root/.ccr/README.md` : « TLS is
  re-terminated there ») : le mandataire de sortie voit donc l'en-tête. Ce n'est pas un défaut de l'outil, mais Lazar doit
  savoir que la clé transite en clair pour ce relais ; rien dans la marche ne l'empêche.
- La boucle `compgen -e … unset` laisse passer `PATH`, `HOME`, `HTTPS_PROXY`, `https_proxy`, `SSL_CERT_FILE` et la clé : jeu
  suffisant (l'outil lit `SSL_CERT_FILE`, et le mandataire passe par l'environnement) ; elle ôte `PWD`, `LANG`, `TMPDIR` sans
  conséquence ; un `unset` d'une variable en lecture seule imprimerait une erreur sans valeur.

**m4. Route non éprouvée à vide.** La première lecture avait fait un `GET /v1/models` **sans clé** (401 attendu) avant le
premier appel (`lecture-g1-v3-1/journal-et-releve-v1.md`, 10:36:20). Le § 6 ne le reprend pas ; le contrôle à blanc l'a
recommandé. Un refus du mandataire (403, hôte non autorisé) ou une erreur TLS survient **après** l'écriture de l'envoi au
journal et tue le dossier (r6, décidé par la mère à R-2804 : nœud). Rejouer ce `GET` sans clé (geste réseau séparé, à valider
par Lazar ou la mère) avant le point 6 coûterait zéro.

**m5. Question (d) : le classement applique la règle v2.1 telle qu'écrite ; la mention est forcée.** Contrôlé ligne à ligne :
portes R2 et R3 retenues ; S v2 = R1 + R4 + R5 + R6 + R7 ; C v2 = 1[portes et N = aucune] × (1 + S v2) ; rang des neuves
(S décroissant, `processeur` avant `depense`, départage enfant 2) et rang restreint à R7 = 1 en information ; L1 (au moins 5
sur 7 dans au moins une lecture), L2, L3 v2 (R7 prouvé dans au moins une lecture), L4 (κ ≥ 0,4 ou accord brut ≥ 0,8),
lisible = lecture complète et L1 à L4 ; L5 v2 par permutation unilatérale (100 000, `SeedSequence(2026111303)`), séparation
(`2026111404`) toujours calculée et lue seulement si L5 rejette, issues renommées, « (non lue : classement non lisible) »,
E2 v2 à E5, audit R4, huit descriptifs avec Holm, descriptifs de la règle § 7. `designees` vaut `[]` en dur et
`verdict += " ; exploratoire : aucune idée désignée (règle v2)"` s'applique après **toutes** les branches (y compris E1 et
lecture incomplète). Écarts, tous sans effet sur le verdict : (i) la mention dit « règle v2 » alors que c'est la v2.1 (le
champ `regle` du JSON dit v2.1) ; (ii) la table de puissance de la règle commence à 10 réelles à R7 = 1, alors que 9 tient
aussi (j ≤ 0) : incomplète, inoffensive ; (iii) **la décision de séparation est un test par permutation de Monte-Carlo, la
table de la règle est exacte** : à 18 réelles et 3 idées au hasard à R7 = 1, le p exact est 0,0484, marge de 0,0016 pour une
erreur de Monte-Carlo d'environ 0,0007 : environ 1 chance sur 100 que le programme dise « non établie » là où la table dit
« réelle » (cas 20 et 4 : exact 0,0528, risque inverse négligeable). Le résultat est déterministe (graine fixée), donc à
rapporter avec le p exact en cas de voisinage du seuil.

**m6. Question (e) : conditions des deux verdicts, une à une.**
- Contre-lecture « utilisable sous conditions » : 1 (empreintes) levée (K1 rejoué) ; 2 (manifestes, absence, **arbre git
  propre**) : K8 et l'absence tiennent, mais « l'arbre git propre » n'est pas dans le § 6 (et il ne l'est pas à cet instant :
  le dossier `controles-mere-v1/` est non suivi) ; 3 (essais et bancs, « 0 échec et 0 mutant vivant ») : essais rejoués par
  moi, 0 échec ; **mutants : deux survivants** (générateur du hasard : « pièces servies oubliées », équivalent sur la sortie
  scellée ; « phrases par fiche non contrôlées », lacune d'essai) et deux inapplicables (outil) : condition « 0 vivant »
  **non remplie à la lettre, déclarée** (r1, § 5), sans effet sur l'argent ; le § 6 ne rejoue d'ailleurs pas les bancs ;
  4 (paramètres, ≤ 0,33) levée au point 4 et en K4 ; 5 (M1, M2, M3, M5) : M1, M2, M3 traités dans la règle v2.1 ; M5 tranché
  par la mère (R-2804) ; 6 et 7 : points 13 (à faire après).
- Relecture courte « suffisantes sous conditions » : 1 (essais et bancs versés) levée (`resultat-essais-…-3-2-1.txt`,
  229 passés ; bancs 32/34 et 23/25) ; 2 (condition de la seconde préparation dans une pièce scellée) levée par le rapport,
  non par la règle ni le devis ; 3 (ambiguïté de `regle-v2-1.md` § 4 : « aucun appel payant (sous-agents de la session) »)
  **non levée dans la règle**, seulement précisée au rapport ; la mère note de plus (R-2759) que ces relecteurs ont consommé
  le quota du compte : la phrase de la règle reste trompeuse ; 4 (M5 par la mère) levée par R-2804 ; m5 levée (R-2804).
- Réserves déjà nommées, toujours vraies : r1 (bancs de l'auteur entièrement tués : « trop propres »), r6.

**m7. Concurrence.** Aucun verrou de fichier : deux `envoyer` lancés dans la même fraction de seconde liraient le même
journal et enverraient le même lot deux fois (le second sort ensuite en erreur de chaîne). Un second lancement **après** le
premier écrit son envoi est refusé (appel en vol). Risque réel faible ; à écrire : un seul processus à la fois.

**m8. Divers.** La règle v2.1 garde la tolérance ± 0,08 et la note des corrections ± 0,15 (déclaré, plus strict) ; le point 6
et K4 supposent `completion_tokens` incluant le raisonnement, vérifié au premier appel (C3) ; K9 vise
`valeur de N illisible`, motif qui existe dans l'outil (ligne 1288) ; `contient_cle` utilisé en K6 existe.

## Réponses brèves

| Question | Réponse |
|---|---|
| (a) dépasser 6,50 USD ? | Non par l'outil seul : garde avant chaque appel, un appel à la fois, journal relu, pire cas en cas de doute, plafond borné à 11,65. Écarts bornés : palier servi autre (un appel), reprise invisible du mandataire (non éprouvée), m1. |
| (b) refus Flex, coupure, réponse partielle | Arrêts nets, rien d'inventé, réponse payée gardée si reçue ; dossier unique perdu pour envoyer ; lecture incomplète (E2 v2). M1 : le plus probable est une coupure causée par la commande elle-même. |
| (c) clé | Non (fichier, sortie, ligne de commande). Réserves : K6 trop tôt ; mandataire qui re-termine TLS ; origine de la clé non écrite. |
| (d) classement | Fidèle à la règle ; mention forcée par le code ; écarts de forme (m5). |
| (e) conditions | Levées, sauf : « 0 mutant vivant » non remplie à la lettre (déclarée), arbre git propre absent du § 6, ambiguïté de la règle non levée dans la règle. |

## Corrections minimales avant le point 6

1. M1 : lancer le point 7 en arrière-plan ou par tranches `--envois-max 6`, avec `bilan` entre chaque.
2. M2 : écrire « 247 passés, ou 246 passés et 1 ignoré sans le clone de l'orchestrateur » (ou jouer ce test là où le clone existe).
3. m4 : décider du `GET /v1/models` sans clé (zéro coût) avant le premier appel.
4. m3 : rejouer K6 après le point 10 ; dire d'où vient la clé ; informer Lazar que le mandataire voit l'en-tête.
5. m6 : ajouter `git status` propre au point 2 ou le retirer des conditions ; dire que « 0 mutant vivant » n'est pas tenu.
