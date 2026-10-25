"""Contrôle des essais de la reprise par segments (R4) : chaque mutation volontaire du noyau doit faire échouer
`tests/test_reprise_segments.py`. Le fichier d'origine est rétabli après chaque mutation (et vérifié par empreinte)."""
import hashlib
import pathlib
import subprocess
import sys

DEPOT = pathlib.Path("/home/claude/noyau-reprise/essaim-m3-refonte-v1")
CIBLE = DEPOT / "essaim_m3" / "noyau" / "boucle.py"
PY = "/opt/venv-essaim-sim-v1/bin/python"

MUTATIONS = [
    ("M1 ronde en cours non rétablie", "        if r is not None:\n            self._ronde_en_cours = {", "        if False:\n            self._ronde_en_cours = {"),
    ("M2 conception déclarée faite après STOP", 'self._conception_faite = raison_conception != "fichier STOP"', "self._conception_faite = True"),
    ("M3 dépense non relue", 'self.depense_totale = float(etat["depense_totale_usd"])', "self.depense_totale = 0.0"),
    ("M4 ronde de conception sautée à la reprise", 'self._prochaine_ronde_conception = int(etat["prochaine_ronde_conception"])',
     'self._prochaine_ronde_conception = int(etat["prochaine_ronde_conception"]) + 1'),
    ("M5 garde du journal retirée", 'if len(lignes_ev) != int(etat.get("n_evenements", -1)):', "if False:"),
    ("M6 ordre des lignées inversé à la reprise", "        for l, e in lignees.items():\n            e = dict(e)",
     "        for l, e in reversed(list(lignees.items())):\n            e = dict(e)"),
    ("M7 lignées faites rejouées", 'for lignee in r["ordre"][len(r["faites"]):]:', 'for lignee in r["ordre"]:'),
    ("M8 numéro de ronde décalé dans l'état", '"ronde": int(self.ronde), "ronde_inachevee"', '"ronde": int(self.ronde) + 1, "ronde_inachevee"'),
    ("M9 STOP ignoré dans la ronde", "        for lignee in r[\"ordre\"][len(r[\"faites\"]):]:\n            raison = self._doit_arreter()\n            if raison:",
     "        for lignee in r[\"ordre\"][len(r[\"faites\"]):]:\n            raison = self._doit_arreter()\n            if raison and raison != \"fichier STOP\":"),
    ("M10 état non écrit au STOP", "                    self._ecrire_etat_reprise(raison)\n", "                    pass\n"),
    ("M11 conception arrêtée suivie de générations", 'if not self._conception_faite and any(e["active"] for e in self.lignees.values()):',
     'if False and any(e["active"] for e in self.lignees.values()):'),
    ("M12 STOP honoré sans unité restante", "                # dernière unité n'appelle pas de segment de plus\n                raison = None",
     "                # dernière unité n'appelle pas de segment de plus\n                pass"),
]


def empreinte(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> int:
    origine = CIBLE.read_bytes()
    sha = empreinte(CIBLE)
    echecs_attendus_manques = []
    try:
        for nom, avant, apres in MUTATIONS:
            texte = origine.decode("utf-8")
            if texte.count(avant) != 1:
                print(f"{nom} : motif trouvé {texte.count(avant)} fois (attendu 1) — mutation non appliquée", flush=True)
                echecs_attendus_manques.append(nom)
                continue
            CIBLE.write_text(texte.replace(avant, apres), encoding="utf-8")
            r = subprocess.run([PY, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "tests/test_reprise_segments.py"],
                               cwd=DEPOT, capture_output=True, text=True, timeout=1200)
            CIBLE.write_bytes(origine)
            derniere = [l for l in r.stdout.splitlines() if l.strip()][-1:] or ["(rien)"]
            echoue = r.returncode != 0
            print(f"{nom} : {'DÉTECTÉE' if echoue else 'NON DÉTECTÉE'} (code {r.returncode}) — {derniere[0]}", flush=True)
            if not echoue:
                echecs_attendus_manques.append(nom)
    finally:
        CIBLE.write_bytes(origine)
    assert empreinte(CIBLE) == sha, "fichier d'origine non rétabli"
    print(f"fichier d'origine rétabli : {sha}")
    print(f"mutations non détectées ou non appliquées : {echecs_attendus_manques or 'aucune'}")
    return 1 if echecs_attendus_manques else 0


if __name__ == "__main__":
    sys.exit(main())
