"""Essais hors réseau de la course Kirchner Q2, v3 = `test_course_kirchner_v1.py` (gardé, R12) appliqué aux modules v2
(Kit Kirchner Q2, v1, dérivé à l'octet près des substitutions de nom du kit Heimersheim — branche outils/course-heimersheim-v1 — par un sous-agent de session-depot, 3 novembre 2026 ; les mentions de versions antérieures ci-dessous sont celles du kit Heimersheim.)
(course, lanceur Python), aux configurations v2 et au lanceur shell v3, plus les essais des corrections de la contre-lecture
(CLH-02, CLH-03, CLH-05, CLH-11) (sous-agent de session-depot, 3 novembre 2026) : chaque garde éprouvée sur
un cas sain et sur un artefact (R5). Aucun appel, aucune clé ; les commandes parlent à un port local fermé (rien ne part).

  env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 PYTHON -B -m pytest -q -p no:cacheprovider test_course_kirchner_v1.py
"""

import copy
import hashlib
import json
import os
import socket
import subprocess
import sys

import pytest

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
DEPOT = os.path.dirname(os.path.dirname(os.path.dirname(RACINE)))
sys.path.insert(0, RACINE)
sys.path.insert(0, ICI)

import course_kirchner_v1 as ch  # noqa: E402
import lancer_course_kirchner_v1 as L  # noqa: E402
import trace_agregee_course_kirchner_v1 as TR  # noqa: E402
from pole import configuration_v56 as cfg  # noqa: E402
from pole.configuration_v53 import ConfigurationRefusee  # noqa: E402
from pole.outils import ecrire_scelle, sha256_fichier  # noqa: E402

CONFS = {"sans_kimi": "configuration-course-kirchner-q2-v1-sans-kimi.json", "avec_kimi": "configuration-course-kirchner-q2-v1-avec-kimi.json",
         "cinq_especes": "configuration-course-kirchner-q2-v1-cinq-especes.json"}
PY = sys.executable
ENV = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "PYTHONDONTWRITEBYTECODE": "1"}
A1 = os.path.join(DEPOT, "docs", "notes", "ideation-organisme-v1", "commandes-a1-bis-v1")


def brut(v):
    with open(os.path.join(ICI, CONFS[v]), encoding="utf-8") as f:
        return json.load(f)


def lire(b):
    return cfg.lire_configuration_v56(b, base=ICI)


def port_ferme():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


# --- configuration (sain, puis un artefact par garde) ---------------------------------------------------------------------


@pytest.mark.parametrize("v", sorted(CONFS))
def test_configurations_saines(v):
    conf = lire(brut(v))
    r = ch.verifier_configuration_kirchner(conf)
    assert r["variante"] == v and r["bras"] == ["gu_krenn", "basique"] and r["k_paires"] >= 3


def refusee(b, motif):
    with pytest.raises(ConfigurationRefusee) as e:
        ch.verifier_configuration_kirchner(lire(b))
    assert motif in str(e.value), str(e.value)[:600]


def test_argon_hors_cinq_especes_refuse():
    b = brut("avec_kimi")
    c5 = brut("cinq_especes")
    b["fournisseurs"]["argon"] = c5["fournisseurs"]["argon"]
    refusee(b, "Argon (port 8805) hors de la variante cinq_especes")


def test_plafond_de_session_sous_le_pire_cas_refuse():
    b = brut("avec_kimi")
    b["plafonds_session"]["juge"] = 0.5
    refusee(b, "plafonds_session.juge")


def test_relais_kimi_au_dessus_de_5_refuse():
    b = brut("avec_kimi")
    b["relais"]["kimi"]["plafond_usd"] = 6.0
    refusee(b, "relais.kimi : plafond propre au plus 5")


def test_relais_argon_au_dessus_de_10_refuse():
    b = brut("cinq_especes")
    b["relais"]["argon"]["plafond_usd"] = 11.0
    refusee(b, "relais.argon : plafond propre au plus 10")


def test_etiquette_claude_refusee():
    b = brut("sans_kimi")
    b["etiquettes_interdites"].append("claude")
    refusee(b, "refusées (la pièce servie les cite)")


def test_etiquette_exigee_manquante_refusee():
    b = brut("sans_kimi")
    b["etiquettes_interdites"].remove("astra")
    refusee(b, "etiquettes_interdites : manquent")


def test_trois_paires_au_moins():
    b = brut("sans_kimi")
    b["bisociateur"]["k_paires"] = 2
    refusee(b, "k_paires")


def test_bras_meta_refuse():
    b = brut("sans_kimi")
    b["bisociateur"]["bras"] = ["gu_krenn", "basique", "meta"]
    with pytest.raises(ConfigurationRefusee):
        ch.verifier_configuration_kirchner(lire(b))


def test_reglages_claude_identiques_au_relais():
    b = brut("sans_kimi")
    c = b["fournisseurs"]["claude"]["commande"]
    c[c.index("--effort") + 1] = "medium"
    refusee(b, "réglages « --effort high --reflexion adaptative »")


def test_proposeurs_de_la_variante():
    b = brut("avec_kimi")
    b["proposeurs"] = b["proposeurs"][:3]
    refusee(b, "proposeurs")


def test_plafond_cumule_des_commandes_egal_a_s17():
    b = brut("sans_kimi")
    c = b["fournisseurs"]["astra"]["commande"]
    c[c.index("--plafond-cumule-usd") + 1] = "999"
    refusee(b, "--plafond-cumule-usd égal à S17")


def piece_mutee(tmp_path, b, nom, texte):
    p = tmp_path / os.path.basename(b["pieces"][nom]["chemin"])
    p.write_text(texte, encoding="utf-8")
    b["pieces"][nom] = {"chemin": str(p), "sha256": sha256_fichier(str(p))}
    for k in b["pieces"]:
        if not os.path.isabs(b["pieces"][k]["chemin"]):
            b["pieces"][k]["chemin"] = os.path.join(ICI, b["pieces"][k]["chemin"])
    s = b["bisociateur"]["gu_krenn"]["source"]
    if not os.path.isabs(s["chemin"]):
        s["chemin"] = os.path.join(ICI, s["chemin"])
    return b


def test_etiquette_interdite_dans_une_consigne_de_juge_refusee(tmp_path):
    b = brut("sans_kimi")
    t = open(os.path.join(ICI, b["pieces"]["consigne_juge"]["chemin"]), encoding="utf-8").read() + "\nUne fusion de deux idées.\n"
    refusee(piece_mutee(tmp_path, b, "consigne_juge", t), "pièce consigne_juge : étiquettes interdites présentes")


def test_consigne_proposeur_qui_n_enchasse_pas_la_piece_refusee(tmp_path):
    b = brut("sans_kimi")
    t = open(os.path.join(ICI, b["pieces"]["consigne_proposeur"]["chemin"]), encoding="utf-8").read()
    t = t.replace("Yudelson", "Yudelsson", 1)
    refusee(piece_mutee(tmp_path, b, "consigne_proposeur", t), "non enchâssées à l'octet")


def test_constructeur_de_consigne_conforme_et_artefact(tmp_path):
    cmd = [PY, "-I", "-B", os.path.join(ICI, "construire_consigne_proposeur_kirchner_v1.py"), "--verifier"]
    assert subprocess.run(cmd + [os.path.join(ICI, "pieces", "consigne-proposeur-kirchner-v1.md")], env=ENV).returncode == 0
    faux = tmp_path / "c.md"
    faux.write_bytes(open(os.path.join(ICI, "pieces", "consigne-proposeur-kirchner-v1.md"), "rb").read() + b" ")
    assert subprocess.run(cmd + [str(faux)], env=ENV, capture_output=True).returncode == 3


def test_aucune_etiquette_interdite_dans_la_question_ni_la_piece():
    b = brut("cinq_especes")
    conf = lire(b)
    from pole.fiches_v54 import trouver
    for nom in ("question_servie", "piece_kirchner", "piece_nos_resultats"):
        assert trouver(cfg.c53.texte_piece(conf, nom), conf["etiquettes_interdites"], "prefixe") == []
    # « témoin » et « argon » ne sont pas dans la liste : la pièce « nos résultats » les emploie (artefact qui le montre)
    assert trouver(cfg.c53.texte_piece(conf, "piece_nos_resultats"), ["témoin", "argon"], "prefixe") == ["argon", "témoin"]


# --- plafonds de session : par calcul et par un essai sur les vraies commandes ------------------------------------------------


def derniere_ligne(sortie):
    return json.loads([l for l in sortie.splitlines() if l.strip()][-1])


def appeler(commande, entree, plafond, modele, role="juge_ideation", registre=None):
    env = dict(ENV, PLAFOND_SESSION_USD=repr(float(plafond)), ROLE_POLE=role, MODELE_DEMANDE_POLE=modele)
    r = subprocess.run(commande, input=entree, env=env, capture_output=True, text=True, timeout=60)
    return r.returncode, derniere_ligne(r.stdout)


def commande_conf(v, f, tmp_path):
    conf = brut(v)
    reg = str(tmp_path / "registre.jsonl")
    c = L.commande_resolue(f, conf["fournisseurs"][f]["commande"], reg)
    c[c.index("--url-relais") + 1] = f"http://127.0.0.1:{port_ferme()}"
    return conf, c


def test_plafonds_de_session_au_dessus_du_pire_cas_par_calcul():
    for v in CONFS:
        conf = lire(brut(v))
        for r, (pire, modele) in ch.pire_cas_par_role(ch.longueurs_servies(conf), v).items():
            assert conf["plafonds_session"][r] > pire, (v, r, pire, modele)


def test_juge_astra_sortie_entiere_au_plafond_de_session(tmp_path):
    conf, c = commande_conf("avec_kimi", "astra", tmp_path)
    entree = open(os.path.join(ICI, "pieces", "consigne-juge-kirchner-v1.md"), encoding="utf-8").read() + "x" * ch.FICHE_MAX_CARACTERES
    code, o = appeler(c, entree, conf["plafonds_session"]["juge"], "gpt-6-astra")
    assert code == 3 and o["max_tokens"] == 16000 and o["envoye"] is False  # relais fermé : rien n'est parti
    code, o = appeler(c, entree, 0.1, "gpt-6-astra")
    assert code == 4 and o["envoye"] is False  # plafond trop bas : refus avant tout envoi


def test_proposeur_fable_sortie_entiere_au_plafond_de_session(tmp_path):
    conf, c = commande_conf("avec_kimi", "claude", tmp_path)
    entree = open(os.path.join(ICI, "pieces", "consigne-proposeur-kirchner-v1.md"), encoding="utf-8").read() + "\n## Case\n" + "x" * 150
    code, o = appeler(c, entree, conf["plafonds_session"]["proposeur"], "claude-fable-5-1", role="proposeur_ideation")
    assert code == 3 and o["max_tokens"] == 64000 and o["modele_demande"] == "claude-fable-5-1"
    entree2 = open(os.path.join(ICI, "pieces", "consigne-metteur-kirchner-v1.md"), encoding="utf-8").read() + "x" * (2 * ch.FICHE_MAX_CARACTERES)
    code, o = appeler(c, entree2, conf["plafonds_session"]["fusion"], "claude-fable-5-1", role="proposeur_ideation")
    assert code == 3 and o["max_tokens"] == 64000


# --- commande Claude de la course (aiguillage du modèle) -------------------------------------------------------------------


def test_commande_claude_modele_permis_et_artefacts(tmp_path):
    conf, c = commande_conf("sans_kimi", "claude", tmp_path)
    code, o = appeler(c, "Réponds seulement par le mot OK.", 0.05, "claude-opus-5-5")
    assert code == 3 and o["modele_demande"] == "claude-opus-5-5"  # sain : la commande A1-bis reçoit --modele opus
    code, o = appeler(c, "Réponds seulement par le mot OK.", 0.05, "claude-sonnet-5-5")
    assert code == 2 and o["envoye"] is False and "hors de" in o["erreur"]
    # claude-opus-4-6 est permis par la commande A1-bis : seul l'aiguillage de la course le refuse (contre-épreuve M4)
    code, o = appeler(c, "Réponds seulement par le mot OK.", 0.05, "claude-opus-4-6")
    assert code == 2 and o["envoye"] is False and o["version"] == "commande-claude-kirchner-v1"
    code, o = appeler(c + ["--modele", "claude-fable-5-1"], "x", 0.05, "claude-fable-5-1")
    assert code == 2 and o["envoye"] is False


def test_commande_claude_empreinte_a1bis_differente(monkeypatch, capsys):
    import commande_claude_kirchner_v1 as cc
    monkeypatch.setitem(cc.EMPREINTES, "commande_claude_a1bis_v1.py", "0" * 64)
    assert cc.principal(["--url-relais", "http://127.0.0.1:9"], environ={"MODELE_DEMANDE_POLE": "claude-opus-5-5"}) == 2
    assert "empreinte" in json.loads(capsys.readouterr().out.splitlines()[-1])["erreur"]


# --- lanceur Python : GO et pièces gelées ------------------------------------------------------------------------------------


def registre(tmp_path, montant=None, ident="GO-2026-11-03-98"):
    montant = montant or "%g USD" % brut("cinq_especes")["budget"]["plafond_usd"]
    p = tmp_path / "go.md"
    p.write_text("# Registre (essai)\n\n| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n"
                 "|---|---|---|---|---|---|---|---|\n"
                 f"| {ident} | 2026-11-03 | calcul | essai | {montant} | 2026-11-30 | Lazar | essai |\n", encoding="utf-8")
    return str(p)


def args_verifier(tmp_path, reg, attendu="GO-2026-11-03-98", fiche=None, cl=None):
    a = ["verifier", "--configuration", os.path.join(ICI, CONFS["avec_kimi"]), "--registre-go", reg, "--go-attendu", attendu]
    if fiche:
        a += ["--preenregistrement", fiche, "--contre-lecture", cl]
    return a


def test_go_sain_et_artefacts(tmp_path, capsys):
    reg = registre(tmp_path)
    assert L.principal(args_verifier(tmp_path, reg), environnement={"GO_ID": "GO-2026-11-03-98"}) == 0
    assert L.principal(args_verifier(tmp_path, reg), environnement={"GO_ID": "GO-2026-11-03-97"}) == 2   # GO_ID ≠ attendu
    d = tmp_path / "b"
    d.mkdir()
    reg2 = registre(d, montant="60 USD")
    assert L.principal(args_verifier(tmp_path, reg2), environnement={"GO_ID": "GO-2026-11-03-98"}) == 2  # montant ≠ S17
    assert "pas exactement le plafond requis" in capsys.readouterr().err


def fiche(tmp_path, retirer=None):
    d = tmp_path / "spec"
    d.mkdir(exist_ok=True)
    cl = str(d / "cl.md")
    if not os.path.exists(cl):
        ecrire_scelle(cl, "Contre-lecture d'essai.\n")
    import table_pieces_gelees_kirchner_v1 as T
    lignes = [l for l in T.lignes() if not (retirer and retirer in l)]
    p = str(d / f"fiche-{'sans-' + os.path.basename(retirer) if retirer else 'saine'}.md")
    ecrire_scelle(p, "# Fiche d'essai\n\nContre-lecture : " + sha256_fichier(cl) + "\n\n### Pièces gelées\n\n| a | b | c |\n|---|---|---|\n"
                  + "\n".join(lignes) + "\n\n## Fin\n")
    return p, cl


def test_pieces_gelees_saines_et_artefacts(tmp_path, capsys):
    reg = registre(tmp_path)
    p, cl = fiche(tmp_path)
    assert L.principal(args_verifier(tmp_path, reg, fiche=p, cl=cl), environnement={"GO_ID": "GO-2026-11-03-98"}) == 0
    p2, _ = fiche(tmp_path, retirer=".claude/hooks/garde_calcul.py")
    assert L.principal(args_verifier(tmp_path, reg, fiche=p2, cl=cl), environnement={"GO_ID": "GO-2026-11-03-98"}) == 2
    assert "pièces non gelées" in capsys.readouterr().err
    texte = open(p, encoding="utf-8").read()
    sha_conf = sha256_fichier(os.path.join(ICI, CONFS["avec_kimi"]))
    p3 = str(tmp_path / "spec" / "fiche-fausse.md")
    ecrire_scelle(p3, texte.replace(sha_conf, "0" * 64))
    assert L.principal(args_verifier(tmp_path, reg, fiche=p3, cl=cl), environnement={"GO_ID": "GO-2026-11-03-98"}) == 2
    assert "pièce gelée modifiée" in capsys.readouterr().err


# --- lanceur shell : refus avant tout relais -----------------------------------------------------------------------------------


def shell(*args, **env):
    e = dict(ENV, GO_ID="GO-2026-11-03-98", PY_RELAIS_CLAUDE=PY, **env)
    return subprocess.run(["bash", os.path.join(ICI, "lancer-course-kirchner-v1.sh")] + list(args), env=e, capture_output=True,
                          text=True, timeout=60)


def test_shell_refus_avant_tout_relais(tmp_path):
    c = CONFS["avec_kimi"]
    r = shell("lancer", "GO-2026-11-03-97", c, str(tmp_path / "run"), "p", "c")
    assert r.returncode == 2 and "ne court que sous" in r.stderr and not (tmp_path / "run").exists()
    r = shell("lancer", "GO-2026-11-03-98", "configuration-inconnue.json", str(tmp_path / "run"), "p", "c")
    assert r.returncode == 2 and not (tmp_path / "run").exists()
    r = shell("lancer", "GO-2026-11-03-98", c, str(tmp_path / "run"), "p", "c", REGISTRE_GO=registre(tmp_path))
    assert r.returncode == 2 and "permis qu'en répétition" in r.stderr
    dedans = os.path.join(DEPOT, "run-essai-interdit")
    r = shell("repeter", "GO-2026-11-03-98", c, dedans, "p", "c", SSL_CERT_FILE="/nulle-part/ca.pem")
    assert r.returncode == 2 and not os.path.exists(dedans)


def test_shell_reglages_claude_identiques_a_la_configuration():
    t = open(os.path.join(ICI, "lancer-course-kirchner-v1.sh"), encoding="utf-8").read()
    assert "--modeles-permis claude-fable-5-1,claude-opus-5-5 --effort high --reflexion adaptative" in t
    for v in CONFS:
        c = brut(v)["fournisseurs"]["claude"]["commande"]
        assert c[c.index("--effort") + 1] == "high" and c[c.index("--reflexion") + 1] == "adaptative"


# --- devis ---------------------------------------------------------------------------------------------------------------------


def test_devis_parts_kimi_argon_et_plafond_technique():
    d = json.load(open(os.path.join(ICI, "devis-course-kirchner-v1.json"), encoding="utf-8"))
    pire_max = max(x["total_pire_cas_usd"] for x in d["variantes"].values())
    assert d["plafond_technique_usd"] == max(60, int(1.2 * pire_max) + 1)
    for v, x in d["variantes"].items():
        f = x["par_fournisseur"]
        if "kimi" in f:
            assert f["kimi"]["pire_cas_usd"] < d["relais"][v]["kimi"]["plafond_usd"] <= 5
        if "argon" in f:
            assert f["argon"]["pire_cas_usd"] < d["relais"][v]["argon"]["plafond_usd"] <= 10
        assert sum(r["plafond_usd"] for r in d["relais"][v].values()) <= d["plafond_technique_usd"] + 1e-9
        assert brut(v)["budget"]["plafond_usd"] == d["plafond_technique_usd"]
        assert brut(v)["relais"] == d["relais"][v]


# --- trace agrégée : garde anti-fuite --------------------------------------------------------------------------------------------


def test_garde_anti_fuite_saine_et_artefacts():
    g = TR.tester_garde()
    assert g["cas_sain"] is True and g["artefacts"] == [True, True, True]
    fiche_ = {"titre": "Titre assez long pour compter", "hypothese": "un deux trois quatre cinq six sept"}
    assert TR.controle_anti_fuite({"fin": "aucun"}, ["KQ2-X"], [fiche_], [fiche_["titre"]])["resultat"] == "conforme"
    assert TR.controle_anti_fuite({"fin": "Titre assez long pour compter"}, ["KQ2-X"], [fiche_], [fiche_["titre"]])["resultat"] == "refuse"


def test_liste_blanche_refuse_un_texte_libre():
    conf = brut("avec_kimi")
    with pytest.raises(ValueError):
        TR.valider_liste_blanche({"fin": "une phrase de fiche recopiée avec des espaces"}, TR.permises_de(conf))
    TR.valider_liste_blanche({"fin": "fini", "par_modele": {"gpt-6-astra": 3}}, TR.permises_de(conf))




# --- corrections de la contre-lecture (CLH-02, CLH-03, CLH-05, CLH-11) ---------------------------------------------------------


def test_clh03_gpt_6_attrape_les_autres_gpt_passent():
    from pole.fiches_v54 import trouver
    conf = lire(brut("cinq_especes"))
    i = conf["etiquettes_interdites"]
    assert "gpt" not in i and {"gpt 6", "gpt6", "gpt-6", "chatgpt"} <= set(i)
    for ok in ("comme sur GPT-2 small", "GPT-J", "GPT-4", "un banc GPT-2 medium"):
        assert trouver(ok, i, "prefixe") == [], ok
    for ko in ("gpt-6-astra", "GPT-6", "gpt6", "ChatGPT"):
        assert trouver(ko, i, "prefixe"), ko


def test_clh03_artefact_gpt_seul_refuse():
    b = brut("sans_kimi")
    b["etiquettes_interdites"].append("gpt")
    refusee(b, "refusées (la pièce servie les cite)")


def test_source_gu_krenn_tiree_des_textes_servis():
    src = json.load(open(os.path.join(ICI, "pieces", "source-gu-krenn-kirchner-v1.json"), encoding="utf-8"))
    liste = json.load(open(os.path.join(ICI, "pieces", "concepts-kirchner-v1.json"), encoding="utf-8"))
    assert all(set(o["concepts"]) <= set(liste) and o["section_piece"] for o in src["oeuvres"])
    conf = lire(brut("avec_kimi"))
    from pole.bisociateur_v53 import SourceGuKrenn
    g = conf["bisociateur"]["gu_krenn"]
    s_ = SourceGuKrenn(os.path.join(ICI, g["source"]["chemin"]), g["source"]["sha256"], oeuvres_min_vocabulaire=1,
                       date_debut=g["date_debut"], date_coupure=g["date_coupure"], actif_depuis=g["actif_depuis"], actif_min_oeuvres=1)
    assert "rappel du moniteur" not in s_.vocabulaire  # aucune source ne le porte
    assert ("moniteur du même modèle", "sélection par classement") not in s_.reliees  # lien qu'aucune source ne fait
    assert ("banc tenu à l'écart", "moniteur du même modèle") in s_.reliees  # lien de 2608.28945 (pièce Kirchner §2)


def test_consignes_aiguilleur_lecteur_juge():
    a = open(os.path.join(ICI, "pieces", "consigne-aiguilleur-kirchner-v1.md"), encoding="utf-8").read()
    assert "ne correspond pas à son contenu" not in a and "En cas de doute entre `niveau_methode` et `concret`, choisis `concret`." in a
    assert "détails opérationnels qui serviraient à tromper un moniteur ou une évaluation ou à masquer un comportement" in a
    l = open(os.path.join(ICI, "pieces", "consigne-lecteur-kirchner-v1.md"), encoding="utf-8").read()
    assert "`premiere_experience`" in l and "`changer_d_avis`" in l
    j_ = open(os.path.join(ICI, "pieces", "consigne-juge-kirchner-v1.md"), encoding="utf-8").read()
    q = open(os.path.join(ICI, "pieces", "conv-audit", "question-ideation-kirchner-v1.md"), encoding="utf-8").read()
    deja = q[q.index("## Ce qui est déjà pris"):q.index("## Règles d'intégrité")].rstrip() + "\n"
    assert deja in j_ and all(f"**K{n}**" in j_ for n in range(1, 6))


_ = (copy, hashlib)
