#!/usr/bin/env python3
"""Une espèce seule (Argon : C, ou Kimi : D) — v2 : = v1 (`espece_seule_v1.py`, gardée, R12) + un mode « tel quel » : le fichier
servi est envoyé **seul, sans préambule ni faits**, comme unique message utilisateur (demande du n° 322 de conv-audit : relecture de
la candidature de Lazar). Usage du mode : espece_seule_v2.py LETTRE --tel-quel FICHIER SORTIE PLAFOND_USD

En-tête de la v1 :
Une espèce seule (Argon : C, ou Kimi : D) sur une question servie avec ses faits — v1 (généralise argon_seul_convergence_v1.py).

session-depot (instance 3, seconde session), 1er novembre 2026. Règle de Lazar du 1er novembre (n° 314 de conv-audit, R-959) : toute
question reformulée va aussi à Kimi seul, en plus d'Argon seul et du collisionneur. Réutilise les fonctions du collisionneur v7 (même
dossier, empreinte vérifiée par le lanceur) : appels Gemini et Kimi (relais local, KIMI_RELAIS_URL), lecture, statut, coût, pire cas.
Un seul appel ; garde de pire cas avant envoi contre le plafond donné ; aucune clé en argument ni en fichier ; sorties dans un dossier
neuf ; rien n'est tranché par cet avis.
Usage : espece_seule_v1.py LETTRE(C|D) QUESTION FAITS SORTIE PLAFOND_USD
"""
import hashlib, json, os, sys, time
from pathlib import Path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # mode -I : le dossier du script n'est pas sur sys.path
import collisionneur_v7 as c

NOMS = {"C": "Argon", "D": "Kimi K3.1 Pro"}

def h(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def principal(lettre, question, faits, sortie, plafond):
    assert lettre in NOMS, "lettre C (Argon) ou D (Kimi)"
    plafond = float(plafond); m = c.MODELES[lettre]; max_tokens = m["max"]
    sortie = Path(sortie); sortie.mkdir(parents=True, exist_ok=False)
    tel_quel = question == "--tel-quel"
    if tel_quel:
        question = faits
        q = Path(question).read_text(encoding="utf-8"); f = ""
        prompt = q
    else:
      q = Path(question).read_text(encoding="utf-8"); f = Path(faits).read_text(encoding="utf-8")
      prompt = (f"Tu es {NOMS[lettre]} ({m['id']}), consulté seul. Réponds en français, au niveau méthode seulement (aucune recette "
              "d'attaque, aucun cas concret), par mécanisme, avec conditions de validité, ce qui réfuterait, et sources (qui "
              "seront vérifiées sur PDF : donne titre, auteurs, année, identifiant). Ne recommande rien au directeur : expose. "
              "Appuie chaque chiffre sur les pièces servies ci-dessous, par renvoi (pièce, section).\n\n"
              "=== QUESTION ===\n" + q + "\n\n=== PIÈCES SERVIES ===\n" + f)
    pire = c.cout_pire_cas(m["prix"], len(prompt), max_tokens)
    (sortie / "prompt.txt").write_text(prompt, encoding="utf-8")
    manifeste = {"espece": lettre, "modele": m["id"], "question": question, "question_sha256": h(question), "faits": None if tel_quel else faits,
                 "faits_sha256": None if tel_quel else h(faits), "tel_quel": tel_quel, "collisionneur_v7_sha256": h(os.path.join(os.path.dirname(os.path.abspath(__file__)), "collisionneur_v7.py")),
                 "caracteres_prompt": len(prompt), "max_tokens": max_tokens, "prix": m["prix"], "pire_cas_usd": round(pire, 4),
                 "plafond_usd": plafond, "debut": c.maintenant()}
    if pire > plafond:
        manifeste["arret"] = "pire cas au-delà du plafond"
        (sortie / "manifeste.json").write_text(json.dumps(manifeste, indent=1, ensure_ascii=False), encoding="utf-8")
        print(f"ARRÊT : pire cas {pire:.2f} > plafond {plafond}"); return 4
    print(f"pire cas {pire:.2f} USD ≤ plafond {plafond} ; appel {m['id']}…", flush=True)
    t0 = time.time(); rep = c.APPELANTS[m["fournisseur"]](m["id"], prompt, max_tokens); duree = time.time() - t0
    statut = "ECHEC" if rep.echec else c.statut_reponse(m["fournisseur"], rep)
    cout = c.cout(m["prix"], rep.usage) if rep.usage else 0.0
    (sortie / "reponse.md").write_text(rep.texte or "", encoding="utf-8")
    manifeste.update({"fin": c.maintenant(), "duree_s": round(duree, 1), "statut": statut, "fin_reponse": rep.fin, "echec": rep.echec,
                      "modele_servi": rep.modele_servi, "identifiant": rep.identifiant, "usage": rep.usage, "cout_usd": round(cout, 4),
                      "reponse_sha256": hashlib.sha256((rep.texte or "").encode()).hexdigest()})
    (sortie / "manifeste.json").write_text(json.dumps(manifeste, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"statut {statut}, fin {rep.fin}, usage {rep.usage}, coût {cout:.4f} USD, {duree:.0f} s ; sorties dans {sortie}")
    return 0 if statut == "OK" else 3

if __name__ == "__main__":
    sys.exit(principal(*sys.argv[1:6]))  # mode tel quel : LETTRE --tel-quel FICHIER SORTIE PLAFOND
