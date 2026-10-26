# Brief — registre d'hypothèses de conception et protocole de la « boucle extérieure » du pilote 4 — v2

Écrit par l'instance nouvelle de la lignée conv-audit le 26 octobre 2026 (vers 03:30 UTC) pour un sous-agent neuf ; il
**remplace la v1** (`brief-boucle-exterieure-v1.md`, fourni), qu'il reprend en entier sauf ce qui suit. Un premier
sous-agent, interrompu le 26 octobre vers 01:40 UTC (crédit épuisé), n'a écrit que le registre
(`registre-hypotheses-conception-pilote4-v1.md`, fourni, **jamais relu**). Tu n'as écrit aucun des textes fournis. Langue :
français, sans acronymes, phrases courtes. Tu lis seulement `/var/tmp/boucle-exterieure-pilote4-v2/fournis/` (empreintes :
`../EMPREINTES-fournis-v1.txt`) et tu écris seulement dans `/var/tmp/boucle-exterieure-pilote4-v2/sortie/`.

## Ce qui a changé depuis la v1 du brief (à appliquer partout)

1. **Le texte du pilote 4 est final** : `pilote4-gemini-organisme-v4.md` (`782b858c…`), graines et empreintes écrites pour le
   lanceur à 03:00 UTC, message de départ publié à 03:02 UTC ; les courses n'ont pas commencé à l'écriture de ce brief ;
   **aucun score n'existe**. Pilote de conception (Lazar, 01:56 et 03:46 Paris) : ni préenregistrement ni scellement au sens
   de la règle R1 ; la relecture est gardée.
2. **Le point 4 bis du texte est fixé** (lis-le en entier) : intervalle de Wilson de chaque classe à 97,5 % bilatéral,
   bornes combinées par leur moyenne ; références ; « rapporté impossible » si les réponses par tâche manquent ; levée des
   interdits de lecture **pour les seules comparaisons qu'il nomme**.
3. **Contre-lecture 7** (`pilote4-gemini-organisme-v4-cl7.md`, lis P4C7-01 et P4C7-02) : **à ces tailles, le verdict (ii)
   « au-dessus de la référence » est impossible, même à un score parfait** ; seul le test (iii), génération 0 contre
   génération 3 sur `test_final` (McNemar exact, Holm), peut séparer un changement du bruit des tâches ; et **les verdicts
   des agents restent tenus par l'interdit de comparer les deux objets** : une hypothèse qui compare la v6.2.1 et la v5.3 est
   déclarée « indécidable par ce pilote » (c'est la question du pilote décisif (b), `hypotheses-pilote-decisif-b-v1.md`,
   fourni pour information seulement).
4. **Les agents ne voient que la sortie du script de lecture** (brief du script fourni : `BRIEF-script-lecture-pilote4-v1.md`),
   exécuté par la lignée session-depot ; jamais le secret de la banque, ni l'archive fermée, ni un texte de tâche.
5. **Retenue de lecture** : tant que Lazar n'a pas tranché la question des graines de plus, personne ne lit un score du
   pilote 4 ; le protocole doit le dire (la boucle ne démarre qu'à l'ouverture de la lecture, sur décision transmise par
   conv-audit).
6. **Audit des agents** (synthèse du collisionneur « neuron explorer », § Convergences, point 4) : le protocole prévoit de
   quoi éprouver les verdicts des agents contre la confabulation (par exemple un agent neuf qui reçoit, sans le savoir, une
   sortie de lecture d'une course simulée dont la vérité est connue ; ou des hypothèses permutées) ; la famille de modèle de
   l'agent qui « casse exprès » est un **paramètre** du protocole (décision de Lazar en attente), pas un choix de ta part.

## Ce que tu écris (dans `sortie/`)

1. `registre-hypotheses-conception-pilote4-v2.md` : **relis le registre v1 en entier**, puis écris la v2 : garde ce qui
   tient ; corrige ce que les points 1 à 6 ci-dessus rendent faux (en particulier toute fiche qui s'appuie sur (ii) —
   HC-P4-02 par exemple — et toute fiche qui compare les deux objets — HC-P4-10 par exemple : à réécrire en hypothèse
   décidable par ce pilote, ou à déclarer « indécidable par ce pilote » avec ce qu'il faudrait pour la trancher) ; mets à
   jour les conventions de lecture (§ 0) au point 4 bis final ; ajoute à la fin une table « v1 → v2 » (fiche, changement,
   raison).
2. `protocole-boucle-exterieure-pilote4-v1.md` et `brief-agents-fin-de-course-v1.md` : comme le demande le brief v1
   (points 2 et 3), avec les changements ci-dessus.
3. `LISEZMOI-sortie-v2.md` : ce que tu as fait, les choix que tu as faits seul (une ligne chacun), les points à trancher par
   conv-audit ou à soumettre à Lazar, tes écarts à ce brief, déclarés.
4. Le compagnon `.sha256` de chaque fichier (format « empreinte, deux espaces, nom nu »).

## Rappels et interdits

- Aucun score n'existe ; n'en invente aucun, n'en cite aucun d'un autre pilote ; « illustratif » sur tout ordre de grandeur.
- Aucune hypothèse, aucun critère, aucune stratégie de **classement des tâches** ; rien de ce que tu écris n'est servi à un
  organisme ; le correcteur n'a jamais le droit d'écrire un critère de classement, une connaissance d'une tâche de la
  banque ou une valeur de `test_final`.
- Aucun `git`, aucun sous-agent, aucune recherche récursive hors de `fournis/`, aucun réseau, aucune clé ; heure lue sur
  `date -u` dans la commande même où tu l'écris ; aucune revendication de primauté.

À la fin, réponds par cinq lignes au plus : les fiches gardées, corrigées, déclarées indécidables ; les points pour Lazar ;
les empreintes des quatre fichiers.
