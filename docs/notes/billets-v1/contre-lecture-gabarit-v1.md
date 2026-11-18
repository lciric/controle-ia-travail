# Contre-lecture du gabarit de rédaction des billets et de son application pas à pas — v1

Écrite par un contre-lecteur neuf (agent Opus 5.5 lancé par la session mère `session_013QMayjsoZJFBUCqcnvD5h1`), le 2026-11-18T22:38:28Z (heure relevée par `date -u`). Le contre-lecteur n'a écrit aucune pièce de l'étude des billets (ni grille, ni tri, ni codage, ni arbitrage, ni analyse, ni gabarit). Le rédacteur du gabarit était un agent Fable 5.2. Je n'ai ouvert aucune copie de billet, aucun commentaire, aucune table de correspondance, aucun dépôt de codeur, aucun fichier d'arbitrage, ni le programme du rédacteur, ni le script d'analyse.

## Verdict

**Après ces couples exacts.** La règle écrite d'avance (grille gelée, section 8) est appliquée juste : mon rejeu, écrit sans voir le programme du rédacteur, donne pour les 25 gestes le même statut de fiabilité et le même qualificatif que l'analyse scellée et que les deux pièces du rédacteur, le même nombre de comparaisons pour la correction de Holm (17), les mêmes valeurs corrigées, et les deux mêmes objections à prévenir (explication concurrente du résultat, antériorité). Les 1 435 contrôles que j'ai faits par programme (valeurs, clés absentes, champs recopiés), et une centaine à la main, concordent avec l'analyse sous la clé citée : **aucun écart de chiffre, aucun écart de statut, aucun écart de consigne.**

Les couples ne changent aucun statut, aucun qualificatif, aucun chiffre. Ils corrigent trois défauts majeurs et six mineurs :
- **majeur 1** — un écart non déclaré : les douze billets recodés du lot 2 du second codeur l'ont été par Opus 5.5, **le modèle du réviseur qui a écrit la grille**, que la mère avait écarté des codeurs ; le gabarit déclare l'écart « un codeur = un modèle » mais pas celui-là (couple G-11 ; liés : G-7, G-12) ;
- **majeur 2** — une ambiguïté déclarée non tranchée l'est de fait dans le texte des trois consignes « sous réserve » (« tient sur les 23 paires seulement », faux dans l'autre lecture) (couples G-2 à G-4) ;
- **majeur 3** — des lignes aussi près d'une frontière que les impasses rapportées ne sont pas dites : les non-revendications (18 bien notés sur 39, à deux billets d'une consigne), le résumé dans les 250 premiers mots (`d` exactement 0 sur les deux ensembles lus), la place de la thèse (`d` exactement 0 sur les 11 paires), l'explication concurrente du résultat (intervalle de sa part sous le seuil de 0,10) (couples G-6, G-8, A-3, A-4) ;
- mineurs : la puissance écrite d'avance n'est donnée qu'en écart observé et attribuée à la grille au-delà de ce qu'elle dit (G-1) ; un titre dit « les plus fréquentes » pour des classes qui ne le sont pas (G-5) ; une lecture prête à la politique du site un contenu que personne n'a lu (G-9, A-1) ; une huitième ambiguïté non relevée (G-10, A-2) ; le second codeur mêlé de deux modèles n'est pas rappelé là où on lit ses chiffres (G-7, G-12) ; l'analyse ne nomme pas les fichiers de codage qu'elle a lus (G-13).

Les deux pièces sont scellées : les couples s'appliquent à des versions neuves, sous des noms neufs, les versions 1 restant archivées (règle R12).

## 0. Pièces lues et empreintes

Empreintes recalculées par `sha256sum`, égales aux compagnons `.sha256` :

| Pièce | Empreinte |
|---|---|
| `docs/notes/billets-v1/gabarit-billets-v1.md` | `97185452dec7ea4f4f1a024b8dbb52f59f836ff09656bd23cd8d6735d9f91313` |
| `docs/notes/billets-v1/application-regle-gabarit-v1.md` | `573c156411eaabbfbaeb231552193470ead17b4e829d035fe3d4aa3bc4340cc9` |
| `docs/notes/billets-v1/analyse-tenue-v1/analyse-tenue-v1.json` | `e29c0613127feee9e26d72d664d9d21b76c9602a0bd44619eeef944d0f1c2a5e` |
| `docs/notes/billets-v1/grille-gestes-v1.md` | `14cf4de9429bcc08dbe88a4f76f61badbadc1b3ff234163d21f5f573f6dbf6f0` |
| `docs/notes/billets-v1/gel-grille-v1.md` | `6148b1297dfe7372430dcb5f046b4572ba3d2cdeda447b9b649b520e7f4915d5` |
| `docs/notes/billets-v1/procedure-codage-par-lots-v1.md` (lecture hors des pièces nommées, section 9) | `62c25abc805754d0bf1e08c40bf41273a7c664540c36d14c25914d33475af605` |

L'analyse nomme elle-même la grille par la même empreinte (`entrees.grille.sha256`) ; `synthetique` = false.

## 1. Rejeu de la règle par un programme du contre-lecteur (point 1 du mandat)

**Méthode.** Programme écrit à partir du seul texte des sections 5.2, 5.3 et 8 de la grille gelée, avant de lire les deux pièces du rédacteur et avant d'ouvrir le champ `consignes` de l'analyse (texte intégral en annexe A). Précision : en explorant la structure de l'analyse avant de l'écrire, j'avais vu la valeur de `m_comparaisons` (17) et le champ `fiabilite` de deux gestes (G01 : « fiable » ; G17 : « non-evaluable-haute »), et que `p_holm` manque pour les gestes non comparés ou non évaluables ; le programme ne lit aucun de ces champs, il les recalcule. Il lit le statut « comparée » ou « descriptive » de chaque geste dans la grille, puis, dans l'analyse, la prévalence et le kappa de l'indicateur sur les 62 billets et sur les 44 hors marquage 1, la fréquence chez les bien notés, `d` sur les 23 paires (`tous`) et sur les 11 (`sans_reunion`), la borne basse de `ic95_d` et `p_signe_exact`. Il **recalcule** la correction de Holm (étagée, plafonnée à 1) sur les gestes fiables et comparés, au lieu de lire `p_holm`. Lectures retenues : prévalence extrême au sens strict (au-dessus de 0,90, sous 0,10) sur l'un des deux ensembles, avant le kappa ; « fiable » = kappa au moins 0,60 sur les deux ensembles ; « après correction de Holm » = valeur corrigée sous 0,05 ; « au moins la moitié des 39 bien notés » = `freq_bien_notes` (tous) au moins 0,5. Les lectures concurrentes (au plus 0,05 ; au moins 0,90 ; « la moitié » sur un autre ensemble) ne changent rien ici (section 3).

**Résultat.** Nombre de gestes fiables et comparés : **17**, égal à `m_comparaisons` = 17 (G01, G02, G04, G05, G07, G10, G11, G12, G13, G14, G15, G16, G18, G19, G20, G21, G23). Valeurs de Holm recalculées : 1,0 pour les 17, égales à `p_holm` (la plus petite valeur brute, 0,125, fois 17, dépasse 1). Statuts et qualificatifs, geste par geste (chiffres arrondis ici ; valeurs exactes dans l'analyse, mêmes clés) :

| Geste | Analyse | Fiabilité : rejeu / analyse | Prévalence tous ; sans marquage 1 | Kappa tous ; sans marquage 1 | Bien notés présents (sur 39) | `d` 23 paires ; 11 paires | Borne basse `ic95_d` | `p_holm` rejeu / analyse | Point de la section 8 (rejeu) | `consignes` de l'analyse | Identique |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Forme du titre (G01) | comparée | fiable / fiable | 0,323 ; 0,295 | 0,926 ; 0,891 | 15 | 0,261 ; 0,364 | -0,0011 | 1,000 / 1,000 | 9 aucune consigne | aucune consigne | oui |
| Place de la thèse (G02) | comparée | fiable / fiable | 0,855 ; 0,818 | 0,870 ; 0,847 | 34 | 0,043 ; 0,000 | -0,1304 | 1,000 / 1,000 | 6 pratique majoritaire, non contredite | consigne — pratique majoritaire, non contredite | oui |
| Polarité du résultat principal (G03) | descriptive | fiable / fiable | 0,202 ; 0,227 | 0,950 ; 1,000 | 6 | -0,130 ; -0,182 | -0,3913 | — / — | 3 descriptif | descriptif : jamais consigne | oui |
| Résumé dans les 250 premiers mots (G04) | comparée | fiable / fiable | 0,694 ; 0,682 | 1,000 ; 1,000 | 26 | 0,000 ; 0,000 | -0,2174 | 1,000 / 1,000 | 6 pratique majoritaire, non contredite | consigne — pratique majoritaire, non contredite | oui |
| Chiffre de résultat en tête (G05) | comparée | fiable / fiable | 0,323 ; 0,295 | 0,926 ; 0,891 | 11 | -0,043 ; -0,091 | -0,3043 | 1,000 / 1,000 | 9 aucune consigne | aucune consigne | oui |
| Statut épistémique déclaré (G06) | comparée | non-evaluable-basse / non-evaluable-basse | 0,065 ; 0,068 | 1,000 ; 1,000 | 4 | 0,087 ; 0,091 | 0,0000 | — / — | 2 exclu | exclu (rare, non évaluable) | oui |
| Caractère préliminaire annoncé (G07) | comparée | fiable / fiable | 0,266 ; 0,239 | 0,716 ; 0,693 | 11 | -0,043 ; -0,091 | -0,2609 | 1,000 / 1,000 | 9 aucune consigne | aucune consigne | oui |
| Rapport à un article des auteurs (G08) | descriptive | fiable / fiable | 0,306 ; 0,295 | 1,000 ; 1,000 | 13 | 0,130 ; 0,182 | -0,1304 | — / — | 3 descriptif | descriptif : jamais consigne | oui |
| Contexte de production nommé (G09) | descriptive | fiable / fiable | 0,565 ; 0,500 | 1,000 ; 1,000 | 26 | 0,261 ; 0,273 | -0,0435 | — / — | 3 descriptif | descriptif : jamais consigne | oui |
| Enjeu de sûreté explicite (G10) | comparée | fiable / fiable | 0,387 ; 0,432 | 1,000 ; 1,000 | 14 | 0,000 ; 0,182 | -0,3043 | 1,000 / 1,000 | 9 aucune consigne | aucune consigne | oui |
| Figure légendée de résultat en tête (G11) | comparée | fiable / fiable | 0,153 ; 0,125 | 0,938 ; 0,896 | 7 | 0,174 ; 0,091 | -0,0435 | 1,000 / 1,000 | 9 aucune consigne | aucune consigne | oui |
| Base externe de comparaison du résultat principal (G12) | comparée | fiable / fiable | 0,177 ; 0,182 | 0,779 ; 0,847 | 8 | 0,087 ; 0,273 | -0,1304 | 1,000 / 1,000 | 9 aucune consigne | aucune consigne | oui |
| Choix justifié contre une option écartée (G13) | comparée | fiable / fiable | 0,702 ; 0,682 | 0,808 ; 0,792 | 30 | 0,087 ; 0,182 | -0,1739 | 1,000 / 1,000 | 6 pratique majoritaire, non contredite | consigne — pratique majoritaire, non contredite | oui |
| Dispositif nommé (G14) | comparée | fiable / fiable | 0,661 ; 0,636 | 0,784 ; 0,804 | 26 | 0,087 ; 0,091 | -0,1304 | 1,000 / 1,000 | 6 pratique majoritaire, non contredite | consigne — pratique majoritaire, non contredite | oui |
| Incertitude statistique (G15) | comparée | fiable / fiable | 0,185 ; 0,193 | 0,947 ; 0,927 | 4 | -0,217 ; -0,091 | -0,4348 | 1,000 / 1,000 | 9 aucune consigne | aucune consigne | oui |
| Non-revendications (G16) | comparée | fiable / fiable | 0,435 ; 0,420 | 0,673 ; 0,674 | 18 | 0,087 ; 0,182 | -0,2174 | 1,000 / 1,000 | 9 aucune consigne | aucune consigne | oui |
| Limites (G17) | comparée | non-evaluable-haute / non-evaluable-haute | 0,935 ; 0,966 | 0,734 ; 0,656 | 36 | -0,043 ; -0,091 | -0,2174 | — / — | 1 convention du genre | convention du genre (fiabilité non mesurée) | oui |
| Impasses rapportées (G18) | comparée | fiable / fiable | 0,573 ; 0,602 | 0,769 ; 0,763 | 20 | -0,130 ; -0,364 | -0,4348 | 1,000 / 1,000 | 9 aucune consigne | aucune consigne | oui |
| Explication concurrente anticipée (G19) | comparée | fiable / fiable | 0,540 ; 0,489 | 0,710 ; 0,683 | 23 | 0,000 ; -0,091 | -0,2609 | 1,000 / 1,000 | 7 sous réserve | consigne sous réserve | oui |
| Appel à poursuivre (G20) | comparée | fiable / fiable | 0,677 ; 0,682 | 0,853 ; 0,792 | 28 | 0,000 ; -0,091 | -0,2174 | 1,000 / 1,000 | 7 sous réserve | consigne sous réserve | oui |
| Code, modèles et données des auteurs (G21) | comparée | fiable / fiable | 0,629 ; 0,614 | 1,000 ; 1,000 | 24 | 0,000 ; -0,091 | -0,3043 | 1,000 / 1,000 | 7 sous réserve | consigne sous réserve | oui |
| Note d'édition visible (G22) | descriptive | fiable / fiable | 0,226 ; 0,205 | 1,000 ; 1,000 | 12 | 0,217 ; 0,091 | 0,0000 | — / — | 3 descriptif | descriptif : jamais consigne | oui |
| Analogie pour le non-spécialiste (G23) | comparée | fiable / fiable | 0,323 ; 0,318 | 0,853 ; 0,895 | 13 | -0,043 ; -0,364 | -0,3478 | 1,000 / 1,000 | 9 aucune consigne | aucune consigne | oui |
| Déclaration d'usage d'une intelligence artificielle dans l'écriture (G24) | descriptive | non-evaluable-basse / non-evaluable-basse | 0,048 ; 0,045 | 1,000 ; 1,000 | 1 | -0,087 ; -0,091 | -0,2174 | — / — | 2 exclu | exclu (rare, non évaluable) | oui |
| Appel aux retours (G25) | comparée | non-evaluable-basse / non-evaluable-basse | 0,097 ; 0,136 | 1,000 ; 1,000 | 4 | 0,000 ; -0,091 | -0,1739 | — / — | 2 exclu | exclu (rare, non évaluable) | oui |

Mêmes qualificatifs dans le gabarit (sections 1 à 3) et dans l'application pas à pas (sections 2 à 4) : 4 consignes « pratique majoritaire, non contredite » (G02, G04, G13, G14), 3 « sous réserve » (G19, G20, G21), 1 convention du genre (G17), 3 exclus rares (G06, G24, G25), 4 descriptifs (G03, G08, G09, G22), 10 « aucune consigne » ; aucun « à éviter », aucune « consigne distinctive », aucune « piste », aucun non fiable. Seuls les libellés de mon programme diffèrent de ceux de l'analyse par la forme (« exclu » contre « exclu (rare, non évaluable) » ; « descriptif, rapporté, jamais consigne » contre « descriptif : jamais consigne ») : même point de la règle.

Objections à prévenir, ensemble « tous » (238 commentaires codables) :

| Classe | Kappa binaire | Prévalence | Part des commentaires codables | Bien notés touchés (sur 39) | À prévenir : rejeu / analyse |
|---|---|---|---|---|---|
| Hors typologie (O0) | 0,875 | 0,246 | 0,256 | 32 | non / non |
| Explication concurrente du résultat (O1) | 0,825 | 0,139 | 0,134 | 21 | oui / oui |
| La mesure ne mesure pas le concept revendiqué (O2) | 0,828 | 0,080 | 0,084 | 16 | non / non |
| Exactitude d'un chiffre, d'un calcul ou du code (O3) | 0,747 | 0,071 | 0,063 | 10 | non / non |
| Antériorité, travaux et techniques voisins (O4) | 0,922 | 0,202 | 0,197 | 22 | oui / oui |
| Cadrage surdimensionné ou mal hiérarchisé (O5) | 0,325 | 0,013 | 0,017 | 4 | non / non |
| Pertinence ou effet pour le risque (O6) | 0,591 | 0,021 | 0,017 | 3 | non / non |
| Généralisation hors du cadre étudié (O7) | 0,851 | 0,044 | 0,046 | 9 | non / non |
| Coût caché ou effet secondaire de la méthode (O8) | 0,746 | 0,017 | 0,021 | 3 | non / non |
| Expérience suivante proposée (O9) | 0,795 | 0,078 | 0,076 | 11 | non / non |
| Critique de la forme et de la présentation (O10) | 1,000 | 0,013 | 0,013 | 3 | non / non |
| Demande de précision ou de matériel (O11) | 0,656 | 0,032 | 0,029 | 7 | non / non |
| Réplication ou prolongement par le lecteur (O12) | 0,907 | 0,023 | 0,021 | 4 | non / non |
| Éloge argumenté (classe nouvelle au brouillon 3) (O13) | 0,721 | 0,023 | 0,025 | 6 | non / non |

**Écarts : aucun.** Textes de consigne : les sept lignes « Consigne si retenue » recopiées dans le gabarit, et celle des limites (G17), sont identiques mot pour mot à la grille ; les définitions des deux objections retenues aussi.

## 2. Chiffres recopiés : valeur et clé (point 2)

- **Application pas à pas** : 1 112 contrôles par programme, chacune contre la valeur de l'analyse sous la clé et l'ensemble que le texte nomme (tableau de fiabilité, pas des neuf points, « chiffres rapportés » des 25 gestes, champs `consignes` et `fiabilite` recopiés, tableau des objections) ; 58 de plus contrôlées une à une (remarques de la section 2, cas de la section 4, sections 5 à 7). **Aucun écart.** Les mentions « clé absente de l'analyse pour ce geste » (`p_holm`, `ic_bonferroni_d` pour les gestes descriptifs et non évaluables) sont justes.
- **Gabarit** : 323 contrôles de valeurs arrondies par programme (lignes des sept consignes : 70 ; tableau de rattachement : 144 ; sensibilités : 24 ; tableau des gestes sans consigne : 85), arrondi à trois décimales vérifié, quatre pour les bornes basses citées ainsi ; une soixantaine à la main (en-tête de l'aveugle, convention du genre, objections, paragraphe des objections non retenues, limites et écarts, chiffres du registre). **Aucun écart.**
- Chiffres du registre recopiés (92 désaccords de gestes sur 1 550, 35 d'objections sur 238, ligne R-3469 ; cinq arbitres, ligne R-3483) : conformes au registre.

## 3. Les ambiguïtés : posées des deux côtés, et ce que la grille impose (point 3)

| Ambiguïté relevée par le rédacteur | Posée des deux côtés ? | Ce que la grille impose |
|---|---|---|
| 1. Lecture liée à l'aveugle (« nettement », section 5.5) | Oui. | La grille impose deux choses, pas le reste : cette lecture « ne commande aucune décision » (section 5.5, dernier point), donc aucun qualificatif n'en dépend dans les deux lectures ; et, sans condition, « chaque différence se lit » avec la part de paris justes, la sensibilité sans billets reconnus et la description sans billets reconnus ni devinés (fait : en-tête, tableau des sensibilités, limite 8). Que la condition soit remplie ou non : **ouvert**, le seuil n'est pas chiffré. Précision sans couple : la lecture A compare les paris justes à 39 et 23 sur 62, mais les paris comptent 41 et 57 billets (« ne sait pas » exclus) dont la composition n'est pas dans l'analyse ; l'écart (0,951 et 0,912 contre 0,629 au plus) reste grand quelle qu'elle soit. |
| 2. Déclaration d'usage d'une intelligence artificielle (G24) | Oui, mais la lecture B prête à la politique du site un contenu (« commande cette déclaration ») que ni la grille ni personne n'a lu (couples G-9, A-1). | L'étiquette est imposée : « le premier qui convient l'emporte », donc « exclu » (point 2) ; « exclu » du gabarit et « rapporté » dans l'étude ne s'opposent pas. Aucune consigne tirée de la mesure : imposé (les deux lectures s'accordent). Un rappel de la politique, hors mesure : **ouvert** ; son texte serait un choix neuf, à faire par la mère ou Lazar. |
| 3. Texte d'une objection à prévenir | Oui. | La grille interdit le lien entre geste et objection au gabarit (section 5.4 : « exploratoires, jamais au gabarit ») et n'écrit d'avance aucun texte de consigne pour les objections. La lecture A (la classe nommée par sa définition) est la seule qui ne demande aucun choix neuf ; la lecture B demande un texte neuf : décision de la mère ou de Lazar. **Ouvert pour B, A seule écrivable sans choix.** |
| 4. Fiabilité d'une classe d'objection sur un ou deux ensembles | Oui. | La section 8 donne sa propre définition entre parenthèses et la lit « sur l'ensemble « tous » » ; la section 5.2 dit « même seuil ; même règle de prévalence extrême ». La lettre de la section 8 penche pour A ; **ouvert**, sans effet vérifié : les deux classes retenues sont fiables aussi sur les 44 hors marquage 1 (kappa 0,818 et 0,919 ; prévalence 0,147 et 0,203), et la lecture B, plus stricte, ne peut ajouter aucune classe. |
| 5. « L'ensemble sur lequel elle tient » | Posée des deux côtés dans la liste, **mais tranchée de fait dans le texte** : les trois consignes « sous réserve » disent « tient sur les 23 paires seulement », ce qui est la lecture A ; dans la lecture B, elles tiennent aussi sur les 20 paires hors marquage 2 (`d` 0,050, 0,000 et 0,100), et « seulement » devient faux. | La grille ne fixe pas lequel des quatre ensembles rapportés « elle tient » désigne ; la structure des points 6 et 7 (définis sur les 23 et les 11) penche pour A. **Ouvert** ; couples G-2 à G-4 pour que le texte porte les deux lectures, comme la liste le dit. |
| 6. Renvoi aux « points 1 à 4 de la section 8 » (section 5.2) | Oui. | Le libellé est imposé de toute façon : point 1, « convention du genre (fiabilité non mesurée) », « jamais « distinctif » ni « à éviter » ». Le renvoi est une incohérence interne sans effet. |
| 7. « La moitié des bien notés » sans nombre aux points 7 et 8 | Oui. | Pour le point 8, la grille impose A : il ne lit que les 23 paires, dont l'ensemble est celui des 39 bien notés. Pour le point 7, **ouvert**, la structure parallèle au point 6 penchant pour A ; sans effet vérifié : G19, G20 et G21 dépassent 0,5 sur les quatre ensembles (0,590 ; 0,538 ; 0,622 ; 0,538 pour G19, au plus bas), et aucun autre geste fiable et comparé n'a `d` positive ou nulle sur les 23 paires et négative sur les 11. |

**Ambiguïté non relevée (couples G-10, A-2).** 8. Le texte sous lequel la convention du genre entre au gabarit : la section 5.2 la fait entrer « sous le libellé « convention du genre (fiabilité non mesurée) » » ; la section 8 réserve la ligne « Consigne si retenue » au « texte de chaque consigne », et la convention du genre n'est pas une consigne (point 1). Le gabarit l'écrit sous la ligne « Consigne si retenue » des limites ; l'application dit « comme la section 8 l'ordonne », ce que la section 8 ne dit pas pour ce cas. **Ouvert** ; la forme seule en dépend.

**Lectures concurrentes vérifiées sans effet (aucun couple).** « Après correction de Holm » lu « au plus 0,05 » plutôt que « sous 0,05 » : les 17 valeurs valent 1. Prévalence extrême lue « au moins 0,90 » ou « au plus 0,10 » : aucune prévalence n'est égale à un seuil (la plus proche, 0,097, est sous 0,10 dans les deux lectures). Méthode de calcul du percentile de `ic95_d` : sans effet sur la forme du titre (section 6).

## 4. Rien n'enjolive-t-il le résultat ? (point 4, règle de symétrie R4)

- **Résultat nul et puissance.** Le gabarit ne dit jamais « aucun geste ne distingue » sans la puissance : il dit « Aucun geste n'a passé le test » suivi, dans le même point, de « Un résultat nul était attendu et ne dit pas « pas d'effet » » et du seuil d'écart observé (0,43) ; la section 3 et la limite 3 disent qu'« un écart très grand » seul était visible. Deux défauts : (a) il attribue à la grille une phrase qu'elle ne dit pas (« avec moins de comparaisons la puissance est à peine plus haute » : la grille le dit pour m = 20 seulement ; j'ai vérifié que, pour m = 17, le plus petit écart observé qui passe reste 10 paires contre 0, soit 0,435, comme pour m = 20 et m = 23) ; (b) il ne donne pas la puissance écrite d'avance pour des écarts vrais (0,3 : 7 à 10 fois sur 100 ; 0,5 : 46 à 55 fois ; détectable seulement un geste présent chez quatre bien notés sur cinq et un apparié sur cinq). Couple G-1.
- **Hors du gabarit, pour la mère** : la ligne R-3487 du registre écrit « **Résultat principal : aucun geste ne distingue les billets bien notés de leurs appariés** » sans la puissance, ce que la grille interdit de lire comme « pas d'effet ». Je n'écris pas sous `registres/` : à redire dans une ligne neuve (section 8).
- **« Non contredite » quand les appariés font plus souvent le geste.** Pour trois consignes, la fréquence chez les appariés dépasse celle des bien notés : résumé dans les 250 premiers mots (0,739 contre 0,667), explication concurrente anticipée (0,609 contre 0,590), code, modèles et données (0,652 contre 0,615). La règle lit `d` par paires, nulle pour les trois, et les deux fréquences ne portent pas sur les mêmes billets (39 bien notés dont 16 sans apparié, 23 appariés) : le qualificatif est juste. Les chiffres sont donnés à côté de chaque consigne, mais rien ne le dit en clair. Couple G-8.
- **Objections.** Le titre « classes de commentaires les plus fréquentes sous les billets bien notés » est inexact : la classe hors typologie (0,256) est plus fréquente que les deux retenues (0,197 et 0,134) ; elles sont retenues par la règle, non par leur rang (couple G-5). L'explication concurrente du résultat est retenue sur une part de 0,134 dont l'intervalle descend à 0,092, sous le seuil, et elle est la première de l'ordre de priorité, ce qui peut gonfler sa part comme la grille dit que les classes basses sont sous-estimées (couple G-6). Le gabarit dit le cas symétrique (la mesure qui ne mesure pas le concept revendiqué, retenue sur deux ensembles, non sur « tous ») : il doit dire aussi celui-là.
- **Ce qui tient** : le libellé honnête est complet pour chaque consigne (texte gelé, qualificatif, fréquence chez les bien notés, `d` et son intervalle, intervalle du kappa, ensemble) ; la section 1.1 porte « elles ne disent pas que le geste distingue les bien notés » ; les cas défavorables sont dits comme les favorables (l'incertitude statistique, négative, dont l'intervalle non ajusté exclut zéro ; la forme du titre, positive, près de « piste » ; le contexte de production, descriptif, rapporté avec `d` 0,261) ; la mesure de l'aveugle est en tête, avec ses deux lectures ; la sensibilité sans billets reconnus (4 paires) est donnée, y compris quand elle est négative (−0,250 pour la place de la thèse, l'explication concurrente anticipée, l'appel à poursuivre, les limites).

## 5. Limites et écarts déclarés : tous présents ? (point 5)

**Écarts déclarés au registre (lignes R-3413 à R-3487 qui parlent des billets) : tous présents, aux bonnes lignes.**

| Écart ou limite au registre | Ligne(s) | Dans le gabarit |
|---|---|---|
| Lot 2 du second codeur arrêté par les garde-fous ; dépôt partiel mis de côté, non ouvert ; recodé par Opus 5.5 sur mot de Lazar | R-3422, R-3434, R-3441 | 5.2, point 1 |
| Arbitres : Opus 5.5 pour quatre lots, Haiku 5.5 pour les huit billets du lot 2 ; script d'arbitrage ajouté après le gel ; 92 et 35 désaccords | R-3441, R-3469, R-3483 | 5.2, point 2 |
| Agents de la seconde passe distincts de ceux de la première | R-3441 | 5.2, point 3 |
| Consignes de lancement non identiques (quatre précisions) ; refus de forme corrigés sans décision changée | R-3423, R-3425 | 5.2, point 4 |
| Dossier temporaire listé (deux fois, noms seulement) ; copie qui laisse en clair un coauteur et son affiliation | R-3423, R-3426, R-3430 | 5.2, point 5 (le compte des copies touchées, demandé en R-3430, manque : le gabarit le dit et ne peut pas le donner) |
| Aveugle faible dès le pilote | R-3413, R-3415 | 5.2, point 6 ; en-tête |
| Constance d'un modèle d'un lot à l'autre non mesurée | R-3415 ; procédure, point 5 | 5.1, point 13 |

**Limites de la grille gelée (sections 4.2, 5.2, 5.3, 5.5, B, 9, 12) et de la note de gel : toutes présentes** (score qui dépend de l'auteur et du reste ; deux populations ; puissance ; marquages ; un seul site, neuf étiquettes, 2022 ; tri imparfait ; images ; aveugle et ce qui ne se masque pas ; grille écrite sur le développement ; tirage sur le score ; une classe par commentaire ; coauteur absent ; hésitations du pilote non traitées ; formules du pilote ; proximité ajoutée à G19 ; numpy ; points laissés à la mère ; version 4 du script). Seul détail omis, sans portée : « 45 paires en tout ».

**Écart non déclaré, relevé par la contre-lecture (majeur 1).** Le réviseur qui a écrit la grille est un agent Opus 5.5 (brouillon 2, ligne R-3381 ; le même réviseur, « repris », a rendu le brouillon 3 et la version, lignes R-3394, R-3415, R-3419). La mère a choisi les codeurs « tous deux autres que le modèle du réviseur (Sonnet 5.5 et Fable 5.2) » (ligne R-3404), et la procédure scellée le redit (point 1). Le recodage du lot 2 du second codeur sur Opus 5.5 (lignes R-3434, R-3441) fait donc coder douze billets par le modèle de l'auteur de la grille ; ni le registre ni le gabarit ne le disent. L'arbitre de quatre lots, Opus 5.5, est aussi de ce modèle, mais la procédure le prévoyait (point 6) : c'est une limite, non un écart. Couple G-11.

**Autres manques (mineurs).** Le « seul second codeur » des sensibilités et la limite 13 (« accord entre deux modèles ») ne rappellent pas que ce codeur est Fable 5.2 pour cinquante billets et Opus 5.5 pour douze (couples G-7, G-12). L'analyse nomme dans `entrees` la grille, le manifeste et les deux fichiers de marquage, avec empreintes, mais ni les dépôts des codeurs ni les fichiers arbitrés : le lien entre l'analyse et le codage ne passe que par le registre (ligne R-3483) ; c'est une limite de traçabilité à écrire (couple G-13).

## 6. Cas près d'une frontière : dits sans changer la règle ? (point 6)

**Dits, sans changer la règle** : la forme du titre (borne basse −0,0011, pas « piste ») ; l'incertitude statistique (intervalle non ajusté tout négatif, pas « à éviter ») ; les impasses rapportées (20 bien notés sur 39, `d` négative) ; les trois « sous réserve » à `d` exactement 0 (application, section 4) ; l'appel aux retours, prévalence sous 0,10 de peu, et les bornes basses du kappa sous 0,60 (application, section 2). Le gabarit renvoie à l'application pour les trois premiers.

**Vérifié par la contre-lecture** : pour la forme du titre, les comptes déduits de `d` et de `p_signe_exact` sont 9 paires en faveur du bien noté, 3 contre, 11 sans écart ; la loi exacte du rééchantillonnage donne P(`d*` < 0) = 0,0235 et P(`d*` ≤ 0) = 0,0460 : la borne exacte est 0, qui n'est pas strictement positive. Le qualificatif ne dépend ni de la graine ni de la méthode du percentile ; la valeur −0,0011 tient au tirage. Pour l'incertitude statistique : 1 paire en faveur du bien noté, 6 contre (`p_signe_exact` 0,125).

**Non dits (majeur 3)** :
- **les non-revendications (G16)** : 18 bien notés sur 39 (0,462), à deux billets de la moitié, `d` positive sur les 23 paires (0,087) et sur les 11 (0,182) : à 20 sur 39, consigne simple. Plus près d'un changement de qualificatif que les impasses rapportées, qui sont dites ;
- **le résumé dans les 250 premiers mots (G04)** : `d` exactement 0 sur les 23 paires et sur les 11 ; une seule paire discordante de plus en faveur de l'apparié en ferait « aucune consigne » ; geste plus fréquent chez les appariés ;
- **la place de la thèse (G02)** : `d` exactement 0 sur les 11 ; une paire de plus en faveur de l'apparié parmi elles en ferait une consigne « sous réserve » ; avec le seul premier codeur, `d` est négative sur les 23 paires (−0,043) ;
- **l'explication concurrente du résultat (O1)** : part 0,134, intervalle [0,092 ; 0,181] sous le seuil de 0,10 à sa borne basse ;
- dans le gabarit lui-même (l'application le dit) : **l'appel aux retours (G25)**, 12 codages présents sur 124 (0,097) ; à 13 (0,105), il aurait été évaluable et « aucune consigne », jamais consigne.

Couples G-6, G-8 (gabarit), A-3, A-4 (application). Aucun ne change la règle ni un qualificatif.

## 7. Couples exacts

Chaque ancienne chaîne figure **une seule fois** dans la version 1 visée (vérifié par programme). Remplacement exact ; les deux versions 1 restent archivées sans modification.

### Gabarit (`gabarit-billets-v1.md` → version neuve)

**G-1** (mineur, puissance)
- Ancien : `et la grille dit qu'avec moins de comparaisons la puissance est à peine plus haute).`
- Nouveau : `et la grille dit seulement qu'avec m = 20 la puissance est à peine plus haute ; avec m = 17, le plus petit écart observé qui peut passer reste 10 paires contre 0, soit 0,435, vérifié par la contre-lecture). **Puissance écrite d'avance** (grille, section 5.3, calcul fait pour 23 paires et 23 comparaisons) : un écart vrai de 0,2 passe 2 fois sur 100 ; de 0,3, 7 à 10 fois ; de 0,4, 21 à 29 fois ; de 0,5, 46 à 55 fois ; de 0,6, 75 à 79 fois ; de 0,7, 94 fois. Seul était détectable un geste présent chez environ quatre bien notés sur cinq et un apparié sur cinq, ou plus tranché ; un écart de 0,3 ou moins, pourtant important pour un geste de rédaction, ne l'était pas. « Aucun geste n'a passé le test » veut donc dire : aucun écart de cette taille, et non « aucun écart ».`

**G-2** (majeur 2)
- Ancien : `tient sur les 23 paires seulement (explication concurrente anticipée, G19).`
- Nouveau : ``tient, des deux ensembles que lit la règle, sur les 23 paires seulement ; des quatre ensembles rapportés, `d` est positive ou nulle sur les 23 paires et sur les 20 hors marquage 2, négative sur les 13 hors marquage 1 et sur les 11 (explication concurrente anticipée, G19).``

**G-3** (majeur 2)
- Ancien : `tient sur les 23 paires seulement (appel à poursuivre, G20).`
- Nouveau : ``tient, des deux ensembles que lit la règle, sur les 23 paires seulement ; des quatre ensembles rapportés, `d` est positive ou nulle sur les 23 paires et sur les 20 hors marquage 2, négative sur les 13 hors marquage 1 et sur les 11 (appel à poursuivre, G20).``

**G-4** (majeur 2)
- Ancien : `tient sur les 23 paires seulement (code, modèles et données des auteurs, G21).`
- Nouveau : ``tient, des deux ensembles que lit la règle, sur les 23 paires seulement ; des quatre ensembles rapportés, `d` est positive ou nulle sur les 23 paires et sur les 20 hors marquage 2, négative sur les 13 hors marquage 1 et sur les 11 (code, modèles et données des auteurs, G21).``

**G-5** (mineur)
- Ancien : `### 1.4 Objections à prévenir (classes de commentaires les plus fréquentes sous les billets bien notés ; description, sans comparaison)`
- Nouveau : `### 1.4 Objections à prévenir (classes retenues par la règle de la section 8 : fiables, au moins 10 % des commentaires codables et au moins un quart des 39 bien notés touchés ; la classe hors typologie, plus fréquente, est exclue par la règle ; description, sans comparaison)`

**G-6** (majeur 3)
- Ancien : ``clés sous `objections.tous.classes.O1` ; 238 commentaires codables (`objections.tous.commentaires_codables`).``
- Nouveau : ``clés sous `objections.tous.classes.O1` ; 238 commentaires codables (`objections.tous.commentaires_codables`). Près de la frontière : la règle lit la part estimée, 0,134 ; son intervalle, [0,092 ; 0,181], passe sous le seuil de 0,10. Et cette classe est la première de l'ordre de priorité (grille, section B : « un long commentaire à plusieurs points tombe dans la première classe de l'ordre ») : sa part peut être surestimée, comme celles des classes basses de l'ordre sont sous-estimées.``

**G-7** (mineur)
- Ancien : `Sensibilités rapportées pour les sept consignes et la convention (aucune règle ne les lit) : différence avec le seul premier codeur, avec le seul second, et sans les billets reconnus par un codeur au moins (21 billets, 4 paires seulement).`
- Nouveau : `Sensibilités rapportées pour les sept consignes et la convention (aucune règle ne les lit) : différence avec le seul premier codeur (Sonnet 5.5), avec le seul second (Fable 5.2 pour cinquante billets, Opus 5.5 pour les douze du lot 2), et sans les billets reconnus par un codeur au moins (21 billets, 4 paires seulement).`

**G-8** (majeur 3 et symétrie)
- Ancien : `les impasses rapportées (G18).`
- Nouveau (la chaîne ancienne, puis la liste) :

```
les impasses rapportées (G18). D'autres lignes sont près d'une frontière, sans que la règle change :
- **les non-revendications (G16)** : présentes chez 18 des 39 bien notés (`freq_bien_notes` 0,462), à deux billets de la moitié, avec `d` positive sur les 23 paires (0,087) et sur les 11 (0,182) : à 20 billets sur 39, elles auraient reçu la consigne simple ;
- **le résumé dans les 250 premiers mots (G04)** : `d` vaut exactement 0 sur les 23 paires et sur les 11 ; une seule paire discordante de plus en faveur de l'apparié en ferait « aucune consigne » ; et le geste est plus fréquent chez les appariés (0,739) que chez les bien notés (0,667) ;
- **la place de la thèse (G02)** : `d` vaut exactement 0 sur les 11 ; une paire de plus en faveur de l'apparié parmi elles en ferait une consigne « sous réserve » ; avec le seul premier codeur, `d` est négative sur les 23 paires (`d_codeur_1` -0,043) ;
- **les trois consignes « sous réserve » (G19, G20, G21)** : `d` vaut exactement 0 sur les 23 paires et -0,091 sur les 11, soit une seule paire nette ; pour deux d'entre elles le geste est plus fréquent chez les appariés (G19 : 0,609 contre 0,590 ; G21 : 0,652 contre 0,615) ; les deux fréquences ne portent pas sur les mêmes billets (39 bien notés dont 16 sans apparié, 23 appariés) et la règle lit la différence par paires ;
- **l'appel aux retours (G25)** : prévalence 0,097 sur les 62 billets (12 codages présents sur 124), sous 0,10 de peu, et 0,136 sur les 44 hors marquage 1 ; évaluable, il aurait été « aucune consigne » (`freq_bien_notes` 0,103 ; borne basse de `ic95_d` -0,174), jamais consigne ;
- **la forme du titre (G01)**, précision : la borne -0,0011 tient au tirage des 10 000 rééchantillonnages ; la loi exacte (9 paires en faveur du bien noté, 3 contre, déduites de `d` et de `p_signe_exact`) place la borne à 0, qui n'est pas non plus strictement positive : le qualificatif ne dépend pas de la graine.
```

**G-9** (mineur)
- Ancien : `(B) le gabarit rappelle, hors mesure, que la politique du site commande cette déclaration.`
- Nouveau : `(B) le gabarit rappelle, hors mesure, que la grille renvoie pour ce geste à la politique du site (« la consigne vient de la politique du site, pas de la mesure ») ; ce que cette politique demande n'a été lu ni par le rédacteur ni par la contre-lecture.`

**G-10** (mineur, ambiguïté non relevée)
- Ancien : `7. « La moitié des bien notés » sans nombre aux points 7 et 8 : sans effet.`
- Nouveau (la chaîne ancienne, puis une ligne) :

```
7. « La moitié des bien notés » sans nombre aux points 7 et 8 : sans effet.
8. Texte sous lequel la convention du genre entre au gabarit (relevée par la contre-lecture) : la section 5.2 fait entrer le geste quasi universel « sous le libellé « convention du genre (fiabilité non mesurée) » » ; la section 8 réserve la ligne « Consigne si retenue » au « texte de chaque consigne », et la convention du genre n'est pas une consigne (point 1). (A) le geste entre sous sa ligne « Consigne si retenue », suivie du libellé (ce que fait la section 1.3) ; (B) il entre sous son seul nom (« Limites (G17) »), suivi du libellé. Non tranché ; l'écrit suit A, la forme seule en dépend.
```

**G-11** (majeur 1)
- Ancien : `Le « second codeur » est donc Fable 5.2 pour cinquante billets et Opus 5.5 pour douze : écart à la procédure scellée (un codeur = un modèle).`
- Nouveau : `Le « second codeur » est donc Fable 5.2 pour cinquante billets et Opus 5.5 pour douze : écart à la procédure scellée (un codeur = un modèle). Écart de plus, relevé par la contre-lecture et non déclaré au registre : Opus 5.5 est aussi le modèle du réviseur qui a écrit la grille (brouillon 2 rendu par un agent Opus 5.5, ligne R-3381 ; le même réviseur a rendu le brouillon 3 et la version, lignes R-3394, R-3415, R-3419), alors que la mère avait choisi deux codeurs « tous deux autres que le modèle du réviseur » (ligne R-3404 ; procédure de codage par lots, point 1). Pour ces douze billets, l'un des deux codeurs est donc du modèle de l'auteur de la grille. L'arbitre des quatre autres lots, Opus 5.5, est lui aussi de ce modèle : prévu d'avance par la procédure (point 6), c'est une limite, non un écart.`

**G-12** (mineur)
- Ancien : `l'accord entre codeurs mesure l'accord entre deux modèles appliquant la même grille, lot par lot (procédure de codage par lots, point 5).`
- Nouveau : `l'accord entre codeurs mesure l'accord entre deux modèles appliquant la même grille, lot par lot (procédure de codage par lots, point 5) ; pour les douze billets du lot 2 du second codeur, entre Sonnet 5.5 et Opus 5.5.`

**G-13** (mineur)
- Ancien : `- Le gabarit ne dit rien du contenu d'un billet, ni de ce qui fait un bon résultat.`
- Nouveau (la chaîne ancienne, puis une ligne) :

```
- Le gabarit ne dit rien du contenu d'un billet, ni de ce qui fait un bon résultat.
- L'analyse nomme dans `entrees` la grille, le manifeste du corpus et les deux fichiers de marquage, avec leurs empreintes, mais ni les dépôts des codeurs ni les fichiers arbitrés qu'elle a lus : le lien entre l'analyse et le codage passe par le registre (ligne R-3483) et les pièces scellées sous `docs/notes/billets-v1/tenue-v1/`, pas par l'analyse elle-même.
```

### Application pas à pas (`application-regle-gabarit-v1.md` → version neuve)

**A-1** (mineur)
- Ancien : `- Lecture B : le gabarit rappelle, hors mesure et sous ce libellé, que la politique du site commande cette déclaration ; ce rappel ne s'appuie sur aucun chiffre de l'étude.`
- Nouveau : `- Lecture B : le gabarit rappelle, hors mesure et sous ce libellé, que la grille renvoie pour ce geste à la politique du site (« la consigne vient de la politique du site, pas de la mesure ») ; ce rappel ne s'appuie sur aucun chiffre de l'étude, et ce que demande la politique n'a pas été lu.`

**A-2** (mineur)
- Ancien : `Le texte gelé est recopié tel quel, comme la section 8 l'ordonne, et la réserve est écrite à côté.`
- Nouveau : `Le texte gelé est recopié tel quel et la réserve est écrite à côté ; la section 8 ordonne ce texte pour « chaque consigne », et la convention du genre n'en est pas une (point 1) : le recopier pour elle est une lecture, écrite comme ambiguïté 8 dans le gabarit.`

**A-3** (majeur 3)
- Ancien : `Quatre cas à signaler parce qu'ils sont près d'une frontière`
- Nouveau : `Cas à signaler parce qu'ils sont près d'une frontière`

**A-4** (majeur 3)
- Ancien : ``Pour les deux premières, les deux codeurs pris seuls donnent une différence négative ou nulle (`d_codeur_1`, `d_codeur_2`, section 3).``
- Nouveau (la chaîne ancienne, puis une ligne) :

```
Pour les deux premières, les deux codeurs pris seuls donnent une différence négative ou nulle (`d_codeur_1`, `d_codeur_2`, section 3).
- **Autres lignes près d'une frontière, relevées par la contre-lecture** : les non-revendications (G16), `freq_bien_notes` (tous) = 0.46153846153846156, soit 18 sur 39, à deux billets de la moitié, avec `d` (tous) = 0.08695652173913043 et `d` (sans_reunion) = 0.18181818181818182 ; le résumé dans les 250 premiers mots (G04), `d` (tous) = 0.0 et `d` (sans_reunion) = 0.0 ; la place de la thèse (G02), `d` (sans_reunion) = 0.0 et `d_codeur_1` (tous) = -0.043478260869565216 ; l'explication concurrente du résultat (O1), `ic95_part` (tous) = [0.09163346613545817, 0.1810344827586207], dont la borne basse est sous 0,10.
```

## 8. Remarques sans couple, pour la session mère

1. **Registre, ligne R-3487** : « Résultat principal : aucun geste ne distingue les billets bien notés de leurs appariés » est écrit sans la puissance ; la grille dit « Un résultat nul est attendu et ne dit pas « pas d'effet » ». Proposition pour une ligne neuve (la ligne ancienne ne se réécrit pas) : « aucun geste n'a passé le test ; avec 23 paires, seul un écart très grand était détectable (un écart vrai de 0,3 passait 7 à 10 fois sur 100) ; ce résultat nul ne dit pas « pas d'effet » ». Même prudence pour le billet en blocs à venir.
2. **Application, point 4 de chaque geste** : la phrase « `d` (tous) = 0.2608… strictement négatif et `p_holm` (tous) = 1.0 sous 0,05 → **non** » se lit comme une affirmation ; les points 5 à 8 donnent « : oui » ou « : non » par condition. Forme seulement ; à aligner si une version neuve est faite.
3. **Version neuve des deux pièces** : la mention « Non contre-lu » de l'en-tête et de la section 5.3 du gabarit est à mettre à jour avec le chemin et l'empreinte du présent rapport.
4. **Dossier de brouillon partagé** : le dossier temporaire de la session contient des programmes d'autres agents (dont, peut-être, celui du rédacteur) ; je n'en ai ouvert aucun ; mes trois programmes y sont et sont recopiés en annexe parce que ce dossier peut être vidé.

## 9. Ce que le contre-lecteur a fait et n'a pas fait ; lectures hors mandat

- **Écrit** : ce seul fichier (et son compagnon d'empreinte), dans `docs/notes/billets-v1/`. Trois programmes et deux sorties dans le dossier de brouillon de la session (empreintes en annexe). Ni commit, ni poussée, rien sous `registres/`, `diag/`, `runs/`, `donnees/`, `docs/verdicts/`.
- **Pas ouvert** : copies de billets, commentaires, tables de correspondance, dossier `docs/notes/billets-v1/tenue-v1/`, dépôts, arbitrages, programme du rédacteur, script d'analyse, politique du site.
- **Lectures hors des pièces nommées** : la procédure de codage par lots (`procedure-codage-par-lots-v1.md`, entière ; citée par le gabarit, « point 5 », vérifié) ; dans le registre, des extraits des lignes R-3381, R-3394 et R-3404 (modèle du réviseur de la grille et choix des codeurs ; hors de l'intervalle R-3413 à R-3487), et les 140 premiers caractères de toutes les lignes de cet intervalle, billets ou non ; dans la grille, hors des sections 4 à 9 et 12 : sections 0 et 1, lignes « Modalités », « Indicateur », « Analyse », « Consigne si retenue » de la section A, préambule de la section B et définitions de O1, O4 et O0, liste des pièces ; le nom des fichiers du dossier `docs/notes/billets-v1/` (liste, sans ouvrir) ; la sortie standard d'une ligne de l'analyse (`sortie-standard-analyse-tenue-v1.txt`).
- **Refus d'outil, de permission, de crochet ou de classifieur** : aucun.

## Annexe A — programme du rejeu de la règle

Empreinte du fichier exécuté : `6e2602e5aa3ea2be030a13d5b1c78e6df823e855bd69574994227000cb22a046`. Appel : `python3 -I -B rejouer_regle.py docs/notes/billets-v1/grille-gestes-v1.md docs/notes/billets-v1/analyse-tenue-v1/analyse-tenue-v1.json` ; sortie `rejeu.json`, `ccb8e51ee1e47854063b665c43a0cf014135b9c9fe1b1f0d5bbf9e1a5aed4695`. Comparaison aux champs `fiabilite`, `consignes`, `m_comparaisons`, `p_holm` et `objection_a_prevenir` faite après la sortie.

```python
"""Rejeu indépendant de la règle de la section 8 (et 5.2, 5.3) de la grille gelée,
écrit par le contre-lecteur sans lire le programme du rédacteur ni celui de l'analyse.

Entrées : la grille gelée (statut d'analyse lu dans son texte) et l'analyse scellée.
Sortie : JSON sur la sortie standard.
"""
import json
import re
import sys

GRILLE, ANALYSE = sys.argv[1], sys.argv[2]

texte = open(GRILLE, encoding="utf-8").read()
# Statut d'analyse de chaque geste, lu dans la section A.
statut_analyse = {}
for bloc in re.split(r"\n### ", texte):
    m = re.match(r"(G\d\d)\. ", bloc)
    if not m:
        continue
    g = m.group(1)
    a = re.search(r"\*\*Analyse\*\* : (\w+)", bloc)
    statut_analyse[g] = "comparée" if a.group(1).startswith("compar") else "descriptive"
    c = re.search(r"\*\*Consigne si retenue\*\* : « (.*?) »", bloc)
    statut_analyse[g + "_consigne"] = c.group(1) if c else None

A = json.load(open(ANALYSE, encoding="utf-8"))
E = A["ensembles"]
GESTES = [f"G{i:02d}" for i in range(1, 26)]


def fiab(g):
    """Section 5.2 : prévalence extrême d'abord (sur l'un des deux ensembles), puis kappa >= 0,60 sur les deux."""
    vals = {}
    for ens in ("tous", "sans_marquage_1"):
        x = E[ens]["gestes"][g]
        vals[ens] = (x["prevalence_indicateur"], x["kappa_indicateur"])
    hautes = [e for e, (p, k) in vals.items() if p > 0.90]
    basses = [e for e, (p, k) in vals.items() if p < 0.10]
    if hautes and basses:
        return "conflit", vals
    if hautes:
        return "non-evaluable-haute", vals
    if basses:
        return "non-evaluable-basse", vals
    ok = all(k is not None and k == k and k >= 0.60 for (p, k) in vals.values())
    return ("fiable" if ok else "non-fiable"), vals


def holm(pvals):
    """Holm étagé, valeurs ajustées monotones, plafonnées à 1."""
    items = sorted(pvals.items(), key=lambda kv: (kv[1], kv[0]))
    m = len(items)
    adj, courant = {}, 0.0
    for i, (g, p) in enumerate(items):
        courant = max(courant, min(1.0, (m - i) * p))
        adj[g] = courant
    return adj


res = {}
fia = {g: fiab(g) for g in GESTES}
fiables_comparees = [g for g in GESTES if fia[g][0] == "fiable" and statut_analyse[g] == "comparée"]
m = len(fiables_comparees)
p_bruts = {g: E["tous"]["gestes"][g]["p_signe_exact"] for g in fiables_comparees}
p_holm = holm(p_bruts)

for g in GESTES:
    st, vals = fia[g]
    t = E["tous"]["gestes"][g]
    r = E["sans_reunion"]["gestes"][g]
    comp = statut_analyse[g] == "comparée"
    fbn = t["freq_bien_notes"]
    d23, d11 = t["d"], r["d"]
    ic_bas = t["ic95_d"][0]
    ph = p_holm.get(g)
    sig = ph is not None and ph < 0.05
    if st == "non-evaluable-haute":
        q = "convention du genre (fiabilité non mesurée)" if comp else "rapporté seulement (quasi universel, descriptif)"
        rang = 1
    elif st in ("non-evaluable-basse", "non-fiable", "conflit"):
        q, rang = "exclu", 2
    elif not comp:
        q, rang = "descriptif, rapporté, jamais consigne", 3
    elif d23 < 0 and sig:
        q, rang = "à éviter", 4
    elif fbn >= 0.5 and d23 >= 0 and d11 >= 0 and d23 > 0 and sig:
        q, rang = "consigne distinctive", 5
    elif fbn >= 0.5 and d23 >= 0 and d11 >= 0:
        q, rang = "consigne — pratique majoritaire, non contredite", 6
    elif fbn >= 0.5 and d23 >= 0 and d11 < 0:
        q, rang = "consigne sous réserve", 7
    elif fbn < 0.5 and ic_bas > 0:
        q, rang = "piste", 8
    else:
        q, rang = "aucune consigne", 9
    res[g] = {
        "analyse": statut_analyse[g],
        "fiabilite": st,
        "prev_tous": vals["tous"][0], "prev_sm1": vals["sans_marquage_1"][0],
        "kappa_tous": vals["tous"][1], "kappa_sm1": vals["sans_marquage_1"][1],
        "freq_bn": fbn, "n_bn": round(fbn * 39, 6),
        "d23": d23, "d11": d11, "ic95_d23": t["ic95_d"],
        "p_signe": t["p_signe_exact"], "p_holm_moi": ph, "p_holm_analyse": t.get("p_holm"),
        "qualificatif": q, "rang": rang,
        "consigne_ecrite": statut_analyse[g + "_consigne"],
    }

# Objections à prévenir (section 8, dernier paragraphe), ensemble « tous ».
OB = A["objections"]["tous"]
ob = {}
for c, x in OB["classes"].items():
    exclue = c in ("O0", "O12", "O13")
    k = x["kappa_binaire"]
    prev = x["prevalence"]
    extreme = prev > 0.90 or prev < 0.10
    fiable = (k is not None and k == k and k >= 0.60) and not extreme
    part = x["part"]
    touches = x["part_des_bien_notes_touches"]
    ok = (not exclue) and fiable and part >= 0.10 and touches >= 0.25
    ob[c] = {"kappa": k, "prev": prev, "part": part, "touches": touches, "n_touches": round(touches * 39, 6),
             "a_prevenir_moi": ok, "a_prevenir_analyse": x.get("objection_a_prevenir")}

print(json.dumps({"m": m, "fiables_comparees": fiables_comparees, "gestes": res, "objections": ob},
                 ensure_ascii=False, indent=1))
```

## Annexe B — contrôle par clé des chiffres de l'application pas à pas

Empreinte : `df471f0a1df7a0a7d9e5b7fdc1317cd5a3588feff9639c98f726187239a5f16e`. Sortie : « vérifiés 1112 écarts 0 ».

```python
"""Vérifie, clé par clé, les chiffres recopiés dans l'application pas à pas.
Écrit par le contre-lecteur. Entrées : application, analyse, grille."""
import json
import re
import sys

APP, ANALYSE, GRILLE = sys.argv[1:4]
txt = open(APP, encoding="utf-8").read()
A = json.load(open(ANALYSE, encoding="utf-8"))
E = A["ensembles"]
grille = open(GRILLE, encoding="utf-8").read()

NUM = r"-?\d+(?:\.\d+)?(?:e-?\d+)?"
ok, ko, vus = 0, [], set()


def chk(label, attendu, lu, pos):
    global ok
    vus.add(pos)
    if attendu is None:
        ko.append((label, "clé absente", lu))
        return
    if repr(float(attendu)) == repr(float(lu)) or float(attendu) == float(lu):
        ok += 1
    else:
        ko.append((label, attendu, lu))


# Découpage par geste (section 3) ; le reste est traité à part.
sections = [x.split("\n## ")[0] for x in re.split(r"\n### ", txt)]
for sec in sections:
    m = re.match(r".*?\((G\d\d)\) — analyse (\w+) — (.*)", sec)
    if not m:
        continue
    g = m.group(1)
    start = txt.index(sec)
    def G(ens):
        return E[ens]["gestes"][g]
    # analyse
    if not G("tous")["analyse"].startswith(m.group(2)[:7]):
        ko.append((g, "analyse", m.group(2)))
    # « Consigne si retenue »
    c = re.search(r"Ligne « Consigne si retenue » de la grille : « (.*?) »", sec)
    bloc = re.search(r"### " + g + r"\. .*?(?=\n### |\n## )", grille, re.S).group(0)
    cg = re.search(r"\*\*Consigne si retenue\*\* : « (.*?) »", bloc)
    if c and cg and c.group(1) != cg.group(1):
        ko.append((g, "consigne", c.group(1)))
    if bool(c) != bool(cg):
        ko.append((g, "consigne présence", bool(c)))
    # deux ensembles : `k` = v (tous), v (sans_marquage_1)
    for mm in re.finditer(r"`(\w+)` = (" + NUM + r") \(tous\), (" + NUM + r") \(sans_marquage_1\)", sec):
        k = mm.group(1)
        chk(f"{g}.{k}.tous", G("tous").get(k), mm.group(2), start + mm.start(2))
        chk(f"{g}.{k}.sm1", G("sans_marquage_1").get(k), mm.group(3), start + mm.start(3))
    # `k` (ens) = v
    for mm in re.finditer(r"`(\w+)` \((\w+)\) = (" + NUM + r")", sec):
        k, ens, v = mm.groups()
        if k == "ic95_d":
            continue
        chk(f"{g}.{k}.{ens}", G(ens).get(k), v, start + mm.start(3))
    # borne basse de `ic95_d` (tous) = v
    for mm in re.finditer(r"borne basse de `ic95_d` \(tous\) = (" + NUM + r")", sec):
        chk(f"{g}.ic95_d[0]", G("tous")["ic95_d"][0], mm.group(1), start + mm.start(1))
    # triple des fréquences
    mm = re.search(r"`freq_bien_notes` / `freq_apparies` / `freq_bien_notes_sans_apparie` \(tous\) : (" + NUM + r") / (" + NUM + r") / (" + NUM + r")", sec)
    if mm:
        for i, k in enumerate(["freq_bien_notes", "freq_apparies", "freq_bien_notes_sans_apparie"]):
            chk(f"{g}.{k}", G("tous")[k], mm.group(i + 1), start + mm.start(i + 1))
    else:
        ko.append((g, "triple absent", ""))
    # d et ic95_d sur les quatre ensembles
    for mm in re.finditer(r"\((tous|sans_marquage_1|sans_marquage_2|sans_reunion)\) (" + NUM + r") \[(" + NUM + r"), (" + NUM + r")\]", sec):
        ens = mm.group(1)
        chk(f"{g}.d.{ens}", G(ens)["d"], mm.group(2), start + mm.start(2))
        chk(f"{g}.ic95_d0.{ens}", G(ens)["ic95_d"][0], mm.group(3), start + mm.start(3))
        chk(f"{g}.ic95_d1.{ens}", G(ens)["ic95_d"][1], mm.group(4), start + mm.start(4))
    # p_signe_exact, p_holm, ic_bonferroni_d
    mm = re.search(r"`p_signe_exact` \(tous\) : (" + NUM + r")", sec)
    chk(f"{g}.p_signe_exact", G("tous")["p_signe_exact"], mm.group(1), start + mm.start(1))
    mm = re.search(r"`p_holm` \(tous\) : (clé absente|" + NUM + r")", sec)
    if mm.group(1) == "clé absente":
        if "p_holm" in G("tous"):
            ko.append((g, "p_holm dit absent", G("tous")["p_holm"]))
        else:
            ok += 1
    else:
        chk(f"{g}.p_holm:", G("tous").get("p_holm"), mm.group(1), start + mm.start(1))
    mm = re.search(r"`ic_bonferroni_d` \(tous\) : (clé absente|\[(" + NUM + r"), (" + NUM + r")\])", sec)
    if mm.group(1) == "clé absente":
        if "ic_bonferroni_d" in G("tous"):
            ko.append((g, "ic_bonf dit absent", ""))
        else:
            ok += 1
    else:
        chk(f"{g}.icb0", G("tous")["ic_bonferroni_d"][0], mm.group(2), start + mm.start(2))
        chk(f"{g}.icb1", G("tous")["ic_bonferroni_d"][1], mm.group(3), start + mm.start(3))
    mm = re.search(r"`aveugle\.sensibilite_sans_reconnus\.d\." + g + r"` = (" + NUM + r")", sec)
    chk(f"{g}.sens", A["aveugle"]["sensibilite_sans_reconnus"]["d"][g], mm.group(1), start + mm.start(1))
    # champ consignes
    mm = re.search(r"Champ `consignes\." + g + r"` de l'analyse : « (.*?) »", sec)
    if mm.group(1) != A["consignes"][g]:
        ko.append((g, "consignes recopié", mm.group(1)))
    else:
        ok += 1

# Tableau de la section 2
for mm in re.finditer(r"^\| [^|]*\((G\d\d)\) \| (" + NUM + r") \| \[(" + NUM + r"), (" + NUM + r")\] \| (" + NUM + r") \| (" + NUM + r") \| (" + NUM + r") \| (" + NUM + r") \| ([^|]+) \| ([^|]+) \|$", txt, re.M):
    g = mm.group(1)
    t, s = E["tous"]["gestes"][g], E["sans_marquage_1"]["gestes"][g]
    vals = [t["kappa_indicateur"], t["ic95_kappa_indicateur"][0], t["ic95_kappa_indicateur"][1], s["kappa_indicateur"],
            t["prevalence_indicateur"], s["prevalence_indicateur"], t["accord_brut_indicateur"]]
    for i, v in enumerate(vals):
        chk(f"tab2.{g}.{i}", v, mm.group(i + 2), mm.start(i + 2))
    if mm.group(10).strip() != A["fiabilite"][g]["statut"]:
        ko.append((g, "fiabilite recopiée", mm.group(10)))
    else:
        ok += 1

# Tableau des objections (section 5)
for mm in re.finditer(r"^\| [^|]*\((O\d+)\) \| (" + NUM + r") \| (" + NUM + r") \| (" + NUM + r") \| [^|]+ \| (" + NUM + r") \| \[(" + NUM + r"), (" + NUM + r")\] \| (" + NUM + r") \| [^|]+ \| [^|]+ \| (true|false) \|$", txt, re.M):
    c = mm.group(1)
    x = A["objections"]["tous"]["classes"][c]
    vals = [x["kappa_binaire"], x["accord_brut"], x["prevalence"], x["part"], x["ic95_part"][0], x["ic95_part"][1], x["part_des_bien_notes_touches"]]
    for i, v in enumerate(vals):
        chk(f"ob.{c}.{i}", v, mm.group(i + 2), mm.start(i + 2))
    if (mm.group(9) == "true") != x["objection_a_prevenir"]:
        ko.append((c, "objection_a_prevenir", mm.group(9)))
    else:
        ok += 1

# Autres chiffres hors des sections de gestes : vérifiés à la main (liste rendue).
reste = []
for mm in re.finditer(NUM, txt):
    if mm.start() not in vus and "." in mm.group(0) and len(mm.group(0)) > 5:
        reste.append((mm.group(0), txt[max(0, mm.start() - 80):mm.start()].replace("\n", " ")[-80:]))
print("vérifiés", ok, "écarts", len(ko))
for k in ko:
    print("ÉCART", k)
print("chiffres longs non couverts par le programme :", len(reste))
for r in reste:
    print("  ", r[0], "<<", r[1])
```

## Annexe C — contrôle des chiffres arrondis du gabarit

Empreinte : `81fd2b9a7839384f390bbba5d874bd294f499026e58b26dc63041fad896fc87c`. Sortie : « lignes de consigne 70 ; tableau 2 144 ; sensibilités 24 ; tableau 3 85 ; écarts [] ».

```python
"""Vérifie les chiffres arrondis du gabarit contre l'analyse (contre-lecteur)."""
import json
import re
import sys

GAB, ANALYSE = sys.argv[1:3]
t = open(GAB, encoding="utf-8").read()
A = json.load(open(ANALYSE, encoding="utf-8"))
E = A["ensembles"]
N = r"-?\d+,\d+"
ok, ko = 0, []


def r(v, nd=3):
    return (f"%.{nd}f" % v).replace(".", ",").replace("-0,000", "0,000")


def eq(label, attendu, lu, nd=3):
    global ok
    if r(attendu, nd) == lu or (lu.startswith("-") and r(attendu, nd) == lu.replace("-", "", 1) and float(attendu) == 0):
        ok += 1
    else:
        ko.append((label, r(attendu, nd), lu))


ENS = ["tous", "sans_marquage_1", "sans_marquage_2", "sans_reunion"]
# 1.1 et 1.2 : lignes de consigne
for m in re.finditer(r"fréquence chez les bien notés (" + N + r") \(chez les appariés (" + N + r")\) ; différence appariée (" + N + r"), intervalle \[(" + N + r") ; (" + N + r")\] sur les 23 paires, (" + N + r") \[(" + N + r") ; (" + N + r")\] sur les 11 ; intervalle du kappa \[(" + N + r") ; (" + N + r")\] ; [^\n]*?(G\d\d)\)\.", t):
    g = m.group(11)
    T, R = E["tous"]["gestes"][g], E["sans_reunion"]["gestes"][g]
    vals = [T["freq_bien_notes"], T["freq_apparies"], T["d"], T["ic95_d"][0], T["ic95_d"][1], R["d"], R["ic95_d"][0], R["ic95_d"][1], T["ic95_kappa_indicateur"][0], T["ic95_kappa_indicateur"][1]]
    for i, v in enumerate(vals):
        eq(f"1.x {g} {i}", v, m.group(i + 1))
n11 = ok
# Tableau 2
for m in re.finditer(r"^\| « [^|]* » \| [^|]*\((G\d\d)\) \| [^|]+ \| [^|]+ \| (" + N + r") \| (" + N + r") \| ([^|]+) \| ([^|]+) \| ([^|]+) \| [^|]+ \|$", t, re.M):
    g = m.group(1)
    T = E["tous"]["gestes"][g]
    eq(f"t2 {g} fbn", T["freq_bien_notes"], m.group(2))
    eq(f"t2 {g} fap", T["freq_apparies"], m.group(3))
    blocs = [b.strip() for b in m.group(4).split(" ; ")]
    # 4 ensembles : "d [a ; b]" séparés par " ; " -> recomposer
    nums = re.findall(N, m.group(4))
    assert len(nums) == 12, (g, nums)
    for k, e in enumerate(ENS):
        X = E[e]["gestes"][g]
        eq(f"t2 {g} d {e}", X["d"], nums[3 * k])
        eq(f"t2 {g} ic0 {e}", X["ic95_d"][0], nums[3 * k + 1])
        eq(f"t2 {g} ic1 {e}", X["ic95_d"][1], nums[3 * k + 2])
    ph = m.group(5).strip()
    if "absente" in ph:
        ok += ("p_holm" not in T)
        if "p_holm" in T:
            ko.append((g, "p_holm dit absent", ph))
    else:
        eq(f"t2 {g} ph", T["p_holm"], ph)
    kk = re.findall(N, m.group(6))
    eq(f"t2 {g} k", T["kappa_indicateur"], kk[0])
    eq(f"t2 {g} k0", T["ic95_kappa_indicateur"][0], kk[1])
    eq(f"t2 {g} k1", T["ic95_kappa_indicateur"][1], kk[2])
n2 = ok - n11
# Sensibilités
for m in re.finditer(r"^\| [^|]*\((G\d\d)\) \| (" + N + r") \| (" + N + r") \| (" + N + r") \|$", t, re.M):
    g = m.group(1)
    T = E["tous"]["gestes"][g]
    eq(f"s {g} c1", T["d_codeur_1"], m.group(2))
    eq(f"s {g} c2", T["d_codeur_2"], m.group(3))
    eq(f"s {g} sr", A["aveugle"]["sensibilite_sans_reconnus"]["d"][g], m.group(4))
n3 = ok - n11 - n2
# Tableau 3
for m in re.finditer(r"^\| [^|]*\((G\d\d)\) \| [^|]+ \| [^|]+ \| ([^|]+) \|$", t, re.M):
    g = m.group(1)
    T = E["tous"]["gestes"][g]
    cell = m.group(2)
    for k, nd, key in (("freq_bien_notes", 3, None), ("freq_apparies", 3, None)):
        mm = re.search(r"`" + k + r"` (" + N + r")", cell)
        if mm:
            eq(f"t3 {g} {k}", T[k], mm.group(1))
    mm = re.search(r"borne basse de `ic95_d` (" + N + r")", cell)
    if mm:
        eq(f"t3 {g} borne", T["ic95_d"][0], mm.group(1), 4)
    mm = re.search(r"`d` (" + N + r") \[(" + N + r") ; (" + N + r")\]", cell)
    if mm:
        eq(f"t3 {g} d", T["d"], mm.group(1)); eq(f"t3 {g} i0", T["ic95_d"][0], mm.group(2)); eq(f"t3 {g} i1", T["ic95_d"][1], mm.group(3))
    mm = re.search(r"`p_holm` (" + N + r")", cell)
    if mm:
        eq(f"t3 {g} ph", T["p_holm"], mm.group(1))
    mm = re.search(r"prévalence de l'indicateur (" + N + r")", cell)
    if mm:
        eq(f"t3 {g} prev", T["prevalence_indicateur"], mm.group(1))
    mm = re.search(r"accord brut (" + N + r")", cell)
    if mm:
        eq(f"t3 {g} ab", T["accord_brut_indicateur"], mm.group(1))
n4 = ok - n11 - n2 - n3
print("lignes de consigne", n11, "; tableau 2", n2, "; sensibilités", n3, "; tableau 3", n4, "; écarts", ko)
```
