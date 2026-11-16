# Contre-lecture de la procédure de la machine du jeu relancé de l'idée 1.1, tour 1 (v1)

- **Auteur** : contre-lecteur neuf (R2), lettre C. Il n'a écrit aucune pièce du dossier (pièces de la lettre A).
- **Heures (UTC, `date -u`)** : de 21:25Z à 21:40Z environ.
- **Pièces lues, entières** (compagnons vérifiés : 9 sur 9 `OK`) : `procedure-machine-jeu-idee-1-1-v1.md`,
  `devis-machine-jeu-idee-1-1-v1.md`, `rapport-machine-jeu-idee-1-1-v1.md`, `lancer_jeu_idee_1_1_machine_v1.sh`,
  `garde_machine_jeu_idee_1_1_v1.py`, `amorce_jeu_idee_1_1_v1.sh`, `repetition_machine_jeu_idee_1_1_v1.sh`,
  `jeu_factice_idee_1_1_v1.py`, `sortie-repetition-machine-jeu-idee-1-1-v1.txt`.
- **Modèles lus** : `lancer_bbis_v3.sh`, `amorce_bbis_v3.sh` (arbre de travail de B bis, lecture seule), contre-lecture de la
  création de B bis (C1 à C8) ; lignes R-2996 à R-3004 et R-3014 ; en plus, pour recouper : R-3010, R-3012, R-3015 à R-3017,
  les lignes GO-2026-11-16-09 et GO-2026-11-16-10 de `registres/go.md`, l'addendum de relance (brouillon 4 et son contrôle
  de mise au propre), `scripts/jouer_idee_1_1_v5.py` et `execution_idee_1_1_v5.py` (par `git show` dans le bloc-notes).
- **Ce que j'ai rejoué** (tout dans le bloc-notes, aucun appel au loueur, aucune machine, aucune dépense) :
  1. la répétition locale entière, dans un dossier neuf : **110 cas, 110 `OK`, 0 écart** (21:27:37Z à 21:29:45Z), sortie
     égale à la sortie gardée une fois les chemins, heures et longueurs de ligne normalisés ;
  2. la ligne de création imprimée par `commande` (sortie de ma répétition), son outil de loueur remplacé par un exécutable
     factice : elle s'analyse telle quelle (argument `--env` unique, `--args -c`, redirection vers un fichier de mode 600),
     seuls `success`, `new_contract` et les noms de clés s'affichent, la valeur du jeton ne figure ni dans le fichier de
     réponse ni dans l'affichage ;
  3. recoupements indépendants : les trois empreintes figées du lanceur et de l'amorce (texte, addendum d'empreintes, essai
     du § 6 point 3) sont égales entre elles et à celles de `HEAD` (`git show`, 64 caractères) ; l'addendum de relance de
     `HEAD` porte `a692d50c…` avec un compagnon d'une ligne ; analyse des importations des 46 fichiers gelés : seuls `numpy`,
     `scipy`, `pytest` sont tiers (confirme le rapport, § 2 point 2) ; lecture publique (sans donnée du programme) : l'étiquette
     `python:3.13.18-bookworm` existe (image amd64 `sha256:2784af83…`), `numpy 2.4.6`, `scipy 1.17.1`, `pytest 9.1.1` existent
     et ont une roue `cp313` `manylinux` x86_64 pour les deux premiers.

## Verdict : `corrections`

La conception tient (aucun motif de `a_refaire`) : les gardes sont éprouvées sur cas sain et artefact, aucune clé ne s'affiche
ni ne s'écrit, la branche de sortie est orpheline et neuve, la destruction se fait par l'identifiant lu, jamais tapé, et se
prouve par un témoin. **Mais trois points majeurs et sept mineurs demandent des corrections avant le feu.** Le premier majeur
(M1) peut perdre un jeu de 15,7 heures entier sur une machine arrêtée ; le deuxième (M2) peut faire détruire à tort un jeu sain ;
le troisième (M3) laisse dans la procédure des préalables déjà levés, que la mère prendrait pour des blocages.

## Constats par point demandé

**(1) Exactitude des tirages : tenue.** Image `python:3.13.18-bookworm` (existe) ; installation `numpy==2.4.6 scipy==1.17.1
pytest==9.1.1` ; lecture de `3.13.18 2.4.6 1.17.1` par l'interpréteur du jeu, nommé par son chemin, comparée à la chaîne exacte de
l'addendum de relance (4.2), arrêt **avant tout clonage** si elle diffère (répété avec numpy 2.5.3). Même commit : `COMMIT` doit
être ancêtre de `main`, arbre propre ; même addendum : texte, addendum d'empreintes, addendum de relance (compagnon d'une ligne
et `EMPREINTE_RELANCE`) et essai vérifiés au commit, côté session puis côté machine ; même commande : `scripts/jouer_idee_1_1_v5.py
--addendum prereg/…-addendum-empreintes-v1.md`, `-I -B`, jamais `--reprendre` (aucune branche de reprise dans l'amorce). Limite
déclarée, non corrigeable : autre processeur, autre système (voir le rapport, § 5 point 3). Réserve facultative F1.

**(2) Gardes : tenues, avec les réserves M1 et M2.** Offre (jouée hors ligne sur chaque offre), création (feu en forme courte,
ligne de GO « calcul », Lazar, période, révocation, périmètre « idée 1.1 », plafond lisible), prix relu, dépense, identifiant,
absence : chacune a son cas sain et son artefact dans la répétition, que j'ai rejouée. Minuterie : TERM par le PID seulement
au-delà de la borne de 48 h comptée depuis `depart.json`, destruction par l'identifiant redemandée sans fin, « stopped » après la
cinquième demande ; répétée dans les deux sens. Aucune destruction par motif de ligne de commande (R10) dans aucune pièce.
Non éprouvé, et déclaré par le rapport : l'API réelle du loueur (`PUT`/`DELETE` sur `/api/v0/instances/<id>/`) ; la
minuterie est donc une défense dont le fonctionnement réel n'est pas encore vu, et seule la garde horaire de la session la
double (voir P3 ci-dessous).

**(3) Clés et sorties : tenu.** Aucune valeur de clé affichée ni écrite : la ligne porte `$GH_TOKEN` en lettres, la réponse du
loueur va dans un fichier de mode 600, seuls les noms de clés s'affichent, la liste brute des instances est effacée par son chemin
exact. Branche `calcul/idee-1-1-jeu-relance-v1`, neuve, orpheline, qui ne reçoit que `traces/machine-jeu-idee-1-1-v1/`,
`runs/<run>/` et `diag/organisme-idees-juge-v1/<run>/` ; le dépôt du jeu ne peut pas pousser (adresse de poussée invalide) ;
un fichier de plus de 94 Mo ou un chemin hors des sorties est refusé. La sortie standard du jeu (poussée avec les traces) ne
porte que le nom du run, l'empreinte de `sortie.json`, le dossier et le nombre de tranches : aucun résultat (vérifié dans
`jouer_idee_1_1_v5.py` l. 165 et `execution_idee_1_1_v5.py`).

**(4) Gestes de l'opérateur : presque tapables telle quelle, avec les corrections m1, m2, m3 ; pièges de B bis évités.** C1
(chaque appel redonne ses constantes), C2 (inventaires et choix de l'offre par programme), C3 (ligne ramenée à ≈ 11,9 Ko, deux
morceaux, `cmp`), C4 (forme courte `R-<N> GO-…`, un seul numéro de GO dans toute commande qui porte le lancement), C5 (`GH_TOKEN`
exporté dans le même appel), C7 (témoins dans l'ordre), C8 (liste brute effacée) : tous repris. C6 (crédit) : recharge
automatique, consignée au feu.

**(5) Devis : arithmétique juste, deux manques (M2, m5, m6).** 16,7 × 0,0522 = 0,87 ; 16,7 × 0,06 = 1,00 ; 24,4 × 0,06 = 1,46 ;
12 × 0,01 = 0,12 ; 0,5 × 0,06 = 0,03 ; 50 × 0,06 = 3,00 ; 3,00 + 24 × 0,01 = 3,24 ; + 0,06 = 3,30 ; surcoût de la minuterie
1,75 h × 0,06 = 0,105 : tout recalculé, exact. Cohérence des constantes (lanceur 49 h 30 à 50 h, amorce 48 h 50 à 50 h, marge de
jeu 48 h 40, TERM 20 minutes avant l'échéance) : exacte, et la raison de 49 h 45 plutôt que 48 h tient (la borne de 48 h court
depuis `depart.json`, après la mise en place et les ≈ 17 minutes de contrôles). Écart à la lettre de la tâche (« minuterie de
48 h ») : déclaré, **acceptable**, à faire trancher (P1).

**(6) Hors périmètre et identifiants : tenu.** Aucun contenu de 7a, 7b, T0.6, T0.7, P3-bis, du bras d'attaque ; seules mentions :
des chemins de B bis cités comme modèles (rapport § 6). Aucun identifiant de modèle dans aucune pièce (lettre A seulement).

## Corrections exigées

Chaque « ancien » ne figure qu'une fois dans le fichier cité (vérifié par programme sur les fichiers du dossier). Les couples
du code (M1, amorce) sont des formes indicatives : la lettre A les fixe et les répète (cas à ajouter à la répétition, voir M1).

### Majeures

**M1. Une poussée des sorties qui échoue arrête la machine et enferme le jeu de 15,7 h sur un disque arrêté.** Au pas 7 de
l'amorce, `commit_pousser` n'essaie que trois fois (pauses de 30, 60 et 90 s) ; au premier échec, `arret … 4` appelle
`fin_machine`, qui demande « stopped ». La poussée des traces échoue alors sans doute aussi (même cause). La procédure
(§ 1 pas 7, § 2 « Après le jeu », geste 13) n'a aucun moyen de récupérer les sorties d'une machine arrêtée ; le rapport (§ 4)
lui-même dit que ce cas n'est pas éprouvé (« poussée des sorties impossible » est un code 4 listé, jamais répété). Une coupure
de quelques minutes de GitHub, un jeton expiré ou une limite de débit à la mauvaise minute perdent donc le run entier, sans
relance possible sans addendum neuf. Correction : reprendre la poussée toutes les cinq pauses
jusqu'à 20 minutes avant l'échéance, **machine vivante**, et ne demander « stopped » qu'après poussée réussie ou
épuisement des reprises ; ajouter à la répétition deux cas (poussée refusée trois fois puis acceptée : machine vivante,
sorties poussées, aucun « stopped » avant ; poussée jamais acceptée : reprises journalisées, arrêt en code 4 à
l'échéance − 20 minutes, sorties intactes sur le disque) ; dire au geste 13 de ne rien détruire dans ce cas.
- `amorce_jeu_idee_1_1_v1.sh`, couple 1 : ancien `RUN="$RUNS"` → nouveau
  `RUN="$RUNS"` suivi, sur les lignes suivantes, de la fonction
  `reprise_sorties() { j "RESERVE : poussée des sorties impossible : reprise toutes les $((PAUSE * 5)) s, machine gardée vivante jusqu'à $MARGE_TERM s avant l'échéance"; while [ "$(date +%s)" -lt $((ECH - MARGE_TERM)) ]; do sleep $((PAUSE * 5)); ( flock -w 600 9 || exit 1; for p in "runs/$RUN" "$DIAG/$RUN"; do [ -d "$D/$p" ] || continue; [ -d "$S/$p" ] || { mkdir -p "$S/$(dirname "$p")" && cp -a "$D/$p" "$S/$p"; } || exit 1; diff -r -q "$D/$p" "$S/$p" > /dev/null || exit 1; done; mapfile -d '' -t F < <(cd "$S" && find "runs/$RUN" "$DIAG/$RUN" -type f -print0 | sort -z); for ((k = 0; k < ${#F[@]}; k += 400)); do git -C "$S" add -f -- "${F[@]:k:400}" && commit_pousser "sorties du run $RUN : reprise, lot $((k / 400 + 1))" || exit 1; done ) 9> "$VERROU" && { j "poussée des sorties reprise : réussie"; return 0; }; done; return 1; }`
  (écrite sur plusieurs lignes dans le fichier).
- `amorce_jeu_idee_1_1_v1.sh`, couple 2 : ancien
  `) 9> "$VERROU" || arret "recopie ou poussée des sorties du run $RUN impossible (sorties restées sur la machine arrêtée ; nœud de la mère)" 4`
  → nouveau
  `) 9> "$VERROU" || reprise_sorties || arret "recopie ou poussée des sorties du run $RUN impossible après reprises (sorties restées sur la machine arrêtée ; nœud de la mère)" 4`.
- `procedure-machine-jeu-idee-1-1-v1.md`, couple 3 : ancien
  `poussée par lots (manifeste, puis tranches par 400 fichiers) ; un chemin hors des` → nouveau
  `poussée par lots (manifeste, puis tranches par 400 fichiers), reprise toutes les 5 minutes jusqu'à 20 minutes avant l'échéance si une poussée échoue, la machine restant vivante (aucun « stopped » tant que les sorties ne sont pas poussées) ; un chemin hors des`.
- `procedure-machine-jeu-idee-1-1-v1.md`, couple 4 : ancien
  `13. **Fin** : le journal porte « FIN » (code 0) ou « ARRET » (code 2 ou 4),` → nouveau
  `13. **Fin** : le journal porte « FIN » (code 0) ou « ARRET » (code 2 ou 4 ; sur « RESERVE : poussée des sorties impossible », ne **rien détruire** : nœud de la mère, qui décide de la copie depuis la machine vivante avant l'échéance),`.

**M2. L'échéance de la ligne de GO n'est proposée nulle part, et la garde de dépense la relit à chaque appel.** La procédure
(§ 2 point 4) écrit « échéance. Proposition au devis », le devis n'en propose aucune. Or `garde_depense` rappelle
`exiger_go_calcul`, qui refuse une date hors de la période de la ligne : avec une échéance au 16 ou au 17 novembre, l'appel
horaire du geste 12 rend le code 2 dès le passage de minuit, et la consigne du geste 12 (« code 2 : destruction ») ferait
détruire un jeu sain, donc le rendrait invalide. Le jeu et ses suites tiennent sur trois dates civiles au pire (50 h, plus 24 h
d'arrêt).
- `devis-machine-jeu-idee-1-1-v1.md`, couple 5 : ancien
  `| Plafond de la ligne de GO proposé | **3.5 USD** (lu par la garde de dépense : cumul + une heure ≥ plafond → destruction) | ligne de GO à inscrire |`
  → nouveau le même texte, suivi d'une ligne de table
  `| Échéance de la ligne de GO proposée | **2026-11-22** au plus tôt (celle de GO-2026-11-16-09 et GO-2026-11-16-10) ; ne jamais la raccourcir : la garde de dépense relit la ligne à chaque appel horaire, et un jeu de 17 à 50 h plus un arrêt de 24 h tient sur trois dates civiles | ligne de GO à inscrire |`.
- `procedure-machine-jeu-idee-1-1-v1.md`, couple 6 : ancien
  ``plafond écrit `3.5 USD` (point décimal ; la garde de dépense le lit), échéance. Proposition au devis.`` → nouveau
  ``plafond écrit `3.5 USD` (point décimal ; la garde de dépense le lit), échéance 2026-11-22 au plus tôt (devis § 1 : la garde de dépense relit la ligne à chaque appel ; un code 2 de date au geste 12 est un nœud de la mère, jamais un ordre de destruction).``

**M3. Préalables périmés dans la procédure : D7 est tranché, l'addendum de relance est scellé, commité et poussé.**
`registres/go.md` porte GO-2026-11-16-10 (Lazar, « Ma recommandation est d'accepter, confiance 0,65. : go », inscrit à
20:47:50Z, R-3016) : l'écart D7 est accepté. L'addendum de relance est scellé sous `prereg/` (R-3017, `a692d50c…`), commité
(`14a0dfc5…`, ancêtre de la tête de `main` `e395dd47…` à 21:3xZ) et poussé. La procédure demande encore à la mère de dire si
GO-09 vaut le mot sur D7, « sinon nœud de Lazar avant tout » : consigne périmée qui fait croire à un blocage ; et elle ne cite
pas GO-10 dans la ligne « calcul », alors que GO-10 est le texte qui prévoit cette ligne sur ce devis.
- `procedure-machine-jeu-idee-1-1-v1.md`, couple 7 : ancien `La mère dit au registre si GO-2026-11-16-09` → nouveau
  `Le mot de Lazar sur D7 est inscrit : GO-2026-11-16-10 (R-3016, 2026-11-16T20:47:50Z) ; GO-2026-11-16-09 ne sert qu'à l'option (a)`.
- `procedure-machine-jeu-idee-1-1-v1.md`, couple 8 : ancien
  `(« option (a) … machine de calcul louée ») est ce mot ; sinon, nœud de Lazar avant tout.` → nouveau
  `(« option (a) … machine de calcul louée ») ; plus aucune question de la mère sur D7 ; le feu cite GO-2026-11-16-10 en toutes lettres.`
- `procedure-machine-jeu-idee-1-1-v1.md`, couple 9 : ancien `citant GO-2026-11-16-09 : périmètre` → nouveau
  `citant GO-2026-11-16-09 et GO-2026-11-16-10 : périmètre`.
- `procedure-machine-jeu-idee-1-1-v1.md`, couple 10 : ancien
  `1. L'addendum de relance est scellé sous son nom final `prereg/organisme-idee-1-1-poids-du-nul-v2-addendum-relance-v1.md`` →
  nouveau le même texte suivi de
  ` (déjà fait : R-3017, empreinte `a692d50c07c1b4b7ef07883ac91124eab4798cab7a579e14235484ea4d2319cf`, commit `14a0dfc5962aad5987d6c88e03e72b5f6d92f150`, ancêtre de la tête de `main` à 21:3xZ ; à relire au moment de remettre la suite, `COMMIT` pouvant être la tête de `main` du moment)`.
- `devis-machine-jeu-idee-1-1-v1.md`, couple 11 : ancien `- **Pour** : GO-2026-11-16-09, point (2)` → nouveau
  `- **Pour** : GO-2026-11-16-09, point (2), et GO-2026-11-16-10 (écart D7 accepté ; même ordre de grandeur de 1 à 3 USD)`.
- `rapport-machine-jeu-idee-1-1-v1.md` (v2 de la lettre A) : son verdict et sa réserve § 5 point 1 présentent D7 comme ouvert ;
  à réécrire dans un fichier neuf avec la date de GO-10.

### Mineures

**m1. Geste 5 : un refus du lanceur est écrit dans le fichier et n'est jamais vu.** `commande … > commande-imprimee.txt` ;
`echo "code $?"` et `wc` n'affichent pas la ligne `JEU11 REFUS : …`, que « Tout `JEU11 REFUS` : arrêt » suppose lue.
- Couple 12 (procédure) : ancien
  ``"$D/commande-imprimee.txt"; echo "code $?"; wc -lc "$D/commande-imprimee.txt"` → `code 0`, **2** lignes, ≈ 12 100 octets.`` →
  nouveau
  ``"$D/commande-imprimee.txt"; echo "code $?"; wc -lc "$D/commande-imprimee.txt"; head -n 1 "$D/commande-imprimee.txt" | cut -c1-300` → `code 0`, **2** lignes, ≈ 12 100 octets, puis l'en-tête `JEU11 COMMANDE (…)` ; un refus s'y lit (`JEU11 REFUS : …`, première ligne seule, jamais le base64).``

**m2. Geste 13 : la recopie des sorties n'est pas une commande.** `git archive` écrit un fichier tar sur la sortie standard ;
rien ne l'extrait, le `fetch` préalable manque, `<run>` n'est pas dit.
- Couple 13 (procédure) : ancien
  ``refs/remotes/origin/$BR runs/<run> diag/organisme-idees-juge-v1/<run>` vers le dépôt, puis chaque compagnon vérifié`` →
  nouveau
  ``refs/remotes/origin/$BR runs/<run> diag/organisme-idees-juge-v1/<run> | tar -x -C $R` (après `git -C $R fetch origin +refs/heads/$BR:refs/remotes/origin/$BR` ; `<run>` est le nom donné par la ligne « FIN : … run … » du journal ; refuser si l'un des deux dossiers existe déjà dans `$R`), puis chaque compagnon vérifié``.

**m3. Gestes 11 à 16 : le texte les range sous « gestes de l'opérateur » mais pas la durée.** Un sous-agent ne tient pas 16 à
50 heures de relèves horaires ; § 2 range la surveillance sous la mère. Dire qui joue quoi.
- Couple 14 (procédure) : ancien `11. **Surveillance** : la première poussée` → nouveau
  `11. **Surveillance** (par la mère, ou par un opérateur que le feu nomme et dont la tâche dure aussi longtemps que le jeu ; aucun rappel seul n'y suffit) : la première poussée`.

**m4. Réseau pendant le jeu : à déclarer.** Le texte scellé (l. 629) écrit « toute dépense, instance payante, appel réseau ou appel
de modèle : interdit » ; GO-10 accepte la machine louée et la dépense ; l'addendum (4.10) dit qu'aucun appel réseau ne se fait
pendant le jeu (garde réseau du lanceur) et renvoie à la procédure pour ce qui précède le départ. Mais l'amorce pousse chaque
heure `etat.txt` et le journal (comptes et dates de fichiers) pendant le jeu, par un processus de la machine hors du jeu, et pousse
les sorties à la fin : le texte ne le dit nulle part. Ni la garde du jeu ni le contenu des poussées ne sont en cause ; c'est une
lecture de l'écart D7, que la mère doit déclarer (P2).
- Couple 15 (procédure, § 5) : ancien
  `- Elle ne lit aucun résultat ; elle ne compare pas le run neuf au run invalide (interdit, addendum de relance § 3).` → nouveau
  le même texte, suivi d'une puce :
  `- Elle ne se passe pas du réseau pendant le jeu : la machine pousse chaque heure `etat.txt` et le journal (comptes et dates de fichiers, jamais un contenu) vers la branche de sortie, hors du processus du jeu dont la garde réseau tient ; ces poussées et celle des sorties à la fin sont déclarées comme part de l'écart D7 (texte scellé l. 629), que le feu cite en toutes lettres.`

**m5. Devis : le pire cas dépasse l'ordre de grandeur de GO-09 et GO-10 (1 à 3 USD).** Pire cas 3,24 à 3,30 USD, plafond 3,5 USD ;
l'attendu (0,87) et le pire cas de la seule minuterie (3,00) y tiennent. À dire, pour que Lazar accorde le plafond en le sachant.
- Couple 16 (devis) : ancien `Le pire cas tient sous le plafond proposé de 3,5 USD` → nouveau
  `Le pire cas des cas cumulés (3,24 à 3,30 USD) dépasse l'ordre de grandeur de 1 à 3 USD des deux GO ; l'attendu (0,87 USD) et le pire cas de la seule minuterie (3,00 USD) y tiennent ; le plafond de 3,5 USD est à faire accorder tel quel par Lazar. Le pire cas tient sous le plafond proposé de 3,5 USD`.

**m6. Devis : le trafic réseau n'est pas compté.** ≈ 5 Go descendants (image, paquets, copie du dépôt), 0,3 Go montants ; certaines
offres le facturent, la garde d'offre ne le borne pas. Ordre de grandeur sûr : au plus 0,10 USD à 20 USD le téraoctet.
- Couple 17 (devis) : ancien
  `- Poussée des sorties (≈ 0,22 Go estimés par l'addendum de relance, 4.4) et fin : **≈ 5 à 10 minutes**.` → nouveau le même texte
  suivi de `
- Trafic réseau (≈ 5 Go descendants, 0,3 Go montants) : facturé par certaines offres, non borné par la garde d'offre ; au plus 0,10 USD à 20 USD le téraoctet ; à relever sur l'offre retenue si l'outil donne son coût de trafic.`

**m7. Statut de la procédure.**
- Couple 18 (procédure) : ancien `**Statut** : écrite et répétée hors ligne, **non contre-lue**` → nouveau
  `**Statut** : écrite et répétée hors ligne, contre-lue au tour 1 (`contre-lecture-machine-jeu-idee-1-1-tour1-v1.md`), corrections de ce tour en v2`.

## Remarques facultatives (aucune exigée)

- **F1.** Épingler l'image par son condensé (`python:3.13.18-bookworm@sha256:…`, le lanceur accepte `@`) fermerait le cas d'une
  étiquette republiée ; le contrôle de `3.13.18` et des versions de paquets reste de toute façon l'arbitre.
- **F2.** Geste 8, branche « autre sortie » : `head -c 400 reponse-creation.json` peut afficher une clé si la forme de la réponse
  change ; préférer `python3 -I -c 'import json,sys; print(sorted(json.load(open(sys.argv[1]))))'` (noms seulement).
- **F3.** Le filtre de la recherche (`dph_total<=0.06`) est moins strict que la garde (prix total + stockage ≤ 0,06) : des offres
  seront refusées par la garde ; sans conséquence de sûreté, seulement un choix plus étroit (la garde compte le stockage deux fois,
  sens sûr).
- **F4.** La forme de `show instance` n'est pas rejouée ici ; un `None` à la place du prix au geste 9 serait une forme à relire,
  non un prix trop cher à punir de destruction : le dire en une ligne au geste 9.

## Points pour la mère

- **P1. Écart de la tâche à trancher : minuterie de 49 h 45 au lieu de 48 h.** Raison tenue (la borne de 48 h court depuis
  `depart.json`, après ≈ 1 h de mise en place et de contrôles) ; surcoût au pire 0,105 USD. Recommandation : accepter ; pour 48 h
  exactes, une v2 des constantes du lanceur et de l'amorce.
- **P2. Réseau pendant le jeu (m4).** Les poussées horaires et finales sont des appels réseau de la machine ; D7 (GO-10) est
  écrit « machine louée, dépense ». À faire dire par le feu, ou à faire confirmer par un mot de Lazar si la mère juge la lecture
  trop large. Les alternatives (pas de suivi poussé) enlèvent toute surveillance et ne sont pas recommandées.
- **P3. Défense par minuterie non vue en vrai.** L'API de destruction de la machine par elle-même n'a jamais été jouée par une
  amorce de ce type (B bis a été détruite par la session). La garde horaire de la session est donc la seule défense éprouvée :
  poser un rappel programmé de la mère à l'échéance (49 h 45 après l'impression), même si tout va bien.
- **P4. Permission.** `.claude/settings.json` n'autorise que la ligne de répétition de B bis ; la ligne de ce jeu a une forme neuve
  (sous-shell `( umask 077; … > fichier )`). Le feu déclare cet écart de forme (§ 2 point 5), mais le classifieur peut refuser :
  l'opérateur s'arrête alors (voulu). Prévoir le mot de Lazar sur la permission avant de lancer, comme pour B bis.
- **P5. Jeton.** `GH_TOKEN` (jeton d'écriture du dépôt) reste dans l'environnement de la machine louée, donc chez l'hôte, jusqu'à
  la destruction ; la procédure ne dit rien de son renouvellement après. À décider : renouveler `CONTROLE_IA_GITHUB_TOKEN_2`
  après la preuve de destruction (nœud de Lazar : compte).
- **P6. Avant le feu** : le commit du feu est à relire au moment de la remise (tête de `main` à 21:3xZ : `e395dd47…`) ; ligne de GO
  « calcul » à inscrire (périmètre « idée 1.1 », `3.5 USD`, échéance du M2) ; feu `R-<N>` à écrire ; dossier du jeu
  `docs/procedures/machine-jeu-idee-1-1-v1/` à commiter (non commité à 21:25Z) ; deux fichiers parasites `/s.txt` et
  `/commande-coupee.txt` à effacer par une personne (incident du développeur, non touchés ici). Contre-lecture du tour 2 sur la v2.

## Déclaration

- **Rôle** : contre-lecteur neuf (R2), lettre C ; aucune pièce du dossier modifiée ; aucun commit ; ce fichier est neuf.
- **Accès extérieurs** : lectures publiques sans donnée du programme (existence de l'étiquette de l'image sur Docker Hub ; des
  trois versions de paquets et de leurs roues sur l'index public) ; un `git ls-remote origin refs/heads/main` (lecture seule,
  fait aussi par la répétition) ; aucun appel au loueur, aucune machine, aucune dépense, aucune poussée.
- **Fichiers du dépôt lus en plus des pièces** : `registres/decisions.md` (R-2961, R-2968, R-2996 à R-3004, R-3010, R-3012, R-3014
  à R-3019, lignes seulement), `registres/go.md` (GO-2026-11-16-09 et -10, fin du registre), `.claude/hooks/garde_calcul.py`,
  `.claude/settings.json`, `prereg/` (lignes 603-662 du texte scellé), le brouillon 4 de l'addendum de relance et son contrôle ;
  `scripts/jouer_idee_1_1_v5.py` et `execution_idee_1_1_v5.py` par `git show` dans le bloc-notes. **Jamais ouvert** : rien sous
  `diag/`, `runs/`, `donnees/` (aucune liste de noms non plus), rien de `/home/user/jeu-idee-1-1-copie-v1`, rien de 7a, 7b, T0.6,
  T0.7, P3-bis, de B bis (hors ses scripts de lancement, la contre-lecture de sa création et les lignes demandées), du bras d'attaque.
  Aucune valeur de clé ; aucun `env`, `printenv`, `set`, `export -p` ; le texte « vastai create » n'a pas été tapé dans une commande
  (la ligne d'essai a été fabriquée dans un fichier par un programme, son outil remplacé par un exécutable factice).
- **Calcul** : léger (une répétition de ≈ 2 minutes ; analyses d'importations).
- **Dossiers de travail** (bloc-notes) : `…/scratchpad/rep-c1/` (ma répétition), `…/scratchpad/test-ligne/` (ligne d'essai),
  `…/scratchpad/cl1/` (extraits de deux fichiers du dépôt).
- **Incidents de ma main** : aucun (aucune commande refusée par le crochet, la garde de sûreté ou le classifieur ; aucun processus
  arrêté ; aucune écriture hors du bloc-notes et de ce fichier).
