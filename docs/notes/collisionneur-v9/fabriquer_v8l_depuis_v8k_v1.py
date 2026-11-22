"""Fabrique collisionneur_v9_v8l.py depuis la v8k par remplacements exacts (chaque ancien texte présent une seule fois)."""
import hashlib, sys
from pathlib import Path
D = Path("/home/user/controle-ia-travail/docs/notes/collisionneur-v9")
src = (D / "collisionneur_v9_v8k.py").read_text(encoding="utf-8")
assert hashlib.sha256(src.encode()).hexdigest().startswith("cc886ae7")


def remplacer(t, ancien, nouveau):
    n = t.count(ancien)
    if n != 1:
        sys.exit(f"ancien texte trouvé {n} fois : {ancien[:80]!r}")
    return t.replace(ancien, nouveau)


src = remplacer(src, """#   Détail : rapport-developpeur-collisionneur-v9-v8k-v1.md, même dossier.
""", """#   Détail : rapport-developpeur-collisionneur-v9-v8k-v1.md, même dossier.
# v9-v8l (même développeur, 22 novembre 2026) : copie du v9-v8k (cc886ae7…, inchangé, R12), corrigée selon la contre-lecture
#   verification-collisionneur-v9-v8k-opus-v1.md et les décisions de l'arbitre du 22 novembre. Changements, et seulement
#   ceux-là : (B1) Kimi borné à 128 000 jetons sous --sortie-max ; (B2) délais sous --sortie-max, table DELAIS_SORTIE_MAX,
#   10 800 s pour toutes les espèces, SUPPOSÉS (accordés par l'arbitre le 22 novembre), journalisés au lancement et à chaque
#   essai ; Astra : l'échéance des relevés suit la même valeur ; (B3) Opus 4.6 : réflexion adaptative
#   (thinking.type « adaptive ») et effort « max » ; (B4) absence d'effort déclarée (Astra, relais de Kimi) sous
#   --effort-max, rien n'est envoyé ; (N2) toute redirection refusée dans `ouvrir`, sur tous les chemins (envois, comptages,
#   relevés, lot, Jev) : refus nommé, l'en-tête d'autorisation ne suit jamais ; (N3) --cle-anthropic refuse les préfixes
#   des autres fournisseurs ; (N4) Kimi direct sous --effort-max : reasoning_effort « max » ; (N6) --sortie-max et
#   --effort-max scellés dans especes.json (seulement s'ils sont donnés) et relus par verifier et devis-reprise ; Mistral
#   « déclaré absent » dans le refus. Détail : rapport-developpeur-collisionneur-v9-v8l-v1.md, même dossier.
""")
src = remplacer(src, 'VERSION = "collisionneur-v9-v8k"', 'VERSION = "collisionneur-v9-v8l"')

# B3 : Opus 4.6
src = remplacer(src, """    "opus46": {"id": "claude-opus-4-6", "fournisseur": "anthropic", "prix": (5.0, 25.0),
               "max": 64000, "max_relance": 64000, "provision": 0, "car_par_jeton": 2.5, "delai_s": 3600},""",
                """    "opus46": {"id": "claude-opus-4-6", "fournisseur": "anthropic", "prix": (5.0, 25.0),
               "max": 64000, "max_relance": 64000, "provision": 0, "car_par_jeton": 2.5, "delai_s": 3600,
               # v9-v8l (B3, décision de l'arbitre) : sans champ de réflexion, Opus 4.6 ne réfléchit pas ; réflexion
               # adaptative (« Adaptive (extended deprecated) », page du modèle) et effort « max » (page « Effort »)
               "reflexion": "adaptive", "effort_defaut": "max"},""")

# B1, B2 : plafond de Kimi, délais sous --sortie-max
src = remplacer(src, """                         "kimi": 1048576, "argon": LIMITES_SORTIE["argon"]["flux"],""",
                """                         "kimi": 128000,  # v9-v8l (B1, arbitre) : documenté 1 048 576, borné à 128 000
                         "argon": LIMITES_SORTIE["argon"]["flux"],""")
src = remplacer(src, """EFFORT_MAX = {"fable": "max", "opus": "max", "opus46": "max", "fable51": "max"}
""", """EFFORT_MAX = {"fable": "max", "opus": "max", "opus46": "max", "fable51": "max"}
# v9-v8l (B2) : délai total d'un envoi sous --sortie-max, par espèce. SUPPOSÉ : aucun fournisseur ne documente de débit ;
# 10 800 s pour toutes, accordé par l'arbitre le 22 novembre 2026 ; journalisé au lancement et à chaque essai. Astra :
# échéance des relevés de l'arrière-plan. Une coupure ou un délai dépassé reste un défaut, compté au pire. Mistral :
# déclaré absent.
DELAIS_SORTIE_MAX = {"fable": 10800, "opus": 10800, "argon": 10800, "kimi": 10800, "astra": 10800, "carbon": 10800,
                     "neon": 10800, "opus46": 10800, "fable51": 10800, "mistral": None}
# v9-v8l (N4) : Kimi K3.1 Pro, https://platform.kimi.ai/docs/api/chat , lue le 22 novembre 2026 : « uses the top-level
# `reasoning_effort` field (`"low"`, `"high"`, or `"max"`; default `"max"`) » ; envoyé seulement en appel direct.
EFFORT_MAX_KIMI = "max"
# v9-v8l (B4) : espèces sans réglage d'effort documenté ou connu : l'absence est déclarée, rien n'est envoyé.
EFFORT_ABSENT = {"openai": "aucun niveau d'effort de raisonnement documenté pour gpt-6.2-astra (page du modèle : seul « none »"
                           " est dit rejeté) ; rien n'est envoyé",
                 "kimi": "relais local : aucun réglage d'effort connu du relais ; rien n'est envoyé (défaut de Moonshot : "
                         "« max »)"}
# v9-v8l (N3) : --cle-anthropic ne peut pas nommer la clé d'un autre fournisseur.
PREFIXES_AUTRES_FOURNISSEURS = ("OPENAI_API_KEY", "MISTRAL_API_KEY", "KIMI_API_KEY", "MOONSHOT_API_KEY", "GEMINI_API_KEY",
                                "TYPESAFE_API_KEY")
# v9-v8l (N6) : options scellées avec la composition (fixées par fixer_composition).
OPTIONS_COMPOSITION = {"sortie_max": False, "effort_max": False}
""")
src = remplacer(src, """    manquantes = []
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
""", """    manquantes = []
    if sortie_max:
        plafond = SORTIE_MAX_DOCUMENTEE.get(m["espece"])
        if plafond is None:
            manquantes.append("plafond de sortie maximal documenté (--sortie-max)")
        else:
            m["max"] = m["max_relance"] = plafond
        delai = DELAIS_SORTIE_MAX.get(m["espece"])  # v9-v8l (B2) : SUPPOSÉ, accordé par l'arbitre
        if delai is None:
            manquantes.append("délai sous --sortie-max")
        else:
            m["delai_s"], m["delai_suppose"] = delai, True
    manquantes = [k for k in VALEURS_A_FIXER if m.get(k) is None] + manquantes
    if m["fournisseur"] == "anthropic":
        m["effort"] = EFFORT_MAX.get(m["espece"]) if effort_max else m.get("effort_defaut", EFFORT)  # v9-v8l (B3)
        if m["effort"] is None:
            manquantes.append("plus haut niveau d'effort documenté (--effort-max)")
    elif effort_max and m.get("chemin_appel") == "direct":  # v9-v8l (N4)
        m["effort"] = EFFORT_MAX_KIMI
    elif effort_max and m["fournisseur"] in EFFORT_ABSENT:  # v9-v8l (B4) : absence déclarée
        m["effort_absent"] = EFFORT_ABSENT[m["fournisseur"]]
    if manquantes:
        raise Arret(CODE_USAGE, f"{m['espece']} ({m['id']}) : valeur à fixer : {', '.join(manquantes)} ; déclaré absent "
                                f"(aucune valeur lue sur une page du fournisseur ; jamais inventée) ; l'espèce ne part pas")
    return m
""")
src = remplacer(src, """    global MODELES, LETTRES
""", """    global MODELES, LETTRES, OPTIONS_COMPOSITION
""")
src = remplacer(src, """    for nom in (nom_cle_anthropic, nom_espace_anthropic, nom_cle_openai, nom_cle_mistral, nom_cle_kimi):""",
                """    if nom_cle_anthropic is not None and nom_cle_anthropic.startswith(PREFIXES_AUTRES_FOURNISSEURS):  # v9-v8l (N3)
        raise Arret(CODE_USAGE, "--cle-anthropic : ce nom est celui de la clé d'un autre fournisseur (une clé ne part "
                                "jamais vers un autre fournisseur que le sien)")
    for nom in (nom_cle_anthropic, nom_espace_anthropic, nom_cle_openai, nom_cle_mistral, nom_cle_kimi):""")
src = remplacer(src, """    MODELES, LETTRES = modeles, tuple(modeles)
    return modeles


def description_composition():
    return {"especes": [MODELES[l]["espece"] for l in LETTRES],
            "lettres": {l: {"espece": MODELES[l]["espece"], "id": MODELES[l]["id"]} for l in LETTRES}}
""", """    MODELES, LETTRES = modeles, tuple(modeles)
    OPTIONS_COMPOSITION = {"sortie_max": bool(sortie_max), "effort_max": bool(effort_max)}  # v9-v8l (N6)
    return modeles


def description_composition():
    d = {"especes": [MODELES[l]["espece"] for l in LETTRES],
         "lettres": {l: {"espece": MODELES[l]["espece"], "id": MODELES[l]["id"]} for l in LETTRES}}
    if any(OPTIONS_COMPOSITION.values()):  # v9-v8l (N6) : scellées seulement si données (anciens runs inchangés)
        d["options"] = dict(OPTIONS_COMPOSITION)
    return d
""")
src = remplacer(src, """            raise Arret(CODE_USAGE, "espèces données différentes de celles du run (especes.json) : un run garde ses "
                                    "espèces ; redonne les mêmes options, ou ouvre un nouveau dossier")""",
                """            raise Arret(CODE_USAGE, "espèces ou options (--sortie-max, --effort-max) données différentes de celles du "
                                    "run (especes.json) : un run garde ses espèces et ces options ; redonne les mêmes "
                                    "options, ou ouvre un nouveau dossier")""")
src = remplacer(src, """    texte, _ = lire_sceau(Path(dossier) / "especes.json")
    fixer_composition(json.loads(texte)["especes"])
""", """    texte, _ = lire_sceau(Path(dossier) / "especes.json")
    compo = json.loads(texte)
    options = compo.get("options") or {}  # v9-v8l (N6) : options scellées relues (verifier, devis-reprise)
    fixer_composition(compo["especes"], sortie_max=bool(options.get("sortie_max")),
                      effort_max=bool(options.get("effort_max")))
""")

# N2 : redirections
src = remplacer(src, """def ouvrir(requete, delai, locale=False):""", """class RedirectionRefusee(Exception):
    \"\"\"v9-v8l (N2) : le serveur a répondu par une redirection ; elle n'est jamais suivie (l'en-tête d'autorisation ne part
    vers aucun autre lieu). Refus nommé.\"\"\"


class RefusRedirection(urllib.request.HTTPRedirectHandler):
    \"\"\"v9-v8l (N2) : remplace le gestionnaire par défaut (301, 302, 303, 307, 308) ; toute redirection lève
    RedirectionRefusee avant qu'une seconde requête parte.\"\"\"

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise RedirectionRefusee(f"redirection refusée (HTTP {code}) depuis {urllib.parse.urlsplit(req.full_url).hostname} "
                                 f"vers {urllib.parse.urlsplit(newurl).hostname} : jamais suivie")


def ouvrir(requete, delai, locale=False):""")
src = remplacer(src, """    gestionnaires = [urllib.request.HTTPSHandler(context=contexte)]
""", """    gestionnaires = [urllib.request.HTTPSHandler(context=contexte), RefusRedirection()]  # v9-v8l (N2)
""")
src = remplacer(src, """            return (transport or TRANSPORT)(requete, delai, locale)
        except urllib.error.HTTPError as e:
""", """            return (transport or TRANSPORT)(requete, delai, locale)
        except RedirectionRefusee as e:  # v9-v8l (N2) : refus nommé, rien n'est suivi ni renvoyé
            raise EchecSansEnvoi(f"REDIRECTION_REFUSEE : {e}")
        except urllib.error.HTTPError as e:
            if 300 <= e.code < 400:  # v9-v8l (N2) : redirection non suivie par urllib (300, 304, 305…) : même refus
                raise EchecSansEnvoi(f"REDIRECTION_REFUSEE : redirection refusée (HTTP {e.code}) : jamais suivie")
""")
src = remplacer(src, """        except CorpsIllisible as e:  # v9-v8 (C-2) : relevé illisible, gardé si l'envoi finit sans réponse
            manques, dernier_brut = manques + 1, masquer(e.brut, cle)
        except (OSError, http.client.HTTPException, ValueError):
            manques += 1""", """        except CorpsIllisible as e:  # v9-v8 (C-2) : relevé illisible, gardé si l'envoi finit sans réponse
            manques, dernier_brut = manques + 1, masquer(e.brut, cle)
        except RedirectionRefusee as e:  # v9-v8l (N2) : refus nommé ; la création est partie : compté au pire
            note = annuler_openai(base, locale, rid, entetes, cle)
            return Reponse(modele_servi=rep.get("model"), identifiant=rid, interrompue=True,
                           echec=f"relevé : REDIRECTION_REFUSEE : {e} ; {note}")
        except (OSError, http.client.HTTPException, ValueError):
            manques += 1""")
src = remplacer(src, """        with TRANSPORT(requete, DELAI_RELEVE_S, locale):
            return "annulation demandée"
    except (OSError, http.client.HTTPException, ValueError) as e:""", """        with TRANSPORT(requete, DELAI_RELEVE_S, locale):
            return "annulation demandée"
    except (OSError, http.client.HTTPException, ValueError, RedirectionRefusee) as e:  # v9-v8l (N2)""")

# B3 : corps d'Anthropic ; N4 : corps de Kimi direct
src = remplacer(src, """             "messages": [{"role": "user", "content": prompt}]}
    requete = urllib.request.Request(URL_ANTHROPIC, data=""", """             "messages": [{"role": "user", "content": prompt}]}
    if m.get("reflexion") == "adaptive":  # v9-v8l (B3) : Opus 4.6 seul
        corps["thinking"] = {"type": "adaptive"}
    requete = urllib.request.Request(URL_ANTHROPIC, data=""")
src = remplacer(src, """    return envoyer_chat_flux(URL_KIMI_DIRECT + "/chat/completions", corps, m, cle)""",
                """    if m.get("effort"):  # v9-v8l (N4) : --effort-max seulement
        corps["reasoning_effort"] = m["effort"]
    return envoyer_chat_flux(URL_KIMI_DIRECT + "/chat/completions", corps, m, cle)""")

# journal par essai
src = remplacer(src, """                  "effort": m.get("effort", EFFORT) if m["fournisseur"] == "anthropic" else None,  # v9-v8k
                  "chemin_appel": m.get("chemin_appel"), "usage": rep.usage,  # v9-v8k""",
                """                  "effort": m.get("effort", EFFORT) if m["fournisseur"] == "anthropic" else m.get("effort"),
                  "chemin_appel": m.get("chemin_appel"), "usage": rep.usage,  # v9-v8k
                  "effort_absent": m.get("effort_absent"), "delai_suppose": m.get("delai_suppose", False),  # v9-v8l
                  "reflexion_anthropic": m.get("reflexion"),  # v9-v8l (B3)""")

# devis-reprise (N6)
src = remplacer(src, """            MODELES[l]["max_relance"] = max(CATALOGUE["fable"]["max_relance"], valeur)""",
                """            MODELES[l]["max_relance"] = max(SORTIE_MAX_DOCUMENTEE["fable"] if OPTIONS_COMPOSITION["sortie_max"]
                                            else CATALOGUE["fable"]["max_relance"], valeur)  # v9-v8l (N6)""")
src = remplacer(src, """    lignes = [f"Devis de reprise, {VERSION} ; dossier {Path(dossier).name} ; reste de la ligne {restant:.2f} USD.",""",
                """    lignes = [f"Devis de reprise, {VERSION} ; dossier {Path(dossier).name} ; reste de la ligne {restant:.2f} USD ; "
              f"options scellées du run {OPTIONS_COMPOSITION}.",  # v9-v8l (N6)""")

# lancement
src = remplacer(src, """                    "effort": MODELES[l].get("effort"), "chemin_appel": MODELES[l].get("chemin_appel")} for l in LETTRES}""",
                """                    "effort": MODELES[l].get("effort"), "chemin_appel": MODELES[l].get("chemin_appel"),
                    "delai_s": MODELES[l]["delai_s"], "delai_suppose": MODELES[l].get("delai_suppose", False),  # v9-v8l
                    "effort_absent": MODELES[l].get("effort_absent"), "reflexion": MODELES[l].get("reflexion")}
                for l in LETTRES}""")
src = remplacer(src, """    if a.sortie_max or a.effort_max:
        print(f"Options : sortie maximale {a.sortie_max}, effort maximal {a.effort_max} (journalisé)", flush=True)
""", """    if a.sortie_max or a.effort_max:
        print(f"Options : sortie maximale {a.sortie_max}, effort maximal {a.effort_max} (journalisé)", flush=True)
    for l in LETTRES:  # v9-v8l (B2, B4)
        m = MODELES[l]
        if m.get("delai_suppose"):
            print(f"{l} = {m['espece']} : délai {m['delai_s']} s SUPPOSÉ (--sortie-max, accordé par l'arbitre le "
                  f"22 novembre) (journalisé)", flush=True)
        if m.get("effort_absent"):
            print(f"{l} = {m['espece']} : effort maximal ABSENT : {m['effort_absent']} (journalisé)", flush=True)
""")
assert src.count("class RefusRedirection(") == 1
(D / "collisionneur_v9_v8l.py").write_text(src, encoding="utf-8")
print("écrit", hashlib.sha256(src.encode()).hexdigest())
