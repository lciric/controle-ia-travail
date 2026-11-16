#!/usr/bin/env bash
# Essai (règle R5) de lecture_audit_r4_base_a_mere_v1.py sur des fichiers jouets fabriqués ici (aucune donnée du programme).
# Écrit le 2026-11-16 par un développeur neuf, sous-agent de la session mère (modèle A) ; modèle : essai_lecture_etat_ba_l2_mere_v1.sh.
#     bash essai_lecture_audit_r4_base_a_mere_v1.sh <dépôt> <bac neuf>
# Jouets : objet JSON à la racine, clés triées, indentation 2, comme la pièce (_json_texte) ; clé « audit_r4 » portant « declenche »
# et des champs voisins marqués SECRET (motifs, items, échantillons, aires) ; compagnon « <sha256>  base-a-t08.json » (forme de
# controle_ia.scellement.sceller). Chaque cas vérifie : le code, une seule ligne sur la sortie standard, rien sur l'erreur, la ligne
# exacte (cas sains) ou le préfixe de refus et le motif (artefacts), et l'absence de toute valeur marquée (SECRET, 0.7777).
set -u
DEPOT=$(cd "$1" && pwd); BAC="$2"
[ ! -e "$BAC" ] || { echo "ARRÊT : $BAC existe déjà"; exit 1; }
mkdir -p "$BAC"; BAC=$(cd "$BAC" && pwd)
L="$DEPOT/docs/procedures/lecture-7b-etape-b-compte-3-v1/lecture_audit_r4_base_a_mere_v1.py"
export LC_ALL=C.UTF-8
date -u +"début de l'essai : %Y-%m-%dT%H:%M:%SZ"; echo "script essayé : $(sha256sum "$L" | cut -d' ' -f1)"; echo "interpréteur : $(python3 -I -c 'import sys; print(sys.version.split()[0])')"
OK=0; KO=0; T="audit R4 de la base (A) : "
# cas NOM CODE_ATTENDU EXACT|MOTIF TEXTE -- arguments du lecteur
cas() { local nom="$1" attendu="$2" genre="$3" texte="$4"; shift 4; local s e c n bon=1
  s=$(python3 -I -B "$L" "$@" 2>"$BAC/err"); c=$?; e=$(cat "$BAC/err"); n=$(printf '%s\n' "$s" | grep -c .)
  [ "$c" = "$attendu" ] && [ "$n" = 1 ] && [ -z "$e" ] || bon=0
  if [ "$genre" = EXACT ]; then [ "$s" = "$texte" ] || bon=0
  else case "$s" in "${T}refus — "*) ;; *) bon=0;; esac; printf '%s' "$s" | grep -qF -- "$texte" || bon=0; fi
  printf '%s%s' "$s" "$e" | grep -qE 'SECRET|0\.7777' && bon=0
  if [ "$bon" = 1 ]; then OK=$((OK+1)); echo "conforme : $nom (code $c) : $s"
  else KO=$((KO+1)); echo "ÉCART : $nom (code $c, attendu $attendu ; $n ligne(s))"; printf '%s\n%s\n' "$s" "$e" | sed 's/^/    /'; fi; }
# jouet DOSSIER GENRE [NOM] : écrit DOSSIER/NOM (défaut base-a-t08.json) et son compagnon ; imprime le chemin du fichier
jouet() { local D="$BAC/$1" nom="${3:-base-a-t08.json}"; mkdir -p "$D"
  python3 -I -B - "$2" "$D/$nom" <<'PY'
import json, sys
genre, chemin = sys.argv[1], sys.argv[2]
audit = {"action": "SECRET-ACTION", "conditions_concernees": ["SECRET-COND"], "echantillons": {"SECRET-COND": ["SECRET-CLE"]},
         "items": {"i": {"declenche": True, "detail": {"aire": 0.7777}}}, "motifs": ["(SECRET)"]}
doc = {"audit_r4": audit, "lignes": {"BA-L2": {"phrase": "SECRET-PHRASE", "s_applique": False}}, "run_id": "SECRET-RUN",
       "doses": {"S25": {"aire": 0.7777}}, "reserves": [{"code": "R-BA6", "phrase": "SECRET-RESERVE", "s_applique": True}]}
brut = None
if genre == "vrai": audit["declenche"] = True
elif genre == "faux": audit["declenche"] = False
elif genre == "sans-declenche": pass
elif genre == "sans-audit": del doc["audit_r4"]
elif genre == "chaine": audit["declenche"] = "true"
elif genre == "nombre": audit["declenche"] = 1
elif genre == "null": audit["declenche"] = None
elif genre == "audit-booleen": doc["audit_r4"] = True
elif genre == "racine-liste": audit["declenche"] = True; doc = [doc]
elif genre == "non-json": brut = b'{"audit_r4": {"declenche": true, "motifs": ["SECRET"]'
elif genre == "non-utf8": brut = b'{"audit_r4": {"declenche": true, "motifs": ["SECRET-\xff\xfe"]}}\n'
elif genre == "doublon": brut = ('{\n  "audit_r4": {\n    "declenche": true,\n    "declenche": false,\n    "motifs": ["SECRET"]\n  }\n}\n').encode()
elif genre == "nan": brut = b'{"audit_r4": {"declenche": false, "items": {"i": {"detail": {"aire": NaN}}}, "motifs": ["SECRET"]}}\n'
else: sys.exit("genre inconnu : " + genre)
if brut is None:
    brut = (json.dumps(doc, indent=2, ensure_ascii=False, sort_keys=True, allow_nan=False) + "\n").encode("utf-8")
open(chemin, "wb").write(brut)
PY
  (cd "$D" && sha256sum "$nom" > "$nom.sha256"); echo "$D/$nom"; }
h() { sha256sum "$1" | cut -c1-64; }
AUTRE=$(printf 'jouet autre' | sha256sum | cut -c1-64)

echo "--- cas sains"
F=$(jouet s1 vrai); cas "S1 audit déclenché" 0 EXACT "${T}déclenché" --fichier "$F" --empreinte "$(h "$F")"
F=$(jouet s2 faux); cas "S2 audit non déclenché" 0 EXACT "${T}non déclenché" --fichier "$F" --empreinte "$(h "$F")"
F=$(jouet s3 vrai); cp "$F" "$BAC/s3-ref"; cas "S3 ordre des options inversé" 0 EXACT "${T}déclenché" --empreinte "$(h "$F")" --fichier "$F"
cmp -s "$F" "$BAC/s3-ref" && echo "conforme : S3b le lecteur n'a rien écrit dans le fichier" && OK=$((OK+1)) || { echo "ÉCART : S3b fichier modifié par le lecteur"; KO=$((KO+1)); }
echo "--- artefacts : empreintes et compagnon"
F=$(jouet a1 vrai); HF=$(h "$F"); echo "$AUTRE  base-a-t08.json" > "$F.sha256"; cas "A1 compagnon faux" 1 MOTIF "≠ compagnon" --fichier "$F" --empreinte "$HF"
F=$(jouet a2 vrai); rm "$F.sha256"; cas "A2 compagnon absent" 1 MOTIF "compagnon base-a-t08.json.sha256 absent" --fichier "$F" --empreinte "$(h "$F")"
F=$(jouet a3 vrai); HF=$(h "$F"); echo "$HF  autre-nom.json" > "$F.sha256"; cas "A3 compagnon d'un autre nom" 1 MOTIF "hors du format" --fichier "$F" --empreinte "$HF"
F=$(jouet a4 vrai); HF=$(h "$F"); { cat "$F.sha256"; cat "$F.sha256"; } > "$BAC/a4c"; mv "$BAC/a4c" "$F.sha256"; cas "A4 compagnon de deux lignes" 1 MOTIF "hors du format" --fichier "$F" --empreinte "$HF"
F=$(jouet a5 faux); cas "A5 empreinte rendue par l'hôte autre" 1 MOTIF "≠ empreinte rendue par l'hôte" --fichier "$F" --empreinte "$AUTRE"
F=$(jouet a6 faux); HF=$(h "$F"); printf ' ' >> "$F"; cas "A6 fichier altéré après son sceau" 1 MOTIF "≠ compagnon" --fichier "$F" --empreinte "$HF"
F=$(jouet a7 faux); HF=$(h "$F"); printf ' ' >> "$F"; (cd "$(dirname "$F")" && sha256sum base-a-t08.json > base-a-t08.json.sha256)
cas "A7 fichier altéré et rescellé (compagnon refait, hôte non)" 1 MOTIF "≠ empreinte rendue par l'hôte" --fichier "$F" --empreinte "$HF"
F=$(jouet a8 vrai); cas "A8 empreinte mal formée (majuscules)" 1 MOTIF "hors du format (64 chiffres" --fichier "$F" --empreinte "$(h "$F" | tr a-f A-F)"
echo "--- artefacts : champ"
F=$(jouet a9 sans-declenche); cas "A9 champ audit_r4.declenche absent" 1 MOTIF "« audit_r4.declenche » absent" --fichier "$F" --empreinte "$(h "$F")"
F=$(jouet a10 sans-audit); cas "A10 champ audit_r4 absent" 1 MOTIF "« audit_r4 » absent" --fichier "$F" --empreinte "$(h "$F")"
F=$(jouet a11 chaine); cas "A11 declenche chaîne \"true\"" 1 MOTIF "de type str, booléen attendu" --fichier "$F" --empreinte "$(h "$F")"
F=$(jouet a12 nombre); cas "A12 declenche nombre 1" 1 MOTIF "de type int, booléen attendu" --fichier "$F" --empreinte "$(h "$F")"
F=$(jouet a13 null); cas "A13 declenche null" 1 MOTIF "de type NoneType, booléen attendu" --fichier "$F" --empreinte "$(h "$F")"
F=$(jouet a14 audit-booleen); cas "A14 audit_r4 booléen au lieu d'un objet" 1 MOTIF "« audit_r4 » de type bool, objet attendu" --fichier "$F" --empreinte "$(h "$F")"
F=$(jouet a15 racine-liste); cas "A15 racine liste" 1 MOTIF "racine de type list" --fichier "$F" --empreinte "$(h "$F")"
F=$(jouet a16 doublon); cas "A16 clé declenche en double" 1 MOTIF "clé en double" --fichier "$F" --empreinte "$(h "$F")"
echo "--- artefacts : fichier"
F=$(jouet a17 non-json); cas "A17 fichier illisible : JSON tronqué" 1 MOTIF "illisible : texte UTF-8 ou JSON invalide" --fichier "$F" --empreinte "$(h "$F")"
F=$(jouet a18 non-utf8); cas "A18 fichier illisible : octets non UTF-8" 1 MOTIF "illisible : texte UTF-8 ou JSON invalide" --fichier "$F" --empreinte "$(h "$F")"
F=$(jouet a19 nan); cas "A19 NaN dans le JSON" 1 MOTIF "constante non standard" --fichier "$F" --empreinte "$(h "$F")"
F=$(jouet a20 vrai); HF=$(h "$F"); rm "$F"; cas "A20 fichier absent" 1 MOTIF "absent, ou pas un fichier ordinaire" --fichier "$F" --empreinte "$HF"
F=$(jouet a21 vrai); HF=$(h "$F"); mkdir -p "$BAC/a21l"; ln -s "$F" "$BAC/a21l/base-a-t08.json"; cp "$F.sha256" "$BAC/a21l/"
cas "A21 lien symbolique" 1 MOTIF "pas un fichier ordinaire" --fichier "$BAC/a21l/base-a-t08.json" --empreinte "$HF"
F=$(jouet a22 vrai issue-mots-et-cout-t06.json); cas "A22 autre fichier de la pièce (nom autre)" 1 MOTIF "nommé autrement que base-a-t08.json" --fichier "$F" --empreinte "$(h "$F")"
F=$(jouet a23 vrai); cas "A23 appel sans --empreinte" 1 MOTIF "appel invalide" --fichier "$F"
F=$(jouet a24 vrai); cas "A24 option inconnue" 1 MOTIF "appel invalide" --fichier "$F" --empreinte "$(h "$F")" --cle-json lignes.BA-L2.s_applique

echo "BILAN : $OK conformes sur $((OK + KO))"; [ "$KO" = 0 ] && echo "ESSAI : TOUT CONFORME" || echo "ESSAI : ÉCARTS"
date -u +"fin de l'essai : %Y-%m-%dT%H:%M:%SZ"
