P = [
("""# Chaîne v3 : vingt-six rapports synthétiques (RAPPORTS_NOMS) ; tokeniseur de substitution sur demande explicite
# (BANC_TOKENISEUR_SUBSTITUT=1), quand la copie de la session de tokenizer.json manque au bloc-notes : annoncé au journal,
# une ligne de plus changée dans la copie des contrôles (TOK_JSON) ; sans la demande, refus en code 2.""",
"""# Chaîne v3 : vingt-six rapports synthétiques (RAPPORTS_NOMS).
# Chaîne v4 (traitement de la vérification « fidélité » de la chaîne v2) : vingt-sept rapports synthétiques
# (VC2-fidelite-01) ; tokeniseur : la copie de la session restaurée (…/tokeniseur/, tokenizer.json 79e3e522…, sceau
# compagnon), exigée à ses deux empreintes, sinon refus en code 2 (VC2-fidelite-02 ; l'option de substitution de la
# chaîne v3 est retirée) ; garde gelée de S piégée (elle écrirait un témoin si elle était exécutée) : KO du bloc 12,
# empreinte relue juste avant le rejeu, garde non rejouée, témoin absent (A55, VC2-fidelite-12)."""),
("""# chaîne v3 : tokeniseur de substitution, sur demande explicite seulement (BANC_TOKENISEUR_SUBSTITUT=1), quand la copie de la
# session de tokenizer.json manque ou n'a pas son empreinte (bloc-notes restauré sans elle) : tokenizer.json synthétique,
# tokenizer_config.json réel exigé ; la ligne TOK_JSON de la copie des contrôles prend l'empreinte du substitut (une ligne
# de plus, comptée et écrite au journal) ; sans la demande : refus en code 2, comme avant. L'empreinte réelle reste
# éprouvée à la répétition finale, sur le vrai C.
SUBSTITUT=non
if [ "$(sha256sum "$TOK/tokenizer.json" 2>/dev/null | cut -d' ' -f1)" != "$TOK_JSON_REEL" ]; then
    [ "${BANC_TOKENISEUR_SUBSTITUT:-}" = 1 ] || { echo "copie de la session de tokenizer.json absente ou d'empreinte autre ($TOK) : banc impossible (BANC_TOKENISEUR_SUBSTITUT=1 pour un substitut annoncé)"; exit 2; }
    [ "$(sha256sum "$TOK/tokenizer_config.json" 2>/dev/null | cut -d' ' -f1)" = "$TOK_CONFIG_REEL" ] || { echo "tokenizer_config.json de la session absent ou d'empreinte autre : banc impossible"; exit 2; }
    mkdir -p "$R/tokeniseur-substitut" && cp "$TOK/tokenizer_config.json" "$R/tokeniseur-substitut/" \\
        && printf '{"essai": "tokenizer.json de substitution du banc des contrôles de P4 (copie de la session absente du bloc-notes restauré)"}\\n' > "$R/tokeniseur-substitut/tokenizer.json" || exit 2
    TOK=$R/tokeniseur-substitut; SUBSTITUT=oui
    echo "TOKENISEUR DE SUBSTITUTION (demandé) : tokenizer.json synthétique $(sha256sum "$TOK/tokenizer.json" | cut -d' ' -f1) au lieu de ${TOK_JSON_REEL:0:12}… (copie de la session absente) ; tokenizer_config.json réel ${TOK_CONFIG_REEL:0:12}…"
else echo "tokeniseur de la session : tokenizer.json ${TOK_JSON_REEL:0:12}…, tokenizer_config.json réel"; fi""",
"""# chaîne v4 (VC2-fidelite-02) : copie de la session restaurée, exigée à ses deux empreintes (et tokenizer.json à son sceau
# compagnon) ; sinon refus en code 2, aucun substitut
[ "$(sha256sum "$TOK/tokenizer.json" 2>/dev/null | cut -d' ' -f1)" = "$TOK_JSON_REEL" ] \\
    && [ "$(cat "$TOK/tokenizer.json.sha256" 2>/dev/null)" = "$TOK_JSON_REEL  tokenizer.json" ] \\
    && [ "$(sha256sum "$TOK/tokenizer_config.json" 2>/dev/null | cut -d' ' -f1)" = "$TOK_CONFIG_REEL" ] \\
    || { echo "copie de la session du tokeniseur ($TOK) absente, sans son sceau ou d'empreinte autre : banc impossible"; exit 2; }
echo "tokeniseur de la session (copie restaurée) : tokenizer.json ${TOK_JSON_REEL:0:12}… (sceau compagnon exact), tokenizer_config.json ${TOK_CONFIG_REEL:0:12}…\""""),
("""    "$(sha256sum "$CFG_RELUE" | cut -d' ' -f1)" "$CFG_RELUE" "$RAPPORTS" "$A" "$(sha256sum "$LOGJ" | cut -d' ' -f1)" \\
    "$( [ "$SUBSTITUT" = oui ] && sha256sum "$TOK/tokenizer.json" | cut -d' ' -f1)" <<'PYCOPIE' || exit 2""",
"""    "$(sha256sum "$CFG_RELUE" | cut -d' ' -f1)" "$CFG_RELUE" "$RAPPORTS" "$A" "$(sha256sum "$LOGJ" | cut -d' ' -f1)" <<'PYCOPIE' || exit 2"""),
("""src, dst, depot, relu_sha, relu, cfg_sha, cfg, rapports, rep_commit, rep_sha, tok_substitut = sys.argv[1:12]""",
"""src, dst, depot, relu_sha, relu, cfg_sha, cfg, rapports, rep_commit, rep_sha = sys.argv[1:11]"""),
("""if tok_substitut:                                  # chaîne v3 : substitut demandé (voir plus haut)
    t = rep(t, r"^TOK_JSON=[0-9a-f]{64}", f"TOK_JSON={tok_substitut}")
""", ""),
("""echo "lignes changées dans la copie des contrôles : $(diff "$HN/controles_avant_depense_p4_v1.sh" "$R/controles-essai.sh" | grep -c '^>') (DEPOT, sept épingles, bouchons de la suite et des mesures$( [ "$SUBSTITUT" = oui ] && echo " ; TOK_JSON du tokeniseur de substitution"))\"""",
"""echo "lignes changées dans la copie des contrôles : $(diff "$HN/controles_avant_depense_p4_v1.sh" "$R/controles-essai.sh" | grep -c '^>') (DEPOT, sept épingles, bouchons de la suite et des mesures)\""""),
("""jouer A52-garde-du-lanceur-autre 1 "empreinte de la garde gelée du lanceur ≠ module commun" "sed -i 's/^GARDE_SHA256=579f65c8/GARDE_SHA256=000f65c8/' $V/lancer_p4_v1.sh && resceller $V/lancer_p4_v1.sh" ":" "" "" 1""",
"""jouer A52-garde-du-lanceur-autre 1 "empreinte de la garde gelée du lanceur ≠ module commun" "sed -i 's/^GARDE_SHA256=579f65c8/GARDE_SHA256=000f65c8/' $V/lancer_p4_v1.sh && resceller $V/lancer_p4_v1.sh" ":" "" "" 1
# chaîne v4 (VC2-fidelite-12) : garde gelée de S piégée (sa première ligne écrirait un témoin si elle était exécutée) :
# KO du bloc 12, empreinte relue juste avant le rejeu, garde non rejouée ; témoin absent après le cas
{ printf 'import pathlib; pathlib.Path("%s").touch()\\n' "$R/garde-executee-A55"; cat .claude/hooks/garde_calcul.py; } > "$R/garde-piegee.py"
jouer A55-garde-de-s-piegee-non-rejouee 1 "garde de calcul de S d'empreinte autre que la garde gelée" "cp $R/garde-piegee.py .claude/hooks/garde_calcul.py" ":"
[ ! -e "$R/garde-executee-A55" ] && grep -q "^KO  garde de calcul de S d'empreinte autre que la garde gelée .* relue juste avant son rejeu : non rejouée$" "$R/sortie-A55-garde-de-s-piegee-non-rejouee.txt" \\
    && echo "    A55 : garde piégée jamais exécutée (témoin absent), refus du bloc 12 : CONFORME" \\
    || { echo "    A55 : garde piégée exécutée ou refus du bloc 12 absent : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
grep -q "^OK  garde de calcul : empreinte relue juste avant le rejeu" "$R/sortie-A00-sain.txt" \\
    && echo "    A00 : bloc 12, empreinte de la garde relue juste avant le rejeu : CONFORME" \\
    || { echo "    A00 : bloc 12 sans relecture de l'empreinte : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }"""),
]
