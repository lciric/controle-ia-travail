# v2 : le registre suit le numéro de version de la réponse (la v1 désignait toujours le registre v1).
"""Fabrique et écrit les deux consignes de vérification (chiffres, lecteur-mentor) d'une réponse rédigée."""
import hashlib, sys
R = '/home/claude/controle-ia-travail/'; P = R + 'brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/'
def h(p): return hashlib.sha256(open(p if p.startswith('/') else R + p, 'rb').read()).hexdigest()
slug, version, mentor, lignes_q, limite, rapport, extra = sys.argv[1:8]
d = f'brouillons/redaction-finale-v1/{slug}/'
rep = d + f'reponse-v{version}.md'; reg = d + f'registre-affirmations-v{version}.md'
V = open(P + 'verification-chiffres-gabarit-v1.md').read(); L = open(P + 'lecteur-mentor-gabarit-v1.md').read()
c = lambda t: t.replace('<<MENTOR>>', mentor).replace('<<LIGNES_QUESTION>>', lignes_q).replace('<<LIMITE>>', limite).replace('<<RAPPORT>>', rapport)
v = c(V).replace('<<REPONSE>>', R + rep).replace('<<H_REPONSE>>', h(rep)).replace('<<REGISTRE>>', R + reg).replace('<<H_REGISTRE>>', h(reg)).replace('<<SORTIE>>', R + d + f'verification-chiffres-v{version}.md')
l = c(L).replace('<<REPONSE>>', R + rep).replace('<<H_REPONSE>>', h(rep)).replace('<<SORTIE>>', R + d + f'lecture-mentor-v{version}.md')
if extra: v += "\n## Ajout (directeur)\n" + extra + "\n"; l += "\n## Ajout (directeur)\n" + extra + "\n"
v += "\n**N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le. Toute commande : `timeout 60 nice -n 10 …`.\n"
l += "\n**N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le. Toute commande : `timeout 60 nice -n 10 …`.\n"
for nom, t in ((f'verification-chiffres-{slug}-v{version}.md', v), (f'lecteur-mentor-{slug}-v{version}.md', l)):
    assert '<<' not in t, nom
    open(P + nom, 'w').write(t); print(P + nom, hashlib.sha256(t.encode()).hexdigest())
