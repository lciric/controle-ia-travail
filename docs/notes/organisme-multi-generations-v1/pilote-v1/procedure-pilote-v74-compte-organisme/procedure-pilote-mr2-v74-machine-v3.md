# Procédure pas à pas du pilote MR-2 sur la machine jetable — code v74, texte scellé candidat 6 — v3

- **Auteur** : modèle A (session du compte organisme). **Ce compte ne lance rien** : son brief interdit tout appel au loueur, et le
  crochet de garde n'est pas chargé dans sa session. Cette procédure est pour la mère, ou pour une session exécutante ouverte dans le
  dépôt de travail, une fois le crochet vérifié chargé (R-2812 : option (a)).
- **Versions** (R12) : v1 (`2b5248b3…`) et v2 (`d428c86c…`) restent en place. La v3 est écrite pas à pas, sur la demande de R-2812 :
  commandes exactes, contrôles, sorties attendues, causes d'arrêt, rapatriement, destruction par identifiant avec `-y` et absence prouvée
  par la liste des instances (R-2789). Elle remplace la v2 pour l'usage.
- **Fait foi** : le texte scellé `docs/notes/organisme-multi-generations-v1/pilote-v1/preenregistrement-pilote-conditionnelles-v1-candidat6-compte-organisme.md`
  (branche `prep/pilote-mr2-compte-organisme-v1`), `8aa33014667da569ec934459d7bc1b1f6b54efa5c2145a6e5bdce5f7fa74603e`, scellé par la mère
  (R-2809). Sections « Ordre », « Mondes et secret », « Préalables », « Liste d'arrêt », « Plan d'analyse ». **Cette procédure ne change
  rien au texte** ; en cas d'écart, le texte prime et l'écart est un nœud.
- **Lignes** : GO-2026-11-14-13 (π1, 20 USD, crédits de Claude) et GO-2026-11-14-14 (π2, 21.72 USD hors crédits, dont la machine,
  3 USD), `main` `20f66b0b`, l. 332-333 (R-2810).
- **Instances intouchables** (R-2812) : 58936096, 58936099, 58936100, 60480302, 60599797, 60670453, 60671759 (Neuron Lens), et toute
  instance ou tout serveur que la session qui lance n'a pas créé. Les serveurs `poste-temoin-bailey-*` ne sont jamais touchés.
- **Interdits rappelés** : aucune valeur de clé affichée ni écrite dans un dépôt ; jamais `env`, `printenv`, `set` sans argument,
  `export -p`, `/proc/*/environ` ; aucune heure écrite à la main (`date -u` dans la même commande) ; arrêts par identifiant (R10) ;
  aucun refus de permission, du crochet ou d'un classifieur contourné ni rejoué.

## 0. Notations

Dans la session qui lance (dépôt de travail à jour, `main` relu) :

```
W=/home/user/controle-ia-travail                     # dépôt de travail
E=$W/../pilote-mr2-v74-envoi                          # dossier d'envoi, hors de tout dépôt (à créer, absent avant)
```

Sur la machine (une seule racine, hors de tout dépôt ; `prive/` en mode 0700) :

```
/root/pilote/arbre        arbre de l'organisme (dépôt git, tête 605e0f6)
/root/pilote/prive        secret, phrase, mondes, clés : rien n'en sort
/root/pilote/sonde        dossier entier de la sonde v74 (relevé et pièces des huit appels)
/root/pilote/texte.md     texte scellé
/root/pilote/go-main.md   copie de registres/go.md de main
/root/pilote/lancements.jsonl   registre des lancements réels (absent avant l'étape 8)
```

`O` désigne `cd /root/pilote/arbre/orchestrator && env -i PATH=/usr/local/bin:/usr/bin:/bin HOME=/root python3 -I -B demonstrations/pilote_mr2_v74.py`.
Chaque sous-commande imprime une ligne JSON (empreintes et contrôles seulement) ; **code 0 conforme, 2 refus nommé (rien appelé),
3 arrêt (pièces versées)**. Toute sortie est gardée dans un fichier `journal-NN-ETAPE.txt` sur la machine, et rapatriée.

## 1. Pièces à envoyer (session qui lance, aucune dépense)

| pièce | source | sha256 attendu |
|---|---|---|
| paquet complet de l'arbre (histoire entière, aucun prérequis), tête `605e0f60f3eed0948948e6a4eb15cb73de1d03de` | branche `lot/compte-organisme-v1`, `docs/notes/organisme-multi-generations-v1/pilote-v1/procedure-pilote-v74-compte-organisme/arbre-organisme-complet-605e0f6.bundle` | `e3d83e47a06b2941c54240b96612cb17880fe4162e7822a2eb02ebac64c785b1` |
| texte scellé | branche `prep/pilote-mr2-compte-organisme-v1`, chemin ci-dessus | `8aa33014667da569ec934459d7bc1b1f6b54efa5c2145a6e5bdce5f7fa74603e` |
| dossier entier de la sonde v74 | branche `lot/compte-organisme-v1`, `docs/notes/organisme-multi-generations-v1/pilote-v1/sonde-complete-v74-compte-organisme/sonde-complete-v74/` (relevé `releve-sonde-pilote-v74.json` et ses compagnons, quatre dossiers de relais, journaux des relais) | relevé : `f56d9c0e14ca1f36ac3d9d226c1e5f763731fcc697ad780ea35c483ccf85d529` |
| copie de `registres/go.md` de `main` | `git show refs/remotes/origin/main:registres/go.md` après `git fetch origin +refs/heads/main:refs/remotes/origin/main` | à relever et consigner ; les lignes 332-333 doivent être GO-2026-11-14-13 et -14 |

Contrôles **avant toute location** : chaque empreinte calculée par `sha256sum` égale à celle du tableau (sinon arrêt) ;
`git bundle verify` du paquet : « The bundle records a complete history » ; le paquet cloné dans un dossier d'essai donne la tête
`605e0f6`. **Ne pas envoyer** les branches du compte entières : seules ces pièces.

## 2. Location de la machine (session qui lance ; GO-2026-11-14-14, part machine 3 USD)

1. Vérifier que le crochet `garde_calcul.py` est chargé (épreuve sur un cas sain et sur un artefact, R5) ; sinon, arrêt.
2. Inventaire **avant** : liste des instances du loueur (identifiants et noms seulement) ; consigner.
3. Louer **une** machine à processeurs seuls (aucun processeur graphique n'est utile), au moins 4 processeurs et 8 Go de mémoire,
   image avec Python 3.13, au prix horaire le plus bas qui tienne la part (3 USD pour ≈ 2 h au plus) ; la commande de location cite la
   ligne (`GO_ID=GO-2026-11-14-14 …`). Consigner identifiant, prix horaire, heure (`date -u`).
4. Inventaire **après** : l'identifiant neuf est le seul ajouté ; aucune instance intouchable n'a changé d'état.

## 3. Mise en place (sur la machine, par ssh ; aucune dépense de fournisseur)

```
mkdir -p /root/pilote && mkdir -m 700 /root/pilote/prive
python3 --version                                    # attendu : 3.13.x
python3 -m pip install --no-cache-dir 'numpy==2.5.3' # seule bibliothèque requise (répétition : aucune autre)
python3 -c 'import numpy; print(numpy.__version__)'  # attendu : 2.5.3 (le mode réel refuse tout autre)
```

Envoi des pièces (`scp` depuis la session qui lance), puis :

```
cd /root/pilote && sha256sum arbre-organisme-complet-605e0f6.bundle texte.md go-main.md sonde/releve-sonde-pilote-v74.json
git clone -q arbre-organisme-complet-605e0f6.bundle arbre && cd arbre && git checkout -q 605e0f60f3eed0948948e6a4eb15cb73de1d03de
git rev-parse HEAD                                   # attendu : 605e0f60f3eed0948948e6a4eb15cb73de1d03de
git status --porcelain --ignored                     # attendu : vide
```

Contrôle du bloc gelé (même code, même relevé) :

```
O bloc --releve-sonde /root/pilote/sonde/releve-sonde-pilote-v74.json > /root/pilote/journal-03-bloc.txt; echo $?   # attendu 0
python3 - <<'X'
t=open('/root/pilote/texte.md',encoding='utf-8').read(); b=open('/root/pilote/journal-03-bloc.txt',encoding='utf-8').read()
i=t.index('<!-- empreintes-du-code-pilote-v74 : début -->'); j=t.index('<!-- empreintes-du-code-pilote-v74 : fin -->')+len('<!-- empreintes-du-code-pilote-v74 : fin -->')
print('bloc égal' if t[i:j]+'\n'==b else 'BLOC DIFFÉRENT')
X
```

**Arrêt** si une empreinte diffère, si la tête n'est pas `605e0f6`, si l'arbre n'est pas propre, si numpy n'est pas 2.5.3, si le bloc
diffère. Rien n'est appelé.

## 4. Secret, puis phrase de Lazar (ordre du texte scellé)

```
O secret /root/pilote/prive/secret.bin > /root/pilote/journal-04-secret.txt; echo $?     # attendu 0
cat /root/pilote/journal-04-secret.txt                # {"secret_sha256": "…"} : la seule chose qui sort
```

1. L'empreinte du secret est **inscrite au registre et poussée** par la mère (le secret lui-même ne sort jamais de `prive/`).
2. **Ensuite seulement**, Lazar donne sa phrase. Elle est envoyée par l'entrée standard, jamais en argument :
   `ssh MACHINE 'umask 077; cat > /root/pilote/prive/phrase.txt'` (la phrase tapée, une ligne, non vide, sans octet nul), puis
   `sha256sum /root/pilote/prive/phrase.txt` → empreinte inscrite. Ni la phrase ni le secret ne sont publiés.

**Arrêt** si le secret existe déjà (le lanceur refuse de l'écraser) ; un secret neuf demande un texte neuf et le mot de Lazar.

## 5. Mondes (≈ 12 min sur 4 processeurs)

```
O generer --secret /root/pilote/prive/secret.bin --phrase-fichier /root/pilote/prive/phrase.txt \
  --texte /root/pilote/texte.md --texte-sha256 8aa33014667da569ec934459d7bc1b1f6b54efa5c2145a6e5bdce5f7fa74603e \
  --sortie /root/pilote/prive/MONDES.json > /root/pilote/journal-05-generer.txt; echo $?                      # attendu 0
```

Sortie attendue : `{"controles": [ {"conforme": true, "monde": 1, "spec_sha256": …, "tirages_refuses": […]}, … 4 mondes ],
"fichier_mondes_sha256": "…"}`. Le fichier `/root/pilote/prive/MONDES.json.engagement.json` porte l'empreinte du fichier des mondes,
celles des quatre mondes et celle du texte : **ces empreintes vont au registre** (le fichier des mondes, jamais).
Noter `H` = `fichier_mondes_sha256` et `S1,S2,S3,S4` = les quatre `mondes_sha256` de l'engagement.

**Arrêt** (avant tout appel, cause écrite) si un monde n'est pas conforme ; une graine neuve demande un texte neuf et le mot de Lazar.

## 6. C-16 et C-17

```
O preparer --mondes /root/pilote/prive/MONDES.json --mondes-sha256 H > /root/pilote/journal-06-preparer.txt; echo $?   # attendu 0
```

Sortie attendue : clés `c16`, `c17`, `episodes_servis`, `gabarit_sha256`, `heritages_sha256`, `mondes`, `textes_servis` ; toutes les
lois de C-16 « admise » vraie ; `gabarit_sha256` = `e77d3041f7815b2c0579cbafdb2898ca8569fe61e6cb51b99a41c3724fc456a2`.
**Arrêt** sur tout refus (une loi hors bornes non récrite en `transformee` qui ne passe pas le gardien, C-16 ; C-17).

## 7. Essai à blanc avec les vraies pièces servies, et rapatriement essayé

```
O jouer --mode a_blanc --mondes /root/pilote/prive/MONDES.json --mondes-sha256 H --sortie /root/pilote/blanc \
  > /root/pilote/journal-07-blanc.txt; echo $?                                                                   # attendu 0
O rapatrier --source /root/pilote/blanc --destination /root/pilote/rapatrie-blanc \
  --mondes /root/pilote/prive/MONDES.json --mondes-sha256 H > /root/pilote/journal-07-rapatrier-blanc.txt; echo $?  # attendu 0
```

Sorties attendues : `"mode": "a_blanc"`, `"comptes": {"complet": 16, "echec": 0, "tronque": 0}`, `"arret": null` ; au rapatriement,
`"aucun_monde": true`. Aucune clé n'est passée à cette étape (relais factices). **L'essai à blanc ne produit aucun résultat** : ne lancer
ni `mesurer` ni `lire` sur `blanc/`.

## 8. Pilote réel (une seule fois)

Contrôles juste avant (comme à la sonde) : dossier `/root/pilote/reel` absent ; `/root/pilote/lancements.jsonl` absent ; lignes -13
et -14 lues au montant exact par le lecteur gelé du lanceur sur `/root/pilote/go-main.md` ; ports des relais libres ; numpy 2.5.3 ;
empreinte du texte ; relevé de la sonde égal à son compagnon.

Clés : envoyées **par l'entrée standard** dans un fichier privé de la machine, jamais en argument ni à l'écran, depuis la session
qui lance (valeurs prises de son environnement par leur nom) :

```
printf 'RR_ANTHROPIC_API_KEY_RIGAUD=%s\nGEMINI_API_KEY=%s\nOPENAI_API_KEY=%s\n' \
  "$RR_ANTHROPIC_API_KEY_RIGAUD" "$GEMINI_API_KEY" "$OPENAI_API_KEY" | ssh MACHINE 'umask 077; cat > /root/pilote/prive/cles.env'
```

Lancement (aucune variable `ANTHROPIC_BASE_URL` : `env -i`) :

```
cd /root/pilote/arbre/orchestrator && env -i PATH=/usr/local/bin:/usr/bin:/bin HOME=/root bash -c '
  set -a; . /root/pilote/prive/cles.env; set +a
  exec python3 -I -B demonstrations/pilote_mr2_v74.py jouer --mode reel \
    --mondes /root/pilote/prive/MONDES.json --mondes-sha256 H --sortie /root/pilote/reel \
    --go-pi1 GO-2026-11-14-13 --go-pi2 GO-2026-11-14-14 --registre-go /root/pilote/go-main.md \
    --texte /root/pilote/texte.md --texte-sha256 8aa33014667da569ec934459d7bc1b1f6b54efa5c2145a6e5bdce5f7fa74603e \
    --mondes-shas S1,S2,S3,S4 --registre-lancements /root/pilote/lancements.jsonl \
    --releve-sonde /root/pilote/sonde/releve-sonde-pilote-v74.json' > /root/pilote/journal-08-reel.txt 2>&1; echo $?
shred -u /root/pilote/prive/cles.env
```

Sortie attendue (code 0) : `"mode": "reel"`, `"comptes"` sur 16 appels, `"arret": null`. **Code 2** : refus nommé, rien appelé (cause
écrite ; corriger seulement ce que le refus nomme, sans toucher au code ni au texte). **Code 3** : arrêt du pilote (coût au-dessus du
pire cas, champ de réflexion apparu chez un proposeur dit « sans réflexion » — aucun à ce relevé —, part atteinte, etc.) : pièces
versées, **la mesure n'est pas lancée, aucune issue n'est lue, pas même P-0**, nœud de Lazar ; toute reprise demande un texte neuf
et des mondes neufs. **Aucun second lancement** pour ce texte (le registre des lancements le refuse).

## 9. Mesure (une seule fois), puis lecture par un sous-agent neuf

```
O mesurer --sortie /root/pilote/reel --mondes /root/pilote/prive/MONDES.json --mondes-sha256 H \
  > /root/pilote/journal-09-mesurer.txt; echo $?                                                                 # attendu 0
O lire --sortie /root/pilote/reel --ecrire /root/pilote/reel/lecture.json > /root/pilote/journal-09-lire.txt; echo $?
```

La sortie de `mesurer` ne porte que des empreintes (`programme_sha256` attendu
`676d5f37f21cf5d512f92d2029991fa8795a77076c285ea9bd83c43841748365`). **La session qui lance n'affiche pas la sortie de `lire`** : le
fichier `lecture.json` (et `journal-09-lire.txt`) est remis, avec le texte scellé, à un **sous-agent neuf** (ni auteur du texte ni de
l'analyse) qui applique les critères gelés du texte (« Règle », « Plan d'analyse », R13) ; son verdict est scellé, puis soumis à
Lazar. Une erreur du programme de mesure (exception) : rien n'est lu, cause écrite (liste d'arrêt).

## 10. Rapatriement, dépense, destruction

```
O rapatrier --source /root/pilote/reel --destination /root/pilote/rapatrie-reel \
  --mondes /root/pilote/prive/MONDES.json --mondes-sha256 H > /root/pilote/journal-10-rapatrier.txt; echo $?     # attendu 0
```

Attendu : `"aucun_monde": true`. Rapatrier vers la session (`scp`) : `rapatrie-blanc/`, `rapatrie-reel/`, tous les
`journal-NN-*.txt`, `prive/MONDES.json.engagement.json` (empreintes seulement), `lancements.jsonl`. **Jamais** `prive/secret.bin`,
`prive/phrase.txt`, `prive/MONDES.json`, ni les textes servis (`reel/prive/`), qui restent sur la machine et meurent avec elle.
Verser sur une branche de travail (pas `main`) : les réponses brutes portent les identifiants servis (R-2731).

Dépense : par relais, depuis le relevé du pilote rapatrié, rapprochée des journaux des relais ; machine : prix horaire × durée ;
proposée à la mère pour inscription ; prix rapprochés de la console par Lazar pour les montants facturés (R-2803).

**Destruction** (R10, R-2789) :

```
vastai destroy instance ID_DE_LA_MACHINE -y        # identifiant consigné à l'étape 2, jamais un motif
vastai show instances                               # l'identifiant doit être ABSENT de la liste
```

Ne jamais conclure la destruction du code de sortie (défaut constaté sur l'outil du loueur 1.11.0, R-2789) : seule l'absence de
l'identifiant dans la liste la prouve. Si l'identifiant reste listé, recommencer la destruction **par ce seul identifiant** et relire la
liste ; aucune instance intouchable n'est nommée dans aucune commande. Consigner l'arrêt (identifiant, heure `date -u`, liste relue).

## 11. Ce que la répétition locale a montré (compte organisme, sans appel ni clé)

Secret public de développement (32 octets nuls), phrase de répétition, 4 processeurs : `generer` 12 min (4 mondes conformes, 7 tirages
refusés puis remplacés) ; `preparer`, `jouer --mode a_blanc` (16 appels factices complets), `mesurer`, `lire`, `rapatrier`
(« aucun_monde » vrai) : code 0 chacun (pièces : `repetition-locale/`). L'issue qu'affiche `lire` sur la répétition n'est pas un
résultat. Non éprouvés par la répétition : la location, l'envoi par `scp`, le passage des clés, les 16 appels réels, la destruction.
