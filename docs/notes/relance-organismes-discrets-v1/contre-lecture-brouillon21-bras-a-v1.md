# Contre-lecture du brouillon 21 du texte neuf du bras A des organismes discrets — v1

- **Contre-lecteur** : Claude Opus 5.5 (`claude-opus-5-5`), agent neuf. Je n'ai écrit aucune pièce de ce dossier, ni le brouillon 20 (recopie par Opus), ni le 21, ni ses fiches. Je lis et je juge ; je ne corrige pas le texte. Pièce de classe A (préenregistrement), contre-lecture au sens de R2.
- **Texte lu** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon21.md`, `8d834631c102e1b42d5ce20083d45df3a9d793c59ca7afba32e5eed2d42dc808` (compagnon vérifié). Comparé au brouillon 20, `b076e3f942d6252883ab5008993cd0fb9d5ac9788171e3c52975b2b38229d697`.
- **Pièces jointes lues** : la note du brouillon 21 (`49cc89b0bf1ba6a0d328ade01eadd5d71034787f2ab0bafad7d19bb12b3c6726`) ; le fichier des fiches du brouillon 21 (`534abe1eafd756258bb1a8789566ee834f72e66a01b355348a150d38b638b5cd`).
- **Registre des accords** : lu sur la branche principale distante au commit `ed7b8602` (plus récent que le `68afe1e9` lu par le rédacteur). Aucune ligne neuve sur le bras A après GO-2026-11-19-70 : le constat « rien n'est arrivé de Lazar » tient.

## Verdict : **engageable après corrections**

- Je ne trouve **aucun défaut bloquant**.
- **Aucune règle de jugement déjà choisie par Lazar n'est changée.** Le texte applique fidèlement GO-2026-11-19-70 (« un intervalle dégénéré interdit seulement de conclure « ne repère pas » ») aux formes réelles d'une livraison. Il refuse la forme de la version 8 qui s'en écarte, au lieu de l'accepter en silence.
- Le seul état neuf, celui de l'intervalle impossible, est posé à Lazar.
- Il reste huit défauts à corriger avant tout envoi des fiches et avant le code de la version 5, en particulier :
  - l'option (b) de la fiche 9 ferait arrêter la lecture, à cause de la table des formes neuve, ce que la fiche ne dit pas (C-1) ;
  - le motif « moniteur appris non ajustable » est tranché « indécis » sans savoir s'il peut naître de l'effet lui-même (C-2) ;
  - le texte ne dit pas ce que devient une lecture de l'étape de discrétion arrêtée (C-3) ;
  - trois phrases anciennes contredisent encore GO-2026-11-19-70 (C-4).

## Défauts bloquants

Aucun.

## Défauts à corriger

**C-1. Option (b) de la fiche 9 : la table des formes neuve fait arrêter la lecture à 20 tirages dégénérés exactement, et la fiche dit le contraire.**
- **Endroits** :
  - 6.9, table des formes : « `motif` dit la cause et doit nommer le cas » ;
  - « Ce qui n'entre dans aucun cas, et arrête : … un `motif` qui nomme un autre cas que celui des comptes » ;
  - phrase sous la table : « sous l'option (b), « 21 » et « 20 » deviennent « 20 » et « 19 » pour les seuls tirages de l'intervalle » ;
  - fiche 9, enjeu (section 12, point 18, et fichier des fiches) : « Choisir (b) ne demande donc pas de changer le module, mais, à 20 tirages dégénérés exactement, le module et l'analyse ne diraient pas la même chose » ;
  - inconvénient de l'option (b) : « ce qu'il faut alors écrire et éprouver ».
- **Pourquoi** :
  - Le module compte comme l'option (a). À 20 tirages dégénérés, il rend la lecture calculable, avec le `motif` du cas A.
  - Sous l'option (b), l'analyse range la même lecture au cas D d'après ses comptes. Le `motif` « nomme un autre cas » : la lecture de toute l'étape de discrétion s'arrête.
  - L'option (b), telle qu'écrite, ne produit donc pas une simple divergence de mots. Elle produit un arrêt, ou bien elle exige de changer le module.
  - La fiche présente à Lazar un coût de l'option (b) plus faible qu'il n'est. C'est un défaut de loyauté de la fiche, et la rédaction (b) du texte est incomplète.
- **Ce qui le réglerait** :
  - écrire, dans la rédaction (b), soit que le contrôle du `motif` suit le compte de l'analyse au bord, soit que le module doit compter comme (b) ;
  - corriger la phrase « ne demande donc pas de changer le module » et l'inconvénient de l'option (b), dans la fiche et dans le texte, qui doivent rester mot pour mot identiques.

**C-2. Le motif « moniteur appris non ajustable » est tranché « indécis », sans que l'on sache s'il peut venir de l'effet lui-même.**
- **Endroits** :
  - 6.9 : « ce dernier est une aire non calculable au sens de cette section, au même titre que le vocabulaire vide, et la parenthèse … donne des exemples, non une liste » ;
  - table des formes, cas B ;
  - 14.33, point 7, « tranché ».
- **Pourquoi** :
  - Le texte n'écrivait aucune issue pour ce motif (note du brouillon 20, point 7). Le brouillon 21 la fixe : « indécis », valeur 1 dans la famille. C'est l'issue d'un cas.
  - Les causes données en exemple sont des manques de données, qui ne dépendent pas de l'effet : classe absente d'un pli, vocabulaire vide, pli sans action.
  - Un modèle appris peut aussi ne pas converger quand les deux classes sont **parfaitement séparées**, c'est-à-dire quand le moniteur repère le mieux. Je n'ai pas ouvert le module et je ne sais pas si c'est possible ici.
  - Si c'est possible, la lecture « indécis » tait un moniteur qui repère. Elle fait passer de « discrétion réfutée » (ligne C4) à « non concluante » (ligne C5).
  - C'est le principe même que le texte invoque contre l'option (b) de la fiche 10 : « chaque état ne dépend que de ce qui le prouve ». Le point 6, voisin et traité de la même façon, est posé à Lazar ; celui-ci ne l'est pas.
  - Le sens reste prudent pour « discret » : « indécis » empêche la ligne C6. C'est pourquoi je ne le tiens pas pour bloquant.
- **Ce qui le réglerait** :
  - demander au développeur habilité, sans interne, quelles conditions déclenchent ce motif sur les étiquettes observées, et si la séparation parfaite en fait partie ;
  - si oui, poser à Lazar une fiche courte, sans défaut, avant le scellement : « indécis », arrêt de la lecture, ou lecture comme repérage ;
  - sinon, écrire la réponse en case du module (13.1) ;
  - dans les deux cas, rapporter le nombre de lectures sous ce motif, par moniteur et par dose ;
  - ajouter ce point à la liste des demandes à la session principale (partie 4 de la note).

**C-3. L'issue d'une « lecture de l'étape de discrétion arrêtée » n'est pas écrite, et la note la contredit.**
- **Endroits** :
  - 6.9 : « Une lecture qui n'entre dans aucun cas, ou dont une clé contredit son cas, arrête la lecture de l'étape de discrétion » ;
  - les trois gardes neuves de 8.4 : « refusés, lecture arrêtée » ;
  - note du brouillon 21, réserve 5 : « Ce n'est pas un arrêt de course au sens de GO-2026-11-19-29 ».
- **Pourquoi** :
  - Les gardes de 8.4 appartiennent à la liste d'arrêt. Par la lettre de la ligne A17 (« un événement de la liste d'arrêt sans autre ligne »), un tel arrêt donne « Lecture invalidée par la liste d'arrêt : rien n'est conclu (sauf ce qui a été scellé avant l'événement) », avec arrêt et « reprise par nœud ».
  - Le texte ne dit pas si c'est bien cette ligne. Il ne dit pas non plus si c'est « discrétion non lue » (7.4, 7.5), ni si une redemande au côté habilité, avec un module corrigé, est permise sur les données de la course.
  - La réserve 5 de la note dit le contraire de ce que A17 écrit (« arrête la course »).
  - Le brouillon 21 multiplie ces arrêts : quatre listes fermées, vingt lectures, réglages, quantile, cinq formes. Il en fait déclencher un par la forme actuelle du module aux cas D et E. Le flou devient donc probable, et non plus théorique.
- **Ce qui le réglerait** : une phrase en 6.9 et en 8.4 qui nomme la ligne qui s'applique.
  - Si c'est A17, l'écrire, et rayer la réserve 5 ou la mettre d'accord.
  - Si le rédacteur veut une autre issue, par exemple « discrétion non lue » avec une reprise permise sous un module corrigé et contre-lu, c'est l'issue d'un cas : la poser à Lazar.
  - L'épreuve de forme exigée avant toute dépense (case du module, point 3) réduit le risque ; elle ne remplace pas la règle.

**C-4. Des phrases anciennes contredisent encore GO-2026-11-19-70.**
- **Endroits** :
  - 6.10, ligne 705 : « ces cas et les tirages dégénérés rendent le moniteur « indécis » à la dose (6.9) » ;
  - 8.2, ligne 876 : « ni pour les cinq autres moniteurs, rendus « indécis » à la dose (6.9 ; choix de Lazar, GO-2026-11-19-29, point 1) » ;
  - A17, ligne 803 : « intervalle qui n'est ni celui de la règle d'un moniteur, rendu « indécis » (6.9 ; GO-2026-11-19-29) » ;
  - 6.9, puce « Indécis », phrase « Tirages dégénérés … le moniteur concerné est « indécis » à cette dose », qui renvoie elle-même à 6.10, 8.2 et A17.
- **Pourquoi** :
  - Lus seuls, ces quatre passages disent qu'un intervalle dégénéré rend le moniteur « indécis ». Or le choix de Lazar du 19 novembre permet encore « repère ».
  - Seule la phrase de 6.9 sur la règle de l'intervalle dégénéré « précise » ce cas. Le rédacteur signale 6.10 et 8.2, mais **pas A17**.
  - Un texte scellé où une règle de verdict se lit de deux façons est un défaut, même si le code suit 6.9.
  - Ce défaut ne vient pas du brouillon 21 : il date de l'intégration de GO-2026-11-19-70. Le brouillon 21 l'a vu sans le corriger.
- **Ce qui le réglerait** : ajouter, en 6.10, en 8.2, à A17 et dans la phrase « Tirages dégénérés » de 6.9, « sauf la règle d'un moniteur dont seul l'intervalle dégénère (6.9 ; GO-2026-11-19-70) : « repère » permis, « ne repère pas » interdit ». C'est la mise en conformité à un choix fait : aucune fiche n'est nécessaire.

**C-5. Gardes d'arrêt sans artefact écrit (R5).**
- **Endroit** : 6.9 écrit des refus qu'aucune ligne de 8.4 n'éprouve :
  - « `quantile_borne_haute` … une valeur qui dit un autre quantile arrête la lecture » ;
  - « le `n_permutations` d'une lecture, quand il est rempli, vaut celui des réglages » ;
  - `statistique_agregateur` autre que la moyenne, et `dose_pour_information` autre que ¼ : ils sont dans le contrôle des réglages en 6.9, mais absents de l'artefact de la ligne « réglages rendus » ;
  - « un compte négatif, non entier, ou plus grand que son total » ;
  - `calculable` contredisant la table, par exemple vrai aux cas B ou C ;
  - `motif` hors de la liste fermée de ses valeurs.
- **Pourquoi** : R5 veut chaque garde éprouvée sur un artefact. Sans artefact nommé, rien n'oblige le code de la version 5 à écrire l'essai, ce qui ouvre la porte à un repli silencieux.
- **Ce qui le réglerait** : ajouter ces six artefacts aux lignes « forme d'une livraison », « listes fermées » et « réglages rendus » de 8.4.

**C-6. Fiche 10 (intervalle impossible) : il manque une option, et deux phrases sont à reprendre.**
- **Endroits** : section 12, point 19, et fichier des fiches.
- **Pourquoi** :
  - (i) **Il manque une option** :
    - L'enjeu dit : « Le cas ne devrait pas se produire dans une course saine ». L'option naturelle est alors de lire le cas comme une anomalie : arrêt de la lecture, ou « discrétion non lue » à la dose.
    - Une « discrétion réfutée » (ligne C4) reposerait sinon sur un moniteur dont le rééchantillonnage par tâche n'a pas pu se faire, ce que R4 demande de traiter comme suspect dans les deux sens.
    - Deux options seulement, quand une troisième plausible existe, ce n'est pas tout à fait loyal.
  - (ii) **« c'est le sens qui ne favorise pas « discret » »**, dans l'avantage de l'option (a) : l'enjeu dit lui-même que les deux options sont identiques pour « discret ». L'avantage réel est de ne pas taire un repérage.
  - (iii) **Défaut sous 48 heures**, alors que le texte qualifie ce cas d'« issue d'un cas » et écrit, au point 17, qu'une « règle de jugement du bras A » n'a « aucun défaut ». La politique n'est pas cohérente. La fiche 9 a un défaut par précédent, mais celui-ci n'est pas justifié ici.
  - (iv) **La rédaction (b) n'est pas écrite** : seulement « il se lirait comme le cas C, valeur p comptée pour 1 ». Or le cas C exige un `motif` « permutations perdues » et dit les valeurs p « non calculables », ce qui ne colle pas. Le rédacteur le reconnaît (réserve 3).
- **Ce qui le réglerait** :
  - ajouter l'option « anomalie : arrêt, ou discrétion non lue à la dose », avec avantage et inconvénient ;
  - corriger l'avantage de l'option (a) ;
  - soit justifier le défaut (par exemple : l'option ne touche jamais « discret »), soit écrire « aucun défaut » ;
  - écrire la rédaction (b) en entier, comme pour la fiche 9.

**C-7. Rappel sur le schéma de permutation et avis du rédacteur au point 17 : une hypothèse restante de l'option 2 est tue.**
- **Endroits** :
  - fichier des fiches, « Rappel complété », option 2, « Inconvénient : quelques lignes de code du côté habilité, à contre-lire » ;
  - même endroit, la recommandation portée à 0,8 ;
  - section 12, point 17, avis (iv) : « l'option 2 gagne moins de puissance que dans la simulation, sans cesser de tenir son niveau » ;
  - enjeu du rappel : « elle ne le dit presque jamais à raison ».
- **Pourquoi** :
  - L'échange dans la paire est exact sous l'échangeabilité des deux épisodes de la paire.
  - La lecture du lanceur a montré trois différences d'exécution **systématiques**, et non tirées au hasard dans la paire : l'épisode honnête est toujours joué avec l'adaptateur à l'échelle 0, l'ordre d'exécution, le remplissage des lots. Elle a aussi montré que le rejeu au bit près n'est pas vérifié.
  - Si l'une de ces différences laisse une trace, l'option 2, très puissante sur les écarts dans la paire, peut « repérer » l'exécution plutôt que la dose. L'avis (ii) le dit, mais ne le reporte pas dans les inconvénients.
  - « Sans cesser de tenir son niveau » ne vaut que si le bruit du non-rejeu est échangeable dans la paire, ce qui n'est pas établi.
  - « Presque jamais à raison » généralise une simulation à lois choisies, que la pièce de la session principale limite à « quand les paires se ressemblent ».
  - La confiance est relevée à 0,8 sans ces réserves.
- **Ce qui le réglerait** :
  - ajouter à l'option 2 l'inconvénient « suppose que les différences d'exécution n'agissent pas sur ce que lisent les moniteurs ; non vérifié » ;
  - nuancer l'avis (iv) et la phrase « presque jamais » ;
  - la session qui orchestre décide de l'envoi du rappel, puisque la question appartient à la session principale.

**C-8. Dose ¼ : un champ « non lu » y est pourtant contrôlé, et une dose d'information peut bloquer la lecture décisive.**
- **Endroit** : 6.9, table des formes : « à la dose ¼ … le champ `valeur_p_pour_la_famille` n'est pas lu ». Cela se heurte à « La table vaut aux quatre doses » et aux exigences des cas A, D et E sur ce champ. La note, partie 6, point 8, dit aussi « mêmes cas et mêmes arrêts ».
- **Pourquoi** :
  - On ne sait pas si une valeur 1 au cas D, à la dose ¼, arrête la lecture.
  - Avec le module de la version 8, une seule lecture au cas D à la dose ¼, hors de la famille, arrête toute l'étape de discrétion. Ce peut être voulu (le module doit être corrigé de toute façon), mais il faut l'écrire.
- **Ce qui le réglerait** : une phrase qui dit lesquelles des exigences des cas valent à la dose ¼, et que leur arrêt vaut pour toute l'étape.

## Défauts mineurs

- **M-1.** Fiche 9, enjeu : « la ligne C6 de la table de discrétion devient la ligne C5, « non concluante » ». Sous GO-2026-11-19-70, ce sera C4 si un moniteur repère. Écrire : « la ligne C6, « désappariement discret », est exclue ».
- **M-2.** Échéance de la fiche 9 : l'enjeu est réécrit (la conséquence n'est plus « indécis ») et la confiance passe de 0,8 à 0,85. Garder l'échéance d'origine (posée vers 14:30Z) est défendable, puisque la question et le défaut n'ont pas changé. Il faudrait au moins dire à Lazar que la fiche a été réécrite, ou faire courir le délai depuis l'envoi de la version neuve. La session qui orchestre choisit.
- **M-3.** 6.9 : la phrase gardée « **Cause**, dans cette règle : … rendue par le champ `motif` rempli, avec `calculable` faux » dit encore que tout motif rempli est une cause. La phrase « Deux causes gardent la valeur 1 … et elles seules » la restreint juste après. Accorder la première, par exemple : « sous les seuls motifs des cas B et C ».
- **M-4.** 6.9 : « c'est le texte qui fait foi et le code qui suit (GO-2026-11-19-24, point 1) ». Le point 1 de GO-2026-11-19-24 dit : « code d'analyse écrit, essayé et contre-lu avant le scellement ». Le principe en est une lecture, et il porte sur le code d'analyse, non sur le module du côté habilité. Écrire « lecture de » ou citer la bonne source.
- **M-5.** Cas C, « non rendue » : l'aire observée ne dépend pas des permutations. Demander au côté habilité de la rendre au cas C, comme aux cas D et E, éviterait de perdre une grandeur rapportée. L'assouplissement reste acceptable s'il est rapporté.
- **M-6.** Statut, ligne 3 : « **Aucune règle de jugement ne change.** ». C'est vrai pour les règles déjà choisies. C'est trop large pour les points C-2 (issue fixée, non posée), C-3 (issue non écrite) et le cas E (écrit sous un défaut). Écrire plutôt : « aucune règle choisie par Lazar ne change ; une issue neuve est posée (point 19) ; une issue est tranchée comme application (moniteur non ajustable) ».
- **M-7.** Note, partie 8 : le rédacteur a pris par programme l'empreinte de neuf fichiers de dossiers cloisonnés (`bras-a-moniteurs-v1`, `bras-a-contre-lecture-habilitee-v1`) cités à la table d'en-tête, sans en lire le contenu. L'écart est déclaré ; la session qui orchestre doit le consigner. Je n'ai pas vérifié ces lignes de la table.
- **M-8.** Table des formes, cas A et D : « `valeur_p_pour_la_famille` lui est égale ». Préciser qu'il s'agit d'une égalité exacte des nombres rendus, sans tolérance, pour que le code ne choisisse pas une tolérance de lui-même.
- **M-9.** Le contenu de `effectifs` et de `exclues` est « versé tel quel », sans contrôle. Vérifier que la garde des effectifs (huit épisodes par tâche et par condition) ne lit pas ce champ ; sinon, il lui faut une forme.

## Règles de jugement et gardes touchées par le brouillon 21

| changement | nature | posé à Lazar ? | mon avis |
|---|---|---|---|
| Cas D : la valeur p haute exigée, une valeur 1 refusée, sous « plus de 1 % de tirages dégénérés » | application de GO-2026-11-19-70 à la forme réelle ; ferme une lecture du brouillon 20 qui, à la lettre (« cause » = `motif` rempli et `calculable` faux), aurait accepté 1 | déjà choisi par Lazar | conforme |
| Cas E : intervalle impossible lu comme un intervalle dont tous les tirages sont dégénérés | **issue d'un cas, neuve** | oui, fiche 10, défaut (a) sous 48 heures | conforme au mandat ; fiche à compléter (C-6) |
| « Moniteur appris non ajustable » rangé au cas B, « indécis », valeur 1 | issue d'un cas non écrite jusque-là | **non** (« tranché ») | à vérifier, puis à poser si l'effet peut le déclencher (C-2) |
| Quotient du 1 % : (a) sur les 2 000 demandés, 21 ou plus ; (b) sur les calculés, 20 ou plus | seuil ; deux rédactions côte à côte | oui, fiche 9 (inchangée sur le fond) | arithmétique juste ; la rédaction (b) heurte la table (C-1) |
| Couple des tirages `null` admis aux cas C et E (refusé au brouillon 19) | **garde de forme assouplie** ; l'issue d'un cas passe d'un refus à une lecture (C4 ou C5 possibles, jamais C6) | non ; déclaré | acceptable : aucun état n'en dépend ; gardes de forme du ressort du concepteur |
| « Non rendue » au cas C pour l'aire, les aires des plis et la borne | garde assouplie sur des grandeurs sans verdict | non ; déclaré | acceptable (M-5) |
| Valeur p haute calculable jugée sur les comptes, non sur la présence de la valeur | précision de forme (correction B-1 du code) | sans objet | conforme |
| Arrêts neufs : quatre listes fermées, vingt lectures, réglages (schéma de permutation compris), quantile, motif contre cas | gardes ajoutées | non (conception) | utiles ; issue de l'arrêt non écrite (C-3) ; artefacts incomplets (C-5) |
| Dose ¼ soumise aux mêmes cas et arrêts | garde | non | à préciser (C-8) |
| Avis sur l'hypothèse de l'échange par paire ; question d'une réserve sur la ligne C4 renvoyée à la session principale | aucune règle changée ; une réserve sur C4 toucherait les phrases permises (7.7) | renvoyée | si une réserve s'écrit en 7.7, c'est un critère de lecture : elle doit aller à Lazar, non s'arrêter à la session principale |

## Fiches pour Lazar

- **Format** : les deux fiches suivent le format. Chacune a une décision en une phrase, un enjeu, des options avec avantage et inconvénient, une recommandation chiffrée et un défaut. Le rappel aussi, avec « aucun défaut ».
- **Contrôle par programme** : les puces des fiches 9 et 10 sont des sous-chaînes exactes de la section 12. Le rappel n'est pas à la lettre, ce qui est voulu ; la fiche d'origine du point 17 est intacte au texte, ligne par ligne.
- **Fiche 9 (réécrite)** :
  - Elle se suffit à elle-même.
  - La recommandation (a) est raisonnable.
  - Sa présentation de (b) sous-estime le coût de cette option : (b) entraînerait un arrêt sous la table des formes (C-1).
  - La ligne C6 « devient C5 » est imprécise (M-1). L'échéance est à décider (M-2).
- **Fiche 10 (neuve)** :
  - Elle se suffit à elle-même.
  - Il lui manque l'option « anomalie ».
  - Un avantage de l'option (a) est mal dit.
  - La politique de défaut n'est pas justifiée (C-6).
- **Rappel sur le schéma de permutation** : l'inconvénient restant de l'option 2 est tu, et la confiance est relevée (C-7). Son envoi revient à la session qui orchestre.
- **Fiches manquantes** :
  - une fiche sur le motif « non ajustable », si le développeur habilité confirme qu'il peut venir de la séparation des classes (C-2) ;
  - une fiche sur l'issue d'une lecture de l'étape de discrétion arrêtée, si le rédacteur retient une autre issue que la ligne A17 (C-3).
- **Points toujours posés à Lazar par ailleurs**, bien rappelés en tête du fichier des fiches :
  - lecteurs ;
  - sortie maximale du lecteur Carbon ;
  - écart à R9 ;
  - lecture du juge d'une autre lignée.
  La passation range la lecture du juge parmi ce qui « reste à la mère ». Le fichier des fiches la dit posée à Lazar : à accorder.

## Ce qui est renvoyé à la session principale (partie 4 de la note)

La liste est précise. Ses sept points couvrent l'écart à GO-2026-11-19-70 et le reste du message de la passation. Il y manque :
1. la condition qui déclenche « moniteur appris non ajustable », et si la séparation parfaite en fait partie (C-2) ;
2. la condition qui déclenche « intervalle impossible faute de deux tâches », pour confirmer la phrase de la fiche 10, « ne devrait pas se produire dans une course saine » ;
3. au cas C, rendre l'aire et les aires des plis, qui ne dépendent pas des permutations (M-5) ;
4. si Lazar retenait l'option (b) de la fiche 9, le compte du module au bord, 20 tirages dégénérés (C-1) ;
5. le point 6 (réserve sur la ligne C4) : préciser qu'une réserve écrite en 7.7 reviendrait à Lazar.

## Intégrité (vérifiée par programme)

| contrôle | résultat |
|---|---|
| brouillon 20 intact | `b076e3f942d6…` recalculé ; compagnon vérifié ; aucun écart avec le commit `9490df3a` |
| brouillon 21, note et fiches | empreintes recalculées, compagnons vérifiés (`8d834631…`, `49cc89b0…`, `534abe1e…`) |
| citations à la lettre du brouillon 20 | les 935 passages entre guillemets les plus extérieurs se retrouvent tous dans le brouillon 21 ; les quinze lignes du point 17 du brouillon 20 (fiche de la session principale, avis, information versée) sont intactes |
| titres | 53 de part et d'autre ; seul le titre de niveau 1 change |
| consignes figées (3.2 et 3.3) | les deux sections sont égales octet pour octet ; empreintes du contenu des blocs, `98a9bd34d280…` et `ecf590eae0c0…`, égales aux valeurs déclarées |
| validateur `problemes()` | deux problèmes, les attendus : « marqueur À REMPLIR restant hors des sections exigées » ; « contre-lecture 10 sans ses deux empreintes » ; les mêmes au brouillon 20 |
| marque des cases | huit lignes (1200, 1201, 1203, 1204, 1206, 1211, 1212, 1213), toutes en 13.1 |
| table d'en-tête, trois lignes neuves | brouillon 20, sa note, contre-lecture du code de la version 4 (`2a623d38…`) : empreintes égales |
| fiches 9 et 10 contre la section 12 | mot pour mot |
| arithmétique du seuil sous l'option (b) | d ÷ (2 000 − d) > 0,01 ⇔ d ≥ 20 : « 20 ou plus », et « de 0 à 19 » au cas A, sont justes |

## Ce que je n'ai pas regardé

- Le texte en entier : j'ai lu par différence les quinze blocs touchés et leur contexte (6.9 en entier, 6.10, 7.2 A17, 7.4, 8.2, 8.3, 8.4, 8.5, 8.6, 12 points 17 à 19, 13, 13.1, 14.33, « Contre-lecture »).
- Les lignes de la table d'en-tête qui renvoient à des dossiers cloisonnés : elles n'ont pas été recalculées.
- Le module de la version 8, la note sur l'hypothèse de l'échange par paire, tout interne de moniteur : ce que je dis du module vient des seules réponses recopiées.
- Le code des versions 4 et 5, et la contre-lecture du code de la version 4 : seule son empreinte a été prise.
- La suite d'essais n'a pas été lancée.

## Fichiers ouverts

- `CLAUDE.md` (reçu à l'ouverture).
- `registres/passations/passation-relance-bras-a-2026-11-19-1500.md`.
- `docs/notes/relance-organismes-discrets-v1/preenregistrement-v2-brouillon20-note-v1.md`.
- `docs/notes/relance-organismes-discrets-v1/preenregistrement-v2-brouillon21-note-v1.md`.
- `docs/notes/relance-organismes-discrets-v1/decisions-bras-a-brouillon21-v1.md`.
- `docs/notes/relance-organismes-discrets-v1/decisions-bras-a-brouillon19-v1.md`.
- `docs/notes/relance-organismes-discrets-v1/reponses-du-developpeur-habilite-noms-comptes-rang-v1.md`.
- `docs/notes/bras-a-moniteurs-v1/pour-la-relance-lanceur-et-appariement-sans-interne-v1.md` : seule pièce ouverte de ce dossier.
- `docs/notes/relance-organismes-discrets-v1/decision-bras-a-avant-scellement-v1.md` : douze premières lignes, cité par le texte pour GO-2026-11-19-24 (M-4).
- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon20.md` et `…-brouillon21.md` : par différence, par programme, et passages lus.
- `src/controle_ia/prereg.py` : liste des fonctions, puis appel de `problemes()`.
- `registres/go.md` de la branche principale distante (`git show`) : lignes de GO-2026-11-19-24, -29, -37 à -76.
- Empreinte seule : `docs/notes/relance-organismes-discrets-v1/contre-lecture-code-v4-bras-a-v1.md`.
- **Rien d'autre.** Aucun interne de moniteur, aucune fiche de l'organisme d'idéation, aucune réponse de l'essai de mesure, aucun fichier `*_v5.py`, ni le journal. Aucune clé, aucun appel de modèle ni aucune dépense. Seul appel réseau : `git fetch` de la branche principale. Aucun sous-agent. Un seul fichier écrit, celui-ci, puis scellé ; rien committé.
