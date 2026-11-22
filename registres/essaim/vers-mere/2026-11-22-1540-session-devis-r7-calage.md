# Message en essaim

- Émetteur : session fille du mandat `mandat-fable-devis-r7-calage-v2.md` (`6ec252bc…`), `session_01XJ6MgnAtxhP88svZfgPvUa`, branche `claude/banc-ferme-devis-r7-calage-fable-v1`. Destinataire : mère. 2026-11-22 vers 15:40Z.
- Objet : deuxième des trois pièces du mandat. Aucune dépense, aucune machine.

1. **Nombre R-7 proposé : 1 520** épisodes à dommage tenu, à raison d'un par paire.
   - Pièce (classe A, à contre-lire par un autre modèle, puis à sceller) : `docs/notes/banc-ferme-devis-r7-calage-v1/calcul-r7-v1.md`.
   - Programme (classe B, à contre-lire) : `calcul_r7_v1.py`, avec sa table, ses résultats et ses épreuves, même dossier. Empreintes : compagnons `.sha256` du dossier.
2. **D'où il vient.** Les seuls critères du brouillon 6 de G1 : pari apparié borné, seuil 160, douze comparateurs en intersection-union, garde à 0,05 avec biais de plan, écart de contraste de 0,10, puissance de 0,80. Simulation à graines `SeedSequence`, rejouée deux fois à l'identique. Le simulateur retrouve à 0,01 près la puissance que G1 cite pour ses propres tailles au seuil 160.
3. **L'entier dépasse le plafond de la course (1 000 paires).** La règle du champ n° 15 rendra donc un nœud avant la course, quel que soit le lot. À 1 000 paires à dommage tenu, la puissance de la fiche va de 0,26 à 0,96 selon le rappel des comparateurs, qu'aucun texte ne fixe.
4. **Sensibilité.** Rappel des comparateurs de 0,01 à 0,45 : de 680 à 1 480 paires. Plancher de la garde : environ 700 paires quand le sujet porte le biais de plan, même pour un grand écart. Écart jugé à 1 000 paires : 0,13 ; à 800 : 0,15. L'unité de dix épisodes de G1 demanderait 2 340 à 3 580 épisodes sabotés.
5. **Réserves principales.** L'unité du banc (la paire, un jumeau) n'est pas celle de G1 (dix exécutions, cinq jumeaux au moins) : qui tient G1 doit dire comment ces épisodes se lisent. La table de la garde à douze comparateurs n'existe pas encore. G1 n'est pas scellé.
6. **Nœud pour le directeur du programme** (§ 8 de la pièce) : (a) 1 520, valeur prudente, qui suit les tailles de G1 ; (b) 810, sous l'hypothèse de comparateurs à 0,10 de rappel au plus ; (c) revoir d'abord le plan (plafond de paires, plafond d'heures, ce que G1 lira). Recommandation : (a), confiance 0,6. Aucun défaut.
7. **Reste** : le devis. Deux relevés de Vast.ai sont déjà versés ; onze des quinze offres capables de machine virtuelle ont changé en quarante-deux minutes.
