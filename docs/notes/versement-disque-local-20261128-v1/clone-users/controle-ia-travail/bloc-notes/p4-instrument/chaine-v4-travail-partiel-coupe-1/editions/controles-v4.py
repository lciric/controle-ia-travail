P = [
("""# texte de S (égal au candidat relu), -B et PYTHONDONTWRITEBYTECODE=1.
""",
"""# texte de S (égal au candidat relu), -B et PYTHONDONTWRITEBYTECODE=1. Chaîne v3 : vingt-six rapports ; trois refus de la
# récupération ; repli de l'affichage. Chaîne v4 (traitement de la vérification « fidélité » de la chaîne v2) :
# vingt-sept rapports (RAPPORTS_NOMS du module commun) ; journal de la répétition jouet à six passages (le sixième :
# délai externe du run), neuf récupérations conformes, état et heure limite dans les trois refus, deux replis de
# l'affichage ; bloc 12 : empreinte de la garde gelée relue immédiatement avant son rejeu, égale à celle du module
# commun (GARDE_SHA256), sinon KO et aucun rejeu (VC2-fidelite-12).
"""),
("""    ok "répétition jouet au commit répété et au candidat relu : journal épinglé, scellé ; cinq passages, sept récupérations conformes suivies de la destruction, vingt-sept artefacts refusés à leur KO, trois refus (état et heure limite dans ceux de la place et du clonage), repli de l'affichage ;""",
"""    ok "répétition jouet au commit répété et au candidat relu : journal épinglé, scellé ; six passages (délai externe du run compris), neuf récupérations conformes suivies de la destruction, vingt-sept artefacts refusés à leur KO, trois refus (état et heure limite dans chacun), deux replis de l'affichage ;"""),
("""# 12. garde de calcul sur le registre de S (jamais contournée)
echo '{"tool_input":{"command":"GO_ID=GO-2026-10-20-07 vastai create instance 1 --raw"}}' | python3 .claude/hooks/garde_calcul.py 2> "$W/garde.txt" \\
    && ok "garde de calcul : registres/go.md de S lisible, GO-2026-10-20-07 accepté" || ko "garde de calcul sur le registre de S : $(tail -1 "$W/garde.txt" | cut -c1-160)\"""",
"""# 12. garde de calcul sur le registre de S (jamais contournée) ; chaîne v4 (VC2-fidelite-12) : son empreinte est relue
# immédiatement avant le rejeu et comparée à celle du module commun (GARDE_SHA256, la garde gelée de 7a54d43) : autre ou
# illisible, KO et aucun rejeu
GARDE_GELEE=$(sed -n 's/^GARDE_SHA256 = "\\([0-9a-f]\\{64\\}\\)".*/\\1/p' "$VERIF")
GARDE_LUE=$(sha256sum .claude/hooks/garde_calcul.py 2>/dev/null | cut -d' ' -f1)
if ! [[ "$GARDE_GELEE" =~ ^[0-9a-f]{64}$ ]] || [ "$GARDE_LUE" != "$GARDE_GELEE" ]; then
    ko "garde de calcul de S d'empreinte autre que la garde gelée (${GARDE_LUE:-illisible} ; ${GARDE_GELEE:-illisible} attendue), relue juste avant son rejeu : non rejouée"
else
    echo '{"tool_input":{"command":"GO_ID=GO-2026-10-20-07 vastai create instance 1 --raw"}}' | python3 .claude/hooks/garde_calcul.py 2> "$W/garde.txt" \\
        && ok "garde de calcul : empreinte relue juste avant le rejeu (${GARDE_LUE:0:12}…) ; registres/go.md de S lisible, GO-2026-10-20-07 accepté" \\
        || ko "garde de calcul sur le registre de S : $(tail -1 "$W/garde.txt" | cut -c1-160)"
fi"""),
]
