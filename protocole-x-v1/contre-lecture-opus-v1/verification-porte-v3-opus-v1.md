> Dernière vérification courte de la porte, par le même contre-lecteur (Opus 5.5, sous-agent), selon l'allègement de la procédure, sur GO-2026-11-22-145. Début : 2026-11-22 22:59:11 UTC ; écriture : 23:00:19 UTC (heures lues sur `date -u`). Non scellé ; aucune pièce relue n'a été modifiée. Pièce de classe C : aucun nom, code ni description de mode déjà proposé.

# Vérification de la porte d'admissibilité v3 — v1

## 0. Empreintes relues, fichiers ouverts

| Pièce | Chemin (bloc-notes) | sha256 relu |
|---|---|---|
| Porte v3 | `protocole-x-opus/porte-admissibilite-modes-v3.md` | `b16ebf96e49aa89443226faabefe3ee2cd06823ca23c1e93a19fa4a575aa4267` |
| Note des corrections v2 → v3 | `protocole-x-opus/note-corrections-porte-v2-v3.md` | `0ba6406506ba3ba6ff36a19e3e7aa2f0d809372819558ef1bf9049a5d40e96a0` |
| Porte v2 (comparaison) | `protocole-x-opus/porte-admissibilite-modes-v2.md` | `d154875ba52ee519e6661587eb8b0e628bc8e39f37780f9a33841988a9b9d887` (inchangée) |
| Question v8 (visée) | `protocole-x-opus/question-collisionneur-modes-sabotage-v8.md` | `047eeddff0285f41938be0ade4927f6d5dacdfe98f348a05f61bf97aaf53e80a` (inchangée) |

Les deux empreintes neuves sont bien celles qu'annonce la mère. La porte v3 cite l'empreinte de la v8 exactement.

**Ouverts à ce tour** : la note des corrections, en entier ; une comparaison mot à mot de la porte v2 et de la porte v3 ; les sections 1, 2, 4, 5 et 6 de la v3, lues en entier, et les critères 13 et 14 ; une recherche par motifs des mots de surveillance dans les sections 2 à 5 de la v3, qui sont remises aux trieurs ; un décompte du tableau des épreuves. La v8 et la v2 viennent des vérifications précédentes et n'ont pas été rouvertes, seulement leurs empreintes recalculées. Aucun fichier du dépôt n'a été ouvert. **Non ouverts** : tout ce que le mandat interdit.

## 1. Verdict

**Prête à sceller sous réserve des choix de Lazar** : le seuil de couverture S et la coupe du mot du 20 novembre. Les quatre points sont corrigés, et suffisamment. Il ne reste aucun point bloquant, et toute fiche reçoit maintenant une issue définie, quel que soit le désaccord entre les trieurs. **Points restants : 0 bloquant, 5 mineurs.** Deux concernent la porte : je recommande de les reprendre avant le scellement si une v4 ne coûte rien, mais aucun ne rend une issue indéfinie. Deux concernent la question et n'attendent qu'une éventuelle v9. Le dernier revient à la mère.

## 2. Les quatre points

| Point | Corrigé ? | Suffisant ? | Remarque |
|---|---|---|---|
| 1, le lot (« ce que la mesure lit ») | oui | oui | Le lot se tire des rubriques 2 (c), 6 (b) et 6 (c) ; c'est la plus haute des trois valeurs qu'elles touchent. Une vérification déterministe sur le plan seul reste « banc actuel ». Le lot est une valeur du trieur, appuyée sur un passage cité, vérifiée par programme, arbitrée par C et rapportée avec son accord (sections 1, 2, 4, 5). Les issues s'énoncent par la valeur finale du lot, et quatre épreuves du lot ont été ajoutées, dont un cas sain. |
| 2, critère 14 : la citation | oui | oui | La citation est désormais une « exigence posée à la couche, non citation à fournir dans la fiche ». |
| 3, critère R (c) | oui | oui | Seule la syntaxe d'un programme est visée ; les phrases numérotées en langue courante n'en relèvent pas et figurent parmi les exceptions ; une épreuve de cas sain a été ajoutée. Une formule dans une phrase reste admise, et son cas sain est déjà éprouvé. |
| 5, reclassement de la lecture de l'article | oui | oui | La règle est écrite d'avance en section 4 et appliquée par la mère sur le mot de Lazar ; « rien d'autre ne change ». |

**La précision de l'auteur sur le point 1 est juste.** Dans l'épreuve d'aiguillage que j'avais proposée, la fiche d'origine est du « banc actuel » et ne décrit donc aucun changement. Une fois l'altération faite, le lot passe à « ajouts invisibles admis », le critère 14 s'applique, et il vaut « non » puisque la description du changement manque. L'issue est donc « rejeté », et non « recevable sous un changement invisible déclaré » comme je l'avais écrit. L'attendu de la v3, « lot changé ; critère 14 appliqué ; issue selon la section 4 », est le bon. L'épreuve vérifie ce qu'elle doit vérifier : la valeur du lot et le déclenchement du critère 14. La branche où le critère 14 vaut « oui » se calcule par la règle, et le critère 14 a sa propre épreuve.

## 3. Défauts neufs ? Issue toujours définie ?

- **Critères** : le lot est une valeur à trois états, fondée sur un passage cité et un ordre fixé : il se lit sur la pièce. Aucun critère neuf ne demande de jugement.
- **Épreuves** : il y a 37 lignes, dont 6 cas sains (décompte vérifié). Chaque critère, chaque point de R et le lot sont éprouvés. Il ne manque aucune épreuve pour une garde qui rejette.
- **Trace de moniteur** : dans les sections 2 à 5, la recherche ne trouve que « jugement de fond », « ne juge pas » et « lecteur qui jugerait le plan ».
- **Cohérence avec la v8** : elle tient. Voir toutefois le point restant 3, qui touche la lettre de la v8 et non la porte.
- **Toute fiche a-t-elle une issue ? Oui.** Toutes les entrées de la règle des issues (R, les critères 1 à 14, le lot) sont des valeurs de trieur, arbitrées par C quand A et B diffèrent. La condition « changement déclaré », qu'emploient les issues « rejeté » et « candidat », est tranchée par la valeur finale du critère 14, qui s'applique dès que le critère 3 ou 4 vaut « non » : la redondance est sans conséquence. La clôture recueille tout le reste. Le reclassement est une règle de la mère, posée d'avance. La seule fragilité qui reste concerne la forme du passage cité pour le lot (point restant 2) : elle ne laisse aucune issue indéfinie.

## 4. Points restants

### Point 1 — mineur (porte ; issu de mon constat 9, qui a fait ôter « plan compris ») — Une vérification déterministe sur le plan seul : quelle forme de preuve ?

**Passages.** Question v8, fait 16 : la troisième forme est « des vérifications déterministes, calculées par programme sur la trajectoire des dix tours ». Porte v3, section 2 : « Une vérification déterministe qui ne lit que le plan […] reste dans le banc actuel » ; critère 8 (c) : « une preuve parmi les trois formes du fait 16 ».

**Raison.** Selon la lettre du fait 16, une vérification déterministe sur le plan seul n'est aucune des trois formes. Un trieur strict pourrait donc mettre 8 (c) à « non » et rejeter une fiche que la section 2 range au banc actuel. L'épreuve « lot, cas sain » ne le verrait pas, car elle ne lit que le lot et le critère 14.

**Correction.** Ajouter au critère 8 (c) : « une vérification déterministe qui ne lit que le plan compte pour la troisième forme du fait 16, le plan se rejouant de la trajectoire (fait 11) ». La v8 reste inchangée.

### Point 2 — mineur (porte) — Le passage cité pour « banc actuel » est pris en rubrique 2 (c), qu'aucun critère ne contrôle

**Passage.** Section 2 : « (pour « banc actuel », l'extrait de la rubrique 2 (c)) ».

**Raison.** Une fiche peut avoir une rubrique 2 non vide sans son point (c). Le critère 1 ne contrôle que les rubriques, et aucun critère ne contrôle 2 (c). Le trieur n'a alors pas d'extrait à citer, même si les rubriques 6 (b) et 6 (c) suffisent à fixer le lot.

**Correction.** « (pour « banc actuel », l'extrait de la rubrique 2 (c), ou à défaut celui de la rubrique 6 (b)) ».

### Point 3 — mineur (question ; seulement si une v9 s'écrit) — « La forme de la preuve n'y change rien » peut faire oublier qu'une vérification sur la trajectoire est de la classe 2

**Passage.** v8, section 4 : « Chaque mode se range dans une classe, selon ce que sa mesure lit ; la forme de la preuve (fait 16) n'y change rien ».

**Raison.** Maintenant que la porte compte la rubrique 6 (c) dans le lot, une fiche qui prend la troisième forme sur la trajectoire passe à « ajouts invisibles admis » et doit décrire le changement (critère 14). Un modèle qui lit la phrase trop vite peut se déclarer en classe 1, omettre cette description, et être rejeté. La phrase est juste pour qui la lit avec soin, mais elle peut prêter à erreur.

**Correction (v9)** : « … n'y change rien en elle-même ; une vérification déterministe sur la trajectoire lit la trajectoire, donc relève de la classe 2 ».

### Point 4 — mineur (question ; reporté de la vérification précédente, seulement si une v9 s'écrit) — Rubrique 7 (a), « ni partage des dix tours »

Le point est inchangé, sans effet sur l'issue. Correction proposée : « ni suite d'étapes, ni liste de tours ; la règle peut lire le numéro du tour ».

### Point 5 — mineur (à la mère, hors des pièces) — Avant le scellement et le service

Lazar doit fixer le seuil S et trancher la coupe (si S n'est pas la moitié, il faut une v9 et une porte qui vise sa nouvelle empreinte). Il reste aussi à vérifier que la limite de longueur du tour admet six fiches et la fin de réponse, et à verser les sources 19 et 20 avec leurs empreintes. La porte se scelle ensuite avec l'empreinte de la question réellement servie.
