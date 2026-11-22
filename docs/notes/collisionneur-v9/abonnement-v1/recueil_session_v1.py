"""Recueil d'une session fille de l'abonnement (v1) : lit la page d'événements enregistrée (list_events, sortes
assistant et result), extrait la réponse finale, la raison d'arrêt et le modèle servi, contrôle que la session n'a
joué qu'un tour sans outil, puis verse par « recueillir » de la voie abonnement v5.
Usage : python recueil_session_v1.py EVENEMENTS.txt DOSSIER CELLULE SESSION"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ICI = Path(__file__).resolve().parent
FINS = {"end_turn": "end_turn", "max_tokens": "max_tokens", "refusal": "refusal"}


def lire(chemin):
    raw = Path(chemin).read_text(encoding="utf-8")
    d = json.loads(raw[raw.find("{"):raw.rfind("}") + 1])
    evs = d["ccr"]["data"]
    res = [e["result"]["internal_anthropic_catchall"] for e in evs if "result" in e]
    if len(res) != 1:
        raise SystemExit(f"ARRÊT : {len(res)} résultats dans la page (un seul attendu)")
    r = res[0]
    outils = [b for e in evs if "assistant" in e
              for b in e["assistant"]["internal_anthropic_catchall"]["message"]["content"] if b.get("type") == "tool_use"]
    modeles = sorted((r.get("modelUsage") or {}).keys())
    ecarts = []
    if r.get("is_error") or r.get("subtype") != "success":
        ecarts.append(f"résultat en erreur ({r.get('subtype')})")
    if r.get("num_turns") != 1 or outils:
        ecarts.append(f"{r.get('num_turns')} tours, {len(outils)} appels d'outil (un tour sans outil attendu)")
    if len(modeles) != 1:
        ecarts.append(f"modèles servis {modeles} (un seul attendu)")
    u = r.get("usage") or {}
    if (u.get("server_tool_use") or {}).get("web_search_requests") or (u.get("server_tool_use") or {}).get("web_fetch_requests"):
        ecarts.append("recherche ou lecture web dans la session")
    fin = FINS.get(r.get("stop_reason"))
    if fin is None:
        ecarts.append(f"raison d'arrêt {r.get('stop_reason')!r} hors de {sorted(FINS)}")
    return r.get("result") or "", fin, (modeles or [None])[0], ecarts, r


def principal(argv):
    evenements, dossier, cellule, session = argv
    texte, fin, modele, ecarts, r = lire(evenements)
    if ecarts:
        raise SystemExit("ARRÊT : " + " ; ".join(ecarts) + " ; rien n'est versé")
    with tempfile.TemporaryDirectory() as t:
        f = Path(t) / "reponse.md"
        f.write_text(texte, encoding="utf-8")
        code = subprocess.run([sys.executable, "-B", str(ICI / "voie_abonnement_v5.py"), "recueillir", dossier, cellule,
                               "--texte", str(f), "--session", session, "--modele-servi", modele, "--fin", fin]).returncode
    print(f"{cellule} : {len(texte)} caractères, fin {fin}, modèle {modele}, coût théorique "
          f"{r.get('total_cost_usd')} USD (abonnement, non facturé), pensées "
          f"{(r.get('usage') or {}).get('output_tokens_details', {}).get('thinking_tokens')}")
    return code


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
