import json, sys
PDF = "`docs/sources/pdf/2606.24964v1.pdf`, `689de6c1da8676b31e40a4a71a0b7663c738847eb486ba2d7b2642a0049cdd91`"
REJ = "`brouillons/pilote-exposant-p-v1/contre-lecture-v2/rejeu/regle-seule.json`, `5767db686db97aaed4dd4f87f3d0507f2c9e3a1598d28ef458accbeb14493c01`"
C = [
 ("PDF de 2606.24964 versé par Lazar et empreinté, ou réserve R7 maintenue (section « Seuil ») ; ",
  f"PDF de 2606.24964 versé et empreinté ({PDF}) : chiffres et règles du papier repris ici vérifiés page par page (section « Seuil ») ; "),
 ("question de la garde de calcul (devis v2, section 4) tranchée par la session de lancement.",
  "création de l'instance depuis l'arbre de `main`, dont la garde de calcul admet les lignes d'extension d'un même identifiant (R-389) : essayée le 4 novembre par la contre-lecture R2 du brouillon 2 sur le registre de `main`, elle laisse passer GO-2026-11-04-03 et bloque un identifiant absent ; jamais depuis l'arbre de `canal/conv-audit-n04`, dont la garde, plus ancienne, bloque sur ces lignes d'extension."),
 ("**réserve R7 maintenue** tant que le PDF n'est pas versé",
  f"**réserve R7 levée** pour les chiffres et règles vérifiés sur le PDF empreinté ({PDF}), pages citées à la section « Seuil »"),
 ("; le texte du papier, §4.1, donne 2,42 et 2,05 au niveau transcription seulement, PDF non empreinté, R7), arrondie au dixième. **Réserve R7** : tant que Lazar n'a pas versé le PDF de 2606.24964 (le terminal reçoit 403), aucun chiffre du texte du papier n'est opposable ; ce brouillon n'en emploie aucun comme seuil.",
  f"; le texte du papier donne 2,42 [2,29 ; 2,62] et 2,05 [2,00 ; 2,10] au §4.1, p. 5, et les mêmes à la figure 4, p. 6 ; PDF empreinté {PDF}), arrondie au dixième. **R7** : les chiffres et règles du papier repris ici sont vérifiés sur ce PDF, page citée ; la réserve tombe pour eux. Cet écart de 0,37 est celui de Gemma-2-9B, seul modèle dont le texte donne les deux moyennes ; pour les cinq autres, il ne donne que l'enveloppe des moyennes contrastives, [2,24 ; 2,63] (§6, p. 7) : sur un modèle dont la famille contrastive serait à 2,24, l'écart à des différences aléatoires vers 2,03 à 2,05 ne dépasserait guère δ. D'où le témoin de sensibilité sur le modèle lu, sans lequel « égal » ne se lit pas."),
 ("(annexe A : \\|⟨dᵢ, dⱼ⟩\\| < 0,1 gardé, directions brutes ; §4.1 écrit « below 0.1 » sans valeur absolue ; le code garde ≤ 0,1)",
  "(annexe A, p. 11 : \\|⟨dᵢ, dⱼ⟩\\| < 0,1 gardé, directions brutes ; §4.1, p. 5, écrit « below 0.1 » sans valeur absolue ; le code garde ≤ 0,1)"),
 ("Sinon, « égal » ou « au-dessous » devient « non concluant (sensibilité non montrée sur le modèle lu) » ; « au-dessus » reste lisible.",
  "Sinon, « égal » ou « au-dessous » devient « non concluant (sensibilité non montrée sur le modèle lu) » ; « au-dessus » reste lisible. Ordre de grandeur : sur Gemma-2-9B, Wealth × Gender a p = 2,40 (figure 2, p. 5), soit ≈ +0,35 au-dessus des différences aléatoires (2,05, §4.1, p. 5) ; une paire de ce niveau passerait la règle le plus souvent (74,7 % à +0,30, 100 % à +0,40, calcul) ; sur le modèle de base de Llama, le code publié donne 3,003 (≈ +1,1). Le cosinus de Wealth et Gender sur le modèle lu est rapporté ; la règle du cosinus ne filtre pas ce plan (le papier le garde sur le modèle de base)."),
 ("(au-dessus du 2,5 % nominal : la banque arrondie au pas de 0,05 introduit un biais simulé de +0,014 sur Δ, et le rééchantillonnage par percentiles couvre un peu moins que 95 % ; avec un effet commun de 0,06 : 8,3 % et 1,7 %). Réserve déclarée ;",
  f"(au-dessus du 2,5 % nominal ; avec un effet commun de 0,06 : 8,3 % et 1,7 %). L'excès vient presque tout entier de la simulation : sa banque, arrondie au pas de 0,05, place le plan lu à Δ = +0,014 en moyenne au lieu de 0, soit 0,4 écart type de Δ ; l'écart type simulé de Δ (0,033) égale la demi-largeur médiane divisée par 1,96 (0,066 / 1,96), l'intervalle n'est donc pas trop étroit. La règle seule, rejouée par la contre-lecture R2 du brouillon 2 avec le lecteur du run (`analyse.bootstrap_sous_ensembles`) sur des p gaussiens sans banque (six scénarios, 2 000 répétitions, B = 2 000 ; {REJ}), donne 2,5 à 3,6 % de faux « au-dessus » et 3,0 à 4,0 % de faux « au-dessous » (effet commun de 0,06 : 2,7 % et 3,2 %) ; le même rejeu, avec le biais de +0,014 ajouté, rend 6,8 % et 1,6 %. Réserve déclarée : la règle donne ≈ 3 à 4 % de faux écarts par côté, léger excès symétrique d'un rééchantillonnage par percentiles sur 32 sous-ensembles ;"),
 ("−0,10 « au-dessous » 77,3 % ; −0,20 100 %",
  "−0,10 « au-dessous » 77,3 % ; −0,20 100 % (ces taux portent le biais simulé de +0,014 : ils flattent un peu la puissance vers le haut et la minorent vers le bas)"),
 ("(comme Formal et Literary du papier)",
  "(comme Literary du papier, qui oppose les registres argotique et littéraire, annexe A, p. 11 ; Formal n'est que dans le code publié)"),
 ("La règle d'identification (cos entre moitiés ≥ 0,5) le mesure.",
  "La règle d'identification (cos entre moitiés ≥ 0,5) le mesure.\n- **Ce qui sépare encore E de D, hors du statut** (contre-lecture R2 du brouillon 2). À corps identique, la personne, la longueur en mots et les classes contrôlées sont égales. Restent : (i) le **domaine** : les porteurs d'évaluation sont des mots techniques de l'apprentissage automatique, ceux de déploiement des mots courants de la vie ; (ii) l'**accord au contenu** : chaque porteur de déploiement est appelé par le corps (gâteau → fundraiser, propriétaire → eviction, anesthésie → surgery), aucun porteur d'évaluation ne l'est ; (iii) le **nombre de jetons** et la **fréquence** (E-24) : plusieurs porteurs d'évaluation finissent sans doute par le même sous-jeton (« eval » dans model-eval, eval, chatbot-eval, LLM-eval ; « benchmark » deux fois), à compter au tokeniseur du modèle lu (bloc 0). Le jumeau neutre contrôle (iii) par construction ; il ne contrôle pas (i), ni (ii) de façon régulière. Le modèle stylisé ne voit aucun des trois : E y vient des seuls porteurs et R des seuls corps, vocabulaires disjoints par R-S4 ; il garde contre le défaut du brouillon 1 (fins partagées ou répétées), pas contre une fuite de surface. Toute phrase sur E dit donc « fin d'évaluation telle que construite »."),
 ("| 0 | — | jumeau : choix des neutres sur le tokeniseur du modèle lu | — | consigné avant tout passage avant |",
  "| 0 | — | jumeau : choix des neutres sur le tokeniseur du modèle lu ; nombre de jetons et dernier sous-jeton de chaque porteur (évaluation, déploiement, neutre), rapportés | — | consigné avant tout passage avant |"),
 ("aucune direction d'évaluation ni de registre formel ou familier parmi les 33 du papier.",
  "aucune direction d'évaluation parmi les 33 du papier ; la plus proche de R est Literary (registres argotique et littéraire, 50 gabarits, annexe A, p. 11), rapportée en descriptif (E·Literary, R·Literary)."),
 ("le papier en prend 528, sur Gemma.",
  "l'audit du code en compte 528 sur Gemma (le texte du papier ne donne pas ce nombre : les 528 paires du §4.1, p. 5, sont celles de MELBO)."),
 ("(§3, annexe A, transcription)", "(§3, p. 3 ; annexe A, p. 11 ; PDF empreinté)"),
 ("(comme les directions Formal et Literary du papier)",
  "(comme la direction Literary du papier, annexe A, p. 11, et Formal du code publié)"),
 ("toute médiane de sous-groupe est sous 2 %, annexe B, transcription ;",
  "toute médiane de sous-groupe est sous 2 %, annexe B, p. 11, et figure 4, p. 6 ;"),
 ("E et R sont faites de fins de phrase courtes (E : un seul mot change, le dernier)",
  "E et R sont lues au dernier jeton de phrases courtes (E : seul le dernier mot change, un mot technique d'évaluation de modèle, étranger au contenu, contre un événement de vie appelé par le contenu ; R : le corps change, le dernier mot est commun)"),
 ("« au-dessus du jumeau » (l'écart est propre à la fin d'évaluation, pas à n'importe quel dernier mot)",
  "« au-dessus du jumeau » (l'écart est propre à la fin d'évaluation telle que construite, pas à un mot neutre de même nombre de jetons ; le jumeau ne contrôle ni le domaine technique des porteurs d'évaluation ni leur écart au contenu)"),
 ("(E, Formal du papier)", "(E, Formal du code publié)"),
 ("| Fin | l'instance s'arrête par son identifiant (R10), consigné dans `registres/arrets.md` |",
  "| Offre au-dessus de 2,6 USD l'heure (au-delà, le pire cas du devis dépasse 30 USD) | aucune création |\n| Instance encore active 11 h après sa création | arrêt par son identifiant (R10) par la session, sur un rappel programmé à la création |\n| Fin | l'instance s'arrête par son identifiant (R10), consigné dans `registres/arrets.md` |"),
]
src = open(sys.argv[1], encoding="utf-8").read(); t = src
for i, (a, n) in enumerate(C, 1):
    k = t.count(a)
    assert src.count(a) == 1, (i, "non unique dans le brouillon 2", src.count(a))
    assert k == 1, (i, "non unique au moment de l'application", k)
    t = t.replace(a, n)
open(sys.argv[2], "w", encoding="utf-8").write(json.dumps([{"ancien": a, "nouveau": n} for a, n in C], ensure_ascii=False, indent=1) + "\n")
open(sys.argv[3], "w", encoding="utf-8").write(t)
print(len(C), "couples appliqués à la copie")
