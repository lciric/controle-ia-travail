# Papier C — nœud H-1 : lire ou non les deux statistiques de stabilité de rang entre juges quand la destination n'est pas identifiable — décision d'un juge de l'étage 3 — v1

- **Cadre.** Autonomie GO-2026-11-22-106 (`registres/go.md`) ; consigne `docs/notes/autonomie-2026-11-22-v1/consigne-autonomie-12h-chaine-de-decision-v2.md` (`fc8e306096ad55367b43c41d1f01f192782b8fa2926678fc4d7dc9fa63c5fae5`) ; étage 3 de la chaîne (consultation) ; Lazar hors ligne depuis 19:11Z selon la mère.
- **Juge.** Session `session_013QMayjGub5sSHD5oivnLhk`, fille de la mère `session_013QMayjbmQUdDuDs2S3i3XD`, branche `juge/papier-c-h1-fable-v1`. Modèle et effort : ceux que `get_session` rapporte pour cette session, donnés à la mère dans la ligne d'inscription envoyée vers 19:52Z ; ils ne sont pas recopiés ici (règle du harnais : aucun identifiant de modèle dans une pièce poussée). Ni rédacteur ni contre-lecteur d'aucune version du texte. Un second juge tranche la même question à part.
- **Écrite** le 2026-11-22 entre 20:07Z et 20:09Z, heures relevées par `date -u` à l'ouverture de la branche et au scellement. Aucune dépense, aucune instance, aucun appel externe, aucune simulation rejouée.

## 1. La question

Les deux statistiques de stabilité de rang entre juges du papier C — la concordance des rangs des trois juges d'une famille d'attaque à l'autre (ligne C-P3a) et la concordance de ces rangs entre les deux corpus (ligne C-P3b) — sont-elles toujours lues, ou ne le sont-elles plus dès qu'une de leurs composantes vient d'un couple juge × famille où la destination de la loi de déférence n'est pas identifiable ? Trois options : (a) toujours lues, lecture écrite le 19 novembre (Plan, section 8, précision 37) ; (b) non lues dans ce cas ; (c) changer la grandeur (ranger les juges sur la pente de la loi séparée, sans destination).

## 2. Décision

**(a) : les deux statistiques restent toujours lues, avec ce que la version c1 déclare. Confiance : 0,80.**

Cette décision vaut pour le choix entre les trois options. Elle ne dit pas que les deux lignes sont « au niveau » : cela, seule la grille de la clause de repli, jouée sur la liste finie entière, le dira.

## 3. Raisons

1. **Une condition de dégénérescence s'attache à la grandeur qu'elle rend indéfinie, et le gain n'en a pas.** Quand la destination s'échappe, la loi n'est plus qu'un décalage : le gain y est proche de zéro, ce qui est une valeur du gain, et non une absence de valeur (analyse du juge : dans la loi, la pente de chaque droite est identifiée ; c'est leur point de rencontre, la destination, qui ne l'est plus quand les pentes sont proches de zéro). Le texte lit déjà ce gain partout pour réfuter la prédiction de signe (C-P2) et celle de l'usurpation (C-P6), et il applique la même règle à la troisième statistique de rang (C-P3c), « non identifiable » quand sa propre grandeur dégénère (le dénominateur du gain d'écart). La règle est générale ; elle n'a pas été taillée pour ces deux lignes.
2. **La lecture écartée retire le test là où le phénomène prédit existe.** Si les juges diffèrent vraiment, le juge le moins déplacé est, le plus souvent, celui dont la destination s'échappe, et la statistique cesse d'être lue. Sur données simulées, sous un effet vrai (gains 0,04, 0,10 et 0,16), « établie » tombe de 0,945 à 0,0075 ; la ligne C-P3a n'est lisible dans aucun essai sans attaque, et dans 0 à 94 % des essais à gain 0,10 selon le modèle d'erreur. Ce n'est pas une lecture plus sévère du test, c'est son retrait.
3. **Ce retrait existe déjà sous son vrai nom, et le directeur l'a soumis à une autre condition.** « Rapportées sans verdict » est la version (b) de la décision D-9 (GO-2026-11-19-53) ; Lazar a retenu la version (a), sous réserve de la grille. Les taux simulés que le texte citait quand il a tranché venaient des programmes de l'archive, qui lisent selon (a) ; ceux de la grille, venus après, aussi. Adopter (b) ici ferait tomber le verdict par une autre porte que celle qu'il a fixée.
4. **Le niveau de la lecture gardée est mesuré, et borné par une règle mécanique.** Sans attaque, les rangs sont du bruit et le test rend « établie » au taux de son niveau : 0,024 à 0,049 (C-P3a) et 0,028 à 0,053 (C-P3b) sur les cases jouées, seuil de la clause 0,0638. Un dépassement dans une seule case de la liste finie, et la ligne passe d'elle-même « rapportée sans verdict ». La sévérité est portée par trois lectures jointes, par la valeur p exacte doublée d'une valeur p par rééchantillonnage centré pour C-P3a, et par un seuil de clause sans correction pour le nombre de cases.
5. **La lecture écartée lierait la lisibilité d'une ligne à la taille de ce qu'elle mesure.** C'est ce que le texte s'interdit pour les juges et les familles (« a deference screen must not threshold the outcome », Panin, p. 11, cité par le texte).

## 4. Symétrie (R4)

- **La règle (a) ne dépend ni du signe ni de la taille du résultat ; la règle (b) en dépend.** Sous (b), ce qui disparaît d'abord, ce sont les « non établie » des mondes sans attaque efficace. La lecture « la plus sévère pour l'établie » est donc aussi celle qui abrite le mieux la prédiction d'une issue négative : la sévérité ne se juge pas d'un seul côté.
- **Le choix du 19 novembre n'a pas joué dans un seul sens.** La même règle laisse la clause de repli jouer contre la troisième ligne (C-P3c : 54 cases sur 96 au-dessus du seuil), qui perd son verdict. Et (b) aurait passé la clause sans peine (taux d'« établie » de 0,000 à 0,029) : choisir (a) après avoir vu les taux n'a donc pas servi à éviter la clause, mais à garder un test.
- **Une asymétrie reste, et je recommande de la fermer (section 8, point 1).** Pour la sonde, le texte écrit d'avance comment lire une confirmation obtenue sans attaque mesurée (audit A9 : « robustesse non éprouvée », dans les deux sens). Il n'a pas l'équivalent pour ces deux lignes : une « établie » sortie de rangs de bruit (au plus 5 % des cas) serait lue après coup.
- **Le sens de l'artefact est déclaré.** Le gain tiré vers zéro quand la destination s'échappe pousse C-P2 et C-P6 vers la réfutation (déclaré en c1) ; pour les rangs, il ajoute du bruit, sauf le mécanisme de la section 5.

## 5. Dureté sur le résultat séduisant (R8), et où la lecture gardée est la plus exposée

- **« Non établie » n'est pas « instabilité établie », et « illisible » ne serait ni l'un ni l'autre.** Aucune de ces issues ne se convertit en constat.
- **Le résultat séduisant est ici « stabilité de rang établie »**, contre les contre-indices publiés que le texte cite lui-même (rangs qui ne se transfèrent pas d'un corpus à l'autre). C'est lui qu'on vérifie le plus durement : la clause sur la liste finie entière est la condition de cette décision, pas un ornement.
- **Le chiffre qui pèse contre (b) vient d'un seul scénario simulé et d'un seul modèle.** Je le dis tel quel : à gain 0,20, (b) lit de 25 à 100 % des essais selon le modèle d'erreur. L'argument tient par sa structure (le juge le plus faible commande la lisibilité), non par ce chiffre.
- **Exposition précise de (a), hypothèse du juge, non simulée.** Un juge plus bruité voit sa destination s'échapper plus souvent ; son gain est alors tiré vers zéro ; il peut se trouver rangé plus bas d'une famille à l'autre sans que son gain vrai diffère. Les cases jouées où les erreurs diffèrent entre juges, sous attaque égale, ne le montrent pas (C-P3a 0,004 à 0,027 ; C-P3b 0,012 à 0,046, à 45 et 60 tâches). Mais l'échappement est le plus fréquent à 30 tâches, et aucune case à 30 tâches n'est jouée. Les 58 cases restantes (compte du texte, à revérifier par l'auteur du rapport) sont donc l'épreuve de ce choix, et une épreuve à l'aveugle : personne n'a vu leurs taux, alors que la lecture a été écrite après les 86 premières.

## 6. Ce qui ferait changer cette décision

1. **Un mécanisme, et non une fluctuation, hors de la liste finie** (compression non linéaire, bords de l'échelle de 0 à 9, juges à décalage pur), par lequel l'échappement de la destination range les juges dans le même ordre d'une famille à l'autre sans différence de gain. La bonne suite serait alors « rapportées sans verdict » (version (b) de D-9), décidée par Lazar ; pas la lecture écartée.
2. **Le mot de Lazar**, s'il préfère la sévérité à la puissance pour ces deux lignes.
3. **Une instruction de (c)** montrant, sur données simulées, un niveau tenu et une puissance au moins égale : je proposerais alors (c) à Lazar, parce qu'elle fait disparaître la question (section 8, point 2).

**Ce qui ne la change pas** : un dépassement du seuil dans une case de la liste finie. La clause s'applique d'elle-même ; c'est la borne prévue, non un motif de revenir à (b).

## 7. Phrase à inscrire (au marqueur du nœud H-1, précision 37)

> Nœud H-1 tranché le 22 novembre 2026 par la chaîne de décision de l'autonomie accordée par le directeur (GO-2026-11-22-106 ; [étage atteint, juges consultés, effort : à écrire par la mère] ; directeur hors ligne) : la lecture écrite ci-dessus est gardée, les deux statistiques de rang restent toujours lues. Raisons de principe : chaque condition de dégénérescence s'attache à la grandeur qu'elle rend indéfinie, et le gain n'en a pas ; la lecture écartée lierait la lisibilité d'une ligne à la taille de l'effet, et retirerait le test là où les juges diffèrent le plus, le juge le moins déplacé étant celui dont la destination s'échappe. Cette lecture reste la moins sévère des deux pour l'« établie » et a été écrite après lecture de taux simulés : son niveau ne tient que par la clause de repli, lue sur la liste finie entière. Le directeur peut la renverser jusqu'au scellement ; la lecture écartée et tout changement de grandeur restent de son ressort.

Le marqueur s'appelle « mot du directeur » : la phrase dit qui a tranché, pour qu'aucun lecteur ne la prenne pour un mot de Lazar.

## 8. Ce que je recommande en plus, hors du nœud (rien de ceci ne retient la décision)

1. **Une mention symétrique sur les deux lignes**, à écrire par le rédacteur et à vérifier par son contre-lecteur, sur le modèle de l'audit A9 : chaque ligne porte le nombre de couples juge × famille, par corpus, où la destination n'est pas identifiable ; si aucune famille n'est positive ni négative chez aucun juge (aucun gain mesuré nulle part), la ligne, quelle que soit son issue, porte « rangs sans gain mesuré : stabilité non éprouvée » — une « établie » n'y vaut pas confirmation de la prédiction 3 de N-005 et déclenche l'audit, une « non établie » n'y vaut pas indice contraire. Grandeurs déjà définies, aucun seuil neuf, aucun verdict changé. Avec elle, ma confiance monte ; sans elle, (a) reste mon choix.
2. **Instruire (c) à bas coût, comme ligne rapportée sans verdict** : les mêmes statistiques de rang calculées sur la moyenne des pentes de la loi séparée nette, que le texte fait déjà calculer pour les destinations par rang. La pente n'emploie pas la destination : cette ligne dirait si une issue tient à l'échappement. Elle ne touche pas la grandeur retenue ; l'adopter comme grandeur du verdict reviendrait à Lazar.
3. **Jouer maintenant, sous la lecture (a), les 58 cases restantes** (travail sur processeur, sans dépense, par un agent qui n'est rédacteur d'aucune version, puis contre-lecture) : c'est la borne du risque, et les cases à 30 tâches sont celles qui comptent (section 5).
4. **Montrer cette décision à Lazar à son retour, avant le scellement.** Le contre-lecteur demandait un nœud du directeur, sans défaut, et le texte dit qu'il ne se scelle pas sans ce mot. Une décision de la chaîne mandatée n'est pas un défaut silencieux, mais d'autres verrous retiennent encore le scellement : attendre son regard ne coûte rien.

## 9. Compétence de la chaîne

La consigne laisse à Lazar tout changement d'hypothèse ou de revendication. (a) confirme le texte tel qu'il est : la chaîne peut la prendre. (b) ôterait en pratique leur verdict à deux lignes de la prédiction 3 de N-005 (le texte nomme « écart partiel », déclaré, le passage d'une de ces lignes à « rapportée sans verdict ») ; (c) change la grandeur d'une prédiction retenue. Si l'autre juge ou l'étage 4 retenait (b) ou (c), ce serait, à mon sens, une proposition à porter à Lazar et non une décision à inscrire : sûrement pour (c), probablement pour (b).

## 10. Réserves sur cette décision

- **J'ai lu, moi aussi, les taux simulés des deux lectures avant de trancher.** La réserve de méthode du 19 novembre vaut donc pour moi. Ce sont des mesures de conception sur des mondes plantés, non des résultats ; mes raisons 1, 2, 3 et 5 n'en dépendent pas, la raison 4 en dépend.
- **Indépendance entre les deux juges, entamée après coup.** Ma décision formée, et dite formée dans le fil de cette session juste avant, j'ai listé entre 20:01Z et 20:07Z les demandes de fusion du dépôt pour en suivre l'usage : le titre de la demande n° 72, celle de l'autre juge, porte la lettre de sa décision. Je n'ai ouvert ni sa branche ni sa note ; je n'ai pas relevé ma confiance pour cela. À retenir pour la suite : un titre de demande de fusion ne devrait pas porter une décision qu'un autre juge doit ignorer.
- **Je n'ai rejoué aucune simulation** : les chiffres sont ceux des deux rapports, dont l'un a été rejoué à l'identique par son contre-lecteur.
- **Routine de reprise réduite**, déclarée à la mère : empreintes de lancement bonnes ; vérification de l'arbre scellé en échec sur 96 problèmes de forme sans rapport avec le nœud (95 empreintes compagnon absentes, 1 nom), signalés et non corrigés ; état, passations, inventaire des instances et suite d'essais non faits, le cloisonnement du juge interdisant `registres/etat.md`.

## 11. D'où viennent les chiffres (R6)

Branche `claude/papier-c-preenregistrement-v1`, commit `48e08c72`, dossier `registres/papier-c/redaction-brouillon6-relance-v1/` :
- rapport de la grille de la clause de repli, `grille/rapport-grille-clause-de-repli-v1.md`, `8d1616fce0dc59ea6bd986e465ae24efd845e1db7954cb39d39399fbc1a6ea89` : section 1 (86 cases, 0,003 à 0,049 et 0,009 à 0,053, seuil 0,0638 ; 54 cases sur 96 pour C-P3c) ; section 6.1 (taux par modèle et par gain, d'où 0,024 à 0,049 et 0,028 à 0,053 sans attaque, 0,004 à 0,027 et 0,012 à 0,046 sous erreurs inégales et attaque égale) ; section 7 (effet vrai 0,04, 0,10, 0,16 : 0,945 et 0,970) ; section 8, ambiguïté A6 (parts lisibles et taux sous la lecture écartée) ;
- contre-lecture de ce rapport, `contre-lecteur-grille/rapport-contre-lecture-grille-clause-de-repli-v1.md`, `d0485a406d0b13b97e2141d42a401e93b026a3a3953b35fe2561ba3848788819` : remarque CG-03 (0,945 à 0,0075, rejoué à l'identique) ; section 9 (avis par ligne).

Branche `prep/papier-c-prereg-fable-v1`, commit `bda789a2` : texte c4, `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22-c4.md`, `51eea9c5d061a5c4f3d838512d69a1b4715530ca84e0cec803dd17e2870fcc99` (verrou 10 : 58 cases restantes, dont toutes celles à 30 tâches ; précision 37 ; bloc de la stabilité de rang) ; rapports du contre-lecteur `30239c46758e5013936b159f67f832ddacaa7ac2e7fe4ef721556a586ee0e625` (remarque CB-04) et `ba71281827a14b33cbf7e37dc8036c2008bb6b09c270ca50ee96260af413ff78`.

## 12. Lu, en fait (ligne « qui a lu quoi »)

Lu au commit `4476e38d` de `main` et aux commits nommés ci-dessus, le 2026-11-22 entre 19:50Z et 20:07Z :
- `CLAUDE.md` (`605db83a…`) et le message de lancement ; la consigne d'autonomie v2, en entier ; `registres/go.md` : les trois lignes où figure « GO-2026-11-22-106 » (GO-106, GO-114, GO-118), tronquées à 1 500 signes ; `registres/qui-a-lu-quoi-v21.md` : puces de tête tronquées, en-tête du tableau, lignes 335 et 341 en entier, débuts tronqués de quelques lignes et réserves ; `registres/rappels.md`, 30 premières lignes tronquées (aucun rappel échu le 22) ;
- les deux rapports du contre-lecteur du brouillon 7 de relance, en entier ; du texte c4 : lignes 1 à 30, 140 à 160, 232 à 256, 300 à 312, 436 à 462, 718 à 1261, 1386 à 1410, 1894 à 1953, 2030 à 2099, 2186 à 2325, 2376 à 2386, et des lignes isolées sorties par recherche de mots ; de la liste des points ouverts v3 (`8d3f1ca6…`) : titres et section H-1 ;
- `docs/decisions/decision-N-005-N-006-v1.md` et `decision-N-013-v1.md`, en entier, empreintes bonnes ;
- extension déclarée à la mère avant de la faire : du rapport de la grille, lignes 1 à 185 et 249 à 323 ; de sa contre-lecture, titres, lignes 60 à 119 et 264 à 321 ;
- des noms seulement : fichiers du dossier de rédaction, fichiers dont le nom porte « grille » sur la branche du rédacteur (dont des pièces d'autres chantiers, non ouvertes), branches distantes du papier C et des juges, fichiers en défaut à la vérification de l'arbre, sujets des trois derniers commits de `main`, titres des huit dernières demandes de fusion.

**Expositions incidentes, sans chiffre ni verdict** : le mot de Lazar de GO-2026-11-22-118 sur la conception des sondes de la boîte blanche ; la mention, dans la liste, d'un second cycle de conception et d'une exposition d'un autre rédacteur ; les titres de demandes de fusion d'autres chantiers ; la lettre de la décision de l'autre juge (section 10).

**Non lus** : ce que le message de lancement interdit (« les verdicts de P3-bis, T0.7, barreaux, ni le coffre »), tout autre verdict, `registres/etat.md`, `registres/decisions.md`, les passations, la branche et la note de l'autre juge, le reste du texte c4, les journaux du rédacteur, le code du module.

## 13. Passation de cette session (R14)

- **Fait** : inscription envoyée à la mère avant lecture, et sa correction ; pièces lues ; cette note, scellée, poussée sur `juge/papier-c-h1-fable-v1` ; décision envoyée à la mère.
- **Reste** : rien pour ce juge. À la mère : la trace de la décision (étage, modèles, effort, coût nul), la ligne de la liste « qui a lu quoi » et sa cellule « exclu de » (je propose : verdict et contre-lecture du préenregistrement du papier C), l'alerte à Lazar, les suites de la section 8.
- **Réserves** : section 10.
- **Prochaine action** : aucune de ma part, sauf question de la mère.
- **Instances actives** : aucune lancée, aucune inventoriée. `registres/etat.md` non mis à jour par cette session : il lui est interdit.
