# Vérification des corrections du brouillon 23 du texte neuf du bras A des organismes discrets — v1

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`). J'ai contre-lu le brouillon 21 et vérifié les corrections du brouillon 22. Je juge, je ne corrige pas.
- **Texte** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon23.md`, `ed7823af1377c55cc3ea911e7dbf2c0c7a6872010b846e8ba54e33d81c3f2c2e`.
- **Pièces jointes** : la note (`f2963374…`) et les fiches (`f20abfed…`). Les compagnons sont vérifiés.
- **Méthode** :
  - différence phrase par phrase entre les brouillons 22 et 23, faite par programme ;
  - lecture de tout ce qui, dans le texte, dépend d'un arrêt ou d'une issue non prononcée. Les lignes trouvées par recherche de « A17 », « non lue », « non prononcée », « lecture de la discrétion » et « arrête la lecture » ont été lues en contexte. S'y ajoutent les sections 6.3 (m) et (n), 7.5, 7.7, 8.5, 8.6, 10 et la convention du fichier de l'étape (m).

## Verdict : **engageable après corrections**

- Le défaut bloquant B-1 est réglé :
  - la ligne A17 est revenue à son texte du brouillon 21, plus la précision de GO-2026-11-19-70 (vérifié caractère par caractère) ;
  - la section 7.5 est intacte ;
  - l'issue d'un arrêt de la lecture de la discrétion est posée à Lazar, sans défaut, sous trois rédactions écrites en entier.
- Les défauts C et M de la vérification du brouillon 22 sont tenus, sauf M-4, qui relève de la session qui orchestre.
- Il reste deux défauts à corriger dans le texte, sans fiche à poser :
  - ce que rend le programme qui refuse est dit de quatre façons (C-1) ;
  - la règle générale de 8.5 rendrait « non opposables » les résultats d'un arrêt, ce qui contredit les rédactions (b) et (c) (C-2).
- **Les fiches 9 à 12 et le rappel peuvent partir à Lazar tels quels.** Aucune ne l'induit en erreur sur ce qu'il choisit. La retouche de M-1 est souhaitable, pas nécessaire.

## 1. Défauts de la vérification du brouillon 22

| défaut | état | endroit |
|---|---|---|
| B-1 livraison refusée rangée sous la ligne A17 | **tenu** | L'événement est retiré de la ligne A17 (ligne 827). En 6.9 (lignes 703 à 711), le nœud est ouvert, avec ce qui est commun aux trois rédactions et les rédactions (a), (b) et (c). La rédaction (a) dit bien, par 7.5, « non prononcée : lecture invalidée par la liste d'arrêt ». Le point 21 et la fiche 12 sont sans défaut. La phrase « le résultat principal, déjà scellé, reste » a disparu. Les deux arrêts d'une anomalie (intervalle impossible, rédaction (c) ; moniteur non ajustable, rédaction (b)) renvoient au point 21. |
| C-1 garde du motif « moniteur appris non ajustable » | **tenu** | 8.4, ligne 949 : un cas sain et un artefact par rédaction, et l'artefact « compte des lectures sous ce motif absent ». |
| C-2 statut et note sur la ligne A17 | **tenu** | Le statut dit l'extension faite au brouillon 22 et son retrait ; la note retire la réserve 1 du brouillon 22. |
| M-1 artefact du cas B | **tenu** | 8.4, ligne 946. |
| M-2 défaut gardé par la fiche 9 | **tenu** | Ligne 1198 : il était déjà posé ; l'option (a) est celle du module ; les deux options ne se séparent qu'à 20 exactement. |
| M-3 contre-lecture 11 et vérification | **tenu, sous réserve** | Entrée « Contre-lecture 11 », ligne 1961 : la vérification est inscrite avec son chemin et son empreinte (justes). La mention « Confirmée par la session qui orchestre » est écrite par le rédacteur : la session doit s'assurer qu'elle est vraie. |
| M-4 compte des fichiers cloisonnés | **tenu en partie** | Renvoyé à la session qui orchestre, qui doit le consigner. Quatorze lignes de la table d'en-tête gardent une empreinte héritée que personne n'a vérifiée. |

## 2. Réserves du rédacteur

**(3) Le programme qui refuse ne rend que la garde, la clé et le cas, jamais une valeur de la livraison.** Ce n'est **pas une règle de jugement** : la garde ne change aucun état, aucune issue, aucun seuil. Elle limite ce qui sort d'une livraison refusée, donc l'occasion de retouche avant une livraison refaite, et elle est éprouvée en 8.4 (artefact : « une valeur de la livraison refusée dans une sortie du programme »). Je la garde. Son contenu est cependant dit de façon incohérente : voir C-1.

**(4) Ni 7.5 ni la ligne A17 ne renvoient au point 21.** Ce n'est pas nécessaire pour la justesse :
- 6.9 dit qu'« aucune des deux n'est touchée d'ici le mot de Lazar » ;
- la rédaction retenue y ajoutera l'événement.

Je recommande pourtant (M-3) deux mesures :
- un renvoi d'une ligne, marqué « nœud ouvert, point 21 », en 7.5 (issue « non lue ») et à la ligne A17. Un lecteur de 7.5 seule, par exemple l'agent du verdict à l'étape (o), qui applique les tables gelées, ne verrait pas la question sans lui ;
- une mention à la case « nœuds » de 13.1 : le mot de Lazar sur le point 21 se porte en 7.5 ou à la ligne A17, et à la section 10. Sinon, rien n'oblige à écrire l'événement au scellement, et le validateur ne le verrait pas.

**(5) Sections non relues.** J'ai lu moi-même tout ce qui dépend d'un arrêt ou d'une issue non prononcée. Je n'y trouve aucune autre conséquence cachée de la gravité de B-1. Deux points restent à écrire :
- **8.5** dit, pour « tout arrêt », des résultats partiels « non opposables » (C-2) ;
- **la section 10** (replis écrits d'avance) n'a pas de ligne pour la livraison refusée, alors qu'elle en a une pour « Renvoi de la base non vérifié : la discrétion n'est pas lue ; le désappariement seul est rapporté » (C-2).

Les autres passages sont cohérents avec les trois rédactions :
- les autres emplois de A17 (prise de la distillation non calculable, ancres, lots d'épreuve, événements de 8.3) ;
- 7.7 (« les issues de 7.5 sont permises telles qu'écrites ») ;
- 8.6 (une livraison refaite n'est ni une redemande ni une reprise au sens de 8.6 : elle passe par le mot de Lazar) ;
- la convention du fichier de l'étape (m) (ligne 155 : discrétion « non lue », rien ne vient après) ;
- 7.6 (sans table C, l'audit de discrétion ne se déclenche pas).

## 3. Défauts à corriger

**C-1. Ce que rend le programme qui refuse est dit de quatre façons.**
- **Endroits** :
  - 6.9, ligne 705 : « ne rend que le nom de la garde, de la clé et du cas en défaut, jamais une valeur de la livraison » ;
  - 8.4, ligne 950 : « la garde, la clé et le cas, rien d'autre » ;
  - fiche 12, enjeu : « ne rend que le nom de la garde et de la clé en défaut » (sans le cas) ;
  - table des formes, cas E, rédaction (c), ligne 711, colonne « ce qui est rapporté » : « l'événement, avec **le moniteur, la dose et le motif** » ;
  - note du brouillon 23, partie 6, point 3, pour le code : « la garde, la clé, le cas et l'étape ».
- **Pourquoi** :
  - Le `motif` est une valeur de la livraison ; le moniteur et la dose en sont des champs.
  - « Clé » peut se lire comme le nom du champ ou comme l'identifiant de la lecture (moniteur, dose).
  - Le code de la version 5 et son essai (« aucune valeur de la livraison dans la sortie ») ne peuvent pas satisfaire à la fois la ligne du cas E et la ligne 950.
  - C'est une garde (R5), pas une règle de jugement.
- **Ce qui le réglerait** : une définition unique, écrite une fois en 6.9 et reprise en 8.4, dans la fiche 12 et dans la ligne du cas E. Elle dirait :
  - ce qui sort : nom de la garde, nom du champ, lettre du cas, étape, et, si on le veut, moniteur et dose comme identifiants ;
  - ce qui ne sort jamais : aucun nombre (aire, valeur p, compte, borne, rang) et aucune valeur de `motif` ni de `calculable`, ou bien le `motif` admis expressément.

**C-2. Sous les rédactions (b) et (c), la règle générale de 8.5 et la section 10 ne sont pas accordées.**
- **Endroits** :
  - 8.5, « Action associée à tout arrêt » : « résultats partiels scellés et marqués non opposables, reprise par nœud » ;
  - section 10, qui a un repli pour le renvoi de la base non vérifié, mais aucun pour une livraison refusée ;
  - 6.9, « Commun aux trois rédactions », qui renvoie à 8.5 pour le versement seul.
- **Pourquoi** : un arrêt de la lecture de la discrétion est un arrêt de la liste d'arrêt. Lue à la lettre, 8.5 marque « non opposables » les résultats partiels de la course, ce qui peut se lire comme les tables A et B. Sous les rédactions (b) et (c), cela contredit « les tables A et B et les autres issues de 7.5 restent prononcées ». C'est le même genre de conséquence cachée que B-1, en moins grave : la rédaction (b) dit expressément le contraire, et l'agent du verdict suivrait 6.9. Il faut fermer la porte.
- **Ce qui le réglerait** :
  - dans « Commun aux trois rédactions » (ou dans (b) et (c)), une phrase : « de 8.5 ne s'appliquent que le versement et la consignation ; sous (b) et (c), seuls la livraison refusée et, sous (c), les grandeurs de l'étape (n) sont non opposables ; les tables A, B et, sous (c), C ne le sont pas » ;
  - une ligne de la section 10 portée par la rédaction retenue.
- C'est un accord de texte qui ne change aucune option ; pas de fiche.

## 4. Mineurs

- **M-1. Fiche 12, option (a).** Avantage : « aucune lecture reprise après que des nombres ont été rendus ». La même option dit « reprise sur un mot de Lazar » ; sous la ligne A17, la reprise par nœud existe aussi. L'avantage réel est « aucune reprise sans nœud, et rien de prononcé d'ici là ». La phrase favorise l'option non recommandée, donc elle ne fausse pas la recommandation, mais elle est à corriger mot pour mot au texte et dans la fiche.
- **M-2. Frontière entre les étapes (m) et (n), sous la rédaction (c).** La rédaction (c) dit : l'étape (n) « ne porte que … le fichier des scores par unité et l'aire conditionnelle ». Or 6.3 (n) range aussi à cette étape les grandeurs des cinq moniteurs à la dose ¼ et aux doses hors de la table B8, qui viennent de la livraison de l'étape (m). Il faut écrire que toutes les gardes sur la sortie de la lecture commune jouent à la réception, à l'étape (m), avant le fichier de cette étape (« reçue entière ou refusée entière »). Ainsi un écart à la dose ¼ ne pourra pas être lu comme un arrêt de l'étape (n), qui garderait la table C.
- **M-3. Réserve 4.** Renvoi d'une ligne en 7.5 et à la ligne A17, et mention dans la case « nœuds » de 13.1 (partie 2 ci-dessus).
- **M-4. Ordre physique des fiches.** Le fichier conseille de lire la fiche 12 d'abord, mais la place en dernier. On peut la mettre en tête du fichier ou laisser tel quel : le conseil est écrit en tête.

## 5. Défauts neufs

Aucune règle de jugement n'est changée sans fiche. Ce que le brouillon 23 change :
- l'issue d'un arrêt (ouverte, fiche 12) ;
- la garde « aucune valeur » (non une règle de jugement, voir la partie 2) ;
- les gardes de 8.4 ;
- le libellé des fiches.

Les seuls défauts neufs sont C-1 (introduit au brouillon 23), M-1 et M-2.

## 6. Les fiches, lues comme un paquet

| fiche | format | loyale | autonome | conséquence d'un arrêt |
|---|---|---|---|---|
| 9, seuil de 1 % | oui ; défaut (a), échéance d'origine, écart justifié | oui | oui | « selon la réponse [au point 21], ou bien plus aucune hypothèse n'est prononcée pour la course entière, résultat principal compris, ou bien la discrétion seule reste « non lue » et le résultat principal demeure » |
| 10, intervalle impossible | oui ; trois options ; aucun défaut | oui | oui | même phrase, mot pour mot |
| 11, moniteur non ajustable | oui ; conditionnelle ; aucun défaut | oui | oui | même phrase, mot pour mot |
| 12, issue d'un arrêt | oui ; trois options ; aucun défaut, justifié (« peut atteindre l'hypothèse principale ») | oui, sauf M-1 | oui | c'est elle qui la fixe ; ses options (b) et (c) se confondent pour un arrêt à l'étape (m) |
| rappel, schéma de permutation | inchangé depuis le brouillon 22 (vérifié par différence) | oui | oui | sans objet |

- **La conséquence se lit-elle de la même façon partout ?** Oui. Les fiches 9, 10 et 11 portent la même phrase. Elle est juste parce que leurs arrêts surviennent tous à l'étape (m), où les options (b) et (c) de la fiche 12 coïncident ; elle ne cite donc que deux issues sur trois, à bon droit.
- **L'ordre conseillé, fiche 12 d'abord, est-il bon ?** Oui : la fiche 12 fixe le coût des options d'arrêt des fiches 10 et 11 et de l'option (b) de la fiche 9. Je conseille ensuite les fiches 10, puis 9, puis le rappel. La fiche 11 peut attendre la réponse du développeur habilité, puisqu'elle tombe si la réponse est non : l'envoyer maintenant ne nuit pas, mais elle demande à Lazar de juger un cas qui peut ne pas exister.
- **Contrôle par programme** : les fiches 9 à 12 (6, 7, 7 et 7 puces) sont des sous-chaînes exactes de la section 12, qui porte les points 1 à 21 dans l'ordre.
- **Peuvent-elles partir telles quelles ?** **Oui.** M-1 est une retouche de loyauté mineure, au bénéfice de l'option non recommandée. C-1 touche une phrase de l'enjeu de la fiche 12 (« la garde et la clé »), sans conséquence sur le choix.

## 7. Intégrité (vérifiée par programme)

| contrôle | résultat |
|---|---|
| brouillons 20, 21 et 22 intacts | `b076e3f9…`, `8d834631…`, `ade786eb…` : compagnons vérifiés |
| brouillon 23, note, fiches | `ed7823af…`, `f2963374…`, `f20abfed…` : compagnons vérifiés |
| citations à la lettre du brouillon 20 | les 935 passages sont tous retrouvés ; les quinze lignes d'origine du point 17 sont intactes |
| citations du brouillon 22 | 1 079 passages ; un seul manque, « lecture invalidée par la liste d'arrêt », tiré de la phrase retirée du brouillon 22, et non une citation transmise : conforme à ce que déclare la note |
| ligne A17 | égale à celle du brouillon 21, plus la seule précision de GO-2026-11-19-70 |
| section 7.5 | identique à celle des brouillons 21 et 22 |
| titres | 53 ; seul le titre de niveau 1 change |
| consignes figées (3.2 et 3.3) | sections égales octet pour octet à celles du brouillon 20 ; `98a9bd34d280…`, `ecf590eae0c0…` |
| validateur `problemes()` | deux problèmes, les attendus |
| marque des cases | huit lignes (1241, 1242, 1244, 1245, 1247, 1252, 1253, 1254), toutes en 13.1 |
| table d'en-tête, quatre lignes neuves | `ade786eb…`, `8f5480f4…`, `80581f3c…`, `efe87934…` : égales. **Aucune empreinte de fichier cloisonné prise.** |

## 8. Ce que je n'ai pas regardé

- Le texte en entier, hors des passages listés en tête.
- Les quatorze lignes de la table d'en-tête qui renvoient à des dossiers cloisonnés.
- Le code de la version 5 et ses notes.
- Tout interne de moniteur.

## 9. Fichiers ouverts

- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon23.md` : par différence, puis les lignes 3, 155, 157, 452, 587, 591 à 593, 607, 697 à 711, 723, 782, 808, 827, 849 à 866, 896 à 902, 940 à 950, 974, 976, 1007, 1193 à 1219, et les sections 7.7 et 10.
- Les brouillons 20, 21 et 22, par programme.
- La note et le fichier des fiches du brouillon 23 ; le fichier des fiches du brouillon 22, pour la comparaison du rappel.
- `src/controle_ia/prereg.py` (`problemes()`).
- Rien d'autre :
  - aucun fichier `*_v5.py`, ni note du code v5, ni relevé des défauts v5, ni journal ;
  - aucun interne de moniteur ;
  - aucune clé ;
  - aucun appel de modèle ni appel réseau ;
  - aucun sous-agent ;
  - un seul fichier écrit, celui-ci, scellé ; rien committé.
