"""Assemble pour Lazar les réponses finales (dernière version reponse-vN.md de chaque réponse), les variantes nommées, le squelette, avec compte de mots, empreinte et notes (v4).
Usage : assembler_reponses_v3.py notes.json sortie.md"""
import hashlib, json, sys, re, os, glob
D = '/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/'
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
def corps(p): return open(p).read().split('\n---\n')[0].strip()
ordre = [('kirchner-q1', 'Kirchner Q1 — un projet mené toi-même', 'aucune limite écrite'),
         ('kirchner-q2', "Kirchner Q2 — problème sous-estimé, première expérience, ce qui te ferait changer d'avis", 'aucune limite écrite'),
         ('ibrahim-q1', 'Ibrahim Q1 — première expérience', 'aucune limite écrite (visée 450)'),
         ('ibrahim-q2', 'Ibrahim Q2 — projet technique', 'aucune limite écrite'),
         ('heimersheim-q2', "Heimersheim Q2 — pourquoi l'interprétabilité mécaniste", '150 mots au plus'),
         ('scheurer', "Scheurer — proposition de tendance d'échelle", 'aucune limite écrite (visée 500)'),
         ('colognese-ward-q1', 'Colognese et Ward Q1 — une expérience de bout en bout', '200 mots au plus'),
         ('colognese-ward-q2', 'Colognese et Ward Q2 — leur billet (facultative)', 'aucune limite écrite (visée 300)'),
         ('jang-feng', 'Feng et Jang — boîte blanche : valeur et limites', 'aucune limite écrite')]
variantes = {'ibrahim-q1': ('reponse-variante-survie-v3.md', 'Variante de repli « Survie au renforcement » (vérifiée)'),
             'colognese-ward-q1': ('reponse-variante-courte-v1.md', 'Variante courte, sans la phrase sur la graine 1'),
             'jang-feng': ('reponse-v4.md', 'Variante de repli : la réponse sur l\'ancienne piste « Accumulation » (vérifiée)')}
N = json.load(open(sys.argv[1])); sortie = sys.argv[2]
L = ["# Réponses Pivotal — versions finales vérifiées — assemblage v3", ""] + [f"- {x}" for x in N.get('_tete', [])] + [""]
for slug, titre, lim in ordre:
    vs = [p for p in glob.glob(D + slug + '/reponse-v*.md') if re.search(r'/reponse-v(\d+)\.md$', p)]
    vs.sort(key=lambda p: int(re.search(r'reponse-v(\d+)\.md$', p).group(1)))
    p = vs[-1]; s = corps(p)
    L += [f"## {titre}", "", f"Fichier `{slug}/{os.path.basename(p)}` (sha256 `{sha(p)[:16]}…`) ; **{len(s.split())} mots** (découpage sur les blancs) ; limite : {lim}.", "", "---", "", s, "", "---", ""]
    L += [f"- {n}" for n in N.get(slug, [])] + [""]
    if slug in variantes:
        f, t = variantes[slug]; q = D + slug + '/' + f; v = corps(q)
        L += [f"### {t}", "", f"Fichier `{slug}/{f}` (sha256 `{sha(q)[:16]}…`) ; **{len(v.split())} mots**.", "", "---", "", v, "", "---", ""]
q = D + 'heimersheim-q1/squelette-heimersheim-q1-v2.md'
L += ["## Heimersheim Q1 — à écrire par toi (règle du mentor : aucun texte écrit par un modèle)", "", f"Squelette en français, sans phrase anglaise : `heimersheim-q1/squelette-heimersheim-q1-v2.md` (sha256 `{sha(q)[:16]}…`), envoyé à part.", ""]
L += ["## Choix des mentors", "", "Ta réponse actuelle du site (51 mots), gardée telle quelle.", ""]
L += ["## Après le dépôt (à ta décision)", ""] + [f"- {x}" for x in N.get('_apres', [])] + [""]
open(sortie, 'w').write('\n'.join(L) + '\n'); print(sortie, sha(sortie))
