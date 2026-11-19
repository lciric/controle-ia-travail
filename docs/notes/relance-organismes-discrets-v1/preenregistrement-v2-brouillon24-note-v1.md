# Note de changements — brouillon 24 du texte neuf du bras A des organismes discrets — v1

**Rédigé par Claude Fable 5.2 (`claude-fable-5-2`)**, le même agent que pour les brouillons 21 à 23. Je conçois ; la session qui m'orchestre consigne, scelle au registre et committe.

- **Brouillon** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon24.md`, `12609c048b7c1118845af38bd639988df9388728e2791fd88e7ac5fbbb4b9012` (1 985 lignes). Les brouillons 20 à 23 ne sont pas modifiés (`b076e3f9…`, `8d834631…`, `ade786eb…`, `ed7823af…`) : vérifiés avant la copie et après l'écriture.
- **Fiches pour Lazar : aucun fichier neuf.** Celles du brouillon 23 restent en vigueur, sans un mot changé : `docs/notes/relance-organismes-discrets-v1/decisions-bras-a-brouillon23-v1.md`, `f20abfed86f30883409b335844920c2b13595fd2060f6c3827ddc907b629783a`. Aucune correction de ce brouillon ne fait naître une question de règle de jugement.
- **Source** : la vérification des corrections du brouillon 23 par le même contre-lecteur, `docs/notes/relance-organismes-discrets-v1/verification-corrections-brouillon23-bras-a-v1.md`, `d6d53be4cfb1aef3bf87b4d551357caf6a28f268a4fcb2536e4dfcebd4a01b69`, lue en entier. Verdict : engageable après corrections, sans défaut bloquant ; deux défauts à corriger ; quatre mineurs.
- **Méthode** : copie du brouillon 23 par `cp`, puis 26 remplacements exacts, chacun vérifié unique par programme.
- **Rien n'est arrivé de Lazar ni de la session principale** : registre des accords relu sur la branche principale distante au commit `94485a11`, aucune ligne de plus.
- **Heures (UTC, `date -u`)** : début 16:05:31Z le 2026-11-19 ; brouillon scellé vers 16:10Z.
- **Interdits tenus** : aucune empreinte de fichier d'un dossier du côté habilité ; aucun interne de moniteur ; aucune fiche de l'organisme d'idéation ; aucune réponse de l'essai de mesure ; aucune clé ; aucun appel de modèle ; seul appel réseau, `git fetch` de la branche principale ; ni `registres/`, ni `.claude/`, ni le journal touchés ; rien committé ; aucun fichier existant écrasé ; suite d'essais non lancée ; aucun sous-agent ; aucun fichier du code de la version 5 ouvert.

## Contrôles par programme

| contrôle | résultat |
|---|---|
| titres de section (53) | les 52 titres de niveau 2 et 3 sont identiques à ceux du brouillon 23 |
| consignes figées (blocs de 3.2 et 3.3) | égales octet pour octet à celles du brouillon 20 ; `98a9bd34d280fc7d9db07a733bc78557ff350538a3ace7a2926999ecf14c9248` et `ecf590eae0c06d413d173f7f03c5575e52d6034613e0a1a30d681149435a1816`, recalculées |
| citations à la lettre du brouillon 20 | les 935 passages sont tous retrouvés ; la fiche du point 17 et l'avis d'origine sont intacts |
| citations du brouillon 23 | les 1 110 passages sont tous retrouvés |
| **points 17 à 21 de la section 12** | **identiques, caractère pour caractère, à ceux du brouillon 23** ; les fiches 9 à 12 du fichier du brouillon 23 restent donc mot pour mot celles du texte |
| table d'en-tête, sans les fichiers cloisonnés | 133 lignes à empreinte : 119 recalculées et égales, 0 différente, 14 sautées et non ouvertes (les mêmes), qui gardent l'empreinte héritée, non vérifiée |
| marque des cases non remplies | huit lignes, toutes en 13.1 |
| validateur (`problemes()`) | deux problèmes, les mêmes, attendus : marque restante hors des sections exigées ; contre-lecture 10 sans ses deux empreintes |
| différence avec le brouillon 23 | 22 lignes de plus ; 19 lignes changées |

## 1. La vérification, défaut par défaut

| défaut | traitement | ce que j'ai écrit |
|---|---|---|
| C-1 ce que rend le programme qui refuse, dit de quatre façons | **corrigé** | une définition unique en 6.9 ; la ligne de garde de 8.4 et la ligne du cas E, rédaction (c), y renvoient ; son artefact en 8.4 est précisé ; la fiche du point 21 garde sa forme abrégée, et le texte dit que la définition vaut |
| C-2 8.5 et la section 10 | **corrigé** | 6.9 dit ce qui s'applique de 8.5 sous chaque rédaction ; 8.5 porte une phrase ; la section 10 porte une ligne de repli à trois rédactions, dont une seule restera |
| M-1 avantage de l'option (a) de la fiche 12 | **non porté, à dessein** | la fiche est partie ; la retouche est écrite en partie 3 ci-dessous |
| M-2 frontière entre les étapes (m) et (n) | **corrigé** | toutes les gardes sur la sortie de la lecture commune jouent à l'étape (m), les vingt lectures ensemble ; seules celles du fichier des scores par unité jouent à l'étape (n) ; artefact en 8.4 |
| M-3 renvois au point 21 | **corrigé** | un renvoi « nœud ouvert » en 7.5 et à la ligne A17, qui n'ajoute aucun événement ; la case « nœuds » de 13.1 dit où le mot de Lazar se reporte |
| M-4 ordre des fiches dans leur fichier | **laissé tel quel** | le fichier est parti ; il conseille en tête de lire la fiche 12 d'abord |

## 2. La définition unique (C-1)

**Ce que rend le programme qui refuse, et rien d'autre** :
- le nom de la garde de 8.4 qui refuse, ou, pour un cas tenu pour une anomalie, le nom de la règle d'arrêt (« intervalle impossible » ; « moniteur appris non ajustable ») ;
- le nom du champ en défaut : le nom d'une clé des listes fermées, jamais ce qu'elle porte ;
- la lettre du cas de la table des formes, ou « aucun cas » ;
- l'étape, (m) ou (n) ;
- le moniteur et la dose, quand le défaut tient à une lecture.

**Ce qu'il ne rend jamais** : un nombre de la livraison (aire, aire d'un pli, valeur p, compte, borne, quantile, effectif, rang) ; la valeur des champs `motif` et `calculable`.

Deux choix que j'ai faits, pour que le vérificateur les voie :
- **Le moniteur et la dose sortent.** Ce sont des identifiants, non des mesures, et le développeur habilité en a besoin pour corriger. La lettre du cas, avec eux, dit par exemple qu'un intervalle a dégénéré pour tel moniteur à telle dose : c'est une information sur la forme, sans nombre.
- **La valeur de `motif` ne sort pas**, mais le nom de la règle d'arrêt dit la cause pour les deux anomalies. C'est inévitable : l'anomalie est l'événement. Le texte le dit en clair.

## 3. Retouche à porter à la fiche 12 après la réponse de Lazar (M-1 et C-1)

La fiche 12 (point 21 de la section 12) est partie telle qu'elle est au brouillon 23. Deux phrases sont à reprendre, au texte et dans la fiche, mot pour mot, quand Lazar aura répondu et que les rédactions écartées seront retirées :

1. **Option (a), avantage.** Aujourd'hui : « une seule règle pour tout arrêt ; aucune lecture reprise après que des nombres ont été rendus ». À écrire : « une seule règle pour tout arrêt ; aucune reprise sans un mot de Lazar, et rien n'est prononcé d'ici là ». La phrase actuelle prête à l'option (a) un avantage qu'elle n'a pas seule : la reprise sur un mot de Lazar existe dans les trois options. Elle favorisait l'option que je ne recommande pas.
2. **Enjeu, dernière phrase.** Aujourd'hui : « le programme qui refuse ne rend que le nom de la garde et de la clé en défaut, jamais une valeur ». À écrire : « le programme qui refuse ne rend que ce qui nomme le défaut — la garde, le champ, le cas, l'étape, le moniteur et la dose —, jamais un nombre ni un motif ».

Aucune des deux ne change ce que Lazar choisit. Si Lazar retient l'option (a), la première retouche devient sans objet avec le retrait des autres rédactions.

## 4. Ce qui change, section par section

| section | changement |
|---|---|
| titre ; statut ; auteur ; date ; commit lu ; note du rédacteur | brouillon 24 |
| table d'en-tête | quatre lignes : le brouillon 23, sa note, ses fiches (en vigueur), la vérification |
| conventions | « Numérotation stable » |
| 6.9, table des formes | « Quand jouent les gardes » ; « Ce que rend le programme qui refuse — définition unique » ; « Ce qui s'applique de 8.5 » ; rédaction (c) précisée sur l'étape (n) ; ligne du cas E, rédaction (c) |
| 7.2, ligne A17 | un renvoi « nœud ouvert, point 21 » ; aucun événement ajouté |
| 7.5, discrétion | un renvoi « nœud ouvert, point 21 » ; aucune cause ajoutée |
| 8.4 | ligne « issue d'un arrêt de la lecture de la discrétion » : cas sain et artefacts accordés à la définition et à l'étape (m) |
| 8.5 | une phrase sur l'arrêt de la lecture de la discrétion |
| 10 | une ligne de repli, à trois rédactions |
| 12 | **rien** |
| 13.1 | case « nœuds » : où se reportent les mots de Lazar |
| 14.36 | neuve |
| « Contre-lecture » | entrée 11 : vérification des corrections du brouillon 23, avec son empreinte |

## 5. Ce qui se reporte au scellement, quand Lazar aura répondu

Pour que rien ne soit oublié, la liste des endroits où une rédaction écartée se retire :

| point | endroits |
|---|---|
| 17, schéma de permutation | 6.9 (deux rédactions) ; 8.4 (deux lignes) ; case de 13.1 |
| 18, seuil de 1 % | 6.9 (la phrase de l'option écartée, trois endroits : règle de l'intervalle dégénéré, seuil, tête de la table des formes) |
| 19, intervalle impossible | 6.9 (phrase de la règle ; « Valeur p absente » ; table des formes, trois lignes E) ; 8.4 (ligne « intervalle dégénéré seul ») |
| 20, moniteur non ajustable | 6.9 (« Valeur p absente » ; table des formes, cas B) ; 8.4 (sa ligne) |
| 21, issue d'un arrêt | 6.9 (trois rédactions ; « Ce qui s'applique de 8.5 ») ; 7.2, ligne A17, ou 7.5 (le renvoi devient l'événement, ou tombe) ; 8.4 (sa ligne) ; 8.5 ; section 10 ; et la retouche de la fiche, partie 3 ci-dessus |

## 6. Ce que le code de la version 5 doit porter

Les parties 6 des notes des brouillons 22 et 23 tiennent. **Trois points changent ou s'ajoutent.**

3. **L'événement « arrêt de la lecture de la discrétion » — changé.** Il porte exactement : le nom de la garde ou de la règle d'arrêt ; le nom du champ en défaut ; la lettre du cas, ou « aucun cas » ; l'étape ; le moniteur et la dose quand le défaut tient à une lecture. Il ne porte **aucun nombre** de la livraison et **aucune valeur de `motif` ni de `calculable`**. La note du brouillon 23 disait « la garde, la clé, le cas et l'étape » : « clé » veut dire le nom du champ, et le moniteur et la dose s'ajoutent.
15. **Essai de la sortie du programme qui refuse — changé.** Il vérifie qu'aucun nombre de la livraison refusée, ni la chaîne de son champ `motif`, ni la valeur de `calculable` ne paraît dans la sortie ; et que les cinq éléments permis y sont. Pour l'anomalie « intervalle impossible », la sortie nomme la règle d'arrêt et le cas E, sans recopier le `motif`.
16. **Étape de l'événement — neuf.** L'étape se déduit de la pièce contrôlée, jamais de la dose : toute garde sur la sortie de la lecture commune donne l'étape (m), même pour une lecture à la dose ¼ ; seules les gardes du fichier des scores par unité donnent l'étape (n). Les gardes de la sortie de la lecture commune jouent toutes à sa réception, sur les vingt lectures, avant tout état et avant l'écriture du fichier de l'étape (m). Un essai : un écart de structure à la dose ¼ est rangé à l'étape (m).

Rien d'autre ne change pour le code. Il porte toujours quatre choix nommés sans valeur par défaut (schéma de permutation ; cas E ; motif « non ajustable » ; issue d'un arrêt) et un choix à défaut écrit (seuil de 1 %, option (a)).

## 7. Réserves

1. **Le texte et la fiche 12 ne disent pas la garde du programme avec les mêmes mots** : la fiche est partie avec sa forme abrégée, et le texte dit que la définition de 6.9 vaut. C'est voulu ; la retouche est écrite en partie 3.
2. **7.5 et la ligne A17 portent maintenant un renvoi.** C'est une phrase entre parenthèses, marquée « nœud ouvert », qui dit expressément que rien n'est ajouté. Ce sont deux passages de critères de lecture gelés : je n'y ai mis aucune règle. Elle devra être remplacée ou retirée au scellement.
3. **La section 10 et 8.5 portent une rédaction par option** : trois endroits de plus à nettoyer au scellement. La partie 5 en tient la liste.
4. **Le moniteur et la dose dans la sortie du programme qui refuse** sont un choix de ma part (partie 2). Le vérificateur le proposait « si on le veut ».
5. **Je n'ai toujours pas relu le texte en entier.** De plus qu'au brouillon 23 : la section 10. Le vérificateur a lu tout ce qui dépend d'un arrêt ou d'une issue non prononcée et n'y trouve pas d'autre conséquence cachée.
6. **Quatorze lignes de la table d'en-tête** gardent une empreinte héritée, non vérifiée.
7. **« Confirmée par la session qui orchestre »**, à l'entrée « Contre-lecture 11 », est écrit sur ta parole ; à toi de t'assurer que c'est consigné.

## 8. Fichiers ouverts pour ce brouillon

- `docs/notes/relance-organismes-discrets-v1/verification-corrections-brouillon23-bras-a-v1.md`, en entier.
- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon23.md` : la section 10 ; mes passages de 6.9 et de 8.4 ; et, par programme, le fichier entier pour les contrôles.
- `registres/go.md` de la branche principale distante, par `git show`, après la ligne 509.
- Par programme, pour leur seule empreinte : les 119 fichiers de la table d'en-tête hors des dossiers cloisonnés.
- Mes propres pièces des brouillons 21 à 23 et mes programmes de construction.
- Rien d'autre.
