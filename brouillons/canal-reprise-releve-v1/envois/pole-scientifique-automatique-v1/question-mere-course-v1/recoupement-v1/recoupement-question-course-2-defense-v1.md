# Recoupement — question de la course 2, volet défense (axes 1, 2, 3, 4, 5, 7 et boucle) — v1

Sous-agent neuf (Opus 5.5), 29 octobre 2026, `date -u` 11:52 UTC ; auteur d'aucune entrée. Critères : § 3 de `question-mere-course-ideation-v3.md`
(`1b08e17f…`), à la lettre. Entrées vérifiées par leur `.sha256` : [CA]
`reponse-conv-audit-question-mere-v1.md` (`7935d458…`) et complément d'axe 7 (`e5511fca…`) ; [ON] `reponse-opus-neuf-question-mere-v1.md`
(`6bf58e99…`) et complément (`a8200b54…`) ; [SD] `entrees/question-course-2-v1.md` (`21833d9f…`, pistes A, B, C) ; [AR]
`entrees/reponse-argon-question-mere-v3-v1.md` (`5a6603e3…`), lu à côté, **jamais compté** ; [v0] `question-course-2-fusion-v0.md`
(`97cf7306…`, lignée conv-audit, structure seulement, non compté). Le collisionneur n'a pas répondu : v2 du recoupement à sa réponse.
Hors périmètre, sauté et non repris : l'axe des hypothèses fragiles et son texte. Rien n'est scellé. Couverture : [CA] et [ON] répondent
aux versions 1 et 2, avant le point 8 ; aucun répondant compté ne traite la boucle ; [SD] ne couvre ni l'axe 2 en propre, ni l'axe 7.
Statuts : **commun** (deux répondants comptés, même livrable, même critère de juge) ; **divergent → Dn** ; **écarté** (mode, recette, sortie
lisible par les concepteurs, hors garde) ; **circulaire** (`donnees/` ou écarts du sujet avant G1) ; **non jugeable** ; **imposé** (Lazar, règle gelée).

## A. Table de recoupement
| Id | Élément (définition opérationnelle) | Donné par | Statut |
|---|---|---|---|
| F1 | Une course, un texte « défense », un préambule commun | CA, ON, SD (une question) ; AR | commun ; imposé |
| F2 | Axe 7 servi à une sous-session neuve, sans le texte des axes 1 à 5 | ON ; contre : CA, AR (même texte) | divergent → D1 |
| F3 | Passe 2 : corrections vérifiables seules, aucune fiche nouvelle | ON ; CA (affinage) ; SD (trois tours dont riposte) ; AR (g = 0 puis 1) | divergent → D2 |
| F4 | Glossaire de théorie de la détection en tête | SD ; AR (notation P_0, P_θ) | imposé (Lazar) |
| F5 | Repères chiffrés d'HELIOS dans le texte, avec page | CA, ON, SD ; AR | commun (0,38 p. 18 ; table 2 p. 27 revérifiés sur pièce B) |
| P1 | Noyau de fiche : hypothèse, prédiction chiffrée signée, coût, antériorités (titre, auteurs, année), critère de mort, SUPPOSÉ | CA, ON, SD ; AR | commun |
| P2 | Critère de mort = seuil numérique écrit avant lecture | ON (K0.3), SD (« quel nombre, lu une fois ») ; CA (forme libre) | commun |
| P3 | Budget de la première expérience : processeur seul ou données déjà payées | CA (axe 7 e), SD (A5, A6) ; ON : ≤ 300 dollars ou processeur ; AR : 50 ou 20 (illustratif) | divergent → D3 |
| P4 | Tout chiffre → pièce et page ; sinon SUPPOSÉ ou « à vérifier » | CA, ON, SD ; AR | commun |
| P5 | Contrôle par programme des chiffres d'HELIOS contre la pièce B | ON | divergent → D10 |
| P6 | Données réclamées seulement dans une liste fermée D ; aucune lecture pendant la course | CA (« dire lesquelles et pour quelle mesure »), ON (F5, K0.5) | commun |
| P7 | Tranche exploratoire : tirée par un tiers, identifiants scellés, déclarée brûlée au registre de fraîcheur | ON (brûlée) ; CA (identifiants scellés) | divergent cumulable → D10 |
| P8 | Directions de sonde réclamables ou servies | CA (réclamables) ; AR (servies) ; contre : ON (internes exclus) | divergent → D9 ; « servies » [AR] : écarté (garde) |
| P9 | Longueur 3 000 à 8 000 caractères ; au plus deux fiches par axe | CA ; ON | divergent mineur → D10 |
| J1 | Critères binaires ; mots d'appréciation interdits | CA, ON ; AR | commun |
| J2 | Fiche sans livrable obligatoire non notée (K1) | CA, ON ; AR | commun |
| J3 | Prédiction chiffrée signée obligatoire ; rappel à 1 % par famille, aire seule insuffisante (K3) | CA (3), ON (K0.2), SD (critère 1, A4) ; AR | commun |
| J4 | Avantage : source dans la liste fermée L + coût de reproduction chiffré, ou élément absent de l'antériorité la plus proche (K2) | ON ; CA (texte libre) | divergent, tranché par la contrainte « listes fermées » |
| J5 | Note 0 à 3, porte max(avantage, originalité) ≥ 2 | CA | non jugeable (« originalité ») ; remplacé par J6 |
| J6 | Classement des notables : facultatifs passés, puis coût | ON ; AR (paliers de mise par compte) | divergent → D8 |
| J7 | Témoin planté | ON | imposé (Lazar) |
| J8 | Fiche décrivant une conduite d'agent écartée avant le juge, comptée | CA, ON, SD ; AR | commun |
| J9 | Antériorité « à vérifier » sauf PDF ; zone vierge = question | CA, ON, SD (critères 2, 3) ; AR | commun |
| A1.1 | Table des écarts : valeur d'HELIOS avec page / « non mesuré » | CA (a), ON (K1.1, trois lignes au moins) ; AR | commun |
| A1.2 | Statistique au point de codage : quantité lue, couche, jeton, agrégation, apprentissage, seuil | CA (b), SD (A1) ; AR | commun |
| A1.3 | « Nouvelle par rapport à HELIOS et au programme » | CA | non jugeable → réécrit « comble une ligne de la table » [ON] |
| A1.4 | Case dans le plan accès × agrégation | SD (A2) | divergent → D10 |
| A1.5 | Plancher apparié | CA, ON, SD (glossaire, A5) ; AR | commun |
| A1.6 | Sonde nulle de chaîne ; couches séparées ; hyperparamètres réglés hors épreuve | ON (K1.2, K1.6) ; AR ; pièce B (avis, A2, A5, C3) | divergent → D4 |
| A1.7 | Au moins un comparateur boîte noire scellé à capacité égale | CA, ON ; AR | commun |
| A1.8 | Comparateur gradué en information (nu, informé, à exemples) obligatoire | CA ; AR ; ON : facultatif (K1.8) | divergent → D4 |
| A1.9 | Lecture d'HELIOS rejouée sur notre banc comme base | CA (cinq couches moyennées), ON (K1.3, dernier jeton) ; AR | commun sur l'objet ; couches → D4 |
| A1.11 | Borne basse contre quantile 0,95 du plancher | CA (d), SD (glossaire) | commun |
| A1.12 | Invariance qui justifie le transfert ; pourquoi la direction logistique ne l'a pas | SD (A3) | divergent → D10 |
| A1.13 | Prédiction sur un transfert de type HELIOS (une famille apprise, six lues) | SD (A4) | divergent → D10 (facultatif) |
| A1.14 | Aucune moyenne ni médiane sur les jetons en production | ON (K1.4) | imposé (interdit du programme) |
| A1.15 | Jouable par le juge figé (unités par famille) ; séparation réalisation / lisibilité | ON (K1.5, K1.7) ; AR (m1, m2) | divergent → D10 (facultatifs) |
| A1.16 | Matériau de méthodes nommé, non imposé | CA, ON, SD ; AR | commun (union abrégée) |
| A1.17 | Traces d'activations d'honnêtes servies pour régler pendant la course | AR | circulaire |
| A2.1 | Forme {loi, notice, garantie, impossibilité} + énoncé quantifié falsifiable | CA (a), ON (K2.1) ; AR | commun |
| A2.2 | Test ou démonstration qui tue l'énoncé, pas seulement le test | CA (c), ON (K2.3, K2.4) | commun |
| A2.3 | Antériorité la plus proche | CA (d), ON (F8) | commun |
| A2.4 | Résultat publié qui rendrait l'énoncé inutile | CA (b) | divergent → D10 |
| A2.5 | Deux issues écrites, chacune en une phrase | ON (K2.2) ; SD (« fort / incrémental », autre définition) | divergent → D10 |
| A2.6 | Classes définies sans référence aux familles scellées | ON (K2.5) | divergent → D10 |
| A2.7 | Formules d'Argon : « vœux pieux », « en 48 heures », « non copiable » | AR | non jugeable |
| A3.1 | Faille + mesure à seuil (valeur qui confirme, valeur qui infirme) | CA (b), ON (K3.2), SD (B2) ; AR | commun |
| A3.2 | Riposte ou correctif, et coût | CA (c, d), ON (K3.3), SD (B5) ; AR | commun |
| A3.3 | Pré-mortem : G1 non franchie, hypothèse qui cède, ordre, mesure qui tranche | SD (B4) | imposé (Lazar) |
| A3.4 | Classe de faille dans une liste fermée | ON (K3.4) ; SD (hypothèses i à iv) ; CA (exemples) | tranché par « listes fermées » (union ON + SD) |
| A3.5 | Faille rattachée à une phrase citée de la pièce A ou C | ON (K3.1) | divergent → D10 |
| A3.6 | Classe de lois déplacées écrite formellement | SD (B1) | divergent → D10 (« si statistique ») |
| A3.7 | Mesure calculable en simulation ou sur D | ON ; SD (« nos données ou processeur ») | commun si « nos données » = D ; sinon circulaire |
| A3.8 | Argon seul : succès obligé de l'axe 3 (juges à 99 %, m1/m2) ; opérateur qui sature la borne (axe 5) ; mort contre les 424 sondes | AR | Argon seul (§ C) ; non compté |
| A4.1 | Livrable = préenregistrement à sceller, pas un résultat | CA, ON, SD (C4) ; AR | commun |
| A4.2 | Familles fixées par une instance tierce | CA, ON, SD ; AR | commun |
| A4.3 | Exclusion d'une famille à la fois | CA, ON ; AR | commun |
| A4.4 | Lecture par famille : borne basse contre quantile 0,95 ; fausses alertes ≤ 5 points | CA, ON ; AR | commun |
| A4.5 | Si échec : hypothèse cédée et statistique qui la relâche | CA, ON ; AR | commun |
| A4.6 | Hypothèse désignée d'avance, avec statistique de diagnostic | ON (K4.4) ; AR ; contre : CA (nommée après) | divergent → D5 |
| A4.7 | Unités, puissance selon le nombre de familles, coût | CA (f), ON (K4.6), SD (C3) ; AR | commun |
| A4.8 | Contrôle d'artefact de source par classifieur de provenance sur honnêtes | ON (K4.5) | divergent → D10 |
| A4.9 | Familles publiées comme familles supplémentaires, ordonnées par distance | SD (C1) | divergent → D6 |
| A4.10 | Statistique d'universalité (rapport hors / en distribution ; pente) | SD (C2) | divergent → D6 |
| A4.11 | « Testable aujourd'hui sans dépense sur les modes existants » | SD (C6) | circulaire tel quel ; réécrit (simulation, données publiques) |
| A4.12 | Arbre de diagnostic sur les 23 hypothèses de la carte | AR | écarté (carte non servie) |
| A5.1 | Objets, hypothèses numérotées, conclusion quantifiée | CA (a), ON (K5.1), SD (B3) ; AR | commun |
| A5.2 | Vérification : Lean, ou simulation préenregistrée | CA (b), ON (K5.2) ; AR | commun |
| A5.3 | Statistique justifiée / condamnée | CA (c), ON (K5.4) | commun |
| A5.4 | Quantité mesurable qui dit si l'hypothèse tient | ON (K5.5), SD (B2) | commun |
| A5.5 | Antériorité classique nommée | CA (d), ON (K5.6) | commun ; « apport explicite » [ON] → D10 |
| A5.6 | Cas d'hypothèse violée | ON (K5.3) | divergent → D10 |
| A7.1 | Angle + question falsifiable (signe ou deux issues) | CA (a), ON (G1) ; AR | commun |
| A7.2 | Pourquoi libre : antériorité la plus proche ; « libre » relatif au dossier ; R8 | CA (b), ON (G4) ; AR | commun |
| A7.3 | Trois requêtes exactes ; occupant qui l'annonce en travail futur | ON (G4) | divergent → D10 |
| A7.4 | Ajoute / coûte | CA (c), ON (G5) ; AR | commun |
| A7.5 | Source d'avantage dans L élargie | ON (G6) ; CA (texte libre) | tranché par « listes fermées » |
| A7.6 | Première expérience qui le tue, valeur qui tue | CA (e), ON (G7) ; AR | commun (budget → D3) |
| A7.7 | Table de substitution, deux colonnes sur quatre différentes | ON (K7.2) | divergent → D7 |
| A7.8 | « Le juge compare aux huit textes et écarte toute paraphrase » | CA | non jugeable → réécrit en bardeaux de mots par programme → D7 |
| A7.9 | Grille des sous-domaines ; trois cases au moins, une au plus couverte | ON (G2, K7.6) | divergent → D11 |
| A7.10 | Au plus cinq angles classés (CA) / au plus quatre (ON) | CA ; ON | divergent → D10 |
| A7.11 | Angle qui exige de produire des lois déplacées : non noté | CA, ON | commun (destination : hors périmètre) |
| A7.12 | Lien obligatoire à un axe, ou « hors axes » | CA (f) ; ON facultatif (K7.8) | divergent → absorbé par D12 |
| A7.13 | Vérification « non occupé » après course par sous-agent neuf, sur PDF | CA, ON ; AR | commun (consigne d'orchestrateur) |
| A7.14 | Seconde recherche, adverse, par un autre fournisseur | ON ; AR | divergent → D10 |
| V1 | Reproduction tierce depuis la copie publique | CA, ON ; AR | commun |
| V2 | Banc d'HELIOS rejoué quand le dépôt est obtenu | CA, ON ; AR | commun (récupération = nœud) |
| V3 | Logiciel de preuve comme arbitre | CA, ON ; AR | commun |
| V4 | Familles tenues hors du programme (occupants publiés [CA] ; organismes publics [ON]) | CA, ON (définitions différentes) ; SD (C1) | divergent → D6 |
| V5 | Statisticien extérieur | ON | divergent (contact externe = nœud) ; hors texte servi |
| M1 | Mort : aucune notable (CA) / moins de trois axes avec une notable (ON) | CA ; ON | divergent → D13 |
| M2 | Mort : PDF (ON b ; CA axe 7) ; reformulation des huit (CA) ; aucun préenregistrement scellable (ON c) | CA ; ON | divergent → D13 |
| M5 | Mort : le témoin planté échoue | ON (d) | imposé (Lazar) |
| M6 | Réserves de symétrie : tables contradictoires (CA) ; presque tout notable (ON) | CA ; ON | divergent → D13 (cumulables) |
| B1 | Vis-à-vis angle ↔ faille vérifié binaire ; exigé dès g = 0 (AR) ou dès la génération 2 (v0) | v0 ; AR | divergent (aucun compté) → D12 |
| B2 | Reçu par g + 1 : anonymes, verdict, classement (v0) / promues entières, rejetées en table (AR) ; étiquette d'héritage (AR) | v0 ; AR | divergent → D12 |
| B5 | Seuil de similarité 0,85 (illustratif) | AR | non jugeable tant qu'il n'est pas fixé |
| B6 | Arrêt : mesure consignée d'abord, règle ensuite si scellable | v0 ; AR | imposé (point 8 de la question-mère) |
| B7 | Règle d'arrêt : deux générations sans neuf (v0) / seuils illustratifs (AR) | v0 ; AR | divergent → D12 |
| B8 | Vis-à-vis par identifiants de la carte des hypothèses | AR | écarté (carte non servie) |
| B9 | Coût et GO par génération | v0 ; AR (montants de la pièce A, à vérifier) | imposé (dépense = nœud) |

**Comptes** : 102 éléments ; **commun 44** ; **divergent 41** (dont 4 tranchés par « listes fermées » ou absorbés : J4, A3.4, A7.5, A7.12) ;
**écarté 2** (A4.12, B8 ; plus P8 en partie) ; **circulaire 2** (A1.17 ; A4.11 tel quel ; A3.7 sous condition) ; **non jugeable 5** ; **imposé 7** ;
Argon seul 1. Aucune antériorité n'entre dans le texte servi ; seule HELIOS est vérifiée sur PDF (pièce B). **À vérifier sur PDF** : Wald 1945 ;
Ramdas et al. 2023 ; Xie et Siegmund 2013 ; Lorden 1971 ; Lai 1998 ; Tartakovsky, Nikiforov, Basseville 2014 ; Shin, Ramdas, Rinaldo
(e-détecteurs) ; Tibshirani et al. 2019 ; Page 1954 ; Goldowsky-Dill et al. 2025 ; McKenzie et al. 2025 ; Arditi et al. 2024 ; Gulrajani et
Lopez-Paz 2021 ; Koh et al. 2021 ; Chong, Tiňo, Yao 2008 ; « leave-one-category-out » (non identifié) ; Kirch et al. ; Das et al. 2026 ;
Shi et al. 2026 ; Greenblatt et al. 2024 ; Korbak et al. 2025 ; Bhatt et al. 2025 ; Mitchell et al. 2019 ; Klein 2007 ; Zwicky (date non établie).

## B. Divergences pour Lazar (format décision ; défaut appliqué sous 48 heures)
- **D1. L'axe 7 est-il servi à une sous-session neuve, sans le texte des axes 1 à 5 ?** Enjeu : ancrage des angles sur nos axes contre
  couplage dans la même génération. (a) Sous-session neuve [ON] : moins d'ancrage ; le couplage passe par la génération suivante. (b) Même
  texte [CA, AR] : couplage immédiat ; risque d'angles qui redisent les axes. Recommandation : (a), confiance 0,6. Défaut : (a).
- **D2. Que permet la passe 2 ?** Enjeu : mesurer l'affinage sans débat. (a) Corrections vérifiables seules, aucune fiche nouvelle [ON] :
  jugeable, pas de dérive par débat ; l'affinage passe à la génération suivante. (b) Affinage, fiches réécrites [CA, AR] : plus de matière ;
  mélange de deux mesures. Recommandation : (a), confiance 0,7. Défaut : (a).
- **D3. Quel budget pour la première expérience qui tue (K4) ?** Enjeu : jugeabilité et absence de dépense implicite. (a) Processeur seul ou
  données déjà payées [CA, SD] : aucune dépense ; exclut des tests utiles sur carte. (b) Jusqu'à 300 dollars [ON] : plus large ; chaque fiche
  appelle un devis. Recommandation : (a), la dépense restant un nœud, confiance 0,7. Défaut : (a).
- **D4. Quels contrôles l'axe 1 rend-il obligatoires ?** Enjeu : comparabilité avec HELIOS. (a) Minimal commun : plancher, un comparateur boîte
  noire. (b) (a) + sonde nulle de chaîne, lecture d'HELIOS rejouée (dernier jeton), couches séparées, hyperparamètres hors épreuve [ON, pièce B] :
  contrôles à coût nul ; fiches plus longues. (c) (b) + comparateur gradué obligatoire [CA, AR] : complet ; plus de lectures au devis.
  Recommandation : (b), gradué en facultatif, confiance 0,7. Défaut : (b).
- **D5. À l'axe 4, l'hypothèse incriminée est-elle désignée d'avance ?** Enjeu : explication après coup. (a) D'avance, avec statistique de
  diagnostic [ON, AR] : falsifiable ; demande une liste d'hypothèses servie. (b) Nommée après l'échec [CA] : plus souple ; non falsifiable.
  Recommandation : (a), confiance 0,8. Défaut : (a).
- **D6. Que fait-on des ajouts de session-depot et des familles hors programme à l'axe 4 ?** Enjeu : puissance contre définition de « tient ».
  (a) Facultatifs rapportés, non décisifs ; critère par famille seul décisif : rien ne change au critère commun. (b) Décisifs : plus de
  familles ; deux critères à concilier. (c) Retirés. Recommandation : (a), confiance 0,65. Défaut : (a).
- **D7. Quelle garde contre la reformulation des huit questions ?** Enjeu : seul point de l'axe 7 où le juge risque d'interpréter. (a) Table de
  substitution [ON] + bardeaux de mots par programme [CA réécrit] : deux filtres, l'un mécanique. (b) Table seule : plus court ; synonymes
  non vus. (c) Bardeaux seuls : mécanique ; manque les reformulations de fond. Recommandation : (a), confiance 0,75. Défaut : (a).
- **D8. Comment classer les fiches notables ?** Enjeu : la note 0 à 3 de [CA] est non jugeable. (a) Nombre de facultatifs passés, puis coût
  [ON] : binaire ; favorise les fiches longues. (b) Paliers de mise par compte [AR] : relie au juge figé ; seuils non fixés. Recommandation :
  (a), confiance 0,65. Défaut : (a).
- **D9. Les directions de sonde peuvent-elles être réclamées ?** Enjeu : garde « internes des moniteurs ». (a) Exclues [ON, garde] : sûr ;
  moins de diagnostic. (b) Réclamables en tranche exploratoire [CA] : diagnostic du nul ; contredit la garde. Recommandation : (a), confiance
  0,85. Défaut : (a) ; la garde le tranche déjà, d'où aucune marque dans le texte.
- **D10. Lot de petits écarts à un seul répondant** (P5, P7, P9, A1.4, A1.12, A1.13, A1.15, A2.4–A2.6, A3.5, A3.6, A4.8, A5.5, A5.6, A7.3,
  A7.10, A7.14, pièces G, H, I de [SD]). Enjeu : longueur du texte. (a) Tous adoptés comme dans la fusion (facultatifs là où marqué) :
  complet ; texte à 11 971 caractères. (b) Ne garder que le commun : plus court ; perd l'invariance [SD] et l'artefact de source [ON].
  Recommandation : (a), confiance 0,6. Défaut : (a) ; non marqué un à un dans le texte.
- **D11. Sert-on une grille des sous-domaines, avec répartition par cases ?** Enjeu : sortir du cadre sans juge qui dise « large ». (a) Oui,
  grille d'[ON] arrêtée par Lazar, trois cases, une couverte au plus : mécanique ; grille non vérifiée. (b) Non : rien à arrêter ; angles
  concentrés. Recommandation : (a), confiance 0,6. Défaut : (a) avec la grille d'[ON] telle quelle.
- **D12. Quelle boucle entre générations ?** Enjeu : aucun répondant compté ne la traite. (a) Règle de la fusion : vis-à-vis dès la génération 2,
  g + 1 reçoit fiches anonymes, verdict, classement, étiquette d'héritage [AR] ; arrêt mesuré puis réglé. (b) Règle d'Argon : vis-à-vis dès
  g = 0, rejetées en table, seuils chiffrés : plus mécanique ; seuils illustratifs. (c) Attendre le collisionneur (v2). Recommandation : (a),
  puis recoupement v2, confiance 0,55. Défaut : (a).
- **D13. Quel critère de mort pour la course ?** Enjeu : aucune condition n'est commune. (a) Union de M1 (version d'ON), M2 et M5, M6 en
  réserves : sévère, écrit d'avance. (b) M1 et M5 seuls : simple ; tolère l'invérifié. Recommandation : (a), confiance 0,7. Défaut : (a).

## C. Ce qu'Argon apporte de neuf sur ces axes, et ce qu'il faut vérifier
- Neuf : calibrage conditionnel à la longueur pour tout maximum sur les jetons (biais d'extrême) ; lecture en intention de traiter et par
  protocole avec taux d'exécution ; à l'axe 5, dériver un opérateur qui sature la borne (retrait de la nuisance d'épisode) ; étiquette
  d'héritage neuve / affine / réfute, reprise en D12. Le deuxième vient de la pièce B (avis, A3) ; le premier est marqué hypothèse par Argon.
- À vérifier : les montants attribués à la pièce A (52,80 et 60 dollars, 424 sondes, 1,76 dollar, 7 500 et 12 000 dollars) ; son texte fait
  12 456 caractères (plafond dépassé) ; il sert la carte des hypothèses et les directions de sonde (hors garde, écartés).

**Réserves.** (1) Si les 240 épisodes de P3 visés par [SD] entrent dans une banque d'épreuve de G1, A3.7 et le test de mort de la piste A
deviennent circulaires : à vérifier chez session-depot. (2) L'axe 4 sur familles scellées consomme du matériau d'épreuve avant G1 : la
question-mère le prévoit ; le recouvrement entre ces familles et la liste de G1 reste à établir. (3) Non contre-lu (R2).
