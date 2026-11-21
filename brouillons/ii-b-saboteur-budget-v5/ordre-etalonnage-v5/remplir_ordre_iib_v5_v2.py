# Remplit par programme les huit champs de l'ordre de l'étalonnage du saboteur à budget v5
# (ordre v2 brouillon 3 -> version v2 à sceller). Écrit par la mère, 2026-11-21. Aucun autre changement.
import hashlib, pathlib, sys

src = pathlib.Path(sys.argv[1]); dst = pathlib.Path(sys.argv[2])
assert not dst.exists(), "on n'écrase jamais"
b = src.read_bytes()
assert hashlib.sha256(b).hexdigest() == "3ec3a60523bbf45c0f345c91d5bdf8e20e9bb220b39a78efa93ea7c57420cc6f", "ordre v2 brouillon 3 attendu"
t = b.decode()
champs = {
    "<<BRANCHE_CODE_V5>>": "prep/iib-code-v5-r2",
    "<<COMMIT_CODE_REVU_POUSSE>>": "2abe5e6b073512f4bd6091da29426f88cdcd2a93",
    "<<COMMIT_LANCEMENT_ETALONNAGE>>": "43d6d0673edd5055917f536e5310ea99c15ab75e",
    "<<CONFIG_ETALONNAGE_CHEMIN_ET_EMPREINTE>>": "docs/notes/barreau8-iib-v1/config-iib-organisme-retenu-v5-etalonnage-v2.json (08e22099d3be9bb8313610379f71ddafaf0e5d77117a1c9cbaadb457304dd363)",
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
    "> **Ordre v2, version scellée, remplie par programme par la mère** (`remplir_ordre_iib_v5_v2.py`) depuis le brouillon 3 de la v2 "
    "(3ec3a605…) ; seuls les huit champs du § 11 changent ; mots de Lazar : GO-2026-11-21-84 (première action), GO-2026-11-21-87 (relance) ; "
    "commit de lancement 43d6d067…, code revu 2abe5e6b… (correctifs 0011 et 0012), contrôles à blanc de l'exécutante.\n\n")
dst.write_text(entete + t)
print(hashlib.sha256(dst.read_bytes()).hexdigest())
