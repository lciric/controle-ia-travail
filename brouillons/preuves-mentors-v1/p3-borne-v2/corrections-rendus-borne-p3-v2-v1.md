# Borne de P3 v2 — corrections des rendus et phrase à citer, v1

Écrit par la session conv-audit le 1er novembre 2026 vers 23:50 UTC, d'après la vérification par un sous-agent neuf (`verification-borne-p3-v2.md`, `397139c6f85953dcde99fd817b6bf8ab2af4a3928e0f452d3cd34b1e7b37353c`, verdict « vérifié avec corrections »). Les rendus `borne-p3-v2.md` et `p3-bound-v2.md` restent tels quels (R12) ; ce fichier dit comment les lire.

## Ce qui est vérifié
- Les nombres de la v2 sont exacts ; la vérification les reproduit avec son propre code et ses propres graines (repère de puissance 0,8 pour la sonde de tromperie au seuil que P3 a réellement affronté : 0,462, dans l'intervalle du JSON [0,449 ; 0,466]).
- Le script fait ce que dit le plan ; le contrôle d'identité avec le code gelé de P3 est réel (écart 0).

## Corrections de lecture (les rendus ne sont pas réécrits)
1. **La fourchette « 0,33–0,46 » doit nommer ses deux bouts** : 0,46 écart type = seuil observé du plancher, celui que P3 a réellement affronté (bout principal) ; 0,33 = plancher de sondes aléatoires **recentré**, c'est-à-dire débarrassé de l'écart saboteur − honnête que portaient déjà les 200 sondes aléatoires du run : un plancher au niveau du bruit, qui rend le nul plus informatif que la règle réellement appliquée. La puissance 0,03 au décalage observé vaut au seuil observé ; au plancher recentré, elle vaut 0,53.
2. **0,03 ne fait que reformuler le nul**, et sa deuxième décimale dépend du tirage (vérification, 2 000 répétitions : 0,019 [0,013 ; 0,026]) : dire « environ 0,02 à 0,03 ».
3. **Le recoupement avec l'addendum 2** (aire 0,6317 contre `A_80` 0,6315, `diag/20261020-220858-addendum2-p3/lecture-addendum2-p3.json`, `916f4536…`) est un recoupement de **méthode**, pas de données : les deux partagent le seuil et la demi-largeur du même run.
4. **Le contrôle de dispersion** (1,03 et 1,01) est presque tautologique pour le modèle apparié (au décalage observé, c'est le rééchantillonnage par tâches du run) ; il aurait arrêté la v1 (1,87 à 2,08).
5. Hors plan, avec le plancher brut recalculé à chaque rééchantillonnage, la vérification trouve ≈ 0,49 (tromperie) et ≈ 0,44 (enjeux) : la valeur 0,46 tient ; la fourchette gelée n'est asymétrique que vers le bas.
6. Écart d'exécution : `ecart-execution-borne-p3-v2-v2.md` (remplace la v1).
7. Forme : tableau du rendu anglais cassé l. 64 (barres verticales) ; points décimaux dans le rendu français l. 50-51 et 127.

## Phrase pour les candidatures — décision de Lazar
- (a) Phrase gelée telle quelle (aucun écart au gabarit ; mal lisible : « reaches 0.8 only near 0.33–0.46 SD »).
- **(b) Recommandée par la vérification (confiance 0,7) et par la session** — nomme les deux bouts, s'écarte de la forme littérale du gabarit :
  > P3's null (no generic probe cleared its random-probe floor) is a bounded null: re-running P3's exact rule on task-paired resamples, power was 0.03 at the observed deception-probe shift of 0.27 honest-score SD (95% CI [0.13, 0.41]) and reaches 0.8 only near 0.46 SD at the floor threshold P3 actually faced (0.33 SD against a random-probe floor re-centred to remove its saboteur–honest offset). It bounds large mean shifts, not small ones; it does not say there is no signal below that, nor that the probes do not read intent.
- (c) « 0.46 SD » seul : exigerait une v3 (la règle gelée impose la fourchette).
Défaut : (b) dans les textes préparés ; c'est Lazar qui soumet, donc qui tranche en dernier.
