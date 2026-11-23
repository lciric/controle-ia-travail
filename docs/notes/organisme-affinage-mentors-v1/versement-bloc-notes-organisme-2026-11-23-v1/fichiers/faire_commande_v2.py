import hashlib, sys
from pathlib import Path
racine = Path(sys.argv[1])
def r(s, a, b, n=1):
    assert s.count(a) == n, (s.count(a), a[:80]); return s.replace(a, b)
src = (racine / "scripts/commande_gemini_flux_v1.py").read_text(encoding="utf-8")
assert hashlib.sha256(src.encode()).hexdigest() == "6aaf235df31eccd7199c0bcea1e8b68009d56d03c66a01427d05ae8137fdbf55"
src = r(src, '"""Commande externe Gemini **en flux, sous la garde des appels à Google** pour l\'orchestrateur du pôle — version 1.\n',
'''"""Commande externe Gemini **en flux, sous la garde des appels à Google** pour l'orchestrateur du pôle — version 2.

Version 2 (R12 ; la v1, `scripts/commande_gemini_flux_v1.py`, `6aaf235d…`, reste en place). Seul changement, sur le constat 12
de la contre-lecture du lanceur v11b (`contre-lecture-lanceur-v11b-v1.md`, `cd7e5455…`) : le pire cas avant l'envoi suppose
la réflexion **comprise** dans `maxOutputTokens` (page de Google versée sur `main`, `fe0b8d88…`, l. 914-916 et 1273-1274) ;
après la réponse, la commande vérifie cette hypothèse sur l'usage lu : `candidatesTokenCount + thoughtsTokenCount ≤
maxOutputTokens`. Le champ `hypothese_sortie_maximale_tenue` (vrai, faux, ou null si l'usage est illisible) est écrit dans
chaque ligne rendue après un envoi ; s'il est faux, la commande le signale sur sa sortie d'erreur (ligne
`commande-gemini-flux-v2 : HYPOTHESE_SORTIE_MAXIMALE_TOMBEE …`, journalisée avec la ligne rendue), sans changer le code : le
coût lu est compté tel quel et reste gardé par le plafond de session (code 7 au-delà). Texte de la v1 ci-dessous.

Commande externe Gemini en flux, sous la garde des appels à Google — version 1.
''')
src = r(src, 'VERSION = "commande-gemini-flux-v1"', 'VERSION = "commande-gemini-flux-v2"')
src = r(src, '    etat = {"pire_cas": None, "envoye": False, "reglages": None}',
        '    etat = {"pire_cas": None, "envoye": False, "reglages": None, "hypothese": None, "sortie_lue": None}')
src = r(src, '''            cout = int(usage["promptTokenCount"]) * pe + sortie * ps
''', '''            cout = int(usage["promptTokenCount"]) * pe + sortie * ps
            etat["sortie_lue"] = sortie
            etat["hypothese"] = sortie <= args.max_sortie_jetons  # v2, constat 12 : réflexion comprise dans la sortie maximale
''')
src = r(src, '''                   "defaut_google": None}''', '''                   "defaut_google": None, "hypothese_sortie_maximale_tenue": etat["hypothese"]}''')
src = r(src, '''                 "defaut_google": e.extra.get("defaut_google")}''',
        '''                 "defaut_google": e.extra.get("defaut_google")}
        if etat["envoye"]:
            ligne["hypothese_sortie_maximale_tenue"] = etat["hypothese"]''')
src = r(src, '''    code, ligne = executer(args, consigne, environ, ouvreur)
''', '''    code, ligne = executer(args, consigne, environ, ouvreur)
    if ligne.get("hypothese_sortie_maximale_tenue") is False:  # v2 : signalé et journalisé, jamais tu
        u = ligne.get("usage") or {}
        print(f"{VERSION} : HYPOTHESE_SORTIE_MAXIMALE_TOMBEE : réflexion {u.get('thoughtsTokenCount')!r} + sortie "
              f"{u.get('candidatesTokenCount')!r} > maxOutputTokens {args.max_sortie_jetons} : le pire cas écrit avant l'envoi "
              "ne bornait pas cet appel", file=sys.stderr)
''')
(racine / "scripts/commande_gemini_flux_v2.py").write_text(src, encoding="utf-8")

t = (racine / "tests/test_commande_gemini_flux_v1.py").read_text(encoding="utf-8")
assert hashlib.sha256(t.encode()).hexdigest() == "e92ff4c99d1eb54b6a49efa9b3ad9c052a780082593bf048192bc3be7be3af0f"
t = r(t, '"""Essais de la commande Gemini en flux sous la garde des appels à Google (`scripts/commande_gemini_flux_v1.py`), hors ligne.',
      '"""Essais de la commande Gemini en flux, version 2 (`scripts/commande_gemini_flux_v2.py`), repris des essais de la v1 (`e92ff4c9…`)\n'
      'et passés aux réglages de production du lanceur v11c (constat 13 : Carbon et Argon à 4 / 20 USD par million, Carbon\n'
      'provision 28 672 et sortie 65 536, juge d\'Argon à 1,00 USD), plus les essais de l\'hypothèse « réflexion comprise dans la\n'
      'sortie maximale » (constat 12). Texte d\'origine : essais de la commande en flux (`scripts/commande_gemini_flux_v1.py`), hors ligne.')
t = r(t, 'COMMANDE = RACINE / "scripts" / "commande_gemini_flux_v1.py"', 'COMMANDE = RACINE / "scripts" / "commande_gemini_flux_v2.py"')
t = r(t, '''# réglages du lanceur v11 pour Carbon (niveau le plus haut, provision 28 672, sortie 49 152 : texte 20 480)
ARGS = ["--espece", "carbon", "--modele", MODELE, "--prix-entree", "8.3", "--prix-sortie", "41.5", "--niveau-reflexion", "high",
        "--provision-pensee-jetons", "28672", "--max-sortie-jetons", "49152", "--delai-s", "60", "--delai-requete-s", "10"]''',
'''# réglages de production du lanceur v11c pour Carbon (ARGUMENTS_COMMANDES["carbon"] : niveau « high », provision 28 672,
# sortie 65 536, 4 / 20 USD par million ; délais raccourcis pour l'essai seulement)
ARGS = ["--espece", "carbon", "--modele", MODELE, "--prix-entree", "4", "--prix-sortie", "20", "--niveau-reflexion", "high",
        "--provision-pensee-jetons", "28672", "--max-sortie-jetons", "65536", "--delai-s", "60", "--delai-requete-s", "10"]''')
t = r(t, '''amont.corps["generationConfig"]["maxOutputTokens"] == 49152
    assert ligne["cout_usd"] == pytest.approx((900 * 8.3 + (300 + 1200) * 41.5) / 1e6)''',
'''amont.corps["generationConfig"]["maxOutputTokens"] == 65536
    assert ligne["cout_usd"] == pytest.approx((900 * 4 + (300 + 1200) * 20) / 1e6)
    assert ligne["hypothese_sortie_maximale_tenue"] is True''')
t = r(t, '''args=ARGS + ["--mots-invite", "5000"])   # 5 000 × 4,2 ≥ 20 480''', '''args=ARGS + ["--mots-invite", "9000"])   # 9 000 × 4,2 ≥ 36 864''')
t = r(t, '''args=ARGS + ["--mots-invite", "4000"])   # 16 800 < 20 480''', '''args=ARGS + ["--mots-invite", "8000"])   # 33 600 < 36 864''')
t = r(t, '''plafond="1.50")      # 49 152 × 41,5 / 10⁶ = 2,04 > 1,50''', '''plafond="1.30")      # 65 536 × 20 / 10⁶ = 1,31 > 1,30''')
t = r(t, '''ligne["cout_origine"] == "pire_cas" and ligne["cout_usd"] > 2.0''',
      '''ligne["cout_origine"] == "pire_cas" and ligne["cout_usd"] > 1.31''')
t = r(t, 'def jouer_argon(pieces, url, args=None, plafond="2.00", role="juge_ideation"):',
      'def jouer_argon(pieces, url, args=None, plafond="1.00", role="juge_ideation"):  # v2 : juge à 1,00 (production)')
t = r(t, '@pytest.mark.parametrize("role,plafond", [("juge_ideation", "2.00"), ("proposeur_ideation", "3.00")])',
      '@pytest.mark.parametrize("role,plafond", [("juge_ideation", "1.00"), ("proposeur_ideation", "3.00")])')
t += '''

# --- v2 : hypothèse « réflexion comprise dans la sortie maximale » (constat 12) ---------------------------------------------------


def jouer_complet(pieces, url, args=None, plafond="3.00"):
    env = {"PATH": "/usr/bin:/bin", "PLAFOND_SESSION_USD": plafond, "ROLE_POLE": "proposeur_ideation", "MODELE_DEMANDE_POLE": MODELE}
    a = (args if args is not None else ARGS) + ["--url-base", url + "/v1beta", "--garde", str(pieces["garde"])]
    p = subprocess.run([sys.executable, "-I", "-B", str(COMMANDE)] + a, input=b"Consigne d'essai.", env=env, capture_output=True,
                       timeout=90)
    return p.returncode, json.loads(p.stdout.decode().splitlines()[-1]), p.stderr.decode()


def test_v2_hypothese_tenue_au_plafond_exact(pieces):
    amont = FauxAmont(pensees=60000, sortie=5536)                                   # 65 536 : égal au plafond
    code, ligne, err = jouer_complet(pieces, relais_devant(pieces, amont))
    assert code == 0 and ligne["hypothese_sortie_maximale_tenue"] is True and "HYPOTHESE" not in err


def test_v2_hypothese_tombee_signalee_et_journalisee(pieces):
    amont = FauxAmont(pensees=60000, sortie=10000)                                  # 70 000 > 65 536
    code, ligne, err = jouer_complet(pieces, relais_devant(pieces, amont))
    assert code == 0 and ligne["texte"] == "réponse d'essai"                        # réponse gardée, coût lu compté
    assert ligne["hypothese_sortie_maximale_tenue"] is False
    assert ligne["cout_usd"] == pytest.approx((900 * 4 + 70000 * 20) / 1e6) and ligne["cout_usd"] > ligne["pire_cas_usd"]
    assert "HYPOTHESE_SORTIE_MAXIMALE_TOMBEE" in err and "65536" in err


def test_v2_hypothese_tombee_et_plafond_depasse_code_7(pieces):
    amont = FauxAmont(pensees=60000, sortie=10000)
    code, ligne, err = jouer_complet(pieces, relais_devant(pieces, amont), plafond="1.35")   # pire 1,3144 ≤ 1,35 < coût 1,4036
    assert code == 7 and ligne["hypothese_sortie_maximale_tenue"] is False and "HYPOTHESE_SORTIE_MAXIMALE_TOMBEE" in err


def test_v2_hypothese_non_ecrite_si_rien_n_est_parti(pieces):
    amont = FauxAmont()
    code, ligne, err = jouer_complet(pieces, relais_devant(pieces, amont), plafond="1.00")   # pire cas > 1,00 : rien envoyé
    assert code == 4 and "hypothese_sortie_maximale_tenue" not in ligne and amont.recues == 0


def test_v2_argon_juge_aux_reglages_de_production(pieces):
    amont = FauxAmont(modele="gemini-4-argon")
    code, ligne = jouer_argon(pieces, relais_argon(pieces, amont))                  # plafond 1,00, juge
    assert code == 0 and ligne["pire_cas_usd"] <= 1.00 and ligne["prix"] == {"entree": 4.0, "sortie": 20.0}
'''
(racine / "tests/test_commande_gemini_flux_v2.py").write_text(t, encoding="utf-8")
print("commande v2 écrite")
