# Quel modèle servir comme expérimentateur d'épreuve dans l'étage des tests de mort (nœud N4) — avis du contre-lecteur et des modèles externes — v1

- **Par** : Claude Fable 5.2 (`claude-fable-5-2`), contre-lecteur neuf, effort normal, sous GO-2026-11-21-43. Écrit le 21 novembre 2026, de 11:10Z à 11:35Z environ. Pièce de travail (classe C), non contre-lue. Ni commit ni poussée.
- **Incomplète : l'avis d'Astra manque.** L'appel à `gpt-6.2-astra` est rendu « failed » par le fournisseur après 21,8 secondes, sans jeton compté et sans motif dans la trace. Je me suis arrêté là, selon le mandat : aucune relance. La recommandation ci-dessous repose sur deux voix (Fable 5.2, Carbon), non sur trois.
- **Dépense** : 0,3241 USD (Carbon, au prix du script, 4 et 20 USD par million de jetons) ; Astra, 0 jeton rapporté, 0 USD compté (une facturation côté fournisseur n'est pas exclue, elle n'est pas visible d'ici). Total 0,32 USD sur 8.
- **Non ouvert** : aucune carte, aucun résultat d'expérience, aucune des branches et aucun des dossiers interdits par le mandat. Aucun refus de classifieur.

## 1. Verdict

1. **Je ne suis pas l'arbitre : je recommande Sonnet 5.5, non Opus 5.5.** Opus 5.5 passe la garde 9, mais casse deux règles que la note de conception pose et que l'arbitre n'a pas confrontées : il a écrit une part des cartes à éprouver, et il écrit le code des bancs et relit les conceptions.
2. **La garde 9 est vérifiée, et la condition laissée ouverte par l'arbitre est levée** : le lecteur témoin de la seule course réelle était `gemini-4-argon`. Tant qu'il reste chez Google, la garde 9 laisse passer tout modèle Claude ou GPT et refuse Argon et Carbon.
3. **Carbon arrive, par sa propre voie, au même modèle** (Sonnet 5.5, confiance 0,78), et ajoute trois failles et deux contraintes qu'il juge mal réglées (§ 4).

## 2. Ce que disent les pièces

| n° | fait | pièce |
|---|---|---|
| F1 | Garde 9 : l'expérimentateur et le vérificateur (le lecteur témoin) ont chacun une famille déclarée ; famille vide ou égale : refus `FamillesNonSeparees`, avant toute session. Elle est appelée à l'entrée de l'étage. | `docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator/pole/tour_ferme_v64.py` (`35a8294e…`), l. 692 à 695 et l. 1076 à 1077 |
| F2 | Le lecteur témoin de la course réelle v67 : relais Argon, 16 appels, dont 14 de vérificateur ; un seul modèle, `gemini-4-argon`. Il est gardé, ne pèse sur aucune issue, et doit être d'une autre lignée que l'expérimentateur. | `registres/depenses.md` (`ee8c045d…`), l. 430 ; erratum 1 de la note (`0198f5f8…`), § 2 |
| F3 | « Un modèle n'éprouve jamais une proposition qu'il a écrite. » | note de conception (`4f3ae86f…`), l. 93 |
| F4 | Espèces qui proposent, à la configuration scellée de la course v9 : `claude-opus-5-5`, `claude-fable-5-1`, `gemini-4-argon` ; Kimi, Astra et Carbon en option, « défaut : absentes ». Opus 5.5 et Argon y sont aussi juges. | branche `origin/lot/compte-organisme-v1` à `773ef79de`, `docs/notes/organisme-auto-conception-v1/course-v4/configuration-course-auto-conception-v5.json` (`3f662ee8…`), l. 122 à 175, 182 à 230, 264 |
| F5 | « Conception par Fable, code par Opus, vérification par un autre modèle » pour les lots du branchement (bancs, mécanismes témoins, porte). « Personne dans l'organisme n'écrit le critère de mort » ; l'expérimentateur implémente. | note de conception, l. 147 et l. 13 |
| F6 | Deux traducteurs de deux lignées, dont aucun n'est l'expérimentateur ; les mondes écrits par une autre lignée que l'expérimentateur et les deux traducteurs ; à trois lignées, un traducteur est de la lignée de l'expérimentateur et l'auteur des mondes de la troisième. | même branche, `docs/notes/ideation-seuil-moniteurs-v1/conception-v4/ordre-course-seuil-et-moniteurs-v4.md` (`390af604…`), l. 94 et l. 188 |
| F7 | L'auteur des mondes est prévu au deuxième relais (Google) : « si l'expérimentateur était du deuxième relais, l'auteur des mondes ne pourrait pas en être ». | même branche, `docs/notes/ideation-seuil-moniteurs-v1/mandat-mondes-plantes-v3/erratum-mandat-1-v1/devis-auteur-mondes-plantes-v8.md` (`53b6b99f…`), § 6, point 6 |
| F8 | Un second modèle GPT, `gpt-6.2-sol`, a été nommé puis remplacé : son identifiant n'est pas établi comme figé. | `registres/go.md`, GO-2026-11-20-48 et GO-2026-11-20-58 |
| F9 | Coût relevé : 0,081 USD par test pour l'expérimentateur à la v67 (un script de loi, deux tours, un autre modèle) ; fourchette d'un greffon, lecteur témoin compris, de 0,14 à 4,10 USD, non mesurée. | note de conception, l. 33 ; erratum 1, § 2 (a) |

**Sur l'arbitrage** (`docs/notes/arbitrages-points-delicats-v1/arbitrage-fable-six-points-delicats-v1.md`, `44d1e86f…`, point 2) :
- « Non tranchable par moi » tient : nommer ce modèle est un changement de modèle.
- Sa condition (« la famille du lecteur témoin ») : levée par F2, sous réserve que la mère garde un lecteur de Google aux courses à venir.
- Son avantage dit d'Opus 5.5, « ce n'est pas le modèle qui a conçu les épreuves », est exact et incomplet : Opus 5.5 code les bancs et les témoins écrits par programme (F5) et a écrit une part des cartes (F4). L'arbitre ne cite ni la l. 93 ni la l. 147 de la note.
- Son objection à un modèle du troisième relais (« l'affectation scellée ne tient plus ») ne vaut que parce qu'un seul modèle GPT a un identifiant figé (F8) ; avec un second, l'affectation de F6 tiendrait.

## 3. Mon avis, candidat par candidat

**Coût, ordre de grandeur.** Deux scénarios à moi, « supposés », aucun n'est une mesure : *court*, 6 000 jetons d'entrée et 3 000 de sortie par greffon (deux tours, proche du relevé de la v67) ; *long*, 150 000 d'entrée et 40 000 de sortie (huit tours, contexte relu, réflexion comprise). Colonnes : par greffon ; pour 12 témoins ; pour 106 greffons (12 témoins et 94 cartes au plus). Le lecteur témoin s'ajoute partout : de 0,061 à 0,10 USD par greffon, soit de 6,5 à 10,6 USD pour 106.

| candidat | prix (entrée, sortie) | par greffon, court à long | 12 témoins | 106 greffons |
|---|---|---|---|---|
| Sonnet 5.5 | 2 et 10 | 0,04 à 0,70 | 0,5 à 8,4 | 4,5 à 74 |
| Opus 5.5 | 4 et 20 | 0,08 à 1,40 | 1,0 à 16,8 | 8,9 à 148 |
| Carbon | 4 et 20 (prix du script de consultation) | 0,08 à 1,40 | 1,0 à 16,8 | 8,9 à 148 |
| Fable 5.2 | 8 et 40 | 0,17 à 2,80 | 2,0 à 33,6 | 17,8 à 297 |
| Astra, Argon | 10 et 50 (prix haut du script ; Astra compté à 8 et 40 dans un devis du bras A) | 0,21 à 3,50 | 2,5 à 42 | 22 à 371 |

**Opus 5.5.**
- *Lignée et relais* : passe la garde 9 (F1, F2). Casse F3 sur la course principale : il a écrit une part des cartes (F4). Les identifiants opaques n'y changent rien, la règle vise le modèle. Tient trois autres rôles : il code les bancs (F5), relit les conceptions, juge dans l'organisme.
- *Fiabilité* : très bon en code. Mais c'est le même modèle qui écrit le banc et qui écrirait le greffon : une lecture fautive de l'interface, commune aux deux, ne se verrait que si les témoins la croisent. Risque de « réparer » une proposition bancale.

**Fable 5.2.**
- *Lignée et relais* : passe la garde 9. Casse la séparation que la note pose comme première règle (F5) : il a conçu l'épreuve, les témoins et l'interface, il reconnaîtrait la forme de ses propres témoins. La règle « Qui conçoit » le réserve à la conception.
- *Fiabilité* : le plus fort, et le moins indépendant. Le plus cher des Claude ; au scénario long, il approche le plafond de 4 USD par item.

**Sonnet 5.5.**
- *Lignée et relais* : passe la garde 9. N'a écrit aucune carte (F4), n'a rien conçu ni codé de l'étage, ne juge rien. Laisse Opus 5.5 ou Fable 5.2 libre comme traducteur de la lignée Claude et un GPT comme second traducteur, l'auteur des mondes chez Google (F6, F7) : l'affectation scellée tient.
- *Fiabilité* : la tâche est bornée (une fonction sous interface fixe, bibliothèque standard) ; un modèle d'exécution y suffit sans doute, et suit plus à la lettre. Ce n'est pas mesuré : la mesure sur les témoins le dira. Limite : même lignée que les auteurs de cartes, le concepteur et le codeur des bancs ; des conventions implicites partagées restent possibles.
- *Ce que je n'ai pas vérifié* : que le premier relais sert `claude-sonnet-5-5` avec la clé en place.

**Un modèle externe.**
- *Argon* : refusé par la garde 9 tant qu'il est lecteur témoin (F2) ; auteur de cartes (F4) ; le plus cher.
- *Carbon* : même famille que le lecteur témoin, refusé par la garde 9 ; même lignée que l'auteur des mondes (F7). Possible seulement si le lecteur témoin et l'auteur des mondes quittent Google : deux textes à reprendre.
- *Astra* : passe la garde 9. Mais il faut alors un autre GPT comme traducteur, dont l'identifiant n'est pas figé (F8) ; peut-être auteur de cartes s'il a été déclaré (F4, non vérifié : je n'ouvre pas les cartes) ; le plus cher ; son appel a échoué aujourd'hui même chez le fournisseur.
- *Leur place* : la seconde implémentation sur un tirage (note, l. 121 et l. 245), qui demande justement une autre lignée.

**Ma recommandation.** Sonnet 5.5 sur le premier relais, expérimentateur des trois emplois ; plafond sur devis après la mesure sur les seuls témoins ; Opus 5.5 mesuré sur les mêmes témoins comme repli, la règle de bascule écrite avant la mesure ; seconde implémentation d'une autre lignée sur un tirage. **Confiance : 0,6.** Elle n'est pas plus haute parce que la fidélité de Sonnet 5.5 dans ce rôle n'est pas mesurée.

## 4. L'avis de Carbon (`gemini-4-carbon`, servi égal au demandé, fin « STOP »)

- **Recommandation** : Sonnet 5.5 sur toutes les propositions ; confiance 0,78 (0,98 sur « seul candidat recevable sous ces règles »). Traducteurs : Astra et Opus 5.5, ce dernier hors des propositions qu'il a écrites. Seconde implémentation sur 10 à 15 % : Astra, hors de ses propres propositions, par dérogation dite à « l'expérimentateur n'est pas un traducteur ».
- **Sa voie** : une déduction sur les lignées. L'auteur des mondes chez Google impose des traducteurs Anthropic et OpenAI ; OpenAI n'a qu'un modèle figé, qui devient traducteur ; Google est fermé par la garde 9 ; reste Anthropic, où seul Sonnet 5.5 n'a aucun rôle.
- **Consigne qu'il demande** : implémentation littérale des champs fermés ; aucune correction, normalisation ni cas particulier absents de la proposition ; un échec explicite plutôt qu'une réparation.
- **Ce qui le ferait changer** : un témoin faux qui « tient » après passage par Sonnet 5.5 (d'abord réduire à deux tours sans retour statistique, puis changer de modèle) ; deux témoins vrais sur douze « non exécutables » ou hors interface ; un second identifiant figé chez OpenAI (alors Astra) ; le lecteur témoin et l'auteur des mondes hors de Google (alors Carbon).
- **Trois failles qu'il nomme** : (i) un traducteur peut mettre en forme une proposition qu'il a lui-même écrite, et la corriger avant que l'expérimentateur la voie ; (ii) la séparation est de lignée face au lecteur témoin, de modèle seulement face aux auteurs et au concepteur : tout le côté Claude partage ses conventions ; (iii) huit tours sur des données de mise au point suffisent à voir qu'une règle dégénère, et poussent à la réparer.
- **Deux contraintes qu'il juge mal réglées** : la garde 9 protège un rôle qui ne pèse sur aucune issue, c'est au lecteur de changer de lignée ; la séparation de l'auteur des mondes et des traducteurs consomme les trois lignées pour peu de gain.
- **Réserve qu'il dit lui-même** : il est de la lignée Google, donc de celle de deux candidats, du lecteur témoin et de l'auteur des mondes ; ses jugements de comportement sont à confronter aux témoins.

## 5. L'avis d'Astra

Absent. Trace : `appel-astra-v1.json`, « fin : failed », 0 jeton, 21,8 secondes, réglage « xhigh » accepté (code 200, mis en file), puis échec. Le script ne garde pas le motif du fournisseur. Je n'ai pas relancé.

## 6. Ce qui converge, ce qui diverge

- **Converge** (Fable 5.2 et Carbon, contre l'arbitre) : Sonnet 5.5 ; Opus 5.5 et Fable 5.2 écartés pour leurs rôles déjà tenus ; Google fermé par la garde 9 et par l'auteur des mondes ; Astra tenu par l'absence d'un second GPT figé ; fidélité à lire sur les témoins avant tout engagement.
- **Diverge** : la confiance (0,6 chez moi, 0,78 chez lui) ; le repli (Opus 5.5 mesuré en second chez moi ; chez lui, moins de tours, puis un autre modèle) ; Carbon veut Astra en second implémenteur bien qu'il soit traducteur, je laisse ce choix au texte de la course.
- **Apports de Carbon que je reprends** : la règle F3 étendue aux traducteurs (faille i) ; la consigne de littéralité ; la mise au point bornée à la forme (faille iii). Ce sont des propositions pour le concepteur, non des décisions.
- **Ce que je ne reprends pas** : desserrer la garde 9 ou la séparation de l'auteur des mondes. Ce sont des textes scellés ; y toucher est un nœud de Lazar.
- **Réserve sur la convergence** : l'énoncé neutre a été écrit par moi après m'être fait un avis. Sa table des rôles est exacte, mais elle rend Sonnet 5.5 seul « sans rôle » : la convergence de Carbon vérifie ma déduction, elle n'en est pas une confirmation indépendante.

## 7. Recommandation à Lazar

- **Décision en une phrase.** Nommer Sonnet 5.5 (`claude-sonnet-5-5`), sur le premier relais, expérimentateur d'épreuve des trois emplois (course principale d'auto-conception, course « seuil et moniteurs », pilier mathématique), le lecteur témoin restant chez Google.
- **Enjeu.** Sans nom : ni mesure du coût d'un greffon, ni devis de la première ligne de la course principale, ni complément de valeurs de la course « seuil et moniteurs ».
- **Options.**
  - (a) Sonnet 5.5. Avantage : seul candidat sans rôle déjà tenu ; passe la garde 9 ; garde l'affectation scellée des lignées ; le moins cher (de 4,5 à 74 USD pour 106 greffons, supposé). Inconvénient : fidélité non mesurée ; modèle neuf dans le programme, service par le relais à vérifier.
  - (b) Opus 5.5, recommandation de l'arbitre. Avantage : déjà servi, très bon en code. Inconvénient : auteur d'une part des cartes, codeur des bancs, relecteur des conceptions ; la règle « un modèle n'éprouve jamais une proposition qu'il a écrite » demande alors une exception écrite, ou d'écarter ses cartes.
  - (c) Astra, hors lignée Claude. Avantage : aucune convention partagée avec le concepteur et le codeur. Inconvénient : il faut un second GPT figé pour traduire ; le plus cher ; l'appel a échoué aujourd'hui.
- **Recommandation.** (a), confiance 0,6. Plafond par devis après la mesure sur les seuls témoins ; Opus 5.5 mesuré sur les mêmes témoins comme repli, règle de bascule écrite avant ; seconde implémentation d'une autre lignée sur un tirage.
- **Défaut.** Aucun : changement de modèle.
- **À dire dans la même question** : l'avis d'Astra manque ; une relance demande ton mot.

**Ce qui me ferait changer.** Un témoin faux qui tient, ou deux témoins vrais sur douze hors interface, après passage par Sonnet 5.5 : alors (b), avec l'exception écrite. Que le relais ne serve pas Sonnet 5.5 : (b). Que Lazar lise F3 par lignée et non par modèle : aucun candidat ne passe pour la course principale, puisque les trois lignées ont proposé, et il faut alors écarter des cartes ou dire l'exception.

## Relevé de méthode

**Chaîne de raisonnement.**
1. La garde 9 refuse un expérimentateur de la famille du lecteur témoin (F1 ; lu sur le fichier, empreinte recalculée).
2. Le lecteur témoin relevé est de Google (F2 ; registre des dépenses, l. 430).
3. Donc Claude et GPT passent, Argon et Carbon non (pas 1 et 2 ; « supposé » : le lecteur reste chez Google aux courses à venir).
4. La note interdit à un modèle d'éprouver sa propre proposition (F3).
5. Opus 5.5 et Argon ont écrit des cartes ; Sonnet 5.5, Fable 5.2 et, par défaut, Carbon et Astra, non (F4 ; « supposé » pour Astra et Carbon : la pièce de départ, qui les déclare ou non, n'est pas lue).
6. Opus 5.5 code les bancs, Fable 5.2 les conçoit (F5).
7. L'affectation des traducteurs et de l'auteur des mondes tient avec un expérimentateur Claude, non avec un GPT tant qu'un seul GPT est figé (F6, F7, F8).
8. Donc Sonnet 5.5 est le seul candidat qui ne casse rien (pas 3 à 7).
9. Coûts : produits des prix du mandat par deux scénarios de jetons « supposés » ; F9 pour l'ancrage bas.
10. Sa fidélité dans ce rôle : « supposé », à mesurer sur les témoins.

**Objets de contrôle.** Le mécanisme est ma grille « casse ou ne casse pas ». Objet où la conclusion « recevable » est fausse par construction : Argon, lecteur témoin lui-même ; attendu : refusé par la garde 9 ; rendu : refusé (pas 1 et 2). Objet où elle est vraie : le modèle de la v67, d'une autre famille que le lecteur, qui a joué 14 tests ; attendu : recevable ; rendu : recevable. La garde elle-même n'a pas été exécutée par moi sur ces deux cas : je l'ai lue.

**Premier pas non justifié.** Le pas 10. Ce qui le justifierait : la mesure sur les témoins, avec la borne de fidélité gelée avant. Avant lui, le pas 3 porte un « supposé » (la famille du lecteur aux courses à venir) : la mère peut le lever en l'écrivant au complément de valeurs.

**Mode d'échec affecté.** Sans objet : le mandat ne m'affecte aucune ligne de la table ; celle que j'ai de fait suivie est « Juge parent de ce qu'il juge ».

**Dérivation de l'énoncé seul.** Sans objet : je ne suis pas un agent de re-dérivation ; Carbon, qui n'a reçu que l'énoncé, en tient lieu en partie (§ 6, réserve).

**Trouvaille de côté.** (1) La règle F3 ne dit rien des traducteurs : un auteur peut traduire sa propre proposition (Carbon, faille i). (2) L'objection de l'arbitre à un modèle du troisième relais tient à un fait de disponibilité (F8), non à la règle. (3) Le script de consultation ne garde pas le motif d'un échec d'Astra. Rien de cela n'est poursuivi ici.

**Évaluateur et conseil.** Ce qui juge cet avis : Lazar, et la mesure sur les témoins. Par où il pourrait être bien reçu sans le mériter : l'énoncé neutre est de moi, et sa table favorise le candidat que je recommande (§ 6) ; Carbon est de la lignée de deux candidats ; la troisième voix manque.
