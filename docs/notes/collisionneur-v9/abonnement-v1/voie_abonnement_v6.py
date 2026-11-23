"""Voie « abonnement » des cellules Claude (v6) : enveloppe des moteurs scellés, sans les modifier.

v6 (GO-2026-11-22-114, mot de Lazar relayé par la mère) : l'effort de Fable suit la difficulté, la portée et
l'importance ; « max » pour un texte décisif à sceller ou un juge de dernier recours, « xhigh » pour une rédaction
importante, « high » pour une cellule de collisionneur, une relecture, un avis. --effort admet donc max|xhigh|high ;
le reste est la v5 (l'effort est écrit dans chaque fiche de kit et rendu dans la ligne voie_abonnement). Rien
d'autre ne change.

En-tête de la v5 :
Voie « abonnement » des cellules Claude (v5) : enveloppe des moteurs scellés, sans les modifier.

v5 (GO-2026-11-22-73, mot de Lazar) : l'effort de la session est un argument obligatoire, --effort max|xhigh
(« max » seulement pour les cellules décisives ; ailleurs « xhigh » pour Fable et Opus) ; il est écrit dans chaque
fiche de kit et rendu dans la ligne voie_abonnement. Rien d'autre ne change.

En-tête de la v4 :
Voie « abonnement » des cellules Claude (v4) : enveloppe des moteurs scellés, sans les modifier.

v4, dernier passage du contre-lecteur (v3 31975897…) : les échecs rendus par le lecteur portent identifiant
« abonnement » (sinon le contrôle du mélange les prenait pour des essais par l'interface et bloquait le dossier après
une absence acceptée) ; la configuration de l'essaim est lue aussi sous la forme --configuration=F, et un fichier
illisible arrête avec un nom, sans trace.

En-tête de la v3 :
Voie « abonnement » des cellules Claude (v3) : enveloppe des moteurs scellés, sans les modifier.

v3, vérification des corrections par le même contre-lecteur (v2 017d5e22…) :
- la réponse recueillie n'est servie au moteur qu'une fois : tout essai suivant du plan (relance au plafond relevé,
  rejeu à un autre effort) rend un échec nommé « relance impossible par la voie abonnement » ; aucun essai fictif ;
- le filet d'erreurs ne couvre plus que le kit et le recueil, jamais l'appel au moteur ;
- « recueillir » refuse le vide aussi en max_tokens (seul un refus peut être vide) : sous v8m à l'effort maximal, un
  vide coupé déclencherait un rejeu déclaré à un autre effort qui n'aurait pas lieu ;
- l'essaim : ordre, parts et réserve des finales contrôlés sur la configuration AVANT le programme ; rien n'est écrit.

En-tête de la v2 :
Voie « abonnement » des cellules Claude (v2) : enveloppe des moteurs scellés, sans les modifier.

v2, corrections de la contre-lecture d'Opus (v1 f541af00…) :
- B1 : garde des motifs, plafond et ligne contrôlés AVANT l'écriture du kit (pire cas au plafond de relance) ;
- B2 : mélange de voies contrôlé sur tout le dossier (aucun essai d'Anthropic par l'interface, quelle que soit la
  cellule) ; sens inverse hors de portée : le moteur nu relancé sur un dossier à kits appellerait l'interface, il ne
  faut donc relancer un tel dossier que par cette enveloppe ;
- B3 : « recueillir » exige --fin (end_turn, max_tokens ou refusal), lue sur la fin de la session ; elle est versée et
  rendue telle quelle au moteur (TRONQUE, REFUS jugés par le moteur) ;
- erreurs de scellement et de recueil converties en arrêt nommé (code 1), sans trace ; ecrire_scelle vérifie le sceau
  d'un fichier déjà présent et refuse un sceau orphelin avant d'écrire ;
- essaim : parts « bloquantes » et reserver_finales refusés (un coût Claude nul changerait les sauts).

En-tête de la v1 :
Voie « abonnement » des cellules Claude (v1) : enveloppe des moteurs scellés, sans les modifier.

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

VERSION = "voie-abonnement-v6"
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
EFFORTS_SESSION = ("max", "xhigh", "high")  # v5 ; v6 : high
CODE_USAGE, CODE_PORTE = 1, 2
FINS_SESSION = ("end_turn", "max_tokens", "refusal")


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
    sceau = Path(str(chemin) + ".sha256")
    if chemin.exists():
        if lire_scelle(chemin) != texte:
            raise ValueError(f"{chemin} existe avec un autre contenu ; rien n'est écrasé")
        return empreinte(texte)
    if sceau.exists():
        raise ValueError(f"{sceau} existe sans son fichier ; rien n'est écrit")
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
    if not Path(str(chemin) + ".sha256").exists():
        raise ValueError(f"{chemin} : sceau .sha256 absent")
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

    def __init__(self, v, branche, effort):
        if effort not in EFFORTS_SESSION:  # v5
            raise ValueError(f"effort {effort!r} hors de {EFFORTS_SESSION}")
        self.v, self.branche, self.kits, self.effort = v, branche, set(), effort
        self.original = v.executer_cellule
        v.COMPTEURS.pop("anthropic", None)  # aucun comptage sur la clé : estimation du moteur
        v.executer_cellule = self.executer

    def executer(self, dossier, tour, lettre, prompt, pieces, plafond, appelants, repli_lot=False):
        v = self.v
        m = v.MODELES[lettre]
        if m["fournisseur"] != "anthropic":
            return self.original(dossier, tour, lettre, prompt, pieces, plafond, appelants, repli_lot)
        cid = v.id_cellule(tour, lettre)
        jouees = sorted({e["cellule"] for e in v.essais_journal(dossier)
                         if str(e.get("modele_demande", "")).startswith("claude-") and e.get("id_reponse") != "abonnement"})
        if jouees:  # v2 (B2) : sur tout le dossier
            raise v.Arret(CODE_USAGE, f"{cid} : dossier où des cellules d'Anthropic ont été jouées par l'interface "
                                      f"({jouees}) ; deux voies ne se mêlent pas ; rien n'est fait")
        try:  # v3 : le filet ne couvre que le kit et le recueil
            lecteur = self._preparer(dossier, cid, m, prompt, plafond)
        except (ValueError, OSError, KeyError, json.JSONDecodeError) as e:  # v2 : arrêt nommé, jamais une trace
            raise v.Arret(CODE_USAGE, f"{cid} : voie abonnement : {type(e).__name__} : {e} ; rien n'est fait")
        if lecteur is None:
            return "KIT"
        return self.original(dossier, tour, lettre, prompt, pieces, plafond, dict(appelants, anthropic=lecteur),
                             repli_lot)

    def garder_avant_kit(self, dossier, cid, m, prompt, plafond):
        """v2 (B1) : gardes du moteur faites avant que le texte ne sorte vers une session : motifs, puis plafond et
        ligne sur le pire cas au plafond de relance (estimation des jetons, aucun comptage sur la clé)."""
        v = self.v
        v.garder_motifs(dossier, cid, prompt)
        compte = v.compter_entree(m, prompt)
        pire = max(v.cout_pire_garde(m, compte["garde"], t) for t in (m["max"], m["max_relance"]))
        if v.depense(dossier) + pire > plafond:
            v.refuser_avant_envoi(dossier, cid, "PLAFOND", f"dépense {v.depense(dossier):.2f} + pire cas {pire:.2f} USD "
                                                           f"> plafond {plafond:.2f} USD ; aucun kit écrit",
                                  v.CODE_PLAFOND)
        ligne = v.ligne_courante(dossier)
        if ligne and v.depense_ligne(dossier, ligne) + pire > ligne["montant"]:
            v.refuser_avant_envoi(dossier, cid, "LIGNE", f"dépense sur la ligne {v.depense_ligne(dossier, ligne):.2f} + "
                                                         f"pire cas {pire:.2f} USD > ligne {ligne['montant']:.2f} USD ; "
                                                         f"aucun kit écrit", v.CODE_PLAFOND)

    def _preparer(self, dossier, cid, m, prompt, plafond):
        """Écrit le kit et rend None, ou rend le lecteur de la réponse recueillie (servie une seule fois)."""
        v = self.v
        h = empreinte(prompt)
        kit = rep_abonnement(dossier) / "kits" / cid
        r = recueil(dossier, cid)
        if r is None:
            self.garder_avant_kit(dossier, cid, m, prompt, plafond)
            ecrire_scelle(kit / "texte-servi.md", prompt)
            fiche = {"cellule": cid, "modele": m["id"], "espece": m["espece"], "effort": self.effort,
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
            return None
        fiche, texte = r
        if fiche["sha256_texte_servi"] != h:
            raise v.Arret(CODE_USAGE, f"{cid} : réponse recueillie pour un autre texte servi "
                                      f"({fiche['sha256_texte_servi']} ≠ {h}) ; rien n'est fait")
        if fiche["modele_demande"] != m["id"]:
            raise v.Arret(CODE_USAGE, f"{cid} : fiche de recueil pour {fiche['modele_demande']}, espèce {m['id']}")
        v.ajouter_journal(dossier, {"voie_abonnement": cid, "session": fiche["session"],
                                    "modele_servi_session": fiche["modele_servi"], "effort_session": fiche["effort"],
                                    "fin_session": fiche["fin"],
                                    "sha256_texte_servi": h, "sha256_reponse": fiche["sha256_reponse"],
                                    "usage": "non mesuré (abonnement) ; coût d'interface zéro", "quand": maintenant(),
                                    "programme": VERSION})

        servie = []

        def lecteur(m2, prompt2, max_tokens):
            if servie:  # v3 : une seule lecture ; aucune relance ni aucun rejeu fictif au journal
                return v.Reponse(echec="relance impossible par la voie abonnement : la session a rendu sa réponse "
                                       "une fois ; un nouveau kit (nouveau dossier ou décision de l'arbitre) est nécessaire",
                                 identifiant="abonnement", modele_servi=fiche["modele_servi"])  # v4
            servie.append(1)
            if empreinte(prompt2) != h:
                return v.Reponse(echec="texte servi changé entre le recueil et la lecture", identifiant="abonnement")
            return v.Reponse(texte=texte, modele_servi=fiche["modele_servi"], identifiant="abonnement",
                             fin=fiche["fin"], usage={"entree": 0, "sortie": 0}, usage_lu=True)  # v2 (B3)

        return lecteur


def refuser_anthropic(m, prompt, max_tokens):
    raise AssertionError("voie abonnement : aucun appel direct à Anthropic")


def lancer_moteur(nom, branche, argv, v=None, appelants=None, effort=None):
    v = v or charger(*MOTEURS[nom], f"moteur_{nom}_voie_abonnement")
    voie = Voie(v, branche, effort)
    code = v.principal(argv, appelants=dict(appelants or v.APPELANTS, anthropic=refuser_anthropic))
    if voie.kits:
        print(f"KITS EN ATTENTE ({len(voie.kits)}) : {sorted(voie.kits)}", flush=True)
    return code


def configuration_de(argv):
    for i, x in enumerate(argv):
        if x == "--configuration" and i + 1 < len(argv):
            return argv[i + 1]
        if x.startswith("--configuration="):
            return x.split("=", 1)[1]
    return None


def ecart_configuration(cfg):
    if cfg.get("ordre") != "simultane":
        return f"ordre {cfg.get('ordre')!r} : la voie abonnement n'admet que « simultane »"
    if cfg.get("parts") != "non_bloquantes" or cfg.get("reserver_finales", False):  # v2
        return (f"parts {cfg.get('parts')!r}, reserver_finales {cfg.get('reserver_finales')!r} : la voie abonnement "
                f"n'admet que des parts non bloquantes sans réserve des finales (un coût Claude nul changerait les sauts)")
    return None


def lancer_essaim(branche, argv, v=None, mod=None, appelants=None, effort=None):
    mod = mod or charger(*ESSAIM, "essaim_v7_voie_abonnement")
    v = v or mod.charger_moteur()
    voie = Voie(v, branche, effort)
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
        if ecart_configuration(cfg):  # v3 : contrôlé aussi ici (configuration relue du dossier)
            raise v.Arret(CODE_USAGE, ecart_configuration(cfg))
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
    chemin_cfg = configuration_de(argv)
    if argv[:1] == ["lancer"] and chemin_cfg:  # v3 : refus avant toute écriture ; v4 : forme --configuration=F
        try:
            cfg = json.loads(Path(chemin_cfg).read_text(encoding="utf-8"))
            ecart = ecart_configuration(cfg) if isinstance(cfg, dict) else "configuration qui n'est pas un objet JSON"
        except (OSError, ValueError) as e:
            ecart = f"configuration illisible ({type(e).__name__} : {e})"
        if ecart:
            print(f"ARRÊT (code {CODE_USAGE}) : {ecart} ; rien n'est écrit", file=sys.stderr, flush=True)
            return CODE_USAGE
    code = mod.principal(argv, appelants=dict(appelants or v.APPELANTS, anthropic=refuser_anthropic), v=v)
    if voie.kits:
        print(f"KITS EN ATTENTE ({len(voie.kits)}) : {sorted(voie.kits)}", flush=True)
    return code


def recueillir(dossier, cid, chemin_texte, session, modele_servi, fin):
    """Verse la réponse finale d'une session fille (texte lu par les événements de la session, enregistré tel quel)."""
    kit = rep_abonnement(dossier) / "kits" / cid
    fiche_kit = json.loads(lire_scelle(kit / "fiche.json"))
    servi = lire_scelle(kit / "texte-servi.md")
    if empreinte(servi) != fiche_kit["sha256_texte_servi"]:
        raise SystemExit(f"ARRÊT : {cid} : texte servi différent de sa fiche")
    if not (modele_servi == fiche_kit["modele"] or modele_servi.startswith(fiche_kit["modele"] + "-")):
        raise SystemExit(f"ARRÊT : {cid} : modèle servi {modele_servi!r} au lieu de {fiche_kit['modele']!r} ; "
                         f"défaut de la cellule, rien n'est versé")
    if fin not in FINS_SESSION:  # v2 (B3)
        raise SystemExit(f"ARRÊT : {cid} : fin {fin!r} hors de {FINS_SESSION} ; rien n'est versé")
    texte = Path(chemin_texte).read_text(encoding="utf-8")
    if not texte.strip() and fin != "refusal":  # v3 : un vide coupé ne se verse pas (le moteur y ferait un rejeu)
        raise SystemExit(f"ARRÊT : {cid} : réponse vide ; défaut de la cellule, rien n'est versé")
    rep = rep_abonnement(dossier) / "reponses"
    h = ecrire_scelle(rep / f"{cid}.md", texte)
    fiche = {"cellule": cid, "voie": "abonnement", "session": session, "modele_demande": fiche_kit["modele"],
             "modele_servi": modele_servi, "effort": fiche_kit["effort"], "fin": fin,
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
        s.add_argument("--effort", required=True, choices=EFFORTS_SESSION,
                       help="effort de la session fille (max : texte décisif ou juge de dernier recours ; xhigh : rédaction importante ; high : cellule de collisionneur, relecture, avis)")
        s.add_argument("reste", nargs=argparse.REMAINDER)
    r = sous.add_parser("recueillir")
    r.add_argument("dossier")
    r.add_argument("cellule")
    r.add_argument("--texte", required=True)
    r.add_argument("--session", required=True)
    r.add_argument("--modele-servi", required=True)
    r.add_argument("--fin", required=True, choices=FINS_SESSION, help="raison d'arrêt lue sur la fin de la session")
    k = sous.add_parser("kits")
    k.add_argument("dossier")
    a = p.parse_args(argv)
    if a.commande in ("v8m", "v8p", "essaim"):
        reste = a.reste[1:] if a.reste[:1] == ["--"] else a.reste
        return (lancer_essaim(a.branche, reste, effort=a.effort) if a.commande == "essaim"
                else lancer_moteur(a.commande, a.branche, reste, effort=a.effort))
    if a.commande == "recueillir":
        try:
            return recueillir(a.dossier, a.cellule, a.texte, a.session, a.modele_servi, a.fin)
        except (ValueError, OSError) as e:
            print(f"ARRÊT (code {CODE_USAGE}) : {e}", file=sys.stderr)
            return CODE_USAGE
    try:
        return kits_en_attente(a.dossier)
    except (ValueError, OSError) as e:
        print(f"ARRÊT (code {CODE_USAGE}) : {e}", file=sys.stderr)
        return CODE_USAGE


if __name__ == "__main__":
    sys.exit(principal())
