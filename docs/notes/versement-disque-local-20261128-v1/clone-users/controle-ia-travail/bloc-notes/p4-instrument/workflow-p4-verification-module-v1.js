export const meta = {
  name: 'p4-instrument-verification-module',
  description: "P4-instrument : vérification neuve des corrections des brouillons 2 et 3 et écriture du module et des tests (en parallèle), puis contre-lecture du code sous deux angles",
  phases: [
    { title: 'Vérification et code', detail: 'vérificateur neuf du brouillon 3 ; rédacteur neuf du module, des mesures de conception et des tests' },
    { title: 'Contre-lecture du code', detail: 'texte face au code ; mutants et pannes' },
  ],
}
const A = args
const COMMUN = `
Programme « contrôle boîte blanche des menaces diffuses », dirigé par Lazar. Français, phrases courtes, quasi aucun acronyme.
Dépôt en LECTURE SEULE : ${A.repo} (aucune écriture, aucune commande git qui écrive, aucune commande Vast.ai, aucun service
payant, aucun contact). Ne lis jamais prereg/P3-consignes-v1.md, ni le contenu des textes d'action
(donnees/*/textes-actions-*.jsonl : tu peux en calculer l'empreinte, jamais en afficher ni en lire une ligne), ni aucune clé.
**Aucune grandeur de P4 ni de P3 sur des données réelles** (R1 : le texte n'est pas scellé) : aucune aire, aucun score,
aucune activation réelle ; les tests et essais n'emploient que le modèle jouet du dépôt (\`modele-jouet\`) et des tables
synthétiques. Les mesures de conception (MC-1 à MC-3) sur les vrais textes seront lancées par la session, pas par toi.
Texte qui fait foi : brouillon 3 de P4-instrument, ${A.brouillon3} (sha256 ${A.sha_b3}) ; brouillons 1 et 2
${A.brouillon1}, ${A.brouillon2} ; contre-lecture 1 ${A.rapport1} et son traitement ${A.traitement} ; relecture externe de
Gemini (requête 014) ${A.gemini} et son traitement ${A.traitement_gemini} ; plan de code et de chaîne ${A.plan}. Code gelé de P3 sous
${A.repo}/src/controle_ia/ (importé, jamais modifié). Modèles de forme : docs/procedures/P3-addendum-v1/ et la chaîne
docs/procedures/P3-premier-test-v2/ (à lire pour le style ; n'en importe aucune fonction des addenda).
Python : ${A.py} ; tests : cd ${A.repo} && PYTHONPATH=src ${A.py} -B -m pytest -q -p no:cacheprovider <chemin>.
Règles gelées : R1, R2, R3, R4, R5 (chaque garde testée sur un cas sain et un artefact), R9 (graines par clés,
SeedSequence), R10, R11, R12 ; aucun repli silencieux ; jamais de moyenne ni de médiane sur les jetons d'une action.
`
const SCHEMA_V = { type: 'object', properties: { chemin_rapport: { type: 'string' }, verdict: { type: 'string' }, constats: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, gravite: { type: 'string' }, ou: { type: 'string' }, probleme: { type: 'string' }, correction: { type: 'string' } }, required: ['id', 'gravite', 'ou', 'probleme', 'correction'] } } }, required: ['chemin_rapport', 'verdict', 'constats'] }
const SCHEMA_C = { type: 'object', properties: { fichiers: { type: 'array', items: { type: 'object', properties: { chemin: { type: 'string' }, sha256: { type: 'string' } }, required: ['chemin', 'sha256'] } }, nombre_tests: { type: 'number' }, sortie_pytest: { type: 'string' }, duree_mesuree: { type: 'string' }, ecarts_au_texte: { type: 'array', items: { type: 'string' } }, commande_mesures_conception: { type: 'string' } }, required: ['fichiers', 'nombre_tests', 'sortie_pytest', 'duree_mesuree', 'ecarts_au_texte', 'commande_mesures_conception'] }

phase('Vérification et code')
const [verif, code] = await parallel([
  () => agent(`${COMMUN}
Tu es VÉRIFICATEUR neuf (R2, contre-lecture 2) : tu n'as écrit ni le brouillon 1, ni les brouillons 2 et 3, ni la
contre-lecture 1, ni les traitements, ni P3, ni le brainstorm. Vérifie que chaque constat RP-01 à RP-11 (contre-lecture 1)
et GP4-01 à GP4-07 (Gemini) est traité juste dans le brouillon 3, que les décisions des traitements (dont les douze
questions du plan) y sont écrites, et que rien d'autre n'a changé (différentiels mot à mot 1 → 2 → 3). Valide ou non la
liste neuve de B′ (phrases en « an » : urban, elderly, adult, indoor, outdoor), comme le contre-lecteur 1 a validé celle
de B : aucun lien avec l'honnêteté, la morale, les enjeux, le coût ou l'affect (\`sondes/temoins.py\` l. 38-54). Vérifie les faits neufs : bras B′ (structure de longueur, pas de mot du concept),
lignes L1 à L11 (mécaniques, exhaustives, sans chevauchement ni trou ; « au-dessous » sur un plancher symétrique,
\`sondes/evaluation.py\` l. 79), jeton de fin lu par \`jetons − jetons_notes\` (\`premier_test_ia/run.py\` l. 274-276),
puissance (erreur type 0,0435 / 2,241 ; plancher + 2,80 × erreur type), autorité de dépense (registres/go.md
GO-2026-10-20-06 et 07 ; registres/decisions.md R-269, R-270), épreuve de la tolérance (c), garde du verdict complété.
Cherche les constats nouveaux (R1, R3, pare-feu, T0.7, coût). Fichiers à lire : ceux que la section « Contre-lecture » du
brouillon 3 énumère (contre-lecture 2). Rapport : ${A.dossier}/verification/verification-corrections-brouillons2-3-P4-v1.md
(et .sha256), verdict en tête (« scellable », « scellable après corrections », « non scellable »), constats VP2-NN, le plus
grave d'abord. Rends le verdict et les constats.`,
    { label: 'verificateur', phase: 'Vérification et code', schema: SCHEMA_V }),
  () => agent(`${COMMUN}
Tu es le RÉDACTEUR DU MODULE (neuf). Écris, dans ${A.dossier}/module/ (le seul dossier où tu écris), les six fichiers que
le brouillon 3 nomme (en-tête, « Module de P4 ») : mesures_conception_p4_v1.py, instrument_p4_v1.py, lecture_p4_v1.py,
test_instrument_p4_v1.py, test_lecture_p4_v1.py, test_gardes_p4_v1.py, qui appliquent le brouillon 3 À LA LETTRE :
reconstruction des épisodes honnêtes de P3 (bras I, D, H, B, B′) avec le code gelé (harnais/episode.py, run.py,
conditions.py, environnements/propositions.py), garde d'identité à deux niveaux et épreuve de la tolérance (c), M5
(validations reconstruites avec les graines de P3 relues), notation par les sondes légères, C1, M6a, M6b
(\`difference_aire_separation\`), descriptives, audit R4, critères L1 à L11 et réserves (\`issue_p4\`), résumé d'arrêt avec
motif, gardes du mode décisif (entropie, \`exiger_module_cite\` sur les lignes « Module de P4 : \`chemin\` : \`empreinte\` »,
configuration, run source, verdict complété de P3 à docs/verdicts/verdict-P3-premier-test-i-a-v2.md scellé et annoncé au
registre), contrôle du GO et de la ligne d'accord, clés de graines du Plan 8. mesures_conception_p4_v1.py : MC-1 à MC-3
sur processeur avec le vrai tokeniseur (fichier ${A.tokeniseur}, sha256 commençant par 79e3e522), sortie : longueurs,
empreintes et comptes seulement, jamais un texte ; teste-le sur des textes synthétiques. Tests : chaque garde sur un cas
sain et un artefact (liste de la section « Garde d'identité », « Tests (R5) »), chaque ligne L1 à L11 et chaque réserve
atteinte par un cas synthétique, mode jouet de bout en bout. Le nombre de tests écrit en tête de chaque fichier de tests.
Mesure la durée du mode jouet. Lance toute la suite de tes tests ; elle doit passer. Écris ${A.dossier}/module/NOTES-MODULE.md :
pour chaque section du texte, la fonction qui l'applique ; les écarts au texte (liste qui doit être vide, sinon dis
pourquoi) ; la durée mesurée ; la commande exacte que la session lancera pour MC-1 à MC-3. Aucun __pycache__ laissé.
Rends les éléments demandés.`,
    { label: 'redacteur-module', phase: 'Vérification et code', schema: SCHEMA_C }),
])

phase('Contre-lecture du code')
const ANGLES = [
  { cle: 'texte', texte: "texte face au code : pour chaque phrase normative du brouillon 3 (données lues, bras, phrases B et B′, jeton de fin, empan, score par le maximum, plancher, M5, C1, M6a, M6b, descriptives, garde d'identité et épreuve (c), alignement, lignes L1 à L11, réserves, audit R4, gardes du mode décisif, GO et accord, graines, liste d'arrêt), la ligne qui l'applique ; chaque écart, règle absente ou ajoutée ; refais à la main, sur un petit jeu synthétique, l'aire, le quantile du plancher, « au-dessous », Δ et la ligne retenue" },
  { cle: 'mutants', texte: "mutants et pannes : écris au moins 30 mutants du module (ligne L mal ordonnée, plancher haut appliqué à un succès, « au-dessous » oublié, B′ remplacé par H, jeton de fin déduit de la longueur, tolérance (c) changée, épreuve (c) ignorée, garde du verdict complété retirée, GO échu accepté, moyenne sur les jetons, graine changée, résumé d'arrêt absent) dans ton dossier, dis lesquels les tests ne tuent pas ; vérifie le déterminisme (deux exécutions du mode jouet, même sortie) et qu'aucun texte d'action n'est lu ni écrit" },
]
const revues = await parallel(ANGLES.map(an => () => agent(`${COMMUN}
Tu es CONTRE-LECTEUR neuf du code (R2) : tu n'as écrit ni le texte, ni le module, ni ses tests. Module et tests :
${code ? code.fichiers.map(f => f.chemin).join(', ') : A.dossier + '/module/'} ; notes ${A.dossier}/module/NOTES-MODULE.md.
Angle : ${an.texte}. Travaille sur une COPIE du module dans ${A.dossier}/revue-${an.cle}/ (jamais sur l'original).
Rapport ${A.dossier}/revue-${an.cle}/contre-lecture-code-P4-${an.cle}-v1.md (et .sha256), verdict en tête (« scellable »,
« scellable après corrections », « non scellable »), constats CP-${an.cle}-NN, le plus grave d'abord, chacun reproduit.
Rends le verdict et les constats.`,
  { label: `code:${an.cle}`, phase: 'Contre-lecture du code', schema: SCHEMA_V })))

return { verif, code, revues: revues.filter(Boolean) }
