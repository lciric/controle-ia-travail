# Cellule A — Tour III.1 : conception ciblée, à l'aveugle

## 0. Pièces absentes ou coupées

- K : parties 2 à 6 non servies (déclaré par la question) ; je ne m'appuie que sur la partie 1.
- La « méta-conception v6.3 » de la pièce C citée dans S (bisociation) n'est toujours pas dans les faits ; comme au tour du 26 octobre, rien ici ne conclut sur la recombinaison bisociative.
- La question cite « pièce 4 », « pièce 4 bis », « couche 1 bis », « comparaison d'échelle », « relève de Gemini » : aucune de ces pièces n'est servie ; je les traite comme des noms, pas comme des contenus.
- M est une position non vérifiée ; ses chiffres (0,88–0,91 ; 0,92–0,98 ; devis 10 $ / 60 $ / 60 $) restent RAPPORTÉ-non-audité.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | supposition | statut | ce que les faits disent |
|---|---|---|---|
| 1 | « Les chercheurs publiés proposent mieux que nous » | HYPOTHÈSE | Aucune mesure de proposition n'existe dans les faits, ni chez eux (la question renvoie à des pages, non à des PDF audités, R7), ni chez nous : le proposeur de v7 est **scripté** (X1 : « le proposeur simulé joue des gabarits » ; X2). On compare un agent inexistant à un système non mesuré. |
| 2 | Le juge est une « garantie » | RAPPORTÉ en simulation ; HYPOTHÈSE sur banque réelle | E1/E2 : contrôles fatals à 0–1 sur 1 000, mais K = 3, d = 2, 200 tirages (E1, E2 : « n'autorise pas »). Sur la banque réelle T0.5 : **0 témoin vrai promu sur 20**, « pas de dents » (X2). Le juge n'a jamais promu quelque chose de vrai sur du réel. |
| 3 | « Proposer » se sépare proprement de « juger » dans les systèmes à boucle complète | HYPOTHÈSE | La question elle-même a dû corriger la v1 sur ce point ; ce que perd l'arbre de recherche privé de son relecteur n'est documenté nulle part. |
| 4 | Juge figé + nul composite ⇒ le proposeur ne peut pas « apprendre à plaire » | HYPOTHÈSE, partiellement contredite | K : l'aptitude est dégénérée (−ln α pour toute survivante), donc le signal visible du proposeur est binaire ; mais X1 déclare une **exposition adaptative** (30–31 verdicts montrés au proposeur sans tranches) et un nul informé par régression à crête que rien n'empêche de contourner par une interaction qu'il ne modélise pas. |
| 5 | « Fiche promue » ≈ « découverte » | HYPOTHÈSE | D4 : sans mémoire, 11 redites comptées comme découvertes ; K : le nul aveugle « promeut le connu, pas le trou » ; X2 : les 8/8 promues du monde planté sont des **témoins**, pas des idées. |
| 6 | Les systèmes publiés peuvent tourner sans clés ni réseau | HYPOTHÈSE | S : Agentic Scientist v3 écarté pour héritage de clés ; D/K : notre propre bac à sable réel « jamais exécuté dans ce dépôt », relais de clé réel absent. On n'a pas encore prouvé la prison pour nos agents. |
| 7 | La traduction idée-texte → loi prédictive conserve l'idée | HYPOTHÈSE | Aucun instrument de fidélité n'existe ; K : « toute hypothèse du programme doit être réécrite en loi par instance, ce qui change son contenu ». |
| 8 | « Même budget » rend les bras comparables | HYPOTHÈSE | K : le coût du monde (les issues) n'est pas budgété ; `Budget` ne compte que les dollars déclarés par le kit. Un proposeur qui demande des fiches à 340 issues et un autre à 120 ne consomment pas la même épreuve. |
| 9 | Développement visible / épreuve cachée suffit contre le sur-réglage de la phase exploratoire | HYPOTHÈSE | X1 : épisodes d'une même tâche **dépendants**, deux traits redondants, tranches qui réduisent les plans ; si développement et épreuve partagent des tâches, l'« épreuve jamais vue » ne l'est pas. |
| 10 | Les deux prises (proposeur, exploration) épuisent ce que ces systèmes apportent | HYPOTHÈSE | Ils apportent aussi une *lecture de littérature* (Agent Laboratory, RAPPORTÉ par la question) : c'est une troisième prise, « lecteur », que la question 3 mentionne pour notre côté et pas pour le leur. |
| 11 | La décision est « quel proposeur » | HYPOTHÈSE | X2 montre que le goulot est la **banque** (dents), pas la source d'idées. Décider du proposeur avant d'avoir un juge qui mord sur du réel, c'est choisir le semeur avant d'avoir un champ. |

---

## (b) Expériences décisives (inférence forte, B4)

Ordre imposé : 1 → 6 → 2 → 4 → 3 → 5. Les expériences 1 et 6 sont des préalables ; si l'une tombe du côté B, le duel de proposeurs (3) est inlisible.

### Exp. 1 — Pourquoi le juge n'a pas de dents sur T0.5 ?

- **H_A** : la puissance manque par **taille de banque** : à nul fixé, la part de témoins vrais promus croît avec le nombre d'épisodes d'épreuve N.
- **H_B** : la puissance manque parce que le **nul informé** explique déjà les témoins (ils sont déclarés sur la partie de calibrage, X1) : la part reste près de 0 quand N croît, et ne remonte qu'en retirant le nul informé (`--sans-nul-informe`).
- **Métrique** : taux de témoins vrais promus, par croisement {N ∈ {60, 120, 240, 480} épisodes d'épreuve par moniteur} × {nul informé : oui/non} × {urne : non}. Banque : couche 1 bis si elle existe, sinon un monde planté dont la loi est *hors* des membres du nul (X2, suite 1).
- **Seuil** (illustratif) : H_A tenue si la part passe de < 0,2 à ≥ 0,8 entre N = 60 et N = 480 avec nul informé ; H_B tenue si la part reste < 0,3 à N = 480 avec nul informé et ≥ 0,8 sans.
- **Contrôle négatif** : témoins faux ≤ α à chaque croisement (E1 : 0–1 sur 1 000 en simulation) ; permutation des issues entre instances → 0 promu.
- **Issues** : H_A réfutée ⇒ la banque n'est pas le levier ; c'est le nul qui mange les témoins et le « connu » est mal défini (il faut des témoins établis ailleurs que sur le calibrage). H_B réfutée ⇒ on sait quelle taille de banque acheter avant tout proposeur. Les deux tenues (ni l'une ni l'autre) ⇒ le juge ne transpose pas au domaine tel quel, ce qui rejoint K.

### Exp. 6 — La prison tient-elle pour un moteur tiers ?

- **H_A** : un système à boucle complète (AI Scientist v2 ou Agent Laboratory, candidats « exploration » RAPPORTÉ par la question) exécute une course de développement dans un conteneur sans clé, avec réseau coupé sauf le relais 127.0.0.1 (D § 2), et termine.
- **H_B** : il échoue ou tente une sortie (appel direct d'une interface externe, lecture de variables d'environnement, écriture hors dossier).
- **Métrique** : nombre de tentatives bloquées dans le journal du relais et du bac à sable ; nombre de fiches rendues.
- **Contrôle négatif** : notre faux moteur de répétition générale (D § 2.3), qui doit donner 0 tentative ; contrôle positif : un script qui tente volontairement une sortie, qui doit être attrapé.
- **Issues** : H_A réfutée ⇒ le système ne va pas à la prise « exploration » ; au mieux à la prise « proposeur » avec texte seul. H_B réfutée ⇒ la réserve de S sur les clés tombe pour ce candidat. Coût : zéro appel de modèle si l'on fait tourner le moteur avec un modèle factice ; sinon, voir (d).

### Exp. 2 — Un proposeur-agent bat-il un catalogue mécanique ?

Avant de comparer maison et littérature, il faut savoir si un *modèle* ajoute quelque chose au catalogue de huit stratégies déjà codé (X1).

- **H_A** : à exposition d'épreuve égale (même nombre d'instances consommées), un proposeur Opus 5.5 servi par le contexte public de v7 promeut plus de fiches **non expliquées par le connu** (`expliquees_par_le_connu` = faux) **et non redites** que le catalogue mécanique.
- **H_B** : l'écart est nul au bruit près : le catalogue couvre déjà ce que le modèle propose.
- **Métrique** : fiches promues-neuves pour 100 fiches gelées, et pour 10 000 instances d'épreuve consommées ; 20 graines par bras.
- **Seuil** (illustratif) : écart ≥ 2 promues-neuves pour 100 gelées sur la médiane des 20 graines, intervalle bootstrap ne contenant pas 0.
- **Contrôle négatif** : un monde planté *dans* un gabarit du catalogue (X2, où l'aveugle gagne par chance) et un monde planté *hors* catalogue (interaction à seuils non nuls, X2 suite 1). Si l'agent ne gagne que hors catalogue, l'apport est réel ; s'il gagne aussi dedans, soupçon de fuite (l'agent a vu les verdicts : vérifier les tranches).
- **Issues** : H_A réfutée ⇒ le débat « proposeur maison contre littérature » perd son objet : le concurrent à battre est gratuit. H_B réfutée ⇒ on tient une ligne de base chiffrée pour l'exp. 3.

### Exp. 4 — La fiche traduite est-elle encore l'idée ?

- **H_A** : la traduction (par gabarit mécanique, ou par un agent traducteur) est **réversible** : un lecteur aveugle d'une autre lignée, qui ne voit que la fiche (loi, espace d'instances, contraintes), rédige une phrase ; un troisième lecteur apparie cette phrase à l'idée d'origine parmi k = 8 idées de même génération.
- **H_B** : l'appariement est au hasard (1/8).
- **Métrique** : taux d'appariement correct ; en parallèle, un contrôle mécanique à battre : cohérence de signe entre la prédiction écrite (`prediction.signe`) et le sens de la loi sur la sonde de la mémoire (256 instances), calculable sans modèle.
- **Seuil** (illustratif) : H_A tenue si ≥ 0,75 sur 80 idées ; H_B tenue si ≤ 0,25.
- **Contrôle négatif** : paires mélangées (idée d'une fiche, fiche d'une autre) → au hasard ; contrôle positif : idée et fiche écrites par le même agent dans le même tour.
- **Issues** : H_A réfutée ⇒ la « prise proposeur » transmet du bruit : ce qu'on jugera n'est pas ce qu'ils proposent, et « fiches promues » ne mesure rien d'eux. H_B réfutée ⇒ la traduction par gabarit est admissible et doit être **la même** des deux côtés du duel.

### Exp. 3 — Le duel maison / littérature sous le même juge

- **H_A** : le proposeur de la littérature (prise proposeur, ou exploration s'il a passé l'exp. 6) produit plus de fiches promues-neuves par unité d'exposition que le proposeur maison (celui de l'exp. 2).
- **H_B** : le maison fait au moins aussi bien.
- **Nul commun** (celui demandé par la question, précisé) : idées tirées au hasard de la mémoire du pôle, paraphrasées par la même consigne, traduites par le même gabarit ; plus un **faux proposeur** qui permute les traits des fiches maison (même forme, contenu détruit).
- **Plan** : même banque de développement, mêmes tranches d'épreuve, même nombre de fiches gelées par génération (12, X1), 4 générations, 10 courses par bras ; vérification, juge, mémoire, nul d'archive identiques ; le relecteur du système tiers débranché.
- **Métrique** (voir question 4) : promues-neuves pour 100 gelées ; en second rang, pour 10 000 instances d'épreuve ; en troisième rang seulement, par dollar, le coût de la traduction et du monde comptés dans les deux bras.
- **Seuil** (illustratif) : différence de médianes ≥ 2 pour 100 gelées, bootstrap sur 10 courses ; en deçà : « n'apporte rien » dans le sens testé.
- **Issues** : trois sorties, toutes informatives : littérature > maison ⇒ la prise est justifiée ; maison ≥ littérature ⇒ pas d'achat ; **les deux ≤ nul** ⇒ ni l'un ni l'autre ne dépasse la mémoire ré-échantillonnée, et le goulot est ailleurs (banque, nul) : retour à l'exp. 1.

### Exp. 5 — Enfermement du proposeur

- **H_A** : exposé aux verdicts (sans tranches, X1), le proposeur dérive vers des fiches à domaine étroit, à faible divergence déclarée, ou jumelles (refusées par la mémoire), et ce de façon croissante sur 6 générations.
- **H_B** : aucune dérive mesurable ; les tranches ne changent rien.
- **Métrique** : par génération, (i) divergence moyenne déclarée à la référence (S : contenu = risque × couverture) ; (ii) part de fiches refusées comme redites ; (iii) couverture de l'espace d'instances (part de sous-populations touchées). Bras : avec tranches / sans tranches.
- **Seuil** (illustratif) : pente de (i) significativement négative sur 6 générations (20 graines) dans le bras sans tranches et non dans le bras avec.
- **Contrôle négatif** : le catalogue mécanique, sans mémoire d'une génération à l'autre, qui ne peut pas dériver.
- **Issues** : H_A réfutée ⇒ les tranches sont un coût sans objet ; H_B réfutée ⇒ l'exposition adaptative est une faille réelle et toute mesure du proposeur doit se faire sous tranches.

---

## (c) Instruments nommés : la mesure minimale

Pour chaque instrument, trois choses : le taux de détection, le taux de fausses alertes, et le contrôle mécanique qu'il doit battre pour justifier son coût. Les chiffres de simulation sont RAPPORTÉ (E1, E2, D4, X2) ; ceux sur banque réelle n'existent pas.

**Juge à mise (nul composite, seuil 1/α).** Détection : témoins vrais promus (simulation : 0,958 à ε = 0,2, 0,196 à ε = 0,05, E1 ; banque réelle : 0/20, X2). Fausses alertes : témoins faux promus (0–1 sur 1 000, E1 ; 0/48, X2). Cas honnêtes appariés : une fiche vraie et sa jumelle fausse (même forme, traits permutés). Mécanique à battre : un test de permutation sur la partie d'épreuve, sans e-processus ; si le juge ne promeut pas plus que la permutation à α égal, l'urne et l'ordre secret coûtent (5,5 nats, K) pour rien sur une banque figée.

**Ordre d'exécution secret.** Détection : l'oracle « calendrier » promu 0 fois sous v1 contre 0,670 sous v0 (E1). Fausses alertes : sans objet. Mais sur banque figée il n'y a pas de temps (K) : la mesure minimale est l'exp. 1 avec/sans urne ; si les deux colonnes sont égales, retirer l'urne (X1 le permet).

**Nul des filles v2.** Détection : fille neuve 0,988 ; fausses alertes : 13 fatals à 0 (E2). À mesurer encore : une fille « ou exclusif » passe (0,963, E2) et personne ne sait si c'est une découverte ; cas honnêtes appariés = fille neuve contre « ou exclusif » des parents, lus par un humain. Mécanique à battre : le produit des parents au nul (option stricte) contre le nul v1 : écart de 10 points de puissance en monde pauvre (M, non vérifié).

**Mémoire à empreinte prédictive.** Détection de redites : 11 doubles évités (D4) ; fausses fusions : 31–39 vraies filles refusées à deux traits, 5–6 à quatre (D4), corrigé par le seuil par fiche (D4b, non ré-éprouvé sur agents). Cas honnêtes appariés : deux idées *différentes* à même loi (K : signature sur la loi, pas sur la recette). Mécanique à battre : Jaccard 3-grammes à 0,5 (K) ; si la signature ne fait pas mieux que le texte, elle ne vaut pas son calcul.

**Vérificateur d'un autre modèle.** Aucune mesure dans les faits : simulation sans persuasion (K). Mesure minimale : tricheurs scriptés *et* tricheurs textuels (note de persuasion dans le dossier de rejeu, canal signalé par K), détection ≥ 0,9, fausses alertes ≤ 0,05 sur des expérimentateurs honnêtes appariés (même fiche, même code, sans note). Mécanique à battre : rejeu bit à bit + empreinte d'ordre, qui n'a pas besoin de modèle ; le vérificateur ne se justifie que par ce qu'il attrape en plus.

**Relecteur modèle des systèmes tiers (celui qu'on retire).** Puisqu'on le retire, le mesurer est gratuit : faire noter par ce relecteur les mêmes fiches que notre juge. Détection : accord avec les promues du juge ; fausses alertes : fiches qu'il classe haut et que le juge élimine. Si l'accord est au hasard, la position de conv-audit (« ne pas prendre leur relecteur ») est corroborée ; s'il est élevé, il devient un *pré-filtre* bon marché avant l'épreuve, et la position est trop tranchée.

**Tournoi d'idées (co-scientist, Robin : RAPPORTÉ par la question).** Même mesure : rang de tournoi contre verdict du juge sur les fiches gelées ; corrélation de rang ≥ 0,3 (illustratif) justifie de l'utiliser comme ordre de passage ; en deçà, non.

**Traduction.** Exp. 4 ; mécanique à battre : cohérence de signe sans modèle.

**Bac à sable et relais.** Exp. 6 ; détection = tentatives bloquées sur un script d'attaque connu (100 %), fausses alertes = blocages d'un agent honnête (0).

---

## (d) Ancrage matériel

**Candidats et prises** (tout vient de la section « Correction » de la question, RAPPORTÉ, non audité sur PDF ; je n'ajoute aucune source de mémoire) :

| candidat | prise possible | entrée / sortie de l'étage | licence | ce que je sais |
|---|---|---|---|---|
| AI Scientist v2 (Sakana, arXiv 2504.08066 selon la question) | exploration + proposeur | idée + gabarit de code → arbre d'expériences exécutées, figures, manuscrit | « code ouvert, licence à vérifier » (question) | les humains ont choisi les idées et le manuscrit (RAPPORTÉ) : la *proposition* n'est donc pas ce qui a été évalué ; sans relecteur, l'arbre garde sa métrique de développement comme seul signal de sélection (HYPOTHÈSE) |
| Agent Laboratory (arXiv 2501.04227 selon la question) | exploration + proposeur + lecteur | sujet → revue de littérature, code, rapport | à vérifier | la revue de littérature est une entrée de proposition que notre organisme n'a pas (HYPOTHÈSE) |
| Co-scientist (Google) | proposeur seulement | objectif → hypothèses classées par tournoi | code non mentionné : à vérifier | expériences humaines (RAPPORTÉ) ; sans code, pas de prise possible sans clé (HYPOTHÈSE) |
| Robin (FutureHouse, arXiv 2505.13400 selon la question) | proposeur ; Finch (analyse de données) peut-être exploration | question → hypothèses classées | à vérifier | expériences de paillasse humaines (RAPPORTÉ) |
| Kosmos, Edison, CodeScientist, Zochi, AI-Researcher, AI Scientist v1 | — | — | référence à vérifier | aucun fait servi ; je ne les classe pas |

Ce qu'un système à boucle complète perd quand on retire son relecteur et qu'on gèle avant l'épreuve : (i) son signal de sélection interne, remplacé par la métrique de développement, ce qui change la pression vers le sur-réglage (exp. 5 le mesure) ; (ii) sa rédaction, sans valeur pour nous ; (iii) la possibilité de réviser l'hypothèse après avoir vu l'épreuve, et c'est exactement ce qu'on veut lui retirer. Tout cela est HYPOTHÈSE.

**Modèles ouverts.** Les faits ne nomment qu'un modèle ouvert : Qwen2.5-7B comme juge d'une autre lignée (N-053) et « le modèle de 8 milliards » du harnais (K). Un proposeur ouvert pour le bras tiers n'est nommé nulle part ; si les candidats de la littérature exigent un modèle propriétaire, le bras « sans clé » revient à les faire tourner sur un modèle ouvert local, ce qui change ce qu'on mesure (HYPOTHÈSE à déclarer dans le plan).

**Calcul.** Le juge est sur processeur : 70 lignes × 1 000 répétitions en 14 min sur un cœur (E1) ; 0,11 s par évaluation de fille (E2) ; démonstration proposeur en 94 s (X2). Exp. 1, 2 (bras mécanique), 5 (bras mécanique) et 6 (modèle factice) : zéro dépense, quelques heures de cœur. Exp. 4 : 80 idées × 3 lectures.

**Coûts** (tout illustratif sauf mention) :

- Repères des faits : 7,82 USD pour neuf cellules de collisionneur (S) ; plafond 17,80 USD pour deux générations réelles (D) ; 10 + 60 + 60 USD de devis pour un bras tiers (M, non vérifié).
- Exp. 2, bras agent : 12 fiches × 4 générations × 20 graines = 960 propositions ; à 0,30 USD par appel (plafond de recombinaison de D, repris comme ordre de grandeur) ≈ 290 USD. Réduire à 10 graines : ≈ 145 USD.
- Exp. 4 : 80 idées × 3 lectures × 0,20 USD ≈ 50 USD.
- Exp. 3 : 3 bras × 10 courses × 48 fiches × 0,30 USD ≈ 430 USD, plus le coût du monde, nul sur banque en cache, et le coût propre du système tiers (inconnu, à mesurer en exp. 6).
- Exp. 5 : couvert par les courses de l'exp. 2 si l'on journalise les métriques (i)–(iii).

Total illustratif pour l'ordre 1 → 6 → 2 → 4 → 3 → 5 : entre 500 et 800 USD, dont 0 avant la fin de l'exp. 1.

---

## Sur la question 4 (la métrique) et la question 5 (décider quand)

« Fiches promues par dollar » compte mal quatre choses : les redites (déjà bloquées par la mémoire, D4, mais seulement si la signature tient sur de vrais agents, D4b), le connu (nul d'archive et nul informé de v7 : non éprouvés sur agents), le coût du monde (K) et la fécondité des lignées (une fiche dont les filles survivent vaut plus qu'une promue stérile). La métrique que je propose : **promues-neuves pour 100 fiches gelées**, avec « neuve » = non redite et non expliquée par le connu, en premier rang ; **par 10 000 instances d'épreuve consommées** en second ; dollars en troisième, toutes charges comprises ; et, en descriptif, la **profondeur de lignée** (nombre de descendantes promues sous preuve héritée) à génération 4.

Décider maintenant est prématuré : le juge n'a pas mordu sur du réel (X2), la prison n'a pas été exercée (K, D), le proposeur maison n'existe pas comme agent (X1). Décider *après* l'option (a) de D ne suffit pas non plus : (a) éprouve la plomberie, pas les dents. La décision devrait attendre l'exp. 1 (dents sur banque) et l'exp. 6 (prison pour un tiers), toutes deux sans dépense.

Ce qui me ferait changer d'avis : si l'exp. 2 montre que le catalogue mécanique égale un proposeur Opus, j'abandonnerais toute prise « proposeur », maison ou tierce, et je mettrais le budget sur la banque. Si l'exp. 3 donne « les deux ≤ nul », je dirais que la question posée (quel proposeur) était la mauvaise et que la position de conv-audit, bien que non réfutée, est sans objet. Si le relecteur tiers, mesuré gratuitement, s'accorde avec le juge au-delà de 0,3 de corrélation de rang, je retirerais le mot « insensé » de la position : il y aurait un pré-filtre à prendre.

FIN-DE-CELLULE