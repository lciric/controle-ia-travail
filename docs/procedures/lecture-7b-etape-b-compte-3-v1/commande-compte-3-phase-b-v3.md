# Commande de la mère au compte 3 — phase B : la course de la pièce « mots et coût » de T0.6 sur 7b (appel unique) — v3

- **Statut** : commande écrite de la session mère au compte 3 (mot de Lazar R-2711 (2) ; GO-2026-11-16-05, lecture de la mère, point 2,
  R-2971 : la phase B, puis la phase C, sont remises dès que leurs préalables sont prêts, dans la session hôte actuelle). À coller par
  Lazar dans **la session hôte de la phase A** (`session_016QhUrrSUMEzEqWPnQYxjHB`), avant la phase C
  (`commande-compte-3-phase-c-v3.md`, ou sa version 4, en cours). Aucune dépense (processeur ; 0 USD) ; aucun texte scellé changé ; aucun critère ajouté. Si elle
  contredit T0.6 scellé, la base (A) scellée de T0.8 ou le code de la pièce cité par la ligne `CODE-MOTS-ET-COUT-T06`, le texte ou le
  code fait foi : tu t'arrêtes et tu le dis.
- **Version 3** : écrite à partir du brouillon v2 (`commande-compte-3-phase-b-v2.md`,
  `e0dba2aad0accfba58dd6e77d4f74e264ae704be3b96ada5edb29ed84080e94f`, scellé par la mère pour son intégrité seulement, jamais remis
  ni contre-lu, gardé, R12) par un programme de couples versé (`couples_commande_phase_b_v3_v1.py`, même dossier). Changements, et
  seulement eux : (1) noms des pièces de cette version (`commande-compte-3-phase-b-v3.md`, `repetition-phase-b-v3/`,
  `rapport-preparateur-phase-b-v3.md`) et du journal provisoire (`…-v3.md`) ; (2) bloc B2 : `pip install --no-cache-dir` (le cache
  de pip doublerait la place prise par torch) ; (3) bloc B3 : la somme des tailles des cinq entrées est imprimée, à comparer aux
  tailles lues au distant (`prealables-v1.md`, P1.4) ; (4) bloc 1B : `bbis` et `b-bis` ajoutés aux noms interdits, comme à la
  phase A ; (5) section 15, point 2 : la condition de l'audit R4 de la base (A) (T0.8, l. 111) avant la ligne
  `ISSUE-MOTS-ET-COUT-T06`, que cette commande ne lève pas (nœud porté à la mère) ; (6) rédacteurs, pièces et annexe à jour. Noms du
  bac et des fichiers de marque **inchangés depuis le brouillon v2, à dessein** (comme la phase C de sa v2 à sa v4) : un bac déjà
  ouvert arrête le bloc 1B, et le marqueur d'appel est le même d'une version à l'autre (aucun second appel possible).
- **Brouillon v2** : la version 1 est le gabarit de la section 9 de `commande-compte-3-v1.md` (`21d891c5…`, gardée, R12 : « Ne joue aucun
  bloc de cette phase avec cette version »). Ses quatre marqueurs sont remplis ici (section 3) ; les défauts trouvés par la contre-lecture
  de la v1 (`contre-lecture-commande-compte-3-v1.md`, `092acef6…`) et par la vérification courte des commandes v2 et v3
  (`verification-courte-commandes-v2-v3-v1.md`, `cb9757d5…`) ne sont pas refaits : appel détaché, marqueur posé avant l'appel, bloc de
  commit relançable seul (CL3-04, CL3-05) ; contrôle à blanc qui joue les gardes de la pièce elle-même (CL3-06) ; répétition de bout en
  bout versée (CL3-07, CL3-15) ; clone superficiel approfondi avant de chercher le commit (CL3-08) ; versions exactes de l'interpréteur
  (CL3-09) ; fichier déjà placé admis s'il est égal (CL3-10) ; aucune fin de journal affichée (CL3-20). Différentiel avec le gabarit,
  choix et limites : `rapport-preparateur-phase-b-v3.md`, même dossier (différentiel avec le gabarit et avec le brouillon v2).
- **Rédacteurs** (aucun identifiant de modèle écrit ; lettres de ce dossier) : brouillon v2, un préparateur neuf, sous-agent de la
  session mère `session_016QhUrtmLyFWJP6Cy7rgfXH` (modèle B), le 2026-11-16 à partir de 12:06:54Z (`date -u`), arrêté par une limite
  d'usage vers 13:05Z avant d'avoir fini ; version 3, un préparateur neuf, sous-agent de la même session mère (modèle A), le
  2026-11-16 à partir de 13:12:02Z (`date -u`). Ni l'un ni l'autre n'est lecteur ni juge d'aucun verdict ; aucune entrée ni sortie de
  7a, de 7b ou de T0.7 ouverte (noms, tailles et empreintes seulement) ; répétitions sur données factices fabriquées par eux.
- **Mots** : « empreinte » = condensé sha256 d'un fichier ; « compagnon » = fichier `.sha256` voisin (règle R6) ; « 7b » = course de
  confirmation de T0.6, run `20261111-151701-t06-reel` ; « la pièce » = `scripts/mots_et_cout_t06_v3.py`, jouée par son lanceur
  `scripts/lancer_mots_et_cout_t06_v3.sh` (base (A) de T0.8 et base (B) « mots et coût », états des doses, issue M1 à M4) ; « UTC » =
  temps universel coordonné.
- **Pièces** (sous-dossier `repetition-phase-b-v3/` de `docs/procedures/lecture-7b-etape-b-compte-3-v1/`, chacune scellée) :

| pièce | rôle |
|---|---|
| `repetition_phase_b_jouet_v3.sh`, `fabrique_depots_jouets_phase_b_v3.py`, sortie `repetition-phase-b-jouet-sortie-v3.txt` | répétition de bout en bout de tous les blocs de cette commande sur dépôts jouets, la **vraie pièce** jouée en mode réel par son lanceur sur des entrées factices, chaque garde sur un artefact (résultat : rapport) |
| `verification_constantes_phase_b_v3.sh`, sortie `verification-constantes-phase-b-sortie-v3.txt` | chaque constante écrite en dur au bloc 1B (lignes du registre, empreintes, commit, têtes de branches, liste) comparée à `main` distant et au distant, sans rien ouvrir de 7b (résultat : rapport) |
| `attestation_qui_a_lu_quoi_compte_3_v3.py` (dossier parent, `a20f137c92022c58fd8090a2c1e25d8c575fec1b0e8a15d2190a1b1bae505a62`) | attestation du bloc 2B (celle de la phase C ; essai 17 sur 17 déjà versé) |

## 0. D'abord, pour Lazar et la mère

1. **Voie d'écriture** : une branche neuve `verdict/t06-mots-et-cout-compte-3-v1`, créée sur `main` à jour, poussée par refspec ; deux
   commits au plus : les sorties scellées de la pièce (`diag/<run de la pièce>/` et `runs/<run de la pièce>/`, rien d'autre), puis le
   journal provisoire. Jamais `main`. Les entrées de 7b ne sont jamais commitées : elles ne sont même jamais dans le dépôt (point 3).
2. **Préalables, vérifiés par les blocs** (aucun marqueur à remplir par la mère) : cette commande versée sur `main` avant d'être
   collée ; lignes `SCELLEMENT-T08-BASE-A`, `RUN-CONFIRMATION-T06` et `CODE-MOTS-ET-COUT-T06` du registre `registres/scellements-v1.md`,
   comparées à l'octet ; ni `LECTURE-T08-BASE-A` ni `ISSUE-MOTS-ET-COUT-T06` (la pièce n'a jamais tourné) ; aucune ouverture des sondes
   de T0.6 ni de l'étape B de T0.7 au journal ; liste « qui a lu quoi » v2 (la dernière scellée ; la v3 suit cette phase).
3. **Code et appel** : la pièce v3, au commit `da06bb57610f840152e4e9a8c449b036577cc582` que cite la ligne `CODE-MOTS-ET-COUT-T06`, jouée
   par son lanceur depuis ta copie du dépôt, sur la branche neuve. **Les cinq fichiers de 7b sont placés hors du dépôt**, dans le bac,
   et donnés à la pièce par son option `--racine-entrees` (prévue par son auteur :
   `docs/notes/piece-mots-et-cout-v1/rapport-developpeur-code-v3-v1.md`, section 7) : aucun fichier de 7b ne peut être commité, et le
   manifeste de la pièce déclare un dépôt propre. L'appel est **lancé détaché** (bloc B5a), attendu par
   relevés courts (B5-attente), puis commité et poussé par un bloc relançable seul (B5b). Durée attendue de la pièce : environ une
   minute (une demi-minute dans la répétition, sur des entrées factices de la taille de 7b) ; **borne : 60 minutes**, au-delà nœud de
   Lazar, le processus n'est jamais arrêté.
4. **Interpréteur** : la pièce exige numpy 2.4.6, scipy 1.17.1 et torch 2.14.1 (`requirements-cpu.txt`). Faute d'un `.venv` conforme
   dans ta copie du dépôt, le bloc B2 l'installe là (dossier ignoré par git ; sans cache de pip ; environ 6 Go ; 10 à 20 minutes ; 9 Gio
   libres exigés) :
   la phase C le reprendra tel quel (son bloc C1a cherche d'abord `.venv`), sans seconde installation.
5. **Irréversible** : le nom de la branche (éprouvé par une poussée de la branche égale à `main`, bloc B1) ; l'unique appel de la pièce
   (bloc B5a), précédé du contrôle à blanc (bloc B4), qui joue sans rien écrire les gardes de la pièce d'avant la lecture des entrées.
6. **Ce que la commande évite** : tout passage par ta branche `main` locale (clone partiel, écart P3A-007 de la phase A : la branche
   neuve part de la référence distante) ; tout fichier fermé (`lecture-sondes-t06.json`, `resume.json`, activations, adaptateurs,
   `distillation-t06.json` : jamais extraits, et la pièce les refuse par sa liste blanche) ; toute lecture d'un contenu par toi.

## 1. Interdits permanents

Recopiés du brief du compte 3, section 6 (à recopier en tête de toute consigne de sous-agent ; cette phase n'en crée aucun) :

- Aucune dépense ni machine louée sans ligne de GO inscrite **et** mot de Lazar.
- Aucune valeur de clé : jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ`.
- Jamais `diag/*/lecture-sondes-t06.json`, la lecture B de 7a, `donnees/lecture-b-7a-quarantaine-v1`,
  `donnees/mesure-unanime-v15-sortie-v1`, `essai/t06-explo-v3`, aucun `diag/` ni `runs/` de 7a, l'étiqueteur,
  `scripts/extraire_mesures_epreuve_t06_v1.py`, la branche `calcul/p3bis-reel-v2`.
- Jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, `registres/index-bras-attaque*`,
  `anteriorite-bras-informe*`, ni la branche `claude/compassionate-meitner-d4ryyk`.
- Aucune recherche récursive qui traverse ces chemins : pas de `ls registres`, pas de `ls diag`, pas de `find` ni de `grep -r` larges ;
  fichiers nommés seulement.
- Jamais d'heure écrite à la main (`date -u` dans la même commande). Jamais de `git fetch` sans refspec.
- Garde des secrets à 0 avant chaque commit (variable `SECRETS` du bloc 1B).
- Jamais toucher les instances Vast 58936096, 58936099, 58936100, 60480302, 60541314 ni les serveurs Hetzner `poste-temoin-bailey-*` ;
  aucun appel au loueur.
- Ne jamais contourner, reformuler ni confier à une autre session un refus de permission, du crochet ou d'un classifieur : arrêt, rapport à la mère.
- Rien de publié, aucun contact extérieur (tu rédiges, Lazar envoie).

**Exception unique, accordée par R-2711 (2) et GO-2026-11-16-05** : les cinq fichiers de 7b nommés au bloc B3 (branche
`calcul/t06-confirmation-7b-v1`) sont récupérés dans un dépôt jetable sans contenu, puis extraits par liste positive
(`git show <tête>:<chemin>`) hors de ton dépôt, pour la seule pièce, dont le code est scellé.

**Interdits ajoutés** :

- **Tu n'ouvres ni entrée ni sortie** : tu copies, tu calcules des empreintes et tu compares. Tu ne lis que : les noms, les tailles,
  les compagnons, le code de sortie de la pièce, le nom de son run, les étapes de son progrès (un nom d'étape et une heure, aucune
  valeur) et, sur un code 2 seulement, la ligne de refus que le bloc B5b affiche. Jamais `sortie-piece-v2.txt` ni `progres-piece-v2.txt`
  en entier ; jamais un fichier de `diag/<run de la pièce>/` ; jamais, sur un code 3, le motif de l'arrêt (il est dans le fichier d'arrêt
  scellé, non ouvert).
- **Un seul appel de la pièce** : le fichier `appel-piece-lance-v2.txt` est posé avant l'appel ; s'il existe, le bloc B5a s'arrête.
  Jamais la pièce lancée autrement que par B5a ; jamais un processus arrêté (aucun `kill`).
- Jamais `resume.json`, `lecture-sondes-t06.json`, `distillation-t06.json`, les activations ni les adaptateurs de 7b.
- Rien n'est effacé dans ton dépôt : un fichier non suivi qui gêne la pièce est un arrêt, rapporté à Lazar par son nom.
- Exclusions de cette session : celles de la phase A, inchangées (analyse du verdict A ; étape B bis, conception et verdicts ; T0.8 ;
  G0 ; préenregistrement NARCBench, rédaction, contre-lecture, course ; brouillons des papiers B et C ; code de la pièce « mots et
  coût », écriture et contre-lecture), plus la lecture et l'analyse des sorties de la pièce.
- Aucune poussée hors de `verdict/t06-mots-et-cout-compte-3-v1` ; jamais `main`, `lot/compte-3-v1` ni `lciric/controle-ia`.

## 2. Qui fait quoi

- **Toi, la session hôte (la même que pour la phase A)** : blocs dans l'ordre ; extraction par liste positive, hors du dépôt ; un seul
  appel de la pièce ; commit des seules sorties, poussée ; rendu. Tu n'ouvres ni entrée ni sortie.
- **Aucun lecteur dans cette phase** : la pièce ne rend pas de verdict. Ce qu'elle écrit est lu plus tard, par d'autres que toi : l'état
  de la ligne BA-L2, par la mère, par programme (bloc M de la phase C v3, section 15) ; le fichier d'issue, par le module gelé de T0.7
  à l'étape B (phase C, bloc C4a), puis par le lecteur B, qui le reçoit parmi ses pièces (phase C, bloc C5) ; les autres fichiers, par
  des lecteurs que nommeront des commandes à part.
- **La mère** : section 15. **Elle ne lit de 7b que l'état de BA-L2** (mot de Lazar R-2741, nœud N-C) : elle vérifie les sorties par
  leurs empreintes, sans les ouvrir.
- **Lazar** : colle cette commande, te donne en conversation son chemin et son empreinte, reçoit ton rendu (section 13).

## 3. Marqueurs

| marqueur | qui, quand | où |
|---|---|---|
| chemin et empreinte de la version remise de cette commande | Lazar, en conversation ; le bloc 0b-B imprime l'empreinte, tu compares | bloc 0b-B |
| les deux variables de tête du bloc F-B (épreuve du crochet : bloquée ou passée ; modèle de ta session : A ou C) | toi, à la main (ce que tu as vu ; identité du modèle dite en conversation seulement) | bloc F-B |
| les trois variables de tête du bloc V (base rendue, commit des sorties rendu, lignes rendues par B5b) | la mère, dans son propre bloc | section 15 |

Aucun marqueur de la mère dans les blocs que tu joues. Pour mémoire, les quatre marqueurs du gabarit de la v1 sont remplis ainsi :
`<<COMMIT_PIECE>>` = `da06bb57610f840152e4e9a8c449b036577cc582` ; `<<LIGNE_CODE_MOTS_ET_COUT>>` =
`| CODE-MOTS-ET-COUT-T06 | 2026-11-14T14:55:41Z | registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json | e418fdafbf8362f0458eb0448ec2d32ffa9a8bb122ec619ad0aaf68a9df3b43b |` ;
`<<COMMANDE_PIECE>>` = `PY=<interpréteur du bloc B2> bash scripts/lancer_mots_et_cout_t06_v3.sh --mode reel --racine-entrees <entrées du bloc B3> 20261111-151701-t06-reel`,
depuis la racine de ton dépôt ; `<<MOTIF_RUN_PIECE>>` = `[0-9]{8}-[0-9]{6}-mots-et-cout-t06` (date et heure UTC de l'appel).

## 4. Mode d'emploi

- **Avant ce message**, la mère a poussé cette commande sur `main`.
- Chaque bloc se lance tel quel, dans un seul appel de ton outil de commande, dans l'ordre ; chaque bloc relit
  `$HOME/bac-mots-et-cout-compte-3-v2/variables-v2.sh`. Une ligne « ARRÊT : » : tu t'arrêtes et tu suis la section 14.
- **Relançables** : 0-B, 0b-B, 2B, B1 ; B3 et B4 tant que B5a n'est pas joué ; B2 et B5-attente autant de fois qu'il faut (ce sont
  eux qui attendent : aucun `sleep`) ; B5b et F-B (ils reprennent à la poussée : leurs commits sont gardés au bac). **Jamais
  relancés** : 1B (sauf section 14) et **B5a**.
- Délai maximal de ton outil pour B1, B3 et B5b. Pendant l'installation du bloc B2, tu peux jouer B3, puis rejouer B2.
- **Si l'outil rend la main pendant ou après B5a** : tu ne relances pas B5a ; tu joues B5-attente, puis B5b quand le code est écrit.
- Au-dessus de 80 % de quota, tu ne commences pas B5a.
- Les commentaires « attendu : » disent la sortie conforme ; toute autre sortie est un arrêt.

## 5. Bloc 0-B — aptitude (deux appels séparés) et bloc 0b-B — `main` distant à jour

```bash
sha256sum scripts/lancer_course_ideation_bassins_etroits_v2.py
# attendu : appel BLOQUÉ par le crochet de garde. S'il passe : dis-le en tête de ton premier message à Lazar.
```

```bash
df -Pk "$HOME" . | awk 'NR>1 && !vu[$6]++ {printf "place libre sous %s : %.1f Gio\n", $6, $4/1048576}'; nproc; python3 --version
cd "$(git rev-parse --show-toplevel)" || exit 1
echo "clone superficiel : $(git rev-parse --is-shallow-repository) ; branche courante : $(git rev-parse --abbrev-ref HEAD)"
[ -x .venv/bin/python ] && echo ".venv : présent" || echo ".venv : absent (le bloc B2 l'installera : environ 6 Go, 10 à 20 minutes)"
echo "fichiers non suivis, non ignorés (dix au plus) : $(git status --porcelain --untracked-files=all | grep -c '^??')"
git status --porcelain --untracked-files=all | grep '^??' | cut -c1-160 | head -n 10; date -u +%Y-%m-%dT%H:%M:%SZ
# attendu : au moins 9 Gio libres si .venv est absent (sinon 1 Gio) ; « fichiers non suivis … : 0 ». S'il y en a, dis leurs noms à Lazar
# avant d'aller plus loin : la pièce exige un arbre de travail sans fichier non suivi, et tu n'effaces rien. Dis aussi à Lazar le modèle
# de ta session et ton quota.
```

```bash
cd "$(git rev-parse --show-toplevel)" || exit 1
F=docs/procedures/lecture-7b-etape-b-compte-3-v1/commande-compte-3-phase-b-v3.md
[ -z "$(git status --porcelain --untracked-files=no)" ] || { echo "ARRÊT : modifications suivies dans ton dépôt"; exit 1; }
git fetch --no-tags -q origin +refs/heads/main:refs/remotes/origin/main || { echo "ARRÊT : récupération de main"; exit 1; }
git cat-file -e "refs/remotes/origin/main:$F" 2>/dev/null || { echo "ARRÊT : la commande n'est pas sur main (la mère la pousse d'abord)"; exit 1; }
echo "main distant : $(git rev-parse refs/remotes/origin/main)"
echo "$(git show "refs/remotes/origin/main:$F" | sha256sum | cut -d' ' -f1)  $F (sur main distant)"
# attendu : l'empreinte imprimée est celle que Lazar t'a donnée en conversation (sinon arrêt). Ta copie de travail et ta branche main
# locale ne sont pas touchées.
```

## 6. Bloc 1B — variables (une seule fois)

```bash
export LC_ALL=C.UTF-8
arret() { echo "ARRÊT : $*"; exit 1; }
date -u +"début : %Y-%m-%dT%H:%M:%SZ"
DEPOT=$(git rev-parse --show-toplevel) || arret "lance ce bloc depuis le dossier du dépôt"
case "$(git -C "$DEPOT" remote get-url origin)" in
  *lciric/controle-ia-travail*) echo "dépôt : $DEPOT (lciric/controle-ia-travail)";;
  *) arret "le dépôt d'origine n'est pas lciric/controle-ia-travail";; esac
BAC="$HOME/bac-mots-et-cout-compte-3-v2"                 # hors de tout arbre git ; neuf (R12)
[ ! -e "$BAC" ] || arret "$BAC existe déjà : rapport à la mère"
git -C "$HOME" rev-parse --show-toplevel >/dev/null 2>&1 && arret "$HOME est dans un arbre git"
SESSION_C3="session_${CLAUDE_CODE_REMOTE_SESSION_ID#cse_}"
[[ "$SESSION_C3" =~ ^session_[0-9A-Za-z]{10,}$ ]] || arret "identifiant de session introuvable (section 14)"
SESSION_HOTE=session_016QhUrrSUMEzEqWPnQYxjHB
[ "$SESSION_C3" = "$SESSION_HOTE" ] || arret "cette session ($SESSION_C3) n'est pas la session hôte de la phase A : rien n'est lancé ; la mère tranche (version nouvelle de la commande)"
mkdir -p "$BAC" && date -u +%Y-%m-%dT%H:%M:%SZ > "$BAC/debut-v2.txt"
cat > "$BAC/variables-v2.sh" <<EOF
export LC_ALL=C.UTF-8 PYTHONDONTWRITEBYTECODE=1
arret() { echo "ARRÊT : \$*"; exit 1; }
DEPOT='$DEPOT'; BAC='$BAC'; SESSION_C3='$SESSION_C3'
R6=20261111-151701-t06-reel; B7B=calcul/t06-confirmation-7b-v1; TETE_7B=55c3e3eb89a4650419f35999aaa4c54288275b0d
BR_P=verdict/t06-mots-et-cout-compte-3-v1; DEPOT_URL=https://github.com/lciric/controle-ia-travail.git
COMMIT_PIECE=da06bb57610f840152e4e9a8c449b036577cc582
LIGNE_CODE='| CODE-MOTS-ET-COUT-T06 | 2026-11-14T14:55:41Z | registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json | e418fdafbf8362f0458eb0448ec2d32ffa9a8bb122ec619ad0aaf68a9df3b43b |'
LIGNE_RUN6='| RUN-CONFIRMATION-T06 | 2026-11-13T18:52:43Z | runs/20261111-151701-t06-reel/manifeste.json | 7e1ac1f02584e4f8babf664e78d12f3122bfdca18292734f28281e9459479bf6 |'
LIGNE_BASE_A='| SCELLEMENT-T08-BASE-A | 2026-11-10T12:21:55Z | prereg/T0.8-base-A-mots-et-cout-v1.md | 72b067d5b3f8c0d7f257677dbc86ace6cd1917b07f7a96e2263b91647dc6205d |'
H_MANIF_7B=7e1ac1f02584e4f8babf664e78d12f3122bfdca18292734f28281e9459479bf6
H_PIECE=9dbcc55ca47b21674636f5d6c9126af15244d5ee63a9df8dee274df126c4e674; H_LANCEUR=e1d2514cd6361f8201a6773a4cf108ac333aa7ca647807698b90c3abeb97a7c5
H_FICHE_CODE=e418fdafbf8362f0458eb0448ec2d32ffa9a8bb122ec619ad0aaf68a9df3b43b; FICHE_CODE=registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json
H_BASE_A=72b067d5b3f8c0d7f257677dbc86ace6cd1917b07f7a96e2263b91647dc6205d; H_T06=ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169
H_ATTESTATION3=a20f137c92022c58fd8090a2c1e25d8c575fec1b0e8a15d2190a1b1bae505a62
LISTE=registres/qui-a-lu-quoi-v2.md; EMPREINTE_LISTE=315fb4b3ab7132f1b85e9b1b816384d3637dae0b9c261858ab9c6558f5b4eff0
CELLULE_HOTE='analyse du verdict A ; étape B bis (conception et verdicts) ; T0.8 ; G0 ; préenregistrement NARCBench (rédaction, contre-lecture, course) ; brouillons des papiers B et C ; code de la pièce « mots et coût »'
MOTIF_RUN='^[0-9]{8}-[0-9]{6}-mots-et-cout-t06\$'; BORNE_S=3600; PLACE_MIN_KIO=9437184
ENTREES="\$BAC/entrees-7b-v2"; CLONE7B="\$BAC/clone-7b-v2"
SECRETS='(sk-ant-[A-Za-z0-9]|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|hf_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{12}|AIza[0-9A-Za-z_-]{20,})'
INTERDITS_NOMS='lecture-sondes|resume\.json|activations|adaptateur|distillation|bras-attaque|mode-tenu|etiqueteur|quarantaine|mesure-unanime|t07|t0\.7|bbis|b-bis'
EOF
echo "session : $SESSION_C3 ; variables : $BAC/variables-v2.sh"
# attendu : dépôt ; session « session_016QhUrrSUMEzEqWPnQYxjHB » ; aucun « ARRÊT »
```

## 7. Bloc 2B — contrôles d'entrée, attestation

```bash
. "$HOME/bac-mots-et-cout-compte-3-v2/variables-v2.sh" || exit 1
date -u +%Y-%m-%dT%H:%M:%SZ
D=$(curl -sS --max-time 20 -D - -o /dev/null https://pypi.org/simple/numpy/ 2>/dev/null | tr -d '\r' | awk -F': ' 'tolower($1)=="date"{print $2}' | tail -1)
[ -n "$D" ] || arret "horloge de référence (en-tête Date de pypi.org) injoignable"
E=$(( $(date -u +%s) - $(date -u -d "$D" +%s) )); echo "écart de l'horloge à pypi.org : $E s"; [ "${E#-}" -le 120 ] || arret "horloge décalée de plus de 120 s"
cd "$DEPOT"; M=refs/remotes/origin/main; P="$BAC/pieces-main-v2"; A=attestation_qui_a_lu_quoi_compte_3_v3.py
mkdir -p "$P/$(dirname "$LISTE")"
git show "$M:docs/procedures/lecture-7b-etape-b-compte-3-v1/$A" > "$P/$A" || arret "attestation v3 absente de main"
[ "$(sha256sum "$P/$A" | cut -d' ' -f1)" = "$H_ATTESTATION3" ] && echo "attestation v3 : pièce conforme" || arret "pièce de l'attestation"
for f in "$LISTE" "$LISTE.sha256"; do git show "$M:$f" > "$P/$f" || arret "liste « qui a lu quoi » absente de main : $f"; done
python3 -I -B "$P/$A" "$P/$LISTE" "$EMPREINTE_LISTE" "$SESSION_C3" --admettre-hote "$CELLULE_HOTE" \
    || arret "attestation « qui a lu quoi » non conforme : rien n'est lancé ; la mère tranche"
[ -z "$(git branch --list 'lot/compte-3-v1')" ] || arret "branche locale lot/compte-3-v1 : session du lot ? la mère tranche"
[ -n "$(git config user.name)" ] && [ -n "$(git config user.email)" ] || arret "identité git (user.name, user.email) absente"
[ -z "$(git status --porcelain --untracked-files=no)" ] || arret "modifications suivies dans ton dépôt"
echo "contrôles d'entrée conformes"
# attendu : écart ≤ 120 s ; « attestation v3 : pièce conforme » ; « ATTESTATION : CONFORME — … lignes de l'hôte admises : 0 » (ou 1) ;
# « contrôles d'entrée conformes » ; aucun « ARRÊT ». La liste et l'attestation sont lues sur main distant, dans le bac.
```

## 8. Phase B — la course de la pièce

### Bloc B1 — historique, branche neuve, lignes du registre, pièces de `main`, poussée éprouvée (délai maximal)

```bash
. "$HOME/bac-mots-et-cout-compte-3-v2/variables-v2.sh" || exit 1
cd "$DEPOT"; M=refs/remotes/origin/main
S=$(git status --porcelain --untracked-files=all)
[ -z "$S" ] || { printf '%s\n' "$S" | cut -c1-160 | head -n 10; arret "arbre de travail non propre, fichiers non suivis compris (dix lignes au plus ci-dessus) : la pièce refuserait ; rien n'est effacé ; rapport à Lazar"; }
# la pièce exige son commit cité présent et ancêtre de la tête : un clone superficiel est approfondi, par refspec explicite
if [ "$(git rev-parse --is-shallow-repository)" = true ] \
   && ! { git cat-file -e "$COMMIT_PIECE^{commit}" 2>/dev/null && git merge-base --is-ancestor "$COMMIT_PIECE" "$M" 2>/dev/null; }; then
    git fetch --no-tags -q --unshallow origin +refs/heads/main:refs/remotes/origin/main || arret "approfondissement de l'historique (relance ce bloc)"
    echo "clone superficiel : historique de main approfondi"
fi
git cat-file -e "$COMMIT_PIECE^{commit}" 2>/dev/null || arret "commit de la pièce $COMMIT_PIECE absent de ton dépôt : rapport à la mère"
git merge-base --is-ancestor "$COMMIT_PIECE" "$M" || arret "le commit de la pièce n'est pas un ancêtre de main : rapport à la mère"
D=$(git ls-remote origin "refs/heads/$BR_P" | cut -f1)
[ -z "$D" ] || { [ -e "$BAC/c-main-p-v2.txt" ] && [ "$D" = "$(cat "$BAC/c-main-p-v2.txt")" ]; } || arret "la branche $BR_P existe déjà au distant (R12) : rapport à la mère"
if [ "$(git rev-parse --abbrev-ref HEAD)" = "$BR_P" ] && [ -e "$BAC/c-main-p-v2.txt" ]; then echo "branche $BR_P déjà créée (bloc relancé)"
else git switch -q --no-track -c "$BR_P" "$M" || arret "création de $BR_P"; git rev-parse HEAD > "$BAC/c-main-p-v2.txt"; fi
[ "$(git rev-parse HEAD)" = "$(cat "$BAC/c-main-p-v2.txt")" ] || arret "la tête de $BR_P n'est plus sa base : rapport à la mère"
R=registres/scellements-v1.md
for L in "$LIGNE_BASE_A" "$LIGNE_RUN6" "$LIGNE_CODE"; do k=$(printf '%s' "$L" | cut -d'|' -f2 | tr -d ' ')
    [ "$(grep -cxF -- "$L" "$R")" = 1 ] && [ "$(grep -c "^| $k |" "$R")" = 1 ] && echo "conforme : ligne $k" || arret "ligne $k absente, autre ou en double dans $R"; done
for k in LECTURE-T08-BASE-A ISSUE-MOTS-ET-COUT-T06; do
    [ "$(grep -c "^| $k |" "$R")" = 0 ] && echo "conforme : aucune ligne $k" || arret "ligne $k déjà inscrite : la pièce a déjà tourné (R12) : nœud"; done
sha256sum -c --quiet <<FIN && echo "conforme : cinq pièces de main à leurs empreintes" || arret "pièces de main"
$H_PIECE  scripts/mots_et_cout_t06_v3.py
$H_LANCEUR  scripts/lancer_mots_et_cout_t06_v3.sh
$H_FICHE_CODE  $FICHE_CODE
$H_BASE_A  prereg/T0.8-base-A-mots-et-cout-v1.md
$H_T06  prereg/T0.6-organismes-v0-v1.md
FIN
for f in "$FICHE_CODE" prereg/T0.8-base-A-mots-et-cout-v1.md prereg/T0.6-organismes-v0-v1.md; do
    [ "$(cut -d' ' -f1 "$f.sha256")" = "$(sha256sum "$f" | cut -d' ' -f1)" ] || arret "compagnon de $f"; done
[ "$(git show "$COMMIT_PIECE:scripts/mots_et_cout_t06_v3.py" | sha256sum | cut -d' ' -f1)" = "$H_PIECE" ] \
    && [ "$(git show "$COMMIT_PIECE:scripts/lancer_mots_et_cout_t06_v3.sh" | sha256sum | cut -d' ' -f1)" = "$H_LANCEUR" ] \
    && echo "conforme : la pièce et son lanceur, au commit cité, à leurs empreintes" || arret "pièce ou lanceur au commit cité"
(cd docs && sha256sum -c --quiet sha256sums-lancement-v2.txt) && echo "empreintes de lancement conformes" || arret "empreintes de lancement"
for d in diag/[0-9]*-mots-et-cout-t06 runs/[0-9]*-mots-et-cout-t06; do [ ! -e "$d" ] || arret "$d existe déjà (R12) : rapport à la mère"; done
git push -q origin "refs/heads/$BR_P:refs/heads/$BR_P" && echo "branche $BR_P poussée (égale à main : $(git ls-remote origin "refs/heads/$BR_P" | cut -c1-12))" \
    || arret "poussée refusée : rapport à la mère"
# attendu : (« clone superficiel : historique de main approfondi », si ton clone l'est) ; cinq « conforme : ligne … » ou « aucune ligne … » ;
# « cinq pièces de main » ; « la pièce et son lanceur, au commit cité » ; « empreintes de lancement conformes » ; « branche … poussée » ;
# aucun « ARRÊT »
```

### Bloc B2 — interpréteur de la pièce (à rejouer jusqu'à la ligne « interpréteur de la pièce : … »)

```bash
. "$HOME/bac-mots-et-cout-compte-3-v2/variables-v2.sh" || exit 1
cd "$DEPOT"; [ "$(git rev-parse --abbrev-ref HEAD)" = "$BR_P" ] || arret "tu n'es pas sur $BR_P"
VERS='import numpy, scipy, torch, sys; v=(numpy.__version__, scipy.__version__, torch.__version__.split("+")[0]); print("versions :", *v); sys.exit(0 if v == ("2.4.6", "1.17.1", "2.14.1") else 1)'
V="$DEPOT/.venv"; L="$BAC/installation-v2"
if [ ! -e "$L.lancee.txt" ]; then          # aucune installation lancée par cette commande
    if [ -x "$V/bin/python" ] && "$V/bin/python" -c "$VERS" >/dev/null 2>&1; then echo "environnement déjà prêt : $V"
    else
        [ ! -e "$V" ] || arret "$V existe avec d'autres versions (non créé par cette commande) : rien n'est écrasé ; rapport à la mère"
        K=$(df -Pk "$DEPOT" | awk 'NR==2{print $4}'); [ "$K" -ge "$PLACE_MIN_KIO" ] || arret "place libre $K Kio < $PLACE_MIN_KIO Kio : rapport à la mère"
        command -v setsid >/dev/null && command -v nohup >/dev/null || arret "setsid ou nohup absent : rapport à la mère"
        date -u +%s > "$L.lancee.txt"
        setsid nohup bash -c 'echo $$ > "$4.pid.txt"; { python3 -m venv "$1" && "$1/bin/pip" install -q --disable-pip-version-check --no-cache-dir -r "$2"; } > "$3" 2>&1; echo $? > "$4.code.tmp" && mv "$4.code.tmp" "$4.code.txt"' \
            _ "$V" "$DEPOT/requirements-cpu.txt" "$L.journal.txt" "$L" > /dev/null 2>&1 < /dev/null &
        date -u +"installation lancée, détachée, à %Y-%m-%dT%H:%M:%SZ : rejoue ce bloc dans quelques minutes (tu peux jouer B3 en attendant)"; exit 0
    fi
elif [ ! -e "$L.code.txt" ]; then
    D=$(( $(date -u +%s) - $(cat "$L.lancee.txt") )); P=$(cat "$L.pid.txt" 2>/dev/null); E=$(awk '/^State:/{print $2}' "/proc/${P:-0}/status" 2>/dev/null)
    if { [ -n "$E" ] && [ "$E" != Z ]; } || { [ -z "$P" ] && [ "$D" -lt 15 ]; }; then echo "installation en cours depuis $D s ($(du -sh "$V" 2>/dev/null | cut -f1) écrits) : rejoue ce bloc dans quelques minutes"; exit 0
    else arret "installation : processus disparu sans code de sortie après $D s ; rien n'est effacé ; rapport à la mère"; fi
else
    [ "$(cat "$L.code.txt")" = 0 ] || { tail -n 5 "$L.journal.txt"; arret "installation en échec (code $(cat "$L.code.txt")) ; rien n'est effacé ; rapport à la mère"; }
    echo "installation finie (code 0) en $(( $(stat -c %Y "$L.code.txt") - $(cat "$L.lancee.txt") )) s"
fi
"$V/bin/python" -c "$VERS" || arret "versions autres que celles de requirements-cpu.txt (2.4.6, 1.17.1, 2.14.1) : rapport à la mère"
PYTHONPATH="$DEPOT/src" "$V/bin/python" -P -B -c 'import controle_ia.t06.test_croise, controle_ia.t06.cout, controle_ia.t06.lanceur, controle_ia.sondes.evaluation, controle_ia.harnais.run_harnais_factice, controle_ia.environnements.propositions, controle_ia.manifeste, controle_ia.scellement, controle_ia.gardes; print("modules gelés de la pièce : importables")' \
    || arret "import des modules gelés de la pièce : rapport à la mère"
grep -q '^PYP=' "$BAC/variables-v2.sh" || echo "PYP='$V/bin/python'" >> "$BAC/variables-v2.sh"
echo "interpréteur de la pièce : $V/bin/python"
# attendu, à la fin : « versions : 2.4.6 1.17.1 2.14.1 » ; « modules gelés de la pièce : importables » ; « interpréteur de la pièce : … ».
# Avant : « installation lancée … » puis « installation en cours … » (rejoue le bloc ; rien d'autre à faire). Tout « ARRÊT » : section 14.
```

### Bloc B3 — entrées de 7b : dépôt jetable, extraction par liste positive, hors du dépôt (délai maximal ; relançable)

```bash
. "$HOME/bac-mots-et-cout-compte-3-v2/variables-v2.sh" || exit 1
[ ! -e "$BAC/appel-piece-lance-v2.txt" ] || arret "la pièce a déjà été lancée : les entrées ne se touchent plus"
[ "$(git ls-remote "$DEPOT_URL" "refs/heads/$B7B" | cut -f1)" = "$TETE_7B" ] || arret "tête de $B7B autre que $TETE_7B : rapport à la mère"
[ -e "$CLONE7B" ] || git clone -q --filter=blob:none --no-checkout --depth 1 --single-branch --branch "$B7B" "$DEPOT_URL" "$CLONE7B" || arret "dépôt jetable sans contenu"
[ "$(git -C "$CLONE7B" rev-parse HEAD)" = "$TETE_7B" ] || arret "tête du dépôt jetable"
[ "$(git -C "$CLONE7B" ls-tree --name-only "$TETE_7B" "diag/$R6/arret.json" | grep -c .)" = 0 ] \
    || arret "diag/$R6/arret.json présent sur la branche de 7b (course arrêtée) : rien n'est placé ; nœud"
git -C "$BAC" rev-parse --show-toplevel >/dev/null 2>&1 && arret "$BAC est dans un arbre git : les entrées n'y sont pas placées"
place() {   # $1 chemin : copie à l'octet sous $ENTREES ; un fichier déjà là n'est admis que s'il est égal au blob
    if [ -e "$ENTREES/$1" ]; then git -C "$CLONE7B" show "$TETE_7B:$1" | cmp -s - "$ENTREES/$1" && { echo "déjà là, égal : $1"; return 0; } || arret "$1 existe et diffère du blob"; fi
    mkdir -p "$ENTREES/$(dirname "$1")"; git -C "$CLONE7B" show "$TETE_7B:$1" > "$ENTREES/$1.partiel" && mv "$ENTREES/$1.partiel" "$ENTREES/$1" || arret "extraction de $1"; }
for f in runs/$R6/manifeste.json diag/$R6/episodes-t06.json diag/$R6/lecture-cout-t06.json donnees/$R6/mesures-t06.npz donnees/$R6/textes-actions-t06.jsonl; do
    place "$f"; place "$f.sha256"; (cd "$ENTREES/$(dirname "$f")" && sha256sum -c --quiet "$(basename "$f").sha256") || arret "compagnon de $f"; done
[ "$(sha256sum "$ENTREES/runs/$R6/manifeste.json" | cut -d' ' -f1)" = "$H_MANIF_7B" ] && echo "manifeste de 7b égal à la ligne RUN-CONFIRMATION-T06" || arret "manifeste de 7b autre que la ligne"
n=$(cd "$ENTREES" && find . -type f | grep -c -i -E "$INTERDITS_NOMS"); [ "$n" = 0 ] || arret "$n nom(s) interdit(s) parmi les entrées : rapport à la mère"
n=$(cd "$ENTREES" && find . -type f | wc -l); [ "$n" = 10 ] || arret "$n fichiers sous $ENTREES, dix attendus (cinq entrées et leurs compagnons) : rapport à la mère"
o=0; for f in runs/$R6/manifeste.json diag/$R6/episodes-t06.json diag/$R6/lecture-cout-t06.json donnees/$R6/mesures-t06.npz donnees/$R6/textes-actions-t06.jsonl; do
    o=$(( o + $(stat -c %s "$ENTREES/$f") )); done
echo "entrées placées hors du dépôt : $n fichiers ; cinq entrées : $o octets ; aucun nom interdit ; aucun ouvert"
# attendu : compagnons « OK » (silencieux) ; « manifeste de 7b égal … » ; « 10 fichiers ; cinq entrées : 18959392 octets » (somme des
# tailles lues au distant à la tête 55c3e3eb, prealables-v1.md, P1.4 : 8 509, 1 556 085, 125 598, 1 830 726 et 15 438 474 octets) ;
# aucun « ARRÊT ». Une autre somme n'arrête pas (les empreintes font foi) : dis-la à Lazar en une ligne. Relancé : dix « déjà là, égal ».
```

### Bloc B4 — contrôle à blanc : les gardes de la pièce, sans rien écrire ni lire des entrées (relançable)

```bash
. "$HOME/bac-mots-et-cout-compte-3-v2/variables-v2.sh" || exit 1
[ ! -e "$BAC/appel-piece-lance-v2.txt" ] || arret "la pièce a déjà été lancée : joue B5-attente"
cd "$DEPOT"; [ "$(git rev-parse --abbrev-ref HEAD)" = "$BR_P" ] || arret "tu n'es pas sur $BR_P"
[ -n "${PYP:-}" ] && [ -x "$PYP" ] || arret "bloc B2 non fini : pas d'interpréteur"
rm -f "$BAC/blanc-conforme-v2.txt"
S=$(git status --porcelain --untracked-files=all)
[ -z "$S" ] || { printf '%s\n' "$S" | cut -c1-160 | head -n 10; arret "arbre de travail non propre, fichiers non suivis compris (dix lignes au plus ci-dessus) : la pièce refuserait ; rien n'est effacé ; rapport à Lazar"; }
for d in diag/[0-9]*-mots-et-cout-t06 runs/[0-9]*-mots-et-cout-t06; do [ ! -e "$d" ] || arret "$d existe déjà (R12) : rapport à la mère"; done
PYTHONPATH="$DEPOT/src" "$PYP" -P -B scripts/mots_et_cout_t06_v3.py verifier-code > "$BAC/verifier-code-v2.txt" 2>&1 \
    || { tail -n 2 "$BAC/verifier-code-v2.txt" | cut -c1-400; arret "verifier-code de la pièce : non conforme ; aucun appel"; }
grep -q -x -F "CODE-MOTS-ET-COUT-T06 conforme : commit $COMMIT_PIECE, 2 fichiers, tête $(git rev-parse HEAD)" "$BAC/verifier-code-v2.txt" \
    && cat "$BAC/verifier-code-v2.txt" || arret "verifier-code de la pièce : sortie autre qu'attendue ; aucun appel"
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONPATH="$DEPOT/src" "$PYP" -P -B - "$DEPOT" "$ENTREES" "$R6" <<'FIN' || arret "contrôle à blanc de la pièce non conforme : aucun appel ; la mère lève la cause"
import importlib.util, os, sys
from pathlib import Path

racine, entrees, run = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve(), sys.argv[3]
try:   # les gardes de `executer`, dans son ordre, jusqu'à la lecture des entrées exclue ; rien n'est écrit, aucun contenu de 7b n'est lu
    spec = importlib.util.spec_from_file_location("mots_et_cout_t06_v3", racine / "scripts" / "mots_et_cout_t06_v3.py")
    mc = importlib.util.module_from_spec(spec); sys.modules[spec.name] = mc; spec.loader.exec_module(mc)
    from controle_ia.prereg import exiger_prereg_scelle
    paquet = mc.paquet_controle_ia()
    if paquet != (racine / "src" / "controle_ia").resolve():
        raise RuntimeError(f"paquet controle_ia importé de {paquet}, hors du dépôt")
    geles = mc.verifier_modules_geles(paquet); mc.charger_modules_geles(paquet)
    print(f"1. modules gelés : {len(geles)} à leurs empreintes, importés du dépôt")
    for texte in (mc.TEXTE_BASE_A, mc.TEXTE_T06):
        mc.verifier_texte(racine, *texte)
    exiger_prereg_scelle(racine / mc.TEXTE_BASE_A[0])
    print("2. textes scellés : base (A) et T0.6 à leurs empreintes ; préenregistrement de la base (A) conforme")
    reg = mc.controler_registre_reel(racine, entrees, racine / mc.REGISTRE_DEFAUT, run, mc.maintenant_utc())
    print(f"3. registre : SCELLEMENT-T08-BASE-A, RUN-CONFIRMATION-T06 et CODE-MOTS-ET-COUT-T06 conformes (commit {reg['code']['commit']}) ; "
          f"ni LECTURE-T08-BASE-A ni ISSUE-MOTS-ET-COUT-T06 ; journal : {reg['journal']['lignes']} ligne(s), aucune ouverture des sondes de T0.6 "
          "ni de l'étape B de T0.7")
    liste = mc.ListeBlanche.pour_7b(entrees, run)
    for rel in liste.relatifs():
        if not rel.endswith(".sha256"):
            mc.compagnon_conforme(entrees / rel)
    if (entrees / "diag" / run / "arret.json").exists():
        raise RuntimeError("arret.json de 7b présent parmi les entrées")
    print(f"4. entrées : les {len(liste.relatifs())} chemins de la liste blanche présents, compagnons égaux (empreintes seules, aucun contenu lu)")
    arbre = mc.exiger_arbre(racine, set())
    if not arbre["propre"]:
        raise RuntimeError("arbre de travail non propre")
    print(f"5. arbre de travail : propre ; commit {arbre['commit']}")
    if [os.environ.get(k) for k in mc.FILS_BLAS] != ["1", "1", "1"]:
        raise RuntimeError("fils de calcul non fixés à 1")
except Exception as e:   # garde de la pièce (GardeArret) ou toute autre erreur : même issue, aucun appel
    print(f"NON CONFORME ({type(e).__name__}) : {e}")
    sys.exit(2)
print("CONTRÔLE À BLANC DE LA PIÈCE : TOUT CONFORME")
FIN
date -u +%s > "$BAC/blanc-conforme-v2.txt"
# attendu : la ligne « CODE-MOTS-ET-COUT-T06 conforme : commit da06bb57…, 2 fichiers, tête <ta tête> » ; cinq lignes numérotées (1. neuf
# modules gelés ; 2. textes ; 3. registre, journal de 2 lignes au 16 novembre ; 4. dix chemins ; 5. arbre propre) ; « CONTRÔLE À BLANC DE LA PIÈCE :
# TOUT CONFORME ». Toute ligne « NON CONFORME : … » : aucun appel ; section 14. Ce contrôle ne voit pas le contenu des entrées : la pièce
# seule le lit (un refus à sa lecture reste possible : code 2, rien d'écrit).
```

### Bloc B5a — l'unique appel de la pièce, détaché (jamais relancé)

```bash
. "$HOME/bac-mots-et-cout-compte-3-v2/variables-v2.sh" || exit 1
[ ! -e "$BAC/appel-piece-lance-v2.txt" ] || arret "la pièce a déjà été lancée : aucun second appel ; joue B5-attente, puis B5b"
cd "$DEPOT"; [ "$(git rev-parse --abbrev-ref HEAD)" = "$BR_P" ] || arret "tu n'es pas sur $BR_P"
[ -e "$BAC/blanc-conforme-v2.txt" ] || arret "bloc B4 non conforme ou non joué : aucun appel"
[ $(( $(date -u +%s) - $(cat "$BAC/blanc-conforme-v2.txt") )) -le 1800 ] || arret "contrôle à blanc vieux de plus de 30 minutes : rejoue B4"
[ -z "$(git status --porcelain --untracked-files=all)" ] || arret "arbre de travail non propre depuis B4 : rejoue B4"
[ "$(git rev-parse HEAD)" = "$(cat "$BAC/c-main-p-v2.txt")" ] || arret "la tête de $BR_P n'est plus sa base : rapport à la mère"
command -v setsid >/dev/null && command -v nohup >/dev/null || arret "setsid ou nohup absent : rapport à la mère"
date -u +%s > "$BAC/appel-piece-lance-v2.txt"          # posé AVANT l'appel : aucun second appel possible
setsid nohup bash -c 'echo $$ > "$7"; cd "$1" && PY="$2" bash scripts/lancer_mots_et_cout_t06_v3.sh --mode reel --racine-entrees "$3" "$4" > "$5" 2> "$6"; echo $? > "$8.tmp" && mv "$8.tmp" "$8"' \
    _ "$DEPOT" "$PYP" "$ENTREES" "$R6" "$BAC/sortie-piece-v2.txt" "$BAC/progres-piece-v2.txt" "$BAC/pid-piece-v2.txt" "$BAC/code-piece-v2.txt" > /dev/null 2>&1 < /dev/null &
date -u +"pièce lancée, détachée, à %Y-%m-%dT%H:%M:%SZ ; joue maintenant B5-attente"
# attendu : « pièce lancée, détachée, à … ». La sortie et le progrès de la pièce restent dans le bac, jamais affichés.
```

### Bloc B5-attente — relevé court (à rejouer jusqu'à « PIÈCE FINIE »)

```bash
. "$HOME/bac-mots-et-cout-compte-3-v2/variables-v2.sh" || exit 1
[ -e "$BAC/appel-piece-lance-v2.txt" ] || arret "B5a non joué"
T0=$(cat "$BAC/appel-piece-lance-v2.txt"); D=$(( $(date -u +%s) - T0 ))
ETAPE=$(grep '^PROGRES ' "$BAC/progres-piece-v2.txt" 2>/dev/null | tail -n 1 | sed 's/^.* etape=//')
if [ -e "$BAC/code-piece-v2.txt" ]; then
    echo "PIÈCE FINIE : code $(cat "$BAC/code-piece-v2.txt") en $(( $(stat -c %Y "$BAC/code-piece-v2.txt") - T0 )) s ; joue B5b"
else
    P=$(cat "$BAC/pid-piece-v2.txt" 2>/dev/null); E=$(awk '/^State:/{print $2}' "/proc/${P:-0}/status" 2>/dev/null)
    if { [ -n "$E" ] && [ "$E" != Z ]; } || { [ -z "$P" ] && [ "$D" -lt 15 ]; }; then
        echo "pièce en cours depuis $D s (dernière étape : ${ETAPE:-aucune}) ; rejoue ce bloc dans une minute"
        [ "$D" -le "$BORNE_S" ] || echo "BORNE DÉPASSÉE ($BORNE_S s) : rapport à la mère, nœud de Lazar ; le processus n'est pas arrêté"
    else
        echo "ARRÊT : processus disparu sans code de sortie après $D s (dernière étape : ${ETAPE:-aucune}) ; dossiers écrits :" \
             "$(cd "$DEPOT" && for d in diag/[0-9]*-mots-et-cout-t06 runs/[0-9]*-mots-et-cout-t06; do [ -e "$d" ] && printf '%s ' "$d"; done) ; rien n'est relancé ni effacé ; nœud"
        exit 1
    fi
fi
# attendu : « pièce en cours … » (étapes : modules gelés, textes et registre, entrées, manifeste, doses (bases A et B), contrôles de la
# base (A), coût brut seul, taux, règle, écriture), puis « PIÈCE FINIE : code 0 en … s ; joue B5b »
```

### Bloc B5b — sorties vérifiées par empreinte, commitées et poussées, sans être ouvertes (délai maximal ; relançable seul)

```bash
. "$HOME/bac-mots-et-cout-compte-3-v2/variables-v2.sh" || exit 1
[ -e "$BAC/code-piece-v2.txt" ] || arret "pièce pas finie (B5-attente)"
CODE=$(cat "$BAC/code-piece-v2.txt"); cd "$DEPOT"; [ "$(git rev-parse --abbrev-ref HEAD)" = "$BR_P" ] || arret "tu n'es pas sur $BR_P"
ETAPE=$(grep '^PROGRES ' "$BAC/progres-piece-v2.txt" 2>/dev/null | tail -n 1 | sed 's/^.* etape=//')
echo "code de la pièce : $CODE ; dernière étape : ${ETAPE:-aucune} ; durée : $(( $(stat -c %Y "$BAC/code-piece-v2.txt") - $(cat "$BAC/appel-piece-lance-v2.txt") )) s"
RMC=$(for d in diag/[0-9]*-mots-et-cout-t06 runs/[0-9]*-mots-et-cout-t06; do [ -e "$d" ] && basename "$d"; done | sort -u)
case "$CODE" in
  0|3) [ "$(printf '%s\n' "$RMC" | grep -c .)" = 1 ] && [ "$(printf '%s\n' "$RMC" | grep -c -E "$MOTIF_RUN")" = 1 ] && [ -d "diag/$RMC" ] && [ -d "runs/$RMC" ] \
           || arret "run de la pièce introuvable, multiple ou incomplet sous diag/ et runs/ : rien n'est commité ni effacé ; nœud" ;;
  2)   [ -z "$RMC" ] || arret "code 2 avec des fichiers écrits ($(printf '%s' "$RMC" | tr '\n' ' ')) : rien n'est commité ni effacé ; nœud"
       echo "refus avant le manifeste : rien n'est écrit (R11). Ligne de refus, pour Lazar (section 13) :"; grep -m 1 '^REFUS' "$BAC/progres-piece-v2.txt" | cut -c1-600
       [ -e "$BAC/c-sorties-p-v2.txt" ] || echo "aucune sortie (code 2)" > "$BAC/c-sorties-p-v2.txt"
       echo "B5b fait : code 2 ; rien à commiter ; joue F-B, puis rends à Lazar ; aucune relance de la pièce"; exit 0 ;;
  *)   arret "code inattendu $CODE : rien n'est commité ni effacé ; dossiers : $(printf '%s' "$RMC" | tr '\n' ' ') ; nœud" ;;
esac
if [ "$CODE" = 0 ]; then
    [ "$(ls -1A "diag/$RMC" | sort | tr '\n' ' ')" = "base-a-t08.json base-a-t08.json.sha256 issue-mots-et-cout-t06.json issue-mots-et-cout-t06.json.sha256 mots-et-cout-t06-details.json mots-et-cout-t06-details.json.sha256 " ] \
        || arret "diag/$RMC : noms autres que les six attendus (code 0) : rien n'est commité ; nœud"
else
    n=$(ls -1A "diag/$RMC" | grep -v -c -x -E '(arret-mots-et-cout-t06|mots-et-cout-t06-details|base-a-t08|issue-mots-et-cout-t06)\.json(\.sha256)?')
    [ "$n" = 0 ] && [ -f "diag/$RMC/arret-mots-et-cout-t06.json" ] || arret "diag/$RMC : noms autres qu'attendus, ou fichier d'arrêt absent (code 3) : rien n'est commité ; nœud"
fi
[ "$(ls -1A "runs/$RMC" | sort | tr '\n' ' ')" = "manifeste.json manifeste.json.sha256 " ] || arret "runs/$RMC : noms autres que le manifeste et son compagnon : rien n'est commité ; nœud"
for f in $(ls -1A "diag/$RMC" | grep -v '\.sha256$'); do (cd "diag/$RMC" && sha256sum -c --quiet "$f.sha256") || arret "compagnon de diag/$RMC/$f : rien n'est commité ; nœud"; done
(cd "runs/$RMC" && sha256sum -c --quiet manifeste.json.sha256) || arret "compagnon du manifeste de la pièce : rien n'est commité ; nœud"
if [ "$CODE" = 0 ]; then
    A=$(grep -E "^(diag|runs)/$RMC/[a-z0-9.-]+ [0-9a-f]{64}\$" "$BAC/sortie-piece-v2.txt")
    [ "$(grep -c -F "PIÈCE MOTS ET COÛT (reel) : run $RMC ; " "$BAC/sortie-piece-v2.txt")" = 1 ] && [ "$(printf '%s\n' "$A" | grep -c .)" = 4 ] \
        || arret "la sortie de la pièce n'annonce pas le run $RMC et ses quatre fichiers : rien n'est commité ; nœud"
    printf '%s\n' "$A" | while read -r p s; do [ "$(sha256sum "$p" 2>/dev/null | cut -d' ' -f1)" = "$s" ] || exit 1; done \
        && echo "les quatre fichiers écrits sont égaux aux empreintes annoncées par la pièce" || arret "fichier écrit autre que l'empreinte annoncée par la pièce : rien n'est commité ; nœud"
    n=$(( $(wc -l < "$BAC/sortie-piece-v2.txt") - 5 )); [ "$n" = 0 ] || echo "note : $n ligne(s) de plus que les cinq attendues dans la sortie de la pièce (non affichées) : dis-le à Lazar"
fi
if [ ! -e "$BAC/c-sorties-p-v2.txt" ]; then
    [ "$(git rev-parse HEAD)" = "$(cat "$BAC/c-main-p-v2.txt")" ] || arret "la tête de $BR_P n'est plus sa base : rien n'est commité ; rapport à la mère"
    n=$(git status --porcelain --untracked-files=all | grep -v -c -E "^.. (diag|runs)/$RMC/"); [ "$n" = 0 ] || arret "autre chose que les sorties de la pièce dans l'arbre de travail ($n entrée(s)) : rien n'est commité ; rapport"
    git add -- "diag/$RMC" "runs/$RMC"
    git diff --cached --name-only | grep -v -E "^(diag|runs)/$RMC/[a-z0-9.-]+$" && arret "index : autre chose que les sorties de la pièce"
    n=$(git diff --cached | grep -cE "$SECRETS"); [ "$n" = 0 ] || arret "garde des secrets : $n"
    git commit -q -m "T0.6, pièce « mots et coût » sur 7b : sorties scellées de la pièce, non ouvertes (code $CODE ; session hôte du compte 3)" || arret "commit des sorties (relance B5b)"
    git rev-parse HEAD > "$BAC/c-sorties-p-v2.txt"
fi
git push -q origin "refs/heads/$BR_P:refs/heads/$BR_P" || arret "poussée (relance B5b : il reprend à la poussée)"
C=$(cat "$BAC/c-sorties-p-v2.txt"); echo "run de la pièce : $RMC ; base : $(cat "$BAC/c-main-p-v2.txt") ; commit des sorties : $C"; git ls-remote origin "refs/heads/$BR_P"
for f in $(git diff --name-only "$C^" "$C" | grep -v '\.sha256$'); do
    echo "$f sha256 $(sha256sum "$f" | cut -d' ' -f1) blob $(git rev-parse "$C:$f") octets $(stat -c %s "$f")"; done
echo "B5b fait : code $CODE ; $(git diff --name-only "$C^" "$C" | wc -l) fichiers commités, aucun ouvert ; poussé"
# attendu (code 0) : « les quatre fichiers écrits sont égaux … » ; le run ; le commit, égal à la tête distante ; quatre lignes « chemin
# sha256 … blob … octets … » (détails, base (A), issue, manifeste) ; « B5b fait : code 0 ; 8 fichiers commités ». Code 2 : la ligne de
# refus, rien de commité, aucune relance. Code 3 : le fichier d'arrêt et le manifeste commités et poussés (4 fichiers, ou plus si la
# pièce a écrit avant de s'arrêter) ; nœud de Lazar ; aucune relance ; le motif n'est pas affiché.
```

### Bloc F-B — journal provisoire (noms, empreintes, code ; aucune valeur), poussée (relançable)

Remplis d'abord les deux variables de tête (texte que tu as vu ; les heures viennent de `date -u`).

```bash
. "$HOME/bac-mots-et-cout-compte-3-v2/variables-v2.sh" || exit 1
CROCHET='<bloquée | passée>'; MODELES='session hôte : <modèle A | modèle C> ; identité dite en conversation seulement'
case "$CROCHET$MODELES" in *'<bloquée | passée>'*|*'<modèle A | modèle C>'*) arret "variables de tête non remplies";; esac
lire() { cat "$1" 2>/dev/null || echo "sans objet"; }
cd "$DEPOT"; [ "$(git rev-parse --abbrev-ref HEAD)" = "$BR_P" ] || arret "tu n'es pas sur $BR_P"
[ -e "$BAC/code-piece-v2.txt" ] || arret "la pièce n'a pas été appelée, ou n'a pas fini : pas de journal (un arrêt d'avant l'appel se dit à Lazar, section 14)"
[ -e "$BAC/nom-provisoire-p-v2.txt" ] || echo "registres-provisoires/compte-3-phase-b-$(date -u +%Y-%m-%d-%H%M)-v3.md" > "$BAC/nom-provisoire-p-v2.txt"
N=$(cat "$BAC/nom-provisoire-p-v2.txt"); C=$(lire "$BAC/c-sorties-p-v2.txt")
if [ ! -e "$BAC/c-provisoire-p-v2.txt" ]; then
mkdir -p registres-provisoires
{ echo "# Compte 3 — session hôte de la course de la pièce « mots et coût » sur 7b — journal provisoire (v3)"; echo
  echo "Écrit le $(date -u +%Y-%m-%dT%H:%M:%SZ) (\`date -u\`) par la session \`$SESSION_C3\`, branche \`$BR_P\` ; identifiants provisoires P3B-…, à numéroter par la mère."; echo
  echo "- P3B-001 : commande phase B v3 exécutée depuis $(lire "$BAC/debut-v2.txt") ; épreuve du crochet : $CROCHET ; $MODELES ; liste \`$LISTE\` (\`$EMPREINTE_LISTE\`) : attestation conforme."
  echo "- P3B-002 : base main \`$(lire "$BAC/c-main-p-v2.txt")\` ; commit de la pièce \`$COMMIT_PIECE\`, ligne \`CODE-MOTS-ET-COUT-T06\` égale à l'octet ; entrées de 7b : tête \`$TETE_7B\`, dix fichiers hors du dépôt (option \`--racine-entrees\`), jamais commités ; contrôle à blanc conforme ; interpréteur : $("$PYP" -c 'import numpy, scipy, torch; print("numpy", numpy.__version__, "scipy", scipy.__version__, "torch", torch.__version__.split("+")[0])' 2>/dev/null)."
  echo "- P3B-003 : appel unique lancé à $(date -u -d "@$(lire "$BAC/appel-piece-lance-v2.txt")" +%Y-%m-%dT%H:%M:%SZ 2>/dev/null), détaché ; code $(lire "$BAC/code-piece-v2.txt") en $(( $(stat -c %Y "$BAC/code-piece-v2.txt") - $(cat "$BAC/appel-piece-lance-v2.txt") )) s ; dernière étape du progrès : $(grep '^PROGRES ' "$BAC/progres-piece-v2.txt" 2>/dev/null | tail -n 1 | sed 's/^.* etape=//') ; sorties commitées : \`$C\`."
  echo "- P3B-004 : fichiers commités (chemin, sha256, objet git), aucun ouvert :"
  if git cat-file -e "$C^{commit}" 2>/dev/null; then for f in $(git diff --name-only "$C^" "$C"); do echo "    $f $(git cat-file blob "$C:$f" | sha256sum | cut -d' ' -f1) $(git rev-parse "$C:$f")"; done
  else echo "    aucun ; sortie de la pièce \`$(sha256sum "$BAC/sortie-piece-v2.txt" 2>/dev/null | cut -d' ' -f1)\`, progrès \`$(sha256sum "$BAC/progres-piece-v2.txt" 2>/dev/null | cut -d' ' -f1)\` (fichiers du bac, non poussés ; sur un code 2, la ligne de refus est dite à Lazar en conversation)"; fi
  echo "- P3B-005 : cette session n'a ouvert ni entrée ni sortie ; elle n'a vu que des noms, des tailles, des empreintes, le code de sortie, les étapes du progrès et, sur un code 2, la ligne de refus de la pièce ; ses exclusions de la phase A sont inchangées ($CELLULE_HOTE), plus la lecture et l'analyse des sorties de la pièce."
} > "$N"
PYTHONPATH="$DEPOT/src" "$PYP" -B -m controle_ia.scellement sceller "$N" || arret "sceau (relance F-B)"
git add -- "$N" "$N.sha256"; [ "$(git diff --cached --name-only | grep -vc '^registres-provisoires/')" = 0 ] || arret "index : autre chose que registres-provisoires/"
n=$(git diff --cached | grep -cE "$SECRETS"); [ "$n" = 0 ] || arret "garde des secrets : $n"
git commit -q -m "Compte 3 : journal provisoire de la session hôte de la course de la pièce « mots et coût »" || arret "commit (relance F-B)"
git rev-parse HEAD > "$BAC/c-provisoire-p-v2.txt"; fi
git push -q origin "refs/heads/$BR_P:refs/heads/$BR_P" || arret "poussée (relance F-B : il reprend à la poussée)"
echo "RENDU — branche $BR_P ; tête $(git rev-parse HEAD) ; journal provisoire $(cat "$BAC/c-provisoire-p-v2.txt")"; sha256sum "$N"
[ -z "$(git status --porcelain --untracked-files=all)" ] && echo "dépôt propre" || arret "dépôt non propre après le journal (git status) : rapport à la mère"
# attendu : « RENDU — branche … ; tête … ; journal provisoire … » ; l'empreinte du journal ; « dépôt propre ». Le bac reste en place (rien
# n'y est à reprendre : la phase C a son propre bac) ; .venv reste pour la phase C.
```

## 12. Ce que tu ne fais jamais ici

Relancer B5a ; lancer la pièce autrement ; afficher ou ouvrir `sortie-piece-v2.txt`, `progres-piece-v2.txt`, une entrée ou une sortie ;
arrêter un processus ; placer un fichier de 7b dans le dépôt ; committer autre chose que `diag/<run de la pièce>/`,
`runs/<run de la pièce>/` et le journal provisoire ; effacer un fichier du dépôt ; pousser sur `main` ; écrire dans `registres/` ; écrire un
identifiant de modèle ; jouer un bloc de la phase C.

## 13. Rendu à Lazar (il transmet à la mère)

1. Une à trois lignes : « Phase B : pièce « mots et coût » appelée une fois (détachée), code <n> en <s> s ; sorties scellées, non
   ouvertes, poussées sur `verdict/t06-mots-et-cout-compte-3-v1` ; rien lu. » — ou le bloc et le motif d'un arrêt.
2. Pour la mère : toute la sortie du bloc B5b (run, base, commit, tête distante, les lignes « chemin sha256 … blob … octets … »), la
   sortie « RENDU » du bloc F-B, le code et la durée, l'épreuve du crochet.
3. **Sur un code 2** : la ligne de refus et le nom de la dernière étape, **à Lazar**. Si l'étape est « modules gelés » ou « textes et
   registre », la ligne ne parle que du code et du registre : elle va aussi à la mère. Si l'étape est « entrées » ou « manifeste », la
   ligne peut citer la forme d'un fichier de 7b (un nom, un effectif, un début d'empreinte ; jamais une aire ni un taux) : Lazar décide
   de ce qu'il transmet à la mère, qui ne lit de 7b que l'état de BA-L2.
4. **Sur un code 3** : rien du motif (tu ne l'as pas lu) ; il est dans `arret-mots-et-cout-t06.json`, scellé, sur la branche.
5. Erreurs, écarts : une ligne chacun. Aucune analyse.

## 14. Ce qui arrête tout

- Tout « ARRÊT » d'un bloc. **Avant B5a, rien d'irréversible** (hors le nom de la branche poussée) : tu le dis à Lazar (bloc et motif), et
  rien d'autre. Un arrêt au bloc 1B : tu peux effacer `$HOME/bac-mots-et-cout-compte-3-v2` et relancer le bloc 1B une fois.
- Identifiant de session introuvable au bloc 1B : remplace `SESSION_C3=…` par celui que donne l'outil qui décrit ta session (ou la ligne
  « Claude-Session » de tes consignes d'attribution), puis relance le bloc 1B ; s'il n'est pas celui de la session hôte : arrêt.
- Fichier non suivi dans ton dépôt (blocs 0-B, B1, B4, B5a) : tu n'effaces rien, tu ne déplaces rien ; tu donnes les noms à Lazar, qui
  tranche.
- Bloc B2 : place libre insuffisante, installation en échec ou versions autres : rapport à la mère ; aucune installation à la main.
- Bloc B4 non conforme : **aucun appel** ; la mère lève la cause.
- **L'outil rend la main pendant ou après B5a** : B5-attente, puis B5b ; jamais B5a. Processus disparu sans code : B5-attente imprime
  les noms des dossiers écrits et s'arrête : nœud ; rien n'est relancé ni effacé. Borne de 60 minutes dépassée : nœud ; le processus
  continue.
- **Code 2** (refus avant le manifeste, rien d'écrit) : c'est une attente. Blocs B5b et F-B, rendu, arrêt ; la pièce ne se relance que
  par une version nouvelle de cette commande, sur un mot écrit de la mère. **Code 3** (arrêt après le manifeste) : fichier d'arrêt et
  manifeste commités, poussés ; nœud de Lazar ; aucune relance ; aucune ligne `ISSUE-MOTS-ET-COUT-T06` ne sera inscrite sur cette
  tentative (base (A), ligne BA-L0). **Tout autre code**, ou des noms inattendus : rien n'est commité ni effacé ; nœud.
- Poussée refusée (blocs B5b, F-B) : tu relances le bloc une fois, il reprend à la poussée ; refusée encore, ou refusée au bloc B1 :
  arrêt, rapport à la mère.
- Refus de permission, du crochet (hors l'épreuve du bloc 0-B) ou d'un classifieur : arrêt, rapport à la mère, aucun contournement.

## 15. Ce que fait la mère ensuite (pour mémoire ; tu ne le fais pas)

Dans l'ordre, et sans contredire la section 15 de `commande-compte-3-phase-c-v3.md`, qui reste la référence pour le bloc M :

1. **Bloc V — vérifier les sorties par leurs empreintes, sans les ouvrir** (dans son conteneur, depuis le dossier du dépôt ; elle remplit
   les trois variables de tête avec le rendu de l'hôte) :

```bash
export LC_ALL=C.UTF-8; date -u +%Y-%m-%dT%H:%M:%SZ
BRP=verdict/t06-mots-et-cout-compte-3-v1; C_BASE='<base main rendue par la session hôte>'; C_SORTIES='<commit des sorties rendu par la session hôte>'
RENDU=$(cat <<'FIN'
<lignes rendues par B5b>
FIN
)
case "$C_BASE$C_SORTIES$RENDU" in *'<base main'*|*'<commit des sorties'*|*'<lignes rendues'*) echo "ARRÊT : variables de tête non remplies"; exit 1;; esac
git fetch --no-tags -q origin "+refs/heads/$BRP:refs/remotes/origin/$BRP" +refs/heads/main:refs/remotes/origin/main || { echo "ARRÊT : récupération de $BRP et de main"; exit 1; }
[ "$(git rev-parse "$C_SORTIES^" 2>/dev/null)" = "$C_BASE" ] && git merge-base --is-ancestor "$C_SORTIES" "refs/remotes/origin/$BRP" \
    && git merge-base --is-ancestor "$C_BASE" refs/remotes/origin/main || { echo "ARRÊT : le commit des sorties n'a pas la base rendue pour parent, n'est pas sur la branche, ou la base n'est pas un commit de main"; exit 1; }
F=$(git diff --name-only "$C_BASE" "$C_SORTIES"); R=$(printf '%s\n' "$F" | sed -n 's#^runs/\([^/]*\)/manifeste\.json$#\1#p')
printf '%s\n' "$R" | grep -q -x -E '[0-9]{8}-[0-9]{6}-mots-et-cout-t06' || { echo "ARRÊT : run de la pièce introuvable dans le commit des sorties"; exit 1; }
n=$(printf '%s\n' "$F" | grep -v -c -x -E "(diag/$R/(mots-et-cout-t06-details|base-a-t08|issue-mots-et-cout-t06|arret-mots-et-cout-t06)|runs/$R/manifeste)\.json(\.sha256)?")
[ "$n" = 0 ] || { echo "ARRÊT : $n chemin(s) hors des sorties de la pièce dans le commit"; exit 1; }
[ "$(git diff --diff-filter=A --name-only "$C_BASE" "$C_SORTIES" | wc -l)" = "$(printf '%s\n' "$F" | wc -l)" ] || { echo "ARRÊT : le commit modifie ou retire un fichier de main"; exit 1; }
V=$(for f in $(printf '%s\n' "$F" | grep -v '\.sha256$'); do
        h=$(git cat-file blob "$C_SORTIES:$f" | sha256sum | cut -d' ' -f1); c=$(git cat-file blob "$C_SORTIES:$f.sha256" 2>/dev/null | cut -d' ' -f1)
        [ "$h" = "$c" ] && echo "$f sha256 $h blob $(git rev-parse "$C_SORTIES:$f") octets $(git cat-file -s "$C_SORTIES:$f")" || echo "ÉCART $f"; done)
printf '%s\n' "$V" | grep -q '^ÉCART' && { printf '%s\n' "$V" | grep '^ÉCART'; echo "ARRÊT : fichier autre que son compagnon, ou compagnon absent"; exit 1; }
[ "$(printf '%s\n' "$V" | sort)" = "$(printf '%s\n' "$RENDU" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//' | grep . | sort)" ] || { echo "ARRÊT : empreintes, objets ou tailles autres que le rendu de l'hôte"; exit 1; }
printf '%s\n' "$V"; echo "BLOC V : run $R ; $(printf '%s\n' "$F" | wc -l) fichiers, égaux à leurs compagnons et au rendu de l'hôte ; aucun ouvert ni affiché"
# attendu (code 0 de la pièce) : quatre lignes (détails, base (A), issue, manifeste) et « BLOC V : run … ; 8 fichiers … »
```

2. **Code 0 seulement : les deux lignes du registre, dans cet ordre** (base (A), plan, point 3, et « Ordre des lectures », point 3 ;
   T0.6, « Concordance avec T0.7 », points 4 et 5) : `LECTURE-T08-BASE-A`, qui cite `diag/<run de la pièce>/base-a-t08.json` et son
   empreinte, **puis** `ISSUE-MOTS-ET-COUT-T06`, qui cite `diag/<run de la pièce>/issue-mots-et-cout-t06.json` et son empreinte ; par
   `t07.registre_v1.ajouter_ligne`, heure du système, deux appels. Aucune autre ligne (une clé de verdict y ferait refuser l'étape B).
   Code 3 : aucune ligne (BA-L0) ; nœud de Lazar. Code 2 : rien ; la mère lève la cause et fait écrire une version nouvelle.
   **Condition que cette commande ne lève pas, avant la ligne `ISSUE-MOTS-ET-COUT-T06`** : la base (A) scellée (T0.8, l. 111, « Audit
   R4 ») veut, si l'audit R4 se déclenche, une relecture « avant l'inscription de `ISSUE-MOTS-ET-COUT-T06`, par un lecteur neuf » ;
   la pièce en écrit l'état dans `base-a-t08.json` (réserve R-BA6), que la mère n'ouvre pas (elle n'en lit que l'état de BA-L2, par
   programme, R-2741) : qui lit cet état, et comment, est à trancher par Lazar avant cette ligne (nœud ; rapport du préparateur v3,
   point M-1). Rien ici ne change l'ordre de la phase C (section 15) : les deux lignes, puis le bloc M.
3. **Bloc M** de la phase C v3 (section 15 ; le même, à l'octet, dans le brouillon 1 de sa v4), avec
   `BRP='verdict/t06-mots-et-cout-compte-3-v1'` : elle lit, par programme, **le seul
   état de BA-L2** (R-2741, nœud N-C). Rien d'autre de 7b n'est lu par la mère : ni une sortie de la pièce, ni le journal du progrès.
   Le programme du bloc M exige la ligne `LECTURE-T08-BASE-A` datée strictement avant l'instant où il est joué : une seconde suffit.
4. **Ligne dédiée du registre des décisions** : l'état de BA-L2 seul (ou le mot de Lazar s'il « s'applique » : l'étape B attend ce mot),
   sans aucun mot de l'étape B bis ; son numéro est le marqueur `<<R_BA_L2>>` de la phase C.
5. **Faits au registre des décisions** (branche, base, commits, run, empreintes, code, durée ; aucune valeur) ; liste « qui a lu quoi »
   v3 : l'hôte a joué la pièce sans rien ouvrir ; la mère a vérifié des empreintes et lu l'état de BA-L2.
6. **Marqueur `<<BRANCHE_PIECE>>` de la phase C** : `verdict/t06-mots-et-cout-compte-3-v1` (les sorties restent sur cette branche, comme
   celles de l'étape A sur la leur) ; ou `main`, si la mère les y recopie par leurs objets git, sans les ouvrir.

## Annexe — essais (règle R5)

- **Répétition de bout en bout** de tous les blocs de cette commande (0b-B, 1B, 2B, B1 à B5b, F-B, bloc V), sur dépôts jouets :
  `repetition-phase-b-v3/repetition_phase_b_jouet_v3.sh`, sortie `repetition-phase-b-v3/repetition-phase-b-jouet-sortie-v3.txt` (résultat
  au rapport v3). La **vraie pièce** v3 y est jouée par son **vrai lanceur**, en mode réel, sur des entrées factices fabriquées par la
  fabrique de ses essais, à la configuration scellée de 7b : codes 0, 2 et 3. Chaînes éprouvées en plus : clone superficiel approfondi ;
  bloc M de la phase C v3 (égal à celui du brouillon 1 de sa v4, comparé par la répétition) rejoué sur la branche jouet (état de
  BA-L2 lu dans une vraie sortie de la pièce) ; fichier d'issue repris sur
  la branche comme le fera le bloc C2 de la phase C.
- **Constantes** : `repetition-phase-b-v3/verification_constantes_phase_b_v3.sh`, sortie
  `repetition-phase-b-v3/verification-constantes-phase-b-sortie-v3.txt` : chaque valeur écrite en dur au bloc 1B est comparée à `main`
  distant (lignes du registre à l'octet, empreintes des pièces et de leurs compagnons, commit de la pièce ancêtre de `main`, fiche du code,
  attestation, liste, empreintes de lancement, journal sans ouverture), et aux têtes du distant (branche de 7b, branche de la pièce absente).
- **Crochet de garde** : le texte de chaque bloc est passé au crochet du dépôt (`.claude/hooks/garde_calcul.py`) par la répétition : le
  premier bloc (l'épreuve) est bloqué, les treize autres passent.
- **Non éprouvé ici** (seul l'hôte peut le jouer) : le téléchargement réel de l'environnement (environ 6 Go : trop lourd pour le
  conteneur partagé du préparateur ; le chemin d'installation du bloc B2 est répété sur des exigences jouets) ; le transport par GitHub
  (transport local dans la répétition) ; la pièce sur les entrées réelles.
