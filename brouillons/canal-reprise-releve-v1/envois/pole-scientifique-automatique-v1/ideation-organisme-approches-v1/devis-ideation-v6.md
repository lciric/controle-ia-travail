# Course d'idéation de l'organisme — devis v6 (Argon à poids égal et à égalité ; après la relecture CL3 de la v35)

Lignée conv-audit (instance de reprise, Fable 5.1), 28 octobre 2026, relevé `date -u` **21:40 UTC**. **Remplace le devis v5**
(gardé, R12) ; les points des v2 à v5 non contredits ici valent. Code : **v36** (317 essais, non contre-lue : relecture
ciblée v35 → v36 par un modèle ≠ Fable chez session-depot, condition 1 du GO). Rien n'est dépensé ici.

**Décisions de Lazar intégrées** (28 octobre, mots directs rapportés par session-depot, n° 118 et 119) : Argon **juge à
poids égal** (le « bras rapporté, jamais agrégé » des v2 à v5 tombe ; le différé reste) et **proposeur à égalité**.

1. **Plafonds, séparés** : côté Claude **17 USD** (`--budget-total-usd 17`, contrôles compris ; relais
   `--plafond-usd 17 --reserve-par-appel 3.5`) ; côté Argon **4 USD** (`--budget-externe-usd 4` : deux passes de proposeur à
   1 USD de plafond de session, un jugement à 1,5, appel de contrôle ≈ 0,01), tenu par le noyau **et** par la commande
   (`PLAFOND_SESSION_USD` lui est passé). Total ≤ 21 ; attendu ≈ 8 à 16 USD, Argon compris. Estimation Argon (SUPPOSÉ,
   barème non vérifié) : proposeur 0,3 à 0,8 par passe ; juge 0,4 à 1 (il lit désormais les pièces des juges et toutes les
   fiches, témoins compris, comme les juges Claude) ; à confirmer par session-depot sur son barème.
2. **Argon proposeur, dans la course** : `--proposeur-externe argon=gemini-argon --commande-externe "…"` ; la clé d'Argon
   existe donc pendant la course, dans un fichier en mode 600 sous un chemin **interdit en lecture aux agents Claude**
   (`tools=[]`, CL34-02, et chemin hors de la sortie), son chemin passé par `--variable-transmise CHEMIN_CLE_ARGON` (jamais
   un nom de clé : refusé). Il reçoit la question et les pièces (déjà vues par Argon au tour du collisionneur des sept
   questions). **Seconde passe** : `--attestation-materiau` écrite par un lecteur neuf (session-depot) après lecture de
   `preideation-interne-v1/fiches-anonymes.md`, scellée, sinon la course refuse avant tout appel.
3. **Argon juge, différé** : `--juge-externe argon-juge=gemini-argon` ; la course écrit sa consigne en attente et
   **aucun classement** ; après l'attestation du lecteur nommé (devis v4 point 1 ; champs `lecteur, lu_le,
   fiches_validees_sha256, consignes_en_attente_sha256`, **scellée**), le bras joue Argon (appel de contrôle, plafond
   externe vérifié avant) et écrit le classement **à trois juges** : médiane par critère, porte sur l'agrégat, unanimité,
   accords de rang par paire (L5 réécrite ci-dessous).
4. **Codes de sortie et aucun repli** : course 0 (en attente du bras) ou 4 (témoins échoués chez un juge Claude) ; bras 0
   lisible, 4 témoins échoués chez Argon (classement à trois juges écrit, illisible), **5** Argon sans réponse (panne,
   plafond, notes invalides : `classement-sans-bras.json` à deux juges, marqué « sans juge externe, illisible au sens du
   devis », jamais de « retenue »), 2 arrêt. Sur une course réelle, seule une commande externe peut jouer le bras.
5. **Commande d'Argon** (session-depot, scellée avec son empreinte, consignée au manifeste) : consigne sur l'entrée
   standard ; dernière ligne `{"texte", "cout_usd"}` avec un coût **toujours** présent, fini, strictement positif, aussi
   sur un échec (sortie ≠ 0) ; sans enveloppeur (au délai, tout le groupe de processus est arrêté) ; `ROLE_POLE` lui dit
   si elle propose ou juge.
6. **Lectures** (fixées d'avance) — L0 : témoins conformes chez **chacun des trois juges** (`lecture.json → temoins`,
   `temoins_juge_externe`) ; L1 : fiches validées / refusées / quarantaine par proposeur (Argon compris) et par passe,
   coûts Claude et externe contre plafonds ; L2 : part des éligibles à l'agrégat des trois, part des « questions » parmi
   les cinq premières, porte « unanimité » contre porte agrégée ; L3 : **accords de rang par paire** (Argon–Fable,
   Argon–Opus, Fable–Opus), auto-préférence des trois juges (Argon juge contre Argon proposeur aussi), longueur × total ;
   L4 : recoupement des cinq premières avec le tour interne, **passe 1 seulement** ; L5 (réécrite) : ce que l'agrégat à
   trois change par rapport à l'agrégat des deux juges Claude (`classements-par-juge.json`, rangs des cinq premières).
   Aucune lecture par proposeur ne sert à choisir un modèle (N-053, N-058) ; aucune lecture ne tranche l'ordre des questions.
7. **Ordre** : relecture v35 → v36 → pièces (17 + témoins du tiers, noms neutres) → liste blanche → attestation du
   matériau → machine, clés (Anthropic tournée ; Argon sous chemin interdit) → GO cité → course → lecture humaine →
   attestation → bras → versement scellé → contre-lecture → décision de Lazar.
