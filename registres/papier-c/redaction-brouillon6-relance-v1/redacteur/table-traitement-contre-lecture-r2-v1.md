# Table de traitement — contre-lecture de la version r2 et contre-lecture du rapport de la grille — v1

Date : 2026-11-19. Auteur : rédacteur du préenregistrement (Claude Fable 5.2). Classe C.
Sources : contre-lecture de r2 (`rapport-contre-lecture-brouillon6-relance-r2-v1.md`,
`71996527139967939b66f8621fe7ab6a41de87c00f45ed8a0a986f478b424abc` : CR-01 à CR-10) ; rapport de la grille
(`8d1616fce0dc59ea6bd986e465ae24efd845e1db7954cb39d39399fbc1a6ea89`) ; sa contre-lecture
(`d0485a406d0b13b97e2141d42a401e93b026a3a3953b35fe2561ba3848788819` : CG-01 à CG-14). Empreintes recalculées par moi.
Texte : version r3 (`160730b4c3980d8d96b0d05ed4041f011b5bf78a7d8dc7f927ee1ed0c2463cac`), 67 remplacements exacts sur
r2 (`1ab62e7d…`) ; identifiants « T-… » = lignes du journal `travail/construire_brouillon6_relance_r3_v1.journal.tsv`.

## 1. Contre-lecture de r2

| Remarque | Gravité | Décision | Ce qui est fait dans r3 | Lieu (identifiant) |
|---|---|---|---|---|
| CR-01, clause générale de primauté | majeure | acceptée | Clause conditionnelle retirée. L'introduction de la section 8 dit : chaque précision fixe un passage nommé, ce passage y renvoie, la précision prime sans condition ; table des passages fixés, précision par précision. Un renvoi « section 8, précision n » est ajouté dans chacun des 36 passages visés (35 neufs, celui de la précision 9 existait), contrôlé par programme. | T-P3, T-R01 à T-R36 |
| CR-02, précision 18 | majeure | acceptée (consigne de la conduite : retour à la lecture symétrique, pas de décision neuve) | « Non testable à cette puissance » : ni confirmation ni réfutation, dans les deux sens ; issue brute rapportée à côté, sans verdict. Le passage du Plan, section 2, le dit aussi. | T-P5, T-R18 |
| CR-03, borne champs / paragraphe | majeure | acceptée, points (1) à (4) | (1) Symétrie : ligne vide suivie de texte dans une cellule sans bras = « illisible » ; paragraphe absent ou contenant une clé de champ dans une cellule à paragraphe = « illisible » ; même règle des 5 %. (2) Parts rapportées par cellule et par motif. (3) Essais du module sur cinq actions synthétiques. (4) Séparateur fixe possible par un champ de la configuration, à contre-lire. Limite restante déclarée : dernier champ de plusieurs paragraphes dans une cellule à paragraphe ; son taux est estimé par les cellules sans bras. | T-P4 |
| CR-04, précision 34 | mineure | acceptée dans sa seconde forme (consigne de la conduite : lecture la plus sévère) | La réserve n'est jamais retirée ni remise à un autre seuil ; son taux sous le nul est mesuré avant le scellement, recopié (`<<RAPPORT_RESERVE_INTENTION>>`) et écrit à côté d'elle. Le recalibrage au quantile n'est pas écrit ; je ne le propose pas comme décision (voir section 3). | T-P7, T-V11, T-R34 |
| CR-05, témoin lexical | mineure | acceptée, (a), (b), (c) | (a) Entrées de l'appel au harnais écrites ; contenu sorti et compté si le harnais ne peut pas produire l'indication, règle des 5 %. (b) Garde 20 : appel distinct de celui de la fonction de reconstruction. (c) Ce que g_trahison,lex mesure est écrit. | T-M1, T-M2, T-A3, T-V9 |
| CR-06, garde de l'arbre gelé | mineure | acceptée | « 734 ajoutés, 2 modifiés, aucun supprimé » (recompté par moi : `git diff --name-status 7a54d43 HEAD -- src tests`) ; promesse sur le code des autres préenregistrements retirée (leurs sceaux la portent). | T-A1 |
| CR-07, dépendances de l'adaptateur | mineure | acceptée | Les dépendances de l'adaptateur sont scellées par l'addendum de lancement ; la garde 1 lit les deux jeux de lignes. | T-C1, T-C2, T-A1, T-V3 |
| CR-08, D-19 (a) mécanique | mineure | acceptée | Règle de remplissage écrite : concept = chaîne de la configuration scellée de l'organisme retenu, octet pour octet, sans traduction ; plusieurs ou aucune : nœud ; consignes recopiées du banc. **Deux choses fixées que l'option (a) ne disait pas** : l'abandon du « libellé anglais » et le nœud en cas de chaîne multiple ou absente. | T-M3, T-A4, T-V12, T-C3 |
| CR-09, « n_cal / 2 » | mineure | acceptée | Facteur d'échelle √(n_éval / n), n_éval = nombre de contenus des huit tâches d'évaluation ; au Plan, section 2, et à la précision 30. | T-P2, T-P6, T-R30 |
| CR-10, version (b) et C-P3c | mineure | acceptée en partie | La vérification courte de la session 16 tient lieu de vérification sous (b) seulement à défaut de toute case de C-P3c jouée par le rapport de la grille ; si une case jouée passe le seuil aux deux lectures, C-P3c est « rapportée sans verdict ». Raison : la vérification courte tire les deux gains d'écart comme un bruit indépendant, alors que le point 13 leur fait partager S et D₀ ; on ne peut pas ignorer un rapport qui le montre. Chiffre cité d'après la pièce relue par moi (0,040 à 0,047), non d'après la remarque (« au plus 0,047, seuil 0,0597 »). | T-S1 |

## 2. Contre-lecture du rapport de la grille (ce qui touche le texte)

| Remarque | Gravité | Décision | Ce qui est fait | Lieu |
|---|---|---|---|---|
| CG-01, « grille entière » indécidable | bloquante | acceptée | Liste finie de 144 cases écrite à la clause et dans `liste-finie-cases-grille-v1.md` ; « grille entière » de l'accord se lit : cette liste ; la case d'erreur homogène 0,4 à g = 0,20 y est. Chaque dimension est justifiée par le texte. | T-S1, T-S2, T-V10 |
| CG-02, conclusion de C-P3c et tirages dégénérés | majeure | pour le rapport ; au texte : voir CG-03 | Rien d'autre au texte. La conclusion de C-P3c n'est pas écrite (marqueur). | — |
| CG-03, sort des tirages dégénérés | majeure | acceptée, tranchée par une raison de principe | Précision 37 : la condition s'attache à la grandeur qu'elle rend indéfinie ; Ḡ n'en a pas ; C-P3a et C-P3b toujours lues ; C-P3c « non identifiable » si D₀ manque chez un juge. Conséquences des deux lectures écrites. Point 11 et garde 17 y renvoient. | T-P8, T-R05, T-A2, T-R08 |
| CG-04, formulation trop large | majeure | pour le rapport | Rien au texte ; le texte dit que le partage de S et de D₀ est la définition du point 13 et adopte le modèle du rapport, sans dire « tout modèle ». | T-S2 |
| CG-05, rejeu de deux cases | mineure | acceptée | Règle de lecture (i) : seule la première passe compte ; un rejeu ne lève ni ne crée un dépassement. | T-S2 |
| CG-06, nombre d'essais et seuil | mineure | acceptée | Effectifs fixés par ligne : 1 000 essais et 1 000 tirages pour C-P3a et C-P3b ; 8 000 essais pour C-P3c ; ce sont ceux des programmes figés avant lancement. Multiplicité déclarée (règle (ii)) : la clause penche vers « sans verdict ». | T-S2 |
| CG-07, T = 30 | mineure | acceptée, première voie | T = 30 ajouté à la liste (le plan permet n = 60). | T-S2 |
| CG-08, longueurs des témoins | mineure | acceptée | Configuration citée (`85173b22…`) ; contrôle par programme au scellement ; rejeu si l'appariement diffère, sinon issue 3. | T-S2 |
| CG-09, libellé « erreur sur v₀ seule » | mineure | acceptée | La liste écrit : erreur d'insertion, la même sur v₀ et sur les insertions (s₀ = σ). | T-S2 ; liste, section 2 |
| CG-10, marge faible de C-P3b sous la compression | mineure | acceptée | Liste fermée ; les quatre cases de la contre-lecture sont hors liste, pour information. | T-S2 ; liste, section 3 |
| CG-11, budget de calcul | mineure | sans objet pour le texte | Signalé à la conduite : la liste ajoute 58 et 48 cases à jouer. | — |
| CG-12, mots du mandat et du registre | mineure | acceptée | Le texte suit le registre (« sinon (b) ») et le dit. | T-S1 |
| CG-13, écart 0,186 / 0,227 | mineure | sans objet pour le texte | Aucune de ces lectures n'entre dans un verdict. | — |
| CG-14, C-P3c sans valeur p centrée | mineure | refusée pour cette version | Ajouter un test à C-P3c changerait ce qui compte comme « établie » : nœud, que le contre-lecteur ne recommande pas ; la clause couvre le cas. | — |

Ambiguïtés du rapport de la grille : A1, liste finie ; A2, « aucune attaque » croisée avec les huit modèles ; A3,
erreur d'insertion sous la compression fixée à 0,4, v₀ exact ; A4, profil de g et corpus B écrits ; A5, modèle des
gains d'écart adopté, deux bras dans la liste ; A6, précision 37 ; A7, précision 8 et règle (iv) ; A8, règles (i) et
(ii) ; A9, 1 000 tirages fixés pour la grille (l'analyse réelle en fait 10 000 : non changé, la clause porte sur la
grille) ; A10, configuration citée et contrôle au scellement.

## 3. Ce que la conduite peut requalifier

- **Précision 37.** Je l'ai tranchée comme une précision : la lecture écartée viderait la réfutation de C-P2 et de
  C-P6 (juges), que le texte écrit. Elle fixe pourtant quand C-P3a et C-P3b peuvent être « établies » ; si la
  conduite y voit un changement de ce qui compte, les deux versions sont écrites en entier dans la précision
  (lecture retenue ; « lecture écartée »).
- **R = 8 000 pour C-P3c, R = 1 000 pour C-P3a et C-P3b.** Repris des programmes figés avant lancement, non choisis
  par moi ; le seuil de C-P3c est donc plus serré (0,0549 contre 0,0638).
- **Bras « contenu » dans la liste** et gain du plaidoyer « lié » au g de la case : choix écrits ; le gain « fort »
  (0,30) est laissé hors liste parce que sa valeur ne vient d'aucun passage du texte.
- **Marqueur neuf `<<RAPPORT_RESERVE_INTENTION>>`**, né de CR-04.
