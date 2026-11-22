"""Versement sur main de fichiers neufs pris sur des branches, sans lecture de contenu.
Pour chaque lot (branche, liste de chemins) : garde un fichier seulement s'il est absent de main,
si son nom ne porte aucun motif cloisonné, et si la paire (fichier, compagnon .sha256) est complète
et l'empreinte du compagnon égale à celle du blob. Écrit les blobs (git cat-file), sort un tsv."""
import hashlib, os, re, subprocess, sys
def g(*a, b=False):
    r = subprocess.run(['git', *a], capture_output=True, check=True)
    return r.stdout if b else r.stdout.decode()
MOTIFS = re.compile(r'coffre|tenu[se]?-a-l-ecart|tenus?-à-l-écart|kit|quarantaine|ne-pas-lire|ne_pas_lire|'
                    r'verite|vérité|rendu|scores|consigne-privee|conception-ii-b|archives-reponses|barreau5|'
                    r't0-6|t0\.6|etape-b|p3-bis|resultat|bras-attaque-oracle|reponses-modeles|matiere-premiere/modes-attaque', re.I)
main = set(g('ls-tree', '-r', '--name-only', 'main').split('\n'))
lignes = []
for lot in sys.argv[1:]:
    nom, ref, liste = lot.split('|', 2)
    chemins = [c for c in open(liste).read().split('\n') if c]
    arbre = set(g('ls-tree', '-r', '--name-only', ref).split('\n'))
    for c in chemins:
        if c.endswith('.sha256'):
            continue
        comp = c + '.sha256'
        if c in main or comp in main:
            idem = all(p not in main or g('rev-parse', f'main:{p}') == g('rev-parse', f'{ref}:{p}') for p in (c, comp))
            lignes.append((nom, ref, c, '', 'non versé : déjà sur main, à l\'identique' if idem else 'refusé : sur main, contenu différent')); continue
        if MOTIFS.search(c):
            lignes.append((nom, ref, c, '', 'refusé : motif cloisonné dans le nom')); continue
        if comp not in arbre:
            lignes.append((nom, ref, c, '', 'refusé : compagnon absent')); continue
        blob = g('show', f'{ref}:{c}', b=True)
        h = hashlib.sha256(blob).hexdigest()
        champs = g('show', f'{ref}:{comp}').split()
        if not champs or champs[0] != h or os.path.basename(champs[-1].lstrip('*')) != os.path.basename(c):
            lignes.append((nom, ref, c, h, 'refusé : compagnon non conforme')); continue
        for p, data in ((c, blob), (comp, g('show', f'{ref}:{comp}', b=True))):
            os.makedirs(os.path.dirname(p) or '.', exist_ok=True)
            assert not os.path.exists(p), p
            open(p, 'wb').write(data)
        lignes.append((nom, ref, c, h, 'versé, avec compagnon'))
    for c in chemins:
        if c.endswith('.sha256') and c[:-7] not in chemins:
            lignes.append((nom, ref, c, '', 'refusé : compagnon sans fichier'))
for l in lignes:
    print('\t'.join(l))
