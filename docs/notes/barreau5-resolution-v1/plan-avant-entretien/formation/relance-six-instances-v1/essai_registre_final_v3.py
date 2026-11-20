"""Essai du registre final : le registre propre de la branche principale, à l'octet, plus la ligne de relance de
l'additif 1, lu par le code dont `src` est sur le chemin. Usage : python essai_registre_final_v3.py REGISTRE COMMIT QUI
(QUI : « lecture » pour le code de lecture figé, « relances » pour le code des relances)."""
import hashlib
import sys
from pathlib import Path

from controle_ia.barreau5_familles import engagement_v1 as en
from controle_ia.gardes import GardeArret

registre, commit, qui = Path(sys.argv[1]).read_text(encoding="utf-8"), sys.argv[2], sys.argv[3]
assert registre.endswith("\n")
ligne = ("| GO-RELANCE-FORMATION-B5F | 2026-11-20T16:00:00Z | GO-2026-11-19-86 ; instances 1,2,3,4,5,7 | mot de Lazar "
         "GO-2026-11-20-51 ; écarts accordés GO-2026-11-20-59 (2) et GO-2026-11-20-60 (2) ; additif 1 scellé (essai) ; "
         f"code des relances commit {commit} ; cumul commun relevé (essai) ; enveloppe GO-2026-11-19-87 non employée |\n")
final = registre + ligne
print(f"[{qui}] engagement_v1.py sha256 {hashlib.sha256(Path(en.__file__).read_bytes()).hexdigest()}")
print(f"[{qui}] registre final sha256 {hashlib.sha256(final.encode()).hexdigest()} ; clés lues :",
      ", ".join(en.lignes_du_registre(final)))
if qui == "lecture":
    from controle_ia.barreau5_familles import lecture_v1 as lv

    print(f"[{qui}] relance lue par lecture_v1.relance_du_registre :", lv.relance_du_registre(final))
    try:
        lv.relance_du_registre(final + f"| CODE-RELANCE-FORMATION-B5F | 2026-11-20T16:00:01Z | commit {commit} | |\n")
        print(f"[{qui}] ARTEFACT ACCEPTÉ : une clé neuve passe")
        sys.exit(1)
    except GardeArret as e:
        print(f"[{qui}] artefact (clé neuve) refusé :", e)
else:
    from controle_ia.barreau5_familles import formation_v1 as fv

    lu = fv.lire_code_et_accord(None, final)
    print(f"[{qui}] relance lue par formation_v1.lire_code_et_accord :", lu["relance"])
    print(f"[{qui}] code des premières marches {lu['commit']} ; entropie inchangée : {lu['entropie'] > 0} ; "
          f"commit_du_code(relance) = {fv.commit_du_code(lu, True)}")
    assert lu["relance"] == {"go_id": "GO-2026-11-19-86", "instances": [1, 2, 3, 4, 5, 7], "commit": commit}
