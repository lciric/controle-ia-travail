"""Construit scripts/lancer_course_affinage_mentors_v8.py à partir de la v6 (inchangée), par remplacements exacts comptés."""
import sys
from pathlib import Path

racine = Path(sys.argv[1])
SHA_CONF, SHA_SONDE = sys.argv[2], sys.argv[3]
src = (racine / "scripts/lancer_course_affinage_mentors_v6.py").read_text(encoding="utf-8")


def r(a, b, n=1):
    global src
    c = src.count(a)
    assert c == n, (c, a[:120])
    src = src.replace(a, b)


ENTETE = '''#!/usr/bin/env python3
"""Lanceur de la course d'affinage des idées des mentors par l'organisme d'idéation — version 8 (clé Claude LUC, Astra
gpt-6.2-astra, garde des appels à Google).

Version 8 (R12 ; v1 à v6 restent en place sur cette branche, inchangées). Dérivée de la v6 (`scripts/lancer_course_affinage_
mentors_v6.py`, `bf2abdc6…`) sur l'ordre de la mère et l'accord de Lazar GO-2026-11-22-107 (« go luc »), avec les précisions
GO-2026-11-22-110 (clé LUC vérifiée, solde non lisible par l'interface) et GO-2026-11-22-111 (recharge automatique active, au
plus 40 euros). **Attention, nom** : des lanceurs `lancer_course_affinage_mentors_v7.py` à `_v10.py` existent sur les branches
`prep/affinage-v7…v10-compte-organisme-v1` (lignée du 18 novembre, jamais versée ici) ; ce fichier-ci n'en descend pas (voir le
rapport du développeur, `course-v8/rapport-developpeur-lanceur-v8.md`). Ce que la v8 change, et rien d'autre :
1. **clé Claude** : tous les appels Claude (deux proposeurs, aiguilleur, premier juge) passent par
   `RR_ANTHROPIC_API_KEY_LUC` ; `RR_ANTHROPIC_API_KEY_MINUIT` (sans crédit, R-4833) rejoint Rigaud parmi les clés exclues ; la
   ligne GO-2026-11-22-107 est lue au registre (exception déclarée à la règle « Claude par l'abonnement », GO-2026-11-22-70 :
   type calcul, accordée par Lazar, en période, non révoquée, qui nomme la clé LUC et la règle) ; configuration **v8** (copie
   de la v6, clés et notes seulement) ;
2. **couverture de la clé LUC** (GO-2026-11-22-111, consigne de la mère) : le relevé porte le solde lu à la console
   (`solde_console_usd`, avec sa source) et la recharge déclarée (`recharge_declaree_usd`, avec sa source) ; couverture = somme
   des deux ; la règle « Minuit compté au prix relevé » (200 USD déclarés) est retirée ; avant le départ, alerte et arrêt (code 3)
   si la couverture ne dépasse pas la part Claude estimée du devis (`PART_CLAUDE_ESTIMEE_USD`) ; **pendant la course**, la part
   Claude engagée (`depense_usd` + `engage_usd` du relais Claude, lus par `/relais/etat`) est relue toutes les
   `intervalle_surveillance_s` secondes : si elle atteint la couverture moins la réserve d'un appel, ou si l'état est illisible
   trois fois de suite, arrêt propre de l'orchestrateur par son PID (SIGTERM), alerte écrite et scellée, **code 6** ; le
   plafond d'arrêt de 150 USD (GO-2026-11-18-14) et la part au pire de la clé Claude (150 USD) ne changent pas, mais la part au
   pire n'est plus confrontée au reste de LUC (remplacée par ce compte au fil de l'eau) ;
3. **Astra** : modèle `gpt-6.2-astra`, prix 8 / 40 USD par million (R-4905 ; palier jusqu'à 272 000 jetons d'entrée), clé
   `OPENAI_API_KEY_2` exigée par son nom ; garde neuve : l'entrée la plus longue servie (octets, plus le préambule du kit et
   la marge de la commande) reste sous le palier ; sonde **v3** (`scripts/sonde_astra_affinage_v3.py`, jouée par la sonde
   commune v2 `scripts/sonde_astra_courses_v2.py`), rapport du jour sous `course-v8/`, modèle servi relu ;
4. **garde des appels à Google** (règle gelée de `CLAUDE.md`, GO-2026-11-21-71) : pour **chaque** commande Google déclarée
   (Argon et Carbon), la commande épinglée est jouée **hors ligne**, devant un faux amont local qui compte les jetons puis
   capture le corps de génération et répond 503 (rien ne part chez Google) ; le corps capturé passe
   `garde_google_v3.verifier_reglages_google` (pièce épinglée de `main`, `923679b5…`), et, pour un proposeur, la limite de
   l'invite (deux cartes de 9 000 caractères au plus, un jeton au plus par caractère) doit tenir dans le plafond de texte ; tout
   problème : **refus avant le départ** en moteur réel (rien de silencieux), écrit au manifeste en moteur simulé. Le relais en
   flux de la passe X n'a pas été repris (ce n'est pas un relais : l'exécutant de la passe appelle Google lui-même, clé en
   main) : Carbon garde la commande par lot de la v6, que la garde refuse en l'état (voir le rapport) ;
5. devis interne : composition déclarée v6b (deux Claude, Argon, Astra, Carbon) 41,33 USD estimés, 103,38 haut (marge
   comprise) ; sans Carbon 32,86 et 84,81 ;
6. noms propres à la version : chemins `course-v8/`, sorties, suffixe des runs, une seule course de v1 à v10.
Codes : 0, 2, 3, 4, 5 comme la v6 ; **6** arrêt propre pour couverture de la clé Claude atteinte ou illisible.

Texte de la v6 :

Lanceur de la course d'affinage des idées des mentors par l'organisme d'idéation — version 6.
'''
r('#!/usr/bin/env python3\n"""Lanceur de la course d\'affinage des idées des mentors par l\'organisme d\'idéation — version 6.\n', ENTETE)

# --- constantes ----------------------------------------------------------------------------------------------------------
r('import datetime as _dt\nimport hashlib\n', 'import datetime as _dt\nimport hashlib\nimport importlib.util\nimport math\nimport shlex\nimport threading\nimport time\nfrom http.server import BaseHTTPRequestHandler, ThreadingHTTPServer\n')
r('VERSION = "lancer_course_affinage_mentors_v6"\nGO_ID = "GO-2026-11-18-14"\n',
  'VERSION = "lancer_course_affinage_mentors_v8"\nGO_ID = "GO-2026-11-18-14"\n'
  'GO_EXCEPTION_CLE = "GO-2026-11-22-107"  # exception déclarée à la règle « Claude par l\'abonnement »\n'
  'REGLE_ABONNEMENT = "GO-2026-11-22-70"\n'
  'GO_PRECISIONS_CLE = ("GO-2026-11-22-110", "GO-2026-11-22-111")  # clé vérifiée ; recharge automatique (cités, non lus)\n')
r('COURSE = "docs/notes/organisme-affinage-mentors-v1/course-v6"\n', 'COURSE = "docs/notes/organisme-affinage-mentors-v1/course-v8"\n')
r('RELEVE_PRIX = f"{COURSE}/releve-prix-claude-course-affinage-v6.json"\nSONDE_ASTRA = f"{COURSE}/sonde-astra-course-affinage-v6.json"\n',
  'RELEVE_PRIX = f"{COURSE}/releve-prix-claude-course-affinage-v8.json"\nSONDE_ASTRA = f"{COURSE}/sonde-astra-course-affinage-v8.json"\n'
  'VERSION_SONDE_ASTRA = "sonde_astra_affinage_v3"\n')
r('MODELES_RELAIS = {"kimi": ["kimi-k3.1-pro"], "astra": ["gpt-6-astra"], "argon": ["gemini-4-argon"], "carbon": ["gemini-4-carbon"]}',
  'MODELES_RELAIS = {"kimi": ["kimi-k3.1-pro"], "astra": ["gpt-6.2-astra"], "argon": ["gemini-4-argon"], "carbon": ["gemini-4-carbon"]}\n'
  '# Astra (R-4905) : USD par million, palier jusqu\'à 272 000 jetons d\'entrée (16 / 60 au-delà, jamais admis ici).\n'
  'PRIX_ASTRA = (8.0, 40.0)\nPALIER_ASTRA_JETONS = 272000\n'
  'PREAMBULE_KIT_OCTETS = 60000  # préambule du kit d\'agent : ≈ 15 000 jetons au plus (devis v6, § 2), à 4 octets par jeton\n'
  'CLE_ASTRA = "OPENAI_API_KEY_2"  # GO-2026-11-22-111 et lots d\'Astra 6.2 du compte organisme')
r('''    "astra": ["--url-relais", "http://127.0.0.1:8790", "--modele", "gpt-6-astra", "--prix-entree", "10", "--prix-sortie", "50",''',
  '''    "astra": ["--url-relais", "http://127.0.0.1:8790", "--modele", "gpt-6.2-astra", "--prix-entree", "8", "--prix-sortie", "40",''')
r('SORTIES_COURSES = tuple(Path(f"/home/user/sorties-course-affinage-mentors-v{k}") for k in (1, 2, 3, 4, 5, 6))',
  'SORTIES_COURSES = tuple(Path(f"/home/user/sorties-course-affinage-mentors-v{k}") for k in range(1, 11))  # v7 à v10 : branches prep')
r('''CLE_CLAUDE = "RR_ANTHROPIC_API_KEY_MINUIT"
CLES_INTERDITES = ("RR_ANTHROPIC_API_KEY_RIGAUD",)
PREFIXE_CLES_CLAUDE = "RR_ANTHROPIC_API_KEY"
CREDIT_DECLARE_CLE_CLAUDE_USD = 200.0  # R-3228, mot de Lazar
''', '''CLE_CLAUDE = "RR_ANTHROPIC_API_KEY_LUC"  # GO-2026-11-22-107
CLES_INTERDITES = ("RR_ANTHROPIC_API_KEY_RIGAUD", "RR_ANTHROPIC_API_KEY_MINUIT")  # Minuit : sans crédit (R-4833)
PREFIXE_CLES_CLAUDE = "RR_ANTHROPIC_API_KEY"
# Couverture de LUC (GO-2026-11-22-111) : part Claude estimée du devis v6b (deux proposeurs, aiguilleur, premier juge, marge
# comprise : 20,65 USD) ; la couverture doit la dépasser avant le départ, puis la part engagée est comptée au fil de l'eau.
PART_CLAUDE_ESTIMEE_USD = 20.65
RESERVE_APPEL_CLAUDE_USD = 0.40  # réserve par appel par défaut du relais Claude (procédure neutre, § 2.1) : arrêt avant
INTERVALLE_SURVEILLANCE_S = 10.0
LECTURES_ILLISIBLES_MAX = 3
''')
r('''PREREG = f"{COURSE}/preenregistrement-course-affinage-mentors-v6.md"
PREREG_SHA256 = "58ccfa5c997d62d252554a86735a0afec88e17587abb2aed55f7e44dcbb116ad"
CONTRE_LECTURE = f"{COURSE}/contre-lecture-preenregistrement-course-affinage-mentors-v6.md"
DECLARATION_RELAIS = f"{COURSE}/declaration-relais-course-affinage-mentors-v6.json"
RELEVE_CREDITS = f"{COURSE}/releve-credits-avant-course-affinage-mentors-v6.json"
''', '''PREREG = f"{COURSE}/preenregistrement-course-affinage-mentors-v8.md"
PREREG_SHA256 = ""  # à poser quand le préenregistrement v8 sera écrit et scellé : d'ici là, aucun lancement (refus nommé)
CONTRE_LECTURE = f"{COURSE}/contre-lecture-preenregistrement-course-affinage-mentors-v8.md"
DECLARATION_RELAIS = f"{COURSE}/declaration-relais-course-affinage-mentors-v8.json"
RELEVE_CREDITS = f"{COURSE}/releve-credits-avant-course-affinage-mentors-v8.json"
''')
r('''    "configuration": (f"{COURSE}/configuration-course-affinage-mentors-v6.json", "0ea89ed2f72ce2693e619eb10b6eecbd46725d4578b548a44c5a98b9bb1ded21"),
    "sonde_astra": ("scripts/sonde_astra_affinage_v2.py", "1799449269e15661b92f2a45eaab95a22e3a766a1fdf10ec9a4648bbe92aebf7"),''',
  f'''    "configuration": (f"{{COURSE}}/configuration-course-affinage-mentors-v8.json", "{SHA_CONF}"),
    "sonde_astra": ("scripts/sonde_astra_affinage_v3.py", "{SHA_SONDE}"),
    # garde commune des appels à Google (règle gelée, GO-2026-11-21-71), pièce de `main` : présente dans le dépôt de travail
    "garde_google": ("src/controle_ia/garde_google_v3.py", "923679b51cfc84b65ff7cfc65296378d08e6d4e64f6b427823d23ba24f4afe91"),''')
r('''# Devis v6 (`devis-course-affinage-mentors-v6.md`, mêmes prix par appel que la v3 et la v5 ; noms des constantes gardés), estimation par appel, USD : sert à l'écart au devis (garde 5).
DEVIS_V5_PAR_APPEL = {"prop-opus": 0.141, "prop-fable": 0.3525, "prop-argon": 0.276, "prop-kimi": 0.276, "prop-astra": 0.276,
                      "prop-carbon": 0.276, "aiguilleur": 0.031, "juge-opus": 0.037, "juge-argon": 0.0347}
DEVIS_V5_TOTAL = {"sans_carbon": 37.576, "avec_carbon": 45.2784}
''', '''# Devis : prix par appel du devis v6 (mêmes que la v3 et la v5 ; noms des constantes gardés), estimation par appel, USD : sert
# à l'écart au devis (garde 5). v8 : composition déclarée de la v6b (deux Claude, Argon, Astra, Carbon ; pas Kimi) :
# sous-total 37,576, estimation marge comprise 41,33, haut 103,38 ; sans Carbon (quatre espèces) : 29,8736, 32,86, 84,81.
# La ligne d'Astra (0,276 ; pire appel 0,400484) est la ligne commune « proposeur hors Claude » du devis v6, mesurée sur Argon
# et Kimi et SUPPOSÉE pour Astra : elle n'est pas tirée d'un prix d'Astra et ne change donc pas avec lui (rapport du
# développeur, § Astra : le calcul au prix de gpt-6.2-astra sur les hypothèses de jetons du devis y est donné, à trancher).
DEVIS_V5_PAR_APPEL = {"prop-opus": 0.141, "prop-fable": 0.3525, "prop-argon": 0.276, "prop-kimi": 0.276, "prop-astra": 0.276,
                      "prop-carbon": 0.276, "aiguilleur": 0.031, "juge-opus": 0.037, "juge-argon": 0.0347}
DEVIS_V5_TOTAL = {"sans_carbon": 29.8736, "avec_carbon": 37.576}
DEVIS_V8_MARGE_COMPRISE = {"sans_carbon": {"estimation": 32.86, "haut": 84.81}, "avec_carbon": {"estimation": 41.33, "haut": 103.38}}
''')
r('DOSSIER_SORTIES = Path("/home/user/sorties-course-affinage-mentors-v6")\nSUFFIXE_RUN = "-course-affinage-mentors-v6"\nSUFFIXES_DEJA_LANCEE = tuple(f"-course-affinage-mentors-v{k}" for k in (1, 2, 3, 4, 5, 6))  # une seule course, quelle que soit la version',
  'DOSSIER_SORTIES = Path("/home/user/sorties-course-affinage-mentors-v8")\nSUFFIXE_RUN = "-course-affinage-mentors-v8"\nSUFFIXES_DEJA_LANCEE = tuple(f"-course-affinage-mentors-v{k}" for k in range(1, 11))  # une seule course, quelle que soit la version (v7 à v10 : branches prep)')

# --- réglages : surveillance et garde Google injectables ------------------------------------------------------------------
r('''    ref_registre: str | None = "origin/main"
    verifier_go: bool = True
''', '''    ref_registre: str | None = "origin/main"
    verifier_go: bool = True
    controler_google: object = None          # v8 : None = la garde réelle (commandes jouées hors ligne devant un faux amont)
    intervalle_surveillance_s: float = INTERVALLE_SURVEILLANCE_S
''')

# --- GO de l'exception de clé ----------------------------------------------------------------------------------------------
r('''def verifier_course_jamais_lancee(r: Reglages) -> None:''', '''def verifier_go_exception_cle(registre: Path, aujourd_hui: _dt.date, go_id: str = GO_EXCEPTION_CLE) -> dict:
    """v8 : la ligne de l'exception déclarée (GO-2026-11-22-107) : une ligne principale, type « calcul », accordée par Lazar, en
    période, non révoquée, dont le périmètre nomme la clé Claude de la course, la règle « Claude par l'abonnement »
    (GO-2026-11-22-70) et la course (« mentors » ou « affinage »). Son plafond est en mots (« sous le plafond d'arrêt de
    GO-2026-11-18-14 ») : il doit citer ce GO ; aucun nombre n'en est lu."""
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


def verifier_course_jamais_lancee(r: Reglages) -> None:''')

# --- déclaration ---------------------------------------------------------------------------------------------------------
r('''            raise Refus(f"fournisseurs.{nom}.nom_cle = {nom_cle} : clé exclue de cette course (R-3228, elle garde son reste)")
        if nom == "claude" and nom_cle != CLE_CLAUDE:
            raise Refus(f"fournisseurs.claude.nom_cle = {nom_cle} : tous les appels Claude passent par {CLE_CLAUDE} (R-3228)")''',
  '''            raise Refus(f"fournisseurs.{nom}.nom_cle = {nom_cle} : clé exclue de cette course (Rigaud garde son reste ; Minuit "
                        f"est sans crédit, R-4833)")
        if nom == "claude" and nom_cle != CLE_CLAUDE:
            raise Refus(f"fournisseurs.claude.nom_cle = {nom_cle} : tous les appels Claude passent par {CLE_CLAUDE} ({GO_EXCEPTION_CLE})")
        if nom == "astra" and nom_cle != CLE_ASTRA:
            raise Refus(f"fournisseurs.astra.nom_cle = {nom_cle} : Astra passe par {CLE_ASTRA} (GO-2026-11-22-111)")''')

# --- crédits -------------------------------------------------------------------------------------------------------------
r('''    - Non lisible : Minuit compté au prix relevé (v2) ; Argon, Astra, Carbon seulement sous la dispense écrite de la mère''',
  '''    - v8 : clé Claude (LUC) : `solde_console_usd` et `recharge_declaree_usd` (nombres ≥ 0, sources écrites) exigés ;
      couverture = leur somme ; alerte (code 3) si elle ne dépasse pas la part Claude estimée ; la part au pire (150) n'y est
      plus confrontée (compte au fil de l'eau pendant la course, `surveiller_cle_claude`) ; « non lisible » refusé.
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
            solde, recharge = x.get("solde_console_usd"), x.get("recharge_declaree_usd")
            sources = (x.get("source"), x.get("recharge_source"))
            if x.get("non_lisible") is True or not (_reel_positif(solde) and _reel_positif(recharge)) \\
                    or not all(isinstance(s, str) and s.strip() for s in sources):
                raise Refus(f"relevé des crédits : clé {nom} : solde_console_usd et recharge_declaree_usd (nombres ≥ 0) et leurs "
                            "sources (source, recharge_source) exigés (GO-2026-11-22-111) ; « non lisible » n'est pas admis")
            couverture = round(float(solde) + float(recharge), 6)
            d = {"fournisseur": fournisseur, "relais": fours, "parts_par_relais": dict(zip(fours, parts_k)), "lisible": True,
                 "solde_console_usd": solde, "recharge_declaree_usd": recharge, "couverture_usd": couverture,
                 "credit_usd": couverture, "reste_usd": couverture, "source": sources[0], "recharge_source": sources[1],
                 "part_au_pire_usd": part, "part_claude_estimee_usd": PART_CLAUDE_ESTIMEE_USD,
                 "regle": "part Claude comptée au fil de l'eau ; arrêt propre (code 6) si elle atteint la couverture moins "
                          f"{RESERVE_APPEL_CLAUDE_USD} USD (GO-2026-11-22-111)"}
            motifs = []
            if couverture <= PART_CLAUDE_ESTIMEE_USD:
                motifs.append(f"couverture {couverture} (solde {solde} + recharge {recharge}) ≤ part Claude estimée "
                              f"{PART_CLAUDE_ESTIMEE_USD}")
            d["motifs_d_arret"] = motifs
            sortie[nom] = d
            if motifs:
                alertes.append({"cle": nom, "fournisseur": fournisseur, "couverture_usd": couverture, "part_au_pire_usd": part,
                                "motifs": motifs})
            continue
        if not isinstance(x, dict):''')

# --- sonde d'Astra ---------------------------------------------------------------------------------------------------------
r('''    if o.get("version") != "sonde_astra_affinage_v2":
        raise Refus("sonde d'Astra : fichier non écrit par la sonde épinglée (scripts/sonde_astra_affinage_v2.py)")''',
  '''    if o.get("version") != VERSION_SONDE_ASTRA:
        raise Refus("sonde d'Astra : fichier non écrit par la sonde épinglée (scripts/sonde_astra_affinage_v3.py)")
    servi = o.get("modele_servi")
    attendu = MODELES_RELAIS["astra"][0]
    if not (isinstance(servi, str) and re.fullmatch(re.escape(attendu) + r"(-\\d{4}-?\\d{2}-?\\d{2})?", servi)):
        raise Refus(f"sonde d'Astra : modèle servi {servi!r}, {attendu} exigé")''')

# --- confidentialité, configuration ---------------------------------------------------------------------------------------
r('re.compile(r"\\b(Lazar|Ciric|lciric|Rigaud|Minuit|Heimersheim', 're.compile(r"\\b(Lazar|Ciric|lciric|Rigaud|Minuit|Luc|Heimersheim')
r('''                                                       "risques_v6")}''', '''                                                       "risques_v6", "changements_v8")}''')
r('''    """v2 : la configuration fixe nomme Minuit pour Claude, exclut Rigaud, et chaque espèce Claude porte Minuit."""
    if (fixe.get("cles") or {}).get("claude") != CLE_CLAUDE:
        raise Refus(f"configuration : cles.claude doit être {CLE_CLAUDE}")
    if any(c not in (fixe.get("cles_interdites") or []) for c in CLES_INTERDITES):
        raise Refus("configuration : la clé Rigaud doit figurer dans cles_interdites")''',
  '''    """v8 : la configuration fixe nomme LUC pour Claude, exclut Rigaud et Minuit, et chaque espèce Claude porte LUC."""
    if (fixe.get("cles") or {}).get("claude") != CLE_CLAUDE:
        raise Refus(f"configuration : cles.claude doit être {CLE_CLAUDE}")
    if any(c not in (fixe.get("cles_interdites") or []) for c in CLES_INTERDITES):
        raise Refus(f"configuration : les clés {list(CLES_INTERDITES)} doivent figurer dans cles_interdites")''')

# --- garde Google, palier d'Astra, surveillance de LUC : section neuve avant l'orchestrateur --------------------------------
NEUF = r'''

# --- v8 : garde des appels à Google (règle gelée de CLAUDE.md, GO-2026-11-21-71) ------------------------------------------------


ROLES_GOOGLE = {"carbon": (("proposeur_ideation", "proposeur", "consigne_proposeur"),),
                "argon": (("proposeur_ideation", "proposeur", "consigne_proposeur"), ("juge_ideation", "juge", "consigne_juge"))}
CARACTERES_PAR_CARTE_MAX = 9000  # consigne du proposeur, point 6 : « une carte entière, en 9 000 [caractères] au plus »
MOTIF_CAPTURE = "capture du lanceur v8 : rien n'est envoyé"


class FauxAmontGoogle:
    """Faux amont local de l'interface de Google : `countTokens` rend un compte (caractères / 4), toute génération
    (`generateContent`, `streamGenerateContent`, `batchGenerateContent`) est **capturée** et reçoit un 503. Aucun réseau."""

    def __init__(self):
        self.captures = []
        moi = self

        class H(BaseHTTPRequestHandler):
            def do_POST(self):
                n = int(self.headers.get("Content-Length") or 0)
                brut = self.rfile.read(n)
                try:
                    objet = json.loads(brut or b"{}")
                except ValueError:
                    objet = None
                if self.path.split("?")[0].endswith(":countTokens"):
                    code, rep = 200, {"totalTokens": max(1, len(brut) // 4)}
                else:
                    moi.captures.append({"chemin": self.path, "corps": objet})
                    code, rep = 503, {"error": {"code": 503, "message": MOTIF_CAPTURE}}
                donnees = json.dumps(rep).encode("utf-8")
                self.send_response(code)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(donnees)))
                self.end_headers()
                self.wfile.write(donnees)

            def do_GET(self):
                self.send_response(404)
                self.end_headers()

            def log_message(self, *a):
                pass

        self.serveur = ThreadingHTTPServer(("127.0.0.1", 0), H)
        self.serveur.daemon_threads = True
        threading.Thread(target=self.serveur.serve_forever, daemon=True).start()
        self.url = f"http://127.0.0.1:{self.serveur.server_address[1]}"

    def fermer(self):
        self.serveur.shutdown()
        self.serveur.server_close()


def charger_garde_google(chemin: Path, attendu: str):
    if not chemin.is_file() or sha256_fichier(chemin) != attendu:
        raise Refus(f"garde des appels à Google absente ou d'une autre empreinte que {attendu[:12]}… ({chemin})")
    spec = importlib.util.spec_from_file_location("garde_google_pour_lanceur_affinage_v8", chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def arguments_enveloppe_argon(enveloppe: Path) -> list:
    """Arguments que l'enveloppe d'Argon (épinglée) passe à sa commande : ceux de sa ligne `exec`, après `"$COMMANDE"`,
    `"$@"` retiré (l'orchestrateur n'en passe aucun)."""
    texte = enveloppe.read_text(encoding="utf-8").replace("\\\n", " ")  # lignes continuées jointes
    lignes = [l for l in texte.splitlines() if l.strip().startswith("exec ")]
    if len(lignes) != 1:
        raise Refus(f"enveloppe d'Argon : {len(lignes)} ligne(s) « exec » (une exigée)")
    jetons = shlex.split(lignes[0])
    if "$COMMANDE" not in jetons:
        raise Refus("enveloppe d'Argon : « $COMMANDE » absent de la ligne exec")
    return [j for j in jetons[jetons.index("$COMMANDE") + 1:] if j != "$@"]


def _remplacer_url_base(args: list, url: str) -> list:
    if "--url-base" not in args:
        return list(args) + ["--url-base", url]
    out = list(args)
    for k, a in enumerate(out[:-1]):
        if a == "--url-base":
            out[k + 1] = url
    return out


def capturer_corps_google(python: str, commande: Path, args: list, env_plus: dict, consigne: str) -> dict:
    """Joue la commande épinglée hors ligne devant le faux amont ; rend {code, capture (chemin, corps) ou None}."""
    amont = FauxAmontGoogle()
    try:
        env = {"PATH": os.environ.get("PATH", os.defpath), "LANG": "C.UTF-8", **env_plus}
        p = subprocess.run([python, "-I", "-B", str(commande)] + _remplacer_url_base(args, amont.url + "/v1beta"),
                           input=consigne.encode("utf-8"), env=env, capture_output=True, timeout=180)
    except (OSError, subprocess.SubprocessError) as e:
        raise Refus(f"garde Google : commande {commande.name} non jouée hors ligne ({type(e).__name__})") from None
    finally:
        amont.fermer()
    return {"code": p.returncode, "captures": amont.captures}


def corps_de_generation(capture: dict) -> tuple:
    """(corps de génération, mode de la garde) d'une capture : lot → la requête unique du lot ; sinon le corps lui-même."""
    chemin, corps = capture["chemin"].split("?")[0], capture["corps"]
    if not isinstance(corps, dict):
        return None, None
    if chemin.endswith(":batchGenerateContent"):
        try:
            return corps["batch"]["input_config"]["requests"]["requests"][0]["request"], "non_diffuse"
        except (KeyError, IndexError, TypeError):
            return None, "non_diffuse"
    return corps, ("flux" if chemin.endswith(":streamGenerateContent") else "non_diffuse")


def _provision(args: list, corps: dict):
    v = _valeur_arg(args, "--provision-pensee-jetons")
    if v is not None:
        try:
            return int(v)
        except ValueError:
            return None
    pensee = ((corps or {}).get("generationConfig") or {}).get("thinkingConfig") or {}
    return pensee.get("thinkingBudget")


def controler_chemins_google(r: "Reglages", decl: dict, pieces: dict, fixe: dict, liste: dict) -> dict:
    """Pour chaque commande Google déclarée (Argon, Carbon) et chaque rôle qu'elle tient : corps réel capturé hors ligne,
    `verifier_reglages_google` de la garde épinglée, limite de l'invite d'un proposeur (cartes × 9 000 caractères, un jeton au
    plus par caractère) sous le plafond de texte. Rend {espèce: {conforme, roles: [...]}} ; aucune consigne n'y est écrite."""
    garde = charger_garde_google(Path(pieces["garde_google"]["absolu"]), pieces["garde_google"]["sha256"])
    plus_long = max((texte_de_case(f) for f in liste["fils"]), key=len)
    out = {"garde": {"chemin": pieces["garde_google"]["chemin"], "sha256": pieces["garde_google"]["sha256"],
                     "version": getattr(garde, "VERSION_GARDE", None)}}
    for nom in ("argon", "carbon"):
        b = decl["fournisseurs"].get(nom)
        if b is None:
            continue
        if nom == "carbon":
            c = b["commande"]
            commande, args, env_cle = Path(c[3]), list(c[4:]), {}
        else:
            commande = Path(pieces["commande_argon"]["absolu"])
            args = arguments_enveloppe_argon(Path(pieces["enveloppe_argon"]["absolu"]))
            env_cle = {"GEMINI_API_KEY": "factice-relais"}  # comme l'enveloppe : jeton factice, la vraie clé reste au relais
        roles = []
        for role_pole, role_plafond, consigne_piece in ROLES_GOOGLE[nom]:
            consigne = Path(pieces[consigne_piece]["absolu"]).read_text(encoding="utf-8") + "\n\n" + plus_long
            env = dict(env_cle, PLAFOND_SESSION_USD=str(fixe["plafonds_session"][role_plafond]), ROLE_POLE=role_pole)
            jeu = capturer_corps_google(r.python, commande, args, env, consigne)
            problemes, reglages = [], None
            gens = [corps_de_generation(x) for x in jeu["captures"]]
            if len(gens) != 1 or gens[0][0] is None:
                problemes.append(f"aucun corps de génération capturé (code {jeu['code']}, {len(gens)} capture(s)) : la "
                                 "commande n'a pas atteint l'envoi, rien ne peut être vérifié")
            else:
                corps, mode = gens[0]
                provision = _provision(args, corps)
                problemes += list(garde.verifier_reglages_google(nom, corps, provision=provision, mots=None, mode=mode))
                config = corps.get("generationConfig") if isinstance(corps.get("generationConfig"), dict) else {}
                reglages = {"mode": mode, "provision": provision, "maxOutputTokens": config.get("maxOutputTokens"),
                            "thinkingConfig": config.get("thinkingConfig")}
                plafond = config.get("maxOutputTokens")
                if role_plafond == "proposeur" and isinstance(plafond, int) and isinstance(provision, int):
                    limite = int(fixe.get("cartes_par_appel") or 1) * CARACTERES_PAR_CARTE_MAX
                    if limite >= plafond - provision:
                        problemes.append(f"limite de l'invite : {limite} caractères (≤ {limite} jetons) ≥ plafond de texte "
                                         f"{plafond - provision}")
            roles.append({"role": role_pole, "plafond_session_usd": fixe["plafonds_session"][role_plafond], "code_commande": jeu["code"],
                          "reglages_captures": reglages, "problemes": problemes})
        out[nom] = {"commande": str(commande), "commande_sha256": sha256_fichier(commande), "roles": roles,
                    "conforme": all(not x["problemes"] for x in roles)}
    return out


def verifier_palier_astra(pieces: dict, liste: dict) -> dict:
    """v8 : prix d'Astra à palier (R-4905) : l'entrée la plus longue servie (consigne et fil en octets, plus le préambule du
    kit et les 1 024 octets de marge de la commande ; un jeton au plus par octet) reste sous 272 000 jetons."""
    consigne = Path(pieces["consigne_proposeur"]["absolu"]).read_bytes()
    borne = len(consigne) + max(len(texte_de_case(f).encode("utf-8")) for f in liste["fils"]) + 200 + PREAMBULE_KIT_OCTETS + 1024
    if borne >= PALIER_ASTRA_JETONS:
        raise Refus(f"Astra : entrée bornée à {borne} jetons ≥ palier {PALIER_ASTRA_JETONS} : prix 16 / 60, hors devis")
    return {"borne_entree_jetons": borne, "palier_jetons": PALIER_ASTRA_JETONS, "prix_usd_par_million": list(PRIX_ASTRA)}


# --- v8 : couverture de la clé Claude, comptée au fil de l'eau ------------------------------------------------------------------


class SurveillanceCleClaude:
    """Relit l'état du relais Claude ; `depasse()` rend un motif d'arrêt (ou None) : part engagée (dépense + engagé) qui
    atteint la couverture moins la réserve d'un appel, ou état illisible trois fois de suite."""

    def __init__(self, r: "Reglages", url: str, couverture: float):
        self.r, self.url, self.couverture = r, url, couverture
        self.seuil = round(couverture - RESERVE_APPEL_CLAUDE_USD, 6)
        self.illisibles, self.lectures, self.derniere = 0, 0, None

    def depasse(self):
        try:
            etat = (self.r.lire_etat_relais or _etat_relais)(self.url)
            engagee = float(etat.get("depense_usd") or 0.0) + float(etat.get("engage_usd") or 0.0)
            if not math.isfinite(engagee):
                raise ValueError("non fini")
        except Exception as e:  # noqa: BLE001 — une lecture manquée est comptée, jamais tue
            self.illisibles += 1
            if self.illisibles >= LECTURES_ILLISIBLES_MAX:
                return f"état du relais Claude illisible {self.illisibles} fois de suite ({type(e).__name__}) : part Claude non comptable"
            return None
        self.illisibles, self.lectures = 0, self.lectures + 1
        self.derniere = round(engagee, 6)
        if engagee >= self.seuil:
            return (f"part Claude engagée {self.derniere} USD ≥ couverture {self.couverture} − réserve d'un appel "
                    f"{RESERVE_APPEL_CLAUDE_USD} = {self.seuil} USD")
        return None

    def bilan(self) -> dict:
        return {"couverture_usd": self.couverture, "seuil_arret_usd": self.seuil, "lectures": self.lectures,
                "derniere_part_engagee_usd": self.derniere, "illisibles_de_suite": self.illisibles}


# --- (6) orchestrateur --------------------------------------------------------------------------------------------------------
'''
r('''

# --- (6) orchestrateur --------------------------------------------------------------------------------------------------------
''', NEUF)

# --- exécution ---------------------------------------------------------------------------------------------------------------
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
r('''r.dossier_runs / (ident.replace(SUFFIXE_RUN, "") + "-alerte-credits-affinage-mentors-v6"), parts)''',
  '''r.dossier_runs / (ident.replace(SUFFIXE_RUN, "") + "-alerte-credits-affinage-mentors-v8"), parts)''')
r('''        "carbon": decl["carbon"], "cles_employees": decl["cles"],''',
  '''        "carbon": decl["carbon"], "cles_employees": decl["cles"], "go_exception_cle": go_cle, "garde_google": google,
        "palier_astra": palier_astra, "devis_v8_marge_comprise_usd": DEVIS_V8_MARGE_COMPRISE["avec_carbon" if decl["carbon"]["active"] else "sans_carbon"],''')
r('''        "cle_claude": {"nom": CLE_CLAUDE, "presente_dans_l_environnement_du_lanceur": cle_presente, "valeur": "jamais lue",
                       "cles_exclues": list(CLES_INTERDITES)},''',
  '''        "cle_claude": {"nom": CLE_CLAUDE, "presente_dans_l_environnement_du_lanceur": cle_presente, "valeur": "jamais lue",
                       "cles_exclues": list(CLES_INTERDITES), "exception": GO_EXCEPTION_CLE,
                       "couverture_usd": (credits.get(CLE_CLAUDE) or {}).get("couverture_usd"),
                       "surveillance": "au fil de l'eau, toutes les " + str(r.intervalle_surveillance_s) + " s" if reel else "moteur simulé : aucune"},''')
r('''    code, pid, echec, arret_credit = None, None, None, []
    debut = _dt.datetime.now(_dt.timezone.utc)''',
  '''    code, pid, echec, arret_credit = None, None, None, []
    surveillance = None
    if reel:
        couverture = (credits.get(CLE_CLAUDE) or {}).get("couverture_usd")
        if not isinstance(couverture, (int, float)):
            raise Refus(f"couverture de {CLE_CLAUDE} inconnue : la part Claude ne peut pas être comptée au fil de l'eau")
        surveillance = SurveillanceCleClaude(r, decl["fournisseurs"]["claude"]["url_relais"], float(couverture))
    arret_couverture = None
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
                    if surveillance is not None and arret_couverture is None and time.monotonic() >= prochaine:
                        prochaine = time.monotonic() + float(r.intervalle_surveillance_s)
                        arret_couverture = surveillance.depasse()
                        if arret_couverture:  # GO-2026-11-22-111 : arrêt propre, par PID (R10), jamais de repli silencieux
                            print(json.dumps({"arret_couverture_cle_claude": arret_couverture, "pid": enfant.pid},
                                             ensure_ascii=False), file=sys.stderr, flush=True)
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
             "couverture_cle_claude": dict(surveillance.bilan(), arret=arret_couverture) if surveillance else {"moteur": "simulé"}}''')
r('''    if alertes_apres or depasse:''', '''    if arret_couverture:
        ecrire_scelle(dossier_run / "alerte-couverture-cle-claude.json",
                      {"alerte": f"course arrêtée proprement : couverture de {CLE_CLAUDE} atteinte ou non comptable (GO-2026-11-22-111)",
                       "motif": arret_couverture, "bilan": surveillance.bilan(), "pour": "la mère, qui prévient Lazar"})
    if alertes_apres or depasse:''')
r('''    if depasse:
        return 4
    if bilan["arret_au_premier_refus_pour_credit"]:''', '''    if depasse:
        return 4
    if arret_couverture:
        return 6
    if bilan["arret_au_premier_refus_pour_credit"]:''')

# --- essai à blanc -----------------------------------------------------------------------------------------------------------
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
r('''    r.moteur, r.exiger_bac_a_sable, r.verifier_go = "simule", False, False''',
  '''    r.moteur, r.exiger_bac_a_sable, r.verifier_go = "simule", False, False
    r.ref_registre = None''')
r('''        return executer(reglages or Reglages.production())
    except AlerteCredit as e:''', '''        return executer(reglages or Reglages.production())
    except AlerteCredit as e:''')

print([l for l in src.splitlines() if "gpt-6-astra" in l or "MINUIT" in l or "Minuit" in l])
(racine / "scripts/lancer_course_affinage_mentors_v8.py").write_text(src, encoding="utf-8")
print("écrit", len(src.splitlines()), "lignes")
