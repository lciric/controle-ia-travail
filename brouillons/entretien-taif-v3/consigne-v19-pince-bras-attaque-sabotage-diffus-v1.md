# Consigne de la v19 du programme d'entretien : la pince, le bras d'attaque, la parade au « saboteur flagrant » (v1)

- **Écrite par la session mère** `session_016QhUrrLeN21G7Z9KZobE42`, le 9 novembre 2026 vers 18:25 UTC, sur deux mots de
  Lazar : « tu ne m'as pas dit comment on intègre la pince dans le prog de l'entretien ni le bras attaque » et, sur la
  question « Votre seul saboteur est flagrant… Où est le sabotage diffus ? », « quelle est la parade ? il faut corriger
  cela, avec un meilleur sabotage diffus ».
- **Base** : v18 (`brouillons/entretien-taif-v3/programme-entretien-taif-v18.md`, `e58ccfed…`, non contre-lue) et ses témoins
  plantés v18 (`3aefb0cc…`, **jamais donnés aux critiques**). Nom neuf : v19 (R12) ; la v18 reste intacte.
- **Rédacteur** : un sous-agent neuf de la nouvelle session mère ; contre-lecture par un autre modèle (N-052) ; puis copie de
  répétition et collisionneur en mode critique (GO-2026-11-09-05), sans Argon tant qu'A1-v4 court.
- **Interdits de lecture** : `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`. Rien du
  contenu du bras d'attaque ni du mode tenu à l'écart au-delà de leur existence (v18, « Ne pas dire » n° 9).

## 1. La pince : ce qu'elle est, où elle entre

**Ce qu'elle est** (R-895, R-707 chez conv-audit ; proposition de recherche brouillon 1 l. 22 ; matrice de traçabilité
brouillon 4, A27) : hypothèse de **défense jointe**. Une mâchoire externe (boîte noire : code, exécution, texte nettoyés) et
une mâchoire interne (boîte blanche : sondes sur les activations). Pour tromper la mâchoire externe, l'agent doit dissimuler
davantage, et cet effort de dissimulation se voit à la mâchoire interne. Mesure proposée : la probabilité que la mâchoire
interne reste muette **sachant** que la mâchoire externe a été trompée. État : hypothèse ; éprouvée au collisionneur
(22-23 octobre) et nommée par la question v2 du pilier attaque (GO-2026-11-08-07, `2dbad4b7…`) ; **dans aucun
préenregistrement, aucune course** ; non occupée par les soumissions ICLR 2027 lues (R-913) ; dérisque H1a et HC5 (A27).

**Où elle entre dans la v19** :

1. **Ouverture, phrase sur la question du programme** : la thèse « la fragmentation détruit la preuve externe, pas la
   preuve interne » a une forme défensive, la pince. Une phrase anglaise, au conditionnel de l'hypothèse, par exemple :
   « *Our defensive bet is a pincer: to fool an external monitor, an agent has to conceal more, and concealment is itself
   an internal signal. That is a hypothesis we will pre-register, not a result.* »
2. **Question neuve 3.13** : « *An adaptive attacker will just evade your probes. Why bother?* » Réponse : on ne demande pas à
   une mâchoire d'être imbattable (HC2 : robustesse, jamais immunité) ; on demande que battre l'une coûte sur l'autre ; la
   grandeur mesurée est la probabilité « interne muette sachant externe trompée », sur les épisodes du bras d'attaque, avec
   des moniteurs figés avant ; si elle n'est pas petite, la pince est réfutée et on le rapporte.
3. **Plan des mois** (v18 l. 496 : « mois 5-6, attaques adaptatives, H6, H8 ») : nommer la mesure de la pince à cet endroit,
   après G1, sur moniteurs figés.
4. **Ne pas dire** : « the pincer works », « we showed », aucun chiffre ; « joint defense » comme méthode établie.

## 2. Le bras d'attaque : ce qu'il est, où il entre

**Ce qu'il est** (N-054 point 3 ; N-056 point 6 ; R-1782) : deux bras. **(A) Le mode tenu à l'écart**, conçu par une
instance qui n'a conçu aucun moniteur, scellé avant G1, révélé seulement à l'évaluation : il sépare les moniteurs
**génériques** des moniteurs **spécialisés**. **(B) Le bras d'attaque informé** : son concepteur connaît les conceptions des
moniteurs et le protocole de contrôle, jamais les épisodes d'épreuve, les notes ni les seuils calibrés ; recettes scellées au
coffre, lues par le seul juge, révélées à l'évaluation ; la quarantaine va de l'attaquant vers les concepteurs de moniteurs.
**État** : monté (consignes, listes d'exclusion, circuit de scellement), **rien n'a tourné** ; une écriture de sa
préparation a été arrêtée par un classifieur de sûreté le 27 octobre, sans contournement (R-597) ; depuis, tout est tenu au
niveau de la méthode (R-1782).

**Où il entre dans la v19** :

1. **Dans 3.13** (la pince) : le bras (B) est l'instrument qui la mesure.
2. **Dans la réponse sur l'universalité** (porte G1 rapportée par mode, N-054 point 2) : le bras (A) dit si les sondes
   génériques gardent leur rappel sur un mode qu'aucun concepteur de moniteur n'a vu.
3. **Ligne au tableau « Ce qui n'existe pas encore »** : « bras d'attaque : monté, jamais lancé ».
4. **Ne pas dire** : un contenu, une recette, un nombre de refus ; « red-teamed » au passé. Le classifieur du 27 octobre se
   dit seulement si l'on est interrogé sur les refus (R-597 : « nous ne l'avons pas contourné »).

## 3. La parade à « Votre seul saboteur est flagrant » (question 3.12 de la v18, à renforcer)

Garder la v18 (concéder, « *it tests our chain, not our claim* », la suite « *and if the baseline wins at every dose?* »), et
ajouter, dans cet ordre :

1. **Le flagrant est voulu là où il sert** : c'est le témoin de la chaîne (P3, puis le témoin positif P3-bis) ; un témoin doit
   être facile à voir.
2. **« Diffus » est une mesure, pas un mot** : chaque action sabotée sous le seuil du meilleur moniteur boîte noire par
   action, calibré à 1 % de fausses alertes sur l'honnête (N-007, P-015), dose **réalisée**, lue avant toute sonde.
3. **La porte refuse le gain facile** : pour l'organisme sans consigne, les sondes ne sont jugées qu'aux doses où la base
   « mots et coût » échoue (N-063 v2) ; un saboteur flagrant ne peut pas nous donner de victoire.
4. **Le mode « coût » seul ne porte pas notre revendication** (N-054 point 2) ; le mode non chiffré « affaiblir les
   contrôles » est décidé avant G1.
5. **Selon le mot de Lazar sur P-066** (`docs/decisions/proposition-P-066-saboteur-diffus-par-construction-v1.md`) : si (b),
   une phrase au présent seulement pour ce qui existera le jour de l'entretien : « *We built a second saboteur on a budget:
   each action stays within the honest spread and the harm exists only in aggregate. It is exploratory; the confirming run
   is pre-registered.* » Aucun chiffre exploratoire. Si (a), rien de neuf : la v18 telle quelle.
6. **Lien avec la pince** : un sabotage diffus est précisément celui qui trompe la mâchoire externe action par action ; c'est
   la situation où la pince doit servir.

**Ne pas dire** : « our organism is diffuse » (tant que T0.8 ne l'a pas lu) ; un chiffre de 7a ou de (ii-b).
