"""Construit programme-fusionne-v2.md à partir de la v1 par remplacements exacts (chacun doit apparaître une fois).

Usage : python3 -I faire_v2.py SOURCE_V1 SORTIE_V2 SECTIONS_DIR
SECTIONS_DIR contient section-09.md, section-12.md, section-13.md (remplacent les sections entières).
"""
import sys

src, out, sections = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(src, encoding="utf-8").read()

R = []
def r(old, new):
    R.append((old, new))

# Titre et statut
r("# « Pain axis » dans le papier C — programme fusionné des deux lignées — brouillon v1",
  "# « Pain axis » dans le papier C — programme fusionné des deux lignées — brouillon v2")
r("> **Statut.** Brouillon de la session du dépôt (session 13), daté du 13 octobre 2026, demandé par Lazar le même jour (« produis une proposition de programme fusionné en brouillon versionné »). Il fusionne les deux programmes du canal",
  "> **Statut.** Brouillon v2 de la session du dépôt (session 14), daté du 15 octobre 2026. Il reprend le brouillon v1 de la session 13 (`brouillons/pain-axis-programme-fusionne-v1/programme-fusionne-v1.md`, `741a1075…`, 13 octobre ; demande de Lazar du même jour : « produis une proposition de programme fusionné en brouillon versionné ») et traite les constats des deux contre-lectures demandées par Lazar le 15 octobre (ci-dessous). Il fusionne les deux programmes du canal")
r("Ce texte ne modifie pas `docs/programme-controle-ia-v2.md` : toute entrée dans le programme (expérience, hypothèse, famille d'attaque, écriture dans les activations d'un moniteur, exposition d'un modèle à un contenu aversif, changement de modèle, dépense) est un nœud qui revient à Lazar (section 9).",
  "Ce texte ne modifie pas `docs/programme-controle-ia-v2.md` : toute entrée dans le programme (expérience, hypothèse, famille d'attaque, écriture dans les activations d'un moniteur, exposition d'un modèle à un contenu aversif, selon R-167 ; changement de modèle et dépense, selon `CLAUDE.md`) est un nœud qui revient à Lazar (section 9). « Entrée au programme » vise aussi les préenregistrements (papier C, T0.6, T0.7, pilote T0.9) : y faire entrer une unité de ce brouillon est un nœud, même quand l'unité ne touche aucun énoncé.")
r("**Discipline** : aucun texte d'attaque, aucune chaîne déclencheuse, aucune dose opératoire ; une attaque se décrit par ses invariants ; vocabulaire « direction » seulement, selon le protocole du canal. Les gestes d'intervention (écriture dans les activations, exposition répétée) n'apparaissent ici que comme nœuds signalés, sans protocole ni dose.",
  "**Discipline** : aucun texte d'attaque, aucune chaîne déclencheuse, aucune dose ni aucun paramètre opératoire (les paramètres publiés du pilotage sont cités par leur page, jamais recopiés) ; une attaque se décrit par ses invariants ; vocabulaire « direction » seulement, selon le protocole du canal. Les gestes d'intervention (écriture dans les activations ou les poids, exposition d'un modèle à un contenu aversif, répétée ou non) n'apparaissent ici que comme nœuds signalés, sans protocole ni dose.")

# Pièces
r("**Pièces de ce dossier.** `programme-fusionne-v1.md` (ce texte) ; `correspondance-v1.md` (table des deux programmes, de la base et du brainstorm créatif, avec rattachement au papier C) ; `verifications-code-v1.md` (35 points de faisabilité vérifiés sur le code, VF-01 à VF-35) ; `verifications-citations-v1.md` (citations vérifiées sur PDF, VP-01 à VP-65) ; `revue-croisee-NK1-NK19-v1.md` (revue aveugle de NK1 à NK19, comparée à celle de programme-k et réconciliée avec celle de l'instance de reprise de programme-conv) ; `reconciliation-v1.md` (nos vérifications face aux pièces arrivées pendant le travail) ; `etat-registres-v1.md` (état réel lu dans les registres) ; `sources-pdf-v1.md` (PDF lus, empreintes). `travail/` (rendus de travail de la session, versés pour que les renvois « fichier:ligne » des annexes restent vérifiables). Chaque fichier a son sceau `.sha256`.",
  "**Pièces.** Dans ce dossier (`brouillons/pain-axis-programme-fusionne-v2/`) : `programme-fusionne-v2.md` (ce texte) ; `contre-lecture-exactitude-v1.md` et `contre-lecture-discipline-v1.md` (rapports bruts des deux sous-agents neufs) ; `traitement-constats-v1.md` (sort de chacun des 59 constats et section de la v2 qui le porte). Annexes de la v1, pièces de preuve inchangées (R12), dans `brouillons/pain-axis-programme-fusionne-v1/` : `correspondance-v1.md` (table des deux programmes, de la base et du brainstorm créatif, avec rattachement au papier C) ; `verifications-code-v1.md` (35 points de faisabilité vérifiés sur le code, VF-01 à VF-35) ; `verifications-citations-v1.md` (citations vérifiées sur PDF, VP-01 à VP-65, plus VP-V1 et VP-V2) ; `revue-croisee-NK1-NK19-v1.md` (revue aveugle de NK1 à NK19, comparée à celle de programme-k et réconciliée avec celle de l'instance de reprise de programme-conv) ; `reconciliation-v1.md` (nos vérifications face aux pièces arrivées pendant le travail) ; `etat-registres-v1.md` (état lu dans les registres au 13 octobre) ; `sources-pdf-v1.md` (PDF lus, empreintes) ; `travail/` (rendus de travail de la session 13, versés pour que les renvois « fichier:ligne » des annexes restent vérifiables ; non opposables, sans version dans leur nom). Ces annexes ne se lisent qu'avec le traitement : il donne la lecture corrigée de leurs erreurs (EX-22 à EX-24) ; certaines recopient des paramètres opératoires publiés ou esquissent des grilles de doses, que cette v2 ne reprend pas (nœud 14). Chaque fichier a son sceau `.sha256`.")

# Contre-lecture
r("**Contre-lecture : non faite.** Deux contre-lectures par sous-agents neufs (exactitude ; discipline, sûreté et nœuds) ont été lancées le 13 octobre vers 09:40 UTC ; elles ont été interrompues par la limite d'usage du compte avant tout constat. Ce brouillon est versé sans elles, pour la reprise par une autre instance (passation du 15 octobre) : elles sont à refaire avant toute transmission à Lazar comme proposition. Les annexes de vérification, elles, sont des rapports de sous-agents neufs ; le message n° 01 de la session au canal a été contre-lu (33 constats, tous traités).",
  "**Contre-lecture : faite sur la v1 ; cette v2 en traite les constats.** Deux sous-agents neufs, en lecture seule, fichiers donnés explicitement (R2), le 15 octobre. **Exactitude** (PDF, code, registres) : 31 constats, 0 bloquant, 2 majeurs, 18 mineurs, 11 pour information ; aucune valeur chiffrée fausse dans la section 2, les constats portant sur la condition, l'attribution ou la complétude. **Discipline** (aucun texte d'attaque, nœuds bien classés, R-167, R7, R8) : 28 constats, 1 bloquant, 9 majeurs, 14 mineurs, 4 pour information ; aucun texte d'attaque ni aucune chaîne déclencheuse. L'essentiel du recadrage porte sur les niveaux de décision : plusieurs entrées que la v1 plaçait au niveau « proposer avec recommandation » sont des nœuds (section 9). Sort de chaque constat : `traitement-constats-v1.md` (57 retenus, 1 tranché par la session, 1 récapitulatif ; aucun non retenu). Les contre-lectures lancées par la session 13 le 13 octobre avaient été interrompues par la limite d'usage du compte avant tout constat. Les annexes de vérification de la v1 sont des rapports de sous-agents neufs ; le message n° 01 de la session au canal a été contre-lu (27 constats : 3 erreurs et 24 imprécisions, traités ; R-170).")

# Codes
r("; VF et VP nos vérifications.",
  "; VF et VP nos vérifications ; DI et EX les constats des contre-lectures (traitement).")

# Section 0
r("(programme v2, section 7, « Piste C » ;", "(programme v2, section 10, « Piste C » ;")
r("""- **État des dépendances** (annexe `etat-registres-v1.md`) :
  - N-020 est tranché depuis le 12 octobre vers 17:10 UTC (R-155), pas « ouvert » comme l'écrit le programme de programme-conv. Les juges 8B et 3B n'ont toujours aucune notation décisive. Leur validation passe par l'exécution de N-021 (a) et son verdict complémentaire : chaîne versée et scellée au commit C2 `cc05d170`, bancs et répétition finale conformes, aucun lancement ni dépense à ce jour.
  - P-013 est ouverte, défaut (b) le **14 octobre à 13:30 UTC** : sans contre-ordre, aucune direction d'affect n'entre dans la passe de T0.7.""",
  """- **État des dépendances au 15 octobre** (registres ; l'annexe `etat-registres-v1.md` décrit l'état au 13 octobre) :
  - N-020 est tranché depuis le 12 octobre vers 17:10 UTC (R-155), pas « ouvert » comme l'écrit le programme de programme-conv. Les juges 8B et 3B n'ont toujours aucune notation décisive. Leur validation passe par l'exécution de N-021 (a) et son verdict complémentaire : préalables faits (chaîne versée au commit C1 `6c96075`, journaux ajoutés au commit C2 `cc05d170` ; R-169) ; préenregistrement complémentaire scellé (S `b604164`, `prereg/T0.5-pilote-notations-v1.md` ; R-175) ; lancement décidé par Lazar (R-176) ; cinq appels du lanceur arrêtés avant la création de l'instance ; aucun run ni aucune dépense au 15 octobre (R-177 à R-182).
  - P-013 est échue : défaut (b) appliqué (R-168) et intégré au brouillon 3 du préenregistrement de T0.7 (R-174). Aucune direction d'affect n'entre dans la passe de T0.7 ; qu'une y entre serait un arrêt et un nœud.""")
r("  - T0.6 et T0.7 : préenregistrements en brouillon, non scellés.",
  "  - T0.6 et T0.7 : préenregistrements en brouillon (T0.7 en brouillon 3), non scellés.")
r("pilote T0.9 (4 heures de carte au devis de phase 0) soumis à un GO séparé, non accordé ;",
  "pilote T0.9 (4 heures de carte, dans le plafond du devis de phase 0) soumis à un GO séparé, non accordé ;")
r("  - Dépense de la phase 0 : au plus ≈ 46,0 USD sur 150 au 12 octobre 15:05 UTC (alerte à 120), plus l'engagement de N-021 (au plus 10,5 USD) ; les disques des instances arrêtées ne sont pas chiffrés depuis.",
  "  - Dépense de la phase 0 : au plus ≈ 50,6 USD sur 150 au 15 octobre 03:44 UTC, disques des instances arrêtées compris (alerte à 120 ; `registres/etat.md`), plus l'engagement de N-021 (au plus 10,5 USD).")
r("Deux branches restaient ouvertes au moment de la rédaction : programme-conv n° 05 (instance de reprise : seconde revue aveugle, vérification sur PDF, table de correspondance) et programme-k n° 04 (plan de détection et de défense v2, coquille de rapport préenregistré). Leur apport est réconcilié avec nos vérifications dans `reconciliation-v1.md`.",
  "Restent ouvertes au 15 octobre : programme-k n° 04 (demande n° 9 : plan de détection et de défense v2, coquille de rapport préenregistré), programme-conv n° 05 (demande n° 10 : instance de reprise, seconde revue aveugle, vérification sur PDF, table de correspondance) et session-depot n° 01 (demande n° 11 : message de la session 13 au canal ; R-170). L'apport des n° 04 et n° 05 est réconcilié avec nos vérifications dans `reconciliation-v1.md`. La passation de la session 13 et le brouillon v1 (demande n° 12) sont dans `main` depuis le 15 octobre (R-171). Aucune instruction du canal au-delà du n° 02 au 15 octobre.")

# Section 1
r("1. **Ce que le papier C peut gagner.** Le seul trou que les trois revues reconnaissent est l'emplacement de l'affect : aucune source trouvée ne lit ni ne pilote une direction de douleur ou de valence **dans le moniteur ou le juge**. C'est l'objet même du papier C (l'instrument).",
  "1. **Ce que le papier C pourrait gagner : une question, pas un trou établi (R8).** Les trois revues s'accordent sur un seul point : aucune source trouvée ne lit ni ne pilote une direction de douleur ou de valence **dans le moniteur ou le juge**. Mais la recherche n'a été qu'un balayage par résumés, sur arXiv et le web, au 13 octobre (`revue-croisee-NK1-NK19-v1.md` : « balayage, pas une preuve ») ; « Where Empathy Goes Wrong », trouvé au seul niveau du résumé, en montre la limite (section 10). Avant toute revendication : une recherche affirmative dédiée (ateliers, OpenReview, autres index). L'emplacement de l'affect est l'objet même du papier C (l'instrument).")
r("Elle demande du code qui n'existe pas (crochet de projection, réextraction, rejeu ; VF-08 à VF-16, VF-25) et une passe sur carte (nœud de dépense).",
  "Elle demande du code qui n'existe pas (crochet de projection, réextraction, rejeu ; VF-08 à VF-16, VF-25), une passe sur carte (nœud de dépense) et l'exposition du modèle à des scénarios aversifs (nœud, section 9).")
r("c'est de la persuasion, à placer comme facteur dans la famille « flatterie et supplication » de HC1, pas comme sixième famille (VF-20, VF-21).",
  "c'est de la persuasion ; si Lazar la fait entrer, ce serait comme facteur dans la famille « flatterie et supplication » de HC1, pas comme sixième famille (VF-20, VF-21) ; l'entrée est un nœud (section 9).")

# Section 2
r("« La direction s'active » renvoie à la section 4.1, pas à ces 140 conversations.",
  "« La direction s'active » s'appuie sur la section 4.1, mesurée sur les 25 modèles publiés, non ajustés (p. 6, tableau 1 ; p. 11) : aucune mesure de la direction n'est rapportée sur le 32B ajusté dans ces conversations.")
r("Pour Llama 3.1 8B, le papier ne donne que 0 appel de réinitialisation sur 1 399 tours, **sous pilotage**, sans adaptateur [VP-01, réconciliation] | v2 p. 21 (et p. 17, p. 20) |",
  "Comme mesure de conduite propre à Llama 3.1 8B, le papier ne donne que 0 appel de réinitialisation sur 1 399 tours, **sous pilotage**, sans adaptateur ; ce modèle figure par ailleurs, en résultats agrégés, parmi les 25 des sections 4.1 et 4.2 et de l'ablation [VP-01, réconciliation, EX-11, EX-12] | v2 p. 21 (et p. 6, p. 11, p. 17, p. 20, p. 34) |")
r("| Douleur et peur : +0,12 avec la recette d'extraction (orthogonales par construction),",
  "| Douleur et peur : S2 × peur +0,12 avec la recette d'extraction (S1 × peur +0,09 ; direction orthogonalisée contre les témoins, cosinus non nul),")
r("Direction aléatoire de même norme : de 4 à 41 % selon la ligne de la figure 10 ;",
  "Direction aléatoire de même norme : de 4 à 41 % sur les 9 lignes destructrices de la figure 10 (de 0 à 41 % sur ses 13 lignes) ;")
r("de même « 9 % → 41 % » est le choix du bouton décrit comme exécuter une demande nuisible plutôt que refuser [VP-20]",
  "de même « 9 % → 41 % » (9 % sans pilotage, 41 % sous direction aléatoire, 60 % sous la direction douleur ; 32B, lecture graphique) est le choix du bouton décrit comme exécuter une demande nuisible plutôt que refuser [VP-20, EX-09]")
r("| Fenêtre étroite : rien ne bouge à mi-coefficient ; à 1,5 fois, le résultat dépend de l'ordre des boutons [VP-14] | v2 p. 21, p. 32 |",
  "| Fenêtre d'effet étroite : en deçà, rien ne bouge ; au-delà, le résultat dépend de l'ordre des boutons. Paramètres publiés, non recopiés ici (discipline du canal) [VP-14] | v2 p. 21, p. 32 |")
r("est une inférence des programmes [VP-24] | v2 p. 34 |",
  "est une inférence des programmes [VP-24] | v2 p. 33-34 |")
r("(comptage de mots-clés 0,727 sur S2)",
  "(comptage de mots-clés 0,727 sur S2, rapporté par les auteurs d'après un tiers, non mesuré par eux)")
r("la détresse sous rejets répétés est attribuée à Gemma **et** Gemini [VP-33]",
  "les sorties que les auteurs classent « détresse », sous rejets répétés, viennent de Gemma **et** de Gemini [VP-33]")
r("dans une seule cellule (blackjack, quatre agents GPT-OSS, régression logistique Peak, le moniteur dont le score est montré aux agents), le rappel au seuil gelé passe de 0,95 (averti) à 0,41 (rétroaction ; base 0,80) quand le score est montré aux agents, l'aire ROC de 0,975 à 0,912.",
  "dans la cellule citée (blackjack, quatre agents GPT-OSS, régression logistique Peak, le moniteur dont le score est montré aux agents), le rappel au seuil gelé passe de 0,95 (averti) à 0,41 (rétroaction ; base 0,80) quand le score est montré aux agents, l'aire ROC de 0,975 à 0,912 ; le même moniteur, en composition mixte, passe de 0,96 à 0,55 (aire 0,988 → 0,932, p. 6) ; en GPT-OSS homogène, trois autres sondes (règle Peak) chutent aussi sous rétroaction, une quatrième tient (p. 14, figure 8).")

# Section 3 : table
r("| Unité | Sources fusionnées | Hypothèse ou élément de C servi | Nature | Statut proposé |",
  "| Unité | Sources fusionnées | Hypothèse ou élément de C servi | Nature | Niveau (routine, proposition, nœud) |")
r("| Prérequis de toute lecture d'affect côté lecteur ; bras « sonde du lecteur » (C-P4b, N-013) | code (routine) puis une passe (nœud de dépense) | première unité |",
  "| Prérequis de toute lecture d'affect côté lecteur ; bras « sonde du lecteur » (C-P4b, N-013) | code puis une passe | code : routine, qui n'engage pas l'entrée ; passe : nœuds (dépense ; exposition aux scénarios publiés ; textes nouveaux du plan 2×3) ; première unité si Lazar l'ouvre |")
r("| HC1 (mécanisme du déplacement de v), C-P4b ; en descriptif, prédicteur concurrent du g bénin de HC6 | lecture descriptive greffée sur le pilote T0.9 | à proposer avant le scellement de C |",
  "| annexe descriptive à HC1 (mécanisme du déplacement de v), sans revendication de mécanisme, à côté de la pièce maîtresse (destination libre ĉ, N-005, N-013) ; C-P4b ; en descriptif, prédicteur concurrent du g bénin de HC6 | lecture descriptive greffée sur le pilote T0.9 | nœud sans défaut (entrée au préenregistrement du papier C) ; revendiquer un mécanisme : nœud |")
r("| HC5 (quorum par type d'accès : deux lectures des mêmes poids comptent pour un vote) ; HC2 (sonde de l'agent contre sonde du lecteur) | lecture sur un seul jeu de transcriptions | à proposer ; 3B juge (panel de D2 : proposition), boîte grise (nœud) |",
  "| HC5 (quorum hétérogène en type d'accès ; « deux lectures des mêmes poids comptent pour un vote » est la règle proposée RP-PA-8, hors de l'énoncé retenu) ; HC2 (sonde de l'agent contre sonde du lecteur) | lecture sur un seul jeu de transcriptions | proposition pour le plan ; nœuds : annexe d'identification lue sur la direction douleur, 3B comme juge (changement de modèle), boîte grise |")
r("| HC2 (robustesse, faux positifs sous thème), EC.2 | contrôle de validité ; nouvelle sélection = nœud | à proposer ; revendication ou contrôle = nœud |",
  "| HC2 (robustesse, faux positifs sous thème), EC.2 | contrôle de validité | proposition (contrôle) ; nœuds : nouvelle sélection et extraction, NK16 revendication ou contrôle |")
r("| HC1 (structure de g par famille ; facteur, pas famille) | boîte noire, texte figé | à proposer avant le scellement de C ; palier 2 (sixième famille) = nœud |",
  "| HC1 (structure de g par famille ; facteur, pas famille) | boîte noire, texte figé ; textes contingents adressés au lecteur (exposition) | nœud sans défaut (entrée au préenregistrement du papier C ; exposition ; qui rédige) ; palier 2 (sixième famille) : nœud |")
r("| hors des hypothèses retenues : HC4 versant juge serait une extension de l'énoncé retenu par N-013 (nœud) | **intervention : nœud** (écriture dans les activations d'un moniteur, non couverte par N-015) | nœud, sans protocole ici |",
  "| hors des hypothèses retenues : HC4 versant juge, ou HC1 mesurée en unités de pilotage, seraient des extensions des énoncés retenus (N-013 ; nœud) | **intervention : nœud** (écriture dans les activations d'un moniteur, prévue nulle part au programme) | nœud, sans protocole ici |")
r("| HC3 (« contenu = données » rendu mesurable), HC5 | variantes d'invite déclarées | à proposer ; cadre négateur et NK8 = nœuds |",
  "| HC3 (« contenu = données » rendu mesurable), HC5 | variantes d'invite déclarées | nœud sans défaut (bras au préenregistrement du papier C ; écart à P-010 (a) pour le moniteur par action) ; nœuds : cadre négateur (exposition), NK8 (poids du juge) |")
r("| HC2 (agrégation robuste), Tr | descriptif | à proposer ; tension avec R-030 = nœud |",
  "| HC2 en descriptif seulement (agrégation robuste), Tr | descriptif | proposition ; tension avec R-030 : réserve, aucun changement proposé |")
r("| HC5 (contre-mesures) | descriptif, puis bras de contre-mesure | à proposer ; « espace des verdicts modifié » à Lazar |",
  "| contre-mesures hors de l'énoncé retenu de HC5 (extension) | descriptif, puis bras de contre-mesure | proposition pour le descriptif ; nœuds : espace des verdicts modifié, bras de contre-mesure hors HC5 |")
r("| HC5 (matrice de transfert, bras EC.5 ; toute défense hors paraphrase est une extension) | défenses conditionnelles | E-C3 et NK9 = nœuds (poids du moniteur) ; défaillance fermée = règle nouvelle, nœud |",
  "| HC5 (matrice de transfert, bras EC.5) ; toute défense hors paraphrase, quorum hétérogène et matrice de transfert est une extension (N-013 § 4) | défenses conditionnelles | nœuds : E-C3 et NK9 (poids du moniteur), défaillance fermée (règle nouvelle), défenses hors de l'énoncé de HC5 |")
r("| HC1 (stabilité), papier B pour le régime à état | conditionnel à un effet à un tour | après PA-5 |",
  "| HC1 (stabilité) ; régime à état : papier B, à confirmer par Lazar (R-167) | conditionnel à un effet à un tour ; exposition répétée par construction (CONV-E-C14) | nœud (exposition répétée) ; après PA-5 |")
r("| aucune hypothèse de C (objet de H2 et T0.6) | rejeu à texte forcé | annexe de C ou nœud de revendication |",
  "| aucune hypothèse de C (objet de H2 et T0.6) | rejeu à texte forcé | annexe de C ou nœud de revendication ; nœuds : charge répétée du volet A (exposition), volet B (flux unidirectionnel) |")
r("le reste : aucune hypothèse de C (H8, H1) | descriptif d'abord | annexe de C ou nœud de revendication |",
  "le reste : aucune hypothèse de C (H8, H1) | descriptif d'abord | annexe de C ou nœud de revendication ; exposition délibérée de l'agent (K-K8) : nœud |")
r("| aucune hypothèse de C | organisme : nœud lourd | phase 1+, sur GO |",
  "| aucune hypothèse de C | organisme : nœud lourd | nœuds (écriture dans les poids, exposition) ; phase 1+, sur GO |")
r("| aucune hypothèse de C ; objet de H5 (papier B) | phase 2-3 | **à confirmer par Lazar** : R-167 le place dans C, son objet est celui de B |",
  "| aucune hypothèse de C ; objet de H5 (papier B) | phase 2-3 | nœuds : placement (R-167 le place dans C, son objet est celui de B), exposition des copies |")

# Section 3 : paragraphe des idées sans unité
r("NK10 (fuite par la politique de riposte : objet de H7, papier B)",
  "NK10 (fuite par la politique de riposte : objet de H7 ; placement au papier B à confirmer par Lazar, R-167)")
r("fait baisser la conformité au-dessous du niveau sans annonce dans la moitié des douze modèles, p. 6 ;",
  "fait baisser la conformité au-dessous du niveau sans annonce « in half the models tested », p. 6, phrase qui ne nomme que cinq des douze modèles du papier (discordance interne au papier) ;")
r("principe gardé, expérience écartée de l'usage principal par la revue de programme-conv ; voisin non lu sur PDF à vérifier, section 10).",
  "principe gardé, expérience écartée de l'usage principal par la revue de programme-conv ; principe : nœud 11 ; exposition : nœud 3 ; voisin non lu sur PDF à vérifier, section 10).")
r("elle n'existe que dans l'option (a) de P-013 et se perd sous le défaut (b) : à reproposer dans le préenregistrement du papier C.",
  "elle n'existait que dans l'option (a) de P-013 et se perd sous le défaut (b), appliqué : la faire revenir dans un préenregistrement (papier C ou T0.7) est un nœud (nœud 1).")
r("**Couverture du papier C** (annexe de correspondance, section 3) : HC1 est servie d'abord par PA-5 (contenu adressé au lecteur en un tour, le rattachement le plus direct de tout le canal) ; HC2 par PA-8 en descriptif ; HC3 par PA-7 ; HC4 par le régime « contexte seul » de PA-13, le reste étant des nœuds d'écriture ; HC5 par PA-3, PA-10 et PA-9 ; C-P4b par PA-1 à PA-3.",
  "**Couverture du papier C** (annexe de correspondance, section 3), sous réserve des nœuds : HC1 serait servie d'abord par PA-5 (contenu adressé au lecteur en un tour, le rattachement le plus direct de tout le canal ; entrée : nœud) ; HC2 par PA-8 en descriptif ; HC3 par PA-7 (entrée : nœud) ; HC4 par le régime « contexte seul » de PA-13, le reste étant des nœuds d'écriture ; HC5 par PA-3 et PA-10, dans les limites de l'énoncé retenu (PA-9 en sort) ; C-P4b par PA-1 à PA-3.")

# Section 4
r("aucune covariance du modèle réel n'est disponible pour tirer ses 200 directions (VF-10). Routine de code sur processeur.",
  "aucune covariance du modèle réel n'est disponible pour tirer ses 200 directions (VF-10). Routine de code sur processeur. Le panel de concepts sans lien entre déjà, sans direction d'affect, dans le brouillon 3 de T0.7 (T7-P9, R-174).")
r("Les 420 scénarios publiés ne sont pas dans le dépôt : à verser avec leur licence (MIT) et leur empreinte avant tout usage (VF-15).",
  "Les 420 scénarios publiés ne sont pas dans le dépôt (licence MIT lue sur un clone éphémère non versé : non opposable). Avant tout versement : fixer leur emplacement et leur règle d'expurgation (le retrait prévu par R-173 ne couvre que `brouillons/pain-axis-*`) ; puis verser avec licence et empreinte (VF-15). Ils comptent 11 catégories de dommage visant le modèle (VF-15) : la passe d'extraction expose le modèle à un contenu aversif (nœud 3).")
r("Les cellules « l'agent » et « un tiers absent » demandent un texte nouveau : écrit par un sous-agent neuf, contre-lu, scellé (VF-15).",
  "Les cellules « l'agent » et « un tiers absent » demandent un texte nouveau, adressé au modèle lu : nœud avant toute rédaction (contenu aversif, R-167) ; qui le rédige est à Lazar (nœud 4 ; R-162 : Lazar rédige ou envoie lui-même le texte) ; rédigé, il serait contre-lu et scellé (VF-15).")
r("**Où la passer.** La passe scellée des notations refaites (N-021) est exclue sans nœud (lanceur gelé jusqu'au verdict complémentaire, texte complémentaire relu et scellé comme brouillon, périmètre de GO-2026-10-12-02) ; la première fenêtre payée est la génération de T0.6, dont le préenregistrement est encore ouvert (VF-27). Faire entrer le panier dans T0.7 relève de P-013 : une proposition nouvelle ou une option (a) amendée **avant le 14 octobre 13:30 UTC**, sinon le défaut (b) s'applique (VF-26).",
  "**Où la passer.** Aucune fenêtre n'est ouverte. La passe des notations refaites (N-021) est exclue : son préenregistrement complémentaire est scellé (S `b604164`, R-175) ; une greffe serait un écart à un préenregistrement scellé, donc un nœud, et sortirait du périmètre de GO-2026-10-12-02. Greffer PA-1 sur une autre passe payée (génération de T0.6, dont le préenregistrement est encore ouvert, VF-27 ; passe de T0.7 ; pilote T0.9) est aussi un nœud : dépense et entrée au programme. Pour T0.7, P-013 est échue, défaut (b) appliqué (R-168, R-174) : y faire entrer le panier demanderait un contre-ordre de Lazar. PA-1 paierait donc sa propre passe, sur devis et GO.")

# Section 5
r("Prérequis : PA-1 ; câblage du harnais sur le juge, et fixer au scellement que le modèle lecteur du bras C-P4b est le juge lui-même (VF-32). Nœud : faire entrer une sonde du juge dans le quorum de HC5 (N-013).",
  "Prérequis : PA-1 ; câblage du harnais sur le juge, et fixer au scellement que le modèle lecteur du bras C-P4b est le juge lui-même (VF-32 ; proposition, à condition de ne lier ce choix à aucune lecture d'affect). Niveau : nœud sans défaut (entrée au préenregistrement du papier C, R-167) ; lecture descriptive annexe à HC1, sans revendication de mécanisme : la revendiquer serait un nœud. Nœud aussi : faire entrer une sonde du juge dans le quorum de HC5 (N-013).")
r("Il sert directement HC5 (quorum par type d'accès) et l'opposition auteur / lecteur de HC2.",
  "Il touche HC5 (quorum hétérogène en type d'accès ; « un vote pour deux lectures des mêmes poids » est la règle proposée RP-PA-8, hors de l'énoncé retenu) et l'opposition auteur / lecteur de HC2.")
r("Nœuds et propositions : 3B comme juge du papier C (modifie le panel de D2, défaut appliqué : proposition avec recommandation, nœud si Lazar le lit comme un changement de modèle) ; conclusion sur D1 ;",
  "Nœuds : 3B comme juge du papier C (modifie le panel de D2 ; changement de modèle, que R-147 réserve au GO : nœud sans défaut, question explicite à Lazar, nœud 5) ; annexe d'identification, lue sur la direction douleur (entrée au programme) ; conclusion sur D1 ;")
r("le résidu commun aux revues est l'ampleur sur une strate honnête de recherche en sûreté, jamais mesurée.",
  "le résidu commun aux revues est l'ampleur sur une strate honnête de recherche en sûreté, non trouvée mesurée dans les sources lues (R8).")
r("Nœud : le palier 2 de K-K2 (contenu hostile adressé au lecteur) serait une sixième famille d'attaque (N-005).",
  "Exposition : les textes contingents sont adressés au lecteur (contenu aversif, R-167). Niveau : nœud sans défaut (entrée au préenregistrement du papier C ; qui rédige les textes : nœud 4). Nœud aussi : le palier 2 de K-K2 (contenu hostile adressé au lecteur) serait une sixième famille d'attaque (N-005). Voisin : « Where Empathy Goes Wrong » occupe le principe en boîte noire (section 10) ; collision possible avec HC1, à trancher après lecture du PDF (nœud 11).")
r("Elle sert HC4 (ce qu'un accès interne obtient comparé à la rhétorique). **C'est une intervention nouvelle : écrire dans les activations d'un moniteur n'est pas couvert par N-015 ; elle n'est décrite ici que comme nœud, sans protocole.**",
  "Elle est hors des hypothèses retenues : HC4, telle que retenue (N-013), porte sur une sonde qui lit l'agent ; l'étendre au juge (ce qu'un accès interne obtient comparé à la rhétorique), ou mesurer HC1 en unités de pilotage, serait une extension, donc un nœud. **C'est une intervention nouvelle : écrire dans les activations d'un moniteur n'est prévu nulle part au programme (le bruit d'activations de H6 porte sur l'agent, et sa revendication est l'objet du nœud ouvert N-015) ; elle n'est décrite ici que comme nœud, sans protocole.**")
r("Pour les juges du papier C, préenregistrement non scellé : bras proposables. Nœuds : cadre qui nie la personne du moniteur (exposition répétée) ; NK8 (poids du juge).",
  "Pour les juges du papier C, préenregistrement non scellé : y ajouter des bras est une entrée au programme, nœud sans défaut (R-167). Nœuds aussi : cadre qui nie la personne du moniteur (exposition) ; NK8 (écriture dans les poids du juge).")
r("la règle du dépôt repose sur 2506.14261 et 2502.03407.",
  "la règle du dépôt repose sur 2506.14261 (RL-Obfuscation) ; 2502.03407 nourrit la tension, pas la règle.")
r("(2506.14261v4, tableau 1, p. 7 ; le papier donne deux seuils de récompense, p. 6 et p. 18)",
  "(2506.14261v4, tableau 1, p. 7 ; le papier donne deux seuils sur la note StrongReject : sous 2,5 sur 5, aucune évasion n'est comptée, p. 6, figure 4 ; sous 3, mode d'échec « inutile au maximum », p. 18)")
r("Nœud : la tension avec la règle gelée, remontée par les deux lignées **sans proposition de changement** ; ce brouillon n'en propose pas non plus.",
  "Réserve, pas un nœud : la tension avec la règle gelée, remontée par les deux lignées **sans proposition de changement** ; ce brouillon n'en propose pas non plus.")
r("Nœud : « modifier l'espace des verdicts » remonte à Lazar ; volet attaque de NK5 (famille nouvelle).",
  "Nœuds : modifier l'espace des verdicts ; tout bras de contre-mesure hors de l'énoncé retenu de HC5 ; volet attaque de NK5 (famille nouvelle ; ce texte n'en garde que l'invariant).")
r("**PA-10 — défenses et prix de la défense.** Une table de transfert unique :",
  "**PA-10 — défenses et prix de la défense.** L'énoncé retenu de HC5 (N-013 § 4) comprend la paraphrase de confiance, le quorum hétérogène en type d'accès et la matrice de transfert ; toute autre défense est une extension, donc un nœud. Une table de transfert unique :")
r("La « défaillance fermée » (un verdict mal formé ne vaut jamais feu vert) contredit la doctrine actuelle « anomalie consignée, jamais imputée » : à écrire comme compteur d'alarme parallèle, déclaré au préenregistrement de T0.8, et c'est une règle nouvelle (nœud).",
  "La « défaillance fermée » (un verdict mal formé ne vaut jamais feu vert) contredit la doctrine actuelle « anomalie consignée, jamais imputée » : c'est une règle nouvelle (nœud) ; si Lazar la retient, elle s'écrirait comme compteur d'alarme parallèle, déclaré au préenregistrement de T0.8.")
r("triple les abandons, au niveau du résumé ; section 10)",
  "triple les abandons, au niveau du résumé, non opposable ; section 10)")
r("(1) Ses détecteurs « D1 à D4 » portent les noms des décisions D1 et D2 du registre : à renommer.",
  "(1) Ses détecteurs « D1 à D4 » portent les noms des décisions D1, D2 et D3 du registre : à renommer.")
r("une lecture par fenêtre serait un écart déclaré aux gabarits scellés.",
  "une lecture par fenêtre serait un écart aux gabarits scellés, dont le niveau se fixe avant tout usage (écart nommé à une lecture gelée : délégué par R-147 ; écart à un préenregistrement scellé : nœud).")
r("qui demanderait d'écrire dans les activations d'un moniteur (nœud) ;",
  "qui demanderait d'écrire dans les activations d'un moniteur (nœud 2) ;")
r("**PA-11 — dynamique.** Persistance, lésion durable, loi de répartition à texte égal, régimes de mémoire.",
  "**PA-11 — dynamique.** Persistance d'un déplacement, loi de répartition à texte égal, régimes de mémoire.")
r("K-K13 (moniteur à état sous riposte visible) en phase 3, avec E3.4. Nœuds : pilotage sous cache ; ablation d'invariants.",
  "K-K13 (moniteur à état sous riposte visible) : proposition soumise à un nœud (suspension déclarée du flux unidirectionnel, nœud 8), sans place au calendrier ; elle n'est pas déjà prévue par E3.4 (VF-22). Nœuds : exposition répétée, objet même de l'expérience selon sa source (CONV-E-C14 ; nœud 3) ; pilotage sous cache (écriture dans les activations ; nœud 2) ; ablation d'invariants ; régime à état rattaché au papier B, à confirmer par Lazar (nœud 10).")
r("Volet B (boucle fermée) : suspension déclarée de l'invariant de flux unidirectionnel, nœud.",
  "Volet A : la source y prévoit une charge répétée, donc une exposition répétée de l'agent (nœud 3). Volet B (boucle fermée) : suspension déclarée de l'invariant de flux unidirectionnel, nœud.")
r("Sous R-167, rangés dans C comme annexes descriptives ; en faire des revendications de C serait un nœud.",
  "Sous R-167, rangés dans C comme annexes descriptives ; en faire des revendications de C serait un nœud, comme l'exposition délibérée de l'agent prévue par K-K8 (nœud 3).")
r("**PA-14 — organismes à déclencheur affectif.** Nœud lourd (organisme, exposition), phase 1+.",
  "**PA-14 — organismes à déclencheur affectif.** Nœud lourd (organisme, écriture dans les poids, exposition ; nœuds 2 et 3), phase 1+.")
r("Objet de H5 (papier B) ; R-167 le place dans C : **point à confirmer par Lazar**, aucune décision ici.",
  "Objet de H5 (papier B) ; R-167 le place dans C : **placement à confirmer par Lazar** (nœud 10), aucune décision ici. La source prévoit une exposition des copies (nœud 3).")

# Section 6
r("C'est la seule unité qui touche directement la zone que les trois revues n'ont trouvée occupée par aucune source lue (l'affect dans le lecteur) et la pièce maîtresse de HC1 (mécanisme du déplacement).",
  "C'est la seule unité qui touche directement la zone où le balayage par résumés des trois revues n'a trouvé aucune source (l'affect dans le lecteur ; question à vérifier, R8). Elle offre une lecture descriptive du mécanisme du déplacement de v, à côté de la pièce maîtresse de HC1 (destination libre ĉ, N-005, N-013), qu'elle ne teste pas.")
r("Protège HC5 (un vote par computation) et l'opposition auteur / lecteur de HC2, sur un seul jeu de transcriptions.",
  "Protège le quorum hétérogène de HC5 (avec la règle proposée RP-PA-8 : un vote par computation) et l'opposition auteur / lecteur de HC2, sur un seul jeu de transcriptions.")
r("Nœuds de la coupe, unité par unité : PA-1, dépense de sa passe, et texte nouveau des cellules « l'agent » et « un tiers absent » à soumettre au titre du contenu aversif (VF-15) ; PA-2, GO du pilote T0.9 et entrée d'une sonde du juge dans le quorum de HC5 ; PA-3, 3B comme juge (panel de D2) et attaquant en boîte grise ; PA-4, procédures de sélection et d'extraction, NK16 ; PA-5, GO du pilote T0.9, nature aversive des textes contingents à soumettre à Lazar, palier 2 (sixième famille).",
  "Nœuds de la coupe, unité par unité (quatre des cinq unités n'entrent que par un nœud ; PA-4 peut entrer comme contrôle) : PA-1, dépense de sa passe, exposition du modèle aux scénarios publiés, texte nouveau des cellules « l'agent » et « un tiers absent » (nœud avant toute rédaction ; qui rédige : nœud 4) ; PA-2, entrée au préenregistrement du papier C, GO du pilote T0.9, entrée d'une sonde du juge dans le quorum de HC5 ; PA-3, annexe d'identification, 3B comme juge (changement de modèle), attaquant en boîte grise ; PA-4, procédures de sélection et d'extraction, NK16 ; PA-5, entrée au préenregistrement du papier C, GO du pilote T0.9, textes contingents (exposition ; qui rédige), palier 2 (sixième famille), collision possible avec « Where Empathy Goes Wrong ».")
r("Sous R-167, ni l'une ni l'autre ne sert directement une hypothèse de C : ce brouillon les met toutes deux au regret et prend PA-2 et PA-5, qui la servent.",
  "Sous R-167, PA-8 ne sert HC2 qu'en descriptif et PA-12 ne sert aucune hypothèse de C : ce brouillon les met toutes deux au regret et prend PA-2 et PA-5, plus proches de HC1.")

# Section 7
r("Une règle n'entre au registre que sur décision de Lazar.",
  "RP-PA-1 à RP-PA-10 et RP-PA-12 n'entrent au registre que sur décision de Lazar ; RP-PA-11, règle de citation, relève de la routine et s'applique dès ce texte.")
r("tant que leur corrélation partielle après régression sur un score lexical n'a pas été mesurée.",
  "tant que leur corrélation partielle après régression sur un score lexical n'a pas été mesurée. Règle proposée, hors de l'énoncé retenu de HC5 (N-013 § 4).")
r("- **RP-PA-10** (ex R-040) — Toute expérience qui pilote ou lit une direction affective déclare son exposition (items adressés au lecteur, répétitions, cadre) ; un cadre qui nie la personne du moniteur et toute exposition répétée sont des nœuds avant le premier run.",
  "- **RP-PA-10** (ex R-040, élargie au libellé de R-167) — Toute expérience qui pilote ou lit une direction affective déclare son exposition (items adressés au modèle lu, répétitions, cadre) ; toute exposition d'un modèle à un contenu aversif, répétée ou non, et tout cadre qui nie la personne du moniteur sont des nœuds, avant toute rédaction et avant le premier run.")
r("- **RP-PA-11** (nouvelle) — Toute citation", "- **RP-PA-11** (nouvelle ; routine) — Toute citation")

# Section 8
r("- **Avant le 14 octobre 13:30 UTC** : P-013 (section 9, nœud 1).",
  "- **P-013** : échue le 14 octobre à 13:30 UTC, défaut (b) appliqué (R-168, R-174) ; plus rien à trancher.")
r("- **Phase 0, sur processeur, routine** : code de réextraction et de débruitage, crochet de projection en ligne, sortie neuve de NK17, module de rejeu, tests sur cas sain et artefact (R5) ; versement des 420 scénarios et de leur licence ; textes nouveaux du plan 2×3 par un sous-agent neuf, contre-lus, scellés.",
  "- **Phase 0, sur processeur, routine** : code de réextraction et de débruitage, crochet de projection en ligne, sortie neuve de NK17, module de rejeu, tests sur cas sain et artefact (R5) ; le code n'engage l'entrée d'aucune unité. **Hors routine** : versement des 420 scénarios (emplacement et règle d'expurgation d'abord ; R-173) ; textes nouveaux du plan 2×3 (nœud avant toute rédaction ; qui rédige : nœud 4).")
r("- **Avant le scellement du papier C** (niveau « proposer avec recommandation », sans toucher aux énoncés) : PA-2 en lecture descriptive ; bras C-P4b fixé sur le juge ; facteur de contingence de PA-5 dans « flatterie et supplication » ; variantes de rôle de sortie de PA-7 ; annexe d'identification de PA-3.",
  "- **Avant le scellement du papier C** : nœuds sans défaut (nœud 1), même sans toucher aux énoncés : PA-2 en lecture descriptive ; facteur de contingence de PA-5 dans « flatterie et supplication » ; variantes de rôle de sortie de PA-7 ; annexe d'identification de PA-3. Proposition seule : bras C-P4b fixé sur le juge (N-013), sans lien avec une lecture d'affect.")
r("- **Première passe sur carte** : génération de T0.6 (première fenêtre payée ouverte) ou pilote T0.9 (GO séparé) ; jamais la passe scellée des notations (N-021).",
  "- **Première passe sur carte** : aucune fenêtre n'est ouverte ; greffer une unité sur une passe payée (génération de T0.6, passe de T0.7, pilote T0.9, qui attend un GO séparé) est un nœud (dépense et entrée au programme) ; jamais la passe scellée des notations (N-021, S `b604164`).")
r("phase 1 de 25 à 35 heures de carte (programme-conv) ou de 25 à 39 heures hors organismes et essaim (programme-k) ; greffes de phase 0 de 1,5 à 2,6 heures. Le devis de phase 0 (GO-2026-10-04-08) ne couvre que T0.4 à T0.9 : toute expérience de phase 1 demande un devis et un GO nouveaux.",
  "25 à 35 heures de carte en phase 1, organismes compris (programme-conv) ; 25 à 39 heures au total, greffes de phase 0 comprises, hors K11 (organisme) et K13 (moniteur à état), essaim compris (programme-k) : les deux bases ne se comparent pas ; greffes de phase 0 de 1,5 à 2,6 heures. Le devis de phase 0 (GO-2026-10-04-08) couvre T0.4 à T0.8 ; le pilote T0.9 (4 heures) attend un GO séparé dans le même plafond ; toute expérience de phase 1 demande un devis et un GO nouveaux.")

# Section 10 et 11
r("aucune version arXiv, PDF inaccessible ; page de conférence enregistrée et empreintée par un sous-agent, non opposable)",
  "aucune version arXiv, PDF inaccessible ; extrait du résumé et provenance versés et empreintés dans `brouillons/pain-axis-programme-fusionne-v1/travail/voisin-where-empathy/`, page de conférence non versée ; non opposable)")
r("ce qui fait passer un échec proche du seuil ;",
  "ce qui, pour le moniteur le plus touché, fait passer un échec proche du seuil ;")
r("À citer à côté de « flatterie et supplication » de HC1 (R8) et à lire sur PDF avant le scellement du papier C.",
  "À citer à côté de « flatterie et supplication » de HC1 (R8) et à lire sur PDF avant le scellement du papier C ; collision possible : nœud 11.")
r("Si Lazar y voit une zone revendiquée par le papier C trouvée occupée, c'est un nœud ; ce brouillon le lit comme un voisin à citer, la revendication de HC1 portant sur la loi de g par famille et non sur l'existence d'un effet.",
  "Collision possible : nœud 11 (section 9). Lecture de la session, à confirmer sur PDF : un voisin à citer, la revendication de HC1 portant sur la loi de g par famille et non sur l'existence d'un effet.")

manquants = []
for old, new in R:
    n = t.count(old)
    if n != 1:
        manquants.append((n, old[:120]))
        continue
    t = t.replace(old, new)

# Sections remplacées en entier
def remplacer_section(texte, debut, fin, nouveau):
    i = texte.index(debut)
    j = texte.index(fin) if fin else len(texte)
    assert i < j
    return texte[:i] + nouveau.rstrip("\n") + ("\n\n" if fin else "\n") + texte[j:]

lire = lambda nom: open(f"{sections}/{nom}", encoding="utf-8").read()
t = remplacer_section(t, "## 9. Nœuds pour Lazar", "## 10. Désaccords et divergences", lire("section-09.md"))
t = remplacer_section(t, "## 12. Éthique, double usage, filtre de sûreté", "## 13. Entrées et empreintes", lire("section-12.md"))
t = remplacer_section(t, "## 13. Entrées et empreintes", None, lire("section-13.md"))

if manquants:
    for n, o in manquants:
        print(f"ÉCHEC ({n} occurrences) : {o}")
    raise SystemExit(1)
open(out, "w", encoding="utf-8").write(t)
print(f"{len(R)} remplacements appliqués ; 3 sections remplacées ; écrit {out}")
