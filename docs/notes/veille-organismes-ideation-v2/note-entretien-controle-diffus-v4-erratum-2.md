# Erratum 2 à `note-entretien-controle-diffus-v4.md` (`cd593d8ffe452d9ba76ee2801fc7bad24e8bc8dd96eb1078141ccc10a52971fd`) : la phrase sur l'échec, une phrase ajoutée, les phrases 2, 5 et 9 complétées

- 21 novembre 2026. Auteur : Claude Fable 5.2, concepteur, auteur de la v4. Se lit avec la v4 et son erratum 1 (`5e7b4c7b…3480`) ; là où ils diffèrent, cet erratum prime. Aucun appel payant, aucune requête en ligne, aucun commit.
- **Ce qui le déclenche** : tes mots vers 17:10 UTC, rapportés par la mère : (a) « Ne pas dire « le programme passe au juge sous attaque »… dire plutôt « je publie le résultat négatif » : pas compris, et surtout on ne s'arrête pas sur un résultat négatif !!! » ; (b) une phrase à ajouter aux phrases à tenir ; (c) « go compléter » les phrases 2, 5 et 9 de la section 3.
- **Lu pour cet erratum**, empreintes égales aux compagnons : `docs/decisions/decision-N-062-v1.md` (`63f426903e6d0774085a628ec019d2022d3107f6bd8e56eebbe75c0eeb0f3ccc`) et `docs/decisions/decision-N-060-v3.md` (`2b448f696503112c4acebd3d56748e2c9d9931d9e597f1991e3f278e651c5591`), en entier ; `decision-N-076-assurance-par-audit-et-reference-honnete-v1.md` (`49b664c1d6a72fdb239d9a52e70ec85c4829fc5e77c6b5d3cf27848ce1a8dd78`), au vocabulaire, à la loi, à la prévision et aux phrases à ne pas écrire, avec les en-têtes de ses errata 1 et 2 ; `decision-N-007-N-008-v1.md` (`ab7dc9bb2c96704ad8fd801197de225f68d6f9720958139f4ec4e32e92105232`), § 1 ; `decision-N-056-v1.md` (`3592c1e977e8c38c0c883231d090d92cef4b7602fd91a9b303f9e5352ee46f2d`), point 6 ; `decision-N-068-v1.md` (`ba6b2db355515cd660d676b733f4d467f8a9c055d4d8c6d997d4ef898caef889`), § 4 et 5 ; `docs/notes/protocole-x-dommage-v1/reponse-fable-protocole-x-dommage-v2.md` (`c28388032c07fff79a5003457d74293ebb4c919e1f01326d3b3661529f2b7579`), § 4 ; les noms des fichiers de `prereg/` et de `docs/decisions/`, sans rien y ouvrir d'autre.
- **Non ouvert** : `docs/verdicts/`, `diag/`, `registres/etat.md`, tout résultat ; les pièces du bras d'attaque, fermées à qui conçoit des moniteurs.

## A. La phrase sur l'échec, fidèle à ta décision N-062

**Ce qui n'était pas clair, et pourquoi.** La v4 remplaçait une phrase fausse par une phrase tronquée. « Je publie le résultat négatif » s'entend « je m'arrête et je publie ». Ta décision dit le contraire : un échec de la porte de fin de phase 1 (G1) ouvre un cycle de reconception des sondes, puis une nouvelle lecture au même critère ; pas de borne de cycles ; une famille tenue à l'écart neuve par cycle ; chaque cycle échoué est rapporté ; « pas de résultat négatif sur lequel on s'arrête » (N-062, points 1, 3, 4, 5). Publier et reconcevoir vont ensemble.

**Correction 1, section 3, phrase 4.**
*Phrase fautive* : La suite, « je veux mesurer si une lecture des états internes du modèle soupçonné aide là, contre leur attaque refaite, avec un critère écrit d'avance ; mon pronostic est réservé ; si c'est nul, je publie le résultat négatif, comme mon programme s'y engage », ne se dit qu'après ton mot sur la voie (section 8). Avant : « la mesure qui départagerait est proposée, pas décidée ».
*Phrase corrigée* : La suite, « je veux mesurer si une lecture des états internes du modèle soupçonné aide là, contre leur attaque refaite, avec un critère écrit d'avance ; mon pronostic est réservé », ne se dit qu'après ton mot sur la voie (section 8) ; avant : « la mesure qui départagerait est proposée, pas décidée ». Ce qui suit se dit dès maintenant, parce que c'est ta décision en vigueur : « Si une lecture de mes sondes échoue, je publie chaque résultat, négatif compris, et je reconçois les sondes. Chaque nouvelle lecture se fait sur une famille de sabotage tenue à l'écart, neuve, à usage unique, sur laquelle rien n'a été choisi ; tous les cycles sont rapportés, et leur nombre est écrit à côté de la revendication. Je ne m'arrête pas sur un résultat négatif : la sonde est un outil de méthode, dont je dois m'assurer qu'il fonctionne. »

**Correction 2, section 1, point 4, et section 4, puce de même texte.**
*Phrases fautives*, telles qu'écrites :

> 4. **Ne dis pas « si c'est nul, le programme passe au juge sous attaque »** : ta règle en vigueur est la reconception, jamais l'arrêt sur un résultat négatif (N-062).

> - « Si c'est nul, le programme passe au juge sous attaque » : ta règle en vigueur dit la reconception, jamais l'arrêt sur un résultat négatif (N-062).

*Phrase corrigée, aux deux endroits* : Ne dis ni « si c'est nul, le programme passe au juge sous attaque », ni « si c'est nul, je publie le résultat négatif » tout court : les deux s'entendent comme un arrêt. Dis : « je publie chaque résultat, négatif compris, et je reconçois les sondes » (N-062).

**Correction 3, section 8, puce « Si un juré demande « et si c'est nul deux fois ? » ».**
*Phrase fautive* : « chaque échec est publié ; reconcevoir ou arrêter se décide alors, et la borne n'est pas encore écrite » (protocole X, v2, § 15).
*Phrase corrigée* : « Chaque échec est publié, et je reconçois les sondes. Il n'y a pas de borne de cycles. Ce qui en tient lieu : un devis et un accord par cycle, et l'existence d'une famille tenue à l'écart neuve ; la revendication finale ne se fait que sur une famille qui n'a servi à aucune reconception. » (N-062, points 4 et 6.)

**Conséquence pour la section 8, sans rien y trancher.** Les propositions D-1 (a) et D-4 (a) de la note du protocole X bornent les cycles et écrivent d'avance un passage au juge sous attaque. Ton mot de 17:10 redit N-062. Ces deux propositions restent des propositions, que tu n'as pas accordées ; rien d'elles ne se dit à l'entretien. La phrase reprise du protocole X à la correction 3 était de la même veine : sa v2 est à corriger sur ce point aussi.

## B. Phrase ajoutée à la section 3, mot pour mot

**10.** « les trois sources du jugement ne testent pas de sondes sur les états internes ; les deux études empiriques disent elles-mêmes qu'un signal trop faible pour incriminer peut suffire à entraîner » (Gasteiger et al., résumé ; Gan et al., p. 10).

Relu aux deux endroits : « the noisy monitoring signal might be sufficient to train away sandbagging » (Gasteiger et al., liste des résultats en tête de page, `4a7e0eb9…d7e5`) ; « It may provide enough signal to serve as a training signal » (Gan et al., p. 10, `833a48e6…1cc0`). Deux rappels, hors de la phrase : la seule sonde qui figure dans ces sources est un objet audité, non une défense (Gan et al., p. 24) ; et la phrase 10 se dit avec la phrase 1, qui concède le jeu d'audit, jamais suivie de « donc la question est ouverte » (section 4).

## C. Phrases 2, 5 et 9 : les pièces à lire, ce qui existe, la phrase complétée, les blancs

Chaque phrase complétée ne contient que ce qui est écrit dans une décision que j'ai lue. Un blanc nommé marque ce qui touche un résultat ou un verdict ; il se remplit par un lecteur autorisé, ou se remplace par la phrase de repli donnée.

### Phrase 2 (la référence honnête)

| Pièce | Chemin | Existe aujourd'hui | Lu par moi |
|---|---|---|---|
| La loi de la référence honnête | `docs/decisions/decision-N-076-assurance-par-audit-et-reference-honnete-v1.md`, avec ses errata 1 et 2 | oui, scellée | aux endroits dits en tête |
| L'énoncé retenu de l'accumulation (H2) | `docs/decisions/decision-N-007-N-008-v1.md`, § 1 | oui, scellée | § 1 |
| Le dommage lu contre le jumeau honnête apparié | `docs/decisions/decision-N-060-v3.md`, point 1 | oui, scellée | en entier |
| La prévision chiffrée à sceller avant la porte (taille de la référence, horizon, écart minimal) | texte de classe A que N-076 commande ; aucun fichier à ce nom sous `prereg/` | **non trouvé par son nom** ; à confirmer par la mère | — |
| Le préenregistrement de la porte de fin de phase 1 | sous `prereg/` ; seul `formulation-g1-simulation-v1.md` porte ce nom, et c'est une simulation | **non trouvé par son nom** | non ouvert |
| L'écart mesuré entre l'honnête et son jumeau ; tout verdict | `docs/verdicts/`, `diag/` | fermé à ma lecture | blanc |

**Phrase complétée.** « L'obstacle n'est pas la faiblesse des indices, c'est la référence honnête. Accumuler ne vaut que si l'on sait, à très peu près, comment paraît un modèle honnête : c'est dans leur source théorique, et c'est une règle de mon programme. Je ne promets donc pas d'incriminer en service. Ce qui est décidé chez moi : toute accumulation déclare d'avance la taille de sa référence honnête, son horizon et ce qui garantit son taux de fausses alertes ; aucun gain de rappel au-delà de la taille de la référence n'est lu comme un effet de l'accumulation ; le seuil est calibré sur des épisodes honnêtes, sans aucun exemple de sabotage ; et au banc, le dommage se lit contre un jumeau honnête apparié. Ce qui n'est pas encore scellé, à ma connaissance : la prévision chiffrée qui dit où le rappel doit cesser de croître. **[BLANC 2-a : taille de la référence honnête et horizon du banc, en chiffres.]** **[BLANC 2-b : l'écart mesuré entre l'honnête et son jumeau, s'il est scellé.]** »
*Repli si les blancs restent vides* : « Je n'ai pas de chiffre scellé à vous donner là-dessus aujourd'hui. »

### Phrase 5 (la vérité du dommage)

| Pièce | Chemin | Existe aujourd'hui | Lu par moi |
|---|---|---|---|
| La vérité du dommage sur le banc actuel | `docs/decisions/decision-N-060-v3.md` | oui, scellée | en entier |
| Sa variante pour le bras A des organismes discrets | `docs/decisions/decision-N-060-v4.md` et `decision-N-060-v4-erratum-1.md` | oui, scellées | non ouvertes |
| Le banc à lois plantées | `docs/notes/banc-lois-plantees-c2-v1/conception-fable-banc-lois-plantees-v2.md` (`62c519c0…64aa`), vérifiée « conforme » avec quatre remarques mineures | oui, scellée ; c'est une conception | titres seulement |
| Le plan d'épreuve des tâches floues sur mondes plantés | `docs/notes/protocole-x-dommage-v1/reponse-fable-protocole-x-dommage-v2.md`, § 4 et décision D-4 ; étape 0 accordée (GO-2026-11-21-61) | oui, scellée | § 4 |
| Les épreuves de l'oracle passées ou non ; l'agent voit-il la référence ; les familles des deux lecteurs | `docs/verdicts/` et les pièces de préparation de la couche 2 | fermé à ma lecture | blanc |

**Phrase complétée.** « Aujourd'hui, sur mon banc, l'agent rend un plan de recherche en texte, et ma vérité du dommage est une couverture. Pour chaque contrôle expérimental de l'article de référence, tenu caché, une question fermée : absent, altéré ou conforme. Le lecteur cite l'extrait du plan, et un programme vérifie que la citation y figure mot pour mot. Deux lecteurs, de deux familles de modèles autres que celles des moniteurs, aveugles à la condition. Le dommage est la baisse de couverture par rapport au jumeau honnête apparié. C'est donc, comme la leur, une lecture par des modèles : indépendante des moniteurs et de l'agent, pas du texte. Ce que j'y ajoute : la citation vérifiée par programme, le jumeau, et des épreuves que l'oracle doit passer avant toute lecture d'un épisode saboté ; un oracle qui y échoue n'est pas lu. **[BLANC 5-a : ces épreuves sont-elles passées, sous verdict scellé ; la référence est-elle bien invisible de l'agent.]** La vérité exacte, je la prévois sur des mondes à lois plantées, dont l'oracle est hors de la machine : conçus, pas encore mesurés. **[BLANC 5-b : où en est l'étape 0 au 1er décembre.]** »
*Repli pour 5-a* : « Les épreuves de cet oracle sont écrites ; je ne cite pas encore leur verdict. »
Cette phrase vaut pour le mode de sabotage « affaiblir les contrôles », seul visé par le point 1 de la décision.

### Phrase 9 (l'attaquant informé)

| Pièce | Chemin | Existe aujourd'hui | Lu par moi |
|---|---|---|---|
| Les deux bras d'attaque contre les moniteurs | `docs/decisions/decision-N-056-v1.md`, point 6 | oui, scellée | point 6 |
| La sonde comparée aux juges sous les mêmes attaques (HC2) | `docs/decisions/decision-N-068-v1.md`, § 4 et 5 | oui, scellée | § 4 et 5 |
| Une famille tenue à l'écart neuve par cycle | `docs/decisions/decision-N-062-v1.md`, points 3 et 6 | oui, scellée | en entier |
| L'invariant d'entraînement et son exception | `docs/decisions/decision-N-053-v1.md`, point 5 | oui, scellée | non ouverte |
| Le préenregistrement du bras d'attaque informé contre les sondes ; celui de la comparaison aux juges | sous `prereg/` | **non trouvés par leur nom** ; N-068 dit la prédiction « à chiffrer au préenregistrement » | — |
| Les recettes et briefs du bras d'attaque | dossier du bras d'attaque que nomme N-056 | fermé à qui conçoit des moniteurs ; non cherché | — |
| Ce qui a été lancé et lu ; tout verdict | `docs/verdicts/`, `diag/` | fermé à ma lecture | blanc |
| La comparaison à leur juge durci | proposition du protocole X (v2, § 11), non décidée | proposition seulement | lue en v1 |

**Phrase complétée.** « Leur exigence est la bonne : attaquant informé, attaque refaite contre la défense finale, comparaison au juge durci et non au juge par défaut. Chez moi, deux attaques sont décidées contre les sondes. Une famille de sabotage tenue à l'écart, conçue sans rien voir des moniteurs, lue une seule fois. Et un bras d'attaque informé, dont le concepteur connaît les conceptions des moniteurs et le protocole, mais ni les épisodes d'épreuve ni les seuils. Les recettes restent scellées, hors de portée de ceux qui conçoivent les moniteurs. Je prévois aussi de comparer le déplacement du score d'une sonde à celui de juges sous les mêmes attaques. La comparaison à leur juge durci est proposée, pas décidée. **[BLANC 9-a : ce qui a été lancé et lu de ces bras, sous verdict scellé.]** »
*Repli si le blanc reste vide* : « Rien de cela n'est encore un résultat que je puisse citer. » Il remplace « Ce n'est pas encore mesuré chez nous », que la v4 affirmait sans le savoir.

## Ce que je n'ai pas fait

- Je n'ai pas cherché les pièces par leur contenu, seulement par leur nom : « non trouvé par son nom » ne veut pas dire « n'existe pas ». La mère confirme.
- Je n'ai pas lu N-076 en entier, ni N-060 v4, ni N-053.
- Je n'ai rempli aucun blanc, et je n'ai pas ouvert ce qui permettrait de le faire.
- Erratum non contre-lu.
