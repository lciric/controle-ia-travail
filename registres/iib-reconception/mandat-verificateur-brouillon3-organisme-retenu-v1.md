# Mandat du vérificateur du brouillon 3 du texte de l'organisme retenu — v1

Écrit le 2026-11-21 par la session de reconception (côté saboteur), reprise après l'arrêt du 19 novembre. Pièce de travail (classe C) qui ouvre la vérification d'une pièce décisive (classe A, R2). Accords : GO-2026-11-19-58, -64, -72 et GO-2026-11-21-63 (registres/go.md sur main).

## 1. Qui tu es, ce que tu ne lis pas
Agent neuf, Claude Opus 5.5, côté saboteur, dans le rôle du contre-lecteur du texte de l'organisme retenu. Le contre-lecteur des brouillons 1 et 2 n'est plus joignable (session arrêtée) : tu prends sa place et tu vérifieras ensuite les corrections. Tu n'as rien écrit de ce que tu lis. Français, aucun sigle seul.
Tu écris seulement dans `/tmp/claude-0/-home-user-controle-ia-travail/6e2b0069-d4f4-5fd1-be63-f516f6a3ee23/scratchpad/verificateur-brouillon3/`. Pas de commit, pas de poussée, pas de routine de reprise, jamais la suite d'essais complète, aucune dépense, aucune suppression de fichier. Au premier refus d'un outil (permission, crochet, classifieur) : arrêt, texte exact rendu, aucun contournement.
Interdits côté sondes : `prereg/lecture-sondes-barreau8-v1.md`, `src/controle_ia/barreau8_moniteurs/`, `brouillons/barreau8-lecture-sondes-v1/`, branche `lot/compte-4-v1`, ligne R-2059, `docs/verdicts/`. Aucune consigne privée recopiée.
Interdits des valeurs mesurées de la première course, hors les cinq données déclarées : dans `registres/`, seulement les fichiers nommés ci-dessous (donc ni le journal de session, ni la note `resultat-negatif-…`, ni son erratum, ni `verification-lecteurs-cout-v1/`) ; ni les branches `claude/iib-executante-v1` et `essai/iib-explo-v1`, ni les dossiers `diag/`, `donnees/`, `runs/`, `traces/` du saboteur à budget. Pas de recherche récursive large sur le dépôt.

## 2. Ce que tu lis
- La pièce : `brouillons/ii-b-saboteur-budget-v5/conception-organisme-retenu-ii-b-v5-brouillon3.md` (sha256 cb39c12b2aec2368542483bcb1ebe07ccc2855a48e516e907c8f0cf30e26e4a0), le fichier des différences avec le brouillon 2, le journal de rédaction v6, et toutes les pièces de son annexe C (grilles, scripts, sorties, heures, achèvement).
- Ce que les lectures précédentes ont demandé : `brouillons/ii-b-saboteur-budget-v5/contre-lecture-cl1/` (contre-lecture du brouillon 1, 4619baae…) et `brouillons/ii-b-saboteur-budget-v5/verification-cl1/` (vérification du brouillon 2, 84249ac2…), avec leurs rejeux. Le brouillon 2 pour comparaison.
- Ce que le rédacteur a reçu : `registres/iib-reconception/mandat-redacteur-conception-revisee-oracle-v1.md` et ses compléments 1 à 9 (même dossier).
- Les cinq données déclarées : `registres/iib-reconception/donnees-de-conception-premiere-course-v1/` (scripts et sorties).
- La conception d'origine : `brouillons/ii-b-saboteur-budget-v1/conception-ii-b-v1.md`. `CLAUDE.md` (R1 à R9, R12).

## 3. Ce que tu vérifies, sans complaisance
1. **Restes de la vérification du brouillon 2** (R1, R2, cinq mineurs) et demandes des compléments 8 et 9 : chacun traité, et bien ? Table : reste → où → traité / partiel / non.
2. **La règle composée de désignation (section 5.1)** : scellable seule avant l'étalonnage ? Aucune liberté après lui (ordre des essais, égalités, cas d'une condition incalculable, issue « ne part pas ») ? Chaque issue nomme-t-elle d'avance oracle, thèse, phrase ? Ses erreurs (10.4 bis : part à tort, ne part pas à tort, bascule) chiffrées d'après les sorties ? La page pour le directeur (5.3) dit-elle la plage à sa juste force, sans pencher ?
3. **L'épreuve de fuite (section 8)** : grille déclarée avant le passage (heures), niveau, puissance contre les deux fuites nommées, arrêt à tort de l'épreuve entière recalculé ; le passage aux quatre composantes à 1/80 est-il un réglage au vu d'un résultat ?
4. **Le contrôle chiffré du premier coût (section 6 bis)** : statistique, unité, usage, niveau fixé a priori, puissance sur gonflements plantés, plus petit gonflement vu (tour, étalonnage, course), coût en appels, phrase pour le jury, ce qu'il ne voit pas. Choix d'une statistique robuste justifié face aux valeurs rondes et à la queue lourde ? Le nœud 1 (usage en règle) bien posé ?
5. **L'incident du passage coupé** (journal v6) : rejoue au moins une configuration des 389 premières avec sa graine fille et une des 133 achevées ; dis si l'achèvement rend bien ce que le passage aurait rendu.
6. **Rejeu indépendant** : par un script à toi, à entropie neuve tirée par `numpy.random.SeedSequence` et consignée, au moins un point de la règle composée et un point de la pente de fuite.
7. **Chiffres** : sondage d'au moins quinze chiffres neufs du brouillon 3, chacun avec chemin et ligne de la sortie.
8. **Pièces manquantes** : l'annexe C cite `assembler-brouillon3-v1.py` et des fragments `b3-…`, absents du dépôt (perdus avec le conteneur du 19 novembre, à ce que je vois) ; douze fichiers du dossier v5 n'ont pas de compagnon `.sha256`. Dis ce que cela empêche de vérifier et la correction de texte à faire.
9. **Les sept nœuds (section 17)** : bien posés, options complètes, rien de tranché qui devait être rendu ? Est-ce que l'un d'eux empêche le scellement ?
10. **La spécification du code (section 13)** : suffit-elle à un développeur neuf pour les modules neufs (désignation, contrôle du premier coût, pente de fuite) ? Cas sain et artefact pour chaque garde (R5) ?

## 4. Ce que tu rends
`verification-conception-organisme-retenu-ii-b-v5-brouillon3-v1.md` dans ton dossier, avec tes scripts et sorties, chacun avec un compagnon `.sha256`. Verdict en tête (« scellable en l'état », « scellable après corrections », « à refaire ») ; remarques numérotées, classées bloquant, majeur, mineur, chacune avec le passage visé, ce qui ne va pas, et la correction proposée en couple « ancien texte → nouveau texte » quand c'est possible. Tu ne tranches aucun nœud. Rends le chemin, l'empreinte, le verdict et la liste des bloquants et majeurs en quinze lignes au plus.
