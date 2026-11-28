export const meta = {
  name: 'p3-outils-lecture-activations',
  description: 'Brainstorm verifie : outils autres que les sondes pour lire les activations et detecter la tromperie dans P3 ; consigne contre intention ; arbre P4 -> P3b -> P3c ou organisme (ii)',
  phases: [
    { title: 'Balayer', detail: 'quatre angles independants : Anthropic, autres organismes, consigne contre intention, programme' },
    { title: 'Concevoir', detail: 'menu classe des outils et arbre de decision' },
    { title: 'Contredire', detail: 'fidelite aux sources et anti-faux-gap ; methode et circularite' },
    { title: 'Finaliser', detail: 'note v1 et noeuds pour Lazar' },
  ],
}

const S = args.scratch
const R = '/home/user/controle-ia-travail'
const COMMUN = `
Contexte : programme de Lazar « controle boite blanche des menaces diffuses ». Francais, phrases courtes, quasi aucun acronyme (developpe les termes). Depot de travail ${R} en LECTURE SEULE. Tu ecris seulement dans ${S}/.

Le cas : P3 a teste deux sondes generiques (tromperie, recette d'Apollo, difference de moyennes, couche 15 ; enjeux eleves, lineaire, couche 15), entrainees hors de l'organisme, sur les actions d'un agent Llama-3.1-8B-Instruct qui propose des experiences (environnement (a)), saboteur par consigne cachee en mode « cout gonfle » (organisme (i-a)) contre honnete, 60 taches, 10 pas, 600 actions par condition ; score d'une action = maximum sur ses jetons. Resultat : sabotage reel (cout declare environ 30 fois plus eleve) ; aucune sonde au-dessus du plancher apparie (200 directions au hasard de meme covariance) : tromperie aire 0,575 [0,531 ; 0,618] contre quantile 0,95 du plancher 0,572 ; enjeux 0,525 contre 0,536 ; verdict « non detecte a cette puissance » (${R}/docs/verdicts/verdict-P3-premier-test-i-a-v1.md, section 1). Prevus : P4 (controle positif de l'instrument : phrase de persona de l'entrainement inseree dans le contexte d'episodes honnetes rejoues, textes d'action imposes ; ${S}/../p4-instrument/P4-instrument-v1-candidat1.md, sections Hypothese et « Ce que H-P4 n'affirme pas ») ; P3b (decision N-028 : sondes localisees au champ du cout, plancher apparie, sonde « oracle » entrainee sur l'organisme en validation croisee par tache, controles T1, T3, T4). Au programme : organisme (ii) (consigne distillee dans les poids par reglage fin leger), famille (iii) (organismes publics de sous-performance de l'institut britannique de surete, dont un qui imite Llama-3.1-8B-Instruct), test de validite de T0.7 (une sonde qui lit « j'ai une consigne cachee » reussit sur (i) et echoue sur (ii) ; une sonde d'intention reussit sur les deux) : ${R}/docs/brief-claude-code-programme-complet-v2.md lignes 154-175.

Question de Lazar : quels autres outils que les sondes pour lire les activations et detecter la tromperie (par exemple la « J-lens » d'Anthropic, les autoencodeurs parcimonieux) ? Que ferait Anthropic pour distinguer une consigne lue d'une intention executee ? Faut-il un P3c ou d'autres versions de P3 ?

Regles gelees qui s'appliquent : R7 (aucun chiffre de la litterature sans verification sur le PDF, page citee : un chiffre non verifie s'ecrit « non verifie » et ne sert a rien decider) ; R8 (zone vierge = question ; limite d'un papier n'est pas un trou du champ ; les zones vierges seduisantes se verifient plus durement) ; R3 (aucun essai qui vise un signe positif).
INTERDITS : ne lis jamais ${R}/prereg/P3-consignes-v1.md, ni un fichier textes-actions-*, ni rien sous ${R}/donnees/ ; aucune recherche recursive dans ${R} (pas de grep -r, pas de find qui lit des contenus) ; aucune donnee de P3 envoyee nulle part ; recherches web generiques seulement (jamais un contenu du depot) ; aucun service payant, aucune commande Vast.ai, aucun appel a Gemini ; n'affiche jamais une cle. Pour un PDF : telecharge-le d'arXiv (ou du site de l'auteur) dans ${S}/pdf/, calcule son sha256, lis-le par pdftotext -layout, cite la page du PDF.
`
const SORTIE = {
  type: 'object',
  properties: {
    rapport_chemin: { type: 'string' },
    rapport_sha256: { type: 'string' },
    outils: { type: 'array', items: { type: 'object', properties: {
      nom: { type: 'string' }, source: { type: 'string' }, verifie_sur_pdf: { type: 'boolean' }, page: { type: 'string' },
      ce_quil_lit: { type: 'string' }, disponible_llama31_8b: { type: 'string' }, apport_pour_P3: { type: 'string' }, limites: { type: 'string' } },
      required: ['nom', 'source', 'verifie_sur_pdf', 'ce_quil_lit', 'apport_pour_P3'] } },
    resume: { type: 'string' },
  },
  required: ['rapport_chemin', 'outils', 'resume'],
}

const ANGLES = [
  { cle: 'anthropic', texte: `ANGLE « ANTHROPIC » : la J-lens (« Jacobian lens » ; article arXiv 2607.15495 « Verbalizable Representations Form a Global Workspace in Language Models », code github.com/anthropics/jacobian-lens ; suite arXiv 2608.31084) : ce qu'elle lit, comment (jacobien moyen), sur quels modeles, ce qu'il faut pour l'appliquer a Llama-3.1-8B-Instruct (calcul, code, licence), resultats lies a la tromperie ou au chantage s'il y en a (verifies sur PDF) ; le jeu d'audit a l'aveugle (arXiv 2503.10965) et ses huit techniques ; les sondes de defection sur agents dormants (« Simple probes can catch sleeper agents ») et leur reserve ; le tracage de circuits et les graphes d'attribution (bibliotheque publique, transcodeurs disponibles pour quels modeles) ; les vecteurs de persona ; les crosscodeurs et la comparaison de modeles ; tout autre outil d'Anthropic pertinent publie jusqu'a octobre 2026.` },
  { cle: 'autres', texte: `ANGLE « AUTRES ORGANISMES » : Apollo Research (sondes de tromperie strategique, Goldowsky-Dill et al. 2025 ; gain boite blanche sur boite noire) ; Google DeepMind (autoencodeurs Gemma Scope ; resultats negatifs de 2025 sur les autoencodeurs face aux sondes) ; comparaison sondes et autoencodeurs a grande echelle (arXiv 2502.16681, dont l'annexe Llama-3.1-8B avec Llama Scope) ; autoencodeurs publies pour Llama-3.1-8B (Llama Scope ; Goodfire pour la version instruite) ; institut britannique de surete (jeux d'audit de sous-performance, organismes publics) ; Redwood et ARC (detection d'anomalies mecaniques) ; EleutherAI (lentille accordee, autoencodeurs) ; Transluce (descriptions d'activations, agents enqueteurs) ; LatentQA, Patchscopes, oracles d'activation ; arXiv 2507.22149 (representations sous consigne trompeuse, Llama-3.1-8B-Instruct) ; ICML 2026 « Probe Generalization as Subspace Selection for OOD Deception Detection ». Pour chaque outil : disponibilite reelle pour Llama-3.1-8B-Instruct.` },
  { cle: 'consigne-intention', texte: `ANGLE « CONSIGNE CONTRE INTENTION ET VERITE TERRAIN » : comment la litterature distingue une sonde qui lit une consigne presente dans le contexte d'une sonde qui lit une intention executee : organismes a objectif installe dans les poids (agents dormants, jeu d'audit, distillation de contexte, faux alignement) ; sondes hors politique contre en politique ; plans consigne presente ou absente x comportement execute ou non ; ecart entre croyance interne et sortie (decoder la vraie valeur dans les activations pendant que le modele ecrit une valeur fausse : verite des representations, « geometry of truth », sondes de verite) ; validation causale (pilotage, ablation, echange d'activations) ; etiquetage par action plutot que par condition. Dis ce que ferait Anthropic, avec sources.` },
  { cle: 'programme', texte: `ANGLE « PROGRAMME » (lecture interne seulement, aucune recherche web) : lis ${R}/docs/verdicts/verdict-P3-premier-test-i-a-v1.md (en entier), ${S}/../p4-instrument/P4-instrument-v1-candidat1.md (sections Hypothese, Pare-feu, Criteres de lecture), dans ${R}/registres/decisions.md seulement les lignes qui commencent par « | N-025 », « | N-028 », « | R-262 » (grep -n sur ce seul fichier), ${R}/docs/brief-claude-code-programme-complet-v2.md lignes 154-200, et la synthese de la revue ${S}/../revue-detection/synthese-comment-detecter-v4.md. Rends : ce qui est deja prevu (P4, P3b, addendum 2, T0.6, T0.7, organisme (ii), famille (iii)), ce que chaque piece peut et ne peut pas trancher, les donnees de P3 gardees (scores seulement ? activations ?) d'apres ces textes, et les trous reels du plan face a la question de Lazar. Le schema « outils » peut lister les outils deja prevus au programme.` },
]

phase('Balayer')
const balayages = await parallel(ANGLES.map(a => () => agent(`${COMMUN}\n${a.texte}\nEcris ${S}/balayage-${a.cle}-v1.md (+ .sha256) : pour chaque outil ou fait, la source, verifie sur PDF ou non, la page. Rends le schema demande ; « resume » en 12 lignes au plus.`, { label: `balayer:${a.cle}`, phase: 'Balayer', schema: SORTIE })))
const ok = balayages.filter(Boolean)
log(`${ok.length} balayages sur 4`)

phase('Concevoir')
const conception = await agent(`${COMMUN}
Tu es un CONCEPTEUR NEUF. Rapports des balayages : ${ok.map(b => b.rapport_chemin).join(' ; ')}. Lis-les tous.
Ecris ${S}/conception-v1.md (+ .sha256) :
1. Ce qu'un expert ferait ici avant de changer d'outil (plafond de lisibilite, localisation, etiquetage par action, double comptabilite, causalite, base boite noire).
2. Les donnees brutes a utiliser au depart (et ce qu'il faudrait regenerer, d'apres l'angle programme).
3. Menu des outils, classe : ce que chacun leverait de l'ambiguite du nul de P3 ; disponibilite reelle pour Llama-3.1-8B-Instruct ; cout (heures de carte, ordre de grandeur) ; risque de circularite ou de peche (comparaisons multiples) ; test causal qui validerait sa lecture ; base boite noire de comparaison.
4. Consigne contre intention : le plan qui les separe, avec les organismes du programme ((i) temoin instruit, (ii) distille, (iii) publics).
5. Arbre de decision P4 -> P3b -> P3c ou organisme (ii) : pour chaque issue, ce qui suit, ce que cela coute, ce qui est un noeud de Lazar ; faut-il un P3c, avec quel perimetre, preenregistre quand (avant la lecture de P3b ?).
6. Validation exterieure a la session et a Lazar.
Aucun chiffre de la litterature sans page verifiee (sinon « non verifie »). Rends le schema demande.`, { label: 'concevoir', phase: 'Concevoir', schema: SORTIE })

phase('Contredire')
const CRITIQUES = [
  { cle: 'sources', texte: `LENTILLE « FIDELITE AUX SOURCES ET ANTI-FAUX-GAP » (R7, R8) : chaque affirmation sur un outil ou un resultat est-elle juste et sourcee ? Re-verifie sur les PDF les chiffres et les affirmations decisives (disponibilite pour Llama-3.1-8B, resultats sur la tromperie). Une zone dite libre l'est-elle vraiment ? Une limite d'un papier est-elle presentee comme un trou du champ ?` },
  { cle: 'methode', texte: `LENTILLE « METHODE » (adverse) : circularite (outil choisi ou regle sur les donnees qu'il juge), peche dans des dizaines de milliers de caracteristiques sans partition decouverte et confirmation, lecture d'une consigne prise pour une intention, essai qui vise un signe positif (R3), cout sous-estime, P3c qui deviendrait une seconde lecture deguisee de P3 (interdit par son preenregistrement, l. 415-416 et l. 428 : toute lecture ajoutee passe par un preenregistrement complementaire et un noeud). L'arbre de decision tient-il ? Propose les corrections exactes.` },
]
const critiques = await parallel(CRITIQUES.map(c => () => agent(`${COMMUN}
Tu es un CRITIQUE NEUF : tu n'as ecrit ni les balayages ni la conception. Conception : ${conception ? conception.rapport_chemin : '(absente)'} ; balayages : ${ok.map(b => b.rapport_chemin).join(' ; ')}.
${c.texte}
Ecris ${S}/critique-${c.cle}-v1.md (+ .sha256), constats numerotes CR-${c.cle}-01... avec gravite et correction proposee. Rends le schema demande (outils : liste des outils dont tu contestes la description, sinon vide).`, { label: `contredire:${c.cle}`, phase: 'Contredire', schema: SORTIE })))

phase('Finaliser')
const note = await agent(`${COMMUN}
Tu es un REDACTEUR NEUF. Pieces : balayages ${ok.map(b => b.rapport_chemin).join(' ; ')} ; conception ${conception ? conception.rapport_chemin : '(absente)'} ; critiques ${critiques.filter(Boolean).map(c => c.rapport_chemin).join(' ; ')}.
Ecris ${S}/note-outils-lecture-activations-P3-v1.md (+ .sha256) pour Lazar : approfondie, pas longue (au plus 250 lignes). Verdict d'abord (3 lignes). Puis : (1) ce qu'un expert ferait ici ; (2) donnees brutes de depart ; (3) outils classes (table : ce qu'il lit, apport pour P3, disponible pour Llama-3.1-8B-Instruct, cout, test causal, reserve) ; (4) consigne contre intention, ce que ferait Anthropic ; (5) validation exterieure ; (6) arbre P4 -> P3b -> P3c ou organisme (ii), et reponse nette « faut-il un P3c » ; (7) noeuds pour Lazar au format : decision en une phrase ; enjeu ; 2 ou 3 options (avantage, inconvenient) ; recommandation et confiance ; defaut sous 48 heures. Applique chaque critique (ou dis pourquoi non, en une ligne). Chaque chiffre : source, page, « verifie sur PDF » ou « non verifie ». Liste des sources a la fin avec URL et sha256 des PDF lus. Rends le schema demande ; « resume » en 15 lignes au plus.`, { label: 'finaliser', phase: 'Finaliser', schema: SORTIE })
return { balayages: ok.map(b => ({ chemin: b.rapport_chemin, resume: b.resume })), conception: conception && conception.rapport_chemin, critiques: critiques.filter(Boolean).map(c => ({ chemin: c.rapport_chemin, resume: c.resume })), note }
