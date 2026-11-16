# Commande de la mère au compte 3 — phase C : l'étape B de T0.7 (appel unique) et son lecteur de verdict — v4

- **Statut** : commande écrite de la session mère au compte 3 (R-2711 (2)), à coller par Lazar dans **la même session** que la phase A
  (`commande-compte-3-phase-a-v2.md`), après ses préalables (section 0, point 2). Aucune dépense (processeur ; 0 USD) ; aucun texte
  scellé changé ; si elle contredit T0.7 scellé, son addendum ou le module `src/controle_ia/t07/` au commit C7, le texte ou le module fait
  foi : tu t'arrêtes et tu le dis.
- **Version 4** : la version 3 (`commande-compte-3-phase-c-v3.md`,
  `9d7889198238c171447a06f56f1a37beb4190572c3a9ceceb18144541c258d2e`, scellée, répétée 53 sur 53, gardée, R12), plus un seul changement :
  le bloc C5 remet au lecteur B, en plus de ses treize fichiers, `diag/$R7/sondes-t07.json` et son compagnon, que le bloc C2 place déjà
  dans la racine et compare à la ligne `SONDES-T07` (quatorze fichiers et leurs compagnons, plus l'extrait : 29 fichiers au bordereau).
  Raisons (décision de la mère R-2980, registre des décisions) : le texte scellé de T0.7 renvoie le lecteur du verdict à ce fichier
  (l. 1539 : effectifs des « paires des jeux » ; l. 2659, défaut DF-05 : le vrai motif d'un échec de T7-P6 dès l'apprentissage y est
  écrit, « où le lecteur du verdict (R13) le lit ») et la version 3 ne le lui remettait pas ; aucun de ses noms n'est touché par les
  filtres du bloc 1C (contrôlé par programme, `rapport-commande-phase-c-v4-v1.md`). Rien d'autre ne change : noms du bac, des fichiers
  de marque, des branches et des marqueurs **inchangés, à dessein** (mêmes raisons qu'à la version 3) ; phase A inchangée.
- **Version 3** : la version 2 (`commande-compte-3-phase-c-v2.md`, `fee4caaa…`, scellée, répétée 44 sur 44, gardée, R12), plus deux
  changements : (1) le bloc C5 refait ses pièces de zéro à chaque relance et n'écrit le bordereau qu'après le filtre de noms (dans la v2,
  une faute de nom laissait un bordereau écrit, qui bloquait la relance) ; (2) la répétition éprouve en plus, sur artefact, les gardes de
  2C (cellule d'exclusions de l'hôte, CL3-02), C0 (ligne de décision mêlée à B bis, sans BA-L2, absente : CL3-03), C5 (nom interdit,
  contenu de B bis : CL3-03) et C7 (message reçu différent, archive : CL3-21, CL3-18), comme la répétition de la phase A (X1 à X5) — règle
  R5. Noms du bac et des fichiers de marque **inchangés depuis la v2, à dessein** : un bac déjà ouvert arrête le bloc 1C, et le marqueur
  d'appel est le même d'une version à l'autre (aucun second appel possible).
- **Version 2** : la phase C de la version 1 (`commande-compte-3-v1.md`, `21d891c5…`, gardée, R12), « non remettable en l'état » selon sa
  contre-lecture (`contre-lecture-commande-compte-3-v1.md`, `092acef6…`, R-2735), corrigée de CL3-04 (bloc de commit et de poussée
  relançable seul), CL3-05 (durée mesurée et bornée ; appel détaché), CL3-06 (contrôle à blanc étendu : garde du module sur une copie du
  registre), CL3-07 (**répétition de bout en bout de tous les blocs de l'appel unique sur dépôts jouets**, sortie versée), CL3-02
  (cellule d'exclusions de l'hôte, attestation v3), CL3-03 (filtres de contenu des blocs C0 et C5), CL3-08, CL3-09, CL3-10, CL3-11,
  CL3-14, CL3-15, CL3-16, CL3-17 (bloc 0b-C), CL3-18 (bloc C7), CL3-19, CL3-20, CL3-21 (traitement de chacun :
  `rapport-preparateur-v2.md`). Décisions de Lazar portées
  (R-2741) : N-C, la mère lit par programme le seul état BA-L2 (bloc M, section 15) ; N-D, le lot NARCBench continue en parallèle sans
  rien ouvrir de T0.7, 7a ou 7b avant les verdicts ; N-E, aucune attente de la grille de G0 ; étape B bis (R-2740) : même hôte, lecteurs
  distincts, plan de B bis scellé avant toute lecture de l'étape B.
- **Rédacteur** : le préparateur (sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, modèle A), le 2026-11-14 à partir de
  12:07:52Z (`date -u`), version 3 à partir de 13:04:29Z ; ni lecteur ni juge ; aucune sortie de 7a, 7b ou T0.7 ouverte.
  **Version 4** : un sous-agent neuf, modèle B, de la session mère `session_016QhUrtmLyFWJP6Cy7rgfXH`, le 2026-11-16 à partir de
  12:58:48Z (`date -u`) ; ni lecteur ni juge ; aucun fichier de `diag/`, `runs/` ou `donnees/` ouvert.
- **Pièces** (même dossier, chacune scellée) :

| pièce | empreinte | rôle |
|---|---|---|
| `controle_a_blanc_etape_b_compte_3_v2.py` | `21310d805b0578f658e26cf1792c2072fe1b1c71c9de205f565e2e056a638795` | contrôle à blanc v2 (registre, sceaux, antériorités, garde adaptée, `CODE-T07`, fichiers, condition d'ordre B bis ; section 9 : garde du module sur une copie du registre, lectures d'avant les scores) |
| `essai_controle_a_blanc_etape_b_compte_3_v2.sh`, sortie `essai-controle-a-blanc-etape-b-compte-3-v2-sortie-v1.txt` | `b53560a5…`, `495d1f9d…` | essai R5 : 19 sur 19 (racine au format réel ; artefacts de CL3-06 et CL3-14) ; non-régression de l'essai v1 sur le script v2 : 28 sur 28 (`essai-v1-sur-script-v2-sortie-v1.txt`, `ad8d7c0c…`) |
| `attestation_qui_a_lu_quoi_compte_3_v3.py` | `a20f137c92022c58fd8090a2c1e25d8c575fec1b0e8a15d2190a1b1bae505a62` | attestation de la phase C : la ligne de l'hôte, inscrite après la phase A, admise à sa seule cellule d'exclusions |
| `essai_attestation_compte_3_v3.sh`, sortie `essai-attestation-compte-3-v3-sortie-v1.txt` | `22375890…`, `6d02b640…` | essai R5 : 17 sur 17 |
| `mesure_duree_etape_b_v1.py`, sortie `mesure-duree-etape-b-sortie-v1.txt` | `2f300ecf…`, `e77e06f1…` | CL3-05 : 1,6 à 2,1 s par comparaison au plancher (800 directions, 2 000 tirages, 1 280 actions) ; 0,6 à 2,2 min attendues |
| `lecture_etat_ba_l2_mere_v1.py`, essai et sortie | `6d63e9d6…` ; `21fc789c…`, `51261a83…` | bloc M de la mère (N-C) : l'état BA-L2 seul ; essai 10 sur 10 |
| `etape_b_jouet_v1.py` | `4043655b42d4fc058e849c6825967fec078ad70ef93e304c24ed8bd212f5ead0` | module d'étape B **jouet**, pour la seule répétition : vraie garde `lecture_v4.ouvrir`, attente, `lecture-t07.json` jouet |
| `repetition_phase_c_jouet_v4.sh`, sortie `repetition-phase-c-jouet-v4-sortie-brouillon1-v1.txt` | voir `rapport-commande-phase-c-v4-v1.md` | répétition de bout en bout des blocs de cette commande sur dépôts jouets, appel interrompu, poussées refusées et artefacts des gardes compris ; bordereau de 29 fichiers, `sondes-t07.json` et son compagnon compris |
| `commande-compte-3-phase-c-v3.md`, `repetition_phase_c_jouet_v3.sh`, sortie `repetition-phase-c-jouet-sortie-v3.txt` | `9d788919…`, `8be57168…`, voir le rapport v2 | version 3, gardée (R12) : 53 sur 53 |
| `commande-compte-3-phase-c-v2.md`, `repetition_phase_c_jouet_v2.sh`, sortie `repetition-phase-c-jouet-sortie-v2.txt` | `fee4caaa…`, `7a9da180…`, `7f01ef2c…` | version 2, gardée (R12) : 44 sur 44 |

## 0. D'abord, pour Lazar et la mère

1. **Voie d'écriture** : branche neuve `verdict/t07-etape-b-compte-3-v1`, créée sur `main` à jour, poussée par refspec ; quatre commits au plus :
   le journal `registres/scellements-v1.md.ouvertures.md` (écrit par le seul module), la sortie scellée du module (`lecture-t07.json` ou
   `arret-etape-b.json`), le verdict, le journal provisoire. La mère recopie dans `main` le journal d'abord, puis le verdict ; la sortie reste
   sur la branche (comme les sorties de l'étape A sur `donnees/t07-etape-a-v1`), avec le chemin et l'empreinte du manifeste de T0.7 (CL3-19).
2. **Préalables, vérifiés par le bloc C0 et par le contrôle à blanc** : lignes `AUDIT-FUITES-T07`, `CODE-MOTS-ET-COUT-T06`,
   `LECTURE-T08-BASE-A`, `ISSUE-MOTS-ET-COUT-T06` dans `registres/scellements-v1.md` ; ligne `<<R_BA_L2>>` du registre des décisions, **dédiée
   à l'état de BA-L2** (bloc M, aucun mot de l'étape B bis) ; ligne `<<CLE_PLAN_BBIS>>` du plan scellé de B bis dans `<<REGISTRE_BBIS>>` ;
   consigne scellée du lecteur B ; liste « qui a lu quoi » v3, dont la ligne de l'hôte porte en « exclu de » exactement `CELLULE_HOTE`
   (bloc 1C) ; tout poussé sur `main` avant ce message.
3. **Code et appel** : `lecture_v4 etape-b` (la v3 refuse la configuration v8), du code d'une **arborescence détachée à C7**
   (`c2fab6cc…`, commit cité par `CODE-T07` ; l'ordre de l'étape A v2, § 9, écrit « S7 », descendant de C7 aux mêmes `src/` et `tests/`, P9 :
   écart de nom déclaré, code égal). L'appel est **lancé détaché** (bloc C4a), attendu par relevés courts (bloc C4-attente), puis commité et
   poussé par un bloc relançable seul (C4b) : l'outil peut rendre la main à tout moment sans perdre le journal ni appeler deux fois. Durée
   attendue : moins de 3 minutes (mesure CL3-05) ; **borne : 60 minutes**, au-delà nœud de Lazar, le processus n'est jamais arrêté.
4. **Section 9 du contrôle à blanc** (CL3-06) : la garde d'ouverture du module lui-même est jouée sur une copie du registre ; elle lit par
   programme la table A, l'issue de P3-bis, l'audit, le fichier « mots et coût », les épisodes et les colonnes des mesures, **sans rien en
   afficher** ; elle n'ouvre jamais les scores. En remettant cette commande, la mère accepte cette lecture structurelle par programme ; sinon
   elle retire `--chaine` du bloc C3 et le risque de refus évitable est déclaré.
5. **Cloisonnement B / B bis** (R-2740) : même hôte, lecteurs distincts ; aucune pièce dont le nom **ou le contenu** porte l'étape B bis ne
   part au lecteur B (filtres du bloc C5) ; rien de cette branche n'entre dans un espace de B bis avant le verdict scellé de B bis. La
   dépense de B bis (ligne GO-2026-11-14-09, 40 USD) est hors de cette commande, qui ne dépense rien.

## 1. Interdits permanents

Ceux de la section 1 de la commande de la phase A (brief du compte 3, section 6, recopiés tels quels), plus :

- **Tu n'ouvres aucun résultat** : ni la sortie du module (gardée dans `$ESPACE_B`, jamais affichée ; seule exception, sur un code 2, la
  ligne `REFUS-T07` que le module écrit au journal), ni `lecture-t07.json`, ni les fichiers placés, ni le verdict en prose. Tu lis les noms,
  les compagnons, les champs `fichier`, `octets` et `sha256` du manifeste des morceaux (par programme), les codes de sortie, le rapport final
  du lecteur.
- Jamais `resume.json`, `lecture-sondes-t06.json`, les activations ou les adaptateurs de 7b ; jamais `sondes-neuves-t07.npz`,
  `planchers-figees-t07.npz`, `temoins-lexicaux-t07.json` ; jamais une pièce de l'étape B bis.
- **Un seul appel de l'étape B** : le fichier `appel-etape-b-lance-v2.txt` est posé avant l'appel ; s'il existe, le bloc C4a s'arrête.
  Jamais le module lancé autrement que par C4a ; jamais un processus arrêté (aucun `kill` d'arrêt ; `kill -0` ne fait que constater).
- Exclusions de cette session : celles de la phase A (section 1), plus l'analyse du verdict B et tout rôle de lecteur de B bis.
- Aucune poussée hors de `verdict/t07-etape-b-compte-3-v1` ; jamais `main`.

## 2. Qui fait quoi

- **Toi, la session hôte (la même que pour la phase A)** : blocs dans l'ordre ; tu lances une fois l'étape B ; tu remets au lecteur B ;
  tu commites et pousses ; tu rends.
- **Le lecteur B** : un sous-agent neuf du **modèle C** (un autre modèle que les auteurs de T0.7), jamais le lecteur A, jamais un lecteur
  de B bis ; si ton outil d'agent ne peut pas créer un sous-agent du modèle C : **arrêt, nœud de Lazar** (aucun repli sur le modèle A).
- **La mère** : bloc M (état BA-L2) avant cette commande ; lignes ; recopies (section 15).

## 3. Marqueurs

| marqueur | qui, quand | où |
|---|---|---|
| chemin et empreinte de la version remise | Lazar, en conversation ; le bloc 0b-C les imprime | bloc 0b-C |
| `<<LISTE>>`, `<<EMPREINTE_LISTE>>` | la mère : liste « qui a lu quoi » v3 (ligne de l'hôte à la cellule `CELLULE_HOTE`) | bloc 1C |
| `<<CONSIGNE_LECTEUR_B>>`, `<<EMPREINTE_CONSIGNE_LECTEUR_B>>` | la mère : consigne scellée du lecteur B | bloc 1C |
| `<<REGISTRE_BBIS>>`, `<<CLE_PLAN_BBIS>>` | la mère : registre propre et clé du scellement du plan de B bis | bloc 1C |
| `<<R_BA_L2>>` | la mère : numéro de la ligne dédiée du registre des décisions (état de BA-L2, ou mot de Lazar) | bloc 1C |
| `<<BRANCHE_PIECE>>` | la mère : branche qui porte le fichier « mots et coût » s'il n'est pas sur `main` (sinon `main`) | bloc 1C |
| `<<ESPACE>>`, `<<EMPREINTE_BORDEREAU>>`, `<<PY>>`, `<<NOTE_MODELE>>`, `<<CONSIGNE>>`, `<<EMPREINTE_CONSIGNE>>` | toi, par programme | bloc C6 |

## 4. Mode d'emploi

- Chaque bloc se lance tel quel, dans un seul appel de ton outil, dans l'ordre ; chaque bloc relit `$HOME/bac-etape-b-compte-3-v2/variables-v2.sh`.
- **Relançables** : 2C, C0, C1a, C1 (avant sa poussée), C2, C3, C4-attente (autant de fois qu'il faut), C4b et F-C (ils reprennent à la
  poussée : leurs commits sont gardés au bac), C5 (avant le bordereau ; pièces refaites de zéro), C7.
  **Jamais relancé** : C4a. Délai maximal de l'outil pour C1a, C1, C2, C3 et C4b.
- **Si l'outil rend la main pendant ou après C4a** : tu ne relances pas C4a ; tu joues C4-attente, puis C4b quand le code est écrit.
- Au-dessus de 80 % de quota, tu ne commences ni C4a ni C6.

## 5. Bloc 0b-C — copie locale à jour

```bash
cd "$(git rev-parse --show-toplevel)" || exit 1
B=$(git rev-parse --abbrev-ref HEAD)
[ -z "$(git status --porcelain --untracked-files=no)" ] || { echo "ARRÊT : modifications suivies dans ton dépôt"; exit 1; }
git fetch --no-tags -q origin +refs/heads/main:refs/remotes/origin/main || { echo "ARRÊT : récupération de main"; exit 1; }
[ "$B" = main ] || git switch -q main || { echo "ARRÊT : passage sur main"; exit 1; }
git merge -q --ff-only refs/remotes/origin/main || { echo "ARRÊT : main local non avançable en avance rapide"; exit 1; }
echo "main local : $(git rev-parse HEAD) (branche quittée : $B)"
sha256sum docs/procedures/lecture-7b-etape-b-compte-3-v1/commande-compte-3-phase-c-v4.md
# attendu : main à jour ; l'empreinte est celle que Lazar t'a donnée (sinon arrêt)
```

## 6. Bloc 1C — variables (une seule fois)

```bash
export LC_ALL=C.UTF-8
arret() { echo "ARRÊT : $*"; exit 1; }
DEPOT=$(git rev-parse --show-toplevel) || arret "lance ce bloc depuis le dossier du dépôt"
case "$(git -C "$DEPOT" remote get-url origin)" in *lciric/controle-ia-travail*) ;; *) arret "dépôt d'origine autre";; esac
BAC="$HOME/bac-etape-b-compte-3-v2"; [ ! -e "$BAC" ] || arret "$BAC existe déjà : rapport à la mère"
SESSION_C3="session_${CLAUDE_CODE_REMOTE_SESSION_ID#cse_}"; [[ "$SESSION_C3" =~ ^session_[0-9A-Za-z]{10,}$ ]] || arret "identifiant de session introuvable"
LISTE='<<LISTE>>'; EMPREINTE_LISTE='<<EMPREINTE_LISTE>>'; CONSIGNE_B='<<CONSIGNE_LECTEUR_B>>'; EMPREINTE_CONSIGNE_B='<<EMPREINTE_CONSIGNE_LECTEUR_B>>'
REGISTRE_BBIS='<<REGISTRE_BBIS>>'; CLE_BBIS='<<CLE_PLAN_BBIS>>'; R_BA_L2='<<R_BA_L2>>'; BR_P='<<BRANCHE_PIECE>>'
case "$LISTE $EMPREINTE_LISTE $CONSIGNE_B $EMPREINTE_CONSIGNE_B $REGISTRE_BBIS $CLE_BBIS $R_BA_L2 $BR_P" in *'<<'*) arret "marqueur non rempli (la mère)";; esac
mkdir -p "$BAC" && date -u +%Y-%m-%dT%H:%M:%SZ > "$BAC/debut-v2.txt"
cat > "$BAC/variables-v2.sh" <<EOF
export LC_ALL=C.UTF-8 PYTHONDONTWRITEBYTECODE=1
arret() { echo "ARRÊT : \$*"; exit 1; }
DEPOT='$DEPOT'; BAC='$BAC'; SESSION_C3='$SESSION_C3'
LISTE='$LISTE'; EMPREINTE_LISTE='$EMPREINTE_LISTE'; CONSIGNE_B='$CONSIGNE_B'; EMPREINTE_CONSIGNE_B='$EMPREINTE_CONSIGNE_B'
REGISTRE_BBIS='$REGISTRE_BBIS'; CLE_BBIS='$CLE_BBIS'; R_BA_L2='$R_BA_L2'; BR_P='$BR_P'
ICI="\$DEPOT/docs/procedures/lecture-7b-etape-b-compte-3-v1"
R6=20261111-151701-t06-reel; R7=20261114-001352-t07-lecture-reel
B7B=calcul/t06-confirmation-7b-v1; TETE_7B=55c3e3eb89a4650419f35999aaa4c54288275b0d
BEA=donnees/t07-etape-a-v1; TETE_EA=0c176db582ec13705e8fb7cc2d281215e2766e42
C7=c2fab6cc7267b76228a75dc3e2e08bc7aa038961; BR_B=verdict/t07-etape-b-compte-3-v1
DEPOT_URL=https://github.com/lciric/controle-ia-travail.git
H_SCORES=13ac4480035f1ef6d4ea8ac81ffa962c1324e4e9e90a78c1d4f569f2abd0509d; H_SONDES=aa6892320f130e96af45e4e70b542b7ccfcea3ccd23d2fdc3e722b5637affa95
H_CONFIG_CANON=0f32c6de1a6bf1f20ee2bf74c3839c2a2054b77c34a44a557dc821a83db60e12
H_BLANC=21310d805b0578f658e26cf1792c2072fe1b1c71c9de205f565e2e056a638795; H_ATTESTATION3=a20f137c92022c58fd8090a2c1e25d8c575fec1b0e8a15d2190a1b1bae505a62
CELLULE_HOTE='analyse du verdict A ; étape B bis (conception et verdicts) ; T0.8 ; G0 ; préenregistrement NARCBench (rédaction, contre-lecture, course) ; brouillons des papiers B et C ; code de la pièce « mots et coût »'
MODULE_ETAPE_B=controle_ia.t07.lecture_v4; PYTHONPATH_SUP=''; BORNE_S=3600; NOTE_MODELE="modèle C"
CLONE7B="\$BAC/clone-7b-v2"; CLONEEA="\$BAC/clone-etape-a-v2"; WT_C7="\$BAC/code-c7-v2"; MORCEAUX="\$BAC/morceaux-scores-v2"; ESPACE_B="\$BAC/espace-etape-b-v2"
CONFIG_T07="\$DEPOT/prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json"
SECRETS='(sk-ant-[A-Za-z0-9]|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|hf_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{12}|AIza[0-9A-Za-z_-]{20,})'
INTERDITS_NOMS_B='bbis|b-bis|etape-b-bis|lecture-sondes|resume\.json|scores-actions|activations|adaptateur|sondes-neuves|bras-attaque|mode-tenu|anteriorite-bras|etiqueteur|quarantaine|mesure-unanime'
INTERDITS_CONTENU_B='bbis|b-bis|etape-b-bis|étape b bis|b bis|bras-attaque|mode-tenu'
EOF
echo "session : $SESSION_C3 ; variables : $BAC/variables-v2.sh"
# attendu : aucun « ARRÊT »
```

## 7. Bloc 2C — contrôles d'entrée, attestation, nouveauté

```bash
. "$HOME/bac-etape-b-compte-3-v2/variables-v2.sh" || exit 1
D=$(curl -sS --max-time 20 -D - -o /dev/null https://pypi.org/simple/numpy/ 2>/dev/null | tr -d '\r' | awk -F': ' 'tolower($1)=="date"{print $2}' | tail -1)
[ -n "$D" ] || arret "horloge de référence injoignable"; E=$(( $(date -u +%s) - $(date -u -d "$D" +%s) )); echo "écart de l'horloge : $E s"
[ "${E#-}" -le 120 ] || arret "horloge décalée de plus de 120 s"
(cd "$DEPOT/docs" && sha256sum -c --quiet sha256sums-lancement-v2.txt) && echo "empreintes de lancement conformes" || arret "empreintes de lancement"
[ "$(sha256sum "$ICI/controle_a_blanc_etape_b_compte_3_v2.py" | cut -d' ' -f1)" = "$H_BLANC" ] || arret "pièce : contrôle à blanc v2"
[ "$(sha256sum "$ICI/attestation_qui_a_lu_quoi_compte_3_v3.py" | cut -d' ' -f1)" = "$H_ATTESTATION3" ] || arret "pièce : attestation v3"
python3 -I -B "$ICI/attestation_qui_a_lu_quoi_compte_3_v3.py" "$DEPOT/$LISTE" "$EMPREINTE_LISTE" "$SESSION_C3" --admettre-hote "$CELLULE_HOTE" \
    || arret "attestation non conforme : rien n'est lancé ; la mère tranche"
cd "$DEPOT"; [ -z "$(git branch --list 'lot/compte-3-v1')" ] || arret "branche locale lot/compte-3-v1 : session du lot ?"
[ -n "$(git config user.name)" ] && [ -n "$(git config user.email)" ] || arret "identité git absente"
echo "contrôles d'entrée conformes"
# attendu : écart ≤ 120 s ; « ATTESTATION : CONFORME — … lignes de l'hôte admises : 1 » (ou 0) ; « contrôles d'entrée conformes »
```

## 8. Phase C — l'étape B

### Bloc C0 — conditions écrites par la mère (lecture seule)

```bash
. "$HOME/bac-etape-b-compte-3-v2/variables-v2.sh" || exit 1
cd "$DEPOT"; M=refs/remotes/origin/main
for k in AUDIT-FUITES-T07 ISSUE-MOTS-ET-COUT-T06 LECTURE-T08-BASE-A CODE-MOTS-ET-COUT-T06; do
    [ "$(git show "$M:registres/scellements-v1.md" | grep -c "^| $k |")" = 1 ] && echo "ligne $k : une" || arret "ligne $k absente ou en double sur main"; done
L=$(git show "$M:registres/decisions.md" | grep "^| $R_BA_L2 |"); [ "$(printf '%s' "$L" | grep -c .)" = 1 ] || arret "ligne $R_BA_L2 absente : l'étape B attend (T0.7, l. 2183)"
printf '%s' "$L" | grep -q -i -E "$INTERDITS_CONTENU_B" && arret "la ligne $R_BA_L2 mêle l'étape B bis : la mère écrit une ligne dédiée (CL3-03)"
printf '%s' "$L" | grep -q 'BA-L2' || arret "la ligne $R_BA_L2 ne nomme pas BA-L2"
echo "décision $R_BA_L2 : présente, dédiée (non lue ici : la mère y a écrit l'état de BA-L2 ou le mot de Lazar)"
[ "$(git show "$M:$REGISTRE_BBIS" 2>/dev/null | grep -c "^| $CLE_BBIS |")" = 1 ] && echo "plan de B bis : ligne présente" || arret "plan de l'étape B bis non scellé : aucune étape B"
[ "$(git show "$M:registres/scellements-v1.md" | grep -c "^| $CLE_BBIS |")" = 0 ] || arret "$CLE_BBIS écrite au registre de T0.7 : nœud"
# attendu : quatre « ligne … : une » ; la décision dédiée ; le plan de B bis ; aucun « ARRÊT »
```

### Bloc C1a — interpréteur avec torch, versions exactes (relançable)

```bash
. "$HOME/bac-etape-b-compte-3-v2/variables-v2.sh" || exit 1
VERS='import numpy, scipy, torch, sys; v=(numpy.__version__, scipy.__version__, torch.__version__.split("+")[0]); print("versions :", *v); sys.exit(0 if v == ("2.4.6", "1.17.1", "2.14.1") else 1)'
if [ -x "$DEPOT/.venv/bin/python" ] && "$DEPOT/.venv/bin/python" -c "$VERS" 2>/dev/null; then PYC="$DEPOT/.venv/bin/python"
elif [ -x "$BAC/venv-c-v2/bin/python" ] && "$BAC/venv-c-v2/bin/python" -c "$VERS" 2>/dev/null; then PYC="$BAC/venv-c-v2/bin/python"
else L=$(df -Pk "$HOME" | awk 'NR==2{print $4}'); [ "$L" -ge 9437184 ] || arret "place libre $L Kio < 9 Gio : rapport à la mère"
     [ -e "$BAC/venv-c-v2" ] || python3 -m venv "$BAC/venv-c-v2" || arret "environnement"
     "$BAC/venv-c-v2/bin/pip" install -q --disable-pip-version-check -r "$DEPOT/requirements-cpu.txt" || arret "installation (relance ce bloc)"
     PYC="$BAC/venv-c-v2/bin/python"; fi
"$PYC" -c "$VERS" || arret "versions autres que requirements-cpu.txt"
grep -q '^PYC=' "$BAC/variables-v2.sh" || echo "PYC='$PYC'" >> "$BAC/variables-v2.sh"
# attendu : « versions : 2.4.6 1.17.1 2.14.1 » ; aucun « ARRÊT »
```

### Bloc C1 — branche neuve, code détaché à C7, poussée éprouvée

```bash
. "$HOME/bac-etape-b-compte-3-v2/variables-v2.sh" || exit 1
cd "$DEPOT"; [ -z "$(git status --porcelain --untracked-files=no)" ] || arret "modifications suivies dans ton dépôt"
[ "$(git rev-parse --is-shallow-repository)" = false ] || git cat-file -e "$C7^{commit}" 2>/dev/null \
    || git fetch --no-tags -q --unshallow origin +refs/heads/main:refs/remotes/origin/main || arret "approfondissement de l'historique"
git cat-file -e "$C7^{commit}" || arret "commit C7 absent de ton dépôt : rapport à la mère"
[ -z "$(git ls-remote origin "refs/heads/$BR_B")" ] || arret "la branche $BR_B existe déjà au distant (R12)"
if [ "$(git rev-parse --abbrev-ref HEAD)" = "$BR_B" ] && [ -e "$BAC/c-main-b-v2.txt" ]; then echo "branche $BR_B déjà créée (bloc relancé)"
else git switch -q --no-track -c "$BR_B" refs/remotes/origin/main || arret "création de $BR_B"; git rev-parse HEAD > "$BAC/c-main-b-v2.txt"; fi
git merge-base --is-ancestor "$C7" HEAD || arret "C7 n'est pas un ancêtre de la base de $BR_B"
[ -e "$WT_C7" ] || git worktree add -q --detach "$WT_C7" "$C7" || arret "arborescence détachée à C7"
[ "$(git -C "$WT_C7" rev-parse HEAD)" = "$C7" ] || arret "arborescence C7 : tête autre"
[ -z "$(git -C "$WT_C7" status --porcelain --untracked-files=all -- src/controle_ia)" ] || arret "arborescence C7 : src/controle_ia/ modifié"
grep -q '^PYTHONPATH_ETAPE_B=' "$BAC/variables-v2.sh" || echo "PYTHONPATH_ETAPE_B='${PYTHONPATH_SUP:+$PYTHONPATH_SUP:}$WT_C7/src'" >> "$BAC/variables-v2.sh"
git push -q origin "refs/heads/$BR_B:refs/heads/$BR_B" && echo "branche $BR_B poussée (égale à main) ; code : $WT_C7 (C7, propre)" || arret "poussée refusée : rapport à la mère"
# attendu : « branche … poussée … ; code : … (C7, propre) » ; aucun « ARRÊT »
```

### Bloc C2 — données de l'étape B placées dans la racine (jamais commitées ; relançable)

```bash
. "$HOME/bac-etape-b-compte-3-v2/variables-v2.sh" || exit 1
cd "$DEPOT"; [ "$(git rev-parse --abbrev-ref HEAD)" = "$BR_B" ] || arret "tu n'es pas sur $BR_B"
place() {   # $1 dépôt, $2 tête, $3 chemin : copie à l'octet ; un fichier déjà là (suivi ou non) est admis s'il est égal au blob
    if [ -e "$DEPOT/$3" ]; then git -C "$1" show "$2:$3" | cmp -s - "$DEPOT/$3" && { echo "déjà là, égal : $3"; return 0; } || arret "$3 existe et diffère du blob"; fi
    mkdir -p "$DEPOT/$(dirname "$3")"; git -C "$1" show "$2:$3" > "$DEPOT/$3" || arret "extraction de $3"; }
[ "$(git ls-remote "$DEPOT_URL" "refs/heads/$B7B" | cut -f1)" = "$TETE_7B" ] || arret "tête de $B7B"
[ -e "$CLONE7B" ] || git clone -q --filter=blob:none --no-checkout --depth 1 --single-branch --branch "$B7B" "$DEPOT_URL" "$CLONE7B" || arret "dépôt jetable de 7b"
for f in diag/$R6/lecture-cout-t06.json diag/$R6/episodes-t06.json runs/$R6/manifeste.json donnees/$R6/mesures-t06.npz donnees/$R6/textes-actions-t06.jsonl; do
    place "$CLONE7B" "$TETE_7B" "$f"; place "$CLONE7B" "$TETE_7B" "$f.sha256"
    (cd "$DEPOT/$(dirname "$f")" && sha256sum -c --quiet "$(basename "$f").sha256") || arret "compagnon de $f"; done
[ "$(git ls-remote "$DEPOT_URL" "refs/heads/$BEA" | cut -f1)" = "$TETE_EA" ] || arret "tête de $BEA"
[ -e "$CLONEEA" ] || git clone -q --filter=blob:none --no-checkout --depth 1 --single-branch --branch "$BEA" "$DEPOT_URL" "$CLONEEA" || arret "dépôt jetable de l'étape A"
for f in runs/$R7/manifeste.json diag/$R7/sondes-t07.json; do
    place "$CLONEEA" "$TETE_EA" "$f"; place "$CLONEEA" "$TETE_EA" "$f.sha256"
    (cd "$DEPOT/$(dirname "$f")" && sha256sum -c --quiet "$(basename "$f").sha256") || arret "compagnon de $f"; done
S=donnees/$R7/scores-actions-t07.npz; place "$CLONEEA" "$TETE_EA" "$S.sha256"
if [ -e "$DEPOT/$S" ] && [ "$(sha256sum "$DEPOT/$S" | cut -d' ' -f1)" = "$H_SCORES" ]; then echo "scores déjà recomposés, égaux à la ligne SCORES-T07"
else
    rm -f -- "$DEPOT/$S"; mkdir -p "$MORCEAUX"
    for g in $(git -C "$CLONEEA" ls-tree --name-only "$TETE_EA" "donnees/$R7/" | grep -E '/scores-actions-t07\.npz\.morceau(x\.json|-[0-9]{3})(\.sha256)?$'); do
        git -C "$CLONEEA" show "$TETE_EA:$g" > "$MORCEAUX/$(basename "$g")" || arret "extraction de $g"; done
    python3 -I -B - "$MORCEAUX" <<'FIN' || arret "morceaux de scores-actions-t07.npz"
import hashlib, json, pathlib, sys
d = pathlib.Path(sys.argv[1]); m = json.loads((d / "scores-actions-t07.npz.morceaux.json").read_text(encoding="utf-8"))
noms = sorted(p.name for p in d.glob("scores-actions-t07.npz.morceau-[0-9][0-9][0-9]"))
assert [pathlib.Path(x["fichier"]).name for x in m["morceaux"]] == noms, "morceaux nommés ≠ morceaux présents"
for x in m["morceaux"]:
    p = d / pathlib.Path(x["fichier"]).name; h = hashlib.sha256(p.read_bytes()).hexdigest()
    assert h == x["sha256"] == (d / (p.name + ".sha256")).read_text(encoding="utf-8").split()[0], f"empreinte de {p.name}"
    assert p.stat().st_size == x["octets"], f"taille de {p.name}"
assert sum(x["octets"] for x in m["morceaux"]) == m["octets"], "somme des tailles"
print(f"{len(noms)} morceaux conformes, {m['octets']} octets")
FIN
    cat "$MORCEAUX"/scores-actions-t07.npz.morceau-[0-9][0-9][0-9] > "$DEPOT/$S" || arret "recomposition"
    (cd "$DEPOT/donnees/$R7" && sha256sum -c --quiet scores-actions-t07.npz.sha256) || arret "recomposition : empreinte autre que le compagnon"
fi
[ "$(sha256sum "$DEPOT/$S" | cut -d' ' -f1)" = "$H_SCORES" ] && echo "scores égaux à la ligne SCORES-T07" || arret "scores autres que la ligne SCORES-T07"
[ "$(sha256sum "$DEPOT/diag/$R7/sondes-t07.json" | cut -d' ' -f1)" = "$H_SONDES" ] && echo "sondes-t07.json égal à la ligne SONDES-T07" || arret "sondes-t07.json autre"
IS=$(grep '^| ISSUE-MOTS-ET-COUT-T06 |' registres/scellements-v1.md | cut -d'|' -f4 | tr -d ' ')
if [ ! -e "$DEPOT/$IS" ] && [ "$BR_P" != main ]; then
    git fetch --no-tags -q origin "+refs/heads/$BR_P:refs/remotes/origin/$BR_P" || arret "récupération de $BR_P"
    place . "refs/remotes/origin/$BR_P" "$IS"; place . "refs/remotes/origin/$BR_P" "$IS.sha256"; fi
(cd "$DEPOT/$(dirname "$IS")" && sha256sum -c --quiet "$(basename "$IS").sha256") && echo "fichier « mots et coût » présent, compagnon égal" || arret "fichier « mots et coût »"
git status --porcelain --untracked-files=no | grep -q . && arret "un fichier suivi a changé"
echo "données placées (non suivies, jamais commitées)"
# attendu : compagnons « OK » (silencieux) ; « 3 morceaux conformes, 132091350 octets » (ou « déjà recomposés ») ; scores et sondes égaux
# aux lignes ; fichier « mots et coût » présent ; aucun « ARRÊT »
```

### Bloc C3 — contrôle à blanc complet, garde du module comprise (section 9)

```bash
. "$HOME/bac-etape-b-compte-3-v2/variables-v2.sh" || exit 1
cd "$BAC"
[ "$(PYTHONPATH="$WT_C7/src" "$PYC" -B -m controle_ia.t07.lecture_v4 empreinte-config "$CONFIG_T07")" = "$H_CONFIG_CANON" ] \
    && echo "configuration v8 : empreinte canonique conforme" || arret "empreinte canonique de la configuration"
C="$BAC/copie-blanc-c3-$(date -u +%Y%m%dT%H%M%SZ)"
PYTHONPATH="$WT_C7/src" "$PYC" -B "$ICI/controle_a_blanc_etape_b_compte_3_v2.py" --racine "$DEPOT" --registre "$DEPOT/registres/scellements-v1.md" \
    --config "$CONFIG_T07" --registre-bbis "$DEPOT/$REGISTRE_BBIS" --cle-bbis "$CLE_BBIS" --mode avant-etape-b --chaine --dossier-copie "$C"; K=$?; echo "code $K"
[ "$K" = 0 ] || arret "contrôle à blanc non conforme : aucune étape B ; la mère lève la cause"
# attendu : manquantes aucune ; aucun refus ; garde adaptée sans code ; CODE-T07 : 26 fichiers conformes ; données « conforme » ;
# condition d'ordre B bis REMPLIE ; « 9. garde d'ouverture du module … : AUTORISÉE » ; « TOUT CONFORME » ; « code 0 »
```

### Bloc C4a — l'unique appel, détaché (jamais relancé)

```bash
. "$HOME/bac-etape-b-compte-3-v2/variables-v2.sh" || exit 1
[ ! -e "$BAC/appel-etape-b-lance-v2.txt" ] || arret "l'étape B a déjà été lancée : aucun second appel ; joue C4-attente puis C4b"
cd "$DEPOT"; [ "$(git rev-parse --abbrev-ref HEAD)" = "$BR_B" ] || arret "tu n'es pas sur $BR_B"
mkdir -p "$ESPACE_B/pieces" "$ESPACE_B/verdict-ferme"; wc -l < registres/scellements-v1.md.ouvertures.md > "$BAC/lignes-journal-avant-v2.txt"
cd "$BAC"
PYTHONPATH="$WT_C7/src" "$PYC" -B "$ICI/controle_a_blanc_etape_b_compte_3_v2.py" --racine "$DEPOT" --registre "$DEPOT/registres/scellements-v1.md" \
    --config "$CONFIG_T07" --registre-bbis "$DEPOT/$REGISTRE_BBIS" --cle-bbis "$CLE_BBIS" --mode avant-etape-b > "$BAC/blanc-avant-appel-v2.txt" 2>&1 \
    || { tail -n 20 "$BAC/blanc-avant-appel-v2.txt"; arret "contrôle à blanc juste avant l'appel : aucune étape B"; }
grep -q "TOUT CONFORME" "$BAC/blanc-avant-appel-v2.txt" && echo "contrôle à blanc juste avant l'appel : tout conforme" || arret "contrôle à blanc"
date -u +%s > "$BAC/appel-etape-b-lance-v2.txt"          # posé AVANT l'appel : aucun second appel possible
setsid nohup bash -c 'cd "$1" && PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$2" "$3" -B -m "$4" etape-b "$5" "$6" "$7" "$8" --registre "$9" > "${10}" 2>&1; echo $? > "${11}.tmp" && mv "${11}.tmp" "${11}"' \
    _ "$BAC" "$PYTHONPATH_ETAPE_B" "$PYC" "$MODULE_ETAPE_B" "$DEPOT" "$R6" "$R7" "$CONFIG_T07" "$DEPOT/registres/scellements-v1.md" \
    "$ESPACE_B/sortie-etape-b-v2.txt" "$BAC/code-etape-b-v2.txt" > /dev/null 2>&1 < /dev/null &
echo $! > "$BAC/pid-etape-b-v2.txt"
date -u +"étape B lancée, détachée, à %Y-%m-%dT%H:%M:%SZ"; echo "identifiant de processus : $(cat "$BAC/pid-etape-b-v2.txt") ; joue maintenant C4-attente"
# attendu : « contrôle à blanc … tout conforme » ; « étape B lancée … » ; l'identifiant de processus. Sortie du module jamais affichée.
```

### Bloc C4-attente — relevé court (relançable autant de fois qu'il faut)

```bash
. "$HOME/bac-etape-b-compte-3-v2/variables-v2.sh" || exit 1
[ -e "$BAC/appel-etape-b-lance-v2.txt" ] || arret "C4a non joué"
D=$(( $(date -u +%s) - $(cat "$BAC/appel-etape-b-lance-v2.txt") ))
if [ -e "$BAC/code-etape-b-v2.txt" ]; then echo "ÉTAPE B FINIE : code $(cat "$BAC/code-etape-b-v2.txt") après $D s ; joue C4b"
elif kill -0 "$(cat "$BAC/pid-etape-b-v2.txt")" 2>/dev/null; then
    echo "étape B en cours depuis $D s (processus vivant) ; rejoue ce bloc dans quelques minutes"
    [ "$D" -le "$BORNE_S" ] || echo "BORNE DÉPASSÉE ($BORNE_S s) : rapport à la mère, nœud de Lazar ; le processus n'est pas arrêté"
else
    echo "ARRÊT : processus disparu sans code de sortie après $D s ; noms sous diag/$R7 : $(ls "$DEPOT/diag/$R7" 2>/dev/null | tr '\n' ' ') ;"\
         "lignes du journal : $(cat "$BAC/lignes-journal-avant-v2.txt") avant, $(wc -l < "$DEPOT/registres/scellements-v1.md.ouvertures.md") maintenant ; rien n'est relancé ; nœud"
    exit 1
fi
```

### Bloc C4b — journal et sortie commités et poussés (relançable seul)

```bash
. "$HOME/bac-etape-b-compte-3-v2/variables-v2.sh" || exit 1
[ -e "$BAC/code-etape-b-v2.txt" ] || arret "étape B pas finie (C4-attente)"
CODE=$(cat "$BAC/code-etape-b-v2.txt"); cd "$DEPOT"; [ "$(git rev-parse --abbrev-ref HEAD)" = "$BR_B" ] || arret "tu n'es pas sur $BR_B"
J=registres/scellements-v1.md.ouvertures.md
echo "code de l'étape B : $CODE ; lignes ajoutées au journal : $(( $(wc -l < "$J") - $(cat "$BAC/lignes-journal-avant-v2.txt") ))"
[ "$CODE" = 2 ] && { echo "ligne de refus :"; grep '^| REFUS-T07 |' "$J" | tail -n 1; }
if [ ! -e "$BAC/c-journal-b-v2.txt" ]; then
    git add -- "$J"; git diff --cached --name-only | grep -v -x -F "$J" && arret "index : autre chose que le journal"
    n=$(git diff --cached | grep -cE "$SECRETS"); [ "$n" = 0 ] || arret "garde des secrets : $n"
    if git diff --cached --quiet; then echo "aucune ligne neuve au journal" > "$BAC/c-journal-b-v2.txt"
    else git commit -q -m "T0.7, étape B : journal des ouvertures (code $CODE ; session hôte du compte 3)" || arret "commit du journal (relance C4b)"
         git rev-parse HEAD > "$BAC/c-journal-b-v2.txt"; fi; fi
if [ ! -e "$BAC/c-sortie-b-v2.txt" ]; then
    for f in "diag/$R7/lecture-t07.json" "diag/$R7/arret-etape-b.json"; do [ -e "$f" ] && git add -- "$f" "$f.sha256"; done
    git diff --cached --name-only | grep -v -E "^diag/$R7/(lecture-t07|arret-etape-b)\.json(\.sha256)?$" && arret "index : autre chose que la sortie du module"
    n=$(git diff --cached | grep -cE "$SECRETS"); [ "$n" = 0 ] || arret "garde des secrets : $n"
    if git diff --cached --quiet; then echo "aucune sortie du module" > "$BAC/c-sortie-b-v2.txt"
    else git commit -q -m "T0.7, étape B : sortie scellée du module (code $CODE)" || arret "commit de la sortie (relance C4b)"
         git rev-parse HEAD > "$BAC/c-sortie-b-v2.txt"; fi; fi
git push -q origin "refs/heads/$BR_B:refs/heads/$BR_B" || arret "poussée (relance C4b : il reprend à la poussée)"
git ls-remote origin "refs/heads/$BR_B"
for f in "diag/$R7/lecture-t07.json" "diag/$R7/arret-etape-b.json"; do if [ -e "$f" ]; then echo "$f : $(cut -d' ' -f1 "$f.sha256")"; fi; done
echo "C4b fait : journal $(cat "$BAC/c-journal-b-v2.txt") ; sortie $(cat "$BAC/c-sortie-b-v2.txt") ; poussé"
# attendu (code 0) : deux lignes neuves au journal ; deux commits poussés ; l'empreinte de lecture-t07.json. Code 2 : ligne REFUS-T07
# affichée, commitée, poussée ; arrêt ; relance de l'étape B seulement sur un mot écrit de la mère (nouvelle version de cette commande).
# Code 3 : arret-etape-b.json commité, poussé ; nœud de Lazar ; aucune relance.
```

### Bloc C5 — pièces du lecteur B, filtres de noms et de contenu, bordereau (code 0 seulement)

```bash
. "$HOME/bac-etape-b-compte-3-v2/variables-v2.sh" || exit 1
[ "$(cat "$BAC/code-etape-b-v2.txt")" = 0 ] || arret "étape B sans lecture : aucun lecteur"
[ ! -e "$ESPACE_B/bordereau-remise-v2.txt" ] || arret "bordereau déjà écrit"
P="$ESPACE_B/pieces"; rm -rf -- "${ESPACE_B:?}/pieces"; mkdir -p "$P"; cd "$DEPOT"   # relance avant le bordereau : pièces refaites de zéro
IS=$(grep '^| ISSUE-MOTS-ET-COUT-T06 |' registres/scellements-v1.md | cut -d'|' -f4 | tr -d ' ')
for f in prereg/T0.7-sondes-v0-v1.md prereg/T0.7-sondes-v0-v1-addendum-cache-motifs-v1.md prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json \
         prereg/T0.6-organismes-v0-v1.md prereg/T0.8-base-A-mots-et-cout-v1.md prereg/T0.7-consigne-audit-fuites-v1.md docs/decisions/decision-N-063-v2.md \
         docs/verdicts/verdict-P3-bis-v1-issue.json "$CONSIGNE_B" "diag/$R7/lecture-t07.json" "diag/$R7/sondes-t07.json" "runs/$R7/manifeste.json" "diag/$R7/audit-fuites-t07.json" "$IS"; do
    cp --parents "$f" "$f.sha256" "$P/" || arret "copie de $f"
    [ "$(cut -d' ' -f1 "$P/$f.sha256")" = "$(sha256sum "$P/$f" | cut -d' ' -f1)" ] || arret "compagnon de $f"; done
[ "$(sha256sum "$P/$CONSIGNE_B" | cut -d' ' -f1)" = "$EMPREINTE_CONSIGNE_B" ] || arret "consigne du lecteur B autre que l'empreinte"
C=$(cat "$BAC/c-main-b-v2.txt")
{ echo "# Extrait des registres pour le lecteur de l'étape B (v2)"; echo; echo "Commit de main : $C ; journal de la branche : $(cat "$BAC/c-journal-b-v2.txt")."
  echo; echo "## registres/scellements-v1.md"; grep -n '^| ' registres/scellements-v1.md
  echo; echo "## registres/scellements-v1.md.ouvertures.md (lignes de l'étape B)"; grep -n 'etape-B\|scores-t07' registres/scellements-v1.md.ouvertures.md
  echo; echo "## registres/decisions.md (état de BA-L2, ligne dédiée)"; git show "$C:registres/decisions.md" | grep -n "^| $R_BA_L2 |"
} > "$P/extrait-registres-etape-b-v2.md"
n=$(grep -c -i -E "$INTERDITS_CONTENU_B" "$P/extrait-registres-etape-b-v2.md"); [ "$n" = 0 ] || arret "contenu de l'étape B bis dans l'extrait ($n ligne(s)) : rien n'est remis"
(cd "$P" && find . -type f -print0 | sort -z | xargs -0 sha256sum) > "$ESPACE_B/bordereau-remise-v2.tmp"
n=$(cut -c67- "$ESPACE_B/bordereau-remise-v2.tmp" | grep -c -i -E "$INTERDITS_NOMS_B"); [ "$n" = 0 ] || arret "$n nom(s) interdit(s) parmi les pièces : rien n'est remis"
mv "$ESPACE_B/bordereau-remise-v2.tmp" "$ESPACE_B/bordereau-remise-v2.txt"
PYTHONPATH="$WT_C7/src" "$PYC" -B -m controle_ia.scellement sceller "$ESPACE_B/bordereau-remise-v2.txt" || arret "sceau du bordereau"
echo "conforme : aucun nom ni contenu de l'étape B bis ; pièces : $(wc -l < "$ESPACE_B/bordereau-remise-v2.txt") fichiers ; bordereau $(cut -d' ' -f1 "$ESPACE_B/bordereau-remise-v2.txt.sha256")"
# attendu : quatorze fichiers et leurs compagnons conformes, plus l'extrait (29 fichiers) ; « conforme : … » ; l'empreinte du bordereau
```

### Bloc C6 — message de remise et création du lecteur B

Avant : vérifie que ton outil peut créer un sous-agent du **modèle C** ; sinon **arrêt, nœud de Lazar**.

```bash
. "$HOME/bac-etape-b-compte-3-v2/variables-v2.sh" || exit 1
[ ! -e "$BAC/message-remise-b-v2.txt" ] || arret "message déjà écrit"
cat > "$BAC/message-remise-b-gabarit-v2.txt" <<'FIN'
Interdits permanents (brief du compte 3, section 6), en plus de ceux de ta consigne : aucune dépense ; aucune valeur de clé (jamais env, printenv, set sans argument, export -p, /proc/*/environ) ; jamais diag/*/lecture-sondes-t06.json, resume.json de 7b, les activations, les adaptateurs, la lecture B de 7a, donnees/lecture-b-7a-quarantaine-v1, donnees/mesure-unanime-v15-sortie-v1, essai/t06-explo-v3, aucun diag/ ni runs/ de 7a, l'étiqueteur, scripts/extraire_mesures_epreuve_t06_v1.py, la branche calcul/p3bis-reel-v2 ; jamais donnees/bras-attaque*, donnees/mode-tenu-a-l-ecart*, docs/notes/bras-attaque/, registres/index-bras-attaque*, anteriorite-bras-informe*, la branche claude/compassionate-meitner-d4ryyk ; rien de l'étape B bis ; aucune recherche récursive hors de l'espace donné ; jamais d'heure écrite à la main (date -u) ; aucun contact extérieur ; un refus de permission ou d'un classifieur : arrêt, tu le rapportes tel quel.
Tu es le lecteur neuf du verdict de l'étape B de T0.7 (critère 3 de G0 ; règle R13). Lis d'abord ta consigne, et elle seule fixe ce que tu lis et écris : <<ESPACE>>/pieces/<<CONSIGNE>> (empreinte <<EMPREINTE_CONSIGNE>>, égale à son compagnon : vérifie-la avant lecture).
- Runs : 20261111-151701-t06-reel (7b) et 20261114-001352-t07-lecture-reel (T0.7). Pièces : <<ESPACE>>/pieces (bordereau <<ESPACE>>/bordereau-remise-v2.txt, empreinte <<EMPREINTE_BORDEREAU>>, scellé). Tu n'écris que dans <<ESPACE>>/verdict-ferme.
- Interpréteur : <<PY>>.
- Avant tout, recopie le texte exact de ce message, tel que tu l'as reçu, dans <<ESPACE>>/verdict-ferme/verdict-T0.7-etape-B-v1-message-recu-v1.txt ; ton rapport final en donne l'empreinte sha256.
- Ton modèle s'écrit au verdict sans aucun identifiant : « <<NOTE_MODELE>> » (« modèle A » = celui des auteurs de T0.7).
- Aucun nombre ni aucune issue hors des fichiers scellés du verdict : ton rapport final suit la section « Ce que tu rends » de ta consigne, mot pour mot.
Tu ne lis rien d'autre (ni le dépôt, ni les scores, ni rien de l'étape B bis).
FIN
ESPACE="$ESPACE_B" BORDEREAU="$(cut -d' ' -f1 "$ESPACE_B/bordereau-remise-v2.txt.sha256")" PYV="$PYC" NOTE="$NOTE_MODELE" CONS="$CONSIGNE_B" ECONS="$EMPREINTE_CONSIGNE_B" \
  python3 -I -B - "$BAC/message-remise-b-gabarit-v2.txt" "$BAC/message-remise-b-v2.txt" <<'FIN' || arret "message de remise B"
import os, sys
t = open(sys.argv[1], encoding="utf-8").read()
for m, v in (("<<ESPACE>>", "ESPACE"), ("<<EMPREINTE_BORDEREAU>>", "BORDEREAU"), ("<<PY>>", "PYV"), ("<<NOTE_MODELE>>", "NOTE"),
             ("<<CONSIGNE>>", "CONS"), ("<<EMPREINTE_CONSIGNE>>", "ECONS")):
    t = t.replace(m, os.environ[v])
if "<<" in t or ">>" in t:
    sys.exit("marqueur resté dans le message")
with open(sys.argv[2], "x", encoding="utf-8") as f:
    f.write(t)
print("message écrit, aucun marqueur restant")
FIN
cd "$DEPOT" && PYTHONPATH="$WT_C7/src" "$PYC" -B -m controle_ia.scellement sceller "$BAC/message-remise-b-v2.txt" || arret "sceau du message B"
cat "$BAC/message-remise-b-v2.txt"
```

**Création du lecteur B** : un sous-agent neuf, sans contexte hérité, du modèle C, jamais le lecteur A ni un lecteur de B bis ; seul message :
le texte affiché, copié tel quel. Tu attends son rapport final sans rien lire de l'espace fermé.

### Bloc C7 — après le verdict B : message reçu attesté, copie, sceaux, commit, poussée (relançable)

```bash
. "$HOME/bac-etape-b-compte-3-v2/variables-v2.sh" || exit 1
V="$ESPACE_B/verdict-ferme"; cd "$V" || arret "verdict-ferme absent"
ls -1A
[ -z "$(find . -mindepth 1 -type d)" ] || arret "dossier inattendu dans verdict-ferme : rien n'est copié"
n=$(ls -1A | grep -v -E '^verdict-T0\.7-etape-B-v1(\.md|-issue\.json|-[a-z0-9-]+-v[0-9]+\.(py|txt|json|md))(\.sha256)?$' | wc -l)
[ "$n" = 0 ] || arret "$n fichier(s) de nom inattendu (archives comprises) : rien n'est copié"
[ -f verdict-T0.7-etape-B-v1.md ] || arret "verdict en prose absent"
M=verdict-T0.7-etape-B-v1-message-recu-v1.txt; [ -f "$M" ] || arret "message reçu non recopié par le lecteur : rien n'est commité ; nœud"
python3 -I -B -c 'import sys; a=open(sys.argv[1],encoding="utf-8").read().rstrip("\n"); b=open(sys.argv[2],encoding="utf-8").read().rstrip("\n"); sys.exit(0 if a == b else 1)' \
    "$M" "$BAC/message-remise-b-v2.txt" && echo "message reçu égal au message scellé" || arret "message reçu différent : rien n'est commité ; nœud"
cd "$DEPOT"; [ "$(git rev-parse --abbrev-ref HEAD)" = "$BR_B" ] || arret "tu n'es pas sur $BR_B"
if [ -e "$BAC/c-verdict-b-v2.txt" ]; then echo "verdict B déjà commité"; else
    mkdir -p docs/verdicts
    for f in $(ls -1A "$V" | grep -v '\.sha256$'); do
        [ -e "docs/verdicts/$f" ] && { cmp -s "$V/$f" "docs/verdicts/$f" || arret "docs/verdicts/$f existe et diffère"; } \
            || { cp "$V/$f" "docs/verdicts/$f" && cmp -s "$V/$f" "docs/verdicts/$f" || arret "copie de $f"; }
        PYTHONPATH="$WT_C7/src" "$PYC" -B -m controle_ia.scellement sceller "docs/verdicts/$f" || arret "sceau de $f"; done
    git add -- docs/verdicts/verdict-T0.7-etape-B-v1*
    git diff --cached --name-only | grep -v -E '^docs/verdicts/verdict-T0\.7-etape-B-v1[^/]*$' && arret "index : autre chose que les fichiers du verdict"
    n=$(git diff --cached | grep -cE "$SECRETS"); [ "$n" = 0 ] || arret "garde des secrets : $n"
    git commit -q -m "T0.7, étape B : verdict du lecteur neuf, fichiers scellés (session hôte du compte 3)" || arret "commit (relance ce bloc)"
    git rev-parse HEAD > "$BAC/c-verdict-b-v2.txt"; fi
git push -q origin "refs/heads/$BR_B:refs/heads/$BR_B" || arret "poussée du verdict B (relance ce bloc)"
echo "commit du verdict B : $(cat "$BAC/c-verdict-b-v2.txt")"; git ls-remote origin "refs/heads/$BR_B"
# attendu : « message reçu égal … » ; copies égales et scellées ; commit poussé
```

### Bloc F-C — journal provisoire (sans issue ni nombre), passation, nettoyage

```bash
. "$HOME/bac-etape-b-compte-3-v2/variables-v2.sh" || exit 1
RAPPORT=$(cat <<'FIN'
<rapport final du lecteur B, tel quel, à la place de cette ligne>
FIN
)
CROCHET='<bloquée | passée>'; MODELES='lecteur : modèle C ; session hôte : <modèle A | modèle C> ; identités dites en conversation seulement'
case "$RAPPORT$CROCHET$MODELES" in *'<rapport final'*|*'<bloquée | passée>'*|*'<modèle A | modèle C>'*) arret "variables de tête non remplies";; esac
lire() { cat "$1" 2>/dev/null || echo "sans objet"; }
cd "$DEPOT"; [ "$(git rev-parse --abbrev-ref HEAD)" = "$BR_B" ] || arret "tu n'es pas sur $BR_B"
[ -e "$BAC/nom-provisoire-b-v2.txt" ] || echo "registres-provisoires/compte-3-phase-c-$(date -u +%Y-%m-%d-%H%M)-v2.md" > "$BAC/nom-provisoire-b-v2.txt"
N=$(cat "$BAC/nom-provisoire-b-v2.txt")
if [ ! -e "$BAC/c-provisoire-b-v2.txt" ]; then
printf '%s\n' "$RAPPORT" > "$BAC/rapport-lecteur-b-v2.txt"; mkdir -p registres-provisoires
{ echo "# Compte 3 — session hôte de l'étape B et de son lecteur — journal provisoire (v2)"; echo
  echo "Écrit le $(date -u +%Y-%m-%dT%H:%M:%SZ) (\`date -u\`) par la session \`$SESSION_C3\`, branche \`$BR_B\` ; identifiants provisoires P3C-…, à numéroter par la mère."; echo
  echo "- P3C-001 : commande phase C v4 depuis $(lire "$BAC/debut-v2.txt") ; épreuve du crochet : $CROCHET ; $MODELES ; liste \`$LISTE\` (\`$EMPREINTE_LISTE\`) : attestation conforme."
  echo "- P3C-002 : base main \`$(lire "$BAC/c-main-b-v2.txt")\` ; appel lancé à $(date -u -d "@$(lire "$BAC/appel-etape-b-lance-v2.txt")" +%Y-%m-%dT%H:%M:%SZ 2>/dev/null) ; code $(lire "$BAC/code-etape-b-v2.txt") ; journal \`$(lire "$BAC/c-journal-b-v2.txt")\` ; sortie \`$(lire "$BAC/c-sortie-b-v2.txt")\`."
  echo "- P3C-003 : bordereau \`$(cut -d' ' -f1 "$ESPACE_B/bordereau-remise-v2.txt.sha256" 2>/dev/null)\` ; message \`$(cut -d' ' -f1 "$BAC/message-remise-b-v2.txt.sha256" 2>/dev/null)\` (reçu égal) ; verdict \`$(lire "$BAC/c-verdict-b-v2.txt")\`."
  echo "- P3C-004 : rapport final du lecteur, seules les lignes STATUT, FICHIERS, DÉCLARATIONS et MESSAGE (le rapport entier est transmis à Lazar) :"
  grep -E '^(STATUT|FICHIERS|DÉCLARATIONS|MESSAGE)' "$BAC/rapport-lecteur-b-v2.txt" | sed 's/^/    /'
  echo "- P3C-005 : aucun résultat ouvert ; exclusions de la phase A, plus l'analyse du verdict B et tout rôle de lecteur de l'étape B bis."
} > "$N"
PYTHONPATH="$WT_C7/src" "$PYC" -B -m controle_ia.scellement sceller "$N" || arret "sceau (relance F-C)"
git add -- "$N" "$N.sha256"; [ "$(git diff --cached --name-only | grep -vc '^registres-provisoires/')" = 0 ] || arret "index : autre chose que registres-provisoires/"
n=$(git diff --cached | grep -cE "$SECRETS"); [ "$n" = 0 ] || arret "garde des secrets : $n"
git commit -q -m "Compte 3 : journal provisoire de la session hôte de l'étape B" || arret "commit (relance F-C)"
git rev-parse HEAD > "$BAC/c-provisoire-b-v2.txt"; fi
git push -q origin "refs/heads/$BR_B:refs/heads/$BR_B" || arret "poussée (relance F-C : il reprend à la poussée)"
echo "RENDU — branche $BR_B ; tête $(git rev-parse HEAD) ; journal provisoire $(cat "$BAC/c-provisoire-b-v2.txt")"; sha256sum "$N"
IS=$(grep '^| ISSUE-MOTS-ET-COUT-T06 |' registres/scellements-v1.md | cut -d'|' -f4 | tr -d ' ')
for f in diag/$R6/lecture-cout-t06.json diag/$R6/episodes-t06.json runs/$R6/manifeste.json donnees/$R6/mesures-t06.npz donnees/$R6/textes-actions-t06.jsonl \
         runs/$R7/manifeste.json diag/$R7/sondes-t07.json donnees/$R7/scores-actions-t07.npz $IS; do
    git ls-files --error-unmatch -- "$f" >/dev/null 2>&1 || rm -f -- "$f" "$f.sha256"; done
if [ -d "$WT_C7" ]; then git worktree remove "$WT_C7" || arret "arborescence C7 non retirée : rapport à la mère"; fi
echo "données placées retirées ; arborescence C7 retirée"
[ -z "$(git status --porcelain --untracked-files=no)" ] && echo "dépôt propre" || arret "dépôt non propre après nettoyage (git status) : rapport à la mère"
# relançable : le nom du journal provisoire et son commit sont gardés au bac ; une relance reprend à la poussée, puis au nettoyage
```

## 12. Ce que tu ne fais jamais ici

Relancer C4a ; afficher la sortie du module ; arrêter un processus ; ouvrir une pièce ; remettre une pièce de B bis ; pousser sur `main` ;
écrire un identifiant de modèle ; prendre un lecteur d'un autre modèle que C ; lancer l'étape B depuis `main` ou par `lecture_v3`.

## 13. Rendu à Lazar (il transmet à la mère)

1. Une à trois lignes : « Étape B appelée une fois (détachée), code <n> après <s> s ; verdict du lecteur neuf (modèle C) scellé et poussé sur
   `verdict/t07-etape-b-compte-3-v1` ; rien d'autre lu. » — ou le bloc et le motif d'un arrêt.
2. Le rapport final du lecteur B en entier, pour Lazar. 3. Pour la mère : sortie « RENDU », commits (`c-*-v2.txt`), empreintes.

## 14. Ce qui arrête tout

- Tout « ARRÊT » d'un bloc. Avant C4a, rien d'irréversible (hors le nom de la branche poussée) : rapport (bloc et motif).
- **L'outil rend la main pendant ou après C4a** : C4-attente, puis C4b ; jamais C4a. Processus disparu sans code : C4-attente imprime noms,
  nombre de lignes du journal, et s'arrête : nœud ; rien n'est relancé. Borne de 60 minutes dépassée : nœud ; le processus continue.
- Code 2 : refus (attente) ; relance seulement par une version nouvelle de cette commande, sur un mot écrit de la mère. Code 3 : nœud, aucune relance.
- Pas de sous-agent du modèle C ; rapport « arrêt » du lecteur ; message reçu absent ou différent : rien n'est commité ; nœud.
- Refus de permission, du crochet, d'un classifieur ; poussée refusée : arrêt, rapport, aucun contournement.

## 15. Ce que fait la mère (pour mémoire ; tu ne le fais pas)

**Bloc M — avant de remettre cette commande, après les lignes `LECTURE-T08-BASE-A` puis `ISSUE-MOTS-ET-COUT-T06` : la mère lit le seul état
de BA-L2** (décision de Lazar R-2741, N-C ; T0.7 l. 2183). Dans son conteneur, depuis le dossier du dépôt à jour, en un seul appel de son
outil (tout « ARRÊT » sort de l'appel sans rien afficher d'autre que son motif) :

```bash
export LC_ALL=C.UTF-8; date -u +%Y-%m-%dT%H:%M:%SZ
BRP='<branche qui porte base-a-t08.json>'; W="$HOME/bloc-m-ba-l2-$(date -u +%Y%m%dT%H%M%SZ)"; mkdir -p "$W/racine/registres"
cp registres/scellements-v1.md "$W/racine/registres/"
REL=$(grep '^| LECTURE-T08-BASE-A |' registres/scellements-v1.md | cut -d'|' -f4 | tr -d ' ')
[ "$(printf '%s\n' "$REL" | grep -c .)" = 1 ] || { echo "ARRÊT : pas exactement une ligne LECTURE-T08-BASE-A au registre (main à jour ?)"; exit 1; }
git clone -q --filter=blob:none --no-checkout --depth 1 --single-branch --branch "$BRP" https://github.com/lciric/controle-ia-travail.git "$W/clone" \
    || { echo "ARRÊT : dépôt jetable de la pièce (branche $BRP)"; exit 1; }
mkdir -p "$W/racine/$(dirname "$REL")"
for f in "$REL" "$REL.sha256"; do git -C "$W/clone" show "HEAD:$f" > "$W/racine/$f" || { echo "ARRÊT : extraction de $f"; exit 1; }; done
python3 -I -B docs/procedures/lecture-7b-etape-b-compte-3-v1/lecture_etat_ba_l2_mere_v1.py --racine "$W/racine" --registre "$W/racine/registres/scellements-v1.md"; echo "code $?"
# n'affiche que « ÉTAT BA-L2 : ne s'applique pas » (code 0), « … s'applique … » (code 3 : mot de Lazar avant l'étape B) ou « … illisible … »
# (code 2). La mère écrit alors une ligne du registre des décisions **dédiée** (état seul, ou mot de Lazar ; aucun mot de l'étape B bis) : c'est
# `<<R_BA_L2>>`. Puis elle efface `$W` par son chemin exact. La forme `lignes.BA-L2.s_applique` est à fixer dans la consigne du développeur de
# la pièce « mots et coût » (sinon `--cle-json` du chemin qu'elle aura fixé).
```

Ensuite : (1) recopie dans `main` le seul commit du journal (`registres/scellements-v1.md.ouvertures.md`, même blob) **avant toute autre
écriture dans ce journal** ; (2) recopie les fichiers du verdict B, rescelle ; (3) garde `lecture-t07.json` sur la branche, avec le chemin et
l'empreinte du manifeste de T0.7 de `donnees/t07-etape-a-v1` (`runs/20261114-001352-t07-lecture-reel/manifeste.json`), nécessaire à
`verifier_resultat` ; (4) liste « qui a lu quoi » (hôte ; lecteur B : pièces du bordereau) ; verdict soumis à Lazar ; (5) **rien de cette
branche n'entre dans un espace de l'étape B bis avant le verdict scellé de B bis** ; la table conjointe B × B bis se lit après les deux.

## Annexe — essais (règle R5)

- Contrôle à blanc v2 : 19 sur 19 (section 9 sur racine au format réel, artefacts de CL3-06 et de CL3-14) ; essai v1 rejoué sur le v2 :
  28 sur 28. Attestation v3 : 17 sur 17. État BA-L2 : 10 sur 10. Durée : `mesure-duree-etape-b-sortie-v1.txt`.
- **Répétition de bout en bout** (CL3-07) : `repetition_phase_c_jouet_v4.sh`, sortie `repetition-phase-c-jouet-v4-sortie-brouillon1-v1.txt`
  (bordereau de 29 fichiers, `sondes-t07.json` et son compagnon compris ; version 3 : 53 sur 53, gardée) : blocs 0b-C,
  1C, 2C, C0, C1a, C1, C2, C3, C4a, C4-attente, C4b, C5, C6, C7, F-C et bloc M joués sur dépôts jouets, avec un module d'étape B **jouet** qui
  appelle la vraie garde `lecture_v4.ouvrir` du code de C7 (journal écrit par elle), attend, puis écrit `lecture-t07.json` par la vraie
  fonction `ecrire_resultat` ; artefacts : C4a relancé, poussée refusée puis C4b relancé, poussée refusée puis F-C relancé, fichier suivi
  modifié avant une relance de F-C, code 2 sur une seconde passe, bloc M sur une branche absente et sur un registre sans
  `LECTURE-T08-BASE-A` ; liste dont la cellule de l'hôte diffère (2C) ; décisions mêlée, sans BA-L2, absente (C0) ; pièce au nom
  interdit et contenu de B bis dans l'extrait, puis C5 relancé (C5) ; message reçu différent et archive (C7). Limite : le calcul de
  l'étape B lui-même n'est pas rejoué sur des données valides (mesuré à part, CL3-05) ; transport local.
