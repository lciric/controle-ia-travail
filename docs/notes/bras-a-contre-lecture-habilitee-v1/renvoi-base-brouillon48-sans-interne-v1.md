# Renvoi de la base, brouillon 48 — relecture habilitée de M-6 et M-7 — sans interne — v1

- **Heure** : 2026-11-22T14:31:48Z (`date -u`).
- **Mandat** : `mandat-lecteur-habilite-module-v11-et-renvoi-base-v1.md` (`7854c2e5…`), partie 2, sur le mot de la mère.
- **Accès** : R-4914.
- **Texte lu** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon48.md`, branche `claude/pensive-bardeen-1fv7hw`, commit `abfa2d8d7`, `838654d6faf4442286dac83046832729a292c3e2388f5b0844f20785f39dc2c3` (vérifiée). Seules les lignes 587, 1034 et 1062 sont lues, et la seule citation de la préparation à la ligne 1471.
- **Comparé à** : ma vérification du brouillon 47 (`renvoi-base-brouillon47-sans-interne-v2.md`, verdict « vérifié »).

## Ce qui change du brouillon 47 au brouillon 48

Seules changent les lignes 1, 3, 587, 1034, 1062 et 2543. Aux trois lignes de M-6 et M-7, chaque changement est un **ajout pur** : aucun mot n'est retiré.

- **Ligne 587 (M-7, énoncé de l'hypothèse)** : l'effet minimal d'intérêt de 0,10 entre dans l'énoncé (« confirmée » au-delà, « réfutée au sens de cette mesure » quand une hausse d'au moins 0,10 est exclue). **Cohérent** : elle porte sur la mesure du désappariement par les lecteurs, non sur la base ni sur les moniteurs. Aucun point du renvoi n'en dépend.
- **Ligne 1034 (ligne B9)** : une phrase de plus quand la hausse est aussi établie sous l'effet minimal. **Cohérent** : même raison.
- **Ligne 1062 (M-6, déclencheurs de l'audit de symétrie)** : ajoute le déclencheur « au moins une dose en C4 », pendant de C6, avec le même contenu, côté habilité compris. **Cohérent** : il ajoute un audit et ne change ni le module, ni la base, ni ce qu'ils lisent. L'audit du côté habilité qu'il déclenche se fait sur l'instrument vérifié tel quel.

**Le renvoi de la base reste « vérifié »** au brouillon 48 pour ces trois lignes.

## Ligne 1471 (à corriger au brouillon 49)

Elle est inchangée au brouillon 48 ; le défaut mineur demeure. **Couple exact demandé**, un seul remplacement dans la ligne 1471.

Ancien :

`` `src/controle_ia/organismes_discrets/bras_a_v2_habilite_preparation/preparation_des_lectures_v1.py`, `72d2216747c102bc5dca12227bb6e6648c20a121b72edcaefa51c817ad037dae`, commit `2ee2a8cf` (fichier non ouvert par moi) ``

Nouveau :

`` `src/controle_ia/organismes_discrets/bras_a_v2_habilite_preparation/preparation_des_lectures_v3.py`, `c0021298c21d027a713b1947d2668ac928f2a856b1a696686dd35b83a9515c45`, commit `e13ed9282` de la branche `claude/bras-a-habilite-developpeur-v1` (fichier non ouvert par moi ; version inscrite par le module des autres moniteurs en version 11) ``

Le commit `e13ed9282` est celui où la préparation v3 entre sur la branche habilitée, à cette empreinte. Je relirai la ligne au brouillon 49.

## Verdict

**Cohérent** : M-6 et M-7 ne touchent aucun point du renvoi de la base, qui reste « vérifié ». Il reste une seule réserve, la correction de la ligne 1471 au brouillon 49.

Cette pièce ne dépense rien et n'autorise rien.
