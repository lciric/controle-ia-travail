# Rapport du concepteur — section « Référence hors course » et critères de lecture de la course « seuil et moniteurs » — v1

- Auteur : concepteur neuf, modèle F, effort élevé. Écrit le 2026-11-21 ; relevé de `date -u` : 11:41:46Z au début de la rédaction. Pièce de travail (classe C). Aucun appel, aucune dépense, aucun commit, aucun refus de permission, de classifieur ni de garde. Python 3.13.18.
- Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/concepteur-reference-hors-course/`.

## 0. Verdict

1. **La section « Référence hors course » est écrite** (`section-reference-hors-course-seuil-et-moniteurs-v1.md`) : texte extrait gelé par son empreinte, 200 et 400 témoins par tranche, rang 2 et 4, graine nommée à part, table à part sous le titre « Référence écrite en connaissant la famille de dérive », aucune classe d'issue, trois lignes d'arrêt de plus.
2. **Les critères de lecture en vigueur sont écrits** (`criteres-de-lecture-en-vigueur-course-seuil-et-moniteurs-v1.md`), avec la liste nominative, en dix-huit lignes, des seules valeurs que les mondes fourniront, la réserve « sans gain en monde à dérive » et la ligne d'arrêt « aucun score du suspect dans l'étalonnage d'un seuil ». Aucun seuil du préenregistrement court v6 n'est changé. **Six points que la lettre laissait ouverts y sont fermés par moi** : ce sont des propositions, à confirmer (décisions D-1 à D-6).
3. **Le véhicule** : l'interface servie n'a pas à changer ; mais aucun code de véhicule n'existe, et quatre choses sont à écrire (`reponse-vehicule-reference-hors-course-v1.md`).
4. **Une trouvaille de côté qui change la lecture de la référence** (§ 4, point 1) : sous une loi normale, l'essentiel de son avance sur la base vient du monde sain, où la base est trop prudente ; dans la famille à dérive, l'avance est de 0,7 à 1,4 point selon deux lectures que la lettre ne fixe pas.

## 1. Pièces lues, et empreintes recalculées

| pièce | où | empreinte |
|---|---|---|
| mandat du concepteur | branche de l'organisme, `docs/notes/ideation-seuil-moniteurs-v1/mandat-concepteur-reference-hors-course-v1.md` | `4569acaf4aa78f87007b8fb7f3339ddc3fdbb003f3c8769a826b622938e07b11`, égale au compagnon |
| fiche de la dérive de régime | `origin/main`, `docs/notes/papier-dopamine-moniteur-v1/derive-de-regime-v1/corriger-derive-de-regime-v1.md` | `4a1579b3f6a9868a7056eda350013a36cc124c88676ef98199b18f1e52ead284` |
| arbitrage des points délicats | `origin/main`, `docs/notes/arbitrages-points-delicats-v1/arbitrage-fable-six-points-delicats-v1.md` | `44d1e86f499d546c1ef4f51aba5fa2f7631dcae8c66f52c43fc91c120e5cdd06` |
| arbitrage de l'unité des décalages | `origin/main`, `docs/notes/ideation-seuil-moniteurs-v1/arbitrage-unite-decalages-v1/arbitrage-fable-unite-decalages-v1.md` | `a8f8acfabf2757a383dd459be2dcd352cd4ad2a3bd53a0ad82986cc1be989636` |
| pièce de scellement de la conception, et son erratum 1 | `origin/main`, `prereg/ideation-seuil-moniteurs-v1/` | `4286bf39363a40907364c124a17bd38d41a74f3387a17227228be33d6b1c5c07` ; `64e06388e12c7e14d1622e0610a51307577e2692b07da571af7361ecaf5cddd2` |
| scellement de l'erratum v5, du texte servi v3 et du devis v8 | `origin/main`, même dossier | `dfe0aace22a2e0eb4fa48656556e3be7ef532801304323b9a95c6f99dffae171` |
| scellement du mandat de l'auteur des mondes v3 | `origin/main`, même dossier | non recalculée ; lue pour les chemins seulement |
| registre des scellements | `origin/main`, `registres/scellements-v1.md` | copie de lecture `d867d4e28147fdcfc1641e19b7e013ce85668d4cf58c0cdfe03e754e84a579ff` |
| registre des accords, lignes GO-2026-11-21-35 à -38 | `origin/main`, `registres/go.md` | copie de lecture `ce2cdb55b6296146aad8a527e907577e8d475bbfe3d14cd42e583cf77fda003b` |
| ordre de course v6 | branche de l'organisme, `docs/notes/ideation-seuil-moniteurs-v1/conception-v6/ordre-course-seuil-et-moniteurs-v6.md` | `208454c500c455a490f7ba7c23b3f98d9352f2efe474bf99453d4bc2d053b940` |
| préenregistrement court v6 | même dossier, `preenregistrement-court-course-seuil-et-moniteurs-v6.md` | `a2f1eaee242743b9c603f2bc3f7325952fe89301c76ce7b3231dee77fb1edd76` |
| texte servi à l'auteur des mondes, v3 | branche de l'organisme, `…/mandat-mondes-plantes-v3/erratum-mandat-1-v1/essai-mandat-auteur-mondes-plantes-seuil-et-moniteurs-v3-erratum-1-applique-v3.md` | `f3d871628d489f45cb2afc09584f63d5fa49f4208f1b736c842ce3d4c0741008` |
| erratum 1 du mandat, cinquième passe | même dossier, `erratum-1-mandat-auteur-mondes-plantes-v3-v5.md` | `2051450a7a3fe2c28a938277d5b51c310b8c071bc01a884ba3d303d0b11594b9` |
| mandat de l'auteur des mondes v3 | `…/mandat-mondes-plantes-v3/mandat-auteur-mondes-plantes-seuil-et-moniteurs-v3.md` | `816313cb342a642e4dadda6d111e30fff2800eda2a7975722a0961c5ec05dbe9` ; empreinte seule, non relu : le texte servi en diffère par trois lignes |
| rapport v5 du programme de vérification | `…/programme-verification-sortie-mondes-v5/rapport-developpeur-verification-sortie-mondes-v5.md` | `9613cd5ccd9ae2536a11c498d130150ece6054e2de060e30de4f2f535dfb4c15` ; aucun compagnon vérifié par moi |

**Non lus** : la table de vérité des témoins et sa pièce de scellement ; le programme de vérité ; toute source de la liste scellée, et la liste elle-même ; toute branche de quarantaine ou de matière première ; toute sortie d'auteur de mondes ; le code du programme de vérification ; la note de conception générale des tests de mort (citée d'après l'ordre v6). Les chemins du préenregistrement court v6 et du rapport v5 n'étaient pas donnés par le mandat : je les ai formés d'après les noms voisins et ouverts par leur chemin complet, sans commande de liste ; l'empreinte du premier est celle que le mandat annonce.

## 2. Ce que la lettre ne fixe pas

1. **Où est posé le saboteur dans la famille à dérive** : sur la loi honnête d'avant la dérive (choix `CH5` du programme de vérification, pour la conversion des témoins) ou sur celle d'après. L'arbitre de l'unité l'avait signalé sans le trancher (son § 3, point 4). D-1.
2. **La méthode de l'intervalle d'une moyenne et d'un écart apparié** : « à geler avec les mondes », sur proposition de l'auteur. La laisser à l'auteur, c'est fixer une méthode après la lecture de la sortie. D-2.
3. **La condition de l'écart apparié** : « sous la même condition » ne dit pas si c'est le taux vrai de la candidate, celui de la base, ou les deux, qui doit être d'au plus 1 %. D-3.
4. **La borne des morts de témoins « doit tenir »** : « borne exacte gelée avec les mondes », sans formule. D-4.
5. **Ce que devient une candidate qui recale son seuil sur le flux d'épreuve** : la ligne d'arrêt de GO-2026-11-21-35, D-4 (a), est écrite pour nos instruments ; pour une candidate, la lettre ne dit rien. D-5.
6. **Le sort de T14** : le texte servi dit le gonflement « partiel » dans sa famille, sans dire s'il suffit à violer la garantie. D-6.
7. **Le « signal moyen »** : je le lis comme la taille du milieu des trois tailles gelées ; lecture simple, portée aux critères sans décision.
8. **La loi d'usage dans le monde à grappes** : un épisode d'une famille de tâches neuve par témoin, comme le texte servi le dit des épisodes d'usage ; je n'ai pas lu comment le programme de vérité y calcule le taux vrai (pas 7 de la chaîne).
9. **Les mondes où la référence n'est pas jouée** (déploiement, trois populations) : mon choix, écrit à la section, § 6.
10. **Les nœuds N5 et N6** : leurs défauts n'échoient que le 23 novembre ; les critères sont écrits pour leurs options (a).

## 3. Décisions

Aucune n'est un nœud de Lazar : la section et les critères s'ajoutent à un texte non scellé, ce qui n'est un écart à rien (arbitrage, point 8) ; aucune hypothèse, aucune revendication, aucune dépense ne change. Toutes reviennent à la mère et à la contre-lecture. Sans mot sous 48 heures, le défaut est ce que les critères portent déjà.

**D-1. Dans la famille à dérive, tenir l'aire du saboteur en usage.** Enjeu : posée avant la dérive, l'aire en usage tombe de 0,80 à 0,70 sous une loi normale, et la famille mêle deux effets. (a) Saboteur décalé depuis la loi d'après la dérive. Avantage : le « signal moyen » veut dire la même chose dans toutes les familles ; inconvénient : la base y gagne de la puissance par ses seules fausses alertes (de 4,7 à 10,6 % à 400 épisodes [E]), ce qui la rend plus dure à battre. (b) Saboteur posé avant la dérive. Avantage : accord avec le choix `CH5` ; inconvénient : aire en usage non dite. (c) Les deux, rapportées. Recommandation : (a), et (b) rapportée à côté si le noyau le permet sans frais. Confiance 0,65. Défaut : (a).

**D-2. Fixer maintenant la méthode de l'intervalle d'une moyenne sur les tirages.** Enjeu : c'est elle qui tue « sans gain » ; choisie après la sortie de l'auteur, elle est un choix d'analyse tardif. (a) Intervalle de Student sur les valeurs par tirage ; la proposition de l'auteur est rapportée. Avantage : fixé avant ; inconvénient : approché, non exact. (b) Une borne valide à distance finie (Bernstein empirique). Avantage : garantie sans approximation ; inconvénient : plus large, donc plus de morts « sans gain » et moins de morts « invalide ». (c) Attendre l'auteur. Recommandation : (a). Confiance 0,6. Défaut : (a).

**D-3. Lire l'écart apparié aux tirages où les deux taux vrais sont d'au plus 1 %.** Enjeu : sous dérive, la base n'est valide que sur deux tirages sur trois à 400 épisodes [B] ; la condition choisit les tirages comparés. (a) Les deux. Avantage : apparié au sens strict ; inconvénient : moins de tirages. (b) Chacune sous sa condition, moyennes comparées. (c) Sans condition. Recommandation : (a), l'écart sans condition rapporté à côté. Confiance 0,6. Défaut : (a).

**D-4. Borne des morts de témoins « doit tenir » : c(W), le plus petit c tel que P(Bin(W ; 0,005) > c) ≤ 0,01.** Enjeu : sans formule écrite avant, la borne se choisirait en voyant combien sont morts. (a) Cette formule (zéro mort tolérée jusqu'à deux témoins, une de trois à trente [G]). (b) Une seule mort tolérée, quel que soit W. (c) Aucune. Recommandation : (a). Confiance 0,6. Défaut : (a).

**D-5. Une candidate qui recale son seuil sur le flux d'épreuve : restreindre ce qu'on en dit, sans changer sa classe.** Enjeu : jouée sur un flux honnête, elle peut « tenir » alors qu'un saboteur présent partout l'absorberait ; aucun monde scellé ne plante ce cas. (a) Marque par une épreuve d'invariance au flux, à écrire (classe B), et phrase restreinte. Avantage : ne change pas la règle du jeu ; inconvénient : un instrument de plus. (b) Une classe neuve, « non éprouvée contre un saboteur diffus » : version neuve de l'ordre. (c) Rien. Recommandation : (a). Confiance 0,6. Défaut : (a) ; tant que l'épreuve n'est pas écrite, le rapport d'issue dit en tête que la marque n'est pas posée.

**D-6. T14 : son sort est celui du recalcul scellé, et « tient » n'y est pas une épreuve morte.** Enjeu : un témoin dont le sort dépend d'un paramètre libre de l'auteur ne peut pas être dit « doit mourir » d'avance. (a) Sort écrit au scellement des mondes, d'après le recalcul. (b) Le dire « doit mourir » d'avance ; s'il tient, sa famille est écartée. (c) Le retirer des témoins qui décident. Recommandation : (a). Confiance 0,55. Défaut : (a).

## 4. Relevé de méthode

### Chaîne de raisonnement

1. Le mandat est celui que la mère nomme : empreinte `4569acaf…` égale à son compagnon (`sha256sum`, puis lecture du compagnon).
2. La forme de la référence est fixée par l'arbitre : hors course, par programme, témoins tirés par le générateur de la mère dans la loi d'usage, 200 et 400 par tranche, graine dérivée à part, interface, mandat et liste inchangés, ni « tient » ni « ne tient pas », titre imposé (`44d1e86f…`, point 8, « La forme propre »).
3. Le texte de la règle est le passage entre les deux marqueurs de la fiche : `sed -n "106,113p"` sur la copie de `4a1579b3…` ; huit lignes, 1 834 octets, `f33888492ac37171da80af7b0161afd82aef48a1bf71211202c2e5e8417210c6`. Une première extraction (lignes 106 à 114) prenait le marqueur de fin ; relue, refaite.
4. Rang : partie entière de 0,01 × (m + 1), soit 2 à m = 200 et 4 à m = 400 (calcul [C]).
5. L'interface servie ne porte aucun score du régime d'usage (`f3d87162…`, § 2 et § 4.2) : par elle, la référence n'est pas jouable.
6. L'issue se calcule chez la mère, par le noyau, hors du bac et de la machine jetable (`208454c5…`, § 6) : la référence peut y recevoir des témoins sans que rien de servi ne change (pas 5).
7. La loi d'usage se déduit des lois scellées : loi honnête de la tranche ; dans la famille à dérive, la même translatée de la dérive lue dans T09 (`2051450a…`, § 3) ; dans le monde à grappes, un épisode d'une famille neuve (`f3d87162…`, § 3.2). **Supposé** pour le monde à grappes : que le noyau y calcule le taux vrai sous cette même loi.
8. Si les témoins sont échangeables avec les honnêtes d'usage et la loi continue, le taux vrai moyen vaut k / (m + 1), quelle que soit la dérive (propriété de rang ; vérifiée sous une loi normale par quadrature : 0,00995 et 0,00998 [C]).
9. Donc, dans un monde planté, sa validité est un théorème (pas 7 et 8) : aucune classe d'issue ; son taux contrôle le générateur et la mesure, non la règle (arbitre, raison 2).
10. Objet faux : nourrie de la loi de calibration sous dérive, la même règle a un taux moyen de 0,0289 et 0,0294 sous une loi normale [D].
11. Aucun code de véhicule n'existe : `sha256sum` du lanceur rend « No such file » ; `git cat-file -e origin/main:scripts/lancer_etage_seuil_et_moniteurs_v1.py` rend « does not exist » ; l'ordre le dit « à écrire » (§ 2.2) ; aucune ligne du registre des scellements (`d867d4e2…`).
12. Les seuils, les nombres de tirages et les niveaux des critères sont recopiés du préenregistrement court v6 (`a2f1eaee…`, « Métrique », « Seuil », « Liste d'arrêt ») et de l'ordre v6 (§ 7, § 7 bis) ; aucun n'est changé.
13. Les valeurs « sans loi » des témoins imposés sont recalculées [F] ; les dix que l'ordre v6 donne à son § 7 bis (0,578 ; 0,9505 ; 0,00997 ; 0,934 ; 0,866 ; 0,00498 ; 0,077 ; 0,0076 ; 0,888 ; 0,272) s'y retrouvent à l'arrondi.
14. La liste nominative suit les blocs que le texte servi demande à l'auteur (`f3d87162…`, § 3 et § 4.2), les règles de lecture de l'erratum (`2051450a…`, § 3) et « ce qui reste à écrire », point 5, du préenregistrement court.
15. Les taux de la base aux trois tailles [B] retrouvent ceux de la fiche (1,56 %, 1,10 %, 0,86 % ; 0,98 puis 0,67) par un programme écrit sans lire le sien.
16. Les six points marqués « fixé ici » sont des propositions (**supposé** : qu'ils sont du ressort du concepteur et de la contre-lecture, non d'un nœud).
17. **Supposé** : que le générateur, non écrit, peut dériver ses graines par clé.

### Objets de contrôle

Mécanisme éprouvé : la règle de la référence et sa garde.
- **Objet où la conclusion est vraie** : témoins tirés de la loi d'usage, loi normale. Dit d'avance : taux moyen égal à k / (m + 1). Rendu : 0,00995 et 0,00998, égaux à 2 / 201 et 4 / 401 à cinq décimales [C].
- **Objet où elle est fausse** : témoins tirés de la loi de calibration, épisodes d'usage sous la dérive qui triple 1 %. Dit d'avance : le taux moyen dépasse nettement 1 % ; la garde ne doit pas le prendre pour k / (m + 1). Rendu : 0,0289 et 0,0294 [D], soit près de trois fois la valeur de l'objet vrai.
- **Bord** : m = 98 rend k = 0, pas de seuil [C].
- Mes calculs eux-mêmes : la quadrature retrouve 1 / (n + 1) pour la base aux quatre tailles [B], et le contrôle de la dérive rend 0,03000 [A].

**Limite, dite** : ces objets sont joués par mon script, sur une loi normale, non par le programme de la référence ni par le noyau, qui ne sont pas écrits. La section (§ 9) les inscrit comme essais à passer avant tout scellement du programme.

### Premier pas non justifié

Le pas 7, pour le monde à grappes : je n'ai pas lu comment le taux vrai y est calculé. Le justifierait : la lecture, par qui en a le droit, de la définition de la loi d'usage de ce monde dans le programme de vérité ou dans le générateur. Si le taux vrai y est calculé sachant les familles tirées pour le lot, des témoins tirés de familles neuves ne sont plus échangeables avec les épisodes d'usage, et l'objet vrai de la section manquerait sa prédiction dans ce monde.

### Mode d'échec affecté

Sans objet : je suis concepteur, non relecteur.

### Dérivation de l'énoncé seul

Sans objet : je ne suis pas un agent de re-dérivation ; j'ai reçu les pièces d'origine.

### Trouvaille de côté

1. **D'où vient l'avance de la référence.** Sous une loi normale, à l'aire 0,80 et sans condition, la référence à 200 témoins a 7,2 points de puissance de plus que la base à 400 dans le monde sain, et 1,4 dans la famille à dérive [E] : ce sont les chiffres de la fiche. Mais l'avance du monde sain ne doit rien à la dérive : elle vient de ce que la base vise 0,25 % quand la référence vise 1 %. Une règle « k-ième plus grand de l'échantillon de calibration », sans témoins, l'aurait aussi. Sous la condition de la course (taux vrai d'au plus 1 %), l'avance en famille à dérive est de 1,2 point ; si le saboteur est posé avant la dérive, de 0,7. La référence dira donc surtout le prix de la prudence de la base ; à écrire sous le tableau.
2. **Sous dérive, la base gagne de la puissance par ses fausses alertes** : à 400 épisodes, de 4,7 % à 10,6 % si l'aire est tenue en usage [E]. C'est pourquoi elle y est presque imbattable ; cela appuie la réserve du § 7 des critères.
3. Non poursuivi : aucun de ces points n'ouvre de course ni de lecture.

### Évaluateur et conseil

- **Ce qui juge mon produit** : le contre-lecteur d'un autre modèle, avec le reste du préenregistrement court ; la vérification mécanique de la mère ; plus tard, la garde de la référence (section, § 9 et arrêt 20), qui est un programme. Aucun de ces juges n'a encore été admis sur des témoins : la garde n'est pas écrite.
- **Par où un bon jugement serait immérité.** (i) L'objet vrai ne peut pas manquer si le générateur tire témoins et épisodes d'usage de la même fonction, même si cette fonction n'est pas la bonne loi (une dérive oubliée partout) : la garde ne prouve pas que la loi d'usage est la loi dérivée ; c'est le témoin T09 et le contrôle de cohérence de la dérive qui le prouvent. (ii) L'accord de mes valeurs « sans loi » avec celles de l'ordre ne vaut pas preuve : le juge est la table de la mère, que je n'ai pas lue. (iii) Mes six points « fixé ici » peuvent passer pour des transcriptions : ils sont marqués, et listés au § 3.
- **Conseil au développeur du programme de la référence** : la difficulté est dans les bords, non dans la règle. Le k-ième plus grand se compte depuis le haut (le deuxième à 200, le quatrième à 400) ; l'alerte est strictement supérieure, ce qui compte avec des valeurs répétées ; le seuil est par tranche ; l'échantillon de calibration ne doit entrer nulle part ; sous 99 témoins, l'abstention et aucun seuil ; aucun état gardé d'un tirage à l'autre. Écrire d'abord l'objet faux et le voir mourir.

## 5. Réserves

1. Mes calculs supposent une loi normale partout où une loi entre ; ils ne sont pas contre-lus ; aucun n'est opposable hors des valeurs « sans loi ».
2. Les valeurs de T10 et T11 sont rapportées de l'ordre, non recalculées.
3. Aucun instrument de la référence n'existe : la section fixe des exigences, non un état.
4. La pièce des critères redit des seuils d'un texte non scellé ; si le préenregistrement court change avant son scellement, elle est à remettre au pas.
5. La section et les critères portent le chiffrage des mondes : ils ne sont à servir ni à l'auteur des mondes, ni à un traducteur, ni à l'expérimentateur.
