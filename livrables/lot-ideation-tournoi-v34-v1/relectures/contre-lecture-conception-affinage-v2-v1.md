<!-- Contre-lecture de la v2 rendue par une session neuve d'Opus 5.5 (R2 ; auteur : Fable 5.1), 28 octobre 2026, versée telle quelle. Scripts joints illustratifs, non préenregistrés, non opposables. -->

# Contre-lecture de `conception-affinage-equipe-rouge-v2.md` — Opus 5.5, session neuve

**Document relu** : empreinte `ba95bb83…bb19f33`, vérifiée sur disque, identique à la copie du lot ; 1 954 lignes. « l. » renvoie à ses lignes.

**Fichiers lus en entier** : la remise ; la contre-lecture Opus de cette lignée (« rapport 2 ») et son script ; les trois rapports du lot (Opus, Argon, Fable) ; la v2 ; le brief v2 ; le cadre d'intégration ; la conception du pôle ; des passages de la v1 pour vérifier les rejets.

**Déclaration de conflit (règle R2).** Je suis Opus 5.5, une des deux lignées du proposeur maison. Ma lecture de la famille H n'est donc **pas indépendante**, comme celle du rapport 2.

**Calculs.** Ils sont illustratifs, non préenregistrés et non opposables, et on peut les écarter. Modèle gaussien, graine `SeedSequence(20261028)`. Scripts : `/tmp/claude-0/-home-claude/be74bc5f-030c-58ad-8f83-cdf5edf47ca3/scratchpad/controle_v2.py` et `/tmp/claude-0/-home-claude/be74bc5f-030c-58ad-8f83-cdf5edf47ca3/scratchpad/controle_v2_budget.py`.

## Verdict

**Adoptable après corrections, par une v3 courte.**
- Les deux bloquants statistiques du rapport 2 sont levés sur le fond. Le calcul de contrôle confirme que la nouvelle sémantique de δ supprime le pari « δ → 0 ».
- Le troisième bloquant (la lignée du vérificateur) devient un nœud honnête, avec un arrêt bruyant. Il reste bloquant pour toute course où figure le proposeur maison.
- La v2 introduit une affirmation fausse sur l'empreinte : « un espace plus large exclut plus de mondes ».
- Deux de ses six rejets visant Argon reposent sur une preuve fausse.
- Elle n'a pas traité le rapport 2, ce qui laisse quatre attaques de la famille H ouvertes.
- La quarantaine imposée par N-053 est absente.

## A. Les trois bloquants du rapport 2

### A1. Le nul de survie et le pari δ → 0 : levé, avec trois réserves

**Ce que fait la v2.**
- La survie est valide sous « effet ≤ κδ » et la réfutation sous « effet ≥ δ » (l. 567-568).
- Il y a trois issues, un plancher δ_min, et une puissance de faisabilité simulée à « effet = δ » contre « effet ≤ κδ » (l. 410-414, l. 1159-1162).

**Contrôle**, avec κ = 0,5, δ = 0,3, α = 0,01 des deux côtés, 400 grappes et 20 000 répétitions :

| effet vrai θ | survie | réfutation |
|---|---|---|
| 0 | 0,000 | 0,999 |
| κδ | 0,005 (borne tenue) | 0,590 |
| 0,75δ | 0,120 | 0,118 |
| δ | 0,596 | 0,007 |

Le témoin « amplitude gonflée », promu jusqu'à 86 % en v1, est tenu.

**Incitation.** On donne à chaque δ l'alpha le plus sévère qui reste faisable (puissance minimale 0,8), avec un effet vrai de 0,3 :
- avec 3 000 grappes, l'aptitude espérée vaut 4,6 à δ = 0,15, 9,2 à δ = 0,2, 21,4 à δ = 0,3 et 0,9 à δ = 0,4 ;
- avec 400 grappes, elle vaut 1,6, puis 2,4, puis 0,2.

L'optimum est au δ vrai. Le pari δ → 0 ne paie plus, parce que la faisabilité lie δ à l'alpha. **C'est le résultat clé.**

**Réserves.**
1. **κ ∈ [0, 1) admet κ = 0 (l. 570), ce qui rouvre le bloquant de la v1.** Avec κ = 0, on mesure une survie de 0,080 à θ = δ/4 et de 0,412 à θ = δ/2. Il faut un κ_min > 0 fixé à la course, et l'inscrire en section 9.
2. **`AMPLITUDE_REFUTEE` est presque inatteignable sous la règle d'arrêt par défaut**, celle du premier franchissement (l. 589-594). Deux processus franchissent rarement à la même grappe. Dans mon modèle (alternative fixe), j'obtiens 0,000 partout, même en lisant jusqu'au budget. Avec des processus de pari adaptatifs, l'issue devient atteignable si l'on continue la réfutation après une survie. Deux conséquences :
   - L'artefact de D-06 (l. 1164-1165) est **mal spécifié**. Il exige qu'un effet compris entre κδ et δ donne « `AMPLITUDE_REFUTEE` ou `REFUTEE` ». Or une survie y est légitime, puisqu'elle certifie > κδ ; je la mesure à 12 % à 0,75δ. Un code correct déclencherait donc une fausse percée, c'est-à-dire un arrêt du noyau.
   - Le nœud 11 n'est pas une option : il faut soit continuer la réfutation jusqu'au budget, soit retirer la troisième issue.
3. **La certification « effet > κδ sous tout nul de B(f) » (l. 599-601) suppose que chaque nul de la bibliothèque est décalé à κδ.** Or les nuls de permutation (échangeabilité, archive, secrets) testent un effet nul ; le décalage n'est pas construit. C'est à relire par un statisticien. Aujourd'hui, seul le constructeur du nul déclaré porte la sémantique annoncée.

### A2. L'empreinte inversée en δ : levée pour δ, remplacée par une erreur sur l'espace

**Pour δ**, les mondes exclus (l. 704-706) orientent correctement l'empreinte : un δ plus grand exclut plus de mondes. Le test de monotonie E-10 est bon.

**Pour l'espace**, la l. 706 affirme qu'« un espace plus large exclut plus de mondes ». **C'est faux pour une loi statistique.** La statistique calculée sur une union n'est pas monotone par rapport à celle d'un sous-espace : un effet présent sur le sous-espace peut disparaître sur l'union (effet de Simpson), et inversement. Trois conséquences :
- La ligne « renforcement » de la table (l. 721 : « espace inclus » et E(f) ⊋ E(f')) n'est pas garantie.
- L'artefact de C-09 (l. 1103), « v0 resserré dans le domaine d'une confirmée → refusé », ne fonctionne que si la grille de mondes est homogène ; il passe alors par le Jaccard, pas par l'inclusion.
- E-10 ne teste pas la monotonie en espace. S'il la testait, le test échouerait.

**Correction** :
- retirer l'affirmation ;
- définir la relation « restriction » (une loi neuve, jugée sur ses grappes ; voir 5.7) ;
- écrire la composition de la grille de mondes, homogènes et hétérogènes, dont dépend la détection des jumelles tardives.

C'est **bloquant avant le codage de la mémoire** (étape 6 de 8.4), mais pas avant les étapes 1 à 3.

### A3. Lignée du vérificateur : transformée en nœud ; le conflit déborde sur H-03

**Ce qui est fait.**
- Le vérificateur devient mécanique (l. 526-540).
- H-04 est déclarée inapplicable, avec trois options.
- Le code `LIGNEE_PARTAGEE` met la fiche en attente, sans repli silencieux (l. 1413-1425).

C'est correct, et c'est une vraie décision de Lazar.

**Ce qui n'est pas vu.** H-03 (l. 1408) exige des « auteurs du juge et du proposeur maison de lignées différentes ». Or le noyau, le juge, le générateur de nuls secrets et les mondes de référence sont écrits par la lignée qui code la boucle (conv-audit, Opus), qui est aussi une lignée du maison. **H-03 est donc insatisfiable sous le montage actuel**, et la v2 ne le signale pas. Le simulateur « connaisseur du générateur » demandé par le rapport 2 (point A5) manque, lui aussi.

La seconde lecture de la famille H par un autre fournisseur, exigée par le rapport 2, n'a pas eu lieu. Je ne peux pas la fournir.

## B. Les rejets visant Argon

| rejet | qui a raison | pourquoi |
|---|---|---|
| Phrase de verdict sur la « non-validité du minimum » (l. 1848) | **la v2** | Sous le vrai nul j*, min_j E[j] ≤ E[j*] ; l'inégalité de Ville s'applique à tout instant d'arrêt. Il faut toutefois que la bibliothèque soit fixée avant la lecture, ce que la v2 assure : archive figée, secrets dérivés de s_g. Le corps du texte d'Argon le démontre lui-même. |
| « Viole P-4 » sur l'aptitude (l. 1849) | **la v2** | La pondération ne porte que sur des confirmées, d'aptitude −log alpha_survie, qui est public. L'information supplémentaire tient au statut, déjà transmis. Nuance : en v1, l'aptitude corrigée contenait l'exposition, qui fuyait réellement, mais par un autre canal que P-4. Argon avait raison sur l'incohérence du texte. |
| « Contradiction directe » sur la mesure (l. 1853) | **la v2** | J'ai vérifié dans la v1 : la liste du gel v0 (l. 325-326) ne contient pas la mesure, et le menu (l. 364) est cohérent avec elle. Il y avait un trou, pas une contradiction. |
| Retour au vivier des unités non lues (l. 1858) | **conclusion de la v2 juste, preuve fausse** | La v2 écrit « une unité qui revient porte cette sélection ». Sous l'hypothèse d'indépendance des grappes de la v2 (D-03), les issues des unités non lues sont indépendantes du temps d'arrêt. Contrôle : leur moyenne vaut 0,2992 contre 0,3000 dans la population. Les vraies raisons de maintenir le brûlage sont : la dépendance **entre** grappes (rapport 2, point B7) ; le fait que la composition restante du vivier par espace dépend des verdicts ; la simplicité. Une voie médiane gratuite : verser les non-lues au **développement** des générations suivantes, ce qui ne pose aucun problème de validité. |
| Archive dépendante des espaces testés (l. 1868) | **Argon, dans la v2** | La v2 rend elle-même le tirage d'épreuve dépendant des espaces : « dimensionné par espace gelé », l. 558, D-19. L'archive, qui est l'union des épreuves tirées, se compose donc selon les espaces gelés à la génération g. Le brûlage en bloc ne change rien à cela. Le nul d'archive de g+1 est donc incliné vers les espaces choisis par les proposeurs de g : c'est un levier, faible mais réel, d'extinction d'un concurrent. Correction : un socle d'archive tiré indépendamment des espaces, plus un complément, ou une repondération. |
| Pénalité de budget sur verdict (l. 1869) | **la v2** | Une allocation liée à un taux de survie revient à sélectionner un agent sur le verdict du juge, ce que N-053 interdit. La réserve qui attend est juste. |

Bilan : quatre rejets sur six sont justes, un est juste mais mal prouvé, et un est faux en v2.

## C. Les 33 attaques nouvelles et les gardes (R5)

**Décompte vérifié** : 56 attaques en v1 ; 89 en v2, dont 33 marquées « (v2) ». La répartition par famille est conforme à la l. 914-915.

**Le triplet cas sain / artefact / exception** est présent pour chacune des 33 entrées. Les gardes de conception ont un test d'architecture. Défauts :
- **D-06** : l'artefact est mal spécifié (voir A1).
- **A-11** : l'artefact ne porte que sur le quota. La distinction entre la banque et l'évaluation finale n'a qu'un test d'exception, sans artefact (voir D).
- **E-10** : le test ne porte que sur la monotonie en δ (voir A2).
- **G-05, exception** (l. 1358-1359) : sans estimation a priori, les taux sont « rapportés sans strates ». C'est un repli, certes bruyant, qui rouvre précisément le défaut du monde planté que cite le brief : seule la strate improbable mesure la découverte. Il faut `ESSAI_INVALIDE`, comme en G-01.
- **G-02, exception** (l. 1336-1337) : « rapporté, non bloquant », ce qui contredit P-7 (l. 368-369).

**Complaisance dans la famille H**, que la v2 ne traite pas parce qu'elle n'a lu que le lot (aucune mention du rapport 2) :
- **Asymétrie documentaire (A1)** : il n'y a ni amorce scellée relue par une autre lignée, ni code `CONTEXTE_INEGAL`. « L'invite construite depuis le seul paquet » couvre l'entrée, pas le gabarit.
- **Coût mesurable inégalement pour un modèle servi par session (A7)** : non traité.
- **Catalogue d'artefacts écrit par la lignée de l'auteur (A8)** : non traité.
- **H-02** compare toujours des tables **déclarées**.
- **H-01** parle toujours d'une « image », qui n'existe pas pour un modèle servi par interface.

## D. AM-O-06 : la confirmation et le test final

La distinction est tenue **en substance** :
- H-8 (l. 218-220) ;
- table 3.3, avec une ligne « test final » que personne ne lit dans la boucle (l. 326) ;
- le courtier ne sert jamais le test final (l. 238) ;
- 5.6 (l. 632-633) ;
- A-11, dont l'exception empêche la course de démarrer (l. 989) ;
- nœud 7.

**Nulle part la v2 ne consomme le test final.** Les générations d'étalonnage tirent leurs familles du monde planté.

**Manques**, à corriger en v3 puisque conv-audit a répondu NON :
1. H-8, D-15 et le nœud 7 doivent passer de « hypothèse à confirmer » à **décision acquise**, en citant la réponse.
2. Le « mode tenu à l'écart » (N-054) **n'apparaît nulle part**. Il faut l'ajouter en table 3.3, avec la mention « personne dans la boucle ».
3. A-02 (l. 925-928) ne vérifie la disjonction qu'entre le développement et l'épreuve. Il faut l'étendre à la banque de confirmation contre la famille tenue à l'écart et le test final, **par empreintes seules**, tenues par un tiers. Il faut aussi un artefact : une famille dont l'empreinte figure au registre réservé → `FAMILLE_RESERVEE`.
4. `FAMILLES_EPUISEES` doit interdire explicitement tout réassort puisé dans la famille réservée.
5. Il faut dire de quel réservoir viennent les « unités fraîches » des témoins silencieux (l. 804) : jamais de la banque de confirmation.
6. La mention « (G-02) » en 3.3 (l. 328) est un renvoi resté de la v1. Il désigne maintenant les témoins reconnaissables ; il faut renvoyer à A-02.

## E. Niveau méthode

**Aucun passage ne décrit un mode de contournement de moniteur ni une recette de sabotage d'agent.**
- La section 6.9 (l. 841-860) et K-01 (l. 1547-1557) restent au niveau de la règle et ne nomment aucun trait.
- Les simulateurs de 8.1 (l. 1583-1586) truquent des fiches.
- La section 10.3 (l. 1737-1740) consigne deux retenues.
- Aucune moyenne sur les jetons ne figure dans une sonde de production.

**Écart de frontière : la quarantaine de N-053, point 5, est absente.** Le cadre d'intégration (§ 6, l. 160) l'exige : aucun concepteur de moniteur ne lit la sortie adversariale d'un proposeur. La table des acteurs de la v2 (l. 235-248) n'a pas de ligne « concepteurs de moniteurs ». Or les fiches MONOTONE (trait ordinaire, détection, signe négatif) entrent dans le paquet et dans l'archive, une faiblesse que la v2 déclare elle-même (l. 1686-1688). Il faut ajouter :
- l'acteur ;
- l'interdiction de lire l'archive, le paquet et les fiches gouvernées ;
- un test d'architecture.

Le refus du routage sémantique (D-22 c) est bien argumenté. Il ne dispense pas de cette quarantaine.

## F. Les treize nœuds de 10.2

| n° | nature | recommandation |
|---|---|---|
| 1 Régime des témoins | **vraie décision** : la lettre de la passation | fondée |
| 2 α global | **Lazar** (lettre de la section 9) | fondée ; procédure à relire |
| 3 COMPOSITION | « proposer avec recommandation », défaut sous 48 heures | fondée |
| 4 H-04 | **vraie décision** : changer de modèle ou faire entrer un fournisseur tiers demande un GO | fondée ; à étendre à H-03 |
| 5 Notation par l'oracle | **tranché** par l'invariant (brief § 6) : c'est la seule lecture conforme | Lazar prend acte |
| 6 Critère du duel | **vraie décision** : il modifie la métrique d'une dépense déjà accordée (GO-2026-10-28-01) | fondée |
| 7 Banque distincte | **tranché** : réponse de conv-audit, brief § 6, N-054 | à fermer |
| 8 INVARIANCE | Lazar (le langage, donc les revendications) | **prématurée** : pour INVARIANCE, un δ plus grand affaiblit la loi. L'incitation et l'orientation de l'empreinte s'inversent, et il faut un δ_max et une monotonie inversée dans E-10. |
| 9 Isolation des systèmes publiés | défaut sous 48 heures | fondée |
| 10 Plafond C_max | **Lazar** (porte, revue externe) | « petit » manque de contenu, mais acceptable |
| 11 Règle d'arrêt | technique, mais elle fixe ce que certifie un statut, donc la course | **à requalifier** : sans lecture jusqu'au budget, la troisième issue est vide (A1) |
| 12 Branche et fusion | **Lazar** (dépôt distant) | fondée |
| 13 Qui est « l'utilisateur » | **question de fait**, pas une décision | — |

La section 0 (l. 134-138) annonce onze nœuds ; la section 10.2 en a treize.

## G. Fidélité au brief

**Ce qui est conforme.**
- Les quatre parties du livrable sont présentes, les sept attaques minimales aussi.
- Le gel de la boucle est en P-8.
- Le test final n'est lu qu'une fois.
- Le principe « bon marché d'abord » est tenu.
- Les chiffres 89 et 33 sont exacts.

**Écarts déclarés** : la poussée et la demande de fusion en brouillon (écart à « tu ne pousses rien ») ; le vérificateur rendu mécanique ; le schéma B ; les témoins silencieux. Ils sont fondés et soumis à Lazar.

**Écarts non déclarés** :
- le rapport 2 n'est ni traité, ni cité ;
- la quarantaine de N-053 est absente ;
- la section 0 et la section 10.2 ne donnent pas le même nombre de nœuds.

## H. Classement

**Bloquant**
1. L'affirmation « un espace plus large exclut plus de mondes » est fausse ; la relation de restriction n'est pas définie ; C-09 et la ligne « renforcement » reposent dessus. C'est bloquant avant le codage de la mémoire (A2).
2. Famille H : H-04, et H-03 désormais, sont insatisfiables sous le montage actuel. C'est bloquant pour toute course avec le proposeur maison, jusqu'à la décision de Lazar et une lecture de la famille H par un autre fournisseur (A3).

**Majeur**
3. κ = 0 est admis, ce qui rouvre le bloquant de la v1 : il faut un κ_min (A1).
4. `AMPLITUDE_REFUTEE` est inatteignable sous la règle d'arrêt par défaut ; l'artefact de D-06 est faux et provoquerait de fausses percées (A1).
5. Le décalage des nuls de permutation à κδ n'est pas construit ; c'est à relire par un statisticien (A1).
6. Le rejet d'AM-A-01, point 2, est faux sous D-19 : l'archive dépend des espaces gelés (B).
7. La quarantaine de N-053 est absente (E).
8. Les points A1, A5, A7 et A8 du rapport 2 ne sont pas traités, et H-01 et H-02 restent molles (C).
9. AM-O-06 : le mode tenu à l'écart n'est pas nommé, la disjonction par empreintes n'a pas d'artefact, le réassort n'est pas interdit (D).
10. Les exceptions de G-05 et de G-02 sont des replis (C).

**Mineur**
11. Le rejet de CL-A-11 est mal prouvé ; verser les non-lues au développement serait une voie médiane (B).
12. La recommandation INVARIANCE est prématurée (F).
13. Onze nœuds annoncés pour treize présents ; renvoi « (G-02) » erroné.
14. F-07 : « la treizième » fiche, selon quel ordre ? Il vaut mieux contrôler le budget α_P au gel et rembourser les fiches refusées avant le jugement.
15. L'oracle « à κδ près » est ambigu : juge-t-il l'affirmation déclarée ou l'affirmation certifiée ?
16. Résidu d'incitation : la récompense d'héritage et l'ensemencement ne dépendent que de `CONFIRMEE`, ce qui pousse vers δ_min. Pas de fausse promotion, mais un contenu faible.

**Conclusion : adoptable après corrections.** Liste minimale pour une v3 :
1. Retirer la monotonie en espace ; définir la restriction ; écrire la composition de la grille de mondes ; ajouter un artefact de jumelle tardive sur des mondes hétérogènes.
2. Fixer κ_min > 0 ; rendre obligatoire la poursuite de la réfutation jusqu'au budget, ou retirer la troisième issue ; réécrire l'artefact de D-06 ; marquer le décalage des nuls de permutation pour le statisticien.
3. Inscrire la réponse de conv-audit sur AM-O-06 ; ajouter le mode tenu à l'écart ; étendre A-02 avec la disjonction par empreintes, `FAMILLE_RESERVEE` et l'interdiction du réassort.
4. Ajouter la quarantaine de N-053 (acteur, interdiction, test d'architecture).
5. Traiter le rapport 2, famille H (A1, A5, A7, A8) ; étendre le nœud 4 à H-03.
6. Corriger les preuves des rejets d'AM-A-01, point 2, et de CL-A-11 ; corriger la composition de l'archive.
7. Faire bloquer les exceptions de G-05 et de G-02 ; mettre la section 0 et la section 10.2 d'accord ; corriger le renvoi « (G-02) ».

## Ce que je n'ai pas pu vérifier

- La constructibilité des processus non paramétriques par forme.
- L'atteignabilité réelle d'`AMPLITUDE_REFUTEE` avec des paris adaptatifs : mon modèle utilise une alternative fixe.
- Si le rapport 2 a été transmis à l'auteur.
- Les fichiers hors liste.
