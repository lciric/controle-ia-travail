# Note de piste — réponse Q2 à Lujain Ibrahim — v1

Rédacteur neuf : je n'ai écrit aucune version antérieure des réponses de Lazar. 3 novembre 2026, de 12:23 à 12:50 UTC environ (`date -u`). Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/redaction-finale-ibrahim-q2-v1.md`, sha256 `8d35c9f6ab44b0718d1654101f5f0c5313ba9e1221dbeedd1ddafea59eb32da5`, vérifiée avant lecture (égale à son compagnon).

**Question** (`brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt`, sha256 `57393598…`, ligne 148) : « Describe a technical project where you trained or evaluated LLMs (feel free to link to code or any public documentation/write up if you have something to share). » Limite : aucune écrite ; 300 mots au plus, règle de Lazar.

**Ce que la question demande en clair** : un projet ; ce qui a été entraîné ou évalué ; ce qui a été trouvé ; un lien. Lazar a évalué, il n'a pas entraîné.

## 1. Pistes candidates

1. **Une mesure qui sépare « jusqu'où » de « vers où ».** La loi d'attraction comme instrument : elle sépare le gain g de la destination ĉ, qu'un décalage moyen confond. Preuves publiques : l'éloge fait baisser les notes déjà hautes, au-delà de la régression vers la moyenne ; sans paramètre réajusté, la loi prédit 60 items neufs (R² 0,68 et 0,58, contre −0,28 et −0,01 pour un décalage constant) ; Qwen et Mistral baissent autant que Llama en moyenne sous critique, mais uniformément (R3) ; sous critique, la formulation déplace la destination et laisse le gain plat (R6, prédiction préenregistrée qui a échoué, publiée comme telle). Forte pour elle : ses travaux portent sur la forme du comportement qu'une seule étiquette ou une seule mesure confond (taxonomie qu'elle co-signe) et sur la validité du juge (revue sur la validité de construit, juge de son papier sur la chaleur validé sur des annotations humaines). Distinctive : personne d'autre n'a cette loi. Vérifiable par elle sur un seul dépôt public. Défendable par Lazar seul : c'est son projet, et chaque nombre est dans son dépôt.
2. **Le juge est l'instrument.** Deux juges Qwen d'une autre famille retrouvent la loi ; la note du modèle lui-même dépend de l'implémentation (R2) ; des juges Qwen s'en remettent à un verdict planté dans le texte qu'ils lisent (R7) ; lecteurs humains préenregistrés (R5) ; refus notés au milieu. Forte pour sa revue sur la validité de construit, mais éparpillée, et R7 mesure un autre objet (le moniteur), pas la loi.
3. **Lire n'est pas piloter** (dépôt `sycophancy-construct-validity`, commit `146b2a4`). Une direction lit la sycophancie (ρ = 0,684, peut-être un ajustement d'entraînement) sans la piloter ; la baisse obtenue par ablation de rang 3 venait de réponses stockées tronquées à 300 caractères ; la greffe transporte surtout « sans pression », pas le contenu de l'item (65 %, 44 %, 2 %). Touche ses sondes d'hypothèses verbalisées (2604.03058), mais par un contraste risqué (construits différents : sycophancie d'opinion contre sycophancie sociale), sur des preuves plus faibles (interventions de rang 1 sans nombres conservés, intervalles larges, bras ajouté après coup) ; et c'est un autre projet.
4. **Des prédictions écrites d'avance, y compris celles qui échouent** : R4 tient ; R6 et R7 échouent (issue C), publiés comme tels. Fort pour la rigueur, mais générique et sans lien propre à ses travaux.
5. **Une empreinte pour le post-entraînement** : R8 (étapes publiques Tülu 3 du même modèle de base, lancé le 3 novembre à 08:01 UTC selon `STATUS.md`). Pont direct vers sa Direction 1, mais aucun résultat, et c'est la matière de la Q1 : écartée par la consigne de coordination.

## 2. Choix : piste 1

Avec, de la piste 2, ce qui valide la loi elle-même (juges Qwen, lecteurs humains, refus) et, de la piste 4, l'échec publié de R6.
1. Elle répond en clair à la question : un projet, ce qui a été évalué, ce qui a été trouvé, le lien.
2. Elle touche ses deux préoccupations (forme du comportement, validité du juge) sans citer ses papiers, donc sans risque de mal les nommer.
3. Chaque phrase se vérifie sur un seul dépôt public (`lciric/sycophancy-psychophysical-law`, commit `b3ecaec`) : 20 affirmations publiques et vérifiées, une lecture, rien d'interne.
4. Elle porte son propre test sévère (aucun paramètre réajusté sur 60 items écrits à l'aveugle) et son propre échec publié.
5. Elle laisse à la Q1 tout le pont vers l'entraînement de caractère et l'apprentissage par renforcement : ni R8, ni Open Character Training, ni ses papiers.

## 3. Forme dictée par la piste

Ordre : le dispositif (ce qui est demandé au modèle, la phrase de pression citée, le juge) ; la loi et ce qu'elle prédit qu'un décalage ne prédit pas ; la séparation gain / destination et ses deux preuves (autres familles ; formulations, avec l'échec) ; ce qui pourrait fabriquer la loi (juges, humains, refus) ; la discipline (préenregistrement, recalcul indépendant, code écrit par des agents). Prose, phrases courtes, aucun titre ni liste. Un seul lien : la racine du dépôt (voir 6, point 6).

## 4. Relecture comme la mentore : ce qu'elle contredirait, et la correction faite

1. Premier jet : « Pressure does not push the rating toward the user. » Faux en moyenne (sous critique, les notes baissent). Remplacé par la loi en fraction fixe, et par la comparaison au décalage constant (R4 : −0,28 et −0,01).
2. Premier jet : « A flip rate cannot see this. » Elle répondrait qu'un taux d'accord n'est pas fait pour compter un mouvement qui s'éloigne de l'utilisateur. Remplacé par « A mean shift cannot separate how far (g) from where (ĉ) », énoncé sur une statistique et deux paramètres, appuyé par R3 et R4.
3. « So praise lowers ratings above 2.9 » appelle aussitôt l'objection de la régression vers la moyenne : ajout de « beyond regression to the mean » (troisième rival du README : c'est l'ampleur, −0,67 contre −0,07, qui l'exclut, pas le compte des descentes).
4. Premier jet : « my preregistered prediction that the gain grows failed ». Faux sous éloge, où le gain a crû (0,276 → 0,797). Remplacé par la prédiction entière (le gain croît et la destination ne bouge pas, issue A de l'addendum) et par ce qui a été observé dans chaque bras.
5. « No human has rated yet » : peut devenir faux si le pilote à lecteurs connus a commencé. Remplacé par « preregistered but not yet run », vrai pour R5.
6. « removing them » : les deux sensibilités retirent des items entiers. Remplacé par « dropping the items with refusals ».
7. « Each follow-up was … recomputed » : R8 tourne et R9 n'a pas couru. Remplacé par « Each published follow-up ».
8. Écarté : présenter R3 comme « un cas mesuré de fragmentation du construit » au sens de sa taxonomie. Chez elle, la fragmentation désigne des études qui mettent une même étiquette sur des comportements de forme différente ; R3 parle de modèles, et elle pourrait contester l'emprunt. La phrase sur le décalage moyen dit la même chose sans le mot.
9. Gardé, à savoir s'il est demandé : « The reversal held there too » vaut pour la cible réajustée sur les 60 items (3,225), pas pour celle de la campagne 1 (registre, n° 9).

## 5. Projet compagnon : phrase prête, non mise

41 mots, vérifiés sur `sycophancy-construct-validity`, README au commit `146b2a4` (sha256 `de5d6032d42cc2eb893e2d1339ae0c6423c4cebc2e1b7ecc83d35cf9c3154da8`, l. 3, 19, 25, 27, 28) :

> In an earlier project (https://github.com/lciric/sycophancy-construct-validity), a rank-3 ablation that cut the judged sycophancy rate from 61% to 46.5% did not replicate: it softened every negative verdict, and the judge, shown responses stored truncated at 300 characters, read that as holding position.

Pour elle, c'est la leçon de validité la plus nette de Lazar (ce que le juge a lu a fabriqué l'effet), mais c'est un autre projet. Pour la placer, il faut retirer environ 41 mots : par exemple les deux phrases sur les refus (37 mots) et « The reversal held there too. » (5 mots). Je ne le recommande pas : les refus touchent un choix de son propre papier (refus exclus) et appartiennent au même projet. Aucun nombre de l'essai D36 original, ni « < 1 % », ni « 68 % », ne doit revenir.

## 6. À confirmer par Lazar

1. **Organisme d'idéation retiré** (sans lien avec ses travaux) ; environ 12 mots pour le remettre en dernière phrase.
2. **« AI coding agents wrote the code. »** : gardé de sa réponse, sous une forme vérifiable (37 commits sur 38 signés par Claude) ; « following guidelines I created » retiré, non vérifiable sur ce dépôt.
3. **Pilote R5 à lecteurs connus** : déclaré le 2 novembre, état non publié. S'il a commencé, la phrase reste vraie pour R5 ; il peut vouloir le dire.
4. **R8** a démarré le 3 novembre à 08:01 UTC (`STATUS.md`) : la Q2 n'en parle pas (coordination avec la Q1), même si ses résultats arrivent avant 23:00 UTC.
5. **Symboles** p₀, ĉ, Δ, ≈, ·, −, R² : vérifier que le formulaire les affiche ; sinon « p0 », « c », « ~ », « - », « R^2 » (même compte de mots).
6. **Lien non épinglé** : la racine du dépôt montre l'état courant (et R8 quand il sera publié) ; les nombres sont ceux du commit `b3ecaec`. Pour épingler : `https://github.com/lciric/sycophancy-psychophysical-law/tree/b3ecaec`.
7. **« about as much as Llama »** : −0,69 et −0,68 contre −0,76 (campagne 1) ou −0,86 (R6, dose standard), sur des jeux d'items voisins mais non identiques (registre, n° 11).
8. La lectrice indépendante annonce une correction datée de `results/R6/README.md` (l. 43 et 62) : sans effet ici, la réponse n'emploie ni « middle of the scale » ni « 2.04 ».

## 7. Fichiers

- Réponse : `brouillons/redaction-finale-v1/ibrahim-q2/reponse-v1.md` (293 mots par `wc -w`, 297 par découpage sur les espaces).
- Registre : `brouillons/redaction-finale-v1/ibrahim-q2/registre-affirmations-v1.md`.
- Cette note.
Aucun commit, aucun `.sha256`, aucun fichier existant modifié, rien lu sous `donnees/`, aucun `git fetch`, aucun appel de modèle, aucun code des dépôts publics exécuté ; `nice -n 10` sur les scripts et recherches.
