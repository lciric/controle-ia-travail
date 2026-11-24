# Erratum 1 du correctif 1 de la v3 du programme et de la feuille de route de publication du papier D

- **Date** : 24 novembre 2026, vers 14 h 30 (temps universel). Pièce de travail. Auteur : Claude Fable 5.2, effort élevé.
- **Pièce corrigée, gardée intacte** : `strategie-cibles-et-feuille-de-route-publication-papier-d-v3-correctif-1.md` (empreinte `67894f0b32726ee4…`). Elle se lit désormais avec cet erratum, qui prime sur les cinq points ci-dessous et sur eux seuls.
- **Origine** : vérification des corrections par le contre-lecteur, Claude Opus 5.5, effort élevé : « corrections acceptées » ; douze défauts traités, le dixième en partie ; quatre défauts mineurs nouveaux, à porter par erratum, sans nouvelle boucle (`verification-opus-corrections-programme-v3-v1.md`, `3c2187dfa7fe25d1…`).
- **Contrôle de l'auteur pour le point 5** : `calc/controle_v3_correctif_1_erratum_1.py` (graine `SeedSequence(2026112417)`), hors dépôt. Aucun fichier du dépôt n'est modifié.

## 1. Second lien en attente dans la page de dépôt

**Où.** Section 7.1, paragraphe « Traces internes à retirer avant diffusion ».

**Avant.** « Dans la page de dépôt : le lien vers le PDF laissé en attente et les noms de fichiers internes. »

**Après.** « Dans la page de dépôt (`P/github-page/README-v4-correctif-3.md`) : deux liens laissés en attente, le lien vers le PDF (`[LINK_PDF]`, ligne 36) et le lien vers le billet (`[LINK_LESSWRONG_POST]`, ligne 38), et les noms de fichiers internes. »

## 2. Ce que le contre-lecteur a réellement refait

**Où.** Section 1.3, phrase d'introduction et phrase finale ; section 8.1, phrase de cadre.

**Avant, section 1.3.** « Le contre-lecteur a relancé le premier et refait les points 1 à 6 par ses propres scripts ; ses comptes concordent avec ceux-ci. »

**Après, section 1.3.** « Le contre-lecteur a refait par ses propres tirages les points 3 (pièges par mélange), 5 (niche parfaite à la contre-lecture ; détection partielle à la vérification) et 6 (un exemple). Pour les points 1, 2 et 4, il a relancé le script de l'auteur et vérifié les formes closes, sans tirages à lui. Ses résultats concordent en signe avec ceux de l'auteur ; les effectifs diffèrent, les tirages n'étant pas les mêmes (par exemple 75 289 contre 75 552). »

**Avant, section 8.1.** « (`calc/controle_v3_correctif_1.py` ; le contre-lecteur trouve les mêmes signes par ses propres tirages) ».

**Après, section 8.1.** « (`calc/controle_v3_correctif_1.py`). Le contre-lecteur trouve les mêmes signes par ses propres tirages pour trois lignes du tableau : la première (taux de croissance de la part furtive, moyenne seule, gradient naturel), la quatrième (avantage normalisé du furtif) et la sixième (taux du furtif contre le visible sous division par l'écart-type). Les autres lignes reposent sur les seuls tirages de l'auteur, relancés par le contre-lecteur. »

Précision sur la numérotation : le rapport de vérification écrit « lignes 1, 3 et 4 ». Les trois grandeurs que ses scripts tirent sont celles nommées ci-dessus ; dans le tableau de la section 8.1 elles occupent les lignes 1, 4 et 6. Le freinage sous gradient euclidien (ligne 7) a été confirmé par lui en forme close, non par tirages.

## 3. Deux effectifs pour le freinage sous gradient euclidien

**Où.** Section 1.3, point 2 ; section 8.1, dernière ligne du tableau.

**Constat.** Les deux effectifs sont exacts. Ils viennent de deux scripts aux graines différentes.

**À lire ainsi.**
- Section 1.3, point 2 : « négatif dans les 17 750 tirages où la part honnête dépasse $1/\sqrt 3$ (`calc/controle_v3.py`, graine `SeedSequence(2026112415)`) ».
- Section 8.1, dernière ligne : « décroît dans les 17 672 tirages où la part honnête dépasse $1/\sqrt 3$ (`calc/controle_v3_correctif_1.py`, graine `SeedSequence(2026112416)`) ».

## 4. Si la section sur le budget d'audit entre dans le manuscrit de base

**Où.** Section 4, « Version courte » ; section 7.1, ligne « Report de la remarque sur la marge dans le manuscrit » ; section 7.2, tâche 8.

**Constat.** La tâche 8 peut faire entrer cette section, ou son théorème de l'audit tiré au hasard, dans le manuscrit de base avant le 1er décembre, si Lazar répond « oui » à la précision demandée en section 6, point 3. La section 4 ne peut alors plus dire « aucun théorème nouveau n'est requis ».

**Section 4, à lire ainsi.** « Le manuscrit de base suffit : deux théorèmes, leurs remarques, la remarque sur les procédures. Aucun théorème nouveau n'est requis, **sauf si Lazar répond que sa « remarque au manuscrit » vise le manuscrit de base (section 6, point 3)** : la version courte porte alors aussi le théorème de l'audit tiré au hasard, avec sa section ou la part de sa section qui le fonde, et la remarque sur la marge. »

**Section 7.1, ligne du report, colonne « Il faut d'abord », à lire ainsi.** « vérification des correctifs 3 et 4 de la section sur le budget d'audit ; corrections de références propres à cette section, selon le registre des références (`D/verification-references-v1/registre-references-v2.md`) : harmonisation des trois clés du budget d'audit avec celles du manuscrit ; la référence à Zhang et al. de 2008 sur l'enseignement de politiques, non confirmée, à ne pas garder sans vérification des actes ; l'article d'Aslam, Popa et Rivest, dont le titre reste à établir, à citer si celui de Rivest l'est ; les citations que l'en-tête du brouillon marque « à vérifier sur PDF », dont le théorème précis de l'ouvrage de Boucheron et al. ; entrée de la section, ou de son théorème de l'audit tiré au hasard, dans un fichier neuf du manuscrit ; précision de Lazar (section 6, point 3). »

**Section 7.2, tâche 8.** Elle porte ces corrections de références avec le report. Rien d'autre n'y change : pas de dépense, pas de diffusion.

## 5. Détection partielle : la condition close à la place de la fréquence

**Où.** Section 8.1, première des « Trois précisions » ; par renvoi, la table de correspondance, défaut 1 (« 49 720 tirages sur 100 000 »).

**Avant.** « **Hors de la niche parfaite**, […] le taux de croissance de la part furtive ne croît avec la pénalité que dans 49 720 tirages sur 100 000, et le taux du furtif contre l'honnête baisse toujours. »

**Après.** « **Hors de la niche parfaite**, quand le furtif est intercepté une partie du temps, la première ligne ne tient plus en général. Sous gradient naturel avec la moyenne seule pour ligne de base, la dérivée, par rapport à la pénalité, du taux de croissance du logarithme de la part furtive vaut
$$\pi_{\mathrm v}(1-\beta_{\mathrm v})-(1-\beta_{\mathrm f})(1-\pi_{\mathrm f}).$$
La pénalité accélère donc le furtif si et seulement si $\pi_{\mathrm v}(1-\beta_{\mathrm v})>(1-\beta_{\mathrm f})(1-\pi_{\mathrm f})$ ; en niche parfaite ($\beta_{\mathrm f}=1$) on retrouve $(1-\beta_{\mathrm v})\pi_{\mathrm v}>0$. Le taux du furtif contre l'honnête a pour dérivée $-(1-\beta_{\mathrm f})$ : il baisse toujours dès que le furtif est parfois intercepté. »

**Sur la fréquence.** Elle n'est pas une propriété du modèle : elle dépend de la loi de tirage des paramètres. Avec la survie du furtif tirée uniformément entre celle du visible et 1, la condition tient dans 49 720 tirages sur 100 000 (`calc/controle_v3_correctif_1.py`). Avec une survie du furtif tirée uniformément entre 0 et 1, elle tient dans 25 077 tirages sur 100 000 (tirages du contre-lecteur). Le contrôle de l'auteur pour cet erratum donne 49 964 et 24 978 sur d'autres tirages, la forme close s'accordant à la dérivée numérique à $10^{-9}$ près dans les 200 000 cas, et le taux du furtif contre l'honnête n'y monte jamais.

## Ce qui ne change pas

Tout le reste du correctif 1, en particulier : les trois points soumis à Lazar et la proposition de la section 6 ; les statuts de la table d'intégration ; le calendrier, hors l'ajout du point 4 ; les contraintes (aucune dépense, formalisation en Lean et arbre exact à quatre bras après le 1er décembre, aucune diffusion, aucune date présentée comme vérifiée).
