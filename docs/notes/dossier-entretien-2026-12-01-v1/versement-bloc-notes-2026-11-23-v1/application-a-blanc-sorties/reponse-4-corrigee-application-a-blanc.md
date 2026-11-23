# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v3` (empreinte du module 95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHQdZRwg8DgdF65T5zUd`
- Heure (UTC) : 2026-11-22T05:27:27Z
- Réglages : effort `high`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-4-problematique-papier-v1.md` — sha256 874eaefed5cc8c61c59a37005f5a98c5b772f58ec5337567222fda56eadb23ab (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/contexte-programme-v1.md` — sha256 534ed7a288fc0729377654c6060ae900ac5ec76c8d6fa2518bee4f1239464a2b (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-2/relecture-fable-api.md` — sha256 542b7bfc86497c0c9bc45ed7f1651162a47789b6b2f00325f989daaac42c59f3 (compagnon : vérifié)
  - remarques : `docs/programme-controle-ia-v2.md` — sha256 2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/lecture-trois-arxiv-v1.md` — sha256 0f8145e61fd8ab4ec5a821e3d21a3853dc6991b7d94c4c3cc001c3533222d464 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/lecture-karkada-buehler-v1.md` — sha256 dc38a409a721f7d334dc9ed3d9323bdf454e713a97ff3117d026def7cda684e9 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/lecture-depots-github-v1.md` — sha256 02aa3d80c6edd6aa8972a27d7e47a31f7a8161b0fc062ddd969798c74da58ac0 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/lecture-energy-based-reasoners-v1.md` — sha256 21e9dab17e199272feab6f85e2fca75762723ab6db9738d4d33cfb7262919ef4 (compagnon : vérifié)
- Empreinte de l'invite envoyée : 75705c096884aee40e485cd6c75851b67c11ff06265b1ab57011c1fc17ffae8d
- Jetons : entrée 31869, sortie 22846 (dont réflexion 14016), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.168792 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 4 — la problématique du papier : réponse approfondie

**Conclusion d'abord.** La question du papier A n'a pas été réécrite après N-075, N-076 et N-077, et c'est pourquoi elle manque. La thèse de la version 2 du programme est une thèse de mécanisme à garantie (« l'accumulation de scores de sondes détecte, avec une garantie toujours valide »), et ces trois décisions lui ont retiré la garantie. Je recommande une question de type (iii), héritée de la stéganographie et de la comptabilité des matières : **combien de dommage un saboteur diffus peut-il cacher, selon l'horizon et la qualité de la référence honnête ?** Le type (ii) y entre comme mesure secondaire (la sonde chiffrée en audits économisés). Le type (i) y entre comme limite déclarée. L'antériorité la plus proche de cette loi vient de la dissimulation d'information ; elle n'est citée ni dans le programme ni dans la demande 2, et elle touche aussi le lemme d'additivité.

**Réserves.**
- Je n'ai pas recalculé les empreintes des pièces.
- Je cite de mémoire : toute antériorité a le statut **« rapporté, non vérifié sur PDF »**.
- Ma connaissance s'arrête avant 2026. Je ne confirme aucun des identifiants arXiv de 2026 cités par le programme ou par les lectures jointes.
- Les lectures jointes sont des rapports d'agent ; leurs chiffres ne sont pas opposables.
- Je ne connais ni l'état de la porte G0 ni le texte exact des décisions.
- « Sans nom de personne » contredit « antériorité nommée » : je ne nomme que les auteurs des travaux cités.

---

## 1. Ce qu'un expert ferait et qui n'est pas demandé

- **Séparer trois objets** [PROPOSITION] : la problématique (ce que le champ ignore), la question (ce que le papier tranche), la revendication (ce que le résultat autorise). La demande les confond.
- **Dater la rupture** [FAIT RAPPORTÉ, pièces]. La version 2 promet une détection à garantie. N-075 fait des sondes « un accélérateur, non une garantie ». N-076 subordonne toute accumulation à une référence déclarée. N-077 retire la marge. Le papier A a gardé son plan d'expériences et perdu sa thèse.
- **Traiter (i), (ii), (iii) comme trois rôles** [PROPOSITION] : limite, instrument, question. Ce ne sont pas trois papiers concurrents.
- **Chercher l'antériorité dans le domaine d'origine** [PROPOSITION]. Les « trois planchers » du collisionneur ont la forme de la loi de la racine carrée de la capacité stéganographique. Non relevé dans les pièces lues à cette date ; Khilar 2026 transpose la loi au suivi des usages.
- **Soumettre chaque question au test de l'usage** [PROPOSITION] : qui agirait autrement selon la réponse ?

## 2. Données brutes de départ

- Les scores de sonde pas à pas et les issues jugées sur des paires d'exécutions honnêtes par tâche. Les aires sous la courbe agrégées ne suffisent pas.
- Les verdicts de l'oracle sur les dommages plantés, lecteur par lecteur.
- Les PDF de la littérature sur la dissimulation d'information (liste sous Q1), lus page à page.
- Le texte scellé de la préinscription de G1 et l'état réel de la porte G0.
- Le texte exact de N-075, N-076 et N-077.
- Les dates des appels à communications visés. Je ne les ai pas.

## 3. Méthodes et outils

- **Régression en échelles logarithmiques** du seuil d'alarme honnête contre l'horizon, avec rééchantillonnage par tâche puis par blocs, car les pas d'une trajectoire sont dépendants.
- **Variance d'Allan** des scores honnêtes le long de l'horizon [PROPOSITION]. C'est l'outil de métrologie qui sépare un bruit qui se moyenne d'une dérive qui ne se moyenne pas (Allan, 1966, « Statistics of atomic frequency standards »).
- **Tableau de revendications**, élément par élément, contre les pages de l'antériorité.
- **Monde planté en simulation**, puis prévision scellée par condensat avant toute mesure réelle.
- **Bases de mots et sonde aléatoire appariée en covariance**, déjà prévues par le programme.

## 4. Ce qui vérifie hors du directeur et de Claude

- Un spécialiste de la stéganalyse, à qui l'on demande : « ceci est-il votre loi ? »
- Un statisticien du sondage ou de l'inférence séquentielle, qui lit le tableau de revendications.
- Une équipe tierce qui écrit le mode tenu à l'écart (N-054).
- La reproduction sur une seconde famille de modèles.
- L'essai « jumeau contre jumeau », dont l'issue ne dépend de l'avis de personne.
- Le préenregistrement horodaté, puis la relecture par les pairs.

## Demande reformulée

« Quelle question, écrite avant les résultats sous forme de prévision scellée, le papier A peut-il trancher avec le harnais existant, de sorte que les deux issues soient publiables, que l'antériorité du domaine d'origine soit citée comme source et non découverte par un relecteur, et que les papiers B et C posent la même question sur un autre axe ? Classe les types (i), (ii), (iii) par ce que chacun permet de réfuter, non par ce qu'il permet de promettre. »

---

## (a) Formulations candidates

### Q1 — Loi d'échelle du dommage caché (type iii, avec ii en mesure)

*« Sur de vrais agents, le dommage qu'un sabotage diffus peut cacher croît-il comme la racine de l'horizon tant que la référence honnête est connue, puis linéairement dès qu'elle est estimée, et l'accès aux activations change-t-il l'exposant ou seulement la constante ? »*

- **Réponse attendue, falsifiable** [HYPOTHÈSE]. Trois prévisions scellées :
  - l'exposant reste un demi sous dépendance courte, qui gonfle la constante (Filler, Ker et Fridrich 2009) ; seule une dérive le long de la tâche le change ; l'hétérogénéité entre tâches ajoute un terme linéaire ;
  - à unités égales, la transition est en n ≈ m par construction (Ker 2010, corollaire 1) ; ce n'est pas une prévision ;
  - la sonde réduit la constante d'un facteur k et laisse l'exposant inchangé.

  Chaque prévision tombe séparément.
- **Portée de la mesure** [HYPOTHÈSE]. Le versant honnête (seuil d'alarme contre horizon) ne dépend d'aucun saboteur : c'est la part de (i) qui survit. Le versant saboté, mesuré sur les organismes du programme, donne une borne basse de ce qu'un saboteur optimal cache. Il reste descriptif, ce qui est conforme à N-077.
- **Intérêt** [HYPOTHÈSE]. Elle donne une règle de dimensionnement : combien d'exécutions honnêtes pour tel horizon. Les rédacteurs de dossiers de sûreté et les concepteurs d'évaluations de contrôle la citeraient, faute de chiffre aujourd'hui.
- **Antériorité la plus proche** [FAIT RAPPORTÉ pour l'existence, HYPOTHÈSE pour la proximité ; rapporté, non vérifié sur PDF] :
  - Ker, 2006, « Batch steganography and pooled steganalysis » ; Ker, 2007, « A capacity result for batch steganography » ;
  - Ker, Pevný, Kodovský, Fridrich, 2008, « The square root law of steganographic capacity » ;
  - Ker, 2010, « The square root law in stegosystems with imperfect information » (mémoire incertaine : traite le cas où la source de couverture est apprise par estimation) ;
  - Bash, Goeckel, Towsley, 2013, « Limits of reliable communication with low probability of detection on AWGN channels » ;
  - Avenhaus, Jaech, 1981, « On subdividing material balances in time and/or space » (mémoire incertaine) ;
  - Meng, 2018, « Statistical paradises and paradoxes in big data (I) », pour le biais qui ne se moyenne pas ;
  - Donoho, Jin, 2004, « Higher criticism for detecting sparse heterogeneous mixtures », pour la frontière entre signaux rares et forts (le maximum suffit) et signaux denses et faibles (la somme est requise).
- **Conséquence pour le programme** [HYPOTHÈSE]. Le lemme d'additivité (noté 0,75 en originalité) et le contraste entre maximum par action et accumulation pourraient être occupés par ces travaux. Je ne peux pas vérifier arXiv 2601.20022 et 2606.10456, cités par le programme. Ils sont à lire avec.
- **Différence résiduelle** [HYPOTHÈSE]. Ker 2010 traite la référence estimée ; reste non trouvée, dans les pièces lues, leur mesure sur des scores de sondes d'agents. Leur mesure sur des agents, avec une référence estimée, une issue jugée et un moniteur interne, m'est inconnue. Chance de rester inédite : 0,5.
- **Acquis** [FAIT RAPPORTÉ, pièces]. Essai « jumeau contre jumeau » réclamé par quatre modèles, simulation du lemme, organismes à dose-réponse, cibles semées, plan deux par deux.

### Q2 — La sonde en économie d'audit (type ii, ramené à une mesure)

*« À certificat égal sur le dommage, combien d'audits une sonde interne figée à l'engagement économise-t-elle face à un juge de texte et à des bases de mots, mode tenu à l'écart compris ? »*

- **Réponse attendue** [HYPOTHÈSE]. Facteur au moins k, scellé. Une issue nulle est probable (dilution par les accidents honnêtes). Chance que l'énoncé soit vrai : 0,35, comme en demande 2.
- **Intérêt** [HYPOTHÈSE]. Une unité commune pour comparer des moniteurs, utile à qui arbitre entre acheter des audits et construire des sondes.
- **Antériorité** [FAIT RAPPORTÉ, demande 2] : Shekhar, Xu, Lipton, Ramdas, 2023 ; Angelopoulos et collaborateurs, 2023 ; Zrnic, Candès, 2024. La méthode est occupée ; seule l'unité de mesure reste.
- **Acquis.** Les mêmes paires que Q1.

### Q3 — Ce que mesure la sonde (type iii, hérité de la psychométrie)

*« Une sonde de sabotage lit-elle l'intention, la présence d'une instruction, la conscience d'être évalué ou une régularité du texte, et ce construit prédit-il sa tenue sous attaque ? »*

- **Réponse attendue** [HYPOTHÈSE, hypothèse H8 du programme]. Une sonde entraînée sur l'instruction cachée échoue sur l'organisme affiné ; le rang de validité prédit le rang de robustesse.
- **Intérêt** [HYPOTHÈSE]. Les équipes de sondes de tromperie la citeraient ; elle prolonge la question unique de la version 2.
- **Antériorité** [rapporté, non vérifié sur PDF] : Cronbach, Meehl, 1955, « Construct validity in psychological tests » ; Hewitt, Liang, 2019, « Designing and interpreting probes with control tasks » ; Goldowsky-Dill, Chughtai, Heimersheim, Hobbhahn, 2025, « Detecting strategic deception using linear probes ».
- **Apport des lectures jointes** [FAIT RAPPORTÉ, agent de lecture]. Trois contrôles :
  - des bases tirées des seules statistiques de mots (Karkada et collaborateurs) ;
  - un contraste apparié étalonné sur un nul neutre (article sur la science des matériaux) ;
  - un test de nécessité sur plusieurs directions, la redondance pouvant tromper une direction unique (Schiffman).
- **Faiblesse** [HYPOTHÈSE]. Avec peu de sondes et peu d'attaques, « prédit » repose sur une poignée de points. Originalité notée 0,40 par le programme.
- **Acquis.** Organismes des familles (i) et (ii), contrôles croisés, plancher aléatoire.

### Q4 — La part universelle (type i, en frontière)

*« Quelle part de la protection contre un sabotage jamais vu tient sans hypothèse sur l'attaque, et quelle part tombe sur un mode tenu à l'écart ? »*

- **Réponse attendue** [HYPOTHÈSE]. L'audit garde sa couverture ; la sonde perd du rappel.
- **Défaut** [FAIT RAPPORTÉ, demande 2]. La première moitié est vraie par construction, donc non revendicable. La seconde repose sur un seul mode : c'est une anecdote, non une universalité.
- **Antériorité** [rapporté, non vérifié sur PDF] : Greenblatt, Shlegeris, Sachan, Roger, 2023, « AI Control: Improving Safety Despite Intentional Subversion » ; Dresher, 1962, « A sampling inspection problem in arms control agreements ».
- **Acquis.** Mode tenu à l'écart, plancher d'audit.

**Lectures non retenues** [FAIT RAPPORTÉ, HYPOTHÈSE pour la pertinence].
- L'article sur les raisonneurs à énergie ne touche aucune des questions.
- Le protocole d'audit d'affirmations corrompues de DiscoveryAgent recoupe les dommages plantés. Sa limite (erreurs insérées par un modèle) est celle d'un papier, non un trou du champ.
- L'édition de poids par miroir pourrait fournir un organisme pour le mode tenu à l'écart ; rien n'est établi.

---

## (b) Classement et recommandation

**Classement** [PROPOSITION] : Q1, puis Q2 (dans le même papier), puis Q3 (repli), puis Q4 (section de limites).

**Recommandation : (iii) pour la question, (ii) pour la mesure, (i) pour la limite.**

| Choix | Ce qu'il coûte | Avant fin 2026 | Premier semestre 2027 |
|---|---|---|---|
| (i) robustesse universelle | Plusieurs familles tenues à l'écart, une équipe rouge tierce. Contredit N-077. Irréfutable avec un seul mode. | Rien, sauf une note de position. | Au mieux une frontière négative. |
| (ii) mécanisme inédit | Dépend du succès de G1. Exposé à une publication externe (une équipe a annoncé des tests toujours valides sur sondes). Chance d'être vrai et encore inédit à mi-2027 : 0,25. | Rien : G1 tombe fin décembre. | Papier A si G1 passe, résultat négatif sinon. |
| (iii) phénomène hérité | Renoncer au titre « nouveau détecteur ». Lire six à huit PDF hors du domaine. Trouver un relecteur de stéganalyse. Risque du reproche « évident ». | Prévision scellée et versant honnête sur l'essai « jumeau contre jumeau ». | Papier A complet. B et C héritent du cadre. |

Le calendrier est celui de la version 2 [FAIT RAPPORTÉ]. Sa tenue est une HYPOTHÈSE, l'état de G0 m'étant inconnu. Les chances sont des jugements.

**Arguments** [HYPOTHÈSE sauf mention] :
- Deux issues ferment quelque chose si le plan a la puissance de les séparer ; sinon l'issue est indéterminée. Si la loi tient, on dispose d'une règle de dimensionnement. Si elle ne tient pas, c'est l'agent honnête réel qui pose problème, et quatre modèles sur cinq demandaient de le mesurer d'abord [FAIT RAPPORTÉ, contexte].
- **Elle répond au reproche « évident ».** La loi est le nul. Le contenu empirique tient en trois inconnues que la statistique élémentaire ne fixe pas : l'exposant réel du bruit honnête, le point de bascule (m ou m divisé par le taux d'audit), l'effet de la sonde sur la constante.
- **Elle s'accorde avec les décisions.** Aucune méthode n'est revendiquée. La règle de la référence est l'application du corollaire 1 de Ker 2010 ; rien n'y est revendiqué. « Accélérateur » reçoit une unité.
- **Elle ne change pas la porte G1.** Le plan deux par deux mesure la constante.
- **Elle unifie A, B et C** [PROPOSITION]. Question d'ensemble : *quel est le bilan d'incertitude d'un moniteur sous adversaire ?* A établit le terme d'horizon. B établit le terme de corrélation entre copies, soit la même loi indexée par agent. C établit l'erreur systématique que l'adversaire induit dans l'instrument, le gain g. Q3 en donne le versant qualitatif.

---

## (c) Titre et résumé

**Titre** [PROPOSITION] : « Ce qu'un saboteur diffus peut cacher : loi d'échelle du dommage indétectable et prix de la référence honnête chez des agents de langue »

**Résumé** (brouillon écrit avant résultats ; les crochets attendent les mesures) :

Un saboteur diffus dégrade une longue tâche par des actes dont aucun n'est suspect. Nous demandons combien de dommage il peut cacher, et de quoi cette quantité dépend. La stéganographie et la comptabilité des matières donnent un modèle nul : pour des pas indépendants et une référence de m pas, le dommage indétectable est d'ordre √(n + n²/m) ; il n'est linéaire qu'à référence bornée ou fautive (Ker 2010). Nous mesurons cette loi sur des agents de langue ouverts, avec des dommages plantés, un audit tiré au hasard et des exécutions honnêtes jumelles. Trois prévisions étaient scellées avant mesure : l'exposant du bruit honnête, l'horizon de bascule, et le facteur par lequel une sonde linéaire sur les activations réduit le nombre d'audits à certificat égal, face à un juge de texte et à des bases de mots. Nous rapportons [résultats], mode de sabotage tenu à l'écart compris. Prévision scellée, non constat : la sonde change la constante, non l'exposant. La taille de la référence fixe l'horizon défendable (Ker 2010, corollaire 1).

---

## (d) Ce qui ferait changer la recommandation

- **Antériorité défavorable.** La lecture des PDF montre que la bascule sous référence estimée a déjà été mesurée sur des agents. Q2 passe alors en tête, avec Q3.
- **Bascule hors de portée.** L'essai « jumeau contre jumeau » montre qu'une référence par régime tient le niveau à tous les horizons atteignables. Le papier devient Q2 avec Q3.
- **G1 franchie largement, mode tenu à l'écart compris.** Le type (ii) reprend le titre et la loi devient le cadre d'analyse.
- **Publication externe du cœur séquentiel sur sondes.** Le type (ii) tombe et le type (iii) se renforce.
- **Organismes sans dose-réponse.** Le versant saboté n'est plus mesurable : le papier se réduit au versant honnête et à Q3.
- **Lieu de publication exigeant une méthode nouvelle.** Le type (iii) y serait mal reçu.

---

## Décisions qui reviennent au directeur

**Décision 1 — Fixer le type de la question du papier A.**
- *Enjeu.* Sans question réécrite, G1 produira des chiffres sans thèse.
- *Option a : (iii) en question, (ii) en mesure, (i) en limite (Q1 avec Q2).* Avantage : deux issues publiables, accord avec N-075 à N-077. Inconvénient : pas de détecteur nouveau au titre.
- *Option b : garder la thèse de mécanisme de la version 2.* Avantage : titre fort si G1 passe. Inconvénient : garantie déjà retirée, antériorité menaçante.
- *Option c : viser (i).* Avantage : ambition. Inconvénient : irréfutable avec les moyens actuels.
- *Recommandation.* Option a. Confiance : 0,65.

**Décision 2 — Faire lire la littérature de dissimulation d'information avant de sceller la prévision, et réviser la note d'originalité du lemme.**
- *Enjeu.* Un relecteur peut y reconnaître le lemme et les « trois planchers ».
- *Option a : lecture sur PDF maintenant, avec avis d'un spécialiste de stéganalyse.* Avantage : cadrage sûr, loi citée comme héritage. Inconvénient : quelques jours.
- *Option b : après G1.* Avantage : aucun retard. Inconvénient : prévision scellée dans un cadre peut-être occupé.
- *Recommandation.* Option a. Confiance : 0,75.

**Décision 3 — Choisir ce qui sort avant la fin de 2026.**
- *Enjeu.* Cinq semaines restent ; seul le versant honnête est atteignable.
- *Option a : prévision scellée, puis note courte sur le versant honnête si l'essai est complet.* Avantage : date d'antériorité, résultat indépendant de tout saboteur. Inconvénient : charge en parallèle de la phase 1.
- *Option b : prévision scellée seule, sans publication.* Avantage : aucune dispersion. Inconvénient : rien de visible en 2026.
- *Option c : note de position.* Avantage : rapide. Inconvénient : sans mesure, contraire à l'esprit de la règle anti-faux-gap.
- *Recommandation.* Option a, repli sur b si l'essai n'est pas complet mi-décembre. Confiance : 0,55.

**Décision 4 — Garder la porte G1 et lui adjoindre les trois prévisions de Q1.**
- *Enjeu.* Changer une porte fixée coûte ; ne rien ajouter laisse la loi hors du papier.
- *Option a : G1 inchangée, prévisions ajoutées et scellées avant.* Avantage : continuité. Inconvénient : préinscription plus lourde.
- *Option b : remplacer G1 par l'exposant et le facteur k.* Avantage : cohérence. Inconvénient : rupture avec les décisions antérieures.
- *Recommandation.* Option a. Confiance : 0,7.

**Décision 5 — Dire la question commune à A, B et C.**
- *Enjeu.* Trois papiers sans question commune se lisent comme trois sujets.
- *Option a : garder « que mesure vraiment un moniteur ? » et y loger le bilan d'incertitude comme forme chiffrée.* Avantage : continuité avec la version 2. Inconvénient : deux formulations à tenir.
- *Option b : remplacer par le bilan d'incertitude.* Avantage : une seule grandeur. Inconvénient : écarte la validité de construit, qui est le repli.
- *Recommandation.* Option a. Confiance : 0,6.

---

## Question neutre pour le collisionneur

Un agent de langue accomplit une longue tâche de recherche ou d'analyse. Un adversaire peut en dégrader le résultat par petites touches dont aucune n'est suspecte isolément. Le défenseur dispose de moniteurs qui lisent le texte, de moniteurs qui lisent les activations internes, d'exécutions honnêtes de référence en nombre limité et d'un budget de vérifications coûteuses.

Une équipe veut écrire un article scientifique dans ce cadre et hésite entre trois types de contribution :
1. une garantie de robustesse tenant contre des attaques jamais vues ;
2. un mécanisme nouveau de détection ou de contrainte ;
3. un phénomène, une loi ou une grandeur connus dans une autre discipline, retrouvés et mesurés chez des agents.

Pour chaque type :
- formulez la meilleure question de recherche en une phrase interrogative ;
- donnez la réponse attendue sous une forme réfutable ;
- nommez l'antériorité la plus proche (auteurs, année, titre), en disant si vous la citez de mémoire ;
- décrivez l'expérience, réalisable en deux mois sur un modèle ouvert de huit milliards de paramètres, qui la trancherait ;
- dites quelle issue rendrait la question sans intérêt.

Classez ensuite les trois types. Dites ce qui vous ferait changer de classement. Signalez tout quatrième type que l'énumération oublie. N'attribuez aucune nouveauté sans dire comment la vérifier.

FIN DE LA RÉPONSE
