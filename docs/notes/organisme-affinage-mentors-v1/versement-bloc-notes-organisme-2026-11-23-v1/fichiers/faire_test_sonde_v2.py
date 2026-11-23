from pathlib import Path
import sys
racine = Path(sys.argv[1])
t = (racine / "tests/test_sonde_astra_courses_v1.py").read_text(encoding="utf-8")
rempl = [
 ('"""Essais de la sonde d\'Astra commune aux deux courses (`scripts/sonde_astra_courses_v1.py`) et diagnostic, hors ligne, du\ndéfaut de la sonde (réserve du relais jeté, code 4 de la commande).',
  '"""Essais de la sonde d\'Astra commune, version 2 (`scripts/sonde_astra_courses_v2.py`, modèle gpt-6.2-astra, prix 8 / 40),\nrepris des essais de la v1 (`tests/test_sonde_astra_courses_v1.py`, inchangés) et adaptés ; plus les mutations propres à la v2\n(relais jeté aux prix de la v1, relais qui ne permet que l\'ancien modèle, sonde appelée d\'une autre empreinte).'),
 ('S = _charger("sonde_astra_courses_v1", RACINE / "scripts" / "sonde_astra_courses_v1.py")',
  'S = _charger("sonde_astra_courses_v2", RACINE / "scripts" / "sonde_astra_courses_v2.py")\nMODELE = "gpt-6.2-astra"\nANCIEN = "gpt-6-astra"'),
 ('ARGS_SONDE_V2 = ["--max-sortie-jetons", "4096", "--sortie-min-jetons", "16", "--delai-s", "120"]  # ceux de la sonde v2',
  'ARGS_SONDE_V2 = ["--prix-entree", "8", "--prix-sortie", "40", "--max-sortie-jetons", "4096", "--sortie-min-jetons", "16",\n                 "--delai-s", "120"]  # ceux de la sonde v3 (nom de variable gardé)'),
 ('def __init__(self, completion_tokens=40, modele="gpt-6-astra"):', 'def __init__(self, completion_tokens=40, modele=MODELE):'),
 ('def __init__(self, amont: FauxAmont, reserve=R.RESERVE_PAR_APPEL_DEFAUT, plafond=0.05, max_appels=1, prix=(10, 50, 1)):',
  'def __init__(self, amont: FauxAmont, reserve=R.RESERVE_PAR_APPEL_DEFAUT, plafond=0.05, max_appels=1, prix=(8, 40, 1),\n                 modeles=(MODELE,)):'),
 ('g = R.fabriquer_gestionnaire("cle-factice-essai", amont.url, ("gpt-6-astra",), self.bareme,',
  'g = R.fabriquer_gestionnaire("cle-factice-essai", amont.url, tuple(modeles), self.bareme,'),
 ('env = {"PATH": "/usr/bin:/bin", "ROLE_POLE": "proposeur_ideation", "MODELE_DEMANDE_POLE": "gpt-6-astra", **env_plus}',
  'env = {"PATH": "/usr/bin:/bin", "ROLE_POLE": "proposeur_ideation", "MODELE_DEMANDE_POLE": MODELE, **env_plus}'),
 ('"--url-relais", url, "--modele", "gpt-6-astra", *args]', '"--url-relais", url, "--modele", MODELE, *args]'),
 ('corps = json.dumps({"model": "gpt-6-astra", "messages"', 'corps = json.dumps({"model": MODELE, "messages"'),
 ('assert v2["version"] == "sonde_astra_affinage_v2" and v2["ok"] is True       # format lu par le lanceur de l\'affinage v6',
  'assert v2["version"] == "sonde_astra_affinage_v3" and v2["ok"] is True       # format lu par le lanceur de l\'affinage v8\n        assert v2["modele_servi"] == MODELE and o["modele"] == MODELE'),
 ('"2026-11-18T11:00:00Z"', '"2026-11-22T11:00:00Z"'),
 ('o["jour"] == "2026-11-18"', 'o["jour"] == "2026-11-22"'),
]
for a, b in rempl:
    assert t.count(a) >= 1, a
    t = t.replace(a, b)
restes = [l for l in t.splitlines() if "gpt-6-astra" in l and "ANCIEN" not in l]
assert not restes, restes
t += '''

# --- 3. mutations propres à la v2 ---------------------------------------------------------------------------------------------


def test_v2_relais_jete_aux_prix_de_la_v1_echec_de_configuration(pieces):
    amont = FauxAmont()
    relais = RelaisFactice(amont, reserve=0.01, prix=(10, 50, 1))     # prix de l'ancien modèle : plus ceux de gpt-6.2-astra
    try:
        assert _sonder(pieces, relais, amont) == 1
        o = json.loads((pieces["tmp"] / "sonde-a.json").read_text())
        assert o["echec_de_configuration"] is True and any("8 / 40" in m for m in o["motif"]) and amont.recues == 0
    finally:
        relais.fermer()


def test_v2_relais_jete_qui_ne_permet_que_l_ancien_modele_refuse(pieces):
    amont = FauxAmont(modele=ANCIEN)
    relais = RelaisFactice(amont, reserve=0.01, modeles=(ANCIEN,))
    try:
        with pytest.raises(S.Refus, match="modeles_permis"):
            _sonder(pieces, relais, amont)
        assert amont.recues == 0 and not list(pieces["tmp"].glob("sonde-*.json"))
    finally:
        relais.fermer()


def test_v2_ancien_modele_servi_par_l_amont_echec_rapporte(pieces):
    amont = FauxAmont(modele=ANCIEN)                                  # l'amont sert l'ancien modèle : pas « ok »
    relais = RelaisFactice(amont, reserve=0.01)
    try:
        assert _sonder(pieces, relais, amont) == 1
        o = json.loads((pieces["tmp"] / "sonde-a.json").read_text())
        assert o["ok"] is False and o["rapport_v2"]["ok"] is False
    finally:
        relais.fermer()


def test_v2_sonde_appelee_d_une_autre_empreinte_refusee(tmp_path):
    faux = tmp_path / "sonde_astra_affinage_v3.py"
    faux.write_bytes((RACINE / "scripts" / "sonde_astra_affinage_v3.py").read_bytes() + b"\\n")
    with pytest.raises(S.Refus, match="sonde v3"):
        S.charger_sonde_v2(faux)
    with pytest.raises(S.Refus, match="sonde v3"):                     # l'ancienne sonde (v2) : refusée aussi
        S.charger_sonde_v2(RACINE / "scripts" / "sonde_astra_affinage_v2.py")
    m = S.charger_sonde_v2()
    assert m.MODELE == MODELE and m.PRIX == ("8", "40") and m.VERSION == "sonde_astra_affinage_v3"
'''
(racine / "tests/test_sonde_astra_courses_v2.py").write_text(t, encoding="utf-8")
print("écrit")
