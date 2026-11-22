# Les six dossiers finis du collisionneur : toutes les propositions et les meilleures retenues

Écrit à 2026-11-22T12:42:57Z (`date -u`). Pièce de travail (classe C). Question du directeur : « quelles sont toutes les propositions et les meilleures retenues ? ». Six dossiers du protocole X, tous finis, dont le contrôle par `verifier` tient. Chaque dossier se joue en trois tours : les modèles conçoivent chacun à l'aveugle (tour III.1), se critiquent les uns les autres (III.2), puis répondent aux critiques (III.3). Chaque section a été écrite par un agent Opus qui a lu toutes les cellules de son dossier ; la mise ensemble est de la session des collisionneurs.

**Règle de lecture.** Aucun chiffre ni aucune référence n'est opposable sans vérification sur pièce. Les vérifications faites portent sur le titre, la date et le résumé d'une page publique (arXiv ou éditeur), jamais sur le PDF entier : elles établissent l'existence d'une référence, pas ce qu'elle démontre.

## En bref : les deux propositions les plus fortes de chaque dossier

| dossier | proposition retenue | portée par |
|---|---|---|
| Coercition | Comparer le levier social à la même demande assortie d'une justification non sociale, et non à « ignore la règle » ; mesurer le dommage par programme, sur l'état final. | B, C, E ; A et D sur le fond |
| | Rejouer le moniteur sur un dossier gelé, avec un témoin adressé à un destinataire absent. | A, B, D, E |
| Problématique du papier | Commencer par une expérience de faisabilité avec contrôles nuls : un dommage furtif mesurable sur le modèle de huit milliards de paramètres, et des moniteurs qui lisent la dégradation, pas le canal. | les cinq |
| | Mesurer l'apport des activations contre une relecture du contexte complet par un modèle sain. | les cinq |
| Revendications | Un plan contrôlé de ce que lit une sonde : témoin d'adaptateur bénin, secret bénin, lecteur tiers. | les cinq |
| | La continuation honnête depuis l'état déployé, à budget fermé. | A, B, E |
| Questions des concurrents | On ne prouve jamais qu'un manque n'a pas été comblé : on date une absence de trouvaille, dont le rappel n'est qu'une borne haute. | tous, après les critiques |
| | Les critères de choix d'une petite équipe deviennent des règles d'arrêt, faute de pouvoir les valider avant l'issue. | A, B, D, F |
| Tirage au hasard | Le duel à même loi de tirage, tirage révélé contre tirage caché, qui isole l'apport du secret. | A, B, C, D, F |
| | Mesurer d'abord si l'agent voit les effets du tirage avant de s'engager, avec des témoins réel contre réel. | A, B, C, E, F |
| Question générale | Vérifier d'abord que le sabotage diffus existe vraiment sur un modèle de huit milliards de paramètres, sans qu'une règle mécanique simple suffise. | les cinq, en premier |
| | Régler un détecteur ou une règle de vérification sur un cadre, le geler, puis voir s'il tient ailleurs face à un témoin fort. | A, B, D, E |

Lettres : A Fable 5.2, B Opus 5.5, C Argon, D Astra, E Carbon ; F Neon dans les deux dossiers qui l'ont.

## Questions des concurrents

Cette section reprend la note déjà scellée, `note-synthese-questions-concurrents-v1.md` (même dossier, d6dd8c58…), qui compte toutes les propositions par modèle, les accords, les désaccords et le tableau des vérifications.
- **La question** : comment relever, à partir du seul texte de publications sur la surveillance d'agents, ce que les auteurs n'ont pas fait, veulent faire ou disent ouvert ; vérifier qu'un manque n'a pas été comblé ; et choisir où porter l'effort.
- **Constat** : aucun modèle n'a reçu la liste des publications. La sortie est donc une méthode, pas une carte des concurrents.
- **Retenu** : on ne prouve jamais qu'un manque n'a pas été comblé : on date une absence de trouvaille, et le rappel n'en est qu'une borne haute. Un surveillant se juge au gain de l'union « contrôles mécaniques ou surveillant », à taux de fausses alertes par trajectoire égal. Les critères de choix deviennent des règles d'arrêt.
- **Désaccords restants** : la première expérience à lancer, l'effectif nécessaire, et la question de savoir si un résultat négatif propre est un « bon choix ».

## Coercition

**La question.** Un tiers peut faire pression sur un agent ou sur son moniteur, par la menace, la récompense, la flatterie ou l'appel à une identité commune. Un agent et un moniteur issus du même modèle peuvent aussi s'entendre. Comment savoir, par la mesure et sur de petits modèles ouverts, si c'est autre chose que les attaques déjà connues (question-etage3).

Lettres : A Fable, B Opus, C Argon, D Astra, E Carbon. Aucune expérience n'a été lancée. Tous les seuils et tous les coûts des cellules sont illustratifs.

### Toutes les propositions, groupées par idée

1. **Mesurer le dommage par un programme qui lit l'état final, sans aucun modèle de langue dans la boucle** (A, B, C, D, E). Il s'appuie sur des tests cachés, des fichiers témoins avec empreinte, un journal du réseau et la comparaison des états. Le sabotage, le silence et la fausse alerte se comptent à part (B). Après les critiques, chacun sépare l'écart demandé de l'échec ordinaire de la tâche (E3-T3-reponse-A, -D, -E). Les fausses alertes se comptent aussi sur les échecs honnêtes (E3-T3-reponse-C).
2. **Le levier ajoute-t-il quelque chose à la demande seule ?** (A, B, C, D, E). On compare la même demande avec et sans habillage social, à longueur et position égales. Contrôles : le levier sans demande, et une demande assortie d'une justification non sociale (E3-T3-reponse-B, -C, -E).
3. **Les défenses contre l'injection de consignes couvrent-elles aussi la pression ?** (B, puis A). Un levier n'est une classe à part que si une défense réglée sur l'injection ne le couvre pas (E3-T1-conception-B ; E3-T3-reponse-A, « D1-bis »).
4. **Pression sur le moniteur, à travail gelé** (A, B, C, D, E). Le même dossier est rejugé sous un cadrage social ou neutre (D), une pression recalibrable ou non (A), une fausse alerte opposée aux simples mots inquiétants (C), et un juge passif opposé à un juge dans la boucle, à dilution du texte contrôlée (E).
5. **« S'entendre » : étiquette, origine ou angle mort partagé ?** (A, B, C, D, E). On sépare l'auteur de l'acte, l'auteur du style et l'étiquette « même modèle » (E3-T3-reponse-B, -C). La paraphrase se fait par une famille tierce (E3-T3-reponse-E). Il faut aussi un essai qui montre qu'une coordination connue serait détectée (E3-T3-reponse-D).
6. **Que lit une sonde des activations ?** (A, B, C, D, E). Elle doit battre un lecteur de texte du même préfixe et une sonde sur la couche d'entrée. Son seuil est gelé hors pression. Une attaque optimisée contre elle se juge sur une autre sonde (E3-T3-reponse-B, -C, -E).
7. **L'exposition répétée sur une longue tâche** (A ; E en test de persistance) (E3-T3-reponse-A).
8. **La docilité générale comme facteur de confusion** (B), et **la crédibilité de la menace** : l'agent sait que le tiers n'a pas les droits pour l'exécuter (C) (E3-T3-reponse-B, -C).
9. **Les instruments face à des vérifications sans modèle, sous un budget d'audit** (A, B, C, D, E). Il faut un audit au hasard de même coût (A, D) et un oracle appliqué aussi aux dossiers non signalés (E3-T3-reponse-A, -C, -D). L'alerte à tort se lit comme une saturation de ce budget (E3-T3-reponse-B).

### Ce que la confrontation retient

- **Le dommage mesuré par programme sur l'état final.** Les cinq le gardent après les critiques. Ils le restreignent à l'écart demandé, sur toutes les trajectoires (E3-T3-reponse-A à -E). C'est la seule mesure qui ne dépend d'aucun composant corruptible.
- **Le levier comparé à une demande élaborée non sociale, pas à « ignore la règle précédente ».** A et B critiquent le comparateur de C, et C l'accepte (E3-T3-reponse-C, point 1). B, C et E convergent sur ce contrôle (E3-T3-reponse-B, bras « justification » ; -C ; -E). Deux autres corrections passent chez tous : le levier candidat est choisi sur un lot de tâches à part, et l'issue « le levier fait refuser » compte comme un effet (E3-T3-reponse-B, -C, -E).
- **Le rejeu du moniteur sur un dossier gelé, avec un contrôle adressé à un destinataire absent.** Le gel est loué même par ses critiques (E3-T2-critique-croisee-B, sur D). A, B, D et E le reprennent (E3-T3-reponse-A, D2 ; -B, E3′ ; -D ; -E, E2′). Les quatre critiques jugent sans valeur le contrôle « après le vote » ; D le retire (E3-T3-reponse-D).
- **L'entente démontée en trois effets, sur trois familles.** Les trois effets sont l'étiquette, l'origine et l'angle mort. Il faut trois familles et une variante de taille, car avec deux familles la parenté se confond avec la capacité (E3-T2-critique-croisee-B). L'échelle est logistique. A, B, C, D et E l'adoptent (E3-T3-reponses). A et D retirent le mot « entente » de leurs duels.
- **Le transfert des défenses avec un témoin hors distribution non social, sans rapport de réductions.** Les quatre critiques attaquent le rapport de B, et B l'abandonne (E3-T3-reponse-B, lignes 9 et 10). A en fait son critère de classe (E3-T3-reponse-A).

Jugement du rédacteur : les deux plus fortes sont le levier contre la demande élaborée non sociale et le rejeu du moniteur à dossier gelé. Elles tiennent après toutes les critiques. Elles coûtent peu. Ce sont elles qui décident si la « coercition » est une classe de menace à part.

### Les désaccords qui restent

- **Par où commencer.** A et B commencent par l'agent : D1 puis D1-bis, ou E1′ (E3-T3-reponse-A, -B). C couple l'agent et la fausse alerte (E3-T3-reponse-C). D et E commencent par le moniteur sur traces gelées, sans attendre qu'un petit agent cède (E3-T3-reponse-D, -E).
- **L'attaque optimisée contre une sonde.** C la dit gagnée d'avance par l'algèbre (E3-T2-critique-croisee-C). B le conteste, parce que l'attaquant ne contrôle que des jetons (E3-T3-reponse-B, ligne 18).
- **La familiarité de style.** E la range du côté de l'entente (E3-T3-reponse-E, point 10). A et C la rangent du côté opposé (E3-T2-critique-croisee-A, sur E).
- **L'avantage mécanique des paires de même modèle.** A ne l'accepte que pour une invite identique et un décodage glouton (E3-T3-reponse-A, ligne 23).
- **Un calcul de C.** D le conteste : la probabilité de non-décision sous effet nul (E3-T3-reponse-D).
- **La règle de décision.** E tranche encore sur l'estimation ponctuelle au seuil (E3-T3-reponse-E, E1′). Les autres tranchent sur des bornes d'intervalle.
- **Le coût.** De 42 heures de processeur graphique (C) à 300–900 heures (A, B). Non vérifié, et non comparable.
- **Les statuts « vérifié » posés par C et E sur des énoncés absents des faits.** A ne les reprend pas (E3-T2-critique-croisee-A).

### Réserve sur les sources

Toutes les références des cellules sont citées de mémoire. J'en ai contrôlé cinq sur leur page arXiv, pour le titre, l'année et le résumé seulement, pas pour ce que les cellules leur font dire :
- « AI Control: Improving Safety Despite Intentional Subversion », 2312.06942, décembre 2023 ; cela tranche la divergence d'année ;
- « LLM Evaluators Recognize and Favor Their Own Generations », 2404.13076, avril 2024 ;
- « Obfuscated Activations Bypass LLM Latent-Space Defenses », 2412.09565, décembre 2024 ;
- « How Johnny Can Persuade LLMs to Jailbreak Them », 2401.06373, janvier 2024 ;
- « Not what you've signed up for… Indirect Prompt Injection », 2302.12173, février 2023.

Les autres références sont non vérifiées, dont AgentDojo, la complaisance, les sondes contre la tromperie et la collusion par stéganographie. Aucune cellule n'a fait de recherche bibliographique : toute « zone ouverte » reste une question (R8).

## Problématique du papier

Source : le dossier fini du collisionneur sur la problématique du papier, étage 3 (cinq modèles : A Fable 5.2, B Opus 5.5, C Argon, D Astra, E Carbon). Aucune expérience n'a tourné. Tout est conception. Tous les chiffres des cellules sont illustratifs.

### 1. La question

Un agent mène une longue analyse, un adversaire la dégrade par petites touches dont aucune n'est suspecte seule : quel article écrire en deux mois sur un modèle ouvert de huit milliards de paramètres — une garantie contre des attaques jamais vues, un mécanisme nouveau, ou une loi d'une autre discipline mesurée chez les agents (question-etage3) ?

### 2. Toutes les propositions, groupées par idée

**Une loi importée (troisième type).**
- La loi de la racine carrée de la stéganographie : le dommage indétectable croît comme la racine de la longueur face à un détecteur qui cumule, et comme la longueur face à un seuil par étape — A (E3-T1-conception-A).
- La loi du délai de détection d'une rupture, en statistique séquentielle : le délai dépend du taux d'information par étape ; on compare ce taux entre le texte et les activations — B (E3-T1-conception-B). Variante : le délai multiplié par le débit d'information égale le seuil d'alarme — D (E3-T1-conception-D).
- La variance d'Allan des horloges atomiques : sa pente séparerait le bruit honnête d'une dérive adverse — C (E3-T1-conception-C).
- Le processus de ramification et le nombre de reproduction des épidémies : une erreur s'éteint ou se propage — E (E3-T1-conception-E).

**Un mécanisme (deuxième type).**
- Cumuler les scores faibles des moniteurs pour choisir où vérifier — A, B, E.
- Cumuler l'écart entre ce que disent les activations et ce que dit le texte — C, E.
- Laisser les activations désigner, dans un rapport, la case à faire vérifier — D.

**Une garantie (premier type).**
- Audit tiré au hasard, avec une influence plafonnée par étape — A ; même idée sur une table de faits sourcés, borne par tirage sans remise, à la manière des audits d'élection — D ; E l'adopte au tour 3 (E3-T3-reponse-E).
- Calibration sur les exécutions honnêtes seules : seuil conforme, martingale de pari — B, C, E.
- Certificat conditionnel à un taux de fuite minimal par étape — B.

**Le type oublié.**
- Une borne d'impossibilité : le dommage qu'aucun moniteur ne peut voir — A, B, C, E.
- Un banc de mesure avec dommage connu et cas honnêtes appariés — A, B, D.
- Une politique d'allocation des audits ; une contribution d'attaque — B.

### 3. Ce que la confrontation retient

**Retenue 1 — une première expérience de faisabilité, avec ses contrôles nuls.** Les cinq convergent après les critiques. Il faut d'abord établir que des touches furtives produisent un dommage mesurable sur huit milliards de paramètres, et que les moniteurs lisent la dégradation et non le seul canal de l'attaque (E3-T3-reponse-A, E3-T3-reponse-B, E3-T3-reponse-C, E3-T3-reponse-E ; D propose un pilote de même rôle, E3-T3-reponse-D). Contrôles acceptés par tous : bifurcation honnête contre honnête, consigne de sabotage présente sans dommage, adaptateur de poids bénin, intensité fixée par la furtivité avant de regarder le dommage. Cette expérience tient face aux critiques parce que chaque issue réfute quelque chose : un échec devient un résultat sur le compromis entre furtivité et dommage (E3-T3-reponse-B).

**Retenue 2 — le gain des activations mesuré contre une relecture propre du texte.** Toutes les critiques notent qu'un lecteur des activations voit les mots émis : battre un moniteur de texte ne prouve rien (E3-T2-critique-croisee-A, E3-T2-critique-croisee-B). Les cinq acceptent le même contrôle : un modèle sain relit le contexte complet, sorties d'outils comprises ; seul compte le gain au-delà de cette relecture (E3-T3-reponse-A, -B, -C, -D, -E).

**Retenue 3 — la garantie réduite à l'audit au hasard, avec ses hypothèses mesurées.** La borne est de l'arithmétique d'échantillonnage. Son contenu empirique est ailleurs : la sensibilité de l'audit selon la taille de la touche, la part de trajectoires où tous les audits échouent, le nombre minimal de cases fausses (E3-T3-reponse-A, E3-T3-reponse-D). A fait monter ce type au deuxième rang ; E le garde sous condition d'une agrégation à influence bornée.

**Retenue 4, plus fragile — la loi importée, sous forme réduite.** Chaque loi a été montrée vraie par construction ou aveugle : la racine carrée sort du théorème central limite sur ce banc ; le délai fois le débit se réduit à l'identité de Wald ; la variance d'Allan ignore un décalage constant ; le nombre de reproduction vaut presque 1 sans aucune propagation, par le seul seuil (E3-T2-critique-croisee-A, -B, -C, -D, -E). A, B et D convergent sur une forme plus sûre : prédire, sans paramètre libre et à horizon fini, des courbes de détection sur une famille d'attaques à partir de grandeurs mesurées ailleurs (E3-T3-reponse-A, -B, -D).

Jugement du rédacteur : les retenues 1 et 2 sont les plus fortes. Elles survivent à toutes les critiques, ne dépendent d'aucune nouveauté revendiquée, et conditionnent les trois types.

### 4. Les désaccords qui restent

- Le classement. A : loi, puis garantie, puis mécanisme. B, C, E : loi, puis mécanisme, puis garantie. D : mécanisme, puis garantie, puis loi ; D retire même sa loi (E3-T3-reponse-D).
- La variance d'Allan. C tient l'aveuglement au décalage constant pour une qualité, après passage aux incréments (E3-T3-reponse-C) ; aucun autre modèle n'a revu ce point.
- Le sens de la régression entre activations et texte : C rejette en partie la critique de A et propose une forme symétrique à tester (E3-T3-reponse-C).
- Le certificat conditionnel : B rejette l'objection de circularité de C (E3-T3-reponse-B).
- La sélection par l'instrument : E rejette la critique de A sur sa mesure du gain des activations (E3-T3-reponse-E).
- Le prix de la garantie : l'agrégation à influence bornée de E peut coûter trop de qualité honnête ; non mesuré.
- Les statuts : C et E marquent « vérifié » des références citées de mémoire ou des déductions sous conditions (E3-T2-critique-croisee-A, E3-T2-critique-croisee-B).

### 5. Réserve sur les sources

J'ai contrôlé cinq références sur leur page de résumé arXiv, et non sur le PDF. Aucun chiffre n'en est donc opposable. Wen et al. 2024, « Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats », arXiv 2411.17693 : selon le résumé, la confiance est mise à jour d'une tâche à l'autre au fil du déploiement. Cela répond en partie à la question ouverte de B (E3-T3-reponse-B). Le résumé ne dit rien d'un cumul à l'intérieur d'une trajectoire, et ne prouve pas qu'il soit absent. Greenblatt et al., « AI Control: Improving Safety Despite Intentional Subversion », arXiv 2312.06942, déposé en 2023 (C écrit 2024). Bhatt et al. 2025, « Ctrl-Z: Controlling AI Agents via Resampling », arXiv 2504.10374. Stark 2008, « Conservative Statistical Post-Election Audits », arXiv 0807.4005, Annals of Applied Statistics. Goldowsky-Dill et al. 2025, « Detecting Strategic Deception Using Linear Probes », arXiv 2502.03407. Toutes les autres références sont non vérifiées : Ker et al. 2008, Lorden 1971, Page 1954, Allan 1966, Harris 1963, Vovk et al. 2005 et les autres. Aucune nouveauté n'est établie.

## Revendications

**La question.** Dans un cadre où un défenseur surveille des agents contre un sabotage diffus (audit au hasard, moniteurs du texte et des activations, peu d'exécutions honnêtes de référence), quelles contributions seraient inédites aujourd'hui, peut-être aucune (question-etage3.md) ?

Lettres : A Fable 5.2, B Opus 5.5, C Argon, D Astra, E Carbon (especes.json). Les cinq ne rapportent aucune expérience exécutée. B et D disent ne pouvoir certifier aucune contribution comme inédite (E3-T3-reponse-B, E3-T3-reponse-D).

### Toutes les propositions, groupées par idée

1. **Ce que lit une sonde d'activations : l'intention, la consigne, le contenu des choix ou les poids modifiés.** A, B, C, D, E. Les formes varient selon l'auteur. A propose une courbe du soupçon en fonction du dommage par action. B propose un contrôle par secret bénin et par saboteur distillé. C propose une sonde sur la dynamique des états internes. D propose le gain des activations sur un défenseur sans activations. E propose l'écart entre les activations et ce que le texte en laisse prévoir (E3-T1-conception-A, -B, -C, -D, -E).
2. **La précondition.** Un petit modèle ouvert sait-il saboter de façon diffuse ? Et quelle part de variance est propre à chaque trajectoire honnête ? A, B, C, D, E (E3-T1-conception-A duel 0, -B S1, -E E0 ; E3-T3-reponse-C test B).
3. **La continuation honnête depuis le même état, rejouée par le défenseur.** A : comment employer des références rares. B : rejeu contre jugement. C : rejeu par blocs de plusieurs pas. E : test séquentiel sur des écarts appariés à un tirage honnête du même modèle (E3-T1-conception-A, -B, -C ; E3-T3-reponse-E).
4. **L'accumulation séquentielle du soupçon calibrée sur peu de références.** B, C, E (E3-T1-conception-B C3, -C contribution 1, -E C3).
5. **La furtivité mesurée contre une dégradation sans intention de même dommage.** B (E3-T1-conception-B C1).
6. **L'audit de paires d'actions liées par un graphe de dépendance.** E (E3-T1-conception-E C1).
7. **L'additivité du dommage et le choix de l'unité d'audit.** A, avec un présupposé proche chez B et C (E3-T1-conception-A C2).
8. **Une batterie de vérifications mécaniques comme référence à battre.** B en fait une candidate. A, C et E la posent comme exigence pour chaque instrument (E3-T1-conception-B C0).

### Ce que la confrontation retient, et pourquoi

**Retenue 1, la plus forte : le plan contrôlé de ce que lit la sonde.** Les cinq critiques font la même objection. Un saboteur obtenu par adaptateur de poids diffère du modèle honnête par ces poids. Une sonde peut donc lire l'adaptateur et non le sabotage (E3-T2-critique-croisee-A, -B, -C, -D, -E). Toutes les réponses acceptent l'objection. B scinde sa candidate en deux duels, avec des adaptateurs bénins, un secret bénin portant sur les mêmes décisions, une dégradation dirigée sans intention et des lectures forcées du même texte. B la classe comme sa candidate la plus nette (E3-T3-reponse-B). A passe à un saboteur conditionnel comparé à un témoin conditionnel bénin, à poids identiques, et retire le mot « intention » (E3-T3-reponse-A). C ajoute un adaptateur honnête de même rang (E3-T3-reponse-C). E ajoute ce témoin et un lecteur tiers (E3-T3-reponse-E). D se limite à un modèle gelé et ajoute un défenseur qui connaît déjà la consigne initiale (E3-T3-reponse-D). Cette retenue a deux raisons : l'accord est le plus large après les critiques, et un résultat négatif resterait publiable (E3-T3-reponse-B). *Source vérifiée :* l'article « Detecting Strategic Deception Using Linear Probes » (arXiv 2502.03407, 2025) entraîne ses sondes sur des consignes contrastées. Son résumé ne mentionne aucun témoin d'adaptateur bénin. Le corps de l'article n'a pas été lu.

**Retenue 2 : la continuation honnête depuis l'état déployé, à budget fermé.** A, B et E la gardent sous une forme corrigée. Les critiques ont imposé trois choses : compter le seuil dans le budget, donner au juge le même budget, et rééchantillonner avec le même modèle honnête (E3-T3-reponse-A duel 3′, -B C4′, -E E3′). *Source vérifiée :* « Ctrl-Z: Controlling AI Agents via Resampling » (arXiv 2504.10374, 2025) rééchantillonne les actions de l'agent surveillé pour bloquer et pour incriminer. Cela confirme la distinction revendiquée par A : chez A, la référence est honnête et de même capacité. B déclare un risque de recouvrement (E3-T3-reponse-B).

**Retenue 3, comme première expérience et non comme contribution : la précondition et la part de variance propre à la trajectoire.** A, B, C et E la mettent en premier (E3-T3-reponse-A, -B, -C, -E). D en fait la qualification du banc (E3-T3-reponse-D). Sans elle, les autres duels sont sans objet.

**Retenue 4 : la batterie mécanique, conservée comme référence à battre.** B en retire les tests cachés, qui contenaient la vérité de terrain (E3-T3-reponse-B, point 29).

**Affaiblies ou retirées.**
- **L'additivité.** A retire sa candidate. Avec une attribution par continuation honnête, le dommage devient additif par construction (E3-T3-reponse-A).
- **L'accumulation séquentielle.** Elle bute sur un plancher : la plus petite valeur-p atteignable vaut un sur le nombre de références plus un. Elle bute aussi sur la part de variance propre à la trajectoire (E3-T2-critique-croisee-A, -C, -E). B la déclasse (E3-T3-reponse-B). C et E la gardent, corrigée. *Source vérifiée :* « Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats » (arXiv 2411.17693, 2024) met déjà à jour une croyance sur l'alignement d'une tâche à l'autre.
- **La furtivité contre une dégradation au hasard.** Sa forme initiale était vraie par l'algèbre de la marche aléatoire (E3-T2-critique-croisee-A, -C, -E). B la retire et la remplace par une comparaison à une dégradation dirigée (E3-T3-reponse-B).
- **Le rejeu par blocs.** À budget constant et à incréments indépendants, le gain est exactement nul (E3-T2-critique-croisee-A, -D, -E). C l'accepte et réduit sa candidate à un régime étroit (E3-T3-reponse-C).
- **L'audit de paires sur graphe.** L'attaque était construite le long du graphe audité (E3-T2-critique-croisee-A, -B, -C). E le garde, avec une équipe rouge aveugle (E3-T3-reponse-E). Aucun autre modèle ne le soutient.

*Jugement du rédacteur :* la retenue 1 est la seule portée par les cinq après critiques. La retenue 2 est portée par trois modèles et adossée à une distinction que le résumé de l'antécédent confirme. Le reste dépend de la précondition, qui n'est pas mesurée.

### Les désaccords qui restent

- **Le nombre de contributions inédites.** C qualifie trois problèmes de « véritablement ouverts et inédits » et marque des résultats comme vérifiés (E3-T3-reponse-C). B et D tiennent à zéro contribution certifiable (E3-T3-reponse-B, -D).
- **La contradiction logique dans le plan de D.** C affirme que le plan de D se contredit. D rejette cette nécessité en s'appuyant sur un contre-exemple de E (E3-T2-critique-croisee-C ; E3-T3-reponse-D).
- **Le saboteur par poids.** D refuse ce bras pour sa candidate. A, B, C et E le gardent avec un témoin bénin (E3-T3-reponse-D).
- **Le bon témoin de poids.** A préfère un contraste à poids identiques, avec déclencheur présent ou absent. B veut des adaptateurs bénins distincts (E3-T3-reponse-A, point 6 bis).
- **Les statuts « vérifié ».** A conteste ceux que E attribue à des issues d'un protocole non exécuté (E3-T3-reponse-A). E maintient, contre A, qu'une somme linéaire fixe ne domine pas toujours sa forme quadratique (E3-T3-reponse-E).

### Réserve sur les sources

J'ai vérifié quatre références sur leur page publique d'arXiv : titre, année et résumé seulement. « AI Control: Improving Safety Despite Intentional Subversion » est daté de 2023 (arXiv 2312.06942), alors que C, D et E écrivent 2024. Toutes les autres références, tous les chiffres et tous les seuils (tous dits illustratifs) sont non vérifiés.

## Tirage au hasard

### 1. La question

Un contrôleur dispose d'un hasard que l'agent ne peut ni prévoir ni observer : à quoi peut-il lui servir face à un agent peut-être déloyal, qu'est-ce que cela garantit, et quels usages sont encore peu étudiés pour les agents fondés sur des modèles de langue (question-etage3.md) ?

### 2. Toutes les propositions, par idée

- **Auditer une part tirée au sort, après que l'agent s'est engagé sur son travail.** A, B, C, D, E, F (E3-T1-conception-A à F). B, D et F séparent la dissuasion (l'agent renonce) de la détection (on trouve la faute).
- **Glisser des cas plantés indiscernables** (leurres, sentinelles, marqueurs de fuite). A, B, C, D, E, F.
- **Poser un défi tiré après l'engagement** (preuves interactives, vérification d'un calcul, marche au hasard dans un graphe de justifications). A, B, C, D, E, F.
- **Rejouer l'agent, faire bifurquer ses copies ou les interroger séparément**, pour lire leurs désaccords. A, B, E, F.
- **Aveugler l'agent** : masquer, renommer ou permuter les entités, inverser les polarités, noyer la vraie tâche parmi des leurres. A, C, D, E, F.
- **Rendre la politique de contrôle aléatoire** : seuils tirés, moniteur actif tiré, calendrier mixte. A, B, C, D, E, F.
- **Brouiller le canal** par une paraphrase aléatoire, contre les messages cachés. A, B, F.
- **Tirer les relecteurs, les comités ou les affectations**, contre la collusion, ou pour mesurer un effet causal. A, B, D, F.
- **Bruiter les retours d'audit** pour que l'agent n'apprenne pas le contrôle. A, D, E.
- **Marquer ou authentifier par une clé secrète** les sorties ou l'état. A, B, D, E.
- **Perturber l'agent ou ses entrées** (lissage aléatoire). A, B.
- **Rendre le tirage vérifiable après coup** par un tiers. A ; défi frais, B.
- **Horizon ou relève à un instant tiré** au sort. B, E, F.
- **Sondage à probabilités d'inclusion connues**, pour estimer les fautes restantes. D.
- **Limiter l'exposition par loterie**, sans rien détecter. D.
- **Couper-et-choisir** sur plusieurs copies d'un artefact. F.
- **Élicitation par tirage** (réponse aléatoire). B.

### 3. Ce que la confrontation retient

**a. Isoler ce qu'ajoute le secret : même loi de tirage, tirage révélé contre tirage caché.** C'est la proposition la plus forte. B l'a demandée dans sa critique (E3-T2-critique-croisee-B, sur A et D). A en fait son contraste principal (E3-T3-reponse-A, E2′). D en fait sa première expérience (E3-T3-reponse-D). F l'ajoute dans deux expériences (E3-T3-reponse-F, E1 et E4 corrigées). C l'ajoute comme cinquième bras (E3-T3-reponse-C, C19). B la décline pour la paraphrase, en distinguant secret de la fonction et fraîcheur du tirage (E3-T3-reponse-B, E5′). Elle résiste aux critiques parce qu'elle répond à l'objection commune : chaque protocole mêlait le hasard avec le format, le nombre d'interventions ou l'anonymisation.

**b. Mesurer d'abord si l'agent voit les effets du tirage avant de s'engager.** Les six signalent que la source peut être parfaite et ses effets visibles (section a des six conceptions). Après les critiques, la mesure est séparée selon ce qui se voit avant ou après l'engagement (critiques de C, D, E sur A ; E3-T3-reponse-A, E1′ ; E3-T3-reponse-E, E4′). Elle est protégée par des témoins « réel contre réel » et « générateur contre générateur » (E3-T3-reponse-B, E3′ ; E3-T3-reponse-F, E5). A, B, C, E et F la retiennent.

**c. Un seuil aléatoire ne vaut que contre un agent qui s'adapte.** Toutes les critiques le montrent : contre un agent qui ne s'adapte pas, un seuil fixe fait au moins aussi bien (E3-T2-critique-croisee-A, B, E, F sur C et E). C, E, F et B l'acceptent et en font une condition testée (E3-T3-reponse-C, C21 ; E3-T3-reponse-E, C18 ; E3-T3-reponse-F, point 4 ; E3-T3-reponse-B, section c).

**d. Le défi après engagement sur une structure imposée** (graphe pondéré chez E, arbre hiérarchique chez F). E et F le placent en premier (E3-T3-reponse-E ; E3-T3-reponse-F). Leur premier protocole était vrai par construction : le chemin partait de la conclusion falsifiée (E3-T2-critique-croisee-C et F, sur E). La version corrigée compare le tirage à un audit fixe sur la même structure. Elle survit, mais elle n'est pas encore éprouvée.

**Abandons acceptés.** F retire le couper-et-choisir : auditer l'artefact ouvert puis exécuter les autres ajoute un risque gratuit (E3-T3-reponse-F, point 3). D retire la loterie de diffusion comme filtre de qualité, et la dissuasion mesurée par un simple texte (E3-T3-reponse-D). Tous adoptent une règle de décision par intervalle, avec un effectif fixé d'avance et un verdict « non tranché » (E3-T3-reponse-A à F).

**Sources vérifiées** (pages publiques arXiv, lues le 22 novembre) :
- « AI Control: Improving Safety Despite Intentional Subversion » (arXiv 2312.06942) : première version du 12 décembre 2023, avec mention d'une version de conférence non datée. La date 2023 de A et B est juste pour la prépublication.
- « Ctrl-Z: Controlling AI Agents via Resampling » (arXiv 2504.10374, avril 2025) : 257 tâches d'administration système **à plusieurs étapes**. La phrase de E, qui le réduit à des « extraits de code courts », est donc inexacte (E3-T1-conception-E, U7).
- « Games for AI Control » (arXiv 2409.07985, septembre 2024) : titre et date conformes à B.

### 4. Les désaccords qui restent

- **Quelle expérience faire en premier.** Chacun garde la sienne. A choisit la visibilité des effets du tirage et la recherche bibliographique (E3-T3-reponse-A). B choisit la recherche bibliographique (E3-T3-reponse-B). C choisit la permutation à polarité opposée entre copies (E3-T3-reponse-C). D choisit le duel révélé contre caché (E3-T3-reponse-D). E choisit le graphe pondéré (E3-T3-reponse-E). F choisit l'arbre hiérarchique (E3-T3-reponse-F).
- **Les usages les moins étudiés.** Les listes ne se recouvrent guère. A : aveuglement, bruit des retours, tirage vérifiable, défi après engagement, affectation contre la collusion. B : horizon aléatoire, défi frais, contre-vérification, dissuasion. D : sondage, retours privés. E : graphe, aveuglement profond, bruitage. F : relèves, aveuglement, interrogation croisée, défi sur texte long. Aucune liste n'est vérifiée.
- **La dissuasion.** D la retire au profit d'une conséquence exécutée en simulateur. B la garde avec un bras « récompense » (E3-T3-reponse-B, E1′). A n'a plus aucune expérience qui la teste (E3-T3-reponse-A, section c).
- **Points rejetés par leurs auteurs.** Pour B, optimiser l'attaquant contre une paraphrase fixe est la menace elle-même, pas une fuite, comme le disait C (E3-T3-reponse-B, R27). A refuse d'exiger un corpus naturel (E3-T3-reponse-A, E4). E corrige B sur la transformation affine (E3-T3-reponse-E, C14).
- **Jugement du rédacteur.** La permutation de C reste fragile : contre un biais qui suit le fond et non l'étiquette, sa divergence est nulle, et C le reconnaît lui-même (E3-T3-reponse-C, section c, point 4).

### 5. Réserve sur les sources

Trois références seulement ont été vérifiées, sur leur page arXiv. Les pages de l'éditeur pour « Private Coins versus Public Coins in Interactive Proof Systems » et pour « The Reusable Holdout » ont refusé l'accès : l'attribution de l'équivalence entre hasard public et hasard privé (à Babai ou à Goldwasser et Sipser) et toutes les autres références sont **non vérifiées**. Tous les seuils, effectifs et coûts des cellules sont illustratifs.

## Question générale

Lettres des modèles (especes.json) : A Fable 5.2, B Opus 5.5, C Argon, D Astra, E Carbon. Aucun chiffre ci-dessous n'est mesuré : ce sont des seuils d'exemple proposés par les modèles, non vérifiés.

### 1. La question

Les trois articles prévus (un agent seul sur une longue tâche, plusieurs copies d'un même modèle, des moniteurs visés par l'adversaire) partagent-ils une question qui les rend plus utiles ensemble que séparément, et laquelle (question-etage3) ?

### 2. Toutes les propositions, groupées par idée

**a. Une porte d'entrée : le sabotage diffus existe-t-il chez un modèle de huit milliards de paramètres ?** On vérifie d'abord qu'un sabotage peut abîmer le résultat sans qu'aucun acte isolé ne trahisse. On vérifie aussi qu'une règle mécanique simple ne suffit pas déjà. A, B, C, D, E (E3-T1-conception-A, -B, -E ; E3-T3-reponse-C, -D).

**b. Le transport d'un réglage d'un cadre à l'autre.** On règle un détecteur ou une règle de vérification sur un cadre. On le gèle. On regarde s'il tient ailleurs.
- A : une même courbe « dégât contre détection », puis le regret d'une règle d'allocation transférée (E3-T1-conception-A).
- B : une seule fonction de quelques grandeurs mesurables (signal par acte, nombre d'actes, ressemblance entre l'agent et sa référence) prédit les trois cadres. La fonction est déposée avant de voir les cadres 2 et 3 (E3-T1-conception-B).
- D : une règle qui choisit quoi vérifier, apprise sans voir un régime, doit encore bien choisir dans ce régime (E3-T1-conception-D).
- E : une règle de tri gelée sur les articles 1 et 2, testée sur l'article 3 (E3-T3-reponse-E).

**c. Une cascade de vérifications sous budget.** Le score cumulé des moniteurs déclenche une exécution de comparaison, qui déclenche une vérification coûteuse. La cascade doit battre les mêmes instruments employés séparément. C, E (E3-T1-conception-C, -E).

**d. L'accumulation des preuves dans le temps.** Somme cumulée des scores, test séquentiel, taille d'échantillon utile quand les étapes se ressemblent. A, B, C, E (E3-T1-conception-A, -B, -C, -E).

**e. Les copies d'un même modèle partagent leurs erreurs.** Une nouvelle exécution du même modèle reproduit le même biais. Il faut donc des comparaisons modifiées : références d'une autre famille (B), entrées perturbées (C), preuves inversées (E), ou ne pas compter un accord comme une confirmation indépendante (D). A teste des copies qui se coordonnent sans plan commun (E3-T3-reponse-A).

**f. Le moniteur visé : l'évasion a-t-elle un prix ?** Échapper à un moniteur coûterait du dégât ou laisserait une trace ailleurs. A, C, E (E3-T1-conception-A, -C, -E). B y voit une simple baisse du signal par acte (E3-T1-conception-B).

### 3. Ce que la confrontation retient, et pourquoi

**Retenue 1 : la porte d'entrée d'abord.** Après les critiques, les cinq modèles la placent en premier (E3-T3-reponse-A, -B, -C, -D, -E). Elle a été durcie, pas affaiblie. Les critiques ont montré qu'un acte peut être probable chez l'honnête et pourtant informatif (E3-T2-critique-croisee-A, -B sur E). E l'a accepté et a rendu son banc continu (E3-T3-reponse-E). A calcule le signal par acte aux seuls points de choix (E3-T3-reponse-A). Une issue négative de cette porte rend la question sans intérêt à cette échelle. Tous l'écrivent.

**Retenue 2 : le transport d'un réglage gelé, jugé contre un témoin fort.** A, B, D et E convergent vers ce même test après les critiques (E3-T3-reponse-A, -B, -D, -E). Les versions faibles sont tombées :
- l'équivalence « copies » contre « agent à contexte coupé » de A était vraie par construction. A l'a reconnu (E3-T2-critique-croisee-B, E3-T3-reponse-A) ;
- la fonction de B n'était pas identifiable sur le seul cadre 1. B a adopté un plan factoriel et une formule analytique sans ajustement comme témoin (E3-T2-critique-croisee-C, -E ; E3-T3-reponse-B) ;
- la règle de D par filiation des documents était vraie par construction du générateur. D l'a retirée au profit d'une règle enrichie (E3-T3-reponse-D).

**Retenue 3 : des contrôles devenus communs.** Chaque modèle les a acceptés après critique :
- un saboteur obtenu par ajustement des poids, sans consigne dans le contexte : la sonde ne doit pas seulement lire la consigne (C à l'origine ; E3-T3-reponse-B) ;
- un ajustement honnête de même taille : la sonde ne doit pas seulement voir que les poids ont changé (E3-T3-reponse-A, -B, -C) ;
- un honnête qui se trompe de bonne foi, ou qui propage une erreur de départ (E3-T3-reponse-A, -B, -C) ;
- un contrôle positif de l'attaque : une attaque ratée ne doit pas passer pour une défense solide (E3-T3-reponse-A, -C, -E) ;
- l'hypothèse rivale est le complément exact, et un intervalle qui chevauche le seuil donne « non tranché » (convention de D ; E3-T3-reponse-A, -E) ;
- des parts de données disjointes pour régler, calibrer et tester (E3-T3-reponse-A, -B, -C).

**Retenue 4 : la cascade de C, sous une forme corrigée.** Elle se compare désormais à un témoin qui garde la somme cumulée, dans un plan croisé « mémoire » sur « couplage » (E3-T2-critique-croisee-A, -E ; E3-T3-reponse-C). Sa première version opposait la cascade à un témoin amputé.

**Jugement du rédacteur.** Les deux propositions les plus fortes sont la porte d'entrée commune et le transport d'un réglage gelé. Elles réunissent le plus d'accords et ont le mieux résisté. La seconde est la seule vraie problématique d'ensemble. Elle répond aussi à la question si le résultat est négatif, car un transport qui échoue justifie trois articles distincts.

### 4. Les désaccords qui restent

- **Unir ou non.** A ne peut plus affirmer qu'une problématique d'ensemble existe (E3-T3-reponse-A). B l'attend, mais prévoit une rupture sur les copies (E3-T3-reponse-B). C et E l'attendent sous condition (E3-T3-reponse-C, -E). D la fait dépendre du transfert du choix de vérification (E3-T3-reponse-D).
- **Ce qui unit.** Une loi prédictive (B), une règle d'allocation (A, D, E) ou une synergie de cascade (C).
- **Le type de contribution.** Test de suffisance (B), loi connue ailleurs transférée (A), mécanisme (C, E), critère expérimental (D).
- **La référence honnête en déploiement.** B estime que le défenseur n'en a pas quand l'agent est l'adversaire. C répond qu'un étalonnage avant déploiement suffit (E3-T2-critique-croisee-B, E3-T3-reponse-C).
- **Le signe de l'effet de la ressemblance.** C le juge vrai par construction. B réplique que l'effet mécanique va dans l'autre sens (E3-T2-critique-croisee-C, E3-T3-reponse-B).
- **La victoire d'une règle mécanique.** B y voit un défaut du banc de A. A y voit une issue légitime, à ne pas empêcher (E3-T2-critique-croisee-B, E3-T3-reponse-A).
- **La comparaison par inversion des preuves (E).** Elle reste aveugle à certains biais. E l'a étendue à trois transformations, sans mesure (E3-T2-critique-croisee-C, E3-T3-reponse-E).

### 5. Réserve sur les sources

Toutes les références des cellules sont citées de mémoire. J'en ai vérifié quatre sur leur page arXiv : titre, auteurs et date seulement, pas le contenu. « AI Control: Improving Safety Despite Intentional Subversion » (2312.06942) : première version le 12 décembre 2023, révisée en juillet 2024 ; cela tranche le désaccord de date. « Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats » (2411.17693) : novembre 2024. « Ctrl-Z: Controlling AI Agents via Resampling » (2504.10374) : avril 2025. « Obfuscated Activations Bypass LLM Latent-Space Defenses » (2412.09565) : décembre 2024. Toutes les autres références ne sont pas vérifiées, ni aucune affirmation sur ce que contient un article ou sur une absence d'antériorité.

