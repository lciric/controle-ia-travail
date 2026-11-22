"""Fabrique collisionneur_v9_essaim_v5.py et ses essais depuis la v4, par remplacements exacts."""
import hashlib, json, sys
from pathlib import Path
E = Path("/home/user/controle-ia-travail/docs/notes/collisionneur-v9/essaim-v1")
SHA_V8E = hashlib.sha256((E.parent / "collisionneur_v9_v8e.py").read_bytes()).hexdigest()

def remplacer(t, ancien, nouveau, n=1):
    k = t.count(ancien)
    if k != n:
        sys.exit(f"trouvé {k} fois (attendu {n}) : {ancien[:90]!r}")
    return t.replace(ancien, nouveau)

s = (E / "collisionneur_v9_essaim_v4.py").read_text(encoding="utf-8")
s = remplacer(s, '''"""Collisionneur v9, mode « essaim » (v4) : société de modèles sous pseudonymes, à budget apparié par modèle.
''', f'''"""Collisionneur v9, mode « essaim » (v5) : société de modèles sous pseudonymes, à budget apparié par modèle.

v5 (session des collisionneurs, Opus 5.5, 22 novembre 2026) : copie de la v4 (brouillon du développeur, inchangé, R12).
Changements, et seulement ceux-là : (1) moteur : la v8e (balises des duels aux tours III.1 et III.3, ordre de la mère du
22 novembre 07:40Z) au lieu de la v8d, empreinte contrôlée au chargement ; le temps 0 reste l'invite III.1 du moteur mot
pour mot, donc avec la « forme imposée » ; clé neuve « place_iii3 » de la configuration (l'une de PLACES_III3 de la v8e),
obligatoire, posée par fixer_place_iii3 ; la consigne finale garde la seule ligne « Livrable » du tour III.3, sans la
forme imposée (point ouvert pour Fable) ; (2) bloquant de la vérification de la v4 (contre-lecteur Opus neuf) : la borne
d'un brouillon non encore écrit prend le plus grand de « max » et « max_relance » de l'espèce (un brouillon valide peut
sortir de la relance) ; (3) essais : brouillon d'Astra au-delà de la borne de la v4 ; balise refusée par `verifier`.
''')
s = remplacer(s, 'VERSION = "collisionneur-v9-essaim-v4"', 'VERSION = "collisionneur-v9-essaim-v5"')
s = remplacer(s, '''SCRIPT_V8D = ICI.parent / "collisionneur_v9_v8d.py"
SHA_V8D = "b780383874598f12b24c79e4087d335c8e01cda685e295f5116898fa3b1715ac"''', f'''SCRIPT_MOTEUR = ICI.parent / "collisionneur_v9_v8e.py"  # v5 : moteur v8e
SHA_MOTEUR = "{SHA_V8E}"''')
s = remplacer(s, "SCRIPT_V8D", "SCRIPT_MOTEUR", n=s.count("SCRIPT_V8D"))
s = remplacer(s, "SHA_V8D", "SHA_MOTEUR", n=s.count("SHA_V8D"))
s = remplacer(s, "charger_v8d", "charger_moteur", n=s.count("charger_v8d"))
s = remplacer(s, '"sha256_v8d"', '"sha256_moteur"', n=s.count('"sha256_v8d"'))
s = remplacer(s, 'raise SystemExit(f"ARRÊT : empreinte de la v8d {h} différente de {sha}")',
              'raise SystemExit(f"ARRÊT : empreinte du moteur (v8e) {h} différente de {sha}")')
s = remplacer(s, '"collisionneur_v9_v8d_pour_essaim"', '"collisionneur_v9_v8e_pour_essaim"')
s = remplacer(s, 'probl.append("programme d\'essaim lancé sur une autre v8d")',
              'probl.append("programme d\'essaim lancé sur un autre moteur (v8e attendue)")')
# configuration : place_iii3
s = remplacer(s, '''                "relecteurs", "pseudonymes", "salles", "salle_injection", "finale_jamais_sautee") + tuple(CHOIX):''',
              '''                "relecteurs", "pseudonymes", "salles", "salle_injection", "finale_jamais_sautee",
                "place_iii3") + tuple(CHOIX):  # v5 : place_iii3''')
s = remplacer(s, '''    if not isinstance(cfg.get("reserver_finales", False), bool):''', '''    if cfg["place_iii3"] not in v.PLACES_III3:  # v5 : place des balises au tour III.3 (v8e), non tranchée ici
        probl.append(f"place_iii3 : l'une de {sorted(v.PLACES_III3)}")
    else:
        v.fixer_place_iii3(cfg["place_iii3"])
    if not isinstance(cfg.get("reserver_finales", False), bool):''')
# bloquant : borne avec la relance
s = remplacer(s, '''    sortie = max(v.MODELES[l]["max"] * v.CAR_SORTIE_MAX[v.MODELES[l]["fournisseur"]] for l in lettres)''',
              '''    sortie = max(max(v.MODELES[l]["max"], v.MODELES[l]["max_relance"]) * v.CAR_SORTIE_MAX[v.MODELES[l]["fournisseur"]]
                 for l in lettres)  # v5 : un brouillon valide peut sortir de la relance''')
s = remplacer(s, "est tenu avant chaque envoi par executer_cellule de la v8d", "est tenu avant chaque envoi par executer_cellule du moteur (v8e)")
(E / "collisionneur_v9_essaim_v5.py").write_text(s, encoding="utf-8")

c = json.loads((E / "configuration-pilote-essaim-v4.json").read_text(encoding="utf-8"))
c["version"] = "configuration-pilote-essaim-v5"
c["place_iii3"] = None
c["statut"] += " ; v5 : moteur v8e ; place_iii3 à fixer (« fin » ou « avant-livrable ») sur le mot de Fable par la mère, null : refusé"
(E / "configuration-pilote-essaim-v5.json").write_text(json.dumps(c, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("v5", hashlib.sha256(s.encode()).hexdigest(), "moteur", SHA_V8E)
