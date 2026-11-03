"""Appel seul, un tour, sur la consigne servie de conv-audit (8d6896a1…) — v1, session-depot, 3 novembre 2026.
Usage : python -I -B appel_seul_heimersheim_v1.py COLLISIONNEUR_V9 CONSIGNE LETTRE(C|E) DOSSIER_SORTIE_NEUF
Sert tout ce qui suit la ligne « ===== DÉBUT DU TEXTE SERVI ===== » et le saut de ligne qui la suit, à l'octet.
Écrit la réponse brute et un méta (statut, modèle servi, jetons, coût au barème du collisionneur) ; n'affiche jamais le texte.
Une seule reprise si l'échec est passager (HTTP 429/5xx ou connexion) ; aucune sur un refus. Clé lue par le collisionneur dans
l'environnement (GEMINI_API_KEY ou OPENAI_API_KEY), jamais affichée."""
import datetime, hashlib, importlib.util, json, os, sys
col, consigne, lettre, sortie = sys.argv[1:5]
assert lettre in ("C", "E")
spec = importlib.util.spec_from_file_location("collisionneur_v9", col); cv = importlib.util.module_from_spec(spec); spec.loader.exec_module(cv)
brut = open(consigne, "rb").read()
marq = "===== DÉBUT DU TEXTE SERVI =====\n".encode("utf-8")
assert brut.count(marq) == 1
servi = brut.split(marq, 1)[1].decode("utf-8")
os.makedirs(sortie, exist_ok=False)
m = cv.MODELES[lettre]
appel = {"gemini": cv.appeler_gemini, "openai": cv.appeler_openai}[m["fournisseur"]]
essais = []
for n in (1, 2):
    debut = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    r = appel(m["id"], servi, m["max_relance"], attentes=(0,))
    st = "ECHEC" if r.echec else ("MODELE_DIFFERENT" if not cv.modele_conforme(m["id"], r.modele_servi) else cv.statut_reponse(m["fournisseur"], r))
    e = {"essai": n, "debut_utc": debut, "fin_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
         "statut": st, "modele_demande": m["id"], "modele_servi": r.modele_servi, "fin": r.fin, "echec": (r.echec or "")[:200],
         "usage": r.usage, "cout_usd_bareme": round(cv.cout(m["prix"], r.usage), 4), "max_tokens": m["max_relance"],
         "caracteres_reponse": len(r.texte or "")}
    essais.append(e)
    with open(os.path.join(sortie, f"reponse-essai{n}.md"), "x", encoding="utf-8") as f:
        f.write(r.texte or "")
    passager = st == "ECHEC" and any(c in (r.echec or "") for c in ("429", "500", "502", "503", "504", "URLError", "timed out", "Connection"))
    if not passager:
        break
meta = {"consigne": consigne, "consigne_sha256": hashlib.sha256(brut).hexdigest(),
        "texte_servi_sha256": hashlib.sha256(servi.encode("utf-8")).hexdigest(), "caracteres_servis": len(servi),
        "collisionneur_sha256": hashlib.sha256(open(col, "rb").read()).hexdigest(), "go": os.environ.get("GO_ID"), "essais": essais}
with open(os.path.join(sortie, "meta.json"), "x", encoding="utf-8") as f:
    json.dump(meta, f, ensure_ascii=False, indent=1)
print(json.dumps([{k: e[k] for k in ("essai", "statut", "modele_servi", "fin", "usage", "cout_usd_bareme", "caracteres_reponse")} for e in essais], ensure_ascii=False))
