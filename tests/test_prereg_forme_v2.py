"""Règles de forme du gabarit v2 (proposition retenue 4 du collisionneur groupé, GO-2026-11-24-46).

Témoin vrai : un préenregistrement complet passe. Témoin faux : le même sans analyse de puissance ni comparateur
apparié est refusé (R5 : garde testée sur un cas sain et sur un artefact)."""
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.prereg import (REGLES_FORME, SECTIONS, problemes, problemes_forme, sceller_prereg_v2)

RACINE = Path(__file__).resolve().parents[1]
EMPREINTES = f"brouillon relu `{'a' * 64}`, rapport `{'b' * 64}`"


def ecrire(chemin, regles=None):
    regles = regles if regles is not None else {r: f"mise en œuvre déclarée pour {r.lower()}" for r in REGLES_FORME}
    corps = ["# Préenregistrement test v2\n"]
    for s in SECTIONS:
        if s == "Critères de lecture gelés":
            lignes = "\n".join(f"- **{r}** : {v}" for r, v in regles.items())
            corps.append(f"## Règles de forme\n\n{lignes}\n")
        corps.append(f"## {s}\n\ncontenu {s}" + (" ; " + EMPREINTES if s == "Contre-lecture" else "") + "\n")
    chemin.write_text("\n".join(corps), encoding="utf-8")
    return chemin


def test_temoin_vrai_complet_passe(tmp_path):
    p = ecrire(tmp_path / "p.md")
    assert problemes(p) == [] and problemes_forme(p) == []
    assert len(sceller_prereg_v2(p)) == 64


def test_temoin_faux_sans_puissance_ni_comparateur_refuse(tmp_path):
    regles = {r: f"mise en œuvre déclarée pour {r.lower()}" for r in REGLES_FORME}
    del regles["Effectif par analyse de puissance"]
    regles["Comparateur apparié"] = "À REMPLIR"
    p = ecrire(tmp_path / "p.md", regles)
    pb = problemes_forme(p)
    assert any(x.startswith("règle de forme absente") and x.endswith(": Effectif par analyse de puissance") for x in pb)
    assert "règle de forme vide ou à remplir : Comparateur apparié" in pb
    with pytest.raises(GardeArret):
        sceller_prereg_v2(p)
    assert not (tmp_path / "p.md.sha256").exists()


def test_sans_objet_avec_et_sans_raison(tmp_path):
    regles = {r: f"mise en œuvre déclarée pour {r.lower()}" for r in REGLES_FORME}
    regles["Amputation placebo"] = "sans objet : aucune redécouverte de primitive ici"
    assert problemes_forme(ecrire(tmp_path / "a.md", regles)) == []
    regles["Amputation placebo"] = "sans objet :"
    assert problemes_forme(ecrire(tmp_path / "b.md", regles)) == [
        "règle de forme « sans objet » sans raison : Amputation placebo"]
    regles["Amputation placebo"] = "oui"
    assert problemes_forme(ecrire(tmp_path / "c.md", regles)) == [
        "règle de forme trop courte ou bouche-trou : Amputation placebo"]


def test_section_absente_et_doublon(tmp_path):
    p = tmp_path / "v1.md"
    p.write_text("# t\n\n## Hypothèse\n\nx\n", encoding="utf-8")
    assert problemes_forme(p) == ["section absente : Règles de forme"]
    regles = {r: f"mise en œuvre déclarée pour {r.lower()}" for r in REGLES_FORME}
    q = ecrire(tmp_path / "d.md", regles)
    q.write_text(q.read_text(encoding="utf-8").replace(
        "## Règles de forme\n\n", "## Règles de forme\n\n- **Unité indépendante** : encore une autre ligne ici\n"),
        encoding="utf-8")
    assert "règle de forme en double : Unité indépendante" in problemes_forme(q)


def test_gabarit_v2_vierge_refuse_et_v1_inchange():
    g2 = RACINE / "prereg" / "gabarit-preregistrement-v2.md"
    pb = problemes_forme(g2)
    assert len(pb) == len(REGLES_FORME) and all("vide ou à remplir" in x for x in pb)
    assert "section absente : Règles de forme" in problemes_forme(RACINE / "prereg" / "gabarit-preregistrement-v1.md")


def _regles():
    return {r: f"mise en œuvre déclarée pour {r.lower()}" for r in REGLES_FORME}


def test_contre_lecture_1_cas_limites(tmp_path):
    """Remarques 2 à 6 et mineures de la contre-lecture du code des règles de forme (v1)."""
    base = ecrire(tmp_path / "b.md").read_text(encoding="utf-8")

    def variante(nom, ancien, nouveau):
        q = tmp_path / nom
        assert ancien in base
        q.write_text(base.replace(ancien, nouveau, 1), encoding="utf-8")
        return problemes_forme(q)

    r = "- **Comparateur apparié** : mise en œuvre déclarée pour comparateur apparié"
    # 2 : multiligne accepté ; marqueur en continuation vu
    assert variante("m1.md", r, "- **Comparateur apparié** :\n  même capacité, même budget de requêtes") == []
    assert variante("m2.md", r, r + "\n  À REMPLIR plus tard") == ["règle de forme vide ou à remplir : Comparateur apparié"]
    # 3 : variantes typographiques tolérées
    assert variante("t1.md", r, "* **Comparateur apparié :** même capacité, même budget") == []
    assert variante("t2.md", r, "1. **comparateur APPARIÉ** : même capacité, même budget") == []
    l = "- **Lot d'étalonnage distinct** : mise en œuvre déclarée pour lot d'étalonnage distinct"
    assert variante("t3.md", l, l.replace("d'é", "d’é", 1)) == []
    import unicodedata
    assert variante("t4.md", r, unicodedata.normalize("NFD", r)) == []
    # 4 : casse du marqueur
    assert variante("c1.md", r, "- **Comparateur apparié** : à remplir plus tard svp") == [
        "règle de forme vide ou à remplir : Comparateur apparié"]
    # 5 : bouche-trous
    for creux in ("n/a n/a n/a", "TODO TODO TODO"):
        assert variante("f.md", r, f"- **Comparateur apparié** : {creux}") == [
            "règle de forme trop courte ou bouche-trou : Comparateur apparié"]
    # 6 : seconde occurrence vide vue
    pb = variante("d.md", r, r + "\n- **Comparateur apparié** :")
    assert "règle de forme en double : Comparateur apparié" in pb
    assert "règle de forme vide ou à remplir : Comparateur apparié" in pb
    # mineures : tiret long, « sans objet » nu, section en double
    a = "- **Amputation placebo** : mise en œuvre déclarée pour amputation placebo"
    assert variante("s1.md", a, "- **Amputation placebo** : sans objet — aucune primitive redécouverte ici") == []
    assert variante("s2.md", a, "- **Amputation placebo** : sans objet") == [
        "règle de forme « sans objet » sans raison : Amputation placebo"]
    assert "section en double : Règles de forme" in variante(
        "s3.md", "## Hypothèse", "## Règles de forme\n\n- **Unité indépendante** : x y z\n\n## Hypothèse")


def test_exiger_prereg_scelle_v2(tmp_path):
    from controle_ia.prereg import exiger_prereg_scelle_v2
    from controle_ia.scellement import sceller
    p = ecrire(tmp_path / "ok.md")
    sceller_prereg_v2(p)
    assert len(exiger_prereg_scelle_v2(p)) == 64
    regles = _regles()
    regles["Unité indépendante"] = "TODO TODO TODO"
    q = ecrire(tmp_path / "ko.md", regles)
    sceller(q)                                   # scellé par la voie v1, qui ignore les règles de forme
    with pytest.raises(GardeArret):
        exiger_prereg_scelle_v2(q)
