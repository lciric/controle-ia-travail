"""v2 : un contenu qui n'est pas un dictionnaire (texte libre) est rendu tel quel. Document de lecture pour Lazar : fiches d'une course de l'organisme, telles que produites (contenu intégral, sans nom de modèle),
fusions d'abord ; ni classement ni notes des juges ; coffre de la course jamais ouvert.
Usage : course_brute_pour_lazar_v1.py PAQUET_JSON CLE_JSON SORTIE_MD TITRE ENTETE"""
import hashlib, json, sys
paquet, cle_p, sortie, titre, entete = sys.argv[1:6]
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
s = json.load(open(paquet)); k = json.load(open(cle_p))['cle']
items = {i['item']: i['contenu'] for i in s['items']}
def ordre(sid):
    m = k[sid]
    if m['fichier'] == 'fusions-inachevees.json': return (1, sid)
    return (0 if (m.get('meta') or {}).get('origine') == 'fusion' else 2, sid)
CH = [('axe', 'Axe'), ('hypothese', 'Hypothèse'), ('prediction', 'Prédiction'), ('epreuve', 'Épreuve'), ('controle', 'Contrôle'), ('test_de_mort', 'Test de mort'), ('cout', 'Coût')]
L = [f"# {titre}", "", entete + f" Paquet sans provenance `{sha(paquet)[:16]}…`. **Brut** : ni dédoublonné, ni moissonné, ni classé ; sans nom de modèle ; sans les notes des juges ; coffre de la course jamais ouvert. Les chiffres des fiches ne sont pas vérifiés." + (f" Non fourni : {'; '.join(s['non_fourni'])}." if s['non_fourni'] else ''), ""]
G = {0: "## 1. Fusions du bisociateur", 1: "## 2. Fusions inachevées (jamais jugées en entier)", 2: "## 3. Propositions"}
cur, n = None, 0
for sid in sorted(items, key=ordre):
    g = ordre(sid)[0]
    if g != cur: L += [G[g], ""]; cur = g
    n += 1; c = items[sid]
    if not isinstance(c, dict): L += [f"### {n}. (contenu en texte libre)  ·  `{sid}`", "", str(c), ""]; continue
    autres = [x for x in c if x not in dict(CH) and x != 'titre']
    L += [f"### {n}. {c.get('titre', '(sans titre)')}  ·  `{sid}`", ""] + [f"- **{nom}** : {c[cl]}" for cl, nom in CH if c.get(cl)] + [f"- **{x}** : {c[x]}" for x in autres] + [""]
open(sortie, 'w').write('\n'.join(L) + '\n'); print(sortie, sha(sortie), n)
