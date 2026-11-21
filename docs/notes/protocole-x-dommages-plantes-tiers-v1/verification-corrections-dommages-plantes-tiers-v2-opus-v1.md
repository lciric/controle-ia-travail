# Vérification des corrections — la campagne de dommages plantés par un tiers (v2)

- **Date** : 21 novembre 2026, vers 16:55 UTC (`date -u` au début : Sat Nov 21 16:47:08 UTC 2026). Dépôt à `7339e448f`.
- **Auteur** : Claude Opus 5.5, le contre-lecteur de la v1 (`contre-lecture-reponse-fable-dommages-plantes-tiers-v1-opus-v1.md`, `ece1df20e5748a6d…`), sur mandat de la mère (R-3735 : vérification des corrections par le même contre-lecteur). Pièce de travail (classe C). Lecture seule hors de ce fichier ; aucun appel payant, aucun commit.
- **Pièces vérifiées, empreintes égales aux compagnons** : `reponse-fable-dommages-plantes-tiers-v2.md` (`1ec3cdf8…`) ; `calculs-dommages-plantes-tiers-v2.py` (`c94ca828d9a7bbcd…`) et `.txt` (`6d541308fbfa9d85…`), égales à celles que la note cite ; `collisionneur-v2/faits-dommages-plantes-tiers-v2.md` (`3eb45ad4cb64f27a…`) et `question-dommages-plantes-tiers-v2.md` (`70b7f75ed94aa859…`).
- **Rejeu** : le programme v2, une fois, dans mon bloc-notes (`python3 -I`) : code de sortie 0, sortie **identique à l'octet** au `.txt` versé (`cmp`).
- **Lu** : la table des constats, le verdict, les § 3.2 à 3.8, 4, 6 et 7, les décisions D-1 à D-12, le relevé de méthode (extraits) ; les blocs B.5, F.2, G.1, K.3, K.4 et I de la sortie, et la fonction de devis du programme.
- **Cloisonnement** : deux sorties trop longues ont été déposées automatiquement par l'outil sous `/root/.claude/` ; je ne les ai pas ouvertes, j'ai relu les mêmes passages par leur chemin du dépôt.

## Verdict

**Conforme.** Les dix-huit constats sont **portés justes** ; aucun n'est porté mal ni manquant. Les nombres neufs sont exacts : la garantie par programme linéaire (1 268, 1 091, 599, et la forme fermée), la borne d'audit à 0,90 et le partage à 95 % (416 et 391 épisodes), le devis (266 et 11 625 USD). D-8 est bien un nœud. D-11 et D-12 sont bien posées. L'ajout du rédacteur sur le niveau du mélange est juste, et sa règle par réunion se démontre en deux lignes (plus bas). Trois réserves mineures restent, aucune ne bloque.

## Les dix-huit constats

| N° | État | Où je l'ai vu, et ce que j'ai vérifié |
|---|---|---|
| 1 | porté juste | § 3.4 (« Mais le saboteur mélange »), verdict 5 et 8, § 3.7, D-3, bloc K.3. Programme linéaire juste (deux contraintes, au plus deux strates). Je retrouve 1 268,2, 1 090,9 et 598,9 par recherche en épisodes entiers. La forme fermée « dose_u × horizon + max sur s de (dose_s − dose_u) × K_s » est exacte quand la strate u est jamais plantée ; 1 349 (tiers à q = 0,2 à côté d'un dixième jamais planté) = 1 000 + (1/3 − 1/10) × 1 496, juste. Le seuil de 0,03 est juste : ln 20 / (0,01 × 10 000) = 0,0300. |
| 2 | porté juste | § 3.4 (« Deux risques, un niveau »), § 3.7, G.1, B.5, D-12. Recalculé : 0,025^(1/30) = 0,884 et 416 épisodes ; 0,025^(1/59) = 0,939 et 391 ; 0,0125^(1/30) = 0,864 et 426. D-12 (b) : 85 % avec deux strates, juste par réunion. |
| 3 | porté juste | § 3.2 (rôle du repéreur ; le côté est scellé avant l'écriture ; le dépositaire ne lit rien), § 3.3 (la liste ne porte que des strates dans la référence), § 3.6 (le témoin se compare aux placebos du même genre), devis, D-11. La branche « dans la liste » est posée en nœud, avec son effet (minimum à peu près f). |
| 4 | porté juste | § 3.4 et § 5 : quatre erreurs par copie injectée, notre choix plus strict. |
| 5 | porté juste | Bloc I v2, § 4. Comptes vérifiés au centre : 540 plants gardés, 772 écrits, 120 témoins (172 écrits), 284 rejetés lus, 180 placebos, (540 + 120 + 180 + 45 + 45 + 284) × 2 = 2 428 lectures. Le repérage est compté à un appel par tâche. Le deuxième placebo de l'étape 1 est retiré avec un motif juste. Le nombre de compléments n'est pas chiffré, et c'est déclaré. |
| 6 | porté juste | D-8 : nœud, sans défaut ; (b) s'applique d'ici le mot de Lazar. § 3.4, plan, point 4. |
| 7 | porté juste | Couple v2 : titres et identifiants seulement, « 29 sur 29 » retiré, témoins non nommés. Aucun chemin, aucun nom, aucun identifiant de registre. Une réserve mineure (R2 ci-dessous). |
| 8 | porté juste | Verdict 4, § 3.4, D-2 (c) : 59 est un repère, la borne exacte s'écrit quel que soit le compte. |
| 9 | porté juste | Verdict 8, § 3.7, D-3 : « borne du plafond, non du plancher ». |
| 10, 11 | portés justes | § 1, point (1). |
| 12 | porté juste | § 3.3, règle 3. |
| 13 | porté juste | § 3.2. |
| 14 | porté juste | § 3.4, plan, point 2 (« si D-3 (a) est retenue »). |
| 15 | porté juste | § 3.4 : toutes les doses sont plantées ; la séquence fixe ne gouverne que les phrases. |
| 16 | porté juste | § 3.6 : le test se fait par genre, à toutes les doses. |
| 17, 18 | portés justes | Verdict 9 et 10. |

## L'ajout du rédacteur : le niveau du mélange

Ce qui est écrit (§ 3.4, K.4) est juste. Avec deux bornes à 2,5 %, le niveau tient à 5 % par réunion. Avec deux bornes à 5 %, la grille ne trouve pas d'erreur au-dessus de 0,048, sans que ce soit prouvé. La note dit justement qu'une grille n'est pas une preuve. La règle par réunion se démontre ainsi, et la note peut l'écrire. Soit x* une répartition optimale de base pour les vrais q, qui emploie au plus deux strates, S* ; elle est fixée par les vrais q et les doses, non par les données. Si la borne de chaque strate de S* reste sous son vrai q, x* reste admissible avec les bornes, car le risque d'y être pris ne peut que baisser. L'optimum écrit vaut alors au moins l'optimum vrai. L'erreur demande donc qu'une des deux bornes de S* dépasse son q, ce qui arrive avec une probabilité d'au plus 2a. Le niveau à 5 % par borne reste sans preuve, et D-12 (a) n'en dépend pas.

## Réserves mineures restantes

| N° | Lieu | Constat | Correction proposée |
|---|---|---|---|
| R1 | D-12 (a) ; § 3.4, « Deux risques, un niveau » | « 1,25 % par borne quand la garantie en dommage emploie deux strates » : si l'on choisit 2,5 % ou 1,25 % après avoir vu combien de strates l'optimum écrit emploie, le niveau n'est plus tenu. Le nombre qui compte est celui de l'optimum vrai, qu'on ne connaît pas. | « Dès que la garantie en dommage est écrite, toutes les bornes de q sont prises à 1,25 %, et ce choix est déclaré avant la lecture ; il ne dépend pas de l'optimum écrit. » |
| R2 | `collisionneur-v2/question-…-v2.md`, lettres C et F | « à quel niveau de confiance d'ensemble » et « un saboteur qui choisit où placer chacun de ses épisodes » orientent vers les constats 2 et 1 (le mélange), sans donner la réponse. C'est léger et légitime comme question, mais la note dit « rien du constat 1 n'y figure ». | Dans le compte rendu de collision, tenir pour orienté l'accord du collisionneur sur le mélange et sur le niveau d'ensemble ; ou retirer « qui choisit où placer chacun de ses épisodes ». |
| R3 | § 3.4 (« Le niveau du mélange ») ; relevé, « Ce que je n'ai pas fait » | « Le niveau du mélange n'est ni démontré ni réfuté » : c'est vrai à 5 % par borne, mais la règle par réunion, elle, est démontrable (ci-dessus). | Ajouter la preuve en trois phrases et écrire : « démontré par réunion à 2,5 % par borne ; non démontré à 5 % par borne ». |

Le couple v2 est neutre sur ce que la consigne vise : il ne nomme pas le programme, ni une personne, ni un chemin interne, et ses publications ne portent plus de leçons. La question pour l'organisme reste en v1, inchangée, et c'est juste. La garde de motifs du collisionneur reste à passer par la mère.
