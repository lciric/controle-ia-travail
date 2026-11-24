# Erratum 1 à la note des écarts des projets de mandats (lecture des sondes sur le saboteur à budget, barreau 8)

Pièce de travail (classe C), écrite le 2026-11-24 entre 16:17Z et 16:28Z (heures lues par `date -u`) par le rédacteur des projets de mandats (sous-agent Opus 5.5 de la conductrice du côté des moniteurs). Elle corrige, sans la réécrire (règle R12), la note `ecarts-brouillon2-vers-v3-v1.md` (`f31cd0073e958f8ccf8cc2c3a16f05c0dfbf1f683a1894dc4c78ceb4249568be`), d'après la contre-lecture `contre-lecture-mandats-v3-brouillon1-v1.md` (`e9c3e339f0b19e430511022147c6c8f65f019160b5a81748ebc636b9ecca1251`), remarques m-1, m-11 et m-12, contrôlées sur le code. Cet erratum prime sur la note aux points qu'il nomme.

## 1. Heures d'écriture fausses (remarque m-1)

- La note dit « écrite le 2026-11-24 vers 17:05Z ». **Faux** : elle a été écrite entre 15:45Z et 15:58Z environ (fichier daté de 15:57Z, scellé à 15:58Z), avant même la contre-lecture (16:05Z à 16:20Z). Lire : « écrite le 2026-11-24 entre 15:45Z et 15:58Z ».
- Même faute, constatée ici sans réécrire les pièces, dans les en-têtes des trois projets de mandats version 3, brouillon 1, qui sont remplacés par les brouillons 2 : lecteur « vers 16:40Z », juge « vers 16:50Z », auditeur « vers 17:00Z » ; lire, pour les trois, « entre 15:45Z et 15:58Z ». Les heures des brouillons 2 et de cet erratum sont lues par `date -u`.

## 2. Point 1 de la section « Points entre les textes et le code » : retiré (remarque m-11)

La note voyait une contradiction entre la notice version 7, ligne 94 (« une relecture arrêtée par une garde est écrite comme défaut D3 ») et le texte scellé, ligne 401 (D3 = « essai A0 non reproduit »), et supposait qu'une relecture des gardes r6 ou r7 arrêtée relèverait de D2. **C'est faux.** Dans le code (`audit_mecanique`, lignes 2652 à 2719, lu après la note) : un recalcul r6 ou r7 non reproduit ne s'arrête pas, il est constaté dans `recalculs_non_reproduits` et va au défaut D2 (ligne 2684 ; `garde_de_reception`, lignes 1411 et 1441) ; une relecture arrêtée ne vient que du recalcul de la lecture (`calculer_lecture`, ligne 2691), qui rejoue l'essai de la chaîne : l'essai n'est alors pas reproduit, ce qui est le défaut D3 à sa lettre (ligne 2695). Il n'y a pas de contradiction. Le mandat de l'auditeur, brouillon 2, recopie ce défaut tel quel, cause comprise, avec l'issue AU-a.

## 3. Point 2 de la même section : faux (remarque m-12)

La note dit : « Une seconde entre la ligne de lecture et l'audit […] aucun contrôle visible dans `_commande_audit` ». **Faux.** `_commande_audit` (ligne 3068) appelle `ouvrir_le_code` avec la clé `LECTURE-SONDES-IIB` exigée ; `ouvrir_le_code` (ligne 2867) appelle `lire_registre_propre`, qui refuse en `[5]` toute ligne exigée qui n'est pas strictement antérieure, à la seconde, à l'instant d'ouverture (lignes 1532 et 1533 : « pas strictement antérieure à l'ouverture »). Le code contrôle donc la seconde d'écart avant l'audit. Le mandat de l'auditeur, brouillon 2, le dit (étape 1).

## Ce qui ne change pas

Les tables des écarts des trois mandats et les points 3, 4 et 5 de la section « Points entre les textes et le code » restent tels quels.
