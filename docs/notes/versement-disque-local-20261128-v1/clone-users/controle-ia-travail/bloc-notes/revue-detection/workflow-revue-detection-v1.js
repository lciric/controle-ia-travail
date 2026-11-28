export const meta = {
  name: 'revue-detection-p3-v1',
  description: "Comment détecter l'organisme de P3 : revue de la littérature (PDF vérifiés, R7) par familles, synthèse avec Gemini et le brainstorm, vérification des chiffres",
  phases: [
    { title: 'Extraction', detail: 'cinq lecteurs neufs, une famille de travaux chacun' },
    { title: 'Synthèse', detail: 'comment détecter : différences de montage, expériences classées' },
    { title: 'Vérification', detail: 'chaque chiffre contre son PDF, page citée' },
  ],
}

const A = args
const COMMUN = `
Programme « contrôle boîte blanche des menaces diffuses », dirigé par Lazar. Français, phrases courtes, quasi aucun acronyme.
Dépôt en LECTURE SEULE : ${A.repo} (aucune écriture, aucune commande git qui écrive, aucune commande Vast.ai, aucun service
payant, aucun contact). Tu écris seulement dans ${A.dossier}/ (ton sous-dossier). Ne lis jamais prereg/P3-consignes-v1.md, ni
les textes d'action (donnees/*/textes-actions-*.jsonl), ni aucune clé.
Question de Lazar : P3 n'a pas détecté l'organisme ; comment faire pour détecter ? Regarder comment Anthropic et les autres
ont fait. Contexte de P3 : prereg/P3-premier-test-i-a-v1.md ; verdict docs/verdicts/verdict-P3-premier-test-i-a-v1.md
(organisme Llama-3.1-8B-Instruct à consigne privée de gonfler le coût ; coût environ 33 fois plus élevé ; le coût écrit seul
sépare à environ 0,89 ; deux sondes génériques entraînées sans organisme, couches 7, 15, 23, agrégation par maximum ou
attention, sous leur plancher de sondes aléatoires appariées). Conception des sondes : docs/decisions/ (P-011, P-013),
src/controle_ia/sondes/.
RÈGLE R7 (gelée) : aucun chiffre de la littérature n'est opposable sans vérification sur le PDF, page ou table citée. Les
PDF déjà vérifiés du programme sont sous ${A.repo}/docs/sources/pdf/ (avec provenance), leurs lectures sous
${A.repo}/docs/sources/lecture-pdf-niveau1/ et lecture-pdf-niveau2/, la synthèse sous ${A.repo}/docs/etat-de-l-art/.
Cite chaque chiffre avec : fichier PDF (chemin du dépôt ou du bloc-notes), page ou table, et la phrase. Ce que tu ne peux
pas vérifier sur un PDF est marqué « non vérifié » et ne sert jamais de preuve. R8 : une absence dans la littérature est
une question, pas une preuve.
Décision de Lazar N-026 (docs/decisions/decision-N-026-v1.md) : la règle « jamais moyenne ni médiane sur les jetons » reste
entière pour toute sonde de production ; un bras de diagnostic « moyenne », préenregistré, comparé au même plancher apparié
de même agrégation, jamais moniteur, est permis. Vérifie donc sur le PDF, page citée, l'agrégation exacte de chaque travail
(en particulier Apollo, 2502.03407 : moyenne sur quels jetons, et ce que dit le papier des autres agrégations).
`
const SCHEMA_EXTR = {
  type: 'object',
  properties: {
    chemin: { type: 'string' },
    travaux: { type: 'array', items: { type: 'object', properties: {
      reference: { type: 'string' }, pdf: { type: 'string' }, montage: { type: 'string' }, resultat: { type: 'string' },
      ce_qui_fait_marcher: { type: 'string' }, transposable: { type: 'string' }, verifie: { type: 'boolean' },
    }, required: ['reference', 'montage', 'resultat', 'ce_qui_fait_marcher', 'transposable', 'verifie'] } },
  },
  required: ['chemin', 'travaux'],
}
const FAMILLES = [
  { cle: 'anthropic', texte: "Anthropic : « sleeper agents » (2401.05566) et sondes de défection (billet « Simple probes can catch sleeper agents », si une copie vérifiable existe ; sinon « non vérifié »), audit d'objectifs cachés (2503.10965), simulation d'alignement (2412.14093), et tout autre travail Anthropic de détection interne présent dans les PDF du dépôt." },
  { cle: 'apollo', texte: "Apollo Research et sondes de tromperie stratégique : 2502.03407 (Goldowsky-Dill et coll.) et les travaux qui en dérivent ou le comparent, présents dans le dépôt ; données d'entraînement des sondes (paires instruites, jeux de rôle), couches, agrégation, ensembles de test, taux de faux positifs." },
  { cle: 'representations', texte: "Lectures internes classiques : ingénierie des représentations (2310.01405), directions de vérité (2310.06824), connaissance latente (2212.03827), « l'état interne sait quand il ment » (2304.13734), détecteur de mensonge par questions de relance (2309.15840), Poser (2405.05466) ; ce qui transfère d'une distribution à l'autre, et ce qui ne transfère pas." },
  { cle: 'agents', texte: "Sabotage, sous-performance volontaire, agents et moniteurs : travaux du dépôt sur la détection du sabotage ou de la sous-performance par sondes, et sur les comparaisons de moniteurs boîte blanche et boîte noire en contexte d'agent ; cherche dans docs/sources/pdf/ et les lectures (mots : sandbag, sabotage, monitor, probe, white-box, control)." },
  { cle: 'nouveaux', texte: "Travaux récents (2025-2026) ABSENTS du dépôt : cherche en ligne (recherche web si tu l'as), télécharge au plus huit PDF d'arXiv dans ton dossier (jamais dans le dépôt), vérifie chaque chiffre que tu retiens sur le PDF, page citée, et donne l'empreinte sha256 de chaque PDF téléchargé. Priorité : détection interne de la tromperie ou du sabotage chez des agents, sondes entraînées sur le modèle lui-même (« on-policy ») contre données génériques, sondes à faux positifs contrôlés, autoencodeurs parcimonieux pour l'audit." },
]

phase('Extraction')
const extr = await parallel(FAMILLES.map(f => () => agent(`${COMMUN}
Tu es LECTEUR neuf de la famille « ${f.cle} ». ${f.texte}
Pour chaque travail : référence exacte, PDF (chemin), montage (modèle, organisme ou consigne, données d'entraînement de la
sonde, couches, position des jetons, agrégation, données de test, témoins), résultat chiffré (page), ce qui a fait marcher
ou échouer la détection, et ce qui est transposable à P3 (où notre montage diffère). Écris
${A.dossier}/extraction/extraction-${f.cle}.md. Rends les travaux.`,
  { label: `lecteur:${f.cle}`, phase: 'Extraction', schema: SCHEMA_EXTR })))

const pieces = extr.filter(Boolean).map(e => e.chemin).join(', ')
phase('Synthèse')
const synth = await agent(`${COMMUN}
Tu es le RÉDACTEUR de la synthèse (neuf). Extractions : ${pieces}. Pièces externes, non opposables : réponse de Gemini à la
requête 009 ${A.gemini || '(absente)'} (ses renvois de ligne ont déjà été trouvés faux : ne retiens d'elle que des pistes,
jamais un chiffre non vérifié) ; note du brainstorm sur la suite de P3 ${A.brainstorm || '(absente)'}.
Écris ${A.dossier}/synthese-comment-detecter-v1.md, pour Lazar (trois à cinq pages) :
1. verdict en trois lignes : ce que la littérature dit des conditions qui font marcher la détection interne ;
2. table de la littérature (travail, montage, résultat vérifié avec page, ce qui a fait marcher) ;
3. les différences de montage entre ces travaux et P3, classées par leur pouvoir d'expliquer notre nul (données génériques
   contre données sur le modèle ; paires contrastées ; couches ; jetons lus ; consigne privée hors de la fenêtre lue ;
   taille d'effet ; plancher apparié plus exigeant que les témoins usuels ; agrégation) ;
4. trois à cinq expériences de détection, de la moins chère à la plus chère : ce qu'elle tranche, coût (heures de carte,
   dollars), piège principal, contrôle obligatoire (notamment contre la lecture du seul nombre écrit, T4 de P3) ;
5. recommandation et confiance ; ce qui est un nœud de Lazar (revendication, dépense).
Règles : jamais de moyenne ni de médiane sur les jetons d'une action dans une sonde de production ; préenregistrement avant
toute expérience décisive. Rends le chemin et un résumé.`,
  { label: 'redacteur', phase: 'Synthèse', schema: { type: 'object', properties: { chemin: { type: 'string' }, resume: { type: 'string' } }, required: ['chemin', 'resume'] } })

phase('Vérification')
const verif = await agent(`${COMMUN}
Tu es VÉRIFICATEUR neuf : tu n'as écrit ni les extractions ni la synthèse. Synthèse : ${synth ? synth.chemin : A.dossier + '/synthese-comment-detecter-v1.md'} ;
extractions : ${pieces}. Pour CHAQUE chiffre et chaque affirmation sur un travail publié dans la synthèse, ouvre le PDF cité
et vérifie la page : conforme, inexact (corrige), ou introuvable (à retirer). Vérifie aussi que les expériences proposées
respectent les règles (pas de moyenne sur les jetons, préenregistrement, contrôle du nombre écrit). Rapport
${A.dossier}/verification-synthese-v1.md : verdict en tête (« conforme », « conforme après corrections », « non conforme »),
puis chaque écart (id VS-NN, où, problème, correction). Rends le verdict et les écarts en quelques lignes.`,
  { label: 'verificateur', phase: 'Vérification' })

return { extractions: pieces, synthese: synth, verification: verif }
