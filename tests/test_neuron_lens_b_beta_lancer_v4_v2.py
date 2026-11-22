"""Essais du lanceur v4 du réajustement de nos lentilles (variante B) et du rangement (`rangement_lentilles_v1`) — sans modèle, sans
réseau, sans loueur ni plateforme de modèles : faux transport, dépôts git jouets, fichiers d'ajustement jouets (torch sur le processeur).

v2 (2026-11-22) = v1 (`test_neuron_lens_b_beta_lancer_v4.py`, `971c45d0…`, scellée trop tôt, archivée sans modification dans
`docs/notes/neuron-lens-v1/devis-reajustement/developpement-v4/brouillons-scelles/`) corrigée de ses deux défauts : l'essai de l'arbre
propre créait `diag/`, qui existe dans l'arbre réduit ; l'essai du texte de `_split_half_64` importait le programme de comparaison, absent
de l'arbre réduit (vu par l'essai à blanc v3). Amorce v5 et dépôt réduit v5 nommés en conséquence. Et cinq essais renforcés après le
banc d'altérations (`developpement-v4/banc_alterations_lanceur_v4_v1.py`, cinq altérations non tuées par la v1) : lignes du 18 refusées
sans la borne de date ; révision rendue illisible ; versions de la pièce du matériel ; un seul retrait de la clé dans l'amorce ; dernière
ligne « COPIE EN ECHEC » et code 23. Rien d'autre.

R5 : pour chaque garde neuve ou changée, un cas sain et au moins un artefact (devis du réajustement v9, § 5, point 5, items (a) à (m) ;
table « item → changement → essai sain → essai artefact » versée dans
`docs/notes/neuron-lens-v1/devis-reajustement/developpement-v4/`). Les essais qui lisent des textes du dépôt (les deux lanceurs,
l'amorce, les exigences) passent aussi dans l'arbre réduit, où ils sont embarqués ; le seul qui construit l'arbre réduit lui-même porte
`copie_reelle` dans son nom : l'amorce l'écarte sur la machine (`-k "not copie_reelle"`), où le script du dépôt réduit n'est pas."""
import ast
import base64
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import quote

import pytest

from controle_ia.manifeste import creer_manifeste, ecrire_resultat
from controle_ia.neuron_lens import b_beta_lancer_v4 as L
from controle_ia.neuron_lens import controles_b_beta_v2 as cb
from controle_ia.neuron_lens import rangement_lentilles_v1 as rg

RACINE = Path(__file__).resolve().parents[1]
GO = "GO-2026-11-23-01"  # forme d'une ligne à venir ; aucune ligne réelle n'est nommée ici
DEPOT = "compte-essai/rangement-essai"
ENV_OK = {"GO_ID": GO, "VARIANTE": "B", "NEURON_LENS_MODEL": L.LLAMA, "HF_HOME": "/tmp/hf", "HF_HUB_OFFLINE": "1"}
REV1, REV2 = "1" * 40, "2" * 40


def _env(etape, **extra):
    e = dict(ENV_OK)
    if etape in L.EN_LIGNE or etape in L.COMMANDES_JETON:
        e.pop("HF_HUB_OFFLINE")
    if etape in L.JETON or etape in L.COMMANDES_JETON:
        e["HF_TOKEN"] = "x"
    if etape in L.COPIES or etape == "cloture":
        e[rg.VARIABLE_DEPOT] = DEPOT
    return e | extra


# ---------------------------------------------------------------- (a) GO attendu, (f) variante, (c) clé, (d) dépôt nommé par variable

def test_a_go_sain_et_artefacts():
    assert L.probleme_go(GO) == [] and L.verifier_environnement("score", ENV_OK) == []
    for go in ("GO-2026-11-18-35", "GO-2026-11-18-02", "GO-2026-11-21-07", "GO-2026-11-2-01", "go-2026-11-23-01", "", None):
        assert L.probleme_go(go), go
        assert L.verifier_environnement("score", ENV_OK | {"GO_ID": go or ""}), go
    assert not hasattr(L, "GO_ATTENDU")  # plus de constante : la ligne n'existe pas à l'écriture


def test_a_lignes_du_18_refusees_meme_sans_la_borne_de_date(monkeypatch):
    monkeypatch.setattr(L, "GO_DATE_MIN", "2026-01-01")  # la borne de date seule ne suffit pas à les écarter (banc d'altérations)
    assert all(L.probleme_go(g) for g in L.GO_REFUSES) and L.probleme_go("GO-2026-11-18-34") == []


def test_f_variante_saine_et_artefacts():
    assert L.verifier_environnement("score", ENV_OK) == []
    assert L.verifier_environnement("croquis", ENV_OK | {"VARIANTE": "A"}) == []
    assert L.verifier_environnement("score", ENV_OK | {"VARIANTE": "A"})  # hors de la variante A
    for v in ("", "C", "b"):
        assert L.verifier_environnement("score", ENV_OK | {"VARIANTE": v}), v
    assert L.ETAPES_A[-1] == "croquis" and L.ETAPES[:len(L.ETAPES_A)] == L.ETAPES_A


def test_c_cle_aux_seules_etapes_jeton():
    for e in ("copie-R", "copie-S", "telecharger-poids"):
        assert L.verifier_environnement(e, _env(e)) == [], e
        sans = {k: v for k, v in _env(e).items() if k != "HF_TOKEN"}
        assert L.verifier_environnement(e, sans), e  # artefact : clé absente
        assert L.verifier_environnement(e, _env(e) | {"HF_HUB_OFFLINE": "1"}), e  # artefact : hors ligne à une copie
    assert L.verifier_environnement("cloture", _env("cloture")) == []
    assert L.verifier_environnement("cloture", {k: v for k, v in _env("cloture").items() if k != "HF_TOKEN"})
    for e in ("score", "croquis", "materiel", "inventaire"):
        assert L.verifier_environnement(e, _env(e)) == [], e
        assert L.verifier_environnement(e, _env(e) | {"HF_TOKEN": "x"}), e  # artefact : clé hors des étapes « jeton »
    assert L.verifier_environnement("score", ENV_OK | {"GH_TOKEN": "x"})


def test_c_env_enfant_sans_secret_meme_avec_la_cle_gardee(monkeypatch):
    monkeypatch.setenv("HF_TOKEN", "secret-gardé-toute-la-course")
    monkeypatch.setenv("GH_TOKEN", "secret")
    e = L.env_enfant(Path("/v"), True)
    assert "HF_TOKEN" not in e and "GH_TOKEN" not in e and e["HF_HUB_OFFLINE"] == "1"


def test_d_depot_nomme_par_variable():
    assert rg.probleme_depot(DEPOT) == [] and L.verifier_environnement("copie-R", _env("copie-R")) == []
    for d in ("", "sans-barre", "a/b/c", "a b/c", "/c", "a/", "https://exemple/a/b"):
        assert rg.probleme_depot(d), d
        assert L.verifier_environnement("copie-R", _env("copie-R") | {rg.VARIABLE_DEPOT: d}), d


def test_d_aucun_nom_de_depot_ni_de_cle_en_dur():
    """Le nom du dépôt de rangement et toute clé : jamais écrits dans le code (seulement des noms de variables)."""
    for f in ("src/controle_ia/neuron_lens/b_beta_lancer_v4.py", "src/controle_ia/neuron_lens/rangement_lentilles_v1.py",
              "scripts/amorce_neuron_lens_b_beta_v5.sh"):
        t = (RACINE / f).read_text(encoding="utf-8")
        assert not re.search(r"hf_[A-Za-z0-9]{20,}|gh[ps]_[A-Za-z0-9]{20,}", t), f
        assert "huggingface.co/" not in t and "lciric/" not in t.replace("lciric/controle-ia-travail", ""), f


# ---------------------------------------------------------------- déroulé : variantes, place des copies et du croquis

def _git_jouet(racine: Path):
    subprocess.run(["git", "init", "-q", str(racine)], check=True)
    (racine / ".gitignore").write_text("/voisin/\n/voisin-banc/\n/originaux/\n")
    subprocess.run(["git", "-C", str(racine), "add", "-A"], check=True)
    subprocess.run(["git", "-C", str(racine), "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-qm", "x"], check=True)


@pytest.fixture
def ctx(tmp_path, monkeypatch):
    _git_jouet(tmp_path)
    c = L.Contexte(tmp_path, "20261123-100000-neuron-lens-b-beta", tmp_path / "hf", depot_rangement=DEPOT, go_id=GO, variante="B")
    creer_manifeste(tmp_path, c.run_id, {"essai": True}, list(cb.TACHES_INTERVALLES), entropie=cb.ENTROPIE)
    return c


def _doubles(monkeypatch):
    monkeypatch.setattr(L, "ETAPE_FONCTIONS", {e: (lambda ctx, e=e: {"double": e}) for e in L.ETAPES})


def _derouler(ctx):
    vues = []
    while (e := L.suite(ctx)) is not None:
        vues.append(e)
        if e == "declencheurs":
            L.ETAPE_FONCTIONS[e] = lambda c: {"declenches": [], "debut_audits": 0.0}
        if e == "verdicts":
            L.ETAPE_FONCTIONS[e] = lambda c: {"fichier": str(L.ecrire_verdicts(c, {"verdict": "partiel"}))}
        L.jouer(ctx, e, _env(e, VARIANTE=ctx.variante))
    return vues


def test_f_d_m_variante_b_entiere_copies_et_croquis_a_leur_place(ctx, monkeypatch):
    _doubles(monkeypatch)
    vues = _derouler(ctx)
    i = vues.index
    assert i("ajustement-R") < i("export") < i("copie-R") < i("ajustement-S") < i("copie-S") < i("croquis") < i("corpus-activations")
    assert vues[1] == "materiel" and vues[-1] == "verdicts" and ctx.fichier_verdicts.exists()


def test_f_variante_a_s_arrete_apres_le_croquis(ctx, monkeypatch):
    _doubles(monkeypatch)
    ctx.variante = "A"
    vues = _derouler(ctx)
    assert vues[-1] == "croquis" and "corpus-activations" not in vues and not ctx.fichier_verdicts.exists()
    with pytest.raises(L.Arret, match="variante"):
        L.jouer(ctx, "corpus-activations", _env("corpus-activations"))  # artefact : étape de B en variante A


def test_f_variante_illisible_arrete_suite(ctx, monkeypatch):
    _doubles(monkeypatch)
    for v in ("", "C"):
        ctx.variante = v
        with pytest.raises(L.Arret, match="variante"):
            L.suite(ctx)


def test_a_preparer_refuse_un_go_ou_une_variante_non_conformes(tmp_path, monkeypatch):
    _git_jouet(tmp_path)
    monkeypatch.setattr(L, "verifier_pieces", lambda r: {})
    monkeypatch.setattr(L, "_git", lambda *a, **k: (_ for _ in ()).throw(AssertionError("le voisin n'est pas touché ici")))
    for go, v in (("GO-2026-11-18-35", "B"), (GO, "")):
        c = L.Contexte(tmp_path, "20261123-100000-neuron-lens-b-beta", tmp_path / "hf", go_id=go, variante=v)
        (c.voisin / ".git").mkdir(parents=True, exist_ok=True)
        with pytest.raises((L.Arret, AssertionError)):
            L.etape_preparer(c)
        assert not c.manifeste.exists()
    cfg = L.configuration({}, GO, "B")
    assert cfg["go_id"] == GO and cfg["variante"] == "B"


# ---------------------------------------------------------------- (h), (i), (k) : ce qui ne change pas, au texte près

def _fonctions(chemin: Path) -> dict:
    s = chemin.read_text(encoding="utf-8")
    return {n.name: ast.get_source_segment(s, n) for n in ast.parse(s).body if isinstance(n, (ast.FunctionDef, ast.ClassDef))}


CHANGEES = {"verifier_environnement", "Contexte", "suite", "exiger_prerequis", "etape_preparer", "configuration", "resume_fit", "main"}


def test_h_i_k_fonctions_de_la_v3_gardees_au_texte_pres():
    v3 = _fonctions(RACINE / "src/controle_ia/neuron_lens/b_beta_lancer_v3.py")
    v4 = _fonctions(RACINE / "src/controle_ia/neuron_lens/b_beta_lancer_v4.py")
    assert set(v3) <= set(v4)
    changees = {n for n in v3 if v3[n] != v4[n]}
    assert changees == CHANGEES, changees
    # (i) : `resume_fit` ne change que d'un commentaire ; `_split_half_64` d'empreinte égale à la constante du programme de comparaison v4
    sans_commentaire = lambda t: [l.split("  #")[0].rstrip() for l in t.splitlines() if not l.strip().startswith("#")]
    assert sans_commentaire(v3["resume_fit"]) == sans_commentaire(v4["resume_fit"])
    assert "jamais lue pour un seuil" not in v4["resume_fit"]
    # méthode `empreinte_fonction` du programme de comparaison v4 (segment source exact, SHA-256), recopiée : le programme n'est pas
    # dans l'arbre réduit (défaut de la v1 de ces essais, vu par l'essai à blanc) ; l'égalité à sa constante est jouée à part
    import hashlib
    assert hashlib.sha256(v4["_split_half_64"].encode("utf-8")).hexdigest() == F_SPLIT_HALF_64
    assert v3["_split_half_64"] == v4["_split_half_64"]


F_SPLIT_HALF_64 = "a5495c68779bb67059cade18b3a92aaf7cf7fd0200f1770b038d8c5d0e62703c"  # critère v8, § 2 ; constante du programme v4


def test_i_empreinte_egale_a_la_constante_du_programme_de_comparaison_copie_reelle():
    from controle_ia.neuron_lens import comparer_reajustement_v4 as cmp
    texte = (RACINE / "src/controle_ia/neuron_lens/b_beta_lancer_v4.py").read_text(encoding="utf-8")
    assert cmp.empreinte_fonction(texte) == cmp.REFERENCES["fonction"] == F_SPLIT_HALF_64


def test_k_ancre_et_constantes_de_la_v3_egales():
    """(k) Lentille publique épinglée par révision et vérifiée par empreinte (critère v8, K2) ; constantes que lit la partie 2 v3."""
    from controle_ia.neuron_lens import b_beta_lancer_v3 as L3
    assert L.REVISION_NEURONPEDIA == L3.REVISION_NEURONPEDIA == "d2527c3cdbaa60dd4b65cbca1604921f044e989a"
    assert L.LENTILLES_NP["npR"][1] == "a63a1588f2cb61850c68131a5f13b74590f4fe137f67bf80c627547d2230d31c"
    for nom in ("LENTILLES_NP", "MODELE_FICHIERS", "CORRECTIFS", "ESSAIS", "PIECES", "VOISIN_AVANT", "VOISIN_APRES", "COMMIT_VOISIN",
                "ARBRE_VOISIN", "REVISION_LLAMA", "LLAMA", "SPECS", "EXPORTS", "DOCS_CORPUS", "N_ESSAIS_VERDICTS"):
        assert getattr(L, nom) == getattr(L3, nom), nom
    assert L.cb is L3.cb  # même module de contrôles importé (`ecart_max`, `ecarts_identite`, `ecarts_npr`)
    assert set(L3.ETAPES) <= set(L.ETAPES) and [e for e in L.ETAPES if e in L3.ETAPES] == list(L3.ETAPES)


def test_i_commentaire_corrige():
    t = (RACINE / "src/controle_ia/neuron_lens/b_beta_lancer_v4.py").read_text(encoding="utf-8")
    assert "jamais lue pour un seuil" not in t and "le critère d'identité du réajustement (v8, § 4) la lit" in t


# ---------------------------------------------------------------- (g) matériel ; `versions` du manifeste égal à celui du 18

def test_g_materiel_sain_et_illisible():
    def faux(cmd, timeout=60):
        if any(a.startswith("--query-gpu") for a in cmd):
            return {"code": 0, "sortie": "NVIDIA H100 80GB HBM3, 570.86.15, 96.00.99.00.01, 81559 MiB, 9.0, 0x233010DE"}
        return {"code": 0, "sortie": "| NVIDIA-SMI 570.86.15   Driver Version: 570.86.15   CUDA Version: 12.8 |"}
    m = L.lire_materiel(faux)
    assert m["modele_carte"] == "NVIDIA H100 80GB HBM3" and m["pilote"] == "570.86.15" and m["cuda_du_pilote"] == "12.8"
    assert m["n_cartes_smi"] == 1 and "torch" in m and m["machine"]["python"]
    assert m["versions"] == L.versions() and m["versions"]["python"]  # (g) versions de la machine : celles que relève le lanceur
    a = L.lire_materiel(lambda cmd, timeout=60: {"code": None, "sortie": "", "erreur": "FileNotFoundError"})
    assert "modele_carte" not in a and a["erreurs"] and a["cuda_du_pilote"] is None  # artefact : noté, rien n'est levé


VERSIONS_18 = {"torch": "2.14.1", "numpy": "2.4.6", "transformers": "5.18.0", "safetensors": "0.8.0", "tokenizers": "0.23.2",
               "huggingface_hub": "1.33.0"}  # critère d'identité v8, § 2 (manifeste du 18, `b90c1514…`), python 3.12.16 à part


def test_g_versions_du_manifeste_egales_a_celles_du_18():
    """(g) Mêmes exigences que la commande v8 : les bibliothèques que le manifeste relève ont les versions du 18 ; aucune autre
    bibliothèque relevée n'est épinglée ; aucun paquet ajouté pour les copies ; l'amorce v4 installe ce fichier et lit python 3.12.16."""
    from controle_ia import manifeste
    texte = (RACINE / "requirements-neuron-lens-b-beta-v2.txt").read_text(encoding="utf-8")
    epingles = dict(l.split("==") for l in texte.splitlines() if "==" in l and not l.startswith("#"))
    releves = {b: epingles[b] for b in manifeste.BIBLIOTHEQUES if b in epingles}
    assert releves == VERSIONS_18
    assert not set(manifeste.BIBLIOTHEQUES) - set(VERSIONS_18) & set(epingles)
    amorce = (RACINE / "scripts/amorce_neuron_lens_b_beta_v5.sh").read_text(encoding="utf-8")
    assert "-r requirements-neuron-lens-b-beta-v2.txt" in amorce and "${PYTHON_ATTENDU:-3.12.16}" in amorce
    assert "pip install" not in amorce.split("# 3. essais")[1]  # rien n'est installé après l'environnement


def test_g_aucun_import_neuf_hors_des_paquets_epingles():
    permis = {"__future__", "argparse", "hashlib", "importlib", "json", "os", "platform", "re", "shutil", "subprocess", "sys", "time",
              "dataclasses", "pathlib", "controle_ia", "torch", "numpy", "huggingface_hub", "neuron_lens", "transformers"}
    for f in ("b_beta_lancer_v4.py", "rangement_lentilles_v1.py"):
        arbre = ast.parse((RACINE / "src/controle_ia/neuron_lens" / f).read_text(encoding="utf-8"))
        noms = {a.name.split(".")[0] for n in ast.walk(arbre) if isinstance(n, ast.Import) for a in n.names}
        noms |= {n.module.split(".")[0] for n in ast.walk(arbre) if isinstance(n, ast.ImportFrom) and n.module}
        assert noms <= permis, (f, noms - permis)


# ---------------------------------------------------------------- (d) copies vérifiées, faux transport

class FauxTransport:
    def __init__(self, prive=True, sha_rendue="vraie", echecs=0, taille_fausse=False):
        self.est_prive, self.sha_rendue, self.echecs, self.taille_fausse = prive, sha_rendue, echecs, taille_fausse
        self.recus, self.stockes, self.n = [], {}, 0

    def prive(self, depot):
        return self.est_prive

    def envoyer(self, chemin_local, chemin_depot, depot, message):
        self.n += 1
        self.recus.append((Path(chemin_local), chemin_depot))
        if self.echecs > 0:
            self.echecs -= 1
            raise ConnectionError("coupure simulée")
        b = Path(chemin_local).read_bytes()
        self.stockes[chemin_depot] = b
        return f"{self.n:040x}"

    def info(self, depot, chemins, revision):
        out = {}
        for c in chemins:
            b = self.stockes.get(c)
            if b is None:
                continue
            s = {"vraie": rg.hashlib.sha256(b).hexdigest(), "fausse": "0" * 64, "absente": None}[self.sha_rendue]
            out[c] = {"taille": len(b) + (1 if self.taille_fausse else 0), "sha256": s}
        return out

    def flux(self, depot, chemin, revision):
        b = self.stockes[chemin]
        for i in range(0, len(b), 3):
            yield b[i:i + 3]


def _fichier(tmp_path, nom, contenu=b"octets d'un fichier d'ajustement"):
    p = tmp_path / nom
    p.write_bytes(contenu)
    return {"local": p, "depot": f"R/{nom}", "sha256": rg.sha256_fichier(p), "taille": len(contenu)}


def test_d_copie_saine_verifiee_a_l_arrivee_sans_copie_sur_le_disque(tmp_path):
    f = _fichier(tmp_path, "r.pt")
    avant = sorted(tmp_path.rglob("*"))
    t = FauxTransport()
    r = rg.envoyer_verifie(t, DEPOT, [f], "essai")
    x = r["fichiers"]["R/r.pt"]
    assert r["toutes_faites"] and x["copie_faite"] and x["essais"] == 1 and re.fullmatch(r"[0-9a-f]{40}", x["revision"])
    assert x["verification"] == "taille et empreinte rendues par la plateforme"
    assert t.recus == [(f["local"], "R/r.pt")] and sorted(tmp_path.rglob("*")) == avant  # envoyé par son chemin, rien d'écrit


def test_d_artefacts_de_la_copie(tmp_path):
    f = _fichier(tmp_path, "r.pt")
    r = rg.envoyer_verifie(FauxTransport(prive=False), DEPOT, [f], "essai")  # dépôt public : aucun envoi
    assert not r["toutes_faites"] and "non privé" in r["refus"] and r["fichiers"]["R/r.pt"]["essais"] == 0
    t = FauxTransport()
    r = rg.envoyer_verifie(t, DEPOT, [f | {"sha256": "f" * 64}], "essai")  # fichier changé depuis son résultat
    assert not r["toutes_faites"] and t.n == 0 and "changé" in r["fichiers"]["R/r.pt"]["erreurs"][0]
    for t in (FauxTransport(sha_rendue="fausse"), FauxTransport(taille_fausse=True), FauxTransport(echecs=5)):
        r = rg.envoyer_verifie(t, DEPOT, [f], "essai")
        x = r["fichiers"]["R/r.pt"]
        assert not x["copie_faite"] and x["essais"] == 3 and t.n == 3, x  # au plus deux reprises
    r = rg.envoyer_verifie(FauxTransport(), "mal forme", [f], "essai")
    assert not r["toutes_faites"] and r["refus"]
    t = FauxTransport()
    t.envoyer = lambda *a: "main"  # révision rendue qui n'est pas un commit entier : aucune copie dite faite (banc d'altérations)
    r = rg.envoyer_verifie(t, DEPOT, [f], "essai")
    assert not r["toutes_faites"] and "révision rendue illisible" in r["fichiers"]["R/r.pt"]["erreurs"][0]


def test_d_reprise_puis_succes_et_empreinte_non_rendue(tmp_path):
    f = _fichier(tmp_path, "r.pt")
    r = rg.envoyer_verifie(FauxTransport(echecs=2), DEPOT, [f], "essai")
    assert r["toutes_faites"] and r["fichiers"]["R/r.pt"]["essais"] == 3
    r = rg.envoyer_verifie(FauxTransport(sha_rendue="absente"), DEPOT, [f], "essai")
    assert r["toutes_faites"] and "relecture en flux exigée" in r["fichiers"]["R/r.pt"]["verification"]
    r = rg.envoyer_verifie(FauxTransport(), DEPOT, [f], "essai", deja={"R/r.pt": 3})  # reprises déjà épuisées dans la course
    assert not r["toutes_faites"] and r["fichiers"]["R/r.pt"]["essais"] == 3 and "3 essai(s)" in r["fichiers"]["R/r.pt"]["erreurs"][-1]


# ---------------------------------------------------------------- (d), (l) : étapes de copie, inventaire, clôture

torch = pytest.importorskip("torch")
D = 4


def ecrire_fit(chemin, lentille="R", graine=0):
    g = torch.Generator().manual_seed(graine)
    cibles = {"R": (("out", 3), ("mid", 4)), "S": (("mid", 4), ("out", 4))}[lentille]
    sums = {(t, h): torch.randn(n, D, D, generator=g) * 466 for t, n in cibles for h in (0, 1)}
    torch.save({"meta": {"lens": lentille}, "state": {"sums": sums, "n_docs": [466, 466]}, "next_doc": 932}, chemin)


def _ajustement_fait(ctx, le, graine=0):
    f = ctx.voisin / "data" / "fits" / cb.FIT_NOMS[le]
    f.parent.mkdir(parents=True, exist_ok=True)
    ecrire_fit(f, le, graine)
    ecrire_resultat(ctx.racine, ctx.manifeste, f"b-beta-ajustement-{le}",
                    {"fichier": f.name, "sha256": rg.sha256_fichier(f), "taille": f.stat().st_size, "etape": f"ajustement-{le}"})
    return f


def _export_fait(ctx):
    sorties = {}
    for spec, (nom, _) in L.EXPORTS.items():
        home = ctx.voisin / "data" / "lenses" / nom
        (home / "c").mkdir(parents=True, exist_ok=True)
        (home / "c" / "manifest.json").write_text(json.dumps({"nom": nom}))
        (home / "c" / "w.safetensors").write_bytes(nom.encode() * 10)
        sorties[spec] = L._empreintes_home(home)
    ecrire_resultat(ctx.racine, ctx.manifeste, "b-beta-export", {"exports": sorties, "etape": "export"})


def test_d_etape_copie_r_saine(ctx):
    _ajustement_fait(ctx, "R")
    _export_fait(ctx)
    ctx.transport = FauxTransport()
    r = L.etape_copie_r(ctx)
    assert r["copie_faite"] and set(r["copie"]["fichiers"]) == {f"R/{cb.FIT_NOMS['R']}"} | {
        f"R/exports/{nom}/c/{x}" for nom, _ in L.EXPORTS.values() for x in ("manifest.json", "w.safetensors")}
    assert all(x["revision"] for x in r["copie"]["fichiers"].values())


def test_d_etape_copie_en_echec_n_arrete_pas_la_course(ctx, monkeypatch):
    _ajustement_fait(ctx, "S")
    ctx.transport = FauxTransport(echecs=99)
    ecrire_resultat(ctx.racine, ctx.manifeste, "b-beta-copie-S", L.etape_copie_s(ctx) | {"etape": "copie-S"})
    assert ctx.lire("copie-S")["copie_faite"] is False  # consigné, aucun arrêt
    inv = json.loads(L.inventaire(ctx).read_text(encoding="utf-8"))
    assert inv["lentilles"]["S"] == "non copiée" and inv["non_copies"] == [f"S/{cb.FIT_NOMS['S']}"]
    assert inv["lentilles"]["R"] == "non réajustée"
    ctx.transport = t = FauxTransport()  # les trois essais permis sont faits : la clôture n'envoie plus rien, et le dit
    assert L.cloture(ctx) == 3 and t.n == 0
    inv = json.loads(sorted((ctx.diag / "inventaire").glob("inventaire-*.json"))[-1].read_text(encoding="utf-8"))
    assert inv["clos"] is True and inv["non_copies"] == [f"S/{cb.FIT_NOMS['S']}"]


def test_l_cloture_copie_ce_qui_reste_puis_inventaire_clos(ctx):
    _ajustement_fait(ctx, "R")  # course arrêtée après l'ajustement de R : ni export ni copie
    ctx.transport = FauxTransport()
    assert L.cloture(ctx) == 0
    inv = json.loads(sorted((ctx.diag / "inventaire").glob("inventaire-*.json"))[-1].read_text(encoding="utf-8"))
    assert inv["clos"] and inv["lentilles"] == {"R": "copiée", "S": "non réajustée"} and inv["non_copies"] == []
    assert list(ctx.diag.glob("cloture-1.json"))
    dep, rev, att = rg.attendus_depuis_inventaire(inv)
    assert dep == DEPOT and set(att) == {f"R/{cb.FIT_NOMS['R']}"} and re.fullmatch(r"[0-9a-f]{40}", rev)


def test_l_cloture_reprend_une_copie_restee_sans_essai(ctx):
    _ajustement_fait(ctx, "S")
    ctx.transport = FauxTransport(prive=False)  # dépôt pas encore privé à l'étape : aucun envoi, aucun essai compté
    ecrire_resultat(ctx.racine, ctx.manifeste, "b-beta-copie-S", L.etape_copie_s(ctx) | {"etape": "copie-S"})
    ctx.transport = t = FauxTransport()
    assert L.cloture(ctx) == 0 and t.n == 1
    inv = json.loads(sorted((ctx.diag / "inventaire").glob("inventaire-*.json"))[-1].read_text(encoding="utf-8"))
    assert inv["lentilles"]["S"] == "copiée" and inv["copies"]["S"]["origine"] == ["copie-S", "cloture-1"]


def test_l_cloture_ne_copie_pas_un_ajustement_inacheve(ctx):
    f = ctx.voisin / "data" / "fits" / cb.FIT_NOMS["S"]
    f.parent.mkdir(parents=True, exist_ok=True)
    ecrire_fit(f, "S")  # point de sauvegarde d'un ajustement non fini : aucun résultat d'étape
    ctx.transport = t = FauxTransport()
    assert L.cloture(ctx) == 0 and t.n == 0
    inv = json.loads(sorted((ctx.diag / "inventaire").glob("inventaire-*.json"))[-1].read_text(encoding="utf-8"))
    assert inv["lentilles"]["S"] == "non réajustée" and any(x["chemin"].endswith(cb.FIT_NOMS["S"]) for x in inv["fichiers"])


def test_l_inventaire_neuf_a_chaque_appel_scelle_et_cache(ctx, monkeypatch):
    _ajustement_fait(ctx, "R")
    from controle_ia.scellement import verifier
    a = L.inventaire(ctx)
    n_sha = []
    vrai = L.sha256
    monkeypatch.setattr(L, "sha256", lambda p: n_sha.append(p) or vrai(p))
    b = L.inventaire(ctx)
    assert a.name == "inventaire-001.json" and b.name == "inventaire-002.json" and verifier(a) and verifier(b)
    ja, jb = (json.loads(x.read_text(encoding="utf-8")) for x in (a, b))
    assert [x["sha256"] for x in ja["fichiers"] if x["chemin"].endswith(".pt")] == [rg.sha256_fichier(ctx.voisin / "data/fits" / cb.FIT_NOMS["R"])]
    assert not any(str(p).endswith(".pt") for p in n_sha)  # empreinte reprise : taille et date inchangées
    assert jb["etapes_faites"] == ["ajustement-R"] and not ja["clos"]
    f = ctx.voisin / "data" / "fits" / cb.FIT_NOMS["R"]
    f.write_bytes(f.read_bytes() + b"x")  # artefact : fichier changé → empreinte recalculée
    c = json.loads(L.inventaire(ctx).read_text(encoding="utf-8"))
    assert [x["sha256"] for x in c["fichiers"] if x["chemin"].endswith(".pt")] == [rg.sha256_fichier(f)]


def test_l_inventaire_sans_manifeste_ne_salit_pas_l_arbre(tmp_path):
    _git_jouet(tmp_path)
    c = L.Contexte(tmp_path, "20261123-100000-neuron-lens-b-beta", tmp_path / "hf", go_id=GO, variante="B")
    assert L.inventaire(c) is None and L.cloture(c) == 0
    assert subprocess.run(["git", "-C", str(tmp_path), "status", "--porcelain"], capture_output=True, text=True).stdout == ""


# ---------------------------------------------------------------- relecture au lieu de rangement (session)

def _inventaire_clos(tmp_path, t):
    f = _fichier(tmp_path, "r.pt")
    r = rg.envoyer_verifie(t, DEPOT, [f], "essai")
    inv = {"clos": True, "copies": {"R": {"depot": DEPOT, "fichiers": r["fichiers"]}}}
    p = tmp_path / "inventaire-clos.json"
    p.write_text(json.dumps(inv))
    return p


def test_relecture_saine_en_flux_et_par_la_plateforme(tmp_path):
    t = FauxTransport()
    p = _inventaire_clos(tmp_path, t)
    lignes = []
    assert rg.main(["relire", "--inventaire", str(p), "--cle-nom", "CLE_ESSAI", "--sortie", str(tmp_path / "s.json")], t,
                   {"CLE_ESSAI": "x" * 12}, lignes.append) == 0
    s = json.loads((tmp_path / "s.json").read_text())
    assert s["toutes_egales"] and s["mode"] == "flux" and s["cle_nom"] == "CLE_ESSAI" and "x" * 12 not in json.dumps(s) + "".join(lignes)
    assert rg.main(["relire", "--inventaire", str(p), "--cle-nom", "CLE_ESSAI", "--sortie", str(tmp_path / "s2.json"), "--mode",
                    "plateforme"], t, {"CLE_ESSAI": "x" * 12}, lignes.append) == 0


def test_relecture_artefacts(tmp_path):
    t = FauxTransport()
    p = _inventaire_clos(tmp_path, t)
    args = lambda s: ["relire", "--inventaire", str(p), "--cle-nom", "CLE_ESSAI", "--sortie", str(tmp_path / s)]
    env = {"CLE_ESSAI": "x" * 12}
    t.stockes["R/r.pt"] = t.stockes["R/r.pt"][:-1] + b"?"  # un octet changé au lieu de rangement
    assert rg.main(args("a.json"), t, env, lambda x: None) == 1
    t.stockes.clear()  # fichier absent : relecture impossible = échec, jamais succès
    assert rg.main(args("b.json"), t, env, lambda x: None) == 1
    assert json.loads((tmp_path / "b.json").read_text())["fichiers"]["R/r.pt"]["erreur"]
    assert rg.main(args("b.json"), t, env, lambda x: None) == 2  # sortie présente : on n'écrase jamais
    assert rg.main(args("c.json"), t, {}, lambda x: None) == 2  # clé absente
    inv = json.loads(p.read_text())
    p.write_text(json.dumps(inv | {"clos": False}))
    assert rg.main(args("d.json"), t, env, lambda x: None) == 2  # inventaire non clos
    with pytest.raises(ValueError):
        rg.relire(t, DEPOT, {"R/r.pt": {"sha256": "x", "taille": 1}}, REV1)


# ---------------------------------------------------------------- (m) croquis numérique

def test_m_croquis_sain_deterministe_et_exact(ctx):
    f = _ajustement_fait(ctx, "R")
    _ajustement_fait(ctx, "S", graine=1)
    a, b = L.etape_croquis(ctx), L.etape_croquis(ctx)
    assert a["croquis_fait"] and a["lentilles"] == b["lentilles"] and a["vecteurs_sha256"] == b["vecteurs_sha256"]
    assert set(a["lentilles"]["R"]) == {f"{t}|{n}" for t in ("mid", "out") for n in ("entiere", "paire", "impaire")}
    assert len(a["lentilles"]["R"]["out|entiere"]) == 3 and len(a["lentilles"]["S"]["out|paire"]) == 4
    st = torch.load(f, weights_only=False)["state"]
    m = (st["sums"][("mid", 0)][2].double() + st["sums"][("mid", 1)][2].double()) / 932
    u, v = L.vecteurs_croquis(D, D)
    x = a["lentilles"]["R"]["mid|entiere"]["2"]
    assert abs(x["norme"] - float(torch.linalg.norm(m))) < 1e-9
    assert abs(x["projections"][5] - float(torch.from_numpy(u[5]) @ m @ torch.from_numpy(v[5]))) < 1e-6
    assert a["lentilles"]["R"]["mid|paire"]["2"] != a["lentilles"]["R"]["mid|impaire"]["2"]


def test_m_croquis_artefacts_notes_sans_arret(ctx):
    f = _ajustement_fait(ctx, "R")
    _ajustement_fait(ctx, "S")
    temps = iter(range(0, 10 ** 6, 100))
    ctx.horloge = lambda: next(temps)
    r = L.etape_croquis(ctx, limite_s=250)  # borne de temps : partiel, noté
    assert r["depassement"] and not r["croquis_fait"] and r["lentilles"]["R"]
    ctx.horloge = __import__("time").time
    f.write_bytes(f.read_bytes()[:-1] + bytes([f.read_bytes()[-1] ^ 1]))  # fichier changé depuis son résultat
    r = L.etape_croquis(ctx)
    assert not r["croquis_fait"] and r["erreurs"] and r["erreurs"][0].startswith("R :") and r["lentilles"]["S"]
    assert L.vecteurs_croquis(3, 4)[0].tobytes() == L.vecteurs_croquis(3, 4)[0].tobytes() != L.vecteurs_croquis(4, 4)[0][:, :3].tobytes()


# ---------------------------------------------------------------- (c), (l) dans l'amorce v4 ; (b), (e) ; balayage, clé gardée

def test_b_c_e_l_amorce_v4():
    a = (RACINE / "scripts/amorce_neuron_lens_b_beta_v5.sh").read_text(encoding="utf-8")
    assert "BRANCHE_RESULTATS=${BRANCHE_RESULTATS:-calcul/neuron-lens-reajustement-v1}" in a  # (b)
    assert "TIMEOUT_PIP=${TIMEOUT_PIP_S:-7200}" in a  # (e)
    assert "controle_ia.neuron_lens.b_beta_lancer_v4" in a and "b_beta_lancer_v3 " not in a
    assert "HF_TOKEN retire de la course" not in a and "telecharger-poids ]; then" not in a  # (c) clé gardée
    assert len(re.findall(r"^[^#\n]*unset[^#\n]*\bHF_TOKEN\b", a, re.M)) == 1  # (c) un seul retrait : celui des étapes « sans-jeton »
    assert '[ "$cle" = jeton ] || unset HF_TOKEN' in a  # (c) les étapes « sans-jeton » ne la reçoivent toujours pas
    assert "appel sans-jeton hors-ligne inventaire" in a and "appel jeton en-ligne cloture" in a  # (l)
    assert 'log "COPIE EN ECHEC : ' in a and "code=23" in a  # (l) dernière ligne de la table de destruction


def _quatorze_formes(gh, hf):
    out = {}
    for nom, v in (("gh", gh), ("hf", hf)):
        h = "x-access-token:" + v
        out |= {f"{nom}-{k}": x for k, x in {
            "brute": v, "adresse": quote(v, safe=""), "b64": base64.b64encode(v.encode()).decode(),
            "b64-decale": base64.b64encode(b"ab" + v.encode() + b"cd").decode(), "b64-url": base64.urlsafe_b64encode(b"z" + v.encode()).decode(),
            "entete": base64.b64encode(h.encode()).decode(), "entete-decale": base64.b64encode(b"Basic " + h.encode()).decode()}.items()}
    return out


@pytest.mark.parametrize("nom", sorted(_quatorze_formes("g", "h")))
def test_c_balayage_quatorze_formes_avec_la_cle_gardee(tmp_path, nom):
    """(c) La clé reste dans l'environnement de l'amorce toute la course : le balayage avant chaque poussée la cherche donc à toutes
    les étapes, sous ses sept formes, comme le jeton de poussée (essai à blanc v3 : les mêmes formes injectées après les copies)."""
    from controle_ia.neuron_lens import balayage_arbre_v1 as b
    env = {"GH_TOKEN": "ghp_" + "Ab1" * 12, "HF_TOKEN": "hf_" + "Zy9" * 11}
    forme = _quatorze_formes(env["GH_TOKEN"], env["HF_TOKEN"])[nom]
    (tmp_path / "diag").mkdir()
    (tmp_path / "diag" / "inventaire-007.json").write_text(f'{{"note": "{forme}"}}')
    (tmp_path / "propre.json").write_text("{}")
    assert b.balayer([tmp_path], env) == [str(tmp_path / "diag" / "inventaire-007.json")]
    (tmp_path / "diag" / "inventaire-007.json").write_text("{}")
    assert b.balayer([tmp_path], env) == []


# ---------------------------------------------------------------- (j) arbre propre : dépôt réduit v5 (seul essai écarté sur la machine)

def test_j_depot_reduit_v5_arbre_propre_au_manifeste_copie_reelle(tmp_path):
    """(j) L'arbre réduit v5, construit depuis le commit courant, porte le lanceur v4, le module de rangement, la v3 (constantes de la
    partie 2) et l'amorce v4 ; ce que la course crée avant le manifeste (`.venv`, `voisin`, `voisin-banc`, `originaux`) est ignoré : le
    manifeste y trouve l'arbre propre (`depot_propre` vrai). Artefact : un fichier de plus dans l'arbre le rend sale."""
    import importlib.util

    from controle_ia.gardes import etat_git
    spec = importlib.util.spec_from_file_location("dr4", RACINE / "scripts/depot_reduit_neuron_lens_b_beta_v5.py")
    dr = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dr)
    if subprocess.run(["git", "-C", str(RACINE), "status", "--porcelain", "--", *dr.liste_fichiers()], capture_output=True,
                      text=True).stdout.strip():
        pytest.fail("fichiers de l'arbre réduit non committés : committer, puis rejouer cet essai")
    r = dr.construire("HEAD", tmp_path / "r")
    arbre = tmp_path / "r" / "depot"
    noms = {c for c, _, _ in r["fichiers"]}
    assert {"src/controle_ia/neuron_lens/b_beta_lancer_v4.py", "src/controle_ia/neuron_lens/rangement_lentilles_v1.py",
            "src/controle_ia/neuron_lens/b_beta_lancer_v3.py", "scripts/amorce_neuron_lens_b_beta_v5.sh"} <= noms
    assert "scripts/amorce_neuron_lens_b_beta_v3.sh" not in noms and "scripts/amorce_neuron_lens_b_beta_v4.sh" not in noms
    for d in (".venv/bin", "voisin/neuron-lens", "voisin-banc/neuron-lens", "originaux"):
        (arbre / d).mkdir(parents=True)
        (arbre / d / "f").write_text("x")
    assert etat_git(arbre)["propre"] is True
    reste = arbre / "diag" / "20261123-100000-neuron-lens-b-beta" / "inventaire" / "inventaire-001.json"
    reste.parent.mkdir(parents=True)  # `diag/` existe déjà dans l'arbre réduit (série repère) : défaut de la v1 de ces essais
    reste.write_text("{}")  # artefact : un reste dans l'arbre avant le manifeste (d'où l'inventaire sans manifeste refusé)
    assert etat_git(arbre)["propre"] is False
    reste.unlink()
    _, m = creer_manifeste(arbre, "20261123-100000-neuron-lens-b-beta", {"essai": True}, ["t"])
    assert m["depot_propre"] is True and m["commit"] == r["commit_reduit"]
