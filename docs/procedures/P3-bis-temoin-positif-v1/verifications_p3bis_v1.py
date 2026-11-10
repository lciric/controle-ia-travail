"""Vérifications communes de la chaîne de session de P3-bis (témoin positif planté ; GO-2026-11-02-29), v1.

Texte qui fait foi : `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon9.md` (`eb65773f…`),
« Liste d'arrêt », « Devis », « Plan d'analyse » points 1, 3, 4, 6, 11, « Ce que le code et la chaîne doivent changer »
point 6 ; contre-lecture du code `brouillons/P3-bis-temoin-positif-v1/contre-lecture-code-p3bis-v1.md` (`7a074ad1…`),
point 6. Un seul texte, lu à l'identique par le lanceur, les contrôles avant dépense, la surveillance, le contrôle à cinq
minutes, la récupération, la destruction et le scellement. Décliné de `docs/procedures/P3-premier-test-v2/
verifications_p3_v1.py` (P3) sous un nom neuf (R12). Bibliothèque standard seulement (lancé par `python3 -I`, hors du
dépôt). Aucun appel externe : ce module lit des fichiers et l'entrée standard, il n'appelle jamais l'outil de location.

Sous-commandes (code 0 si conforme ; 1 avec le motif sur la dernière ligne sinon ; 2 sur un usage faux ; 3 pour les
refus « d'attente » : aucune offre conforme, crédit insuffisant, dépense au plafond) :

  go PREREG GO_MD JOUR
      GO cité par le texte (ligne « - GO : **GO-…** » et `GO_ID=…` de la ligne « Lancement ») égal à GO_CALCUL ; une seule
      ligne de ce GO au registre, à huit colonnes, type « calcul », accordée par Lazar, plafond « 80 USD », échéance
      2026-11-16 ; JOUR (AAAA-MM-JJ, UTC) entre l'octroi et DATE_LIMITE_CREATION ; aucune ligne de type « révocation »
      qui nomme GO_CALCUL dans son périmètre ou sa référence (forme exacte du texte) ; toute ligne « | GO-… » à un autre
      nombre de colonnes que huit refuse le registre (comme la garde de calcul). La ligne d'accord du jour de P3 n'existe
      plus : DB-5 (a), le GO en tient lieu.
  instances TOLEREES EN_MARCHE GO_MD JOURNAL         (entrée : réponse de « show instances --raw »)
      chaque instance du compte : arrêtée et inscrite dans TOLEREES (constante ARRETEES_TOLEREES du lanceur), ou en marche
      et nommée dans EN_MARCHE (« ID:GO-…,ID:GO-… » ou « - ») avec un GO de calcul accordé par Lazar et non révoqué ;
      toute autre : refus ; une instance nommée absente du compte : refus (liste fermée fausse). Écrit la somme des prix
      des instances nommées.
  offres BRUT SORTIE JOURNAL RELUES REPLI
      filtre du point 11 du plan sur la réponse de « search offers » ; REPLI 0 : processeur CPU_EXIGE exigé ; REPLI 1 :
      condition du processeur retirée (seule), tout le reste gardé. La moins chère des offres conformes (à prix égal, le
      plus petit identifiant) est écrite dans SORTIE ; écrit « identifiant prix ». Code 3 : aucune offre conforme.
  credit SOMME_EN_MARCHE                             (entrée : réponse de « show user --raw »)
      crédit ≥ CREDIT_FIXE_USD + HEURES_CREDIT_AUTRES × somme des prix des instances nommées en marche. Code 3 sinon.
  identifiant ID LANCEMENT
      ID est l'identifiant de l'instance créée par ce lanceur (seule ligne « instance <id> » de LANCEMENT) et n'est pas
      dans ARRETEES_TOLEREES : seule cible permise d'un arrêt ou d'une destruction (R10).
  etat                                               (entrée : réponse de « show instance <id> --raw »)
      écrit « actual_status=… cur_state=… intended_status=… status_msg=… » ou « illisible: … ».
  motif JOURNAL PROGRES
      motif de fin lu dans le dernier journal de l'instance et le relevé cumulatif : « GARDER », « PROCESSUS MORT »,
      « FIN », « ÉCHEC D'AMORCE », « REDÉMARRAGE » ou « AUCUN », puis une tabulation et le détail.
  depense CREATION MAINTENANT DPH_OFFRE ANTERIEURE INTERVALLE   (entrée : réponse de « show instance <id> --raw »)
      dépense cumulée de la course : ANTERIEURE (tentatives et relances précédentes, USD) + prix × durée depuis la
      création (le plus haut du prix relu et de celui de l'offre ; PRIX_MAX si le prix relu est illisible, écrit) +
      téléchargement relevé (MAJORANT_TELECHARGEMENT_USD si illisible, écrit). Code 3 si la dépense projetée au prochain
      relevé atteint PLAFOND_USD.
  valeurs PREREG
      valeurs de P3-bis citées par le texte (bloc des valeurs, point 6 (iv) du code ; texte aux espaces réduites, sans
      gras).
  constantes DOSSIER
      constantes des scripts de la chaîne (dans DOSSIER) égales à celles de ce module, une ligne chacune.
  config CFG CFG_P3 CONSIGNES
      configuration de P3-bis : seuls écarts à celle de P3 ceux du texte (chemin et empreinte des consignes, deux durées à
      null, 30 fils d'entraînement), empreinte des consignes égale à celle du fichier, mode « reel ».
  longueurs MESURE ATTENDUES
      longueurs en jetons mesurées (JSON écrit par le bloc du tokeniseur des contrôles) : A et T égaux tâche par tâche
      sur les quatre mesures ; résumé égal aux longueurs attendues (JSON épinglé au candidat).
  preuves DOSSIER [JOURNAL …]
      journaux des bancs et des répétitions : verdict sur la dernière ligne, aucune ligne d'échec, lignes « script éprouvé »
      bien formées et exactement les scripts attendus ; écrit « <script> <sha256> » par script éprouvé.
"""
from __future__ import annotations

import json
import math
import re
import sys
from datetime import date

# --- GO, dates et bornes du texte (brouillon 9 : en-tête « GO », « Liste d'arrêt », plan, point 11, « Devis ») ------
GO_CALCUL = "GO-2026-11-02-29"           # seul GO accepté (texte, en-tête ; liste d'arrêt)
OCTROI_GO = "2026-11-02"
PLAFOND_GO = "80 USD"                    # colonne « plafond » du registre
ECHEANCE_GO = "2026-11-16"               # colonne « échéance » du registre
DATE_LIMITE_CREATION = "2026-11-16"      # « création au plus tard le 16 novembre 2026 » (constante)
PRIX_MAX = 2.10                          # USD de l'heure
FIABILITE_MIN = 0.98
STOCKAGE_MAX = 0.08                      # USD de l'heure
TELECHARGEMENT_MAX = 0.05                # USD par Go
COEURS_MIN = 30                          # cœurs effectifs
MEMOIRE_VIVE_MIN_MO = 128000
DISQUE_MIN_GO = 80
CARTE = "A100 SXM4"
CARTE_RAM_MIN_MO = 79000                 # « 80 Go » (79 000 Mo, comme le filtre de P3)
CUDA_MIN = 13.0
CPU_EXIGE = "AMD EPYC 7513 32-Core Processor"
ESSAIS_AVANT_REPLI = 12                  # « douze essais à 15 minutes d'intervalle »
INTERVALLE_OFFRE_S = 900
CREDIT_FIXE_USD = 20.0                   # « ≥ 20 USD plus 10 heures du prix des instances nommées en marche »
HEURES_CREDIT_AUTRES = 10
PLAFOND_USD = 80.0                       # dépense cumulée de la course, toutes tentatives et relances comprises
MAJORANT_TELECHARGEMENT_USD = 2.0        # devis : « ≤ 2,0 USD à 0,05 USD/Go » ; pris si le relevé est illisible
ALERTE_SANS_PROGRES_S = 7200             # « l'absence de ligne PROGRES pendant deux heures donne une alerte »
ARRETEES_TOLEREES = ("58936096", "58936099", "58936100")   # constante du lanceur (consigne du lanceur, 2026-11-10)
DEPOT_URL = "https://github.com/lciric/controle-ia-travail.git"
MOTIF_GO = r"GO-\d{4}-\d{2}-\d{2}-\d{2}"
# --- lignes du journal de l'instance (scripts de l'instance, noms v2 ; dépendance déclarée au rapport) ---------------
MOTIF_AMORCE_DEBUT = re.compile(r"^AMORCE \d{4}-\d{2}-\d{2}T\S* : commit [0-9a-f]{40}$")
MOTIF_AMORCE_FIN = re.compile(r"^AMORCE \S+ : fin, code (\d+)$")
MOTIF_AMORCE_ECHEC = re.compile(r"^AMORCE : ")
MOTIF_RUN_FINI = re.compile(r"(?:^|\s)run : processus (\d+) fini, code (\d+)$")
MOTIF_RUN_COMPLET = "résumé écrit sans arrêt consigné : run complet"
MOTIF_SECOND_PAQUET_ECHEC = "SECOND PAQUET EN ÉCHEC"
CODE_SECOND_PAQUET = 5                   # code de sortie de p3bis_instance_v2.sh quand le second paquet échoue
MOTIF_PROGRES = re.compile(r"^PROGRES [0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z( [a-z_]+=[^ ]+)+$")


def lire(chemin: str) -> str:
    try:
        return open(chemin, encoding="utf-8").read()
    except OSError:
        raise SystemExit(f"fichier {chemin} absent ou illisible") from None


def cellules(ligne: str) -> list[str]:
    return [x.strip() for x in ligne.strip().strip("|").split("|")]


def nombre(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)


def entier(v) -> bool:
    return isinstance(v, int) and not isinstance(v, bool)


def jour_iso(j: str) -> date:
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", j or ""):
        raise SystemExit(f"jour « {str(j)[:20]} » mal formé : AAAA-MM-JJ attendu")
    try:
        return date.fromisoformat(j)
    except ValueError:
        raise SystemExit(f"jour « {j} » impossible") from None


def nomme(identifiant: str, cellule: str) -> bool:
    """Identifiant entier (ni préfixe ni suffixe d'un autre identifiant) cité dans la cellule."""
    return re.search(rf"(?<![\w-]){re.escape(identifiant)}(?![\w-])", cellule) is not None


def lignes_go(go_t: str) -> list[list[str]]:
    sortie = []
    for n, ligne in enumerate(go_t.split("\n"), 1):
        if not re.match(rf"^\|\s*{MOTIF_GO}\s*\|", ligne):
            continue
        c = cellules(ligne)
        if len(c) != 8:
            raise SystemExit(f"registre des GO mal formé ligne {n} : 8 colonnes attendues, {len(c)} trouvées")
        sortie.append(c)
    return sortie


def revocations(registre: list[list[str]], g: str) -> list[str]:
    return [c[0] for c in registre if c[2] == "révocation" and (nomme(g, c[3]) or nomme(g, c[7]))]


# ================================================================================================= GO
def go(prereg: str, go_md: str, jour: str) -> str:
    texte, go_t = lire(prereg), lire(go_md)
    j = jour_iso(jour)
    m = re.findall(rf"^- GO : \*\*({MOTIF_GO})\*\*", texte, re.M)
    if len(m) != 1 or len(re.findall(r"^- GO :", texte, re.M)) != 1:
        raise SystemExit("ligne « - GO : **GO-…** » absente, en double ou mal formée dans le texte")
    g = m[0]
    if g != GO_CALCUL:
        raise SystemExit(f"{g} : seul {GO_CALCUL} est accepté pour P3-bis")
    lanc = [x for x in texte.split("\n") if x.startswith("- Lancement : ")]
    if len(lanc) != 1:
        raise SystemExit("ligne « - Lancement : » absente ou en double dans le texte")
    cites = re.findall(rf"`GO_ID=({MOTIF_GO})`", lanc[0])
    if cites != [GO_CALCUL] or set(re.findall(MOTIF_GO, lanc[0])) != {GO_CALCUL}:
        raise SystemExit(f"ligne « Lancement » : GO_ID {cites} ; `GO_ID={GO_CALCUL}` seul attendu")
    registre = lignes_go(go_t)
    c = [x for x in registre if x[0] == g]
    if len(c) != 1:
        raise SystemExit(f"{g} absent ou en double au registre des GO")
    ident, accorde, typ, _, plafond, echeance, par, _ = c[0]
    if typ != "calcul" or par != "Lazar":
        raise SystemExit(f"{g} : {typ}, {par} : GO de type « calcul », accordé par Lazar, attendu")
    if plafond != PLAFOND_GO or echeance != ECHEANCE_GO or accorde != OCTROI_GO:
        raise SystemExit(f"{g} : octroi {accorde}, plafond {plafond}, échéance {echeance} ; "
                         f"{OCTROI_GO}, {PLAFOND_GO}, {ECHEANCE_GO} attendus (ligne réécrite ?)")
    if not (jour_iso(accorde) <= j <= jour_iso(echeance)):
        raise SystemExit(f"jour {jour} hors de la validité de {g} ({accorde} → {echeance})")
    if j > jour_iso(DATE_LIMITE_CREATION):
        raise SystemExit(f"jour {jour} après le {DATE_LIMITE_CREATION} : aucune création (ligne de GO neuve, nœud)")
    r = revocations(registre, g)
    if r:
        raise SystemExit(f"{g} révoqué au registre des GO ({', '.join(r)})")
    return f"{g} conforme (jour {jour}, au plus tard le {DATE_LIMITE_CREATION} ; aucune révocation)"


# ================================================================================================= instances
def instances(tolerees: str, en_marche: str, go_md: str, journal: str, entree: str) -> str:
    tol = set(tolerees.split())
    if not tol or any(not re.fullmatch(r"[0-9]{6,10}", x) for x in tol):
        raise SystemExit("instances tolérées non épinglées ou mal formées")
    nommees: dict[str, str] = {}
    if en_marche != "-":
        for x in en_marche.split(","):
            m = re.fullmatch(rf"([0-9]{{6,10}}):({MOTIF_GO})", x)
            if not m or m.group(1) in nommees:
                raise SystemExit(f"instances en marche : « ID:GO-…,ID:GO-… » ou « - » attendu ({x[:40]})")
            nommees[m.group(1)] = m.group(2)
    if tol & set(nommees):
        raise SystemExit(f"instance(s) à la fois tolérée(s) arrêtée(s) et nommée(s) en marche : {sorted(tol & set(nommees))}")
    registre = lignes_go(lire(go_md))
    for ident, g in nommees.items():
        c = [x for x in registre if x[0] == g]
        if len(c) != 1 or c[0][2] != "calcul" or c[0][6] != "Lazar":
            raise SystemExit(f"instance {ident} : {g} absent, en double, ou pas un GO de calcul accordé par Lazar")
        if revocations(registre, g):
            raise SystemExit(f"instance {ident} : {g} révoqué")
    try:
        liste = json.loads(entree)
        assert isinstance(liste, list)
    except Exception:
        raise SystemExit("show instances : réponse illisible ou commande en échec") from None
    vues, marche, refusees, trouvees, somme = [], [], [], set(), 0.0
    for i in liste:
        if not isinstance(i, dict):
            refusees.append("entrée illisible")
            continue
        ident, etat, cur = str(i.get("id")), i.get("actual_status"), i.get("cur_state")
        arretee = etat in ("exited", "stopped") and cur == "stopped"
        trouvees.add(ident)
        if ident in tol:
            (vues if arretee else refusees).append(f"{ident} ({etat}, {cur}){'' if arretee else ' : tolérée seulement arrêtée'}")
        elif ident in nommees:
            dph = i.get("dph_total")
            if arretee:
                refusees.append(f"{ident} ({etat}, {cur}) : nommée en marche mais arrêtée")
            elif not nombre(dph) or dph < 0:
                refusees.append(f"{ident} (prix illisible)")
            else:
                somme += float(dph)
                marche.append(f"{ident} ({etat}, {cur}, {float(dph):.3f} USD/h, {nommees[ident]})")
        else:
            refusees.append(f"{ident} ({etat}, {cur})")
    absentes = sorted(set(nommees) - trouvees)
    if absentes:
        refusees.append("nommées en marche mais absentes du compte : " + ", ".join(absentes))
    lignes = ["instances arrêtées tolérées (ARRETEES_TOLEREES) : " + (", ".join(vues) or "aucune"),
              "instances en marche nommées avec leur GO : " + (", ".join(marche) or "aucune")]
    if refusees:
        lignes.append("instances non tolérées : " + ", ".join(refusees))
    with open(journal, "a", encoding="utf-8") as f:
        for x in lignes:
            f.write(x + "\n")
    for x in lignes:
        print(x, file=sys.stderr)
    if refusees:
        raise SystemExit("instance(s) non tolérée(s) sur le compte : aucune création")
    return f"{somme:.4f}"


# ================================================================================================= offres
def conforme(o: dict, repli: bool) -> bool:
    fiab = o.get("reliability2", o.get("reliability"))
    p = o.get("dph_total")
    return (entier(o.get("id")) and o.get("gpu_name") == CARTE
            and nombre(o.get("gpu_ram")) and o["gpu_ram"] >= CARTE_RAM_MIN_MO
            and entier(o.get("num_gpus")) and o["num_gpus"] == 1
            and (repli or o.get("cpu_name") == CPU_EXIGE)
            and nombre(o.get("cpu_cores_effective")) and o["cpu_cores_effective"] >= COEURS_MIN
            and nombre(o.get("cpu_ram")) and o["cpu_ram"] >= MEMOIRE_VIVE_MIN_MO
            and nombre(o.get("disk_space")) and o["disk_space"] >= DISQUE_MIN_GO
            and nombre(o.get("cuda_max_good")) and o["cuda_max_good"] >= CUDA_MIN
            and nombre(fiab) and fiab >= FIABILITE_MIN
            and nombre(o.get("inet_down_cost")) and 0 <= o["inet_down_cost"] <= TELECHARGEMENT_MAX
            and nombre(o.get("storage_total_cost")) and 0 <= o["storage_total_cost"] <= STOCKAGE_MAX
            and nombre(p) and 0 < p <= PRIX_MAX)


def offres(brut: str, sortie: str, journal: str, relues: str, repli: str) -> str:
    if repli not in ("0", "1"):
        raise SystemExit("REPLI : 0 (processeur exigé) ou 1 (repli écrit)")
    try:
        liste = json.loads(lire(brut))
    except ValueError:
        print("offres : réponse illisible", file=sys.stderr)
        sys.exit(2)
    if not isinstance(liste, list):
        print("offres : liste attendue", file=sys.stderr)
        sys.exit(2)
    extrait = ("id", "machine_id", "host_id", "gpu_name", "gpu_ram", "num_gpus", "cpu_name", "cpu_cores_effective",
               "cpu_ram", "disk_space", "cuda_max_good", "reliability2", "reliability", "dph_total", "inet_down_cost",
               "storage_total_cost", "end_date")
    with open(relues, "w", encoding="utf-8") as f:
        json.dump([{k: o.get(k) for k in extrait} if isinstance(o, dict) else {"illisible": type(o).__name__}
                   for o in liste], f, indent=1)
    vus = [repr(o.get("id")) for o in liste if isinstance(o, dict)]
    if len(vus) != len(set(vus)):
        print("offres : identifiant en double dans la réponse (ambiguë) : pas de création", file=sys.stderr)
        sys.exit(2)
    bons = sorted((o for o in liste if isinstance(o, dict) and conforme(o, repli == "1")),
                  key=lambda o: (float(o["dph_total"]), o["id"]))
    with open(journal, "a", encoding="utf-8") as j:
        j.write(f"offres conformes relues ({'repli écrit : condition du processeur retirée' if repli == '1' else 'processeur ' + CPU_EXIGE + ' exigé'}) : "
                + (", ".join(f"{o['id']} ({float(o['dph_total']):.4f} USD/h ; machine {o.get('machine_id')} ; hôte "
                             f"{o.get('host_id')} ; processeur {o.get('cpu_name')} ; cœurs effectifs "
                             f"{o.get('cpu_cores_effective')} ; mémoire vive {o.get('cpu_ram')} Mo ; fiabilité "
                             f"{o.get('reliability2', o.get('reliability'))} ; téléchargement {o.get('inet_down_cost')} "
                             f"USD/Go ; stockage {o.get('storage_total_cost')} USD/h)" for o in bons) or "aucune") + "\n")
    if not bons:
        print(f"aucune offre conforme au filtre du plan, point 11 (au plus {PRIX_MAX} USD/h, fiabilité ≥ {FIABILITE_MIN}, "
              f"≥ {COEURS_MIN} cœurs effectifs, {MEMOIRE_VIVE_MIN_MO} Mo, disque ≥ {DISQUE_MIN_GO} Go, stockage au plus "
              f"{STOCKAGE_MAX} USD/h, téléchargement au plus {TELECHARGEMENT_MAX} USD/Go"
              + ("" if repli == "1" else f", processeur {CPU_EXIGE}") + ")", file=sys.stderr)
        sys.exit(3)
    o = bons[0]
    champs = ("id", "machine_id", "host_id", "gpu_name", "gpu_ram", "num_gpus", "cuda_max_good", "driver_version",
              "cpu_name", "cpu_arch", "cpu_cores", "cpu_cores_effective", "cpu_ram", "disk_space", "reliability2",
              "reliability", "verification", "hosting_type", "rentable", "end_date", "dph_total", "storage_total_cost",
              "inet_down_cost", "inet_up_cost", "geolocation")
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump({k: o.get(k) for k in champs}, f, indent=1)
    return f"{o['id']} {float(o['dph_total'])}"


# ================================================================================================= crédit
def credit(somme: str, entree: str) -> str:
    try:
        s = float(somme)
        assert math.isfinite(s) and s >= 0
    except (ValueError, AssertionError):
        raise SystemExit(f"somme des instances en marche illisible ({somme[:20]})") from None
    try:
        c = json.loads(entree)["credit"]
    except Exception:
        print("crédit illisible (show user)")
        sys.exit(2)
    if not nombre(c):
        print("crédit illisible (show user)")
        sys.exit(2)
    m = round(CREDIT_FIXE_USD + HEURES_CREDIT_AUTRES * s, 2)
    print(f"crédit {c:.2f} USD ; minimum {m:.2f} USD ({CREDIT_FIXE_USD:g} USD plus {HEURES_CREDIT_AUTRES} h × "
          f"{s:.4f} USD/h des instances nommées en marche)")
    sys.exit(0 if round(c, 2) >= m else 3)


# ================================================================================================= identifiant (R10)
def identifiant(ident: str, lancement: str) -> str:
    if not re.fullmatch(r"[0-9]{6,10}", ident):
        raise SystemExit(f"identifiant d'instance « {ident[:20]} » mal formé")
    if ident in ARRETEES_TOLEREES:
        raise SystemExit(f"instance {ident} : dans ARRETEES_TOLEREES ; jamais touchée par cette chaîne")
    vus = re.findall(r"^instance ([0-9]+)$", lire(lancement), re.M)
    if len(vus) != 1:
        raise SystemExit("traces du lancement : aucune ou plusieurs lignes « instance <id> » (création douteuse ?)")
    if vus[0] != ident:
        raise SystemExit(f"instance {ident} : ce lanceur a créé {vus[0]} ; aucune autre n'est arrêtée ni détruite ici")
    return f"instance {ident} : créée par ce lanceur, hors des instances tolérées"


def etat(entree: str) -> str:
    try:
        d = json.loads(entree)
        assert isinstance(d, dict)
    except Exception:
        return "illisible: " + entree[:120].replace("\n", " ")
    return " ".join(f"{k}={d.get(k)}" for k in ("actual_status", "cur_state", "intended_status", "status_msg"))


# ================================================================================================= motif de fin
def motif(journal: str, progres: str) -> str:
    j = lire(journal).split("\n") if journal != "-" else []
    p = lire(progres).split("\n")
    fins = [x for x in j if MOTIF_AMORCE_FIN.match(x)]
    echec_paquet = [x for x in j if MOTIF_SECOND_PAQUET_ECHEC in x]
    finis = [MOTIF_RUN_FINI.search(x) for x in j]
    finis = [f for f in finis if f]
    mort = [f for f in finis if f.group(2) != "0"] and not any(MOTIF_RUN_COMPLET in x for x in j)
    if fins:
        code = int(MOTIF_AMORCE_FIN.match(fins[0]).group(1))
        if code == CODE_SECOND_PAQUET or echec_paquet:
            return (f"GARDER\tfin, code {code} ; second paquet en échec : instance arrêtée par son identifiant, gardée, "
                    f"jamais détruite jusqu'au paquet refait (le run n'est pas rejoué)")
        if mort:
            f = [f for f in finis if f.group(2) != "0"][0]
            return (f"PROCESSUS MORT\tfin, code {code} ; run : processus {f.group(1)} fini, code {f.group(2)}, sans résumé "
                    f"écrit (erreur de chaîne si ni resume.json ni arret.json à la récupération)")
        return f"FIN\t{fins[0]}"
    echecs = [x for x in j if MOTIF_AMORCE_ECHEC.match(x)]
    if echecs:
        return f"ÉCHEC D'AMORCE\t{echecs[0][:200]}"
    if sum(1 for x in p if MOTIF_AMORCE_DEBUT.match(x)) > 1:
        return "REDÉMARRAGE\tl'amorce a été relancée par le conteneur"
    return "AUCUN\t-"


# ================================================================================================= dépense
def depense(creation: str, maintenant: str, dph_offre: str, anterieure: str, intervalle: str, entree: str) -> str:
    try:
        cr, mt, iv = int(creation), int(maintenant), int(intervalle)
        po, an = float(dph_offre), float(anterieure)
        assert cr > 0 and mt >= cr and iv >= 0 and math.isfinite(po) and 0 < po and math.isfinite(an) and an >= 0
    except (ValueError, AssertionError):
        raise SystemExit("dépense : arguments illisibles (création, maintenant, prix de l'offre, dépense antérieure, intervalle)") from None
    notes = []
    try:
        d = json.loads(entree)
        assert isinstance(d, dict)
    except Exception:
        d = {}
    pr = d.get("dph_total")
    if nombre(pr) and pr > 0:
        prix = max(float(pr), po)
    else:
        prix = max(PRIX_MAX, po)
        notes.append(f"prix relu illisible : {prix:.2f} USD/h pris (borne)")
    tel = None
    if all(nombre(d.get(k)) and d.get(k) >= 0 for k in ("inet_down_billed", "inet_down_cost")):
        tel = float(d["inet_down_billed"]) * float(d["inet_down_cost"])
        if all(nombre(d.get(k)) and d.get(k) >= 0 for k in ("inet_up_billed", "inet_up_cost")):
            tel += float(d["inet_up_billed"]) * float(d["inet_up_cost"])
    if tel is None:
        tel = MAJORANT_TELECHARGEMENT_USD
        notes.append(f"téléchargement non relevé : majorant {tel:.2f} USD pris")
    calcul = prix * (mt - cr) / 3600
    total = an + calcul + tel
    projete = total + prix * iv / 3600
    ligne = (f"dépense {total:.2f} USD (antérieure {an:.2f} ; calcul {calcul:.2f} à {prix:.4f} USD/h sur {mt - cr} s ; "
             f"téléchargement {tel:.2f}) ; projetée au prochain relevé {projete:.2f} USD ; plafond {PLAFOND_USD:g} USD"
             + ("" if not notes else " ; " + " ; ".join(notes)))
    print(ligne)
    sys.exit(3 if projete >= PLAFOND_USD else 0)


# ================================================================================================= valeurs et constantes
VALEURS_TEXTE = (
    "au plus 2,10 USD de l'heure", "fiabilité ≥ 0,98", "stockage au plus 0,08 USD de l'heure",
    "téléchargement au plus 0,05 USD par Go", "au moins 30 cœurs effectifs", "128 000 Mo de mémoire vive",
    "disque ≥ 80 Go", "processeur AMD EPYC 7513 exigé d'abord", "douze essais à 15 minutes d'intervalle",
    "plafond exactement 80 USD", "création au plus tard le 16 novembre 2026",
    "≥ 20 USD plus 10 heures du prix des instances nommées en marche",
    "l'absence de ligne `PROGRES` pendant deux heures donne une alerte",
    "`duree_max_s` et `budget_entrainement_s` à `null`", "aucun `timeout`", "16 783 360 octets",
    f"`DEPOT_URL={DEPOT_URL}`", f"`GO_ID={GO_CALCUL}`")

# (fichier de la chaîne, nom) → valeur exacte, une seule ligne « NOM=valeur » (suivie d'une espace, d'un commentaire ou
# de la fin de ligne)
CONSTANTES = {
    ("lancer_p3bis_v1.sh", "GO_CALCUL"): GO_CALCUL,
    ("lancer_p3bis_v1.sh", "DATE_LIMITE_CREATION"): DATE_LIMITE_CREATION,
    ("lancer_p3bis_v1.sh", "ESSAIS_AVANT_REPLI"): str(ESSAIS_AVANT_REPLI),
    ("lancer_p3bis_v1.sh", "INTERVALLE_OFFRE_S"): str(INTERVALLE_OFFRE_S),
    ("lancer_p3bis_v1.sh", "DEPOT_URL"): DEPOT_URL,
    ("lancer_p3bis_v1.sh", "ARRETEES_TOLEREES"): '"' + " ".join(ARRETEES_TOLEREES) + '"',
    ("lancer_p3bis_v1.sh", "FILTRE"): ('"gpu_name=A100_SXM4 gpu_ram>=79 num_gpus=1 cuda_vers>=13.0 verified=true '
                                       'datacenter=true reliability>=0.98 cpu_ram>=128 disk_space>=80 rentable=true"'),
    ("surveiller_p3bis_v1.sh", "ALERTE_SANS_PROGRES_S"): str(ALERTE_SANS_PROGRES_S),
    ("controle_cinq_minutes_p3bis_v1.sh", "PRIX_MAX"): f"{PRIX_MAX:.2f}",
    ("controles_avant_depense_p3bis_v1.sh", "DEPOT_URL"): DEPOT_URL,
    ("recuperation_p3bis_v1.sh", "DEPOT_URL"): DEPOT_URL,
}


def sans_gras(texte: str) -> str:
    return " ".join(texte.replace("**", "").split())


def valeurs(prereg: str) -> str:
    t = sans_gras(lire(prereg))
    manquantes = [v for v in VALEURS_TEXTE if v not in t]
    if manquantes:
        raise SystemExit(f"valeur(s) non citée(s) par le texte : {manquantes}")
    return f"{len(VALEURS_TEXTE)} valeurs de P3-bis citées par le texte"


def constantes(dossier: str) -> str:
    fautes = []
    for (fichier, nom), attendue in CONSTANTES.items():
        t = lire(f"{dossier}/{fichier}")
        vus = re.findall(rf"^{nom}=(\S+(?: \S+)*?)(?:\s+#.*)?$", t, re.M)
        vus = [v.rstrip() for v in vus]
        if vus != [attendue]:
            fautes.append(f"{fichier} {nom} : {vus} ≠ [{attendue}]")
    if fautes:
        raise SystemExit("constantes de la chaîne différentes de celles du module commun : " + " ; ".join(fautes))
    return f"{len(CONSTANTES)} constantes de la chaîne égales à celles du module commun"


# ================================================================================================= configuration
# texte, en-tête : « Écarts à la configuration de P3 (…), seuls écarts : chemin_consignes ; consignes_sha256 ; duree_max_s
# et budget_entrainement_s à null ; fils_entrainement à 30 »
ECARTS_CONFIG = {"chemin_consignes": "prereg/P3-bis-consignes-v1.md", "duree_max_s": None, "budget_entrainement_s": None,
                 "fils_entrainement": 30}


def config(cfg: str, cfg_p3: str, consignes: str) -> str:
    import hashlib
    try:
        c, p = json.loads(lire(cfg)), json.loads(lire(cfg_p3))
        assert isinstance(c, dict) and isinstance(p, dict)
    except (ValueError, AssertionError):
        raise SystemExit("configuration : JSON illisible ou pas un objet") from None
    absent = object()
    ecarts = sorted(k for k in set(c) | set(p) if c.get(k, absent) != p.get(k, absent))
    permis = set(ECARTS_CONFIG) | {"consignes_sha256"}
    hors = [k for k in ecarts if k not in permis]
    if hors:
        raise SystemExit(f"configuration : écarts à celle de P3 hors des écarts du texte : {hors}")
    for k, v in ECARTS_CONFIG.items():
        if k not in c or c[k] != v or (v is None and c[k] is not None) or (isinstance(v, int) and isinstance(c[k], bool)):
            raise SystemExit(f"configuration : {k} = {c.get(k, 'absent')!r} ; {v!r} attendu")
    try:
        sha = hashlib.sha256(open(consignes, "rb").read()).hexdigest()
    except OSError:
        raise SystemExit(f"consignes {consignes} absentes ou illisibles") from None
    if c.get("consignes_sha256") != sha:
        raise SystemExit(f"configuration : consignes_sha256 {str(c.get('consignes_sha256'))[:16]}… ≠ empreinte des consignes {sha[:16]}…")
    if c.get("mode") != "reel":
        raise SystemExit(f"configuration : mode {c.get('mode')!r} ; « reel » attendu")
    return f"configuration : seuls écarts à P3 ceux du texte ({', '.join(ecarts)}) ; consignes citées par leur empreinte"


# ================================================================================================= longueurs
MESURES =("consigne_seule", "indication_seule", "consigne_gabarit", "indication_gabarit")


def resume_longueurs(par_tache: list[dict]) -> dict:
    """par_tache : [{"tache": id, "<mesure>": {"saboteur": n, "temoin": n, "mention": n}, …}] → résumé (valeur : compte)."""
    r: dict = {}
    for m in MESURES:
        r[m] = {}
        for k in ("saboteur", "temoin", "mention"):
            c: dict[str, int] = {}
            for t in par_tache:
                v = str(t[m][k])
                c[v] = c.get(v, 0) + 1
            r[m][k] = dict(sorted(c.items()))
    return r


def comparer_longueurs(mesure: dict, attendues: dict) -> list[str]:
    fautes = []
    par_tache = mesure.get("par_tache")
    if not isinstance(par_tache, list) or not par_tache:
        return ["mesure sans tâche"]
    for t in par_tache:
        for m in MESURES:
            try:
                a, b = t[m]["saboteur"], t[m]["temoin"]
            except (KeyError, TypeError):
                fautes.append(f"{t.get('tache')} : mesure {m} absente")
                continue
            if not (entier(a) and entier(b) and a > 0 and b > 0):
                fautes.append(f"{t.get('tache')} : {m} illisible ou nulle")
            elif a != b:
                fautes.append(f"{t.get('tache')} : {m} A {a} ≠ T {b} (jeu décisif : aucun scellement, nœud)")
    if fautes:
        return fautes
    r = resume_longueurs(par_tache)
    if r != attendues:
        fautes.append(f"résumé des longueurs ≠ longueurs attendues épinglées : {json.dumps(r, sort_keys=True)[:300]}")
    return fautes


def longueurs(mesure: str, attendues: str) -> str:
    try:
        me, at = json.loads(lire(mesure)), json.loads(lire(attendues))
    except ValueError:
        raise SystemExit("longueurs : JSON illisible") from None
    f = comparer_longueurs(me, at)
    if f:
        raise SystemExit("longueurs : " + " ; ".join(f[:5]))
    return f"longueurs : A = T sur {len(me['par_tache'])} tâches et quatre mesures ; résumé égal aux longueurs attendues"


# ================================================================================================= preuves
JOURNAUX = {
    "banc-verifications-p3bis-v1.log": ("FIN DU BANC DU MODULE COMMUN DE P3-BIS ; cas non conformes : 0",
                                        {"verifications_p3bis_v1.py", "essais_verifications_p3bis_v1.py"}),
    "banc-lanceur-p3bis-v1.log": ("FIN DU BANC DU LANCEUR DE P3-BIS ; cas non conformes : 0",
                                  {"lancer_p3bis_v1.sh", "verifications_p3bis_v1.py", "essais_lanceur_p3bis_v1.sh"}),
    "banc-surveillance-p3bis-v1.log": ("FIN DU BANC DE LA SURVEILLANCE DE P3-BIS ; cas non conformes : 0",
                                       {"surveiller_p3bis_v1.sh", "controle_cinq_minutes_p3bis_v1.sh",
                                        "verifications_p3bis_v1.py", "essais_surveillance_p3bis_v1.sh"}),
    "banc-controles-p3bis-v1.log": ("FIN DU BANC DES CONTRÔLES DE P3-BIS ; cas non conformes : 0",
                                    {"controles_avant_depense_p3bis_v1.sh", "verifications_p3bis_v1.py",
                                     "essais_controles_p3bis_v1.sh"}),
    "banc-recuperation-p3bis-v1.log": ("FIN DU BANC DE LA RÉCUPÉRATION DE P3-BIS ; cas non conformes : 0",
                                       {"recuperation_p3bis_v1.sh", "detruire_p3bis_v1.sh", "verifications_p3bis_v1.py",
                                        "essais_recuperation_p3bis_v1.sh"}),
    "repetition-jouet-p3bis-v1.log": ("RÉPÉTITION JOUET DE LA CHAÎNE DE P3-BIS : CONFORME",
                                      {"lancer_p3bis_v1.sh", "controle_cinq_minutes_p3bis_v1.sh", "surveiller_p3bis_v1.sh",
                                       "recuperation_p3bis_v1.sh", "detruire_p3bis_v1.sh", "verifications_p3bis_v1.py",
                                       "repetition_jouet_p3bis_v1.sh"}),
    "repetition-finale-p3bis-v1.log": ("RÉPÉTITION FINALE DE P3-BIS : CONFORME",
                                       {"sceller_p3bis_v1.sh", "controles_avant_depense_p3bis_v1.sh",
                                        "verifications_p3bis_v1.py", "repetition_finale_p3bis_v1.sh"}),
}


def preuves(dossier: str, noms: list[str]) -> list[str]:
    noms = noms or list(JOURNAUX)
    inconnus = [n for n in noms if n not in JOURNAUX]
    if inconnus or len(set(noms)) != len(noms):
        raise SystemExit(f"journaux nommés inconnus ou en double : {noms}")
    vus: dict[str, str] = {}
    for nom in noms:
        verdict, attendus = JOURNAUX[nom]
        try:
            lignes = open(f"{dossier}/{nom}", encoding="utf-8").read().split("\n")
        except OSError:
            raise SystemExit(f"journal {nom} absent ou illisible") from None
        non_vides = [x for x in lignes if x.strip()]
        if not non_vides or non_vides[-1] != verdict:
            raise SystemExit(f"journal {nom} : dernière ligne ≠ « {verdict} »")
        fautes = [x for x in lignes if "NON CONFORME" in x or x.lstrip().startswith(("Traceback", "JETON AFFICHÉ"))]
        if fautes:
            raise SystemExit(f"journal {nom} : ligne d'échec avant le verdict : {fautes[0].strip()[:90]}")
        propres = set()
        for x in lignes:
            if x.startswith("script éprouvé : "):
                m = re.fullmatch(r"script éprouvé : ([a-z0-9_]+_v1\.(?:py|sh)) ([0-9a-f]{64})", x)
                if not m:
                    raise SystemExit(f"journal {nom} : ligne « script éprouvé » mal formée : {x[:90]}")
                if vus.setdefault(m.group(1), m.group(2)) != m.group(2):
                    raise SystemExit(f"{m.group(1)} éprouvé sous deux empreintes")
                propres.add(m.group(1))
        if propres != attendus:
            raise SystemExit(f"journal {nom} : scripts éprouvés ≠ attendus (manquants {sorted(attendus - propres)}, "
                             f"en trop {sorted(propres - attendus)})")
    return [f"{s} {vus[s]}" for s in sorted(vus)]


# ================================================================================================= ligne de commande
def main(argv: list[str]) -> int:
    n = len(argv)
    c = argv[1] if n > 1 else ""
    if c == "go" and n == 5:
        print(go(*argv[2:5]))
    elif c == "instances" and n == 6:
        print(instances(*argv[2:6], sys.stdin.read()))
    elif c == "offres" and n == 7:
        print(offres(*argv[2:7]))
    elif c == "credit" and n == 3:
        credit(argv[2], sys.stdin.read())
    elif c == "identifiant" and n == 4:
        print(identifiant(*argv[2:4]))
    elif c == "etat" and n == 2:
        print(etat(sys.stdin.read()))
    elif c == "motif" and n == 4:
        print(motif(*argv[2:4]))
    elif c == "depense" and n == 7:
        depense(*argv[2:7], sys.stdin.read())
    elif c == "valeurs" and n == 3:
        print(valeurs(argv[2]))
    elif c == "constantes" and n == 3:
        print(constantes(argv[2]))
    elif c == "longueurs" and n == 4:
        print(longueurs(*argv[2:4]))
    elif c == "config" and n == 5:
        print(config(*argv[2:5]))
    elif c == "preuves" and n >= 3:
        print("\n".join(preuves(argv[2], argv[3:])))
    else:
        print("usage : go PREREG GO_MD JOUR | instances TOLEREES EN_MARCHE GO_MD JOURNAL | offres BRUT SORTIE JOURNAL "
              "RELUES REPLI | credit SOMME | identifiant ID LANCEMENT | etat | motif JOURNAL PROGRES | depense CREATION "
              "MAINTENANT DPH_OFFRE ANTERIEURE INTERVALLE | valeurs PREREG | constantes DOSSIER | longueurs MESURE "
              "ATTENDUES | preuves DOSSIER [JOURNAL …]", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
