# Décision — N-077 : la marge asymétrique (H6) sort des hypothèses revendiquées du papier A ; sa mesure reste, descriptive, avec une lecture fixée d'avance (v1)

- **Décision de Lazar** : GO-2026-11-21-64 (`registres/go.md`, l. 663, type « décision »), mots de Lazar dans la session mère, 21 novembre 2026 vers 16:15 UTC. Texte de la ligne pour ce point : « Marge asymétrique (H6) : retrait des hypothèses revendiquées accordé, mesure gardée, après correction de la note. » Extrait que la ligne donne pour ce point : « go; c'etait quoi deja la marge asymetrique ? ». Le rattachement de chaque extrait à chaque point de la ligne est la lecture de la mère.
- **Auteur et heure** : Claude Fable 5.2 (`claude-fable-5-2`), concepteur (R-3735), sur mandat de la session mère ; 21 novembre 2026, de 16:23 à 16:25 UTC (`date -u`). Dépôt à `ee2ba480d`. Ni commit, ni poussée, ni appel payant, ni recherche en ligne. Je ne modifie ni `CLAUDE.md`, ni le programme, ni les registres : la ligne pour `CLAUDE.md` est dans `ligne-claude-md-N-077-v1.md`, la mère l'inscrit.
- **Numéro** : N-077, le premier libre après N-076 (aucun N-077 dans `docs/decisions/`, `CLAUDE.md`, `registres/` ni `docs/notes/`, par recherche de motifs ce jour).
- **Nœud posé par** : la note du protocole X sur la marge asymétrique, décision D-1, option (a) (`docs/notes/protocole-x-marge-asymetrique-v1/reponse-fable-marge-asymetrique-v2.md`, `6c7e1c2f…050d`, § 4 et « Décisions pour toi »). Chaîne : GO-2026-11-21-54 laisse ouverte la D-2 de la note sur l'attaquant informé (« H6 resserrée ») ; GO-2026-11-21-57 l'envoie au protocole X ; GO-2026-11-21-61 lance ce protocole ; GO-2026-11-21-64 tranche.
- **La condition « après correction de la note » est remplie** : la v1 de la note a été contre-lue par un Opus 5.5 neuf (« à corriger », un constat bloquant sur la raison du retrait) ; la v2 porte les seize constats ; le même contre-lecteur l'a vérifiée, verdict « Conforme », bloquant levé (`verification-corrections-marge-asymetrique-v2-opus-v1.md`, `6edb4acb…`, même dossier). Deux remarques mineures restent, qui ne touchent pas le retrait (section 7).
- **Statut** : v1, scellée, **non contre-lue**. Elle touche une revendication : je recommande une vérification courte par le contre-lecteur de la note avant l'inscription à `CLAUDE.md` ; la mère en décide.
- **Lu**, empreintes égales aux compagnons : la note v2 et sa vérification ; le programme (`2fd63bad…`, l. 45, 97, 188, 190) ; N-013 (`157d388e…`, § 6) ; N-015 (`462785b3…`) ; N-070 (`7c4ce221…`), modèle de forme ; N-053 (`2204256d…`, point 5), N-054 (`c8a00b3f…`, point 5) et N-076 (`49b664c1…`, l. 130 et 233), par motifs ; le brief (`9261932a…`, tâche T1.6 et porte G1) ; le préenregistrement des sondes (`d7d180ec…`, l. 2824 et 2938) et celui des organismes (l. 375 à 384), par motifs ; la note sur l'attaquant informé (`c23a1034…`, question 5 et D-2), par motifs ; `registres/go.md`, l. 653, 656 et 663. Rien d'ouvert sous un dossier cloisonné ; aucun résultat d'expérience lu.

## 0. En clair

La marge asymétrique était l'idée suivante : il existerait un réglage d'une intervention aveugle (reformuler ce que l'agent écrit, retirer sa réponse au sort plusieurs fois, vider sa mémoire) où le saboteur perd beaucoup et l'agent honnête perd peu. Le programme la portait comme une hypothèse du papier sur le temps.

Elle n'est plus revendiquée. Un saboteur qui connaît l'intervention et y répond au mieux ne perd rien. Et si nous mesurions quand même une marge sur nos saboteurs de laboratoire, elle dirait comment nous les avons fabriqués (un saboteur à consigne se contredit d'un tirage à l'autre), non ce que vaut la défense.

Nous faisons toujours la mesure. Elle est rapportée comme une description, avec ses attentes écrites d'avance, sans rien promettre.

## 1. Ce qui est retiré : les énoncés, recopiés

1. **Programme** (`docs/programme-controle-ia-v2.md`, `2fd63bad…`), section 5, l. 97 : « **H6 — marge asymétrique** (0,66). Il existe une intensité d'intervention non spécifique (paraphrase, ré-échantillonnage, remise à zéro de contexte, bruit d'activations) où le succès d'attaque chute significativement plus vite que l'utilité honnête. » Et l. 45, table des trois papiers, colonne « A — le temps » : « Hypothèses | H1, H2, L, T, H6, Tr, H8 ».
2. **N-013** (`decision-N-013-v1.md`, `157d388e…`), § 6, « H6 — marge asymétrique (papier A) » : « **Énoncé retenu** : pour l'une au moins des quatre interventions non spécifiques (paraphrase, ré-échantillonnage, remise à zéro du contexte, bruit d'activations), il existe une intensité où, **en moyenne à intensité fixe**, le succès du sabotage d'agent chute significativement plus vite que l'utilité honnête. »
3. **N-015** (`decision-N-015-v1.md`, `462785b3…`), § 1, l'énoncé en vigueur jusqu'à ce jour : « **Énoncé retenu** : pour l'une au moins des trois interventions non spécifiques (paraphrase, ré-échantillonnage, remise à zéro du contexte), il existe une intensité où, **en moyenne à intensité fixe**, le succès du sabotage d'agent chute significativement plus vite que l'utilité honnête. »

**À partir de cette décision** : la marge asymétrique (H6) n'est plus une hypothèse revendiquée du papier A. Aucune prédiction n'est revendiquée en son nom, aucune priorité n'est affirmée, et la probabilité d'originalité de 0,66 ne s'applique plus à rien. La liste des hypothèses revendiquées du papier A se lit : H1, H2, L, T, Tr, H8.

**Restent en vigueur**, de N-013 et de N-015 : le bruit sur les poids n'est pas revendiqué (Tice et al., arXiv 2412.01784) ; le bruit d'activations n'est pas revendiqué et reste mesuré comme une extension agentique de « Poser », cité comme antériorité, avec son retour possible par un nœud ; le risque de collision avec la feuille de route de Google DeepMind (arXiv 2607.13087), que la note v2 trouve réalisé pour l'idée : l'affaiblissement sélectif de l'attaquant y est publié comme une classe de parades, sans mesure (note v2, § 2, p. 18 et 29 de la pièce).

## 2. La raison

Elle tient en deux phrases, celles de la note v2 (§ 4, « La raison, corrigée » ; D-1) et de sa vérification.

1. **Contre un saboteur qui répond au mieux, aucune des trois interventions ne garde de marge sur le succès.** Ce que la note établit, et à quel degré :
   - rééchantillonnage, exécution d'un tirage au hasard : la loi de l'action exécutée ne change pas ; nul exact, pour toute politique (calcul C1 de la note) ;
   - rééchantillonnage, exécution par règle : le gain serait nul contre un attaquant parfaitement cohérent d'un tirage à l'autre, selon les auteurs mêmes (Lucassen et Kaufman, arXiv 2605.26047, p. 10, lu sur PDF par l'auteur de la note) ;
   - paraphrase de la sortie qui garde le contenu, et remise à zéro du contexte : nulles sur un sabotage porté par le contenu ou qui ne tient aucun fil, **par construction, non mesuré**.
2. **Une marge mesurée sur nos organismes lirait leur fabrication.** Un attaquant à modèle de langage n'est cohérent d'un tirage à l'autre qu'à 80 % environ (même page ; chiffre vérifié à la page par le contre-lecteur) ; un sous-rendement induit par consigne se contredit d'une paraphrase de la question à l'autre (Lin Yulong et al., actes de la conférence ICML 2026, p. 1 et 3). Une marge trouvée chez nous dirait donc l'incohérence de l'organisme, c'est-à-dire la façon dont nous l'avons induit, non une propriété de la défense.

**Bornes de cette raison, à garder avec elle.**
- La note ne dit **pas** que la marge est « prédite nulle sur nos organismes » : elle dit ne pas le savoir, et que pour l'organisme à consigne les sources penchent vers une marge positive. Le retrait ne dépend pas de l'inventaire de ce dont le sabotage de chaque organisme dépend.
- Les articles qui défont la marge publiée ne traitent que du rééchantillonnage. Pour la paraphrase et la remise à zéro, il n'y a que des arguments par construction.
- La seconde phrase est marquée « supposé » par son auteur : c'est le premier pas non justifié de la note v2 (relevé de méthode, pas 11). Qu'une marge mesurée sur un organisme construit dise sa fabrication plutôt qu'une limite de capacité qui vaudrait pour un saboteur réel n'est pas démontré. Ce qui le justifierait : le contraste entre nos deux modes d'induction, et la même mesure sur un attaquant qui n'est pas de notre fabrication.
- Confiance de l'auteur de la note dans sa recommandation : 0,6. Le même jour, il avait recommandé le contraire dans la note sur l'attaquant informé (garder H6, resserrée).
- Aucune mesure n'a été faite, aucun résultat lu : la raison est un argument, appuyé sur des pièces publiées et des calculs sur des mondes supposés.

## 3. Ce qui est gardé : la mesure, et sous quelle forme

L'expérience de la marge du papier A (E1.6 du programme, tâche T1.6 du brief) **reste au plan**. Elle devient une **mesure descriptive**, rapportée sous la ligne « description », sans hypothèse revendiquée, sans critère de réussite, sans priorité. Sa forme est l'option (a) de la D-1 de la note v2 (§ 4) :

1. **Ce qui est mesuré.** Le succès du sabotage et l'utilité honnête, sous chaque intervention et à chaque intensité : paraphrase (objet déclaré : ce que l'agent lit ou ce qu'il écrit ; contenu gardé ou non), rééchantillonnage (règle d'exécution et règle d'agrégation déclarées ; les deux règles de sélection de N-053, point 5, restent), remise à zéro du contexte. Le bruit d'activations reste mesuré selon N-015. Le tout rapporté par mode de sabotage (N-054, point 5).
2. **Des attentes écrites d'avance, qui ne sont pas des hypothèses du papier.** Des nuls là où ils sont exacts ou plantés : l'exécution au hasard, partout ; les trois interventions contre le saboteur cohérent d'un monde planté, puis du bras informé. Sur nos organismes, aucun signe attendu avant l'inventaire. Les seuils de la note (écart de succès dans ± 5 points pour un nul) sont indicatifs ; le préenregistrement les fixe.
3. **Une marge lue à utilité égale, contre une base nommée, sur une échelle déclarée.** La base n'est plus « Ctrl-Z » seul : il faut la décomposition entre l'information et l'exécution (Lucassen et Kaufman) et une base à utilité égale (note v2, § 4, dernier alinéa).
4. **Un contraste de validité** entre l'organisme à consigne cachée et l'organisme à adaptateur, avec un adaptateur bénin de même budget pour témoin de fragilité.
5. **Les quatre lectures rapportées** que demandait la D-2 de la note sur l'attaquant informé : le tirage secret de l'intervention ; le bras informé ; la trace par action chez le saboteur qui tient ; la marge par tour d'adaptation.
6. **Règle de lecture d'un résultat.** Une marge positive sur l'organisme à consigne se rapporte comme une lecture de sa fabrication (une consigne tenue en contexte), jamais comme une propriété de la défense ni comme une confirmation de H6.
7. **Retour possible**, par un nœud de Lazar seulement, et sur résultat : une revendication pourrait alors être proposée comme résultat, non comme prédiction (même règle que N-015 pour le bruit d'activations).

Comme pour toute mesure : préenregistrement scellé (R1), contre-lecture (R2), devis et GO de calcul. **Aucune dépense n'est ouverte par cette décision.** Le détail (intensités, seuils, échelle, base, nombre de cellules et correction pour plusieurs cellules) appartient au préenregistrement de cette expérience, non à cette note.

## 4. Ce que cela change aux autres pièces

| Pièce | Effet |
|---|---|
| Programme v2, § 5 (l. 97) et table des papiers (l. 45) | Non réécrit : il se lit avec cette décision. À reporter à la prochaine version : « papier A : une mesure descriptive de la marge sous interventions non spécifiques, sans hypothèse revendiquée (N-077) ». La thèse, la figure-titre et le calendrier du papier A ne reposent pas sur H6 et ne changent pas |
| Programme v2, § 10, E1.6 (l. 188) ; brief v2, T1.6 | La tâche reste. « Marge asymétrique (H6). Base : Ctrl-Z » se lit : mesure descriptive, base selon la section 3, point 3. « Métrique de marge fixée au préenregistrement » reste vrai |
| Porte G0 | Rien : aucune tâche de la phase 0 ne dépend de H6 (N-015, § 2) |
| Porte G1 | Rien : H6 n'entre pas dans son critère, qui oppose la boîte blanche séquentielle aux bases (programme, l. 190 ; brief, « Porte G1 » ; N-008 et N-056 selon la liste de `CLAUDE.md`, non rouverts) ; aucune mention de H6 dans `prereg/formulation-g1-simulation-v1.md` (recherche de motifs). Portes GC et G2 : rien |
| N-013, § 6 ; N-015, § 1 | Leur « énoncé retenu » de H6 n'est plus en vigueur ; le reste tient (section 1) |
| N-053, point 5 | Les deux règles de sélection déclarées restent dans la mesure |
| N-054, point 5, et sa liste « textes à modifier » | « H6 s'écrit par mode » se lit : la mesure est rapportée par mode. Pour H6, la modification du § 5 à la prochaine version est le retrait |
| N-076, l. 130 et 233 | « Les interventions revendiquées par la marge asymétrique » et « celles de la marge asymétrique » se lisent : celles de la mesure de la marge. Rien d'autre |
| Préenregistrement des sondes (T0.7), l. 2824 et 2938 | Texte scellé inchangé, aucun écart : le bras qu'il décrit n'était pas une intervention de H6, et l'arrêt « toute présentation de ce bras comme une intervention de H6 » reste, à plus forte raison |
| Préenregistrement des organismes (T0.6), l. 375 à 384 | Sans rapport : « H6-1 » à « H6-4 » y sont les prédictions numérotées de ce texte sur l'organisme à adaptateur, non la marge asymétrique. Rien ne change |
| Plan d'épreuve de la note v2 (§ 5 : quatorze mondes, dix-huit témoins, trois motifs de mort) | Ni lancé ni annulé ici : il reste suspendu à sa décision D-3. Le retrait ne lui ôte pas son objet : il tue d'avance les règles qui annoncent une marge et les lectures qui en voient une, ce dont la mesure gardée a besoin pour sa règle de lecture (section 3, point 3) |
| L'hypothèse candidate de la marge qui survit au protocole connu (H10) | Non inscrite, non touchée : ses quatre retouches sont la D-2 de la note v2, ouverte |

**Ne pas écrire**, dans un texte interne ou un papier :
- « il existe une intensité où le succès du sabotage chute plus vite que l'utilité honnête », comme hypothèse ou prédiction du programme ;
- qu'une marge mesurée sur nos organismes est une marge de la défense ;
- que la marge est « prédite nulle sur nos organismes » : ce n'est pas su ;
- que la marge est défaite par la littérature pour les trois interventions : elle ne l'est que pour le rééchantillonnage ;
- que le rééchantillonnage ne sert à rien : son gain d'information est publié, et il tient lui-même à des suppositions (section 7, remarque 1).

## 5. Ce que cette décision ferme

- **La D-2 de la note sur l'attaquant informé** (`docs/notes/attaquant-informe-v1/reponse-fable-attaquant-informe-v1.md`, `c23a1034…`, l. 262), laissée à Lazar par GO-2026-11-21-54 (« Restent à Lazar : D-1 …, D-2 (H6 resserrée), D-3 … »). Elle est tranchée contre sa recommandation : son option (a), garder H6 resserrée à son échelon, n'est pas retenue ; son option (b), la « taxe de robustesse » en seconde branche revendiquée, non plus ; ses quatre lectures rapportées passent dans la mesure gardée (section 3, point 5). Les propositions 5.1 et 5.2 de cette note ne portent plus sur une hypothèse revendiquée.
- **La D-1 de la note du protocole X sur la marge asymétrique**, option (a). Les deux décisions formaient un seul nœud, tranché d'un seul mot.

À consigner par la mère : la fermeture des deux, au registre des accords et à l'état.

## 6. Ce qui reste ouvert

Rien de ce qui suit n'est tranché par GO-2026-11-21-64, qui ne porte, pour cette note, que le retrait et la garde de la mesure.

| Point de la note v2 | Objet | Statut selon la note |
|---|---|---|
| H6′, « la taxe de cohérence » (§ 4 ; option (c) de D-1) | Énoncé candidat : ce que coûte au saboteur de tenir sous le mélange, et en quelle monnaie | **Non inscrit.** À reproposer seulement après les étapes 0 à 2 du plan et la lecture de D-5 ; nœud |
| D-2 | Quatre retouches à l'hypothèse candidate de la marge qui survit au protocole connu (H10), si elle est inscrite | Nœud, sans défaut |
| D-3 | Étape 0 du plan d'épreuve, sans dépense | Défaut sous 48 heures selon la note ; l'étape 1 est une dépense, nœud |
| D-4 | L'inventaire de ce dont le sabotage de chaque organisme dépend, sur textes ; puis trois mesures sur devis | Défaut sous 48 heures pour l'inventaire seul. Il fixe les attentes de la mesure gardée (section 3, point 2), non le retrait |
| D-5 | Lecture en entier de six voisins avant toute phrase de revendication | Défaut sous 48 heures |

Le départ et le décompte des délais de 48 heures reviennent à la mère, ainsi que leur accord avec la limite de trois chantiers actifs.

## 7. Points attachés

- **Deux remarques mineures de la vérification**, à porter par erratum de la note v2 ou à laisser ; aucune ne touche le retrait. (1) Verdict 4 : « une seule tient » est à borner par « tant que l'attaquant ne choisit ni la ressemblance de ses scores ni ne distingue la réplique ». (2) § 3, table : « de −0,045 à −0,19 » réunit deux suppositions distinctes. Cette décision n'emploie aucun de ces deux chiffres.
- **Reviennent à la mère** : la garde de motifs du collisionneur et la relecture de cloisonnement pour le couple neutre v2 et la sous-question v2 de l'organisme ; le couple v1 et la sous-question v1 ne doivent plus être servis ; l'erratum d'une ligne dû à la lecture en entier d'Opus (pages de Terekhov et al.).
- **Chiffres** : cette décision ne reprend de l'état de l'art qu'un chiffre, la cohérence à 80 % environ, lu sur PDF empreinté par l'auteur de la note et vérifié à la page par le contre-lecteur (R7) ; « ± 5 points » est un seuil proposé par la note, non un chiffre publié. Table de provenance : `docs/sources/pdf/protocole-x-marge-asymetrique-v1/provenance-protocole-x-marge-asymetrique-v1.md`. Aucun n'entre dans un préenregistrement par cette note.
- **Ce que je n'ai pas fait** : aucune contre-lecture de cette pièce ; aucune relecture des PDF ; N-053, N-054, N-076, le brief, le préenregistrement des sondes et la note sur l'attaquant informé lus par motifs seulement, autour des mentions de H6 ; H6 cherchée par motifs dans `prereg/*.md` seulement (deux textes, table de la section 4) ; non cherchée dans les archives de contre-lecture, les notes en cours ni les textes des papiers, que la mère fera passer à la même recherche.
