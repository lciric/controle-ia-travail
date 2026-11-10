"""Essai différentiel de fermeture de P3-bis, v2 (`scripts/essai_fermeture_p3bis_v2.py` ; texte de P3-bis, brouillon 9,
plan, point 6 ; contre-lecture du code v1, CP-03, CP-07, CP-14), joué entier sur jouet, sur processeur : quatre passages par
issue (« vu », « non vu », « non tranché », « échec ») aux sorties de classe 1 identiques, taille du paquet comprise ; règle
des plages de la longueur comprimée (16 octets) ; contrôle négatif par issue ; contrôles positifs détectés, chacun par son
critère (issue imprimée, code qui dépend de l'issue, paquet non bourré, 4 096 zéros de bourre sous « vu », sommeil de 60 s,
corps non comprimé, fichier de lecture laissé en clair dans un chemin exclu de git) ; second paquet ; graines dérivées
écrites. Puis les comparateurs eux-mêmes (R5) : règle des plages, durée, fichiers laissés (inventaire de l'arbre)."""
import importlib.util
import subprocess
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("essai_fermeture_p3bis_v2", RACINE / "scripts" / "essai_fermeture_p3bis_v2.py")
ef = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ef)


def test_essai_differentiel_de_fermeture_complet(tmp_path):
    sortie = tmp_path / "essai-fermeture-p3bis-v2.txt"
    r = ef.essai(tmp_path / "essai", sortie)
    texte = sortie.read_text(encoding="utf-8")
    assert r["conforme"], texte
    assert texte.rstrip().endswith("ESSAI DIFFÉRENTIEL DE FERMETURE : CONFORME") and "NON CONFORME" not in texte
    base = r["base"]
    assert len(base) == 16 and all(sum(p["issue_visee"] == i for p in base) == ef.PASSAGES_PAR_ISSUE >= 4 for i in ef.ISSUES)
    assert {p["taille"] for p in base} == {ef.ob.TAILLE_PAQUET_LECTURES}
    assert len({p["empreinte"] for p in base}) == 16                                     # sel neuf à chaque passage
    assert ef.regle_zlib(base)["conforme"] and ef.ecart_de_duree(base) < ef.SEUIL_DUREE_S
    for v in ef.VARIANTES:
        ligne = next(x for x in texte.splitlines() if f"contrôle positif « {v} »" in x)
        assert ligne.startswith("CONFORME — ") and f"'{ef.CRITERE_ATTENDU[v]}'" in ligne, ligne
    reste = next(x for x in texte.splitlines() if "« fichier-reste »" in x)
    assert "reste.json" in reste and "`git status --porcelain` (relevé de la v1) sous « vu » : []" in reste   # CP-07
    zeros = next(p for p in r["variantes"]["zeros-bourre"] if p["issue_visee"] == "vu")
    sain = next(p for p in r["variantes"]["zeros-bourre"] if p["issue_visee"] == "non vu")
    assert sain["zlib"] - zeros["zlib"] > 4000                                           # les zéros se compriment
    assert sum(x.startswith("graine de l'issue") for x in texte.splitlines()) == 4 and "spawn_key=(3,)" in texte
    assert not any((tmp_path / "essai").iterdir())                                      # dossiers des passages effacés


def test_essai_refuse_un_dossier_ou_une_sortie_deja_la(tmp_path):
    (tmp_path / "essai").mkdir()
    with pytest.raises(SystemExit, match="R12"):
        ef.essai(tmp_path / "essai", tmp_path / "sortie.txt")
    assert ef.main(["un seul argument"]) == 2


def _p(issue, zlib_, duree=10.0, **k):
    base = {"issue_visee": issue, "code": 0, "sortie": "x", "erreurs": "", "publics": [(x, 1) for x in ef.laisses_attendus()],
            "suivis_modifies": [], "taille": ef.ob.TAILLE_PAQUET_LECTURES, "zlib": zlib_, "duree_s": duree}
    base.update(k)
    return base


def test_regle_des_plages_cas_sain_au_seuil_et_au_dela():
    """Règle du texte (l. 610-613) : plage totale ≤ plus grande plage d'une même issue + 16 octets."""
    sain = [_p("vu", 1000), _p("vu", 1006), _p("non vu", 1003), _p("non vu", 1009)]
    z = ef.regle_zlib(sain)
    assert z["conforme"] and (z["plage_totale"], z["plus_grande_plage_d_une_issue"]) == (9, 6)
    au_seuil = [_p("vu", 1000), _p("vu", 1006), _p("non vu", 1022)]
    assert ef.regle_zlib(au_seuil)["conforme"] and ef.regle_zlib(au_seuil)["depassement"] == 16
    au_dela = [_p("vu", 1000), _p("vu", 1006), _p("non vu", 1023)]
    assert not ef.regle_zlib(au_dela)["conforme"] and "zlib" in ef.constats(au_dela)
    assert ef.constats(sain) == {}


def test_constats_voient_chaque_sortie_de_classe_1_la_taille_les_fichiers_et_la_duree():
    a = _p("vu", 1000)
    for cle, v in (("code", 1), ("sortie", "y"), ("erreurs", "e"), ("suivis_modifies", [" M x"])):
        assert cle in ef.constats([a, _p("non vu", 1000, **{cle: v})])
    assert "taille_fixe" in ef.constats([a, _p("non vu", 1000, taille=10240)])
    laisse = [(x, 1) for x in ef.laisses_attendus()] + [("runs/x/reste.json", 12)]
    assert "publics" in ef.constats([_p("vu", 1000, publics=laisse), _p("non vu", 1000, publics=laisse)])   # même sous
    assert "duree_s" in ef.constats([a, _p("non vu", 1000, duree=40.01)])                                 # les deux
    assert "duree_s" not in ef.constats([a, _p("non vu", 1000, duree=39.9)]) and ef.ecart_de_duree([a]) == 0.0
    assert ef.ecart_de_duree([_p("vu", 1, 10.0), _p("vu", 1, 50.0)]) == 0.0                # même issue : pas un écart


def test_fichiers_laisses_voit_les_chemins_ignores_et_exclus(tmp_path, monkeypatch):
    """CP-07 : l'inventaire de l'arbre voit un fichier sous un chemin ignoré ou exclu, que `git status --porcelain` tait."""
    monkeypatch.setenv("GIT_CEILING_DIRECTORIES", str(tmp_path))
    d = ef.depot_vide(tmp_path / "d")
    assert ef.fichiers_laisses(d) == []
    (d / ".git" / "info" / "exclude").write_text("/runs/l/\n", encoding="utf-8")
    for chemin in ("runs/l/lecture.json", "donnees/r/scores.npz", "libre.txt"):
        (d / chemin).parent.mkdir(parents=True, exist_ok=True)
        (d / chemin).write_text("x" * 5, encoding="utf-8")
    assert ef.fichiers_laisses(d) == [("donnees/r/scores.npz", 5), ("libre.txt", 5), ("runs/l/lecture.json", 5)]
    porcelaine = subprocess.run(["git", "-C", str(d), "status", "--porcelain", "--untracked-files=all"], capture_output=True,
                                text=True, check=True).stdout
    assert porcelaine.strip() == "?? libre.txt"                                         # la v1 ne voyait que celui-ci


def test_graines_derivees_par_issue():
    g = [ef.graine(i) for i in ef.ISSUES]
    assert [x.spawn_key for x in g] == [(0,), (1,), (2,), (3,)] and all(x.entropy == ef.ENTROPIE_JOUET for x in g)
    assert len({tuple(x.generate_state(2).tolist()) for x in g}) == 4
    assert ef.graine("vu").generate_state(2).tolist() == ef.graine("vu").generate_state(2).tolist()   # reproductible
