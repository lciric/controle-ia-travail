#!/bin/bash
# § 4.2 — relevé d'avant lancement
# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
# seulement, le bloc « § 4.2 » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/4-2-releve-avant-lancement.sh 1
. "$(dirname "$0")/commun.sh"
N="${1:-}"; exiger_numero "$N"
R="$T/releve-avant-lancement-$N.txt"; neuf "$R"; neuf "$T/run-lecture-$N.txt"; neuf "$T/commit-local-noms.txt"
RUNL="$(date -u +%Y%m%d-%H%M%S)-bbis-t07-lecture-v1"; printf '%s\n' "$RUNL" > "$T/run-lecture-$N.txt"
{
cd "$ARBRE" || exit 1
dire "== 4.2 avant le lancement n° $N, $(date -u +%Y-%m-%dT%H:%M:%SZ) ; run de lecture $RUNL"
dire "-- arbre de lecture"
egal "parent de la tête de l'arbre de lecture" "$TETE_TRAVAIL" "$(git rev-parse HEAD^1)"
egal "fichiers ajoutés par le commit local" 32 "$(git diff --name-status HEAD^1 HEAD | grep -c '^A')"
egal "fichiers changés ou retirés par le commit local" 0 "$(git diff --name-status HEAD^1 HEAD | grep -c -v '^A')"
git diff --name-only HEAD^1 HEAD | sort > "$T/commit-local-noms.txt"
egal "le commit local ajoute les entrées attendues, et elles seules" 0 "$(comm -3 "$T/commit-local-noms.txt" "$T/attendus-noms.txt" | wc -l | tr -d ' ')"
dire "tête de l'arbre de lecture : $(git rev-parse HEAD)"
vrai "aucun dossier de ce run de lecture" test ! -e "runs/$RUNL" -a ! -e "diag/$RUNL"
dire "-- journal du registre propre"
vrai "journal suivi par git" git ls-files --error-unmatch -- "$JOURNAL"
egal "journal : nombre de lignes" 1 "$(wc -l < "$JOURNAL" | tr -d ' ')"
egal "journal : lignes d'ouverture" 0 "$(grep -c 'OUVERTURE-BBIS' "$JOURNAL")"
dire "-- environnement"
dire "variables GIT_ de la session, noms seulement : $(env | cut -d= -f1 | grep '^GIT_' | sort | tr '\n' ' ')"
set -- $("${NETTOYE[@]}" "$PY" -c 'import os; r = sorted(k for k in os.environ if k.startswith("GIT_")); print(len(r), *r)')
egal "variables GIT_ restantes dans l'environnement nettoyé" 0 "${1:-illisible}"
[ "$#" -gt 1 ] && { shift; dire "noms restants (jamais leurs valeurs) : $*"; }
egal "variable BBIS_INSTANCE dans l'environnement nettoyé" absente "$("${NETTOYE[@]}" "$PY" -c 'import os; print("posée" if os.environ.get("BBIS_INSTANCE") else "absente")')"
dire "-- git répond dans l'environnement nettoyé (commandes neutres, en lecture)"
egal "tête lue par git nettoyé" "$(git rev-parse HEAD)" "$(G rev-parse HEAD 2>/dev/null)"
egal "dépôt non superficiel, lu par git nettoyé" false "$(G rev-parse --is-shallow-repository 2>/dev/null)"
egal "arbre de lecture propre, lu par git nettoyé (lignes de statut)" 0 "$(G status --porcelain --untracked-files=all 2>/dev/null | wc -l | tr -d ' ')"
vrai "git nettoyé rend le statut sans erreur" G status --porcelain --untracked-files=all
dire "-- base « mots et coût » : code de la pièce au commit cité"
vrai "commit cité par la ligne CODE-MOTS-ET-COUT-T06 présent" G cat-file -e "$C_PIECE^{commit}"
egal "pièce sur le disque égale à la pièce au commit cité" "$(G rev-parse --verify -q "$C_PIECE:scripts/mots_et_cout_t06_v3.py")" "$(git hash-object -- scripts/mots_et_cout_t06_v3.py)"
dire "-- contrôles que l'écriture du résultat rejouerait après le seuil, faits ici sur des fichiers hors données"
egal "nom du run de lecture à la forme exigée par le manifeste" oui "$(printf '%s' "$RUNL" | grep -q -E '^[0-9]{8}-[0-9]{6}-[a-z0-9][a-z0-9-]{0,62}$' && echo oui || echo non)"
vrai "dossiers runs et diag de l'arbre de lecture ouverts à l'écriture" test -d runs -a -w runs -a -d diag -a -w diag
vrai "aucun fichier de lecture ni compagnon à ce nom de run" test ! -e "diag/$RUNL/lecture-bbis.json" -a ! -e "diag/$RUNL/lecture-bbis.json.sha256"
egal "préenregistrement scellé conforme pour un manifeste décisif (prereg.exiger_prereg_scelle, sur le texte seul)" 0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb "$("${NETTOYE[@]}" PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$ARBRE/src" "$PY" -c 'import sys; from controle_ia.prereg import exiger_prereg_scelle; print(exiger_prereg_scelle(sys.argv[1]))' "$ARBRE/prereg/T0.7-etape-B-bis-v1.md" 2>&1 | tail -n 1)"
egal "fiche de code lisible, niveau décisif admis, entropie de plus de 64 bits (registre_bbis_v1.lire_fiche_code, commun_v1.exiger_entropie)" conforme "$("${NETTOYE[@]}" PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$ARBRE/src" "$PY" -c 'import sys; from controle_ia.t07bbis.registre_bbis_v1 import lire_fiche_code; from controle_ia.t07bbis.commun_v1 import exiger_entropie; f = lire_fiche_code(sys.argv[1]); exiger_entropie(int(f["entropie"]), reelle=True); print("conforme")' "$ARBRE/registres/t07-etape-b-bis/code-bbis-v2.json" 2>&1 | tail -n 1)"
dire "-- branche de l'arbre de lecture sur le distant (poussée par la conductrice), utilitaires du lancement"
egal "tête, sur le distant, de la branche de l'arbre de lecture" "$(git rev-parse HEAD)" "$(git ls-remote --heads origin "$BRANCHE_DISTANTE_ARBRE" 2>/dev/null | awk '{print $1}')"
vrai "utilitaire de détachement (nouvelle session de processus) présent" command -v setsid
vrai "utilitaire d'insensibilité à la fermeture du terminal présent" command -v nohup
vrai "utilitaire de relevé de l'état d'un processus présent" command -v ps
dire "-- versions (fils de calcul fixés à 1 par la ligne de lancement)"
egal "versions de numpy, scipy, torch" "2.4.6 1.17.1 2.14.1" "$("${NETTOYE[@]}" PYTHONDONTWRITEBYTECODE=1 "$PY" -c 'import numpy, scipy, torch; print(numpy.__version__, scipy.__version__, torch.__version__.split("+")[0])' 2>/dev/null)"
dire "python : $("$PY" -c 'import platform; print(platform.python_version())')"
dire "place libre : $(df -h "$T" | tail -1 | awk '{print $4}')"
conclure
} 2>&1 | tee "$R"
cp -n "$R" "$LV1/releve-avant-lancement-lecture-bbis-$N-v1.txt" && sceller "registres/t07-etape-b-bis/lecture-v1/releve-avant-lancement-lecture-bbis-$N-v1.txt"
