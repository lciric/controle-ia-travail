# Procédure pas à pas du pilote MR-2 sur la machine jetable — code v74, texte scellé candidat 6 — v9

- **Auteur** : modèle A (session du compte organisme). **Ce compte ne lance rien** (brief : aucun appel au loueur ; crochet de garde
  non chargé dans sa session). Pour la mère, ou une session exécutante ouverte dans le dépôt de travail, crochet vérifié chargé
  (R-2812, option (a)). Jouée seulement après une vérification « jouable » du différentiel v8 → v9 (mère).
- **Versions** (R12) : v1 `2b5248b3…`, v2 `d428c86c…`, v3 `efc29199…`, v4 `3c0e6627…`, v5 `a5719e26…`, v6 `6eb3a1cf…` restent en place ;
  v7 `be688ec1…` et v8 `56ccdb5a…` restent en place aussi ; **la v9 remplace la v8 pour l'usage** : elle porte la vérification courte
  de la v8 faite dans la session mère (`verification-courte-procedure-pilote-mr2-v74-machine-v8-v1.md`, `main`,
  `fbf07c0409e64339e9f773f5911314f2ba84a780b988bd435ca58cb5e69c59a5`, R-2858, « jouable après corrections », 0 bloquant, 2 majeurs M1 et
  M2, 9 mineurs m1 à m9) **et l'étape d'épreuve des clés** (ligne GO-2026-11-15-02, R-2856, préalable d'exécution accordé par le mot de
  Lazar) ; **différentiel v8 → v9 déclaré point par point, retraits compris, à la section 12 sexies**. La v8 elle porte la vérification courte de la v7 faite dans la
  session mère (`verification-courte-procedure-pilote-mr2-v74-machine-v7-v1.md`, `main`,
  `4be9e744ce1b1c53f6a835042f94c5ba510e63b8aeea492af046a3ef32cca3a2`, R-2853, « jouable après corrections », 0 bloquant, 2 majeurs MA et
  MB, 9 mineurs a1 à a9) ; **différentiel v7 → v8 déclaré point par point, retraits compris, à la section 12 quinquies**. La v7 portait la vérification courte de la v6 faite dans la session mère sur le mot de Lazar
  (R-2839) : `docs/notes/organisme-multi-generations-v1/pilote-v1/procedure-pilote-v74-compte-organisme/verification-courte-procedure-pilote-mr2-v74-machine-v6-v1.md`
  (`main`, `e5dd91242eaded4af2918c5b2ed2c7ba448ffb33db7cb98a6cb6392786ea65b2`, R-2846), « jouable après corrections », 0 bloquant,
  2 majeurs, 14 mineurs ; **différentiel v6 → v7 déclaré point par point à la section 12 quater**. Les versions précédentes portaient :
  v3 → v4 la contre-lecture du modèle J (`f07f9604…`) et les exigences de la mère sur la machine ; v4 → v5 la contre-lecture du
  modèle B (`f403f89f…`) ; v5 → v6 le verdict, rendu en réponse seulement, de la vérification courte en modèle B dont le rapport a été
  refusé par un classifieur (non contourné).
- **Outil du loueur** : version installée chez la mère **1.8.3** (la v6 citait 1.11.0, d'après R-2789 ; écart levé). Les formes
  employées ici (`create instance ID --image --disk --label`, option générale `--raw`, sortie brute de la création
  `{"success": …, "new_contract": N}`, `show instances --raw` en liste plate de lignes à champs `id` et `label`, `destroy instance ID -y`)
  ont été lues dans le code de cette version par le lecteur de la mère (rapport `e5dd9124…`, section 5), sans l'exécuter ; les champs
  `credit`, `ssh_host` et `ssh_port`, et le piège de `ssh-url` (code 0 même en erreur), dans le rapport `4be9e744…` (section 5).
- **Fait foi** : le texte scellé `docs/notes/organisme-multi-generations-v1/pilote-v1/preenregistrement-pilote-conditionnelles-v1-candidat6-compte-organisme.md`
  (branche `prep/pilote-mr2-compte-organisme-v1`), `8aa33014667da569ec934459d7bc1b1f6b54efa5c2145a6e5bdce5f7fa74603e`, scellé par la mère
  (R-2809), et sa vérification courte cumulée (`verification-courte-candidat3-candidat6-preenregistrement-pilote-v1.md`, `35d4216b…`,
  « scellable »). **Cette procédure ne change rien au texte** ; en cas d'écart, le texte prime et l'écart est un nœud.
- **Lignes** : GO-2026-11-14-13 (π1, 20 USD, crédits de Claude) et GO-2026-11-14-14 (π2, 21.72 USD hors crédits, dont machine 3 USD),
  `main` `20f66b0b`, l. 332-333 (R-2810).
- **Instances intouchables** : 58936096, 58936099, 58936100, 60480302, 60599797, 60670453, 60671759 (Neuron Lens), et toute instance ou
  tout serveur que la session qui lance n'a pas créé ; jamais les serveurs `poste-temoin-bailey-*`. **Aucune commande n'en nomme une.**
- **Interdits** : aucune valeur de clé affichée ni écrite dans un dépôt ; jamais `env`, `printenv`, `set` sans argument, `export -p`,
  `/proc/*/environ` ; aucune heure écrite à la main (`date -u` dans la même commande) ; arrêts par identifiant (R10) ; aucun refus de
  permission, du crochet ou d'un classifieur contourné ni rejoué.

## 0. Notations

**Session qui lance** (sous **bash** : le `printf '%q'` de la section 9 l'exige). Une session d'agent ne garde pas l'état de son
interpréteur d'une commande à l'autre : **chaque commande commence par**

```
ENV=/home/user/pilote-mr2-v74-envoi; : "${ENV:?}"; cd "$ENV" 2>/dev/null; test -e "$ENV/variables.sh" && . "$ENV/variables.sh"
```

- `W=/home/user/controle-ia-travail` (dépôt de travail) ; `ENV` : dossier d'envoi, **hors de tout dépôt**, absent avant
  (`test ! -e /home/user/pilote-mr2-v74-envoi && mkdir /home/user/pilote-mr2-v74-envoi`).
- `"$ENV/variables.sh"` : les seules valeurs non secrètes qui doivent survivre (`ETIQ`, `H`, `S1` à `S4`, `REEL`), **écrites par programme**
  au fil des sections 2 et 6, jamais tapées ; aucune clé n'y entre.
- `ETIQ` = l'étiquette de la machine, écrite une fois dans `"$ENV/etiquette.txt"` (section 2), relue ensuite (une location de **14 h**
  passe minuit).
- `ID` = l'identifiant de la machine, écrit une fois par programme dans `"$ENV/identifiant.txt"` (section 2), toujours relu de ce
  fichier, exigé entier.
- **ssh** : `ssh M` se lit `ssh -F "$ENV/ssh_config" pilote` ; `scp … M:CHEMIN` se lit `scp -F "$ENV/ssh_config" … pilote:CHEMIN`
  (fichier de configuration écrit à la section 3).

**Machine** (racine hors de tout dépôt) :

```
/root/pilote/arbre            arbre de l'organisme (dépôt git, tête 605e0f6)
/root/pilote/prive            (0700) secret, phrase, mondes, clés : rien n'en sort
/root/pilote/sonde            dossier entier de la sonde v74 (relevé et compagnon, quatre dossiers de relais, journaux)
/root/pilote/texte.md         texte scellé
/root/pilote/go-main.md       copie de registres/go.md de main
/root/pilote/lancements.jsonl registre des lancements réels (absent avant l'étape 9)
```

`O` = `cd /root/pilote/arbre/orchestrator && env -i PATH=/usr/local/bin:/usr/bin:/bin HOME=/root python3 -I -B demonstrations/pilote_mr2_v74.py`.
Chaque sous-commande imprime une ligne JSON (empreintes et contrôles) ; **0 conforme, 2 refus nommé (rien appelé), 3 arrêt (pièces
versées)** ; l'interprète rend lui-même 1 sur une erreur non rattrapée, et 2 sur une erreur d'usage. Toute sortie va dans
`/root/pilote/journal-NN-ETAPE.txt`, rapatrié.

**Arrêt commun (A)**, appelé par toute cause d'arrêt de toute étape après la location, **sauf entre un `jouer` réel réussi et la mesure
faite** (section 10, où un code inattendu mène à un nœud, machine gardée) : (1) écrire la cause (`date -u`) ;
(2) `ssh M 'shred -u /root/pilote/prive/cles.env 2>/dev/null; true'` ; (3) rapatrier ce qui peut l'être (section 11 : journaux,
empreintes ; `rapatrier` si un dossier de sortie existe, y compris après un code 3, qui y laisse `CARTES-partiel.json`, pièce permise) ;
(4) détruire la machine (section 11) ; (5) nœud à la mère. Après un code 3 de `jouer` ou de `mesurer` : **ni relance, ni mesure, ni
lecture d'issue, pas même P-0**. (6) **Refus d'un outil, du crochet ou d'un classifieur**, à toute étape après la location : ni rejoué,
ni reformulé, ni confié à une autre session ; si le refus ne frappe pas l'effacement des clés et qu'aucun `jouer` ne tourne, faire
l'étape (2) **avant** le nœud ; nœud immédiat à la mère, qui porte l'identifiant, l'étiquette, le prix horaire, l'heure de création et
l'étape du refus ; la machine reste louée jusqu'au mot de la mère (au plus jusqu'à l'heure limite) ; aucune création entre-temps ; si
le refus frappe la destruction elle-même, la mère (ou Lazar, par la console du loueur) détruit par l'identifiant consigné, et
l'absence est prouvée par la liste relue (section 11).

**« NON LANCÉ » inattendu** (à une ligne de lancement des sections 6, 9 ou 10, alors qu'aucun lancement n'a été fait) : ne rien
relancer ; effacer les clés (étape (2) de (A)) ; nœud à la mère.

**« Aucun `jouer` ne tourne »** se constate par `ssh M 'pgrep -af "[p]ilote_mr2_v74.py" || echo "aucun processus du pilote"'` (lecture
seule ; aucun arrêt par motif, R10).

**Heure limite** (section 2) : écrite dans `"$ENV/heure-limite.txt"`. Une heure avant : nœud à la mère. **À 2,70 USD dépensés sur la
machine** (prix × durée) : nœud à la mère (remis ; à 0,20 USD par heure il tombe après le nœud d'une heure avant). Aucun arrêt d'un
processus du pilote sans le mot de la mère, et alors **par son PID** (R10). À l'heure limite, sans mot de
la mère : aucun processus du pilote en cours (`generer`, `jouer`, `mesurer`) → arrêt (A) ; un processus en cours → nœud à Lazar par
la mère, la part de 3 USD n'étant jamais dépassée sans son mot. La garde est tenue par l'horloge de la session ; elle n'est pas
mécanique.

## 1. Pièces à préparer (session qui lance, aucune dépense)

```
W=/home/user/controle-ia-travail; ENV=/home/user/pilote-mr2-v74-envoi; : "${ENV:?}"
cd "$W" && git fetch origin +refs/heads/main:refs/remotes/origin/main \
  +refs/heads/lot/compte-organisme-v1:refs/remotes/origin/lot/compte-organisme-v1 \
  +refs/heads/prep/pilote-mr2-compte-organisme-v1:refs/remotes/origin/prep/pilote-mr2-compte-organisme-v1
P=docs/notes/organisme-multi-generations-v1/pilote-v1
git show refs/remotes/origin/lot/compte-organisme-v1:$P/procedure-pilote-v74-compte-organisme/arbre-organisme-complet-605e0f6.bundle > "$ENV/arbre-organisme-complet-605e0f6.bundle"
git show refs/remotes/origin/prep/pilote-mr2-compte-organisme-v1:$P/preenregistrement-pilote-conditionnelles-v1-candidat6-compte-organisme.md > "$ENV/texte.md"
git show refs/remotes/origin/main:registres/go.md > "$ENV/go-main.md"
mkdir "$ENV/sonde" && git archive refs/remotes/origin/lot/compte-organisme-v1 $P/sonde-complete-v74-compte-organisme/sonde-complete-v74 \
  | tar -x -C "$ENV/sonde" --strip-components=6
sha256sum "$ENV"/arbre-organisme-complet-605e0f6.bundle "$ENV"/texte.md "$ENV"/go-main.md "$ENV"/sonde/releve-sonde-pilote-v74.json
```

Attendus : paquet `e3d83e47a06b2941c54240b96612cb17880fe4162e7822a2eb02ebac64c785b1` ; texte `8aa33014667da569ec934459d7bc1b1f6b54efa5c2145a6e5bdce5f7fa74603e` ;
relevé `f56d9c0e14ca1f36ac3d9d226c1e5f763731fcc697ad780ea35c483ccf85d529` (et `sonde/releve-sonde-pilote-v74.json.sha256` présent, égal) ;
`ls "$ENV/sonde"` montre `releve-sonde-pilote-v74.json`, `argon/`, `astra/`, `fable52/`, `opus55/`. **Le paquet porte une histoire
tronquée** (dépôt public d'origine superficiel) : `git bundle verify` le dit « complete history », mais seul le dépaquetage marche
(section 4).

**Contrôles qui ne coûtent rien, faits ici et non après la location** (constat m6) :

```
: "${RR_ANTHROPIC_API_KEY_RIGAUD:?}" "${GEMINI_API_KEY:?}" "${OPENAI_API_KEY:?}"     # noms présents et non vides ; rien n'est affiché
ENV=/home/user/pilote-mr2-v74-envoi; mkdir "$ENV/arbre-local" && cd "$ENV/arbre-local" && git init -q \
  && git bundle unbundle ../arbre-organisme-complet-605e0f6.bundle > /dev/null && git checkout -q 605e0f60f3eed0948948e6a4eb15cb73de1d03de
cd "$ENV/arbre-local/orchestrator" && env -i PATH=/usr/local/bin:/usr/bin:/bin HOME=/root python3 -I -B -c '
import sys; sys.path.insert(0, ".")
from pole import proposeurs_pilote_v72 as PC, proposeurs_pilote_v70 as PR
from demonstrations import pilote_mr2_v74 as L
conf, _ = PC.lire_configuration(L.CONFIGURATION)
PR.lire_go_du_pilote(conf, sys.argv[1], "GO-2026-11-14-13", "GO-2026-11-14-14"); print("lignes du pilote lues au montant exact")' "$ENV/go-main.md"
```

Un nom de clé absent, ou les lignes refusées par le lecteur gelé : **arrêt, rien n'est loué**, nœud.

**Épreuve des trois clés** (préalable d'exécution, **GO-2026-11-15-02**, 0,10 USD, R-2856 ; écart au texte scellé déclaré et accordé
par le mot de Lazar : ni monde, ni appel du pilote, ni lecture), jouée **ici, à la fin de la section 1, avant toute location**, depuis
la session qui lance le pilote, **une seule fois** : programme `epreuve_cles_pilote_v1.py` (branche `lot/compte-organisme-v1`,
`docs/notes/organisme-multi-generations-v1/pilote-v1/epreuve-cles-pilote-v1-compte-organisme/`, `f56eaecbe6f79aef7b4d40e794a0f317c8306326d8665ae532bf02efa0d8221f`), un appel minimal par clé,
sortie sans clé ni corps.

```
ENV=/home/user/pilote-mr2-v74-envoi; : "${ENV:?}"
git -C /home/user/controle-ia-travail show refs/remotes/origin/lot/compte-organisme-v1:docs/notes/organisme-multi-generations-v1/pilote-v1/epreuve-cles-pilote-v1-compte-organisme/epreuve_cles_pilote_v1.py > "$ENV/epreuve_cles_pilote_v1.py"
sha256sum "$ENV/epreuve_cles_pilote_v1.py"            # attendu f56eaecbe6f79aef7b4d40e794a0f317c8306326d8665ae532bf02efa0d8221f
test ! -e "$ENV/epreuve-cles.json" && GO_ID=GO-2026-11-15-02 env -i PATH=/usr/bin:/bin HOME=/root HTTPS_PROXY="$HTTPS_PROXY" NO_PROXY="$NO_PROXY" \
  SSL_CERT_FILE="$SSL_CERT_FILE" RR_ANTHROPIC_API_KEY_RIGAUD="$RR_ANTHROPIC_API_KEY_RIGAUD" GEMINI_API_KEY="$GEMINI_API_KEY" \
  OPENAI_API_KEY="$OPENAI_API_KEY" python3 -I -B "$ENV/epreuve_cles_pilote_v1.py" \
  "$ENV/arbre-local/orchestrator/exemples/pilote-mr2-v70/configuration-pilote-mr2-v12.json" 0.10 "$ENV/epreuve-cles.json"; echo "code=$?"
```

Attendu : `code=0` et une ligne `{"toutes_valides": true, "depense_usd": …, "pire_cas_usd": 0.027168}` (pire cas 0,027168 USD sous la
ligne de 0,10). **Code 4** (une clé au moins ne passe pas) **ou tout autre code** : **arrêt, aucune location, aucune reprise de
l'épreuve** (la ligne sert une fois), nœud à la mère, avec `epreuve-cles.json` (par clé : code HTTP, modèle servi conforme, jetons,
coût ; aucune clé). La dépense de l'épreuve est proposée à la mère depuis `depense_usd`. Si `"$ENV/epreuve-cles.json"` existe déjà,
l'épreuve a eu lieu : **ne pas la rejouer**.
**Arrêt** (rien n'est loué) si une empreinte diffère.

## 2. Location (session qui lance ; GO-2026-11-14-14, part machine 3 USD) — une seule machine

1. Crochet `garde_calcul.py` chargé et éprouvé (cas sain et artefact, R5) ; sinon arrêt. Toute commande qui porte `vastai create`
   doit citer `GO_ID=GO-2026-11-14-14`, **aide comprise** (le crochet la prend aussi) ; les formes de la commande sont déjà lues dans
   le code de l'outil 1.8.3 (en-tête) : l'aide n'est pas nécessaire ; si on la lit, c'est sous le même préfixe.
2. **Crédit et moyen de paiement relevés avant la création**, par la session qui lance : solde lu **seul, par programme** (la commande
   de compte affiche des champs personnels, qui ne sont ni affichés ni gardés) :
   `vastai show user --raw | python3 -c 'import json,sys;u=json.load(sys.stdin);print("solde", u["credit"], "balance", u.get("balance"));assert float(u["credit"])>=5'` (champ `credit` lu dans le code de l'outil 1.8.3 ; le repli « lecture du seul solde à l'interface » est retiré : si le
   programme échoue, aucune création, nœud) ; solde **au moins 5 USD** ; le moyen de paiement
   actif est constaté par la mère à l'interface ; consignés (heure `date -u`) ; sinon, **aucune création**, nœud.
3. **Inventaire avant**, avec témoin : `vastai show instances --raw > "$ENV/instances-avant.json"` ; **témoin** = au moins une
   instance listée (le compte en porte d'autres, dont des intouchables : la liste vide est une liste mal lue, nœud), compté par programme
   (`python3 -c 'import json,sys;l=json.load(open(sys.argv[1]));assert isinstance(l,list) and len(l)>=1;print(len(l),"instances listées")' "$ENV/instances-avant.json"`), sans en
   nommer aucune ; `sha256sum` consigné ; la liste ne
   doit faire changer d'état aucune instance (lecture seule).
4. **Étiquette**, une fois : `test ! -e "$ENV/etiquette.txt" && echo "pilote-mr2-v74-$(date -u +%Y%m%d)" > "$ENV/etiquette.txt"` ;
   `echo "ETIQ=$(cat "$ENV/etiquette.txt")" >> "$ENV/variables.sh"`.
5. **Création, une seule** : une offre à processeurs seuls, au moins 4 processeurs, 8 Go de mémoire, **image `python:3.13-bookworm`**
   (Python 3.13 et git ; à contrôler à la section 3), **prix horaire total au plus 0,20 USD** (stockage compris) : pire cas ≈ 14 h
   (16 appels à la suite, délais de la configuration v12 : 3600 s pour `fable52` et `opus55`, 1800 s pour `argon` et `astra`, soit
   4 × 10 800 s = 12 h, plus ≈ 2 h de mise en place, d'attente de la phrase et de génération), soit ≈ 2,80 USD, sous la part :

   ```
   GO_ID=GO-2026-11-14-14 vastai create instance OFFRE --image python:3.13-bookworm --disk 20 --label "${ETIQ:?}" --raw > "$ENV/creation.json"
   # (pour cette seule ligne, le préambule de la section 0 est joué dans la commande d'avant : la ligne commence par GO_ID=)
   date -u -d '+14 hours' +%Y-%m-%dT%H:%M:%SZ > "$ENV/heure-limite.txt"      # dans la commande qui suit la création
   python3 -c 'import json,sys;v=json.load(open(sys.argv[1]))["new_contract"];assert isinstance(v,int) or str(v).isdigit();print(v)' \
     "$ENV/creation.json" > "$ENV/identifiant.txt" && ID=$(cat "$ENV/identifiant.txt") && [[ "$ID" =~ ^[0-9]+$ ]] && echo "ID=$ID"
   ```

   (`OFFRE` : l'identifiant de l'offre, **choisie à la main par la session qui lance** à la recherche d'offres du loueur, prix horaire
   total consigné avec la ligne de l'offre ; la recherche n'est pas écrite en commande ici.) Un `null`, un vide ou un non-nombre
   arrête ; l'identifiant n'est **jamais retapé**. **Repli** si la sortie n'est pas du JSON ou n'a pas `new_contract` :

   ```
   vastai show instances --raw > "$ENV/instances-apres-creation.json"
   python3 -c 'import json,sys;a={str(i["id"]) for i in json.load(open(sys.argv[1]))};n=[str(i["id"]) for i in json.load(open(sys.argv[2])) if str(i["id"]) not in a and i.get("label")==sys.argv[3]];assert len(n)==1,n;print(n[0])' \
     "$ENV/instances-avant.json" "$ENV/instances-apres-creation.json" "$ETIQ" > "$ENV/identifiant.txt"
   ```

   Zéro ou plus d'un identifiant neuf portant l'étiquette : nœud, aucune autre création. Consigner identifiant, étiquette, prix horaire,
   heure de création, heure limite.
6. **Inventaire après** : `vastai show instances --raw > "$ENV/instances-apres-creation.json"` ; l'identifiant y est avec l'étiquette, et
   c'est le seul ajouté : le programme du repli, **sans sa redirection**, suivi de `| diff - "$ENV/identifiant.txt" && echo "seul ajouté,
   égal à l'identifiant"` (rejoué avec la redirection, il récrirait `identifiant.txt`) ; aucune instance intouchable n'a changé d'état.
7. **Aucune seconde création** tant que l'absence de la première n'est pas prouvée (section 11). Une création en échec ou douteuse :
   arrêt (A), destruction par l'identifiant lu, absence prouvée, puis nœud.
8. Attente bornée : si la phrase de Lazar (section 5) ne vient pas dans l'heure qui suit la location, arrêt (A).

## 3. Mise en place (par ssh ; aucune dépense de fournisseur)

Fichier de configuration ssh, écrit par la session qui lance à partir de l'adresse et du port que donne l'outil pour `ID` (lus par
programme, jamais tapés), avec acceptation sans dialogue de la clé d'hôte (une session d'agent ne peut pas répondre) :

```
cat > "$ENV/ssh_config" <<EOF
Host pilote
  HostName ADRESSE
  Port PORT
  User root
  StrictHostKeyChecking accept-new
  UserKnownHostsFile $ENV/known_hosts
  ServerAliveInterval 30
EOF
```

`ADRESSE` et `PORT` viennent de `show instances --raw` (champs `ssh_host`, `ssh_port`), **jamais de `ssh-url`** (code 0 même en erreur),
par programme, avec une **attente bornée** du montage : le programme exige aussi `actual_status` égal à `running` et un `ssh_host` non
nul ; la boucle ne fait que lire, elle est **rejouable**, coupée en commandes de trois tours (90 s), **sept commandes au plus** (≈ dix
minutes), puis arrêt (A) ; le fichier est écrit par le programme. Avant la création, constater que le compte du loueur porte une clé ssh ; si la
clé privée n'est pas celle par défaut, ajouter `IdentityFile CHEMIN` :

```
rm -f "$ENV/adresse-port.txt"      # une seule fois, avant la première des sept commandes
for k in 1 2 3; do
  vastai show instances --raw > "$ENV/instances-ssh.json" && python3 -c 'import json,re,sys;m=[i for i in json.load(open(sys.argv[1])) if str(i["id"])==sys.argv[2]];assert len(m)==1,m;assert m[0].get("actual_status")=="running" and m[0]["ssh_host"],m[0].get("actual_status");h=str(m[0]["ssh_host"]);p=int(m[0]["ssh_port"]);assert re.fullmatch(r"[A-Za-z0-9.-]+",h) and 0<p<65536;print(h,p)' \
    "$ENV/instances-ssh.json" "$(cat "$ENV/identifiant.txt")" > "$ENV/adresse-port.txt" && break; rm -f "$ENV/adresse-port.txt"; sleep 30; done
if test -s "$ENV/adresse-port.txt" && read A PT < "$ENV/adresse-port.txt"; then sed -i "s/ADRESSE/$A/; s/PORT/$PT/" "$ENV/ssh_config"; grep -c -E 'ADRESSE|PORT$' "$ENV/ssh_config"; else echo "pas encore montée (après la septième commande : arrêt (A))"; fi
ssh -F "$ENV/ssh_config" -o ConnectTimeout=20 pilote true && echo "ssh prêt"   # refusé : reprise bornée, une fois par minute, dix minutes au plus, puis arrêt (A)
```

(dernière ligne : `0` attendu, aucune marque restante.) Puis :

```
ssh M 'mkdir -p /root/pilote && mkdir -m 700 /root/pilote/prive'
ssh M 'python3 -m pip install --no-cache-dir "numpy==2.5.3"'
ssh M 'env -i PATH=/usr/local/bin:/usr/bin:/bin HOME=/root python3 -I -c "import sys,numpy;print(sys.version_info[:2],numpy.__version__)" && git --version'
scp -F "$ENV/ssh_config" "$ENV/arbre-organisme-complet-605e0f6.bundle" "$ENV/texte.md" "$ENV/go-main.md" pilote:/root/pilote/
scp -F "$ENV/ssh_config" -r "$ENV/sonde" pilote:/root/pilote/
```

Attendu au contrôle : `(3, 13) 2.5.3` puis une version de git, **dans le même chemin réduit que `O`** (constat m7). numpy 2.5.3 est la
seule bibliothèque requise. **Arrêt (A)** sinon (le mode réel refuse tout autre numpy).

## 4. Arbre et bloc gelé (sur la machine)

```
cd /root/pilote && sha256sum arbre-organisme-complet-605e0f6.bundle texte.md go-main.md sonde/releve-sonde-pilote-v74.json
git init -q arbre && cd arbre && git bundle unbundle ../arbre-organisme-complet-605e0f6.bundle \
  && git checkout -q 605e0f60f3eed0948948e6a4eb15cb73de1d03de
git rev-parse HEAD                    # attendu 605e0f60f3eed0948948e6a4eb15cb73de1d03de
git status --porcelain --ignored      # attendu : vide
O bloc --releve-sonde /root/pilote/sonde/releve-sonde-pilote-v74.json > /root/pilote/journal-04-bloc.txt; echo $?    # attendu 0
python3 - <<'X'
t=open('/root/pilote/texte.md',encoding='utf-8').read(); b=open('/root/pilote/journal-04-bloc.txt',encoding='utf-8').read()
d='<!-- empreintes-du-code-pilote-v74 : début -->'; f='<!-- empreintes-du-code-pilote-v74 : fin -->'
i=t.index(d); j=t.index(f)+len(f); print('bloc égal' if t[i:j]+'\n'==b else 'BLOC DIFFÉRENT')
X
```

Le contre-lecteur a rejoué ces commandes hors machine : tête juste, arbre propre, bloc égal. **Arrêt (A)** sur tout écart.

## 5. Secret, puis phrase de Lazar

```
ssh M 'cd /root/pilote/arbre/orchestrator && env -i PATH=/usr/local/bin:/usr/bin:/bin HOME=/root python3 -I -B demonstrations/pilote_mr2_v74.py secret /root/pilote/prive/secret.bin > /root/pilote/journal-05-secret.txt; echo $?; cat /root/pilote/journal-05-secret.txt'
```

Attendu : `0` puis `{"secret_sha256": "…"}`, la seule chose qui sort. (1) La mère **inscrit cette empreinte et la pousse**. (2) **Ensuite
seulement**, Lazar donne sa phrase ; elle est envoyée par l'entrée standard, jamais en argument, par un document en entrée de ssh au
délimiteur entre guillemets :

```
ssh M 'umask 077; cat > /root/pilote/prive/phrase.txt' <<'PHRASE'
(la phrase de Lazar, une ligne, non vide, sans octet nul)
PHRASE
ssh M 'sha256sum /root/pilote/prive/phrase.txt'
```

L'empreinte inscrite est celle du **fichier**, retour à la ligne final compris (`generer` le retire à la lecture). La phrase passe dans
le journal de la session qui lance : celle-ci n'est pas publiée. **Arrêt (A)** si le secret existe déjà (le lanceur refuse d'écraser).

## 6. Mondes (≈ 12 min sur 4 processeurs, lancés détachés)

Script détaché (forme de la section 9, **sans** les lignes des clés), pour qu'une coupure de ssh ne tue pas la génération :

```
ssh M 'cat > /root/pilote/lancer-generer.sh' <<'SCRIPT'
#!/bin/bash
cd /root/pilote/arbre/orchestrator || { echo 97 > /root/pilote/code-06-generer.txt; exit 97; }
env -i PATH=/usr/local/bin:/usr/bin:/bin HOME=/root python3 -I -B demonstrations/pilote_mr2_v74.py generer --secret /root/pilote/prive/secret.bin --phrase-fichier /root/pilote/prive/phrase.txt --texte /root/pilote/texte.md --texte-sha256 8aa33014667da569ec934459d7bc1b1f6b54efa5c2145a6e5bdce5f7fa74603e --sortie /root/pilote/prive/MONDES.json > /root/pilote/journal-06-generer.txt 2>&1
echo $? > /root/pilote/code-06-generer.txt
SCRIPT
ssh M 'test ! -e /root/pilote/code-06-generer.txt && test ! -e /root/pilote/journal-06-generer.txt && { setsid nohup bash /root/pilote/lancer-generer.sh > /dev/null 2>&1 < /dev/null & echo lancé; } || echo "NON LANCÉ"'
# si cette commande ne rend pas la main ou dépasse son délai : NE JAMAIS LA REJOUER ; passer au suivi
ssh M 'cat /root/pilote/code-06-generer.txt 2>/dev/null || echo en cours'        # suivi, jusqu'au code (attendu 0)
ssh M 'cat /root/pilote/journal-06-generer.txt; cat /root/pilote/prive/MONDES.json.engagement.json'
```

Attendus : quatre mondes `"conforme": true` ; l'engagement porte `fichier_mondes_sha256` (noté `H`), les quatre `mondes_sha256`
(`S1` à `S4`, dans cet ordre) et le texte. Ces valeurs sont **tirées par programme** d'une copie de l'engagement, jamais tapées :

```
scp -F "$ENV/ssh_config" pilote:/root/pilote/prive/MONDES.json.engagement.json "$ENV/engagement-mondes.json"
python3 -c 'import json,sys;e=json.load(open(sys.argv[1]));print("H="+e["fichier_mondes_sha256"]);[print(f"S{k}={s}") for k,s in enumerate(e["mondes_sha256"],1)]' \
  "$ENV/engagement-mondes.json" >> "$ENV/variables.sh"
```

**Barrière** : ces empreintes sont **inscrites au registre** par la mère avant l'étape 7. **Arrêt (A)** si un monde n'est pas conforme
ou si le code n'est pas 0 (une graine neuve demande un texte neuf et le mot de Lazar).

## 7. C-16 et C-17

```
O preparer --mondes /root/pilote/prive/MONDES.json --mondes-sha256 H > /root/pilote/journal-07-preparer.txt; echo $?   # attendu 0
```

Attendus : clés `c16`, `c17`, `episodes_servis`, `gabarit_sha256`, `heritages_sha256`, `mondes`, `textes_servis` ; toutes les lois de
C-16 « admise » vraie ; `gabarit_sha256` = `e77d3041f7815b2c0579cbafdb2898ca8569fe61e6cb51b99a41c3724fc456a2`. **Arrêt (A)** sur tout refus.

## 8. Essai à blanc (vraies pièces servies, relais factices) et rapatriement essayé

```
O jouer --mode a_blanc --mondes /root/pilote/prive/MONDES.json --mondes-sha256 H --sortie /root/pilote/blanc \
  > /root/pilote/journal-08-blanc.txt; echo $?                                                                    # attendu 0
O rapatrier --source /root/pilote/blanc --destination /root/pilote/rapatrie-blanc \
  --mondes /root/pilote/prive/MONDES.json --mondes-sha256 H > /root/pilote/journal-08-rapatrier-blanc.txt; echo $?   # attendu 0
```

Attendus : `"mode": "a_blanc"`, `"comptes": {"complet": 16, "echec": 0, "tronque": 0}`, `"arret": null` ; au rapatriement
`"aucun_monde": true`. Aucune clé. **Ni `mesurer` ni `lire` sur `blanc/`** : l'essai à blanc ne produit aucun résultat. **Arrêt (A)** sur tout code non
nul ou toute sortie différente de l'attendu (aucun `blanc-2` : choix prudent, qui coûte les mondes ; un nœud le dit).

## 9. Pilote réel (une seule fois)

**Contrôles juste avant**, tous exigés :

```
: "${H:?}" "${S1:?}" "${S2:?}" "${S3:?}" "${S4:?}"
ssh M 'test ! -e /root/pilote/reel && test ! -e /root/pilote/reel-2 && test ! -e /root/pilote/lancements.jsonl && echo absents'
ssh M 'env -i PATH=/usr/local/bin:/usr/bin:/bin HOME=/root python3 -I -c "import numpy;print(numpy.__version__)"; sha256sum /root/pilote/texte.md /root/pilote/sonde/releve-sonde-pilote-v74.json'
ssh M 'python3 - <<X
import socket
for p in (8811, 8812, 8813, 8814):
    s = socket.socket(); s.settimeout(2)
    print("port", p, "OCCUPÉ" if s.connect_ex(("127.0.0.1", p)) == 0 else "libre"); s.close()
X'
ssh M 'python3 - <<X
import socket,ssl
for h in ["api.anthropic.com","generativelanguage.googleapis.com","api.openai.com"]:
    try:
        s=socket.create_connection((h,443),timeout=10); c=ssl.create_default_context().wrap_socket(s,server_hostname=h); print(h,"TLS",c.version()); c.close()
    except Exception as e: print(h,"ÉCHEC",type(e).__name__)
X'
```

Le contrôle de joignabilité n'envoie aucune clé et n'appelle aucune interface. **Arrêt (A)** si un dossier existe, si un port est
occupé, si un fournisseur est injoignable, si une empreinte diffère.

**Clés** (noms déjà contrôlés à la section 1, contrôlés de nouveau ici ; un nom absent ici : effacer ce qui a été envoyé, arrêt (A)) :

```
: "${RR_ANTHROPIC_API_KEY_RIGAUD:?}" "${GEMINI_API_KEY:?}" "${OPENAI_API_KEY:?}"
printf 'RR_ANTHROPIC_API_KEY_RIGAUD=%q\nGEMINI_API_KEY=%q\nOPENAI_API_KEY=%q\n' \
  "$RR_ANTHROPIC_API_KEY_RIGAUD" "$GEMINI_API_KEY" "$OPENAI_API_KEY" | ssh -F "$ENV/ssh_config" pilote 'umask 077; cat > /root/pilote/prive/cles.env'
```

(`%q` protège une valeur à caractères spéciaux, relue par `.` sous bash. La validité des clés n'est prouvée par aucun appel avant le
lancement unique : ce sont celles de la sonde v74 du 14 novembre, 13:38Z. **Risque résiduel à trancher par la mère** (la v7 écrivait à
tort « accepté » : aucune décision ne l'accepte) : qu'une clé ait été révoquée, épuisée ou changée depuis la sonde, de sorte que le
premier appel de chaque proposeur de ce fournisseur échoue, que ce proposeur est abandonné (ses autres appels portés « echec » sans
être envoyés), que le pilote continue et sort en code 0, lancement unique consommé, sans reprise. **La clé du premier fournisseur sert
deux proposeurs sur quatre (8 appels sur 16) : invalide seule, elle mène à P-0**, pendant que les appels des deux autres fournisseurs
sont payés (jusqu'à 9,36 USD chacun). La clé du deuxième ou du troisième fournisseur, invalide seule, laisse exactement le minimum (12
sur 16, 3 par monde), sans marge. **Réduit par l'épreuve des clés de la section 1** (GO-2026-11-15-02), qui ne couvre pas un
changement de clé entre l'épreuve et le lancement (≈ 2 h).)

**Script de lancement** (document au délimiteur entre guillemets : rien n'y est développé à l'envoi ; marques `@SORTIE@`, `@SUFFIXE@`,
`@H@`, `@S@` remplacées ensuite) :

```
ssh M 'cat > /root/pilote/lancer-reel.modele' <<'SCRIPT'
#!/bin/bash
cd /root/pilote/arbre/orchestrator || { echo 97 > /root/pilote/code-09-@SUFFIXE@.txt; shred -u /root/pilote/prive/cles.env; exit 97; }
env -i PATH=/usr/local/bin:/usr/bin:/bin HOME=/root bash -c 'set -a; . /root/pilote/prive/cles.env; set +a; exec python3 -I -B demonstrations/pilote_mr2_v74.py jouer --mode reel --mondes /root/pilote/prive/MONDES.json --mondes-sha256 @H@ --sortie /root/pilote/@SORTIE@ --go-pi1 GO-2026-11-14-13 --go-pi2 GO-2026-11-14-14 --registre-go /root/pilote/go-main.md --texte /root/pilote/texte.md --texte-sha256 8aa33014667da569ec934459d7bc1b1f6b54efa5c2145a6e5bdce5f7fa74603e --mondes-shas @S@ --registre-lancements /root/pilote/lancements.jsonl --releve-sonde /root/pilote/sonde/releve-sonde-pilote-v74.json' > /root/pilote/journal-09-@SUFFIXE@.txt 2>&1
echo $? > /root/pilote/code-09-@SUFFIXE@.txt
shred -u /root/pilote/prive/cles.env
SCRIPT
ssh M "sed 's/@SORTIE@/reel/; s/@SUFFIXE@/reel/g; s/@H@/$H/; s/@S@/$S1,$S2,$S3,$S4/' /root/pilote/lancer-reel.modele > /root/pilote/lancer-reel.sh && grep -c '@' /root/pilote/lancer-reel.sh; cat /root/pilote/lancer-reel.sh"
ssh M 'test ! -e /root/pilote/code-09-reel.txt && test ! -e /root/pilote/journal-09-reel.txt && { setsid nohup bash /root/pilote/lancer-reel.sh > /dev/null 2>&1 < /dev/null & echo lancé; } || echo "NON LANCÉ"'
# dès que « lancé » s'affiche : echo REEL=reel >> "$ENV/variables.sh"   (pour que REEL existe aussi dans un arrêt (A) après un code 3)
# si cette commande ne rend pas la main ou dépasse son délai : NE JAMAIS LA REJOUER ; passer au suivi
```

Attendu : `0` marque restante (`grep -c '@'` rend `0`), script relu. **Suivi** :
`ssh M 'cat /root/pilote/code-09-reel.txt 2>/dev/null || echo en cours; test -e /root/pilote/prive/cles.env && echo "clés encore là" || echo "clés effacées"'`,
toutes les quelques minutes ; un code ne compte que s'il est accompagné de « clés effacées » ; « en cours » avec « clés effacées » : nœud
à la mère. Heure limite : section 0. **Les relais sont lancés par le lanceur avec leur part comme plafond** (parts 12, 8, 9,36,
9,36 USD).

**Issues de `jouer`** :
- **code 0** : `"mode": "reel"`, 16 appels comptés, `"arret": null` (un fournisseur en panne donne des appels « echec », code 0, **sans
  reprise** ; le minimum de 12 sur 16 et de 3 par monde décide de P-0 à la lecture) → section 10.
- **code 2** : refus nommé : cause écrite, corriger seulement ce que le refus nomme, sans regarder aucune attribution, sans toucher ni au
  code ni au texte. Si **`lancements.jsonl` existe** : aucune relance, arrêt (A) (un refus levé après les appels, au contrôle du
  manifeste, sort aussi en code 2 : la règle le couvre). S'il est **absent** (aucun appel parti) : **une seule relance, toujours sous
  `reel-2`**, que `reel/` ait été créé ou non (le lanceur n'exige qu'un dossier de sortie absent) ; après une relance, **tous les noms sont
  ceux en `-2`, sans exception** :

  ```
  ssh M 'cd /root/pilote && mv journal-09-reel.txt journal-09-reel-essai1.txt && mv code-09-reel.txt code-09-reel-essai1.txt \
    && test ! -e reel-2 && test ! -e lancements.jsonl && echo prêt'
  # rejouer tous les contrôles « juste avant » ci-dessus SAUF la ligne des dossiers, remplacée par :
  ssh M 'test ! -e /root/pilote/reel-2 && test ! -e /root/pilote/lancements.jsonl && echo absents'
  # (reel/ du premier essai peut exister : il reste en place, jamais rapatrié) ; puis renvoyer les clés (bloc « Clés »)
  ssh M "sed 's/@SORTIE@/reel-2/; s/@SUFFIXE@/reel-2/g; s/@H@/$H/; s/@S@/$S1,$S2,$S3,$S4/' /root/pilote/lancer-reel.modele > /root/pilote/lancer-reel-2.sh && grep -c '@' /root/pilote/lancer-reel-2.sh; cat /root/pilote/lancer-reel-2.sh"
  ssh M 'test ! -e /root/pilote/code-09-reel-2.txt && test ! -e /root/pilote/journal-09-reel-2.txt && { setsid nohup bash /root/pilote/lancer-reel-2.sh > /dev/null 2>&1 < /dev/null & echo lancé; } || echo "NON LANCÉ"'
  # si cette commande ne rend pas la main ou dépasse son délai : NE JAMAIS LA REJOUER ; passer au suivi
  ssh M 'cat /root/pilote/code-09-reel-2.txt 2>/dev/null || echo en cours; test -e /root/pilote/prive/cles.env && echo "clés encore là" || echo "clés effacées"'
  ```

  Les sections 10 et 11 suivent alors `REEL=reel-2` : **dès le « lancé » de la relance**, `echo REEL=reel-2 >> "$ENV/variables.sh"` (la
  dernière ligne écrite l'emporte). Les lignes des sections 10 et 11 qui emploient `REEL` ou `H` portent leur garde (`${REEL:?}`,
  `${H:?}`).
  **Un second code 2** : aucune autre relance, arrêt (A).
- **code 3** : arrêt du pilote (coût au-dessus du pire cas, champ de réflexion apparu chez un proposeur dit « sans réflexion » — aucun à
  ce relevé —, part atteinte, autre arrêt) : arrêt (A), nœud de Lazar, toute reprise demande un texte neuf et des mondes neufs.
- **tout autre code** (1, 126, 127, 137, 97…), ou un code jamais écrit alors que le processus a disparu ou que la machine ne répond
  plus : aucune relance ; constater le registre par `ssh M 'test -e /root/pilote/lancements.jsonl && echo présent || echo absent'`
  (un échec de ssh vaut « illisible ») ; si aucun `jouer` ne tourne, effacer les clés (étape (2) de (A)) avant tout nœud ;
  si `lancements.jsonl` existe ou ne peut pas être lu, arrêt (A) ; s'il est absent, **nœud à la mère, machine
  gardée** (au plus jusqu'à l'heure limite).

## 10. Mesure (une seule fois, lancée détachée), puis lecture par un sous-agent neuf

`REEL` = `reel`, ou `reel-2` après une relance (lu dans `"$ENV/variables.sh"`). Script détaché, sans les lignes des clés :

```
: "${REEL:?}" "${H:?}"
ssh M 'cat > /root/pilote/lancer-mesurer.modele' <<'SCRIPT'
#!/bin/bash
cd /root/pilote/arbre/orchestrator || { echo 97 > /root/pilote/code-10-mesurer.txt; exit 97; }
env -i PATH=/usr/local/bin:/usr/bin:/bin HOME=/root python3 -I -B demonstrations/pilote_mr2_v74.py mesurer --sortie /root/pilote/@REEL@ --mondes /root/pilote/prive/MONDES.json --mondes-sha256 @H@ > /root/pilote/journal-10-mesurer.txt 2>&1
echo $? > /root/pilote/code-10-mesurer.txt
SCRIPT
ssh M "sed 's/@REEL@/$REEL/; s/@H@/$H/' /root/pilote/lancer-mesurer.modele > /root/pilote/lancer-mesurer.sh && grep -c '@' /root/pilote/lancer-mesurer.sh"
ssh M 'test ! -e /root/pilote/code-10-mesurer.txt && test ! -e /root/pilote/journal-10-mesurer.txt && { setsid nohup bash /root/pilote/lancer-mesurer.sh > /dev/null 2>&1 < /dev/null & echo lancé; } || echo "NON LANCÉ"'
# si cette commande ne rend pas la main ou dépasse son délai : NE JAMAIS LA REJOUER ; passer au suivi
ssh M 'cat /root/pilote/code-10-mesurer.txt 2>/dev/null || echo en cours'        # attendu 0 ; journal : empreintes seulement
```

`mesurer` ne rend que des empreintes (`programme_sha256` attendu `676d5f37f21cf5d512f92d2029991fa8795a77076c285ea9bd83c43841748365`).
Un `mesurer` lancé deux fois rend 2 la seconde fois : on ne le relance pas.
- **code 3** de `mesurer` : ne pas relancer, arrêt (A).
- **tout autre code non nul** de `mesurer` (2 : refus nommé, rendu avant le programme de mesure ; 1 : erreur non rattrapée ; 97), **ou
  `mesurer` muet** (aucun code, processus disparu) : cause
  écrite ; constater par `ssh M "ls /root/pilote/${REEL:?}"` qu'aucun fichier `sortie-mesure*` ni `mesure-pilote-v70*` n'existe ; puis
  **nœud à la mère, machine gardée** (au plus jusqu'à l'heure limite) ; **ni relance ni arrêt (A) sans son mot** : les mondes ne quittent
  jamais la machine, et sa destruction rendrait la mesure impossible.

Lecture (sortie non affichée ; seul le code l'est) :

```
ssh M "cd /root/pilote/arbre/orchestrator && env -i PATH=/usr/local/bin:/usr/bin:/bin HOME=/root python3 -I -B demonstrations/pilote_mr2_v74.py lire --sortie /root/pilote/${REEL:?} --ecrire /root/pilote/${REEL:?}/lecture-pilote-v70.json > /root/pilote/sortie-lire-non-ouverte.txt 2>&1; echo \$?"   # attendu 0
```

**La sortie de `lire` n'est pas affichée** ; sur un code non nul, la cause est dans `sortie-lire-non-ouverte.txt`, qui porte aussi
l'issue : la session qui lance **ne l'ouvre pas**, elle la rapatrie à part (section 11) et la remet telle quelle au sous-agent ; un code
non nul de `lire` mène, comme pour `mesurer`, à un nœud à la mère, machine gardée. Le fichier `REEL/lecture-pilote-v70.json` (nom
permis par le rapatriement ; séquence `lire --ecrire` puis `rapatrier` éprouvée sur la répétition :
`repetition-locale/lire-ecrire-puis-rapatrier-*.txt`) est remis, avec le texte scellé, à un **sous-agent neuf** (ni auteur du texte ni
de l'analyse), qui applique les critères gelés (« Règle », « Plan d'analyse », R13) ; son verdict est scellé, puis soumis à Lazar.

## 11. Rapatriement, dépense, destruction

```
# dans un arrêt (A) où REEL n'est pas écrit (aucun dossier de sortie réel) : sauter la ligne de rapatrier, la copie de rapatrie-reel et
# le contrôle du compagnon ; les autres copies se jouent
ssh M "cd /root/pilote/arbre/orchestrator && env -i PATH=/usr/local/bin:/usr/bin:/bin HOME=/root python3 -I -B demonstrations/pilote_mr2_v74.py rapatrier --source /root/pilote/${REEL:?} --destination /root/pilote/rapatrie-reel --mondes /root/pilote/prive/MONDES.json --mondes-sha256 ${H:?} > /root/pilote/journal-11-rapatrier.txt 2>&1; echo \$?"   # attendu 0
mkdir -p "$ENV/retour" "$ENV/retour-sous-agent"
scp -F "$ENV/ssh_config" -r pilote:/root/pilote/rapatrie-blanc "$ENV/retour/"       # chacune à part : un arrêt précoce n'en laisse que certaines
scp -F "$ENV/ssh_config" -r pilote:/root/pilote/rapatrie-reel "$ENV/retour/"
scp -F "$ENV/ssh_config" pilote:'/root/pilote/journal-*.txt' "$ENV/retour/"
scp -F "$ENV/ssh_config" pilote:'/root/pilote/code-*.txt' pilote:/root/pilote/lancements.jsonl pilote:/root/pilote/prive/MONDES.json.engagement.json "$ENV/retour/"
scp -F "$ENV/ssh_config" pilote:/root/pilote/sortie-lire-non-ouverte.txt "$ENV/retour-sous-agent/"    # non ouvert, remis au sous-agent
(cd "$ENV/retour/rapatrie-reel" && sha256sum -c lecture-pilote-v70.json.sha256)                     # comparé au compagnon, non ouvert
```

Attendu : `"aucun_monde": true` au rapatriement, et `OK` au contrôle du compagnon ; **arrêt (A)** sur un autre résultat (sans détruire
avant d'avoir rapatrié les journaux). **Jamais** rapatriés : `prive/secret.bin`, `prive/phrase.txt`, `prive/MONDES.json`, `REEL/prive/` et
`reel/prive/` d'un premier essai (textes servis). Verser sur une branche de travail, jamais `main` (réponses brutes : identifiants
servis, R-2731). Dépense : par relais, depuis le relevé du pilote, rapprochée des journaux des relais ; machine : prix horaire ×
durée ; proposée à la mère ; montants facturés : console de Lazar (R-2803).

**Destruction** (R10, R-2789) — identifiant relu dans `"$ENV/identifiant.txt"`, jamais retapé ; chaque étape conditionne la suivante :

```
ID=$(cat "$ENV/identifiant.txt") && [[ "$ID" =~ ^[0-9]+$ ]] && ETIQ=$(cat "$ENV/etiquette.txt") \
&& vastai show instances --raw > "$ENV/instances-avant-destruction.json" \
&& python3 -c 'import json,sys;m=[i for i in json.load(open(sys.argv[1])) if str(i["id"])==sys.argv[2]];assert len(m)==1 and m[0].get("label")==sys.argv[3],m;print("présent, étiquette juste")' \
     "$ENV/instances-avant-destruction.json" "$ID" "$ETIQ" \
&& vastai destroy instance "$ID" -y \
; vastai show instances --raw > "$ENV/instances-apres-destruction.json" \
&& python3 -c 'import json,sys;av={str(i["id"]) for i in json.load(open(sys.argv[1]))};ap={str(i["id"]) for i in json.load(open(sys.argv[2]))};t=av-{sys.argv[3]};assert sys.argv[3] not in ap;assert t<=ap;print("absent ; témoins toujours listés :",len(t))' \
     "$ENV/instances-avant-destruction.json" "$ENV/instances-apres-destruction.json" "$ID"
```

La destruction n'est prouvée **que** par le dernier programme : `ID` absent de la liste relue, et **toute autre instance listée avant
l'est encore après** (le témoin, sans nommer aucun identifiant intouchable) ; jamais par le code de sortie de l'outil. Si le compte n'a
aucune autre instance (témoin vide : le programme rend « 0 »), le dire : nœud, ou preuve par la console du loueur. Si l'étiquette n'est
pas celle de la création, ou si l'identifiant est illisible : **aucune destruction**, nœud. Si `ID` reste listé : recommencer la
destruction **par ce seul identifiant**, puis relire. Consigner : identifiant, étiquette, heure (`date -u`), empreintes des listes.
Aucune nouvelle création avant cette preuve.

## 12. Ce que fait la v4 des constats de la contre-lecture de la v3

| constat | ce que fait la v4 |
|---|---|
| B1 (clonage du paquet impossible : histoire tronquée) | dépaquetage `git init` + `git bundle unbundle` + `checkout` (éprouvé par le contre-lecteur) ; « complete history » dit trompeur (sections 1, 4) |
| M1 (lancement réel sans persistance) | script de lancement écrit sur la machine, lancé détaché (`setsid nohup`), code écrit dans un fichier, clés effacées par le même script, suivi par relecture (section 9) ; forme éprouvée avec des clés et une commande factices |
| M2 (`lecture.json` non rapatrié) | `--ecrire reel/lecture-pilote-v70.json`, nom de la liste permise du rapatriement ; séquence éprouvée sur la répétition (section 10) |
| M3 (clé absente non détectée) | `: "${NOM:?}"` pour chaque nom avant l'envoi (section 9) |
| M4 (arrêts sans destruction) | arrêt commun (A), appelé par chaque arrêt (section 0) |
| M5 (joignabilité non éprouvée) | contrôle TLS sans clé des trois hôtes d'amont de la configuration avant l'étape 9 |
| m1 | vérification courte cumulée citée en tête |
| m2 | barrière « empreintes des mondes inscrites » avant l'étape 7 |
| m3 | phrase par document en entrée de ssh ; empreinte du fichier, retour à la ligne compris ; journal non publié |
| m4 | commandes d'envoi écrites, compagnons et dossier `sonde/` entiers, `vastai show instances`, `test ! -e`, ports |
| m5 | panne de fournisseur : code 0, « echec », sans reprise ; pas de relance après un code 3 de `mesurer` ; code 2 corrigé sans regarder d'attribution |
| m6 | relais lancés par le lanceur avec leur part comme plafond |
| m7 | attente de la phrase bornée à une heure après la location |
| m8 | `rapatrier` après un code 3 : `CARTES-partiel.json` est une pièce permise ; dit dans l'arrêt commun (A) |
| exigences de la mère (23:14Z) | crédit et paiement relevés avant création ; étiquette ; identifiant tiré de `new_contract`, relu avec l'étiquette avant `destroy`, jamais retapé ; `-y` ; absence prouvée par la liste avec témoin ; aucune seconde création avant l'absence prouvée |

Refus rencontré par le contre-lecteur, dit tel quel : une lecture groupée de deux fichiers hors de sa liste (module d'audit du
rapatriement, configuration v12) a été refusée par un classifieur ; il ne l'a ni contournée ni reformulée. Ce compte a lu ces deux
fichiers par ailleurs pour les sections 9 à 11 (liste permise du rapatriement ; adresses d'amont et ports).

## 13. Répétition locale (compte organisme, sans appel ni clé)

Secret public de développement (32 octets nuls), phrase de répétition, 4 processeurs : `generer` 12 min (4 mondes conformes, 7 tirages
refusés puis remplacés) ; `preparer`, `jouer --mode a_blanc` (16 appels factices complets), `mesurer`, `lire`, `rapatrier` : code 0 ;
`lire --ecrire blanc/lecture-pilote-v70.json` puis `rapatrier` : le fichier et son compagnon sont rapatriés. L'issue affichée sur la
répétition n'est pas un résultat. Non éprouvés : location, `scp`, passage des clés, lancement détaché, appels réels, destruction.

## 12 bis. Ce que fait la v5 des constats de la contre-lecture de la v4 (modèle B)

| constat | ce que fait la v5 |
|---|---|
| M1 (identifiant : commande de création non écrite ; sortie JSON seulement sous la forme brute ; aucun repli) | forme `--raw` écrite, à confirmer par l'aide de l'outil ; `${ID:?}` ; repli : l'unique identifiant neuf portant l'étiquette, tiré par programme ; sinon nœud (section 2) |
| M2 (reprise après un code 2 : `reel/` déjà créé) | une seule relance sous `reel-2` si `lancements.jsonl` est absent ; sinon arrêt (A) (section 9) |
| M3 (durée : pire cas 12 h, part de 3 USD) | prix au plus 0,20 USD par heure ; heure limite = création + 13 h ; nœud à 2,70 USD et une heure avant l'heure limite (sections 2, 9) |
| M4 (refus d'outil après la location, y compris à la destruction) | point (6) de l'arrêt commun (A) |
| mineurs : (A) absent aux sections 8, 10, 11 ; rapatriement par `&&` | (A) ajouté ; commandes de rapatriement séparées |
| mineur : séquence `lire --ecrire` puis `rapatrier` non montrée | pièces versées (`repetition-locale/lire-ecrire-puis-rapatrier-*.txt`) |
| mineur : contrôle de ports propre à bash | contrôle des ports en Python |
| mineur : valeurs de clés à caractères spéciaux | `printf '%q'` |
| mineur : `lire` avale la cause d'un refus | sortie dans `journal-10-lire-non-affiche.txt`, non affichée, remise au sous-agent |
| mineur : crédit sans commande, acteur, seuil | acteur, seuil (5 USD), consignation (section 2) |
| mineur : validité des clés non prouvée | dite ; risque résiduel à trancher par la mère |
| autres mineurs du rapport (sans conséquence sur l'exécution) | gardés à la contre-lecture, non repris ici |

Non vérifiés par ce compte (aucun appel au loueur permis) : syntaxe exacte de `vastai create instance … --label … --raw`, de
`vastai show instances --raw` et de `vastai destroy instance … -y`. La session qui lance les confirme par l'aide de l'outil avant usage.

## 12 ter. Ce que fait la v6 du verdict de la vérification courte v4 → v5 (modèle B, rendu en réponse, rapport non écrit)

| constat | ce que fait la v6 |
|---|---|
| N1 (majeur : relance sous `reel-2`, pièces du premier essai réemployées, suivi trompé) | pièces du premier essai renommées ; script neuf ; contrôles rejoués ; suivi sur `code-09-reel-2.txt` avec « clés effacées » ; sections 10 et 11 sur `REEL` (section 9) |
| n1 (`None` passe `${ID:?}`) | identifiant exigé entier, `[[ "$ID" =~ ^[0-9]+$ ]]` |
| n2 (`ID` du repli et `ETIQ` dans aucun fichier) | `etiquette.txt` et `identifiant.txt`, écrits une fois, relus ensuite |
| n3 (programmes « par programme » non écrits) | lecture de `new_contract` écrite ; comparaison des listes brutes dite ; champs de la sortie brute à confirmer par l'aide de l'outil (non vérifiables ici) |
| n4 (prix total ; pire cas ≈ 14 h) | « prix horaire total, stockage compris » ; heure limite à création + 14 h ; ≈ 2,80 USD au pire, sous la part |
| n5 (`%q` exige bash) | dit en notations |
| n6 (sortie de `lire` rapatriée parmi les journaux) | `sortie-lire-non-ouverte.txt`, hors du motif `journal-*.txt`, rapatriée à part, non ouverte, remise au sous-agent |
| n7 (code 2 avant la création de `reel/`) | la seule relance garde `reel` |
| n8 (contenu du nœud du point (6)) | identifiant, étiquette, prix, heure, étape ; machine louée jusqu'au mot de la mère, au plus jusqu'à l'heure limite |
| n9 (pas de `blanc-2`) | dit (choix prudent) |
| n10 (pièce `…-lire.txt` = sortie affichée) | la preuve est la liste des copies de `…-rapatrier.txt` (section 10, inchangé) |
| n11 (coupure de ssh pendant `generer` ou `mesurer`) | les deux lancés détachés, code écrit dans un fichier |

Refus, dit tel quel : l'écriture du rapport de la vérification courte v4 → v5 a été refusée par un classifieur ; le lecteur ne l'a ni
contournée ni reformulée ; l'auteur ne l'écrit pas à sa place ; la voie d'une vérification de la v6 est laissée à la mère.

## 12 quater. Différentiel v6 → v7, point par point (vérification courte de la v6, session mère, `e5dd9124…`, R-2846)

| constat | où | ce que fait la v7 |
|---|---|---|
| M1 (relance quand `reel/` n'a pas été créé : consignes contraires) | 9 | une seule relance, **toujours sous `reel-2`**, que `reel/` existe ou non ; après une relance, tous les noms en `-2`, sans exception ; `REEL` écrit dans `variables.sh` |
| M2 (code inattendu entre un `jouer` réussi et la mesure ; (A) y détruit le seul lieu de la mesure) | 0, 9, 10 | (A) exclu de cet intervalle ; `mesurer` en code 2, 1 ou 97 : cause écrite, absence de sortie constatée, **nœud, machine gardée**, ni relance ni (A) sans mot de la mère ; `jouer` hors 0, 2, 3, ou muet : registre absent → nœud, machine gardée ; registre présent ou illisible → (A) ; `lire` non nul → nœud |
| m1 (relance décrite, non écrite) | 9 | `mv` par ssh, script modèle à marques, `sed` et lancement de `lancer-reel-2.sh`, suivi sur `code-09-reel-2.txt` ; « en cours » avec « clés effacées » : nœud ; second code 2 : (A) |
| m2 (création sans `GO_ID` ; aide prise par le crochet) | 2 | `GO_ID=GO-2026-11-14-14` en tête de la création et de toute aide ; formes déjà lues dans le code 1.8.3 |
| m3 (preuves « par programme » non écrites) | 2, 11 | programmes du repli, de l'étiquette avant `destroy` et de l'absence après, écrits (forme éprouvée par le lecteur de la mère sur des listes factices) ; témoin = toute autre instance listée avant l'est encore après ; témoin vide dit |
| m4 (garde de l'identifiant décorative) | 11 | bloc de destruction enchaîné par `&&`, programme « avant » juste devant `destroy` |
| m5 (restes de la v5) | en-tête, 0, 11 | définition de `ID` par `creation.json` supprimée ; « 14 h » ; `REEL/prive/` et `reel/prive/` ; « remplace la v6 pour l'usage » |
| m6 (clés et lignes contrôlées après la location) | 1 | noms des clés et lecteur gelé des lignes sur `go-main.md`, dans l'arbre dépaqueté localement, **avant** toute location |
| m7 (Python et numpy hors du chemin de `O` ; image non nommée) | 2, 3 | image `python:3.13-bookworm` ; contrôle sous `env -i PATH=/usr/local/bin:/usr/bin:/bin` et `-I`, plus `git --version` |
| m8 (rien pour l'heure limite elle-même) | 0, 2 | `heure-limite.txt` écrit après la création ; à l'heure limite : aucun processus → (A) ; un processus → nœud à Lazar par la mère |
| m9 (clés laissées sur la machine pendant le point (6)) | 0 | effacement des clés avant le nœud si le refus ne le frappe pas et qu'aucun `jouer` ne tourne |
| m10 (scripts détachés de `generer` et `mesurer` non écrits) | 6, 10 | scripts écrits, sans lignes de clés, `cd … || exit 97` ; `mesurer` lancé deux fois rend 2 : non relancé |
| m11 (variables de la session non gardées) | 0, 2, 6, 9 | préambule à chaque commande, `variables.sh` écrit par programme, `: "${ENV:?}"`, `: "${H:?}" … "${S4:?}"` avant le `sed` |
| m12 (crédit sans commande nommée) | 2 | solde lu seul, par programme ; champs personnels ni affichés ni gardés ; paiement constaté par la mère |
| m13 (ssh non écrit) | 0, 3 | `ssh_config` (adresse et port tirés par programme, `accept-new`, fichier d'hôtes dans `ENV`) ; `ssh -F`, `scp -F` |
| m14 (contrôle sans compagnon) | 11 | `sha256sum -c lecture-pilote-v70.json.sha256`, fichier non ouvert |
| écart de version de l'outil (1.11.0 / 1.8.3) | en-tête | 1.8.3 dit ; formes lues dans son code |

Éprouvé dans le conteneur du compte, sans clé ni appel ni loueur : le lecteur gelé des lignes de la section 1 sur une copie de
`registres/go.md` de `main` (« lues au montant exact », code 0) ; le script modèle de la section 9 rendu pour `reel` et pour `reel-2`
(aucune marque restante, `bash -n` juste, noms de sortie et de code justes) ; les programmes de la section 11 sur des listes factices
(présent avec l'étiquette juste ; absent avec témoin ; un identifiant encore listé rend une erreur) ; l'extraction de `H` et `S1` à `S4`
de l'engagement de la répétition.

Sections 4, 5, 7, 8, 12, 12 bis, 12 ter et 13 : texte de la v6, inchangé (dans la section 8, `O … rapatrier` reste au premier plan :
quelques secondes). Rien n'est changé au texte scellé ni au code.

## 12 quinquies. Différentiel v7 → v8, point par point, retraits compris (vérification courte de la v7, session mère, `4be9e744…`, R-2853)

| constat | où | changement en v8 |
|---|---|---|
| MA (lancement détaché qui retient ssh et dit « lancé » même quand rien ne part ; changement non déclaré de la v7) | 6, 9, 10 | les quatre lignes de lancement : garde sur le **code et le journal**, `{ setsid nohup … & echo lancé; } \|\| echo "NON LANCÉ"`, et « si la commande ne rend pas la main ou dépasse son délai : ne jamais la rejouer ; passer au suivi ». Éprouvé dans le conteneur du compte, à travers un tube, avec un script factice de 4 s : retour en 0,005 s, « lancé » ; second essai pendant le premier : « NON LANCÉ » en 0,004 s ; après la fin : « NON LANCÉ » (a9) |
| MB (relance : contrôle rejoué qui exige `reel` absent) | 9 | à la relance, la ligne des dossiers est remplacée par `test ! -e reel-2 && test ! -e lancements.jsonl` ; `reel/` du premier essai reste, jamais rapatrié |
| a1 (`|| exit 97` sans fichier de code) | 6, 10 | `|| { echo 97 > code-…; exit 97; }` pour `generer` et `mesurer` ; « `mesurer` muet : même conduite que tout autre code non nul » |
| a2 (`REEL`, `ETIQ` non gardés) | 2, 9, 10, 11 | `echo REEL=reel` après un code 0 du premier essai ; `: "${REEL:?}" "${H:?}"` en tête des sections 10 et 11 ; `: "${ETIQ:?}"` devant la création |
| a3 (programme du repli rejoué qui récrit `identifiant.txt`) | 2 | contrôle de l'inventaire après : programme sans redirection, `\| diff - identifiant.txt` |
| a4 (i) nœud à 2,70 USD retiré par la v7 sans le dire | 0 | **remis** dans le paragraphe de l'heure limite |
| a4 (ii) « arrêt par son PID (R10) » retiré par la v7 sans le dire | 0 | **remis** dans le paragraphe de l'heure limite |
| a4 (iii) « risque résiduel accepté par la mère » (erreur de la v7 : aucune décision) | 9 | **remis à « à trancher par la mère »**, et le risque est dit exactement : clé révoquée, épuisée ou changée depuis la sonde v74 → appels « echec » d'un fournisseur, lancement unique consommé, jusqu'à P-0 si deux fournisseurs tombent ; aucune épreuve sans appel ne le lève |
| a4 (iv) témoin de l'inventaire d'avant retiré par la v7 sans le dire | 2 | **remis**, redéfini : au moins une instance listée, compté par programme, sans en nommer aucune |
| a5 (programme d'`ADRESSE` et `PORT`, attente, clé) | 3 | programme sur `show instances --raw` (`ssh_host`, `ssh_port`), jamais `ssh-url` ; attente bornée à dix minutes, puis (A) ; clé ssh du compte constatée avant la création ; `IdentityFile` si besoin |
| a6 (solde) | 2 | champ `credit` (outil 1.8.3), `balance` affiché aussi, seuil de 5 USD exigé par programme ; réserve levée |
| a7 (« tout autre code » : registre non constaté ; clés laissées) | 9 | commande de constat du registre écrite ; effacement des clés avant le nœud si aucun `jouer` ne tourne |
| a8 (recherche de l'offre non écrite) | 2 | dite faite à la main par la session qui lance, prix horaire total consigné avec la ligne de l'offre |
| a9 (lancement détaché non éprouvé) | 12 quinquies | éprouvé (ligne MA ci-dessus) |
| retraits de la v8 | — | **aucun** : la v8 ne retire rien de la v7 hors des lignes remplacées ci-dessus (anciennes formes de lancement, `|| exit 97`, mention « nom du champ à confirmer », mention « recopié par programme de la recherche d'offres », mention `ssh-url`, ligne « rejouer TOUS les contrôles », mot « accepté ») |

Sections 1, 4, 5, 7, 8, 11 (hors la ligne de garde du point a2 en tête de son premier bloc), 12, 12 bis, 12 ter, 12 quater et 13 : texte de la v7, inchangé.
Rien n'est changé au texte scellé ni au code.

## 12 sexies. Différentiel v8 → v9, point par point, retraits compris (vérification courte de la v8, session mère, `fbf07c04…`, R-2858 ; épreuve des clés, R-2856)

| point | où | changement en v9 |
|---|---|---|
| épreuve des clés (GO-2026-11-15-02, R-2856) | 1 | étape neuve à la fin de la section 1, avant toute location, depuis la session qui lance, une seule fois ; programme `epreuve_cles_pilote_v1.py` (`f56eaecbe6f79aef…`) tiré de la branche et contrôlé par empreinte ; garde « fichier de sortie absent » ; code 4 ou tout autre code : arrêt, aucune location, aucune reprise, nœud à la mère ; dépense depuis `depense_usd` |
| M1 (risque des clés sous-décrit) | 9 | phrase réécrite : proposeur abandonné, code 0, lancement consommé ; la clé du premier fournisseur, seule, mène à P-0 ; une autre clé seule laisse le minimum sans marge ; réduit par l'épreuve, sauf changement entre l'épreuve et le lancement |
| M2 (garde de `REEL` et `H` qui bloquait tout le rapatriement d'un arrêt précoce) | 9, 11 | **retrait** de la ligne de garde en tête du premier bloc de la section 11 ; garde portée par la ligne de `rapatrier` (`${REEL:?}`, `${H:?}`) ; consigne « REEL non écrit : sauter rapatrier, la copie de `rapatrie-reel` et le contrôle du compagnon » ; `REEL=reel` écrit **dès le « lancé »** du premier essai, `REEL=reel-2` dès celui de la relance |
| m1 (création ne commençant plus par `GO_ID=`) | 2 | `GO_ID=` en tête ; `${ETIQ:?}` dans l'option ; **retrait** du `: "${ETIQ:?}";` devant ; préambule joué dans la commande d'avant, dit |
| m2 (échec du programme d'adresse sans arrêt ; reste d'un passage d'avant ; hôte nul) | 3 | `rm -f adresse-port.txt` avant ; `assert` sur `ssh_host` ; `if … then sed … else …` |
| m3 (« NON LANCÉ » inattendu) | 0 | conduite écrite : rien relancé, clés effacées, nœud |
| m4 (attente du montage plus longue qu'une commande ; champs peut-être remplis avant la fin du montage) | 3 | boucle coupée en commandes de trois tours, sept au plus, rejouable ; `actual_status == running` exigé ; reprise bornée du premier `ssh … true` |
| m5 (« aucun `jouer` ne tourne » sans commande) | 0 | `pgrep -af "[p]ilote_mr2_v74.py"`, lecture seule |
| m6 (garde de `REEL` absente des lignes de `ls` et de `lire`) | 10 | `${REEL:?}` dans ces lignes |
| m7 (`REEL=reel` sous l'issue « code 2 ») | 9 | **retrait** de cette place ; écrit sous la ligne de lancement (M2) |
| m8 (restes de rédaction) | en-tête, 0, 2 | l. 5 : « v8 → v9 » ; `REEL` ajouté à la liste de `variables.sh` ; rapport `4be9e744…` cité pour les champs neufs de l'outil ; **retrait** du repli « lecture du seul solde à l'interface » ; en-tête changé déclaré ici |
| m9 (témoin de l'inventaire) | 2 | `isinstance(l, list)` exigé |
| retraits de la v9 | — | ceux marqués **retrait** ci-dessus ; et la phrase de la v8 « aucune épreuve sans appel ne le lève ; un appel d'épreuve serait une dépense hors des lignes » est **retirée**, remplacée par la mention de l'épreuve ; rien d'autre |

Sections 4, 5, 6, 7, 8, 12, 12 bis, 12 ter, 12 quater, 12 quinquies et 13 : texte de la v8, inchangé. Rien n'est changé au texte scellé
ni au code du pilote.
