# Vérification des corrections du brouillon 24 du texte neuf du bras A des organismes discrets — v1

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`). C'est moi qui ai contre-lu le brouillon 21 et vérifié les brouillons 22 et 23. Je juge ; je ne corrige rien.
- **Texte** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon24.md`, `12609c048b7c…`. La note est `86e17f6e52f9…`. Les deux compagnons sont vérifiés.
- **Méthode** : comparaison des brouillons 23 et 24, phrase par phrase, par programme. J'ai lu les 18 blocs touchés et leur contexte, ainsi que la note (contrôles, parties 2, 3, 5 et 6, réserves).

## Verdict : **engageable**

- Les quatre corrections demandées sont tenues : C-1, C-2, M-2 et M-3.
- Le brouillon 24 n'ouvre ni ne ferme aucune question.
- Les points 17 à 21 de la section 12 sont identiques au caractère près à ceux du brouillon 23, et la section 12 l'est en entier.
- Les renvois écrits en 7.5 et à la ligne A17 n'ajoutent rien à une ligne de verdict. La ligne de repli neuve de la section 10 n'ajoute rien qui ne soit déjà dans les trois rédactions de 6.9.
- Il reste trois remarques mineures. Aucune ne demande de nouveau brouillon avant le mot de Lazar. Deux sont à dire à Lazar avec les réponses en attente (M-2 et M-3).

## 1. Les corrections demandées

| défaut | état | endroit et constat |
|---|---|---|
| C-1 ce que rend le programme qui refuse | **tenu** | 6.9, ligne 713 : une définition unique. **Ce qui sort, et rien d'autre** : la garde ou la règle d'arrêt, le nom du champ, la lettre du cas ou « aucun cas », l'étape, et le moniteur et la dose. **Ce qui ne sort jamais** : un nombre (aire, aire d'un pli, valeur p, compte, borne, quantile, effectif, rang), ni la valeur de `motif` ou de `calculable`. Cette définition est reprise en 8.4 (ligne 960, avec un artefact à jour) et à la ligne du cas E (ligne 733 : « ni nombre, ni valeur de `motif` »). La fiche 12, déjà partie, garde sa forme abrégée. Le texte dit que la définition de 6.9 vaut, et la retouche de la fiche est écrite dans la note, partie 3. |
| C-2 8.5 et section 10 | **tenu** | 6.9, ligne 715 : sous la rédaction (a), 8.5 s'applique en entier. Sous (b) et (c), seuls le versement et la consignation s'appliquent ; la livraison refusée est seule non opposable, ainsi que les grandeurs de l'étape (n) sous (c). Les tables A et B, les autres issues de 7.5 et la table C (sous (c), pour un arrêt à l'étape (n)) ne sont pas touchées. 8.5, ligne 1019, porte une phrase de renvoi. La section 10, ligne 1048, a une ligne de repli à trois rédactions. |
| M-2 frontière entre les étapes (m) et (n) | **tenu** | 6.9, ligne 705, « Quand jouent les gardes » : toutes les gardes sur la sortie de la lecture commune jouent à sa réception, à l'étape (m), sur les vingt lectures ensemble. Seules les gardes du fichier des scores par unité jouent à l'étape (n). La rédaction (c) est récrite (ligne 721). Artefact en 8.4 : « un écart sur la sortie de la lecture commune, fût-il à la dose ¼, rangé à l'étape (n) ». |
| M-3 renvois au point 21 | **tenu** | 7.5, ligne 875, et ligne A17, ligne 837 : un renvoi entre parenthèses, marqué « nœud ouvert », qui dit « rien n'est ajouté d'ici là ». La case « nœuds » de 13.1 (ligne 1252) dit où se reporte le mot de Lazar : 7.5 ou A17, 8.5, section 10, et le retrait des rédactions écartées de 6.9 et 8.4. |
| M-1 et M-4 | **non portés, à dessein** | Les fiches sont parties. La retouche de M-1 est écrite dans la note, partie 3, pour être portée après la réponse de Lazar : c'est acceptable. M-4 est laissé tel quel, et le conseil d'ordre est écrit en tête du fichier. |

## 2. Moniteur et dose dans ce que rend le programme qui refuse

- **Cloisonnement : acceptable.**
  - Le nom du moniteur et la dose ne sont pas des internes de moniteur (ni poids, ni vocabulaire, ni trait, ni score).
  - L'instance d'analyse les reçoit déjà dans chaque lecture ordinaire.
  - Aucun nombre ni aucune chaîne de `motif` ne sort, et l'artefact de 8.4 l'éprouve.
- **Reprise bornée par la fiche 12 : acceptable, avec une réserve à porter à Lazar (M-3).**
  - Le nom du champ, la lettre du cas et le nom de la règle d'arrêt donnent une information grossière sur ce qui s'est passé à une dose, pour un moniteur. Par exemple, « intervalle dégénéré » au cas D, ou « moniteur appris non ajustable », qui peut venir d'une séparation parfaite des classes, donc d'un repérage fort.
  - C'est le minimum qu'il faut pour corriger le module.
  - La reprise reste bornée : elle passe par le mot de Lazar, le module corrigé est contre-lu, le lecteur habilité atteste qu'aucun calcul de moniteur ne change, la livraison est refaite en entier avec les mêmes clés de graine, et elle est lue une seule fois.
  - Mais la décision d'accorder la reprise se prend après cette information, sans règle écrite d'avance. Voir M-3.

## 3. La section 10 et les renvois en 7.5 et à la ligne A17

- **7.5 et la ligne A17** : la comparaison par programme montre une seule insertion en chaque endroit, la parenthèse de renvoi. Aucun événement n'est ajouté à la liste de A17. Aucune cause n'est ajoutée à l'issue « non lue » de 7.5. Chacune des deux parenthèses dit expressément « rien n'y est ajouté d'ici là ». **Rien n'est ajouté à une ligne de verdict.** La parenthèse de A17 est placée dans la liste « à savoir », entre deux de ses événements. Un lecteur pressé pourrait la prendre pour un événement, mais son texte l'exclut. Elle doit être retirée ou remplacée au scellement, ce que la case « nœuds » prévoit.
- **Section 10, ligne 1048** : elle redit les trois rédactions de 6.9, marquées « nœud ouvert », et la ligne retenue sera la seule à rester. Elle n'ajoute aucune issue. Une nuance de mots, voir M-1.

## 4. Remarques mineures

- **M-1. Section 10, rédactions (b) et (c) : « rapportés », « rapportée ».**
  - La rédaction (b) dit « le désappariement et les autres issues sont rapportés ». La rédaction (c) dit « la table C scellée est rapportée ».
  - En 6.9, la rédaction (b) dit « restent prononcées ». Sous la rédaction (a), « rapporté tel quel » veut justement dire « non prononcé ». C'est l'ambiguïté qui avait fait B-1.
  - La ligne voisine (« Renvoi de la base non vérifié : … le désappariement seul est rapporté ») emploie le mot dans le même sens, et 6.9 et 8.5 sont nets. Ce n'est donc pas un défaut de règle.
  - Au scellement, écrire « restent prononcés » et « reste prononcée » dans la ligne retenue.
- **M-2. La fiche 11 (option (b)) et la fiche 12 (options (b) et (c)) se combinent mal.**
  - La livraison refaite exige que le lecteur habilité atteste qu'« aucun calcul de moniteur n'y change ».
  - Or la correction d'un moniteur appris non ajustable, pour qu'une séparation parfaite donne une aire, change ce calcul.
  - Sous ce couple d'options, cette anomalie ne peut donc jamais être reprise : la discrétion reste « non lue ». La fiche 11 ne le dit pas. Le texte ne le contredit pas, c'est une conséquence des conditions écrites.
  - Les fiches sont parties. Il faut le dire à Lazar avec la réponse du développeur habilité, qui rouvre la fiche 11. C'est un argument de plus pour son option (c), corriger le module avant la course.
- **M-3. Accorder la reprise reste une décision prise sans règle écrite d'avance (fiche 12, options (b) et (c)).**
  - La sortie du programme qui refuse informe un peu sur le résultat (partie 2).
  - Par symétrie (R4), il vaudrait mieux que la réponse de Lazar fixe d'avance la règle de la reprise. Par exemple : « reprise accordée dès que les conditions sont remplies, quel que soit le défaut nommé », plutôt qu'un mot donné au cas par cas.
  - À proposer avec la réponse au point 21. Je n'en fais pas un défaut du texte.

## 5. Points 17 à 21 et fiches (vérifiés par programme)

- Les points 17, 18, 19, 20 et 21 sont **identiques** au brouillon 23, au caractère près. La section 12 entière l'est aussi ; elle porte les points 1 à 21, dans l'ordre.
- Les fiches du brouillon 23 (`f20abfed…`, compagnon vérifié, non modifiées) restent mot pour mot dans la section 12 : fiches 9, 10, 11 et 12, avec 6, 7, 7 et 7 puces.

## 6. Intégrité (vérifiée par programme)

| contrôle | résultat |
|---|---|
| brouillons 20 à 23 intacts | `b076e3f9…`, `8d834631…`, `ade786eb…`, `ed7823af…` : compagnons vérifiés |
| brouillon 24 et note | `12609c04…`, `86e17f6e…` : compagnons vérifiés |
| citations à la lettre | brouillon 20 : 935 sur 935 retrouvées ; brouillon 23 : 1 110 sur 1 110 retrouvées |
| titres | 53 ; seul le titre de niveau 1 change |
| consignes figées (3.2 et 3.3) | sections égales octet pour octet à celles du brouillon 20 ; `98a9bd34d280…`, `ecf590eae0c0…` |
| validateur `problemes()` | deux problèmes, les attendus : marque restante ; contre-lecture 10 sans ses empreintes |
| marque des cases | huit lignes (1252, 1253, 1255, 1256, 1258, 1263, 1264, 1265), toutes en 13.1 |
| 7.5 et ligne A17 | une seule insertion chacune, la parenthèse de renvoi |
| table d'en-tête, quatre lignes neuves | `ed7823af…`, `f2963374…`, `f20abfed…`, `d6d53be4…` : égales. **Aucune empreinte de fichier cloisonné prise.** |
| entrée « Contre-lecture 11 » | la vérification du brouillon 23 est inscrite avec son chemin et son empreinte, qui sont justes. La mention « confirmée par la session qui orchestre », écrite au brouillon 23, reste à consigner par elle (réserve 7 de la note). |

## 7. Ce que je n'ai pas regardé

- Le texte en entier : seulement les blocs touchés et leur contexte. Les passages qui dépendent d'un arrêt ont été lus au brouillon 23 et ne sont pas changés, hors des blocs vus ici.
- Les quatorze lignes de la table d'en-tête qui renvoient à des dossiers cloisonnés.
- Le code de la version 5 et ses notes.
- Tout interne de moniteur.

## 8. Fichiers ouverts

- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon24.md` : par différence, puis les lignes 3, 705 à 721, 733, 837, 875, 960, 1019, 1047 et 1048, et 1252.
- Les brouillons 20 et 23, par programme.
- `docs/notes/relance-organismes-discrets-v1/preenregistrement-v2-brouillon24-note-v1.md`, par recherches ciblées : parties 1 à 3, 5, 6 et 7.
- `src/controle_ia/prereg.py` (`problemes()`).
- Rien d'autre. Aucun fichier `*_v5.py`, ni note du code v5, ni journal. Aucun interne de moniteur, aucune clé. Aucun appel de modèle ni appel réseau. Aucun sous-agent. Un seul fichier écrit, celui-ci, scellé ; rien committé.
