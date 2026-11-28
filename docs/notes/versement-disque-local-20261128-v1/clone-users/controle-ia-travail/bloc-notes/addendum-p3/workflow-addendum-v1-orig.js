export const meta = {
  name: 'addendum-p3-v1',
  description: "Addendum de lecture complémentaire de P3 : contre-lecture du brouillon, deux implémentations indépendantes, jury, synthèse, revue adversariale",
  phases: [
    { title: 'Contre-lecture et implémentations', detail: "R2 du brouillon en parallèle de deux implémentations indépendantes" },
    { title: 'Jury', detail: 'trois juges, trois angles, sur les candidats' },
    { title: 'Synthèse', detail: 'module final à partir du gagnant et des greffes' },
    { title: 'Revue adversariale', detail: 'trois angles sur le module final' },
  ],
}

const A = args
const COMMUN = `
Contexte (lis-le, ne le résume pas) :
- Dépôt de travail en LECTURE SEULE : ${A.repo}. Ne modifie, ne crée, ne supprime AUCUN fichier dans ce dépôt, ne fais aucun
  commit ni aucune poussée, n'appelle aucun service payant ni aucune instance de calcul. Tu écris seulement dans le dossier
  qu'on te donne.
- Python à utiliser : ${A.py} (numpy, pytest). Lance les tests avec PYTHONPATH=${A.repo}/src depuis ton dossier de travail.
- Code gelé de P3 (à importer, jamais à modifier ni à recopier en le changeant) : ${A.repo}/src/controle_ia/premier_test_ia/
  (lecture.py, statistiques.py, conditions.py, notation.py, run.py, empans.py), ${A.repo}/src/controle_ia/sondes/evaluation.py
  (aire_sous_courbe, intervalle_blocs), ${A.repo}/src/controle_ia/manifeste.py (creer_manifeste, ecrire_resultat,
  verifier_resultat, graines, generateur), ${A.repo}/src/controle_ia/harnais/run_harnais_factice.py (graine_entiere),
  ${A.repo}/src/controle_ia/environnements/propositions.py (lire_action, heures_declarees, _NOMBRE).
- Aides de données synthétiques existantes : ${A.repo}/tests/test_premier_test_ia_lecture.py (_source, _graines, P).
- Brouillon du préenregistrement de l'addendum (fait foi pour le fond) : ${A.brouillon}.
- Spécification d'origine de Gemini (base, moins précise que le brouillon) : ${A.spec}.
- Blocs de code de Gemini (tour 1, propositions écrites DANS le code gelé, à n'utiliser que comme idées) : ${A.blocs}.
Règles du programme qui s'appliquent ici : jamais de moyenne ni de médiane sur les jetons d'une action dans un score (seuls le
maximum et la somme pondérée par le softmax des logits, via notation.agreger_par_jeton) ; aucun repli silencieux (tout cas
hors de forme est écrit avec son motif) ; graines par numpy.random.SeedSequence dérivées de clés (manifeste.graines) ; R5 :
chaque garde est testée sur un cas sain et sur un artefact ; français, phrases courtes, quasi aucun acronyme dans les textes.
`

const SCHEMA_RAPPORT = {
  type: 'object',
  properties: {
    chemin_rapport: { type: 'string' },
    resume: { type: 'string' },
    constats: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          gravite: { type: 'string', enum: ['bloquant', 'majeur', 'mineur', 'information'] },
          ou: { type: 'string' },
          probleme: { type: 'string' },
          correction: { type: 'string' },
        },
        required: ['id', 'gravite', 'ou', 'probleme', 'correction'],
      },
    },
  },
  required: ['chemin_rapport', 'resume', 'constats'],
}

const SCHEMA_CANDIDAT = {
  type: 'object',
  properties: {
    module: { type: 'string' },
    tests: { type: 'string' },
    sortie_pytest: { type: 'string' },
    duree_estimee_reelle: { type: 'string' },
    ecarts_au_brouillon: { type: 'array', items: { type: 'string' } },
    incertitudes: { type: 'array', items: { type: 'string' } },
  },
  required: ['module', 'tests', 'sortie_pytest', 'ecarts_au_brouillon', 'incertitudes'],
}

const SCHEMA_JUGE = {
  type: 'object',
  properties: {
    notes: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          candidat: { type: 'string' },
          note_sur_10: { type: 'number' },
          forces: { type: 'array', items: { type: 'string' } },
          defauts: { type: 'array', items: { type: 'string' } },
        },
        required: ['candidat', 'note_sur_10', 'forces', 'defauts'],
      },
    },
    gagnant: { type: 'string' },
    greffes: { type: 'array', items: { type: 'string' } },
  },
  required: ['notes', 'gagnant', 'greffes'],
}

phase('Contre-lecture et implémentations')

const consigneR2 = `${COMMUN}
Tu es le contre-lecteur neuf (règle R2) du brouillon du préenregistrement de l'addendum de lecture complémentaire de P3. Tu
n'as écrit ni ce brouillon ni aucun code. Lis le brouillon en entier, puis vérifie-le contre le code gelé (chaque clé, chaque
fonction, chaque règle doit exister telle qu'elle est écrite ; cite fichier et ligne) et contre la spécification de Gemini.
Cherche en priorité : (1) toute voie par laquelle l'addendum pourrait promouvoir une conclusion ou changer la lecture
décisive (verrou unidirectionnel) ; (2) toute moyenne ou médiane sur les jetons d'une action dans un score ; (3) les règles de
réserve ambiguës, non mécaniques, ou qui lisent une clé que lecture.py n'écrit pas ; (4) les erreurs statistiques (plancher
conjoint, fenêtres appariées en longueur, tranches internes, aire intra-tâche, dégénérescences, niveaux) ; (5) les cas
dégénérés et la liste d'arrêt ; (6) la faisabilité du calcul (2 400 actions, 430 sondes, 2 000 tirages) ; (7) la conformité
au gabarit ${A.repo}/prereg/gabarit-preregistrement-v1.md et au validateur ${A.repo}/src/controle_ia/prereg.py.
Écris ton rapport en français dans ${A.rapports}/contre-lecture-R2-brouillon1-addendum-P3-v1.md : verdict en tête (scellable,
scellable après corrections, non scellable), puis un tableau des constats (id RA-01…, gravité, où, problème, correction).
Rends aussi les constats dans la sortie structurée.`

const consigneImpl = (lettre) => `${COMMUN}
Tu écris, seul et sans voir le travail d'un autre, une implémentation complète de l'addendum décrit par le brouillon.
Dossier de travail (le seul où tu écris) : ${A.out}/candidat-${lettre}/.
Fichiers à produire :
- ${A.out}/candidat-${lettre}/complements_p3_v1.py : module autonome, à verser plus tard sous
  docs/procedures/P3-addendum-v1/ (hors de l'arbre gelé : src/ et tests/ ne doivent pas être touchés). Interface en ligne de
  commande du plan d'analyse du brouillon (--run-source, --lecture, --run-addendum, --prereg, --entropie) et une fonction
  pure \`analyser_addendum(source: dict, lecture: dict, graines: dict) -> dict\` testable sans fichier. Chargement réel par
  lecture.charger_source et manifeste.verifier_resultat ; manifeste propre par manifeste.creer_manifeste (non décisif,
  préenregistrement de l'addendum cité) ; clés de graines \`addendum/...\` ; sortie par manifeste.ecrire_resultat sous le nom
  \`lecture-addendum-p3\`.
- Les analyses A1 à A9, les règles de réserve, le verrou unidirectionnel et la synthèse mécanique du brouillon, à la lettre.
  Aire vectorisée par rangs pour le plancher (une passe de tri par tirage pour la sonde et ses sondes de plancher), égale à
  sondes.evaluation.aire_sous_courbe à 1e-12 près. Le calcul complet doit tenir en moins de 30 minutes sur 4 cœurs pour
  2 400 actions notées, 430 sondes et 2 000 tirages : mesure-le sur données synthétiques de cette taille (tirages réduits
  puis extrapolés si besoin) et donne l'estimation.
- ${A.out}/candidat-${lettre}/test_complements_p3_v1.py : pour chaque analyse, un cas sain (aucune réserve), un artefact qui
  déclenche la réserve, un cas dégénéré (non calculable ou échec écrit, sans exception non gérée), un test du verrou (une
  conclusion non établie par la lecture ne le devient jamais) ; déterminisme (deux exécutions, même sortie octet pour
  octet) ; refus d'une entropie autre ; issue primaire inchangée ; aucune moyenne sur les jetons (action à score constant sauf
  un jeton : le score d'empan est le maximum). Données synthétiques : réutilise _source et _graines de
  tests/test_premier_test_ia_lecture.py (importe-les en ajoutant ${A.repo}/tests au chemin) et lecture.lire pour produire une
  lecture décisive synthétique ; ajoute des textes d'action synthétiques pour A5 et A6.
Lance tes tests (${A.py} -m pytest -q ${A.out}/candidat-${lettre}/test_complements_p3_v1.py avec PYTHONPATH=${A.repo}/src) jusqu'à
ce qu'ils passent tous ; aucun test ne doit être retiré ou affaibli pour passer. Rends les chemins, la dernière sortie de
pytest, la durée estimée sur données réelles, tes écarts au brouillon (chacun motivé) et tes incertitudes.`

const [r2, candA, candB] = await parallel([
  () => agent(consigneR2, { label: 'R2:brouillon1', phase: 'Contre-lecture et implémentations', schema: SCHEMA_RAPPORT }),
  () => agent(consigneImpl('a'), { label: 'implementation:a', phase: 'Contre-lecture et implémentations', schema: SCHEMA_CANDIDAT }),
  () => agent(consigneImpl('b'), { label: 'implementation:b', phase: 'Contre-lecture et implémentations', schema: SCHEMA_CANDIDAT }),
])
log(`R2 : ${r2 ? r2.constats.length + ' constats' : 'absent'} ; candidats : a ${candA ? 'prêt' : 'absent'}, b ${candB ? 'prêt' : 'absent'}`)

phase('Jury')
const candidats = [
  candA && { nom: 'a', module: candA.module, tests: candA.tests },
  candB && { nom: 'b', module: candB.module, tests: candB.tests },
  { nom: 'gemini', module: A.gemini_module, tests: A.gemini_tests },
].filter(Boolean)
const listeCandidats = candidats.map(c => `- candidat « ${c.nom} » : module ${c.module}, tests ${c.tests} (si un fichier est absent, note ce candidat 0 et dis-le)`).join('\n')
const constatsR2 = r2 ? r2.constats.map(c => `${c.id} [${c.gravite}] ${c.ou} : ${c.probleme}`).join('\n') : '(contre-lecture absente)'
const ANGLES = [
  { cle: 'fidelite', texte: "fidélité au brouillon et au verrou unidirectionnel : chaque analyse, chaque règle de réserve, chaque clé lue, la synthèse mécanique, la liste d'arrêt ; aucune voie de promotion ; aucune moyenne sur les jetons" },
  { cle: 'statistique', texte: "justesse statistique : plancher conjoint tirage par tirage, fenêtres appariées en longueur, tranches recalculées dans le tirage, aire intra-tâche, niveaux, dégénérescences, graines et déterminisme ; refais à la main un ou deux calculs sur un petit exemple" },
  { cle: 'robustesse', texte: "robustesse et preuves : lance toi-même les tests de chaque candidat (sans les modifier), cherche les cas que les tests ne couvrent pas, mesure la durée sur données synthétiques de taille réelle, vérifie la gestion des cas dégénérés et l'absence de texte d'action dans la sortie" },
]
const votes = await parallel(ANGLES.map(an => () => agent(`${COMMUN}
Tu es juge (angle : ${an.texte}). Compare les candidats d'implémentation de l'addendum :
${listeCandidats}
Constats de la contre-lecture R2 du brouillon (pour information) :
${constatsR2}
N'écris aucun fichier hors de ${A.rapports}/. Écris ton jugement dans ${A.rapports}/jury-${an.cle}.md, puis rends les notes,
le gagnant et les greffes utiles des autres candidats (fonction précise, ce qu'elle apporte).`,
  { label: `juge:${an.cle}`, phase: 'Jury', schema: SCHEMA_JUGE })))
const jugements = votes.filter(Boolean)
const scores = {}
for (const j of jugements) for (const n of j.notes) scores[n.candidat] = (scores[n.candidat] || 0) + n.note_sur_10
const gagnant = Object.entries(scores).sort((x, y) => y[1] - x[1])[0]?.[0] || 'a'
log(`jury : ${JSON.stringify(scores)} ; gagnant ${gagnant}`)

phase('Synthèse')
const greffes = jugements.flatMap(j => j.greffes).join('\n- ')
const gagnantC = candidats.find(c => c.nom === gagnant) || candidats[0]
const synthese = await agent(`${COMMUN}
Tu écris le module final de l'addendum à partir du candidat gagnant du jury, « ${gagnantC.nom} » (module ${gagnantC.module},
tests ${gagnantC.tests}), en y greffant ce qui suit quand c'est juste :
- ${greffes}
et en corrigeant ce que la contre-lecture R2 du brouillon a relevé et qui touche le code :
${constatsR2}
Dossier de sortie (le seul où tu écris) : ${A.out}/final/ : complements_p3_v1.py, test_complements_p3_v1.py, et
NOTES-SYNTHESE.md (ce qui vient de quel candidat, chaque greffe, chaque correction, ce qui reste ouvert, et toute règle du
brouillon que le code ne peut pas appliquer telle quelle, avec la reformulation proposée pour le texte). Tous les tests
doivent passer ; aucun test retiré ni affaibli. Rends les chemins, la sortie de pytest, la durée estimée et les points
ouverts.`, { label: 'synthese', phase: 'Synthèse', schema: SCHEMA_CANDIDAT })

phase('Revue adversariale')
const LENTILLES = [
  "exactitude : refais à la main, sur un petit exemple construit, le calcul de A1, A2, A3 et A4 et compare au module ; cherche les erreurs d'indice, de condition, d'étiquette, de niveau",
  "verrou et règles : prouve ou réfute qu'aucune sortie ne peut promouvoir une conclusion, changer l'issue primaire, ou omettre une réserve due ; cherche les règles de réserve mal câblées et les clés de lecture-p3.json mal lues",
  "pannes : cas dégénérés, données hors de forme, déterminisme, durée sur données de taille réelle, sortie sans texte d'action, garde d'entropie et de préenregistrement, comportement si la lecture décisive est en échec sur un jeu",
]
const revues = await parallel(LENTILLES.map((l, i) => () => agent(`${COMMUN}
Tu es relecteur adversarial du module final de l'addendum : ${A.out}/final/complements_p3_v1.py (tests
${A.out}/final/test_complements_p3_v1.py, notes ${A.out}/final/NOTES-SYNTHESE.md). Angle : ${l}.
Essaie de le casser : écris tes essais dans ${A.out}/rapports/revue-${i + 1}/ (jamais ailleurs), lance-les, et ne retiens
que les constats que tu as reproduits. Écris ton rapport dans ${A.rapports}/revue-adversariale-${i + 1}.md et rends les
constats.`, { label: `revue:${i + 1}`, phase: 'Revue adversariale', schema: SCHEMA_RAPPORT })))

return { r2, candA, candB, jugements, scores, gagnant, synthese, revues: revues.filter(Boolean) }
