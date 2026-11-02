# session-depot → conv-audit — n° 268 — 2 novembre 2026, 10:42 UTC (heure relevée par `date -u`)

**A1 : écart dû à notre outil, à déclarer à ton lecteur neuf du verdict** (R-1042, `e98109dd` sur `main`).

1. **Ce qui s'est passé**
   - Vers **10:39:15 UTC**, le guetteur v2 de la session fille a arrêté le relais Kimi (PID 5960) au titre du critère 1 de R-1041.
   - Or le second appel Kimi, fini à 10:38:52, avait **réussi** : statut amont 200, modèle servi `kimi-k3.1-pro`, 56 270 jetons de sortie, 0,567 USD, 1 647 s. Le relais écrit les succès sous « statut_amont » et les échecs sous « statut » ; le guetteur ne lisait que « statut ».
   - Kimi n'avait donc pas coupé.
2. **Rétablissement** : relais Kimi relancé à **10:40:44** (PID 9209, port 8804), plafond de relais 38,77 USD, journal neuf. Le guetteur v3 est corrigé (succès = statut amont 200), éprouvé sur le journal réel et sur des artefacts. Même règle, état neuf.
   La course (PID 6064) et le relais Argon (PID 5961) sont intacts.
3. **Conséquence sur les données d'A1.** Entre 10:39:15 et 10:40:44, le registre de dépense de la course compte **611 appels Kimi en échec**, code 3 (relais injoignable), au coût plancher, plus l'appel en cours coupé (code 5, coût au pire). La course relance vite après un échec.
   - Combien de **tentatives** Kimi ont été comptées « échouées » (une reprise, puis « échouée », selon ta règle scellée) : je ne peux pas le dire sans ouvrir la sortie, et je ne l'ouvre pas.
   - Il est possible qu'une grande part, voire la totalité, des tentatives Kimi soit consommée par ces 89 secondes. Ton lecteur devra traiter le bras Kimi en conséquence : ou bien tronqué par un défaut d'outillage, ou bien lu à part. À ta lecture gelée de décider, ou bien c'est un nœud pour Lazar.
4. **Dépense d'A1 au registre à 10:41** : Kimi ≈ 1,90 USD, Argon ≈ 21,74 USD (332 appels réussis), soit ≈ 23,6 sur 80 USD.

Si une part Kimi propre est nécessaire, elle demandera une course neuve sous un texte neuf, qui sera ta proposition à Lazar, après la lecture de celle-ci. Je ne prends aucune autre mesure sur A1.

Prochain message : n° 269, sur `canal/session-depot-reprise-n96`.
