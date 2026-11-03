"""Colognese et Ward Q2, ensemble tour + course v2 : consignes des moissonneurs du lot 2 et du groupeur aveugle de l'ensemble (mode prep),
puis dossier « ensemble » et consigne du classeur (mode classeur). Gabarits scellés."""
import hashlib, json, sys, os, glob, shutil
R = '/home/claude/controle-ia-travail/'; P = R + 'brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/'
S = '/home/claude/scratch/soir-rapport/colognese-ward-q2/'; E = '/home/claude/scratch/soir-rapport/colognese-ward-q2-ensemble/'
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
QNOM = "la question 2 (facultative) de Paul Colognese et Francis Rhys Ward, sur leur billet"
QTEXTE = "(Optional) Read this post. Should we have done anything differently? What was the most interesting finding in your view and why?"
PIECE = R + 'brouillons/ideation-mentors-soir-v1/piece-colognese-ward-v1.md'
def gabarit(nom):
    g = P + nom; assert sha(g) == open(g + '.sha256').read().split()[0], nom; return open(g).read()
NA = "\n**N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le. Toute commande : `timeout 60 nice -n 10 …`.\n"
if sys.argv[1] == 'prep':
    tpl = gabarit('soir-moissonneur-C-gabarit-v1.md')
    for part in sorted(glob.glob(S + 'prep-v1/fiches-lot2-moisson-part-*-v1.json')):
        k = part.split('-part-')[1].split('-')[0]; n = len(json.load(open(part)))
        t = (tpl.replace('<<QNOM>>', QNOM).replace('<<QTEXTE>>', QTEXTE).replace('<<ENTREE>>', part).replace('<<H_ENTREE>>', sha(part)).replace('<<N>>', str(n))
             .replace('<<MENTOR_TRAVAUX>>', f"Leur billet et leurs travaux sont décrits dans `{PIECE}`, section 1 (lecture permise). N'ouvre pas les autres parts ni leurs sorties.")
             .replace('<<SORTIE>>', S + f'moisson-C/moisson-lot2-part-{k}-v1.json')) + NA
        q = P + f'soir-moissonneur-C-colognese-ward-q2-lot2-part-{k}-v1.md'; open(q, 'w').write(t); print('moissonneur', k, n, sha(q))
    os.makedirs(E + 'piste', exist_ok=True)
    gi = E + 'piste/fiches-a-grouper-v1.json'; shutil.copy(S + 'piste/fiches-a-grouper-ensemble-v1.json', gi)
    g = open(P + 'piste-colognese-ward-q2-groupeur-aveugle-v1.md').read()
    a = "`/home/claude/scratch/soir-rapport/colognese-ward-q2/piste/fiches-a-grouper-v1.json` (sha256 `ee72eed6c715dc49a1651388b3a8191546e92b298bf7f48f6fb44d8abfc85ffa`)"
    assert g.count(a) == 1
    g = g.replace(a, f"`{gi}` (sha256 `{sha(gi)}`)").replace('dossier `/home/claude/scratch/soir-rapport/colognese-ward-q2/piste/`', f'dossier `{E}piste/`')
    g = g.replace("Ne lis rien d'autre que le fichier d'entrée (surtout pas `classement-D/`, `moisson-C/`, `prep-v1/`, `lecteur-A/`, ni `/home/claude/coffre-*`).",
                  "Ne lis rien d'autre que le fichier d'entrée (surtout pas `classement-D/`, `moisson-C/`, `prep-v1/`, `lecteur-A/`, `source-2/`, le dossier `colognese-ward-q2/` ni `/home/claude/coffre-*`).") + NA
    q = P + 'piste-colognese-ward-q2-groupeur-aveugle-ensemble-v1.md'; open(q, 'w').write(g); print('groupeur', sha(q))
elif sys.argv[1] == 'classeur':
    for d in ('prep-v1', 'moisson-C', 'classement-D', 'lecteur-A'): os.makedirs(E + d, exist_ok=True)
    fs = E + 'prep-v1/fiches-servies-v1.json'; shutil.copy(S + 'prep-v1/fiches-ensemble-v1.json', fs)
    shutil.copy(S + 'lecteur-A/fiches-normalisees-v2.json', E + 'lecteur-A/fiches-normalisees-v1.json')
    m1 = json.load(open(S + 'moisson-C/moisson-fusionnee-v1.json')); m1 = m1 if isinstance(m1, list) else next(v for v in m1.values() if isinstance(v, list))
    m2 = []
    for p in sorted(glob.glob(S + 'moisson-C/moisson-lot2-part-*-v1.json')):
        x = json.load(open(p)); m2 += x if isinstance(x, list) else next(v for v in x.values() if isinstance(v, list))
    mf = E + 'moisson-C/moisson-fusionnee-v1.json'; json.dump(m1 + m2, open(mf, 'w'), ensure_ascii=False, indent=1)
    ids = {f['id'] for f in json.load(open(fs))}; idm = {e['id'] for e in m1 + m2}
    print('moisson', len(m1), '+', len(m2), '; fiches sans moisson', sorted(ids - idm), sha(mf))
    t = (gabarit('soir-classeur-D-gabarit-v1.md').replace('<<QNOM>>', QNOM).replace('<<QTEXTE>>', QTEXTE).replace('<<FICHES>>', fs).replace('<<H_FICHES>>', sha(fs))
         .replace('<<MOISSON>>', mf).replace('<<H_MOISSON>>', sha(mf)).replace('<<PIECE>>', PIECE).replace('<<DOSSIER>>', E + 'classement-D/').replace('<<SLUG>>', 'colognese_ward_q2'))
    t += NA + "numpy 2.5.3 est installé. Écris `notes-v1.json` dans les dix premières minutes.\n"
    q = P + 'soir-classeur-D-colognese-ward-q2-ensemble-v1.md'; open(q, 'w').write(t); print('classeur', sha(q))
