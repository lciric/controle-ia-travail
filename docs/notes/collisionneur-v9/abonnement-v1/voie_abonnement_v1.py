"""Voie « abonnement » des cellules Claude (v1) : enveloppe des moteurs scellés, sans les modifier.

Mot de la mère (GO-2026-11-22-70, 14:01Z) : les cellules Claude passent par des sessions filles éphémères de
l'abonnement, que la mère crée ; la session des collisionneurs prépare un kit par cellule et recueille les réponses.
Classe B, Opus 5.5. Aucun appel à Anthropic par cette voie : ni génération, ni comptage.

Principe, par vagues :
- pour une cellule d'une espèce d'Anthropic sans réponse recueillie, l'enveloppe écrit le kit
  (DOSSIER/abonnement/kits/CID/texte-servi.md et fiche.json, chacun avec son .sha256) et rend « KIT » au lieu de partir ;
  les cellules des autres fournisseurs du même tour partent par l'interface comme d'habitude ; la porte se ferme à la
  fin du tour (code 2, « kits en attente ») ;
- la mère crée une session par kit (sans dépôt, modèle et effort de la fiche, invite = texte servi) ;
- « recueillir » verse la réponse (DOSSIER/abonnement/reponses/CID.md et CID.json, scellés), liée à l'empreinte
  du texte servi ; la relance du même dossier lit la réponse par le chemin ordinaire du moteur (executer_cellule,
  juger, cellule écrite), coût zéro, usage déclaré non mesuré, et une ligne « voie_abonnement » au journal.
Le comptage des jetons d'Anthropic est retiré (estimation du moteur, caractères par jeton de la table) : aucun appel
sur la clé. Un dossier ne mêle pas deux voies : une cellule d'Anthropic déjà jouée par l'interface arrête tout.
L'essaim n'est admis qu'en ordre « simultane » (les invites d'un même temps ne lisent pas les textes de ce temps).
"""
import argparse
import datetime
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

VERSION = "voie-abonnement-v1"
ICI = Path(__file__).resolve().parent
MOTEURS = {  # nom : (chemin, empreinte) ; rien d'autre n'est chargé
    "v8m": (ICI.parent / "collisionneur_v9_v8m.py",
            "420394f9d803bc4eb41f0e469a30e0be647e11a2c91ac9f42e70c90fdb31c377"),
    "v8p": (ICI.parent / "collisionneur_v9_v8p.py",
            "5979c712101034265d5a7dcacc2110b691f97e69b3c4158d8a3c6c2af6704290"),
}
ESSAIM = (ICI.parent / "essaim-v1" / "collisionneur_v9_essaim_v7.py",
          "98397f49a9366d6c79a0ad47df3e62300db4e83d97de2ac28f3a43af7b71362c")
BRANCHE_DEFAUT = "runs/collisionneurs-reprise-v8d-v1"
EFFORT_SESSION = "max"
CODE_USAGE, CODE_PORTE = 1, 2


def empreinte(texte):
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


def maintenant():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def charger(chemin, sha, nom):
    h = hashlib.sha256(Path(chemin).read_bytes()).hexdigest()
    if h != sha:
        raise SystemExit(f"ARRÊT : empreinte de {chemin} {h} différente de {sha}")
    spec = importlib.util.spec_from_file_location(nom, chemin)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def ecrire_scelle(chemin, texte):
    """Écrit F et F.sha256 ; si F existe, il doit être identique (R12 : jamais écrasé), sinon arrêt."""
    chemin = Path(chemin)
    if chemin.exists():
        if chemin.read_text(encoding="utf-8") != texte:
            raise ValueError(f"{chemin} existe avec un autre contenu ; rien n'est écrasé")
        return empreinte(texte)
    chemin.parent.mkdir(parents=True, exist_ok=True)
    with open(chemin, "x", encoding="utf-8", newline="\n") as f:
        f.write(texte)
    h = empreinte(texte)
    with open(str(chemin) + ".sha256", "x", encoding="utf-8", newline="\n") as f:
        f.write(f"{h}  {chemin.name}\n")
    return h


def lire_scelle(chemin):
    chemin = Path(chemin)
    texte = chemin.read_text(encoding="utf-8")
    sceau = Path(str(chemin) + ".sha256").read_text(encoding="utf-8").split()[0]
    if empreinte(texte) != sceau:
        raise ValueError(f"{chemin} : empreinte {empreinte(texte)} différente du sceau {sceau}")
    return texte


def rep_abonnement(dossier):
    return Path(dossier) / "abonnement"


def recueil(dossier, cid):
    """La réponse recueillie de la cellule, ou None ; refus si elle est mal scellée."""
    j = rep_abonnement(dossier) / "reponses" / f"{cid}.json"
    if not j.exists():
        return None
    fiche = json.loads(lire_scelle(j))
    texte = lire_scelle(rep_abonnement(dossier) / "reponses" / f"{cid}.md")
    if empreinte(texte) != fiche["sha256_reponse"]:
        raise ValueError(f"{cid} : réponse différente de sa fiche de recueil")
    return fiche, texte


class Voie:
    """Remplace executer_cellule du moteur `v` pour les espèces d'Anthropic ; les autres passent à l'original."""

    def __init__(self, v, branche):
        self.v, self.branche, self.kits = v, branche, set()
        self.original = v.executer_cellule
        v.COMPTEURS.pop("anthropic", None)  # aucun comptage sur la clé : estimation du moteur
        v.executer_cellule = self.executer

    def executer(self, dossier, tour, lettre, prompt, pieces, plafond, appelants, repli_lot=False):
        v = self.v
        m = v.MODELES[lettre]
        if m["fournisseur"] != "anthropic":
            return self.original(dossier, tour, lettre, prompt, pieces, plafond, appelants, repli_lot)
        cid = v.id_cellule(tour, lettre)
        if any(e.get("id_reponse") != "abonnement" for e in v.essais_journal(dossier, cid)):
            raise v.Arret(CODE_USAGE, f"{cid} : cellule d'Anthropic déjà jouée par l'interface dans ce dossier ; "
                                      f"deux voies ne se mêlent pas ; rien n'est fait")
        h = empreinte(prompt)
        kit = rep_abonnement(dossier) / "kits" / cid
        r = recueil(dossier, cid)
        if r is None:
            ecrire_scelle(kit / "texte-servi.md", prompt)
            fiche = {"cellule": cid, "modele": m["id"], "espece": m["espece"], "effort": EFFORT_SESSION,
                     "outils": "aucun", "depot": "aucun (session sans source_url)",
                     "sha256_texte_servi": h, "caracteres": len(prompt),
                     "branche_versement": self.branche,
                     "reponse_attendue": f"abonnement/reponses/{cid}.md", "programme": VERSION}
            ecrire_scelle(kit / "fiche.json", json.dumps(fiche, ensure_ascii=False, indent=1) + "\n")
            if not any(e.get("kit_abonnement") == cid for e in v.lire_journal(dossier)):
                v.ajouter_journal(dossier, {"kit_abonnement": cid, "sha256_texte_servi": h, "modele": m["id"],
                                            "quand": maintenant(), "programme": VERSION})
            print(f"{cid} : kit écrit ({kit}), en attente de la session de l'abonnement", flush=True)
            self.kits.add(cid)
            return "KIT"
        fiche, texte = r
        if fiche["sha256_texte_servi"] != h:
            raise v.Arret(CODE_USAGE, f"{cid} : réponse recueillie pour un autre texte servi "
                                      f"({fiche['sha256_texte_servi']} ≠ {h}) ; rien n'est fait")
        if fiche["modele_demande"] != m["id"]:
            raise v.Arret(CODE_USAGE, f"{cid} : fiche de recueil pour {fiche['modele_demande']}, espèce {m['id']}")
        v.ajouter_journal(dossier, {"voie_abonnement": cid, "session": fiche["session"],
                                    "modele_servi_session": fiche["modele_servi"], "effort_session": fiche["effort"],
                                    "sha256_texte_servi": h, "sha256_reponse": fiche["sha256_reponse"],
                                    "usage": "non mesuré (abonnement) ; coût d'interface zéro", "quand": maintenant(),
                                    "programme": VERSION})

        def lecteur(m2, prompt2, max_tokens):
            if empreinte(prompt2) != h:
                return v.Reponse(echec="texte servi changé entre le recueil et la lecture")
            return v.Reponse(texte=texte, modele_servi=fiche["modele_servi"], identifiant="abonnement",
                             fin="end_turn", usage={"entree": 0, "sortie": 0}, usage_lu=True)

        return self.original(dossier, tour, lettre, prompt, pieces, plafond, dict(appelants, anthropic=lecteur),
                             repli_lot)


def refuser_anthropic(m, prompt, max_tokens):
    raise AssertionError("voie abonnement : aucun appel direct à Anthropic")


def lancer_moteur(nom, branche, argv, v=None, appelants=None):
    v = v or charger(*MOTEURS[nom], f"moteur_{nom}_voie_abonnement")
    voie = Voie(v, branche)
    code = v.principal(argv, appelants=dict(appelants or v.APPELANTS, anthropic=refuser_anthropic))
    if voie.kits:
        print(f"KITS EN ATTENTE ({len(voie.kits)}) : {sorted(voie.kits)}", flush=True)
    return code


def lancer_essaim(branche, argv, v=None, mod=None, appelants=None):
    mod = mod or charger(*ESSAIM, "essaim_v7_voie_abonnement")
    v = v or mod.charger_moteur()
    voie = Voie(v, branche)
    appel_original = mod.appel

    def appel(v_, cfg, tirage, dossier, phase, k, lettre, plafond, absences, appelants_):
        avant = len(voie.kits)
        try:
            return appel_original(v_, cfg, tirage, dossier, phase, k, lettre, plafond, absences, appelants_)
        except v.Arret:
            if len(voie.kits) > avant:
                return "KIT"
            raise

    def porte(quoi):
        if voie.kits:
            raise v.Arret(CODE_PORTE, f"kits en attente après {quoi} : {sorted(voie.kits)} ; recueillir, puis relancer "
                                      f"le même dossier avec --reprise")

    def derouler(v_, cfg, tirage, dossier, plafond, absences, appelants_):
        """Copie de derouler de l'essaim v7, avec la porte des kits après chaque temps."""
        if cfg.get("ordre") != "simultane":
            raise v.Arret(CODE_USAGE, f"ordre {cfg.get('ordre')!r} : la voie abonnement n'admet que « simultane »")
        for l in tirage["ordres"]["0"]:
            appel(v_, cfg, tirage, dossier, "temps0", 0, l, plafond, absences, appelants_)
        porte("le temps 0")
        manquants = [l for l in v_.LETTRES if not v_.cellule_valide(dossier, v_.id_cellule(mod.TOUR_BROUILLON, l))
                     and v_.id_cellule(mod.TOUR_BROUILLON, l) not in absences]
        if manquants:
            raise v_.Arret(v_.CODE_PORTE, f"brouillons manquants {manquants}")
        for k in range(1, cfg["cycles"] + 1):
            etats = [appel(v_, cfg, tirage, dossier, "temps1", k, l, plafond, absences, appelants_)
                     for l in tirage["ordres"][str(k)]]
            porte(f"le cycle {k}")
            if all(e != "FAIT" for e in etats):
                if not any(e.get("arret_societe") for e in v_.lire_journal(dossier)):
                    v_.ajouter_journal(dossier, {"arret_societe": k, "motif": "aucun agent appelé à ce cycle (parts "
                                                                             "épuisées ou absences) : fin du temps 1",
                                                 "quand": v_.maintenant(), "programme": mod.VERSION})
                break
        for l in tirage["ordres"][str(cfg["cycles"] + 1)]:
            appel(v_, cfg, tirage, dossier, "temps2", 0, l, plafond, absences, appelants_)
        porte("le temps final")

    mod.appel, mod.derouler = appel, derouler
    code = mod.principal(argv, appelants=dict(appelants or v.APPELANTS, anthropic=refuser_anthropic), v=v)
    if voie.kits:
        print(f"KITS EN ATTENTE ({len(voie.kits)}) : {sorted(voie.kits)}", flush=True)
    return code


def recueillir(dossier, cid, chemin_texte, session, modele_servi):
    """Verse la réponse finale d'une session fille (texte lu par les événements de la session, enregistré tel quel)."""
    kit = rep_abonnement(dossier) / "kits" / cid
    fiche_kit = json.loads(lire_scelle(kit / "fiche.json"))
    servi = lire_scelle(kit / "texte-servi.md")
    if empreinte(servi) != fiche_kit["sha256_texte_servi"]:
        raise SystemExit(f"ARRÊT : {cid} : texte servi différent de sa fiche")
    if not (modele_servi == fiche_kit["modele"] or modele_servi.startswith(fiche_kit["modele"] + "-")):
        raise SystemExit(f"ARRÊT : {cid} : modèle servi {modele_servi!r} au lieu de {fiche_kit['modele']!r} ; "
                         f"défaut de la cellule, rien n'est versé")
    texte = Path(chemin_texte).read_text(encoding="utf-8")
    if not texte.strip():
        raise SystemExit(f"ARRÊT : {cid} : réponse vide ; défaut de la cellule, rien n'est versé")
    rep = rep_abonnement(dossier) / "reponses"
    h = ecrire_scelle(rep / f"{cid}.md", texte)
    fiche = {"cellule": cid, "voie": "abonnement", "session": session, "modele_demande": fiche_kit["modele"],
             "modele_servi": modele_servi, "effort": fiche_kit["effort"],
             "sha256_texte_servi": fiche_kit["sha256_texte_servi"], "sha256_reponse": h,
             "recueilli": maintenant(), "programme": VERSION}
    ecrire_scelle(rep / f"{cid}.json", json.dumps(fiche, ensure_ascii=False, indent=1) + "\n")
    print(f"{cid} : réponse versée ({len(texte)} caractères, {h[:12]}…)")
    return 0


def kits_en_attente(dossier):
    base = rep_abonnement(dossier) / "kits"
    attente = [p.name for p in sorted(base.iterdir()) if p.is_dir() and recueil(dossier, p.name) is None] \
        if base.exists() else []
    for cid in attente:
        f = json.loads(lire_scelle(base / cid / "fiche.json"))
        print(f"{cid}\t{f['modele']}\teffort {f['effort']}\t{f['sha256_texte_servi']}\t{base / cid / 'texte-servi.md'}")
    return 0


def principal(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sous = p.add_subparsers(dest="commande", required=True)
    for nom in ("v8m", "v8p", "essaim"):
        s = sous.add_parser(nom, help=f"lance le {nom} sous la voie abonnement ; arguments du programme après --")
        s.add_argument("--branche", default=BRANCHE_DEFAUT)
        s.add_argument("reste", nargs=argparse.REMAINDER)
    r = sous.add_parser("recueillir")
    r.add_argument("dossier")
    r.add_argument("cellule")
    r.add_argument("--texte", required=True)
    r.add_argument("--session", required=True)
    r.add_argument("--modele-servi", required=True)
    k = sous.add_parser("kits")
    k.add_argument("dossier")
    a = p.parse_args(argv)
    if a.commande in ("v8m", "v8p", "essaim"):
        reste = a.reste[1:] if a.reste[:1] == ["--"] else a.reste
        return lancer_essaim(a.branche, reste) if a.commande == "essaim" else lancer_moteur(a.commande, a.branche, reste)
    if a.commande == "recueillir":
        return recueillir(a.dossier, a.cellule, a.texte, a.session, a.modele_servi)
    return kits_en_attente(a.dossier)


if __name__ == "__main__":
    sys.exit(principal())
