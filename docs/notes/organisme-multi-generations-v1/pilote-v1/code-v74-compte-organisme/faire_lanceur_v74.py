"""Écrit demonstrations/pilote_mr2_v74.py depuis pilote_mr2_v73.py : remplacements comptés (mot de Lazar « Option (a) : code v74,
réflexion absente sans effet » ; R-2731, R-2738)."""
import sys
racine = sys.argv[1]
t = open(f"{racine}/demonstrations/pilote_mr2_v73.py", encoding="utf-8").read()
i = t.index("\nChangements de la v72, gardés")
doc = '''"""Lanceur du pilote d'une génération sur la famille MR-2 — code v74 (fichier neuf, R12 ; `pilote_mr2_v73.py` reste en place,
inchangé ; C-11, C-13, C-14, C-18 ; sonde).

Changements depuis la v73 (mot de Lazar « Option (a) : code v74, réflexion absente sans effet » ; R-2731) : le **module de la sonde
v74** (`pole/sonde_pilote_v74.py` : pour Argon, une réflexion absente aux deux appels, sans jeton caché, est « sans effet » et
remplace la règle confirmée ; relevé `releve-sonde-pilote-v74.json`) ; et sa contrepartie, ici, en mode réel : **un proposeur que le
relevé de la sonde dit « sans réflexion » arrête le pilote** (code 3, l'appel porté au relevé partiel, sa dépense comptée une fois)
si un champ de réflexion apparaît dans l'usage brut d'un de ses appels
(`garder_reflexion_absente`) ; noms (version, marqueurs « empreintes-du-code-pilote-v74 »,
liste des fichiers gelés : lanceur v74 et sonde v74 en plus). Tout le reste est le lanceur v73 (bloc par clés, `sonde-un`).

Changements de la v73, gardés (R-2690, GO-2026-11-14-02) : le bloc gelé nomme les proposeurs par leurs clés, sans identifiant de
modèle ; sous-commande `sonde-un` (sonde d'un seul relais sous une ligne à part).
'''
assert t.startswith('"""Lanceur du pilote')
t = doc + t[i:]
R = [
 ("from pole import sonde_pilote_v72 as S  # noqa: E402\n", "from pole import sonde_pilote_v74 as S  # noqa: E402\n", 1),
 ('VERSION = "lanceur-pilote-mr2-v73"\nLANCEUR = "demonstrations/pilote_mr2_v73.py"\n',
  'VERSION = "lanceur-pilote-mr2-v74"\nLANCEUR = "demonstrations/pilote_mr2_v74.py"\n', 1),
 ('"<!-- empreintes-du-code-pilote-v73 : début -->", "<!-- empreintes-du-code-pilote-v73 : fin -->"',
  '"<!-- empreintes-du-code-pilote-v74 : début -->", "<!-- empreintes-du-code-pilote-v74 : fin -->"', 1),
 ('    "demonstrations/pilote_mr2_v73.py", "pole/pilote_mr2_v70.py",', '    "demonstrations/pilote_mr2_v74.py", "pole/pilote_mr2_v70.py",', 1),
 ('"pole/sonde_pilote_v71.py", "pole/sonde_pilote_v72.py",\n', '"pole/sonde_pilote_v71.py", "pole/sonde_pilote_v72.py",\n    "pole/sonde_pilote_v74.py",\n', 1),
 ('raise P.Refus("texte scellé : bloc « empreintes-du-code-pilote-v73 » absent")', 'raise P.Refus("texte scellé : bloc « empreintes-du-code-pilote-v74 » absent")', 1),
 ('    go, releve_sha = None, None\n    if args.mode == "reel":\n        go, releve_sha = exiger_mode_reel(args, conf)\n',
  '    go, releve_sha, sans_reflexion = None, None, []\n    if args.mode == "reel":\n        go, releve_sha = exiger_mode_reel(args, conf)\n'
  '        sans_reflexion = S.proposeurs_sans_reflexion(args.releve_sonde)  # v74 : contrepartie de « réflexion sans effet »\n', 1),
 ('                r = PR.appeler(conf, nom, s["texte"], os.path.join(args.sortie, f"monde-{w}", nom), jeton, python=sys.executable)\n',
  '                r = PR.appeler(conf, nom, s["texte"], os.path.join(args.sortie, f"monde-{w}", nom), jeton, python=sys.executable)\n'
  '                garder_reflexion_absente(conf, nom, os.path.join(args.sortie, f"monde-{w}", nom), r, sans_reflexion)  # v74 : avant de compter la dépense (comptée une fois, à l\'arrêt)\n', 1),
 ('\n\ndef jouer(args):', '''

def garder_reflexion_absente(conf, nom, dossier_appel, r, sans_reflexion):
    """v74 (R-2738) : un proposeur que la sonde a dite « sans réflexion » (aucune réflexion cachée, règle de comptage sans effet)
    arrête le pilote (code 3, l'appel porté au relevé partiel avec sa dépense) si un champ de réflexion apparaît dans l'usage brut
    de son appel (corps du relais), ou si la commande lui compte une réflexion non nulle."""
    if nom not in sans_reflexion:
        return
    d = conf["proposeurs"][nom]["dialecte"]
    corps_f = os.path.join(dossier_appel, "corps-relais.json")
    u = None
    if os.path.isfile(corps_f):
        try:
            with open(corps_f, encoding="utf-8") as f:
                u = S.usage_brut(d, (json.load(f) or {}).get("corps"))
        except (OSError, ValueError, AttributeError):
            raise PR.ArretPilote(f"{nom} : corps du relais illisible : la garde de la réflexion ne peut pas lire l'appel (v74)",
                                 appel=r) from None
    jetons = r.get("jetons") if isinstance(r.get("jetons"), dict) else {}
    t = jetons.get("reflexion")
    if S.champ_de_reflexion_present(d, u) or (t is not None and t != 0):
        raise PR.ArretPilote(f"{nom} : champ de réflexion apparu en cours de course (réflexion comptée {t!r}) alors que la sonde "
                             f"l'a dit absent : arrêt du pilote (v74)", appel=r)


def jouer(args):''', 1),
]
for a, b, n in R:
    assert t.count(a) == n, (a[:80], t.count(a))
    t = t.replace(a, b)
open(f"{racine}/demonstrations/pilote_mr2_v74.py", "x", encoding="utf-8").write(t)
print("écrit")
