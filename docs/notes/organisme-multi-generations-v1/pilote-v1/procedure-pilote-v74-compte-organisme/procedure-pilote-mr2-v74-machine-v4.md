# Procédure pas à pas du pilote MR-2 sur la machine jetable — code v74, texte scellé candidat 6 — v4

- **Auteur** : modèle A (session du compte organisme). **Ce compte ne lance rien** (brief : aucun appel au loueur ; crochet de garde
  non chargé dans sa session). Pour la mère, ou une session exécutante ouverte dans le dépôt de travail, crochet vérifié chargé
  (R-2812, option (a)).
- **Versions** (R12) : v1 `2b5248b3…`, v2 `d428c86c…`, v3 `efc29199…` restent en place. La v4 porte (section 12) : la contre-lecture
  de la v3 par le modèle J (`contre-lecture-procedure-pilote-mr2-v74-machine-v3.md`, `f07f9604…`, « jouable après corrections »,
  1 bloquant, 5 majeurs, 8 mineurs) et les exigences de la mère sur la machine (message du 14 novembre, 23:14Z : étiquette, identifiant
  tiré de `new_contract`, crédit relevé, une seule création, destruction prouvée avec témoin). La v4 remplace la v3 pour l'usage.
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

Session qui lance : `W=/home/user/controle-ia-travail` (dépôt de travail) ; `ENV=$W/../pilote-mr2-v74-envoi` (dossier d'envoi, **hors de
tout dépôt**, absent avant : `test ! -e "$ENV" && mkdir "$ENV"`) ; `M` = l'adresse ssh de la machine ; `ID` = son identifiant, **lu
dans le fichier `$ENV/creation.json`, jamais retapé** (section 2).

Machine (racine hors de tout dépôt) :

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
versées)**. Toute sortie va dans `/root/pilote/journal-NN-ETAPE.txt`, rapatrié.

**Arrêt commun (A)**, appelé par toute cause d'arrêt de toute étape après la location : (1) écrire la cause (`date -u`) ;
(2) `shred -u /root/pilote/prive/cles.env 2>/dev/null` ; (3) rapatrier ce qui peut l'être (section 11 : journaux, empreintes ;
`rapatrier` si un dossier de sortie existe, y compris après un code 3, qui y laisse `CARTES-partiel.json`, pièce permise) ; (4) détruire
la machine (section 11) ; (5) nœud à la mère. Après un code 3 de `jouer` ou de `mesurer` : **ni relance, ni mesure, ni lecture d'issue,
pas même P-0**.

## 1. Pièces à préparer (session qui lance, aucune dépense)

```
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
copie de `go.md` : empreinte consignée, et `sed -n 332,333p "$ENV/go-main.md"` montre GO-2026-11-14-13 et -14. **Le paquet porte une
histoire tronquée** (le dépôt public d'origine est un clone superficiel) : `git bundle verify` le dit « complete history » mais un
`git clone` échoue ; il se monte par dépaquetage (section 4), éprouvé par le contre-lecteur. Le chemin `--strip-components=6` est à
vérifier par `ls "$ENV/sonde"` (on doit y voir `releve-sonde-pilote-v74.json`, `argon/`, `astra/`, `fable52/`, `opus55/`).
**Arrêt** (rien n'est loué) si une empreinte diffère.

## 2. Location (session qui lance ; GO-2026-11-14-14, part machine 3 USD) — une seule machine

1. Crochet `garde_calcul.py` chargé et éprouvé (cas sain et artefact, R5) ; sinon arrêt.
2. **Crédit et moyen de paiement relevés avant la création** (solde du compte du loueur, moyen de paiement actif) ; consignés.
3. **Inventaire avant**, avec témoin : `vastai show instances > "$ENV/instances-avant.txt"` ; `sha256sum` du fichier consigné ; la liste
   doit montrer les instances intouchables qui existent (c'est le témoin que la commande lit bien le compte) ; elle n'en change aucune.
4. **Création, une seule** : une offre à processeurs seuls (aucun processeur graphique utile), au moins 4 processeurs, 8 Go de mémoire,
   image avec Python 3.13, prix horaire tel que 2 h au plus tiennent dans 3 USD ; **étiquette** `pilote-mr2-v74-AAAAMMJJ` (date par
   `date -u +%Y%m%d`) ; la commande cite `GO_ID=GO-2026-11-14-14`. Sortie de la création écrite **telle quelle** dans
   `"$ENV/creation.json"` ; `ID` = son champ `new_contract`, lu par programme (`python3 -c 'import json,sys;print(json.load(open(sys.argv[1]))["new_contract"])' "$ENV/creation.json"`),
   **jamais retapé**. Consigner identifiant, étiquette, prix horaire, heure.
5. **Inventaire après** : `vastai show instances > "$ENV/instances-apres-creation.txt"` : l'identifiant `ID` y est, avec l'étiquette,
   et c'est le seul ajouté ; aucune instance intouchable n'a changé d'état.
6. **Aucune seconde création** tant que l'absence de la première n'est pas prouvée (section 11). Une création en échec ou douteuse :
   arrêt commun (A), destruction par l'identifiant lu, absence prouvée, puis nœud.
7. Attente bornée : si la phrase de Lazar (section 5) ne vient pas dans l'heure qui suit la location, arrêt commun (A) ; la machine ne
   reste pas louée à vide.

## 3. Mise en place (par ssh ; aucune dépense de fournisseur)

```
ssh M 'mkdir -p /root/pilote && mkdir -m 700 /root/pilote/prive && python3 --version'           # attendu 3.13.x
ssh M 'python3 -m pip install --no-cache-dir "numpy==2.5.3" && python3 -c "import numpy;print(numpy.__version__)"'   # 2.5.3
scp "$ENV/arbre-organisme-complet-605e0f6.bundle" "$ENV/texte.md" "$ENV/go-main.md" M:/root/pilote/
scp -r "$ENV/sonde" M:/root/pilote/
```

numpy 2.5.3 est la seule bibliothèque requise (répétition locale : aucune autre). **Arrêt (A)** si Python n'est pas 3.13 ou numpy pas
2.5.3 (le mode réel refuse tout autre).

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

## 6. Mondes (≈ 12 min sur 4 processeurs)

```
O generer --secret /root/pilote/prive/secret.bin --phrase-fichier /root/pilote/prive/phrase.txt \
  --texte /root/pilote/texte.md --texte-sha256 8aa33014667da569ec934459d7bc1b1f6b54efa5c2145a6e5bdce5f7fa74603e \
  --sortie /root/pilote/prive/MONDES.json > /root/pilote/journal-06-generer.txt; echo $?                      # attendu 0
cat /root/pilote/prive/MONDES.json.engagement.json
```

Attendus : quatre mondes `"conforme": true` ; l'engagement porte `fichier_mondes_sha256` (noté `H`), les quatre `mondes_sha256` (notés
`S1,S2,S3,S4`, dans cet ordre) et le texte. **Barrière** : ces empreintes sont **inscrites au registre** par la mère avant l'étape 7.
**Arrêt (A)** si un monde n'est pas conforme (une graine neuve demande un texte neuf et le mot de Lazar).

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
`"aucun_monde": true`. Aucune clé. **Ni `mesurer` ni `lire` sur `blanc/`** : l'essai à blanc ne produit aucun résultat.

## 9. Pilote réel (une seule fois)

**Contrôles juste avant**, tous exigés :

```
ssh M 'test ! -e /root/pilote/reel && test ! -e /root/pilote/lancements.jsonl && echo absents'
ssh M 'python3 -c "import numpy;print(numpy.__version__)"; sha256sum /root/pilote/texte.md /root/pilote/sonde/releve-sonde-pilote-v74.json'
ssh M 'for p in 8811 8812 8813 8814; do (exec 3<>/dev/tcp/127.0.0.1/$p) 2>/dev/null && echo "port $p OCCUPÉ" || echo "port $p libre"; done'
ssh M 'python3 - <<X
import socket,ssl
for h in ["api.anthropic.com","generativelanguage.googleapis.com","api.openai.com"]:
    try:
        s=socket.create_connection((h,443),timeout=10); c=ssl.create_default_context().wrap_socket(s,server_hostname=h); print(h,"TLS",c.version()); c.close()
    except Exception as e: print(h,"ÉCHEC",type(e).__name__)
X'
```

Le contrôle de joignabilité n'envoie aucune clé et n'appelle aucune interface (connexion TLS seule ; éprouvé ici depuis le conteneur
du compte). Les lignes -13 et -14 sont relues au montant exact par le lecteur gelé du lanceur lui-même, au lancement. **Arrêt (A)** si un
dossier existe, si un port est occupé, si un fournisseur est injoignable, si une empreinte diffère.

**Clés** : chaque nom est contrôlé présent et non vide dans la session qui lance **avant l'envoi** (`${NOM:?}` échoue sinon), puis
les valeurs passent par l'entrée standard dans un fichier privé de la machine, jamais en argument ni à l'écran :

```
: "${RR_ANTHROPIC_API_KEY_RIGAUD:?}" "${GEMINI_API_KEY:?}" "${OPENAI_API_KEY:?}"
printf 'RR_ANTHROPIC_API_KEY_RIGAUD=%s\nGEMINI_API_KEY=%s\nOPENAI_API_KEY=%s\n' \
  "$RR_ANTHROPIC_API_KEY_RIGAUD" "$GEMINI_API_KEY" "$OPENAI_API_KEY" | ssh M 'umask 077; cat > /root/pilote/prive/cles.env'
```

**Lancement détaché** (une coupure de ssh ne doit pas tuer le pilote : le registre des lancements est écrit avant le premier appel, et
aucun second lancement n'est permis), code de sortie écrit dans un fichier, clés effacées dans la même enveloppe :

Le script de lancement est écrit sur la machine (document au délimiteur entre guillemets : rien n'y est développé à l'envoi), les deux
marques `@H@` et `@S@` y sont remplacées par les empreintes de l'étape 6 (non secrètes), on le relit, puis on le lance détaché :

```
ssh M 'cat > /root/pilote/lancer-reel.sh' <<'SCRIPT'
#!/bin/bash
cd /root/pilote/arbre/orchestrator
env -i PATH=/usr/local/bin:/usr/bin:/bin HOME=/root bash -c 'set -a; . /root/pilote/prive/cles.env; set +a; exec python3 -I -B demonstrations/pilote_mr2_v74.py jouer --mode reel --mondes /root/pilote/prive/MONDES.json --mondes-sha256 @H@ --sortie /root/pilote/reel --go-pi1 GO-2026-11-14-13 --go-pi2 GO-2026-11-14-14 --registre-go /root/pilote/go-main.md --texte /root/pilote/texte.md --texte-sha256 8aa33014667da569ec934459d7bc1b1f6b54efa5c2145a6e5bdce5f7fa74603e --mondes-shas @S@ --registre-lancements /root/pilote/lancements.jsonl --releve-sonde /root/pilote/sonde/releve-sonde-pilote-v74.json' > /root/pilote/journal-09-reel.txt 2>&1
echo $? > /root/pilote/code-09-reel.txt
shred -u /root/pilote/prive/cles.env
SCRIPT
ssh M "sed -i 's/@H@/$H/; s/@S@/$S1,$S2,$S3,$S4/' /root/pilote/lancer-reel.sh && cat /root/pilote/lancer-reel.sh"   # relire
ssh M 'setsid nohup bash /root/pilote/lancer-reel.sh > /dev/null 2>&1 < /dev/null & echo lancé'
```

(Dans la session qui lance, `H`, `S1` à `S4` sont les valeurs relevées à l'étape 6. La forme — script écrit par document entre guillemets,
marques remplacées, lancement par `setsid nohup`, code écrit dans un fichier, clés effacées après — est éprouvée dans le conteneur du
compte, avec des clés factices et une commande factice : variables vues par le processus, arguments justes, code 0, fichier des clés
effacé.)
Suivi : `ssh M 'cat /root/pilote/code-09-reel.txt 2>/dev/null || echo en cours; test -e /root/pilote/prive/cles.env && echo "clés encore là" || echo "clés effacées"'`,
toutes les quelques minutes, jusqu'au code. **Les relais sont lancés par le lanceur avec leur part comme plafond** (configuration v12,
parts 12, 8, 9,36, 9,36 USD).

Issues de `jouer` : **code 0** : `"mode": "reel"`, 16 appels comptés, `"arret": null` (un fournisseur en panne donne des appels
« echec », code 0, **sans reprise** ; le minimum de 12 sur 16 et de 3 par monde décide de P-0 à la lecture) ; **code 2** : refus nommé,
rien appelé : cause écrite, corriger seulement ce que le refus nomme, sans regarder aucune attribution, sans toucher ni au code ni au
texte ; **code 3** : arrêt du pilote (coût au-dessus du pire cas, champ de réflexion apparu chez un proposeur dit « sans réflexion »
— aucun à ce relevé —, part atteinte, autre arrêt) : **arrêt commun (A)**, nœud de Lazar, toute reprise demande un texte neuf et des
mondes neufs.

## 10. Mesure (une seule fois), puis lecture par un sous-agent neuf

```
O mesurer --sortie /root/pilote/reel --mondes /root/pilote/prive/MONDES.json --mondes-sha256 H \
  > /root/pilote/journal-10-mesurer.txt; echo $?                                                                 # attendu 0
O lire --sortie /root/pilote/reel --ecrire /root/pilote/reel/lecture-pilote-v70.json > /dev/null 2>&1; echo $?   # attendu 0
```

`mesurer` ne rend que des empreintes (`programme_sha256` attendu `676d5f37f21cf5d512f92d2029991fa8795a77076c285ea9bd83c43841748365`).
Après un code 3 de `mesurer`, ne pas relancer : arrêt commun (A). **La sortie de `lire` n'est pas affichée** : elle est écrite dans
`reel/lecture-pilote-v70.json` (nom permis par le rapatriement ; la séquence `lire --ecrire` puis `rapatrier` est éprouvée sur la
répétition, le fichier et son compagnon sont rapatriés) et remise, avec le texte scellé, à un **sous-agent neuf** (ni auteur du texte
ni de l'analyse) qui applique les critères gelés (« Règle », « Plan d'analyse », R13) ; son verdict est scellé, puis soumis à Lazar.

## 11. Rapatriement, dépense, destruction

```
O rapatrier --source /root/pilote/reel --destination /root/pilote/rapatrie-reel \
  --mondes /root/pilote/prive/MONDES.json --mondes-sha256 H > /root/pilote/journal-11-rapatrier.txt; echo $?     # attendu 0
mkdir "$ENV/retour" && scp -r M:/root/pilote/rapatrie-blanc M:/root/pilote/rapatrie-reel "$ENV/retour/" \
  && scp M:'/root/pilote/journal-*.txt' M:/root/pilote/code-09-reel.txt M:/root/pilote/lancements.jsonl \
         M:/root/pilote/prive/MONDES.json.engagement.json "$ENV/retour/"
sha256sum "$ENV"/retour/rapatrie-reel/lecture-pilote-v70.json      # le fichier de l'issue est là, égal à son compagnon
```

Attendu : `"aucun_monde": true`. **Jamais** rapatriés : `prive/secret.bin`, `prive/phrase.txt`, `prive/MONDES.json`, `reel/prive/`
(textes servis). Verser sur une branche de travail, jamais `main` (réponses brutes : identifiants servis, R-2731). Dépense : par relais,
depuis le relevé du pilote, rapprochée des journaux des relais ; machine : prix horaire × durée ; proposée à la mère ; montants facturés :
console de Lazar (R-2803).

**Destruction** (R10, R-2789) — identifiant lu dans `"$ENV/creation.json"`, jamais retapé :

```
ID=$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1]))["new_contract"])' "$ENV/creation.json")
vastai show instances > "$ENV/instances-avant-destruction.txt"     # relire : ID présent, avec l'étiquette pilote-mr2-v74-AAAAMMJJ
vastai destroy instance "$ID" -y
vastai show instances > "$ENV/instances-apres-destruction.txt"     # ID ABSENT ; les instances témoins toujours listées
```

La destruction n'est prouvée **que** par l'absence de `ID` dans la liste relue, la liste montrant toujours les instances témoins (preuve
que la commande lit le compte) ; jamais par le code de sortie (défaut de l'outil du loueur 1.11.0, R-2789). Si `ID` reste listé,
recommencer la destruction **par ce seul identifiant**, puis relire. Avant tout `destroy`, l'étiquette de `ID` dans la liste doit être
celle de la création ; sinon, **aucune destruction**, nœud. Consigner : identifiant, étiquette, heure (`date -u`), empreintes des listes.
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
