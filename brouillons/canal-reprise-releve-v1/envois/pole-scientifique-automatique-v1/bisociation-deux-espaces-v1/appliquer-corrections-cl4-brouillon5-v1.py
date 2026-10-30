import re, sys
src, dst, heure = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(src, encoding="utf-8").read()

def rep(old, new, n=1):
    global t
    c = t.count(old)
    assert c == n, (c, old[:80])
    t = t.replace(old, new)

H4 = "7e4557b14c3a6e662c28c8a77e4582a752f17164361baa55a3f0632cb6522a61"
HC4 = "0ad1be93f2e4996dfcf581a59fab3f151477a670191e0f9140ce356a0de3cf37"

# Titre et en-tête
rep("— v2 — BROUILLON 4 (version soumise au gel de Lazar), NON SCELLÉ",
    "— v2 — BROUILLON 5 (version soumise au gel de Lazar ; corrections de la contre-lecture 4), NON SCELLÉ\n\n"
    "Brouillon 5 : corrections N1 à N4, N5 et N7 de la contre-lecture 4 appliquées par conv-audit (Opus 5.5), relevé `date -u` "
    + heure + " UTC le 30 octobre 2026, sur le brouillon 4 (Sonnet 5.5, `" + H4[:8] + "…`), inchangé ailleurs. **Aucun chiffre calculé, "
    "aucun seuil, aucune valeur recommandée n'est modifié** ; seules changent des phrases (N1, N4, N5, N7), les deux racines de graines (N2) "
    "et la définition opérationnelle de l'issue de l'audit et de V7 (N3).")

# N1 — résumé point 4
rep("0,78 / 0,75 sur toute la fourchette honnête de cette avance (−3 à +9 points en « moyen »)",
    "0,78 / 0,75 sur toute la fourchette de transfert de cette avance (−3 à +9 points en « moyen »)")
rep("Tout repose sur une seule donnée de la version 1 dont le transfert n'est pas vérifié.",
    "Tout repose sur une seule donnée de la version 1 dont le transfert n'est pas vérifié. **Ces trois chiffres supposent en outre "
    "l'avance propre du concept (P4, N − N_β0) entre +3 et +8 points, fourchette sans aucune donnée** (opinion de l'auteur : la "
    "version 1 n'avait pas de canal de concepts) ; sous la forme F-A de S3, l'adoption vaut 0,88 / 0,82 à P4 = 3, 0,23 à P4 = 2,5 et "
    "0,00 à P4 = 1,5 (script § 17 ; contre-lecture 4, N1).")

# résumé point 7
rep("Une contre-lecture 4 courte, ciblée sur ce qui est nouveau, est recommandée avant le scellement.",
    "La contre-lecture 4 est faite (Sonnet 5.5 neuf, rapport `" + HC4[:8] + "…`) : « soumettable avec corrections mineures » ; N1 à N4 "
    "sont corrigés dans ce brouillon 5, N5 et N7 appliqués, N6 noté ; selon son rapport, aucune nouvelle contre-lecture complète n'est nécessaire.")

# nœud ouvert 3
m = re.search(r"\*\*Contre-lecture 4 : recommandée\*\*[^\n]*", t)
assert m and t.count("**Contre-lecture 4 : recommandée**") == 1
t = t[:m.start()] + ("**Contre-lecture 4 : faite** (Sonnet 5.5 neuf, rapport `" + HC4[:8] + "…`, « soumettable avec corrections "
    "mineures ») ; N1 à N4 corrigés, N5 et N7 appliqués, N6 noté (section « Contre-lecture »). **Réserve d'indépendance** : le "
    "contre-lecteur 4 est du même modèle que l'auteur du brouillon 4 (Sonnet 5.5) — instance neuve et non-auteur (R2 tenue), "
    "indépendance de modèle non tenue (Fable indisponible, limite d'usage ; R-539). Les corrections du brouillon 5 sont d'Opus 5.5.") + t[m.end():]

# N1 — réserve 5
rep("la probabilité d'adoption dépend presque uniquement de l'avance de l'éloignement seul (N_β0) sur b en « moyen » (section « Prédiction ») ;",
    "la probabilité d'adoption dépend de **deux** grandeurs, de sensibilité comparable sous S3 = F-A (script § 17 ; contre-lecture 4, N1) : "
    "l'avance propre du concept P4 (N − N_β0), dont la fourchette +3 à +8 n'a **aucune donnée** (adoption 0,88 / 0,82 à P4 = 3, 0,23 à "
    "2,5, 0,00 à 1,5), et l'avance de l'éloignement seul (N_β0) sur b en « moyen » (section « Prédiction ») ; pour cette dernière,")
rep("La section « Prédiction » porte cette incertitude dans ses fourchettes :",
    "La section « Prédiction » porte l'incertitude de transfert dans ses fourchettes (celle de P4 non : P4 y est pris entre 3 et 8, sans source) :")

# N1 — confiance de P4
rep("0,90 (plafonnée : la fourchette suppose que le générateur ne fait pas échouer le canal, CB3-04, non mesuré) |",
    "**sans donnée** : fourchette d'auteur (la version 1 n'avait pas de canal de concepts ; la fourchette suppose aussi que le générateur "
    "ne fait pas échouer le canal, CB3-04, non mesuré) ; aucune confiance chiffrée (contre-lecture 4, N1 : la valeur 0,90 du brouillon 4 est retirée) |")
rep("P4 1,00 → 0,90 ;",
    "P4 : aucune confiance chiffrée (fourchette sans donnée ; la règle donnerait 1,00 → 0,90 par construction, toute la fourchette étant au-dessus de δ) ;")
rep("(script § 19 ; 0,78 / 0,75 au § 16)",
    "(script § 19 ; 0,78 / 0,75 au § 16 ; P4 pris entre +3 et +8, sans donnée)")

# N5
rep("| > 0 ; −5 à 0 ; 0 à +3 |", "| > 0 (signe seul, sans grandeur prédite) ; −5 à 0 ; 0 à +3 |")
rep("| croissante | pente > 0 |", "| croissante | pente > 0 (signe seul, sans grandeur prédite ; descriptive) |")

# N4 — validation
rep("**Validation du générateur, avant toute méthode, sur graines distinctes",
    "**Validation du générateur, avant les bras candidats (N et ses ablations ; seuls les témoins d1c et c y sont calculés, pour V9 ; "
    "contre-lecture 4, N4), sur graines de validation (RACINE_VALIDATION, indices 0 à 299, § 7)")
rep("J vraie est un **déclencheur d'audit R4** (probabilité 0,02 à effet nul, 0,92 pour un effet parasite de +3, script § 21), jamais un arrêt.",
    "J vraie est un **déclencheur d'audit R4** (probabilité 0,02 à effet nul, 0,92 pour un effet parasite de +3, script § 21), jamais un "
    "arrêt ; **l'audit qu'il déclenche est rendu et scellé avant l'invocation unique des mondes de décision (§ 9)**, qui n'a pas lieu tant qu'il ne l'est pas.")
rep("validation du générateur (V1 à V9 ; V9 ne calcule que d1c et c) →",
    "validation du générateur (V1 à V9 ; V9 ne calcule que d1c et c ; si V9 déclenche l'audit, il est rendu et scellé avant l'invocation "
    "ci-dessous, contre-lecture 4, N4) →")
rep("Contre-lecture 3 (faite) puis 4 si demandée →", "Contre-lecture 3 (faite) puis 4 (faite ; corrections intégrées au brouillon 5) →")
rep("| Validation du générateur ratée (V1 à V6, plafond de l'oracle S8) | arrêt avant toute méthode ;",
    "| Validation du générateur ratée (V1 à V6, plafond de l'oracle S8) | arrêt avant les bras candidats (N et ses ablations) ;")
rep("les méthodes sur 200 mondes de validation de M_bien et de M_moyen",
    "les méthodes sur 200 mondes de validation de M_bien et de M_moyen (RACINE_VALIDATION, indices 300 à 499, disjoints de ceux de V1 à V9)")

# N3 — V7
rep("- **V7 (rapport sans seuil, CB-13)**", "- **V7 (rapport sans seuil et sans conséquence, CB-13)**")
rep("si la loi de κ montre un monde mal réglé (par exemple des paires de fond partagé qui dominent les paires valides, ou un recouvrement "
    "des lois de κ entre vrai et faux pont), la conséquence est une version nouvelle du préenregistrement (R12), non un réglage (CB2-03).",
    "**V7 ne déclenche rien** (contre-lecture 4, N3 : le jugement « monde mal réglé » du brouillon 4 n'avait pas de critère opérationnel, "
    "il est retiré) : un canal de concepts mal réglé se lit seulement par les règles écrites — J (Table 1 ligne 8, Table 2 ligne 4), A7 "
    "(Table 1 ligne 9) et les déclencheurs d'audit —, jamais par un jugement sur V7 ; aucun paramètre n'est modifié après sa lecture (CB2-03). "
    "Une version nouvelle motivée par V7 ne peut être écrite qu'après le verdict scellé (R12).")

# N3 — audit
rep("relance sur les graines de validation (RACINE_VALIDATION) ; test de permutation. **Issue** : « artefact trouvé » → verdict **non "
    "concluant** et version nouvelle du préenregistrement (R12) ; « aucun artefact » → les tables ci-dessous s'appliquent telles quelles, "
    "le rapport d'audit étant scellé.",
    "relance sur les graines de validation (RACINE_VALIDATION) ; test de permutation = recalcul du placebo N_PCg (permutation globale des "
    "vecteurs de concepts) sur ces graines. **Issue, sans autre jugement (contre-lecture 4, N3)** : « artefact trouvé » si et seulement si "
    "le rapport d'audit scellé constate l'une au moins des trois choses suivantes : (i) un bras lit un champ latent (exception `AccesLatent` "
    "levée à la relance, ou appel à un champ de `Latent` trouvé par le balayage statique dans le code d'un bras) ; (ii) sur les graines de "
    "validation, la borne basse à 99 % de Δ(N_PCg, N_β0) est > 0 ; (iii) une erreur de code nommée (fichier, ligne, effet), avec un essai "
    "sain et un essai d'artefact (R5) écrits par le sous-agent d'audit, dont la correction déplace, sur les graines de validation, au moins "
    "un contraste décisif de plus que sa demi-largeur à 95 %. Sinon : « aucun artefact ». « Artefact trouvé » → verdict **non concluant** "
    "et version nouvelle du préenregistrement (R12) ; « aucun artefact » → les tables ci-dessous s'appliquent telles quelles, le rapport "
    "d'audit étant scellé.")

# N2 — racines
rep("- Chaque tâche reçoit `numpy.random.SeedSequence(entropy=RACINE,",
    "- **Racines (contre-lecture 4, N2)** : RACINE = 20261101 pour les mondes de décision ; RACINE_VALIDATION = 20261102 pour la "
    "validation du générateur (V1 à V9, indices 0 à 299), les 200 mondes de validation de l'étape (1) du § 9 (indices 300 à 499) et "
    "l'audit. Deux entiers fixés par ce texte avant toute exécution, sans lien avec un résultat, recopiés au manifeste ; aucune autre "
    "racine n'est permise. Les rôles de validation emploient `entropy=RACINE_VALIDATION` avec les mêmes clés de dérivation.\n"
    "- Chaque tâche reçoit `numpy.random.SeedSequence(entropy=RACINE,")
rep("| numpy < 1.25 | arrêt (R9) |",
    "| numpy < 1.25 | arrêt (R9) |\n| Racine du manifeste différente de RACINE ou de RACINE_VALIDATION du § 7, ou monde de décision tiré avec RACINE_VALIDATION | arrêt (R9) ; V0 fausse |")

# Journal des changements
rep("### Ce qui change par rapport au brouillon 3 (constat CB3-xx → où)",
    "### Ce qui change par rapport au brouillon 4 (contre-lecture 4, N1 à N7 → où)\n\n"
    "Source : `bisociation-deux-espaces-v1/contre-lecture-preenregistrement-bisociation-v2-brouillon4.md` `" + HC4 + "` (verdict : "
    "soumettable avec corrections mineures ; N1 à N4 avant scellement ; sortie du script reproduite au bit près).\n\n"
    "1. **N1 (moyenne)** — l'incertitude de P4 est dite : résumé point 4, nœud ouvert 5, confiance de P4 retirée (« sans donnée »), "
    "note des confiances, ligne de gel ; « fourchette honnête » devient « fourchette de transfert » ; « presque uniquement » corrigé.\n"
    "2. **N2 (faible à moyenne)** — racines fixées : RACINE = 20261101, RACINE_VALIDATION = 20261102, indices de validation disjoints "
    "(0 à 299 pour V1 à V9, 300 à 499 pour l'étape (1)) ; ligne d'arrêt ajoutée (§ 7 ; Liste d'arrêt).\n"
    "3. **N3 (faible)** — issue de l'audit définie par trois constatations (i) à (iii) ; V7 sans conséquence (le jugement « monde mal "
    "réglé » est retiré, faute de critère ; les faux ponts partagent par construction un concept rare latent, de sorte qu'un critère de "
    "recouvrement des lois de κ entre vrais et faux ponts aurait été faux).\n"
    "4. **N4 (faible)** — « avant toute méthode » devient « avant les bras candidats » ; l'audit de V9 est rendu et scellé avant "
    "l'invocation unique (§ 6, § 9, Liste d'arrêt).\n"
    "5. **N5 (facultative, appliquée)** — P7 (première partie) et P12 : « signe seul, sans grandeur prédite ».\n"
    "6. **N6 (note)** — gardée telle quelle : δ et F-A sont justifiés aux centres d'auteur, sans résultat de v2 ; le garde-fou est ce que "
    "l'adoption autorise.\n"
    "7. **N7 (mécanique, appliquée)** — entrée « Contre-lecture 4 » remplie (deux empreintes, traitement de chaque remarque).\n\n"
    "### Historique — ce qui avait changé entre le brouillon 3 et le brouillon 4 (constat CB3-xx → où)")

# N7 — entrée contre-lecture 4
m = re.search(r"^- Contre-lecture 4 : À REMPLIR[^\n]*", t, re.M)
assert m
t = t[:m.start()] + (
    "- **Contre-lecture 4** : sous-agent neuf, Sonnet 5.5 (`claude-sonnet-5-5`), non-auteur de ce brouillon, des brouillons 1 à 3, du "
    "script de puissance et du recoupement (même modèle que l'auteur du brouillon 4 : réserve d'indépendance de modèle, Fable indisponible, "
    "R-539). Brouillon relu : `preenregistrement-bisociation-deux-espaces-v2-brouillon4.md`, empreinte `" + H4 + "`. Rapport : "
    "`bisociation-deux-espaces-v1/contre-lecture-preenregistrement-bisociation-v2-brouillon4.md`, empreinte `" + HC4 + "`. Conclusion du "
    "rapport : soumettable avec corrections mineures (N1 à N4 avant scellement, N5 à N7 facultatives ou mécaniques) ; CB3-01 à CB3-09 "
    "traités ; sortie du script reproduite au bit près ; aucune nouvelle contre-lecture complète nécessaire après N1 à N4. Le brouillon 5 "
    "n'est pas la version relue.\n\n"
    "  Traitement de chaque remarque :\n\n"
    "  | Constat | Gravité | Traitement | Où |\n"
    "  |---|---|---|---|\n"
    "  | N1 incertitude de P4 hors de la fourchette | moyenne | accepté : P4 « sans donnée », sensibilité dite (0,88 / 0,82 ; 0,23 ; 0,00), "
    "« fourchette de transfert », « presque uniquement » corrigé | Résumé 4 ; nœud 5 ; Prédiction ; Ligne de gel |\n"
    "  | N2 racines non fixées | faible à moyenne | accepté : valeurs fixées au texte, indices disjoints, ligne d'arrêt | § 7 ; Liste d'arrêt |\n"
    "  | N3 audit et V7 sans critère | faible | accepté : trois constatations (i) à (iii) ; V7 sans conséquence | Audit de symétrie ; V7 |\n"
    "  | N4 « avant toute méthode » et ordre de V9 | faible | accepté : « avant les bras candidats », audit de V9 avant l'invocation | § 6 ; § 9 ; Liste d'arrêt |\n"
    "  | N5 P7 et P12 sans grandeur | faible | accepté : signe seul, dit | Prédiction |\n"
    "  | N6 seuils aux centres d'auteur | note | noté, sans changement : aucun résultat de v2, adoption limitée au descriptif | — |\n"
    "  | N7 mécanique | note | accepté : cette entrée | Contre-lecture |") + t[m.end():]

# Ligne de gel
rep("(brouillon 4) aux valeurs recommandées", "(brouillon 5) aux valeurs recommandées")
rep("probabilité d'adoption intégrée sur ces fourchettes 0,78 / 0,75 (0,63 / 0,60 sur −6 à +9)",
    "probabilité d'adoption intégrée sur ces fourchettes 0,78 / 0,75 (0,63 / 0,60 sur −6 à +9), **en supposant P4 entre +3 et +8 sans "
    "donnée** (0,23 à P4 = 2,5)")
rep("**Contre-lecture 4** : demandée, ciblée sur les ajouts de l'auteur du brouillon 4 ; le scellement attend son rapport.",
    "**Contre-lecture 4** : faite (Sonnet 5.5 neuf, `" + HC4[:8] + "…`, « soumettable avec corrections mineures »), corrections N1 à N4 "
    "lues dans le brouillon 5, réserve d'indépendance de modèle lue.")
rep(", « contre-lecture 4 non demandée »", "")

open(dst, "w", encoding="utf-8").write(t)
print("REMPLIR restants:", t.count("À REMPLIR"))
