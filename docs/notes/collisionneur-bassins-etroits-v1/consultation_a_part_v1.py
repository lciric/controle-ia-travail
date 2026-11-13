#!/usr/bin/env python3
"""Consultations à part (Argon, Astra, Kimi), hors du protocole de collision — v1.

Écrit le 13 novembre 2026 par l'opérateur neuf du tour « bassins étroits » (Claude Opus 5.5), sur la consigne
`consigne-collisionneur-bassins-etroits-v2.md` (`2a3b09b1…`), point 3.

- Importe le script du collisionneur **par son chemin, sans le modifier**, après avoir vérifié son empreinte
  (`EMPREINTE_SCRIPT`) ; n'utilise que ses objets existants : MODELES, appeler_gemini, appeler_openai, appeler_kimi,
  statut_reponse, cout, cout_pire_cas, empreinte, normaliser (et PREAMBULE_GABARIT, d'où les six règles d'intégrité sont
  recopiées mot pour mot, et MARQUEUR n'est pas utilisé : le marqueur est FIN-DE-CONSULTATION).
- Un appel par modèle, **un seul essai** (les attentes de transport déjà dans les fonctions d'appel exceptées) ; aucun
  repli, aucune relance, aucune reformulation.
- Pire cas calculé avant tout appel ; arrêt (code 2), sans appel, s'il dépasse --plafond-usd ; contrôle refait avant
  chaque appel (dépense déjà faite + pire cas de l'appel).
- Par consultation, dans un dossier de sortie neuf : prompt servi (`prompt.txt`), réponse entière telle que la rend la
  fonction d'appel du script (`reponse-brute.json` : tous les champs de l'objet Reponse ; les fonctions du script ne
  rendent pas le corps JSON du fournisseur), texte extrait (`texte.md`), et `releve.json` (statut, modèle demandé et servi,
  usage, coût au barème du script, heures UTC, empreintes, marqueur de fin). Aucun fichier n'est jamais écrasé.
- Clés : lues par les fonctions d'appel du script dans GEMINI_API_KEY et OPENAI_API_KEY ; Kimi par son relais local
  (KIMI_RELAIS_URL), sans clé ici. Jamais affichées ni écrites.

Usage :
  python consultation_a_part_v1.py --script SCRIPT.py --faits FAITS.md --question QUESTION.md --sortie DOSSIER \
      --plafond-usd X [--modeles argon,astra,kimi] [--devis]
Codes : 0 fini (chaque consultation a son relevé, valide ou non), 1 usage, 2 plafond (aucun appel).
"""
import argparse
import dataclasses
import datetime
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

VERSION = "consultation-a-part-v1"
EMPREINTE_SCRIPT = "4ad78ccce8228aed2679c854eaec7ee4d2ab8f867098218387024adfeb1e7756"
MARQUEUR = "FIN-DE-CONSULTATION"
# nom -> (lettre de l'espèce dans MODELES du script, fonction d'appel, plafond de sortie en jetons)
CONSULTATIONS = {
    "argon": ("C", "appeler_gemini", 24000),
    "astra": ("E", "appeler_openai", 16000),
    "kimi": ("D", "appeler_kimi", None),  # None : plafond du script pour D (MODELES["D"]["max"])
}
INTRO = ("Tu es consulté seul, hors de tout échange avec d'autres modèles, par Lazar Ciric, directeur d'un programme de "
         "recherche, sur une question de conception.")
FORMAT = ("Format : français, Markdown, au plus 5 000 mots ; développe les mathématiques (définitions, énoncés, esquisses "
          "de preuve quand tu en as). Termine par une ligne qui contient exactement : " + MARQUEUR)


class Arret(Exception):
    def __init__(self, code, message):
        super().__init__(message)
        self.code = code


def maintenant():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def charger_script(chemin):
    chemin = Path(chemin)
    h = hashlib.sha256(chemin.read_bytes()).hexdigest()
    if h != EMPREINTE_SCRIPT:
        raise Arret(1, f"script du collisionneur : empreinte {h} au lieu de {EMPREINTE_SCRIPT} ; arrêt")
    spec = importlib.util.spec_from_file_location("collisionneur_v8_plafonds_bas_v1", chemin)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def regles_integrite(script):
    """Les six règles d'intégrité du préambule du collisionneur, recopiées mot pour mot (en-tête compris)."""
    g = script.PREAMBULE_GABARIT
    debut = g.index("Règles d'intégrité")
    fin = g.index("\n\nRègles du protocole")
    bloc = g[debut:fin]
    if "{" in bloc or not all(f"\n{i}. " in bloc for i in range(1, 7)) or "\n7. " in bloc:
        raise Arret(1, "règles d'intégrité introuvables ou inattendues dans le préambule du script")
    return bloc


def lire(script, chemin):
    try:
        return script.normaliser(Path(chemin).read_bytes().decode("utf-8-sig"))
    except (OSError, UnicodeDecodeError) as e:
        raise Arret(1, f"{Path(chemin).name} illisible ({type(e).__name__})")


def construire_prompt(script, faits, question):
    h_f, h_q = script.empreinte(faits), script.empreinte(question)
    morceaux = [INTRO, regles_integrite(script), FORMAT,
                f"<<<DÉBUT FAITS sha256={h_f}>>>\n{faits}\n<<<FIN FAITS>>>",
                f"<<<DÉBUT QUESTION DE L'ARBITRE sha256={h_q}>>>\n{question}\n<<<FIN QUESTION DE L'ARBITRE>>>"]
    return "\n\n".join(morceaux) + "\n", h_f, h_q


def plan(script, noms):
    lignes = []
    for nom in noms:
        lettre, fonction, max_tokens = CONSULTATIONS[nom]
        m = script.MODELES[lettre]
        lignes.append({"nom": nom, "lettre": lettre, "modele": m["id"], "fournisseur": m["fournisseur"],
                       "fonction": fonction, "prix": m["prix"], "max_tokens": max_tokens or m["max"]})
    return lignes


def ecrire_neuf(chemin, texte):
    chemin = Path(chemin)
    with open(chemin, "x", encoding="utf-8", newline="\n") as f:
        f.write(texte)
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


def conforme(demande, servi):
    return isinstance(servi, str) and (servi == demande or servi.startswith(demande + "-"))


def consulter(script, ligne, prompt, h_prompt, dossier, appelant, h_f, h_q):
    d = Path(dossier) / ligne["nom"]
    d.mkdir(parents=True, exist_ok=False)
    ecrire_neuf(d / "prompt.txt", prompt)
    debut = maintenant()
    print(f"[{debut}] {ligne['nom']} : {ligne['modele']}, plafond de sortie {ligne['max_tokens']} jetons", flush=True)
    try:
        rep = appelant(ligne["modele"], prompt, ligne["max_tokens"])
    except Exception as e:  # imprévu : consigné ; jamais de repli
        rep = None
        exception = f"exception {type(e).__name__} : {str(e)[:300]}"
    fin_utc = maintenant()
    if rep is None:
        brut = {"exception": exception}
        statut, texte, usage, servi = "ECHEC", "", {"entree": 0, "sortie": 0}, None
    else:
        brut = dataclasses.asdict(rep)
        texte = script.normaliser(rep.texte or "")
        usage, servi = rep.usage, rep.modele_servi
        if rep.echec:
            statut = "ECHEC"
        elif not conforme(ligne["modele"], servi):
            statut = "MODELE_DIFFERENT"
        else:
            statut = script.statut_reponse(ligne["fournisseur"], rep)
    ecrire_neuf(d / "reponse-brute.json", json.dumps(brut, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    h_texte = ecrire_neuf(d / "texte.md", texte)
    marqueur = texte.rstrip().endswith(MARQUEUR)
    c = round(script.cout(ligne["prix"], usage), 4)
    releve = {"version": VERSION, "consultation": ligne["nom"], "modele_demande": ligne["modele"],
              "modele_servi": servi, "fournisseur": ligne["fournisseur"], "max_tokens": ligne["max_tokens"],
              "statut": statut, "fin": None if rep is None else rep.fin,
              "categorie_refus": None if rep is None else rep.categorie,
              "echec": None if rep is None else rep.echec, "usage": usage, "prix_bareme_script": list(ligne["prix"]),
              "cout_usd_bareme_script": c, "sha256_prompt": h_prompt, "sha256_faits": h_f, "sha256_question": h_q,
              "sha256_texte": h_texte, "caracteres": len(texte), "marqueur_fin": marqueur,
              "valide": statut == "OK" and marqueur, "debut_utc": debut, "fin_utc": fin_utc,
              "sha256_script_collisionneur": EMPREINTE_SCRIPT}
    ecrire_neuf(d / "releve.json", json.dumps(releve, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    print(f"    statut {statut}, fin {releve['fin']}, {usage.get('sortie', 0)} jetons de sortie, marqueur "
          f"{'oui' if marqueur else 'non'}, {c:.4f} USD", flush=True)
    return releve


def principal(argv=None, appelants=None):
    p = argparse.ArgumentParser(description="Consultations à part (un appel par modèle, un seul essai)")
    p.add_argument("--script", required=True)
    p.add_argument("--faits", required=True)
    p.add_argument("--question", required=True)
    p.add_argument("--sortie")
    p.add_argument("--plafond-usd", type=float, required=True)
    p.add_argument("--modeles", default="argon,astra,kimi")
    p.add_argument("--devis", action="store_true", help="pire cas seulement, aucun appel, rien d'écrit")
    a = p.parse_args(argv)
    try:
        script = charger_script(a.script)
        noms = [n.strip() for n in a.modeles.split(",") if n.strip()]
        if not noms or any(n not in CONSULTATIONS for n in noms) or len(set(noms)) != len(noms):
            raise Arret(1, f"--modeles : parmi {sorted(CONSULTATIONS)}, sans doublon")
        prompt, h_f, h_q = construire_prompt(script, lire(script, a.faits), lire(script, a.question))
        h_prompt = script.empreinte(prompt)
        lignes = plan(script, noms)
        pires = {l["nom"]: script.cout_pire_cas(l["prix"], len(prompt), l["max_tokens"]) for l in lignes}
        total = sum(pires.values())
        print(f"{VERSION} ; prompt {len(prompt)} caractères, sha256 {h_prompt} ; faits {h_f} ; question {h_q}")
        for l in lignes:
            print(f"  {l['nom']:6s} {l['modele']:16s} plafond de sortie {l['max_tokens']:6d} ; prix {l['prix']} ; "
                  f"pire cas {pires[l['nom']]:.4f} USD")
        print(f"  pire cas total {total:.4f} USD ; plafond {a.plafond_usd:.2f} USD")
        if total > a.plafond_usd:
            raise Arret(2, f"pire cas {total:.4f} USD > plafond {a.plafond_usd:.2f} USD ; aucun appel")
        if a.devis:
            return 0
        if not a.sortie:
            raise Arret(1, "--sortie obligatoire hors --devis")
        sortie = Path(a.sortie)
        if sortie.exists():
            raise Arret(1, f"{sortie} existe déjà : dossier de sortie neuf exigé (on n'écrase jamais)")
        sortie.mkdir(parents=True)
        appelants = appelants or {n: getattr(script, l["fonction"]) for n, l in zip(noms, lignes)}
        depense = 0.0
        releves = []
        for l in lignes:
            if depense + pires[l["nom"]] > a.plafond_usd:
                raise Arret(2, f"{l['nom']} : dépense {depense:.4f} + pire cas {pires[l['nom']]:.4f} > plafond ; "
                               f"aucun appel")
            r = consulter(script, l, prompt, h_prompt, sortie, appelants[l["nom"]], h_f, h_q)
            depense += r["cout_usd_bareme_script"]
            releves.append({k: r[k] for k in ("consultation", "modele_demande", "modele_servi", "statut", "fin",
                                              "marqueur_fin", "valide", "usage", "cout_usd_bareme_script",
                                              "debut_utc", "fin_utc")})
        resume = {"version": VERSION, "sha256_prompt": h_prompt, "pire_cas_usd": round(total, 4),
                  "plafond_usd": a.plafond_usd, "depense_usd_bareme_script": round(depense, 4),
                  "consultations": releves, "fin_utc": maintenant()}
        ecrire_neuf(sortie / "resume.json", json.dumps(resume, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
        print(f"fini ; dépense au barème du script {depense:.4f} USD")
        return 0
    except Arret as e:
        print(f"ARRÊT (code {e.code}) : {e}", file=sys.stderr)
        return e.code


if __name__ == "__main__":
    sys.exit(principal())
