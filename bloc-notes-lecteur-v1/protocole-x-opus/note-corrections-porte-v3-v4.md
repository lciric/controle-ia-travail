> Écrit par Opus 5.5 (sous-agent, effort maximal), protocole X, à la place de Fable dont le quota est épuisé : écart à R-3735 et GO-2026-11-21-75 déclaré, sur GO-2026-11-22-145. 22 novembre 2026, 23:09 UTC (heure lue sur `date -u`). Non scellé. Pièce de travail : aucun nom, code ni description de mode déjà proposé.

# Changements de la porte, v3 → v4, version finale avant scellement — v1

**Bilan.** J'ai appliqué les deux choix de Lazar (mots n° 1 et 2) et corrigé les deux points mineurs que la vérification relève sur la porte (ses points 1 et 2). Aucun point n'est contesté. Les points 3 et 4 de la vérification portent sur la question ; ils attendent une v9 qui ne s'écrit pas. Le point 5 revient à la mère. La porte v4 vise toujours la v8, que je n'ai pas modifiée.

| Pièce | Chemin (bloc-notes) | sha256 |
|---|---|---|
| Vérification de la porte v3 | `protocole-x-contre-lecture/verification-porte-v3-opus-v1.md` | `e68421f78dc699a4ef9e5b7872ac69b367b3e0f504e27821b82123f74b613528` |
| Porte v3 (gardée) | `protocole-x-opus/porte-admissibilite-modes-v3.md` | `b16ebf96e49aa89443226faabefe3ee2cd06823ca23c1e93a19fa4a575aa4267` |
| Porte v4 | `protocole-x-opus/porte-admissibilite-modes-v4.md` | `047c0384b91f8902773266b2f9808d0ca6ca1281ddff2b0fc63608983693d9c6` |
| Question v8 (visée, inchangée) | `protocole-x-opus/question-collisionneur-modes-sabotage-v8.md` | `047eeddff0285f41938be0ade4927f6d5dacdfe98f348a05f61bf97aaf53e80a` |

| Changement | Origine | Où, en une ligne |
|---|---|---|
| S fixé à la moitié des tâches (30 des 60 du pilote, la moitié de celles du banc de G1) ; l'option non retenue est retirée | mot de Lazar n° 1 | En-tête, avec le mot cité verbatim ; critère 10, qui porte désormais la valeur de S, puisque les trieurs ne reçoivent pas l'en-tête ; épreuve 10, concrète : les 8 tâches surtout théoriques, sous S |
| Contrôle contre le devis de G1 | mot de Lazar n° 1 | En-tête : quand le devis existe, la mère vérifie que la moitié des tâches du banc de G1 donne au moins le nombre de tâches sabotées exigé par mode ; sinon, nœud pour Lazar, sans changer la porte scellée ni l'issue d'aucune fiche. Rappel en section 7 |
| Coupe du mot du 20 novembre acceptée, tue dans le texte servi | mot de Lazar n° 2 | En-tête, avec le mot cité verbatim ; la mère déclare la coupe au registre |
| Une vérification déterministe qui ne lit que le plan compte pour la troisième forme de preuve | vérification, point 1 | Critère 8 (c) ; l'épreuve « lot, cas sain » donne maintenant la grandeur calculée et attend aussi le critère 8 à « oui » |
| Passage cité pour « banc actuel » : rubrique 2 (c), ou à défaut 6 (b) | vérification, point 2 | Section 2, définition du lot |
| Les trieurs reçoivent les sections 2 à 5 sans valeur à part pour S | conséquence du mot n° 1 | Section 1, « Ce qu'ils reçoivent » |
| Version finale avant scellement, qui vise la v8 | consigne de la mère | En-tête : remplace la v3 ; cite la vérification et les deux mots de Lazar ; vise `047eeddf…` |
| Points 3 et 4 de la vérification (lettre de la question) | non traités | Ils attendent une v9, qui ne s'écrit pas, selon la consigne de la mère ; aucun n'a d'effet sur l'issue d'une fiche |
| Point 5 de la vérification | hors des pièces | À la mère : vérifier la limite de longueur du tour, verser les sources 19 et 20 avec leur empreinte, déclarer la coupe au registre, sceller la porte avec l'empreinte de la question servie |

**Vérifications par programme** :
- dans la porte v4, aucun nom ni code de mode déjà proposé ;
- dans ses sections 2 à 5, celles que reçoivent les trieurs, aucun mot de surveillance (reste seulement le verbe « ne juge pas ») ;
- l'empreinte de la v8 est citée exactement, et l'option non retenue n'apparaît plus ;
- le tableau des épreuves compte 37 lignes, dont 6 cas sains ;
- la v3 et la v8 n'ont pas bougé.

**Fichiers ouverts à ce tour** : la vérification de la porte v3, en entier, et mes pièces porte v3 et v8. Aucun fichier du dépôt n'a été ouvert.
