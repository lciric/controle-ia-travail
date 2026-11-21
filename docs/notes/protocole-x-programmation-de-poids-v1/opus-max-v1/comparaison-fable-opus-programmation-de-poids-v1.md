# Comparaison des deux réponses sur la programmation de poids : Fable 5.2 (v2) et Opus 5.5 en effort maximal (v1)

- **Classe C** (travail), non contre-lue. Comparateur neuf : Claude Opus 5.5, qui n'a écrit aucune des deux réponses. Le 21 novembre 2026, après 20:09 UTC. Ni commit, ni appel payant, ni recherche en ligne.
- **Grille** : écrite et scellée avant toute lecture, `grille-comparaison-programmation-de-poids-v1.md` (même dossier), `89d133ec66ec212d6755716bcdc87b24716043c98a317dc4a9f68ed6127884ee`. Échelle de 0 à 3 par critère, sans total.
- **Pièces lues** (empreintes égales à leur compagnon) :
  - la réponse de Fable, v2 : `../reponse-fable-programmation-de-poids-v2.md`, `90bbe866…35d6` ;
  - sa contre-lecture par Opus : `../contre-lecture-reponse-fable-programmation-de-poids-v1-opus-v1.md`, `2f0929fb…001c` (verdict et constats 1 à 5, 9) ;
  - la vérification de ses corrections : `../verification-corrections-programmation-de-poids-v2-opus-v1.md` (verdict « conforme ») ;
  - la question servie à l'organisme d'idéation, v1 ;
  - la réponse d'Opus en effort maximal : `reponse-opus-max-programmation-de-poids-v1.md`, `a50517f8…cf6`, avec sa sortie de calcul `calcul-poids-v1.txt`.
- **Non lu** : le dossier `../recherche-approfondie-v1/`. Il contient une réponse de Fable plus récente (18:49 UTC), « approfondie », sur une question voisine, et elle sort du mandat. Elle n'est pas comparée ici, et la mère devra dire si elle remplace la v2.
- **Cloisonnement** : aucun chemin interdit n'a été ouvert ; rien sous les dossiers exclus.

## 1. Les chiffres vérifiés à la page

J'ai extrait le texte des PDF empreintés avec `pdftotext`, page par page.

| Réponse | Chiffre | Source, page | Résultat |
|---|---|---|---|
| Fable | 135 essais d'attaque sur 374 (36 %) installent la propriété | Zhou et Sehwag, 2610.27735v2, p. 7 | juste, à la lettre |
| Fable | Le rappel des moniteurs de transcription, à 2 % de fausses alertes, tombe de 56-81 % à 16-28 % ; de 91-99 % à 56-89 % avec le raisonnement | même source, p. 10 | juste |
| Fable | Auditer le successeur donne 0,68 d'aire sous la courbe et signale 36 % des successeurs sains | même source, p. 34 | juste |
| Fable | Sondes de tromperie : 0,991 et 0,996 d'aire avant l'entraînement, 0,376 et 0,655 après, 1,000 pour la sonde du domaine ; ce sont des sondes réapprises | Taufeeque et al., 2602.15515v2, p. 7, tableau 4 | juste depuis la v2. La v1 lisait mal la nature des sondes ; c'est le contre-lecteur qui l'a vu |
| Fable | Deux auditeurs généralistes désignent 73 % et 56 % des points édités ; l'un s'abstient sur presque tous les sains ; l'autre déclare sains 41 % des édités | Zeng et al., 2611.15118, p. 16, tableau 5 (72,81 ; 56,14 ; 99,03 ; 41,23) | juste |
| Fable | Remise à zéro toutes les 50 épisodes : 1 013 épisodes avant l'alerte contre 269 en continu (facteur 3,8) ; 6 479 contre 1 102 (facteur 5,9) ; fausse alerte de l'honnête 0,1238 | `../calculs-programmation-de-poids-v2.txt`, lignes 108, 109 et 156 | juste |
| Opus | Sept neurones sur plus de 12 000, ajustés sur 23 trajectoires, déclenchent la charge sur au moins 98,8 % des trajectoires déclenchées ; la technique a été trouvée seule par Claude Code | Zeng et al., p. 1 | juste, à la lettre |
| Opus | Opus 5.5 juge propres 47 des 114 points modifiés (41,23 %) et modifiés 2 des 103 propres ; Astra ne se prononce pas sur 99,03 % des points propres | même source, p. 16, tableau 5 | juste |
| Opus | Le détecteur à cinq traits trouve 32 des 35 points modifiés, pour 3 fausses alertes sur 31 points propres | même source, p. 17, tableau 6 (91,43 % et 9,68 %) | juste |
| Opus | Sous transformation qui garde la fonction : 7,3 % puis 22,0 % de prédictions changées ; justesse de 57,8 % à 54,4 % | Cha et al., 2611.05798, p. 1 | juste |
| Opus | Les mises à jour de type réglage fin rendent souvent périmées des sondes gelées ; « fine-tuning should trigger activation-monitor revalidation by default » | Duan, 2606.15980v2, p. 1 | juste, à la lettre |
| Opus | « tampering only with its random coins » ; la détection à l'exécution est « akin to giving the defender an additional chance… » | Goldwasser et al., 2204.06974, p. 1 ; Christiano et al., 2409.03077, p. 1 | juste |
| Opus | À 1 % d'artefacts falsifiés : risque résiduel 0,445 % (÷ 2,2) et précision 22,6 % ; ÷ 10,4 pour le détecteur à traits | `calcul-poids-v1.txt`, ligne 95 ; recalculé à la main à partir du tableau 5 | juste |

J'ai aussi vérifié deux affirmations sur le code du dépôt :
- **Le dépôt prend déjà des empreintes de poids** (Opus). Les fonctions `empreinte_base` et `empreinte_adaptateurs` existent (`src/controle_ia/organismes/lora.py`, lignes 110 à 128). Opus a raison. Fable dit que le manifeste ne consigne aucune empreinte de poids ; c'est vrai pour le seul module du manifeste, et Fable n'avait pas lu les lanceurs.
- **L'invariant « aucun score de moniteur dans l'entraînement de l'agent » est « gardé par le code »** (Opus). C'est bien le texte de la décision N-053, ligne 43. La taxe de déplacement (HC4) est bien à la ligne 106 du programme.

## 2. Notes par critère

| Critère | Fable v2 | Opus max v1 | Pourquoi |
|---|---|---|---|
| 1. Chiffres à la page | 3 | 3 | Tous les chiffres vérifiés sont justes et bien situés. Pour Fable, c'est vrai après la contre-lecture : une lecture fausse de la v1 n'a été prise que par le contre-lecteur. Opus n'est pas encore contre-lu |
| 2. Profondeur | 3 | 2 | Fable chiffre le mécanisme central : la remise à zéro de l'accumulation, la dépense du niveau d'alerte à chaque écriture, la cadence, le rejeu partiel. Il pose six mondes plantés, avec ce qui doit mourir et ce qui doit tenir. Opus range très bien les défenses en couches et pose les bornes d'impossibilité, mais il ne calcule pas ce que devient une accumulation à travers une écriture |
| 3. Originalité | 3 | 2 | Fable : l'écriture comme troisième axe de fragmentation, le rodage tiré au sort entre l'ancien et le nouvel état, le jumeau d'écriture avec le test du signe, la quarantaine chiffrée, le retournement (l'écriture comme pièce à conviction). Opus : la graine tirée hors de celui qui écrit (tirée de Goldwasser et al.), l'audit du cumul des retouches, les canaris dans les pièces cloisonnées, le correctif de flotte interdit par la décision N-053, la taxe de déplacement rapportée par niveau d'accès. Opus présente lui-même sa réponse comme un assemblage de défenses publiées |
| 4. Limites et R8 | 3 | 3 | Les deux disent « rien de revendicable » et nomment leur premier pas non justifié. Fable s'est corrigé deux fois, et il signale le risque « trop beau » (R4). Opus déclare qu'il a vu deux lignes du registre résumant la note de Fable, et il marque chaque recoupement avec elles |
| 5. Règles et nœuds | 3 | 2 | Fable écarte du défaut la lecture des organismes saboteurs : il faut un agent habilité et ton mot. Opus met cette lecture dans le défaut de sa décision D-4. Sa condition (hors du mode tenu à l'écart, par une session qui ne conçoit aucun moniteur) est bonne mais ne suffit pas. Ses nœuds D-2 et D-3 sont justement posés |
| 6. Actionnabilité | 2 | 3 | Fable propose neuf décisions et treize propositions sur 105 Ko : c'est complet, mais lourd à trancher. Opus propose cinq décisions au format demandé, adossées au code existant |
| 7. Coût | 3 | 3 | Les deux font le code d'abord et mettent toute passe de modèle sur devis. Fable passe par le crochet à l'inférence avant toute écriture dans les poids. Pour la rédaction, Opus coûte moins : la réponse de Fable a pris le quota rare de Fable plus une contre-lecture (GO-2026-11-21-75) |
| 8. Ce qui manque | 2 | 2 | Fable : il manque le papier de Duan (pourtant au dépôt, sous `docs/sources/pdf/`), les bornes d'impossibilité, le hasard comme pièce de la provenance, l'extension de la décision N-053 à l'écriture directe, et la taxe de déplacement par niveau d'accès. Opus : il manque les deux voisins les plus proches de la menace diffuse, le banc où l'agent entraîne son successeur (Zhou et Sehwag) et ResearchArena (Libon et al.), ainsi que Davies et al. Il ne corrige pas « borne haute » (Sheshadri et al. ; Abu Baker et al.), et il n'a ni le rodage, ni le sas, ni le coût de la remise à zéro |

**Qui l'emporte.** Fable v2 l'emporte de peu, sur la profondeur, l'originalité et le respect des règles. Opus l'emporte sur la concision et sur la couverture de deux appuis décisifs : la péremption des sondes gelées et les bornes d'impossibilité. Il apporte aussi la correction de fait la plus lourde de conséquences (contradiction 1).

## 3. Ce que chacune a seule

**Seulement chez Fable.**
- Les quatre plumes (l'entraîneur, le chargeur, l'éditeur, le magasin de fichiers) et les échelons d'écriture.
- Le calcul de la remise à zéro : facteurs de 1,4 à 5,9 ; fausse alerte de l'honnête de 12 % ; le niveau d'alerte réparti entre les états ; la règle de cadence.
- Le rejeu partiel des écritures : 95 % rejouées pour prendre la première déviation avec probabilité 0,95.
- Le rodage tiré au sort, sous la forme du hasard du défenseur.
- Le sas et sa liste de ce qu'il faut réadmettre.
- La correction de « borne haute » pour nos organismes à adaptateur.
- L'environnement de curation de données comme terrain de la menace, avec cinq citations obligatoires.
- La quarantaine chiffrée des poids du bras d'exception.
- Le rejet chiffré des témoins-leurres.
- Le couple neutre pour le collisionneur.

**Seulement chez Opus.**
- Les bornes d'impossibilité : une porte dérobée peut être indétectable même avec tous les poids en main, et la défense reste possible à l'exécution.
- La graine tirée hors de celui qui écrit, après le scellement des données et du code.
- Le test du résidu de re-dérivation, chiffré : une écriture cachée reste sous environ σ√n, et rien ne se cache quand la re-dérivation est exacte.
- La lecture comme porte, chiffrée : elle divise le risque par 2 à 10.
- Trois objets de contrôle pour tout lecteur de poids : le jumeau honnête, la copie qui garde la fonction, la vérité plantée.
- Le point d'attaque de la quantification : l'artefact audité n'est pas l'artefact servi.
- L'extension de la décision N-053 à l'écriture directe et à la lecture des moniteurs (sa D-2).
- La taxe de déplacement rapportée par niveau d'accès (sa D-3).
- Le correctif de flotte jugé hors de la sonde qui l'a motivé.
- Les canaris posés dans les pièces cloisonnées pour détecter une fuite.
- Le risque d'initié sur le banc : la technique a été trouvée par un agent de la famille Claude.

## 4. Contradictions, et qui a raison à la source

1. **Une sonde fixe glisse-t-elle sous une écriture bénigne ?**
   - Fable v2 : « aucun appui publié direct » ; il donne 0,5 de chances au glissement.
   - Opus cite Duan, 2606.15980v2, p. 1 : les mises à jour de type réglage fin (dont les adaptateurs à rang bas) « frequently make probes stale », la quantification beaucoup moins, et la fragilité dépend du moniteur.
   - **Opus a raison** : l'appui publié direct existe, et il est au dépôt. Duan le mesure en aire sous la courbe, c'est-à-dire sur le rang. Une perte de rang est plus forte qu'un décalage de niveau, donc l'appui vaut aussi pour le niveau. La réserve de Fable tient pour un autre point : une aire stable ne garantit pas un seuil stable.
   - Opus va trop loin dans l'autre sens. « Violée par toute écriture » contredit sa propre source : la quantification préserve la sonde, et « retraining a behavior need not stale its corresponding monitor ». Et Taufeeque et al. ne valent pas pour une écriture bénigne : c'est la page 7 que Fable a relue, la page 1 qu'Opus cite ne suffit pas. Fable a raison sur ce point.
2. **Que faire de la preuve accumulée après une écriture ?**
   - Opus : refaire la référence honnête (son compte m), sans rien dire de l'accumulation.
   - Fable : la référence se refait ; l'accumulation, elle, ne traverse l'écriture que par un nul refait à chaque acte contre un jumeau honnête du même état, ou par un événement que l'honnête ne commet jamais. Repartir de zéro dépense le niveau d'alerte à chaque écriture, et le calcul le montre.
   - Ce n'est pas une contradiction : la position d'Opus est incomplète. Sa règle « auditer le cumul depuis le dernier état signé » applique aux poids la même logique de non-remise à zéro.
3. **Témoins-leurres ou canaris.**
   - Fable : l'empreinte domine les leurres.
   - Opus : des canaris dans chaque organisme, pour identifier la copie servie.
   - Pour voir une substitution, Fable a raison : l'empreinte fait mieux. Le canari ne vaut que là où l'on n'a pas les octets. Les canaris dans les pièces cloisonnées, eux, sont un autre objet : ils détectent une fuite, et ce n'est pas un leurre. L'idée d'Opus est à garder sur ce point.
4. **Ce qui existe déjà au dépôt.** Opus a raison : les empreintes de la base et des adaptateurs existent dans `lora.py`. Les deux s'accordent sur ce qui manque : l'artefact servi, les sondes, les juges, et la vérification à chaque chargement.
5. **La lecture de la différence de poids des organismes saboteurs, par défaut.**
   - Fable la sort du défaut : un agent habilité, ton mot, et la dispersion entre graines honnêtes d'abord.
   - Opus la met dans le défaut de sa D-4.
   - **Fable a raison.** La règle de cloisonnement des organismes (N-054, point 3) et la hiérarchie de décision ne permettent pas qu'un défaut ouvre une lecture d'organisme saboteur. Et sans la dispersion entre graines honnêtes, on ne saurait pas à quoi comparer l'écart du saboteur.

## 5. Synthèse recommandée pour Lazar

**Ce qu'il faut retenir.**
- L'écriture de poids est bon marché ; la lecture ne l'est pas, et elle est impossible au pire. La défense tient donc par la structure :
  - l'agent propose, le harnais écrit ;
  - l'empreinte de l'artefact servi ;
  - la graine tirée hors de celui qui écrit ;
  - le sas, qui réadmet les instruments sur chaque nouvel état ;
  - le rodage tiré au sort.
- La lecture des poids oriente l'audit ; elle ne sert jamais de porte.
- Une écriture dans l'agent surveillé périme ses sondes jusqu'à leur revalidation. C'est publié (Duan), et cela dépend du moniteur.
- La preuve accumulée ne traverse une écriture que dans les deux voies chiffrées par Fable.
- Rien n'est revendicable.

**Décisions qui changent.**
- **Le registre des empreintes de poids** (D-1 de Fable et D-1 d'Opus fusionnées) : bâtir sur les fonctions de `lora.py`, étendre aux sondes, aux juges et à l'artefact servi, et ajouter la graine tirée hors de celui qui écrit. Défaut (a) : du code, sans dépense.
- **La mesure du glissement des sondes** (D-3 de Fable) : sa prémisse a maintenant un appui publié, ce qui la rend plus probable et la mesure plus urgente. Il faut reprendre le protocole de Duan (perte d'aire d'au moins 0,05) et mesurer en plus le niveau. Il faut un erratum à la note de Fable sur « aucun appui publié direct ».
- **Les voisins à lire en entier** (D-9 de Fable) : ajouter Duan à la liste.
- **Deux nœuds neufs, pris chez Opus** :
  - étendre l'invariant « aucun score de moniteur dans l'entraînement de l'agent » à l'écriture directe et à la lecture des moniteurs (je recommande (a)) ;
  - déclarer le niveau d'accès dans les papiers A et C, et rapporter la taxe de déplacement par niveau (je recommande (a)).
- **La lecture de la différence de poids des organismes** (D-4 d'Opus) : son défaut se restreint aux adaptateurs honnêtes, comme dans la D-3 de Fable. Le saboteur ne se lit que sur ton mot.
- **Les témoins plantés** (D-5 de Fable et d'Opus) : ils ne servent que d'objets de contrôle, posés par crochet à l'inférence d'abord. On y ajoute les trois objets de contrôle des lecteurs (Opus) et les canaris de fuite, posés par la seule session habilitée.
- **Inchangées** : les D-4, D-6, D-7 et D-8 de Fable.
- **Avant tout emploi** : la réponse d'Opus doit être contre-lue, comme celle de Fable l'a été.

**Pour la règle « repose les questions exploratoires à Opus en effort maximal ».** Sur cette question, Opus en effort maximal n'égale pas Fable sur le mécanisme chiffré. Il le complète sur la littérature et le corrige sur un fait. Les deux ensemble valent mieux que chacun seul.
