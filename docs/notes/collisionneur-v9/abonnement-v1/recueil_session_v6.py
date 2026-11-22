"""Recueil d'une session fille de l'abonnement (v6).

v6 : en voie fichier, le premier message « user » avant le premier résultat doit être exactement INVITE_FICHIER (invite
courte fixée d'avance) ; sinon refus. Les branches de kits sont autorisées par Lazar (« je t'autorise à pousser des
branches kits-abonnement/* », session des collisionneurs, 22 novembre).

En-tête de la v5 :
Recueil d'une session fille de l'abonnement (v5).

v5 (contre-lecture de la v4) : hors voie fichier, le premier message « user » de la page, avant le premier résultat, doit
porter exactement le texte servi du kit (empreinte égale) ; sinon refus. Ainsi le résultat lu répond bien au texte servi,
même si la page commence plus tard (pagination) ou si un tour humain suit avec le même modèle. La page doit donc être
prise sans filtre de sortes (événements « user » compris).

En-tête de la v4 :
Recueil d'une session fille de l'abonnement (v4).

v4 : --premier-tour : seuls les événements jusqu'au PREMIER résultat de la session sont lus (le tour qui répond au texte
servi) ; les tours suivants (message humain arrivé plus tard dans la session, par exemple) sont ignorés, et leur nombre
est déclaré dans la déclaration de voie. Sans l'option, comme la v3 : un seul résultat exigé.

En-tête de la v3 :
Recueil d'une session fille de l'abonnement (v3).

v3, contre-lecture d'Opus de la v2 : (B1) en voie « lecture permise », la page doit porter aussi les événements « user » ;
chaque lecture du texte servi doit avoir un retour sans erreur, et le texte reconstruit à partir des retours (lignes
numérotées) doit être identique, ligne à ligne, au texte servi du kit : une lecture en erreur, tronquée ou d'un autre
fichier ne compte pas ; (B2) l'empreinte du texte servi du kit et le commit de la branche sont déclarés, et le contenu
rendu par les lectures est comparé au kit (B1) ; la déclaration de voie dit que l'invite n'est plus le texte servi
(voie « fichier ») ; non bloquants : la déclaration de voie n'écrase rien et est contrôlée avant le versement,
--refusee-avec-outils exige au moins un écart.

En-tête de la v2 :
Recueil d'une session fille de l'abonnement (v2).

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
import re
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


LIGNE_NUMEROTEE = re.compile(r"^\s*(\d+)[\t\u2192](.*)$")


def texte_de_retour(contenu):
    if isinstance(contenu, str):
        return contenu
    if isinstance(contenu, list):
        return "\n".join(b.get("text", "") for b in contenu if isinstance(b, dict) and b.get("type") == "text")
    return ""


def lignes_rendues(evs, ids):
    """Lignes numérotées rendues par les retours (tool_result) des lectures d'identifiants `ids` ; erreurs comptées."""
    vues, erreurs, trouves = {}, 0, set()
    for e in evs:
        if "user" not in e:
            continue
        msg = (e["user"].get("internal_anthropic_catchall") or {}).get("message") or {}
        contenu = msg.get("content") if isinstance(msg.get("content"), list) else []
        for b in contenu:
            if not isinstance(b, dict) or b.get("type") != "tool_result" or b.get("tool_use_id") not in ids:
                continue
            trouves.add(b["tool_use_id"])
            if b.get("is_error"):
                erreurs += 1
                continue
            for l in texte_de_retour(b.get("content")).split("\n"):
                m = LIGNE_NUMEROTEE.match(l)
                if m:
                    vues[int(m.group(1))] = m.group(2)
    return vues, erreurs, ids - trouves


INVITE_FICHIER = "Lis texte-servi.md en entier, puis réponds à ce qu'il demande."


def premier_message_humain(evs):
    for e in evs:
        if "result" in e:
            return None
        if "user" in e:
            c = ((e["user"].get("internal_anthropic_catchall") or {}).get("message") or {}).get("content")
            if isinstance(c, str):
                return c
            if isinstance(c, list) and not any(isinstance(b, dict) and b.get("type") == "tool_result" for b in c):
                return "".join(b.get("text", "") for b in c if isinstance(b, dict) and b.get("type") == "text")
    return None


def lire(chemin, lecture_permise=None, lignes=None, texte_servi=None, premier_tour=False):
    raw = Path(chemin).read_text(encoding="utf-8")
    d = json.loads(raw[raw.find("{"):raw.rfind("}") + 1])
    evs = d["ccr"]["data"]
    ignores = 0
    if premier_tour:  # v4 : jusqu'au premier résultat inclus
        i = next((k for k, e in enumerate(evs) if "result" in e), None)
        if i is not None:
            ignores = sum(1 for e in evs[i + 1:] if "result" in e)
            evs = evs[:i + 1]
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
        if texte_servi is None:
            ecarts.append("texte servi du kit absent : le contenu lu ne peut pas être comparé")
        elif lectures:  # v3 (B1, B2) : contenu rendu comparé ligne à ligne au kit
            vues, erreurs, sans_retour = lignes_rendues(evs, {b.get("id") for b in lectures})
            attendu = texte_servi.split("\n")
            if attendu and attendu[-1] == "":
                attendu = attendu[:-1]
            if sans_retour:
                ecarts.append(f"{len(sans_retour)} lectures sans retour dans la page (événements « user » manquants ?)")
            differentes = [k for k in range(1, len(attendu) + 1) if vues.get(k) != attendu[k - 1]]
            if differentes:
                ecarts.append(f"{len(differentes)} lignes rendues absentes ou différentes du texte servi (première : "
                              f"{differentes[0]}) ; {erreurs} lectures en erreur")
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
    if lecture_permise is not None:  # v6 : l'invite d'ouverture de la voie fichier
        ouverture = premier_message_humain(evs)
        if ouverture is None:
            ecarts.append("aucun message d'ouverture avant le premier résultat (page incomplète ?)")
        elif ouverture.strip() != INVITE_FICHIER:
            ecarts.append("message d'ouverture différent de l'invite fixée de la voie fichier")
    if lecture_permise is None:  # v5 : le tour lu répond au texte servi
        if texte_servi is None:
            ecarts.append("texte servi du kit absent : le message d'ouverture ne peut pas être comparé")
        else:
            ouverture = premier_message_humain(evs)
            if ouverture is None:
                ecarts.append("aucun message d'ouverture avant le premier résultat (page incomplète ?)")
            elif ouverture.rstrip("\n") != texte_servi.rstrip("\n"):
                ecarts.append("message d'ouverture différent du texte servi du kit")
    r["_lectures"] = len(lectures)
    r["_tours_ignores"] = ignores
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
    p.add_argument("--commit-branche", default=None, help="commit de la branche qui porte le texte servi")
    p.add_argument("--premier-tour", action="store_true", help="ne lire que le premier tour (jusqu'au premier résultat)")
    p.add_argument("--refusee-avec-outils", action="store_true")
    a = p.parse_args(argv)
    evenements, dossier, cellule, session = a.evenements, a.dossier, a.cellule, a.session
    if a.lecture_permise and a.lignes is None:
        raise SystemExit("ARRÊT : --lecture-permise exige --lignes (couverture du texte servi)")
    kit = Path(dossier) / "abonnement" / "kits" / cellule / "texte-servi.md"
    servi = kit.read_text(encoding="utf-8") if kit.exists() else None
    if a.lecture_permise and not a.commit_branche:
        raise SystemExit("ARRÊT : --lecture-permise exige --commit-branche")
    texte, fin, modele, ecarts, r = lire(evenements, a.lecture_permise, a.lignes, servi, a.premier_tour)
    if a.refusee_avec_outils and not ecarts:
        raise SystemExit("ARRÊT : --refusee-avec-outils sans aucun écart : la réponse se verse au dossier")
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
    voie = Path(dossier) / "abonnement" / "reponses" / f"{cellule}.voie.json"
    if voie.exists() or Path(str(voie) + ".sha256").exists():
        raise SystemExit(f"ARRÊT : {voie} existe déjà ; rien n'est versé")
    with tempfile.TemporaryDirectory() as t:
        f = Path(t) / "reponse.md"
        f.write_text(texte, encoding="utf-8")
        code = subprocess.run([sys.executable, "-B", str(ICI / "voie_abonnement_v5.py"), "recueillir", dossier, cellule,
                               "--texte", str(f), "--session", session, "--modele-servi", modele, "--fin", fin]).returncode
    if code == 0:
        ecrire_scelle(voie,
                      json.dumps({"cellule": cellule, "session": session, "tours": r.get("num_turns"),
                                  "lectures_du_texte_servi": r["_lectures"], "lecture_permise": a.lecture_permise,
                                  "invite": ("texte servi lu dans un fichier de la branche, rendu par l'outil de lecture "
                                             "(invite différente du texte servi)") if a.lecture_permise
                                            else "texte servi en invite",
                                  "commit_branche": a.commit_branche,
                                  "premier_tour_seul": a.premier_tour, "tours_suivants_ignores": r["_tours_ignores"],
                                  "sha256_texte_servi_lu": hashlib.sha256(servi.encode("utf-8")).hexdigest()
                                  if servi is not None else None,
                                  "consigne_systeme_ajoutee": a.consigne_systeme,
                                  "cout_theorique_usd": r.get("total_cost_usd"),
                                  "pensees": (r.get("usage") or {}).get("output_tokens_details", {}).get("thinking_tokens"),
                                  "programme": "recueil-session-v6"}, ensure_ascii=False, indent=1) + "\n")
    print(f"{cellule} : {len(texte)} caractères, fin {fin}, modèle {modele}, coût théorique "
          f"{r.get('total_cost_usd')} USD (abonnement, non facturé), pensées "
          f"{(r.get('usage') or {}).get('output_tokens_details', {}).get('thinking_tokens')}")
    return code


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
