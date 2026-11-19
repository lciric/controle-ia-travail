import pathlib, sys, hashlib, subprocess
R = pathlib.Path('/home/user/controle-ia-travail')
D = R/'brouillons/barreau8-lecture-sondes-v1'
B7 = D/'prereg-lecture-sondes-barreau8-v1-brouillon7.md'
P = D/'prereg-lecture-sondes-barreau8-v1-brouillon8.md'
N = D/'differences-brouillon7-brouillon8-v1.md'
assert not P.exists() and not N.exists()
def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
H7 = '8749b51816fca87987c3e163fd0b5e872164812f19287f102f95ad92c7fcf337'
assert sha(B7) == H7
CL7 = 'brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon7-v1.md'
HC7 = 'b62ec7795e8495ed693a3fd8dd2cdbb43219bfb73afb5d735e219d80dfd6194e'
assert sha(R/CL7) == HC7
t = B7.read_text(encoding='utf-8'); fautes = []
def r(a, b, n=1):
    global t
    c = t.count(a)
    if c != n: fautes.append((c, a[:90])); return
    t = t.replace(a, b)
DEBUT = '2026-11-19T01:24Z'
# titre, statut (M-4), auteur, date
r("— v1 — brouillon 7", "— v1 — brouillon 8")
r("**Statut : brouillon 7, non scellé comme préenregistrement.**", "**Statut : brouillon 8, texte soumis au scellement ; il n'est scellé que si son compagnon `.sha256` et la ligne `SCELLEMENT-SONDES-IIB` le disent.**")
r("contre-lecteurs des brouillons 1, 3, 4 et 6 : Opus 5.5", "contre-lecteurs des brouillons 1, 3, 4, 6 et 7 : Opus 5.5")
r("brouillon 7 écrit entre 2026-11-19T01:12Z et 2026-11-19T01:16Z (`date -u`).", "brouillon 7 écrit entre 2026-11-19T01:12Z et 2026-11-19T01:16Z ; brouillon 8 écrit entre " + DEBUT + " et HEURE_DE_FIN (`date -u`).")
# M-4, ligne 52
r("**Il reste deux marqueurs ouverts : F-3 (entropie des graines) et l'entrée « Contre-lecture 4 (finale, texte rempli) » de la section « Contre-lecture ».**", "**Au dernier brouillon, deux marqueurs restaient ouverts, et deux seulement : F-3 (entropie des graines) et l'entrée « Contre-lecture 4 (finale, texte rempli) » de la section « Contre-lecture » ; ils sont remplis au scellement, et rien d'autre ne change.**")
# M-1
r("ou un texte soumis au scellement qui diffère du texte relu par la dernière contre-lecture ailleurs que dans cette entrée", "ou un texte soumis au scellement qui diffère du texte relu par la dernière contre-lecture ailleurs que dans cette entrée et dans la cellule « état et raison » de F-3 (où seule l'entropie tirée remplace le marqueur), constaté par une comparaison faite par programme")
r("**Règle** : le texte scellé ne diffère du texte relu par cette dernière contre-lecture que par cette entrée ;", "**Règle** : le texte scellé ne diffère du texte relu par cette dernière contre-lecture que par cette entrée et par la cellule « état et raison » de F-3, où seule l'entropie tirée remplace le marqueur ;")
# M-2
r("**Si le champ manque, n'est pas un booléen,", "**Si le fichier est absent, si le champ manque, s'il n'est pas un booléen,")
# M-3
r("(b-10) ce bloc de décision : son titre dit « texte écrit sous (a) », et la liste (b-1) à (b-10) reste comme mémoire de la différence.", "(b-10) ce bloc de décision : son titre dit « texte écrit sous (a) » ; (b) y est dite « non retenue » et (a) « appliquée » ; sa « Règle du scellement » dit « Le texte est scellé sous (a). **Après le scellement, aucun défaut n'échoit** : tout passage à (b) est un écart au préenregistrement, nœud de Lazar. » ; la liste (b-1) à (b-10) reste comme mémoire de la différence.")
# entrée de la contre-lecture du brouillon 7
r("- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR", "- **Contre-lecture 3 ter** — sous-agent neuf, modèle Claude Opus 5.5, qui n'a écrit aucun brouillon ni aucune contre-lecture antérieure de ce texte, ni la note d'interface ; contre-lecture de la différence du brouillon 6 au brouillon 7. Brouillon relu : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon7.md`, empreinte `" + H7 + "`. Rapport : `" + CL7 + "`, empreinte `" + HC7 + "`. Conclusion : « PAS PRÊT » sur une liste fermée ; les remarques N-1 à N-11 sont dites réellement appliquées, sans changement hors remarque ; une remarque bloquante (M-1), trois mineures (M-2 à M-4). Traitement de chaque remarque : `brouillons/barreau8-lecture-sondes-v1/differences-brouillon7-brouillon8-v1.md` (empreinte dans son compagnon).\n- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR")
h = subprocess.run(['date','-u','+%Y-%m-%dT%H:%MZ'],capture_output=True,text=True).stdout.strip()
r("HEURE_DE_FIN", h)
for c in ("À REMPLIR — À FIXER : tirée par la session mère au scellement", "- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :", "versée avec l'empreinte du texte scellé."):
    if t.count(c) != 1: fautes.append(('unicité', t.count(c), c))
if t.count("À REMPLIR") != 2: fautes.append(('marqueurs', t.count("À REMPLIR")))
if fautes:
    for f in fautes: print("FAUTE", f)
    sys.exit(1)
P.write_text(t, encoding='utf-8')
N.write_text(f"""# Différences entre le brouillon 7 et le brouillon 8 du texte « lecture des sondes du barreau 8 et passe de recalcul de l'activité interne » — v1

- Brouillon 7 : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon7.md`, empreinte `{H7}`.
- Contre-lecture du brouillon 7 (Opus 5.5, contre-lecteur neuf) : `{CL7}`, empreinte `{HC7}` (vérifiée ; lue en entier).
- Brouillon 8 : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon8.md` (empreinte : son compagnon `.sha256`).
- Rédacteur : Fable 5.2. Écrit le 2026-11-19 entre {DEBUT} et {h} (`date -u` ; mêmes heures que la ligne de date du brouillon 8), par programme, à partir du brouillon 7 : dix remplacements contrôlés (chaque texte cherché doit paraître exactement une fois, sinon rien n'est écrit). Le programme vérifie aussi que les deux chaînes de la procédure de remplissage restent uniques et qu'il reste exactement deux marqueurs.

## Une ligne par remarque

| n° | objet | état | où, dans le brouillon 8 |
|---|---|---|---|
| M-1 (bloquante) | la règle de la dernière contre-lecture interdisait de verser l'entropie après elle | appliquée, textes de remplacement repris mot pour mot (deux remplacements) | liste d'arrêt, ligne 2 ; entrée « Contre-lecture 4 (finale, texte rempli) », « Règle » |
| M-2 (mineure) | garde d'alignement : fichier de configuration du jetoniseur absent | appliquée, mot pour mot | garde P3, clause (b) |
| M-3 (mineure) | passage (b-10) incomplet | appliquée, mot pour mot | bloc de décision « scores par jeton », liste du retour à (a) |
| M-4 (mineure) | le texte scellé dirait « il reste deux marqueurs ouverts » et « non scellé » | appliquée, mot pour mot (trois remplacements) | titre (« brouillon 8 ») ; statut ; phrase des marqueurs de la section « Champs ouverts » |

Remarques refusées ou adaptées : aucune.

## Changements hors remarque (trois, demandés par la conductrice ou de conséquence)

- Ligne de date : le brouillon 8 s'ajoute.
- Section « Contre-lecture » : entrée **« Contre-lecture 3 ter »** ajoutée avant l'entrée 4 (contre-lecture du brouillon 7 : empreintes du brouillon 7 et du rapport). Le motif du validateur (`src/controle_ia/prereg.py`, ligne 29, `^\\s*-?\\s*\\**Contre-lecture (\\d+)\\**`) la reconnaît comme une entrée à part, contrôlée sur son propre segment, comme « 3 bis ».
- En-tête, auteur : « contre-lecteurs des brouillons 1, 3, 4, 6 et 7 ».

Rien d'autre ne change.

## Marqueurs restants et chaînes de la procédure de remplissage

Deux marqueurs, et deux seulement : F-3 (entropie racine des graines) et l'entrée « Contre-lecture 4 (finale, texte rempli) ». Les deux chaînes à remplacer au scellement paraissent chacune une seule fois dans le brouillon 8 : `À REMPLIR — À FIXER : tirée par la session mère au scellement` ; la ligne qui commence par `- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :` et finit par `versée avec l'empreinte du texte scellé.`

Sortie exacte du validateur sur le brouillon 8 : `['section vide ou à remplir : Contre-lecture']`.
""", encoding='utf-8')
print("ok", h, len(t.splitlines()))
