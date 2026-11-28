export const meta = {
  name: 'plan-b-code-v1',
  description: "Plan B des juges (N-022, voie a) : code neuf et tests dans un clone à part, puis relecture R2 sous trois angles",
  phases: [
    { title: 'Lecture RS1', detail: "invite RS1 et lecteur des réponses, avec leurs tests" },
    { title: 'Juges et lecteur', detail: "messages et adaptateur, lanceur de l'étape, lecteur mince" },
    { title: 'Intégration', detail: 'suite ciblée, nombre de tests, notes' },
    { title: 'Relecture R2', detail: 'trois sous-agents neufs, trois angles' },
  ],
}

const A = args
const COMMUN = `
Contexte (lis-le en entier avant d'écrire) :
- Clone de travail, le SEUL endroit où tu écris : ${A.clone} (branche locale travail/plan-b-v1). Ne pousse rien, ne fais
  aucun commit (la session committera elle-même), ne touche jamais ${A.repo} (dépôt principal, lecture seule), n'appelle
  aucun service payant, aucune instance, aucun outil Vast.ai, aucun téléchargement de modèle réel : modèles et tokeniseurs
  jouets seulement (voir les tests existants de ${A.clone}/tests qui en utilisent).
- Python : ${A.py} ; tests : cd ${A.clone} && PYTHONPATH=src ${A.py} -m pytest -q <fichiers ciblés>. La suite complète dure
  environ 30 minutes : ne la lance pas, sauf consigne contraire.
- Préenregistrement du plan B, brouillon 3 (fait foi, à suivre à la lettre) : ${A.brouillon}. Sections clés : « Métrique »,
  « Plan d'analyse », « Critères de lecture gelés », « Liste d'arrêt », « Code à écrire et tests (R5) », annexes A et B.
- Notes de conception : ${A.notes}. Décision de la session R-225 (à appliquer) : la règle neuve de lecture rend aussi
  invalide une valeur qui continue, après le premier nombre, par « , », « ; », « and » ou une parenthèse ouvrante suivis d'un
  chiffre (« 3, 4 », « 3 and 4 », « 3 (4) », « 3; 4 », « 3/5, 4/5 ») : la réponse devient incomplète, jamais lue sur un
  choix ; avec ses tests ; la phrase « ne choisit jamais entre deux nombres » n'est gardée que si elle devient vraie.
- Modules gelés à importer tels quels, JAMAIS modifiés : rubrique.py, juges.py, pilote_a.py, lancer_pilote_a.py,
  lire_pilote.py, analyse_pilote.py, noter_pilote_a.py, lire_notations_pilote.py, invites.py, harnais/episode.py,
  harnais/activations.py, harnais/modeles.py, harnais/validation_reelle.py (sous ${A.clone}/src/controle_ia/). Commit de
  référence de leurs empreintes : c63d4f1c073f3b6146729dae0086cd7205cdfa57.
Règles du programme : aucun repli silencieux ; chaque garde testée sur un cas sain et sur un artefact (R5) ; graines par
SeedSequence (R9) ; jamais de moyenne ni de médiane sur les jetons d'une action dans un score ; français, phrases courtes
dans les commentaires et les messages ; style et densité de commentaires du code voisin.
`
const SCHEMA_TRAVAIL = {
  type: 'object',
  properties: {
    fichiers: { type: 'array', items: { type: 'string' } },
    tests: { type: 'array', items: { type: 'string' } },
    sortie_pytest: { type: 'string' },
    ecarts_au_texte: { type: 'array', items: { type: 'string' } },
    questions: { type: 'array', items: { type: 'string' } },
  },
  required: ['fichiers', 'tests', 'sortie_pytest', 'ecarts_au_texte', 'questions'],
}
const SCHEMA_RAPPORT = {
  type: 'object',
  properties: {
    chemin_rapport: { type: 'string' },
    verdict: { type: 'string' },
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
  required: ['chemin_rapport', 'verdict', 'constats'],
}

phase('Lecture RS1')
const rs1 = await agent(`${COMMUN}
Ta part : les points 1 et 2 de « Code à écrire et tests » :
1. ${A.clone}/docs/sources/invites-plan-b-v1/ : invites/RS1.txt (texte de l'annexe A, octet pour octet), index.json
   (identifiant RS1, fichier, nombre de caractères, sha256), LISEZMOI.md, sceaux (PYTHONPATH=src ${A.py} -m
   controle_ia.scellement sceller <fichiers>) ; chargement par la fonction gelée charger_invite("RS1", racine=…).
2. ${A.clone}/src/controle_ia/environnements/rubrique_simplifiee.py : critères RS1 ; lecture d'une réponse (règle de la
   section « Métrique », étapes 1 à 10, plus la règle de R-225) ; score par la classe gelée NotesRubrique.
Tests : ${A.clone}/tests/test_plan_b_rubrique_simplifiee.py, avec TOUS les cas de lecture RS1 listés dans « Tests » (y
compris intervalles, contradictions, demi-points, prose avant le bloc, réponse tronquée, cas sains du contrôle) et les cas de
R-225 ; invite RS1 : empreinte ou index altérés, arrêt. Tous tes tests doivent passer. Rends fichiers, tests, sortie de
pytest, écarts au texte (motivés) et questions.`, { label: 'rs1', phase: 'Lecture RS1', schema: SCHEMA_TRAVAIL })

phase('Juges et lecteur')
const [juges, lecteur] = await parallel([
  () => agent(`${COMMUN}
Le point 2 est fait (fichiers : ${rs1 ? rs1.fichiers.join(', ') : 'voir le clone'}) ; ne le modifie que pour une erreur
prouvée par un test, et dis-le. Ta part : les points 3 et 4 de « Code à écrire et tests » :
3. ${A.clone}/src/controle_ia/environnements/juges_simplifies.py : messages RS1 (système = H.3 ; utilisateur = RS1, puis le
   corps assemblé exactement comme b0) ; adaptateur d'environnement de notation pour jouer_episodes (consigne = message
   système, observation = message utilisateur, N = 1, T = 1), pour RS1 et pour H.4.
4. ${A.clone}/src/controle_ia/environnements/requalifier_juges.py : lanceur de l'étape (gardes, manifeste, phases et
   échéances, garde en ligne, rejeu, ancrage, témoin, écriture « tout ou rien », lignes de progression sans compte, arrêt
   consigné, « témoin impossible ») ; generer_lot seulement à travers jouer_episodes ; generate de la bibliothèque
   seulement dans le témoin.
Tests : ${A.clone}/tests/test_plan_b_juges_simplifies.py et ${A.clone}/tests/test_plan_b_requalifier.py : assemblage,
format en deux temps, équivalence de chemin (modèle jouet, lot pour lot, champs de noter_ensembles), garde en ligne et règle
k(n − 1), rejeu (graines, reproduction, simple précision, TF32, palier, D1, classement des dépassements, ancrage couche par
couche, couverture), témoin (configuration par défaut à 0,6 et noyau remplacée, témoin impossible, pannes propagées, queues
binomiales), tirage sur le processeur, mémoire, échéances et signal TERM — chacun avec cas sain et artefact, tels que listés.
Signale comme tels les tests sensibles au matériel. Rends fichiers, tests, sortie de pytest, écarts au texte et questions.`,
    { label: 'juges+lanceur', phase: 'Juges et lecteur', schema: SCHEMA_TRAVAIL }),
  () => agent(`${COMMUN}
Le point 2 est fait (fichiers : ${rs1 ? rs1.fichiers.join(', ') : 'voir le clone'}). Un autre agent écrit en même temps
juges_simplifies.py et requalifier_juges.py : ne les touche pas ; si tu as besoin de leur format de sortie, prends-le dans
le texte (« Plan d'analyse », fichiers écrits par l'étape) et écris des fichiers synthétiques de ce format.
Ta part : le point 5 de « Code à écrire et tests » : ${A.clone}/src/controle_ia/environnements/lire_requalification.py,
lecteur mince (« Plan d'analyse », « Lecture », « Critères de lecture gelés », tables A à E), et
${A.clone}/tests/test_plan_b_lecteur.py : équivalence avec les fonctions gelées sur un run jouet ; chaque ligne des tables
A, B, C, D et E sur fichiers synthétiques ; chaque recouvrement de lignes listé dans « Tests » ; statut de PB1 à PB10. Rends
fichiers, tests, sortie de pytest, écarts au texte et questions.`,
    { label: 'lecteur', phase: 'Juges et lecteur', schema: SCHEMA_TRAVAIL }),
])

phase('Intégration')
const integ = await agent(`${COMMUN}
Intègre le travail des trois agents précédents dans ${A.clone} : fichiers ${[rs1, juges, lecteur].filter(Boolean).flatMap(x => x.fichiers).join(', ')}.
Vérifie les imports croisés (le lanceur et le lecteur utilisent les mêmes noms de fichiers et de clés), corrige les
incohérences sans affaiblir aucun test, puis lance : (1) tous les tests du plan B (tests/test_plan_b_*.py) ; (2) les tests
des modules gelés qu'ils touchent (tests/test_rubrique*.py, tests/test_juges*.py, tests/test_invites*.py, s'ils existent) ;
(3) un contrôle que AUCUN module gelé n'a changé : cd ${A.clone} && git diff --stat HEAD -- src/controle_ia/environnements/rubrique.py
src/controle_ia/environnements/juges.py src/controle_ia/harnais (doit être vide), et git status pour la liste des fichiers
neufs. Écris ${A.clone}/../NOTES-INTEGRATION-plan-b-v1.md : fichiers neufs, nombre de tests ajoutés, sorties de pytest,
écarts au texte et questions de chaque agent, et la liste des points du texte que le code ne couvre pas encore (dont la
chaîne de lancement, point 6, hors de cette étape). Rends le résumé.`, { label: 'integration', phase: 'Intégration', schema: SCHEMA_TRAVAIL })

phase('Relecture R2')
const ANGLES = [
  'lanceur et lecteur face au texte : chaque garde, chaque phase, chaque échéance, chaque table de lecture, la liste d\'arrêt',
  'lecture RS1 et invite face au texte : étapes 1 à 10 de la Métrique, règle R-225, annexe A octet pour octet, index et sceaux, tests de chaque cas listé',
  'tests et gardes (R5) : chaque garde a-t-elle un cas sain et un artefact ? un test peut-il passer avec un code faux ? écris et lance des mutants (dans un dossier à part, jamais dans le clone) pour le prouver',
]
const revues = await parallel(ANGLES.map((an, i) => () => agent(`${COMMUN}
Tu es contre-lecteur neuf (R2) du code neuf du plan B, que tu n'as pas écrit. Angle : ${an}.
Fichiers neufs : ${integ ? integ.fichiers.join(', ') : 'git -C ' + A.clone + ' status'} ; notes d'intégration :
${A.clone}/../NOTES-INTEGRATION-plan-b-v1.md. Lecture seule sur le clone : tes essais vont dans
${A.clone}/../relecture-R2-${i + 1}/ et nulle part ailleurs. Écris ton rapport dans
${A.clone}/../relecture-R2-${i + 1}/rapport-R2-plan-b-code-${i + 1}.md : verdict en tête (« prêt », « prêt après
corrections », « non prêt »), puis un tableau des constats (id, gravité, où, problème, correction), le plus grave d'abord.
Rends les constats.`, { label: `R2:${i + 1}`, phase: 'Relecture R2', schema: SCHEMA_RAPPORT })))

return { rs1, juges, lecteur, integ, revues: revues.filter(Boolean) }
