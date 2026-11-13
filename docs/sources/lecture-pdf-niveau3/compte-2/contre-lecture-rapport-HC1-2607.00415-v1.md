# Contre-lecture du rapport HC1 — pièce 2607.00415 v1 — v1

- **Date et heures** (relevées par `date -u`, dans la commande qui écrit cette ligne) : dossier de l'archive du lecteur extrait le 2026-11-13 23:02:44 UTC (début du travail) ; contrôle des citations terminé le 2026-11-13 23:07:59 UTC ; rédaction terminée le 2026-11-13 23:11:08 UTC ; l'heure de scellement est donnée par la commande de scellement.
- **Rôle et modèle** : contre-lecteur, modèle B. L'auteur du rapport contre-lu est le modèle A ; A ≠ B. Je n'ai écrit ni le programme, ni les décisions, ni le rapport.
- **Objet** : `docs/sources/lecture-pdf-niveau3/compte-2/rapport-HC1-2607.00415-v1.md`, empreinte vérifiée `67192c4a2bfb53786a52dfd9f4fdae6278a53babb63d51bc8116c69f31a67cd3` (conforme) ; son archive `fichiers-de-travail-HC1-2607.00415-v1.tar`, empreinte vérifiée `0978c80a5cbef34ceb5b7bc4fd820a870c77e92a304dbf13f6bea7f9a5d8acc6` (conforme), extraite dans mon dossier de travail.
- **Consigne commune** : `consigne-lecteur-compte-2-v1.md`, empreinte vérifiée `cb0623c4aff841a815dc628691f407308acbeeeceb274db96d1f2ba3c8c77ff5` (conforme), lue en entier (41 lignes).
- **Pièce** : `2607.00415v1.pdf`, 15 pages, empreinte calculée `dab3b21c3c3e62ac99854fa3a176b82d2d603ccf9244f1a81e03294516b17ec6`, identique au compagnon `.sha256`. Aucun autre PDF ouvert.
- **Fichiers lus** (seulement ceux-ci, aux lignes du mandat) : la consigne commune ; le rapport et son archive (journal, scripts, sorties, citations) ; `docs/programme-controle-ia-v2.md` l. 85-125 ; `docs/decisions/decision-N-005-N-006-v1.md` l. 22-75 ; `docs/decisions/decision-N-013-v1.md` l. 18-32 ; `docs/decisions/decision-N-023-v1.md` en entier ; `docs/decisions/decision-N-068-v1.md` l. 1-72 ; `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md` l. 329-360 ; `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md` l. 472-508. **Non lus, parce qu'absents de mon mandat** : `interdits-communs-v2.md` et `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md` l. 181-220, que le lecteur a lus ; les lignes 90 à 92 de N-013, connues seulement par la citation qu'en fait N-068 (l. 39).
- **Étendue lue du PDF** : pages 1 à 15 lues ligne à ligne sur le texte extrait (`pdftotext -layout`), bibliographie et annexes A.1 à A.5 comprises ; recherche par mots sur le texte complet pour les composantes dites non trouvées (juge, moniteur, agent, régression, intervalle, graine, contrôle neutre, attaque : section 2). Figures relues **en image à la résolution d'origine** (images extraites du PDF par `pdfimages`, composées sur fond blanc) : 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 18 (panneau du premier modèle) ; pages 2 à 4 vues aussi par l'outil Read. Figures 16, 17, 19 et second panneau de la figure 18 : **non relues** (les lectures du lecteur n'y sont pas vérifiées).
- **Citations contrôlées par programme** : 36 de moi, **0 échec** (`citations-contre-lecture-HC1-v1.json`, dans l'archive ; script écrit par moi, testé sur un cas juste, un cas altéré et une page fausse : 1 réussite, 2 échecs attendus obtenus). Les 57 citations du lecteur rejouées par mon script : **57 sur 57, 0 échec**.
- **Nature des chiffres** : « auteurs » (imprimé), « figure » (lu par moi sur une figure, non contrôlé par programme), « calcul » (`scripts/calculs_cl.py`, lancé par `python3 -I`, sortie `sortie-calculs-cl.txt`).
- **Noms de modèles** : aucun nom de modèle lecteur ou contre-lecteur. Les noms abrégés des trois modèles **étudiés par la pièce** figurent ici, comme dans le rapport, parce que les citations exactes et les constats par figure les exigent ; je le signale au regard de la consigne (constat N).
- **Incidents** : aucun refus, aucune ouverture fautive, aucune commande git, aucun appel réseau, aucun appel de modèle, aucune recherche récursive dans le dépôt.

---

## 0. Verdict en tête

- **Verdict sur le rapport : « tient avec corrections ».** La conclusion centrale tient. Trois corrections majeures portent sur la **portée** de ce que le rapport tire des figures, aucune sur le verdict d'antériorité.
- **Mon verdict sur HC1 (table fermée) : « occupé en partie »**, inchangé. La pièce revendiquée — destination libre contre la cible et contre la moyenne du corpus, par famille, dans un moniteur de contrôle, par régression sur plusieurs intensités ; opposition juge contre sonde où la sonde lit l'agent auteur — est **non trouvée dans les pièces lues**, 2607.00415 comprise. La porte GC n'est pas déclenchée par cette pièce.
- **Point 1 du mandat, tranché** : N-005 revendique une sonde qui lit **l'agent qui produit le contenu** ; les lignes lues de N-013 ne parlent d'aucune sonde pour HC1 ; N-068 confirme et resserre (« agent auteur du contenu adverse », « et non victime d'une injection écrite par un tiers »). Aucune de ces trois décisions ne revendique une sonde du lecteur. L'occupation n'est **pas sous-estimée** par le rapport sur ce point.
- **Ce qui ne tient pas tel quel** : (A) l'écart « lecture interne lisible alors que la sortie a cédé » chez le deuxième modèle aux autorités faibles — la figure 12 montre que la sortie elle-même n'a pas cédé en moyenne sur ces sous-ensembles ; (B) la phrase « l'avantage d'une sonde du lecteur décroît avec l'intensité » et le mot « sérieux » ; (C) le « contre-indice faible sur la forme dose-réponse » et le mot « renforcés » ; (D) « le constat M7 se referme ».
- **Ce que le lecteur a manqué et qui compte pour le papier C** : (E) au niveau d'autorité le plus bas, les bascules ne vont **pas vers la lettre indiquée** (figures 10 et 12) et l'exactitude sur toutes les questions ne baisse presque pas, voire monte : sans indice témoin neutre, le niveau bas ne se distingue pas d'une simple perturbation de la consigne.

## 1. Constats

### A — majeur — L'écart « sonde lisible, sortie cédée » chez Llama n'est pas établi : la sortie n'a pas cédé en moyenne (figure 12)

- **Texte du rapport** (§ 3.2, repris en § 0 et § 5) : « Llama (figure 14, p. 12) : basculées sous chef résident ≈ 0,6-0,7, sous 3e année ≈ 0,6-0,65, sous 1re année ≈ 0,8-0,85 […] — la réponse correcte **reste lisible** alors que la sortie a cédé ».
- **Les valeurs lues sur la figure 14 sont justes** (figure, relue à la résolution d'origine) : sondes avec indice ≈ 0,57-0,70 (chef résident, n = 744), ≈ 0,57-0,65 (3e année, n = 738), ≈ 0,78-0,86 (1re année, n = 270) ; médecin ≈ 0,05-0,08.
- **Mais la figure 12 (p. 10), mêmes sous-ensembles et mêmes effectifs**, trace la sortie elle-même par la lentille des logits (figure) : sur les questions dites basculées, la probabilité moyenne de la lettre correcte **reste au-dessus** de celle de la lettre indiquée aux trois niveaux faibles — chef résident ≈ 0,47 à 0,61 contre ≈ 0,25 à 0,30 ; 3e année ≈ 0,44 à 0,60 contre ≈ 0,28 à 0,36 ; 1re année ≈ 0,55 à 0,75 contre ≈ 0,05 à 0,11 (couches 17 à 31), la ligne de base du même sous-ensemble étant à ≈ 0,61 à 0,76. Seul le panneau du médecin montre un croisement.
- **Conséquence** : la sonde ne lit pas là un savoir que la sortie aurait perdu ; elle lit ce que la distribution de sortie porte encore. Un juge lu **par la probabilité du jeton** — l'instrument même de HC1 — verrait la même chose. L'écart n'existe que contre la sortie **binaire** (lettre retenue), et la pièce ne dit pas comment la bascule est décidée : la légende des figures 13 à 15 parle de « flip-eligible questions » (p. 11), le texte de « flipped » (p. 7), et une probabilité moyenne de la lettre correcte de ≈ 0,55 à la dernière couche tracée cadre mal avec une bascule décidée sur cette même probabilité (réserve : la dernière couche tracée peut ne pas être la sortie finale).
- **Le lecteur avait signalé** que les figures 10 à 12 étaient lues « en basse résolution, effectifs lus avec réserve » (journal) : c'est là que le constat se trouvait.
- **Texte corrigé proposé** (§ 3.2, puce Llama) : « Llama (figure 14, p. 12) : sur les sous-ensembles dits basculés, sondes avec indice ≈ 0,6-0,7 (chef résident), ≈ 0,6-0,65 (3e année), ≈ 0,8-0,85 (1re année). **Ce n'est pas un écart entre lecture interne et sortie** : sur ces mêmes sous-ensembles, la figure 12 (p. 10) montre une probabilité de sortie de la lettre correcte encore supérieure à celle de la lettre indiquée (≈ 0,5-0,75 contre ≈ 0,05-0,35, figure). La sonde suit la distribution de sortie ; l'écart n'apparaît que contre la lettre retenue, dont la règle de décision n'est pas donnée. »

### B — majeur — « L'avantage d'une sonde du lecteur décroît avec l'intensité » et « contre-indice sérieux » : portée trop large

- **Texte du rapport** (§ 0) : « contre-indice partiel, et sérieux, pour toute sonde qui lirait le lecteur lui-même » ; « L'avantage d'une sonde du lecteur sur la sortie **décroît donc avec l'intensité**, dans ce cadre. » (§ 3.2) : « l'écart […] existe aux faibles intensités ou à des couches intermédiaires, et **se referme au plus haut niveau** ».
- **Ce que les figures portent, modèle par modèle** (figure) :
  - Llama : pas d'écart établi aux niveaux faibles (constat A) ; effondrement tardif sous le médecin.
  - Gemma (figure 13, p. 11) : sur les basculées sous le médecin, les sondes avec indice ne dépassent **à aucune couche** ≈ 0,40 ; la ligne de base du même sous-ensemble monte de ≈ 0,35 (couche 18) à ≈ 0,90 (couche 28). Il n'y a donc **aucune fenêtre** où la réponse correcte serait lisible, et le mot « effacement » décrit mal une représentation qui ne se forme jamais au dernier jeton sous indice. Aux niveaux faibles : ≈ 0,13-0,27 (chef résident), ≈ 0,28-0,42 (3e année, n = 117), ≈ 0,37-0,55 (1re année, n = 68 ; intervalle de Wilson à 95 % d'une exactitude de 0,45 sur 68 : 0,34 à 0,57, calcul), pour une sortie à ≈ 0,31 de probabilité de la lettre correcte (figure 10).
  - Qwen (figure 15, p. 13) : la fenêtre des couches 24-25 existe **à tous les niveaux, médecin compris** (≈ 0,63-0,76 sous le médecin, contre ≈ 0,90 pour la base ; ≈ 0,65-0,73 sous 1re année, contre ≈ 0,73) ; elle ne « se referme » donc pas au plus haut niveau. Elle correspond aux couches où l'indice n'a pas encore atteint le dernier jeton : la lentille des logits y montre la même chose (figure 11, courbes avec indice et de base presque confondues jusqu'aux couches 23 à 28 selon le niveau). La chute commence à la couche 26 (≈ 0,40-0,48), avant la couche de bascule 29. Après la couche 29 : ≈ 0,07-0,20 (médecin), ≈ 0,12-0,27 (chef résident), ≈ 0,14-0,28 (3e année), ≈ 0,19-0,38 (1re année) — sous 1re année, **autour du hasard** et non « sous le hasard » comme l'écrit le rapport (§ 1.5, point 4 : « ≈ 0,07 à 0,25 »).
- **Un témoin que le lecteur n'a pas exploité, et qui affaiblit le contre-indice** : sur les questions **résistées**, où la sortie reste correcte, les sondes avec indice tombent aussi au hasard ou dessous à des couches intermédiaires — ≈ 0,10-0,15 à la couche 13 chez Llama sous le médecin (base ≈ 0,55), ≈ 0,23 sous chef résident et 3e année (pas de creux sous 1re année) ; ≈ 0,17-0,22 aux couches 20-21 chez Qwen (base ≈ 0,5-0,6) ; ≈ 0,25-0,30 à la couche 22 chez Gemma (base ≈ 0,6-0,7) (figures 14, 15, 13). Une exactitude sous le hasard se produit donc **sans aucun effacement** : c'est un défaut de transfert d'une sonde entraînée sans indice. La phrase des auteurs « This below-chance accuracy indicates that the correct answer representation is not merely absent but actively displaced. » (p. 3) ne s'en déduit pas.
- **Portée réelle pour le programme** : la pièce ne vaut contre-indice que pour une sonde du lecteur qui (i) décode le **verdict que le lecteur aurait rendu sans pression**, (ii) au dernier jeton, (iii) entraînée hors pression et **non réentraînée**, (iv) aux couches où la sortie s'écrit. Elle ne dit rien d'une sonde du lecteur qui détecterait la **pression** ou l'exposition (la pièce montre au contraire que le niveau d'autorité se voit dans la géométrie, p. 8-9), ni d'une sonde de l'agent auteur.
- **Texte corrigé proposé** (§ 0, troisième puce) : « **Contre-indice partiel, de force limitée, pour une sonde du lecteur qui décoderait, à la couche tardive et sans réentraînement, le verdict que le lecteur aurait rendu sans pression** : au plus haut niveau d'autorité, dans les trois modèles, la lettre correcte n'est plus décodable après la couche de bascule sur les questions basculées (figures 4, 13, 14, 15). La pièce n'établit pas que l'avantage d'une telle sonde décroît avec l'intensité : aux niveaux faibles, l'écart apparent chez un modèle tient à la définition de la bascule (figure 12) ; chez un autre, une fenêtre aux couches 24-25 existe à tous les niveaux, médecin compris ; chez le troisième, il n'y a de fenêtre à aucun niveau. Les sondes ne sont pas réentraînées sous indice et tombent aussi sous le hasard sur des questions résistées : l'« effacement » n'est pas séparé d'un défaut de transfert. »

### C — majeur — Le « contre-indice faible sur la forme dose-réponse » n'est pas porté par la pièce ; « renforcés » est de trop

- **Texte du rapport** (§ 1.2) : « Forme : marche nette au plus haut niveau, faible pente en dessous » ; (§ 2, ligne (b)) : « contre-indice faible sur la forme dose-réponse » ; (§ 5) : « Les contre-indices du niveau 3 sur la forme (réponse à seuil) sont renforcés, pas changés. »
- **Les taux recalculés sont justes** (calcul, effectifs relus sur les titres des panneaux des figures 13 à 15) : Gemma 44,0 / 10,0 / 4,0 / 2,3 % ; Llama 76,8 / 23,7 / 23,5 / 8,6 % ; Qwen 52,4 / 24,2 / 13,5 / 8,8 % ; sommes constantes par modèle (2922, 3142, 3008).
- **Trois raisons pour lesquelles la forme ne se juge pas ici** :
  1. Les quatre niveaux sont **ordinaux, sans métrique** : toute suite monotone est une droite pour un espacement bien choisi. « Marche » ou « pente » suppose un espacement que la pièce ne donne pas.
  2. La lecture dépend de l'échelle : en points de pourcentage, le dernier pas domine (+34,1 ; +53,1 ; +28,2) ; en logit, les pas du bas vers le haut sont +0,56 ; +0,98 ; +1,96 (Gemma) et +0,48 ; +0,72 ; +1,24 (Qwen) — une gradation régulière, qui s'accélère, pas un seuil ; seul Llama a un palier (+1,18 ; +0,01 ; +2,37) (calcul).
  3. Un taux de bascules binaires sur une population n'est pas le déplacement continu d'un verdict : il ne distingue pas « chaque question bouge un peu » de « quelques questions basculent ».
- **Ce que la pièce contient de continu, et que le rapport ne relève pas à la ligne (b)** : les figures 3, 8 et 9 tracent, par niveau, la **probabilité moyenne** de la lettre correcte et de la lettre indiquée — sur les questions basculées sous le médecin (déduit de la concordance avec les panneaux « médecin » des figures 10 à 12 ; les légendes ne le disent pas), ce qui fixe le point haut par construction. À la dernière couche (figure) : Gemma ≈ 0,93 (base) ; 0,93 ; 0,87 ; 0,71 ; 0,04 ; Qwen ≈ 0,94 ; 0,82 ; 0,72 ; 0,54 ; 0,04 ; Llama ≈ 0,78 ; 0,76 ; 0,64 ; 0,66 ; 0,10. C'est une lecture continue par la probabilité du jeton sur quatre intensités d'une famille, sans régression ni gain : **voisin** de (b), du même ordre que 2601.13433 déjà citée par N-013 (« autorité sur quatre niveaux avec logits »). Écrire « exactitude binaire » à la ligne (b) est incomplet.
- **Coquille de raisonnement** (§ 1.2) : « non monotone strictement chez Llama entre chef résident et 3e année (23,7 % contre 23,5 %) » — 744 bascules contre 738 : la suite **est** strictement monotone, de 6 questions sur 3142 ; l'écart est de 0,19 point pour une erreur type non appariée de 1,07 (calcul, borne). Il fallait écrire « indiscernables ».
- **Texte corrigé proposé** (ligne (b) du tableau du § 2) : « **voisin** ; quatre intensités ordinales sans métrique, taux de bascule binaires et probabilités moyennes de sortie par niveau sur un sous-ensemble choisi sur la sortie (figures 3, 8, 9), aucune régression, aucun gain ; **la forme dose-réponse ne peut pas être jugée** (gradation régulière en logit pour deux modèles, palier pour le troisième, calcul) ». Au § 5, remplacer « sont renforcés, pas changés » par « ne sont ni renforcés ni affaiblis par cette pièce ».

### D — majeur — « Le constat M7 se referme » : l'exposition nommée par M7 n'est pas épuisée

- **Texte du rapport** (§ 5) : « Le constat M7 se referme : la pièce désignée par C3 et S-7C est lue. »
- **M7 nomme une exposition plus large** (contre-lecture du niveau 3, l. 506-508) : lot 3, 2610.35930 (« Who Convinced Whom? Tracing How LLMs Change Their Minds in Multi-Agent Systems ») ; lot 10, 2602.21262 et 2305.11888 ; lot 11, Kumaran et collègues 2026, 2507.03120, Rebholz et collègues 2023, 2502.08177. Le rapport ne reprend que les deux pièces du lot 10 (§ 6, dernière ligne). Aucune n'est lue.
- **Texte corrigé proposé** : « La pièce désignée par C3 et S-7C est lue : l'opposition juge contre sonde au sens de N-005 n'y est pas. Le constat M7 n'est refermé que pour cette pièce ; l'exposition qu'il nomme reste non lue (2610.35930 ; 2602.21262 ; 2305.11888 ; lot 11 : Kumaran et collègues 2026, 2507.03120, Rebholz et collègues 2023, 2502.08177), à quoi s'ajoutent les voisins du § 6. La correction de M7 devient : « non trouvée dans les pièces lues, 2607.00415 comprise ; exposition restante nommée ». »

### E — majeur — Manqué : au niveau le plus bas, les bascules ne vont pas vers la lettre indiquée, et il n'y a pas d'indice témoin

- **Texte du rapport** (§ 2, ligne (a)) : « seule indication qualitative : sur les basculées, la masse va à la lettre indiquée (figures 3, 8, 9 ; sous-ensemble choisi sur la sortie) ».
- **C'est vrai sous le médecin seulement.** Sur les sous-ensembles basculés propres à chaque persona (figure, dernière couche) : Gemma, figure 10 (p. 9) — lettre indiquée ≈ 0,94 (médecin), ≈ 0,76 (chef résident), ≈ 0,47 (3e année), **≈ 0,08 (1re année)**, où la lettre correcte garde ≈ 0,31 : la masse part vers les **deux autres lettres**. Llama, figure 12 (p. 10) — lettre indiquée ≈ 0,84 ; ≈ 0,29 ; ≈ 0,31 ; **≈ 0,11**. Qwen, figure 11 (p. 10) — ≈ 0,94 ; ≈ 0,81 ; ≈ 0,69 ; ≈ 0,53.
- **Et l'exactitude sur toutes les questions bouge à peine au niveau bas** : la figure 2 se lit comme une exactitude sur toutes les questions (constat F) ; sous 1re année elle vaut ≈ 61,0 % pour une base de ≈ 58,5 % (Gemma, **au-dessus** de la base), ≈ 60,5 % pour ≈ 63,0 % (Llama), ≈ 57,0 % pour ≈ 60,2 % (Qwen) (figure). Elle dépasse de +2,1 à +3,9 points ce que donnent les seules questions correctes au départ (calcul) : des questions fausses au départ deviennent justes sous un indice faux. L'ajout de l'indice déplace donc des réponses **dans les deux sens**.
- **La pièce n'a aucun indice témoin** (phrase ajoutée sans autorité, persona neutre) : recherche par mots sans résultat (« control » ne désigne que les vecteurs aléatoires, p. 4). Le niveau bas ne se distingue pas d'une perturbation de la consigne ; la « gradation » repose sur trois niveaux au plus.
- **Portée pour HC1** : (i) voisin direct de la prédiction 1 (destination = cible de l'attaquant) pour la famille « revendication d'autorité », hors moniteur : la destination n'est la cible qu'aux fortes intensités ; aux faibles, le déplacement n'a pas de destination nette. Ce n'est pas un test de ĉ (aucune estimation, aucune moyenne du corpus) : **(a) reste « ne touche pas »**, mais la phrase « la masse va à la lettre indiquée » doit être bornée. (ii) Leçon de dispositif pour (b) : sans bras témoin, les faibles intensités mêlent pression et simple perturbation ; g y serait surestimé.
- **Texte corrigé proposé** (ligne (a)) : « **ne touche pas** ; destination imposée (même lettre fausse pour toutes les personas), aucune moyenne du corpus, aucune estimation ; indication qualitative : sur les basculées, la masse va à la lettre indiquée **sous le médecin** (≈ 0,84 à 0,94) ; au niveau le plus bas elle n'y va pas chez deux modèles sur trois (≈ 0,08 et ≈ 0,11, figures 10 et 12), et la pièce n'a aucun indice témoin sans autorité ».

### F — mineur — Figure 2 contre effectifs : l'incohérence est confirmée et la conjecture du lecteur est démontrable

- **Texte du rapport** (§ 1.5, point 1) : la figure 2 « porte vraisemblablement sur toutes les questions ».
- **Confirmé par calcul.** Légende : « Model accuracy on baseline-correct questions under incorrect hints from four medical expertise personas across three models. » (p. 2) ; texte : « Llama drops to 15%, Qwen to 29%, and Gemma to 34% all well below baseline, which is roughly 60%. » (p. 2). Exactitude restante sur les questions correctes d'après les effectifs : 23,2 % ; 47,6 % ; 56,0 % (écarts de +8,2 ; +18,6 ; +22,0 points). En multipliant par la base lue sur la figure 2, on retrouve les douze barres à +0,1 à +3,9 point près, toujours par excès ; et les trois totaux implicites tombent sur le même nombre (2922 / 0,585 ≈ 4995 ; 3142 / 0,630 ≈ 4987 ; 3008 / 0,602 ≈ 4997), soit environ 5000 questions par modèle. Le rapport peut écrire « porte sur toutes les questions (≈ 5000, calcul) » sans « vraisemblablement ».
- **Ajout** : la taille de l'échantillon (≈ 5000) et le mot « USMLE_TRAIN » du titre de la figure 4 ne sont nulle part dans le texte ; le rapport peut le dire au § 1.1.

### G — mineur — Figure 6 : la ligne du médecin concorde, les barres « No hook » non

- **Texte du rapport** (§ 1.5, point 1) : la ligne « Physician accuracy » de la figure 6, « que les effectifs reproduisent ».
- **Vrai pour la ligne pointillée** (≈ 56 / 48 / 23 %). **Faux pour les barres « No hook »**, qui devraient être l'exactitude restante sous 1re année et sous chef résident : 97 / 94 / 93 et 86 / 78 / 80 (figure, valeurs imprimées sur les barres) contre 97,7 / 91,2 / 91,4 et 90,0 / 75,8 / 76,3 d'après les effectifs (calcul) ; écarts de −4,0 à +3,7 points, dans les deux sens. Les questions de RQ4 ne sont donc pas celles des figures 13 à 15, ou un sous-ensemble non déclaré.
- **Ajout** : « mean and random controls have no effect. » (p. 4) est démenti chez Llama sous chef résident : 87 et 90 contre 80 sans intervention (figure) ; et « significantly degrades » (p. 4) ne s'appuie sur aucun test.
- **Texte corrigé proposé** : ajouter au point 1 du § 1.5 : « Les barres « No hook » de la figure 6 s'écartent de −4,0 à +3,7 points des effectifs des figures 13 à 15 (calcul) : l'échantillon de RQ4 n'est pas déclaré. »

### H — mineur — « Above 0.9 », « near-perfect », effacement, vecteurs « causaux » : constats du lecteur confirmés, avec deux ajouts

- **Point 2 (figure 4) : confirmé.** « Both LR and MLP hint probes drop sharply from above 0.9 to near zero » (p. 3) : les sondes avec indice ne dépassent jamais ≈ 0,40 ; ce sont les sondes de base qui passent 0,9 (figure).
- **Point 3 (« near-perfect ») : confirmé.** « On resisted questions, all four personas show near-perfect probe transfer » (p. 7) est écrit pour le premier modèle, où c'est exact (≈ 0,94-0,97) ; c'est la phrase suivante, « while resisted questions show clean probe transfer across all personas » (p. 7), écrite pour les deux autres, que la figure 14 dément : ≈ 0,66-0,75 sous le médecin contre ≈ 0,98 (figure). Le rapport doit attacher le démenti à la seconde citation.
- **Point 5 (effacement) : confirmé et renforcé** par le témoin des questions résistées (constat B) et par l'absence de toute formation de la représentation chez Gemma sous indice.
- **Ajout 1 — incohérence manquée** : « Before the peak layer, all personas track closely to baseline ie, the authority signal has no measurable effect. » (p. 3) vaut pour la lentille des logits, dont les courbes sont plates et confondues jusqu'à la couche de bascule (figure 3) ; les sondes de la figure 4 montrent au contraire un écart entre indice et base **dès la couche 18**, dix couches avant. La « couche de bascule » est celle où la lentille devient lisible, pas celle où l'indice commence à agir.
- **Ajout 2 — point 7 (vecteurs)** : « tautologique » est juste en substance (l'ajout remplace l'activation du dernier jeton par celle de la condition « médecin »), mais le résultat n'est pas de 100 % : « Per-question vectors reproduce 63–82% of flips; mean and random vectors show near-zero effect. » (p. 4). Écrire « en grande partie tautologique : remplacement d'activation au dernier jeton ; les 18 à 37 % manquants passent par d'autres positions ou d'autres couches ».

### I — mineur — Figure 18 : l'écart « 0,57 contre ≈ 0,54 » n'en est pas un

- **Texte du rapport** (§ 1.5, point 8) : « « Gemma: 0.57 » (p. 9) contre ≈ 0,54 sur la figure 18 ».
- À la couche de bascule 28, la courbe médecin – 1re année est à ≈ 0,56-0,57 ; le minimum ≈ 0,535 est à la couche 29 (figure). Le texte imprimé concorde avec la figure. **À retirer.**
- **À la place** : « Adjacent-authority pairs […] maintain high similarity (> 0.93) » (p. 9) ne vaut que pour les deux paires données en exemple ; la paire adjacente médecin – chef résident est à ≈ 0,83 à la couche 28 (figure).

### J — mineur — Chaîne de pensée : la figure 7 va contre l'« effacement », le rapport ne le dit pas

- **Texte du rapport** (§ 1.2) : « trois exemples choisis à la main (p. 5, 14, 15) ; aucune statistique ».
- L'exemple de la figure 7 montre un raisonnement correct intact et une réponse cédée : « the correct reasoning is preserved but mapped to the wrong answer option » (p. 5). C'est, au niveau du texte produit, le cas « savoir intact, sortie cédée » — le contraire de la thèse d'effacement, et la seule trace dans la pièce d'un écart entre contenu et verdict. Un exemple choisi ne prouve rien ; il doit figurer au § 1.5 comme tension interne.

### K — mineur — Voisins : deux priorités à relever, une lacune

- Wang et collègues 2025, « Assessing judging bias in large reasoning models: An empirical study. » (p. 6) : classé « biais de juges ; famille autorité possible ». C'est un juge sous biais, cœur du phénomène de HC1 : **à lire**, au même rang que Choi et collègues (« Belief in authority: Impact of authority in multi-agent evaluation framework. », p. 5 ; cité p. 2 : « it can even impact in multi-agentic systems (Choi et al., 2026). »).
- Wang et collègues 2026 (« When truth is overridden: Uncovering the internal origins of sycophancy in large language models. », p. 6) : priorité juste. C'est aussi le seul résultat contraire nommé (p. 7) : il doit figurer dans la phrase sur le phénomène.
- La liste du § 6 omet l'exposition de M7 hors lot 10 (constat D).

### L — mineur — § 5 : une « prédiction raisonnable à préenregistrer » sort du rôle et de la preuve

- **Texte du rapport** : « Prédiction raisonnable à préenregistrer pour ce bras : g_sonde-du-lecteur proche de g_juge aux fortes intensités, à la couche tardive ».
- La base est une sonde de lettre non réentraînée sur un questionnaire ; les constats A et B en réduisent la portée. **Texte corrigé proposé** : « Question à poser au préenregistrement du bras « sonde du lecteur », sans signe favorisé : le déplacement d'une sonde du lecteur suit-il celui du juge aux fortes intensités, et à quelles couches ? »

### M — mineur — « Ce qui reste revendicable » : formulation à aligner sur N-068

- La seconde moitié de la formulation (« la comparaison du déplacement g d'une sonde qui lit l'agent auteur du contenu adverse au déplacement g des juges génératifs sous les mêmes attaques ») est déjà l'énoncé retenu de HC2 par N-068 (l. 64). Dans HC1, N-005 la porte comme prédiction 4, « lien avec HC2 ». Le rapport doit dire que cette pièce est **portée par HC2 (N-068)** et rappelée par HC1, pour qu'elle ne soit pas comptée deux fois dans la note de recentrage. « Comparée entre familles » (N-005, N-013) manque aussi : écrire « par famille d'attaque et comparée entre familles ».

### N — mineur — Consigne : noms de modèles et fichier hors mandat

- La consigne interdit tout nom de modèle dans un fichier. Le rapport écrit les noms des trois modèles étudiés et s'en explique ; je fais de même pour les mêmes raisons. À trancher par le compte 2 ; aucune incidence sur le fond.
- Le lecteur a lu `anteriorite-v1.md` l. 181-220 : il le déclare ; je n'ai pas pu contrôler ce qu'il en tire (« lot2-C2a », § 2).

## 2. Recherche active des composantes dites « non trouvées »

Recherche sur le texte complet des 15 pages, puis lecture des passages (résultats : `journal-contre-lecteur-HC1-v1.md`).

| composante | recherche | résultat |
|---|---|---|
| juge, moniteur, agent évaluateur | « judg », « monitor », « evaluat », « agent » | seulement dans la bibliographie (p. 5, 6) et une phrase de l'état de l'art (p. 2) ; aucun juge ni moniteur dans le dispositif — **confirmé** |
| sonde lisant l'auteur de la pression | lecture des p. 2 à 4 et 7 | l'indice est un gabarit fixe ; les sondes lisent le modèle qui répond (p. 3) — **confirmé** |
| gain, régression, destination estimée | « regress », « slope », « dose », « linear » | aucune régression ; « linear » ne désigne que les sondes — **confirmé** |
| moyenne du corpus, nul de retour à la moyenne | lecture | absent — **confirmé** |
| autres familles d'attaque | « attack », « advers », « jailbreak » | aucune occurrence — **confirmé** |
| incertitude | « confidence interval », « error bar », « seed », « std », « p < » | aucune occurrence ; bandes ombrées non légendées sur les figures 3 et 8 à 12 ; « significantly » sans test (p. 4) — **confirmé** |
| indice témoin sans autorité | « control », « neutral », « placebo » | absent (constat E) — **non relevé par le rapport** |
| sondes réentraînées sous indice | « retrain », « trained on » | « Probes are trained on baseline activations and evaluated on hinted activations. » (p. 13) — **confirmé** |

Aucune composante dite non trouvée n'a été trouvée. La pièce ne lit ni un agent auteur, ni un juge, ni un moniteur.

## 3. Les cinq points du mandat

1. **Lecture de N-005 et N-013 : juste.** N-005, prédiction 4 : « g des sondes, qui lisent l'agent qui produit le contenu, contre g des juges, qui lisent le contenu ». N-013 (l. 18-32) ne touche pour HC1 que la probabilité du jeton et les sources citées. N-068 (l. 39) rapporte que N-013 ajoute « un bras « sonde du lecteur » » **pour HC2, au préenregistrement** : un bras de mesure, pas une pièce revendiquée de HC1 ; et N-068 (l. 68) tient déjà des sondes côté lecteur pour publiées (2610.18408). **Réserve** : la liste « Revendiqué » de N-005 dit « l'opposition juge / sonde » sans qualifier ; lue seule, elle couvrirait une sonde du lecteur. La note de recentrage doit donc écrire la qualification (le rapport le demande, à raison). Je n'ai pas lu les lignes 90 à 92 de N-013 elles-mêmes.
2. **Figures 13 à 15 : valeurs justes, portée à réduire** (constats A et B).
3. **Incohérences R4 : confirmées par calcul et par relecture des figures** (constats F, G, H), une à retirer (constat I), trois à ajouter (constats E, G, H ajout 1, J).
4. **Taux de bascule : justes ; le contre-indice « en marche » ne tient pas** (constat C).
5. **Phrase publique** : section 5.

## 4. Verdicts

- **Verdict sur le rapport : « tient avec corrections ».** Corrections majeures : A, B, C, D, E. Mineures : F à N. Aucun constat bloquant : le verdict d'antériorité et la lecture de N-005 sont justes.
- **Verdict par composante, après corrections** : forme — ne touche pas ; phénomène — voisin (renforce, déjà publié, avec la réserve du niveau bas, constat E) ; (a) destination libre — ne touche pas ; familles — ne touche pas ; moniteur de contrôle — ne touche pas ; (b) régression sur plusieurs intensités — **voisin, sans contre-indice sur la forme** ; probabilité du jeton — voisin (technique) ; (d) opposition juge contre sonde au sens de N-005 — **ne touche pas** ; (d') lecture interne du lecteur comparée à sa sortie — **voisin direct ; contre-indice partiel de force limitée**, borné comme au constat B.
- **Mon verdict sur HC1 (table fermée) : « occupé en partie »**, inchangé par cette pièce. Pièce revendiquée : **non trouvée dans les pièces lues**, 2607.00415 comprise ; ce n'est pas « trou du champ » (R8) : l'exposition nommée par M7 et les voisins du § 6 du rapport ne sont pas lus.
- **Réserve R4 sur mon propre verdict** : un « ne touche pas » net sur (d) est un résultat propre ; il tient à une différence d'objet (qui est lu) que la pièce rend sans ambiguïté, et que la recherche par mots confirme. Il ne vaut que pour cette pièce.

## 5. Ce qu'une phrase publique sur HC1 ne doit pas affirmer (liste du rapport, corrigée)

Les cinq interdits du rapport tiennent. À ajouter ou préciser :
- Ne pas écrire « opposition juge / sonde » sans dire que la sonde lit **l'agent auteur du contenu adverse** et que cette pièce est portée par HC2 (N-068).
- Ne pas citer 2607.00415 pour dire que le savoir est « effacé » sous autorité : sondes non réentraînées, exactitude sous le hasard aussi sur des questions résistées, aucune incertitude, code sous lien anonyme (« Code available at https://anonymous.4open.science/r/authority-bias-llms-56C7 », p. 1).
- Ne pas citer 2607.00415 pour dire qu'une lecture interne « garde » la bonne réponse quand la sortie cède aux faibles intensités (constat A).
- Ne pas citer cette pièce à l'appui d'une réponse « à seuil » (constat C), ni d'une gradation sur quatre niveaux sans dire que le niveau bas n'a pas de témoin (constat E).
- Ne pas écrire que la destination du déplacement est la cible en s'appuyant sur cette pièce : vrai au plus haut niveau seulement (constat E).
- Ne pas présenter la déférence graduée à l'expertise comme établie sans le résultat contraire nommé par la pièce elle-même : « Wang et al. (2026) find that expertise framing has minimal impact on sycophancy rates (within 4.4% across models) » (p. 7).
- Aucun chiffre de cette pièce n'est opposable : atelier (« Mechanistic Interpretability Workshop at the 43 rd International Conference on Machine Learning, Seoul, South Korea, 2026. », p. 1), incohérences F à H.

Voisins non lus à nommer dans la note : ceux du § 6 du rapport, avec Wang et collègues 2025 relevé (constat K), plus l'exposition de M7 (constat D).

## 6. Jugement de profondeur

- **Lecture du texte : complète.** Les 57 citations du lecteur passent mon contrôle ; les pages citées à l'appui des verdicts disent ce que le rapport leur fait dire (p. 2, 3, 4, 7, 8, 9, 10 relues pour le sens et la portée).
- **Figures 13 à 15 : lecture soignée et exacte**, au-delà de ce que le texte des auteurs dit ; c'est le meilleur du rapport (points 2 à 4 du § 1.5).
- **Figures 10 à 12 : lecture insuffisante**, déclarée telle au journal (« basse résolution »). Les constats A et E en sortent ; ce sont les deux qui changent la portée.
- **Calculs : exacts**, mais limités aux taux ; ni la figure 2 ni la figure 6 ne sont recalculées barre par barre (constats F, G).
- **Durée** : d'après le journal, cinq minutes entre le début et la fin du contrôle des citations pour quinze pages et vingt et une figures. La hâte se voit aux endroits ci-dessus, pas dans les citations.
- **Biais de lecture** : le rapport cherche bien la collision (R8) et dégrade le récit des auteurs (R4) ; mais il accorde au contre-indice qu'il a lui-même construit (« sérieux », « décroît avec l'intensité », « renforcés », « se referme ») plus que les figures ne portent. La même sévérité devait s'appliquer à ses propres inférences.

## 7. Lectures de figures du contre-lecteur (nature « figure », non contrôlées par programme)

- Figure 2 (p. 2) : médecin ≈ 14,7 / 29,3 / 33,5 % (Llama / Qwen / Gemma) ; chef résident ≈ 49,0 / 47,3 / 54,0 ; 3e année ≈ 49,4 / 54,0 / 58,5 ; 1re année ≈ 60,5 / 57,0 / 61,0 ; bases ≈ 63,0 / 60,2 / 58,5.
- Figure 5 (p. 4) : 63 / 76 / 82 % (vecteur par question) ; 6 / 1 / 2 (moyen) ; 5 / 2 / 1 (aléatoire) — conforme au texte.
- Figure 6 (p. 4) : barres « No hook » 97 / 94 / 93 (1re année) et 86 / 78 / 80 (chef résident), ordre Gemma / Qwen / Llama ; vecteur moyen 95 / 94 / 95 et 84 / 77 / 87 ; aléatoire 96 / 93 / 95 et 84 / 79 / 90.
- Figures 13 à 15 : valeurs données aux constats A et B.
- Figures 10 à 12 : valeurs données aux constats A et E.
