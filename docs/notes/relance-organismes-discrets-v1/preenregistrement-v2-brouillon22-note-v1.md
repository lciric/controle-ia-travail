# Note de changements — brouillon 22 du texte neuf du bras A des organismes discrets — v1

**Rédigé par Claude Fable 5.2 (`claude-fable-5-2`)**, le même agent que pour le brouillon 21. Je conçois ; la session qui m'orchestre consigne, scelle au registre et committe.

- **Brouillon** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon22.md`, `ade786eb4065722aee6b05ce8246767dd8cf5f52bff16463f7c59b95547a0396` (1 930 lignes). Le brouillon 21 n'est pas modifié (`8d834631c102e1b42d5ce20083d45df3a9d793c59ca7afba32e5eed2d42dc808`), ni le brouillon 20 (`b076e3f9…`) : vérifiés avant la copie et après l'écriture.
- **Fiches pour Lazar** : `docs/notes/relance-organismes-discrets-v1/decisions-bras-a-brouillon22-v1.md`, `80581f3cec1f143c6582d60f9d8fe6775b7186f238adf5d2080eb9b1efe343e2`. Elle remplace celles des brouillons 21 (`534abe1e…`) et 19 (`955aa979…`), qui restent archivées.
- **Source** : la contre-lecture du brouillon 21 par un agent Claude Opus 5.5 neuf, `docs/notes/relance-organismes-discrets-v1/contre-lecture-brouillon21-bras-a-v1.md`, `6b155c84965eb24615d77c7409eeff3798603401fa410078b0f0dd9d14dca6e6`, lue en entier. Verdict : engageable après corrections ; aucun bloquant ; huit défauts à corriger ; neuf mineurs.
- **Méthode** : copie du brouillon 21 par `cp`, puis 38 remplacements exacts, chacun vérifié unique par programme.
- **Rien n'est arrivé de Lazar ni de la session principale** : registre des accords relu sur la branche principale distante au commit `c84fe1c4` ; une ligne de plus, GO-2026-11-19-76, sans rapport avec le bras A.
- **Heures (UTC, `date -u`)** : début 15:36:06Z le 2026-11-19 ; brouillon scellé à 15:46:24Z.
- **Interdits tenus, sans écart cette fois** : mon programme de contrôle ne prend plus l'empreinte d'aucun fichier des dossiers du côté habilité (liste ci-dessous) ; aucun interne de moniteur ; aucune fiche de l'organisme d'idéation ; aucune réponse de l'essai de mesure ; aucune clé ; aucun appel de modèle ; seul appel réseau, `git fetch` de la branche principale ; ni `registres/`, ni `.claude/`, ni le journal touchés ; rien committé ; aucun fichier existant écrasé ; suite d'essais non lancée ; aucun sous-agent ; aucun fichier `*_v5.py` ouvert.

## Contrôles par programme

| contrôle | résultat |
|---|---|
| titres de section (53) | les 52 titres de niveau 2 et 3 sont identiques à ceux du brouillon 21 ; seul le titre de niveau 1 change |
| consignes figées (blocs de 3.2 et 3.3) | égales octet pour octet à celles du brouillon 20 ; `98a9bd34d280fc7d9db07a733bc78557ff350538a3ace7a2926999ecf14c9248` et `ecf590eae0c06d413d173f7f03c5575e52d6034613e0a1a30d681149435a1816`, recalculées |
| citations à la lettre du brouillon 20 | les 935 passages entre guillemets les plus extérieurs du brouillon 20 sont tous retrouvés ; la fiche du point 17 et l'avis d'origine sont intacts |
| citations du brouillon 21 | 1 021 passages ; un seul n'est pas retrouvé, « forme d'une livraison », qui était le nom d'une garde dans une phrase que j'ai récrite : ce n'est pas une citation d'un texte transmis |
| table d'en-tête, **sans les fichiers cloisonnés** | 125 lignes à empreinte : 111 recalculées et égales, 0 différente, **14 sautées et non ouvertes** — tout ce qui est sous `docs/notes/bras-a-moniteurs-v1/` hors la pièce permise (6), sous `docs/notes/bras-a-contre-lecture-habilitee-v1/` (4), sous `registres/` (1), et les fichiers `prereg/T0.6…` (2, dont la configuration de référence) et `prereg/T0.8…` (1) ; ces quatorze lignes gardent l'empreinte héritée des brouillons précédents, **non vérifiée par moi** |
| marque des cases non remplies | huit lignes, toutes en 13.1 |
| validateur (`problemes()`) | deux problèmes, les mêmes qu'aux brouillons 20 et 21, attendus : marque restante hors des sections exigées ; contre-lecture 10 sans ses deux empreintes. La contre-lecture 11, neuve, porte les siennes |
| section 12 | points 1 à 20, dans l'ordre |
| fiches 9, 10 et 11 | chaque puce du fichier des fiches est une sous-chaîne exacte de la section 12 du brouillon 22 |
| différence avec le brouillon 21 | 43 lignes de plus ; 42 lignes changées |

## 1. La contre-lecture, défaut par défaut

| défaut | traitement | ce que j'ai écrit |
|---|---|---|
| C-1 option (b) du seuil de 1 % | **corrigé** | sous l'option (b), le module doit compter de même, sinon la table des formes arrête la lecture à 20 tirages dégénérés ; la fiche le dit, et dit que choisir (b) demande de changer le module |
| C-2 « moniteur appris non ajustable » | **rouvert, posé** | l'issue n'est plus tranchée : trois rédactions en 6.9 ; question au développeur habilité ; fiche 11, sans défaut, qui tombe s'il répond que la séparation parfaite ne peut pas déclencher ce motif ; nombre de lectures sous ce motif rapporté |
| C-3 issue d'une lecture arrêtée | **corrigé, sans fiche** | c'est la ligne A17, par sa lettre : rien n'est conclu sur la discrétion, ce qui est scellé avant reste, reprise par nœud ; la livraison refusée est ajoutée à la liste de A17 ; ma réserve 5 du brouillon 21 était fausse |
| C-4 phrases contraires à GO-2026-11-19-70 | **corrigé** | la précision est portée en 6.9, 6.10, 8.2, à la ligne A17, et à un cinquième endroit que le contre-lecteur ne citait pas, 6.12, point 5 |
| C-5 gardes sans artefact | **corrigé** | les six artefacts sont dans les lignes de 8.4 |
| C-6 fiche de l'intervalle impossible | **corrigé** | option « anomalie » ajoutée ; avantage de l'option (a) repris ; **aucun défaut** ; les trois rédactions écrites en entier (6.9, table des formes, 8.4) ; ma confiance passe de 0,8 à 0,6 |
| C-7 hypothèse restante de l'option 2 | **corrigé** | l'inconvénient est rendu à l'option 2, dans l'avis du point 17 et dans le rappel ; « presque jamais » est borné aux paires qui se ressemblent ; « tient son niveau » est conditionné ; ma confiance passe de 0,8 à 0,7 |
| C-8 dose ¼ | **corrigé** | un écart de structure arrête toute l'étape, à toute dose ; une grandeur `null` n'arrête qu'à une dose de la famille ; à la dose ¼ elle est « non rendue », et la valeur de la famille n'y est ni lue ni contrôlée |
| M-1 « C6 devient C5 » | **corrigé** | « la ligne C6 est exclue à cette dose » |
| M-2 échéance de la fiche 9 | **corrigé** | échéance d'origine gardée, le 21 novembre vers 14:30Z ; la fiche dit qu'elle a été réécrite ; la session qui orchestre en décide |
| M-3 phrase « Cause » | **corrigé** | bornée aux seuls motifs qui gardent la valeur 1 |
| M-4 source du principe | **corrigé** | lecture de GO-2026-11-19-24, point 1, étendue par le texte au module ; dit comme une exigence du texte, non un mot de Lazar |
| M-5 aire au cas C | **repris comme demande** | demandé à la session principale, non exigé ; l'assouplissement reste, rapporté |
| M-6 « aucune règle de jugement ne change » | **corrigé** | « aucune règle choisie par Lazar ne change ; trois issues sont ouvertes, sans défaut » |
| M-7 empreintes de fichiers cloisonnés | **corrigé dans la méthode** | le programme les saute ; à consigner par la session qui orchestre |
| M-8 égalité de la valeur de la famille | **corrigé** | égalité exacte, sans tolérance |
| M-9 `effectifs` et `exclues` | **corrigé** | aucune règle de l'instance d'analyse ne les lit ; la garde des effectifs est celle de 6.12, point 2, et de 8.1 |

Aucun défaut n'est écarté. Sur l'avis du contre-lecteur à la dernière ligne de sa table (une réserve écrite en 7.7 doit aller à Lazar) : repris, dans l'avis du point 17, dans le rappel et dans les demandes ci-dessous.

## 2. Ce qui change, section par section

| section | changement |
|---|---|
| titre ; statut ; auteur ; date ; commit lu | brouillon 22 ; la phrase du brouillon 21 sur les règles de jugement est reprise (M-6) |
| table d'en-tête | quatre lignes : le brouillon 21, sa note, ses fiches, sa contre-lecture |
| conventions | « Numérotation stable » ; « non rendue » étendue à la dose ¼ |
| 6.9, « Indécis » | précision de GO-2026-11-19-70 dans la phrase « Tirages dégénérés » ; intervalle impossible sous trois rédactions |
| 6.9, « Partage du travail » | option (b) du seuil : module à changer ; « Vides » accordé aux trois rédactions ; source du principe ; `effectifs` ; « Cause » ; motif « non ajustable » ouvert, trois rédactions |
| 6.9, table des formes | récrite : ordre de reconnaissance B, C, E, D, A ; deux sortes d'écart ; ce que vaut l'arrêt (ligne A17) ; égalité exacte ; trois lignes pour le cas E |
| 6.10 ; 6.12, point 5 ; 8.2 | précision de GO-2026-11-19-70 |
| 7.2, ligne A17 | précision de GO-2026-11-19-70 ; la livraison refusée entre dans la liste des événements |
| 8.4 | cinq lignes reprises : famille de Holm, intervalle dégénéré seul, forme d'une livraison, listes fermées, réglages rendus |
| 12 | avis du point 17 repris ; fiches des points 18 et 19 réécrites ; **point 20 neuf** |
| 13 ; 13.1 | point 20 ; case « nœuds » ; case du module : quatre demandes de plus |
| 14.34 | neuve : table du traitement de la contre-lecture |
| « Contre-lecture » | **contre-lecture 11**, inscrite avec ses deux empreintes ; la contre-lecture 10 reste à faire |

## 3. Les fiches pour Lazar

1. **Fiche 9 — sur quel nombre se compte le seuil de 1 % de tirages dégénérés.** (a) sur les 2 000 demandés, 21 ou plus, module inchangé ; (b) sur les calculés, 20 ou plus, module à changer et à contre-lire. Recommandation (a), confiance 0,85. Défaut : (a), échéance d'origine, le 21 novembre vers 14:30Z.
2. **Fiche 10 — l'état d'un moniteur dont l'intervalle n'a pas pu être calculé du tout.** (a) comme un intervalle entièrement dégénéré ; (b) « indécis » d'office ; (c) anomalie, la lecture de la discrétion s'arrête. Recommandation (a), confiance 0,6 ; (c) si le développeur habilité répond que le cas ne peut venir que d'un défaut de la course. **Aucun défaut.**
3. **Fiche 11, neuve — l'état d'un moniteur appris qui n'a pas pu être ajusté.** Elle tombe si la séparation parfaite ne peut pas déclencher ce cas. Sinon : (a) « indécis » toujours ; (b) anomalie ; (c) faire corriger le module pour qu'il rende une aire. Recommandation : attendre la réponse, puis (c), confiance 0,6. **Aucun défaut.**
4. **Rappel complété — schéma de permutation.** Option 2 recommandée, confiance 0,7, avec son inconvénient rendu. **Aucun défaut.** Son envoi revient à la session qui tient la question.

## 4. Ce qui est demandé à la session principale (rien n'est présumé)

Les sept points de la note du brouillon 21 tiennent. Ils sont repris et complétés des cinq manques relevés par le contre-lecteur (points 6 à 10).

1. **Corriger l'écart à GO-2026-11-19-70** : quand seul l'intervalle manque, rendre l'aire, les aires des plis, les deux valeurs p et le nombre d'aires au moins égales, et mettre la valeur p haute dans `valeur_p_pour_la_famille`, exactement égale. Sinon l'analyse arrête la lecture (ligne A17).
2. **Intervalle impossible** : la forme dépend de la fiche 10 ; sous son option (a), la même que ci-dessus.
3. **Version qui fait foi** : chemin, empreinte complète, commit, essais ; épreuve par retrait et notice pour cette version ; **épreuve de forme**, un cas synthétique par ligne de la table des formes, avant toute dépense.
4. **Valeurs à transmettre, à la lettre** : la liste fermée des valeurs de `motif` et le cas que nomme chacune ; la valeur de `motif` quand tout est calculable ; celle de `calculable` aux cas A, D et E ; les valeurs de `reglages.permutation` et de `reglages.unite_de_la_permutation` sous chaque schéma ; celle de `reglages.statistique_agregateur` ; la forme des doses dans `reglages` ; ce que porte `quantile_borne_haute`.
5. **Deux lectures à confirmer** : les comptes d'exclusion dans `exclues` ; l'empreinte du fichier des scores par unité dans `scores_par_unite.sha256`.
6. **Neuf — ce qui déclenche « moniteur appris non ajustable »** sur les étiquettes observées, dit sans interne, et si une séparation parfaite des deux classes en fait partie. La fiche 11 en dépend.
7. **Neuf — ce qui déclenche « intervalle impossible faute de deux tâches »**, et si cela peut arriver dans une course aux effectifs conformes. La fiche 10 s'appuie sur « ne devrait pas se produire dans une course saine », que je n'ai pas pu vérifier.
8. **Neuf — au cas C** (plancher au-delà de 1 %), rendre l'aire et les aires des plis, qui ne dépendent pas des permutations. Demandé, non exigé.
9. **Neuf — si Lazar retient l'option (b) de la fiche 9**, un module qui compte le 1 % de l'intervalle sur les tirages calculés, et rend le motif de l'intervalle dégénéré dès 20.
10. **Neuf — réserve sur la ligne C4** : les trois différences d'exécution entre l'épisode honnête et l'épisode dosé appellent-elles une réserve ? L'avis de la session principale est demandé ; **si une réserve s'écrit en 7.7, c'est un critère de lecture, qui revient à Lazar**.
11. Inchangés : la lecture du juge d'une autre lignée (2 560 ou 6 400), sur un chiffrage à écrire ; le renvoi de la base ; le lanceur de l'étape de discrétion.

## 5. Cases restantes de 13.1 (huit lignes portent la marque)

| case | ce qui manque | qui |
|---|---|---|
| nœuds | mot de Lazar ou défaut échu sur le point 18 ; mot de Lazar, sans défaut, sur le point 19, et sur le point 20 si le développeur habilité répond oui ; dates d'envoi | Lazar |
| schéma de permutation | mot de Lazar sur le point 17 ; sans défaut | Lazar |
| lecteurs et juge des ancres | sortie maximale du lecteur 2 ; mot de Lazar sur le choix des lecteurs | Lazar |
| lecture du juge d'une autre lignée | 2 560 ou 6 400 | Lazar, sur un chiffrage de la session principale |
| entropie | l'entier racine ; mot de Lazar sur l'écart à R9 | Lazar ; session de relance |
| renvoi de la base | « vérifié » ou « non vérifié » | lecteur habilité de la session principale |
| commit du code de l'instrument et de l'analyse | commit et empreintes de la version 5 | session de relance |
| module des cinq moniteurs, côté habilité | douze exigences (partie 4 ci-dessus) | session principale |

Hors de 13.1 : la contre-lecture 10, par un agent Claude Opus 5.5 neuf, sur le texte aux cases remplies.

## 6. Ce que le code de la version 5 doit porter

Cette partie remplace la partie 6 de la note du brouillon 21. Les points marqués **changé** diffèrent de cette note-là ; le reste en est repris.

**Tient, sans changement** : nom du fichier et champ `rang` ; les quatre listes de noms de la version 8 ; `null` et zéro ; seuil sous l'option (a), 21 sur 2 000 demandés, total des tirages exigé à 2 000 ; la famille prend `valeur_p_pour_la_famille` sans la recomposer ; garde du cloisonnement.

1. **Le cas se reconnaît aux comptes**, dans cet ordre : B si les comptes de permutations sont `null` ; sinon C si `permutations_degenerees` vaut 21 ou plus ; sinon E si le couple des tirages est `null` ; sinon D si `tirages_degeneres` vaut 21 ou plus ; sinon A. `motif` doit ensuite nommer le même cas et appartenir à sa liste fermée.
2. **Deux sortes d'écart — changé.**
   - Écart de structure, à toute dose, la dose ¼ comprise : arrêt pour toute l'étape. Ce sont : un seul compte d'un couple `null` ; permutations `null` et tirages remplis ; `n_permutations` ou total des tirages autre que 2 000 ; compte négatif, non entier ou plus grand que son total ; au cas B, aire, valeur p ou borne remplie ; `motif` qui nomme un autre cas ou hors de sa liste ; `calculable` vrai au cas B ou C ; liste fermée ou réglage en défaut ; `quantile_borne_haute` autre que 1 − 0,05 ÷ 15.
   - Grandeur `null` que le cas exige : arrêt **à une dose de {½, ¾, 1} seulement** ; à la dose ¼, « non rendue » avec le motif, sans arrêt. La note du brouillon 21 disait « mêmes cas et mêmes arrêts » à la dose ¼ : ce n'est plus vrai.
3. **L'arrêt est la ligne A17 — changé.** L'exception levée doit porter ce nom d'issue, et non un simple refus : rien n'est conclu sur la discrétion ; les lignes de la table B, scellées avant, restent ; la livraison refusée est versée et scellée ; aucun état n'est dit après. Un essai vérifie qu'aucun état ne sort après un refus.
4. **Valeur p haute calculable** : comptes de permutations remplis et plancher de 20 au plus. À une dose de la famille, `valeur_p_haut` `null`, ou une valeur de la famille différente d'elle, arrête. **Égalité exacte, sans tolérance — changé.**
5. **Cas E, trois rédactions — changé.** Un seul choix nommé, sans valeur par défaut, à trois valeurs : (a) comme le cas D ; (b) valeur 1 gardée, « indécis », valeurs p non lues ; (c) arrêt à une dose de la famille, rien à la dose ¼. Un essai par rédaction. La note du brouillon 21 en prévoyait deux et un défaut.
6. **Motif « moniteur appris non ajustable », trois rédactions — changé.** Un seul choix nommé, sans valeur par défaut : (a) cas B, « indécis », valeur 1 ; (b) arrêt à une dose de la famille ; (c) comme (a), le module ne rendant plus ce motif pour une séparation. Pour l'analyse, (a) et (c) se codent de même. Le nombre de lectures sous ce motif est rapporté par moniteur et par dose. La note du brouillon 21 le rangeait au cas B sans condition.
7. **Seuil et option** : un seul endroit nommé pour l'option (a) ou (b) ; sous (b), 20 sur les calculés pour les seuls tirages, et le module doit compter de même.
8. **« Non rendue »** : au cas C et au cas E sous la rédaction (b), aire, aires des plis ou valeurs p `null` ; à la dose ¼, toute grandeur exigée `null`. Aux cas D et E, la borne haute est toujours rapportée « non calculable », ligne C4 comprise.
9. **Couples `null` admis** : les deux au cas B ; le seul couple des tirages aux cas C et E.
10. **Listes fermées et vingt lectures** ; **contrôle des réglages**, avec en plus, depuis ce brouillon, des artefacts nommés pour `dose_pour_information`, `statistique_agregateur` et le `n_permutations` d'une lecture — **changé** : chacun a son essai.
11. **Chaînes inconnues** : valeurs de `motif`, de `calculable` aux cas A, D et E, de `permutation`, d'`unite_de_la_permutation`, de `statistique_agregateur`, forme des doses, contenu de `quantile_borne_haute` : paramètres obligatoires, sans valeur par défaut, lus dans la configuration scellée ; ne deviner aucune chaîne.
12. **Empreinte du fichier des scores par unité** : prise dans `scores_par_unite.sha256` de la sortie scellée ; compagnon vérifié.
13. **`effectifs` et `exclues`** : aucune règle ne les lit ; rapportés tels quels.
14. **Le cas et le motif de chaque lecture sont rapportés**, par moniteur et par dose — **changé** (neuf).

**Inchangé, à prendre dans la contre-lecture du code** : C-2, C-5, C-6, C-7, C-10, M-1, M-2, M-5 à M-11. M-4 (valeurs p confrontées à leurs comptes) : le texte ne l'exige toujours pas.

## 7. Réserves

1. **Ligne A17 : j'applique la lettre, je ne la choisis pas.** La ligne dit « un événement de la liste d'arrêt sans autre ligne » ; j'y ai ajouté la livraison refusée, dans sa liste. C'est une ligne d'une table de verdict : si la session qui orchestre ou Lazar veut une autre issue — par exemple « discrétion non lue » et une reprise permise sans nœud —, c'est l'issue d'un cas, donc une fiche. Je ne la propose pas.
2. **Trois issues ouvertes au lieu d'une.** Le texte porte maintenant plusieurs rédactions en trois endroits (schéma de permutation ; intervalle impossible ; moniteur non ajustable). Le code doit porter trois choix nommés sans défaut ; le scellement attend les trois.
3. **La fiche 11 dépend d'un fait que je ne peux pas lire.** Elle peut tomber. Je l'ai écrite quand même, comme le mandat le demande, en disant en tête qu'elle peut tomber.
4. **Assouplissement neuf à la dose ¼.** Une grandeur `null` n'y arrête plus rien. C'est un choix de conception qui ne touche aucun état ; le second contre-lecteur peut vouloir l'arrêt.
5. **Je n'ai toujours pas relu le texte en entier.** De plus qu'au brouillon 21 : 6.10, 6.12 point 5, 7.2, 8.2, 8.3, 8.5, 8.6. Le contre-lecteur a trouvé à la ligne A17 une phrase que je n'avais pas vue ; d'autres peuvent rester ailleurs.
6. **Quatorze lignes de la table d'en-tête ne sont plus vérifiées par moi.** Elles gardent l'empreinte héritée. **Rectification du compte déclaré au brouillon 21** : sa note disait neuf fichiers du côté habilité dont l'empreinte avait été prise par programme ; le compte juste est **onze** — six de `docs/notes/bras-a-moniteurs-v1/` (j'en avais nommé six et écrit « cinq »), quatre de `docs/notes/bras-a-contre-lecture-habilitee-v1/`, et la configuration de référence `prereg/T0.6-organismes-config-7b-v1.json`, que je n'avais pas comptée. Aucun contenu n'a été lu ni affiché. À consigner avec l'écart.
7. **Contre-lecture 11 inscrite par moi** dans la section « Contre-lecture », avec les deux empreintes ; à confirmer par la session qui orchestre, qui tient le registre.
8. **La vérification des corrections** revient au même contre-lecteur (allègement de la procédure, classe A).

## 8. Fichiers ouverts pour ce brouillon

- `docs/notes/relance-organismes-discrets-v1/contre-lecture-brouillon21-bras-a-v1.md`, en entier.
- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon21.md` : la ligne A17 ; les passages de 6.10 et de 6.12 qui parlent des tirages dégénérés ; 7.2 jusqu'à sa table ; 8.2 (une ligne) ; 8.3 ; 8.5 ; 8.6 ; les passages où paraît le mot « effectifs » ; et, par programme, le fichier entier pour les contrôles.
- `registres/go.md` de la branche principale distante, par `git show`, après la ligne 508.
- Par programme, pour leur seule empreinte : les 111 fichiers de la table d'en-tête hors des dossiers cloisonnés.
- Mes propres pièces du brouillon 21 et mes programmes de construction.
- Rien d'autre. Ni le journal, ni les modules du code, ni rien de ce que visent les interdits.
