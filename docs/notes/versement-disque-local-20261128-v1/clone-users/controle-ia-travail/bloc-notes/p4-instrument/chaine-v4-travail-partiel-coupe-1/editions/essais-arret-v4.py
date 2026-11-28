P = [
("""# code 2, aucune demande d'arrêt) ; ligne prête pour registres/arrets.md aux quatre cellules du registre (VC2-depense-04).
# Usage : essais_arret_p4_v1.sh RACINE_NEUVE""",
"""# code 2, aucune demande d'arrêt) ; ligne prête pour registres/arrets.md aux quatre cellules du registre (VC2-depense-04).
# Chaîne v4 : A00 relit aussi la ligne « ARRÊT CONFIRMÉ : INSTANCE <id> ARRÊTÉE PAR SON IDENTIFIANT (<heure>) » d'arret.txt,
# une fois, à l'heure de l'arrêt relu : c'est la ligne que la récupération lit pour l'heure limite de destruction
# (VC2-fidelite-03) ; quatre cellules et date avec heure vérifiées (VC2-fidelite-05).
# Usage : essais_arret_p4_v1.sh RACINE_NEUVE"""),
("""    && [ "$(cat "$E/scenario-A00-sain/lectures")" = 2 ] && grep -q "^.*Z : vastai stop instance $ID demandé$" "$E/arret-A00/arret.txt" \\""",
"""    && [ "$(cat "$E/scenario-A00-sain/lectures")" = 2 ] && grep -q "^.*Z : vastai stop instance $ID demandé$" "$E/arret-A00/arret.txt" \\
    && [ "$(grep -cE "^ARRÊT CONFIRMÉ : INSTANCE $ID ARRÊTÉE PAR SON IDENTIFIANT \\([0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z\\)$" "$E/arret-A00/arret.txt")" = 1 ] \\"""),
("""    && echo "    A00 : heure de la demande et de l'arrêt écrites, ligne prête pour registres/arrets.md à quatre cellules (date et heure de l'arrêt relu), deux lectures : CONFORME" \\""",
"""    && echo "    A00 : heure de la demande et de l'arrêt écrites, ligne prête pour registres/arrets.md à quatre cellules (date et heure de l'arrêt relu), deux lectures, ligne « ARRÊT CONFIRMÉ » lue par la récupération : CONFORME" \\"""),
]
