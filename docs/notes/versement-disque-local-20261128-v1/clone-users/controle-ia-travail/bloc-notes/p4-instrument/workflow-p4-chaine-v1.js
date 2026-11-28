export const meta = {
  name: 'p4-chaine-lancement',
  description: 'Ecrire la chaine de lancement de P4-instrument adaptee de celle de P3, puis trois relectures neuves et independantes',
  phases: [
    { title: 'Ecrire', detail: 'chaine de P4 sous noms neufs, bancs et repetition jouet' },
    { title: 'Relire', detail: 'depense et arrets ; donnees et fuites ; fidelite au texte' },
  ],
}

const S = args.scratch
const R = '/home/user/controle-ia-travail'
const COMMUN = `
Contexte : programme de Lazar (francais, phrases courtes, quasi aucun acronyme). Depot de travail ${R} en LECTURE SEULE pour toi : aucune ecriture, aucune commande git qui ecrit, aucun __pycache__ (python -B, PYTHONDONTWRITEBYTECODE=1, -p no:cacheprovider). Python de la session : /tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python, avec PYTHONPATH=src depuis la racine du depot.

Texte qui fait foi : le brouillon 4 du preenregistrement de P4-instrument, ${S}/P4-instrument-v1-brouillon4.md (sha256 32d821fb42e54341f2649637085de18e2b6b9758b51dc38c504f702ba393ead6) ; plan v2 ${S}/plan-code-et-chaine-v2.md (7c65e4f64e8c65d9f63af1fe6dd755959bba10e7424e2e8ab2826cc1b1d06e13). Le texte prime sur le plan. Module de P4 deja ecrit et teste (182 tests), dans ${S}/module/ (instrument_p4_v1.py 90b9ae8b..., lecture_p4_v1.py 5212cf4d..., mesures_conception_p4_v1.py 483b8ac3..., trois fichiers de tests, NOTES-MODULE.md) : il fournit deja \`--controle module\` et \`--controle go\`. Chaine eprouvee de P3 a adapter : ${R}/docs/procedures/P3-premier-test-v2/ (verifications_p3_v1.py, controles_avant_depense_p3_v1.sh, lancer_p3_v1.sh, surveiller_p3_v1.sh, controle_cinq_minutes_p3_v1.sh, recuperation_p3_v1.sh, sceller_p3_v1.sh, repetition_jouet_p3_v1.sh, repetition_finale_p3_v1.sh, essais_*_p3_v1.sh et leurs journaux de banc) et ${R}/scripts/amorce_instance_p3.sh, ${R}/scripts/p3_instance.sh. Garde de calcul gelee : ${R}/.claude/hooks/garde_calcul.py (registre ${R}/registres/go.md, 8 colonnes, R-281).

Regles gelees a tenir : R5 (chaque garde testee sur un cas sain et sur un artefact, aucun repli silencieux) ; R10 (arrets par PID ou identifiant d'instance, jamais par motif de ligne de commande : pas de pkill, killall, pgrep|xargs kill) ; R11 ; R12 (noms neufs, on n'ecrase jamais) ; aucun texte d'action de P3 dans un fichier pousse ; jamais de moyenne ni de mediane sur les jetons. INTERDITS ABSOLUS : aucune commande Vast.ai reelle (aucune creation, aucun appel au compte : uniquement des binaires factices places dans un PATH de banc, comme les bancs de P3) ; aucun service payant ; aucun reseau sauf la lecture git locale ; ne lis jamais ${R}/prereg/P3-consignes-v1.md ni le contenu d'un fichier textes-actions-* ; n'affiche jamais une cle ou un jeton d'acces. Ecris en francais.`

const RAPPORT = {
  type: 'object',
  properties: {
    verdict: { type: 'string' },
    fichiers: { type: 'array', items: { type: 'object', properties: { chemin: { type: 'string' }, sha256: { type: 'string' } }, required: ['chemin', 'sha256'] } },
    constats: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, gravite: { type: 'string' }, texte: { type: 'string' } }, required: ['id', 'gravite', 'texte'] } },
    points_du_texte: { type: 'array', items: { type: 'string' } },
    rapport_chemin: { type: 'string' },
    resume: { type: 'string' },
  },
  required: ['verdict', 'fichiers', 'constats', 'rapport_chemin', 'resume'],
}

phase('Ecrire')
const ecrit = await agent(`${COMMUN}

TA TACHE (redacteur neuf de la chaine ; dossier d'ecriture ${S}/chaine/, et nulle part ailleurs) :
Adapte la chaine de P3 a P4 sous des noms neufs (R12), selon le texte (en-tete « GO et depense », Plan d'analyse points 1 et 7, Liste d'arret, Chaine de lancement) et le plan v2 (section 4) :
- verifications_p4_v1.py : GO cite GO-2026-10-20-07 seul ; colonne « plafond » qui commence exactement par « 10 USD par lancement » ; echeance lue dans la colonne du GO cite ; revocation par ligne de GO de type « revocation » a 8 colonnes nommant GO-2026-10-04-08, GO-2026-10-20-06, GO-2026-10-20-07, R-262 ou R-269, ou ligne R-... dont la cellule de decision commence par « **Révocation de R-262** » ou « **Révocation de R-269** » ; ligne d'accord du jour « **Accord de Lazar pour le lancement de P4-instrument** » qui cite GO-2026-10-20-07 ou un message de Lazar du jour ; borne de l'etape strictement inferieure a 10 USD ; garde de calcul gelee rejouee sur la commande de creation (jamais contournee). Reutilise les controles du module (--controle go, --controle module) plutot que de les recoder, ou dis pourquoi.
- controles_avant_depense_p4_v1.sh, lancer_p4_v1.sh (GO_ID=GO-2026-10-20-07 dans la commande de creation ; HEURES_CREDIT 3,0 ; surveillance a la creation + 9 600 s ; filtre d'offre egal a celui de P3 ; instance 56799469 toleree si relue arretee tant qu'elle existe ; autres projets de Lazar comme dans P3), amorce_instance_p4_v1.sh (plafond 150 minutes), p4_instance_v1.sh (suite COMPLETE des tests sur l'instance, puis le run ; delai externe 90 minutes ; poussee des sorties des cinq bras ; aucun texte), surveiller_p4_v1.sh, controle_cinq_minutes_p4_v1.sh, recuperation_p4_v1.sh (fichiers attendus de P4, sceaux, aucune fenetre de 48 caracteres d'un texte honnete de P3 dans un fichier pousse — lis ce que fait la recuperation de P3 pour cela et reprends-le sans afficher de texte —, chaines de 200 caracteres au plus, destruction de l'instance par son identifiant apres la recuperation verifiee), sceller_p4_v1.sh (commit S : texte, configuration et sceaux seulement), repetition_jouet_p4_v1.sh, repetition_finale_p4_v1.sh, et les bancs essais_*_p4_v1.sh avec leurs journaux.
- Lance les bancs (cas sain et artefacts de chaque controle neuf) et la repetition jouet sur processeur, dans des depots jouets sous ${S}/chaine/tmp/, avec des binaires vastai factices. Garde les journaux. Chaque fichier ecrit recoit un compagnon .sha256 « <sha>  <nom> ».
- Ecris ${S}/chaine/NOTES-CHAINE.md : correspondance avec la chaine de P3 (ce qui change, ce qui reste), liste des bancs et de leurs resultats, et tout point ou le texte se tait ou se contredit, avec ta lecture.
Rends le schema demande ; « resume » en 15 lignes au plus.`, { label: 'redacteur-chaine', phase: 'Ecrire', schema: RAPPORT })

if (!ecrit) return { ecrit: null, relectures: [] }

phase('Relire')
const LENTILLES = [
  { cle: 'depense', texte: `LENTILLE « DEPENSE ET ARRETS » : formes exactes du GO, de l'accord, de la revocation et du plafond ; garde gelee rejouee ; credit exige ; borne de l'etape ; filtre d'offre ; surveillance et arret par identifiant (R10, jamais par motif) ; codes de sortie ; aucun chemin ou une creation peut avoir lieu apres un controle en echec. Fabrique toi-meme des artefacts (registre mal forme, GO echu, revocation sous chaque forme, accord d'un autre jour, plafond sans le prefixe, garde qui refuse) et fais-les passer dans les verifications.` },
  { cle: 'donnees', texte: `LENTILLE « DONNEES ET FUITES » : empreintes des donnees de P3, du module et de la configuration verifiees (R11) ; arbre gele egal a 7a54d43 ; aucun texte d'action poussee (controle des fenetres de 48 caracteres), aucune activation gardee, aucune cle affichee ; commit S limite au texte, a la configuration et aux sceaux ; recuperation qui verifie les sceaux avant la destruction de l'instance. Fabrique des artefacts (fichier pousse portant une fenetre de texte, sceau faux, fichier attendu absent) et verifie qu'ils arretent.` },
  { cle: 'fidelite', texte: `LENTILLE « FIDELITE AU TEXTE » : chaque ligne de la section « Chaine de lancement », des points 1 et 7 du Plan d'analyse, de l'en-tete « GO et depense » et de la Liste d'arret du brouillon 4 a-t-elle son controle dans la chaine, au bon moment, et rien de plus ? Ordre des etapes ; suite complete des tests sur l'instance ; bornes de temps (3 600 s, 90 minutes, 150 minutes, creation + 9 600 s) ; lecture refusee avant le verdict complete de P3. Donne pour chaque ecart la ligne du texte et la ligne du script.` },
]
const relectures = await parallel(LENTILLES.map(l => () => agent(`${COMMUN}

Tu es un relecteur NEUF : tu n'as ecrit ni le texte, ni le module, ni la chaine. ${l.texte}

Chaine a relire : ${S}/chaine/ (rendu du redacteur : ${JSON.stringify(ecrit, null, 1)}).
Ecris seulement dans ${S}/relecture-chaine-${l.cle}/ : ton rapport relecture-chaine-${l.cle}-v1.md (compagnon .sha256), tes depots jouets et tes artefacts. Verdict : « conforme », « conforme apres corrections » ou « non conforme » ; constats numerotes RC-${l.cle}-01... avec gravite (critique, majeur, mineur, information), ligne du script, cas qui le montre, correction proposee. Rends le schema demande ; « resume » en 10 lignes au plus.`, { label: `relire:${l.cle}`, phase: 'Relire', schema: RAPPORT })))

return { ecrit, relectures }
