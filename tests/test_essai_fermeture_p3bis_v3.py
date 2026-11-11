"""Essai différentiel de fermeture de P3-bis, v3 (`scripts/essai_fermeture_p3bis_v3.py`) : la v2 jouée sur la chaîne fermée de
la règle (a') (`ouverture_p3bis_v3`, lecture complémentaire `lecture_p3bis_v2`) et sur des runs fabriqués à 800 directions.
Essais : comparaison ligne à ligne au script v2 (seuls les remplacements déclarés) ; essai complet joué sur jouet (quatre
passages par issue aux sorties de classe 1 identiques, contrôles positifs détectés, second paquet), comme l'essai de la v2
(`tests/test_essai_fermeture_p3bis_v2.py`, dont les essais des comparateurs valent pour la v3 : mêmes fonctions)."""
import difflib
import importlib.util
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("essai_fermeture_p3bis_v3", RACINE / "scripts" / "essai_fermeture_p3bis_v3.py")
ef = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ef)

REMPLACEMENTS = [
    ('"""Essai différentiel de fermeture de P3-bis, v2, sur jouet, sur processeur, 0 USD, avant la création de l\'instance.', None),
    ("from controle_ia.premier_test_ia import ouverture_p3bis_v2 as ob  # noqa: E402",
     "from controle_ia.premier_test_ia import ouverture_p3bis_v3 as ob  # noqa: E402"),
    ("N_TACHES, T_PAS, N_PLANCHER, L_JETONS, D_SIGNAL = 8, 4, 20, 6, 2.5",
     "N_TACHES, T_PAS, N_PLANCHER, L_JETONS, D_SIGNAL = 8, 4, 800, 6, 2.5"),
    ('           "src/controle_ia/premier_test_ia/ouverture_p3bis_v2.py", "scripts/essai_fermeture_p3bis_v2.py")', None),
    ('          "from controle_ia.premier_test_ia import ouverture_p3bis_v2 as ob\\nETAT = {}\\nCODE = lambda c: c\\n"',
     '          "from controle_ia.premier_test_ia import ouverture_p3bis_v3 as ob\\nETAT = {}\\nCODE = lambda c: c\\n"'),
    ('        commande = [sys.executable, "-m", "controle_ia.premier_test_ia.ouverture_p3bis_v2", *args]',
     '        commande = [sys.executable, "-m", "controle_ia.premier_test_ia.ouverture_p3bis_v3", *args]'),
    ("    ecrire(f\"Essai différentiel de fermeture de P3-bis, v2 — {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}\")",
     "    ecrire(f\"Essai différentiel de fermeture de P3-bis, v3 — {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}\")"),
    ('        print("usage : essai_fermeture_p3bis_v2.py DOSSIER_NEUF SORTIE.txt", file=sys.stderr)',
     '        print("usage : essai_fermeture_p3bis_v3.py DOSSIER_NEUF SORTIE.txt", file=sys.stderr)'),
]
MODULES_V3 = ['           "src/controle_ia/premier_test_ia/lecture_p3bis_v2.py", "src/controle_ia/t07/plancher_v2.py",',
              '           "src/controle_ia/premier_test_ia/ouverture_p3bis_v3.py", "scripts/essai_fermeture_p3bis_v3.py")']


def test_v3_egal_au_script_v2_hors_des_remplacements_declares():
    a = (RACINE / "scripts" / "essai_fermeture_p3bis_v2.py").read_text(encoding="utf-8").splitlines()
    b = (RACINE / "scripts" / "essai_fermeture_p3bis_v3.py").read_text(encoding="utf-8").splitlines()
    retirees = [x[2:] for x in difflib.ndiff(a, b) if x.startswith("- ")]
    ajoutees = [x[2:] for x in difflib.ndiff(a, b) if x.startswith("+ ")]
    assert retirees == [x for x, _ in REMPLACEMENTS]
    en_tete = ajoutees[:8]
    assert en_tete[0].startswith('"""Essai différentiel de fermeture de P3-bis, v3,') and en_tete[-1] == REMPLACEMENTS[0][0][3:]
    reste = ajoutees[8:]
    attendu = [y for _, y in REMPLACEMENTS[1:3]] + MODULES_V3 + [y for _, y in REMPLACEMENTS[4:]]   # 1re ligne de MODULES gardée
    assert reste == attendu
    assert ef.N_PLANCHER == 800 and ef.ob.__name__ == "controle_ia.premier_test_ia.ouverture_p3bis_v3"
    assert all((RACINE / m).is_file() for m in ef.MODULES)


def test_essai_differentiel_de_fermeture_v3_complet(tmp_path):
    sortie = tmp_path / "essai-fermeture-p3bis-v3.txt"
    r = ef.essai(tmp_path / "essai", sortie)
    texte = sortie.read_text(encoding="utf-8")
    assert r["conforme"], texte
    assert texte.rstrip().endswith("ESSAI DIFFÉRENTIEL DE FERMETURE : CONFORME") and "NON CONFORME" not in texte
    base = r["base"]
    assert len(base) == 16 and all(p["issue_lue"] == p["issue_visee"] for p in base)
    assert {p["taille"] for p in base} == {ef.ob.TAILLE_PAQUET_LECTURES} and len({p["empreinte"] for p in base}) == 16
    for v in ef.VARIANTES:
        ligne = next(x for x in texte.splitlines() if f"contrôle positif « {v} »" in x)
        assert ligne.startswith("CONFORME — ") and f"'{ef.CRITERE_ATTENDU[v]}'" in ligne, ligne
    assert "fichier essayé : src/controle_ia/premier_test_ia/lecture_p3bis_v2.py" in texte
    assert not any((tmp_path / "essai").iterdir())
