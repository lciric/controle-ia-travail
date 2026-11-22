"""Recueil d'une session fille de l'abonnement (v2).

v2 (mot de la mère, 14:54Z, GO-2026-11-22-73) : (i) option --lecture-permise NOM : la session peut lire le texte servi
dans le dépôt (branche à part qui ne porte que ce fichier) ; seuls des appels Read dont file_path finit par /NOM (ou vaut
NOM) sont admis, aucun autre outil, au moins une lecture ; (ii) --consigne-systeme TEXTE : la consigne ajoutée à
l'invite système de la session est déclarée ; (iii) une déclaration de voie est versée à côté de la réponse
(reponses/CID.voie.json, scellée) : session, tours, lectures, consigne, coût théorique, pensées. Le reste est la v1.
--refusee-avec-outils : verse la réponse à part (abonnement/hors-dossier/CID-SESSION-avec-outils.md, scellée) sans la
verser au dossier.

En-tête de la v1 :
Recueil d'une session fille de l'abonnement (v1) : lit la page d'événements enregistrée (list_events, sortes
assistant et result), extrait la réponse finale, la raison d'arrêt et le modèle servi, contrôle que la session n'a
joué qu'un tour sans outil, puis verse par « recueillir » de la voie abonnement v5.
Usage : python recueil_session_v2.py EVENEMENTS.txt DOSSIER CELLULE SESSION [--lecture-permise NOM] [--consigne-systeme T]"""
import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ICI = Path(__file__).resolve().parent
FINS = {"end_turn": "end_turn", "max_tokens": "max_tokens", "refusal": "refusal"}


def couverture(lectures, lignes):
    """Lignes 1..lignes couvertes par les lectures (offset 1-indexé par défaut, limit 2000 par défaut)."""
    vues = set()
    for b in lectures:
        i = b.get("input") or {}
        debut = int(i.get("offset") or 1)
        debut = max(debut, 1)
        n = int(i.get("limit") or 2000)
        vues.update(range(debut, debut + n))
    return [k for k in range(1, lignes + 1) if k not in vues]


def lire(chemin, lecture_permise=None, lignes=None):
    raw = Path(chemin).read_text(encoding="utf-8")
    d = json.loads(raw[raw.find("{"):raw.rfind("}") + 1])
    evs = d["ccr"]["data"]
    res = [e["result"]["internal_anthropic_catchall"] for e in evs if "result" in e]
    if len(res) != 1:
        raise SystemExit(f"ARRÊT : {len(res)} résultats dans la page (un seul attendu)")
    r = res[0]
    outils = [b for e in evs if "assistant" in e
              for b in e["assistant"]["internal_anthropic_catchall"]["message"]["content"] if b.get("type") == "tool_use"]
    lectures = [b for b in outils if lecture_permise and b.get("name") == "Read"
                and isinstance((b.get("input") or {}).get("file_path"), str)
                and (b["input"]["file_path"] == lecture_permise or b["input"]["file_path"].endswith("/" + lecture_permise))]
    autres = [b for b in outils if b not in lectures]
    modeles = sorted((r.get("modelUsage") or {}).keys())
    ecarts = []
    if r.get("is_error") or r.get("subtype") != "success":
        ecarts.append(f"résultat en erreur ({r.get('subtype')})")
    if lecture_permise is None and (r.get("num_turns") != 1 or outils):
        ecarts.append(f"{r.get('num_turns')} tours, {len(outils)} appels d'outil (un tour sans outil attendu)")
    if lecture_permise is not None:
        if autres:
            ecarts.append(f"{len(autres)} appels d'outil autres que la lecture permise : "
                          f"{sorted({b.get('name') for b in autres})}")
        if not lectures:
            ecarts.append("aucune lecture du texte servi")
        if lignes is not None and lectures:
            manque = couverture(lectures, lignes)
            if manque:
                ecarts.append(f"{len(manque)} lignes du texte servi jamais lues (première : {manque[0]})")
        if r.get("num_turns") != len(lectures) + 1:
            ecarts.append(f"{r.get('num_turns')} tours pour {len(lectures)} lectures (lectures + 1 attendu)")
    if len(modeles) != 1:
        ecarts.append(f"modèles servis {modeles} (un seul attendu)")
    u = r.get("usage") or {}
    if (u.get("server_tool_use") or {}).get("web_search_requests") or (u.get("server_tool_use") or {}).get("web_fetch_requests"):
        ecarts.append("recherche ou lecture web dans la session")
    fin = FINS.get(r.get("stop_reason"))
    if fin is None:
        ecarts.append(f"raison d'arrêt {r.get('stop_reason')!r} hors de {sorted(FINS)}")
    r["_lectures"] = len(lectures)
    r["_outils"] = len(outils)
    return r.get("result") or "", fin, (modeles or [None])[0], ecarts, r


def ecrire_scelle(chemin, texte):
    chemin = Path(chemin)
    chemin.parent.mkdir(parents=True, exist_ok=True)
    with open(chemin, "x", encoding="utf-8", newline="\n") as f:
        f.write(texte)
    h = hashlib.sha256(texte.encode("utf-8")).hexdigest()
    with open(str(chemin) + ".sha256", "x", encoding="utf-8", newline="\n") as f:
        f.write(f"{h}  {chemin.name}\n")
    return h


def principal(argv):
    p = argparse.ArgumentParser()
    p.add_argument("evenements")
    p.add_argument("dossier")
    p.add_argument("cellule")
    p.add_argument("session")
    p.add_argument("--lecture-permise", default=None)
    p.add_argument("--consigne-systeme", default=None)
    p.add_argument("--lignes", type=int, default=None, help="nombre de lignes du texte servi (couverture exigée)")
    p.add_argument("--refusee-avec-outils", action="store_true")
    a = p.parse_args(argv)
    evenements, dossier, cellule, session = a.evenements, a.dossier, a.cellule, a.session
    if a.lecture_permise and a.lignes is None:
        raise SystemExit("ARRÊT : --lecture-permise exige --lignes (couverture du texte servi)")
    texte, fin, modele, ecarts, r = lire(evenements, a.lecture_permise, a.lignes)
    if a.refusee_avec_outils:  # versée à part, jamais au dossier
        h = ecrire_scelle(Path(dossier) / "abonnement" / "hors-dossier" / f"{cellule}-{session}-avec-outils.md", texte)
        ecrire_scelle(Path(dossier) / "abonnement" / "hors-dossier" / f"{cellule}-{session}-avec-outils.json",
                      json.dumps({"cellule": cellule, "session": session, "statut": "avec outils, hors dossier",
                                  "ecarts": ecarts, "outils": r["_outils"], "tours": r.get("num_turns"),
                                  "modeles": sorted((r.get("modelUsage") or {}).keys()), "sha256": h},
                                 ensure_ascii=False, indent=1) + "\n")
        print(f"{cellule} : versée hors dossier ({len(texte)} caractères, {r['_outils']} appels d'outil)")
        return 0
    if ecarts:
        raise SystemExit("ARRÊT : " + " ; ".join(ecarts) + " ; rien n'est versé")
    with tempfile.TemporaryDirectory() as t:
        f = Path(t) / "reponse.md"
        f.write_text(texte, encoding="utf-8")
        code = subprocess.run([sys.executable, "-B", str(ICI / "voie_abonnement_v5.py"), "recueillir", dossier, cellule,
                               "--texte", str(f), "--session", session, "--modele-servi", modele, "--fin", fin]).returncode
    if code == 0:
        ecrire_scelle(Path(dossier) / "abonnement" / "reponses" / f"{cellule}.voie.json",
                      json.dumps({"cellule": cellule, "session": session, "tours": r.get("num_turns"),
                                  "lectures_du_texte_servi": r["_lectures"], "lecture_permise": a.lecture_permise,
                                  "consigne_systeme_ajoutee": a.consigne_systeme,
                                  "cout_theorique_usd": r.get("total_cost_usd"),
                                  "pensees": (r.get("usage") or {}).get("output_tokens_details", {}).get("thinking_tokens"),
                                  "programme": "recueil-session-v2"}, ensure_ascii=False, indent=1) + "\n")
    print(f"{cellule} : {len(texte)} caractères, fin {fin}, modèle {modele}, coût théorique "
          f"{r.get('total_cost_usd')} USD (abonnement, non facturé), pensées "
          f"{(r.get('usage') or {}).get('output_tokens_details', {}).get('thinking_tokens')}")
    return code


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
