"""Appel unique à Carbon (gemini-4-carbon) pour une demande reformulée du protocole X « entraîner plutôt que détecter ;
juges de la base boîte noire ». Pièce d'instrument (classe B). Version 3.

v3 : copie de appel_carbon_protocole_x_v2.py (même dossier, gardé tel quel, R12), après la vérification de ses
corrections par le même contre-lecteur (« conformes avec remarques » ; envoi jugé possible). Durcissements, tous :
  (D1) l'accord cité doit figurer au registre sur une ligne unique qui nomme Carbon ET le protocole X (la v2
       acceptait toute ligne d'accord nommant Carbon) ; le commit de la branche principale distante lue est affiché
       et journalisé ;
  (D2) un envoi ne part que si DOSSIER est le dossier même de ce script : une copie du dossier ne peut pas envoyer
       (le verrou et la réponse y seraient absents) ; code de sortie 11 ;
  (D3) le module du collisionneur n'est chargé que si son empreinte égale son compagnon ;
  (D4) la lecture du corps d'un refus HTTP ne peut plus lever d'exception ;
  (D5) en-tête : le verrou est retiré dans deux cas, et deux seulement : refus HTTP avant tout traitement, et clé
       absente (constatée avant tout envoi). Les scripts v1 et v2 ne doivent plus servir à un envoi.

v2 : copie de appel_carbon_protocole_x_v1.py (même dossier, gardé tel quel, R12), corrigée après sa contre-lecture par
un Opus neuf (« conforme avec remarques », 24 novembre 2026). Corrections, toutes :
  (C1) les gardes qui étaient des `assert` sont des refus durs (`sys.exit` nommé) : elles tiennent sous `python -O` ;
  (C2) un verrou de tentative est créé en création exclusive avant tout envoi ; il empêche deux envois pour une même
       demande (deux processus, ou relance manuelle après une issue incertaine) ; il n'est retiré que si l'échec est un
       refus HTTP avant tout traitement (rien n'est facturé) ; toute autre issue le garde : une relance demande alors
       une décision nommée ;
  (C3) une coupure avant les en-têtes (erreur d'adresse, délai) ou en cours de flux est journalisée comme un défaut,
       avec son code de sortie ; le brut partiel est gardé ; jamais une réponse ;
  (C4) l'accord est contrôlé dans sa forme entière, puis cherché dans le registre des accords de la branche principale
       distante (ligne qui commence par son identifiant et nomme Carbon) ;
  (C5) garde de motifs : celle du collisionneur (`motifs_trouves`, noms accentués compris), plus des motifs propres
       (codes internes de décision, de tâche ou d'idée, chemins de dossiers du dépôt) ;
  (C6) la phrase qui introduit le dossier dans l'invite dit exactement ce qui est relu ce jour et ce qui est repris ;
       elle dit aussi d'où vient l'ordre de grandeur du budget et ce que désigne « le papier du programme ». Les
       invites deviennent des fichiers « v2 », d'empreintes neuves ; les invites v1 restent pour mémoire.

Par rapport au script d'origine (docs/notes/lecteur-synthese-verdicts-pour-lazar-01qi7-v1/appel_carbon_v2.py, branche
du lecteur des verdicts, employé sous GO-2026-11-24-10), les changements sont, tous déclarés :
  (1) l'invite est construite par ce script à partir de deux fichiers scellés (la demande reformulée et son dossier de
      faits), écrite sur disque telle qu'elle partira, puis relue : c'est ce fichier qui part, à l'octet ;
  (2) garde de motifs avant tout envoi : refus nommé, rien n'est retiré en silence ;
  (3) limite de mots 3 500 (au lieu de 1 200), contrôlée aussi dans le texte de l'invite ; plafond 3 USD par demande ;
  (4) l'empreinte de l'invite est exigée en argument de l'envoi : une invite changée après la contre-lecture ne part pas ;
  (5) journal : ligne « tentative », ligne « envoi accepté », bilan ; le modèle servi (`modelVersion`) est relevé ;
  (6) un défaut n'est jamais écrit sous le nom d'une réponse : son texte éventuel va dans un fichier « defaut-… »
      (le script d'origine écrivait le texte dans le fichier de réponse même en cas de défaut) ;
  (7) les corrections C1 à C6 ci-dessus.
Sans l'option --envoyer, rien ne part : seules la construction de l'invite, les gardes et l'estimation du pire cas sont
jouées. Clé lue par son nom (GEMINI_API_KEY, sinon GEMINI_API_KEY_2 ; jamais _3) ; jamais affichée ni journalisée.

Usage : python appel_carbon_protocole_x_v2.py DOSSIER N [--envoyer GO-AAAA-MM-JJ-NN EMPREINTE_DE_L_INVITE]
        N = 1 ou 2 (numéro de la demande).
Codes de sortie : 0 rien n'est parti (à blanc) ou réponse écrite ; 2 réglages refusés par la garde ; 3 une réponse ou un
verrou existe déjà ; 4 motif interdit ; 5 empreinte ou arguments ; 6 accord introuvable ou mal formé ; 7 issue
incertaine (coupure) ; 8 refus HTTP avant tout traitement ; 9 défaut de réponse ; 10 garde de construction ou de coût ;
11 DOSSIER n'est pas le dossier du script (aucun envoi d'une copie)."""
import hashlib, importlib.util, json, os, re, subprocess, sys, time, urllib.error, urllib.request

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.normpath(os.path.join(ICI, "..", "..", ".."))
sys.path.insert(0, os.path.join(RACINE, "src"))
from controle_ia.garde_google_v3 import verifier_reglages_google, defaut_reponse_google, VERSION_GARDE


def refuser(code, message):
    print(message)
    sys.exit(code)


if len(sys.argv) < 3 or sys.argv[2] not in ("1", "2"):
    refuser(5, "REFUS : usage DOSSIER N [--envoyer GO-… EMPREINTE], N = 1 ou 2")
S, N = sys.argv[1], sys.argv[2]
PROVISION, PLAFOND, MOTS, PLAFOND_USD = 49152, 65536, 3500, 3.0
PRIX_ENTREE, PRIX_SORTIE = 8.3e-6, 41.5e-6  # le plus haut des deux tarifs trouvés au dépôt (8,3 / 41,5 USD par million)

# (C5) garde de motifs du collisionneur, chargée sans écrire de fichier compilé, plus des motifs propres.
sys.dont_write_bytecode = True
_CHEMIN_COL = os.path.join(RACINE, "docs", "notes", "collisionneur-v9", "collisionneur_v9_v8m.py")
_attendue = open(_CHEMIN_COL + ".sha256", encoding="utf-8").read().split()[0]  # (D3) empreinte compagnon
if hashlib.sha256(open(_CHEMIN_COL, "rb").read()).hexdigest() != _attendue:
    refuser(10, "REFUS : le module de la garde de motifs du collisionneur ne répond pas à son empreinte")
_spec = importlib.util.spec_from_file_location("collisionneur_garde", _CHEMIN_COL)
_col = importlib.util.module_from_spec(_spec)
sys.modules["collisionneur_garde"] = _col
_spec.loader.exec_module(_col)
MOTIFS_PROPRES = {
    "code interne de décision, de tâche ou d'idée": re.compile(
        r"\b(?:N|P|R)-\d{1,5}\b|\bT\d\.\d\b|\bIDE-\d+\b|\bD-S\d+\b|\bK-\d+\b|\bDB8-\d\b"),
    "chemin de dossier du dépôt": re.compile(r"\b(?:papiers|livrables|scripts|tests|coffre|brouillons|donnees|src)/"),
    "prénom ou nom d'une personne du programme": re.compile(r"(?i)\bluc\b"),
}


def motifs_de(texte):
    trouves = [nom for nom, _position in _col.motifs_trouves(texte)]
    trouves += [nom for nom, motif in MOTIFS_PROPRES.items() if motif.search(texte)]
    return trouves


def bloc_demande(texte, n):
    """Le bloc « Demande reformulée (à servir telle quelle…) » de la demande n, sans son titre."""
    titre = f"### Demande reformulée (à servir telle quelle, avec le dossier de faits de la demande {n})"
    if texte.count(titre) != 1:
        refuser(10, f"REFUS : titre du bloc de la demande {n} absent ou répété")
    suite = texte.split(titre, 1)[1]
    fin = suite.find("\n---\n")
    return (suite if fin < 0 else suite[:fin]).strip()


def corps_dossier(texte, n):
    """Le dossier de faits depuis sa section A ; pour la demande 1, sans la table des sources (chemins internes)."""
    debut = texte.find("\n## A. ")
    if debut <= 0:
        refuser(10, "REFUS : section A du dossier absente")
    corps = texte[debut:]
    if n == "1":
        fin = corps.find("\n## F. Sources et empreintes")
        if fin <= 0:
            refuser(10, "REFUS : section F du dossier 1 absente")
        corps = corps[:fin]
    return corps.strip()


# (C6) ce qui est relu ce jour et ce qui est repris, demande par demande.
INTRODUCTIONS = {
    "1": ("Faits seulement ; aucune recommandation. La plupart sont relus ce jour sur les pièces d'origine, aux pages "
          "dites. Cinq sont repris de lectures antérieures du programme, sans relecture ce jour : ce qui est dit de "
          "Gasteiger et al., de Gan et al., de Boxo et al., de Soopal et al., et le tableau 4 de Taufeeque et al. "
          "Le budget n'est connu que par l'ordre de grandeur du point A.2. « Le papier du programme » désigne le "
          "premier article que le programme prépare, sur la détection dans le temps chez un agent seul."),
    "2": ("Faits seulement ; aucune recommandation. Les chiffres de résultat sont relus ce jour sur le verdict "
          "d'origine ; les repères publiés sont relus sur les pièces d'origine, sauf celui qui est marqué « repris »."),
}

reformulations = open(f"{S}/demandes-reformulees-quatre-points-v1.md", encoding="utf-8").read()
dossier = open(f"{S}/dossier-faits-demande-{N}-v1.md", encoding="utf-8").read()
invite = (bloc_demande(reformulations, N) + "\n\n---\n\n# Dossier de faits\n\n" + INTRODUCTIONS[N] + "\n\n"
          + corps_dossier(dossier, N) + "\n")
chemin_invite = f"{S}/invite-carbon-demande-{N}-v2.md"
if os.path.exists(chemin_invite):
    if open(chemin_invite, encoding="utf-8").read() != invite:
        refuser(10, "REFUS : l'invite sur disque diffère de l'invite reconstruite")
else:
    open(chemin_invite, "w", encoding="utf-8").write(invite)
q = open(chemin_invite, encoding="utf-8").read()
empreinte = hashlib.sha256(q.encode("utf-8")).hexdigest()
trouves = motifs_de(q)
if trouves:
    refuser(4, f"REFUS AVANT ENVOI (motifs) {trouves}")
corps = {"contents": [{"role": "user", "parts": [{"text": q}]}],
         "generationConfig": {"maxOutputTokens": PLAFOND,
                              "thinkingConfig": {"thinkingLevel": "high", "includeThoughts": True}}}
prob = verifier_reglages_google("carbon", corps, provision=PROVISION, mots=MOTS, mode="flux")
if prob:
    refuser(2, f"REFUS AVANT ENVOI {prob}")
if f"{MOTS:,}".replace(",", " ") + " mots" not in q.replace(" ", " ").replace(" ", " "):
    refuser(10, "REFUS : la limite de mots écrite dans l'invite n'est pas celle passée à la garde")
pire = PLAFOND * PRIX_SORTIE + (len(q) / 2) * PRIX_ENTREE
print(VERSION_GARDE, f"demande {N} : invite {len(q)} caractères, empreinte {empreinte} ; réglages conformes ; pire cas USD", round(pire, 3))
if not pire < PLAFOND_USD:
    refuser(10, f"REFUS : pire cas {pire:.3f} au-delà du plafond de {PLAFOND_USD} USD")
if len(sys.argv) < 4:
    refuser(0, "RIEN N'EST PARTI : option --envoyer GO-… EMPREINTE absente")
if len(sys.argv) != 6 or sys.argv[3] != "--envoyer":
    refuser(5, "REFUS : pour envoyer, exactement --envoyer GO-AAAA-MM-JJ-NN EMPREINTE")
ACCORD = sys.argv[4]
if not re.fullmatch(r"GO-\d{4}-\d{2}-\d{2}-\d{1,3}", ACCORD):
    refuser(6, "REFUS : identifiant d'accord mal formé")
if sys.argv[5] != empreinte:
    refuser(5, "REFUS : l'empreinte donnée n'est pas celle de l'invite sur disque")
# (C4, D1) l'accord figure-t-il au registre des accords de la branche principale distante, sur une ligne unique qui
# nomme Carbon et le protocole X ?
commit_registre = subprocess.run(["git", "-C", RACINE, "rev-parse", "origin/main"], capture_output=True, text=True).stdout.strip()
registre = subprocess.run(["git", "-C", RACINE, "show", "origin/main:registres/go.md"], capture_output=True, text=True)
if registre.returncode != 0:
    refuser(6, "REFUS : registre des accords illisible sur la branche principale distante")
lignes_accord = [l for l in registre.stdout.splitlines()
                 if re.match(rf"\s*(?:\|\s*|-\s*\*\*)?{re.escape(ACCORD)}\b", l)]
if len(lignes_accord) != 1 or "Carbon" not in lignes_accord[0] or "protocole X" not in lignes_accord[0]:
    refuser(6, f"REFUS : l'accord {ACCORD} ne figure pas, sur une ligne unique nommant Carbon et le protocole X, au "
               f"registre des accords (commit {commit_registre[:12]})")
print(f"accord {ACCORD} lu au registre de la branche principale distante, commit {commit_registre[:12]}")
brute, sortie, journal, verrou = (f"{S}/reponse-carbon-demande-{N}-v1-brute.jsonl", f"{S}/reponse-carbon-demande-{N}-v1.md",
                                  f"{S}/journal-appel-carbon-demande-{N}-v1.txt", f"{S}/tentative-carbon-demande-{N}-v1.verrou")
if os.path.exists(brute) or os.path.exists(sortie):
    refuser(3, "REFUS : une réponse existe déjà ; aucune relance après dépense sans décision nommée")


def noter(ligne):
    with open(journal, "a", encoding="utf-8") as j:
        j.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} {ligne}\n")


# (C2) verrou en création exclusive : un seul processus passe ; un verrou resté en place refuse toute relance.
if os.path.exists(verrou):
    refuser(3, "REFUS : un verrou de tentative existe (envoi en cours, ou issue incertaine d'un envoi passé) ; "
               "aucune relance sans décision nommée")
if os.path.realpath(S) != os.path.realpath(ICI):  # (D2) aucun envoi d'une copie du dossier
    refuser(11, "REFUS : DOSSIER n'est pas le dossier de ce script ; aucun envoi ne part d'une copie")
try:
    descripteur = os.open(verrou, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
except FileExistsError:
    refuser(3, "REFUS : un verrou de tentative existe (envoi en cours, ou issue incertaine d'un envoi passé) ; "
               "aucune relance sans décision nommée")
os.write(descripteur, f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} {ACCORD} {empreinte}\n".encode())
os.close(descripteur)
cle = os.environ.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY_2")
if not cle:
    os.remove(verrou)
    refuser(5, "REFUS : aucune des deux clés permises n'est présente ; rien n'est parti")
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-carbon:streamGenerateContent?alt=sse"
req = urllib.request.Request(url, data=json.dumps(corps).encode(),
                             headers={"Content-Type": "application/json", "x-goog-api-key": cle})
noter(f"tentative, accord {ACCORD} (registre au commit {commit_registre[:12]}), invite {empreinte}, garde {VERSION_GARDE}")
t0, texte, fin, usage, blocage, modele = time.time(), [], None, {}, None, None
# Un refus HTTP avant tout traitement (429, 500, 502, 503, 504 : rien n'est facturé, rien n'est rendu) est journalisé
# avec son corps et réessayé au plus quatre fois (attentes 20, 60, 120, 240 s) ; un autre refus HTTP arrête, verrou
# retiré. Toute autre erreur (adresse, délai, coupure) est d'issue incertaine : verrou gardé, code 7.
r = None
for n, attente in enumerate((20, 60, 120, 240, None), 1):
    try:
        r = urllib.request.urlopen(req, timeout=1800)
        break
    except urllib.error.HTTPError as e:
        try:  # (D4)
            corps_erreur = e.read()[:800].decode("utf-8", "replace")
        except Exception:
            corps_erreur = "(corps du refus illisible)"
        noter(f"essai {n} HTTP {e.code} {corps_erreur!r}")
        print("essai", n, "HTTP", e.code, corps_erreur[:300], flush=True)
        if e.code not in (429, 500, 502, 503, 504) or attente is None:
            os.remove(verrou)
            noter("arrêt : refus HTTP avant tout traitement ; verrou retiré ; une relance est permise sur le même accord")
            refuser(8, "ARRÊT : panne technique avant tout traitement, rien n'est parti en réponse")
        time.sleep(attente)
    except Exception as e:  # erreur d'adresse, délai, coupure avant les en-têtes : issue incertaine
        noter(f"essai {n} DÉFAUT issue incertaine avant les en-têtes : {type(e).__name__} ; verrou gardé")
        refuser(7, f"ARRÊT : issue incertaine ({type(e).__name__}) ; verrou gardé, aucune relance sans décision nommée")
noter("envoi accepté (en-têtes reçus)")
coupure = None
with open(brute, "w", encoding="utf-8") as brut:
    try:
        with r:
            for ligne in r:
                ligne = ligne.decode("utf-8").strip()
                if not ligne.startswith("data:"):
                    continue
                brut.write(ligne[5:].strip() + "\n")
                m = json.loads(ligne[5:])
                usage = m.get("usageMetadata", usage)
                modele = m.get("modelVersion", modele)
                blocage = m.get("promptFeedback", {}).get("blockReason", blocage)
                for c in m.get("candidates", []):
                    fin = c.get("finishReason", fin)
                    texte += [p.get("text", "") for p in c.get("content", {}).get("parts", []) if not p.get("thought")]
    except Exception as e:  # coupure en cours de flux, ligne illisible : défaut, brut partiel gardé
        coupure = type(e).__name__
texte = "".join(texte)
d = f"COUPURE_{coupure}" if coupure else defaut_reponse_google(fin, texte, usage.get("thoughtsTokenCount"), blocage)
cout = (usage.get("promptTokenCount", 0) * PRIX_ENTREE
        + (usage.get("candidatesTokenCount", 0) + usage.get("thoughtsTokenCount", 0)) * PRIX_SORTIE)
bilan = (f"accord {ACCORD} défaut {d} fin {fin} modèle servi {modele} usage {json.dumps(usage, ensure_ascii=False)} "
         f"coût USD (tarif haut) {cout:.4f} durée s {round(time.time() - t0)}")
noter(bilan)
print(bilan)
if d is None:
    open(sortie, "w", encoding="utf-8").write(texte)
else:  # un défaut n'est jamais une réponse : le texte éventuel est gardé à part, sous un nom qui le dit ; verrou gardé
    open(f"{S}/defaut-carbon-demande-{N}-v1-{d}.md", "w", encoding="utf-8").write(texte)
    sys.exit(7 if coupure else 9)
