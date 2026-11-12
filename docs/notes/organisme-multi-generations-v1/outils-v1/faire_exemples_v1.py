"""Écrit deux pièces d'exemple, sans écraser : les exigences du monde riche (`exigences-monde-riche-v1.json`, valeurs de
`verifier_monde_kimi_v1.EXIGENCES_DEFAUT`) et un devis de monde MR-1 **synthétique, écrit par programme** (graine 424242),
pour montrer la forme attendue de Kimi et le rapport du vérificateur. Ce devis n'est pas le monde de la course.
Concepteur neuf (Claude Opus 5.5), 12 novembre 2026. Lancement : `python3 -I -B faire_exemples_v1.py DOSSIER`."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import monde_riche_outils_v1 as M
import verifier_monde_kimi_v1 as V

d = sys.argv[1]
for nom, obj in (("exigences-monde-riche-v1.json", V.EXIGENCES_DEFAUT),
                 ("exemple-devis-synthetique-v1.json", M.generer_monde_synthetique(424242)[0])):
    p = os.path.join(d, nom)
    if os.path.exists(p):
        sys.exit(f"refus : {p} existe déjà")
    with open(p, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(p)
