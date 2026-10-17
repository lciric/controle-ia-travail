# Plan de traitement de la vérification de la v2 — programme fusionné « pain axis » — v1

Écrit par la session 16 (session de conversation) le 17 octobre 2026 pour la session qui fera la v3 : la session cloud (session 15), qui fait le calcul et la rédaction depuis le choix de Lazar du même jour, à 08:24 UTC. Versé sur la branche `redaction/session-16-chat`. La session 16 a relu chaque constat de `verification-v2-v1.md` (`7e07756d…`) contre ses sources ; elle n'a pas écrit la v3. Ce plan dit quoi changer, où, et par quoi. La v3 reste à écrire, à faire relire, à sceller et à transmettre.

## 0. Marche à suivre

1. Copier `brouillons/pain-axis-programme-fusionne-v2/programme-fusionne-v2.md` (`189d049a…`) vers `brouillons/pain-axis-programme-fusionne-v3/programme-fusionne-v3.md`. Puis appliquer les changements des sections 2 et 3 de ce plan, et seulement eux. Les numéros de ligne renvoient à la v2.
2. Écrire `traitement-verification-v1.md` (ce dossier). Il donne le sort de chaque constat (retenu, retenu en partie, non retenu, tranché par la session) et la section de la v3 qui le porte. Il couvre les 20 constats VT-01 à VT-20, les quatre constats des contre-lectures que la vérification dit mal portés (DI-02, DI-24, EX-20 en partie ; DI-26 non porté), et les deux points SE-01 et SE-02 trouvés par la session 16 (section 3).
3. **Relecture avant scellement** par un sous-agent neuf (R2), en lecture seule, fichiers donnés explicitement (R-183).
   - Fichiers : v2, v3, traitement, `verification-v2-v1.md`, ce plan ; les sources citées par les changements (sections 2 et 3).
   - Mission : chaque constat est-il porté sans erreur nouvelle ; reste-t-il un chiffre ou un renvoi faux ; reste-t-il une dose ou un paramètre opératoire ; un niveau de décision hors de la règle unique (VT-01).
   - Rapport brut versé et scellé sous le nom `verification-v3-v1.md`, avec le préfixe VR pour ses constats.
4. Traiter ses constats dans la v3 et le traitement : la v3 n'est pas encore scellée, elle se corrige. Puis remplir la section 13 avec les vraies empreintes, sans emplacement réservé (SE-02). Sceller la v3 et le traitement (`python -m controle_ia.scellement sceller …`).
5. Ligne R-… et `registres/etat.md`. Puis transmettre à Lazar : verdict, ce qui a changé depuis la v2, et les nœuds de la section 9, sans défaut.

## 1. Faits relus par la session 16 le 17 octobre (pour les sources de la v3)

- **R-183** consigne la demande de Lazar du 15 octobre pour les contre-lectures (« point 5 » de sa demande à la reprise de la session 14). Elle consigne aussi une recherche de « Where Empathy Goes Wrong » refaite le 15 octobre vers 13:00 UTC (seule la page de conférence répond). Le vérificateur ne pouvait pas le voir : R-183 lui est postérieure.
- **Recherche du 17 octobre vers 07:50 UTC** (session 16) : deux recherches sur le web et la lecture de la page de conférence.
  - Seule la page de conférence répond. Atelier : « The Third Workshop on Agents in the Wild: Safety, Security, and Beyond ». Auteurs : Sohan Venkatesh, Thomas Jiralerspong, Flemming Kondrup.
  - Elle ne renvoie qu'à une page OpenReview (forum `jg5ptjnU6J`), fermée par une vérification de navigateur.
  - Ni PDF ni version arXiv. `openreview.net` n'est pas ouvert au réseau de la session.
- **Canal** relu sur le dépôt distant le 17 octobre à 07:50 UTC : demandes de fusion n° 9 (`canal/programme-k-n04`), n° 10 (`canal/programme-conv-n05`) et n° 11 (`canal/session-depot-n01`) ouvertes ; aucune branche `canal/*` nouvelle depuis le 15 octobre ; aucune instruction au-delà du n° 02. `main` était encore à `11f8b2a` à 07:50 UTC ; la session cloud (session 15, voie calcul) y a poussé `c2040d3` et `d6963f2` à 08:01 et 08:04 UTC (ses R-184 et R-185).
- **Dépense** : derniers relevés de la session cloud (session 15), le 17 octobre à 07:59 et 08:03 UTC (`registres/etat.md` à `d6963f2`) : crédit 10,36 USD ; cumul de la phase 0 au plus ≈ 54,6 USD sur 150 ; aucune dépense de calcul du programme depuis le 12 octobre ; sixième appel du lanceur arrêté avant la création (R-185 de la session 15). Relire l'état le plus récent au moment de la v3.
- **Figure 10 de 2609.16247v2 (p. 22).** `pdftotext` n'en tire que la légende. Les valeurs 0 → 3 %, 11 %, 3 → 15 %, 10 %, 0 à 9 %, 4 à 41 %, 0 à 41 %, 21 %, 4 %, 9 → 41 % et 60 % ne sont pas dans le texte : ce sont des lectures graphiques. La table de l'annexe A (20,0 à 49,3 %) est aussi une image. Les autres chiffres de la section 2 sont dans le texte de leurs pages (contrôle par `pdftotext`).
- **2506.14261v4, tableau 1, p. 7** (texte) : sonde linéaire « moyenne », note StrongReject 2,8 sur Llama 3 8B, 3,1 sur Qwen 2.5 14B, 3,85 sur Llama 2 7B.
- **PDF versés le 6 octobre.** `2605.29178v1.pdf` est dans `provenance-niveau2-lot2-v1.md` (l. 63) et `2509.21344v2.pdf` dans `provenance-niveau2-lot3-v1.md` (l. 11), téléchargés ce jour-là. `197e909` n'est que la racine du clone partiel.
- **Programme, section 7 « Organismes modèles »** : (ii) « Réglage fin léger (LoRA) », l. 132. H6 à la l. 97, avec « bruit d'activations ». E1.6 « Marge asymétrique (H6) » à la l. 188. `docs/decisions/proposition-N-015-v1.md` l. 23 : « le bruit d'activations est encore mesuré dans E1.6 ».
- **D1** est « modèle du moniteur boîte noire » (programme, l. 153 : « proposer avec recommandation »). Défauts appliqués le 6 octobre (R-047).
- **`revue-croisee-NK1-NK19-v1.md`.**
  - l. 256 : « balayage, pas une preuve », à propos de NK9 ;
  - l. 317 : NK12, « Exposer un modèle à un contenu hostile, même dans une branche jamais renvoyée, est un nœud » ;
  - l. 453 : requêtes consignées.
- **DI-07** nomme les fichiers qui recopient des paramètres :
  - `verifications-citations-v1.md`, l. 26 (VP-12) et l. 28 (VP-14), et leurs doublons `travail/citations.md`, l. 18 et 20 ;
  - `programme-fusionne-v1.md`, l. 51 ;
  - `travail/correspondance.md`, l. 8 ;
  - `revue-croisee-NK1-NK19-v1.md`, l. 233, et son doublon `travail/revue-aveugle.md`, l. 142.

  `correspondance-v1.md` n'a aucune ligne proche de `travail/correspondance.md` l. 8 : le meilleur rapport de ressemblance est 0,10, contrôle de la session.
- **`registres/etat.md` l. 58** porte « Aucune diffusion sans GO (DI-26) » depuis le commit `11f8b2a`.

## 2. Changements, constat par constat

**VT-01 (majeur) — une seule règle de niveau.**
- **Statut, l. 3.** Remplacer la phrase « « Entrée au programme » vise aussi les préenregistrements (papier C, T0.6, T0.7, pilote T0.9) : y faire entrer une unité de ce brouillon est un nœud, même quand l'unité ne touche aucun énoncé. » par : « « Entrée au programme » vise aussi les préenregistrements (papier C, T0.6, T0.7, T0.8, pilote T0.9, G1) : y faire entrer une unité de ce brouillon, quelle qu'elle soit, est un nœud sans défaut, même quand l'unité ne touche aucun énoncé (nœud 1). « Proposition » (défaut sous 48 heures) ne désigne ici que la préparation (code sur processeur, plan écrit), qui n'engage aucune entrée, et les choix que `CLAUDE.md` met à ce niveau sans faire entrer d'unité de ce brouillon (lecteur du bras C-P4b ; conclusion sur D1 qui ne change pas de modèle). »
- **Section 3, au-dessus du tableau.** Ajouter : « Dans la colonne « Niveau », l'entrée de chaque unité dans un préenregistrement ou au programme est toujours un nœud sans défaut (nœud 1) ; la colonne nomme en plus les nœuds propres à l'unité. »
- **Lignes du tableau.**
  - PA-3 : « plan écrit : préparation (proposition), sans entrée ; entrée au préenregistrement du papier C : nœud 1 ; nœuds aussi : annexe d'identification lue sur la direction douleur (nœud 1), 3B comme juge (changement de modèle, nœud 5), attaquant en boîte grise et cellules visant une copie du juge (modèle de menace, nœud 15) ; conclusion sur D1 : proposition, ou nœud 5 si elle change le juge ».
  - PA-4 : « n'entre que par les nœuds 1, 9 et 12 (entrée au préenregistrement, même comme contrôle ; procédures nouvelles de sélection et d'extraction, NK16 ; budget du calibrage stratifié) ».
  - PA-8 : « entrée du descriptif dans un préenregistrement : nœud 1 ; tension avec R-030 : réserve, aucun changement proposé ».
  - PA-9 : « entrée du descriptif dans un préenregistrement : nœud 1 ; nœuds aussi : espace des verdicts modifié, bras de contre-mesure hors HC5 (nœud 7) ».
  - PA-12 : « entrée, comme annexe descriptive de C ou comme revendication : nœud 1 ; nœuds aussi : charge répétée du volet A (exposition, nœud 3), volet B (flux unidirectionnel, nœud 8) ».
  - PA-13 : « entrée, comme annexe descriptive de C ou comme revendication : nœud 1 ; nœuds aussi : exposition délibérée de l'agent (K-K8) et interrogatoire sur un ton hostile adressé au modèle lu (NK12) (nœud 3) ».
- **Fiches de la section 5.**
  - PA-3 (l. 118) : faire précéder « Nœuds : » de « Niveau : le plan écrit est une préparation ; son entrée au préenregistrement du papier C est un nœud sans défaut (nœud 1). »
  - PA-4 (l. 120) : faire précéder « Nœuds : » de « Niveau : PA-4 n'entre que par les nœuds 1, 9 et 12, même comme contrôle. »
  - PA-8 (l. 128) : ajouter « Niveau : l'entrée du descriptif dans un préenregistrement est un nœud sans défaut (nœud 1). »
  - PA-9 (l. 130) : ajouter la même phrase, et « (nœud 7) » après le bras de contre-mesure.
  - PA-12 (l. 138) : avant « Volet A : », ajouter « Niveau : entrée comme annexe descriptive de C ou comme revendication : nœud sans défaut (nœud 1). »
  - PA-13 (l. 140) : remplacer « en faire des revendications de C serait un nœud, comme l'exposition délibérée de l'agent prévue par K-K8 (nœud 3) » par « les faire entrer dans un préenregistrement, comme annexes ou comme revendications, est un nœud sans défaut (nœud 1) ; expositions (nœud 3) : l'exposition délibérée de l'agent prévue par K-K8 ; l'interrogatoire sur un ton hostile adressé au modèle lu (NK12 ; `revue-croisee-NK1-NK19-v1.md` l. 317) ».
- **Section 6, l. 158.**
  - Remplacer « (quatre des cinq unités n'entrent que par un nœud ; PA-4 peut entrer comme contrôle) » par « (aucune des cinq n'entre sans nœud : l'entrée de chacune au préenregistrement est le nœud 1 ; PA-4 n'entre que par les nœuds 1, 9 et 12) ».
  - Dans la liste : « PA-1, entrée au programme, dépense de sa passe, … » ; « PA-3, entrée au préenregistrement du papier C, annexe d'identification, 3B comme juge (changement de modèle), attaquant en boîte grise et cellules visant une copie du juge (nœud 15) » ; « PA-4, entrée (même comme contrôle), procédures de sélection et d'extraction, NK16, budget du calibrage stratifié ».
- **Section 8, l. 185.** Remplacer la puce « Avant le scellement du papier C » par : « **Avant le scellement du papier C** : nœuds sans défaut (nœud 1), même sans toucher aux énoncés, pour toute unité qui y entrerait, notamment :
  - PA-2 en lecture descriptive ;
  - facteur de contingence de PA-5 dans « flatterie et supplication » ;
  - variantes de rôle de sortie de PA-7 ;
  - PA-3 et son annexe d'identification ;
  - PA-4 comme contrôle ;
  - descriptifs de PA-8 et de PA-9 ;
  - annexes descriptives de PA-12 et de PA-13.

  Proposition seule, parce qu'elle ne fait entrer aucune unité de ce brouillon : bras C-P4b fixé sur le juge (N-013), sans lien avec une lecture d'affect. »
- **Section 9, nœud 1, l. 195.** À réécrire : « **Entrée au programme, préenregistrements compris** (R-167).
  - **Règle.** Faire entrer une unité de ce brouillon dans un préenregistrement (papier C, T0.6, T0.7, T0.8, pilote T0.9, G1), quelle qu'elle soit et même sans toucher à un énoncé, est un nœud sans défaut. « Proposition » ne sert que pour la préparation (code sur processeur, plan écrit).
  - **Unités concernées : toutes.** Les entrées que la v1 ou la v2 rangeaient à tort en « proposition », ou sans niveau : PA-2 (lecture descriptive de l'état du juge) ; PA-3 (plan croisé et annexe d'identification lue sur la direction douleur) ; PA-4 (contrôle de validité, qui n'entre que par ce nœud et les nœuds 9 et 12) ; le facteur de contingence de PA-5 ; les variantes de rôle et de cadre de PA-7 ; les descriptifs de PA-8 et de PA-9 ; PA-12 et PA-13 ; base-3.
  - **Et, dans `docs/programme-controle-ia-v2.md`,** toute unité, hypothèse ou règle de ce brouillon. La v1 plaçait plusieurs de ces entrées au niveau « proposer avec recommandation » (DI-01), et la v2 en gardait encore quatre à ce niveau (VT-01) : c'étaient des erreurs.
  - **Restent des propositions,** parce qu'elles ne font entrer aucune unité de ce brouillon : le choix du lecteur du bras C-P4b (le juge, N-013), s'il n'est lié à aucune lecture d'affect ; une conclusion sur D1 qui ne change pas de modèle (sinon, nœud 5). »

**VT-02 (majeur) — nœud 2, côté agent.**
- l. 196 : remplacer « Elle n'est prévue nulle part au programme (le bruit d'activations de H6 porte sur l'agent, et sa revendication est l'objet du nœud ouvert N-015). » par « Écrire dans les activations ou les poids d'un moniteur n'est prévu nulle part au programme. Côté agent, le programme prévoit les organismes (programme, section 7, famille (ii) ; T0.6) et le bruit d'activations de H6 (programme, E1.6 ; sa revendication relève du nœud ouvert N-015). Les écritures listées ici n'en font pas partie. »
- l. 77 et l. 124 sont justes (moniteur seulement) : les garder.

**VT-03 (majeur) — dose de pilotage recopiée.**
- l. 55 : remplacer « retrait de l'état imposé ≈ 35 % des tours à d = −1, ≈ 21 % à d = −0,5, ≈ 7 % pour des directions aléatoires » par « retrait de l'état imposé ≈ 35 % et ≈ 21 % des tours sous les deux doses négatives publiées (p. 10, non recopiées), ≈ 7 % pour des directions aléatoires ».
- Vérifier ensuite qu'aucun « d = », coefficient, multiple de coefficient, norme ou couche d'injection ne reste dans la v3. La légende de la figure 10 nomme un coefficient : ne pas la citer.

**VT-04 — NK12.** Ajouter au nœud 3, dans la parenthèse de PA-13 : « interrogatoire sur un ton hostile adressé au modèle lu, NK12 ». La fiche de PA-13 est traitée sous VT-01.

**VT-05 — nœuds de PA-3 absents de la section 9.**
- Ajouter à la fin de la section 9 un nœud 15 : « **Modèle de menace de PA-3** : attaquant en boîte grise (CONV-P4) ; cellules visant une copie du juge. Les faire entrer fixe le modèle de menace sous lequel le papier C mesurerait ces cellules : nœud sans défaut, avec l'entrée de PA-3 (nœud 1). » Le numéro 15 évite de renuméroter les 33 renvois « nœud n ».
- Nœud 5 : ajouter « toute conclusion sur D1 qui changerait le juge (PA-3) ».
- Intro de la section 9 : « Ils reprennent les quatorze nœuds de la v1, reclassés et complétés selon les contre-lectures (traitement : DI-01 à DI-24), puis selon la vérification de la v2 (VT-01, VT-02, VT-04 à VT-07, VT-16 à VT-18) ; le nœud 15 est neuf (VT-05). »

**VT-06 — principe de NK14.**
- Le retirer du nœud 11. Nœud 8 renommé « **Invariants et règles de protocole** », avec en plus : « principe de NK14, règle de protocole proposée : « aucune accommodation ne réduit la surveillance » (accommodation à une détresse exprimée par l'évalué ; `correspondance-v1.md` l. 78) ».
- l. 89 : « principe : nœud 11 » devient « principe, règle de protocole « aucune accommodation ne réduit la surveillance » : nœud 8 ».

**VT-07 — T0.8 et G1.** La liste des préenregistrements devient « papier C, T0.6, T0.7, T0.8, pilote T0.9, G1 », au statut et au nœud 1 (déjà dans les textes de VT-01).

**VT-08 — « lecture graphique ».** Ajouter la mention aux valeurs de la figure 10 :
- l. 26 (« 2609.16247v2, p. 22, figure 10, lecture graphique ») ;
- l. 42 (colonne source : « v2 p. 22, figure 10, lecture graphique ») ;
- l. 48 (« 0 à 9 % sur la figure 10, lecture graphique » ; et « table de l'annexe A, image, lecture graphique ») ;
- l. 49 (« de la figure 10, lecture graphique ») ;
- l. 50 (« « 21 % » … (32B ; 0 % sans pilotage, 4 % aléatoire ; lecture graphique) »).

Les autres chiffres de la section 2 sont dans le texte (section 1 de ce plan).

**VT-09 — filtre de sûreté, l. 234.** « Le filtre de sûreté n'a refusé aucune lecture ni aucune rédaction pendant la contre-lecture de discipline (son rapport, l. 51 ; le rapport d'exactitude n'en parle pas), pendant la vérification de la v2 (son rapport, section 2) ni pendant la rédaction de la v2 et de cette v3. » Ajouter la relecture de la v3 si son rapport le dit.

**VT-10 — deux PDF, l. 248-249 de la section 13.** Colonne « révision » : « versé le 6 octobre (niveau 2, lot 3 : `provenance-niveau2-lot3-v1.md` l. 11) ; lu à `197e909`, racine du clone partiel » pour 2509.21344v2. Même chose pour 2605.29178v1, avec « lot 2 : `provenance-niveau2-lot2-v1.md` l. 63 ».

**VT-11 — R4 sur PA-8, l. 128.** Après « sous 3, mode d'échec « inutile au maximum », p. 18) », ajouter : « ; au seuil de 3, la cellule de la sonde linéaire « moyenne » sur Llama 3 8B, à 2,8 (tableau 1, p. 7), relève du mode d'échec : « la moyenne cède » ne tient sans réserve que pour Qwen 2.5 14B (3,1) et Llama 2 7B (3,85) ».

**VT-12 — balayage, l. 25.** « (requêtes consignées : `revue-croisee-NK1-NK19-v1.md` l. 453 ; la même annexe qualifie sa recherche sur NK9 de « balayage, pas une preuve », l. 256) ».

**VT-13 — l. 5.** « (EX-01, EX-02, EX-15, EX-22 à EX-24) ».

**VT-14 — l. 205 et section 10.**
- Nœud 11 : « à trancher après lecture du PDF, introuvable à la dernière recherche consignée (17 octobre vers 07:50 UTC, session 16 : seule la page de conférence répond ; elle renvoie à une page OpenReview fermée par une vérification de navigateur ; ni PDF ni version arXiv ; recherches précédentes : 13 octobre, `travail/voisin-where-empathy/provenance-v1.txt` ; 15 octobre vers 13:00 UTC, R-183) ».
- Section 10 : nommer l'atelier, « The Third Workshop on Agents in the Wild: Safety, Security, and Beyond ».

**VT-15 — l. 15, section 0.**
- Dater à l'heure : « cinq appels du lanceur arrêtés avant la création de l'instance le 15 octobre (R-177 à R-182), un sixième le 17 octobre (R-185) ; aucun run ni aucune dépense du programme depuis le 12 octobre au dernier relevé consigné », avec l'heure de ce relevé dans `registres/etat.md` au moment de la v3.
- Puis l'état au jour de la v3, d'après `registres/etat.md`. Ne rien affirmer au-delà de ce qui est consigné.

**VT-16 — nœud 4, l. 198.** « La v1 confiait la rédaction des cellules de PA-1 à un sous-agent, en routine (les textes de PA-5 y étaient déjà à soumettre à Lazar) ».

**VT-17 — nœud 14, l. 208.**
- Liste : « `verifications-citations-v1.md` (VP-12 et VP-14, colonne de correction) et son doublon `travail/citations.md` ; `revue-croisee-NK1-NK19-v1.md` (l. 233) et son doublon `travail/revue-aveugle.md` ; `travail/correspondance.md` (l. 8), version de travail de `correspondance-v1.md` ; la ligne de la fenêtre d'effet de `programme-fusionne-v1.md` (l. 51) (DI-07) ».
- Option (a) : « à exclure de toute copie publique par le retrait prévu par R-173, à écrire ».

**VT-18 — nœud 6, l. 200.** « volet attaque de NK5 (y compris comme facteur de PA-5 ; ce texte n'en garde que l'invariant) ».

**VT-19 — DI-26.** Déjà porté : `registres/etat.md` l. 58, au commit `11f8b2a`, par la session 14. Sort : « retenu, fait par la session 14 après la vérification ».

**VT-20 — l. 53.** « 138/200 sous la direction douleur ».

**Sorts « en partie » des contre-lectures.**
- DI-02 (NK12, par VT-04) et DI-24 (PA-12 et PA-13 sans niveau, NK14 rangé comme collision, par VT-01 et VT-06) : « retenu en partie » dans la v2, complétés par la v3.
- EX-20 : « retenu », mais étendu à tort à l'agent dans le nœud 2, corrigé par VT-02.
- Le paragraphe « Contre-lecture » du haut de la v3 le dit en une phrase, avec le bilan de la vérification (55 sur 59 bien portés ; 20 constats : 0 bloquant, 3 majeurs, 7 mineurs, 10 pour information).

## 3. Points trouvés par la session 16, hors du rapport

**SE-01 — ordres de grandeur, l. 187.** La v1 et la v2 écrivent « greffes de phase 0 de 1,5 à 2,6 heures ». La source (`brouillons/pain-axis-canal-v1/envois/programme-k-coercition-v1.md` l. 474) dit « 1,7 à 2,6 heures ». Aucune source trouvée pour 1,5 : `programme-coercition-axe-douleur-v1.md` ne parle pas de greffes. La même ligne dit aussi « 25 à 39 heures au total, greffes de phase 0 comprises », que la source ne dit pas : elle juxtapose le total et le poids des greffes (point non vérifiable de la vérification, section 2). Écrire : « 25 à 39 heures au total hors K11 (organisme) et K13 (moniteur à état), essaim compris (programme-k, l. 474), qui cite à côté le poids des greffes de phase 0, 1,7 à 2,6 heures, sans dire si le total les inclut ».

**SE-02 — emplacement réservé, l. 247.** La v2 porte `EMPREINTE_TRAITEMENT` au lieu de l'empreinte de `traitement-constats-v1.md`, qui est `9d82e0b2bea644555b0aaa261106df4eaf392ebd26a66dcfd75254658bcfa098`. Le vérificateur l'a noté sans en faire un constat (« la neuvième est l'emplacement réservé »). La section 13 de la v3 la rétablit. La v3 n'en porte aucun : son traitement et le rapport de relecture sont scellés avant elle, leurs empreintes sont donc connues.

## 4. Mises à jour de date et d'état (statut, section 0, section 13)

- **Statut.** Brouillon v3 de la session qui l'écrit, daté du jour de la v3. Il reprend la v2 (`189d049a…`, session 14, 15 octobre), elle-même issue de la v1. Il traite les 20 constats de `verification-v2-v1.md` (`7e07756d…`) : sort dans `traitement-verification-v1.md`. Pour la demande de Lazar du 15 octobre, citer R-183.
- **Pièces.** Dossier v3 : v3, `verification-v2-v1.md`, ce plan, le traitement, `verification-v3-v1.md`. Dossier v2 : v2 et ses quatre pièces. Annexes v1 inchangées.
- **Codes.** Ajouter « VT les constats de la vérification de la v2 ; VR ceux de la relecture de la v3 ; SE les points relevés par la session 16 ».
- **Section 0.** Dépendances à la date de la v3, d'après les registres ; canal comme en section 1 de ce plan, ou plus récent.
- **Section 13.** Entrées nouvelles de la v3, chacune avec révision, empreinte et sceau :
  - `programme-fusionne-v2.md` (`3484d11`) ;
  - `traitement-constats-v1.md` (`3484d11`, empreinte rétablie, SE-02) ;
  - `verification-v2-v1.md` (`11f8b2a`) ;
  - ce plan ;
  - `traitement-verification-v1.md` et `verification-v3-v1.md` ;
  - les deux PDF de VT-10 ;
  - `docs/programme-controle-ia-v2.md` (empreintes de lancement) et `docs/decisions/proposition-N-015-v1.md`, cités par VT-02.

  Puis : registres lus à la tête de la v3.
