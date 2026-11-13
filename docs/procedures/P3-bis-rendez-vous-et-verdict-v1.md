# P3-bis — jour du rendez-vous (20 novembre 2026, 12:00 UTC) et remise au lecteur du verdict — procédure v1

- **Statut** : procédure d'exécution, **non décisive**. Elle applique le texte scellé de P3-bis et son module scellé
  d'ouverture ; elle n'en change rien. Si elle les contredit, le texte et le module font foi et l'écart se signale (nœud de
  Lazar s'il touche une ouverture). En l'écrivant, rien n'a été ouvert ni inscrit.
- **Rédacteur** : sous-agent neuf (Claude Opus 5.5, `claude-opus-5-5`) de la session mère
  `session_01QPDgKgACWyCkCN8HjqwNXy`, du 2026-11-13T18:00Z au 2026-11-13T18:39Z (heures relevées par `date -u`). Il n'a écrit aucune
  pièce de P3-bis ni de T0.7 ; il ne sera **ni lecteur ni auteur du verdict** ; il n'a ouvert ni la branche
  `calcul/p3bis-reel-v2` ni aucun paquet ; du texte scellé de T0.7, il n'a calculé que l'empreinte (égale à son compagnon et
  aux deux lignes de registre qui le citent), sans le lire.
- **Sigles** : UTC (temps universel coordonné) ; JSON (format de données texte) ; « empreinte » = condensé sha256 d'un fichier ;
  « compagnon » = fichier `.sha256` voisin (règle R6) ; GO = accord de dépense de Lazar inscrit à `registres/go.md`.
- **Pièces lues** (empreinte recalculée avant lecture, égale au compagnon ; registres vivants sans compagnon : empreinte au
  commit cité) :

| pièce | empreinte | où |
|---|---|---|
| `prereg/P3-bis-temoin-positif-v1.md` (texte scellé, « le texte ») | `76ab66ce967796b944e2ca585ee0dc2d780189e8e0cbe429e390c427a46121cb` | `main` |
| `prereg/P3-bis-temoin-positif-config-v1.json` | `612b0c6ce5c4263eb3016b72ad85155dd2307f9dd887379d2a1133ed644a9d05` | `main` |
| `prereg/P3-bis-consignes-v1.md` | `7d35576d65c030edcc6441e142ea95732679b674edcb1fd1af86ab8f69c04367` | `main` |
| `prereg/P3-bis-addendum-1-garde-credit-v1.md` (« A1 ») | `4e188814b52736edb6f690931b25e6c0d9cdaede20b23490d50aa5461c5ca537` | `main` |
| `prereg/P3-bis-addendum-2-telechargement-controle-v1.md` (« A2 ») | `c23b2eb0beb5de34db4359b9b97624df09c9b076d5ebe3d20c5b74e257ec9444` | `main` |
| `prereg/P3-bis-addendum-3-relance-credit-v1.md` (« A3 ») | `02674ff7693d4dee069abea8d48fd27826f98455084dbf4da4724d8bf72cb103` | `main` |
| `docs/decisions/decision-N-066-v1.md` | `21e83ed58c7498c65b7f9ae78613bc38301acdf0dd15a9890af13e6c0edbd351` | `main` |
| `src/controle_ia/premier_test_ia/ouverture_p3bis_v3.py` (« le module ») | `4a54a437e4a6031b1890f0f5f0261cf1141e72aee82d456d9fcd5483946693e9` | `scellement/p3bis-v2` = S `8f8df8b2726a69568b4d4a54bae16188e7f1b3d0`, par `git show` |
| `tests/test_premier_test_ia_ouverture_p3bis_v3.py` | `205b2f41a83b999609c89ff6d47d7dc723dddbbf9823809364d0cffc309ea29c` | S |
| `src/controle_ia/premier_test_ia/lecture_p3bis_v2.py` | `c7a060c83b51c023d84448cb237e3479d39ce6860b64a5d292b65e63c41d1646` | S |
| `src/controle_ia/premier_test_ia/lecture_p3bis_v1.py` | `bfe0effcfa0d7f525872410a7f9823c509cac878143a4fdcce7d207dfbddfea9` | S et `main` |
| `docs/procedures/P3-bis-temoin-positif-v1/recuperation_p3bis_v2.sh` | `3b21c80cf9a040e779cbea2832f513d299b08c291eeed169cb8d1670df735cd9` | S |
| `registres/decisions.md` | `3deb5cc46671f86c1ff3bd510d14c0a5b2ae9438db5625119a66f79541863e9a` | `main`, commit `07b4d7c567223f3645aa143f9ba5738084fabeab` |
| `registres/prealables-p3bis-v1.md` | `ca7e743a2082882a21e3cdbe22dfeaf88473b463d2c2107a561f95147726d7ab` | idem |
| `registres/scellements-v1.md` | `1eaab114be2b8d44797645cf0791f9dd639cd13195784f170235f9d16259d3d8` | idem |
| `registres/depenses.md` ; `registres/arrets.md` | `4e61067974100bbdb279825e69b7e717891786cccad70e6138d04f8ab5dc5ef7` ; `55a87e3bdc2a108ebf494d505d1e866155751673e48ed79b5e64b9126ee5f506` | idem |
| `registres/passations/2026-11-13-1732.md` | `a808b3eeff198936f13cc1367cb3e264799d8dc119a0635074039ccf4375cbc6` | `main` |
| `prereg/T0.7-sondes-v0-v1.md` (empreinte seule, **non lu**) | `d7d180eccbbce8ff2e370f82957543c28f1e564c872f981c7ada403949baade5` | `main` |

Les numéros « l. » renvoient au fichier nommé à côté ; « le texte, l. » = `prereg/P3-bis-temoin-positif-v1.md` ; « le module,
l. » = `ouverture_p3bis_v3.py` ; « registre, l. » = `registres/decisions.md` au commit `07b4d7c5`.

## 0. Verdict d'abord (pour Lazar)

1. **Ce que tu écris, et quand** : au plus tôt le **2026-11-20 à 12:00:00 UTC** (13:00 à Paris), et seulement si les lignes
   `SCORES-T07` et `SONDES-T07` ne sont pas inscrites et conformes à ce moment, un seul mot, sans voir les sorties fermées :
   « maintenir », « ouvrir » ou « ouvrir pleinement ». Un mot reçu avant 12:00:00 UTC ne vaut pas décision (la garde le refuse).
2. **Blocage à lever avant toute ouverture, voie normale comprise** : les **trois lignes d'écrit** (`ECRIT-PERIMETRE-JEUX-P3BIS`,
   `ECRIT-LANCEMENT-RELANCE-P3BIS`, `ECRIT-ENGAGEMENT-ETAPE-A-P3BIS`) **manquent** au registre des préalables ; sans elles la
   garde refuse tout (`ligne-absente`), contrôle à blanc à l'appui (section 8). La mère les inscrit avant (section 2) ; datées
   après la mise en paquet, elles portent la réserve gelée « écrit après la lecture fermée : sa cécité repose sur la fermeture ».
3. **Voie normale possible avant le 20** : l'étape A de T0.7 est accordée (R-2555, registre l. 2514). Si `SCORES-T07` et
   `SONDES-T07` sont inscrites et conformes avant l'heure du rendez-vous, il tombe : ouverture `pleine`, verdict entier, sans
   décision de ta part.

## 1. État constaté le 2026-11-13 vers 18:30 UTC

| fait | renvoi |
|---|---|
| Course finie (fin normale), récupération « TOUS CONFORMES », run unique `20261113-121129-p3bis-reel` ; paquet des lectures `0fb83f67…` (16 783 360 octets) poussé sur `calcul/p3bis-reel-v2`, commit `2aaaaf87` ; aucun paquet ouvert, aucun résultat lu | R-2546 et R-2547, registre l. 2505-2506 ; `registres/arrets.md` l. 113-114 |
| L'empreinte entière du paquet n'est écrite dans aucun registre (préfixe `0fb83f67` seulement) ; la garde l'écrira au journal | recherche dans `registres/etat.md`, `decisions.md`, `depenses.md`, `arrets.md` et les deux dernières passations |
| Le module n'ouvre que par la voie pleine (`SCORES-T07`, `SONDES-T07`) ou par le rendez-vous `DATE_RENDEZ_VOUS = "2026-11-20T12:00:00Z"` | le module, l. 173 ; R-2552, registre l. 2511 |
| Registre des préalables : **une seule ligne**, `GARDE-ADAPTEE-T07-P3BIS` (2026-11-11T07:12:25Z, `prereg/T0.7-sondes-v0-v1.md`, `d7d180ec…`) ; **aucune ligne d'écrit, aucune ligne de rendez-vous** | `registres/prealables-p3bis-v1.md` l. 3 |
| Registre des scellements : `SCELLEMENT-T07` (2026-11-11T07:11:42Z, même chemin, même empreinte) ; **ni `SCORES-T07` ni `SONDES-T07`**, ni `VERDICT-P3BIS` | `registres/scellements-v1.md` l. 8 |
| Garde adaptée **en vigueur** pour une décision « ouvrir » à venir : deux lignes au même texte et à la même empreinte, au chemin exigé, datées du 11 novembre (strictement avant toute ligne de rendez-vous) | le module, l. 1077-1102 ; le texte, l. 1733-1743 ; N-066, l. 15-21 |
| Journal des ouvertures `registres/ouvertures-p3bis-v1.md` **absent** : vaut « aucune tentative » ; il ne doit jamais être créé à la main (un fichier vide est hors format pour toujours) | le module, l. 805-809 et 851-866 ; le texte, l. 1640-1642 |
| Le module v3 n'est pas sur `main` (seul `ouverture_p3bis_v1.py` y est) : il se prend dans le clone de la branche de calcul, dont `src/` est celui de S | `ls src/controle_ia/premier_test_ia/` sur `main` ; `recuperation_p3bis_v2.sh` l. 126 |
| Étape A de T0.7 accordée le 13 novembre (lignes GO-2026-11-10-04 et -06) | R-2555, registre l. 2514 |
| Disque libre du conteneur de la session mère : 2,8 Go à 18:2xZ ; dépôt `.git` 2,2 Go ; mémoire disponible ≈ 9 Go | `df -h`, `du -sh .git`, `free -g` (relevés du rédacteur) |

## 2. Préalable, avant le 20 : les trois lignes d'écrit (session mère)

**Ce que dit le texte.** Le texte, l. 1583-1600 : « trois écrits exigés avant toute ouverture. Ils relèvent de T0.7, qui les
écrit ; ce texte ne les écrit pas et ne fait que les exiger, chacun par une ligne du registre des préalables qui cite, par son
chemin et son empreinte, **un seul texte** de T0.7 […] « T0.7 brouillon 16, ou son successeur gardé mot pour mot dans ces
passages, ou le texte scellé » ; la ligne est unique et jamais réécrite » ; « Chaque ligne est datée **strictement avant**
l'ouverture ; une ligne datée après la mise en paquet est acceptée avec la réserve « écrit après la lecture fermée : sa cécité
repose sur la fermeture » ». Le module exige exactement une ligne de chacune (l. 167 et 927-931) pour **tout** mode, voie
normale comprise (l. 1146-1152), sinon refus `ligne-absente`, avec sa ligne au journal.

**Qui, quand.** La session mère, qui a créé le registre (le texte, l. 1573-1576 ; R-2321, registre l. 2279), comme elle y a
inscrit la ligne de garde adaptée. Les lignes ne font que pointer le texte de T0.7 scellé sur mot de Lazar (R-2321), la
troisième forme permise. **Au plus tôt**, et en tout cas : avant tout appel de la garde ; de préférence avant le lancement de
l'étape A de T0.7 (l'écrit (i) fixe le périmètre des clés que l'étape A lira, l'écrit (iii) l'engagement de la jouer quel que
soit le verdict : le texte, l. 1587-1598) et avant la décision du rendez-vous. Inscrites après la mise en paquet du
13 novembre, elles porteront la réserve gelée ci-dessus, que la garde imprime d'elle-même (le module, l. 1306-1307) et que le
verdict recopie. Une ligne à Lazar (fait, réserve), une entrée au registre des décisions.

**Forme exacte** (trois lignes, ajoutées en fin de `registres/prealables-p3bis-v1.md`, jamais réécrites ; `<D>` = `date -u
+%Y-%m-%dT%H:%M:%SZ` au moment de l'ajout) :

~~~~text
| ECRIT-PERIMETRE-JEUX-P3BIS | <D> | prereg/T0.7-sondes-v0-v1.md | d7d180eccbbce8ff2e370f82957543c28f1e564c872f981c7ada403949baade5 |
| ECRIT-LANCEMENT-RELANCE-P3BIS | <D> | prereg/T0.7-sondes-v0-v1.md | d7d180eccbbce8ff2e370f82957543c28f1e564c872f981c7ada403949baade5 |
| ECRIT-ENGAGEMENT-ETAPE-A-P3BIS | <D> | prereg/T0.7-sondes-v0-v1.md | d7d180eccbbce8ff2e370f82957543c28f1e564c872f981c7ada403949baade5 |
~~~~

**Contrôle avant d'inscrire** (une ligne fautive ne se corrige jamais : une seconde ligne de la même clé donne `ligne-double`,
le module, l. 930-931). Le contrôle à blanc versé avec cette procédure (`controle_prealables_p3bis_v1.py`, section 8) rejoue la
garde du module de S sur une **copie** des registres, n'écrit rien dans le dépôt, ne touche aucun paquet, et imprime les lignes
exactes à inscrire :

```bash
DEPOT=/home/user/controle-ia-travail; BAC=<bac de la mère, chemin absolu, hors de tout arbre git>
PY="$DEPOT/.venv/bin/python"; S=8f8df8b2726a69568b4d4a54bae16188e7f1b3d0
P="$DEPOT/docs/procedures/P3-bis-rendez-vous-et-verdict-v1-pieces"
M="$BAC/module-s-v1"; mkdir -p "$M/controle_ia/premier_test_ia"          # neuf (R12)
for f in __init__.py gardes.py scellement.py premier_test_ia/__init__.py premier_test_ia/ouverture_p3bis_v3.py; do
    git -C "$DEPOT" show "$S:src/controle_ia/$f" > "$M/controle_ia/$f"; done
sha256sum "$M/controle_ia/premier_test_ia/ouverture_p3bis_v3.py"         # 4a54a437e4a6031b… attendue, sinon ARRÊT
D=$(date -u +%Y-%m-%dT%H:%M:%SZ)
PYTHONPATH="$M" "$PY" -B "$P/controle_prealables_p3bis_v1.py" --racine "$DEPOT" --bac "$BAC/controle-ecrits-v1" \
    --mode reduite --ecrits "$D"
# attendu : trois « LIGNE À INSCRIRE (telle quelle) » et « CONTRÔLE À BLANC : REFUS ni-scores-ni-ouvrir » (aucune décision
# encore) ; tout autre code de refus (ligne-double, sceau-faux, ligne-mal-formee, cle-inconnue…) : ARRÊT, rien n'est inscrit
```

Puis, si le contrôle est conforme : la dernière ligne du registre finit par un saut de ligne (`[ -z "$(tail -c1
registres/prealables-p3bis-v1.md)" ]`), les trois lignes imprimées sont ajoutées **telles quelles** par `>>`, l'ajout est relu
(`tail -n 3`), puis commité et poussé seul, avec son entrée au registre des décisions.

## 3. (a) Ce que Lazar écrit, et quand

### 3.1 Le rendez-vous s'applique-t-il ?

Le texte, l. 1765-1767 : « (2) **rendez-vous du 2026-11-20T12:00:00Z** : il ne s'applique que si, à cette date, ces deux lignes
[`SCORES-T07` et `SONDES-T07`] ne sont pas inscrites et conformes ». Le 20, avant 12:00 UTC, la mère relit
`registres/scellements-v1.md` : lignes `SCORES-T07` et `SONDES-T07` présentes, une chacune, bien formées, datées, compagnon du
fichier cité présent et égal à l'empreinte de la ligne (le module, l. 1030-1042 et 1067-1074). Si oui : **le rendez-vous tombe**
(« rendez-vous sans objet », écrit au verdict : le texte, l. 1759-1760), aucune décision n'est demandée ; voie normale, section
4 avec le mode `pleine`. Si non : section 3.2 et suivantes.

### 3.2 Quand

- **Au plus tôt 2026-11-20T12:00:00Z** : la ligne `Date :` du fichier de décision doit être au moins `DATE_RENDEZ_VOUS` (le
  module, l. 1020-1022 ; sinon `ligne-mal-formee`). Un mot de Lazar reçu avant 12:00:00 UTC n'est pas une décision du rendez-vous :
  la mère le lui dit et attend un mot écrit à 12:00:00 UTC ou après.
- **Aucune borne haute** : le module ne borne la date que par le bas et par sa ligne (l. 1020-1024) ; Lazar peut écrire plus
  tard (le texte, l. 1721-1723 et 1731-1732) ; tant qu'il n'a rien écrit, rien n'est ouvert, et la levée par le calendrier seul
  est interdite (le texte, l. 2001-2002).
- **Sans voir les sorties fermées** : Lazar ne voit que la classe 1 (le texte, l. 1720-1721 et 1489-1506 : codes de sortie,
  `resume.json`, `sondes-figees.json`, manifeste du run, lignes `PROGRES`, empreintes et tailles des paquets, traces).

### 3.3 Ce que Lazar écrit

Un seul des trois mots, écrit en clair dans la session mère, par exemple : « Rendez-vous P3-bis : ouvrir ». Les trois sont, à
la lettre du module (l. 175-176) : `maintenir`, `ouvrir`, `ouvrir pleinement` (minuscules). Un mot ambigu (« go », « ok »,
« ouvre tout ») ne s'interprète pas : la mère redemande. « ouvrir » n'a de sens que si la garde adaptée est en vigueur (elle
l'est, section 1) ; sans elle, « ouvrir » n'ouvrirait rien et ne pourrait plus être suivi d'aucune décision (le texte,
l. 1721).

### 3.4 Le fichier de décision (écrit par la mère, mot de Lazar recopié)

Chemin imposé par le numéro (le module, l. 174 et 1003-1005) : `docs/decisions/rendez-vous-P3-bis-v1.md` pour la première
décision, `-v2.md` pour la deuxième, etc. Gabarit (éprouvé, section 8) :

~~~~text
# Rendez-vous de P3-bis — décision n° 1 de Lazar (v1)

- Mots de Lazar, verbatim, reçus dans la session mère `<identifiant>` ; heure de réception relevée par `date -u` : <H>.

> <mots de Lazar, chaque ligne précédée de « > »>

Décision : <maintenir|ouvrir|ouvrir pleinement>
Date : <H>

- Recopiée mot pour mot par la session mère ; scellée par son compagnon `.sha256` ; citée par la ligne
  `RENDEZ-VOUS-P3BIS-1` de `registres/prealables-p3bis-v1.md`. Lazar n'a vu que la classe 1 des sorties (plan, point 6).
~~~~

Règles de forme (le module, l. 176-177 et 1009-1015 ; chacune éprouvée en cas sain et en artefact, section 8) :
- **exactement une** ligne qui commence par `Décision :` et **exactement une** qui commence par `Date :`, sans rien devant
  (ni tiret, ni `>`, ni espace) ni après (aucune espace en fin de ligne) ; aucune autre ligne du fichier ne commence par ces
  mots (la citation de Lazar est précédée de `> ` à chaque ligne) ;
- espace **ordinaire** (U+0020) de part et d'autre du deux-points : une espace insécable, que la typographie française met
  souvent, fait refuser (`ligne-mal-formee`) ; « Décision » écrit avec un « é » composé (U+00E9) ;
- le mot en minuscules, exactement `maintenir`, `ouvrir` ou `ouvrir pleinement` (« Ouvrir » est refusé) ;
- `<H>` au format `AAAA-MM-JJTHH:MM:SSZ`, heure du mot de Lazar (sa réception, `date -u`), **au moins**
  `2026-11-20T12:00:00Z` et **au plus** la date de sa ligne de registre ;
- jamais réécrit après son scellement (règle R12 ; `scellement.sceller` refuse une autre empreinte) : le brouillon est d'abord
  écrit dans le bac et passé au contrôle à blanc (section 3.5), puis seulement copié à son chemin et scellé.

### 3.5 La ligne de registre (inscrite par la mère)

~~~~text
| RENDEZ-VOUS-P3BIS-1 | <L> | docs/decisions/rendez-vous-P3-bis-v1.md | <empreinte du fichier de décision> |
~~~~

Règles (le module, l. 169, 899-942 et 1000-1027 ; le texte, l. 1576-1582 et 1724-1732) : clé au motif `RENDEZ-VOUS-P3BIS-[1-9][0-9]*`
(`-01` ou `-0` : `cle-inconnue`) ; numéros consécutifs depuis 1 ; dates des lignes de rendez-vous strictement croissantes ;
`<L>` (`date -u` à l'inscription) **au moins** `<H>` ; **strictement avant** l'instant de l'ouverture (la garde prend son
horloge : attendre au moins une seconde après `<L>`) ; pour une ouverture réduite, `SCELLEMENT-T07` et
`GARDE-ADAPTEE-T07-P3BIS` strictement avant `<L>` (elles sont du 11 novembre) ; la décision qui fait foi est celle du fichier
cité par la **dernière** ligne de rendez-vous, jamais le fichier le plus récent par son nom (le texte, l. 1727-1728).

Suite exacte, sur le brouillon `"$BAC/decision-v1.md"` (variables de la section 2) :

```bash
L=$(date -u +%Y-%m-%dT%H:%M:%SZ)                       # au moins l'heure <H> du fichier
PYTHONPATH="$M" "$PY" -B "$P/controle_prealables_p3bis_v1.py" --racine "$DEPOT" --bac "$BAC/controle-decision-1-v1" \
    --mode <MODE> --decision "$BAC/decision-v1.md" --date-ligne "$L"
# <MODE> : reduite pour « ouvrir », pleine-anticipee pour « ouvrir pleinement », reduite pour « maintenir » (refus
# decision-maintenir attendu : il prouve que le fichier et la ligne sont lus) ; attendu : « CONTRÔLE À BLANC : AUTORISÉ … »
# (ou le refus attendu pour « maintenir ») et une « LIGNE À INSCRIRE » ; tout autre refus : ARRÊT, rien n'est copié ni inscrit
cd "$DEPOT"
test ! -e docs/decisions/rendez-vous-P3-bis-v1.md && cp "$BAC/decision-v1.md" docs/decisions/rendez-vous-P3-bis-v1.md
PYTHONPATH=src "$PY" -B -m controle_ia.scellement sceller docs/decisions/rendez-vous-P3-bis-v1.md   # même empreinte qu'au contrôle
[ -z "$(tail -c1 registres/prealables-p3bis-v1.md)" ] && printf '%s\n' '<LIGNE À INSCRIRE, recopiée telle quelle>' >> registres/prealables-p3bis-v1.md
tail -n 1 registres/prealables-p3bis-v1.md
git add docs/decisions/rendez-vous-P3-bis-v1.md docs/decisions/rendez-vous-P3-bis-v1.md.sha256 registres/prealables-p3bis-v1.md
git commit -m "P3-bis : décision de Lazar au rendez-vous (<mot>), RENDEZ-VOUS-P3BIS-1"
git push origin HEAD:refs/heads/main
```

### 3.6 Dates permises par le module

| objet | borne basse | borne haute | si hors bornes |
|---|---|---|---|
| `Date :` du fichier de décision | `2026-11-20T12:00:00Z` (l. 1020) | date de sa ligne (l. 1023) | `ligne-mal-formee` |
| date de la ligne `RENDEZ-VOUS-P3BIS-N` | `Date :` de son fichier ; strictement après la ligne de rendez-vous précédente (l. 938) | strictement avant l'ouverture (l. 1158) | `ligne-mal-formee`, `rendez-vous-non-croissant`, `date-posterieure` |
| `SCELLEMENT-T07`, `GARDE-ADAPTEE-T07-P3BIS` (ouverture réduite) | — | strictement avant la ligne « ouvrir » (l. 1090-1098) | `garde-adaptee-posterieure` |
| trois lignes d'écrit, ligne de garde | — | strictement avant l'ouverture (l. 1151-1155) | `date-posterieure` |
| « ouvrir pleinement » après « ouvrir » | ouverture `reduite` appuyée sur la ligne « ouvrir », au journal, datée strictement avant la ligne « ouvrir pleinement » (l. 1056-1063) | — | `ligne-apres-decision-finale` |
| horloge de l'ouverture | date de la dernière ligne du journal (égalité permise, l. 834-841) | — | refus sans ligne, code 2 |

### 3.7 Ce que chaque décision entraîne

| | « maintenir » | « ouvrir » | « ouvrir pleinement » |
|---|---|---|---|
| mode de la garde | aucun appel (un appel ne donnerait qu'un refus `decision-maintenir`, l. 1172-1173 et 1193-1194) | `reduite` (branche 1) ; `pleine-anticipee` refusée (l. 1205-1210) | `pleine-anticipee` (branche 2) ; refusée si `SCORES-T07` et `SONDES-T07` sont alors inscrites et conformes : `pleine` seule (l. 1186-1190) |
| ce qui s'ouvre | rien ; l'attente continue ; la voie normale reste ouverte, à toute date, sans décision (le texte, l. 1700-1714 et 1766-1767) | les deux paquets, **pour le seul lecteur du verdict** ; seules `issue` et `ligne` du fichier d'issue sont affichées, par `exposer-issue` ; le fichier d'issue entier est commité ; le verdict en prose et les paquets restent fermés (le texte, l. 1743-1751) | les deux paquets en entier ; verdict entier à sa date réelle (le texte, l. 1753-1758) |
| ligne `VERDICT-P3BIS` | non | oui, après le fichier d'issue ; admise avant `SCORES-T07` quand seule l'issue est ouverte (le texte, l. 1738-1739 et 1752) | oui, après le verdict |
| pour T0.7 | ordre de DS-2 inchangé : scores de T0.7 scellés, puis verdict, puis lecture (N-066, l. 19) | T0.7 garde son étape A et la lecture de la course 7b, **avec une réserve écrite** par T0.7 ; règle 4 restreinte au seul lancement où l'ouverture réduite a eu lieu (N-066, l. 15-18) ; aucune version de T0.7 scellée après `VERDICT-P3BIS` ne lit 7b ; T0.7 joue son étape A quelle que soit l'issue (le texte, l. 1739-1740 et 1752) | **« T0.7 ne lit plus la course 7b sous son texte : nœud de Lazar, déclaré dans le verdict et transmis à T0.7 »** (le texte, l. 1757-1758) ; toute ligne `pleine-anticipee`, à toute date, ferme 7b à T0.7 (l. 1693-1694) |
| suite permise | toute décision, plus tard (`RENDEZ-VOUS-P3BIS-2`…) | une seule : « ouvrir pleinement », après l'ouverture réduite journalisée (complément `pleine-anticipee`, mêmes paquets, ferme 7b) ; ou le complément `pleine` dès `SCORES-T07` et `SONDES-T07` conformes, avant l'étape B de T0.7 (le texte, l. 1749-1751 et 1695-1699) | aucune (`ligne-apres-decision-finale`, l. 1053-1055) |

Coût pratique de « ouvrir » à connaître avant de l'écrire : le verdict en prose doit rester **fermé et intact** jusqu'à
l'ouverture pleine, parce que son empreinte est commitée dans le fichier d'issue et que l'étape B de T0.7 la vérifie (le texte,
l. 1884-1889). Un bac de session ne survit pas à un changement de session : voir le point ouvert 2 (section 7).

Passages du texte qui font foi pour cette section (recopiés à l'octet) :

~~~~text
   - **rendez-vous écrit de Lazar** à date fixée d'avance : **2026-11-20T12:00:00Z**, date **proposée** par la mère avec
     recommandation (R-2021, l. 1979) ; **elle attend le mot de Lazar ou son défaut** : sans mot de Lazar sous 48 heures
     (échéance ≈ 2026-11-11 16:03 UTC, R-2021), elle tient ; un mot de Lazar avant le scellement qui la change fait une
     version neuve de ce texte, relue sur l'écart ; après le scellement, la changer est un écart à un texte scellé (nœud).
     **Aucune levée automatique** : la date oblige à décider, elle n'ouvre rien. À cette date, si le chemin normal n'est
     pas déjà ouvert, Lazar écrit l'une de deux décisions sans consulter les sorties fermées (il ne voit que la classe 1 du
     point 6) : « maintenir » (l'attente continue, le chemin normal reste ouvert) ou « ouvrir » (à n'écrire que si la garde adaptée est en vigueur : sans elle, « ouvrir » n'ouvre rien et ne peut plus être suivi d'aucune décision, toute ligne de rendez-vous inscrite ensuite faisant refuser jusqu'à la voie normale, `ligne-apres-decision-finale` ; résumé, (3)) ; au rendez-vous ou plus tard, une troisième
     est possible, « ouvrir pleinement » (brouillon 7 : forme écrite du mot de Lazar qui ferme T0.7 sur 7b ; brouillon 11 : sauf si
     `SCORES-T07` et `SONDES-T07` sont alors inscrites et conformes, où seule `pleine` est permise, D-2). Chaque décision
     est recopiée mot pour mot dans un **fichier versionné** `docs/decisions/rendez-vous-P3-bis-vN.md` (N = 1, 2… :
     `rendez-vous-P3-bis-v1.md`, puis `-v2.md`… ; R12), qui porte une ligne `Décision : maintenir`, `Décision : ouvrir` ou
     `Décision : ouvrir pleinement` et une ligne `Date : AAAA-MM-JJTHH:MM:SSZ` ; il est scellé, et cité par la ligne
     `RENDEZ-VOUS-P3BIS-N` du même numéro ; **la décision qui fait foi est celle du fichier versionné que cite la dernière
     ligne `RENDEZ-VOUS-P3BIS-N`**, jamais le fichier le plus récent par son nom, ni `-v1` par défaut. La première ligne est
     datée au plus tôt à l'heure du rendez-vous ; « maintenir » peut être suivi de toute décision ; « ouvrir » n'est suivi
     de rien, sauf, s'il a donné une ouverture réduite, d'une seule décision « ouvrir pleinement » ; « ouvrir pleinement »
     n'est suivi de rien (refus `ligne-apres-decision-finale`). Une décision « ouvrir » ou « ouvrir pleinement » après un
     « maintenir » suit les branches ci-dessous et porte sa date réelle. Sans décision écrite, rien n'est ouvert ;
     - **branche 1, ouverture réduite à l'issue** : si, à la date de la décision « ouvrir », T0.7 est scellé (ligne
       `SCELLEMENT-T07`) **avec la garde adaptée** (ligne `GARDE-ADAPTEE-T07-P3BIS` du registre des préalables, **inscrite
       avant la ligne de la décision « ouvrir »** (contre-lecture 3, D2), qui cite le texte scellé de T0.7 portant cette
       garde, au même chemin et à la même empreinte que la ligne `SCELLEMENT-T07`, ces deux lignes étant strictement
       antérieures à la ligne « ouvrir » et citant toutes deux `prereg/T0.7-sondes-v0-v1.md` (brouillon 11, D-4) ; ce texte
       accepte `VERDICT-P3BIS` avant `SCORES-T07` quand seule l'issue est
       ouverte, et aucune version de T0.7 scellée après `VERDICT-P3BIS` ne lit 7b ; règles 2 et 4 de [A-T3] ; réécriture
       qui touche DS-2, **accordée par Lazar, option 1 : N-066, R-2027** (réserve écrite par T0.7 ; règle 4 restreinte au
       seul lancement où l'ouverture réduite a eu lieu). **La ligne `GARDE-ADAPTEE-T07-P3BIS` est inscrite par la session
       mère au scellement de T0.7 avec cette garde, avant toute décision « ouvrir » au rendez-vous** (N-066, point 3) ; la
       branche 1 existe donc dès que cette ligne est inscrite) : les paquets
       sont ouverts **pour le seul lecteur du verdict**, qui écrit le verdict et le fichier d'issue ; **seules les valeurs
       `issue` et `ligne` sont affichées par la garde ; le fichier d'issue entier est commité, `verdict_sha256` compris**
       (contre-lecture 3, D4 ; contre-lecture de T0.7 b15, m-1) : `verdict` est un chemin constant, et `verdict_sha256`
       l'empreinte d'un verdict en prose, à réserves et à nombres, qui ne se devine pas par dictionnaire (l'attaque de la
       synthèse, § I.4, vise un fichier reconstructible) ; cette empreinte engage le verdict avant l'ouverture pleine, qui la
       vérifie ; le verdict en prose et les paquets restent fermés jusqu'aux lignes `SCORES-T07` et `SONDES-T07` (ouverture
       `pleine` alors, par la même garde, **avant** l'étape B de T0.7, dont le module vérifie l'empreinte du verdict en
       prose) ou jusqu'à une décision « ouvrir pleinement » de Lazar, qui ferme T0.7 sur 7b (ouverture `pleine-anticipee`) ;
       la ligne `VERDICT-P3BIS` est écrite ; T0.7 joue son étape A quelle que soit l'issue (écrit (iii)) ;
     - **branche 2, ouverture pleine anticipée** : sinon (T0.7 non scellé, scellé sans la garde adaptée, aucune ligne
       `GARDE-ADAPTEE-T07-P3BIS`, ou une ligne inscrite après la décision « ouvrir »), et toujours sous une décision « ouvrir
       pleinement », ouverture `pleine-anticipee` à la date réelle de la décision, verdict à sa date réelle (brouillon 11,
       D-2 : si `SCORES-T07` et `SONDES-T07` sont alors inscrites et conformes, `pleine-anticipee` est refusée et seule
       `pleine` ouvre, par le chemin normal, sans fermer 7b) ; **T0.7 ne lit
       plus la course 7b sous son texte : nœud de Lazar**, déclaré dans le verdict et transmis à T0.7 ;
   - **le rendez-vous tombe** si `SCORES-T07` et `SONDES-T07` sont inscrites avant sa date : chemin normal, « rendez-vous
     sans objet » écrit au verdict (brouillon 11 : inscrites **et conformes**, au sens du chemin normal) ;
   - **quand le verdict s'ouvre, en résumé** (brouillon 11 ; contre-lecture du socle de preuves, constat 2, R-2133 ; les
     règles ci-dessus font foi) : (1) **en entier, sans rendez-vous** : dès que l'étape A de T0.7 est jouée et que ses
     lignes `SCORES-T07` et `SONDES-T07` sont inscrites et conformes, avec le registre des préalables conforme et les deux
     paquets, par `pleine` (chemin normal), à toute date ; si c'est avant 2026-11-20T12:00:00Z, aucune décision n'est
     demandée à Lazar ; (2) **rendez-vous du 2026-11-20T12:00:00Z** : il ne s'applique que si, à cette date, ces deux
     lignes ne sont pas inscrites et conformes ; Lazar écrit alors « maintenir » ou « ouvrir », sans voir les sorties
     fermées ; « maintenir » laisse ouverte la voie (1) ; (3) **ouverture réduite de N-066** (branche 1) : seulement sous
     une dernière décision « ouvrir », si T0.7 est scellé avec la garde adaptée (lignes `SCELLEMENT-T07` et
     `GARDE-ADAPTEE-T07-P3BIS` au même texte, au chemin `prereg/T0.7-sondes-v0-v1.md`, toutes deux strictement avant la
     ligne de cette décision) ; elle n'affiche que `issue` et `ligne`, garde fermés le verdict en prose et les paquets,
     coûte à T0.7 une réserve écrite (N-066, point 1) et se complète par `pleine` dès la voie (1) ; sans la garde adaptée
     en vigueur, une décision « ouvrir » n'ouvre rien, et aucune décision ne peut plus la suivre : seule la voie (1)
     reste ; (4) **ouverture pleine anticipée** (branche 2) : seulement sous une dernière décision « ouvrir pleinement »
     (écrite au rendez-vous ou après un « maintenir », ou, après une ouverture réduite, comme seule décision qui suit
     « ouvrir »), quand `SCORES-T07` et `SONDES-T07` ne sont pas conformes (D-2) ; elle ferme 7b à T0.7 (nœud).
~~~~

## 4. (b) Les commandes de la mère, le jour de l'ouverture

Tout se fait dans un **espace fermé** neuf, hors de tout arbre git : ce que la garde extrait n'entre jamais dans le dépôt. Rien
n'est imprimé des paquets ; aucune empreinte d'un fichier contenu dans un paquet n'est calculée par la mère (le texte,
l. 1486-1488). La mère ne lit ni les paquets extraits ni le verdict en prose. Le journal n'est écrit **que** par la garde.

### 4.1 Variables

```bash
export LC_ALL=C.UTF-8
DEPOT=/home/user/controle-ia-travail                    # clone de main : registres, décisions (--racine)
BAC=<bac de la mère, chemin absolu, hors de tout arbre git>
ESPACE="$BAC/p3bis-espace-ferme-v1"                     # ne doit pas exister (R12)
CLONE="$ESPACE/clone-calcul-p3bis-reel-v2"              # paquets (--racine-paquets) et code de S
SORTIE="$ESPACE/paquets-ouverts"                        # --sortie : ne doit pas exister ; son parent existe
PIECES="$ESPACE/pieces"                                 # pièces remises au lecteur
VERDICT_FERME="$ESPACE/verdict-ferme"                   # seul dossier où le lecteur écrit
RUN=20261113-121129-p3bis-reel
S=8f8df8b2726a69568b4d4a54bae16188e7f1b3d0
DEPOT_URL=https://github.com/lciric/controle-ia-travail.git
PY="$DEPOT/.venv/bin/python"                            # python avec numpy (requirements-cpu.txt)
MODULE=controle_ia.premier_test_ia.ouverture_p3bis_v3
P="$DEPOT/docs/procedures/P3-bis-rendez-vous-et-verdict-v1-pieces"   # contrôle à blanc (section 8)
M="$BAC/module-s-v1"                                    # module de S tiré par git show (section 2)
"$PY" -c 'import numpy' || echo "ARRÊT : interpréteur sans numpy"
if [ ! -e "$M" ]; then mkdir -p "$M/controle_ia/premier_test_ia"
    for f in __init__.py gardes.py scellement.py premier_test_ia/__init__.py premier_test_ia/ouverture_p3bis_v3.py; do
        git -C "$DEPOT" show "$S:src/controle_ia/$f" > "$M/controle_ia/$f"; done; fi
sha256sum "$M/controle_ia/premier_test_ia/ouverture_p3bis_v3.py"     # 4a54a437e4a6031b… attendue, sinon ARRÊT
```

### 4.2 Contrôles d'entrée

```bash
date -u +%Y-%m-%dT%H:%M:%SZ
git -C "$DEPOT" fetch --no-tags -q origin +refs/heads/main:refs/remotes/origin/main
git -C "$DEPOT" merge --ff-only -q refs/remotes/origin/main
git -C "$DEPOT" status --porcelain -- registres/ docs/decisions/ docs/verdicts/      # vide attendu
cd "$DEPOT"
for k in GARDE-ADAPTEE-T07-P3BIS ECRIT-PERIMETRE-JEUX-P3BIS ECRIT-LANCEMENT-RELANCE-P3BIS ECRIT-ENGAGEMENT-ETAPE-A-P3BIS; do
    echo "$k : $(grep -c "^| $k |" registres/prealables-p3bis-v1.md)"; done              # 1 chacune, sinon ARRÊT
grep -E '^\| RENDEZ-VOUS-P3BIS-[0-9]+ \|' registres/prealables-p3bis-v1.md
grep -E '^\| (SCELLEMENT-T07|SCORES-T07|SONDES-T07|VERDICT-P3BIS) \|' registres/scellements-v1.md   # aucun VERDICT-P3BIS
if [ -e registres/ouvertures-p3bis-v1.md ]; then cat registres/ouvertures-p3bis-v1.md; else echo "journal absent : aucune tentative"; fi
PYTHONPATH=src "$PY" -B -m controle_ia.scellement verifier prereg/T0.7-sondes-v0-v1.md
ls docs/decisions/rendez-vous-P3-bis-v*.md 2>/dev/null && PYTHONPATH=src "$PY" -B -m controle_ia.scellement verifier docs/decisions/rendez-vous-P3-bis-v*.md
```

### 4.3 Choix du mode : la décision le fixe, jamais l'opérateur

| situation lue aux registres | mode | sinon |
|---|---|---|
| `SCORES-T07` et `SONDES-T07` inscrites et conformes, aucune ouverture `pleine` ou `pleine-anticipee` au journal | `pleine` (voie normale, ou complément d'une ouverture réduite) | — |
| dernière ligne de rendez-vous : « ouvrir » ; garde adaptée en vigueur ; aucune ouverture au journal | `reduite` | jamais `pleine-anticipee` sous « ouvrir » |
| dernière ligne de rendez-vous : « ouvrir pleinement » ; `SCORES-T07`/`SONDES-T07` non conformes | `pleine-anticipee` | conformes : `pleine` |
| dernière ligne de rendez-vous : « maintenir », ou aucune décision et pas de lignes de T0.7 | **aucun appel** | — |

Ne jamais essayer un autre mode « pour voir » : chaque tentative laisse une ligne définitive au journal, que T0.7 lit. Le mode
retenu passe d'abord le contrôle à blanc, qui ne lit aucun paquet et n'écrit rien au journal :

```bash
MODE=<pleine|reduite|pleine-anticipee>                  # celui de la table, rien d'autre
PYTHONPATH="$M" "$PY" -B "$P/controle_prealables_p3bis_v1.py" --racine "$DEPOT" --bac "$BAC/controle-jour-v1" \
    --mode "$MODE" --instant "$(date -u -d '+1 minute' +%Y-%m-%dT%H:%M:%SZ)"
# attendu : « CONTRÔLE À BLANC : AUTORISÉ <MODE> … » ; tout refus : ARRÊT, la garde n'est pas appelée
```

### 4.4 Récupération du paquet par refspec explicite

Une seule référence est récupérée (aucune autre branche, aucune étiquette), sans contenu de fichier (`blob:none`), puis
seuls les chemins utiles sont extraits (liste positive : aucun chemin interdit, aucun fichier de T0.7, n'arrive sur le disque ;
la récupération du 13 novembre procédait par liste d'exclusion, `recuperation_p3bis_v2.sh` l. 34-37). Suite éprouvée sur un
dépôt jetable (section 8) :

```bash
test ! -e "$ESPACE" || echo "ARRÊT : $ESPACE existe déjà (R12)"
mkdir -p "$ESPACE"
git init -q "$CLONE"
git -C "$CLONE" remote add origin "$DEPOT_URL"
git -C "$CLONE" config remote.origin.promisor true
git -C "$CLONE" config remote.origin.partialclonefilter blob:none
git -C "$CLONE" fetch --no-tags --filter=blob:none -q origin \
    +refs/heads/calcul/p3bis-reel-v2:refs/remotes/origin/calcul/p3bis-reel-v2
git -C "$CLONE" sparse-checkout set --no-cone /src/controle_ia/__init__.py /src/controle_ia/gardes.py \
    /src/controle_ia/scellement.py /src/controle_ia/premier_test_ia/__init__.py \
    '/src/controle_ia/premier_test_ia/ouverture_p3bis_v3.py*' '/src/controle_ia/premier_test_ia/lecture_p3bis_v1.py*' \
    '/src/controle_ia/premier_test_ia/lecture_p3bis_v2.py*' "/diag/p3bis-ferme-$RUN/" "/diag/$RUN/" "/runs/$RUN/" \
    '/traces/p3bis-*/'
# place avant l'extraction : T = taille du second paquet, lue dans son index (classe 1)
T=$(git -C "$CLONE" show "refs/remotes/origin/calcul/p3bis-reel-v2:diag/$RUN/paquet-run-ferme-v1.json" \
    | "$PY" -c 'import json, sys; print(json.load(sys.stdin)["taille"])')
echo "second paquet : $T octets ; disque libre : $(df -B1 --output=avail "$ESPACE" | tail -1) ; mémoire disponible : $(free -b | awk '/^Mem:/{print $7}')"
# exigés : disque libre ≥ 3 × T + 1 Go (morceaux dans .git et sur disque, fichiers extraits) ; mémoire ≥ 3 × T + 1 Go
# (la garde relit les morceaux, puis l'archive, puis les fichiers, en mémoire : le module, l. 503-535) ; sinon ARRÊT
git -C "$CLONE" checkout -q --detach refs/remotes/origin/calcul/p3bis-reel-v2
```

Vérifications, toutes exigées (sinon ARRÊT, rien n'est appelé) :

```bash
cd "$CLONE"
git rev-parse HEAD                                                     # commence par 2aaaaf87 (R-2547)
git merge-base --is-ancestor "$S" HEAD && echo "S ancêtre de la tête"
git diff --name-status --no-renames "$S" HEAD | grep -vc '^A'           # 0 : seulement des ajouts depuis S
sha256sum src/controle_ia/premier_test_ia/ouverture_p3bis_v3.py; cat src/controle_ia/premier_test_ia/ouverture_p3bis_v3.py.sha256
#   4a54a437e4a6031b1890f0f5f0261cf1141e72aee82d456d9fcd5483946693e9 deux fois
stat -c %s "diag/p3bis-ferme-$RUN/paquet-ferme-v1.tar"                  # 16783360
sha256sum "diag/p3bis-ferme-$RUN/paquet-ferme-v1.tar"; cat "diag/p3bis-ferme-$RUN/paquet-ferme-v1.tar.sha256"
#   égales et commençant par 0fb83f67 (seule empreinte exposée du paquet des lectures, classe 1)
find . -path ./.git -prune -o -type f -print | sed 's#^\./##' \
    | grep -v -E "^(src/controle_ia/|diag/p3bis-ferme-$RUN/|diag/$RUN/|runs/$RUN/|traces/p3bis-)"   # rien
test -e "diag/$RUN/resume.json" && ! test -e "diag/$RUN/arret.json" && echo "run complet : résumé, sans arrêt"
```

### 4.5 Appel de la garde

Le jour du rendez-vous : **strictement après** la date de la dernière ligne `RENDEZ-VOUS-P3BIS-N` (au moins une seconde) ; la
voie normale : à toute date. `--date-paquet` n'est pas donné : la garde lit la date de la mise en paquet au commit du paquet
(le module, l. 1224-1234).

```bash
cd "$CLONE" && date -u +%Y-%m-%dT%H:%M:%SZ          # MODE : fixé en 4.3, contrôle à blanc conforme
PYTHONPATH="$CLONE/src" PYTHONDONTWRITEBYTECODE=1 "$PY" -B -m "$MODULE" ouvrir --mode "$MODE" --run "$RUN" \
    --racine "$DEPOT" --racine-paquets "$CLONE" --sortie "$SORTIE" \
    > "$ESPACE/sortie-de-la-garde-v1.txt" 2> "$ESPACE/erreurs-de-la-garde-v1.txt"; CODE=$?
echo "code $CODE"; cat "$ESPACE/sortie-de-la-garde-v1.txt" "$ESPACE/erreurs-de-la-garde-v1.txt"
tail -n 1 "$DEPOT/registres/ouvertures-p3bis-v1.md"
```

Ce que la garde imprime (le module, l. 1314-1320 et 1402-1418) : en mode réduit, « ouverture réduite : paquets extraits dans
…, remis au seul lecteur du verdict ; seules `issue` et `ligne` du fichier d'issue seront affichées (exposer-issue) » ;
sinon « ouverture <mode> (<chemin>) : paquets extraits dans … » ; puis une ligne « réserve : … » par ligne d'écrit datée après
la mise en paquet. Rien d'autre. Codes :

| code | sens | suite |
|---|---|---|
| 0 | ligne `OUVERTURE-P3BIS` écrite au journal, paquets extraits dans `$SORTIE` | 4.6, puis la remise (section 6) |
| 2 | refus : ligne `REFUS-OUVERTURE-P3BIS` écrite, avec son code (liste fermée, le module, l. 191-194) ; ou refus **sans ligne** (horloge en arrière de la dernière ligne du journal ; journal impossible à écrire, l. 216-222), motif sur la sortie d'erreur | 4.6 (commit du refus s'il a une ligne), ARRÊT, une ligne à Lazar ; aucun verdict |
| 1 | « ARRÊT : » erreur d'appel avant toute lecture (mode inconnu, `$SORTIE` déjà présent, parent absent), sans ligne ; **ou** extraction en échec **après** la ligne `OUVERTURE-P3BIS` (la ligne reste, sens prudent pour T0.7 ; rien n'est laissé dans `$SORTIE`) | ARRÊT ; second cas : écart consigné, nœud de Lazar |

### 4.6 Journal : relu, commité et poussé seul

```bash
cd "$DEPOT"
git status --porcelain -- registres/                    # seul registres/ouvertures-p3bis-v1.md (créé ou augmenté d'une ligne)
git add registres/ouvertures-p3bis-v1.md
git commit -m "P3-bis : <ouverture <mode>|refus <code>> journalisé par la garde (paquets <préfixes>)"
git push origin HEAD:refs/heads/main                    # refus d'avance rapide : git pull --rebase, puis à nouveau
```

La ligne attendue d'une ouverture réduite (forme éprouvée, section 8) : `| OUVERTURE-P3BIS | <instant> | reduite |
RENDEZ-VOUS-P3BIS-1=<empreinte du fichier de décision> GARDE-ADAPTEE-T07-P3BIS=d7d180ec… | 0fb83f67… <empreinte du
second paquet> | - |`. La mère consigne au registre des décisions : mode, ligne du journal, réserves imprimées.

### 4.7 Ce qui arrête tout

- tout « ARRÊT » des commandes ci-dessus : empreinte autre que celle attendue, tête autre que `2aaaaf87…`, paquet d'une autre
  taille ou d'un autre préfixe, chemin hors de la liste positive extrait, place ou mémoire insuffisante, `$ESPACE` ou `$SORTIE`
  déjà présents, ligne d'écrit absente, contrôle à blanc qui refuse ;
- un mot de Lazar reçu avant 2026-11-20T12:00:00Z, ou ambigu : aucune ligne, on redemande ;
- dernière décision « maintenir » : aucun appel ;
- un refus de la garde (code 2) : aucun nouvel appel avant d'en avoir établi la cause ; jamais un autre mode « pour voir » ;
  un refus dû à une ligne de registre ou à un fichier de décision fautifs est définitif (une ligne ne se corrige pas) : nœud ;
- journal hors format (`ligne-mal-formee` à chaque tentative, voie normale comprise) : nœud, aucune réparation à la main (le
  texte, l. 1994-1998) ;
- toute ouverture hors de la garde (un paquet lu ou extrait autrement, un fichier de la classe 2 ouvert, un fichier de lecture
  commité en clair) : consignée comme écart, réserve « résultat de P3-bis exposé avant les scores de T0.7 » au verdict et à
  T0.7 (le texte, l. 1981-1983) ;
- verdict commandé, fichier d'issue écrit ou ligne `VERDICT-P3BIS` inscrite sans ligne `OUVERTURE-P3BIS` au journal : interdit
  (le texte, l. 2003-2004).

### 4.8 Après le verdict

Sous **ouverture réduite** (le texte, l. 1566-1568 et 1884-1886 : seul le fichier d'issue est commité) :

```bash
test -f "$VERDICT_FERME/verdict-P3-bis-v1-issue.json" && test -f "$VERDICT_FERME/verdict-P3-bis-v1.md"
cd "$DEPOT" && test ! -e docs/verdicts/verdict-P3-bis-v1-issue.json
cp "$VERDICT_FERME/verdict-P3-bis-v1-issue.json" docs/verdicts/verdict-P3-bis-v1-issue.json
cmp "$VERDICT_FERME/verdict-P3-bis-v1-issue.json" docs/verdicts/verdict-P3-bis-v1-issue.json
PYTHONPATH=src "$PY" -B -m controle_ia.scellement sceller docs/verdicts/verdict-P3-bis-v1-issue.json
PYTHONPATH=src "$PY" -B -m controle_ia.scellement sceller "$VERDICT_FERME/verdict-P3-bis-v1.md"   # compagnon, rien n'est lu
"$PY" -B -c 'import hashlib, json, sys; d = json.load(open(sys.argv[1], encoding="utf-8")); h = hashlib.sha256(open(sys.argv[2], "rb").read()).hexdigest(); print("empreinte du verdict en prose : " + ("égale" if d["verdict_sha256"] == h else "AUTRE : ARRÊT"))' \
    docs/verdicts/verdict-P3-bis-v1-issue.json "$VERDICT_FERME/verdict-P3-bis-v1.md"
LP=$(ls -d "$SORTIE"/diag/*-p3bis-lecture-complementaire/lecture-p3bis.json)   # exactement un chemin
cd "$CLONE" && PYTHONPATH="$CLONE/src" "$PY" -B -m "$MODULE" exposer-issue "$DEPOT/docs/verdicts/verdict-P3-bis-v1-issue.json" \
    --lecture-p3bis "$LP"
# imprime {"issue": …, "ligne": …} seulement (le module, l. 1325-1353) ; tout « ARRÊT » (désaccord avec l'issue mécanique,
# sceau faux, forme hors table) : rien n'est commité, nœud de Lazar (le texte, l. 1881-1883 et 2008)
cd "$DEPOT"
[ "$(grep -c '^| VERDICT-P3BIS |' registres/scellements-v1.md)" = 0 ] && [ -z "$(tail -c1 registres/scellements-v1.md)" ] \
  && printf '| VERDICT-P3BIS | %s | docs/verdicts/verdict-P3-bis-v1-issue.json | %s |\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
     "$(cut -d' ' -f1 docs/verdicts/verdict-P3-bis-v1-issue.json.sha256)" >> registres/scellements-v1.md
git add docs/verdicts/verdict-P3-bis-v1-issue.json docs/verdicts/verdict-P3-bis-v1-issue.json.sha256 registres/scellements-v1.md
git commit -m "P3-bis : fichier d'issue (ouverture réduite) et ligne VERDICT-P3BIS" && git push origin HEAD:refs/heads/main
```

À Lazar : l'issue et la ligne affichées, rien d'autre (aucun nombre, aucune réserve : ils restent dans le verdict fermé). Le
verdict en prose, ses fichiers de travail et `$SORTIE` restent dans l'espace fermé, ni lus ni copiés ailleurs (voir le point
ouvert 2).

Sous **ouverture pleine ou pleine anticipée** : même suite, plus la copie à l'octet, sous `docs/verdicts/`, du verdict en prose
`verdict-P3-bis-v1.md` et des fichiers de travail du lecteur (noms versionnés qu'il donne), chacun scellé ; tout est commité
avec le fichier d'issue ; ligne `VERDICT-P3BIS` ensuite (voie normale : datée strictement après `SCORES-T07` et `SONDES-T07`,
le texte, l. 1712-1714) ; verdict soumis à Lazar (verdict d'abord). Sous `pleine-anticipee`, la mère transmet à T0.7 le nœud
« T0.7 ne lit plus la course 7b sous son texte ».

### 4.9 Plus tard, après une ouverture réduite

- **Complément `pleine`** dès que `SCORES-T07` et `SONDES-T07` sont inscrites et conformes, **avant l'étape B** de T0.7 :
  mêmes sections 4.2 à 4.6 avec un `--sortie` neuf ; la garde exige les mêmes paquets (sinon `paquet-faux`, le module,
  l. 1297-1300) ; le verdict en prose fermé est alors copié à l'octet sous `docs/verdicts/verdict-P3-bis-v1.md`, scellé, son
  empreinte égale à `verdict_sha256`, commité avec ses fichiers de travail.
- **« ouvrir pleinement »** de Lazar : `RENDEZ-VOUS-P3BIS-2` (section 3, numéro 2), datée strictement après la ligne
  `reduite` du journal ; complément `pleine-anticipee` (refusé si `SCORES-T07` et `SONDES-T07` sont alors conformes : `pleine`) ;
  il ferme 7b à T0.7.

## 5. (c) Qui peut être le lecteur du verdict

- **Un agent neuf** (règle R13 ; le texte, l. 1561-1562), créé pour ce seul verdict, sans contexte antérieur, sous-agent de la
  session mère (il lit l'espace fermé, sur le même disque, par chemins absolus), à qui rien d'autre n'est confié.
- **D'un autre modèle que les auteurs du texte et de l'analyse quand c'est possible** : le texte (candidats 1 à 3) et le code
  de la lecture complémentaire v2 ont été écrits par Claude Opus 5.5 (le texte, l. 3-7 ; rapport du développeur
  `docs/notes/g0-deux-semaines-v1/p3bis-regle-plancher-v1/rapport-code-p3bis-regle-a-v1.md`, `0f57e202…`, l. 3-4) : choisir
  **Claude Fable** (5.2, ou 5.1) ; à défaut, Opus 5.5, et le dire au verdict.
- **Exclus** : la session-dépôt (passation `2026-11-13-1732.md`, l. 46) ; **tout lecteur de T0.7** (tout agent qui a lu le texte,
  un brouillon, une contre-lecture, le code ou une sortie de T0.7, ou `lecture-sondes-t06.json`) ; **tout auteur ou
  contre-lecteur de P3-bis** (texte et brouillons, addendums 1 à 3, code, chaîne, contre-lectures, vérifications courtes, la
  fille qui a mené la course et la récupération, `session_01XJ6MgndxPY844vwbKNNGHu`, et ses sous-agents) ; **le rédacteur de
  cette procédure** ; la session mère elle-même.
- Le lecteur déclare au verdict n'être d'aucune de ces catégories, et n'avoir lu aucun fichier de T0.7 ni
  `lecture-sondes-t06.json` (le texte, l. 1563-1565). Un de ces fichiers donné au lecteur : ce verdict n'est pas inscrit, un
  autre lecteur neuf le refait sans eux (le texte, l. 2005-2007).

## 6. (d) La remise au lecteur

### 6.1 Pièces, copiées dans l'espace fermé (le lecteur ne lit ni `$DEPOT` ni `$CLONE`)

```bash
mkdir -p "$PIECES" "$VERDICT_FERME"
cd "$DEPOT"
for f in prereg/P3-bis-temoin-positif-v1.md prereg/P3-bis-temoin-positif-config-v1.json prereg/P3-bis-consignes-v1.md \
         prereg/P3-bis-addendum-1-garde-credit-v1.md prereg/P3-bis-addendum-2-telechargement-controle-v1.md \
         prereg/P3-bis-addendum-3-relance-credit-v1.md docs/procedures/P3-bis-consigne-lecteur-verdict-v1.md \
         docs/decisions/decision-N-066-v1.md diag/20261019-230011-p3-reel/sondes-figees.json \
         diag/20261019-230011-p3-reel/episodes-p3.json; do
    cp --parents "$f" "$f.sha256" "$PIECES/"; done
for f in docs/decisions/rendez-vous-P3-bis-v*.md; do [ -e "$f" ] && cp --parents "$f" "$f.sha256" "$PIECES/"; done
cp --parents registres/ouvertures-p3bis-v1.md "$PIECES/"
cp "$ESPACE/sortie-de-la-garde-v1.txt" "$PIECES/"
C=$(git rev-parse HEAD)
{ echo "# Extrait des registres pour le lecteur du verdict de P3-bis (v1)"; echo
  echo "Commit de main : $C. Lignes recopiées telles quelles, précédées de leur numéro."
  for f in registres/decisions.md registres/depenses.md registres/arrets.md; do
      echo "- $f : $(git show "$C:$f" | sha256sum | cut -d' ' -f1)"; done
  echo; echo "## registres/decisions.md"; echo
  for r in R-2386 R-2399 R-2407 R-2450 R-2457 R-2492 R-2493 R-2495 R-2496 R-2497 R-2498 R-2499 R-2512 R-2516 R-2517 \
           R-2518 R-2519 R-2520 R-2521 R-2546 R-2547; do git show "$C:registres/decisions.md" | grep -n "^| $r |"; done
  echo; echo "## registres/depenses.md"; echo
  git show "$C:registres/depenses.md" | grep -n -E '60286945|60370121|60432755|60492378'
  echo; echo "## registres/arrets.md"; echo
  git show "$C:registres/arrets.md" | grep -n -E '60286945|60370121|60432755|60492378'
} > "$PIECES/extrait-registres-p3bis-v1.md"
cd "$CLONE"
cp --parents "runs/$RUN/manifeste.json" "runs/$RUN/manifeste.json.sha256" "diag/$RUN/resume.json" "diag/$RUN/resume.json.sha256" \
    "diag/$RUN/sondes-figees.json" "diag/$RUN/sondes-figees.json.sha256" "diag/$RUN/paquet-run-ferme-v1.json" \
    "diag/$RUN/paquet-run-ferme-v1.json.sha256" src/controle_ia/premier_test_ia/lecture_p3bis_v1.py \
    src/controle_ia/premier_test_ia/lecture_p3bis_v1.py.sha256 src/controle_ia/premier_test_ia/lecture_p3bis_v2.py \
    src/controle_ia/premier_test_ia/lecture_p3bis_v2.py.sha256 "$PIECES/"
cp -r --parents traces/p3bis-* "$PIECES/"
(cd "$PIECES" && find . -type f -print0 | sort -z | xargs -0 sha256sum) > "$ESPACE/bordereau-remise-v1.txt"
cd "$DEPOT" && PYTHONPATH=src "$PY" -B -m controle_ia.scellement sceller "$ESPACE/bordereau-remise-v1.txt"
```

Le bordereau ne porte **aucune** empreinte d'un fichier extrait des paquets (`$SORTIE` n'y est que par son chemin).

### 6.2 Message de remise (à envoyer tel quel, chevrons remplis)

~~~~text
Tu es le lecteur neuf du verdict de P3-bis (règle R13). Lis d'abord ta consigne, et elle seule fixe ce que tu lis et écris :
<ESPACE>/pieces/docs/procedures/P3-bis-consigne-lecteur-verdict-v1.md (empreinte <empreinte de la consigne>, égale à son
compagnon : vérifie-la avant lecture).
- Mode de l'ouverture : <reduite | pleine-anticipee | pleine>. Ligne du journal : <ligne OUVERTURE-P3BIS recopiée>.
- Espace fermé : <ESPACE>. Pièces : <ESPACE>/pieces (bordereau <ESPACE>/bordereau-remise-v1.txt, empreinte <…>, scellé).
  Paquets ouverts : <ESPACE>/paquets-ouverts. Tu n'écris que dans <ESPACE>/verdict-ferme.
- Run : 20261113-121129-p3bis-reel. Interpréteur : <PY>.
- Réserves imprimées par la garde : dans <ESPACE>/pieces/sortie-de-la-garde-v1.txt.
Tu ne lis rien d'autre (ni le dépôt, ni le clone de calcul, ni aucun fichier de T0.7, ni lecture-sondes-t06.json). Ton rapport
final suit la section « Ce que tu rends » de ta consigne, mot pour mot ; sous ouverture réduite, il ne contient ni issue, ni
nombre, ni réserve.
~~~~

### 6.3 Ce que le lecteur rend, et ce que la mère fait ensuite

Le lecteur écrit dans `$VERDICT_FERME` le verdict en prose `verdict-P3-bis-v1.md`, le fichier d'issue
`verdict-P3-bis-v1-issue.json` et ses fichiers de travail (script de PB-9 et sa sortie, noms versionnés) ; son rapport suit
le format fermé de sa consigne (section 11). Sur « fichier d'issue écrit » : section 4.8. Sur un arrêt : rien n'est copié ni
commité, une ligne à Lazar (le code de l'arrêt seulement), nœud.

## 7. Points ouverts (pour Lazar et la mère)

1. **Trois lignes d'écrit manquantes** (section 2) : sans elles, aucune ouverture n'est possible, ni le 20 ni par la voie
   normale. Acte de la mère, à faire avant le lancement de l'étape A de T0.7 si possible, avec la réserve gelée qu'elles
   emportent. Le rédacteur n'a pas lu le texte de T0.7 : que la section « Écrits exigés par P3-bis » y figure n'est pas vérifié
   ici (la forme « le texte scellé » est permise telle quelle par le texte, l. 1586) ; la mère peut le vérifier.
2. **Conservation du verdict fermé sous ouverture réduite** : le texte veut le verdict en prose « dans l'espace fermé
   jusqu'à l'ouverture pleine » (l. 1566-1568) et son empreinte est vérifiée par l'étape B de T0.7 (l. 1884-1889) ; un bac de
   session est perdu à chaque changement de session ou de conteneur (R-2550, R-2552). Options : (a) le garder dans le bac et
   accepter le risque (perte = nœud : un verdict refait aurait une autre empreinte) ; (b) le mettre, avec les fichiers de
   travail, dans un « paquet du verdict » fait avec les fonctions mêmes du module (`paquet_lectures`, sel tiré par `secrets`,
   taille fixe de 16 783 360 octets, relecture par `relire_paquet_lectures`), commité sur une branche dédiée, ouvert seulement
   au complément `pleine` ou `pleine-anticipee` : même discipline de fermeture que le paquet des lectures (l. 1466-1488), mais un
   objet que le texte ne nomme pas, donc un petit code neuf, éprouvé (R5) et contre-lu ; (c) le chiffrer pour une clé que seul
   Lazar détient. **Recommandation : (b), confiance 0,6** ; à trancher **avant** d'écrire « ouvrir » ; défaut proposé : (a).
3. **Place disque** : 2,8 Go libres dans le conteneur de la mère au 13 novembre ; l'ouverture demande environ trois fois la
   taille du second paquet (section 4.4), qui n'est pas connue ici (≈ 0,9 Go si les 40 fichiers ajoutés en comptent une
   dizaine de morceaux : estimation, non mesurée). À relever et libérer avant le 20.
4. **Interpréteur** : la récupération employait un environnement aux dépendances épinglées de S
   (`/home/user/venv-p3bis-py311-v1`, `recuperation_p3bis_v2.sh` l. 42), absent d'un conteneur neuf ; la garde n'emploie que la
   bibliothèque standard et numpy (le module, l. 120-142) ; la répétition à blanc a tourné sous Python 3.13.18 et numpy 2.4.6.
5. **Facture de 60492378** non relevée (R-2552, registre l. 2511 ; `registres/depenses.md` l. 440 : « facture du loueur à
   relever ») : le verdict rapporte la dépense telle qu'inscrite le jour où il est écrit.
6. **Si l'étape A de T0.7 aboutit avant le 20** : voie normale (`pleine`), « rendez-vous sans objet » ; aucune décision de
   Lazar ; les trois lignes d'écrit restent exigées.

## 8. Répétition à blanc, versée avec cette procédure

Dossier `docs/procedures/P3-bis-rendez-vous-et-verdict-v1-pieces/` (chaque fichier scellé par son compagnon) :

| fichier | empreinte | rôle |
|---|---|---|
| `repetition_rendez_vous_v1.sh` | `185fe3dd39e309e91e0a7ac223b0ffd3d70c1381b5cd3490e33c625e82fff665` | pilote : tire le module de S par `git show` (empreinte vérifiée), joue l'essai Python, puis la récupération par refspec explicite, `blob:none` et liste positive sur un dépôt jetable local qui porte des chemins interdits factices |
| `essai_rendez_vous_v1.py` | `faffca89e000fb72a42004c73a8b3675294ca82b11bf89dfd481d0520be86fdd` | 25 cas sur jouet : garde (autorisations et refus attendus), gabarit de décision (espace insécable, majuscule, heure avant 12:00:00Z, heure après la ligne, midi pile), ouverture réduite de bout en bout sur paquets factices, journal, trois réserves « écrit après la lecture fermée », `exposer-issue`, deuxième tentative refusée, « ouvrir pleinement » après « ouvrir », appel en ligne de commande, contrôle à blanc |
| `controle_prealables_p3bis_v1.py` | `c7e7cb93fcfa7c5d1d1c7e73f2b045e36a4ee6688c13f6d307a0a6ec8b698794` | contrôle à blanc sur copie des registres (sections 2, 3.5 et 4.3) : imprime les lignes exactes à inscrire, rejoue la garde de S, n'écrit rien dans le dépôt, ne lit aucun paquet |
| `repetition-rendez-vous-sortie-v1.txt` | `2795e214d0db0c378c01a15b7d541b99b1f2b6a9955fcd6b5424c281f0c2b174` | sortie du pilote, 2026-11-13T18:36Z : « BILAN : 25 conformes sur 25 » (l. 51), « BILAN GIT : 6 conformes sur 6 » (l. 60), « RÉPÉTITION : TOUT CONFORME » (l. 62) |
| `controle-a-blanc-registres-reels-v1.txt` | `0d0aa09232a3f2912a2942819bffe7febd67ae9d63f201daf22109698b6b812d` | contrôle à blanc sur COPIE des registres réels de `main` (commit `d8f92d87`, registres inchangés avant et après) : aujourd'hui, décision « ouvrir » supposée → `ligne-absente` ×3 (cas 1) ; avec les trois lignes d'écrit supposées → « ouvrir » : réduite autorisée, appui `GARDE-ADAPTEE-T07-P3BIS=d7d180ec…` (cas 2) ; `pleine-anticipee` sous « ouvrir » refusée (cas 3) ; « maintenir » → `decision-maintenir` (cas 4) ; « ouvrir pleinement » → pleine anticipée autorisée (cas 5), réduite refusée (cas 6) |

Rejouer (aucun réseau, aucune écriture dans le dépôt ; le bac doit être neuf et hors du dépôt) :

```bash
bash docs/procedures/P3-bis-rendez-vous-et-verdict-v1-pieces/repetition_rendez_vous_v1.sh /home/user/controle-ia-travail <bac neuf> [<python avec numpy>]
```

Limites : jouet seulement (registres, texte de T0.7, décisions et paquets factices ; dépôt distant local) ; la garde
réelle, le vrai dépôt distant et les vrais paquets ne sont éprouvés que le jour même, par les vérifications de la
section 4.

## 9. Ce que cette procédure ne fait pas

Elle n'ouvre rien, n'inscrit rien, ne décide d'aucune option du texte et ne change aucune date. Elle ne remplace ni le texte
scellé ni le module : en cas de doute, ils font foi.
