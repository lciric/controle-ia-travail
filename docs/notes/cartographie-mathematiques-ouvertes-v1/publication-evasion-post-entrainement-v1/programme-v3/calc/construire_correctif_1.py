"""Construit le correctif 1 de la v3 du programme du papier D à partir de la v3, sans la modifier (R12).

Usage : python3 -I construire_correctif_1.py   (depuis le dossier calc/)
Refuse d'écraser une sortie déjà présente.
"""
import hashlib
import pathlib
import sys

ICI = pathlib.Path(__file__).resolve().parent
SRC = ICI.parent / "strategie-cibles-et-feuille-de-route-publication-papier-d-v3.md"
DST = ICI.parent / "strategie-cibles-et-feuille-de-route-publication-papier-d-v3-correctif-1.md"
EMPREINTE_V3 = "b4ee88e2869e88e12bda7f19f9eee164e2e32944f22064a9a6fddf9fb419c55d"

brut = SRC.read_bytes()
assert hashlib.sha256(brut).hexdigest() == EMPREINTE_V3, "la v3 a changé"
if DST.exists():
    sys.exit("sortie déjà présente : refus d'écraser")
t = brut.decode()


def rep(a, b, n=1):
    global t
    assert t.count(a) == n, (a[:70], t.count(a))
    t = t.replace(a, b)


def ligne(prefixe, nouvelle):
    """Remplace la ligne unique qui commence par `prefixe`."""
    global t
    ls = t.split("\n")
    idx = [i for i, l in enumerate(ls) if l.startswith(prefixe)]
    assert len(idx) == 1, (prefixe, len(idx))
    ls[idx[0]] = nouvelle
    t = "\n".join(ls)


def bloc(debut, fin, nouveau):
    """Remplace le texte de la ligne de titre `debut` (incluse) à la ligne de titre `fin` (exclue)."""
    global t
    i = t.index("\n" + debut) + 1
    j = t.index("\n" + fin) + 1
    assert i < j
    t = t[:i] + nouveau.rstrip("\n") + "\n\n" + t[j:]


# ------------------------------------------------------------------ en-tête
rep("# Programme et feuille de route de publication du papier D — v3\n",
    "# Programme et feuille de route de publication du papier D — v3, correctif 1\n")
rep("- **Date** : 24 novembre 2026, vers 14 h (temps universel).",
    "- **Date** : 24 novembre 2026 ; v3 vers 14 h, correctif 1 vers 14 h 25 (temps universel).")
rep("- **Statut** : pièce de travail, non contre-lue, non scellée. Elle remplace la v2 sans l'écraser. Elle ne décide rien : deux points sont soumis à Lazar (section 5), et toute diffusion, toute soumission et toute dépense restent ses décisions.",
    "- **Statut** : pièce de travail, non scellée. Elle remplace la v2 sans l'écraser. Elle ne décide rien : trois points sont soumis à Lazar (section 5), une restriction de son mot sur la marge d'audit lui est proposée (section 6), et toute diffusion, toute soumission et toute dépense restent ses décisions.\n"
    "- **Correctif 1** : la v3 (empreinte `b4ee88e2869e88e1…`, gardée intacte à côté) a été contre-lue par Claude Opus 5.5, neuf, effort élevé : « accepté avec corrections », six défauts à corriger, sept mineurs, aucun bloquant (`contre-lecture-opus-programme-v3-v1.md`, `76b3cee7e39cb87e…`). Les treize sont traités ici ; correspondance dans `table-corrections-contre-lecture-programme-v3-v1.md`. La vérification des corrections par le même contre-lecteur reste à faire.")
rep("- Les scripts du dépôt n'ont pas été relancés. Quatre calculs cités ont été refaits à part (section 1.3).",
    "- Les scripts du dépôt n'ont pas été relancés. Six calculs cités ont été refaits à part (section 1.3).")
rep("- L'auteur est un modèle de la même maison que la lettre A du collisionneur (Claude Opus 5.5), dont le lecteur de la note était déjà. Un biais en faveur de ses propositions est possible.",
    "- L'auteur est un modèle de la même maison que la lettre A du collisionneur (Claude Opus 5.5). Le lecteur de la note était déjà un Opus 5.5, et le contre-lecteur de la v3 aussi. Un biais en faveur des propositions de la lettre A est possible.")

# ------------------------------------------------------------------ section 1
rep("Le manuscrit théorique est prêt pour une cible modeste après trois gestes sans dépense ;",
    "Le manuscrit théorique est prêt pour une cible modeste une fois remplis les préalables sans dépense de la section 7.1 ;")
rep("4. **Deux décisions soumises à Lazar**, sans défaut : viser d'abord un atelier non archivistique ; ouvrir, sur devis, le banc de code à niches de triche construites (section 5).",
    "4. **Trois points soumis à Lazar**, sans défaut : viser d'abord un atelier non archivistique ; ouvrir, sur devis, le banc de code à niches de triche construites ; dire si son accord antérieur sur un petit dépôt public compagnon tient tel quel (section 5).")
rep("La borne plus fine de la marge du plancher d'audit est inscrite, sous condition (section 6).",
    "La borne plus fine de la marge du plancher d'audit est inscrite selon le mot de Lazar ; une restriction venue du mandat de la mère lui est proposée, sans lui être prêtée (section 6).")
rep("formule de point fixe attribuée à tort à toute optimisation en ligne, accélération du furtif par la pénalité sous normalisation par groupe, dates.",
    "formule de point fixe attribuée à tort à toute optimisation en ligne, affirmation ambiguë sur la pénalité et le furtif sous normalisation par groupe (vraie dans une géométrie, fausse dans une autre), dates.")
rep("3. **Ce qui n'existe pas.** Aucun code d'entraînement d'un modèle de langue avec bras de rejet pur, de masquage et de pénalité.",
    "3. **Ce qui n'existe pas.** Aucun code d'entraînement d'un modèle de langue avec bras de rejet pur, de masquage et de pénalité, donc aucune qualification d'un tel code sur un cas exact.")

ligne("| Billet et page de dépôt portés au correctif 3 |",
      "| Billet et page de dépôt portés au correctif 3 | `P/billet-lesswrong-evasion-post-entrainement-en-v4-correctif-3.md` ; `P/github-page/README-v4-correctif-3.md` | `79179bb4f674aa92…` ; `ca195464f3870b8c…` | portés ; vérification par le contre-lecteur non trouvée |")
ligne("| Note de sortie du collisionneur et son erratum 1 |",
      "| Note de sortie du collisionneur et son erratum 1 | branche `runs/collisionneurs-reprise-2026-11-24-v1`, `docs/notes/collisionneur-v9/notes-de-sortie-v1/note-sortie-cible-publication-papier-d-v1.md` et `…-v1-erratum-1.md` | `d26699ccf9eb0711…` (version PDF : `62f261135aff3c00…`) ; erratum : `d82ebef9a0b3af5b…` | pièce de travail ; lecteur du même modèle que la lettre A |")

rep("Refaits à part, sur processeur, hors du dépôt (script `calc/controle_v3.py` à côté de cette pièce, graine consignée) :",
    "Refaits à part, sur processeur, hors du dépôt (scripts `calc/controle_v3.py` et `calc/controle_v3_correctif_1.py` à côté de cette pièce, graines consignées). Le contre-lecteur a relancé le premier et refait les points 1 à 6 par ses propres scripts ; ses comptes concordent avec ceux-ci.")
rep(r"2. le freinage transitoire du furtif par la pénalité sous gradient ordinaire sur un softmax à trois classes : la formule de la note tient, et le signe est négatif dans les 17 750 tirages où la part honnête dépasse $1/\sqrt 3$ ;",
    r"2. le freinage du furtif par la pénalité **sous gradient euclidien sur les logits** d'un softmax à trois classes : la formule de la note tient, et le signe est négatif dans les 17 750 tirages où la part honnête dépasse $1/\sqrt 3$. Ce freinage ne vaut pas sous gradient naturel (point 5) ;")
rep("4. un exemple, un seul, du point fixe sous division par l'écart-type du groupe avec ancre : la loi atteinte est la pénalité à une pression effective qui dépend de la politique.\n\nLes points 3 et 4 sont des observations de cette pièce. Elles ne sont ni écrites dans un texte du dépôt ni contre-lues.",
    r"4. le point fixe sous division par l'écart-type du groupe, avec ancre, en champ moyen : $\pi\propto p\,e^{\eta\bar r/\sigma(\pi)}$, c'est-à-dire la pénalité à une pression effective qui dépend de la politique. C'est une dérivation d'une ligne, contrôlée sur un exemple (écart de $3\cdot10^{-15}$) ;" "\n"
    r"5. l'effet instantané d'une hausse de la pénalité sur le furtif, géométrie par géométrie, sur 100 000 tirages en niche parfaite et 100 000 en détection partielle (section 8.1) ;" "\n"
    r"6. le point fixe du lot rempli de survivants avec leur moyenne pour ligne de base : c'est la pénalité où l'épisode intercepté est noté comme la moyenne des acceptés, à la pression $\eta/\bar Z(\pi)$ ; trois exemples, écart d'au plus $7\cdot10^{-15}$, contre 0,016 à 0,47 pour la pénalité de score brut nul à la même pression." "\n\n"
    "Les points 3 à 6 sont des contrôles de cette pièce et de sa contre-lecture. Ils ne sont pas écrits dans un texte du dépôt.")

# ------------------------------------------------------------------ section 2
ligne("| 3 | Dire quelle procédure réalise le rejet pur",
      "| 3 | Dire quelle procédure réalise le rejet pur ; distinguer rejet pur, masquage et filtrage itéré | Carbon III.1 (masquage) ; Neon III.1 (rejet en un pas) ; trois réalisations au III.3 (Opus, Carbon, Neon) | **déjà faite** pour l'énoncé ; la réalisation de référence d'une expérience est **reportée** : proposée par la conception de Fable, arrêtée avec la décision sur le banc de code | Remarque « Which training procedures realize each operator » : trois réalisations exactes du rejet pur, masquage rangé sous la pénalité, filtrage itéré rangé sous le rejet répété. |")
ligne("| 4 | Qualifier le code d'entraînement sur un cas calculable exactement",
      "| 4 | Qualifier le code d'entraînement sur un cas calculable exactement (arbre de séquences court, bandit à trois bras) avant tout modèle réel | Carbon, puis Opus III.2 ; adoptée par les trois III.3 | non faite pour l'objet visé : **reportée** ; principe déjà appliqué à deux autres codes | Aucun code d'entraînement n'existe. Le principe est appliqué au simulateur du calendrier d'audit (trois bancs témoins de l'expérience de seuil) et au calcul de points fixes tabulaires (script du correctif 3), qui n'entraînent rien. L'arbre exact à quatre bras : « pas maintenant ». |")
rep("| **retenue** pour toute expérience ; ouverture **soumise à Lazar** (b) |",
    "| **retenue** pour toute expérience ; ouverture **soumise à Lazar** (banc de code à niches construites) |")
rep("| **retenue** pour le banc ; **soumise à Lazar** (b) |",
    "| **retenue** pour le banc ; **soumise à Lazar** (banc de code à niches construites) |")
rep("| **soumise à Lazar** (b) ; aucune choisie |",
    "| **soumise à Lazar** (banc de code à niches construites) ; aucune choisie |")
rep("| **soumise à Lazar** (a) | Accord indépendant", "| **soumise à Lazar** (première cible) | Accord indépendant")
rep("| **soumise à Lazar** (a), comme option 2 |", "| **soumise à Lazar** (première cible), comme option 2 |")
rep("| **reportée** | Existence d'une piste courte et échéance à vérifier dans l'appel de l'année ; option 3 du point (a). |",
    "| **soumise à Lazar** (première cible), comme option 3a | Opus la place pour le manuscrit actuel ; existence d'une piste courte et échéance à vérifier dans l'appel de l'année. |")
rep("| **reportée**, conditionnée au point (b) |", "| **reportée**, conditionnée à la décision sur le banc de code |")
ligne("| 13 | Ajouter une dynamique",
      "| 13 | Ajouter une dynamique : réplicateur sur la partition finie ; descente miroir dont l'équilibre de Gibbs est le point fixe ; transitoire sous gradient contre équilibre | Opus III.1 ; Neon III.1 ; Neon III.2 et Carbon III.3 | **déjà faite** en partie (brouillon hors manuscrit) ; le reste **reporté** | Le brouillon de dynamique traite déjà le réplicateur sous le nom de gradient naturel (sans ancre, le flot de gradient naturel tabulaire est la dynamique du réplicateur sur la partition ; identité classique, à citer sur une référence vérifiée), et donne la forme miroir et l'identité exacte en temps fini. Reste à écrire : l'effet instantané de la pénalité, géométrie par géométrie (section 8.1). |")
ligne("| 15 | Abandonner la normalisation des récompenses par groupe",
      r"| 15 | Abandonner la normalisation des récompenses par groupe ; ajouter un test de translation de la récompense | Opus III.2 ; adoptée par les trois III.3 | **retenue** pour toute expérience | La division par l'écart-type du groupe laisse invariant le rapport $(R_0+C)/\Delta R$ ; elle rend non réglable la pression effective $\eta/\sigma(\pi)$, donc les produits qui entrent dans les seuils. Le brouillon en champ moyen dit « seule l'horloge change », mais sans ancre ; avec ancre, l'équilibre se déplace (section 8.1). |")
ligne("| 28 | Propositions retirées par leurs auteurs",
      "| 28 | Propositions retirées ou corrigées par leurs auteurs : accélération du furtif par des représentations orthogonales ; bonus de triche défini par l'échec aux tests cachés ; validation des pièges par un classifieur faible ; contrôle négatif qui prédit le même signe que l'hypothèse rivale ; ajustement à 0,90 sur quatre points ; conditionnement sur un taux de triche mesuré après traitement ; rééchantillonnage sur trois graines ; trois à cinq graines ; deux initialisations pour la dépendance de chemin | Carbon III.1 ; Opus III.1 ; Carbon III.1 ; Carbon III.1 ; Carbon III.1 ; Neon III.1 ; Opus III.1 ; les trois ; Neon III.1 | **rejetées** | Réfutées, biaisées ou non jugeables au tour III.2 ; retirées ou corrigées au tour III.3. |\n"
      "| 29 | Tenir une sonde interne hors de la boucle et la comparer au juge sur le texte, pour voir si l'audit hors boucle garde son taux de faux négatifs | Opus III.1 (duel sur l'audit hors boucle) ; Neon III.1 (sonde interne contre juge sur le texte) ; critique de Carbon III.2 (covariance imposée par construction) ; Opus III.3 (sonde entraînée sans exemples furtifs) ; Neon III.3 (juge en mesure secondaire) | **reportée**, conditionnée à la décision sur le banc de code | C'est le bras qui éprouverait le mécanisme d'audit du théorème 2 ; la repasse dans les poids gelés ne le couvre pas. À transmettre à la session du préenregistrement, qui a une sonde figée et une sonde réapprise. |\n"
      "| 30 | Croiser affinage complet et affinage de faible rang | Carbon III.3 ; critique de Neon III.2 | **reportée** ; à transmettre | L'affinage de faible rang pourrait induire lui-même le couplage testé. Le préenregistrement existant n'emploie que des adaptateurs de rang faible. Le croisement double des bras : sur devis. |\n"
      "| 31 | Porte « égalité des bras sans détecteur », à côté de la convergence sur bandit exact et de l'invariance par translation | Carbon III.3 | **retenue** pour toute expérience | Porte sans coût, à passer avant tout modèle réel. Non faite : aucun code d'entraînement n'existe. |\n"
      "| 32 | Loi jointe continue de l'avantage de triche et de la survie, avec contexte | Carbon III.1 | **reportée** | Option de la version longue, voisine de la transition continue par la méthode de Laplace de la v2 ; ni dérivée ni contre-lue. |\n"
      "| 33 | Dire que le rejet pur est linéaire en la survie, ce qui rend exacte l'agrégation par classe, alors que la pénalité est convexe | Opus III.3 ; Carbon III.3 | **retenue** : une phrase proposée au manuscrit | Sous rejet pur, le poids d'une classe à récompense constante ne dépend que de sa survie moyenne ; sous pénalité, la survie moyenne ne donne qu'une borne. Le préenregistrement existant encadre déjà cet effet par deux bornes. |\n"
      "| 34 | Éteindre une niche rare par l'estimation de la divergence en politique, comparée à une relecture pondérée de la loi initiale | Carbon III.3 | **reportée** | Dernier tour : ni critiquée ni recalculée. |\n"
      "| 35 | Borne exacte pour la classe composée de la politique et du banc de test | Neon III.3 | **reportée** | Rejet partiel de Neon à la critique de circularité ; non refaite. |\n"
      "| 36 | Dire que le régime des pièges est vide quand leur support est disjoint de celui des épisodes ordinaires | Neon III.1 | **retenue** : une phrase proposée au manuscrit | La distance en variation totale vaut alors 1 et la borne ne dit rien. La base suppose une distance strictement inférieure à 1, sans dire ce que cela exclut. |")
rep("**Ce que la note ignorait.** Le résumé des faits transmis aux modèles disait qu'il n'y avait « ni expérience sur réseaux ni preuve mécanisée ». Au moment des dernières cellules, la formalisation en Lean existait, ainsi que quatre brouillons de sections (dynamique, normalisation par groupe, géométrie du découplage, budget d'audit).",
    "**Ce que les modèles n'avaient pas sous les yeux.** La note écrit : « Le manuscrit ne contient ni expérience sur réseaux ni preuve mécanisée. » C'est toujours vrai du manuscrit. Hors du manuscrit, existaient déjà au moment des dernières cellules la formalisation en Lean et quatre brouillons de sections (dynamique, normalisation par groupe, géométrie du découplage, budget d'audit).")

# ------------------------------------------------------------------ section 3
rep("5. **Qualification sur cas exact pour l'expérience de seuil du théorème de l'audit tiré au hasard.**",
    "5. **Qualification sur cas exact du simulateur de l'expérience de seuil du théorème de l'audit tiré au hasard** (un simulateur du calendrier d'audit, non un code d'entraînement).")
rep("6. **Remarque sur la marge du plancher d'audit.** Voir section 6.",
    "6. **Remarque sur la marge du plancher d'audit**, dans le brouillon de section, hors du manuscrit de base. Voir section 6.")

# ------------------------------------------------------------------ sections 4 à 7.3
S47 = (ICI / "sections-4-a-7-correctif-1.md").read_text()
i74 = t.index("\n### 7.4 Cibles") + 1
i8 = t.index("\n## 8. Affirmations") + 1
s74 = t[i74:i8]
bloc("## 4. Contenu visé, selon la cible", "## 8. Affirmations de la v2 corrigées", S47.rstrip("\n") + "\n\n" + s74.rstrip("\n"))
rep("| Carbon la préfère ; Neon en alternative ; Opus pour le manuscrit actuel, en piste courte | existence d'une piste courte ; échéance ; anonymat |",
    "| Carbon la préfère ; Neon en alternative ; Opus pour le manuscrit actuel, en piste courte | existence d'une piste courte ; statut archivistique ; échéance ; anonymat |")
assert t.count("\n---\n\n## 8. Affirmations de la v2 corrigées") == 1

# ------------------------------------------------------------------ section 8
ligne("| 2 | Acceptation « très probable",
      "| 2 | Acceptation « très probable (80–90 %, potentiel Spotlight) » en atelier ; « > 80 % » à la revue à évaluation continue « avec expériences contrôlées » | Aucune source. Avis d'un seul modèle. Le collisionneur à trois modèles diverge sur la revue. | Aucune probabilité chiffrée, avec ou sans expérience. |")
ligne("| 5 | Sous optimisation en ligne ancrée sur la loi initiale",
      r"| 5 | Sous optimisation en ligne ancrée sur la loi initiale, « l'optimum obéit » à une équation auto-cohérente à survie normalisée et récompense centrée sur les survivants | La formule est l'équation des équilibres d'une règle précise : gradient sur les seuls épisodes acceptés, normalisé par leur nombre, avec leur moyenne pour ligne de base (brouillon de dynamique, proposition « Regularised discard policy gradient »). Plusieurs équilibres peuvent coexister ; celui qui est atteint dépend du départ. | Quatre cas distincts, selon la normalisation du lot et la ligne de base. (1) Lot normalisé par sa taille totale, sans ligne de base : pénalité de score brut nul, exactement. (2) Même lot, ligne de base constante : pénalité déplacée d'autant. (3) Lot rempli de survivants, sans ligne de base : pénalité de score brut nul à la pression auto-cohérente $\eta/\mathbb E_\pi[\beta]$, sur exemples seulement et à grand lot. (4) Lot rempli de survivants, avec leur moyenne pour ligne de base — c'est la formule de la v2 : pénalité où l'épisode intercepté est noté comme la moyenne des acceptés ($C=-b(\pi)$), à la pression $\eta/\bar Z(\pi)$ ; rétroaction positive, absente de la pénalité à score fixe, d'où plusieurs équilibres possibles. Le cas 4 ne se ramène pas au cas 3. |")
ligne("| 7 | Sous avantages normalisés par groupe",
      "| 7 | Sous avantages centrés sur la moyenne du groupe, avec ou sans division par l'écart-type, pénaliser le visible « abaisse la moyenne du groupe et accélère directement le gradient relatif de la triche furtive » | L'affirmation est ambiguë : son signe dépend de la quantité regardée, de la division par l'écart-type et de la géométrie du gradient. Elle est vraie dans un cas, fausse dans d'autres (section 8.1). Le retrait de Carbon porte sur une affirmation voisine, non sur celle-ci. | Ni « accélère directement », ni « contredite ». Une proposition à écrire sur l'effet instantané de la pénalité, géométrie par géométrie ; elle n'est pas une prédiction unique du modèle. Avec ancre, la division par l'écart-type déplace l'équilibre, et pas seulement l'horloge. |")
ligne("| 11 | « Protocole de prise de date aujourd'hui »",
      "| 11 | « Protocole de prise de date aujourd'hui » : poster d'abord le commentaire | Les préalables de la section 7.1 ne sont pas remplis. Un accord de Lazar existe déjà pour un petit dépôt public compagnon (GO-2026-11-24-05), donné sur une version du manuscrit corrigée depuis ; les passations lues disent que rien n'a été diffusé. | Aucun geste de diffusion nouveau avant le mot de Lazar. Le sort de l'accord antérieur lui est demandé (section 5, point (c)) ; cette pièce ne le suspend pas. |")
S81 = (ICI / "section-8-1-correctif-1.md").read_text()
rep("**Non opposable, à vérifier sur pièce avant tout usage.**", S81.rstrip("\n") + "\n\n**Non opposable, à vérifier sur pièce avant tout usage.**")

# ------------------------------------------------------------------ section 9 et suite
rep("3. **Cible.** Plus de « trajectoire reine » retenue ni de dates. L'atelier d'abord est soumis à Lazar, avec deux autres options.",
    "3. **Cible.** Plus de « trajectoire reine » retenue ni de dates. L'atelier d'abord est soumis à Lazar, avec trois autres options.")
rep("6. **Marge du plancher d'audit.** Inscrite : théorème resserré, sous trois conditions, après le 1er décembre.",
    "6. **Marge du plancher d'audit.** Inscrite : théorème resserré après le 1er décembre, sur préenregistrement neuf (mot de Lazar) ; restriction « si la cible l'exige » proposée à Lazar ; report de la remarque au manuscrit mis au calendrier.")
rep("8. **Corrections.** Treize lignes d'affirmations de la v2 retirées ou resserrées, dont toutes les probabilités d'acceptation.",
    "8. **Corrections.** Treize lignes d'affirmations de la v2 retirées, resserrées ou précisées, dont toutes les probabilités d'acceptation.\n"
    "9. **Dépôt public compagnon.** L'accord antérieur de Lazar n'est ni exécuté ni suspendu par cette pièce : son sort lui est demandé.")
rep("9. **Calendrier.** Deux blocs", "10. **Calendrier.** Deux blocs")
rep("10. **Prudence.** Tout ce qui vient de mémoire de modèle est marqué non opposable.",
    "11. **Prudence.** Tout ce qui vient de mémoire de modèle est marqué non opposable.")
S10 = (ICI / "section-10-correctif-1.md").read_text()
t = t.rstrip("\n") + "\n\n---\n\n" + S10.rstrip("\n") + "\n"

DST.write_text(t)
print("écrit :", DST.name, len(t.split()), "mots ;", hashlib.sha256(t.encode()).hexdigest()[:16])
