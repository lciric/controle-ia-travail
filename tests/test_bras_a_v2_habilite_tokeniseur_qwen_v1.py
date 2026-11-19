"""Essais de la vérification du tokeniseur et du gabarit de Qwen (lot 15 du développeur habilité du bras A).

Chaque garde a un cas sain et un artefact (R5). Les tokeniseurs jouets découpent par plus longue correspondance sur un
vocabulaire donné ; le vrai tokeniseur n'est lu que si son dossier est donné par `QWEN_TOKENISEUR_DOSSIER` (les
fichiers ne sont pas versés : 11 Mo ; le gabarit, lui, est versé et toujours éprouvé)."""
import json
import os
import shutil
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets.bras_a_v2_habilite import verification_tokeniseur_qwen_v1 as V

RACINE = Path(__file__).resolve().parents[1]
SOURCES = RACINE / "docs/sources/qwen2.5-7b-instruct-revision-a09a3545-v1"


class _Encodage:
    def __init__(self, ids):
        self.ids = ids


class Jouet:
    """Tokeniseur jouet : plus longue correspondance, de gauche à droite, sur un vocabulaire de chaînes."""

    def __init__(self, jetons):
        self.vocab = {t: i for i, t in enumerate(dict.fromkeys(jetons))}
        self.longueur = max(len(t) for t in self.vocab)

    def encode(self, texte, add_special_tokens=False):
        ids, k = [], 0
        while k < len(texte):
            for n in range(min(self.longueur, len(texte) - k), 0, -1):
                if texte[k:k + n] in self.vocab:
                    ids.append(self.vocab[texte[k:k + n]])
                    k += n
                    break
            else:
                raise AssertionError(f"caractère hors vocabulaire : {texte[k]!r}")
        return _Encodage(ids)


CARACTERES = sorted(set("".join(V.AVANT + V.APRES) + V.BALISE + V.BALISE_FERMANTE + V.CHIFFRES))
JOUET_B = CARACTERES
JOUET_A = CARACTERES + [str(v) for v in range(10, 1000)]


# --- découpage des valeurs ----------------------------------------------------------------------------------------

def test_decoupage_cas_b_sain():
    r = V.decoupage_des_valeurs(Jouet(JOUET_B))
    assert r["cas"] == "B" and r["jetons_des_valeurs"] is None and len(r["jetons_des_chiffres"]) == 10
    assert r["decoupages_en_contexte_controles"] == len(V.AVANT) * 101 * len(V.APRES)


def test_decoupage_cas_a_sain():
    r = V.decoupage_des_valeurs(Jouet(JOUET_A))
    assert r["cas"] == "A" and len(r["jetons_des_valeurs"]) == 101 and r["jetons_des_chiffres"] is None


def test_decoupage_ni_a_ni_b_arrete():
    with pytest.raises(GardeArret, match="ni cas A ni cas B"):
        V.decoupage_des_valeurs(Jouet(CARACTERES + ["10"]))


def test_decoupage_frontiere_instable_arrete():
    """Un jeton qui colle la fin de la balise au premier chiffre : la valeur ne suit plus la balise en propre."""
    with pytest.raises(GardeArret, match="frontière instable"):
        V.decoupage_des_valeurs(Jouet(CARACTERES + [">5"]))


def test_decoupage_valeur_changee_par_la_suite_arrete():
    """Au cas A, un jeton « 100% » avalerait la valeur quand un signe la suit."""
    with pytest.raises(GardeArret, match="change de découpage"):
        V.decoupage_des_valeurs(Jouet(JOUET_A + ["100%"]))


def test_decoupage_deux_valeurs_un_jeton_arrete():
    class Confondu(Jouet):
        def encode(self, texte, add_special_tokens=False):
            e = super().encode(texte)
            return _Encodage([self.vocab["57"] if i == self.vocab["58"] else i for i in e.ids])

    with pytest.raises(GardeArret, match="partagent un même jeton"):
        V.decoupage_des_valeurs(Confondu(JOUET_A))


# --- recensement du vocabulaire -----------------------------------------------------------------------------------

def test_recensement_sain_et_jetons_longs():
    base = {c: i for i, c in enumerate(CARACTERES)}
    r = V.jetons_qui_commencent_par_un_chiffre(base, [{"content": "<|fin1|>", "id": 999}])
    assert sorted(r["chiffres_seuls"]) == list(V.CHIFFRES)
    assert r["longs_commencant_par_un_chiffre"] == {} and r["contenant_un_chiffre_ailleurs"] == {}
    r = V.jetons_qui_commencent_par_un_chiffre({**base, "00": 500, "Ġ7": 501, "5th": 502}, [])
    assert r["longs_commencant_par_un_chiffre"] == {"00": 500, "5th": 502}
    assert r["contenant_un_chiffre_ailleurs"] == {"Ġ7": 501}


def test_recensement_chiffre_manquant_arrete():
    base = {c: i for i, c in enumerate(CARACTERES) if c != "7"}
    with pytest.raises(GardeArret, match="incomplets"):
        V.jetons_qui_commencent_par_un_chiffre(base, [])


# --- empreintes ---------------------------------------------------------------------------------------------------

def _dossier(tmp_path):
    attendues = {}
    for nom in ("a.json", "b.txt"):
        (tmp_path / nom).write_text(nom, encoding="utf-8")
        attendues[nom] = V._sha256(tmp_path / nom)
    return attendues


def test_empreintes_saines(tmp_path):
    attendues = _dossier(tmp_path)
    assert V.verifier_empreintes(tmp_path, attendues) == attendues


def test_empreintes_un_octet_change_arrete(tmp_path):
    attendues = _dossier(tmp_path)
    (tmp_path / "b.txt").write_text("b.txT", encoding="utf-8")
    with pytest.raises(GardeArret, match="empreinte"):
        V.verifier_empreintes(tmp_path, attendues)


def test_empreintes_fichier_absent_arrete(tmp_path):
    attendues = _dossier(tmp_path)
    (tmp_path / "a.json").unlink()
    with pytest.raises(GardeArret, match="absent"):
        V.verifier_empreintes(tmp_path, attendues)


def test_empreintes_fichier_de_poids_arrete(tmp_path):
    attendues = _dossier(tmp_path)
    (tmp_path / "model-00001-of-00004.safetensors").write_bytes(b"")
    with pytest.raises(GardeArret, match="poids"):
        V.verifier_empreintes(tmp_path, attendues)


# --- gabarit (fichier de configuration versé) ---------------------------------------------------------------------

def _gabarit():
    chemin = SOURCES / "tokenizer_config.json"
    assert V._sha256(chemin) == V.EMPREINTES["tokenizer_config.json"]
    return json.loads(chemin.read_text(encoding="utf-8"))["chat_template"]


def test_sources_versees_aux_empreintes_figees():
    for nom in ("tokenizer_config.json", "config.json", "generation_config.json"):
        assert V._sha256(SOURCES / nom) == V.EMPREINTES[nom]


def test_gabarit_sain():
    r = V.verifier_gabarit(_gabarit())
    assert r["variables"] == ["add_generation_prompt", "messages", "tools"]
    assert r["consigne_par_defaut_sans_message_systeme"].startswith("You are Qwen")
    rendu = V.rendre_gabarit(_gabarit(), [{"role": "system", "content": "S"}, {"role": "user", "content": "U"}], True)
    assert rendu == "<|im_start|>system\nS<|im_end|>\n<|im_start|>user\nU<|im_end|>\n<|im_start|>assistant\n"
    assert "You are Qwen" not in rendu


def test_gabarit_avec_date_arrete():
    g = _gabarit().replace("messages[0]['content'] + '<|im_end|>", "messages[0]['content'] + date_string + '<|im_end|>")
    assert g != _gabarit()
    with pytest.raises(GardeArret, match="variables du gabarit"):
        V.verifier_gabarit(g)


def test_gabarit_qui_ajoute_un_texte_arrete():
    g = _gabarit().replace("'<|im_start|>assistant\\n'", "'<|im_start|>assistant\\nSure. '")
    assert g != _gabarit()
    with pytest.raises(GardeArret, match="forme attendue"):
        V.verifier_gabarit(g)


def test_gabarit_qui_reecrit_la_consigne_arrete():
    g = _gabarit().replace("'<|im_start|>system\\n' + messages[0]['content'] + '<|im_end|>\\n'",
                           "'<|im_start|>system\\nYou are Qwen. ' + messages[0]['content'] + '<|im_end|>\\n'")
    assert g != _gabarit()
    with pytest.raises(GardeArret, match="forme attendue"):
        V.verifier_gabarit(g)


# --- vrai tokeniseur, si son dossier est donné --------------------------------------------------------------------

DOSSIER = os.environ.get("QWEN_TOKENISEUR_DOSSIER")
reel = pytest.mark.skipif(not DOSSIER, reason="QWEN_TOKENISEUR_DOSSIER absent : fichiers du tokeniseur non versés")


@reel
def test_vrai_tokeniseur_cas_b():
    r = V.verifier(DOSSIER)
    assert r["cas"] == "B" and r["revision"] == V.REVISION
    assert r["recensement"]["nombre_de_jetons_longs_commencant_par_un_chiffre"] == 0
    assert r["recensement"]["nombre_de_jetons_contenant_un_chiffre_ailleurs"] == 0
    assert r["decoupage"]["jetons_des_chiffres"] == {str(c): 15 + c for c in range(10)}
    assert r["jetons_speciaux"]["fins_de_generation"] == [151643, 151645]


@reel
def test_vrai_tokeniseur_altere_arrete(tmp_path):
    for nom in V.EMPREINTES:
        shutil.copy(Path(DOSSIER) / nom, tmp_path / nom)
    brut = json.loads((tmp_path / "tokenizer.json").read_text(encoding="utf-8"))
    brut["model"]["vocab"]["00"] = brut["model"]["vocab"].pop("!")
    (tmp_path / "tokenizer.json").write_text(json.dumps(brut), encoding="utf-8")
    with pytest.raises(GardeArret, match="empreinte"):
        V.verifier(tmp_path)
    attendues = {**V.EMPREINTES, "tokenizer.json": V._sha256(tmp_path / "tokenizer.json")}
    with pytest.raises(GardeArret, match="vocab.json"):
        V.verifier(tmp_path, attendues)
