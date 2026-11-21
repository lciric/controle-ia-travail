# Remplit par programme les huit champs de l'ordre de l'étalonnage du saboteur à budget v5
# (brouillon 8 -> version à sceller v1). Écrit par la mère, 2026-11-21. Aucun autre changement.
import hashlib, pathlib, sys

src = pathlib.Path(sys.argv[1]); dst = pathlib.Path(sys.argv[2])
assert not dst.exists(), "on n'écrase jamais"
b = src.read_bytes()
assert hashlib.sha256(b).hexdigest() == "55de7ac17d27514a4110682c6e46bcace0540291bbb14853aaaaae5614d41a20", "brouillon 8 attendu"
t = b.decode()
champs = {
    "<<BRANCHE_CODE_V5>>": "prep/iib-code-v5",
    "<<COMMIT_CODE_REVU_POUSSE>>": "62356e2ff612a8228b37a8333689e8114099f3c0",
    "<<COMMIT_LANCEMENT_ETALONNAGE>>": "b2d568c459a9479c2465c7fc74a69287da884e69",
    "<<CONFIG_ETALONNAGE_CHEMIN_ET_EMPREINTE>>": "docs/notes/barreau8-iib-v1/config-iib-organisme-retenu-v5-etalonnage-v1.json (a7c6f3948a1d44e2cd7476a8adf4855bb06b5b63d66fa8870ff80a95be0b23cb)",
    "<<FICHIER_ENTREES_CHEMIN_ET_EMPREINTE>>": "docs/notes/barreau8-iib-v1/entrees-iib-organisme-retenu-v5-etalonnage-v1.json (44f90de6e4b46b2931f2d0aa7fb7cbd614c5331be5859cf2ecb2a3ad0d09c74d)",
    "<<INSTANCES_INTOUCHABLES>>": "58936096,58936099,58936100,60988826",
    "<<ETIQUETTE_ETALONNAGE>>": "iib-explo-v5",
    "<<SORT_DE_LA_MACHINE_APRES_ETALONNAGE>>": (
        "garde à l'arrêt pour la course sous son ordre à part, dans les bornes de ce point "
        "(48 heures d'arrêt au plus, destruction avant 2026-12-01T00:00:00Z) ; si aucun ordre de course "
        "n'est scellé à 40 heures d'arrêt, destruction après le rapatriement vérifié et la désignation "
        "scellée, sur le mot de la mère"),
}
for k, v in champs.items():
    assert t.count(k) >= 1, k
    t = t.replace(k, v)
assert "<<" not in t and ">>" not in t, "champ restant"
entete = (
    "> **Version à sceller v1, remplie par programme par la mère** (`remplir_ordre_iib_v5_v1.py`) depuis le brouillon 8 "
    "(55de7ac1…) ; seuls les huit champs du § 11 changent ; mot de Lazar sur la première action : GO-2026-11-21-84 ; "
    "commit de lancement b2d568c4…, contrôles à blanc conformes (compte rendu 7 de l'exécutante, 21:00:55Z).\n\n")
dst.write_text(entete + t)
print(hashlib.sha256(dst.read_bytes()).hexdigest())
