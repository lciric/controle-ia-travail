"""Garde des réglages des appels aux modèles de Google, version 3.

v3 (même développeur, 21 novembre 2026, décision de la mère sur les réserves de la v8b du collisionneur) : copie de
garde_google_v2.py (9d39a749…, inchangée, R12). Changement, et seulement celui-là : rapport de jetons par mot PAR ESPÈCE,
égal au plus haut mesuré pour cette espèce sur les 43 réponses réelles complètes des journaux versés (relevé de Fable,
verification-corrections-collisionneur-v9-v8-fable-v1.md, 9cf6799f…, section 4.2), arrondi au dixième supérieur : Argon
5,06 (22 réponses) → 5,1 ; Carbon 4,11 (21 réponses) → 4,2 ; Neon : AUCUNE mesure (jamais servi par le dépôt), pris au plus
haut mesuré toutes espèces confondues, 5,1, par prudence, à remplacer par sa mesure après l'essai réel.

v2 (même développeur, 21 novembre 2026, après la vérification de Fable verification-corrections-collisionneur-v9-v8-fable-v1.md,
9cf6799f…, et les décisions de la mère) : copie de garde_google_v1.py (04d233bd…, inchangée, R12). Changements, et
seulement ceux-là : (K-2, décision de la mère) rapport de jetons par mot pris sur les mesures : le plus haut relevé sur les
43 réponses réelles complètes d'Argon et de Carbon des journaux versés (branche runs/collisionneurs-reprise-minuit-v1,
relevé de Fable, section 4.2 : Argon 1,78 à 5,06, Carbon 2,40 à 4,11 jetons de texte par mot de la limite du tour), 5,06,
arrondi à 5,1, pour toutes les espèces (table JETONS_PAR_MOT_MESURES, une ligne par espèce) ; Argon à 65 536 en flux
(page versée docs/sources/google-gemini-reflexion-v1/gemini-thinking-generate-content-2026-11-21-v1.md.txt, fe0b8d88…,
ligne 931 : 65 536 « on streaming or SDK calls for gemini-4-carbon and gemini-4-argon »), jamais servi : à confirmer par
l'essai réel de la mère ; sources des pages de Google accordées à leur versement.

Écrite le 21 novembre 2026 par Claude Opus 5.5, développeur du collisionneur v9 révision 8, sur l'ordre de la mère et la
règle de `CLAUDE.md` « Appels aux modèles de Google » (GO-2026-11-21-71) : « Avant tout envoi à un modèle de Google, par
tout script, une vérification par code refuse l'envoi si : le réglage de réflexion n'est pas explicite dans le corps
(niveau le plus haut admis ou budget prévu) ; le plafond de sortie n'atteint pas réflexion plus 16 000 jetons de texte ;
la limite de mots de l'invite ne tient pas dans le plafond de texte. Après la réponse : zéro jeton de pensée, fin en
MAX_TOKENS, SAFETY, RECITATION ou texte vide = défaut journalisé, jamais une réponse. »
Pièce d'instrument (classe B), à contre-lire. Sans état, sans réseau, bibliothèque standard seule.

Emploi, avant l'envoi :
    problemes = verifier_reglages_google("carbon", corps, provision=49152, mots=3500, mode="flux")
    if problemes: refuser l'envoi (rien ne part), consigner les problèmes.
Après la réponse :
    defaut = defaut_reponse_google(finishReason, texte, thoughtsTokenCount, blocage=promptFeedback.blockReason)
    if defaut: journaliser le défaut ; jamais une réponse.
Repli déclaré : si Google refuse le niveau de réflexion (400 qui nomme le niveau, `niveau_refuse`), un appelant peut
renvoyer une fois au budget prévu (`BUDGETS_REPLI`), en le disant au journal ; la garde contrôle alors le budget
(`budget_attendu`). Jamais de repli silencieux.

Sources (provenance de chaque chiffre) :
- niveaux : page publique « Gemini thinking », variante generateContent, https://ai.google.dev/gemini-api/docs/thinking.md.txt
  ?generate-content=true, lue le 21 novembre 2026 à 17:42Z, empreinte fe0b8d88…, NON VERSÉE à l'écriture de la v1, versée
  depuis (v2) : docs/sources/google-gemini-reflexion-v1/gemini-thinking-generate-content-2026-11-21-v1.md.txt (sceau tenu) ;
  référence versée : docs/sources/google-gemini-reflexion-v1/reference-generate-content-2026-11-21-v1.md.txt (829dabb8…) : ligne 591 (Carbon et
  Argon : low, medium, high ; Neon : low, medium, high, xhigh ; « thinkingLevel […] required for Gemini 4 ») ; ligne 939
  (« thinkingBudget […] is deprecated […] sending thinkingBudget and thinkingLevel together returns a 400 error ») ;
  ligne 750 (corps REST : "thinkingConfig": {"thinkingLevel": "xhigh"}). Versée : page du modèle Neon,
  docs/sources/prix/page-modele-gemini-4-neon-20261121T134943Z.html (2eadc192…), ligne 153, « Supported (low, medium,
  high, xhigh) ». Dans le dépôt : "thinkingLevel": "high" accepté (code 200) pour Argon et Carbon le 21 novembre 2026,
  docs/notes/papier-dopamine-moniteur-v1/approfondissement-v1/appel-argon-v1.json (99539ec5…) et appel-carbon-v1.json.
- limites de sortie : liste des modèles versée, docs/notes/collisionneur-v9/liste-modeles-gemini-20261121T134904Z.json
  (eeec19e8…), outputTokenLimit : Argon 32 768 (ligne 594), Carbon 32 768 (ligne 612), Neon 65 536 (ligne 648) ; page du
  modèle Neon versée, ligne 53 (« 65,536 (default synchronous) »). Carbon en flux : 65 536, AU-DELÀ de la liste versée,
  sur la page non versée (fe0b8d88…, ligne 931 : 65 536 « on streaming […] calls for gemini-4-carbon and gemini-4-argon »,
  32 768 en appel REST non diffusé) et sur les journaux versés (branche runs/collisionneurs-reprise-minuit-v1, run
  « percée », sortie facturée 55 125 en flux sous un plafond de 65 536). Argon en flux : v1, gardé à la liste versée
  (32 768) ; v2, 65 536 (même ligne 931 de la page versée), jamais servi au-delà de 32 768.
- 16 000 jetons de texte : CLAUDE.md, « Appels à Carbon » (GO-2026-11-21-47) et « Appels aux modèles de Google ».
- 1,6 jeton par mot (v1) : ordre de la mère du 21 novembre, non mesuré ; v2 : 5,1, mesuré (voir l'en-tête v2).
- budgets de repli : Carbon 32 768 (accepté par Google le 20 novembre, journaux du collisionneur v9-v3) ; Neon 32 768
  (jamais envoyé) ; Argon 16 384 (SUPPOSÉ ; sous 8 192, zéro pensée sur 22 réponses, contre-lecture de Fable de la v9-v7,
  section 3.1). Un budget seul est déprécié chez Gemini 4 (page non versée, ligne 939) : le refus de zéro pensée après la
  réponse reste la protection.
"""
import math
import re

VERSION_GARDE = "garde-google-v3"

NIVEAUX_REFLEXION = {"argon": ("low", "medium", "high"), "carbon": ("low", "medium", "high"),
                     "neon": ("low", "medium", "high", "xhigh")}
NIVEAU_MAX_REFLEXION = {e: niveaux[-1] for e, niveaux in NIVEAUX_REFLEXION.items()}
# Limite de sortie par espèce et par mode d'appel : « flux » (streamGenerateContent) ou « non_diffuse » (generateContent
# sans flux, lot batchGenerateContent compris).
LIMITES_SORTIE = {"argon": {"flux": 65536, "non_diffuse": 32768},  # v2 : Argon à 65 536 en flux (page versée, l. 931)
                  "carbon": {"flux": 65536, "non_diffuse": 32768},
                  "neon": {"flux": 65536, "non_diffuse": 65536}}
MODES = ("flux", "non_diffuse")
TEXTE_MIN_GOOGLE = 16000
# v3 (décision de la mère) : le plus haut mesuré PAR ESPÈCE, arrondi au dixième supérieur : Argon 5,06 → 5,1 ; Carbon
# 4,11 → 4,2 ; Neon sans mesure, 5,1 (le plus haut mesuré toutes espèces), par prudence. v2 : 5,1 pour toutes.
JETONS_PAR_MOT_MESURES = {"argon": 5.1, "carbon": 4.2, "neon": 5.1}
MESURES_JETONS_PAR_MOT = {"argon": {"reponses": 22, "minimum": 1.78, "mediane": 3.47, "maximum": 5.06},
                          "carbon": {"reponses": 21, "minimum": 2.40, "mediane": 3.41, "maximum": 4.11},
                          "neon": None}  # relevé de Fable (9cf6799f…, section 4.2), sur les journaux versés
JETONS_PAR_MOT = max(JETONS_PAR_MOT_MESURES.values())  # le plus haut de la table (5,1), pour mémoire
BUDGETS_REPLI = {"argon": 16384, "carbon": 32768, "neon": 32768}
REFUS_GOOGLE = {"SAFETY", "PROHIBITED_CONTENT", "BLOCKLIST", "SPII", "RECITATION", "IMAGE_SAFETY"}
STATUT_SANS_PENSEES = "SANS_PENSEES"
MOTIF_NIVEAU_REFUSE = re.compile(r"thinking[_ ]?level|thinkingLevel", re.I)


def entier(valeur):
    """Entier ≥ 0 (booléen exclu), ou None."""
    return valeur if isinstance(valeur, int) and not isinstance(valeur, bool) and valeur >= 0 else None


def verifier_reglages_google(espece, corps, provision, mots=None, mode="flux", niveau_attendu=None, budget_attendu=None,
                             texte_min=TEXTE_MIN_GOOGLE, jetons_par_mot=None):
    """Avant l'envoi. `corps` : corps de génération tel qu'il partira (contents, generationConfig) ; `provision` :
    réflexion comptée, en jetons (positive) ; `mots` : limite de mots demandée dans l'invite ; `mode` : « flux » ou
    « non_diffuse » ; `niveau_attendu` : niveau à envoyer (défaut : le plus haut admis) ; `budget_attendu` : repli déclaré
    au budget (le niveau est alors interdit). Renvoie la liste des problèmes ; vide : l'envoi peut partir.
    (1) réflexion explicite : thinkingLevel admis et attendu, sans thinkingBudget ; ou, en repli déclaré, thinkingBudget
        égal au budget attendu, positif, au plus la provision, sans thinkingLevel ; includeThoughts vrai ;
    (2) plafond : maxOutputTokens entier, au plus la limite de l'espèce pour ce mode, au moins provision + texte_min ;
    (3) limite de mots : ⌈mots × jetons_par_mot⌉ < maxOutputTokens − provision ; v2 : jetons_par_mot, par défaut, le
        rapport mesuré de l'espèce (JETONS_PAR_MOT_MESURES)."""
    if espece not in NIVEAUX_REFLEXION or espece not in LIMITES_SORTIE or espece not in JETONS_PAR_MOT_MESURES:
        return [f"{espece} : espèce de Google sans réglage de réflexion ni limite connus ; rien ne part"]
    jetons_par_mot = JETONS_PAR_MOT_MESURES[espece] if jetons_par_mot is None else jetons_par_mot  # v2 (K-2)
    if mode not in MODES:
        return [f"mode d'appel {mode!r} inconnu ({', '.join(MODES)})"]
    problemes = []
    config = corps.get("generationConfig") if isinstance(corps, dict) else None
    config = config if isinstance(config, dict) else {}
    pensee = config.get("thinkingConfig") if isinstance(config.get("thinkingConfig"), dict) else {}
    niveau, budget = pensee.get("thinkingLevel"), pensee.get("thinkingBudget")
    if budget_attendu is None:
        attendu = NIVEAU_MAX_REFLEXION[espece] if niveau_attendu is None else niveau_attendu
        if niveau is None:
            problemes.append("réflexion : thinkingConfig.thinkingLevel absent du corps")
        elif niveau not in NIVEAUX_REFLEXION[espece]:
            problemes.append(f"réflexion : niveau {niveau!r} non admis pour {espece}")
        elif niveau != attendu:
            problemes.append(f"réflexion : niveau envoyé {niveau!r} au lieu de {attendu!r}")
        if "thinkingBudget" in pensee:
            problemes.append("réflexion : thinkingBudget présent (déprécié chez Gemini 4 ; 400 avec un niveau)")
    else:
        if "thinkingLevel" in pensee:
            problemes.append("réflexion : repli au budget déclaré, mais thinkingLevel présent (400 avec un budget)")
        if entier(budget) is None or budget <= 0:
            problemes.append(f"réflexion : budget {budget!r} absent, nul ou mal formé (réflexion coupée)")
        elif budget != budget_attendu:
            problemes.append(f"réflexion : budget envoyé {budget} au lieu du budget prévu {budget_attendu}")
        elif entier(provision) is not None and budget > provision:
            problemes.append(f"réflexion : budget {budget} au-delà de la provision comptée {provision}")
    if pensee.get("includeThoughts") is not True:
        problemes.append("réflexion : includeThoughts non vrai (les pensées ne seraient pas lues en retour)")
    plafond = config.get("maxOutputTokens")
    if entier(plafond) is None or entier(provision) is None or provision <= 0:
        problemes.append(f"plafond : maxOutputTokens {plafond!r} ou provision {provision!r} mal formés ou nuls")
        return problemes
    limite = LIMITES_SORTIE[espece][mode]
    if plafond > limite:
        problemes.append(f"plafond : maxOutputTokens {plafond} au-delà de la limite de {espece} en {mode} ({limite})")
    texte = plafond - provision
    if texte < texte_min:
        problemes.append(f"plafond : {plafond} − réflexion {provision} = {texte} jetons de texte < {texte_min}")
    if mots is not None and math.ceil(mots * jetons_par_mot) >= texte:
        problemes.append(f"limite de mots : {mots} mots × {jetons_par_mot:g} = {math.ceil(mots * jetons_par_mot)} jetons ≥ "
                         f"plafond de texte {texte}")
    return problemes


def defaut_reponse_google(fin, texte, pensees, blocage=None):
    """Après la réponse. Renvoie None si c'est une réponse (fin STOP, texte non vide, au moins un jeton de pensée), sinon
    le nom du défaut : le motif de blocage de l'invite, un motif de refus (SAFETY, RECITATION…), MAX_TOKENS, VIDE,
    FIN_<motif> (autre fin, fin absente comprise) ou SANS_PENSEES (zéro jeton, ou champ absent : jamais lu comme zéro
    accepté). Un défaut n'est jamais une réponse."""
    if blocage:
        return str(blocage)
    if fin in REFUS_GOOGLE:
        return fin
    if fin == "MAX_TOKENS":
        return "MAX_TOKENS"
    if not str(texte or "").strip():
        return "VIDE"
    if fin != "STOP":
        return f"FIN_{fin}"
    if entier(pensees) is None or pensees <= 0:
        return STATUT_SANS_PENSEES
    return None


def niveau_refuse(message):
    """Vrai si un message d'échec avant traitement (HTTP 400) nomme le niveau de réflexion : seul cas où un appelant peut
    faire le repli déclaré au budget prévu."""
    texte = str(message or "")
    return "400" in texte and bool(MOTIF_NIVEAU_REFUSE.search(texte))
