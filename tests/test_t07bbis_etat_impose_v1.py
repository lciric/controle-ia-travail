"""Essais R5 de `t07bbis.etat_impose_v1` (B bis, plan, point 3 ; « Code neuf », épreuves : état imposé — identité au bit près sous le
modèle nu, sous `S100` et sous `T100`, et artefact ; garde d'équivalence (activations décalées) ; texte décodé ou clé autre :
arrêt ; état d'adaptateur autre que l'état imposé : arrêt), **en mode jouet seulement** : une vraie course jouet de la chaîne de
T0.6 dans un dépôt jetable (`aide_t07bbis_jouet_v1`) ; la série O est recalculée par `t07.repli_recalcul_v1.recalculer`
(réutilisé sans modification)."""
from __future__ import annotations

import shutil

import numpy as np
import pytest

import aide_t07bbis_jouet_v1 as aide
from controle_ia.gardes import GardeArret
from controle_ia.t07 import repli_recalcul_v1 as rr
from controle_ia.t07bbis import commun_v1 as cm
from controle_ia.t07bbis import etat_impose_v1 as ei


@pytest.fixture(scope="module")
def course(tmp_path_factory):
    if not aide.disponible():
        pytest.skip("chaîne de T0.6 absente de ce clone")
    d = aide.course_jouet(tmp_path_factory.mktemp("depot-bbis-etat"))
    dossier_o = d.parent / f"{d.name}-serie-O"
    rapport_o = rr.recalculer(d, aide.RUN, dossier_o)
    ch = ei.charger(d, aide.RUN)
    return d, dossier_o, rapport_o, ch


def test_chemin_impose_trois_cas_sains_au_bit_pres_et_artefact(course):
    d, dossier_o, rapport_o, ch = course
    assert rapport_o["garde_equivalence"]["ecart_max"] == 0.0
    assert set(ch["identite"]) == {"saboteur", "temoin"} and all(x["dose_0_identique"] and x["dose_1_differente"]
                                                                 for x in ch["identite"].values())
    r = ei.eprouver_chemin(ch, dossier_o, cm.Graines(2 ** 100 + 3, reelle=False).rng("bbis/chemin-impose"), n=8)
    assert r["n"] == 6 and all(c["egales"] > 0 and c["differentes"] == 0 for c in r["cas_sains"].values())
    assert r["artefact_H_sous_S100"]["differentes"] > 0
    assert set(r["cas_sains"]) == {"H sous le modèle nu", "S100 sous S100", "T100 sous T100"}


def test_chemin_impose_artefact_serie_o_alteree_arret(course, tmp_path):
    d, dossier_o, _, ch = course
    for cond in ("honnete", "S100", "T100"):
        faux = tmp_path / f"O-altere-{cond}"
        shutil.copytree(dossier_o, faux)
        for f in sorted((faux / "c1").glob(f"{cond}__*.npy")):
            a = np.load(f)
            a.flat[0] = np.float16(a.flat[0] + np.float16(1.0))
            np.save(f, a)
        with pytest.raises(GardeArret, match="chemin de l'état imposé en échec"):
            ei.eprouver_chemin(ch, faux, np.random.default_rng(0), n=6)


def test_series_imposees_jumeau_differe_de_l_origine_et_nu_egal_a_l_origine(course, tmp_path):
    """J100 (textes de S100 sous le modèle nu) diffère de O[S100] ; A100 (textes de H sous l'adaptateur) diffère de O[H] ; une série
    « H sous le modèle nu » écrite par la fonction neuve égale O[H] au bit près ; J_instruit relit les textes de l'instruit sans
    sa consigne (contexte autre : activations différentes de O[saboteur])."""
    d, dossier_o, _, ch = course
    from controle_ia.t06.lanceur_v2 import ActivationsDemi
    specs = {s["serie"]: s for s in cm.series_imposees((0.5, 1.0))}
    for nom in ("J100", "A100", "Jinstruit", "AT", "J50", "A50"):
        act = ActivationsDemi(tmp_path / nom, ch["config"]["couches"])
        r = ei.relire_serie(ch, specs[nom], act.ecrire)
        assert r["episodes"] == 6 and r["actions"] > 0 and r["etat"]["dose"] == specs[nom]["dose"]
    diff = lambda serie, cle: not np.array_equal(np.load(tmp_path / serie / "c1" / f"{cle}.npy"),
                                                 np.load(dossier_o / "c1" / f"{cle}.npy"))
    cles_s = sorted(p.stem for p in (tmp_path / "J100" / "c1").glob("*.npy"))
    assert cles_s and all(c.startswith("S100__") for c in cles_s) and any(diff("J100", c) for c in cles_s)
    cles_h = sorted(p.stem for p in (tmp_path / "A100" / "c1").glob("*.npy"))
    assert cles_h and all(c.startswith("honnete__") for c in cles_h) and any(diff("A100", c) for c in cles_h)
    cles_i = sorted(p.stem for p in (tmp_path / "Jinstruit" / "c1").glob("*.npy"))
    assert cles_i and all(c.startswith("saboteur__") for c in cles_i) and any(diff("Jinstruit", c) for c in cles_i)
    nu = ActivationsDemi(tmp_path / "Hnu", ch["config"]["couches"])
    ei.relire_serie(ch, {"serie": "Hnu", "textes": "honnete", "environnement": "honnete", "adaptateur": None, "dose": 0.0},
                    nu.ecrire)
    assert all(not diff("Hnu", c) for c in cles_h)


def test_etat_impose_artefacts_dose_et_empreinte(course, monkeypatch):
    d, dossier_o, _, ch = course
    with pytest.raises(GardeArret, match="dose 0"):
        ei.imposer_etat(ch, None, 0.5)
    with pytest.raises(GardeArret, match="inconnu"):
        ei.imposer_etat(ch, "autre", 1.0)
    assert ei.imposer_etat(ch, "saboteur", 0.5)["dose"] == 0.5
    monkeypatch.setitem(ch["empreintes"], "saboteur", "0" * 64)       # empreinte de distillation-t06.json autre
    with pytest.raises(GardeArret, match="adaptateurs chargés"):
        ei.imposer_etat(ch, "saboteur", 1.0)


def test_texte_decode_ou_cle_autre_arret(course):
    d, dossier_o, _, ch = course
    tache = ei.taches(ch)[0]
    cle_ep = ("honnete", tache["identifiant"])
    origine = ch["textes"][cle_ep][0]
    try:
        ch["textes"][cle_ep][0] = dict(origine, texte=origine["texte"] + " altéré")
        with pytest.raises(GardeArret, match="texte décodé"):
            ei.rejouer_episode(ch, "honnete", "honnete", tache, 0)
        ch["textes"][cle_ep][0] = dict(origine, cle="honnete__t099__p0")
        with pytest.raises(GardeArret, match="clé reconstruite"):
            ei.rejouer_episode(ch, "honnete", "honnete", tache, 0)
    finally:
        ch["textes"][cle_ep][0] = origine
    with pytest.raises(GardeArret, match="actions écrites"):
        ei.rejouer_episode(ch, "S25", "honnete", tache, 0)


def test_garde_d_equivalence_sain_et_activations_decalees(course, monkeypatch, tmp_path):
    d, dossier_o, rapport_o, _ = course
    assert rapport_o["garde_equivalence"]["actions"] >= 1 and rapport_o["garde_equivalence"]["ecart_max"] == 0.0
    monkeypatch.setattr(rr, "EMPAN_DECALAGE", 1)
    with pytest.raises(GardeArret):
        rr.recalculer(d, aide.RUN, tmp_path / "O-decale")
