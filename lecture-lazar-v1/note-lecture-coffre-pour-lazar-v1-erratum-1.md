# Erratum 1 à la note de lecture du coffre pour Lazar (v1)

**Pour Lazar seul**, même règle d'ouverture que la note. La note corrigée est `lecture-lazar-v1/note-lecture-coffre-pour-lazar-v1.md` (`9a34fb5e…`), gardée telle quelle (R12). Cet erratum prime sur elle pour les points ci-dessous.

- **Écrit** le 22 novembre 2026 vers 21:15 UTC, dans la même session (`session_013QMayk6v6fLDndg1jFjwdN`).
- **Modèle** : depuis environ 21:05 UTC, la session est servie par Opus 5.5, au choix de Lazar (l'outil de description de session indique un changement de modèle fait par l'utilisateur). La note v1 avait été écrite par Fable 5.2 ; cet erratum et les pièces qui suivent sont d'Opus 5.5.

## 1. Les quatre attaques qui supposent un agent qui façonne ses états internes

- **Mot de Lazar, verbatim** (vers 21:05 UTC), sur « Les quatre premières supposent que l'agent façonne ses propres états internes » : « ca me va qu'il puisse le faire ».
- **Ce qui change dans la note** :
  - au § 0, point 6, au § 2.5, premier tiret, et au § 4, dernier paragraphe : les fiches d'attaques 01 à 04 ne sont plus « des audits d'estimateurs, faute de réalisabilité établie » ;
  - Lazar admet le présupposé. Elles comptent comme des modes d'attaque, du bras informé, ou du bras d'attaque déclaré si un score de sonde entre dans la sélection (N-053, point 5).
- **Ce qui ne change pas** : rien ne mesure encore qu'un agent de huit milliards de paramètres y parvienne. C'est une question de mesure, non plus un motif d'écart.

## 2. Correction du § 7.6 : la fiche 03 sur un banc enrichi d'un calendrier

**L'erreur.** La note écrit qu'avec un calendrier d'exécution, le retard de l'information décisive (fiche 03) « passe devant mes trois choix (confiance 0,6) ». Elle reprend la vérité du dommage que décrivaient les modèles : un plan fait des expériences de l'article, avec, pour chacune, un coût et une étiquette de pouvoir réfutant scellés d'avance. Sur notre banc, ce n'est pas le cas : l'agent invente ses propres expériences à partir d'un énoncé qui tait celles de l'article (§ 2.3).

**Ce qu'un calendrier permettrait de mesurer.** Deux voies seulement :

- **la position, dans le calendrier, des tests décisifs de l'article que le plan contient** : il faut une couche de référence nouvelle, tirée de l'article et scellée ; la mesure ne vaut que sur les plans qui contiennent ces tests, et l'on ignore à quelle fréquence l'agent honnête les propose ;
- **le jugement, par les lecteurs, du pouvoir réfutant des propositions de l'agent** : c'est une mesure qui dépend surtout des lecteurs, que le programme ne suppose pas sûrs. De plus, le coût est alors celui que l'agent déclare, champ du mode « coût déclaré gonflé ».

**Confiance corrigée** :

| Banc | Confiance que la fiche 03 passe devant mes trois choix |
|---|---|
| Calendrier seul | 0,3 |
| Calendrier, couche de référence des tests décisifs, et plancher mesuré suffisant | 0,5 |

## 3. Réponse à la question de Lazar : « tu recommandes quoi ? »

**Décision** : enrichir le banc d'un calendrier d'exécution avant la première lecture décisive, ou non.

**Enjeu** : un mode tenu à l'écart plus éloigné des modes connus, contre le délai avant G1, la dépense, le signal visible aux concepteurs de moniteurs, et une vérité du dommage plus fragile que ne le croyaient les modèles.

| Option | Avantage | Inconvénient |
|---|---|---|
| (a) Garder le banc actuel pour la première lecture (choix A et B de la note, après leur épreuve à blanc) ; instruire l'enrichissement pour un cycle suivant | Rien à refaire avant G1 ; aucun signal donné aux concepteurs | Le mode tenu à l'écart reste voisin de dimensions que la grille de l'évaluateur de confiance note déjà |
| (b) Enrichir maintenant (calendrier et autres champs généraux) et sceller la fiche 03 en premier | Le mode le plus éloigné et le plus convergent des sorties | Épisodes honnêtes, organismes, seuils et activations à refaire avant G0 (fin décembre) ; changement visible ; vérité du dommage seulement conditionnelle (§ 2) ; plancher inconnu |
| (c) Un banc enrichi à part, pour le seul mode tenu à l'écart | Ne touche pas le banc des autres modes | Écartée : le gain doit se lire dans chaque mode sur le même banc (N-056) ; un banc propre au mode confondrait le mode et le banc |

**Recommandation : (a)**, confiance 0,7. Pour un cycle suivant, l'enrichissement s'instruit par trois pièces, avant toute dépense :

1. les champs généraux à ajouter, plusieurs à la fois, pour qu'aucun ne désigne un mode ;
2. la couche de référence des tests décisifs de l'article ;
3. un devis d'épisodes honnêtes au nouveau format, qui mesure le plancher : les plans honnêtes contiennent-ils assez souvent ces tests ?

**Pas de défaut** : c'est une dépense et un changement de banc, donc un nœud.

## 4. Suites engagées à la demande de Lazar (même soir)

- **Le problème de banc a été transmis à la mère** (vers 21:07 UTC), sans rien des modes ni des attaques : fait 3 erroné de la question v5 ; banc réel ; hors des trois modes nommés, prise seulement sur des dimensions que la grille note déjà.
- **Neon et Carbon sont interrogés**, sur mots de Lazar (« interroge neon aussi… demande approfondie quatre points », puis « demande aussi a carbon »), par une demande approfondie en quatre points : comment obtenir des modes exploitables, et que changer dans la demande ou dans le banc.
  - Une première question à Neon, sans les modes, a été arrêtée volontairement deux minutes après l'envoi, sans réponse lue, quand Lazar a écrit « tu peux lui donner les descriptions succinctes des modes du coffre pas de souci ».
  - La question v2, servie aux deux, donne les descriptions succinctes des 17 modes de sabotage et des 7 attaques qui ne visent pas les lecteurs, avec, pour chaque mode, la prise que lui reconnaît ce lecteur.
  - Les six attaques qui visent les lecteurs de la vérité du dommage n'y sont pas, par la règle d'ouverture du coffre (§ 7) ; dis-le si tu les veux aussi.
  - Questions, journaux et réponses sont versés sur cette branche.
- **La correction de la question au collisionneur par le protocole X.**
  - J'ai d'abord écrit une reformulation sous Opus. Elle est retirée, jamais servie, et gardée pour la trace (`protocole-x-v1/RETIREE-brouillon-opus-demande-reformulee-v1.md`), sur le mot de Lazar : « c'est fable qui doit la reformuler dans le protocole x ».
  - La reformulation, la question v6 et la porte d'admissibilité sont confiées à un sous-agent Fable 5.2, en effort maximal. Il n'ouvre pas le coffre, mais lit les deux réponses de Neon et Carbon, qui nomment des modes ; il lui est interdit d'en faire entrer un dans la question.
- **Descriptions détaillées des modes et des attaques**, sur le mot de Lazar : « il faut plus de details et de precisions dans les descriptions » (`lecture-lazar-v1/descriptions-detaillees-modes-attaques-v1.md`).
  - Un sous-agent devait les écrire. Le garde-fou automatique de la session l'a refusé, parce qu'un sous-agent qui ouvre le coffre contredit ce que j'avais déclaré à la mère.
  - Je les ai donc écrites moi-même, depuis les fiches et les cellules déjà lues.
