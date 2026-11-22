"""Fabrique collisionneur_v9_v8k.py depuis la v8j par remplacements exacts (chaque ancien texte présent une seule fois)."""
import hashlib, sys
from pathlib import Path
D = Path("/home/user/controle-ia-travail/docs/notes/collisionneur-v9")
src = (D / "collisionneur_v9_v8j.py").read_text(encoding="utf-8")
assert hashlib.sha256(src.encode()).hexdigest().startswith("d199a14b")


def remplacer(t, ancien, nouveau):
    n = t.count(ancien)
    if n != 1:
        sys.exit(f"ancien texte trouvé {n} fois : {ancien[:80]!r}")
    return t.replace(ancien, nouveau)


# 1. en-tête
src = remplacer(src, """#   de lettres et de chiffres ASCII séparés par un seul « - », « _ » ou « . » (aucun homoglyphe, aucune pleine chasse).
""", """#   de lettres et de chiffres ASCII séparés par un seul « - », « _ » ou « . » (aucun homoglyphe, aucune pleine chasse).
# v9-v8k (développeur, Claude Opus 5.5, 22 novembre 2026 ; pièce de classe B, à contre-lire) : copie du v9-v8j (d199a14b…,
#   inchangé, R12), sur le mot du directeur « tous les modèles dans le collisionneur ». Changements, et seulement ceux-là :
#   (1) trois espèces en fin d'ordre (les lettres des compositions existantes ne bougent pas) : Opus 4.6 (--opus46) et
#       Fable 5.1 (--fable51), même chemin d'appel que Fable 5.2 et Opus 5.5 ; Mistral (--mistral), fournisseur neuf,
#       interface de discussion en flux, clé lue dans la variable nommée par --cle-mistral (préfixe MISTRAL_API_KEY),
#       comptage par /v1/responses/input_tokens, mêmes gardes ; une valeur non trouvée dans les pages publiques reste à
#       None et la composition est refusée (« valeur à fixer ») ;
#   (2) Kimi : appel direct à l'interface de Moonshot par l'option explicite --kimi-direct (clé par --cle-kimi), en flux,
#       comptage par estimate-token-count ; le relais local reste le défaut ; le chemin est journalisé ;
#   (3) --sortie-max : plafonds de sortie (premier envoi et relance) au maximum documenté de chaque espèce (table
#       SORTIE_MAX_DOCUMENTEE, sources citées) ; Google sous la règle du plafond large inchangée ; sans l'option, rien ne
#       change ; le devis compte ces plafonds ;
#   (4) --effort-max : effort « max » chez Anthropic (output_config.effort), le plus haut niveau documenté pour les quatre
#       espèces d'Anthropic ; aucun réglage d'effort n'existe chez OpenAI dans ce script (rien n'y change) ;
#   (5) garde « sortie facturée au-delà du plafond envoyé » (REFLEXION_HORS_PROVISION, sens de la v9-v7) étendue aux deux
#       chemins neufs (Mistral, Kimi direct) ; jusqu'à dix espèces (lettres A à J).
#   Détail : rapport-developpeur-collisionneur-v9-v8k-v1.md, même dossier.
""")
src = remplacer(src, "(N = nombre d'espèces activées, de deux à sept)", "(N = nombre d'espèces activées, de deux à dix)")
src = remplacer(src, """passe par le relais local (KIMI_RELAIS_URL), sans clé ici.
""", """passe par le relais local (KIMI_RELAIS_URL), sans clé ici.
v9-v8k : --opus46 (claude-opus-4-6) et --fable51 (claude-fable-5-1) prennent la clé d'Anthropic (--cle-anthropic) ;
--mistral prend la clé lue dans la variable nommée par --cle-mistral (défaut MISTRAL_API_KEY ; le nom doit commencer par
MISTRAL_API_KEY) ; --kimi-direct (avec --kimi) envoie Kimi à l'interface de Moonshot, clé lue dans la variable nommée par
--cle-kimi (défaut KIMI_API_KEY ; le nom doit commencer par KIMI_API_KEY ou MOONSHOT_API_KEY) ; sans --kimi-direct, Kimi
passe par le relais local, comme avant ; le chemin est journalisé à chaque lancement (options_appel_v8k) et à chaque essai.
--sortie-max : plafonds de sortie au maximum documenté de chaque espèce (refus nommé si la valeur n'est pas documentée).
--effort-max : effort « max » chez Anthropic. Sans ces options, rien ne change.
""")
src = remplacer(src, 'VERSION = "collisionneur-v9-v8j"', 'VERSION = "collisionneur-v9-v8k"')

# 2. catalogue
src = remplacer(src, """             "car_par_jeton": 2.5, "delai_s": 5400},  # v9-v8 : niveau « xhigh », aucun budget envoyé
}
""", """             "car_par_jeton": 2.5, "delai_s": 5400},  # v9-v8 : niveau « xhigh », aucun budget envoyé
    # v9-v8k : trois espèces en fin d'ordre. Pages publiques lues le 22 novembre 2026 entre 12:05Z et 12:20Z :
    # - Opus 4.6 : https://platform.claude.com/docs/en/models/opus-4-6/overview , « Model ID: `claude-opus-4-6` »,
    #   « Max output: 128K tokens · Input pricing: $5 / MTok · Output pricing: $25 / MTok » ; même liste dans
    #   https://platform.claude.com/docs/en/about-claude/models/overview (table « All models »).
    # - Fable 5.1 : https://platform.claude.com/docs/en/models/fable-5-1/overview , « Model ID: `claude-fable-5-1` »,
    #   « Max output: 128K tokens · Input pricing: $10 / MTok · Output pricing: $50 / MTok ».
    #   Plafonds par défaut de ces deux espèces : alignés sur Opus 5.5 et Fable 5.2 de la table (choix interne, aucun
    #   relèvement sans --sortie-max) ; délai 3 600 s, aligné sur le même chemin (choix interne, aucune page ne le donne).
    # - Mistral (mistral-large-4-0) : https://docs.mistral.ai/models/mistral-large-4-0.md , « API names: `mistral-large-4`,
    #   `mistral-large-4-0`, `mistral-large-latest` » ; prix 0,70 / 2,10 USD par million (entrée, sortie), page du modèle
    #   https://docs.mistral.ai/models/mistral-large-4-0 (la page https://mistral.ai/pricing ne donne pas de prix pour
    #   Large 4 ; son exemple « Mistral Large costs $0.5 /M tokens in and $1.5 /M tokens out » n'est pas retenu, le plus
    #   haut est pris). Plafond de sortie : AUCUNE page de Mistral ne le donne (contexte « 1M » seulement) : None, valeur à
    #   fixer. Délai : aucune page, aucune espèce du même chemin : None, valeur à fixer. Composition refusée tant que ces
    #   valeurs manquent (VALEURS_A_FIXER).
    "opus46": {"id": "claude-opus-4-6", "fournisseur": "anthropic", "prix": (5.0, 25.0),
               "max": 64000, "max_relance": 64000, "provision": 0, "car_par_jeton": 2.5, "delai_s": 3600},
    "fable51": {"id": "claude-fable-5-1", "fournisseur": "anthropic", "prix": (10.0, 50.0),
                "max": MAX_FABLE_V3, "max_relance": 64000, "provision": 0, "car_par_jeton": 2.5, "delai_s": 3600},
    "mistral": {"id": "mistral-large-4-0", "fournisseur": "mistral", "prix": (0.7, 2.1),
                "max": None, "max_relance": None, "provision": 0, "car_par_jeton": 2.5, "delai_s": None},
}
""")
src = remplacer(src, """ORDRE_CATALOGUE = ("fable", "opus", "argon", "kimi", "astra", "carbon", "neon")
NOMS_CLES = {"gemini": "GEMINI_API_KEY", "openai": "OPENAI_API_KEY", "kimi": None}  # v9-v5 : openai = défaut de --cle-openai
""", """ORDRE_CATALOGUE = ("fable", "opus", "argon", "kimi", "astra", "carbon", "neon",
                   "opus46", "fable51", "mistral")  # v9-v8k : trois espèces en fin d'ordre
NOMS_CLES = {"gemini": "GEMINI_API_KEY", "openai": "OPENAI_API_KEY", "kimi": None,  # v9-v5 : openai = défaut de --cle-openai
             "mistral": "MISTRAL_API_KEY"}  # v9-v8k : défaut de --cle-mistral
# v9-v8k : valeurs sans lesquelles une espèce ne part pas ; None = non trouvée dans les pages publiques, jamais inventée.
VALEURS_A_FIXER = ("id", "prix", "max", "max_relance", "delai_s")
PREFIXE_CLE_MISTRAL = "MISTRAL_API_KEY"
PREFIXES_CLE_KIMI = ("KIMI_API_KEY", "MOONSHOT_API_KEY")
NOM_CLE_KIMI_DEFAUT = "KIMI_API_KEY"
URL_MISTRAL = "https://api.mistral.ai/v1"
URL_KIMI_DIRECT = "https://api.moonshot.ai/v1"
# v9-v8k : interfaces lues le 22 novembre 2026 vers 12:15Z.
# - Mistral, spécification publique https://docs.mistral.ai/openapi.yaml (empreinte 7652f130…, non versée) : POST
#   /v1/chat/completions, champs model, messages, max_tokens, stream ; flux « data-only server-side events […] terminated
#   by a data: [DONE] message » (page https://docs.mistral.ai/api/endpoint/chat) ; morceau CompletionChunk (id, model,
#   usage UsageInfo {prompt_tokens, completion_tokens, total_tokens}, choices[].delta.content, chaîne ou liste de
#   morceaux « text » et « thinking ») ; finish_reason du flux : stop, length, error, tool_calls ; ChatCompletionChoice
#   ajoute model_length ; comptage POST /v1/responses/input_tokens {model, input} → {input_tokens} ; reasoning_effort
#   documenté (none … max) mais non envoyé : aucune page ne dit que mistral-large-4-0 l'accepte.
# - Moonshot (Kimi), https://platform.kimi.ai/docs/api/chat (renvoi depuis platform.moonshot.ai) : serveur
#   https://api.moonshot.ai, POST /v1/chat/completions, jeton « Bearer » ; max_completion_tokens (max_tokens « Deprecated »)
#   « defaults to 131072 and can be set up to 1048576 » pour la série K3 ; flux « Each line starts with `data:` » ,
#   delta.reasoning_content puis delta.content ; stream_options.include_usage : « The final usage chunk has `choices: []`
#   and reports totals in the top-level `usage` » ; fin « data: [DONE] » ; finish_reason stop, length, tool_calls.
#   Comptage : https://platform.kimi.ai/docs/api/estimate.md , POST /v1/tokenizers/estimate-token-count {model, messages}
#   → data.total_tokens, « Estimated total number of tokens » ; la page ne dit pas s'il est gratuit. Prix de Kimi : la
#   page https://platform.kimi.ai/docs/pricing/chat.md n'a pas rendu ses tables : prix de la table inchangés (v8).
# v9-v8k (--sortie-max) : plafond de sortie le plus haut documenté par le fournisseur, par espèce ; None = non documenté.
# - Anthropic : « Max output: 128K tokens » (« Synchronous Messages API limit ») pour Fable 5.2, Opus 5.5, Fable 5.1 et
#   Opus 4.6, https://platform.claude.com/docs/en/about-claude/models/overview , lue le 22 novembre 2026 ; 128K lu 128 000.
# - Astra : « 128,000 max output tokens », https://developers.openai.com/api/docs/models/gpt-6.2-astra , même jour.
# - Kimi : « can be set up to 1048576 » (max_completion_tokens), page de Moonshot ci-dessus ; vaut pour le relais aussi.
# - Google : limites versées de la garde commune (LIMITES_SORTIE, appel en flux), sources dans garde_google_v3.
# - Mistral : aucune page : None (refus nommé « valeur à fixer »).
SORTIE_MAX_DOCUMENTEE = {"fable": 128000, "opus": 128000, "opus46": 128000, "fable51": 128000, "astra": 128000,
                         "kimi": 1048576, "argon": LIMITES_SORTIE["argon"]["flux"],
                         "carbon": LIMITES_SORTIE["carbon"]["flux"], "neon": LIMITES_SORTIE["neon"]["flux"],
                         "mistral": None}
# v9-v8k (--effort-max) : plus haut niveau d'effort documenté chez Anthropic, https://platform.claude.com/docs/en/
# build-with-claude/effort , lue le 22 novembre 2026 : « `max` | Absolute maximum capability […] Available on Claude Fable
# 5.2, […] Claude Fable 5.1, […] Claude Opus 5.5, […] Claude Opus 4.6 » ; envoyé par output_config.effort.
EFFORT_MAX = {"fable": "max", "opus": "max", "opus46": "max", "fable51": "max"}
""")
src = remplacer(src, """NOMBRE_EN_LETTRES = {2: "deux", 3: "trois", 4: "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit", 9: "neuf"}""",
                """NOMBRE_EN_LETTRES = {2: "deux", 3: "trois", 4: "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit", 9: "neuf",
                     10: "dix"}  # v9-v8k""")
src = remplacer(src, """CAR_SORTIE_MAX = {"anthropic": 3.0, "gemini": 4.5, "openai": 4.5, "kimi": 4.5}""",
                """CAR_SORTIE_MAX = {"anthropic": 3.0, "gemini": 4.5, "openai": 4.5, "kimi": 4.5, "mistral": 4.5}  # v9-v8k""")

# 3. composition
src = remplacer(src, """def fixer_composition(especes, nom_cle_anthropic=None, nom_espace_anthropic="ANTHROPIC_WORKSPACE_ID",
                      nom_cle_openai=None):""", """def regler_espece_v8k(m, sortie_max=False, effort_max=False):
    \"\"\"v9-v8k : pose les plafonds au maximum documenté (--sortie-max) et l'effort d'Anthropic (--effort-max), puis refuse
    l'espèce si une valeur manque (« valeur à fixer ») : rien n'est inventé.\"\"\"
    manquantes = []
    if sortie_max:
        plafond = SORTIE_MAX_DOCUMENTEE.get(m["espece"])
        if plafond is None:
            manquantes.append("plafond de sortie maximal documenté (--sortie-max)")
        else:
            m["max"] = m["max_relance"] = plafond
    manquantes = [k for k in VALEURS_A_FIXER if m.get(k) is None] + manquantes
    if m["fournisseur"] == "anthropic":
        m["effort"] = EFFORT_MAX.get(m["espece"]) if effort_max else EFFORT
        if m["effort"] is None:
            manquantes.append("plus haut niveau d'effort documenté (--effort-max)")
    if manquantes:
        raise Arret(CODE_USAGE, f"{m['espece']} ({m['id']}) : valeur à fixer : {', '.join(manquantes)} (non trouvée dans "
                                f"les pages publiques du fournisseur ; jamais inventée) ; l'espèce ne part pas")
    return m


def fixer_composition(especes, nom_cle_anthropic=None, nom_espace_anthropic="ANTHROPIC_WORKSPACE_ID",
                      nom_cle_openai=None, nom_cle_mistral=None, kimi_direct=False, nom_cle_kimi=None,
                      sortie_max=False, effort_max=False):""")
src = remplacer(src, """        raise Arret(CODE_USAGE, "au moins deux espèces, chacune par son option (--fable --opus --argon --kimi --astra "
                                "--carbon --neon) ; aucune n'est implicite")""",
                """        raise Arret(CODE_USAGE, "au moins deux espèces, chacune par son option (--fable --opus --argon --kimi --astra "
                                "--carbon --neon --opus46 --fable51 --mistral) ; aucune n'est implicite")
    if kimi_direct and "kimi" not in choisies:  # v9-v8k : jamais implicite
        raise Arret(CODE_USAGE, "--kimi-direct exige --kimi")""")
src = remplacer(src, """    nom_cle_openai = NOMS_CLES["openai"] if nom_cle_openai is None else nom_cle_openai
    for nom in (nom_cle_anthropic, nom_espace_anthropic, nom_cle_openai):""",
                """    nom_cle_openai = NOMS_CLES["openai"] if nom_cle_openai is None else nom_cle_openai
    nom_cle_mistral = NOMS_CLES["mistral"] if nom_cle_mistral is None else nom_cle_mistral  # v9-v8k
    nom_cle_kimi = NOM_CLE_KIMI_DEFAUT if nom_cle_kimi is None else nom_cle_kimi  # v9-v8k
    for nom in (nom_cle_anthropic, nom_espace_anthropic, nom_cle_openai, nom_cle_mistral, nom_cle_kimi):""")
src = remplacer(src, """                                f"vers un autre fournisseur que le sien)")
    modeles = {}
""", """                                f"vers un autre fournisseur que le sien)")
    if not nom_cle_mistral.startswith(PREFIXE_CLE_MISTRAL):  # v9-v8k : même règle que pour OpenAI
        raise Arret(CODE_USAGE, f"--cle-mistral : le nom doit commencer par {PREFIXE_CLE_MISTRAL} (une clé ne part jamais "
                                f"vers un autre fournisseur que le sien)")
    if not nom_cle_kimi.startswith(PREFIXES_CLE_KIMI):  # v9-v8k
        raise Arret(CODE_USAGE, f"--cle-kimi : le nom doit commencer par {' ou '.join(PREFIXES_CLE_KIMI)} (une clé ne part "
                                f"jamais vers un autre fournisseur que le sien)")
    modeles = {}
""")
src = remplacer(src, """        elif m["fournisseur"] == "openai":  # v9-v5
            m["nom_cle"] = nom_cle_openai
        else:
            m["nom_cle"] = NOMS_CLES[m["fournisseur"]]
""", """        elif m["fournisseur"] == "openai":  # v9-v5
            m["nom_cle"] = nom_cle_openai
        elif m["fournisseur"] == "mistral":  # v9-v8k
            m["nom_cle"] = nom_cle_mistral
        elif m["fournisseur"] == "kimi":  # v9-v8k : relais local (sans clé) ou appel direct, par l'option seule
            m["chemin_appel"] = "direct" if kimi_direct else "relais"
            m["nom_cle"] = nom_cle_kimi if kimi_direct else None
        else:
            m["nom_cle"] = NOMS_CLES[m["fournisseur"]]
        regler_espece_v8k(m, sortie_max, effort_max)  # v9-v8k : avant toute règle qui lit les plafonds
""")
src = remplacer(src, """        modeles["ABCDEFGHI"[i]] = m""", """        modeles["ABCDEFGHIJ"[i]] = m  # v9-v8k : dix espèces au plus""")

# 4. appels
src = remplacer(src, """"output_config": {"effort": EFFORT},""", """"output_config": {"effort": m.get("effort", EFFORT)},""")
src = remplacer(src, """    url = os.environ.get("KIMI_RELAIS_URL", "http://127.0.0.1:8789").rstrip("/") + "/v1/chat/completions"
""", """    if m.get("chemin_appel") == "direct":  # v9-v8k : seulement par --kimi-direct
        return appeler_kimi_direct(m, prompt, max_tokens)
    url = os.environ.get("KIMI_RELAIS_URL", "http://127.0.0.1:8789").rstrip("/") + "/v1/chat/completions"
""")
src = remplacer(src, """def adresse_locale(url):
""", """def cle_par_son_nom(m, option, prefixes):
    \"\"\"v9-v8k : (clé, None) ou (None, motif) ; le nom vient de la composition, jamais de repli sur un autre nom.\"\"\"
    nom_cle = m.get("nom_cle")
    if not nom_cle or not nom_cle.startswith(prefixes):
        return None, f"nom de la variable de la clé absent de la composition ou hors préfixe ({option})"
    cle = os.environ.get(nom_cle)
    if not cle:
        return None, f"{nom_cle} absente (variable nommée par {option})"
    return cle, None


def envoyer_chat_flux(url, corps, m, cle):
    \"\"\"v9-v8k : envoi en flux à une interface de discussion au format chat.completion.chunk (Mistral ; Kimi en appel
    direct). Aucune reprise sauf 429 ; délai de l'espèce tenu ; une coupure, une erreur dans le flux, finish_reason
    « error » ou un flux clos sans finish_reason : envoi interrompu, compté au pire. Pensées (delta.reasoning_content,
    morceaux « thinking ») exclues du texte. Usage lu dans le champ usage d'un morceau (le dernier qui le porte).\"\"\"
    entetes = {"Content-Type": "application/json", "Accept": "text/event-stream", "Authorization": f"Bearer {cle}"}
    requete = urllib.request.Request(url, data=json.dumps(corps, ensure_ascii=False).encode("utf-8"), method="POST",
                                     headers=entetes)
    debut = HORLOGE()
    try:
        flux = envoyer(requete, min(DELAI_INACTIVITE_S, m["delai_s"]), cle)
    except EchecSansEnvoi as e:
        return Reponse(echec=str(e))
    except EnvoiInterrompu as e:
        return Reponse(echec=str(e), interrompue=True)
    texte, types = [], []
    etat = {"servi": None, "id": None, "fin": None, "entree": None, "sortie": None}
    try:
        with flux:
            for d in evenements_sse(flux, debut, m["delai_s"], cle):
                if not isinstance(d, dict):
                    raise EnvoiInterrompu("flux : morceau qui n'est pas un objet")
                if d.get("error") is not None or d.get("object") == "error":
                    raise EnvoiInterrompu(f"erreur dans le flux : "
                                          f"{masquer(json.dumps(d.get('error', d), ensure_ascii=False)[:300], cle)}")
                etat["servi"] = d.get("model") or etat["servi"]
                etat["id"] = d.get("id") or etat["id"]
                u = d.get("usage")
                if isinstance(u, dict):
                    if entier(u.get("prompt_tokens")) is not None:
                        etat["entree"] = u["prompt_tokens"]
                    if entier(u.get("completion_tokens")) is not None:
                        etat["sortie"] = u["completion_tokens"]
                for choix in d.get("choices") or []:
                    if not isinstance(choix, dict):
                        continue
                    delta = choix.get("delta") if isinstance(choix.get("delta"), dict) else {}
                    if delta.get("reasoning_content") and "thinking" not in types:
                        types.append("thinking")
                    contenu = delta.get("content")
                    if isinstance(contenu, str):
                        texte.append(contenu)
                    elif isinstance(contenu, list):
                        for morceau in contenu:
                            if not isinstance(morceau, dict):
                                continue
                            if morceau.get("type", "text") == "text":
                                texte.append(morceau.get("text") or "")
                            elif morceau.get("type") == "thinking" and "thinking" not in types:
                                types.append("thinking")
                    if choix.get("finish_reason"):
                        etat["fin"] = choix["finish_reason"]
            if etat["fin"] is None:
                raise EnvoiInterrompu("flux clos sans finish_reason")
            if etat["fin"] == "error":
                raise EnvoiInterrompu("finish_reason « error » après envoi")
    except EnvoiInterrompu as e:
        return Reponse(texte=avec_brut("".join(texte), e), modele_servi=etat["servi"], identifiant=etat["id"],
                       fin=etat["fin"], types_blocs=types, echec=str(e), interrompue=True,
                       usage={"entree": etat["entree"] or 0, "sortie": etat["sortie"] or 0})
    lu = etat["entree"] is not None and etat["sortie"] is not None
    return Reponse(texte="".join(texte), modele_servi=etat["servi"], identifiant=etat["id"], fin=etat["fin"],
                   usage={"entree": etat["entree"] or 0, "sortie": etat["sortie"] or 0}, types_blocs=types + ["text"],
                   usage_lu=lu)


def appeler_mistral(m, prompt, max_tokens):
    \"\"\"v9-v8k : interface de discussion de Mistral en flux ; clé lue dans la variable nommée par --cle-mistral, jamais
    affichée ; aucun réglage de réflexion envoyé (aucune page ne dit que le modèle l'accepte).\"\"\"
    cle, motif = cle_par_son_nom(m, "--cle-mistral", PREFIXE_CLE_MISTRAL)
    if cle is None:
        return Reponse(echec=motif)
    corps = {"model": m["id"], "messages": [{"role": "user", "content": prompt}], "max_tokens": max_tokens,
             "stream": True}
    return envoyer_chat_flux(URL_MISTRAL + "/chat/completions", corps, m, cle)


def appeler_kimi_direct(m, prompt, max_tokens):
    \"\"\"v9-v8k : interface de Moonshot en flux (--kimi-direct) ; clé lue dans la variable nommée par --cle-kimi ;
    max_completion_tokens (max_tokens est déprécié) ; usage demandé par stream_options.include_usage.\"\"\"
    cle, motif = cle_par_son_nom(m, "--cle-kimi", PREFIXES_CLE_KIMI)
    if cle is None:
        return Reponse(echec=motif)
    corps = {"model": m["id"], "messages": [{"role": "user", "content": prompt}], "max_completion_tokens": max_tokens,
             "stream": True, "stream_options": {"include_usage": True}}
    return envoyer_chat_flux(URL_KIMI_DIRECT + "/chat/completions", corps, m, cle)


def adresse_locale(url):
""")
src = remplacer(src, """APPELANTS = {"anthropic": appeler_anthropic, "gemini": appeler_gemini, "kimi": appeler_kimi, "openai": appeler_openai,
""", """APPELANTS = {"anthropic": appeler_anthropic, "gemini": appeler_gemini, "kimi": appeler_kimi, "openai": appeler_openai,
             "mistral": appeler_mistral,  # v9-v8k
""")
src = remplacer(src, """    if fournisseur == "openai":  # v8 ;""", """    if fournisseur == "mistral":  # v9-v8k : aucun refus nommé dans l'interface ; model_length = troncature
        if rep.fin in ("length", "model_length"):
            return "TRONQUE" if plein else "VIDE"
        if rep.fin == "stop":
            return "OK" if plein else "VIDE"
        return "ANOMALIE"
    if fournisseur == "openai":  # v8 ;""")

# 5. comptage
src = remplacer(src, """    n = entier(rep.get(champ)) if isinstance(rep, dict) else None
""", """    valeur = rep  # v9-v8k : `champ` peut être un chemin (tuple), par exemple ("data", "total_tokens")
    for nom_champ in (champ if isinstance(champ, tuple) else (champ,)):
        valeur = valeur.get(nom_champ) if isinstance(valeur, dict) else None
    n = entier(valeur)
""")
src = remplacer(src, """COMPTEURS = {"anthropic": compter_anthropic, "gemini": compter_gemini, "openai": compter_openai}
SOURCES_COMPTE = {"anthropic": "count_tokens d'Anthropic", "gemini": "countTokens de Google",
""", """def compter_mistral(m, prompt):
    \"\"\"v9-v8k : POST /v1/responses/input_tokens de Mistral {model, input} → input_tokens ; clé par --cle-mistral.\"\"\"
    cle, motif = cle_par_son_nom(m, "--cle-mistral", PREFIXE_CLE_MISTRAL)
    if cle is None:
        raise RefusCompte("COMPTE_IMPOSSIBLE", motif)
    requete = urllib.request.Request(URL_MISTRAL + "/responses/input_tokens",
                                     data=json.dumps({"model": m["id"], "input": prompt}, ensure_ascii=False).encode(
                                         "utf-8"), method="POST",
                                     headers={"Content-Type": "application/json", "Authorization": f"Bearer {cle}"})
    return lire_compte(requete, "input_tokens", cle)


def compter_kimi_direct(m, prompt):
    \"\"\"v9-v8k : POST /v1/tokenizers/estimate-token-count de Moonshot {model, messages} → data.total_tokens.\"\"\"
    cle, motif = cle_par_son_nom(m, "--cle-kimi", PREFIXES_CLE_KIMI)
    if cle is None:
        raise RefusCompte("COMPTE_IMPOSSIBLE", motif)
    corps = {"model": m["id"], "messages": [{"role": "user", "content": prompt}]}
    requete = urllib.request.Request(URL_KIMI_DIRECT + "/tokenizers/estimate-token-count",
                                     data=json.dumps(corps, ensure_ascii=False).encode("utf-8"), method="POST",
                                     headers={"Content-Type": "application/json", "Authorization": f"Bearer {cle}"})
    return lire_compte(requete, ("data", "total_tokens"), cle)


COMPTEURS = {"anthropic": compter_anthropic, "gemini": compter_gemini, "openai": compter_openai,
             "mistral": compter_mistral}  # v9-v8k
SOURCES_COMPTE = {"anthropic": "count_tokens d'Anthropic", "gemini": "countTokens de Google",
                  "mistral": "responses/input_tokens de Mistral",  # v9-v8k
""")
src = remplacer(src, """    compteur = COMPTEURS.get(m["fournisseur"])
    if compteur is None:""", """    direct = m.get("chemin_appel") == "direct"  # v9-v8k : Kimi en appel direct, compté par Moonshot
    compteur = compter_kimi_direct if direct else COMPTEURS.get(m["fournisseur"])
    if compteur is None:""")
src = remplacer(src, """    return {"compte": compte, "garde": garde_entree(compte), "interface": True, "source": SOURCES_COMPTE[m["fournisseur"]]}
""", """    if direct:  # v9-v8k : compte « estimé » par Moonshot : garde au plus grand du compte toléré et de l'estimation prudente
        return {"compte": compte, "garde": max(garde_entree(compte), math.ceil(len(prompt) / m["car_par_jeton"])),
                "interface": True, "source": f"estimate-token-count de Moonshot, garde au plus grand du compte toléré et "
                                             f"de l'estimation à {m['car_par_jeton']:g} caractères par jeton"}
    return {"compte": compte, "garde": garde_entree(compte), "interface": True, "source": SOURCES_COMPTE[m["fournisseur"]]}
""")

# 6. jugement et journal
src = remplacer(src, """    if m["provision"] and rep.usage.get("sortie", 0) > sortie_comptee:""",
                """    sortie_gardee = m["provision"] or m["fournisseur"] == "mistral" or m.get("chemin_appel") == "direct"  # v9-v8k
    if sortie_gardee and rep.usage.get("sortie", 0) > sortie_comptee:""")
src = remplacer(src, """                  "effort": EFFORT if m["fournisseur"] == "anthropic" else None, "usage": rep.usage,""",
                """                  "effort": m.get("effort", EFFORT) if m["fournisseur"] == "anthropic" else None,  # v9-v8k
                  "chemin_appel": m.get("chemin_appel"), "usage": rep.usage,  # v9-v8k""")
src = remplacer(src, """                      f"{m['car_par_jeton']:g} caractères par jeton, délai {m['delai_s']} s")""",
                """                      f"{m['car_par_jeton']:g} caractères par jeton, délai {m['delai_s']} s"
                      + (f", effort {m['effort']}" if m.get("effort") else "")  # v9-v8k
                      + (f", appel {m['chemin_appel']}" if m.get("chemin_appel") else ""))""")

# 7. ligne de commande
src = remplacer(src, """def especes_demandees(a):
""", """def ajouter_options_v8k(s, etage=True):
    \"\"\"v9-v8k : plafonds au maximum documenté, effort maximal ; pour les étages, clés de Mistral et de Kimi et chemin de
    Kimi.\"\"\"
    s.add_argument("--sortie-max", action="store_true",
                   help="plafonds de sortie au maximum documenté de chaque espèce (sources dans le script)")
    s.add_argument("--effort-max", action="store_true", help="effort « max » chez Anthropic (output_config.effort)")
    if etage:
        s.add_argument("--cle-mistral", default=NOMS_CLES["mistral"],
                       help="NOM de la variable qui porte la clé de Mistral (commence par MISTRAL_API_KEY)")
        s.add_argument("--cle-kimi", default=NOM_CLE_KIMI_DEFAUT,
                       help="NOM de la variable qui porte la clé de Moonshot pour --kimi-direct")
        s.add_argument("--kimi-direct", action="store_true",
                       help="Kimi par l'interface de Moonshot au lieu du relais local (journalisé)")


def declarer_options(dossier, a):
    \"\"\"v9-v8k : options d'appel de ce lancement et réglages qui en découlent, à l'écran, et au journal quand ils
    changent (chaque essai porte aussi son chemin d'appel et son effort).\"\"\"
    reglages = {l: {"espece": MODELES[l]["espece"], "max": MODELES[l]["max"], "max_relance": MODELES[l]["max_relance"],
                    "effort": MODELES[l].get("effort"), "chemin_appel": MODELES[l].get("chemin_appel")} for l in LETTRES}
    options = {"kimi_direct": a.kimi_direct, "sortie_max": a.sortie_max, "effort_max": a.effort_max,
               "reglages": reglages}
    deja = [e["options_appel_v8k"] for e in lire_journal(dossier) if "options_appel_v8k" in e]
    if not deja or deja[-1] != options:  # écrit au premier lancement et à chaque changement ; une relance identique
        ajouter_journal(dossier, {"options_appel_v8k": options,  # n'écrit rien (journal inchangé)
                                  "quand": maintenant(), "script": VERSION})
    for l in LETTRES:
        if MODELES[l].get("chemin_appel"):
            print(f"Kimi ({l}) : appel {'DIRECT à l’interface de Moonshot (--kimi-direct)' if a.kimi_direct else 'par le relais local'} "
                  f"(journalisé)", flush=True)
    if a.sortie_max or a.effort_max:
        print(f"Options : sortie maximale {a.sortie_max}, effort maximal {a.effort_max} (journalisé)", flush=True)


def especes_demandees(a):
""")
src = remplacer(src, """    d.add_argument("--jev", action="store_true")
""", """    d.add_argument("--jev", action="store_true")
    ajouter_options_v8k(d, etage=False)  # v9-v8k : le devis compte les plafonds de --sortie-max
""")
src = remplacer(src, """        s.add_argument("--go-ligne", default=None, help="GO-AAAA-MM-JJ-NN qui accorde la ligne de reprise")
""", """        s.add_argument("--go-ligne", default=None, help="GO-AAAA-MM-JJ-NN qui accorde la ligne de reprise")
        ajouter_options_v8k(s)  # v9-v8k
""")
src = remplacer(src, """            fixer_composition(especes_demandees(a))
            devis(a.faits, a.question, a.jev)""", """            fixer_composition(especes_demandees(a), sortie_max=a.sortie_max, effort_max=a.effort_max)  # v9-v8k
            devis(a.faits, a.question, a.jev)""")
src = remplacer(src, """        fixer_composition(especes_demandees(a), a.cle_anthropic, a.nom_espace_anthropic, a.cle_openai)  # v9-v5
""", """        fixer_composition(especes_demandees(a), a.cle_anthropic, a.nom_espace_anthropic, a.cle_openai,  # v9-v5
                          nom_cle_mistral=a.cle_mistral, kimi_direct=a.kimi_direct, nom_cle_kimi=a.cle_kimi,
                          sortie_max=a.sortie_max, effort_max=a.effort_max)  # v9-v8k
""")
src = remplacer(src, """        declarer_script(dossier, a.reprise)  # v9-v3
""", """        declarer_script(dossier, a.reprise)  # v9-v3
        declarer_options(dossier, a)  # v9-v8k
""")

assert src.count("def fixer_composition(") == 1 and src.count("def appeler_mistral(") == 1
(D / "collisionneur_v9_v8k.py").write_text(src, encoding="utf-8")
print("écrit", hashlib.sha256(src.encode()).hexdigest())
