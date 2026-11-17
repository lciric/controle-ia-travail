"""Essai à blanc complet du crible (iii) — v1 (niveau B des essais) : la chaîne entière, avec relais factices et sans aucun appel réel.

Joué dans un dossier jetable hors de tout dépôt (`--travail`), sur des mondes de développement à graine publique : le lanceur
(`jouer --mode a_blanc`) lance les deux relais factices (le relais du pilote, amont scripté), la commande du pilote sert chaque
appel (sessions neuves, réponses brutes et témoins scellés), le gardien du pilote lit les cartes, cinq files de quatre mondes
courent en parallèle ; puis `mesure_crible_iii_v1.py` (une fois), `lire_crible_iii_v1.py` et `rapatrier`. Suivent les cas
artefacts de la liste d'arrêt qui demandent la chaîne réelle (configuration, relevé de la sonde, ports, mode réel, coût, témoin,
limite de débit, borne par appel, tronquage, passe 1 illisible, carte en trop, seconde mesure, lecture avant scellement).

Les sorties des relais (corps, réponses brutes) restent dans le dossier jetable : elles portent les identifiants servis ; le
compte rendu imprimé n'en porte aucun (comptes, empreintes, verdicts).

Usage : python3 -I -B essai_a_blanc_crible_iii_v1.py --arbre ORCHESTRATEUR --mondes MONDES.json --mondes-sha256 H
        --releve-sonde RELEVE --travail DOSSIER_JETABLE
Code 0 si chaque cas rend l'attendu.
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import json
import os
import shutil
import socket
import subprocess
import sys
import time

ICI = os.path.dirname(os.path.abspath(__file__))
if ICI not in sys.path:
    sys.path.insert(0, ICI)
import crible_iii_v1 as N  # noqa: E402
import lanceur_crible_iii_v1 as LA  # noqa: E402

TEXTE_SHA = "91b4bf30fbf8b83d2c057088d8776be19831b006f1010bcb3c7e2e231d2c7179"   # la pièce qui fera foi (racine des graines à blanc)
PY = sys.executable


def args_jouer(a, sortie, **k):
    ns = argparse.Namespace(commande="jouer", mode="a_blanc", arbre=a.arbre, mondes=a.mondes, mondes_sha256=a.mondes_sha256,
                            texte_sha256=TEXTE_SHA, sortie=sortie, echeance_utc_s=str(int(time.time()) + 17 * 3600),
                            releve_sonde=a.releve_sonde, bornes_a_blanc=None, scenarios_a_blanc=None, texte=None, registre_go=None,
                            go_credits=None, go_hors=None, mondes_shas=None, registre_lancements=None, addendum=None,
                            repetes_permis=True)
    for x, v in k.items():
        setattr(ns, x, v)
    return ns


def jouer(a, nom, scenarios=None, apres_appel=None, **k):
    sortie = os.path.join(a.travail, nom)
    if scenarios is not None:
        f = os.path.join(a.travail, f"scenarios-{nom}.json")
        with open(f, "x", encoding="utf-8") as g:
            json.dump(scenarios, g)
        k["scenarios_a_blanc"] = f
    buf, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(err):
        try:
            code = LA.jouer(args_jouer(a, sortie, **k), apres_appel=apres_appel)
        except N.Refus as e:
            code, msg = 2, str(e)
            return code, sortie, {"refus": msg}
    rel = None
    p = os.path.join(sortie, "releve-crible-iii-v1.json")
    if os.path.isfile(p):
        with open(p, encoding="utf-8") as f:
            rel = json.load(f)
    return code, sortie, rel


def resume(rel):
    if not isinstance(rel, dict) or "appels" not in rel:
        return rel
    c = {e: sum(1 for x in rel["appels"] if x["etat"] == e) for e in ("complet", "tronque", "echec", "non appele")}
    return {"comptes": c, "complets": rel["complets"], "arret": rel["arret"], "depense_usd": rel["depense_usd"],
            "appels_faits": rel["appels_faits"]}


def mesurer(a, sortie):
    r = subprocess.run([PY, "-I", "-B", os.path.join(ICI, "mesure_crible_iii_v1.py"), "mesurer", "--arbre", a.arbre, "--mondes",
                        a.mondes, "--mondes-sha256", a.mondes_sha256, "--sortie", sortie, "--texte-sha256", TEXTE_SHA],
                       capture_output=True, text=True, encoding="utf-8", timeout=7200)
    return r.returncode, (r.stdout + r.stderr).strip().splitlines()[-1:] if (r.stdout + r.stderr).strip() else []


def lire(sortie, ecrire=None):
    cmd = [PY, "-I", "-B", os.path.join(ICI, "lire_crible_iii_v1.py"), "--sortie", sortie] + (["--ecrire", ecrire] if ecrire else [])
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", timeout=600)
    return r.returncode, json.loads(r.stdout) if r.stdout.strip().startswith("{") else r.stdout[-300:]


def consignes_egales_d_b(sortie):
    """Texte servi de B égal à celui de D, monde par monde, relu dans les corps des relais (empreinte de la consigne reçue)."""
    out = {}
    for r in N.MONDES:
        sha = {}
        for b in ("D", "B"):
            p = os.path.join(sortie, f"monde-{r}", b, "corps-relais.json")
            if os.path.isfile(p):
                with open(p, encoding="utf-8") as f:
                    sha[b] = json.load(f).get("consigne_recue_sha256")
        out[r] = len(sha) == 2 and sha["D"] == sha["B"]
    return out


def main(argv):
    p = argparse.ArgumentParser()
    for o in ("--arbre", "--mondes", "--mondes-sha256", "--releve-sonde", "--travail"):
        p.add_argument(o, required=True)
    p.add_argument("--python-reel", help="interpréteur à numpy 2.5.3 (gardes du mode réel, sans appel)")
    a = p.parse_args(argv)
    os.makedirs(a.travail, exist_ok=False)
    R = []

    def cas(nom, ok, detail):
        R.append((nom, bool(ok), detail))
        print(f"CAS {'OK ' if ok else 'ÉCHEC'} | {nom} | {json.dumps(detail, ensure_ascii=False, sort_keys=True, default=str)[:900]}",
              flush=True)

    t0 = time.time()
    # 1. crible complet, bornes gelées, cinq files
    code, s1, rel = jouer(a, "complet")
    egal = consignes_egales_d_b(s1)
    man = json.load(open(os.path.join(s1, "manifeste-crible-iii-v1.json"), encoding="utf-8")) if os.path.isfile(
        os.path.join(s1, "manifeste-crible-iii-v1.json")) else {}
    cas("crible complet à blanc : 100 appels, 20 mondes complets, cinq files, B servi du texte de D",
        code == 0 and rel and resume(rel)["comptes"]["complet"] == 100 and rel["complets"] == 20 and all(egal.values())
        and man.get("files") == {str(k): v for k, v in N.files_des_mondes().items()} and man.get("bornes") == N.BORNES_GELEES,
        {"code": code, "resume": resume(rel), "duree_s": man.get("duree_s"), "d_egal_b": sum(egal.values())})
    cm, lm = mesurer(a, s1)
    cas("mesure, une seule fois, sortie scellée", cm == 0, {"code": cm, "sortie": lm})
    cm2, lm2 = mesurer(a, s1)
    cas("liste d'arrêt : mesure lancée deux fois (refus)", cm2 == 2 and "seconde mesure refusée" in " ".join(lm2), {"code": cm2})
    cl, lec = lire(s1, os.path.join(a.travail, "lecture-complet.json"))
    cas("lecture gelée sur la sortie scellée", cl == 0 and isinstance(lec, dict) and lec.get("etage_arret") in (1, 3, 7),
        {"code": cl, "etage": lec.get("etage_arret") if isinstance(lec, dict) else lec,
         "verdicts": lec.get("verdicts") if isinstance(lec, dict) else None,
         "reserves": lec.get("reserves") if isinstance(lec, dict) else None})
    if cm == 0:
        corps = json.load(open(os.path.join(s1, "mesure-crible-iii-v1.json"), encoding="utf-8"))["corps"]
        cas("mesure : vingt mondes complets, couvertures et dollars par bras rapportés",
            corps["n_complets"] == 20 and corps["appels_faits"] == 100,
            {"n_complets": corps["n_complets"], "sommes": corps["principal"]["sommes"], "execution": corps["execution"],
             "format_tenu": corps["format_tenu_mondes"], "zone_utile": corps["zone_utile_mondes"]})
    # lecture avant scellement : compagnon de la mesure retiré dans une copie
    cp = os.path.join(a.travail, "complet-copie-sans-compagnon")
    shutil.copytree(s1, cp, ignore=shutil.ignore_patterns("prive"))
    if os.path.exists(os.path.join(cp, "mesure-crible-iii-v1.json.sha256")):
        os.remove(os.path.join(cp, "mesure-crible-iii-v1.json.sha256"))
    cl2, lec2 = lire(cp)
    cas("liste d'arrêt : lecture avant le scellement de la sortie (étage 0)",
        isinstance(lec2, dict) and lec2.get("etage_arret") == 0, {"etage": lec2.get("etage_arret") if isinstance(lec2, dict) else lec2})
    # rapatriement : jamais les mondes ni le dossier privé
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        cr = LA.rapatrier(argparse.Namespace(source=s1, destination=os.path.join(a.travail, "rapatrie-complet"), mondes=a.mondes,
                                             mondes_sha256=a.mondes_sha256, repetes_permis=True))
    cas("rapatriement sans monde ni dossier privé", cr == 0 and '"aucun_monde": true' in buf.getvalue()
        and not os.path.exists(os.path.join(a.travail, "rapatrie-complet", "prive")), buf.getvalue().strip()[:200])
    # 2. artefacts de la chaîne réelle
    b = "2,4.8,2"
    code, s2, rel = jouer(a, "borne-appel", {"1|H": "lent-2.6"}, bornes_a_blanc=b,
                          echeance_utc_s=str(int(time.time()) + 17 * 3600))
    c1 = [x for x in (rel or {}).get("appels", []) if x["bras"] == "H" and x.get("coupe")]
    cas("liste d'arrêt : appel scripté au-delà de la borne par appel (coupé, compté en échec ; les autres files continuent)",
        code == 0 and [(x["monde"], x["bras"]) for x in c1] == [(1, "H")] and c1[0]["etat"] == "echec" and rel["complets"] == 19,
        {"code": code, "coupes": [(x["monde"], x["bras"]) for x in c1], "resume": resume(rel)})
    code, s3, rel = jouer(a, "limite", {"*|S": "limite"})
    cas("liste d'arrêt : erreurs de limite de débit au-dessus de 5 % (arrêt, code 3)",
        code == 3 and rel and rel["arret"]["ligne"] == "limite de débit", {"code": code, "resume": resume(rel)})
    code, s4, rel = jouer(a, "cout", {"*|H": "cout_excessif"})
    cas("liste d'arrêt : coût d'un appel au-dessus de son pire cas (code 3, dépense comptée)",
        code == 3 and rel and rel["arret"]["ligne"] == "coût au-dessus du pire cas", {"code": code, "resume": resume(rel)})

    def supprimer_temoin(bras, nom, r, dossier, res):
        if r == 3 and bras == "S":
            os.remove(os.path.join(dossier, "temoin-isolement.json"))
    code, s5, rel = jouer(a, "temoin", apres_appel=supprimer_temoin)
    cas("liste d'arrêt : témoin d'isolement supprimé (arrêt, code 3)",
        code == 3 and rel and rel["arret"]["ligne"] == "réponse brute ou témoin d'isolement absent", {"code": code, "resume": resume(rel)})
    code, s6, rel = jouer(a, "b-tronque", {"*|B": "tronque"})
    cm6 = mesurer(a, s6)[0] if code == 0 else None
    l6 = lire(s6)[1] if code == 0 else None
    cas("B tronqué partout : aucun monde complet, ligne du minimum (code 0), lecture « non concluant »",
        code == 0 and rel["arret"]["ligne"] == "minimum" and cm6 == 0 and isinstance(l6, dict) and l6.get("etage_arret") == 1,
        {"code": code, "resume": resume(rel), "mesure": cm6, "lecture": l6.get("verdicts") if isinstance(l6, dict) else l6})
    code, s7, rel = jouer(a, "p1-illisible", {"*|P1": "illisible"})
    sans = [k for k, v in (rel or {}).get("ensembles", {}).items() if v.get("sans_passe2")]
    cas("liste d'arrêt : passe 1 sans liste (ni D ni B ; aucune dépense de plus)",
        code == 0 and rel and not any(x["bras"] in ("D", "B") for x in rel["appels"]) and len(sans) > 0,
        {"code": code, "resume": resume(rel), "mondes_sans_passe2": len(sans)})
    code, s8, rel = jouer(a, "sept-cartes", {"*|D": "sept_cartes"})
    refusees = [c for c in (rel or {}).get("cartes", []) if c["bras"] == "D" and c["emplacement"] > 6]
    cas("gardien : carte au-delà de la sixième refusée (comptée)",
        code == 0 and refusees and all(c["etat"] == "refusee" for c in refusees), {"code": code, "refusees": len(refusees)})
    # 3. sonde des gabarits (κiii0), à blanc
    def sonde(nom, scenarios=None, **k):
        ns = argparse.Namespace(mode="a_blanc", arbre=a.arbre, mondes=a.mondes, mondes_sha256=a.mondes_sha256, texte_sha256=TEXTE_SHA,
                                sortie=os.path.join(a.travail, nom), releve_sonde=a.releve_sonde, scenarios_a_blanc=None,
                                registre_go=None, go_sonde=None, registre_lancements=None)
        if scenarios is not None:
            f = os.path.join(a.travail, f"scenarios-{nom}.json")
            with open(f, "x", encoding="utf-8") as g:
                json.dump(scenarios, g)
            ns.scenarios_a_blanc = f
        for x, v in k.items():
            setattr(ns, x, v)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(io.StringIO()):
            try:
                code = LA.sonde_gabarits(ns)
            except N.Refus as e:
                return 2, {"refus": str(e)}
        return code, json.load(open(os.path.join(ns.sortie, "releve-sonde-gabarits-crible-iii-v1.json"), encoding="utf-8"))
    code, rs = sonde("sonde-saine")
    cas("sonde des gabarits à blanc : trois appels (G1 par Pr-2, G2 par Pr-4 et Pr-2), règles d'avance non déclenchées, III-7 calculée",
        code == 0 and len(rs["appels"]) == 3 and rs["regles_d_avance"]["declenchee"] is False and rs["III_7"] is not None
        and [x["bras"] for x in rs["appels"]] == ["P1", "D", "B"],
        {"code": code, "regles": rs.get("regles_d_avance"), "III_7": rs.get("III_7"), "ensembles": rs.get("ensembles")})
    code, rs = sonde("sonde-g2-tronque", {"*|D": "tronque"})
    cas("sonde des gabarits : un appel sous G2 tronqué déclenche la règle d'avance (gabarit réécrit, crible non lancé)",
        code == 0 and rs["regles_d_avance"]["declenchee"] is True, {"regles": rs.get("regles_d_avance")})
    code, rs = sonde("sonde-g1-illisible", {"*|P1": "illisible"})
    cas("sonde des gabarits : aucune liste analysable sous G1 déclenche la règle d'avance (aucun appel sous G2)",
        code == 0 and rs["regles_d_avance"]["declenchee"] is True and len(rs["appels"]) == 1, {"regles": rs.get("regles_d_avance")})
    code, rs = sonde("sonde-reel-sans-ligne", mode="reel")
    cas("sonde réelle sans ligne κiii0 : refus avant tout appel", code == 2, rs)
    # 4. refus avant tout appel
    arbre = LA.Arbre(a.arbre)
    conf = arbre.configuration()
    conf2 = json.loads(json.dumps(conf))
    conf2["proposeurs"][N.PR4]["borne_sortie_jetons"] = 70000
    cas("liste d'arrêt : configuration autre que v12 (borne de Pr-4 changée)", LA.refuse_ou_none(LA.exiger_configuration, arbre, conf)
        is None and LA.refuse_ou_none(LA.exiger_configuration, arbre, conf2) is not None,
        LA.refuse_ou_none(LA.exiger_configuration, arbre, conf2))
    rs = os.path.join(a.travail, "releve-autre-configuration.json")
    r0 = json.load(open(a.releve_sonde, encoding="utf-8"))
    r0["configuration_sha256"] = "0" * 64
    octets = (json.dumps(r0, ensure_ascii=False, sort_keys=True, indent=1) + "\n").encode()
    open(rs, "wb").write(octets)
    open(rs + ".sha256", "w").write(f"{hashlib.sha256(octets).hexdigest()}  {os.path.basename(rs)}\n")
    cas("liste d'arrêt : relevé de la sonde v74 d'une autre configuration",
        LA.refuse_ou_none(LA.exiger_releve_sonde, arbre, conf, a.releve_sonde) is None
        and LA.refuse_ou_none(LA.exiger_releve_sonde, arbre, conf, rs) is not None
        and LA.refuse_ou_none(LA.exiger_releve_sonde, arbre, conf, rs + ".absent") is not None,
        LA.refuse_ou_none(LA.exiger_releve_sonde, arbre, conf, rs))
    cas("liste d'arrêt : monde sans tirage conforme en 8", True if LA.refuse_ou_none(
        LA.exiger_mondes_generes, [{"monde": r, "spec": {"r": r}, "spec_sha256": str(r)} for r in N.MONDES]) is None else False,
        LA.refuse_ou_none(LA.exiger_mondes_generes, [{"monde": 1, "spec": None, "refus": ["C8"] * 8}] +
                          [{"monde": r, "spec": {"r": r}, "spec_sha256": str(r)} for r in N.MONDES[1:]]))
    code, _, rel = jouer(a, "garde-depart", echeance_utc_s=str(int(time.time()) + 35000))
    cas("liste d'arrêt : garde de départ (moins de 10 h avant l'échéance : refus, aucun dossier)",
        code == 2 and not os.path.exists(os.path.join(a.travail, "garde-depart")), rel)
    code, _, rel = jouer(a, "reel-sans-options", mode="reel")
    cas("mode réel : options exigées absentes (refus avant tout dossier)", code == 2 and "options exigées" in rel["refus"], rel)
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("127.0.0.1", conf["proposeurs"][N.PR4]["port"]))
    s.listen(1)
    try:
        code, _, rel = jouer(a, "port-occupe")
    finally:
        s.close()
    cas("ports des relais occupés : refus avant tout appel", code == 2 and "ports" in rel["refus"], rel)
    # 5. gardes du mode réel (sans relais ni appel) : interpréteur à numpy 2.5.3 exigé par la configuration v12
    if a.python_reel:
        d = os.path.join(a.travail, "gardes-reel")
        os.makedirs(d)
        texte = os.path.join(d, "texte.md")
        open(texte, "w", encoding="utf-8").write("Texte factice des gardes du mode réel.\n")
        ts = hashlib.sha256(open(texte, "rb").read()).hexdigest()
        lignes = [f"{hashlib.sha256(open(os.path.join(ICI, f), 'rb').read()).hexdigest()}  {LA.DOSSIER_DU_CODE}/{f}"
                  for f in LA.FICHIERS_DU_CRIBLE]
        open(os.path.join(d, "addendum.md"), "w", encoding="utf-8").write(f"texte {ts}\n" + "\n".join(lignes) + "\n")
        open(os.path.join(d, "addendum-faux.md"), "w", encoding="utf-8").write(f"texte {ts}\n" + "\n".join(lignes[1:]) + "\n")
        jour = time.strftime("%Y-%m-%d", time.gmtime())
        open(os.path.join(d, "go.md"), "w", encoding="utf-8").write(
            f"| GO-2026-11-17-81 | {jour} | calcul | Organisme d'idéation, crible (iii) : fable52 et opus55 (essai) | 260 USD (sur crédits) "
            f"| 2026-11-30 | Lazar | GO-2026-11-15-06 |\n| GO-2026-11-17-82 | {jour} | calcul | Même crible, machine jetable seule (essai) "
            f"| 3 USD | 2026-11-30 | Lazar | GO-2026-11-15-06 |\n")
        shas = [hashlib.sha256(f"monde factice {r}".encode()).hexdigest() for r in N.MONDES]
        mondes = os.path.join(d, "MONDES.json")
        open(mondes, "wb").write(b"factice")
        hm = hashlib.sha256(b"factice").hexdigest()
        for nom, public in (("", False), ("-public", True)):
            os.makedirs(d + nom, exist_ok=True)
        json.dump({"texte_sha256": ts, "fichier_mondes_sha256": hm, "public": False, "mondes_sha256": shas},
                  open(mondes + ".engagement.json", "w"))
        code = f"""
import argparse, json, sys
sys.path.insert(0, {ICI!r})
import crible_iii_v1 as N, lanceur_crible_iii_v1 as LA
arbre = LA.Arbre({a.arbre!r}); conf = arbre.configuration()
def ns(**k):
    b = dict(texte={texte!r}, texte_sha256={ts!r}, registre_go={os.path.join(d, 'go.md')!r}, go_credits="GO-2026-11-17-81",
             go_hors="GO-2026-11-17-82", mondes={mondes!r}, mondes_sha256={hm!r}, mondes_shas={",".join(shas)!r},
             registre_lancements={os.path.join(d, 'lancements.jsonl')!r}, addendum={os.path.join(d, 'addendum.md')!r},
             scenarios_a_blanc=None, bornes_a_blanc=None, repetes_permis=False)
    b.update(k); return argparse.Namespace(**b)
def essai(**k):
    try:
        LA.exiger_mode_reel(ns(**k), arbre, conf); return None
    except N.Refus as e:
        return str(e)
open({os.path.join(d, 'lancements-deja.jsonl')!r}, "w").write(json.dumps({{"texte_sha256": {ts!r}}}) + "\\n")
print(json.dumps({{"sain": essai(), "addendum_faux": essai(addendum={os.path.join(d, 'addendum-faux.md')!r}),
                  "second_lancement": essai(registre_lancements={os.path.join(d, 'lancements-deja.jsonl')!r}),
                  "ligne_absente": essai(go_hors="GO-2026-11-17-83"), "mondes_autres": essai(mondes_shas=",".join(["0" * 64] * 20)),
                  "scenarios": essai(scenarios_a_blanc="x")}}, ensure_ascii=False))
"""
        r = subprocess.run([a.python_reel, "-I", "-B", "-c", code], capture_output=True, text=True, encoding="utf-8", timeout=600)
        try:
            g = json.loads(r.stdout.strip().splitlines()[-1])
        except (ValueError, IndexError):
            g = {"sortie": (r.stdout + r.stderr)[-400:]}
        cas("gardes du mode réel : addendum, ligne de GO, engagement, second lancement, scénario (sain accepté, chaque artefact refusé)",
            g.get("sain") is None and "sain" in g and all(g.get(k) for k in ("addendum_faux", "second_lancement", "ligne_absente",
                                                                            "mondes_autres", "scenarios")), g)
    ko = [n for n, ok, _ in R if not ok]
    print(f"ESSAI A BLANC : {len(R)} cas, {len(R) - len(ko)} conformes, {len(ko)} écarts ; durée {time.time() - t0:.0f} s")
    return 0 if not ko else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
