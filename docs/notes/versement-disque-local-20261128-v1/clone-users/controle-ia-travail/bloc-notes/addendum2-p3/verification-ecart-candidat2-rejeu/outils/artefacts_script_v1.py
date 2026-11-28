"""Éprouve les refus du script `ecrire_candidat2_addendum2_v1.py` (sha256 51c7bd1b…) sur des copies.

Usage : python -I -B artefacts_script_v1.py SCRIPT CANDIDAT1 LIGNE DOSSIER
  SCRIPT, CANDIDAT1, LIGNE : copies des pièces (empreintes vérifiées ici avant usage).
  DOSSIER : dossier vide à moi ; chaque cas y reçoit un sous-dossier (entrées altérées, sortie attendue absente).
Cas : sain ; candidat 1 d'autre empreinte (un octet changé) ; ancre « Date (UTC) » absente ou en double, et ancien
texte absent (ces trois-là demandent une copie du script dont seule la constante CANDIDAT1 vise l'entrée altérée,
sinon le contrôle d'empreinte refuse avant) ; élément « Candidat 2 » mal formé ; mauvais nombre d'arguments.
Chaque cas lance le script dans un processus neuf (python -I -B) et note code, message et présence de la sortie.
N'importe rien du dépôt ; n'écrit que sous DOSSIER.
"""
import hashlib
import subprocess
import sys
from pathlib import Path

ATTENDU = {
    "script": "51c7bd1b4886e43fd6a4bc80c8a11fbed3813c5307cd00b532c833d2295d5943",
    "candidat1": "9900a721560c87361efcf60660863727644e8fdc3ab88e4fd1f325a613306b0e",
    "ligne": "7e106f17410587947775451f7ea58df978853b0e051338ba522c63d98b028568",
}
CANDIDAT2 = "5d5e5aa83c57d37e6406ea1d57e87bc841c8e69e22a4918324a36b2b877bc247"
ANCRE = "- Date (UTC) : celle du commit de scellement, qui fait foi.\n"


def h(b):
    return hashlib.sha256(b).hexdigest()


def lancer(nom, script, args, dossier):
    sortie = dossier / "sortie.md"
    r = subprocess.run([sys.executable, "-I", "-B", str(script), *[str(a) for a in args]],
                       capture_output=True, text=True, cwd=dossier)
    existe = sortie.exists()
    emp = h(sortie.read_bytes()) if existe else "-"
    msg = (r.stderr.strip().splitlines() or [""])[-1][:160]
    print(f"{nom} | code={r.returncode} | sortie_ecrite={existe} | sha256_sortie={emp} | stdout={r.stdout.strip()[:64]!r} | stderr_fin={msg!r}")
    return r.returncode, existe, emp


def script_vise(script_octets, cible_hex, dossier):
    t = script_octets.decode("utf-8")
    ancien = f'CANDIDAT1 = "{ATTENDU["candidat1"]}"'
    assert t.count(ancien) == 1
    s = dossier / "script-altere.py"
    s.write_text(t.replace(ancien, f'CANDIDAT1 = "{cible_hex}"'), encoding="utf-8")
    return s


def main(argv):
    script, cand1, ligne, base = map(Path, argv[1:5])
    sb, cb, lb = script.read_bytes(), cand1.read_bytes(), ligne.read_bytes()
    for k, b in (("script", sb), ("candidat1", cb), ("ligne", lb)):
        assert h(b) == ATTENDU[k], k
    print("empreintes des copies : justes")
    res = {}
    t = cb.decode("utf-8")

    d = base / "0-sain"; d.mkdir(parents=True)
    res["sain"] = lancer("0-sain", script, [cand1, ligne, d / "sortie.md"], d)

    d = base / "1-autre-empreinte"; d.mkdir()
    alt = bytearray(cb); i = alt.index(b"Candidat 1 :"); alt[i] = ord("c")
    (d / "candidat1-altere.md").write_bytes(bytes(alt))
    res["autre_empreinte"] = lancer("1-autre-empreinte", script, [d / "candidat1-altere.md", ligne, d / "sortie.md"], d)

    d = base / "1b-fin-de-ligne-ajoutee"; d.mkdir()
    (d / "candidat1-altere.md").write_bytes(cb + b"\n")
    res["octet_ajoute"] = lancer("1b-octet-ajoute", script, [d / "candidat1-altere.md", ligne, d / "sortie.md"], d)

    d = base / "2-ancre-absente"; d.mkdir()
    assert t.count(ANCRE) == 1
    alt = t.replace(ANCRE, "- Date (UTC) : celle du commit de scellement.\n").encode("utf-8")
    (d / "candidat1-sans-ancre.md").write_bytes(alt)
    res["ancre_absente_script_original"] = lancer("2a-ancre-absente-script-original", script, [d / "candidat1-sans-ancre.md", ligne, d / "sortie.md"], d)
    s = script_vise(sb, h(alt), d)
    res["ancre_absente"] = lancer("2b-ancre-absente-script-vise", s, [d / "candidat1-sans-ancre.md", ligne, d / "sortie.md"], d)

    d = base / "3-ancre-en-double"; d.mkdir()
    alt = t.replace(ANCRE, ANCRE + ANCRE).encode("utf-8")
    (d / "candidat1-ancre-double.md").write_bytes(alt)
    s = script_vise(sb, h(alt), d)
    res["ancre_double"] = lancer("3-ancre-en-double-script-vise", s, [d / "candidat1-ancre-double.md", ligne, d / "sortie.md"], d)

    d = base / "4-ancien-texte-absent"; d.mkdir()
    a = "(2026-10-20 vers 21:45 UTC)"; assert t.count(a) == 1
    alt = t.replace(a, "(2026-10-20 vers 21:46 UTC)").encode("utf-8")
    (d / "candidat1-sans-ancien.md").write_bytes(alt)
    s = script_vise(sb, h(alt), d)
    res["ancien_absent"] = lancer("4-ancien-texte-absent-script-vise", s, [d / "candidat1-sans-ancien.md", ligne, d / "sortie.md"], d)

    d = base / "4b-ancien-texte-en-double"; d.mkdir()
    alt = (t + "(2026-10-20 vers 21:45 UTC)\n").encode("utf-8")
    (d / "candidat1-ancien-double.md").write_bytes(alt)
    s = script_vise(sb, h(alt), d)
    res["ancien_double"] = lancer("4b-ancien-texte-en-double-script-vise", s, [d / "candidat1-ancien-double.md", ligne, d / "sortie.md"], d)

    d = base / "5-element-mal-forme"; d.mkdir()
    (d / "ligne-sans-tiret.md").write_bytes(lb.replace(b"- Candidat 2 : ", b"Candidat 2 : ", 1))
    res["element_sans_tiret"] = lancer("5a-element-sans-tiret", script, [cand1, d / "ligne-sans-tiret.md", d / "sortie.md"], d)
    d2 = base / "5b-element-sans-fin-de-ligne"; d2.mkdir()
    (d2 / "ligne-sans-fin.md").write_bytes(lb.rstrip(b"\n"))
    res["element_sans_fin"] = lancer("5b-element-sans-fin-de-ligne", script, [cand1, d2 / "ligne-sans-fin.md", d2 / "sortie.md"], d2)

    d = base / "6-arguments"; d.mkdir()
    res["arguments"] = lancer("6-deux-arguments", script, [cand1, ligne], d)

    ok = (res["sain"] == (0, True, CANDIDAT2)
          and all(v[0] != 0 and not v[1] for k, v in res.items() if k != "sain"))
    print("bilan :", "sain = candidat 2 ; chaque artefact refusé, aucune sortie écrite" if ok else "ÉCART")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
