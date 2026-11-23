"""Campagne de mutations du module des lots v3, écrite sur une COPIE : l'arbre `src/`, la page `pyproject.toml`
et les essais v3 sont copiés dans le bloc-notes ; chaque mutant est écrit dans la copie du module, jamais dans le
dépôt ; les essais sont joués avec -x depuis la copie ; le module du dépôt est confronté à son empreinte avant et
après, et la copie restaurée à la fin."""
import hashlib, subprocess, sys, os, shutil
DEPOT = "/home/user/controle-ia-travail"
SP = "/tmp/claude-0/-home-user-controle-ia-travail/445c1b8c-c9f5-52f6-966f-fc165ad0e0c8/scratchpad"
COPIE = f"{SP}/mutations_v3_copie"
MOD_DEPOT = f"{DEPOT}/src/controle_ia/organismes_discrets/lots_bras_a_v3.py"
shutil.rmtree(COPIE, ignore_errors=True)
shutil.copytree(f"{DEPOT}/src", f"{COPIE}/src", ignore=shutil.ignore_patterns("__pycache__"))
os.makedirs(f"{COPIE}/tests")
for f in ("conftest.py", "test_lots_bras_a_v3.py"):
    shutil.copy(f"{DEPOT}/tests/{f}", f"{COPIE}/tests/{f}")
shutil.copy(f"{DEPOT}/pyproject.toml", f"{COPIE}/pyproject.toml")
MOD = f"{COPIE}/src/controle_ia/organismes_discrets/lots_bras_a_v3.py"
ESSAIS = "tests/test_lots_bras_a_v3.py"
h_depot0 = hashlib.sha256(open(MOD_DEPOT, "rb").read()).hexdigest()
M = [
 ("plancher des génériques 32 -> 31", "PLANCHER_GENERIQUES = 32 ", "PLANCHER_GENERIQUES = 31 "),
 ("génériques : seuil > au lieu de >=", "elif len(h) >= PLANCHER_GENERIQUES:", "elif len(h) > PLANCHER_GENERIQUES:"),
 ("génériques 32..63 : actions tirées", "        rec = list(h)\n", "        rec = [h[int(i)] for i in rng.choice(len(h), len(h), replace=False)]\n"),
 ("parts égales : reste aux derniers textes", "(1 if k <= r else 0)", "(1 if k > N_TEXTES_GENERIQUES - r else 0)"),
 ("parts égales sans permutation", "textes = rng.permutation(textes_a_parts_egales(len(h)))", "textes = textes_a_parts_egales(len(h))"),
 ("constat des génériques omis", "        constats.append(Constat(", "        (lambda *a: None)(Constat("),
 ("cas complet des génériques à 63", "if len(h) >= N_GENERIQUES:", "if len(h) >= N_GENERIQUES - 1:"),
 ("plancher des ancres 24 -> 23", "PLANCHER_ANCRE = 24 ", "PLANCHER_ANCRE = 23 "),
 ("ancre des jumeaux sans constat", "                         \"aucun jumeau n'est remis au juge ; le critère de l'ancre des jumeaux échoue (ligne A7)\")\n    if k:", "                         \"aucun jumeau n'est remis au juge ; le critère de l'ancre des jumeaux échoue (ligne A7)\")\n    if False:"),
 ("plancher des plans honnêtes 32 -> 33", "PLANCHER_PLANS_HONNETES = 32 ", "PLANCHER_PLANS_HONNETES = 33 "),
 ("plancher des plans déplacés 32 -> 31", "PLANCHER_PLANS_DEPLACES = 32 ", "PLANCHER_PLANS_DEPLACES = 31 "),
 ("sans plan présenté comme déplacé admis", "    if not set(sp) <= set(lh):", "    if False:"),
 ("partition : recouvrement admis", "if set(a) & set(s) or len(a)", "if len(a)"),
 ("méca : toujours tiré", "if len(de_t) <= PLANS_MECA_PAR_TACHE:", "if len(de_t) < 0:"),
 ("méca : tirage parmi les 8 épisodes", "rng.choice(len(de_t), PLANS_MECA_PAR_TACHE, replace=False)", "rng.choice(min(len(de_t), EPISODES), PLANS_MECA_PAR_TACHE, replace=True)"),
 ("mécanique : effectif exact 32 fixe", "borne = ARTEFACTS_PAR_PLAN[ep] * len(meca)", "borne = ARTEFACTS_PAR_PLAN[ep] * 32"),
 ("jumeaux couverture : comptes non confrontés", "    if (len(d), len(lh)) != (lot_honnete.comptes", "    if False and (len(d), len(lh)) != (lot_honnete.comptes"),
 ("jumeaux couverture : plans relus omis", "    desc += [{\"composante\": \"plan-d-epreuve-relu\", \"tache\": t, \"episode\": e} for t, e in p]\n", "\n"),
 ("plancher des relues 80 -> 79", "PLANCHER_RELUES = 80 ", "PLANCHER_RELUES = 79 "),
 ("relues : classe de 160 prise sans tirage", "if n < N_RELUES_PAR_CLASSE and len(population) == n:", "if len(population) == n:"),
 ("relues : classe courte toujours tirée", "if n < N_RELUES_PAR_CLASSE and len(population) == n:", "if False:"),
 ("relues : n = le plus grand", "n = min(len(hon), len(dep), N_RELUES_PAR_CLASSE)", "n = min(max(len(hon), len(dep)), N_RELUES_PAR_CLASSE)"),
 ("relues : constat omis", "                         \"décisif n'est pas construit : ligne A10, sans aucun appel de la lecture décisive (6.8)\")\n    if k:", "                         \"décisif n'est pas construit : ligne A10, sans aucun appel de la lecture décisive (6.8)\")\n    if False:"),
 ("relues : déplacées tirées d'abord", "    desc += [_action_d(\"action-d-epreuve-relue\", p, classe=\"honnete\", epreuve=epreuve)\n             for p in _classe_relue(rng, hon, n, \"actions d'épreuve relues, honnêtes\")]\n    desc += [_action_d(\"action-d-epreuve-relue\", p, classe=\"deplacee\", epreuve=epreuve)\n             for p in _classe_relue(rng, dep, n, \"actions d'épreuve relues, déplacées à effet\")]",
  "    _d = [_action_d(\"action-d-epreuve-relue\", p, classe=\"deplacee\", epreuve=epreuve)\n             for p in _classe_relue(rng, dep, n, \"actions d'épreuve relues, déplacées à effet\")]\n    desc += [_action_d(\"action-d-epreuve-relue\", p, classe=\"honnete\", epreuve=epreuve)\n             for p in _classe_relue(rng, hon, n, \"actions d'épreuve relues, honnêtes\")]\n    desc += _d"),
 ("relues déplacées sans effet admises", "if d[\"verite\"] == A_EFFET))", "if d[\"verite\"] != DEPLACEE_NON_JUGEABLE))"),
 ("plans des conditions : arrêt simple au lieu d'ambiguïté", "            raise AmbiguiteDuTexte(f\"lot décisif : {len(pl)}", "            raise GardeArret(f\"lot décisif : {len(pl)}"),
 ("donneuse absente : arrêt simple au lieu d'ambiguïté", "            raise AmbiguiteDuTexte(\"contrôles d'une autre tâche", "            raise GardeArret(\"contrôles d'une autre tâche"),
 ("étape (d) : ordre inversé", "    for lot in (ancre_plans, ancre_couverture_):", "    for lot in (ancre_couverture_, ancre_plans):"),
 ("ancre incomplète admise", "    if vu != voulu or len(lot.appels) != sum(voulu.values()):", "    if False:"),
 ("ancre de la couverture de la révision admise", "    if lot.revision and lot.nom not in LOTS_DU_JUGE_DE_LA_REVISION:", "    if False:"),
 ("étape (d) de la révision avec couverture admise", "        if ancre_couverture_ is not None:\n            raise", "        if False:\n            raise"),
 ("constat réécrit au manifeste", "    if cle in registre and registre[cle] != ligne:", "    if False:"),
 ("constats hors des octets du lot", "        if self.constats:\n            c[\"constats\"]", "        if False:\n            c[\"constats\"]"),
 ("constat mal formé admis", "                or not self.sous_le_plancher:", "                or False:"),
 ("tirer : arrêt dès l'égalité", "    if len(population) < k:\n        raise GardeArret(f\"{ou} : {len(population)} disponibles", "    if len(population) <= k:\n        raise GardeArret(f\"{ou} : {len(population)} disponibles"),
 # mutants repris de la v1
 ("tirage sans remise -> avec remise", "return [population[int(i)] for i in rng.choice(len(population), size=k, replace=False)]", "return [population[int(i)] for i in rng.choice(len(population), size=k, replace=True)]"),
 ("128 -> 127", "N_AUTRE_TACHE, N_SANS_RAPPORT, N_GENERIQUES = 128, 64, 64", "N_AUTRE_TACHE, N_SANS_RAPPORT, N_GENERIQUES = 127, 64, 64"),
 ("donneuse de la même tâche", "donneuses = [q for q in h if q[0] != p[0]]", "donneuses = [q for q in h if q != p]"),
 ("ordre ignoré", "        d = canon[ordre[r]]", "        d = canon[r]"),
 ("identifiants inversés", "appels.append({\"rang\": r + 1, \"identifiant\": ids[r]})\n        tables.setdefault(tables_de(d) if tables_de else \"entrees\", {})[ids[r]] = d", "appels.append({\"rang\": r + 1, \"identifiant\": ids[n - 1 - r]})\n        tables.setdefault(tables_de(d) if tables_de else \"entrees\", {})[ids[n - 1 - r]] = d"),
 ("liste non triée", "    canon = sorted(descriptions, key=_tri)", "    canon = list(descriptions)"),
 ("non jugeables envoyées", "for s in dep if s[3] != DEPLACEE_NON_JUGEABLE]", "for s in dep]"),
 ("sentinelles sans tirage", "            pas = [pas[int(i)] for i in rng.choice(len(pas), SENTINELLES_PAR_EPISODE, replace=False)]", "            pas = pas[:SENTINELLES_PAR_EPISODE]"),
 ("tables échangées", "tables_de=lambda d: TABLE_DES_SENTINELLES if d[\"composante\"] in _DES_SENTINELLES", "tables_de=lambda d: TABLE_DES_CONDITIONS if d[\"composante\"] in _DES_SENTINELLES"),
 ("parité inversée", "CLE_DES_RANGS_IMPAIRS if r % 2 else CLE_DES_RANGS_PAIRS", "CLE_DES_RANGS_PAIRS if r % 2 else CLE_DES_RANGS_IMPAIRS"),
 ("reprise sous l'autre clé admise", "    if cle_du_premier_envoi is not None and cle_du_premier_envoi != c:", "    if False:"),
 ("clé alea sans révision", "cle_alea=g.cle_alea(nom, *p, revision=revision)", "cle_alea=g.cle_alea(nom, *p)"),
 ("garde de la coupe retirée", "    if (list(sep.ouvertes), list(sep.gardees)) != (ouv, gar):", "    if False:"),
 ("lot réécrit au manifeste", "    if lot.cle_ordre in lots and lots[lot.cle_ordre] != ligne:", "    if False:"),
]
exec(open(f"{SP}/neufs_v3.py", encoding="utf-8").read())
M += NEUFS
orig = open(MOD, "rb").read()
h0 = hashlib.sha256(orig).hexdigest()
assert h0 == h_depot0
env = dict(os.environ, PYTHONPATH=f"{COPIE}/src")
r = subprocess.run([sys.executable, "-c", "import controle_ia.organismes_discrets.lots_bras_a_v3 as L; print(L.__file__)"],
                   cwd=COPIE, env=env, capture_output=True, text=True)
assert r.stdout.strip() == MOD, r.stdout + r.stderr
r = subprocess.run([sys.executable, "-m", "pytest", "-x", "-q", "-p", "no:cacheprovider", ESSAIS], cwd=COPIE, env=env,
                   capture_output=True)
assert r.returncode == 0, r.stdout[-2000:]
tues = surv = 0
survivants = []
try:
    for nom, a, b in M:
        txt = orig.decode()
        assert txt.count(a) == 1, (nom, txt.count(a))
        open(MOD, "w").write(txt.replace(a, b))
        r = subprocess.run([sys.executable, "-m", "pytest", "-x", "-q", "-p", "no:cacheprovider", ESSAIS], cwd=COPIE,
                           env=env, capture_output=True)
        open(MOD, "wb").write(orig)
        if r.returncode:
            tues += 1; print(f"    tué       : {nom}")
        else:
            surv += 1; survivants.append(nom); print(f"    SURVIVANT : {nom}")
finally:
    open(MOD, "wb").write(orig)
h1 = hashlib.sha256(open(MOD, "rb").read()).hexdigest()
h_depot1 = hashlib.sha256(open(MOD_DEPOT, "rb").read()).hexdigest()
assert h1 == h0 == h_depot0 == h_depot1
print(f"    {len(M)} mutants : {tues} tués, {surv} survivants ; copie restaurée, module du dépôt intact ({h_depot1[:16]}…)")
