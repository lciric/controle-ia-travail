"""Fabrique collisionneur_v9_essaim_v7.py, ses essais et sa configuration depuis la v6, par remplacements exacts."""
import hashlib, json, sys
from pathlib import Path
E = Path("/home/user/controle-ia-travail/docs/notes/collisionneur-v9/essaim-v1")
SHA_V8P = hashlib.sha256((E.parent / "collisionneur_v9_v8p.py").read_bytes()).hexdigest()
assert SHA_V8P.startswith("5979c712")
assert hashlib.sha256((E / "collisionneur_v9_essaim_v6.py").read_bytes()).hexdigest().startswith("90274147")
RELECTURE = E / "demande-fable-essaim-pilote-v1" / "reponse-fable-v1" / "relecture-fable-api.md"
assert hashlib.sha256(RELECTURE.read_bytes()).hexdigest().startswith("28cc1d81")


def remplacer(t, ancien, nouveau, n=1):
    k = t.count(ancien)
    if k != n:
        sys.exit(f"trouvé {k} fois (attendu {n}) : {ancien[:90]!r}")
    return t.replace(ancien, nouveau)


s = (E / "collisionneur_v9_essaim_v6.py").read_text(encoding="utf-8")
s = remplacer(s, '''"""Collisionneur v9, mode « essaim » (v6) : société de modèles sous pseudonymes, à budget apparié par modèle.
''', '''"""Collisionneur v9, mode « essaim » (v7) : société de modèles sous pseudonymes, à budget apparié par modèle.

v7 (session des collisionneurs, Opus 5.5, 22 novembre 2026) : copie de la v6 (90274147…, inchangée, R12), selon la
relecture de Fable demande-fable-essaim-pilote-v1/reponse-fable-v1/relecture-fable-api.md (28cc1d81…). Changements, et
seulement ceux-là : (1) moteur v8p (lignée v8f : tour III.3 à la seule place « fin », phrase du remplacement 1 avant la
forme imposée, ligne de format du tour III.3 selon le remplacement 5), empreinte contrôlée ; (2) finale : paragraphe
« Temps final » (remplacement 2) et ligne « Livrable » (remplacement 3) de Fable mot pour mot, puis la phrase du
remplacement 1 et la forme imposée (remplacement 4), puis la ligne de format du tour III.3 du moteur (remplacement 5) ;
(3) chaque invite de cycle reçoit, après la consigne de Fable inchangée, la ligne de format du tour III.3 à la limite du
cycle (langue, format, marqueur de fin) ; (4) configuration : place_iii3 « fin ». Le temps 0 reste l'invite III.1 du
moteur mot pour mot.
''')
s = remplacer(s, 'VERSION = "collisionneur-v9-essaim-v6"', 'VERSION = "collisionneur-v9-essaim-v7"')
s = remplacer(s, 'SCRIPT_MOTEUR = ICI.parent / "collisionneur_v9_v8f.py"  # v6 : moteur v8f',
              'SCRIPT_MOTEUR = ICI.parent / "collisionneur_v9_v8p.py"  # v7 : moteur v8p (lignée v8f)')
s = remplacer(s, 'SHA_MOTEUR = "445fe2d37eebbda1aede9a7e7351a394dbdfdf9d0c907ffa86eaafde9363001e"', f'SHA_MOTEUR = "{SHA_V8P}"')
s = remplacer(s, '"collisionneur_v9_v8f_pour_essaim"', '"collisionneur_v9_v8p_pour_essaim"')
s = remplacer(s, 'raise SystemExit(f"ARRÊT : empreinte du moteur (v8f) {h} différente de {sha}")',
              'raise SystemExit(f"ARRÊT : empreinte du moteur (v8p) {h} différente de {sha}")')
s = remplacer(s, '''        probl.append("programme d'essaim lancé sur un autre moteur (v8f attendue)")''',
              '''        probl.append("programme d'essaim lancé sur un autre moteur (v8p attendue)")''')
s = remplacer(s, "est tenu avant chaque envoi par executer_cellule du moteur (v8f)",
              "est tenu avant chaque envoi par executer_cellule du moteur (v8p)")
s = remplacer(s, '''CONSIGNE_FINALE = """Temps final. Écrivez seul votre réponse à la question ; aucun participant ne la verra. Vous recevez \\
votre brouillon initial, votre dernière prépublication, les revues qu'elle a reçues, la liste du fil commun et les \\
textes demandés au dernier cycle. Vous êtes libre de maintenir, de modifier ou d'abandonner toute position, la vôtre \\
comme celle d'un autre. N'y mentionnez ni pseudonyme ni le déroulement à plusieurs : la réponse doit se lire seule.
{format_iii3} — 3 500 mots au plus.
{format_isole}"""''', '''# v7 : relecture de Fable (28cc1d81…), remplacements 2, 3 et 4 mot pour mot ; {phrase_duels} et {forme_imposee} sont
# PHRASE_DUELS_III3 et FORME_IMPOSEE_DUELS du moteur ; {format_isole} est la ligne de format du tour III.3 du moteur
# (remplacement 5), la même chaîne que dans le jumeau isolé. La ligne « Livrable » neuve remplace la ligne servie par la v6
# (« Livrable » du tour III.3 suivie de « — 3 500 mots au plus. »).
CONSIGNE_FINALE = """Temps final. Écris seul ta réponse à la question ; aucun participant ne la verra. Tu reçois ton \\
brouillon initial, ta dernière prépublication, les revues qu'elle a reçues, la liste du fil commun et les textes \\
demandés au dernier cycle. Tu es libre de maintenir, de modifier ou d'abandonner toute position, la tienne comme celle \\
d'un autre. N'y mentionne ni pseudonyme ni le déroulement à plusieurs : la réponse doit se lire seule.
Livrable : (a) pour chaque objection des revues, reformulée sans dire d'où elle vient : acceptée, rejetée avec sa \\
raison, ou transformée en test ; (b) les expériences corrigées ; (c) ta réponse à la question, en une page : ce qui est \\
établi, ce qui ne l'est pas, et l'expérience à faire en premier.
{phrase_duels}
{forme_imposee}
{format_isole}"""''')
s = remplacer(s, '''def format_isole_iii3(v):
    """v3 : ligne « Format : … » du préambule de la v8d, remplie comme pour le tour III.3 isolé."""
    ligne = next(l for l in v.PREAMBULE_GABARIT.splitlines() if l.startswith("Format :"))
    return ligne.format(mots=v.TOURS["E3-T3"]["mots"], marqueur=v.MARQUEUR)
''', '''def format_isole_iii3(v):
    """v3 : ligne « Format : … » du tour III.3 isolé. v7 : celle du moteur v8p (remplacement 5), même chaîne."""
    return v.ligne_format("E3-T3")


def nombre_fr(n):
    """v7 : 3000 → « 3 000 » (forme de Fable)."""
    return f"{n:,}".replace(",", " ")


def format_cycle(v, cfg):
    """v7 : règle de Fable pour les cycles : la ligne de format du tour III.3, avec la limite du texte du cycle
    (mots.cycle) ; la mention de la page (point (c), propre au tour III.3) n'y est pas."""
    ligne = v.ligne_format("E3-T3")
    assert ligne.count(v.FORMAT_III3_NOUVEAU) == 1
    return ligne.replace(v.FORMAT_III3_NOUVEAU,
                         f"{nombre_fr(cfg['mots']['cycle'])} mots au plus pour l'ensemble de la réponse")
''')
s = remplacer(s, '''        c(CONSIGNE_CYCLE.format(c=k, N=cfg["cycles"], balises=BALISES))
    else:
        c(CONSIGNE_FINALE.format(format_iii3=format_iii3(v), format_isole=format_isole_iii3(v)))''',
              '''        c(CONSIGNE_CYCLE.format(c=k, N=cfg["cycles"], balises=BALISES) + "\\n" + format_cycle(v, cfg))  # v7
    else:
        c(CONSIGNE_FINALE.format(phrase_duels=v.PHRASE_DUELS_III3, forme_imposee=v.FORME_IMPOSEE_DUELS,
                                 format_isole=format_isole_iii3(v)))  # v7''')
(E / "collisionneur_v9_essaim_v7.py").write_text(s, encoding="utf-8")

cfg_texte = (E / "configuration-pilote-essaim-v6.json").read_text(encoding="utf-8")
cfg_texte = remplacer(cfg_texte, '"place_iii3": null', '"place_iii3": "fin"')
cfg_texte = remplacer(cfg_texte, "v6 : moteur v8f ; place_iii3 à fixer (« fin » ou « avant-livrable ») sur le mot de Fable par "
                                 "la mère, null : refusé",
                      "v6 : moteur v8f ; v7 : moteur v8p, place_iii3 « fin » (seule place, relecture de Fable 28cc1d81…)")
json.loads(cfg_texte)
(E / "configuration-pilote-essaim-v7.json").write_text(cfg_texte, encoding="utf-8")
print("écrit", hashlib.sha256(s.encode()).hexdigest(), hashlib.sha256(cfg_texte.encode()).hexdigest())
