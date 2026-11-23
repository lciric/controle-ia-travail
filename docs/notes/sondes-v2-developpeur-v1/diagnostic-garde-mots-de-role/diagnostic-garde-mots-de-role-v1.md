# Diagnostic de la garde des mots de rôle de la note des effectifs (v1)

- **Pour** la mère (mandat F2, R-5204), avant toute relance de la note. **Écrit par** le développeur des sondes v2, session_016QhUrtqKazbonFiVhXMm3R (Opus 5.5), 2026-11-23T23:24Z. Classe C : c'est une proposition ; la correction retenue sera de classe B. **Aucun résultat.**
- **Lu** : `src/controle_ia/sondes_v2/formats_v1.py` (8351e49b4), lignes 28, 77 à 86, 107 et 136 ; `spec-note-des-effectifs-v2.md`, § 1 et § 4 ; R-5200 dans `registres/decisions.md` ; les seuls motifs de noms de séries écrits dans les documents de code du barreau 5 sur main (`rapport-developpeur-code-lecture-v3.md`, ligne 51 : « `nu`, les noms opaques de la table, les `A<k>-<membre>` ; facultatives : `ancre-<nom>` et `propre-A<k>-saboteur` »). **Non lus** : l'attestation que le lecteur habilité a écrite, la liste de garde, tout manifeste ou toute activation.

## Ce qui arrête
1. `formats_v1.py`, ligne 136 : tout nom de série qui contient « saboteur », « jumeau », « paire » ou « famille » arrête. La ligne 107 applique la même règle aux clés de toute la section des activations.
2. Le format du barreau 5 nomme par construction des séries qui portent un rôle **public** : les séries propres `propre-A<k>-saboteur` (épisodes d'évaluation du saboteur, hors des clés communes, que la lecture ne lit pas) et, selon le cas, des `ancre-<nom>` et des `A<k>-<membre>`. La garde ne peut donc jamais passer sur ce format. Elle a été écrite pour l'aveuglement des seules paires opaques du test sur les adaptateurs jumeaux, mais elle frappe tous les noms.
3. Le lecteur habilité s'est arrêté comme le veut la spécification, § 1 : son arrêt est juste, et c'est l'outil qui ne sait pas distinguer.

## Ce qui reste à protéger
L'aveuglement porte sur le rôle (saboteur ou jumeau) des adaptateurs aux **noms opaques** de la table de l'ouvreur. Un nom public qui dit « saboteur » ne révèle rien sur ces paires-là, **à une condition** : qu'aucune série à nom public ne soit un membre d'une paire du test. Je ne peux pas vérifier cette condition sans lire ce qui m'est cloisonné.

## Options
- **A (recommandée, confiance 0,7) — séries publiques comptées, non nommées.** Par un erratum de la spécification (classe B) et du chargeur, la note porte un champ `series_publiques` : `{"propre": n, "ancre": n, "autres_a_nom_public": n}`. Elle ne donne que des comptes, et le lecteur habilité atteste qu'aucune série publique n'est membre d'une paire opaque. La garde reste entière sur `series` (noms opaques, `nu`, adaptateurs de la table) et sur les clés.
  - Avantage : aucun nom à rôle n'est écrit, et la garde ne s'affaiblit pas.
  - Inconvénient : il faut changer la spécification et le code ; le programme de l'épreuve n'en a pas besoin, puisqu'il ne lit que les cases.
- **B — motifs exemptés dans le code** (`^propre-A\d+-saboteur$`, `^ancre-`, `^A\d+-`).
  - Avantage : simple.
  - Inconvénient : si les `A<k>-<membre>` sont des membres de paires du test, la note écrirait un rôle aveugle en clair. Ne le faire qu'après que le concepteur a confirmé la condition ci-dessus.
- **C — retirer la garde des noms.** Rejetée : plus aucune défense contre un nom opaque mal choisi.

## Questions pour la mère, avant toute relance
1. Option A, B ou C ?
2. Avec A ou B : qui atteste qu'aucune série à nom public n'est membre d'une paire opaque du test ? Ma proposition : le lecteur habilité neuf, par les noms seuls, et le concepteur, sur la table de l'ouvreur, après le verdict.
3. Le code n'est corrigé qu'après ton mot, puis contre-lu par un autre modèle (classe B).
