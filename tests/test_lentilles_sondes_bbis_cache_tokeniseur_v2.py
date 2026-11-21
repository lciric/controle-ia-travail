"""Essais du correctif du tokeniseur pour le script voisin du corpus des jetons gardés (`cache_tokeniseur_v2`, `lanceur_v9`).

Le défaut : le script du corpus est joué **en ligne et sans clé** ; la bibliothèque de chargement y demande au dépôt à porte
les fichiers de tokeniseur que le cache ne porte pas (`tokenizer.model` le premier), et le refus du dépôt arrête le script.

R5 : chaque garde a son cas sain et son artefact. Les essais de la première partie jouent le **vrai chargement** (versions de
`requirements-cpu.txt`) dans un processus enfant, avec l'environnement que le montage donne aux scripts du voisin, contre une
**porte simulée sur 127.0.0.1** : interface du dépôt ouverte sans clé (elle rend le commit de la branche principale), tout
fichier refusé par le code 401 du dépôt à porte. Aucune requête ne sort de la machine ; aucune clé n'est lue (la seule clé
des essais est la fausse clé des jouets) ; le tokeniseur est un jouet de cinq jetons fabriqué ici.
"""
from __future__ import annotations

import ast
import difflib
import inspect
import json
import os
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import pytest

pytest.importorskip("torch")
pytest.importorskip("transformers")
pytest.importorskip("tokenizers")
pytest.importorskip("safetensors")

import lentilles_sondes_bbis_jouets_v8 as J8  # noqa: E402
import lentilles_sondes_bbis_jouets_v9 as J  # noqa: E402
from controle_ia.lentilles_sondes_bbis import cache_tokeniseur_v2 as ct  # noqa: E402
from controle_ia.lentilles_sondes_bbis import constantes_v1 as K  # noqa: E402
from controle_ia.lentilles_sondes_bbis import lanceur_v8 as la8  # noqa: E402
from controle_ia.lentilles_sondes_bbis import lanceur_v9 as la  # noqa: E402
from controle_ia.lentilles_sondes_bbis import montage_v1 as mo  # noqa: E402
from controle_ia.lentilles_sondes_bbis.constantes_v1 import Arret, Refus  # noqa: E402

PAQUET = Path(la.__file__).resolve().parent
ESSAIS = Path(__file__).resolve().parent
OUTIL = J.RACINE / "docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/outils/fabrique-lanceur-v9-v1.py"
COPIE_CATALOGUE = J.RACINE / "docs/sources/neuron-lens-lecture-20261113/depot-neuron-lens/neuron_lens-catalog.py.txt"
DEPOT, REV = K.DEPOT_LLAMA, K.REVISION_LLAMA
AUTRE_REV = "f" * 40
ARBRE = mo.url_arbre(DEPOT, REV)
# Le chargement du tokeniseur par le catalogue du voisin, tel que la copie versée le porte (essai d'égalité plus bas).
TOKENISEUR_DU_VOISIN = ('@functools.cache\n'
                        'def tokenizer(model: str = MODEL):\n'
                        '    from transformers import AutoTokenizer\n'
                        '    return AutoTokenizer.from_pretrained(model)\n')
CATALOGUE = ('import functools\nimport os\n\nMODEL = os.environ.get("NEURON_LENS_MODEL", "Qwen/Qwen3-8B")\n\n\n'
             + TOKENISEUR_DU_VOISIN)


# --- tokeniseur jouet, arbre de racine, porte simulée ------------------------------------------------------------------------------------------
def _fichiers_jouets() -> dict[str, bytes]:
    """Les quatre fichiers `.json` que le lanceur pose (mêmes noms que ceux du dépôt), pour un tokeniseur de cinq jetons."""
    from tokenizers import Tokenizer, models, pre_tokenizers
    tok = Tokenizer(models.BPE(vocab={"<|begin_of_text|>": 0, "<|eot|>": 1, "a": 2, "b": 3, "ab": 4}, merges=[("a", "b")]))
    tok.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=False)
    return {
        "tokenizer.json": tok.to_str().encode("utf-8"),
        "tokenizer_config.json": json.dumps({
            "bos_token": "<|begin_of_text|>", "eos_token": "<|eot|>", "clean_up_tokenization_spaces": False,
            "chat_template": "{{ bos_token }}", "model_input_names": ["input_ids", "attention_mask"], "model_max_length": 131072,
            "tokenizer_class": "PreTrainedTokenizerFast"}).encode(),
        "special_tokens_map.json": json.dumps({"bos_token": "<|begin_of_text|>", "eos_token": "<|eot|>"}).encode(),
        "config.json": json.dumps({"architectures": ["LlamaForCausalLM"], "model_type": "llama", "vocab_size": 5, "hidden_size": 8,
                                   "num_hidden_layers": 1, "num_attention_heads": 1, "bos_token_id": 0, "eos_token_id": 1}).encode()}


FICHIERS = _fichiers_jouets()
ATTENDUS = {n: (len(c), mo.identifiant_git(c)) for n, c in FICHIERS.items()}
RACINE_DU_DEPOT = ["LICENSE", "README.md", "USE_POLICY.md", "generation_config.json", "model.safetensors.index.json", *FICHIERS]


def _arbre(fichiers=RACINE_DU_DEPOT, dossiers=("original",)) -> bytes:
    return json.dumps([{"type": "file", "path": f, "oid": "0" * 40, "size": 1} for f in fichiers]
                      + [{"type": "directory", "path": d, "oid": "0" * 40, "size": 0} for d in dossiers]).encode()


def _transport(arbre: bytes | None = None, refus=()) -> J.TransportSimule:
    """Hôte simulé du lanceur : l'arbre de la racine du dépôt du modèle, servi avec la bonne clé seulement."""
    return J.TransportSimule({ARBRE: _arbre() if arbre is None else arbre}, a_porte={ARBRE}, refus=refus)


def _poser(tmp: Path, transport=None, **kw) -> dict:
    return ct.poser_cache_tokeniseur(_transport() if transport is None else transport, mo.Cle(J.FAUSSE_CLE), tmp / "hf",
                                     dict(FICHIERS), dict(ATTENDUS), **kw)


@pytest.fixture
def porte():
    """Porte simulée : `ouvrir(commit)` rend (port, appels). L'interface du dépôt répond sans clé (commit de la branche
    principale, liste des fichiers, 404 pour un dossier absent) ; tout fichier (`/resolve/`) est refusé par le code 401 et
    l'en-tête du dépôt à porte. `appels` : (méthode, chemin, clé présente dans les en-têtes)."""
    serveurs = []

    def ouvrir(commit: str = REV):
        appels = []

        class Reponse(BaseHTTPRequestHandler):
            def log_message(self, *a):
                pass

            def _rendre(self, code, corps, code_d_erreur=None):
                self.send_response(code)
                self.send_header("Content-Type", "application/json")
                if code_d_erreur:
                    self.send_header("X-Error-Code", code_d_erreur)
                self.send_header("Content-Length", str(len(corps)))
                self.end_headers()
                if self.command != "HEAD":
                    self.wfile.write(corps)

            def _tout(self):
                appels.append((self.command, self.path, "Authorization" in self.headers))
                chemin, interface = self.path.split("?")[0], "/api/models/" + DEPOT
                if not chemin.startswith(interface):
                    return self._rendre(401, b'{"error":"porte"}', "GatedRepo")
                reste = chemin[len(interface):]
                if reste == "" or reste.startswith("/revision/"):
                    return self._rendre(200, json.dumps({"id": DEPOT, "modelId": DEPOT, "sha": commit, "private": False,
                                                         "gated": "manual", "siblings": [{"rfilename": f} for f in
                                                                                         RACINE_DU_DEPOT + ["original/tokenizer.model"]]}).encode())
                if reste.startswith("/tree/") and reste.count("/") == 2:
                    return self._rendre(200, _arbre())
                return self._rendre(404, b'{"error":"absent"}', "EntryNotFound")

            do_GET = do_HEAD = do_POST = _tout

        s = ThreadingHTTPServer(("127.0.0.1", 0), Reponse)
        threading.Thread(target=s.serve_forever, daemon=True).start()
        serveurs.append(s)
        return s.server_address[1], appels

    yield ouvrir
    for s in serveurs:
        s.shutdown()
        s.server_close()


def _voisin(tmp: Path) -> Path:
    v = tmp / "voisin"
    (v / "neuron_lens").mkdir(parents=True)
    (v / "neuron_lens" / "__init__.py").write_text("")
    (v / "neuron_lens" / "catalog.py").write_text(CATALOGUE, encoding="utf-8")
    return v


def _charger(tmp: Path, port: int | None, hors_ligne: bool, nom: str) -> tuple[bool, str]:
    """Joue le chargement du tokeniseur par le catalogue (script du lanceur), dans l'environnement que le montage donne aux
    scripts du voisin ; l'hôte des téléchargements est la porte simulée. Rend (réussi, journal)."""
    voisin = tmp / "voisin" if (tmp / "voisin").exists() else _voisin(tmp)
    env = {k: v for k, v in os.environ.items() if not k.lower().endswith("_proxy") and not k.startswith("HF_")}
    env |= {K.NOM_CLE: J.FAUSSE_CLE, "NO_PROXY": "127.0.0.1", "no_proxy": "127.0.0.1",
            "HF_ENDPOINT": f"http://127.0.0.1:{9 if port is None else port}"}
    enfant = mo.environnement_enfant(voisin, tmp / "hf", hors_ligne, env)
    assert K.NOM_CLE not in enfant and enfant.get("HF_HUB_OFFLINE") == ("1" if hors_ligne else None)
    journal = tmp / f"journal-{nom}.txt"
    try:
        mo.jouer_script([sys.executable, "-c", la.SCRIPT_TOKENISEUR + "print('LU', repr(tok.decode([4])), len(tok))\n"], voisin,
                        enfant, journal)
        return True, journal.read_text(encoding="utf-8", errors="replace")
    except Arret:
        return False, journal.read_text(encoding="utf-8", errors="replace")


def _fichiers_demandes(appels) -> list[str]:
    return [chemin.split("/resolve/")[1] for _, chemin, _ in appels if "/resolve/" in chemin]


# --- le défaut et sa correction, par le vrai chargement ----------------------------------------------------------------------------------------
def test_le_jouet_charge_le_tokeniseur_comme_la_copie_versee_du_catalogue_du_voisin():
    assert TOKENISEUR_DU_VOISIN in COPIE_CATALOGUE.read_text(encoding="utf-8")
    assert 'MODEL = os.environ.get("NEURON_LENS_MODEL", "Qwen/Qwen3-8B")\n' in COPIE_CATALOGUE.read_text(encoding="utf-8")


def test_artefact_l_ancien_cache_en_ligne_et_sans_cle_refus_du_depot_a_porte_sur_tokenizer_model(tmp_path, porte):
    """Le défaut : cache posé par `montage_v1.poser_cache_tokeniseur` seul. Hors ligne il suffit ; en ligne et sans clé, le
    chargement demande `tokenizer.model` à l'hôte, à la révision épinglée, et s'arrête sur le refus du dépôt à porte."""
    mo.poser_cache_tokeniseur(tmp_path / "hf", dict(FICHIERS))
    reussi, journal = _charger(tmp_path, None, True, "hors-ligne")
    assert reussi and "LU 'ab' 5" in journal
    port, appels = porte()
    reussi, journal = _charger(tmp_path, port, False, "en-ligne")
    assert not reussi and "gated repo" in journal and f"/resolve/{REV}/tokenizer.model" in journal
    assert _fichiers_demandes(appels) == [f"{REV}/tokenizer.model"]
    assert appels and not any(avec_cle for _, _, avec_cle in appels) and J.FAUSSE_CLE not in journal


def test_sain_le_cache_neuf_charge_en_ligne_et_sans_cle_sans_demander_un_seul_fichier(tmp_path, porte):
    releve = _poser(tmp_path)
    assert releve["marqueurs_d_absence"] == sorted(ct.ABSENTS_CONNUS)
    port, appels = porte()
    reussi, journal = _charger(tmp_path, port, False, "en-ligne")
    assert reussi and "LU 'ab' 5" in journal, journal
    assert _fichiers_demandes(appels) == []                                # aucun fichier demandé à l'hôte
    assert appels and not any(avec_cle for _, _, avec_cle in appels)        # l'interface seule, et jamais la clé
    assert J.FAUSSE_CLE not in journal
    assert ct.exiger_cache(tmp_path / "hf", ATTENDUS)["fichiers_poses"] == releve["fichiers_poses"]   # le chargement n'a rien changé
    reussi, journal = _charger(tmp_path, None, True, "hors-ligne")          # et le chargement hors ligne lit le même tokeniseur
    assert reussi and "LU 'ab' 5" in journal


@pytest.mark.parametrize("sans", ct.ABSENTS_CONNUS)
def test_chaque_marqueur_est_necessaire(sans, tmp_path, porte):
    """Sans l'un des marqueurs, le chargement en ligne demande ce fichier à l'hôte et s'arrête sur le refus du dépôt à porte."""
    _poser(tmp_path, absents=tuple(n for n in ct.ABSENTS_CONNUS if n != sans))
    port, appels = porte()
    reussi, journal = _charger(tmp_path, port, False, "en-ligne")
    assert not reussi and "gated repo" in journal and _fichiers_demandes(appels) == [f"{REV}/{sans}"]


def test_limite_la_branche_principale_du_depot_a_bouge_le_chargement_echoue_et_la_garde_du_cache_le_nomme(tmp_path, porte):
    """Si la branche principale du dépôt ne désigne plus la révision épinglée, le chargement en ligne ne lit plus le cache
    posé : il échoue, et la relecture du cache nomme la cause (la bibliothèque a réécrit la branche dans le cache)."""
    _poser(tmp_path)
    port, appels = porte(AUTRE_REV)
    reussi, journal = _charger(tmp_path, port, False, "en-ligne")
    assert not reussi and all(f.startswith(AUTRE_REV + "/") for f in _fichiers_demandes(appels)) and _fichiers_demandes(appels)
    with pytest.raises(Arret, match="la branche principale n'y désigne pas la révision du texte"):
        ct.exiger_cache(tmp_path / "hf", ATTENDUS)


# --- gardes du module : noms, arbre, absence ---------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("nom", ["original/tokenizer.model", "../tokenizer.model", "", ".cache", "a b", None, 3])
def test_noms_hors_de_la_racine_refuses(nom, tmp_path):
    with pytest.raises(Arret, match="nom de fichier inattendu"):
        _poser(tmp_path, absents=("tokenizer.model", nom))
    with pytest.raises(Arret, match="nom de fichier inattendu"):
        ct.exiger_noms({"tokenizer.json": b"", nom: b""}, ())
    assert not (tmp_path / "hf").exists()


def test_noms_en_double_ou_a_la_fois_poses_et_marques_refuses(tmp_path):
    ct.exiger_noms(FICHIERS, ct.ABSENTS_CONNUS)                                                        # cas sain
    with pytest.raises(Arret, match="donné deux fois"):
        _poser(tmp_path, absents=("tokenizer.model", "tokenizer.model"))
    with pytest.raises(Arret, match=r"\['tokenizer.json'\] à la fois posé et marqué absent"):
        _poser(tmp_path, absents=("tokenizer.model", "tokenizer.json"))
    assert not (tmp_path / "hf").exists()


def test_arbre_lu_avec_la_cle_a_l_adresse_de_la_racine_a_la_revision_epinglee(tmp_path):
    t = _transport()
    releve = _poser(tmp_path, t)
    assert t.appels == [("octets", ARBRE, True, None, None)] and "recursive=false" in ARBRE and REV in ARBRE
    assert releve["racine_du_depot"] == sorted(RACINE_DU_DEPOT + ["original"])
    assert ct.racine_du_depot(t, mo.Cle(J.FAUSSE_CLE))["original"] == "directory"


def test_arbre_refuse_arret_sans_la_cle_et_rien_n_est_ecrit(tmp_path):
    for t, cle in ((_transport(refus={ARBRE}), mo.Cle(J.FAUSSE_CLE)), (_transport(), None), (_transport(), mo.Cle("autre-cle"))):
        with pytest.raises(Arret, match="arbre des fichiers du modèle refusé .* avant tout flux long") as e:
            ct.poser_cache_tokeniseur(t, cle, tmp_path / "hf", dict(FICHIERS), dict(ATTENDUS))
        assert J.FAUSSE_CLE not in str(e.value) and "autre-cle" not in str(e.value) and not (tmp_path / "hf").exists()


@pytest.mark.parametrize("arbre, motif", [
    (b"\xff\xfe", "illisible"), (b"{pas du json", "illisible"),
    (b'{"error": "x"}', "forme inattendue"), (b'["tokenizer.json"]', "forme inattendue"),
    (b'[{"type": "file"}]', "forme inattendue"), (b'[{"path": "a", "type": 1}]', "forme inattendue"),
    (_arbre(RACINE_DU_DEPOT + [f"f{i}" for i in range(ct.BORNE_ARBRE - len(RACINE_DU_DEPOT) - 1)]), "il peut être coupé"),
    (_arbre(RACINE_DU_DEPOT + ["tokenizer.json"]), "entrée en double")])
def test_arbre_illisible_de_forme_inattendue_peut_etre_coupe_ou_en_double_arret(arbre, motif, tmp_path):
    with pytest.raises(Arret, match=motif):
        _poser(tmp_path, _transport(arbre))
    assert not (tmp_path / "hf").exists()


def test_arbre_juste_sous_la_borne_lu(tmp_path):
    arbre = _arbre(RACINE_DU_DEPOT + [f"f{i}" for i in range(ct.BORNE_ARBRE - len(RACINE_DU_DEPOT) - 2)])
    assert len(json.loads(arbre)) == ct.BORNE_ARBRE - 1
    assert len(_poser(tmp_path, _transport(arbre))["racine_du_depot"]) == ct.BORNE_ARBRE - 1


@pytest.mark.parametrize("arbre", [_arbre([], ()), _arbre([f for f in RACINE_DU_DEPOT if f != "tokenizer_config.json"]),
                                   _arbre([f for f in RACINE_DU_DEPOT if f != "config.json"], ("original", "config.json"))])
def test_temoin_un_fichier_pose_absent_de_l_arbre_arret(arbre, tmp_path):
    """Un arbre vide dirait tout fichier absent : le témoin (chaque fichier posé y figure comme fichier) l'arrête."""
    with pytest.raises(Arret, match="posé\\(s\\) dans le cache mais absent\\(s\\) de l'arbre"):
        _poser(tmp_path, _transport(arbre))
    assert not (tmp_path / "hf").exists()


@pytest.mark.parametrize("present", ct.ABSENTS_CONNUS)
@pytest.mark.parametrize("sorte", ["file", "directory"])
def test_un_fichier_a_marquer_existe_a_la_racine_aucun_marqueur_arret(present, sorte, tmp_path):
    """Second cas du mandat : si le fichier existe à la racine du dépôt, aucun marqueur d'absence n'est écrit ; arrêt, nœud."""
    arbre = _arbre(RACINE_DU_DEPOT + ([present] if sorte == "file" else []), ("original",) + ((present,) if sorte != "file" else ()))
    with pytest.raises(Arret, match=rf"\['{present}'\] existe\(nt\) à la racine du dépôt du modèle") as e:
        _poser(tmp_path, _transport(arbre))
    assert "aucun marqueur d'absence n'est écrit" in str(e.value) and not (tmp_path / "hf").exists()


def test_un_fichier_du_meme_nom_dans_un_dossier_ne_compte_pas_pour_la_racine(tmp_path):
    """Le dépôt réel porte `original/tokenizer.model` : la bibliothèque cherche `tokenizer.model` à la racine, où il manque."""
    arbre = _arbre(RACINE_DU_DEPOT + ["original/tokenizer.model"])
    assert _poser(tmp_path, _transport(arbre))["marqueurs_d_absence"] == sorted(ct.ABSENTS_CONNUS)


# --- la pose et la relecture du cache ---------------------------------------------------------------------------------------------------------
def _base(tmp: Path) -> Path:
    return tmp / "hf" / "hub" / "models--meta-llama--Llama-3.1-8B-Instruct"


def test_pose_saine_les_fichiers_de_l_ancienne_pose_et_trois_marqueurs_vides(tmp_path):
    releve = _poser(tmp_path)
    base = _base(tmp_path)
    assert base == ct.base_du_cache(tmp_path / "hf")
    ancien = mo.poser_cache_tokeniseur(tmp_path / "ancien", dict(FICHIERS))
    for nom, contenu in FICHIERS.items():                                   # mêmes fichiers, aux mêmes places, que l'ancienne pose
        assert (base / "snapshots" / REV / nom).read_bytes() == contenu == (ancien / nom).read_bytes()
    assert (base / "refs" / "main").read_text() == REV
    marqueurs = sorted((base / ".no_exist" / REV).iterdir())
    assert [p.name for p in marqueurs] == sorted(ct.ABSENTS_CONNUS) and all(p.stat().st_size == 0 for p in marqueurs)
    assert releve["fichiers_poses"] == {n: {"taille": t, "identifiant_git": i} for n, (t, i) in ATTENDUS.items()}
    assert releve["depot"] == DEPOT and releve["revision"] == REV and J.FAUSSE_CLE not in json.dumps(releve)
    assert ct.ABSENTS_CONNUS == ("tokenizer.model", "added_tokens.json", "chat_template.jinja")


def test_sans_nom_a_marquer_aucun_dossier_de_marqueurs(tmp_path):
    assert _poser(tmp_path, absents=())["marqueurs_d_absence"] == [] and not (_base(tmp_path) / ".no_exist").exists()
    with pytest.raises(Arret, match="marqueurs d'absence ne sont pas exactement ceux attendus"):
        ct.exiger_cache(tmp_path / "hf", ATTENDUS)                          # relu avec les trois noms attendus : arrêt


def test_cache_deja_present_rien_n_est_reecrit(tmp_path):
    _poser(tmp_path)
    t = _transport()
    with pytest.raises(Arret, match="existe déjà dans le cache"):
        _poser(tmp_path, t)
    assert t.appels == []


def test_fichiers_et_attendus_qui_ne_se_repondent_pas_arret(tmp_path):
    t = _transport()
    with pytest.raises(Arret, match="ne se répondent pas"):
        ct.poser_cache_tokeniseur(t, mo.Cle(J.FAUSSE_CLE), tmp_path / "hf", dict(FICHIERS),
                                  {n: v for n, v in ATTENDUS.items() if n != "config.json"})
    assert t.appels == [] and not (tmp_path / "hf").exists()


def test_fichier_pose_d_une_autre_empreinte_que_le_texte_arret(tmp_path):
    """La pose relit le disque : un contenu qui ne répond pas à la taille et à l'identifiant du texte arrête."""
    for nom, autre in (("tokenizer.json", (ATTENDUS["tokenizer.json"][0], "0" * 40)),
                       ("config.json", (ATTENDUS["config.json"][0] + 1, ATTENDUS["config.json"][1]))):
        with pytest.raises(Arret, match=f"{nom} d'une autre taille ou d'un autre identifiant de contenu"):
            ct.poser_cache_tokeniseur(_transport(), mo.Cle(J.FAUSSE_CLE), tmp_path / nom, dict(FICHIERS), ATTENDUS | {nom: autre})


def _alterer(nom: str, base: Path) -> None:
    instantane, marqueurs = base / "snapshots" / REV, base / ".no_exist" / REV
    if nom == "contenu de même taille":
        c = bytearray((instantane / "tokenizer.json").read_bytes())
        c[10] ^= 1
        (instantane / "tokenizer.json").write_bytes(bytes(c))
    elif nom == "fichier allongé":
        (instantane / "special_tokens_map.json").write_bytes(FICHIERS["special_tokens_map.json"] + b"\n")
    elif nom == "fichier manquant":
        (instantane / "config.json").unlink()
    elif nom == "fichier de plus":
        (instantane / "tokenizer.model").write_bytes(b"x")
    elif nom == "dossier de plus":
        (instantane / "original").mkdir()
    elif nom == "fichier remplacé par un lien":
        (instantane / "config.json").unlink()
        (base / "ailleurs.json").write_bytes(FICHIERS["config.json"])
        (instantane / "config.json").symlink_to(base / "ailleurs.json")
    elif nom == "branche sur une autre révision":
        (base / "refs" / "main").write_text(AUTRE_REV)
    elif nom == "branche suivie d'un saut de ligne":
        (base / "refs" / "main").write_text(REV + "\n")
    elif nom == "branche absente":
        (base / "refs" / "main").unlink()
    elif nom == "autre branche":
        (base / "refs" / "autre").write_text(REV)
    elif nom == "autre instantané":
        (base / "snapshots" / AUTRE_REV).mkdir()
    elif nom == "marqueur manquant":
        (marqueurs / "added_tokens.json").unlink()
    elif nom == "marqueur de plus":
        (marqueurs / "tokenizer.json").touch()
    elif nom == "marqueur non vide":
        (marqueurs / "tokenizer.model").write_bytes(b"x")
    elif nom == "marqueur remplacé par un dossier":
        (marqueurs / "chat_template.jinja").unlink()
        (marqueurs / "chat_template.jinja").mkdir()
    elif nom == "marqueur remplacé par un lien":
        (marqueurs / "tokenizer.model").unlink()
        (marqueurs / "tokenizer.model").symlink_to(marqueurs / "added_tokens.json")
    elif nom == "marqueurs d'une autre révision":
        (base / ".no_exist" / AUTRE_REV).mkdir()
    elif nom == "dossier des marqueurs absent":
        for p in marqueurs.iterdir():
            p.unlink()
        marqueurs.rmdir()
        (base / ".no_exist").rmdir()
    else:
        raise AssertionError(nom)


@pytest.mark.parametrize("alteration, motif", [
    ("contenu de même taille", "tokenizer.json d'une autre taille ou d'un autre identifiant"),
    ("fichier allongé", "special_tokens_map.json d'une autre taille ou d'un autre identifiant"),
    ("fichier manquant", "l'instantané ne porte pas exactement les fichiers posés"),
    ("fichier de plus", "l'instantané ne porte pas exactement les fichiers posés"),
    ("dossier de plus", "l'instantané ne porte pas exactement les fichiers posés"),
    ("fichier remplacé par un lien", "l'instantané ne porte pas exactement les fichiers posés"),
    ("branche sur une autre révision", "la branche principale n'y désigne pas la révision du texte"),
    ("branche suivie d'un saut de ligne", "la branche principale n'y désigne pas la révision du texte"),
    ("branche absente", "la branche principale n'y désigne pas la révision du texte"),
    ("autre branche", "une autre branche ou une autre révision"),
    ("autre instantané", "une autre branche ou une autre révision"),
    ("marqueur manquant", "marqueurs d'absence ne sont pas exactement ceux attendus"),
    ("marqueur de plus", "marqueurs d'absence ne sont pas exactement ceux attendus"),
    ("marqueurs d'une autre révision", "marqueurs d'absence ne sont pas exactement ceux attendus"),
    ("dossier des marqueurs absent", "marqueurs d'absence ne sont pas exactement ceux attendus"),
    ("marqueur non vide", "le marqueur d'absence tokenizer.model n'est pas un fichier vide"),
    ("marqueur remplacé par un dossier", "le marqueur d'absence chat_template.jinja n'est pas un fichier vide"),
    ("marqueur remplacé par un lien", "le marqueur d'absence tokenizer.model n'est pas un fichier vide")])
def test_relecture_du_cache_artefacts(alteration, motif, tmp_path):
    _poser(tmp_path)
    assert ct.exiger_cache(tmp_path / "hf", ATTENDUS)["marqueurs_d_absence"] == sorted(ct.ABSENTS_CONNUS)      # cas sain
    _alterer(alteration, _base(tmp_path))
    with pytest.raises(Arret, match=motif):
        ct.exiger_cache(tmp_path / "hf", ATTENDUS)


def test_relecture_d_un_cache_absent_arret(tmp_path):
    with pytest.raises(Arret, match="la branche principale n'y désigne pas la révision du texte"):
        ct.exiger_cache(tmp_path / "hf", ATTENDUS)


def test_la_valeur_de_la_cle_n_est_lue_par_aucune_ligne_du_module():
    source = inspect.getsource(ct)
    assert ".valeur(" not in source and "environ" not in source and "Authorization" not in source
    importes = {n.name for x in ast.walk(ast.parse(source)) if isinstance(x, ast.Import) for n in x.names}
    importes |= {f"{'.' * x.level}{x.module or ''}" for x in ast.walk(ast.parse(source)) if isinstance(x, ast.ImportFrom)}
    assert importes == {"__future__", "json", "re", "pathlib", ".", ".constantes_v1"}        # ni réseau, ni processus, ni environnement


# --- le lanceur de la version 9 ------------------------------------------------------------------------------------------------------------------
def _rapport(tmp: Path) -> dict:
    return json.loads((tmp / "sortie" / "diag" / J.RUN / "montage-lentilles-bbis.json").read_text(encoding="utf-8"))


def test_montage_entier_de_la_version_9_cache_marque_et_deux_essais_du_tokeniseur_avant_tout_flux(tmp_path):
    m = J.monde(tmp_path)
    la.monter(m.ctx)
    rapport, r = _rapport(tmp_path), m.reglages
    poses = sorted(n for n in r.petits if n.endswith(".json") and n != K.INDEX_LLAMA)
    cache = rapport["cache_du_tokeniseur"]
    assert sorted(cache["fichiers_poses"]) == poses == ["config.json", "tokenizer.json"]
    assert cache["marqueurs_d_absence"] == sorted(ct.ABSENTS_CONNUS) and cache["revision"] == r.revision_llama
    assert "original" in cache["racine_du_depot"] and not set(ct.ABSENTS_CONNUS) & set(cache["racine_du_depot"])
    base = ct.base_du_cache(tmp_path / "travail" / "hf", r.depot_llama)
    assert sorted(p.name for p in (base / ".no_exist" / r.revision_llama).iterdir()) == sorted(ct.ABSENTS_CONNUS)
    assert ct.exiger_cache(tmp_path / "travail" / "hf", {n: r.petits[n] for n in poses}, r.depot_llama, r.revision_llama)
    assert rapport["essai_du_tokeniseur_hors_ligne"] == {"tenu": True, "journal": "journal-essai-tokeniseur.txt"}
    assert rapport["essai_du_tokeniseur_en_ligne_sans_cle"] == {"tenu": True, "journal": la.JOURNAL_ESSAI_EN_LIGNE}
    assert (tmp_path / "travail" / la.JOURNAL_ESSAI_EN_LIGNE).is_file()
    for garde in ("tokeniseur lu du cache par le voisin, hors ligne et sans clé",
                  "fichiers absents du dépôt du modèle vérifiés sur son arbre et marqués absents dans le cache",
                  "tokeniseur lu par le voisin, en ligne et sans clé"):
        assert rapport["gardes"]["liste"].count(garde) == 1
    appels = m.transport.appels
    arbre = mo.url_arbre(r.depot_llama, r.revision_llama)
    lectures = [i for i, a in enumerate(appels) if a[1] == arbre]
    premier_flux = next(i for i, a in enumerate(appels) if a[0] == "flux")
    assert len(lectures) == 2 and lectures[0] < premier_flux and all(appels[i][2] for i in lectures)   # avec la clé, avant tout flux
    assert set(rapport["code"]["empreintes"]) == {f"{x}.py" for x in la.MODULES}
    for dossier in (tmp_path / "sortie", tmp_path / "travail"):
        for p in dossier.rglob("*"):
            if p.is_file() and not p.is_symlink():
                assert J.FAUSSE_CLE.encode() not in p.read_bytes(), p


def test_les_deux_essais_du_tokeniseur_un_hors_ligne_puis_un_en_ligne_tous_deux_sans_cle(tmp_path, monkeypatch):
    m = J.monde(tmp_path)
    trace = tmp_path / "trace.txt"
    monkeypatch.setattr(la, "SCRIPT_TOKENISEUR", la.SCRIPT_TOKENISEUR + (
        "import os\n"
        f"open({str(trace)!r}, 'a').write(repr((os.environ.get('HF_HUB_OFFLINE'), {K.NOM_CLE!r} in os.environ,"
        " os.environ.get('HF_HUB_DISABLE_IMPLICIT_TOKEN'), os.environ.get('NEURON_LENS_MODEL'))) + '\\n')\n"))
    la.monter(m.ctx)
    assert trace.read_text().splitlines() == [repr(("1", False, "1", K.DEPOT_LLAMA)), repr((None, False, "1", K.DEPOT_LLAMA))]


def test_artefact_lanceur_un_fichier_a_marquer_existe_a_la_racine_arret_avant_tout_flux(tmp_path):
    m = J.monde(tmp_path)
    arbre = mo.url_arbre(m.reglages.depot_llama, m.reglages.revision_llama)
    m.transport.fichiers[arbre] = json.dumps(json.loads(m.transport.fichiers[arbre])
                                             + [{"type": "file", "path": "tokenizer.model", "oid": "0" * 40, "size": 9}]).encode()
    with pytest.raises(Arret, match=r"\['tokenizer.model'\] existe\(nt\) à la racine du dépôt du modèle") as e:
        la.monter(m.ctx)
    assert not any(a[0] == "flux" for a in m.transport.appels) and J.FAUSSE_CLE not in str(e.value)
    assert not ct.base_du_cache(tmp_path / "travail" / "hf", m.reglages.depot_llama).exists()
    assert not (tmp_path / "travail" / "journal-essai-tokeniseur.txt").exists()


def test_artefact_lanceur_arbre_des_jouets_de_la_version_8_sans_les_petits_fichiers_arret(tmp_path):
    """L'arbre des jouets de la version 8 ne liste que les poids : le témoin de la lecture de l'arbre l'arrête."""
    m = J.monde(tmp_path)
    arbre = mo.url_arbre(m.reglages.depot_llama, m.reglages.revision_llama)
    m.transport.fichiers[arbre] = json.dumps([e for e in json.loads(m.transport.fichiers[arbre]) if "lfs" in e]).encode()
    with pytest.raises(Arret, match="posé\\(s\\) dans le cache mais absent\\(s\\) de l'arbre"):
        la.monter(m.ctx)
    assert not any(a[0] == "flux" for a in m.transport.appels)


def test_artefact_lanceur_essai_en_ligne_en_echec_arret_avant_tout_flux(tmp_path, monkeypatch):
    """Le chargement réussit hors ligne et échoue en ligne (le défaut) : l'essai en ligne l'arrête avant tout flux long."""
    m = J.monde(tmp_path)
    monkeypatch.setattr(la, "SCRIPT_TOKENISEUR", la.SCRIPT_TOKENISEUR + (
        f"import os\nassert {K.NOM_CLE!r} not in os.environ\n"
        "if os.environ.get('HF_HUB_OFFLINE') != '1':\n    raise SystemExit('refus du dépôt à porte (jouet)')\n"))
    with pytest.raises(Arret, match="ne lit pas le tokeniseur en ligne et sans clé") as e:
        la.monter(m.ctx)
    assert not any(a[0] == "flux" for a in m.transport.appels) and J.FAUSSE_CLE not in str(e.value)
    assert (tmp_path / "travail" / "journal-essai-tokeniseur.txt").read_text() == ""                  # l'essai hors ligne a tenu
    journal = (tmp_path / "travail" / la.JOURNAL_ESSAI_EN_LIGNE).read_text()
    assert "refus du dépôt à porte (jouet)" in journal and "AssertionError" not in journal
    assert str(e.value).count(la.JOURNAL_ESSAI_EN_LIGNE) == 1


def test_artefact_lanceur_l_essai_en_ligne_reecrit_la_branche_du_cache_arret_avant_tout_flux(tmp_path, monkeypatch):
    """La branche principale du dépôt a bougé : la bibliothèque la réécrit dans le cache pendant l'essai en ligne (jouet : le
    script le fait) ; la relecture du cache arrête avant tout flux long."""
    m = J.monde(tmp_path)
    ref = ct.base_du_cache(tmp_path / "travail" / "hf", m.reglages.depot_llama) / "refs" / "main"
    monkeypatch.setattr(la, "SCRIPT_TOKENISEUR", la.SCRIPT_TOKENISEUR + (
        f"import os\nif os.environ.get('HF_HUB_OFFLINE') != '1':\n    open({str(ref)!r}, 'w').write({AUTRE_REV!r})\n"))
    with pytest.raises(Arret, match="la branche principale n'y désigne pas la révision du texte"):
        la.monter(m.ctx)
    assert not any(a[0] == "flux" for a in m.transport.appels)


def test_le_montage_de_la_version_8_pose_un_cache_sans_marqueur(tmp_path):
    """Le défaut au niveau du lanceur : le cache que `lanceur_v8` pose ne porte aucun marqueur d'absence (c'est l'ancien
    cache, dont le premier essai de ce fichier montre l'échec en ligne) ; le catalogue des jouets ne charge aucun tokeniseur
    réel, si bien que le montage de la version 8 ne peut pas le voir."""
    m = J8.monde(tmp_path)
    la8.monter(m.ctx)
    base = ct.base_du_cache(tmp_path / "travail" / "hf", m.reglages.depot_llama)
    assert (base / "snapshots" / m.reglages.revision_llama / "tokenizer.json").is_file() and not (base / ".no_exist").exists()
    assert not (tmp_path / "travail" / la.JOURNAL_ESSAI_EN_LIGNE).exists()


def test_modules_de_la_fiche_du_code_quinze_dont_le_module_du_correctif():
    assert la.MODULES == la8.MODULES[:-1] + ("cache_tokeniseur_v2", "lanceur_v9") and la8.MODULES[-1] == "lanceur_v8"
    assert len(la.MODULES) == 15 and set(la.empreintes_du_code()) == {f"{m}.py" for m in la.MODULES}
    assert la.empreintes_du_code()["cache_tokeniseur_v2.py"] == J.sha((PAQUET / "cache_tokeniseur_v2.py").read_bytes())


def test_fiche_du_code_sans_l_empreinte_du_module_du_correctif_rien_ne_part(tmp_path):
    """La fiche du code doit porter `cache_tokeniseur_v2.py` : sans lui, ou avec une autre empreinte, rien ne part."""
    _, propre = J.ecrire_registres(tmp_path / "r")
    J.ecrire_fiche_code(tmp_path / "depot", propre)
    assert la.exiger_fiche_code(tmp_path / "depot", propre)["sha256"]                                  # cas sain
    fichiers = {f"{la.CHEMIN_PAQUET}/{m}.py": J.sha((PAQUET / f"{m}.py").read_bytes()) for m in la.MODULES}
    nom = f"{la.CHEMIN_PAQUET}/cache_tokeniseur_v2.py"
    for artefact in ({k: v for k, v in fichiers.items() if k != nom}, fichiers | {nom: "0" * 64}):
        J.ecrire_fiche_code(tmp_path / "depot", propre, fichiers=artefact)
        with pytest.raises(Refus, match=r"cache_tokeniseur_v2\.py : empreinte absente de la fiche"):
            la.exiger_fiche_code(tmp_path / "depot", propre)


# --- la version 9 est la version 8 plus ce seul changement -------------------------------------------------------------------------------------------
COPIES = {"lentilles_sondes_bbis_jouets_v8.py": "lentilles_sondes_bbis_jouets_v9.py",
          "test_lentilles_sondes_bbis_addendum_concentration_v6.py": "test_lentilles_sondes_bbis_addendum_concentration_v7.py",
          "test_lentilles_sondes_bbis_corrections_contre_lecture_v7.py": "test_lentilles_sondes_bbis_corrections_contre_lecture_v8.py",
          "test_lentilles_sondes_bbis_garde_egalite_v5.py": "test_lentilles_sondes_bbis_garde_egalite_v6.py",
          "test_lentilles_sondes_bbis_gardes_non_vues_v7.py": "test_lentilles_sondes_bbis_gardes_non_vues_v8.py",
          "test_lentilles_sondes_bbis_montage_v8.py": "test_lentilles_sondes_bbis_montage_v9.py",
          "test_lentilles_sondes_bbis_procedure_v8.py": "test_lentilles_sondes_bbis_procedure_v9.py",
          "test_lentilles_sondes_bbis_lanceur_v8_v1.py": "test_lentilles_sondes_bbis_lanceur_v9_v1.py",
          "test_lentilles_sondes_bbis_lanceur_v8_interruptions_v1.py": "test_lentilles_sondes_bbis_lanceur_v9_interruptions_v1.py",
          "test_lentilles_sondes_bbis_lanceur_v8_garde_arret_present_v1.py": "test_lentilles_sondes_bbis_lanceur_v9_garde_arret_present_v1.py"}
# Importent aussi `lanceur_v8`, sans être copiés : les essais du correctif de la pagination, propres à la version 8, et ce fichier.
PROPRES_A_LA_VERSION_8 = {"test_lentilles_sondes_bbis_corpus_pagine_v1.py"}


def test_l_outil_de_fabrique_rejoue_rend_le_lanceur_de_la_version_9_a_l_octet_pres(tmp_path):
    paquet, essais = tmp_path / "paquet", tmp_path / "essais"
    paquet.mkdir()
    essais.mkdir()
    (paquet / "lanceur_v8.py").write_bytes((PAQUET / "lanceur_v8.py").read_bytes())
    for origine in COPIES:
        (essais / origine).write_bytes((ESSAIS / origine).read_bytes())
    r = subprocess.run([sys.executable, "-B", str(OUTIL), str(paquet), str(essais)], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert (paquet / "lanceur_v9.py").read_bytes() == (PAQUET / "lanceur_v9.py").read_bytes()
    for copie in COPIES.values():
        assert (essais / copie).read_bytes() == (ESSAIS / copie).read_bytes(), copie
    importent = {p.name for p in ESSAIS.glob("*lentilles_sondes_bbis_*.py")
                 if any(ligne.split("#")[0].rstrip().endswith("import lanceur_v8 as la")
                        for ligne in p.read_text(encoding="utf-8").splitlines())}
    assert importent == set(COPIES) | PROPRES_A_LA_VERSION_8


def test_lignes_de_la_version_8_toutes_gardees_hors_la_liste_des_modules_et_la_pose_du_cache():
    """De `lanceur_v8` à `lanceur_v9` : trois lignes retirées seulement (la ligne des modules ; les deux lignes de l'appel à
    `montage_v1.poser_cache_tokeniseur`). Lignes ajoutées hors de l'en-tête : l'import du module neuf, les deux lignes des
    modules, la pose du cache par le module neuf, l'essai en ligne et la relecture du cache, deux gardes dans la liste du
    rapport, la fonction de l'essai en ligne. Aucune autre ligne ne change."""
    v8 = (PAQUET / "lanceur_v8.py").read_text(encoding="utf-8").splitlines()
    v9 = (PAQUET / "lanceur_v9.py").read_text(encoding="utf-8").splitlines()
    diff = list(difflib.ndiff(v8, v9))
    assert [l[2:] for l in diff if l.startswith("- ")] == [
        '           "statistiques_v2", "statistiques_v3", "audits_v1", "phrases_v1", "corpus_pagine_v1", "lanceur_v8")',
        '    mo.poser_cache_tokeniseur(hf_home, {n: c for n, c in petits.items() if n.endswith(".json") and n != K.INDEX_LLAMA},',
        '                              r.depot_llama, r.revision_llama)']
    ajoutees = [l[2:] for l in diff if l.startswith("+ ")]
    debut = ajoutees.index("from . import cache_tokeniseur_v2 as ct")
    fonction = debut + 12                                   # le reste : la fonction de l'essai en ligne et la constante de son journal
    assert ajoutees[debut:fonction] == [
        "from . import cache_tokeniseur_v2 as ct",
        '           "statistiques_v2", "statistiques_v3", "audits_v1", "phrases_v1", "corpus_pagine_v1", "cache_tokeniseur_v2",',
        '           "lanceur_v9")',
        '    poses = {n: c for n, c in petits.items() if n.endswith(".json") and n != K.INDEX_LLAMA}',
        "    attendus = {n: r.petits[n] for n in poses}",
        '    rapport["cache_du_tokeniseur"] = ct.poser_cache_tokeniseur(transport, cle, hf_home, poses, attendus, r.depot_llama,',
        "                                                               r.revision_llama)",
        "    essayer_tokeniseur_en_ligne(ctx, voisin, hf_home)",
        "    ct.exiger_cache(hf_home, attendus, r.depot_llama, r.revision_llama)",
        '    rapport["essai_du_tokeniseur_en_ligne_sans_cle"] = {"tenu": True, "journal": JOURNAL_ESSAI_EN_LIGNE}',
        '        "fichiers absents du dépôt du modèle vérifiés sur son arbre et marqués absents dans le cache",',
        '        "tokeniseur lu par le voisin, en ligne et sans clé",']
    corps = [l for l in ajoutees[fonction:] if l.strip()]
    assert sorted(corps) == sorted(inspect.getsource(la.essayer_tokeniseur_en_ligne).rstrip("\n").splitlines()
                                   + ['JOURNAL_ESSAI_EN_LIGNE = "journal-essai-tokeniseur-en-ligne.txt"']) and len(corps) == 11
    en_tete = ajoutees[:debut]
    assert len(en_tete) == 11 and en_tete[0] == "" and en_tete[1].startswith("Version 9 : correctif du tokeniseur")
    assert v9.index('"""', 1) == v8.index('"""', 1) + 11                                        # les onze lignes sont dans la docstring
    assert not any("mo.poser_cache_tokeniseur" in l for l in v9) and sum("ct.poser_cache_tokeniseur" in l for l in v9) == 1
    assert sum("mo.environnement_enfant(voisin, hf_home, False, ctx.env)" in l for l in v9) == 1   # le seul enfant en ligne du lanceur
