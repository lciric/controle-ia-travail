# Note du rédacteur — brouillon 39 du texte neuf du bras A des organismes discrets — v1

- **Rédacteur** : Claude Fable 5.2 (`claude-fable-5-2`), le même que pour les brouillons 21 à 38. Je conçois ; je ne consigne pas au registre et je ne committe pas.
- **Texte** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon39.md`, `4425e9e922044a749a6d1357f2fadbc9e212d8f4843e954b704792840ae23b61`, scellé. 2 364 lignes.
- **Point de départ** : le brouillon 38 (`16545485b0ff8df1bb610c28c7f147cc91a0c051d932a78b970e9cda94d4d04f`), inchangé.
- **Heures (UTC)** : commencé le 2026-11-20T08:32:18Z ; texte scellé à 08:34:46Z.
- **Méthode** : 32 remplacements exacts ; 30 sur une ancre trouvée une seule fois, deux sur une chaîne remplacée partout (six et cinq fois : la citation des deux mots de Lazar). Texte construit dans le bloc-notes, contrôlé, posé une fois sans écrasement, comparé octet pour octet, puis scellé.
- **Pièce traitée** : `docs/notes/relance-organismes-discrets-v1/verification-brouillon38-bras-a-v1.md`, `50229101836fd8fc1034f889c8ac9408260ce6f889ea1c6a0bc45827345b4964`.
- **Aucune fiche n'est ajoutée.**

## 1. Points traités

| point | ce que le texte écrit | où |
|---|---|---|
| **C-1** | l'attestation qu'aucun calcul de moniteur ne change de la version 7 à la version 10 est à écrire à part, par le côté habilité, sur la version 10 ; rien n'en tient lieu, sauf si le lecteur habilité écrit qu'une autre pièce suffit | 13.1, case du module |
| **C-2** | garde de procédure neuve : la configuration ne porte, pour chacun des cinq choix, que la seule valeur que le texte garde ; le contre-lecteur de la configuration les confronte un à un, et le manifeste de course les consigne. 8.4 ne dit plus qu'un programme refuse les autres valeurs | conventions ; 8.4 ; 8.7 |
| **C-3** | en 7.4 et en 7.7, il ne reste que « sur toutes les actions », aux trois endroits ; la suite « faute de puissance… » part avec le sous-échantillon | 7.4 ; 7.7 |
| m-1 | les deux mots du 20 novembre sont cités par leur pièce scellée (`docs/notes/relance-organismes-discrets-v1/mots-de-lazar-juge-et-point-19-bras-a-2026-11-20-v1.md`, `2845ca37e79361aaff125fb2f01cbcb569257526bae0c8eeaeddef7f61dcf6df`), onze fois ; la phrase « portée à Lazar avant tout retrait » dit maintenant ce que dit la pièce : la décision a été réexpliquée | en-tête ; conventions ; 6.9 ; 6.10 ; marque du point 19 ; 13.1 ; 14.50 |
| m-2 | `effectifs` : ou `null` quand un pli n'a aucune unité | 13.1 |
| m-3 | une seule valeur par dose, un nombre ou `null` au cas B | 13.1 |
| m-4 | qui confirme quoi : ce que la vérification de la version 10 confirme, et ce qui reste la parole du développeur, éprouvée par le passage des sorties de l'épreuve de forme | 13.1 |
| m-5 | la clé `lec6` « n'est tirée par aucun programme » | 6.2 |
| m-6 | toutes les positions des deux épisodes sont offertes à la lecture ; une action non appliquée est non lue | 6.9 |
| m-7 | la stratification du sous-échantillon du juge est dite sans objet, au devis | 13.2 |
| m-8 | la réponse du lecteur habilité à la demande 25 est versée en 14.51, comme un avis ; la remarque sur la table B devient une garde de procédure | 14.51 ; 8.7 |
| m-9 | « plus aucun cas n'est tenu pour une anomalie » est borné à la lecture commune des cinq moniteurs | 6.9 |

## 2. Contrôles par programme

| contrôle | résultat |
|---|---|
| **7.1 à 7.8** | 3 lignes changées sur 102, et rien d'autre. Ce qui est retiré : « le sous-échantillon ou », « selon la », « ; faute de puissance, il est plus souvent indécis, ce qui mène à C5 » ; « « sur un sous-échantillon de 2 560 actions » ou » ; « [sur un sous-échantillon de 2 560 actions \| » et le crochet fermant. Rien n'est ajouté, hors la ponctuation de la parenthèse |
| **section 12** | 1 ligne changée sur 172 : la marque du point 19, où le journal laisse place à la pièce scellée et où « lui ayant été portée » devient « posée… puis réexpliquée ». Les fiches 9 à 12 restent mot pour mot |
| **section 10** | identique |
| hypothèse au seuil ; 6.3 à 6.8 ; 8.1 à 8.3 ; 8.5 et 8.6 ; sections 9 et 11 | identiques |
| titres | 54, identiques hors le titre de niveau 1 |
| consignes figées (3.2 et 3.3) | égales à celles du brouillon 20 ; `98a9bd34d280fc7d9db07a733bc78557ff350538a3ace7a2926999ecf14c9248`, `ecf590eae0c06d413d173f7f03c5575e52d6034613e0a1a30d681149435a1816` |
| marque des cases | 5 lignes, toutes en 13.1 : nœuds, entropie, renvoi de la base, commit du code, module |
| table d'en-tête | 212 empreintes recalculées, toutes égales ; 14 lignes cloisonnées sautées, **aucune empreinte prise sur elles** |
| validateur `problemes()` | les deux problèmes attendus |
| citations du brouillon 38 | 1 396, dont 2 absentes : « sur un sous-échantillon de 2 560 actions », et la phrase permise de la ligne C6, récrite sans son crochet |
| mots du 20 novembre | plus aucune citation par le journal seul |

**Registre relu** au commit `c1725862f` de la branche principale : une ligne de plus, GO-2026-11-20-30, qui ne touche pas le bras A. Les deux mots du 20 novembre n'ont pas encore leur ligne.

## 3. Ce qui sépare encore le texte du scellement

### Ce qui attend Lazar
- Plus aucun choix. Ses lignes de GO de dépense viennent après le scellement, sur devis.

### Ce qui attend la session principale
1. **Au registre** : la ligne des deux mots du 20 novembre, qui renvoie à leur pièce scellée et ne nomme pas GO-2026-11-19-97 (case « nœuds ») ; le type « inscription », confirmé et déclaré à l'en-tête ; les formes et les consignes de tenue.
2. **Par le côté habilité, pour la case du module** :
   - **l'attestation**, écrite à part, sur la version 10, qu'aucun calcul de moniteur ne change depuis la version 7 ;
   - le lanceur de l'étape de discrétion, écrit et contre-lu, sur l'extrait en version 3 ;
   - le dossier du fichier des scores par unité, que la configuration du lanceur fixe ;
   - la confirmation que la préparation des lectures ne tire plus aucune position pour le juge.
3. **Le renvoi de la base**, par le lecteur habilité, après la contre-lecture 10, sur la version qu'elle rend.

### Ce qui attend la session de relance
1. Le commit du code arrêté, à la case « commit du code ».
2. Les sorties de l'épreuve de forme du module, à passer par le programme d'analyse : c'est ce qui éprouve la parole du développeur sur les chaînes et les réglages.
3. La contre-lecture 10, par un agent Claude Opus 5.5 neuf, et la vérification indépendante du code et du texte ensemble.
4. Un dernier passage sur le texte, pour remplir les cases et retirer la marque.
5. Au scellement : l'entier racine ; le contrôle de différence avec le texte contre-lu ; le validateur sans aucun problème ; le scellement (R1) et la ligne `SCELLEMENT-BRAS-A-V2`.

### Après le scellement, avant toute dépense (13.2)
- le dossier de l'essai de mesure, versé sur la branche principale ;
- le programme d'enchaînement de la lecture, écrit et contre-lu ;
- la configuration de l'analyse, **contre-lue pour ses cinq choix** (8.7) ;
- l'épreuve de forme de bout en bout ;
- les tarifs, le devis contre-lu, et les lignes de GO.

## 4. Réserves

1. **La garde de procédure des cinq choix** désigne un contre-lecteur de la configuration. Le texte demandait déjà que cette configuration soit contre-lue par un agent d'un autre modèle (13.2) ; je lui ai donné cette tâche de plus.
2. **La garde sur la table B** : je l'ai écrite en 8.7, tenue par la session principale, vérifiée par le lecteur habilité au renvoi de la base. Le vérificateur laissait le choix entre l'écrire et la dire couverte.
3. **La réponse à la demande 25** est versée en 14.51, non dans le corps du texte : aucune règle n'en dépend.
4. **La partie historique de la case du module** garde deux phrases qui parlent d'une « rédaction (c) », sous « Histoire de la case ». Le dernier passage pourra les abréger.
5. **Je n'ai pas relu le texte en entier.**

## 5. Fichiers ouverts

- La vérification du brouillon 38 : ses parties 3, 4 et 6, et sa liste de fichiers.
- La pièce scellée des deux mots de Lazar, en entier.
- Le brouillon 38, par passages et par programme ; le brouillon 20 et le fichier des fiches du brouillon 23, par programme.
- Le registre des GO de la branche principale distante, par `git show` après un `git fetch`, seul appel réseau.
- **Non ouverts** : aucun module du code ; aucun interne de moniteur, aucun module habilité, rien sous `bases/`, `sondes/` ou `t07*/`, rien de T0.8, rien sous `docs/notes/bras-a-moniteurs-v1/` ; aucune fiche de l'organisme d'idéation ; aucune réponse de l'essai de mesure ; aucune clé. Aucun appel de modèle, aucun sous-agent, aucune dépense. Rien de committé ; `registres/`, `.claude/` et le journal non touchés.
