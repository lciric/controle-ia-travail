# Vérification des différences — préenregistrement de la course du banc fermé, brouillon 9 — v1

- **Pièce vérifiée** : `prereg/course-banc-ferme-v1-brouillon9.md`, branche `claude/prereg-course-banc-ferme-v1`, commit `ad96271dc7a3b64c5e3df8aef34fdbd02f48e430`. Empreinte recalculée : `bf8de475cc85624fb75de4b88e78746059806742c527f396dc4b9883f9955781`, égale à son `.sha256` compagnon. Les brouillons 1 à 8 sont inchangés.
- **Contre-lectrice** : la même, `session_01Qi7Gr5LQA3YbKmpEK7DG2D` (Opus 5.5). Pièce de classe A, règle R2.
- **Date** : 21 novembre 2026, vers 19:55 UTC. Refus d'un classifieur : aucun.
- **Objet** : les différences du brouillon 8 avec le brouillon 7, vérifiées dans `prereg/course-banc-ferme-v1-verification-brouillon8-v1.md` (`cc81f6f2…`, accepté, deux restes M1 et M2), puis celles du brouillon 9 avec le brouillon 8, par `diff`, lues en entier.
- **Liste d'arrêt** : les vingt-huit lignes reprises ont été comparées **par programme** à la section 4.2 de la v11 (`af429106…`). Elles sont identiques. La seule ligne changée depuis la v10, « deux passages gardés », est bien celle de la v11.
- **Validateur** : il ne rend que le marqueur du champ n° 19, ce qui est attendu.

## Différences du brouillon 9

| Lieu | Constat | État |
|---|---|---|
| [PS] v11 | Citée avec son verdict (`ea16c756…`, commit `ece1b2d2`). Ses trois changements depuis la v10, vérifiés par `diff`, sont bien ceux que dit le texte. | conforme |
| Liste d'arrêt | Recopiée de la v11 ; la « seconde précision » du brouillon 8 est retirée à bon droit, la pièce le disant elle-même. | conforme |
| D6, lignées | « [PS] ne nomme aucune famille ; l'audit les dit », selon la condition 11 de la v11. | conforme |
| D6, questions | « ni de la tâche » ; le monteur de l'oracle l'atteste à l'addendum O ; sinon, forme à questions identiques avec épreuves refaites, ou nœud. **Cela tient lieu de mon point M2 du brouillon 8**, mieux même : c'est le monteur, qui connaît l'oracle, qui atteste. | conforme ; voir R2 |
| D6, garde 15 | Le mot témoin tombe sous la définition du mot propre. | conforme |
| Nœud 8 | Source précisée par R-4680. | conforme |
| Réserves 4 et 12 | Mises à jour. | conforme |
| [RG] | Cite le brouillon 4 de la répétition et dit l'erreur du « brouillon 3 ». | conforme |

Aucun contenu de mode.

## Restes

**R1 — L'ordre des scellements (mon M1 du brouillon 8, non encore porté).** Le brouillon 9 a été écrit avant ce rapport. Porter l'ordre en quatre temps :
1. le brouillon de la répétition est accepté et son contenu figé ;
2. la course est scellée et cite ce brouillon ;
3. la répétition est scellée et ne diffère de ce brouillon que par le champ R-1, ce qui se vérifie par `diff` et se consigne ;
4. l'addendum B cite la répétition scellée.

Sous cet ordre, le brouillon 4 de la répétition est maintenant **accepté**, avec deux restes à porter. Le brouillon accepté qui servira à l'étape 1 sera donc le brouillon suivant.

**R2 — La comparaison après le retour, en quarantaine.** Le même reste que M1 de ma vérification du brouillon 4 de la répétition (`prereg/repetition-generale-banc-ferme-v1-verification-brouillon4-v1.md`). Si l'oracle de la famille est porté sous une forme à questions identiques, il faut dire qui fait la comparaison à la référence propre à la tâche, et comment. Si c'est un programme seul, dire ce qu'il tranche. Si un modèle y concourt, il est un lecteur du dommage au sens de N-060 v3 et du champ n° 18, et la sortie de la référence vers lui est un nœud. Écrire aussi la règle d'accord des lecteurs sur ce que la forme leur fait rendre.

**R3 — Deux mentions de « la v10 ».** La table des nœuds tranchés (nœud 11) et la ligne du repère de GO-2026-11-21-76 disent encore « la v10 ». Lire « la v11 », comme l'auteur l'a vu lui-même.

## Verdict

**Accepté.** Les différences du brouillon 8, déjà vérifiées, et celles du brouillon 9 sont conformes. La liste d'arrêt est identique à celle de la v11. Trois restes mineurs, R1 à R3, sont à porter avant le scellement définitif.
