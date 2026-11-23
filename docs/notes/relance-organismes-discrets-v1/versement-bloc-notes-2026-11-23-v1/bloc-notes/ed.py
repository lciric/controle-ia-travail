p = 'tests/test_amorce_ligne_1_bras_a_v2.py'
s = open(p, encoding='utf-8').read()


def r(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:90])
    s = s.replace(a, b)


r('''"""Essais de la machine autonome de la ligne 1 de carte du bras A, version 1 : construction de la branche d'entrée
(`scripts/construire_branche_entree_ligne_1_bras_a_v1.py`), amorce (`scripts/amorce_ligne_1_bras_a_v1.sh`) et lanceur
de la session (`scripts/lanceur_machine_ligne_1_bras_a_v1.py`).''', '''"""Essais de la machine autonome de la ligne 1 de carte du bras A, version 2 (les essais v1 restent, R12) : construction
de la branche d'entrée v2 (`scripts/construire_branche_entree_ligne_1_bras_a_v2.py`, 58 fichiers : l'amorce complète y
est portée), amorce d'appel (`scripts/amorce_appel_ligne_1_bras_a_v1.sh`, onstart de moins de 2 500 octets), amorce
complète v2 (`scripts/amorce_ligne_1_bras_a_v2.sh`, lancée par l'appel) et lanceur de la session v2
(`scripts/lanceur_machine_ligne_1_bras_a_v2.py`). Le monde jouet passe désormais par l'amorce d'appel. Heure du plafond
(règle v2) : coupe, versement, preuve, grâce en marche, destruction ; sans preuve, arrêt seulement.''')
r('AMORCE = DEPOT / "scripts/amorce_ligne_1_bras_a_v1.sh"\n',
  'AMORCE = DEPOT / "scripts/amorce_ligne_1_bras_a_v2.sh"\nAPPEL = DEPOT / "scripts/amorce_appel_ligne_1_bras_a_v1.sh"\n')
r('''    for x in modules + list(cb.EXIGENCES):''', '''    for x in modules + list(cb.EXIGENCES) + [cb.AMORCE_COMPLETE]:''')
r('''           "JOUET_CONSTANTES": "essai/constantes.json", "GIT_CONFIG_NOSYSTEM": "1", **SECRETS}''',
  '''           "JOUET_CONSTANTES": "essai/constantes.json", "GIT_CONFIG_NOSYSTEM": "1", "AMORCE_SHA256": _sha(AMORCE),
           "AMORCE_GRACE_S": "3", **SECRETS}''')
r('''    r = subprocess.run(["bash", str(AMORCE)], env=env, capture_output=True, text=True, timeout=delai)
    journal = (racine / "ligne-1-bras-a/journal-amorce.txt").read_text(encoding="utf-8")''',
  '''    r = subprocess.run(["bash", str(APPEL)], env=env, capture_output=True, text=True, timeout=delai)
    journal = "".join((racine / "ligne-1-bras-a" / n).read_text(encoding="utf-8")
                      for n in ("journal-appel.txt", "journal-amorce.txt") if (racine / "ligne-1-bras-a" / n).exists())''')
r('''def test_commit_d_entree_different_echec(monde):
    commit = entree("entree/jouet-commit")
    r, journal, appels, _ = jouer("commit", "entree/jouet-commit", "f" * 40)
    assert r.returncode == 0 and "≠ COMMIT_ENTREE" in journal and "course lancée" not in journal
    assert appels[-1].startswith("DELETE ")
''', '''def test_commit_d_entree_different_arret_par_l_appel(monde):
    """Erreur avant l'exec de l'amorce complète : arrêt simple, jamais de destruction (rien n'est produit)."""
    commit = entree("entree/jouet-commit")
    r, journal, appels, racine = jouer("commit", "entree/jouet-commit", "f" * 40)
    assert r.returncode == 3 and "APPEL ARRET : commit cloné différent" in journal, journal + r.stdout
    assert appels == ["PUT https://console.vast.ai/api/v0/instances/4242/"]
    assert not (racine / "ligne-1-bras-a/journal-amorce.txt").exists()
    exiger_aucun_secret(racine, textes=[r.stdout, r.stderr])


# --- Amorce d'appel ----------------------------------------------------------------------------------------------------

def test_amorce_d_appel_courte():
    assert APPEL.stat().st_size < 2500


def test_appel_empreinte_de_l_amorce_complete_fausse_arret(monde):
    commit = entree("entree/jouet-appel-sha")
    r, journal, appels, racine = jouer("appel-sha", "entree/jouet-appel-sha", commit, AMORCE_SHA256="0" * 64)
    assert r.returncode == 3 and "empreinte de l'amorce complète" in journal
    assert appels == ["PUT https://console.vast.ai/api/v0/instances/4242/"]
    assert not (racine / "ligne-1-bras-a/journal-amorce.txt").exists()
    # l'aide d'identification est inscrite dans la configuration du clone (R-5101), par le nom du jeton seulement
    aide = subprocess.run(["git", "-C", str(racine / "ligne-1-bras-a/entree"), "config", "credential.helper"],
                          capture_output=True, text=True).stdout
    assert "x-access-token" in aide and "${GH_TOKEN}" in aide
    exiger_aucun_secret(racine, textes=[r.stdout, r.stderr])


@pytest.mark.parametrize("absente", ["GH_TOKEN", "COMMIT_ENTREE", "AMORCE_SHA256", "CONTAINER_API_KEY"])
def test_appel_variable_absente_arret_sans_clone(monde, absente):
    r, journal, appels, racine = jouer(f"appel-{absente.lower()}", "entree/jouet-court", "a" * 40, **{absente: None})
    assert r.returncode == 3 and f"{absente} absente" in journal
    assert appels == ["PUT https://console.vast.ai/api/v0/instances/4242/"]
    assert not (racine / "ligne-1-bras-a/entree").exists()


def test_appel_hors_jouet_refuse_les_variables_de_jouet(tmp_path):
    r = subprocess.run(["bash", str(APPEL)], env={"PATH": os.environ["PATH"], "RACINE_AMORCE": str(tmp_path / "r")},
                       capture_output=True, text=True, timeout=60)
    assert r.returncode == 2 and "variable de jouet hors jouet" in r.stdout and not (tmp_path / "r").exists()
''')
r('''def test_heure_du_plafond_destruction_quel_que_soit_le_versement(monde):
    """La minuterie détruit à l'heure du plafond même sans versement prouvé (borne de la dépense)."""
    commit = entree("entree/jouet-heure-plafond")
    r, journal, appels, _ = jouer("heure-plafond", "entree/jouet-heure-plafond", commit, AMORCE_PLAFOND_S="0",
                                  JOUET_INJECTEUR=None, JOUET_CONSTANTES=None)
    avant_poussee = journal.split("POUSSÉE PROUVÉE")[0]
    assert "MINUTERIE : heure du plafond atteinte" in avant_poussee and "(heure du plafond) : DELETE" in avant_poussee
    assert appels[0] == "DELETE https://console.vast.ai/api/v0/instances/4242/"
''', '''def test_heure_du_plafond_poussee_prouvee_grace_puis_destruction(monde):
    """Règle v2 : la minuterie coupe la course ; le fil principal verse, prouve, passe la grâce en marche, relit la
    preuve, puis détruit ; aucune destruction avant."""
    commit = entree("entree/jouet-heure-plafond")
    ecart = int(time.time() - MAINTENANT.timestamp()) + 25
    r, journal, appels, racine = jouer("heure-plafond", "entree/jouet-heure-plafond", commit, AMORCE_PLAFOND_S=str(ecart))
    assert r.returncode == 0, journal + r.stderr
    assert "MINUTERIE : heure du plafond atteinte" in journal and "TERM envoyé" in journal
    assert "coupée par la minuterie à l'heure du plafond" in journal
    suite = journal.split("POUSSÉE PROUVÉE")[1]
    assert "grâce de 3 s en marche" in suite and "preuve relue après la grâce" in suite
    assert appels == ["DELETE https://console.vast.ai/api/v0/instances/4242/"]
    exiger_aucun_secret(racine, textes=[r.stdout, r.stderr])


def test_heure_du_plafond_sans_poussee_prouvee_arret_seulement(monde, tmp_path):
    nu = tmp_path / "rejet.git"
    _git("clone", "-q", "--bare", str(monde["nu"]), str(nu))
    crochet = nu / "hooks/pre-receive"
    crochet.write_text("#!/bin/sh\\nwhile read a b ref; do case \\"$ref\\" in refs/heads/calcul/*) exit 1;; esac; done\\n")
    crochet.chmod(0o755)
    commit = entree("entree/jouet-plafond-rejet", distant=nu)
    r, journal, appels, _ = jouer("plafond-rejet", "entree/jouet-plafond-rejet", commit, distant=nu, AMORCE_PLAFOND_S="0",
                                  JOUET_INJECTEUR=None, JOUET_CONSTANTES=None)
    assert r.returncode == 3, journal + r.stderr
    assert "heure du plafond atteinte" in journal and "nœud pour la mère" in journal
    assert appels == ["PUT https://console.vast.ai/api/v0/instances/4242/"]       # jamais de destruction
''')
r('''    assert compte["nombre_de_fichiers"] == 57 and''', '''    assert compte["nombre_de_fichiers"] == 58 and''')
r('''    assert lignes["constat-ligne-1.json"] == _sha(constat)''', '''    assert lignes["constat-ligne-1.json"] == _sha(constat)
    assert lignes[cb.AMORCE_COMPLETE] == _sha(AMORCE) == compte["amorce_complete_sha256"]''')
r('''    """La vraie branche (sans poussée) : 57 fichiers''', '''    """La vraie branche (sans poussée) : 58 fichiers''')
r('''    assert ligne.endswith("--onstart scripts/amorce_ligne_1_bras_a_v1.sh")''',
  '''    assert ligne.endswith("--onstart scripts/amorce_appel_ligne_1_bras_a_v1.sh")''')
open(p, 'w', encoding='utf-8').write(s)
