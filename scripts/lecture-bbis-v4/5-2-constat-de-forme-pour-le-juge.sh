#!/bin/bash
# § 5.2 — constat de forme, pour le juge seul (écrit et scellé sans être affiché)
# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
# seulement, le bloc « § 5.2, constat de forme » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/5-2-constat-de-forme-pour-le-juge.sh 1
. "$(dirname "$0")/commun.sh"
N="${1:-}"; exiger_numero "$N"; RUNL="$(cat "$T/run-lecture-$N.txt")"
grep -q -E '^ETAT : (écrit|non consommée)' "$LV1/releve-apres-lancement-lecture-bbis-$N-v1.txt" || { echo "aucun fichier de lecture écrit : pas de constat de forme"; exit 1; }
C="$LV1/constat-forme-pour-le-juge-lecture-bbis-$N-v1.txt"; neuf "$C"
G1="$LV1/sortie-lancement-lecture-bbis-$N-v1.txt"
{
dire "Constat de forme pour le juge — lancement n° $N, run de lecture $RUNL — pièce que la conductrice n'ouvre pas"
dire "lignes du seuil « BBIS LECTURE ENTREES OUVERTES » : $(grep -c '^BBIS LECTURE ENTREES OUVERTES$' "$G1")"
dire "lignes « BBIS LECTURE ECRITE » : $(grep -c '^BBIS LECTURE ECRITE ' "$G1")"
dire "lignes « BBIS LECTURE NON CONSOMMEE » : $(grep -c '^BBIS LECTURE NON CONSOMMEE ' "$G1")"
dire "lignes « BBIS LECTURE ARRET » : $(grep -c '^BBIS LECTURE ARRET' "$G1")"
dire "lignes de la sortie gardée : $(wc -l < "$G1" | tr -d ' ')"
dire "début $(cat "$T/lancement-$N.debut") ; fin $(cat "$T/lancement-$N.fin" 2>/dev/null)"
dire "octets du fichier de lecture : $(wc -c < "$ARBRE/diag/$RUNL/lecture-bbis.json" | tr -d ' ')"
"$PY" - "$ARBRE/diag/$RUNL/lecture-bbis.json" <<'EOF'
import json, sys
r = json.load(open(sys.argv[1], encoding="utf-8"))["resultat"]
g = r.get("garde")
print("clé garde présente :", g is not None)
if g is not None:
    print("nature du refus :", g.get("nature"))
    print("motif du refus :", g.get("refus"))
    print("preuve d'aucune ouverture conforme :", (g.get("aucune_ouverture") or {}).get("conforme"))
print("clé cellules présente :", "cellules" in r)
print("clé p3bis présente :", "p3bis" in r)
print("règle d'ordre des lignes :", (r.get("ordre_propre") or {}).get("regle"))
print("lecture réelle (essai faux) :", r.get("essai") is False)
print("fichiers ouverts par la chaîne :")
for p in r.get("entrees_lues") or []:
    print("  ", p)
EOF
} > "$C" 2>&1
sceller "registres/t07-etape-b-bis/lecture-v1/constat-forme-pour-le-juge-lecture-bbis-$N-v1.txt"
echo "constat de forme écrit, non affiché : $C $(sha256sum "$C" | cut -d' ' -f1)"
