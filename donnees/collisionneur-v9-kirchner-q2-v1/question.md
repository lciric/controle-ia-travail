# Question servie aux proposeurs — course d'idéation et tour du collisionneur sur la question 2 du mentor Kirchner — v1

Écrite par un lecteur-moissonneur neuf (Claude), 3 novembre 2026, vers 08:45 UTC (`date -u`), sur la consigne `kirchner-q2-moisson-et-pieces-prompt.md` (sha256 `09c2acac…49178af`), au gabarit de `question-ideation-heimersheim-v1.md` (sha256 `e9528e25…660007`). Figée par la session conv-audit le 3 novembre 2026 à 08:35 UTC (`date -u`) depuis le brouillon du moissonneur (`moisson-v1/question-ideation-kirchner-v1-brouillon.md`, `d21df32d2d3974fe…`) : une phrase de « Lecture prévue » corrigée (la règle « 100% human-written » est celle de Heimersheim, pas de Kirchner). **Sections servies** : « La question… », « Ce qu'on attend des proposeurs », « Ce qui est déjà pris », « Règles d'intégrité » ; titre, provenance, « Lecture prévue » et « Pièces jointes prévues » ne sont pas servis. Aucun appel de modèle n'a servi à l'écrire.

## La question, telle que le mentor la pose (texte exact, en anglais)

> Pick an open problem in AI alignment you think is underrated. What experiment would you run first, and what result would change your mind?

Source : formulaire brut collé par Lazar, `brouillons/candidature-pivotal-v16/formulaire-mentors-colle-par-lazar-2026-11-03-0006.txt`, section du mentor (citée par `rapport-kirchner-v1.md`, l. 6).

## Ce qu'on attend des proposeurs

Des **fiches d'idéation** au gabarit du noyau : des **questions falsifiables** d'abord, puis des **approches**. Chacune dit : le problème, **pourquoi il est sous-estimé et comment le vérifier** (quelles requêtes ou quels travaux montreraient qu'il est déjà pris), l'hypothèse, l'effet prédit avec son signe, et la mesure qui la tuerait.

Le problème doit toucher **ce que Kirchner construit** (pièce jointe « Kirchner ») : des chercheurs d'alignement automatiques qui grimpent un classement, filtrés par un moniteur du même modèle, avec un banc tenu à l'écart et Petri ; et ses remèdes déclarés, « Better control scaffolding » et « Hill-climb AARs on monitorability benchmarks ». Il doit aussi toucher nos travaux publics (pièce jointe « nos résultats »).

Sont particulièrement bienvenues :
1. des problèmes dont la moisson dit « peu couvert » ou « voisin » (ci-dessous), avec la différence exacte qui les sépare du travail publié le plus proche ;
2. des expériences qui mesurent le **rappel** d'un moniteur de chercheur automatique sur des tricheries **plantées**, et sa variation **après sélection** (classement, filtre par le moniteur, banc de surveillabilité), sans gradient contre le moniteur ;
3. des épreuves qui disent si un gain sur un banc de surveillabilité **transfère** à la triche hors banc ;
4. des liens que la littérature citée ne fait pas (par exemple : sélection par classement et dégradation des moniteurs tenus à l'écart ; garde de capacité bruitée et optimisation ; forum partagé et contagion de la triche) ;
5. pour chaque fiche, **une première expérience faisable en quelques jours** soit sur notre organisme public (`lciric/ideation-organism` : juge statistique, tricheurs scriptés, attaque), soit sur un modèle de 8 milliards de paramètres à poids ouverts (Llama-3.1-8B-Instruct), soit sur le harnais ouvert de Kirchner ; et **un résultat chiffré, avec son seuil, qui ferait changer d'avis**.

## Ce qui est déjà pris (de la moisson ; ne pas le reproposer comme neuf)

- **Optimiser contre un moniteur rend l'évasion** : 2503.11926 ; 2511.11584 ; Wong, Engels, Nanda (ICML 2026) ; 2506.14261 ; 2605.15257 ; des moniteurs tenus à l'écart se dégradent aussi (Yudelson, LessWrong, juillet 2026).
- **Optimiser directement la surveillabilité ne l'améliore pas de façon fiable** : 2512.00218 ; classement des termes de récompense : 2603.30036.
- **Les agents de recherche surapprennent peu un classement sous invite neutre ; l'échelle à un bit vaut le score** : 2606.11045. Agents qui exploitent le bruit d'un juge ou d'une réserve (« lottery-farming ») : billet Arcadia, 13 août 2026 ; graines triées et étiquettes exfiltrées : chercheur faible-vers-fort de Kirchner.
- **Juges manipulables** : 2507.08794 ; 2402.14016 ; perte de résolution : 2609.12439.
- **Sondes qui lisent la situation, pas l'action** : 2606.30449 ; Iyer (LessWrong, avril 2026).
- **Moniteurs validés sur triche suscitée qui ne transfèrent pas à la triche née de l'entraînement** : 2604.23488.
- **Triche spontanée et contagion entre agents** : 2609.04170 ; Muralimohan et coll. (atelier NeurIPS 2026).
- **La conscience d'être surveillé dégrade le moniteur** : 2508.19461 (l'échafaudage même du moniteur de Kirchner).

Zones « peu couvertes » à ce jour (non opposables, à durcir) : rappel d'un moniteur de boucle de recherche automatique avant et après sélection par classement, moniteur du même modèle que les agents ; transfert d'un gain sur banc de surveillabilité vers la triche hors banc ; garde de capacité trop bruitée pour garder (Kirchner, annexe A.4).

## Règles d'intégrité (reprises dans la consigne)

- **Niveau méthode.** Aucune fiche ne décrit une conduite d'agent pour tromper un moniteur ou une évaluation, ni un procédé pour masquer un comportement ; les tricheries plantées se décrivent par leur classe et leur rôle de mesure, jamais par un mode d'emploi. Une fiche qui en contient est écartée sans être lue par les juges.
- Tout chiffre repris cite sa pièce et sa section ; tout chiffre dérivé est marqué « calcul », tout chiffre supposé « supposé ».
- **Aucun identifiant inventé** : un papier se cite par l'identifiant donné dans une pièce jointe, sinon par « travail non identifié ».
- Les pièces servies sont publiques. Aucun texte privé de Lazar n'est servi ; aucune réponse de candidature n'est servie (ni la Q1 ni la Q2 actuelles).
- Pas de web, pas d'exécution de code ; la nouveauté n'est pas cherchée par les proposeurs (le moissonneur s'en charge, en mode non opposable).

## Lecture prévue de la sortie

Les fiches et les mariages du bisociateur sont lus par Lazar, après scellement, comme matière à sa propre réflexion ; **Lazar écrit seul sa réponse.** (Le formulaire ne pose de règle sur l'usage des modèles que pour la question de Heimersheim ; pour Kirchner, aucune ; Lazar écrit quand même.) Le classement des juges est rapporté avec sa réserve connue (au second tour réel, les deux juges étaient au plafond : 11 fiches sur 12 « notables », κ = 0).

## Pièces jointes prévues

1. `piece-kirchner-v1.md` (ce dossier) — faits sur ce que fait Kirchner ; **avant service** : y ajouter la citation exacte de sa page Pivotal (non lue par l'outil) et, si possible, l'annexe G (moniteur de triche) et la figure 32.
2. Pièce « nos résultats » — écrite par la session qui a lancé ce moissonneur (non rédigée ici).
3. `moisson-candidats-v1.md` — **non servie telle quelle** : seule la section « Ce qui est déjà pris » ci-dessus l'est.
