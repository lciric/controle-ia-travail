import sys
from pathlib import Path

racine = Path(sys.argv[1])
t = (racine / "tests/test_lancer_course_affinage_mentors_v6.py").read_text(encoding="utf-8")


def r(a, b, n=None):
    global t
    c = t.count(a)
    assert c >= 1 and (n is None or c == n), (c, a[:100])
    t = t.replace(a, b)


r('"""Essais du lanceur de la course d\'affinage des idées des mentors (v5 : constats de la contre-lecture de la v4, Carbon déclaré, sonde d\'Astra, confidentialité des textes servis)',
  '"""Essais du lanceur v8 de la course d\'affinage des idées des mentors : ceux du lanceur v6 (`tests/test_lancer_course_affinage_mentors_v6.py`,\ninchangés), repris et adaptés (clé LUC, Astra gpt-6.2-astra sur OPENAI_API_KEY_2, sonde v3, chemins v8), puis les essais propres à\nla v8 en fin de fichier (couverture de LUC au fil de l\'eau, exception de clé, garde des appels à Google, palier d\'Astra, mutations)')
r("lancer_course_affinage_mentors_v6", "lancer_course_affinage_mentors_v8")
r("RR_ANTHROPIC_API_KEY_MINUIT", "RR_ANTHROPIC_API_KEY_LUC")
r("2026-11-18T", "2026-11-22T")
r("AUJOURD_HUI = dt.date(2026, 11, 18)", "AUJOURD_HUI = dt.date(2026, 11, 22)", 1)
r("gpt-6-astra", "gpt-6.2-astra")
r("CLE_ESSAI_S", "OPENAI_API_KEY_2")
r("-alerte-credits-affinage-mentors-v6", "-alerte-credits-affinage-mentors-v8")
r("sonde_astra_affinage_v2", "sonde_astra_affinage_v3")
r("L.PREREG_SHA256", "PREREG_SHA")
# relevé : LUC au format v8 (solde lu à la console + recharge déclarée ; couverture 900 comme le reste de la v6)
r('''    base = {"RR_ANTHROPIC_API_KEY_LUC": {"credit_usd": 1000.0, "reste_usd": 900.0, "source": "essai"},''',
  '''    base = {"RR_ANTHROPIC_API_KEY_LUC": luc(),''', 1)
r('''def releve(**cles) -> dict:''', '''def luc(solde=860.0, recharge=40.0, **modifs) -> dict:
    """Ligne de la clé Claude au format v8 (GO-2026-11-22-111) : solde lu à la console + recharge déclarée."""
    o = {"solde_console_usd": solde, "recharge_declaree_usd": recharge, "source": "essai : console",
         "recharge_source": "essai : recharge automatique déclarée"}
    o.update(modifs)
    return o


def releve(**cles) -> dict:''', 1)
# registre : la ligne du GO de la course, plus l'exception de clé (GO-2026-11-22-107)
r('''            f"| {L.GO_ID} | 2026-11-18 | calcul | {perimetre} | {plafond} | 2026-11-30 | Lazar | R-3215 |\\n")''',
  '''            f"| {L.GO_ID} | 2026-11-18 | calcul | {perimetre} | {plafond} | 2026-11-30 | Lazar | R-3215 |\\n" + LIGNE_GO_CLE)


LIGNE_GO_CLE = ("| GO-2026-11-22-107 | 2026-11-22 | calcul | course d'affinage des idées des mentors : exception déclarée à la règle "
                "« Claude par l'abonnement » (GO-2026-11-22-70), clé RR_ANTHROPIC_API_KEY_LUC | sous le plafond d'arrêt de "
                "GO-2026-11-18-14 (150 USD) | 2026-11-25 | Lazar | GO-2026-11-18-14 |\\n")''', 1)
# préenregistrement d'essai (le v8 n'est pas encore écrit : PREREG_SHA256 du lanceur est vide)
r('''    prereg = depot / L.PREREG
    shutil.copy2(RACINE / L.PREREG, prereg)
    sceller(prereg)''', '''    prereg = depot / L.PREREG
    prereg.parent.mkdir(parents=True, exist_ok=True)
    prereg.write_text(PREREG_TEXTE, encoding="utf-8")
    sceller(prereg)''', 1)
r('''@pytest.fixture
def monde(tmp_path):''', '''PREREG_TEXTE = "# Préenregistrement d'ESSAI de la course d'affinage v8 (aucune valeur réelle)\\n"
PREREG_SHA = hashlib.sha256(PREREG_TEXTE.encode("utf-8")).hexdigest()


def _octets_de_main(rel: str) -> bytes | None:
    p = subprocess.run(["git", "-C", str(RACINE), "show", f"refs/remotes/origin/main:{rel}"], capture_output=True)
    return p.stdout if p.returncode == 0 else None


def octets_piece(rel: str) -> bytes:
    """Pièce du dépôt, ou de `origin/main` si elle n'est pas sur cette branche (garde Google)."""
    p = RACINE / rel
    return p.read_bytes() if p.is_file() else (_octets_de_main(rel) or b"")


def garde_google_factice(r, decl, pieces, fixe, liste):
    """Garde Google remplacée dans les essais de bout en bout : Argon réel ne passe pas la garde (voir les essais v8)."""
    return {"essai": "garde Google remplacée par un double conforme", **{n: {"conforme": True, "roles": []}
                                                                        for n in ("argon", "carbon") if n in decl["fournisseurs"]}}


@pytest.fixture
def monde(tmp_path):''', 1)
r('''    for rel, _ in L.PIECES.values():
        (depot / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(RACINE / rel, depot / rel)''', '''    for rel, _ in L.PIECES.values():
        (depot / rel).parent.mkdir(parents=True, exist_ok=True)
        (depot / rel).write_bytes(octets_piece(rel))''', 1)
r('''                   lire_etat_relais=lambda url: dict(etats_par_port[url.rsplit(":", 1)[1]]))''',
  '''                   lire_etat_relais=lambda url: dict(etats_par_port[url.rsplit(":", 1)[1]]),
                   controler_google=garde_google_factice, intervalle_surveillance_s=0.05)''', 1)
exec(open(str(Path(sys.argv[0]).resolve().parent / "remplacements_v8.py"), encoding="utf-8").read())
(racine / "tests/test_lancer_course_affinage_mentors_v8.py").write_text(t, encoding="utf-8")
print("écrit")
