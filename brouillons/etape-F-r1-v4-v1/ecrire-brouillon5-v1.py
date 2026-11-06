"""Brouillon 5 (brouillon final) de l'addendum 1 des gardes (R1 v4) = brouillon 4 + (1) ligne 19 rendue à l'identique du
brouillon 3 (marqueur du GO), (2) ligne « Statut » réécrite, (3) ligne « Date » prolongée (fille 6, mot de la mère du
6 novembre 2026, 11:58 UTC). Chaque « ancien » doit apparaître exactement une fois ; arrêt sinon.
Usage (racine de l'arbre) : python3 -I brouillons/etape-F-r1-v4-v1/ecrire-brouillon5-v1.py B3 B4 SORTIE JOURNAL HEURE"""
import hashlib, sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd() / "src"))   # -I ignore PYTHONPATH : code du dépôt lu depuis la racine de l'arbre

B3, B4, SORTIE, JOURNAL = (Path(a) for a in sys.argv[1:5]); HEURE = sys.argv[5]
SHA = {B3: "81a04e7b9d0dc075bec03371a64f96c3c70fa1c540b7c32c2bd2486b953e6110",
       B4: "d6e94c3741c5d0177d5b9275ed6a21e04dd7532ecd5c63b79d930cd4ef7557dd"}
txt = {}
for p, s in SHA.items():
    txt[p] = p.read_text(encoding="utf-8")
    if hashlib.sha256(txt[p].encode("utf-8")).hexdigest() != s:
        sys.exit(f"ARRÊT : {p} d'empreinte inattendue")
t, l3, l4 = txt[B4], txt[B3].split("\n")[18], txt[B4].split("\n")[18]
assert "<<GO_LAZAR_SECOND_PASSAGE>>" in l3 and "GO-2026-11-06-02" in l4, "ARRÊT : ligne 19 inattendue"
STATUT_ANCIEN = t[t.index("- Statut : brouillon 2, non scellé ;"):t.index("dans l'arbre des analyses.\n") + len("dans l'arbre des analyses.\n")]
assert STATUT_ANCIEN.count("\n") == 4, "ARRÊT : « Statut » ne fait pas quatre lignes"
STATUT_NOUVEAU = ("- Statut : brouillon 5 (brouillon final), non scellé ; contre-lecture 1 (R2) faite sur le brouillon 1 et le code v6, v7, v4 : "
    "ses quinze couples appliqués, ses corrections de code K1, K2 et K3 faites (code v8, v9, v5) ; contre-lecture 2 (R2) faite sur "
    "le brouillon 2 (entrée « Contre-lecture 2 ») : ses six couples appliqués (brouillon 3) ; GO de Lazar sur les deux écarts "
    "déclarés et sur l'arrêt K3 donné le 6 novembre 2026 (GO-2026-11-06-02) ; scellé selon la procédure du Plan d'analyse, "
    "point 0, avant toute extraction de `calcul/r1-r2-reel-v1` dans l'arbre des analyses.\n")
DATE_ANCIEN = "brouillon 2, 2026-11-05, 19:48 (`date -u`)."
DATE_NOUVEAU = (f"brouillon 2, 2026-11-05, 19:48 ; brouillon 3, 2026-11-05, 20:27 ; brouillon 4, 2026-11-06, 11:49 ; "
                f"brouillon 5, 2026-11-06, {HEURE} (`date -u`).")
journal = []
for nom, a, n in (("ligne 19 (GO → marqueur)", l4 + "\n", l3 + "\n"), ("Statut", STATUT_ANCIEN, STATUT_NOUVEAU), ("Date", DATE_ANCIEN, DATE_NOUVEAU)):
    k = t.count(a)
    if k != 1:
        sys.exit(f"ARRÊT : « {nom} » trouvé {k} fois (1 exigé)")
    journal.append(f"- {nom} : 1 occurrence, ligne {t[:t.index(a)].count(chr(10)) + 1} de l'entrée")
    t = t.replace(a, n)
SORTIE.write_text(t, encoding="utf-8")
sha5 = hashlib.sha256(t.encode("utf-8")).hexdigest()
from controle_ia.prereg import problemes
p = problemes(SORTIE)
JOURNAL.write_text("# Journal du brouillon 5 (fille 6)\n\n" + f"- entrées : {B3} ({SHA[B3]}), {B4} ({SHA[B4]})\n- sortie : {SORTIE} ({sha5})\n"
                   + "\n".join(journal) + f"\n- problemes() : {p}\n", encoding="utf-8")
print(sha5); print(p)
