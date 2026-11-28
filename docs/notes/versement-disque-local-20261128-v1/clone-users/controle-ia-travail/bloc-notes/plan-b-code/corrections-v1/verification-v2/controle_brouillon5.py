"""Vérification (R2, vérificateur neuf) du brouillon 5 face au code du clone : annexe A (octets, commande de
`LISEZMOI.md`, garde du code, artefacts) ; table « Configuration » (lanceur et lecteur) ; lignes de citation (texte tel
quel ; copie aux marqueurs remplis de valeurs factices de bonne forme ; artefacts par intitulé). Seuls des empreintes
de fichiers scellés et la configuration du manifeste du pilote sont lus ; aucun contenu n'est affiché.
Copies écrites sous <travail>, effacées à la fin (sauf la copie exacte du brouillon 5 pour la commande de LISEZMOI).
Usage : PYTHONPATH=<clone>/src python -B controle_brouillon5.py <brouillon 5> <clone> <travail>"""
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
from controle_ia.harnais.validation_reelle import COMMIT_CITE, exiger_code_cite

B5, D, W = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
W.mkdir(parents=True, exist_ok=True)
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()  # noqa: E731
RS1 = D / "docs/sources/invites-plan-b-v1/invites/RS1.txt"
SHA_RS1 = "b1e3e003daf2c64bb317fe5623495f73ec25e7a703c5d799ceb1ab8c1eb042e7"
octets = B5.read_bytes()
texte = octets.decode("utf-8")
print("brouillon 5 :", sha(B5), len(texte.split("\n")) - 1, "lignes")
print("RS1.txt :", sha(RS1), "=", SHA_RS1, ":", sha(RS1) == SHA_RS1)


def essai(nom, f, *a):
    try:
        r = f(*a)
        print(f"  {nom} : passe -> {r}")
        return r
    except GardeArret as e:
        print(f"  {nom} : ARRÊT : {e}")
        return None


# ---------------------------------------------------------------- A. annexe A
print("\n== A. annexe A")
L = octets.split(b"\n")
debuts = [i + 1 for i, x in enumerate(L) if x == b"    ## Scoring Rubric"]
fins = [i + 1 for i, x in enumerate(L) if x.startswith(b"    - Do not write any analysis.")]
print("lignes de début (n°) :", debuts, "; lignes de fin (n°) :", fins)
bloc = L[debuts[0] - 1:fins[-1]]
assert all(not x or x.startswith(b"    ") for x in bloc)
extrait = b"\n".join(x[4:] for x in bloc) + b"\n"
attendu = RS1.read_bytes()
print("extraction indépendante (octets) :", len(extrait), "octets ; égale à RS1.txt :", extrait == attendu,
      "; sha256", hashlib.sha256(extrait).hexdigest())
print("RS1.txt : ASCII", all(b < 128 for b in attendu), "; sans CR", b"\r" not in attendu,
      "; sans espace de fin", not any(x.endswith(b" ") for x in attendu.split(b"\n")),
      "; une seule fin de ligne finale", attendu.endswith(b"\n") and not attendu.endswith(b"\n\n"))
# commande de LISEZMOI.md, extraite du fichier et jouée telle qu'écrite, sur une copie nommée comme au scellement
lisezmoi = (D / "docs/sources/invites-plan-b-v1/LISEZMOI.md").read_text(encoding="utf-8")
commande = [x for x in lisezmoi.split("\n") if x.startswith("python3 -I -c ")]
assert len(commande) == 1
argv = shlex.split(commande[0])
dl = W / "lisezmoi"
dl.mkdir(exist_ok=True)


def lisezmoi_sur(contenu: bytes) -> str:
    (dl / "T0.5-plan-B-juges-v1.md").write_bytes(contenu)
    p = subprocess.run([sys.executable] + argv[1:], cwd=dl, capture_output=True, text=True)
    return p.stdout.strip() if p.returncode == 0 else f"échec ({p.stderr.strip().splitlines()[-1]})"


print("commande de LISEZMOI.md (python3 -I -c …), copie exacte du brouillon 5 :", lisezmoi_sur(octets))
pb = subprocess.run(["python3", "-V"], capture_output=True, text=True)
p3 = subprocess.run(argv, cwd=dl, capture_output=True, text=True)
print(f"  même commande avec le python3 du système ({pb.stdout.strip() or pb.stderr.strip()}) :", p3.stdout.strip())
print("  copie de la commande (empreinte = brouillon 5) :", sha(dl / "T0.5-plan-B-juges-v1.md") == sha(B5))
c = dl / "copie-garde.md"
c.write_bytes(octets)
essai("exiger_annexe_a_egale_a_rs1 (brouillon 5, cas sain)", rs.exiger_annexe_a_egale_a_rs1, c)
lb = texte.split("\n")
d0, f0 = debuts[0] - 1, fins[-1] - 1
i_mot = next(i for i in range(d0 + 10, f0) if re.search(r"[a-z]\.$", lb[i]))      # une ligne finie par « x. »
annexe_b = next(i for i, x in enumerate(lb) if x.startswith("## Annexe B"))
artefacts = {
    "un caractère changé dans l'annexe": lb[:i_mot] + [lb[i_mot][:-1] + ";"] + lb[i_mot + 1:],
    "ligne vide de plus dans l'annexe": lb[:d0 + 1] + [""] + lb[d0 + 1:],
    "retrait manquant (une ligne)": lb[:d0 + 2] + [lb[d0 + 2].lstrip(" ") or "x"] + lb[d0 + 3:],
    "seconde ligne de fin après l'annexe B": lb[:annexe_b + 1] + [lb[f0]] + lb[annexe_b + 1:],
    "seconde ligne de début avant l'annexe": lb[:d0] + [lb[d0], ""] + lb[d0:],
    "ligne de fin retirée": lb[:f0] + lb[f0 + 1:],
}
for nom, lignes in artefacts.items():
    contenu = "\n".join(lignes)
    c.write_text(contenu, encoding="utf-8")
    r = essai(f"artefact « {nom} »", rs.exiger_annexe_a_egale_a_rs1, c)
    h = lisezmoi_sur(contenu.encode("utf-8"))
    print(f"    commande de LISEZMOI.md : {h[:16]}… ; = RS1 : {h == SHA_RS1} ; accord avec la garde : "
          f"{(h == SHA_RS1) == (r is not None)}")
(dl / "T0.5-plan-B-juges-v1.md").write_bytes(octets)          # la copie gardée est le brouillon 5 exact
c.unlink()

# ---------------------------------------------------------------- B. table « Configuration »
print("\n== B. table « Configuration »")
debut = texte.index("**Configuration** (`prereg/T0.5-plan-B-juges-config-v1.json`")
fin = texte.index("**Avant le scellement**", debut)
config = {}
for x in texte[debut:fin].split("\n"):
    m = re.match(r"^\| `([a-z_0-9]+)` \| `(.*)` \| .* \|$", x)
    if m:
        assert m[1] not in config, m[1]
        config[m[1]] = json.loads(m[2])
print("clés :", len(config), "; ordre de rq.CLES :", list(config) == list(rq.CLES),
      "; en plus :", sorted(set(config) - set(rq.CLES)), "; en moins :", sorted(set(rq.CLES) - set(config)))
essai("rq.exiger_config_planb", rq.exiger_config_planb, config)
print("  écarts à lr.CONSTANTES_CONFIG :", {k: (config.get(k), v) for k, v in lr.CONSTANTES_CONFIG.items()
                                           if k not in config or config[k] != v})
essai("lr.exiger_config_de_l_etape (rend lot_juge)", lr.exiger_config_de_l_etape, {"config": config},
      config["run_pilote"], config["manifeste_pilote_sha256"], config["run_notations"])
mp = json.loads((D / "runs" / config["run_pilote"] / "manifeste.json").read_text(encoding="utf-8"))
essai("rq.exiger_egal_au_pilote_planb (mode jouet : sans les versions)", rq.exiger_egal_au_pilote_planb, config,
      {"manifeste": mp}, "jouet")
print("  manifeste_pilote_sha256 = empreinte du manifeste du pilote :",
      config["manifeste_pilote_sha256"] == sha(D / "runs" / config["run_pilote"] / "manifeste.json"))
print("  couverture_jetons = lr.SEUILS_COUVERTURE :", config["couverture_jetons"] == lr.SEUILS_COUVERTURE)
print("  invite_rs1.sha256 = RS1.txt :", config["invite_rs1"]["sha256"] == sha(RS1))
essai("rq.exiger_invites_planb (invites chargées, configuration)", lambda: rq.exiger_invites_planb(config)["sha256"])
cfg_sha = empreinte_config(config)
print("  empreinte canonique :", cfg_sha)
for nom, v in (("lot_juge absent", None), ("lot_juge 0", 0), ("lot_juge \"8\"", "8")):
    c2 = {k: x for k, x in config.items() if k != "lot_juge"}
    if v is not None:
        c2["lot_juge"] = v
    essai(f"artefact « {nom} », lecteur", lr.exiger_config_de_l_etape, {"config": c2}, config["run_pilote"],
          config["manifeste_pilote_sha256"], config["run_notations"])
    essai(f"artefact « {nom} », lanceur", rq.exiger_config_planb, c2)

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
# valeurs du texte, lues hors des gardes, face aux fichiers du clone et à la section « Pièces scellées »
for nom, rx in rq.CITATIONS.items():
    v = rx.findall(texte)
    if nom in attendus:
        print(f"  {nom:24s} texte {v} ; fichier = texte : {v == [str(attendus[nom])]} ; ailleurs dans le texte : "
              f"{texte.count(str(attendus[nom])) - 1}")
for j, h in notations.items():
    print(f"  notations {j:15s} fichier = texte : {rq.NOTATIONS_CITEES.findall(texte).count((j, h)) == 1}")
print("texte tel quel :")
essai("exiger_code_cite", exiger_code_cite, D, B5)
essai("exiger_citations_planb", rq.exiger_citations_planb, B5, attendus, notations)
commit = subprocess.run(["git", "-C", str(D), "rev-parse", "HEAD"], capture_output=True, text=True,
                        check=True).stdout.strip()
racine_git = subprocess.run(["git", "-C", str(D), "rev-list", "--max-parents=0", "HEAD"], capture_output=True,
                            text=True, check=True).stdout.split()[0]
FACTICES = {"COMMIT_CODE": commit, "EMPREINTE_CONFIG": cfg_sha, "ENTROPIE": "271828182845904523536028747135266249",
            "TESTS_ATTENDUS": "413", "SHA256_AMORCE": "ab" * 32, "SHA256_SCRIPT_INSTANCE": "cd" * 32}
dc = W / "citations"
dc.mkdir(exist_ok=True)
p = dc / "T0.5-plan-B-juges-v1-rempli.md"


def remplir(t: str, quels) -> str:
    for k in quels:
        t = t.replace(f"`<<{k}>>`", f"`{FACTICES[k]}`")
    return t


try:
    trois = ("COMMIT_CODE", "EMPREINTE_CONFIG", "ENTROPIE")
    partiel = remplir(texte, trois)
    p.write_text(partiel, encoding="utf-8")
    print("copie aux trois marqueurs du lanceur remplis (marqueurs de la chaîne restants :",
          sorted(set(re.findall(r"<<([A-Z_0-9]+)>>", partiel))), ")")
    essai("exiger_code_cite", exiger_code_cite, D, p)
    essai("exiger_citations_planb", rq.exiger_citations_planb, p, attendus, notations)
    rempli = remplir(texte, FACTICES)
    p.write_text(rempli, encoding="utf-8")
    print("copie aux six marqueurs remplis ; marqueurs restants :", re.findall(r"<<[A-Z_0-9]+>>", rempli))
    for nom, rx in list(rq.CITATIONS.items()) + [("commit (COMMIT_CITE)", COMMIT_CITE)]:
        print(f"  {nom:24s} occurrences : {len(rx.findall(rempli))}")
    print(f"  {'notations par juge':24s} occurrences : {rq.NOTATIONS_CITEES.findall(rempli)}")
    print("chaîne du lanceur sur la copie remplie (ordre d'`executer`) :")
    essai("exiger_code_cite", exiger_code_cite, D, p)
    essai("exiger_citations_planb (rend l'entropie)", rq.exiger_citations_planb, p, attendus, notations)
    essai("exiger_annexe_a_egale_a_rs1 (lanceur et lecteur)", rs.exiger_annexe_a_egale_a_rs1, p)
    print("artefacts (copie remplie, une altération chacun) :")
    q = dc / "artefact.md"
    lignes_cit = {"commit du code d'analyse": "- Commit du code d'analyse : `",
                  "configuration": "- Configuration du plan B (empreinte canonique) : `",
                  "run du pilote": "- Run du pilote requalifié : `", "manifeste du pilote": "- Manifeste du pilote requalifié : `",
                  "épisodes du pilote": "- Épisodes du pilote requalifié : `", "tâches": "- Tâches du pilote : `",
                  "run des notations": "- Run des notations rejoué : `",
                  "manifeste des notations": "- Manifeste des notations rejoué : `",
                  "résumé des notations": "- Résumé des notations rejoué : `", "invite RS1": "- Invite RS1 : `",
                  "index de l'invite RS1": "- Index de l'invite RS1 : `", "entropie": "- Entropie : `",
                  "notations 8B": "- Notations rejouées du juge 8B : `", "notations 3B": "- Notations rejouées du juge 3B : `"}
    for nom, debut_l in lignes_cit.items():
        i = rempli.index(debut_l)
        j = rempli.index("`", i + len(debut_l))
        v = rempli[i + len(debut_l):j]
        if nom == "commit du code d'analyse":
            autre = racine_git
        elif nom.startswith("run"):
            autre = v[:16] + "autre"
        elif nom == "entropie":
            autre = "42"
        else:
            autre = ("0" if v[0] != "0" else "1") + v[1:]
        ligne = rempli[i:rempli.index("\n", i)]
        formes = {"différent": rempli.replace(ligne, ligne.replace(v, autre), 1),
                  "répété (deux valeurs)": rempli.replace(ligne, ligne + "\n" + ligne.replace(v, autre), 1),
                  "absent": rempli.replace(ligne + "\n", "", 1)}
        if nom == "entropie":
            del formes["différent"]
        for forme, t in formes.items():
            q.write_text(t, encoding="utf-8")
            arrets = []
            for g, a in (("exiger_code_cite", (D, q)), ("exiger_citations_planb", (q, attendus, notations))):
                try:
                    (exiger_code_cite if g == "exiger_code_cite" else rq.exiger_citations_planb)(*a)
                except GardeArret as e:
                    arrets.append(f"{g} : {str(e).replace(str(q), '<copie>')[:110]}")
            print(f"  {nom:24s} {forme:22s} -> {'ARRÊT ' + arrets[0] if arrets else 'ACCEPTÉ (défaut)'}")
        q.unlink()
finally:
    for x in dc.iterdir():
        print("effacé :", x.name, sha(x))
        x.unlink()
    dc.rmdir()
