# Consigne du contre-lecteur — brouillon 6 (relance du 19 novembre 2026) du préenregistrement du papier C — v1

Écrite par la session de conduite, sous l'accord GO-2026-11-19-41 et le mandat `registres/papier-c/mandat-redaction-preenregistrement-papier-c-v1.md` (`cfe4a3c3…`), qui fait foi. Règle R2 : tu es un agent neuf, d'un autre modèle que le rédacteur ; tu n'as rien écrit de ce texte. Langue : français, sans sigle seul.

## 1. Ce que tu relis
Dans `/tmp/claude-0/-home-user-controle-ia-travail/ea38fd7e-2b5a-5aae-9611-af6160a314d6/scratchpad/bloc-notes/redacteur/` (lecture seule pour toi) :
- le brouillon 6 de relance `papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19.md` (pièce principale ; commence par en prendre l'empreinte sha256 et écris-la en tête de ton rapport) ;
- la note des différences `note-differences-brouillon5-brouillon6-relance-v1.md` ;
- la liste des décisions du directeur `decisions-du-directeur-exigees-v1.md` ;
- la sortie du validateur `problemes-brouillon6-relance-v1.txt`.

## 2. Contre quoi (dépôt `/home/user/controle-ia-travail`)
- `CLAUDE.md` : règles gelées R1 à R14, interdits, liste des décisions.
- Le brouillon 5 : `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md` (`9d55160f59cf…`).
- Le gabarit `prereg/gabarit-preregistrement-v1.md`, le validateur `src/controle_ia/prereg.py` (relance-le toi-même : `PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 python3 -B -c "from controle_ia.prereg import problemes; print(problemes('<chemin>'))"`).
- Décisions, dans `docs/decisions/` : `decision-N-005-N-006-v1.md`, `decision-N-013-v1.md`, `decision-N-023-v1.md`, `decision-N-064-v1.md`, `decision-N-065-v1.md`, `decision-N-066-v1.md`, `decision-N-067-v1.md`, `decision-N-068-v1.md`, `decision-resserrement-juge-au-nul-v1.md`, `decision-N-073-revendications-apres-veille-exploration-idees-v1.md` et ses compléments 1, 2, 3.
- Le programme et le brief : `docs/programme-controle-ia-v2.md`, `docs/brief-claude-code-programme-complet-v2.md` (sections du papier C).
- L'état de l'art vérifié : `docs/etat-de-l-art/` ; rapports de lecteurs sur les branches `prep/etat-de-l-art-niveau3-pieces-v1` et `prep/etat-de-l-art-niveau3-v1` (`git fetch origin <branche>` puis `git show origin/<branche>:<chemin>`, sans changer de branche).
- `registres/decisions.md`, `registres/go.md` par recherche ciblée seulement (voir interdits).

## 3. Ce que tu vérifies — contre-lecture complète
1. **Conformité aux décisions en vigueur.** HC2 : énoncé retenu de N-068, section 4, mot pour mot ; ce qui n'est plus revendiqué ne l'est plus ; plan apparié non dit neuf ; citations obligatoires présentes avec la formulation imposée ; contre-indices dits avec la prédiction ; lettre de N-013 pour HC4 restreinte ; sources de HC2b complétées. Même examen pour HC1, HC3 et tout ce que N-005, N-006, N-013, N-023, N-064 à N-067, N-071, N-073 (et compléments) imposent là où le texte y touche.
2. **Aucune revendication neuve.** Chasse toute phrase qui revendique plus que les décisions ne le permettent, ou qui présente comme neuf ce qui est publié. Chaque cas : citation exacte, ligne, décision violée.
3. **Aucun chiffre de l'état de l'art non vérifié (R7).** Pour chaque chiffre tiré d'un article : remonte à la pièce vérifiée (chemin, empreinte, page) ; contrôle par programme quand c'est possible (recherche du chiffre dans la pièce source) ; signale tout chiffre sans source vérifiée, toute mention « opposable » indue. R6 : tout chiffre renvoie à un chemin et une empreinte ; vérifie un échantillon large d'empreintes citées contre les fichiers.
4. **R1, complétude et cohérence interne.** Pour chaque hypothèse traitée : hypothèse, prédiction chiffrée et signe, ce qui compte comme réfutation, métrique, seuil, plan d'analyse, critères de lecture gelés (toute combinaison d'issues a un verdict ; aucune issue sans lecture), liste d'arrêt. Cohérence des chiffres entre sections (tailles d'échantillon, seuils, graines, comparaisons multiples). Un préenregistrement que deux lecteurs pourraient lire différemment sur un résultat donné est défaillant : cherche ces ambiguïtés.
5. **R3, R4, R5, R9**, et l'interdit « moyenne ou médiane sur les jetons dans une sonde de production » (bras de diagnostic permis : N-026). Méthode statistique : estimateurs, intervalles, puissance, multiplicité, appariement.
6. **Fidélité de la note des différences** : chaque changement réel entre brouillon 5 et brouillon 6 de relance y figure (fais un `diff` et compare) ; aucun changement n'est sans décision ou pièce qui le commande ; aucun changement silencieux.
7. **La liste des décisions du directeur** : complète ? (tout « À REMPLIR » et tout marqueur `<<…>>` de décision y renvoie ; aucune décision que le texte a tranchée seul alors qu'elle revenait au directeur) ; options honnêtes ; recommandation défendable ; « aucun défaut » pour les nœuds.
8. Ce que le rédacteur n'a pas vu : contradiction entre décisions, pièce en vigueur oubliée.

## 4. Interdits (du mandat)
- **Aucun résultat d'expérience lu** : rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`.
- Rien dont le nom contient « consigne-privee » ou « conception-ii-b » ; ni la branche `lot/compte-4-v1` ; ni la ligne R-2059 des registres (filtre-la : `grep … | grep -v 'R-2059'`).
- Aucune dépense, aucune machine, aucun appel à une interface de modèle extérieure, aucun accès au réseau hors `git fetch` du dépôt ; jamais la suite d'essais complète.
- Tu n'écris que dans `/tmp/claude-0/-home-user-controle-ia-travail/ea38fd7e-2b5a-5aae-9611-af6160a314d6/scratchpad/bloc-notes/contre-lecteur/`. Tu ne corriges pas le texte toi-même. Aucune modification du dépôt. N'engage aucun autre agent.
- **Au premier refus de permission : arrête-toi et rends le texte exact du refus.**

## 5. Ce que tu rends
`rapport-contre-lecture-brouillon6-relance-v1.md` dans ton dossier : empreinte du brouillon relu ; pièces lues avec empreintes ; remarques numérotées `CL-01`, `CL-02`…, chacune avec gravité (**bloquante** : interdit le scellement ; **majeure** ; **mineure**), lieu (ligne ou section), citation exacte, pièce qui fonde la remarque, correction demandée ; contrôles faits par programme et leur sortie ; ce que tu n'as pas pu vérifier ; avis d'ensemble : scellable en l'état, scellable après corrections, ou non scellable.

Message final court : chemin et empreinte du rapport, nombre de remarques par gravité, avis d'ensemble, liste d'une ligne par remarque bloquante ou majeure.

Tu seras rappelé ensuite, toi et non un autre, pour vérifier les corrections.
