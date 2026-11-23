p = 'tests/test_amorce_ligne_1_bras_a_v3.py'
s = open(p, encoding='utf-8').read()


def r(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:90])
    s = s.replace(a, b)


s = s.replace('lanceur_machine_ligne_1_bras_a_v2', 'lanceur_machine_ligne_1_bras_a_v3')
s = s.replace('construire_branche_entree_ligne_1_bras_a_v2', 'construire_branche_entree_ligne_1_bras_a_v3')
r('''"""Essais de la machine autonome de la ligne 1 de carte du bras A, version 2 (les essais v1 restent, R12)''',
  '''"""Essais de la machine autonome de la ligne 1 de carte du bras A, version 3 (amorce d'appel v2, amorce complète v3,
construction v3, lanceur v3 ; corrections de la contre-lecture de la v2 : reprise par bash sous `sh`, arrêt redemandé
quand le premier échoue, fichier trop gros gardé hors de la poussée, secours à 25 min, groupe de processus coupé).
Les essais v1 et v2 restent (R12). Ce qui suit décrit la version 2''')
r('AMORCE = DEPOT / "scripts/amorce_ligne_1_bras_a_v2.sh"\nAPPEL = DEPOT / "scripts/amorce_appel_ligne_1_bras_a_v1.sh"\n',
  'AMORCE = DEPOT / "scripts/amorce_ligne_1_bras_a_v3.sh"\nAPPEL = DEPOT / "scripts/amorce_appel_ligne_1_bras_a_v2.sh"\n')
r('''             "cat > /dev/null\\n"''', '''             "cat > /dev/null\\n"
             "if [ -n \\"${FAUX_CURL_ECHECS:-}\\" ]; then k=$(cat \\"$FAUX_CURL_JOURNAL.compte\\" 2>/dev/null || echo 0); k=$((k + 1))\\n"
             "  echo $k > \\"$FAUX_CURL_JOURNAL.compte\\"; [ $k -le $FAUX_CURL_ECHECS ] && { printf '%s %s\\\\n' \\"$m\\" \\"$u\\" >> \\"$FAUX_CURL_JOURNAL\\"; printf '500'; exit 0; }; fi\\n"''')
r('''def jouer(scenario: str, branche_entree: str, commit_entree: str, distant=None, racine=None, delai=900, **env_de_plus):''',
  '''def jouer(scenario: str, branche_entree: str, commit_entree: str, distant=None, racine=None, delai=900, coquille="bash",
          **env_de_plus):''')
r('''           "AMORCE_GRACE_S": "3", **SECRETS}''', '''           "AMORCE_GRACE_S": "3", "AMORCE_PAS_ARRET_S": "1", **SECRETS}''')
r('''    r = subprocess.run(["bash", str(APPEL)], env=env, capture_output=True, text=True, timeout=delai)''',
  '''    r = subprocess.run([coquille, str(APPEL)], env=env, capture_output=True, text=True, timeout=delai)''')
r('''    appels = journal_curl.read_text(encoding="utf-8").splitlines() if journal_curl.exists() else []''',
  '''    appels = journal_curl.read_text(encoding="utf-8").splitlines() if journal_curl.exists() else []
    appels = [a for a in appels if not a.startswith("GET ")]        # relectures de l'état, à part''')
r('''"--dossier", str(tmp_path / "d")], capture_output=True''', '''"--dossier", str(tmp_path / "d"), "--sans-fetch"], capture_output=True''')
r('''"APPEL ARRET : commit cloné différent" in journal''', '''"APPEL ARRET : commit différent" in journal''')
r('''    assert r.returncode == 3 and "empreinte de l'amorce complète" in journal''', '''    assert r.returncode == 3 and "APPEL ARRET : empreinte" in journal''')
r('''    assert r.returncode == 2 and "variable de jouet hors jouet" in r.stdout''', '''    assert r.returncode == 2 and "ARRET : jouet" in r.stdout''')
r('''    assert ligne.endswith("--onstart scripts/amorce_appel_ligne_1_bras_a_v1.sh")''',
  '''    assert "--onstart scripts/amorce_appel_ligne_1_bras_a_v2.sh 2>&1 | " in ligne
    assert ligne.endswith("scripts/lanceur_machine_ligne_1_bras_a_v3.py masquer")''')
r('''    assert "-e GH_TOKEN=$GH_TOKEN -e HF_TOKEN=$HF_TOKEN " in brut''', '''    assert "-e GH_TOKEN=${GH_TOKEN:?} -e HF_TOKEN=${HF_TOKEN:?} " in brut''')
s += '''

# --- Corrections de la contre-lecture de la v2 -------------------------------------------------------------------------

def test_appel_sous_sh_repris_par_bash(monde):
    """M1 : jouée par `sh` (dash), l'amorce d'appel se reprend par bash, puis arrête sur la variable absente."""
    r, journal, appels, racine = jouer("appel-sh", "entree/jouet-court", "a" * 40, coquille="sh", AMORCE_SHA256=None)
    assert r.returncode == 3 and "AMORCE_SHA256 absente" in journal and "Bad substitution" not in r.stderr, r.stderr
    assert appels == ["PUT https://console.vast.ai/api/v0/instances/4242/"]


def test_appel_premier_arret_en_echec_redemande(monde):
    """M2 : le premier PUT échoue (HTTP 500) ; l'arrêt est redemandé."""
    commit = entree("entree/jouet-appel-echec")
    r, journal, appels, _ = jouer("appel-echec", "entree/jouet-appel-echec", "f" * 40, FAUX_CURL_ECHECS="1")
    assert r.returncode == 3 and "PUT 1 : 500" in journal and "PUT 2 : 200" in journal, journal
    assert appels == ["PUT https://console.vast.ai/api/v0/instances/4242/"] * 2


def test_amorce_complete_premier_arret_en_echec_redemande(monde, tmp_path):
    """M2 : poussée non prouvée, premier PUT en échec : l'amorce complète redemande l'arrêt, relit l'état, ne détruit
    jamais."""
    nu = tmp_path / "rejet.git"
    _git("clone", "-q", "--bare", str(monde["nu"]), str(nu))
    crochet = nu / "hooks/pre-receive"
    crochet.write_text("#!/bin/sh\\nwhile read a b ref; do case \\"$ref\\" in refs/heads/calcul/*) exit 1;; esac; done\\n")
    crochet.chmod(0o755)
    commit = entree("entree/jouet-arret-echec", distant=nu)
    r, journal, appels, _ = jouer("arret-echec", "entree/jouet-arret-echec", commit, distant=nu, FAUX_CURL_ECHECS="1",
                                  JOUET_INJECTEUR=None, JOUET_CONSTANTES=None)
    assert r.returncode == 3, journal + r.stderr
    assert "essai 1, disque gardé" in journal and "HTTP 500" in journal and "essai 2, disque gardé" in journal
    assert "état relu" in journal
    assert appels == ["PUT https://console.vast.ai/api/v0/instances/4242/"] * 2


def test_fichier_trop_gros_garde_hors_de_la_poussee(monde):
    """m10 : au-delà du seuil (ici 5 000 octets en jouet), le fichier reste sur le disque et le manifeste le dit."""
    commit = entree("entree/jouet-gros")
    r, journal, appels, racine = jouer("gros", "entree/jouet-gros", commit, AMORCE_TAILLE_MAX_O="5000",
                                       JOUET_INJECTEUR=None, JOUET_CONSTANTES=None)
    assert r.returncode == 0 and "non poussé : empreintes-posees.txt" in journal, journal
    assert (racine / "ligne-1-bras-a/hors-versement/empreintes-posees.txt").is_file()
    v = verification("calcul/jouet-gros")
    assert v.returncode == 0, v.stderr
    sortie = json.loads(v.stdout)
    m = json.loads((Path(sortie["copie_locale"]) / sortie["dossier"] / "manifeste-du-versement.json").read_text(encoding="utf-8"))
    assert {"nom": "empreintes-posees.txt", "pourquoi": "plus de 100 Mo : non poussé, gardé sur le disque de la machine"} \\
        in m["manquants"]
    assert "empreintes-posees.txt" not in {x["nom"] for x in m["inventaire"]}


def test_masquer_recopie_l_entree_masquee():
    r = subprocess.run([sys.executable, str(DEPOT / "scripts/lanceur_machine_ligne_1_bras_a_v3.py"), "masquer"],
                       input=f"erreur : {SECRETS['GH_TOKEN']} et api_key\\n", capture_output=True, text=True,
                       env=dict(os.environ, **SECRETS))
    assert r.returncode == 0 and r.stdout == "erreur : [masqué] et api_key\\n"


def test_constantes_de_la_v3():
    texte = AMORCE.read_text(encoding="utf-8")
    assert 'SECOURS_S="${AMORCE_SECOURS_S:-1500}"' in texte and "setsid" in texte and "timeout 900 git" in texte
    assert "-c credential.helper= -c credential.helper=" in texte and "env -u GH_TOKEN -u HF_TOKEN -u CONTAINER_API_KEY" in texte
    appel = APPEL.read_text(encoding="utf-8")
    assert appel.startswith('[ -n "${BASH_VERSION:-}" ] || exec bash "$0" "$@"\\n')
    assert "apt-get install -y -qq git curl ca-certificates" in appel and "python3 -Ic" in appel
'''
open(p, 'w', encoding='utf-8').write(s)
