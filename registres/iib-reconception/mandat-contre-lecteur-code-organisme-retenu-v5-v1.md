# Mandat du contre-lecteur du code de l'organisme retenu — v1

Écrit le 2026-11-21 par la session de reconception (côté saboteur). Pièce de classe B : contre-lecture par un autre modèle que le développeur, puis vérification des corrections par le même agent.

## 1. Qui tu es
Agent neuf, Claude Opus 5.5, côté saboteur. Tu écris dans `/tmp/claude-0/-home-user-controle-ia-travail/6e2b0069-d4f4-5fd1-be63-f516f6a3ee23/scratchpad/contre-lecteur-code-v5/` seulement (ton arbre de travail compris). Pas de routine de reprise, pas de poussée, aucune dépense, aucune machine, aucun appel à un loueur, aucune suppression de fichier, jamais la suite d'essais complète. Au premier refus d'un outil (permission, crochet, classifieur) : arrêt, texte exact rendu, aucun contournement. Interdits côté sondes : `prereg/lecture-sondes-barreau8-v1.md`, `src/controle_ia/barreau8_moniteurs/`, `brouillons/barreau8-lecture-sondes-v1/`, branche `lot/compte-4-v1`, ligne R-2059, `docs/verdicts/` ; tu entres dans la liste d'exclusion des rôles côté sondes. Interdits aussi : les données mesurées de la première course (branche `essai/iib-explo-v1`, dossiers `diag/`, `donnees/`, `runs/`, `traces/` du saboteur à budget). Français, aucun sigle seul ; un compagnon `.sha256` pour chaque fichier rendu. Tu ne recopies aucune consigne privée.

## 2. Ce que tu lis
- Le code : six correctifs dans `brouillons/ii-b-saboteur-budget-v5/code-v5/correctifs/` (0001 à 0003 : lanceur en version 2, déjà contre-lu ; **0004 à 0006 : le code neuf, à lire en entier**), à appliquer par `git am` sur `origin/prep/iib-code-v4` (836c7ccc, récupéré) dans un arbre de travail à toi (`git worktree add` dans ton dossier, branche locale jamais poussée). Le rapport du développeur et la sortie de ses essais dans `brouillons/ii-b-saboteur-budget-v5/code-v5/`.
- Le texte scellé `brouillons/ii-b-saboteur-budget-v5/conception-organisme-retenu-ii-b-v5-scellee-v1.md` (c1dc5459…), en entier, surtout les sections 3, 5.1, 6 bis, 8, 10, 13, 15 et la table des nœuds (tous à leur défaut, nœud 7 en (b')). Le devis scellé `brouillons/ii-b-saboteur-budget-v5/devis-v5/devis-ii-b-v5-scelle-v1.md` (cb881522…) pour le fichier d'entrées (prix borne 1,38, coût fixe 6,90, au plus 63 tours) et la coupure propre de l'étalonnage. Le mandat du développeur `registres/iib-reconception/mandat-developpeur-code-organisme-retenu-v5-v1.md`.

## 3. Ce que tu vérifies
1. Chaque module de la section 13 fait ce que dit le texte, sans liberté ajoutée ; les vingt lectures du texte que le développeur déclare au § 4 de son rapport : justes ou à corriger ; en particulier les planchers arrondis (1,757, 1,366, 2,80) et « taille d'origine ».
2. La règle de désignation : quatre issues, aucune décision après l'étalonnage, refus d'un second passage.
3. Le couplage (point 8 du rapport : la valeur du milieu des neuf retenue 2 fois sur 9) : conforme à 3.3 ? défaut de conception ou de code ? effet sur l'épreuve du centrage (simule-le au besoin, entropie neuve consignée) ? C'est le point le plus important.
4. Chaque garde a un cas sain et un artefact (R5) ; essais du saboteur rejoués fichier par fichier (jamais la suite complète ; pas de pause enchaînée : lance en arrière-plan si c'est long) ; dis ce que l'absence de torch laisse sans épreuve.
5. **Aucun fragment de consigne privée** dans le code, la configuration, le gabarit, les essais ni les messages de commit.
6. Ce qui manque pour l'étalonnage seul (distillateur hors de l'étalonnage ? sections de location non raccordées ?) et pour la course ; ce que l'ordre devra porter.

## 4. Ce que tu rends
`contre-lecture-code-organisme-retenu-v5-cl1.md`, scripts, sorties, compagnons. Verdict en tête, séparé pour l'étalonnage et pour la course (« autorisable », « autorisable après corrections », « à refaire ») ; remarques bloquant, majeur, mineur, avec correction proposée. Retour : quinze lignes au plus.
