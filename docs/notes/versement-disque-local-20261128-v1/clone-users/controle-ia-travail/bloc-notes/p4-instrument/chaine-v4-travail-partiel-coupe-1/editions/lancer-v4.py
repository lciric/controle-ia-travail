P = [
("""# code 2 du contrôle à cinq minutes ou de la surveillance après la création n'arrête rien d'office ; l'arrêt se fait
# alors à la main par arreter_p4_v1.sh, puis nœud.
""",
"""# code 2 du contrôle à cinq minutes ou de la surveillance après la création n'arrête rien d'office ; l'arrêt se fait
# alors à la main par arreter_p4_v1.sh, puis nœud. Chaîne v4 (VC2-fidelite-03) : la récupération est appelée avec
# l'arret.txt de l'arrêt (heure limite de destruction : 24 heures après l'arrêt relu) ; une ligne de plus dans
# lancement.txt, relue avant la création : l'heure limite de repli (création + 9 600 s + 24 heures) et le rappel que la
# session programme au lancement (geste de session) ; au-delà : nœud de Lazar.
"""),
("""(recuperation_p4_v1.sh %s <id> %s <dossier neuf>), 24 heures au plus après l arrêt (R10 ; texte, Plan d analyse, point 7)\\ntraces de la session""",
"""(recuperation_p4_v1.sh %s <id> %s <dossier neuf> <arret.txt de l arrêt>), 24 heures au plus après l arrêt relu dans arret.txt (R10 ; texte, Plan d analyse, point 7)\\nheure limite de destruction : 24 heures après l arrêt relu dans arret.txt ; sans arret.txt, repli déclaré par la récupération : %s (création + 9 600 s + 24 h) ; rappel programmé par la session au lancement (geste de session) ; dépassée : nœud de Lazar\\ntraces de la session"""),
("""    "$((CREATION + PLAFOND_SURVEILLANCE_S))" "$PLAFOND_SURVEILLANCE_S" "$T" "$((CREATION + 180))" "$((CREATION + 300))" "$T" "$S" "$T" >> "$T/lancement.txt\"""",
"""    "$((CREATION + PLAFOND_SURVEILLANCE_S))" "$PLAFOND_SURVEILLANCE_S" "$T" "$((CREATION + 180))" "$((CREATION + 300))" "$T" "$S" "$T" \\
    "$(date -u -d "@$((CREATION + PLAFOND_SURVEILLANCE_S + DISQUE_H * 3600))" +%FT%TZ)" >> "$T/lancement.txt\""""),
("""         "code 2 du contrôle à cinq minutes ou de la surveillance après la création : \\`arreter_p4_v1.sh <id> <dossier neuf>\\` à la main, puis nœud"; do""",
"""         "code 2 du contrôle à cinq minutes ou de la surveillance après la création : \\`arreter_p4_v1.sh <id> <dossier neuf>\\` à la main, puis nœud" \\
         "heure limite de destruction : 24 heures après l arrêt relu dans arret.txt ; sans arret.txt, repli déclaré par la récupération : $(date -u -d "@$((CREATION + PLAFOND_SURVEILLANCE_S + DISQUE_H * 3600))" +%FT%TZ) (création + 9 600 s + 24 h) ; rappel programmé par la session au lancement"; do"""),
]
