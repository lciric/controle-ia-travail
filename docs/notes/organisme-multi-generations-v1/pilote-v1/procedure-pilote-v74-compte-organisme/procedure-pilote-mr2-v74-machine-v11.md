# Procédure pas à pas du pilote MR-2 sur la machine jetable — code v74, texte scellé candidat 6 — v11 (sans ssh)

- **Auteur** : modèle A (session du compte organisme). **Ce compte ne lance rien** (brief : aucun appel au loueur). Pour la mère, ou
  une session exécutante ouverte dans le dépôt de travail, crochet vérifié chargé (R-2812, option (a)). Jouée seulement après une
  vérification « jouable » du différentiel v10 → v11 (mère) ; le feu est ensuite donné en autonomie (mot de Lazar « go recos tu es en
  autonomie », R-2883), **avec préavis à Lazar au moment de la création**.
- **Pourquoi une v11** : la v10 a été jugée jouable (`verification-courte-procedure-pilote-mr2-v74-machine-v10-et-epreuve-cles-v2-v1.md`,
  `main`, `986a8e3d836cc9b6e4c78ab3f877b8b9dc73ac1bc4b0a562306ab8894cc3f9da` : 0 bloquant, 0 majeur, mineurs q1 à q5 et f1 à f5), mais
  **la session qui lance n'a pas de ssh** (aucun client ni clé ; sortie réseau par le mandataire HTTPS seulement ; connexion directe au
  port 22 refusée ; R-2876, R-2877). Mot de Lazar, verbatim : « (a) : go » (R-2882) : une v11 sans ssh, sur le modèle des courses déjà
  jouées depuis ce conteneur (B bis, `prep/t07bbis-code-v1` à `95cfada6` ; Neuron Lens, `prep/neuron-lens-v1` à `71223541`).
- **Versions** (R12) : v1 à v10 restent en place ; **la v11 remplace la v10 pour l'usage**. Différentiel v10 → v11 déclaré point par
  point, retraits compris, à la section 12 octies.
- **Principe** : chaque geste ssh ou scp de la v10 est remplacé par l'équivalent « amorce + branche ». Une **amorce** est passée à la
  création (base64 dans `--args`) ; elle arme la minuterie de destruction **avant toute passe**, prend au commit le **programme
  machine** et son aide (empreintes exigées), qui jouent sur la machine les sections 3 à 11 de la v10, dans le même ordre et avec les
  mêmes attendus, écrits en programme. **Tout ce qui sort** (états, journaux, empreintes, pièces permises) est poussé par la machine
  sur une **branche neuve de sortie** ; la session lit cette branche, jamais la machine. Aux trois **barrières**, la machine attend un
  **feu** écrit par la mère sur une **branche neuve d'entrée**. Rien de privé ne sort : secret, phrase, clé privée de la phrase,
  mondes, textes servis restent sur la machine et meurent avec elle.
- **Pièces** (dossier `sans-ssh-v1/` à côté de cette procédure, branche `lot/compte-organisme-v1`) :

  | pièce | rôle | empreinte |
  |---|---|---|
  | `amorce_pilote_mr2_v74_v1.sh` | amorce passée à la création (machine) | `81c31613cd895d7b42619c7bc24bb20ff43c22c243125a31bc70a848ef41af34` |
  | `machine_pilote_mr2_v74_v1.sh` | programme machine, sections 3 à 11 de la v10 | `5247414ae93d045a1a3eb2416142f94a57866fa359fb60596668c4a5f8e37ca2` |
  | `machine_pilote_mr2_v74_v1.py` | aide du programme machine (attendus, feux, balayage) | `2d42d69e80fedb7277bdcc528152cb06902a57e1d632e0c864b57b28477e1dcc` |
  | `session_pilote_mr2_v74_v1.sh` | outil de la session (commande imprimée, feux, suivi, destruction) | `b065522e748a82cd1916cc07663fab67f4791c48ff19f05bc02207ca92e982a9` |
  | `session_pilote_mr2_v74_v1.py` | aide de l'outil de la session | `bf868eb9d7a8c63bd4fa5a64694237b91e41f65d3b2bea9c55bce6590c5f203f` |
  | `essais/` | essais à blanc sur dossier jetable (section 13) | voir `essais/LISEZMOI.md` |

- **Fait foi** : le texte scellé `docs/notes/organisme-multi-generations-v1/pilote-v1/preenregistrement-pilote-conditionnelles-v1-candidat6-compte-organisme.md`
  (branche `prep/pilote-mr2-compte-organisme-v1`), `8aa33014667da569ec934459d7bc1b1f6b54efa5c2145a6e5bdce5f7fa74603e`, scellé par la mère
  (R-2809). **Cette procédure ne change rien au texte** ; en cas d'écart, le texte prime et l'écart est un nœud.
- **Lignes** : GO-2026-11-14-13 (π1, 20 USD, crédits de Claude) et GO-2026-11-14-14 (π2, 21.72 USD hors crédits, dont machine 3 USD),
  `main` `20f66b0b`, l. 332-333 (R-2810) ; **GO-2026-11-15-04** (passage des clés à la machine louée, mot de Lazar) ; épreuve des clés :
  GO-2026-11-15-02 étendue par GO-2026-11-15-05 (R-2867), **faite**, code 0, 0,001164 USD (R-2876, R-2877), **ne se rejoue pas**.
- **Instances intouchables** : 58936096, 58936099, 58936100, 60480302, 60599797, 60670453, 60671759 (Neuron Lens), et toute instance ou
  tout serveur que la session qui lance n'a pas créé ; jamais les serveurs `poste-temoin-bailey-*`. **Aucune commande n'en nomme une.**
- **Interdits** : aucune valeur de clé affichée ni écrite dans un dépôt ou un fichier gardé ; jamais `env`, `printenv`, `set` sans
  argument, `export -p`, `/proc/*/environ` ; aucune heure écrite à la main (`date -u` dans la même commande) ; arrêts par identifiant
  (R10) ; aucun refus de permission, du crochet ou d'un classifieur contourné ni rejoué ; **jamais `git fetch` sans refspec**.

## 0. Notations

**Session qui lance** (sous **bash**). Chaque commande commence par

```
ENV=/home/user/pilote-mr2-v74-envoi-v11; : "${ENV:?}"; cd "$ENV" 2>/dev/null; test -e "$ENV/variables.sh" && . "$ENV/variables.sh"
```

- `W=/home/user/controle-ia-travail` (dépôt de travail) ; `ENV` : dossier d'envoi **neuf** (R12 ; celui de la v10,
  `/home/user/pilote-mr2-v74-envoi`, porte l'épreuve des clés faite et reste en place), **hors de tout dépôt**.
- `"$ENV/variables.sh"` : seules valeurs non secrètes qui survivent (`CL`, `CP`, `CM`, `BS`, `BE`, `ETIQ`, `OUTIL`), **écrites par
  programme** à la section 1, jamais tapées ; aucune clé n'y entre.
- `CL` : le commit de `lot/compte-organisme-v1` qui porte ce dossier aux empreintes ci-dessus (**donné par le compte organisme dans son
  message de remise**) ; `CP` : sommet de `prep/pilote-mr2-compte-organisme-v1` ; `CM` : sommet de `main` (qui porte
  GO-2026-11-14-13 et -14) au moment de la section 1.
- `BS=calcul/pilote-mr2-v74-sortie-v1` (branche de sortie, écrite par la machine seule) ; `BE=calcul/pilote-mr2-v74-entree-v1` (branche
  d'entrée, écrite par la mère seule) ; les deux **absentes avant la création** (contrôlé par l'outil, puis par la machine).
- `OUTIL` = `env W=/home/user/controle-ia-travail ENVP=$ENV bash $ENV/outil/session_pilote_mr2_v74_v1.sh` (copie prise au commit `CL`).
  Codes de l'outil : 0 accepté ; 2 refus nommé.
- `ID` : identifiant de la machine, écrit une fois par l'outil dans `"$ENV/identifiant.txt"`, jamais retapé.
- **Les clés passent par `--env` à la création** (GO-2026-11-15-04). Conséquence, dite : la configuration de l'instance chez le loueur
  porte leurs valeurs jusqu'à la destruction, et **la liste `show instances --raw` peut les porter** (champ de configuration de
  l'instance ; non vérifié, tenu pour vrai). Toute lecture de cette liste passe donc par
  l'outil (écriture sous `umask 077` dans un dossier jetable, champs utiles lus par programme, fichier supprimé aussitôt) ; **aucune
  sortie brute de `show instances` n'est gardée ni affichée** (la v10 en gardait dans `$ENV`).

**Machine** : `/root/pilote` (racine, hors de tout dépôt) ; `prive/` (0700 : secret, phrase, clé privée de la phrase, mondes) ;
`depot/` (copie partielle du dépôt de travail aux commits `CL`, `CP`, `CM`, extraction limitée au paquet et à la sonde) ; `arbre/`
(arbre de l'organisme, tête 605e0f6) ; `sortie/` (liste blanche, copiée sur `BS`).

**Ce que pousse la machine sur `BS`** (et rien d'autre) : `etat.txt` (étape, motif, heures, échéance, PID de la minuterie, clés, `H`,
codes, fichiers exclus par le balayage) ; `journal-machine.txt` ; les journaux et codes de chaque étape (`journal-NN-*.txt`,
`code-NN-*.txt`, ceux que la v10 rapatriait) ; `mise-en-place.txt` ; `secret-sha256.txt` ; `cle-publique-phrase.pem` et son
empreinte ; `phrase-sha256.txt` ; `engagement-mondes.json` ; `rapatrie-blanc/` et `rapatrie-reel/` (sorties de `rapatrier`,
`"aucun_monde": true` exigé) ; `lancements.jsonl` ; `remis-au-sous-agent/sortie-lire-non-ouverte.txt`. Avant chaque poussée, un
**balayage** cherche dans chaque fichier le jeton, les trois clés (brutes, en URL, en base64), le secret (brut, hexadécimal, base64) et
la phrase (si au moins 8 octets) : un fichier où une forme est trouvée est **exclu de toute poussée**, nommé dans `etat.txt`
(`exclus_balayage=`) et dans le journal (jamais la valeur), le reste rebalayé puis poussé. Aucun fichier de plus de 95 Mo.

**États de la machine** (`etape=` dans `etat.txt`, lus par `$OUTIL etat $BS`) : `mise en place` → `pieces et arbre` → `secret` →
`attente du feu 1 (phrase)` → `mondes` → `attente du feu 2 (mondes)` → `preparer` → `essai a blanc` → `attente du feu 3 (pilote
reel)` → `jouer reel en cours` (et `attente du feu de relance (reel-2)`, `jouer reel-2 en cours`) → `mesure` → `rapatriement` →
**finales** : `fini`, `fini, poussee finale en echec`, `arret (A)`, `noeud, machine gardee`, `sortie inattendue`. Dans un état final,
la machine ne fait plus rien : elle attend la destruction (par la session, ou par la minuterie à l'échéance).

**Arrêt commun (A)** — côté machine, il est joué par le programme lui-même sur toute cause d'arrêt (refus d'un attendu, feu manquant à
l'échéance d'une barrière, feu d'arrêt, code 3, code inattendu avec lancement consigné) : (1) cause écrite ; (2) clés jamais plus
transmises à aucun processus, effacées du programme après la dernière poussée ; (3) rapatriement du dossier réel s'il existe (y compris
après un code 3 : `CARTES-partiel.json`, pièce permise) ; (4) traces poussées ; (5) attente de la destruction. **Côté session**, toute
cause d'arrêt vue par la session (heure limite, dépense, refus d'outil, état illisible) : (1) écrire la cause (`date -u`) ; (2)
`$OUTIL feu-arret $BE "CAUSE"` (la machine le lit à chaque attente et pendant `jouer` réel, où elle arrête le pilote **par son PID**,
R10) ; (3) attendre l'état final (`$OUTIL etat $BS`, quelques minutes) ; (4) `$OUTIL recuperer $BS "$ENV/retour"` ; (5) détruire
(section 11) ; (6) nœud à la mère. **Exception** (inchangée) : entre un `jouer` réel réussi et la mesure faite, **aucun feu d'arrêt**
(la machine ne le lit pas pendant la mesure ; un code inattendu mène à « noeud, machine gardee »). Après un code 3 de `jouer` ou de
`mesurer` : **ni relance, ni mesure, ni lecture d'issue, pas même P-0**. **Refus d'un outil, du crochet ou d'un classifieur** à toute
étape après la location : ni rejoué, ni reformulé, ni confié à une autre session ; nœud immédiat à la mère (identifiant, étiquette,
prix horaire, heure de création, étape du refus) ; la machine reste louée jusqu'au mot de la mère, au plus jusqu'à l'échéance de la
minuterie ; aucune création entre-temps.

**« Noeud, machine gardee »** : comme en v10, aucune relance ni arrêt (A) sans le mot de la mère ; **sans ssh, rien d'autre que la
destruction n'est possible** sur une machine gardée (les traces sont déjà poussées ; les mondes ne quittent jamais la machine) : le
mot de la mère porte donc sur le moment de la destruction (au plus l'échéance de la minuterie).

**« Aucun `jouer` ne tourne »** se constate par l'état poussé : `etape=` autre que `jouer reel en cours` et `jouer reel-2 en cours`.
Pendant `jouer`, la machine pousse son état toutes les 15 minutes ; **un état « jouer … en cours » vieux de plus de 40 minutes**
(`heure=` de `etat.txt`) vaut « constat illisible » : nœud à la mère, sans feu d'arrêt sur ce seul constat.

**Échéance et heure limite** : l'échéance de la **minuterie** est écrite par l'outil dans `"$ENV/echeance.txt"` (14 h 40 après
l'impression de la commande ; à 0,20 USD/h au plus, 2,93 USD, sous la part machine de 3 USD). À l'échéance, la minuterie de la machine
demande sa destruction **sans condition** (DELETE répété, puis « stopped » ; jamais jugé par un code ; l'absence est prouvée par la
session, section 11). **Une heure avant** : nœud à la mère ; si un `jouer` tourne, nœud à Lazar par la mère, **en sachant que la
minuterie détruira à l'échéance** (aucune prolongation n'est possible sans ssh). **À 2,70 USD dépensés sur la machine** (prix ×
durée) : nœud à la mère. Avant le pilote réel, la machine exige **au moins 12 h 30** avant l'échéance (pire cas de `jouer`, 4 × 10 800 s,
plus mesure, rapatriement et poussée), sinon arrêt (A) **sans aucun appel** : la réponse aux feux doit être prompte (section 6).

## 1. Pièces à préparer (session qui lance, aucune dépense)

```
W=/home/user/controle-ia-travail; ENV=/home/user/pilote-mr2-v74-envoi-v11; : "${ENV:?}"
test ! -e "$ENV" && mkdir "$ENV" && cd "$W" && git fetch origin +refs/heads/main:refs/remotes/origin/main \
  +refs/heads/lot/compte-organisme-v1:refs/remotes/origin/lot/compte-organisme-v1 \
  +refs/heads/prep/pilote-mr2-compte-organisme-v1:refs/remotes/origin/prep/pilote-mr2-compte-organisme-v1
CL=COMMIT_DONNÉ_PAR_LE_COMPTE_ORGANISME     # 40 caractères ; puis :
git -C "$W" merge-base --is-ancestor "$CL" refs/remotes/origin/lot/compte-organisme-v1 && echo "CL sur la branche du lot"
DC=docs/notes/organisme-multi-generations-v1/pilote-v1/procedure-pilote-v74-compte-organisme/sans-ssh-v1
mkdir "$ENV/outil" && git -C "$W" archive "$CL" "$DC" | tar -x -C "$ENV/outil" --strip-components=6
(cd "$ENV/outil" && sha256sum -c - <<'X'
81c31613cd895d7b42619c7bc24bb20ff43c22c243125a31bc70a848ef41af34  amorce_pilote_mr2_v74_v1.sh
5247414ae93d045a1a3eb2416142f94a57866fa359fb60596668c4a5f8e37ca2  machine_pilote_mr2_v74_v1.sh
2d42d69e80fedb7277bdcc528152cb06902a57e1d632e0c864b57b28477e1dcc  machine_pilote_mr2_v74_v1.py
b065522e748a82cd1916cc07663fab67f4791c48ff19f05bc02207ca92e982a9  session_pilote_mr2_v74_v1.sh
bf868eb9d7a8c63bd4fa5a64694237b91e41f65d3b2bea9c55bce6590c5f203f  session_pilote_mr2_v74_v1.py
X
) && { printf 'CL=%s\nCP=%s\nCM=%s\n' "$CL" "$(git -C "$W" rev-parse refs/remotes/origin/prep/pilote-mr2-compte-organisme-v1)" \
  "$(git -C "$W" rev-parse refs/remotes/origin/main)"; printf 'BS=calcul/pilote-mr2-v74-sortie-v1\nBE=calcul/pilote-mr2-v74-entree-v1\n'
  printf 'OUTIL="env W=%s ENVP=%s bash %s/outil/session_pilote_mr2_v74_v1.sh"\n' "$W" "$ENV" "$ENV"; } > "$ENV/variables.sh"
```

Attendu : « CL sur la branche du lot », cinq `OK`. **Arrêt** (rien n'est loué) sur tout écart.

**Contrôles qui ne coûtent rien, faits ici et non après la location** (inchangés, plus le jeton des machines) :

```
: "${RR_ANTHROPIC_API_KEY_RIGAUD:?}" "${GEMINI_API_KEY:?}" "${OPENAI_API_KEY:?}" "${CONTROLE_IA_GITHUB_TOKEN_2:?}"   # noms présents ; rien n'est affiché
ENV=/home/user/pilote-mr2-v74-envoi-v11; . "$ENV/variables.sh"; P=docs/notes/organisme-multi-generations-v1/pilote-v1
git -C /home/user/controle-ia-travail show "$CL:$P/procedure-pilote-v74-compte-organisme/arbre-organisme-complet-605e0f6.bundle" > "$ENV/arbre-organisme-complet-605e0f6.bundle"
git -C /home/user/controle-ia-travail show "$CM:registres/go.md" > "$ENV/go-main.md"
echo "e3d83e47a06b2941c54240b96612cb17880fe4162e7822a2eb02ebac64c785b1  $ENV/arbre-organisme-complet-605e0f6.bundle" | sha256sum -c - \
&& mkdir "$ENV/arbre-local" && cd "$ENV/arbre-local" && git init -q \
  && git bundle unbundle ../arbre-organisme-complet-605e0f6.bundle > /dev/null && git checkout -q 605e0f60f3eed0948948e6a4eb15cb73de1d03de
cd "$ENV/arbre-local/orchestrator" && env -i PATH=/usr/local/bin:/usr/bin:/bin HOME=/root python3 -I -B -c '
import sys; sys.path.insert(0, ".")
from pole import proposeurs_pilote_v72 as PC, proposeurs_pilote_v70 as PR
from demonstrations import pilote_mr2_v74 as L
conf, _ = PC.lire_configuration(L.CONFIGURATION)
PR.lire_go_du_pilote(conf, sys.argv[1], "GO-2026-11-14-13", "GO-2026-11-14-14"); print("lignes du pilote lues au montant exact")' "$ENV/go-main.md"
```

Un nom absent, ou les lignes refusées par le lecteur gelé : **arrêt, rien n'est loué**, nœud. (La machine relit elle-même les pièces
aux commits `CL`, `CP`, `CM` et exige les empreintes du paquet, du texte et du relevé, section 4 de la v10.)

**Épreuve des trois clés** : **faite** depuis la session qui lance, sous GO-2026-11-15-05 (R-2867), code 0, dépense 0,001164 USD
(R-2876, R-2877) ; **elle ne se rejoue pas** ; sa sortie (`/home/user/pilote-mr2-v74-envoi/epreuve-cles.json`) porte les identifiants
servis : rien n'en est recopié dans un registre de `main` (R-2731, rappel q5). Ce qu'elle ne couvre pas reste dit à la section 7.

## 2. Location (session qui lance ; GO-2026-11-14-14, part machine 3 USD) — une seule machine

1. Crochet `garde_calcul.py` chargé et éprouvé (cas sain et artefact, R5) ; sinon arrêt. Toute commande qui porte `vastai create`
   cite `GO_ID=GO-2026-11-14-14` en tête de ligne.
2. **Crédit** : `$OUTIL credit` (champ `credit` seul, au moins 5 USD) ; moyen de paiement actif constaté par la mère à l'interface ;
   consignés (`date -u`) ; sinon aucune création, nœud.
3. **Inventaire avant**, avec témoin : `$OUTIL inventaire avant` (identifiants seuls dans `ids-avant.txt` ; liste vide refusée).
4. **Étiquette**, une fois : `test ! -e "$ENV/etiquette.txt" && echo "pilote-mr2-v74-$(date -u +%Y%m%d)" > "$ENV/etiquette.txt" && echo "ETIQ=$(cat "$ENV/etiquette.txt")" >> "$ENV/variables.sh"`.
5. **Recherche d'offres** (lecture seule ; aucune clé dans une offre) :
   `/home/user/vastai-env/bin/vastai search offers 'num_gpus=0 cpu_cores_effective>=4 cpu_ram>=8 disk_space>=20 dph_total<=0.2' -o 'dph_total' --raw > "$ENV/recherche.json"` ;
   l'offre est **choisie à la main** (la moins chère conforme) ; `$OUTIL offre "$ENV/recherche.json" OFFRE` la contrôle par programme
   (processeurs seuls, au moins 4 processeurs, 8 Go, 20 Go de disque, prix total au plus 0,20 USD/h). Aucune offre conforme : nœud.
6. **Commande de création**, imprimée par l'outil après tous ses contrôles :
   `$OUTIL commande "$ENV/recherche.json" OFFRE "$CL" "$CP" "$CM" "$BS" "$BE" "$ETIQ"` — l'outil refuse si : l'offre sort des bornes ;
   un commit manque ; l'amorce du commit `CL` diffère de sa copie ; la ligne GO-2026-11-14-14 manque au registre de `CM` ; `BS` ou `BE`
   existe déjà sur le dépôt distant ; un des quatre noms (`CONTROLE_IA_GITHUB_TOKEN_2` et les trois clés) manque ou n'a pas une forme
   passable par `--env` (lettres, chiffres, `_`, `-`, contrôlé sans rien afficher) ; l'amorce refuse ses arguments (essai des
   arguments, sans réseau ni dossier) ; `echeance.txt` existe déjà avec une autre échéance (une commande déjà imprimée : ne jamais
   créer deux fois). Il imprime l'offre, le prix, l'échéance, les débuts des empreintes, puis **deux lignes à jouer comme une seule
   commande** : la première pose `GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN_2"` (affectation séparée, jamais le jeton de session), `ENVP`
   et `umask 077` ; la seconde commence par `GO_ID=GO-2026-11-14-14 /home/user/vastai-env/bin/vastai create instance OFFRE --raw
   --image python:3.13-bookworm --disk 20 --cancel-unavail --label ETIQ --env "…"`, avec les **noms** des clés (`$GH_TOKEN`,
   `$RR_ANTHROPIC_API_KEY_RIGAUD`, `$GEMINI_API_KEY`, `$OPENAI_API_KEY`), développés par l'interpréteur au moment de la création,
   jamais leurs valeurs écrites ; l'amorce en base64 ; la sortie dans `"$ENVP/creation.json"` (0600) et `code=…`.
   **Préavis à Lazar** au moment de la création (mère). La session joue les deux lignes telles qu'imprimées (préambule de la section 0
   devant), **une seule fois** ; si la commande ne rend pas la main ou dépasse son délai : **ne jamais la rejouer** ; passer au point 7.
7. **Identifiant** : `$OUTIL creation` (lit `new_contract`, supprime `creation.json` sans l'afficher, écrit `identifiant.txt` une
   fois) ; **repli** si la sortie n'a pas `new_contract` lisible : `$OUTIL trouver "$ETIQ"` (une seule instance de l'étiquette). Puis
   `date -u +%Y-%m-%dT%H:%M:%SZ > "$ENV/heure-creation.txt"` ; consigner identifiant, étiquette, prix horaire, heure de création,
   échéance (`echeance.txt`).
8. **Inventaire après** : `$OUTIL inventaire apres-creation` puis `$OUTIL ajoute` (seule instance ajoutée, égale à l'identifiant ;
   toutes les autres toujours listées) ; `$OUTIL relire "$ETIQ"` (étiquette, prix au plus 0,20 USD/h ; hors borne : détruire aussitôt,
   section 11).
9. **Aucune seconde création** tant que l'absence de la première n'est pas prouvée (section 11).

## 3. Mise en place (sur la machine, par l'amorce et le programme machine ; aucune dépense de fournisseur)

La session suit par `$OUTIL etat "$BS"` (état et fin du journal de la machine), toutes les quelques minutes. Ce que fait la machine,
sans geste de la session :

- **Amorce** : arguments contrôlés (commits de 40 caractères, empreintes de 64, `GO_ID` égal à GO-2026-11-14-14, branches `calcul/…`
  distinctes, échéance dans les 14 h 45, identifiant de l'instance, quatre valeurs présentes et de forme lisible, outils présents :
  git, curl, python3, openssl, …) ; **un refus avant la minuterie demande la destruction de l'instance par elle-même** (DELETE trois
  fois, puis « stopped », jamais jugé ; la session prouve l'absence) ; **minuterie armée** ; dépôt partiel aux trois commits ;
  programme machine et aide pris au commit `CL`, **empreintes exigées** ; puis la main passe au programme machine (même PID).
- **Relance du conteneur par le loueur** (marque `amorce-lancee` présente) : minuterie réarmée à la même échéance, **aucune passe
  refaite** (ni `generer`, ni `jouer`), arrêt (A) poussé.
- **Programme machine** : `BS` absente (sinon arrêt sans poussée, R12 : lisible par `vastai logs ID`), `BE` absente (sinon arrêt (A) :
  un feu ancien serait lu), première poussée (`mise en place`) ; numpy 2.5.3 installé (`pip`, 900 s au plus) ; contrôle
  `(3, 13) 2.5.3` dans le chemin réduit de `O` ; version de git.

**Attente bornée** : si `BS` n'est pas poussée **20 minutes** après la création (`$OUTIL etat "$BS"` rend « pas encore poussée ») :
lire `vastai logs ID` (lecture seule ; aucune valeur secrète n'y est écrite) ; puis arrêt (A) côté session (la machine n'a rien à
pousser : destruction directe, section 11).

## 4. Arbre et bloc gelé (sur la machine)

Extraction partielle limitée au paquet et au dossier de la sonde (aucun `runs/`, `diag/`, `donnees/`, `essai/`, `registres/` dans
l'arbre extrait, sinon arrêt (A)) ; texte scellé pris à `CP`, registre des lignes pris à `CM` ; empreintes exigées : paquet
`e3d83e47…`, texte `8aa33014…`, relevé `f56d9c0e…` et son compagnon ; quatre dossiers de relais ; dépaquetage, tête `605e0f6`, arbre
propre ; `bloc --releve-sonde` code 0 et **bloc égal à l'octet** à celui du texte scellé. Arrêt (A) sur tout écart. Journal :
`journal-04-pieces.txt`, `journal-04-bloc.txt`.

## 5. Secret, puis phrase de Lazar (barrière 1)

La machine tire le secret (`secret`, code 0, une seule clé `secret_sha256`), crée **sur la machine** une paire de clés RSA de
4096 bits pour la phrase (privée dans `prive/`, 0600), pousse `secret-sha256.txt`, `cle-publique-phrase.pem` et son empreinte, et passe
à `attente du feu 1 (phrase)`. Puis, dans cet ordre :

1. La mère **inscrit l'empreinte du secret** (lue dans `secret-sha256.txt` de `BS`) sur `main`, dans un fichier qu'elle nomme, et la
   pousse ; elle note le commit (`COMMIT_INSCRIPTION`) et le chemin (`CHEMIN_INSCRIPTION`).
2. **Ensuite seulement**, Lazar donne sa phrase. Elle est écrite par la session dans un fichier privé, par un document au délimiteur
   entre guillemets (rien n'est développé), jamais en argument :

   ```
   ( umask 077; cat > "$ENV/phrase.txt" ) <<'PHRASE'
   (la phrase de Lazar, une ligne, non vide, sans octet nul, au plus 400 octets)
   PHRASE
   ```

3. `$OUTIL feu-phrase "$BS" "$BE" "$ENV/phrase.txt" COMMIT_INSCRIPTION CHEMIN_INSCRIPTION` : l'outil exige l'état
   `attente du feu 1 (phrase)`, l'empreinte du secret de `BS` présente dans le fichier inscrit au commit, ce commit ancêtre de `main`,
   la forme de la phrase, la clé publique égale à son empreinte poussée ; il **chiffre la phrase par la clé publique de la machine**
   (RSA-OAEP, SHA-256), pousse sur `BE` `phrase-chiffree.b64` et `feu-1-phrase.txt` (empreinte du secret, **empreinte du fichier de la
   phrase**, commit et chemin de l'inscription), imprime l'empreinte du fichier de la phrase, puis **efface le fichier de la phrase**
   (`shred -u`).
4. La mère **inscrit l'empreinte du fichier de la phrase** (retour à la ligne final compris ; `generer` le retire à la lecture).
5. La machine lit le feu (**au plus une heure après son départ**, comme la v10 : sinon arrêt (A)), revérifie l'inscription du secret
   sur `main` (commit ancêtre de `main`, empreinte dans le fichier), déchiffre, contrôle la forme et **l'empreinte du fichier déchiffré,
   égale à celle du feu** (sinon arrêt (A)), **efface la clé privée** (`shred -u`), pousse `phrase-sha256.txt`.

**La phrase n'est jamais écrite en clair dans un dépôt** : seul son chiffré passe sur `BE` ; la clé privée qui le lit naît et meurt
sur la machine, effacée dès la lecture. Elle passe, comme en v10, dans le journal de la session qui lance, qui n'est pas publié. **Le
texte scellé dit « jamais publiés (ni secret, ni phrase, ni devis) »** : un chiffré sur une branche privée du dépôt de travail n'est
pas une publication de la phrase ; **lecture à confirmer par la mère** (recommandation : la tenir pour permise, confiance haute ; si la
mère la juge contraire au texte, c'est un nœud de Lazar avant toute location). Le secret existe déjà : arrêt (A) (le lanceur refuse
d'écraser).

## 6. Mondes (barrière 2), C-16 et C-17, essai à blanc (barrière 3)

- **Mondes** (≈ 12 min sur 4 processeurs) : `generer` ; code 0, quatre mondes « conforme » vrais, `H` et `S1` à `S4` lus par programme
  dans l'engagement (jamais tapés) ; `engagement-mondes.json` poussé ; état `attente du feu 2 (mondes)`. Arrêt (A) si un monde n'est pas
  conforme ou si le code n'est pas 0 (une graine neuve demande un texte neuf et le mot de Lazar).
- **Barrière 2** : la mère **inscrit `H` et `S1` à `S4`** au registre (`main`), puis
  `$OUTIL feu-mondes "$BS" "$BE" COMMIT_INSCRIPTION CHEMIN_INSCRIPTION` (l'outil exige les cinq empreintes dans le fichier inscrit, le
  commit ancêtre de `main`). La machine revérifie, **20 minutes au plus** après la poussée de l'engagement, sinon arrêt (A).
- **C-16 et C-17** : `preparer` ; code 0 ; clés `c16`, `c17`, `episodes_servis`, `gabarit_sha256`, `heritages_sha256`, `mondes`,
  `textes_servis` ; toutes les lois de C-16 « admise » vraie ; `gabarit_sha256` = `e77d3041…`. Arrêt (A) sinon.
- **Essai à blanc** : `jouer --mode a_blanc` (`"mode": "a_blanc"`, comptes 16/0/0, `"arret": null`), puis `rapatrier`
  (`"aucun_monde": true`), poussés ; **ni `mesurer` ni `lire` sur `blanc/`** ; aucun `blanc-2`. Arrêt (A) sinon. État
  `attente du feu 3 (pilote reel)`.
- **Barrière 3** : la mère lit l'état et `journal-08-blanc.txt` sur `BS`, puis `$OUTIL feu-reel "$BS" "$BE"` (feu portant `H` et les
  lignes GO-2026-11-14-13 et -14). La machine l'attend **20 minutes au plus**, sinon arrêt (A).

## 7. Pilote réel (une seule fois)

**Contrôles juste avant**, joués par la machine : dossier `reel/` et registre des lancements absents ; numpy 2.5.3 ; empreintes du texte
et du relevé ; ports 8811 à 8814 libres ; les trois fournisseurs joignables (poignée TLS seule, aucune clé) ; **au moins 12 h 30 avant
l'échéance** ; trois clés présentes. Arrêt (A) sur tout écart, sans aucun appel.

**Clés** : passées à la création (GO-2026-11-15-04), gardées dans des variables du programme machine, retirées de l'environnement de
tout autre processus ; **seul `jouer` réel les reçoit**, par `env -i` ; **aucune n'est jamais écrite sur le disque** (la v10 écrivait
`prive/cles.env`, puis l'effaçait). Après `jouer`, elles ne sont plus transmises à aucun processus, sauf le balayage, qui les cherche
dans les fichiers à pousser ; elles sont effacées du programme après la dernière poussée. **Exposition restante, dite** : la
configuration de l'instance chez le loueur et l'environnement du processus d'entrée du conteneur les portent jusqu'à la destruction
(l'amorce ne lance aucun service ; la création ne demande ni ssh ni port ouvert). **Risque restant sur leur validité** (texte de la v10,
inchangé) : l'épreuve des clés (section 1) ne couvre pas un changement de clé depuis l'épreuve, le modèle de `fable52` (même clé, autre
modèle), le réglage `output_config`, un quota suffisant pour un appel du pilote, ni le chemin de réseau de la machine louée ; la clé du
premier fournisseur sert deux proposeurs sur quatre (8 appels sur 16) : invalide seule, elle mène à P-0 pendant que les appels des deux
autres fournisseurs sont payés (jusqu'à 9,36 USD chacun) ; la clé du deuxième ou du troisième fournisseur, invalide seule, laisse
exactement le minimum (12 sur 16, 3 par monde), sans marge.

**Lancement** : `jouer --mode reel … --go-pi1 GO-2026-11-14-13 --go-pi2 GO-2026-11-14-14 --registre-go go-main.md --texte texte.md
--texte-sha256 8aa33014… --mondes-shas S1,S2,S3,S4 --registre-lancements lancements.jsonl --releve-sonde …` (mêmes arguments que la
v10), lancé en arrière-plan par le programme machine, **son PID gardé** ; état `jouer reel en cours` poussé au lancement (c'est
l'équivalent du « lancé » de la v10 : le nom `reel` est écrit une fois, `reel-nom.txt`), puis toutes les 15 minutes. Un feu d'arrêt
lu pendant `jouer` arrête le pilote **par son PID** (R10), puis arrêt (A). **Les relais sont lancés par le lanceur avec leur part comme
plafond** (parts 12, 8, 9,36, 9,36 USD).

**Issues de `jouer`** (jouées par la machine ; la session lit `code_jouer=` et le motif dans l'état) :
- **code 0** : sortie contrôlée (`"mode": "reel"`, 16 appels comptés, `"arret": null` ; un fournisseur en panne donne des appels
  « echec », code 0, **sans reprise** ; le minimum de 12 sur 16 et de 3 par monde décide de P-0 à la lecture) → section 8. Code 0 avec
  une autre sortie : « noeud, machine gardee ».
- **code 2** : si **`lancements.jsonl` existe** : arrêt (A). S'il est **absent** (aucun appel parti) : état `attente du feu de relance
  (reel-2)`, clés gardées dans le programme ; la mère lit `journal-09-reel.txt` (le refus nommé), et **seulement si ce que le refus nomme
  est levé sans toucher ni au code ni au texte ni à la machine** (sans ssh, rien d'autre ne peut être corrigé), donne
  `$OUTIL feu-relance "$BS" "$BE" "CAUSE"` dans les **20 minutes** ; sinon `$OUTIL feu-arret "$BE" "CAUSE"` (ou rien : arrêt (A) à 20
  minutes). Une seule relance, **toujours sous `reel-2`** : journal et code du premier essai renommés `…-essai1`, contrôles juste avant
  rejoués (dossier `reel-2/` et registre absents ; `reel/` du premier essai reste en place, jamais rapatrié), puis `jouer` sous
  `reel-2` ; **tous les noms suivants sont ceux en `-2`**. **Un second code 2** : arrêt (A).
- **code 3** : arrêt (A), nœud de Lazar ; toute reprise demande un texte neuf et des mondes neufs.
- **tout autre code** (1, 126, 127, 137…) : si `lancements.jsonl` existe : arrêt (A) ; s'il est absent : « noeud, machine gardee ».

## 8. Mesure (une seule fois), puis lecture par un sous-agent neuf

Joué par la machine après un code 0 contrôlé : `mesurer` une seule fois (`programme_sha256` = `676d5f37…`). **code 3** : arrêt (A).
**Tout autre code non nul**, ou programme inattendu : présence d'une sortie de mesure constatée (`journal-10-mesure-presente.txt`),
puis « noeud, machine gardee » (**ni relance ni arrêt (A) sans le mot de la mère** ; les mondes ne quittent jamais la machine). Puis
`lire --sortie REEL --ecrire REEL/lecture-pilote-v70.json`, **sortie non affichée** : elle va dans `sortie-lire-non-ouverte.txt`,
poussée sous `remis-au-sous-agent/` ; **la session qui lance ne l'ouvre pas** ; un code non nul de `lire` : « noeud, machine gardee »
(le fichier est remis tel quel). `REEL/lecture-pilote-v70.json` est rapatrié (section 9), comparé à son compagnon par la machine
(`journal-11-compagnon-lecture.txt`), et remis, avec le texte scellé, à un **sous-agent neuf** (ni auteur du texte ni de l'analyse),
qui applique les critères gelés (« Règle », « Plan d'analyse », R13) ; son verdict est scellé, puis soumis à Lazar.

## 9. Rapatriement et dépense

Sur la machine : `rapatrier --source REEL --destination rapatrie-reel --mondes … --mondes-sha256 H` (`"aucun_monde": true` exigé ; sinon
`rapatrie-reel` retiré, rien n'en sort, « noeud, machine gardee ») ; **jamais** rapatriés : `prive/` (secret, phrase, mondes),
`REEL/prive/` et `reel/prive/` d'un premier essai (textes servis). Poussée finale, état `fini`. Si la poussée finale échoue : état local
`fini, poussee finale en echec` (lisible par `vastai logs ID`) : **nœud, ne pas détruire sans la mère** (les résultats ne sont que sur
le disque de la machine).

Côté session : `$OUTIL recuperer "$BS" "$ENV/retour"` (copie hors dépôt du sommet de `BS` ; `remis-au-sous-agent/` **non ouvert**) ;
`(cd "$ENV/retour/rapatrie-reel" && sha256sum -c lecture-pilote-v70.json.sha256)` (comparé, non ouvert) ; verser sur une branche de
travail, **jamais `main`** (réponses brutes : identifiants servis, R-2731) ; `BS` elle-même n'est jamais fusionnée dans `main`.
Dépense : par relais, depuis le relevé du pilote, rapprochée des journaux des relais ; machine : prix horaire × durée ; proposée à la
mère, **avec la dépense de l'épreuve des clés** (0,001164 USD, q2) ; montants facturés : console de Lazar (R-2803) ; une dépense
d'épreuve tirée d'appels jamais partis serait une borne, non une dépense (f4).

## 10. Feux de la mère : récapitulatif

| feu | quand (état de la machine) | commande | délai de la machine |
|---|---|---|---|
| 1, phrase | `attente du feu 1 (phrase)`, après l'inscription du secret puis la phrase de Lazar | `$OUTIL feu-phrase "$BS" "$BE" "$ENV/phrase.txt" COMMIT CHEMIN` | 1 h après le départ de la machine |
| 2, mondes | `attente du feu 2 (mondes)`, après l'inscription de `H`, `S1` à `S4` | `$OUTIL feu-mondes "$BS" "$BE" COMMIT CHEMIN` | 20 min |
| 3, réel | `attente du feu 3 (pilote reel)`, essai à blanc lu | `$OUTIL feu-reel "$BS" "$BE"` | 20 min |
| relance | `attente du feu de relance (reel-2)` | `$OUTIL feu-relance "$BS" "$BE" "CAUSE"` | 20 min |
| arrêt | toute étape, sauf entre un `jouer` réel réussi et la mesure faite | `$OUTIL feu-arret "$BE" "CAUSE"` | lu à chaque attente et toutes les minutes pendant `jouer` |

Un feu mal formé est refusé par la machine (motif au journal), qui continue d'attendre jusqu'à son délai : la mère peut pousser un feu
corrigé. **Si la poussée sur `BE` est refusée** (mandataire de la session, droits) : nœud, sans contournement.

## 11. Destruction

Identifiant relu dans `"$ENV/identifiant.txt"`, jamais retapé ; chaque étape conditionne la suivante :

1. `$OUTIL detruire "$ETIQ"` : instance présente avec l'étiquette de la création (sinon **aucune destruction**, nœud) ; inventaire
   avant destruction (`ids-avant-destruction.txt`, identifiants seuls) ; imprime `GO_ID=GO-2026-11-14-14 /home/user/vastai-env/bin/vastai destroy instance ID -y`.
2. La session joue cette ligne.
3. `$OUTIL verifier-destruction` : **l'absence est prouvée seulement** si `ID` manque à la liste relue sans erreur **et** si toute autre
   instance listée avant l'est encore (témoins, sans nommer aucune intouchable) ; jamais par le code de sortie de l'outil. Témoin vide :
   nœud, ou preuve par la console du loueur. `ID` encore listé : recommencer par ce seul identifiant, puis revérifier.
4. Consigner identifiant, étiquette, heure (`date -u`), résultat. Aucune nouvelle création avant cette preuve.

Si la minuterie a déjà détruit la machine (échéance atteinte), l'étape 1 rend « instance absente » : passer à l'étape 3, qui prouve
l'absence.

## 12. … 12 septies. Différentiels des versions précédentes

Textes de la v10, inchangés (sections 12 à 12 septies de la v10, `28a83444…`).

## 12 octies. Différentiel v10 → v11, point par point, retraits compris (pas de ssh dans la session qui lance, R-2877 ; mot de Lazar « (a) : go », R-2882 ; vérification de la v10, `986a8e3d…`)

| point | où (v10 → v11) | changement en v11 |
|---|---|---|
| pas de ssh (R-2877, R-2882) | 0, 3 à 11 | **retrait** de tout geste `ssh` et `scp`, du fichier `ssh_config`, de l'attente de montage ssh (`ssh_host`, `ssh_port`, sept commandes de trois tours), de l'acceptation de la clé d'hôte ; remplacés par l'amorce passée à la création, le programme machine, la branche de sortie `BS` et la branche d'entrée `BE` |
| ordre et attendus des sections 3 à 11 | 3 à 9 | **inchangés** : mêmes étapes, mêmes commandes du lanceur, mêmes arguments, mêmes attendus, mêmes conduites sur chaque code ; ils sont écrits en programme (`machine_pilote_mr2_v74_v1.sh`, `.py`) au lieu d'être lus par la session |
| barrières | 5, 6, 10 | trois feux de la mère sur `BE` : phrase (après l'inscription du secret), mondes (après l'inscription de `H`, `S1` à `S4`), réel (après l'essai à blanc lu) ; **nouveau** : le feu réel est une barrière explicite (en v10, la même session enchaînait les sections 8 et 9) |
| phrase de Lazar | 5 | **retrait** de l'envoi par l'entrée de ssh ; chiffrée par une clé publique née sur la machine, chiffré poussé sur `BE`, clé privée effacée dès la lecture ; empreinte du fichier comparée par la machine ; fichier de la session effacé par l'outil ; **lecture du texte scellé (« jamais publiés ») soumise à la mère** |
| inscription prouvée par la machine | 5, 6 | **nouveau** : la machine exige que le commit d'inscription soit ancêtre de `main` et que le fichier inscrit porte les empreintes (secret ; `H`, `S1` à `S4`) avant d'aller plus loin |
| clés | 0, 7 | **retrait** de `printf %q … \| ssh … cles.env` et de `shred -u prive/cles.env` ; clés par `--env` à la création (GO-2026-11-15-04), jamais écrites sur le disque, seul `jouer` réel les reçoit ; exposition restante dite (configuration chez le loueur, environnement d'entrée) ; **la liste `show instances --raw` peut désormais porter les clés** : **retrait** des fichiers `instances-*.json` gardés dans `$ENV` en v10, remplacés par des identifiants seuls |
| effacement des clés à l'arrêt (A) | 0 | **retrait** de l'étape (2) « `ssh M 'shred -u …/cles.env'` » ; remplacée par : clés jamais plus transmises après `jouer`, effacées du programme après la dernière poussée ; côté session, feu d'arrêt |
| « aucun `jouer` ne tourne » | 0 | **retrait** du constat par `pgrep` ; remplacé par l'état poussé ; état « en cours » de plus de 40 minutes = constat illisible |
| heure limite | 0, 2 | **changé** : minuterie de destruction sur la machine à l'échéance (14 h 40 après la commande, au lieu d'une heure limite de 14 h tenue par l'horloge de la session) ; **retrait** de « un processus en cours à l'heure limite → nœud à Lazar, la part n'étant jamais dépassée sans son mot » : à l'échéance la minuterie détruit sans condition ; le nœud à Lazar reste, une heure avant ; **nouveau** : 12 h 30 au moins avant l'échéance exigées avant le pilote réel |
| attente de la phrase | 2, 5 | inchangée (une heure), comptée depuis le départ de la machine au lieu de la location |
| lancement détaché et « ne jamais rejouer » | 6, 9, 10 | **retrait** des scripts `lancer-*.sh`, `setsid nohup`, marques `@…@`, et de la ligne `REEL=…` dans `variables.sh` ; le programme machine lance et suit lui-même ; « ne jamais rejouer » porte désormais sur la commande de création (2.6) |
| relance sous `reel-2` | 7 | inchangée dans ses conditions ; **nouveau** : décidée par un feu de la mère dans les 20 minutes (sans ssh, aucune correction de la machine n'est possible) |
| machine gardée | 0, 8 | **retrait** de toute action sur une machine gardée autre que la destruction (sans ssh, aucune) ; dit |
| feu d'arrêt | 0, 7, 10 | **nouveau** : arrêt (A) demandé par la mère ; pendant `jouer`, arrêt du pilote par son PID (R10) ; jamais entre un `jouer` réussi et la mesure faite |
| relance du conteneur | 3 | **nouveau** : marque `amorce-lancee` ; aucune passe refaite ; arrêt (A) |
| balayage | 0 | **nouveau** : avant chaque poussée ; fichier fautif exclu et nommé |
| création | 2 | commande imprimée par l'outil après ses contrôles (offre, commits, amorce, ligne de GO, branches absentes, noms des clés, essai des arguments de l'amorce, échéance unique) ; `--cancel-unavail` ajouté ; sortie de la création écrite sous `umask 077` et supprimée après lecture de `new_contract` ; **préavis à Lazar** (mère) |
| recherche d'offres | 2 | **nouveau** : forme de la recherche écrite ; contrôle de l'offre par programme (la v10 la laissait à la main) |
| crédit, inventaires, relecture, destruction | 2, 11 | mêmes contrôles, joués par l'outil (lecture privée, supprimée) ; preuve d'absence inchangée (identifiant absent, témoins toujours listés) |
| épreuve des clés | 1 | **retrait** de la commande d'épreuve et de ses conduites (faite, code 0, R-2876, R-2877 ; ne se rejoue pas) ; q1 sans objet ; rappel q5 porté |
| q2 (dépense de l'épreuve remise) | 9 | portée : la dépense de l'épreuve (0,001164 USD) est proposée à la mère avec les autres |
| q3 (déclarations manquantes de la v10) | 12 octies | déclarées ici : la v10 avait **retiré**, sans les nommer parmi ses retraits, « (pire cas 0,027168 USD sous la ligne de 0,10) » (v9 l. 153), « ce sont celles de la sonde v74 du 14 novembre, 13:38Z » (v9 l. 378), « **Réduit par l'épreuve des clés de la section 1** (GO-2026-11-15-02) » (v9 l. 384), et changé le titre |
| q4 (« l'épreuve a eu lieu » après un refus) | 1 | sans objet : l'épreuve est faite (code 0) |
| q5 (sortie de l'épreuve hors de `main`) | 1 | rappel porté |
| f1 à f5 (programme d'épreuve) | — | sans objet pour la v11 (épreuve faite) ; f4 rappelé à la section 9 |
| dossier d'envoi | 0, 1 | **nouveau nom** (`…-envoi-v11`, R12) ; **retrait** de la copie du paquet, du texte et de la sonde vers la machine (la machine les prend aux commits) |
| retraits de la v11 | — | ceux marqués **retrait** ci-dessus ; rien d'autre |

Rien n'est changé au texte scellé ni au code du pilote (lanceur v74, configuration v12, programme de mesure `676d5f37…`).

## 13. Essais (compte organisme, sans appel, sans clé, sans réseau extérieur)

Pièces : `sans-ssh-v1/essais/` (programmes et résultats scellés ; `LISEZMOI.md`). Dépôt nu local à la place du dépôt distant (mêmes
chemins, vraies pièces : paquet, sonde, texte scellé, registre des lignes) ; doublure locale du loueur ; mère jouée par le banc au
moyen de l'outil de la session ; valeurs factices des clés.

- **Amorce et programme machine** (`essai_amorce_v1.py`) : 16 scénarios sur 16 conformes (arret-pendant-jouer, budget, code3, comptes-faux, entree-presente, feu1-faux, fuite-cle, mesure-code2, minuterie, phrase-alteree, refus-arguments, relance-conteneur, relance-deux-fois, relance-ok, sain, sortie-presente) ; sur chacun, aucune des valeurs factices, ni le secret, ni la phrase, dans aucun commit de la branche de sortie, aucun nom interdit ; résultats `essais/resultats-essai-amorce-v1.json`.
- **Scénario intégral** (vrai lanceur v74 : `bloc`, `secret`, `generer` des quatre mondes, `preparer`, `jouer --mode a_blanc`,
  `rapatrier`, `mesurer`, `lire`, `rapatrier`) : conforme (fini, 691 s, 248 fichiers poussés, aucune fuite, aucun nom interdit) ; résultats `essais/resultats-essai-amorce-integral-v1.json`. Seul écart au chemin de la machine louée : le pilote « réel » est joué
  en mode à blanc (le mode réel refuse toute configuration autre que la gelée, donc toute doublure de fournisseur).
- **Outil de la session** (`essai_outil_session_v1.py`) : 24 cas sur 24 conformes (offre, commande imprimée sans aucune valeur et jouée sur une doublure de l'outil du loueur, création, inventaires, relecture, crédit, destruction et preuve d'absence, aucune valeur gardée) ; résultats `essais/resultats-essai-outil-session-v1.json`.

**Non éprouvés** : la création chez le loueur et la forme réelle de `--env` et `--args` chez lui (la commande imprimée a été jouée sur
une doublure de l'outil du loueur, qui a reçu les arguments attendus) ; l'interface d'autodestruction du loueur (`CONTAINER_ID`,
`CONTAINER_API_KEY`, éprouvée par B bis) ; le clonage par jeton depuis la machine (éprouvé par B bis et Neuron Lens) ; la poussée sur
`BE` depuis la session (mandataire) ; les appels réels ; l'image `python:3.13-bookworm` (git, curl, openssl attendus ; l'amorce les
exige et refuse sinon).
