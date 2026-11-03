# Heimersheim Q1 — remarques de fond sur ton texte — v1

Conv-audit, 3 novembre 2026, vers 20:46 UTC (`date -u`). Ton texte : `reponse-lazar-v1.md` (`d842e467…`), 2 762 mots ; aucune limite au formulaire. Comparé au plan vérifié (`squelette-heimersheim-q1-v2.md`, `d2f0aded…`).

**Règle du mentor** : texte 100 % humain. Ce fichier ne contient **aucune phrase anglaise** ; je ne cite que tes propres mots pour situer l'endroit. Les corrections sont à écrire par toi. Un vérificateur neuf contrôle en parallèle les affirmations absentes du plan (rapport à venir, `verification-texte-lazar-v1.md`).

## À corriger (le fond est faux ou plus fort que la source)

1. **l. 47-53, D36, « Not that of the specific item. »** C'est trop fort : la même pièce donne 65 % et l'autre pièce 44 % ; le contenu de l'item porte donc une part. Le plan dit « surtout » le cadre, pas uniquement.
2. **l. 43, réplication manquée.** Deux écarts de logique :
   - « It took both to activate against sycophancy » laisse croire à une vraie baisse. Ce qu'il a fallu, ce sont les deux causes réunies pour produire une **baisse apparente**.
   - « Which could explain my finding above that the answers were cut off » inverse la causalité : la troncature à 300 caractères n'est pas un résultat expliqué, c'est la seconde cause qui explique la baisse apparente.
   Le sens de « think the model wasn't backing down » est juste (un verdict négatif adouci ou différé se lit, au début, comme une position tenue).
3. **l. 89, R6 sous éloge, « it increased by 0.28 to 0.80 ».** Le gain va **de** 0,28 **à** 0,80 (+0,52 [0,29 ; 0,76]) ; « by » fait lire une hausse comprise entre 0,28 et 0,80.
4. **l. 87, R6 sous critique, « no change ».** L'intervalle contient 0 : c'est « pas de changement détectable », pas « aucun changement » (le plan interdit « saturé » pour la même raison).
5. **l. 27, R7, « The 72B was activated but not controlled ».** R7 est une note plantée dans le texte lu par le moniteur, pas un pilotage d'activations : le 72 milliards est **déplacé**, pas capturé. Le verbe « activate » est faux ici.
6. **l. 7, ce que pilotent Hua et coll.** Ils pilotent la conscience d'évaluation (vers le déploiement) ; les indices de type sont la **lecture**, pas la cible du pilotage. « they activated against type hinting » mélange les deux.
7. **Le verbe « activate » partout (titre, thèse, § 2 à 7, l. 83 « activating after layer 1 »).** Le terme du champ, et celui de la question (c) du mentor, est le pilotage (« steering ») ; « activate » veut dire autre chose en interprétabilité. Chez Janiak et coll., c'est une **perturbation** après la couche 1.
8. **l. 109, « log of the 2 thresholds ».** La mesure de la fiche M-066 est le logarithme du **rapport** des deux seuils.
9. **l. 83, « 70 times more ».** C'est l'écart de **sensibilité** entre directions, environ 70 fois au plus sous la mesure de Kullback-Leibler (note 1), pas un facteur fixe à appliquer.
10. **l. 19, (d), « There is no attempt at controlling for formality… ».** Le plan dit seulement qu'aucune paire formel / familier à statut constant n'est rapportée **chez Hua et coll.** ; tel quel, la phrase vaut pour tout le champ.
11. **l. 57, nom** : « Ferreara da silva » → Ferreira da Silva.

## À vérifier avant d'envoyer (absent du plan ; le vérificateur en cours y répond)

- l. 13 : les deux phrases d'invite entre guillemets sont-elles les mots exacts du papier ? Sinon, retire les guillemets.
- l. 16 : « couldn't confirm on their smaller model (Appendix B) ».
- l. 18 : les noms d'auteurs (« Devbunova », « Singh & Chaudhary ») et le modèle Llama-3.1-8B-Instruct pour 2603.19426 ; ce que tu attribues à 2608.13329 (directions moins semblables entre invites différentes qu'entre deux moitiés d'une même invite). Le plan n'a que les titres et résumés de ces trois papiers, « à ouvrir avant de citer ».
- l. 59 : que 2603.19426 ait employé des paraphrases dans un plan croisé.
- l. 27 : R7, « all monitors … from 0.5B to 32B » et « could control 1.5B, 3B and 32B with very little left over ».
- l. 73 : « 5 token prompts from fineweb ».
- l. 91 : « (2.6) » comme moyenne sans pression, et « refusals under praise » (le plan dit des refus que le juge note au milieu, sans préciser sous éloge).
- l. 109 : que les quatre vecteurs de l'Institut britannique viennent de la fiche système d'Opus 4.6.

## Juste (repris du plan vérifié)

Chiffres de Hua et coll. (v5 : 80 %, 33 %, 10 % ; 56,8 → 55,2 % ; 24 vecteurs gaussiens ; 16 paires ; avant affinage) ; l'objection forte et ta réponse par la dose ; annexe I.1.1, tableau 16, 0,34 à 0,60 ; ρ = 0,684 et sa réserve ; méthodes de rang 1, sans nombre ; trois têtes 58,5 → 57,5 % ; rang 3 61,0 → 46,5 %, −14,5 [−23,0 ; −5,7], p = 0,0019 sur 83 ; D36 (29 juillet ; 5 et 6 août ; 13 jetons, couches 13 à 25 ; 37 items ; 65 %, 44 %, 2 % et leurs intervalles ; critère (c)) ; 33 concepts sans l'évaluation ; règle des paires (210 sur 528) ; p = 2,05 [2,00 ; 2,10] ; 2,42, 2,30 et 2,05 sur Gemma seul ; 2,24 à 2,63 ; aucune valeur pour Llama ; p > 2 sur tous les modèles, Llama compris ; Lee et Heimersheim sur GPT-2 small, couche 6 ; Janiak et coll. (0,5 à 7 milliards) ; R6 (1 350 générations, trois doses, 0,66 / 0,68 / 0,63, −0,03 [−0,22 ; 0,20], 1,87 / 1,33 / 2,37, 4,01 → 2,47, les 14 items à refus) ; R9 (addendum archivé, non lancé ; 33 contrastives, 40 différences aléatoires, richesse–genre) ; R9-bis (3 novembre, avant toute donnée, `b3ecaec`, 2° à 60°, direction neutre) ; « control_book » à −0,025 ; Lindsey ; Opus 4.6 et les oracles d'activation (« pas entièrement éliminée »).

## Pièges du plan : bien évités
Fin du prompt (pas « points of pressure ») ; « environ deux tiers, intervalle large » ; ρ = 0,684 jamais fondu avec « < 1 % » ; pas de « similar to my rho vector » ; trois têtes et L0.H29 sans nombre ; « clamping » ; la réserve des refus ; aucun chiffre du bras original de D36.
