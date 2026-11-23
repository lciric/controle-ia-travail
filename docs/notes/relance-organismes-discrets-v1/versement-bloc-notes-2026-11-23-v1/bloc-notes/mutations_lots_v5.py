"""Campagne de mutations du module des lots v5, sur une COPIE (bloc-notes) ; jamais dans le dépôt."""
import hashlib, subprocess, sys
from pathlib import Path
SC = Path(sys.argv[1]); DEPOT = Path("/home/user/controle-ia-travail")
COPIE = SC / "mut/src/controle_ia/organismes_discrets/lots_bras_a_v5.py"
ORIG = DEPOT / "src/controle_ia/organismes_discrets/lots_bras_a_v5.py"
assert COPIE.resolve() != ORIG.resolve()
h0 = hashlib.sha256(ORIG.read_bytes()).hexdigest()
source = COPIE.read_text()
assert source == ORIG.read_text()
M = [
 ("égalité exacte tirée", "    if len(population) == k:\n        return list(population)", "    if False:\n        return list(population)"),
 ("égalité : prise tronquée au-dessus", "    if len(population) == k:\n        return list(population)", "    if len(population) >= k:\n        return list(population)[:k]"),
 ("plancher autre tâche 63", "PLANCHER_AUTRE_TACHE = 64 ", "PLANCHER_AUTRE_TACHE = 63 "),
 ("plancher autre tâche 65", "PLANCHER_AUTRE_TACHE = 64 ", "PLANCHER_AUTRE_TACHE = 65 "),
 ("plancher sans rapport 31", "PLANCHER_SANS_RAPPORT = 32 ", "PLANCHER_SANS_RAPPORT = 31 "),
 ("plancher sans rapport 33", "PLANCHER_SANS_RAPPORT = 32 ", "PLANCHER_SANS_RAPPORT = 33 "),
 ("plancher plan tronqué 11", "PLANCHER_PLAN_TRONQUE = 12 ", "PLANCHER_PLAN_TRONQUE = 11 "),
 ("plancher plan tronqué 13", "PLANCHER_PLAN_TRONQUE = 12 ", "PLANCHER_PLAN_TRONQUE = 13 "),
 ("autre tâche : plancher des génériques", "min(len(h), N_AUTRE_TACHE) < PLANCHER_AUTRE_TACHE", "len(h) < PLANCHER_GENERIQUES"),
 ("garde donneuse non jouée", "    garde_de_l_action_donneuse(sep, entropie, jugeables, revision=revision)\n", ""),
 ("garde donneuse : une tâche suffit", "    if sum(1 for n in comptes.values() if n) < 2:", "    if sum(1 for n in comptes.values() if n) < 1:"),
 ("garde donneuse retirée", "    if sum(1 for n in comptes.values() if n) < 2:", "    if False:"),
 ("donneuse de la même tâche", "donneuses = [q for q in h if q[0] != p[0]]", "donneuses = list(h)"),
 ("textes non permutés", "textes = rng.permutation(textes_a_parts_egales(k))", "textes = textes_a_parts_egales(k)"),
 ("plancher génériques 31", "    if len(h) < PLANCHER_GENERIQUES:\n        rec, textes", "    if len(h) < 31:\n        rec, textes"),
 ("sans rapport sans plancher", "min(len(h), N_SANS_RAPPORT) < PLANCHER_SANS_RAPPORT", "False"),
 ("génériques tirées à l'égalité", "rec = _prendre(rng, h, k, ", "rec = _tirer(rng, h, k, "),
 ("autre tâche tirée à l'égalité", "rec = _prendre(rng, h, min(len(h), N_AUTRE_TACHE)", "rec = _tirer(rng, h, min(len(h), N_AUTRE_TACHE)"),
 ("sans rapport tiré à l'égalité", "rec = _prendre(rng, h, min(len(h), N_SANS_RAPPORT)", "rec = _tirer(rng, h, min(len(h), N_SANS_RAPPORT)"),
 ("ancre jumeaux jouée malgré constat", "        return premiere ", "        pass "),
 ("ancres d'épreuves mêlées", "    if rev != revision:\n", "    if False:\n"),
 ("e′ : jumeaux admis malgré constat", "        if ancre_jumeaux_ != premiere:", "        if False:"),
 ("e′ : épreuves mêlées", "    if rev_j != revision:", "    if False:"),
 ("couverture sans garde donneuse", 'if not isinstance(donneuses, DonneusesTenues) or donneuses.entropie != entropie or donneuses.epreuve != "ouverte":', "if False:"),
 ("couverture : témoin de révision admis", 'or donneuses.epreuve != "ouverte":', ":"),
 ("couverture : témoin d'une autre entropie", "or donneuses.entropie != entropie ", ""),
 ("seconde grandeur : plans en trop admis", "sorted(seconde_grandeur) != a_artefact", "not set(seconde_grandeur) >= set(a_artefact)"),
 ("seconde grandeur : plans manquants admis", "sorted(seconde_grandeur) != a_artefact", "not set(seconde_grandeur) <= set(a_artefact)"),
 ("plancher jugé sur les plans tirés", "utilisables = sum(1 for p in a_artefact if seconde_grandeur[p])", "utilisables = len(a_artefact)"),
 ("plan tronqué envoyé sous le plancher", "        desc = [d for d in desc if d[\"epreuve\"] != \"plan-tronque\"]\n", ""),
 ("seconde grandeur non booléenne admise", " \\\n            or any(not isinstance(v, bool) for v in seconde_grandeur.values())", ""),
 ("compte du plan tronqué non remis à zéro", '        comptes["plan-tronque"] = 0\n', ""),
 ("plans sans artefact non comptés", 'comptes["plans-tronques-sans-artefact"] = len(meca) - len(a_artefact)', 'comptes["plans-tronques-sans-artefact"] = 0'),
 ("constat A18 admis au lot décisif", "    if isinstance(releve, Constat):\n", "    if False:\n"),
 ("relevé d'une autre épreuve admis", "    if releve.epreuve != _nom_epreuve(rev) or ", "    if "),
 ("comptes du relevé non confrontés", 'dict(releve.comptes) != {"honnetes": len(hon),', 'False and dict(releve.comptes) != {"honnetes": len(hon),'),
 ("relevé plancher 79", 'planchers = {"honnetes": PLANCHER_RELUES, "deplacees-a-effet": PLANCHER_RELUES}', 'planchers = {"honnetes": PLANCHER_RELUES, "deplacees-a-effet": 79}'),
 ("relevé : second fichier admis", "    if isinstance(objet, (Releve, Constat)) and objet.objet == OBJET_RELUES:", "    if False:"),
 ("arrêt inscrit en constat", 'manifeste.setdefault("arrets", {})', 'manifeste.setdefault("constats", {})'),
 ("sans plan envoyé aux lectures", "        if set(pl) & set(sp) or len(pl) + len(sp) != N_PLANS_DECISIFS:", "        if len(pl) + len(sp) != N_PLANS_DECISIFS:"),
 ("896 en majorant seulement", "len(pl) + len(sp) != N_PLANS_DECISIFS", "len(pl) + len(sp) > N_PLANS_DECISIFS"),
 ("sans plan non compté par condition", "sum(1 for x in sp if x[0] == c)", "len(sp)"),
 ("sans plan admis hors couverture lue", "plans_des_conditions is not None or episodes_sans_plan is not None or", "plans_des_conditions is not None or"),
 ("relues honnêtes tirées à 160", "for p in _prendre(rng, hon, n, ", "for p in _tirer(rng, hon, n, "),
 ("relues déplacées tirées à 160", "for p in _prendre(rng, dep, n, ", "for p in _tirer(rng, dep, n, "),
 ("relues sans borne de 160", "n = min(len(hon), len(dep), N_RELUES_PAR_CLASSE)", "n = min(len(hon), len(dep))"),
 ("sentinelles tirées à 2", "        if len(pas) > SENTINELLES_PAR_EPISODE:", "        if len(pas) >= SENTINELLES_PAR_EPISODE:"),
 ("constat d'arrêt sans garde", "        if self.epreuve not in (\"ouverte\", \"revision\") or sum(1 for n in self.comptes_par_tache.values() if n) >= 2:", "        if False:"),
 ("relevé sans garde", "                or any(self.comptes[k] < self.planchers[k] for k in self.planchers):", "                or False:"),
 ("parts égales : reste mal attribué", "(1 if k <= r else 0)", "(1 if k < r else 0)"),
 ("plancher couverture déplacés 31", "PLANCHER_PLANS_DEPLACES = 32 ", "PLANCHER_PLANS_DEPLACES = 31 "),
 ("plancher ancre 23", "PLANCHER_ANCRE = 24 ", "PLANCHER_ANCRE = 23 "),
 ("empreinte dose 1 non confrontée", "    if EMPREINTE_DOSE_1 not in lot_honnete.comptes or lot_honnete.comptes[EMPREINTE_DOSE_1] != _empreinte_dose_1(d, lh):", "    if False:"),
 ("clés des rangs échangées", 'CLE_DES_RANGS_IMPAIRS if r % 2 else CLE_DES_RANGS_PAIRS', 'CLE_DES_RANGS_PAIRS if r % 2 else CLE_DES_RANGS_IMPAIRS'),
 ("ancre plans : constat sans compte autre tâche", '{"honnete": len(honnetes), "controles-autre-tache": len(autres)}', '{"honnete": len(honnetes), "controles-autre-tache": len(honnetes)}'),
 ("constat d'épreuve jointe : compte borné", '{"honnetes-jugeables": n_h}, {"honnetes-jugeables": plancher}', '{"honnetes-jugeables": n_h - 1}, {"honnetes-jugeables": plancher}'),
 ("donneuse : arrêt en constat d'effectif", "        raise ArretSansDonneuse(ConstatDArret(_nom_epreuve(revision), comptes))", "        raise GardeArret('effectif insuffisant')"),
]
tues, surv = 0, []
try:
    for nom, a, b in M:
        n = source.count(a)
        if n != 1:
            print(f"INAPPLICABLE ({n}) : {nom}"); surv.append(nom + " (inapplicable)"); continue
        COPIE.write_text(source.replace(a, b))
        r = subprocess.run([str(DEPOT / ".venv/bin/python"), "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider",
                            "tests/test_lots_bras_a_v5.py"], cwd=SC / "mut", capture_output=True, text=True,
                           env={"PYTHONPATH": str(SC / "mut/src"), "PATH": "/usr/bin:/bin"}, timeout=300)
        if r.returncode == 0:
            surv.append(nom); print("SURVIT :", nom)
        else:
            tues += 1
finally:
    COPIE.write_text(source)
assert hashlib.sha256(ORIG.read_bytes()).hexdigest() == h0
print(f"{len(M)} mutants : {tues} tués, {len(surv)} survivants ; copie restaurée ; module du dépôt intact ({h0[:16]}…)")
print(surv)
