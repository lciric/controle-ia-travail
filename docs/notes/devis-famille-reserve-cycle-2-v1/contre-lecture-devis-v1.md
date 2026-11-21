# Contre-lecture du devis de la banque d'épisodes de la famille de réserve du cycle 2 — v1

- **Pièce contre-lue** (classe A, devis) : `docs/notes/devis-famille-reserve-cycle-2-v1/devis-banque-d-episodes-famille-reserve-cycle-2-v1.md`, empreinte compagnon vérifiée conforme (`sha256sum -c`), avec son programme de recalcul et sa sortie (compagnons conformes).
- **Source** : esquisse de la pièce 6, version 1, `git show origin/claude/scellement-2-famille-reserve-cycle-2-v1:docs/notes/scellement-2-famille-reserve-cycle-2-v1/piece-6-esquisse-de-devis-banque-d-episodes-v1.md`, empreinte recalculée `981c85a1911d85e4a17a8d0828ec73bc16549b171e0d106ca6d048c8b1db79a0`, égale à son compagnon et à celle que cite le devis. Le sommet de la branche est aujourd'hui `5d6b7a2a` ; la version 1 du fichier y est inchangée.
- **Contre-lecteur** : agent neuf, Opus 5.5, qui n'a écrit ni la famille, ni l'esquisse, ni le devis, ni aucun moniteur. Écrit le 2026-11-21, fini à 18:05:57Z (`date -u`).
- **Ce que je n'ai pas lu** : les pièces 1 à 5 et 7 de la famille, la version 2 de la pièce 6, le coffre, la valeur de `k`, la pièce de sécurité du banc fermé, la note des lignées, tout fichier interdit par le mandat. Une ligne du registre des accords (la 669), dont le texte portait un motif interdit, a été masquée par un filtre avant affichage et n'a pas été lue.

## Verdict

**À corriger.** L'arithmétique est juste : je l'ai recalculée deux fois, en relançant le programme (sortie identique octet pour octet à la sortie scellée) puis avec un programme indépendant écrit ici. Tous les prix sont fidèles à leur source. L'esquisse est suivie point par point, et rien ne montre une lecture des pièces 2 à 5. Il reste trois corrections de fond et plusieurs mises au point avant toute demande d'accord. Elles portent sur la confrontation des lecteurs aux familles des moniteurs, sur les plafonds par file de la garde d'arrêt et sur la clé Claude. Aucune ne change le total attendu de 84,73 dollars ni le plafond de 389 dollars, sauf le point 4 (marge de change).

## Ce qui a été vérifié et tient

- **Empreintes des pièces de la section 1** : les quatorze empreintes recalculées sont égales aux préfixes cités. Cela vaut pour le devis du bras A en version 2, le brouillon 3 de l'essai de mesure, les deux pages de prix scellées, le collisionneur 9-3, le relais Claude, la note sur Mistral, l'esquisse du premier cycle en version 3 (que l'index sans contenu donne comme celle qui fait foi), le devis de la banque à deux modes, le devis de la nuit du 1er novembre, la décision sur les tâches fraîches, les deux procédures et l'environnement des propositions. La branche `claude/pensive-bardeen-1fv7hw` est passée de `4c652340` à `079dc9f4`, mais les fichiers cités y sont identiques.
- **Prix, relus à la source** :
  - Opus 5.5 à 4 et 20 dollars, Sonnet 5.5 à 2 et 10, relus sur la page d'Anthropic scellée (tableau des modèles) ; même barème dans `relais_reel.py:50-51` et `collisionneur_v9_v3.py:131`.
  - Gemini 4 Neon à 3 et 15 dollars, réflexion comprise, relu sur la page de Google scellée, onglet « Standard ».
  - Mistral Large 4 à 0,70 et 2,10 dollars, avec un facteur de 1,1 pour un point d'accès régional, relu dans `choix-mistral-deepseek-v1.md:19`, qui dit lui-même que la page a été lue par un outil de résumé (`:6`). Le prix de repli au double se justifie donc.
  - Carte : 1,1833 dollar par heure (offre à 1,1843, stockage compris) à `registres/depenses.md:515` ; bornes de 1,30, 0,08 et 0,05 à `devis-bras-a-v2.md:67-69` ; 42,8 et 40,2 secondes par épisode à `:42-43` et `:54` ; 1,0 heure de mise en route, supposée, à `:56` ; pire cas au facteur 4 à `:81` ; coût fixe de 2 à 3,5 dollars à `devis-couche-2-banque-deux-modes-v1.md:37`.
  - Jetons : sorties de 49 à 234 et de 62 à 403 jetons à `depenses.md:541-542` ; 0,602 dollar pour les 48 lectures d'Opus à `:546`, d'où environ 302 jetons de sortie, recalculés ; entrées supposées et garde à un jeton par octet à `devis-essai…:144-145` et `:166`.
  - Les traitements par lots sont bien refusés par le relais (`relais_reel.py:57-60`).
- **Arithmétique, recalculée par python** :
  - Volumes : 260 épisodes, 2 600 actions, 320 ensembles par lecteur, ce qui donne bien les 4 × `n` × `e` + `n_f` × `e` + 3 × 20 de l'esquisse.
  - Prix par question : 0,0273 et 0,0736 (Opus) ; 0,0105, 0,0292 et 0,0584 (Mistral) ; soit 0,0378 et 0,1320 pour les deux lecteurs.
  - Carte : 4,03 à 5,68 dollars, pire cas 18,71 ; 3,77 à 5,35, pire cas 17,40 ; plafond 37.
  - Lectures : 212 et 127 ; essai 13 ; total 389.
  - Attendu au centre : 84,73 ; rapport du plafond à l'attendu : 4,59.
  - Lecture groupée : 51, 31 et 4, total 123.
  - Variante à 100 épisodes par dose : 420 épisodes, 480 ensembles, carte 47, lectures 508, total 568.
  - Ancre jugée par Neon : 1,38, 4,72, plafond 5.
  - Seuil d'alerte : 311,20. Étapes : 244 et 145.
  - Aucun écart.
- **Plafond pessimiste** : il couvre bien un débit deux fois plus lent avec une relance complète, `k` ≤ 8, des entrées à 6 000 jetons, des sorties de 2 000 jetons (Claude) et de 9 000 jetons (Mistral), 15 % d'envois en plus et le prix de repli de Mistral. Ses angles morts sont aux points 4, 6 et 7.
- **Fidélité aux cinq points de l'esquisse** : les cinq points sont repris tels qu'énoncés à la section 5 de l'esquisse.
  - Le point 2 garde « ni celle des moniteurs, ni celle de l'agent ».
  - Le point 3 garde « ni l'auteur, ni un concepteur de moniteur ».
  - Le point 4 reprend la réserve de la section 3 de l'esquisse sur les tâches fraîches.
  - Les quatre postes, l'ordre en deux étapes (A et C, puis les épreuves, puis B), l'ancre humaine sur 30 éléments sans calcul et le renvoi des moniteurs gelés hors du devis sont fidèles.
- **Absence de lecture des pièces 2 à 5** : déclarée, et rien dans le texte ne nomme, ne décrit ni ne suggère un mode. Seules la structure en clair de la pièce 6 et une question fermée sur la pièce 3 apparaissent (attestation à trois cases).

## Corrections et mises au point

1. **À corriger : mauvaise citation, et lecteur Claude hors de la confrontation en cours.**
   - Le devis écrit « Un audit des lignées est en cours (`registres/go.md:671`) ». Cette ligne porte sur la voie de sécurité du banc fermé et ne dit rien des lignées.
   - La ligne qui le dit est `registres/go.md:664` : le côté habilité du bras A est chargé de confronter Mistral Large 4 et Gemini 4 Neon aux familles, et de contre-lire le module des autres moniteurs, en version 11.
   - Cette confrontation ne nomme pas de lecteur Claude. Or le devis recommande Opus 5.5 (ou Sonnet 5.5) comme premier lecteur. Depuis les pièces que je peux lire, rien n'établit qu'aucun moniteur du cycle 2, ni aucun du module des autres moniteurs, ne soit de la famille Claude.
   - « Deux familles hors de la contrainte » (point 2, option (a)) n'est donc pas établi ; seules sont écartées Llama et Qwen.
   - À faire : corriger la citation ; écrire au point 2 et à la condition 7 que la confrontation couvre les deux lecteurs retenus (le modèle Claude compris) et l'option Neon de l'ancre, contre les moniteurs du cycle 2, et qu'elle est rendue par le côté habilité (`go.md:664`) ; retirer jusque-là la phrase qui affirme l'exclusion.
2. **À corriger : plafonds de la garde d'arrêt, par file.**
   - Le texte de la section 4.2 donne entre parenthèses, comme « plafond de la file », 0,260 dollar pour Opus 5.5 et 0,113 pour Mistral. Ces chiffres sont le pire cas d'un seul envoi (`devis-essai…:166` ; recalculés : 0,2598 et 0,1127). Ce ne sont pas des plafonds de file.
   - La garde est dite « par file et par fournisseur », mais le devis ne donne de plafond que par étape (les deux lecteurs ensemble) et par compte.
   - À faire : écrire le plafond de chaque file. Recalculés ici, à `k` = 8 :
     - Opus 5.5 : 117,76 dollars à l'étape 1, 70,66 à l'étape 2, 7,07 à l'essai ;
     - Mistral au prix de repli : 93,51 à l'étape 1, 56,11 à l'étape 2, 5,61 à l'essai.
   - Corriger la phrase entre parenthèses pour séparer le pire cas d'un envoi du plafond de la file.
3. **À corriger : la clé Claude.**
   - « La clé "Luc" sur son mot (`registres/go.md:547`) » ne tient pas. Cette ligne répartit les clés pour la course « nouvelles attaques » de l'organisme, une course fixée par clé, et n'accorde rien à cette banque.
   - De plus, `registres/decisions.md:4786` rapporte, sur la même ligne que les 153 dollars restants de Luc, une décision de Lazar à 100 dollars par clé pour une autre course. Ce reste n'est donc peut-être pas libre.
   - À faire : écrire qu'aucune clé Claude n'est aujourd'hui désignée pour cette banque. La clé « Rigaud » est sans crédit (`depenses.md:577-578`), et la clé est à désigner et à recharger par Lazar (nœud, condition 8). Retirer la citation de `go.md:547` comme mot d'accord.
4. **À corriger : marge de change hors du plafond.**
   - Le plafond de 389 dollars ne comprend pas les 5 % de marge de change, renvoyés « en sus si un compte est facturé en euros ».
   - Le devis ne dit pas quels comptes facturent en euros. Le compte Mistral, européen, est le premier candidat. La ligne citée, `go.md:667`, parle de « euros affichés » pour les clés du bras A, sans nommer le fournisseur.
   - Un plafond pessimiste ne peut pas laisser dehors un surcoût connu. À faire : dire, compte par compte, la devise de facturation. Faute de relevé, ajouter 5 % à la part de Mistral au plafond (155,22 dollars, essai compris, soit 7,76 de plus ; plafond total porté à 397), ou à tout le plafond.
5. **À préciser : compte Google de l'ancre.** La ligne citée pour « compte Google du projet, clés 1 et 2 » (`go.md:667`) ne nomme pas Google. Citer la ligne qui nomme ces clés et leur fournisseur, ou écrire « à confirmer ». Cela reste hors des totaux tant que le nœud de l'ancre n'est pas tranché.
6. **À ajouter aux gardes des lecteurs (section 4.2)** :
   - (a) Refus, avant l'envoi, de tout corps qui demande le mode rapide d'Anthropic, facturé à 8 et 40 dollars pour Opus 5.5 sur la page scellée, ou une géographie d'inférence « us », à 1,1 fois. Le plafond ne couvre ni l'un ni l'autre.
   - (b) Arrêt de la file sur toute réponse dont les compteurs dépassent la sortie maximale comptée. C'est la garde de sortie maximale du bras A (`devis-essai…:254`). Elle compte surtout pour Mistral : sa longueur maximale de sortie n'est pas publiée (`choix-mistral-deepseek-v1.md:16`), et on ne sait pas si la borne de sortie s'applique au raisonnement.
   - (c) Le délai d'attente par envoi et par file, garde de délai du bras A (`:253`), nommé et non seulement « repris ».
   - (d) Le coût d'écriture du cache d'Anthropic (5 dollars, au-dessus des 4 de base), si la lecture de cache, comptée comme économie, est employée.
7. **À dire : effort du lecteur Claude.**
   - L'attendu suppose l'effort bas ; le plafond couvre l'effort moyen (section 11, point 6).
   - Pour le bras A, Lazar a demandé l'effort maximal pour le lecteur Mistral (`go.md:569`), et le devis renvoie l'effort du lecteur Claude « à la règle du bras A ». Si cette règle donne un effort haut, l'attendu et le plafond ne sont pas couverts : une file arrêtée au plafond laisse des tâches lues à moitié.
   - À faire : fixer l'effort du lecteur Claude dans le devis, ou écrire que l'essai d'admission et de mesure le mesure avant tout plafond d'étape (option (b) du point 1, déjà recommandée).
8. **À déclarer comme supposé : deux jeux de constantes.** Ils servent au calcul sans figurer au tableau 3.3 :
   - la lecture groupée : 150 jetons d'entrée et 150 de sortie par question, réflexion de 300 jetons (Claude) et de 3 000 (Mistral) ;
   - les sorties de Neon : 1 500 jetons attendus, 6 000 au pire.
   Le plafond de 123 dollars et celui de 5 dollars en dépendent.
9. **Mise au point : arrondi du prix d'une action.** Le programme rend 0,00141 à 0,00164 dollar ; le devis retient « 0,0014 à 0,0016 » au point 1 comme prix à retenir. Le haut est arrondi vers le bas : écrire 0,00164, ou 0,0017. De même, l'attendu bas de la carte prend 1,1833 dollar par heure (carte seule), alors que le relevé stockage compris est de 1,1843. L'écart est négligeable, mais à dire.
10. **Mise au point : minuterie du lancement 2.** Si le plafond du lancement 2 est recalculé sur le débit mesuré (12,67 dollars pour 42,8 secondes), la minuterie d'arrêt dur à 9,7 heures doit l'être aussi, par la même formule. Sans cela, la garde horaire permet plus d'heures que le plafond recalculé n'en paie.
11. **Réserve bloquante, déjà déclarée : la version 2 de la pièce 6.**
    - D'après le registre (`decisions.md:4784`), la famille a été acceptée en version 2 (sommet `5d6b7a2a`). Le devis chiffre la version 1, conformément à son mandat, et son propre sondage dit que les relectures des épreuves et l'ancre ont été récrites.
    - Tant que la condition 2 de la section 9 n'est pas remplie, les lignes des lectures et de l'ancre ne sont pas engageables. La ligne de la carte reste opposable.
    - Le comptage de chaînes fait par programme sur la version 2 est un écart au mandat, qui ne nommait que la version 1. Il est déclaré, et ne touche ni les pièces 2 à 5 ni le coffre. La mère en juge. Je ne l'ai pas refait.
12. **Mineur : variante à 200 épisodes.** L'esquisse cite aussi « 100 ou 200 épisodes par bras » (section 3). Seule la variante à 100 est chiffrée ; les formules du programme suffisent pour 200, à écrire en une ligne si le titulaire la demande.

## Vérification des corrections

Le même contre-lecteur vérifie les points 1 à 4, et les points 6, 7 et 8 s'ils sont repris. Le programme de recalcul doit être relancé après les points 2, 4 et 10, et sa sortie scellée de nouveau.

## Journal

- Refus d'outil ou de classifieur : aucun.
- Réseau : trois récupérations de branches par `git fetch`. Aucun appel à un modèle, aucune dépense, aucun commit, aucune poussée.
- Écrit : cette pièce seule, dans ce dossier, scellée. Copies de travail et programme de recalcul indépendant dans le bloc-notes de session, hors du dépôt.
- Lu en passant, à déclarer :
  - (1) `devis-bras-a-v2.md:42-43` porte des durées de courses de la chaîne précédente (nombre d'épisodes et secondes). Ce sont des relevés de débit, sans score ni verdict ; je n'en ai gardé que les secondes par épisode.
  - (2) `registres/decisions.md:4786` porte des relevés d'une autre course (« Raisons ou regard ? »). Je n'en ai gardé que le solde de la clé.
  - (3) Une recherche dans les registres a affiché des débuts de lignes qui nomment une course interdite par le mandat. Seuls les en-têtes ont été affichés, sans aucun résultat.
