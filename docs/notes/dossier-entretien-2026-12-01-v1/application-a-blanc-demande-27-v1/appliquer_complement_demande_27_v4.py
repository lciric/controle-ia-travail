"""Applique, par programme, le complément d'erratum de la demande 27 (jumelles, renvois
orphelins, défauts A1 à A4) aux brouillons de l'application à blanc, puis vérifie le
second erratum (entrées E2-) sur ses trois cibles sans les modifier.

v2 : corrections de la contre-lecture Sonnet de la v1 (défauts 1 à 8).
v3 : deux mineurs de la vérification (--attendu non entier ; .tmp partiel nettoyé).
v4 : enchaînement admis pour le seul préfixe C (liste de citations construite entrée par entrée) :
     l'ANCIEN d'une entrée C absente du brouillon d'origine doit figurer dans le NOUVEAU de l'entrée
     immédiatement précédente, elle-même C et de même cible ; signalé « enchaîné » au rapport.

Lancement, depuis la racine du dépôt :
    python3 appliquer_complement_demande_27_v4.py <complément> <dossier des brouillons> <dossier de sortie> [--attendu N]

Gardes (refus, jamais de repli silencieux) :
- tout en-tête qui ressemble à un bloc (ligne contenant « ANCIEN ») est lu comme bloc, sinon refus ;
- avec --attendu N, le nombre de blocs doit valoir N ;
- préfixes admis : J, O, S, T, C, E2 ; S- et C- visent le seul programme v3 ;
- toute ligne contenant « Cible » doit suivre le motif strict « Cible : <chemin> » ;
- chaque bloc a un identifiant unique, un ANCIEN, un NOUVEAU entre « » et une Raison ;
- chaque ANCIEN est présent dans le brouillon d'origine, et exactement une fois dans sa cible
  au moment de son application ;
- après remplacement, l'ANCIEN n'est plus présent, sauf s'il est contenu dans le NOUVEAU ;
- les entrées E2- ne modifient rien : leur ANCIEN doit être présent exactement une fois dans
  la pièce d'origine (chemin relatif à la racine du dépôt) ;
- lecture impossible ou arguments manquants : « ÉCHEC », code 1 ;
- écriture atomique : tous les fichiers en .tmp, puis renommés ; rien d'écrit en cas d'échec.
"""
import hashlib
import os
import re
import sys

PROGRAMME = 'programme-controle-ia-v3-application-a-blanc.md'
BROUILLONS = {
    PROGRAMME,
    'note-problematiques-programme-v2-application-a-blanc.md',
    'reponse-4-corrigee-application-a-blanc.md',
    'reponse-8-corrigee-application-a-blanc.md',
}
PREFIXES = {'J', 'O', 'S', 'T', 'C', 'E2'}
PROGRAMME_SEUL = {'S', 'C'}
MOTIF_BLOC = re.compile(r'^\*\*([A-Z][A-Z0-9]*)-(\d+[a-z]?)\.\*\* ANCIEN : ', re.M)
MOTIF_ANCIEN_LARGE = re.compile(r'^.*\bANCIEN\b.*$', re.M)
MOTIF_CIBLE_LARGE = re.compile(r'^.*\bCible\b.*$', re.M)
MOTIF_CIBLE = re.compile(r'^Cible : `?([^`\s]+)`?$')


class Echec(Exception):
    pass


def entre_guillemets(texte, ident, champ):
    texte = texte.strip()
    if not (texte.startswith('« ') and texte.endswith(' »')):
        raise Echec(f'{ident} : {champ} hors guillemets « »')
    return texte[2:-2]


def lire_cibles(complement):
    cibles = []
    for m in MOTIF_CIBLE_LARGE.finditer(complement):
        ligne = m.group(0).strip()
        if not ligne.startswith('Cible') and 'Cible :' not in ligne:
            continue  # « Cible » dans une phrase de prose (raison, notes)
        strict = MOTIF_CIBLE.match(ligne)
        if not strict:
            raise Echec(f'ligne de cible hors motif strict « Cible : <chemin> » : {ligne[:80]}')
        cibles.append((m.start(), strict.group(1)))
    return cibles


def lire_blocs(complement, attendu=None):
    """Renvoie la liste ordonnée (identifiant, préfixe, cible, ancien, nouveau)."""
    lignes_cible = lire_cibles(complement)
    debuts = [(m.start(), m.group(1), f'{m.group(1)}-{m.group(2)}', m.end())
              for m in MOTIF_BLOC.finditer(complement)]
    if not debuts:
        raise Echec('aucun bloc lu')
    tetes_larges = [m for m in MOTIF_ANCIEN_LARGE.finditer(complement)
                    if re.match(r'^\s*\*\*', m.group(0))]
    if len(tetes_larges) != len(debuts):
        lues = {p for p, *_ in debuts}
        ignorees = [m.group(0)[:60] for m in tetes_larges if m.start() not in lues]
        raise Echec(f'{len(tetes_larges)} en-têtes de bloc, {len(debuts)} lus ; ignorés : {ignorees}')
    if attendu is not None and len(debuts) != attendu:
        raise Echec(f'{len(debuts)} blocs lus, {attendu} attendus')
    blocs = []
    for k, (pos, prefixe, ident, fin_tete) in enumerate(debuts):
        if prefixe not in PREFIXES:
            raise Echec(f'{ident} : préfixe {prefixe} hors liste {sorted(PREFIXES)}')
        cibles_avant = [c for p, c in lignes_cible if p < pos]
        if not cibles_avant:
            raise Echec(f'{ident} : aucune ligne « Cible : » avant le bloc')
        cible = cibles_avant[-1]
        suite = debuts[k + 1][0] if k + 1 < len(debuts) else len(complement)
        prochaine_cible = [p for p, _ in lignes_cible if pos < p < suite]
        if prochaine_cible:
            suite = prochaine_cible[0]
        corps = complement[fin_tete:suite]
        if corps.count('\nNOUVEAU : ') != 1:
            raise Echec(f'{ident} : {corps.count(chr(10) + "NOUVEAU : ")} lignes NOUVEAU (une attendue)')
        ancien, reste = corps.split('\nNOUVEAU : ', 1)
        if reste.count('\nRaison :') != 1:
            raise Echec(f'{ident} : {reste.count(chr(10) + "Raison :")} lignes Raison (une attendue)')
        nouveau = reste.split('\nRaison :', 1)[0]
        blocs.append((ident, prefixe, cible, entre_guillemets(ancien, ident, 'ANCIEN'),
                      entre_guillemets(nouveau, ident, 'NOUVEAU')))
    ids = [b[0] for b in blocs]
    doublons = sorted({i for i in ids if ids.count(i) > 1})
    if doublons:
        raise Echec(f'identifiants en double : {doublons}')
    return blocs


def lire_fichier(chemin):
    try:
        with open(chemin, encoding='utf-8') as f:
            return f.read()
    except OSError as e:
        raise Echec(f'lecture impossible : {chemin} ({e.__class__.__name__})')


def appliquer(complement, dossier_brouillons, lire=None, attendu=None, racine='.'):
    """Renvoie (textes modifiés par nom de brouillon, rapport). Lève Echec au premier défaut.
    Fonction pure : n'écrit rien."""
    lire = lire or lire_fichier
    blocs = lire_blocs(complement, attendu)
    textes, originaux, pieces, rapport = {}, {}, {}, []
    precedent = None  # (préfixe, nom de cible, NOUVEAU) de l'entrée appliquée juste avant
    for ident, prefixe, cible, ancien, nouveau in blocs:
        nom = os.path.basename(cible)
        if prefixe == 'E2':
            if nom in BROUILLONS:
                raise Echec(f'{ident} : une entrée du second erratum vise un brouillon ({nom})')
            chemin = os.path.join(racine, cible)
            if chemin not in pieces:
                pieces[chemin] = lire(chemin)
            n = pieces[chemin].count(ancien)
            if n != 1:
                raise Echec(f'{ident} : ANCIEN trouvé {n} fois dans {cible} (pièce scellée, non modifiée)')
            rapport.append(f'{ident} : vérifié, 1 occurrence dans {cible} (non modifiée)')
            precedent = None
            continue
        if nom not in BROUILLONS:
            raise Echec(f'{ident} : cible {cible} hors des quatre brouillons')
        if prefixe in PROGRAMME_SEUL and nom != PROGRAMME:
            raise Echec(f'{ident} : le préfixe {prefixe} ne vise que le programme v3, pas {nom}')
        if nom not in textes:
            textes[nom] = originaux[nom] = lire(os.path.join(dossier_brouillons, nom))
        enchaine = False
        if ancien not in originaux[nom]:
            enchaine = (prefixe == 'C' and precedent is not None and precedent[0] == 'C'
                        and precedent[1] == nom and ancien in precedent[2])
            if not enchaine:
                raise Echec(f'{ident} : ANCIEN absent du brouillon d\'origine {nom} (texte inséré par une entrée précédente ?)')
        n = textes[nom].count(ancien)
        if n != 1:
            raise Echec(f'{ident} : ANCIEN trouvé {n} fois dans {nom} au moment de son application')
        textes[nom] = textes[nom].replace(ancien, nouveau)
        if ancien not in nouveau and ancien in textes[nom]:
            raise Echec(f'{ident} : ANCIEN encore présent après remplacement')
        rapport.append(f'{ident} : appliqué à {nom}' + (' (enchaîné sur l\'entrée précédente)' if enchaine else ''))
        precedent = (prefixe, nom, nouveau)
    return textes, rapport


def ecrire_atomique(textes, sortie):
    os.makedirs(sortie, exist_ok=True)
    temporaires = []
    try:
        for nom, texte in sorted(textes.items()):
            final = os.path.join(sortie, nom.replace('-application-a-blanc', '-complement-applique'))
            temporaires.append((final + '.tmp', final))
            with open(final + '.tmp', 'w', encoding='utf-8') as f:
                f.write(texte)
    except OSError:
        for tmp, _ in temporaires:
            if os.path.exists(tmp):
                os.remove(tmp)
        raise
    for tmp, final in temporaires:
        os.replace(tmp, final)
    return [final for _, final in temporaires]


def main(argv):
    args = [a for a in argv[1:] if not a.startswith('--attendu')]
    attendu = None
    for a in argv[1:]:
        if a.startswith('--attendu='):
            try:
                attendu = int(a.split('=', 1)[1])
            except ValueError:
                print(f'ÉCHEC : --attendu non entier : {a}', file=sys.stderr)
                return 1
    if len(args) != 3:
        print('ÉCHEC : usage : <complément> <dossier des brouillons> <dossier de sortie> [--attendu=N]', file=sys.stderr)
        return 1
    complement_chemin, dossier_brouillons, sortie = args
    try:
        complement = lire_fichier(complement_chemin)
        textes, rapport = appliquer(complement, dossier_brouillons, attendu=attendu)
    except Echec as e:
        print(f'ÉCHEC : {e}', file=sys.stderr)
        return 1
    print(f'complément {complement_chemin} sha256 {hashlib.sha256(complement.encode()).hexdigest()}')
    print('\n'.join(rapport))
    for chemin in ecrire_atomique(textes, sortie):
        texte = lire_fichier(chemin)
        print(f'{os.path.basename(chemin)} sha256 {hashlib.sha256(texte.encode()).hexdigest()}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
