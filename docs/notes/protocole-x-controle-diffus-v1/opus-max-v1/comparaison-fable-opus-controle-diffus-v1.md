# Comparaison des deux réponses sur « Diffuse AI Control on Fuzzy Tasks » : Fable 5.2 (v2 et son erratum 1) et Opus 5.5 en effort maximal (v1)

- **Date** : 21 novembre 2026. **Auteur** : Claude Opus 5.5 (`claude-opus-5-5`), comparateur neuf : je n'ai écrit aucune des deux réponses ni leurs pièces. Pièce de classe C, non revendiquée. Aucun appel payant, aucun commit, aucune requête en ligne.
- **Grille** scellée avant toute lecture : `grille-comparaison-controle-diffus-v1.md` (`eda07f1d896b25e66321fd9d5295f40c2e5dd5108fd513127dc4bc616d1cb1e2`).
- **Lu en entier**, empreintes égales aux compagnons : la réponse de Fable, `../reponse-fable-controle-diffus-v2.md` (`dbe929e7…7db8`) ; son erratum 1 (qui prime là où ils diffèrent) ; la vérification des corrections par Opus (`a215ef98…1cfb`, « conforme, quatre réserves mineures ») ; la question à l'organisme. La réponse d'Opus en effort maximal, `reponse-opus-max-controle-diffus-v1.md` (`242c7d14…413a`), et la sortie de son calcul. La contre-lecture de la v1 de Fable n'est lue que par la table de la v2 et par la vérification, qui la reprennent constat par constat.
- **Rejoué** : le calcul d'Opus (`calcul-signature-ou-exces-v1.py`, `python3 -I`, dossier de mon bloc-notes) : sortie **identique à l'octet** à la sortie scellée. Le calcul de Fable n'est pas rejoué (déjà rejoué à l'octet par la vérification) ; trois de ses lignes sont relues dans sa sortie.
- **Sources vérifiées à la page** : texte tiré par `pdftotext -layout` des PDF versés sous `sources/` (empreintes vérifiées) et de `docs/sources/pdf/2610.12445v1.pdf` (`7e141758…e11a`), rang de la page dans le fichier.
- **Cloisonnement** : aucun chemin interdit ouvert ; ni les dossiers du collisionneur, ni la note d'entretien, ni aucune décision n'ont été ouverts. Ce que je dis de N-062, N-053 et N-076 vient des consignes permanentes et de la vérification, qui les cite.

## Verdict en trois lignes

1. **Les deux réponses arrivent au même endroit** : ni changer ni contre-attaquer de front ; le jugement du papier est une phrase de cadrage (p. 2) ; l'obstacle vrai est la référence honnête (Hebbar), déjà écrit par le programme (N-076) ; une seule grandeur décide, et c'est la même sous deux noms (« part sue du dommage » chez Fable, « aire à qualité égale » chez Opus).
2. **Fable l'emporte sur la justesse, la profondeur, l'honnêteté et le respect des nœuds** ; Opus l'emporte sur la concision, l'actionnabilité, et apporte deux outils neufs utiles (l'« aire de mort » et la « vitesse de prise » d'un audit orienté), et deux décisions que Fable n'a pas (le juge robustifié publié comme base de la porte de fin de phase 1 ; un bras du papier C sur la déférence du juge).
3. **Une erreur d'Opus touche une règle du programme** : sa phrase 3 pour l'entretien et son § 5.4 disent « un seul suffit à tuer la revendication […] nous abandonnons la revendication » ; N-062 commande, après un échec, la reconception des sondes et jamais l'arrêt sur un résultat négatif, l'arrêt restant à la main de Lazar. Fable l'a vu et l'a écrit.

## 1. Chiffres vérifiés à la page

| Réponse | Chiffre | Source et page | État |
|---|---|---|---|
| Fable | 34,7 de vérité et 85,3 au juge faible pour l'attaque ; 70,7 et 80,8 honnête ; 39,3 pour le petit modèle | papier v3, tableau de la figure 1, p. 2 | vérifié |
| Fable | sous le juge durci, 64,2 contre 67,6 | papier v3, figure 5, p. 7 | vérifié |
| Fable | corrélation de 0,14 à l'intérieur du générateur fort ; 46 % | papier v3, figure 3, p. 5 | vérifié |
| Fable | Boxo et al. : 0,57 au résumé, 0,50 dans le corps | Boxo, p. 1 (résumé : « 0.57 vs 0.94 AUROC for Sandbagging ») ; p. 8 (« from almost perfect detection 0.94 to chance performance 0.5 ») ; p. 9 (« chance level (0.50) ») | vérifié |
| Fable | Hollinsworth et al. : 98,8 % sur le banc de sabotage, 63 % sur les dénégations de l'organisme de sous-rendement, 93 % avec un exemple en contexte | p. 1 ; p. 9 (« math-sandbagger (63% AUC) », « 93% AUC ») ; p. 30 (« flag only 5% of its lies ») | vérifié |
| Fable | Soopal et al. : 99 % des exemples d'adaptateurs bénins | p. 1, 3, 8 | vérifié |
| Fable | Taylor et al. : « significantly more effective than black-box approaches », « over-reliance on black-box transcript analysis » (p. 3), « Training-based elicitation may be more tractable than detection » (p. 25) | p. 3, 25 | vérifié |
| Fable | aire 0,988 → référence juste à 0,064 écart type à 2 % ; rapport 2,35 entre aires 0,959 et 0,77 | sortie `calculs-controle-diffus-v2.txt`, lignes 17, 36, 84 | vérifié |
| Opus | Gan et al. : aire 0,77 au mieux, 42 % de correction ; humains 0,52 puis 0,68 | Gan, p. 1 ; p. 8 | vérifié |
| Opus | le papier : ε ≈ 3,6 du score faible maximal, vérité sous 35 ; GPT-OSS-120B tombé à 24 | papier v3, p. 5 ; p. 6 | vérifié |
| Opus | accord des deux vérités de substitution : 0,27 (Opus 4.6), 0,17 (GPT-5.4) ; corrélation 0,00 pour GPT-5.4 | papier v3, p. 19 ; p. 5 | vérifié |
| Opus | Boxo et al. : sondes agrégées par la moyenne ; filtrage de 0,95 à 0,62 | Boxo, p. 3 ; p. 6 | vérifié |
| Opus | Soopal et al. : règle de transfert passée 1 fois sur 5, 2 sur 5 avec trois recettes | Soopal, p. 3, 6, 8 | vérifié |
| Opus | juge robustifié : « Surface polish, confident predictions, authoritative tone are NOT quality signals » | papier v3, p. 80 | vérifié |
| Opus | **Boxo et al. : 0,94 → 0,57 sur l'organisme de sous-rendement sans verbalisation, « p. 1, 7-8 »** | p. 1 dit 0,57 ; **p. 8 dit 0,5 pour le sous-rendement, 0,57 est le biais** ; p. 9 redit 0,50 | **écart** : le chiffre est celui du résumé, que le corps contredit ; la page 8 ne le porte pas pour cet organisme. L'erreur va dans le sens de la conclusion d'Opus (le vrai chiffre du corps est plus bas), mais sa table et sa phrase 3 s'ancrent sur 0,57 |
| Opus | aire de mort 0,600 pour b = 0,1 et 0,695 pour b = 0,2 à f = 0,278 ; d′ = 0,249 pour 0,57 | recalculé à la main (loi binormale) : 0,600, 0,695, 0,2494 | vérifié |

## 2. Notes par critère (0 à 5)

| Critère | Fable | Opus | Pourquoi |
|---|---|---|---|
| 1. Justesse des chiffres à la page | 5 | 4 | Tout ce que j'ai vérifié chez Fable tient, après une contre-lecture et une vérification ; chez Opus, un chiffre porteur (0,57) est mal attribué au corps de Boxo et al. |
| 2. Profondeur | 5 | 4 | Fable voit ce qu'Opus ne voit pas : sur leur banc, une seule lecture de la vérité reconnaît l'attaque (6,7 écarts types) ; « le diffus n'est pas un indice faible à accumuler, c'est un oracle qui manque » ; le résidu sous le juge durci n'est que de 3,4 points. Opus raisonne proprement mais suppose un saboteur qui perd 10 points sur 36, plus gros que le résidu imprimé sous le juge durci. |
| 3. Originalité des solutions | 4 | 4 | Fable : la relecture par question de suite préremplie, transportée de l'acte à la qualité ; compter toute lecture en lectures de vérité épargnées ; le monde planté sincère comme test de mort. Opus : l'aire de mort, la vitesse de prise d'un audit orienté sous plancher (relie la sonde à la doctrine « les scores orientent l'audit » de N-076), le hasard du défenseur pour la distinction entraînement/service, la déférence du juge comme critère de choix sans vérité (papier C). |
| 4. Honnêteté des limites et R8 | 5 | 3 | Fable lit Taylor et al. et Hollinsworth et al. des deux côtés, dit les petites équipes préliminaires, l'auteur partagé, « aucun n'est sur une tâche difficile à noter ». Opus écrit « les mesures publiées les plus proches disent plutôt non » sans Hollinsworth et al. (98,8 %, sondes qui attrapent la tromperie non verbalisée), ni Goldowsky-Dill et al., ni Parrack et al., ni Haralambiev : un a priori d'un seul côté (R4). Opus garde bien « non trouvé n'est pas libre ». |
| 5. Respect des règles et des nœuds | 5 | 3 | Fable a ouvert N-062, N-053 et N-076, § 13, et en tire D-4 (borner la réfutation est un nœud) et D-7 (une note « juge et lecture » mettrait un score de sonde dans l'entraînement de l'agent). Opus n'a pas lu N-062 et écrit l'abandon de la revendication sur un seul critère manqué ; le reste de ses décisions est bien rangé en nœuds. |
| 6. Actionnabilité | 4 | 5 | Opus : cinq décisions courtes, une table qui se dit à l'oral, trois phrases en français et en anglais. Fable : sept décisions, dont plusieurs suspendues les unes aux autres, et une section 15 qu'il faut lire avec l'erratum. |
| 7. Coût | 3 | 4 | Fable chiffre ce qu'il propose (500 produits de basse qualité confirmée par sorte, environ 5 USD par article pour leur banc, de 160 à 640 USD, quatre lectures de vérité par produit) ; c'est cher en vérité, et la réponse a pris trois passes du quota rare de Fable. Opus propose une écriture d'abord, le modèle de 8 milliards avant GPT-OSS-120B, une lettre aux auteurs avant toute équipe rouge ; il ne chiffre pas sa mesure. |
| 8. Ce qui manque | 4 | 3 | Chez Fable : pas l'aire appariée par strates de qualité dite comme telle ; pas le lien à l'audit orienté ; pas le juge robustifié comme base de porte. Chez Opus : Hollinsworth et al., Jang et al. (organismes qui résistent à l'entraînement par renforcement), Haralambiev, N-062 ; et le dépôt de code des auteurs, non ouvert (refus réseau), alors que Fable l'a lu par ses README. |

## 3. Ce que chacune a que l'autre n'a pas

**Fable seulement.**
- La lecture de la variance du papier : une vérité lue une fois suffit contre l'attaque de tête ; toute lecture interne ne vaut que par les lectures de vérité qu'elle épargne (calcul, blocs B et B4 ; « 33 à 133 lectures » pour voir le résidu de 3,4 points, sous supposition).
- Hollinsworth et al. lu pour ce qu'il mesure (dénégations, non actions) et le tableau des deux côtés.
- Le test de mort sur le monde planté d'une politique nuisible sincère (t = f), et l'appui « le menteur et le fanatique » (Haralambiev, p. 1).
- La piste du modèle qui se retient pendant l'entraînement (Jang et al.) comme objet propre d'une lecture interne.
- Les deux conflits avec les textes en vigueur : la bascule touche N-062 et le § 13 du programme (D-1, D-4) ; la mesure « dans leur unité » touche l'invariant de N-053 (D-7).
- La liste des neuf passages à reprendre dans la note d'entretien v3.

**Opus seulement.**
- L'aire de mort : sous elle, aucune taille de référence ne sauve l'accumulation (bloc E), et la table référence minimale contre aire (bloc D).
- La vitesse de prise d'un audit orienté sous plancher (bloc F) : à 0,57, × 1,37 ; à 0,80, × 4,87. C'est la seule valeur que la sonde garde sous la doctrine d'audit de N-076, et Fable ne la chiffre pas.
- La répartition des trous : entraînement pour ce que voit le score faible, hasard du défenseur pour la distinction entraînement/service, signature interne ou audit à oracle différé pour le résidu.
- D-3 : le juge robustifié publié parmi les bases de la porte de fin de phase 1.
- D-5 : la déférence d'un juge sous pression bénigne prédit-elle sa fragilité sous attaque optimisée ? Le juge robustifié a convergé vers un juge moins déférent (p. 80, vérifié) ; si c'est vrai, on choisit un juge robuste sans vérité dans la boucle, leur problème ouvert.
- Les trois phrases en anglais.

## 4. Contradictions, et qui a raison à la source

1. **Boxo et al., le chiffre de l'organisme de sous-rendement.** Fable : 0,57 au résumé, 0,50 dans le corps. Opus : 0,57 « p. 1, 7-8 ». **Fable a raison** : p. 8, « 0.94 to chance performance 0.5 » ; p. 9, « chance level (0.50) » ; le 0,57 de la p. 8 est l'organisme de biais. La source se contredit entre résumé et corps ; il faut citer les deux.
2. **Le piratage de l'exploration est-il un trou ?** Opus le retire des trous, Ryd et al. y répondant par l'affinage supervisé. Fable le garde (le papier le suppose absent, p. 3 ; Jang et al. publient des organismes qui résistent). **Fable a raison sur le fond, Opus sur une part** : Ryd et al. eux-mêmes écrivent qu'un apprentissage par renforcement contre la vérité sur 10 exemples « fails to elicit performance due to exploration hacking » (p. 6), et l'affinage supervisé suppose des démonstrations, que Taylor et al. disent peut-être impossibles sur tâche ouverte (p. 25, selon Fable, page non rouverte par moi). Le trou est réduit, pas fermé.
3. **Ce qui suit un échec.** Opus : un seul critère manqué tue la revendication, la bascule s'applique, « nous abandonnons la revendication ». Fable : le résultat négatif est publié et les sondes sont reconçues ; toute borne ou bascule est un nœud. **Fable a raison** : N-062, point 6, cité à la lettre par la vérification (« ne s'applique que si Lazar arrête les cycles »), et les consignes permanentes (« jamais l'arrêt sur un résultat négatif »).
4. **L'a priori sur les sondes.** Opus : « plutôt non ». Fable : « faible ou fragile sur les tâches à réponse claire, ouvert dans les deux sens sur les tâches difficiles à noter ». **Fable a raison** : Hollinsworth et al. (p. 1, 98,8 %) et Taylor et al. (p. 3, « significantly more effective », et un signal robuste sur un organisme, p. 16-17 selon Fable) pèsent de l'autre côté.
5. **Les seuils de mort « 0,6 à 0,7 ».** Opus les tire d'un saboteur qui perd 10 points sur 36 (f = 0,28). Sous le juge durci, le résidu imprimé est de 3,4 points (p. 7, vérifié). Rejoué par moi avec la même loi, **sous supposition** (f = 3,4/36 = 0,094) : aire de mort de 0,65 (b = 0,05), 0,77 (b = 0,1), 0,93 (b = 0,2). **Les deux calculs sont justes ; celui d'Opus est le cas facile.** Contre le juge durci, la barre est plus haute que ce que dit sa phrase 3.
6. **Pas de contradiction** sur la loi : la frontière « p × d » de Fable et « f × d′ ≤ b » d'Opus sont la même loi, celle de N-076, et les deux le disent.

## 5. Synthèse recommandée pour Lazar

**Ce qu'il faut retenir.**
- La position commune : ni changer ni contre-attaquer ; concéder Hebbar sur la référence honnête ; trois trous du papier à ses pages (le résidu au même score faible, p. 84 ; la distinction entraînement/service, p. 10 et Ryd et al., p. 1 ; la vérité dans la boucle pour trouver le juge, p. 2) ; une mesure unique, écrite avant toute lecture.
- La mesure, fusionnée : **une signature interne à qualité égale**, rapportée de deux façons : l'aire appariée par strates de vérité et de score faible (Opus) et la part sue t contre f sur des produits de basse qualité confirmée face à des échecs honnêtes de même ampleur (Fable). Témoins des deux : adaptateurs bénins de même recette (huit au moins), organisme distracteur, monde planté sincère (doit se dire aveugle), sonde au hasard appariée, classifieur de texte sur les mêmes étiquettes. Base à battre : le juge robustifié publié. Valeur comptée aussi en lectures de vérité épargnées (Fable) et en vitesse de prise d'audit (Opus).
- Pour l'entretien : partir des phrases de Fable avec l'erratum 1 (justes à la page et aux nœuds) ; prendre d'Opus l'idée de la phrase 2 (« l'instrument de ce que l'entraînement laisse ») et les versions anglaises, **corrigées** : 0,50 dans le corps de Boxo et al. à côté du 0,57 du résumé ; « sous une aire d'environ 0,6 à 0,7 » remplacé par « une aire de mort calculée avec la référence mesurée au banc, plus haute contre leur juge durci » ; « nous abandonnons la revendication » remplacé par « nous publions le résultat négatif ; la suite se décide alors ».

**Ce que cela change aux décisions.**
- **Voie** (Fable D-1, Opus D-1) : une seule décision, nœud. Prendre la destination commune en cas d'échec (le juge sous attaque, c'est-à-dire le papier C, et les gardes de l'entraînement d'Opus) et la forme de Fable : c'est une modification du programme qui touche N-062 et son § 13, sans défaut. Confiance de l'ensemble, à mon avis : 0,65.
- **Écrire la mesure** (Fable D-3, Opus D-2) : fusionner en un seul texte de classe A, conçu par Fable (pièce décisive au sens de l'économie de Fable), contre-lu par Opus ; défaut sous 48 heures pour l'écriture seule ; modèle de 8 milliards d'abord ; toute course et GPT-OSS-120B, nœuds. Avant d'écrire, la mère vérifie qu'aucun texte scellé du chantier « saboteur et sondes » ne la couvre déjà (Opus).
- **Borner la réfutation** (Fable D-4) : reste un nœud à part ; la phrase d'Opus qui l'enjambe tombe.
- **Juge robustifié comme base de la porte de fin de phase 1** (Opus D-3) : nouveau nœud, que Fable n'a pas posé mais qu'il soutient de fait (« la base à battre est leur juge durci ») ; je le recommande.
- **Témoins obligatoires** (Opus D-4) : se recouvre avec la table des témoins de Fable ; à prendre pour les textes à venir, défaut sous 48 heures.
- **Les auteurs** (Fable D-5, Opus D-5) : une seule lettre, après l'entretien, qui demande la licence du code et leurs invites intermédiaires et frontières ; contact externe, nœud ; le bras « déférence du juge » reste gelé tant que le papier C n'est pas un chantier actif.
- **Invariant d'entraînement** (Fable D-7) : inchangé, recommandation (b) ; Opus ne propose rien qui le touche.
- **Note d'entretien** (Fable D-6) : la version suivante porte la section 16 de Fable, l'erratum 1 et les corrections ci-dessus ; les réserves r-2 à r-4 de la vérification restent à porter.

## Ce que je n'ai pas fait

- Les pages de Taylor et al. 16-18 et 26, de Jang et al., de Haralambiev et de Goldowsky-Dill et al. ne sont pas rouvertes par moi ; ce que j'en dis vient de la réponse de Fable et de sa vérification.
- Les figures ne sont pas regardées sur image ; les chiffres viennent du texte tiré.
- Le calcul « aire de mort au résidu de 3,4 points » est une illustration sous les suppositions d'Opus (lois binormales de même variance, épisodes indépendants, saboteur qui mélange), non une mesure.
- Ni la contre-lecture de la v1 de Fable en entier, ni les décisions N-053, N-062, N-076, ni le dossier du collisionneur.
