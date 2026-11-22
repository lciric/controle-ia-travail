# Veille de cap — conception (Fable, v1)

- **Nature** : pièce de travail (classe C), écrite le 22 novembre 2026 par la session fille de conception (Claude Fable 5.2, `session_01XJ6MgqK7APqd1Hi98jL4GT`), sur la demande approfondie du directeur relayée par la mère (R-4925). Elle répond à la demande reformulée de `demande-reformulee-quatre-points-conception-fable-v1.md` (`bd6fdf1f…`), écrite et committée avant toute lecture (commit `c8bcafe5`).
- **Lu**, à ce commit : mandat v1 (`7874ce7e…`) ; `registres/decisions.md` (`1be620d4…`, lignes citées et comptages par motifs) ; `registres/go.md` (`3db30eb9…`) ; tête de `registres/etat.md` (`bf6bd9e6…`) ; passation `2026-11-22-0630.md` (`0409dd53…`) ; `docs/notes/etat-des-chantiers-2026-11-22-v2.md` (`2a5ae067…`, plan, verdict, contradictions) ; en-têtes de l'inventaire des courses anciennes (`b49dc246…`), de l'inventaire des décisions ouvertes (`5986c079…`), des mandats perdus (`57424307…`), de la mémoire des problèmes v3 (`5a0693e1…`), de la carte de la porte G0 (`85d6d454…`) ; manifeste de fin de la course des bassins étroits (`24c5d6ae…`) ; noms de fichiers et de branches.
- **Non lu** : tout ce que le mandat v1 interdit ; aucun résultat, aucun verdict, aucune sortie de collisionneur ni d'organisme ; aucune branche autre que `claude/veille-de-cap-v1` (qui ne porte encore que le mandat).
- **Statut des chiffres** : les comptages viennent de commandes sur les fichiers cités ; les seuils du § 6 sont des cibles de conception, non mesurées, à confirmer après une semaine de marche.

## Verdict

1. Le programme ne manque pas d'inventaires : il en a fait cinq en douze jours. Il lui manque ce qui suit leurs trouvailles dans le temps, et une règle qui sépare « l'essai a échoué » de « l'essai n'a pas pu juger ».
2. La veille proposée tient en trois objets (un registre des idées à états fermés, un grand livre des promesses, une liste de contrôle du faux échec), une boucle où chaque journée du programme est relue à 7, 14, 30 et 60 jours, et sa propre épreuve, faite hors d'elle.
3. Un signal vrai est sorti en l'écrivant : l'organisme sur les bassins étroits. Accord de 60 dollars, 0,28 dépensé, relance accordée par ton mot, jamais faite ; l'accord tombe le 30 novembre.

## 1. Ce que les traces montrent

**Le cas d'école.** Le 13 novembre, la première génération de l'atelier d'idées sur les bassins étroits part (R-2544) et se clôt en trois minutes « en défaut, sans fiche » : le relais refuse l'authentification (R-2545). La cause est établie le jour même, sans dépense (R-2549) ; le lanceur corrigé est jugé « non autorisable », il en faut un quatrième (R-2556) ; tu dis « une seule relance au total : go » (R-2558). Puis plus rien : aucun quatrième lanceur dans `scripts/`, un seul dossier de course, une seule ligne de dépense (0,275477 USD), aucun nom de branche distante n'y renvoie, plus un mot dans le registre des décisions après le 15 novembre, aucune passation n'en parle après celle du 13 à 17:32. L'accord GO-2026-11-13-03 (60 USD) court jusqu'au 30 novembre. Trois leçons. L'atelier n'a jamais jugé sa question, et rien ne l'a abandonné. La trace brute trompe : le manifeste de fin écrit « issue : fin propre » avec le code 2 ; seuls le code et l'absence de produit disent ce qui s'est passé. Et une photo ne suffit pas : l'inventaire du 18 novembre a bien vu la course (« close en défaut, aucune fiche », ligne 76 de son tableau), sans suite. Le tour du collisionneur sur la même question, lui, a servi (une de ses méthodes est devenue un préenregistrement, R-2878).

**Les mots perdus en route.** Le mandat v1 cite ta demande jusqu'à « ou abandonnées ». Le message de la mère qui m'ouvre la donne jusqu'à « car test mal lu comme un échec ». La proposition perdue à la copie est celle qui porte le faux échec.

**Le volume.** Le registre des décisions va jusqu'à R-4924 depuis le 4 octobre, et près de la moitié de ces lignes datent d'après le 13 novembre ; 360 accords de calcul ; 213 pièces de passation ; 755 branches distantes. Aucun lecteur ne relit cela à chaque cycle : il faut un calendrier, et des programmes pour le tri.

**Les photos sans suite.** Sorties non lues et idées de l'organisme (10 novembre, citées par l'inventaire du 18, non ouvertes ici) ; environ quatre-vingt-dix courses anciennes, dont deux tours « payés ≈ 32,6 USD et jamais ouverts » (18 novembre) ; deux mandats perdus (20 novembre) ; décisions ouvertes (21 novembre) ; état des chantiers, qui écrit « au repos, non relancés » pour cinq d'entre eux (22 novembre). Chaque photo vieillit à son tour ; aucune ne dit ce que ses trouvailles sont devenues.

**Le cap.** La règle en vigueur veut trois chantiers actifs au plus ; l'état des chantiers du 22 en numérote onze, dont certains au repos. Le compte exact des actifs est le premier travail du contrôle de dérive.

## 2. Le cerveau, pris au sérieux

| Fonction | Ce qu'elle fait | Instrument |
|---|---|---|
| Mémoire des épisodes | garde ce qui s'est passé, dans l'ordre | registres, passations : existent |
| Mémoire du sens | range par objet, non par date | registre des idées, à poser ; mémoire des problèmes : existe |
| Consolidation par rejeu | rejoue l'ancien entrelacé au neuf, à intervalles croissants | boucle des anniversaires, tranche tirée au sort |
| Mémoire des intentions | se souvenir de faire, sur un indice de date ou d'événement | grand livre des promesses, condition de réveil |
| Contrôle de la source | savoir d'où vient un souvenir ; pas de faux souvenir | citation mot pour mot, vérifiée par programme |
| Détection de l'écart | signale quand l'action quitte le but | contrôle de dérive |

Limite de l'image : le cerveau oublie par construction. Ici l'oubli doit être un acte.

## 3. Les trois objets

### 3.1 Le registre des idées

**Deux niveaux**, sinon il se noie. Un **gisement** est un lot de propositions brutes : un dossier de collisionneur, une course de l'organisme, une série de demandes à Fable, des notes de mentors. Il a une fiche, avec son compte et son état : dépouillé (synthèse écrite, idées retenues fichées) ou non. Une **idée** reçoit sa fiche quand elle est portée : dite par toi, retenue par une synthèse ou une décision, attachée à un accord, un devis, un préenregistrement ou une course, ou promise à l'essai. Le reste demeure joignable par son gisement.

**Une fiche** : nom en clair ; énoncé mot pour mot avec chemin, commit et repère ; porteur ; ce qu'elle sert (hypothèse, porte, chantier, ou « hors cap ») ; état ; essais rattachés avec leur issue ; prochaine action ; condition de réveil ; mots-clés.

**Dix états, liste fermée** : proposée ; retenue ; en préparation ; à l'essai ; essai non évaluable ; testée, non concluant ; testée, verdict valide ; intégrée au programme ; gardée de côté ; abandonnée. Plus « fusionnée dans » pour les doublons.

**Trois règles.** (1) « Gardée de côté » et « abandonnée » exigent une décision nommée, citée ; la première porte une condition de réveil, la seconde une raison codée (réfutée, occupée, trop chère, remplacée, hors cap, risque, mot du directeur). (2) « Verdict valide » exige que la liste du faux échec soit passée. (3) Une fiche sans mouvement ni décision depuis quatorze jours est **en souffrance** : ce n'est pas un état, c'est une alerte, et son âge se compte.

**La forme.** Un journal d'événements à ajouts seuls, une ligne par événement, lisible par programme ; une vue en clair, régénérée chaque jour sous un nom daté. Ce que la veille v1 aura déjà écrit entre tel quel, comme première capture.

**La décision par lot.** Des centaines de fiches ne recevront pas chacune ton mot. La page hebdomadaire propose des lots (« ces douze-là : gardées jusqu'après G0 »). Un mot pour un lot nommé est une décision nommée.

### 3.2 Le grand livre des promesses

Même journal, autre nature. Sources : la « prochaine action » et le « reste » de chaque passation contre le « fait » des suivantes ; chaque accord de calcul (consommé ? lu ? échu ?) ; les « à faire », « à écrire », « plus tard », « sur devis » des registres ; les préenregistrements scellés sans verdict ; tes « go » sur recommandation ; les trouvailles des inventaires. Chaque promesse porte son indice : une date ou un événement (« au retour du quota », « après G0 »). La veille est l'indice.

### 3.3 La liste de contrôle du faux échec

Pour tout essai dit en échec, nul, clos en défaut ou arrêté :

1. La course a-t-elle produit ce qu'elle devait mesurer ?
2. Le journal porte-t-il une faute d'instrument qui touche la mesure (authentification, quota, plafond de sortie, troncature, délai, machine perdue, refus de garde, bogue du lanceur) ?
3. L'effectif obtenu atteint-il l'effectif prévu ?
4. Un témoin positif est-il passé ?
5. Le critère gelé a-t-il été appliqué par un lecteur neuf ?
6. Le négatif porte-t-il sur l'idée, ou sur une mise en œuvre (dose, modèle, couche, tâche) ?

Quatre issues : **jamais parti** ; **non évaluable** (1 ou 2 en défaut) ; **non concluant** (3 ou 4) ; **verdict valide**, avec sa portée (6). Dans les deux premiers cas l'idée reste « non testée ». La symétrie R4 vaut : un succès trop propre passe la même liste.

La veille ne lit aucun résultat. Elle répond à 1, 2, 3 et 5 par les traces de procédure ; pour 4 et 6 elle cite le registre, ou écrit « à juger par un lecteur habilité ».

## 4. La boucle

- **Cycle du présent** (toutes les quatre heures si les registres ont bougé) : lire ce qui est neuf, ficher, coder les essais dits en échec, chercher pour chaque problème du jour une fiche ancienne qui y répond.
- **Cycle du passé** (une fois par jour) : le **calendrier des anniversaires**. Chaque journée du programme est reprise à 7, 14, 30 et 60 jours. À 7 jours, un sous-agent neuf, qui ne voit pas le registre, refait l'extraction sur les traces brutes : avec celle du jour même, cela donne deux captures indépendantes, donc une estimation des idées manquées, sans coût de plus. À 14, 30 et 60 jours, on reprend les fiches nées ce jour-là : état, âge, réveil échu, promesse échue, accord proche de sa fin. L'arriéré (4 octobre au 14 novembre) se rattrape par cinq journées par jour, les plus anciennes d'abord.
- **Cycle de la semaine** : carte de la dérive ; visite des fiches gardées et abandonnées ; une tranche ancienne tirée au sort, extraite à l'aveugle par un autre modèle ; mesures de la veille ; page pour toi. Une fois par mois, le « pré-mortem » : « nous sommes à la date de la porte et elle est manquée — pourquoi ? ».

## 5. Les contrôles et les signaux

Six signaux, pas plus : idée en souffrance ; essai mal lu ; promesse échue ; dérive ; réemploi ; gisement non dépouillé.

**La dérive se mesure sur trois repères** : la règle des trois chantiers actifs ; les huit critères de la porte G0 et les jours restants ; l'entretien du 1er décembre. Mesures : compte des chantiers actifs ; part des lignes de décision et de la dépense par chantier sur sept jours ; chantiers sans lien à une hypothèse, une porte ou un mot de toi ; critères et hypothèses sans travail en face. La veille montre la carte ; elle ne juge pas tes choix.

**L'attention est bornée.** Cinq signaux au plus par bulletin, classés par une grille déclarée : qui porte l'idée (ton mot d'abord), ce qu'elle sert, ce que coûte de trancher, son âge. Un signal au moins vient de la moitié ancienne. Chaque signal finit par une décision à prendre, et son sort est suivi.

## 6. L'épreuve de la veille, hors d'elle

1. **Cas marqués à clé scellée.** La mère note, dans une clé que la veille ne lit pas, de vrais reports, de vraies promesses et de vrais essais avortés, au moment où elle les voit. Rien de faux n'entre dans les registres. Rappel : part des cas retrouvés sous sept jours. Le cas des bassins étroits, cité ici, ne peut plus servir de cas caché.
2. **Banc planté** (R5) : une journée de registre fabriquée, avec idées plantées et leurres, et une journée saine ; la consigne d'extraction passe sur les deux avant d'être employée.
3. **Double extraction.** Avec n₁ et n₂ idées vues par chaque capture et m en commun, l'estimateur de Chapman donne N = (n₁+1)(n₂+1)/(m+1) − 1 ; les manquées sont N moins les vues. Deux lecteurs de la même famille partagent leurs angles morts : ce chiffre est un plancher.
4. **Contrôles par programme, sans modèle** : chaque citation retrouvée mot pour mot au chemin et au commit cités ; invariants du journal ; ajouts seuls ; cadence lue dans git.
5. **Épreuve à froid** : une session neuve, le dépôt seul, retrouve trois idées désignées et leur état en dix minutes chacune.
6. **L'issue** : idées rouvertes puis testées ou tranchées ; et **échappées**, c'est-à-dire enfouissements trouvés par une autre voie. Chaque échappée reçoit sa cause et son remède.

Les critères chiffrés sont au mandat v2 (§ 9). Le verdict hebdomadaire sur la veille (« marche », « dégradée », « à refaire ») est prononcé par la mère ou un agent neuf, jamais par la veille.

## 7. Ce qui la ferait échouer

| Risque | Parade |
|---|---|
| Elle se noie sous les fiches | deux niveaux ; idée fichée seulement si portée |
| Elle répète les registres | extraction à l'aveugle sur les traces brutes à sept jours |
| Elle crie sans cesse | cinq signaux ; justesse auditée |
| Elle meurt à un changement de compte | état tout entier dans git ; battement vérifié à la reprise |
| Ses signaux restent lettre morte | suite mesurée ; page hebdomadaire ; lots |
| Elle dit « jamais testé » à tort, faute d'accès | « inconnu pour cause de cloisonnement », à confirmer par la mère (R11) |
| Elle fuit entre partitions | registre remis à la mère seule ; aucun résultat, seuil ni mécanisme recopié |
| Elle se met à décider | elle signale et recommande, c'est tout |

## 8. Ce qui revient à la mère, et quatre décisions pour toi

**À la mère** : tenir la clé des cas marqués (dix cas en deux semaines suffisent pour commencer) ; juger chaque signal « fondé » ou non, d'un mot ; verser le dossier de la veille sur `main` à chaque passation ; vérifier le battement à la reprise ; prononcer le verdict de la semaine.

**D-1 — Le sort de l'organisme sur les bassins étroits, avant le 30 novembre.** Enjeu : un essai accordé, jamais jugé, s'éteint par l'échéance. Options : (a) relance sous l'accord existant, quatrième lanceur à écrire et contre-lire ; (b) gardé de côté par ton mot, réveil « après G0 », accord à redonner ; (c) abandon nommé. Dans tous les cas, la synthèse des méthodes (`docs/notes/collisionneur-bassins-etroits-v1/synthese-v1.md`, `5fd7e26f…` selon R-2541), déjà exploitée pour une méthode, est remise à la session qui travaille aujourd'hui sur l'exploration des idées (R-4923, R-4924) : c'est un réemploi. Recommandation : (b) plus le réemploi, confiance 0,6 — je ne connais pas l'état du chantier de l'organisme. Défaut : (b).

**D-2 — L'issue codée de tout essai dit en échec.** Enjeu : fermer la porte au faux échec à la source. Options : (a) règle pour toutes les sessions : la ligne qui dit l'échec porte l'un des quatre mots ; (b) la veille seule code après coup ; (c) rien. Recommandation : (a) avec (b) en filet, confiance 0,8. Défaut : (b).

**D-3 — Ton œil sur échantillon.** Trois fiches tirées au sort par semaine, cinq minutes : énoncé fidèle, état juste ? Options : (a) chaque semaine ; (b) chaque mois ; (c) la mère à ta place. Recommandation : (a), confiance 0,6. Défaut : (c).

**D-4 — Un lecteur d'une autre lignée pour l'audit à l'aveugle.** Enjeu : les angles morts communs aux modèles d'une même famille ; mais c'est une dépense, et des extraits du registre sortent vers un tiers. Options : (a) un autre modèle de la même famille, sans dépense ; (b) une fois avant G0, sur devis. Recommandation : (a), à revoir si le plancher des manquées reste haut ; confiance 0,7. Défaut : (a).

## 9. L'ordre de pose

1. **Tout de suite** : mandat v2 à la veille ; premier bulletin sur les cinq inventaires existants (que sont devenues leurs trouvailles ?) et sur les accords de calcul proches de leur fin.
2. **Sous trois jours** : journal, vue, calendrier ; programme de contrôle écrit par la veille, contre-lu par un autre modèle (pièce d'instrument) ; banc planté.
3. **Sous deux semaines** : arriéré clos ; première mesure du rappel ; premier verdict de la semaine ; première épreuve à froid au prochain changement de compte.

Rien de cela n'ajoute de contre-lecture aux pièces de travail ; une seule pièce d'instrument est créée.

## 10. Réserves

- Aucun seuil n'est mesuré ; la première semaine les confirmera ou les changera.
- Je n'ai lu ni les branches ni les sorties : le constat sur les bassins étroits tient à ce que montrent `main`, les registres et les noms de branches ; la mère le confirme avant de le porter.
- L'estimateur suppose des captures indépendantes ; elles ne le sont pas tout à fait.
- La veille juge la procédure, non le fond : elle ne lit aucun résultat.
- Concepteur et veille sont de la même famille de modèles ; le mandat v2 n'a pas été contre-lu (pièce de travail).
