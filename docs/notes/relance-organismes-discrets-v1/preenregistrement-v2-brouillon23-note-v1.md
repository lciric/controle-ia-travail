# Note de changements — brouillon 23 du texte neuf du bras A des organismes discrets — v1

**Rédigé par Claude Fable 5.2 (`claude-fable-5-2`)**, le même agent que pour les brouillons 21 et 22. Je conçois ; la session qui m'orchestre consigne, scelle au registre et committe.

- **Brouillon** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon23.md`, `ed7823af1377c55cc3ea911e7dbf2c0c7a6872010b846e8ba54e33d81c3f2c2e` (1 963 lignes). Les brouillons 22 (`ade786eb…`), 21 (`8d834631…`) et 20 (`b076e3f9…`) ne sont pas modifiés : vérifiés avant la copie et après l'écriture.
- **Fiches pour Lazar** : `docs/notes/relance-organismes-discrets-v1/decisions-bras-a-brouillon23-v1.md`, `f20abfed86f30883409b335844920c2b13595fd2060f6c3827ddc907b629783a`. Elle remplace celles des brouillons 22, 21 et 19. **Celles du brouillon 22 ne doivent pas partir.**
- **Source** : la vérification des corrections du brouillon 22 par le contre-lecteur Claude Opus 5.5, `docs/notes/relance-organismes-discrets-v1/verification-corrections-brouillon22-bras-a-v1.md`, `efe8793445a81dec02ebf7f38197211c29664a6eb71946fd037592b46b63c64b`, lue en entier. Verdict : non engageable en l'état, pour un défaut bloquant borné ; deux défauts à corriger ; quatre mineurs.
- **Méthode** : copie du brouillon 22 par `cp`, puis 30 remplacements exacts, vérifiés par programme (29 uniques, un qui porte sur deux occurrences identiques, déclaré).
- **Rien n'est arrivé de Lazar ni de la session principale** : registre des accords relu sur la branche principale distante au commit `ae26270a`, aucune ligne de plus.
- **Heures (UTC, `date -u`)** : début 15:54:34Z le 2026-11-19 ; brouillon scellé vers 15:59Z.
- **Interdits tenus** : aucune empreinte de fichier d'un dossier du côté habilité ; aucun interne de moniteur ; aucune fiche de l'organisme d'idéation ; aucune réponse de l'essai de mesure ; aucune clé ; aucun appel de modèle ; seul appel réseau, `git fetch` de la branche principale ; ni `registres/`, ni `.claude/`, ni le journal touchés ; rien committé ; aucun fichier existant écrasé ; suite d'essais non lancée ; aucun sous-agent ; aucun fichier `*_v5.py` ni note du code ouverts.

## Mon erreur, dite une fois

Au brouillon 22, j'ai rangé la livraison refusée sous la ligne A17 en écrivant que je n'appliquais que sa lettre et que le résultat principal restait. Les deux étaient faux. Je n'avais pas lu 7.5 : sous la ligne A17, aucune hypothèse n'est prononcée, le désappariement compris. Et ajouter un événement à la liste d'une ligne d'une table de verdict, c'est fixer l'issue d'un cas. Les fiches 10 et 11 du brouillon 22 portaient la phrase fausse. La réserve 1 de la note du brouillon 22 est à tenir pour retirée.

## Contrôles par programme

| contrôle | résultat |
|---|---|
| titres de section (53) | les 52 titres de niveau 2 et 3 sont identiques à ceux du brouillon 22 |
| consignes figées (blocs de 3.2 et 3.3) | égales octet pour octet à celles du brouillon 20 ; `98a9bd34d280fc7d9db07a733bc78557ff350538a3ace7a2926999ecf14c9248` et `ecf590eae0c06d413d173f7f03c5575e52d6034613e0a1a30d681149435a1816`, recalculées |
| citations à la lettre du brouillon 20 | les 935 passages sont tous retrouvés ; la fiche du point 17 et l'avis d'origine sont intacts |
| citations du brouillon 22 | 1 079 passages ; un seul n'est pas retrouvé tel quel, « lecture invalidée par la liste d'arrêt », qui était de ma phrase du brouillon 22 sur la ligne A17 ; ce n'est pas une citation d'un texte transmis |
| ligne A17 | elle ne porte plus l'événement « livraison refusée » ; elle garde la précision de GO-2026-11-19-70 |
| phrase « le résultat principal, déjà scellé, reste » | absente du brouillon 23 |
| table d'en-tête, sans les fichiers cloisonnés | 129 lignes à empreinte : 115 recalculées et égales, 0 différente, 14 sautées et non ouvertes (les mêmes qu'au brouillon 22), qui gardent l'empreinte héritée, non vérifiée par moi |
| marque des cases non remplies | huit lignes, toutes en 13.1 |
| validateur (`problemes()`) | deux problèmes, les mêmes, attendus : marque restante hors des sections exigées ; contre-lecture 10 sans ses deux empreintes |
| section 12 | points 1 à 21, dans l'ordre |
| fiches 9 à 12 | chaque puce du fichier des fiches est une sous-chaîne exacte de la section 12 du brouillon 23 |
| différence avec le brouillon 22 | 33 lignes de plus ; 32 lignes changées |

## 1. La vérification, défaut par défaut

| défaut | traitement | ce que j'ai écrit |
|---|---|---|
| B-1 livraison refusée rangée sous la ligne A17 | **corrigé : issue ouverte, posée à Lazar sans défaut** | l'événement est retiré de la ligne A17 ; 6.9 porte trois rédactions côte à côte, plus ce qui leur est commun ; ni A17 ni 7.5 ne sont touchées d'ici le mot de Lazar ; point 21 de la section 12 et fiche 12 ; les fiches 9, 10 et 11 disent la conséquence d'un arrêt par une même phrase, qui la dit ouverte |
| C-1 gardes du motif « moniteur appris non ajustable » | **corrigé** | une ligne de 8.4, cas sain et artefact pour chacune des trois rédactions |
| C-2 statut et réserve de la note | **corrigé** | le statut dit l'extension faite au brouillon 22 et son retrait ; la réserve 1 de la note du brouillon 22 est retirée ici |
| M-1 artefact du cas B | **corrigé** | « au cas B, une aire, une valeur p ou une borne remplie », à la ligne « forme d'une livraison » |
| M-2 défaut gardé par la fiche 9 | **corrigé** | une phrase dans la fiche dit pourquoi elle garde un défaut |
| M-3 contre-lecture 11 ; vérification à inscrire | **fait** | la confirmation de la session qui orchestre et la vérification, avec son chemin et son empreinte, sont à l'entrée « Contre-lecture 11 » |
| M-4 compte des fichiers cloisonnés | **renvoyé à la session qui orchestre** | à consigner : onze fichiers au brouillon 21, aucun depuis ; quatorze lignes de la table non vérifiées |

## 2. L'issue ouverte : les trois rédactions, et pourquoi je n'en propose pas une quatrième

- **(a) la ligne A17 en entier** : aucune hypothèse prononcée, désappariement compris.
- **(b) discrétion « non lue »**, à quelque étape que survienne l'arrêt ; le désappariement reste prononcé ; livraison refaite sur un mot de Lazar, sous un module corrigé et contre-lu dont le lecteur habilité écrit qu'aucun calcul de moniteur n'y change, mêmes clés de graine.
- **(c) la rédaction (b), en distinguant les étapes** : à l'étape (m), comme (b) ; à l'étape (n), qui ne porte que le fichier des scores par unité et l'aire conditionnelle, la table C scellée reste, et seules ces grandeurs sont « non rapportées ».

Je recommande (c), confiance 0,7 : c'est le principe que Lazar a retenu le 19 novembre, chaque issue ne dépendant que de ce qui la touche. Je n'ai pas trouvé de quatrième option meilleure. J'ai ajouté une chose, **commune aux trois** : le programme qui refuse ne rend que le nom de la garde, de la clé et du cas, jamais une valeur de la livraison. Elle borne la retouche que permet une livraison refaite. C'est une garde, éprouvée en 8.4.

Les deux arrêts écrits ailleurs sous une rédaction ouverte — l'intervalle impossible tenu pour une anomalie, le moniteur non ajustable tenu pour une anomalie — prennent la même issue : une seule question pour Lazar, non trois.

## 3. Ce qui change, section par section

| section | changement |
|---|---|
| titre ; statut ; auteur ; date ; commit lu | brouillon 23 ; la phrase du brouillon 22 sur la ligne A17 est reprise |
| table d'en-tête | quatre lignes : le brouillon 22, sa note, ses fiches, la vérification |
| conventions | « Numérotation stable » |
| 6.9 | les deux arrêts sous rédaction ouverte renvoient au point 21 ; « Ce que vaut cet arrêt » récrit : nœud ouvert, commun aux trois, trois rédactions ; ligne E, rédaction (c), de la table |
| 7.2, ligne A17 | l'événement ajouté au brouillon 22 est retiré |
| 8.4 | « ligne A17 » retiré de cinq lignes ; artefact du cas B ; deux lignes neuves : moniteur appris non ajustable ; issue d'un arrêt de la lecture de la discrétion |
| 12 | fiches des points 18, 19 et 20 reprises ; **point 21 neuf** |
| 13 ; 13.1 | point 21 ; case « nœuds » |
| 14.35 | neuve |
| « Contre-lecture » | entrée 11 : confirmation, et vérification des corrections avec son empreinte |

7.5 n'est pas touchée.

## 4. Les fiches pour Lazar

1. **Fiche 9 — seuil de 1 % de tirages dégénérés.** (a) sur les 2 000 demandés, 21 ou plus, module inchangé ; (b) sur les calculés, 20 ou plus, module à changer. Recommandation (a), confiance 0,85. Défaut : (a), échéance d'origine, le 21 novembre vers 14:30Z ; la fiche dit pourquoi elle garde un défaut.
2. **Fiche 10 — intervalle qui n'a pas pu être calculé.** (a) comme un intervalle entièrement dégénéré ; (b) « indécis » d'office ; (c) anomalie, la lecture de la discrétion s'arrête, avec la conséquence que fixe la fiche 12. Recommandation (a), confiance 0,6. **Aucun défaut.**
3. **Fiche 11 — moniteur appris qui n'a pas pu être ajusté.** Elle tombe si la séparation parfaite ne peut pas déclencher ce cas. Sinon : (a) « indécis » toujours ; (b) anomalie, même conséquence ; (c) faire corriger le module. Recommandation : attendre la réponse, puis (c), confiance 0,6. **Aucun défaut.**
4. **Fiche 12, neuve — ce que vaut un arrêt de la lecture de la discrétion.** (a) plus aucune hypothèse prononcée, résultat principal compris ; (b) la discrétion seule est « non lue » ; (c) comme (b), sans retirer la table de discrétion si l'arrêt vient après elle. Recommandation (c), confiance 0,7. **Aucun défaut.**
5. **Rappel — schéma de permutation.** Inchangé depuis le brouillon 22 : option 2, confiance 0,7. **Aucun défaut.**

## 5. Ce qui est demandé à la session principale

La liste de la note du brouillon 22 (partie 4, onze points) tient sans changement. Un point s'y ajoute :

12. **Si Lazar retient la rédaction (b) ou (c) de la fiche 12** : pour une livraison refaite, l'attestation du lecteur habilité qu'aucun calcul de moniteur ne change entre le module refusé et le module corrigé, et le rejeu avec les mêmes clés de graine.

À dire aussi au contre-lecteur du code de la version 5 : le point 3 de la partie 6 de la note du brouillon 22 est remplacé par le point 3 ci-dessous.

## 6. Ce que le code de la version 5 doit porter

Cette partie reprend la partie 6 de la note du brouillon 22. **Seuls les points 3, 5 et 6 changent** ; un point 15 s'ajoute. Les autres points de cette note-là tiennent tels quels.

3. **L'arrêt n'est plus « la ligne A17 » — changé.** Une garde qui refuse lève un événement nommé, « arrêt de la lecture de la discrétion », qui porte la garde, la clé, le cas et l'étape, (m) ou (n), et **aucune valeur de la livraison**. Ce que cet événement entraîne est **un choix nommé, sans valeur par défaut**, à trois valeurs :
   - (a) verdict de la course à la ligne A17 ; aucune issue de 7.5 prononcée, désappariement compris ; lignes de la table B rapportées, non opposables ;
   - (b) discrétion « non lue », quelle que soit l'étape ; tables A et B et autres issues inchangées ;
   - (c) à l'étape (m), comme (b) ; à l'étape (n), fichier de l'étape (m) et table C gardés, grandeurs de l'étape (n) « non rapportées : livraison refusée ».
   Le code ne doit écrire en dur ni « A17 » ni « la table B reste ». Un essai par valeur. Dans les trois : aucun état de moniteur n'est dit après un arrêt à l'étape (m) ; la livraison refusée est versée et scellée ; aucune livraison refaite n'est lue sans une ligne de GO.
5. **Cas E, rédaction (c) — changé** : l'arrêt à une dose de la famille lève le même événement que ci-dessus, non un arrêt propre.
6. **Motif « moniteur appris non ajustable », rédaction (b) — changé** : de même ; et la ligne neuve de 8.4 donne ses essais, un cas sain et un artefact par rédaction.
15. **Neuf** : un essai vérifie qu'aucune valeur de la livraison refusée ne paraît dans la sortie du programme qui refuse.

Le code de la version 5 porte donc **quatre** choix nommés sans valeur par défaut : le schéma de permutation, le cas E, le motif « non ajustable », l'issue d'un arrêt. Un cinquième a un défaut écrit : le seuil de 1 %, option (a).

## 7. Réserves

1. **Quatre issues ouvertes.** Le scellement attend quatre mots de Lazar, dont un suspendu à une réponse du développeur habilité. C'est beaucoup ; chacune est une issue d'un cas que le texte n'écrivait pas, et je n'en vois aucune que je puisse fermer seul.
2. **La fiche 12 décide du coût des fiches 10 et 11.** Je conseille de la lire d'abord ; le fichier des fiches le dit.
3. **La garde « aucune valeur dans la sortie du programme qui refuse »** est de moi, commune aux trois rédactions. Elle ne change aucune issue ; le vérificateur peut la juger de trop.
4. **7.5 et la ligne A17 ne portent aucun renvoi** vers le point 21 : je les ai laissées intactes, comme demandé. Un lecteur de 7.5 seule ne voit donc pas la question ; 6.9 et 8.4 la portent.
5. **Je n'ai toujours pas relu le texte en entier.** De plus qu'au brouillon 22 : 7.5, 6.12 point 2, 6.3 (m) et (n). L'erreur de B-1 est venue d'une section non lue ; d'autres peuvent rester.
6. **Quatorze lignes de la table d'en-tête** gardent une empreinte héritée, non vérifiée.
7. **La vérification des corrections de ce brouillon** revient au même contre-lecteur.

## 8. Fichiers ouverts pour ce brouillon

- `docs/notes/relance-organismes-discrets-v1/verification-corrections-brouillon22-bras-a-v1.md`, en entier.
- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon22.md` : 7.5 en entier ; 6.12, point 2 ; 6.3, de l'étape (m) à la fin ; les lignes qui portent « A17 » entre 6.9 et 8.4 ; et, par programme, le fichier entier pour les contrôles.
- `registres/go.md` de la branche principale distante, par `git show`, après la ligne 509.
- Par programme, pour leur seule empreinte : les 115 fichiers de la table d'en-tête hors des dossiers cloisonnés.
- Mes propres pièces des brouillons 21 et 22 et mes programmes de construction.
- Rien d'autre.
