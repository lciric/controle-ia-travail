"""Essais (R5) du suivi sans secret v6 (ceux de la v5, plus le secret à cheval sur l'ancienne coupure de 200 caractères, dans `msg`, `error`, la dernière ligne d'erreur et la sortie de création illisible : refusé ; artefact : la v5 le laissait sortir) ; v5 (ceux de la v4, plus les champs d'erreur de la création et son code) ; v4 (ceux de la v3, plus : codes de sortie sur erreur, option --non-vide) ; v3 : ceux de la v2 (champs filtrés, formes encodées, champ gardé, variable exigée, forme
inattendue, absence, création, outil introuvable), plus : sortie vide = erreur, témoin de lecture, enveloppes déballées, délai,
`new_contract` par motif, base 64 « url-safe », plusieurs suffixes, `verifier`."""
import base64
import io
import json
from urllib.parse import quote

import pytest

from controle_ia.neuron_lens import suivi_vast_v6 as sv

JETON = "ghp_factice0123456789ABCDEFabcdef"
ENV = {"CONTROLE_IA_GITHUB_TOKEN_2": JETON}


def appel_factice(*args):
    if args[:2] == ("show", "instance"):
        return 0, json.dumps({"id": 7, "actual_status": "running", "dph_total": 0.42,
                              "extra_env": [["GH_TOKEN", JETON]], "onstart": "x"}), ""
    if args[:2] == ("show", "instances"):
        return 0, json.dumps([{"id": 7, "label": "neuron-lens-volet-a", "extra_env": {"GH_TOKEN": JETON}}]), ""
    if args[0] == "logs":
        return 0, "AMORCE ok\n", ""
    raise AssertionError(args)


def test_champs_filtres_sans_secret():
    vus = []
    sv.main(["instance", "7"], appel=appel_factice, env=ENV, sortie=vus.append)
    sv.main(["instances"], appel=appel_factice, env=ENV, sortie=vus.append)
    assert JETON not in "".join(vus) and '"dph_total": 0.42' in vus[0] and "extra_env" not in vus[1]


def test_variable_exigee_absente_refus():
    vus = []
    with pytest.raises(SystemExit, match="absente"):
        sv.main(["logs", "7"], appel=appel_factice, env={"GH_TOKEN": JETON}, sortie=vus.append)
    with pytest.raises(SystemExit, match="absente"):
        sv.main(["logs", "7"], appel=appel_factice, env={"CONTROLE_IA_GITHUB_TOKEN_2": "court"}, sortie=vus.append)
    assert vus == []
    sv.main(["logs", "7"], appel=appel_factice, env=ENV, sortie=vus.append)  # cas sain
    assert vus == ["AMORCE ok\n"]


@pytest.mark.parametrize("prefixe", ["", "a", "ab", "abc", "Authorization: Basic "])
@pytest.mark.parametrize("forme", ["brut", "adresse", "b64", "b64_entete"])
def test_formes_encodees_refusees(prefixe, forme):
    charge = {"brut": JETON.encode(), "adresse": JETON.encode(), "b64": JETON.encode(),
              "b64_entete": b"x-access-token:" + JETON.encode()}[forme]
    if forme in ("b64", "b64_entete"):
        fuite = base64.b64encode(prefixe.encode() + charge + b"\nsuite").decode()
    elif forme == "adresse":
        fuite = prefixe + "https://x-access-token:" + quote(JETON, safe="") + "@github.com"
    else:
        fuite = prefixe + JETON + " suite"
    vus = []
    with pytest.raises(SystemExit, match="refusée"):
        sv.main(["logs", "7"], appel=lambda *a: (0, f"trace {fuite}\n", ""), env=ENV, sortie=vus.append)
    assert vus == []


def test_formes_ne_refusent_pas_un_texte_sain():
    sec = sv.valeurs_secretes(ENV)
    assert all(len(f) >= sv.MIN_FORME for f in sec)
    sain = "AMORCE 2026-11-14T00:00:00Z pousse : essais passes ; " + base64.b64encode(b"x-access-token:autre-jeton-0123456789").decode()
    assert sv.balayer(sain, sec) == sain


def test_champ_garde_portant_le_secret_refuse():
    vus = []
    app = lambda *a: (0, json.dumps({"id": 7, "label": f"etiquette {JETON}", "status_msg": "ok"}), "")
    with pytest.raises(SystemExit, match="refusée"):
        sv.main(["instance", "7"], appel=app, env=ENV, sortie=vus.append)
    app2 = lambda *a: (0, json.dumps([{"id": 7, "status_msg": f"erreur {JETON}"}]), "")
    with pytest.raises(SystemExit, match="refusée"):
        sv.main(["instances"], appel=app2, env=ENV, sortie=vus.append)
    assert vus == []


def test_instance_absente_erreur_ou_forme_inattendue():
    assert sv.instance(7, appel=lambda *a: (0, "{}", "")) == {"absente": True}
    assert "erreur" in sv.instance(7, appel=lambda *a: (1, "", "Error: instance 7 not found"))
    assert "forme inattendue" in sv.instance(7, appel=lambda *a: (0, json.dumps({"x": 1}), ""))["erreur"]  # v3 : enveloppe déballée
    assert "forme inattendue" in sv.instance(7, appel=lambda *a: (0, json.dumps("texte"), ""))["erreur"]
    assert "illisible" in sv.instance(7, appel=lambda *a: (0, "pas du json", ""))["erreur"]
    assert sv.instances(appel=lambda *a: (0, json.dumps({"instances": [{"id": 3}]}), "")) == [{"id": 3}]
    assert "forme inattendue" in sv.instances(appel=lambda *a: (0, json.dumps({"x": 1}), ""))["erreur"]


def test_absence_prouvee_seulement_sans_erreur():
    vus = []
    assert sv.main(["absente", "8"], appel=appel_factice, env=ENV, sortie=vus.append) == 0  # cas sain : 8 n'est pas listée
    assert sv.main(["absente", "7"], appel=appel_factice, env=ENV, sortie=vus.append) == 1  # présente
    assert sv.main(["absente", "8"], appel=lambda *a: (1, "", "Error: 401"), env=ENV, sortie=vus.append) == 1  # erreur ≠ absence
    assert sv.main(["absente", "8"], appel=lambda *a: (0, '{"x": 1}', ""), env=ENV, sortie=vus.append) == 1  # forme inattendue
    assert "NON prouvée" in vus[2] and "PRÉSENTE" in vus[1]


def test_creation_reduite_et_balayee():
    vus = []
    entree = io.StringIO(json.dumps({"success": True, "new_contract": 123, "env": {"GH_TOKEN": JETON}}))
    sv.main(["creation"], appel=appel_factice, env=ENV, sortie=vus.append, entree=entree)
    assert json.loads(vus[0]) == {"success": True, "new_contract": 123}
    with pytest.raises(SystemExit, match="refusée"):
        sv.main(["creation"], appel=appel_factice, env=ENV, sortie=vus.append, entree=io.StringIO(f"Error: bad env {JETON}"))
    sv.main(["creation"], appel=appel_factice, env=ENV, sortie=vus.append, entree=io.StringIO("Error: no such offer"))
    assert "no such offer" in vus[-1] and len(vus) == 2


def test_outil_introuvable(monkeypatch):
    monkeypatch.setenv("VASTAI_OUTIL", "/inexistant/vastai")
    assert sv.instance(7) == {"erreur": "outil introuvable : /inexistant/vastai"}
    assert "NON prouvée" in sv.absente(7)[1]


def test_sortie_vide_jamais_une_absence():
    vide = lambda *a: (0, "  \n", "")
    assert "sortie vide" in sv.instance(7, appel=vide)["erreur"]
    assert "sortie vide" in sv.instances(appel=vide)["erreur"]
    ok, t = sv.absente(7, appel=vide)
    assert not ok and "NON prouvée" in t
    assert sv.instances(appel=lambda *a: (0, "[]", "")) == []  # cas sain : liste vide écrite en JSON
    assert sv.absente(7, appel=lambda *a: (0, "[]", ""))[0]


def test_temoin_de_lecture():
    liste = lambda *a: (0, json.dumps([{"id": 60480302}, {"id": 9}]), "")
    assert sv.absente(7, appel=liste, temoin=60480302)[0]  # cas sain
    ok, t = sv.absente(7, appel=liste, temoin=58936096)  # artefact : témoin manquant
    assert not ok and "témoin" in t
    vus = []
    assert sv.main(["absente", "7", "--temoin", "58936096"], appel=liste, env=ENV, sortie=vus.append) == 1
    assert sv.main(["absente", "7", "--temoin", "9"], appel=liste, env=ENV, sortie=vus.append) == 0


def test_enveloppes_deballees_et_delai():
    env1 = lambda *a: (0, json.dumps({"instances": {"id": 7, "actual_status": "running", "extra_env": {"GH_TOKEN": JETON}}}), "")
    assert sv.instance(7, appel=env1) == {"id": 7, "actual_status": "running"}
    env2 = lambda *a: (0, json.dumps({"instances": [{"id": 8}, {"id": 7, "cur_state": "stopped"}]}), "")
    assert sv.instance(7, appel=env2) == {"id": 7, "cur_state": "stopped"}
    assert sv.instance(5, appel=env2) == {"absente": True}
    assert "délai" in sv.instance(7, appel=lambda *a: (124, "", "délai de 120 s dépassé"))["erreur"]


def test_delai_capture(monkeypatch):
    import subprocess

    def lent(*a, **k):
        raise subprocess.TimeoutExpired(cmd="vastai", timeout=120)
    monkeypatch.setattr(sv.subprocess, "run", lent)
    assert sv.instance(7) == {"erreur": "délai de 120 s dépassé"}


def test_creation_par_motif():
    r = sv.creation("WARNING: quelque chose\n{'success': True, 'new_contract': 4242}\n")
    assert r == {"new_contract": 4242, "extrait_par_motif": True}
    vus = []
    assert sv.main(["creation"], appel=appel_factice, env=ENV, sortie=vus.append, entree=io.StringIO("Error: x")) == 1
    assert sv.main(["creation"], appel=appel_factice, env=ENV, sortie=vus.append,
                   entree=io.StringIO('{"success": true, "new_contract": 5}')) == 0


@pytest.mark.parametrize("suffixe", [b"", b"x", b"xy", b"\nsuite plus longue"])
@pytest.mark.parametrize("prefixe", [b"", b"a", b"ab"])
@pytest.mark.parametrize("urlsafe", [False, True])
def test_base64_tous_alignements_et_suffixes(prefixe, suffixe, urlsafe):
    for charge in (JETON.encode(), b"x-access-token:" + JETON.encode()):
        enc = (base64.urlsafe_b64encode if urlsafe else base64.b64encode)(prefixe + charge + suffixe).decode()
        with pytest.raises(SystemExit, match="refusée"):
            sv.balayer(f"trace {enc}", sv.valeurs_secretes(ENV))


def test_verifier():
    assert sv.verifier(appel=lambda *a: (0, json.dumps([{"id": 60480302}]), ""))[0]  # cas sain
    assert not sv.verifier(appel=lambda *a: (0, "", ""))[0]  # sortie vide
    assert not sv.verifier(appel=lambda *a: (0, json.dumps([{"id": sv.ID_BIDON}]), ""))[0]  # bidon présent
    with pytest.raises(SystemExit, match="absente"):
        sv.main(["verifier"], appel=appel_factice, env={}, sortie=print)


def test_url_safe_discrimine_sur_un_secret_non_alphanumerique():
    """Pour un jeton fait de lettres, chiffres, `_` et `-`, la base 64 ne contient jamais `+` ni `/` (« url-safe » = standard) ; un
    secret contenant `~` ou `?` en contient : la v3 le voit sous sa forme « url-safe », pas la v2 (artefact)."""
    from controle_ia.neuron_lens import suivi_vast_v2 as v2
    sec = "~~~jeton?factice~~~0123456789~~~"
    env = {"CONTROLE_IA_GITHUB_TOKEN_2": sec}
    manques_v2 = 0
    for prefixe in (b"", b"a", b"ab"):
        enc = base64.urlsafe_b64encode(prefixe + sec.encode() + b"\n").decode()
        assert "-" in enc or "_" in enc
        with pytest.raises(SystemExit, match="refusée"):
            sv.balayer(enc, sv.valeurs_secretes(env))
        manques_v2 += not any(s in enc for s in v2.valeurs_secretes(env))
    assert manques_v2 == 3


def test_codes_de_sortie_sur_erreur():
    vus = []
    err = lambda *a: (1, "", "Error: 401")
    assert sv.main(["instance", "7"], appel=err, env=ENV, sortie=vus.append) == 1
    assert sv.main(["instances"], appel=err, env=ENV, sortie=vus.append) == 1
    assert sv.main(["logs", "7"], appel=err, env=ENV, sortie=vus.append) == 1
    assert sv.main(["instance", "7"], appel=lambda *a: (0, "", ""), env=ENV, sortie=vus.append) == 1  # sortie vide
    assert sv.main(["instance", "7"], appel=lambda *a: (0, '"texte"', ""), env=ENV, sortie=vus.append) == 1  # forme inattendue
    assert sv.main(["instance", "7"], appel=appel_factice, env=ENV, sortie=vus.append) == 0  # cas sain
    assert sv.main(["instances"], appel=appel_factice, env=ENV, sortie=vus.append) == 0
    assert sv.main(["logs", "7"], appel=appel_factice, env=ENV, sortie=vus.append) == 0
    assert "Error: 401" in vus[2]


def test_non_vide():
    vide = lambda *a: (0, "[]", "")
    assert sv.absente(7, appel=vide)[0]  # sans l'option : liste vide = absence prouvée
    ok, t = sv.absente(7, appel=vide, non_vide=True)
    assert not ok and "liste vide" in t
    vus = []
    assert sv.main(["absente", "7", "--non-vide"], appel=vide, env=ENV, sortie=vus.append) == 1
    assert sv.main(["absente", "8", "--non-vide"], appel=appel_factice, env=ENV, sortie=vus.append) == 0


def test_creation_champs_d_erreur_et_code():
    r = sv.creation('{"success": false, "new_contract": 60669495, "error": "insufficient_credit", "msg": "x" , "env": {"GH_TOKEN": "y"}}')
    assert r == {"success": False, "new_contract": 60669495, "error": "insufficient_credit", "msg": "x"}
    vus = []
    code = sv.main(["creation"], appel=appel_factice, env=ENV, sortie=vus.append,
                   entree=io.StringIO('{"success": false, "new_contract": 60669495, "msg": "solde"}'))
    assert code == 1 and "solde" in vus[0]  # success faux : code 1 malgré le new_contract
    with pytest.raises(SystemExit, match="refusée"):
        sv.main(["creation"], appel=appel_factice, env=ENV, sortie=vus.append,
                entree=io.StringIO('{"success": false, "msg": "bad env %s"}' % JETON))
    assert sv.main(["creation"], appel=appel_factice, env=ENV, sortie=vus.append,
                   entree=io.StringIO('{"success": true, "new_contract": 5}')) == 0


@pytest.mark.parametrize("ou", ["msg", "error", "erreur_instance", "creation_illisible"])
def test_secret_a_cheval_sur_l_ancienne_coupure(ou):
    from controle_ia.neuron_lens import suivi_vast_v5 as v5
    texte = "x" * 180 + "GH_TOKEN=" + JETON + " suite"  # le jeton commence vers le 190e caractère, à cheval sur la coupure
    if ou in ("msg", "error"):
        entree = json.dumps({"success": False, "new_contract": 1, ou: texte})
        arg, appel = ["creation"], appel_factice
    elif ou == "creation_illisible":
        entree, arg, appel = "Error: " + texte, ["creation"], appel_factice
    else:
        entree, arg, appel = "", ["instance", "7"], (lambda *a: (1, "", texte))
    vus = []
    with pytest.raises(SystemExit, match="refusée"):
        sv.main(arg, appel=appel, env=ENV, sortie=vus.append, entree=io.StringIO(entree))
    assert vus == []
    # artefact : la v5 tronquait avant de balayer et laissait sortir le début du jeton
    vus5 = []
    try:
        v5.main(arg, appel=appel, env=ENV, sortie=vus5.append, entree=io.StringIO(entree))
    except SystemExit:
        pass
    assert vus5 and JETON[:4] in vus5[0] and JETON not in vus5[0]


def test_sortie_bornee_apres_balayage():
    vus = []
    sv.main(["creation"], appel=appel_factice, env=ENV, sortie=vus.append,
            entree=io.StringIO(json.dumps({"success": False, "msg": "m" * 5000})))
    assert len(vus[0]) <= sv.LIMITE_SORTIE + 40 and vus[0].endswith("(tronqué après balayage)")
