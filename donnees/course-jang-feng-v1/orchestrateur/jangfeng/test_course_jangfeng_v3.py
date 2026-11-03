"""(ESSAIS JANG-FENG v2, sous-agent de session-depot, 3 novembre 2026 : test_course_jangfeng_v3.py, gardé, R12, appliqué aux
# KIT JANGFENG v3 (sous-agent de session-depot, 3 novembre 2026) : v2 (gardée, R12) plus la variante « sans-claude » (proposeurs Argon, Kimi, Astra ; aiguilleur Astra ; juges Astra et Argon ; lecteurs Astra et Argon ; metteur Astra ; aucun rôle Claude ; relais 8806 non démarré, contrôle de Claude non joué) ; S17 propre à cette variante ; les configurations existantes ne sont ni réécrites ni changées.
# KIT JANG-FENG v2 (sous-agent de session-depot, 3 novembre 2026) : v1 (gardée, R12) plus deux variantes sans Opus (« sans-opus », « sans-opus-argon » : Fable 5.1 aiguilleur, juge et lecteur), contre-lecture CLJ-01 ; les trois configurations v1 restent inchangées ; S17 par variante (198, ou 237 pour « sans-opus-argon »).
KIT JANG-FENG, v1 (sous-agent de session-depot, 3 novembre 2026) : dérivé du kit Ibrahim v2 (outils/course-ibrahim-q1-v1, 965eb21b) par substitution de noms et par les changements de la course Jang-Feng (question à une section servie et ses règles d'intégrité, deux pièces servies, trois variantes comme Ibrahim, juge du n° 419, marge d'appels 2 × plan + 5).
configurations Jang-Feng q1-v2, au lanceur shell v2, à la table v2 et à la source Gu-Krenn v2, plus les essais des corrections
CLI-01 (max_appels = 2 × plan + 5, plafonds en dollars inchangés, borne des fiches en trop) et CLI-02 (source v2).
Les lignes suivantes sont héritées.)
(v2 = test_course_jangfeng_v3.py, gardé, R12, appliqué aux configurations v2, au lanceur shell v2 et à la table v2, avec
les essais des corrections CLK-01 et CLK-02.)
Essais hors réseau de la course Jang-Feng, v3 = `test_course_jangfeng_v3.py` (gardé, R12) appliqué aux modules v2
(course, lanceur Python), aux configurations v2 et au lanceur shell v3, plus les essais des corrections de la contre-lecture
(CLH-02, CLH-03, CLH-05, CLH-11) (sous-agent de session-depot, 3 novembre 2026) : chaque garde éprouvée sur
un cas sain et sur un artefact (R5). Aucun appel, aucune clé ; les commandes parlent à un port local fermé (rien ne part).

  env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 PYTHON -B -m pytest -q -p no:cacheprovider test_course_jangfeng_v3.py
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

import course_jangfeng_v3 as ch  # noqa: E402
import lancer_course_jangfeng_v3 as L  # noqa: E402
import trace_agregee_course_jangfeng_v1 as TR  # noqa: E402
from pole import configuration_v56 as cfg  # noqa: E402
from pole.configuration_v53 import ConfigurationRefusee  # noqa: E402
from pole.outils import ecrire_scelle, sha256_fichier  # noqa: E402

import calcul_devis_course_jangfeng_v3 as DV  # noqa: E402

CONFS = DV.NOMS
V_KIMI, V_ARGON, V_BASE = 'avec_kimi', 'cinq_especes', 'sans_kimi'  # variante avec Kimi sans Argon ; avec Argon ; la plus petite
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
    r = ch.verifier_configuration_jangfeng(conf)
    assert r["variante"] == v and r["bras"] == ["gu_krenn", "basique"] and r["k_paires"] >= 3


def refusee(b, motif):
    with pytest.raises(ConfigurationRefusee) as e:
        ch.verifier_configuration_jangfeng(lire(b))
    assert motif in str(e.value), str(e.value)[:600]


def test_argon_hors_cinq_especes_refuse():
    b = brut(V_KIMI)
    c5 = brut(V_ARGON)
    b["fournisseurs"]["argon"] = c5["fournisseurs"]["argon"]
    refusee(b, "Argon (port 8805) hors des variantes")


def test_plafond_de_session_sous_le_pire_cas_refuse():
    b = brut(V_KIMI)
    b["plafonds_session"]["juge"] = 0.5
    refusee(b, "plafonds_session.juge")


def test_relais_kimi_au_dessus_de_5_refuse():
    b = brut(V_KIMI)
    b["relais"]["kimi"]["plafond_usd"] = 6.0
    refusee(b, "relais.kimi : plafond propre au plus 5")


def test_relais_argon_au_dessus_de_10_refuse():
    b = brut(V_ARGON)
    b["relais"]["argon"]["plafond_usd"] = 11.0
    refusee(b, "relais.argon : plafond propre au plus 10")


def test_etiquette_claude_refusee():
    b = brut(V_BASE)
    b["etiquettes_interdites"].append("claude")
    refusee(b, "refusées (la pièce servie les cite)")


def test_etiquette_exigee_manquante_refusee():
    b = brut(V_BASE)
    b["etiquettes_interdites"].remove("astra")
    refusee(b, "etiquettes_interdites : manquent")


def test_trois_paires_au_moins():
    b = brut(V_BASE)
    b["bisociateur"]["k_paires"] = 2
    refusee(b, "k_paires")


def test_bras_meta_refuse():
    b = brut(V_BASE)
    b["bisociateur"]["bras"] = ["gu_krenn", "basique", "meta"]
    with pytest.raises(ConfigurationRefusee):
        ch.verifier_configuration_jangfeng(lire(b))


def test_reglages_claude_identiques_au_relais():
    b = brut(V_BASE)
    c = b["fournisseurs"]["claude"]["commande"]
    c[c.index("--effort") + 1] = "medium"
    refusee(b, "réglages « --effort high --reflexion adaptative »")


def test_proposeurs_de_la_variante():
    b = brut(V_KIMI)
    b["proposeurs"] = b["proposeurs"][:-1]
    refusee(b, "proposeurs")


def test_plafond_cumule_des_commandes_egal_a_s17():
    b = brut(V_BASE)
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
    b = brut(V_BASE)
    t = open(os.path.join(ICI, b["pieces"]["consigne_juge"]["chemin"]), encoding="utf-8").read() + "\nUne idée venue de Kimi.\n"
    refusee(piece_mutee(tmp_path, b, "consigne_juge", t), "pièce consigne_juge : étiquettes interdites présentes")


def test_consigne_proposeur_qui_n_enchasse_pas_la_piece_refusee(tmp_path):
    b = brut(V_BASE)
    t = open(os.path.join(ICI, b["pieces"]["consigne_proposeur"]["chemin"]), encoding="utf-8").read()
    t = t.replace('Moodley', 'Moodleya', 1)
    refusee(piece_mutee(tmp_path, b, "consigne_proposeur", t), "non enchâssées à l'octet")


def test_constructeur_de_consigne_conforme_et_artefact(tmp_path):
    cmd = [PY, "-I", "-B", os.path.join(ICI, "construire_consigne_proposeur_jangfeng_v1.py"), "--verifier"]
    assert subprocess.run(cmd + [os.path.join(ICI, "pieces", "consigne-proposeur-jangfeng-v1.md")], env=ENV).returncode == 0
    faux = tmp_path / "c.md"
    faux.write_bytes(open(os.path.join(ICI, "pieces", "consigne-proposeur-jangfeng-v1.md"), "rb").read() + b" ")
    assert subprocess.run(cmd + [str(faux)], env=ENV, capture_output=True).returncode == 3


def test_aucune_etiquette_interdite_dans_la_question_ni_la_piece():
    b = brut(V_ARGON)
    conf = lire(b)
    from pole.fiches_v54 import trouver
    for nom in ("question_servie", *ch.PIECES_SERVIES):
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
    conf, c = commande_conf(V_KIMI, "astra", tmp_path)
    entree = open(os.path.join(ICI, "pieces", "consigne-juge-jangfeng-v1.md"), encoding="utf-8").read() + "x" * ch.FICHE_MAX_CARACTERES
    code, o = appeler(c, entree, conf["plafonds_session"]["juge"], "gpt-6-astra")
    assert code == 3 and o["max_tokens"] == 16000 and o["envoye"] is False  # relais fermé : rien n'est parti
    code, o = appeler(c, entree, 0.1, "gpt-6-astra")
    assert code == 4 and o["envoye"] is False  # plafond trop bas : refus avant tout envoi


def test_proposeur_fable_sortie_entiere_au_plafond_de_session(tmp_path):
    conf, c = commande_conf(V_KIMI, "claude", tmp_path)
    entree = open(os.path.join(ICI, "pieces", "consigne-proposeur-jangfeng-v1.md"), encoding="utf-8").read() + "\n## Case\n" + "x" * 150
    code, o = appeler(c, entree, conf["plafonds_session"]["proposeur"], "claude-fable-5-1", role="proposeur_ideation")
    assert code == 3 and o["max_tokens"] == 64000 and o["modele_demande"] == "claude-fable-5-1"
    entree2 = open(os.path.join(ICI, "pieces", "consigne-metteur-jangfeng-v1.md"), encoding="utf-8").read() + "x" * (2 * ch.FICHE_MAX_CARACTERES)
    code, o = appeler(c, entree2, conf["plafonds_session"]["fusion"], "claude-fable-5-1", role="proposeur_ideation")
    assert code == 3 and o["max_tokens"] == 64000


# --- commande Claude de la course (aiguillage du modèle) -------------------------------------------------------------------


def test_commande_claude_modele_permis_et_artefacts(tmp_path):
    conf, c = commande_conf(V_BASE, "claude", tmp_path)
    code, o = appeler(c, "Réponds seulement par le mot OK.", 0.05, "claude-opus-5-5")
    assert code == 3 and o["modele_demande"] == "claude-opus-5-5"  # sain : la commande A1-bis reçoit --modele opus
    code, o = appeler(c, "Réponds seulement par le mot OK.", 0.05, "claude-sonnet-5-5")
    assert code == 2 and o["envoye"] is False and "hors de" in o["erreur"]
    # claude-opus-4-6 est permis par la commande A1-bis : seul l'aiguillage de la course le refuse (contre-épreuve M4)
    code, o = appeler(c, "Réponds seulement par le mot OK.", 0.05, "claude-opus-4-6")
    assert code == 2 and o["envoye"] is False and o["version"] == "commande-claude-jangfeng-v1"
    code, o = appeler(c + ["--modele", "claude-fable-5-1"], "x", 0.05, "claude-fable-5-1")
    assert code == 2 and o["envoye"] is False


def test_commande_claude_empreinte_a1bis_differente(monkeypatch, capsys):
    import commande_claude_jangfeng_v1 as cc
    monkeypatch.setitem(cc.EMPREINTES, "commande_claude_a1bis_v1.py", "0" * 64)
    assert cc.principal(["--url-relais", "http://127.0.0.1:9"], environ={"MODELE_DEMANDE_POLE": "claude-opus-5-5"}) == 2
    assert "empreinte" in json.loads(capsys.readouterr().out.splitlines()[-1])["erreur"]


# --- lanceur Python : GO et pièces gelées ------------------------------------------------------------------------------------


def registre(tmp_path, montant=None, ident="GO-2026-11-03-98"):
    montant = montant or "%g USD" % brut(V_KIMI)["budget"]["plafond_usd"]
    p = tmp_path / "go.md"
    p.write_text("# Registre (essai)\n\n| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n"
                 "|---|---|---|---|---|---|---|---|\n"
                 f"| {ident} | 2026-11-03 | calcul | essai | {montant} | 2026-11-30 | Lazar | essai |\n", encoding="utf-8")
    return str(p)


def args_verifier(tmp_path, reg, attendu="GO-2026-11-03-98", fiche=None, cl=None):
    a = ["verifier", "--configuration", os.path.join(ICI, CONFS[V_KIMI]), "--registre-go", reg, "--go-attendu", attendu]
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
    import table_pieces_gelees_jangfeng_v3 as T
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
    sha_conf = sha256_fichier(os.path.join(ICI, CONFS[V_KIMI]))
    p3 = str(tmp_path / "spec" / "fiche-fausse.md")
    ecrire_scelle(p3, texte.replace(sha_conf, "0" * 64))
    assert L.principal(args_verifier(tmp_path, reg, fiche=p3, cl=cl), environnement={"GO_ID": "GO-2026-11-03-98"}) == 2
    assert "pièce gelée modifiée" in capsys.readouterr().err


# --- lanceur shell : refus avant tout relais -----------------------------------------------------------------------------------


def shell(*args, **env):
    e = dict(ENV, GO_ID="GO-2026-11-03-98", PY_RELAIS_CLAUDE=PY, **env)
    return subprocess.run(["bash", os.path.join(ICI, "lancer-course-jangfeng-v3.sh")] + list(args), env=e, capture_output=True,
                          text=True, timeout=60)


def test_shell_refus_avant_tout_relais(tmp_path):
    c = CONFS[V_KIMI]
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
    t = open(os.path.join(ICI, "lancer-course-jangfeng-v3.sh"), encoding="utf-8").read()
    assert "--modeles-permis claude-fable-5-1,claude-opus-5-5 --effort high --reflexion adaptative" in t
    for v in CONFS:
        if "claude" not in brut(v)["fournisseurs"]:
            continue  # sans-claude : aucune commande Claude
        c = brut(v)["fournisseurs"]["claude"]["commande"]
        assert c[c.index("--effort") + 1] == "high" and c[c.index("--reflexion") + 1] == "adaptative"


# --- devis ---------------------------------------------------------------------------------------------------------------------


def test_devis_parts_kimi_argon_et_plafond_technique():
    d = json.load(open(os.path.join(ICI, "devis-course-jangfeng-v3.json"), encoding="utf-8"))
    pire_max = max(x["total_pire_cas_usd"] for x in d["variantes"].values())
    assert d["s17_par_variante"] == {v: max(198, int(1.2 * x["total_pire_cas_usd"]) + 1) for v, x in d["variantes"].items()}
    assert d["s17_par_variante"]["sans_opus_argon"] == 237 and "sans_claude" in d["s17_par_variante"] and d["go_par_variante"]["sans_opus_argon"] == "GO-2026-11-03-13"
    assert all(d["go_par_variante"][v] == "GO-2026-11-03-12" for v in d["variantes"] if v not in ("sans_opus_argon", "sans_claude"))
    for v, x in d["variantes"].items():
        f = x["par_fournisseur"]
        if "kimi" in f:
            assert f["kimi"]["pire_cas_usd"] < d["relais"][v]["kimi"]["plafond_usd"] <= 5
        if "argon" in f:
            assert f["argon"]["pire_cas_usd"] < d["relais"][v]["argon"]["plafond_usd"] <= ch.plafond_relais_max(v).get("argon", 1e9)
        assert sum(r["plafond_usd"] for r in d["relais"][v].values()) <= d["s17_par_variante"][v] + 1e-9
        assert brut(v)["budget"]["plafond_usd"] == d["s17_par_variante"][v]
        # v2 (CLI-01) : seul max_appels change (2 × plan + 5), essayé plus bas
        assert {f: {k: x for k, x in r.items() if k != "max_appels"} for f, r in brut(v)["relais"].items()} == \
            {f: {k: x for k, x in r.items() if k != "max_appels"} for f, r in d["relais"][v].items()}


# --- trace agrégée : garde anti-fuite --------------------------------------------------------------------------------------------


def test_garde_anti_fuite_saine_et_artefacts():
    g = TR.tester_garde()
    assert g["cas_sain"] is True and g["artefacts"] == [True, True, True]
    fiche_ = {"titre": "Titre assez long pour compter", "hypothese": "un deux trois quatre cinq six sept"}
    assert TR.controle_anti_fuite({"fin": "aucun"}, ["JF1-X"], [fiche_], [fiche_["titre"]])["resultat"] == "conforme"
    assert TR.controle_anti_fuite({"fin": "Titre assez long pour compter"}, ["JF1-X"], [fiche_], [fiche_["titre"]])["resultat"] == "refuse"


def test_liste_blanche_refuse_un_texte_libre():
    conf = brut(V_KIMI)
    with pytest.raises(ValueError):
        TR.valider_liste_blanche({"fin": "une phrase de fiche recopiée avec des espaces"}, TR.permises_de(conf))
    TR.valider_liste_blanche({"fin": "fini", "par_modele": {"gpt-6-astra": 3}}, TR.permises_de(conf))




# --- corrections de la contre-lecture (CLH-02, CLH-03, CLH-05, CLH-11) ---------------------------------------------------------


def test_clh03_gpt_6_attrape_les_autres_gpt_passent():
    from pole.fiches_v54 import trouver
    conf = lire(brut(V_ARGON))
    i = conf["etiquettes_interdites"]
    assert "gpt" not in i and {"gpt 6", "gpt6", "gpt-6", "chatgpt"} <= set(i)
    for ok in ("comme sur GPT-2 small", "GPT-J", "GPT-4", "un banc GPT-2 medium"):
        assert trouver(ok, i, "prefixe") == [], ok
    for ko in ("gpt-6-astra", "GPT-6", "gpt6", "ChatGPT"):
        assert trouver(ko, i, "prefixe"), ko


def test_clh03_artefact_gpt_seul_refuse():
    b = brut(V_BASE)
    b["etiquettes_interdites"].append("gpt")
    refusee(b, "refusées (la pièce servie les cite)")


PAIRES_RELIEES = [("sonde linéaire", "sophistique non voulue"), ("bruit ajouté aux poids", "sous-élicitation bénigne"), ("distance de Mahalanobis", "retouche d'activation")]
PAIRES_NON_RELIEES = [("autoencodeur parcimonieux", "sonde linéaire"), ("menaces diffuses", "moniteur boîte blanche"), ("exploration hacking", "évasion des moniteurs latents")]
HORS_VOCABULAIRE = []
RETIRES = []  # aucune étiquette exigée n'apparaît dans les textes servis
SANS_OPUS_PROPOSEUR = ["sans_opus", "sans_opus_argon"]
BORNE_SANS_CLAUDE = 23  # calcul : min((max_appels − plan) // appels par fiche en trop), Astra 4, Argon 3
BORNES = {'sans_kimi': 23, 'avec_kimi': 29, 'cinq_especes': 35, 'sans_opus': 23, 'sans_opus_argon': 29}  # calcul : min((max_appels − plan) // appels par fiche en trop)


def source_gk(v):
    from pole.bisociateur_v53 import SourceGuKrenn
    g = brut(v)["bisociateur"]["gu_krenn"]
    return SourceGuKrenn(os.path.join(ICI, g["source"]["chemin"]), g["source"]["sha256"], oeuvres_min_vocabulaire=1,
                         date_debut=g["date_debut"], date_coupure=g["date_coupure"], actif_depuis=g["actif_depuis"], actif_min_oeuvres=1)


def test_source_gu_krenn_tiree_des_textes_servis():
    from pole.bisociateur_v53 import cle_paire
    src = json.load(open(os.path.join(ICI, "pieces", "source-gu-krenn-jangfeng-v1.json"), encoding="utf-8"))
    liste = json.load(open(os.path.join(ICI, "pieces", "concepts-jangfeng-v1.json"), encoding="utf-8"))
    assert all(set(o["concepts"]) <= set(liste) and o["section_piece"] for o in src["oeuvres"])
    assert len({o["ident"] for o in src["oeuvres"]}) == len(src["oeuvres"])  # une œuvre par source
    assert len(set(liste)) == len(liste)
    s_ = source_gk(V_BASE)
    for a, b in PAIRES_RELIEES:
        assert cle_paire(a, b) in s_.reliees, (a, b)
    for a, b in PAIRES_NON_RELIEES:
        assert cle_paire(a, b) not in s_.reliees, (a, b)
    for c in HORS_VOCABULAIRE:
        assert c in liste and c not in s_.vocabulaire, c


def test_fiches_six_par_proposeur_et_question_servie():
    for v in CONFS:
        assert brut(v)["simulation"]["fiches_par_appel"] == 6
    conf = lire(brut(V_ARGON))
    cp = cfg.c53.texte_piece(conf, "consigne_proposeur")
    assert "## Ce qu'on attend de chaque espèce" not in cp and "## Lecture prévue de la sortie" not in cp
    assert "## Règles d'intégrité" in cp and "Exactement **six fiches**" in cp


def test_garde_retire_ce_que_les_pieces_emploient():
    from pole.fiches_v54 import trouver
    conf = lire(brut(V_ARGON))
    servis = "\n".join(cfg.c53.texte_piece(conf, n) for n in ("question_servie", *ch.PIECES_SERVIES))
    for e in RETIRES:
        assert e not in conf["etiquettes_interdites"] and e in ch.ETIQUETTES_REFUSEES
        assert trouver(servis, [e], "prefixe") == [e], e  # la pièce servie l'emploie : l'interdire exclurait à tort
    assert trouver(servis, conf["etiquettes_interdites"], "prefixe") == []
    b = brut(V_BASE)
    b["etiquettes_interdites"].append((RETIRES or ["claude"])[0])  # aucune retirée : une étiquette refusée de base
    refusee(b, "refusées (la pièce servie les cite)")


def test_consignes_aiguilleur_lecteur_juge():
    a = open(os.path.join(ICI, "pieces", "consigne-aiguilleur-jangfeng-v1.md"), encoding="utf-8").read()
    assert "En cas de doute entre `niveau_methode` et `concret`, choisis `concret`." in a
    assert "pour ÉPROUVER une mesure ou un juge" in a and "seule une fiche qui donne la recette opérationnelle" in a
    l = open(os.path.join(ICI, "pieces", "consigne-lecteur-jangfeng-v1.md"), encoding="utf-8").read()
    assert "`controle`" in l and "`epreuve`" in l
    j_ = open(os.path.join(ICI, "pieces", "consigne-juge-jangfeng-v1.md"), encoding="utf-8").read()
    q = cfg.c53.texte_piece(lire(brut(V_BASE)), "question_servie")
    i, k = q.index(ch.TETE_QUESTION), q.index(ch.FIN_QUESTION)
    assert q[i:k].split("\n", 1)[1].strip() in j_
    assert all(f"**{x}**" in j_ for x in ch.ITEMS_JUGE) and "originalité n'est pas" in j_
    assert all(brut(v)["items_juge"] == list(ch.ITEMS_JUGE) for v in CONFS)


@pytest.mark.parametrize("v", sorted(CONFS))
def test_max_appels_deux_fois_le_plan_plus_cinq(v):
    devis = json.load(open(os.path.join(ICI, "devis-course-jangfeng-v3.json"), encoding="utf-8"))
    for f, r in brut(v)["relais"].items():
        assert r["max_appels"] == 2 * devis["variantes"][v]["par_fournisseur"][f]["appels"] + 5


APPELS_PAR_FICHE_EN_TROP = {"claude": 4, "astra": 3}  # aiguilleur + juge + deux lectures (Claude) ; juge + deux lectures (Astra)


def plan_par_fournisseur(v, fiches=ch.FICHES_PAR_PROPOSEUR):
    d = {}
    for _, role, modele, n in ch.plan_appels(v, brut(v)["bisociateur"]["k_paires"], fiches_par_proposeur=fiches):
        f = ch.FOURNISSEUR_DE[modele]
        d[f] = d.get(f, 0) + n
    return d


@pytest.mark.parametrize("v", sorted(CONFS))
def test_borne_des_fiches_en_trop_et_huit_fiches(v):
    p6, p7 = plan_par_fournisseur(v), plan_par_fournisseur(v, fiches=ch.FICHES_PAR_PROPOSEUR + 1)
    APPELS_PAR_FICHE_EN_TROP = {"claude": 4, "astra": 3} if v != "sans_claude" else {"astra": 4, "argon": 3}
    for f, k in APPELS_PAR_FICHE_EN_TROP.items():
        assert p7[f] - p6[f] == k * len(ch.VARIANTES[v])
    devis = json.load(open(os.path.join(ICI, "devis-course-jangfeng-v3.json"), encoding="utf-8"))
    rel = brut(v)["relais"]
    borne = min((rel[f]["max_appels"] - devis["variantes"][v]["par_fournisseur"][f]["appels"]) // k
                for f, k in APPELS_PAR_FICHE_EN_TROP.items())
    assert borne == BORNES.get(v, BORNE_SANS_CLAUDE)
    p8 = plan_par_fournisseur(v, fiches=8)
    for f, r in rel.items():
        controles = devis["variantes"][v]["par_fournisseur"][f]["appels"] - p6.get(f, 0)
        assert p8[f] + controles <= r["max_appels"]


@pytest.mark.parametrize("v", sorted(CONFS))
def test_roles_de_la_variante_et_artefact(v):
    b = brut(v)
    ai, ju, le = ch.roles(v)
    assert (b["aiguilleur"]["etiquette"], b["aiguilleur"]["modele"]) == ai
    assert [(j["etiquette"], j["modele"]) for j in b["juges"]] == [tuple(x) for x in ju]
    assert [(x["etiquette"], x["modele"]) for x in b["lecteurs_etiquettes"]] == [tuple(x) for x in le]
    autre = "fable" if ch.ROLES_DE_VARIANTE[v] == "opus" else "opus"
    b["aiguilleur"]["etiquette"], b["aiguilleur"]["modele"] = ch.JEUX_ROLES[autre][0]
    refusee(b, "aiguilleur :")


def test_variantes_sans_opus():
    for v in SANS_OPUS_PROPOSEUR:
        assert all(p["modele"] != "claude-opus-5-5" for p in brut(v)["proposeurs"])
        if ch.ROLES_DE_VARIANTE[v] == "fable":
            assert "claude-opus-5-5" not in json.dumps(brut(v))  # ni proposeur, ni aiguilleur, ni juge, ni lecteur


def test_lanceur_shell_n_accepte_que_les_configurations_du_kit(tmp_path):
    t = open(os.path.join(ICI, "lancer-course-jangfeng-v3.sh"), encoding="utf-8").read()
    for n in CONFS.values():
        assert n in t
    r = shell("lancer", "GO-2026-11-03-98", "configuration-course-" + "ibra" + "him-q1-v2-avec-kimi.json", str(tmp_path / "run"), "p", "c")
    assert r.returncode == 2 and not (tmp_path / "run").exists()


_ = (copy, hashlib)


# --- v2 (CLJ-01) : les trois configurations v1 inchangées ; une ligne de GO par S17 ------------------------------------------

def test_v2_configurations_v1_inchangees_et_neuves_seules_ecrites():
    import hashlib as h
    attendu = {"sans_kimi": "c4270524b26336c08f9ec2625d612750f651d554ea17db16e5ac54931c587bf6",
               "avec_kimi": "b3501965b7054685bbf2722495854ebfccf2144781f4b5678fb258c05c9ead15",
               "cinq_especes": "073528ebe0d361a5158027080b75454fe4000fca03c9e77d0f2b9682b49e575c"}
    for v, s in attendu.items():
        assert h.sha256(open(os.path.join(ICI, CONFS[v]), "rb").read()).hexdigest() == s
    assert DV.NOUVELLES == ("sans_claude",)  # v3 : seule la configuration sans Claude est écrite
    for v, s in {"sans_opus": "fccdac4f71f99ccd12aebe1a7036ab763d518ef12148906ae39895d2cd113698",
                 "sans_opus_argon": "b2baa681a4ed94de75fb663194dbc939826b9c82397821ca2eb73133bd864fed"}.items():
        assert h.sha256(open(os.path.join(ICI, CONFS[v]), "rb").read()).hexdigest() == s  # configurations v2 inchangées
    assert brut("sans_opus")["budget"]["plafond_usd"] == 198 and brut("sans_opus_argon")["budget"]["plafond_usd"] == 237


def test_v2_go_attendu_par_variante(tmp_path, capsys):
    """Le lanceur vérifie une seule ligne : celle de --go-attendu, dont le montant doit être le S17 de la configuration."""
    reg = registre(tmp_path, montant="198 USD", ident="GO-2026-11-03-98")
    a = ["verifier", "--configuration", os.path.join(ICI, CONFS["sans_opus_argon"]), "--registre-go", reg, "--go-attendu", "GO-2026-11-03-98"]
    assert L.principal(a, environnement={"GO_ID": "GO-2026-11-03-98"}) == 2  # ligne à 198 pour une configuration à 237 : refus
    assert "pas exactement le plafond requis" in capsys.readouterr().err
    d = tmp_path / "b"
    d.mkdir()
    reg2 = registre(d, montant="237 USD", ident="GO-2026-11-03-97")
    a2 = ["verifier", "--configuration", os.path.join(ICI, CONFS["sans_opus_argon"]), "--registre-go", reg2, "--go-attendu", "GO-2026-11-03-97"]
    assert L.principal(a2, environnement={"GO_ID": "GO-2026-11-03-97"}) == 0
    a3 = ["verifier", "--configuration", os.path.join(ICI, CONFS["sans_opus"]), "--registre-go", reg, "--go-attendu", "GO-2026-11-03-98"]
    assert L.principal(a3, environnement={"GO_ID": "GO-2026-11-03-98"}) == 0


# --- v3 : variante sans Claude ------------------------------------------------------------------------------------------------

def test_sans_claude_aucun_claude_et_roles():
    b = brut("sans_claude")
    s = json.dumps(b)
    assert "claude-fable-5-1" not in s and "claude-opus-5-5" not in s and "claude" not in b["fournisseurs"] and "claude" not in b["relais"]
    assert (b["aiguilleur"]["modele"], [j["modele"] for j in b["juges"]], [x["modele"] for x in b["lecteurs_etiquettes"]],
            b["bisociateur"]["metteur_fusion"]["modele"]) == ("gpt-6-astra", ["gpt-6-astra", "gemini-4-argon"],
                                                              ["gpt-6-astra", "gemini-4-argon"], "gpt-6-astra")
    assert [p["modele"] for p in b["proposeurs"]] == ["gemini-4-argon", "kimi-k3.1-pro", "gpt-6-astra"]
    assert "kimi-k3.1-pro" not in [b["aiguilleur"]["modele"]] + [j["modele"] for j in b["juges"]] + [x["modele"] for x in b["lecteurs_etiquettes"]]


def test_sans_claude_artefact_fournisseur_claude_ajoute_refuse():
    b = brut("sans_claude")
    b["fournisseurs"]["claude"] = brut(V_KIMI)["fournisseurs"]["claude"]
    refusee(b, "fournisseurs : exactement")


def test_sans_claude_artefact_metteur_claude_refuse():
    b = brut("sans_claude")
    b["bisociateur"]["metteur_fusion"] = {"etiquette": "metteur-fable", "modele": "claude-fable-5-1", "fournisseur": "claude"}
    refusee(b, "metteur :")


def test_shell_sans_claude_ne_demarre_pas_le_relais_claude():
    t = open(os.path.join(ICI, "lancer-course-jangfeng-v3.sh"), encoding="utf-8").read()
    assert "if a claude; then\n  env -i PATH=/usr/bin:/bin LANG=C.UTF-8 ANTHROPIC_API_KEY=" in t
    assert 'MODELES=""; a claude && MODELES="claude-fable-5-1 claude-opus-5-5 "' in t


def test_sans_claude_go_attendu_au_s17(tmp_path, capsys):
    s = brut("sans_claude")["budget"]["plafond_usd"]
    reg = registre(tmp_path, montant="%g USD" % s, ident="GO-2026-11-03-97")
    a = ["verifier", "--configuration", os.path.join(ICI, CONFS["sans_claude"]), "--registre-go", reg, "--go-attendu", "GO-2026-11-03-97"]
    assert L.principal(a, environnement={"GO_ID": "GO-2026-11-03-97"}) == 0
    d = tmp_path / "b"
    d.mkdir()
    reg2 = registre(d, montant="%g USD" % (s + 1), ident="GO-2026-11-03-97")
    a2 = ["verifier", "--configuration", os.path.join(ICI, CONFS["sans_claude"]), "--registre-go", reg2, "--go-attendu", "GO-2026-11-03-97"]
    assert L.principal(a2, environnement={"GO_ID": "GO-2026-11-03-97"}) == 2
    assert "pas exactement le plafond requis" in capsys.readouterr().err
