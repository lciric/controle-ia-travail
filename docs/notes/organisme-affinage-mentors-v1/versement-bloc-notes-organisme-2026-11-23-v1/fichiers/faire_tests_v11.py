"""Construit tests/test_lancer_course_affinage_mentors_v11.py à partir des essais v10 (prep/affinage-v10, 4e651669…)."""
import hashlib
import re
import sys
from pathlib import Path

racine, t10 = Path(sys.argv[1]), Path(sys.argv[2])
ICI = Path(sys.argv[0]).resolve().parent
t = t10.read_text(encoding="utf-8")
assert hashlib.sha256(t.encode("utf-8")).hexdigest() == "4e6516695fb086363fdc5fb46c8b609d15f8ea4b728431c841e532e91dc3b992"


def r(a, b, n=None):
    global t
    c = t.count(a)
    assert c >= 1 and (n is None or c == n), (c, a[:100])
    t = t.replace(a, b)


r('"""Essais du lanceur v10 de la course d\'affinage des idées des mentors',
  '"""Essais du lanceur v11 de la course d\'affinage des idées des mentors : ceux de la v10 (branche prep/affinage-v10, '
  '`tests/test_lancer_course_affinage_mentors_v10.py`, `4e651669…`) portés par transformation (clé LUC, Astra gpt-6.2-astra sur '
  'OPENAI_API_KEY_2, sonde v3 et sonde commune v2 sous course-v11/, Carbon en flux par le relais Gemini v3 au port 8791, '
  'préenregistrement d\'essai, garde Google remplacée par un double conforme dans les essais de bout en bout) ; les essais propres '
  'à la commande par lot et ceux qui relisent des pièces des branches prep (lanceurs v7 à v9, commandes et gabarits v10) sont '
  'retirés (liste au rapport du développeur v11) ; les essais propres à la v11 sont en fin de fichier.\n\nTexte des essais v10 : '
  'Essais du lanceur v10 de la course d\'affinage des idées des mentors', 1)
r("lancer_course_affinage_mentors_v10", "lancer_course_affinage_mentors_v11")
r("RR_ANTHROPIC_API_KEY_MINUIT", "RR_ANTHROPIC_API_KEY_LUC")
r("gpt-6-astra", "gpt-6.2-astra")
r("CLE_ESSAI_S", "OPENAI_API_KEY_2")
r("-alerte-credits-affinage-mentors-v10", "-alerte-credits-affinage-mentors-v11")
r('"prix_entree_usd_par_million": 10.0, "prix_sortie_usd_par_million": 50.0', '"prix_entree_usd_par_million": 8.0, "prix_sortie_usd_par_million": 40.0')
r("sonde_astra_affinage_v2", "sonde_astra_affinage_v3")
r('"version": "sonde_astra_courses_v1"', '"version": "sonde_astra_courses_v2"')
r('COMMUNE_DU_JOUR = "docs/notes/organisme-auto-conception-v1/course-v2/sonde-astra-commune-2026-11-18-v1.json"',
  'COMMUNE_DU_JOUR = "docs/notes/organisme-affinage-mentors-v1/course-v11/sonde-astra-commune-2026-11-18-v2.json"', 1)
r("commande_gemini_lot_v1", "commande_gemini_flux_v1")
r("L.PREREG_SHA256", "PREREG_SHA")
# relais de Carbon : Gemini v3 en flux, port 8791
r('(progs / "relais_gemini_v4.py").write_text("# relais factice gemini v4\\n", encoding="utf-8")',
  '(progs / "relais_gemini_v3.py").write_text("# relais factice gemini v3 en flux\\n", encoding="utf-8")', 1)
r('''                    "8792": {"appels": 0, "variable_cle_encore_presente": False, "modeles": ["gemini-4-carbon"], "max_appels": 40,
                             "max_lots": 20, "lots_crees": 0, "releves": 0, "releves_restants": 2000},''',
  '''                    "8791": {"appels": 0, "variable_cle_encore_presente": False, "modeles": ["gemini-4-carbon"], "max_appels": 40},''', 1)
r('''                PID_CARBON: [sys.executable, "-I", "-B", str(progs / "relais_gemini_v4.py"), "--variable-cle", "CLE_ESSAI_G",
                             "--port", "8792", "--max-appels", "40", "--max-lots", "20", "--modele", "gemini-4-carbon"]}''',
  '''                PID_CARBON: [sys.executable, "-I", "-B", str(progs / "relais_gemini_v3.py"), "--variable-cle", "CLE_ESSAI_G",
                             "--port", "8791", "--max-appels", "40", "--delai-silence-s", "240", "--delai-amont-s", "1800",
                             "--modele", "gemini-4-carbon"]}''', 1)
r('''"carbon": ("relais_gemini_v4.py", hashlib.sha256((progs / "relais_gemini_v4.py").read_bytes()).hexdigest())},''',
  '''"carbon": ("relais_gemini_v3.py", hashlib.sha256((progs / "relais_gemini_v3.py").read_bytes()).hexdigest())},''', 1)
r('monde["etats"]["8792"]', 'monde["etats"]["8791"]')
# relevé : LUC au format v11
r('''    base = {"RR_ANTHROPIC_API_KEY_LUC": {"credit_usd": 1000.0, "reste_usd": 900.0, "source": "essai"},''',
  '''    base = {"RR_ANTHROPIC_API_KEY_LUC": luc(),''', 1)
r('''def releve(**cles) -> dict:''', '''def luc(solde=860.0, recharge=40.0, **modifs) -> dict:
    """Ligne de la clé Claude au format v11 (GO-2026-11-22-111) : solde lu à la console + recharge déclarée."""
    o = {"solde_console_usd": solde, "recharge_declaree_usd": recharge, "source": "essai : console",
         "recharge_source": "essai : recharge automatique déclarée"}
    o.update(modifs)
    return o


def releve(**cles) -> dict:''', 1)
r('''            f"| {L.GO_ID} | 2026-11-18 | calcul | {perimetre} | {plafond} | 2026-11-30 | Lazar | R-3215 |\\n")''',
  '''            f"| {L.GO_ID} | 2026-11-18 | calcul | {perimetre} | {plafond} | 2026-11-30 | Lazar | R-3215 |\\n" + LIGNE_GO_CLE)


LIGNE_GO_CLE = ("| GO-2026-11-22-107 | 2026-11-18 | calcul | course d'affinage des idées des mentors : exception déclarée à la règle "
                "« Claude par l'abonnement » (GO-2026-11-22-70), clé RR_ANTHROPIC_API_KEY_LUC | sous le plafond d'arrêt de "
                "GO-2026-11-18-14 (150 USD) | 2026-11-25 | Lazar | GO-2026-11-18-14 |\\n")  # accordée « le 18 » : date du monde d'essai''', 1)
# préenregistrement d'essai ; pièces de main ; garde Google remplacée ; surveillance rapide
r('''    prereg = depot / L.PREREG
    prereg.parent.mkdir(parents=True, exist_ok=True)  # v7 : course-v7/ ne porte aucune pièce épinglée
    shutil.copy2(RACINE / L.PREREG, prereg)
    sceller(prereg)''', '''    prereg = depot / L.PREREG
    prereg.parent.mkdir(parents=True, exist_ok=True)
    prereg.write_text(PREREG_TEXTE, encoding="utf-8")
    sceller(prereg)''', 1)
r('''    for rel, _ in L.PIECES.values():
        (depot / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(RACINE / rel, depot / rel)''', '''    for rel, _ in L.PIECES.values():
        (depot / rel).parent.mkdir(parents=True, exist_ok=True)
        (depot / rel).write_bytes(octets_piece(rel))''', 1)
r('''@pytest.fixture
def monde(tmp_path):''', '''PREREG_TEXTE = "# Préenregistrement d'ESSAI de la course d'affinage v11 (aucune valeur réelle)\\n"
PREREG_SHA = hashlib.sha256(PREREG_TEXTE.encode("utf-8")).hexdigest()


def _octets_de_main(rel: str) -> bytes | None:
    p = subprocess.run(["git", "-C", str(RACINE), "show", f"refs/remotes/origin/main:{rel}"], capture_output=True)
    return p.stdout if p.returncode == 0 else None


def octets_piece(rel: str) -> bytes:
    """Pièce du dépôt, ou de `origin/main` si elle n'est pas sur cette branche (garde Google)."""
    p = RACINE / rel
    return p.read_bytes() if p.is_file() else (_octets_de_main(rel) or b"")


def garde_google_factice(r, decl, pieces, fixe, liste):
    """Garde Google remplacée dans les essais de bout en bout : l'Argon réel ne passe pas la garde (voir les essais v11)."""
    return {"essai": "garde Google remplacée par un double conforme", **{n: {"conforme": True, "roles": []}
                                                                        for n in ("argon", "carbon") if n in decl["fournisseurs"]}}


@pytest.fixture
def monde(tmp_path):''', 1)
r('''                   lire_etat_relais=lambda url: dict(etats_par_port[url.rsplit(":", 1)[1]]))''',
  '''                   lire_etat_relais=lambda url: dict(etats_par_port[url.rsplit(":", 1)[1]]),
                   controler_google=garde_google_factice, intervalle_surveillance_s=0.05)''', 1)
r("sorties_courses=tuple(tmp_path / f\"sorties-anciennes-v{k}\" for k in (1, 2, 3, 4, 5, 6, 7)),",
  "sorties_courses=tuple(tmp_path / f\"sorties-anciennes-v{k}\" for k in range(1, 12)),", 1)

# --- retrait des essais propres au lot ou qui relisent des pièces des branches prep -----------------------------------------------
RETIRES = (ICI / "retires_v11.txt").read_text(encoding="utf-8").split()
retires_faits = []
for nom in RETIRES:
    m = re.search(r"^(@pytest\.mark\.parametrize\([^\n]*(?:\n(?![@d])[^\n]*)*\n)?def " + re.escape(nom) + r"\(.*?(?=^(?:@|def |# ---|[A-Z_]+ = |_spec|class )|\Z)",
                  t, re.S | re.M)
    if m:
        t = t[:m.start()] + t[m.end():]
        retires_faits.append(nom)
exec((ICI / "remplacements_v11.py").read_text(encoding="utf-8"))
t += (ICI / "tests_propres_v11.py").read_text(encoding="utf-8")
(racine / "tests/test_lancer_course_affinage_mentors_v11.py").write_text(t, encoding="utf-8")
print("écrit ;", len(retires_faits), "essais retirés :", " ".join(retires_faits))
print("non trouvés :", sorted(set(RETIRES) - set(retires_faits)))
