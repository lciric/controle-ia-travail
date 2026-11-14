"""Écrit les couples du brouillon 6 « validité de l'adaptateur » (R12 : refuse d'écraser).

Usage : python3 -I faire-couples-brouillon6-v1.py DATE_UTC HEURE_UTC COMMIT ANNONCE SORTIE_JSON
- DATE_UTC AAAA-MM-JJ et HEURE_UTC HH:MM relevées par `date -u` dans la même commande ;
- COMMIT : identifiant complet (40 caractères) du commit de la ligne `CODE-T07` que la mère annonce ; ce script
  refuse tout autre commit que la fusion c2fab6cc, seule vérifiée par la pièce de confirmation citée (sinon, pièce
  neuve sous un nom neuf, puis version neuve de ce script) ;
- ANNONCE : renvoi court à l'annonce de la mère (par exemple « message de la mère du AAAA-MM-JJ, R-xxxx ») ;
- couples de l'auteur (session du compte 4, modèle A ; modèles notés sans identifiant, R-2598, R-2605) :
  remplissage du marqueur du commit de T0.7 (VB4-02), parenthèse retirée, pièce de confirmation neuve de
  `reextraction_p3_v1.py`, identifiants de modèles remplacés par « modèle A » et « modèle B ».
"""
import hashlib, json, re, sys
from pathlib import Path

FUSION = "c2fab6cc"
PIECE = "brouillons/validite-adaptateur-v1/candidat1-pieces/confirmation-champs-t07-fusion-c2fab6cc-v2.md"
SHA_PIECE = "321b169aef79a0ef3291a88f08d60f83ceaacef400615a3d8c14f97de88a440f"
SHA_B5 = "56fb63e9b2f4ae8cb8361e94568a99c4ddbdb219220670a7e05f004afdaead26"
SHA_B4 = "417d6aee9a86d56f3478b57da30cb8d1af47493ff79ba69858f2167b8ad15f42"
M = "<<" + "COMMIT_C7_T07" + ">>"

def couples_auteur(d, h, c, annonce):
    out = []
    def a(i, ancien, nouveau): out.append({"id": i, "ancien": ancien, "nouveau": nouveau})
    a("A6-01", "honnête (iii) — v1 — brouillon 5", "honnête (iii) — v1 — brouillon 6")
    a("A6-02", "- Auteur des **brouillons 4 et 5** : la session du compte 4",
      "- Auteur des **brouillons 4 à 6** : la session du compte 4")
    a("A6-03", "la vérification courte du brouillon 4 et les décisions R-2597 et R-2604.",
      "la vérification courte du brouillon 4 et les décisions R-2597 et R-2604 ; le brouillon 6 de même, sur le brouillon 5, "
      "l'annonce par la mère du commit de la ligne `CODE-T07` et R-2605 (modèles notés « modèle A » et « modèle B » dans tout le texte).")
    a("A6-04", "- Date (UTC) : brouillon 5 écrit le 2026-11-13 à partir de ",
      f"- Date (UTC) : brouillon 6 écrit le {d} à partir de {h} UTC (heure relevée par `date -u`) ; brouillon 5 écrit le 2026-11-13 à partir de ")
    a("A6-05", f"- Statut : **brouillon 5**, écrit sur le brouillon 4 (`{SHA_B4}`) par couples versés : applique",
      f"- Statut : **brouillon 6**, écrit sur le brouillon 5 (`{SHA_B5}`) par couples versés : remplit le marqueur du commit de T0.7 "
      f"(VB4-02) au commit `{c}` de la ligne `CODE-T07`, annoncé par la mère ({annonce}) ; cite la pièce de confirmation neuve de "
      "`reextraction_p3_v1.py` ; note les modèles « modèle A » et « modèle B », sans identifiant, dans tout le texte (R-2605, point 2) ; "
      "aucun marqueur restant ; **non scellable avant la vérification courte du différentiel brouillon 5 → brouillon 6** (section "
      f"« Contre-lecture »). Le brouillon 5, écrit sur le brouillon 4 (`{SHA_B4}`) par couples versés, applique")
    a("A6-06", f"; un seul marqueur restant, `{M}`, gardé sur le mot de la mère (R-2597, point 3) jusqu'au commit corrigé de T0.7 ; "
      "**non scellable avant de l'avoir rempli** (VB4-02) et avant une vérification courte du différentiel.",
      "; il gardait un seul marqueur, celui du commit de T0.7, sur le mot de la mère (R-2597, point 3), rempli au brouillon 6.")
    a("A6-07", "Claude Opus 5.5 (`claude-opus-5-5`), auteur du brouillon 2", "modèle A, auteur du brouillon 2")
    a("A6-08", f"et code du module au commit de la ligne `CODE-T07` (`{M}` (marqueur laissé sur le mot de la mère : le commit C7, "
      "`b4cd9953` au 13 novembre, change pour un correctif du contrôle de cache qui ne touche que `reextraction_p3_v1.py`, R-2593 ; "
      "à remplir par le commit de la ligne `CODE-T07` en vigueur au scellement), vingt-six modules ;",
      f"et code du module au commit de la ligne `CODE-T07` (`{c}`, fusion du correctif du contrôle de cache, qui ne touche que "
      f"`reextraction_p3_v1.py` (R-2593) ; avant lui, C7 `b4cd9953` au 13 novembre ; commit annoncé par la mère, {annonce}), vingt-six modules ;")
    a("A6-09", f"puis confirmés par l'auteur du brouillon 4 sur le code au commit C7 de la ligne `CODE-T07` (`{M}`), égal à `main` sur les vingt-six modules,",
      "puis confirmés par l'auteur du brouillon 4 sur le code au commit C7 `b4cd9953`, alors celui de la ligne `CODE-T07` et égal à `main` sur les vingt-six modules,")
    a("A6-10", "`reextraction_p3_v1.py`, qui écrit `planchers-figees-t07.npz`, change au commit C7 suivant (R-2593) : ses champs sont revérifiés au commit qui remplira le marqueur ;",
      f"`reextraction_p3_v1.py`, qui écrit `planchers-figees-t07.npz`, est le seul fichier du module changé au commit `{c[:8]}` (R-2593 ; "
      "fonction `revision_au_cache` seule) : ses deux champs (états « établi », `meta` de `planchers-figees-t07.npz`) y sont revérifiés, "
      f"inchangés, et les vingt-cinq autres fichiers du module y sont identiques à C7 (pièce `{PIECE}`, `{SHA_PIECE}`, même réserve) ;")
    a("A6-11", "Claude Fable 5.2 (`claude-fable-5-2`), autre modèle que le rédacteur", "modèle B, autre modèle que le rédacteur")
    a("A6-12", "commit C7 laissé en marqueur (R-2593)",
      f"commit C7 remplacé par la fusion `{c[:8]}` au brouillon 6, champs de `reextraction_p3_v1.py` revérifiés (pièce `confirmation-champs-t07-fusion-c2fab6cc-v2.md`)")
    a("A6-13", "| VB4-02 (remplissage du marqueur) | différé au commit corrigé de T0.7 (R-2597, point 3) : deux couples à contexte, parenthèse retirée, pièce de confirmation neuve pour `reextraction_p3_v1.py` |",
      f"| VB4-02 (remplissage du marqueur) | appliqué au brouillon 6, au commit `{c[:8]}` de la ligne `CODE-T07` annoncé par la mère : deux couples à contexte, parenthèse retirée, pièce de confirmation neuve pour `reextraction_p3_v1.py` (`confirmation-champs-t07-fusion-c2fab6cc-v2.md`) |")
    a("A6-14", f"**Avant le scellement** : remplissage du marqueur `{M}` au commit corrigé de T0.7 (VB4-02), puis une vérification courte du différentiel brouillon 4 → brouillon suivant par un sous-agent neuf d'un autre modèle que l'auteur (modèle A), non lecteur de P3-bis.",
      "**Avant le scellement** : marqueur du commit de T0.7 rempli au brouillon 6 (VB4-02) ; reste une vérification courte du différentiel "
      "brouillon 5 → brouillon 6 par un sous-agent neuf d'un autre modèle que l'auteur (modèle A), non lecteur de P3-bis ; son entrée, avec "
      "ses deux empreintes, s'ajoute à cette section dans le texte qui suit.")
    return out

def principal():
    if len(sys.argv) != 6:
        sys.exit(__doc__)
    d, h, c, annonce, sortie = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], Path(sys.argv[5])
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", d) or not re.fullmatch(r"\d{2}:\d{2}", h):
        sys.exit("ARRÊT : date AAAA-MM-JJ et heure HH:MM attendues")
    if not re.fullmatch(r"[0-9a-f]{40}", c) or not c.startswith(FUSION):
        sys.exit(f"ARRÊT : commit complet attendu, égal à la fusion {FUSION} (seule vérifiée par la pièce citée)")
    if not annonce.strip() or "<<" in annonce:
        sys.exit("ARRÊT : renvoi à l'annonce de la mère vide ou marqué")
    if hashlib.sha256(Path(PIECE).read_bytes()).hexdigest() != SHA_PIECE:
        sys.exit("ARRÊT : empreinte de la pièce de confirmation différente")
    if sortie.exists():
        sys.exit(f"ARRÊT : {sortie} existe déjà (R12)")
    tout = couples_auteur(d, h, c, annonce)
    sortie.write_text(json.dumps(tout, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(tout)} couples écrits dans {sortie} ; sha256 {hashlib.sha256(sortie.read_bytes()).hexdigest()}")

principal()
