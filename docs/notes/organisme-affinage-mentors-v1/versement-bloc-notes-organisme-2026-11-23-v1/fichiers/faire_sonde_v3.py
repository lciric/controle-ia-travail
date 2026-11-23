import hashlib, sys
from pathlib import Path
racine = Path(sys.argv[1])
def r(s, a, b, n=1):
    assert s.count(a) == n, (s.count(a), a[:80]); return s.replace(a, b)
src = (racine / "scripts/sonde_astra_courses_v2.py").read_text(encoding="utf-8")
assert hashlib.sha256(src.encode()).hexdigest() == "80074c82c8ea79d059c9f74b3ae89f7f50635283672a4bd26f1c2e77c27d6704"
src = r(src, '"""Sonde d\'Astra commune — version 2 (`gpt-6.2-astra`, pour le lanceur v11 de la course d\'affinage).\n',
        '"""Sonde d\'Astra commune — version 3 (`gpt-6.2-astra`, variable de clé du relais jeté contrôlée ; lanceur v11c).\n\n'
        'Version 3 (R12 ; la v2, `scripts/sonde_astra_courses_v2.py`, `80074c82…`, reste en place). Seul changement, sur le constat 9\n'
        'de la contre-lecture du lanceur v11b (`contre-lecture-lanceur-v11b-v1.md`, `cd7e5455…`) : la ligne de commande du relais\n'
        'jeté, lue par son PID, doit porter `--variable-cle OPENAI_API_KEY_2` (la clé d\'Astra de la course v11) ; sinon refus avant\n'
        'tout appel (code 2). Version écrite au rapport : `sonde_astra_courses_v3`. Texte de la v2 ci-dessous.\n\n'
        'Sonde d\'Astra commune — version 2 (`gpt-6.2-astra`, pour le lanceur v11 de la course d\'affinage).\n')
src = r(src, 'VERSION = "sonde_astra_courses_v2"', 'VERSION = "sonde_astra_courses_v3"\nVARIABLE_CLE = "OPENAI_API_KEY_2"  # v3 : clé d\'Astra de la course v11, lue au relais jeté par son PID')
src = r(src, '''    if _valeur(cmdline, "--port") != str(port):
        raise Refus(f"relais jeté (PID {pid}) : --port différent de l'adresse donnée ({port})")''',
'''    if _valeur(cmdline, "--port") != str(port):
        raise Refus(f"relais jeté (PID {pid}) : --port différent de l'adresse donnée ({port})")
    if cmdline.count("--variable-cle") != 1 or _valeur(cmdline, "--variable-cle") != VARIABLE_CLE:  # v3, constat 9
        raise Refus(f"relais jeté (PID {pid}) : --variable-cle {_valeur(cmdline, '--variable-cle')!r}, {VARIABLE_CLE} exigée "
                    "(une seule fois)")''')
src = r(src, '''    return {"url": url, "port": port, "pid": pid, "programme": progs[0], "programme_sha256": EMPREINTE_RELAIS,''',
        '''    return {"url": url, "port": port, "pid": pid, "programme": progs[0], "programme_sha256": EMPREINTE_RELAIS,
            "variable_cle": VARIABLE_CLE,''')
(racine / "scripts/sonde_astra_courses_v3.py").write_text(src, encoding="utf-8")

t = (racine / "tests/test_sonde_astra_courses_v2.py").read_text(encoding="utf-8")
assert hashlib.sha256(t.encode()).hexdigest() == "742f66beef23b83d8b0a5ab31495e2d343309dd15112d6f98664d36adaf6a44c"
t = r(t, '"""Essais de la sonde d\'Astra commune, version 2 (`scripts/sonde_astra_courses_v2.py`,',
      '"""Essais de la sonde d\'Astra commune, version 3 (`scripts/sonde_astra_courses_v3.py` : variable de clé du relais jeté\n'
      'contrôlée), repris des essais de la v2 (`742f66be…`) ; texte d\'origine : essais de la version 2 (`scripts/sonde_astra_courses_v2.py`,')
t = r(t, 'S = _charger("sonde_astra_courses_v2", RACINE / "scripts" / "sonde_astra_courses_v2.py")',
      'S = _charger("sonde_astra_courses_v3", RACINE / "scripts" / "sonde_astra_courses_v3.py")')
# toute ligne de commande factice du relais jeté porte la variable de la course
n = t.count('"--port", str(relais.port)]')
t = t.replace('"--port", str(relais.port)]', '"--port", str(relais.port), "--variable-cle", "OPENAI_API_KEY_2"]')
t = r(t, '"port": [sys.executable, str(pieces["relais"]), "--port", "1"]}',
      '"port": [sys.executable, str(pieces["relais"]), "--port", "1", "--variable-cle", "OPENAI_API_KEY_2"]}')
t += '''

# --- v3 : variable de clé du relais jeté (constat 9 de la contre-lecture du lanceur v11b) -----------------------------------------


@pytest.mark.parametrize("variable", [None, "OPENAI_API_KEY", "OPENAI_API_KEY_3", "double"])
def test_v3_relais_jete_d_une_autre_variable_de_cle_refuse(pieces, variable):
    amont = FauxAmont()
    relais = RelaisFactice(amont, reserve=0.01)
    t = pieces["tmp"]
    cmd = [sys.executable, "-I", "-B", str(pieces["relais"]), "--port", str(relais.port)]
    if variable == "double":
        cmd += ["--variable-cle", "OPENAI_API_KEY_2", "--variable-cle", "OPENAI_API_KEY"]
    elif variable is not None:
        cmd += ["--variable-cle", variable]
    try:
        with pytest.raises(S.Refus, match="variable-cle"):
            S.sonder(pieces["commande"], relais.url, os.getpid(), t / "s-var.json", t / "v2-var.json",
                     lire_cmd=lambda pid: cmd, amont=amont.url, horodatage=lambda: "2026-11-22T11:00:00Z")
        assert amont.recues == 0 and relais.compteur.appels == 0 and not (t / "s-var.json").exists()
    finally:
        relais.fermer()


def test_v3_cas_sain_variable_ecrite_au_rapport(pieces):
    amont = FauxAmont()
    relais = RelaisFactice(amont, reserve=0.01)
    try:
        assert _sonder(pieces, relais, amont, nom="var") == 0
        o = json.loads((pieces["tmp"] / "sonde-var.json").read_text())
        assert o["version"] == "sonde_astra_courses_v3" and o["relais_jete"]["variable_cle"] == "OPENAI_API_KEY_2"
    finally:
        relais.fermer()
'''
(racine / "tests/test_sonde_astra_courses_v3.py").write_text(t, encoding="utf-8")
print("sonde v3 ;", n, "lignes de commande factices complétées")
