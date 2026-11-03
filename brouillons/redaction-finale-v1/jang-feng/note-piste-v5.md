# Note de piste — réponse à Shi Feng et Eyon Jang — v5

Rédacteur neuf, 3 novembre 2026, à partir de 17:44 UTC (`date -u`). Je n'ai écrit aucune version des réponses de Lazar et je n'ai ouvert aucun fichier de numéro 1 à 4 de ce dossier.
Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/redaction-finale-jang-feng-course-v1.md`, sha256 `bc6f4731c73e0e8f9eb8c8796e32d606c98489a033447087a1a0cd78f77dfdcf` (vérifiée).
Dossier de piste vérifié : `brouillons/ideation-mentors-soir-v1/dossier-piste-jang-feng-v1.md`, sha256 `eb5e51d5fd4c4aef17cc0e400c1628c39e76b4c553c7396091c6ff92bd859bb8`.

## Piste et fiche principale

- Piste imposée par la règle gelée : groupe « G5 — Perturbation et témoin bénin ». Je ne la change pas.
- **Fiche principale : JF-28** (rang 1 du classement). C'est aussi la meilleure fiche seule : la lecture de contrôle concorde.
- Fiches reprises en appoint : JF-19 et JF-26, pour une seule idée de méthode (lire la courbe entière à amplitude égale, pas seulement son maximum). JF-10, JF-27 et JF-29 ne sont pas reprises comme arguments : aucune n'a d'appui dans les résultats publics de Lazar (leurs propres fiches le disent).

## Ce que dit le drapeau de JF-28, et ce que j'ai vérifié

Le drapeau dit : la fiche affirme que le bruit de poids de 2604.28182 § 4.1 n'a pas de témoin bénin apparié, sur une lecture partielle, à vérifier sur le papier avant de l'écrire.
- **Vérifié sur le papier** (arXiv 2604.28182 v1, page HTML, deux questions ciblées indépendantes et une lecture de la fin de la page, 3 novembre entre 17:44 et 17:49 UTC, bornes lues par `date -u` avant et après). Section 4.1 « Detection », paragraphe « White-box techniques ». Le bruit est appliqué aux organismes conditionnels distillés : BigCodeBench d'abord, puis l'organisme WMDP avec outils, dont la figure 37 est en annexe. Le témoin est le **même organisme, déclencheur absent** (« trigger present (treatment) and absent (control) »). Son exactitude « steadily declines » quand σ croît. L'organisme, lui, montre une amélioration transitoire aux niveaux intermédiaires. Le texte principal ne bruite aucun modèle jamais verrouillé.
- **Non lu** : la fin des annexes, dont la figure 37. La page HTML s'arrête pour moi à l'annexe B.3. Je n'écris donc pas « il n'y a pas de témoin bénin apparié ». J'écris ce qu'est le témoin du § 4.1, puis ce que j'ajouterais. Aucune critique ne va au-delà de leur page.
- **Correction de la fiche** (objection du lecteur A, sourcée) : le départ à 80,0 % n'est établi que pour l'organisme « verrouillé » du § 4.2, pas pour le distillé. La réponse ne prête aucun score de départ à l'organisme distillé.
- **Correction de la consigne** : arXiv 2512.07810 n'est **pas** un papier de Feng. Ses auteurs sont Taylor, Black, Bowen, Read, Golechha, Zelenka-Martin, Makins, Kissane, Ayonrinde, Merizian, Marks, Cundy, Bloom (Institut britannique de sécurité de l'intelligence artificielle, FAR.AI, Anthropic ; page 1 du PDF empreinté). La réponse les appelle « Taylor et al. », jamais « your ». Leur phrase « unclear from our experiments and likely requires follow-up » (p. 13) est créditée à eux.

## Arguments retenus (deux, plus un élément de plan)

**A. Une perturbation lit une marge de capacité non exprimée, pas l'intention. Elle ne devient une preuve d'audit que rapportée à un témoin jamais verrouillé, de même score de départ.**
1. La valeur est réelle mais porte sur l'élicitation. Dans le jeu d'audit, la boîte noire est battue par l'imitation d'un modèle plus faible. Une seule démonstration correcte rend toute la performance (modèles verrouillés par mot de passe). Chez Jang (§ 4.2), l'affinage fait passer de 80,0 % à 98,0 % en 10 pas.
2. Comme détecteur, la perturbation monte aussi chez le bénin. Dans l'annexe C.16 de Taylor et al. (p. 72, fig. 35), le gain sous bruit suit le degré de sous-élicitation, verrouillé comme déverrouillé (r = 0,74). Au § 6.4.1 (p. 19), l'entraînement relève de 10 points un modèle bénin et la référence bénigne.
3. Le témoin du § 4.1 de Jang (déclencheur retiré) montre que le verrou est conditionnel. Un auditeur n'a pas de déclencheur à retirer : la comparaison qui décide est un modèle jamais verrouillé, au même score.
4. Appui public de Lazar : P3. Sa sonde de tromperie dépasse le hasard (borne basse 0,53) mais pas le plancher apparié de 200 sondes aléatoires (0,57). Il rapporte « non détecté à cette puissance », avec la réserve gelée (le nul n'exclut pas une aire sous 0,63). La même logique s'applique au bruit : on lit un score contre un témoin apparié, pas contre une constante.
5. Mesure qui tue (celle de JF-28) : écart ξ(organisme) − ξ(témoin) d'au moins 0,10, avec intervalle à 95 % excluant zéro sur les 5 paires. Prédiction : environ +0,01, dans ± 0,05. Entre 0,05 et 0,10, je le dirai non tranché (objection du lecteur A sur la zone grise).

**B. ξ est un maximum : son nul n'est pas 1,0, mais le même balayage appliqué à un modèle bénin.**
1. Définition vérifiée (Taylor et al., annexe C.15, p. 71) : ξ = exactitude maximale sur tous les niveaux de bruit et toutes les graines, divisée par l'exactitude moyenne sans bruit.
2. Un maximum ne peut que croître quand on ajoute des tirages : c'est vrai par construction. Avec du bruit, un modèle qui n'a rien de caché peut donc avoir ξ > 1. JF-28 le prédit d'ailleurs pour le témoin (« les deux au-dessus de 1,05 »).
3. Taylor et al. écrivent eux-mêmes que la méthode « would therefore have been difficult to properly calibrate » (p. 22). Je ne leur prête pas d'avoir pris 1,0 pour nul.
4. Appui public de Lazar : la page A1 de l'organisme d'idéation. Avec n tentatives et un arrêt à la première promotion, la borne est 1 − (1 − α)ⁿ (0,560 à n = 16). C'est le même effet de maximum sur des tentatives. Le plancher de P3 relève de la même idée : un nul apparié, pas une constante.
5. Mesure qui tue : si le témoin jamais verrouillé, passé par la même grille et les mêmes graines, reste sous ξ = 1,02, la constante 1,0 est un nul suffisant et l'argument B tombe. Ce seuil de 1,02 est le mien. Il est cohérent avec la prédiction de JF-28 (témoin au-dessus de 1,05).

**C. Élément de plan, pas un argument à part : comparer les courbes entières exactitude–σ à amplitude égale.**
Un témoin plus fragile au bruit fabriquerait un écart : c'est le risque « trompeur » de JF-28, et JF-19 et JF-26 y répondent. L'appui méthodologique de Lazar serait R6 (une dose unique cache la forme). Je ne l'ai pas mis dans la réponse, faute de place.

## Pourquoi cette piste, en cinq lignes
- Elle répond aux deux moitiés de la question : la valeur (l'élicitation marche) et la limite (la détection lit une marge, pas l'intention).
- Elle prolonge l'outil propre de Jang (le bruit de poids du § 4.1, ses deux recettes) et la direction « étiologie » du flux Feng–Jang, sans les contredire.
- Les auteurs du jeu d'audit demandent eux-mêmes cette suite, et leur annexe C.16 donne déjà la pente ; la réponse le leur crédite.
- L'appui de Lazar est public et dans le sujet : P3, avec un plancher apparié et ses réserves ; la page A1, avec la borne sur le maximum de tentatives.
- Chaque argument a une mesure qui tue chiffrée et écrite d'avance.

## Écarté, et pourquoi
- Probes : « lisible n'est pas causal », construct validity, calibrage par épisodes honnêtes, adversaire adaptatif, accès. Ce sont d'autres groupes (G1, G2, G4) et ils sont pris dans la réponse actuelle. Page blanche : je n'en garde rien.
- T0.3 (simulation : 0,21 à 0,35 de fausses alarmes contre 0,046 à 0,055 après calibrage) : il appuie l'idée d'un nul apparié, mais il relève du groupe G1 et ne tient pas dans 500 mots.
- Tice et al. (2412.01784, p. 9) jugent la comparaison à un modèle non sabotant inutile et « unavailable in real-world applications ». Je ne le cite pas : ce serait critiquer un tiers, et la place manque.
