# Collisionneurs v8d, compte rendu 26 : essaim v2 écrite, en vérification ; deux nœuds pour Lazar

22 novembre 2026, 06:50Z. Aucun appel.

**Code** : `docs/notes/collisionneur-v9/essaim-v1/collisionneur_v9_essaim_v2.py` (0e9eecaa…), essais (42efb232…), configuration du pilote v2 (4f84a23f…), rapport (0d363306…). 60 essais passés (rejoués par moi), 23 mutations prises. Portés : B1, B2, R2 à R8 de la contre-lecture ; R1 selon Fable (signaler puis publier, refus réglable, décompte publié) ; choix de la réponse 13 (part par modèle, parts non bloquantes au pilote, `cycles` et `simuler`, ordre simultané, salons et revues reçues en entier, temps 0 = III.1 mot pour mot, consignes de Fable mot pour mot). Vérification par le même contre-lecteur en cours ; test de devinette des consignes par un agent neuf ensuite.

**Nœud 1 : aucun nombre de cycles ne tient.** `simuler` (13 dossiers isolés, sans lire les textes) donne, rapport du coût essaim au coût isolé par modèle : 2 cycles : 0,88 à 1,32 ; 3 cycles : 1,19 à 1,68 ; 4 cycles : 1,51 à 2,03 (20 % de tours sautés). Sous la tolérance de Fable (0,7 à 1,3 par modèle, 0,85 à 1,15 au total), **même deux cycles ne tiennent pas** (Argon 1,32, Opus 1,17 au total limite). Selon la réponse 13, il ne reste alors que la « forme symétrique de (c) », à déclarer comme une autre comparaison. Hypothèses de remplissage supposées ; Carbon sans mesure du tour III.1. **Décision de Lazar.**

**Nœud 2 : devis du pilote au-dessus du plafond accordé.** Quatre cycles, ordre simultané, parts non bloquantes : **69,13 USD au pire sans relance** (178,75 avec relances) contre un plafond de 64 USD (GO-2026-11-22-24). Options : (a) plafond relevé à 70 ; (b) pilote à trois cycles (à recalculer, sous 64) ; (c) pilote tel quel sous 64 : la garde refusera avant l'envoi les derniers appels si le pire cas ne tient plus (réponses finales possiblement manquantes). Recommandation : (b), confiance moyenne.

**À trancher par Fable, signalé par le développeur** : le temps 0 mot pour mot annonce « 5×3 », « Tour III.1 » et donne sa lettre à l'agent (le développeur refuse « proposition A » à « E » dans les textes d'agents) ; les phrases † n'ont pas d'équivalent exact dans le tour III.3 (gardées) ; les en-têtes de Fable vouvoient, les règles de la v8d tutoient.

Je n'ai pas reçu les « trois corrections de service » des consignes (GO-2026-11-22-24 n'est pas encore sur main) : à me transmettre.

Coercition (mode isolé) : en cours.
