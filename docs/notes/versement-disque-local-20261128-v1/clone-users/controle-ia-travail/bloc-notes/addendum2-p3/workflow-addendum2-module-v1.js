export const meta = {
  name: 'addendum2-p3-module',
  description: "Addendum 2 de P3 : vérification des corrections du brouillon 2 et écriture du module et des tests (en parallèle), puis contre-lecture du code sous deux angles",
  phases: [
    { title: 'Vérification et code', detail: 'vérificateur neuf du brouillon 2 ; rédacteur neuf du module' },
    { title: 'Contre-lecture du code', detail: 'texte face au code ; mutants et pannes' },
  ],
}
const A = args
const COMMUN = `
Programme « contrôle boîte blanche des menaces diffuses », dirigé par Lazar. Français, phrases courtes, quasi aucun acronyme.
Dépôt en LECTURE SEULE : ${A.repo} (aucune écriture, aucune commande git qui écrive, aucune commande Vast.ai, aucun service
payant, aucun contact). Ne lis jamais prereg/P3-consignes-v1.md, ni les textes d'action (donnees/*/textes-actions-*.jsonl),
ni aucune clé. **Aucune grandeur de B1 ni de B2 ne doit être calculée sur les données réelles du run** (R1 : le texte n'est
pas encore scellé) : les tests et les essais n'emploient que des tables synthétiques ; ne charge jamais
donnees/20261019-230011-p3-reel/ ni diag/ de ce run dans un calcul.
Texte qui fait foi : brouillon 2 de l'addendum 2 de P3, ${A.brouillon2} (sha256 ${A.sha_b2}) ; brouillon 1 ${A.brouillon1} ;
contre-lecture 1 ${A.rapport1} ; traitement ${A.traitement}. Code gelé de P3 sous ${A.repo}/src/controle_ia/ (importé, jamais
modifié). Modèle de forme : le premier addendum, prereg/P3-addendum-lecture-complementaire-v1.md et
docs/procedures/P3-addendum-v1/ (à lire pour le style ; n'en importe aucune fonction).
Python : ${A.py} ; tests : cd ${A.repo} && PYTHONPATH=src ${A.py} -B -m pytest -q -p no:cacheprovider <chemin>.
Règles gelées : R1, R2, R4, R5 (chaque garde testée sur un cas sain et un artefact), R9 (graines par clés, SeedSequence),
aucun repli silencieux ; jamais de moyenne ni de médiane sur les jetons d'une action.
`
const SCHEMA_V = { type: 'object', properties: { chemin_rapport: { type: 'string' }, verdict: { type: 'string' }, constats: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, gravite: { type: 'string' }, ou: { type: 'string' }, probleme: { type: 'string' }, correction: { type: 'string' } }, required: ['id', 'gravite', 'ou', 'probleme', 'correction'] } } }, required: ['chemin_rapport', 'verdict', 'constats'] }
const SCHEMA_C = { type: 'object', properties: { module: { type: 'string' }, tests: { type: 'string' }, sha_module: { type: 'string' }, sha_tests: { type: 'string' }, nombre_tests: { type: 'number' }, sortie_pytest: { type: 'string' }, duree_mesuree: { type: 'string' }, ecarts_au_texte: { type: 'array', items: { type: 'string' } } }, required: ['module', 'tests', 'sha_module', 'sha_tests', 'nombre_tests', 'sortie_pytest', 'duree_mesuree', 'ecarts_au_texte'] }

phase('Vérification et code')
const [verif, code] = await parallel([
  () => agent(`${COMMUN}
Tu es VÉRIFICATEUR neuf (R2) : tu n'as écrit ni le brouillon 1, ni le brouillon 2, ni la contre-lecture 1, ni le
traitement. Vérifie que chaque constat RB-01 à RB-13 est corrigé juste dans le brouillon 2, que les décisions du traitement
sur les questions ouvertes y sont écrites, et que rien d'autre n'a changé (différentiel mot à mot 1 → 2) ; cherche les
constats nouveaux (verrou, mécanique des réserves, table des cas de B1, cohérence des comptes de contrôles, R1). Rapport :
${A.dossier}/verification/verification-corrections-brouillon2-addendum2-P3-v1.md, verdict en tête (« scellable »,
« scellable après corrections », « non scellable »), constats VB2-NN. Rends le verdict et les constats.`,
    { label: 'verificateur', phase: 'Vérification et code', schema: SCHEMA_V }),
  () => agent(`${COMMUN}
Tu es le RÉDACTEUR DU MODULE (neuf). Écris, dans ${A.dossier}/module/ (le seul dossier où tu écris),
audit_verdict_p3_v1.py et test_audit_verdict_p3_v1.py, qui appliquent le brouillon 2 À LA LETTRE : entrées et gardes 1 à 15
dans l'ordre du plan (point 3), M1 à M10, B1, B2 (même fonction que B1), écarts de forme, B3, verrou (table du plan,
point 6), réserves de la table « Seuil » et sa table des cas de B1, critères de lecture (recommandation au verdict),
audit de symétrie, forme de la sortie, liste fermée des 47 clés de graines, lecture des empreintes du module et des tests
dans le texte (lignes « Module de l'addendum 2 (sha256) : \`…\` » et « Tests du module (sha256) : \`…\` »). Tests : la liste
fermée de la fin de « Liste d'arrêt », chaque garde sur un cas sain et un artefact, sur des tables synthétiques seulement ;
le nombre de tests écrit en tête du fichier de tests. Mesure la durée sur des données synthétiques de taille réelle (60
tâches, 4 conditions, 10 pas, 600 actions par condition, 430 sondes). Lance toute la suite ; elle doit passer. Écris
${A.dossier}/module/NOTES-MODULE.md : pour chaque section du texte, la fonction qui l'applique ; les écarts au texte (liste
qui doit être vide, sinon dis pourquoi) ; la durée mesurée. Aucun __pycache__ laissé. Rends les éléments demandés.`,
    { label: 'redacteur-module', phase: 'Vérification et code', schema: SCHEMA_C }),
])

phase('Contre-lecture du code')
const ANGLES = [
  { cle: 'texte', texte: "texte face au code : pour chaque phrase normative du brouillon 2 (entrées, gardes, M1 à M10, réserves et table des cas, verrou, critères, audit de symétrie, sortie, clés de graines), la ligne qui l'applique ; chaque écart, règle absente ou ajoutée ; refais à la main, sur un petit jeu synthétique, E_sf, D, M et A_80" },
  { cle: 'mutants', texte: "mutants et pannes : écris au moins 25 mutants du module (réserve mal câblée, cible fausse, cas de B1 inversé, mention sans cible P3-P1, verrou ouvert, garde retirée, seuil ou niveau changé, NaN remplacé par l'infini, clés de graines changées) dans ton dossier, dis lesquels les tests ne tuent pas ; vérifie le déterminisme (deux exécutions, même sortie) et qu'aucun texte d'action, aucun score par jeton n'est lu" },
]
const revues = await parallel(ANGLES.map(an => () => agent(`${COMMUN}
Tu es CONTRE-LECTEUR neuf du code (R2) : tu n'as écrit ni le texte, ni le module, ni ses tests. Module :
${code ? code.module : A.dossier + '/module/audit_verdict_p3_v1.py'} ; tests : ${code ? code.tests : A.dossier + '/module/test_audit_verdict_p3_v1.py'} ;
notes ${A.dossier}/module/NOTES-MODULE.md. Angle : ${an.texte}. Travaille sur une COPIE du module dans
${A.dossier}/revue-${an.cle}/ (jamais sur l'original). Rapport ${A.dossier}/revue-${an.cle}/contre-lecture-code-addendum2-${an.cle}-v1.md,
verdict en tête (« scellable », « scellable après corrections », « non scellable »), constats CC-${an.cle}-NN, le plus grave
d'abord, chacun reproduit. Rends le verdict et les constats.`,
  { label: `code:${an.cle}`, phase: 'Contre-lecture du code', schema: SCHEMA_V })))

return { verif, code, revues: revues.filter(Boolean) }
