# Contre-lecture de la commande de la mère au compte 2 (ouverture pleine de P3-bis et lecteur du verdict) — v1

- **Objet** : `docs/procedures/P3-bis-commande-compte-2-v1/commande-ouverture-verdict-p3bis-compte-2-v1.md`
  (`e9974afed2f39bc73e5491701fa729f49098384c35ba9d91327bcdea08131023`, égale à son compagnon) et ses cinq pièces
  (R-2673, R-2683 ; fait neuf R-2684).
- **Contre-lecteur** : sous-agent neuf de la session mère, **modèle B** (autre que le modèle A du rédacteur ; identités
  dites en conversation seulement, R-2598), du 2026-11-14T09:33:22Z au 2026-11-14T09:43:58Z (heures relevées par `date -u`). Il n'a
  écrit aucune pièce de P3-bis ni de cette commande ; il ne sera ni lecteur ni auteur du verdict.
- **Ce qui a été lu** : le dossier de la commande en entier ; la procédure du rendez-vous v1 (sections 1, 2, 4, 5, 6, 8) ;
  la consigne du lecteur v1 ; le texte scellé de P3-bis aux lignes citées ; le module de S tiré par `git show`
  (`4a54a437…`, 1 418 lignes) ; `registres/scellements-v1.md`, `registres/prealables-p3bis-v1.md` ; le brief du compte 2 ;
  les lignes R-2547, R-2598, R-2637, R-2673, R-2683, R-2684 de `registres/decisions.md`.
- **Ce qui n'a pas été fait** : aucun appel de la garde en mode réel ; aucun paquet ouvert ; de `calcul/p3bis-reel-v2`,
  la tête seule par `git ls-remote` ; de `donnees/t07-etape-a-v1`, les deux compagnons seuls (dépôt jetable sans contenu,
  effacé ensuite) ; du texte scellé de T0.7, l'empreinte seule ; aucun fichier de la liste des interdits.
- **Sigles** : UTC = temps universel coordonné ; « empreinte » = condensé sha256 ; « compagnon » = fichier `.sha256`
  voisin ; S = révision `8f8df8b2726a69568b4d4a54bae16188e7f1b3d0` ; « module, l. » = `ouverture_p3bis_v3.py` de S ;
  « texte, l. » = `prereg/P3-bis-temoin-positif-v1.md` (`76ab66ce…`) ; « commande, l. » = le fichier contre-lu.

## 0. Verdict

**Remettable après corrections.** Aucun constat bloquant. Cinq constats majeurs, tous sur l'irréversibilité : la commande
prévient bien les refus de la garde qui tiennent aux registres, mais pas ceux qui tiennent aux **paquets**, ni un
processus tué entre la ligne d'ouverture et l'extraction, ni une poussée refusée après l'ouverture. Les corrections C1 à
C5 les ferment sans toucher à un texte scellé. Le diagnostic des deux compagnons absents et sa correction sont
**confirmés** par un rejeu indépendant. La pose des compagnons n'est **pas** un écart au texte scellé.

Les corrections changent des blocs : la répétition de bout en bout est à rejouer sur la version 2 (l'empreinte des
blocs citée à l'annexe B, `2aeb04c0…`, que j'ai retrouvée à l'identique, changera).

## 1. Ce que j'ai rejoué (lecture seule)

| contrôle | résultat |
|---|---|
| Empreintes des six fichiers du dossier contre leurs compagnons et contre la table de la commande (l. 23-27) | égales, six sur six |
| Module de S tiré par `git show` : cinq fichiers contre les empreintes du bloc 4 (commande, l. 322-326) | égales ; `lecture_p3bis_v1.py` `bfe0effc…` et `lecture_p3bis_v2.py` `c7a060c8…` égales à leurs compagnons de S |
| Onze pièces du bloc 2 (f) (commande, l. 237-247) et empreintes de lancement | conformes (le texte de T0.7 seulement haché) |
| Têtes au distant, 09:35:20Z | `calcul/p3bis-reel-v2` = `2aaaaf872356e51272a36e670d348603a31f32f3` ; `donnees/t07-etape-a-v1` = `0c176db582ec13705e8fb7cc2d281215e2766e42` ; `verdict/p3bis-compte-2-v1` absente ; `main` avait avancé (`a6b5d5a7`, puis `2ac07f79`) |
| Registres lus par la garde, `main` distant contre la copie de travail | mêmes blobs (`686a53b3…`, `f7695d10…`) : les sept lignes « attendu » du bloc 2 (e) valent toujours ; aucun journal des ouvertures sur `main` |
| Deux compagnons de T0.7 par la suite exacte du bloc 3 | blobs `34181fd1…` et `60d8dfb0…`, 89 et 82 octets, empreintes `5f5672fc…` et `77af718b…` : égaux à la commande ; aucun fichier extrait |
| Garde de S (`garde_ouverture`, mode `pleine`) sur une copie des registres **sans** les compagnons, 09:35:39Z | `REFUS ni-scores-ni-ouvrir`, avec `[compagnon-absent]` pour `SCORES-T07` et pour `SONDES-T07` : diagnostic de la commande confirmé |
| Même garde, copie **avec** les deux compagnons | autorisée, « chemin normal », appui `SCORES-T07=13ac4480… SONDES-T07=aa689232…`, trois lignes d'écrit, aucune décision, aucune ligne antérieure ; aucun journal créé |
| `controle_a_blanc_compte_2_v1.py` sur ces deux copies, liste factice | « TOUT CONFORME », code 0 ; et arrêt « compagnon … absent de la racine » |
| Crochet `garde_calcul.py` rejoué sur le texte de chacun des 13 blocs ; `bash -n` | les 13 passent ; syntaxe saine (la répétition lançait les blocs par fichier : le crochet n'y voyait pas leur texte) |
| Numéros de ligne de l'annexe A contre le module de S | tous exacts (l. 166, 396-427, 470, 555, 663, 767-809, 834-872, 993-997, 1030-1042, 1067-1074, 1133-1220, 1224-1234, 1262-1273, 1276-1291, 1304, 1308, 1310, 1325-1353) |
| Lignes du texte scellé citées (l. 1566-1567, 1611-1614, 1700-1705) | exactes |

## 2. Réponses aux six questions

### 2.1 Irréversibilité : chaque refus est-il prévenu avant l'appel réel ?

**Refus tenant aux registres : oui.** Le bloc 5 rejoue `garde_ouverture` elle-même, sur la racine même que lira l'appel
réel. Sont donc prévenus, par la garde et non par une imitation : `registre-absent`, `ligne-absente`, `ligne-double`
(module, l. 927-933 et 960-962), `ligne-mal-formee`, `cle-inconnue`, `sceau-faux` et `compagnon-absent` (l. 976-990,
1030-1042), `date-posterieure` (l. 993-997), les refus de rendez-vous, `deja-ouverte`. Le bloc 2 (e) compte les lignes
par `grep '^| CLÉ |'`, plus étroit que la garde (qui lit toute ligne commençant par `|` après retrait des espaces) : sans
conséquence, le bloc 5 fait foi. Les antériorités ne se jugent que contre l'horloge (l. 1151-1158) : elles ne peuvent que
s'améliorer entre le bloc 5 et le bloc 8, et le bloc 2 (a) contrôle l'horloge. `SCELLEMENT-VADAPT` (2026-11-14T08:18:30Z,
inscrite avant `VERDICT-P3BIS`) est sans effet sur la garde, qui ne lit que trois clés du registre des scellements
(l. 945-965). Journal absent : contrôlé aux blocs 2, 5 et 8, sur la racine et sur `main`.

**Refus tenant aux paquets : non** (constat M1). Après la garde, `ouvrir` lit la date de la mise en paquet puis relit
les deux paquets (l. 1295-1302) ; tout défaut y donne `paquet-faux`, **journalisé** (l. 1304). Le bloc 7 ne contrôle que
le paquet des lectures ; du second paquet, il ne lit que l'empreinte dans l'index.

**Processus interrompu : non** (constat M2). **Poussée après l'ouverture : jamais éprouvée** (constat M3).

### 2.2 La pose des deux compagnons de T0.7 : conforme, pas un écart

- Le texte exige (l. 1703-1705) que « le compagnon `.sha256` du fichier cité [soit] présent et égal à l'empreinte de la
  ligne ; le fichier de T0.7 lui-même n'est vérifié que s'il est présent dans le clone (D8 : aucun fichier fermé de T0.7
  n'est déplacé pour cela) ». Il pose une condition sur la racine de la garde ; il ne dit ni d'où vient le compagnon ni
  qu'il doit être commité. D8 interdit de déplacer le **fichier fermé**, pas son compagnon — et présuppose justement que
  le compagnon, lui, est là sans le fichier.
- Le module fait exactement cela (l. 1035-1041) : compagnon exigé, fichier haché seulement s'il est présent.
- Le compagnon ne porte qu'une empreinte et un nom, déjà écrits à l'octet dans les lignes `SCORES-T07` et `SONDES-T07`
  de `main`, et à nouveau dans la ligne d'ouverture du journal : il n'apprend rien. Il vient de la branche où l'étape A
  l'a poussé (R-2637), vérifié par blob et par empreinte.
- Il n'est pas donné au lecteur (retiré au bloc 9, avant le bloc 10 ; le bordereau refuse tout nom en `t07`) : le point 7
  du texte (l. 1563-1565) est tenu.
- Le commiter dans `main` serait pire : `diag/` est un dossier scellé, et `verifier-arbre` y verrait une « empreinte
  orpheline » à chaque reprise de la mère (`scellement.py`, l. 103-106).

Réserves mineures : constat m6.

### 2.3 Voie d'écriture : admise par le module et par le texte

- Le module n'écrit dans la racine que le journal, relatif à `--racine` (l. 166, 851-872), ne lance aucune commande git
  sur elle (la seule, l. 1230, porte sur `--racine-paquets`) et n'exige que l'existence de `registres/` (l. 857-858).
- Le texte (l. 1612-1614) : journal « écrit par la **seule garde `ouvrir`** […] commité et poussé par la session avec
  l'ouverture ou le refus qu'il consigne ». La session qui ouvre est celle du compte 2 ; la recopie par la mère garde le
  blob (la répétition le vérifie par `cherry-pick`).
- Le compte 2 n'écrit rien dans `registres/` de `main` : toutes ses poussées nomment `refs/heads/verdict/p3bis-compte-2-v1`
  (commande, l. 460, 621, 676) ; le bloc 9 refuse tout autre changement sous `registres/` et tout autre fichier à l'index
  (l. 452-454) ; ses faits vont dans `registres-provisoires/`.
- « La session mère scelle les deux (compagnons), commit, pousse » (texte, l. 1566-1567) : ici le compte 2 scelle
  d'abord sur sa branche, la mère rescelle sur `main`. Lecture tenable (constat m7).

### 2.4 Isolement du compte 2 : tenu

La commande ne fait lire au compte 2 ni le texte de T0.7 (haché au bloc 2 (f), puis par la garde), ni la procédure du
rendez-vous (les commandes sont recopiées), ni rien de 7a ou 7b. De `donnees/t07-etape-a-v1`, deux blobs nommés, jamais
affichés. Le lecteur reçoit exactement la liste de la section 6.1 de la procédure (mêmes dix pièces, journal, sortie de
la garde, extrait des 21 lignes, classe 1, traces), plus un contrôle des noms interdits que la procédure n'avait pas. Le
message de remise n'ajoute que les interdits permanents et la note de modèle. Réserve : constat m8.

### 2.5 Perte de session entre l'ouverture et la poussée : parade proposée

Voir le constat M4 et la correction C4. En bref : (1) réduire la fenêtre où le journal n'existe que sur le disque du
conteneur, en lançant les blocs 8 et 9 dans le même appel ; (2) éprouver la poussée avant l'appel ; (3) faire trancher
**d'avance** par Lazar la voie de reprise. Je ne recommande **pas** de pousser les fichiers extraits, même chiffrés.

### 2.6 Marqueurs, chemins, empreintes

Toutes les empreintes citées sont vérifiées (section 1). Marqueurs restants : `<<LISTE>>` et `<<EMPREINTE_LISTE>>`
(commande, l. 161 ; le bloc 1 s'arrête tant qu'ils restent), `<<MODÈLE_B>>` (conversation), cinq marqueurs remplis par
programme au bloc 11. « `main` `54aece9f` » (l. 45, 750) est périmé sans conséquence (registres inchangés).

## 3. Constats

### Majeurs

**M1 — Le refus `paquet-faux` n'est prévenu par aucun contrôle à blanc.** Commande, l. 392-405 (bloc 7) ; module,
l. 1224-1259 et 503-535. Avant d'écrire la ligne d'ouverture, la garde exige : la date du commit du paquet (`git log`,
l. 1230-1233), le compagnon de l'index, chaque morceau avec son compagnon, son empreinte et sa taille égales à l'index,
les morceaux réunis égaux à l'index. Dans un dépôt sans contenu où les morceaux arrivent à la demande, un morceau
manquant ou tronqué est le défaut le plus vraisemblable du jour, et il donnerait une ligne `REFUS-OUVERTURE-P3BIS`
définitive. Tout cela se contrôle par empreintes seules (classe 1 : « empreintes des deux paquets et de leurs morceaux »,
texte, l. 1489-1506), sans rien déplier. Reste non prévenu, par nature : la structure interne (sel, flux comprimé,
membres), vérifiée à la fermeture et figée par les empreintes. → **C1**. J'ai éprouvé le contrôle proposé sur un paquet
jouet fait par `fermer_run` de S : cas sain conforme ; morceau altéré et compagnon absent arrêtés.

**M2 — Empreinte entière du paquet des lectures (question de la mère, R-2684) : oui, à contrôler à l'égalité.**
Commande, l. 395-396 : seul le préfixe `0fb83f67` est comparé. L'égalité à
`0fb83f67e92b8041294a47448990e828a9dcea87b97cab80bc79da3919bc12f1` (64 caractères, préfixe cohérent) ne coûte rien et se
fait avant l'appel : une erreur de transcription ne donnerait qu'un arrêt sans ligne. Le gain de sûreté est modeste (la
tête `2aaaaf87…` entière fige déjà le blob), mais le contrôle ne dépend plus d'un préfixe de 32 bits. Je n'ai pas pu
vérifier cette empreinte contre le paquet (branche interdite) : le bloc 7 le fera. → **C1** (même couple). La répétition
remplace aujourd'hui `0fb83f67` par `sed` (`repetition_commande_jouet_v1.sh`, l. 99) : avec l'empreinte entière en
variable, sa surcharge se fait en fin de `variables-v1.sh`, comme `TETE_CALCUL` (script de répétition en version 2).

**M3 — Rien ne protège l'appel de la garde contre le délai de l'outil de commande.** Commande, l. 138-142 et 424-426 ;
module, l. 1308-1313. L'outil tue une commande au bout de son délai (deux minutes par défaut, dix au plus). La garde
relit plusieurs fois T octets, puis les écrit. Tuée **après** la ligne `OUVERTURE-P3BIS` et **avant** le renommage du
dossier de sortie (l. 1270), elle laisse le pire état : ouverture journalisée, rien d'extrait, seconde ouverture
refusée. Tuée avant la ligne, elle ne laisse rien, mais la commande ne dit pas quoi faire. La taille T n'est connue
qu'au bloc 6. → **C2** (délai maximal exigé, mesure de durée au bloc 7 qui arrête avant l'appel si elle est trop longue,
règle écrite pour un appel qui rend la main sans code).

**M4 — La première poussée réelle a lieu après l'irréversible.** Commande, l. 460 ; annexe B, l. 791-792 (limite
déclarée). Si le compte 2 ne peut pas pousser `verdict/p3bis-compte-2-v1` (droit, mandataire, règle de branche), on ne
l'apprend qu'au bloc 9 : journal écrit, non poussé, « arrêt ». → **C3** : pousser la branche neuve, encore égale à
`main`, juste avant l'appel ; un refus arrête sans rien journaliser.

**M5 — Perte de session : la commande la classe en nœud sans réduire la fenêtre ni préparer la reprise.** Commande,
l. 708-709. Deux fenêtres distinctes :
- *entre la ligne d'ouverture et la poussée du journal* (blocs 8 et 9 dans deux appels) : si le conteneur meurt là, le
  journal disparaît avec lui ; `main` et la branche disent « aucune tentative » alors qu'une ouverture a eu lieu. C'est
  le seul cas où la trace elle-même se perd. → **C4 (a)** : blocs 8 et 9 dans un seul appel ;
- *après la poussée du journal, avant celle du verdict* : la trace est sauve, les fichiers extraits et le verdict en
  cours sont perdus. Les paquets restent intacts sur `calcul/p3bis-reel-v2`, et l'extraction est déterministe : les
  fonctions `lire_paquets` et `extraire` de S redonnent les mêmes octets sans écrire au journal. Le texte ne compte comme
  écart qu'une ouverture hors de la garde « avant une ouverture autorisée » (l. 1981-1982) ; ici elle viendrait après.
  C'est une lecture du texte, donc un mot de Lazar. → **C4 (b)** : le lui demander **avant** la remise, pour que la perte
  ne fige pas P3-bis.
- *pousser les fichiers extraits chiffrés avant la remise* : je ne le recommande pas. Il faudrait une clé (perdue avec
  la session si elle y vit, ou à fournir par Lazar), du code neuf non scellé dans la fenêtre critique, et cela pousse
  des résultats avant que le verdict soit écrit, alors que la reprise ci-dessus n'expose rien et ne demande aucun code.

### Mineurs

**m6 — Compagnons de T0.7 : trois retouches.** (i) Le dépôt jetable `$CT` garde les arbres et les messages de commit de
la branche de T0.7 : l'effacer en fin de bloc 3. (ii) Au bloc 9, le retrait des compagnons (l. 469-473) vient après
l'arrêt sur code non nul (l. 463) : en cas de refus, ils restent dans la racine ; les retirer avant. (iii) Dire la pose
dans la section 0 comme une lecture du texte que Lazar accepte en remettant la commande (elle y est déjà, l. 42-46 ;
ajouter « conforme au texte, l. 1703-1705 »).

**m7 — « La session mère scelle les deux ».** Commande, l. 600 et 729-730 ; texte, l. 1566-1567. Le compte 2 scelle
avant la mère parce que `exposer-issue` exige le compagnon du fichier d'issue (module, l. 1329). Le compagnon est
déterministe et la mère rescelle : la lettre est tenue. À écrire en section 0, pas seulement à l'annexe A.

**m8 — Liste « qui a lu quoi » : périmètre à fixer.** Commande, l. 123 ; `controle_a_blanc_compte_2_v1.py`, l. 97-100.
Le contrôle arrête dès qu'une ligne nomme le compte 2. Si la liste recense toutes les lectures (le compte 2 a lu des
pièces de l'état de l'art), l'attestation arrêtera à tort. Préciser que la liste ne porte que les lectures qui excluent
du verdict (T0.7 et ses sorties, 7a, 7b, `lecture-sondes-t06.json`, procédure du rendez-vous, pièces de P3-bis en tant
qu'auteur ou contre-lecteur). L'attestation porte sur la session hôte et le compte, pas sur le lecteur, qui se déclare
lui-même : la commande le dit (l. 111-113).

**m9 — Bloc 2 : la branche est créée avant la fin des contrôles.** Commande, l. 210 puis 213-255. Un arrêt en (d), (e)
ou (f) laisse la branche locale créée et `$BAC` présent : le bloc n'est plus relançable, et la section 14 ne permet de
relancer que le bloc 1. Déplacer (c) en fin de bloc 2, ou écrire la reprise.

**m10 — Place disque non revérifiée avant l'appel.** Commande, l. 364-368. La marge de 3 × T + 1 Gio est prise avant
l'extraction du clone ; un disque plein pendant `extraire` survient **après** la ligne d'ouverture. Revérifier au
bloc 8 : disque libre d'au moins T + 1 Gio (dans **C3**).

**m11 — Ligne 1 « non lu ».** Commande, l. 607-608 : le bloc 12 exige `lecture-p3bis.json` même si l'issue est la
ligne 1, où `exposer-issue` ne le demande pas (module, l. 1341). Cas fermé en pratique par le bloc 7 (run sans résumé :
arrêt). À noter seulement.

**m12 — Répétition : le dépôt jetable sans contenu n'est pas éprouvé sur la branche de calcul.** Sortie de la
répétition, l. 46 : « filtering not recognized by server, ignoring ». Le bloc 3 l'éprouve sur le dépôt réel, et j'ai
vérifié qu'un `git log` limité à un chemin y répond hors ligne. Limite à écrire à l'annexe B.

**m13 — Hors périmètre, pour la mère.** `SCELLEMENT-VADAPT` n'est pas dans `CLES_CONNUES` du lecteur de registre de T0.7
(`src/controle_ia/t07/registre_v1.py`, l. 58-60), dont la règle refuse une clé « ni exigée ni permise » si sa marque
n'est pas déclarée (l. 138-150). Je n'ai pas tracé l'appel de l'étape B : à vérifier avant elle. Sans effet sur
l'ouverture de P3-bis ni sur `VERDICT-P3BIS`.

## 4. Corrections (couples ancien texte / nouveau texte)

### C1 — bloc 1 et bloc 7 : empreinte entière, second paquet, date de la mise en paquet (M1, M2)

Ancien (commande, l. 179) :

```text
TETE_CALCUL=2aaaaf872356e51272a36e670d348603a31f32f3; BRANCHE=verdict/p3bis-compte-2-v1
```

Nouveau :

```text
TETE_CALCUL=2aaaaf872356e51272a36e670d348603a31f32f3; BRANCHE=verdict/p3bis-compte-2-v1
PAQUET_LECTURES=0fb83f67e92b8041294a47448990e828a9dcea87b97cab80bc79da3919bc12f1     # R-2684
```

Ancien (commande, l. 395-396) :

```text
case "$H" in 0fb83f67*) echo "conforme : paquet des lectures $H (préfixe 0fb83f67, R-2547)";;
             *) arret "paquet des lectures d'un autre préfixe que 0fb83f67";; esac
```

Nouveau :

```text
[ "$H" = "$PAQUET_LECTURES" ] && echo "conforme : paquet des lectures $H (empreinte entière, R-2684)" \
    || arret "paquet des lectures d'une autre empreinte que $PAQUET_LECTURES"
```

Ancien (commande, l. 405-406) :

```text
echo "$R2" > "$BAC/paquet-run-sha256-v1.txt"; echo "second paquet (index, classe 1) : $R2"
# attendu : sept « conforme », cinq « OK », l'empreinte du second paquet ; aucun « ARRÊT »
```

Nouveau :

```text
echo "$R2" > "$BAC/paquet-run-sha256-v1.txt"; echo "second paquet (index, classe 1) : $R2"
# ce que la garde exigera des paquets avant d'écrire sa ligne (module, l. 1224-1259 et 503-535), par empreintes seules
git log -1 --format=%ct -- "$P" | grep -qx '[0-9][0-9]*' && echo "conforme : date de la mise en paquet lisible" \
    || arret "date de la mise en paquet illisible : la garde refuserait (paquet-faux)"
t0=$(date -u +%s)
PYTHONPATH="$M" "$PY" -B - "diag/$RUN" "$R2" <<'FIN' || arret "second paquet : index, morceaux ou compagnons non conformes ; la garde n'est pas appelée"
import hashlib, json, sys
from pathlib import Path
from controle_ia.scellement import verifier          # la fonction même que la garde applique (module de S)
d, attendu = Path(sys.argv[1]), sys.argv[2]
verifier(d / "paquet-run-ferme-v1.json")
x = json.loads((d / "paquet-run-ferme-v1.json").read_text(encoding="utf-8"))
assert x.get("version") == 1 and x.get("run") == d.name and x.get("paquet") == "paquet-run-ferme-v1.tar", "index d'un autre run"
assert x["sha256"] == attendu, "empreinte de l'index"
m = x["morceaux"]
assert m and [y["nom"] for y in m] == [f"paquet-run-ferme-v1.tar.{k:03d}" for k in range(len(m))], "noms des morceaux"
tout, n = hashlib.sha256(), 0
for y in m:
    assert verifier(d / y["nom"]) == y["sha256"], y["nom"]
    b = (d / y["nom"]).read_bytes()
    assert len(b) == y["taille"] <= 90_000_000, y["nom"]
    tout.update(b); n += len(b)
assert tout.hexdigest() == x["sha256"] and n == x["taille"], "morceaux réunis"
print(f"conforme : second paquet, {len(m)} morceau(x), {n} octets ; index, morceaux et compagnons égaux")
FIN
D=$(( $(date -u +%s) - t0 )); echo "durée du contrôle des morceaux : $D s"
[ "$D" -le 120 ] || arret "contrôle des morceaux de plus de 120 s : la garde risquerait le délai de l'outil ; rapport à la mère"
# attendu : neuf « conforme », cinq « OK », l'empreinte du second paquet, la durée ; aucun « ARRÊT »
```

(Le compte des « conforme » est à recompter sur la sortie de la répétition rejouée. Le seuil de 120 s est une
proposition : la garde fait environ trois passes de ce coût, dix minutes étant le délai maximal de l'outil.)

### C2 — mode d'emploi : délai de l'outil (M3)

Ancien (commande, l. 141-142) :

```text
- **Quota** : au-dessus de 80 % (brief, section 7), tu ne lances pas le bloc 6. Du bloc 6 à la poussée du bloc 12, **aucune
  pause** : après la ligne d'ouverture, aucune seconde ouverture n'est possible (refus `deja-ouverte`).
```

Nouveau :

```text
- **Quota** : au-dessus de 80 % (brief, section 7), tu ne lances pas le bloc 6. Du bloc 6 à la poussée du bloc 12, **aucune
  pause** : après la ligne d'ouverture, aucune seconde ouverture n'est possible (refus `deja-ouverte`).
- **Délai de l'outil** : les blocs 6, 7 et 8-9 se lancent avec le **délai maximal** de ton outil de commande (dix minutes),
  au premier plan, jamais en tâche de fond. Si l'outil rend la main sans la ligne « code de la garde : … » (délai dépassé,
  commande interrompue) : tu ne relances **rien** ; un seul appel à part, `[ -e registres/ouvertures-p3bis-v1.md ] && echo
  présent || echo absent`, puis arrêt et rapport à la mère avec ce mot (nœud de Lazar dans les deux cas).
```

### C3 — bloc 8 : poussée éprouvée et place revérifiée avant l'appel (M4, m10)

Ancien (commande, l. 423) :

```text
cd "$CLONE"
```

Nouveau :

```text
# la poussée est éprouvée avant l'irréversible : la branche neuve, encore égale à main, est poussée (un refus n'a rien journalisé)
[ "$(git -C "$DEPOT" rev-parse HEAD)" = "$(cat "$BAC/c-main-v1.txt")" ] || arret "ta branche n'est plus sur la base main"
git -C "$DEPOT" push -q origin "refs/heads/$BRANCHE:refs/heads/$BRANCHE" || arret "poussée de la branche refusée : la garde n'est pas appelée"
T=$(cat "$BAC/taille-second-paquet-v1.txt"); LIBRE=$(df -B1 --output=avail "$ESPACE" | tail -1)
[ "$LIBRE" -ge $((T + 1073741824)) ] || arret "disque insuffisant pour l'extraction : la garde n'est pas appelée"
cd "$CLONE"
```

(Conséquence pour la section 15, point 1 : inchangée, le commit du journal garde la base `main` pour parent. La
répétition doit rejouer ce bloc contre son faux dépôt distant.)

### C4 — perte de session (M5)

(a) Ancien (commande, l. 411, titre de la section 11) :

```text
## 11. Blocs 8 et 9 — appel de la garde, journal relu, commité, poussé
```

Nouveau :

```text
## 11. Blocs 8 et 9 — appel de la garde, journal relu, commité, poussé

**Ces deux blocs se lancent dans un seul appel de ton outil**, collés l'un sous l'autre, dans l'ordre : le journal ne
doit jamais n'exister que sur le disque de ton conteneur plus longtemps que le temps de le pousser.
```

(b) Ancien (commande, l. 708-709) :

```text
- Session ou conteneur perdus après la ligne d'ouverture et avant la poussée du verdict : nœud de Lazar ; aucune seconde
  ouverture n'est possible (`deja-ouverte`) et aucun paquet ne s'extrait hors de la garde.
```

Nouveau (si Lazar retient la reprise ; sinon l'ancien texte reste) :

```text
- Session ou conteneur perdus après la ligne d'ouverture et avant la poussée du verdict : nœud de Lazar ; aucune seconde
  ouverture n'est possible (`deja-ouverte`). Voie de reprise, **sur mot de Lazar seulement**, par une commande neuve de
  la mère à une session neuve de ce compte : les mêmes paquets, vérifiés aux empreintes de la ligne du journal, sont
  redépliés par les fonctions `lire_paquets` et `extraire` du module de S, sans appel de `ouvrir` et sans ligne neuve ;
  un lecteur neuf écrit le verdict ; l'écart (« paquets redépliés hors de la garde après l'ouverture pleine du <date> »)
  est déclaré au verdict et au registre.
```

Décision à demander à Lazar avant la remise — **enjeu** : sans elle, une session perdue fige P3-bis jusqu'à un nœud
traité à chaud. **Options** : (1) reprise par redépliage écrite d'avance (avantage : aucune exposition, aucun code neuf
le jour même ; inconvénient : une lecture du texte, l. 1981-1982, à assumer) ; (2) nœud le moment venu (avantage : rien
à trancher aujourd'hui ; inconvénient : attente) ; (3) fichiers extraits poussés chiffrés avant la remise (avantage :
reprise sans redépliage ; inconvénient : clé, code neuf dans la fenêtre critique, résultats poussés avant le verdict).
**Recommandation : (1), confiance 0,7.** Défaut : (2), le texte actuel.

### C5 — retouches mineures (m6, m8)

Ancien (commande, l. 294, bloc 3) :

```text
echo "fichiers extraits hors .git dans $CT : $(find "$CT" -path "$CT/.git" -prune -o -type f -print | wc -l)"
```

Nouveau :

```text
echo "fichiers extraits hors .git dans $CT : $(find "$CT" -path "$CT/.git" -prune -o -type f -print | wc -l)"
rm -rf -- "$CT" && echo "dépôt jetable des compagnons effacé"
```

Ancien (commande, l. 463, bloc 9) : la ligne `[ "$CODE" = 0 ] || arret "la garde a rendu le code $CODE : …"` précède le
retrait des compagnons (l. 469-473). Nouveau : déplacer les lignes 469 à 473 (retrait et contrôle du retrait) juste
avant la ligne 463, sans autre changement.

Ancien (commande, l. 123, fin de la cellule) :

```text
une ligne par lecture déclarée | bloc 1 |
```

Nouveau :

```text
une ligne par lecture **qui exclut du verdict** (T0.7 et ses sorties, 7a, 7b, `lecture-sondes-t06.json`, procédure du rendez-vous, écriture ou contre-lecture d'une pièce de P3-bis) et elles seules : toute ligne qui nomme le compte 2 arrête le bloc 5 | bloc 1 |
```

## 5. Ce qui reste hors de portée de cette contre-lecture

La garde sur les vrais paquets, leur taille T, la durée réelle de l'appel, la poussée réelle du compte 2 et le vrai
lecteur ne sont éprouvés que le jour même. Les corrections C1 à C3 déplacent chacune de ces inconnues **avant** la ligne
d'ouverture. Je n'ai pas rejoué la répétition de bout en bout (elle crée un environnement et un dépôt de 13 blocs) :
j'ai rejoué ses contrôles un à un et retrouvé l'empreinte de ses blocs.
