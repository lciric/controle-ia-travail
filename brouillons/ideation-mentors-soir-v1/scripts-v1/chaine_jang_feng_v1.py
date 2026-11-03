"""Chaîne Feng et Jang après le lecteur A : préparation (source unique), consignes du groupeur aveugle et des moissonneurs (gabarit scellé),
puis, en mode « classeur », fusion des moissons et consigne du classeur (gabarit scellé).
Usage : chaine_jang_feng_v1.py prep | chaine_jang_feng_v1.py classeur"""
import hashlib, json, sys, os, subprocess, glob
R = '/home/claude/controle-ia-travail/'; P = R + 'brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/'
S = '/home/claude/scratch/soir-rapport/jang-feng/'; SC = '/home/claude/scratch/soir-rapport/scripts/'
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
QNOM = "la question de Shi Feng et Eyon Jang (valeur et limites des moniteurs et des méthodes d'audit en boîte blanche)"
QTEXTE = "What are your thoughts on the value of white-box monitors and white-box methods for auditing? What do you see as their current limitations?"
PIECE = R + 'brouillons/ideation-mentors-soir-v1/piece-jang-feng-v1.md'
def gabarit(nom):
    g = P + nom; assert sha(g) == open(g + '.sha256').read().split()[0], nom; return open(g).read()
mode = sys.argv[1]
if mode == 'prep':
    out = subprocess.run(['python3', '-I', SC + 'preparer_source_unique_v1.py', S + 'lecteur-A/fiches-normalisees-v1.json', 'JF', S + 'prep-v1', S + 'piste',
                          '/home/claude/coffre-soir/cle-preparation-jang-feng-v1.json', '8'], capture_output=True, text=True, check=True).stdout
    print(out)
    gi = S + 'piste/fiches-a-grouper-v1.json'
    g = f"""Tu es un **groupeur neuf**, aveugle au classement. Travail en français, sans sigle non développé ; toute heure vient de `date -u`. Vise 15 minutes.

## Contexte
Deux mentors (Shi Feng et Eyon Jang) demandent : que valent les moniteurs et les méthodes d'audit en boîte blanche (lecture des activations, sondes, autoencodeurs épars), et quelles sont leurs limites actuelles ? Le fichier contient des fiches d'idées.

## Entrée (lecture seule)
`{gi}` (sha256 `{sha(gi)}`) : pour chaque fiche, `id`, `enonce`, `mecanisme`. Vérifie l'empreinte avant de lire.

## Ce que tu fais
1. **D'abord, avant toute affectation**, écris les groupes : 3 à 6 **affirmations sur la valeur ou les limites (ce que la réponse soutiendrait)** distinctes, par mécanisme. Pour chacune : un nom court, une définition en deux lignes, et le critère qui dit si une fiche en relève.
2. Puis affecte **chaque fiche à un seul groupe** (son idée principale), avec une raison en une ligne ; « second choix » si une fiche relève presque autant d'un autre groupe. Aucune fiche hors groupe.
3. Ne change pas les définitions après coup ; note toute tension dans une rubrique « limites ».

## Ce que tu écris (fichiers neufs, dossier `{S}piste/`)
- `groupes-v1.json` : `{{"groupes": [{{"nom", "definition", "critere"}}], "affectations": [{{"id", "groupe", "raison", "second_choix"}}]}}`.
- `groupes-v1.md` : les définitions (avec l'heure à laquelle tu les as écrites), le tableau des affectations, les limites.

## Interdits
Ne lis rien d'autre que le fichier d'entrée (surtout pas `classement-D/`, `moisson-C/`, `prep-v1/`, `lecteur-A/`, `source-2/`, ni `/home/claude/coffre-*`). Aucun commit, aucun `.sha256`, aucun fichier existant modifié, aucun appel réseau ni de modèle, aucun `git`. Toute commande : `timeout 60 nice -n 10 …`. **N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le.

## Rendu
Réponse finale : les groupes (nom et définition en une ligne), le nombre de fiches par groupe, les fiches à second choix, les limites ; chemins et sha256 des deux fichiers.
"""
    open(P + 'piste-jang-feng-groupeur-aveugle-v1.md', 'w').write(g)
    print('groupeur', sha(P + 'piste-jang-feng-groupeur-aveugle-v1.md'))
    tpl = gabarit('soir-moissonneur-C-gabarit-v1.md')
    os.makedirs(S + 'moisson-C', exist_ok=True)
    for part in sorted(glob.glob(S + 'prep-v1/fiches-moisson-part-*-v1.json')):
        k = part.split('-part-')[1].split('-')[0]; n = len(json.load(open(part)))
        t = (tpl.replace('<<QNOM>>', QNOM).replace('<<QTEXTE>>', QTEXTE).replace('<<ENTREE>>', part).replace('<<H_ENTREE>>', sha(part)).replace('<<N>>', str(n))
             .replace('<<MENTOR_TRAVAUX>>', f"Leurs travaux sont décrits dans `{PIECE}`, section 1 (lecture permise). N'ouvre pas les autres parts ni leurs sorties.")
             .replace('<<SORTIE>>', S + f'moisson-C/moisson-part-{k}-v1.json'))
        t += "\n**N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le. Toute commande : `timeout 60 nice -n 10 …`.\n"
        q = P + f'soir-moissonneur-C-jang-feng-part-{k}-v1.md'; open(q, 'w').write(t); print('moissonneur', k, n, sha(q))
elif mode == 'classeur':
    parts = sorted(glob.glob(S + 'moisson-C/moisson-part-*-v1.json'))
    fus = []
    for p in parts:
        x = json.load(open(p)); fus += x if isinstance(x, list) else next(v for v in x.values() if isinstance(v, list))
    mf = S + 'moisson-C/moisson-fusionnee-v1.json'; json.dump(fus, open(mf, 'w'), ensure_ascii=False, indent=1)
    fs = S + 'prep-v1/fiches-servies-v1.json'
    ids_f = {f['id'] for f in json.load(open(fs))}; ids_m = {e['id'] for e in fus}
    print('moisson fusionnée', len(fus), 'entrées ; fiches sans moisson', sorted(ids_f - ids_m), sha(mf))
    os.makedirs(S + 'classement-D', exist_ok=True)
    t = (gabarit('soir-classeur-D-gabarit-v1.md').replace('<<QNOM>>', QNOM).replace('<<QTEXTE>>', QTEXTE).replace('<<FICHES>>', fs).replace('<<H_FICHES>>', sha(fs))
         .replace('<<MOISSON>>', mf).replace('<<H_MOISSON>>', sha(mf)).replace('<<PIECE>>', PIECE).replace('<<DOSSIER>>', S + 'classement-D/').replace('<<SLUG>>', 'jang_feng'))
    t += "\n**N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le. Toute commande : `timeout 60 nice -n 10 …` (numpy 2.5.3 est installé). Écris `notes-v1.json` dans les dix premières minutes.\n"
    q = P + 'soir-classeur-D-jang-feng-v1.md'; open(q, 'w').write(t); print('classeur', sha(q))
