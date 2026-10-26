# Brief — contre-lecture du registre d'hypothèses, du protocole et des briefs d'agents de la boucle extérieure du pilote 4 — v1

Écrit par la lignée conv-audit le 26 octobre 2026 à 03:42 UTC (heure lue sur `date -u`) pour un sous-agent neuf, qui n'a
écrit aucun des textes à relire (règle R2 : contre-lecture par un agent qui n'est pas l'auteur). Langue : français, sans
acronymes. **Ton rôle est de chercher ce qui est faux, flou ou dangereux**, pas de confirmer.

## Ce que tu relis
Tout le dossier `/var/tmp/boucle-exterieure-pilote4-v2/sortie/` (registre d'hypothèses de conception v2, protocole de la
boucle extérieure, briefs des agents de fin de course, LISEZMOI de l'auteur, compagnons `.sha256` : vérifie-les d'abord).

## Ce qui fait foi
1. Les briefs que l'auteur a reçus : `/var/tmp/boucle-exterieure-pilote4-v2/LISEZMOI-brief-v2.md` (`bb472681…`) et
   `/var/tmp/boucle-exterieure-pilote4-v2/fournis/brief-boucle-exterieure-v1.md`.
2. Les pièces qu'il avait (lecture seule) : `/var/tmp/boucle-exterieure-pilote4-v2/fournis/` (empreintes :
   `../EMPREINTES-fournis-v1.txt`), en particulier le texte du pilote `pilote4-gemini-organisme-v4.md` (`782b858c…`), § Plan,
   points 3, 4 et 4 bis, et § Décisions ; la contre-lecture 7 (`…-cl7.md`, constats P4C7-01 et P4C7-02) ; le registre v1 ;
   le brief du script de lecture ; les hypothèses du pilote décisif (b). **Le texte du pilote prime** sur tout le reste.

## Ce que tu vérifies (au moins)
1. **Décidabilité** : chaque fiche du registre v2 se tranche par ce que la sortie du script de lecture donne (point 4 bis :
   bornes de Wilson par classe, test de McNemar génération 0 contre génération 3 avec Holm, scores sur les catégories
   absentes du train), ou bien elle est déclarée « indécidable par ce pilote » avec ce qu'il faudrait pour la trancher.
   Aucune fiche ne s'appuie sur le verdict « au-dessus de la référence » comme s'il était atteignable (P4C7-01) ; aucune ne
   compare les deux objets (P4C7-02).
2. **Multiplicité** : les verdicts des agents n'ajoutent pas de tests cachés au-delà des quatre au plus du point 4 bis ;
   sinon, ils sont déclarés descriptifs ou corrigés.
3. **Symétrie (règle R3)** : aucune fiche ne vise un signe ; les hypothèses nulles existent ; une issue qui conserve et une
   issue qui élimine ont chacune une règle écrite d'avance.
4. **Qui voit quoi et quand** : la retenue de lecture (aucun score lu avant la décision de Lazar sur les graines,
   transmise par conv-audit) ; les agents ne voient que la sortie du script, jamais le fichier secret de la banque,
   l'archive fermée ni un texte de tâche ; rien du registre ni des verdicts n'est servi à un organisme ; les scores de
   `test_final` ne vont à aucun organisme.
5. **Le correcteur** : il ne peut écrire ni critère ni stratégie de classement des tâches, ni connaissance d'une tâche de la
   banque, ni valeur de `test_final` ; la garde est-elle vérifiable par un tiers, et par quoi ?
6. **Audit des agents contre la confabulation** : le dispositif prévu (sortie simulée dont la vérité est connue,
   hypothèses permutées, ou autre) est-il faisable avec ce que le script produit, et assez aveugle pour l'agent audité ?
   La famille de modèle de l'agent qui « casse exprès » est-elle bien un paramètre laissé à Lazar ?
7. **Suites** : toute relance proposée est une course nouvelle, payante, sur le mot direct de Lazar dans la session de
   session-depot ; aucune dépense par défaut ; aucune graine de plus hors d'un texte nouveau.
8. **Cohérence** : chemins, empreintes et numéros de fiches cités existent et concordent ; la table « v1 → v2 » couvre
   toutes les fiches changées ; les écarts de l'auteur à son brief sont déclarés.

## Interdits (sans exception)
Aucun `git`, aucun sous-agent, aucun réseau, aucune clé ; tu ne lis que les deux dossiers ci-dessus ; aucun score
n'existe : n'en invente aucun ; aucun critère ni aucune stratégie de classement des tâches dans ce que tu écris ; heure lue
sur `date -u` dans la commande même où tu l'écris. N'écris que sous `/var/tmp/contre-lecture-boucle-exterieure-pilote4-v1/`.

## Ce que tu rends
`rapport-contre-lecture-boucle-exterieure-v1.md` : constats numérotés CLB-01, CLB-02… (fichier et ligne ; gravité :
« bloquant », « à corriger avant usage » ou « mineur » ; ce qui ne va pas ; correction proposée) ; verdict en une ligne :
« utilisable tel quel », « utilisable après corrections » ou « non utilisable » ; ce que tu n'as pas pu vérifier. Avec son
compagnon `.sha256`. À la fin, réponds en trois lignes : le verdict, les constats bloquants ou à corriger (numéros),
l'empreinte du rapport.
