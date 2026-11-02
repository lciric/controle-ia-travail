#!/usr/bin/env python3
"""Argon seul (gemini-4-argon) sur la question de convergence v2 (conv-audit, `08f2b017…`) — v1.

session-depot (instance 3, seconde session), 1er novembre 2026. Sous GO-2026-10-31-08 (3 USD par appel) et le mot direct de Lazar
du 1er novembre (« go depenses go TOUTES les depenses », R-949). Réutilise les fonctions du collisionneur v7 (même dossier,
empreinte vérifiée par le script de lancement) : appel Gemini, lecture de la réponse, statut, coût, pire cas. Un seul appel ;
garde de pire cas avant envoi (entrée aux caractères / 3, sortie au maximum) contre le plafond ; aucune clé en argument ni en
fichier (GEMINI_API_KEY lue par le collisionneur dans l'environnement posé par le script sous env -i). Sorties : réponse, usage,
coût, statut, empreintes, dans le dossier de sortie ; rien n'est tranché par cet avis (GO-08).
"""
import hashlib, json, os, sys, time
from pathlib import Path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # mode -I : le dossier du script n'est pas sur sys.path
import collisionneur_v7 as c

PLAFOND_USD = 3.0
MAX_TOKENS = 32000
MODELE = "C"  # gemini-4-argon

def h(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def principal(question, faits, sortie):
    sortie = Path(sortie); sortie.mkdir(parents=True, exist_ok=False)
    q = Path(question).read_text(encoding="utf-8"); f = Path(faits).read_text(encoding="utf-8")
    prompt = ("Tu es Argon (gemini-4-argon), consulté seul. Réponds en français, au niveau méthode seulement (aucune recette "
              "d'attaque, aucun cas concret), par mécanisme, avec conditions de validité, ce qui réfuterait, et sources (qui "
              "seront vérifiées sur PDF : donne titre, auteurs, année, identifiant). Ne recommande rien au directeur : expose. "
              "Appuie chaque chiffre sur les pièces servies ci-dessous, par renvoi (pièce, section).\n\n"
              "=== QUESTION (conv-audit, v2) ===\n" + q + "\n\n=== PIÈCES SERVIES ===\n" + f)
    m = c.MODELES[MODELE]
    pire = c.cout_pire_cas(m["prix"], len(prompt), MAX_TOKENS)
    (sortie / "prompt.txt").write_text(prompt, encoding="utf-8")
    manifeste = {"modele": m["id"], "question": question, "question_sha256": h(question), "faits": faits, "faits_sha256": h(faits),
                 "collisionneur_v7_sha256": h("collisionneur_v7.py"), "caracteres_prompt": len(prompt), "max_tokens": MAX_TOKENS,
                 "prix": m["prix"], "pire_cas_usd": round(pire, 4), "plafond_usd": PLAFOND_USD, "debut": c.maintenant()}
    if pire > PLAFOND_USD:
        manifeste["arret"] = "pire cas au-delà du plafond"; (sortie / "manifeste.json").write_text(json.dumps(manifeste, indent=1, ensure_ascii=False))
        print(f"ARRÊT : pire cas {pire:.2f} > plafond {PLAFOND_USD}"); return 4
    print(f"pire cas {pire:.2f} USD ≤ plafond {PLAFOND_USD} ; appel {m['id']}…", flush=True)
    t0 = time.time(); rep = c.appeler_gemini(m["id"], prompt, MAX_TOKENS); duree = time.time() - t0
    statut = "ECHEC" if rep.echec else c.statut_reponse("gemini", rep)
    cout = c.cout(m["prix"], rep.usage) if rep.usage else 0.0
    (sortie / "reponse-argon.md").write_text(rep.texte or "", encoding="utf-8")
    manifeste.update({"fin": c.maintenant(), "duree_s": round(duree, 1), "statut": statut, "fin_reponse": rep.fin, "echec": rep.echec,
                      "modele_servi": rep.modele_servi, "identifiant": rep.identifiant, "usage": rep.usage, "cout_usd": round(cout, 4),
                      "types_blocs": rep.types_blocs, "reponse_sha256": hashlib.sha256((rep.texte or "").encode()).hexdigest()})
    (sortie / "manifeste.json").write_text(json.dumps(manifeste, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"statut {statut}, fin {rep.fin}, usage {rep.usage}, coût {cout:.4f} USD, {duree:.0f} s ; sorties dans {sortie}")
    return 0 if statut == "OK" else 3

if __name__ == "__main__":
    sys.exit(principal(*sys.argv[1:4]))
