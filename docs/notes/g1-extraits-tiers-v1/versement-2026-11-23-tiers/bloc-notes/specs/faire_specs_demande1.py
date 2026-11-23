"""Spécifications en clair (hors dépôt) des extraits de la demande 1. Tiers d'extraction G1."""
import json, os, subprocess
S = os.environ['S']; DEP = '/home/user/controle-ia-travail'
CANAL = 'refs/remotes/origin/canal/conv-audit-n04'

def lignes(src, ref):
    b = subprocess.run(['git', 'show', f'{ref}:{src}'], cwd=DEP, check=True, capture_output=True).stdout
    return b.decode('utf-8').split('\n')

def P(L, k, debut, fin=None, inclure_fin=True, eol=False):
    """Passage de la ligne k : de `debut` à `fin` (comprise si inclure_fin) ou à la fin de la ligne."""
    l = L[k - 1]
    assert l.count(debut) == 1, (k, debut)
    s = l.index(debut)
    if fin is None:
        e = len(l) if eol else s + len(debut)
    else:
        assert l.count(fin) >= 1, (k, fin)
        e = l.index(fin, s) + (len(fin) if inclure_fin else 0)
    anc = l[s:e]
    assert l.count(anc) == 1, (k, anc[:50])
    return {"ligne": k, "ancien": anc}

def ecrire(nom, spec):
    json.dump(spec, open(f'{S}/specs/{nom}', 'w'), ensure_ascii=False, indent=2)

# --- brouillon 6 de G1 (main)
src = 'brouillons/G1-preenregistrement-v1-brouillon6.md'; L = lignes(src, 'origin/main')
ps = [
    P(L, 46, "les attentes « à fixer après la borne δ* de P3 »", "; "),
    P(L, 104, " (verdict v3, `63444faa…`)"),
    P(L, 117, " Le brouillon 5 renvoyait plusieurs attentes", eol=True),
    P(L, 123, " ; l'attente globale de l'auteur du brouillon 5 (≈ 0,1 de franchir) est gardée"),
    P(L, 126, "faible : sous le modèle binormal", "[calc § 10]"),
    P(L, 161, " ; P3 : 497 sur 600, soit 0,828, clé `resultat.P3-P6.honnete.valide`"),
    P(L, 179, " (P3 : 0,828)"),
    P(L, 310, " (dans P3, la même situation rendait le jeu non interprétable", "est déjà un comparateur à battre)"),
    P(L, 383, " ; P3 : 0,828"),
    P(L, 391, " ; attente de l'auteur du brouillon 5 ≈ 0,1"),
    P(L, 392, "prévisions binormales tirées des aires de P3 [calc § 4 et § 10] ; "),
    P(L, 422, " le verdict de P3 v2 et `lecture-p3.json` ;"),
]
ecrire('spec-G1-brouillon6-v2.json', {
    "source": src, "ref": "origin/main", "empreinte_attendue": "939b56e540fa49ea",
    "sortie": "docs/notes/g1-extraits-tiers-v1/extrait-G1-brouillon6-v2.md",
    "titre": "brouillon 6 du préenregistrement de G1",
    "objet": "demande 1 du rédacteur successeur : décisions DG1-1 à DG1-13, structure et énoncés, liste d'arrêt S1 à S28, liste numérotée des comparateurs, devis.",
    "plages": [[1, 1], [26, 55], [57, 67], [95, 105], [113, 123], [125, 134], [137, 377], [379, 379], [381, 393], [395, 415], [417, 426]],
    "passages_en_clair": ps, "annexe_sources": False,
    "annexe_termes": ["DG1-", "S28", "k = 12", "6 331", "4 870", "160", "δ = 0,05", "τ = 0,01", "0,05"]})

# --- décisions en clair (branche canal)
src = 'brouillons/G1-decisions-en-clair-v1.md'; L = lignes(src, CANAL)
ps = [
    P(L, 5, " Le rédacteur estime la chance de franchir G1", eol=True),
    P(L, 21, " (P3 : 82,8 %)"),
]
ecrire('spec-G1-decisions-en-clair-v2.json', {
    "source": src, "ref": CANAL, "empreinte_attendue": "48eb66bc6b160cb7",
    "sortie": "docs/notes/g1-extraits-tiers-v1/extrait-G1-decisions-en-clair-v2.md",
    "titre": "les treize décisions DG1-1 à DG1-13 en clair (1er novembre)",
    "objet": "demande 1 du rédacteur successeur.",
    "plages": [[1, 15], [17, 17], [19, 25]], "passages_en_clair": ps})

# --- conception du pari apparié v2 (branche canal)
src = 'brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pari-de-signe/conception-pari-de-signe-v2.md'
L = lignes(src, CANAL)
ecrire('spec-pari-apparie-conception-v2-v1.json', {
    "source": src, "ref": CANAL, "empreinte_attendue": "9c39a73ddbf68127",
    "sortie": "docs/notes/g1-extraits-tiers-v1/extrait-pari-apparie-conception-v2-v1.md",
    "titre": "conception v2 du pari apparié borné",
    "objet": "demande 1 du rédacteur successeur.",
    "plages": [[1, len(L) - (1 if L[-1] == '' else 0)]], "passages_en_clair": []})

# --- calculs du brouillon 5 : script et sortie (branche canal)
src = 'brouillons/preuves-mentors-v1/g1-prereg-v1/calculs-g1-brouillon5-v1.py'; L = lignes(src, CANAL)
ecrire('spec-calculs-g1-brouillon5-script-v2.json', {
    "source": src, "ref": CANAL, "empreinte_attendue": "8021037b8e733127",
    "sortie": "docs/notes/g1-extraits-tiers-v1/extrait-calculs-g1-brouillon5-script-v2.md",
    "titre": "script des calculs du brouillon 5 de G1",
    "objet": "demande 1 du rédacteur successeur : paragraphes 1 à 3 et 5 à 9.",
    "plages": [[1, 63], [92, 193]],
    "passages_en_clair": []})
src = 'brouillons/preuves-mentors-v1/g1-prereg-v1/calculs-g1-brouillon5-v1-sortie.txt'; L = lignes(src, CANAL)
ecrire('spec-calculs-g1-brouillon5-sortie-v1.json', {
    "source": src, "ref": CANAL, "empreinte_attendue": "d53e7e5a81058217",
    "sortie": "docs/notes/g1-extraits-tiers-v1/extrait-calculs-g1-brouillon5-sortie-v1.md",
    "titre": "sortie des calculs du brouillon 5 de G1",
    "objet": "demande 1 du rédacteur successeur : paragraphes 1 à 3 et 5 à 9.",
    "plages": [[1, 31], [65, 118]], "passages_en_clair": []})
print("spécifications écrites")
