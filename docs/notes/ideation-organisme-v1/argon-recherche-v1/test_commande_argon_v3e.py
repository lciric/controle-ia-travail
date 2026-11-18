"""Essais de commande_argon_v3e.py (la v3d, plus la lecture du modèle demandé par le noyau, `MODELE_DEMANDE_POLE`). Copie de
`test_commande_argon_v3d.py` (inchangée, R12) qui vise la v3e : la suite de la v3d est rejouée telle quelle sur la v3e
(seuls changent le fichier importé et visé, le nom de version attendu, et le témoin v2 qui, à défaut de la copie installée
`/opt/argon/commande_argon_v2.py`, est lu dans `../lancement-v2/commande_argon_v2.py`, même empreinte scellée) ; les essais
de l'enveloppe visent toujours la v4d, inchangée. Plus la section « v3e » : (a) `MODELE_DEMANDE_POLE` différent de `--modele`
→ code 2, rien envoyé, coût plancher, message qui nomme les deux modèles (contre-épreuve : la v3d, qui ne lit pas la
variable, rend le code 0) ; (b) `MODELE_DEMANDE_POLE` égal à `--modele` → même comportement que la v3d sur le cas sain du
faux amont ; (c) variable absente → identique à la v3d, succès et échec ; (d) la source de la v3e ne diffère de celle de la
v3d que par l'en-tête, la constante `VERSION`, le bloc de trois lignes après la vérification de `ROLE_POLE` et les deux
préfixes de la sortie d'erreur (`difflib`). Écrite le 18 novembre 2026 ; aucune clé réelle, aucun appel réseau.
Lancement :

    cd docs/notes/ideation-organisme-v1/argon-recherche-v1 && PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q \\
        -p no:cacheprovider test_commande_argon_v3e.py

--- en-tête des essais de la v3d, tel quel ---

Essais de commande_argon_v3d.py (la v3c corrigée après sa contre-lecture par deux relecteurs neufs). Copie de
`test_commande_argon_v3c.py` (empreinte `33a69adcd793a569…`, inchangée, R12) qui vise la v3d : tous les essais de la v3c
gardent leur sens ; seuls changent le fichier visé, le nom de version, les champs ajoutés (`total_jetons`,
`ecart_total_jetons`) et les essais de l'enveloppe, qui visent la v4d. Plus un essai par constat, en échec sur la v3c
(contre-épreuve : la section « v3d (1) » lancée contre la v3c), et ses cas sains (R5) : bloquant 1 (scénario exact,
avec et sans recherche ; écart sous le plafond et sous la provision, code 11 ; écart contre la provision, code 9 ;
total mal formé, code 5 ; cas sains : total égal à la somme, total absent, total sous la somme). Le faux amont v3
(inchangé) rend toujours un total égal à la somme ; les essais du constat remplacent donc `poster` dans le processus.
Lancement :

    cd docs/notes/ideation-organisme-v1/argon-recherche-v1 && PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q \\
        -p no:cacheprovider test_commande_argon_v3d.py

--- en-tête des essais de la v3c, tel quel ---

Essais de commande_argon_v3c.py (la v3b corrigée après sa contre-lecture) devant le faux amont local v3, et de bout en
bout derrière le relais (v1 en témoin, v2) — aucune clé réelle, aucun appel à l'interface de Google. Copie de
`test_commande_argon_v3b.py` (inchangée, R12) qui vise la v3c (les essais de la v3b gardent leur sens ; seuls changent le
fichier visé, le nom de version, les champs ajoutés et l'essai de l'enveloppe, qui vise la v4c), plus un essai par constat
de la contre-lecture, en échec sur la v3b (contre-épreuve : ces essais lancés contre une copie de la v3b), plus leurs
cas sains (R5) : bloquant 1 (scénario exact, code 9 ; sans recherche, code 10 ; avec recherche et sortie au-delà de
maxOutputTokens, code 10 ; cas sains : excédent sous le plafond, excédent dans la provision, bord exact du pire cas),
mineur 2 (30 chaînes et un null), mineur 3 (jetons d'outil sans requête), mineur 4 (ordre des réglages de l'enveloppe).
Lancement :

    cd docs/notes/ideation-organisme-v1/argon-recherche-v1 && PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q \\
        -p no:cacheprovider test_commande_argon_v3c.py
"""

import difflib
import json
import math
import os
import shlex
import subprocess
import sys

import pytest

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import commande_argon_v3e as v3c  # noqa: E402 — nom gardé : la v3e, importée comme la suite v3d importe la v3d ; nom importable (essais unitaires de nettoyer_web, adresse_permise)

V3C = os.path.join(ICI, "commande_argon_v3e.py")  # nom gardé : la v3e
V3D = os.path.join(ICI, "commande_argon_v3d.py")  # la v3d, témoin des essais « v3e »
V2 = "/opt/argon/commande_argon_v2.py"  # la copie installée ; à défaut, la même (empreinte scellée) dans le dépôt
if not os.path.exists(V2):
    V2 = os.path.join(ICI, "..", "lancement-v2", "commande_argon_v2.py")
FAUX = os.path.join(ICI, "faux_amont_gemini_recherche_v3.py")
RELAIS_V1 = os.path.join(ICI, "..", "lancement-v2", "relais_gemini_v1.py")
RELAIS_V2 = os.path.join(ICI, "relais_gemini_v2.py")
CLE = "cle-FACTICE-tres-secrete-42"  # factice : jamais une vraie clé
CLE_DU_RELAIS = "cle-factice-du-relais-AIzaTEST-9876543210"  # factice : la « vraie » clé que seul le relais détient
CONSIGNE = "Propose trois idées de moniteurs pour le contrôle des agents.\n" * 20
PRIX_E, PRIX_S = 8.3, 41.5
PROVISION_OUTIL = 32768


@pytest.fixture
def amont(tmp_path):
    """Lance un faux amont (options données) ; rend (url de base, lecteur du journal). Arrêt par le PID (R10)."""
    processus = []

    def lancer(*options):
        journal = tmp_path / f"journal-{len(processus)}.jsonl"
        p = subprocess.Popen([sys.executable, "-I", "-B", FAUX, "--port", "0", "--journal", str(journal), *options],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        processus.append(p)
        ligne = p.stdout.readline().strip()
        assert ligne.startswith("pret http://127.0.0.1:"), ligne

        def lire():
            if not journal.exists():
                return []
            return [json.loads(x) for x in journal.read_text(encoding="utf-8").splitlines() if x.strip()]

        return ligne.split(" ", 1)[1] + "/v1beta", lire

    yield lancer
    for p in processus:
        p.terminate()
        try:
            p.wait(timeout=5)
        except subprocess.TimeoutExpired:
            p.kill()
            p.wait()


def lancer_commande(script, url, *options, plafond="3", consigne=CONSIGNE, cle=CLE):
    env = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "PLAFOND_SESSION_USD": plafond, "ROLE_POLE": "proposeur_ideation",
           "GEMINI_API_KEY": cle}
    r = subprocess.run([sys.executable, "-I", "-B", script, "--prix-entree", str(PRIX_E), "--prix-sortie", str(PRIX_S),
                        *options, "--url-base", url], input=consigne.encode("utf-8"), capture_output=True, env=env,
                       timeout=60)
    sortie = r.stdout.decode("utf-8")
    erreurs = r.stderr.decode("utf-8")
    objet = json.loads(sortie.strip().splitlines()[-1])
    return r.returncode, objet, sortie, erreurs


def corps_de(journal, action):
    return [e["corps"] for e in journal if e["chemin"].endswith(":" + action)]


def cout_jetons(objet):
    u = objet["usage"]
    return u["entree"] * PRIX_E / 1e6 + u["sortie"] * PRIX_S / 1e6


CHAMPS_V3C = {"total_jetons", "ecart_total_jetons",  # v3d
              "entree_excedent_jetons", "provision_outil_consommee_jetons",  # v3c
              "requetes_web", "sources_web", "recherche_web", "requetes_web_facturees", "requetes_web_origine",
              "prix_requete_web_usd", "max_requetes_web_pire_cas", "cout_recherche_usd", "appuis_web", "outil_jetons",
              "provision_outil_jetons", "supplement_recherche_usd"}


# --- (a) sans l'option : comportement de la v2 ---------------------------------------------------------------------------

def test_sans_outil_meme_corps_et_meme_sortie_que_la_v2(amont):
    url, journal = amont()
    code2, obj2, _, _ = lancer_commande(V2, url)
    code3, obj3, _, _ = lancer_commande(V3C, url)
    j = journal()
    gen2, gen3 = corps_de(j, "generateContent")
    cpt2, cpt3 = corps_de(j, "countTokens")
    assert gen3 == gen2 and cpt3 == cpt2
    assert "tools" not in gen3 and set(gen3) == {"contents", "generationConfig"}
    assert code2 == code3 == 0
    assert obj3["version"] == "commande-argon-v3e" and obj2["version"] == "commande-argon-v2"
    assert obj3["requetes_web"] == [] and obj3["sources_web"] == [] and obj3["recherche_web"] is False
    assert obj3["provision_outil_jetons"] is None and obj3["supplement_recherche_usd"] is None
    assert obj3["entree_excedent_jetons"] == 0 and obj3["provision_outil_consommee_jetons"] is None
    commun3 = {k: v for k, v in obj3.items() if k not in CHAMPS_V3C | {"version"}}
    commun2 = {k: v for k, v in obj2.items() if k != "version"}
    assert commun3 == commun2  # même texte, même coût, même garde, même diagnostic
    assert "Sources consultées" not in obj3["texte"]


def test_sans_outil_garde_identique_a_la_v2_au_bord_du_plafond(amont):
    """La provision d'outil n'est comptée qu'avec --recherche-web : sans elle, même refus et même acceptation que la v2."""
    url, _ = amont()
    for plafond in ("0.45", "0.6", "0.9"):
        c2, o2, _, _ = lancer_commande(V2, url, "--sans-compter-jetons", plafond=plafond)
        c3, o3, _, _ = lancer_commande(V3C, url, "--sans-compter-jetons", plafond=plafond)
        assert c2 == c3 and o2["pire_cas_usd"] == o3["pire_cas_usd"] and o2["cout_usd"] == o3["cout_usd"]


# --- (a, d) avec l'option : l'outil google_search, et rien d'autre ------------------------------------------------------

def test_avec_recherche_le_corps_porte_exactement_l_outil(amont):
    url, journal = amont()
    _, obj2, _, _ = lancer_commande(V2, url)
    code, obj, _, _ = lancer_commande(V3C, url, "--recherche-web")
    assert code == 0, obj["erreur"]
    j = journal()
    gen2, gen3 = corps_de(j, "generateContent")
    cpt2, cpt3 = corps_de(j, "countTokens")
    assert set(gen3) == {"contents", "generationConfig", "tools"}
    assert gen3["tools"] == [{"google_search": {}}]
    assert gen3["contents"] == gen2["contents"]
    assert set(gen3["generationConfig"]) == {"maxOutputTokens", "thinkingConfig"}
    assert gen3["generationConfig"]["thinkingConfig"] == gen2["generationConfig"]["thinkingConfig"]
    assert cpt3 == cpt2 and "tools" not in cpt3  # countTokens inchangé
    # le reste du plafond paie d'abord 20 requêtes à 0,05 USD et 32 768 jetons d'outil au prix d'entrée, puis la provision
    # de pensée, puis la sortie
    garde = obj["entree_jetons_garde"]
    fixe = garde * PRIX_E / 1e6 + 20 * 0.05 + PROVISION_OUTIL * PRIX_E / 1e6
    attendu = min(65536, math.floor((3 - fixe) / (PRIX_S / 1e6)) - 8192)
    assert gen3["generationConfig"]["maxOutputTokens"] == attendu < gen2["generationConfig"]["maxOutputTokens"]
    assert obj["pire_cas_usd"] <= 3 and obj["provision_outil_jetons"] == PROVISION_OUTIL
    assert obj["pire_cas_usd"] == pytest.approx(fixe + (attendu + 8192) * PRIX_S / 1e6, abs=1e-6)


# --- (b) sources dans le texte et le JSON ---------------------------------------------------------------------------------

def test_sources_dans_le_texte_et_le_json(amont):
    url, _ = amont()
    code, obj, _, _ = lancer_commande(V3C, url, "--recherche-web")
    assert code == 0
    assert obj["texte"].startswith("Réponse factice d'Argon.")
    assert "Sources consultées (recherche Google)" in obj["texte"]
    assert obj["requetes_web"] == ["requête factice 1 sur le contrôle des agents",
                                   "requête factice 2 sur le contrôle des agents"]
    assert len(obj["sources_web"]) == 3
    for i, s in enumerate(obj["sources_web"], 1):
        assert s == {"uri": f"https://vertexaisearch.cloud.google.com/grounding-api-redirect/FAUX{i}",
                     "titre": f"source-factice-{i}.example.org"}
        assert s["uri"] in obj["texte"] and s["titre"] in obj["texte"]
    for q in obj["requetes_web"]:
        assert q in obj["texte"]
    assert obj["appuis_web"] == 2 and obj["requetes_web_origine"] == "webSearchQueries"
    assert obj["supplement_recherche_usd"] == 0 and obj["avertissements"] == []


# --- (c) coût ------------------------------------------------------------------------------------------------------------

@pytest.mark.parametrize("prix", ["0.05", "0.014"])
def test_cout_jetons_plus_requetes_fois_prix(amont, prix):
    url, _ = amont()
    code, obj, _, _ = lancer_commande(V3C, url, "--recherche-web", "--prix-requete-web-usd", prix)
    assert code == 0 and obj["cout_origine"] == "usage"
    assert obj["requetes_web_facturees"] == 2
    assert obj["cout_recherche_usd"] == pytest.approx(2 * float(prix))
    assert obj["cout_usd"] == pytest.approx(cout_jetons(obj) + 2 * float(prix), rel=1e-12)


def test_jetons_d_outil_comptes_au_prix_d_entree(amont):
    url, _ = amont("--usage-outil", "1000")
    code, obj, _, erreurs = lancer_commande(V3C, url, "--recherche-web")
    assert code == 0 and obj["outil_jetons"] == 1000
    assert obj["cout_usd"] == pytest.approx(cout_jetons(obj) + 1000 * PRIX_E / 1e6 + 2 * 0.05, rel=1e-12)
    assert "toolUsePromptTokenCount" in erreurs


def test_garde_pire_cas_refuse_un_plafond_trop_bas(amont):
    url, journal = amont()
    # 0,9 USD : assez sans recherche (≈ 0,51 USD de pire cas minimal), pas avec 20 requêtes à 0,05 USD
    code, obj, _, erreurs = lancer_commande(V3C, url, "--recherche-web", "--sans-compter-jetons", plafond="0.9")
    assert code == 4 and obj["envoye"] is False and obj["cout_usd"] == 1e-6 and obj["cout_origine"] == "plancher"
    assert "20 requêtes de recherche" in obj["erreur"] and "rien envoyé" in obj["erreur"]
    assert "32768 jetons d'outil" in obj["erreur"]
    assert journal() == []  # rien n'est parti
    code, obj, _, _ = lancer_commande(V3C, url, "--recherche-web", plafond="0.9")  # avec countTokens (gratuit)
    assert code == 4 and obj["envoye"] is False
    assert corps_de(journal(), "generateContent") == []
    code, obj, _, _ = lancer_commande(V3C, url, "--sans-compter-jetons", plafond="0.9")  # même plafond, sans recherche
    assert code == 0


def test_garde_compte_la_provision_d_outil(amont):
    """Un plafond qui passe sans provision d'outil et non avec : refusé sans envoi ; accepté avec une provision nulle."""
    url, journal = amont()
    # pire cas minimal sans provision d'outil : entrée + 1 USD + (4 096 + 8 192) × 41,5e-6 ≈ 1,53 USD ; la provision ajoute
    # 32 768 × 8,3e-6 ≈ 0,27 USD
    code, obj, _, _ = lancer_commande(V3C, url, "--recherche-web", "--sans-compter-jetons", plafond="1.6")
    assert code == 4 and obj["envoye"] is False and journal() == []
    code, obj, _, _ = lancer_commande(V3C, url, "--recherche-web", "--sans-compter-jetons", "--provision-outil-jetons",
                                      "0", plafond="1.6")
    assert code == 0 and obj["provision_outil_jetons"] == 0


def test_grounding_absent_cout_au_maximum_signale(amont):
    url, _ = amont("--sans-grounding")
    code, obj, _, erreurs = lancer_commande(V3C, url, "--recherche-web")
    assert code == 0
    assert obj["requetes_web"] == [] and obj["sources_web"] == []
    assert obj["requetes_web_facturees"] == 20 and obj["requetes_web_origine"].startswith("maximum_pire_cas")
    assert obj["cout_usd"] == pytest.approx(cout_jetons(obj) + 20 * 0.05, rel=1e-12)
    assert any("groundingMetadata absent" in a for a in obj["avertissements"])
    assert "groundingMetadata absent" in erreurs
    assert "groundingMetadata absent" in obj["texte"]


def test_requetes_illisibles_cout_au_maximum(amont):
    url, _ = amont("--sans-requetes")
    code, obj, _, _ = lancer_commande(V3C, url, "--recherche-web", "--max-requetes-web-pire-cas", "7")
    assert code == 0 and obj["requetes_web_facturees"] == 7 and len(obj["sources_web"]) == 3
    assert obj["cout_usd"] == pytest.approx(cout_jetons(obj) + 7 * 0.05, rel=1e-12)
    assert any("webSearchQueries" in a for a in obj["avertissements"])


def test_requetes_au_dela_du_pire_cas_code_8(amont):
    url, _ = amont("--requetes", "5")
    code, obj, _, _ = lancer_commande(V3C, url, "--recherche-web", "--max-requetes-web-pire-cas", "3")
    assert code == 8 and obj["texte"] == "" and obj["cout_origine"] == "usage"
    assert obj["cout_usd"] == pytest.approx(cout_jetons(obj) + 5 * 0.05, rel=1e-12)
    assert "au-delà du pire cas" in obj["erreur"]
    assert obj["supplement_recherche_usd"] == pytest.approx(2 * 0.05)


# --- v3b (1) : usage illisible et requêtes au-delà du maximum --------------------------------------------------------------

@pytest.mark.parametrize("usage", [("--sans-usage",), ("--usage-outil", "-1")])
def test_usage_absent_et_requetes_au_dela_du_maximum_cout_jamais_sous_estime(amont, usage):
    url, _ = amont("--requetes", "30", *usage)
    code, obj, _, _ = lancer_commande(V3C, url, "--recherche-web")  # maximum 20
    assert code == 8, obj["erreur"]
    assert obj["texte"] == "" and obj["cout_origine"] == "pire_cas" and obj["requetes_web_facturees"] == 30
    assert obj["supplement_recherche_usd"] == pytest.approx(10 * 0.05)
    assert obj["cout_usd"] == pytest.approx(obj["pire_cas_usd"] + 10 * 0.05, abs=1e-9)
    assert obj["cout_usd"] >= obj["pire_cas_usd"] + 0.5 - 1e-9  # au moins le minimum facturé des 10 requêtes de plus
    assert "au-delà du pire cas" in obj["erreur"] and "30 lues" in obj["erreur"]


@pytest.mark.parametrize("usage", [("--sans-usage",), ("--usage-outil", "-1")])
def test_usage_illisible_sans_requetes_en_trop_reste_code_5_au_pire_cas(amont, usage):
    url, _ = amont(*usage)
    code, obj, _, _ = lancer_commande(V3C, url, "--recherche-web")
    assert code == 5 and obj["cout_origine"] == "pire_cas" and obj["cout_usd"] == obj["pire_cas_usd"]
    assert obj["supplement_recherche_usd"] == 0


# --- v3b (2) : requêtes vides, sources présentes ---------------------------------------------------------------------------

def test_requetes_vides_mais_sources_rendues_au_moins_une_requete_comptee(amont):
    url, _ = amont("--requetes-vides")
    code, obj, _, erreurs = lancer_commande(V3C, url, "--recherche-web")
    assert code == 0 and len(obj["sources_web"]) == 3
    assert obj["requetes_web_facturees"] == 20 >= 1
    assert obj["requetes_web_origine"] == "maximum_pire_cas (requêtes vides, sources présentes)"
    assert obj["cout_usd"] == pytest.approx(cout_jetons(obj) + 20 * 0.05, rel=1e-12)
    assert any("webSearchQueries vide" in a for a in obj["avertissements"]) and "webSearchQueries vide" in erreurs


def test_requetes_vides_sans_aucun_temoin_zero_requete(amont):
    url, _ = amont("--grounding-vide")
    code, obj, _, _ = lancer_commande(V3C, url, "--recherche-web")
    assert code == 0 and obj["requetes_web_facturees"] == 0 and obj["cout_recherche_usd"] == 0
    assert obj["requetes_web_origine"] == "webSearchQueries"
    assert obj["cout_usd"] == pytest.approx(cout_jetons(obj), rel=1e-12)


# --- v3b (3) : jetons d'outil au-delà de la provision ----------------------------------------------------------------------

def test_cout_au_dela_du_plafond_n_est_pas_un_succes(amont):
    url, _ = amont("--usage-outil", "400000")
    code, obj, _, _ = lancer_commande(V3C, url, "--recherche-web")
    assert code == 9 and obj["texte"] == "" and obj["cout_origine"] == "usage"
    assert obj["cout_usd"] > 3  # le coût réel est rendu, jamais sous-estimé
    assert obj["cout_usd"] == pytest.approx(cout_jetons(obj) + 400000 * PRIX_E / 1e6 + 2 * 0.05, rel=1e-12)
    assert "au-delà de la provision" in obj["erreur"] and "400000" in obj["erreur"]


def test_jetons_d_outil_a_la_provision_exacte_succes_sous_le_pire_cas(amont):
    url, _ = amont("--usage-outil", str(PROVISION_OUTIL))
    code, obj, _, _ = lancer_commande(V3C, url, "--recherche-web")
    assert code == 0 and obj["cout_usd"] <= obj["pire_cas_usd"] <= 3
    url, _ = amont("--usage-outil", str(PROVISION_OUTIL + 1))
    code, obj, _, _ = lancer_commande(V3C, url, "--recherche-web")
    assert code == 9


def test_ordre_des_echecs_pensees_puis_requetes_puis_outil(amont):
    url, _ = amont("--pensees", "9000", "--requetes", "30", "--usage-outil", "400000")
    assert lancer_commande(V3C, url, "--recherche-web")[0] == 7
    url, _ = amont("--requetes", "30", "--usage-outil", "400000")
    assert lancer_commande(V3C, url, "--recherche-web")[0] == 8
    url, _ = amont("--usage-outil", "400000", "--modele-servi", "gemini-9-autre")
    assert lancer_commande(V3C, url, "--recherche-web")[0] == 9  # prime sur le code 5


# --- v3b (4) : parties refusées --------------------------------------------------------------------------------------------

@pytest.mark.parametrize("partie", ["functionCall", "functionResponse", "executableCode", "codeExecutionResult"])
def test_parties_d_appel_ou_de_code_refusees(amont, partie):
    url, _ = amont("--partie", partie)
    code, obj, _, _ = lancer_commande(V3C, url, "--recherche-web")
    assert code == 5 and obj["texte"] == "" and partie in obj["erreur"]
    assert "seul google_search est déclaré" in obj["erreur"]
    code, obj, _, _ = lancer_commande(V3C, url)
    assert code == 5 and "aucun outil n'est déclaré" in obj["erreur"]


# --- v3b (5) : la clé ne sort jamais --------------------------------------------------------------------------------------

@pytest.mark.parametrize("options_amont", [(), ("--refus", "http400"), ("--cle-dans-titre",), ("--sans-grounding",),
                                           ("--modele-servi", "autre"), ("--cle-dans-modele",), ("--cle-dans-fin",),
                                           ("--cle-coupee-dans-titre",)])
def test_cle_jamais_dans_la_sortie(amont, options_amont):
    url, journal = amont(*options_amont)
    code, obj, sortie, erreurs = lancer_commande(V3C, url, "--recherche-web")
    assert CLE not in sortie and CLE not in erreurs
    assert all(e["cle_presente"] for e in journal())  # la clé (factice) est bien partie dans l'en-tête
    if options_amont == ("--refus", "http400"):
        assert "[clé]" in obj["erreur"]
    if options_amont == ("--cle-dans-titre",):
        assert code == 0 and "[clé]" in obj["sources_web"][0]["titre"]
    if options_amont == ("--cle-dans-modele",):
        assert code == 0 and obj["modele_servi"] == "gemini-4-argon-[clé]"
    if options_amont == ("--cle-dans-fin",):
        assert code == 5 and obj["fin"] == "AUTRE [clé]"
    if options_amont == ("--cle-coupee-dans-titre",):
        assert code == 0 and "[clé]" in obj["sources_web"][0]["titre"]
        m = len(CLE) // 2
        assert CLE[:m] + " " + CLE[m:] not in sortie


def test_nettoyer_web_masque_avant_et_apres_le_nettoyage():
    m = len(CLE) // 2
    assert v3c.nettoyer_web(f"a {CLE[:m]}\x00{CLE[m:]} b", CLE) == "a[clé]b"  # forme compacte, masquée
    assert v3c.nettoyer_web(f"a {CLE[:m]}\n{CLE[m:]} b", CLE) == "a[clé]b"
    assert v3c.nettoyer_web(f"titre\x00propre", CLE) == "titre propre"  # sans clé : rien ne change
    assert v3c.nettoyer_web(f"x{CLE}", CLE, 3) == "x[c…"  # le masquage passe avant la coupe
    assert v3c.masquer_objet({"a": [CLE, {CLE: 1}], "b": 2.0}, CLE) == {"a": ["[clé]", {"[clé]": 1}], "b": 2.0}


def _lancer_relais(script, amont_url):
    env = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "GEMINI_API_KEY": CLE_DU_RELAIS}
    p = subprocess.Popen([sys.executable, "-I", "-B", script, "--port", "0", "--amont", amont_url], env=env,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    ligne = p.stdout.readline()
    assert ligne.startswith("relais prêt sur "), ligne
    return p, ligne.split()[3]


def _arreter(p):
    p.kill()  # par le PID (R10)
    p.communicate(timeout=10)


@pytest.mark.parametrize("options_amont", [("--cle-dans-titre",), ("--refus", "http400"), ("--cle-dans-modele",)])
def test_bout_en_bout_relais_v2_la_vraie_cle_ne_sort_pas(amont, options_amont):
    url, journal = amont(*options_amont)
    relais, url_relais = _lancer_relais(RELAIS_V2, url.replace("/v1beta", ""))
    try:
        code, obj, sortie, erreurs = lancer_commande(V3C, url_relais + "/v1beta", "--recherche-web", cle="factice-relais")
    finally:
        _arreter(relais)
    assert CLE_DU_RELAIS not in sortie and CLE_DU_RELAIS not in erreurs
    assert all(e["cle_presente"] for e in journal())
    if options_amont == ("--cle-dans-titre",):
        assert code == 0 and obj["sources_web"][0]["titre"] == "titre avec clé [clé]"
    if options_amont == ("--refus", "http400"):
        assert code == 3 and "[clé]" in obj["erreur"]
    if options_amont == ("--cle-dans-modele",):
        assert code == 0 and obj["modele_servi"] == "gemini-4-argon-[clé]"


def test_temoin_relais_v1_laisse_passer_la_vraie_cle_dans_le_corps(amont):
    """Artefact (R5) : le défaut que corrige le relais v2. Avec le relais v1, la commande ne peut masquer que la clé factice
    qu'elle détient ; la vraie clé recopiée par l'amont dans un titre traverse jusqu'à la sortie."""
    url, _ = amont("--cle-dans-titre")
    relais, url_relais = _lancer_relais(RELAIS_V1, url.replace("/v1beta", ""))
    try:
        code, obj, sortie, _ = lancer_commande(V3C, url_relais + "/v1beta", "--recherche-web", cle="factice-relais")
    finally:
        _arreter(relais)
    assert code == 0 and CLE_DU_RELAIS in obj["sources_web"][0]["titre"]


# --- v3b (6) : dernière ligne lisible par splitlines ----------------------------------------------------------------------

def test_derniere_ligne_lisible_par_splitlines_avec_separateur_unicode(amont):
    url, _ = amont("--texte-separateurs")
    code, obj, sortie, _ = lancer_commande(V3C, url, "--recherche-web")
    assert code == 0
    # ce que fait AdaptateurCommandeExterne.lire_derniere_ligne (orchestrateur-v52/arbre/pole/adaptateurs.py)
    lignes = [l for l in sortie.splitlines() if l.strip()]
    lu = json.loads(lignes[-1])
    assert len(lignes) == 1 and lu == obj
    assert " ligne paragraphe\x85suite" in lu["texte"]
    assert " " not in sortie and " " not in sortie and "\x85" not in sortie


# --- v3b (7) : adresses des sources ---------------------------------------------------------------------------------------

@pytest.mark.parametrize("uri, schema", [("javascript:alert(1)//x", "javascript"), ("data:text/html,x", "data"),
                                         ("file:///etc/passwd", "file"), ("https:///sans-hote", "https sans hôte"),
                                         ("sans-schema", "absent")])
def test_adresse_non_web_refusee(amont, uri, schema):
    url, _ = amont("--uri-source", uri)
    code, obj, _, _ = lancer_commande(V3C, url, "--recherche-web")
    assert code == 0
    assert obj["sources_web"][0]["uri"] == f"[adresse refusée : schéma {schema}]"
    assert uri not in obj["texte"] and uri not in json.dumps(obj["sources_web"])
    assert any("adresse(s) de source refusée(s)" in a for a in obj["avertissements"])
    assert obj["sources_web"][1]["uri"].startswith("https://")


def test_adresse_permise():
    assert v3c.adresse_permise("https://exemple.org/a") == (True, None)
    assert v3c.adresse_permise("http://exemple.org") == (True, None)
    assert v3c.adresse_permise("HTTPS://exemple.org") == (True, None)
    assert v3c.adresse_permise("http://[::1") == (False, "illisible")


# --- v3b (8) : bornes du texte ajouté -------------------------------------------------------------------------------------

def test_bornes_des_sources_et_de_la_section(amont):
    url, _ = amont("--sources", "1000", "--requetes", "300", "--longueur-champs", "600")
    code, obj, _, _ = lancer_commande(V3C, url, "--recherche-web", "--max-requetes-web-pire-cas", "400",
                                      "--prix-requete-web-usd", "0.001")
    assert code == 0 and obj["requetes_web_facturees"] == 300  # le compte facturé n'est jamais coupé
    assert len(obj["requetes_web"]) == 50 and len(obj["sources_web"]) == 50
    assert all(len(q) <= 201 for q in obj["requetes_web"])
    assert all(len(s["titre"]) <= 201 and len(s["uri"]) <= 501 for s in obj["sources_web"])
    section = obj["texte"].split("Réponse factice d'Argon.", 1)[1]
    assert len(section) <= v3c.LONGUEUR_MAX_SECTION + 200 and "section coupée" in section
    assert any("section des sources coupée" in a for a in obj["avertissements"])
    assert any("950 source(s) au-delà" in a for a in obj["avertissements"])
    assert any("300 requêtes lues : 50 listées" in a for a in obj["avertissements"])


# --- non-conformités ----------------------------------------------------------------------------------------------------

def test_modele_servi_different_code_5(amont):
    url, _ = amont("--modele-servi", "gemini-9-autre")
    code, obj, _, _ = lancer_commande(V3C, url, "--recherche-web")
    assert code == 5 and obj["texte"] == "" and obj["cout_origine"] == "usage"
    assert "gemini-9-autre" in obj["erreur"]
    assert obj["cout_usd"] == pytest.approx(cout_jetons(obj) + 2 * 0.05, rel=1e-12)  # la recherche est comptée


def test_reponse_tronquee_et_bloquee_code_5(amont):
    url, _ = amont("--tronquee")
    code, obj, _, _ = lancer_commande(V3C, url, "--recherche-web")
    assert code == 5 and "MAX_TOKENS" in obj["erreur"]
    url, _ = amont("--refus", "bloque")
    code, obj, _, _ = lancer_commande(V3C, url, "--recherche-web")
    assert code == 5 and "bloquée" in obj["erreur"]


def test_refus_http_de_l_outil_code_3_sans_repli(amont):
    url, journal = amont("--refus", "http400")
    code, obj, _, _ = lancer_commande(V3C, url, "--recherche-web")
    assert code == 3 and obj["cout_origine"] == "plancher" and obj["cout_usd"] == 1e-6
    assert "google_search déclaré" in obj["erreur"] and "aucun repli" in obj["erreur"]
    assert len(corps_de(journal(), "generateContent")) == 1  # aucune relance


def test_reglages_refuses_code_2(amont):
    url, journal = amont()
    code, _, _, _ = lancer_commande(V3C, url, "--recherche-web", "--prix-requete-web-usd", "0")
    assert code == 2
    code, _, _, _ = lancer_commande(V3C, url, "--recherche-web", "--max-requetes-web-pire-cas", "0")
    assert code == 2
    code, _, _, _ = lancer_commande(V3C, url, "--recherche-web", "--provision-outil-jetons", "-1")
    assert code == 2
    assert journal() == []


# --- enveloppe v4d (réglages de la v4c) -----------------------------------------------------------------------------------------------

REGLAGES_FIGES = ["--prix-entree", "8.3", "--prix-sortie", "41.5", "--prix-requete-web-usd", "0.05",
                  "--max-requetes-web-pire-cas", "20", "--provision-outil-jetons", "32768",
                  "--url-base", "http://127.0.0.1:8788/v1beta"]
# réglages qu'un noyau (ou une consigne détournée) pourrait passer par "$@" pour desserrer la garde ; formes longue,
# avec « = » et abrégée (argparse accepte un préfixe sans ambiguïté)
REGLAGES_HOSTILES = ["--prix-entree", "0.001", "--prix-sortie=0.001", "--prix-e", "0.002", "--prix-requete-web-usd",
                     "0.0001", "--max-requetes-web-pire-cas", "1000", "--provision-outil-jetons", "0",
                     "--url-base", "https://ailleurs.example/v1beta"]


def _ligne_exec(chemin):
    """La commande lancée par `exec` (lignes de continuation jointes), découpée comme le ferait sh."""
    texte = open(chemin, encoding="utf-8").read().replace("\\\n", " ")
    ligne = next(x for x in texte.splitlines() if x.startswith("exec "))
    return shlex.split(ligne)


def _lancer_brut(script, argv, plafond="3"):
    env = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "PLAFOND_SESSION_USD": plafond, "ROLE_POLE": "proposeur_ideation",
           "GEMINI_API_KEY": CLE}
    r = subprocess.run([sys.executable, "-I", "-B", script, *argv], input=CONSIGNE.encode("utf-8"), capture_output=True,
                       env=env, timeout=60)
    return r.returncode, json.loads(r.stdout.decode("utf-8").strip().splitlines()[-1])


def test_enveloppe_v4d_reglages_figes_apres_les_arguments_du_noyau():
    """Mineur 4 : prix et bornes de la garde posés APRÈS "$@" ; avant lui, seul --delai-s."""
    mots = _ligne_exec(os.path.join(ICI, "appel-argon-v4d.sh"))
    assert mots[:7] == ["exec", "/usr/bin/timeout", "-k", "20", "1700", "/usr/bin/python3", "-I"]
    assert mots[7:9] == ["-B", "/opt/argon/commande_argon_v3d.py"]
    i = mots.index("$@")
    assert mots[9:i] == ["--delai-s", "1500"]
    assert mots[i + 1:] == REGLAGES_FIGES
    assert subprocess.run(["sh", "-n", os.path.join(ICI, "appel-argon-v4d.sh")]).returncode == 0


def test_enveloppe_v4d_la_derniere_occurrence_prime_analyseur_et_execution(amont):
    """La commande garde la dernière occurrence : sur l'analyseur, puis sur une exécution complète (même garde, même corps,
    même coût, avec ou sans réglages hostiles devant les réglages figés de l'enveloppe)."""
    mots = _ligne_exec(os.path.join(ICI, "appel-argon-v4d.sh"))
    figes = mots[mots.index("$@") + 1:]
    a = v3c.analyseur().parse_args(["--recherche-web", *REGLAGES_HOSTILES, *figes])
    assert (float(a.prix_entree), float(a.prix_sortie), float(a.prix_requete_web_usd)) == (8.3, 41.5, 0.05)
    assert (a.max_requetes_web_pire_cas, a.provision_outil_jetons) == (20, 32768)
    assert a.url_base == "http://127.0.0.1:8788/v1beta"
    url, journal = amont()
    figes_ici = [url if x == "http://127.0.0.1:8788/v1beta" else x for x in figes]
    c1, o1 = _lancer_brut(V3C, ["--recherche-web", *figes_ici])
    c2, o2 = _lancer_brut(V3C, ["--recherche-web", *REGLAGES_HOSTILES, *figes_ici])
    assert c1 == c2 == 0
    for champ in ("pire_cas_usd", "max_sortie_jetons", "cout_usd", "provision_outil_jetons", "prix_requete_web_usd",
                  "max_requetes_web_pire_cas", "entree_jetons_garde"):
        assert o1[champ] == o2[champ], champ
    assert o2["provision_outil_jetons"] == 32768 and o2["prix_requete_web_usd"] == 0.05
    g1, g2 = corps_de(journal(), "generateContent")
    assert g1 == g2  # aucune requête vers l'adresse hostile : les deux sont arrivées au faux amont
    # un réglage laissé sans valeur en fin de "$@" n'avale pas le réglage figé suivant : refus, rien envoyé
    c3, o3 = _lancer_brut(V3C, ["--recherche-web", "--modele", *figes_ici])
    assert c3 == 2 and o3["envoye"] is False and len(corps_de(journal(), "generateContent")) == 2


def test_enveloppe_v4d_ne_change_que_la_commande():
    """La v4d est la v4c (en-têtes, garde d'utilisateur, réglages, ordre) ; seul le nom de la commande lancée change."""
    v4c = open(os.path.join(ICI, "appel-argon-v4c.sh"), encoding="utf-8").read().splitlines()
    v4d = open(os.path.join(ICI, "appel-argon-v4d.sh"), encoding="utf-8").read().splitlines()
    assert v4d[0] == v4c[0] == "#!/bin/sh"
    assert all(x.startswith("# ") for x in v4d[1:5]) and v4d[5] == "# --- en-tête de la v4c, tel quel ---"
    assert v4d[6:-3] == v4c[1:-3]  # en-têtes et garde d'utilisateur repris tels quels
    assert v4d[-2:] == v4c[-2:]  # réglages figés après "$@", tels quels
    assert v4d[-3] == v4c[-3].replace("/opt/argon/commande_argon_v3c.py", "/opt/argon/commande_argon_v3d.py") != v4c[-3]


# --- v3c (1) : coût au-delà du plafond, entrée facturée au-delà de l'entrée gardée ------------------------------------------

CONSIGNE_420 = ("Propose une idée de moniteur. " * 60)[:1600]  # 400 jetons estimés et comptés, 420 gardés (marge 5 %)


def _bloquant(amont, *options_amont, options=("--recherche-web",), plafond="3"):
    url, _ = amont(*options_amont)
    return lancer_commande(V3C, url, *options, plafond=plafond, consigne=CONSIGNE_420)


def test_bloquant_1_scenario_exact_jamais_un_succes(amont):
    """Constat bloquant 1, scénario exact : entrée facturée 60 400 jetons pour 420 gardés, sortie maximale (pensées à la
    provision), 20 requêtes, 32 768 jetons d'outil, plafond 3 USD. La v3b rendait le code 0 et 3,4978 USD."""
    code, obj, _, erreurs = _bloquant(amont, "--entree-facturee", "60400", "--candidats-au-maximum", "--pensees", "8192",
                                      "--requetes", "20", "--usage-outil", "32768")
    assert obj["entree_jetons_garde"] == 420 and obj["max_sortie_jetons"] == 33363  # le scénario est bien celui-là
    assert obj["usage"]["candidats"] == 33363 and obj["usage"]["pensees"] == 8192 and obj["requetes_web_facturees"] == 20
    assert code != 0 and code == 9  # excédent 59 980 + 32 768 > 32 768 ; aucun succès
    assert obj["texte"] == "" and "Sources consultées" not in obj["texte"]
    assert obj["cout_origine"] == "usage" and obj["cout_usd"] == pytest.approx(3.4978269, abs=1e-6)  # coût réel rendu
    assert obj["entree_excedent_jetons"] == 59980 and obj["provision_outil_consommee_jetons"] == 59980 + 32768
    assert "59980" in obj["erreur"] and "(dépassé)" in obj["erreur"]
    assert any("> plafond de session 3 USD" in a for a in obj["avertissements"]) and "> plafond" in erreurs


def test_bloquant_1a_sans_recherche_cout_au_dela_du_plafond_code_10(amont):
    """(a) sans --recherche-web : la v2 et la v3b rendaient le code 0 (avertissement CL44-03) ; la v3c rend le code 10, même
    coût réel que la v2."""
    url, _ = amont("--entree-facturee", "400000")
    code2, obj2, _, _ = lancer_commande(V2, url, consigne=CONSIGNE_420)
    code, obj, _, _ = lancer_commande(V3C, url, consigne=CONSIGNE_420)
    assert code2 == 0  # le défaut, sur la commande installée
    assert code == 10 and obj["texte"] == "" and obj["cout_origine"] == "usage"
    assert obj["cout_usd"] == obj2["cout_usd"] > 3
    assert "coût au-delà du plafond de session" in obj["erreur"] and obj["entree_excedent_jetons"] == 400000 - 420
    assert obj["provision_outil_consommee_jetons"] is None  # sans recherche, aucune provision d'outil


def test_bloquant_1a_sans_recherche_excedent_sous_le_plafond_reste_un_avertissement(amont):
    """Cas sain (R5) : excédent d'entrée sans dépassement du plafond, sans recherche : comportement de la v2 (code 0)."""
    url, _ = amont("--entree-facturee", "1000")
    code2, obj2, _, _ = lancer_commande(V2, url, consigne=CONSIGNE_420)
    code, obj, _, _ = lancer_commande(V3C, url, consigne=CONSIGNE_420)
    assert code == code2 == 0 and obj["cout_usd"] == obj2["cout_usd"] and obj["texte"] == obj2["texte"]
    assert obj["avertissements"] == obj2["avertissements"] and len(obj["avertissements"]) == 1
    assert obj["entree_excedent_jetons"] == 580


def test_bloquant_1a_avec_recherche_sortie_au_dela_du_maximum_code_10(amont):
    """(a) avec --recherche-web, sans excédent d'entrée ni jetons d'outil : une sortie facturée au-delà de maxOutputTokens
    porte le coût au-delà du plafond ; la v3b rendait le code 0."""
    code, obj, _, _ = _bloquant(amont, "--candidats", "200000")
    assert code == 10 and obj["texte"] == "" and obj["cout_usd"] > 3 and obj["cout_origine"] == "usage"
    assert obj["provision_outil_consommee_jetons"] == 0


def test_bloquant_1a_code_10_prime_sur_le_code_5(amont):
    code, obj, _, _ = _bloquant(amont, "--candidats", "200000", "--modele-servi", "gemini-9-autre")
    assert code == 10


def test_bloquant_1b_excedent_compte_contre_la_provision_d_outil(amont):
    """(b) excédent + jetons d'outil = provision : succès sous le pire cas (cas sain) ; un jeton de plus : code 9."""
    code, obj, _, _ = _bloquant(amont, "--entree-facturee", "10420", "--usage-outil", "22768")
    assert code == 0 and obj["provision_outil_consommee_jetons"] == 32768
    assert obj["cout_usd"] <= obj["pire_cas_usd"] <= 3
    assert any("compté contre la provision d'outil" in a for a in obj["avertissements"])
    code, obj, _, _ = _bloquant(amont, "--entree-facturee", "10420", "--usage-outil", "22769")
    assert code == 9 and obj["texte"] == "" and obj["provision_outil_consommee_jetons"] == 32769
    assert "(dépassé)" not in obj["erreur"]  # la garde est franchie, le plafond pas encore : échec quand même


def test_bloquant_1_au_bord_exact_du_pire_cas_succes(amont):
    """Cas sain (R5) : tout au maximum permis (entrée = entrée gardée, sortie maximale, pensées et jetons d'outil à la
    provision, 20 requêtes) : coût = pire cas ≤ plafond, code 0 (la comparaison exacte ne refuse pas le bord)."""
    code, obj, _, _ = _bloquant(amont, "--entree-facturee", "420", "--candidats-au-maximum", "--pensees", "8192",
                                "--requetes", "20", "--usage-outil", "32768")
    assert code == 0, obj["erreur"]
    # pire_cas_usd est arrondi à 1e-6 ; le coût rendu ne l'est pas
    assert obj["cout_usd"] == pytest.approx(obj["pire_cas_usd"], abs=1e-6) and obj["cout_usd"] <= 3
    assert obj["provision_outil_consommee_jetons"] == 32768 and obj["entree_excedent_jetons"] == 0


# --- v3c (2) : webSearchQueries en partie illisible ------------------------------------------------------------------------

def test_mineur_2_trente_chaines_et_un_null_code_8(amont):
    url, _ = amont("--requetes", "30", "--requete-nulle")
    code, obj, _, _ = lancer_commande(V3C, url, "--recherche-web")  # maximum 20
    assert code == 8 and obj["texte"] == "" and obj["requetes_web_facturees"] == 31  # tout élément compte
    assert obj["requetes_web_origine"] == "maximum_pire_cas ou longueur (webSearchQueries en partie illisible)"
    assert len(obj["requetes_web"]) == 30 and obj["supplement_recherche_usd"] == pytest.approx(11 * 0.05)
    assert obj["cout_usd"] == pytest.approx(cout_jetons(obj) + 31 * 0.05, rel=1e-12)


def test_mineur_2_peu_de_chaines_et_un_null_jamais_moins_que_le_maximum(amont):
    url, _ = amont("--requetes", "2", "--requete-nulle")
    code, obj, _, _ = lancer_commande(V3C, url, "--recherche-web")
    assert code == 0 and obj["requetes_web_facturees"] == 20 and len(obj["requetes_web"]) == 2
    assert any("en partie illisible" in a for a in obj["avertissements"])


def test_mineur_2_lecture_unitaire():
    rep = {"candidates": [{"groundingMetadata": {"webSearchQueries": ["a", "", None, 3, "b"]}}]}
    r = v3c.lire_recherche(rep, 2, CLE)
    assert r["facturees"] == 5 and r["requetes"] == ["a", "b"]
    assert v3c.lire_recherche(rep, 20, CLE)["facturees"] == 20


# --- v3c (3) : jetons d'outil sans requête listée ------------------------------------------------------------------------

def test_mineur_3_jetons_d_outil_sans_requete_ni_source_comptent_une_recherche(amont):
    url, _ = amont("--grounding-vide", "--usage-outil", "500")
    code, obj, _, erreurs = lancer_commande(V3C, url, "--recherche-web")
    assert code == 0 and obj["requetes_web_facturees"] == 20 >= 1
    assert obj["requetes_web_origine"] == "maximum_pire_cas (requêtes vides, jetons d'outil facturés)"
    assert obj["cout_usd"] == pytest.approx(cout_jetons(obj) + 500 * PRIX_E / 1e6 + 20 * 0.05, rel=1e-12)
    assert "toolUsePromptTokenCount" in erreurs


@pytest.mark.parametrize("outil", [None, "0"])
def test_mineur_3_sans_jetons_d_outil_zero_requete(amont, outil):
    """Cas sain (R5) : groundingMetadata vide, jetons d'outil absents ou nuls : 0 requête, comme en v3b."""
    url, _ = amont("--grounding-vide", *(("--usage-outil", outil) if outil else ()))
    code, obj, _, _ = lancer_commande(V3C, url, "--recherche-web")
    assert code == 0 and obj["requetes_web_facturees"] == 0 and obj["requetes_web_origine"] == "webSearchQueries"


def test_mineur_3_temoin_outil_unitaire():
    assert v3c.temoin_outil({"toolUsePromptTokenCount": 7}) == 7
    assert [v3c.temoin_outil(u) for u in ({"toolUsePromptTokenCount": True}, {"toolUsePromptTokenCount": -1},
                                           {"toolUsePromptTokenCount": "9"}, {}, None)] == [0] * 5


# --- v3d (1) : totalTokenCount au-delà des jetons comptés (bloquant des deux relecteurs de la v3c) ------------------------
# Le faux amont v3 (inchangé) rend toujours totalTokenCount = somme : ces essais remplacent `poster` dans le processus et
# lancent `executer` avec les réglages figés de l'enveloppe v4d (lus dans le fichier), comme le scénario des relecteurs.

CONSIGNE_100 = b"x" * 400  # 100 jetons estimés et comptés, 105 gardés (marge 5 %)


def _figes_v4d():
    mots = _ligne_exec(os.path.join(ICI, "appel-argon-v4d.sh"))
    i = mots.index("$@")
    return mots[9:i] + mots[i + 1:]  # --delai-s 1500, puis prix, bornes de la garde et adresse (jamais contactée)


def _en_processus(monkeypatch, usage, recherche=True, servi="gemini-4-argon", plafond="3"):
    def faux_poster(_ouv, url, _cle, _corps, _delai):
        if url.endswith(":countTokens"):
            return {"totalTokens": 100}
        return {"candidates": [{"content": {"parts": [{"text": "Idée."}]}, "finishReason": "STOP",
                                "groundingMetadata": {"webSearchQueries": ["une requête"]}}],
                "usageMetadata": usage, "modelVersion": servi}
    monkeypatch.setattr(v3c, "poster", faux_poster)
    env = {"PLAFOND_SESSION_USD": plafond, "ROLE_POLE": "proposeur_ideation", "GEMINI_API_KEY": "factice-relais"}
    code, obj, _ = v3c.executer((["--recherche-web"] if recherche else []) + _figes_v4d(), CONSIGNE_100, env)
    return code, obj


def _cout_attendu(entree, sortie, ecart=0, outil=0, recherche=True):
    return (entree * PRIX_E + (sortie + ecart) * PRIX_S + outil * PRIX_E) / 1e6 + (0.05 if recherche else 0)


def test_v3d_1_scenario_exact_avec_recherche_jamais_un_succes(monkeypatch):
    """Scénario exact des relecteurs : prompt 105, candidats 10, total 2 000 000, plafond 3 USD, réglages figés ; la v3c
    rendait le code 0 et 0,0513 USD. L'écart (1 999 885) dépasse la provision d'outil : code 9, coût réel écart compris."""
    usage = {"promptTokenCount": 105, "candidatesTokenCount": 10, "totalTokenCount": 2_000_000}
    code, obj = _en_processus(monkeypatch, usage)
    assert code != 0 and code == 9 and obj["texte"] == "" and obj["cout_origine"] == "usage"
    assert obj["cout_usd"] == pytest.approx(_cout_attendu(105, 10, 1_999_885), rel=1e-12) and obj["cout_usd"] > 3
    assert obj["total_jetons"] == 2_000_000 and obj["ecart_total_jetons"] == 1_999_885
    assert obj["provision_outil_consommee_jetons"] == 1_999_885 and "écart de totalTokenCount 1999885" in obj["erreur"]
    assert "(dépassé)" in obj["erreur"] and any("usage incohérent" in a for a in obj["avertissements"])


def test_v3d_1_scenario_exact_sans_recherche_code_10(monkeypatch):
    """Même usage sans --recherche-web : la v3c rendait le code 0 et 0,0013 USD ; l'écart au prix de sortie porte le coût
    au-delà du plafond : code 10."""
    usage = {"promptTokenCount": 105, "candidatesTokenCount": 10, "totalTokenCount": 2_000_000}
    code, obj = _en_processus(monkeypatch, usage, recherche=False)
    assert code == 10 and obj["texte"] == "" and obj["cout_origine"] == "usage"
    assert obj["cout_usd"] == pytest.approx(_cout_attendu(105, 10, 1_999_885, recherche=False), rel=1e-12)
    assert obj["cout_usd"] > 80 and "écart de totalTokenCount 1999885" in obj["erreur"]
    assert obj["ecart_total_jetons"] == 1_999_885 and obj["provision_outil_consommee_jetons"] is None


@pytest.mark.parametrize("recherche", [True, False])
def test_v3d_1_petit_ecart_sous_le_plafond_et_la_provision_code_11(monkeypatch, recherche):
    """Écart de 100 jetons : ni le plafond ni la provision ne sont franchis ; échec nommé quand même (code 11), écart
    compté au prix de sortie."""
    usage = {"promptTokenCount": 105, "candidatesTokenCount": 10, "thoughtsTokenCount": 20, "totalTokenCount": 235}
    code, obj = _en_processus(monkeypatch, usage, recherche=recherche)
    assert code == 11 and obj["texte"] == "" and obj["cout_origine"] == "usage"
    assert obj["cout_usd"] == pytest.approx(_cout_attendu(105, 30, 100, recherche=recherche), rel=1e-12)
    assert obj["ecart_total_jetons"] == 100 and "usage incohérent" in obj["erreur"]
    assert obj["provision_outil_consommee_jetons"] == (100 if recherche else None)


def test_v3d_1_ecart_contre_la_provision_d_outil_code_9_sous_le_plafond(monkeypatch):
    """Avec la recherche, jetons d'outil + écart > provision, coût sous le plafond : code 9 (la garde ne tient plus)."""
    usage = {"promptTokenCount": 105, "candidatesTokenCount": 10, "toolUsePromptTokenCount": 30000,
             "totalTokenCount": 105 + 10 + 30000 + 2769}
    code, obj = _en_processus(monkeypatch, usage)
    assert code == 9 and obj["provision_outil_consommee_jetons"] == 32769 and obj["ecart_total_jetons"] == 2769
    assert obj["cout_usd"] == pytest.approx(_cout_attendu(105, 10, 2769, outil=30000), rel=1e-12) and obj["cout_usd"] < 3
    assert "(dépassé)" not in obj["erreur"]


def test_v3d_1_sans_recherche_jetons_d_outil_rendus_tombent_dans_l_ecart(monkeypatch):
    """Sans la recherche, toolUsePromptTokenCount n'est pas compté à part : inclus dans le total, il est compté par l'écart
    (prix de sortie) et nommé, jamais ignoré."""
    usage = {"promptTokenCount": 105, "candidatesTokenCount": 10, "toolUsePromptTokenCount": 500, "totalTokenCount": 615}
    code, obj = _en_processus(monkeypatch, usage, recherche=False)
    assert code == 11 and obj["ecart_total_jetons"] == 500
    assert obj["cout_usd"] == pytest.approx(_cout_attendu(105, 10, 500, recherche=False), rel=1e-12)


@pytest.mark.parametrize("total", ["2000000", True, -1, 1.5])
def test_v3d_1_total_mal_forme_usage_mal_forme_code_5(monkeypatch, total):
    usage = {"promptTokenCount": 105, "candidatesTokenCount": 10, "totalTokenCount": total}
    code, obj = _en_processus(monkeypatch, usage)
    assert code == 5 and obj["texte"] == "" and obj["cout_origine"] == "pire_cas"
    assert obj["cout_usd"] == obj["pire_cas_usd"] and "totalTokenCount" in obj["erreur"]


def test_v3d_1_ordre_pensees_puis_ecart_et_11_prime_sur_5(monkeypatch):
    usage = {"promptTokenCount": 105, "candidatesTokenCount": 10, "thoughtsTokenCount": 9000, "totalTokenCount": 9215}
    assert _en_processus(monkeypatch, usage)[0] == 7  # code 7 d'abord
    usage = {"promptTokenCount": 105, "candidatesTokenCount": 10, "totalTokenCount": 215}
    assert _en_processus(monkeypatch, usage, servi="gemini-9-autre")[0] == 11  # prime sur le code 5


# cas sains (R5) : passent sur la v3c comme sur la v3d (même code, même coût)

@pytest.mark.parametrize("recherche", [True, False])
def test_v3d_1_sain_total_egal_a_la_somme_succes(monkeypatch, recherche):
    outil = {"toolUsePromptTokenCount": 700} if recherche else {}
    usage = {"promptTokenCount": 105, "candidatesTokenCount": 10, "thoughtsTokenCount": 20, **outil,
             "totalTokenCount": 135 + (700 if recherche else 0)}
    code, obj = _en_processus(monkeypatch, usage, recherche=recherche)
    assert code == 0 and obj["texte"].startswith("Idée.") and obj["cout_origine"] == "usage"
    assert obj["cout_usd"] == pytest.approx(_cout_attendu(105, 30, outil=700 if recherche else 0, recherche=recherche),
                                            rel=1e-12)
    assert not any("totalTokenCount" in a for a in obj["avertissements"])


@pytest.mark.parametrize("total", [None, 100])
def test_v3d_1_sain_total_absent_ou_sous_la_somme_succes(monkeypatch, total):
    """Total absent (aucun écart lu) ou sous la somme (la somme des champs, plus grande, est comptée) : code 0."""
    usage = {"promptTokenCount": 105, "candidatesTokenCount": 10}
    if total is not None:
        usage["totalTokenCount"] = total
    code, obj = _en_processus(monkeypatch, usage)
    assert code == 0 and obj["cout_usd"] == pytest.approx(_cout_attendu(105, 10), rel=1e-12)


# --- v3e : MODELE_DEMANDE_POLE, le modèle demandé par le noyau (le seul changement de fond depuis la v3d) -------------------
# Le noyau pose la variable quand la commande est lancée avec `--commande-externe-lit-modele` ; la v3d ne la lisait pas.

ARGON, CARBON = "gemini-4-argon", "gemini-4-carbon"


def lancer_commande_env(script, url, variables, *options, plafond="3", consigne=CONSIGNE, cle=CLE):
    """`lancer_commande`, plus des variables d'environnement (MODELE_DEMANDE_POLE) ; jamais l'environnement de la session."""
    env = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "PLAFOND_SESSION_USD": plafond, "ROLE_POLE": "proposeur_ideation",
           "GEMINI_API_KEY": cle, **variables}
    r = subprocess.run([sys.executable, "-I", "-B", script, "--prix-entree", str(PRIX_E), "--prix-sortie", str(PRIX_S),
                        *options, "--url-base", url], input=consigne.encode("utf-8"), capture_output=True, env=env,
                       timeout=60)
    sortie = r.stdout.decode("utf-8")
    erreurs = r.stderr.decode("utf-8")
    objet = json.loads(sortie.strip().splitlines()[-1])
    return r.returncode, objet, sortie, erreurs


def _sans_version(objet):
    return {k: v for k, v in objet.items() if k != "version"}


# (a) différent : refus de réglage, rien envoyé

@pytest.mark.parametrize("demande, options", [(CARBON, ()), (ARGON, ("--modele", CARBON)), ("gemini-9-autre", ("--modele", ARGON)),
                                              ("", ()), (CARBON, ("--recherche-web",))])
def test_v3e_a_modele_demande_different_code_2_rien_envoye(amont, demande, options):
    url, journal = amont()
    code, obj, sortie, erreurs = lancer_commande_env(V3C, url, {"MODELE_DEMANDE_POLE": demande}, *options)
    attendu = options[options.index("--modele") + 1] if "--modele" in options else ARGON
    assert code == 2 and obj["envoye"] is False and obj["texte"] == ""
    assert obj["cout_usd"] == 1e-6 and obj["cout_origine"] == "plancher"
    assert "MODELE_DEMANDE_POLE" in obj["erreur"] and "rien envoyé" in obj["erreur"]
    assert repr(demande) in obj["erreur"] and repr(attendu) in obj["erreur"]  # les deux modèles sont nommés
    assert obj["modele_demande"] == attendu
    assert journal() == []  # aucun appel au faux amont : ni countTokens ni generateContent
    assert erreurs.startswith("commande_argon_v3e : ErreurCommande : MODELE_DEMANDE_POLE")
    assert len([l for l in sortie.splitlines() if l.strip()]) == 1


def test_v3e_a_contre_epreuve_la_v3d_ne_lit_pas_la_variable(amont):
    """Artefact (R5) : la même variable, différente de --modele, laisse la v3d envoyer et réussir (code 0) ; l'essai (a)
    discrimine donc bien la v3e de la v3d."""
    url, journal = amont()
    code_d, obj_d, _, _ = lancer_commande_env(V3D, url, {"MODELE_DEMANDE_POLE": CARBON})
    assert code_d == 0 and obj_d["envoye"] is True and obj_d["modele_demande"] == ARGON
    assert len(corps_de(journal(), "generateContent")) == 1
    code_e, obj_e, _, _ = lancer_commande_env(V3C, url, {"MODELE_DEMANDE_POLE": CARBON})
    assert code_e == 2 and obj_e["envoye"] is False
    assert len(corps_de(journal(), "generateContent")) == 1  # toujours un seul : la v3e n'a rien envoyé


def test_v3e_a_en_processus_poster_jamais_appele(monkeypatch):
    """Dans le processus : `poster` remplacé par un compteur ; le refus arrive avant tout appel, et n'est pas l'« erreur
    inattendue » qu'aurait produite un appel au faux."""
    appels = []

    def faux_poster(*a):
        appels.append(a)
        raise AssertionError("poster ne doit pas être appelé")
    monkeypatch.setattr(v3c, "poster", faux_poster)
    env = {"PLAFOND_SESSION_USD": "3", "ROLE_POLE": "proposeur_ideation", "GEMINI_API_KEY": "factice-relais",
           "MODELE_DEMANDE_POLE": CARBON}
    code, obj, erreur = v3c.executer(["--recherche-web"] + _figes_v4d(), CONSIGNE_100, env)
    assert code == 2 and appels == [] and obj["envoye"] is False and obj["cout_usd"] == 1e-6
    assert "inattendue" not in erreur and CARBON in erreur and ARGON in erreur
    # l'ordre : le modèle demandé est vérifié après ROLE_POLE et avant la clé
    env_sans_cle = {k: v for k, v in env.items() if k != "GEMINI_API_KEY"}
    code, obj, erreur = v3c.executer(_figes_v4d(), CONSIGNE_100, env_sans_cle)
    assert code == 2 and "MODELE_DEMANDE_POLE" in erreur and "GEMINI_API_KEY" not in erreur
    env_sans_role = {k: v for k, v in env.items() if k != "ROLE_POLE"}
    code, obj, erreur = v3c.executer(_figes_v4d(), CONSIGNE_100, env_sans_role)
    assert code == 2 and "ROLE_POLE" in erreur and "MODELE_DEMANDE_POLE" not in erreur


# (b) égal : comme la v3d

@pytest.mark.parametrize("modele, options", [(CARBON, ("--modele", CARBON)), (ARGON, ()), (CARBON, ("--modele", CARBON, "--recherche-web"))])
def test_v3e_b_modele_demande_egal_meme_comportement_que_la_v3d(amont, modele, options):
    url, journal = amont("--modele-servi", modele)
    variables = {"MODELE_DEMANDE_POLE": modele}
    code_d, obj_d, _, err_d = lancer_commande_env(V3D, url, variables, *options)
    code_e, obj_e, _, err_e = lancer_commande_env(V3C, url, variables, *options)
    assert code_d == code_e == 0, (obj_d.get("erreur"), obj_e.get("erreur"))
    assert obj_d["version"] == "commande-argon-v3d" and obj_e["version"] == "commande-argon-v3e"
    assert _sans_version(obj_e) == _sans_version(obj_d)  # même texte, même coût, même garde, même diagnostic
    assert obj_e["modele_demande"] == obj_e["modele_servi"] == modele and obj_e["envoye"] is True
    j = journal()
    chemins = [e["chemin"] for e in j]
    assert len(chemins) == 4 and chemins[:2] == chemins[2:]  # countTokens puis generateContent, deux fois, mêmes chemins
    assert all(f"/models/{modele}:" in c for c in chemins)
    assert corps_de(j, "generateContent")[0] == corps_de(j, "generateContent")[1]
    assert corps_de(j, "countTokens")[0] == corps_de(j, "countTokens")[1]
    assert err_e == err_d.replace("commande_argon_v3d :", "commande_argon_v3e :")


# (c) absente : identique à la v3d

@pytest.mark.parametrize("options_amont, options, code_attendu", [((), (), 0), ((), ("--recherche-web",), 0),
                                                                 (("--modele-servi", "gemini-9-autre"), ("--recherche-web",), 5),
                                                                 (("--refus", "http400"), ("--recherche-web",), 3)])
def test_v3e_c_variable_absente_identique_a_la_v3d(amont, options_amont, options, code_attendu):
    url, journal = amont(*options_amont)
    code_d, obj_d, _, err_d = lancer_commande_env(V3D, url, {}, *options)
    code_e, obj_e, _, err_e = lancer_commande_env(V3C, url, {}, *options)
    assert code_d == code_e == code_attendu
    assert _sans_version(obj_e) == _sans_version(obj_d)
    assert err_e == err_d.replace("commande_argon_v3d :", "commande_argon_v3e :")
    gen = corps_de(journal(), "generateContent")
    assert len(gen) == 2 and gen[0] == gen[1]


def test_v3e_c_variable_absente_en_processus_plafond_minuscule_code_4_comme_la_v3d(monkeypatch):
    """Cas de garde (code 4), sans la variable : la v3e refuse comme la v3d, avant tout appel."""
    appels = []
    monkeypatch.setattr(v3c, "poster", lambda *a: appels.append(a))
    env = {"PLAFOND_SESSION_USD": "0.01", "ROLE_POLE": "proposeur_ideation", "GEMINI_API_KEY": "factice-relais"}
    code, obj, _ = v3c.executer(["--sans-compter-jetons"] + _figes_v4d(), CONSIGNE_100, env)
    assert code == 4 and obj["envoye"] is False and appels == []


# (d) la source : un seul changement de fond

def test_v3e_d_source_ne_differe_de_la_v3d_que_par_l_en_tete_la_version_le_bloc_et_les_prefixes():
    d = open(V3D, encoding="utf-8").read().splitlines()
    e = open(V3C, encoding="utf-8").read().splitlines()
    ops = [op for op in difflib.SequenceMatcher(None, d, e, autojunk=False).get_opcodes() if op[0] != "equal"]
    assert len(ops) == 5, ops
    en_tete, version, bloc, prefixe_1, prefixe_2 = ops
    # 1. l'en-tête : la première ligne de la docstring de la v3d (ligne 2) remplacée par l'en-tête de la v3e, qui se termine
    #    par cette même ligne sans ses guillemets ; la docstring n'est pas fermée dans l'en-tête : la suite de celle de la v3d
    #    la continue, inchangée
    t, i1, i2, j1, j2 = en_tete
    assert t == "replace" and (i1, i2) == (1, 2) and d[0] == e[0] == "#!/usr/bin/env python3"
    assert d[1].startswith('"""Commande externe d\'Argon (gemini-4-argon) — version 3d')
    assert e[j1].startswith('"""Commande externe d\'Argon et de Carbon (gemini-4-argon, gemini-4-carbon) — version 3e')
    assert e[j2 - 1] == d[1][3:] and e[j2 - 3] == "## En-tête de la v3d (inchangé ci-dessous)"
    assert '"""' not in "\n".join(e[j1 + 1:j2]) and "MODELE_DEMANDE_POLE" in "\n".join(e[j1:j2])
    # 2. la constante VERSION
    t, i1, i2, j1, j2 = version
    assert t == "replace" and d[i1:i2] == ['VERSION = "commande-argon-v3d"'] and e[j1:j2] == ['VERSION = "commande-argon-v3e"']
    # 3. le bloc de trois lignes, inséré juste après la vérification de ROLE_POLE, avant la lecture de la clé
    t, i1, i2, j1, j2 = bloc
    assert t == "insert" and i1 == i2 and j2 - j1 == 3
    assert d[i1 - 1].strip().startswith("raise ErreurCommande(REGLAGE, f\"ROLE_POLE ∉")
    assert d[i1].strip().startswith("cle = environ.get(VARIABLE_CLE)")
    l1, l2, l3 = (x.strip() for x in e[j1:j2])
    assert l1.startswith('demande = environ.get("MODELE_DEMANDE_POLE")')
    assert l2 == "if demande is not None and demande != args.modele:"
    assert l3.startswith("raise ErreurCommande(REGLAGE,") and "MODELE_DEMANDE_POLE" in l3 and "rien envoyé" in l3
    assert all(x.startswith("        ") for x in e[j1:j2])  # même bloc `try` que les vérifications voisines
    # 4 et 5. les deux préfixes de la sortie d'erreur, et rien d'autre sur ces lignes
    for t, i1, i2, j1, j2 in (prefixe_1, prefixe_2):
        assert t == "replace" and i2 - i1 == 1 and j2 - j1 == 1
        assert e[j1] == d[i1].replace("commande_argon_v3d : ", "commande_argon_v3e : ") != d[i1]
        assert "file=sys.stderr" in e[j1]
    assert "avertissement" in e[prefixe_2[3]] and "avertissement" not in e[prefixe_1[3]]
    # rien d'autre : hors ces blocs, les deux fichiers sont identiques ligne à ligne
    assert len(e) == len(d) + 19 + 3
