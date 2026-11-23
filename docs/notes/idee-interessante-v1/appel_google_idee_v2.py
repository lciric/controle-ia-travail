"""[v2, 2026-11-23 : question, suffixe et limite de mots paramétrés par DEMANDE_FICHIER, SUFFIXE, MOTS ; GO-2026-11-23-23] Appel seul d'un modèle de Google (Argon, Carbon, Neon) sur la demande reformulée des idées intéressantes, v1.

Pièce d'instrument (classe B), écrite par la mère le 2026-11-23 sur le mot du directeur (GO-2026-11-23-20) ; non
contre-lue avant l'envoi (urgence déclarée, réserve inscrite). Emploie la garde commune src/controle_ia/garde_google_v3.py
avant l'envoi et après la réponse (règle « Appels aux modèles de Google »). Clé lue par son seul nom ; jamais écrite.

  essai  : python appel_google_idee_v1.py essai  ESPECE NOM_DE_CLE
  appel  : python appel_google_idee_v1.py appel  ESPECE NOM_DE_CLE DOSSIER_SORTIE
"""
import hashlib, json, os, sys, time, urllib.request, urllib.error, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "src"))
from controle_ia.garde_google_v3 import verifier_reglages_google, defaut_reponse_google, NIVEAU_MAX_REFLEXION

MODELES = {"argon": "gemini-4-argon", "carbon": "gemini-4-carbon", "neon": "gemini-4-neon"}
ICI = pathlib.Path(__file__).resolve().parent
DEMANDE = ICI / os.environ.get("DEMANDE_FICHIER", "demande-reformulee-modele-idees-interessantes-v1.md")
SUFFIXE = os.environ.get("SUFFIXE", "v1")
BASE = "https://generativelanguage.googleapis.com/v1beta/models/"


def envoyer(url, cle, corps, flux):
    req = urllib.request.Request(url, data=json.dumps(corps).encode(), method="POST",
                                 headers={"Content-Type": "application/json", "x-goog-api-key": cle})
    try:
        rep = urllib.request.urlopen(req, timeout=1800)
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")[:600], None
    if not flux:
        return rep.status, None, [json.loads(rep.read().decode())]
    morceaux = []
    for ligne in rep:
        ligne = ligne.decode("utf-8", "replace").strip()
        if ligne.startswith("data:"):
            morceaux.append(json.loads(ligne[5:].strip()))
    return rep.status, None, morceaux


def lire(morceaux):
    texte, pensees_texte, fin, usage, blocage = [], [], None, {}, None
    for m in morceaux:
        blocage = blocage or (m.get("promptFeedback") or {}).get("blockReason")
        usage = m.get("usageMetadata") or usage
        for c in m.get("candidates") or []:
            fin = c.get("finishReason") or fin
            for p in (c.get("content") or {}).get("parts") or []:
                (pensees_texte if p.get("thought") else texte).append(p.get("text") or "")
    return "".join(texte), "".join(pensees_texte), fin, usage, blocage


def main():
    mode, espece, nom_cle = sys.argv[1], sys.argv[2], sys.argv[3]
    cle = os.environ.get(nom_cle)
    if not cle:
        print(f"{nom_cle} absente de l'environnement ; rien ne part"); return 2
    if mode == "essai":
        corps = {"contents": [{"role": "user", "parts": [{"text": "Réponds seulement : OK."}]}],
                 "generationConfig": {"maxOutputTokens": 20000,
                                      "thinkingConfig": {"thinkingLevel": "low", "includeThoughts": True}}}
        prob = verifier_reglages_google(espece, corps, provision=2000, mots=5, mode="non_diffuse", niveau_attendu="low")
        if prob: print("REFUS DE LA GARDE :", prob); return 3
        code, err, morceaux = envoyer(BASE + MODELES[espece] + ":generateContent", cle, corps, False)
        if err: print(f"{nom_cle} {espece} code {code} : {err}"); return 1
        texte, _, fin, usage, blocage = lire(morceaux)
        print(f"{nom_cle} {espece} code {code} fin {fin} texte {texte.strip()[:20]!r} usage {usage}")
        return 0
    sortie = pathlib.Path(sys.argv[4]); sortie.mkdir(parents=True, exist_ok=True)
    demande = DEMANDE.read_text()
    corps = {"contents": [{"role": "user", "parts": [{"text": demande}]}],
             "generationConfig": {"maxOutputTokens": 65536,
                                  "thinkingConfig": {"thinkingLevel": NIVEAU_MAX_REFLEXION[espece], "includeThoughts": True}}}
    prob = verifier_reglages_google(espece, corps, provision=45000, mots=int(os.environ.get("MOTS", "3500")), mode="flux")
    if prob: print("REFUS DE LA GARDE :", prob); return 3
    t0 = time.time()
    code, err, morceaux = envoyer(BASE + MODELES[espece] + ":streamGenerateContent?alt=sse", cle, corps, True)
    duree = round(time.time() - t0, 1)
    rec = {"espece": espece, "modele_demande": MODELES[espece], "cle_nom": nom_cle, "code": code, "duree_s": duree,
           "demande_sha256": hashlib.sha256(DEMANDE.read_bytes()).hexdigest(), "reglage": corps["generationConfig"],
           "heure_fin": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    if err:
        rec["erreur"] = err
    else:
        texte, pensees, fin, usage, blocage = lire(morceaux)
        defaut = defaut_reponse_google(fin, texte, usage.get("thoughtsTokenCount"), blocage=blocage)
        rec.update({"fin": fin, "usage": usage, "defaut": defaut, "modele_servi": (morceaux[-1] if morceaux else {}).get("modelVersion")})
        (sortie / f"reponse-{espece}-{SUFFIXE}.md").write_text(texte)
        (sortie / f"pensees-{espece}-{SUFFIXE}.md").write_text(pensees)
    (sortie / f"appel-{espece}-{SUFFIXE}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1))
    print(json.dumps({k: rec.get(k) for k in ("espece", "code", "fin", "defaut", "duree_s", "usage", "erreur")}, ensure_ascii=False))
    return 0 if not err and not rec.get("defaut") else 1


if __name__ == "__main__":
    sys.exit(main())
