# Procédure de réception et de lecture du run R1 relancé sur la table v3 (addendum v3 de R1) — v2

Version 2 de `../reception-r1-relance-v1/procedure-reception-lecture-r1-relance-v1.md` (`d85bd5e4…`, non modifiée, R12),
pour l'addendum v3 de R1 **scellé** : `prereg/R1-addendum-relance-v3.md`,
`88e262e26ea38a30e8acdf0cdf204cbdaba381baf3dbc352b4333d1fe6b299a4`, commit de scellement
`139a81d37fbd2255aff8d27698f84b47b9433221` (branche `prep/r1-relance-v3`) ; configuration
`prereg/R1-rejeu-config-v5.json` (`acad6253…`, empreinte canonique `1cfb7fba…`) et table
`prereg/R1-table-tokenisation-v3.json` (`ead8a668…`) au même commit. Changements demandés par notre concordance sur le
brouillon 2 de cet addendum (`../analyse-principale-r1-r2-v1/concordance-addendum-r1-v3-brouillon2-v1.md`,
`8482b4cd…`, section 8, « De notre côté », R-1 à R-5).

Pour la session conv-audit. Deux temps :
- **étape 0, dès maintenant**, avant toute récupération des sorties de la course par session-depot : la fiche de
  réception (notre document de contrôles) est contre-éprouvée, scellée, commitée, poussée et annoncée au canal (C-1) ;
- puis, au message de versement de session-depot, les étapes A0 à I, dans cet ordre et sans lecture entre deux :
  constat, récupération, fiches JSON écrites par le script, scellées et commitées, lancement décisif de l'analyse
  principale, lecture par épisode, analyse secondaire, verdicts R13.

Écrite sans aucune donnée (rapport joint : `rapport-preparation-reception-v2.md`). Script `ecrire_fiches_reception_v2.py`
(deux modes : « avant la récupération », « après le versement ») ; ses essais (`tests/test_ecrire_fiches_reception_v2.py`,
61) et son banc de mutations (`tests/banc_mutations_v2.py`, 46 mutants tués) sont dans ce dossier.

**Ce qui change par rapport à la v1** (une ligne chacun ; détail au rapport, section 1) :
1. Étape 0 neuve : la fiche de réception, écrite par le script en mode « avant la récupération », est scellée et annoncée
   au canal **avant la récupération** (C-1, R-5) ; P1 l'exige ; elle gouverne ensuite le script en mode « après ».
2. P1 et P2 pointent vers l'addendum v3 scellé, la configuration v5, la table v3 et la concordance sur la version
   scellée ; l'empreinte de l'addendum n'est plus un paramètre à remplir (constante vérifiée en 0.1 et A1).
3. `NON_INVERSIBLES` disparaît : liste vide fixée (E2, E19) ; le lecteur R13 de la principale reçoit « N-A sans objet »
   et la réserve sur HG-2 (R-1).
4. D1 : le script v2 relit la fiche scellée et **refuse** tout écart du manifeste (commande, `decisif`, texte qui
   gouverne lu dans la clé réelle `preenregistrement` — `src/controle_ia/manifeste.py` l. 104 —, configuration, commit,
   entropie), du résultat (`tokenisation.table_sha256` **comparée** ; `tokenisation.addendum` =
   `prereg/R1-addendum-relance-v2.md` à l'identique, réserve E16 ; comptes fixés par la table) et des empreintes des
   scores des juges citées par l'addendum v3 (R-2, R-3) ; clé `addendum_v3` dans `redaction`.
5. Reprise E21 : variables `BRANCHE_SOURCE`, `ARRETEE_E21`, `ARRET_E21_SHA`, `ANNONCE_E21` ; la course arrêtée est
   notée en C et dans les fiches, jamais ouverte (R-4).
6. Étape A0 neuve : le dépôt de cette instance est un clone superficiel ; deux commits cités par la v1 y manquent.
7. Aucune valeur observée de P-R5 n'est lue avant les analyses (règle écrite ; le script ne garde que les clés nommées).
8. Les lignes d'attribution des commits ne sont plus écrites en dur : variable `SIGNATURE`, celles de la session qui
   exécute.

**Règle générale** (inchangée ; procédure de scellement de la principale, `procedure-scellement-analyse-principale-r1-r2-v1.md`,
section F) : chaque bloc dit ce qu'il doit afficher pour continuer ; tout autre affichage, ou un code de sortie non nul,
**arrête la procédure** : rien n'est lancé, rien n'est corrigé à la main dans un arbre séparé, Lazar est prévenu. Une
fiche déjà scellée et commitée ne se réécrit pas : version nouvelle, nom nouveau (R12). Un `ARRÊT [garde] : …` du script
sur un écart à la fiche de réception (texte, commande, configuration, commit, entropie, table, provenance, comptes,
juges) signale une autre course ou un écart au texte scellé : **nœud de Lazar**.

Règles qui valent du début à la fin :
- aucun fichier `.npz` n'est ouvert par la session ; les résultats JSON du fournisseur ne sont ouverts que par le script
  (clés nommées ; ce qui est ouvert est écrit dans `redaction.ce_qui_a_ete_ouvert`, les noms des clés lues dans
  `redaction.cles_lues`, jamais leurs valeurs : les fiches JSON ne portent aucun nombre, analyse secondaire l. 24) ;
- **aucune valeur observée de P-R5 ni lecture de l'instrument n'est lue avant les analyses** (fiche de réception,
  section 6) : ni les traces de l'instance (`traces/…/r1-rejeu.json` recopie la sortie standard du module), ni la ligne
  de journal `etape=fin fideles=… notees=…`, ni `fidelite_toutes.fideles`, `notees`, `tokenisation.part_fideles_parmi_notees`,
  `p_r5_au_moins_90_pour_cent`, `fidelite_echantillon`, `controle_negatif` ; si un message en porte une, la session la
  déclare au registre (« vue avant les analyses ») et aux lecteurs R13 ;
- aucun `git merge` d'une branche `calcul/…` ; `donnees/<run>/` passe hors index (`git show > fichier`) ;
- aucune écriture sous `donnees/20261019-230011-p3-reel/` ;
- `nice -n 10` pour tout calcul ; une seule session shell (les variables ci-dessous vivent du début à la fin).

## Variables

```bash
DEPOT=/home/claude/controle-ia-travail
ARBRE_P=/home/claude/controle-ia-analyse-principale-r1-r2-v1   # arbre de la principale, recréé (n'existe pas)
ARBRE_S=/home/claude/controle-ia-analyse-bn-v3                 # arbre de la secondaire, recréé (n'existe pas)
BR_P=analyse-principale-r1-r2-v1 ; BR_S=analyse-blanche-noire-v3
CITE_P=a8b7fdb2dd7f68e7f3789720936ae074dd362f0c ; SCELLE_P=83ce7a91f681b36668a9f91424d53ebd632b50b1
CITE_S=326601cf39d91754ceb13813f10c47a8e6f4a465 ; SCELLE_S=7a238666630a6d6dca064e8da6b309320060200d
CITE_E=5f2f9bf505b4b57ccd3df71178d0a1f596e97899 ; SCELLE_E=   # 40 hex, résolu en A0 depuis 52eb34c8 (texte par épisode commité)
SCELLEMENT=139a81d37fbd2255aff8d27698f84b47b9433221 ; CODE_CITE=f921fcec10539f1565fab410624a926efdfec12e
ADDENDUM=prereg/R1-addendum-relance-v3.md ; ADDENDUM_SHA=88e262e26ea38a30e8acdf0cdf204cbdaba381baf3dbc352b4333d1fe6b299a4
PY=$DEPOT/.venv/bin/python
V2R=brouillons/preuves-mentors-v1/reception-r1-relance-v2           # relatif à $DEPOT
SCRIPT=$DEPOT/$V2R/ecrire_fiches_reception_v2.py
FICHE_R=$V2R/fiche-reception-r1-relance-v3-v1.md                     # fiche de réception (relatif à $DEPOT)
FICHE_P=prereg/fiche-reception-principale-r1-r2-v1.json ; FICHE_S=prereg/fiche-reception-blanche-noire-v3.json
PREREG_P=prereg/analyse-principale-r1-r2-v1.md ; PREREG_S=prereg/analyse-blanche-noire-v3.md
PREREG_E=prereg/analyse-par-episode-v1.md
J3=20261102-004328-r2-juge3b-reel ; J8=20261102-005048-r2-juge8b-reel
QUI="session conv-audit (Claude), session <id>"
# --- à remplir : SIGNATURE avant 0.1 ; FICHE_R_SHA en 0.3 ; le reste depuis le message de versement (P4) ---
SIGNATURE=                        # lignes d'attribution des commits de la session qui exécute (son rappel système)
FICHE_R_SHA=                      # 64 hex : compagnon de la fiche de réception (0.3)
VERSEMENT=                        # 40 hex : commit du versement sur calcul/r1-r2-reel-v1
REJEU=                            # nom du run lu, AAAAMMJJ-HHMMSS-r1-rejeu-reel
BRANCHE_SOURCE=calcul/r1-relance-v3-reel-v1                          # calcul/r1-relance-v3-reel-v2 après une reprise E21
ARRETEE_E21= ; ARRET_E21_SHA= ; ANNONCE_E21=                         # vides sans reprise E21 (sinon : run, 64 hex ou absent, n° du message)
SCR=/tmp/claude-0/reception-r1-relance-v2 ; mkdir -p "$SCR"          # hors du dépôt
export PYTHONDONTWRITEBYTECODE=1
```

## 0. Fiche de réception, avant toute récupération (C-1 ; R-5) — ≈ 5 minutes, dès maintenant

La fiche `$FICHE_R` a été écrite le 3 novembre 2026 par le script, en mode « avant la récupération » (rapport,
section 2) ; elle n'est pas scellée. La session la contre-éprouve (0.2), la scelle avec le dossier (0.3) et l'annonce
(0.4). La création de l'instance n'en dépend pas (addendum v3, E8 (d)) ; la récupération, si (E8 (e)).

### 0.1 Constat

```bash
cd $DEPOT && date -u
git for-each-ref --format='%(refname)' | grep -c -E '(^|/)calcul/' ; git for-each-ref refs/remotes | grep -c donnees
git show $SCELLEMENT:$ADDENDUM | sha256sum ; git show $SCELLEMENT:$ADDENDUM.sha256
git diff --quiet $CODE_CITE $SCELLEMENT -- src tests scripts && echo "code du commit cité = code du commit de scellement"
test ! -e "$FICHE_R.sha256" && echo "fiche non encore scellée" ; test -n "$SIGNATURE" && echo "signature remplie"
```

**Doit afficher :** l'heure ; `0` et `0` (aucune référence `calcul/…`, aucune `donnees` : rien n'est récupéré) ;
`88e262e26ea38a30e8acdf0cdf204cbdaba381baf3dbc352b4333d1fe6b299a4  -`, puis la même empreinte suivie de
`R1-addendum-relance-v3.md` ; `code du commit cité = code du commit de scellement` (constaté le 3 novembre) ;
`fiche non encore scellée` ; `signature remplie`. Une référence `calcul/…` présente : arrêt (une récupération a eu
lieu avant la fiche).

### 0.2 Contre-épreuve : le script réécrit la fiche ailleurs ; les attendus doivent être identiques

```bash
cd $DEPOT && nice -n 10 $PY -I "$SCRIPT" avant-recuperation --depot . --sortie "$SCR/fiche-contre-epreuve.md" --qui "$QUI"
$PY -I - "$FICHE_R" "$SCR/fiche-contre-epreuve.md" <<'PY'
import json, sys
def bloc(p):
    t = open(p, encoding="utf-8").read()
    b = json.loads(t.split("<!-- attendus-machine : debut -->")[1].split("<!-- attendus-machine : fin -->")[0].strip()[7:-3])
    for x in b["textes"].values():
        x.pop("commit")      # la tête de la branche de travail avance ; les empreintes, elles, sont comparées
    return b
print("attendus identiques" if bloc(sys.argv[1]) == bloc(sys.argv[2]) else "ATTENDUS DIFFÉRENTS : arrêt")
PY
```

**Doit afficher :** `gardes passées : recuperation, config-table, canonique, table, ligne-104, attentes-texte, piece,
compagnon` ; `fiche de réception : … <empreinte>` (autre que celle de `$FICHE_R` : l'heure et la tête diffèrent) ;
`attendus identiques`. Sinon : arrêt ; la session écrit par le script une fiche nouvelle (`--sortie …-v2.md`, R12) et
signale l'écart. (Mesuré : 0,19 s sur le vrai dépôt.)

### 0.3 Scellement, commit, poussée (le dossier v2 entier ; la fiche en dernier dans la liste)

```bash
cd $DEPOT && PYTHONPATH=src $PY -m controle_ia.scellement sceller $V2R/procedure-reception-lecture-r1-relance-v2.md \
  $V2R/ecrire_fiches_reception_v2.py $V2R/tests/test_ecrire_fiches_reception_v2.py $V2R/tests/banc_mutations_v2.py \
  $V2R/essais-v2-sortie.txt $V2R/banc-mutations-v2-sortie.txt $V2R/rapport-preparation-reception-v2.md "$FICHE_R"
FICHE_R_SHA=$(cut -c1-64 "$FICHE_R.sha256") && echo "$FICHE_R_SHA"
git add -- $V2R && git commit -q -m "Réception de la relance de R1 (addendum v3) : fiche de réception scellée avant la récupération (C-1), procédure et script v2" \
  -m "$SIGNATURE" -- $V2R
git show --name-only --format= HEAD | grep -c . ; git push origin canal/conv-audit-n04 ; git log -1 --format='%H %cI' ; date -u
```

**Doit afficher :** huit sceaux écrits ; l'empreinte de la fiche, égale à celle du rapport (section 6) si la fiche n'a pas
été réécrite ; `16` (huit fichiers et leurs compagnons) ; un push réussi ; le commit et son heure ; l'heure.

### 0.4 Annonce au canal, puis registre

Message à session-depot, selon l'usage du canal (numéro, empreinte du message) :
- la fiche : chemin `$FICHE_R`, empreinte `$FICHE_R_SHA`, commit de 0.3 sur `canal/conv-audit-n04` (session-depot
  vérifie que le compagnon est égal ; addendum v3, « Liste d'arrêt », « Récupération ») ;
- ce que le message de versement doit donner : commit du versement sur `calcul/r1-r2-reel-v1` ; nom du run ; identifiant
  de l'instance et heure de sa destruction ; **heure de la récupération** de la branche de la course (postérieure à ce
  message) ; branche source ; en cas de reprise E21 : nom de la course arrêtée, empreinte de son `arret.json` (ou
  « absent »), numéro et empreinte du message d'annonce de la reprise, fait avant la création ;
- ce qu'il ne doit pas porter : aucune valeur observée de P-R5 ni lecture de l'instrument (ni ligne `etape=fin`, ni
  `etape=fidelite`, ni `etape=controle_negatif`, ni la sortie standard du module, ni `fidelite_toutes`) ; après une
  reprise E21, les lignes `etape=fidelite lecture=…` et `etape=controle_negatif lecture=…` du journal de la course
  arrêtée vont dans un fichier à part, scellé, que la session ne lit pas et transmet aux lecteurs R13 (étape I). Les
  jalons de comptes fixés par la table (`etape=verification_table …`, `etape=reconstruction …`) peuvent figurer.

**Consigner au registre** : heure du scellement, `$FICHE_R_SHA`, commit, numéro du message.

## Préconditions de l'étape A (points d'arrêt, consignés au registre avant l'étape A)

| n° | précondition | preuve attendue |
|---|---|---|
| P1 | **Fiche de réception scellée, commitée, poussée et annoncée avant la récupération** des sorties de la course par session-depot (C-1) | 0.3 et 0.4 faits ; `$FICHE_R_SHA` ; bloc A1 : sceau conforme, commit et heure du scellement **antérieurs** à l'heure de récupération donnée par le message de versement (P4) ; sinon : C-1 non tenu, nœud |
| P2 | **Concordance d'un lecteur neuf de conv-audit sur la version scellée** de l'addendum v3 (section 9 de `8482b4cd…`, points 1 à 4), rapport scellé et commité, verdict « concordant » | chemin et empreinte, égaux à ceux que session-depot a consignés dans `docs/notes/runs-r1-r2-r4-v1/concordance-relance-v3-consignee-v1.md` (condition de création, addendum v3, étape 1 ; branche `prep/r1-relance-v3`, récupérée par refspec explicite, jamais `calcul/…`) |
| P3 | Nos trois textes scellés inchangés : principale `8e267952…` (branche `analyse-principale-r1-r2-v1`, commit `83ce7a91`), secondaire `1f6a6da2…` (`analyse-blanche-noire-v3`, `7a238666`), par épisode `26a3ff72…` (`52eb34c8`) | blocs A0 et A1 |
| P4 | **Message de versement** de session-depot : `$VERSEMENT`, `$REJEU`, instance et heure de destruction, heure de récupération, `$BRANCHE_SOURCE` ; s'il y a eu une reprise E21 : `$ARRETEE_E21`, `$ARRET_E21_SHA`, `$ANNONCE_E21` ; aucune valeur observée de P-R5 (sinon : déclarée au registre et aux lecteurs R13) ; les juges restent ceux déjà versés (`$J3`, `$J8` ; addendum v3, « R2 ») | message n°, empreinte ; aucun nom n'est deviné depuis l'arbre |
| P5 | Aucun arbre séparé existant aux chemins ci-dessus, aucune branche locale de ces noms | bloc A2 |
| P6 | Les commits cités sont présents dans le clone | bloc A0 |

## A0. Commits cités présents (le clone est superficiel) — ≈ 1 à 3 minutes s'il faut approfondir (réseau)

```bash
cd $DEPOT && git rev-parse --is-shallow-repository
for c in $CITE_P $SCELLE_P $CITE_S $SCELLE_S $CITE_E 52eb34c8 $SCELLEMENT $CODE_CITE; do
  git rev-parse -q --verify "$c^{commit}" >/dev/null && echo "présent $c" || echo "ABSENT $c"; done
git merge-base --is-ancestor $CITE_S $CITE_P && echo "ascendance $CITE_S → $CITE_P visible"
```

**Constat du 3 novembre 2026 (05:27 UTC)** : `true` (racine greffée `d1b1c8c6`) ; `5f2f9bf5…` et `52eb34c8` **absents** ;
`326601cf` présent mais non atteignable depuis `a8b7fdb2` (`git rev-list a8b7fdb2` : 4 commits) : le bloc A1 de la v1
s'arrêterait sur « ordre des commits cités » et l'étape F ne pourrait pas fusionner `52eb34c8`. S'il reste une ligne
`ABSENT` ou si l'ascendance n'est pas visible : approfondir les seules branches de travail, par refspec explicite, jamais
`calcul/…` :

```bash
cd $DEPOT && git fetch -q --unshallow origin "+refs/heads/canal/conv-audit-n04:refs/remotes/origin/canal/conv-audit-n04" \
  "+refs/heads/analyse-principale-r1-r2-v1:refs/remotes/origin/analyse-principale-r1-r2-v1" \
  "+refs/heads/analyse-blanche-noire-v3:refs/remotes/origin/analyse-blanche-noire-v3" ; echo "code $?"
git for-each-ref refs/remotes | grep -c donnees ; git for-each-ref --format='%(refname)' | grep -c -E '(^|/)calcul/'
```

puis relancer le premier bloc, et `SCELLE_E=$(git rev-parse --verify 52eb34c8^{commit}) && echo "$SCELLE_E"`.

**Doit afficher :** `code 0`, `0`, `0` ; puis `présent` pour les huit commits ; `ascendance … visible` ; `SCELLE_E` en 40
hexadécimaux (noté au registre). Sinon : arrêt (le commit du texte par épisode ou de son code n'est pas dans l'historique
de ces branches ; le localiser est un nœud ; le texte lui-même, `26a3ff72…`, est commité à la tête de la branche de
travail). L'approfondissement n'a pas été éprouvé par l'auteur de cette procédure (réseau interdit au sous-agent) : un
échec arrête ; aucune autre forme n'est essayée hors registre.

## A. Constat (dépôt principal) — ≈ 1 minute

### A1. Références, textes scellés, fiche de réception

```bash
cd $DEPOT && git for-each-ref --format='%(refname) %(objectname)' 'refs/heads/calcul/*' 'refs/remotes/origin/calcul/*'; echo "fin de liste"
git rev-parse origin/$BR_P origin/$BR_S $SCELLE_E
git show origin/$BR_P:$PREREG_P | sha256sum ; git show origin/$BR_S:$PREREG_S | sha256sum ; git show $SCELLE_E:$PREREG_E | sha256sum
git merge-base --is-ancestor $CITE_S $CITE_P && git merge-base --is-ancestor $CITE_E HEAD && echo "ordre des commits cités conforme"
git diff --quiet $CITE_E $SCELLE_E -- src tests && echo "code par épisode inchangé entre commit cité et texte scellé"
git merge-tree --write-tree --name-only $SCELLE_P $SCELLE_E > "$SCR/fusion-anticipee.txt"; echo "fusion anticipée : code $? ; $(wc -l < "$SCR/fusion-anticipee.txt") ligne(s)"
test "$(git show $SCELLEMENT:$ADDENDUM | sha256sum | cut -c1-64)" = "$ADDENDUM_SHA" && echo "addendum v3 scellé conforme"
(cd "$(dirname "$FICHE_R")" && sha256sum -c "$(basename "$FICHE_R").sha256") && test "$(cut -c1-64 "$FICHE_R.sha256")" = "$FICHE_R_SHA" \
  && echo "fiche de réception : sceau conforme, empreinte annoncée au canal"
git log -1 --format='scellement de la fiche : %H %cI' -- "$FICHE_R.sha256"
test -n "$FICHE_R_SHA" -a -n "$VERSEMENT" -a -n "$REJEU" -a -n "$SCELLE_E" -a -n "$SIGNATURE" && echo "paramètres remplis"
```

**Doit afficher :**
- la liste des références `calcul/*` du dépôt, puis `fin de liste` : les noter telles quelles (constat du 3 novembre :
  aucune) ; aucun fichier de ces références n'est ouvert ;
- `83ce7a91…`, `7a238666…`, `$SCELLE_E` ;
- `8e2679526b2777a9fe8564dd5f5fdaf98b70affd759cf47857abc8b168d92537`, `1f6a6da2c551060a5f90ff3358b0aaf276dd9f336a5b953e6d93233c8c581fa9`,
  `26a3ff72e3a39636d3bdb965971fd1b237a04acc133a31a42f9a695d6d5970a4` ;
- `ordre des commits cités conforme` ; `code par épisode inchangé …` ;
- `fusion anticipée : code 0 ; 1 ligne(s)` (l'arbre résultant seul ; vérifié le 2 novembre dans le clone complet) ;
- `addendum v3 scellé conforme` ;
- `fiche-reception-r1-relance-v3-v1.md: OK`, puis `fiche de réception : sceau conforme, empreinte annoncée au canal` ;
- `scellement de la fiche : <commit> <heure>` : heure **antérieure** à l'heure de récupération du message de versement
  (P1 ; sinon arrêt, nœud) ;
- `paramètres remplis`.

### A2. Arbres et branches libres

```bash
cd $DEPOT && git worktree list && test ! -e "$ARBRE_P" && test ! -e "$ARBRE_S" \
  && ! git show-ref --quiet refs/heads/$BR_P && ! git show-ref --quiet refs/heads/$BR_S && echo LIBRE
```

**Doit afficher** la liste des arbres (le dépôt seul) puis `LIBRE`. Sinon : arrêt (un arbre ou une branche locale de ce
nom existe déjà ; ne rien supprimer, signaler).

## B. Arbre séparé de la principale, recréé — ≈ 2 minutes (essais compris, 20 à 40 s)

```bash
cd $DEPOT && git worktree add -b "$BR_P" "$ARBRE_P" "origin/$BR_P"
cd "$ARBRE_P" && test "$(git rev-parse HEAD)" = "$SCELLE_P" && echo "HEAD = texte scellé" && git status --porcelain --untracked-files=all | wc -l
test "$(git rev-parse HEAD~1)" = "$CITE_P" && echo "parent = commit cité" && git diff --quiet "$CITE_P" HEAD -- src tests && echo "code identique au commit cité"
PYTHONPATH=src $PY -c "import controle_ia; print(controle_ia.__file__)"
PYTHONPATH=src $PY -c "from controle_ia.analyse_principale_r1_r2 import lecture_v1; print(lecture_v1.exiger_versions())"
PYTHONPATH=src $PY -c "from controle_ia.prereg import exiger_prereg_scelle; print(exiger_prereg_scelle('$PREREG_P'))"
git rev-parse HEAD:donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl
sha256sum donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl donnees/20261019-230011-p3-reel/scores-p3.npz
PYTHONPATH=src $PY -m controle_ia.scellement verifier donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl \
  donnees/20261019-230011-p3-reel/scores-p3.npz diag/20261019-230011-p3-reel/resume.json \
  diag/20261019-230011-p3-reel/episodes-p3.json diag/20261019-230011-p3-reel/sondes-figees.json
PYTHONPATH=src:tests nice -n 10 $PY -m pytest -q -p no:cacheprovider --basetemp="$SCR/essais-arbre-p" \
  tests/test_analyse_principale_r1_r2_v1.py tests/test_analyse_principale_r1_r2_v2.py 2>&1 | tail -1
git status --porcelain --untracked-files=all | wc -l ; ls runs | grep -c . ; ls donnees | grep -v -c 20261019-230011-p3-reel
```

**Doit afficher** (inchangé depuis la v1 ; non revérifié dans ce clone, où aucun arbre n'a été créé) : la création de
l'arbre ; `HEAD = texte scellé`, `0` ; `parent = commit cité`, `code identique au commit cité` ;
`/home/claude/controle-ia-analyse-principale-r1-r2-v1/src/controle_ia/__init__.py` ;
`{'python': '3.13.18', 'numpy': '2.4.6', 'scipy': '1.17.1'}` ; `8e267952…` ; `bad1403f1454f46de23adbbee59da8586170c7ec`
(revérifié le 3 novembre par `git rev-parse 83ce7a91:…`) ; `ba05fa13…` et `968414fc…` ; cinq sceaux conformes ;
`24 passed` ; `0` ; le nombre de manifestes déjà suivis sous `runs/` (noter) ; `0`.

## C. Récupération de `calcul/r1-r2-reel-v1` seule, dans l'arbre de la principale — ≈ 1 à 3 minutes (réseau)

```bash
cd "$ARBRE_P" && git fetch --no-tags origin "+refs/heads/calcul/r1-r2-reel-v1:refs/remotes/origin/calcul/r1-r2-reel-v1" && git rev-parse FETCH_HEAD origin/calcul/r1-r2-reel-v1
test "$(git rev-parse FETCH_HEAD)" = "$VERSEMENT" && echo "versement = commit annoncé"
git for-each-ref refs/remotes | grep -c donnees ; git status --porcelain --untracked-files=all | wc -l ; ls donnees | grep -v -c 20261019-230011-p3-reel
git ls-tree -d --name-only FETCH_HEAD runs/ diag/ donnees/
git show FETCH_HEAD:diag/20261102-002114-r1-rejeu-reel/arret.json | sha256sum
git ls-tree -r --name-only FETCH_HEAD "runs/$REJEU" "diag/$REJEU" "donnees/$REJEU" "runs/$J3" "diag/$J3" "donnees/$J3" "runs/$J8" "diag/$J8" "donnees/$J8"
if [ -n "$ARRETEE_E21" ]; then
  git ls-tree -r --name-only FETCH_HEAD "runs/$ARRETEE_E21" "diag/$ARRETEE_E21" | sed 's/^/E21, noté : /'
  echo "E21, fichiers d'activations : $(git ls-tree -r --name-only FETCH_HEAD "donnees/$ARRETEE_E21" | grep -c .)"
  git cat-file -e "FETCH_HEAD:diag/$ARRETEE_E21/arret.json" 2>/dev/null && git show "FETCH_HEAD:diag/$ARRETEE_E21/arret.json" | sha256sum
fi
```

**Doit afficher :**
- deux fois le même commit, puis `versement = commit annoncé` (sinon : arrêt, le fournisseur n'a pas annoncé ce commit) ;
- `0` ; `0` ; `0` (« `donnees` = 0 » dans les références ; le fetch n'a rien écrit dans l'arbre ni dans l'index ; aucun
  dossier sous `donnees/` hors P3) ;
- la liste des runs par nom seulement : on y attend `20261102-002114-r1-rejeu-reel` (première course, arrêtée), `$J3`,
  `$J8`, le run de R4 (arrêté), le ou les runs du rejeu à graine s'ils ont été versés, `$REJEU`, et, après une reprise
  E21, la course arrêtée si session-depot l'a versée (son étape 7 ne verse que `$REJEU`) ; **tout nom absent de cette
  attente est noté, aucun fichier n'en est ouvert** ;
- `c6671d2c9534463f82da90c21eba80f29a2bce04e898643b59a0caa4c9a9eb07` (l'`arret.json` de la première course est intact ;
  haché par un tube, jamais ouvert) ;
- la liste exacte des fichiers des trois runs à recevoir, soit, pour `$REJEU` : `runs/$REJEU/manifeste.json`,
  `diag/$REJEU/rejeu-activations.json` (ou `arret.json` seul), les trois
  `donnees/$REJEU/activations-p3-rejeu-v1{,-maximum,-complement-hors-cout}.npz` (absents si `arret.json`), et leurs
  compagnons `.sha256` ; pour chaque juge : `manifeste.json`, `juge-actions.json`, `scores-juge{3b,8b}-p3-v1.npz` et
  compagnons. **Un nom en plus ou en moins arrête** (le script de D le refuse aussi) ;
- sans reprise : rien d'autre ; après une reprise E21 : les noms de la course arrêtée (notés), `E21, fichiers
  d'activations : 0` (sinon E21 ne s'appliquait pas : arrêt, nœud) et, si son `arret.json` est versé, son empreinte égale
  à `$ARRET_E21_SHA` ; si la course arrêtée n'est pas versée, la noter « non versée » ; rien n'en est ouvert.

Puis écriture des fichiers, index pour `runs/` et `diag/` seulement :

```bash
cd "$ARBRE_P" && for R in "$REJEU" "$J3" "$J8"; do
  git checkout FETCH_HEAD -- "runs/$R" "diag/$R" || { echo "ARRÊT checkout $R"; break; }
  for f in $(git ls-tree -r --name-only FETCH_HEAD "donnees/$R"); do test ! -e "$f" || { echo "EXISTE $f : ARRÊT"; break 2; }
    mkdir -p "$(dirname "$f")"; git show "FETCH_HEAD:$f" > "$f"; done
done; echo "écriture faite"
PYTHONPATH=src $PY -m controle_ia.scellement verifier $(git ls-tree -r --name-only FETCH_HEAD "donnees/$REJEU" "diag/$REJEU" "runs/$REJEU" "donnees/$J3" "diag/$J3" "runs/$J3" "donnees/$J8" "diag/$J8" "runs/$J8" | grep -v '\.sha256$') | grep -c '^OK'
git add -- "runs/$REJEU" "diag/$REJEU" "runs/$J3" "diag/$J3" "runs/$J8" "diag/$J8"
git commit -q -m "Réception R1 relancé (addendum v3) et juges : runs/ et diag/ du fournisseur ($(git rev-parse --short=8 FETCH_HEAD) sur calcul/r1-r2-reel-v1)" \
  -m "$SIGNATURE" -- "runs/$REJEU" "diag/$REJEU" "runs/$J3" "diag/$J3" "runs/$J8" "diag/$J8"
git show --name-only --format= HEAD | grep -v -c -E "^(runs|diag)/" ; git status --porcelain --untracked-files=all | wc -l
```

**Doit afficher :** `écriture faite` sans `ARRÊT` ni `EXISTE` ; le compte des `OK` égal au nombre de fichiers hors
compagnons (11 si le rejeu est allé au bout : 3 manifestes + 1 résultat + 3 `.npz` du rejeu + 2 × (1 résultat + 1
`.npz`) ; 8 s'il s'est arrêté : 3 manifestes + `arret.json` + 2 × 2) ; `0` (le commit ne porte que `runs/` et `diag/`) ;
`0` (arbre propre : `donnees/` est ignoré). Durée mesurée de la vérification des sceaux sur trois fichiers de 59 Mo :
0,3 s (v1).

## D. Fiches JSON de nos analyses, écrites par le script, scellées et commitées **avant toute lecture** — ≈ 3 minutes

### D1. Écriture (le script relit la fiche de réception, compare et refuse, n'ouvre aucun `.npz`)

```bash
cd "$ARBRE_P" && E21=() && { [ -z "$ARRETEE_E21" ] || E21=(--course-arretee-e21 "$ARRETEE_E21" --arret-e21-sha256 "$ARRET_E21_SHA" --annonce-e21 "$ANNONCE_E21"); }
nice -n 10 $PY -I "$SCRIPT" apres-versement --racine . --fiche-reception "$DEPOT/$FICHE_R" --fiche-reception-sha256 "$FICHE_R_SHA" \
  --rejeu "$REJEU" --juge3b "$J3" --juge8b "$J8" --qui "$QUI" --commit-versement "$(git rev-parse FETCH_HEAD)" \
  --branche-source "$BRANCHE_SOURCE" "${E21[@]}" 2>&1 | tee "$SCR/fiches-$REJEU.txt"; echo "code ${PIPESTATUS[0]}"
```

**Doit afficher :**
- une ligne `contexte déclaré du juge 3B …` (à lire : s'il contient la consigne ou l'indication privée d'un épisode,
  **arrêt** : la secondaire exige `R2: null` avec `consigne_dans_contexte` — cas non prévu par le script, fiche à écrire à
  la main et à soumettre ; nœud) ;
- `fiche principale : prereg/fiche-reception-principale-r1-r2-v1.json <empreinte>` ; `fiche secondaire :
  prereg/fiche-reception-blanche-noire-v3.json <empreinte>` ;
- `gardes passées : fiche, attendus, nom-rejeu, e21, rattachement, texte, commande, decisif, configuration, commit,
  entropie, table-comparee, provenance, comptes, juges, P-R5` (rejeu arrêté : sans `table-comparee`, `provenance`,
  `comptes`) ;
- `fichiers vérifiés contre leur compagnon : 11` (rejeu arrêté : 8) ;
- `ouverts : [… runs/$REJEU/manifeste.json, … rejeu-activations.json (ou arret.json), … juge-actions.json × 2]` ;
- `code 0`.

Un `ARRÊT [garde] : …` (code 2) n'écrit aucune fiche. Gardes et sens : `fiche` (fiche de réception absente, non scellée,
modifiée, ou d'empreinte autre que celle du canal) ; `attendus` (bloc illisible) ; `nom-rejeu` (le run n'est pas un
`…-r1-rejeu-reel` neuf) ; `e21` (reprise incohérente avec la branche source) ; `rattachement` (run ou manifeste du
résultat ≠ versés) ; `texte` (`preenregistrement` ≠ addendum v3 scellé) ; `commande` ; `decisif` ; `configuration`
(canonique ≠ `1cfb7fba…`, recalcul ≠, table citée ≠ v3) ; `commit` (≠ `139a81d3…`, ou arbre non propre) ; `entropie` ;
`table-comparee` (`tokenisation.table_sha256` ≠ `ead8a668…`) ; `provenance` (`tokenisation.addendum` ≠
`prereg/R1-addendum-relance-v2.md` à l'identique : autre code) ; `comptes` (dont `episodes_non_resolus` ≠ [] : E19) ;
`juges` (run ou empreinte des scores ≠ cités) ; `P-R5` (une fiche porterait une clé interdite ou un nombre : défaut du
script) ;
`fichiers`, `forme`, `R12` (comme la v1). Consigner la garde et le message ; nœud de Lazar pour tout écart à la fiche.

Ce que le script a fait en ouvrant le manifeste et les résultats JSON (clés nommées seulement, jamais de tableau ni de
valeur interdite) : sceaux confrontés aux compagnons ; noms exacts ; contrôles de la fiche de réception, sections 3 à 5 ;
`verdict_fidelite` ; `fichiers` du résultat = empreintes des `.npz` versés ; pointeurs de la fiche secondaire résolus
(existence seulement) ; les noms des clés lues sont dans `redaction.cles_lues`, leurs valeurs ne sont pas recopiées
(elles égalent les attendus de la fiche de réception ; garde `P-R5` : aucune clé interdite ni aucun nombre dans les
fiches JSON, qui ne contiennent que chemins, empreintes, pointeurs et motifs, analyse secondaire l. 24).

Si le rejeu s'est arrêté (`arret.json` et pas de `donnees/$REJEU`) : même commande ; les contrôles du manifeste valent ;
le script écrit `R1: null` avec le motif fermé lu dans `verdict_fidelite` (`rejeu_non_conforme` ou `rejeu_en_echec`) ;
la principale lit alors « rejeu non validé : rien n'est lu » ; la suite (E à H) se fait quand même, car les lectures sont
rapportées en entier quel qu'en soit le signe, mais la lecture par épisode ne lit rien non plus (sa l. 111).

### D2. Contrôle de forme par les deux lecteurs, sans donnée, puis scellement et commit de la fiche principale seule

```bash
cd "$ARBRE_P" && PYTHONPATH=src $PY -c "from pathlib import Path; from controle_ia.analyse_principale_r1_r2.entrees_v1 import lire_fiche; print(lire_fiche(Path('.'), '$FICHE_P', scellee=False)[1])"
PYTHONPATH=src $PY -c "from pathlib import Path; from controle_ia.analyse_blanche_noire.entrees_v3 import lire_fiche_v3; print(lire_fiche_v3(Path('.'), '$FICHE_S', scellee=False)[1])"
$PY -c "import json; f=json.load(open('$FICHE_P')); print(f['R1'] is not None, f['motif_R1'], f['R2']['juge8b'] is not None, f['motif_R2'])"
$PY -c "import json; r=json.load(open('$FICHE_P'))['redaction']; print(r['fiche_reception']['sha256'] == '$FICHE_R_SHA', r['addendum_v3']['sha256'][:12], r['provenance_table']['valeur'], r['e21']['reprise'], r['episodes_non_inversibles_declares'], len(r['controles']))"
PYTHONPATH=src $PY -m controle_ia.scellement sceller "$FICHE_P"
cp "$FICHE_S" "$SCR/fiche-secondaire-a-copier.json" && sha256sum "$FICHE_S" "$SCR/fiche-secondaire-a-copier.json" && rm "$FICHE_S"
git add "$FICHE_P" "$FICHE_P.sha256" && git commit -q -m "Analyse principale de R1-R2 : fiche de réception scellée (R1 relancé $REJEU, addendum v3)" \
  -m "$SIGNATURE" -- "$FICHE_P" "$FICHE_P.sha256"
git show --name-only --format= HEAD ; git status --porcelain --untracked-files=all | wc -l ; git push origin "$BR_P"
```

**Doit afficher :** les deux empreintes des fiches (les lecteurs n'ont rien levé ; le code de `entrees_v3` est identique
dans cet arbre et au commit cité `326601cf`, vérifié le 2 novembre ; `entrees_v1` et `entrees_v3` du dépôt de travail
identiques aux commits cités, revérifié le 3 novembre) ; `True None True None` (rejeu livré, deux juges) ;
`True 88e262e26ea3 prereg/R1-addendum-relance-v2.md False [] 16` (sans reprise ; `True` à la place du premier `False`
après une reprise E21 ; 13 au lieu de 16 si le rejeu s'est arrêté) ; l'empreinte scellée de la fiche principale ; les
deux copies de la fiche secondaire d'empreinte égale (elle est retirée de cet arbre : elle appartient à l'arbre de la
secondaire, D3) ; exactement `prereg/fiche-reception-principale-r1-r2-v1.json` et son compagnon ; `0` ; un push réussi.

### D3. Arbre de la secondaire, recréé ; sa fiche scellée et commitée seule, toujours avant toute lecture

```bash
cd $DEPOT && git worktree add -b "$BR_S" "$ARBRE_S" "origin/$BR_S" && cd "$ARBRE_S"
test "$(git rev-parse HEAD)" = "$SCELLE_S" && test "$(git rev-parse HEAD~1)" = "$CITE_S" && git diff --quiet "$CITE_S" HEAD -- src tests && echo "arbre S conforme"
PYTHONPATH=src $PY -c "import controle_ia; print(controle_ia.__file__)" ; PYTHONPATH=src $PY -c "from controle_ia.prereg import exiger_prereg_scelle; print(exiger_prereg_scelle('$PREREG_S'))"
sha256sum donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl donnees/20261019-230011-p3-reel/scores-p3.npz | cut -c1-12
cp "$SCR/fiche-secondaire-a-copier.json" "$FICHE_S" && sha256sum "$FICHE_S" | cut -c1-12
PYTHONPATH=src $PY -c "from pathlib import Path; from controle_ia.analyse_blanche_noire.entrees_v3 import lire_fiche_v3; print(lire_fiche_v3(Path('.'), '$FICHE_S', scellee=False)[1])"
PYTHONPATH=src $PY -m controle_ia.scellement sceller "$FICHE_S" && git add "$FICHE_S" "$FICHE_S.sha256" && git commit -q -m "Analyse boîte blanche / boîte noire v3 : fiche de réception scellée (R1 relancé $REJEU, addendum v3)" \
  -m "$SIGNATURE" -- "$FICHE_S" "$FICHE_S.sha256"
git show --name-only --format= HEAD ; git status --porcelain --untracked-files=all | wc -l ; git push origin "$BR_S"
```

**Doit afficher :** `arbre S conforme` ; `/home/claude/controle-ia-analyse-bn-v3/src/controle_ia/__init__.py` ;
`1f6a6da2…` ; `ba05fa13…` et `968414fc…` (P3 suivi par git, vérifié, jamais copié par-dessus) ; l'empreinte de la fiche
(celle de D1 et de D2 : identique à l'octet) ; la même empreinte par le lecteur ; exactement
`prereg/fiche-reception-blanche-noire-v3.json` et son compagnon ; `0` ; un push réussi. (Les fichiers que la fiche cite
ne sont pas encore dans cet arbre : ils y sont écrits en H, où leur empreinte est confrontée à la fiche avant le
lancement.)

**À ce point, consigner au registre** : `$REJEU`, le commit du versement, l'heure de la récupération par session-depot
(postérieure au scellement de la fiche de réception), les deux empreintes des fiches JSON et leurs commits, ce que le
script a ouvert et lu (`redaction.ce_qui_a_ete_ouvert`, `redaction.cles_lues` : noms seulement), la
reprise E21 s'il y en a eu une, et « aucune lecture n'a eu lieu ; aucune valeur observée de P-R5 vue » (ou ce qui a été
vu, déclaré).

## E. Lancement décisif de l'analyse principale — ≈ 1 à 5 minutes (mesuré : 9,8 s de calcul à la taille réelle sur données synthétiques non compressées ; plus la décompression des trois fichiers)

```bash
cd "$ARBRE_P" && RUN_P=$(date -u +%Y%m%d-%H%M%S)-analyse-principale-r1-r2-v1 && echo "$RUN_P"
PYTHONPATH=src nice -n 10 $PY -m controle_ia.analyse_principale_r1_r2.lecture_v2 --fiche "$FICHE_P" --run-analyse "$RUN_P" --prereg "$PREREG_P" > "$SCR/lancement-$RUN_P.txt" 2>&1; echo "code $?"
ls "runs/$RUN_P" "diag/$RUN_P" && PYTHONPATH=src $PY -m controle_ia.scellement verifier "diag/$RUN_P/analyse-principale-r1-r2-v1.json" "diag/$RUN_P/analyse-principale-r1-r2-v1.md" | grep -c '^OK'
git add -- "runs/$RUN_P" "diag/$RUN_P" && git commit -q -m "Analyse principale de R1-R2 : sorties de la lecture décisive $RUN_P" \
  -m "$SIGNATURE" -- "runs/$RUN_P" "diag/$RUN_P"
git status --porcelain --untracked-files=all | wc -l ; git push origin "$BR_P"
```

**Doit afficher :** `code 0` ; `manifeste.json`, les deux sorties `.json` et `.md` avec compagnons ; `2` ; `0` ; un push
réussi. Un `ARRÊT : …` dans `$SCR/lancement-*.txt` se consigne avec son motif ; **aucun second passage** sans l'accord de
Lazar, qui ne peut porter que sur la cause technique (manifeste déjà écrit = texte épuisé). Ne pas lire l'issue avant
d'avoir commité et poussé ; la session la lit ensuite (elle n'est pas le lecteur R13).

## F. Lecture par épisode : fusion du commit cité, puis lancement — ≈ 2 minutes (mesuré : 2,0 s de calcul, synthétique, non décisif)

```bash
cd "$ARBRE_P" && git merge --no-edit "$SCELLE_E" ; echo "code $?"
git diff --quiet "$CITE_E" HEAD -- src tests && echo "code = commit cité de la lecture par épisode" ; git status --porcelain --untracked-files=all | wc -l
PYTHONPATH=src $PY -c "from controle_ia.prereg import exiger_prereg_scelle; print(exiger_prereg_scelle('$PREREG_E'))"
PYTHONPATH=src $PY -m controle_ia.scellement verifier "$FICHE_P" "diag/$RUN_P/analyse-principale-r1-r2-v1.json" | grep -c '^OK'
PYTHONPATH=src $PY -c "from controle_ia.analyse_principale_r1_r2 import lecture_v1; print(lecture_v1.exiger_versions())"
RUN_E=$(date -u +%Y%m%d-%H%M%S)-analyse-par-episode-v1 && echo "$RUN_E"
PYTHONPATH=src nice -n 10 $PY -m controle_ia.analyse_principale_r1_r2.lecture_v5 --fiche "$FICHE_P" --principale "diag/$RUN_P/analyse-principale-r1-r2-v1.json" \
  --run-analyse "$RUN_E" --prereg "$PREREG_E" > "$SCR/lancement-$RUN_E.txt" 2>&1; echo "code $?"
git add -- "runs/$RUN_E" "diag/$RUN_E" && git commit -q -m "Lecture par épisode de R1-R2 : sorties de la lecture décisive $RUN_E" \
  -m "$SIGNATURE" -- "runs/$RUN_E" "diag/$RUN_E"
git status --porcelain --untracked-files=all | wc -l ; git push origin "$BR_P"
```

**Doit afficher :** `code 0` à la fusion (sans conflit : la fusion anticipée de A1 l'a montré ; **jamais de rebasage**,
et un conflit arrête) ; `code = commit cité …` ; `0` ; `26a3ff72…` ; `2` ; les versions gelées ; `code 0` au
lancement ; `0` ; un push réussi. La fusion vient **après** E : elle ajoute des fichiers sous
`src/controle_ia/analyse_principale_r1_r2/` que la liste fermée de la principale ne cite pas.

## G. Fusion dans la branche de travail (dépôt principal) — ≈ 1 minute

```bash
cd $DEPOT && git merge --no-edit "$BR_P" ; echo "code $?" ; git push origin canal/conv-audit-n04
```

**Doit afficher** `code 0` et un push réussi (refus : `git pull --no-rebase`, puis repousser ; jamais de rebasage).

## H. Analyse secondaire, dans son arbre (créé en D3) — ≈ 8 à 10 minutes (lecture : 5 à 8 minutes selon son texte, l. 64)

```bash
cd "$ARBRE_S" && git status --porcelain --untracked-files=all | wc -l ; ls donnees | grep -v -c 20261019-230011-p3-reel
for R in "$REJEU" "$J3" "$J8"; do git checkout origin/calcul/r1-r2-reel-v1 -- "runs/$R" "diag/$R" || { echo "ARRÊT $R"; break; }
  for f in $(git ls-tree -r --name-only origin/calcul/r1-r2-reel-v1 "donnees/$R"); do test ! -e "$f" || { echo "EXISTE $f : ARRÊT"; break 2; }
    mkdir -p "$(dirname "$f")"; git show "origin/calcul/r1-r2-reel-v1:$f" > "$f"; done; done; echo "écriture faite"
git add -- runs/"$REJEU" diag/"$REJEU" runs/"$J3" diag/"$J3" runs/"$J8" diag/"$J8" && git commit -q -m "Réception R1 relancé (addendum v3) et juges : runs/ et diag/ du fournisseur ($(git rev-parse --short=8 origin/calcul/r1-r2-reel-v1))" \
  -m "$SIGNATURE" -- runs/"$REJEU" diag/"$REJEU" runs/"$J3" diag/"$J3" runs/"$J8" diag/"$J8"
$PY -c "import json, hashlib, pathlib; f = json.load(open('$FICHE_S')); e = [f['R1'][k] for k in ('moyenne', 'maximum', 'manifeste')] + [f['R2']['fichier'], f['R2']['manifeste']]; print(all(hashlib.sha256(pathlib.Path(x['chemin']).read_bytes()).hexdigest() == x['sha256'] for x in e), len(e))"
PYTHONPATH=src $PY -m controle_ia.scellement verifier "$FICHE_S" | grep -c '^OK' ; git status --porcelain --untracked-files=all | wc -l
RUN_S=$(date -u +%Y%m%d-%H%M%S)-analyse-blanche-noire-v3 && echo "$RUN_S"
PYTHONPATH=src nice -n 10 $PY -m controle_ia.analyse_blanche_noire.lecture_v3 --fiche "$FICHE_S" --run-analyse "$RUN_S" --prereg "$PREREG_S" > "$SCR/lancement-$RUN_S.txt" 2>&1; echo "code $?"
git add -- "runs/$RUN_S" "diag/$RUN_S" && git commit -q -m "Analyse boîte blanche / boîte noire v3 : sorties de la lecture $RUN_S" \
  -m "$SIGNATURE" -- "runs/$RUN_S" "diag/$RUN_S"
git status --porcelain --untracked-files=all | wc -l ; git push origin "$BR_S" ; cd $DEPOT && git merge --no-edit "$BR_S" ; echo "code $?" ; git push origin canal/conv-audit-n04
```

**Doit afficher :** `0` ; `0` (arbre propre, aucune donnée hors P3) ; `écriture faite` ; `True 5` (les cinq fichiers que
cite la fiche secondaire ont, dans cet arbre, l'empreinte de la fiche ; P3 est celui suivi par git, vérifié en D3) ;
`1` ; `0` ; `code 0` au lancement ; `0` ; deux push et `code 0` à la fusion. Si le rejeu s'est arrêté, la fiche
secondaire porte `R1: null` : la ligne `$PY -c …` est remplacée par la seule vérification des deux fichiers de `R2`.
Le résultat de la secondaire est rapporté en entier à côté de la principale, quel qu'en soit le signe (règle
symétrique, son texte l. 226) ; la réserve N2 (`reserve-N2-bras-moyenne-v1.md`, `c82b4d00…`) est citée par le lecteur
R13 de la secondaire (I) et par le registre à la réception.

## I. Verdicts R13 — trois lecteurs neufs, en parallèle, ≈ 15 à 30 minutes chacun

Chaque lecteur n'a écrit ni le texte, ni le code, ni la fiche, ni la concordance de la lecture qu'il juge ; il reçoit
explicitement (R2) les fichiers, et rien d'autre ne lui est raconté du résultat. Il applique la table gelée du texte,
ligne par ligne, prononce la classe de chaque comparaison, et dit si l'issue mécanique du code la contredit. Son
rapport est scellé, commité, puis soumis à Lazar (information et nœuds ouverts ; aucune porte).

| lecteur | fichiers à donner (chemins dans l'arbre fusionné, avec empreintes) |
|---|---|
| principale | `$PREREG_P` (`8e267952…`) et sa table des critères (l. 140-167) ; `$FICHE_P` ; `runs/$RUN_P/manifeste.json` ; `diag/$RUN_P/analyse-principale-r1-r2-v1.{json,md}` ; `$SCR/lancement-$RUN_P.txt` ; l'addendum v3 scellé (`88e262e2…`, commit `139a81d3`) et le rapport de concordance sur la version scellée (P2) ; la fiche de réception `$FICHE_R` (`$FICHE_R_SHA`) ; **« N-A sans objet »** (E19 de l'addendum v3 ; concordance `8482b4cd…` § 7 : aucun épisode non résolu, liste vide fixée, la l. 146 se lit après la table, aucune décision nouvelle de Lazar) ; **la réserve sur HG-2** (addendum v3, « Hypothèse » et ligne ajoutée des critères gelés ; verdict `64fab1a5…`), rapportée à côté, sans changer aucune classe ; après une reprise E21, le fichier scellé des lectures de la course arrêtée (0.4), rapportées à côté (réserve d'instrument si elles diffèrent) ; `registres/decisions.md`, entrées de gel et de réception |
| par épisode | `$PREREG_E` (`26a3ff72…`), sa table (l. 105-134) ; `diag/$RUN_E/analyse-par-episode-v1.{json,md}` et manifeste ; le résultat de la principale ci-dessus (il doit rapporter ses classes à côté, sans les rejuger) |
| secondaire | `$PREREG_S` (`1f6a6da2…`), ses critères (l. 166-200) et ses écarts déclarés (l. 11-18, 218-226) ; la réserve N2 `brouillons/preuves-mentors-v1/analyse-blanche-noire-v3/reserve-N2-bras-moyenne-v1.md` (`c82b4d00…`) ; `$FICHE_S` ; `diag/$RUN_S/…` et manifeste ; le résultat de la principale (règle symétrique : les deux lectures sont rapportées en entier, aucune citation de l'une sans l'autre) ; la conséquence déclarée par l'addendum v3 (« Prédiction », n° 343) : P-R5 contraire équivaut à plus de 10 % d'actions non fidèles, garde de la secondaire qui ne lit alors pas son bras (i) sur R1 |

Consignes communes : symétrie (R4 : un résultat trop propre, positif ou négatif, déclenche le même audit) ; un nul se lit
« non détecté à cette puissance », avec son intervalle ; P-R5 se lit « observé à côté du prédit, sans verdict propre »
(principale l. 48, l. 161) ; le lecteur de la principale vérifie que `tokenisation.episodes_non_resolus` du résultat du
fournisseur est vide (garde `comptes` de `redaction.controles` de `$FICHE_P`, attendu `[]` de la fiche de réception ;
valeur dans le résultat cité par la fiche) ; aucune citation hors du dépôt sans Lazar.

## Durées attendues

| étape | durée |
|---|---|
| 0 fiche de réception (contre-épreuve 0,19 s mesurée, scellement, commit, annonce) | 5 min, dès maintenant |
| A0 commits cités (approfondissement réseau s'il le faut) et A constat | 1 à 4 min |
| B arbre de la principale (essais 20 à 40 s) | 2 min |
| C récupération, écriture, sceaux, commit | 1 à 3 min (réseau) ; sceaux 0,3 s |
| D fiches, contrôle de forme, scellements, commits, arbre de la secondaire, registre | 4 min (script < 1 s ; 61 essais en 7,5 s) |
| E lancement décisif de la principale | 1 à 5 min (calcul 9,8 s mesuré, v1) |
| F fusion et lecture par épisode | 2 min (calcul 2,0 s mesuré, v1) |
| G fusion dans la branche de travail | 1 min |
| H secondaire (réception, lecture 5 à 8 min, fusion) | 8 à 10 min |
| **total depuis le message de versement jusqu'aux trois sorties scellées** | **≈ 20 à 30 minutes** |
| I verdicts R13 (trois lecteurs en parallèle) | 15 à 30 min |
