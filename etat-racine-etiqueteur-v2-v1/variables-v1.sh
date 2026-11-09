# Lecture exploratoire v2 de l'étiqueteur : variables et fonctions ; aucun secret, aucune valeur de clé (noms seulement).
RACINE=/home/user/etiqueteur-lecture-exploratoire-v2-v1
DEPOT=/home/user/controle-ia-travail
CODE=$RACINE/code
EPR=$CODE/docs/notes/epreuve-etiqueteur-v1
RELAIS_DIR=$CODE/docs/notes/ideation-organisme-v1/relais-kimi-v1
RELAIS_SCRIPT=$RELAIS_DIR/relais_kimi_v4.py
ORDRE_NOM=ordre-execution-lecture-exploratoire-etiqueteur-v2-v1.md
ORDRE=$CODE/docs/procedures/$ORDRE_NOM
QUESTION=$CODE/docs/procedures/ordre-exploratoire-etiqueteur-v2-brouillon1.md
ACTIONS=$CODE/donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl
TACHES=$CODE/donnees/t05-pilote-v1/taches-pilote-60-v1.json
REGISTRE_GO=$CODE/registres/go.md
NOTE_BLOQUES=$CODE/diag/etiqueteur-phase1-v1/analyse-v1/repartition-items-bloques-v1.md
SONDE_TIRAGE=/home/user/sonde-refus-lecteur-c-v1/tirage
COMMIT_SONDE=9bdcc6d88a6c812a86b2c99b2561d3e0e469939c
PHASE1=/home/user/epreuve-etiqueteur-phase1-v1
ENTREES=$RACINE/entrees
ESSAIS=$RACINE/essais
GEN=$RACINE/generation
FORMAT=$RACINE/lecture-format
PRINC=$RACINE/lecture-principale
RELAIS_F=$RACINE/relais-format
RELAIS_P=$RACINE/relais-principale
ANALYSE=$RACINE/analyse
CONSOLES=$RACINE/consoles
CR=$RACINE/compte-rendu
CRF=$RACINE/compte-rendu/compte-rendu-v1.md
VERSE=$CODE/diag/etiqueteur-lecture-exploratoire-v2-v1
PY=/home/user/controle-ia-travail/.venv/bin/python
VENV_L=$RACINE/venv-lecture
PYL=$RACINE/venv-lecture/bin/python
GO_ID=GO-2026-11-09-03
GO_ECHEANCE=2026-11-16
NOM_CLE_ARGON=GEMINI_API_KEY_2
NOM_CLE_KIMI=KIMI_API_KEY
NOM_CLE_CLAUDE=RR_ANTHROPIC_API_KEY_RIGAUD
PORT_RELAIS=8789
EMPREINTE_RELAIS=67f369518102b3f7408f28dab053a4d6f9bc2b676eadfaa338f55d39af99027e
EMPREINTE_BLOC_QUESTION=8f77e68b2f3a15acf761237cf630bf38fe079f839e279483355e28bb8998b607
EMPREINTE_ANALYSE_V5='7fe487d61b9affa42b4f123258d47ceeb3fa88c2cee0f3ae1bcf1548d748cb0f'
EMPREINTE_ESSAIS_ANALYSE_V5='f9ca7a9ffbfbfb58e445d5c5bbf7110b2ad21ef901547c78fd5f7c22ac00e7a9'
ESSAIS_ANALYSE_V5='53'
PLAFOND_HORS_CREDITS=100
PLAFOND_CLAUDE=50
MAX_APPELS_FORMAT=100
MAX_APPELS_PRINCIPALE=3015
FILS=2
BRANCHE=donnees/etiqueteur-lecture-exploratoire-v2-v1
COMMIT_CODE=$(cat /home/user/etiqueteur-lecture-exploratoire-v2-v1/entrees/commit-code-v1.txt 2>/dev/null)
ENTROPIE=$(cat /home/user/etiqueteur-lecture-exploratoire-v2-v1/entrees/entropie-v1.txt 2>/dev/null)
sans_cle() { env -i PATH=/usr/bin:/bin LANG=C.UTF-8 "$@"; }
filtrer_env() {
  local garder=" PATH HTTPS_PROXY https_proxy HTTP_PROXY http_proxy NO_PROXY no_proxy SSL_CERT_FILE LANG $* " v
  while IFS= read -r v; do case "$garder" in *" $v "*) ;; *) unset "$v" 2>/dev/null ;; esac; done < <(compgen -e)
  export PATH=/usr/bin:/bin LANG=C.UTF-8 SSL_CERT_FILE=/root/.ccr/ca-bundle.crt
}
