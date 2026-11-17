# Procédure de la machine louée du crible (v) — v1

- **Objet** : jouer le crible (v) de l'organisme d'idéation (« n'appeler les proposeurs chers que si les bon marché ne rendent que
  des copies », regroupement, sans juge) sur une machine louée, jetable, sans ssh : 20 mondes MR-2 du secret du crible, quatre
  proposeurs de la configuration v12 du pilote, 80 appels, borne B_a = 900 s par appel, M files de mondes (M de la règle), la
  mesure une seule fois, la lecture gelée remise non ouverte à un sous-agent neuf.
- **Texte qui fera foi** : `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-v-version-foi-v2.md`
  (`2b99627dd378564dba816bc10593cdb0d06d77a3fdd4eb9e3cca022c76838715`, scellée comme pièce de travail ; jugée scellable au tour
  différentiel 2, `contre-lecture-crible-v-foi-tour2-v1.md`), **à sceller par `sceller_prereg` et à copier sous `prereg/`** ; ses
  sections « Plan d'analyse », « Liste d'arrêt » et « Devis » priment : en cas d'écart, le texte prime et l'écart est un nœud.
- **Modèles suivis (lus, non modifiés)** : la procédure v14 du pilote MR-2 sans ssh (`procedure-pilote-mr2-v74-machine-v14.md`,
  `20355627…`, branche `lot/compte-organisme-v1` : barrières, branches de sortie et d'entrée, balayage, états finaux) ; la
  procédure v6 de la machine du jeu de l'idée 1.1 (`procedure-machine-jeu-idee-1-1-v6.md` : garde jouée sur chaque offre, ligne
  compressée, contrôle de la ligne par programme, inventaires, prix relu, garde de dépense, destruction par l'identifiant lu,
  preuve d'absence par un témoin, reprise de la poussée).
- **Pièces de ce dossier** (`docs/procedures/crible-v-v1/`, chacune avec son compagnon `.sha256`) : `crible_v_commun_v1.py`,
  `lanceur_crible_v_v1.py`, `mesure_crible_v_v1.py`, `lire_crible_v_v1.py`, `partie_a_crible_v_v1.py` (code du crible) ;
  `amorce_crible_v_v1.sh`, `machine_crible_v_v1.py` (machine) ; `session_crible_v_v1.py` (outil de la session) ;
  `essais_crible_v_v1.py`, `banc_mutations_crible_v_v1.py`, `repetition_crible_v_v1.py` et leurs sorties gardées ;
  `devis-machine-crible-v-v1.md` ; `rapport-crible-v-v1.md` ; cette procédure. Empreintes : au rapport, § 1.
- **Statut** : écrite et répétée hors ligne ; **non contre-lue** ; **ne part pas au feu** sans : contre-lecture du code et de cette
  procédure par un sous-agent neuf d'un autre modèle (R2, étape 0 du texte), rendue `scellable` ; texte scellé sous `prereg/` ;
  addendum d'empreintes scellé ; fiche de lancement commitée ; lignes κv1 et κv2 inscrites ; D relevée et inscrite ; mot de Lazar sur
  le passage des clés à la machine du crible. Aucune machine, aucun appel au loueur, aucune dépense.

## 0. Notations

- `W=/home/user/controle-ia-travail` (dépôt de travail) ; `P=$W/docs/procedures/crible-v-v1` ; `ENV=/home/user/crible-v-envoi-v1`
  (dossier d'envoi **neuf**, hors de tout dépôt ; s'il existe : arrêt, R12) ; `V=/home/user/vastai-env/bin/vastai` ;
  `S="python3 -I -B $P/session_crible_v_v1.py"`.
- `CC` : commit du code (sur `main`, ancêtre de la tête distante) qui porte ce dossier, ses compagnons, la **fiche de lancement**
  `fiche-lancement-crible-v-v1.json` (chemins et empreintes du texte sous `prereg/` et de l'addendum, `duree_d_s` = D, `files` = M),
  le texte et l'addendum ; `CL` : commit de `lot/compte-organisme-v1` qui porte le paquet de l'arbre (`e3d83e47…`, tête 605e0f6).
- `BS=calcul/crible-v-v1-sortie-v1` (écrite par la machine seule) ; `BE=calcul/crible-v-v1-entree-v1` (écrite par la mère seule) ;
  absentes avant la création (contrôlé par l'outil, puis par la machine). Une seconde tentative prend des noms neufs (`-v2`, R12).
- `KV1`, `KV2` : identifiants des lignes « calcul » κv1 (104.39 USD, crédits de Claude) et κv2 (100.28 USD, hors crédits, dont la
  machine 3 USD), toutes deux citant GO-2026-11-15-06 ; le feu de création est `R-<N> KV2` (forme courte, leçon C4).
- **Interdits** : aucune valeur de clé affichée ni écrite ; jamais `env`, `printenv`, `set` sans argument, `export -p` ; aucune
  heure écrite à la main (`date -u`) ; arrêts par PID ou par identifiant (R10) ; jamais `git fetch` sans refspec ; aucun refus de
  permission, du crochet ou d'un classifieur rejoué ni contourné (nœud de la mère) ; aucune machine d'une autre tâche nommée.
- **États de la machine** (`etape=` de `etat.txt` sur `BS`, horodatés dans `etats-horodates.jsonl`) : `mise en place` →
  `pieces et arbre` → `secret` → `attente du feu 1 (phrase)` → `mondes` → `attente du feu 2 (mondes)` → `preparer` →
  `essai a blanc` → `attente du feu 3 (crible reel)` → `sonde reelle` → `jouer reel en cours` → `mesure` → `rapatriement` →
  finales : `fini`, `arret (A)`, `noeud, machine gardee`, `sortie inattendue`. Dans un état final, la machine ne calcule plus ;
  une poussée manquée est reprise toutes les 5 minutes jusqu'à l'échéance.
- **Échéance** : 17 h (61 200 s) après l'impression de la commande (budget de pire cas du texte) ; la minuterie de l'amorce
  demande la destruction de la machine par son identifiant à l'échéance (DELETE chaque minute, « stopped » à la cinquième) ; la
  session joue la destruction (§ 5) **cinq minutes après l'échéance au plus tard**, ou dès un état final, sans attendre aucun mot.
- **Ce que la machine pousse sur `BS`** (et rien d'autre) : `etat.txt`, `journal-machine.txt`, `etats-horodates.jsonl`, les
  journaux et codes des étapes, `mise-en-place.txt`, `secret-sha256.txt`, `cle-publique-phrase.pem` et son empreinte,
  `phrase-sha256.txt`, `engagement-mondes.json`, `engagement-certifiees.json`, `rapatrie-blanc/`, `rapatrie-sonde/`,
  `rapatrie-reel/` (pièces permises, aucun monde), `lancements*.jsonl`, `remis-au-sous-agent/sortie-lire-non-ouverte.txt` ; tout
  fichier où le balayage trouve le jeton, une clé, le secret ou la phrase est exclu et nommé.

## 1. Ce que fait la machine, dans l'ordre (amorce puis programme machine)

0. **Amorce** : arguments (commits, fiche, GO, branches de même version, échéance dans [maintenant + 16 h 50, + 17 h 05], forme
   des quatre valeurs passées par leur nom, identifiant de la machine) ; refus avant la minuterie : destruction demandée par la
   machine elle-même ; marque `amorce-lancee` (une relance du conteneur par le loueur ne refait rien : arrêt (A)) ; **minuterie
   armée avant toute passe** ; clone partiel (blobs à la demande) aux commits `CC` et `CL`, extraction limitée au dossier du crible et
   à `prereg/`, aucune poussée possible depuis ce dépôt ; programme machine à l'empreinte écrite dans l'amorce et à son compagnon ;
   `exec` (même PID).
1. **Mise en place** : `BS` absente (sinon rien n'est poussé, jamais), `BE` absente (sinon arrêt (A)) ; **première poussée** ;
   numpy 2.5.3 (pip, 900 s au plus) ; `(3, 13) 2.5.3` exigé.
2. **Pièces et arbre** : fiche à `FICHE_SHA256`, texte et addendum à leurs empreintes, D et M lisibles ; aucun `runs/`, `diag/`,
   `donnees/`, `registres/` extrait ; paquet à `e3d83e47…`, arbre 605e0f6 propre ; empreintes du code du crible présentes dans
   l'addendum.
3. **Secret, barrière 1** : secret tiré (`lanceur secret`), paire RSA de 4 096 bits pour la phrase (privée dans `prive/`) ;
   `secret-sha256.txt` et la clé publique poussés ; attente du feu 1 **une heure au plus** après le départ ; inscription relue sur
   `main` ; phrase déchiffrée, empreinte égale à celle du feu ; clé privée effacée (`shred`).
4. **Mondes, barrière 2** : `lanceur generer` (20 mondes, 8 tirages au plus chacun, étiquettes C8 gardées dans `CERTIFIEES.json`,
   privé) ; engagements poussés (H, HC, S1 à S20) ; attente du feu 2 (20 minutes) ; inscription de H, HC et des 20 empreintes
   relue sur `main`.
5. **Préparer, essai à blanc, barrière 3** : `lanceur preparer` (C-16, C-17, textes servis, gabarit `e77d3041…`) ; **essai à
   blanc à la valeur de M de la fiche** (`jouer --mode a_blanc --files M` : M mondes servis à la fois, 4 M relais factices ouverts,
   quatre empreintes de corps égales par monde, **une coupure simulée par file** : un appel qui dort au-delà d'une borne d'essai de
   60 s, coupé, compté « échec », journalisé), attendu 80 appels, M coupures, aucun arrêt ; rapatriement à blanc sans monde ;
   attente du feu 3 (20 minutes) : H, κv1, κv2, M et D égaux à la fiche, D et M inscrits sur `main`.
6. **Sonde neuve** (payante ; exigée, R-2992) : `lanceur sonde --mode reel` (quatre relais du crible aux ports de la file 0,
   consignes de la sonde de la v12, κv1 et κv2 lues au montant exact, registre des lancements de la sonde) ; code non nul : arrêt (A),
   **aucun appel du crible**.
7. **Crible réel** (une seule fois) : ports 8811 à 8814 et 8821 à 8824 libres, clés présentes ; `jouer --mode reel` avec toutes
   les pièces exigées (texte, addendum, relevé de la sonde, κv1 et κv2, mondes et étiquettes, registre des lancements, échéance,
   D) : le lanceur rejoue la **garde de départ** (arrêt sans appel si moins de 6 000 + 3 D + ⌈20/M⌉ × 900 s restent) et la règle
   de M ; état poussé toutes les 15 minutes ; **feu d'arrêt lu chaque minute** : lanceur arrêté par son PID, puis ses relais par
   leurs PID (`pids-relais.json`), arrêt (A). Code 0 → mesure ; code 3 par la seule règle d'abandon d'un fournisseur → mesure
   (lecture « non concluant ») ; tout autre code → arrêt (A), ni mesure ni lecture.
8. **Mesure une seule fois** (`lanceur mesurer` : programme `mesure_crible_v_v1.py` à l'empreinte du manifeste ; sortie
   principale scellée, puis le rejeu sous archive fictive vers un second fichier scellé) ; code non nul : « noeud, machine gardee »
   (exception de la mesure : rien n'est lu). **Lecture** (`lanceur lire`) écrite et scellée sur la machine, sa sortie standard
   remise **non ouverte** (`remis-au-sous-agent/`).
9. **Rapatriement** (pièces permises seulement, aucun monde, aucun texte servi, aucune graine, aucun identifiant de fournisseur),
   état `fini`, poussée finale (reprise toutes les 5 minutes si elle manque) ; attente de la destruction.

## 2. Ce que fait la mère avant de remettre la suite à l'opérateur (aucun point ne manque)

1. Texte qui fera foi scellé (`sceller_prereg`) et copié sous `prereg/` ; son empreinte est la racine des graines.
2. **Contre-lecture du code** (étape 0 du texte : sous-agent neuf d'un autre modèle) et de cette procédure, rendue `scellable` ;
   **addendum d'empreintes** scellé sous `prereg/` (une ligne « empreinte  chemin » par fichier du code du crible, programme machine
   compris ; graines des essais et des mutations listées).
3. **Quatre durées relevées** sur les états nommés du journal de la machine du pilote (texte, « Devis ») ; D inscrite ; M par la
   règle (`m_de_la_regle`) ; « non lançable » au-delà de 15 400 s : nœud de la mère.
4. **Fiche de lancement** commitée sur `main` (`CC`) : `{"version": "fiche-lancement-crible-v-v1", "texte": {chemin, sha256},
   "addendum": {chemin, sha256}, "duree_d_s": D, "files": M}`.
5. **Lignes « calcul » κv1 et κv2** inscrites par la mère sur ce devis (montants 104.39 et 100.28 USD, mots du périmètre
   « crible (v) », « crédits de Claude » ; « crible », « hors crédits »), citant **GO-2026-11-15-06** ; cumul des lignes sous
   l'enveloppe ≤ 1 275 USD (l'outil le contrôle ; au-delà : nœud de Lazar).
6. **Mot de Lazar sur le passage des trois clés et du jeton des machines à la machine du crible** (GO-2026-11-15-04 portait sur le
   pilote) et sur l'exposition qui en suit (configuration de l'instance chez le loueur jusqu'à la destruction ; environnement de la
   minuterie) ; remplacement des clés proposé après le crible.
7. **Feu écrit** : ligne `R-<N>` de `registres/decisions.md` qui cite KV1, KV2, `CC` et l'étiquette `crible-v-v1` ; le texte passé
   aux commandes est la forme courte `R-<N> KV2`.
8. Recharge du crédit du loueur active ; préavis d'une ligne à Lazar au moment de l'impression (geste 6) ; **mot de Lazar daté de
   moins de dix minutes disant qu'il est présent pour la demi-heure qui suit** (la phrase est demandée dans l'heure).

## 3. Gestes exacts de l'opérateur

Chaque geste est autonome (aucun dossier courant ni variable d'un appel à l'autre) ; tout code ou toute sortie autre que l'attendu :
**arrêt**, compte rendu à la mère, aucun rejeu. Constantes à redonner : `W`, `P`, `ENV`, `V`, `S`, `CC`, `CL`, `KV1`, `KV2`,
`FEU="R-<N> KV2"`, `BS`, `BE`.

1. **Pièces et feu** : `cd "$P" && for c in *.sha256; do sha256sum -c "$c"; done` → tous `OK` ; `git -C $W fetch origin
   +refs/heads/main:refs/remotes/origin/main +refs/heads/lot/compte-organisme-v1:refs/remotes/origin/lot/compte-organisme-v1`
   (refspecs) ; `$S creation $W "$FEU" $CC` → `CRIBLEV CREATION PERMISE {…}` (κv1, κv2, enveloppe inscrite).
2. **Dossier d'envoi neuf** : `mkdir /home/user/crible-v-envoi-v1; echo "code $?"` → `code 0`.
3. **Inventaire d'avant** : `( umask 077; "$V" show instances --raw < /dev/null ) | $S inventaire > "$ENV/ids-avant.txt"` → une
   ligne `<id> <étiquette>` par machine ; aucune `crible-v-v1` ; au moins un témoin.
4. **Recherche, offre par la garde** : `( umask 077; "$V" search offers 'rentable=true reliability>=0.98 cpu_cores_effective>=4
   cpu_ram>=8 disk_space>=20 inet_down>=100 dph_total<=0.15' -o 'dph_total' --storage 20 --raw < /dev/null > "$ENV/recherche.json" )` ;
   `$S offre-depuis-recherche "$ENV/recherche.json" "$ENV/offre.json"` → une ligne par offre, puis `CRIBLEV OFFRE ECRITE …`
   (prix garde ≤ 0,15 USD/h, prix du réseau imprimés et consignés).
5. **Préavis à Lazar** (mère), puis **mot de Lazar daté de moins de dix minutes** (§ 2, point 8).
6. **Commande, sortie écrite** : `ECH=$(( $(date +%s) + 61200 )); $S commande $W "$ENV/offre.json" $CC $CL $ECH "$FEU" "$ENV" $BS $BE >
   "$ENV/commande-imprimee.txt"; echo "code $?"` → `code 0`, **deux** lignes (en-tête `CRIBLEV COMMANDE`, puis la ligne). L'outil a
   contrôlé : offre, échéance, feu, κv1 et κv2, enveloppe, commits (code et compagnons à `CC`, paquet à `CL`), fiche, branches
   absentes, amorce en essai local. Plus de 10 minutes avant le geste 8 : refaire ce geste dans un fichier neuf.
7. **Contrôle par programme** : `$S controle-ligne "$ENV/commande-imprimee.txt"` → `CRIBLEV LIGNE CONFORME : amorce décodée égale à
   l'octet (…)`, puis la ligne, base64 masqué : préfixe `GO_ID=KV2`, image `python:3.13-bookworm`, disque 20, étiquette
   `crible-v-v1`, variables `COMMIT_CODE`, `COMMIT_LOT`, `ECHEANCE_UTC_S`, `FICHE_SHA256`, `GO_KV1`, `GO_KV2`, `BR_SORTIE`,
   `BR_ENTREE`, puis **`$GH_TOKEN`, `$RR_ANTHROPIC_API_KEY_RIGAUD`, `$GEMINI_API_KEY`, `$OPENAI_API_KEY` en lettres** (jamais une
   valeur), sortie dans `"$ENV/reponse-creation.json"`. Lecture de la ligne en morceaux si elle est longue, copie dans un fichier par
   un appel à part, `cmp` avec la ligne 2 → `cmp 0`.
8. **Création, un seul appel, une seule fois** : `test -n "${CONTROLE_IA_GITHUB_TOKEN_2:-}" && export GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN_2"
   &&` suivi de la ligne **identique à l'octet**. Attendu : `CRIBLEV CREATION success True new_contract <id> cles [...]` (noms
   seulement). Autre sortie : ne pas rejouer ; geste 9 (une machine a pu être créée).
9. **Inventaire d'après, identifiant, prix relu** : nouvel inventaire, `diff` avec `ids-avant.txt` : exactement **une** ligne ajoutée
   `<id> crible-v-v1`, égale au `new_contract` ; `grep ' crible-v-v1$' … | cut -d' ' -f1 > "$ENV/id-machine.txt"` ; prix relu par
   `show instance` (champ `dph_total`) puis `$S prix-relu <prix>` → `CRIBLEV PRIX RELU ACCEPTE` ; refus : destruction aussitôt
   (§ 5). **Rappel posé à l'échéance plus cinq minutes** dès la création.
10. **Surveillance** : `$S etat $W $BS` (état et fin du journal) toutes les quelques minutes ; aucune branche 20 minutes après la
    création : lire les journaux du loueur (lecture seule) ; 30 minutes : destruction (§ 5). Un état qui ne bouge plus 40 minutes
    hors de `jouer` : nœud de la mère (ne pas détruire avant l'échéance sans son mot).
11. **Chaque heure, garde de dépense** : `$S depense $W $KV2 <CUMUL> <PRIX>` (point décimal ; cumul = heures × prix relu) →
    `CRIBLEV DEPENSE {…}` ; refus : destruction.

## 4. Feux de la mère

| feu | quand (état poussé) | commande | délai de la machine |
|---|---|---|---|
| 1, phrase | `attente du feu 1 (phrase)`, après l'inscription sur `main` de l'empreinte du secret (`secret-sha256.txt` de `BS`), puis la phrase **tapée par Lazar dans la session qui lance**, écrite par un document au délimiteur entre guillemets dans `$ENV/phrase.txt` (`( umask 077; cat > … ) <<'PHRASE'`) | `$S feu-phrase $W $BS $BE "$ENV/phrase.txt" COMMIT CHEMIN` (phrase chiffrée par la clé publique RSA 4 096 de la machine, fichier effacé par `shred` que la poussée réussisse ou non) ; la mère inscrit ensuite l'empreinte du fichier de la phrase | 1 h après le départ |
| 2, mondes | `attente du feu 2 (mondes)`, après l'inscription de H, HC et S1 à S20 (`engagement-mondes.json`, `engagement-certifiees.json` de `BS`) | `$S feu-mondes $W $BS $BE COMMIT CHEMIN` | 20 min |
| 3, crible réel | `attente du feu 3 (crible reel)`, essai à blanc lu (`$S recuperer $W $BS "$ENV/retour-blanc"`), après l'inscription des lignes « D = … s » et « M = … » | `$S feu-reel $W $BS $BE $KV1 $KV2 D M COMMIT CHEMIN` | 20 min |
| arrêt | toute étape (lu à chaque attente et chaque minute pendant `jouer`) | `$S feu-arret $W $BE "CAUSE"` (lettres sans accent, chiffres, « , . : ; ( ) _ - », 100 caractères au plus) | aussitôt |

Un feu refusé par la machine est journalisé ; elle attend jusqu'à son délai. Une poussée sur `BE` refusée : nœud, sans contournement.

## 5. Fin, destruction par l'identifiant, preuve d'absence

1. **Fin** : `fini`, `arret (A)`, `sortie inattendue` → `$S recuperer $W $BS "$ENV/retour"` (dossier neuf), puis destruction
   **aussitôt** ; `noeud, machine gardee` → au mot de la mère, au plus tard à l'échéance plus cinq minutes. Les sorties du crible
   (`rapatrie-reel/`) sont versées sur une **branche de travail, jamais sur `main`** (R-2731) ; `BS` n'est jamais fusionnée dans
   `main` ; `remis-au-sous-agent/` n'est pas ouvert par la session.
2. **Destruction** : `$S detruire "$(cat "$ENV/id-machine.txt")" "$ENV" $KV2` → imprime `GO_ID=KV2 … destroy instance <id> -y` ;
   la jouer telle quelle ; **le code de sortie n'est jamais jugé**.
3. **Preuve** (au moins 30 secondes après) : liste relue `( umask 077; "$V" show instances --raw < /dev/null > <fichier privé> )`
   puis `$S absence <id> <TEMOIN> <fichier>` → `CRIBLEV DESTRUCTION PROUVEE …` (identifiant absent, témoin présent dans
   `ids-avant.txt` et dans la liste) ; « toujours listée » : refaire 2 puis 3 ; « témoin absent » : autre témoin ou nœud.
4. **Nettoyage** : effacer par leurs chemins exacts la liste brute et `"$ENV/reponse-creation.json"` ; lignes aux registres
   (`arrets.md`, `depenses.md` : relais depuis le relevé rapproché des journaux, machine prix × durée, sonde ; montants facturés :
   console de Lazar, R-2803 ; `decisions.md`) ; lecture par un sous-agent neuf (R13), audit de symétrie (R4) écrit avant le
   prononcé, rapport à la mère ; **aucune adoption**.

## 6. Ce que la procédure ne fait pas

- Elle ne lit aucun résultat dans la session : la lecture est écrite sur la machine et remise non ouverte.
- Elle n'emploie aucune reprise d'appel : un appel au-delà de B_a est coupé et compté « échec » ; une panne de relais abandonne le
  fournisseur (règle du pilote) ; aucune bascule.
- Elle ne relance pas le crible réel : une seconde tentative demande des branches et un dossier d'envoi neufs, et le mot de la mère.
- Elle ne garantit pas l'égalité au bit près sur un autre processeur ; `mise-en-place.txt` garde les versions.
- La sonde neuve ne passe que par les ports de la file 0 ; à M = 2, les ports de la file 1 ne sont éprouvés que par l'essai à blanc
  (réserve, rapport § 4).
