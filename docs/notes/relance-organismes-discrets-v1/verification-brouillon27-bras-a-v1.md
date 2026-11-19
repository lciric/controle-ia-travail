# Vérification du brouillon 27 du texte neuf du bras A des organismes discrets — v1

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`), contre-lecteur des brouillons 21 à 26. Je juge ; je ne corrige rien.
- **Texte** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon27.md`, `428f9e553e9c…`. Note : `fdc5196129fc…`. Les deux compagnons sont vérifiés.
- **Méthode** :
  - comparaison des brouillons 26 et 27 phrase par phrase, faite par programme ;
  - lecture des 16 blocs touchés et de leur contexte ;
  - lecture de la section 13, des huit cases marquées de 13.1 et des lignes de 13.2, pour dresser la liste de ce qui reste avant le scellement.
  - Aucun code ouvert.

## Verdict : **engageable**

- Les quatre points de ma vérification du brouillon 26 sont tenus.
- Le constat de lancement respecte R5. Il n'ajoute ni issue ni règle de jugement.
- Ma réserve sur la phrase « aucun score, aucun texte » est levée.
- Par programme, sont identiques au brouillon 26 :
  - la section 12 ;
  - les critères de lecture gelés (7.1 à 7.8) ;
  - la section 10 ;
  - et aussi l'hypothèse, la prédiction, la métrique, le seuil, les sections 6.1 à 6.8, 9 et 11.
- Il reste deux remarques mineures (partie 4). Aucune ne retient le texte.
- **Le texte n'attend plus de brouillon pour sa conception** : il attend des mots, des pièces et sa contre-lecture 10 (partie 6).

## 1. Les points de ma vérification du brouillon 26

| point | état | endroit |
|---|---|---|
| C-1 constat de lancement sans cas sain ni artefact | **tenu** | Conventions, ligne 177 : un programme nommé (`scripts/constat_de_lancement_discretion_bras_a_v1.py`), un fichier scellé à six champs, le programme d'analyse qui ne part que sur un constat sain, et ce qui suit chaque refus. 8.4, ligne 997 : une garde neuve, avec cas sain et artefacts. 13.2, ligne 1312. |
| M-1 valeurs p à pleine précision ; valeurs ajustées | **tenu** | 13.1, demande 13 complétée. 6.9, ligne 767 : « Toute valeur ajustée rapportée est calculée sur les valeurs rendues … elle peut différer en nombre …, jamais en état. » C'est conforme à ce que j'ai vérifié par programme au brouillon 26. |
| M-2 rejeu par étape | **tenu** | 6.9, ligne 738 : une étape interrompue avant d'avoir écrit son propre résultat se rejoue, et les étapes scellées restent. Une panne pendant l'étape (n) fait rejouer la seule étape (n). 8.4, ligne 994 : un cas sain, et un artefact, l'étape (m) rejouée alors que son fichier est scellé. |
| M-3 `effectifs`, `exclues`, aires de l'agrégateur | **tenu** | 6.9, ligne 721 : comptes du côté habilité, non des sorties de moniteur, rapportés tels quels. La phrase « aucun score, aucun texte » est bornée à ce que le côté habilité s'engage à rendre et à ce que l'analyse lit pour une règle. Le lanceur et sa contre-lecture en répondent (13.2). |

## 2. Le constat de lancement

**R5 est respecté.**
- **Garde éprouvée** : la ligne neuve de 8.4 (ligne 997) a un cas sain : la configuration est inscrite, aucune révocation n'est entrée, le constat est sain, scellé et cité, la lecture part. Le cas sain d'une première livraison, sans ligne de GO à lire, est écrit aussi.
- **Artefacts, plus de trois** :
  - une révocation entrée après l'état figé ;
  - l'empreinte de la configuration absente du registre courant ;
  - un constat absent, non scellé ou d'une autre configuration ;
  - un constat écrit à la main ;
  - une lecture partie sur un constat qui dit une révocation.
- **Aucun repli silencieux** : le programme d'analyse exige le fichier, son sceau, l'égalité des empreintes de configuration, `configuration_inscrite` vrai et `revocation_entree` faux. Sinon, il s'arrête par une garde ordinaire et le défaut est consigné.
- Le fait que ce soit **un programme** (écrit, essayé, contre-lu), et non un geste à la main, répond à ma crainte d'un oubli.
- La limite est dite honnêtement : le programme d'analyse, sans réseau, vérifie qu'un constat sain existe pour sa configuration, non que ce constat dit vrai. C'est le mieux possible ici, et la note le déclare (réserve 2).

**Aucune issue neuve, aucune règle de jugement.**
- Les trois refus (configuration non inscrite, constat absent, révocation entrée) arrêtent le programme avant toute lecture. Rien de la livraison n'est lu.
- Le texte les range dans « Ce qui n'est pas un refus d'une livraison », qui existe depuis le brouillon 26 : ni événement d'arrêt, ni issue du point 21.
- Ce qui suit est la procédure déjà écrite :
  - inscrire, puis refaire le constat ;
  - faire le constat ;
  - après une révocation, une ligne de GO neuve, donc un autre mot de Lazar, et une configuration neuve. C'est la règle « aucune livraison sans un mot de Lazar ».
- Rien n'y est décidé à la place de Lazar.

## 3. La phrase « aucun score, aucun texte »

**Réserve levée.**
- Le texte ne prétend plus que le programme d'analyse garantit l'absence de score ou de texte dans des champs qu'il ne contrôle pas.
- Il dit qui en répond : le côté habilité, par ce qu'il s'engage à rendre, et le lanceur et sa contre-lecture.
- Il ne crée pas de cause de refus nouvelle, ce qui garde la liste fermée.
- Un garde-fou peu coûteux reste possible, sans en faire un défaut : ne rapporter ces champs que s'ils sont des entiers, et sinon les dire « non rapportés », sans arrêt. C'est une suggestion pour le rédacteur du code (M-1).

## 4. Mineurs

- **M-1. Facultatif.** Pour `effectifs` et `exclues`, rapporter les valeurs seulement si ce sont des comptes entiers, et sinon « non rapportés », sans arrêt et sans entrer dans la liste des refus. Cela fermerait la seule voie par laquelle un texte ou un score rendu par erreur atteindrait un rapport lu par la relance.
- **M-2. Deux demandes à la session principale ne sont que dans les notes, pas dans la case du module de 13.1** (qui s'arrête à la demande 16) :
  - la liste des chemins que la garde statique doit élaguer (note du brouillon 25, demande 17) ;
  - la façon dont `piece_source` désigne le module qui a produit la livraison (note du brouillon 26, demande 18 ; vérification du code de la version 7, M-6).

  Sans la seconde, rien ne lie une première livraison au module que la configuration inscrit. Les porter dans la case, comme demandes 17 et 18, les ferait bloquer le scellement au lieu de dépendre de la mémoire des notes.

## 5. Intégrité (vérifiée par programme)

| contrôle | résultat |
|---|---|
| brouillons 20 à 26 intacts | compagnons vérifiés (`b076e3f9…` à `4a731b4e…`) |
| brouillon 27 et note | `428f9e55…`, `fdc51961…` : compagnons vérifiés |
| **section 12** | **identique au brouillon 26** ; les fiches 9 à 12 restent mot pour mot dans le texte |
| **7.1 à 7.8** (« Critères de lecture gelés » en entier) | **identiques au brouillon 26** |
| **section 10** | **identique au brouillon 26** |
| hypothèse à seuil ; 6.1 à 6.8 ; sections 9 et 11 | identiques au brouillon 26 |
| citations à la lettre | brouillon 20 : 935 sur 935 retrouvées ; brouillon 26 : 1 161 sur 1 161 retrouvées |
| titres | 53 ; seul le titre de niveau 1 change |
| consignes figées (3.2 et 3.3) | sections égales octet pour octet à celles du brouillon 20 ; `98a9bd34d280…`, `ecf590eae0c0…` |
| validateur `problemes()` | deux problèmes, les attendus : la marque restante ; la contre-lecture 10 sans ses empreintes |
| marque des cases | huit lignes (1290, 1291, 1293, 1294, 1296, 1301, 1302, 1303), toutes en 13.1 |
| table d'en-tête, trois lignes neuves | empreintes égales (brouillon 26, sa note, ma vérification). **Aucune empreinte de fichier cloisonné prise.** |

## 6. Ce qui sépare encore le texte du scellement

### A. Mots de Lazar (fiches du brouillon 23 parties, `f20abfed…` ; et questions posées par ailleurs)

1. **Point 21, fiche 12 : ce que vaut un arrêt de la lecture de la discrétion.** Sans défaut ; à lire d'abord. Sous l'option (a), le mot doit dire aussi ce que rétablit une livraison refaite lue avec succès.
2. **Point 19, fiche 10 : intervalle impossible.** Sans défaut.
3. **Point 18, fiche 9 : seuil de 1 %.** Défaut (a), qui échoit le 21 novembre vers 14:30Z.
4. **Point 20, fiche 11 : moniteur appris non ajustable.** Sans défaut, et seulement si le développeur habilité répond que la séparation parfaite peut déclencher ce motif ; sinon, la fiche tombe.
5. **Point 17 : schéma de permutation.** Sans défaut ; question tenue par la session principale.
6. **Choix des deux lecteurs**, et **sortie maximale du lecteur Carbon** (8 192 ou 4 096) : case « lecteurs ».
7. **Écart à R9** pour l'entropie propre de la table des identifiants opaques : case « entropie ».
8. **Lecture du juge d'une autre lignée**, 2 560 ou 6 400 actions, sur un chiffrage que la session principale doit d'abord écrire.
9. Les **informations** déjà envoyées n'appellent pas de réponse : la liste fermée des refus et le sens de « retirée » ; la révocation et le rejeu.

Chaque mot se reporte au texte : retrait des rédactions écartées de 6.9, 8.4, 8.5 et de la section 10, et report en 7.5 ou à la ligne A17 pour le point 21 (case « nœuds » de 13.1).

### B. Pièces de la session principale (côté habilité)

10. **Case du module des cinq moniteurs** : les seize demandes de 13.1, et d'abord :
    - (1) une version du module qui respecte la table des formes, qui corrige donc l'écart de la version 8 à GO-2026-11-19-70, avec son chemin, son empreinte complète, son commit et ses essais ;
    - (2) l'épreuve par retrait et sa notice pour cette version ;
    - (3) l'épreuve de forme, un cas par ligne de la table des formes ;
    - (4) et (5) les chaînes : valeurs de `motif`, de `calculable` et des réglages ;
    - (9) et (10) ce qui déclenche les motifs « non ajustable » et « intervalle impossible » ; la fiche 11 dépend de (9) ;
    - (13) à (16) : forme des valeurs p, à pleine précision ; forme de `lectures` ; formes du fichier des scores ; chemins.
    - S'y ajoutent les deux demandes de M-2 : chemins de la garde statique, et `piece_source`.
11. **Lanceur de l'étape de discrétion** : non écrit ; écrit par le développeur habilité, puis contre-lu.
12. **Renvoi de la base** : « vérifié » ou « non vérifié », par le lecteur habilité, sur la version que la contre-lecture 10 rendra.
13. **Code côté habilité** : moniteurs à modèle de langue et extraction pour la base, cités par leur commit.
14. **Chiffrage de la lecture du juge** (préalable au point 8).

### C. Session de relance

15. **Code de l'instrument et de l'analyse**, version qui suit la 7, aligné sur ce brouillon : configuration à trois parties, une par livraison ; règle (α) et (β) en fractions exactes ; programme du constat de lancement ; rejeu par étape ; écriture sans reste. Essayé, contre-lu par un agent d'un autre modèle, puis commit et empreintes inscrits en case.
16. **Entier racine des graines**, tiré et inscrit (case « entropie »), après le mot de Lazar sur R9.

### D. Contre-lecture 10, vérification habilitée, scellement

17. **Contre-lecture 10** : sur le texte aux cases remplies, par un agent Claude Opus 5.5 neuf, qui n'a pas écrit ni recopié de brouillon. Ce ne peut donc pas être moi, qui ai vérifié les brouillons 21 à 27. Elle porte aussi sur la reprise des corrections de la contre-lecture 9 ; la liste de ses fichiers est en section « Contre-lecture ». Ses deux empreintes sont à inscrire : c'est le second problème du validateur.
18. **Vérification habilitée** du texte aux cases remplies, par le lecteur habilité de la session principale. Elle devrait vérifier aussi les quatorze lignes héritées de la table d'en-tête, que personne de la relance ne peut recalculer.
19. **Validateur sans problème** : plus aucune marque, contre-lecture 10 inscrite.
20. **Scellement (R1)** et inscription au registre (clé `SCELLEMENT-BRAS-A-V2`).

### E. Après le scellement, avant toute dépense (13.2, pour mémoire)

Tarifs ; devis contre-lu ; lignes de GO de calcul ; lanceur et sa configuration ; configuration de l'analyse et constat de lancement ; clés du registre ; confinement. Rien de cela ne retient le scellement.

## 7. Ce que je n'ai pas regardé

- Le texte en entier, hors des blocs touchés, de leur contexte, de la section 13 et des sections que j'ai vérifiées identiques par programme.
- Aucun code.
- Les quatorze lignes héritées de la table d'en-tête.

## 8. Fichiers ouverts

- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon27.md` : par différence ; les blocs touchés ; la section 13 ; les cases marquées de 13.1 ; la liste des lignes de 13.2.
- Les brouillons 20 et 26, par programme.
- La note du brouillon 27.
- Le fichier des fiches du brouillon 23, par programme.
- `src/controle_ia/prereg.py` (`problemes()`).
- Rien d'autre : aucun code, aucun interne de moniteur, aucune clé, aucun appel de modèle ni appel réseau, aucun sous-agent. Un seul fichier écrit, celui-ci, scellé ; rien committé.
