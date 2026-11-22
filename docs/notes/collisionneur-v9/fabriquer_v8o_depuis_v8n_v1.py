"""Fabrique collisionneur_v9_v8o.py depuis la v8n par remplacements exacts (chaque ancien texte présent une seule fois)."""
import hashlib, sys
from pathlib import Path
D = Path("/home/user/controle-ia-travail/docs/notes/collisionneur-v9")
src = (D / "collisionneur_v9_v8n.py").read_text(encoding="utf-8")
assert hashlib.sha256(src.encode()).hexdigest().startswith("4bd86e65")


def remplacer(t, ancien, nouveau):
    n = t.count(ancien)
    if n != 1:
        sys.exit(f"ancien texte trouvé {n} fois : {ancien[:80]!r}")
    return t.replace(ancien, nouveau)


src = remplacer(src, """#   neuve pour l'ajout. Détail : rapport-developpeur-collisionneur-v9-v8n-v1.md, même dossier.
""", """#   neuve pour l'ajout. Détail : rapport-developpeur-collisionneur-v9-v8n-v1.md, même dossier.
# v9-v8o (même développeur, 22 novembre 2026) : copie du v9-v8n (4bd86e65…, inchangé, R12), corrigée selon
#   verification-collisionneur-v9-v8n-opus-v1.md. Changements, et seulement ceux-là : avec --espece-ajoutee,
#   --rejuger-essai, --accepter-absence et --accepter-motif sont refusés et --ligne-usd est exigé, avant toute écriture ;
#   une ligne du préambule de l'espèce ajoutée dit qu'elle est ajoutée après coup ; `devis --espece-ajoutee` chiffre les
#   trois cellules de l'ajout. Détail : rapport-developpeur-collisionneur-v9-v8o-v1.md, même dossier.
""")
src = remplacer(src, 'VERSION = "collisionneur-v9-v8n"', 'VERSION = "collisionneur-v9-v8o"')
src = remplacer(src, """    espece = a.espece_ajoutee
""", """    espece = a.espece_ajoutee
    interdites = [nom for nom, valeur in (("--rejuger-essai", a.rejuger_essai), ("--accepter-absence", a.accepter_absence),
                                          ("--accepter-motif", a.accepter_motif)) if valeur]
    if interdites:  # v9-v8o (bloquant 1) : elles écriraient dans les cellules ou le journal d'origine
        raise Arret(CODE_USAGE, f"--espece-ajoutee : {', '.join(interdites)} refusée(s) avec l'ajout (aucune cellule ni "
                                f"décision d'origine ne change) ; rien n'est écrit")
    if a.ligne_usd is None:  # v9-v8o (bloquant 2) : jamais sur la ligne du run d'origine
        raise Arret(CODE_USAGE, "--espece-ajoutee exige --ligne-usd : une ligne propre à l'ajout, sur GO ; rien n'est "
                                "écrit")
""")
src = remplacer(src, """    morceaux = [preambule().format(lettre=lettre, autres=", ".join(autres(lettre)), mots=TOURS[tour]["mots"],
                                   marqueur=MARQUEUR),
                f"<<<DÉBUT FAITS sha256={h_faits}>>>\\n{faits}\\n<<<FIN FAITS>>>",
                CONSIGNES[tour]]""", """    morceaux = [preambule().format(lettre=lettre, autres=", ".join(autres(lettre)), mots=TOURS[tour]["mots"],
                                   marqueur=MARQUEUR),
                f"<<<DÉBUT FAITS sha256={h_faits}>>>\\n{faits}\\n<<<FIN FAITS>>>",
                CONSIGNES[tour]]
    if AJOUT and lettre == AJOUT["lettre"]:  # v9-v8o : dit à l'espèce ajoutée, juste après le préambule
        morceaux.insert(1, f"La proposition {lettre} est ajoutée après coup : les propositions "
                           f"{', '.join(autres(lettre))} ont écrit leurs tours III sans la connaître.")""")
src = remplacer(src, """def devis(faits, question=None, jev=False):""", """def devis_ajout(faits, question=None):
    \"\"\"v9-v8o : pire cas des trois cellules III de l'espèce ajoutée (AJOUT), même borne que `devis`, plus le pire avec
    relances (nombre_relances, au plafond de relance). Renvoie {"sans_relance", "avec_relances"}.\"\"\"
    n_faits = len(lire_entree(faits))
    n_question = len(lire_entree(question)) if question else 4000
    lettre = AJOUT["lettre"]
    m = MODELES[lettre]
    total, avec, lignes = 0.0, 0.0, [f"Ajout : {lettre} = {m['espece']} ({m['id']}), sortie {m['max']} (relance "
                                    f"{m['max_relance']}), effort {m.get('effort')}"]
    for tour in ORDRE_ETAGE[3]:
        pieces = len(entrees(tour, lettre, []))
        absentes = len(autres(lettre)) if tour == "E3-T3" else 0
        caracteres = n_faits + 6000 + n_question + pieces * TOURS[tour]["mots"] * 7 + absentes * SURCOUT_BLOC
        c = cout_pire_cas(m, caracteres, m["max"])
        r = cout_pire_cas(m, caracteres, m["max_relance"])
        total += c
        avec += c + nombre_relances(m) * r
        lignes.append(f"{id_cellule(tour, lettre):24s} {m['id']:18s} pire cas {c:5.2f} USD (relance {r:5.2f})")
    lignes.append(f"  ajout : 3 cellules, {total:.2f} USD au pire cas sans relance, {avec:.2f} USD avec "
                  f"{nombre_relances(m)} relance(s) par cellule")
    print("\\n".join(lignes))
    return {"sans_relance": total, "avec_relances": avec}


def devis(faits, question=None, jev=False):""")
src = remplacer(src, """    d.add_argument("--jev", action="store_true")
""", """    d.add_argument("--jev", action="store_true")
    d.add_argument("--espece-ajoutee", default=None, help="chiffre les trois cellules III de l'espèce ajoutée")  # v9-v8o
""")
src = remplacer(src, """            fixer_composition(especes_demandees(a), sortie_max=a.sortie_max, effort_max=a.effort_max)  # v9-v8k
            devis(a.faits, a.question, a.jev)""", """            fixer_composition(especes_demandees(a), sortie_max=a.sortie_max, effort_max=a.effort_max)  # v9-v8k
            if a.espece_ajoutee:  # v9-v8o
                if a.espece_ajoutee not in CATALOGUE or a.espece_ajoutee in especes_demandees(a):
                    raise Arret(CODE_USAGE, f"--espece-ajoutee : espèce inconnue ou déjà dans la composition : "
                                            f"{a.espece_ajoutee!r}")
                etendre_composition(a.espece_ajoutee)
                devis_ajout(a.faits, a.question)
            else:
                devis(a.faits, a.question, a.jev)""")
(D / "collisionneur_v9_v8o.py").write_text(src, encoding="utf-8")
print("écrit", hashlib.sha256(src.encode()).hexdigest())
