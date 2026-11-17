# Procédure de la machine louée du crible (iii) — v1

- **Objet** : jouer le crible (iii) de l'organisme d'idéation (deux passes : `opus55` choisit, `fable52` écrit ; bras S, D, H, B ;
  20 mondes MR-2 du secret du crible ; 100 appels sur crédits de Claude ; cinq files de quatre mondes) sur une petite machine louée,
  sans ssh, du secret à la lecture non ouverte, selon la pièce qui fera foi
  `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-iii-version-foi-v1.md` (`91b4bf30fbf8b83d2c057088d8776be19831b006f1010bcb3c7e2e231d2c7179`)
  — ses sections « Partie B », « Graines », « Étapes » (4 et 5), « Liste d'arrêt » font foi ; en cas d'écart, la pièce prime et
  l'écart est un nœud.
- **Modèles suivis** : procédure v14 du pilote MR-2 (`procedure-pilote-mr2-v74-machine-v14.md`, `20355627…`, branche
  `lot/compte-organisme-v1` : barrières, feux, phrase chiffrée, balayage, minuterie) et procédure v6 de la machine de l'idée 1.1
  (`docs/procedures/machine-jeu-idee-1-1-v1/procedure-machine-jeu-idee-1-1-v6.md` : offre choisie par la garde, amorce compressée,
  réponse du loueur écrite à part, reprise de la poussée, destruction prouvée par un témoin). Aucune de ces pièces n'est modifiée.
- **Statut** : écrite, essayée hors ligne (essais, banc de mutations, essai à blanc complet, répétition de la machine : sorties
  gardées dans ce dossier) ; **ne part pas au feu** avant les préalables du § 2 (contre-lecture du code et de cette procédure par un
  sous-agent neuf d'un autre modèle, R2 ; texte qui fait foi scellé sous `prereg/` ; addendum d'empreintes ; sonde des gabarits ;
  lignes « calcul » ; mot et phrase de Lazar). Aucune machine, aucun appel au loueur, aucun appel de modèle, aucune dépense à
  l'écriture.
- **Pièces** (dossier `docs/procedures/crible-iii-v1/`, chacune avec son compagnon `.sha256`) :

  | pièce | rôle | empreinte |
  |---|---|---|
  | `crible_iii_v1.py` | noyau : analyseur, filtre, tirage de H, gabarits G1 et G2, files, bornes, gardes, lignes de GO | `b163e4c6d8070ec40c544c4519143711fbb8d9ec3d6f9a6a931152b0d265a156` |
  | `lanceur_crible_iii_v1.py` | lanceur : secret, mondes, préparation, crible (à blanc, réel), sonde des gabarits, rapatriement, empreintes | `20cff93d6e22a0cad695e42d6a90510d0fb54bb148f988ae588ac86bfff549e1` |
  | `mesure_crible_iii_v1.py` | mesure gelée (nom réservé par la pièce), une seule fois | `8e0df42ac59f8c30e7eece797b1d28b2c770af1d2f1f0516d9bd4b98408a9eeb` |
  | `lire_crible_iii_v1.py` | lecture gelée (nom réservé par la pièce), étages 0 à 7 | `fb83b6303dfc2433082a372ce15fbbc0c18e4077cefcb0daf91fdb045ee0a2e7` |
  | `relais_factice_crible_iii_v1.py` | relais factice (relais du pilote, amont scripté) : essais à blanc seulement | `8f28dacd87e800c74e6278b0c2663a6298fe572698832c1bac99edecc2d56a11` |
  | `amorce_crible_iii_v1.sh` | amorce de la machine (passée à la création) | `7f589103b64ab36813ea8a3e17efded5ca73b7279d987d78a134a3f7f167f730` |
  | `machine_crible_iii_v1.sh` | programme machine (barrières, crible, mesure, rapatriement) | `cdc2420b879d80e773cb0ae1764f44b3d0b22308cff3a79c7962a8e87c9f2002` |
  | `machine_crible_iii_v1.py` | aide du programme machine (attendus, feux, balayage) | `5dc046c2940b8feaf1ed8b595918b19a8ad76a657170015df06e27e1a109b669` |
  | `session_crible_iii_v1.sh` | outil de la session (offre, commande, feux, état, destruction, preuve) | `89ed262b7f490b51f67d7aad72d745f8d096050412c7e010b3e4681e11284a3a` |
  | `garde_session_crible_iii_v1.py` | gardes de la session (offre, échéance, identifiant, absence, dépense, lignes de GO) | `4e4aa32af4e9149790042287cd83a8c6f574dc6e0da1eb993a25633b36d5059b` |
  | `essais_crible_iii_v1.py` | essais R5 du niveau A (cas sain et artefact par ligne d'arrêt ; filtre à la main) | `04153eb16fb2fb931dc87d3a8c5bb94dde26ce59c0a9d7c648718af1ca089708` |
  | `mutations_crible_iii_v1.py` | banc de mutations (35 mutations) | `8c77eae8c3970ccc51d20c0fa41f5e5a6ef45e55cb202ce77d425d88eed0d36a` |
  | `essai_a_blanc_crible_iii_v1.py` | essai à blanc complet, chaîne réelle, relais factices (niveau B) | `7878813196515006cf9e4dfd7a4ee23a1879ab1f600588b7378eee4d09d5a9ef` |
  | `repetition_machine_crible_iii_v1.sh` | répétition locale de la machine (dépôt jouet, doublures) | `a72ca88d28547827d172adf40c39e53aea76405613fe52b5453e160bdb9bf32c` |
  | `doublures_repetition_crible_iii_v1.py` | doublures de la répétition (loueur, lanceur, mesure, lecture) | `f264d6dc8bf787e877c3c94d7ae90adff81e8ad410ca2adc06b314f93d62257a` |
  | `sortie-essais-crible-iii-v1.txt` | sortie gardée des essais | `f200776ef8027cea337c1a20bb56202f8754dff85d109e3706501f827b362aa4` |
  | `sortie-mutations-crible-iii-v1.txt` | sortie gardée du banc de mutations | `8e034dba1e9c4414cd8271a4c3ed2c4b1235da656ab38d5275e54142014ca31d` |
  | `sortie-essai-a-blanc-crible-iii-v1.txt` | sortie gardée de l'essai à blanc complet | `7105d41db9d367ef36da58f278c2a880762cec6b797ec6b4aa1f44c4985a856a` |
  | `sortie-repetition-machine-crible-iii-v1.txt` | sortie gardée de la répétition de la machine | `3720c374532f5d648244f32bdcf699917bd6255e2af5fdf72cca205200ce512e` |
  | `devis-machine-crible-iii-v1.md` | devis de la machine (κiii2) | `066f8297aa52e0e3df77e1b0b27458ca3b33c7f0874dcdc7a8f0fa3454b6b740` |
  | `sortie-essai-a-blanc-crible-iii-v1-jeu-1-avant-correction.txt` | premier jeu de l'essai à blanc, avant la correction de la garde du pire cas (gardé, R4) | `4fbbeb8eaef597abf73f84b5539a96ebc939c12d21b9a61c06552e26b9b46de3` |
  | `rapport-crible-iii-v1.md` | rapport (ce qui reste avant le feu) | son compagnon |

## 1. Ce que fait la machine (amorce, puis programme machine), dans l'ordre

0. **Amorce** (`amorce_crible_iii_v1.sh`, passée compressée en base64 à la création) : arguments contrôlés (deux commits de 40
   caractères, empreintes de 64, trois lignes de GO lisibles, `GO_ID` = la ligne de la part machine, branches
   `calcul/crible-iii-…` distinctes, chemins du texte et de l'addendum, échéance dans les 17 h 05, identifiant de l'instance, jeton et
   clé présents par leur nom, outils présents) ; **un refus avant la minuterie demande la destruction de l'instance par elle-même**
   (DELETE trois fois, puis « stopped », jamais jugé ; la session prouve l'absence) ; **minuterie armée** (à l'échéance : DELETE
   répété par l'identifiant, « stopped » après cinq demandes) ; dépôt partiel aux commits `COMMIT_LOT` (paquet de l'arbre 605e0f6 et
   relevé de la sonde v74, branche `lot/compte-organisme-v1`) et `COMMIT_MAIN` (code du crible, texte, addendum, registre des GO) ;
   programme machine et aide pris à `COMMIT_MAIN`, empreintes exigées ; `exec` du programme machine (la minuterie reste son enfant).
   Relance du conteneur par le loueur (marque présente) : minuterie réarmée, **aucune passe refaite**, arrêt (A) poussé.
1. **Mise en place** : branche de sortie absente (sinon arrêt sans poussée, R12), branche d'entrée absente (sinon arrêt (A)), première
   poussée ; numpy 2.5.3 (`pip`, 900 s au plus), contrôle `(3, 13) 2.5.3`.
2. **Pièces** : paquet `e3d83e47…`, relevé de la sonde `f56d9c0e…` et son compagnon, texte (`TEXTE_SHA256`), addendum
   (`ADDENDUM_SHA256`) ; code du crible **égal à l'addendum** (cinq fichiers, ligne « empreinte  chemin ») ; arbre dépaqueté, tête
   605e0f6, propre. Arrêt (A) sur tout écart.
3. **Secret, puis phrase de Lazar (barrière 1)** : `lanceur secret` (32 octets, 0600, hors dépôt), paire RSA de 4 096 bits pour la
   phrase, `secret-sha256.txt`, clé publique et son empreinte poussés ; état `attente du feu 1 (phrase)` ; la machine attend le feu au
   plus **une heure** après son départ, revérifie l'inscription du secret sur `main`, déchiffre, contrôle la forme et l'empreinte
   du fichier de la phrase, **efface la clé privée**, pousse `phrase-sha256.txt`.
4. **Vingt mondes (barrière 2)** : `lanceur generer` (graine `graine_monde_crible` : étiquette « crible-iii-v1 », secret, phrase,
   empreinte du texte, r ; huit tirages de `generer_v4` ; quatre processus) ; vingt mondes « conforme » exigés, distincts ;
   `engagement-mondes.json` (H et S1 à S20) poussé ; état `attente du feu 2 (mondes)` ; feu attendu **20 minutes** ; inscription de
   H et des vingt empreintes revérifiée sur `main`.
5. **Préparation** : `lanceur preparer` (C-16 admises, C-17, épisodes « crible-iii-v1 », textes G0 et G1 bâtis et relus, pire G2 sous
   53 000 octets, ensembles de H tirés et filtrés) ; **essai à blanc sur les vrais mondes** (`jouer --mode a_blanc`, relais factices,
   cinq files, bornes gelées : 100 appels complets, 20 mondes complets exigés) et son rapatriement (aucun monde) ; état `attente du feu
   3 (crible reel)` ; feu attendu **20 minutes**, portant H et les deux lignes de GO.
6. **Crible réel, une seule fois** : contrôles juste avant (dossier et registre des lancements absents, numpy, texte, ports 8811 et
   8812 libres, fournisseur joignable par poignée TLS, **au moins 10 h avant l'échéance** : garde de départ, clé présente) ; lanceur
   `jouer --mode reel` par `env -i`, la seule clé passée ; le lanceur refait ses gardes (configuration v12, relevé de la sonde,
   addendum, lignes de GO, engagement, registre des lancements, garde de départ) **avant tout appel** ; état poussé toutes les 15
   minutes ; un feu d'arrêt lu toutes les minutes arrête le lanceur **par son PID** (R10). **Aucune relance, aucune reprise d'appel.**
   Code 0 : mesure ; code 2 ou 3 : arrêt (A), ni mesure ni lecture d'issue.
7. **Mesure, une seule fois** (`mesure_crible_iii_v1.py`, empreinte de l'addendum exigée) ; **lecture** écrite sans être ouverte
   (`sortie-lire-non-ouverte.txt`, poussée sous `remis-au-sous-agent/`) ; **rapatriement** sans `prive/` (jamais les mondes ni les
   textes servis) ; état `fini` ; poussée finale reprise toutes les cinq minutes jusqu'à l'échéance si elle échoue ; puis attente de
   la destruction (par la session, ou par la minuterie à l'échéance).

Avant chaque poussée, un **balayage** cherche dans chaque fichier le jeton, la clé (brute, en URL, en base64), le secret (brut,
hexadécimal minuscules et majuscules, base64) et la phrase (brute et base64, 8 octets au moins) ; un fichier où une forme est trouvée
est **exclu**, nommé dans `etat.txt` (`exclus_balayage=`), jamais la valeur. Rien de plus de 95 Mo.
États poussés : `mise en place` → `pieces et arbre` → `secret` → `attente du feu 1 (phrase)` → `mondes` → `attente du feu 2
(mondes)` → `preparer` → `essai a blanc` → `attente du feu 3 (crible reel)` → `jouer reel en cours` → `mesure` → `rapatriement` →
finaux : `fini`, `arret (A)`, `noeud, machine gardee`, `sortie inattendue`.

## 2. Ce que fait la mère

**Avant de remettre la suite à l'opérateur** — ne pas commencer tant qu'un point manque :

1. **Texte qui fait foi** scellé par `sceller_prereg` et recopié sous `prereg/` (chemin `TEXTE_CHEMIN`, compagnon d'une ligne), après
   la sonde des gabarits (version 2 si elle précède la recopie : III-7 par sa règle), les trois valeurs calculées sur processeur, le
   versement de l'annexe A et le tour différentiel (pièce, statut, restes (a) à (d)).
2. **Contre-lecture du code** (les cinq fichiers du crible, la machine, la session, cette procédure, les essais et leurs sorties) par
   un sous-agent neuf **d'un autre modèle** (pièce, Étapes, point 0) ; puis **addendum d'empreintes** scellé (`ADDENDUM_CHEMIN`) :
   une ligne « empreinte  `docs/procedures/crible-iii-v1/<fichier>` » pour chacun des cinq fichiers du crible, l'empreinte du texte
   qui fait foi, et les empreintes de l'arbre (`lanceur empreintes --arbre …`) ; il ne change rien d'autre.
3. **Sonde des gabarits** (κiii0, obligatoire) jouée depuis la session, sans machine (§ 4, geste 0), relevé versé et lu avant la
   recopie : ses règles d'avance déclenchées (un appel sous G2 tronqué, une carte non évaluable, aucune liste sous G1) arrêtent tout
   (gabarit réécrit, nouvelle sonde sur nouvelle ligne, crible non lancé).
4. **Lignes « calcul »** κiii0, κiii1 et κiii2 inscrites dans `registres/go.md` (accord de Lazar), dans l'enveloppe de
   GO-2026-11-15-06 : le lecteur gelé exige pour κiii1 un périmètre portant « crible (iii) », `fable52` et `opus55`, plafond
   `260 USD` ; pour κiii2, « crible » et « machine », plafond `3 USD` ; pour κiii0, « Sonde des gabarits » et « crible (iii) »,
   plafond `7 USD` ; référence GO-2026-11-15-06 ; échéance au plus tôt le jour du jeu. Commit et poussée sur `main` : `COMMIT_MAIN`
   (40 caractères), qui porte aussi le dossier du code, le texte et l'addendum.
5. **Feu écrit** : une ligne `R-<N>` de `registres/decisions.md` qui cite en toutes lettres κiii1, κiii2, `COMMIT_LOT`, `COMMIT_MAIN`,
   l'étiquette `crible-iii-v1-AAAAMMJJ`, les branches `calcul/crible-iii-sortie-v1` et `calcul/crible-iii-entree-v1`, l'image
   `python:3.13-bookworm`, le disque de 20 Go, le prix garde maximal de 0,15 USD/h (relu au plus 0,17), l'échéance à 17 h,
   0 relance, l'opérateur (arrêt au premier refus d'une permission, du crochet ou du classifieur, sans rejeu ni contournement).
6. **Solde des crédits de Claude** vérifié (270 USD au pire pour ce crible et sa sonde, en plus des autres usages) ; crédit du loueur
   au moins 5 USD ; **mot de Lazar** tapé dans la session mère, daté de moins de dix minutes, disant qu'il est présent pour la
   demi-heure qui suit (la phrase est demandée dans l'heure) ; **préavis** à Lazar avant l'impression (création imminente, échéance à
   17 h, exposition de la clé dans la configuration de l'instance jusqu'à la destruction).
7. **Fenêtre seule** : entre l'inventaire d'avant et la preuve d'absence, aucune autre création ni destruction chez le loueur par une
   session du programme ; annonce aux autres sessions (et interdit de la liste brute des instances : elle porte la clé).

**Pendant le jeu** : inscriptions des barrières (secret, phrase, H et S1 à S20) sur `main`, dans un fichier qu'elle nomme ; feux dans
les cinq minutes ; rappel posé à l'échéance plus cinq minutes dès la création ; garde de dépense chaque heure. **Après** :
destruction et preuve (§ 4, gestes 16 à 18) ; sorties versées sur une branche de travail, **jamais sur `main`** (les réponses brutes
portent les identifiants servis, R-2731) ; dépense rapprochée des journaux des relais et de la console ; lecture remise à un
sous-agent neuf (R13), audit de symétrie (R4) écrit avant le prononcé ; **aucune adoption**.

## 3. Leçons reprises

- Pilote v14 : sans ssh, tout passe par l'amorce, la branche de sortie (écrite par la machine seule) et la branche d'entrée (écrite
  par la mère seule) ; la phrase ne passe jamais en clair (RSA-OAEP, clé privée née et morte sur la machine) ; la machine exige les
  inscriptions sur `main` ; feu d'arrêt à chaque attente ; une seule machine, aucune seconde création sans absence prouvée.
- Idée 1.1 v6 : l'offre se choisit **par la garde jouée sur chaque offre** de la recherche (la moins chère acceptée, chaque refus
  nommé), avec ou sans carte (inutilisée) ; l'amorce passe **compressée** ; la réponse du loueur (qui porte une clé propre à la
  machine) est écrite dans `creation.json` (0600) et jamais affichée ; `GH_TOKEN` posé depuis `CONTROLE_IA_GITHUB_TOKEN_2` par son nom,
  dans le même appel ; destruction jamais jugée par un code de sortie : absence prouvée, témoins présents.
- Changements propres au crible : **une seule clé** (un seul fournisseur sert les deux relais) ; vingt mondes générés en quatre
  processus ; garde de départ de 10 h (4 × 7 200 s + 2 h) au lieu de 12 h 30 ; **aucune relance** du crible réel (la pièce : « aucune
  reprise, aucune bascule ») ; la mesure et la lecture sont celles du crible.

## 4. Gestes exacts de l'opérateur

**Constantes à redonner en tête de chaque appel** : `W=/home/user/controle-ia-travail ; DC=$W/docs/procedures/crible-iii-v1 ;
ENVP=/home/user/crible-iii-envoi-v1 ; V=/home/user/vastai-env/bin/vastai ; OUTIL="env W=$W ENVP=$ENVP bash $DC/session_crible_iii_v1.sh" ;
CL=<COMMIT_LOT> ; CM=<COMMIT_MAIN> ; BS=calcul/crible-iii-sortie-v1 ; BE=calcul/crible-iii-entree-v1 ; GC=<κiii1> ; GH=<κiii2> ;
TC=<TEXTE_CHEMIN> ; AC=<ADDENDUM_CHEMIN>`. Règle générale : tout code ou toute sortie autre que l'attendu = **arrêt**, compte rendu à
la mère, aucun rejeu, aucun contournement. Jamais `env`, `printenv`, `set` sans argument, `export -p` ; jamais une valeur de clé à
l'écran ; aucune heure écrite à la main (`date -u`) ; `git fetch` avec refspec seulement.

0. **Sonde des gabarits (κiii0), sans machine, depuis la session** (avant tout le reste ; trois appels, 7 USD au pire) : monde de
   développement public `python3 -I -B $DC/lanceur_crible_iii_v1.py generer --public --arbre <arbre> --texte-sha256 <empreinte du
   texte> --sortie <privé>/MONDES-public.json --un-seul` (le seul monde de développement 1, graine publique, ≈ 3 à 10 min),
   puis `GO_ID=<κiii0> python3 -I -B $DC/lanceur_crible_iii_v1.py sonde-gabarits --mode reel --arbre <arbre> --mondes … --mondes-sha256 …
   --texte-sha256 … --sortie <dossier neuf hors dépôt> --releve-sonde <relevé v74> --registre-go $W/registres/go.md --go-sonde <κiii0>
   --registre-lancements <hors dépôt>` (l'arbre dépaqueté du paquet `e3d83e47…` ; la clé passée par son nom ; aucune autre). Attendu :
   `regles_d_avance` non déclenchée, trois appels. Le relevé va à la mère (versé hors de `main`, il porte les identifiants servis).
1. **Pièces et feu** : `cd "$DC" && for c in *.sha256; do sha256sum -c "$c"; done` → toutes `OK` ; `git -C $W fetch origin
   +refs/heads/main:refs/remotes/origin/main +refs/heads/lot/compte-organisme-v1:refs/remotes/origin/lot/compte-organisme-v1` ;
   `git -C $W merge-base --is-ancestor $CL refs/remotes/origin/lot/compte-organisme-v1 && git -C $W merge-base --is-ancestor $CM
   refs/remotes/origin/main && echo ancetres` → `ancetres` ; `grep -c "^| R-<N> |" $W/registres/decisions.md` → `1`.
2. **Dossier d'envoi neuf** : `test ! -e $ENVP && mkdir $ENVP && echo code 0` → `code 0` (sinon arrêt, R12).
3. **Crochet** `garde_calcul.py` éprouvé dans la session de l'opérateur (cas sain et artefact, R5) ; toute ligne qui porte la création
   commence par `GO_ID=$GH`.
4. **Crédit** : `$OUTIL credit` → `crédit … USD (au moins 5)`.
5. **Inventaire d'avant** : `$OUTIL inventaire avant` → `n instance(s) listée(s)` (liste vide refusée).
6. **Essai de poussée** (chemin exact des feux, sans dépense) : `$OUTIL essai-poussee calcul/essai-poussee-session-crible-iii-v1` →
   `feu poussé sur …`.
7. **Recherche, puis offre par la garde** : `( umask 077; "$V" search offers 'rentable=true reliability>=0.98 cpu_cores_effective>=4
   cpu_ram>=8 disk_space>=20 inet_down>=100 dph_total<=0.15' -o 'dph_total' --storage 20 --raw < /dev/null > $ENVP/recherche.json )`
   puis `$OUTIL offre-depuis-recherche $ENVP/recherche.json $ENVP/offre.json` → une ligne par offre, puis `CRIBLE OFFRE ECRITE …`
   (prix du réseau consignés). Aucune offre : arrêt.
8. **Étiquette** : `test ! -e $ENVP/etiquette.txt && echo "crible-iii-v1-$(date -u +%Y%m%d)" > $ENVP/etiquette.txt`.
9. **Mot de Lazar, puis préavis** (§ 2, point 6) ; sans le mot daté de moins de dix minutes : rien n'est imprimé.
10. **Commande** : `$OUTIL commande $ENVP/offre.json $CL $CM $BS $BE $(cat $ENVP/etiquette.txt) $GC $GH $TC $AC > $ENVP/commande-imprimee.txt;
    echo code $?` → `code 0` ; l'outil refuse si : offre hors bornes ; commit absent ou `CM` non ancêtre de `main` ; amorce du commit
    différente de celle du dossier ; texte ou addendum absent ou différent de son compagnon au commit ; paquet absent de `CL` ; lignes
    de GO refusées par le lecteur gelé ; branche présente sur le dépôt distant ; jeton ou clé absent par son nom ; arguments refusés
    par l'amorce ; `echeance.txt` déjà écrit (jamais deux créations). Il écrit l'amorce compressée en base64 dans `$ENVP/amorce.b64`
    (0600) et **deux lignes** dans `$ENVP/commande-creation.txt` : la première pose `GH_TOKEN` (depuis `CONTROLE_IA_GITHUB_TOKEN_2`),
    `ENVP` et `umask 077` ; la seconde commence par `GO_ID=$GH` puis l'outil du loueur à son chemin complet, `create instance`,
    l'offre, `--image python:3.13-bookworm --disk 20 --cancel-unavail --label <étiquette> --env "…"` (les **noms** de la clé et du
    jeton, jamais leurs valeurs), `--entrypoint bash --args -c "…"` (l'amorce lue par `$(cat "$ENVP/amorce.b64")`), la réponse dans
    `$ENVP/creation.json`, puis `echo code=$?`.
11. **Jeu de la ligne, une seule fois, dans les dix minutes** (un seul appel) : `cat > $ENVP/a-jouer.txt <<'LIGNES'` (les deux lignes
    recopiées telles quelles) `LIGNES` puis `$OUTIL comparer $ENVP/a-jouer.txt && . $ENVP/a-jouer.txt`. Attendu : `code=0`. Si la
    commande ne rend pas la main : **ne jamais la rejouer** ; passer au geste 12. Premier refus d'une permission, du crochet ou du
    classifieur : arrêt, sans rejeu.
12. **Identifiant** : `$OUTIL creation` → `ID=<n>` (repli sans `new_contract` lisible : `$OUTIL trouver $(cat $ENVP/etiquette.txt)`) ;
    `date -u +%FT%TZ > $ENVP/heure-creation.txt`. Puis `$OUTIL inventaire apres-creation` (témoin écrit à la création), `$OUTIL
    ajoute` → une seule instance ajoutée, et `$OUTIL relire $(cat $ENVP/etiquette.txt)` → prix relu au plus 0,17 USD/h ; hors borne :
    destruction aussitôt (gestes 16 à 18), puis nœud. Consigner identifiant, étiquette, prix, heure, échéance (`echeance.txt`) ; la
    mère pose le rappel de l'échéance plus cinq minutes.
13. **Barrière 1** : `$OUTIL etat $BS` jusqu'à `etape=attente du feu 1 (phrase)` (première poussée attendue en quelques minutes ;
    rien 20 minutes après la création : `"$V" logs <ID>` en lecture seule, puis destruction) ; la mère inscrit l'empreinte du secret
    (`secret-sha256.txt` de la sortie) sur `main` et donne `COMMIT_INSCRIPTION`, `CHEMIN_INSCRIPTION` ; **Lazar tape sa phrase dans la
    session qui lance** : `( umask 077; cat > $ENVP/phrase.txt ) <<'PHRASE'` (une ligne) `PHRASE` ; puis `$OUTIL feu-phrase $BS $BE
    $ENVP/phrase.txt <COMMIT_INSCRIPTION> <CHEMIN_INSCRIPTION>` → `feu poussé …`, l'empreinte du fichier de la phrase (à inscrire), et
    `fichier de la phrase effacé` (effacé même si la poussée échoue) ; la mère inscrit cette empreinte.
14. **Barrière 2** : `$OUTIL etat $BS` jusqu'à `attente du feu 2 (mondes)` (≈ 15 à 75 min de génération) ; la mère inscrit H et S1 à
    S20 (`engagement-mondes.json` de la sortie, lus par programme, jamais tapés) ; `$OUTIL feu-mondes $BS $BE <COMMIT> <CHEMIN>`.
15. **Barrière 3** : `$OUTIL etat $BS` jusqu'à `attente du feu 3 (crible reel)` ; `$OUTIL recuperer $BS $ENVP/retour-blanc` (dossier
    neuf) ; la mère lit `journal-08-blanc.txt` (100 appels complets, 20 mondes complets) ; puis `$OUTIL feu-reel $BS $BE $GC $GH`.
16. **Pendant le crible** : `$OUTIL etat $BS` toutes les 15 minutes (un état `jouer reel en cours` vieux de plus de 40 minutes : nœud
    de la mère, sans feu d'arrêt sur ce seul constat) ; **chaque heure**, garde de dépense : `$OUTIL depense <CUMUL> <PRIX>` (point
    décimal ; `CUMUL` = heures depuis la création × prix relu) → refus : destruction. Toute cause d'arrêt vue par la session :
    `$OUTIL feu-arret $BE "CAUSE"` (lettres sans accent, chiffres, espaces et « , . : ; ( ) _ - », 100 caractères au plus) ; l'arrêt
    doit paraître dans les trois minutes, sinon destruction sans attendre.
17. **Fin** : état final `fini`, `arret (A)` ou `sortie inattendue` → `$OUTIL recuperer $BS $ENVP/retour` (`remis-au-sous-agent/`
    **non ouvert**) ; `(cd $ENVP/retour/rapatrie-reel && sha256sum -c lecture-crible-iii-v1.json.sha256)` (comparé, non ouvert) ;
    `noeud, machine gardee` → destruction au mot de la mère, au plus tard à l'échéance plus cinq minutes.
18. **Destruction et preuve** : `$OUTIL detruire $(cat $ENVP/etiquette.txt)` → imprime `GO_ID=$GH <outil> destroy instance <ID> -y`
    (instance déjà absente : `verifier-destruction` d'abord) ; la jouer telle quelle (le code de sortie n'est jamais jugé) ; au moins 30
    secondes après : `$OUTIL verifier-destruction` → `absente ; témoins toujours listés : n` (référence : `ids-avant-destruction.txt`,
    sinon `ids-apres-creation.txt`) ; « toujours listée » : refaire par ce seul identifiant ; consigner identifiant, étiquette, heure
    (`date -u`), résultat au registre des arrêts ; effacer `$ENVP/creation.json` par son chemin exact (clé propre à la machine).
    **À l'échéance plus cinq minutes au plus tard**, la session joue ce geste sans attendre aucun mot.

## 5. Ce que la procédure ne fait pas

- Elle ne lit aucune issue : la lecture est remise à un sous-agent neuf (R13) ; la session qui lance n'ouvre pas
  `remis-au-sous-agent/`.
- Elle ne relance rien : une machine arrêtée avant le crible réel consomme ses branches et son échéance ; une seconde tentative
  demande une version nouvelle (noms neufs, R12) et le mot de la mère.
- Sans ssh, le recours de la pièce après une exception de la mesure (correction sous un nom neuf, mêmes entrées) n'est pas
  praticable sur la machine : la machine est gardée (« noeud ») jusqu'au mot de la mère, puis détruite ; dit à Lazar dans le préavis.
- Elle n'éprouve pas la concurrence réelle chez le fournisseur (vingt sessions à la fois) : l'essai à blanc éprouve le lanceur, non
  la limite réelle ; la ligne « limite de débit » de la liste d'arrêt la garde au premier tour des files.

## 6. Contre-lecture

À faire (R2) : un sous-agent neuf **d'un autre modèle** que l'auteur, qui n'a écrit ni la pièce ni ce code ; fichiers à lui donner :
la pièce qui fera foi et son dernier rapport de contre-lecture ; ce dossier entier (code, essais, sorties gardées, devis, rapport) ;
la procédure v14 du pilote et ses pièces `sans-ssh-v2/`, `sans-ssh-v3/`, `sans-ssh-v4/` (branche `lot/compte-organisme-v1`) ; la
procédure v6 de l'idée 1.1 et son dossier.
