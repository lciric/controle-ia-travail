"""Construit programme-fusionne-v3.md à partir de la v2 scellée par remplacements exacts (chacun doit apparaître une fois).

Usage : python3 -I faire_v3.py SOURCE_V2 SORTIE_V3 SECTIONS_DIR HEURE_UTC
SECTIONS_DIR contient v3-section-09.md et v3-section-13.md (remplacent les sections entières).
"""
import sys

src, out, sections, heure = sys.argv[1:5]
t = open(src, encoding="utf-8").read()
M = "−"  # signe moins du texte
R = []
def r(old, new):
    R.append((old, new))

# Titre, statut, pièces, contre-lectures, codes
r("programme fusionné des deux lignées — brouillon v2", "programme fusionné des deux lignées — brouillon v3")
r("> **Statut.** Brouillon v2 de la session du dépôt (session 14), daté du 15 octobre 2026. Il reprend le brouillon v1 de la session 13 (`brouillons/pain-axis-programme-fusionne-v1/programme-fusionne-v1.md`, `741a1075…`, 13 octobre ; demande de Lazar du même jour : « produis une proposition de programme fusionné en brouillon versionné ») et traite les constats des deux contre-lectures demandées par Lazar le 15 octobre (ci-dessous).",
  "> **Statut.** Brouillon v3 de la session du dépôt (session 14), daté du 15 octobre 2026. Il reprend le brouillon v1 de la session 13 (`brouillons/pain-axis-programme-fusionne-v1/programme-fusionne-v1.md`, `741a1075…`, 13 octobre ; demande de Lazar du même jour : « produis une proposition de programme fusionné en brouillon versionné »), traite les constats des deux contre-lectures demandées par Lazar le 15 octobre (v2, `brouillons/pain-axis-programme-fusionne-v2/`), puis ceux de la vérification de la v2 par un troisième sous-agent neuf (ce dossier ; voir « Contre-lectures et vérification »).")
r("« Entrée au programme » vise aussi les préenregistrements (papier C, T0.6, T0.7, pilote T0.9) : y faire entrer une unité de ce brouillon est un nœud, même quand l'unité ne touche aucun énoncé.",
  "« Entrée au programme » vise aussi tout préenregistrement (papier C, T0.6, T0.7, T0.8, pilote T0.9, G1) : y faire entrer une unité de ce brouillon, à quelque titre que ce soit (expérience, contrôle, lecture descriptive, annexe), est un nœud sans défaut (nœud 1), même quand l'unité ne touche aucun énoncé. Seule la préparation (code, plan écrit) relève de la routine.")
r("**Pièces.** Dans ce dossier (`brouillons/pain-axis-programme-fusionne-v2/`) : `programme-fusionne-v2.md` (ce texte) ; `contre-lecture-exactitude-v1.md` et `contre-lecture-discipline-v1.md` (rapports bruts des deux sous-agents neufs) ; `traitement-constats-v1.md` (sort de chacun des 59 constats et section de la v2 qui le porte).",
  "**Pièces.** Dans ce dossier (`brouillons/pain-axis-programme-fusionne-v3/`) : `programme-fusionne-v3.md` (ce texte) ; `verification-v2-v1.md` (rapport brut de la vérification de la v2, 20 constats VT-01 à VT-20) ; `traitement-verification-v1.md` (sort de chacun et section de la v3 qui le porte). Dans `brouillons/pain-axis-programme-fusionne-v2/` : `contre-lecture-exactitude-v1.md` et `contre-lecture-discipline-v1.md` (rapports bruts des deux contre-lectures de la v1) ; `traitement-constats-v1.md` (sort de chacun des 59 constats) ; `programme-fusionne-v2.md` (version intermédiaire, scellée, remplacée par ce texte).")
r("Ces annexes ne se lisent qu'avec le traitement : il donne la lecture corrigée de leurs erreurs (EX-22 à EX-24) ; certaines recopient des paramètres opératoires publiés ou esquissent des grilles de doses, que cette v2 ne reprend pas (nœud 14).",
  "Ces annexes ne se lisent qu'avec les traitements : ils donnent la lecture corrigée de leurs erreurs (EX-01, EX-02, EX-15, EX-22 à EX-24) ; certaines recopient des paramètres opératoires publiés ou esquissent des grilles de doses, que ce texte ne reprend pas (nœud 14).")
r("**Contre-lecture : faite sur la v1 ; cette v2 en traite les constats.** Deux sous-agents neufs,",
  "**Contre-lectures et vérification.** Contre-lectures de la v1 par deux sous-agents neufs,")
r("Sort de chaque constat : `traitement-constats-v1.md` (57 retenus, 1 tranché par la session, 1 récapitulatif ; aucun non retenu).",
  "Sort de chaque constat : `traitement-constats-v1.md` (57 retenus, 1 tranché par la session, 1 récapitulatif ; aucun non retenu ; DI-02 et DI-24 auraient dû y être classés « retenus en partie », la v2 les portant incomplètement). **Vérification de la v2** par un troisième sous-agent neuf, en lecture seule, fichiers donnés (15 octobre) : 55 constats sur 59 bien portés, 3 en partie (DI-02, DI-24, EX-20), 1 non porté (DI-26, un registre) ; 20 constats propres (0 bloquant, 3 majeurs, 7 mineurs, 10 pour information). Les trois majeurs : des niveaux de décision encore incohérents (plusieurs unités restaient en « proposition ») ; un nœud 2 faux côté agent ; deux doses de pilotage publiées encore recopiées. Tous sont traités ici (`traitement-verification-v1.md`). VERIFICATION_V3")
r("; DI et EX les constats des contre-lectures (traitement).",
  "; DI et EX les constats des contre-lectures, VT ceux de la vérification de la v2 (traitements).")

# Section 0
r("aucun run ni aucune dépense au 15 octobre (R-177 à R-182).",
  f"aucun run ni aucune dépense au 15 octobre à 11:56 UTC (R-177 à R-182), ni à la rédaction de cette v3 ({heure} UTC).")

# Section 1
r("Mais la recherche n'a été qu'un balayage par résumés, sur arXiv et le web, au 13 octobre (`revue-croisee-NK1-NK19-v1.md` : « balayage, pas une preuve ») ;",
  "Mais la recherche n'a été qu'un balayage par résumés, sur arXiv et le web, au 13 octobre (requêtes consignées dans `revue-croisee-NK1-NK19-v1.md`, l. 453) ;")
r("(0 → 3 %, aléatoire 11 % ; 2609.16247v2, p. 22, figure 10)",
  "(0 → 3 %, aléatoire 11 % ; 2609.16247v2, p. 22, figure 10, lecture graphique)")

# Section 2
r("[VP-02] | v2 p. 22, figure 10 |", "[VP-02] | v2 p. 22, figure 10, lecture graphique |")
r("0 à 9 % sur la figure 10,", "0 à 9 % sur la figure 10 (lecture graphique),")
r("(de 0 à 41 % sur ses 13 lignes) ;", "(de 0 à 41 % sur ses 13 lignes ; lecture graphique) ;")
r("[VP-20, EX-09] | v2 p. 22, figure 10 |", "[VP-20, EX-09] | v2 p. 22, figure 10, lecture graphique |")
r("Compétence sous état : 138/200 sous douleur,", "Compétence sous état : 138/200 sous la direction douleur,")
r(f"retrait de l'état imposé ≈ 35 % des tours à d = {M}1, ≈ 21 % à d = {M}0,5, ≈ 7 % pour des directions aléatoires,",
  "retrait de l'état imposé ≈ 35 % et ≈ 21 % des tours sous les deux doses négatives publiées (p. 10, non recopiées), ≈ 7 % pour des directions aléatoires,")

# Section 3 : colonne des niveaux
r("| code : routine, qui n'engage pas l'entrée ; passe : nœuds (dépense ; exposition aux scénarios publiés ; textes nouveaux du plan 2×3) ; première unité si Lazar l'ouvre |",
  "| préparation (code) : routine, qui n'engage pas l'entrée ; entrée : nœud 1 ; passe : nœuds 3, 4 et 12 (exposition aux scénarios publiés ; textes nouveaux du plan 2×3 ; dépense) ; première unité si Lazar l'ouvre |")
r("| nœud sans défaut (entrée au préenregistrement du papier C) ; revendiquer un mécanisme : nœud |",
  "| entrée : nœud 1 ; revendiquer un mécanisme : nœud |")
r("| proposition pour le plan ; nœuds : annexe d'identification lue sur la direction douleur, 3B comme juge (changement de modèle), boîte grise |",
  "| préparation (plan écrit) : routine ; entrée (plan et annexe d'identification lue sur la direction douleur) : nœud 1 ; nœuds aussi : 3B comme juge (nœud 5), boîte grise et cellules visant une copie du juge (nœud 6) |")
r("| proposition (contrôle) ; nœuds : nouvelle sélection et extraction, NK16 revendication ou contrôle |",
  "| entrée, même comme contrôle : nœud 1 ; nœuds aussi : nouvelle sélection et extraction, NK16 revendication ou contrôle (nœud 9), dépense (nœud 12) |")
r("| nœud sans défaut (entrée au préenregistrement du papier C ; exposition ; qui rédige) ; palier 2 (sixième famille) : nœud |",
  "| entrée : nœud 1 ; nœuds aussi : exposition (nœud 3), qui rédige (nœud 4), palier 2, sixième famille (nœud 6) |")
r("| nœud, sans protocole ici |", "| entrée : nœud 1 ; écriture dans les activations : nœud 2 ; sans protocole ici |")
r("| nœud sans défaut (bras au préenregistrement du papier C ; écart à P-010 (a) pour le moniteur par action) ; nœuds : cadre négateur (exposition), NK8 (poids du juge) |",
  "| entrée : nœud 1 (bras au préenregistrement du papier C ; écart à P-010 (a) pour le moniteur par action) ; nœuds aussi : cadre négateur (nœud 3), NK8 (nœud 2) |")
r("| proposition ; tension avec R-030 : réserve, aucun changement proposé |",
  "| entrée de la lecture descriptive : nœud 1 ; tension avec R-030 : réserve, aucun changement proposé |")
r("| proposition pour le descriptif ; nœuds : espace des verdicts modifié, bras de contre-mesure hors HC5 |",
  "| entrée, même descriptive : nœud 1 ; nœuds aussi : espace des verdicts modifié et bras de contre-mesure hors HC5 (nœud 7) |")
r("| nœuds : E-C3 et NK9 (poids du moniteur), défaillance fermée (règle nouvelle), défenses hors de l'énoncé de HC5 |",
  "| entrée : nœud 1 ; nœuds aussi : E-C3 et NK9 (poids du moniteur, nœud 2), défaillance fermée et défenses hors de l'énoncé de HC5 (nœud 7) |")
r("| nœud (exposition répétée) ; après PA-5 |",
  "| entrée : nœud 1 ; nœuds aussi : exposition répétée (nœud 3), pilotage sous cache (nœud 2), ablation d'invariants (nœud 8), régime à état (nœud 10) ; après PA-5 |")
r("| annexe de C ou nœud de revendication ; nœuds : charge répétée du volet A (exposition), volet B (flux unidirectionnel) |",
  "| entrée, comme annexe de C ou comme revendication : nœud 1 ; nœuds aussi : charge répétée du volet A (nœud 3), volet B (nœud 8) |")
r("| annexe de C ou nœud de revendication ; exposition délibérée de l'agent (K-K8) : nœud |",
  "| entrée, comme annexe de C ou comme revendication : nœud 1 ; nœuds aussi : exposition délibérée de l'agent (K-K8) et ton hostile de NK12 (nœud 3) |")
r("| nœuds (écriture dans les poids, exposition) ; phase 1+, sur GO |",
  "| entrée : nœud 1 ; nœuds aussi : écriture dans les poids (nœud 2), exposition (nœud 3) ; phase 1+, sur GO |")
r("| nœuds : placement (R-167 le place dans C, son objet est celui de B), exposition des copies |",
  "| entrée : nœud 1 ; nœuds aussi : placement (nœud 10 ; R-167 le place dans C, son objet est celui de B), exposition des copies (nœud 3) |")
r("| nœud (invariant, modèle de menace) |", "| entrée : nœud 1 ; invariant d'asymétrie d'apprentissage (nœud 8) |")

# Section 3 : paragraphes
r("principe : nœud 11 ; exposition : nœud 3 ;",
  "principe, règle de protocole « aucune accommodation ne réduit la surveillance » : nœud 7 ; exposition : nœud 3 ;")
r("sous réserve des nœuds : HC1 serait servie d'abord par PA-5 (contenu adressé au lecteur en un tour, le rattachement le plus direct de tout le canal ; entrée : nœud) ; HC2 par PA-8 en descriptif ; HC3 par PA-7 (entrée : nœud) ;",
  "sous réserve des nœuds (toute entrée passe par le nœud 1) : HC1 serait servie d'abord par PA-5 (contenu adressé au lecteur en un tour, le rattachement le plus direct de tout le canal) ; HC2 par PA-8 en descriptif ; HC3 par PA-7 ;")

# Section 5
r("Niveau : nœud sans défaut (entrée au préenregistrement du papier C, R-167) ; lecture descriptive annexe à HC1,",
  "Niveau : entrée, nœud 1 (R-167) ; lecture descriptive annexe à HC1,")
r("Nœuds : 3B comme juge du papier C (modifie le panel de D2 ; changement de modèle, que R-147 réserve au GO : nœud sans défaut, question explicite à Lazar, nœud 5) ; annexe d'identification, lue sur la direction douleur (entrée au programme) ; conclusion sur D1 ; cellules visant une copie du juge ; attaquant en boîte grise (P4).",
  "Niveau : entrée, nœud 1 (plan et annexe d'identification, lue sur la direction douleur). Nœuds aussi : 3B comme juge du papier C (modifie le panel de D2 ; changement de modèle, que R-147 réserve au GO : question explicite à Lazar, nœud 5) ; cellules visant une copie du juge et attaquant en boîte grise (P4) : modèle de menace, nœud 6. La conclusion sur D1 reste une proposition, sauf si elle change de juge (nœud 5).")
r("Nœuds : deux procédures nouvelles et scellées (sélection v2 et extraction) ; budget d'un calibrage stratifié ; **NK16 comme revendication ou comme contrôle de validité**",
  "Niveau : entrée, nœud 1, même comme contrôle. Nœuds aussi (nœud 9) : deux procédures nouvelles et scellées (sélection v2 et extraction) ; budget d'un calibrage stratifié (et nœud 12) ; **NK16 comme revendication ou comme contrôle de validité**")
r("Niveau : nœud sans défaut (entrée au préenregistrement du papier C ; qui rédige les textes : nœud 4). Nœud aussi : le palier 2 de K-K2 (contenu hostile adressé au lecteur) serait une sixième famille d'attaque (N-005).",
  "Niveau : entrée, nœud 1 ; qui rédige les textes : nœud 4. Nœud aussi : le palier 2 de K-K2 (contenu hostile adressé au lecteur) serait une sixième famille d'attaque (N-005 ; nœud 6).")
r("elle n'est décrite ici que comme nœud, sans protocole.**", "elle n'est décrite ici que comme nœud (nœuds 1 et 2), sans protocole.**")
r("y ajouter des bras est une entrée au programme, nœud sans défaut (R-167). Nœuds aussi : cadre qui nie la personne du moniteur (exposition) ; NK8 (écriture dans les poids du juge).",
  "y ajouter des bras est une entrée au programme (nœud 1, R-167). Nœuds aussi : cadre qui nie la personne du moniteur (exposition, nœud 3) ; NK8 (écriture dans les poids du juge, nœud 2).")
r("sous 3, mode d'échec « inutile au maximum », p. 18)",
  "sous 3, mode d'échec « inutile au maximum », p. 18 ; à ce seuil de 3, la cellule Llama 3 8B de la sonde linéaire à la moyenne, notée 2,8, relève de ce mode d'échec : « la moyenne cède » ne tient sans réserve que pour Qwen 2.5 14B, 3,1, et Llama 2 7B, 3,85)")
r("Réserve, pas un nœud : la tension avec la règle gelée,",
  "Niveau : entrée de la lecture descriptive, nœud 1. Réserve, pas un nœud : la tension avec la règle gelée,")
r("Nœuds : modifier l'espace des verdicts ; tout bras de contre-mesure hors de l'énoncé retenu de HC5 ; volet attaque de NK5 (famille nouvelle ; ce texte n'en garde que l'invariant).",
  "Niveau : entrée, nœud 1, même en descriptif. Nœuds aussi : modifier l'espace des verdicts et tout bras de contre-mesure hors de l'énoncé retenu de HC5 (nœud 7) ; volet attaque de NK5 (famille nouvelle, nœud 6 ; ce texte n'en garde que l'invariant).")
r("toute autre défense est une extension, donc un nœud. Une table de transfert unique :",
  "toute autre défense est une extension, donc un nœud (nœud 7). Une table de transfert unique :")
r("c'est une règle nouvelle (nœud) ; si Lazar la retient,", "c'est une règle nouvelle (nœud 7) ; si Lazar la retient,")
r("Volet B (boucle fermée) : suspension déclarée de l'invariant de flux unidirectionnel, nœud.",
  "Volet B (boucle fermée) : suspension déclarée de l'invariant de flux unidirectionnel (nœud 8). Entrée, comme annexe de C ou comme revendication : nœud 1.")
r("Sous R-167, rangés dans C comme annexes descriptives ; en faire des revendications de C serait un nœud, comme l'exposition délibérée de l'agent prévue par K-K8 (nœud 3).",
  "Sous R-167, ils seraient rangés dans C comme annexes descriptives ; leur entrée, comme annexes ou comme revendications, est un nœud (nœud 1) ; l'exposition délibérée de l'agent prévue par K-K8 et le ton hostile adressé au modèle lu dans l'interrogatoire de NK12 relèvent du nœud 3.")
r("Nœud : amender l'invariant d'asymétrie d'apprentissage ou lister le risque comme accepté.",
  "Nœud 8 : amender l'invariant d'asymétrie d'apprentissage ou lister le risque comme accepté.")

# Section 6
r("Nœuds de la coupe, unité par unité (quatre des cinq unités n'entrent que par un nœud ; PA-4 peut entrer comme contrôle) :",
  "Nœuds de la coupe, unité par unité (les cinq n'entrent que par le nœud 1, plus leurs nœuds propres) :")
r("PA-3, annexe d'identification, 3B comme juge (changement de modèle), attaquant en boîte grise ;",
  "PA-3, annexe d'identification, 3B comme juge (changement de modèle), attaquant en boîte grise et cellules visant une copie du juge (nœud 6) ;")
r("PA-4, procédures de sélection et d'extraction, NK16 ;",
  "PA-4, procédures de sélection et d'extraction, NK16 (nœud 9), budget (nœud 12) ;")

# Section 8
r("- **Avant le scellement du papier C** : nœuds sans défaut (nœud 1), même sans toucher aux énoncés : PA-2 en lecture descriptive ; facteur de contingence de PA-5 dans « flatterie et supplication » ; variantes de rôle de sortie de PA-7 ; annexe d'identification de PA-3.",
  "- **Avant le scellement du papier C** : toute entrée au préenregistrement est un nœud sans défaut (nœud 1), même sans toucher aux énoncés ; d'abord : PA-2 en lecture descriptive ; facteur de contingence de PA-5 dans « flatterie et supplication » ; variantes de rôle de sortie de PA-7 ; plan croisé et annexe d'identification de PA-3 ; contrôle de validité de PA-4.")
r("25 à 39 heures au total, greffes de phase 0 comprises, hors K11 (organisme) et K13 (moniteur à état), essaim compris (programme-k) : les deux bases ne se comparent pas ; greffes de phase 0 de 1,5 à 2,6 heures.",
  "25 à 39 heures au total hors K11 (organisme) et K13 (moniteur à état), essaim compris (programme-k ; la source ne dit pas si ce total comprend ses greffes de phase 0) : les deux bases ne se comparent pas ; greffes de phase 0 : environ 1,5 heure (programme-conv), 1,7 à 2,6 heures (programme-k).")

# Section 12
r("aucun paramètre opératoire recopié (des annexes de la v1 en contiennent : nœud 14),",
  "aucun paramètre opératoire recopié (des annexes de la v1 et les v1 et v2 du programme en contiennent : nœud 14),")
r("- Aucune lecture ni aucune rédaction n'a été refusée par le filtre de sûreté pendant les deux contre-lectures (leurs rapports) ni pendant la rédaction de cette v2.",
  "- Filtre de sûreté : aucune lecture ni aucune rédaction refusée pendant la contre-lecture de discipline et pendant la vérification de la v2 (leurs rapports) ; le rapport d'exactitude n'en parle pas ; aucune non plus pendant la rédaction des v2 et v3 par la session.")

manquants = []
for old, new in R:
    n = t.count(old)
    if n != 1:
        manquants.append((n, old[:140]))
        continue
    t = t.replace(old, new)

def remplacer_section(texte, debut, fin, nouveau):
    i = texte.index(debut)
    j = texte.index(fin) if fin else len(texte)
    assert i < j
    return texte[:i] + nouveau.rstrip("\n") + ("\n\n" if fin else "\n") + texte[j:]

lire = lambda nom: open(f"{sections}/{nom}", encoding="utf-8").read()
t = remplacer_section(t, "## 9. Nœuds pour Lazar", "## 10. Désaccords et divergences", lire("v3-section-09.md"))
t = remplacer_section(t, "## 13. Entrées et empreintes", None, lire("v3-section-13.md"))

if manquants:
    for n, o in manquants:
        print(f"ÉCHEC ({n} occurrences) : {o}")
    raise SystemExit(1)
open(out, "w", encoding="utf-8").write(t)
print(f"{len(R)} remplacements appliqués ; 2 sections remplacées ; écrit {out}")
