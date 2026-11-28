"""Vérification VCB3 (R2, vérificateur neuf) du brouillon 6 face au code du clone.
A. annexe A : extraction indépendante en octets, commande de `LISEZMOI.md` jouée telle qu'écrite, garde du code,
   artefacts (garde et commande d'accord).
B. table « Configuration » : lanceur (`exiger_config_planb`, égalité au pilote, invites) et lecteur
   (`CONSTANTES_CONFIG`, `exiger_config_de_l_etape`) ; artefacts `lot_juge` et `max_nouveaux_juge`.
C. lignes de citation : texte tel quel ; copie aux six marqueurs remplis de valeurs factices de bonne forme ; marqueurs
   laissés un à un (VCB2-03) ; artefacts par intitulé ; même valeur répétée.
Seuls des empreintes de fichiers scellés et la configuration du manifeste du pilote sont lus ; aucun contenu scellé
n'est affiché. Les copies aux valeurs factices sont écrites sous <travail>/citations et effacées à la fin ; la copie
exacte du brouillon 6 pour la commande de LISEZMOI est gardée.
Usage : PYTHONPATH=<clone>/src python -B controle_brouillon6_v3.py <brouillon 6> <brouillon 5> <clone> <travail>"""
import hashlib
import json
import re
import shlex
import subprocess
import sys
from pathlib import Path

from controle_ia.environnements import lire_requalification as lr
from controle_ia.environnements import requalifier_juges as rq
from controle_ia.environnements import rubrique_simplifiee as rs
from controle_ia.environnements.lancer_pilote_a import empreinte_config
from controle_ia.gardes import GardeArret
from controle_ia.harnais.validation_reelle import COMMIT_CITE, ENTROPIE_CITEE, exiger_code_cite

B6, B5, D, W = (Path(x) for x in sys.argv[1:5])
W.mkdir(parents=True, exist_ok=True)


def sha(p) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def sha_b(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


RS1 = D / "docs/sources/invites-plan-b-v1/invites/RS1.txt"
SHA_RS1 = "b1e3e003daf2c64bb317fe5623495f73ec25e7a703c5d799ceb1ab8c1eb042e7"
SHA_B6 = "4a4184c0d62bb44213106b9f86ca078f15eb9c89c7b65a6a4010969af022ee33"
SHA_B5 = "1d6f1932d8597421caeedeff16e7d0175003921c40bc0173c133cbdb3ef768f2"
CFG_SHA_ATTENDUE = "8ff777cf903a104a94e9759d0b7dc1240d8e6c68ae58a0e52d225d4e80837b76"
octets = B6.read_bytes()
texte = octets.decode("utf-8")
bilan = {"ok": 0, "ko": 0}


def constat(nom: str, vrai: bool, detail="") -> None:
    bilan["ok" if vrai else "ko"] += 1
    print(f"  [{'OK' if vrai else 'ÉCART'}] {nom}{' : ' + str(detail) if detail != '' else ''}")


def garde(f, *a):
    """(passe, valeur ou message)"""
    try:
        return True, f(*a)
    except GardeArret as e:
        return False, str(e)


print("brouillon 6 :", sha(B6), texte.count("\n"), "lignes")
constat("empreinte du brouillon 6 = notes VCB2", sha(B6) == SHA_B6)
constat("empreinte du brouillon 5 = notes VCB2 (intact)", sha(B5) == SHA_B5)
constat("RS1.txt = b1e3e003…", sha(RS1) == SHA_RS1)

# ---------------------------------------------------------------- A. annexe A
print("\n== A. annexe A")
L = octets.split(b"\n")
debuts = [i + 1 for i, x in enumerate(L) if x == b"    ## Scoring Rubric"]
fins = [i + 1 for i, x in enumerate(L) if x.startswith(b"    - Do not write any analysis.")]
print("  lignes de début :", debuts, "; lignes de fin :", fins)
constat("une seule ligne de début et une seule ligne de fin dans tout le texte", len(debuts) == 1 and len(fins) == 1)
bloc = L[debuts[0] - 1:fins[-1]]
constat("chaque ligne non vide du bloc porte le retrait de quatre espaces",
        all(not x or x.startswith(b"    ") for x in bloc))
extrait = b"\n".join(x[4:] for x in bloc) + b"\n"
attendu = RS1.read_bytes()
constat("extraction indépendante = RS1.txt, octet pour octet", extrait == attendu,
        f"{len(extrait)} octets, sha256 {sha_b(extrait)}")
constat("RS1.txt : ASCII, sans CR, sans espace de fin, une seule fin de ligne finale",
        all(b < 128 for b in attendu) and b"\r" not in attendu
        and not any(x.endswith((b" ", b"\t")) for x in attendu.split(b"\n"))
        and attendu.endswith(b"\n") and not attendu.endswith(b"\n\n"))
L5 = B5.read_bytes().split(b"\n")
d5 = [i for i, x in enumerate(L5) if x == b"    ## Scoring Rubric"]
f5 = [i for i, x in enumerate(L5) if x.startswith(b"    - Do not write any analysis.")]
constat("bloc de l'annexe A du brouillon 6 = celui du brouillon 5 (octets)", bloc == L5[d5[0]:f5[-1] + 1])
# texte de l'annexe A, de son titre à l'annexe B : différences entre brouillons 5 et 6 (introduction seule attendue)
t5 = B5.read_text(encoding="utf-8")
a6 = texte[texte.index("## Annexe A"):texte.index("## Annexe B")]
a5 = t5[t5.index("## Annexe A"):t5.index("## Annexe B")]
diff_a = [i for i, (x, y) in enumerate(zip(a5.split("\n"), a6.split("\n"))) if x != y]
print("  lignes de la section « Annexe A » qui diffèrent (rang dans la section) :", diff_a,
      "; nombre de lignes", len(a5.split("\n")), len(a6.split("\n")))
lisezmoi = (D / "docs/sources/invites-plan-b-v1/LISEZMOI.md").read_text(encoding="utf-8")
commande = [x for x in lisezmoi.split("\n") if x.startswith("python3 -I -c ")]
constat("une seule commande « python3 -I -c » dans LISEZMOI.md", len(commande) == 1)
dl = W / "lisezmoi"
dl.mkdir(exist_ok=True)
copie_exacte = dl / "T0.5-plan-B-juges-v1.md"


def commande_sur(contenu: bytes, python=None) -> str:
    copie_exacte.write_bytes(contenu)
    if python is None:          # telle qu'écrite, par le shell
        p = subprocess.run(["bash", "-c", commande[0]], cwd=dl, capture_output=True, text=True)
    else:
        p = subprocess.run([python] + shlex.split(commande[0])[1:], cwd=dl, capture_output=True, text=True)
    return p.stdout.strip() if p.returncode == 0 else f"échec ({(p.stderr.strip().splitlines() or ['?'])[-1]})"


h_shell = commande_sur(octets)
v3 = subprocess.run(["bash", "-c", "python3 -V"], capture_output=True, text=True).stdout.strip()
constat(f"commande de LISEZMOI.md telle qu'écrite (bash, {v3}), copie exacte du brouillon 6", h_shell == SHA_RS1,
        h_shell)
h_venv = commande_sur(octets, sys.executable)
constat("même commande, Python du venv", h_venv == SHA_RS1, h_venv)
constat("copie gardée = brouillon 6", sha(copie_exacte) == SHA_B6)
c = W / "copie-garde-annexe.md"
c.write_bytes(octets)
ok, r = garde(rs.exiger_annexe_a_egale_a_rs1, c)
constat("exiger_annexe_a_egale_a_rs1, brouillon 6 (cas sain)", ok and r == SHA_RS1, r)
lb = texte.split("\n")
d0, f0 = debuts[0] - 1, fins[-1] - 1
i_point = next(i for i in range(d0 + 5, f0) if lb[i].endswith("."))
i_annexe_b = next(i for i, x in enumerate(lb) if x.startswith("## Annexe B"))
i_vide = next(i for i in range(d0, f0) if lb[i] == "")
artefacts = {
    "un caractère changé (point final en point-virgule)": lb[:i_point] + [lb[i_point][:-1] + ";"] + lb[i_point + 1:],
    "une espace de fin ajoutée à une ligne": lb[:i_point] + [lb[i_point] + " "] + lb[i_point + 1:],
    "ligne vide de plus dans le bloc": lb[:i_vide] + [""] + lb[i_vide:],
    "ligne vide du bloc retirée": lb[:i_vide] + lb[i_vide + 1:],
    "retrait de trois espaces sur une ligne": lb[:d0 + 2] + [lb[d0 + 2][1:]] + lb[d0 + 3:],
    "seconde ligne de fin après l'annexe B": lb[:i_annexe_b + 1] + [lb[f0]] + lb[i_annexe_b + 1:],
    "seconde ligne de début avant l'annexe": lb[:d0] + [lb[d0], ""] + lb[d0:],
    "ligne de fin retirée": lb[:f0] + lb[f0 + 1:],
    "ligne de début retirée": lb[:d0] + lb[d0 + 1:],
}
# fins de ligne CRLF dans le bloc : la garde et la commande lisent en mode texte (fins de ligne universelles) ; on
# exige seulement leur accord (information)
crlf = "\n".join(lb[:d0] + [x + "\r" for x in lb[d0:f0 + 1]] + lb[f0 + 1:])
for nom, lignes in artefacts.items():
    contenu = "\n".join(lignes)
    c.write_text(contenu, encoding="utf-8", newline="")
    ok, r = garde(rs.exiger_annexe_a_egale_a_rs1, c)
    h = commande_sur(contenu.encode("utf-8"))
    constat(f"artefact « {nom} » : la garde arrête ; la commande ne rend pas RS1", (not ok) and h != SHA_RS1,
            f"garde : {str(r)[:90]} ; commande : {h[:20]}")
c.write_text(crlf, encoding="utf-8", newline="")
constat("artefact CRLF écrit tel quel (octets \\r présents)", b"\r\n" in c.read_bytes())
ok, r = garde(rs.exiger_annexe_a_egale_a_rs1, c)
h = commande_sur(crlf.encode("utf-8"))
constat("fins de ligne CRLF dans le bloc (information) : la garde et la commande s'accordent", ok == (h == SHA_RS1),
        f"garde : {'passe' if ok else 'arrête'} ; commande : {h[:20]}")
copie_exacte.write_bytes(octets)
constat("copie gardée remise au brouillon 6 exact", sha(copie_exacte) == SHA_B6)
c.unlink()

# ---------------------------------------------------------------- B. table « Configuration »
print("\n== B. table « Configuration »")
debut = texte.index("**Configuration** (`prereg/T0.5-plan-B-juges-config-v1.json`")
fin = texte.index("**Avant le scellement**", debut)
config, rangs = {}, {}
for n, x in enumerate(texte[debut:fin].split("\n")):
    m = re.match(r"^\| `([a-z_0-9]+)` \| `(.*)` \| (.*) \|$", x)
    if m:
        constat(f"clé {m[1]} unique dans la table", m[1] not in config) if m[1] in config else None
        config[m[1]] = json.loads(m[2])
        rangs[m[1]] = texte[:debut].count("\n") + n + 1
print("  clés :", len(config), "; lignes", min(rangs.values()), "à", max(rangs.values()))
constat("50 clés, dans l'ordre de rq.CLES, aucune en plus ni en moins", list(config) == list(rq.CLES),
        f"en plus {sorted(set(config) - set(rq.CLES))}, en moins {sorted(set(rq.CLES) - set(config))}")
constat("lignes de lot_juge et de max_nouveaux_juge (339, 340)",
        (rangs["lot_juge"], rangs["max_nouveaux_juge"]) == (339, 340), (rangs["lot_juge"], rangs["max_nouveaux_juge"]))
ok, r = garde(rq.exiger_config_planb, config)
constat("lanceur : exiger_config_planb accepte la table", ok, r)
ecarts = {k: (config.get(k), v) for k, v in lr.CONSTANTES_CONFIG.items() if k not in config or config[k] != v}
constat("lecteur : aucun écart à CONSTANTES_CONFIG", not ecarts, ecarts)
ok, r = garde(lr.exiger_config_de_l_etape, {"config": config}, config["run_pilote"], config["manifeste_pilote_sha256"],
              config["run_notations"])
constat("lecteur : exiger_config_de_l_etape accepte la table et rend lot_juge = 8", ok and r == 8, r)
mp = json.loads((D / "runs" / config["run_pilote"] / "manifeste.json").read_text(encoding="utf-8"))
ok, r = garde(rq.exiger_egal_au_pilote_planb, config, {"manifeste": {"config": mp["config"]}}, "jouet")
constat("lanceur : exiger_egal_au_pilote_planb face à la configuration du manifeste du pilote (versions non comparées)",
        ok, r)
pc = json.loads((D / "prereg/T0.5-pilote-config-v1.json").read_text(encoding="utf-8"))
constat("clés égales au pilote = prereg/T0.5-pilote-config-v1.json",
        all(config[k] == pc.get(k) for k in rq.CLES_EGALES_AU_PILOTE),
        [k for k in rq.CLES_EGALES_AU_PILOTE if config[k] != pc.get(k)])
constat("variante_rejeu = variante_juge du pilote", config["variante_rejeu"] == mp["config"].get("variante_juge"))
constat("manifeste_pilote_sha256 = empreinte du manifeste du pilote",
        config["manifeste_pilote_sha256"] == sha(D / "runs" / config["run_pilote"] / "manifeste.json"))
constat("couverture_jetons = lr.SEUILS_COUVERTURE", config["couverture_jetons"] == lr.SEUILS_COUVERTURE)
ok, r = garde(lambda: rq.exiger_invites_planb(config))
constat("lanceur : exiger_invites_planb accepte invite_rs1 (RS1 chargée, index)", ok and r["sha256"] == SHA_RS1,
        r if not ok else r["index_sha256"])
cfg_sha = empreinte_config(config)
constat("empreinte canonique de la table = 8ff777cf… (inchangée)", cfg_sha == CFG_SHA_ATTENDUE, cfg_sha)
g = config["duree_globale_s"]
constat("chaîne des limites : 23 700 + 900 + 120 = 24 720 ; + 300 + 2 700 = 27 720 ; + 600 = 28 320",
        (config["delai_externe_s"], config["plafond_amorce_s"], config["surveillance_s"]) == (24720, 27720, 28320))
# configuration des tests (`_config_reelle`) face à la table
sys.path.insert(0, str(D / "tests"))
try:
    import test_plan_b_requalifier as tq            # noqa: E402
    cr = tq._config_reelle()
    diff_t = sorted(k for k in set(cr) | set(config) if cr.get(k) != config.get(k))
    constat("`_config_reelle()` des tests = table, sauf manifeste_pilote_sha256 (factice dans les tests)",
            diff_t == ["manifeste_pilote_sha256"], diff_t)
except Exception as e:                               # import des tests impossible : signalé, sans repli
    constat("`_config_reelle()` des tests importée", False, repr(e)[:200])
# artefacts au lanceur et au lecteur
for cle, valeurs in (("lot_juge", (None, 0, -8, "8", 8.0, True)),
                     ("max_nouveaux_juge", (None, 0, -3072, "3072", 3072.0, True))):
    for v in valeurs:
        c2 = {k: x for k, x in config.items() if k != cle}
        if v is not None:
            c2[cle] = v
        okl, rl = garde(lr.exiger_config_de_l_etape, {"config": c2}, config["run_pilote"],
                        config["manifeste_pilote_sha256"], config["run_notations"])
        okq, rq_ = garde(rq.exiger_config_planb, c2)
        nom = "absent" if v is None else repr(v)
        constat(f"artefact {cle} {nom} : arrêt au lecteur et au lanceur", (not okl) and (not okq),
                f"lecteur : {str(rl)[:80]} | lanceur : {str(rq_)[:60]}")
c3 = dict(config, tolerance_simple=0.004)
okl, rl = garde(lr.exiger_config_de_l_etape, {"config": c3}, config["run_pilote"], config["manifeste_pilote_sha256"],
                config["run_notations"])
constat("artefact tolerance_simple 0.004 : arrêt au lecteur (seuil gelé)", not okl, str(rl)[:100])
c4 = dict(config, max_nouveaux_juge=3072.0)
okp, rp_ = garde(rq.exiger_egal_au_pilote_planb, c4, {"manifeste": {"config": mp["config"]}}, "jouet")
print(f"  (information) max_nouveaux_juge 3072.0 face au pilote seul : {'accepté' if okp else 'arrêt : ' + rp_[:60]}"
      " ; c'est exiger_config_planb qui l'arrête au lanceur")

# ---------------------------------------------------------------- C. lignes de citation
print("\n== C. lignes de citation")
rp, rn = config["run_pilote"], config["run_notations"]
attendus = {"configuration": cfg_sha, "run du pilote": rp,
            "manifeste du pilote": sha(D / "runs" / rp / "manifeste.json"),
            "épisodes du pilote": sha(D / "diag" / rp / "episodes.json"),
            "tâches": sha(D / "donnees/t05-pilote-v1/taches-pilote-60-v1.json"), "run des notations": rn,
            "manifeste des notations": sha(D / "runs" / rn / "manifeste.json"),
            "résumé des notations": sha(D / "diag" / rn / "resume.json"),
            "invite RS1": sha(RS1), "index de l'invite RS1": sha(D / "docs/sources/invites-plan-b-v1/index.json")}
notations = {j: sha(D / "diag" / rn / f"notations-{j}-decisives.json") for j in ("8B", "3B")}
for nom, rx in rq.CITATIONS.items():
    if nom == "configuration":
        constat("« configuration » : marqueur dans le texte, aucune valeur lue",
                rx.findall(texte) == [] and "Configuration du plan B (empreinte canonique) : `<<EMPREINTE_CONFIG>>`"
                in texte)
    elif nom in attendus:
        v = rx.findall(texte)
        constat(f"valeur citée « {nom} » = fichier du clone (une seule occurrence)", v == [str(attendus[nom])], v)
for j, h in notations.items():
    constat(f"valeur citée « notations {j} » = fichier du clone (une seule occurrence)",
            rq.NOTATIONS_CITEES.findall(texte).count((j, h)) == 1)
print("  texte tel quel :")
ok1, r1 = garde(exiger_code_cite, D, B6)
ok2, r2 = garde(rq.exiger_citations_planb, B6, attendus, notations)
constat("texte tel quel refusé par exiger_code_cite et par exiger_citations_planb", not ok1 and not ok2,
        f"{r1.replace(str(B6), '<b6>')[:70]} | {r2.replace(str(B6), '<b6>')[:70]}")
commit = subprocess.run(["git", "-C", str(D), "rev-parse", "HEAD"], capture_output=True, text=True,
                        check=True).stdout.strip()
racine_git = subprocess.run(["git", "-C", str(D), "rev-list", "--max-parents=0", "HEAD"], capture_output=True,
                            text=True, check=True).stdout.split()[0]
FACTICES = {"COMMIT_CODE": commit, "EMPREINTE_CONFIG": cfg_sha, "ENTROPIE": "314159265358979323846264338327950288",
            "TESTS_ATTENDUS": "4321", "SHA256_AMORCE": "e7" * 32, "SHA256_SCRIPT_INSTANCE": "5a" * 32}
marqueurs = sorted(set(re.findall(r"<<([A-Z_0-9]+)>>", texte)))
constat("marqueurs du texte : les six de l'en-tête", marqueurs == sorted(FACTICES), marqueurs)
for k in FACTICES:
    print(f"    <<{k}>> : {texte.count(f'<<{k}>>')} occurrence(s), dont {texte.count(f'`<<{k}>>`')} entre accents graves")
dc = W / "citations"
dc.mkdir(exist_ok=True)
p = dc / "T0.5-plan-B-juges-v1-rempli.md"


def remplir(t: str, quels) -> str:
    for k in quels:
        t = t.replace(f"`<<{k}>>`", f"`{FACTICES[k]}`")
    return t


def chaine(chemin: Path):
    """Gardes de citation du lanceur, dans l'ordre d'`executer` ; rend (passe, message ou entropie)."""
    ok, r = garde(exiger_code_cite, D, chemin)
    if not ok:
        return False, "exiger_code_cite : " + r.replace(str(chemin), "<copie>")
    ok, r = garde(rq.exiger_citations_planb, chemin, attendus, notations)
    if not ok:
        return False, "exiger_citations_planb : " + r.replace(str(chemin), "<copie>")
    return True, r


try:
    # VCB2-03 : chaque marqueur du lanceur laissé seul ; les trois de la chaîne laissés seuls
    for k in ("COMMIT_CODE", "EMPREINTE_CONFIG", "ENTROPIE"):
        p.write_text(remplir(texte, [x for x in FACTICES if x != k]), encoding="utf-8")
        ok, r = chaine(p)
        constat(f"marqueur <<{k}>> laissé seul : les gardes du lanceur refusent", not ok, str(r)[:110])
    p.write_text(remplir(texte, ("COMMIT_CODE", "EMPREINTE_CONFIG", "ENTROPIE")), encoding="utf-8")
    ok, r = chaine(p)
    constat("les trois marqueurs de la chaîne laissés seuls : les gardes du lanceur passent (texte l. 10, VCB2-03)", ok,
            r)
    rempli = remplir(texte, FACTICES)
    p.write_text(rempli, encoding="utf-8")
    constat("copie remplie : aucun marqueur restant", not re.findall(r"<<[A-Z_0-9]+>>", rempli))
    occ = {nom: len(rx.findall(rempli)) for nom, rx in list(rq.CITATIONS.items()) + [("commit", COMMIT_CITE)]}
    constat("copie remplie : chaque intitulé une fois, commit compris", set(occ.values()) == {1}, occ)
    constat("copie remplie : notations 8B et 3B une fois chacune",
            sorted(j for j, _ in rq.NOTATIONS_CITEES.findall(rempli)) == ["3B", "8B"])
    ok, r = chaine(p)
    constat("copie remplie : exiger_code_cite puis exiger_citations_planb passent, entropie rendue",
            ok and r == int(FACTICES["ENTROPIE"]), r)
    ok, r = garde(rs.exiger_annexe_a_egale_a_rs1, p)
    constat("copie remplie : exiger_annexe_a_egale_a_rs1 passe (lanceur et lecteur)", ok and r == SHA_RS1, r)
    lignes_cit = {"commit": "- Commit du code d'analyse : `",
                  "configuration": "- Configuration du plan B (empreinte canonique) : `",
                  "run du pilote": "- Run du pilote requalifié : `",
                  "manifeste du pilote": "- Manifeste du pilote requalifié : `",
                  "épisodes du pilote": "- Épisodes du pilote requalifié : `", "tâches": "- Tâches du pilote : `",
                  "run des notations": "- Run des notations rejoué : `",
                  "manifeste des notations": "- Manifeste des notations rejoué : `",
                  "résumé des notations": "- Résumé des notations rejoué : `", "invite RS1": "- Invite RS1 : `",
                  "index de l'invite RS1": "- Index de l'invite RS1 : `", "entropie": "- Entropie : `",
                  "notations 8B": "- Notations rejouées du juge 8B : `",
                  "notations 3B": "- Notations rejouées du juge 3B : `"}
    print("  artefacts sur la copie remplie (une altération chacun) :")
    n_formes = 0
    for nom, debut_l in lignes_cit.items():
        constat(f"ligne « {nom} » présente une fois dans la copie remplie", rempli.count(debut_l) == 1)
        i = rempli.index(debut_l)
        j = rempli.index("`", i + len(debut_l))
        v = rempli[i + len(debut_l):j]
        ligne = rempli[i:rempli.index("\n", i)]
        if nom == "commit":
            autres = {"racine du dépôt": racine_git, "commit inexistant": "0123456789abcdef" * 2 + "01234567"}
        elif nom.startswith("run"):
            autres = {"": v[:16] + "autre-run"}
        elif nom == "entropie":
            autres = {}
        else:
            autres = {"": ("f" if v[0] != "f" else "e") + v[1:]}
        formes = {"absent": rempli.replace(ligne + "\n", "", 1)}
        for etiquette, autre in autres.items():
            suffixe = f" ({etiquette})" if etiquette else ""
            formes[f"différent{suffixe}"] = rempli.replace(ligne, ligne.replace(v, autre), 1)
            formes[f"répété, deux valeurs{suffixe}"] = rempli.replace(ligne, ligne + "\n" + ligne.replace(v, autre), 1)
        if nom == "entropie":
            formes["répété, deux valeurs"] = rempli.replace(ligne, ligne + "\n" + ligne.replace(v, "42"), 1)
        for forme, t in formes.items():
            p.write_text(t, encoding="utf-8")
            ok, r = chaine(p)
            n_formes += 1
            constat(f"{nom} — {forme} : arrêt", not ok, str(r)[:105])
        # même valeur répétée : une seule valeur, acceptée
        p.write_text(rempli.replace(ligne, ligne + "\n" + ligne, 1), encoding="utf-8")
        ok, r = chaine(p)
        print(f"    (information) {nom} — répété, même valeur : {'accepté' if ok else 'ARRÊT ' + str(r)[:80]}")
    print("  formes d'artefact essayées :", n_formes)
    # commit cité deux fois, deux valeurs, dont la seconde ailleurs dans le texte : `exiger_code_cite` lit la première
    p.write_text(rempli + f"\nCommit du code d'analyse : `{racine_git}`\n", encoding="utf-8")
    okc, rc = garde(exiger_code_cite, D, p)
    okp, rp2 = garde(rq.exiger_citations_planb, p, attendus, notations)
    constat("commit répété en fin de texte, autre valeur : exiger_code_cite passe (première occurrence), "
            "exiger_citations_planb arrête", okc and not okp, f"{str(rc)[:12]} | {str(rp2).replace(str(p), '<copie>')[:80]}")
finally:
    for x in sorted(dc.iterdir()):
        print("  effacé :", x.name, sha(x))
        x.unlink()
    dc.rmdir()

# ---------------------------------------------------------------- D. lignes citées par le traitement (brouillon 6)
print("\n== D. lignes du brouillon 6 citées par le traitement et les notes VCB2")
for n in (10, 37, 264, 302, 339, 340, 386, 501, 504, 518, 519, 532, 534, 565, 572, 580, 583, 590, 647):
    print(f"  l. {n} : {lb[n - 1][:110]}")
print(f"\nbilan : {bilan['ok']} contrôles conformes, {bilan['ko']} écarts")
