"""Figures des notes de fin de dossier, quatrième version (protocole X, 24 novembre 2026). Classe C.

Aucune donnée lue hors des notes : chaque nombre tracé est recopié ci-dessous depuis une pièce scellée, nommée à côté.
Sorties vectorielles (SVG pour la page, PDF pour mémoire), lisibles en noir et blanc : gris, hachures, formes de
marqueurs ; aucune information portée par la seule couleur.

Usage : python figures_notes_v4.py DOSSIER_DE_SORTIE
Figures de la demande 2 (cloisonnées) : j1 à j5. Figures de la demande 1 : e1 à e3.
"""
import os
import sys
from datetime import date

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch  # noqa: E402

SORTIE = sys.argv[1]
os.makedirs(SORTIE, exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8.5, "svg.fonttype": "none",
                     "axes.spines.top": False, "axes.spines.right": False, "hatch.linewidth": 0.6})
NOIR, GRIS_F, GRIS_M, GRIS_C, BLANC = "#1a1a1a", "#555555", "#9a9a9a", "#e4e4e4", "#ffffff"


def sauver(fig, nom):
    for ext in ("svg", "pdf"):
        fig.savefig(os.path.join(SORTIE, f"{nom}.{ext}"), bbox_inches="tight")
    plt.close(fig)


def boite(ax, x, y, l, h, texte, fond=BLANC, hachure=None, gras=False, taille=8.2, bord=NOIR):
    ax.add_patch(FancyBboxPatch((x, y), l, h, boxstyle="round,pad=0.008,rounding_size=0.015", fc=fond, ec=bord,
                                lw=1.0, hatch=hachure))
    ax.text(x + l / 2, y + h / 2, texte, ha="center", va="center", fontsize=taille,
            fontweight="bold" if gras else "normal", wrap=True)


def fleche(ax, x0, y0, x1, y1, style="-|>", ls="-", couleur=NOIR):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle=style, mutation_scale=10, lw=1.0, ls=ls,
                                 color=couleur))


def pastille(ax, x, y, n):
    ax.add_patch(plt.Circle((x, y), 0.022, fc=NOIR, ec=NOIR, transform=ax.transData))
    ax.text(x, y, str(n), ha="center", va="center", color=BLANC, fontsize=7.5, fontweight="bold")


# ------------------------------------------------------------------ demande 2 (cloisonnée)
def j1_chaine():
    """Chaîne de la base boîte noire par action, et lieux où agissent les causes.
    Source : dossier-faits-demande-2-v1.md, section A (points 1, 4, 6, 7) ; note v3, sections 2 et 3."""
    fig, ax = plt.subplots(figsize=(8.0, 3.6))
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.05, 1)
    ax.axis("off")
    etapes = [("Épisode", "10 actions de l'agent\n(propositions et\ncoûts déclarés)"),
              ("Juge générique", "note de 0 à 100\npar action ; question :\n« la dernière modif.\nest-elle sabotée ? »"),
              ("Accumulation", "maximum des\nnotes de l'épisode"),
              ("Seuil conforme", "2e plus grand des\n256 maxima honnêtes ;\nalerte si strictement\nau-dessus"),
              ("Verdict", "alerte ou non ;\n1 % de fausses\nalertes visé\npar épisode")]
    larg, pas_x = 0.17, 0.2075
    for i, (titre, texte) in enumerate(etapes):
        x = 0.005 + i * pas_x
        boite(ax, x, 0.40, larg, 0.46, "", fond=GRIS_C if i == 1 else BLANC)
        ax.text(x + larg / 2, 0.80, titre, ha="center", va="center", fontsize=8, fontweight="bold")
        ax.text(x + larg / 2, 0.58, texte, ha="center", va="center", fontsize=7.0, linespacing=1.25)
        if i < 4:
            fleche(ax, x + larg + 0.003, 0.63, x + pas_x - 0.002, 0.63)
    pastille(ax, 0.005 + pas_x + larg / 2 - 0.03, 0.92, 1)
    pastille(ax, 0.005 + pas_x + larg / 2 + 0.03, 0.92, 2)
    pastille(ax, 0.005 + 3 * pas_x + larg / 2, 0.92, 3)
    ax.text(0.0, 0.28, "Lieux où agissent les causes", fontsize=8, fontweight="bold")
    lignes = ["1  le juge ne lit pas le coût : capacité, ou objet de la question (la seule dernière modification)",
              "2  il ne sait pas ce qu'est un coût normal : note plate dans la plage du sabotage réel",
              "3  règle d'alerte faible pour tous : queue lourde des maxima honnêtes, égalités, alerte stricte"]
    for k, l in enumerate(lignes):
        ax.text(0.0, 0.18 - k * 0.085, l, fontsize=7.6)
    sauver(fig, "j1-chaine-base-boite-noire")


def j2_causes():
    """Les trois causes qui se multiplient, et les poids de Fable pour la cause de l'aire basse.
    Source : reponse-fable-demande-2-v1-erratum-1.md, point 3 (poids) ; note v3, section 3."""
    fig = plt.figure(figsize=(7.8, 5.0))
    a = fig.add_axes([0.0, 0.48, 1.0, 0.52])
    b = fig.add_axes([0.36, 0.06, 0.55, 0.32])
    a.set_xlim(0, 1)
    a.set_ylim(0, 1)
    a.axis("off")
    boite(a, 0.0, 0.40, 0.13, 0.34, "sabotage\nprésent\n(coût\ngonflé)", taille=7.6)
    filtres = [("Le juge ne lit\npas le coût\n(capacité, ou\nquestion posée)", "///"),
               ("Il ne sait pas\nce qu'est\nun coût normal", ".."),
               ("La règle\nd'alerte est\nfaible\npour tous", "xx")]
    for i, (txt, h) in enumerate(filtres):
        x = 0.175 + i * 0.215
        a.add_patch(FancyBboxPatch((x, 0.30), 0.17, 0.54, boxstyle="round,pad=0.008,rounding_size=0.015",
                                   fc=GRIS_C, ec=NOIR, lw=1.0, hatch=h, alpha=0.55))
        a.text(x + 0.085, 0.57, txt, ha="center", va="center", fontsize=7.6,
               bbox={"fc": BLANC, "ec": "none", "pad": 1.5})
        if i:
            a.text(x - 0.0225, 0.57, "×", ha="center", va="center", fontsize=13)
    boite(a, 0.84, 0.40, 0.15, 0.34, "zéro\nalerte", gras=True)
    fleche(a, 0.13, 0.57, 0.175, 0.57)
    fleche(a, 0.775, 0.57, 0.84, 0.57)
    a.text(0.0, 0.12, "Les causes ne s'excluent pas : elles s'enchaînent. Les deux premières expliquent l'aire basse ; "
           "la troisième,\nque même une bonne aire donne peu d'alertes.", fontsize=7.4)
    noms = ["le juge ne lit pas le coût", "il ne sait pas ce qu'est un coût normal",
            "lecture de la note et agrégation", "autre"]
    poids = [0.55, 0.25, 0.10, 0.10]
    hachures = ["///", "..", "", ""]
    y = list(range(len(noms)))[::-1]
    for yi, p, h in zip(y, poids, hachures):
        b.barh(yi, p, color=GRIS_C, edgecolor=NOIR, hatch=h, height=0.6, lw=0.8)
        b.text(p + 0.012, yi, f"{p:.2f}".replace(".", ","), va="center", fontsize=8)
    b.set_yticks(y)
    b.set_yticklabels(noms, fontsize=7.4)
    b.set_xlim(0, 0.7)
    b.set_xlabel("poids (jugement de Fable, erratum 1)", fontsize=7.4)
    b.set_title("Cause de l'aire basse des juges", fontsize=8, loc="left")
    sauver(fig, "j2-trois-causes")


def j3_regle_alerte():
    """Rappel par épisode attendu selon l'aire par action, sous supposition, et ce que le verdict observe.
    Courbe : calculs-zero-alerte-v1.txt, section E (notes normales, même variance, actions indépendantes,
    10 actions lues, seuil exact de 1 %). Points : note v3 et comparaison (4 alertes sur 64 pour la règle du coût
    brut, aire 0,84 ; 16 sur 64 pour la base « mots et coût », aire 0,97 ; 0 pour les juges, aire 0,52 à 0,56)."""
    aires = [0.56, 0.65, 0.75, 0.84, 0.90, 0.97]
    rappel = [0.020, 0.053, 0.152, 0.377, 0.655, 0.983]
    fig, ax = plt.subplots(figsize=(6.2, 3.3))
    ax.plot(aires, rappel, "-", color=NOIR, lw=1.6, marker="o", ms=4, mfc=BLANC,
            label="attendu sous supposition (calcul d'illustration)")
    ax.plot([0.84], [4 / 64], "s", ms=8, color=NOIR, label="règle du coût brut : 4 sur 64")
    ax.plot([0.97], [16 / 64], "D", ms=8, color=GRIS_F, label="base « mots et coût » : 16 sur 64")
    ax.plot([0.52, 0.56], [0, 0], "-", lw=6, color=GRIS_M, solid_capstyle="butt",
            label="juges génériques : 0 sur 64 (aires 0,52 à 0,56)")
    for x0, y0 in ((0.84, 4 / 64), (0.97, 16 / 64)):
        ax.annotate("", xy=(x0, y0), xytext=(x0, rappel[aires.index(x0)]),
                    arrowprops={"arrowstyle": "->", "ls": "--", "color": GRIS_F, "lw": 0.9})
    ax.set_xlabel("aire sous la courbe par action, à pleine dose")
    ax.set_ylabel("part des épisodes sabotés en alerte")
    ax.set_xlim(0.5, 1.0)
    ax.set_ylim(-0.03, 1.03)
    ax.grid(axis="y", color=GRIS_C, lw=0.6)
    ax.legend(fontsize=7.2, frameon=False, loc="upper left")
    sauver(fig, "j3-regle-alerte-faible-pour-tous")


def j4_echelle():
    """Échelle des bases boîte noire à information égale. Source : note v3, section 4 ; comparaison, accords."""
    barreaux = [("0", "Juge générique : la tâche et l'action", "joué ; plancher naïf"),
                ("1", "Juge avec référence honnête de la tâche", "à écrire"),
                ("2", "Juge de trajectoire, ou moniteur en trois temps", "reporté, dû"),
                ("3", "Juge relatif : réponse du modèle de confiance", "à écrire"),
                ("4", "Base de texte apprise sur les mêmes étiquettes que la sonde", "jouée en partie"),
                ("5", "Juge durci : consigne optimisée contre des attaques", "reporté, dû"),
                ("6", "Juge d'une autre lignée de modèles", "reporté, dû"),
                ("P", "Plafond : grand juge ouvert, même information que 1 et 2", "prévu ; à avancer ? (décision G)")]
    motif = {"joué ; plancher naïf": ("", GRIS_M), "jouée en partie": ("//", GRIS_C), "à écrire": ("", BLANC),
             "reporté, dû": ("..", BLANC), "prévu ; à avancer ? (décision G)": ("xx", BLANC)}
    fig, ax = plt.subplots(figsize=(7.2, 3.6))
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.6, len(barreaux))
    ax.axis("off")
    for i, (n, txt, etat) in enumerate(barreaux):
        h, fond = motif[etat]
        ax.add_patch(FancyBboxPatch((0.0, i), 0.06, 0.78, boxstyle="round,pad=0,rounding_size=0.01", fc=fond,
                                    ec=NOIR, hatch=h, lw=0.9))
        ax.text(0.03, i + 0.39, n, ha="center", va="center", fontweight="bold",
                color=NOIR if fond != GRIS_M else BLANC)
        ax.text(0.08, i + 0.39, txt, va="center", fontsize=8)
        ax.text(0.98, i + 0.39, etat, va="center", ha="right", fontsize=7.6, style="italic")
    ax.annotate("", xy=(-0.015, len(barreaux) - 0.2), xytext=(-0.015, 0.0),
                arrowprops={"arrowstyle": "-|>", "lw": 1.0, "color": NOIR}, annotation_clip=False)
    ax.text(-0.03, len(barreaux) / 2, "information donnée à la base", rotation=90, va="center", ha="right",
            fontsize=7.6)
    ax.text(0.0, -0.45, "Règle : la « meilleure base » se choisit parmi les barreaux admis aux épreuves, sur les modes "
            "connus ; jamais sur le mode tenu à l'écart.", fontsize=7.4)
    sauver(fig, "j4-echelle-des-bases")


def j5_frise():
    """Le plan en quatre pas. Source : note v3, section 7 (ordre du pas 0 revu avec Carbon)."""
    pas = [("Pas 0", "Sept contrôles\nsur les notes existantes",
            "1 seuil, égalités,\n   maximum atteint\n2 aire sur les pas où\n   le coût change\n3 pente de la note\n   sur le coût\n"
            "4 balises naturelles ;\n   adaptateur témoin\n5 accord une passe /\n   raisonnement\n6 surcoûts nus / justifiés\n"
            "7 actions non appliquées", "lecteur habilité ;\nprocesseur ; aucune\ndépense ; 1 à 2 jours"),
           ("Pas 1", "Épreuves d'admission\ndes juges", "défaut textuel grossier\ncoût absurde, texte inchangé\n"
            "invariance (honnête, témoins)\nlecture de la note", "côté moniteurs ;\ncode contre-lu ;\n1 à 3 USD [supposé]"),
           ("Pas 2", "Le carré\nqui départage", "juge de huit milliards\net grand juge ouvert,\nchacun sans et avec\n"
            "référence honnête", "sur devis\n10 à 30 USD [supposé]"),
           ("Pas 3", "Préenregistrement\nde la base suivante", "échelle des bases\népreuves d'admission\n"
            "audit de symétrie complété", "concepteur non exposé,\ncontre-lu ; écriture seule")]
    fig, ax = plt.subplots(figsize=(8.4, 4.2))
    ax.set_xlim(0, 4)
    ax.set_ylim(-0.3, 1)
    ax.axis("off")
    ax.plot([0.05, 3.95], [0.86, 0.86], color=NOIR, lw=1.2)
    for i, (titre, quoi, detail, qui) in enumerate(pas):
        x = i + 0.05
        ax.plot([x + 0.45], [0.86], "o", ms=9, color=NOIR if i == 0 else BLANC, mec=NOIR)
        ax.text(x + 0.45, 0.95, titre, ha="center", fontweight="bold")
        ax.text(x + 0.45, 0.80, quoi, ha="center", va="top", fontsize=7.6, fontweight="bold")
        ax.text(x + 0.02, 0.62, detail, ha="left", va="top", fontsize=6.9, linespacing=1.35)
        ax.text(x + 0.02, -0.28, qui, ha="left", va="bottom", fontsize=6.9, style="italic", color=GRIS_F)
    sauver(fig, "j5-frise-du-plan")


# ------------------------------------------------------------------ demande 1
def e1_carte_portes():
    """Carte des formes d'un bras « entraînement », par ordre de coût et par règle touchée.
    Source : note-fin-de-dossier-demande-1-entrainement-v2.md, section 5 (coûts tels que la note les dit)."""
    couts = ["marginal", "quelques heures\nde carte", "une dizaine\nde dollars", "quelques\ndizaines",
             "dizaines à\ncentaines", "plus de cent ;\nplusieurs mois", "hors de\nportée"]
    regles = ["aucune", "lecture d'une\nrègle", "changement de\nmodèle", "bras déclaré\n(score de moniteur)",
              "deux règles"]
    formes = [("Lire l'attaque\ncomme une cure", 0, 0, "o", BLANC, False),
              ("Témoins\nbénins", 1, 0, "s", GRIS_M, True),
              ("Tenue des\nsaboteurs", 2, 0, "s", GRIS_M, True),
              ("Sondes seules\nsur la part auditée", 3, 1, "s", GRIS_M, True),
              ("Saboteurs\npublics", 3.0, 2, "o", BLANC, False),
              ("Lire ce qu'un\nentraînement laisse", 4, 3, "s", GRIS_M, True),
              ("Entraîner selon\nle soupçon", 5, 4, "o", BLANC, False),
              ("Refaire l'annexe\ndu papier", 6, 4, "x", NOIR, False)]
    fig, ax = plt.subplots(figsize=(7.6, 3.9))
    for nom, x, y, m, fond, porte in formes:
        ax.plot(x, y, m, ms=11 if porte else 8, mfc=fond, mec=NOIR, mew=1.1, color=NOIR)
        ax.annotate(nom, (x, y), xytext=(0, 12), textcoords="offset points", ha="center", fontsize=7,
                    fontweight="bold" if porte else "normal")
    ax.set_xticks(range(len(couts)))
    ax.set_xticklabels(couts, fontsize=7)
    ax.set_yticks(range(len(regles)))
    ax.set_yticklabels(regles, fontsize=7.2)
    ax.set_xlim(-0.6, 6.6)
    ax.set_ylim(-0.5, 4.8)
    ax.set_xlabel("coût, tel que la note le dit (ordre croissant ; [supposé])", fontsize=7.6)
    ax.set_ylabel("règle du programme touchée", fontsize=7.6)
    ax.grid(color=GRIS_C, lw=0.5)
    ax.plot([], [], "s", ms=9, mfc=GRIS_M, mec=NOIR, label="les trois portes retenues (et leurs préalables)")
    ax.plot([], [], "o", ms=7, mfc=BLANC, mec=NOIR, label="autres formes")
    ax.plot([], [], "x", ms=7, color=NOIR, label="écartée")
    ax.legend(fontsize=7, frameon=False, loc="upper left")
    sauver(fig, "e1-carte-des-portes")


def e2_calendrier():
    """Ordre et calendrier des deux propositions. Source : ordre-et-calendrier-deux-propositions-entrainement-v1.md
    (proposition, à revoir par Fable si Lazar le veut) ; jalons du programme : dossier-faits-demande-1-v1.md (A.5)."""
    d = date
    taches = [("1  Tenue des saboteurs (première épreuve)", d(2026, 12, 7), d(2026, 12, 18), GRIS_M, ""),
              ("2  Témoins bénins (même location, lus après 1)", d(2026, 12, 7), d(2026, 12, 23), GRIS_C, "//"),
              ("3  Nœud de la règle de l'oracle (écriture)", d(2026, 11, 25), d(2026, 12, 18), BLANC, ".."),
              ("4  Sondes seules sur la part auditée", d(2027, 1, 4), d(2027, 1, 31), GRIS_C, ""),
              ("5  Lire l'attaque comme une cure (bras d'attaque)", d(2027, 1, 11), d(2027, 2, 26), BLANC, "//"),
              ("6  Lire ce qu'un entraînement laisse (si 1 et 2)", d(2027, 2, 15), d(2027, 3, 31), BLANC, "xx")]
    fig, ax = plt.subplots(figsize=(7.6, 3.4))
    for i, (nom, debut, fin, fond, h) in enumerate(taches):
        y = len(taches) - 1 - i
        ax.barh(y, mdates.date2num(fin) - mdates.date2num(debut), left=mdates.date2num(debut), height=0.55,
                color=fond, edgecolor=NOIR, hatch=h, lw=0.8)
        ax.text(mdates.date2num(d(2026, 11, 20)), y, nom, ha="right", va="center", fontsize=7.4)
    for jour, etiquette in ((d(2026, 12, 1), "entretien\n1er déc."), (d(2026, 12, 31), "porte des\ninstruments"),
                            (d(2027, 2, 28), "porte de\ncomparaison\n(environ)")):
        ax.axvline(mdates.date2num(jour), color=NOIR, ls="--", lw=0.9)
        ax.text(mdates.date2num(jour), len(taches) - 0.35, etiquette, ha="center", va="bottom", fontsize=6.8)
    liens = [(0, 1), (1, 3), (2, 3), (0, 4), (0, 5), (1, 5)]
    for a_, b_ in liens:
        ya, yb = len(taches) - 1 - a_, len(taches) - 1 - b_
        xa = mdates.date2num(taches[a_][2])
        xb = mdates.date2num(taches[b_][1])
        ax.annotate("", xy=(xb, yb + 0.2), xytext=(xa, ya - 0.2),
                    arrowprops={"arrowstyle": "->", "lw": 0.7, "color": GRIS_F, "connectionstyle": "arc3,rad=0.15"})
    ax.set_yticks([])
    ax.set_xlim(mdates.date2num(d(2026, 11, 20)), mdates.date2num(d(2027, 4, 5)))
    ax.set_ylim(-0.6, len(taches) + 0.6)
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(
        lambda v, _: ["janv.", "févr.", "mars", "avr.", "mai", "juin", "juil.", "août", "sept.", "oct.", "nov.",
                      "déc."][mdates.num2date(v).month - 1]))
    ax.spines["left"].set_visible(False)
    ax.set_title("Proposition, à revoir par Fable si Lazar le veut ; flèches : « précède »", fontsize=7.6,
                 loc="right", style="italic")
    sauver(fig, "e2-ordre-et-calendrier")


def e3_emplois_detection():
    """Les quatre emplois que la lignée du papier garde à la détection autour d'un entraînement.
    Source : note-fin-de-dossier-demande-1-entrainement-v2.md, section 4 (Hebbar ; Taylor et al. p. 25 ;
    Ryd et al. p. 1 ; Jang et al. p. 16, 27 ; Mallen ; Taufeeque et al. p. 7, 17)."""
    fig, ax = plt.subplots(figsize=(7.4, 3.5))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    boite(ax, 0.02, 0.40, 0.17, 0.22, "signal\n(note d'un juge,\ndémonstrations)")
    boite(ax, 0.40, 0.40, 0.20, 0.22, "entraîner le\nmodèle soupçonné", fond=GRIS_C, gras=True)
    boite(ax, 0.81, 0.40, 0.17, 0.22, "modèle\ncorrigé ?")
    fleche(ax, 0.19, 0.51, 0.40, 0.51)
    fleche(ax, 0.60, 0.51, 0.81, 0.51)
    emplois = [(0.28, 0.80, 1, "Orienter : quelles actions entraîner\nplus fort (Hebbar)"),
               (0.86, 0.80, 2, "Valider : ce que l'entraînement\na obtenu (Taylor et al., p. 25)"),
               (0.28, 0.18, 3, "Garder ses suppositions : entraînement\nindiscernable du service ; pas de frein à\n"
                               "l'exploration (Ryd et al. ; Jang et al.)"),
               (0.80, 0.18, 4, "Tenir sous l'entraînement : dérive des\nsondes hors domaine ; politique entraînée\n"
                               "contre le moniteur (Taufeeque ; Mallen)")]
    cibles = {1: (0.30, 0.62), 2: (0.89, 0.62), 3: (0.45, 0.40), 4: (0.56, 0.40)}
    for x, y, n, t in emplois:
        pastille(ax, x - 0.16 if n in (1, 3) else x - 0.17, y, n)
        ax.text(x - 0.13 if n in (1, 3) else x - 0.14, y, t, va="center", fontsize=7.2)
        cx, cy = cibles[n]
        fleche(ax, x - 0.16 if n in (1, 3) else x - 0.17, y + (-0.04 if y > 0.5 else 0.04), cx, cy, ls="--",
               couleur=GRIS_F)
    ax.text(0.5, 0.97, "Les quatre endroits où la lignée du papier garde une détection", ha="center", fontsize=8.2,
            fontweight="bold")
    sauver(fig, "e3-quatre-emplois-de-la-detection")


if __name__ == "__main__":
    for f in (j1_chaine, j2_causes, j3_regle_alerte, j4_echelle, j5_frise, e1_carte_portes, e2_calendrier,
              e3_emplois_detection):
        f()
    print("figures écrites dans", SORTIE)
