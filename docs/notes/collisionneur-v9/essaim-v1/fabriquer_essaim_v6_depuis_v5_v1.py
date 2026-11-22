"""Fabrique collisionneur_v9_essaim_v6.py, ses essais et sa configuration depuis la v5, par remplacements exacts."""
import hashlib, json, sys
from pathlib import Path
E = Path("/home/user/controle-ia-travail/docs/notes/collisionneur-v9/essaim-v1")
SHA_V8F = hashlib.sha256((E.parent / "collisionneur_v9_v8f.py").read_bytes()).hexdigest()
assert SHA_V8F.startswith("445fe2d3")
assert hashlib.sha256((E / "collisionneur_v9_essaim_v5.py").read_bytes()).hexdigest().startswith("f2593ce9")

def remplacer(t, ancien, nouveau, n=1):
    k = t.count(ancien)
    if k != n:
        sys.exit(f"trouvé {k} fois (attendu {n}) : {ancien[:90]!r}")
    return t.replace(ancien, nouveau)

s = (E / "collisionneur_v9_essaim_v5.py").read_text(encoding="utf-8")
s = remplacer(s, '''"""Collisionneur v9, mode « essaim » (v5) : société de modèles sous pseudonymes, à budget apparié par modèle.
''', '''"""Collisionneur v9, mode « essaim » (v6) : société de modèles sous pseudonymes, à budget apparié par modèle.

v6 (session des collisionneurs, Opus 5.5, 22 novembre 2026) : copie de la v5 (f2593ce9…, inchangée, R12). Changements,
et seulement ceux-là : (1) moteur v8f (445fe2d3…, corrections de la v8e, conforme selon son contre-lecteur) ; (2) journal
d'un programme d'essaim plus ancien (clé sha256_v8d) lu sans erreur par `verifier`, et dit « autre moteur » ;
(3) essais : configuration sans place_iii3 refusée proprement ; empreinte du moteur contrôlée par `verifier`.
''')
s = remplacer(s, 'VERSION = "collisionneur-v9-essaim-v5"', 'VERSION = "collisionneur-v9-essaim-v6"')
s = remplacer(s, 'SCRIPT_MOTEUR = ICI.parent / "collisionneur_v9_v8e.py"  # v5 : moteur v8e',
              'SCRIPT_MOTEUR = ICI.parent / "collisionneur_v9_v8f.py"  # v6 : moteur v8f')
s = remplacer(s, 'SHA_MOTEUR = "0d591933032e249d17d618e406fe6390ee2536569abc9a232289168122186957"', f'SHA_MOTEUR = "{SHA_V8F}"')
s = remplacer(s, '"collisionneur_v9_v8e_pour_essaim"', '"collisionneur_v9_v8f_pour_essaim"')
s = remplacer(s, 'raise SystemExit(f"ARRÊT : empreinte du moteur (v8e) {h} différente de {sha}")',
              'raise SystemExit(f"ARRÊT : empreinte du moteur (v8f) {h} différente de {sha}")')
s = remplacer(s, '''    if any(h["sha256_moteur"] != SHA_MOTEUR for h in hist):
        probl.append("programme d'essaim lancé sur un autre moteur (v8e attendue)")''',
              '''    if any(h.get("sha256_moteur") != SHA_MOTEUR for h in hist):  # v6 : journal ancien (sha256_v8d) lu sans erreur
        probl.append("programme d'essaim lancé sur un autre moteur (v8f attendue)")''')
s = remplacer(s, "est tenu avant chaque envoi par executer_cellule du moteur (v8e)",
              "est tenu avant chaque envoi par executer_cellule du moteur (v8f)")
(E / "collisionneur_v9_essaim_v6.py").write_text(s, encoding="utf-8")

t = (E / "test_collisionneur_v9_essaim_v5.py").read_text(encoding="utf-8")
t = remplacer(t, 'ICI / "collisionneur_v9_essaim_v5.py"', 'ICI / "collisionneur_v9_essaim_v6.py"')
t = remplacer(t, '"essaim_essai_v5"', '"essaim_essai_v6"')
t = remplacer(t, "configuration-pilote-essaim-v5.json", "configuration-pilote-essaim-v6.json", n=t.count("configuration-pilote-essaim-v5.json"))
t = remplacer(t, 'VERSION == "collisionneur-v9-v8e"', 'VERSION == "collisionneur-v9-v8f"', n=t.count('VERSION == "collisionneur-v9-v8e"'))
t = remplacer(t, 'mod.SCRIPT_MOTEUR.name == "collisionneur_v9_v8e.py"', 'mod.SCRIPT_MOTEUR.name == "collisionneur_v9_v8f.py"')
t = '"""Essais de l\'essaim v6 : copie des essais de la v5 (moteur v8f), plus les essais de la v6 en fin.\n\nEn-tête de la v5 :\n' + t[3:]
t += '''

# ---------- v6 ----------

def test_v6_configuration_sans_place_iii3_refusee(es, tmp_path):
    mod, v = es
    p = config(tmp_path)
    cfg = json.loads(p.read_text(encoding="utf-8"))
    del cfg["place_iii3"]
    p.write_text(json.dumps(cfg, ensure_ascii=False), encoding="utf-8")
    with pytest.raises(v.Arret, match="clé place_iii3 absente"):
        mod.lire_configuration(v, p)


def _reecrire_programme(d, champ):
    chemin = d / "journal.jsonl"
    lignes = []
    for l in chemin.read_text(encoding="utf-8").splitlines():
        e = json.loads(l)
        if "programme_essaim" in e:
            e["programme_essaim"].pop("sha256_moteur", None)
            e["programme_essaim"].update(champ)
        lignes.append(json.dumps(e, ensure_ascii=False))
    chemin.write_text("\\n".join(lignes) + "\\n", encoding="utf-8")


@pytest.mark.parametrize("champ", [{"sha256_moteur": "0" * 64}, {"sha256_v8d": "b7803838" + "0" * 56}])
def test_v6_verifier_controle_l_empreinte_du_moteur(es, tmp_path, champ):
    mod, v = es
    assert lancer(mod, v, tmp_path, config(tmp_path, cycles=1), Faux(v)) == 0
    d = tmp_path / "essaim"
    assert mod.verifier_essaim(v, d) == []
    _reecrire_programme(d, champ)
    assert "programme d'essaim lancé sur un autre moteur (v8f attendue)" in mod.verifier_essaim(v, d)
'''
(E / "test_collisionneur_v9_essaim_v6.py").write_text(t, encoding="utf-8")

c = json.loads((E / "configuration-pilote-essaim-v5.json").read_text(encoding="utf-8"))
c["version"] = "configuration-pilote-essaim-v6"
c["statut"] = c["statut"].replace("v5 : moteur v8e", "v6 : moteur v8f")
assert "v6 : moteur v8f" in c["statut"]
(E / "configuration-pilote-essaim-v6.json").write_text(json.dumps(c, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("v6", hashlib.sha256(s.encode()).hexdigest())
