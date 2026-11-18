## État actuel de l'organisme

Résumé, sans jugement de valeur, de la documentation publique de l'organisme (dépôt public de l'organisme, `README.md`, sections 2, 3 et 7, état du 13 novembre 2026 ; empreinte et commit au préenregistrement de la course). Ce que le code fait aujourd'hui, et ce qui reste ouvert selon cette documentation. Les noms en gras sont **les noms des modules** à employer dans le champ `module_change`.

### Le trajet d'une idée, module par module

1. **proposeurs** — des agents de plusieurs familles écrivent, en parallèle, des cartes à champs fermés (hypothèse, effet prédit, mesure qui la tuerait). Une session neuve par appel, une consigne figée et empreintée.
2. **aiguilleur** — une session neuve lit **la forme seule** de chaque carte, une carte anonyme par appel, et la classe : « niveau de la méthode » (passeport), « à corriger », ou « trop concrète » (scellée dans le coffre, lue par personne). Cette étape n'est jamais sacrifiée au budget ; une carte sans passeport est refusée par tout consommateur en aval.
3. **mémoire anti-redite** — l'orchestrateur indexe l'archive et compte les redites (bardeaux de mots, seuil fixé) ; elle ne garde que des champs en liste blanche, caviardés ; jamais une clé, jamais un verdict, jamais un témoin planté.
4. **juges croisés** — chaque carte à passeport est notée par chaque juge de la configuration, un appel par carte et par juge, session neuve, identifiant opaque ; aucun juge ne voit la note d'un autre ; items vrai ou faux, agrégation fixée par configuration ; verdicts déposés au coffre et ouverts seulement après la fin de la phase de mesure.
5. **bisociateur** — l'orchestrateur forme des paires d'idées selon trois bras (« loin mais proche », paires « jamais reliées », « trou de structure commun ») et une session neuve écrit la fusion à l'aveugle ; une fusion n'entre au lot qu'avec son passeport et tous ses verdicts.
6. **moisson de nouveauté** — l'orchestrateur relève des métadonnées et des résumés (archives ouvertes de prépublications, index bibliographique ouvert) ; les correspondances sont marquées non opposables ; une absence apparente dans la littérature est traitée comme une question.
7. **juge statistique (pari)** — pour le pôle d'épreuve, une carte s'engage sur une loi prédictive des issues ; un processus de richesse est calculé par l'orchestrateur contre un nul formé des lois connues (l'archive, mise en commun ajustée), sur des tirages frais dont la graine est l'empreinte de l'engagement ; la promotion suit une règle à e-valeurs écrite dans le code, hors de tout agent. Ce nul ne couvre pas toute recombinaison : chaque version dit ce qu'elle laisse dehors.
8. **tests de mort** — la carte figée devient un script, exécuté dans un bac à sable (sans réseau, mémoire bornée, appels système filtrés, sans clé) sur des données déjà présentes ; la prédiction est scellée avant l'exécution ; depuis la version 57, le verdict (« survit » ou « éliminée ») est calculé par l'orchestrateur sur le fichier brut que nomme le préenregistrement scellé, jamais lu dans ce que le script imprime ; un vérificateur d'une autre famille relit. **Ouvert** : éprouvé hors ligne seulement (exécuteur simulé) ; le lanceur et la ronde d'idéation appellent encore l'étage de la version 56.
9. **sélection entre générations** — une carte qui « affine » une autre sans en changer la statistique, les couches, la borne ou le seuil est refusée ; depuis la version 57b, seules les cartes « survit » sont gardées, scellées. **Ouvert** : la génération suivante ne lit pas encore cette sélection dans la course 2 ; dans la plus petite boucle réelle, la génération 2 a été servie et jugée une fois avec la sélection de la génération 1.
10. **noyau et budget** — plafond dur par étape et par course, recalculé deux fois et accusé à chaque étape, étapes protégées et sacrifiables, arrêts écrits (champ manquant, modèle servi inconnu, plafond atteint, signal), aucun repli silencieux.
11. **coffre** — verdicts et clés scellés ; toute lecture avant la fin déclarée de la mesure est un incident qui arrête l'orchestrateur.
12. **dossier fermé** — une course ne lit que les fichiers listés dans un manifeste scellé, sans lien symbolique.
13. **témoins plantés** — des lois vraies et fausses plantées, anonymes, mêlées à chaque génération, indexées pour l'audit et exclues de tout ce qui est servi aux agents ; mondes plantés à vérité connue pour les démonstrations hors ligne.

### Gardes contre l'auto-tromperie (ce qui existe, et sa limite écrite)

- **Un agent imprime son propre verdict** : la promotion est calculée par l'orchestrateur à partir d'engagements scellés et de tirages frais ; pour les tests de mort, le verdict vient du fichier brut (limite : éprouvé hors ligne seulement).
- **Le juge voit les données avant de s'engager** : l'engagement est scellé avant toute issue ; les tirages sont semés par l'empreinte de l'engagement.
- **Le proposeur apprend le goût du juge** : juges aveugles entre eux et aux notes passées ; la mémoire ne sert jamais un verdict ni un témoin.
- **Lecture d'un verdict avant la fin** : le coffre arrête l'orchestrateur.
- **L'exécutant atteint le réseau, l'hôte ou une clé** : garde des outils (première barrière, par motifs) ; vraie barrière : le bac à sable ; variables d'environnement en liste blanche fermée.
- **Une fuite de secret dans l'archive** : caviardage des formes connues de clé (limite : une forme inconnue passe).
- **Repli silencieux** : aucun ; chaque manque arrête le rôle ou la course avec un motif écrit.
- **Les données dérivent sous le test** : dossier fermé.
- **Les témoins sont reconnus et joués** : témoins anonymes, exclus de tout ce qui est servi.
- **L'aiguilleur est sauté pour épargner** : étape protégée, passeport exigé partout en aval.
- **Banc de tricheurs** : onze tricheurs scriptés contre le juge statistique (copie renommée, mélange de survivants, survivant tempéré, etc.) ; sous le nul mis en commun, les lignes fatales tiennent dans la validation décisive préenregistrée ; hors de la classe couverte (compositions de plusieurs étapes, recombinaisons par morceaux, multiplicité entre cartes, puissance aux effets faibles, banque réelle) : rien n'est dit. **Banc de mutations** : des mutations délibérées du code, chacune devant être tuée par les essais pour la raison attendue ; il ne dit rien des gardes qui n'existent pas.
- **Attaque de Goodhart** : un proposeur modèle qui lit la description exacte du juge et voit ses verdicts a percé le nul de la version 8 dans une classe que celle-ci déclarait non couverte ; un nul nouveau (version 9) couvre les recombinaisons par morceaux à un niveau.

### Ce qui n'est délibérément pas là

Aucun contenu d'attaque (les cartes trop concrètes vont, scellées, au coffre d'une session séparée) ; aucune donnée en quarantaine, aucun registre de travail ; aucune exécution payante (le moteur réel exige des clés et un plafond signé). Le module de bras d'attaque est un talon qui refuse de tourner.
