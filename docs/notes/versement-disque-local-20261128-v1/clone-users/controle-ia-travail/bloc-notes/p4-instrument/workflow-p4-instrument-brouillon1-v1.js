export const meta = {
  name: 'p4-instrument-brouillon1',
  description: "P4-instrument (contrôle positif de l'instrument, R-262 point 1) : brouillon 1 du préenregistrement et plan de chaîne par un rédacteur neuf, puis contre-lecture R2 par un sous-agent neuf",
  phases: [
    { title: 'Rédaction', detail: 'préenregistrement, plan de code et de chaîne, devis' },
    { title: 'Contre-lecture', detail: 'R2 par un sous-agent neuf' },
  ],
}
const A = args
const COMMUN = `
Programme « contrôle boîte blanche des menaces diffuses », dirigé par Lazar. Français, phrases courtes, quasi aucun acronyme.
Dépôt en LECTURE SEULE : ${A.repo} (aucune écriture, aucune commande git qui écrive, aucune commande Vast.ai, aucun service
payant, aucun contact). Tu écris seulement dans ${A.dossier}/. Ne lis jamais prereg/P3-consignes-v1.md, ni les textes
d'action (donnees/*/textes-actions-*.jsonl), ni aucune clé.
Décision de Lazar R-262 (registres/decisions.md) : avant la présentation, point (1) : un contrôle positif de l'instrument,
« P4-instrument », tel que la note du brainstorm le décrit (docs/notes/brainstorm-suite-P3-v1/note-decision-suite-P3-v1.md,
option A1 et section « À préenregistrer en premier », point 2 ; objections et réponses dans le même dossier). Contexte :
verdict de P3 docs/verdicts/verdict-P3-premier-test-i-a-v1.md (nul : sondes génériques sous leur plancher) ; préenregistrement
de P3 prereg/P3-premier-test-i-a-v1.md ; chaîne de P3 docs/procedures/P3-premier-test-v2/ (lanceur, contrôles, surveillance,
récupération) ; code src/controle_ia/premier_test_ia/ (entrainement.py, figees.py, run.py, lecture.py, statistiques.py) et
src/controle_ia/sondes/ ; décisions P-011, P-013, N-026 (bras de diagnostic « moyenne » permis s'il est préenregistré, jamais
en production), N-027 (G0 fin novembre) ; brouillons T0.6 et T0.7 sous brouillons/. Addendum 2 de P3 (N-025) en cours : une
réserve qu'il ajouterait se recopie dans P4-instrument (branche B de la note).
Règles gelées : R1 (préenregistrement scellé avant toute lecture), R2, R3 (aucun run visant un signe positif), R4, R5, R9
(graines par SeedSequence, manifeste), R10, R12 ; jamais de moyenne ni de médiane sur les jetons d'une action dans une sonde
de production ; dépense seulement par la délégation R-217 (préenregistrement scellé et contre-lu, GO-2026-10-04-08, plafond
150 USD, échéance 1er novembre, crédit 11,79 USD : un lancement à la fois).
`
phase('Rédaction')
const b1 = await agent(`${COMMUN}
Tu es le RÉDACTEUR (neuf). Écris ${A.dossier}/P4-instrument-v1-brouillon1.md : préenregistrement complet au gabarit du dépôt
(prereg/gabarit-preregistrement-v1.md ; sections exigées par src/controle_ia/prereg.py), qui fixe : la liste fermée de la
note (M5 : plancher noté sur la validation générique, garde de lisibilité ; C1 corrigée, seule lecture décisive : actions
honnêtes de P3 précédées de la phrase de persona de l'entraînement, malhonnête contre honnête, sonde, plancher et métrique de
P3 figés ; M6 : consigne bénigne de même longueur, référence) ; hypothèse, prédictions chiffrées et signe, métrique, seuils
fixés d'avance (dont « sonde non privilégiée » si le plancher dépasse 0,80 ou si sa médiane sort de [0,45 ; 0,55], audit R4
au-dessus de 0,90), plan d'analyse, critères de lecture gelés, liste d'arrêt, garde d'identité (empreinte de trajectoire ou, à
défaut, nombre de jetons par action et scores des sondes légères, tolérance fixée ; écarts exclus et comptés ; plus de 10 %
d'une condition : pas de lecture ; garde testée sur un cas sain et un artefact), pare-feu (rien ne relit P3, rien ne règle
T0.7), lieu de confirmation (épisodes de T0.6 lus par T0.7). Vérifie chaque fait dans le code (fichier, ligne) : en
particulier ce que sont la phrase de persona, la validation générique (taille), le plancher et sa recette. Écris aussi
${A.dossier}/plan-code-et-chaine-v1.md : ce qui se réutilise de P3 tel quel, ce qui est neuf (module, tests), la chaîne de
lancement (adaptée de celle de P3), et un devis (heures de carte, prix, plafond, avec leurs sources dans registres/depenses.md
et les journaux de P3). Rends les chemins, les empreintes et les questions ouvertes pour la session.`,
  { label: 'redacteur', phase: 'Rédaction', schema: { type: 'object', properties: { prereg: { type: 'string' }, sha256: { type: 'string' }, plan: { type: 'string' }, devis: { type: 'string' }, questions: { type: 'array', items: { type: 'string' } } }, required: ['prereg', 'sha256', 'plan', 'devis', 'questions'] } })

phase('Contre-lecture')
const r2 = await agent(`${COMMUN}
Tu es CONTRE-LECTEUR neuf (R2) : tu n'as écrit ni ce brouillon, ni la note du brainstorm, ni P3. Brouillon :
${b1 ? b1.prereg : A.dossier + '/P4-instrument-v1-brouillon1.md'} ; plan ${A.dossier}/plan-code-et-chaine-v1.md.
Vérifie : chaque grandeur est-elle définie sans ambiguïté et fidèle au code (fichier, ligne) ? Le contrôle positif est-il
vraiment positif (ce que la sonde DOIT voir), et la lecture « sonde non privilégiée » contre « aveugle » est-elle mécanique ?
La garde d'identité tient-elle (cas sain, artefact) ? Le texte relit-il P3 ou règle-t-il T0.7 (interdit) ? R3 : vise-t-il un
signe ? Le devis est-il sourcé et dans le crédit ? Rapport ${A.dossier}/contre-lecture-R2-P4-instrument-brouillon1-v1.md :
verdict en tête (« scellable », « scellable après corrections », « non scellable »), constats (id RP-NN, gravité, où,
problème, correction), le plus grave d'abord. Rends le verdict et les constats en quelques lignes.`,
  { label: 'contre-lecteur', phase: 'Contre-lecture' })
return { b1, r2 }
