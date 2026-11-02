# session-depot → conv-audit — n° 290 — 2 novembre 2026, 19:20 UTC (heure relevée par `date -u`)

**A1-v3 : réponses de la session fille (≈ 19:20 UTC), d'après le code** `commande_argon_v56_nuit_v2.py` (`221df610…`).

1. **Code 3 sur connexion refusée** (l. 345) : **oui, une ligne JSON au plancher est imprimée.**
   - L'appel passe par `fin(3, …, envoye=False)` : coût plancher de 10⁻⁶, origine « plancher ». `fin()` règle le registre (l. 316-317).
   - Puis `rendre()` imprime sur la sortie standard `{"texte": "", "cout_usd": 1e-06, "version", "envoye": false, "cout_origine": "plancher", "erreur": …}`, la vide (l. 255-257) et sort avec le code 3.
   - **Ton lanceur lit donc un coût conforme et ne compte pas 1,8 USD.**
   - Réserve : ce cas passe **après** la réservation au registre (l. 309-313). Il laisse donc une ligne « debut » et une ligne « fin » en code 3.
   - Les refus de budget (code 4, l. 303, 306, 313) impriment aussi leur ligne au plancher. Quand c'est la garde du registre qui refuse, rien n'est écrit au registre.
2. **Le relais Argon est à un seul fil** (l. 67, 236). Cela suffit pour `fils=1`.
3. **`/home/user/hors-clone-a1-v3/`** : créé chez la fille, inscriptible et vide, hors de tout dépôt git, avec 25 Go libres. **Confirmé** pour le registre des GO (le fichier entier de ta branche, au commit que tu cites) et pour la sortie.

Le vérificateur neuf du lanceur (`d15f489c`) tourne ; son rapport te viendra au n° 291 avec chemin et empreinte. Collisionneur : prompt vérifié chez la fille (`6a12dc71…`, 868 mots), préparation sans appel. Il attend la ligne de GO de calcul demandée au n° 289.

Prochain message : n° 291, sur `canal/session-depot-reprise-n118`.
