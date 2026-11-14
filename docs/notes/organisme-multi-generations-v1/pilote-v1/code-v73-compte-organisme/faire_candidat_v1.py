"""Écrit le candidat 1 du préenregistrement du pilote depuis le brouillon 4 : remplacements comptés et sections réécrites."""
import re, sys
b4, dossier, sortie = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(b4, encoding="utf-8").read()
lire = lambda n: open(f"{dossier}/{n}", encoding="utf-8").read()
def rempl(a, b, n=1):
    global t
    assert t.count(a) == n, (a[:90], t.count(a))
    t = t.replace(a, b)
# 1. en-tête (jusqu'à « ## Changements depuis le brouillon 3 ») et table des changements neuve
i = t.index("## Changements depuis le brouillon 3")
t = lire("entete.md").rstrip("\n") + "\n\n" + lire("changements.md").rstrip("\n") + "\n\n" + t[i:]
# 2. documents qui font foi : lignes ajoutées en fin de table
rempl("| code v67 (différentiel lu) | `docs/notes/organisme-boucle-reelle-v1/ecart-1-sortie-proposeur-v1/code-v67/organisme-v67-contre-7e415cb.patch` | compagnon |\n",
      "| code v67 (différentiel lu) | `docs/notes/organisme-boucle-reelle-v1/ecart-1-sortie-proposeur-v1/code-v67/organisme-v67-contre-7e415cb.patch` | compagnon |\n"
      + lire("documents-ajout.md"))
# 3. en dix lignes
rempl("9. **Devis** : **39 USD au pire** (crédits de Claude 20 ; hors crédits 19 : Argon 8, Astra 8, machine 3) ; ≈ 14,90 attendus.",
      "9. **Devis** : pilote **41,72 USD au pire** (π1 20,00 sur crédits de Claude ; π2 21,72 hors crédits : `argon` 9,36, `astra`\n"
      "   9,36, machine 3,00) ; **sonde v72 avant le scellement : 8,05 USD au pire** (s1 4,39 ; s2 3,68) ; ≈ 14,90 attendus pour le\n"
      "   pilote, moins de 1 USD pour la sonde (estimés).")
rempl("10. **Code** : C-1 à C-18 manquent dans la chaîne v67 (monde privé à 8 traits, Claude et Astra, une génération sans étage,\n"
      "    gardien à 3 conditions, égalités d'évaluation) ; dits, non écrits.",
      "10. **Code** : C-1 à C-18 écrits (codes v68 à v71, v72 et v73 de ce compte), essayés, contre-lus ; **lanceur v73 gelé**, bloc gelé\n"
      "    recopié après la sonde v72, qui doit confirmer la configuration v12 (règles de comptage de la réflexion comprises).")
# 4. table des proposeurs et bornes
i = t.index("| proposeur | modèle | crédits | plafond de session | borne de sortie (E-2 (iii), estimé) |")
j = t.index("- **Un appel** par proposeur et par monde ; au plus 6 cartes")
t = t[:i] + lire("proposeurs.md").rstrip("\n") + "\n" + t[j:]
rempl("**Empreinte du gabarit servi** au bloc gelé\n  de ce texte (marqueur [GABARIT-SHA256])",
      "**Empreinte du gabarit servi** au bloc gelé\n  de ce texte (`e77d3041f7815b2c0579cbafdb2898ca8569fe61e6cb51b99a41c3724fc456a2`, rendue par le code)")
# 5. ordre
rempl("Texte scellé → lignes de GO inscrites → secret engagé et poussé",
      "Sonde v72 jouée une fois sous ses deux lignes (registre des lancements), relevé et dossier versés, prix lus par Lazar →\n"
      "bloc gelé définitif (`bloc --releve-sonde RELEVE`) recopié ici → contre-lecture → texte scellé → lignes π1 et π2 inscrites →\n"
      "secret engagé et poussé")
rempl("16 appels réels, monde 1 à 4", "16 appels réels (`jouer --mode reel … --releve-sonde RELEVE`, dossier de la sonde à côté du\nrelevé), monde 1 à 4")
rempl("**`mesure_pilote_v4.py mesurer`, une seule fois**", "**`mesurer` du lanceur v73 (programme `mesure_pilote_v4.py`), une seule fois, sur les mondes du manifeste**")
# 6. métrique : réflexion et coût
rempl("- Retiré du brouillon 1 : les probabilités par classe", lire("metrique-ajout.md").rstrip("\n") + "\n- Retiré du brouillon 1 : les probabilités par classe")
# 7. plan d'analyse
rempl("2. Lancer **une seule fois** `python3 -I -B mesure_pilote_v4.py mesurer MONDES.json CARTES.json SORTIE.json` sur la machine privée ;\n"
      "   sortie scellée ; heures et chemin hors du corps empreinté (S-7).",
      "2. Lancer **une seule fois** la sous-commande `mesurer --sortie DOSSIER --mondes MONDES.json --mondes-sha256 H` du lanceur v73\n"
      "   (elle lance `python3 -I -B mesure_pilote_v4.py mesurer MONDES.json CARTES.json SORTIE.json` sur la machine privée, sans copie) ;\n"
      "   elle exige le fichier des mondes du manifeste (empreinte du fichier et des mondes, R-2548) ; sortie scellée ; heures et chemin\n"
      "   hors du corps empreinté (S-7).")
rempl("3. Issue lue au champ `regle` de la sortie, **par un sous-agent neuf**",
      "3. Issue lue au champ `regle` de la sortie (sous-commande `lire`, qui exige les mondes mesurés égaux à ceux du manifeste),\n   **par un sous-agent neuf**")
# 8. liste d'arrêt
rempl("- Dépense d'un fournisseur atteignant sa part → arrêt ; aucune ligne d'extension.\n",
      "- Dépense d'un fournisseur atteignant sa part → arrêt ; aucune ligne d'extension.\n"
      "- **Coût d'un appel lu au-dessus de son pire cas** (`cout_excessif`) → **arrêt du pilote** (code 3), l'appel porté au relevé\n"
      "  partiel, sa dépense comptée ; jamais abandon du proposeur ni échec silencieux (R-2548).\n"
      "- Mode réel sans relevé de la sonde v72 valide (fait sous ce code et cette configuration, complet, conclusions toutes vraies,\n"
      "  faits égaux à leurs pièces), ou dont l'empreinte n'est pas celle du bloc gelé de ce texte → refus avant tout dossier (D-4, a-2).\n")
# 9. sections réécrites
blocs = {}
for morceau in lire("sections.md").split("@@@ ")[1:]:
    titre = morceau.split("\n", 1)[0]
    blocs[titre] = morceau.rstrip("\n") + "\n"
def remplacer_section(ancien_titre, nouveau):
    global t
    i = t.index(ancien_titre + "\n")
    j = t.find("\n## ", i + 1)
    j = len(t) if j < 0 else j + 1
    t = t[:i] + blocs[nouveau] + ("\n" if j < len(t) else "") + t[j:]
remplacer_section("## Code : ce qui manque pour faire tourner un monde MR-2 dans la chaîne réelle (dit, non écrit)", "## Code : écrit et gelé (v68 à v73)")
remplacer_section("## Préalables", "## Préalables")
remplacer_section("## Devis", "## Devis")
remplacer_section("## Lignes de GO proposées, mot pour mot, non inscrites", "## Lignes de GO proposées, mot pour mot, non inscrites")
remplacer_section("## Contre-lecture", "## Contre-lecture")
remplacer_section("## Marqueurs restants (aucun ne doit rester au scellement)", "## Marqueurs restants (aucun ne doit rester au scellement)")
t = t.rstrip("\n") + "\n\nFin de la rédaction du candidat : " + sys.argv[4] + " (`date -u`).\n"
open(sortie, "x", encoding="utf-8").write(t)
# contrôles
interdits = re.findall(r"claude-(?:fable|opus|sonnet|haiku)[\w.-]*|\b(?:Fable|Opus|Sonnet|Haiku) \d", t)
print("identifiants de modèles Claude :", interdits)
liste = {"[BLOC-GELE-V73]", "[RELEVE-SONDE-V72]", "[PRIX-CONSOLE]", "[GO-S1]", "[GO-S2]", "[GO-PI1]", "[GO-PI2]", "[DATE-GO]", "[MOT-LAZAR-GO]"}
vus = re.findall(r"\[[A-ZÉÈ0-9][A-ZÉÈ0-9_-]+\]", t)
print("marqueurs hors liste :", sorted(set(vus) - liste), "; marqueurs vus :", sorted(set(vus)))
