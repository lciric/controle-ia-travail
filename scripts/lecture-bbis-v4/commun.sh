# Fichier commun des scripts de la commande de lecture, version 4 (étape B bis de T0.7) : paramètres et fonctions.
# Relu par chaque script. Porte le fichier des paramètres de la version 3 ; ne supprime rien, ne réécrit rien.
DEPOT=/home/user/controle-ia-travail
T=/tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis-v4
ARBRE="$T/arbre-de-lecture-v4"
PY="$DEPOT/.venv/bin/python"
LV1="$DEPOT/registres/t07-etape-b-bis/lecture-v1"
RUN_7B=20261111-151701-t06-reel
RUN_BBIS=20261118-154143-bbis-t07-v1
RUN_MC=20261116-205721-mots-et-cout-t06
RUN_B=20261114-001352-t07-lecture-reel
MAIN_INSCRIPTIONS=4aefb5b166b55a5ff7341454770a64caab923f52
FICHIER_DE_LA_CONDUCTRICE="$T/parametres-conductrice-v4.txt"
if [ ! -f "$FICHIER_DE_LA_CONDUCTRICE" ]; then echo "$FICHIER_DE_LA_CONDUCTRICE absent : l'opérateur l'écrit par l'outil d'écriture de fichiers ; arrêt"; exit 1; fi
if [ "$(grep -c '^TETE_TRAVAIL=' "$FICHIER_DE_LA_CONDUCTRICE")" != 1 ]; then echo "$FICHIER_DE_LA_CONDUCTRICE : une ligne TETE_TRAVAIL=, et une seule, attendue ; arrêt"; exit 1; fi
TETE_TRAVAIL="$(grep '^TETE_TRAVAIL=' "$FICHIER_DE_LA_CONDUCTRICE" | cut -d= -f2)"
if ! printf '%s' "$TETE_TRAVAIL" | grep -q -E '^[0-9a-f]{40}$'; then echo "TETE_TRAVAIL : 40 caractères hexadécimaux attendus ; arrêt"; exit 1; fi
COURSE=438a9c5257bdc4fa65f25c42cc89753a049b4586
C_CONJ=c098fb512d999e1dbf7cef5fba6430ff8b1a8fb5
C_REMISE=06c8832819af344d01c184222833c5a42e8ac901
C_FICHE=05cd22aa15382f61eb62b9e7817890dde728dd5f
C_PIECE=da06bb57610f840152e4e9a8c449b036577cc582
REF_SORTIES=refs/remotes/origin/donnees/t07-etape-b-bis-v2
TETE_SORTIES=7322049dbbc10975ec1fa7dd54c10c8bc1ec4cf9
REF_7B=refs/remotes/origin/calcul/t06-confirmation-7b-v1
TETE_7B=55c3e3eb89a4650419f35999aaa4c54288275b0d
REF_MC=refs/remotes/origin/verdict/t06-mots-et-cout-compte-3-v1
PROPRE=registres/t07-etape-b-bis-v1.md
VOISIN=registres/t07-etape-b-bis-v1-addenda-v1.md
PARTAGE=registres/scellements-v1.md
JOURNAL=registres/t07-etape-b-bis-v1.md.ouvertures.md
MODULE=src/controle_ia/t07bbis/lecture_v5.py
BRANCHE_DISTANTE_ARBRE=claude/lecture-verdict-etape-b-bis-v1-arbre-de-lecture
BRANCHE_LOCALE_ARBRE=lecture/bbis-arbre-de-lecture-v4
NETTOYE=(env -u GIT_SSL_CAINFO -u GIT_ASKPASS -u GIT_EDITOR -u GIT_TERMINAL_PROMPT -u GIT_CONFIG_COUNT -u GIT_CONFIG_KEY_0 -u GIT_CONFIG_KEY_1 -u GIT_CONFIG_KEY_2 -u GIT_CONFIG_VALUE_0 -u GIT_CONFIG_VALUE_1 -u GIT_CONFIG_VALUE_2 -u BBIS_INSTANCE)
G() { "${NETTOYE[@]}" git -C "$ARBRE" "$@"; }
FAUTES=0
dire() { printf '%s\n' "$*"; }
egal() { if [ -n "$2" ] && [ "$2" = "$3" ]; then dire "CONFORME : $1"; else dire "DEFAUT : $1 (attendu « $2 » ; relevé « $3 »)"; FAUTES=$((FAUTES+1)); fi; }
vrai() { local l="$1"; shift; if "$@" >/dev/null 2>&1; then dire "CONFORME : $l"; else dire "DEFAUT : $l"; FAUTES=$((FAUTES+1)); fi; }
conclure() { dire "FAUTES : $FAUTES"; if [ "$FAUTES" = 0 ]; then dire "CONCLUSION : conforme, on continue"; else dire "CONCLUSION : ON NE LANCE PAS"; fi; }
neuf() { if [ -e "$1" ]; then echo "$1 existe déjà : on n'écrase jamais ; arrêt"; exit 1; fi; }
sceller() { ( cd "$DEPOT" && PYTHONPATH=src "$PY" -m controle_ia.scellement sceller "$1" ); }
# -- forme de la version 4
numero_neuf_du_releve_des_tetes() { local k=1; while [ -e "$T/releve-mise-en-place-$k.txt" ]; do k=$((k+1)); done; echo "$k"; }
dernier_releve_des_tetes() { local k=1; while [ -e "$T/releve-mise-en-place-$((k+1)).txt" ]; do k=$((k+1)); done; echo "$T/releve-mise-en-place-$k.txt"; }
exiger_numero() { if [ "$1" != 1 ]; then echo "numéro du lancement « $1 » : cette version ne joue que le lancement 1, donné en argument ; arrêt"; exit 1; fi; }
