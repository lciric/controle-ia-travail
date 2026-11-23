"""Construit scripts/lancer_course_affinage_mentors_v11.py à partir de la v10 (branche prep/affinage-v10, b0829025…), par
remplacements exacts comptés. Usage : python3 faire_lanceur_v11.py RACINE V10 SHA_CONF SHA_SONDE_V3 SHA_SONDE_COMMUNE_V2 SHA_COMMANDE_FLUX"""
import hashlib
import sys
from pathlib import Path

racine, v10 = Path(sys.argv[1]), Path(sys.argv[2])
SHA_CONF, SHA_SONDE, SHA_COMMUNE, SHA_FLUX = sys.argv[3:7]
src = v10.read_text(encoding="utf-8")
assert hashlib.sha256(src.encode("utf-8")).hexdigest() == "b08290254982744ba7985232ea54a354bfb31ef7f92ada682d32e349d3294577"


def r(a, b, n=1):
    global src
    c = src.count(a)
    assert c == n, (c, a[:140])
    src = src.replace(a, b)


ENTETE = '''#!/usr/bin/env python3
"""Lanceur de la course d'affinage des idées des mentors par l'organisme d'idéation — version 11 (clé Claude LUC et son
plafond propre, Astra gpt-6.2-astra, Carbon en flux sous la garde des appels à Google).

Version 11 (R12). Base : le lanceur **v10** de la branche `prep/affinage-v10-compte-organisme-v1` (`b0829025…`, contre-lu
« Scellable. », jamais joué ; les v7 à v10 vivent sur les branches `prep/affinage-v7…v10-compte-organisme-v1`, et les noms v8
de la branche du compte organisme sont pris : d'où le numéro 11, ordre de la mère du 22 novembre). Accords : GO-2026-11-22-107
(« go luc », exception déclarée à la règle « Claude par l'abonnement », GO-2026-11-22-70), GO-2026-11-22-110 (clé LUC
vérifiée), GO-2026-11-22-111 (recharge automatique au plus 40 euros ; Astra sur `OPENAI_API_KEY_2`), R-4995 (plafond propre
de LUC). Ce que la v11 change, et rien d'autre :
1. **clé Claude** : tous les appels Claude (deux proposeurs, aiguilleur, premier juge) passent par
   `RR_ANTHROPIC_API_KEY_LUC` ; `RR_ANTHROPIC_API_KEY_MINUIT` (sans crédit, R-4833) rejoint Rigaud parmi les clés exclues ;
   la ligne GO-2026-11-22-107 est lue au registre (`verifier_go_exception_cle`) ; configuration **v11** (copie de la v9 : clés,
   notes, plafond de LUC) ;
2. **couverture et plafond de la part Claude** (GO-2026-11-22-111, R-4995, brouillon 1 du préenregistrement v11) : relevé de LUC
   = solde lu à la console, recharge déclarée, réserves déclarées (sources écrites) ; la règle « Minuit compté au prix relevé »
   est retirée ; **plafond de la part Claude = min(45 USD ; 4/5 × (solde + recharge − réserves))**, arrondi au centime
   inférieur ; sous 20,65 USD (part Claude estimée) : alerte, pas de départ (**code 3**) ; le relais Claude doit être lancé à ce
   plafond exactement (le relevé précède son lancement) ; 45 USD est lu dans la configuration v11 et égal à la constante du
   lanceur (sinon refus : un plafond retiré ou relevé ne part pas) ;
3. **arrêt au fil de l'eau** : l'état du relais Claude est relu toutes les `intervalle_surveillance_s` secondes ; au **premier
   refus du relais** (statut 402, plafond atteint), à une part engagée (dépense + engagé) qui atteint le plafond, ou à un état
   illisible trois fois de suite : arrêt propre de l'orchestrateur par son PID, alerte scellée `alerte-arret-part-claude.json`,
   **code 5**, sans relance ; le plafond d'arrêt de 150 USD (orchestrateur) ne change pas ;
4. **Astra** : `gpt-6.2-astra`, prix 8 / 40 USD par million (R-4905), clé `OPENAI_API_KEY_2` exigée par son nom ; sonde v3 par
   la sonde commune v2 (rapports du jour sous `course-v11/`) ; modèle servi relu ; entrée la plus longue sous le palier de
   272 000 jetons ;
5. **Carbon en flux** : commande neuve `scripts/commande_gemini_flux_v1.py` (épinglée) par le relais Gemini v3 en flux de
   `main` (`relais_gemini_v3.py`, `2cf6bc6d…`, port 8791) ; niveau de réflexion « high », provision 28 672, sortie 65 536
   (limite en flux ; texte 36 864 ≥ 16 000 et > 2 cartes × 9 000 caractères), délai 1 500 + 60 s ; pire cas d'un appel sous le plafond de
   session (3,00 USD, configuration v9) écrit au manifeste ; relais : `--max-appels` ≥ 40, `--delai-silence-s` ≤ 240,
   `--delai-amont-s` ≥ délai de la commande, tous explicites ; les gardes de la commande par lot (lots, relevés) sont retirées ;
6. **garde des appels à Google** (règle gelée, GO-2026-11-21-71) : chaque commande Google déclarée (Argon, Carbon) est jouée
   hors ligne devant un faux amont local qui capture le corps de génération (rien ne part) ; le corps passe
   `garde_google_v3.verifier_reglages_google` (pièce de `main`, `923679b5…`) et la limite de l'invite d'un proposeur ; tout
   problème refuse le départ réel (écrit au manifeste en moteur simulé) ;
7. devis interne : Carbon à 0,997 USD par appel (même pensée et réponse que le devis v8, sans remise de lot) ;
8. noms propres à la version (chemins `course-v11/`, sorties, suffixe des runs ; une seule course de v1 à v11).
Codes : 0, 2, 3, 4, 6 comme la v10 ; **5** : arrêt par la garde de crédit d'un relais dispensé (v10) **ou** arrêt propre sur la
part Claude (premier 402 du relais Claude, plafond atteint, état illisible) — le fichier d'alerte dit lequel.
Argon : emplacement `argon_v11.plafond_session_juge_usd` de la configuration (vide : en attente du mot de la mère) ; rempli, il
remplace le plafond de session des juges dans la configuration servie (la garde Google juge ensuite le chemin d'Argon).

Texte de la v10 :

Lanceur de la course d'affinage des idées des mentors par l'organisme d'idéation — version 10.
'''
r('#!/usr/bin/env python3\n"""Lanceur de la course d\'affinage des idées des mentors par l\'organisme d\'idéation — version 10.\n', ENTETE)

r('import datetime as _dt\nimport hashlib\n', 'import datetime as _dt\nimport hashlib\nimport importlib.util\nimport shlex\nimport threading\nimport time\nfrom http.server import BaseHTTPRequestHandler, ThreadingHTTPServer\n')
r('VERSION = "lancer_course_affinage_mentors_v10"\nGO_ID = "GO-2026-11-18-14"\n',
  'VERSION = "lancer_course_affinage_mentors_v11"\nGO_ID = "GO-2026-11-18-14"\n'
  'GO_EXCEPTION_CLE = "GO-2026-11-22-107"  # exception déclarée à la règle « Claude par l\'abonnement »\n'
  'REGLE_ABONNEMENT = "GO-2026-11-22-70"\n'
  'GO_PRECISIONS_CLE = ("GO-2026-11-22-110", "GO-2026-11-22-111", "R-4995")  # cités au manifeste, non lus\n')
r('COURSE = "docs/notes/organisme-affinage-mentors-v1/course-v10"\n',
  'COURSE_V10 = "docs/notes/organisme-affinage-mentors-v1/course-v10"\nCOURSE = "docs/notes/organisme-affinage-mentors-v1/course-v11"\n')

# --- Carbon en flux : constantes ------------------------------------------------------------------------------------------
r('''MAX_SORTIE_CARBON = 32768                     # v9 : la sortie maximale compte la pensée (documentation du fournisseur)''',
  '''MAX_SORTIE_CARBON = 65536                     # v11 (flux) : limite en flux ; texte 36 864 au-delà de la provision 28 672''')
r('''DELAI_CARBON_S = 1620                         # délai de lot relevé (1 500 en v7), borné par l'orchestrateur épinglé''',
  '''DELAI_CARBON_S = 1500                         # v11 (flux) : délai de la génération ; + 60 s du compte de jetons, sous 1 800''')
r('''OPTIONS_CARBON_EXIGEES = ("--prix-entree", "--prix-sortie", "--facteur-lot", "--max-sortie-jetons", "--sortie-min-jetons",
                          "--provision-pensee-jetons", "--intervalle-s", "--delai-s", "--delai-requete-s")''',
  '''OPTIONS_CARBON_EXIGEES = ("--prix-entree", "--prix-sortie", "--max-sortie-jetons", "--provision-pensee-jetons", "--delai-s",
                          "--delai-requete-s")  # v11 : options numériques de la commande en flux
NIVEAU_REFLEXION_CARBON = "high"              # v11 : le plus haut admis pour Carbon (garde Google v3)
TEXTE_MIN_GOOGLE = 16000                      # règle gelée : réflexion + 16 000 jetons de texte au moins
CARACTERES_PAR_CARTE_MAX = 9000               # consigne du proposeur, point 6 (une carte, 9 000 caractères au plus)
DELAI_SILENCE_RELAIS_MAX_S = 240.0            # relais v3 : sous la coupure à 300 s des connexions muettes
PORT_CARBON = 8791                            # relais Gemini v3 en flux (procédure neutre, § 2.4)''')
r('''PORTS_DES_COURSES = (8787, 8788, 8789, 8790, 8791, 8792)''', '''PORTS_DES_COURSES = (8787, 8788, 8789, 8790, 8791, 8792)''')
r('''SONDE_ASTRA = f"{COURSE_V6}/sonde-astra-course-affinage-v6.json"
SONDES_ASTRA_V2 = (f"{COURSE}/sonde-astra-course-affinage-v10-{{jour}}.json",
                   f"{COURSE_V9}/sonde-astra-course-affinage-v9-{{jour}}.json",
                   f"{COURSE_V8}/sonde-astra-course-affinage-v8-{{jour}}.json",
                   f"{COURSE_V7}/sonde-astra-course-affinage-v7-{{jour}}.json", SONDE_ASTRA)
SONDES_ASTRA_COMMUNES = (f"{COURSE}/sonde-astra-commune-{{jour}}-v1.json",
                         f"{COURSE_V9}/sonde-astra-commune-{{jour}}-v1.json",
                         f"{COURSE_V8}/sonde-astra-commune-{{jour}}-v1.json",
                         f"{COURSE_V7}/sonde-astra-commune-{{jour}}-v1.json",
                         "docs/notes/organisme-auto-conception-v1/course-v2/sonde-astra-commune-{jour}-v1.json",
                         f"{COURSE_V6}/sonde-astra-commune-{{jour}}-v1.json")''',
  '''# v11 : sonde v3 (gpt-6.2-astra, 8 / 40) jouée par la sonde commune v2, rapports du jour sous `course-v11/` seulement (les
# rapports des versions précédentes sont d'un autre modèle).
SONDE_ASTRA = f"{COURSE}/sonde-astra-course-affinage-v11.json"
SONDES_ASTRA_V2 = (f"{COURSE}/sonde-astra-course-affinage-v11-{{jour}}.json", SONDE_ASTRA)
SONDES_ASTRA_COMMUNES = (f"{COURSE}/sonde-astra-commune-{{jour}}-v2.json",)
VERSION_SONDE_ASTRA = "sonde_astra_affinage_v3"
VERSION_SONDE_COMMUNE = "sonde_astra_courses_v2"''')
r('''                     "carbon": ("relais_gemini_v4.py", "543e728d90e809c661fdc26f1e1b1a32b2e23128a7d09e3b5d16f851408a35b4")}
MODELES_RELAIS = {"kimi": ["kimi-k3.1-pro"], "astra": ["gpt-6-astra"], "argon": ["gemini-4-argon"], "carbon": ["gemini-4-carbon"]}''',
  '''                     "carbon": ("relais_gemini_v3.py", "2cf6bc6df83f8847e75911c8cc0b6153c4467b36ce69273de649b5cbdc7e2378")}  # v11 : en flux
MODELES_RELAIS = {"kimi": ["kimi-k3.1-pro"], "astra": ["gpt-6.2-astra"], "argon": ["gemini-4-argon"], "carbon": ["gemini-4-carbon"]}
# Astra (R-4905) : USD par million, palier jusqu'à 272 000 jetons d'entrée (16 / 60 au-delà, jamais admis ici).
PRIX_ASTRA = (8.0, 40.0)
PALIER_ASTRA_JETONS = 272000
CLE_ASTRA = "OPENAI_API_KEY_2"  # GO-2026-11-22-111''')
r('''    "carbon": {"commande_gemini_lot_v1.py": "9484dce066514185dc1155d5c8dcff44b256fdf835b371b59ebdffa1d50bad75"}}''',
  f'''    "carbon": {{"commande_gemini_flux_v1.py": "{SHA_FLUX}"}}}}  # v11 : commande en flux (dépôt de travail)
GARDE_GOOGLE_PRODUCTION = "/home/user/controle-ia-travail/src/controle_ia/garde_google_v3.py"''')
r('''    "carbon": ["--modele", "gemini-4-carbon", "--url-base", "http://127.0.0.1:8792/v1beta", "--prix-entree", "8.3",
               "--prix-sortie", "41.5", "--facteur-lot", "0.5", "--max-sortie-jetons", str(MAX_SORTIE_CARBON),
               "--sortie-min-jetons", str(SORTIE_MIN_CARBON), "--provision-pensee-jetons", str(PROVISION_PENSEE_CARBON),
               "--intervalle-s", str(INTERVALLE_CARBON_S), "--delai-s", str(DELAI_CARBON_S),
               "--delai-requete-s", str(DELAI_REQUETE_CARBON_S), "--roles", "proposeur_ideation"],
    "astra": ["--url-relais", "http://127.0.0.1:8790", "--modele", "gpt-6-astra", "--prix-entree", "10", "--prix-sortie", "50",''',
  '''    "carbon": ["--espece", "carbon", "--modele", "gemini-4-carbon", "--url-base", f"http://127.0.0.1:{PORT_CARBON}/v1beta",
               "--prix-entree", "8.3", "--prix-sortie", "41.5", "--niveau-reflexion", NIVEAU_REFLEXION_CARBON,
               "--provision-pensee-jetons", str(PROVISION_PENSEE_CARBON), "--max-sortie-jetons", str(MAX_SORTIE_CARBON),
               "--delai-s", str(DELAI_CARBON_S), "--delai-requete-s", str(DELAI_REQUETE_CARBON_S), "--roles", "proposeur_ideation",
               "--garde", GARDE_GOOGLE_PRODUCTION],
    "astra": ["--url-relais", "http://127.0.0.1:8790", "--modele", "gpt-6.2-astra", "--prix-entree", "8", "--prix-sortie", "40",''')
r('''SORTIES_COURSES = tuple(Path(f"/home/user/sorties-course-affinage-mentors-v{k}") for k in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))''',
  '''SORTIES_COURSES = tuple(Path(f"/home/user/sorties-course-affinage-mentors-v{k}") for k in range(1, 12))''')
r('''CLE_CLAUDE = "RR_ANTHROPIC_API_KEY_MINUIT"
CLES_INTERDITES = ("RR_ANTHROPIC_API_KEY_RIGAUD",)
PREFIXE_CLES_CLAUDE = "RR_ANTHROPIC_API_KEY"
CREDIT_DECLARE_CLE_CLAUDE_USD = 200.0  # R-3228, mot de Lazar
''', '''CLE_CLAUDE = "RR_ANTHROPIC_API_KEY_LUC"  # GO-2026-11-22-107
CLES_INTERDITES = ("RR_ANTHROPIC_API_KEY_RIGAUD", "RR_ANTHROPIC_API_KEY_MINUIT")  # Minuit : sans crédit (R-4833)
PREFIXE_CLES_CLAUDE = "RR_ANTHROPIC_API_KEY"
# v11 : part Claude estimée du devis v10 (deux proposeurs, aiguilleur, premier juge ; marge comprise ; table du § 4) ; la
# couverture de LUC (solde + recharge déclarés) doit la dépasser avant le départ ; puis compte au fil de l'eau.
PART_CLAUDE_ESTIMEE_USD = 20.65
PART_CLAUDE_HAUT_USD = 74.62
PLAFOND_PART_CLAUDE_USD = 45.0   # R-4995 : plafond propre de LUC ; égal à celui de la configuration v11, sinon refus
PART_DE_LA_COUVERTURE = 0.8      # brouillon 1 du préenregistrement v11 : quatre cinquièmes de la couverture nette
RESERVE_APPEL_CLAUDE_USD = 0.40  # réserve par appel par défaut du relais Claude (procédure neutre, § 2.1)
INTERVALLE_SURVEILLANCE_S = 10.0
LECTURES_ILLISIBLES_MAX = 3
''')
r('''PREREG = f"{COURSE}/preenregistrement-course-affinage-mentors-v10.md"
PREREG_SHA256 = "7fc71712136cf20d86f3603eb581bc61dd6bc35fcfe0650b230cf659674a3856"
CONTRE_LECTURE = f"{COURSE}/contre-lecture-preenregistrement-course-affinage-mentors-v10.md"
DECLARATION_RELAIS = f"{COURSE}/declaration-relais-course-affinage-mentors-v10.json"
RELEVE_CREDITS = f"{COURSE}/releve-credits-avant-course-affinage-mentors-v10.json"''',
  '''PREREG = f"{COURSE}/preenregistrement-course-affinage-mentors-v11.md"
PREREG_SHA256 = ""  # à poser quand le préenregistrement v11 sera écrit et scellé : d'ici là, aucun lancement (refus nommé)
CONTRE_LECTURE = f"{COURSE}/contre-lecture-preenregistrement-course-affinage-mentors-v11.md"
DECLARATION_RELAIS = f"{COURSE}/declaration-relais-course-affinage-mentors-v11.json"
RELEVE_CREDITS = f"{COURSE}/releve-credits-avant-course-affinage-mentors-v11.json"''')
r('''RELEVE_PRIX = f"{COURSE}/releve-prix-claude-course-affinage-v10.json"''', '''RELEVE_PRIX = f"{COURSE}/releve-prix-claude-course-affinage-v11.json"''')
r('''    "configuration": (f"{COURSE_V9}/configuration-course-affinage-mentors-v9.json", "e7378f89ae39eacd169ff912526a8e998e4f01f0aba235eeaa0bf12e4b195d5d"),  # v9 : proposeur 3,00
    "sonde_astra": ("scripts/sonde_astra_affinage_v2.py", "1799449269e15661b92f2a45eaab95a22e3a766a1fdf10ec9a4648bbe92aebf7"),
    "sonde_commune": ("scripts/sonde_astra_courses_v1.py", "d374d1071f4ef70b3604d97dc62e2f14103c440a166342b330d7a576d8b4c777"),''',
  f'''    "configuration": (f"{{COURSE}}/configuration-course-affinage-mentors-v11.json", "{SHA_CONF}"),  # v9 + LUC + plafond de LUC
    "sonde_astra": ("scripts/sonde_astra_affinage_v3.py", "{SHA_SONDE}"),
    "sonde_commune": ("scripts/sonde_astra_courses_v2.py", "{SHA_COMMUNE}"),
    "commande_carbon": ("scripts/commande_gemini_flux_v1.py", "{SHA_FLUX}"),
    # garde commune des appels à Google (règle gelée, GO-2026-11-21-71), pièce de `main` : présente dans le dépôt de travail
    "garde_google": ("src/controle_ia/garde_google_v3.py", "923679b51cfc84b65ff7cfc65296378d08e6d4e64f6b427823d23ba24f4afe91"),''')
r('''                      "prop-carbon": 0.4985, "aiguilleur": 0.031, "juge-opus": 0.037, "juge-argon": 0.0347}''',
  '''                      "prop-carbon": 0.997, "aiguilleur": 0.031, "juge-opus": 0.037, "juge-argon": 0.0347}
# v11 : Carbon en flux, sans remise de lot : 2 618 × 8,3 + (20 000 + 3 500) × 41,5, par million = 0,996979, arrondi 0,997 ;
# pire cas d'un appel : 2 618 × 8,3 + 65 536 × 41,5, par million = 2,741473 USD (sous 3,00).''')
r('''DEVIS_V5_TOTAL = {"cinq_especes": 41.136, "six_especes": 48.8384}''',
  '''DEVIS_V5_TOTAL = {"cinq_especes": 49.112, "six_especes": 56.8144}  # v11 : + 16 × (0,997 − 0,4985) = + 7,976''')
r('''DOSSIER_SORTIES = Path("/home/user/sorties-course-affinage-mentors-v10")
SUFFIXE_RUN = "-course-affinage-mentors-v10"
SUFFIXES_DEJA_LANCEE = tuple(f"-course-affinage-mentors-v{k}" for k in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))''',
  '''DOSSIER_SORTIES = Path("/home/user/sorties-course-affinage-mentors-v11")
SUFFIXE_RUN = "-course-affinage-mentors-v11"
SUFFIXES_DEJA_LANCEE = tuple(f"-course-affinage-mentors-v{k}" for k in range(1, 12))''')

# --- réglages --------------------------------------------------------------------------------------------------------------
r('''    references_kimi_admises: tuple = REFERENCES_KIMI_ADMISES
''', '''    references_kimi_admises: tuple = REFERENCES_KIMI_ADMISES
    controler_google: object = None          # v11 : None = la garde réelle (commandes jouées hors ligne devant un faux amont)
    intervalle_surveillance_s: float = INTERVALLE_SURVEILLANCE_S
''')

# --- GO de l'exception de clé ------------------------------------------------------------------------------------------------
r('''def verifier_course_jamais_lancee(r: Reglages) -> None:''', '''def verifier_go_exception_cle(registre: Path, aujourd_hui: _dt.date, go_id: str = GO_EXCEPTION_CLE) -> dict:
    """v11 : la ligne de l'exception déclarée (GO-2026-11-22-107) : une seule ligne, type « calcul », accordée par Lazar, en
    période, non révoquée, dont le périmètre nomme la clé Claude de la course, la règle « Claude par l'abonnement »
    (GO-2026-11-22-70) et la course (« mentors » ou « affinage ») ; son plafond, en mots, renvoie au GO de la course."""
    if not registre.is_file():
        raise Refus(f"registre des GO absent : {registre}")
    ligne_go = re.compile(r"^\\|\\s*(GO-\\d{4}-\\d{2}-\\d{2}-\\d{2,3})\\s*\\|")
    trouvees, revocations = [], []
    for ligne in registre.read_text(encoding="utf-8").splitlines():
        m = ligne_go.match(ligne)
        if not m:
            continue
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if m.group(1) == go_id:
            trouvees.append(cellules)
        elif _est_revocation(cellules, go_id):
            revocations.append(m.group(1))
    if len(trouvees) != 1 or len(trouvees[0]) != 8:
        raise Refus(f"{go_id} : {len(trouvees)} ligne(s) dans {registre.name} (une ligne de 8 colonnes exigée) — exception de clé "
                    f"non trouvée : aucun appel Claude par l'interface")
    ident, accorde, typ, perimetre, plafond, echeance, par, _ref = trouvees[0]
    if typ != "calcul" or par != "Lazar":
        raise Refus(f"{go_id} : type {typ!r} accordé par {par!r} (« calcul », Lazar exigés)")
    try:
        d_acc, d_ech = _dt.date.fromisoformat(accorde), _dt.date.fromisoformat(echeance)
    except ValueError:
        raise Refus(f"{go_id} : dates illisibles ({accorde!r}, {echeance!r})") from None
    if not d_acc <= aujourd_hui <= d_ech:
        raise Refus(f"{go_id} hors de sa période de validité ({d_acc} → {d_ech}, aujourd'hui {aujourd_hui})")
    if revocations:
        raise Refus(f"{go_id} révoqué par {', '.join(sorted(revocations))}")
    p = _normaliser(perimetre)
    if CLE_CLAUDE not in perimetre or REGLE_ABONNEMENT not in perimetre or not ("mentors" in p or "affinage" in p):
        raise Refus(f"{go_id} : le périmètre doit nommer {CLE_CLAUDE}, la règle {REGLE_ABONNEMENT} et la course d'affinage")
    if GO_ID not in plafond:
        raise Refus(f"{go_id} : le plafond doit renvoyer au plafond d'arrêt de {GO_ID}")
    return {"id": ident, "accorde": accorde, "echeance": echeance, "par": par, "regle_exceptee": REGLE_ABONNEMENT,
            "precisions_citees": list(GO_PRECISIONS_CLE),
            "ligne_sha256": hashlib.sha256(("|".join(trouvees[0])).encode("utf-8")).hexdigest()}


def verifier_plafond_luc(fixe: dict) -> float:
    """v11 (R-4995) : plafond propre de LUC lu dans la configuration et égal à la constante du lanceur ; ni retiré, ni relevé,
    au plus le plafond d'arrêt de la course."""
    lu = ((fixe.get("changements_v11") or {}).get("plafond_part_claude_usd"))
    if not _nombre(lu) or float(lu) != PLAFOND_PART_CLAUDE_USD or not 0 < PLAFOND_PART_CLAUDE_USD <= PLAFOND_ARRET_USD:
        raise Refus(f"plafond propre de {CLE_CLAUDE} : configuration {lu!r}, lanceur {PLAFOND_PART_CLAUDE_USD!r} ; 45 USD exigés "
                    "aux deux (R-4995) : un plafond retiré ou relevé ne part pas")
    return float(lu)


def verifier_course_jamais_lancee(r: Reglages) -> None:''')

# --- déclaration -------------------------------------------------------------------------------------------------------------
r('''            raise Refus(f"fournisseurs.{nom}.nom_cle = {nom_cle} : clé exclue de cette course (R-3228, elle garde son reste)")
        if nom == "claude" and nom_cle != CLE_CLAUDE:
            raise Refus(f"fournisseurs.claude.nom_cle = {nom_cle} : tous les appels Claude passent par {CLE_CLAUDE} (R-3228)")''',
  '''            raise Refus(f"fournisseurs.{nom}.nom_cle = {nom_cle} : clé exclue de cette course (Rigaud garde son reste ; Minuit "
                        f"est sans crédit, R-4833)")
        if nom == "claude" and nom_cle != CLE_CLAUDE:
            raise Refus(f"fournisseurs.claude.nom_cle = {nom_cle} : tous les appels Claude passent par {CLE_CLAUDE} ({GO_EXCEPTION_CLE})")
        if nom == "astra" and nom_cle != CLE_ASTRA:
            raise Refus(f"fournisseurs.astra.nom_cle = {nom_cle} : Astra passe par {CLE_ASTRA} (GO-2026-11-22-111)")''')
r('''            if nom == "carbon":  # v8 : options exigées lues d'abord (motif précis), puis l'égalité aux arguments épinglés
                controler_delai_carbon(lire_reglages_carbon(c[4:]), fixe)''',
  '''            if nom == "carbon":  # v8 : options exigées lues d'abord (motif précis), puis l'égalité aux arguments épinglés
                controler_delai_carbon(lire_reglages_carbon(c[4:]), fixe)
                if _valeur_arg(c[4:], "--niveau-reflexion") != NIVEAU_REFLEXION_CARBON:  # v11 : réflexion explicite, la plus haute
                    raise Refus(f"fournisseurs.carbon.commande : --niveau-reflexion {_valeur_arg(c[4:], '--niveau-reflexion')!r}, "
                                f"{NIVEAU_REFLEXION_CARBON!r} exigé (règle des appels à Google)")''')

# --- Carbon : délai et pire cas en flux ------------------------------------------------------------------------------------
r('''        raise Refus(f"fournisseurs.carbon.commande : options {manquantes} absentes (v8 : provision de pensée, sortie, délais "
                    "exigés explicitement ; le défaut de la commande — 8 192 jetons de pensée, 1 500 s — est refusé)")''',
  '''        raise Refus(f"fournisseurs.carbon.commande : options {manquantes} absentes (provision de pensée, sortie, délais exigés "
                    "explicitement)")''')
r('''    duree_max = lues["--delai-s"] + lues["--intervalle-s"] + 2 * lues["--delai-requete-s"]''',
  '''    duree_max = lues["--delai-s"] + lues["--delai-requete-s"]  # v11 (flux) : compte de jetons, puis une génération''')
r('''        raise Refus(f"fournisseurs.carbon.commande : --delai-s {lues['--delai-s']:g} < {DELAI_CARBON_S} (v8 : délai de lot relevé ; "
                    "un lot a dépassé 1 500 s dans la course d'auto-conception v4)")''',
  '''        raise Refus(f"fournisseurs.carbon.commande : --delai-s {lues['--delai-s']:g} < {DELAI_CARBON_S} (v11 : délai de la "
                    "génération en flux)")''')
ANCIEN_PIRE = src[src.index("def controler_pire_cas_carbon("):src.index("def parts_au_pire(")]
NOUVEAU_PIRE = '''def controler_pire_cas_carbon(decl: dict, fixe: dict, liste: dict, pieces: dict) -> dict | None:
    """v11 (flux, `commande_gemini_flux_v1.py`) : la commande ne baisse jamais sa sortie ; elle refuse (code 4) si l'entrée
    gardée × prix d'entrée + sortie maximale × prix de sortie dépasse le plafond de session. Sur l'entrée **la plus longue** de
    la course (consigne servie et fil expurgé, caractères / 3 × 1,05) et l'entrée la plus courte : pire cas d'un appel ≤ plafond
    de session (sinon Carbon serait absente de fait) ; texte = sortie − provision ≥ 16 000 (règle gelée) et > cartes × 9 000
    caractères (limite de l'invite, un jeton au plus par caractère) ; sortie ≥ pensée et réponse observées (24 500). Rend None si
    Carbon n'est pas active."""
    if "carbon" not in decl["fournisseurs"]:
        return None
    c = decl["fournisseurs"]["carbon"]["commande"]
    lues = lire_reglages_carbon(c[4:])
    delai = controler_delai_carbon(lues, fixe)
    plafond = float(fixe["plafonds_session"]["proposeur"])
    consigne = Path(pieces["consigne_proposeur"]["absolu"]).read_text(encoding="utf-8")
    caracteres = [len(consigne_servie_proposeur(consigne, expurger(texte_de_case(f))[0])) for f in liste["fils"]]
    pe, ps = lues["--prix-entree"] / 1e6, lues["--prix-sortie"] / 1e6
    p, smax = lues["--provision-pensee-jetons"], lues["--max-sortie-jetons"]
    texte = smax - p
    limite_invite = int(fixe.get("cartes_par_appel") or 1) * CARACTERES_PAR_CARTE_MAX
    if texte < TEXTE_MIN_GOOGLE or texte <= limite_invite:
        raise Refus(f"fournisseurs.carbon.commande : texte {texte:g} jetons (sortie {smax:g} − provision {p:g}) : au moins "
                    f"{TEXTE_MIN_GOOGLE} et plus que la limite de l'invite ({limite_invite} caractères) exigés (règle des appels à Google)")
    if smax < SORTIE_RETENUE_MIN_CARBON:
        raise Refus(f"fournisseurs.carbon.commande : sortie {smax:g} < {SORTIE_RETENUE_MIN_CARBON} (pensée et réponse observées)")
    sortie = {}
    for nom_cas, n in (("entree_la_plus_longue", max(caracteres)), ("entree_la_plus_courte", min(caracteres))):
        e = math.ceil(n / CARACTERES_PAR_JETON_CARBON * (1 + MARGE_ENTREE_CARBON))
        pire = e * pe + smax * ps
        if pire > plafond + 1e-12:
            raise Refus(f"fournisseurs.carbon.commande : pire cas d'un appel {pire:.6f} USD (entrée gardée {e}, sortie {smax:g}) > "
                        f"plafond de session {plafond} USD : la commande refuserait chaque appel (code 4, rien envoyé)")
        sortie[nom_cas] = {"caracteres": n, "entree_gardee_jetons": e, "sortie_demandee_jetons": int(smax),
                           "pire_cas_appel_usd": round(pire, 6), "marge_sous_le_plafond_usd": round(plafond - pire, 6)}
    return {"reglages": {k: lues[k] for k in OPTIONS_CARBON_EXIGEES}, "niveau_reflexion": NIVEAU_REFLEXION_CARBON,
            "texte_jetons": texte, "limite_invite_caracteres": limite_invite, "plafond_session_usd": plafond, "delai": delai,
            "cas": sortie, "part_au_pire_usd": round(len(liste["fils"]) * plafond, 6),
            "note": "flux, prix plein, aucune remise ; la sortie maximale compte la pensée ; une sortie coupée (MAX_TOKENS) ou "
                    "sans pensée est un défaut de la commande (garde Google après réponse), jamais une réponse"}


'''
src = src.replace(ANCIEN_PIRE, NOUVEAU_PIRE)

# --- relais vivant de Carbon (v3 en flux) --------------------------------------------------------------------------------
r('''        out["max_appels"] = egal_a_l_etat["max_appels"] = max_appels
        if nom == "carbon":
            max_lots = _entier_arg(args, "--max-lots", nom)
            if max_lots < MIN_LOTS_CARBON:
                raise Refus(f"relais carbon : --max-lots {max_lots} < {MIN_LOTS_CARBON} (16 propositions + marge de "
                            f"{MARGE_APPELS_PROPOSEUR})")
            out["max_lots"] = egal_a_l_etat["max_lots"] = max_lots''',
  '''        out["max_appels"] = egal_a_l_etat["max_appels"] = max_appels
        if nom == "carbon":  # v11 : relais Gemini v3 en flux ; délais explicites (aucun défaut supposé)
            for option in ("--delai-silence-s", "--delai-amont-s"):
                if _valeur_arg(args, option) is None:
                    raise Refus(f"relais carbon : {option} absent des arguments lus par PID (explicite exigé)")
            try:
                silence, amont = float(_valeur_arg(args, "--delai-silence-s")), float(_valeur_arg(args, "--delai-amont-s"))
            except ValueError:
                raise Refus("relais carbon : --delai-silence-s ou --delai-amont-s illisible") from None
            if not 0 < silence <= DELAI_SILENCE_RELAIS_MAX_S:
                raise Refus(f"relais carbon : --delai-silence-s {silence:g} hors de ]0, {DELAI_SILENCE_RELAIS_MAX_S:g}] (coupure à 300 s)")
            if amont < DELAI_CARBON_S:
                raise Refus(f"relais carbon : --delai-amont-s {amont:g} < délai de la commande {DELAI_CARBON_S} (relais ≥ commande)")
            if "--sans-pensees-amont" in args:
                raise Refus("relais carbon : --sans-pensees-amont refusé (les pensées doivent être demandées à l'amont)")
            out["delai_silence_s"], out["delai_amont_s"] = silence, amont''')
r('''    champs = ("appels",) + (("depense_usd", "engage_usd") if nom in RELAIS_A_DOLLARS else ()) \\
        + (("lots_crees", "releves") if nom == "carbon" else ())  # v8 : « releves » nul exigé aussi pour Carbon''',
  '''    champs = ("appels",) + (("depense_usd", "engage_usd") if nom in RELAIS_A_DOLLARS else ())  # v11 : plus de lots pour Carbon''')
r('''    if nom == "carbon":  # v8 : délai de lot relevé, donc plus de relevés par lot ; le relais les borne à part (--max-releves)
        restants = etat.get("releves_restants")
        if not _nombre(restants) or restants < MIN_RELEVES_CARBON:
            raise Refus(f"relais carbon : releves_restants {restants!r} < {MIN_RELEVES_CARBON} (20 lots × (⌈{DELAI_CARBON_S} / "
                        f"{INTERVALLE_CARBON_S}⌉ + 2)) : les derniers lots ne seraient plus relevés (429) — v8")
        out["releves_restants"] = restants
''', '')

# --- crédits : LUC -----------------------------------------------------------------------------------------------------------
r('''    - Non lisible : Minuit compté au prix relevé (v2) ; Argon, Astra, Carbon seulement sous la dispense écrite de la mère''',
  '''    - v11 : clé Claude (LUC) : `solde_console_usd` et `recharge_declaree_usd` (nombres ≥ 0, sources écrites) exigés ;
      couverture = leur somme ; alerte (code 3) si elle ne dépasse pas la part Claude estimée ; la part au pire (150) n'y est
      plus confrontée (compte au fil de l'eau pendant la course, `SurveillanceCleClaude`) ; « non lisible » refusé.
    - Non lisible : Argon, Astra, Carbon seulement sous la dispense écrite de la mère''')
r('''        if nom == CLE_CLAUDE and isinstance(x, dict) and x.get("non_lisible") is True:
            anterieure = x.get("depense_anterieure_usd")
            if not _reel_positif(anterieure):
                raise Refus(f"crédit de {nom} non lisible : depense_anterieure_usd (≥ 0) exigée pour le compter au prix relevé")
            x = {"credit_usd": CREDIT_DECLARE_CLE_CLAUDE_USD, "reste_usd": max(0.0, CREDIT_DECLARE_CLE_CLAUDE_USD - anterieure),
                 "source": "compté au prix relevé : crédit déclaré 200 USD (R-3228) moins la dépense antérieure déclarée"}
        if not isinstance(x, dict):''', '''        if nom == CLE_CLAUDE:
            if not isinstance(x, dict):
                raise Refus(f"relevé des crédits : clé {nom} (Claude) absente — solde lu à la console et recharge déclarée exigés")
            solde, recharge, reserves = x.get("solde_console_usd"), x.get("recharge_declaree_usd"), x.get("reserves_declarees_usd")
            sources = (x.get("source"), x.get("recharge_source"))
            if x.get("non_lisible") is True or not (_reel_positif(solde) and _reel_positif(recharge) and _reel_positif(reserves)) \\
                    or not all(isinstance(s, str) and s.strip() for s in sources):
                raise Refus(f"relevé des crédits : clé {nom} : solde_console_usd, recharge_declaree_usd, reserves_declarees_usd "
                            "(nombres ≥ 0) et les sources (source, recharge_source) exigés (GO-2026-11-22-111) ; « non lisible » "
                            "n'est pas admis")
            couverture = round(float(solde) + float(recharge) - float(reserves), 6)
            plafond_part = math.floor(min(PLAFOND_PART_CLAUDE_USD, PART_DE_LA_COUVERTURE * couverture) * 100 + 1e-9) / 100
            d = {"fournisseur": fournisseur, "relais": fours, "parts_par_relais": dict(zip(fours, parts_k)), "lisible": True,
                 "solde_console_usd": solde, "recharge_declaree_usd": recharge, "reserves_declarees_usd": reserves,
                 "couverture_usd": couverture, "plafond_part_claude_usd": plafond_part,
                 "credit_usd": couverture, "reste_usd": couverture, "source": sources[0], "recharge_source": sources[1],
                 "part_au_pire_usd": part, "part_claude_estimee_usd": PART_CLAUDE_ESTIMEE_USD,
                 "plafond_propre_usd": PLAFOND_PART_CLAUDE_USD,
                 "regle": "plafond de la part Claude = min(45 ; 4/5 × (solde + recharge − réserves)) ; relais Claude lancé à ce "
                          "plafond ; arrêt propre au premier 402 du relais (code 5)"}
            motifs = []
            if plafond_part < PART_CLAUDE_ESTIMEE_USD:
                motifs.append(f"plafond de la part Claude {plafond_part} (min(45 ; 4/5 × ({solde} + {recharge} − {reserves}))) < part "
                              f"Claude estimée {PART_CLAUDE_ESTIMEE_USD} : pas de départ")
            d["motifs_d_arret"] = motifs
            sortie[nom] = d
            if motifs:
                alertes.append({"cle": nom, "fournisseur": fournisseur, "couverture_usd": couverture, "part_au_pire_usd": part,
                                "motifs": motifs})
            continue
        if not isinstance(x, dict):''')

# --- sonde d'Astra -----------------------------------------------------------------------------------------------------------
r('''    if c.get("version") != "sonde_astra_courses_v1":''', '''    if c.get("version") != VERSION_SONDE_COMMUNE:''')
r('''                    "(un seul exigé, R-3273) ; un autre jour : sonde neuve, rapports sous course-v10/")''',
  '''                    "(un seul exigé, R-3273) ; un autre jour : sonde neuve, rapports sous course-v11/")''')
r('''    if o.get("version") != "sonde_astra_affinage_v2":
        raise Refus("sonde d'Astra : fichier non écrit par la sonde épinglée (scripts/sonde_astra_affinage_v2.py)")''',
  '''    if o.get("version") != VERSION_SONDE_ASTRA:
        raise Refus("sonde d'Astra : fichier non écrit par la sonde épinglée (scripts/sonde_astra_affinage_v3.py)")
    servi = o.get("modele_servi")
    attendu = MODELES_RELAIS["astra"][0]
    if not (isinstance(servi, str) and re.fullmatch(re.escape(attendu) + r"(-\\d{4}-?\\d{2}-?\\d{2})?", servi)):
        raise Refus(f"sonde d'Astra : modèle servi {servi!r}, {attendu} exigé")''')

# --- confidentialité, configuration ------------------------------------------------------------------------------------------
r('re.compile(r"\\b(Lazar|Ciric|lciric|Rigaud|Minuit|Heimersheim', 're.compile(r"\\b(Lazar|Ciric|lciric|Rigaud|Minuit|Luc|Heimersheim')
r('''                                                       "risques_v6")}''', '''                                                       "risques_v6", "changements_v11")}''')
r('''    """v2 : la configuration fixe nomme Minuit pour Claude, exclut Rigaud, et chaque espèce Claude porte Minuit."""
    if (fixe.get("cles") or {}).get("claude") != CLE_CLAUDE:
        raise Refus(f"configuration : cles.claude doit être {CLE_CLAUDE}")
    if any(c not in (fixe.get("cles_interdites") or []) for c in CLES_INTERDITES):
        raise Refus("configuration : la clé Rigaud doit figurer dans cles_interdites")''',
  '''    """v11 : la configuration fixe nomme LUC pour Claude, exclut Rigaud et Minuit, et chaque espèce Claude porte LUC."""
    if (fixe.get("cles") or {}).get("claude") != CLE_CLAUDE:
        raise Refus(f"configuration : cles.claude doit être {CLE_CLAUDE}")
    if any(c not in (fixe.get("cles_interdites") or []) for c in CLES_INTERDITES):
        raise Refus(f"configuration : les clés {list(CLES_INTERDITES)} doivent figurer dans cles_interdites")''')

NEUF = (Path(sys.argv[0]).resolve().parent / "neuf_v11.py").read_text(encoding="utf-8")
r('''

# --- (6) orchestrateur --------------------------------------------------------------------------------------------------------
''', NEUF)

# --- exécution -----------------------------------------------------------------------------------------------------------------
r('''        raise Refus(f"variable {CLE_CLAUDE} absente ou vide dans l'environnement du lanceur : arrêt au départ (R-3228)")
    commit_registre = verifier_registre_main(r) if (reel and r.verifier_go) else None
    go = verifier_go(r.registre_go, aujourd_hui) if (reel and r.verifier_go) else {"go": "sans objet (moteur simulé, aucune dépense)"}''',
  '''        raise Refus(f"variable {CLE_CLAUDE} absente ou vide dans l'environnement du lanceur : arrêt au départ ({GO_EXCEPTION_CLE})")
    commit_registre = verifier_registre_main(r) if (reel and r.verifier_go) else None
    go = verifier_go(r.registre_go, aujourd_hui) if (reel and r.verifier_go) else {"go": "sans objet (moteur simulé, aucune dépense)"}
    go_cle = verifier_go_exception_cle(r.registre_go, aujourd_hui) if (reel and r.verifier_go) else {"go": "sans objet (moteur simulé)"}''')
r('''    decl = verifier_declaration(decl_brute, fixe, r)
    releve_brut, releve_sha = lire_json_scelle(r.releve, "relevé des crédits")''',
  '''    decl = verifier_declaration(decl_brute, fixe, r)
    plafond_luc = verifier_plafond_luc(fixe)
    google = (r.controler_google or controler_chemins_google)(r, decl, pieces, fixe, liste)
    non_conformes = {n: [p for x in v["roles"] for p in x["problemes"]] for n, v in google.items()
                     if isinstance(v, dict) and v.get("conforme") is False}
    if non_conformes:
        if reel:
            raise Refus("garde des appels à Google (règle gelée, GO-2026-11-21-71) : " + json.dumps(non_conformes, ensure_ascii=False)
                        + " — retirer l'espèce de la déclaration (motif dans « absences ») ou lui donner un chemin conforme")
        print(json.dumps({"avertissement_garde_google": non_conformes, "moteur": "simulé : refus en moteur réel"},
                         ensure_ascii=False), file=sys.stderr)
        google["refus_en_moteur_reel"] = sorted(non_conformes)
    palier_astra = verifier_palier_astra(pieces, liste) if "astra" in decl["fournisseurs"] else {"astra": "non déclarée"}
    releve_brut, releve_sha = lire_json_scelle(r.releve, "relevé des crédits")''')
r('''r.dossier_runs / (ident.replace(SUFFIXE_RUN, "") + "-alerte-credits-affinage-mentors-v10"), parts)''',
  '''r.dossier_runs / (ident.replace(SUFFIXE_RUN, "") + "-alerte-credits-affinage-mentors-v11"), parts)''')
r('''        "carbon": decl["carbon"], "cles_employees": decl["cles"],''',
  '''        "carbon": decl["carbon"], "cles_employees": decl["cles"], "go_exception_cle": go_cle, "garde_google": google,
        "palier_astra": palier_astra,''')
r('''        "cle_claude": {"nom": CLE_CLAUDE, "presente_dans_l_environnement_du_lanceur": cle_presente, "valeur": "jamais lue",
                       "cles_exclues": list(CLES_INTERDITES)},''',
  '''        "cle_claude": {"nom": CLE_CLAUDE, "presente_dans_l_environnement_du_lanceur": cle_presente, "valeur": "jamais lue",
                       "cles_exclues": list(CLES_INTERDITES), "exception": GO_EXCEPTION_CLE,
                       "couverture_usd": (credits.get(CLE_CLAUDE) or {}).get("couverture_usd"), "plafond_propre_usd": plafond_luc,
                       "part_estimee_usd": PART_CLAUDE_ESTIMEE_USD, "part_haut_usd": PART_CLAUDE_HAUT_USD,
                       "surveillance": ("au fil de l'eau, toutes les " + str(r.intervalle_surveillance_s) + " s") if reel else "moteur simulé : aucune"},''')
r('''        "reglages_carbon_v8": reglages_carbon if reglages_carbon is not None else {"carbon": "non active"},''',
  '''        "reglages_carbon_v11_flux": reglages_carbon if reglages_carbon is not None else {"carbon": "non active"},''')
r('''                            "6": "course partie : orchestrateur à code non nul ou erreur du lanceur après le départ"},''',
  '''                            "6": "course partie : orchestrateur à code non nul ou erreur du lanceur après le départ",
                            "7": "arrêt propre : couverture de LUC (solde + recharge déclarés) atteinte ou non comptable",
                            "8": "arrêt propre : plafond propre de LUC (45 USD, R-4995) atteint, sans relance"},''')
r('''    code, pid, echec, arret_credit = None, None, None, []
    debut = _dt.datetime.now(_dt.timezone.utc)''',
  '''    code, pid, echec, arret_credit = None, None, None, []
    surveillance, arret_luc = None, None
    if reel:
        couverture = (credits.get(CLE_CLAUDE) or {}).get("couverture_usd")
        if not _nombre(couverture):
            raise Refus(f"couverture de {CLE_CLAUDE} inconnue : la part Claude ne peut pas être comptée au fil de l'eau")
        surveillance = SurveillanceCleClaude(r, decl["fournisseurs"]["claude"]["url_relais"], float(couverture), plafond_luc)
    debut = _dt.datetime.now(_dt.timezone.utc)''')
r('''            try:
                while True:
                    try:
                        code = enfant.wait(timeout=1.0)
                        break
                    except subprocess.TimeoutExpired:''',
  '''            try:
                prochaine = 0.0
                while True:
                    if surveillance is not None and arret_luc is None and time.monotonic() >= prochaine:
                        prochaine = time.monotonic() + float(r.intervalle_surveillance_s)
                        arret_luc = surveillance.depasse()
                        if arret_luc:  # R-4995 et GO-2026-11-22-111 : arrêt propre par PID (R10), message écrit, jamais muet
                            print(json.dumps({"arret_cle_claude": arret_luc, "pid": enfant.pid}, ensure_ascii=False),
                                  file=sys.stderr, flush=True)
                            try:
                                enfant.send_signal(signal.SIGTERM)
                            except ProcessLookupError:
                                pass
                    try:
                        code = enfant.wait(timeout=min(1.0, float(r.intervalle_surveillance_s)))
                        break
                    except subprocess.TimeoutExpired:''')
r('''                                               for x in sorted(dossier_arrets.glob("soupcon-credit-*.json"))]}''',
  '''                                               for x in sorted(dossier_arrets.glob("soupcon-credit-*.json"))],
             "cle_claude_au_fil_de_l_eau": dict(surveillance.bilan(), arret=arret_luc) if surveillance else {"moteur": "simulé"}}''')
r('''    if alertes_apres or depasse:''', '''    if arret_luc:
        ecrire_scelle(dossier_run / "alerte-cle-claude.json",
                      {"alerte": f"course arrêtée proprement sur la clé {CLE_CLAUDE} : " +
                                 ("plafond propre de 45 USD atteint (R-4995), sans relance" if arret_luc["code"] == 8 else
                                  "couverture déclarée atteinte ou non comptable (GO-2026-11-22-111)"),
                       "code": arret_luc["code"], "motif": arret_luc["motif"], "bilan": surveillance.bilan(),
                       "relance": "aucune (une relance est une nouvelle version et un mot de la mère)",
                       "pour": "la mère, qui prévient Lazar"})
    if alertes_apres or depasse:''')
r('''    sortie_lanceur = code_de_sortie(depasse, bool(bilan.get("arret_au_premier_refus_pour_credit")), echec, code)''',
  '''    sortie_lanceur = code_de_sortie(depasse, bool(bilan.get("arret_au_premier_refus_pour_credit")), echec, code,
                                    arret_luc["code"] if arret_luc else None)''')
r('''def code_de_sortie(depasse: bool, arret_credit: bool, echec, code_orchestrateur) -> int:''',
  '''def code_de_sortie(depasse: bool, arret_credit: bool, echec, code_orchestrateur, arret_luc: int | None = None) -> int:''')
r('''    if depasse:
        return 4
    if arret_credit:
        return 5
    if echec or code_orchestrateur != 0:''', '''    if depasse:
        return 4
    if arret_luc in (7, 8):  # v11 : arrêt propre sur la clé Claude (8 : plafond propre de LUC ; 7 : couverture)
        return arret_luc
    if arret_credit:
        return 5
    if echec or code_orchestrateur != 0:''')

# --- essai à blanc -------------------------------------------------------------------------------------------------------------
r('''CHEMINS_MAIN_COMMANDES = {
    "carbon": "docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_gemini_lot_v1.py",
    "astra": "docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py"}''',
  '''CHEMINS_MAIN_COMMANDES = {
    "astra": "docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py"}  # v11 : Carbon par la commande du dépôt''')
r('''    cmd = {n: extraire_de_main(r.depot, CHEMINS_MAIN_COMMANDES[n], next(iter(COMMANDES_EPINGLEES[n].values())),
                               essai / os.path.basename(CHEMINS_MAIN_COMMANDES[n])) for n in ("carbon", "astra")}''',
  '''    cmd = {n: extraire_de_main(r.depot, CHEMINS_MAIN_COMMANDES[n], next(iter(COMMANDES_EPINGLEES[n].values())),
                               essai / os.path.basename(CHEMINS_MAIN_COMMANDES[n])) for n in ("astra",)}
    cmd["carbon"] = r.depot / PIECES["commande_carbon"][0]''')
r('''                  "modele_propose": "gpt-6-astra", "nom_cle": "CLE_FACTICE_ASTRA", "porte_plafond": {"type": "environnement"}},''',
  '''                  "modele_propose": "gpt-6.2-astra", "nom_cle": CLE_ASTRA, "porte_plafond": {"type": "environnement"}},''')
r('''              "cles": dict({n: {"non_lisible": True, "motif": "essai à blanc : solde illisible, sous dispense"}
                            for n in ("CLE_FACTICE_ARGON", "CLE_FACTICE_ASTRA")},
                           **{CLE_CLAUDE: {"non_lisible": True, "motif": "essai à blanc : compté au prix relevé",
                                           "depense_anterieure_usd": 0.0}}),
              "dispense": {"par": "mère", "reference": REFERENCE_DISPENSE,
                           "cles": ["CLE_FACTICE_ARGON", "CLE_FACTICE_ASTRA"]}}''',
  '''              "cles": dict({n: {"non_lisible": True, "motif": "essai à blanc : solde illisible, sous dispense"}
                            for n in ("CLE_FACTICE_ARGON", CLE_ASTRA)},
                           **{CLE_CLAUDE: {"solde_console_usd": 0.0, "source": "essai à blanc : aucune lecture réelle",
                                           "recharge_declaree_usd": 100.0, "recharge_source": "essai à blanc : valeur factice"}}),
              "dispense": {"par": "mère", "reference": REFERENCE_DISPENSE,
                           "cles": ["CLE_FACTICE_ARGON", CLE_ASTRA]}}''')
r('''    r.moteur, r.exiger_bac_a_sable, r.verifier_go = "simule", False, False
    return r''', '''    r.moteur, r.exiger_bac_a_sable, r.verifier_go = "simule", False, False
    r.ref_registre = None
    return r''')

exec((Path(sys.argv[0]).resolve().parent / "post_v11.py").read_text(encoding="utf-8"))
exec((Path(sys.argv[0]).resolve().parent / "post2_v11.py").read_text(encoding="utf-8"))
exec((Path(sys.argv[0]).resolve().parent / "post3_v11.py").read_text(encoding="utf-8"))
exec((Path(sys.argv[0]).resolve().parent / "post4_v11.py").read_text(encoding="utf-8"))
exec((Path(sys.argv[0]).resolve().parent / "post5_v11.py").read_text(encoding="utf-8"))
exec((Path(sys.argv[0]).resolve().parent / "post6_v11.py").read_text(encoding="utf-8"))
(racine / "scripts/lancer_course_affinage_mentors_v11.py").write_text(src, encoding="utf-8")
print("écrit", len(src.splitlines()), "lignes")
print([l.strip()[:120] for l in src.split('"""\nfrom __future__', 1)[1].splitlines() if "gpt-6-astra" in l or "MINUIT" in l or "lot_v1" in l])
