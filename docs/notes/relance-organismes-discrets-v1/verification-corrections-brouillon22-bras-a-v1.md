# Vérification des corrections du brouillon 22 du texte neuf du bras A des organismes discrets — v1

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`). C'est moi qui ai contre-lu le brouillon 21 (`contre-lecture-brouillon21-bras-a-v1.md`, `6b155c84…`). Je vérifie ici les corrections, comme le veut l'allègement de la procédure pour une pièce de classe A, et je ne corrige rien moi-même.
- **Texte vérifié** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon22.md`, `ade786eb4065722aee6b05ce8246767dd8cf5f52bff16463f7c59b95547a0396`, commit `a95b1d52`.
- **Pièces jointes** : la note du brouillon 22 (`8f5480f4…`) et le fichier des fiches du brouillon 22 (`80581f3c…`). Leurs compagnons sont vérifiés.
- **Méthode** : comparaison des brouillons 21 et 22 phrase par phrase, faite par programme. J'ai lu les 23 blocs touchés, avec leur contexte. J'ai lu aussi la section 7.5, que le rédacteur n'avait pas lue, et c'est elle qui décide du défaut B-1.

## Verdict : **non engageable en l'état**, avec une correction bornée

- Presque tout est corrigé. Sur les huit défauts C du brouillon 21, sept sont tenus et un est tenu en partie (C-3) ; les neuf mineurs sont tenus.
- Les fiches 9, 10 et 11 et le rappel sont au format. Le retrait du défaut de la fiche 10 est justifié.
- Il reste un défaut bloquant, et il vient de la correction de mon C-3 :
  - le brouillon 22 range la livraison refusée sous la ligne A17 ;
  - or, par la section 7.5, la ligne A17 rend **toutes** les hypothèses « non prononcées », le désappariement compris ;
  - le texte, la note et les fiches disent pourtant que « le résultat principal, déjà scellé, reste ».
- C'est l'issue d'un cas, qui touche l'hypothèse principale du bras, choisie sans le mot de Lazar et décrite de façon inexacte dans les fiches (B-1).
- Une fois B-1 réglé, le texte est engageable après deux petites corrections (C-1 et C-2 ci-dessous).
- **Les fiches 9, 10 et 11 ne doivent pas partir avant la correction de B-1** : elles décrivent mal la conséquence de leurs options d'arrêt.

## 1. Défauts de la contre-lecture du brouillon 21

| défaut | état | endroit et constat |
|---|---|---|
| C-1 option (b) du seuil, arrêt à 20 | **tenu** | 6.9, ligne 694 : « et le module du côté habilité devrait compter de même » ; fiche 9 : « Choisir (b) demande donc de changer le module ». La conséquence est mal mesurée : voir B-1 (« arrête la lecture de toute l'étape de discrétion » ; en fait, c'est toute la course qui reste sans issue prononcée). |
| C-2 « moniteur appris non ajustable » | **tenu** | 6.9, ligne 694 : trois rédactions ; question au développeur habilité (13.1, demande 9) ; fiche 11, sans défaut ; nombre de lectures sous ce motif rapporté. Il manque la garde de 8.4 : voir C-1 neuf. |
| C-3 issue d'une lecture arrêtée | **tenu en partie, et à l'origine de B-1** | L'issue est écrite (6.9, lignes 699 et 815). Mais l'effet réel de la ligne A17 sur la course (7.5) n'est pas celui que le texte décrit. |
| C-4 phrases contraires à GO-2026-11-19-70 | **tenu** | La précision « repère permis, ne repère pas interdit » est en 6.9 (ligne 693), 6.10 (717), 6.12 point 5 (770), A17 (815) et 8.2 (888). Une recherche par programme ne trouve plus aucune phrase de règle sans elle, hors des passages qui racontent l'histoire (section 14, fiche d'origine du point 16). |
| C-5 gardes sans artefact | **tenu** | 8.4, lignes 934 à 936 : quantile, `n_permutations` d'une lecture, `dose_pour_information`, `statistique_agregateur`, compte négatif ou non entier, `calculable` vrai aux cas B ou C, `motif` hors de sa liste. Il reste un artefact manquant mineur (M-1 neuf). |
| C-6 fiche de l'intervalle impossible | **tenu** | Option (c), « anomalie », ajoutée ; avantage de l'option (a) corrigé ; défaut retiré et justifié ; trois rédactions en entier (6.9, lignes 693 et 709 à 711 ; 8.4, ligne 933). La description de l'option (c) est inexacte : voir B-1. |
| C-7 hypothèse restante de l'option 2 du schéma de permutation | **tenu** | Point 17, avis (ii) et (iv) ; dans le rappel, l'inconvénient est rendu à l'option 2, « presque jamais » est borné aux paires qui se ressemblent, la confiance passe à 0,7, et la réserve sur la ligne C4 est renvoyée à Lazar. |
| C-8 dose ¼ | **tenu** | 6.9, ligne 697 : deux sortes d'écart ; à la dose ¼, la valeur de la famille n'est ni lue ni contrôlée ; conventions, ligne 155 ; 8.4, lignes 933 et 934. |
| M-1 ligne C6 | **tenu** | « la ligne C6 … est exclue à cette dose ». |
| M-2 échéance de la fiche 9 | **tenu** | Échéance d'origine gardée et dite ; la fiche dit qu'elle a été réécrite. |
| M-3 phrase « Cause » | **tenu** | 6.9 : « sous les seuls motifs qui gardent la valeur 1 ». |
| M-4 source du principe « le texte fait foi » | **tenu** | Dit comme une lecture de GO-2026-11-19-24, étendue par le texte, « non un mot de Lazar ». |
| M-5 aire au cas C | **tenu**, comme demande | Table des formes, ligne 713 ; 13.1, demande 11. |
| M-6 statut | **tenu** | « Aucune règle choisie par Lazar ne change. Trois issues sont ouvertes, sans défaut. » Il faut compléter : la livraison refusée, rangée sous la ligne A17, est une quatrième issue choisie (B-1). |
| M-7 empreintes de fichiers cloisonnés | **tenu** dans la méthode | Le rédacteur rectifie aussi son compte du brouillon 21 : onze fichiers, et non neuf. Voir M-4 neuf. |
| M-8 égalité exacte | **tenu** | 6.9, ligne 695 ; 8.4, « fût-ce d'une décimale ». |
| M-9 `effectifs` et `exclues` | **tenu** | La garde des effectifs est bien en 6.12, point 2, et en 8.1 (vérifié). |

## 2. Défaut bloquant

**B-1. La livraison refusée est rangée sous la ligne A17, ce qui fait tomber l'issue du désappariement : le texte, la note et les fiches disent le contraire.**

**Endroits** :
- 6.9, ligne 699 : « c'est **la ligne A17** (7.2) … Rien n'est conclu sur la discrétion ; ce qui a été scellé avant l'événement est rapporté tel quel — les lignes de la table B … — » ;
- A17, ligne 815 : la livraison refusée est ajoutée « (6.9 : rien n'est conclu sur la discrétion ; les lignes de la table B, scellées avant l'étape (m), sont rapportées telles quelles) » ;
- fiche 10, option (c), et fiche 11, option (b) : « la lecture de la discrétion s'arrête, rien n'est conclu sur elle, **le résultat principal, déjà scellé, reste** » ;
- fiche 9, option (b) : « ce désaccord arrête la lecture de toute l'étape de discrétion » ;
- note du brouillon 22, partie 6, point 3 (consigne au code de la version 5) : « rien n'est conclu sur la discrétion ; les lignes de la table B, scellées avant, restent ».

**Pourquoi** :
1. **La section 7.5 dit autre chose.** « Sous toute autre ligne de la table A (course arrêtée, lecture invalide ou suspendue : A1 à A14, **A17**, A11), **aucune issue de cette section n'est prononcée, pour aucune hypothèse** : le verdict est celui de la ligne, écrit « non prononcée : [verdict de la ligne] » ; ce qui a été scellé avant l'événement est rapporté tel quel. »
   - Les autres règles de la table A vont dans le même sens : (i) le verdict de la course est **une** ligne ; (iii) après une ligne d'arrêt, aucun constat n'est rapporté comme verdict et l'audit de symétrie n'est pas joué ; la colonne « suite » de A17 dit « résultats partiels scellés, non opposables ».
   - Un défaut de forme dans les nombres que rend le côté habilité, même à la dose ¼ pour un écart de structure, ou à l'étape (n) sur des grandeurs sans verdict, rend donc le désappariement « non prononcé ». Le désappariement, qui est l'hypothèse principale du bras, ne serait plus que « rapporté tel quel ».
   - Le rédacteur n'a pas relu 7.5 (sa note, réserve 5). Ses phrases supposent que la table B reste un verdict.
2. **Ce n'est pas la lettre de A17.** La ligne énumère ses événements (« à savoir : … »). Au brouillon 21, la livraison refusée n'y figurait pas. Le brouillon 22 l'ajoute : il étend le champ d'une ligne d'une table de verdict. Le rédacteur le reconnaît (« C'est une ligne d'une table de verdict ») mais la déclare appliquée « par sa lettre ».
   - Ma contre-lecture du brouillon 21 (C-3) avait écrit elle aussi « par la lettre de la ligne A17 », sans voir 7.5. Le rédacteur a suivi ma lecture : l'erreur de départ est en partie la mienne.
3. **C'est asymétrique avec le cas voisin.** Pour les effectifs de la base différents, qui sont aussi une défaillance du côté des moniteurs, le texte écrit « discrétion **non lue** » (6.12, point 2 ; 7.5), sans toucher au désappariement. Faire tomber l'hypothèse principale pour une faute de forme du module des moniteurs est disproportionné. Ce n'est pas exigé par le texte, et Lazar ne l'a pas choisi.
4. **C'est l'issue d'un cas**, désormais probable, puisque la version 8 du module produit cette forme aux cas D et E. Ce choix est fait sans fiche, alors que les trois autres issues ouvertes de ce brouillon sont posées. Et les fiches 9, 10 et 11 décrivent à Lazar une conséquence fausse pour leurs options d'arrêt : c'est un défaut de loyauté.

**Ce qui le réglerait** :
- Poser à Lazar une fiche **sans défaut** : « ce que vaut une livraison du côté habilité refusée par une garde de 8.4 ». Options :
  - (a) ligne A17 en entier, telle que 7.5 la lit : aucune hypothèse prononcée ;
  - (b) « discrétion **non lue** », issue qui existe déjà en 7.5, le désappariement restant prononcé, et une livraison refaite sous un module corrigé et contre-lu sur un mot de Lazar ;
  - (c) une variante de (b) qui distingue l'étape (m) de l'étape (n).
- Écrire au texte les rédactions de ces options, comme pour les points 19 et 20.
- D'ici là, accorder 6.9 (ligne 699), A17, 8.4 et la note : dire que, sous la lettre actuelle, le désappariement est « non prononcé ».
- Corriger dans les fiches 9, 10 et 11 la phrase « le résultat principal, déjà scellé, reste », ou la rendre conditionnelle à l'option retenue.
- Prévenir le contre-lecteur du code de la version 5 que le point 3 de la partie 6 de la note (exception « ligne A17 », table B qui « reste ») dépend de cette fiche.
- L'épreuve de forme exigée avant toute dépense (13.1, demande 3) réduit la probabilité du cas. Elle ne remplace pas la règle.

## 3. Défauts à corriger, neufs

**C-1. Aucune garde de 8.4 pour les trois rédactions du motif « moniteur appris non ajustable » (R5).**
- **Endroit** : 6.9, ligne 694, rédaction (b), « à une dose de {½, ¾, 1}, la lecture de l'étape de discrétion s'arrête (ligne A17) ».
- **Pourquoi** : c'est un arrêt neuf, sans cas sain ni artefact. Le point 19, lui, a les siens (8.4, ligne 933).
- **Ce qui le réglerait** : une ligne « moniteur appris non ajustable (6.9 ; point 20) », écrite sur le modèle de celle de l'intervalle impossible :
  - rédaction (a) : valeur 1 et « indécis » ;
  - rédaction (b) : arrêt à une dose de la famille, aucun arrêt à la dose ¼ ;
  - rédaction (c) : une aire rendue, et la règle ordinaire.

**C-2. Les phrases du statut et de la note sur la ligne A17 sont à reprendre avec B-1.**
- **Endroits** : statut, ligne 3, « Il écrit ce que vaut l'arrêt … — la ligne A17, par sa lettre — » ; note, réserve 1, « j'applique la lettre, je ne la choisis pas ».
- **Pourquoi** : c'est une extension de la liste de A17, dont l'effet est fixé par 7.5 (B-1, point 2).
- **Ce qui le réglerait** : les récrire avec la fiche de B-1.

## 4. Mineurs, neufs

- **M-1.** 8.4, ligne 934 : l'artefact « au cas B, une aire, une valeur p ou une borne remplie », écrit dans la liste des écarts de structure de 6.9 (ligne 713), manque à la ligne « forme d'une livraison ».
- **M-2.** La fiche 9 garde son défaut sous 48 heures, alors que le texte dit qu'une règle de jugement du bras A n'a « aucun défaut » (fiches 10, 11 et rappel). L'écart est défendable : c'est le précédent, la fiche est déjà posée, et l'option (a) est celle du module. Il devrait être dit dans la fiche, en une phrase, pour que Lazar le voie.
- **M-3.** « Contre-lecture » : la contre-lecture 11, inscrite par le rédacteur, a des empreintes justes (`8d834631…`, `6b155c84…`). La session qui orchestre doit la confirmer. La présente vérification des corrections est à inscrire de même avant le scellement, avec son empreinte.
- **M-4.** La rectification du compte des fichiers cloisonnés dont le programme du brouillon 21 a pris l'empreinte (onze, dont `prereg/T0.6-organismes-config-7b-v1.json`) est à consigner par la session qui orchestre avec l'écart déjà déclaré. Les quatorze lignes de la table d'en-tête qui ne sont plus recalculées gardent l'empreinte héritée, non vérifiée. Je ne les ai pas vérifiées non plus.

## 5. Les points que signale le rédacteur

- **Ligne A17 appliquée « à la lettre », livraison refusée ajoutée à sa liste** : oui, **une ligne d'une table de verdict est changée sans le mot de Lazar**. Son champ est étendu. Par 7.5, l'effet atteint le désappariement, ce que le texte ne dit pas. C'est B-1.
- **Assouplissement neuf à la dose ¼** (une grandeur `null` n'y arrête plus rien) : **acceptable**.
  - Aucun état n'est dit à cette dose, et sa valeur n'entre pas dans la famille.
  - La grandeur est rapportée « non rendue », avec le motif : ce n'est pas un repli silencieux.
  - Le cas sain est écrit en 8.4 (lignes 933 et 934).
  - Les écarts de structure restent un arrêt, à toute dose. Il est donc vrai qu'une faute de structure à la dose ¼ peut bloquer la course entière (B-1).
- **Contre-lecture 11 inscrite par le rédacteur** : les empreintes sont justes et le texte est exact. Elle n'empêche pas le validateur, qui rend toujours les deux problèmes attendus. Reste à confirmer par la session qui orchestre (M-3).
- **Phrases relues de plus** (6.10, 6.12 point 5, 7.2, 8.2, 8.3, 8.5, 8.6) : les précisions portées sont justes, et 8.3, 8.5 et 8.6 n'appelaient pas de changement. **7.5, qui n'est pas dans cette liste, est le passage qui manque** (B-1).

## 6. Fiches pour Lazar

| fiche | format | loyale | autonome | remarque |
|---|---|---|---|---|
| 9, seuil de 1 % | oui | presque | oui | L'option (b) « arrête la lecture de toute l'étape de discrétion » : la conséquence réelle, sous A17, est plus large (B-1). Le défaut est gardé (M-2). |
| 10, intervalle impossible | oui ; trois options | **non**, pour l'option (c) | oui | « le résultat principal, déjà scellé, reste » est faux sous la lettre actuelle (B-1). **Retrait du défaut justifié** : c'est l'issue d'un cas, comme le schéma de permutation, et le scellement attend déjà le mot de Lazar ; la phrase le dit. La confiance de 0,6 et la condition sur l'option (c) sont honnêtes. |
| 11, moniteur non ajustable | oui ; conditionnelle (« si, et seulement si ») | **non**, pour l'option (b) | oui | Même phrase fausse (B-1). Sinon, elle est claire : elle tombe si le développeur habilité répond non, et l'option (c), corriger le module, est bien présentée comme dépendant de lui. |
| Rappel sur le schéma de permutation | oui | oui | oui | Le défaut de C-7 est corrigé. Son envoi revient à la session qui tient la question. |

- **Contrôle par programme** : les puces des fiches 9 (6), 10 (7) et 11 (7) sont des sous-chaînes exactes de la section 12. La section 12 porte les points 1 à 20, dans l'ordre.
- **Fiche manquante** : celle de B-1.

## 7. Intégrité (vérifiée par programme)

| contrôle | résultat |
|---|---|
| brouillons 20 et 21 intacts | `b076e3f9…` et `8d834631…` recalculés ; compagnons vérifiés |
| brouillon 22, note et fiches | `ade786eb…`, `8f5480f4…`, `80581f3c…` ; compagnons vérifiés |
| citations à la lettre du brouillon 20 | les 935 passages sont tous retrouvés ; les quinze lignes d'origine du point 17 sont intactes |
| citations du brouillon 21 | 1 021 passages ; un seul manque, « forme d'une livraison », nom d'une garde récrit sans guillemets et non une citation transmise : c'est conforme à ce que déclare la note |
| titres | 53 ; seul le titre de niveau 1 change |
| consignes figées (3.2 et 3.3) | sections égales octet pour octet à celles du brouillon 20 ; empreintes du contenu des blocs `98a9bd34d280…` et `ecf590eae0c0…` |
| validateur `problemes()` | deux problèmes, les attendus : marque restante ; contre-lecture 10 sans ses empreintes |
| marque des cases | huit lignes (1220, 1221, 1223, 1224, 1226, 1231, 1232, 1233), toutes en 13.1 |
| table d'en-tête, quatre lignes neuves | `8d834631…`, `49cc89b0…`, `534abe1e…`, `6b155c84…` : égales. **Aucune empreinte de fichier cloisonné prise.** |

## 8. Ce que je n'ai pas regardé

- Le texte en entier : seulement les blocs touchés et leur contexte, avec 7.2, 7.5 et 6.12 point 2.
- Les quatorze lignes de la table d'en-tête qui renvoient à des dossiers cloisonnés.
- Le code de la version 5 et ses notes : ils sont confiés à un autre contre-lecteur.
- Le module habilité, et tout interne de moniteur.

## 9. Fichiers ouverts

- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon22.md` (par différence avec le brouillon 21, plus les lignes 3, 155, 693 à 713, 717, 760 à 770, 796 à 815, 849 à 856, 882 à 888, 932 à 936, et la section 12).
- Les brouillons 20 et 21, par programme.
- `docs/notes/relance-organismes-discrets-v1/preenregistrement-v2-brouillon22-note-v1.md`.
- `docs/notes/relance-organismes-discrets-v1/decisions-bras-a-brouillon22-v1.md`.
- `src/controle_ia/prereg.py` (appel de `problemes()`).
- Les pièces du premier mandat, déjà lues.
- **Rien d'autre.** Aucun fichier `*_v5.py`, ni `code-v5-bras-a-note-v1.md`, ni `defauts-du-texte-trouves-en-codant-v5.md`, ni le journal. Aucun interne de moniteur, aucune réponse de l'essai de mesure, aucune clé. Aucun appel de modèle ni aucun appel réseau. Aucun sous-agent. Un seul fichier écrit, celui-ci, scellé ; rien committé.
