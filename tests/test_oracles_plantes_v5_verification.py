"""Lot B1, v3 — essais des remarques de la vérification des corrections (`verification-corrections-lot-b1-v1.md`,
`eb7f1819…`) : 13 (héritage qui tuait des vérités plantées), 14 (mort par vacuité de forme « vrai »), 4 (tête du
registre au manifeste du rejeu). Les chaînes reprennent les sondes `v2_etage2.py` et `v2_chaine.py` du vérificateur.

Rejoués sur la v2 (`OP_PAQUET=oracles_plantes_v2`), les essais des remarques 13 et 14 échouent ; ceux de la
remarque 4 n'y ont pas d'objet (pas de registre au rejeu de la v2) et sont sautés.
"""
import importlib
import json
import os

import numpy as np
import pytest

from controle_ia.gardes import GardeArret

PAQUET = os.environ.get("OP_PAQUET", "oracles_plantes_v5")


def mod(nom):
    return importlib.import_module(f"controle_ia.{PAQUET}.{nom}")


par = mod("parametres")
P, _ = par.charger()
tdm = mod("tests_de_mort")
lignee = mod("lignee")
banque_mod = mod("banque")

TERME_HORS_CAPACITE = {"F1": "vt(1000) > 0", "F2": "pfa_t(OU, 100000) > 0", "F3": "u(1000) > 0"}


@pytest.fixture(scope="module")
def banque11():
    return banque_mod.construire_banque(11, P)


def batterie(m, texte, reg):
    return tdm.appliquer_batterie(tdm.sortie_de_texte(texte), m, registre=reg)


def _corps(texte, k):
    """Corps après les k premiers quantificateurs « pour tout … , »."""
    return texte.split(", ", k)[k]


# ---------------------------------------------------------------- remarque 13, étage 2 (table de vérité)
@pytest.mark.parametrize("w", [8, 9])
@pytest.mark.parametrize("gabarit", ["duplication", "addition"])
def test_r13_etage2_verite_plantee_survit(banque11, tmp_path, w, gabarit):
    m, plantes = banque11[w]
    T = next(p.texte for p in plantes if p.etiquette == "VERITE_PLANTEE" and p.gabarit == gabarit)
    reg = lignee.Registre(tmp_path / "r.jsonl")
    if gabarit == "duplication":
        poison = f"pour tout n dans NAT, ({_corps(T, 1)}) et (w(n - 1) > 0 ou w(n - 1) <= 0)"
    else:
        poison = f"pour tout n dans NAT, pour tout m dans NAT, ({_corps(T, 2)}) et (w(m - 1) > 0 ou w(m - 1) <= 0)"
    assert batterie(m, poison, reg).statut == "morte"
    r = batterie(m, T, reg)
    assert r.statut == "vivante" and r.vraie_bornee


def test_r13_etage2_enonce_vrai_garde_survit(banque11, tmp_path):
    m, _ = banque11[8]
    reg = lignee.Registre(tmp_path / "r.jsonl")
    assert batterie(m, "pour tout n dans NAT, w(n - 1) > 0 ou w(n - 1) <= 0", reg).statut == "morte"
    assert batterie(m, "pour tout n dans NAT, n >= 1 implique (w(n - 1) > 0 ou w(n - 1) <= 0)", reg).statut == "vivante"


# ---------------------------------------------------------------- remarque 13, étage 3 (profil, chaîne non transitive)
@pytest.mark.parametrize("w", [8, 9, 10, 11])
@pytest.mark.parametrize("gabarit", ["periode_modulaire", "cassini"])
def test_r13_etage3_chaine_ne_tue_pas_la_verite(banque11, tmp_path, w, gabarit):
    m, plantes = banque11[w]
    T = next(p.texte for p in plantes if p.etiquette == "VERITE_PLANTEE" and p.gabarit == gabarit)
    c = _corps(T, 1)
    reg = lignee.Registre(tmp_path / "r.jsonl")
    assert batterie(m, f"pour tout n dans NAT, ({c}) et n != 2", reg).statut == "morte"
    batterie(m, f"pour tout n dans NAT, ({c}) et (n != 2 ou u(1000) > 0)", reg)  # hors capacité en n = 2
    assert batterie(m, T, reg).statut == "vivante"


def test_r13_cas_sain_heritage_toujours_actif(banque11, tmp_path):
    # un piège tué par T6, et ses reformulations fausses au témoin, héritent toujours de la mort
    m, plantes = banque11[8]
    pg = next(p for p in plantes if p.etiquette == "PIEGE" and p.gabarit == "seuil_u")
    reg = lignee.Registre(tmp_path / "r.jsonl")
    r = batterie(m, pg.texte, reg)
    n0 = int(pg.instance["n"])
    s = json.dumps({"verdict": "faux", "contre_exemples": [{"n": n0}], "raison": "essai"})
    assert tdm.appliquer_t6(s, r.arbre, m, reg).tue()
    c = pg.texte.split("< ")[1]
    for t in (f"pour tout k dans NAT, u(k) <= {c} - 1", f"pour tout n dans NAT, 2 * u(n) < 2 * {c}",
              f"pour tout n dans NAT, u(n) < {c} et u(n) >= 0"):
        r2 = batterie(m, t, reg)
        assert r2.statut == "morte" and r2.issues[-1].type == tdm.TypeIssue.MORTE_PAR_HERITAGE, t


# ---------------------------------------------------------------- remarque 13, invariant sur un registre adverse
def _mutants(m, texte):
    """Variantes adverses d'une vérité : mortes jusqu'à N, ou hors capacité, de même squelette ou de même corps."""
    pre = texte.count("pour tout ")
    corps = _corps(texte, pre) if pre else texte
    tete = texte[: len(texte) - len(corps)]
    var = next((tok.split(" dans")[0] for tok in texte.split("pour tout ")[1:] if " dans NAT" in tok), None)
    h = TERME_HORS_CAPACITE[m.famille]
    sortie = [f"{tete}({corps}) et {h}", f"{tete}({corps}) ou faux", f"{tete}({corps}) et (vrai ou {h})"]
    if var is not None:
        for k in sorted({0, 1, 2, m.N}):
            sortie += [f"{tete}({corps}) et {var} != {k}", f"{tete}({corps}) et ({var} != {k} ou {h})",
                       f"{tete}({corps}) et ({var} != {k} ou faux)"]
    return sortie


def _remplir_registre_adverse(banque, reg, racine):
    base = mod("base_aleatoire")
    rng = np.random.default_rng(np.random.SeedSequence(racine, spawn_key=(77,)))  # graine d'essai, hors de l'arbre
    for m, plantes in banque:
        cfg = dict(P["base_aleatoire"], par_monde=40)
        for t in base.tirer_base(rng, m, cfg):  # mortes et vivantes tirées au hasard dans la grammaire
            batterie(m, t, reg)
        for p in plantes:
            if p.etiquette in ("VERITE_PLANTEE", "FAUX_TOT", "PIEGE"):
                for t in _mutants(m, p.texte):
                    batterie(m, t, reg)


@pytest.mark.parametrize("racine", [11, 20261122])
def test_r13_invariant_aucune_verite_plantee_ne_meurt_par_heritage(tmp_path, racine):
    banque = banque11_ou(racine)
    reg = lignee.Registre(tmp_path / "r.jsonl")
    _remplir_registre_adverse(banque, reg, racine)
    assert sum(1 for d in reg.lignes if d["statut"] == "morte") > 300  # le registre est bien rempli de mortes
    tuees = []
    for m, plantes in banque:  # puis toute la banque est soumise
        for p in plantes:
            r = batterie(m, p.texte, reg)
            if p.etiquette == "VERITE_PLANTEE" and r.statut != "vivante":
                tuees.append((m.indice, p.gabarit, r.issues[-1].motif))
            if p.etiquette == "PIEGE":
                assert r.statut == "vivante" or r.issues[-1].type == tdm.TypeIssue.MORTE_PAR_HERITAGE
    assert tuees == []


_BANQUES = {}


def banque11_ou(racine):
    if racine not in _BANQUES:
        _BANQUES[racine] = banque_mod.construire_banque(racine, P)
    return _BANQUES[racine]


# ---------------------------------------------------------------- remarque 14 : mort par vacuité de forme « vrai »
def test_r14_vacuite_n_empoisonne_pas_les_triviales(banque11, tmp_path):
    m, _ = banque11[8]
    reg = lignee.Registre(tmp_path / "r.jsonl")
    assert batterie(m, "pour tout n dans NAT, n > N + 5 implique 0 = 0", reg).statut == "morte"
    for t in ("pour tout n dans NAT, n + 1 > n", "1 = 1"):
        r = batterie(m, t, reg)
        assert r.statut == "vivante" and r.triviale, t


def test_r14_cas_sain_la_vacuite_tue_toujours(banque11, tmp_path):
    m, _ = banque11[8]
    reg = lignee.Registre(tmp_path / "r.jsonl")
    batterie(m, "pour tout n dans NAT, n > N + 5 implique 0 = 0", reg)
    assert batterie(m, "pour tout k dans NAT, k > N + 5 implique 1 = 1", reg).statut == "morte"


# ---------------------------------------------------------------- remarque 4 : tête du registre au manifeste du rejeu
@pytest.fixture(scope="module")
def rejeu_v3(tmp_path_factory):
    if PAQUET == "oracles_plantes_v2":
        pytest.skip("la v2 ne tient pas de registre au rejeu")
    d = tmp_path_factory.mktemp("rejeu") / "a"
    code, rapport = mod("rejeu").executer(11, d)
    return d, code, rapport


def test_r4_tete_consignee_et_verifiee(rejeu_v3):
    d, code, _ = rejeu_v3
    assert code == 0
    m = json.loads((d / "manifeste-rejeu-v5.json").read_text(encoding="utf-8"))
    tete = mod("rejeu").verifier_tete_manifeste(d)
    assert tete["lignes"] == m["tete_registre_lignee"]["lignes"] >= 312
    assert (d / "lignee-rejeu-v5.jsonl.sha256").exists()


def test_r4_registre_reecrit_avec_sa_tete_refuse(rejeu_v3, tmp_path):
    import shutil
    d, _, _ = rejeu_v3
    copie = tmp_path / "c"
    shutil.copytree(d, copie)
    ch = copie / "lignee-rejeu-v5.jsonl"
    lignes = ch.read_text(encoding="utf-8").splitlines()
    ch.write_text("\n".join(lignes[:-1]) + "\n", encoding="utf-8")  # dernière ligne retirée…
    import hashlib  # …et tête réécrite en accord : le registre seul ne voit rien
    der = hashlib.sha256(lignes[-2].encode("utf-8")).hexdigest()
    (copie / "lignee-rejeu-v5.jsonl.tete.json").write_text(json.dumps({"lignes": len(lignes) - 1, "derniere": der}) + "\n",
                                                           encoding="utf-8")
    assert lignee.Registre(ch).tete()["lignes"] == len(lignes) - 1
    with pytest.raises(GardeArret):
        mod("rejeu").verifier_tete_manifeste(copie)


# ---------------------------------------------------------------- remarque 13 bis (balayage v3) : collision entre mondes
def test_r13bis_meme_forme_dans_deux_mondes_ni_mort_ni_arret(tmp_path):
    # racine 19 : le faux tôt « croissance sans QU » du monde 9 et la vérité de croissance du monde 10 ont la même
    # forme normale (constantes substituées) ; le registre est commun à toute la banque
    banque = banque11_ou(19)
    (m9, p9), (m10, p10) = banque[9], banque[10]
    # v5 : ces deux gabarits ne sont plus plantés ; les textes sont écrits ici, sur les mêmes mondes
    ft = "pour tout n dans NAT, u(n) <= max(U0, U1) * PU^n"
    vr = "pour tout n dans NAT, u(n) <= max(U0, U1) * (PU + QU)^n"
    nm = mod("normalisation")
    assert nm.normaliser(m9.analyser(ft), m9, m9.ev).empreinte == nm.normaliser(m10.analyser(vr), m10, m10.ev).empreinte
    reg = lignee.Registre(tmp_path / "r.jsonl")
    assert batterie(m9, ft, reg).statut == "morte"
    r = batterie(m10, vr, reg)
    assert r.statut == "vivante" and r.vraie_bornee
