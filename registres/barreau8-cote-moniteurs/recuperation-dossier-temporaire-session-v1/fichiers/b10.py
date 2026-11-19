import pathlib, sys, hashlib, subprocess
R = pathlib.Path('/home/user/controle-ia-travail')
D = R/'brouillons/barreau8-lecture-sondes-v1'
B9 = D/'prereg-lecture-sondes-barreau8-v1-brouillon9.md'
P = D/'prereg-lecture-sondes-barreau8-v1-brouillon10.md'
N = D/'differences-brouillon9-brouillon10-v1.md'
assert not P.exists() and not N.exists()
def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
H9 = 'aca110b0635abf9e7e5a1bdd1dc66b94aaae40ad5c72a6e7d6127967f87f272d'
assert sha(B9) == H9
CL9 = 'brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon9-v1.md'; HC9 = '906bec723f0528c6055be8fbb2d88cc44d2be10a09aa9353d492ab4be7c55654'
assert sha(R/CL9) == HC9
t = B9.read_text(encoding='utf-8'); F3 = t.splitlines()[75]; fautes = []
def r(a, b):
    global t
    c = t.count(a)
    if c != 1: fautes.append((c, a[:90])); return
    t = t.replace(a, b)
DEBUT = '2026-11-19T02:12Z'
r("— v1 — brouillon 9", "— v1 — brouillon 10")
r("**Statut : brouillon 9, texte soumis au scellement", "**Statut : brouillon 10, texte soumis au scellement")
r("contre-lecteur du brouillon 8 : désigné par la conductrice", "contre-lecteur du brouillon 8 : désigné par la conductrice ; contre-lecteur du brouillon 9 : Opus 5.5")
r("brouillon 9 écrit entre 2026-11-19T01:57Z et 2026-11-19T02:01Z (`date -u`).", "brouillon 9 écrit entre 2026-11-19T01:57Z et 2026-11-19T02:01Z ; brouillon 10 écrit entre " + DEBUT + " et HEURE_DE_FIN (`date -u`).")
r("`docs/notes/barreau8-cote-moniteurs-sorties-v1/notice-passe-recalcul-v1.md` — `45da9b99be0a3f9dacbf0a98aae570982f1f8b4dfb000920a402ec202c9aa472` ;", "`docs/notes/barreau8-cote-moniteurs-sorties-v1/notice-passe-recalcul-v1.md` — `45da9b99be0a3f9dacbf0a98aae570982f1f8b4dfb000920a402ec202c9aa472` (le code de la passe et sa notice sont passés depuis en version 2, sans changement des noms ni des formats de la livraison ; c'est la ligne de registre du code qui fait foi sur la version) ;")
# R-1
r("tout autre fichier du dépôt ou d'un dossier d'entrée, et tout chemin dont un composant porte « iib », « ii-b », « consigne-privee » ou « extrait_cote_moniteurs », est refusé avant ouverture", "hors de cette liste, tout autre fichier du dépôt ou d'un dossier d'entrée, et tout chemin dont un composant porte « iib », « ii-b », « consigne-privee » ou « extrait_cote_moniteurs », est refusé avant ouverture ; un chemin de la liste fermée n'est jamais refusé par ce motif (les noms des fichiers de la course et du registre propre portent « iib »)")
# R-2
r("(moins de 0,01 Go ; la garde P9 leur réserve 4 000 000 octets)", "(moins de 0,01 Go : compte au point « Taille des fichiers ajoutés par ces formes » ; la garde P9 réserve 4 000 000 octets à la trace, au bordereau et à leurs compagnons)")
# R-3
r("de nom `a` suivi du rang de l'action sur cinq chiffres (par exemple `a00016`)", "de nom `a` suivi, sur cinq chiffres, de la valeur du champ `rang` de l'index (ordre du fichier des identifiants, non le rang dans le tri du sous-échantillon ; par exemple `a00016`)")
# R-4
r("la lecture exige les cinq premières", "la lecture exige les cinq autres clés")
# cinquième remplacement (libellés)
r("`agregations`, JSON : les deux libellés des cases.", "`agregations`, JSON : les deux libellés des cases, exactement `\"maximum (production)\"` pour la case 0 et `\"moyenne (bras de diagnostic, jamais en production)\"` pour la case 1 ; la lecture refuse si ces deux libellés ne sont pas exactement ceux-là, dans cet ordre.")
# entrée
r("- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR", "- **Contre-lecture 3 quinquies** — sous-agent neuf, modèle Claude Opus 5.5, qui n'a écrit ni ce texte, ni aucune contre-lecture antérieure de ce texte, ni la note d'interface, ni la notice, ni la note des lacunes, ni aucun code ; contre-lecture de la différence du brouillon 8 au brouillon 9. Brouillon relu : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon9.md`, empreinte `" + H9 + "`. Rapport : `" + CL9 + "`, empreinte `" + HC9 + "`. Conclusion : « PAS PRÊT » sur une liste fermée de quatre remplacements (R-1, bloquante ; R-2 et R-3, à corriger ; R-4, mineure) ; les 32 points sont dits portés, sans changement de fond. Traitement : `brouillons/barreau8-lecture-sondes-v1/differences-brouillon9-brouillon10-v1.md` (empreinte dans son compagnon).\n- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR")
h = subprocess.run(['date','-u','+%Y-%m-%dT%H:%MZ'],capture_output=True,text=True).stdout.strip()
r("HEURE_DE_FIN", h)
for c in ("À REMPLIR — À FIXER : tirée par la session mère au scellement", "- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :", "versée avec l'empreinte du texte scellé."):
    if t.count(c) != 1: fautes.append(('unicité', t.count(c), c))
if t.count("À REMPLIR") != 2: fautes.append(('marqueurs', t.count("À REMPLIR")))
if t.splitlines()[75] != F3: fautes.append(('F-3 changée',))
if fautes:
    for f in fautes: print("FAUTE", f)
    sys.exit(1)
P.write_text(t, encoding='utf-8')
N.write_text(f"""# Différences entre le brouillon 9 et le brouillon 10 du texte « lecture des sondes du barreau 8 et passe de recalcul de l'activité interne » — v1

- Brouillon 9 : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon9.md`, empreinte `{H9}`.
- Contre-lecture du brouillon 9 (Opus 5.5, contre-lecteur neuf) : `{CL9}`, empreinte `{HC9}` (vérifiée ; lue en entier).
- Brouillon 10 : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon10.md` (empreinte : son compagnon `.sha256`).
- Rédacteur : Fable 5.2. Écrit le 2026-11-19 entre {DEBUT} et {h} (`date -u` ; mêmes heures que la ligne de date du brouillon 10), par programme, à partir du brouillon 9 : onze remplacements contrôlés (chaque texte cherché doit paraître exactement une fois, sinon rien n'est écrit). Le programme vérifie que les chaînes de la procédure de remplissage restent uniques, qu'il reste exactement deux marqueurs et que la ligne 76 (F-3) est identique à celle du brouillon 9. Ni le code ni ses essais n'ont été lus.

## Une ligne par remplacement

| n° | objet | état | où, dans le brouillon 10 |
|---|---|---|---|
| R-1 (bloquante) | garde des chemins lus de la passe : le refus des chemins portant « iib » ne vaut que hors de la liste fermée | appliqué mot pour mot | garde P8 (ligne 296) |
| R-2 | attribution de la réserve de 4 000 000 octets | appliqué mot pour mot | décision de taille (ligne 210) |
| R-3 | nom des tableaux d'activité brute : valeur du champ `rang` de l'index | appliqué mot pour mot | « Noms et champs », (4) (ligne 264) |
| R-4 (mineure) | « la lecture exige les cinq autres clés » | appliqué mot pour mot | conditions d'ordre du registre (ligne 305) |
| cinquième (développeur de la passe, transmis par la conductrice) | les deux libellés de la liste `agregations`, écrits exactement : `"maximum (production)"` (case 0) et `"moyenne (bras de diagnostic, jamais en production)"` (case 1) ; la lecture refuse sinon | appliqué ; la ligne 261 a été relue en entier : seule la phrase « `agregations`, JSON : les deux libellés des cases. » y change | « Noms et champs », (1) (ligne 261). Les deux libellés sont ceux que la conductrice transmet du code de la passe : le rédacteur ne les a pas vérifiés dans le code, qu'il ne lit pas |

Refusés ou adaptés : aucun.

## Changements hors remplacements (demandés)

- Ligne 1 : titre « brouillon 10 » ; ligne 3 : statut « brouillon 10 » (le numéro seul).
- Ligne 5 : « contre-lecteur du brouillon 9 : Opus 5.5 ».
- Ligne 7 : ligne de date.
- Ligne 24 : après la citation de la notice du code de la passe (version 1, celle que le rédacteur a lue), la demi-phrase « le code de la passe et sa notice sont passés depuis en version 2, sans changement des noms ni des formats de la livraison ; c'est la ligne de registre du code qui fait foi sur la version » (fait transmis par la conductrice).
- Section « Contre-lecture » : entrée « Contre-lecture 3 quinquies » (empreintes du brouillon 9 et du rapport), ajoutée avant l'entrée 4.

Rien d'autre ne change.

## Marqueurs restants

Deux, et deux seulement : ligne 76 (F-3, entropie racine des graines, inchangée au caractère près) et ligne 429 (entrée « Contre-lecture 4 (finale, texte rempli) », décalée d'une ligne par l'entrée ajoutée : la procédure de remplissage du contre-lecteur dit 428). Sortie exacte du validateur sur le brouillon 10 : `['section vide ou à remplir : Contre-lecture']`.
""", encoding='utf-8')
print("ok", h, len(t.splitlines()))
