# Procédure pas à pas du pilote MR-2 sur la machine jetable — code v74, texte scellé candidat 6 — v6

- **Auteur** : modèle A (session du compte organisme). **Ce compte ne lance rien** (brief : aucun appel au loueur ; crochet de garde
  non chargé dans sa session). Pour la mère, ou une session exécutante ouverte dans le dépôt de travail, crochet vérifié chargé
  (R-2812, option (a)).
- **Versions** (R12) : v1 `2b5248b3…`, v2 `d428c86c…`, v3 `efc29199…`, v4 `3c0e6627…` restent en place. **La v6** porte le verdict de la vérification courte v4 → v5 par un lecteur neuf du modèle B, **rendu en réponse seulement** : l'écriture de
  son rapport a été refusée par un classifieur (motif « Destructive or Unwanted Actions »), refus non contourné, et l'auteur ne l'écrit pas
  à sa place ; verdict « jouable après corrections », 0 bloquant, 1 majeur (N1), 11 mineurs (section 12 ter). La v5 (`a5719e26…`) reste en
  place. **La v5 portait la contre-lecture de la v4 en modèle B** (`contre-lecture-procedure-pilote-mr2-v74-machine-v4.md`, `f403f89f…`, « jouable après corrections », 0 bloquant, 4 majeurs, 13 mineurs ; section 12 bis) et remplace la v4 pour l'usage. La v4 portait (section 12) : la contre-lecture
  de la v3 par le modèle J (`contre-lecture-procedure-pilote-mr2-v74-machine-v3.md`, `f07f9604…`, « jouable après corrections »,
  1 bloquant, 5 majeurs, 8 mineurs) et les exigences de la mère sur la machine (message du 14 novembre, 23:14Z : étiquette, identifiant
  tiré de `new_contract`, crédit relevé, une seule création, destruction prouvée avec témoin).
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
tout dépôt**, absent avant : `test ! -e "$ENV" && mkdir "$ENV"`) ; `ETIQ` = l'étiquette de la machine, fixée **une fois** et écrite dans un fichier, puis toujours relue de ce fichier (une location de 13 h
passe minuit) : `test ! -e "$ENV/etiquette.txt" && echo "pilote-mr2-v74-$(date -u +%Y%m%d)" > "$ENV/etiquette.txt" ; ETIQ=$(cat "$ENV/etiquette.txt")` ;
`ID` = l'identifiant de la machine, écrit une fois par programme dans `"$ENV/identifiant.txt"` (section 2) et toujours relu de ce fichier ;
la session qui lance tourne sous **bash** (le `printf '%q'` de la section 9 l'exige) ; `M` = l'adresse ssh de la machine ; `ID` = son identifiant, **lu
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
pas même P-0**. (6) **Refus d'un outil, du crochet ou d'un classifieur**, à toute étape après la location : ni rejoué, ni reformulé,
ni confié à une autre session ; nœud immédiat à la mère, qui porte l'identifiant, l'étiquette, le prix horaire, l'heure de création et
l'étape du refus ; la machine reste louée jusqu'au mot de la mère (au plus jusqu'à l'heure limite) ; aucune création entre-temps ; si le refus frappe la destruction elle-même, la
mère (ou Lazar, par la console du loueur) détruit par l'identifiant consigné, et l'absence est prouvée par la liste relue (section 11).

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
2. **Crédit et moyen de paiement relevés avant la création**, par la session qui lance, à l'interface du loueur ou par sa commande de
   compte : solde **au moins 5 USD** (part machine 3 USD et marge) et moyen de paiement actif ; consignés (heure `date -u`) ; sinon,
   **aucune création**, nœud.
3. **Inventaire avant**, avec témoin : `vastai show instances --raw > "$ENV/instances-avant.json"` (forme brute, lue par programme) ; `sha256sum` du fichier consigné ; la liste
   doit montrer les instances intouchables qui existent (c'est le témoin que la commande lit bien le compte) ; elle n'en change aucune.
4. **Création, une seule** : une offre à processeurs seuls (aucun processeur graphique utile), au moins 4 processeurs, 8 Go de mémoire,
   image avec Python 3.13, **prix horaire total au plus 0,20 USD** (stockage compris) : le pire cas de durée est de **12 h** pour les seuls appels (16 appels à
   la suite, délais de la configuration v12 : 3600 s pour `fable52` et `opus55`, 1800 s pour `argon` et `astra`, soit 4 × 10 800 s), plus
   ≈ 2 h de mise en place, d'attente de la phrase (une heure au plus) et de génération : pire cas ≈ 14 h, soit ≈ 2,80 USD, sous la part ;
   **heure limite** = heure de création + 14 h, consignée ; à 2,70 USD dépensés sur la machine
   (prix × durée), nœud à la mère avant tout dépassement de la part ; **étiquette** `pilote-mr2-v74-AAAAMMJJ` (date par
   `date -u +%Y%m%d`) ; la commande cite `GO_ID=GO-2026-11-14-14`. Forme de la commande (à confirmer par `vastai create instance --help` juste avant ; non vérifiée par ce compte, qui n'a aucun
   appel au loueur) : `vastai create instance OFFRE --image IMAGE --disk 20 --label "$ETIQ" --raw > "$ENV/creation.json"`. Sortie écrite
   **telle quelle** ; `ID` = son champ `new_contract`, lu par programme et exigé non vide :
   `python3 -c 'import json,sys;v=json.load(open(sys.argv[1]))["new_contract"];assert isinstance(v,int) or str(v).isdigit();print(v)' "$ENV/creation.json" > "$ENV/identifiant.txt" && ID=$(cat "$ENV/identifiant.txt") && [[ "$ID" =~ ^[0-9]+$ ]]`
   (un `null`, un vide ou un non-nombre arrête : `None` ne passe plus), **jamais retapé**. **Repli écrit** si la sortie n'est pas du JSON ou n'a pas `new_contract` : `vastai show instances --raw >
   "$ENV/instances-apres-creation.json"`, et `ID` = l'**unique** identifiant absent de `instances-avant.json` et portant l'étiquette
   `$ETIQ`, tiré par programme (comparaison des deux listes brutes) et écrit dans `"$ENV/identifiant.txt"` ; zéro ou plus d'un : nœud, aucune autre création. Consigner identifiant, étiquette, prix horaire, heure.
5. **Inventaire après** : `vastai show instances --raw > "$ENV/instances-apres-creation.json"` : l'identifiant `ID` y est, avec l'étiquette,
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
# (≈ 12 min : lancer cette commande, comme `mesurer` à la section 10, dans un script détaché de la forme de la section 9, code écrit dans
#  code-06-generer.txt, pour qu'une coupure de ssh ne la tue pas ; suivi par relecture du code)
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
`"aucun_monde": true`. Aucune clé. **Ni `mesurer` ni `lire` sur `blanc/`** : l'essai à blanc ne produit aucun résultat. **Arrêt (A)** sur tout code non
nul ou toute sortie différente de l'attendu (aucun `blanc-2` : choix prudent, qui coûte les mondes ; un nœud le dit).

## 9. Pilote réel (une seule fois)

**Contrôles juste avant**, tous exigés :

```
ssh M 'test ! -e /root/pilote/reel && test ! -e /root/pilote/lancements.jsonl && echo absents'
ssh M 'python3 -c "import numpy;print(numpy.__version__)"; sha256sum /root/pilote/texte.md /root/pilote/sonde/releve-sonde-pilote-v74.json'
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

Le contrôle de joignabilité n'envoie aucune clé et n'appelle aucune interface (connexion TLS seule ; éprouvé ici depuis le conteneur
du compte). Les lignes -13 et -14 sont relues au montant exact par le lecteur gelé du lanceur lui-même, au lancement. **Arrêt (A)** si un
dossier existe, si un port est occupé, si un fournisseur est injoignable, si une empreinte diffère.

**Clés** : chaque nom est contrôlé présent et non vide dans la session qui lance **avant l'envoi** (`${NOM:?}` échoue sinon), puis
les valeurs passent par l'entrée standard dans un fichier privé de la machine, jamais en argument ni à l'écran :

```
: "${RR_ANTHROPIC_API_KEY_RIGAUD:?}" "${GEMINI_API_KEY:?}" "${OPENAI_API_KEY:?}"
printf 'RR_ANTHROPIC_API_KEY_RIGAUD=%q\nGEMINI_API_KEY=%q\nOPENAI_API_KEY=%q\n' \
  "$RR_ANTHROPIC_API_KEY_RIGAUD" "$GEMINI_API_KEY" "$OPENAI_API_KEY" | ssh M 'umask 077; cat > /root/pilote/prive/cles.env'
```

(`%q` protège une valeur à caractères spéciaux, relue par `.` sous bash. La validité des clés n'est prouvée par aucun appel
avant le lancement unique : elles sont celles qui ont servi à la sonde v74 du 14 novembre, 13:38Z ; risque résiduel à trancher par la
mère.)

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
Suivi (premier essai ; après une relance, `code-09-reel-2.txt`) : `ssh M 'cat /root/pilote/code-09-reel.txt 2>/dev/null || echo en cours; test -e /root/pilote/prive/cles.env && echo "clés encore là" || echo "clés effacées"'`,
toutes les quelques minutes, jusqu'au code ; **une heure avant l'heure limite** (section 2), si le code n'est pas écrit : nœud à la
mère ; aucun arrêt du processus sans elle, et alors par son PID (R10), puis arrêt (A). **Les relais sont lancés par le lanceur avec leur part comme plafond** (configuration v12,
parts 12, 8, 9,36, 9,36 USD).

Issues de `jouer` : **code 0** : `"mode": "reel"`, 16 appels comptés, `"arret": null` (un fournisseur en panne donne des appels
« echec », code 0, **sans reprise** ; le minimum de 12 sur 16 et de 3 par monde décide de P-0 à la lecture) ; **code 2** : refus nommé,
rien appelé : cause écrite, corriger seulement ce que le refus nomme, sans regarder aucune attribution, sans toucher ni au code ni au
texte ; le lanceur crée `reel/` avant de lancer les relais : si `reel/` existe et que **`lancements.jsonl` est absent** (aucun appel
parti), **une seule** relance est permise, sous `--sortie /root/pilote/reel-2` ; si `reel/` n'a pas été créé (refus avant), la seule
relance garde `reel` ; si `lancements.jsonl` existe, aucune relance : arrêt (A). **Relance (N1)** : (1) renommer les pièces du premier
essai, `mv journal-09-reel.txt journal-09-reel-essai1.txt` et `mv code-09-reel.txt code-09-reel-essai1.txt` (rien n'est récrit) ; (2) écrire
un **script neuf** `lancer-reel-2.sh` qui nomme `--sortie /root/pilote/reel-2`, `journal-09-reel-2.txt` et `code-09-reel-2.txt` ; (3) rejouer
**tous** les contrôles « juste avant » (dossier `reel-2` absent, registre toujours absent, ports, empreintes, joignabilité) et renvoyer les
clés ; (4) le suivi lit **`code-09-reel-2.txt`**, et un code ne compte que s'il est accompagné de « clés effacées » ; (5) les sections 10
et 11 suivent le nom `reel-2` (noté `REEL` ci-dessous : `reel`, ou `reel-2` après une relance) ; **code 3** : arrêt du pilote (coût au-dessus du pire cas, champ de réflexion apparu chez un proposeur dit « sans réflexion »
— aucun à ce relevé —, part atteinte, autre arrêt) : **arrêt commun (A)**, nœud de Lazar, toute reprise demande un texte neuf et des
mondes neufs.

## 10. Mesure (une seule fois), puis lecture par un sous-agent neuf

```
O mesurer --sortie /root/pilote/REEL --mondes /root/pilote/prive/MONDES.json --mondes-sha256 H \
  > /root/pilote/journal-10-mesurer.txt; echo $?      # attendu 0 ; lancée détachée (script de la forme de la section 9, code-10-mesurer.txt)
O lire --sortie /root/pilote/REEL --ecrire /root/pilote/REEL/lecture-pilote-v70.json > /root/pilote/sortie-lire-non-ouverte.txt 2>&1; echo $?   # attendu 0
```

`mesurer` ne rend que des empreintes (`programme_sha256` attendu `676d5f37f21cf5d512f92d2029991fa8795a77076c285ea9bd83c43841748365`).
Après un code 3 de `mesurer`, ne pas relancer : arrêt commun (A). **La sortie de `lire` n'est pas affichée** (seul le code l'est ; sur un code non nul, la cause est dans
`sortie-lire-non-ouverte.txt`, qui porte aussi l'issue : la session qui lance **ne l'ouvre pas**, elle le rapatrie à part et le remet tel
quel au sous-agent, et arrêt (A) ; ce nom n'est pas pris par le motif `journal-*.txt` du rapatriement) : elle est écrite dans
`REEL/lecture-pilote-v70.json` (nom permis par le rapatriement ; la séquence `lire --ecrire` puis `rapatrier` est éprouvée sur la
répétition : `repetition-locale/lire-ecrire-puis-rapatrier-lire.txt` et `…-rapatrier.txt`, où le fichier et son compagnon figurent
parmi les copies) et remise, avec le texte scellé, à un **sous-agent neuf** (ni auteur du texte
ni de l'analyse) qui applique les critères gelés (« Règle », « Plan d'analyse », R13) ; son verdict est scellé, puis soumis à Lazar.

## 11. Rapatriement, dépense, destruction

```
O rapatrier --source /root/pilote/REEL --destination /root/pilote/rapatrie-reel \
  --mondes /root/pilote/prive/MONDES.json --mondes-sha256 H > /root/pilote/journal-11-rapatrier.txt; echo $?     # attendu 0
mkdir -p "$ENV/retour" "$ENV/retour-sous-agent"
scp -r M:/root/pilote/rapatrie-blanc "$ENV/retour/"           # chacune à part : un arrêt précoce n'en laisse que certaines
scp -r M:/root/pilote/rapatrie-reel "$ENV/retour/"
scp M:'/root/pilote/journal-*.txt' "$ENV/retour/"
scp M:'/root/pilote/code-*.txt' M:/root/pilote/lancements.jsonl M:/root/pilote/prive/MONDES.json.engagement.json "$ENV/retour/"
scp M:/root/pilote/sortie-lire-non-ouverte.txt "$ENV/retour-sous-agent/"   # dossier à part, non ouvert, remis au sous-agent
sha256sum "$ENV"/retour/rapatrie-reel/lecture-pilote-v70.json      # le fichier de l'issue est là, égal à son compagnon
```

Attendu : `"aucun_monde": true` ; **arrêt (A)** sur un autre résultat (sans détruire avant d'avoir rapatrié les journaux). **Jamais** rapatriés : `prive/secret.bin`, `prive/phrase.txt`, `prive/MONDES.json`, `reel/prive/`
(textes servis). Verser sur une branche de travail, jamais `main` (réponses brutes : identifiants servis, R-2731). Dépense : par relais,
depuis le relevé du pilote, rapprochée des journaux des relais ; machine : prix horaire × durée ; proposée à la mère ; montants facturés :
console de Lazar (R-2803).

**Destruction** (R10, R-2789) — identifiant relu dans `"$ENV/identifiant.txt"` (écrit à la section 2, création ou repli), jamais retapé :

```
ID=$(cat "$ENV/identifiant.txt") && [[ "$ID" =~ ^[0-9]+$ ]] || { echo "identifiant illisible : nœud, aucune destruction"; false; }
ETIQ=$(cat "$ENV/etiquette.txt")
vastai show instances --raw > "$ENV/instances-avant-destruction.json"   # relire par programme : ID présent, avec l'étiquette $ETIQ
vastai destroy instance "$ID" -y
vastai show instances --raw > "$ENV/instances-apres-destruction.json"   # par programme : ID ABSENT ; les instances témoins toujours listées
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
