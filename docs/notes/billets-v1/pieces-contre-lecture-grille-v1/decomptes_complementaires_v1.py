"""Contre-lecture de la grille brouillon 2 : décomptes complémentaires cités dans le rapport.
Usage : python decomptes_complementaires_v1.py W SORTIE_JSON   (W contient copies-dev/, sortie de preparer_copies_neutres_v1.py
sur la moitié développement). Lit le manifeste v2 (métadonnées des deux moitiés), les deux listes de marquage, la grille,
et les copies neutres de DÉVELOPPEMENT. N'ouvre aucun texte de la tenue à l'écart. N'écrit aucun extrait de texte."""
import json, re, sys, statistics, glob, collections
W, SORTIE = sys.argv[1], sys.argv[2]
D = '/home/user/controle-ia-travail/docs/notes/billets-v1/'
man = json.load(open(D + 'manifeste-corpus-v2.json')); B = man['billets']
BORNE = "⟦FIN DE L'EN-TÊTE — 250 MOTS⟧"
table = json.load(open(f'{W}/copies-dev/cles/table-de-correspondance.json'))['neutre_vers_site']
res = {}
# 1. borne tombée dans un marqueur (crochet ouvert avant la borne)
coupes = []
for n, i in table.items():
    t = open(f'{W}/copies-dev/codeurs/billets/{n}.md', encoding='utf-8').read()
    avant = t[:t.index(BORNE)]
    if avant.count('[') != avant.count(']'):
        coupes.append({"billet": i, "marqueur": "image" if avant.rstrip().endswith('[IMAGE') else "lien ou autre"})
res["borne_dans_un_marqueur"] = {"billets": len(table), "cas": coupes}
# 2. noms affichés (manifeste seul)
def noms(b): return [n for n in [b['auteur'], *(b['coauteurs'] or [])]]
for m in ('developpement', 'tenue-a-l-ecart'):
    bb = [b for b in B if b['moitie'] == m]
    distincts = {n for b in bb for n in noms(b) if n}
    res[f"noms_affiches_{m}"] = {
        "billets": len(bb),
        "billets_avec_un_nom_en_un_seul_mot": sum(any(n and ' ' not in n.strip() for n in noms(b)) for b in bb),
        "noms_distincts_de_cinq_lettres_au_plus": sum(1 for n in distincts if len(n) <= 5),
        "noms_nuls": sum(n is None for b in bb for n in noms(b))}
# 3. écarts de population (manifeste seul)
def auc(pos, neg): return sum((a > b) + 0.5 * (a == b) for a in pos for b in neg) / (len(pos) * len(neg))
for m in ('developpement', 'tenue-a-l-ecart'):
    bn = [b for b in B if b['moitie'] == m and b['classe'] == 'bien-note']; ap = [b for b in B if b['moitie'] == m and b['classe'] != 'bien-note']
    res[f"population_{m}"] = {
        "forum_voisin_bien_notes": [sum(b['alignment_forum'] for b in bn), len(bn)], "forum_voisin_apparies": [sum(b['alignment_forum'] for b in ap), len(ap)],
        "nombre_moyen_d_auteurs_bien_notes": round(statistics.mean(len([n for n in noms(b) if n]) for b in bn), 2),
        "nombre_moyen_d_auteurs_apparies": round(statistics.mean(len([n for n in noms(b) if n]) for b in ap), 2),
        "aire_sous_la_courbe_longueur": round(auc([b['nombre_de_mots_site'] for b in bn], [b['nombre_de_mots_site'] for b in ap]), 3)}
# 4. images par billet (copies de développement)
cl = {b['identifiant']: b['classe'] for b in B}
img = {i: len(re.findall(r"\[IMAGE", open(f'{W}/copies-dev/codeurs/billets/{n}.md', encoding='utf-8').read())) for n, i in table.items()}
res["aire_sous_la_courbe_images_developpement"] = round(auc([v for i, v in img.items() if cl[i] == 'bien-note'], [v for i, v in img.items() if cl[i] != 'bien-note']), 3)
# 5. commentaires neutres de développement : réponses dans un fil
c = collections.Counter(); fichiers = 0
for p in glob.glob(f'{W}/copies-dev/codeurs/commentaires/*.json'):
    fichiers += 1
    for x in json.load(open(p))['commentaires']:
        if x['reponse_d_auteur_ne_pas_coder']: c['reponses_d_auteur'] += 1; continue
        c['codables'] += 1
        r = x['reponse_a']
        c['racines' if r is None else ('reponses_a_un_parent_non_retenu' if r == 'commentaire non retenu' else 'reponses_a_un_parent_retenu')] += 1
res["commentaires_developpement"] = {"fichiers": fichiers, **dict(c)}
# 6. marquage 1 : classes d'après le manifeste
mk = json.load(open(D + 'pieces-grille-v2/billets-marques-v1.json'))
ids = [d['identifiant'] for d in mk['marques']]; par = {b['identifiant']: b for b in B}
res["marquage_1"] = {"billets": len(ids), "bien_notes": sum(par[i]['classe'] == 'bien-note' for i in ids), "apparies": sum(par[i]['classe'] != 'bien-note' for i in ids),
                     "bien_notes_sans_apparie": sum(par[i]['classe'] == 'bien-note' and par[i]['sans_apparie'] for i in ids)}
# 7. grille : billets cités en A et B, et où figurent les identifiants de la tenue à l'écart
g = open(D + 'grille-gestes-v1-brouillon2.md', encoding='utf-8').read()
ab = g[g.index('## A. Gestes'):g.index('## 4. Protocole')]
cites = set(re.findall(r"`([A-Za-z0-9]{17})(?:/[A-Za-z0-9]{17})?`", ab))
moit = {b['identifiant']: b['moitie'] for b in B}
s6 = g[g.index('## 6. Exemples'):g.index('## 7. Vérification')]
tenue_dans_grille = {i for i in set(re.findall(r"`([A-Za-z0-9]{17})`", g)) if moit.get(i) == 'tenue-a-l-ecart'}
res["grille"] = {"billets_cites_en_A_et_B": len(cites), "dont_developpement": sum(moit.get(i) == 'developpement' for i in cites),
                 "dont_marques_du_developpement": len(cites & {'3ecs6duLmTfyra3Gp', 's7uD3tzHMvD868ehr'}),
                 "billets_de_developpement_cites_en_A": len(set(re.findall(r"`([A-Za-z0-9]{17})(?:/[A-Za-z0-9]{17})?`", g[g.index('## A. Gestes'):g.index('## B. Classes')]))),
                 "identifiants_de_la_tenue_dans_la_grille": len(tenue_dans_grille),
                 "dont_hors_section_6": len({i for i in tenue_dans_grille if i in g.replace(s6, '')})}
json.dump(res, open(SORTIE, 'w'), ensure_ascii=False, indent=1)
print(json.dumps(res, ensure_ascii=False, indent=1))
