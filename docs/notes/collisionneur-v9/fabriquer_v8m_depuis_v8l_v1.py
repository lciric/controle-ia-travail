"""Fabrique collisionneur_v9_v8m.py depuis la v8l par remplacements exacts (chaque ancien texte présent une seule fois)."""
import hashlib, sys
from pathlib import Path
D = Path("/home/user/controle-ia-travail/docs/notes/collisionneur-v9")
src = (D / "collisionneur_v9_v8l.py").read_text(encoding="utf-8")
assert hashlib.sha256(src.encode()).hexdigest().startswith("da282cf7")


def remplacer(t, ancien, nouveau):
    n = t.count(ancien)
    if n != 1:
        sys.exit(f"ancien texte trouvé {n} fois : {ancien[:80]!r}")
    return t.replace(ancien, nouveau)


src = remplacer(src, """#   « déclaré absent » dans le refus. Détail : rapport-developpeur-collisionneur-v9-v8l-v1.md, même dossier.
""", """#   « déclaré absent » dans le refus. Détail : rapport-developpeur-collisionneur-v9-v8l-v1.md, même dossier.
# v9-v8m (même développeur, 22 novembre 2026) : copie du v9-v8l (da282cf7…, inchangé, R12), sur une règle neuve de
#   l'arbitre. Changements, et seulement ceux-là : (1) chez Anthropic, sous --effort-max, un essai fini en max_tokens sans
#   aucun texte est rejoué une fois, une seule, à l'effort REJEU_EFFORT (« xhigh » ; Opus 4.6, qui n'a pas « xhigh » :
#   « high »), déclaré au journal (rejeu_effort_xhigh_declare) et à l'écran avant l'envoi ; le rejeu prend la place de la
#   relance restante, ou vient en troisième essai après une relance ; un rejeu encore sans texte est un défaut de réglage
#   (code 9), rien n'est écrit ; deux relances au pire dans le devis de reprise ; (2) Opus 4.6 : réflexion adaptative
#   toujours, effort « high » par défaut, « max » seulement avec --effort-max. Détail :
#   rapport-developpeur-collisionneur-v9-v8m-v1.md, même dossier.
""")
src = remplacer(src, 'VERSION = "collisionneur-v9-v8l"', 'VERSION = "collisionneur-v9-v8m"')

# (2) Opus 4.6
src = remplacer(src, """               # adaptative (« Adaptive (extended deprecated) », page du modèle) et effort « max » (page « Effort »)
               "reflexion": "adaptive", "effort_defaut": "max"},""",
                """               # adaptative (« Adaptive (extended deprecated) », page du modèle). v9-v8m (arbitre) : effort « high »
               # par défaut, comme les autres ; « max » seulement avec --effort-max
               "reflexion": "adaptive"},""")

# (1) table du rejeu
src = remplacer(src, """# v9-v8l (B2) : délai total d'un envoi sous --sortie-max, par espèce.""",
                """# v9-v8m (règle de l'arbitre) : effort du rejeu unique après max_tokens sans texte, sous --effort-max. Page
# https://platform.claude.com/docs/en/build-with-claude/effort , lue le 22 novembre 2026 : « `xhigh` | Extended capability
# for long-horizon work. Available on Claude Fable 5.2, […] Claude Fable 5.1, […] Claude Opus 5.5, […] » ; Opus 4.6 n'y
# est pas (« Not every model that supports `max` supports `xhigh` ») : pour lui, le plus haut niveau documenté sous
# « max » est « high ».
REJEU_EFFORT = {"fable": "xhigh", "opus": "xhigh", "fable51": "xhigh", "opus46": "high"}
# v9-v8l (B2) : délai total d'un envoi sous --sortie-max, par espèce.""")

# (1) exécution
src = remplacer(src, """        envoi_m, correction = m, None
""", """        envoi_m, correction = m, None
        if genre == "rejeu_xhigh":  # v9-v8m : effort abaissé pour ce seul essai
            envoi_m = dict(m, effort=REJEU_EFFORT[m["espece"]])
""")
src = remplacer(src, """        if dernier_recours:  # (K-1) déclaré au journal et à l'écran avant l'envoi, jamais silencieux""",
                """        if genre == "rejeu_xhigh":  # v9-v8m : déclaré au journal et à l'écran, après les gardes, avant l'envoi
            ajouter_journal(dossier, {"rejeu_effort_xhigh_declare": cid, "de": m.get("effort"),
                                      "vers": envoi_m["effort"], "plafond": max_tokens, "quand": maintenant(),
                                      "script": VERSION})
            print(f"    REJEU DÉCLARÉ : max_tokens sans texte à l'effort {m.get('effort')!r} ; rejeu unique à l'effort "
                  f"{envoi_m['effort']!r}, plafond {max_tokens} (journalisé)", flush=True)
        if dernier_recours:  # (K-1) déclaré au journal et à l'écran avant l'envoi, jamais silencieux""")
src = remplacer(src, """        statut, cout_usd = juger(m, rep, prompt, pire, compte["garde"], max_tokens)  # v9-v7 (V-1)
""", """        statut, cout_usd = juger(m, rep, prompt, pire, compte["garde"], max_tokens)  # v9-v7 (V-1)
        if genre == "rejeu_xhigh" and statut == "VIDE" and rep.fin == "max_tokens":  # v9-v8m : défaut, rien n'est écrit
            statut = STATUT_REGLAGE
""")
src = remplacer(src, """                  "effort": m.get("effort", EFFORT) if m["fournisseur"] == "anthropic" else m.get("effort"),""",
                """                  "effort": envoi_m.get("effort", EFFORT) if m["fournisseur"] == "anthropic" else m.get("effort"),
                  "rejeu_effort_xhigh": genre == "rejeu_xhigh",  # v9-v8m""")
src = remplacer(src, """        if statut not in ("VIDE", "TRONQUE"):
            return statut  # REFUS ou ANOMALIE : pas de relance, la décision revient à l'arbitre
        i += 1
    return statut
""", """        if statut not in ("VIDE", "TRONQUE"):
            return statut  # REFUS ou ANOMALIE : pas de relance, la décision revient à l'arbitre
        if (rejeu_permis(m) and genre != "rejeu_xhigh" and statut == "VIDE"  # v9-v8m : le rejeu prend la place
                and rep.fin == "max_tokens"):  # de la relance restante (ou vient après la relance) ; une seule fois
            plan = plan[:i + 1] + [(m["max_relance"], "rejeu_xhigh")]
        i += 1
    return statut


def rejeu_permis(m):
    \"\"\"v9-v8m : vrai chez Anthropic sous --effort-max (option de la composition).\"\"\"
    return m["fournisseur"] == "anthropic" and OPTIONS_COMPOSITION["effort_max"] and m["espece"] in REJEU_EFFORT


def nombre_relances(m):
    \"\"\"v9-v8m : relances payées au plus après le premier essai : deux chez Google à plafonds égaux (relance identique,
    puis dernier recours) et chez Anthropic sous --effort-max (relance, puis rejeu) ; une ailleurs.\"\"\"
    if m["fournisseur"] == "gemini" and reglage_de_relance(m)[1]:
        return 2
    return 2 if rejeu_permis(m) else 1
""")
src = remplacer(src, """    dernier = essais[-1]
""", """    dernier = essais[-1]
    if dernier.get("rejeu_effort_xhigh"):  # v9-v8m : rejeu encore sans texte, même réglage : jamais renvoyé
        return (dernier["statut"] == STATUT_REGLAGE and dernier.get("effort") == REJEU_EFFORT.get(m["espece"])
                and max(m["max"], m["max_relance"]) <= dernier.get("max_tokens", 0))
""")
src = remplacer(src, """            relances = 2 if m["fournisseur"] == "gemini" and reglage_de_relance(m)[1] else 1""",
                """            relances = nombre_relances(m)  # v9-v8m : deux aussi chez Anthropic sous --effort-max""")
src = remplacer(src, """                  f"Google à plafonds égaux : relance identique, puis dernier recours ; une ailleurs ; refusé avant \"""",
                """                  f"Google à plafonds égaux : relance identique, puis dernier recours ; deux chez Anthropic sous "
                  f"--effort-max : relance, puis rejeu ; une ailleurs ; refusé avant \"""")
assert src.count("def nombre_relances(") == 1
(D / "collisionneur_v9_v8m.py").write_text(src, encoding="utf-8")
print("écrit", hashlib.sha256(src.encode()).hexdigest())
