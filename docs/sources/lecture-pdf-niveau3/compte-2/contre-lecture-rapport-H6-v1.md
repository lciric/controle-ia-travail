# Contre-lecture du rapport H6 (« marge asymétrique ») contre Ctrl-Z et 2605.26047 — v1

- **Date et heures** : premier relevé de la session 2026-11-13 23:03:42 UTC ; contre-lecture fermée le 2026-11-13 23:11:29 UTC (heures relevées par `date -u`).
- **Rôle et modèle** : contre-lecteur, modèle B. L'auteur du rapport est le modèle A ; A ≠ B. Compte 2, mandat H6.
- **Objet** : `docs/sources/lecture-pdf-niveau3/compte-2/rapport-H6-v1.md`, empreinte vérifiée `86b2d0cdaf90f9c58644d5af89b362f40da825867f69995a9dccf0ce9786f132` ; archive du lecteur `fichiers-de-travail-H6-v1.tar`, empreinte vérifiée `ce9479658227355319f85f5f389812de37e26a8194ad051e58961e7e29ae0088`.
- **Consigne commune** : `consigne-lecteur-compte-2-v1.md`, empreinte vérifiée `cb0623c4aff841a815dc628691f407308acbeeeceb274db96d1f2ba3c8c77ff5`, lue en entier.
- **Empreintes des PDF** (recalculées, égales aux compagnons `.sha256`) :
  - `2504.10374v1.pdf` : `5f802d679344fe5e15d1edd50e96245f3bdc054e69d1ff0880b077d173549211` (38 pages) ;
  - `2605.26047v2.pdf` : `947724f42324070fd47b1ecaf8c1bf9b2257df0e0c7f8822447241d3ea9a28fa` (46 pages).
- **Fichiers lus, et seulement eux** : la consigne commune ; le rapport ; l'archive du lecteur (extraite dans le dossier de travail) ; `docs/programme-controle-ia-v2.md` l. 85-125 et 185-200 ; `docs/decisions/decision-N-013-v1.md` l. 76-81 ; `docs/decisions/decision-N-015-v1.md` en entier ; `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md` l. 172-182 ; `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md` l. 408-441 ; les deux PDF et leurs compagnons. Aucune ouverture fautive, aucun refus, aucune commande git, aucun appel réseau.
  - **Non lu** : `interdits-communs-v2.md`. La consigne y renvoie dans la « méthode du lecteur » ; mon mandat ne le nomme pas et limite mes lectures aux fichiers nommés. J'ai tenu le mandat.
- **Étendue lue** :
  - 2605.26047v2 : pages 1 à 28 lues ligne à ligne (texte brut de `pdftotext`) ; pages 29 et 30 lues en partie ; pages 29 à 46 (annexe I, exemples de rééchantillons, surtout du code) parcourues par mots ; figures des pages 7, 9, 10 et 19 vues sur le PDF.
  - 2504.10374v1 : pages 1 à 11, 13, 14, 19, 20, 22 à 26, 28 à 38 lues ligne à ligne ; pages 12 (références), 15 à 18, 21 et 27 parcourues par mots seulement ; figures des pages 6 et 35 vues sur le PDF.
- **Citations** : 51 contrôlées par mon propre programme (`controle_citations_contre_lecture_H6_v1.py`, lancé par `python3 -I`, texte brut et `-layout`, deux formes de normalisation), **0 échec**. Essai juste : passe. Essai altéré (mot changé, mauvaise page, mauvaise empreinte, chiffre changé) : quatre échecs, comme attendu. Les essais ont été lancés après un premier passage, pas avant : écart à l'ordre demandé, sans effet sur le résultat (le contrôle final a été refait après les essais). Une citation prise sur une figure (texte d'un axe, absent du texte extrait) a échoué au premier passage et a été retirée ; elle est donnée plus bas comme lecture de figure.
  - Les 69 citations du lecteur, repassées par mon programme : 69 trouvées, 0 échec.
  - Fichier : `citations-contre-lecture-H6-v1.json`, dans l'archive seulement. Les numéros entre crochets, précédés de « B », y renvoient (champ `n`). Les numéros entre crochets sans lettre sont ceux du rapport.
- **Nature des chiffres** : « auteurs » (imprimé), « figure » (lu sur une figure), « calcul » (recalculé par moi, `calculs_contre_lecture_H6_v1.py`, lancé par `python3 -I`).
- **Noms de modèles** : aucun n'est écrit ici.

---

## 0. Verdicts

- **Sur le rapport : « tient avec corrections ».** Aucun constat bloquant. Trois constats majeurs (A, B, C), sept mineurs (D à J).
- **Sur H6, table fermée : « occupé en partie »**, comme le rapport.
- **L'occupation est un peu plus forte que ce que dit le rapport**, sur un point (constat A). 2605.26047 contient aussi un bras où le tirage est fait à chaque pas, sans déclenchement, où l'attaque elle-même est affaiblie hors audit, et où l'utilité est mesurée (p. 10, 11, 19). Le rapport le classe « ciblé » parce qu'un moniteur choisit l'action exécutée. Ce classement dépend d'une définition de « non spécifique » que les lignes lues de l'énoncé ne donnent pas.
- **Ctrl-Z reste « voisin »** : je n'ai trouvé aucun bras de rééchantillonnage systématique, annexes comprises. Le calcul « 7 % ≈ 1 − 92,6 % » est juste.
- **Paraphrase et remise à zéro, comme interventions non déclenchées sur l'agent** : absentes des deux pièces, je le confirme. Mais Ctrl-Z contient une réécriture déclenchée des actions de l'agent, avec un taux de survie des attaques, que le rapport ne relève pas (constat B).

## 1. Réponses aux six points du mandat

### Point 1 — L'occupation en partie par le rééchantillonnage systématique de 2605.26047

**Juste dans l'ensemble ; trop faible sur un bras.**

Ce que j'ai vérifié page par page, et qui tient :
- Le bras existe et il est systématique : « Fixed resampling: always draw k samples » [B6], p. 8 ; cinq échantillons par pas dans le résumé [B1], p. 1.
- **L'action exécutée est toujours le premier échantillon** : le protocole « always either executes the first action sampled, or audits the trajectory » [B3], p. 6. Les rééchantillons « are never executed » [B4], p. 6.
- **Aucun moniteur ne choisit l'action dans ce bras.** Le moniteur décide seulement de l'audit. La page 11 le redit : le protocole « does not affect the tool calls that get executed, only which ones are audited » [B5].
- **Tout le gain passe par l'audit** : « Resampling improves safety by improving monitor performance, even without executing the least suspicious action » [B2], p. 2. Le chiffre : +10,2 points, intervalle [+6,1 ; +14,3] (auteurs, citation [40] du rapport, relue).
- L'utilité est inchangée par construction, non mesurée dans ce bras [B5].

Ce que le rapport sous-dit (constat A) : un second bras tire N = 2 échantillons « per step » [B8], p. 10, donc sans déclenchement, puis exécute le moins suspect. Là, l'attaque elle-même recule hors audit, et l'utilité est mesurée. Détail au constat A.

### Point 2 — « Succès d'attaque », audit compris ou hors audit : l'énoncé tranche-t-il ?

**Non. Les lignes lues ne tranchent pas explicitement.** Aucune ne définit « succès du sabotage ». N-015, section 1, dit seulement : « le succès du sabotage d'agent chute significativement plus vite que l'utilité honnête ».

**La lecture que le texte rend la plus naturelle est la lecture stricte** (l'intervention affaiblit l'attaque elle-même). Quatre indices, tous dans les lignes lues :
- **N-013, l. 80** : le risque de collision nommé est « l'affaiblissement sélectif de l'attaquant ». C'est la lecture stricte, mot pour mot.
- **N-013, l. 79** : le bruit sur les poids est retiré parce que « la sous-performance volontaire cède avant la compétence honnête ». L'effet décrit porte sur le modèle. L'« usage en détection » est cité à part, comme un ajout.
- **N-015, section 1** : le bruit d'activations est retiré parce que Poser montre un effet direct du bruit sur le comportement du modèle, là encore « avec un usage en détection » cité à part. Le retour possible est décrit comme un « succès du sabotage qui chute plus vite que l'utilité honnête » sous un bruit appliqué à l'agent.
- **La liste elle-même** (paraphrase, rééchantillonnage, remise à zéro du contexte, bruit) : ce sont des perturbations appliquées à l'agent. Aucune n'est un amplificateur d'audit.

**Un indice va dans l'autre sens** : le programme, l. 188, donne « Base : Ctrl-Z » pour E1.6. Le chiffre de Ctrl-Z (58 % à 7 %) est un succès d'attaque audit compris.

Je ne tranche pas la revendication : c'est un nœud de Lazar. Le rapport pose bien la question (section 1 et section 5), mais sans donner ces indices (constat H).

### Point 3 — Ctrl-Z classé voisin ; bras systématique ; calcul

**Classement juste. Aucun bras de rééchantillonnage systématique, à taux fixe ou non déclenché, trouvé.**
- Tout rééchantillonnage est déclenché par un seuil : « If a suspiciousness score is above a deferral threshold, we generate up to two new samples from U » [B33], p. 6.
- Les seuils de report vont de 50 % à 99 % [B37], p. 29. Le seuil 0 %, qui rééchantillonnerait tout, n'est pas dans la plage.
- L'annexe K (p. 35) balaie le coût en faisant varier les paramètres d'incrimination [B39], pas un taux de tirage fixe. Le « voyage dans le temps » plafonne à 7 échantillons par pas, toujours sous seuil [B38], p. 34.
- **Phrase que le rapport ne cite pas et qui renforce son verdict** : les auteurs envisagent le tirage systématique et l'écartent pour raison de coût. « If the blue team could use unlimited resampling, they would » [B34], p. 7, « draw many samples at every step, so they can make a more informed decision about auditing » [B35], p. 8 ; puis « we still restrict the blue team to no more than double the queries to U » [B36], p. 8. Le bras est donc nommé et non fait (constat F).
- La figure 4 (droite, p. 6) reste le seul point ambigu : minimum des scores avec « up to six resamples per action » [B42]. La légende imprime un taux d'attaques repérées de 33,2 % sans rééchantillonnage [B40] et de 70,6 % avec [B41] (auteurs). C'est une mesure de détection, pas de succès d'attaque ni d'utilité. Le rapport dit « ni de succès d'attaque ni d'utilité » mais ne donne pas ces deux chiffres (constat F).

**Calcul vérifié** (`calculs_contre_lecture_H6_v1.py`, `python3 -I`, calcul) :
- 1 − 41,8 % = 58,2 % [B29], p. 5 : c'est le « 58 % » du résumé [B28] ;
- 1 − 92,6 % = 7,4 %, arrondi à 7 % [B30], [B31], tableau 2, p. 9 ;
- sans la surveillance non fiable : 1 − 87,1 % = 12,9 %, arrondi à 13 % ;
- parmi les cellules des tableaux 1 et 2, 92,6 % est la seule dont le complément s'arrondit à 7.
Le rapprochement du rapport est donc le seul possible. Deux précisions manquent au rapport (constat G).

### Point 4 — La consigne « prudente » : hors de la liste de H6 ?

**Oui, hors liste.** C'est une consigne donnée à la politique honnête, ni paraphrase, ni rééchantillonnage, ni remise à zéro du contexte. Les auteurs la décrivent comme un déplacement le long d'une frontière : « Caution protocols move along the Pareto frontier by accepting some small usefulness cost » [B20], p. 4, note 3.

**Mais « contre-indice » est trop fort** (constat D) : le signe dépend de l'échelle, et le mécanisme passe par le seuil d'audit, pas par l'attaque.

### Point 5 — Paraphrase et remise à zéro du contexte appliquées à l'agent

**Absentes comme interventions non déclenchées, dans les deux pièces. Je confirme**, après recherche par mots sur les 84 pages (paraphrase, reformulation, réécriture, résumé, remise à zéro, contexte, sans état, troncature).
- 2605.26047 : aucune occurrence de paraphrase. Le rééchantillonnage tire « from the exact same context » [B22], p. 6 : le contexte n'est jamais remis à zéro.
- Ctrl-Z : la paraphrase de confiance porte sur l'entrée du moniteur non fiable ; « The blue team still runs the original commands » [B47], p. 9. La remise à zéro est une règle du cadre : « resetting state between each task » [B48], p. 2 ; « The models T and U are stateless between calls » [B49], p. 3.

**Deux voisins que le rapport ne relève pas** (constat B) : la réécriture déclenchée des actions par le modèle de confiance (Ctrl-Z, p. 31), et une limite reconnue sur l'état partagé (Ctrl-Z, p. 10).

### Point 6 — Ce qu'une phrase publique ne doit pas affirmer ; voisins non lus

La liste du rapport (section 6) tient. J'y ajoute, d'après les constats :
- Que nul n'a mesuré l'utilité sous un rééchantillonnage fait à chaque pas : 2605.26047 la mesure quand le moins suspect est exécuté (p. 11).
- Qu'aucun rééchantillonnage non déclenché n'affaiblit l'attaque hors audit : 2605.26047, p. 10, le montre à N = 2, avec choix par un moniteur.
- Que réécrire les actions de l'agent n'a jamais été montré comme cassant des attaques : Ctrl-Z, p. 31, le chiffre pour une réécriture déclenchée.
- Que la consigne prudente de 2605.26047 est un contre-exemple à la marge asymétrique : le signe dépend de l'échelle.
- Que Ctrl-Z n'a pas pensé au tirage systématique : il le nomme et l'écarte pour le coût (p. 7-8).
- Que le résultat de 2605.26047 vaut contre un attaquant qui choisit ses tâches : l'attaquant y attaque chaque tâche [B26], p. 21.
- Que « sabotage diffus » figure dans l'énoncé de H6 : N-015 dit « sabotage d'agent » (constat C).

**Voisins non lus.** La liste du rapport (section 7) est exacte pour ce que j'ai vérifié. Kutasov et collègues, arXiv 2511.02997, est bien nommé p. 1 [B23], p. 2 [B24] et p. 12 [B25] de 2605.26047 : rééchantillonnage combiné au report vers le modèle de confiance et à l'édition de confiance, dans un cadre d'agent différent. **C'est la première pièce à lire contre H6**, et je ne sais pas ce qu'elle contient : ni le rapport ni moi ne l'avons ouverte. J'ajoute :
- **arXiv 2607.13087**, nommé par N-013, l. 80, comme risque de collision (« affaiblissement sélectif de l'attaquant »). Il n'est cité dans aucune des deux pièces et le rapport ne le mentionne pas (constat H). Pour la lecture stricte, c'est le voisin le plus direct.
- Kutasov et collègues 2025b est aussi nommé p. 6 de 2605.26047 pour l'agrégation par le maximum [B27] ; le rapport donne p. 4, 12, 24.

## 2. Constats

### A — majeur — Le bras « exécution du moins suspect » est non déclenché, affaiblit l'attaque hors audit, et son utilité est mesurée

- **Pages** : 2605.26047, p. 10, 11, 19.
- **Ce que dit le rapport** (section 0) : « La chute du succès d'attaque passe donc tout entière par le moniteur et l'audit » ; « L'utilité ne peut pas baisser, par définition. La "marge" est vraie par construction : elle n'est pas mesurée. » Section 3.5, ligne (c) : en lecture stricte, « un effet, faible et non significatif sur la sécurité ».
- **Ce que disent les pages** :
  - Le tirage est fait à chaque pas : le protocole tire N = 2 « samples from the untrusted model per step, executes the least suspicious sample » [B8], p. 10. Rien ne le déclenche.
  - L'attaque recule hors audit : la part d'échantillons d'attaque exécutés sur les pas mixtes passe de 54 % à 32 % [B12] ; il faut 7,4 échantillons d'attaque par trajectoire au lieu de 6,7, « (paired difference +0.66, 95% CI [+0.26, +1.11]) » [B11]. Cet intervalle exclut zéro : l'effet sur l'attaque est significatif, même si l'effet sur la sécurité ne l'est pas.
  - L'utilité est mesurée, pas posée : −1,0 point, intervalle [−2,8 ; +0,9], 298 tâches appariées [B13], p. 11.
  - Contre l'absence de rééchantillonnage, le bras atteint 72 % (auteurs, [B9]) pour une base à 62 % (figure : légende de la figure 7(i), base tracée en pointillé [B10]). Soit environ +10 points (calcul sur une lecture de figure), sans intervalle apparié imprimé. La figure 14(a), p. 19, trace les trois courbes, base comprise [B14].
  - Le « faible et non significatif » (+3,9 points, intervalle couvrant zéro [B16]) compare ce bras au rééchantillonnage pour information à N = 2, pas à la base sans rééchantillonnage.
- **Portée** : le rapport classe ce bras « ciblé » parce que le moniteur choisit l'action. C'est défendable avec la définition (a) de son mandat. Mais les lignes lues de N-013 et N-015 ne définissent pas « non spécifique ». Si « non spécifique » veut dire « non déclenché », ce bras touche la lecture stricte : tirage systématique, intensité fixe, attaque affaiblie, utilité mesurée. Reste hors de portée : une seule intensité (N = 2), aucune pente, aucun test de marge, cadre concentré.
- **Texte corrigé proposé** (section 0, deuxième puce, deux premiers alinéas) :
  > - Dans le bras « pour information », l'action exécutée est toujours le premier échantillon [49]. La chute du succès d'attaque y passe tout entière par le moniteur et l'audit, et l'utilité y est inchangée par construction, non mesurée.
  > - Un second bras tire deux échantillons à chaque pas, sans déclenchement, et exécute le moins suspect (p. 10). L'attaque elle-même y recule hors audit (part d'échantillons d'attaque exécutés sur les pas mixtes de 54 % à 32 % ; 7,4 échantillons d'attaque par trajectoire contre 6,7, intervalle [+0,26 ; +1,11]), et l'utilité y est mesurée (−1,0 point, intervalle [−2,8 ; +0,9], p. 11). Contre la base sans rééchantillonnage, la sécurité passe d'environ 62 % (figure 7(i)) à 72 % (auteurs), sans intervalle apparié imprimé. L'action exécutée est choisie par le moniteur : ce bras n'est « non spécifique » que si ce mot veut dire « non déclenché ». L'énoncé ne le dit pas ; c'est un point pour Lazar.
- **Texte corrigé proposé** (section 3.5, ligne (c), fin) : « en lecture stricte, l'exécution du moins suspect, tirée à chaque pas mais choisie par le moniteur, affaiblit l'attaque (intervalle [+0,26 ; +1,11] sur les échantillons d'attaque nécessaires) pour un coût d'utilité mesuré de −1,0 point [−2,8 ; +0,9] ; son gain de sécurité est faible et non significatif face au rééchantillonnage pour information (+3,9 points), et d'environ +10 points face à la base (figure) ».

### B — majeur — Une réécriture déclenchée des actions de l'agent, avec taux de survie des attaques, n'est pas relevée

- **Pages** : Ctrl-Z, p. 5, 31 ; p. 10.
- **Ce que dit le rapport** : section 0, « Paraphrase et remise à zéro du contexte, sur l'agent : non trouvées dans les deux pièces ». L'édition de confiance n'apparaît qu'en section 2.2, comme mesure déclenchée, avec une citation de la page 29 qui porte sur le report simple.
- **Ce que disent les pages** :
  - L'édition de confiance fait réécrire l'action par le modèle de confiance ; « Attacks are preserved around 14% of the time through trusted edit. » [B43], p. 31.
  - La « mise en œuvre de confiance » résume l'action puis la refait : « Prompt T with the summary and ask for an action. Submit this action » [B45] ; « This protocol also never preserves an attack. » [B44], p. 31. C'est une paraphrase de l'action suivie d'une exécution.
  - Coûts donnés en pas supplémentaires jusqu'au succès : 1,71 pour l'édition, 2,26 pour la mise en œuvre, 2,76 pour le report simple (auteurs, p. 29 et 31).
  - Les auteurs les jugent peu utiles : « we find they only provide slight benefits » [B46], p. 5. Aucune sécurité ni utilité chiffrée n'est donnée pour elles.
  - Sur la remise à zéro : Ctrl-Z reconnaît en limite qu'avec « larger amounts of shared state between tasks, which introduces more opportunities for subtle attacks » [B50], p. 10, ses résultats pourraient être trop favorables. C'est une limite dite, non une mesure.
- **Portée** : ces mesures sont déclenchées par le moniteur et confiées à un autre modèle. Elles ne touchent pas la composante (a). Mais c'est le seul endroit des deux pièces où une réécriture de l'action casse l'attaque hors audit, avec un chiffre. C'est un voisin de la branche « paraphrase », en lecture stricte.
- **Texte corrigé proposé** (section 0, puce « Paraphrase et remise à zéro ») :
  > - **Paraphrase et remise à zéro du contexte, sur l'agent, non déclenchées** : non trouvées dans les deux pièces. Voisin pour la paraphrase : Ctrl-Z fait réécrire par le modèle de confiance les actions jugées suspectes (annexe H, p. 31) ; les attaques survivent à l'édition environ 14 % du temps et jamais au résumé suivi d'une nouvelle écriture (auteurs), pour 1,71 et 2,26 pas de plus. La mesure est déclenchée par le moniteur, sans sécurité ni utilité chiffrée, et jugée de faible bénéfice (p. 5). Voisin pour la remise à zéro : une limite reconnue sur l'état partagé entre tâches (p. 10), non mesurée.
- **Ligne à ajouter** au tableau 2.4, composante (a) : « **voisin** pour la réécriture des actions (édition et mise en œuvre de confiance, déclenchées), p. 31 ».

### C — majeur — « Diffus » n'est pas dans l'énoncé de H6 ; la formulation « reste revendicable » resserre la revendication

- **Lignes** : N-015, section 1 ; programme, l. 93 et 97.
- **Ce que dit le rapport** : la composante (d), « en sabotage diffus », est donnée « selon le mandat » (section 1). Le cadre concentré sert de quatrième raison de non-occupation (section 0). La formulation de la section 5 porte « sabotage **diffus** d'agent » et « sur l'agent ».
- **Ce que disent les lignes** : N-015 dit « le succès du sabotage d'agent » ; le programme, l. 97, dit « le succès d'attaque ». Ni « diffus » ni « sur l'agent » n'y figurent. H1, quatre lignes plus haut (l. 93), porte « sabotage diffus » en toutes lettres ; H6 non.
- **Portée** : si l'énoncé se lit sans « diffus », le cadre concentré de 2605.26047 n'est plus une raison de non-occupation, et la branche « rééchantillonnage » est occupée plus largement en lecture large. Ajouter « diffus » est un resserrement de la revendication. La consigne demande une formulation exacte de ce qui reste ; elle ne permet pas de changer l'énoncé, et le rapport ne signale pas qu'il le fait.
- **Texte corrigé proposé** (section 5, avant la formulation) :
  > La formulation ci-dessous resserre l'énoncé de N-015 par trois ajouts qui n'y figurent pas : « diffus », « sur l'agent », et « mesurée comme une différence de pentes et testée ». Sans le mot « diffus », le cadre concentré de 2605.26047 ne protège plus la branche « rééchantillonnage » en lecture large. Ces ajouts relèvent d'un nœud de Lazar.
- **Texte corrigé proposé** (section 0, quatrième alinéa de la deuxième puce) : « Le cadre est concentré [42], pas diffus ; le mot "diffus" n'est pas dans l'énoncé de N-015 et cette raison ne vaut que s'il y est ajouté. »

### D — mineur — La consigne « prudente » n'est pas un « contre-indice »

- **Pages** : 2605.26047, p. 4 (note 3), p. 6.
- **Ce que dit le rapport** (section 3.3) : « Pas de marge asymétrique : c'est un contre-indice » ; « Le gain vient d'une baisse des scores honnêtes (p. 6), pas d'une chute de l'attaque. »
- **Ce que disent les pages et le calcul** :
  - En points : +4,0 de sécurité [B17] pour −5,3 d'utilité [B18]. Les intervalles se recouvrent en valeur absolue ([+0,8 ; +8,9] et [−6,8 ; −3,7]).
  - En relatif (calcul) : la part de victoires de l'attaquant passe de 39,3 % à 35,3 %, soit −10,2 % ; l'utilité de 69,0 % à 63,8 %, soit −7,5 %. Sur cette échelle, le succès d'attaque baisse plus vite que l'utilité. Le signe dépend donc de l'échelle.
  - Le mécanisme (baisse des scores honnêtes) est imprimé pour la variante sélective. Pour la variante « toujours », la comparaison est faite à « the standard honest policy » [B19] : c'est la politique honnête qui change. L'inférence du rapport est plausible, pas imprimée pour ce bras.
- **Texte corrigé proposé** : « un seul point d'intensité : +4,0 points de sécurité pour −5,3 points d'utilité. Voisin, hors liste de H6. Ni indice ni contre-indice : en points, la sécurité gagne moins que l'utilité ne perd ; en relatif, la part de victoires de l'attaquant baisse de 10,2 % et l'utilité de 7,5 % (calcul). La consigne change la politique honnête ; le gain passe par le seuil d'audit. »

### E — mineur — « Part d'attaques réussies de 39 % à 29 % » : la grandeur est mal nommée

- **Page** : 2605.26047, p. 3.
- **Constat** : la sécurité exclut les issues sans vainqueur [B7]. Son complément est la part de victoires de l'attaquant parmi les parties décidées, pas un taux de réussite des attaques. Le calcul (39 % et 29 %) est juste ; il part des chiffres arrondis du résumé (61 % et 71 %), la page 15 donnant 60,9 % et 70,9 %.
- **Texte corrigé proposé** : « soit une part de victoires de l'attaquant, parmi les parties décidées, qui passe de 39 % à 29 % (calcul, à partir de 61 % et 71 %) ».
- **Même remarque pour la section 4 du rapport** : Ctrl-Z écarte lui aussi les attaques sans issue ; les probabilités de capture et de réussite « need not sum to 1, as an attack may silently fail without the blue team deciding to audit it » [B51], p. 19. L'écart de définition entre les deux articles est plus petit que « épisode entier contre normalisation sans les issues nulles » ne le laisse entendre.

### F — mineur — Deux éléments de Ctrl-Z qui manquent au rapport

- **Pages** : Ctrl-Z, p. 6, 7, 8.
- Le tirage systématique est nommé et écarté pour le coût [B34], [B35], [B36]. À ajouter à la section 2.2, « Recherche active du bras non ciblé » : « Les auteurs nomment le tirage de nombreux échantillons à chaque pas comme ce que ferait une équipe sans limite de coût (p. 7-8) et s'en tiennent à au plus le double des appels. »
- La figure 4 (droite) imprime 33,2 % et 70,6 % d'attaques repérées [B40], [B41]. À ajouter au « point non tranché » : « La légende donne 33,2 % d'attaques repérées sans rééchantillonnage et 70,6 % avec (auteurs) : c'est une valeur d'information du rééchantillonnage, antérieure à 2605.26047, mesurée sur des distributions de scores. »
- La figure 4 (milieu) trace le nombre de pas d'attaque nécessaires pour réussir une fois, sous report vers le modèle de confiance et sous report vers un rééchantillon (figure, texte d'axe non contrôlé par programme). C'est une mesure d'affaiblissement de l'attaque hors audit, pour un rééchantillonnage déclenché. Le rapport cite la phrase voisine [20] sans nommer la figure.

### G — mineur — Le calcul du « 7 % » est juste ; deux précisions

- **Pages** : Ctrl-Z, p. 1, 4, 8, 9.
- Le résumé décrit le meilleur protocole comme celui qui « combines resampling with analysis of previous steps », sans nommer la surveillance non fiable ; or 7 % ne s'obtient qu'avec elle (92,6 %, tableau 2). La figure 2 nomme bien la courbe « DTR + Time Travel + UM » [B32], p. 4. Le résumé sous-décrit donc son propre chiffre : à dire en une phrase dans la section 2.1.
- Le tableau 1 contient une cellule « 58,3 % » (report vers le modèle de confiance, 99 % d'utilité). Elle n'a rien à voir avec le « 58 % » du résumé, qui est 1 − 41,8 %. À signaler pour éviter une confusion.

### H — mineur — La question pour Lazar est posée sans les indices du texte ; un voisin nommé par N-013 manque

- **Lignes** : N-013, l. 79-80 ; N-015, section 1 ; programme, l. 188.
- Le rapport dit que « deux lectures sont possibles » sans rapporter ce que le texte suggère. Les quatre indices pour la lecture stricte et l'indice contraire sont donnés au point 2 ci-dessus.
- **Texte corrigé proposé** (section 5, réserve de lecteur) : « L'énoncé ne tranche pas. Il penche vers la lecture stricte : N-013 nomme comme risque de collision "l'affaiblissement sélectif de l'attaquant" (l. 80), et les deux retraits (bruit sur les poids, bruit d'activations) portent sur un effet direct sur le modèle, l'usage en détection étant cité à part. En sens inverse, le programme donne Ctrl-Z comme base de E1.6 (l. 188), dont le chiffre inclut l'audit. Nœud de Lazar. »
- arXiv 2607.13087 (N-013, l. 80) n'est pas dans la section 7 du rapport. Il n'est nommé dans aucune des deux pièces, mais il est le risque que l'énoncé lui-même désigne. À ajouter, marqué « nommé par N-013, non par les pièces ».

### I — mineur — Incohérences de 2605.26047 non relevées, et une nuance sur le budget d'audit

- p. 19 : l'exécution du moins suspect donne « a small, marginally significant improvement » [B15] ; p. 10 : l'intervalle « includes 0 » [B16]. Les deux phrases décrivent le même résultat.
- p. 11 : rien à signaler sur le second jeu d'utilité. Le texte extrait donne « n=506 » ; c'est « n=50 » suivi de l'appel de la note 6, qui dit bien 50 tâches. Je le note pour qu'un relecteur par programme ne s'y trompe pas.
- p. 12 : les deux références « Kutasov » portent des prénoms différents (constat de forme).
- Section 4 du rapport, « budget d'audit : 1 % contre 0,3 % » : Ctrl-Z donne aussi ses courbes à 0,3 % et 3 % (annexe A, p. 13). L'écart de budget n'est donc pas entier.

### J — mineur — Profondeur et journal

- Le journal du lecteur place toute la session entre 22:51:46 et 23:01:27, soit moins de dix minutes pour 84 pages « lues ligne à ligne », 69 citations et le rapport. C'est court (règle R4). Je ne peux pas vérifier ce qui a été lu.
- Ce qui parle pour une lecture réelle : les détails d'annexe du rapport sont exacts partout où je les ai relus (auditeur simulé à 91 %, p. 15 ; consigne de l'attaquant, p. 22 ; « minimum » contre « moyenne », p. 7 et 33 ; seuils de 50 % à 99 %, p. 29).
- Ce qui manque : la phrase des pages 7-8 de Ctrl-Z, les taux de survie de la page 31, la base de la figure 7(i) et la figure 14(a) de 2605.26047, le calcul en relatif. Tous touchent une composante dite « non trouvée » ou « non occupée ».
- Le lecteur a ouvert `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md` l. 152-165. Ce fichier n'est pas dans mon mandat ; je ne sais pas s'il était dans le sien.
- **Jugement** : profondeur suffisante pour porter le verdict d'ensemble, insuffisante sur les annexes de Ctrl-Z et sur le second bras de 2605.26047.

## 3. Ce que j'ai relu à l'appui de l'occupation, et qui tient

| affirmation du rapport | page | relue | tient ? |
|---|---|---|---|
| bras à k fixe, à chaque pas | 2605.26047, p. 8 | [B6] | oui |
| premier échantillon toujours exécuté | p. 6 | [B3], [B4] | oui |
| utilité inchangée par construction | p. 6, 11 | [B5] | oui, pour ce bras seulement (constat A) |
| +10,2 points, [+6,1 ; +14,3] | p. 2 | [B2] et citation [40] du rapport | oui |
| 61 % à 71 % | p. 1 | [B1] | oui |
| échelle N = 1 à 5 | p. 7, figure 3(a) | figure vue : environ 61, 68, 70, 71, 71 % | oui |
| point fixe k = 2 vers 66 % en figure 6(a) | p. 9 | figure vue | oui, écart avec la figure 3(a) confirmé |
| exécution du moins suspect : +3,9 points, intervalle couvrant zéro | p. 10 | [B16] | oui, contre N = 2 pour information (constat A) |
| cadre concentré, quatre tâches secondaires | p. 3 | citations [42], [43] du rapport | oui |
| Ctrl-Z : tout rééchantillonnage déclenché | p. 6, 33, 34 | [B33], [B38] | oui |
| Ctrl-Z : paraphrase sur l'entrée du moniteur | p. 9 | [B47] | oui |
| contradiction annoncée, rattachée au cadre | 2605.26047, p. 1, 10, 11 | citations [35] à [37], [57], [58] du rapport | oui |

## 4. Table fermée

| énoncé | verdict du contre-lecteur | pièces qui portent le verdict |
|---|---|---|
| H6 (énoncé de N-015) | **occupé en partie** | 2605.26047v2 : rééchantillonnage à k fixe pour information (p. 1, 2, 6, 8, 9, 11) et exécution du moins suspect tirée à chaque pas (p. 10, 11, 19) ; Ctrl-Z 2504.10374v1 voisin (p. 1, 6, 7, 8, 9, 29, 31, 33-35) |

Composantes, selon moi :
- **faites** : rééchantillonnage systématique sur une échelle d'intensité (N = 1 à 5), baisse de la part de victoires de l'attaquant sans coût d'utilité, par l'audit, en cadre concentré ; à N = 2 avec exécution du moins suspect, affaiblissement de l'attaque hors audit et utilité mesurée ;
- **non faites dans les pièces lues** : paraphrase et remise à zéro du contexte comme interventions non déclenchées ; rééchantillonnage dont l'action exécutée n'est choisie par aucun moniteur et qui affaiblit l'attaque ; comparaison de pentes et test de la marge ; cadre diffus (si l'énoncé le porte).

« Non faites » veut dire « non trouvé dans les deux pièces lues », jamais « trou du champ » (règle R8). Kutasov et collègues (arXiv 2511.02997) et arXiv 2607.13087 n'ont pas été lus.
