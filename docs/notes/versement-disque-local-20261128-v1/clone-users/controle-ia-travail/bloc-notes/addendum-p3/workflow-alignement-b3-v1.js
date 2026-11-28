export const meta = {
  name: 'addendum-p3-alignement-b3',
  description: "Addendum de P3 : alignement du module final sur le brouillon 3, puis contre-lecture du code face au texte par deux sous-agents neufs",
  phases: [
    { title: 'Alignement', detail: 'module et tests alignés sur le brouillon 3' },
    { title: 'Contre-lecture', detail: 'code face au texte, deux angles, sous-agents neufs' },
  ],
}

const A = args
const COMMUN = `
Contexte :
- Dépôt de travail en LECTURE SEULE : ${A.repo} (aucune écriture, aucun commit, aucune poussée, aucun git fetch ;
  aucune commande Vast.ai ; aucun service payant).
- Python : ${A.py} ; tests : PYTHONPATH=${A.repo}/src:${A.repo}/tests ${A.py} -m pytest -q <fichier>.
- Préenregistrement qui fait foi : brouillon 3 de l'addendum, ${A.brouillon3} (lis-le en entier, à la lettre).
- Code gelé de P3 : ${A.repo}/src/controle_ia/ (premier_test_ia/lecture.py, statistiques.py, conditions.py, notation.py,
  run.py ; environnements/propositions.py ; manifeste.py ; prereg.py ; harnais/validation_reelle.py ; sondes/evaluation.py ;
  sondes/temoins.py), à importer, jamais à modifier.
Règles : jamais de moyenne ni de médiane sur les jetons d'une action dans un score ; aucun repli silencieux ; R5 (chaque garde
testée sur un cas sain et sur un artefact) ; français, phrases courtes ; style du code voisin.
`
const SCHEMA_CODE = {
  type: 'object',
  properties: {
    module: { type: 'string' }, tests: { type: 'string' }, nombre_tests: { type: 'number' },
    sortie_pytest: { type: 'string' }, duree_estimee: { type: 'string' },
    regles_non_appliquees: { type: 'array', items: { type: 'string' } },
  },
  required: ['module', 'tests', 'nombre_tests', 'sortie_pytest', 'regles_non_appliquees'],
}
const SCHEMA_RAPPORT = {
  type: 'object',
  properties: {
    chemin_rapport: { type: 'string' }, verdict: { type: 'string' },
    constats: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, gravite: { type: 'string' }, ou: { type: 'string' }, probleme: { type: 'string' }, correction: { type: 'string' } }, required: ['id', 'gravite', 'ou', 'probleme', 'correction'] } },
  },
  required: ['chemin_rapport', 'verdict', 'constats'],
}

phase('Alignement')
const aligne = await agent(`${COMMUN}
Point de départ : le module final de l'orchestration précédente, ${A.final}/complements_p3_v1.py, ses tests
${A.final}/test_complements_p3_v1.py, ses notes ${A.final}/NOTES-SYNTHESE.md, et les rapports de revue adversariale
${A.rapports}/revue-adversariale-*.md. Le texte a changé depuis : le brouillon 3 remplace le brouillon 1 (traitement des
changements : ${A.traitement}).
Tâche : écris dans ${A.sortie}/ (dossier neuf, le seul où tu écris) complements_p3_v1.py et test_complements_p3_v1.py,
alignés **à la lettre** sur le brouillon 3 : chaque analyse, chaque cible, chaque réserve de la table « Seuil », la table de
\`conclusions_etablies\` (plan, point 5), les clés interdites, \`controle_contraire\` (« sans objet »), la forme de la sortie,
\`audit_symetrie_addendum\`, les gardes 1 à 11 de la liste d'arrêt dans l'ordre écrit (gardes avant le manifeste), la lecture
des empreintes du module et des tests dans le préenregistrement (lignes « Module de l'addendum (sha256) : \`…\` » et « Tests
du module (sha256) : \`…\` »), et chaque test de la liste fermée. Corrige aussi les constats des revues adversariales qui
restent vrais. Les tirages se réduisent dans les tests par un paramètre propre au module, jamais en modifiant le module gelé.
Tous les tests doivent passer (aucun retiré ni affaibli). Écris ${A.sortie}/NOTES-ALIGNEMENT.md : pour chaque section du
brouillon 3, la fonction qui l'applique ; la liste des règles que tu n'as pas pu appliquer telles quelles (doit être vide,
sinon dis pourquoi) ; le nombre de tests ; la durée mesurée sur données synthétiques de taille réelle (60 tâches, 4
conditions, 10 pas, 430 sondes, 2 000 tirages ; extrapole si besoin). Rends ces éléments.`,
  { label: 'alignement', phase: 'Alignement', schema: SCHEMA_CODE })

phase('Contre-lecture')
const ANGLES = [
  "texte face au code : pour chaque phrase normative du brouillon 3 (analyses, niveaux, cibles, réserves, table des conclusions établies, verrou, gardes, sortie), trouve la ligne de code qui l'applique ; liste chaque écart, chaque règle absente, chaque règle ajoutée",
  "preuves et pannes : les tests prouvent-ils chaque garde (cas sain et artefact) ? Écris des mutants du module (dans ton dossier, jamais dans le sien) qui violent une règle (réserve mal câblée, verrou ouvert, moyenne sur les jetons, garde retirée, niveau changé) et dis lesquels les tests ne tuent pas ; vérifie le déterminisme et l'absence de texte d'action dans la sortie",
]
const revues = await parallel(ANGLES.map((an, i) => () => agent(`${COMMUN}
Tu es contre-lecteur neuf (R2) : tu n'as écrit ni le brouillon 3 ni le module. Module : ${aligne ? aligne.module : A.sortie + '/complements_p3_v1.py'} ;
tests : ${aligne ? aligne.tests : A.sortie + '/test_complements_p3_v1.py'} ; notes : ${A.sortie}/NOTES-ALIGNEMENT.md.
Angle : ${an}.
Tes essais vont dans ${A.rapports}/code-b3-${i + 1}/ et nulle part ailleurs. Rapport :
${A.rapports}/contre-lecture-code-b3-${i + 1}.md, verdict en tête (« scellable », « scellable après corrections »,
« non scellable »), puis les constats (id CB${i + 1}-NN, gravité, où, problème, correction), le plus grave d'abord, chacun
reproduit. Rends les constats.`, { label: `R2-code:${i + 1}`, phase: 'Contre-lecture', schema: SCHEMA_RAPPORT })))

return { aligne, revues: revues.filter(Boolean) }
