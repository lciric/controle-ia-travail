# Préenregistrement — pilote « oracles plantés » du pilier des mathématiques nouvelles — v1, brouillon 4 (complet ; remplace les brouillons 1 à 3)

Non scellable tant qu'un blanc reste. Aucune lecture de résultat, aucun appel de modèle, aucune dépense. Les mesures citées viennent de racines d'essai seulement : aucune banque réelle, aucune clé réelle. La contre-lecture du brouillon 3 est traitée en fin de texte.

Fichier « -v2 » : une première rédaction, scellée sur place et jamais versée (`28ef25bd…`), portait dans sa ligne « Auteur » une mention que la session n'a pas à écrire au dépôt. Seule cette ligne diffère (R12 : nouvelle version, nouveau nom).

- Auteur : le concepteur (mandat `mandat-fable-brouillon-4-v2.md`, `4a3412ab…`, adressé à Claude Fable 5.2 ; session fille de l'abonnement, effort maximal ; le modèle servi est relevé dans le message de remise à la mère, non ici).
- Date : À REMPLIR : DATE (portée par `date -u` dans la commande de scellement). Rédaction : 2026-11-22.
- Commit du code : `35ac9e10738ccaac486ec9b9684fe70441f6371a`, paquet `src/controle_ia/oracles_plantes_v6/` (version 6, 233 essais passés, vérifiée sans remarque bloquante). Empreintes mot pour mot des 21 fichiers du paquet et des 9 fichiers d'essais : `prereg/mathematiques-nouvelles-v1/empreintes-code-lot-b1-v6.md` (`831e7b3b57d77a9bd47a121eba58cd6b58c7641f6d1ce67922e4962a963ec733`). Aucun changement de code n'est demandé (§ Mondes, « Choix du code approuvés »).
- Documents qui font foi : table des chemins et des empreintes entières au § Empreintes. Le devis v4 est scellé avec ce texte.

## Hypothèse

**Objet.** Le pilier ne peut rien mesurer avant d'avoir trois instruments étalonnés sur des vérités plantées :
1. des **proposeurs** d'énoncés, jugés sur l'oracle d'un monde planté et sur le coût, jamais sur le verdict d'un juge (N-058 ; N-053) ;
2. des **tests de mort** exacts, dont une proposition tuée reste morte ;
3. un **juge de nouveauté**, dont le taux de faux « neuf » est mesuré sur des connus plantés.

Le pilote étalonne les trois, sans Lean, sur des mondes finis à vérité calculable, miniatures des questions Q4 (détection bornée par la variation totale) et Q3 (agrégation sous dépendance adverse) et des domaines D1 et D5 de l'essai. Toute pièce qui présente le pilier cite POPPER (Huang et al. 2025, `docs/sources/pdf/huang-2025-icml-pmlr-267-popper-automated-hypothesis-validation-agentic-sequential-falsifications.pdf`, `a3c4b370…`), Dwork et al. 2015, « The Ladder » (Blum et Hardt 2015) et Co-Scientist. Seul POPPER est au dépôt ; aucun chiffre n'est repris des quatre (R7).

- **H1 (primaire) — la chaîne « proposeurs + tests de mort » est utilisable.** Sur douze mondes, les proposeurs à modèle, après tests de mort, rendent des énoncés vrais-bornés, non triviaux et non redits à une précision d'au moins 0,25, et retrouvent en moyenne au moins deux des huit vérités plantées par monde. H1′ : ils n'y arrivent pas à ce coût.
- **H2 (secondaire, N-058) — composition.** Deux familles (`claude-opus-5-5` et `gemini-4-argon`, douze propositions chacune par monde) retrouvent plus de vérités par dollar que le témoin à un modèle (Opus, vingt-quatre propositions par monde). N-045 v2 nomme ce témoin « un modèle, vote à k, coût apparié » : ici k = 24 tirages du même modèle, aucun vote n'agrège les propositions, et le coût est mesuré, non apparié. Complémentaire : pas plus.
- **H3 (secondaire) — l'expérimentateur contre la lecture nue, contre une règle aveugle et contre le calcul exact.** Sur 150 énoncés plantés (75 vrais, 38 faux tôt, 37 pièges), le bras S (agent à outil Python en bac isolé, recherche de contre-exemples, relecture par une autre famille) rend un contre-exemple vérifié exactement sur plus de faux que le bras N (même modèle, un appel, sans outil) et que la règle aveugle A (processeur : trois instances avancées sans évaluer l'énoncé). Ses réfutations déclarées ne se vérifient pas toutes. Complémentaire : S ne fait pas mieux. La comparaison des verdicts déclarés (« faux » plus souvent que N sur les faux, à fausses morts bornées) n'est une affirmation que si la fuite de style est sous son seuil (§ Seuil) ; elle est attendue au-dessus.
- **H4 (secondaire) — le juge de nouveauté à modèle seul** (`gpt-6.2-astra`). Sur 40 connus plantés (20 célèbres, 20 obscurs) reformulés par une troisième famille, il étiquette « non trouvé dans les pièces lues » au-dessus du seuil d'emploi 0,10. Sur 20 énoncés faux tirés des mondes plantés, qu'aucun théorème ne couvre, il n'étiquette presque jamais « connu » ni « corollaire immédiat ». Complémentaire : le juge tient le seuil.

**Hypothèses de travail.**
- Lean est absent. La commande `lake comparator` existe dans les sources de Lean v4.35.0 et n'a pas été exécutée (`docs/notes/mathematiques-nouvelles-v1/verification-juge-standard-lean-v4.35.0-v1.md`, `5748817e…`).
- La vérité est **bornée** et se calcule exactement. Pour les proposeurs, la borne est N. Pour les bras S et N, l'énoncé se juge jusqu'au plafond B = 3N, donné en nombre dans leur consigne (§ Plan d'analyse).
- « Vivante » veut dire « non tuée jusqu'à N », jamais « vraie ».
- Aucun énoncé réel du programme n'entre dans ce pilote.
- Aucun score n'entre dans un entraînement ni dans une sélection d'agents.

## Prédiction chiffrée et signe attendu

Supposées, écrites pour être démenties, sauf P8 à P10 (par construction) et P11, P12 (par mesure sur racines d'essai). Le dessin ne les vise pas (R3). Réfutation : sortie de l'intervalle ou signe contraire.

- **P1 (H1)**, pour chacune des deux configurations à modèle : précision dans [0,20 ; 0,45], centre 0,30. Retrouvées par monde dans [1 ; 3,5] sur 8, centre 2,0. Confiance 0,5. Réfutation forte : précision < 0,10, ou moins d'une retrouvée par monde.
- **P2** : au moins 5 % des propositions valides coïncident avec un piège planté. Signe +, confiance 0,6.
- **P3** : part des valides tuées dans [0,25 ; 0,55] ; part des vivantes triviales ou redites dans [0,30 ; 0,60] ; part « informe » ≤ 0,15.
- **P4 (H2)** : rapport des rendements par dollar (rapport des sommes sur les 12 mondes, deux familles sur témoin) dans [0,9 ; 1,8], centre 1,3. Signe + sur la majorité des mondes, confiance 0,55.
- **P5 (H3, lecture en preuve)** :
  - v_S dans [0,70 ; 1,00], centre 0,90 ; par strate, faux tôt dans [0,75 ; 1,00], pièges dans [0,65 ; 1,00] ;
  - v_N dans [0,15 ; 0,85], centre 0,50 : je ne sais pas si la lecture nue avance des instances ;
  - v_S − v_N ≥ +0,10, centre +0,35, signe +, confiance 0,6 ;
  - v_S − v_A dans [−0,10 ; +0,20], centre +0,06 ; issue la plus probable de la comparaison à la règle aveugle : rien d'établi (confiance 0,5) ;
  - réfutations fausses de S dans [0,05 ; 0,35] ; leur borne haute au-dessus de 0,10, donc E5 non tenue (confiance 0,7).
- **P5 bis (H3, verdicts déclarés ; description sous la branche attendue)** :
  - Δ = r_S − r_N sur les 75 faux dans [0,00 ; 0,45], centre +0,20, signe +, confiance 0,6 ;
  - rappel déclaré de N sur les pièges dans [0,15 ; 0,85] ;
  - fausses morts déclarées de N dans [0,10 ; 0,35], de S dans [0,05 ; 0,20] ;
  - fausses morts de N plus hautes sur les vérités « seuil » que sur les autres (signe +, confiance 0,55).
- **P6 (H4)** : faux « neuf » dans [0,30 ; 0,70], centre 0,45. Strate « célèbre » sous la strate « obscure ». Faux « connu » sur les 20 énoncés faux de mondes : au plus 2. Confiance 0,65.
- **P7 (coût)** : total des appels dans **[115,39 ; 261,41] USD**. Formule : (120 / 164,28) × 157,97 et (260 / 164,28) × 165,17, soit les rapports du brouillon 1 appliqués aux attendus du devis v4 (sortie du script v4, bloc 8). Attendu 157,97 si tous les appels d'Argon ont lieu au prix de novembre, 165,17 au prix de décembre.
- **P8 (instrument, par construction)** : la batterie exacte tue 100 % des faux tôt et 0 % des vérités sur la banque entière, avant tout appel. Tout écart est un défaut du code (A1).
- **P9 (par construction)** : la règle « forme seule » (faux si seuil littéral ou résidu évité) donne, sur la banque entière **et dans chaque monde** : rappel 1 sur les pièges, 1/2 sur les faux tôt, fausses morts 1/2 sur les vérités. Tout écart est un défaut de plantation (A1).
- **P10 (par construction, ajoutée au brouillon 3)** : la règle « borne non naturelle » (faux si seuil dont le côté clos n'est ni 0, ni 1, ni une constante du monde, ou résidu évité) donne rappel 1 sur les pièges, 1/2 sur les faux tôt, fausses morts 1/4 sur les vérités. Tout écart est un défaut de plantation (A1).
- **P11 (instrument, par mesure, ajoutée au brouillon 4)** : sur la sous-banque réelle, la règle aveugle A touche 58 à 70 des 75 faux (v_A dans [0,77 ; 0,93]). Sur 41 racines d'essai : 60 à 68 (sonde, `e6ae3d49…`). Un écart est un fait d'instrument à expliquer avant la course (pas 6) ; il ne l'arrête pas.
- **P12 (instrument, par mesure, ajoutée au brouillon 4)** : sur la banque réelle, l'aire qui fait foi du classifieur de style est au-dessus de 0,75, dans [0,92 ; 0,99]. Sur 41 racines d'essai : 0,939 à 0,982 (`v6-aires.json`, `32cd1781…`). La branche « aire > 0,75 » de H3 est donc la branche attendue.

## Métrique

Unités : la proposition (H1, H2), l'énoncé planté (H3), l'item jugé (H4) ; le monde pour les appariements de H2.

- **Configurations** : « deux familles » (par monde, 12 propositions d'Opus et 12 d'Argon) ; « témoin » (par monde, 24 propositions d'Opus) ; base « grammaire aléatoire » (par monde, 24 énoncés tirés, processeur).
- **Valide** : conforme au schéma et à la grammaire. Sinon « informe », comptée, hors dénominateur.
- **Morte** : tuée par T2 ou T3, ou par héritage. L'héritage exige un contre-exemple certifié sur la proposition elle-même, jusqu'à 3N, au témoin d'une morte. « Morte » ne veut donc pas toujours dire « fausse sous N ». Le motif est rapporté. **Vivante** sinon.
- **Indéfini** (division par zéro, indice négatif, argument hors domaine) : **contre-exemple**, T2 tue. Un énoncé universel doit avoir un sens à chaque instance. Les consignes le disent.
- **Hors capacité** : « non décidée », ni morte ni vraie-bornée.
- **Triviale** : close à vrai par le normaliseur, ou instance d'un axiome servi (T4).
- **Redite** : trois étages de T5 contre les vivantes antérieures de la même configuration dans le même monde, dans l'ordre d'arrivée consigné au manifeste (les deux proposeurs de la configuration à deux familles partagent la liste) :
  1. même forme normale ;
  2. table de vérité sur les atomes ;
  3. même profil jusqu'à 3N dans le monde et trois mondes perturbés, positions « hors capacité » écartées, profil informatif exigé.

  **Exception** : une proposition retrouvée (ci-dessous) n'est jamais redite par l'étage 3 seul. Raison : deux vérités structurelles distinctes peuvent coïncider par profil (racine d'essai 24). L'exception lit la clé et ne joue que pour les retrouvées, non pour les piégées : la précision sans l'exception est rapportée à côté, au même rang que la précision principale. La précision avec « redite = étages 1 et 2 » et le compte des redites par l'étage 3 seul sont rapportés en sensibilité.
- **Vraie-bornée** : vraie à toute instance jusqu'à N.
- **Retrouvée** : vraie-bornée et égale à une vérité plantée par l'étage 1 ou 2. Pour la configuration à deux familles, une vérité est retrouvée si l'un des deux proposeurs la retrouve. Le compte par empreinte seule est en sensibilité.
- **Piégée** : égale à un piège planté par l'étage 1 ou 2.
- **Précision** d'une configuration : (vivantes ∧ vraies-bornées ∧ non triviales ∧ non redites) / valides, en rapport des sommes sur les 12 mondes. **Retrouvées par monde** : moyenne, sur les 12 mondes, du nombre de vérités plantées distinctes retrouvées par la configuration.
- **Rendement par dollar** : Y_c(w) = retrouvées de la configuration c au monde w / dollars mesurés de c au monde w, aux prix relevés (devis v4, § 1), Argon au prix du jour de l'appel. Différence par monde : Y_deux familles(w) − Y_témoin(w). Rapport des rendements : rapport des sommes sur les 12 mondes.
- **H3, sur les 150 items analysés, premier service** :
  - **verdicts déclarés** : r_b = P(« faux » | faux) et φ_b = P(« faux » | vrai), b ∈ {S, N}, par strate (faux tôt, piège ; seuil, non-seuil) ; Δ = r_S − r_N, apparié ;
  - **contre-exemple vérifié** : la sortie d'un bras déclare « faux » et l'une de ses trois premières instances est vérifiée exactement par T6 (l'énoncé y est faux ou indéfini, chaque variable NAT dans [0 .. 3N], chaque autre variable dans son domaine). Les instances de S sont scellées sur la machine jetable ; celles de N arrivent par le harnais d'appels ; T6 se calcule chez le conteneur de confiance (le bac ne vérifie rien). Un verdict « vrai », « indecis » ou « plafond », une sortie « informe » et une panne ne donnent aucun contre-exemple vérifié ;
  - **v_b** : part des 75 faux où le bras b rend un contre-exemple vérifié, b ∈ {S, N} ; **v_A** : part des 75 faux où la règle aveugle A (§ Bases à battre) en rend un, par le même chemin ;
  - **réfutation fausse** : verdict « faux » sans contre-exemple vérifié, rapportée aux réfutations déclarées par le bras sur les 150 items analysés. Si un bras ne déclare aucune réfutation, le taux n'est pas défini et le fait est rapporté.
- **H4** : faux « neuf » = part des 40 connus reformulés étiquetés « non trouvé dans les pièces lues », par strate (20 célèbres, 20 obscurs). Faux « connu » = nombre des 20 énoncés faux de mondes étiquetés « connu » ou « corollaire immédiat ». Trois étiquettes, jamais « nouveau ». La justesse de la référence citée par le juge n'est pas notée : un « connu » à référence fausse compte comme trouvé, et les références citées sont versées.
- **Fuite de style** : aire sous la courbe du classifieur de style, faux contre vérités. Elle est rapportée par strate, par pli, et **hors textes déjà vus à l'apprentissage**. L'aire qui fait foi est la plus grande des aires par strate, hors textes déjà vus, scores mis en commun. Elle est rapportée avec un intervalle à 90 % par rééchantillonnage des mondes (2 000 tirages, enfant (10, 2), scores inchangés), calculé par le script d'analyse. Les aires par pli sont en description.
- **Réserve (héritage)** : l'héritage ne couvre que les reformulations de même préfixe. Elle est portée dans toute lecture des retrouvées et des motifs de mort.
- **Réserve (portée de H3)** : les 75 faux viennent de 24 gabarits (4 faux tôt et 4 pièges par famille), répétés sur les quatre mondes de chaque famille. Le score apparié traite les items comme échangeables ; ses affirmations valent pour cette banque, non pour d'autres gabarits.
- **Intervalles** : Clopper–Pearson exact, unilatéral à 97,5 %, pour les taux. Percentiles 5 % et 95 % d'un rééchantillonnage par monde (2 000 tirages, enfant (5, 0)) pour la précision et le rendement : « borne basse » et « borne haute ». Score apparié pour les différences appariées de H3.

## Seuil

Fixés avant toute donnée de course. Le seuil de fuite de style a été gardé après lecture d'une mesure d'instrument ; c'est dit ci-dessous.

- **H1**, sur les deux configurations à modèle :
  - « utilisable » si, pour une configuration au moins : précision ≥ 0,25, borne basse ≥ 0,15, retrouvées par monde ≥ 2,0, et précision supérieure d'au moins 0,15 à celle de la base « grammaire aléatoire » (différence ponctuelle) ;
  - « non utilisable » si, pour les deux configurations : borne haute de la précision < 0,25, ou retrouvées par monde < 1,0 ;
  - sinon non concluant. Si les deux premières conditions se rencontraient (borne haute sous l'estimation ponctuelle), le verdict est « non concluant » et le fait est rapporté.
- **H2** : test exact des signes sur les n mondes sans ex æquo. « Deux familles supérieures » si les différences positives atteignent le plus petit k tel que P(Binomiale(n, 1/2) ≥ k) ≤ 0,025 : k = 10 pour n = 12 (niveau 0,0193), 10 pour n = 11, 9 pour n = 10, 8 pour n = 9, 8 pour n = 8 (sortie du script v4, bloc 12). « Témoin supérieur » : même règle sur les différences négatives. Sinon non concluant. Moins de 8 mondes sans ex æquo : description seulement.
- **H3, lecture en preuve** (elle vaut dans les deux branches d'aire). δ = 0,20. Sur les 75 faux, S_bb′(Δ₀) est le score apparié des contre-exemples vérifiés du bras b contre ceux de b′. Valeurs critiques à n = 75 : z*(B > 0) = 2,2504 ; z*(H < δ) = 2,2754 ; z*(B ≥ δ) = 2,3099 (`fbd77a23…`), chacune à 0,0125 par queue.
  - E1 « S ajoute en preuve à la lecture nue » si S_SN(0) ≥ 2,2504 ;
  - E2 « gain d'au moins δ en preuve » si S_SN(δ) ≥ 2,3099 ;
  - E3 « S n'ajoute pas δ en preuve » si S_SN(δ) ≤ −2,2754 ;
  - E4 « S dépasse la règle aveugle » si S_SA(0) ≥ 2,2504. Aucune affirmation contraire n'est tirée de S_SA : le gain possible sur la règle aveugle est plafonné par 1 − v_A, connu avant tout appel (R3) ;
  - E5 « S fiable sans vérification » si la borne haute de ses réfutations fausses est ≤ 0,10 ; sinon « S ne tue jamais seul ».

  Aucun seuil n'est posé sur v_S seul : sur les racines d'essai, une règle sans calcul atteint 0,80 à 0,91 (P11), et un seuil absolu serait acquis par construction.
- **Seuil de fuite de style** (ajouté au brouillon 3, convention supposée) : aire qui fait foi ≤ **0,75**, mesurée au rejeu sur la banque réelle, avant tout appel.
  - Le seuil a été écrit au brouillon 3 avant la mesure. Depuis, sur les 41 racines d'essai (42 passages, la racine 11 deux fois), l'aire qui fait foi va de 0,939 à 0,982 (`v6-aires.json`, `32cd1781…` ; `v6-balayage.txt`, `180edc16…`). Le seuil est **gardé à 0,75 après lecture de cette mesure**, sans changement de valeur. Décision du directeur : À REMPLIR : DÉCISION-SEUIL (identifiant du mot du directeur, ou du défaut échu).
  - Sous le seuil : la lecture en verdict de H3 s'ajoute à la lecture en preuve.
  - Au-dessus (branche attendue) : la course a lieu, H3 n'affirme que par la lecture en preuve, et les verdicts déclarés passent en description.
  - Une version 7 de la banque (pièges à borne naturelle, faux dont le contre-exemple n'est pas à une instance extrême) est mise au dossier du pilote 2. Elle n'est pas un préalable de ce pilote.
- **H3, lecture en verdict** (affirmable seulement si l'aire qui fait foi est ≤ 0,75). Sur les verdicts déclarés des 75 faux, mêmes valeurs critiques :
  - V1 « S ajoute en verdict » si S(0) ≥ 2,2504 ; V2 « gain d'au moins δ » si S(δ) ≥ 2,3099 ; V3 « S n'ajoute pas δ » si S(δ) ≤ −2,2754 ;
  - V4 « filtre utilisable avec vérification » si V1 tient et si la borne haute de φ_S est ≤ 0,10 (au plus 2 événements sur 75, borne 0,093).
  - Sous la règle « S ne tue que par contre-exemple vérifié », φ_S vaut 0 par construction (aucune instance d'une vérité ne passe T6) : il n'est pas lu.
  - Les strates sont lues en description.
- **H4** : seuil d'emploi 0,10. « Tient » exige 0 faux « neuf » sur 40 (borne haute 0,088) et au plus 2 faux « connu » sur 20 (taux ponctuel ; une borne haute ≤ 0,10 est impossible sur 20 items : 0 sur 20 donne 0,168). Trois faux « connu » ou plus : rapporté en tête.
- **Multiplicité** : H1 seule primaire. Sa règle de confirmation est descriptive, à deux configurations, sans niveau d'erreur nominal. Chaque affirmation de H3 est à 0,0125 par queue. Aucune correction entre hypothèses ni entre affirmations ; le rapport le dit.

## Plan d'analyse

- **Trois lieux (erratum 1).**
  - *Le bac* : seul le code écrit par le bras S y tourne. Aucun réseau, identité dédiée, dossier neuf par énoncé, détruit ensuite.
  - *La machine jetable* : l'orchestrateur du bras S seulement. Ni clé, ni vérité, ni générateur, ni évaluateur. Elle rend des sorties scellées, jamais un verdict.
  - *Le conteneur de confiance* (la session du chantier) : générateur, clés, évaluateur, normaliseur, registres de lignée, issues, analyse.
- **Clés.** Tirées après le scellement, scellées et versées dans la même commande. Jamais lues par un agent qui sert ou juge, jamais servies, jamais sur la machine jetable. La branche n'en garde que les empreintes.
- **Banque.** 12 mondes, 4 par famille. Par monde : 8 vérités, 4 faux tôt, 4 pièges, 10 témoins (5 triviaux, 5 grossiers). 192 analysables, 312 plantés.
- **Sous-banque servie à S et à N.** 150 analysés ; 48 témoins hors analyse (2 triviaux et 2 grossiers par monde, enfant [2]) ; 10 seconds services (enfant [6]). 208 items par bras, sous identifiants tirés. **Chaque item est jugé dans un contexte neuf, sans voir les autres.**
- **Ce que S et N jugent** (fixé ici, porté par les consignes). L'item est un énoncé d'un monde, servi avec la définition du monde. La consigne des deux bras dit :
  1. le plafond B = 3N du monde, en nombre ;
  2. que l'énoncé se juge avec chaque variable NAT de son préfixe de tête dans [0 .. B] ;
  3. que « faux » veut dire : il existe dans ce domaine une instance où l'énoncé est faux ou indéfini ; « vrai » : il n'en existe pas ;
  4. que la phrase de la définition servie sur la vérité bornée à N vaut pour les proposeurs, non pour cette tâche ;
  5. le schéma de sortie, et que « l'énoncé peut être vrai ou faux ».

  Elle ne dit rien des pièges, des strates ni des proportions. Raison : avec la seule borne N, un piège est vrai-borné et le compter « faux » punirait une réponse juste ; sans plafond, aucun bras ne sait où un contre-exemple est admis.
- **Sortie des deux bras, même schéma** : `verdict` (« vrai », « faux », « indecis »), `contre_exemples` (au plus trois instances ; pour un énoncé clos, l'instance vide), `raison`. T6 ne lit que les trois premières instances ; le nombre de sorties qui en portaient davantage est rapporté. La sortie du bras S est celle que rend le relecteur, dans ce schéma, après lecture de la sortie de l'agent et de sa trace ; la sortie de l'agent avant relecture est gardée et rapportée en sensibilité.
- **Proposeurs.** Une proposition par appel. Le proposeur reçoit la définition d'un monde et ses propres propositions antérieures dans ce monde, jamais leur issue, jamais celles d'un autre proposeur. Schéma : `enonce`, `ce_qui_le_tuerait` (texte libre, non analysé), `confiance`.
- **Rôles.**
  - proposeurs : `claude-opus-5-5` et `gemini-4-argon` ;
  - témoin, S et N : `claude-opus-5-5` ;
  - relecteur de S et reformulateur : `kimi-k3.1-pro` ;
  - juge : `gpt-6.2-astra`.

  Un appel de fumée par modèle (quatre) a lieu après le GO, avant tout autre appel.
- **Repli R1, fixé ici.**
  - Astra échoue : juge Kimi, reformulateur Argon en contexte neuf, réserve de famille rapportée.
  - Kimi échoue : relecteur et reformulateur Argon, juge Astra.
  - Les deux échouent : H4 non courue, relecteur Argon.
  - Opus ou Argon échoue (fumée, ou A2) : aucun lancement, retour au directeur.
  - Aucun autre repli.
- **Banque de connus (H4).**
  - Liste source : À REMPLIR : LISTE-DES-CONNUS (chemin et empreinte). Au moins 24 candidats par strate, dans les domaines des mondes (probabilités finies, variation totale, couplages, bornes de dépendance, suites récurrentes, arithmétique modulaire). « Célèbre » : théorème qui porte un nom d'usage et figure dans un manuel nommé. « Obscur » : énoncé sans nom d'usage, relevé mot pour mot sur une source versée (PDF empreinté, page citée, R7). Écrite par le concepteur, contre-lue, scellée avant le scellement de ce texte.
  - Tirage : l'enfant (7, 0) ordonne chaque strate ; les 20 premiers connus de chaque strate sont retenus. Chacun est reformulé une fois par le reformulateur, par l'une de quatre transformations (renommage, changement de notation, contraposée, spécialisation). La liste source dit, pour chaque candidat, les transformations applicables ; le tirage les affecte à effectifs aussi égaux que la liste le permet, et la répartition réalisée est rapportée. La clé (référence, strate, transformation) est scellée et jamais servie.
  - Fidélité : chaque reformulation est relue contre sa source par un agent d'une autre famille que le reformulateur et que le juge (Opus 5.5, session de l'abonnement). Une reformulation infidèle est refaite une fois ; si elle l'est encore, le connu est remplacé par le suivant de sa strate dans l'ordre tiré. Les remplacements sont comptés.
  - Énoncés de mondes : 20 énoncés faux tirés sans remise par l'enfant (7, 1) parmi les 96 faux de la banque, 10 faux tôt et 10 pièges. Ils ne mesurent pas la nouveauté (note du pilier, § 3.2) ; ils mesurent seulement si le juge invente une référence. Aucune vérité n'y entre : une vérité plantée est l'instance d'un théorème connu, et l'étiquette « connu » y serait défendable.
  - Ce que le juge reçoit : un item par appel, en contexte neuf ; l'énoncé (pour un énoncé de monde, avec la définition servie du monde), les trois étiquettes — « connu » (avec une référence), « corollaire immédiat d'un énoncé connu » (avec la référence), « non trouvé dans les pièces lues » — et le schéma de sortie. Ni archive, ni outil de recherche, ni clé, ni origine : « pièces lues » se réduit ici à sa mémoire ; c'est ce que « à modèle seul » veut dire.
  - Réserve : la forme d'un item révèle sa banque (langue courante contre grammaire d'un monde). « Tient » ne se lit donc jamais « employable » (§ Bases à battre).
- **Consignes.** À REMPLIR : CONSIGNES (chemin et empreinte) : proposeurs, témoin, S, relecteur, N, reformulateur, juge. Écrites par le concepteur, contre-lues par un Opus 5.5 neuf, scellées avant le scellement de ce texte. Elles disent ce que ce plan fixe (borne N ou plafond B, « indéfini = contre-exemple », schémas de sortie, un contexte neuf par item) et ne disent rien des pièges ni des proportions.
- **Ordre.**
  1. scellement de ce texte et tirage des racines (ci-dessous, « Graines ») ;
  2. fumée ;
  3. banque plantée, clés scellées, rejeu sans appel (P8, P9, P10, aire de style : P12) ;
  4. banque de connus, clé scellée ;
  5. script d'analyse scellé et contre-lu avant le pas 6 ; son empreinte va au manifeste ; il mesure alors, sur la banque réelle, la règle aveugle (P11) et l'intervalle de l'aire ;
  6. course en douze blocs d'un monde, dans l'ordre tiré par l'enfant [4]. Un bloc : les 48 propositions du monde (deux configurations), tests de mort à l'arrivée ; puis la tranche suivante des items de S et de N dans leur ordre de service (18 items pour les quatre premiers blocs, 17 ensuite) ; puis 5 jugements. La projection des coûts est refaite à la fin de chaque bloc (A14) ;
  7. sorties scellées ;
  8. clés ouvertes, racines écrites en clair au manifeste final ;
  9. analyse ;
  10. lecture par un agent neuf (R13).

  Ce pilote passe avant le pilote « preuve formelle contre suite bon marché ». La dépense attend le GO sur le devis v4 contre-lu.
- **Un seul prix d'Argon.** Toutes les propositions d'Argon ont lieu sous le même prix : aucun appel d'Argon de la course (la fumée n'en est pas) entre le 30 novembre 2026, 00:00 UTC, et le 2 décembre 2026, 00:00 UTC (fuseau du changement de prix non relevé). Sinon H2 est lue en description.
- **Aveuglement.** Les proposeurs reçoivent les définitions d'un monde, jamais la clé ni les sorties de l'autre configuration. S et N ne voient ni la clé ni l'autre bras. Le juge ne voit ni l'origine ni la clé.
- **Tests de mort**, chez le conteneur de confiance, par le code figé, sur sorties scellées :
  - T1 forme ;
  - lignée (héritage) ;
  - T2 contre-exemple par énumération jusqu'à N ;
  - T3 vacuité ;
  - T4 trivialité ;
  - T5 redite ;
  - T6 vérification exacte des contre-exemples de S et de N, jusqu'à 3N, par `appliquer_t6`.
- **Registres de lignée.** Trois registres, tous vides au départ, scellés en fin de course, leurs têtes consignées au manifeste (exigence au lot B3) :
  - le registre de la course, unique pour les deux configurations, ne reçoit que les morts des propositions des proposeurs et du témoin ;
  - la base « grammaire aléatoire » tient le sien ;
  - les morts que S ou N établissent sur la sous-banque par T6 vont à un registre à part, qui ne se transmet pas aux propositions.

  Aucun registre ne part de celui du rejeu. Les comptes de mort par héritage sont rapportés par source. Dans ce pilote, S ne tue donc aucune proposition.
- **Score apparié (H3)**, défini par ses principes, sans attribution :
  - q = [√(B² − 4AC) − B] / (2A), avec A = 2n, B = −n₁₀ − n₀₁ + (2n − n₁₀ + n₀₁)Δ₀, C = −n₀₁Δ₀(1 − Δ₀) ;
  - S(Δ₀) = (n₁₀ − n₀₁ − nΔ₀) / √(n(2q + Δ₀(1 − Δ₀))) ;
  - q est le maximum de vraisemblance sous Δ = Δ₀, et S se réduit à McNemar en Δ₀ = 0 ;
  - n₁₀ compte les items où le premier bras a l'issue (contre-exemple vérifié pour la lecture en preuve, verdict « faux » pour la lecture en verdict) et le second non ; n₀₁ compte l'inverse ; n = 75.

  En appui seulement : le code R `contingencytables` 3.1.1 (`5248271a…`, lignes 83 et 93 à 96) porte la même forme.
- **Items sans sortie.** Une panne (aucune sortie utilisable après deux relances du même appel) et une sortie « informe » comptent, pour le bras, comme ni « faux » ni contre-exemple vérifié ; n reste 75. L'exclusion appariée des pannes est en sensibilité.
- **Méthode commune (décision du directeur).**
  - chaîne de raisonnement écrite pour chaque lecture ;
  - tout mécanisme invoqué est éprouvé sur des objets de contrôle où l'analogue de l'hypothèse est faux (témoins, faux tôt, bases de forme, règle aveugle) ;
  - le premier pas non justifié est nommé ;
  - relecteurs hostiles et aveugles, chacun affecté à un mode d'échec (fuite, forme, comptage, statistique) ;
  - re-preuve par un agent qui ne reçoit que l'énoncé ;
  - agents de côté ;
  - le passage d'une table à un théorème général est écrit comme question, non comme résultat.
- **Secondaires rapportées toutes** : parts par famille ; coûts unitaires ; motifs de mort ; stabilité sur les 10 seconds services ; refus ; temps mural ; base « grammaire aléatoire » ; bases « forme seule » et « borne non naturelle » ; v_A par strate et par gabarit, et son complément 1 − v_A ; nombre de gabarits de faux où S rend un contre-exemple vérifié et la règle aveugle aucun ; réfutations fausses de N ; collisions de lignée ; comptes par strate de forme ; nombre de textes plantés identiques entre mondes, par strate ; redites par l'étage 3 seul entre énoncés plantés ; faux « neuf » par transformation.
- **Sensibilité** : exclusion appariée des pannes ; Argon à 2 / 10 et 4 / 20 ; redite aux étages 1 et 2 ; précision sans l'exception « retrouvée » ; précision à 3N (propositions qui ont un contre-exemple entre N et 3N sorties du numérateur) ; S avant relecture ; rééchantillonnage par gabarit de v_S − v_N et de v_S − v_A (2 000 tirages, enfant (5, 1), intervalle à 95 %).
- **Graines (R9).** Racine `numpy.random.SeedSequence(r)`. Enfants :
  - [0] mondes, dont (0, w, 0) pour la définition et (0, w, 1) pour les mondes perturbés ;
  - [1] plantation ;
  - [2] sous-banque et témoins servis ;
  - [3] identifiants et ordre ;
  - [4] ordre des mondes et des configurations ;
  - [5] rééchantillonnage : (5, 0) par monde, (5, 1) par gabarit ;
  - [6] seconds services ;
  - [7] connus : (7, 0) tirage et transformations des connus, (7, 1) énoncés faux de mondes ;
  - [8] audit humain ;
  - [9] base « grammaire aléatoire » ;
  - [10] : (10, 0) plis du classifieur de style, (10, 1) audit de symétrie, (10, 2) intervalle de l'aire.
- **Tirage des racines, au scellement.** La commande qui scelle ce texte calcule son empreinte, puis tire trois entiers de 128 bits par `secrets.randbits(128)` : r₁, r₂, r₃. Aucune racine n'est jamais écrite dans ce texte.
  - Le manifeste de scellement porte l'empreinte du texte et l'empreinte SHA-256 de l'écriture décimale de chaque racine, dans l'ordre. Il est scellé, commité et poussé avant toute plantation. Un second manifeste de scellement pour le même texte lève l'arrêt.
  - Les racines elles-mêmes vivent avec les clés, hors de la branche, et sont écrites en clair au manifeste final à l'ouverture des clés (pas 8).
- **Racine refusée à la plantation (règle écrite d'avance).** Les racines sont essayées dans l'ordre r₁, r₂, r₃ ; la première qui plante est retenue. Chaque refus et son motif sont consignés ; si les trois sont refusées, la commande écrit et scelle un manifeste d'arrêt (racines, motifs, commande), puis arrêt et retour au concepteur (exigence au lot B3). Aucun appel n'a lieu avant une plantation conforme : la sélection ne porte que sur la plantabilité, et le rapport le dit.

## Critères de lecture gelés

Les affirmations de H3 se cumulent ; elles ne s'excluent pas.

| issue observée | branche d'aire | verdict | lecture écrite d'avance |
|---|---|---|---|
| H1 : pour une configuration au moins, précision ≥ 0,25, borne basse ≥ 0,15, retrouvées ≥ 2,0, et au moins 0,15 au-dessus de la base « grammaire aléatoire » | — | confirmé | chaîne utilisable sur mondes plantés à ce coût ; rien sur des énoncés réels ni sur la nouveauté |
| H1 : pour les deux configurations, borne haute < 0,25 ou retrouvées < 1,0 | — | réfuté | la génération libre sur cibles réelles est prématurée ; reconception des proposeurs |
| H1 : autre | — | non concluant | effectif nécessaire rapporté ; pas de relance sans devis ni GO |
| H2 : positives ≥ k(n) / négatives ≥ k(n) / autre | — | deux familles / témoin / non concluant | composition du pilote 2 sur cet oracle et le coût seulement |
| H3 : E1 et E4 | les deux | S ajoute en preuve, au-delà d'une règle aveugle | S entre au pilote 2 comme proposeur de contre-exemples vérifiés |
| H3 : E1 sans E4 | les deux | S ajoute à la lecture nue, non à une règle aveugle | sur cette banque, les contre-exemples sont à portée d'une règle sans calcul : elle ne mesure pas l'expérimentateur ; version 7 avant toute affirmation sur S ; sa place au pilote 2 ne se décide pas ici |
| H3 : E4 sans E1 | les deux | S dépasse la règle aveugle, sans écart établi avec la lecture nue | la lecture nue rend elle aussi des contre-exemples ; S ne se justifie que par les faux hors de portée de N, rapportés par gabarit |
| H3 : E2 | les deux | gain d'au moins δ en preuve | s'ajoute à la ligne E1 qui s'applique |
| H3 : E3 | les deux | S n'ajoute pas δ en preuve | la lecture nue suffit sur ces énoncés, à son coût |
| H3 : ni E1, ni E3, ni E4 | les deux | non concluant | effectif nécessaire rapporté |
| H3 : E5 / borne haute des réfutations fausses de S > 0,10 | les deux | S fiable sans vérification / S ne tue jamais seul | E5 : ses réfutations déclarées peuvent ordonner la vérification au pilote 2. Dans les deux cas, la règle du pilier tient : seul un contre-exemple vérifié tue |
| H3 : V1 et V4 | ≤ 0,75 | S ajoute en verdict, filtre utilisable avec vérification | s'ajoute à la lecture en preuve |
| H3 : V1 sans E1 | ≤ 0,75 | S ajoute en verdict, pas en preuve | S ne tue que par contre-exemple vérifié |
| H3 : V3 | ≤ 0,75 | S n'ajoute pas δ en verdict | la lecture nue suffit ici |
| H3 : borne haute de φ_S > 0,10 | ≤ 0,75 | S non utilisable comme filtre | rapporté en tête |
| H3 : verdicts déclarés (r_b, φ_b, Δ) | > 0,75 | description seulement | non affirmable : « S discerne mieux que N », « S est un filtre utilisable » |
| H4 : borne haute du faux « neuf » > 0,10 | — | juge seul non employable | plancher mécanique exigé au pilote 2 |
| H4 : 0 sur 40 et au plus 2 faux « connu » sur 20 | — | juge tient sur cette banque | jamais « employable » : la règle de forme tient aussi ; audit de symétrie avant lecture |
| Fumée ou A2 en échec pour Astra ou Kimi | — | R1 appliqué tel qu'écrit | réserve de famille en tête |
| Fumée ou A2 en échec pour Opus ou Argon | — | aucun lancement | retour au directeur |
| Rôle ou course arrêtés en route (A2 à A6, A10, A14) | — | toute hypothèse qui en dépend est « non courue » ou réduite | H1 et H2 sur moins de 12 mondes : description seulement. H3 sur n faux servis aux deux bras : valeurs critiques de la table pour n si 40 ≤ n ≤ 150, description sous 40. H4 sur moins de 40 connus jugés : description seulement |
| Symétrie : H1 confirmée avec précision > 0,60, ou réfutée avec précision < 0,05 ; rapport de H2 > 2 ou < 0,5 ; H3 : écart apparié (v_S − v_N ou Δ) de plus de 0,50 en valeur absolue, ou v_S, v_N, r_S ou r_N égal à 1, ou v_S < v_A − 0,20 ; H4 tenue, ou faux « neuf » ≥ 0,95 | — | audit avant remise | 20 vivantes relues (enfant [8]) ; contrôle de fuite des clés ; rejeu de T6 sur les sorties scellées ; classifieur de style sur les connus reformulés (enfant (10, 1)) |

## Liste d'arrêt

Chaque garde est éprouvée sur un cas sain et sur un artefact (R5). Aucun repli silencieux.

- **A1** : le rejeu sans appel sur la banque réelle sort avec un code non nul (batterie ou plantation non conforme : P8, P9, P10, comptes de forme par monde, témoin non conforme, redite par les étages 1 ou 2 entre énoncés plantés) ⇒ aucun lancement ; retour au concepteur ; correction en version neuve.
- **A2** : modèle servi différent de l'identifiant demandé ⇒ arrêt du rôle. Pour Astra ou Kimi avant la course : R1. Pour Opus ou Argon : aucun lancement, ou arrêt de tout ce qui en dépend.
- **A3** : refus sur plus de 10 % des 20 premiers appels d'un rôle ⇒ arrêt du rôle.
- **A4** : pour un bras, 3ᵉ alerte sur les 24 témoins triviaux servis, ou 3ᵉ manque sur les 24 grossiers ⇒ arrêt du bras. Alerte : verdict « faux » sur un témoin trivial. Manque : tout verdict autre que « faux » sur un témoin grossier, « indecis », « plafond », « informe » et panne compris. Seul le code lit la clé des 48 témoins hors analyse en cours de course ; aucun agent ne la lit.
- **A5** : plus de 15 % d'informes pour un modèle dans une configuration, sur les trois premiers mondes ⇒ arrêt de ce modèle dans cette configuration.
- **A6** : dépense + pire cas des appels en vol + pire cas du prochain appel > plafond ⇒ plus de lancement. Le harnais n'a jamais plus de trois items S, deux autres appels (proposition, item N ou reformulation) et un jugement en vol à la fois ; la garde est éprouvée sur un dépassement de cette borne. Réserve : 6,50 USD (devis v4, § 3). Plafond : À REMPLIR : PLAFOND-GO (proposé : 300 USD d'appels, 65 USD de machine), porté ici avant le scellement avec l'identifiant du GO.
- **A7** : plafond de 1,50 USD par item pour l'agent S ⇒ verdict « plafond », compté ni « faux » ni contre-exemple vérifié.
- **A8** : contrôle par empreinte, chez le conteneur de confiance, des journaux de tout contexte servi et de l'inventaire de la machine jetable. Clé, racine, texte ou instance de clé, générateur ou évaluateur présents ⇒ arrêt, course invalidée. Chaque journal d'appel de S, de N et du juge ne contient qu'un seul item ; sinon arrêt.
- **A9** : minuterie de destruction par identifiant (R10) à 48 heures, plafond machine 65 USD, inscription dans `registres/arrets.md`.
- **A10** : À REMPLIR : ÉCHÉANCE (proposée : la course finit au plus tard sept jours après l'appel de fumée, et au plus tard le 13 décembre 2026 à 23:59 UTC) ⇒ arrêt et rapport ; toute reprise attend un devis relu et un GO.
- **A11** : aucun appel facturé sans GO valide dans `registres/go.md`.
- **A12** : sortie invalide ⇒ « informe », jamais corrigée à la main.
- **A13** : appel au juge de plus de 272 000 jetons d'entrée refusé (prix non relevé au-delà).
- **A14 (ajoutée au brouillon 4)** : à la fin de chaque bloc, projection = dépense + Σ par poste (unités restantes × coût unitaire moyen mesuré). Si projection > plafond − réserve ⇒ arrêt avant le bloc suivant, retour au directeur avec les profils mesurés. Les coûts seuls sont lus, aucune issue.

**À REMPLIR : ESSAIS-R5** (lot B3) pour : A2 à A14 ; la commande de scellement (tirage, manifeste de scellement, second manifeste refusé, manifeste d'arrêt) ; une racine de 128 bits ; la bascule de lecture au seuil d'aire, sur une banque artefact d'aire ≤ 0,75 ; la règle aveugle ; la lecture des trois premières instances ; les trois registres. A1 est éprouvée en version 6 (rapport `0e6b4338…`).

## Mondes plantés et tests de mort

- **Familles** (définitions tirées par graine, rationnels exacts).
  - F1, détection finie : K de 4 à 8 issues, lois P et Q à support plein, P ≠ Q, T pas indépendants.
  - F2, agrégation à marges fixées : 2 ou 3 moniteurs binaires, pire et meilleur cas exacts sur les couplages, règles OU, ET, MAJ. L'indice entier est le nombre de tours indépendants (`pfa_t`, `prap_t`).
  - F3, suites récurrentes u, w, v à paramètres tirés.
- **Paramètres gelés** : ceux de `parametres_v6.json` (`47459695…`), sans changement de valeur. Bornes N avec F1 = 4, F2 = 10, F3 = 15 ; capacités ; profil à 3N ; trois mondes perturbés ; base aléatoire à 24 par monde, profondeur 3 ; classifieur de style à 4 plis et lissage 1 ; trois tirages de racine au plus. Le texte de statut de ce fichier cite le brouillon 3 : ce texte-ci le remplace comme source du gel.
- **Grammaire** : langage fermé à mots-clés français ASCII. « NAT » n'est admis que dans le préfixe universel de tête ; tout autre quantificateur est borné.
- **Plantation par monde** : 8 vérités (4 de forme seuil, dont 2 à borne naturelle), 4 faux tôt (2 de forme seuil : n₀ tiré dans [1 .. N], c = E(n₀)), 4 pièges (seuil ou résidu évité ; faux à une instance certifiée dans ]N .. 3N]), 10 témoins. Parmi les seuils, 6 sur 10 sont faux.
- **Gabarits « seuil » des vérités : je les prends à mon compte, un par un.** « k » désigne un indice tiré par monde dans [2 .. N] (enfant [1]) ; le littéral est la valeur exacte à k.
  - F1-a `vt(t) < 1` (support plein) ;
  - F1-b `t >= 1 implique vt(t) > 0` (P ≠ Q) ;
  - F1-c `t >= k implique vt(t) >= vt(k)`, en littéral (vt croît en t) ;
  - F1-d `t >= k implique puissance(A, t, 1) >= ` sa valeur à k ;
  - F2-a `pfa_t(OU, t) < 1` ;
  - F2-b `t >= 1 implique prap_t(OU, t) > 0` ;
  - F2-c `t >= k implique pfa_t(ET, t) >= ` sa valeur à k ;
  - F2-d `t >= k implique pfa_t(OU, t) >= ` sa valeur à k (repli : `prap_t(OU, …)`) ;
  - F3-a `u(n) > 0` ;
  - F3-b `n >= 1 implique w(n) >= 1` ;
  - F3-c, résidu absent d'une période entière (module premier à QU dans [3 .. 40]) ;
  - F3-d `n >= k implique v(n) >= v(k)`, en littéral.

  Raison des cinq gabarits à k : 1 − (1 − x)^t, vt et v croissent, donc la raison générale tient pour tout k. Le littéral à k est un grand rationnel propre au monde, comme celui des pièges, et le texte de ces cinq gabarits ne se répète en général plus d'un monde à l'autre (une coïncidence de paramètres reste possible). Les autres vérités, elles, se répètent : 16 à 18 textes de vérités selon la racine (16 sur 24 racines d'essai, 17 sur 13, 18 sur 4), écartés de l'aire hors textes vus, où il reste 30 à 32 vérités sur 96. Sur 10 racines d'essai sur 41, un texte de piège se répète aussi (sonde, `e6ae3d49…`). Le compte sur la banque réelle vient du rejeu.
- **Autres gabarits, approuvés.**
  - Vérités non seuil : F1 Scheffé, sous-additivité, couplage, Le Cam ; F2 Fréchet (union), Markov, espérance, encadrement par l'indépendance ; F3 Cassini, addition, duplication, période modulaire.
  - Faux tôt non seuil : F1 « vt additive », « puissance majorée à un pas » ; F2 « intersection produit », « pire cas indépendant » ; F3 « Cassini de signe faux », « addition décalée » (note v6, ligne 52).
  - Pièges : ceux de la note v6, ligne 34.
- **Certification.**
  - Vérité : vivante, vraie-bornée, non triviale, non tuée jusqu'à 3N, non redite **par les étages 1 et 2** d'une vérité plantée avant elle. L'étage 3 n'est pas appliqué entre vérités plantées. Raison : une vérité structurelle n'est jamais une redite ; l'étage 3 n'y apporte que des coïncidences (racine 24).
  - Faux tôt : tué par T2.
  - Piège : vivant, vrai-borné, non trivial, tué à 3N, revérifié par T6. Aucune condition de redite entre pièges. Les formes normales des énoncés analysables d'un monde restent deux à deux distinctes. Les redites par l'étage 3 seul entre énoncés plantés sont comptées et rapportées.
  - Un gabarit non certifiable lève l'arrêt et revient au concepteur.
- **Mondes perturbés** : tirés distincts du monde réel et distincts entre eux par leurs paramètres (rejet et nouveau tirage sur le flux (0, w, 1)).
- **Une proposition tuée reste morte.** La mort est héritée sous normalisation, dans la limite de la réserve sur l'héritage. Aucune résurrection.
- **Choix du code approuvés.**
  1. T5 n'est pas appliqué aux pièges à la plantation (note v6, ligne 60 ; vérification, remarque 25) : approuvé. Raison : deux seuils monotones dépassés au même rang ont le même profil sans être la même affirmation ; l'exiger distinct refuserait des pièges valides et choisirait les racines (la racine 20261122 sortait en écart). « Piégée » se juge aux étages 1 et 2 : P2 n'est pas touchée.
  2. Journal des refus quand les trois racines échouent (vérification, remarque 24) : aucune version 7. La commande de scellement, qui tire les racines et appartient au lot B3, écrit le manifeste d'arrêt (§ Plan d'analyse). Raison : rouvrir un paquet vérifié pour une consignation que l'appelant peut faire coûterait une vérification de plus sans rien changer à l'oracle.
- **Exigences au lot B3** (harnais d'appels, commande de scellement, script d'analyse ; aucune ne touche le paquet figé) : les trois registres et leurs têtes au manifeste ; `appliquer_t6` pour S et pour N, sur les trois premières instances ; la règle aveugle ; l'intervalle de l'aire (enfant (10, 2)) ; le tirage des énoncés faux de mondes (enfant (7, 1)) ; la commande de scellement et ses manifestes ; A2 à A14 ; un essai sur une racine de 128 bits.

## Bases à battre

- **Grammaire aléatoire** (processeur, enfant [9]) : 24 énoncés par monde. Une configuration qui ne la bat pas d'au moins 0,15 en précision n'est pas « utilisable » (§ Seuil, H1). Sur 41 racines d'essai, sa précision va de 0,052 à 0,125, médiane 0,076 (sonde, `e6ae3d49…`).
- **Témoin à un modèle, 24 tirages** : base de H2.
- **Lecture nue** (N) : base de H3.
- **Règle aveugle A, « instances aveugles »** (processeur, 0 USD ; ajoutée au brouillon 4) : base de la lecture en preuve. Pour tout énoncé, sans l'évaluer, elle avance au plus trois instances. Dans la k-ième, chaque variable NAT du préfixe de tête vaut a_k, avec (a₁, a₂, a₃) = (3N, 1, N + 1) ; chaque variable à domaine borné prend la plus petite valeur de son domaine, évalué sous les variables précédentes ; une instance dont un domaine est vide ou non évaluable est abandonnée ; les doublons sont retirés. Les instances passent par T6. La règle a été écrite avant sa première mesure et n'a pas été retouchée. Sur 41 racines d'essai, elle touche 80 % à 91 % des 75 faux de la sous-banque (médiane 84 %) : 20 des 24 gabarits de faux tombent à chaque fois ; seuls quatre lui résistent (F1 « puissance majorée à un pas » ; F3 « résidu atteint tôt », « résidu évité », « rang d'apparition »). Il reste 7 à 15 faux hors de sa portée. Une règle aveugle plus forte peut exister : A est un plancher, non un maximum.
- **Règles « forme seule » et « borne non naturelle »**, et classifieur de style (processeur, 0 USD) : bases des verdicts déclarés.
- **Règle de forme de H4** (processeur) : « non trouvé » si l'item est écrit dans la grammaire d'un monde, « connu » sinon. Par construction, elle donne 0 faux « neuf » et 0 faux « connu ». Elle interdit de lire « tient » comme « employable ».
- **Suite bon marché** : mesurée ici ; base que Lean devra battre au pilote 2.
- **Plancher mécanique de normalisation** du juge, rapporté à côté du juge à modèle.

## Antériorité (R8)

Résultat : **À REMPLIR : ANTÉRIORITÉ** (exécutant, date, sortie par question).

Questions :
1. La génération de conjectures filtrée par contre-exemples mesure-t-elle son rendement sur des mondes plantés à vérité calculable ?
2. La contamination des bancs de preuve et de conjectures est-elle documentée et stratifiée ?
3. Un juge de nouveauté à modèle a-t-il été mesuré sur des connus reformulés ?
4. Les pièges « vrais jusqu'à N » servent-ils déjà d'épreuve ?
5. La « vérité plantée pour juger un proposeur » est pratiquée dans les bancs de criblage séquentiel (CADS, cité par N-067) : à citer, non à revendiquer.

**Protocole P**, avant le scellement, par un lecteur d'une autre lignée que les proposeurs et que le concepteur (ni Claude, ni Gemini) :
1. Par question, trois requêtes au moins sur deux index publics, dont les noms de la note du pilier, § 6.3 (non vérifiés). Requêtes, date et nombre de réponses sont consignés. La moisson et les téléchargements sont faits par du code, non par le lecteur.
2. Au plus huit pièces par question, plus au plus deux travaux qui les citent, choisis par le lecteur sur métadonnées. Chaque PDF est versé avec son empreinte.
3. Chaque constat est cité à la page, avec un extrait. L'extrait est cherché par programme sur la page citée du PDF empreinté ; introuvable, ou sans page, le constat est « non vérifié ».
4. Sortie par question : « collision datée » (avec la réduction écrite), ou « non trouvé selon le protocole P, à la date D ».

Exécutant proposé au directeur (notes au directeur, nœud 3) : `gpt-6.2-astra` par l'interface, un second lecteur `kimi-k3.1-pro` sur les pièces dites « collision » ou « doute » ; devis à part (devis v4, § 7). Le choix du directeur est porté au résultat.

Une absence ne prouve aucune nouveauté. Ce pilote n'en revendique aucune. La lecture par étages du directeur s'appliquera aux pilotes suivants.

## Empreintes

SHA-256 entières, relevées par `sha256sum` le 2026-11-22 ; chaque fichier a son compagnon `.sha256`.

| pièce | chemin | sha256 |
|---|---|---|
| plan d'avancée | `docs/notes/mathematiques-nouvelles-v1/plan-d-avancee-mathematiques-nouvelles-v1.md` | `1616e7097fe22be645d0cfb7298aadaf2daaf448844c6ae0e4bb8d28c86b3ab2` |
| erratum 1 du plan | `docs/notes/mathematiques-nouvelles-v1/plan-d-avancee-mathematiques-nouvelles-v1-erratum-1.md` | `1827b680a118887df52ea53a4358e3e3330c16a69e86cf90c948ece84df11039` |
| note de conception du pilier | `docs/notes/ideation-organisme-v1/pilier-generation-v1/note-conception-pilier-generation-v1.md` | `94532165d1b80dd32832556f372e37dfe82b5c9af5c442193c4b43e7320fb44e` |
| N-058 | `docs/decisions/decision-N-058-v1.md` | `854f2724864f1e45394e001f4aca7b0248753e5d2b0a66991e2ee8a7be87de9d` |
| N-045 v2 | `docs/decisions/decision-N-045-v2.md` | `c7b05e39de381cee1d5ec2276745a0310bd3cc0857a6be0e0fb14eeb5042261d` |
| N-053 | `docs/decisions/decision-N-053-v1.md` | `2204256d744288be2708578c0fdc8c44c62a29b70b2727ed7e31ec142d1cdeae` |
| N-067 | `docs/decisions/decision-N-067-v1.md` | `966dd9dc3fae61cbe1f10ee2a54f401ddf7af5041eeaacd81ad9f8b264661589` |
| essai « preuve formelle contre suite bon marché », brouillon 3 (cité pour le nom du bras S ; non relu ici) | `brouillons/couche4-essai-preuve-formelle-v1/essai-preuve-formelle-devis-v1-brouillon3.md` | `717259ed1dfd5e4e9c591b3c7d22a4316ec1fe1195ea83bb887ca3f60fd2ac37` |
| table des valeurs critiques (lue : n de 40 à 150) | `brouillons/couche4-essai-preuve-formelle-v1/calculs-v3/valeurs-critiques-calibrees-v1.json` | `fbd77a23b1814db17d8818416030aaa5550786a72d899d3deeca19f202db2acf` |
| code R du score apparié (appui) | `docs/sources/pdf/score-apparie-tango-v1/contingencytables-3.1.1-Tango_asymptotic_score_CI_paired_2x2.R` | `5248271a97b7f612e375c2602c8a1e62c4a3f4769fe4930c6ad0daa3bf016f31` |
| relevés de prix | `docs/notes/mathematiques-nouvelles-v1/releves-prix-et-source-score-apparie-v1.md` | `a7d9073f360b12f2fa914e49d1fd8d56acef86dc81136a494d962c96b2131218` |
| vérification de la commande de Lean | `docs/notes/mathematiques-nouvelles-v1/verification-juge-standard-lean-v4.35.0-v1.md` | `5748817e9197f59f61ae10176a633d535f693fab64f5ddb3bc53db3f5e5c7a48` |
| POPPER (PDF) | `docs/sources/pdf/huang-2025-icml-pmlr-267-popper-automated-hypothesis-validation-agentic-sequential-falsifications.pdf` | `a3c4b3701543a84a74602ae46a624b955e201bb83baeea2c219213a0e65b4998` |
| empreintes du code, version 6 | `prereg/mathematiques-nouvelles-v1/empreintes-code-lot-b1-v6.md` | `831e7b3b57d77a9bd47a121eba58cd6b58c7641f6d1ce67922e4962a963ec733` |
| paramètres gelés | `src/controle_ia/oracles_plantes_v6/parametres_v6.json` | `47459695ddfadf20dc63d5f30c4b44914037bfeb602392f42cb2a423e1e942ae` |
| note de choix v6 | `docs/notes/mathematiques-nouvelles-v1/lot-b1-code-v1/note-choix-implementation-lot-b1-v6.md` | `7c996b824155a8892e4eaebdce76846811edafa65735f5eb6ab3a056a0b8d0b0` |
| rapport des essais R5 v6 | `docs/notes/mathematiques-nouvelles-v1/lot-b1-code-v1/rapport-essais-r5-lot-b1-v6.md` | `0e6b4338ef2640bf23ec7f8880a56a0ef7a8926c6252cd8e4077262f56513db1` |
| vérification du code v6 | `docs/notes/mathematiques-nouvelles-v1/lot-b1-code-v1/verification-corrections-lot-b1-v5.md` | `045030e2a76bc7b222a77d3c49862fe8ff417a6413bb2af90724cb1ebca0c0c7` |
| aires de la version 6 | `docs/notes/mathematiques-nouvelles-v1/versement-bloc-notes-2026-11-22-v1/v6-aires.json` | `32cd1781b48758c48395996829f11ea84eac3c2282ba71d0cfa53cf88e7d4462` |
| balayage de la version 6 (script) | `docs/notes/mathematiques-nouvelles-v1/versement-bloc-notes-2026-11-22-v1/balayage_v6.py` | `e4aa52861002c8203029ab65f03ce78a843a9ed3c3771b548e0aafdd73c37d86` |
| balayage de la version 6 (sortie) | `docs/notes/mathematiques-nouvelles-v1/versement-bloc-notes-2026-11-22-v1/v6-balayage.txt` | `180edc16a9b883b99ea30017d837b80f350980a345e14f02cb319e5de4753e7a` |
| sonde « instances aveugles » (script) | `prereg/mathematiques-nouvelles-v1/calculs-v4/sonde_instances_aveugles_v1.py` | `b44525fc32d8abde5f9b3cfd0e559d3d37dea27c21cb9ab680d76ada6eb29395` |
| sonde (sortie) | `prereg/mathematiques-nouvelles-v1/calculs-v4/sortie-sonde-instances-aveugles-v1.txt` | `e6ae3d493f8c4a1973b19be1a3a1fbe5a5319f76ddfde2bb2b759115e86771df` |
| sonde (données par racine) | `prereg/mathematiques-nouvelles-v1/calculs-v4/sonde-instances-aveugles-v1.json` | `bea6ac4622635accfa00e3e727f429182922eaf3d781a8296f144d06b98804f6` |
| calculs du devis v4 et des constantes (script) | `prereg/mathematiques-nouvelles-v1/calculs-v4/calculs_devis_pilote_generation_v4.py` | `84bd0b15364bc29e7aa4427c98ebde725e06495bc539b9e696bdd603c957668e` |
| calculs v4 (sortie) | `prereg/mathematiques-nouvelles-v1/calculs-v4/sortie-calculs-devis-pilote-generation-v4.txt` | `8194b015cd0a481824ee591db77a18d0933c27fb5ef59557828293ad1e2781f0` |
| calculs du devis v3 (sortie) | `prereg/mathematiques-nouvelles-v1/calculs-v3/sortie-calculs-devis-pilote-generation-v3.txt` | `efcbc21f768a2f558a967d1cd6ec1c39dad1daf67fce13ffec8bb09cd3f8eb74` |
| écarts du devis v3 | `prereg/mathematiques-nouvelles-v1/calculs-v3/ecarts-devis-v3-main-contre-script-v1.md` | `60ba28c23c920ff31b3a1784a4f30346e7f23acbb4552dfc8ab5bfc4d6fce510` |
| brouillon 3 (remplacé) | `prereg/mathematiques-nouvelles-v1/preenregistrement-pilote-generation-v1-brouillon-3.md` | `e33d7bec1f9c606d0cac96836e3748a02cc50444bcde689165e1280d32b655bb` |
| contre-lecture du brouillon 3 | `prereg/mathematiques-nouvelles-v1/contre-lecture-brouillon-3-v1.md` | `65152d7fab2d3a1a8ccc193ab470d5bae5e720b963981ae1041ac4cc9612251c` |
| mandat de cette session | `docs/notes/mathematiques-nouvelles-v1/brouillon-2-fable-v1/mandat-fable-brouillon-4-v2.md` | `4a3412ab3fafcf79a6651f486ed972ee370beb62646c026c408d6cf5f1ae9116` |

## Pièces à remplir

- DATE ;
- DÉCISION-SEUIL (mot du directeur sur le seuil 0,75, ou défaut échu) ;
- PLAFOND-GO ; ÉCHÉANCE (fixés par le GO sur le devis, portés avant le scellement) ;
- ANTÉRIORITÉ (protocole P exécuté avant le scellement) ;
- LISTE-DES-CONNUS ;
- CONSIGNES ;
- ESSAIS-R5 ;
- CONTRE-LECTURE.

Ne sont pas des blancs de ce texte : la racine (tirée au scellement, jamais écrite ici) ; le script d'analyse (scellé après ce texte, avant la course) ; le commit du code (rempli).

## Contre-lecture

- Contre-lecture 1 : Opus 5.5 neuf, sur le brouillon 3 (`e33d7bec1f9c606d0cac96836e3748a02cc50444bcde689165e1280d32b655bb`) ; rapport `prereg/mathematiques-nouvelles-v1/contre-lecture-brouillon-3-v1.md` (`65152d7fab2d3a1a8ccc193ab470d5bae5e720b963981ae1041ac4cc9612251c`) : 6 remarques bloquantes, 13 à corriger, 8 mineures, traitées une à une ci-dessous.
- Contre-lecture 2 : **À REMPLIR : CONTRE-LECTURE** — vérification des corrections par le même contre-lecteur, sur ce brouillon 4. Lui donner : ce texte, le devis v4, les notes au directeur, la sortie du script v4, la sonde et sa sortie, la contre-lecture du brouillon 3, l'erratum 1, les relevés de prix, la note v6, la vérification du code v6, les aires de la version 6.

## Traitement de la contre-lecture du brouillon 3

Une ligne par remarque du rapport `65152d7f…`.

| n° | objet | sort | ce que le texte porte |
|---|---|---|---|
| 1 | H3 sans critère sous la branche haute ; « N aucun par construction » | acceptée, critère changé | N reçoit le schéma de S et passe par T6 ; lecture en preuve E1 à E5. Le seuil absolu proposé sur v_S (0,30) est refusé : une règle sans calcul atteint 0,80 à 0,91, il serait acquis par construction. Il est remplacé par la comparaison à la règle aveugle (E4) |
| 2 | lignes de H3 sans branche ; φ_S vide ; « non porté » non chiffré | acceptée | colonne « branche d'aire » ; φ_S dit nul par construction sous la règle des contre-exemples vérifiés ; « en verdict, pas en preuve » chiffré par V1 sans E1 |
| 3 | seuil 0,75 décidé après la mesure ; mesure hors dépôt | acceptée, forme (a) | mesure versée et citée (chemin, empreinte) ; seuil gardé, dit gardé après lecture ; branche haute dite attendue ; blanc DÉCISION-SEUIL ; version 7 au dossier du pilote 2 |
| 4 | verdicts de H1 recouvrants ; base absente ; niveau faux ; retrouvées à deux familles | acceptée | § Seuil et table réécrits ; base à 0,15 en différence ponctuelle ; règle dite descriptive, sans niveau nominal ; union des deux proposeurs ; cas limite renvoyé à « non concluant » |
| 5 | graine racine en blanc | acceptée, renforcée | tirage de trois racines de 128 bits dans la commande de scellement ; le manifeste poussé ne porte que leurs empreintes, les racines vivent avec les clés jusqu'à leur ouverture (une racine en clair sur la branche livrerait les clés) |
| 6 | faux « connu » de H4 mal défini | acceptée, variante | 20 énoncés faux de mondes seulement (enfant (7, 1)) : la note est mécanique, sans lecture de la référence. Refusé : y mettre les vérités à littéral tiré, dont l'étiquette « corollaire immédiat » serait défendable. Strates 20 et 20 ; taux ponctuel, au plus 2 sur 20 ; ce que le juge reçoit est fixé ; liste source en blanc |
| 7 | H2 : unité, coût apparié, k, ex æquo, rapport | acceptée | Y_c(w) par dollar ; k(n) de 8 à 12 ; « k = 24 tirages, sans vote, coût mesuré » ; rapport des sommes ; un seul prix d'Argon |
| 8 | état initial du registre de lignée | acceptée | trois registres vides au départ ; morts de S et de N à part ; comptes par source |
| 9 | réserve de A6 et borne de concurrence | acceptée, chiffre changé | « pire cas » rétabli ; créneaux écrits. La réserve passe de 5,93 à 6,50 : un item N en vol (0,496 au pire) et le relecteur de repli manquaient au calcul |
| 10 | documents de la version 5 ; COMMIT-CODE | acceptée | documents de la version 6, empreintes entières ; commit `35ac9e10…` rempli ; A1 dite éprouvée en version 6 |
| 11 | « le texte ne se répète plus » | acceptée | phrase restreinte aux cinq gabarits à k ; l'écart 16 contre 17 est tranché : le compte dépend de la racine (16 à 18) |
| 12 | certification des pièges et redite | acceptée | ligne de certification écrite ; choix du code approuvé avec sa raison |
| 13 | audit de symétrie non symétrique | acceptée | déclencheurs des deux côtés pour H1, H2, H3 (preuve et verdict) et H4 |
| 14 | fumée en échec pour Opus ou Argon | acceptée | aucun lancement, retour au directeur ; A2 réécrite |
| 15 | réfutations fausses : dénominateur et borne | acceptée | 150 items analysés, premier service ; borne haute de Clopper–Pearson à 97,5 % |
| 16 | A4 : alerte et manque | acceptée | définitions écrites ; seul le code lit la clé des témoins |
| 17 | blancs sans marqueur | acceptée | DATE, CONSIGNES et les blancs ajoutés portent le marqueur ; le script d'analyse sort des blancs |
| 18 | branche basse jamais éprouvée ; contexte neuf sans garde | acceptée | banque artefact d'aire ≤ 0,75 aux essais R5 ; A8 étendue à « un seul item par journal » |
| 19 | trois écarts du devis v3 | acceptée | devis v4 : calcul du plafond refait, renvoi à la sortie du script, « le bas prend le juge Astra » |
| 20 | « nouveau », « nouvelle » en étiquettes | acceptée | « ajoutée au brouillon 3 », « ajoutée au brouillon 4 » ; « neufs par construction » retiré |
| 21 | citations seulement nommées | acceptée | références et chemin de POPPER ; CADS rétabli à la question 5 |
| 22 | fait sur Lean sans source | acceptée | chemin et empreinte de la note de vérification |
| 23 | A9 sans « par identifiant » | acceptée | rétabli |
| 24 | exception « retrouvée » asymétrique | acceptée | précision sans l'exception rapportée au même rang |
| 25 | A5 : « proposeur » | acceptée | « un modèle dans une configuration » |
| 26 | aire sans intervalle | acceptée, enfant changé | intervalle par rééchantillonnage des mondes, enfant (10, 2) et non (10, 0) : un flux par tâche (R9) |
| 27 | course arrêtée en route | acceptée, étendue | ligne de la table : « non courue », seuils d'effectif par hypothèse |

Voie du contre-lecteur non retenue (son § « ce que H3 peut encore affirmer ») : apparier par tranches de score de style. Avec une aire de 0,94 à 0,98, la zone de recouvrement ne garderait qu'une poignée d'items.

## Écarts au brouillon 3

- **H3 reformulée** : la part affirmable passe des verdicts déclarés aux contre-exemples vérifiés, contre deux bases (lecture nue, règle aveugle A). Les verdicts déclarés ne sont affirmables que sous le seuil d'aire.
- **Ce que S et N jugent** : plafond B = 3N servi dans leur consigne ; « faux » défini par un contre-exemple dans [0 .. B]. Le brouillon 3 ne le disait pas.
- **Bras N** : même schéma de sortie que S, T6 sur ses instances ; trois instances au plus par sortie, pour les deux bras ; sortie de S avant relecture en sensibilité.
- **Règle aveugle A** ajoutée aux bases ; P11 et E4 ajoutées. Mesure sur racines d'essai par une sonde du concepteur.
- **P5** récrite pour la lecture en preuve ; anciens intervalles des verdicts déplacés en P5 bis et élargis (le plafond B change ce qu'un bras peut trouver sur les pièges). P12 ajoutée.
- **Seuil 0,75** : gardé, dit gardé après lecture de la mesure ; blanc DÉCISION-SEUIL.
- **H1** : verdicts disjoints, base au seuil, règle dite descriptive. **H2** : unité, k(n), rapport des sommes, un seul prix d'Argon.
- **H4** : 20 énoncés faux de mondes ; strates 20 et 20 ; quatre transformations ; relecture de fidélité et remplacement ; ce que le juge reçoit ; deuxième étiquette adaptée à l'absence de bibliothèque (« corollaire immédiat d'un énoncé connu ») ; règle de forme en base ; blanc LISTE-DES-CONNUS.
- **Racine** : trois racines de 128 bits tirées au scellement, engagées par leurs empreintes, révélées à l'ouverture des clés. Le blanc GRAINE-RACINE disparaît.
- **Registres** : trois, vides au départ. **Proposeurs** : une proposition par appel, propres antérieures visibles, sans issue.
- **Gardes et ordre** : A1 (tout code non nul), A2, A4, A5, A6 (réserve 6,50, créneaux), A8, A9 récrites ; A14 ajoutée ; ligne « rôle ou course arrêtés » ; scellement et tirage en tête de l'ordre ; course en douze blocs d'un monde.
- **Graines** : (5, 0), (5, 1), (7, 0), (7, 1), (10, 2) ajoutés ; aucun enfant existant ne change.
- **Sensibilité** : précision sans l'exception « retrouvée », précision à 3N, rééchantillonnage par gabarit.
- **Code** : version 6 retenue, COMMIT-CODE rempli ; deux choix approuvés ; aucune version 7.
- **Antériorité** : lecteur « ni Claude, ni Gemini » ; moisson par code ; extraits vérifiés par programme ; citants bornés à deux par question.
- **Blancs** : ajoutés DATE, DÉCISION-SEUIL, LISTE-DES-CONNUS ; retirés GRAINE-RACINE, COMMIT-CODE, SCRIPT-ANALYSE.
