"""Geste du scellement du texte du bras A (case « entropie », 13.1) — un seul tirage de l'entier racine. Version 3.

v3 (23 novembre 2026) : seule différence avec la v2 (`ee09a6dc…`, vérifiée), la source est le brouillon 56 (empreinte,
titre, statut et textes de la note adaptés) ; la logique est inchangée.

v2 (22 novembre 2026, contre-lecture du programme v1 : deux défauts) : (1) toutes les vérifications sont faites AVANT le
tirage, sur un texte fabriqué avec un entier de remplacement ; le tirage ne fait ensuite que substituer l'entier ;
(2) après le tirage, l'entier et l'heure sont d'abord écrits sur la sortie d'erreur et dans un fichier de reprise, puis la
note et le texte sont écrits en mode exclusif binaire (« xb ») avec fsync ; un échec après le tirage affiche l'entier et
le chemin de reprise, sans nouveau tirage ; l'empreinte est calculée sur les octets écrits ; l'heure est prise au
moment du tirage. Mineurs : version de numpy ≥ 1.25 exigée ; entier vérifié (entier ≥ 0, au plus 128 bits) ; la marque
doit appartenir à la ligne « | entropie ».

Usage : geste_scellement_v3.py SOURCE(brouillon 56) SORTIE NOTE
Refuse si SORTIE, NOTE ou le fichier de reprise existent (aucun second tirage, R12)."""
import datetime, hashlib, os, sys
import numpy as np

SOURCE, SORTIE, NOTE = sys.argv[1:4]
REPRISE = NOTE + ".entier-tire.txt"
ATTENDUE = "561723f15bd777a315aedb561a4cfa406aabdefed4d34548a7432aee535bb012"
MARQUE = "**À REMPLIR** pour l'entier racine :"
JETON = "§ENTIER§"
JETON_HEURE = "§HEURE§"


def refus(m):
    sys.exit(f"refus (avant tout tirage) : {m}")


# 1. Vérifications, toutes avant le tirage.
for p in (SORTIE, NOTE, REPRISE):
    if os.path.exists(p):
        refus(f"{p} existe déjà ; aucun second tirage")
v = tuple(int(x) for x in np.__version__.split(".")[:2])
if v < (1, 25):
    refus(f"numpy {np.__version__} < 1.25 (R9)")
octets = open(SOURCE, "rb").read()
if hashlib.sha256(octets).hexdigest() != ATTENDUE:
    refus("empreinte de la source inattendue")
avant = octets.decode("utf-8").split("\n")
lignes = [i for i, l in enumerate(avant) if MARQUE in l]
if len(lignes) != 1 or avant[lignes[0]].count(MARQUE) != 1 or sum(l.count("À REMPLIR") for l in avant) != 1:
    refus("la marque de l'entier racine n'est pas unique, ou une autre marque reste")
i = lignes[0]
if not avant[i].startswith("| entropie |"):
    refus("la marque n'est pas dans la ligne « | entropie »")
commande = "numpy.random.SeedSequence().entropy"
L = list(avant)
L[i] = L[i].replace(MARQUE, f"**remplie pour l'entier racine** : **{JETON}** (tiré le {JETON_HEURE}, `{commande}`, numpy {np.__version__}, une seule fois, par la session de relance ; note du scellement `docs/notes/relance-organismes-discrets-v1/scellement-bras-a-v2/{os.path.basename(NOTE)}`) :")
a, b = "— v2, BROUILLON 56", "— v2"
if L[0].count(a) != 1:
    refus("titre inattendu")
L[0] = L[0].replace(a, b)
a = "**Statut : brouillon 56, non exécutable.** Le brouillon 56 porte"
if L[2].count(a) != 1:
    refus("statut inattendu")
L[2] = L[2].replace(a, f"**Statut : texte scellé, version 2 du préenregistrement du bras A** (entier racine tiré et inscrit le {JETON_HEURE} en 13.1, case « entropie » ; aucune autre différence avec le brouillon 56, `561723f1…`, que le titre et cette ligne). Le brouillon 56 porte")
changees = [j for j in range(len(avant)) if avant[j] != L[j]]
if len(avant) != len(L) or changees != sorted({0, 2, i}):
    refus(f"différence hors des trois lignes : {changees}")
gabarit = "\n".join(L)
if gabarit.count(JETON) != 1 or gabarit.count(JETON_HEURE) != 2 or "À REMPLIR" in gabarit:
    refus("gabarit inattendu")

# 2. Le tirage, une seule fois.
entier = np.random.SeedSequence().entropy
heure = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
print(f"ENTIER TIRÉ : {entier} à {heure} — ne jamais tirer de nouveau ; reprise : {REPRISE}", file=sys.stderr, flush=True)
try:
    with open(REPRISE, "xb") as f:
        f.write(f"{entier}\n{heure}\n".encode()); f.flush(); os.fsync(f.fileno())
    if not (isinstance(entier, int) and 0 <= entier < 2 ** 128):
        raise ValueError(f"entier hors de 128 bits : {entier!r}")
    neuf = gabarit.replace(JETON, str(entier)).replace(JETON_HEURE, heure).encode("utf-8")
    h = hashlib.sha256(neuf).hexdigest()
    note = f"""# Note du scellement — texte du bras A, version 2

- Heure du tirage (UTC) : {heure}
- Commande : `{commande}` (numpy {np.__version__}), appelée une seule fois, sans argument, par la session de relance (programme `geste_scellement_v3.py` de ce dossier, après vérification de toutes ses gardes sur un texte de remplacement).
- Entier racine : {entier}
- Source : brouillon 56, `{ATTENDUE}`.
- Texte obtenu : `{os.path.basename(SORTIE)}`, `{h}` (empreinte des octets écrits).
- Différence avec le brouillon 56, vérifiée par programme avant le tirage : lignes {[c + 1 for c in changees]} seulement — titre (« BROUILLON 56 » retiré), statut, et la case « entropie » (entier inscrit, marque retirée).
- Chaîne de lecture : contre-lecture 11 (`45d76769…`) et sa vérification (`a96a4d9d…`) ; contre-lectures des cases remplies des brouillons 54 (`c68b20de…`) et 55 (`b0c9960b…`) ; contre-lecture du brouillon 56 (§CL56§) ; vérification habilitée (R-5032).
- Aucun programme de la course, aucun essai ni aucune simulation n'a tourné avec cet entier ; les essais du programme ont pris une entropie fictive, déclarée telle.
"""
    for chemin, contenu in ((NOTE, note.encode("utf-8")), (SORTIE, neuf)):
        with open(chemin, "xb") as f:
            f.write(contenu); f.flush(); os.fsync(f.fileno())
except Exception as e:
    print(f"ÉCHEC APRÈS LE TIRAGE : {e!r} ; entier {entier}, heure {heure}, dans {REPRISE} ; AUCUN nouveau tirage : "
          "écrire le texte à la main depuis le gabarit et ce fichier, et le déclarer", file=sys.stderr)
    sys.exit(3)
print(h, entier)
