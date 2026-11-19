import sys, difflib
sys.path.insert(0, '/home/user/controle-ia-travail/src')
from controle_ia import prereg
src = '/home/user/controle-ia-travail/brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon8.md'
t8 = open(src, encoding='utf-8').read()
ENT = 'À REMPLIR — À FIXER : tirée par la session mère au scellement'
DEBUT = '- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :'
H1 = '1' * 64; H2 = '2' * 64
L4 = ('- **Contre-lecture 4 (finale, texte rempli)** — sous-agent neuf, modèle Claude Opus 5.5, qui n\'a écrit ni ce texte, ni aucune contre-lecture antérieure de ce texte, ni la note d\'interface ; vérification de la différence du brouillon 7 au brouillon 8. '
      'Brouillon relu : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon8.md`, empreinte `' + H1 + '`. '
      'Rapport : `brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon8-v1.md`, empreinte `' + H2 + '`. '
      'Conclusion : « PRÊT : … ». **Règle** : le texte scellé ne diffère du texte relu par cette contre-lecture que par cette entrée et par la cellule « état et raison » de F-3, où seule l\'entropie tirée remplace le marqueur ; la session mère le vérifie par une comparaison faite par programme, versée avec l\'empreinte du texte scellé.')
def remplir(t, entropie=None, ligne4=None):
    if entropie is not None:
        assert t.count(ENT) == 1; t = t.replace(ENT, entropie)
    if ligne4 is not None:
        ls = t.split('\n'); idx = [i for i, l in enumerate(ls) if l.startswith(DEBUT)]
        assert len(idx) == 1; ls[idx[0]] = ligne4; t = '\n'.join(ls)
    return t
def essai(nom, t):
    p = f'{nom}.md'; open(p, 'w', encoding='utf-8').write(t)
    d = [l for l in difflib.unified_diff(t8.split('\n'), t.split('\n'), n=0, lineterm='') if l.startswith('@@')]
    print(nom, '->', prereg.problemes(p), '| blocs changés :', d)
ENTIER = '123456789012345678901234567890123456789'
essai('sain-entier-seul', remplir(t8, ENTIER, L4))
essai('sain-entier-provenance', remplir(t8, ENTIER + ' (essai : tirée une seule fois par la session mère au scellement : numpy.random.SeedSequence().entropy, numpy X.Y.Z, 2026-11-19THH:MMZ)', L4))
essai('artefact-entree4-sans-empreinte-rapport', remplir(t8, ENTIER, L4.replace(', empreinte `' + H2 + '`', '')))
essai('artefact-entropie-ouverte', remplir(t8, None, L4))
essai('artefact-entree4-meme-empreinte', remplir(t8, ENTIER, L4.replace(H2, H1)))
