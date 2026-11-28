export const meta = {
  name: 'addendum-p3-verification-finale',
  description: "Addendum de P3 : vérification finale du module corrigé face au texte final, par trois sous-agents neufs (texte face au code ; mutants et pannes ; calculs refaits et verrou par propriétés)",
  phases: [
    { title: 'Vérification', detail: 'trois angles, sous-agents neufs, en parallèle' },
  ],
}

const A = args
const COMMUN = `
Contexte (addendum de lecture complémentaire de P3 ; français, phrases courtes) :
- Dépôt de travail en LECTURE SEULE : ${A.repo} (aucune écriture, aucun commit, aucune poussée, aucun git fetch ; aucune
  commande Vast.ai ; aucun service payant ; ne lis rien sous runs/, diag/, donnees/ ni traces/ : aucun résultat de P3 ne
  doit être lu avant le scellement de l'addendum).
- Python : ${A.py}. Tests du module : cd ${A.repo} && PYTHONPATH=src ${A.py} -B -m pytest -q -p no:cacheprovider
  <copie>/test_complements_p3_v1.py (le module s'importe depuis le dossier de son fichier de tests ; travaille sur une
  COPIE du dossier final, jamais sur l'original, et contrôle à la fin que les empreintes de l'original n'ont pas changé).
- Texte qui fait foi (non scellé, final) : ${A.texte} ; lis-le en entier, à la lettre. Diff avec le brouillon 3 relu par
  les revues de code : ${A.brouillon3}.
- Module final : ${A.final}/complements_p3_v1.py (sha256 ${A.sha_module}) ; tests : ${A.final}/test_complements_p3_v1.py
  (sha256 ${A.sha_tests}, ${A.nombre_tests} tests) ; notes de correction : ${A.final}/NOTES-CORRECTIONS-CB1.md.
- Constats à vérifier : CB1 ${A.cb1} ; CB3 ${A.cb3} ; CB2 (revue inachevée, preuves) ${A.cb2} (liste des 51 mutants dans
  mutants_b3_2.py, essais dans sondes/) ; Gemini GB6 et traitement : ${A.traitement} (dernière section).
- Code gelé de P3 sous ${A.repo}/src/controle_ia/ : importé, jamais modifié.
- 4 processeurs partagés avec un autre chantier : la suite complète prend environ 10 minutes ; parallélise au plus par 2.
Règles gelées : R5 (chaque garde testée sur un cas sain et sur un artefact), aucun repli silencieux, jamais de moyenne ni
de médiane sur les jetons d'une action dans un score, verrou unidirectionnel (aucune promotion, issue jamais changée,
réserve due jamais omise).
Tu es contre-lecteur neuf (R2) : tu n'as écrit ni le texte, ni le module, ni ses tests, ni les corrections.
`
const SCHEMA = {
  type: 'object',
  properties: {
    chemin_rapport: { type: 'string' }, verdict: { type: 'string' },
    constats: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, gravite: { type: 'string' }, ou: { type: 'string' }, probleme: { type: 'string' }, correction: { type: 'string' } }, required: ['id', 'gravite', 'ou', 'probleme', 'correction'] } },
    resume: { type: 'string' },
  },
  required: ['chemin_rapport', 'verdict', 'constats', 'resume'],
}
const ANGLES = [
  { cle: 'texte', id: 'VF1', consigne: `Angle : texte final face au code. (1) Pour chaque constat de CB1, CB3, CB2 (tel que décrit par
les essais et la section « Preuve du verrou » du gabarit) et GB6 accepté, vérifie que la correction est faite et juste.
(2) Pour chaque phrase normative du texte final qui a changé depuis le brouillon 3 (précisions d'application 1 à 18, gardes 12
à 16, critères gelés), trouve la ligne de code qui l'applique ; liste chaque écart, chaque règle absente, chaque règle
ajoutée. (3) Vérifie que le module lit dans le texte les lignes « Module de l'addendum (sha256) : \`…\` » et « Tests du
module (sha256) : \`…\` » et les compare aux fichiers exécutés (essai sur une copie du texte où tu remplis les marqueurs).
(4) Lance la suite complète une fois sur ta copie et rapporte le compte.` },
  { cle: 'mutants', id: 'VF2', consigne: `Angle : mutants et pannes. (1) Rejoue les 51 mutants de CB2 sur une copie du module final :
pour chacun, vérifie que son motif existe une seule fois (sinon adapte-le au code actuel en gardant la règle mutée, et dis-le),
applique-le, et lance d'abord le test que les notes de correction donnent comme tueur ; s'il ne meurt pas, lance la suite
complète avec -x. Un mutant survit si toute la suite passe. (2) Ajoute au moins six mutants à toi, sur les règles neuves
(précisions 16 à 18, gardes 12 à 16, découpage des textes sur le seul saut de ligne, recommandation en deux listes, audit de
symétrie qui ne compte que les contrôles contraires) et traite-les de même. (3) Pannes : déterminisme (deux exécutions sur
le run synthétique des tests, sortie identique octet pour octet), aucun texte d'action dans la sortie, U+2028 dans un texte
d'action (aucun arrêt, alignement gardé). Tes essais vont dans ton dossier seulement.` },
  { cle: 'calculs', id: 'VF3', consigne: `Angle : calculs refaits et verrou par propriétés. (1) Sur un petit run synthétique que tu
construis (avec les aides des tests du module), refais à la main, sans appeler les fonctions du module qui les calculent,
A1 (plancher conjoint), A2 (a) et (b) (fenêtres appariées, δ̄), A3, A4 (a) et (b) (tranches par copie, plancher conjoint
intra-tâche), A6 et A8, avec les mêmes graines (clés écrites au texte, précision 12), et compare au module à 1e-12 près ;
écris chaque écart. (2) Verrou par propriétés : sur au moins 200 lectures décisives synthétiques variées (organisme établi
ou non, jeux au-dessus ou non, contrastes établis ou non, entrées en échec ou non calculables), vérifie que chaque contrôle
lu et chaque réserve visent une conclusion établie par la table du plan (point 5), que l'issue recopiée est la ligne
décisive, qu'aucune clé interdite n'apparaît, que la recommandation suit la table des critères gelés à la lettre (deux
listes, formes du coût de A7), et que l'audit de symétrie suit sa phrase (contrôles contraires seulement). Ne lance pas la
suite complète (un autre angle le fait) ; seulement tes essais.` },
]

phase('Vérification')
const rapports = await parallel(ANGLES.map(an => () => agent(`${COMMUN}
${an.consigne}
Tes fichiers vont dans ${A.sortie}/${an.cle}/ et nulle part ailleurs. Rapport :
${A.sortie}/verification-code-final-addendum-P3-v1-${an.cle}.md, verdict en tête (« scellable », « scellable après
corrections », « non scellable »), puis : ce qui a été lu (avec empreintes), ce qui a été lancé (comptes), les constats (id
${an.id}-NN, gravité, où, problème, correction), le plus grave d'abord, chacun reproduit ; et, pour l'angle mutants, la
table complète des mutants (id, règle, statut, test qui le tue). Rends les constats.`,
  { label: `verif:${an.cle}`, phase: 'Vérification', schema: SCHEMA })))

return rapports.filter(Boolean)
