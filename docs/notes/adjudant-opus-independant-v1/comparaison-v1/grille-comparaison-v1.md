# Grille de comparaison des deux réponses sur le mécanisme adjudant aux moniteurs pour le hors distribution — v1

- Auteur : comparateur neuf, Claude Opus 5.5 ; ni auteur de l'une ou l'autre réponse, ni de la contre-lecture de la réponse de Fable.
- Cadre : GO-2026-11-21-56, décision D-7. Pièce de travail (classe C).
- Date : 2026-11-21. Statut : écrite et scellée **avant** toute lecture des deux réponses, de la contre-lecture et des pièces qui les entourent.
- Objets comparés :
  - la réponse de Fable 5.2, dite « réponse A » : `docs/notes/mecanisme-adjudant-hors-distribution-v1/reponse-fable-mecanisme-adjudant-v1.md` (empreinte annoncée 896cec0e…) ;
  - la réponse d'Opus écrite sans voir A, dite « réponse B » : `docs/notes/adjudant-opus-independant-v1/reponse-opus-mecanisme-adjudant-v1.md` (empreinte annoncée 998bd5d9…) ;
  - la contre-lecture de A : `docs/notes/mecanisme-adjudant-hors-distribution-v1/contre-lecture-opus-mecanisme-adjudant-v1.md` (empreinte annoncée 2167a5ae…).

## 0. Ce que j'ai lu avant de sceller cette grille

- `CLAUDE.md` (consignes permanentes) et `src/controle_ia/scellement.py` (outil de scellement).
- La seule ligne GO-2026-11-21-34 de `registres/go.md` : Lazar demande un Fable 5.2 en effort maximal sur la demande reformulée du mécanisme adjudant aux sondes pour le hors distribution, puis le collisionneur, puis un manuel clé en main pour lancer l'organisme d'idéation sur la question ; l'organisme part sur devis.
- Les seuls noms des fichiers des deux dossiers de réponses, sans leur contenu.

Rien d'autre : ni les réponses, ni la contre-lecture, ni les fichiers du collisionneur, ni les calculs, ni les dossiers de sources des deux réponses, ni les autres lignes des registres qui les citent.

## 1. Conflit d'intérêts déclaré et contrepoids fixés d'avance

- Je suis du même modèle que l'auteur de la réponse B et que le contre-lecteur de la réponse A (Opus). Biais attendu : une préférence pour les choix et le style d'un texte de mon propre modèle.
- Contrepoids :
  1. mêmes procédures de vérification, même règle d'échantillonnage et même effort pour A et pour B (règle de symétrie, R4) ;
  2. quand une note hésite vraiment entre deux valeurs voisines, la valeur basse va à B et la valeur haute à A ; chaque usage de cette règle est signalé dans la comparaison ;
  3. les objections de la contre-lecture de A sont des pistes, pas des verdicts : chacune est vérifiée par moi avant d'entrer dans une note, et chacune est appliquée à B avec la même rigueur, puisque B n'a pas eu de contre-lecture (asymétrie à corriger, pas à exploiter).
- Ordre de lecture fixé : A, puis B, puis la contre-lecture de A, puis les pièces de vérification. Les notes sont données critère par critère, les deux réponses côte à côte.

## 2. Règles générales

- Échelle commune : entiers de 0 à 4 pour les huit critères. Chaque note porte la ligne ou le paragraphe cité qui la justifie (citation courte ou renvoi de section) et, si elle s'appuie sur une vérification, le chemin et l'empreinte de la pièce.
- On note le texte scellé tel qu'il est : les empreintes de A, de B et de la contre-lecture sont vérifiées par `sha256sum` avant lecture. Les objections de la contre-lecture ne changent la note de A que par les erreurs que je confirme ; elles sont rapportées à part.
- Les annexes qu'une réponse cite comme siennes (calculs, provenance de ses sources) font partie de cette réponse. Le reste du matériel produit autour d'elle (collisionneur, contre-lecture, recalculs du contre-lecteur) sert de source de vérification et n'est crédité à aucune des deux.
- Aucun total pondéré ne départage. La comparaison se lit critère par critère ; je donne aussi le nombre de critères où chaque réponse l'emporte d'au moins un point.
- Une note qui dépend d'une vérification non faite (pièce introuvable, temps) est marquée « provisoire » et dit ce qui manque.

## 3. Les huit critères

### 3.1 Justesse des affirmations sur pièce

Ce qui est noté : les affirmations vérifiables sont-elles vraies sur la pièce ?

- Affirmation vérifiable : (a) un contenu ou un chiffre attribué à une publication nommée ; (b) un fait sur le dépôt (fichier, décision, règle, nombre, empreinte, état d'un chantier) ; (c) un résultat de calcul.
- Échantillon fixé d'avance : je relève dans l'ordre du texte toutes les affirmations vérifiables. Si elles sont 12 ou moins, toutes sont vérifiées. Sinon : toutes les affirmations porteuses (celles sur lesquelles une recommandation de la réponse s'appuie explicitement), au plus 6, puis un tirage systématique parmi les autres (pas k égal à la partie entière supérieure de « reste divisé par 6 », en partant de la première) jusqu'à 12. S'y ajoutent les affirmations contrôlées aux points de vérification sur PDF du § 4, signalées comme telles.
- Verdict par affirmation : juste (1) ; approchée, le fond juste et un détail faux (0,5) ; fausse (0) ; non vérifiable, pièce introuvable (hors du dénominateur, comptée et rapportée).
- Note : p = somme des verdicts divisée par le nombre d'affirmations vérifiées. 4 si p ≥ 0,95 ; 3 si p ≥ 0,85 ; 2 si p ≥ 0,70 ; 1 si p ≥ 0,50 ; 0 sinon. Plafond à 2 si une affirmation fausse est porteuse. « Provisoire » si plus de la moitié de l'échantillon est non vérifiable.

### 3.2 Profondeur de la reformulation

Ce qui est noté : jusqu'où la réponse transforme la demande en problème bien posé. Niveaux cumulatifs ; la note est le plus haut niveau dont toutes les conditions sont remplies.

- 0 : la demande est reprise telle quelle.
- 1 : les termes sont précisés : ce qu'est le hors distribution et par rapport à quelle distribution de référence ; ce qu'est l'adjudant, ce qu'il lit, ce qu'il décide.
- 2 : formulation opérationnelle : entrées, sortie et règle de décision de l'adjudant ; modèle de menace qui distingue le hors distribution naturel du hors distribution provoqué par un attaquant ; mesure du succès.
- 3 : en plus, au moins une hypothèse cachée ou un point mal posé de la demande est nommé et traité (par exemple : l'absence d'étiquettes de vérité pour le hors distribution ; un attaquant qui reste dans la distribution ; un adjudant qui devient lui-même une cible).
- 4 : en plus, le problème est ramené à une question testable (prédiction, mesure et seuil qui la trancheraient), et la reformulation change ce qu'il faut construire par rapport à la demande de départ, avec la raison.

### 3.3 Part de mécanismes qui tiennent face à un attaquant informé

Ce qui est noté : la part des mécanismes proposés qui résistent à un attaquant qui connaît le dispositif.

- Attaquant informé : il connaît l'architecture, les familles de moniteurs, la règle de l'adjudant et l'ordre de grandeur de ses seuils (principe de Kerckhoffs) ; il ne connaît ni les graines secrètes, ni l'identité de la famille tenue à l'écart, ni les données scellées ; il choisit ses sorties et ses traces. Je dis à part si le mécanisme tient aussi contre un attaquant entraîné contre lui (adaptation de ses activations).
- Unité : un mécanisme est une règle de décision ou un signal distinct de l'adjudant ; deux variantes qui ne diffèrent que d'un réglage comptent pour un.
- Classes, attribuées par moi, avec une phrase d'argument par mécanisme :
  - tient (T) : la meilleure réponse de l'attaquant informé ne fait pas tomber la détection sous celle du dispositif sans ce mécanisme, ou l'oblige à renoncer à une partie du sabotage ;
  - tient sous condition (C) : tient si une condition nommée tient (secret, famille tenue à l'écart, absence de collusion, budget de l'attaquant), et cette condition est plausible dans le programme ;
  - ne tient pas (N) : l'attaquant informé l'évite à faible coût (par exemple : rester dans la distribution, faire concorder tous les moniteurs, viser l'adjudant lui-même) ;
  - indéterminé (I) : mécanisme trop peu spécifié pour juger.
- Note : s = (T + 0,5 × C) / (T + C + N + I). 4 si s ≥ 0,75 ; 3 si s ≥ 0,55 ; 2 si s ≥ 0,35 ; 1 si s ≥ 0,15 ; 0 sinon. Les quatre décomptes sont rapportés. Je rapporte aussi, sans le noter ici, si la réponse fait elle-même cette analyse et si ses classes concordent avec les miennes.

### 3.4 Antériorité honnête

Ce qui est noté : la réponse dit-elle ce qui existe déjà, sans s'attribuer ce qui est publié ni inventer de trou ?

- Départ à 4, puis retraits :
  - −1 par revendication de nouveauté (« nouveau », « personne n'a », « zone vierge », « propre ») sur un mécanisme dont je trouve un voisin publié proche que la réponse ne nomme pas (au plus −3) ;
  - −1 par citation mal attribuée (auteurs, année, contenu) établie sur PDF (au plus −2) ;
  - −1 si plus d'un tiers des mécanismes n'ont ni voisin nommé ni mention « antériorité à vérifier » ;
  - −1 si un chiffre de l'état de l'art est donné sans pièce empreintée ni page (R7), sauf s'il est marqué non vérifié.
- Plancher 0. Une limitation d'un papier présentée comme un trou du champ (R8) compte comme une revendication de nouveauté non fondée.

### 3.5 Utilité pour le programme

Cinq éléments, chacun 0 ou 1 :

- (a) la réponse traite la question posée (un adjudant aux moniteurs pour le hors distribution) et non une question voisine ;
- (b) chaque mécanisme recommandé est rattaché correctement à un élément existant du programme (hypothèse, porte G0 de sortie de la phase des instruments ou porte G1, base de comparaison, mode de sabotage, mode tenu à l'écart, chantier actif) ;
- (c) un premier pas faisable dans les chantiers actifs avant la porte G0 (fin décembre 2026) ou avant l'entretien du 1er décembre, sans rouvrir un chantier gelé ;
- (d) les invariants du programme sont respectés : aucun score de moniteur dans l'entraînement de l'agent ; G1 rapportée par mode, mode tenu à l'écart compris ; composition jugée sur l'oracle du monde planté et le coût, jamais sur le verdict du juge (N-058) ; ni moyenne ni médiane sur les jetons dans une sonde de production ;
- (e) la réponse dit quel résultat changerait quelle décision du programme.

Note : somme 5 → 4 ; 4 → 3 ; 3 → 2 ; 2 → 1 ; 0 ou 1 → 0. Plafond à 2 si la réponse recommande, et non seulement discute, une action qui viole un invariant.

### 3.6 Coût

Quatre éléments, chacun 0 ou 1 :

- (a) chiffré : chaque pas recommandé porte un coût en argent ou en calcul, et un délai ;
- (b) fondé : les chiffres ont une base traçable (tarif, nombre de jetons, heures de machine, pièce du dépôt) ;
- (c) échelonné : le premier pas recommandé est le moins cher qui puisse changer une décision (voies bon marché avant la voie chère, N-045), avec un point d'arrêt avant la dépense suivante ;
- (d) conforme à la hiérarchie de décision : toute dépense est renvoyée à un devis et à un GO ; aucune n'est engagée par la réponse elle-même.

Note = somme (0 à 4). Je rapporte en plus le coût annoncé du chemin recommandé jusqu'à la première lecture décisive, corrigé s'il est faux ; ce chiffre ne change pas la note.

### 3.7 Manuel de course utilisable

Ce qui est noté : le manuel clé en main pour lancer l'organisme d'idéation sur la question (demande GO-2026-11-21-34). Neuf éléments, chacun présent et utilisable sans demander à l'auteur (0 ou 1) :

1. le texte exact de la question donnée à l'organisme, ou le fichier qui la porte ;
2. la configuration : rôles, modèle par rôle (sans changement de modèle non autorisé), budget par génération, nombre de générations ;
3. les commandes ou programmes à lancer, existants dans le dépôt (vérifié sur disque), et les variables d'environnement ;
4. les gardes d'arrêt (plafond de coût, de durée) et leur essai sur un cas sain et sur un artefact (R5) ;
5. ce qui est scellé avant le lancement, le manifeste et les graines (R1, R9) ;
6. comment les sorties sont jugées : sur un oracle ou un monde planté, jamais sur le seul verdict d'un juge (N-058), et le critère de lecture ;
7. le cloisonnement : ce que l'organisme ne doit pas voir ;
8. la fin de course : inventaire et versement des sorties, arrêt des machines par identifiant (R10) ;
9. le coût et le GO ou le devis qui l'autorisent.

Note : 9 → 4 ; 7 ou 8 → 3 ; 5 ou 6 → 2 ; 3 ou 4 → 1 ; 0 à 2 → 0. Plafond à 2 si un agent neuf ne peut pas dire les trois premières actions sans deviner. Un programme cité qui n'existe pas dans le dépôt et n'est pas annoncé comme à écrire compte comme absent. Si une réponse n'a pas été chargée d'écrire ce manuel, je le dis, et la note est donnée quand même, marquée ainsi.

### 3.8 Décisions bien posées

Ce qui est noté : les décisions que la réponse soumet à Lazar.

- Pour chaque décision : la forme, soit les cinq éléments du format de `CLAUDE.md` (décision en une phrase ; enjeu ; deux ou trois options avec avantage et inconvénient ; recommandation et confiance ; défaut sous 48 heures), donne une part f de 0 à 1 ; la classe juste (nœud, proposition avec recommandation, routine, selon la hiérarchie de `CLAUDE.md`) vaut 0 ou 1.
- Note brute = 2 × (moyenne des f) + 2 × (part des décisions de classe juste), arrondie à l'entier inférieur.
- Retraits : −1 par action recommandée qui exige un GO (dépense, changement de modèle, d'hypothèse ou de revendication, contact, publication, écart à un préenregistrement scellé) sans être posée en décision (au plus −2) ; −1 si la réponse tranche elle-même un nœud qui revient à Lazar. Plancher 0.
- Aucune décision posée alors que la réponse en appelle au moins une : 0. Aucune décision nécessaire : « sans objet ».

## 4. Vérification sur PDF (au moins cinq points)

- Sélection fixée d'avance : d'abord les contradictions entre A et B sur un fait, une citation ou un chiffre, les porteuses d'abord ; puis les recoupements où les deux réponses s'appuient sur la même publication pour un contenu précis. Au moins cinq points, au plus huit.
- Pièce : le PDF empreinté du dépôt (dossiers de sources) ; à défaut, le PDF public et gratuit de la publication, empreinté par moi, avec chemin, adresse et empreinte cités ; à défaut, « non vérifiable » et je passe au point suivant de la liste.
- Pour chaque point : publication, page, extrait court, verdict pour A et pour B (juste, approché, faux, non abordé).

## 5. Convergences, divergences, apports propres

- Convergence : un mécanisme présent dans A et dans B au sens de l'unité du § 3.3. Elle compte comme trouvée indépendamment seulement si B atteste ne pas avoir vu A ni une pièce tirée de A (question ou faits du collisionneur, calculs, registres qui résument A) ; sinon, « convergence non indépendante ».
- Poids : les deux auteurs sont de la même famille de modèles ; une convergence dit qu'un mécanisme est naturel, pas qu'il est juste. Elle sert de deuxième clé de rang (§ 6), jamais de preuve.
- Divergence : la même question traitée avec des conclusions incompatibles. Chaque divergence est tranchée sur pièce si possible, sinon laissée ouverte avec ce qui la trancherait.
- Apports propres : ce que l'une a et que l'autre n'a pas, mécanismes et non-mécanismes (reformulation, calculs, manuel, décisions).

## 6. Liste fusionnée et rangée des mécanismes

- Fusion selon l'unité du § 3.3 ; chaque mécanisme porte sa ou ses réponses sources (A, B, ou A et B).
- Rang par clés successives : (1) classe face à l'attaquant informé (T, puis C, puis I, puis N) ; (2) convergence indépendante (trouvé par les deux avant trouvé par une seule) ; (3) utilité pour le programme, éléments (a) à (c) du § 3.5 appliqués au mécanisme (0 à 3) ; (4) coût annoncé ou estimé, le moins cher d'abord. Égalité restante : même rang.

## 7. Corrections de la contre-lecture de A appliquées à B

- Chaque objection de la contre-lecture est d'abord vérifiée par moi sur la pièce : confirmée, partiellement confirmée, infirmée.
- Chaque objection confirmée ou partiellement confirmée est cherchée dans B : même erreur, erreur voisine, absente. Seules les deux premières sont des corrections imposées à B.
