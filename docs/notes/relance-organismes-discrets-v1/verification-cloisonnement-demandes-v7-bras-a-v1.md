# Vérification de cloisonnement des demandes v7 du bras A (courte) — v1

- **Pièces vérifiées.**
  - Pièce du développeur : `docs/notes/relance-organismes-discrets-v1/demandes-au-developpeur-habilite-bras-a-v7.md`, `e55a70882edd5b69afd99e6f5db73d7de2a2626d379d0b46b87b0943bfb31150`. Comparée à la v6, `4937274b3d360e1dc3f95a6d0888eec5fd68d598e0f9a1b9a3e86fd9ad2d9a81`.
  - Pièce du lecteur : `…/demandes-au-lecteur-habilite-et-a-lazar-bras-a-v7.md`, `1700ca19663ea471cda03b4db41cf8bf7955bd25d498af53c649d128a54e2e50`. Comparée à la v6, `5a32c11168b023334940962717e4103027be2043b66bb8018e0809cd059cb633`.
  - Mot de Lazar : `mot-de-lazar-go-recos-bras-a-2026-11-19-v1.md`, `1fcfae81182ff3434ae33fe5a5ac7bd58cb90b47cf55ccc9432c5bce0416673d`.
  - Les cinq compagnons sont conformes.
- **Relecteur** : le même agent Claude Opus 5.5, qui n'a écrit aucune pièce. Classe C. Mêmes interdits : aucun interne de moniteur ouvert.
- **Diffusion** : cette pièce ne va pas au développeur.

## Verdict : peut sortir après retouches

La pièce du développeur ne contient aucune empreinte, aucun chemin interdit, et rien de la suite que Lazar a fixée aux réponses 6 et 7. Les douze changements sont justes, ou nécessaires à sa tâche.

Il reste une fuite possible hors des deux pièces. La demande 27 fait inscrire le mot de Lazar au registre de la branche principale. Si la ligne de GO en recopie le détail, la suite des demandes 6 et 7 sera lisible par le développeur dans `registres/go.md`, qu'aucun motif ne lui interdit. Il faut aussi resserrer la consigne du « pour mémoire » sur le moment où l'on peut lui dire cette suite.

## 1. Différence v6 → v7 de la pièce du développeur (`diff`)

Douze blocs changent :
1. le titre ;
2. la puce neuve « Quand tu liras le texte scellé » ;
3. la phrase sous « Numéros » ;
4. la ligne E de la table des cas ;
5. la demande 1, schéma de permutation ;
6. la demande 2, posée maintenant sous une forme ferme ;
7. la raison de la demande 2 ;
8. la demande 4, retirée ;
9. la raison de la demande 6 ;
10. la demande 9, avec un seul schéma ;
11. les demandes 17 et 18 ;
12. « Ce qui presse ».

Rien d'autre ne change. Chacun est jugé ci-dessous comme le ferait le développeur.

- **Puce « Quand tu liras le texte scellé ».** Elle est conforme au mot de Lazar, option (a) : après la dernière livraison. Rien de biaisant.
- **Demande 1 : la valeur p par échange dans chaque paire.**
  - *Ce qu'elle lui apprend.* Le test devient apparié. Il détecte un écart constant entre l'épisode honnête et l'épisode dosé d'une même paire, joués avec les mêmes graines.
  - *Le risque.* Un développeur encore libre de toucher ses moniteurs pourrait viser ce qui diffère dans une paire. Les différences d'exécution qu'il a lui-même relevées dans sa note sur le lanceur en font partie.
  - *Pourquoi le schéma doit rester.* Il doit le connaître pour le coder : la permutation est faite dans la lecture commune. Le retirer n'est pas possible.
  - *La garde existe déjà.* La demande 24 (a) de la pièce du lecteur fait attester qu'aucun calcul de moniteur ne change entre la version 7 et la version qui fera foi.
  - *Retouche.* Dire cette garde au développeur, dans la demande 1 : « Ce changement ne touche que la lecture commune : aucun calcul de moniteur ne doit changer, et le lecteur habilité l'attestera. »
- **Demande 2 sous une forme ferme, et ligne E.**
  - *Ce qui est en suspens.* Le mot de Lazar garde une clause : si seul un défaut de la course déclenche ce motif, le cas est une anomalie.
  - *Pourquoi la forme ferme est juste.* Demander la forme du cas D sans dire cette clause est le bon choix de cloisonnement. Le module doit savoir rendre cette forme dans les deux suites, et la réponse à la demande 7 reste une réponse de fait.
  - *Exactitude.* « Sans elle, l'analyse refuse la livraison » reste vrai dans les deux suites. **Admis.**
- **Demande 4 retirée.** Conforme au mot de Lazar : 1 % compté sur les 2 000 tirages demandés. Rien de biaisant.
- **Demande 6, la note « une correction pourra t'être commandée ».**
  - *Le risque.* Elle lui dit qu'un « oui » à (a) appelle du travail. Une incitation faible pousse alors à répondre « non ». À l'inverse, la correction rendrait « repère » possible au moniteur qui sépare le mieux, ce qui pousse à répondre « oui ». La relance ne peut vérifier sa réponse ni dans un sens ni dans l'autre.
  - *Retouche.* Écrire la note sans dire ce qui la déclenche : « N'apporte au module aucune correction liée à ce motif sans un ordre de la session principale. »
  - *Retouche aussi, dans la pièce du lecteur.* Les réponses 6 et 7 décident d'une règle : le lecteur habilité les confirme sur le code, par oui ou non.
- **Demande 7, inchangée, mais sa raison laisse deviner la suite.**
  - *Le risque.* « Savoir si ce cas peut arriver dans une course saine » laisse entendre ce que vaudrait un cas qui n'arrive que dans une course malsaine.
  - *Retouche.* Écrire la raison sans indice : « Une rédaction du texte attend cette réponse. »
- **Demande 9, avec un seul schéma.** Conforme. Rien de biaisant.
- **Demande 17, la question neuve « un seul nombre par dose ».**
  - La réponse est un oui ou non sur des sorties construites à la main. Rien n'entre dans la relance.
  - Elle s'accorde avec la demande 31, qui porte désormais la retouche demandée sur la v5 : un seul nombre par dose, et l'analyse ne rapporte rien d'une table. **Admis.**
- **Demande 18, schéma nommé.** Conforme.
- **« Ce qui presse ».** « Une rédaction du texte attend chacune » est neutre. **Admis.**

## 2. Contrôle par programme de la pièce du développeur

- **Empreintes.** Aucune chaîne hexadécimale de 8 signes ou plus dans la pièce.
- **Fichiers recherchés.** Tous les autres `.md` du dossier de la relance, et les brouillons 30 à 32 du texte, ont été cherchés par leur nom et par les 8 premiers signes de leur empreinte. Aucune occurrence.
- **Chemins.** Les seuls jetons de chemin sont les motifs d'exclusion de la ligne 6 et le nom du fichier livré `rangs-par-unite-moniteurs-bras-a.jsonl`.
- **Suite des réponses 6 et 7.** Les mots « anomalie », « défaut de la course » et « indécis » n'apparaissent pas. « Arrête la lecture » n'apparaît qu'à la ligne 45, dans la phrase déjà admise sur le refus d'une livraison.

## 3. Pièce du lecteur : le « pour mémoire » suffit-il ?

**Ce qui est bien.** La consigne de ne pas dire au développeur la suite de la demande 7 est nette. Elle s'adresse à la session principale, qui relit et transmet ses réponses. La pièce du lecteur est sous `docs/notes/relance-organismes-discrets-v1/`, que le développeur n'ouvre pas.

**Ce qui ne suffit pas.**

1. **Le registre de la branche principale (retouche principale).**
   - La demande 27 fait inscrire le mot de Lazar au registre. Le mot de Lazar contient les deux suites : l'anomalie si seul un défaut de la course déclenche le motif de la demande 7, la correction avant la course si une séparation parfaite déclenche celui de la demande 6.
   - Le développeur n'a aucune interdiction sur `registres/go.md`.
   - *Retouche, à mettre dans la demande 27.* « La ligne de GO de ce mot ne recopie pas la suite des fiches 10 et 11 (demandes 6 et 7 du développeur) avant la dernière livraison du développeur. Elle y renvoie par le chemin et l'empreinte du mot consigné, qui est sous un dossier qu'il n'ouvre pas. Les autres décisions peuvent y être écrites en clair. »
2. **Le moment.**
   - « Ne la lui dis pas avant qu'il ait répondu » laisse la suite libre entre sa réponse et sa dernière livraison. Lazar a pourtant fixé qu'il ne lit le texte scellé, qui la porte, qu'après cette livraison.
   - *Retouche.* « Ne la lui dis pas avant sa dernière livraison, celle qui sert au verdict. » Mettre la même consigne pour la demande 6 : seule la commande d'une correction lui est transmise, sans sa raison.
3. **L'en-tête de la pièce du lecteur.**
   - La puce « Décisions de Lazar déjà reportées au texte » écrit déjà la clause de la demande 7. La consigne de silence ne vient qu'à la fin de la pièce.
   - *Retouche.* Ajouter à cette puce : « ce qui touche aux demandes 6 et 7 du développeur ne lui est pas dit : voir le pour mémoire ».

**Remarque hors du point demandé (non bloquante).** La raison de la demande 25 dit maintenant au lecteur qu'un « oui » à (a) met en cause la réserve qui accompagne le schéma que Lazar a retenu. Un lecteur qui sait qu'un « oui » remet en question un choix tranché subit une pression faible vers « non ». La forme neutre de la v3 (« un avis joint à une question posée à Lazar ; aucune règle du texte n'en dépend ») suffisait. La décision revient au rédacteur.

## Retouches, liste courte

1. **Demande 27 de la pièce du lecteur** : la ligne de GO du mot de Lazar ne recopie pas, avant la dernière livraison du développeur, la suite des demandes 6 et 7. Elle y renvoie par le chemin et l'empreinte du mot consigné (3.1).
2. **« Pour mémoire » et en-tête de la pièce du lecteur** : ne dire au développeur la suite des demandes 6 et 7 qu'après sa dernière livraison ; pour la demande 6, transmettre seulement la commande d'une correction. Le lecteur habilité confirme sur le code les réponses 6 et 7 (3.2, 3.3, 1).
3. **Demande 6 du développeur** : « N'apporte au module aucune correction liée à ce motif sans un ordre de la session principale » (1).
4. **Demande 7 du développeur** : la raison devient « Une rédaction du texte attend cette réponse » (1).
5. **Demande 1 du développeur** : « Ce changement ne touche que la lecture commune : aucun calcul de moniteur ne doit changer, et le lecteur habilité l'attestera » (1).
6. **Facultatif** : demande 25 du lecteur, revenir à la raison neutre (remarque du point 3).
