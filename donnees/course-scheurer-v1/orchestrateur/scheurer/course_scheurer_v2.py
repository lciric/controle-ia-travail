"""KIT SCHEURER v2 (sous-agent de session-depot, 3 novembre 2026) : v1 (gardée, R12) plus la variante « sans-claude » (proposeurs Argon, Kimi, Astra ; aiguilleur Astra ; juges Astra et Argon ; lecteurs Astra et Argon ; metteur Astra ; aucun rôle Claude ; relais 8806 non démarré, contrôle de Claude non joué) ; S17 propre à cette variante ; les configurations existantes ne sont ni réécrites ni changées.
KIT SCHEURER, v1 (sous-agent de session-depot, 3 novembre 2026) : dérivé du kit Ibrahim v2 (outils/course-ibrahim-q1-v1, 965eb21b) par substitution de noms et par les changements de la course Scheurer (deux pièces servies, cinq variantes dont trois sans Opus proposeur, jeu de rôles par variante (Opus ou Fable), garde lexicale sans « gemini » ni « openai », juge du n° 419, marge d'appels 2 × plan + 5).
Course d'idéation sur la question 1 de le mentor Scheurer — v2 = `course_scheurer_v2.py` (gardé, R12) avec la seule garde
lexicale changée (contre-lecture CLH-03) : « gpt » remplacé par « gpt 6 », « gpt6 », « gpt-6 » (« GPT-2 », « GPT-J », « GPT-4 » passent,
« gpt-6-astra » reste attrapé). Au-dessus de l'orchestrateur v56 (copie à l'octet, inchangée).

Rédigé le 3 novembre 2026 (sous-agent de session-depot) ; rien n'a été lancé de payant par le rédacteur. Reprend la génération
de la mini-course (`pole/course2_nuit_v1.GenerationNuitV1` : une génération, passe « tableau » sans appel, liste d'arrêt) et
l'adaptateur des commandes (`pole/course2_nuit_v2.AdaptateurCommandeExterneNuitV2` : modèle servi différent, dépassement de
réserve, garde cumulée, garde d'étape, plafond d'un relais = arrêt de la course), avec ce qui change pour cette course :

- **contrôles de configuration propres** (`verifier_configuration_scheurer`, avant tout appel) : trois variantes fermées
  (`sans_kimi`, `avec_kimi`, `cinq_especes`) ; rôles fixes (aiguilleur Opus 5.5, juges Opus 5.5 et Astra, lecteurs Opus 5.5
  et Astra, metteur Fable 5.1) ; bras `gu_krenn` (substitut) et `basique` seuls (bras méta hors course, motif au LISEZMOI) ;
  au moins trois paires par bras ; Argon (port 8805) seulement dans `cinq_especes` ; ports fixes ; réglages Claude
  `--effort high --reflexion adaptative` ; plafonds de session au-dessus du pire cas de chaque appel de leur rôle (calcul
  ci-dessous) ; relais Kimi ≤ 5 USD, Argon ≤ 10 USD, somme des relais ≤ S17 ; plafond cumulé de chaque commande = S17 ;
  garde lexicale sans aucune étiquette présente dans la question ou la pièce servies, ni dans les consignes servies aux
  juges, à l'aiguilleur et aux lecteurs, ni dans les listes fermées ; consigne du proposeur qui enchâsse à l'octet les trois
  sections de la question et la pièce entière ;
- **aucun témoin planté** (la course v56 n'en porte pas ; constat de session-depot) : dit au manifeste ;
- **première exécution réelle des bras** : dite au manifeste ;
- le plan d'appels et le devis (`plan_appels`, `devis`) sont calculés ici, une seule fois, pour le script de devis, le
  constructeur des configurations et les essais.
"""

import json
import math
import os

from pole.configuration_v53 import ConfigurationRefusee, texte_piece
from pole.course2_nuit_v1 import (ArretDebordementKimi, ArretModeleServiDifferent, ArretTroisEchecs,  # noqa: F401
                                  GenerationNuitV1)
from pole.course2_nuit_v2 import AdaptateurCommandeExterneNuitV2, motif_de_ligne  # noqa: F401
from pole.fiches_v54 import trouver
from pole.noyau_v56 import ArretSurSignal, motif_arret
from pole.outils import EcrasementInterdit, ecrire_json_scelle

VERSION = "course-scheurer-v1 (orchestrateur v56, génération course2_nuit_v1, adaptateur course2_nuit_v2)"
SCENARIO = ("Scheurer : une génération, 6 fiches par proposeur, bras « gu_krenn » (substitut) et « basique », sans passe "
            "« tableau », aucun témoin planté ; bras méta hors course (aucune annexe)")
ITEMS_JUGE = ['K1', 'K2', 'K3', 'K4']
FICHES_PAR_PROPOSEUR = 6  # comme Scheurer (ordre de session-depot, 13:50 UTC)
K_PAIRES_MIN = 3
BRAS_JOUES = ("gu_krenn", "basique")

# --- espèces, rôles fixes, prix et sorties maximales (USD par million, entrée / sortie) -----------------------------------------
PRIX = {"claude-fable-5-1": (10.0, 50.0), "claude-opus-5-5": (4.0, 20.0), "gpt-6-astra": (10.0, 50.0),
        "kimi-k3.1-pro": (2.0, 10.0), "gemini-4-argon": (10.0, 50.0)}
SOURCE_PRIX = {"claude-fable-5-1": "documentation de l'interface (table des modèles, cache du 6 octobre 2026), commande A1-bis",
               "claude-opus-5-5": "documentation de l'interface (table des modèles, cache du 6 octobre 2026), commande A1-bis",
               "gpt-6-astra": "SUPPOSÉ haut (commande A1-bis, collisionneur v8)",
               "kimi-k3.1-pro": "commande_kimi_v2.py (défauts --prix-entree 2, --prix-sortie 10)",
               "gemini-4-argon": "SUPPOSÉ (commande_argon_v56_nuit_v2.py, barème prudent du collisionneur v7)"}
FOURNISSEUR_DE = {"claude-fable-5-1": "claude", "claude-opus-5-5": "claude", "gpt-6-astra": "astra", "kimi-k3.1-pro": "kimi",
                  "gemini-4-argon": "argon"}
# sorties maximales (jetons) par fournisseur : (proposeur et metteur, rôles courts) — options des commandes de la configuration
MAX_SORTIE = {"claude": (64000, 16000), "astra": (32000, 16000), "kimi": (65536, 16000), "argon": (32000, 4000)}
PORTS = {"claude": 8806, "astra": 8807, "kimi": 8804, "argon": 8805}
PLAFOND_RELAIS_MAX = {"kimi": 5.0, "argon": 10.0}
REGLAGES_CLAUDE = ("--effort", "high", "--reflexion", "adaptative")
PROPOSEURS = {"prop-fable": "claude-fable-5-1", "prop-opus": "claude-opus-5-5", "prop-argon": "gemini-4-argon",
              "prop-kimi": "kimi-k3.1-pro", "prop-astra": "gpt-6-astra"}
VARIANTES = {
    'sans_opus': ('prop-fable', 'prop-kimi', 'prop-astra'),
    'sans_opus_argon': ('prop-fable', 'prop-argon', 'prop-kimi', 'prop-astra'),
    'sans_opus_sans_kimi': ('prop-fable', 'prop-astra'),
    'sans_opus_juges_opus': ('prop-fable', 'prop-kimi', 'prop-astra'),
    'avec_opus': ('prop-fable', 'prop-opus', 'prop-kimi', 'prop-astra'),
    'sans_claude': ('prop-argon', 'prop-kimi', 'prop-astra'),
}
# jeu de rôles par variante : « opus » (aiguilleur, juge et lecteur Opus 5.5, comme Scheurer) ou « fable » (Fable 5.1 à la place d'Opus)
ROLES_DE_VARIANTE = {
    'sans_opus': 'fable',
    'sans_opus_argon': 'fable',
    'sans_opus_sans_kimi': 'fable',
    'sans_opus_juges_opus': 'opus',
    'avec_opus': 'opus',
    'sans_claude': 'astra_argon',
}
VARIANTES_ARGON = tuple(v for v, p in VARIANTES.items() if "prop-argon" in p)
JEUX_ROLES = {"opus": (("aiguilleur-opus", "claude-opus-5-5"), (("juge-opus", "claude-opus-5-5"), ("juge-astra", "gpt-6-astra")),
                       (("lecteur-opus", "claude-opus-5-5"), ("lecteur-astra", "gpt-6-astra"))),
              "fable": (("aiguilleur-fable", "claude-fable-5-1"), (("juge-fable", "claude-fable-5-1"), ("juge-astra", "gpt-6-astra")),
                        (("lecteur-fable", "claude-fable-5-1"), ("lecteur-astra", "gpt-6-astra")))}
# sans Claude (au plus près d'Ibrahim : chaque rôle de Claude passe à Astra, chaque rôle d'Astra passe à Argon ; Kimi hors des rôles, R-1155)
JEUX_ROLES["astra_argon"] = (("aiguilleur-astra", "gpt-6-astra"), (("juge-astra", "gpt-6-astra"), ("juge-argon", "gemini-4-argon")),
                             (("lecteur-astra", "gpt-6-astra"), ("lecteur-argon", "gemini-4-argon")))
AIGUILLEUR, JUGES, LECTEURS = JEUX_ROLES["opus"]  # jeu par défaut (repère) ; chaque variante lit le sien par roles()


def roles(variante):
    """(aiguilleur, juges, lecteurs) de la variante."""
    return JEUX_ROLES[ROLES_DE_VARIANTE[variante]]


PIECES_SERVIES = ('piece_mentor', 'piece_nos_resultats')  # dans l'ordre de la consigne du proposeur
TETE_QUESTION = '## La question, telle que le mentor la pose'
METTEUR = ("metteur-fable", "claude-fable-5-1")
JEUX_METTEUR = {"opus": METTEUR, "fable": METTEUR, "astra_argon": ("metteur-astra", "gpt-6-astra")}
# plafond propre maximal des relais : Kimi ≤ 5, Argon ≤ 10 ; sans Claude, Argon juge et lit : borné par sa part au pire cas et S17
PLAFOND_RELAIS_MAX_VARIANTE = {"sans_claude": {"kimi": 5.0}}


def metteur(variante):
    return JEUX_METTEUR[ROLES_DE_VARIANTE[variante]]


def plafond_relais_max(variante):
    return PLAFOND_RELAIS_MAX_VARIANTE.get(variante, PLAFOND_RELAIS_MAX)


def modeles_de_variante(variante):
    """Modèles appelés par la course dans cette variante (proposeurs et rôles), sans les contrôles."""
    ai, ju, le = roles(variante)
    return sorted({PROPOSEURS[p] for p in VARIANTES[variante]} | {ai[1], metteur(variante)[1]} | {x[1] for x in ju} | {x[1] for x in le})
ETIQUETTES_EXIGEES = ('exploratoire', 'bras méta', 'gu et krenn', 'gu krenn', 'bisociation', 'kimi', 'moonshot', 'fable', 'astra', 'gpt 6', 'gpt6', 'gpt-6', 'chatgpt')
ETIQUETTES_REFUSEES = ('claude', 'opus', 'anthropic', 'sonnet', 'gpt', 'argon', 'fusion', 'gemini', 'openai')  # la pièce servie les cite : jamais interdites ici
FICHE_MAX_CARACTERES = 12000  # borne supposée d'une fiche servie (calcul des plafonds de session : mesure au second tour ≈ 2 500)


def jetons_entree_pire(caracteres):
    """Formule des commandes Claude, Astra et Argon : caractères / 3."""
    return caracteres / 3.0


def pire_cas_appel(modele, caracteres, role_long):
    """Pire cas d'un appel au barème : entrée (caractères / 3 ; Kimi : octets + 1024, octets ≤ 2 × caractères) et sortie maximale."""
    pe, ps = PRIX[modele]
    four = FOURNISSEUR_DE[modele]
    sortie = MAX_SORTIE[four][0 if role_long else 1]
    if four == "kimi":
        entree = (2 * caracteres + 1024)
    else:
        entree = jetons_entree_pire(caracteres)
    return entree * pe / 1e6 + sortie * ps / 1e6


# --- plan d'appels -----------------------------------------------------------------------------------------------------------


def plan_appels(variante, k_paires, fiches_par_proposeur=FICHES_PAR_PROPOSEUR, bras=BRAS_JOUES, passeport=1.0):
    """Lignes (étape, rôle, modèle, nombre) d'une course complète : chaque fiche reçoit un passeport (`passeport` = part des
    fiches admises, 1 au pire cas), chaque bras a ses `k_paires` paires, chaque fusion est aiguillée puis jugée."""
    props = VARIANTES[variante]
    AIGUILLEUR, JUGES, LECTEURS = roles(variante)
    n_fiches = fiches_par_proposeur * len(props)
    admises = int(round(n_fiches * passeport))
    n_fus = k_paires * len(bras)
    lignes = [("proposition", p, PROPOSEURS[p], 1) for p in props]
    lignes.append(("aiguillage", AIGUILLEUR[0], AIGUILLEUR[1], n_fiches))
    lignes += [("juges", j, m, admises) for j, m in JUGES]
    lignes += [("etiquettes", lec, m, admises * len(bras)) for lec, m in LECTEURS]
    lignes.append(("fusions", *metteur(variante), n_fus))
    lignes.append(("fusions", AIGUILLEUR[0], AIGUILLEUR[1], n_fus))
    lignes += [("fusions", j, m, n_fus) for j, m in JUGES]
    return lignes


def role_plafond(role):
    if role.startswith("prop-"):
        return "proposeur"
    return {"aiguilleur-opus": "aiguilleur", "aiguilleur-fable": "aiguilleur", "juge-fable": "juge", "lecteur-fable": "lecteur", "juge-opus": "juge", "juge-astra": "juge", "lecteur-opus": "lecteur",
            "lecteur-astra": "lecteur", "metteur-fable": "fusion", "aiguilleur-astra": "aiguilleur", "juge-argon": "juge",
            "lecteur-argon": "lecteur", "metteur-astra": "fusion"}[role]


def caracteres_pire(role_plaf, longueurs):
    """Borne des caractères d'entrée d'un appel du rôle (`longueurs` : caractères des consignes et des listes servies)."""
    f = FICHE_MAX_CARACTERES
    return {"proposeur": longueurs["consigne_proposeur"] + 200, "aiguilleur": longueurs["consigne_aiguilleur"] + f + 50,
            "juge": longueurs["consigne_juge"] + f + 50,
            "lecteur": longueurs["consigne_lecteur"] + longueurs["liste_la_plus_longue"] + f + 100,
            "fusion": longueurs["consigne_fusion"] + 2 * f + 100}[role_plaf]


def pire_cas_par_role(longueurs, variante):
    """{rôle de plafond : (pire cas USD d'un appel au modèle le plus cher du rôle, modèle)}."""
    AIGUILLEUR, JUGES, LECTEURS = roles(variante)
    modeles = {"proposeur": [PROPOSEURS[p] for p in VARIANTES[variante]], "aiguilleur": [AIGUILLEUR[1]],
               "juge": [m for _, m in JUGES], "lecteur": [m for _, m in LECTEURS], "fusion": [metteur(variante)[1]]}
    sortie = {}
    for r, ms in modeles.items():
        c = caracteres_pire(r, longueurs)
        sortie[r] = max((pire_cas_appel(m, c, r in ("proposeur", "fusion")), m) for m in ms)
    return sortie


# --- configuration -----------------------------------------------------------------------------------------------------------


def _commande(conf, f):
    return list(((conf.get("fournisseurs") or {}).get(f) or {}).get("commande") or [])


def _option(commande, nom):
    if nom in commande:
        i = commande.index(nom)
        return commande[i + 1] if i + 1 < len(commande) else None
    return None


def longueurs_servies(conf):
    t = {n: texte_piece(conf, n) for n in ("consigne_proposeur", "consigne_aiguilleur", "consigne_juge", "consigne_lecteur",
                                           "consigne_fusion", "liste_concepts")}
    vocab = json.dumps(sorted({c for o in json.loads(texte_piece(conf, "source_gu_krenn"))["oeuvres"] for c in o["concepts"]}),
                       ensure_ascii=False)
    return {"consigne_proposeur": len(t["consigne_proposeur"]), "consigne_aiguilleur": len(t["consigne_aiguilleur"]),
            "consigne_juge": len(t["consigne_juge"]), "consigne_lecteur": len(t["consigne_lecteur"]),
            "consigne_fusion": len(t["consigne_fusion"]),
            "liste_la_plus_longue": max(len(json.dumps(json.loads(t["liste_concepts"]), ensure_ascii=False)), len(vocab))}


def verifier_configuration_scheurer(conf):
    """Contrôles propres à la course Scheurer, avant tout appel ; tous les manques en une fois. Rend le résumé."""
    m = []
    v = conf.get("variante")
    if v not in VARIANTES:
        raise ConfigurationRefusee(f"variante : une de {sorted(VARIANTES)} exigée (reçu {v!r})")
    props = [(p.get("etiquette"), p.get("modele"), p.get("fournisseur")) for p in conf["proposeurs"]]
    attendus = [(p, PROPOSEURS[p], FOURNISSEUR_DE[PROPOSEURS[p]]) for p in VARIANTES[v]]
    if props != attendus:
        m.append(f"proposeurs : {attendus} exigés pour la variante {v} (reçu {props})")
    AIGUILLEUR, JUGES, LECTEURS = roles(v)
    ai = conf["aiguilleur"]
    if (ai.get("etiquette"), ai.get("modele"), ai.get("fournisseur")) != (*AIGUILLEUR, FOURNISSEUR_DE[AIGUILLEUR[1]]):
        m.append(f"aiguilleur : {AIGUILLEUR}, claude exigés")
    if [(j.get("etiquette"), j.get("modele"), j.get("fournisseur")) for j in conf["juges"]] != \
            [(e, mo, FOURNISSEUR_DE[mo]) for e, mo in JUGES]:
        m.append(f"juges : {JUGES} exigés, dans cet ordre")
    if [(x.get("etiquette"), x.get("modele"), x.get("fournisseur")) for x in conf["lecteurs_etiquettes"]] != \
            [(e, mo, FOURNISSEUR_DE[mo]) for e, mo in LECTEURS]:
        m.append(f"lecteurs : {LECTEURS} exigés, dans cet ordre")
    b = conf["bisociateur"]
    mf = b.get("metteur_fusion") or {}
    if (mf.get("etiquette"), mf.get("modele"), mf.get("fournisseur")) != (*metteur(v), FOURNISSEUR_DE[metteur(v)[1]]):
        m.append(f"metteur : {metteur(v)} exigé")
    if sorted(b.get("bras") or []) != sorted(BRAS_JOUES):
        m.append(f"bisociateur.bras : {list(BRAS_JOUES)} exigés (bras méta hors course : annexe Scheurer absente)")
    if (b.get("gu_krenn") or {}).get("mode") != "substitut":
        m.append("bisociateur.gu_krenn.mode : « substitut » exigé (seul permis en v56)")
    if not isinstance(b.get("k_paires"), int) or b["k_paires"] < K_PAIRES_MIN:
        m.append(f"bisociateur.k_paires : au moins {K_PAIRES_MIN} (trois mariages par bras)")
    if (conf.get("tableau") or {}).get("juger_passe_tableau") is not False:
        m.append("tableau.juger_passe_tableau : false exigé (passe retirée)")
    pt = [e for e in conf["budget"]["etapes"] if e.get("nom") == "passe_tableau"]
    if len(pt) != 1 or pt[0].get("attendu_usd") != 0 or pt[0].get("plafond_relais_usd") != 0 or pt[0].get("role") != "sacrifiable":
        m.append("budget.etapes : passe_tableau sacrifiable, attendu 0 et plafond de relais 0 exigés")
    if conf["budget"].get("portee_plafond") != "course":
        m.append("budget.portee_plafond : « course » exigé")
    if (conf.get("simulation") or {}).get("fiches_par_appel") != FICHES_PAR_PROPOSEUR:
        m.append(f"simulation.fiches_par_appel : {FICHES_PAR_PROPOSEUR} exigé")
    s17 = float(conf["budget"]["plafond_usd"])
    utilises = sorted({FOURNISSEUR_DE[mo] for mo in modeles_de_variante(v)})
    four = conf.get("fournisseurs") or {}
    if sorted(four) != utilises:
        m.append(f"fournisseurs : exactement {utilises} (reçu {sorted(four)})")
    if v not in VARIANTES_ARGON and ("argon" in four or any("8805" in " ".join(_commande(conf, f)) for f in four)):
        m.append(f"Argon (port 8805) hors des variantes {list(VARIANTES_ARGON)} : refusé")
    for f in four:
        c = _commande(conf, f)
        if four[f].get("type") != "commande_externe" or (four[f].get("porte_plafond") or {}).get("type") != "environnement":
            m.append(f"fournisseurs.{f} : commande externe à porte « environnement » exigée")
        if _option(c, "--url-relais") != f"http://127.0.0.1:{PORTS[f]}":
            m.append(f"fournisseurs.{f} : --url-relais http://127.0.0.1:{PORTS[f]} exigé")
        if _option(c, "--plafond-cumule-usd") is None or abs(float(_option(c, "--plafond-cumule-usd")) - s17) > 1e-9:
            m.append(f"fournisseurs.{f} : --plafond-cumule-usd égal à S17 ({s17:g}) exigé")
        mp, mc = MAX_SORTIE[f]
        if _option(c, "--max-sortie-proposeur") != str(mp) or _option(c, "--max-sortie-court") != str(mc):
            m.append(f"fournisseurs.{f} : --max-sortie-proposeur {mp} et --max-sortie-court {mc} exigés (devis)")
        if sum("{REGISTRE}" in x for x in c) != 1:
            m.append(f"fournisseurs.{f} : jeton {{REGISTRE}} une fois exigé")
    cl = _commande(conf, "claude")
    if "claude" in utilises and not any(tuple(cl[i:i + 4]) == REGLAGES_CLAUDE for i in range(len(cl))):
        m.append("fournisseurs.claude : réglages « --effort high --reflexion adaptative » exigés (identiques au relais)")
    rel = conf.get("relais") or {}
    if sorted(rel) != utilises:
        m.append(f"relais : exactement {utilises}")
    else:
        for f, r in rel.items():
            if r.get("port") != PORTS[f] or not (isinstance(r.get("plafond_usd"), (int, float)) and r["plafond_usd"] > 0) \
                    or not (isinstance(r.get("max_appels"), int) and r["max_appels"] > 0):
                m.append(f"relais.{f} : port {PORTS[f]}, plafond_usd > 0 et max_appels entier > 0 exigés")
            elif f in plafond_relais_max(v) and r["plafond_usd"] > plafond_relais_max(v)[f]:
                m.append(f"relais.{f} : plafond propre au plus {plafond_relais_max(v)[f]:g} USD")
        if sum(float(r.get("plafond_usd") or 0) for r in rel.values()) > s17 + 1e-9:
            m.append("relais : somme des plafonds propres au-dessus de S17")
    interdites = conf["etiquettes_interdites"]
    manquent = [e for e in ETIQUETTES_EXIGEES if e not in interdites]
    if manquent:
        m.append(f"etiquettes_interdites : manquent {manquent}")
    refusees = [e for e in interdites if e in ETIQUETTES_REFUSEES]
    if refusees:
        m.append(f"etiquettes_interdites : {refusees} refusées (la pièce servie les cite)")
    if (conf.get("a4") or {}).get("mode") != "prefixe":
        m.append("a4.mode : « prefixe » exigé (comme la mini-course)")
    mode = (conf.get("a4") or {}).get("mode", "prefixe")
    for nom in ("question_servie", *PIECES_SERVIES, "consigne_juge", "consigne_aiguilleur", "consigne_lecteur", "liste_concepts",
                "source_gu_krenn"):
        try:
            t = texte_piece(conf, nom)
        except (KeyError, ConfigurationRefusee, OSError) as e:
            m.append(f"pièce {nom} : {e}")
            continue
        if nom == "source_gu_krenn":
            t = json.dumps(sorted({c for o in json.loads(t)["oeuvres"] for c in o["concepts"]}), ensure_ascii=False)
        trouvees = trouver(t, interdites, mode)
        if trouvees:
            m.append(f"pièce {nom} : étiquettes interdites présentes {trouvees} (A4 arrêterait ou exclurait tout)")
    try:
        cp, q = texte_piece(conf, "consigne_proposeur"), texte_piece(conf, "question_servie")
        pieces = [texte_piece(conf, n) for n in PIECES_SERVIES]
        i, j = q.find("\n" + TETE_QUESTION), q.find("\n## Ce qu'on attend de chaque espèce")
        k, l = q.find("\n## Règles d'intégrité"), q.find("\n## Lecture prévue de la sortie")
        s1, s2 = q[i + 1:j + 1], q[k + 1:l + 1]
        ordre = [s1, s2] + pieces
        if min(i, j, k, l) < 0 or any(x not in cp for x in ordre) \
                or [cp.index(x) for x in ordre] != sorted(cp.index(x) for x in ordre):
            m.append(f"consigne_proposeur : sections de la question et pièces entières ({list(PIECES_SERVIES)}) non enchâssées à l'octet")
    except (KeyError, ConfigurationRefusee, OSError) as e:
        m.append(f"consigne_proposeur : {e}")
    try:
        ps = conf["plafonds_session"]
        for r, (pire, modele) in pire_cas_par_role(longueurs_servies(conf), v).items():
            if not float(ps.get(r, 0)) > pire:
                m.append(f"plafonds_session.{r} = {ps.get(r)} : pas au-dessus du pire cas d'un appel ({pire:.4f} USD, {modele})")
    except (KeyError, ConfigurationRefusee, OSError, ValueError) as e:
        m.append(f"plafonds_session : {e}")
    if m:
        raise ConfigurationRefusee("configuration de la course Scheurer refusée :\n- " + "\n- ".join(m))
    return {"variante": v, "proposeurs": [x[0] for x in attendus], "bras": list(b["bras"]), "k_paires": b["k_paires"],
            "fournisseurs": utilises}


# --- génération et course ----------------------------------------------------------------------------------------------------


class GenerationScheurerV1(GenerationNuitV1):
    def manifeste_depart_v56(self):
        d = super().manifeste_depart_v56()
        d["version_nuit"] = "remplacé par version_course (course Scheurer)"
        d["version_course"] = VERSION
        d["scenario"] = SCENARIO
        d["variante"] = self.conf.get("variante")
        d["temoins_plantes"] = "aucun (la course v56 n'en porte pas ; le second tour réel n'en avait pas)"
        d["bras_premiere_execution_reelle"] = ("bras « gu_krenn » (substitut) et « basique » : première exécution réelle sur une "
                                               "question de recherche réelle ; bras méta hors course (aucune annexe)")
        d["moissonneur"] = "non appelé (nouveauté non cherchée)"
        return d


def executer_course_scheurer_v1(conf, sortie, adaptateurs, *, go, racine_sessions=None, portes=None, specification=None,
                                   horloge=None):
    """Une génération (`GenerationScheurerV1`), sans étage ; `bilan-course.json` écrit sur tout chemin (arrêt compris)."""
    verifier_configuration_scheurer(conf)
    if os.path.exists(sortie):
        raise EcrasementInterdit(f"sortie {sortie} déjà présente (R12)")
    os.makedirs(sortie)
    bilan, noeud, arret = [], None, None
    with ArretSurSignal() as garde:
        try:
            rs = None if racine_sessions is None else os.path.join(racine_sessions, "generation-1")
            gen = GenerationScheurerV1(conf, os.path.join(sortie, "generation-1"), adaptateurs, numero=1, memoire=None,
                                          heritage_texte=None, go=go, horloge=horloge, racine_sessions=rs, portes=portes,
                                          specification=specification)
            resultat = gen.executer()
            ligne = {"generation": 1, "fiches_classees": len(resultat), "notables": sum(l["notable"] for l in resultat),
                     "c13_satisfaite": gen.budget.etat()["c13_satisfaite"], "noeud": gen.noeud}
            if gen.noeud:
                noeud = f"génération 1 : {gen.noeud}"
            bilan.append(ligne)
        except BaseException as e:
            arret = motif_arret(e)
            raise
        finally:
            garde.nettoyage()
            ecrire_json_scelle(os.path.join(sortie, "bilan-course.json"), {"version": VERSION, "scenario": SCENARIO, "go": go,
                                                                           "variante": conf.get("variante"), "generations": bilan,
                                                                           "noeud": noeud, "arret": arret, "signaux": garde.etat()})
    return {"bilan": bilan, "noeud": noeud}


def arrondi_haut(x, pas=0.01):
    return math.ceil(x / pas - 1e-9) * pas


__all__ = ("VERSION", "SCENARIO", "PRIX", "VARIANTES", "PROPOSEURS", "PORTS", "MAX_SORTIE", "plan_appels", "pire_cas_appel",
           "pire_cas_par_role", "longueurs_servies", "verifier_configuration_scheurer", "GenerationScheurerV1",
           "executer_course_scheurer_v1", "AdaptateurCommandeExterneNuitV2", "ETIQUETTES_EXIGEES", "roles", "ROLES_DE_VARIANTE",
           "VARIANTES_ARGON", "PIECES_SERVIES")
