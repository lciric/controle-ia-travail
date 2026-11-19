# Note de changements — brouillon 25 du texte neuf du bras A des organismes discrets — v1

**Rédigé par Claude Fable 5.2 (`claude-fable-5-2`)**, le même agent que pour les brouillons 21 à 24. Je conçois ; la session qui m'orchestre consigne, scelle au registre et committe.

- **Brouillon** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon25.md`, `ab5fc58ee69813288923cbd316848b0b25275659590e5f84e17e498b69d620da` (2 020 lignes). Les brouillons 20 à 24 ne sont pas modifiés : vérifiés avant la copie et après l'écriture.
- **Fiches pour Lazar : aucun fichier neuf.** Celles du brouillon 23 restent en vigueur (`decisions-bras-a-brouillon23-v1.md`, `f20abfed…`). Aucun point porté ici ne touche une règle de jugement.
- **Sources** : le relevé des défauts trouvés en écrivant la version 6 du code (`b1d3c0fa…`) ; mon avis sur ses points 1 à 3 (`24f4f9b3…`) ; la vérification des corrections de ce code (`4a6e1b41…`) ; la vérification du brouillon 24 (`31a698e3…`, verdict « engageable », trois remarques mineures). Les quatre lus en entier.
- **Méthode** : copie du brouillon 24 par `cp`, puis 33 remplacements exacts, chacun vérifié unique par programme.
- **Rien n'est arrivé de Lazar ni de la session principale sur le bras A** : registre des accords relu sur la branche principale distante au commit `eccb5e71` ; deux lignes de plus, GO-2026-11-19-77 et -78, sans rapport avec le bras A.
- **Heures (UTC, `date -u`)** : début 16:52:29Z le 2026-11-19 ; brouillon scellé à 16:58:21Z.
- **Interdits tenus** : aucune empreinte de fichier d'un dossier du côté habilité ; aucun interne de moniteur ; aucune fiche de l'organisme d'idéation ; aucune réponse de l'essai de mesure ; aucune clé ; aucun appel de modèle ; seul appel réseau, `git fetch` de la branche principale ; ni `registres/`, ni `.claude/`, ni le journal touchés ; rien committé ; aucun fichier existant écrasé ; suite d'essais non lancée ; aucun sous-agent.
- **À déclarer** : pour nommer au texte les fichiers que le code écrit, j'ai ouvert, pour la première fois, du code de la relance — les noms de fichiers et de champs seulement : `configuration_bras_a_v6.py`, lignes 56 à 86 ; `analyse_bras_a_v6.py`, lignes 1036 à 1058 et 1168 à 1200 ; et les lignes de la note du code qui nomment ces fichiers. Ce code n'est l'interne d'aucun moniteur.

## Contrôles par programme

| contrôle | résultat |
|---|---|
| **section 12 entière** | **identique, caractère pour caractère, à celle du brouillon 24** ; les points 17 à 21 sont donc ceux du brouillon 23, et les fiches parties restent mot pour mot celles du texte |
| 7.5 et ligne A17 | inchangées depuis le brouillon 24 |
| titres de section (53) | les 52 titres de niveau 2 et 3 sont identiques |
| consignes figées (blocs de 3.2 et 3.3) | égales octet pour octet à celles du brouillon 20 ; `98a9bd34d280fc7d9db07a733bc78557ff350538a3ace7a2926999ecf14c9248` et `ecf590eae0c06d413d173f7f03c5575e52d6034613e0a1a30d681149435a1816`, recalculées |
| citations à la lettre | brouillon 20 : 935 sur 935 retrouvées ; brouillon 24 : 1 121 sur 1 121 retrouvées |
| table d'en-tête, sans les fichiers cloisonnés | 139 lignes à empreinte : 125 recalculées et égales, 0 différente, 14 sautées et non ouvertes (les mêmes), qui gardent l'empreinte héritée, non vérifiée |
| marque des cases non remplies | huit lignes, toutes en 13.1 |
| validateur (`problemes()`) | deux problèmes, les mêmes, attendus : marque restante hors des sections exigées ; contre-lecture 10 sans ses deux empreintes |
| différence avec le brouillon 24 | 35 lignes de plus ; 26 lignes changées |

## 1. Ce qui est porté, point par point

| source | objet | ce que le texte dit maintenant | où |
|---|---|---|---|
| avis, point 1 ; vérification du code, C-1 | liste des refus | **déclarée fermée** : le programme ne refuse rien que le texte ne nomme | 6.9 ; 8.4 |
| idem | valeur p contre ses comptes | écart de structure à un demi-pas de la grille ou plus ; en deçà, prise telle quelle | 6.9 ; 8.4 |
| idem | lecture hors de sa place | désignée par ses champs ; clé et champ s'accordent ; l'ordre d'une liste ne compte pas | 6.9 ; 8.4 |
| idem | nombre impossible | aire, aire de pli, borne : de 0 à 1 ; valeur p : au-dessus de 0, au plus 1 | 6.9 ; 8.4 |
| idem | borne sans quantile | borne remplie : quantile rempli et juste ; borne `null` : quantile non lu | 6.9 ; 8.4 |
| idem | borne remplie au cas E | écart, sous les rédactions (a) et (b) du point 19 | 6.9 ; 8.4 |
| vérification du code, C-1 (ajout) | fichier des scores par unité | **liste fermée de ses refus** ; valeurs de `dose` et de `condition` nommées au texte (elles viennent du texte cité du développeur habilité, version 7) et lues dans la configuration ; `tache`, `episode`, `pas` non contrôlés | 6.9 ; 8.4 ; 13.1 |
| avis, point 2 ; vérification du code, C-2 | « une seule fois » | une livraison refaite est lue une fois ; **une ligne de GO n'ouvre qu'une livraison refaite**, liée par un acte de reprise ; dit expressément « ni un plafond ni une règle neuve » | conventions ; 6.9 ; 8.4 ; 13.2 |
| avis, point 3 | fichier de l'étape (m) après un arrêt à l'étape (n) | jamais supprimé ; le fichier d'arrêt cite son empreinte et son statut, une valeur par rédaction | conventions ; 6.9 ; 8.4 |
| relevé, points 4 à 6 | « nom du champ en défaut » | étendu aux dix champs du fichier des scores par unité, au préfixe `reglages.`, et à la désignation d'une liste entière | 6.9 |
| relevé, points 8, 10, 11 ; vérification du code, M-1, M-4 | fichiers sans nom | quatre fichiers nommés, avec leur rôle et leurs champs | conventions ; 13.2 |
| relevé, point 18 ; vérification du code, partie 6 | lecture d'un dossier | le fichier des scores par unité est rangé dans un dossier que rien ne parcourt | conventions ; 8.4 ; 13.2 |
| vérification du brouillon 24, M-1 | section 10 | « restent prononcés », « reste prononcée » | 10 |

## 2. Les quatre fichiers nommés

| fichier | champs, et eux seuls | qui l'écrit |
|---|---|---|
| `configuration-de-l-analyse-de-la-discretion-bras-a.json` | deux parties : `choix` (les cinq choix nommés, recopiés du texte scellé) ; `chaines_du_module` (ce que la case du module inscrit) | session de relance, après le scellement ; inscrite au registre avant la réception de la sortie de la lecture commune |
| `constats-de-l-etape-m-bras-a.json` | `etape`, `journal_de_la_table_a`, `lignes_de_la_table_a`, `renvoi_de_la_base`, `effectifs_de_la_base_conformes`, `sha256_de_la_livraison`, `sha256_de_la_configuration`, `sha256_du_fichier_de_l_etape_m` | instance d'analyse, à côté du fichier de l'étape (m) |
| `arret-de-la-lecture-de-la-discretion-bras-a-<seize signes>.json` | `evenement`, `constat`, `sha256_de_la_livraison`, `sha256_du_fichier_de_l_etape_m`, `statut_du_fichier_de_l_etape_m` | instance d'analyse, dans le dossier des arrêts |
| `reprise-de-la-lecture-de-la-discretion-bras-a-<seize signes>.json` | `evenement`, `ligne_de_go`, `sha256_de_la_livraison_refusee`, `sha256_de_la_livraison_refaite` | instance d'analyse, avant toute lecture de la livraison refaite |

Les deux premiers noms et leurs champs sont ceux du code de la version 6, à un près : la configuration n'avait pas de nom. Les deux derniers champs du fichier d'arrêt et tout l'acte de reprise sont de moi.

## 3. Ce que le code de la version 7 doit porter

Le rédacteur de la version 7 travaille sur mon avis et sur la vérification du code. Cette partie dit **ce que le texte fixe en plus ou autrement**. Chaque point dit s'il confirme l'avis, le précise, ou s'en écarte.

**A. Liste fermée (confirme l'avis).**
1. Le programme ne refuse une livraison que pour une cause écrite en 6.9. Un essai le dit : tout refus levé porte le nom d'une garde de 8.4.
2. **Valeur p contre ses comptes** : refus si l'écart à la formule atteint un demi-pas de la grille. Valeur p haute : écart ≥ 1 ÷ (2 × 2 001). Valeur p basse : écart ≥ 1 ÷ (2 × (1 + `n_permutations` − `permutations_degenerees`)). Joue aux cas A et D, et au cas E sous la rédaction (a) ; jamais au cas C, où les valeurs p ne sont pas lues. **La valeur rendue est prise telle quelle**, jamais remplacée par la formule. Essais : 0,3 avec zéro aire au moins égale, refusé ; une valeur arrondie à quatre décimales, acceptée.
3. **Lecture hors de sa place** : refus si une clé de rangement contredit le champ `moniteur` ou `dose` ; **aucun refus pour l'ordre** d'une liste (précise l'avis). Essai : vingt lectures complètes dans un autre ordre, acceptées.
4. **Nombre impossible** : aire, `pli0`, `pli1`, `borne_haute` de 0 à 1 ; valeurs p et valeur de la famille au-dessus de 0 et d'au plus 1 ; un texte, un booléen ou une valeur qui n'est pas finie est refusé.
5. **Quantile** : exigé seulement quand la borne est remplie ; non lu quand elle est `null`.
6. **Cas E, rédactions (a) et (b)** : borne remplie refusée.

**B. Fichier des scores par unité (s'écarte du code de la version 6).**
7. Les valeurs permises de `dose` et la valeur de `condition` pour l'honnête se lisent dans la configuration scellée — deux chaînes de plus dans `chaines_du_module` —, plus rien n'est écrit en dur. Leurs valeurs attendues sont celles du texte : `dose-0.25`, `dose-0.50`, `dose-0.75`, `dose-1.00` ; `honnete`.
8. **Retirer** les contrôles d'étendue de `episode` (0 à 7) et de `pas` (0 à 9) : le texte dit ces champs non contrôlés, et la liste est fermée. Garder : `pas` rempli pour l'agrégateur séquentiel, refusé.
9. La liste fermée des refus de ce fichier est en 6.9 ; l'aligner sur elle, ligne par ligne. `scores_par_unite.forme` n'est pas lu.

**C. Livraison refaite (précise l'avis).**
10. Une ligne de GO n'ouvre qu'une livraison refaite. **Aucun plafond** : ne pas refuser au motif que le dossier porte déjà plus d'un arrêt (c'est la première des deux corrections proposées par la vérification du code, C-2 ; le texte retient la seconde, une reprise par ligne).
11. Avant toute lecture de la livraison refaite, écrire et sceller l'acte de reprise (nom et quatre champs en partie 2). Une ligne que porte déjà un acte de reprise est refusée.
12. La ligne doit citer trois empreintes : fichier d'arrêt de la livraison refusée, module corrigé, rapport de sa contre-lecture. Elle doit dire l'accord. **Le texte ne fixe pas les mots de l'accord** : la phrase exigée par le code et la recherche des mots de refus restent au code (vérification du code, M-3) ; le texte demande seulement que le registre lu soit celui de la branche principale.
13. Le rapport compte les livraisons refusées et lues, et cite les lignes.

**D. Fichier d'arrêt (s'écarte du code de la version 6).**
14. Cinq champs et eux seuls, toujours présents : aux trois du code s'ajoutent `sha256_du_fichier_de_l_etape_m` et `statut_du_fichier_de_l_etape_m`, tous deux `null` pour un arrêt à l'étape (m).
15. Pour un arrêt à l'étape (n), le statut est l'une de trois valeurs, selon le choix de l'issue : « rapporté tel quel, non opposable » ; « non opposable : discrétion non lue » ; « inchangé, opposable ». Sous la deuxième, le rapport reprend le contenu du fichier de l'étape (m) sous cette marque, et aucune ligne de la table C n'est un verdict.
16. Le fichier de l'étape (m) n'est jamais supprimé, réécrit ni déplacé.
17. L'enchaînement ne tire de l'exception que son constat.

**E. Autres fichiers (confirme le code, à deux ajouts près).**
18. Configuration scellée : le nom est fixé (partie 2). Ses deux parties sont celles du code. Les cinq choix recopient le texte scellé.
19. Constats de l'étape (m) : nom et huit champs du code. **Sa lecture rejoue ce qu'il affirme** (vérification du code, M-1) : lignes de la table A relues du journal ; trois empreintes comparées.
20. Définition unique : le « champ » peut être l'un des dix champs du fichier des scores par unité ; une clé de `reglages` porte son préfixe ; pour une liste entière, la désignation de la liste et la nature du défaut (un champ de plus, de moins, en double ; pièce illisible). Le texte donne quatre natures et six listes possibles ; si le code a d'autres désignations, me le dire.

**F. Dossier.**
21. Le fichier des scores par unité est rangé dans un dossier que rien ne parcourt. La garde statique garde son signalement ; le texte porte maintenant la règle.

## 4. Ce qui n'est pas porté, et pourquoi

| point | pourquoi |
|---|---|
| relevé, point 7 — fichier absent, non scellé, ou qui n'est pas la bonne pièce | je n'ai pas voulu dire à la hâte ce que vaut une pièce qui ne répond pas à son empreinte ; le code garde sa garde ordinaire ; à reprendre |
| relevé, point 9 — nom de la pièce qui porte la sortie de la lecture commune | elle vient du côté habilité : à nommer par la session principale |
| relevé, point 12 — phrases d'accord d'une ligne de GO | partie 3, point 12 : le texte ne fixe pas les mots |
| relevé, points 13 à 16 — chaînes et formes du module | attendent la liste du développeur habilité |
| relevé, point 17 — une clé de graine rejouée pour plusieurs intervalles | touche des nombres rapportés, non un verdict ; à écrire en 6.2 à un prochain brouillon, après lecture de cette section, que je n'ai pas lue |
| relevé, point 19 ; vérification du code, C-3 — chemins exclus de la garde statique | code, et liste à confirmer par la session principale |
| vérification du code, M-2, M-3, M-5, M-6, M-8 | code |
| vérification du code, M-7 — `effectifs`, `exclues`, aires de l'agrégateur rendus tels quels | le texte dit déjà « rapportés tels qu'ils sont rendus » pour les deux premiers ; je n'ai pas tranché s'il faut les rapporter par leur seule empreinte |

## 5. À dire à Lazar avec les réponses en attente (vérification du brouillon 24)

Ces deux remarques ne changent pas le texte ; elles accompagnent les fiches.

1. **Fiche 11, option (b), avec la fiche 12, options (b) ou (c).** Une livraison refaite exige que le lecteur habilité atteste qu'aucun calcul de moniteur ne change. Or corriger un moniteur appris non ajustable change ce calcul. Sous ce couple d'options, cette anomalie ne peut donc jamais être reprise : la discrétion reste « non lue ». C'est un argument de plus pour l'option (c) de la fiche 11.
2. **La reprise est accordée au cas par cas.** Ce que rend le programme qui refuse informe un peu sur le résultat. Lazar peut préférer fixer d'avance la règle : « reprise accordée dès que les conditions sont remplies, quel que soit le défaut nommé ». Le texte ne l'écrit pas ; ce serait une règle de plus, à poser avec sa réponse au point 21.

## 6. Demandes à la session principale, en plus des précédentes

13. La forme sous laquelle le module rend ses valeurs p (décimales, arrondi).
14. Si `lectures` est une liste ou une table à clés de dose et de moniteur.
15. La confirmation des valeurs de `dose` et de `condition` dans le fichier des scores par unité, et de ce que portent `scores_par_unite.lignes`, `.champs` et `.forme`.
16. Le chemin de tout programme du côté habilité qui nomme ce fichier, et le dossier où il est rangé.
17. La liste des chemins que la garde statique doit élaguer avant tout parcours (vérification du code, C-3).

## 7. Réserves

1. **Le demi-pas de la grille** est un choix de conception. Il suppose que le module rend ses valeurs p à quatre décimales au moins ; l'épreuve de forme doit le dire avant toute dépense.
2. **L'acte de reprise et les deux champs de plus du fichier d'arrêt** sont de moi. Le rédacteur de la version 7 a pu faire autrement sur mon avis, qui ne les nommait pas : à réconcilier, le texte faisant foi.
3. **Sous la rédaction (b), le contenu du fichier de l'étape (m) est rapporté tel quel sous la marque « non opposable : discrétion non lue ».** C'est ma lecture de « retirée » dans la fiche 12, alignée sur 7.5 et la ligne A17. Si Lazar ou la session qui orchestre préfère que ce contenu ne soit pas rapporté, c'est une autre forme de rapport ; l'issue ne change pas.
4. **Les formes de `dose` et de `condition` du fichier des scores par unité** viennent du texte du développeur habilité pour la version 7, et ses réponses sur la version 8 disent ces champs inchangés. Je n'ai pas d'autre preuve que la version 8 les écrit ainsi.
5. **J'ai ouvert du code de la relance** pour ses noms de fichiers et de champs (déclaré en tête). Je n'en ai pas lu la logique.
6. **Je n'ai toujours pas relu le texte en entier.** De plus qu'au brouillon 24 : la case « lignes de GO » de 13.2.
7. **Le texte s'allonge** (2 020 lignes). Les rédactions ouvertes y sont pour beaucoup ; elles tombent au scellement.

## 8. Fichiers ouverts pour ce brouillon

- `docs/notes/relance-organismes-discrets-v1/verification-corrections-code-v6-bras-a-v1.md`, en entier.
- `docs/notes/relance-organismes-discrets-v1/verification-corrections-brouillon24-bras-a-v1.md`, en entier.
- `docs/notes/relance-organismes-discrets-v1/defauts-du-texte-trouves-en-codant-v6.md`, en entier (au mandat précédent).
- `docs/notes/relance-organismes-discrets-v1/code-v6-bras-a-note-v1.md` : les lignes qui nomment des fichiers (recherche), et les lignes 77 et 108 à 120.
- `src/controle_ia/organismes_discrets/configuration_bras_a_v6.py`, lignes 56 à 86 et liste des noms ; `src/controle_ia/organismes_discrets/analyse_bras_a_v6.py`, lignes 1036 à 1058 et 1168 à 1200, et les lignes qui nomment un fichier (recherche, aussi dans `arrets_bras_a_v6.py` et `verdicts_bras_a_v6.py`).
- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon24.md` : mes passages de 6.9, des conventions, de 8.4 et de 13.2 ; et, par programme, le fichier entier pour les contrôles.
- `registres/go.md` de la branche principale distante, par `git show`, après la ligne 509.
- Par programme, pour leur seule empreinte : les 125 fichiers de la table d'en-tête hors des dossiers cloisonnés.
- Rien d'autre.
