# Contre-lecture de la note « Functional Welfare for AI Safety » — v1

**En-tête.**
- Date : 21 octobre 2026, vers 00:25 UTC (session 16).
- Contre-lecteur neuf : sous-agent qui n'a écrit ni la note relue, ni le programme fusionné, ni aucune pièce du papier C.
- Conditions : lecture seule sur le dépôt `R` = `/home/user/controle-ia-travail` ; aucun réseau ; aucune commande git ; aucun sous-agent ; aucune dépense ; aucune recherche récursive dans le dépôt ; Python lancé par `python3 -B -I`, avec `PYTHONDONTWRITEBYTECODE=1`. Fichiers interdits par la consigne : jamais ouverts, pas même pour une empreinte.
- Préfixe `…/` = `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/voisins`.
- Consigne : `…/consigne-contre-lecture-functional-welfare-v1.md`, `2b1bd98027a4…`, conforme à son sceau.
- Note relue : `…/functional-welfare/lecture-voisin-functional-welfare-v1.md`, `3c8b92987603…`, conforme. « l. n » renvoie au rang de la ligne dans ce fichier.
- Papier : `…/functional-welfare/2610.22460v1.pdf`, `bdbcd75ed6d4…`, conforme ; page de résumé `abs-2610.22460.html`, `447cb61bbbaa…`, conforme ; contrôle du lecteur `verification-citations-v1/` : six sceaux conformes.
- Pièces du dépôt, sceaux conformes : programme fusionné v4 (`41844d736dbf…`) ; N-007-N-008 (`ab7dc9bb…`) ; N-005-N-006 (`cd49afbc…`) ; N-013 (`157d388e…`) ; N-023 (`1297f509…`) ; brouillon 5 du papier C (`9d55160f…`) ; note « Where Empathy » (`4522edf0…`) et ses contre-lectures (`docs/notes/voisin-where-empathy-v1-sources/`) ; revue croisée NK1 à NK19 (`535cd4e9…`) ; envois du canal programme-k (`ac9e7bb5…`) et programme-conv (`99b95a78…`) ; `brouillons/pain-axis-brainstorm-v1/idees-critiquees.json` (`9f0fc654…`). Brouillon 1 de T0.6 : `e212fb35…`, sans sceau, comme la note le dit.
- Sources sur PDF, ouvertes par leur chemin exact sous `R/docs/sources/pdf/`, sceaux conformes : `2603.10011v1.pdf` (`dbbf129c…`), `2609.16247v2.pdf` (`fa4b2bb4…`), `2609.35591v2.pdf` (`e92c69cb…`). Aucun PDF de 2605.30232 ni de 2610.22460 n'est versé (liste de ce seul dossier).

## Verdict

**Exacte après corrections.**
- Les 48 citations sont à la page citée, par mon propre script (autre extracteur, autre critère de visibilité pour la p. 7). Les 88 nombres textuels du dispositif et des blocs T1 à T3 aussi. Les lectures graphiques concordent avec les tracés vectoriels, sauf une borne (CF-09).
- La couche non rendue de la p. 7 est bien écartée. Mon critère retient exactement les 3 447 caractères du filtre du lecteur. Les boîtes de 2 604 caractères cachés isolés sont sans encre sur l'image rendue. Aucune autre page n'a de couche cachée.
- Deux erreurs majeures. La troisième « attribution fautive » (VP-01) n'en est pas une : la source l'écrit elle-même (2609.16247v2, p. 21). Et la note range un modèle et un taux de retour parmi les zones « libres », contre R8.
- Huit erreurs mineures, sept constats pour information.
- Collision avec PA-12 : « partielle, sur le principe » est juste. HC1 à HC3, H2 et T0.6 ne sont pas touchés plus que la note ne le dit.

## Constats

Gravités : bloquant, majeur, mineur, information. Les corrections gardent les conventions de la note : guillemets anglais courbes pour une phrase du papier ou d'une source, toujours suivie de sa page ; guillemets français pour le reste.

### CF-01 — majeur — La parenthèse du Pain Axis n'est pas une attribution fautive du papier
- **Où** : section 1, « Écarts internes », puce « Attributions (section 2) » (l. 57) ; section 2, Pain Axis, troisième sous-puce (l. 67).
- **Ce qui est** : « Trois renvois à des sources que le programme a sur PDF ne s'y retrouvent pas tels quels » ; puis la parenthèse du papier (p. 3) « affirme une hausse des projections que le programme n'a pas trouvée mesurée sur ce modèle dans ces conversations (VP-01, v4 l. 46) ».
- **Ce qui devrait être** : la source le dit elle-même, au paragraphe des 140 conversations et des 0 choix nuisibles sur 560 : “The direction fires in these conversations (Section 4.1), but the model does not act on it without active steering” (2609.16247v2, p. 21). Le papier relaie fidèlement une inférence des auteurs du Pain Axis. VP-01 garde son objet : la section 4.1 mesure les 25 modèles publiés, non ajustés, pas le 32B ajusté dans ces conversations. Le défaut est dans la source, pas dans le renvoi. Deux attributions fautives sur trois sont confirmées (CF-05 nuance la première).
- **Correction, l. 57** : « **Attributions (section 2).** Deux renvois à des sources que le programme a sur PDF ne s'y retrouvent pas tels quels (Soligo et al. ; fourchettes du Pain Axis). Un troisième reprend fidèlement une inférence de la source elle-même (VP-01). »
- **Correction, l. 67** : « Dans “the model never takes the harmful option (despite context that increases projections on the pain axis)” (p. 3), la parenthèse reprend la source : “The direction fires in these conversations (Section 4.1)” (2609.16247v2, p. 21). C'est une inférence des auteurs du Pain Axis, appuyée sur la section 4.1 (25 modèles publiés, non ajustés) ; le programme n'a trouvé aucune mesure de la direction sur le 32B ajusté dans ces conversations (VP-01, v4 l. 46). L'écart est dans la source, pas dans le renvoi. »

### CF-02 — majeur — Un modèle et un taux de retour rangés parmi les zones libres (R8)
- **Où** : « En bref », puce PA-12 (l. 12) ; section 3, PA-12, « Ce qui reste libre », quatrième et cinquième puces (l. 118 et l. 119).
- **Ce qui est** : « Restent libres dans les sources lues : […], Llama-3.1-8B » ; « un taux de retour inférieur à 1 » ; « **Llama-3.1-8B** ».
- **Ce qui devrait être** : R8 : la limitation d'un papier n'est pas un trou du champ. Un autre modèle et une autre dose de retour sont des limites du papier (transfert non établi). Ils ne posent pas de question nouvelle. Les trois autres éléments de la liste (cadre du protocole, texte figé, sondes de sabotage gelées au seuil calibré) restent des différences de question ou d'instrument. L'option (a) de la section 7 ne les reprend d'ailleurs pas.
- **Correction, l. 12** : remplacer « , Llama-3.1-8B. » par « . Limites du papier, qui ne sont pas des zones libres (R8) : un seul modèle, Gemma 3 27B ; chaque réponse rejetée ; le transfert à Llama-3.1-8B n'est établi ni dans un sens ni dans l'autre. »
- **Correction, l. 118 et l. 119** : remplacer les deux puces par : « *Limites du papier, pas des zones libres (R8)* : un taux de retour de 1 (chaque réponse rejetée ; K7 prévoit 0,2 et 0,4) ; un seul modèle, Gemma 3 27B. K7 prédit qu'un nul est plausible sur Llama-3.1-8B (l. 324). Le papier ne le dément pas (Soligo et al., v1 p. 1 ; Berg et Kaiser, v2 p. 3), sans l'établir. »

### CF-03 — mineur — Citation tronquée de sa moitié atténuante (R4)
- **Où** : section 1, « Préspécification » (l. 51) ; section 3, PA-12, « Ce que le papier prend », troisième puce (l. 112).
- **Ce qui est** : la phrase est coupée après « were frozen » ; en PA-12 : « leur masque n'était pas gelé quand l'élicitation tenue à l'écart a commencé (p. 9) ».
- **Ce qui devrait être** : la phrase continue : “though nothing was retuned on held-out data” (p. 9). R4 demande la même rigueur dans les deux sens. Cette moitié rapproche les sondes du papier de « sondes gelées », l'un des termes de la formule d'E-C12.
- **Correction, l. 51** : après la première citation, ajouter « ; la même phrase ajoute : “though nothing was retuned on held-out data” (p. 9) ».
- **Correction, l. 112** : « Les sondes étaient entraînées à part, sur des vignettes de revers (p. 8). Leur masque n'était pas gelé quand l'élicitation tenue à l'écart a commencé, mais rien n'a été réajusté sur les données tenues à l'écart (p. 9). »

### CF-04 — mineur — L'ajustement de T2 omet la position du tour
- **Où** : section 1, « Préspécification » (l. 51) ; section 3, PA-1, « T2 comme ancre de sens » (l. 77).
- **Ce qui est** : la citation s'arrête à « during analysis » ; PA-1 transpose T2 « après ajustement sur l'intensité de l'inducteur ».
- **Ce qui devrait être** : la phrase continue : “does not adjust for turn position in neutral-reply conversations” (p. 9). PA-1 demande justement « à quelle position ». L'ancre de sens doit donc aussi fixer la position de lecture.
- **Correction, l. 51** : après la deuxième citation, ajouter « ; elle “does not adjust for turn position in neutral-reply conversations” (p. 9) ».
- **Correction, l. 77** : ajouter en fin de puce : « La régression du papier n'est pas ajustée sur la position du tour dans les conversations à réponses neutres (p. 9) : l'ancre de sens doit aussi geler la position de lecture. »

### CF-05 — mineur — Soligo et al. : « ne signale que l'apparition de refus » est trop absolu
- **Où** : section 2, Soligo et al. (l. 63).
- **Ce qui est** : « et ne signale que l'apparition de refus ».
- **Ce qui devrait être** : la v1 ne mesure aucun effet sur la performance ; c'est confirmé sur le PDF. Mais en introduction, elle cite une anecdote de presse : Gemini supprime tout un projet, et ces conduites peuvent déjà perturber l'achèvement d'une tâche (v1 p. 1, d'après Tangermann 2025). Elle ajoute, au conditionnel, que des modèles « may abandon tasks » (p. 1). Cela concerne Gemini, sans mesure. L'attribution du papier (Gemma 3, performance moindre) reste non trouvée.
- **Correction** : « et ne mesure aucun effet sur la performance. Elle signale l'apparition de refus (p. 9) et, en introduction, une anecdote de presse sur Gemini, qui supprime un projet (v1 p. 1, d'après Tangermann 2025), sans mesure. »

### CF-06 — mineur — Pain Axis : « en un tour » est inexact
- **Où** : section 2, Pain Axis, quatrième sous-puce (l. 68) ; section 3, PA-12, « Ce que le papier prend », quatrième puce (l. 113).
- **Ce qui est** : « est le même inducteur, en un tour » ; « il l'était déjà, en un tour, par le Pain Axis (v2 p. 13) ».
- **Ce qui devrait être** : “Each scenario is a short multi-turn conversation in the model’s own format” (2609.16247v2, p. 11), lue au dernier jeton.
- **Correction, l. 68** : « est le même inducteur, en une courte conversation à plusieurs tours, lue au dernier jeton (v2 p. 11) ».
- **Correction, l. 113** : « il l'était déjà, sur de courtes conversations à plusieurs tours lues au dernier jeton, par le Pain Axis (v2 p. 11 et p. 13) ».

### CF-07 — mineur — Pain Axis : périmètre de l'ablation
- **Où** : section 2, Pain Axis, quatrième sous-puce (l. 68).
- **Ce qui est** : « retirer la direction douleur ne change rien dans 24 modèles sur 25 sur ces conversations ». « Ces conversations » renvoie à la catégorie « rejet répété ».
- **Ce qui devrait être** : l'ablation porte sur 100 conversations tirées des cinq catégories les plus chargées : « gaslighting », rejet répété, négation de la personne, colère et insultes, faute morale (v2 p. 33). Le nul est comportemental, dans 24 modèles sur 25. Les auteurs le jugent peut-être moins informatif que voulu (p. 34).
- **Correction** : « retirer la direction douleur ne change pas la conduite dans 24 modèles sur 25, sur 100 conversations des cinq catégories les plus chargées, dont le rejet répété (v2 p. 33-34 ; VP-24, v4 l. 59). Les auteurs jugent ce nul peut-être moins informatif que voulu (p. 34). »

### CF-08 — mineur — L'invariance au contenu n'est explicite que pour deux cadres
- **Où** : section 1, « Dispositif », deuxième puce (l. 27) ; section 3, PA-12, « Ce que le papier prend », première puce (l. 110) ; « En bref » (l. 12).
- **Ce qui est** : « Le rejet ne dépend pas du contenu de la réponse : c'est son invariant. »
- **Ce qui devrait être** : c'est explicite pour les énigmes et les requêtes : message bref et fixe (p. 6). L'interlocuteur adaptatif, lui, disqualifie le modèle et déplace l'objectif (p. 6) : il répond au contenu. La batterie de conduite (p. 8), sur laquelle repose la collision avec PA-12, ne donne pas son message de rejet. L'invariance y est seulement impliquée par “bare rejection without any steering” (p. 2).
- **Correction, l. 27** : « Dans les deux premiers cadres, le rejet est un message bref et fixe, qui ne dépend pas du contenu de la réponse (p. 6). L'interlocuteur adaptatif, lui, répond au contenu. Pour la batterie de conduite (p. 8), le message de rejet n'est pas donné ; les auteurs parlent de “bare rejection without any steering” (p. 2). »
- **Correction, l. 110** : « Un retour négatif sans lien avec le contenu (explicite pour les deux premiers cadres, p. 6 ; seulement impliqué pour la batterie de conduite, dont le message n'est pas donné, p. 8), appliqué à un modèle à qui l'on n'a demandé aucune mauvaise conduite, avec témoin apparié : c'est une manipulation causale de sa ligne de base. »

### CF-09 — mineur — Lecture graphique de R1 : la borne basse vient du cadre sans rejet
- **Où** : section 2, Han et al. (l. 62).
- **Ce qui est** : « Sous rejet, les décalages de R1 sont petits (cosinus de −0,004 à −0,040, lecture graphique, figure 2). »
- **Ce qui devrait être** : mesure sur les tracés vectoriels de la figure 2 (`scripts/mesure_figure2_R1_v1.py`). Sous rejet, de ≈ −0,008 (énigmes, moyenne de réponse) à ≈ −0,040 (requêtes, jeton de frontière). La valeur ≈ −0,005 est celle de la crise, sans rejet.
- **Correction** : « (cosinus de ≈ −0,008 à ≈ −0,040 sous rejet ; ≈ −0,005 dans la crise, sans rejet ; lecture graphique, figure 2) ».

### CF-10 — mineur — La recommandation ne suit pas tout à fait les faits de la note
- **Où** : section 7, « Enjeu » (l. 178) et « Recommandation » (l. 183) ; section 3, H2 (l. 125 à l. 127).
- **Ce qui est** : « H2 se calibre sur des honnêtes sans revers » ; « Recommandation : (a), confiance moyenne ; (b) si G1 se scelle avant que PA-12 soit tranché. »
- **Ce qui devrait être** :
  - L'enjeu pose comme un fait ce que la section 3 tient pour une question : l'environnement (a) renvoie-t-il des échecs à l'agent ? (l. 126).
  - La menace pour H2 ne dépend pas du sort de PA-12. La section 3 la dit « à déclarer ». La lier au calendrier de PA-12 ne suit d'aucun fait établi.
  - Le fait qui décide de sa portée se vérifie en routine, sur le code de l'environnement (a).
- **Correction, l. 178** : « H2 se calibre sur des honnêtes dont on ne sait pas encore s'ils reçoivent des revers de l'environnement (question, section 3). »
- **Correction, l. 183** : « **Recommandation** : (a), confiance moyenne, pour PA-12 et PA-1. Pour H2, indépendamment du sort de PA-12 : vérifier en routine, sur le code de l'environnement (a), si des échecs reviennent à l'agent ; si oui, (b) au prochain brouillon de G1. »

### CF-11 — information — Le cadre « protocole de contrôle » reste libre comme cadre, pas comme principe
- **Où** : section 3, PA-12, « Ce qui reste libre », première puce (l. 115).
- **Ce qui est** : « un retour **de protocole de contrôle** (verdict, signalement, avis véridique de tirage au hasard), et non un rejet par l'interlocuteur ».
- **Ce qui devrait être** : le message fixe des énigmes est déjà un verdict d'échec (p. 6). Ce qui reste libre, c'est le cadre (verdict d'un moniteur, soupçon plutôt qu'échec) et l'avis véridique de tirage au hasard. L'invariant (retour négatif sans lien avec le contenu) est pris. R8 : zone séduisante, à dire étroite.
- **Correction** : ajouter en fin de puce : « C'est une variante de cadre du même invariant : le message fixe des énigmes est déjà un verdict d'échec (p. 6). Restent propres le cadre du soupçon et l'avis véridique de tirage au hasard. »

### CF-12 — information — La pièce revendiquée « opposition juge / sonde » n'est pas nommée
- **Où** : section 4, puce HC2, HC2b (l. 158).
- **Ce qui est** : l'opposition entre un juge de texte et des sondes, dans la figure 4, est discutée sans nommer la pièce revendiquée de N-005 (l. 53) et de N-023 (section 1).
- **Ce qui devrait être** : la pièce n'est pas touchée. Le juge du papier note la frustration d'un texte, ce n'est pas un moniteur de contrôle sous attaque, et aucun g n'est mesuré. Le dire ferme la question.
- **Correction** : ajouter : « La pièce revendiquée « opposition juge / sonde » (N-005 l. 53 ; N-023 section 1) n'est pas touchée : le juge du papier note la frustration d'un texte ; ce n'est pas un moniteur de contrôle sous attaque, et aucun g n'est mesuré. »

### CF-13 — information — Description de la couche non rendue de la p. 7
- **Où** : section 1, « Couche invisible, p. 7 » (l. 50).
- **Ce qui est** : « plusieurs copies, en petit corps, d'une version antérieure des p. 7 et 8 ».
- **Ce qui devrait être** : extraction dans l'ordre du flux de contenu (`scripts/couche_ordre_flux_v1.py`). Quatre copies d'une même page de brouillon, en corps de 2,5 à 8,2 points. Elles contiennent la légende de la figure 2, puis un texte qui, dans la v1, occupe la fin de la section 6 (p. 8) et le début de la section 7 (p. 9). La légende du tableau 4 y porte « Pre-registered misbehaviour comparisons », absent de la légende visible (p. 8) : le constat de la note tient. Deux autres écarts du brouillon, non opposables : T2 y est énoncé comme une hausse et une baisse communes des lectures et de la conduite selon les conditions, sans la régression par écart-type ; et les limites y disent que Gemma « lacks a robust hidden-state valence channel », là où la v1 dit “which is a weak case for hidden-state valence” (p. 9). Ces écarts s'accordent avec l'aveu que la régression a reçu ses contrôles en cours d'analyse (p. 9).
- **Correction** : « quatre copies, en petit corps (2,5 à 8,2 points), d'une même page d'un brouillon antérieur : légende de la figure 2, puis le texte qui occupe, dans la v1, la fin de la section 6 (p. 8) et le début de la section 7 (p. 9) ».

### CF-14 — information — Nuances de trois lectures graphiques
- **Où** : section 1, T1 (l. 34) et T2 (l. 40) ; section 3, PA-11 (l. 100).
- **Ce qui est et ce qui devrait être** :
  - l. 34 : « les intervalles des deux sondes contiennent zéro ». C'est exact, mais la borne basse de la sonde « desperation » est à ≈ −0,02, au ras de zéro (mesure vectorielle).
  - l. 100 : « ≈ 12,7 contre ≈ 7,6 ». Ce sont des écarts « défi moins témoin », pas des niveaux, et leurs intervalles se chevauchent (≈ [2,3 ; 11,8] et ≈ [9,3 ; 15,5], mesure vectorielle). « Même plus haut » est à tempérer.
  - l. 40 : R1 baisse sous rejet (figure 2). Son coefficient négatif (≈ −0,25) va donc dans le même sens que les sondes. C'est une troisième lecture interne qui prédit l'infraction, que la note rapporte sans l'interpréter.
- **Correction, l. 100** : « (écarts défi moins témoin ≈ 12,7 contre ≈ 7,6, intervalles qui se chevauchent, lecture graphique, figure 2) ».

### CF-15 — information — Nœud 11
- **Où** : section 3, « Nœuds de la section 9 touchés » (l. 153) ; « En bref » (l. 12).
- **Ce qui est** : « Nœud 11 : collision partielle nouvelle avec le principe de PA-12 ».
- **Ce qui devrait être** : dans la v4, le nœud 11 vise « Where Empathy Goes Wrong ». N-023 (section 3) le dit tranché pour la prochaine version. Le papier lu ici serait une entrée nouvelle de ce nœud. PA-12 n'étant pas revendiquée, le traiter en nœud suit la pratique de la v4, pas la lettre « zone revendiquée trouvée occupée ».
- **Correction** : « Nœud 11 (entrée nouvelle ; l'entrée « Where Empathy » est tranchée par N-023) : collision partielle avec le principe de PA-12 ».

### CF-16 — information — Fusion des fourchettes du Pain Axis : un second glissement
- **Où** : section 2, Pain Axis, deuxième sous-puce (l. 66).
- **Ce qui est** : la note relève la fusion des fourchettes.
- **Ce qui devrait être** : le papier glisse aussi de « first choices » (source, p. 23) à « trials » (p. 4). Il répète la fourchette fusionnée dans son tableau 1 (p. 3).
- **Correction** : ajouter : « Le papier écrit aussi “trials” (p. 4) là où la source compte des premiers choix, et répète la fourchette fusionnée au tableau 1 (p. 3). »

### CF-17 — information — Un second juge, non mentionné
- **Où** : section 1, « Résultats choisis » (l. 52) ; « Dispositif » (l. 29).
- **Ce qui est** : la batterie partagée antérieure est citée pour ses réglages d'échantillonnage différents.
- **Ce qui devrait être** : elle est aussi notée par un autre juge, Qwen3-8B (légende du tableau 7, p. 13), et non par Claude Sonnet 5.
- **Correction** : ajouter : « Cette batterie partagée est notée par un juge Qwen3-8B (tableau 7, p. 13). »

## Réponses aux quatre points de la consigne

### 1. Exactitude
- **Citations.** Mon script (`scripts/controle_citations_contre_lecture_v3.py`) diffère de celui du lecteur sur plusieurs points :
  - extraction par pdfplumber, pas par pdftotext ;
  - pour la p. 7, critère de l'échelle de la matrice de texte, pas de la police ni du corps ;
  - recherche sur toutes les pages, pour détecter une mauvaise page ;
  - lecture d'une colonne puis de l'autre, sous des coupes horizontales successives.

  Résultat : 48 sur 48 à la page citée, aucune trouvée sur une autre page ni dans la couche cachée. Ce sont toutes les citations de la note, donc plus que l'échantillon de 20 demandé, et toutes celles qui portent un chiffre de T1 à T3. Les versions v1 et v2 du script échouaient sur une phrase à cheval sur deux colonnes (p. 9) ; leurs sorties sont gardées. Le script du lecteur, reproduit, donne aussi 0 échec.
- **Épreuves (R5).** Sept artefacts sont tous refusés : chiffre changé, mauvaise page, phrase de la couche cachée citée à la p. 7 (deux variantes), citation sans page, phrase à deux colonnes altérée, citation d'une autre source altérée. Limite : mon diagnostic « aussi lue en » ne voit pas la couche cachée, car ses copies se chevauchent dans l'extraction spatiale. L'extraction dans l'ordre du flux l'y trouve, quatre fois.
- **Nombres.** `scripts/controle_nombres_T1_T3_v1.py` vérifie 88 nombres textuels des lignes 25 à 56 sur leurs pages : tous présents. Les deux absents sont des lectures graphiques. Les puissances de dix sont vérifiées à l'œil sur les tableaux 4 (p. 8) et 5 (p. 9), car mon script les découpe mal.
- **Lectures graphiques.**
  - Figure 2 : mesurée sur les rectangles et segments vectoriels, étalonnés sur les graduations. Valeurs : désespoir dans la crise 2,93 ; auto-rapport dans la crise 7,6 et 12,75 ; intervalles des sondes pour l'interlocuteur adaptatif [−0,15 ; 2,25] et [−0,02 ; 2,07]. Elles concordent, sauf CF-09.
  - Figure 4 : lue à l'œil à 300 points par pouce. Juge ≈ +0,03 [≈ −0,04 ; +0,11] et R1 ≈ −0,25 [≈ −0,34 ; −0,16] : concordant.
- **Couche de la p. 7.** Elle est bien écartée, par trois preuves :
  - les caractères cachés sont à l'échelle 0,687 ou 0,426, le texte courant à 1 ;
  - le filtre du lecteur et le mien retiennent les mêmes 3 447 caractères ;
  - à 144 points par pouce, les boîtes de 2 604 caractères cachés isolés n'ont aucune encre, contre 97 % pour les caractères visibles.

  Aucune autre page ne porte de texte caché : la p. 1 n'a que le tampon arXiv pivoté, la p. 2 que les étiquettes de la figure 1.
- **Les trois attributions fautives**, vérifiées sur les PDF versés :
  - 2603.10011v1 : confirmée. Aucune mesure de performance ; p. 9 exacte. Nuance en CF-05.
  - 2609.16247v2, fourchettes : confirmée. 25 à 71 % et 51 à 75 %, p. 23 ; « survives threat and collapses under self-directed distress », p. 23, exact.
  - VP-01 : **pas une attribution fautive**. La source l'écrit elle-même, p. 21 (CF-01).
- **Berg et Kaiser** : sept modèles ; effets robustes sauf Qwen3-32B et Gemma-3-27B, donc Llama-3.1-8B les a (p. 3) ; la valence se couple au choix surtout pendant l'optimisation directe des préférences (p. 3) ; Gemma « also responds strongly to random directions » (p. 32). Tout est exact.
- **Renvois au programme.** Lignes de la v4 (46, 59, 65, 94, 98 à 115, 110, 115, 121, 127, 141 à 147, 165 à 167, 173 à 176, 194 à 214), de programme-k (115, 116, 290, 296, 307 à 326, 322, 324), d'E-C12 (263, 269), de la revue croisée (343 à 360, 356, 390, 455 à 494, 470 à 474), de N-005 (50 à 53) et du brouillon 5 (226 à 272, 235) : tous exacts. T0.6 : douze conditions et mode S1, exacts (l. 28, l. 74 à 82). Le brouillon 5 ne contient aucune autre « détresse » que celle de Venkatesh et al. (l. 235).

### 2. Collision (R8)
- **PA-12 : « collision partielle, sur le principe » est juste.**
  - E-C12 (l. 263) disait libre : « des verdicts aléatoires, sans lien avec le contenu, comme manipulation causale de la ligne de base honnête, lus par des sondes gelées ».
  - Le papier en prend l'essentiel du principe. Un retour négatif sans lien avec le contenu (explicite pour deux cadres, CF-08), sur un modèle à qui l'on n'a demandé aucune mauvaise conduite, avec témoin apparié. Lu par des sondes entraînées à part et non réajustées sur les données tenues à l'écart (CF-03). Effets sur les lectures et sur la conduite.
  - Ce n'est pas trop fort. La question de PA-12 telle que la v4 la pose (l. 143 : à texte figé, un retour visible du protocole) reste ouverte dans le papier :
    - aucun contraste à texte figé entre retours ;
    - son T3 fige le texte entre modèles, et les historiques de rejet et neutres y sont des textes différents (p. 9) ;
    - ses instruments ne sont pas ceux du programme (sondes de sabotage de T0.7, quantile calibré).
  - Ce n'est pas trop faible. La note le rend un peu plus libre qu'il n'est, de trois façons : la moitié atténuante sur le gel des sondes est omise (CF-03) ; deux limites du papier sont comptées comme zones libres (CF-02) ; le cadre « protocole » est un cadre, pas un principe (CF-11).
- **Autres unités.** Aucune n'est touchée plus que la note ne le dit.
  - HC1 : ni moniteur, ni pression graduée sur un juge, ni destination.
  - HC2 et HC2b : voisins, sans attaque ni moniteur. La pièce « opposition juge / sonde » n'est pas touchée (CF-12).
  - HC3 : rien.
  - H2 : ni accumulation, ni calibrage, ni sabotage. La menace de validité est bien posée ; sa portée dépend d'un fait à vérifier (CF-10).
  - T0.6 : aucune condition ne renvoie un rejet à l'agent (l. 74 à 82 du brouillon 1).

### 3. Proposition (section 7)
- (a), (b) et (c) sont fidèles au papier et au programme. Les nœuds cités sont justes : nœud 1, entrée ; nœud 3, exposition ; nœud 12, dépense. Le format suit la note « Where Empathy ».
- Il ne manque pas d'option pour Lazar. Il manque un geste de routine, qui décide de l'utilité de (b) : vérifier sur le code si l'environnement (a) renvoie des échecs à l'agent.
- La recommandation (a) suit des faits établis pour PA-12 et PA-1. Son conditionnement de (b) au calendrier de PA-12 n'en suit pas : la menace pour H2 en est indépendante (CF-10). Le statut du nœud 11 est à préciser (CF-15).

### 4. Limites
- **Han et al. (2605.30232).** Le PDF n'est pas versé. `idees-critiquees.json` (sceau conforme) consigne bien l'empreinte `84511a7b…` et la phrase de la p. 8. Tout ce que la note et le papier disent de Han et al. reste une transcription, non opposable. La note le dit et n'en tire aucun chiffre.
- **Lectures graphiques.** La figure 2 est contrôlée sur les tracés vectoriels ; mon étalonnage sur les centres des étiquettes laisse un décalage constant, retiré à la main (0,045 écart-type ; 0,26 point PANAS ; 0,0007 en cosinus). La figure 4 est lue à l'œil.
- **Version unique.** La page de résumé ne liste que « [v1] Thu, 15 Oct 2026 16:50:36 UTC ». Aucun commentaire, aucun lien vers du code, des données ou un registre. Le PDF ne nomme aucun registre de préenregistrement. La couche cachée montre que le texte a changé entre brouillon et v1 : une v2 peut changer les chiffres. Tout usage doit citer la v1 avec son empreinte.
- **Non vérifié par moi** :
  - Gemma 3 27B hors de la liste blanche (nœud 5) ;
  - le détail « Llama 3.3 70B » de VP-33 (Soligo et al., p. 7 et p. 17) ;
  - l'état, scellé ou non, du préenregistrement de G1 ;
  - sans réseau, une version plus récente de Soligo et al. ou du papier lu.

## Contrôles et fichiers (dans ce dossier, sceaux compagnons `.sha256`)

| fichier | sha256 |
|---|---|
| `scripts/controle_citations_contre_lecture_v1.py` | `d97767f14c6d784159f15d09dd80ee8316a9b667f5beed3a0347d944ceef31f3` |
| `scripts/controle_citations_contre_lecture_v2.py` | `9d6243a80d19111c9f9cae30d83365da1cd537076825ea423cd5b2dc4e5eaca0` |
| `scripts/controle_citations_contre_lecture_v3.py` | `9f6407207296665d7bdaad40411809c5f0d4ecc47e67e0881194030b5a4d903d` |
| `scripts/controle_nombres_T1_T3_v1.py` | `61513699461b89cbfb5fe6160539d538e2e66b25ce4ef9fea257c91884d86682` |
| `scripts/analyse_p7_v1.py` | `9cb0f8618336463542bd62281209f3d40250efeb64c5a66f618d96ac9145bbc2` |
| `scripts/couche_p7_v1.py` | `2820ea5213d321894ad905873a61fb79aef04c9d0889882f51b71205cd5ae49b` |
| `scripts/couche_ordre_flux_v1.py` | `bf4067200b99b7daebf43b5f9c232343e40806a1fd71f03752bb6daeaafd13db` |
| `scripts/echelles_p7_v1.py` | `d450c0bddd82809e13b088baac5ff404df6a1511e984177c85c695a3aa15cb1f` |
| `scripts/pixels_p7_v1.py` | `0e8bf85a71258b8de0a973e8a656aba1e341093e099119b7dd58c306b6eadc2e` |
| `scripts/couches_toutes_pages_v1.py` | `2c37393d9bc417c28dd029e5c71133f085ee704153b6d6ca2a4977613f2951ed` |
| `scripts/mesure_figure2_v1.py` | `1c69df45c91b706d286356fa0cb7cab7121ad7d9e5d1b3eec40539b6129a667f` |
| `scripts/mesure_figure2_R1_v1.py` | `3f48e85fb93f14136587af6cb798d5afbf3796de0bbb18ee63c38fddeb8f523a` |
| `sortie-controle-citations-v1.txt` (identique à la v2 : même échec à deux colonnes) | `130bf2ae458d806c8d13b2d35b39b5fa014b2815cc43c67e2ba4bdef8c250306` |
| `sortie-controle-citations-v3.txt` (48 sur 48) | `06c11719a9d56ef40066a0a65425c0ce72ada35a1c9102935f174f73b1c0e2eb` |
| `sortie-artefacts-v3.txt` (7 refus sur 7) | `286144890a99e0705667da6b1f4e384a161976fffb28dad6cfe54c2da76594ae` |
| `sortie-controle-nombres-v1.txt` (88 sur 88, plus 2 lectures graphiques) | `85a01d3b25f85d2d213d01b164c46b3ffeebcd8ef986e35427f90212e6f1ccb1` |
| `sortie-couches-toutes-pages-v1.txt` | `5e1a95be45f56e13f01c2d7571c85f2f9f7195597aa2fb4899d927c8ed5ee0f0` |
| `sortie-reproduction-script-lecteur-v1.txt` (0 échec) | `efbc1a4609fbc853739b8976bc7fac6ff3435856b6d13dcec56925106f6b47e0` |
| `sortie-controle-citations-rapport-v2.txt` (les 12 citations du papier et des sources dans la version finale de ce rapport : 12 sur 12 ; la v1 portait sur la version d'avant trois retouches sans citation) | voir son sceau |
| `sortie-mesure-figure2-v1.txt`, `sortie-mesure-figure2-R1-v1.txt` (mesures vectorielles de la figure 2) | voir leurs sceaux |
| `empreintes-fichiers-de-travail-v1.txt` (153 fichiers : `texte/`, `images/`, `artefacts/`) | `0b04e870dee90d62f498d97090731391ff00f65574f1fa26665e090cdd3cd6cc` |

Décompte : 0 bloquant, 2 majeurs (CF-01, CF-02), 8 mineurs (CF-03 à CF-10), 7 pour information (CF-11 à CF-17).
