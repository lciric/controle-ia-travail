"""Mentors du soir : règle gelée R-1371 (lecture R-1375) puis dossier de piste pour le rédacteur.
Score d'un groupe = somme des sommes (trois critères) de ses fiches parmi les huit comparées par paires ; égalité : meilleur rang de
Bradley-Terry, puis nombre de « ouverte » ou « voisin lointain » ; lecture de contrôle : groupe de la meilleure fiche seule.
v3 : accepte un fichier du lecteur A en dictionnaire. v2 : accepte aussi des notes rangées par identifiant (dictionnaire). Dossier : fiches complètes (lecteur A ou fiche du matin) après levée de la clé de préparation, moisson, notes, drapeaux."""
import json, hashlib, sys, glob
m, cle_p = sys.argv[1:3]
S = f'/home/claude/scratch/soir-rapport/{m}/'
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
G = json.load(open(S + 'piste/groupes-v1.json')); aff = {a['id']: a['groupe'] for a in G['affectations']}; gdef = {g['nom']: g for g in G['groupes']}
notes_raw = json.load(open(S + 'classement-D/notes-v1.json'))
if isinstance(notes_raw, dict) and isinstance(notes_raw.get('notes'), dict) and all(isinstance(v, dict) for v in notes_raw['notes'].values()):
    _l = [dict(v, id=k) for k, v in notes_raw['notes'].items()]
elif isinstance(notes_raw, dict):
    _l = notes_raw.get('fiches') if isinstance(notes_raw.get('fiches'), list) else notes_raw.get('notes') if isinstance(notes_raw.get('notes'), list) else None
    if _l is None: _l = next(v for v in notes_raw.values() if isinstance(v, list) and v and isinstance(v[0], dict) and 'id' in v[0])
else: _l = notes_raw
notes = {n['id']: n for n in _l}
bt_p = glob.glob(S + 'classement-D/bradley_terry_*_v1-sortie.json')[0]; bt = json.load(open(bt_p))
if 'ordre_final' in bt: ordre = bt['ordre_final']
else: ordre = [c['id'] for c in sorted(bt['classement'], key=lambda c: (c['rang'], c['id']))]
rang = {i: k for k, i in enumerate(ordre, 1)}
moisson = {e['id']: e for e in json.load(open(S + 'moisson-C/moisson-fusionnee-v1.json'))}
CRIT = ('originalite_verifiee', 'testable_en_jours', 'prolonge_outil_mentor', 'originalite', 'testable', 'outil_mentor', 'prolonge_un_outil_du_mentor', 'testable_en_jours_')
def notes_de(i):
    n = notes.get(i)
    if n is None: return {}
    if isinstance(n.get('notes'), dict): return {k: (v['note'] if isinstance(v, dict) else v) for k, v in n['notes'].items()}
    def val(v):
        if isinstance(v, dict): return v['note']
        if isinstance(v, (list, tuple)): return v[0]
        return v
    return {k: val(n[k]) for k in CRIT + ('outil', 'mentor') if k in n}
def drapeau(i):
    n = notes.get(i, {}); ks = [k for k in n if 'drapeau' in k or 'risque' in k]
    return n[ks[0]] if ks else ''
def somme(i):
    n = notes.get(i, {})
    if isinstance(n.get('somme'), (int, float)): return n['somme']
    return sum(notes_de(i).values())
def ouverte(i):
    e = moisson.get(i, {}); c = (e.get('classe') or '').lower(); d = (e.get('distance') or '').lower()
    return c.startswith('ouverte') or 'lointain' in d or 'lointain' in c
tab = []
for g in sorted(set(aff.values())):
    mem = [i for i, x in aff.items() if x == g]; d8 = sorted([i for i in mem if i in rang], key=lambda i: rang[i])
    tab.append(dict(groupe=g, n=len(mem), dans_les_comparees=d8, score=sum(somme(i) for i in d8), meilleur_rang=min([rang[i] for i in d8], default=99), ouvertes_ou_lointaines=sum(ouverte(i) for i in mem)))
tab.sort(key=lambda t: (-t['score'], t['meilleur_rang'], -t['ouvertes_ou_lointaines']))
meill = min((i for i in rang if i in aff), key=lambda i: rang[i])
choix = dict(tableau=tab, piste=tab[0]['groupe'], egalite_au_sommet=len(tab) > 1 and (tab[0]['score'], tab[0]['meilleur_rang']) == (tab[1]['score'], tab[1]['meilleur_rang']),
             controle_meilleure_fiche=dict(fiche=meill, groupe=aff[meill], concorde=aff[meill] == tab[0]['groupe']),
             entrees={'groupes': sha(S + 'piste/groupes-v1.json'), 'notes': sha(S + 'classement-D/notes-v1.json'), 'bt': sha(bt_p), 'moisson': sha(S + 'moisson-C/moisson-fusionnee-v1.json')})
json.dump(choix, open(S + 'piste/choix-piste-v1.json', 'w'), ensure_ascii=False, indent=1)
for t in tab: print(t)
print('PISTE :', choix['piste'], '| égalité :', choix['egalite_au_sommet'], '| contrôle :', choix['controle_meilleure_fiche'])
# dossier
cle = json.load(open(cle_p))['cle']
_lr = json.load(open(S + 'lecteur-A/fiches-normalisees-v1.json'))
_lr = _lr if isinstance(_lr, list) else (_lr.get('fiches') if isinstance(_lr.get('fiches'), list) else next(v for v in _lr.values() if isinstance(v, list)))
lect = {f['id']: f for f in _lr}
matin = {f['id']: f for f in json.load(open('/home/claude/scratch/ideation-rapport/melange-v1/fiches-classement-B-v1.json'))}
def complete(i):
    k = cle[i]; return lect.get(k['ident']) if k['source'] == 'tour' else matin.get(k['ident'])
piste = choix['piste']
L = [f"# Dossier de piste — {m} — groupe « {piste} »", "", f"Définition (groupeur aveugle) : {gdef[piste]['definition']}", "",
     f"Choix par la règle gelée : `{S}piste/choix-piste-v1.json` (sha256 `{sha(S + 'piste/choix-piste-v1.json')}`) ; contrôle : {choix['controle_meilleure_fiche']}.", ""]
mem = sorted([i for i, x in aff.items() if x == piste], key=lambda i: rang.get(i, 99))
for i in mem:
    f = complete(i) or {}; e = moisson.get(i, {})
    L += [f"## {i} (rang {rang.get(i, 'hors des comparées')}, somme {somme(i)} ; source {cle[i]['source']})", "",
          f"- Drapeau : {json.dumps(drapeau(i), ensure_ascii=False)[:500]}",
          f"- Notes : {notes_de(i)}",
          f"- Moisson : {e.get('classe')} {e.get('distance') or ''} — " + " ; ".join(f"{s.get('identifiant')} « {s.get('titre','')[:100]} » ({s.get('date','')}) : {s.get('phrase', s.get('ce_qui_differe',''))[:200]}" for s in e.get('sources', [])[:5]) + (f" — contradiction : {json.dumps(e.get('contradiction'), ensure_ascii=False)[:300]}" if e.get('contradiction') else '')]
    for k, v in f.items():
        if k in ('id', 'classement', 'statut'): continue
        L.append(f"- **{k}** : {json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v}")
    L.append("")
L += ["## Les autres fiches (une ligne chacune)", ""]
for i in sorted(aff, key=lambda i: rang.get(i, 99)):
    if i in mem: continue
    f = complete(i) or {}; L.append(f"- {i} (groupe « {aff[i]} », rang {rang.get(i, 'hors des comparées')}) : {str(f.get('enonce',''))[:240]}")
out = f'/home/claude/controle-ia-travail/brouillons/ideation-mentors-soir-v1/dossier-piste-{m}-v1.md'
open(out, 'w').write('\n'.join(L) + '\n'); print(out, sha(out), len(mem), 'fiches dans la piste')
