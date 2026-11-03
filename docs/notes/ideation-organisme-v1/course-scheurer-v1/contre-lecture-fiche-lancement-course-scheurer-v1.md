# Contre-lecture de la fiche de lancement de la course Scheurer (brouillon 1) — v1

Contre-lecteur neuf (règle R2), sous-agent qui n'a écrit ni le kit ni la fiche. 3 novembre 2026, 14:11 UTC (`date -u`).
Aucun appel payant, aucun réseau, aucune clé, aucun fichier existant modifié. J'ai lu dans un arbre partiel neuf
(`wt-cl-scheurer`, `c4797620`) et extrait les sources de `origin/canal/conv-audit-n04` par `git show`. Seul fichier écrit :
ce rapport (non scellé, non commité).

Objet : `docs/notes/ideation-organisme-v1/course-scheurer-v1/fiche-lancement-course-scheurer-v1-brouillon1.md`,
sha256 `95a9eddc4cdb0cbb5f8f9fb2d95d225f9207f64a4308ed65b931ea8d3cc9dd07` (compagnon vérifié : OK). Configuration de
lancement `sans-opus`, `e6e739d7…`. Les numéros de ligne renvoient à la fiche.

## Verdict

**Scellable après corrections.** Aucun constat bloquant. Deux constats majeurs :
- CLS-01 : la fiche dit qu'aucune spécification n'existe, alors que conv-audit en a scellé une (`97c67ec1…`), et les écarts à
  cette spécification ne sont pas déclarés.
- CLS-02 : la règle de la spécification sur les refus (« la fiche refusée est déclarée absente ») ne peut pas être tenue par
  le noyau v56, et la variante de lancement s'écarte de la spécification pour cette raison.

Tout se corrige dans le texte. La fiche se scelle sous un nom neuf (R12), et l'on joint au kit une copie de la spécification
avec son empreinte. Les points du développeur sont jugés justes (voir « Vérifié conforme »).

## Vérifié conforme

- **Sources** : question `edb1d5f1…`, pièce Scheurer `2d0e60fc…`, nos résultats `d6fa8011…`, protocole `fbbbb520…` et
  n° 419 `75aedf2e…`. Chacune est à l'empreinte de son compagnon sur le canal et identique à l'octet à la copie du kit.
- **Pièces gelées** :
  - Les 50 lignes de la table sont OK par `sha256sum -c`.
  - `table_pieces_gelees_scheurer_v1.py --verifier` donne « conforme : 50 pièces gelées ».
  - Tous les compagnons du kit sont OK, et les empreintes de l'orchestrateur sont conformes sur disque.
  - Le seul marqueur est `<<EMPREINTE_RAPPORT>>`, à la l. 10.
- **Consigne du proposeur** :
  - `--verifier` donne « conforme ».
  - Contrôle indépendant : on y trouve à l'octet, dans cet ordre, la section « La question… », les règles d'intégrité, la
    pièce Scheurer et nos résultats (positions 461 < 1 605 < 2 481 < 12 107).
  - Le texte propre au collisionneur est absent. La consigne fait 19 868 octets.
- **Juge** :
  - La question est reprise à l'octet.
  - K1 à K3 reprennent les trois items du n° 419 dans leur ordre, sans l'originalité.
  - K4 (« une vraie tendance ») vient de la question elle-même et de sa section « Ce qu'on attend » : même mesure d'un modèle à
    l'autre, échelle continue, modèles datés.
  - Aucun item ne pousse vers une réponse.
  - Réserve : le n° 419 a été écrit pour Ibrahim (« Critères du juge de la course Ibrahim »), et le kit l'applique ici par
    analogie. Écrire « par analogie » à la l. 57.
- **Fable remplace Opus comme aiguilleur, juge et lecteur.** C'est juste, et cohérent avec la R-486 et le n° 421 :
  - ne pas reposer la question à l'espèce qui l'a refusée, même reformulée ;
  - un refus d'un rôle de lecture compte comme un échec, et peut arrêter la course sans fiche.
- **Garde lexicale** :
  - Retirer « gemini » et « openai » est juste : la pièce Scheurer nomme « Gemini 3 Pro » et « Gemini 2.5 » (§ 2.1, § 3.3) et
    « Apollo Research et OpenAI » (§ 1.2). Toute fiche qui cite ces travaux serait exclue.
  - Passée par `pole/fiches_v54.trouver` (« prefixe ») sur les consignes, la liste, le vocabulaire du substitut, la question et
    les deux pièces : rien n'est trouvé.
  - Le prix est déclaré.
- **Dépense** :
  - S17 = 237 ≥ 1,2 × 196,89 = 236,27 (calcul), pour la variante au pire cas le plus haut.
  - Plafonds de session, chacun au-dessus du pire cas d'un appel de son rôle : proposeur 3,5 > 3,2647 ; aiguilleur 0,9 > 0,8462
    (Fable) ; juge 0,9 > 0,8513 ; lecteur 0,9 > 0,8485 ; fusion 3,5 > 3,2862.
  - Relais, chacun au-dessus de son pire cas, la somme faisant 237 dans les cinq variantes :
    - `sans-opus` : Claude 169,7 ≥ 104,33 ; Astra 65,3 ≥ 54,40 ; Kimi 2 ≥ 0,79 ;
    - `sans-opus-argon` : Claude 148,3 ≥ 124,70 ; Astra 83,7 ≥ 69,69 ; Argon 3 ≥ 1,71 ;
    - `sans-kimi` : Claude 190 ≥ 83,97 ; Astra 47 ≥ 39,10 ;
    - `avec-opus` : Claude 151,3 ≥ 68,98 ; Astra 83,7 ≥ 69,69.
- **Marge d'appels** :
  - Elle vaut 2 × le plan + 5 dans chaque variante.
  - Bornes recalculées pour `sans-opus` : Claude (203 − 99) / 4 = 26 ; Astra (133 − 64) / 3 = 23. Le minimum, 23, est exact.
  - La répétition a été jouée avec un faux amont à **8 fiches** : course `sans-opus-argon` au bout, code 0, 32 fiches, Claude 155
    appels sur 251. Le correctif est donc éprouvé sur l'artefact (R5).
- **Source Gu-Krenn** : 17 œuvres. Chaque concept est attribué par la pièce à sa source. Je ne vois aucun rapprochement du
  rédacteur et aucun lien venu d'une note de moisson. Une omission mineure, en CLS-04.
- **Fiche** :
  - course non décisive ;
  - mot direct de Lazar cité à la lettre (conforme à R-1149) ;
  - liste d'arrêt complète, avec C13, les refus comme échecs, l'arrêt sans fiche et les codes du lanceur ;
  - échéance de 16:00 UTC ;
  - lecture « par extension » au protocole, déclarée.

## Constats

### CLS-01 — majeur — la fiche nie une spécification qui existe, et les écarts à cette spécification ne sont pas déclarés

- **Où** : l. 15-16 (« aucune spécification de conv-audit pour cette course ») et l. 153 (§ 8.1).
- **La spécification** : conv-audit a scellé `brouillons/ideation-mentors-soir-v1/specification-course-scheurer-v1.md`
  (sha256 `97c67ec1b55e86417b46dea6338a46aba134ac5dedadcfa1d9ae12eea4edc192`, conforme à son compagnon, écrite à 13:47 UTC).
  Elle n'est ni dans `pieces/conv-audit/` ni dans la table.
- **Écarts du kit à cette spécification, par gravité** :
  1. **Majeur — variante de lancement** (spécification § 2 : « comme la course Ibrahim […] cinq espèces si Argon est libre au
     départ, sinon quatre sans Argon »).
     - Le kit n'a **aucune** variante à cinq espèces : aucune ne réunit Opus proposeur et Argon.
     - Il recommande `sans-opus` (trois espèces : Fable, Kimi, Astra), même quand Argon est libre (l. 38-39 : la ligne
       `sans-opus-argon` n'est que « si Argon est libre », sans dire laquelle l'emporte).
     - Ce que j'en pense : l'absence d'Opus est justifiée (CLS-02). Mais quand Argon est libre, `sans-opus-argon` est la
       variante la plus proche de la spécification.
     - Correction : écrire « `sans-opus-argon` si Argon est libre au départ, sinon `sans-opus` ». Déclarer l'écart : Opus
       absent comme proposeur, sur le refus du tour (n° 421) et la R-1149.
  2. **Majeur — règle des refus** : voir CLS-02.
  3. **Mineur — question servie** : la spécification (§ 1) ne sert que la section « La question ». Le kit sert aussi les
     règles d'intégrité, avec la règle des « 1 200 mots par cellule ». C'est déclaré au § 8.2, mais comme un écart à Ibrahim ;
     le dire comme un écart à cette spécification.
  4. **Mineur — rôles de lecture** : « comme la course Ibrahim » met Opus aiguilleur, juge et lecteur ; le kit y met Fable.
     C'est déclaré au § 8.5 ; rattacher cet écart à la spécification.
  5. **Mineur — plafond** : la spécification (§ 3) demande l'« entier supérieur à 1,2 × pire cas du devis ». Le kit applique
     237 à toutes les variantes, à partir du pire cas le plus haut. Pour `sans-opus`, la règle donnerait 192 (1,2 × 159,51 =
     191,41, calcul). La garde est plus large, mais elle reste dans le « pas de plafond » de Lazar. Le déclarer, ou porter un
     plafond par variante.
- **Correction** :
  - Citer la spécification en § 1, chemin et empreinte, et en joindre une copie à l'octet dans `pieces/conv-audit/`, ajoutée à
    la table.
  - Réécrire le § 8 comme une liste d'écarts **à cette spécification**.

### CLS-02 — majeur — « la fiche refusée est déclarée absente » (spécification § 2) est impossible avec le noyau v56

- **Où** : spécification § 2 (R-486). Fiche l. 47-52 et l. 121-126 (§ 5).
- **Le mécanisme** : dans le noyau, un refus est un appel inexploitable.
  - Pour un proposeur, un seul échec fait tomber C13, et la course s'arrête **sans aucune fiche**.
  - Pour un rôle de lecture, trois refus consécutifs ou plus de 25 % d'appels inexploitables donnent le même arrêt.
  - On ne peut donc pas « déclarer absente » une fiche refusée et continuer. Chaque refus d'une espèce arrête tout.
- **Ce que ça implique** :
  - Le choix « sans Opus » est la seule façon de tenir à la fois la R-486 (ne pas rejouer un refus) et une course qui rende
    des fiches. C'est conforme au n° 421 et à la R-1149. Ce n'est pas contourner un refus : la question n'est pas reposée à
    Opus, et le mot de Lazar couvre la suite avec les autres espèces.
  - Le risque reste entier pour Fable, de la même famille qu'Opus. Fable tient cinq rôles dans `sans-opus` : proposeur,
    aiguilleur, juge, lecteur, metteur. La pièce parle beaucoup de portes dérobées et d'injections (§ 3.3, § 3.4), et le refus
    d'Opus était classé « cyber ».
- **Correction (texte)** :
  - Déclarer l'écart à la spécification § 2 : la règle « fiche refusée déclarée absente » ne peut pas être tenue, et tout
    refus d'une espèce arrête la course sans fiche.
  - Dire au § 7 si Fable a répondu sans refus au tour du collisionneur sur cette question. La l. 28 dit qu'Opus seul a refusé :
    c'est le meilleur indice dont on dispose.
  - La variante `sans-opus-juges-opus` fait lire toutes les fiches à l'espèce qui a refusé. Dire qu'elle n'est pas à lancer
    sans un mot de Lazar.

### CLS-03 — mineur — en `sans-opus`, le contrôle d'Opus reste un point de rupture

- **Où** : l. 51-52 ; `lancer-course-scheurer-v1.sh` l. 153 (`MODELES="claude-fable-5-1 claude-opus-5-5 gpt-6-astra"`).
- **Le constat** : le contrôle (« OK », sans la question) ne pose pas la question refusée. Mais s'il échoue (indisponibilité),
  il empêche une course où Opus ne joue aucun rôle (code 3).
- **Correction** : le dire au § 5. Le changement de code n'est pas nécessaire ce soir.

### CLS-04 — mineur — source Gu-Krenn : une distinction que fait aussi 2412.04984

- **Où** : `pieces/source-gu-krenn-scheurer-v1.json`, œuvre `manigance-2412.04984`.
- **Le constat** :
  - La pièce (§ 1.1, p. 15) y oppose déjà disposition et capacité : « aversion de disposition […] même s'ils en ont la
    capacité ».
  - « capacité et propension mêlées » n'est porté que par 2603.01608. Les paires « capacité et propension mêlées » × concepts
    de 2412.04984 (par exemple « sous-performance stratégique ») sortent donc « jamais reliées ».
- **Correction** : ajouter le concept à `manigance-2412.04984` dans une version suivante, ou le déclarer au § 3.4.
