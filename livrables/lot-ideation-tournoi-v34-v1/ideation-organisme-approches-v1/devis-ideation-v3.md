# Course d'idéation de l'organisme — devis v3 (v2 + juge d'une autre lignée en bras rapporté)

Lignée conv-audit (instance de reprise, Fable 5.1), 28 octobre 2026, relevé `date -u` **17:07 UTC**. **Remplace le devis v2**
(gardé, R12) sur trois points ; tout le reste du v2 (pièces, plan, coûts, conditions, lecture) vaut.

1. **Décisions de Lazar (17:58 heure de Paris)** : (a) **oui** au juge d'une autre lignée (Gemini Argon, chez session-depot)
   en bras rapporté — extension de N-053 point 4 à ce tournoi ; (b) **oui** à l'ordre « extraits scellés → lancement » ;
   (c) **« go »** sur le devis une fois le chiffre de session-depot posé.
2. **Code : v33** (`orchestrateur-pole-v7/LISEZMOI-orchestrateur-pole-v7-v33.md`, 303 essais) : `--juge-externe
   argon=gemini-argon --commande-juge-externe "<commande d'appel d'Argon chez session-depot>"` — la commande reçoit la
   consigne anonymisée sur l'entrée standard, imprime `{"texte": …, "cout_usd": …}`, tient sa clé elle-même ; ses notes
   sont rapportées à part (`notes-bras-rapporte.json`, accord de rang avec le classement agrégé), **jamais agrégées** ;
   lecture ajoutée : **L5** — accord de rang entre le juge externe et le classement agrégé, et conformité des témoins chez
   lui ; plafond par session du juge externe : 3 USD (`--budget 'juge_ideation|gemini-argon=3'`) ; coût attendu de la course
   : ≈ 7 à 14 USD, plafond total **20** inchangé.
3. **Extraits scellés faits** (CL31-14) : `extraits-v1/` (11 fichiers : marque, section A, classement v2 §1-4, huit
   antériorités §1-3). **Liste blanche** : `ideation-organisme-approches-v1/liste-blanche-sans-temoins-v1.json` (question,
   11 extraits, 4 documents entiers, matériau ; 17 fichiers, chemins réels de ma copie) — session-depot la **reconstruit**
   chez lui avec `--construire-liste-blanche` en y ajoutant le fichier des **témoins du tiers**, vérifie que les 17
   empreintes coïncident avec les miennes, et scelle sa liste ; c'est elle qui est servie.
