# Contre-lecture de la fiche de lancement de la course Colognese et Ward Q2 (brouillon 1) — v1

Contre-lecteur neuf (règle R2), sous-agent qui n'a écrit ni le kit ni la fiche. 3 novembre 2026, 14:19 UTC (`date -u`).
Aucun appel payant, aucun réseau, aucune clé, aucun fichier existant modifié. J'ai lu dans un arbre partiel neuf
(`wt-cl-colognese`, `3e9cb48a`) et extrait les sources de `origin/canal/conv-audit-n04` par `git show`. Seul fichier écrit :
ce rapport (non scellé, non commité).

Objet : `docs/notes/ideation-organisme-v1/course-colognese-ward-q2-v1/fiche-lancement-course-colognese-ward-q2-v1-brouillon1.md`,
sha256 `ba567aa9457c64bc5ecbccefdc7bcc0476e74094879c97bba80db0dcc3b05924` (compagnon vérifié : OK). Configuration de
lancement à cinq espèces, `63e48ad9…`. Les numéros de ligne renvoient à la fiche.

## Verdict

**Scellable tel quel.** Aucun constat bloquant, aucun majeur. Trois constats mineurs, à corriger dans le texte si c'est bon
marché ; aucun ne fausse la course. Les cinq points du développeur sont jugés justes.

## Vérifié conforme

- **Sources** : spécification `711fcf52…`, question `06d83795…`, pièce `7533e4b5…`, nos résultats `d6fa8011…`, protocole
  `fbbbb520…` et n° 419 `75aedf2e…`. Chacune est à l'empreinte de son compagnon sur le canal et identique à l'octet à la copie du
  kit. La spécification est dans le kit et dans la table (pas de répétition du défaut Scheurer).
- **Pièces gelées** :
  - Les 49 lignes de la table sont OK par `sha256sum -c`.
  - `table_pieces_gelees_colognese_v1.py --verifier` donne « conforme : 49 pièces gelées ».
  - Tous les compagnons du kit sont OK, et les empreintes de l'orchestrateur sont conformes sur disque.
  - Les quatre empreintes citées en § 4 et § 7 sont exactes : devis, course à blanc, mutations, répétition.
  - Le seul marqueur est `<<EMPREINTE_RAPPORT>>`, à la l. 10.
- **Consigne du proposeur** :
  - `--verifier` donne « conforme ».
  - Contrôle indépendant : on y trouve à l'octet, dans cet ordre, la section « La question, telle que les mentors la posent »
    (avec la ligne du billet), les règles d'intégrité, la pièce Colognese et Ward, et nos résultats (positions 474 < 917 < 1 802
    < 14 558).
  - Le texte propre au collisionneur est absent. La consigne fait 22 158 octets.
- **Juge** :
  - La question est reprise à l'octet.
  - K1 à K3 reprennent les trois items du n° 419 dans leur ordre, sans l'originalité.
  - K4 (« ancrée dans le billet ») vient des demandes 1 à 3 de la question.
  - Aucun item ne pousse vers une réponse.
- **Rôles comme Ibrahim**, conformes à la spécification § 2 : aiguilleur Opus ; juges et lecteurs Opus et Astra ; metteur
  Fable. Le tour de cette question n'a eu aucun refus (R-1142 : panne d'OpenAI, reprise ; R-1145 : 12 cellules valides). Garder
  Opus est donc justifié.
- **Aiguilleur** au niveau Kirchner v2. La pièce a déjà remplacé par leur classe les trois extraits de code de triche (en-tête de
  la pièce).
- **Garde lexicale** :
  - Retirer « openai » est juste : la pièce écrit « (OpenAI) » (§ 2, 2503.11926). Toute fiche qui cite ce travail serait exclue.
  - « gemini » est gardé, et la pièce ne l'emploie pas.
  - Passée par `pole/fiches_v54.trouver` (« prefixe ») sur les consignes, la liste, le vocabulaire du substitut, la question et
    les deux pièces : rien n'est trouvé.
- **Dépense** :
  - S17 = 198 ≥ 1,2 × 164,64 = 197,57 (calcul).
  - Plafonds de session, chacun au-dessus du pire cas d'un appel de son rôle : proposeur 3,5 > 3,2722 ; aiguilleur 0,4 > 0,3386 ;
    juge 0,9 > 0,8489 ; lecteur 0,9 > 0,85 ; fusion 3,5 > 3,2864.
  - Relais, chacun au-dessus de son pire cas, la somme faisant 198 dans les trois variantes :
    - cinq espèces : Claude 91,0 ≥ 77,14 ; Astra 102,0 ≥ 84,98 ; Argon 3 ≥ 1,72 ; Kimi 2 ≥ 0,79 ;
    - avec Kimi : Claude 112,3 ≥ 68,99 ; Astra 83,7 ≥ 69,69 ;
    - sans Kimi : Claude 132,7 ≥ 60,84 ; Astra 65,3 ≥ 54,39.
  - Étape « proposition » : plafond 8,67 contre 8,63 avec la formule des commandes (caractères / 3, calcul). La marge est mince,
    mais suffisante.
- **Marge d'appels** :
  - Elle vaut 2 × le plan + 5.
  - Bornes recalculées : cinq espèces, Claude (301 − 148) / 4 = 38 et Astra (205 − 100) / 3 = 35 ; avec Kimi 29 ; sans Kimi 23.
    Elles sont exactes.
  - La répétition a été jouée avec un faux amont à **8 fiches** : code 0, 40 fiches, Claude 188 sur 301, Astra 130 sur 205.
- **Règle des refus** : la limite du noyau (un refus de proposeur fait tomber C13 et arrête la course sans fiche) est déclarée
  (l. 40-42, § 5).
- **Source Gu-Krenn** : 15 œuvres. Chaque concept est attribué par la pièce à sa source. Je ne vois aucun rapprochement du
  rédacteur. Le lien que la pièce fait elle-même (§ 3.6, avec R7) n'est pas codé, ce qui est juste. Voir CLC-02.
- **Fiche** :
  - course non décisive ;
  - mot direct de Lazar cité à la lettre (conforme à R-1149) ;
  - variante de lancement conforme à la spécification (cinq espèces si Argon est libre, sinon quatre) ;
  - liste d'arrêt complète ;
  - échéance de 16:00 UTC ;
  - lecture « par extension » au protocole, déclarée.

## Constats

### CLC-01 — mineur — l'écart n° 5 renvoie à une règle que cette spécification ne porte pas

- **Où** : l. 142 (§ 8.5 : « au lieu de laisser sa fiche “déclarée absente” (§ 2) »).
- **Le constat** : la spécification Colognese et Ward (§ 2) ne dit rien des refus. La règle « déclarée absente » (R-486) est
  celle de la spécification Scheurer.
- **Correction** : écrire « limite du noyau v56, déclarée (la spécification ne traite pas des refus) », ou retirer l'écart.

### CLC-02 — mineur — source Gu-Krenn : « rappel du moniteur » et « taux de capture » désignent la même grandeur

- **Où** : `pieces/source-gu-krenn-colognese-v1.json`. « rappel du moniteur » est porté par 2503.11926 seul, et « taux de
  capture » par le billet seul.
- **Le constat** : le billet mesure exactement un rappel, la part de triches attrapées (§ 3.2). Les paires « rappel du moniteur »
  × concepts du billet (« entraînement de caractère », « triche silencieuse »…) sortent donc « jamais reliées » alors qu'elles
  le sont.
- **Correction** : le déclarer au § 3.4. Dans une version suivante, ajouter « rappel du moniteur » au billet.

### CLC-03 — mineur — K4 demande une section du billet que le juge ne voit pas

- **Où** : `pieces/consigne-juge-colognese-v1.md`, K4. Fiche l. 50-52.
- **Le constat** : le juge ne voit que la question. Il ne peut pas vérifier qu'une section citée du billet existe, ni qu'un
  résultat lui est bien attribué.
- **Correction** : ajouter K4 à la phrase des l. 51-52 (« il ne peut pas vérifier les identifiants ni… »).
