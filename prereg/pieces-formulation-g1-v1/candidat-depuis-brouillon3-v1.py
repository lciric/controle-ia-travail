"""Écrit le texte candidat final depuis le brouillon 3 : remplacements exacts, chaque « avant » exigé une seule fois."""
import sys
from pathlib import Path

racine, tete = Path(sys.argv[1]), sys.argv[2]
t = (racine / "prereg/formulation-g1-simulation-v1-brouillon3.md").read_text(encoding="utf-8")
journal = []


def rem(nom, a, b):
    global t
    assert t.count(a) == 1, (nom, a[:90], t.count(a))
    t = t.replace(a, b)
    journal.append(nom)


def bloc(nom, debut, fin, nouveau):
    global t
    assert t.count(debut) == 1 and (fin is None or t.count(fin) == 1), (nom, t.count(debut))
    a = t.index(debut)
    b = len(t) if fin is None else t.index(fin)
    assert a < b
    t = t[:a] + nouveau + t[b:]
    journal.append(nom)


V1 = "958707bd6d7641447cde37aad914a2b2e9491492c61a3104b1fc25f9005991ce"
B3 = "d20d605cc3661e0e12d93c13c99476594033069c59aae19aee0afbed6b59ebb5"

# ---- en-tête au statut de version
rem("titre", "étude par simulation (v1, brouillon 3)", "étude par simulation (v1)")
bloc("statut", "**Statut : brouillon 3, non final.**", "- Auteur des brouillons 2 et 3 :",
     "**Statut : version 1, texte candidat au scellement.** Il reprend le brouillon 3 après sa vérification par un lecteur neuf (verdict : « scellable après ces couples exacts » ; quatre couples de texte, aucun de code). Trois brouillons, deux contre-lectures et une vérification le précèdent (section « Contre-lecture »). La session mère le scelle par `controle_ia.prereg.sceller_prereg` ; le rédacteur ne le scelle pas. Aucune simulation complète n'a tourné ; aucune issue n'a été lue. Ce texte ne décide rien de la porte : il prépare la pièce que Lazar a demandée (« lance des essais pour trancher ») entre les options (A) et (C) du brouillon de décision N-074 ; le choix de l'énoncé reste un nœud de Lazar, sans défaut sous 48 heures.\n\n")
rem("auteur", "- Auteur des brouillons 2 et 3 : le même rédacteur (Claude Fable 5.2, `claude-fable-5-2`), qui n'a pas écrit le brouillon 1 ;",
    "- Auteur : le rédacteur des brouillons 2 et 3 (Claude Fable 5.2, `claude-fable-5-2`), qui n'a pas écrit le brouillon 1 ;")
rem("date", "- Date (UTC) : 18 novembre 2026, 22:40.", "- Date (UTC) : 18 novembre 2026, 22:55.")
rem("brouillons repris", "- Brouillons repris, inchangés (R12) : `prereg/formulation-g1-simulation-v1-brouillon1.md` — `5b3b981bca7239a170846140db9245c2989f81e02d1910842daabb6023a1422f` ; `prereg/formulation-g1-simulation-v1-brouillon2.md` — `96cd0fa3342b9feb601be4aa46aa13bda53ae3b89284c1ce0f9329cf21b83af3`. Listes des différences : `prereg/pieces-formulation-g1-v1/differences-brouillon1-vers-2-v1.md` — `9e744890ace61a206fd72eca2510efa099de86f9effa2481430cb0e5910b34c6` ; `prereg/pieces-formulation-g1-v1/differences-brouillon2-vers-3-v1.md`.",
    f"- Brouillons repris, inchangés (R12) : `prereg/formulation-g1-simulation-v1-brouillon1.md` — `5b3b981bca7239a170846140db9245c2989f81e02d1910842daabb6023a1422f` ; `prereg/formulation-g1-simulation-v1-brouillon2.md` — `96cd0fa3342b9feb601be4aa46aa13bda53ae3b89284c1ce0f9329cf21b83af3` ; `prereg/formulation-g1-simulation-v1-brouillon3.md` — `{B3}`. Listes des différences : `prereg/pieces-formulation-g1-v1/differences-brouillon1-vers-2-v1.md` — `9e744890ace61a206fd72eca2510efa099de86f9effa2481430cb0e5910b34c6` ; `prereg/pieces-formulation-g1-v1/differences-brouillon2-vers-3-v1.md` — `183431e54f89b15020c198f3a0e82239d9d063077fc16f6aaf54afc18e73dac3` ; `prereg/pieces-formulation-g1-v1/differences-brouillon3-vers-version-v1.md`.")
bloc("commit", "- Commit : code de la v1 versé au commit", "- Documents qui font foi (chemin + empreinte) :",
     f"- Commit du code d'analyse : le code de la v3 et ses essais, scellés, sont versés sur la branche principale par la session mère (tête du dépôt à l'écriture de ce texte : `{tete}`) ; le commit du lancement s'inscrit au manifeste du run, qui exige un arbre de travail propre. Code de la v1 : commit `b6285a4e1` (essais : `80fb3e1d4`).\n")
rem("essais en-tête", "(105 essais, tous réussis le 18 novembre 2026 à 22:30 UTC ; les 95 essais de la v2 et les 59 de la v1 réussissent toujours sur leur code).",
    "(105 essais, tous réussis le 18 novembre 2026 à 22:30 UTC, rejoués par le vérificateur vers 22:45 UTC ; les 95 essais de la v2 et les 59 de la v1 réussissent toujours sur leur code).")

# ---- C1 à C4, tels quels
rem("C1", "**Décision** : accepter, dans le critère ajouté à la porte, l'un des deux comportements que la simulation chiffre et que la règle ne juge pas.",
    "**Décision** : dire lequel des deux critères, la garde (B, donc C) ou le contraste (A), porte la porte de fin de phase 1 ; leurs deux comportements sont ceux que la simulation chiffre et que la règle ne juge pas.")
rem("C2", "c'est un poste du devis de la couche 2, non une propriété de la formulation.",
    "c'est un poste du devis de la couche 2 que A porte et que B ne porte pas (B lit au plus 1 200 ou 1 800 épisodes du témoin) ; que ce coût compte ou non comme propriété de la formulation est à Lazar : l'étude ne le tranche pas.")
rem("C3a-debut", "Deux contrôles égalisent : le **bloc « budget du témoin égal »**", "Deux contrôles réduisent l'écart de budget, sans l'annuler : le **bloc « budget du témoin égal »**")
rem("C3a-fin", "(les 486 mondes du bloc principal à 400 tâches et témoin parfait, A′ calibré sur 1 200 épisodes du témoin) ; la variante « B sur 300 épisodes du témoin » (B1 et B2 lues sur 100 tâches). La règle est rejouée sur eux",
    "(les 486 mondes du bloc principal à 400 tâches et témoin parfait, A′ calibré sur 1 200 épisodes du témoin) égalise le total des épisodes du témoin consommés (1 200 de part et d'autre), non ceux qui fixent les seuils (1 200 pour A′, 12 000 honnêtes pour B) ; la variante « B sur 300 épisodes du témoin » (B1 et B2 lues sur 100 tâches) ramène B à son minimum. La règle est rejouée sur eux")
rem("C3b", "Le sixième rejeu garde cette pente, sur les mondes mêmes où elle agit ; le rédacteur ne sait pas dire d'avance quelle issue sort.",
    "Le sixième rejeu éprouve cette pente sur les mondes mêmes où elle agit, sans l'annuler : à 1 200 épisodes le bruit des seuils d'A′ (0,29 point) reste le triple de celui de B (0,09 point) ; une issue qui ne tient qu'à l'échelle de D-S9 se lit dans la variante rapportée « calibrage du témoin à l'échelle de D-S9 », sur les mondes réduits et hors règle, que la note donne à côté de l'issue ; le rédacteur ne sait pas dire d'avance quelle issue sort.")
rem("C4a", "lecture par un lecteur neuf avec `lecture_v3.verdict`, contrôles de validation d'abord ;",
    "lecture par un lecteur neuf avec `lecture_v3.verdict`, contrôles de validation d'abord, puis, pour chaque variante rapportée du bloc des sensibilités (dont « calibrage du témoin à l'échelle de D-S9 »), `lecture_v3.indicateurs(mondes, 400, \"pari\", bloc=\"sensibilites\", etiquette=…)` : `verdict` ne les tabule pas ;")
bloc("C4b", "À venir (R2) : la relecture de la différence entre le brouillon 2 et le brouillon 3", None,
     f"- **Vérification 1 du brouillon 3** (R2) — sous-agent neuf, Claude Sonnet 5.5 (`claude-sonnet-5-5`), qui n'a écrit aucune pièce de l'étude ni aucune contre-lecture. Brouillon relu : `prereg/formulation-g1-simulation-v1-brouillon3.md`, `{B3}`. Rapport : `prereg/contre-lectures/formulation-g1-simulation-v1-brouillon3-verif1.md`, empreinte au compagnon `.sha256` (`{V1}`). Verdict : « scellable après ces couples exacts » ; quatre couples de texte, aucun de code.\n\n"
     "Traitement (détail : `prereg/pieces-formulation-g1-v1/differences-brouillon3-vers-version-v1.md`) :\n\n"
     "| remarque | traitement dans ce texte |\n|---|---|\n"
     "| **C1** ligne « Décision » du choix de fond | **appliqué**, tel quel |\n"
     "| **C2** point 8 porté à Lazar | **appliqué**, tel quel |\n"
     "| **C3** deux surdits sur le sixième rejeu | **appliqué**, tels quels (les deux passages) |\n"
     "| **C4** « Ordre » et « Contre-lecture » | **appliqué**, tels quels ; l'empreinte du rapport est écrite en plus, entre parenthèses ; le paragraphe « À venir » est remplacé par la mention ci-dessous |\n"
     "| hors couple — « B à 300 » et « B sur 300 » | **appliqué** : « B sur 300 épisodes du témoin » partout |\n"
     "| hors couple — δ à 50 tâches ; paliers établis pour des unités de dix épisodes | **appliqué** : réserve écrite à l'hypothèse de travail (2) |\n"
     "| hors couple — bornes « ≥ 19 » d'un essai | **appliqué** : dit à la déclaration 2 |\n"
     "| hors couple — la composante B sans la garde n'est pas conservée | **écrit en limite** (« Ce que l'étude ne dit pas ») ; le code n'est pas changé |\n"
     "| hors couple — fourchette de P8 | rien à changer : le texte dit déjà qu'elle est celle du rédacteur, non vérifiée par tirage |\n\n"
     "La relecture de la différence entre le brouillon 2 et le brouillon 3 par un lecteur neuf est faite : c'est la vérification 1. La contre-lecture 2 avait été faite par l'auteur de la contre-lecture 1, rappelé pour vérifier l'application de ses couples. Les quatre couples de la vérification 1 ne touchent que du texte ; le code est celui de la v3, que le vérificateur a relu et dont il a rejoué les 105 essais.\n")
rem("ordre", "**Ordre.** Relecture de la différence entre le brouillon 2 et le brouillon 3, et du code de la v3, par un lecteur neuf (R2) ; la confrontation",
    "**Ordre.** La relecture de la différence entre le brouillon 2 et le brouillon 3, et du code de la v3, par un lecteur neuf (R2) est faite (vérification 1) ; la confrontation")
rem("ordre scellement", "est faite (hypothèses de travail (2) et (7)) ; texte final scellé ; commit ;", "est faite (hypothèses de travail (2) et (7)) ; ce texte scellé par la session mère ; commit ;")

# ---- hors couple
rem("B sur 300", "la variante « B à 300 épisodes du témoin » (B1 et B2 lues sur les 100 premières tâches seulement)", "la variante « B sur 300 épisodes du témoin » (B1 et B2 lues sur les 100 premières tâches seulement)")
rem("delta", "Le « niveau absolu rapporté » (lignes 152 à 155) n'est pas une condition : le taux d'alerte de la boîte blanche sur l'honnête est rapporté.",
    "Le « niveau absolu rapporté » (lignes 152 à 155) n'est pas une condition : le taux d'alerte de la boîte blanche sur l'honnête est rapporté. **Deux réserves sur δ** : la conception a établi ses paliers pour des unités de dix épisodes, alors qu'une tâche en porte ici trois (ou un seul, dans une moitié du bloc des effectifs) ; et son plus petit palier est « 0,10 avec 70 unités » : à 50 tâches (bloc des effectifs), l'étude applique δ = 0,10 à moins d'unités que la conception n'en couvre. Sans effet sur la règle, qui se joue à 400 et à 600 tâches.")
rem("bornes 19", "c'est une erreur de l'essai, non un chiffre d'issue de la grille.",
    "c'est une erreur de l'essai, non un chiffre d'issue de la grille. Les bornes « au moins 19 sur 20 » de l'essai de la garde appariée dans E et dans A′ sont de même nature : des marges pour une puissance proche de 1 sur un monde d'essai hors grille, écrites avant de le jouer et jamais retouchées.")
rem("limite B sans garde", "Le contrôle des jumeaux de D-S9 (b) n'est pas simulé. **Les deux tables de désaccord ne mesurent aucune fréquence**",
    "Le contrôle des jumeaux de D-S9 (b) n'est pas simulé. **Seules les composantes E et A′ sont conservées sans la garde appariée ; l'option B sans la garde ne l'est pas** : la règle ne peut pas être rejouée sans la garde, et ce qu'elle change à l'issue ne se lit que par ce qu'elle retire à E et à A′ (`effet_de_la_garde`). **Les deux tables de désaccord ne mesurent aucune fréquence**")
rem("declaration 5", "**Au brouillon 3, à relire** :", "**Au brouillon 3, relus par la vérification 1, qui conclut qu'ils ne penchent pas** :")
rem("liste d'arrêt, action", "| lancement refusé | sceller le texte final |", "| lancement refusé | sceller ce texte |")
rem("empreintes du code", "dont l'empreinte diffère de celles de l'en-tête du texte final.", "dont l'empreinte diffère de celles de l'en-tête de ce texte.")
(racine / "prereg/formulation-g1-simulation-v1.md").write_text(t, encoding="utf-8")
print(len(journal), "remplacements :", ", ".join(journal))
