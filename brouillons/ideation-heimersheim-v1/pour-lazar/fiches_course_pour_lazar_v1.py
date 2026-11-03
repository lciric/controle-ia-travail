"""Document de lecture pour Lazar : les fiches de la course de l'organisme sur la question 1 de Heimersheim, telles que la course les a
produites (contenu intégral, sans nom de modèle), fusions du bisociateur d'abord. Aucun classement, aucune note des juges."""
import hashlib, json, sys
k = json.load(open(sys.argv[1])); s = json.load(open(sys.argv[2])); sortie = sys.argv[3]; empreinte_source = sys.argv[4]
items = {i['item']: i['contenu'] for i in s['items']}
def ordre(sid):
    m = k['cles'][sid]
    if m['fichier'] == 'fusions-inachevees.json': return (1, sid)
    return (0 if m['meta'].get('origine') == 'fusion' else 2, sid)
CHAMPS = [('axe', 'Axe'), ('hypothese', 'Hypothèse'), ('prediction', 'Prédiction'), ('epreuve', 'Épreuve'), ('controle', 'Contrôle'),
          ('test_de_mort', 'Test de mort'), ('cout', 'Coût')]
L = ["# Course de l'organisme sur ta question 1 de Heimersheim — les fiches telles que la course les a produites — v1", "",
     "Course du 3 novembre 2026 (GO-2026-11-03-02, 08:31 → 09:29 UTC, code 0, 10,03 USD ; cinq espèces, une génération, deux bras du bisociateur). "
     f"Source : copie à l'octet de session-depot (liste de copie vérifiée, 0 écart), paquet préparé sans provenance (`{empreinte_source[:8]}…`). "
     "**Brut** : ni dédoublonné, ni moissonné, ni classé ; sans nom de modèle ; sans les notes des juges de la course. "
     "Une fiche de proposeur classée « à corriger » n'a de contenu nulle part dans la sortie : comptée, absente ici. "
     "Les chiffres des fiches ne sont pas vérifiés ; une fiche qui dit « pièce B.n » renvoie à la pièce servie à la course. "
     "Règle du mentor : ta réponse est écrite par toi ; ce document donne des idées, pas des phrases.", ""]
groupes = {0: "## 1. Fusions du bisociateur (7)", 1: "## 2. Fusion inachevée (classée « à corriger » par l'aiguilleur, jamais jugée)", 2: "## 3. Propositions (39)"}
courant, n = None, 0
for sid in sorted(items, key=ordre):
    g = ordre(sid)[0]
    if g != courant:
        L += [groupes[g], ""]; courant = g
    n += 1; c = items[sid]
    L += [f"### {n}. {c.get('titre', '(sans titre)')}  ·  `{sid}`", ""]
    for cle, nom in CHAMPS:
        if c.get(cle): L += [f"- **{nom}** : {c[cle]}"]
    L += [""]
open(sortie, 'w', encoding='utf-8').write('\n'.join(L))
print(n, 'fiches ;', hashlib.sha256(open(sortie, 'rb').read()).hexdigest())
