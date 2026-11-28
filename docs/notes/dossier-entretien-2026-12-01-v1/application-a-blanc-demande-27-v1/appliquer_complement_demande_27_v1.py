"""Applique, par programme, le complément d'erratum de la demande 27 (jumelles, renvois
orphelins, défauts A1 à A4) aux brouillons de l'application à blanc, puis vérifie le
second erratum (entrées E2-) sur ses trois cibles sans les modifier.

Lancement, depuis la racine du dépôt :
    python3 appliquer_complement_demande_27_v1.py <complément> <dossier des brouillons> <dossier de sortie>

Gardes (refus, jamais de repli silencieux) :
- chaque bloc a un identifiant unique, un ANCIEN et un NOUVEAU entre guillemets « » ;
- chaque section déclare une cible par « Cible : <chemin> » ;
- chaque ANCIEN est présent exactement une fois dans sa cible au moment de son application ;
- après remplacement, l'ANCIEN n'est plus présent, sauf s'il est contenu dans le NOUVEAU ;
- les entrées E2- ne modifient rien : leur ANCIEN doit être présent exactement une fois
  dans la pièce d'origine (pièce scellée, jamais réécrite).
Code de sortie 1 au premier échec ; aucun fichier écrit dans ce cas.
"""
import hashlib
import os
import re
import sys

BROUILLONS = {
    'programme-controle-ia-v3-application-a-blanc.md',
    'note-problematiques-programme-v2-application-a-blanc.md',
    'reponse-4-corrigee-application-a-blanc.md',
    'reponse-8-corrigee-application-a-blanc.md',
}
MOTIF_BLOC = re.compile(r'^\*\*([A-Z][A-Z0-9]*-\d+[a-z]?)\.\*\* ANCIEN : ', re.M)


class Echec(Exception):
    pass


def entre_guillemets(texte, ident, champ):
    texte = texte.strip()
    if not (texte.startswith('« ') and texte.endswith(' »')):
        raise Echec(f'{ident} : {champ} hors guillemets « »')
    return texte[2:-2]


def lire_blocs(complement):
    """Renvoie la liste ordonnée (identifiant, cible, ancien, nouveau)."""
    blocs, cible = [], None
    lignes_cible = [(m.start(), m.group(1).strip().strip('`'))
                    for m in re.finditer(r'^Cible : (.+)$', complement, re.M)]
    debuts = [(m.start(), m.group(1), m.end()) for m in MOTIF_BLOC.finditer(complement)]
    if not debuts:
        raise Echec('aucun bloc lu')
    for k, (pos, ident, fin_tete) in enumerate(debuts):
        cibles_avant = [c for p, c in lignes_cible if p < pos]
        if not cibles_avant:
            raise Echec(f'{ident} : aucune ligne « Cible : » avant le bloc')
        cible = cibles_avant[-1]
        suite = debuts[k + 1][0] if k + 1 < len(debuts) else len(complement)
        prochaine_cible = [p for p, _ in lignes_cible if pos < p < suite]
        if prochaine_cible:
            suite = prochaine_cible[0]
        corps = complement[fin_tete:suite]
        if '\nNOUVEAU : ' not in corps:
            raise Echec(f'{ident} : NOUVEAU absent')
        ancien, reste = corps.split('\nNOUVEAU : ', 1)
        if '\nRaison :' not in reste:
            raise Echec(f'{ident} : Raison absente')
        nouveau = reste.split('\nRaison :', 1)[0]
        blocs.append((ident, cible, entre_guillemets(ancien, ident, 'ANCIEN'),
                      entre_guillemets(nouveau, ident, 'NOUVEAU')))
    ids = [b[0] for b in blocs]
    doublons = sorted({i for i in ids if ids.count(i) > 1})
    if doublons:
        raise Echec(f'identifiants en double : {doublons}')
    return blocs


def appliquer(complement, dossier_brouillons, lire=None):
    """Renvoie (textes modifiés par nom de brouillon, rapport). Lève Echec au premier défaut."""
    lire = lire or (lambda p: open(p, encoding='utf-8').read())
    blocs = lire_blocs(complement)
    textes, origines, rapport = {}, {}, []
    for ident, cible, ancien, nouveau in blocs:
        nom = os.path.basename(cible)
        if ident.startswith('E2-'):
            if nom in BROUILLONS:
                raise Echec(f'{ident} : une entrée du second erratum vise un brouillon ({nom})')
            if cible not in origines:
                origines[cible] = lire(cible)
            n = origines[cible].count(ancien)
            if n != 1:
                raise Echec(f'{ident} : ANCIEN trouvé {n} fois dans {cible} (pièce scellée, non modifiée)')
            rapport.append(f'{ident} : vérifié, 1 occurrence dans {cible} (non modifiée)')
            continue
        if nom not in BROUILLONS:
            raise Echec(f'{ident} : cible inconnue {cible}')
        if nom not in textes:
            textes[nom] = lire(os.path.join(dossier_brouillons, nom))
        n = textes[nom].count(ancien)
        if n != 1:
            raise Echec(f'{ident} : ANCIEN trouvé {n} fois dans {nom} au moment de son application')
        textes[nom] = textes[nom].replace(ancien, nouveau)
        if ancien not in nouveau and ancien in textes[nom]:
            raise Echec(f'{ident} : ANCIEN encore présent après remplacement')
        rapport.append(f'{ident} : appliqué à {nom}')
    return textes, rapport


def main(argv):
    complement_chemin, dossier_brouillons, sortie = argv[1:4]
    complement = open(complement_chemin, encoding='utf-8').read()
    try:
        textes, rapport = appliquer(complement, dossier_brouillons)
    except Echec as e:
        print(f'ÉCHEC : {e}', file=sys.stderr)
        return 1
    os.makedirs(sortie, exist_ok=True)
    print(f'complément {complement_chemin} sha256 {hashlib.sha256(complement.encode()).hexdigest()}')
    print('\n'.join(rapport))
    for nom, texte in sorted(textes.items()):
        nom_sortie = nom.replace('-application-a-blanc', '-complement-applique')
        with open(os.path.join(sortie, nom_sortie), 'w', encoding='utf-8') as f:
            f.write(texte)
        print(f'{nom_sortie} sha256 {hashlib.sha256(texte.encode()).hexdigest()}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
