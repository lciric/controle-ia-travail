#!/usr/bin/env bash
# Répétition locale de la machine du jeu relancé de l'idée 1.1, v2 (procédure du même dossier, v5). Aucun appel au loueur,
# aucune machine, aucune dépense, aucun réseau : dépôt distant jouet en file://, loueur simulé (faux curl qui note l'heure,
# la méthode et l'adresse, jamais l'en-tête), jeu factice (jeu_factice_idee_1_1_v1.py, inchangé), clés factices dont on
# prouve qu'elles ne s'affichent ni ne se poussent. Chaque garde sur un cas sain et sur un artefact (R5).
# v2 = les 110 cas de la v1 sur le lanceur v2 et l'amorce v2, plus la reprise de la poussée des sorties (contre-lecture,
#   tour 1, M1) : un crochet « pre-receive » du dépôt jouet refuse les poussées qui portent des sorties (runs/) sur deux
#   branches seulement : -v15 (refusée trois fois puis acceptée) et -v16 (jamais acceptée).
#   bash repetition_machine_jeu_idee_1_1_v2.sh DOSSIER_NEUF [DEPOT_PRINCIPAL]
# DEPOT_PRINCIPAL (défaut /home/user/controle-ia-travail) n'est que lu : `git show HEAD:<chemin>` de trois fichiers et de leurs
# compagnons (texte, addendum d'empreintes, essai du § 6 point 3) et l'interpréteur .venv/bin/python (contrôle des versions).
# Code 0 : tous les cas attendus ; 1 : au moins un écart (ligne « ECART »).
set -uo pipefail
W="${1:?DOSSIER_NEUF}"; MAIN="${2:-/home/user/controle-ia-travail}"
ICI="$(cd "$(dirname "$0")" && pwd)"
LAN="$ICI/lancer_jeu_idee_1_1_machine_v2.sh"; AMO="$ICI/amorce_jeu_idee_1_1_v2.sh"; FAC="$ICI/jeu_factice_idee_1_1_v1.py"
PYS="$MAIN/.venv/bin/python"
[ ! -e "$W" ] || { echo "REFUS : $W existe déjà (R12)"; exit 2; }
mkdir -p "$W/bin" && W="$(cd "$W" && pwd)"
export TMPDIR="$W/tmp"; mkdir -p "$TMPDIR"
export PYTHON_JEU11="$PYS" VASTAI_JEU=/home/user/vastai-env/bin/vastai GIT_CONFIG_GLOBAL="$W/gitconfig" GIT_CONFIG_NOSYSTEM=1
git config --file "$W/gitconfig" user.name "repetition" && git config --file "$W/gitconfig" user.email "repetition@invalid" \
    && git config --file "$W/gitconfig" init.defaultBranch main && git config --file "$W/gitconfig" protocol.file.allow always
CLE=cle-factice-NE-PAS-AFFICHER-7c1e; JETON=jeton-factice-NE-PAS-AFFICHER-93ad
NB=0; NE=0
ok() { NB=$((NB + 1)); echo "OK    $*"; }
ecart() { NB=$((NB + 1)); NE=$((NE + 1)); echo "ECART $*"; }
attendu() {  # $1 nom ; $2 code attendu ; $3 code lu ; $4 motif attendu dans $5 (fichier) ou vide
    if [ "$3" != "$2" ]; then ecart "$1 : code $3, attendu $2"; [ -n "${5:-}" ] && tail -n 5 "$5" | sed 's/^/        | /'; return; fi
    if [ -n "${4:-}" ] && ! grep -q -- "$4" "$5"; then ecart "$1 : motif « $4 » absent"; tail -n 5 "$5" | sed 's/^/        | /'; return; fi
    ok "$1 (code $3${4:+, « $4 »})"; }
echo "répétition de la machine du jeu de l'idée 1.1, v2 : début $(date -u +%FT%TZ) ; dossier $W"
echo "empreintes : lanceur $(sha256sum < "$LAN" | cut -c1-16) ; amorce $(sha256sum < "$AMO" | cut -c1-16) ; garde $(sha256sum < "$ICI/garde_machine_jeu_idee_1_1_v1.py" | cut -c1-16) ; jeu factice $(sha256sum < "$FAC" | cut -c1-16)"
# ---------------------------------------------------------------------------------------------------------- outils simulés
cat > "$W/bin/curl-factice" <<EOF
#!/usr/bin/env bash
# loueur simulé : note la méthode et l'adresse seulement (jamais l'en-tête), rend 200
m=GET; u=""; while [ "\$#" -gt 0 ]; do case "\$1" in -X) m="\$2"; shift;; http*) u="\$1";; esac; shift; done
printf '%s %s %s %s\n' "\$(date -u +%T)" "\$(date +%s)" "\$m" "\$u" >> "$W/api.log"; printf 200
EOF
cat > "$W/bin/python-fausses-versions" <<'EOF'
#!/usr/bin/env bash
case "$*" in *pytest*) echo 9.1.1;; *numpy*scipy*) echo "3.13.18 2.5.3 1.17.1";; esac
EOF
chmod +x "$W/bin/curl-factice" "$W/bin/python-fausses-versions"
# ---------------------------------------------------------------------------------------------------------- dépôt jouet
NU="$W/distant/lciric/controle-ia-travail.git"; URL="file://$NU"; FAB="$W/fabrique"
git init -q --bare "$NU" && git init -q -b main "$FAB" || { echo "dépôt jouet impossible"; exit 1; }
for p in prereg/organisme-idee-1-1-poids-du-nul-v2.md prereg/organisme-idee-1-1-poids-du-nul-v2-addendum-empreintes-v1.md \
         docs/notes/organisme-idees-juge-v1/correction-poids-v1/projection/essai_projection_cas_v1.py; do
    for q in "$p" "$p.sha256"; do mkdir -p "$FAB/$(dirname "$q")"; git -C "$MAIN" show "HEAD:$q" > "$FAB/$q" || { echo "git show $q"; exit 1; }; done; done
REL=prereg/organisme-idee-1-1-poids-du-nul-v2-addendum-relance-v1.md
printf '# Addendum de relance FACTICE (répétition de la machine, aucune valeur)\n' > "$FAB/$REL"
( cd "$FAB/prereg" && sha256sum "$(basename "$REL")" > "$(basename "$REL").sha256" )
ER=$(sha256sum < "$FAB/$REL" | cut -d' ' -f1)
printf 'dépôt jouet de la répétition\n' > "$FAB/LISEZMOI.txt"
mkdir -p "$FAB/runs/autre-run" "$FAB/diag/organisme-idees-juge-v1/autre-run"; echo x > "$FAB/runs/autre-run/a.txt"; echo x > "$FAB/diag/organisme-idees-juge-v1/autre-run/a.txt"
cm() { git -C "$FAB" add -A && git -C "$FAB" commit -q -m "$1" && git -C "$FAB" rev-parse HEAD; }
C1=$(cm "jouet : état sain")
git -C "$FAB" checkout -q -b cote && echo cote > "$FAB/cote.txt" && CX=$(cm "jouet : commit hors de main") && git -C "$FAB" checkout -q main
echo "0000000000000000000000000000000000000000000000000000000000000000  $(basename "$REL")" > "$FAB/$REL.sha256"; C2=$(cm "jouet : compagnon de relance faux")
( cd "$FAB/prereg" && sha256sum "$(basename "$REL")" > "$(basename "$REL").sha256" )
mkdir -p "$FAB/runs/20261116-173428-idee-1-1-poids-du-nul-v5"; echo factice > "$FAB/runs/20261116-173428-idee-1-1-poids-du-nul-v5/manifeste.json"; C3=$(cm "jouet : sortie antérieure de ce jeu")
git -C "$FAB" rm -q -r "runs/20261116-173428-idee-1-1-poids-du-nul-v5" && echo "# altéré" >> "$FAB/docs/notes/organisme-idees-juge-v1/correction-poids-v1/projection/essai_projection_cas_v1.py"; C4=$(cm "jouet : essai altéré")
git -C "$FAB" push -q "$URL" main cote || { echo "poussée du jouet"; exit 1; }
# v2 : crochet du dépôt jouet ; refuse une poussée dont l'arbre porte runs/ (les sorties) sur -v15 (trois fois) et -v16 (toujours)
cat > "$NU/hooks/pre-receive" <<EOF
#!/usr/bin/env bash
r=0
while read -r ancien neuf ref; do
    case "\$ref" in
        refs/heads/calcul/idee-1-1-jeu-relance-v15) max=3; f="$W/refus-v15.n";;
        refs/heads/calcul/idee-1-1-jeu-relance-v16) max=-1; f="$W/refus-v16.n";;
        *) continue;;
    esac
    git ls-tree -r --name-only "\$neuf" 2> /dev/null | grep -q '^runs/' || continue
    n=\$(cat "\$f" 2> /dev/null || echo 0)
    if [ "\$max" = -1 ] || [ "\$n" -lt "\$max" ]; then echo \$((n + 1)) > "\$f"; echo "refus factice du dépôt jouet (\$((n + 1)))" >&2; r=1
    else echo x >> "\$f.acceptees"; fi
done
exit \$r
EOF
chmod +x "$NU/hooks/pre-receive"
echo "dépôt jouet : sain ${C1:0:12} ; hors de main ${CX:0:12} ; compagnon faux ${C2:0:12} ; sortie antérieure ${C3:0:12} ; essai altéré ${C4:0:12} ; addendum de relance factice ${ER:0:12}"
RS="$W/racine-session"; git clone -q "$URL" "$RS" || { echo "clone de la racine de session"; exit 1; }
mkdir -p "$RS/registres"
cat > "$RS/registres/go.md" <<'EOF'
| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |
|---|---|---|---|---|---|---|---|
| GO-2026-11-16-91 | 2026-11-16 | calcul | FACTICE : machine du jeu relancé de l'idée 1.1 (répétition) | 3.5 USD | 2026-11-30 | Lazar | répétition |
| GO-2026-11-16-92 | 2026-11-16 | décision | FACTICE : idée 1.1 (répétition) | 0 USD | 2026-11-30 | Lazar | répétition |
| GO-2026-11-16-93 | 2026-11-01 | calcul | FACTICE : idée 1.1, échu (répétition) | 3.5 USD | 2026-11-02 | Lazar | répétition |
| GO-2026-11-16-94 | 2026-11-16 | calcul | FACTICE : idée 1.1, révoqué (répétition) | 3.5 USD | 2026-11-30 | Lazar | répétition |
| GO-2026-11-16-95 | 2026-11-16 | révocation | FACTICE : révoque GO-2026-11-16-94 | — | 2026-11-30 | Lazar | répétition |
| GO-2026-11-16-96 | 2026-11-16 | calcul | FACTICE : autre jeu (répétition) | 3.5 USD | 2026-11-30 | Lazar | répétition |
| GO-2026-11-16-97 | 2026-11-16 | calcul | FACTICE : idée 1.1 (répétition) | trois USD | 2026-11-30 | Lazar | répétition |
| GO-2026-11-16-98 | 2026-11-16 | calcul | FACTICE : idée 1.1 (répétition) | 3.5 USD | 2026-11-30 | Autre | répétition |
EOF
{ for n in 1 2 3 4 6 7 8; do echo "| R-900$n | 2026-11-16 | FACTICE : feu de la machine, étiquette jeu-idee-1-1-relance-v1, commit $C1, sous GO-2026-11-16-9$n | feu |"; done
  echo "| R-9009 | 2026-11-16 | FACTICE : feu sans commit, étiquette jeu-idee-1-1-relance-v1, sous GO-2026-11-16-91 | feu |"; } > "$RS/registres/decisions.md"
DATE_GO=$(date -u +%F); [ "$DATE_GO" \< 2026-11-16 ] || [ "$DATE_GO" \> 2026-11-30 ] && echo "RESERVE : la date du jour $DATE_GO sort de la période des GO factices ; les cas de création échoueront"
# ---------------------------------------------------------------------------------------------------------- 1. session : offre
E="$W/envoi"; mkdir -p "$E"
"$PYS" -I - "$E/recherche.json" <<'EOF'
import json, sys
base = {"num_gpus": 1, "cpu_arch": "amd64", "cpu_cores_effective": 8, "cpu_ram": 16000, "disk_space": 60, "dph_total": 0.045,
        "storage_cost": 0.1, "inet_down": 500, "reliability2": 0.995, "reliability": 0.995, "rentable": True, "cpu_name": "Xeon factice"}
o = lambda i, **k: {**base, "id": i, **k}
offres = [o(91000002, dph_total=0.055), o(91000001), o(91000003, dph_total=0.07), o(91000004, cpu_arch="arm64"),
          o(91000005, cpu_cores_effective=2), o(91000006, cpu_ram=4000), o(91000007, reliability2=0.9, reliability=0.9),
          o(91000008, num_gpus=True), {k: v for k, v in o(91000009).items() if k != "inet_down"}, o(91000010, storage_cost=1.0),
          o(91000011, num_gpus=0, dph_total=0.05), o(91000012, disk_space=10), o(91000013, inet_down=50)]
json.dump(offres, open(sys.argv[1], "w"))
EOF
bash "$LAN" offre-depuis-recherche "$E/recherche.json" "$E/offre.json" > "$W/s.txt" 2>&1; c=$?
attendu "offre-depuis-recherche : la moins chère acceptée (91000001), refus nommés" 0 "$c" "OFFRE ECRITE $E/offre.json : offre 91000001" "$W/s.txt"
for i in 91000003 91000004 91000005 91000006 91000007 91000008 91000009 91000010 91000012 91000013; do
    grep -q "offre $i : refusée" "$W/s.txt" && ok "  offre $i refusée par la garde" || ecart "  offre $i non refusée"; done
grep -q "offre 91000011 : acceptée" "$W/s.txt" && ok "  offre sans carte (num_gpus 0) acceptée" || ecart "  offre sans carte non acceptée"
bash "$LAN" offre-depuis-recherche "$E/recherche.json" "$E/offre.json" > "$W/s.txt" 2>&1; attendu "offre-depuis-recherche : OFFRE.json existant jamais réécrit (R12)" 2 $? "File exists" "$W/s.txt"
"$PYS" -I -c 'import json, sys; l = json.load(open(sys.argv[1])); json.dump([x for x in l if x["id"] in (91000003, 91000004)], open(sys.argv[2], "w"))' "$E/recherche.json" "$W/r-mauvaise.json"
bash "$LAN" offre-depuis-recherche "$W/r-mauvaise.json" "$W/o-mauvaise.json" > "$W/s.txt" 2>&1; c=$?
attendu "offre-depuis-recherche : aucune offre acceptée" 2 "$c" "aucune offre acceptée" "$W/s.txt"; [ ! -e "$W/o-mauvaise.json" ] && ok "  aucun OFFRE.json écrit" || ecart "  OFFRE.json écrit malgré le refus"
"$PYS" -I -c 'import json, sys; l = json.load(open(sys.argv[1])); json.dump(l + [l[1]], open(sys.argv[2], "w"))' "$E/recherche.json" "$W/r-double.json"
bash "$LAN" offre-depuis-recherche "$W/r-double.json" "$W/o-double.json" > "$W/s.txt" 2>&1; attendu "offre-depuis-recherche : identifiant en double" 2 $? "en double" "$W/s.txt"
bash "$LAN" offre "$E/offre.json" 91000001 > "$W/s.txt" 2>&1; attendu "offre : relue, saine" 0 $? "OFFRE ACCEPTEE" "$W/s.txt"
bash "$LAN" offre "$E/offre.json" 91000002 > "$W/s.txt" 2>&1; attendu "offre : identifiant différent" 2 $? "≠ offre demandée" "$W/s.txt"
"$PYS" -I -c 'import json, sys; o = json.load(open(sys.argv[1])); o["prix_total_usd_h"] = 0.08; json.dump(o, open(sys.argv[2], "w"))' "$E/offre.json" "$W/o-chere.json"
bash "$LAN" offre "$W/o-chere.json" > "$W/s.txt" 2>&1; attendu "offre : prix altéré après coup" 2 $? "prix garde" "$W/s.txt"
# ---------------------------------------------------------------------------------------------------------- 2. session : création
cr() { bash "$LAN" creation "$RS" "$1" "$2" "$3" > "$W/s.txt" 2>&1; }
cr "R-9001 GO-2026-11-16-91" "$C1" 0; attendu "creation : feu sain" 0 $? "CREATION PERMISE" "$W/s.txt"
cr "| R-9001 | 2026-11-16 | GO-2026-11-16-91 |" "$C1" 0; attendu "creation : feu en forme longue (C4)" 2 $? "forme courte" "$W/s.txt"
cr "R-9002 GO-2026-11-16-92" "$C1" 0; attendu "creation : GO de type décision" 2 $? "pas « calcul »" "$W/s.txt"
cr "R-9003 GO-2026-11-16-93" "$C1" 0; attendu "creation : GO échu" 2 $? "période de validité" "$W/s.txt"
cr "R-9004 GO-2026-11-16-94" "$C1" 0; attendu "creation : GO révoqué" 2 $? "révoqué" "$W/s.txt"
cr "R-9006 GO-2026-11-16-96" "$C1" 0; attendu "creation : GO sans l'idée 1.1" 2 $? "ne couvre pas" "$W/s.txt"
cr "R-9007 GO-2026-11-16-97" "$C1" 0; attendu "creation : plafond illisible" 2 $? "plafond" "$W/s.txt"
cr "R-9008 GO-2026-11-16-98" "$C1" 0; attendu "creation : GO non accordé par Lazar" 2 $? "pas accordé par Lazar" "$W/s.txt"
cr "R-9009 GO-2026-11-16-91" "$C1" 0; attendu "creation : ligne du feu sans le commit" 2 $? "ne cite pas" "$W/s.txt"
cr "R-9999 GO-2026-11-16-91" "$C1" 0; attendu "creation : ligne du feu absente" 2 $? "0 trouvée" "$W/s.txt"
cr "R-9001 GO-2026-11-16-91" "$C1" 2; attendu "creation : seconde relance" 2 $? "une relance au plus" "$W/s.txt"
# ---------------------------------------------------------------------------------------------------------- 3. session : commande
N0=$(date +%s); ECH=$((N0 + 49 * 3600 + 45 * 60))
co() { local c="$1" er="$2" ech="$3" feu="$4" dos="$5" br="${6:-calcul/idee-1-1-jeu-relance-v1}"; mkdir -p "$dos"
    bash "$LAN" commande "$RS" "$E/offre.json" "$c" "$er" "$ech" "$feu" 0 python:3.13.18-bookworm "$dos" "$br" > "$W/s.txt" 2>&1; }
co "$C1" "$ER" "$ECH" "R-9001 GO-2026-11-16-91" "$W/envoi-c1"; attendu "commande : cas sain" 0 $? "JEU11 COMMANDE" "$W/s.txt"
cp "$W/s.txt" "$W/commande-imprimee.txt"
"$PYS" -I - "$W/commande-imprimee.txt" "$AMO" "$C1" "$ER" "$JETON" > "$W/s2.txt" 2>&1 <<'EOF'
import base64, gzip, hashlib, re, sys
t = open(sys.argv[1], encoding="utf-8").read().split("\n")
l = t[1]
b = re.search(r"echo ([A-Za-z0-9+/=]+) \| base64 -d \| gunzip", l).group(1)
a = gzip.decompress(base64.b64decode(b))
ok = hashlib.sha256(a).hexdigest() == hashlib.sha256(open(sys.argv[2], "rb").read()).hexdigest()
print("amorce décodée égale :", ok, "; longueur de la ligne :", len(l), "; lignes :", len(t) - 1)
need = [" create instance 91000001 --raw --image python:3.13.18-bookworm --disk 20 --cancel-unavail --label jeu-idee-1-1-relance-v1 ",
        "-e COMMIT=" + sys.argv[3], "-e EMPREINTE_RELANCE=" + sys.argv[4], "-e GO_ID=GO-2026-11-16-91", "-e GH_TOKEN=$GH_TOKEN\"",
        "-e BRANCHE_SORTIE=calcul/idee-1-1-jeu-relance-v1", "GO_ID=GO-2026-11-16-91 /home/user/vastai-env/bin/vastai create",
        "> " + sys.argv[1].rsplit("/", 1)[0] + "/envoi-c1/reponse-creation.json )"]
manque = [n for n in need if n not in l]
print("formes attendues présentes :", not manque, manque)
print("clé factice absente :", sys.argv[5] not in "\n".join(t))
sys.exit(0 if ok and not manque and sys.argv[5] not in "\n".join(t) and len(t) - 1 == 2 else 1)
EOF
attendu "commande : amorce décodée à l'octet, formes de la ligne, aucune clé" 0 $? "amorce décodée égale : True" "$W/s2.txt"; sed 's/^/        | /' "$W/s2.txt"
bash "$LAN" controle-ligne "$W/commande-imprimee.txt" > "$W/s.txt" 2>&1; attendu "controle-ligne : sortie saine" 0 $? "LIGNE CONFORME" "$W/s.txt"
"$PYS" -I -c 'import base64, gzip, re, sys
t = open(sys.argv[1], encoding="utf-8").read(); b = re.search(r"echo ([A-Za-z0-9+/=]+) \| base64", t).group(1)
a = gzip.decompress(base64.b64decode(b)) + b"# un octet de plus\n"
open(sys.argv[2], "w", encoding="utf-8").write(t.replace(b, base64.b64encode(gzip.compress(a, mtime=0)).decode()))' "$W/commande-imprimee.txt" "$W/commande-autre-amorce.txt"
bash "$LAN" controle-ligne "$W/commande-autre-amorce.txt" > "$W/s.txt" 2>&1; attendu "controle-ligne : amorce différente" 2 $? "≠ fichier" "$W/s.txt"
head -n 1 "$W/commande-imprimee.txt" > "$W/commande-coupee.txt"
bash "$LAN" controle-ligne "$W/commande-coupee.txt" > "$W/s.txt" 2>&1; attendu "controle-ligne : sortie coupée" 2 $? "mal formée" "$W/s.txt"
echo '[{"id": 60953606, "label": "bbis-t07-v1", "env": "x"}, {"id": 58936096, "label": null}]' | bash "$LAN" inventaire > "$W/s.txt" 2>&1
attendu "inventaire : identifiants et étiquettes seulement, triés" 0 $? "58936096 None" "$W/s.txt"
[ "$(tr '\n' '|' < "$W/s.txt")" = "58936096 None|60953606 bbis-t07-v1|" ] && ok "  ordre et champs (aucun autre champ imprimé)" || ecart "  inventaire : $(tr '\n' ' ' < "$W/s.txt")"
echo '{"pas": "une liste"}' | bash "$LAN" inventaire > "$W/s.txt" 2>&1; attendu "inventaire : liste illisible" 2 $? "illisible" "$W/s.txt"
co "$CX" "$ER" "$ECH" "R-9001 GO-2026-11-16-91" "$W/envoi-cx"; attendu "commande : commit hors de main" 2 $? "pas un ancêtre" "$W/s.txt"
co "$C2" "$ER" "$ECH" "R-9001 GO-2026-11-16-91" "$W/envoi-c2"; attendu "commande : compagnon de l'addendum de relance faux" 2 $? "compagnon de l'addendum de relance faux" "$W/s.txt"
co "$C3" "$ER" "$ECH" "R-9001 GO-2026-11-16-91" "$W/envoi-c3"; attendu "commande : sortie antérieure de ce jeu au commit" 2 $? "sortie(s) ou manifeste(s) de ce jeu" "$W/s.txt"
co "$C4" "$ER" "$ECH" "R-9001 GO-2026-11-16-91" "$W/envoi-c4"; attendu "commande : essai du § 6 point 3 altéré" 2 $? "essai du § 6 point 3" "$W/s.txt"
co "$C1" "$(printf '%064d' 7)" "$ECH" "R-9001 GO-2026-11-16-91" "$W/envoi-er"; attendu "commande : EMPREINTE_RELANCE différente" 2 $? "≠ EMPREINTE_RELANCE" "$W/s.txt"
co "$C1" "$ER" "$((N0 + 48 * 3600))" "R-9001 GO-2026-11-16-91" "$W/envoi-ech"; attendu "commande : échéance trop courte" 2 $? "échéance hors" "$W/s.txt"
co "$C1" "$ER" "$ECH" "R-9002 GO-2026-11-16-92" "$W/envoi-go"; attendu "commande : feu sous un GO de décision" 2 $? "" "$W/s.txt"
: > "$W/envoi-c1/reponse-creation.json"
co "$C1" "$ER" "$ECH" "R-9001 GO-2026-11-16-91" "$W/envoi-c1"; attendu "commande : dossier d'envoi déjà employé (R12)" 2 $? "existe déjà" "$W/s.txt"
# ---------------------------------------------------------------------------------------------------------- 4. session : prix, dépense, destruction
bash "$LAN" prix-relu 0.05 > "$W/s.txt" 2>&1; attendu "prix-relu : 0,05 USD/h" 0 $? "PRIX RELU ACCEPTE" "$W/s.txt"
bash "$LAN" prix-relu 0.0601 > "$W/s.txt" 2>&1; attendu "prix-relu : 0,0601 USD/h" 2 $? "détruire la machine aussitôt" "$W/s.txt"
bash "$LAN" prix-relu 0,05 > "$W/s.txt" 2>&1; attendu "prix-relu : virgule décimale" 2 $? "hors de" "$W/s.txt"
bash "$LAN" depense "$RS" GO-2026-11-16-91 1.0 0.05 > "$W/s.txt" 2>&1; attendu "depense : sous le plafond" 0 $? "DEPENSE" "$W/s.txt"
bash "$LAN" depense "$RS" GO-2026-11-16-91 3.46 0.05 > "$W/s.txt" 2>&1; attendu "depense : plafond atteint dans l'heure" 2 $? "arrêt et destruction" "$W/s.txt"
DM="$W/envoi-m"; mkdir -p "$DM"; echo 99000001 > "$DM/id-machine.txt"
bash "$LAN" detruire 99000001 "$DM" GO-2026-11-16-91 > "$W/s.txt" 2>&1; attendu "detruire : identifiant lu de l'inventaire" 0 $? "destroy instance 99000001 -y" "$W/s.txt"
bash "$LAN" detruire 99000002 "$DM" GO-2026-11-16-91 > "$W/s.txt" 2>&1; attendu "detruire : identifiant autre que celui de l'inventaire" 2 $? "≠ celui de" "$W/s.txt"
bash "$LAN" detruire 60953606 "$DM" GO-2026-11-16-91 > "$W/s.txt" 2>&1; attendu "detruire : machine de B bis (autre tâche)" 2 $? "autre tâche" "$W/s.txt"
bash "$LAN" detruire 9900x "$DM" GO-2026-11-16-91 > "$W/s.txt" 2>&1; attendu "detruire : identifiant illisible" 2 $? "illisible" "$W/s.txt"
echo '[{"id": 58936096}, {"id": 60953606}]' > "$W/l-absente.json"; echo '[{"id": 58936096}, {"id": 99000001}]' > "$W/l-presente.json"
echo '[{"id": 60953606}]' > "$W/l-sans-temoin.json"; echo 'pas du json' > "$W/l-illisible.json"
bash "$LAN" verifier-destruction 99000001 58936096 "$W/l-absente.json" > "$W/s.txt" 2>&1; attendu "verifier-destruction : absente, témoin présent" 0 $? "DESTRUCTION PROUVEE" "$W/s.txt"
bash "$LAN" verifier-destruction 99000001 58936096 "$W/l-presente.json" > "$W/s.txt" 2>&1; attendu "verifier-destruction : toujours listée" 2 $? "toujours listée" "$W/s.txt"
bash "$LAN" verifier-destruction 99000001 58936096 "$W/l-sans-temoin.json" > "$W/s.txt" 2>&1; attendu "verifier-destruction : témoin absent" 2 $? "témoin 58936096 absent" "$W/s.txt"
bash "$LAN" verifier-destruction 99000001 58936096 "$W/l-illisible.json" > "$W/s.txt" 2>&1; attendu "verifier-destruction : liste illisible" 2 $? "illisible" "$W/s.txt"
# ---------------------------------------------------------------------------------------------------------- 5. machine : amorce
nettoyer() {  # $1 = racine de l'amorce : processus restants arrêtés par leur PID (R10), jamais par motif
    local p
    for p in $(grep -ohE '\(PID [0-9]+' "$1"/jeu-idee-1-1-relance-v1/traces/journal.txt 2>/dev/null | grep -oE '[0-9]+') \
             $(cat "$1"/jeu-idee-1-1-relance-v1/traces/pid-jeu.txt 2>/dev/null) $(grep -ohE 'PID [0-9]+ \(parent' "$1"/jeu-idee-1-1-relance-v1/traces/journal.txt 2>/dev/null | grep -oE '[0-9]+'); do
        kill -0 "$p" 2>/dev/null && { kill "$p" 2>/dev/null; echo "        | nettoyage : PID $p arrêté"; }; done; }
am() {  # $1 = nom ; $2 = branche (vN) ; puis affectations NOM=valeur ; sortie dans $W/m-$1.txt
    local nom="$1" br="calcul/idee-1-1-jeu-relance-$2" c; shift 2
    : > "$W/api.log"
    env AMORCE_REPETITION=1 RACINE_AMORCE="$W/m-$nom" DEPOT_URL_REPETITION="$URL" CURL_REPETITION="$W/bin/curl-factice" \
        PY_REPETITION="$PYS" JEU_FACTICE="$FAC" COMMIT="$C1" EMPREINTE_RELANCE="$ER" GO_ID=GO-2026-11-16-91 CONTAINER_ID=99000001 \
        CONTAINER_API_KEY="$CLE" GH_TOKEN="$JETON" BRANCHE_SORTIE="$br" ECHEANCE_UTC_S=$(( $(date +%s) + 300 )) \
        DUREES_REPETITION="200 400 100 20 2 1 1 6 172800" "$@" timeout -k 5 150 bash "$AMO" > "$W/m-$nom.txt" 2>&1 < /dev/null; c=$?
    nettoyer "$W/m-$nom"; cp "$W/api.log" "$W/m-$nom.api.log"; return "$c"; }
dist() { git --git-dir="$NU" "$@"; }
[ ! -e /root/jeu-idee-1-1-relance-v1 ] || echo "RESERVE : /root/jeu-idee-1-1-relance-v1 existe avant l'essai local"
env AMORCE_ESSAI_LOCAL=1 COMMIT="$C1" EMPREINTE_RELANCE="$ER" ECHEANCE_UTC_S=1 GO_ID=GO-2026-11-16-91 bash "$AMO" > "$W/s.txt" 2>&1
attendu "amorce : essai local, rien écrit" 0 $? "ESSAI LOCAL" "$W/s.txt"; [ ! -e /root/jeu-idee-1-1-relance-v1 ] && ok "  aucun dossier écrit sous /root" || ecart "  dossier écrit sous /root"
env RACINE_AMORCE="$W/m-hors" COMMIT="$C1" EMPREINTE_RELANCE="$ER" ECHEANCE_UTC_S=1 GO_ID=GO-2026-11-16-91 bash "$AMO" > "$W/s.txt" 2>&1
attendu "amorce : variable de répétition hors répétition" 2 $? "en répétition seulement" "$W/s.txt"
am args-commit v90 COMMIT=abc; attendu "amorce : COMMIT illisible" 2 $? "COMMIT de 40" "$W/m-args-commit.txt"; [ ! -e "$W/m-args-commit" ] && ok "  aucun dossier écrit" || ecart "  dossier écrit"
am args-go v90 GO_ID=GO-1; attendu "amorce : GO_ID illisible" 2 $? "GO_ID illisible" "$W/m-args-go.txt"
am args-ech v90 ECHEANCE_UTC_S=$(( $(date +%s) + 50 )); attendu "amorce : échéance hors des bornes" 2 $? "échéance hors" "$W/m-args-ech.txt"
am args-br v90 BRANCHE_SORTIE=main; attendu "amorce : branche de sortie illisible" 2 $? "BRANCHE_SORTIE illisible" "$W/m-args-br.txt"
# cas sain
am sain v1; c=$?; J="$W/m-sain/jeu-idee-1-1-relance-v1/traces/journal.txt"
attendu "amorce : cas sain (jeu factice mené au bout)" 0 "$c" "FIN : jeu mené au bout" "$J"
for m in "contrôle des versions (addendum de relance, 4.2) : « 3.13.18 2.4.6 1.17.1 »" "aucune sortie antérieure" "jeu lancé : PID" "sorties : 8 fichiers, chacun égal à son compagnon" "suivi : "; do
    grep -q -- "$m" "$J" && ok "  journal : « $m »" || ecart "  journal sans « $m »"; done
NC=$(dist rev-list --count refs/heads/calcul/idee-1-1-jeu-relance-v1 2>/dev/null); NR=$(dist rev-list --max-parents=0 refs/heads/calcul/idee-1-1-jeu-relance-v1 2>/dev/null | wc -l)
[ "${NC:-0}" -ge 6 ] && [ "$NR" = 1 ] && ok "  branche de sortie : $NC commits, une seule racine (orpheline)" || ecart "  branche de sortie : $NC commits, $NR racines"
NS=$(dist log --oneline refs/heads/calcul/idee-1-1-jeu-relance-v1 | grep -c "suivi : "); [ "$NS" -ge 2 ] && ok "  poussées intermédiaires du journal : $NS" || ecart "  poussées intermédiaires : $NS"
H=$(dist ls-tree -r --name-only refs/heads/calcul/idee-1-1-jeu-relance-v1 | grep -vE '^(traces/machine-jeu-idee-1-1-v1/|runs/[0-9]{8}-[0-9]{6}-idee-1-1-poids-du-nul-v5/|diag/organisme-idees-juge-v1/[0-9]{8}-[0-9]{6}-idee-1-1-poids-du-nul-v5/)')
[ -z "$H" ] && ok "  branche de sortie : traces et deux dossiers du run seulement" || ecart "  chemins hors des sorties permises : $H"
RUNV=$(ls "$W/m-sain/jeu-idee-1-1-relance-v1/depot/runs" | grep -E 'idee-1-1-poids-du-nul-v5$')
DIF=0; while IFS= read -r p; do a=$(dist show "refs/heads/calcul/idee-1-1-jeu-relance-v1:$p" | sha256sum); b=$(sha256sum < "$W/m-sain/jeu-idee-1-1-relance-v1/depot/$p")
    [ "$a" = "$b" ] || DIF=$((DIF + 1)); done < <(dist ls-tree -r --name-only refs/heads/calcul/idee-1-1-jeu-relance-v1 -- runs diag)
[ "$DIF" = 0 ] && ok "  sorties poussées égales à l'octet à celles de la machine (run $RUNV)" || ecart "  $DIF sorties différentes"
grep -q " PUT " "$W/m-sain.api.log" && ! grep -q " DELETE " "$W/m-sain.api.log" && ok "  loueur : état « stopped » demandé, aucune destruction avant l'échéance" || ecart "  loueur : $(tr '\n' ' ' < "$W/m-sain.api.log")"
[ "$(git -C "$W/m-sain/jeu-idee-1-1-relance-v1/depot" remote get-url --push origin)" = "interdit://aucune-poussee-depuis-le-depot-du-jeu" ] && ok "  dépôt du jeu : poussée impossible" || ecart "  dépôt du jeu : poussée possible"
# artefacts de la machine (traces poussées sur une branche neuve à chaque cas)
am versions v2 PY_REPETITION="$W/bin/python-fausses-versions"; attendu "amorce : versions fausses (numpy 2.5.3)" 2 $? "pas de relance sous cet addendum ; arrêt avant tout calcul" "$W/m-versions/jeu-idee-1-1-relance-v1/traces/journal.txt"
[ ! -e "$W/m-versions/jeu-idee-1-1-relance-v1/depot" ] && ok "  aucun clonage, aucun calcul" || ecart "  dépôt cloné malgré l'arrêt"
dist show refs/heads/calcul/idee-1-1-jeu-relance-v2:traces/machine-jeu-idee-1-1-v1/journal.txt 2>/dev/null | grep -q "ARRET : versions" && ok "  traces de l'arrêt poussées" || ecart "  traces de l'arrêt non poussées"
am hors-main v3 COMMIT="$CX"; attendu "amorce : commit hors de main" 2 $? " de main" "$W/m-hors-main/jeu-idee-1-1-relance-v1/traces/journal.txt"
am comp-faux v4 COMMIT="$C2"; attendu "amorce : compagnon de l'addendum de relance faux" 2 $? "différent de son compagnon" "$W/m-comp-faux/jeu-idee-1-1-relance-v1/traces/journal.txt"
am empreinte v5 EMPREINTE_RELANCE="$(printf '%064d' 7)"; attendu "amorce : EMPREINTE_RELANCE différente" 2 $? "≠ EMPREINTE_RELANCE" "$W/m-empreinte/jeu-idee-1-1-relance-v1/traces/journal.txt"
am anterieure v6 COMMIT="$C3"; attendu "amorce : sortie antérieure de ce jeu au commit" 2 $? "sortie ou manifeste antérieur" "$W/m-anterieure/jeu-idee-1-1-relance-v1/traces/journal.txt"
am essai v7 COMMIT="$C4"; attendu "amorce : essai du § 6 point 3 altéré" 2 $? "essai du § 6 point 3" "$W/m-essai/jeu-idee-1-1-relance-v1/traces/journal.txt"
am disque v8 SEUIL_DISQUE_REPETITION=999999999999999999; attendu "amorce : disque libre sous le seuil" 2 $? "disque libre" "$W/m-disque/jeu-idee-1-1-relance-v1/traces/journal.txt"
am marge v9 DUREES_REPETITION="200 400 1000 20 2 1 1 6 172800"; attendu "amorce : échéance trop proche pour la borne de 48 h" 2 $? "échéance trop proche" "$W/m-marge/jeu-idee-1-1-relance-v1/traces/journal.txt"
[ ! -e "$W/m-marge/jeu-idee-1-1-relance-v1/traces/pid-jeu.txt" ] && ok "  jeu non lancé" || ecart "  jeu lancé malgré la marge"
am arret v10 JEU_FACTICE_MODE=arret; attendu "amorce : arrêt écrit du jeu" 4 $? "arrêt écrit (arret.json poussé" "$W/m-arret/jeu-idee-1-1-relance-v1/traces/journal.txt"
dist ls-tree -r --name-only refs/heads/calcul/idee-1-1-jeu-relance-v10 | grep -q '/arret.json$' && ok "  arret.json poussé" || ecart "  arret.json non poussé"
am faux v11 JEU_FACTICE_MODE=faux; attendu "amorce : compagnon de sortie faux" 4 $? "RESERVE : sorties sans compagnon ou différentes de lui" "$W/m-faux/jeu-idee-1-1-relance-v1/traces/journal.txt"
am hors v12 JEU_FACTICE_MODE=hors; attendu "amorce : fichier écrit hors des dossiers du run (réserve, non poussé)" 0 $? "RESERVE : fichiers écrits par le jeu hors de ses deux dossiers" "$W/m-hors/jeu-idee-1-1-relance-v1/traces/journal.txt"
dist ls-tree -r --name-only refs/heads/calcul/idee-1-1-jeu-relance-v12 | grep -q '^donnees/' && ecart "  fichier hors poussé" || ok "  fichier hors non poussé"
am minuterie-term v13 JEU_FACTICE_MODE=lent JEU_FACTICE_TRANCHES=200 ECHEANCE_UTC_S=$(( $(date +%s) + 40 )) DUREES_REPETITION="30 60 20 15 2 1 1 6 5" ATTENDRE_MINUTERIE_REPETITION=1
c=$?; J="$W/m-minuterie-term/jeu-idee-1-1-relance-v1/traces/journal.txt"
attendu "minuterie : jeu au-delà de sa borne : TERM par son PID, arrêt écrit" 4 "$c" "TERM par son PID" "$J"
[ "$(grep -c ' DELETE ' "$W/m-minuterie-term.api.log")" = 6 ] && [ "$(grep -c ' PUT ' "$W/m-minuterie-term.api.log")" = 2 ] \
    && ok "  loueur : 6 demandes de destruction par l'identifiant, « stopped » à la fin et après la cinquième" || ecart "  loueur : $(tr '\n' ' ' < "$W/m-minuterie-term.api.log")"
dist ls-tree -r --name-only refs/heads/calcul/idee-1-1-jeu-relance-v13 | grep -q '/arret.json$' && ok "  arret.json poussé" || ecart "  arret.json non poussé"
grep -q "/instances/99000001/" "$W/m-minuterie-term.api.log" && ok "  destruction visée par l'identifiant de la machine" || ecart "  adresse de destruction"
am minuterie-borne v14 JEU_FACTICE_MODE=lent JEU_FACTICE_TRANCHES=40 ECHEANCE_UTC_S=$(( $(date +%s) + 30 )) DUREES_REPETITION="20 60 10 10 2 1 1 6 1000" ATTENDRE_MINUTERIE_REPETITION=1
c=$?; J="$W/m-minuterie-borne/jeu-idee-1-1-relance-v1/traces/journal.txt"
attendu "minuterie : jeu dans sa borne : jamais coupé par TERM" 0 "$c" "dans sa borne (ou depart.json absent) : la minuterie ne le coupe pas" "$J"
grep -q "TERM par son PID" "$J" && ecart "  TERM envoyé à un jeu dans sa borne" || ok "  aucun TERM"
[ "$(grep -c ' DELETE ' "$W/m-minuterie-borne.api.log")" = 6 ] && ok "  destruction demandée à l'échéance (6 essais)" || ecart "  loueur : $(tr '\n' ' ' < "$W/m-minuterie-borne.api.log")"
T1=$(dist rev-parse refs/heads/calcul/idee-1-1-jeu-relance-v1)
am branche-existe v1; attendu "amorce : branche de sortie déjà présente (R12)" 2 $? "présente sur le dépôt distant" "$W/m-branche-existe/jeu-idee-1-1-relance-v1/traces/journal.txt"
[ "$(dist rev-parse refs/heads/calcul/idee-1-1-jeu-relance-v1)" = "$T1" ] && ok "  branche existante non touchée" || ecart "  branche existante modifiée"
# fonction de poussée extraite et jouée seule : chemin hors des sorties permises, fichier trop gros
P="$W/poussee"; mkdir -p "$P"; git init -q -b calcul/idee-1-1-jeu-relance-v99 "$P/S"
sed -n '/^# >>> poussee/,/^# <<< poussee/p' "$AMO" > "$P/bloc.sh"
cat > "$P/essai.sh" <<EOF
S="$P/S"; XT=traces/machine-jeu-idee-1-1-v1; DIAG=diag/organisme-idees-juge-v1; RUN=20261116-000000-idee-1-1-poids-du-nul-v5
BR=calcul/idee-1-1-jeu-relance-v99; PAS=1; X="$P"; VERROU="$P/verrou"; j() { echo "\$*"; }
git -C "\$S" remote add origin "$URL"
. "$P/bloc.sh"
SEUIL_FICHIER=94000000
mkdir -p "\$S/autre" && echo x > "\$S/autre/x.txt" && git -C "\$S" add -f autre/x.txt; commit_pousser "essai"; echo "code-hors \$?"
git -C "\$S" rm -q --cached autre/x.txt
mkdir -p "\$S/\$DIAG/\$RUN" && head -c 2000 /dev/zero > "\$S/\$DIAG/\$RUN/gros.bin" && git -C "\$S" add -f "\$DIAG/\$RUN/gros.bin"
SEUIL_FICHIER=1000; commit_pousser "essai"; echo "code-gros \$?"
SEUIL_FICHIER=94000000; commit_pousser "essai"; echo "code-sain \$?"
EOF
bash "$P/essai.sh" > "$W/s.txt" 2>&1
grep -q "code-hors 3" "$W/s.txt" && grep -q "REFUS DE POUSSEE : chemin hors" "$W/s.txt" && ok "poussée : chemin hors des sorties permises refusé" || ecart "poussée : chemin hors non refusé"
grep -q "code-gros 3" "$W/s.txt" && ok "poussée : fichier au-dessus du seuil refusé" || ecart "poussée : fichier trop gros non refusé"
grep -q "code-sain 0" "$W/s.txt" && dist rev-parse -q --verify refs/heads/calcul/idee-1-1-jeu-relance-v99 > /dev/null && ok "poussée : cas sain poussé" || ecart "poussée : cas sain non poussé"
# ---------------------------------------------------------------------------------------------------------- 5 bis. v2 : reprise de la poussée des sorties
ligne_de() { grep -n -m 1 -- "$1" "$2" | cut -d: -f1; }  # numéro de la première ligne qui porte $1 dans $2 (vide si aucune)
heure_de() { date -u -d "$(sed -n "$1p" "$2" | cut -d' ' -f1)" +%s; }  # heure (s) de la ligne $1 du journal $2
sorties_egales() {  # $1 = branche : sorties poussées égales à l'octet à celles de la machine $2, même nombre de fichiers
    local b="refs/heads/calcul/idee-1-1-jeu-relance-$1" m="$W/m-$2/jeu-idee-1-1-relance-v1/depot" p a d=0 nb nm
    while IFS= read -r p; do a=$(dist show "$b:$p" | sha256sum); [ "$a" = "$(sha256sum < "$m/$p")" ] || d=$((d + 1)); done < <(dist ls-tree -r --name-only "$b" -- runs diag)
    nb=$(dist ls-tree -r --name-only "$b" -- runs diag | wc -l); nm=$( (cd "$m" && find runs diag/organisme-idees-juge-v1 -type f -path '*idee-1-1-poids-du-nul-v5/*') | wc -l)
    [ "$d" = 0 ] && [ "$nb" = "$nm" ] && [ "$nb" -gt 0 ]; }
# (a) poussée refusée trois fois puis acceptée : machine vivante, sorties poussées, aucun « stopped » avant
am reprise-acceptee v15; c=$?; J="$W/m-reprise-acceptee/jeu-idee-1-1-relance-v1/traces/journal.txt"
attendu "reprise : poussée des sorties refusée trois fois puis acceptée : jeu mené au bout" 0 "$c" "FIN : jeu mené au bout" "$J"
[ "$(cat "$W/refus-v15.n" 2>/dev/null)" = 3 ] && [ -s "$W/refus-v15.n.acceptees" ] && ok "  dépôt jouet : trois refus, puis poussées acceptées" || ecart "  refus : $(cat "$W/refus-v15.n" 2>/dev/null), acceptées : $(wc -l < "$W/refus-v15.n.acceptees" 2>/dev/null)"
grep -q "RESERVE : poussée des sorties impossible : reprise toutes les 5 s" "$J" && ok "  journal : « RESERVE : poussée des sorties impossible », reprise annoncée" || ecart "  journal sans la réserve de reprise"
LR=$(ligne_de "poussée des sorties reprise : réussie" "$J"); LS=$(ligne_de "« stopped » demandé" "$J")
[ -n "$LR" ] && [ -n "$LS" ] && [ "$LS" -gt "$LR" ] && ok "  aucun « stopped » avant la poussée réussie (lignes $LR puis $LS)" || ecart "  ordre : réussie ligne ${LR:-absente}, « stopped » ligne ${LS:-absente}"
grep -q "ARRET" "$J" && ecart "  arrêt écrit malgré la reprise réussie" || ok "  aucun arrêt"
[ "$(grep -c ' PUT ' "$W/m-reprise-acceptee.api.log")" = 1 ] && ! grep -q ' DELETE ' "$W/m-reprise-acceptee.api.log" && ok "  loueur : un seul « stopped », à la fin ; aucune destruction" || ecart "  loueur : $(tr '\n' ' ' < "$W/m-reprise-acceptee.api.log")"
sorties_egales v15 reprise-acceptee && ok "  sorties poussées égales à l'octet à celles de la machine, toutes présentes" || ecart "  sorties poussées incomplètes ou différentes"
# (b) poussée jamais acceptée : reprises journalisées, arrêt en code 4 à l'échéance − MARGE_TERM, sorties intactes sur le disque
EB=$(( $(date +%s) + 90 )); MB=40
am reprise-jamais v16 ECHEANCE_UTC_S=$EB DUREES_REPETITION="30 400 10 $MB 2 1 1 6 172800" ATTENDRE_MINUTERIE_REPETITION=1
c=$?; J="$W/m-reprise-jamais/jeu-idee-1-1-relance-v1/traces/journal.txt"; DJ="$W/m-reprise-jamais/jeu-idee-1-1-relance-v1/depot"
attendu "reprise : poussée des sorties jamais acceptée : arrêt en code 4 après reprises" 4 "$c" "impossible après reprises" "$J"
grep -q "RESERVE : poussée des sorties impossible" "$J" && ok "  journal : « RESERVE : poussée des sorties impossible »" || ecart "  journal sans la réserve"
NRP=$(grep -cE "reprise [0-9]+ de la poussée des sorties : échec" "$J"); grep -q "reprises de la poussée des sorties épuisées ($NRP)" "$J" && [ "$NRP" -ge 2 ] \
    && ok "  reprises journalisées : $NRP échecs, puis « épuisées »" || ecart "  reprises journalisées : $NRP"
LA=$(ligne_de "ARRET : recopie ou poussée des sorties" "$J"); LS=$(ligne_de "« stopped » demandé" "$J")
HA=$([ -n "$LA" ] && heure_de "$LA" "$J"); HP=$(awk '$3 == "PUT" { print $2; exit }' "$W/m-reprise-jamais.api.log")
[ -n "$HA" ] && [ "$HA" -ge $((EB - MB - 1)) ] && [ "$HA" -lt "$EB" ] && ok "  arrêt à l'échéance − $MB s ou juste après (à $((HA - EB + MB)) s de cette borne), avant l'échéance" || ecart "  heure de l'arrêt ${HA:-absente} ; borne $((EB - MB)) ; échéance $EB"
[ -n "$LS" ] && [ "$LS" -gt "${LA:-999999}" ] && [ -n "$HP" ] && [ "$HP" -ge $((EB - MB - 1)) ] && ok "  aucun « stopped » avant l'arrêt (premier « stopped » demandé à $((HP - EB + MB)) s de la borne)" || ecart "  « stopped » trop tôt : ligne ${LS:-absente}, loueur ${HP:-absent}"
HD=$(awk '$3 == "DELETE" { print $2; exit }' "$W/m-reprise-jamais.api.log")
[ "$(grep -c ' DELETE ' "$W/m-reprise-jamais.api.log")" = 6 ] && [ -n "$HD" ] && [ "$HD" -ge "$EB" ] && ok "  destruction par l'identifiant demandée à l'échéance seulement (6 essais)" || ecart "  loueur : $(tr '\n' ' ' < "$W/m-reprise-jamais.api.log")"
RJ=$(ls "$DJ/runs" 2>/dev/null | grep -E 'idee-1-1-poids-du-nul-v5$'); NI=0; NK=0
for p in "runs/$RJ" "diag/organisme-idees-juge-v1/$RJ"; do
    while IFS= read -r -d '' k; do NK=$((NK + 1)); ( cd "$(dirname "$k")" && sha256sum -c --quiet "$(basename "$k")" ) > /dev/null 2>&1 || NI=$((NI + 1)); done < <(find "$DJ/$p" -name '*.sha256' -print0 2>/dev/null)
    diff -r -q "$DJ/$p" "$W/m-reprise-jamais/jeu-idee-1-1-relance-v1/sortie/$p" > /dev/null 2>&1 || NI=$((NI + 1)); done
[ -n "$RJ" ] && [ "$NK" = 8 ] && [ "$NI" = 0 ] && ok "  sorties intactes sur le disque : 8 fichiers égaux à leurs compagnons, copie de sortie égale" || ecart "  sorties sur le disque : run ${RJ:-absent}, $NK compagnons, $NI écarts"
dist show refs/heads/calcul/idee-1-1-jeu-relance-v16:traces/machine-jeu-idee-1-1-v1/journal.txt > /dev/null 2>&1 && [ -z "$(dist ls-tree -r --name-only refs/heads/calcul/idee-1-1-jeu-relance-v16 -- runs diag)" ] \
    && ok "  branche -v16 : traces d'avant la fin seulement, aucune sortie poussée (refus du dépôt jouet tenus)" || ecart "  branche -v16 : sorties poussées malgré le refus, ou traces absentes"
# (c) le cas sain ne reprend rien
grep -q "RESERVE : poussée des sorties impossible" "$W/m-sain/jeu-idee-1-1-relance-v1/traces/journal.txt" && ecart "cas sain : reprise déclenchée sans échec" || ok "cas sain : aucune reprise (poussée acceptée du premier coup)"
# ---------------------------------------------------------------------------------------------------------- 6. clés jamais affichées ni poussées
FU=$(grep -rlF -e "$CLE" -e "$JETON" "$W"/m-* "$W"/*.txt "$W"/*.log "$W"/envoi* "$W"/poussee 2>/dev/null | head -n 3)
[ -z "$FU" ] && ok "clés factices absentes de toutes les sorties et de tous les fichiers des machines" || ecart "clé factice trouvée dans : $FU"
NF=0; for r in $(dist for-each-ref --format='%(refname)' refs/heads/calcul/); do dist grep -q -F -e "$CLE" -e "$JETON" "$r" -- . 2>/dev/null && NF=$((NF + 1)); done
dist log --all --format=%B | grep -q -F -e "$CLE" -e "$JETON" && NF=$((NF + 1))
[ "$NF" = 0 ] && ok "clés factices absentes de toutes les branches poussées (contenus et messages)" || ecart "clé factice poussée ($NF)"
REST=$(for d in "$W"/m-*/jeu-idee-1-1-relance-v1/traces; do for p in $(cat "$d/pid-jeu.txt" 2>/dev/null) $(grep -ohE '\(PID [0-9]+' "$d/journal.txt" 2>/dev/null | grep -oE '[0-9]+'); do s=$(ps -o stat= -p "$p" 2>/dev/null | tr -d ' '); [ -n "$s" ] && [ "${s#Z}" = "$s" ] && echo "$p($s)"; done; done)
[ -z "$REST" ] && ok "aucun processus de la répétition encore vivant" || ecart "processus vivants : $REST"
echo "répétition : $NB cas, $NE écart(s) ; fin $(date -u +%FT%TZ)"
[ "$NE" = 0 ]
