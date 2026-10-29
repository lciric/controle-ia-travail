#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Annexe A de la table de dépendance « critères de G0 -> travaux », v7 (dernière version avant soumission à Lazar).

Usage (toujours `python3 -I`) ; D = la table, V1 = la table v1, DEC = fichiers de décisions séparés par des virgules :
  verifier   D V1 DEC [SY]          texte gelé (sections, règles, § 9, sources, GO, travail, producteurs, dates et heures),
                                    § 0, registre des décisions (mot DIRECT de Lazar contrôlé), résumé = § 9 = registre,
                                    cas du § 6.7, recalcul de chaque ligne dérivée comparée une à une ; imprime les R-nnn
                                    cités et l'empreinte de chaque fichier de DEC ;
                                    avec SY (synthèse du collisionneur) : la clause du § 0 est comparée mot pour mot à SY § 5
  artefact   D V1 DEC               R5 : une copie altérée doit faire échouer `verifier`
  feuille    D V1 DEC "A=..;G=..;V=..;C=..;abs=..;val=..;plaf=oui|non;plafV1=oui|non[;pres=..][;gel=..]"
                                    appelle `verifier`, puis REFUSE si la table ou ce script n'a pas de compagnon .sha256
                                    conforme, ou si une décision du registre (§ 9) est « en attente » ; aucune option par défaut ;
                                    une décision ne vaut que si elle cite une ligne de registres/decisions.md qui est un mot
                                    direct de Lazar (motif, identifiant, option ; aucune marque de relevé hors guillemets)
  simuler    D V1 DEC "A=..;...;d0b=..;d1=..;d2=..;d3=..;d4=..;d5=..;d6=..;d7=.."
                                    même calcul, décisions passées EN ARGUMENT (toutes exigées) ; imprime « SIMULATION » :
                                    ce n'est pas une feuille de repli
  tester     D V1 DEC DEPOT [P-X=chemin+chemin,...]   T1, T2 (par controle_ia.scellement du dépôt), T4 ; imprime abs=
  constat    D V1 DEC FICHIER "A=..;V=..;C=.."   format fermé du constat du 31 décembre ; mêmes refus que `feuille`
  calculer   D V1 DEC               imprime les cellules dérivées et les constantes à geler
  essais     D V1 DEC [DEPOT|-] [SY]  R5 : altérations (v5, contre-lectures de la v5 et de la v6, neuves), refus (dont
                                    mots de Lazar mal fondés : R-521 réelle refusée, ligne factice au bon format acceptée),
                                    constat, tester
  sources    D DEPOT                recalcule l'empreinte de chaque source de la table des sources (lignes `S:`)
  aveugle    D                      imprime les lignes sans classe ni produit, pour une classification à l'aveugle
  concordance D FICHIER             compare des réponses « Wxx classe produits sert » à la table
Aucun repli silencieux : toute anomalie lève une erreur et un code de sortie non nul.
"""
import glob, hashlib, os, re, shutil, sys, tempfile


class Echec(Exception):
    pass


def exige(c, m):
    if not c:
        raise Echec(str(m))


cells = lambda l: [c.strip() for c in l.strip().strip('|').split('|')]
ks = lambda t: set(map(int, re.findall(r'\d', t)))
fmt = lambda s: ', '.join(sorted(s)) or 'aucune'
NOM = r'P-[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*'
MARQUES = '†‡°'
TYPES = ('verdict', 'lecture', 'prereg', 'autre')
CLES_ETAT = {'abs', 'A', 'G', 'V', 'C', 'pres', 'gel', 'val', 'plaf', 'plafV1'}
EMPREINTE_SCRIPT = lambda: hashlib.sha256(open(__file__, 'rb').read()).hexdigest()
sha_txt = lambda t: hashlib.sha256(t.encode('utf-8')).hexdigest()

# ---------------------------------------------------------------- registre des décisions (§ 9) : aucune option par défaut
DECISIONS = {  # identifiant -> (clé d'argument, options admises, recommandation)
    'D:0b': ('d0b', ('absent', 'négatif'), 'absent'),
    'D:1': ('d1', ('a', 'b', 'c'), 'a'),
    'D:2': ('d2', ('a', 'b', 'c'), 'b'),
    'D:3': ('d3', ('1', '2', '3'), '1'),
    'D:4': ('d4', ('a', 'b', 'c'), 'a'),
    'D:5': ('d5', ('a', 'b', 'c'), 'c'),
    'D:6': ('d6', ('a', 'b'), 'a'),
    'D:7': ('d7', ('garder', 'retirer'), 'garder'),
}
CLES_DEC = {v[0] for v in DECISIONS.values()}
# sens de chaque recommandation pour la porte (résumé et § 9 doivent l'écrire à l'identique)
SENS = {'D:0b': 'ouvre', 'D:1': 'ferme', 'D:2': 'ouvre', 'D:3': 'ferme', 'D:4': 'ferme', 'D:5': 'mixte', 'D:6': 'ouvre', 'D:7': 'ferme'}
# Mot DIRECT de Lazar (CT6-07) : motif exigé hors guillemets dans la ligne citée de registres/decisions.md
MOT_DIRECT = re.compile(r'Lazar \([^()«»]*heure de Paris, mots? directs?\b|[Mm]ots directs de Lazar\b')
MARQUES_RELEVE = ('version soumise', 'décisions attendues', 'recommandation')  # ligne de relevé de session : refusée
REGISTRE_LAZAR = 'registres/decisions.md'
# expressions plus fortes que la table, interdites dans le résumé (CT6-04 ; liste partielle, la contre-lecture reste juge)
INTERDITS_RESUME = ('garanti', 'reste atteignable', 'par défaut', 'défaut sous 48', 'lit les résultats', 'ne lit aucun résultat.',
                    'produit la feuille même', 'reprise avant la borne')
RENVOI_S9 = 'détail, appuis et options complètes : **§ 9**'  # renvoi exigé dans le résumé (CT6-03)
CAS_67 = ('i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x', 'xi', 'xii', 'xiii')  # cas du § 6.7, dans l'ordre
D7_LIGNES = ('W19', 'W33')  # arêtes † vers P-T04 posées hors de la borne du § 2 (D:7)
SC_HYP = 'd0b=absent;d1=a;d2=b;d3=1;d4=a;d5=c;d6=a;d7=garder'  # hypothèse d'illustration des scénarios (§ 5), non une décision

# ---------------------------------------------------------------- constantes gelées avec la table
CLAUSE_SY_SHA = 'd6d8e154d6bdcbc2fb35242c325aff54d357046e5cf4c8a8655c839b82469758'
CLAUSE_APPLIQUEE_SHA = '86cc7e2a3366ef8ad3d4c96bea425adc479974e875e4a7e156e77a208613a307'
CLAUSE_MOTS = 168
CITATION_R765 = ("gèle-t-il seulement ce critère jusqu'au second verdict (le troisième modèle, et les deux avis "
                 "indépendants de Fable et de conv-audit) : go")
MARQUES_CLAUSE = ('[R-765]', '[D:0b, en attente du mot de Lazar]', '« non tenu — absent » (recommandation)',
                  '[plafond non fixé ; D:3]', "[D:1 pour l'arrêt de la lecture]")
# Toutes les dates ET heures du texte, dans l'ordre : une date ou une heure changée arrête `verifier`.
DATES_HEURES = '23:33|30 novembre 2026|31 janvier 2027|30 novembre|31 janvier|30 novembre|24 janvier|31 janvier|23:59|7 février|1er novembre|15 novembre|25 novembre|31 décembre|23:59:59|1er janvier|00:00|2026-10-29|23:40:59|23:33|2026-10-29|2026-10-29|30 novembre 2026|23:59|31 janvier 2027|23:59|30 novembre|11:03|30 novembre|31 janvier 2027|23:59|30 novembre 2026|23:59|31 janvier 2027|23:59|30 novembre|31 décembre|24 janvier|31 décembre|31 décembre|2026-10-17|30 novembre|29 octobre|30 novembre|31 décembre 2026|31 décembre 2026|23:59:59|31 décembre 2026|00:00|29 octobre|2026-10-29|2026-11-05|2026-10-29|2026-11-05|2026-10-29|2026-11-05|2026-10-29|2026-10-29|16:45|2026-10-29|2026-11-05|2026-10-29|2026-11-05|2026-10-29|2026-11-05|2026-10-29|2026-11-05|2026-10-29|2026-11-05|2026-10-29|2026-11-05|5 novembre 2026|30 novembre|29 octobre|29 octobre|2026-10-29|2026-10-24|30 novembre|31 janvier 2027|23:59|29 octobre|7 février 2027|23:59|30 novembre|29 octobre|29 octobre|29 octobre|29 octobre|29 octobre|29 octobre|29 octobre|24 janvier|29 octobre|29 octobre|29 octobre|15 novembre|29 octobre|5 novembre|29 octobre|30 novembre|31 janvier|30 novembre|31 janvier 2027|23:59|24 janvier|24 janvier 2027|23:59|24 janvier|31 janvier 2027|23:59|24 janvier|24 janvier|31 janvier 2027|23:59|7 février 2027|23:59|1er novembre 2026|23:59|15 novembre 2026|23:59|25 novembre 2026|23:59|29 octobre|31 décembre|31 décembre|31 décembre 2026|23:59:59|1er janvier|31 décembre 2026|00:00|30 novembre|31 décembre|29 octobre|2026-10-29|23:57:35'
RE_DATE_HEURE = re.compile(r'\b\d{1,2}(?:er)? (?:janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre)'
                           r'(?: \d{4})?|\b20\d\d-\d\d-\d\d\b|\b\d{1,2}:\d\d(?::\d\d)?\b')
CHEMINS = {
    'P-T04': 'docs/verdicts/verdict-T0.4-critere-1-G0-v*.md',
    'P-V6': 'docs/verdicts/verdict-T0.6-critere-2-G0-v*.md',
    'P-L7': 'docs/verdicts/verdict-T0.7-critere-3-G0-v*.md',
    'P-B4': 'docs/verdicts/verdict-T0.8-critere-4-G0-v*.md',
    'P-T03': 'diag/*-t03/lecture.json diag/*-t03/lecture.md',
    'P-G1': 'prereg/G1-*-v*.md',
    'P-C': 'prereg/papier-C-*-v*.md',
    'P-EA': ('docs/etat-de-l-art/etat-de-l-art-verifie-niveau1-v*.md docs/etat-de-l-art/etat-de-l-art-verifie-niveau2-v*.md '
             'docs/etat-de-l-art/table-des-chiffres-v*.md docs/etat-de-l-art/controle-tracabilite-v*.md'),
    'P-EAV': ('docs/etat-de-l-art/etat-de-l-art-verifie-niveau1-v*.md docs/etat-de-l-art/etat-de-l-art-verifie-niveau2-v*.md '
              'docs/etat-de-l-art/table-des-chiffres-v*.md'),
    'P-6a': 'prereg/T0.6-etape1-*-v*.md',
    'P-6a-res': 'nommé par P-6a',
    'P-6': 'prereg/T0.6-decisif-*-v*.md',
    'P-7': 'prereg/T0.7-*-v*.md',
    'P-8': 'prereg/T0.8-*-v*.md',
    'P-EP': 'nommé par P-6',
    'P-LST': 'nommé par P-7',
    'P-P4': 'docs/verdicts/verdict-P4-instrument-v*.md',
    'P-NM': 'docs/notes/note-mathematique-lemme-theoreme-v*.md',
    'P-PIL': 'nommé par P-ARR',
    'P-ARR': 'prereg/couche2-pilote-*-v*.md',
}
PRODUCTEURS = {  # producteur(s) de chaque produit : un changement, même cohérent dans les deux tables, arrête `verifier`
    'P-T04': 'W10', 'P-V6': 'W41', 'P-L7': 'W16', 'P-B4': 'W19', 'P-T03': 'W09', 'P-G1': 'W21', 'P-C': 'W25',
    'P-EA': 'W04, W05, W06', 'P-EAV': 'W04', 'P-6a': 'W13', 'P-6a-res': 'W14', 'P-6': 'W50', 'P-7': 'W40', 'P-8': 'W18',
    'P-EP': 'W41', 'P-LST': 'W16', 'P-P4': 'W12', 'P-NM': 'W08', 'P-PIL': 'W23', 'P-ARR': 'W42',
}
GO_TABLE = [  # § 6.5 (i), lu dans S:GO
    ('GO-2026-10-29-08', '50 USD (Claude), enveloppe 60 USD', '2026-11-05'),
    ('GO-2026-10-29-09', 'enveloppe 63 USD', '2026-11-05'),
    ('GO-2026-10-29-10', '11,8 USD', '2026-11-05'),
    ('GO-2026-10-29-11', '« sans plafond fixé par Lazar » (plafond prudentiel de session-depot : 300 USD)',
     '2026-10-29 (fin de l\'autonomie ≈ 16:45 UTC)'),
    ('GO-2026-10-29-12', '5 USD', '2026-11-05'),
    ('GO-2026-10-29-13', 'enveloppe 78 USD', '2026-11-05'),
    ('GO-2026-10-29-14', '6 USD', '2026-11-05'),
    ('GO-2026-10-29-15', '30 USD', '2026-11-05'),
    ('GO-2026-10-29-16', '2 USD', '2026-11-05'),
    ('GO-2026-10-29-17', '6 USD', '2026-11-05'),
]
TRAVAIL_SHA = '38ce6e4771cb13afaad5bcbefde1b140f4d762397dced931d337d49b835885cf'     # colonne « travail » des lignes W
SOURCES_SHA = '981d8488b3e649aa56c6834fd8810f96b3a2dab43caf21b0aef9af9988544ebe'     # table des sources (lignes S:)
DECISIONS_SHA = '48fe7d64c3d2877a57df83105b2d6a900d87f3675bbb38543f43515964751d83'   # registre des décisions, sans la colonne « mot de Lazar »
REGLES_SHA = 'eeddc4748b5db4dc0242ecfd8761acfea4af35ab57729b2b3eb3eb4139b98df2'      # paragraphe des règles L0 à L14 (§ 5)
S9_SHA = 'fef81b9f7a5b63d183a420f174ff1c3423cb45808e81e5f868cddb1b9acc919e'          # § 9 entier, normalisé
SECTIONS = {'(tête)': 'ad194e9261d542bbd5eafa0e7da8bf9b9168dd9a0ffacb726f151f56b54cd326', 'Résumé pour Lazar (une page)': '8898e307f92b8b29c1c632efffdcbbb4d68cab225ddf04fda303cfd635e9e2e9', 'Déclaration, empreintes, sources': 'a1a47e091c21eeb65ac9a24b7a35d320d1351b554de704e82ef9677cf1bbc343', '0. Clause de repli de référence (la clause prime ; si la clause scellée diffère, la table est à refaire)': '286edd40701bb980c94be71e4684dd70c875adcfadcc0f9504dd0bb18839b479', '1. Constats de la contre-lecture de la v6 → traitement': 'befa40ff8ee531730575caecbdd82ae0e8d90fb945c3f97f4a7e5c285a337b69', '2. Définitions (mécaniques ; aucun jugement après V1)': '275c1b9a0e9c40964cd9449a47214be43d9802b8c20677b2dd3ccee05653f549', "3. Produits (producteur ; lignes K fermées si le produit est absent ou, pour ‡, présent sans la classe « établi » — calculé par l'annexe A)": '8a3df65823ebd7e833e222815199fe5cbd800cddc346120b863b458055e893dd', '4. Table des travaux': '52bc43b13c7e1f708c2bde2e9b41845a031691753823a6080253bf2ad6aeae30', '5. Règle de lecture mécanique (option (b) verrouillée, R-470 ; gel selon R-765)': '5f6a673a09806df5b01f830194e6dcb2d1a049a090bf0dc554a854ff42afbbe2', '6. Application': 'd7d282254233188c4cf3e1cdab8ae9ce4757b799a0d8cbe1f310405ab06649a7', "7. Audit de symétrie R4 (recompté par l'annexe A)": '2a753a3956790c5670f7b36ac70e7c034cca60fa1e0d4b8de5ae6cd9682769ec', '8. Points ouverts (signalés, non masqués)': 'a7d044ecf59933dd762dfbe72e80b6c5f1938f916eee14c3138a20cf97a00cc3', '9. Décisions pour Lazar': 'fef81b9f7a5b63d183a420f174ff1c3423cb45808e81e5f868cddb1b9acc919e', 'Annexe A — script de vérification (fichier séparé)': 'b46b49e8927655bd213ba95a6cd75b51410595ee32446d24542f5db3e626e4c0'}                  # empreinte de chaque section, texte normalisé (rempli par `calculer`)


# ---------------------------------------------------------------- normalisation et sections
def norm(texte):
    """Texte normalisé : l'empreinte de ce script et la colonne « mot de Lazar » du registre sont remplacées."""
    t = re.sub(r'(annexe-A-verif-v1\.py` \(`sha256sum` : `)[0-9a-f]{64}(`)', r'\1<SCRIPT>\2', texte.replace(EMPREINTE_SCRIPT(), '<SCRIPT>'))
    out = []
    for l in t.split('\n'):
        if l.startswith('| D:'):
            c = cells(l)
            l = '| ' + ' | '.join(c[:-1] + ['<MOT>']) + ' |'
        out.append(l)
    return '\n'.join(out)


def sections(texte):
    s = {}; cur = '(tête)'; buf = []
    for l in norm(texte).split('\n'):
        if l.startswith('## '):
            s[cur] = '\n'.join(buf); cur = l[3:].strip(); buf = []
        buf.append(l)
    s[cur] = '\n'.join(buf)
    return {k: sha_txt(v) for k, v in s.items()}


def section_texte(texte, debut):
    L = norm(texte).split('\n'); i = next((j for j, l in enumerate(L) if l.startswith('## ' + debut)), None)
    exige(i is not None, ('section introuvable', debut))
    j = next((k for k in range(i + 1, len(L)) if L[k].startswith('## ')), len(L))
    return '\n'.join(L[i:j])


def regles(texte):
    L = [l for l in texte.split('\n') if l.startswith('**L0 (applicabilité)**')]
    exige(len(L) == 1, ('§ 5 : paragraphe des règles L0 à L14 introuvable ou dupliqué', len(L)))
    return L[0]


# ---------------------------------------------------------------- lecture de la table
def prods(cell):
    """Liste de (nom, †, ‡, °)."""
    if cell.strip() == '—':
        return []
    r = []
    for x in cell.split(','):
        x = x.strip(); n = x.rstrip(MARQUES); m = x[len(n):]
        exige(re.fullmatch(NOM, n), ('produit mal formé', x))
        exige(set(m) <= set(MARQUES), ('marque inconnue', x))
        r.append((n, '†' in m, '‡' in m, '°' in m))
    return r


pr = lambda w: [q[0] for q in prods(w['prod'])]
ets = lambda w: {q[0] for q in prods(w['prod']) if q[2]}
bas = lambda w: {q[0] for q in prods(w['prod']) if q[3]}


def fourn(w):
    return [] if w['four'] == '—' else [x.strip() for x in w['four'].split(',')]


def tab(texte, pre, n):
    r = [cells(l) for l in texte.splitlines() if l.startswith(pre)]
    exige(r, 'table absente ' + pre)
    for c in r:
        exige(len(c) == n, ('colonnes', c[0], len(c), n))
    return r


def producteurs(t):
    if t == '—':
        return set()
    L = [x.strip() for x in t.split(',')]
    exige(all(re.fullmatch(r'W\d\d', x) for x in L), ('producteur mal formé', t))
    return set(L)


def charge(texte):
    W = [dict(zip(('ref', 'trav', 'prod', 'four', 'sert', 'cl', 'src'), c)) for c in tab(texte, '| W', 7)]
    P = {}
    for c in tab(texte, '| P-', 8):
        exige(c[0] not in P, ('produit en double', c[0]))
        P[c[0]] = dict(k=int(c[1]) if c[1].isdigit() else 0, typ=c[2], pro=producteurs(c[3]), pro_txt=c[3], cls=c[4], chem=c[5])
    return W, P


def classe(w):
    s = w['src']
    if re.search(r'\bd1\b|\bd2\b|préalable|\[GEL-SY\]', s):
        return 'F'
    if '[H]' in s:
        return 'H'
    if w['prod'] != '—':
        return 'K'
    return 'R' if '[REJEU]' in s else 'I'


def kprod(P):
    return {v['k']: p for p, v in P.items() if v['k']}


def cvk(P, d4):
    """L14 : critères dont le produit a une classe lue, selon D:4."""
    exige(d4 != 'b', 'D:4 = (b) : la table n\'est pas applicable (L14 : ‡ et L2bis exigent une classe lue)')
    K = sorted(v['k'] for v in P.values() if v['k'] and v['cls'] == 'oui')
    return [k for k in K if k == 2] if d4 == 'c' else K


# ---------------------------------------------------------------- règles de lecture
def requis(w, E):
    """Produits exigés par la ligne : L11 (D:3) pour les produits °, L13 (D:7) pour W19 et W33."""
    r = []
    for n in pr(w):
        if n in bas(w) and (E['d3'] == '2' or (E['d3'] == '3' and not E['plafV1'])):
            continue
        if n == 'P-T04' and w['ref'] in D7_LIGNES and E['d7'] == 'retirer':
            continue
        r.append(n)
    return r


def heritiers(W, P, X0, ab, E):
    """L9 : producteurs, sans « sert », des produits auxiliaires absents requis (de proche en proche) par les lignes visées."""
    by = {w['ref']: w for w in W}
    need = set(); todo = [by[r] for r in X0 if r in by]
    while todo:
        x = todo.pop()
        for p in requis(x, E):
            if p in ab and P[p]['k'] == 0:
                for q in sorted(P[p]['pro']):
                    if q in by and q not in need:
                        need.add(q); todo.append(by[q])
    return {r for r in need if by[r]['sert'] == '—' and by[r]['cl'] in 'KI'}


def analyser(W, P, E):
    """Retourne {réf: (état, motif, droit de devis)}, G', A'."""
    ab, val = E['ab'], E['val']
    G = set(E['Geff']) | set(E['gel']) | {k for k, v in val.items() if v == 'négatif'}
    Ap = (set(E['Aeff']) - set(E['pres'])) - G
    X0 = {w['ref'] for w in W if w['cl'] in 'KIR' and ks(w['sert']) & Ap and not ks(w['sert']) & G}
    heirs = heritiers(W, P, X0, ab, E)
    st = {}
    for w in W:
        s = ks(w['sert']); c = w['cl']; a = sorted(set(requis(w, E)) & ab)
        ne = sorted(n for n in ets(w) if n not in ab and val.get(P[n]['k']) != 'établi')
        if c == 'F': e, m = 'fermée', 'L1'
        elif c == 'H': e, m = 'Lazar', 'L6'
        elif s & G: e, m = 'fermée', 'L2 gel %s' % sorted(s & G)
        elif c == 'K' and a: e, m = 'fermée', 'L3 absent %s' % a
        elif c == 'K' and ne: e, m = 'fermée', 'L3 non établi %s' % ne
        elif c == 'R' and not s & Ap: e, m = 'fermée', 'L4 hors A'
        else: e, m = 'ouverte', 'L3' if c == 'K' else 'L4'
        # § 6.5 (ii) : sans plafond fixé à l'étape, aucun devis ne passe, donc aucun droit de devis
        st[w['ref']] = (e, m, E['plaf'] and e == 'ouverte' and (bool(s & Ap) or w['ref'] in heirs))
    return st, G, Ap


# ---------------------------------------------------------------- arguments
def lire_spec(s, cles):
    d = {}
    for x in filter(None, s.split(';')):
        exige('=' in x, ('argument sans =', x))
        k, v = x.split('=', 1)
        exige(k not in d, ('clé en double', k))
        d[k] = v
    if CLES_DEC & set(d) and not CLES_DEC <= cles:
        raise Echec(('décision passée en argument : refusée ; les décisions viennent du registre du § 9 (mots de Lazar)', sorted(CLES_DEC & set(d))))
    exige(set(d) <= cles, ('clé inconnue', sorted(set(d) - cles)))
    return d


def ensemble(t, nom):
    if not t.strip():
        return set()
    L = [x.strip() for x in t.split(',')]
    exige(all(re.fullmatch(r'[1-8]', x) for x in L), (nom, 'critère hors 1..8', t))
    exige(len(set(L)) == len(L), (nom, 'doublon', t))
    return set(map(int, L))


def produits(t, P):
    if not t.strip():
        return set()
    L = [x.strip() for x in t.split(',')]
    exige(len(set(L)) == len(L), ('abs : doublon', t))
    for x in L:
        exige(x in P, ('produit inexistant', x))
    return set(L)


def oui_non(d, k):
    v = d.get(k, 'oui')
    exige(v in ('oui', 'non'), (k, 'oui ou non attendu', v))
    return v == 'oui'


def valider_decisions(dec):
    """dec : {clé d'argument: option} ; chaque décision exigée, option admise."""
    for i, (cle, opts, _) in DECISIONS.items():
        exige(cle in dec, ('décision manquante (aucune option par défaut)', i))
        exige(dec[cle] in opts, ('option non admise', i, dec[cle], opts))
    return dec


def evaluer(W, P, s, mode, decisions=None):
    """mode : 'feuille' (décisions du registre), 'simuler' (décisions en argument), 'scenario' (hypothèse d'illustration)."""
    d = lire_spec(s, CLES_ETAT | (CLES_DEC if mode != 'feuille' else set()))
    if mode == 'feuille':
        dec = dict(decisions)
    elif mode == 'simuler':
        dec = {k: d.pop(k) for k in list(d) if k in CLES_DEC}
    else:
        dec = dict(x.split('=', 1) for x in SC_HYP.split(';')); dec.update({k: d.pop(k) for k in list(d) if k in CLES_DEC})
    valider_decisions(dec)
    strict = mode != 'scenario'
    if strict:
        manque = {'A', 'G', 'V', 'C', 'abs', 'val', 'plaf', 'plafV1'} - set(d)
        exige(not manque, ('arguments manquants', sorted(manque)))
    A, G1, V, C = (ensemble(d.get(x, ''), x) for x in 'AGVC')
    S4 = {'A': A, 'G': G1, 'V': V, 'C': C}
    for x, y in (('A', 'G'), ('A', 'V'), ('A', 'C'), ('G', 'V'), ('G', 'C'), ('V', 'C')):
        exige(not (S4[x] & S4[y]), ('états de V1 non disjoints', x, y))
    # L8 (D:5)
    Aeff = A | ((V | C) if dec['d5'] == 'b' else set()) | (C if dec['d5'] == 'c' else set())
    Geff = G1 | (V if dec['d5'] == 'c' else set())
    pres = ensemble(d.get('pres', ''), 'pres'); exige(pres <= Aeff, ('pres hors de A (L8 compris)', sorted(pres - Aeff)))
    gel = ensemble(d.get('gel', ''), 'gel')
    plaf, plafV1 = oui_non(d, 'plaf'), oui_non(d, 'plafV1')
    exige(plaf or not plafV1, ('plafV1=oui et plaf=non : un plafond fixé à V1 ne se défait pas',))
    ab = produits(d.get('abs', ''), P)
    # L12 (D:0b)
    if dec['d0b'] == 'négatif':
        for k, p in ((2, 'P-6'), (3, 'P-7'), (4, 'P-8')):
            exige(not (k in A and p in ab), ('L12 (D:0b = négatif) : critère %d dans A sans préenregistrement (%s absent) : V1 devait le ranger dans G' % (k, p),))
    kp = kprod(P); K = cvk(P, dec['d4']); val = {}
    for x in filter(None, d.get('val', '').split(',')):
        exige(re.fullmatch(r'[1-8]:(établi|négatif|autre)', x.strip()), ('val mal formée', x))
        k = int(x.strip()[0]); exige(k not in val, ('val : doublon', k))
        exige(k in K, ('val : critère sans classe lue (L14, D:4 = %s)' % dec['d4'], k))
        exige(kp[k] not in ab, ('val : produit absent, aucune classe à lire', kp[k]))
        val[k] = x.strip().split(':')[1]
    for k in K:
        if kp[k] not in ab and k not in val:
            exige(not strict, ('val manquante : produit présent, classe à copier', k, kp[k]))
            val[k] = 'négatif' if k in Geff else 'établi'
    E = dict(ab=ab, val=val, G1=G1, A=A, V=V, C=C, Aeff=Aeff, Geff=Geff, pres=pres, gel=gel, plaf=plaf, plafV1=plafV1)
    E.update(dec)
    return E


def scenario(W, P, s):
    E = evaluer(W, P, s, 'scenario')
    st, G, Ap = analyser(W, P, E)
    by = {w['ref']: w for w in W}
    f23 = {r for r, (e, m, d) in st.items() if m.startswith(('L2', 'L3 ')) and e == 'fermée'}
    ro = {r for r, (e, m, d) in st.items() if by[r]['cl'] == 'R' and e == 'ouverte'}
    dv = {r for r, (e, m, d) in st.items() if d}
    return [fmt(f23), fmt(ro), fmt(dv)]


SC = ['abs=P-V6,P-L7;G=;A=2,3',
      'abs=P-7,P-8;G=;A=2',
      'abs=P-PIL;G=;A=6',
      'abs=P-PIL;G=3;A=6',
      'abs=P-L7,P-B4;G=2;A=3,4',
      'abs=P-L7,P-B4;G=;A=2,3,4;val=2:négatif',
      'abs=;G=;A=4;val=3:négatif',
      'abs=;G=;A=3;val=2:autre',
      'd3=1;abs=P-PIL;G=;A=6;plafV1=non;plaf=non',
      'd3=2;abs=P-PIL;G=;A=6;plafV1=non;plaf=non',
      'd3=3;abs=P-PIL;G=;A=6;plafV1=non;plaf=non',
      'd3=3;abs=P-PIL;G=;A=6;plafV1=non;plaf=oui',
      'd3=3;abs=P-V6,P-L7,P-B4,P-G1,P-C,P-EA,P-EAV,P-6a,P-6a-res,P-6,P-7,P-8,P-EP,P-LST,P-P4,P-PIL,P-ARR;G=;A=2,3,4,6,7,8;plafV1=non;plaf=non',
      'd3=1;abs=P-V6,P-L7,P-B4,P-G1,P-C,P-EA,P-EAV,P-6a,P-6a-res,P-6,P-7,P-8,P-EP,P-LST,P-P4,P-PIL,P-ARR;G=;A=2,3,4,6,7,8',
      'd5=a;abs=P-V6;G=;A=;C=2',
      'd5=c;abs=P-V6;G=;A=;C=2',
      'd5=c;abs=P-V6;G=;A=;V=2',
      'd7=garder;abs=P-T04;G=;A=1',
      'd7=retirer;abs=P-T04;G=;A=1']
ABS_29 = 'P-V6,P-L7,P-B4,P-G1,P-C,P-EA,P-EAV,P-6a,P-6a-res,P-6,P-7,P-8,P-EP,P-LST,P-P4,P-PIL,P-ARR'


# ---------------------------------------------------------------- audit R4
ANC = {'W1': 'W01', 'W2': 'W04 W05 W06 W07', 'W3': 'W02', 'W4': 'W03', 'W5': 'W36', 'W6': 'W08 W09', 'W7': 'W10', 'W8': 'W11',
       'W9': 'W13 W14 W41 W50', 'W10': 'W15 W16 W17 W40', 'W11': 'W17', 'W12': 'W18 W19', 'W13': 'W32 W33', 'W14': 'W20 W21',
       'W15': 'W22', 'W16': 'W34', 'W17': 'W25', 'W18': 'W26', 'W19': 'W28', 'W20': 'W29', 'W21': 'W35', 'W22': 'W30', 'W23': 'W30',
       'W24': 'W27', 'W25': 'W31'}
JETONS29 = r'\b(?:DP|PG|PC|MO|TC|DV|P40|MSG216|SY)\b'


def audit(W, P, V1t, dates):
    by = {w['ref']: w for w in W}
    v1 = [dict(ref=c[0], dep=c[2], sert=c[3], cl=c[4]) for c in tab(V1t, '| W', 5) if c[0] in ANC]
    used = set(); rs = ra = bo = sr = sa = 0
    for x in v1:
        D = [by[r] for r in ANC[x['ref']].split()]; used |= {d['ref'] for d in D}
        s1 = set() if x['sert'].startswith('—') else ks(x['sert'])
        s3 = set().union(*[ks(d['sert']) for d in D]); sr += len(s1 - s3); sa += len(s3 - s1)
        cond = x['cl'].startswith('cond'); d1 = ks(x['dep']) if cond else set()
        d3 = {P[p]['k'] for d in D for p in pr(d)} - {0}
        aux = any(P[p]['k'] == 0 for d in D for p in pr(d))  # un produit auxiliaire est un produit ajouté
        t = bool(s1 - s3 or d3 - d1 or aux) or (x['cl'].startswith('cont') and any(d['cl'] in 'KRF' for d in D)) or (cond and any(d['cl'] == 'F' for d in D))
        l = bool(s3 - s1 or (d1 - d3 and any(d['cl'] != 'F' for d in D))) or ('ferm' in x['cl'] and any(d['cl'] != 'F' for d in D))
        rs += t; ra += l; bo += t and l
    neuves = [w for w in W if w['ref'] not in used]

    def du29(w):
        ids = re.findall(r'R-\d+', w['src']); jt = re.findall(JETONS29, w['src'])
        return bool(ids or jt) and all(dates.get(i) == '2026-10-29' for i in ids) and not re.search(r'(?<![A-Za-z])[BGE] l\.|T7|N-\d|CLAUDE', w['src'])

    L = [w['ref'] for w in W if du29(w)]; keep = [w for w in W if w['ref'] not in L]
    drop = {p for p, v in P.items() if v['pro'] and v['pro'] <= set(L)}

    def reduit(w):
        pp = [q for q in prods(w['prod']) if q[0] not in drop]
        w2 = dict(w, prod=', '.join(n + ('†' if a else '') + ('‡' if b else '') + ('°' if c else '') for n, a, b, c in pp) or '—')
        w2['cl'] = classe(w2)
        return w2

    red = [reduit(w) for w in keep]
    cdiff = sum(a['cl'] != b['cl'] for a, b in zip(keep, red))
    K = cvk(P, 'a')
    S = ['abs=' + p for p in P] + ['G=%d' % k for k in range(1, 9)] + ['A=%d' % k for k in range(1, 9)] + ['val=%d:négatif' % k for k in K] + SC
    nd = 0; dl = set(); r0 = {w['ref'] for w in keep}
    for s in S:
        E = evaluer(W, P, s, 'scenario')
        a, _, _ = analyser(keep, P, E)
        b, _, _ = analyser(red, P, E)
        dif = {r for r in r0 if (a[r][0], a[r][2]) != (b[r][0], b[r][2])}
        if dif:
            nd += 1; dl |= dif
    I = [w for w in W if w['cl'] == 'I']; Id = [w for w in I if '[IND]' not in w['src']]
    h = hashlib.sha256('\n'.join(w['src'] for w in W).encode('utf-8')).hexdigest()[:16]
    v = lambda k, x: ('aud:' + k, [str(x)])
    return dict([v('v1', len(v1)), v('resserrees', rs), v('assouplies', ra), v('deux', bo), v('neutres', len(v1) - rs - ra + bo),
                 v('sert-retires', sr), v('sert-ajoutes', sa), v('deductions', sum(w['prod'].count('†') for w in W)),
                 v('lignes-deduites', sum('†' in w['prod'] for w in W)), v('bascules', sum(w['prod'].count('°') for w in W)),
                 v('neuves', len(neuves)),
                 v('neuves-sert', sum(w['sert'] != '—' for w in neuves)), v('neuves-ouvertes', sum(w['cl'] in 'IR' for w in neuves)),
                 v('L29', len(L)), v('retrait-sc', len(S)), v('retrait-diff', nd), v('retrait-lignes', len(dl)), v('retrait-classes', cdiff),
                 v('I-total', len(I)), v('I-IND', len(I) - len(Id)), v('I-defaut', len(Id)),
                 v('I-defaut-L29', sum(w['ref'] in L for w in Id)), v('chemins-a-nommer', sum(p['chem'].startswith('à nommer') for p in P.values())),
                 v('sources', h)])


def calc(W, P, V1t, dates):
    aux = {p for p, v in P.items() if v['k'] == 0}
    o = {}
    for p in P:
        o[p] = [fmt({w['ref'] for w in W if w['cl'] == 'K' and p in pr(w)}), fmt({w['ref'] for w in W if w['cl'] == 'K' and p in ets(w)})]
    Eh = dict(d3='1', d7='garder', plafV1=True)  # L9 avec le produit ° exigé (D:3 = (1) ou (3) avec plafond)
    for k in range(1, 9):
        L = [w for w in W if w['cl'] in 'KIR' and k in ks(w['sert'])]
        o['k:%d' % k] = [fmt({w['ref'] for w in L}), fmt({w['ref'] for w in L if w['cl'] == 'R'}), fmt(heritiers(W, P, {w['ref'] for w in L}, aux, Eh))]
    for s in SC:
        o['sc:' + s] = scenario(W, P, s)
    o.update(audit(W, P, V1t, dates))
    return o


# ---------------------------------------------------------------- § 0, dates et heures, sources, GO, décisions
def clauses(texte):
    L = [l[2:] for l in texte.splitlines() if l.startswith('> Si le verdict scellé de G0')]
    exige(len(L) == 2, ('§ 0 : deux clauses attendues (recommandée, appliquée)', len(L)))
    return L


def dates_du_texte(texte):
    return '|'.join(m.group(0) for m in RE_DATE_HEURE.finditer(texte))


def controle_s0(texte, dec_texte):
    sy, app = clauses(texte)
    exige(sha_txt(sy) == CLAUSE_SY_SHA, ('§ 0 : clause du collisionneur différente du texte gelé', sha_txt(sy)[:16]))
    exige(len(sy.split()) == CLAUSE_MOTS, ('§ 0 : compte de mots de la clause', len(sy.split())))
    exige('(%d mots' % CLAUSE_MOTS in texte, ('§ 0 : le compte de mots écrit n\'est pas %d' % CLAUSE_MOTS,))
    exige(sha_txt(app) == CLAUSE_APPLIQUEE_SHA, ('§ 0 : clause appliquée différente du texte gelé', sha_txt(app)[:16]))
    for m in MARQUES_CLAUSE:
        exige(m in app, ('§ 0 : marque absente de la clause appliquée', m))
    exige(CITATION_R765 in texte, ('§ 0 : citation de Lazar (R-765) absente ou tronquée',))
    exige(CITATION_R765 in dec_texte, ('§ 0 : citation de Lazar introuvable dans les fichiers de décisions',))


def clause_de_sy(sytexte):
    L = sytexte.splitlines()
    i = next((j for j, l in enumerate(L) if 'Clause (150 mots)' in l), None)
    exige(i is not None, 'SY : bloc « Clause (150 mots) » introuvable')
    j = i + 1
    while j < len(L) and not L[j].startswith('> '):
        j += 1
    bloc = []
    while j < len(L) and L[j].startswith('> '):
        bloc.append(L[j][2:]); j += 1
    return ' '.join(bloc)


def lignes_sources(texte):
    return [c for c in tab(texte, '| S:', 6)]


def controle_sources(texte):
    S = lignes_sources(texte)
    for c in S:
        exige(re.fullmatch(r'[0-9a-f]{64}', c[2]), ('source : empreinte mal formée', c[0]))
        exige(c[5] in ('figé', 'vivant'), ('source : statut figé ou vivant', c[0]))
        exige(not os.path.isabs(c[1].strip('`')) and '/tmp/' not in c[1], ('source : chemin non durable (absolu ou bloc-notes)', c[0], c[1]))
    exige(len({c[0] for c in S}) == len(S), 'source en double')
    exige(sha_txt('\n'.join('|'.join(c) for c in S)) == SOURCES_SHA, ('table des sources (S:) différente du texte gelé : chemin, empreinte, origine, lignes relues ou statut',))


def controle_go(texte):
    G = [tuple(c) for c in tab(texte, '| GO-', 3)]
    exige(G == GO_TABLE, ('§ 6.5 : tableau des GO différent du texte gelé', [g for g in G if g not in GO_TABLE][:1] or len(G)))


class Decs(dict):
    """{clé d'argument: option ou None} ; .cit = {identifiant: (R-nnn, option)} pour les décisions inscrites."""
    cit = None


def hors_guillemets(l):
    return re.sub(r'«[^«»]*»', '«»', l)


def option_citee(ligne, ident, opt):
    """L'option suit l'identifiant après « : », ou est écrite entre guillemets juste après lui."""
    i = r'(?<![\w:])' + re.escape(ident) + r'(?![0-9a-z])'
    o = r'\(?' + re.escape(opt) + r'\)?(?!\w)'
    return bool(re.search(i + r'\s*:\s*(?:«\s*)?' + o, ligne) or re.search(i + r'[^«»;:]{0,40}«\s*' + o + r'\s*»', ligne))


def est_registre(f):
    return os.path.normpath(f).replace(os.sep, '/').endswith(REGISTRE_LAZAR)


def controle_mot(ident, opts, opt, rnnn, lignes_dec):
    """CT6-07 : la ligne citée doit être un mot DIRECT de Lazar, non un relevé de session."""
    cands = lignes_dec.get(rnnn, [])
    exige(cands, ('§ 9 : décision citée introuvable dans DEC', ident, rnnn))
    regs = [l for l, f in cands if est_registre(f)]
    exige(regs, ('§ 9 : la ligne citée n\'est pas dans %s' % REGISTRE_LAZAR, ident, rnnn))
    l = regs[-1]; h = hors_guillemets(l)
    exige(MOT_DIRECT.search(h), ('§ 9 : la ligne citée n\'est pas un mot direct de Lazar (motif « Lazar (… heure de Paris, mot direct) » '
                                 'ou « Mots directs de Lazar » absent hors guillemets)', ident, rnnn))
    marques = [m for m in MARQUES_RELEVE if m in h.lower()]
    exige(not marques, ('§ 9 : ligne de relevé de session, non un mot de Lazar (marques hors guillemets)', ident, rnnn, marques))
    exige(re.search(r'(?<![\w:])' + re.escape(ident) + r'(?![0-9a-z])', l), ('§ 9 : la ligne citée ne contient pas l\'identifiant', ident, rnnn))
    donnees = sorted(x for x in opts if option_citee(l, ident, x))
    exige(donnees == [opt], ('§ 9 : option retenue absente de la ligne citée (après « : » ou entre guillemets) ou différente de la cellule',
                             ident, rnnn, donnees, opt))


def registre(texte, lignes_dec):
    """Lit le registre des décisions ; retourne Decs {clé d'argument: option ou None (« en attente »)}."""
    R = tab(texte, '| D:', 5)
    exige([c[0] for c in R] == list(DECISIONS), ('§ 9 : registre des décisions : identifiants ou ordre', [c[0] for c in R]))
    exige(sha_txt('\n'.join('|'.join(c[:-1]) for c in R)) == DECISIONS_SHA, ('§ 9 : registre des décisions : objet, options ou recommandation différents du texte gelé',))
    out = Decs(); out.cit = {}
    for c in R:
        cle, opts, reco = DECISIONS[c[0]]
        exige(c[2] == ' / '.join(opts), ('§ 9 : options admises', c[0], c[2]))
        exige(c[3].split(' ')[0] == reco, ('§ 9 : recommandation', c[0], c[3]))
        if c[4] == 'en attente':
            out[cle] = None; continue
        m = re.fullmatch(r'(R-\d+) : (\S+)', c[4])
        exige(m, ('§ 9 : mot de Lazar mal formé (« en attente » ou « R-nnn : option »)', c[0], c[4]))
        exige(m.group(2) in opts, ('§ 9 : option non admise', c[0], m.group(2)))
        controle_mot(c[0], opts, m.group(2), m.group(1), lignes_dec)
        out[cle] = m.group(2); out.cit[c[0]] = (m.group(1), m.group(2))
    return out


def controle_resume(texte):
    """Garde CT6-03 / CT6-04 / (f) : mêmes décisions, recommandations, confiances et sens dans le résumé, le § 9 et le registre."""
    res = section_texte(texte, 'Résumé pour Lazar')
    exige(RENVOI_S9 in res, ('résumé : renvoi au § 9 absent', RENVOI_S9))
    for x in INTERDITS_RESUME:
        exige(x not in res.lower(), ('résumé : expression plus forte que la table', x))
    s9 = section_texte(texte, '9. ')
    reg = {c[0]: c[3] for c in tab(texte, '| D:', 5)}
    ids_r = re.findall(r'^- \*\*(D:\w+)\*\*', res, re.M)
    ids_9 = re.findall(r'^\*\*(D:\w+) — ', s9, re.M)
    exige(ids_r == list(DECISIONS), ('résumé : décisions absentes, en trop ou hors ordre', ids_r))
    exige(ids_9 == list(DECISIONS), ('§ 9 : décisions absentes, en trop ou hors ordre', ids_9))

    def bloc(t, debut, fins):
        i = t.index(debut); j = min([k for k in (t.find(f, i + len(debut)) for f in fins) if k > 0] or [len(t)])
        return t[i:j]
    for i, (cle, opts, reco) in DECISIONS.items():
        br = bloc(res, '- **%s**' % i, ('\n- **D:', '\n**'))
        b9 = bloc(s9, '**%s — ' % i, ('\n**D:', '\n**Registre'))
        exige('Enjeu :' in br, ('résumé : enjeu absent', i))
        mr = re.findall(r'Recommandation : \(?([^),\s]+)\)?, confiance (0,\d+) ; sens : (ouvre|ferme|mixte)', br)
        m9 = re.findall(r'\*Recommandation[^*]*\* : \(?([^),\s]+)\)?, confiance (0,\d+)', b9)
        s9s = re.findall(r'\*Sens\* : (ouvre|ferme|mixte)', b9)
        mg = re.fullmatch(r'(\S+) \((0,\d+)\), .+', reg[i])
        exige(len(mr) == 1 and len(m9) == 1 and len(s9s) == 1 and mg, ('résumé ou § 9 : recommandation, confiance ou sens introuvable ou dupliqué', i))
        exige(mr[0][0] == m9[0][0] == mg.group(1) == reco, ('recommandation : résumé, § 9 et registre diffèrent', i, mr[0][0], m9[0][0], mg.group(1)))
        exige(mr[0][1] == m9[0][1] == mg.group(2), ('confiance : résumé, § 9 et registre diffèrent', i, mr[0][1], m9[0][1], mg.group(2)))
        exige(mr[0][2] == s9s[0] == SENS[i], ('sens : résumé, § 9 et constante diffèrent', i, mr[0][2], s9s[0], SENS[i]))


def controle_67(texte):
    """Garde CT6-08 : les treize cas d'inatteignabilité du § 6.7, dans l'ordre."""
    L = [l for l in texte.split('\n') if l.startswith('- **6.7 ')]
    exige(len(L) == 1, ('§ 6.7 introuvable ou dupliqué', len(L)))
    pos = -1
    for c in CAS_67:
        i = L[0].find('(%s) **' % c, pos + 1)
        exige(i > pos, ('§ 6.7 : cas absent ou hors ordre', c))
        pos = i


def hyp_du_texte(texte):
    m = re.findall(r'`hyp: ([^`]+)`', texte)
    exige(len(m) == 1, ('§ 5 : ligne d\'hypothèse des scénarios introuvable ou dupliquée', len(m)))
    exige(m[0] == SC_HYP, ('§ 5 : hypothèse des scénarios différente du texte gelé', m[0]))
    reco = ';'.join('%s=%s' % (v[0], v[2]) for v in DECISIONS.values())
    exige(SC_HYP == reco, ('§ 5 : l\'hypothèse des scénarios doit égaler les recommandations du § 9', reco))


def verifier_texte(texte, V1t, dates, dec_texte, lignes_dec, sytexte=None, sections_gelees=True):
    controle_s0(texte, dec_texte)
    if sytexte is not None:
        exige(clauses(texte)[0] == clause_de_sy(sytexte), '§ 0 : la clause recopiée diffère de SY § 5 (comparaison mot pour mot)')
    dt = dates_du_texte(texte)
    if dt != DATES_HEURES:
        a, b = dt.split('|'), DATES_HEURES.split('|')
        i = next((j for j in range(min(len(a), len(b))) if a[j] != b[j]), min(len(a), len(b)))
        raise Echec(('dates et heures : différence au rang %d' % i, a[i] if i < len(a) else '(fin)', 'attendu', b[i] if i < len(b) else '(fin)'))
    exige(EMPREINTE_SCRIPT() in texte, 'annexe A : la table ne cite pas l\'empreinte de ce script')
    controle_sources(texte)
    controle_go(texte)
    decs = registre(texte, lignes_dec)
    controle_resume(texte)
    controle_67(texte)
    hyp_du_texte(texte)
    exige(sha_txt(regles(texte)) == REGLES_SHA, '§ 5 : texte des règles L0 à L14 différent du texte gelé')
    exige(sha_txt(section_texte(texte, '9. ')) == S9_SHA, '§ 9 : texte des décisions différent du texte gelé')
    W, P = charge(texte)
    exige(set(P) == set(CHEMINS), ('produits différents de la liste gelée', sorted(set(P) ^ set(CHEMINS))))
    for p, v in P.items():
        exige(v['chem'] == CHEMINS[p], (p, 'motif de chemin différent du motif gelé', v['chem']))
        exige(v['pro_txt'] == PRODUCTEURS[p], (p, 'producteur différent du producteur gelé', v['pro_txt']))
    exige(sha_txt('\n'.join(w['ref'] + '|' + w['trav'] for w in W)) == TRAVAIL_SHA, '§ 4 : colonne « travail » différente du texte gelé (ou ligne ajoutée, retirée, déplacée)')
    exige(len({w['ref'] for w in W}) == len(W), 'refs en double')
    exige(sorted(p['k'] for p in P.values() if p['k']) == list(range(1, 9)), 'un produit par critère')
    four = {}
    for w in W:
        exige(re.fullmatch(r'W\d\d', w['ref']), ('réf mal formée', w['ref']))
        for x in pr(w):
            exige(x in P, (w['ref'], 'produit inconnu', x))
        for x in fourn(w):
            exige(x in P, (w['ref'], 'produit fourni inconnu', x))
            exige(w['ref'] not in four.get(x, set()), (w['ref'], 'produit fourni deux fois', x))
            four.setdefault(x, set()).add(w['ref'])
        exige(classe(w) == w['cl'], (w['ref'], 'classe recalculée sans date'))
        exige(w['cl'] not in 'FH' or w['sert'] == '—', (w['ref'], 'F ou H avec sert'))
        exige(w['cl'] != 'R' or w['sert'] != '—', (w['ref'], 'R sans sert'))
        exige(w['sert'] == '—' or re.fullmatch(r'[1-8](, [1-8])*', w['sert']), (w['ref'], 'sert mal formé'))
        exige(not set(fourn(w)) & set(pr(w)), (w['ref'], 'cite son propre produit'))
        exige('[IND]' not in w['src'] or w['cl'] == 'I', (w['ref'], '[IND] hors classe I'))
        for n in ets(w):
            exige(P[n]['cls'] == 'oui', (w['ref'], '‡ sur un produit sans classe lue', n))
        for n in bas(w):
            exige(P[n]['k'] == 0 and w['cl'] == 'K', (w['ref'], '° hors produit auxiliaire ou hors ligne K', n))
        if w['ref'] in D7_LIGNES:
            exige(any(q[0] == 'P-T04' and q[1] for q in prods(w['prod'])), (w['ref'], 'D:7 : l\'arête P-T04† attendue'))
    for p, v in P.items():
        exige(v['pro'] == four.get(p, set()), (p, 'producteur différent des lignes qui le fournissent', sorted(v['pro']), sorted(four.get(p, set()))))
        exige(v['typ'] in TYPES, (p, 'type inconnu'))
        exige(v['cls'] in ('oui', 'non'), (p, 'classe oui/non'))
        exige(v['cls'] == 'non' or v['typ'] in ('verdict', 'lecture'), (p, 'classe lue sur un produit sans verdict'))
        exige(v['chem'] != '—', (p, 'chemin absent'))
    g = {w['ref']: set().union(*[P[x]['pro'] for x in pr(w)]) if pr(w) else set() for w in W}

    def vis(r, pile):
        exige(r not in pile, ('cycle', pile, r))
        for s in sorted(g[r]):
            vis(s, pile + [r])
    for r in g:
        vis(r, [])
    o = calc(W, P, V1t, dates)
    rows = {}
    for l in texte.splitlines():
        if l.startswith('|'):
            c = cells(l)
            if c and re.fullmatch(r'P-[A-Za-z0-9-]+|k:\d+|sc:.+|aud:[A-Za-z0-9-]+', c[0]):
                rows.setdefault(c[0], []).append(c)
    exige(set(rows) == set(o), ('lignes dérivées en trop ou manquantes', sorted(set(rows) ^ set(o))))
    for key, v in o.items():
        exige(len(rows[key]) == 1, ('ligne dérivée dupliquée', key))
        exige(rows[key][0][-len(v):] == v, ('ligne dérivée fausse', key, v, rows[key][0]))
    if sections_gelees:  # filet final : le texte entier, section par section
        s = sections(texte)
        exige(set(s) == set(SECTIONS), ('sections ajoutées, retirées ou renommées', sorted(set(s) ^ set(SECTIONS))))
        for k, h in s.items():
            exige(h == SECTIONS[k], ('texte gelé : section modifiée', k))
    return W, P, o, decs


def charger_dec(dec):
    """lignes : {R-nnn: [(ligne, fichier), ...]} (le fichier compte : seul registres/decisions.md porte un mot de Lazar)."""
    dates = {}; txt = []; lignes = {}
    for f in dec.split(','):
        t = open(f, encoding='utf-8').read(); txt.append(t)
        for l in t.splitlines():
            m = re.match(r'\| (R-\d+) \| (\S+) \|', l)
            if m:
                dates[m.group(1)] = m.group(2); lignes.setdefault(m.group(1), []).append((l, f))
    return dates, '\n'.join(txt), lignes


def bilan_dec(DEC, decs):
    """Imprime l'empreinte de chaque fichier de DEC et les R-nnn cités (le lecteur R13 les recopie)."""
    for f in DEC.split(','):
        print('fichier de décisions : %s sha256 %s%s' % (f, sha(f), '' if est_registre(f) else ' (non lu pour les mots de Lazar)'))
    cit = decs.cit or {}
    print('mots de Lazar cités : ' + (' ; '.join('%s=%s (%s)' % (i, cit[i][0], cit[i][1]) for i in DECISIONS if i in cit) or 'aucun'))


def lire(p):
    return open(p, encoding='utf-8').read()


def verif_fichiers(D, V1, DEC, SY=None):
    dates, dt, lg = charger_dec(DEC)
    return verifier_texte(lire(D), lire(V1), dates, dt, lg, lire(SY) if SY else None)


# ---------------------------------------------------------------- feuille, simulation
def exige_scelle(f, quoi):
    r = t2_local(f)
    exige(r is None, ('%s (%s) : aucune feuille ; L0 et § 6.1 (aucune lecture de G0 avant le scellement)' % (quoi, r),))


def imprimer(W, P, E, st, G, Ap, entete):
    T = set(range(1, 9)) - E['A'] - E['G1'] - E['V'] - E['C']
    ls = lambda s: ','.join(map(str, sorted(s))) or '—'
    on = lambda b: 'oui' if b else 'non'
    print(entete)
    print('décisions : ' + ' ; '.join('%s=%s' % (i, E[v[0]]) for i, v in DECISIONS.items()))
    print('V1 : A=%s G=%s V=%s C=%s tenus=%s | lus par L8 : A=%s G=%s | constat : pres=%s | gel antérieur=%s' % (
        ls(E['A']), ls(E['G1']), ls(E['V']), ls(E['C']), ls(T), ls(E['Aeff']), ls(E['Geff']), ls(E['pres']), ls(E['gel'])))
    print('lu à l\'étape : abs=%s | val=%s | plafond fixé à V1=%s | plafond fixé à l\'étape=%s' % (
        ','.join(sorted(E['ab'])) or '—', ','.join('%d:%s' % kv for kv in sorted(E['val'].items())) or '—', on(E['plafV1']), on(E['plaf'])))
    print('G\' (gel effectif)=%s | A\'=%s' % (ls(G), ls(Ap)))
    if E['d3'] == '3' and not E['plafV1']:
        print('L11 (D:3 = 3) : plafond non fixé à V1 : les produits marqués ° ne sont pas exigés (W21 sans P-PIL)')
    if E['d3'] == '2':
        print('D:3 = 2 : les produits marqués ° ne sont jamais exigés (W21 sans P-PIL)')
    if E['d7'] == 'retirer':
        print('L13 (D:7 = retirer) : W19 et W33 n\'exigent pas P-T04')
    if not E['plaf']:
        print('§ 6.5 (ii) : plafond non fixé à l\'étape : aucun devis ne passe, aucun droit de devis')
    for k in sorted(G & {k for k, v in E['val'].items() if v == 'établi'}):
        print('ALERTE : critère %d gelé dont la classe lue est établi : le gel demeure (L2bis)' % k)
    for r in sorted(st):
        e, m, d = st[r]
        print(r, e, m, 'devis' if d else '—')
    n = lambda x: sum(1 for v in st.values() if v[0] == x)
    print('bilan : %d ouvertes, %d fermées, %d à Lazar, %d avec droit de devis' % (n('ouverte'), n('fermée'), n('Lazar'), sum(v[2] for v in st.values())))


def feuille(D, V1, DEC, spec, script=None):
    texte = lire(D); W, P, o, decs = verif_fichiers(D, V1, DEC)
    exige_scelle(D, 'table non scellée'); exige_scelle(script or __file__, 'script non scellé')
    attente = [i for i, v in DECISIONS.items() if decs[v[0]] is None]
    exige(not attente, ('table non applicable (L0, R-518) : décisions en attente du mot de Lazar : ' + ', '.join(attente),))
    E = evaluer(W, P, spec, 'feuille', decs)
    st, G, Ap = analyser(W, P, E)
    imprimer(W, P, E, st, G, Ap, 'FEUILLE DE REPLI | table sha256 %s | script sha256 %s' % (sha_txt(texte), EMPREINTE_SCRIPT()))
    bilan_dec(DEC, decs)


def simuler(D, V1, DEC, spec):
    texte = lire(D); W, P, o, decs = verif_fichiers(D, V1, DEC)
    E = evaluer(W, P, spec, 'simuler')
    st, G, Ap = analyser(W, P, E)
    b = 'SIMULATION — décisions passées en argument, non les mots de Lazar ; ce n\'est pas une feuille de repli'
    imprimer(W, P, E, st, G, Ap, b + ' | table sha256 %s' % sha_txt(texte))
    print(b)


# ---------------------------------------------------------------- tests de produit (T1, T2, T4)
def sha(f):
    h = hashlib.sha256()
    with open(f, 'rb') as fh:
        for b in iter(lambda: fh.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def t2_local(f):
    c = f + '.sha256'
    if not os.path.isfile(c):
        return 'T2 compagnon absent'
    l = [x for x in lire(c).splitlines() if x.strip()]
    if len(l) != 1:
        return 'T2 compagnon : une ligne attendue'
    m = re.fullmatch(r'([0-9a-f]{64})  (\S.*)', l[0])
    if not m:
        return 'T2 compagnon illisible'
    if m.group(2) != os.path.basename(f):
        return 'T2 nom du compagnon'
    return None if m.group(1) == sha(f) else 'T2 empreinte différente'


def module_depot(depot, nom):
    sys.path.insert(0, os.path.realpath(os.path.join(depot, 'src')))  # chemin réel : un lien du dépôt jouet ne survit pas
    try:
        return __import__('controle_ia.' + nom, fromlist=[nom])
    except Exception as e:
        raise Echec('import de controle_ia.%s échoué (%s) ; aucun repli' % (nom, e))


def t2(depot, f, officiel):
    """T2 : `controle_ia.scellement.verifier` du dépôt fait foi ; la réimplémentation locale doit concorder."""
    loc = t2_local(f)
    if not officiel:
        return loc
    sc = module_depot(depot, 'scellement')
    try:
        sc.verifier(f); off = None
    except Exception as e:
        off = 'T2 ' + str(e)[:90]
    exige((loc is None) == (off is None), ('T2 : divergence entre scellement.verifier et la réimplémentation', f, loc, off))
    return off


def t4(depot, f):
    pg = module_depot(depot, 'prereg')
    try:
        pg.exiger_prereg_scelle(os.path.abspath(f))
    except Exception as e:
        return 'T4 ' + str(e)[:90]
    return None


version = lambda f: int((re.search(r'-v(\d+)(?:\.[^/]*)?$', f) or [0, 0])[1])


def tester(P, depot, nommes, avec_t4=True, officiel=True):
    abs_ = []; lignes = []
    for p, v in P.items():
        pats = nommes[p].split('+') if p in nommes else ([] if v['chem'].startswith(('nommé par', 'à nommer')) else v['chem'].split())
        if not pats:
            abs_.append(p); lignes.append('%s absent (chemin non nommé : %s)' % (p, v['chem'])); continue
        motif = ''; ref = []
        for pat in pats:
            valides = []; raisons = []
            for f in sorted(glob.glob(os.path.join(depot, pat))):
                if f.endswith('.sha256') or not os.path.isfile(f):
                    continue
                r = t2(depot, f, officiel) or (t4(depot, f) if (v['typ'] == 'prereg' and avec_t4) else None)
                (raisons if r else valides).append(r or f)
            if not valides:
                motif = 'T1 aucun fichier pour %s' % pat if not raisons else raisons[-1] + ' (%s)' % pat; break
            ref.append(max(valides, key=lambda f: (version(f), f)))
        if motif:
            abs_.append(p); lignes.append('%s absent (%s)' % (p, motif))
        else:
            lignes.append('%s présent : %s' % (p, ' ; '.join(os.path.relpath(f, depot) for f in ref)))
    return abs_, lignes


# ---------------------------------------------------------------- constat du 31 décembre
def constat(A, fichier):
    pres = set(); vus = set(); entetes = {'commit C_31': False, 'grille': False}
    for l in lire(fichier).splitlines():
        if not l.strip() or l.startswith('#'):
            continue
        m = re.fullmatch(r'critère ([1-8]) : (présents|absents(?: — T[1-4])?)', l)
        if m:
            k = int(m.group(1)); exige(k in A, ('critère hors de A', k)); exige(k not in vus, ('critère en double', k)); vus.add(k)
            if m.group(2) == 'présents':
                pres.add(k)
            continue
        m = re.fullmatch(r'(commit C_31|grille) : ([0-9a-f]{40}|[0-9a-f]{64})', l)
        exige(m, ('ligne hors format fermé', l)); exige(not entetes[m.group(1)], ('en-tête en double', m.group(1))); entetes[m.group(1)] = True
    exige(vus == A, ('critères de A non couverts', sorted(A - vus)))
    exige(all(entetes.values()), ('en-tête manquant', [k for k, v in entetes.items() if not v]))
    return pres


def constat_table(D, V1, DEC, fichier, spec, script=None):
    W, P, o, decs = verif_fichiers(D, V1, DEC)
    exige_scelle(D, 'table non scellée'); exige_scelle(script or __file__, 'script non scellé')
    attente = [i for i, v in DECISIONS.items() if decs[v[0]] is None]
    exige(not attente, ('constat refusé (L0, R-518) : décisions en attente du mot de Lazar : ' + ', '.join(attente),))
    d = lire_spec(spec, {'A', 'V', 'C'})
    A, V, C = (ensemble(d.get(x, ''), x) for x in 'AVC')
    cible = A | ((V | C) if decs['d5'] == 'b' else set()) | (C if decs['d5'] == 'c' else set())
    pres = constat(cible, fichier)
    bilan_dec(DEC, decs)
    return pres


# ---------------------------------------------------------------- sources
def sources(D, depot):
    err = 0
    for c in lignes_sources(lire(D)):
        f = c[1].strip('`')
        exige(not os.path.isabs(f), ('source : chemin absolu', c[0]))
        p = os.path.join(depot, f)
        if not os.path.isfile(p):
            print('ABSENTE   ', c[0], f); err += c[5] == 'figé'; continue
        h = sha(p); ok = h == c[2]
        print('%-10s %s %s %s' % ('OK' if ok else ('DIFFÉRENTE' if c[5] == 'figé' else 'a bougé'), c[0], c[5], h[:16]))
        err += (not ok) and c[5] == 'figé'
    exige(err == 0, ('sources figées différentes ou absentes', err))


# ---------------------------------------------------------------- classification à l'aveugle
def aveugle(W):
    for w in W:
        s = re.sub(r'\[(?:H|REJEU|IND|GEL-SY)\]|\b(?:d1|d2|préalable)\b', '', w['src'])
        print('%s | %s | %s' % (w['ref'], w['trav'], re.sub(r'\s*;\s*;', ' ;', s).strip(' ;')))


def concordance(W, fichier):
    rep = {}
    for l in lire(fichier).splitlines():
        if not l.strip():
            continue
        m = re.fullmatch(r'(W\d\d) ([FKRIH]) (—|P-\S+) (—|[1-8](?:,[1-8])*)', l.strip())
        exige(m, ('réponse mal formée', l)); exige(m.group(1) not in rep, ('réponse en double', m.group(1)))
        rep[m.group(1)] = (m.group(2), set() if m.group(3) == '—' else set(m.group(3).split(',')), set() if m.group(4) == '—' else set(map(int, m.group(4).split(','))))
    ecarts = 0
    for w in W:
        if w['ref'] not in rep:
            continue
        c, p, s = rep[w['ref']]
        mot = [x for x, ok in (('classe', c == w['cl']), ('produits', p == set(pr(w))), ('sert', s == ks(w['sert']))) if not ok]
        if mot:
            ecarts += 1; print('ÉCART', w['ref'], ','.join(mot), '| table :', w['cl'], fmt(set(pr(w))), w['sert'])
    exige(set(rep) <= {w['ref'] for w in W}, ('réponse sur une réf inconnue', sorted(set(rep) - {w['ref'] for w in W})))
    print('concordance : %d réponses, %d écarts' % (len(rep), ecarts))


# ---------------------------------------------------------------- essais (R5)
def altérations(base):
    def sub(old, new, n=1, b=None):
        b = base if b is None else b
        exige(b.count(old) >= 1, ('essai : texte introuvable', old[:70]))
        return b.replace(old, new, n)
    L = {}
    # E01 à E48 : altérations de la v5 (dont celles des contre-lectures de la v3 et de la v4), rejouées sur la v7
    L['E01 cellule k:3 changée'] = re.sub(r'(\| k:3 \| [^|]*?), (W\d\d) \|', r'\1 |', base, count=1)
    L['E02 produit ajouté à W15'] = sub('témoin lexical | P-T04† |', 'témoin lexical | P-T04†, P-NM |')
    L['E03 sert de W16 : 3 -> 2, 3'] = sub('| P-T04†, P-V6‡, P-7, P-P4, P-EP | P-L7, P-LST | 3 |', '| P-T04†, P-V6‡, P-7, P-P4, P-EP | P-L7, P-LST | 2, 3 |')
    L['E04 aud:neutres modifié'] = re.sub(r'(\| aud:neutres \| [^|]*\| )(\d+)( \|)', lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), base, count=1)
    L['E05 producteur de P-L7 changé (colonne producteur)'] = sub('| P-L7 | 3 | verdict | W16 |', '| P-L7 | 3 | verdict | W19 |')
    L['E06 classe de W20 K -> I'] = sub('| P-T03† | — | 6 | K |', '| P-T03† | — | 6 | I |')
    L['E07 ligne W42 supprimée'] = ''.join(l for l in base.splitlines(True) if not l.startswith('| W42 |'))
    L['E08 jeton [REJEU] retiré de W09'] = sub('D R-025 ; [REJEU]', 'D R-025')
    L['E09 scénario 1 : une cellule changée'] = re.sub(r'(\| sc:abs=P-V6,P-L7;G=;A=2,3 \| )([^|]*?), (W\d\d) \|', r'\1\2 |', base, count=1)
    L['E10 † retiré de W11'] = sub('rubrique | P-T04† |', 'rubrique | P-T04 |')
    L['E11 W24 (F) reçoit un sert'] = sub('sentinelle GO-03 | — | — | — | F |', 'sentinelle GO-03 | — | — | 5 | F |')
    L['E12 ligne k:2 dupliquée, fausse en tête'] = sub('| k:2 |', '| k:2 | W99 | aucune | aucune |\n| k:2 |')
    L['E13 ligne k:9 parasite'] = sub('| k:8 |', '| k:9 | W01 | aucune | aucune |\n| k:8 |')
    L['E14 cycle : W16 cite P-L7'] = sub('| P-T04†, P-V6‡, P-7, P-P4, P-EP | P-L7, P-LST | 3 |', '| P-T04†, P-V6‡, P-7, P-P4, P-EP, P-L7 | P-L7, P-LST | 3 |')
    L['E15 ligne P-T04 : W48 retirée'] = re.sub(r'(\| P-T04 \|[^\n]*?), W48', r'\1', base, count=1)
    L['E16 W19 : P-L7 ajouté (resserrement)'] = sub('| P-T04†, P-V6‡, P-LST, P-8, P-EP |', '| P-T04†, P-V6‡, P-LST, P-8, P-EP, P-L7 |')
    L['E17 citation de source changée'] = sub('B l.126-135 ; G l.356-362', 'B l.999-1000 ; G l.356-362')
    L['E18 W38 : [H] remplacé'] = sub('R-485 ; [H] |', 'R-485 ; [X] |')
    E19 = sub('essais hors ligne (v44 à v47) ; course réelle = dépense facturée sur GO | — | — | — | I |', 'essais hors ligne (v44 à v47) ; course réelle = dépense facturée sur GO | — | — | 2 | I |')
    L['E19 W34 reçoit sert 2, sans mise à jour des tables'] = E19
    L['E20 W34 sert 2 et k:2 mis à jour (cohérent)'] = re.sub(r'(\| k:2 \| )([^|]*?) \|', lambda m: m.group(1) + ', '.join(sorted(m.group(2).split(', ') + ['W34'])) + ' |', E19, count=1)
    L['E21 ‡ retiré de W16'] = sub('| P-T04†, P-V6‡, P-7, P-P4, P-EP | P-L7, P-LST | 3 |', '| P-T04†, P-V6, P-7, P-P4, P-EP | P-L7, P-LST | 3 |')
    L['E22 W23 : sert 6 ajouté (droit direct)'] = sub('| P-T04†, P-ARR | P-PIL | — | K |', '| P-T04†, P-ARR | P-PIL | 6 | K |')
    L['E23 W16 cite un produit inexistant'] = sub('| P-T04†, P-V6‡, P-7, P-P4, P-EP | P-L7, P-LST | 3 |', '| P-T04†, P-V6‡, P-7, P-P4, P-EP, P-V66 | P-L7, P-LST | 3 |')
    L['E24 produit fourni par une seconde ligne'] = sub('| P-L7, P-LST | 3 |', '| P-L7, P-LST, P-B4 | 3 |')
    L['E25 P-V6 : classe lue retirée'] = sub('| P-V6 | 2 | verdict | W41 | oui |', '| P-V6 | 2 | verdict | W41 | non |')
    L['E26 [IND] sur une ligne K'] = sub('B l.154-158 ; E l.44', 'B l.154-158 ; E l.44 ; [IND]')
    L['E27 cycle réel : W41 cite P-L7'] = sub('| P-T04†, P-6, P-7, P-8 | P-V6, P-EP |', '| P-T04†, P-6, P-7, P-8, P-L7 | P-V6, P-EP |')
    L['E28 † retiré de W14'] = sub('| P-T04†, P-6a | P-6a-res |', '| P-T04, P-6a | P-6a-res |')
    L['E29 « sert » ajouté à W17'] = sub('| P-T04†, P-7, P-EP | — | — | K |', '| P-T04†, P-7, P-EP | — | 3 | K |')
    L['E30 citation changée'] = sub('G l.196-201, l.473-475', 'G l.196-299, l.473-475')
    L['E31 F -> I avec jeton retiré (W26)'] = sub('| — | — | — | F | E l.49 ; B l.180 ; d1 |', '| — | — | — | I | E l.49 ; B l.180 |')
    L['E32 H -> I (W38)'] = sub('| — | — | — | H | B l.340-342', '| — | — | — | I | B l.340-342').replace('R-485 ; [H] |', 'R-485 |')
    L['E33 ‡ retiré de W19'] = sub('| P-T04†, P-V6‡, P-LST, P-8, P-EP |', '| P-T04†, P-V6, P-LST, P-8, P-EP |')
    L['E34 produit retiré de W41'] = sub('| P-T04†, P-6, P-7, P-8 | P-V6, P-EP |', '| P-T04†, P-6, P-7 | P-V6, P-EP |')
    L['E35 « sert » retiré de W18'] = sub('| — | P-8 | 4 | I |', '| — | P-8 | — | I |')
    L['E36 clause appliquée : (b) « absent » -> « négatif »'] = sub('vaut « non tenu — absent » (recommandation)', 'vaut « non tenu — négatif » (recommandation)')
    L['E37 date du 31 janvier changée hors clause (§ 6.6)'] = sub('au second verdict (31 janvier 2027, 23:59 UTC au plus tard)', 'au second verdict (28 février 2027, 23:59 UTC au plus tard)')
    L['E38 motif de chemin changé (P-V6)'] = sub('| docs/verdicts/verdict-T0.6-critere-2-G0-v*.md |', '| docs/verdicts/verdict-T0.6bis-critere-2-G0-v*.md |')
    L['E39 bascule ° retirée de W21'] = sub('P-PIL†° |', 'P-PIL† |')
    L['E40 citation de Lazar tronquée'] = base.replace(CITATION_R765, 'gèle seulement ce critère jusqu\'au second verdict')
    L['E41 compte de mots 168 -> 150'] = sub('(168 mots', '(150 mots')
    L['E42 clause du collisionneur : un mot changé'] = sub("n'est jamais retenté et rend la porte", "n'est jamais retenté et laisse la porte")
    L['E43 échéance ISO d\'un GO changée'] = sub('| GO-2026-10-29-16 | 2 USD | 2026-11-05 |', '| GO-2026-10-29-16 | 2 USD | 2026-11-15 |')
    L['E44 ° posé sur un produit de critère'] = sub('P-V6‡†, P-L7,', 'P-V6‡†, P-L7°,')
    L['E45 P-EA : un producteur retiré'] = sub('| P-EA | 8 | autre | W04, W05, W06 |', '| P-EA | 8 | autre | W04, W05 |')
    L['E46 W28 revient à P-EA'] = sub('| P-T03, P-NM, P-EAV |', '| P-T03, P-NM, P-EA |')
    L['E47 W24 : jeton [GEL-SY] retiré'] = sub('B l.218 ; [GEL-SY] |', 'B l.218 |')
    L['E48 empreinte du script retirée de l\'annexe'] = base.replace(EMPREINTE_SCRIPT(), '0' * 64)
    # CL01 à CL32 : les 32 altérations de la contre-lecture de la v5 (rapport, (e)), reconstruites sur le texte de la v7
    L['CL01 « sert » de W21 : 6 -> 6, 7'] = sub('| P-V6‡†, P-L7, P-B4, P-T03†, P-PIL†° | P-G1 | 6 |', '| P-V6‡†, P-L7, P-B4, P-T03†, P-PIL†° | P-G1 | 6, 7 |')
    L['CL02 W44 I -> H (avec [H])'] = sub('écrite avant lecture ; aucun code tiers avant revue ; exécution = dépense facturée sur GO | — | — | — | I | D R-480, R-488, R-776 ; MSG216 pt 3 |',
                                          'écrite avant lecture ; aucun code tiers avant revue ; exécution = dépense facturée sur GO | — | — | — | H | D R-480, R-488, R-776 ; MSG216 pt 3 ; [H] |')
    L['CL03 cellule k:2 modifiée'] = re.sub(r'(\| k:2 \| )([^|]*?)( \|)', lambda m: m.group(1) + m.group(2) + ', W22' + m.group(3), base, count=1)
    L['CL04 aud:L29 modifié'] = re.sub(r'(\| aud:L29 \| [^|]*\| )(\d+)( \|)', lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), base, count=1)
    L['CL05 date 15 -> 16 novembre (D:2)'] = sub('(b) 15 novembre 2026, 23:59 UTC, avec la grille', '(b) 16 novembre 2026, 23:59 UTC, avec la grille')
    L['CL06 recommandation de D:1 changée, date de l\'option (c) retirée'] = sub('*Recommandation* : (a), confiance 0,55 (écrite par', '*Recommandation* : (c), confiance 0,55 (écrite par',
                                                                                   b=sub('second lecteur unique jusqu\'au 7 février 2027 à 23:59 UTC, puis', 'second lecteur unique, puis'))
    L['CL07 jeton [GEL-SY] -> préalable (W24)'] = sub('B l.218 ; [GEL-SY] |', 'B l.218 ; préalable |')
    L['CL08 clause appliquée (c) changée'] = sub('[plafond non fixé ; D:3] pendant le report, seules les tâches de la table de dépendance scellée continuent, sur devis sous un plafond fixé d\'avance,',
                                                 '[plafond non fixé ; D:3] pendant le report, seules les tâches de la table de dépendance scellée continuent, sur devis,')
    L['CL09 motif de chemin de P-C'] = sub('| prereg/papier-C-*-v*.md |', '| prereg/papierC-*-v*.md |')
    L['CL10 en-tête : modèle déclaré'] = sub('Modèle : **Opus 5.5** (sous-agent neuf)', 'Modèle : **Sonnet 5.5** (sous-agent neuf)')
    L['CL11 puce (c) du § 0'] = sub('- **(c) gardé, sans son plafond.**', '- **(c) gardé, avec son plafond.**')
    L['CL12 producteur de P-P4 changé dans les deux tables (cohérent)'] = sub('| P-P4 | — | lecture | W12 |', '| P-P4 | — | lecture | W15 |',
        b=sub('| P-T04† | P-P4 | 3 | K | G l.236-237', '| P-T04† | — | 3 | K | G l.236-237', b=sub('témoin lexical | P-T04† | — | 3 | K |', 'témoin lexical | P-T04† | P-P4 | 3 | K |')))
    L['CL13 heure du second verdict 23:59 -> 12:00 (§ 6.6)'] = sub('au second verdict (31 janvier 2027, 23:59 UTC au plus tard)', 'au second verdict (31 janvier 2027, 12:00 UTC au plus tard)')
    L['CL14 empreinte de S:B changée'] = sub('| S:B | docs/brief-claude-code-programme-complet-v2.md | 9261932a', '| S:B | docs/brief-claude-code-programme-complet-v2.md | 9261932b')
    L['CL15 colonne travail de W52 : neuvième -> huitième'] = sub('recette d\'HELIOS comme neuvième comparateur', 'recette d\'HELIOS comme huitième comparateur')
    L['CL16 colonne travail de W23 : seize -> soixante'] = sub('pilote réel sur seize tâches', 'pilote réel sur soixante tâches')
    L['CL17 prose du § 3 : dernière -> première version scellée'] = sub('le produit de référence est la **dernière version scellée**', 'le produit de référence est la **première version scellée**')
    L['CL18 montant d\'un GO : 11,8 -> 118 USD'] = sub('| GO-2026-10-29-10 | 11,8 USD |', '| GO-2026-10-29-10 | 118 USD |')
    L['CL19 texte de L3'] = sub('**L3** Une ligne K non gelée est ouverte', '**L3** Une ligne K non gelée est toujours ouverte')
    L['CL20 texte de L8'] = sub('Sous (a), lettre de R-765, les critères de V et de C n\'ont ni gel, ni constat, ni droit de devis', 'Sous (a), lettre de R-765, les critères de V et de C ont un droit de devis')
    L['CL21 texte de L9'] = sub('a droit de devis si le plafond du report est fixé à l\'étape (`plaf=oui`)', 'a droit de devis (`plaf=oui`)')
    L['CL22 statut de S:B : figé -> vivant'] = re.sub(r'(\| S:B \|[^\n]*\| )figé( \|)', r'\1vivant\2', base, count=1)
    L['CL23 lignes relues de S:B'] = sub('| dépôt de travail | l. 140-180, 218 | figé |', '| dépôt de travail | en entier | figé |')
    L['CL24 recommandation de D:1 : a -> b (registre)'] = sub('| a / b / c | a (0,55), auteur de la v6 |', '| a / b / c | b (0,55), auteur de la v6 |')
    L['CL25 recommandation de D:3 : 1 -> 3 (prose)'] = sub('*Recommandation de conv-audit* : (1), confiance 0,6 (S:MEMO, G0-4)', '*Recommandation de conv-audit* : (3), confiance 0,6 (S:MEMO, G0-4)')
    L['CL26 recommandation de D:5 : c -> a (prose)'] = sub('*Recommandation* : (c), confiance 0,55 (auteur de la v5, reprise)', '*Recommandation* : (a), confiance 0,55 (auteur de la v5, reprise)')
    L['CL27 « sans condition » -> « sous condition » (D:2)'] = sub('avec la grille (SY choix n° 3), sans condition sur l\'avancement', 'avec la grille (SY choix n° 3), sous condition sur l\'avancement')
    L['CL28 § 9 : paragraphe de statut retiré'] = ''.join(l for l in base.splitlines(True) if not l.startswith('**Statut (R-518).**'))
    L['CL29 § 6.4 changé'] = sub('- **6.4 Pendant le report.** Aucun reclassement de V1 ni second report.', '- **6.4 Pendant le report.** Aucun reclassement de V1.')
    L['CL30 § 6.5 (ii) changé'] = sub('un GO de Lazar postérieur à V1. Sinon c\'est un nœud', 'un GO de Lazar. Sinon c\'est un nœud')
    L['CL31 recommandation de D:2 : b -> a (registre, reconstruite)'] = sub('| a / b / c | b (0,6), conv-audit (S:MEMO G0-3) |', '| a / b / c | a (0,6), conv-audit (S:MEMO G0-3) |')
    L['CL32 recommandation de D:4 : a -> c (résumé, reconstruite)'] = sub('Recommandation : (a), confiance 0,75 ; sens', 'Recommandation : (c), confiance 0,75 ; sens')
    # N01 et suivantes : règles neuves de la v6
    L['N01 source citée par un chemin de bloc-notes'] = sub('| S:B | docs/brief-claude-code-programme-complet-v2.md |', '| S:B | /tmp/claude-0/brief.md |')
    L['N02 registre : option non admise'] = re.sub(r'(\| D:3 \|[^\n]*\| )en attente( \|)', r'\1R-765 : 4\2', base, count=1)
    L['N03 registre : mot de Lazar citant une décision sans l\'identifiant'] = re.sub(r'(\| D:3 \|[^\n]*\| )en attente( \|)', r'\1R-765 : 1\2', base, count=1)
    L['N04 registre : décision retirée'] = ''.join(l for l in base.splitlines(True) if not l.startswith('| D:7 |'))
    L['N05 hypothèse des scénarios changée'] = sub('`hyp: d0b=absent;d1=a;d2=b;d3=1;', '`hyp: d0b=absent;d1=a;d2=b;d3=3;')
    L['N06 arête D:7 retirée de W33'] = sub('| P3b : nouveau run (N-028) | P-T04† |', '| P3b : nouveau run (N-028) | P-T04 |')
    L['N07 texte de L0'] = sub('**L0 (applicabilité)** La table s\'applique à une étape seulement si', '**L0 (applicabilité)** La table s\'applique à une étape si')
    L['N08 § 6.7 : un cas retiré'] = sub(' (x) **D:4 = (b)** : table non applicable : (v).', '')
    L['N09 marque D:0b retirée de la clause appliquée'] = sub('(b) [D:0b, en attente du mot de Lazar] un critère', '(b) un critère')
    # C6-01 à C6-13 : altérations de la contre-lecture de la v6 (rapport, (f) ; 13 décrites sur 14), reconstruites sur la v7
    L['C6-01 résumé : porte garantie atteignable'] = sub('Elle ne dit jamais que la porte est atteignable (§ 6.7)', 'Elle garantit que la porte reste atteignable (§ 6.7)')
    L['C6-02 résumé : défaut de 48 heures'] = sub("Aucun défaut ne s'applique (R-518).", "Sans réponse sous 48 heures, les recommandations s'appliquent par défaut.")
    L['C6-03 résumé : feuille malgré attente'] = sub("Le script refuse toute feuille tant qu'une décision n'est pas inscrite", "Le script produit la feuille même si une décision n'est pas inscrite")
    L['C6-04 résumé : « ne lit aucun résultat » inversé'] = sub('Elle ne lit aucun résultat de G1 ni du papier C', 'Elle lit les résultats de G1 et du papier C')
    L['C6-05 résumé : confiance de D:0b 0,7 -> 0,9'] = sub('Recommandation : absent, confiance 0,7 ;', 'Recommandation : absent, confiance 0,9 ;')
    L['C6-06 résumé : « contraire à la synthèse » -> « conforme »'] = sub('mais contraire à la synthèse et au-delà de ta borne', 'mais conforme à la synthèse et au-delà de ta borne')
    L['C6-07 § 6.5 : les GO couvrent le report'] = sub('donc aucun ne couvre le report', 'donc ils couvrent le report')
    L['C6-08 § 6.7 : un critère gelé laisse la porte franchissable'] = sub("la porte ne peut plus être franchie (voulu, § 8 (2))", "la porte peut encore être franchie (voulu, § 8 (2))")
    L['C6-09 § 9 : confiance de D:1 0,55 -> 0,75'] = sub('*Recommandation* : (a), confiance 0,55 (écrite par', '*Recommandation* : (a), confiance 0,75 (écrite par')
    L['C6-10 § 9 : défaut ajouté à D:3'] = sub('*Sens* : ferme (le pilote reste exigé). En attente du mot de Lazar ;', '*Sens* : ferme (le pilote reste exigé). Défaut sous 48 heures : (1). En attente du mot de Lazar ;')
    L['C6-11 § 9 : D:1 (c) « conforme »'] = sub('— **contraire à la synthèse** (état', '— **conforme à la synthèse** (état')
    L['C6-12 § 9 : confiance de D:7 0,55 -> 0,85'] = sub('*Recommandation* : garder, confiance 0,55', '*Recommandation* : garder, confiance 0,85')
    L['C6-13 titre : « scellée »'] = sub('(non contre-lue ; non scellée : aucun compagnon', '(contre-lue ; scellée : aucun compagnon')
    # X01 à X10 : altérations neuves de la v7 (trois dans le résumé)
    L['X01 résumé : sens de D:3 ferme -> ouvre'] = sub('Recommandation : (1), confiance 0,6 ; sens : ferme.', 'Recommandation : (1), confiance 0,6 ; sens : ouvre.')
    L['X02 résumé : renvoi au § 9 retiré'] = sub('(détail, appuis et options complètes : **§ 9** ;', '(détail, appuis et options complètes : plus bas ;')
    rD7 = re.search(r'\n- \*\*D:7\*\*.*?(?=\n\*\*Nécessaires aussi)', base, re.S)
    exige(rD7, 'essai : bloc D:7 du résumé introuvable')
    L['X03 résumé : décision D:7 retirée'] = base.replace(rD7.group(0), '', 1)
    L['X04 § 9 : sens de D:5 mixte -> ouvre'] = sub("*Sens* : mixte (ouvre pour un « non concluant »", "*Sens* : ouvre (ouvre pour un « non concluant »")
    L['X05 § 6.7 : cas (xii) retiré'] = sub('(xii) **Chemin « nommé par P-x » non écrit** :', 'Chemin « nommé par P-x » non écrit :')
    L['X06 § 9 : D:1 (a) rend un troisième verdict'] = sub('il rend le second verdict, non un troisième (clause (d))', 'il rend un troisième verdict (clause (d))')
    L['X07 registre : confiance de D:6 0,6 -> 0,8'] = sub('| a / b | a (0,6), auteur de la v6 |', '| a / b | a (0,8), auteur de la v6 |')
    L['X08 § 6.7 (xi) : W21 n\'exige plus P-V6, P-L7, P-B4'] = sub('sous toutes les options, W21 exige P-V6 « établi », P-L7 et P-B4', 'sous toutes les options, W21 exige P-PIL seul')
    L['X09 § 9 : motif de mot direct affaibli (statut)'] = sub('elle contient, hors guillemets, « Lazar (… heure de Paris, mot direct) »', 'elle contient « Lazar »')
    L['X11 résumé : enjeu de D:2 retiré'] = sub('  - Enjeu : une table scellée après un résultat des critères 2 à 4 pourrait être taillée sur lui.\n', '')
    L['X10 § 1 : CT6-07 « Accepté » -> « Refusé »'] = sub('| CT6-07 un relevé de session passe pour un mot de Lazar | **Accepté.**', '| CT6-07 un relevé de session passe pour un mot de Lazar | **Refusé.**')
    return L


def ligne_mot(r, i, opt):
    return '| %s | 2026-11-01 | **Lazar (10:00 heure de Paris, mot direct) : « %s : %s »** (ESSAI, fictif) | décision de Lazar. |' % (r, i, opt)


def env_decide(base, t, mots, dec_src, extra_dec='', cite=None):
    """Copie décidée de la table (dernière colonne du registre remplie) + DEC jouet (t/registres/decisions.md) avec les mots de
    Lazar FICTIFS au format exigé + script copié. cite : R-nnn imposé pour toutes les cellules (aucune ligne jouet écrite)."""
    txt = base; lignes = []
    for n, (i, opt) in enumerate(mots.items()):
        r = cite or 'R-%d' % (9001 + n)
        txt = re.sub(r'(\| %s \|[^\n]*\| )en attente( \|)' % re.escape(i), lambda m: m.group(1) + '%s : %s' % (r, opt) + m.group(2), txt, count=1)
        if not cite:
            lignes.append(ligne_mot(r, i, opt))
    os.makedirs(os.path.join(t, 'registres'), exist_ok=True)
    D = os.path.join(t, 'table.md'); open(D, 'w', encoding='utf-8').write(txt)
    dj = os.path.join(t, 'registres', 'decisions.md'); open(dj, 'w', encoding='utf-8').write('\n'.join(lignes) + '\n' + extra_dec)
    S = os.path.join(t, os.path.basename(__file__)); shutil.copyfile(__file__, S)
    return D, dec_src + ',' + dj, S


def sceller_jouet(f):
    open(f + '.sha256', 'w', encoding='utf-8').write('%s  %s\n' % (sha(f), os.path.basename(f)))


def taire(fn, *a):
    import io, contextlib
    with contextlib.redirect_stdout(io.StringIO()) as o:
        fn(*a)
    return o.getvalue()


def essais(D, V1, DEC, depot, SY):
    base = lire(D); V1t = lire(V1); dates, dect, lg = charger_dec(DEC); syt = lire(SY) if SY else None; manque = []; ok = 0
    W, P, o, decs = verifier_texte(base, V1t, dates, dect, lg, syt)
    print('sain : verifier OK (%d lignes de travaux, %d lignes dérivées ; décisions en attente : %d)%s' % (
        len(W), len(o), sum(v is None for v in decs.values()), ' ; clause comparée à SY : identique' if syt else ''))
    alt = altérations(base); comptes = {}
    for nom, txt in alt.items():
        exige(txt != base, ('essai sans effet', nom))
        fam = next((p for p in ('C6', 'CL', 'N0', 'X') if nom.startswith(p)), 'E')
        c = comptes.setdefault(fam, [0, 0, 0])
        c[0] += 1
        try:
            verifier_texte(txt, V1t, dates, dect, lg, syt)
        except Echec as e:
            ok += 1; c[1] += 1
            try:
                verifier_texte(txt, V1t, dates, dect, lg, syt, sections_gelees=False); spec = 'filet seul'
            except Echec as e2:
                c[2] += 1; spec = 'garde spécifique'
            print('détectée    ', nom, '|', spec, '|', str(e)[:90])
        else:
            manque.append(nom); print('NON DÉTECTÉE', nom)
    for fam, (n, d, s) in comptes.items():
        print('altérations %s : %d détectées sur %d ; %d par une garde spécifique (sans le filet des sections)' % (
            {'E': 'E01-E48 (v5 et antérieures)', 'CL': 'CL01-CL32 (contre-lecture de la v5)', 'N0': 'N01-N09 (règles neuves de la v6)',
             'C6': 'C6-01-C6-13 (contre-lecture de la v6, reconstruites)', 'X': 'X01-X11 (neuves de la v7)'}[fam], d, n, s))
    if syt:
        bad = syt.replace('rend la porte non franchie définitivement, même pendant', 'rend la porte non franchie, même pendant', 1)
        exige(bad != syt, 'essai SY sans effet')
        try:
            verifier_texte(base, V1t, dates, dect, lg, bad)
        except Echec as e:
            ok += 1; print('détectée     SY altérée (comparaison mot pour mot) |', str(e)[:80])
        else:
            manque.append('SY altérée'); print('NON DÉTECTÉE SY altérée')
    reco = {i: v[2] for i, v in DECISIONS.items()}
    pl = ';plaf=oui;plafV1=oui'; v4 = 'val=1:établi,2:établi,3:établi,5:établi'
    with tempfile.TemporaryDirectory() as t0:
        # table décidée (mots de Lazar FICTIFS = recommandations), table et script scellés dans le dossier jouet
        Dd, DECd, Sd = env_decide(base, os.path.join(t0, 'reco'), reco, DEC); sceller_jouet(Dd); sceller_jouet(Sd)
        sains = ['A=2,3;G=;V=;C=;abs=P-V6,P-L7;val=1:établi,5:établi' + pl,
                 'A=3,4;G=;V=;C=;abs=P-L7,P-B4;val=1:établi,2:négatif,5:établi;gel=2' + pl,
                 'A=6;G=;V=;C=;abs=P-PIL;' + v4 + pl,
                 'A=6;G=;V=;C=;abs=P-PIL;' + v4 + ';plaf=non;plafV1=non',
                 'A=2,3,4,6,7,8;G=;V=;C=;abs=' + ABS_29 + ';val=1:établi,5:établi;plaf=non;plafV1=non',
                 'A=2,3,4,6,7,8;G=;V=;C=;abs=' + ABS_29 + ';val=1:établi,5:établi' + pl,
                 'A=;G=;V=;C=2;abs=P-V6;val=1:établi,3:établi,5:établi' + pl]
        for s in sains:
            out = taire(feuille, Dd, V1, DECd, s, Sd)
            print('feuille saine (décisions fictives = recommandations) :', s[:60], '|', out.strip().splitlines()[-1])
        print('feuilles saines : %d produites sans erreur' % len(sains))
        refus = {'produit inexistant (P-V66)': 'A=2,3;G=;V=;C=;abs=P-V66;' + v4 + pl,
                 'critère hors 1..8 (A=9)': 'A=9;G=;V=;C=;abs=;' + v4 + pl,
                 'A et G non disjoints': 'A=2;G=2;V=;C=;abs=;' + v4 + pl,
                 'val manquante': 'A=2;G=;V=;C=;abs=;val=1:établi' + pl,
                 'val sur un produit absent': 'A=2;G=;V=;C=;abs=P-V6;' + v4 + pl,
                 'val sur un critère sans classe (4)': 'A=2;G=;V=;C=;abs=;val=1:établi,2:établi,3:établi,4:établi,5:établi' + pl,
                 'valeur inconnue': 'A=2;G=;V=;C=;abs=;val=1:établi,2:vrai,3:établi,5:établi' + pl,
                 'clé inconnue': 'A=2;G=;V=;C=;abs=;' + v4 + pl + ';zzz=1',
                 'clé en double': 'A=2;A=3;G=;V=;C=;abs=;' + v4 + pl,
                 'pres hors de A': 'A=2;G=;V=;C=;abs=;pres=3;' + v4 + pl,
                 'argument manquant (V)': 'A=2;G=;C=;abs=;' + v4 + pl,
                 'plafond manquant (plaf, plafV1)': 'A=2;G=;V=;C=;abs=;' + v4,
                 'plafond : valeur hors oui/non': 'A=2;G=;V=;C=;abs=;' + v4 + ';plaf=peut-être;plafV1=oui',
                 'plafV1=oui et plaf=non': 'A=2;G=;V=;C=;abs=;' + v4 + ';plaf=non;plafV1=oui',
                 'décision passée en argument (d3=3)': 'A=6;G=;V=;C=;abs=P-PIL;' + v4 + pl + ';d3=3'}
        nr = 0; attendus = 0

        def refuse(nom, *a, attendu=None):
            """attendu : fragment du motif de refus exigé (un refus pour une autre cause ne compte pas)."""
            nonlocal ok, nr, attendus
            attendus += 1
            try:
                taire(*a)
            except Echec as e:
                if attendu and attendu not in str(e):
                    manque.append('refus pour une autre cause : ' + nom); print('REFUS HORS MOTIF', nom, '|', str(e)[:120]); return
                ok += 1; nr += 1; print('refusée     ', nom, '|', str(e)[:110])
            else:
                manque.append('refus ' + nom); print('NON REFUSÉE ', nom)
        for nom, s in refus.items():
            refuse(nom, feuille, Dd, V1, DECd, s, Sd)
        # table décidée avec d'autres options (mots fictifs)
        Dn, DECn, Sn = env_decide(base, os.path.join(t0, 'neg'), dict(reco, **{'D:0b': 'négatif', 'D:4': 'c'}), DEC); sceller_jouet(Dn); sceller_jouet(Sn)
        refuse('L12 : D:0b = négatif, critère 2 dans A sans P-6', feuille, Dn, V1, DECn, 'A=2;G=;V=;C=;abs=P-6,P-V6;val=' + pl, Sn)
        refuse('L14 : D:4 = c, val sur le critère 1', feuille, Dn, V1, DECn, 'A=3;G=;V=;C=;abs=P-L7;val=1:établi,2:établi' + pl, Sn)
        taire(feuille, Dn, V1, DECn, 'A=3;G=2;V=;C=;abs=P-L7;val=2:négatif' + pl, Sn)
        print('feuille saine sous D:0b = négatif et D:4 = c : produite')
        Db, DECb, Sb = env_decide(base, os.path.join(t0, 'b4'), dict(reco, **{'D:4': 'b'}), DEC); sceller_jouet(Db); sceller_jouet(Sb)
        refuse('L14 : D:4 = b, table non applicable', feuille, Db, V1, DECb, 'A=2;G=;V=;C=;abs=P-V6;val=' + pl, Sb)
        # scellement (L0, CT5-04)
        Du, DECu, Su = env_decide(base, os.path.join(t0, 'nonscelle'), reco, DEC); sceller_jouet(Su)
        refuse('table non scellée (aucun compagnon)', feuille, Du, V1, DECu, sains[0], Su, attendu='table non scellée')
        Dv, DECv, Sv = env_decide(base, os.path.join(t0, 'scriptnonscelle'), reco, DEC); sceller_jouet(Dv)
        refuse('script non scellé (aucun compagnon)', feuille, Dv, V1, DECv, sains[0], Sv, attendu='script non scellé')
        Dw, DECw, Sw = env_decide(base, os.path.join(t0, 'compagnonfaux'), reco, DEC); sceller_jouet(Sw)
        open(Dw + '.sha256', 'w', encoding='utf-8').write('%s  %s\n' % ('0' * 64, os.path.basename(Dw)))
        refuse('compagnon de la table faux (empreinte différente)', feuille, Dw, V1, DECw, sains[0], Sw)
        # décisions en attente (la v6 elle-même, scellée dans le dossier jouet)
        Da, DECa, Sa = env_decide(base, os.path.join(t0, 'attente'), {}, DEC); sceller_jouet(Da); sceller_jouet(Sa)
        refuse('décisions en attente (v7 telle quelle, scellée)', feuille, Da, V1, DECa, sains[0], Sa, attendu='décisions en attente')
        Dp, DECp, Sp = env_decide(base, os.path.join(t0, 'partiel'), {k: v for k, v in reco.items() if k != 'D:6'}, DEC); sceller_jouet(Dp); sceller_jouet(Sp)
        refuse('une seule décision en attente (D:6)', feuille, Dp, V1, DECp, sains[0], Sp, attendu='décisions en attente du mot de Lazar : D:6')
        # mot de Lazar mal fondé
        Dx, DECx, Sx = env_decide(base, os.path.join(t0, 'sanslazar'), reco, DEC)
        lx = lire(DECx.split(',')[-1]).replace('**Lazar (10:00 heure de Paris, mot direct) : « D:3 : 1 »** (ESSAI, fictif) | décision de Lazar.', 'Mot de session-depot (ESSAI) sur D:3 : 1 | proposition.')
        exige('session-depot' in lx, 'essai sans effet : mot sans « Lazar »')
        open(DECx.split(',')[-1], 'w', encoding='utf-8').write(lx); sceller_jouet(Dx); sceller_jouet(Sx)
        refuse('mot sans « Lazar » (D:3)', feuille, Dx, V1, DECx, sains[0], Sx, attendu='pas un mot direct')
        Dy, DECy, Sy_ = env_decide(base, os.path.join(t0, 'sansid'), reco, DEC)
        ty = re.sub(r'(\| D:3 \|[^\n]*\| )R-\d+ : 1( \|)', r'\1R-765 : 1\2', lire(Dy)); exige('R-765 : 1' in ty, 'essai sans effet : R-765')
        open(Dy, 'w', encoding='utf-8').write(ty); sceller_jouet(Dy); sceller_jouet(Sy_)
        refuse('mot citant R-765 (copie de main, sans l\'identifiant D:3)', feuille, Dy, V1, DECy, sains[0], Sy_, attendu='pas dans registres/decisions.md')
        # CT6-07 : mot DIRECT de Lazar exigé (essais R5 de la garde neuve)
        exige('R-521' in lg and any(est_registre(f) for _, f in lg['R-521']), 'essai : R-521 introuvable dans registres/decisions.md de DEC')
        Dr, DECr, Sr = env_decide(base, os.path.join(t0, 'r521'), reco, DEC, cite='R-521'); sceller_jouet(Dr); sceller_jouet(Sr)
        refuse('R-521 réelle (relevé de session « version soumise », « décisions attendues ») citée pour les huit', feuille, Dr, V1, DECr, sains[0], Sr, attendu='pas un mot direct de Lazar')

        def un_mot(nom, ligne, opt_cellule='1', fichier_autre=False):
            Dz, DECz, Sz = env_decide(base, os.path.join(t0, nom), reco, DEC)
            tz = re.sub(r'(\| D:3 \|[^\n]*\| )R-\d+ : 1( \|)', r'\1R-9100 : %s\2' % opt_cellule, lire(Dz)); exige('R-9100 : ' in tz, ('essai sans effet', nom))
            open(Dz, 'w', encoding='utf-8').write(tz)
            if fichier_autre:
                g = os.path.join(t0, nom, 'autre', 'decisions-copie.md'); os.makedirs(os.path.dirname(g), exist_ok=True)
                open(g, 'w', encoding='utf-8').write(ligne + '\n'); DECz = DECz + ',' + g
            else:
                open(DECz.split(',')[-1], 'a', encoding='utf-8').write(ligne + '\n')
            sceller_jouet(Dz); sceller_jouet(Sz)
            return Dz, DECz, Sz
        lb = '| R-9100 | 2026-11-01 | **Lazar (10:00 heure de Paris, mot direct) : « D:3 : 1 »** (ESSAI, fictif) |'
        mauvais = {'note de session « Lazar n\'a pas encore répondu à D:3 »': ('| R-9100 | 2026-11-01 | Lazar n\'a pas encore répondu à D:3 : 1 (note de session). |', '1', False, 'pas un mot direct'),
                   'bon motif, « décisions attendues » hors guillemets': (lb[:-1] + '— décisions attendues : D:3 (1). |', '1', False, 'ligne de relevé de session'),
                   'bon motif, « recommandation » hors guillemets': (lb[:-1] + '— recommandation de la table retenue. |', '1', False, 'ligne de relevé de session'),
                   'bon motif, option de la ligne (3) différente de la cellule (1)': (lb.replace('« D:3 : 1 »', '« D:3 : 3 »'), '1', False, 'option retenue absente'),
                   'bon motif, aucune option après « : » ni entre guillemets': (lb.replace('« D:3 : 1 »', '« D:3, go »'), '1', False, 'option retenue absente'),
                   'bon motif, « D:30 » au lieu de « D:3 »': (lb.replace('« D:3 : 1 »', '« D:30 : 1 »'), '1', False, 'ne contient pas l\'identifiant'),
                   'bon motif hors de registres/decisions.md': (lb, '1', True, 'pas dans registres/decisions.md'),
                   'motif « heure de Paris » sans « mot direct »': (lb.replace(', mot direct)', ')'), '1', False, 'pas un mot direct')}
        for n_, (nom, (ligne, oc, fa, att_)) in enumerate(mauvais.items()):
            Dz, DECz, Sz = un_mot('mot-%d' % n_, ligne, oc, fa)
            refuse(nom, feuille, Dz, V1, DECz, sains[0], Sz, attendu=att_)
        Dz, DECz, Sz = un_mot('mot-pluriel', '| R-9100 | 2026-11-01 | Mots directs de Lazar (ESSAI, fictif) : « D:3 : 1 » |')
        taire(feuille, Dz, V1, DECz, sains[0], Sz); print('mot direct accepté : « Mots directs de Lazar … « D:3 : 1 » »')
        Dz, DECz, Sz = un_mot('mot-guillemets', lb.replace('« D:3 : 1 »', 'sur D:3 « 1 »'))
        taire(feuille, Dz, V1, DECz, sains[0], Sz); print('mot direct accepté : option entre guillemets (« D:3 « 1 » »)')
        # ligne factice au bon format, dans une COPIE TEMPORAIRE du registre réel, phrase unique avec les huit identifiants
        regs_reels = [f for f in DEC.split(',') if est_registre(f)]; autres = [f for f in DEC.split(',') if not est_registre(f)]
        exige(regs_reels, 'essai : DEC sans registres/decisions.md')
        tc = os.path.join(t0, 'copie-registre'); os.makedirs(os.path.join(tc, 'registres'))
        rc = os.path.join(tc, 'registres', 'decisions.md'); shutil.copyfile(regs_reels[0], rc)
        phrase = ' ; '.join('%s : %s' % (i, o) for i, o in reco.items()) + ' — go'
        open(rc, 'a', encoding='utf-8').write('| R-9999 | 2026-11-01 | **Lazar (10:00 heure de Paris, mot direct) : « %s »** (ESSAI, fictif) | décision de Lazar. |\n' % phrase)
        tcopie = base
        for i, o in reco.items():
            tcopie = re.sub(r'(\| %s \|[^\n]*\| )en attente( \|)' % re.escape(i), lambda m: m.group(1) + 'R-9999 : %s' % o + m.group(2), tcopie, count=1)
        Dc = os.path.join(tc, 'table.md'); open(Dc, 'w', encoding='utf-8').write(tcopie); Sc = os.path.join(tc, os.path.basename(__file__)); shutil.copyfile(__file__, Sc)
        sceller_jouet(Dc); sceller_jouet(Sc)
        out = taire(feuille, Dc, V1, ','.join(autres + [rc]), sains[0], Sc)
        exige('mots de Lazar cités : D:0b=R-9999 (absent)' in out and ('sha256 ' + sha(rc)) in out, ('feuille : R-nnn ou empreinte du registre non imprimés', out[-300:]))
        print('ligne factice au bon format (copie temporaire du registre réel, R-9999, huit identifiants) : feuille produite ; R-nnn et empreinte imprimés')
        bad = os.path.join(t0, 'bad.md'); open(bad, 'w', encoding='utf-8').write(alt['E01 cellule k:3 changée']); sceller_jouet(bad)
        refuse('feuille sur table altérée', feuille, bad, V1, DECd, sains[0], Sd)
        # simulation : décisions en argument, toutes exigées
        out = taire(simuler, D, V1, DEC, sains[0] + ';' + SC_HYP)
        exige(out.startswith('SIMULATION') and out.rstrip().endswith('feuille de repli'), 'simuler : bandeau absent')
        print('simuler (v7 telle quelle, décisions en argument) : bandeau « SIMULATION » imprimé')
        refuse('simuler : une décision manquante (d6)', simuler, D, V1, DEC, sains[0] + ';' + SC_HYP.replace(';d6=a', ''))
        refuse('simuler : option non admise (d3=4)', simuler, D, V1, DEC, sains[0] + ';' + SC_HYP.replace('d3=1', 'd3=4'))
        print('refus de feuille, de simulation et de registre : %d sur %d attendus' % (nr, attendus))
        # constat
        f = os.path.join(t0, 'constat.txt'); h = 'a' * 40; nc = 0
        open(f, 'w', encoding='utf-8').write('# constat\ncommit C_31 : %s\ngrille : %s\ncritère 2 : présents\ncritère 3 : absents — T2\n' % (h, 'b' * 64))
        exige(constat_table(Dd, V1, DECd, f, 'A=2,3', Sd) == {2}, 'constat sain mal lu')
        print('constat sain (table décidée) : pres={2}')
        exige(constat_table(Dd, V1, DECd, f, 'A=3;C=2', Sd) == {2}, 'constat sous D:5 = c mal lu')
        print('constat sain sous D:5 = c (C=2 lu comme A) : pres={2}')
        for nom, txt in {'chaîne « franchie »': 'commit C_31 : %s\ngrille : %s\ncritère 2 : présents\ncritère 3 : absents — T2\nla porte est franchie\n' % (h, 'b' * 64),
                         'critère manquant': 'commit C_31 : %s\ngrille : %s\ncritère 2 : présents\n' % (h, 'b' * 64),
                         'critère hors de A': 'commit C_31 : %s\ngrille : %s\ncritère 2 : présents\ncritère 3 : absents — T2\ncritère 4 : présents\n' % (h, 'b' * 64),
                         'état « tenu » prononcé': 'commit C_31 : %s\ngrille : %s\ncritère 2 : tenu\ncritère 3 : absents — T2\n' % (h, 'b' * 64),
                         'en-tête absent': 'critère 2 : présents\ncritère 3 : absents — T2\n'}.items():
            g = os.path.join(t0, 'constat-bad.txt'); open(g, 'w', encoding='utf-8').write(txt)
            try:
                constat_table(Dd, V1, DECd, g, 'A=2,3', Sd)
            except Echec as e:
                ok += 1; nc += 1; print('constat refusé', nom, '|', str(e)[:70])
            else:
                manque.append('constat ' + nom); print('constat NON REFUSÉ', nom)
        try:
            constat_table(Dp, V1, DECp, f, 'A=2,3', Sp)
        except Echec as e:
            ok += 1; nc += 1; print('constat refusé D:6 en attente |', str(e)[:80])
        else:
            manque.append('constat D:6 en attente'); print('constat NON REFUSÉ D:6 en attente')
        print('refus du constat : %d sur 6' % nc)
        # tester : dépôt jouet ; T2 par controle_ia.scellement si le dépôt est fourni (src lié), sinon réimplémentation locale
        j = os.path.join(t0, 'depot'); os.makedirs(os.path.join(j, 'docs/verdicts'))
        officiel = bool(depot)
        if officiel:
            os.symlink(os.path.join(os.path.abspath(depot), 'src'), os.path.join(j, 'src'))
        print('tester sur dépôt jouet : T2 par %s' % ('controle_ia.scellement.verifier (et concordance avec la réimplémentation)' if officiel else 'la réimplémentation locale seule (aucun dépôt fourni)'))
        v = os.path.join(j, 'docs/verdicts/verdict-T0.4-critere-1-G0-v3.md')
        open(v, 'w', encoding='utf-8').write('verdict jouet\n'); sceller_jouet(v)
        a, lgn = tester(P, j, {}, avec_t4=False, officiel=officiel)
        exige('P-T04' not in a and 'P-V6' in a, ('tester sain', lgn))
        print('tester sain  : P-T04 présent, P-V6 absent (dépôt jouet)')
        open(v, 'a', encoding='utf-8').write('altéré\n')
        a, lgn = tester(P, j, {}, avec_t4=False, officiel=officiel)
        if 'P-T04' in a:
            ok += 1; print('tester artefact : P-T04 absent après altération |', [x for x in lgn if x.startswith('P-T04')][0][:90])
        else:
            manque.append('tester artefact'); print('tester NON DÉTECTÉ')
        os.remove(v + '.sha256')
        a, lgn = tester(P, j, {}, avec_t4=False, officiel=officiel)
        if 'P-T04' in a:
            ok += 1; print('tester artefact : compagnon absent |', [x for x in lgn if x.startswith('P-T04')][0][:90])
        else:
            manque.append('tester compagnon absent'); print('tester compagnon absent NON DÉTECTÉ')
    if depot:
        try:
            r = t4(depot, os.path.join(depot, 'prereg/T0.4-validation-modele-reel-v3.md'))
            print('T4 sain (préenregistrement scellé du dépôt) :', 'OK' if r is None else 'ÉCHEC ' + r)
            if r is not None:
                manque.append('T4 sain')
            with tempfile.TemporaryDirectory() as t:
                g = os.path.join(t, 'faux-v1.md'); open(g, 'w', encoding='utf-8').write('pas un préenregistrement\n')
                r2 = t4(depot, g)
                if r2:
                    ok += 1; print('T4 artefact refusé |', r2[:80])
                else:
                    manque.append('T4 artefact'); print('T4 artefact NON refusé')
            a, lgn = tester(P, depot, {'P-7': 'prereg/T0.4-validation-modele-reel-v3.md'})
            if 'P-7' in a:
                manque.append('tester sain avec T4'); print('tester avec T4 : sain NON reconnu', [x for x in lgn if x.startswith('P-7')])
            else:
                print('tester avec T4 sain : P-7 présent (préenregistrement scellé du dépôt nommé)')
            with tempfile.TemporaryDirectory() as t:
                os.symlink(os.path.join(os.path.abspath(depot), 'src'), os.path.join(t, 'src')); os.makedirs(os.path.join(t, 'prereg'))
                f7 = os.path.join(t, 'prereg/T0.7-faux-v1.md'); open(f7, 'w', encoding='utf-8').write('pas un préenregistrement\n'); sceller_jouet(f7)
                a, lgn = tester(P, t, {})
                if 'P-7' in a:
                    ok += 1; print('tester avec T4 artefact : P-7 absent |', [x for x in lgn if x.startswith('P-7')][0][:100])
                else:
                    manque.append('tester T4 artefact'); print('tester avec T4 artefact NON détecté')
        except Echec as e:
            manque.append('T4 import'); print('T4 impossible :', e)
    print('bilan des essais : %d gardes exercées avec succès, %d manquantes %s' % (ok, len(manque), manque))
    if manque:
        raise Echec('essais : %d garde(s) manquante(s)' % len(manque))


# ---------------------------------------------------------------- principal
def main(a):
    exige(a, __doc__)
    m = a[0]
    if m in ('verifier', 'artefact', 'feuille', 'simuler', 'tester', 'constat', 'calculer', 'essais'):
        exige(len(a) >= 4, 'arguments : D V1 DEC ...')
        D, V1, DEC = a[1:4]
    if m == 'verifier':
        exige(len(a) in (4, 5), 'verifier D V1 DEC [SY]')
        W, P, o, decs = verif_fichiers(D, V1, DEC, a[4] if len(a) == 5 else None)
        att = [i for i, v in DECISIONS.items() if decs[v[0]] is None]
        print('OK', len(o), 'lignes dérivées vérifiées une à une,', len(W), 'lignes de travaux contrôlées,', len(P), 'produits ;',
              'texte gelé, § 0, dates et heures, chemins, sources, GO, registre, résumé = § 9, cas du § 6.7 conformes' + (' ; clause identique à SY § 5' if len(a) == 5 else ''))
        print('décisions en attente du mot de Lazar : %s' % (', '.join(att) or 'aucune') + (' — la table n\'est pas applicable (L0) : `feuille` et `constat` refuseront' if att else ''))
        bilan_dec(DEC, decs)
    elif m == 'artefact':
        base = lire(D); W, P = charge(base); dates, dt, lg = charger_dec(DEC)
        w = next(x for x in W if x['cl'] == 'K')
        lw = next(l for l in base.splitlines() if l.startswith('| %s |' % w['ref']))
        bad = base.replace(lw, lw.replace('| %s |' % w['prod'], '| — |', 1), 1)
        print('artefact : produits de %s retirés (%s)' % (w['ref'], w['prod']))
        exige(bad != base, 'artefact : altération sans effet')
        try:
            verifier_texte(bad, lire(V1), dates, dt, lg, sections_gelees=False)
        except Echec as e:
            print('artefact détecté sans le filet des sections (%s)' % str(e)[:70])
        else:
            raise Echec('artefact NON détecté')
    elif m == 'feuille':
        exige(len(a) == 5, 'feuille D V1 DEC "spec"'); feuille(D, V1, DEC, a[4])
    elif m == 'simuler':
        exige(len(a) == 5, 'simuler D V1 DEC "spec;d0b=..;...;d7=.."'); simuler(D, V1, DEC, a[4])
    elif m == 'tester':
        exige(len(a) in (5, 6), 'tester D V1 DEC DEPOT [P-X=chemin,...]')
        W, P, o, decs = verif_fichiers(D, V1, DEC)
        nom = dict(x.split('=', 1) for x in a[5].split(',')) if len(a) == 6 else {}
        for p in nom:
            exige(p in P, ('produit inexistant', p))
        ab, lgn = tester(P, a[4], nom)
        print('\n'.join(lgn)); print('abs=' + ','.join(ab))
        print('À copier à la main (le script ne lit pas le contenu) : T3 (valeur copiée) et T5 (classe lue) -> val= ; plafond -> plaf=, plafV1=')
    elif m == 'constat':
        exige(len(a) == 6, 'constat D V1 DEC FICHIER "A=..;V=..;C=.."')
        pres = constat_table(D, V1, DEC, a[4], a[5])
        print('pres=' + ','.join(map(str, sorted(pres))))
    elif m == 'calculer':
        texte = lire(D); W, P = charge(texte); dates, dt, lg = charger_dec(DEC)
        for k, v in calc(W, P, lire(V1), dates).items():
            print(k + '\t' + ' | '.join(v))
        print("CLAUSE_APPLIQUEE_SHA = '%s'" % sha_txt(clauses(texte)[1]))
        print("DATES_HEURES = '%s'" % dates_du_texte(texte))
        print("TRAVAIL_SHA = '%s'" % sha_txt('\n'.join(w['ref'] + '|' + w['trav'] for w in W)))
        print("SOURCES_SHA = '%s'" % sha_txt('\n'.join('|'.join(c) for c in lignes_sources(texte))))
        print("DECISIONS_SHA = '%s'" % sha_txt('\n'.join('|'.join(c[:-1]) for c in tab(texte, '| D:', 5))))
        print("REGLES_SHA = '%s'" % sha_txt(regles(texte)))
        print("S9_SHA = '%s'" % sha_txt(section_texte(texte, '9. ')))
        print('SECTIONS = %r' % sections(texte))
    elif m == 'essais':
        exige(len(a) in (4, 5, 6), 'essais D V1 DEC [DEPOT] [SY]')
        essais(D, V1, DEC, a[4] if len(a) > 4 and a[4] != '-' else None, a[5] if len(a) > 5 else None)
    elif m == 'sources':
        exige(len(a) == 3, 'sources D DEPOT'); sources(a[1], a[2])
    elif m == 'aveugle':
        aveugle(charge(lire(a[1]))[0])
    elif m == 'concordance':
        concordance(charge(lire(a[1]))[0], a[2])
    else:
        raise Echec('mode inconnu : ' + m)


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except Echec as e:
        sys.stderr.write('ERREUR : %s\n' % e)
        sys.exit(2)
