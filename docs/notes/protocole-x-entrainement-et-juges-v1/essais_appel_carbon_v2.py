"""Essais des gardes de appel_carbon_protocole_x_v2.py, sur un cas sain et sur des artefacts (R5). Aucun envoi : les
clés sont retirées de l'environnement des essais, et chaque essai tourne sur une copie du dossier dans un dossier
temporaire. Usage : python essais_appel_carbon_v2.py (depuis la racine du dépôt). Sortie : une ligne par essai."""
import hashlib, os, shutil, subprocess, sys, tempfile

RACINE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
D = os.path.join(RACINE, "docs", "notes", "protocole-x-entrainement-et-juges-v1")
SCRIPT = os.path.join(D, "appel_carbon_protocole_x_v2.py")
ENV = {k: v for k, v in os.environ.items() if not k.startswith("GEMINI_API_KEY")}
ENV["PYTHONDONTWRITEBYTECODE"] = "1"
ACCORD = "GO-2026-11-24-16"
echecs = 0


def jouer(dossier, *args, optimise=False):
    cmd = [sys.executable] + (["-O"] if optimise else []) + [SCRIPT, dossier] + list(args)
    r = subprocess.run(cmd, capture_output=True, text=True, env=ENV, cwd=RACINE)
    return r.returncode, (r.stdout + r.stderr).strip().splitlines()[-1][:110] if (r.stdout + r.stderr).strip() else ""


def copie():
    t = tempfile.mkdtemp(prefix="essais-carbon-")
    for nom in ("demandes-reformulees-quatre-points-v1.md", "dossier-faits-demande-1-v1.md", "dossier-faits-demande-2-v1.md"):
        shutil.copy(os.path.join(D, nom), t)
    return t


def empreinte_invite(dossier, n):
    return hashlib.sha256(open(os.path.join(dossier, f"invite-carbon-demande-{n}-v2.md"), "rb").read()).hexdigest()


def attendre(nom, code, attendu, ligne):
    global echecs
    ok = code == attendu
    echecs += 0 if ok else 1
    print(f"{'OK  ' if ok else 'ÉCHEC'} {nom} : code {code} (attendu {attendu}) | {ligne}")


for n in ("1", "2"):
    t = copie()
    attendre(f"cas sain à blanc, demande {n}", *jouer(t, n)[:1], 0, jouer(t, n)[1])
    e = empreinte_invite(t, n)
    attendre(f"cas sain à blanc sous -O, demande {n}", jouer(t, n, optimise=True)[0], 0, "")
    attendre(f"empreinte fausse, demande {n}", *jouer(t, n, "--envoyer", ACCORD, "0" * 64)[:1], 5, "")
    attendre(f"accord mal formé, demande {n}", *jouer(t, n, "--envoyer", "GO-2026", e)[:1], 6, "")
    attendre(f"accord absent du registre, demande {n}", *jouer(t, n, "--envoyer", "GO-2026-11-24-999", e)[:1], 6, "")
    attendre(f"accord qui ne nomme pas Carbon, demande {n}", *jouer(t, n, "--envoyer", "GO-2026-11-24-14", e)[:1], 6, "")
    attendre(f"arguments en trop, demande {n}", *jouer(t, n, "--envoyer", ACCORD, e, "x")[:1], 5, "")
    # sans clé : le cas sain complet s'arrête au contrôle de la clé, verrou retiré, rien ne part
    code, ligne = jouer(t, n, "--envoyer", ACCORD, e)
    attendre(f"cas sain sans clé (rien ne part), demande {n}", code, 5, ligne)
    attendre(f"verrou retiré après le refus de clé, demande {n}",
             int(os.path.exists(os.path.join(t, f"tentative-carbon-demande-{n}-v1.verrou"))), 0, "")
    # artefact : verrou déjà présent
    open(os.path.join(t, f"tentative-carbon-demande-{n}-v1.verrou"), "w").write("x")
    attendre(f"verrou présent, demande {n}", *jouer(t, n, "--envoyer", ACCORD, e)[:1], 3, "")
    os.remove(os.path.join(t, f"tentative-carbon-demande-{n}-v1.verrou"))
    # artefact : réponse déjà présente
    open(os.path.join(t, f"reponse-carbon-demande-{n}-v1-brute.jsonl"), "w").write("{}")
    attendre(f"réponse déjà présente, demande {n}", *jouer(t, n, "--envoyer", ACCORD, e)[:1], 3, "")
    # artefact : invite changée après coup
    t2 = copie(); jouer(t2, n)
    with open(os.path.join(t2, f"invite-carbon-demande-{n}-v2.md"), "a", encoding="utf-8") as f:
        f.write("ajout\n")
    attendre(f"invite changée après coup, demande {n}", jouer(t2, n)[0], 10, "")
    # artefacts : motifs interdits glissés dans le dossier de faits
    for nom, poison in (("nom de personne", "relu par Lazar"), ("nom accentué", "relu par Ćirić"),
                        ("identifiant d'accord", "sous GO-2026-11-24-16"), ("identifiant de registre", "ligne R-52"),
                        ("code de décision", "décision N-075"), ("code de tâche", "tâche T0.8"),
                        ("chemin", "voir docs/notes/x.md"), ("chemin de dossier", "voir papiers/A/x"),
                        ("courriel", "écrire à a.b@exemple.org"), ("session", "session_01Qi7Gr31b1s4znXx53GF1ik")):
        t3 = copie()
        p = os.path.join(t3, f"dossier-faits-demande-{n}-v1.md")
        texte = open(p, encoding="utf-8").read().replace("\n## B. ", f"\n{poison}\n\n## B. ", 1)
        open(p, "w", encoding="utf-8").write(texte)
        attendre(f"motif « {nom} », demande {n}", jouer(t3, n)[0], 4, "")
        shutil.rmtree(t3)
    # artefact : limite de mots retirée de la demande
    t4 = copie()
    p = os.path.join(t4, "demandes-reformulees-quatre-points-v1.md")
    open(p, "w", encoding="utf-8").write(open(p, encoding="utf-8").read().replace("3 500 mots", "9 000 mots"))
    attendre(f"limite de mots changée, demande {n}", jouer(t4, n)[0], 10, "")
    for d in (t, t2, t4):
        shutil.rmtree(d)
print("essais en échec :", echecs)
sys.exit(1 if echecs else 0)
