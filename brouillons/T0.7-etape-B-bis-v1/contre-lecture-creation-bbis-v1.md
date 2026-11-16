# Contre-lecture de la création de la machine de la course de B bis, avant le feu (v1)

- **Auteur** : contre-lecteur neuf (R2), modèle C. Il n'a écrit aucun fichier de l'étape B bis.
- **Date (UTC, `date -u`)** : 2026-11-16, de 13:43:01 à 13:50 environ.
- **Lieu** : arbre de travail `/home/user/controle-ia-travail/.claude/worktrees/agent-a4f221610ce6d5a67`, branche
  `prep/t07bbis-code-v1`, tête locale = tête distante `0f948b0e0593e0a639e1ea3cba903c6cceaa50a8` ; commit de la course à citer
  `31fa8ac6041faf76b66282e0346750b9aefd4790` (ancêtre de la tête : code 0). Rien modifié, rien committé, aucun appel au loueur.
- **Programmes et sorties** (dossier neuf du bloc-notes, chemin complet :
  `/tmp/claude-0/-home-user-controle-ia-travail/78897fa0-2926-5bf2-a108-3e893bc2db62/scratchpad/contre-lecture-creation-bbis-v1-C/`) :
  recherche fabriquée `recherche-fabriquee.json` (deux offres inventées, identifiants 99999991 et 99999992), `offre.json`,
  `sortie-commande.txt` (sortie de `commande`, 32 733 octets), `analyse.py`, listes fabriquées `l-*.json`.

## Verdict : `corrections`

Aucun obstacle de fond : le lanceur imprime exactement la forme du plan § 4.1 (point 2), aucune valeur de clé ne s'affiche
(point 3), la garde de création, la garde d'offre, la garde de destruction et la garde de dépense se comportent comme le plan le dit
(joués sur offre et listes fabriquées). Mais **le plan § 4.1 n'est pas une suite de gestes que l'opérateur peut taper tel quel** :
sept points sont à corriger avant de la lui remettre (liste exacte ci-dessous), et **une condition de la mère n'est pas remplie**
(crédit du loueur). La suite corrigée est en tête de la partie « Gestes exacts ».

### Corrections exactes (C1 à C8)

- **C1. Chaque geste doit être autonome.** L'opérateur est un sous-agent : le dossier courant est remis à zéro et aucune variable
  de shell ne survit d'un appel de l'outil Bash à l'autre. Le bloc du plan § 4.1 est écrit comme un seul shell (`$D`, `$V`,
  `$COMMIT`, `$RUNB`, `$ECH`, `OFFRE_ID`, `PYTHON_BBIS`, `VASTAI_BBIS`, `cd`). Chaque appel redonne ses constantes et fait son `cd`
  (modèle ci-dessous). Sans cela, l'échec est sûr (le lanceur refuse un identifiant ou une échéance vide ; `vastai` est hors du
  chemin de la session, relevé à 13:44Z : « vastai hors PATH »), mais la suite n'avance pas.
- **C2. Trois gestes que le plan ne décrit que par un commentaire ou un nom** : l'inventaire d'avant (« identifiants et étiquettes
  seulement » : aucune commande), le choix de `OFFRE_ID` (aucune règle ni commande), l'inventaire d'après et la lecture de
  l'identifiant. Commandes fournies ci-dessous (filtre par programme, aucune liste brute affichée ni gardée).
- **C3. La ligne imprimée dépasse l'affichage de l'outil.** `commande` rend 32 733 octets (la ligne 2 : 32 629 caractères, dont
  32 072 de base64) ; l'outil Bash coupe au-delà d'environ 30 Ko (relevé sur cette session : sorties de 32 Ko renvoyées en
  « Output too large », début et fin seulement). L'opérateur ne peut pas copier la ligne depuis l'affichage direct. Remède sans
  recomposition : écrire la sortie dans le dossier d'envoi, puis l'afficher **en trois morceaux de moins de 11 000 caractères**
  (`cut -c`), et vérifier par programme la forme et l'empreinte de l'amorce décodée (gestes 8 et 9). **Réserve de fond (R-1)** :
  taper 32 Ko de base64 sans faute est le risque réel du geste ; une faute fait échouer l'amorce sans que la minuterie soit armée
  (l'instance vivrait, facturée, jusqu'à ce que la session la détruise). Jouer la ligne par `bash fichier` ou `eval` éviterait la
  copie mais **contournerait** le crochet de garde (il ne verrait pas le texte du lancement) et la visibilité du classifieur :
  c'est le geste que R-2950 condamne (« aucune chaîne coupée, aucun script qui la recompose ») ; **non permis sans mot écrit de
  Lazar**. Le plan doit dire que l'opérateur copie, et que la mère prend le risque ; surveillance à prévoir (geste 12).
- **C4. Le texte du feu passé aux commandes doit être court et ne porter qu'un numéro de GO.** `exiger_creation` n'exige que la
  sous-chaîne `GO-2026-11-14-09` dans l'argument ; le crochet de garde, lui, lit tout le texte de la commande : s'il y trouve
  `vastai` suivi de `create`, `launch` ou `start`, **chaque** numéro de la forme `GO-AAAA-MM-JJ-NN` du texte doit être un GO de type
  « calcul », accordé par Lazar, en validité. Passer en argument la ligne R- entière (qui cite sans doute GO-2026-11-16-06, de type
  « décision », et peut citer `vastai create`) ferait **bloquer** la commande. Forme retenue : `"R-<N> GO-2026-11-14-09"`. Le crochet
  en a fait la preuve sur ma propre commande (incident 1 de la déclaration).
- **C5. `GH_TOKEN` existe déjà dans l'environnement de la session** (présent, relevé par `test -n` à 13:44Z) : c'est le jeton de
  session, celui que la mère a transmis à tort le 14 novembre (R-2829). L'`export GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN_2"` doit donc
  être **inconditionnel et dans le même appel que le lancement**, précédé de la vérification que la source est non vide
  (`&&`) ; une affectation en tête de ligne ne suffit pas (`$GH_TOKEN` se développe avant elle, R-2829).
- **C6. Le crédit du loueur n'est pas au niveau exigé** : R-2985 relève **7,76 USD à 13:41Z**, la condition (R-2975 point 7 ;
  GO-2026-11-16-06) est **20 USD au moins** ; rien ne la contrôle mécaniquement. Le geste 0 est un arrêt tant qu'une ligne R- n'a pas
  consigné le crédit atteint. Prix : le lanceur ne borne pas le prix horaire (seulement le stockage, 0,08 USD/h) ; à crédit de
  20 USD, l'échéance de 13 heures n'est couverte que jusqu'à 1,5 USD/h : borne à écrire dans le feu (recommandation : refuser une
  offre à plus de 1,5 USD/h).
- **C7. Témoin de la preuve de destruction** : le plan dit « 58936096 s'il est listé ; jamais 60480302, 60599797, 60670453 » et ne dit
  rien de 58936099 ni de 58936100. Lecture proposée : repli sur 58936099 puis 58936100 s'ils sont dans l'inventaire d'avant et dans
  celui du moment ; à confirmer par la mère. Et `detruire` **n'a pas** 60918148 dans sa liste de refus (joué : `detruire 60918148`
  imprime la commande) ; la machine est détruite, sans objet, mais l'opérateur lit l'identifiant dans un fichier, jamais ne le tape.
- **C8. Liste brute des instances laissée dans `/tmp`** : `verifier-destruction` sans fichier écrit la liste brute (qui porte
  l'environnement d'autres instances, dont des jetons : R-2829) dans `mktemp -d` et imprime son chemin. À effacer, par ce chemin
  exact, après la preuve (le pilote le faisait, section 11, point 4, R-2981). Le plan ne le dit pas.

## 1. Pièces et gardes relues

- `creation` : exige `SCELLEMENT-BBIS`, `CODE-BBIS`, `GO-BBIS` au registre propre (présentes : lignes de 2026-11-14T12:30:30Z,
  2026-11-16T12:57:51Z, 2026-11-16T12:58:51Z), aucune clé de B bis dans le registre partagé, `GO-2026-11-14-09` contenu dans le
  feu (sous-chaîne), au plus une relance, échéance de la ligne de GO 2026-11-22, relance interdite après le 21 à 12:00Z.
  Joué : feu sans numéro → code 2 « feu écrit … absent » ; feu « R-TEST GO-2026-11-14-09 » → code 0, `BBIS CREATION PERMISE`.
- `offre-depuis-recherche` : joué sur ma recherche fabriquée : offre à CUDA 12.8 → code 2 ; offre à CUDA 13.2 → code 0, fichier
  d'offre écrit (mode `x` : jamais réécrit), stockage calculé 0,0308 USD/h. **Le fichier n'est écrit que si l'offre est acceptée.**
- `commande` : joué (voir point 2). Il rejoue l'offre, l'amorce en essai local (dossier jetable créé puis supprimé : il faut un
  `TMPDIR` accessible ; vide après), la garde de création, l'ancêtre (`CODE-BBIS` → commit demandé) et l'absence de la branche de
  sortie `donnees/t07-etape-b-bis-v1` (`git ls-remote`, lecture seule ; code 2 relevé à 13:47Z, donc absente).
- Branche de la course à distance : `0f948b0e…`, descendante de `31fa8ac6…` ; branche de 7b `calcul/t06-confirmation-7b-v1` présente
  (`55c3e3eb…`) ; branche de sortie absente.

## 2. Le lanceur imprime-t-il la forme du plan § 4.1 ? Oui

Joué dans un dossier neuf du bloc-notes, avec l'offre fabriquée 99999991 et le feu « R-TEST GO-2026-11-14-09 » (aucun appel au
loueur ; `TMPDIR` pointé sur le bloc-notes ; arbre de travail propre après, tête inchangée). Sortie : deux lignes plus une fin de
ligne, aucun retour chariot.

- Ligne 1 : `BBIS COMMANDE (à jouer par la mère, après le feu écrit ; empreinte de l'amorce 18e2f2052efdca0d) :`.
- Ligne 2 (base64 remplacé par `<B64>`) : `GO_ID=GO-2026-11-14-09 vastai create instance <OFFRE_ID> --raw --image python:3.11-bookworm --disk 150
  --cancel-unavail --label bbis-t07-v1 --env "-e COMMIT=31fa8ac6041faf76b66282e0346750b9aefd4790 -e BRANCHE_CODE=prep/t07bbis-code-v1
  -e RUN_7B=20261111-151701-t06-reel -e BRANCHE_7B=calcul/t06-confirmation-7b-v1 -e RUN_BBIS=<AAAAMMJJ-HHMMSS>-bbis-t07-v1
  -e ECHEANCE_UTC_S=<ECH> -e GO_ID=GO-2026-11-14-09 -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$GH_TOKEN" --entrypoint bash --args -c "echo <B64> |
  base64 -d > /root/amorce_bbis_v3.sh && bash /root/amorce_bbis_v3.sh"`.
- **Conforme au plan** : étiquette `bbis-t07-v1` ; image `python:3.11-bookworm` ; disque 150 ; échéance = argument (13 heures
  après l'impression si l'opérateur calcule `date +%s` + 13 × 3600 ; la RUN_BBIS jouée : `20261116-134512-bbis-t07-v1`, échéance
  1794883512 = 13 heures plus tard) ; relances 0 (argument de la garde, non imprimé, à bon droit) ; `GO_ID=GO-2026-11-14-09` en
  préfixe et en variable ; sept variables de la configuration plus les deux clés par leur nom. Le base64 décodé est **égal à
  l'octet** à `scripts/amorce_bbis_v3.sh` (`18e2f2052efdca0d…`, égal à l'empreinte annoncée sur la ligne 1).
- **Écart permis, et un seul à la lettre** : `vastai` nu au lieu de `/home/user/vastai-env/bin/vastai`. Les variables `PYTHON_BBIS`
  (interprète du dépôt) et `VASTAI_BBIS` (outil du loueur) ne figurent pas dans la ligne : elles servent aux sous-commandes du
  lanceur (`VASTAI_BBIS` seulement à `verifier-destruction`).
- **Le lanceur n'a pas de mode « ECHO »** : l'essai se fait avec une offre fabriquée (fait). Aucun appel au loueur dans `commande`
  (seul `git ls-remote` vers le dépôt de travail).
- **Crochet de garde** : les expressions rationnelles de l'arrêt par motif (R10) ne peuvent pas se déclencher sur la ligne (leurs
  motifs exigent une espace, `;`, `&`, `|` ou `(` avant `pkill` / `killall`, ou la suite `$(` avant `pgrep` ; le base64 n'a aucun de ces
  caractères et la ligne n'a pas de `$(`) : lecture du code, non jouée (voir incident 1).

## 3. Les clés : `GH_TOKEN` et `HF_TOKEN` sans aucune valeur affichée

- La ligne imprimée porte **`$HF_TOKEN` et `$GH_TOKEN` en lettres** (jamais une valeur) ; vérifié sur la sortie : aucun motif de clé
  (`ghp_`, `github_pat_`, `hf_` suivi de 20 caractères) dans les 32 733 octets. Elles se développent dans le shell de l'opérateur au
  moment du jeu de la ligne (guillemets doubles).
- `HF_TOKEN` : présence par `test -n "${HF_TOKEN:-}"` (présente à 13:44Z) ; aucune affectation, aucun affichage.
- `GH_TOKEN` : `export GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN_2"` (source présente à 13:44Z, par `test -n`, sans valeur), dans **le même
  appel** que la ligne (C5). La ligne de commande de l'outil, le journal du crochet et la sortie de la création ne portent que des
  noms de variables ; la sortie de `vastai create … --raw` est un petit objet JSON (`success`, `new_contract`) qui ne répète pas
  l'environnement (non joué, fondé sur les passes antérieures citées au plan § 4.2).
- **Ce que la ligne ne dit pas** : l'amorce garde `HF_TOKEN` et `GH_TOKEN` dans la configuration de la machine jusqu'à sa
  destruction (R-2975 point 5) ; le préavis à Lazar doit le dire.

## 4. Texte exact du feu écrit de la mère (ligne R- de `registres/decisions.md`)

Pour que `exiger_creation` et le crochet l'acceptent, **la ligne R- doit exister avant les gestes 6 à 9** (le crochet et la garde ne
vérifient pas son existence ; c'est le geste 1 de l'opérateur) et porter, en toutes lettres :

1. la chaîne exacte `GO-2026-11-14-09` (type « calcul », accordée par Lazar, 2026-11-14 → 2026-11-22, unique, non révoquée : la
   seule révocation du registre vise d'autres GO) ;
2. le feu lui-même : « feu pour la création de la machine de la course de B bis », le commit `31fa8ac6041faf76b66282e0346750b9aefd4790`
   sur `prep/t07bbis-code-v1`, l'étiquette `bbis-t07-v1`, une A100 SXM4 80 Go, hôte à CUDA 13.0 au moins, **prix horaire maximal
   accepté** (C6), échéance de 13 heures, 0 relance ;
3. **l'écart de forme permis, seul** : « `vastai` est joué par son chemin complet `/home/user/vastai-env/bin/vastai` ; tout le reste de
   la ligne imprimée par `scripts/lancer_bbis_v3.sh commande`, à l'octet » ; et, pour ne pas être un écart non dit, le préfixe de
   clés (`export GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN_2"`, vérifications de présence par `test -n`), qui est déjà celui de R-2829 ;
4. que l'opérateur est du modèle A (GO-2026-11-16-06), arrêt au premier refus d'une permission, du crochet ou du classifieur ;
5. le crédit du loueur atteint (≥ 20 USD, montant et heure) ; le préavis d'une ligne à Lazar fait ; le témoin de destruction
   permis (C7) ; que le texte passé au lanceur est la forme courte `R-<N> GO-2026-11-14-09` (C4).

La ligne peut citer d'autres numéros de GO (elle n'est pas passée en entier à une commande qui contient le lancement), mais **ne
doit jamais être copiée en argument d'une commande qui contient le lancement** (C4).

**Ce que le crochet inspecte, et exige** : toute commande dont le texte contient `vastai` + espace + `create`, `launch` ou `start`
(le geste 11 ; mais aussi, par erreur, un `grep`, un `echo` ou un fichier de commande qui cite ces mots) doit contenir au moins un
numéro `GO-AAAA-MM-JJ-NN`, et **tous** ceux du texte doivent être, dans `registres/go.md` de la racine du crochet
(`/home/user/controle-ia-travail`) : présents ; de type exactement « calcul » ; « Lazar » ; la date du jour entre l'accord et
l'échéance ; non cités par une ligne de type « révocation ». Les autres gestes (`search offers`, `show instances`, `destroy instance`,
toutes les sous-commandes du lanceur sauf si leur texte cite le lancement) ne sont pas inspectés pour le GO ; tous le sont pour l'arrêt
par motif (R10) : aucun `pkill`, `killall`, `kill $(pgrep …)`.

## 5. Preuve de destruction (plan § 5), jouée sur listes fabriquées

- **Refus de détruire** (`detruire`, `absence`) : 58936096, 58936099, 58936100, 60480302, 60599797, 60670453 (joué : 58936096 →
  code 2 « instance d'une autre session ») ; non numérique → code 2. Aucun refus pour 60918148 (C7).
- **Témoin à prendre** : dans `ids-avant.txt` **et** dans l'inventaire du moment, différent de l'identifiant de la course, jamais
  60480302, 60599797, 60670453 ; ordre : 58936096, puis 58936099, puis 58936100 (C7).
- **Refus à prévoir (code 2, jamais un code de sortie de la destruction)** : joué : « instance … toujours dans la liste » (refaire la
  destruction puis la preuve) ; « témoin … absent de la liste » (autre témoin, ou nœud) ; « identifiants illisibles » ; échec de lecture de
  la liste (code ≠ 0 de `show instances`, dont 127 si `VASTAI_BBIS` n'est pas posé dans l'appel). Accepté : code 0,
  `BBIS DESTRUCTION PROUVEE <ID> : absente de la liste, témoin <T> présent, <N> instance(s) listée(s)`.
- **Relecture de la mère** : identifiant absent, **toutes** les autres instances de `ids-avant.txt` encore présentes (N = nombre
  d'instances de l'inventaire d'avant).

## 6. Garde de dépense pendant la course

`bash scripts/lancer_bbis_v3.sh depense CUMUL PRIX` : joué : `0.749 1.2` → code 0 (`projete` 1,049) ; `39.0 1.2` → code 0 (39,3 < 39,5) ;
`0,749 1,2` (virgule) → code 2 « could not convert string to float » + commande de destruction imprimée : **point décimal obligatoire**,
une virgule arrête à tort. Refus (code 2, cumul + 0,25 h × prix ≥ 39,5) → destruction par l'identifiant (geste 15), jamais autre
chose. CUMUL = 0,749 (répétitions, R-2957) + heures écoulées × prix relu de l'instance + disque (formule du plan § 4.4 ; elle peut
compter deux fois le stockage si le prix relu l'inclut déjà : sens sûr). Cadence : au moins chaque heure. **Remarque** : avec la
minuterie de 13 heures (≈ 15,5 USD à 1,2 USD/h) la coupure de 39,5 USD ne peut pas être atteinte par cette course seule ; la
garde ne protège réellement que contre une machine qui survivrait à sa minuterie ou une relance ; le crédit (C6) est la contrainte
qui compte.

## Gestes exacts (suite corrigée, prête à remettre à l'opérateur)

Constantes à redonner **en tête de chaque appel** (C1) ; chaque appel commence par `cd "$W"` quand il lance le lanceur :
`W=/home/user/controle-ia-travail/.claude/worktrees/agent-a4f221610ce6d5a67 ; D=/home/user/bbis-course-envoi-v1 ;
V=/home/user/vastai-env/bin/vastai ; PY=/home/user/controle-ia-travail/.venv/bin/python ; C=31fa8ac6041faf76b66282e0346750b9aefd4790`.
Le filtre d'inventaire `F` est : `python3 -I -c 'import json,sys; d=json.load(sys.stdin); l=d.get("instances") if isinstance(d,dict) else d;
assert isinstance(l,list) and all(isinstance(i,dict) and "id" in i for i in l); [print(i["id"], i.get("label")) for i in sorted(l,
key=lambda i: int(i["id"]))]'` (il n'imprime que l'identifiant et l'étiquette). Règle générale : tout code ou toute sortie autre que
l'attendu = **arrêt**, compte rendu à la mère, aucun rejeu, aucun contournement.

0. **Conditions (la mère, avant de remettre)** : ligne R- du feu inscrite (texte du point 4) ; crédit du loueur ≥ 20 USD consigné
   (C6) ; préavis à Lazar ; prix horaire maximal fixé. Sinon : ne pas commencer.
1. **Le feu existe, et l'état de départ** (aucune clé, rien chez le loueur) :
   `cd "$W" && N=<N> && grep -c "^| R-$N |" /home/user/controle-ia-travail/registres/decisions.md && grep "^| R-$N |" /home/user/controle-ia-travail/registres/decisions.md | grep -c -e 'GO-2026-11-14-09' -e '/home/user/vastai-env/bin/vastai'`
   puis `git --no-optional-locks rev-parse HEAD ; git --no-optional-locks ls-remote origin refs/heads/prep/t07bbis-code-v1 ;
   git --no-optional-locks merge-base --is-ancestor 31fa8ac6041faf76b66282e0346750b9aefd4790 HEAD ; echo "ancetre $?" ;
   git --no-optional-locks ls-remote --exit-code origin refs/heads/donnees/t07-etape-b-bis-v1 > /dev/null 2>&1 ; echo "sortie $?"`.
   Attendu : `1` (la ligne R-<N> existe, une fois), puis `2` (elle porte le numéro de GO et le chemin complet de l'outil) ; HEAD égal à la tête distante
   (`0f948b0e…` à 13:47Z ; toute autre tête : arrêt, la mère ne pousse plus de code sur cette branche) ; `ancetre 0` ; `sortie 2`.
   Arrêt si autrement (feu absent ; branche de sortie présente : nouveau nom exigé, nœud).
2. **Dossier d'envoi neuf** : `D=/home/user/bbis-course-envoi-v1 ; mkdir "$D" ; echo "code $?"` → `code 0`. S'il existe : arrêt (R12,
   jamais le réutiliser ; un `-v2` ne s'invente pas : mot de la mère).
3. **Inventaire d'avant** : `D=… ; V=… ; ( umask 077 ; "$V" show instances --raw < /dev/null ) | F > "$D/ids-avant.txt" ; echo "codes ${PIPESTATUS[@]}" ;
   cat "$D/ids-avant.txt"`. Attendu : `codes 0 0` ; une ligne `<id> <étiquette>` par instance ; **aucune** ligne d'étiquette `bbis-t07-v1` ;
   aucune ligne 60918148 ; au moins un de 58936096, 58936099, 58936100 (témoin). Sinon arrêt (pas de témoin : nœud de la mère).
4. **Recherche d'offres** (lecture seule ; plan § 4.1 b) : `D=… ; V=… ; ( umask 077 ; "$V" search offers 'gpu_name=A100_SXM4 num_gpus=1
   cpu_cores_effective>=16 cpu_ram>=128 disk_space>=150 cuda_max_good>=13.0' -o 'dph_total' --raw < /dev/null > "$D/recherche.json" ) ;
   echo "code $?" ; wc -c "$D/recherche.json"`. Attendu : `code 0`, fichier non vide. Puis le choix de l'offre **par programme** (index 0 = la
   moins chère) : `D=… ; python3 -I -c 'import json,sys; d=json.load(open(sys.argv[1])); l=d.get("offers") if isinstance(d,dict) else d;
   o=sorted(l,key=lambda o:o["dph_total"])[int(sys.argv[2])]; print(o["id"], o["dph_total"], o["cuda_max_good"], o["gpu_name"])' "$D/recherche.json" 0`.
   Attendu : un identifiant entier, un prix ≤ le maximum du feu, `cuda_max_good` ≥ 13.0, `A100 SXM4`. Liste vide : arrêt.
5. **Offre construite par programme** : `cd "$W" && D=… && PY=… && OID=<identifiant lu au geste 4, copié, jamais composé> && PYTHON_BBIS="$PY"
   bash scripts/lancer_bbis_v3.sh offre-depuis-recherche "$D/recherche.json" "$OID" "$D/offre.json" ; echo "code $?"`. Attendu :
   `code 0` et `BBIS OFFRE ECRITE … offre <OID>, A100 SXM4 80GB, <prix> USD/h, stockage <s> USD/h, CUDA de l'hôte <v ≥ 13>`. Code 2
   (`BBIS REFUS`) : aucune offre écrite ; reprendre le geste 4 avec l'index 1, puis 2, au plus 5 essais, puis arrêt. Si accepté :
   `printf '%s\n' "$OID" > "$D/offre-id.txt"` (une seule fois).
6. **Garde de création** (porte le texte du feu ; **ne pas** contenir `vastai` + `create`) : `cd "$W" && PYTHON_BBIS="$PY" bash scripts/lancer_bbis_v3.sh
   creation . "R-<N> GO-2026-11-14-09" 0 ; echo "code $?"`. Attendu : `BBIS CREATION PERMISE {'go': 'GO-2026-11-14-09', 'relances': 0}`,
   `code 0`. Autre : arrêt.
7. **Commande (treize arguments `$#`)**, sortie écrite dans le dossier d'envoi, rien affiché :
   `cd "$W" && D=… && PY=… && RUNB=$(date -u +%Y%m%d-%H%M%S)-bbis-t07-v1 && ECH=$(( $(date +%s) + 13 * 3600 )) && PYTHON_BBIS="$PY" bash
   scripts/lancer_bbis_v3.sh commande . "$D/offre.json" "$(cat "$D/offre-id.txt")" 31fa8ac6041faf76b66282e0346750b9aefd4790
   prep/t07bbis-code-v1 20261111-151701-t06-reel calcul/t06-confirmation-7b-v1 "$RUNB" "$ECH" "R-<N> GO-2026-11-14-09" 0 python:3.11-bookworm >
   "$D/commande-imprimee.txt" ; echo "code $?" ; wc -lc "$D/commande-imprimee.txt"`. Attendu : `code 0` ; `wc -l` = **2** lignes, environ 32 700 octets. Tout `BBIS REFUS` : arrêt. À partir d'ici l'heure compte : l'échéance est celle du calcul de
   `ECH` ; plus de 20 minutes avant le jeu → refaire le geste 7 dans un fichier neuf `commande-imprimee-2.txt` (jamais écraser, R12).
8. **Contrôle par programme de la ligne imprimée** (rien de secret : le base64 est remplacé) :
   `D=… ; W=… ; python3 -I -c 'import re,sys,base64,hashlib; h,l,r=open(sys.argv[1],encoding="utf-8").read().split("\n"); b=re.search(r"echo ([A-Za-z0-9+/=]+) \| base64 -d",l).group(1); print(hashlib.sha256(base64.b64decode(b)).hexdigest()[:16], hashlib.sha256(open(sys.argv[2],"rb").read()).hexdigest()[:16], len(l)); print(h); print(l.replace(b,"<B64>"))'
   "$D/commande-imprimee.txt" "$W/scripts/amorce_bbis_v3.sh"`. Attendu : les deux empreintes **égales** (`18e2f2052efdca0d`), longueur de la ligne ≈ 32 600, ligne 1 qui
   porte `18e2f2052efdca0d`, et la ligne 2 selon le point 2 (étiquette `bbis-t07-v1`, `--disk 150`, `COMMIT=31fa8ac6…`, `GO_ID=GO-2026-11-14-09`,
   `-e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$GH_TOKEN`, échéance, `RUN_BBIS` de forme `AAAAMMJJ-HHMMSS-bbis-t07-v1`). Autre : arrêt.
9. **Lecture de la ligne, en trois morceaux** (C3), chacun de moins de 11 000 caractères : `D=… ; sed -n 2p "$D/commande-imprimee.txt" | cut -c1-11000`
   puis `… | cut -c11001-22000` puis `… | cut -c22001-`. Le contenu de ces trois sorties, mises bout à bout **sans une lettre de
   plus ni de moins**, est la ligne 2.
10. **Contrôle de la copie, facultatif** (réduit le risque R-1 ; ne prouve pas le jeu) : écrire la ligne copiée dans `"$D/ligne-copiee.txt"` par un appel à part
    (`cat > … <<'EOF'`, sans exécuter la ligne ; le texte contient le lancement, donc le crochet exige le seul numéro `GO-2026-11-14-09`, qui y est), puis
    `cmp "$D/ligne-copiee.txt" <(sed -n 2p "$D/commande-imprimee.txt")` → silence, code 0. Écart : arrêt, jamais jouer une copie qui diffère. La mère peut
    supprimer ce geste ; il n'est pas indispensable à la conformité.
11. **Jeu de la ligne, un seul appel, une seule fois** : `test -n "${CONTROLE_IA_GITHUB_TOKEN_2:-}" && export GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN_2" && test -n "${HF_TOKEN:-}" &&`
    suivi de la ligne 2, **identique à l'octet**, sauf `vastai` remplacé par `/home/user/vastai-env/bin/vastai` (C5). Rien d'autre :
    pas de redirection, pas de découpage, pas de script. Attendu (hors crochet) : le crochet laisse passer (point 4 : un seul numéro,
    `GO-2026-11-14-09`) ; la permission ou le classifieur peut refuser : **arrêt au premier refus, sans rejeu, sans reformulation**, le dire à la mère ;
    sortie `{"success": true, "new_contract": <identifiant>}` (forme des passes antérieures). Sortie autre, ou erreur : **ne pas rejouer** ; faire
    d'abord le geste 12 (une machine a pu être créée).
12. **Inventaire d'après et lecture de l'identifiant par programme** : `D=… ; V=… ; ( umask 077 ; "$V" show instances --raw < /dev/null ) | F > "$D/ids-apres.txt" ;
    echo "codes ${PIPESTATUS[@]}" ; diff "$D/ids-avant.txt" "$D/ids-apres.txt"`. Attendu : exactement **une** ligne ajoutée (`> <id> bbis-t07-v1`),
    aucune retirée ; cet identifiant égal au `new_contract` ; l'écrire : `grep ' bbis-t07-v1$' "$D/ids-apres.txt" | cut -d' ' -f1 > "$D/id-course.txt"`.
    Sinon (deux lignes, aucune, étiquette autre) : arrêt, compte rendu ; si une machine existe sans que l'amorce ait de chances de partir
    (copie douteuse), la détruire par les gestes 15 à 17. **Surveillance** (décision de la mère) : relire l'inventaire deux fois dans les dix
    premières minutes ; une instance qui reste « chargement » ou « arrêtée » sans trace de l'amorce est le signe d'une copie fausse.
13. **Garde de dépense, au moins chaque heure** : `cd "$W" && PYTHON_BBIS="$PY" bash scripts/lancer_bbis_v3.sh depense <CUMUL> <PRIX>` (point décimal ;
    CUMUL = 0,749 + heures écoulées × prix relu + disque). Attendu : `BBIS DEPENSE {…}`, code 0. Code 2 : destruction (geste 15).
14. **(rappel) Aucune relance, aucune seconde création** sans mot de la mère ; échéance de la minuterie = geste 7 (13 heures).
15. **Destruction, par l'identifiant lu** : `cd "$W" && D=… && PYTHON_BBIS="$PY" bash scripts/lancer_bbis_v3.sh detruire "$(cat "$D/id-course.txt")"`. Attendu :
    `GO_ID=GO-2026-11-14-09 vastai destroy instance <ID> -y` puis le rappel du geste 17 ; refus si l'identifiant est l'un des six
    intouchables (jamais attendu : c'est une faute de lecture, arrêt). Jouer ensuite la ligne **avec le chemin complet**
    (`GO_ID=GO-2026-11-14-09 /home/user/vastai-env/bin/vastai destroy instance <ID> -y`, `<ID>` pris de `id-course.txt`). Le code de sortie n'est jamais jugé.
16. **Témoin** : `D=… ; V=… ; ( umask 077 ; "$V" show instances --raw < /dev/null ) | F` : dans cette sortie, prendre dans l'ordre 58936096, 58936099, 58936100, présent
    **aussi** dans `ids-avant.txt` ; jamais 60480302, 60599797, 60670453 ; jamais l'identifiant de la course.
17. **Preuve de destruction** (attendre au moins 30 secondes après le geste 15) : `cd "$W" && D=… && PYTHON_BBIS="$PY" VASTAI_BBIS="$V" bash scripts/lancer_bbis_v3.sh
    verifier-destruction "$(cat "$D/id-course.txt")" <TEMOIN>`. Attendu : `BBIS DESTRUCTION PROUVEE …`, code 0. Code 2 « toujours dans la liste » : refaire
    les gestes 15 puis 17 ; « témoin absent » : autre témoin (geste 16) ou nœud. Puis supprimer, par le chemin exact imprimé
    (`liste des instances gardée : <DOSSIER>/instances.json`), ce dossier de liste brute (C8). Puis **la mère relit l'inventaire** : identifiant absent, les autres présentes.

## Réserves pour la mère

1. **R-1** : copie de 32 Ko (C3) ; décision de la mère : accepter le risque, ou demander à Lazar un mot écrit pour jouer la ligne par fichier (crochet vu).
2. **R-2** : crédit (C6) ; prix horaire maximal à écrire dans le feu.
3. Les règles de permission de `.claude/settings.json` ne couvrent que l'étiquette de la répétition : le geste 11 sera jugé sans règle ; arrêt au premier refus (plan § 4.2).
4. Ce que je n'ai pas pu jouer : `show instances`, `search offers`, `create`, `destroy` (aucun appel au loueur, par consigne) ; la forme exacte de leurs sorties
   (clés `id`, `label`, `dph_total`, `cuda_max_good`, `new_contract`) est celle que le code et les passes antérieures supposent, non revérifiée ici.
5. Le crochet n'a pas été simulé sur la ligne complète (incident 1) ; l'analyse du point 4 vient de la lecture de son code.

## Déclaration d'exclusion

- **Rôle** : contre-lecteur neuf (R2) de la création de la machine de la course de B bis ; **lettre de modèle : C** ; n'a écrit aucun fichier de B bis ;
  ne sera lecteur d'aucun verdict.
- **Heures** (`date -u`) : début 13:43:01Z ; jeu à blanc du lanceur et des gardes de 13:44Z à 13:47Z ; rédaction de 13:49Z environ ; fin : voir la ligne finale.
- **Pièces lues** (chemin, empreinte) :
  - `brouillons/T0.7-etape-B-bis-v1/plan-course-bbis-v1.md`, `e2505df9fbb28c9b84ab24f552a130078b8a0281b94f0c6d1ea961f08a289239` : lignes 1 à 200 et 256 à 422 (§ 4, § 5, § 6, § 7 entiers ; § 8 à 10 non lus) ;
  - `brouillons/T0.7-etape-B-bis-v1/verification-gestes-avant-course-bbis-v1.md`, `415927e13c507690acf1be0e7d98eef1ef984d1c64dfe66c1fa3dcc14073ea34`, entier ;
  - `scripts/lancer_bbis_v3.sh`, `dc26ea01a06bfb9eac3fc4f9f1b9b3bb86490d61d9e8f5deb54bcb180b17ee68`, entier ;
  - `scripts/amorce_bbis_v3.sh`, `18e2f2052efdca0d9d447738c3c4f1099302f7134b9518b59eea78ba563695dd`, entier ;
  - `src/controle_ia/t07bbis/registre_bbis_v1.py`, `c3b1848b3466a88a250aee2b58477c91ff5d660592c1a6cc695f8910005dcf1b`, entier ;
  - `/home/user/controle-ia-travail/.claude/hooks/garde_calcul.py`, `73be063822531b27e74cf522794cd262495ba21ceea9b62a41ef4a17879a4850`, entier ;
  - `/home/user/controle-ia-travail/.claude/settings.json`, `7bf78ecf10dc41979bb5f6f4b35922ff228e1000fcf0475581277aab9e521333`, début (60 lignes ; **hors de la liste donnée**) ;
  - `/home/user/controle-ia-travail/registres/go.md`, `b5468a46787856b2e53817599a951b6aa04a0def05db057bec3c43689f48a0a4` : lignes `GO-2026-11-14-09` et `GO-2026-11-16-06` entières ; comptes de types ; début des colonnes de la seule ligne de type « révocation » ;
  - `/home/user/controle-ia-travail/registres/decisions.md`, `91df5cd3abac76965305786e092e3c6af83d17c22b0d5e5447ac217ecdd186de` : lignes R-2975, R-2981, R-2982, R-2985 entières ; **en plus de la liste** : R-2829, R-2883, R-2950 (début, jusqu'à 3 500 caractères) pour la façon de jouer le lancement et les clés ;
  - sorties du bloc-notes énumérées en tête (offre et listes fabriquées).
- **Jamais ouvert** : rien sous `diag/`, `donnees/`, `docs/verdicts/` ; rien de l'étape B de T0.7 ni de 7a ou 7b ; aucune valeur de clé (`test -n` seulement, aucune `env`,
  `printenv`, `set` ni `export -p`) ; `registres/decisions.md` et `registres/go.md` jamais entiers ; aucun fichier du dossier d'envoi réel (inexistant) ; le reste du plan (§ 8 à 10) et le texte scellé
  de B bis ; aucun clone, aucun `git fetch`, aucune variable `GIT_*`.
- **Incidents** :
  1. **Commande refusée par le crochet de garde (13:45Z)** : mon script de simulation du crochet (un fichier écrit par `cat`, rejouant le crochet sur la ligne imprimée et sur des variantes)
     citait dans son texte `vastai create` et le numéro `GO-2026-11-16-06` (GO de type « décision ») : le crochet l'a bloqué (« GO-2026-11-16-06 est un GO de type 'décision', pas calcul »).
     **Arrêt sans rejeu ni reformulation** : le script n'a pas été écrit ni joué ; je n'ai rien contourné ; cet incident prouve le point C4. Conséquence : le crochet n'est pas simulé (réserve 5) ;
     les comptes de types de `go.md` ont été relevés par une commande séparée, sans ces mots.
  2. Aucune autre commande refusée par une permission ou le classifieur ; aucun processus arrêté ; un seul processus léger à la fois (le jeu à blanc, 4 secondes) ; `TMPDIR` pointé sur le bloc-notes ;
     aucune écriture sous le dépôt hors ce rapport ; `git --no-optional-locks` pour les lectures.
  3. `ls-remote` interrogé quatre fois (dépôt de travail, lecture seule) ; aucun appel au loueur.
  4. Les sorties de la ligne 2 et du plan n'ont pas été affichées en entier (lecture par programme et par plage de lignes).

Fin de la rédaction : 2026-11-16T13:51:16Z (`date -u`), juste avant le scellement ; fichier neuf, non committé.
