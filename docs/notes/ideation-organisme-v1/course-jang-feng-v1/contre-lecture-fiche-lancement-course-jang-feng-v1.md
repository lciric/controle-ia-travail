# Contre-lecture de la fiche de lancement de la course Jang-Feng (brouillon 1) — v1

Contre-lecteur neuf (règle R2), sous-agent qui n'a écrit ni le kit ni la fiche. 3 novembre 2026, 14:26 UTC (`date -u`).
Aucun appel payant, aucune clé, aucun fichier existant modifié. J'ai lu dans un arbre partiel neuf (`wt-cl-jangfeng`,
`ce3dec8a`) et extrait les sources de `origin/canal/conv-audit-n04` (`d0e15c86`) par `git show`. Seul fichier écrit : ce
rapport (non scellé, non commité).

Objet : `docs/notes/ideation-organisme-v1/course-jang-feng-v1/fiche-lancement-course-jang-feng-v1-brouillon1.md`,
sha256 `0974e14d9f19532aae6fc554bba598ed732777a90ebcbce276df54237e8e9154` (compagnon vérifié : OK). Les numéros de ligne
renvoient à la fiche.

## Verdict

**À corriger.** Aucun constat bloquant. Un constat majeur (CLJ-01) :
- le risque de refus d'Opus est sous-déclaré ;
- le kit n'a **aucune variante sans Opus**.

Trois constats mineurs. Tout se corrige dans le texte de la fiche, sauf si session-depot choisit d'ajouter une variante sans
Opus (CLJ-01, option).

## Vérifié conforme

- **Sources** :
  - Question `d68c6c5c…`, pièce Feng et Jang `1f423643…`, nos résultats `d6fa8011…`, protocole `fbbbb520…` et n° 419
    `75aedf2e…` : chacune est à l'empreinte de son compagnon sur le canal et identique à l'octet à la copie du kit.
  - Aucune spécification propre à cette course n'existe sur le canal (recherche de « jang » et « feng » dans
    `brouillons/ideation-mentors-soir-v1/`).
- **Pièces gelées** :
  - Les 48 lignes de la table sont OK par `sha256sum -c`.
  - `table_pieces_gelees_jangfeng_v1.py --verifier` donne « conforme : 48 pièces gelées ».
  - Tous les compagnons du kit sont OK, et les empreintes de l'orchestrateur sont conformes sur disque.
  - Les empreintes citées sont exactes : consigne `d42df37e…`, devis `b3204219…`, course à blanc `767dcd34…`, mutations
    `4e02b0b5…`, répétition `b7e07a9d…`, configurations `073528eb…` (cinq espèces) et `b3501965…` (avec Kimi).
- **Marqueurs** : le seul est `<<EMPREINTE_RAPPORT>>`, à la l. 10. Voir CLJ-03 pour `GO-2026-11-03-NN`.
- **Vérification du lanceur** : `lancer_course_jangfeng_v1.py verifier --configuration … --registre-go <registres/go.md de
  main à 9d40b65d> --go-attendu GO-2026-11-03-12`, avec `GO_ID=GO-2026-11-03-12`, rend le **code 0** pour les trois
  configurations (« écriture : aucune, appel : aucun »). Je l'ai jouée sans la fiche, puisqu'elle n'est pas encore scellée.
- **Consigne du proposeur** :
  - `--verifier` donne « conforme ».
  - Contrôle indépendant : on y trouve à l'octet, dans cet ordre, la section « La question, telle que les mentors la posent »
    (avec le paragraphe « Ce qui est attendu d'une fiche »), les règles d'intégrité, la pièce Feng et Jang, et nos résultats
    (positions 467 < 1 061 < 1 861 < 14 369).
  - La consigne fait 21 797 octets.
- **Juge** : K1 à K3 reprennent les trois items du n° 419 dans leur ordre, sans l'originalité.
- **Garde lexicale** : la liste d'Ibrahim est entière. La pièce n'emploie ni « openai » ni « gemini ». Passée par
  `pole/fiches_v54.trouver` (« prefixe ») sur les consignes, la liste, le vocabulaire du substitut, la question et les deux
  pièces : rien n'est trouvé.
- **Dépense** :
  - S17 = 198 ≥ 1,2 × 164,64 = 197,57 (calcul). La ligne GO-2026-11-03-12 porte 198 USD.
  - Plafonds de session, chacun au-dessus du pire cas d'un appel de son rôle : proposeur 3,5 > 3,271 ; aiguilleur 0,4 > 0,3386 ;
    juge 0,9 > 0,8493 ; lecteur 0,9 > 0,8498 ; fusion 3,5 > 3,2862.
  - Relais, chacun au-dessus de son pire cas, la somme faisant 198 dans les trois variantes :
    - cinq espèces : Claude 91,0 ≥ 77,14 ; Astra 102,0 ≥ 84,98 ; Argon 3 ≥ 1,72 ; Kimi 2 ≥ 0,79 ;
    - avec Kimi : Claude 112,3 ≥ 68,99 ; Astra 83,7 ≥ 69,69 ;
    - sans Kimi : Claude 132,7 ≥ 60,84 ; Astra 65,3 ≥ 54,40.
  - Marge d'appels : 2 × le plan + 5. Bornes : 35, 29 et 23 fiches de trop (calcul). La répétition a été jouée avec 8 fiches par
    proposeur.
- **Source Gu-Krenn** : 19 œuvres. J'ai contrôlé les attributions sensibles contre la pièce, toutes justes :
  - « exploration hacking » pour 2512.07810 (§ 7 p. 25) ;
  - « bruit ajouté aux poids » pour 2604.28182 et 2512.07810 ;
  - « attaquant sans mémoire » pour 2411.17693 (§ 3) ;
  - « moniteur texte » pour 2604.28182 (§ 6.2).
  Je ne vois aucun rapprochement du rédacteur.

## Points demandés

1. **Écarts du § 8** (l. 129-137) : tous **acceptables à déclarer**, aucun n'est bloquant.
   - L'absence de spécification propre est un fait (la question servie dit elle-même la section servie et le format) ; le GO de
     Lazar (R-1149) et la ligne GO-12 couvrent la course.
   - La lecture « par extension » au protocole des mentors du soir est déclarée et renvoyée à conv-audit.
   - L'arrêt par C13 sur un refus de proposeur est une limite du noyau, déclarée.
   - Réserve de forme en CLJ-02.
2. **Opus sans tour préalable** : le risque n'est déclaré que de façon générique (l. 46-47). **Le kit n'a pas de repli sans
   Opus** : les trois configurations ont Opus proposeur, aiguilleur, juge et lecteur. Voir CLJ-01.
3. **K4** : il vient bien de la question (« falsifiable, avec l'expérience qui la tranche, son témoin, et le résultat qui la
   tuerait »). Il est symétrique (« la valeur **ou** une limite ») et ne pousse vers aucune réponse. Réserve mineure en CLJ-04
   sur les exemples de témoin et un axe.

## Constats

### CLJ-01 — majeur — risque de refus d'Opus sous-déclaré, et aucun repli sans Opus

- **Où** : l. 40-47 (§ 2) ; l. 58-61 (§ 3.2) ; trois configurations.
- **Le constat** :
  - Opus tient quatre rôles : proposeur, aiguilleur, juge, lecteur. Aucun tour du collisionneur n'a éprouvé cette question
    (l. 114-115).
  - La pièce partage plusieurs sources et thèmes avec la pièce Scheurer, qu'Opus a refusée (catégorie « cyber ») :
    2510.09462 (injections d'invite contre les moniteurs, solutions piégées, § 2.4) ; portes dérobées (2411.17693, § 1.3) ;
    évasion des moniteurs latents (2609.36490, § 2.2).
  - Elle nomme aussi des bancs « Weapons of Mass Destruction Proxy » et « Virology Capabilities Test » (§ 1.2).
- **Ce que coûte un refus** :
  - Un refus d'Opus proposeur fait tomber C13 : arrêt sans fiche.
  - Trois refus de suite à l'aiguillage donnent le même arrêt.
  - La R-486 interdit de rejouer la question à Opus. Un nouveau départ demanderait donc une variante sans Opus, qui n'existe pas,
    sous l'échéance de 16:00 UTC.
- **Correction** :
  - Minimum : déclarer au § 2 ou au § 7 ce risque précis (sources communes avec la question refusée par Opus, aucun tour
    préalable) et écrire qu'**il n'existe pas de repli sans Opus**.
  - Option recommandée si le temps le permet : ajouter, sous un nom neuf, une variante au modèle du kit Scheurer. Fable y
    remplace Opus comme aiguilleur, juge et lecteur. Les proposeurs seraient Fable, Kimi et Astra (Argon si libre). Puis
    refaire les empreintes, la table et une répétition. C'est sans dépense, et le choix revient à session-depot.

### CLJ-02 — mineur — l'écart n° 4 renvoie à une règle sans source

- **Où** : l. 135 (« au lieu de laisser sa fiche “déclarée absente” (§ 2) »).
- **Le constat** : aucune spécification n'existe pour cette course, et la question ne dit rien des refus. La règle « déclarée
  absente » vient de la spécification Scheurer, et le renvoi « (§ 2) » ne mène nulle part.
- **Correction** : écrire « limite du noyau v56 ; la règle “refus jamais rejoué” vient du message de session-depot de
  14:10 UTC (R-486) ».

### CLJ-03 — mineur — le numéro de GO est connu

- **Où** : l. 31 (`GO-2026-11-03-NN`).
- **Le constat** : la ligne GO-2026-11-03-12 est inscrite sur `main` (`9d40b65d`), 198 USD, kit `ce3dec8a`.
- **Correction** : écrire le numéro réel dans la version scellée.

### CLJ-04 — mineur — juge et axes : deux cadrages hors de la question

- **Juge** (`pieces/consigne-juge-jangfeng-v1.md`, K4) : les exemples de témoin (« boîte noire, organisme bénin ou ligne de base
  calibrée ») viennent de la pièce (2512.07810, 2507.12691), pas de la question. L'effet est faible, puisque les sorties des
  juges sont rapportées à part.
- **Axe** : `comparaison_a_la_boite_noire` (l. 64) n'est pas dans la question (« la valeur… et les limites actuelles »).
- **Correction** : le déclarer au § 3.2 et au § 3.3, comme choix du rédacteur.
