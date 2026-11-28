P = [("""        ("- Récupération en échec (code 1, ou refus en code 2 faute de place disque ou de clonage) : aucune destruction ;\\n"
         "  la récupération écrit l'état de l'instance et l'heure limite de destruction (création + 9 600 s + 24 heures) ;\\n"
         "  nœud de Lazar.",
         "- Récupération en échec (code 1, ou refus en code 2 faute de place disque, de clonage ou pour des traces d'un autre\\n"
         "  lancement) : aucune destruction ; la récupération écrit l'état de l'instance et l'heure limite de destruction ;\\n"
         "  nœud de Lazar. L'heure limite de destruction est 24 heures après l'heure d'arrêt relue dans `arret.txt` (écrit par\\n"
         "  `arreter_p4_v1.sh`, passé à la récupération) ; sans lui, la récupération écrit le repli déclaré « création\\n"
         "  + 9 600 s + 24 heures » et sa raison. Toute récupération écrit cette heure ; dépassée, elle écrit « heure limite\\n"
         "  dépassée de N s : borne du disque dépassée : nœud de Lazar », sans retarder la destruction. La session programme\\n"
         "  au lancement un rappel à l'heure de repli, puis le remet à 24 heures après l'arrêt relu (consigne écrite dans\\n"
         "  `lancement.txt`)."))),""",
"""        ("- Récupération en échec (code 1, ou refus en code 2 faute de place disque ou de clonage) : aucune destruction ;\\n"
         "  la récupération écrit l'état de l'instance et l'heure limite de destruction (création + 9 600 s + 24 heures) ;\\n"
         "  nœud de Lazar. Elle exige 3 Go libres avant le clonage et relit\\n"
         "  l'instance absente de la liste après la destruction.",
         "- Récupération en échec (code 1, ou refus en code 2 faute de place disque, de clonage ou pour des traces d'un autre\\n"
         "  lancement) : aucune destruction ; la récupération écrit l'état de l'instance et l'heure limite de destruction ;\\n"
         "  nœud de Lazar. Elle exige 3 Go libres avant le clonage et relit l'instance absente de la liste après la\\n"
         "  destruction. L'heure limite de destruction est 24 heures après l'heure d'arrêt relue dans `arret.txt` (écrit par\\n"
         "  `arreter_p4_v1.sh`, passé à la récupération) ; sans lui, la récupération écrit le repli déclaré « création\\n"
         "  + 9 600 s + 24 heures » et sa raison. Toute récupération écrit cette heure ; dépassée, elle écrit « heure limite\\n"
         "  dépassée de N s : borne du disque dépassée : nœud de Lazar », sans retarder la destruction. La session programme\\n"
         "  au lancement un rappel à l'heure de repli, puis le remet à 24 heures après l'arrêt relu (consigne écrite dans\\n"
         "  `lancement.txt`)."))),""")]
