"""v2 du traitement du correcteur v5 (VV5-fidelite-08). Rejouable.

- v1 contrôlée par empreinte complète (constante et compagnon) ; jamais modifiée (R12).
- Remplacements exacts, chacun trouvé une seule fois, sinon ARRÊT : titre « v1 » → « v2 » ; une note de version sous le
  titre ; colonne « écart » de VV4-sens-04 = mots exacts de VV5-fidelite-08.
- Contrôle : la colonne « écart » est remplie (≠ « aucun ») pour 13 constats exactement, VV4-sens-04 n'y étant plus.
Usage : PYTHONDONTWRITEBYTECODE=1 python3 -I -B traitement_v4_v2.py [--essai]
"""
import hashlib
import sys
from pathlib import Path

RD = Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection")
V1 = RD / "traitement-verification-v4-par-correcteur-v1.md"
V2 = RD / "traitement-verification-v4-par-correcteur-v2.md"
VV5 = RD / "verification-v5-fidelite/verification-v5-fidelite-v1.md"
VV5_SHA = "054720926c0fe16140dd5aebbb508317eb1ddbc385ac9c02032225a3ae214881"
CELLULE_VV5 = "« aucun (le constat demande une phrase ; elle est faite de ses mots) »"


def lire(p, attendu=None):
    b = p.read_bytes()
    h = hashlib.sha256(b).hexdigest()
    comp = (p.parent / (p.name + ".sha256")).read_text(encoding="utf-8").split()
    if comp != [h, p.name] or (attendu and h != attendu):
        raise SystemExit(f"ARRÊT : {p.name} : empreinte {h}, compagnon {comp}")
    return b.decode("utf-8"), h


def main():
    v1, h1 = lire(V1)
    vv5, _ = lire(VV5, VV5_SHA)
    if " ".join(vv5.split()).count(CELLULE_VV5) != 1:
        raise SystemExit("ARRÊT : mots de VV5-fidelite-08 non trouvés une fois dans le rapport")
    cellule = CELLULE_VV5[2:-2]
    note = (
        "\n\nv2 (correcteur v7, session 16, 2026-10-21) : seule la colonne « écart » de VV4-sens-04 change, en mots exacts de "
        "VV5-fidelite-08\n(`…/revue-detection/verification-v5-fidelite/verification-v5-fidelite-v1.md`, `05472092…`) : "
        "ce n'est pas un écart ; le compte de 13\nécarts du bilan était juste, la table le montre désormais. La v1 "
        f"(`{h1[:8]}…`) reste intacte (R12)."
    )
    R = [
        ("# Traitement des vérifications de la synthèse v4 « comment détecter » (tour 3), par le correcteur v5 — v1",
         "# Traitement des vérifications de la synthèse v4 « comment détecter » (tour 3), par le correcteur v5 — v2" + note),
        ("; nœud E2, l. 401-403 | au nœud E2, la phrase unique est composée des mots du constat |",
         f"; nœud E2, l. 401-403 | {cellule} |"),
    ]
    t = v1
    for a, b in R:
        if t.count(a) != 1:
            raise SystemExit(f"ARRÊT : « {a[:60]} » trouvé {t.count(a)} fois")
        t = t.replace(a, b)
    lignes = [l for l in t.split("\n") if l.startswith("| VV4-")]
    ecarts = [l.split(" | ")[0][2:] for l in lignes if l.rstrip(" |").split(" | ")[-1].strip() != "aucun"
              and not l.rstrip(" |").split(" | ")[-1].startswith("aucun (")]
    print(f"{len(lignes)} lignes de constats ; écart rempli pour {len(ecarts)} : {', '.join(ecarts)}")
    if len(lignes) != 28 or len(ecarts) != 13 or "VV4-sens-04" in ecarts:
        raise SystemExit("ARRÊT : compte des écarts différent de 13")
    if "--essai" in sys.argv:
        return
    if V2.exists():
        raise SystemExit(f"ARRÊT : {V2} existe déjà (R12)")
    V2.write_text(t, encoding="utf-8")
    print(f"v2 écrite ; {len(R)} remplacements ; v1 {h1} ; v2 {hashlib.sha256(t.encode('utf-8')).hexdigest()}")


if __name__ == "__main__":
    main()
