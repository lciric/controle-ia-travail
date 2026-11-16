"""Brouillon 2 de l'addendum d'écart de B bis = brouillon 1 (991ab560…) + couples C1 à C5 et mineurs m1 à m8 de
`contre-lecture-addendum-ecart-v1-brouillon1-v1.md` (a5d0cc8a…), avec les décisions de la mère R-2955 et R-2956.
Usage : python -I couples-addendum-ecart-v1-brouillon2-v1.py DOSSIER_DES_BROUILLONS_DE_B_BIS
Arrêt (code 1) si l'empreinte du brouillon 1 n'est pas la bonne, si un « ancien » ne figure pas exactement une fois, si un des
seize blocs de texte change d'un octet, ou si le brouillon 2 existe déjà (R12 : on n'écrase jamais)."""
import hashlib, re, sys
from pathlib import Path

DOSSIER = Path(sys.argv[1])
SOURCE = DOSSIER / "T0.7-etape-B-bis-v1-addendum-ecart-v1-brouillon1.md"
CIBLE = DOSSIER / "T0.7-etape-B-bis-v1-addendum-ecart-v1-brouillon2.md"
SHA_SOURCE = "991ab56066c229c2a04cfa0489e6cbe0f2b11a717587d305fdcfb65ea1582efe"
BLOC = re.compile(r"```text\n(.*?)\n```", re.S)

def arret(motif):
    print("ARRET :", motif); sys.exit(1)

brut = SOURCE.read_bytes()
if hashlib.sha256(brut).hexdigest() != SHA_SOURCE:
    arret("empreinte du brouillon 1 inattendue")
if CIBLE.exists():
    arret(f"{CIBLE.name} existe déjà")
t = brut.decode("utf-8")
blocs_avant = BLOC.findall(t)
if len(blocs_avant) != 16:
    arret("seize blocs attendus")

# --- C2 (M2) : renommage E1…E8 → EC-1…EC-8, hors des blocs, aux 22 lignes nommées par la contre-lecture (numéros du brouillon 1)
LIGNES_C2 = (42, 75, 98, 115, 132, 149, 166, 183, 112, 129, 146, 212, 213, 214, 228, 230, 251, 256, 273, 276, 277, 278)
L = t.split("\n")
for n in LIGNES_C2:
    ligne = L[n - 1]
    if ligne.startswith("```") or ligne in blocs_avant or not re.search(r"\bE[1-8]\b", ligne):
        arret(f"C2 : ligne {n} inattendue")
    L[n - 1] = re.sub(r"\bE([1-8])\b", r"EC-\1", ligne)
t = "\n".join(L)
reste = [i + 1 for i, l in enumerate(t.split("\n")) if l not in blocs_avant and re.search(r"\bE[1-8]\b", l)
         and not l.startswith("```")]
if reste:
    arret(f"C2 : nom d'écart non renommé aux lignes {reste}")

COUPLES = [
# titre, statut, date (forme du brouillon 2)
("forme-titre", "réserve R-PILE — v1 — brouillon 1", "réserve R-PILE — v1 — brouillon 2"),
("forme-date", "- **Date (UTC)** : 2026-11-16, de 00:31 à 00:37 (`date -u`).",
 "- **Date (UTC)** : 2026-11-16, de 00:31 à 00:37 (`date -u`), brouillon 1 (`991ab560…`, gardé tel quel, R12).\n"
 "- **Brouillon 2** : même auteur, 2026-11-16, de 00:50 à 00:50 (`date -u`) = brouillon 1 + les couples C1 à C5 et les mineurs\n"
 "  m1 à m8 de `brouillons/T0.7-etape-B-bis-v1/contre-lecture-addendum-ecart-v1-brouillon1-v1.md`\n"
 "  (`a5d0cc8a85cfd723d5b08258bd2515554b629667e27ad88981af3ff4bd3225c2`, « scellable après corrections » ; R-2956), appliqués par\n"
 "  `brouillons/T0.7-etape-B-bis-v1/pieces/couples-addendum-ecart-v1-brouillon2-v1.py` ; les seize blocs du § 2 sont égaux à\n"
 "  l'octet à ceux du brouillon 1 (vérifié par ce programme)."),
# C3 (statut)
("C3-statut", "et l'inscription de sa ligne (point ouvert P2 du § 7), **avant `CODE-BBIS`**.",
 "et l'inscription de sa ligne `ADDENDUM-ECART-1-BBIS` au registre voisin\n"
 "  `registres/t07-etape-b-bis-v1-addenda-v1.md` et d'une ligne R- de `registres/decisions.md` (décision de la mère R-2955, § 7),\n"
 "  **avant `CODE-BBIS`**. Texte qui fera foi : `prereg/T0.7-etape-B-bis-v1-addendum-ecart-v1.md` et son compagnon (R-2955, R-2956)."),
("forme-statut", "- **Statut** : brouillon 1. Il ne vaut", "- **Statut** : brouillon 2. Il ne vaut"),
# m1
("m1", "phrase du texte scellé fait foi telle quelle.",
 "phrase du texte scellé fait foi telle quelle ; « relance sous ce texte » (liste d'arrêt scellée, ligne 186) se lit\n"
 "désormais « sous ce texte et cet addendum »."),
# C3 (§ 1)
("C3-par1", "le code v3 restant tel quel (R-2933, voie (ii)) ». La recommandation",
 "le code v3 restant tel quel (R-2933, voie (ii)) ». « Au registre propre » est la formule de la mère, non le mot de\n"
 "Lazar ; le registre propre n'admet que huit clés (§ 7) : inscription au registre voisin, R-2955, dit à Lazar (R-2956). La recommandation"),
# C1 (M1), forme écrite par la mère (R-2956)
("C1", "ne valent ici que par cette ligne.",
 "ne valent ici que par cette ligne. **Hors des dix-sept couples** (a1 à a5, b1, b2, c1 à c10) que R-2933 a portés à Lazar :\n"
 "les ajouts m4 (premier écart) et m5 (deuxième écart), mineurs de la même contre-lecture ; m4 écrit ce que `marche_v3` fait\n"
 "déjà, m5 étend R-PILE à la sonde d'ENC (la réserve s'écrit plus souvent, sans changer d'issue). **Dits à Lazar** par la mère,\n"
 "dans la conversation, le 16 novembre vers 00:45 UTC, avant le scellement, avec l'affaiblissement du § 5, point 4 (« la sonde\n"
 "lue à 300 époques n'est plus comparée à une référence d'une autre pile ») et le registre voisin du § 7 (R-2956). Aucun mot de\n"
 "Lazar en retour sur ces points n'est consigné à la rédaction de ce brouillon, et aucun n'est revendiqué ici."),
# m2
("m2", "(le brouillon 6 a 32 lignes de plus\nen tête :", "(le brouillon 6 a 32 lignes de plus\naprès le titre :"),
# C2 (phrase d'explication)
("C2-phrase", "Les citations sont exactes, au\ncaractère, dans les blocs.",
 "Les citations sont exactes, au\ncaractère, dans les blocs. Les écarts sont nommés EC-1 à EC-8 pour ne pas être confondus avec les états E0 à\nE6 du texte scellé."),
# m6 (raison du premier écart ; bloc intouché)
("m6", "il écrit ce que `marche_v3` fait déjà (même contre-lecture, § 3 et § 4, essai (a)).",
 "il écrit ce que `marche_v3` fait déjà (même contre-lecture, § 3 et § 4, essai (a)). **Lecture déclarée** du bloc « nouveau » :\n"
 "quand le réglage retenu du couple est linéaire, « la sonde « attention » de 300 époques du couple » est une sonde apprise sur la\n"
 "carte au réglage « attention » de mêmes couche et régularisation, pour le seul contrôle ; ce n'est pas une sonde lue\n"
 "(`src/controle_ia/t07bbis/validation_imbriquee_v3.py`, `71bffa5bf26c2b182bb81ebfb920c1246b6c9784b2332ff1304f0ff3c24890eb`,\n"
 "docstring, lignes 9 à 22 ; § 5, point 4)."),
# m8 (contrôle mécanique)
("m8", "brouillon 6 n'a pas) : aucun autre fragment ne change.",
 "brouillon 6 n'a pas) : aucun autre fragment ne change. Rejoué par la contre-lecture du brouillon 1 (`a5d0cc8a…`, § 1 et annexe).\n"
 "Les seize blocs du brouillon 2 sont ceux du brouillon 1 (`991ab560…`) à l'octet ; le même rejeu se fera sur la version scellée."),
# m3, m4 (§ 3)
("m3-m4", "`GO-2026-11-14-09`, une relance), calendrier, lignes de registre, données gardées : inchangés.",
 "`GO-2026-11-14-09`, une relance), calendrier, lignes de registre, données gardées : inchangés ; deux effets déclarés\n"
 "sans changement de ces sections : le contrôle vient à la fin de l'apprentissage, donc un arrêt du contrôle coûte tout\n"
 "l'apprentissage (§ 5, point 8), et il ajoute sur la carte au plus une linéaire de 300 époques, une attention de 3 époques et deux\n"
 "de 300 (`validation_imbriquee_v3`, `71bffa5b…`, docstring, ligne 30) ; le choix du réglage n'est pas modifié par cet addendum,\n"
 "mais il peut dépendre de la pile (§ 5, point 6)."),
# m5 (§ 4)
("m5", "(contre-lecture du brouillon 6, § 3 et § 8, par `git ls-remote`).",
 "(contre-lecture du brouillon 6, § 3, ligne 183, par `git ls-remote`) ;\n"
 "  absente encore à 2026-11-16T00:42:38Z (contre-lecture du brouillon 1 de cet addendum, `a5d0cc8a…`, § 3 : `git ls-remote\n"
 "  --exit-code` de `refs/heads/donnees/t07-etape-b-bis-v1` et du motif `refs/heads/donnees/t07-etape-b-bis*` → code 2 ; témoin\n"
 "  positif `refs/heads/prep/t07bbis-code-v1` → code 0) ; relevé de la mère au scellement : avec l'état de l'étape B, ci-dessous."),
# § 4 : quatrième passe (renvoi au § 5, sans marqueur ici)
("passe-par4", "aucune référence `calcul/t07bbis-repetition-v4` dans les références locales à la rédaction ;",
 "aucune référence `calcul/t07bbis-repetition-v4` dans les références locales à la rédaction du brouillon 1, ni à\n"
 "  distance à 00:42:38Z ; la passe tourne depuis 00:35 UTC (instance créée, R-2953), sur données synthétiques seulement ; sa mesure :\n"
 "  § 5, point 5 ;"),
# marqueur 1 (§ 4) : état de l'étape B
("etat-B", "de cet addendum : `<<ETAT_ETAPE_B_AU_SCELLEMENT_ADDENDUM>>` (point ouvert P1 du § 7).",
 "de cet addendum, et absence de la branche de données de B bis à la même heure : `<<ETAT_ETAPE_B_AU_SCELLEMENT_ADDENDUM>>`\n"
 "  (relevé par la mère, par les noms seulement ; point ouvert P1 du § 7)."),
# C4 (§ 5)
("C4-artefact", "3,4·10⁻⁸ à 7,8·10⁻⁷) ;",
 "3,4·10⁻⁸ à 7,8·10⁻⁷) ; le cinquième artefact non attrapé, actions et étiquettes permutées ensemble, n'est pas une erreur ;"),
("C4-point4", "seul son déterminisme sur la\n   carte est vérifié.",
 "seul son déterminisme sur la\n   carte est vérifié, et le déterminisme ne prouve pas la justesse (une erreur déterministe propre à la carte après la\n"
 "   troisième époque passe les trois contrôles). Si le réglage retenu du couple tiré est linéaire, sa sonde lue est comparée\n"
 "   comme au texte scellé et les sondes « attention » du contrôle ne sont pas des sondes lues ; les sondes « attention » des autres\n"
 "   couples et celles d'ENC ne reçoivent aucun contrôle, comme au texte scellé."),
# marqueur 2 (§ 5) : mesure de la quatrième passe
("passe-par5", "(contre-lecture du brouillon 6, § 7) : la quatrième passe le dira, sur données synthétiques ; le\n   contrôle porte sur un seul couple tiré, comme au texte scellé.",
 "(contre-lecture du brouillon 6, § 7). Mesure de la quatrième passe de répétition (données synthétiques, R-2953 ; règle de\n"
 "   lecture du premier écart) : `<<MESURE_QUATRIEME_PASSE_REPETITION>>` (chemin et empreinte de la sortie poussée, écart de la\n"
 "   linéaire à 300 époques, écart de l'attention à 3 époques, déterminismes, lot reconstruit, issue de la règle de lecture ;\n"
 "   rempli par la mère avant le scellement). Le contrôle porte sur un seul couple tiré, comme au texte scellé ;\n"
 "6. le réglage retenu peut dépendre de la pile : sans signal, l'étendue 0,0074 dépasse le seuil d'ex aequo 0,005 ; la\n"
 "   famille, la couche ou la régularisation retenues, donc l'écriture même de R-PILE, peuvent changer d'une pile à l'autre\n"
 "   (`diagnostic-stabilite-aires-attention-v1.md`, `dd67802d…`, lignes 24 et 106) ; l'état rapporté est celui de la carte de la\n"
 "   course ;\n"
 "7. les régimes mesurés sont ceux d'un bruit gaussien isotrope ; entre les aires 0,47 et 0,56, et pour un signal faible mêlé\n"
 "   à une forte mémorisation, rien n'est mesuré (même pièce, ligne 108) ; l'horizon de 3 époques a été fixé sur ces trajectoires\n"
 "   synthétiques (`diagnostic-ecart-attention-carte-v1.md`, `5ecb9235…`, lignes 161 à 169) ;\n"
 "8. un couple dont la sonde finale est en échec n'est jamais contrôlé ; le contrôle vient à la fin de l'apprentissage : une\n"
 "   erreur de chaîne coûte tout l'apprentissage (mineur m7 de la contre-lecture du brouillon 6 ; le pire cas du devis compte\n"
 "   déjà une relance complète)."),
# C3 (§ 6)
("C3-par6", "et sa ligne (P2) ;", "et sa ligne `ADDENDUM-ECART-1-BBIS` du registre voisin ;"),
# C5
("C5", "porte R-PILE et le point (7) selon EC-2 et EC-3.",
 "porte R-PILE et le point (7) selon EC-2 et EC-3.\n"
 "- **Recevabilité** : un verdict de B bis qui ne cite pas cet addendum, son empreinte et sa ligne n'est pas scellé ; la mère le\n"
 "  vérifie avant de le soumettre à Lazar. L'addendum figure nommément dans la liste des fichiers donnés au lecteur du verdict\n"
 "  (R13) et dans `registres/etat.md` ; la table conjointe et tout document qui cite une aire de B bis le citent aussi. Il\n"
 "  n'entre pas dans la liste de la fiche `CODE-BBIS` (`marche_v3` vérifie chaque fichier de la fiche sur l'instance, où il\n"
 "  n'est pas extrait)."),
# P1 (sans marqueur hors des § 4 et § 5)
("P1", "- **P1** — remplir `<<ETAT_ETAPE_B_AU_SCELLEMENT_ADDENDUM>>` (§ 4) par l'état",
 "- **P1** — remplir le marqueur de l'état de l'étape B (§ 4) par l'état"),
("P1-bis", "comme pour `ABSENCE-B-BBIS`.",
 "comme pour `ABSENCE-B-BBIS`.\n"
 "- **P1 bis** — remplir le marqueur de la mesure de la quatrième passe (§ 5, point 5),\n"
 "  puis rejouer le contrôle des seize blocs ; une vérification éclair par un lecteur neuf suffit (différentiel du brouillon 2 à\n"
 "  la version scellée)."),
# C3 (P2 tranché)
("C3-P2-titre", "- **P2** — **lieu de la ligne de scellement : conflit avec le code v3.**",
 "- **P2** — **lieu de la ligne de scellement (tranché, R-2955).**"),
("C3-P2", "rendrait donc la course illisible. Options :",
 "rendrait donc la course illisible. **Décision de la mère (R-2955)** : registre voisin à nom neuf\n"
 "  `registres/t07-etape-b-bis-v1-addenda-v1.md` (lu par aucun code ; nom hors des motifs d'extraction de l'amorce), clé\n"
 "  `ADDENDUM-ECART-1-BBIS`, et ligne R- ; aucune ligne au registre propre ni au registre partagé ; une forme de clé que le code\n"
 "  ignorerait est écartée (ce serait passer une garde par sa forme). Fichier scellé : `prereg/T0.7-etape-B-bis-v1-addendum-ecart-v1.md`.\n"
 "  ANCIEN-P2-RETIRE"),
# m7 (§ 8)
("m7", "R-2917, R-2919, R-2931, R-2933, R-2950 (une à une, par",
 "R-2917, R-2919, R-2931, R-2933, R-2950, R-2953, R-2955, R-2956 (une à une, par"),
("m7-cl", "- cet addendum ; `prereg/T0.7-etape-B-bis-v1.md` (`0ae6210f…`) ;",
 "- cet addendum, son brouillon 1 et `contre-lecture-addendum-ecart-v1-brouillon1-v1.md` (`a5d0cc8a…`), avec le programme de\n"
 "  couples du brouillon 2 ; `prereg/T0.7-etape-B-bis-v1.md` (`0ae6210f…`) ;"),
]
for nom, ancien, nouveau in COUPLES:
    n = t.count(ancien)
    if n != 1:
        arret(f"couple {nom} : « ancien » trouvé {n} fois")
    t = t.replace(ancien, nouveau)
# fin de C3-P2 : retrait des options (a) à (c) et de la recommandation du brouillon 1, jusqu'à la fin du point P2
m = re.search(r"ANCIEN-P2-RETIRE \(a\) registre voisin.*?la lettre de la ligne l'exige\.", t, re.S)
if not m or t.count("ANCIEN-P2-RETIRE") != 1:
    arret("C3-P2 : fin du point P2 introuvable")
t = t[:m.start()].rstrip(" \n") + t[m.end():]
if BLOC.findall(t) != blocs_avant:
    arret("un bloc de texte a changé")
for mq in ("ETAT_ETAPE_B_AU_SCELLEMENT_ADDENDUM", "MESURE_QUATRIEME_PASSE_REPETITION"):
    if t.count(f"<<{mq}>>") != 1:
        arret(f"marqueur {mq} : une occurrence attendue")
CIBLE.write_text(t, encoding="utf-8")
print(f"couples appliqués : C2 (22 lignes) puis {', '.join(c[0] for c in COUPLES)} ; seize blocs égaux ; écrit {CIBLE.name}")
