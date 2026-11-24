"""Appel unique à Carbon (gemini-4-carbon) pour une demande reformulée du protocole X « entraîner plutôt que détecter ;
juges de la base boîte noire ». Pièce d'instrument (classe B).

Copie de docs/notes/lecteur-synthese-verdicts-pour-lazar-01qi7-v1/appel_carbon_v2.py (branche du lecteur des verdicts,
employé sous GO-2026-11-24-10), avec ces changements, et seulement ceux-là :
  (1) l'invite est construite par ce script à partir de deux fichiers scellés (la demande reformulée et son dossier de
      faits), écrite sur disque telle qu'elle partira, puis relue : c'est ce fichier qui part, à l'octet ;
  (2) garde de motifs avant tout envoi (nom de personne, identifiant de session, d'accord ou de registre, chemin interne,
      adresse de courriel) : refus nommé, rien n'est retiré en silence ;
  (3) limite de mots 3 500 (au lieu de 1 200) et plafond de dépense 3 USD par demande (au lieu de 5) ;
  (4) l'empreinte de l'invite est exigée en argument de l'envoi : une invite changée après la contre-lecture ne part pas.
Sans l'option --envoyer, rien ne part : seules la construction de l'invite, les gardes et l'estimation du pire cas sont
jouées. Clé lue par son nom (GEMINI_API_KEY, sinon GEMINI_API_KEY_2 ; jamais _3).

Usage : python appel_carbon_protocole_x_v1.py DOSSIER N [--envoyer GO-AAAA-MM-JJ-NN EMPREINTE_DE_L_INVITE]
        N = 1 ou 2 (numéro de la demande)."""
import hashlib, json, os, re, sys, time, urllib.error, urllib.request

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "src"))
from controle_ia.garde_google_v3 import verifier_reglages_google, defaut_reponse_google, VERSION_GARDE

S, N = sys.argv[1], sys.argv[2]
assert N in ("1", "2"), "N = 1 ou 2"
PROVISION, PLAFOND, MOTS, PLAFOND_USD = 49152, 65536, 3500, 3.0
PRIX_ENTREE, PRIX_SORTIE = 8.3e-6, 41.5e-6  # le plus haut des deux tarifs trouvés au dépôt (8,3 / 41,5 USD par million)

MOTIFS = {
    "nom de personne": re.compile(r"\bLazar\b|\bCiric\b|\bLuc\b|\bRigaud\b", re.I),
    "identifiant de session": re.compile(r"session_[0-9A-Za-z]{8,}"),
    "identifiant d'accord": re.compile(r"\bGO-\d{4}-\d{2}-\d{2}-\d+"),
    "identifiant de registre ou de décision": re.compile(r"\bR-\d{3,}\b|\bN-0\d{2}\b|\bP-0\d{2}\b|\bT0\.\d\b"),
    "chemin interne": re.compile(r"\b(?:docs|registres|prereg|src|runs|diag|coffre|brouillons)/"),
    "adresse de courriel": re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+"),
    "nom du dépôt": re.compile(r"controle-ia", re.I),
}


def bloc_demande(texte, n):
    """Le bloc « Demande reformulée (à servir telle quelle…) » de la demande n, sans son titre."""
    titre = f"### Demande reformulée (à servir telle quelle, avec le dossier de faits de la demande {n})"
    assert texte.count(titre) == 1, f"titre du bloc de la demande {n} absent ou répété"
    suite = texte.split(titre, 1)[1]
    fin = suite.find("\n---\n")
    return (suite if fin < 0 else suite[:fin]).strip()


def corps_dossier(texte, n):
    """Le dossier de faits depuis sa section A ; pour la demande 1, sans la table des sources (chemins internes)."""
    debut = texte.find("\n## A. ")
    assert debut > 0, "section A du dossier absente"
    corps = texte[debut:]
    if n == "1":
        fin = corps.find("\n## F. Sources et empreintes")
        assert fin > 0, "section F du dossier 1 absente"
        corps = corps[:fin]
    return corps.strip()


reformulations = open(f"{S}/demandes-reformulees-quatre-points-v1.md", encoding="utf-8").read()
dossier = open(f"{S}/dossier-faits-demande-{N}-v1.md", encoding="utf-8").read()
invite = (bloc_demande(reformulations, N) + "\n\n---\n\n# Dossier de faits\n\n"
          "Faits seulement, relus sur les fichiers d'origine aux pages dites ; aucune recommandation.\n\n"
          + corps_dossier(dossier, N) + "\n")
chemin_invite = f"{S}/invite-carbon-demande-{N}-v1.md"
if os.path.exists(chemin_invite):
    assert open(chemin_invite, encoding="utf-8").read() == invite, "l'invite sur disque diffère de l'invite reconstruite"
else:
    open(chemin_invite, "w", encoding="utf-8").write(invite)
q = open(chemin_invite, encoding="utf-8").read()
empreinte = hashlib.sha256(q.encode("utf-8")).hexdigest()
trouves = {nom: sorted(set(m.findall(q)))[:5] for nom, m in MOTIFS.items() if m.search(q)}
if trouves:
    print("REFUS AVANT ENVOI (motifs)", trouves); sys.exit(4)
corps = {"contents": [{"role": "user", "parts": [{"text": q}]}],
         "generationConfig": {"maxOutputTokens": PLAFOND,
                              "thinkingConfig": {"thinkingLevel": "high", "includeThoughts": True}}}
prob = verifier_reglages_google("carbon", corps, provision=PROVISION, mots=MOTS, mode="flux")
if prob:
    print("REFUS AVANT ENVOI", prob); sys.exit(2)
assert f"{MOTS:,}".replace(",", " ") in q.replace(" ", " ").replace(" ", " "), "la limite de mots de l'invite n'est pas celle de la garde"
pire = PLAFOND * PRIX_SORTIE + (len(q) / 2) * PRIX_ENTREE
print(VERSION_GARDE, f"demande {N} : invite {len(q)} caractères, empreinte {empreinte} ; réglages conformes ; pire cas USD", round(pire, 3))
assert pire < PLAFOND_USD, f"pire cas au-delà du plafond de {PLAFOND_USD} USD"
if len(sys.argv) < 6 or sys.argv[3] != "--envoyer" or not sys.argv[4].startswith("GO-"):
    print("RIEN N'EST PARTI : option --envoyer GO-… EMPREINTE absente"); sys.exit(0)
if sys.argv[5] != empreinte:
    print("REFUS : l'empreinte donnée n'est pas celle de l'invite sur disque"); sys.exit(5)
brute, sortie, journal = (f"{S}/reponse-carbon-demande-{N}-v1-brute.jsonl", f"{S}/reponse-carbon-demande-{N}-v1.md",
                          f"{S}/journal-appel-carbon-demande-{N}-v1.txt")
if os.path.exists(brute):
    print("REFUS : une réponse existe déjà ; aucune relance après dépense sans décision nommée"); sys.exit(3)
cle = os.environ.get("GEMINI_API_KEY") or os.environ["GEMINI_API_KEY_2"]
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-carbon:streamGenerateContent?alt=sse"
req = urllib.request.Request(url, data=json.dumps(corps).encode(),
                             headers={"Content-Type": "application/json", "x-goog-api-key": cle})


def noter(ligne):
    with open(journal, "a", encoding="utf-8") as j:
        j.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} {ligne}\n")


t0, texte, fin, usage, blocage, modele = time.time(), [], None, {}, None, None
# Une panne avant tout traitement (HTTP 429, 500, 502, 503, 504 : rien n'est facturé, rien n'est rendu) est journalisée
# avec son corps et réessayée au plus quatre fois (attentes 20, 60, 120, 240 s) ; tout autre échec arrête. Dès qu'une
# réponse commence, plus aucun réessai.
r = None
for n, attente in enumerate((20, 60, 120, 240, None), 1):
    try:
        r = urllib.request.urlopen(req, timeout=1800); break
    except urllib.error.HTTPError as e:
        corps_erreur = e.read()[:800].decode("utf-8", "replace")
        noter(f"essai {n} HTTP {e.code} {corps_erreur!r}")
        print("essai", n, "HTTP", e.code, corps_erreur[:300], flush=True)
        if e.code not in (429, 500, 502, 503, 504) or attente is None:
            print("ARRÊT : panne technique avant tout traitement, rien n'est parti en réponse"); sys.exit(8)
        time.sleep(attente)
noter(f"envoi accepté, accord {sys.argv[4]}, invite {empreinte}, garde {VERSION_GARDE}")
with r, open(brute, "w", encoding="utf-8") as brut:
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
texte = "".join(texte)
d = defaut_reponse_google(fin, texte, usage.get("thoughtsTokenCount"), blocage)
cout = (usage.get("promptTokenCount", 0) * PRIX_ENTREE
        + (usage.get("candidatesTokenCount", 0) + usage.get("thoughtsTokenCount", 0)) * PRIX_SORTIE)
bilan = (f"accord {sys.argv[4]} défaut {d} fin {fin} modèle servi {modele} usage {json.dumps(usage, ensure_ascii=False)} "
         f"coût USD (tarif haut) {cout:.4f} durée s {round(time.time() - t0)}")
noter(bilan); print(bilan)
if d is None:
    open(sortie, "w", encoding="utf-8").write(texte)
else:  # un défaut n'est jamais une réponse : le texte éventuel est gardé à part, sous un nom qui le dit
    open(f"{S}/defaut-carbon-demande-{N}-v1-{d}.md", "w", encoding="utf-8").write(texte)
    sys.exit(9)
