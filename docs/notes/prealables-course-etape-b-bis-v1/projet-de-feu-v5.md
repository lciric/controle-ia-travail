PROJET DE FEU ÉCRIT DE LA SESSION MÈRE — version 5
Course de l'étape B bis de l'épreuve des sondes entraînées sur la tâche (T0.7)

**projet, non en vigueur ; accords de Lazar sur les clés et sur le plafond au lanceur cités (champs 1 et 2) ; champ 3 (relevé de crédit et recharge de Lazar) ouvert jusqu'au moment du feu**

Rédigé le 2026-11-18, de 07:01:23Z (premier relevé `date -u` ; la lecture des pièces avait commencé quelques minutes plus tôt) à 07:35:52Z (`date -u`, relevé à la fin de la rédaction), par un sous-agent de la session mère, qui n'a écrit ni le texte scellé, ni ses trois addenda, ni la chaîne de lancement, ni les projets de feu versions 3 et 4, ni leurs contre-lectures, ni l'arbitrage, ni les mesures. Il remplace le projet version 4 (`projet-de-feu-v4.md`, `92b1502b95390c0f65a69712b791b6fad30992bdc8532213e976ba066ab8896b`, gardé intact, R12), jugé « à corriger » par sa contre-lecture (`contre-lecture-projet-de-feu-v4.md`, `98bedba8ec9bd0505b9b160e4068b6ba66f14f31c90c1e262a35c18e67c1264d`), et qui n'a jamais été versé ni mis en vigueur. Une fois en vigueur, il remplace aussi, pour la suite, le feu du 2026-11-17T11:13:33Z (`registres/t07-etape-b-bis/feu-bbis-v2.txt`, `33912cbe418f25c25ea3108572fa9cc07ee1b6bbecc236b9b934ff43cb21760b`), qui reste archivé sans modification. Les noms `feu-bbis-v3.txt` et `feu-bbis-v4.txt` n'ont jamais servi et ne servent pas : la mère verse ce feu sous `registres/t07-etape-b-bis/feu-bbis-v5.txt` (R12 : son texte n'est pas celui de la version 4).

Sources qui fondent ce texte : celles de la version 4 (décisions R-3188 et R-3191 ; arbitrage des quatre contre-lectures de la chaîne version 6, `arbitrage-contre-lecture-amorce-v6-v1.md`, `688abea5965a872b646148538f979be9dfd90d687c8eb73185eb092bcac150e3` ; troisième addendum scellé, `e5604cbdce509958e1f3e3bc3a36c8d17a78c8900b5f93a2102fff9b51d07872` ; projet version 3 et sa contre-lecture, `1d60a69bae14ecb8a70bfe55df31f66bd706c46adb2ebc6098e229480ae08e96` ; répétition de la mesure du plancher, `550c7d99e4c9dfcf420554bc1b77ac43948a83f646aedffa99bbe54125ce86de` ; mesures définitives au commit de la course, `527ab727cf8edc8789352cb908293705236d1a9661540dd3ecff4cce9bba0fbc`) ; la contre-lecture du projet version 4 (`98bedba8…`, ci-dessus : corrections C1 à C7, onze points mineurs) ; la décision R-3218 et le commit `081bc453ce144a1a313465d0ee7366d22a26db1d` (registre des accords rendu lisible par la garde) ; la décision R-2975 (plancher de 20 USD) ; les lignes GO-2026-11-14-09, GO-2026-11-16-06, GO-2026-11-16-11, GO-2026-11-16-12, GO-2026-11-18-03 à GO-2026-11-18-08 de `registres/go.md` ; les choix de la mère transmis au rédacteur (C1, C3, C6, C7, points mineurs 7 et 10, relevé de la garde au geste 3, accords cités). Tous ces fichiers sont sous `docs/notes/prealables-course-etape-b-bis-v1/` sauf mention contraire.

---

## CORRESPONDANCE DE LA VERSION 5 — corrections de la contre-lecture et choix de la mère

« C » renvoie aux corrections exigées de la contre-lecture du projet version 4 (§ 2), « m » à ses points mineurs (§ 3). Chaque ligne dit le geste modifié et la manière. Ce qui a été rejoué sur un analogue sans effet, et ce qui ne l'a pas été, est au § 15.

| correction | geste(s) modifié(s) | comment |
|---|---|---|
| C1 — le geste 2 (a) arrêtait un opérateur sain | geste 2 ; réserve 9 | (a) n'est plus qu'un relevé, recopié au compte rendu, jamais un critère d'arrêt (dans un sous-agent, la variable du dossier de projet n'est pas exportée au shell même quand le crochet est chargé). La preuve de chargement du crochet est le refus de (e), avec (b) et (c). Réserve 9 réécrite. |
| C2 — au geste 14, les fenêtres ne gardaient pas la création | gestes 1, 5, 6 (c), 14 | Une seule liste `&&` par appel : le document en ligne s'ouvre **au milieu** de la chaîne (`… && cat > ligne-courte.sh <<'FIN' && …`), son texte suivant la ligne de commande. Les fenêtres (30 minutes, une heure), l'outil du geste 4, le tour, les fichiers neufs conditionnent donc l'égalité des arguments, les clés et la création. « CREATION TENTEE » ne s'imprime que dans la chaîne ; sinon « AUCUNE CREATION TENTEE PAR CET APPEL » et une ligne de diagnostic. **Écart de forme à la proposition de la contre-lecture** (ligne courte écrite dans un appel à part, fin du geste 13) : le texte de la création reste dans l'appel qui crée, pour que le crochet le voie et contrôle l'accord au moment même ; écrite dans un appel à part, la ligne courte serait jouée par un appel sans texte de création, que le crochet ne contrôlerait pas. Même forme au geste 6 (c), aux gestes 1 et 5. |
| C3 — reprises « sous des noms neufs » injouables | préambule P, commande O, gestes 7 à 24 | Suffixe de tour **porté par tous les chemins** des gestes 7 à 24 (la mère demandait 11 à 23 ; les gestes 7 à 10 en sont aussi, car un tour neuf relit l'inventaire, le débit des autres et le crédit ; le geste 24 lit le dossier d'envoi entier), sous la forme d'un dossier de tour `$TD` = `$D/tour-<n>`. `<n>` est compté par le préambule dans `$D/tours.txt`, journal en ajout écrit par programme (commande O). Au plus trois tours, jamais après une création tentée. Un tour neuf rejoue les gestes 7 à 14, dans l'ordre, dans un dossier neuf : plus aucun fichier à renommer, plus aucune lecture d'un fichier « au lieu d' » un autre. À l'intérieur d'un tour, les noms restent ceux de la version 4, d'où une ligne courte inchangée à l'octet. Les lectures répétées prennent un nom donné par `mktemp`. Le suffixe a été rejoué sur analogue (§ 15) : le rédacteur ne l'a pas jugé trop risqué, et n'a pas retenu l'interdiction de toute reprise. |
| C4 — pas de ligne pour une marche qui tombe | geste 20 | Ligne « toute autre ligne `BBIS ARRET` : geste 21 (présence seulement), puis gestes 22 et 23 dans les quinze minutes ». **Raffinement déclaré** : les arrêts qui laissent les résultats de la marche sur le disque sans les pousser (« branche locale de sortie depuis COMMIT », « ajout », « fichier de plus de … octets », « commit ») suivent la ligne « poussée impossible » de la version 4 (garde de 12 heures, nœud), pour le motif qu'elle donnait déjà ; ligne voisine pour un conteneur arrêté sans ligne FIN ni ARRET. |
| C5 — une lecture passagère pouvait détruire la course | commande L, gestes 16, 17, 19 ; programme `inventaire_v2.py` | Commande propre aux gestes 17 et 19 (et à la garde de 12 heures), aux noms donnés par `mktemp`, qui n'écrit jamais `prix-relu.sh`. Ce fichier est écrit une seule fois au geste 16, sous `noclobber`, et seulement depuis un verdict conforme. « Absente » ne compte que si le témoin figure dans la même liste (code 4) ; sinon « incomplète » (code 5) ; prix illisible : code 6. Trois lectures sans verdict au plus, à une minute d'écart ; le compteur est tenu par programme dans `etat.txt`. Étendu au relevé du crédit du geste 19 (même motif). |
| C6 — les deux planchers de crédit ne tenaient pas ensemble | § 0 champ 3, § 6, geste 8, § 11, réserve 10 | Choix de la mère : condition du geste 8, **crédit − 13 × débit des autres ≥ 8 + 11 × 1,48 = 24,28 USD**, calculée par programme (en dix-millièmes entiers, sans arrondi flottant). Le plancher de 20 USD (R-2975, GO-2026-11-18-03 (2)) est vérifié aussi. L'heure du relevé n'est écrite que sous « CREDIT SUFFISANT », dans le fichier du tour `credit-heure.sh`, jamais réécrit : un relevé par tour, donc un nom neuf par relevé. |
| C7 — sortie de l'amorce avant la minuterie bornée par un opérateur vivant seulement | § 5, § 6, geste 16 | Le pire cas suppose la minuterie armée : c'est écrit au § 5 et au § 6. Filet de la mère : au geste 16, elle pose un rappel à création + 30 minutes (état et trois lignes confirmés par l'opérateur, sinon destruction par l'identifiant et preuve d'absence) et un rappel à échéance + 15 minutes. Le geste 16 imprime les deux heures par programme. |
| m1 — geste B.3 de l'arbitrage, à la lettre | geste 3 (b) | Registre voisin dans la liste de `git diff --quiet` ; ligne `ADDENDUM-ECART-3-BBIS` comptée (une fois, chemin et empreinte entiers) ; compagnon de l'addendum vérifié ; deux empreintes de la chaîne présentes dans l'addendum. Tout est jugé par programme. |
| m2 — heure de rédaction | en-tête, § 15 | Heure de fin relevée par `date -u` à la fin de la rédaction. |
| m3 — « le jeton factice apparaît » | geste 6 (c), geste 14 | Phrase corrigée : la sortie coupée à 80 caractères ne montre pas les jetons. Leur place en fin de `--env` est comptée par programme (« CLES PASSEES PAR LEUR NOM »). |
| m4 — geste 5 hors du dossier si `cd` échoue | geste 5 | Chaque programme écrit par chemin absolu, un appel par programme, une seule liste ; contrôle final des trois empreintes par `sha256sum -c`. |
| m5 — étiquette déjà portée lue à l'œil ; débit | geste 7, § 6, `inventaire_v2.py` | Étiquette déjà portée : code 3 (arrêt, nœud). Le débit ne compte que les instances à l'état « running » : c'est dit dans la sortie du programme et au § 6. |
| m6 — code de la garde de dépense ambigu | gestes 11 et 19 | Seule la ligne « GARDE DE DEPENSE : REFUS AVEC ORDRE DE DESTRUCTION » (refus de la garde, ordre imprimé) commande la destruction ; un échec de la chaîne s'imprime à part. |
| m7 — qui répond aux demandes d'autorisation | § 0 condition 8, § 10, § 11 | Choix de la mère : l'opérateur est un sous-agent lancé depuis la session mère ; toute demande d'autorisation refusée ou expirée est un arrêt et un nœud, jamais contournée ni rejouée autrement. |
| m8 — fichiers `.err` | § 9, tous les gestes qui lisent le loueur, geste 24 | Jamais affichés (taille seulement) ; effacés au geste 24. |
| m9 — instance gardée 12 heures encore en marche | geste 20 (garde de 12 heures) | État relu dès l'arrêt lu au journal, puis toutes les heures ; « running » ou « loading » : gestes 22 et 23 aussitôt. |
| m10 — réponse illisible avec une instance saine | geste 15, `inventaire_v2.py` | Choix de la mère : adoption par l'étiquette (une seule instance de l'étiquette, créée après la commande du geste 14, sur l'offre retenue), puis geste 16 ; toute autre configuration suit le chemin de destruction et de preuve d'absence. Tolérance de 120 secondes sur l'heure de création, déclarée (réserve 16). |
| m11 — échec de la lecture du journal | geste 18, réserve 13 | Écrit à la réserve 13 : il ne se distingue pas d'une ligne absente ; destruction à cinq minutes ; la sous-commande `logs` n'a jamais servi dans cette chaîne. |
| mère — relevé de la garde | geste 3 (a) ; § 0 condition 4 | `python3 -I -c` qui importe `.claude/hooks/garde_calcul.py` et appelle `lire_go(Path("registres/go.md"))` sans arrêt. La condition 4 de la version 4 (registre illisible) est **levée** : R-3218, commit `081bc453`. |
| mère — accords | § 0 champs 1 et 2 ; § 1 | Cités par leur identifiant : GO-2026-11-18-06 (deux clés par leur nom), GO-2026-11-18-07 (plafond au lanceur ; plus aucune recharge jusqu'à nouvel ordre). Aucune valeur de clé. |
| mère — recharge | § 0 champ 3 | La course ne part qu'après une recharge de Lazar ; le champ du relevé de crédit reste ouvert jusqu'au moment du feu (geste 8). |
| rédacteur — autres changements, déclarés | gestes 3, 6 (a), 9 à 13, 22, 23 ; § 8 ; réserves 15 à 18 | Noms en `-v5` (dossier d'envoi, outil, feu versé). Empreinte du feu exigée sur 64 caractères avant la commande (gestes 6 (a) et 12) : renfort seulement ; avec `pipefail`, posé par le préambule, la version 4 s'arrêtait déjà sur un feu absent, mais sans lui le texte du feu partait vide et la garde de création du lanceur, qui n'y cherche que les deux numéros d'accord, l'aurait accepté (rejoué). Geste 13 jugé par programme. Gestes 9 à 12 : verdicts imprimés en clair. Geste 22 : « demandée » imprimé seulement si la destruction a été jouée. Geste 23 : liste brute du lanceur effacée par le nom de son dossier jetable, où qu'il soit. Les gestes 22 et 23 lisent `a-detruire.txt`, écrit au geste 15. |

---

## § 0 — CE FEU N'EST PAS EN VIGUEUR À SA RÉDACTION

Il n'autorise aucune création de machine et aucun appel au loueur. Les gestes de la phase A (§ 10, gestes 1 à 6) ne touchent pas le loueur ; ils sont permis dès que ce feu est scellé, versé et inscrit. Les gestes 7 et suivants ne sont permis que lorsque **toutes** les conditions ci-dessous sont levées, chacune par une pièce versée et scellée, ou par un mot écrit de Lazar inscrit au registre des accords, et sur un message de la mère à l'opérateur qui cite la recharge du champ 3. Un opérateur qui lit ce feu sans elles s'arrête au geste 6, ne crée rien, et le dit en une ligne.

**Champs** :

1. **Passage des deux clés : accord de Lazar, cité.**
   Les deux clés sont le jeton GitHub des machines, `CONTROLE_IA_GITHUB_TOKEN_2`, passé comme `GH_TOKEN`, et le jeton de la plateforme de modèles, `HF_TOKEN`. Elles passent **par leur nom seulement**, dans le seul shell de lancement, pour cette seule course. Aucune valeur n'est lue, affichée ni copiée.
   Accord cité : **GO-2026-11-18-06** (`registres/go.md`, l. 370 à la rédaction ; décision R-3195, inscrite à 2026-11-18T05:49:30Z ; mot direct de Lazar reçu vers 05:50Z, verbatim « oui cles, je n'ai plus de budget pour recharger avant qq heures au moins » ; échéance 2026-11-22). La mère vérifie au moment du feu que la ligne est toujours au registre et qu'aucune révocation ne la cite.
2. **Plafond de prix de 1,40 USD/h tenu aussi par le lanceur : accord de Lazar, cité.**
   Ce plafond va contre la lettre de GO-2026-11-18-03 (3), « tenu hors du code ». C'est une garde plus stricte, sans effet sur les résultats.
   Accord cité : **GO-2026-11-18-07** (`registres/go.md`, l. 371 à la rédaction ; décision R-3196, inscrite à 2026-11-18T05:52:51Z ; mot direct de Lazar reçu vers 05:55Z, verbatim « plud de recharge jusqu a nouvel ordre, oui a la limite jusqu a nouvel ordre , quand le credit sera recharge on poura la lever » ; échéance « — » depuis R-3218, correction de forme seulement). Le même accord interdit **toute recharge du loueur jusqu'à nouvel ordre**. Si Lazar lève plus tard ce plafond, le lanceur version 6 le tient quand même : seul un lanceur version 7 pourrait le retirer, et ce n'est pas cette course.
3. **Relevé de crédit du loueur et recharge de Lazar** — ouvert jusqu'au moment du feu ; rempli non dans ce texte scellé, mais par la sortie du geste 8 du tour de la création, que la mère recopie à l'engagement (geste 16, registre des dépenses) :
   - crédit `______ USD`, relevé à `____-__-__T__:__:__Z` par le geste 8 du tour `__` ; ce relevé date de moins d'une heure à la création (contrôlé par programme au geste 14) ;
   - **plancher** : crédit d'au moins **20,00 USD** (R-2975 ; GO-2026-11-18-03 (2)) ;
   - **et marge** (choix de la mère sur C6) : crédit − 13 × débit horaire des autres instances à l'état « running » **≥ 8 + 11 × 1,48 = 24,28 USD**, calculé par programme au geste 8, jamais à l'œil ;
   - **recharge de Lazar qui ouvre la course** : `________________` (mot de Lazar ou ligne du registre des accords). GO-2026-11-18-07 interdit toute recharge jusqu'à nouvel ordre ; l'exception de GO-2026-11-18-08 (environ 20 USD) est réservée à la course de confirmation du témoin de Bailey, et « aucune autre machine ne puise dans cette exception ». La course ne part qu'après une recharge de Lazar ; la mère la cite dans le message qui ouvre la phase B.

**Conditions à lever par la mère, sans champ** :

4. **Registre des accords lisible par le crochet de garde : levée.** Jusqu'à 06:41Z le 2026-11-18, trois échéances « jusqu'à nouvel ordre » rendaient `registres/go.md` illisible pour le crochet (`.claude/hooks/garde_calcul.py`), qui répondait « registre GO mal formé ligne 371 : dates illisibles » et refusait toute création, pour toutes les sessions. La mère a ramené ces cellules à « — » (GO-2026-11-18-07 et GO-2026-11-18-15, type décision) et à 2026-11-25, date de forme (GO-2026-11-18-13, type calcul) : décision R-3218 (2026-11-18T06:41:31Z), commit `081bc453ce144a1a313465d0ee7366d22a26db1d`. Relevés du rédacteur : `lire_go()` lit le registre sans arrêt (336 accords à 07:01Z ; 337 à 07:27Z, le registre croissant). Preuves exigées au moment du feu : geste 2 (c) et geste 3 (a).
5. **Accord de l'opérateur valide le jour de la création.** GO-2026-11-16-06 (opérateur sous-agent du modèle A) porte l'échéance 2026-11-18. Au-delà, la mère écrit sous quel accord l'opérateur agit (R-2883 (2) demande le modèle B, disponible à partir du 2026-11-21T04:00Z), ou demande un mot à Lazar.
6. **Mesures définitives versées et suivies : levée à la rédaction.** Le compte rendu `mesures-definitives-commit-course-v1.md` (`527ab727…`) est suivi par git (commit `2a9ed001`, 2026-11-18T05:58:05Z), avec ses seize sorties scellées (commit `478111c2`). Preuve rejouée au geste 3 (b), lignes 11 à 13.
7. **Vérification courte de cette version par un lecteur neuf** (ni rédacteur des projets versions 3, 4 ou 5, ni contre-lecteur de la version 4), sur les corrections C1 à C7, les onze points mineurs et les choix de la mère, rendue sans bloquant. Puis :
   - le feu scellé et versé sous `registres/t07-etape-b-bis/feu-bbis-v5.txt`, avec son compagnon ;
   - son empreinte inscrite par une ligne du registre des décisions (le geste 3 (b) l'y cherche), **jamais au registre propre** (celui-ci n'admet que les huit clés du texte scellé) ;
   - le tout commité et poussé sur `main`.
8. **Opérateur neuf : un sous-agent lancé depuis la session mère** (choix de la mère sur m7 ; GO-2026-11-16-06) :
   - la session mère a le dépôt de travail `/home/user/controle-ia-travail` pour dossier d'origine (R-3114 : le crochet ne se charge qu'ainsi ; preuve de chargement : geste 2 (e)) ;
   - les gestes 6, 13 et 14 portent le texte d'une ligne de création, que le crochet contrôle et que les permissions ne couvrent pas d'avance (seule l'étiquette de la répétition l'est dans `.claude/settings.json`) ; d'autres gestes peuvent demander une autorisation selon le mode de la session ;
   - **toute demande d'autorisation refusée ou expirée est un arrêt et un nœud** : jamais contournée, jamais rejouée autrement (reformulée, découpée, déplacée dans un fichier, confiée à un autre agent) ;
   - l'opérateur n'a lu aucun résultat de l'étape B, de 7a, de 7b, de T0.6 ni de P3-bis.
9. **Budget du jour.** La dépense du jour, comptée à l'heure de Paris de 23:00Z à 23:00Z, recharges comprises, plus le pire cas de cette course (20,20 USD, § 6), doit rester sous 100 euros (≈ 108 USD au taux déclaré). Règle de R-3124, maintenue par GO-2026-11-18-03 (2). La mère le vérifie au registre des dépenses et l'écrit.

**Conditions des versions 3 et 4, désormais levées** :

- **Nœud « entropie » (N-1).** L'écart d'entropie est couvert par GO-2026-11-18-03 (1). Celui de l'épreuve de niveau et sa clause d'antériorité sont couverts par le troisième addendum, accordé par la mère sous GO-2026-11-18-05 et R-3170 (8) (R-3191).
- **Nœud « recharge » (N-2).** GO-2026-11-18-03 (2) maintient le plancher de 20 USD, en plus du budget de 100 euros par jour, recharges comprises.
- **Trace du pilote de la commande.** Remplacée par le geste 6, au commit de la course.
- **Outil du loueur.** Geste 4.
- **Portillon des essais.** Levé par les mesures définitives : 151 et 25, sous Python 3.13 et 3.11.
- **Crochet.** Son compagnon d'empreinte est présent ; sa preuve de chargement est le refus du geste 2 (e).
- **Nombre de relances.** Fixé au § 7.
- **Champs 1 et 2 de la version 4.** Remplis par les accords cités ci-dessus.
- **Condition 4 de la version 4 (registre illisible).** Levée (R-3218).
- **Condition 6 de la version 4 (mesures non commitées).** Levée (commit `2a9ed001`).

---

## § 1 — LIGNES D'ACCORD

- **Ligne d'accord de calcul : GO-2026-11-14-09** (type « calcul », 40,00 USD, échéance 2026-11-22). Elle porte :
  - une A100 seulement, une relance au plus ;
  - une garde de débit ;
  - un feu écrit de la mère portant ce numéro avant toute location ;
  - l'arrêt et la destruction par identifiant (R10).
  Extrait fidèle : `registres/t07-etape-b-bis/go-bbis-v2.txt` (`33f38e675ca2114674b6f7dd96727b222fae613ecb53b57ef16240b74aca8e62`), égal à la ligne 328 de `registres/go.md`, inscrit au registre propre (ligne `GO-BBIS`).
- **Course supplémentaire, une seule : GO-2026-11-16-11** (second addendum, contrôle carte-processeur).
- **Mesure de la dispersion des aires entre deux ordres de calcul : GO-2026-11-16-12.**
- **Opérateur : GO-2026-11-16-06.** La machine est créée par un sous-agent opérateur. Arrêt au premier refus de permission, du crochet ou du classifieur, sans rejeu, reformulation, découpage ni contournement. Préavis d'une ligne à Lazar au moment du geste. Échéance 2026-11-18 : voir § 0, condition 5.
- **Accord de lancement et de dépense de Lazar**, 2026-11-18 vers 02:14Z, verbatim « Billet sur le contrôle de l'IA — un seul run manque : la course de l'étape B bis. : go » (R-3129). Il ne dispense ni des préalables ni de ce feu.
- **Trois décisions de l'étape B bis : GO-2026-11-18-03** (R-3149) :
  - (1) écart d'entropie couvert, réserve nommée au verdict ;
  - (2) plancher de 20 USD de crédit maintenu, en plus du budget de 100 euros par jour, recharges comprises ;
  - (3) plafond de 1,40 USD/h écrit au feu et prix relu après création ; le verdict dira que ce plafond tenait à un opérateur.
- **Amorce corrigée : GO-2026-11-18-04** (R-3162).
- **Autonomie de 24 heures : GO-2026-11-18-05** (R-3170).
  - R-3170 (8) : accord de la mère sur le troisième addendum, donné et inscrit (R-3191).
  - Le passage d'une clé à une machine reste à Lazar (champ 1).
  - Dépenses, chacune avec un devis écrit au registre avant le lancement : le devis de cette course est le § 6 de ce feu.
- **Passage des deux clés : GO-2026-11-18-06** (champ 1).
- **Plafond au lanceur ; plus aucune recharge jusqu'à nouvel ordre : GO-2026-11-18-07** (champ 2).
- **Exception de recharge réservée au témoin de Bailey : GO-2026-11-18-08.** Aucun crédit de cette course n'y puise (champ 3).

## § 2 — TEXTES QUI FONT FOI, À CITER DANS LE VERDICT

- **Texte scellé** : `prereg/T0.7-etape-B-bis-v1.md`, `0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb`. Ligne `SCELLEMENT-BBIS` du registre propre, 2026-11-14T12:30:30Z.
- **Premier addendum d'écart** : `prereg/T0.7-etape-B-bis-v1-addendum-ecart-v1.md`, `f00eda8a9fb74516289a085350425d128bf5b1cf1dbc50eee32d8bbe749c78d7`. Ligne `ADDENDUM-ECART-1-BBIS`.
- **Second addendum d'écart** (contrôle carte-processeur à deux horizons) : `prereg/T0.7-etape-B-bis-v1-addendum-ecart-2-v1.md`, `18baeac32d26ebf174c62d7a36caedeee1d5b80648c6743c21dc30d2747afd26`. Ligne `ADDENDUM-ECART-2-BBIS`.
- **Troisième addendum d'écart** : `prereg/T0.7-etape-B-bis-v1-addendum-ecart-3-v1.md`, `e5604cbdce509958e1f3e3bc3a36c8d17a78c8900b5f93a2102fff9b51d07872`. Il porte :
  - la chaîne version 6, hors de la fiche de code ;
  - l'entropie changée ;
  - l'épreuve de niveau rejouée et sa clause d'antériorité ;
  - la lecture déclarée de la liste d'arrêt.
  Ligne `ADDENDUM-ECART-3-BBIS`, présente une fois à la l. 9 du registre voisin au commit de la course, 2026-11-18T05:46:36Z.
- **Registre propre** : `registres/t07-etape-b-bis-v1.md`. Lignes : `SCELLEMENT-BBIS`, `ABSENCE-B-BBIS`, `CODE-BBIS` version 1 (remplacée), `CODE-BBIS` version 2 (en vigueur), `GO-BBIS`. Jamais `registres/scellements-v1.md` : une clé de l'étape B bis dans ce registre partagé ferait refuser la création.
- **Registre voisin des addenda** : `registres/t07-etape-b-bis-v1-addenda-v1.md`. Aucun code ne le lit. **Un verdict qui ne cite pas les trois lignes `ADDENDUM-ECART-1-BBIS`, `-2-BBIS` et `-3-BBIS` n'est pas scellé.**

## § 3 — CODE DE LA COURSE, COMMIT, MESURES SCELLÉES

- **Commit de la course, fixé une fois** : `438a9c5257bdc4fa65f25c42cc89753a049b4586`. Il porte le troisième addendum scellé et sa ligne `ADDENDUM-ECART-3-BBIS`. Il est présent sur `origin/main` (relevé par le rédacteur vers 07:00Z, puis par le geste 3 (b) joué sur analogue à 07:27Z ; à rejouer au geste 3), et le commit de la fiche `05cd22aa15382f61eb62b9e7817890dde728dd5f` en est un ancêtre. **Branche de code passée à l'amorce : `main`.** Toute mesure et toute commande de ce feu portent ce commit exact.
- **Fiche de code en vigueur** : `registres/t07-etape-b-bis/code-bbis-v2.json`, `4b28535c17fe450ff1c1ecc9164d91c4c8d03354e4f4137e324f2b04390be5bb`. Elle cite 63 fichiers au commit de la fiche `05cd22aa…` : 22 sous `src/controle_ia/t07bbis/`, 21 scripts, 20 essais. La garde d'entrée de la marche les contrôle sur la machine.
  - Entropie : `149084685129585384182032033013812122656`. Elle est changée par rapport à la première fiche (TA-3 du troisième addendum, GO-2026-11-18-03 (1)).
  - Épreuve de niveau rejouée : `registres/t07-etape-b-bis/epreuve-niveau-deux-plis-bbis-v2.json`, `da9fa42bf95c9d6507b01d7bf69db2876a56c00d26b0cc58c15cd7893bfa5919`. Niveau décisif retenu : 0,99.
  - Le second addendum épinglait l'épreuve `641adeb5…` de la première fiche ; elle est absente du dépôt. Cet écart et la clause d'antériorité (épreuve versée le 2026-11-17 à 11:03:40Z, après la course du 16 novembre qui avait relu les données de 7b sans écrire de score) sont couverts par TA-4, TA-5 et le § 0 du troisième addendum.
- **Chaîne de lancement version 6**, hors de la fiche, rattachée par le § 6 du troisième addendum. Empreintes **entières** :
  - amorce `scripts/amorce_bbis_v6.sh` : `26f954e9e9783bf95a5149db9e848e1bd207dc8b027e6027d879363be2dfbbb5` (31 075 octets, 41 436 caractères en base64) ;
  - lanceur `scripts/lancer_bbis_v6.sh` : `3224ce14dc3fefe7cc46774072f65288a39c3fe760f325e311c5f948c45344b7` ;
  - essais de la chaîne `tests/test_chaine_bbis_v6_v1.py` : `f36571bd7fb7f5693f8e45433f44c7826722b9baf995ce219038923d486b49ca`.
  Elle a été contre-lue sous quatre angles par des agents neufs, avec arbitrage (`688abea5…`, R-3188).
- **Lanceur joué depuis la racine du dépôt**, `PYTHON_BBIS` posé en chemin absolu, `/home/user/controle-ia-travail/.venv/bin/python`, pour toutes ses sous-commandes. Un chemin relatif rend un faux refus dans `essais-du-commit` (répétition, § 3).
- **Mesures scellées au commit exact** (`mesures-definitives-commit-course-v1.md`, `527ab727cf8edc8789352cb908293705236d1a9661540dd3ecff4cce9bba0fbc`, verdict « tout conforme ») :
  - **Plancher d'essais, geste B.2.**
    - Sous Python 3.13.18 : code 0, « 151 passed, 25 skipped, 4 warnings », 516 fichiers, liste `d48e74d31bce24bfb0774e9d8ae24bf4325058a47152d5d3abb3c7117a49edc0`, sortie d'erreur vide.
    - Sous Python 3.11.18 : code 0, « 151 passed, 25 skipped », mêmes 516 fichiers, même liste.
    - Sorties : `commande-1-…-sortie-lanceur.txt` `35805d014b504c3e6c88d39eb41e20b6897d6e5f1eedde4b1c897ed65449f3e7`, `commande-1-…-essais.txt` `f6b483ef0e18f050d73aaaea99b2a9247ab4302a5eadcfcffcbd9c434ced35bc`, `commande-2-…-sortie-lanceur.txt` `acc5c4abe1b2de06c4bd79801d2dbe51339146e455d61e4fc3c726024dd0964c`, `commande-2-…-essais.txt` `762e561a244ad6a295c6461af94e9417c94ac1e833ddeb982ac1539beffa1f49`.
    - **Plancher de l'amorce : 151, partout dans ce feu (et non 176).**
  - **Code hors de la fiche, geste B.4.**
    - `git diff --quiet 05cd22aa 438a9c52… -- src requirements-gpu.txt pyproject.toml tests/conftest.py 'tests/test_t07bbis_*' 'tests/aide_t07bbis_*'` : code 0 (`commande-3-…`, `bce8326b86e8bfede07dc8bec63902be7f7c8917b42116fdb16cd2e3a7fad697`).
    - Fichiers réutilisés de la l. 19 du texte scellé : 11 sur 11 conformes (`commande-4-…`, `f2b4d3c9ef8e60f026a239c63a33bbacf19fb2d739fe7fb0bdc7eb3e42a8e130`).
    - Racine : 35 entrées aux deux commits, liste égale (`commande-5-…`, `b37b2d0f6abf57a9698adaf426a8b41064fe7ee40a25069c603c629469e83199`).
  - **Chaîne et addendum, geste B.3 hors loueur.**
    - Empreintes de la chaîne au commit, égales en entier au § 6 de l'addendum (`commande-6-…`, `25bbbbd40e0b1a9b9d10a784b1e3d07976df41e2be5fa4fa66f993ca74c33de5`).
    - Ligne `ADDENDUM-ECART-3-BBIS` présente une fois, chemin et empreinte entiers (`commande-7-…`, `7e352de624efdc55a085df2077468c6e3d0163e8d7cc9bc2c18f2eb48d84c6c3`).
    - Addendum conforme à son compagnon (`commande-8-…`, `6ccd117866c4780da038581783bac8c7d7d5e290dd9426c802cda3b556263059`).
    - Le geste 3 (b) rejoue ces trois contrôles dans le shell de lancement (point mineur 1).
  - **Ce qui reste à faire au feu** : le décodage du base64 de la commande imprimée. C'est le geste 13.
  - Toutes ces sorties sont sous `mesures-definitives-commit-course-v1/`, chacune avec son compagnon.
- **Remarque des mesures, reprise** : un seul fichier de la racine diffère, par son contenu, entre `05cd22aa` et le commit de la course : `CLAUDE.md`, sur 3 lignes. Ni le code de la course, ni ses essais, ni l'amorce ne le lisent. Ce n'est pas un écart aux critères écrits.
- **LE CODE DE LA COURSE EST GELÉ.** La garde de création exige exactement deux lignes `CODE-BBIS` pour deux relances. Une troisième fiche ferait refuser la création. Aucune retouche n'est possible avant cette course.

## § 4 — DONNÉES

- **Branche d'entrée** : `calcul/t06-confirmation-7b-v1` ; course de 7b `20261111-151701-t06-reel`. Tête `55c3e3eb89a4650419f35999aaa4c54288275b0d`, relevée par le projet version 3 et **non relue par le rédacteur**, qui ne touche aucune branche de calcul. L'amorce n'en extrait que des fichiers nommés.
- **Branche de sortie**, neuve et exigée **absente** du distant avant la course : `donnees/t07-etape-b-bis-v2`. Le lanceur refuse si elle existe (« nouveau nom exigé ») et refuse si le distant est muet (« absence de la branche de sortie non prouvée »). Aucun repli silencieux (R5).
- **Dépôt de travail et lui seul** : `https://github.com/lciric/controle-ia-travail.git`. Jamais `lciric/controle-ia`, qui sera la copie expurgée publique.

## § 5 — MACHINE ET OFFRE

- **Carte et ressources** :
  - une seule carte A100 SXM4 80 Go, aucune H200 (mot de Lazar seulement) ;
  - au moins 16 cœurs effectifs, au moins 128 000 Mo de mémoire vive, disque de 150 Go ;
  - stockage au plus 0,08 USD/h (clé `storage_cost` × 150 / 730).
- **Hôte** :
  - version CUDA servie par l'hôte (`cuda_max_good`, recopiée telle quelle de la recherche) d'au moins 13.0 ; clé absente ou illisible : refus ;
  - **pilote de série 595 ou 580** : `driver_version` commence par `595.` ou `580.`. Il est recopié tel quel au registre des dépenses. Une offre sans cette clé ne peut pas être retenue.
  - Raison : l'amorce ne lit que « CUDA Version: ». Les pilotes des séries 610 à 620 affichent « CUDA UMD Version: ». L'instance 60952525 s'est arrêtée ainsi le 16 novembre, sur le pilote 615.71.09.
  - La série 595 est la seule éprouvée sur une vraie machine de cette chaîne (595.91.07 : instances 60760941 et 60953606). La série 580 ne l'a jamais été (réserve 7).
- **Prix de carte au plus 1,40 USD/h**, clé `dph_total` de l'offre. Il est tenu trois fois :
  - par le programme de choix de l'opérateur (geste 10) ;
  - par le lanceur version 6 (`PRIX_MAX_USD_H=1.40`, champ 2) ;
  - par le prix relu après création (geste 16) et à chaque lecture d'état (gestes 17 et 19).
- **Image** : `python:3.11-bookworm`, exigée par son nom par le lanceur version 6 (`IMAGE_COURSE`) et contrôlée par programme sur la ligne imprimée (geste 13). Elle est nommée, non épinglée par un condensé (réserve 4).
- **Étiquette** : `bbis-t07-v1`, fixée par le texte scellé.
- **Choix de l'offre par programme, dans la sortie brute de la recherche, jamais retapée** (gestes 9 et 10). Le programme écarte les pilotes hors série et les prix au-dessus du plafond. Puis la sous-commande `offre-depuis-recherche` du **lanceur de la course** est jouée sur chaque survivante, de la moins chère à la plus chère. La première acceptée est retenue.
  - La sous-commande `offre` de `scripts/repetition_carte_bbis_v3.py` est **interdite ici** : elle exige l'étiquette de la répétition et 60 Go de disque, et refuserait l'offre de la course pour une raison étrangère au prix.
- **Échéance de la minuterie : 13 heures**, calculée par commande au geste 12, `ECH=$(( $(date +%s) + 46800 ))`. Si la création attend plus de 30 minutes après la commande, un tour neuf rejoue les gestes 7 à 14 (§ 10, commande O).
  - L'amorce refuse une échéance hors de l'intervalle ]maintenant ; maintenant + 24 h]. Elle exige la clé d'interface du conteneur (par son nom) avant d'armer la minuterie.
  - La minuterie demande ensuite la destruction toutes les 60 secondes, sans jamais juger le code de retour, et demande l'état « arrêtée » après cinq essais.
  - **Réserve** : la minuterie vit dans le conteneur et meurt avec lui. Une instance arrêtée facture son disque sans minuterie. La destruction finale reste un geste de session.
  - L'opérateur lit la ligne « minuterie lancée » au journal dans les cinq minutes (geste 18).
  - **Le pire cas suppose la minuterie armée (C7).** Entre la création et la ligne « minuterie lancée » lue au geste 18, rien d'automatique ne borne la dépense. Si l'amorce sort avant d'armer la minuterie (ses dix sorties « BBIS REFUS » d'avant la minuterie, ou un base64 illisible qui ne laisse aucune ligne) et que la session de l'opérateur tombe, la carte facture sans minuterie, et le loueur peut relancer le conteneur en boucle (déjà vu : instance 60671759). Ce cas n'est borné que par l'opérateur vivant (gestes 17 et 18) et par **le filet de la mère** : au geste 16, à l'inscription de l'engagement, elle pose deux rappels dans sa session :
    - **à la création plus 30 minutes** : l'opérateur doit lui avoir confirmé l'état « running » (geste 17) et les trois lignes du journal (geste 18, « JOURNAL CONFORME ») ; sinon elle détruit par l'identifiant (geste 22) et prouve l'absence contre un témoin (geste 23) ;
    - **à l'échéance plus 15 minutes** : elle relit la liste ; une instance de la course encore listée est détruite par l'identifiant et son absence prouvée, sauf garde de 12 heures déclarée par l'opérateur (geste 20) ; dans ce cas, elle relit l'état (commande L) et détruit si l'état est « running » ou « loading ».

## § 6 — DEVIS, PRIX, DÉPENSE, CRÉDIT

**Devis de la course** (exigé par GO-2026-11-18-05 avant le lancement) :

| | montant | source |
|---|---|---|
| coût attendu | 5,6 à 9,9 USD | texte scellé |
| coût attendu, mesure de dispersion comprise | 5,8 à 6,6 USD | second addendum |
| plafond horaire de carte | 1,40 USD/h | stockage ≤ 0,08 USD/h en plus |
| pire cas sous la minuterie | 13 h × (1,40 + 0,08) = **19,24 USD** | |
| pire cas avec 12 h de disque après un arrêt (garde de débit, résultats restés sur le disque) | ≈ **20,20 USD** | ≤ 0,96 USD de disque, section 6 du second addendum |
| coupure de la garde de dépense | 39,50 USD | inclusive |
| plafond de la ligne d'accord | 40,00 USD | |

**Ces pires cas supposent la minuterie armée (C7, § 5).** Avant la ligne « minuterie lancée », la dépense n'est bornée que par l'opérateur (gestes 17 et 18 : au plus 25 minutes après la création) et par le filet de la mère (rappel à la création plus 30 minutes) : environ une demi-heure de carte, ≈ 0,74 USD, plus le temps de réaction de la mère. Si ni l'un ni l'autre n'agit, rien ne borne la dépense.

**Cumul de la ligne et marges** :

- Cumul déjà dépensé sous GO-2026-11-14-09 : **5,989 USD**. Il se compose des répétitions (0,749), de la première création du 16 novembre (0,10) et de la relance unique (5,14) (`registres/depenses.md`, l. 476, 481 et 482). Aucune dépense depuis sous cette ligne.
- C'est **ce** cumul, celui de la ligne, que l'opérateur passe à la garde de dépense.
- Cumul de la ligne au pire après cette course : 5,989 + 20,20 = **26,19 USD** sur 40.
- Reste sous la coupure après ce pire cas : 39,50 − 26,19 = **13,31 USD**.
- Aucune autre course n'est permise après celle-ci (§ 7).

**Garde de dépense** (`bash scripts/lancer_bbis_v6.sh depense CUMUL PRIX`) :

- C'est une calculette, sans guetteur, sans boucle, sans lecture du vrai cumul chez le loueur.
- Elle refuse dès que le cumul relevé plus un quart d'heure de carte atteint 39,50 USD, et imprime alors l'ordre de destruction (« BBIS : arrêt et destruction par l'identifiant … »).
- Elle est jouée une fois avant la création (geste 11), puis à chaque heure de marche (geste 19 (b)), avec cumul = 5,989 + heures écoulées depuis la création × prix relu.
- **Seul un refus de la garde avec son ordre imprimé commande la destruction** (point mineur 6) : la commande imprime alors « GARDE DE DEPENSE : REFUS AVEC ORDRE DE DESTRUCTION ». Un échec de la chaîne (fichier du tour manquant, prix relu illisible) s'imprime autrement et se rejoue.
- **Garde de débit**, dans le code : arrêt si la marche projetée dépasse 11,0 h.

**Crédit du loueur** (le code de la course ne contrôle pas le crédit : la règle est tenue par l'opérateur et par ce feu) :

- **avant la création, deux conditions vérifiées par programme au geste 8** (C6) :
  - plancher : crédit ≥ **20,00 USD** (R-2975 ; GO-2026-11-18-03 (2)) ;
  - marge : crédit − 13 × débit horaire des autres instances ≥ **8 + 11 × 1,48 = 24,28 USD** (choix de la mère). Motif : une course saine menée jusqu'à la garde de débit (11 h) au plafond de 1,48 USD/h consomme 16,28 USD ; partie de 24,28 USD hors débit des autres, elle reste au-dessus du plancher de 8 USD du geste 19. La marge est plus sévère que le plancher : à débit des autres nul, il faut 24,28 USD ; avec la relance du témoin de Bailey (≈ 1,22 USD/h), 24,28 + 13 × 1,22 = **40,14 USD**.
  - **Le débit des autres ne compte que les instances à l'état « running »** (point mineur 5) ; le disque des instances arrêtées d'autres sessions n'est pas compté (réserve 10).
  - Le relevé date de moins d'une heure à la création (geste 14). Son heure n'est écrite que sous « CREDIT SUFFISANT », dans le fichier du tour, jamais réécrit.
- **pendant la course**, à chaque suivi horaire (geste 19 (b)) : crédit relevé par la sous-commande `credit` du lanceur de la répétition, qui ne lit que le champ du crédit et n'affiche aucune clé. **Sous 8,00 USD, l'opérateur détruit proprement par l'identifiant et rend compte.** Un arrêt côté loueur perdrait la poussée, donc toute la dépense. Un relevé illisible se refait, trois fois au plus à une minute d'écart (C5) ; trois relevés illisibles : destruction.
- La recharge automatique du loueur (5 USD sous 5 USD) était encore configurée à 05:54Z, contre l'ordre de GO-2026-11-18-07 (R-3196, R-3197). L'opérateur ne compte pas sur elle et ne la déclenche jamais.

**Prix relu après création** (geste 16) :

- C'est la clé `dph_total` de l'instance. Elle a jusqu'ici valu le prix de carte de l'offre plus son stockage (par exemple 1,2547 + 0,0164 ≈ 1,2700 USD/h le 15 novembre).
- Règle : prix relu au-dessus de **1,40 + stockage de l'offre retenue (`stockage_usd_h`, au plus 1,48)** : destruction aussitôt par identifiant, puis nœud. Lecture déclarée : réserve 12.
- Il est écrit **une seule fois**, au geste 16, dans `prix-relu.sh` ; les lectures d'état des gestes 17 et 19 le contrôlent sans jamais l'écrire (C5).

## § 7 — RELANCES ET ÉCHÉANCES

- **Nombre passé à la garde de création : 2**, en onzième argument de la sous-commande `commande`. Ce nombre n'est dérivé d'aucune pièce : la garde ne contrôle que la valeur qu'on lui passe.
- **Motif** : la relance unique de l'accord original est consommée :
  - premier départ perdu sur la garde du pilote, instance 60952525, ≈ 0,10 USD ;
  - relance unique, instance 60953606, ≈ 4,23 h, ≈ 5,14 USD, arrêtée sur le contrôle carte-processeur, aucun score écrit.
  La course de ce feu est la course supplémentaire de GO-2026-11-16-11 : la seconde relance au sens de la garde, et **la dernière course accordée**.
- **Une perte au démarrage la consomme** (pilote, image, clé, journal muet, machine qui ne démarre pas). Après elle, aucune autre course sans un mot neuf de Lazar : la garde refuse toute troisième relance.
- **Un tour neuf n'est pas une course** : tant qu'aucune création n'a été tentée, rejouer les gestes 7 à 14 dans un tour neuf ne consomme rien (§ 10, commande O). Dès qu'une création a été tentée (fichier `t-creation.sh` écrit au geste 14), aucun tour neuf ne s'ouvre ; toute nouvelle tentative est un nœud, dont la mère écrit la forme.
- Trois branches de sortie de courses antérieures existent sur le distant (`calcul/t07bbis-repetition-v1`, `-v2`, `-v4`). Elles ne sont pas ouvertes.
- **Aucune création après le samedi 2026-11-21 à 12:00:00Z** (la garde refuse une relance au-delà ; c'est un nœud, et le billet sort sans l'étape B bis). **Aucune création après 2026-11-22T23:59:59Z** (échéance de l'accord, contrôlée par la garde).
- Échéance dure du programme : le verdict scellé de l'étape B bis est dû au plus tard le dimanche 2026-11-22.

## § 8 — JAMAIS DÉTRUITES PAR CETTE COURSE

- **Règle** : aucune instance n'est détruite par cette course hormis celles dont l'identifiant est écrit par programme au geste 15 dans `a-detruire.txt` : l'instance de la course ; ou, sur une réponse de création sans identifiant non adoptée (geste 15 (b)), les instances portant l'étiquette de la course `bbis-t07-v1` (choix de la mère sur m10). Aucun serveur.
- **Connues à la rédaction de la version 4** (registres, non vérifiées par le rédacteur) :
  - 58936096, 58936099, 58936100 (arrêtées) ;
  - 60988826 (jeu de l'idée du poids du nul, arrêtée, non détruite) ;
  - **61170458** (relance du témoin de Bailey, autre session, en marche ; son repli à 14:00Z est réglé par GO-2026-11-18-09 et GO-2026-11-18-12, hors de cette course) ;
  - le serveur `sauvegarde-temoin-bailey-v2` chez l'hébergeur allemand.
- 61049303 a été détruite le 18 novembre vers 02:38Z. 60480302, 60599797 et 60670453 restent refusées par le code du lanceur (`INSTANCES_D_AUTRES_SESSIONS`), qu'elles existent encore ou non.
- **Témoin de destruction** : une instance de la liste lue au geste 7 du tour, sans l'étiquette de la course, choisie par programme (la première de la liste). Si elle a disparu au geste 23, un témoin neuf est pris par programme dans une liste neuve (geste 23 (b)).

## § 9 — CE QUE L'OPÉRATEUR LIT, ET CE QU'IL NE LIT JAMAIS

- **Liste blanche des entrées de la marche** : point 1 du plan d'analyse du texte scellé (l. 98), tenue par le code. **Liste « Jamais »** : même point. L'ouverture par la chaîne d'un de ces fichiers est un arrêt de la liste d'arrêt (l. 191).
- **L'opérateur lit seulement** :
  - les sorties des gestes de ce feu ;
  - au journal de la machine, les seules lignes `BBIS` d'étapes : minuterie, empreinte de l'amorce, pilote, carte, dépôt, essais du paquet, marche (début et code), poussé, traces, FIN, fin, ARRET, MINUTERIE, REFUS.
- **Il ne lit jamais** :
  - rien sous `diag/`, `runs/` ni `donnees/` ;
  - le contenu d'aucune branche `donnees/` ou `calcul/` (il ne relève que la présence de la branche de sortie, geste 21) ;
  - la réponse brute de la création, qui peut porter la clé propre à l'instance (R-3004) : elle est effacée au geste 15 ;
  - la liste brute des instances, qui peut porter des clés d'autres sessions (R-2829) : chaque lecture l'écrit sous un nom donné par `mktemp` et l'efface aussitôt ;
  - **le contenu des fichiers `.err`** de l'outil du loueur (point mineur 8) : sur un refus d'authentification, la version 1.8.3 y écrit la fin de la clé du loueur. Seule leur taille est affichée ; ils sont effacés au geste 24. Au geste 4 (b), joué sans réseau, aucune authentification n'a lieu : les 400 premiers octets qu'il affiche ne peuvent porter cette fin de clé ;
  - aucune valeur de clé.
- **Pas de `env`, pas de `printenv`.**

---

## § 10 — GESTES NUMÉROTÉS

**Conventions** :

- Chaque appel au shell commence par le **préambule P**, `cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v5/env.sh &&` (sauf les gestes 1, 2, 3 (a), 5 et 21, écrits en entier ; aux gestes 14 et 19 (b), le préambule suit la remise à zéro d'un drapeau de compte rendu, `TENTEE=0;` ou `JOUE=0;`). Il fixe `R`, `C`, `D`, `PYTHON_BBIS` (chemin absolu), `VASTAI_BBIS`, `PATH`, **`TOUR`** (nombre de lignes de `$D/tours.txt`, 0 s'il est absent), **`TD`** (dossier du tour, `$D/tour-$TOUR`), `umask 077` et `set -o pipefail`. Le shell ne garde rien d'un appel à l'autre ; les valeurs passent par des fichiers du dossier d'envoi, écrits par programme, jamais retapés.
- **Une seule liste par appel** (C2) : les contrôles de chaque commande forment une seule chaîne `&&` ; un document en ligne s'ouvre au milieu de la chaîne (`… && cat > f <<'FIN' && …`), son texte suit la ligne de commande. Un contrôle qui échoue arrête tout ce qui le suit dans la chaîne ; seule une ligne de compte rendu explicite peut s'imprimer après (« AUCUNE CREATION TENTEE PAR CET APPEL », « RELEVE NON ECRIT … », « COMMANDE NON IMPRIMEE … », « SUIVI NON JOUE … »).
- Tout fichier est écrit sous un nom neuf (R12) : un nom fixe à l'intérieur d'un dossier de tour neuf, ou un nom donné par `mktemp` pour une lecture répétée. Toute sortie est gardée dans le dossier d'envoi pour le compte rendu.
- **Tours** (C3). Les gestes 7 à 14 forment un tour ; leurs fichiers sont dans le dossier du tour `$TD`. Les gestes 15 à 24 se jouent dans le dossier du tour de la création. Le tour 1 s'ouvre au geste 7 (a). Un tour neuf s'ouvre par la commande O, et seulement pour l'un de ces motifs, recopié entre apostrophes droites à la place de `MOTIF` :
  - `'recherche sans offre retenue'` (geste 9 en échec, ou geste 10 sans candidate acceptée) ;
  - `'plus de 30 minutes depuis la commande'` (geste 14) ;
  - `'plus d une heure depuis le releve du credit'` (geste 14) ;
  - `'mot de la mere R-<numéro>'` (par exemple après un crédit insuffisant suivi d'une recharge).
  Au plus trois tours ; jamais après une création tentée (la commande O le refuse). Au-delà : arrêt et nœud. Un tour neuf rejoue les gestes 7 à 14 dans l'ordre.
- **Lecture sans verdict** (C5). Une liste illisible, une liste incomplète (témoin absent), un prix illisible ou un crédit illisible ne concluent rien : la lecture se refait, trois fois au plus, à une minute d'écart, par l'outil d'attente de la session (jamais une pause muette dans le shell). À la troisième lecture sans verdict : gestes 22 et 23, nœud (au geste 15 (b) : arrêt et nœud, rien n'étant identifié à détruire).
- **Arrêt** veut dire : rien de plus n'est lancé ; si une instance existe, gestes 22 et 23 ; puis compte rendu d'une ligne à la mère.
- Tout refus d'une permission, du crochet (hors le refus attendu du geste 2 (e)) ou du classifieur arrête au premier refus, sans rejeu, reformulation, découpage ni contournement (GO-2026-11-16-06). **Toute demande d'autorisation refusée ou expirée est un arrêt et un nœud**, jamais contournée ni rejouée autrement (point mineur 7).

**Commande O — ouverture d'un tour** (remplacer `MOTIF` par l'un des motifs ci-dessus ; rien d'autre ne change) :
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v5/env.sh && N=$((TOUR + 1)) && test "$N" -le 3 && test -z "$(find "$D" -name t-creation.sh -print -quit)" && mkdir -m 700 "$D/tour-$N" && printf 'tour %s ouvert à %s : %s\n' "$N" "$(date -u +%FT%TZ)" 'MOTIF' >> "$D/tours.txt" && . /home/user/bbis-course-envoi-feu-v5/env.sh && test "$TOUR" = "$N" && test -d "$TD" && echo "TOUR $TOUR OUVERT : $TD" && cat "$D/tours.txt"
```
Attendu : `TOUR <n> OUVERT : /home/user/bbis-course-envoi-feu-v5/tour-<n>`, puis le journal des tours. Rien d'autre : la commande a refusé (quatrième tour, création déjà tentée, dossier déjà présent) ; c'est un arrêt et un nœud.

**Commande L — lecture d'état** (gestes 17 et 19 (a), garde de 12 heures ; n'écrit jamais `prix-relu.sh`) :
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v5/env.sh && test "$TOUR" -ge 1 && . "$TD/instance.sh" && . "$TD/plafond.sh" && . "$TD/temoin.sh" && . "$TD/t-creation.sh" && F=$(mktemp "$TD/liste-etat-XXXXXXXX") && { ( vastai show instances --raw < /dev/null > "$F" 2> "$F.err" ); c=$?; "$PYTHON_BBIS" -I "$D/inventaire_v2.py" course "$F" "$ID" "$PLAFOND_RELU" "$TEMOIN" > "$F.lecture"; k=$?; rm -f -- "$F"; echo "$(date -u +%FT%TZ) ; $(( ($(date +%s) - T_CREATION) / 60 )) minutes depuis la création ; liste : code $c, sortie d'erreur $(wc -c < "$F.err") octets ; inventaire : code $k"; grep -a -E '^(COURSE|VERDICT)' "$F.lecture"; printf '%s | %s | liste %s | inventaire %s | %s\n' "$(date -u +%FT%TZ)" "${F##*/}" "$c" "$k" "$(grep -a '^VERDICT' "$F.lecture" | head -n 1)" >> "$TD/etat.txt"; awk -F' [|] ' '{ if ($NF == "" || $NF ~ /^VERDICT (INCOMPLETE|PRIX_ILLISIBLE|ILLISIBLE)/) n++; else n = 0 } END { printf "lectures sans verdict consécutives : %d (trois au plus)\n", n }' "$TD/etat.txt"; }
```
Sortie : l'heure, les minutes depuis la création, les codes ; la ligne `COURSE <ID> | etat … | prix relu … | etiquette … | carte … | pilote …` ; une ligne `VERDICT` ; le compte des lectures sans verdict consécutives. Les verdicts :
- `VERDICT CONFORME ETAT <état> PRIX <p>` (code 0) : prix relu sous le plafond, étiquette de la course, pilote de série ou absent ;
- `VERDICT HORS_BORNES ETAT <état> (…)` (code 3) : prix relu au-dessus de `PLAFOND_RELU`, autre étiquette, ou pilote hors série : gestes 22 et 23 aussitôt, nœud ;
- `VERDICT ABSENTE (…)` (code 4) : la course manque **et le témoin figure dans la même liste** : gestes 22 et 23, nœud ;
- `VERDICT INCOMPLETE (…)` (code 5 : course et témoin absents), `VERDICT PRIX_ILLISIBLE ETAT <état>` (code 6), `VERDICT ILLISIBLE (…)` (code 2) : lecture sans verdict, refaite selon la convention ci-dessus.

### Phase A — préparatifs, aucun appel au loueur

**Geste 1. Dossier d'envoi neuf et préambule.**
```bash
cd /home/user/controle-ia-travail && test ! -e /home/user/bbis-course-envoi-feu-v5 && mkdir -m 700 /home/user/bbis-course-envoi-feu-v5 && cat > /home/user/bbis-course-envoi-feu-v5/env.sh <<'FIN' && sha256sum /home/user/bbis-course-envoi-feu-v5/env.sh && date -u +%FT%TZ
R=/home/user/controle-ia-travail
C=438a9c5257bdc4fa65f25c42cc89753a049b4586
D=/home/user/bbis-course-envoi-feu-v5
export PYTHON_BBIS=/home/user/controle-ia-travail/.venv/bin/python
export VASTAI_BBIS=/home/user/vastai-env-bbis-feu-v5/bin/vastai
export PATH=/home/user/vastai-env-bbis-feu-v5/bin:$PATH
if [ -f "$D/tours.txt" ]; then TOUR=$(grep -c '' "$D/tours.txt"); else TOUR=0; fi
TD="$D/tour-$TOUR"
umask 077
set -o pipefail
FIN
```
Sortie attendue : `d33b81002735d075bbf5565532a1efed95dc4ba925df65611c3476c11d839f81  /home/user/bbis-course-envoi-feu-v5/env.sh`, puis l'heure.
Arrêt si : le dossier existe déjà (la mère donne un nom neuf, et l'empreinte change), ou si l'empreinte diffère.

**Geste 2. Session de l'opérateur : crochet chargé, compagnon, registre des accords lisible.**
(a) **Relevé seulement** (C1) : `echo "dossier de projet (relevé) : ${CLAUDE_PROJECT_DIR:-vide}"`. La valeur est recopiée au compte rendu ; elle n'arrête rien. Dans une session de sous-agent, cette variable n'est pas exportée au shell même quand le crochet est chargé (constat de la contre-lecture de la version 4).
(b) `cd /home/user/controle-ia-travail/.claude/hooks && sha256sum -c garde_calcul.py.sha256 && sha256sum garde_calcul.py` — attendu `garde_calcul.py: OK`, puis `73be063822531b27e74cf522794cd262495ba21ceea9b62a41ef4a17879a4850  garde_calcul.py`.
(c) Le registre des accords, lu par le lecteur même du crochet, en lecture seule :
```bash
cd /home/user/controle-ia-travail && /home/user/controle-ia-travail/.venv/bin/python -I -c 'import sys; sys.path.insert(0, "/home/user/controle-ia-travail/.claude/hooks"); import garde_calcul as g; r = g.lire_go(g.REGISTRE_GO); x = r["GO-2026-11-14-09"]; print("registre lisible :", len(r), "accords ;", x["type"], x["accorde"], x["echeance"], x["par"])'; echo "code $?"
```
Attendu : `registre lisible : <n> accords ; calcul 2026-11-14 2026-11-22 Lazar` (337 accords au dernier relevé du rédacteur, 07:27Z), puis `code 0`. Jusqu'à 06:41Z le 18 novembre, la sortie était « registre GO mal formé ligne 371 : dates illisibles », code 2 : levé par R-3218 (§ 0, condition 4).
(d) Cas sain : `echo crochet-cas-sain` — attendu `crochet-cas-sain`.
(e) Artefact, **refus attendu et prévu par ce feu** (il ne compte pas comme premier refus ; c'est **la** preuve de comportement que le crochet est chargé) : `echo crochet-artefact ; : pkill` — attendu : un refus du crochet portant « R10 — arrêt par motif de ligne de commande interdit ». La commande est sans effet si elle passe (`:` ne fait rien).
Arrêt si : (b) diffère ; (c) ne rend pas `code 0` ; (e) imprime `crochet-artefact` (crochet non chargé) ; ou tout autre refus. (a) n'est pas un critère d'arrêt.

**Geste 3. Registre des accords lu par la garde ; commit de la course, disque de la session, mesures scellées.**
(a) **Relevé de la garde** (ajout de la mère), par l'interpréteur `python3` de la session, celui qui joue le crochet, avant le préambule :
```bash
cd /home/user/controle-ia-travail && python3 -I -c 'import importlib.util; from pathlib import Path; s = importlib.util.spec_from_file_location("garde_calcul", ".claude/hooks/garde_calcul.py"); g = importlib.util.module_from_spec(s); s.loader.exec_module(g); r = g.lire_go(Path("registres/go.md")); x = r["GO-2026-11-14-09"]; print("registre des accords lu par la garde :", len(r), "accords ; GO-2026-11-14-09", x["type"], x["accorde"], x["echeance"], x["par"])' && echo "REGISTRE DES ACCORDS LISIBLE PAR LA GARDE"
```
Attendu : `registre des accords lu par la garde : <n> accords ; GO-2026-11-14-09 calcul 2026-11-14 2026-11-22 Lazar`, puis `REGISTRE DES ACCORDS LISIBLE PAR LA GARDE`. Sur un registre mal formé, `lire_go` s'arrête (« GARDE (registres/go, R10) — commande bloquée : … », code 2) et la seconde ligne manque : arrêt, rien n'est créé (la garde refuserait toute création).
(b) Commit de la course, fichiers de la session, chaîne, addendum, feu, mesures (points de la version 4, plus le point mineur 1) :
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v5/env.sh && git cat-file -e "$C^{commit}" && git fetch -q origin main && git merge-base --is-ancestor "$C" origin/main && echo "1. commit de la course sur main distant" && git merge-base --is-ancestor 05cd22aa15382f61eb62b9e7817890dde728dd5f "$C" && echo "2. commit de la fiche ancêtre du commit de la course" && git diff --quiet "$C" -- scripts/amorce_bbis_v6.sh scripts/lancer_bbis_v6.sh scripts/lancer_repetition_bbis_v3.sh scripts/repetition_carte_bbis_v3.py src/controle_ia/t07bbis src/controle_ia/gardes.py src/controle_ia/scellement.py src/controle_ia/manifeste.py registres/t07-etape-b-bis-v1.md registres/t07-etape-b-bis-v1-addenda-v1.md registres/t07-etape-b-bis/code-bbis-v1.json registres/t07-etape-b-bis/code-bbis-v2.json registres/t07-etape-b-bis/go-bbis-v2.txt registres/t07-etape-b-bis/epreuve-niveau-deux-plis-bbis-v2.json registres/t07-etape-b-bis/ABSENCE-B-BBIS-v1.json prereg/T0.7-etape-B-bis-v1-addendum-ecart-3-v1.md prereg/T0.7-etape-B-bis-v1-addendum-ecart-3-v1.md.sha256 && echo "3. fichiers lus par la session égaux au commit de la course (registre voisin et compagnon de l'addendum compris)" && test "$(git status --porcelain --untracked-files=all -- src/controle_ia/t07bbis scripts/amorce_bbis_v6.sh scripts/lancer_bbis_v6.sh scripts/lancer_repetition_bbis_v3.sh scripts/repetition_carte_bbis_v3.py | grep -c .)" = 0 && echo "4. fichiers non suivis : 0" && test "$(grep -c 'ADDENDUM-ECART-3-BBIS' registres/t07-etape-b-bis-v1-addenda-v1.md)" = 1 && test "$(grep -c -F '| ADDENDUM-ECART-3-BBIS | 2026-11-18T05:46:36Z | prereg/T0.7-etape-B-bis-v1-addendum-ecart-3-v1.md | e5604cbdce509958e1f3e3bc3a36c8d17a78c8900b5f93a2102fff9b51d07872 |' registres/t07-etape-b-bis-v1-addenda-v1.md)" = 1 && echo "5. ligne ADDENDUM-ECART-3-BBIS du registre voisin : une fois, chemin et empreinte entiers" && ( cd prereg && sha256sum -c T0.7-etape-B-bis-v1-addendum-ecart-3-v1.md.sha256 ) | sed 's/^/6. /' && test "$(grep -c -F -e 26f954e9e9783bf95a5149db9e848e1bd207dc8b027e6027d879363be2dfbbb5 -e 3224ce14dc3fefe7cc46774072f65288a39c3fe760f325e311c5f948c45344b7 prereg/T0.7-etape-B-bis-v1-addendum-ecart-3-v1.md)" = 2 && echo "7. empreintes entières de l'amorce et du lanceur présentes dans l'addendum : 2 lignes" && printf '%s  %s\n' 26f954e9e9783bf95a5149db9e848e1bd207dc8b027e6027d879363be2dfbbb5 scripts/amorce_bbis_v6.sh 3224ce14dc3fefe7cc46774072f65288a39c3fe760f325e311c5f948c45344b7 scripts/lancer_bbis_v6.sh f36571bd7fb7f5693f8e45433f44c7826722b9baf995ce219038923d486b49ca tests/test_chaine_bbis_v6_v1.py e5604cbdce509958e1f3e3bc3a36c8d17a78c8900b5f93a2102fff9b51d07872 prereg/T0.7-etape-B-bis-v1-addendum-ecart-3-v1.md | sha256sum -c | sed 's/^/8. /' && ( cd registres/t07-etape-b-bis && sha256sum -c feu-bbis-v5.txt.sha256 ) | sed 's/^/9. /' && H=$(sha256sum < registres/t07-etape-b-bis/feu-bbis-v5.txt | cut -c1-64) && test "${#H}" = 64 && test "$(grep -c -F "$H" registres/decisions.md)" -ge 1 && echo "10. empreinte du feu $H inscrite au registre des décisions" && cd docs/notes/prealables-course-etape-b-bis-v1 && sha256sum -c mesures-definitives-commit-course-v1.md.sha256 arbitrage-contre-lecture-amorce-v6-v1.md.sha256 repetition-mesure-plancher-py311-py313-v1.md.sha256 | sed 's/^/11. /' && git ls-files --error-unmatch mesures-definitives-commit-course-v1.md > /dev/null && echo "12. compte rendu des mesures suivi par git" && cd mesures-definitives-commit-course-v1 && test "$(for f in *.sha256; do sha256sum -c "$f"; done | grep -c ': OK$')" = 16 && echo "13. seize sorties de mesure conformes à leur compagnon" && echo "GESTE 3 CONFORME"
```
Sortie attendue, dans l'ordre : lignes 1 à 5 ; `6. T0.7-etape-B-bis-v1-addendum-ecart-3-v1.md: OK` ; ligne 7 ; quatre lignes `8. <fichier>: OK` (amorce, lanceur, essais, addendum, comparés sur 64 caractères par `sha256sum -c`) ; `9. feu-bbis-v5.txt: OK` ; `10. empreinte du feu <64 caractères> inscrite au registre des décisions` ; trois lignes `11. <note>: OK` ; lignes 12 et 13 ; `GESTE 3 CONFORME`.
Arrêt si : `GESTE 3 CONFORME` manque (la chaîne s'arrête au premier écart ; la dernière ligne imprimée dit lequel).
Les gestes 3 (a) et (b) se rejouent si plus de deux heures séparent le geste 3 du geste 12 (réserve 14).

**Geste 4. Outil du loueur réinstallé, version inscrite, option `-y` éprouvée sans réseau.**
(a) Installation dans un environnement dédié neuf (réseau des paquets seulement) :
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v5/env.sh && test ! -e /home/user/vastai-env-bbis-feu-v5 && /usr/bin/python3 -m venv /home/user/vastai-env-bbis-feu-v5 && /home/user/vastai-env-bbis-feu-v5/bin/pip install -q --no-cache-dir -r requirements-pilotage.txt && /home/user/vastai-env-bbis-feu-v5/bin/pip show vastai | sed -n 1,2p | tee "$D/g4-outil.txt" && echo "outil appelé : $(command -v vastai)" | tee -a "$D/g4-outil.txt" && for s in "search offers" "show instances" "show user" "destroy instance" "logs"; do "$VASTAI_BBIS" $s --help > /dev/null 2>&1; echo "aide de « $s » : code $?"; done | tee -a "$D/g4-outil.txt" && "$VASTAI_BBIS" destroy instance --help 2>&1 | grep -n -e ' -y' -e '--yes' | tee -a "$D/g4-outil.txt"
```
Attendu :
- `Name: vastai` et `Version: 1.8.3` (version figée par `requirements-pilotage.txt` ; à inscrire au compte rendu) ;
- `outil appelé : /home/user/vastai-env-bbis-feu-v5/bin/vastai` ;
- cinq lignes `code 0` ;
- au moins une ligne d'aide qui nomme `-y` ou `--yes`.

(b) Option `-y` éprouvée sur un cas sain, et sur un artefact, **sans réseau** (`unshare -n -r`). Aucune demande ne peut partir, rien n'est détruit, rien n'est dépensé ; l'identifiant 1 n'est pas une instance du compte.
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v5/env.sh && unshare -n -r "$VASTAI_BBIS" destroy instance 1 -y < /dev/null > "$D/g4-y-sain.txt" 2>&1; echo "cas sain : code $? ; demandes de confirmation : $(grep -c -i -e '\[y/n\]' -e 'y/n' "$D/g4-y-sain.txt")"; unshare -n -r "$VASTAI_BBIS" destroy instance 1 < /dev/null > "$D/g4-y-artefact.txt" 2>&1; echo "artefact : code $? ; demandes de confirmation : $(grep -c -i -e '\[y/n\]' -e 'y/n' "$D/g4-y-artefact.txt")"; head -c 400 "$D/g4-y-sain.txt"; echo; head -c 400 "$D/g4-y-artefact.txt"
```
Attendu :
- cas sain : `demandes de confirmation : 0`, et une erreur de connexion (aucune question posée, demande tentée) ;
- artefact : `demandes de confirmation : 1` ou plus (la version demande une confirmation sans `-y`, défaut de R-2789).
- Si l'artefact ne montre aucune demande, la version ne confirme pas : c'est inscrit, ce n'est pas un arrêt, car la destruction n'est jamais jugée par un code de sortie mais par l'absence prouvée (geste 23).

Arrêt si : l'installation échoue ; la version n'est pas 1.8.3 ; une aide ne rend pas le code 0 ; aucune ligne d'aide ne nomme `-y` ; le cas sain montre une demande de confirmation ; `unshare` est indisponible (l'option n'est alors pas éprouvée : compte rendu, la mère décide).

**Geste 5. Programmes de l'opérateur, écrits par chemin absolu et vérifiés par empreinte** (point mineur 4 : un appel par programme, une seule liste ; un `cd` raté ne peut plus écrire dans le dépôt).
(a) Programme de choix de l'offre (inchangé depuis la version 4) :
```bash
cd /home/user/bbis-course-envoi-feu-v5 && umask 077 && test ! -e /home/user/bbis-course-envoi-feu-v5/choisir_offre.py && cat > /home/user/bbis-course-envoi-feu-v5/choisir_offre.py <<'PY' && sha256sum /home/user/bbis-course-envoi-feu-v5/choisir_offre.py
import json, sys
d = json.load(open(sys.argv[1], encoding="utf-8"))
L = d.get("offers") if isinstance(d, dict) else d
if not isinstance(L, list):
    print("ARRET : sortie de la recherche illisible"); sys.exit(2)
def n(x):
    if isinstance(x, bool):
        return None
    try:
        return float(x)
    except (TypeError, ValueError):
        return None
garde = []
for o in L:
    if not isinstance(o, dict) or isinstance(o.get("id"), bool) or not isinstance(o.get("id"), int):
        continue
    dv = o.get("driver_version")
    pr, st, cu = n(o.get("dph_total")), n(o.get("storage_cost")), n(o.get("cuda_max_good"))
    m = []
    if not (isinstance(dv, str) and (dv.startswith("595.") or dv.startswith("580."))):
        m.append("pilote %r" % (dv,))
    if o.get("gpu_name") != "A100 SXM4" or n(o.get("num_gpus")) != 1 or not (n(o.get("gpu_ram")) or 0) >= 79000:
        m.append("carte")
    if cu is None or cu < 13.0:
        m.append("cuda_max_good %r" % (o.get("cuda_max_good"),))
    if pr is None or not 0 < pr <= 1.40:
        m.append("prix %r" % (o.get("dph_total"),))
    if st is None or st * 150 / 730 > 0.08:
        m.append("stockage %r" % (o.get("storage_cost"),))
    if not (n(o.get("cpu_cores_effective")) or 0) >= 16:
        m.append("coeurs")
    if not (n(o.get("cpu_ram")) or 0) >= 128000:
        m.append("memoire vive")
    if not (n(o.get("disk_space")) or 0) >= 150:
        m.append("disque")
    print("offre %s | prix %s | stockage %s USD/Go/mois | pilote %s | cuda %s | %s" % (
        o["id"], o.get("dph_total"), o.get("storage_cost"), dv, o.get("cuda_max_good"),
        "RETENABLE" if not m else "ecartee : " + ", ".join(m)))
    if not m:
        garde.append((pr, o["id"], dv))
garde.sort()
with open(sys.argv[2], "x", encoding="utf-8") as f:
    f.write("".join("%s %s\n" % (i, dv) for _, i, dv in garde))
print("CANDIDATES %d" % len(garde))
sys.exit(0 if garde else 2)
PY
```
(b) Programme d'inventaire, version 2 (neuf : C5, points mineurs 5 et 10 ; il remplace `inventaire.py` de la version 4) :
```bash
cd /home/user/bbis-course-envoi-feu-v5 && umask 077 && test ! -e /home/user/bbis-course-envoi-feu-v5/inventaire_v2.py && cat > /home/user/bbis-course-envoi-feu-v5/inventaire_v2.py <<'PY' && sha256sum /home/user/bbis-course-envoi-feu-v5/inventaire_v2.py
import json, math, sys
# Inventaire des instances du loueur (projet de feu, version 5). N'imprime jamais une cle.
#   temoin LISTE SORTIE avant|apres     geste 7 (avant) et geste 23 (apres)
#   course LISTE ID PLAFOND TEMOIN      gestes 16, 17, 19, garde de 12 heures
#   etiquette LISTE RECHERCHE OFFRE T_CREATION TEMOIN SORTIE_ID SORTIE_A_DETRUIRE   geste 15
# Codes : 0 conforme ; 2 illisible ; 3 hors bornes ou etiquette deja portee ; 4 absente, temoin present ;
#         5 incomplete, temoin absent ; 6 prix illisible ; 7 non adoptee.
ETIQ = "bbis-t07-v1"
def fin(code, texte):
    print(texte)
    sys.exit(code)
def nombre(x):
    if isinstance(x, bool) or not isinstance(x, (int, float)):
        return None
    x = float(x)
    return x if math.isfinite(x) else None
def texte_nombre(s):
    try:
        x = float(s)
    except (TypeError, ValueError):
        return None
    return x if math.isfinite(x) else None
def prix(i):
    return nombre(i.get("dph_total"))
def serie(dv):
    return isinstance(dv, str) and (dv.startswith("595.") or dv.startswith("580."))
def lire(chemin):
    try:
        with open(chemin, encoding="utf-8") as f:
            d = json.load(f)
    except Exception as e:
        fin(2, "VERDICT ILLISIBLE (liste : %s)" % type(e).__name__)
    L = d.get("instances") if isinstance(d, dict) else d
    if not isinstance(L, list) or any(not isinstance(i, dict) or "id" not in i for i in L):
        fin(2, "VERDICT ILLISIBLE (liste d'objets portant id attendue)")
    for i in L:
        print("instance %s | etiquette %s | etat %s | prix %s" % (i["id"], i.get("label"), i.get("actual_status"), prix(i)))
    return L
a = sys.argv[1:]
if len(a) == 4 and a[0] == "temoin" and a[3] in ("avant", "apres"):
    L = lire(a[1])
    course = [str(i["id"]) for i in L if i.get("label") == ETIQ]
    autres = [i for i in L if i.get("label") != ETIQ]
    debit = 0.0
    for i in autres:
        if i.get("actual_status") == "running":
            p = prix(i)
            debit += p if p is not None else float("nan")
    print("INSTANCES %d ; ETIQUETTE %s : %s ; AUTRES %s ; DEBIT DES AUTRES A L'ETAT running %.4f USD/h (les autres etats ne comptent pas)" % (
        len(L), ETIQ, course, [str(i["id"]) for i in autres], debit))
    if a[3] == "avant" and course:
        fin(3, "ARRET : instance(s) portant deja l'etiquette %s : %s (noeud)" % (ETIQ, course))
    if math.isnan(debit):
        fin(2, "ARRET : prix illisible sur une autre instance a l'etat running")
    if not autres:
        fin(2, "ARRET : aucune autre instance, aucun temoin possible")
    with open(a[2], "x", encoding="utf-8") as f:
        f.write("TEMOIN=%s\nDEBIT_AUTRES=%.4f\n" % (autres[0]["id"], debit))
    fin(0, "TEMOIN %s ECRIT" % autres[0]["id"])
elif len(a) == 5 and a[0] == "course":
    L = lire(a[1])
    ident, temoin, plafond = a[2], a[4], texte_nombre(a[3])
    if plafond is None:
        fin(2, "VERDICT ILLISIBLE (plafond %r)" % a[3])
    vues = [i for i in L if str(i["id"]) == ident]
    if len(vues) > 1:
        fin(2, "VERDICT ILLISIBLE (instance %s en double)" % ident)
    if not vues:
        if temoin in [str(i["id"]) for i in L]:
            fin(4, "VERDICT ABSENTE (course %s absente, temoin %s present dans la meme liste)" % (ident, temoin))
        fin(5, "VERDICT INCOMPLETE (course %s et temoin %s absents de la liste : lecture a refaire)" % (ident, temoin))
    i = vues[0]
    p, dv, st = prix(i), i.get("driver_version"), i.get("actual_status")
    print("COURSE %s | etat %s | prix relu %s | etiquette %s | carte %s | pilote %s" % (
        ident, st, p, i.get("label"), i.get("gpu_name"), dv))
    m = []
    if p is not None and p > plafond:
        m.append("prix relu %r au-dessus de %.4f" % (p, plafond))
    if i.get("label") != ETIQ:
        m.append("etiquette %r" % (i.get("label"),))
    if dv is not None and not serie(dv):
        m.append("pilote %r" % (dv,))
    if m:
        fin(3, "VERDICT HORS_BORNES ETAT %s (%s)" % (st, " ; ".join(m)))
    if p is None:
        fin(6, "VERDICT PRIX_ILLISIBLE ETAT %s (lecture a refaire)" % (st,))
    fin(0, "VERDICT CONFORME ETAT %s PRIX %.4f" % (st, p))
elif len(a) == 8 and a[0] == "etiquette":
    L = lire(a[1])
    recherche, offre, temoin, sortie_id, sortie_liste = a[2], a[3], a[5], a[6], a[7]
    t0 = texte_nombre(a[4])
    if temoin not in [str(i["id"]) for i in L]:
        fin(5, "VERDICT INCOMPLETE (temoin %s absent de la liste : lecture a refaire)" % temoin)
    lab = [i for i in L if i.get("label") == ETIQ]
    print("ETIQUETTE %s : %s" % (ETIQ, [str(i["id"]) for i in lab]))
    machine = None
    try:
        with open(recherche, encoding="utf-8") as f:
            d = json.load(f)
        O = d.get("offers") if isinstance(d, dict) else d
        vues = [o for o in O if isinstance(o, dict) and str(o.get("id")) == offre]
        m0 = vues[0].get("machine_id") if len(vues) == 1 else None
        machine = m0 if isinstance(m0, int) and not isinstance(m0, bool) else None
    except Exception:
        machine = None
    motifs = []
    if len(lab) != 1:
        motifs.append("%d instance(s) portant l'etiquette" % len(lab))
    else:
        sd, mi = nombre(lab[0].get("start_date")), lab[0].get("machine_id")
        if t0 is None:
            motifs.append("heure de la commande du geste 14 illisible")
        if sd is None:
            motifs.append("start_date de l'instance illisible")
        elif t0 is not None and sd < t0 - 120:
            motifs.append("creee avant la commande du geste 14 (start_date %.0f < %.0f - 120 s)" % (sd, t0))
        if machine is None:
            motifs.append("machine de l'offre %s illisible dans la recherche" % offre)
        elif isinstance(mi, bool) or mi != machine:
            motifs.append("autre offre (machine %r de l'instance, %r de l'offre retenue)" % (mi, machine))
    if not motifs:
        with open(sortie_id, "x", encoding="utf-8") as f:
            f.write("ID=%s\n" % lab[0]["id"])
        with open(sortie_liste, "x", encoding="utf-8") as f:
            f.write("%s\n" % lab[0]["id"])
        fin(0, "VERDICT ADOPTEE %s (seule instance de l'etiquette, creee apres la commande du geste 14, sur la machine de l'offre retenue)" % lab[0]["id"])
    with open(sortie_liste, "x", encoding="utf-8") as f:
        f.write("".join("%s\n" % i["id"] for i in lab))
    fin(7, "VERDICT NON_ADOPTEE (%s) ; a detruire : %s" % (" ; ".join(motifs), [str(i["id"]) for i in lab]))
fin(2, "VERDICT ILLISIBLE (usage : temoin LISTE SORTIE avant|apres | course LISTE ID PLAFOND TEMOIN | etiquette LISTE RECHERCHE OFFRE T_CREATION TEMOIN SORTIE_ID SORTIE_A_DETRUIRE)")
PY
```
(c) Lecture de la réponse de création (inchangée depuis la version 4) :
```bash
cd /home/user/bbis-course-envoi-feu-v5 && umask 077 && test ! -e /home/user/bbis-course-envoi-feu-v5/lire_creation.py && cat > /home/user/bbis-course-envoi-feu-v5/lire_creation.py <<'PY' && sha256sum /home/user/bbis-course-envoi-feu-v5/lire_creation.py
import json, sys
try:
    d = json.load(open(sys.argv[1], encoding="utf-8"))
except Exception as e:
    print("CREATION ILLISIBLE (%s)" % type(e).__name__); sys.exit(2)
s = d.get("success") if isinstance(d, dict) else None
c = d.get("new_contract") if isinstance(d, dict) else None
ok = isinstance(c, int) and not isinstance(c, bool) and c > 0
print("success %r ; new_contract %s" % (s, c if ok else "illisible"))
if s is True and ok:
    with open(sys.argv[2], "x", encoding="utf-8") as f:
        f.write("ID=%d\n" % c)
    sys.exit(0)
sys.exit(2)
PY
```
(d) Les trois empreintes, comparées par programme :
```bash
cd /home/user/bbis-course-envoi-feu-v5 && printf '%s  %s\n' 2d32e1ace8f4539f3201997de103a64a9f3d4bba6fc524d008d0a012254b23b4 choisir_offre.py 3e40e35565f6118b0e15a29aca04f0a3bde1b0184955b415a069e3da45143fea inventaire_v2.py 1fa46d02def8602a2bf026d70072535c056c4a23770049b93667aceafce29e09 lire_creation.py | sha256sum -c && echo "TROIS PROGRAMMES CONFORMES"
```
Sortie attendue : `choisir_offre.py: OK`, `inventaire_v2.py: OK`, `lire_creation.py: OK`, `TROIS PROGRAMMES CONFORMES`. Les empreintes : `2d32e1ace8f4539f3201997de103a64a9f3d4bba6fc524d008d0a012254b23b4` (choix, celle de la version 4), `3e40e35565f6118b0e15a29aca04f0a3bde1b0184955b415a069e3da45143fea` (inventaire, neuve), `1fa46d02def8602a2bf026d70072535c056c4a23770049b93667aceafce29e09` (lecture de la création, celle de la version 4).
Arrêt si : une empreinte diffère (le fichier est effacé et réécrit, une fois ; second écart : arrêt).
Le rédacteur a éprouvé l'inventaire version 2 sur des listes fabriquées, cas sains et artefacts (§ 15).

**Geste 6. Répétition à blanc de la commande et de l'égalité des arguments, sur une offre fabriquée — aucune création.**
Les commandes (b) et (c) contiennent le texte d'une ligne de création, que le crochet contrôle ; il peut venir une demande d'autorisation (§ 0, condition 8). Le pilote a son propre dossier, `$D/pilote`, hors des tours.
(a) Commande imprimée pour l'offre fabriquée d'identifiant 1, jamais louée :
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v5/env.sh && mkdir "$D/pilote" && printf '{"carte": "A100 SXM4 80GB", "coeurs": 32.0, "cuda_max_good": 13.2, "disque_go": 150.0, "etiquette": "bbis-t07-v1", "id": 1, "memoire_vive_mo": 257000.0, "prix_usd_h": 1.2, "source": "offre fabriquée du pilote, jamais louée", "stockage_usd_h": 0.03}\n' > "$D/pilote/offre-fabriquee.json" && H=$(sha256sum < registres/t07-etape-b-bis/feu-bbis-v5.txt | cut -c1-64) && test "${#H}" = 64 && ECH=$(( $(date +%s) + 46800 )) && RUN_BBIS=$(date -u +%Y%m%d-%H%M%S)-bbis-t07-v1 && printf 'OFFRE_ID=1\nRUN_BBIS=%s\nECH=%s\nT_COMMANDE=%s\n' "$RUN_BBIS" "$ECH" "$(date +%s)" > "$D/pilote/valeurs.sh" && git fetch -q origin main && bash scripts/lancer_bbis_v6.sh commande "$R" "$D/pilote/offre-fabriquee.json" 1 "$C" main 20261111-151701-t06-reel calcul/t06-confirmation-7b-v1 "$RUN_BBIS" "$ECH" "feu-bbis-v5 $H GO-2026-11-14-09 GO-2026-11-16-11" 2 python:3.11-bookworm > "$D/pilote/commande-imprimee.txt" 2> "$D/pilote/commande.err" && echo "COMMANDE IMPRIMEE : sortie d'erreur $(wc -c < "$D/pilote/commande.err") octets" && sed -n 1p "$D/pilote/commande-imprimee.txt" || { echo "COMMANDE NON IMPRIMEE (refus du lanceur ou chaîne en échec) :"; grep -a 'BBIS REFUS' "$D/pilote/commande-imprimee.txt" 2> /dev/null | cut -c1-300; }
```
Attendu : `COMMANDE IMPRIMEE : sortie d'erreur 0 octets`, puis `BBIS COMMANDE (à jouer par la mère, après le feu écrit ; empreinte de l'amorce 26f954e9e9783bf9) :`. **La ligne imprimée n'est jamais jouée.** Un feu absent ou illisible arrête la chaîne avant le lanceur (son empreinte est exigée sur 64 caractères).
(b) Le geste 13, joué avec `X="$D/pilote"` au lieu de `X="$TD"`. Mêmes sorties attendues, jusqu'à `GESTE 13 CONFORME`.
(c) L'égalité des arguments, avec un outil factice seulement, en une seule liste (C2). Dans un environnement vidé (`env -i`), `vastai` est une fonction qui imprime ses arguments, et les deux jetons sont des valeurs factices. Aucune clé réelle n'est présente, et aucun outil réel n'est sur le chemin :
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v5/env.sh && cd "$D/pilote" && test ! -e ligne-courte.sh && cat > ligne-courte.sh <<'FIN' && env -i PATH=/usr/bin:/bin HF_TOKEN=JETON-FACTICE-HF GH_TOKEN=JETON-FACTICE-GH bash -c 'vastai() { printf "GO_ID=%s\0" "$GO_ID"; printf "%s\0" "$@"; }; . ./valeurs.sh; . ./ligne-imprimee.sh' > argv-imprimee.bin && env -i PATH=/usr/bin:/bin HF_TOKEN=JETON-FACTICE-HF GH_TOKEN=JETON-FACTICE-GH bash -c 'vastai() { printf "GO_ID=%s\0" "$GO_ID"; printf "%s\0" "$@"; }; . ./valeurs.sh; . ./ligne-courte.sh' > argv-courte.bin && cmp argv-courte.bin argv-imprimee.bin && echo "ARGUMENTS EGAUX A LA LIGNE IMPRIMEE" && test "$(tr '\0' '\n' < argv-courte.bin | grep -c -e '-e HF_TOKEN=JETON-FACTICE-HF -e GH_TOKEN=JETON-FACTICE-GH$')" = 1 && echo "CLES PASSEES PAR LEUR NOM (jetons factices substitués en fin de --env)" && tr '\0' '\n' < argv-courte.bin | cut -c1-80 | head -n 22
GO_ID=GO-2026-11-14-09 vastai create instance "$OFFRE_ID" --raw --image python:3.11-bookworm --disk 150 --cancel-unavail --label bbis-t07-v1 --env "-e COMMIT=438a9c5257bdc4fa65f25c42cc89753a049b4586 -e BRANCHE_CODE=main -e RUN_7B=20261111-151701-t06-reel -e BRANCHE_7B=calcul/t06-confirmation-7b-v1 -e RUN_BBIS=$RUN_BBIS -e ECHEANCE_UTC_S=$ECH -e GO_ID=GO-2026-11-14-09 -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$GH_TOKEN" --entrypoint bash --args -c "echo $(cat amorce.b64) | base64 -d > /root/amorce_bbis_v6.sh && bash /root/amorce_bbis_v6.sh"
FIN
```
Attendu : `ARGUMENTS EGAUX A LA LIGNE IMPRIMEE`, `CLES PASSEES PAR LEUR NOM (…)`, puis les arguments, coupés à 80 caractères : `GO_ID=GO-2026-11-14-09`, `create`, `instance`, `1`, `--raw`, …, `-c`, `echo …`. **Les jetons factices n'y paraissent pas** (point mineur 3) : ils sont à la fin de l'argument `--env`, au-delà des 80 caractères ; leur présence là, et là seulement, est comptée par programme, ce qui prouve que la ligne passe les deux clés par leur nom. Aucune vraie clé n'est jamais présente.
Arrêt si : (a) n'imprime pas `COMMANDE IMPRIMEE` ; un « BBIS REFUS » est imprimé ; (b) n'imprime pas `GESTE 13 CONFORME` ; (c) n'imprime pas ses deux lignes. Compte rendu, rien n'est créé. Un refus du lanceur ici aurait arrêté le geste 12 : c'est la raison de cette répétition.

### Phase B — jour de la création (toutes les conditions du § 0 levées, recharge citée par la mère)

**Geste 7. Ouverture du tour et inventaire des instances avec témoin** (premier appel au loueur, en lecture).
(a) Ouverture du tour 1 : la commande O, avec le motif `'premier tour'`. Attendu : `TOUR 1 OUVERT : /home/user/bbis-course-envoi-feu-v5/tour-1`. (Dans un tour neuf ouvert pour un autre motif, (a) est la commande O de ce motif.)
(b) Inventaire :
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v5/env.sh && test "$TOUR" -ge 1 && test ! -e "$TD/temoin.sh" && F=$(mktemp "$TD/liste-g7-XXXXXXXX") && { ( vastai show instances --raw < /dev/null > "$F" 2> "$F.err" ); c=$?; "$PYTHON_BBIS" -I "$D/inventaire_v2.py" temoin "$F" "$TD/temoin.sh" avant > "$F.lecture"; k=$?; rm -f -- "$F"; cat "$F.lecture"; echo "liste : code $c, sortie d'erreur $(wc -c < "$F.err") octets ; inventaire : code $k"; test "$c" = 0 && test "$k" = 0 && cat "$TD/temoin.sh"; }
```
Attendu :
- une ligne par instance (identifiant, étiquette, état, prix ; rien d'autre) ;
- `INSTANCES n ; ETIQUETTE bbis-t07-v1 : [] ; AUTRES [...] ; DEBIT DES AUTRES A L'ETAT running x USD/h (les autres etats ne comptent pas)` ;
- `TEMOIN <identifiant> ECRIT` ; `liste : code 0, … ; inventaire : code 0` ;
- `TEMOIN=<identifiant>` et `DEBIT_AUTRES=<x>`.
La liste brute est effacée aussitôt.
Arrêt si :
- inventaire code 3 : une instance porte déjà l'étiquette `bbis-t07-v1` (point mineur 5 ; nœud) ;
- inventaire code 2 avec « aucune autre instance » (aucun témoin : la preuve d'absence serait impossible ; nœud) ou « prix illisible sur une autre instance à l'état running » ;
- liste illisible ou lecture en échec : lecture sans verdict, refaite selon la convention (le témoin n'est écrit que par une lecture conforme ; chaque lecture a son nom `mktemp`) ; à la troisième : arrêt.

**Geste 8. Crédit relevé — champ 3** (C6 : deux conditions calculées par programme ; heure écrite seulement si le crédit suffit).
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v5/env.sh && test "$TOUR" -ge 1 && test ! -e "$TD/credit-heure.sh" && . "$TD/temoin.sh" && { v=$(bash scripts/lancer_repetition_bbis_v3.sh credit < /dev/null | tee -a "$TD/g8-credit.txt" | sed -n 's/^BBIS REPETITION CREDIT \(-\{0,1\}[0-9][0-9.]*\) USD.*$/\1/p'); t=$(date +%s); echo "crédit relevé « $v » USD à $(date -u -d "@$t" +%FT%TZ) ; débit des autres à l'état running $DEBIT_AUTRES USD/h" | tee -a "$TD/g8-credit.txt"; awk -v v="$v" -v d="$DEBIT_AUTRES" 'BEGIN { s4 = 8 * 10000 + 11 * int(1.48 * 10000 + 0.5); if (v !~ /^-?[0-9]+(\.[0-9]+)?$/ || d !~ /^[0-9]+(\.[0-9]+)?$/) { printf "plancher et marge non calculés : crédit « %s » ou débit « %s » illisible\n", v, d; print "CREDIT INSUFFISANT"; exit 1 } v4 = int(v * 10000 + (v < 0 ? -0.5 : 0.5)); d4 = int(d * 10000 + 0.5); m4 = v4 - 13 * d4; plancher = v4 >= 20 * 10000; marge = m4 >= s4; printf "plancher de 20,00 USD : %s ; marge : %.4f - 13 x %.4f = %.4f USD pour un seuil de 8 + 11 x 1,48 = %.2f USD : %s\n", (plancher ? "tenu" : "NON TENU"), v4 / 10000, d4 / 10000, m4 / 10000, s4 / 10000, (marge ? "tenue" : "NON TENUE"); ok = plancher && marge; print (ok ? "CREDIT SUFFISANT" : "CREDIT INSUFFISANT"); exit !ok }' | tee -a "$TD/g8-credit.txt" && printf 'T_CREDIT=%s\nCREDIT_RELEVE=%s\n' "$t" "$v" > "$TD/credit-heure.sh" && echo "HEURE DU RELEVE ECRITE ($TD/credit-heure.sh)"; } || echo "RELEVE NON ECRIT : aucune création dans ce tour"
```
Attendu :
- `BBIS REPETITION CREDIT <v> USD : suffisant (au moins 4 USD)` ;
- `crédit relevé « <v> » USD à <heure> ; débit des autres à l'état running <d> USD/h` ;
- `plancher de 20,00 USD : tenu ; marge : <v> - 13 x <d> = <m> USD pour un seuil de 8 + 11 x 1,48 = 24.28 USD : tenue` ;
- `CREDIT SUFFISANT` ; `HEURE DU RELEVE ECRITE (…)`.
La mère recopie `<v>`, `<heure>` et le tour au champ 3, à l'engagement.
Arrêt si : `RELEVE NON ECRIT` (lecture du crédit en échec ou illisible, `CREDIT INSUFFISANT`, ou relevé déjà fait dans ce tour). Rien n'est créé ; le relevé est inscrit. Une reprise n'a lieu que dans un tour neuf, sur un mot de la mère (par exemple après une recharge).

**Geste 9. Recherche d'offres** (sortie brute écrite dans un fichier du tour, jamais retapée).
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v5/env.sh && test "$TOUR" -ge 1 && test ! -e "$TD/recherche.json" && ( vastai search offers 'gpu_name=A100_SXM4 num_gpus=1 cpu_cores_effective>=16 cpu_ram>=128 disk_space>=150 cuda_max_good>=13.0' -o 'dph_total' --raw < /dev/null > "$TD/recherche.json" 2> "$TD/recherche.err" ) && echo "RECHERCHE ECRITE" && sha256sum "$TD/recherche.json" || echo "RECHERCHE EN ECHEC (sortie d'erreur : $(wc -c < "$TD/recherche.err" 2> /dev/null) octets)"
```
Attendu : `RECHERCHE ECRITE`, puis l'empreinte du fichier (inscrite).
Arrêt si : `RECHERCHE EN ECHEC`. Rien n'est créé ; un tour neuf est permis (motif « recherche sans offre retenue »).

**Geste 10. Choix de l'offre par programme.**
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v5/env.sh && test "$TOUR" -ge 1 && test ! -e "$TD/candidates.txt" && "$PYTHON_BBIS" -I "$D/choisir_offre.py" "$TD/recherche.json" "$TD/candidates.txt" | tee "$TD/choix.txt" && while read -r id dv; do bash scripts/lancer_bbis_v6.sh offre-depuis-recherche "$TD/recherche.json" "$id" "$TD/offre-$id.json" < /dev/null | tee -a "$TD/choix.txt" && { printf 'OFFRE_ID=%s\nPILOTE=%s\n' "$id" "$dv" > "$TD/offre-retenue.sh"; break; }; done < "$TD/candidates.txt"; test -e "$TD/offre-retenue.sh" && cat "$TD/offre-retenue.sh" || echo "AUCUNE OFFRE RETENUE"
```
Attendu :
- une ligne par offre, `RETENABLE` ou `ecartee : <motifs>` ;
- `CANDIDATES k` (k ≥ 1) ;
- pour la première candidate acceptée par le lanceur : `BBIS OFFRE ECRITE …/offre-<id>.json : offre <id>, A100 SXM4 80GB, <prix ≤ 1,40> USD/h, stockage <≤ 0,08> USD/h, CUDA de l'hôte <≥ 13>` ;
- `OFFRE_ID=<id>` et `PILOTE=595.…` ou `580.…`. Le pilote est recopié tel quel au registre des dépenses.
Arrêt si : `AUCUNE OFFRE RETENUE` (`CANDIDATES 0`, ou aucune candidate acceptée par le lanceur). Rien n'est créé ; un tour neuf est permis (motif « recherche sans offre retenue »).

**Geste 11. Plafond relu et garde de dépense avant la création.**
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v5/env.sh && test "$TOUR" -ge 1 && . "$TD/offre-retenue.sh" && test ! -e "$TD/plafond.sh" && "$PYTHON_BBIS" -I -c 'import json, sys; o = json.load(open(sys.argv[1], encoding="utf-8")); print("PLAFOND_RELU=%.4f" % (1.40 + o["stockage_usd_h"])); print("PRIX_OFFRE=%.4f" % (o["prix_usd_h"] + o["stockage_usd_h"]))' "$TD/offre-$OFFRE_ID.json" > "$TD/plafond.sh" && cat "$TD/plafond.sh" && . "$TD/plafond.sh" && bash scripts/lancer_bbis_v6.sh depense 5.989 "$PRIX_OFFRE" && echo "GARDE DE DEPENSE ACCEPTEE"
```
Attendu : `PLAFOND_RELU=1.4xxx` (au plus 1,48), `PRIX_OFFRE=…`, puis `BBIS DEPENSE {'cumul': 5.989, 'projete': …, 'coupure': 39.5}` et `GARDE DE DEPENSE ACCEPTEE`.
Arrêt si : `GARDE DE DEPENSE ACCEPTEE` manque.

**Geste 12. Échéance, nom du run, commande de création imprimée.**
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v5/env.sh && test "$TOUR" -ge 1 && . "$TD/offre-retenue.sh" && test ! -e "$TD/valeurs.sh" && H=$(sha256sum < registres/t07-etape-b-bis/feu-bbis-v5.txt | cut -c1-64) && test "${#H}" = 64 && ECH=$(( $(date +%s) + 46800 )) && RUN_BBIS=$(date -u +%Y%m%d-%H%M%S)-bbis-t07-v1 && printf 'OFFRE_ID=%s\nRUN_BBIS=%s\nECH=%s\nT_COMMANDE=%s\n' "$OFFRE_ID" "$RUN_BBIS" "$ECH" "$(date +%s)" > "$TD/valeurs.sh" && cat "$TD/valeurs.sh" && echo "échéance de la minuterie : $(date -u -d "@$ECH" +%FT%TZ)" && git fetch -q origin main && bash scripts/lancer_bbis_v6.sh commande "$R" "$TD/offre-$OFFRE_ID.json" "$OFFRE_ID" "$C" main 20261111-151701-t06-reel calcul/t06-confirmation-7b-v1 "$RUN_BBIS" "$ECH" "feu-bbis-v5 $H GO-2026-11-14-09 GO-2026-11-16-11" 2 python:3.11-bookworm > "$TD/commande-imprimee.txt" 2> "$TD/commande.err" && echo "COMMANDE IMPRIMEE : sortie d'erreur $(wc -c < "$TD/commande.err") octets" && sed -n 1p "$TD/commande-imprimee.txt" || { echo "COMMANDE NON IMPRIMEE (refus du lanceur ou chaîne en échec) :"; grep -a 'BBIS REFUS' "$TD/commande-imprimee.txt" 2> /dev/null | cut -c1-300; }
```
Attendu :
- les quatre valeurs ;
- une échéance à 13 heures de l'heure présente ;
- `COMMANDE IMPRIMEE : sortie d'erreur 0 octets` ;
- `BBIS COMMANDE (à jouer par la mère, après le feu écrit ; empreinte de l'amorce 26f954e9e9783bf9) :`.
Le lanceur a alors contrôlé, sans rien créer :
- l'offre et son identifiant ;
- l'image ;
- le prix ≤ 1,40 USD/h ;
- l'amorce en essai local ;
- la garde de création (registre propre, feu portant les deux numéros, deux relances, échéances) ;
- le commit de la fiche ancêtre du commit de la course ;
- le commit de la course joignable sur `main` ;
- la garde d'entrée de la marche rejouée sur l'arbre extrait au commit ;
- la branche de sortie absente.
Arrêt si : `COMMANDE NON IMPRIMEE` (motif « BBIS REFUS » recopié au compte rendu).

**Geste 13. Vérification de la ligne imprimée** (geste B.3 de l'arbitrage, partie qui demande la commande ; tout est jugé par programme, sur 64 caractères ou à l'octet).
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v5/env.sh && X="$TD" && . "$X/valeurs.sh" && test ! -e "$X/ligne-imprimee.sh" && test "$(grep -c '' "$X/commande-imprimee.txt")" = 2 && test "$(grep -c "empreinte de l'amorce 26f954e9e9783bf9) :" "$X/commande-imprimee.txt")" = 1 && sed -n 2p "$X/commande-imprimee.txt" > "$X/ligne-imprimee.sh" && git show "$C:scripts/amorce_bbis_v6.sh" | base64 -w 0 > "$X/amorce.b64" && test "$(base64 -d < "$X/amorce.b64" | sha256sum | cut -c1-64)" = 26f954e9e9783bf95a5149db9e848e1bd207dc8b027e6027d879363be2dfbbb5 && echo "1. amorce lue au commit : empreinte 26f954e9e9783bf95a5149db9e848e1bd207dc8b027e6027d879363be2dfbbb5" && test "$(wc -c < "$X/amorce.b64")" = 41436 && echo "2. base64 de 41436 caractères" && printf 'GO_ID=GO-2026-11-14-09 vastai create instance %s --raw --image python:3.11-bookworm --disk 150 --cancel-unavail --label bbis-t07-v1 --env "-e COMMIT=438a9c5257bdc4fa65f25c42cc89753a049b4586 -e BRANCHE_CODE=main -e RUN_7B=20261111-151701-t06-reel -e BRANCHE_7B=calcul/t06-confirmation-7b-v1 -e RUN_BBIS=%s -e ECHEANCE_UTC_S=%s -e GO_ID=GO-2026-11-14-09 -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$GH_TOKEN" --entrypoint bash --args -c "echo %s | base64 -d > /root/amorce_bbis_v6.sh && bash /root/amorce_bbis_v6.sh"\n' "$OFFRE_ID" "$RUN_BBIS" "$ECH" "$(cat "$X/amorce.b64")" > "$X/ligne-reconstruite.sh" && cmp "$X/ligne-reconstruite.sh" "$X/ligne-imprimee.sh" && echo "3. LIGNE IMPRIMEE EGALE A LA LIGNE RECONSTRUITE" && test "$(grep -o 'echo [A-Za-z0-9+/=]* | base64 -d' "$X/ligne-imprimee.sh" | grep -c '')" = 1 && test "$(grep -o 'echo [A-Za-z0-9+/=]* | base64 -d' "$X/ligne-imprimee.sh" | sed 's/^echo //; s/ | base64 -d$//' | base64 -d | sha256sum | cut -c1-64)" = 26f954e9e9783bf95a5149db9e848e1bd207dc8b027e6027d879363be2dfbbb5 && echo "4. base64 de la ligne imprimée décodé : amorce version 6" && echo "GESTE 13 CONFORME"
```
Sortie attendue :
```
1. amorce lue au commit : empreinte 26f954e9e9783bf95a5149db9e848e1bd207dc8b027e6027d879363be2dfbbb5
2. base64 de 41436 caractères
3. LIGNE IMPRIMEE EGALE A LA LIGNE RECONSTRUITE
4. base64 de la ligne imprimée décodé : amorce version 6
GESTE 13 CONFORME
```
La ligne reconstruite est bâtie indépendamment, depuis les valeurs de ce feu et depuis l'amorce lue au commit. Son égalité à l'octet prouve en une fois :
- l'identifiant de l'offre ;
- l'image `python:3.11-bookworm` ;
- le disque de 150 Go et l'étiquette ;
- le commit et la branche de code `main` ;
- le run et la branche de 7b ;
- le nom du run de la course et l'échéance ;
- le numéro d'accord ;
- **les deux clés passées par leur nom seulement** (`$HF_TOKEN`, `$GH_TOKEN`, jamais une valeur) ;
- l'amorce embarquée, à l'octet.
Le base64 décodé de la ligne imprimée est l'amorce version 6.
Arrêt si : `GESTE 13 CONFORME` manque. Rien n'est créé.

**Geste 14. Création — ligne courte, égalité des arguments, clés par leur nom, une seule liste** (C2).
- **Seul écart de forme permis** : la ligne jouée est la « ligne courte » ci-dessous, et non la ligne imprimée de 41 900 caractères environ. La ligne courte lit l'amorce encodée dans `amorce.b64` (geste 13), et les valeurs dans `valeurs.sh`, écrits par programme dans le dossier du tour. Elle évite ainsi la recopie d'un base64 de 41 436 caractères (réserve R-1 du 16 novembre, « risque de copie »). Son texte est celui de la version 4, à l'octet.
- Le même appel prouve, avant de jouer, que les arguments qu'elle passe à l'outil sont **égaux à l'octet** à ceux de la ligne imprimée. L'épreuve se fait avec un outil factice et des jetons factices, dans un environnement vidé.
- **Tout est une seule liste** : le tour, les deux fenêtres (30 minutes depuis la commande, une heure depuis le relevé du crédit), l'outil du geste 4, l'absence de création tentée et de ligne courte antérieures, l'égalité des arguments, les clés et la création. Un contrôle qui échoue arrête tout ce qui suit ; « CREATION TENTEE » ne s'imprime que si la création a été jouée.
- Le texte de la création est dans l'appel même, dans le document en ligne : le crochet le voit avec son numéro d'accord, et les contrôle au moment de créer.
- Préavis d'une ligne à Lazar, porté par la mère au moment du geste (GO-2026-11-16-06) : « création de la machine de la course de l'étape B bis, offre <id>, <prix> USD/h, échéance <heure> ».
```bash
TENTEE=0; cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v5/env.sh && test "$TOUR" -ge 1 && cd "$TD" && . ./valeurs.sh && . ./credit-heure.sh && test $(( $(date +%s) - T_COMMANDE )) -le 1800 && test $(( $(date +%s) - T_CREDIT )) -le 3600 && test "$(command -v vastai)" = "$VASTAI_BBIS" && test ! -e t-creation.sh && test ! -e ligne-courte.sh && cat > ligne-courte.sh <<'FIN' && env -i PATH=/usr/bin:/bin HF_TOKEN=JETON-FACTICE-HF GH_TOKEN=JETON-FACTICE-GH bash -c 'vastai() { printf "GO_ID=%s\0" "$GO_ID"; printf "%s\0" "$@"; }; . ./valeurs.sh; . ./ligne-imprimee.sh' > argv-imprimee.bin && env -i PATH=/usr/bin:/bin HF_TOKEN=JETON-FACTICE-HF GH_TOKEN=JETON-FACTICE-GH bash -c 'vastai() { printf "GO_ID=%s\0" "$GO_ID"; printf "%s\0" "$@"; }; . ./valeurs.sh; . ./ligne-courte.sh' > argv-courte.bin && cmp argv-courte.bin argv-imprimee.bin && echo "ARGUMENTS EGAUX A LA LIGNE IMPRIMEE" && test "$(tr '\0' '\n' < argv-courte.bin | grep -c -e '-e HF_TOKEN=JETON-FACTICE-HF -e GH_TOKEN=JETON-FACTICE-GH$')" = 1 && echo "CLES PASSEES PAR LEUR NOM (jetons factices substitués en fin de --env)" && export GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN_2" && test -n "$GH_TOKEN" && test -n "${HF_TOKEN:-}" && test -n "${VAST_API_KEY:-}" && echo "trois clés présentes, par leur nom" && printf 'T_CREATION=%s\n' "$(date +%s)" > t-creation.sh && TENTEE=1 && { ( . ./ligne-courte.sh < /dev/null > creation.json 2> creation.err ); echo "CREATION TENTEE : code $? à $(date -u +%FT%TZ) (code non jugé ; réponse lue au geste 15)"; }; [ "$TENTEE" = 1 ] || { echo "AUCUNE CREATION TENTEE PAR CET APPEL"; echo "diagnostic : tour ${TOUR:-?} ; âge de la commande ${T_COMMANDE:+$(( $(date +%s) - T_COMMANDE )) s} ; âge du relevé du crédit ${T_CREDIT:+$(( $(date +%s) - T_CREDIT )) s} ; outil $(command -v vastai) ; ligne courte $(test -e "$TD/ligne-courte.sh" && echo présente || echo absente) ; création déjà tentée dans ce tour $(test -e "$TD/t-creation.sh" && echo oui || echo non)"; }
GO_ID=GO-2026-11-14-09 vastai create instance "$OFFRE_ID" --raw --image python:3.11-bookworm --disk 150 --cancel-unavail --label bbis-t07-v1 --env "-e COMMIT=438a9c5257bdc4fa65f25c42cc89753a049b4586 -e BRANCHE_CODE=main -e RUN_7B=20261111-151701-t06-reel -e BRANCHE_7B=calcul/t06-confirmation-7b-v1 -e RUN_BBIS=$RUN_BBIS -e ECHEANCE_UTC_S=$ECH -e GO_ID=GO-2026-11-14-09 -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$GH_TOKEN" --entrypoint bash --args -c "echo $(cat amorce.b64) | base64 -d > /root/amorce_bbis_v6.sh && bash /root/amorce_bbis_v6.sh"
FIN
```
Attendu : `ARGUMENTS EGAUX A LA LIGNE IMPRIMEE`, `CLES PASSEES PAR LEUR NOM (…)`, `trois clés présentes, par leur nom`, `CREATION TENTEE : code <c> à <heure> (…)`. Le code n'est pas jugé ; la réponse est lue au geste 15. La réponse brute n'est jamais affichée.
Sinon : `AUCUNE CREATION TENTEE PAR CET APPEL` et la ligne de diagnostic. Les lignes imprimées avant elle disent où la chaîne s'est arrêtée. Alors, sans création :
- commande de plus de 30 minutes : tour neuf (motif « plus de 30 minutes depuis la commande »), gestes 7 à 14 ;
- relevé du crédit de plus d'une heure : tour neuf (motif « plus d une heure depuis le releve du credit »), gestes 7 à 14 ;
- outil autre que celui du geste 4, ligne courte déjà présente, création déjà tentée, arguments différents, clé absente : arrêt et nœud ;
- tout refus de permission, du crochet ou du classifieur, toute demande d'autorisation refusée ou expirée : arrêt et nœud.

**Geste 15. Lecture de la création et identifiant de l'instance.**
(a) Lecture de la réponse :
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v5/env.sh && test "$TOUR" -ge 1 && test -e "$TD/t-creation.sh" && test ! -e "$TD/instance.sh" && { "$PYTHON_BBIS" -I "$D/lire_creation.py" "$TD/creation.json" "$TD/instance.sh"; c=$?; rm -f -- "$TD/creation.json"; echo "lecture de la création : code $c ; sortie d'erreur de la création : $(wc -c < "$TD/creation.err") octets"; test "$c" = 0 && . "$TD/instance.sh" && ( set -o noclobber; printf '%s\n' "$ID" > "$TD/a-detruire.txt" ) && echo "INSTANCE DE LA COURSE : ID=$ID (instance.sh et a-detruire.txt)"; }
```
Attendu : `success True ; new_contract <ID>`, `lecture de la création : code 0 ; …`, `INSTANCE DE LA COURSE : ID=<ID> (…)`. La réponse brute est effacée aussitôt : elle peut porter la clé de l'instance. Puis geste 16.
(b) Si la lecture ne rend pas d'identifiant (code autre que 0 : réponse illisible, `success` faux ou identifiant illisible ; cas « créée malgré tout », R-2789) — **adoption par l'étiquette ou chemin de destruction** (choix de la mère sur m10) :
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v5/env.sh && test "$TOUR" -ge 1 && test -e "$TD/t-creation.sh" && test ! -e "$TD/instance.sh" && test ! -e "$TD/a-detruire.txt" && . "$TD/t-creation.sh" && . "$TD/valeurs.sh" && . "$TD/temoin.sh" && F=$(mktemp "$TD/liste-g15-XXXXXXXX") && { ( vastai show instances --raw < /dev/null > "$F" 2> "$F.err" ); c=$?; "$PYTHON_BBIS" -I "$D/inventaire_v2.py" etiquette "$F" "$TD/recherche.json" "$OFFRE_ID" "$T_CREATION" "$TEMOIN" "$TD/instance.sh" "$TD/a-detruire.txt" > "$F.lecture"; k=$?; rm -f -- "$F"; echo "liste : code $c, sortie d'erreur $(wc -c < "$F.err") octets ; inventaire : code $k"; grep -a -E '^(ETIQUETTE|VERDICT)' "$F.lecture"; test -e "$TD/a-detruire.txt" && echo "à détruire : $(tr '\n' ' ' < "$TD/a-detruire.txt")"; }
```
- `VERDICT ADOPTEE <ID> (…)` : **exactement une** instance porte l'étiquette de la course, créée après l'heure de commande du geste 14 (`start_date` au moins `T_CREATION` − 120 s, tolérance d'horloge déclarée, réserve 16), sur la machine de l'offre retenue (`machine_id` égal à celui de l'offre dans la recherche du tour). `instance.sh` et `a-detruire.txt` sont écrits ; puis geste 16, comme sur une réponse lisible.
- `VERDICT NON_ADOPTEE (<motifs>) ; a detruire : [...]` : toute autre configuration (zéro, plusieurs, autre offre, créée avant, clé illisible). Chemin de destruction et de preuve d'absence : gestes 22 et 23 sur chaque identifiant de `a-detruire.txt` ; s'il n'y en a aucun, la lecture elle-même (liste complète, témoin présent, aucune instance de l'étiquette) prouve que rien de la course n'existe. La course est consommée ; nœud, et la mère juge avant tout nouvel essai.
- `VERDICT INCOMPLETE` ou `ILLISIBLE` : lecture sans verdict, refaite selon la convention ; rien n'est écrit. À la troisième : arrêt et nœud (rien d'identifié à détruire ; le rappel de la mère à la création plus 30 minutes prend le relais).

**Geste 16. Relecture de l'instance : prix, étiquette, pilote ; prix relu écrit une seule fois ; heures des rappels de la mère.**
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v5/env.sh && test "$TOUR" -ge 1 && . "$TD/instance.sh" && . "$TD/plafond.sh" && . "$TD/temoin.sh" && . "$TD/t-creation.sh" && . "$TD/valeurs.sh" && F=$(mktemp "$TD/liste-g16-XXXXXXXX") && { ( vastai show instances --raw < /dev/null > "$F" 2> "$F.err" ); c=$?; "$PYTHON_BBIS" -I "$D/inventaire_v2.py" course "$F" "$ID" "$PLAFOND_RELU" "$TEMOIN" > "$F.lecture"; k=$?; rm -f -- "$F"; echo "liste : code $c, sortie d'erreur $(wc -c < "$F.err") octets ; inventaire : code $k"; grep -a -E '^(COURSE|VERDICT)' "$F.lecture"; printf '%s | %s | liste %s | inventaire %s | %s\n' "$(date -u +%FT%TZ)" "${F##*/}" "$c" "$k" "$(grep -a '^VERDICT' "$F.lecture" | head -n 1)" >> "$TD/etat.txt"; awk -F' [|] ' '{ if ($NF == "" || $NF ~ /^VERDICT (INCOMPLETE|PRIX_ILLISIBLE|ILLISIBLE)/) n++; else n = 0 } END { printf "lectures sans verdict consécutives : %d (trois au plus)\n", n }' "$TD/etat.txt"; test "$k" = 0; } && p=$(sed -n 's/^VERDICT CONFORME ETAT [^ ]* PRIX \([0-9][0-9]*\.[0-9]*\)$/\1/p' "$F.lecture") && test -n "$p" && ( set -o noclobber; printf 'PRIX_RELU=%s\n' "$p" > "$TD/prix-relu.sh" ) && echo "PRIX RELU ECRIT UNE FOIS : PRIX_RELU=$p" && echo "RAPPELS DE LA MERE (C7) : création + 30 min = $(date -u -d "@$((T_CREATION + 1800))" +%FT%TZ) ; échéance + 15 min = $(date -u -d "@$((ECH + 900))" +%FT%TZ)"
```
Attendu : `COURSE <ID> | etat … | prix relu <p> | etiquette bbis-t07-v1 | carte A100 SXM4 | pilote 595.… ou 580.…` (le pilote peut manquer sur la fiche de l'instance : ce n'est pas un refus), `VERDICT CONFORME ETAT <état> PRIX <p>`, `PRIX RELU ECRIT UNE FOIS : PRIX_RELU=<p>`, `RAPPELS DE LA MERE (C7) : …`.
Puis la mère inscrit l'**engagement** au registre des dépenses, sous GO-2026-11-14-09. Il porte :
- l'instance, l'offre, le prix relu, le pilote (`PILOTE` du geste 10) ;
- l'échéance, la création, le crédit relevé, le tour et la recharge de Lazar citée (champ 3) ;
- le cumul de la ligne avant la course (5,989 USD) et le pire cas (20,20 USD).
Et elle pose **les deux rappels du filet** (C7, § 5) aux deux heures imprimées.
Arrêt si :
- `VERDICT HORS_BORNES` (code 3 : prix relu au-dessus de 1,40 + stockage de l'offre, étiquette autre, pilote hors série) : gestes 22 et 23 aussitôt, nœud ;
- `VERDICT ABSENTE` (code 4, témoin présent) : gestes 22 et 23, nœud ;
- `VERDICT INCOMPLETE`, `PRIX_ILLISIBLE` ou `ILLISIBLE` : geste 16 refait selon la convention (noms neufs par `mktemp` ; `prix-relu.sh` n'est écrit que par un verdict conforme) ; à la troisième lecture sans verdict : gestes 22 et 23, nœud.

**Geste 17. Attente de l'état « running ».** Toutes les 30 à 60 secondes, au plus 20 minutes après `T_CREATION`, la **commande L** (jamais la commande du geste 16). L'attente se fait par l'outil d'attente de la session, sans pause muette.
- `VERDICT CONFORME ETAT running` : geste 18 aussitôt ;
- `ETAT loading` ou `created` : attendre et relire ;
- lecture sans verdict : convention (trois au plus) ;
- `HORS_BORNES` ou `ABSENTE` : gestes 22 et 23, nœud.
Arrêt si :
- l'état « running » n'est pas lu dans les 20 minutes (la machine ne démarre pas : aucun journal ne viendra, ni l'empreinte ni la minuterie ne peuvent alerter) ;
- ou un état terminal est lu (`exited`, `offline` ou autre que `loading`, `created`, `running`).
Dans les deux cas : gestes 22 et 23, la course est consommée, nœud.

**Geste 18. Lecture du journal dans les cinq minutes qui suivent l'état « running ».**
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v5/env.sh && test "$TOUR" -ge 1 && . "$TD/valeurs.sh" && . "$TD/instance.sh" && J=$(mktemp "$TD/journal-g18-XXXXXXXX") && { ( vastai logs "$ID" < /dev/null > "$J" 2> "$J.err" ); echo "journal : code $? ; sortie d'erreur $(wc -c < "$J.err") octets"; ISO=$(date -u -d "@$ECH" +%FT%TZ); a=$(grep -a -c "BBIS minuterie lancée (PID [0-9][0-9]*, échéance $ISO)" "$J"); b=$(grep -a -c -E 'BBIS amorce v6 : empreinte 26f954e9e9783bf95a5149db9e848e1bd207dc8b027e6027d879363be2dfbbb5([^0-9a-f]|$)' "$J"); p=$(grep -a -c -E 'BBIS CUDA servie par le pilote : [0-9]+\.[0-9]+ \(au moins 13\.0\)' "$J"); r=$(grep -a -c -e 'BBIS REFUS' -e 'BBIS ARRET' "$J"); echo "minuterie $a ; empreinte $b ; pilote $p ; refus ou arrêt $r (attendu : 1 ; 1 ; 1 ; 0)"; test "$a $b $p $r" = "1 1 1 0" && echo "JOURNAL CONFORME" || echo "JOURNAL NON CONFORME A CETTE LECTURE"; grep -a -e 'BBIS minuterie lancée' -e 'BBIS amorce v6' -e 'BBIS CUDA servie' -e 'BBIS carte' -e 'BBIS REFUS' -e 'BBIS ARRET' "$J" | cut -c1-300; }
```
Attendu : `minuterie 1 ; empreinte 1 ; pilote 1 ; refus ou arrêt 0 (…)`, `JOURNAL CONFORME`, et les trois lignes exigées :
- « minuterie lancée (PID …, échéance <l'échéance du geste 12 du tour>) » ;
- « amorce v6 : empreinte » égale aux 64 caractères `26f954e9…dbbb5` ;
- « CUDA servie par le pilote : … (au moins 13.0) ».
Les lignes peuvent tarder de quelques dizaines de secondes. La lecture est refaite (nom neuf par `mktemp`) jusqu'à cinq minutes après l'état « running », pas au-delà. L'opérateur confirme alors à la mère, en une ligne : état « running » et « JOURNAL CONFORME » (le rappel de la mère à la création plus 30 minutes attend cette ligne).
Arrêt si, à cinq minutes, `JOURNAL CONFORME` n'a pas été lu : une ligne manque, apparaît plus d'une fois (conteneur relancé en boucle), une ligne `BBIS REFUS` ou `BBIS ARRET` est lue (toute sortie de l'amorce avant la minuterie), ou la lecture du journal elle-même échoue (réserve 13). Alors : destruction par l'identifiant avec `-y` (geste 22), absence prouvée contre un témoin (geste 23), compte rendu. La course est consommée.

### Phase C — marche

**Geste 19. Suivi horaire** (toutes les heures depuis `T_CREATION`, et avant toute décision).
(a) **Commande L** : état, prix relu, étiquette, pilote, sans écrire `prix-relu.sh`.
(b) Dépense, crédit, journal :
```bash
JOUE=0; cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v5/env.sh && test "$TOUR" -ge 1 && . "$TD/instance.sh" && . "$TD/t-creation.sh" && . "$TD/prix-relu.sh" && case "$PRIX_RELU" in ''|*[!0-9.]*) false;; esac && CUMUL=$(awk -v t="$T_CREATION" -v n="$(date +%s)" -v p="$PRIX_RELU" 'BEGIN { printf "%.3f", 5.989 + (n - t) / 3600 * p }') && JOUE=1 && { echo "$(date -u +%FT%TZ) cumul de la ligne estimé $CUMUL USD (prix relu $PRIX_RELU USD/h)" | tee -a "$TD/suivi.txt"; s=$(bash scripts/lancer_bbis_v6.sh depense "$CUMUL" "$PRIX_RELU" < /dev/null); g=$?; printf '%s\n' "$s" | tee -a "$TD/suivi.txt"; if [ "$g" = 0 ]; then echo "GARDE DE DEPENSE ACCEPTEE"; elif printf '%s\n' "$s" | grep -q "^BBIS : arrêt et destruction par l'identifiant"; then echo "GARDE DE DEPENSE : REFUS AVEC ORDRE DE DESTRUCTION"; else echo "GARDE DE DEPENSE : ECHEC SANS ORDRE (rejouer ce geste)"; fi | tee -a "$TD/suivi.txt"; v=$(bash scripts/lancer_repetition_bbis_v3.sh credit < /dev/null | tee -a "$TD/suivi.txt" | sed -n 's/^BBIS REPETITION CREDIT \(-\{0,1\}[0-9][0-9.]*\) USD.*$/\1/p'); awk -v v="$v" 'BEGIN { if (v !~ /^-?[0-9]+(\.[0-9]+)?$/) print "CREDIT ILLISIBLE (relevé à refaire, trois fois au plus)"; else if (v + 0 >= 8) printf "CREDIT AU-DESSUS DE 8 USD (%s USD)\n", v; else printf "CREDIT SOUS 8 USD (%s USD)\n", v }' | tee -a "$TD/suivi.txt"; J=$(mktemp "$TD/journal-g19-XXXXXXXX") && { ( vastai logs "$ID" < /dev/null > "$J" 2> "$J.err" ); echo "journal : code $? ; sortie d'erreur $(wc -c < "$J.err") octets"; grep -a -e 'BBIS essais du paquet' -e 'BBIS marche' -e 'BBIS poussé' -e 'BBIS traces' -e 'BBIS FIN' -e 'BBIS fin, code' -e 'BBIS ARRET' -e 'BBIS MINUTERIE' "$J" | tail -n 20 | cut -c1-300; }; }; [ "$JOUE" = 1 ] || echo "SUIVI NON JOUE : fichier du tour manquant ou prix relu illisible : arrêt, compte rendu"
```
Attendu :
- (a) `VERDICT CONFORME ETAT running PRIX <p>` ;
- (b) `GARDE DE DEPENSE ACCEPTEE` ; `CREDIT AU-DESSUS DE 8 USD (…)` ; au journal, dans l'ordre : `essais du paquet : code 0, ligne de compte : 151 passed, …` (l'amorce s'arrête elle-même sous 151), `marche : début (run <RUN_BBIS>)`.
Arrêt si :
- `GARDE DE DEPENSE : REFUS AVEC ORDRE DE DESTRUCTION` : destruction par l'ordre qu'elle imprime (gestes 22 et 23). **Seule cette ligne commande la destruction** (point mineur 6) ; `ECHEC SANS ORDRE` fait rejouer (b) ;
- `CREDIT SOUS 8 USD` : destruction propre, gestes 22 et 23, compte rendu : la course est perdue, nœud ;
- `CREDIT ILLISIBLE` : (b) refait selon la convention ; trois relevés illisibles : gestes 22 et 23, nœud ;
- (a) `HORS_BORNES` (prix relu au-dessus de `PLAFOND_RELU`, …) ou `ABSENTE` : gestes 22 et 23, nœud ; lecture sans verdict : convention ;
- `SUIVI NON JOUE` : arrêt, compte rendu (aucun fichier du tour ne doit manquer à ce stade).
**État autre que « running »** en (a) : lire le journal (b) et appliquer le geste 20.
**Heure manquée** : le suivi est rejoué dès que possible et l'écart est inscrit à la minute près au compte rendu. Rien ne permet de laisser filer au-delà de l'échéance de la minuterie.

**Geste 20. Issues lues au journal, et suite** (C4).

| ligne lue au journal | ce que l'opérateur fait |
|---|---|
| « BBIS FIN : marche menée au bout » puis « BBIS fin, code 0 » | gestes 21, 22 et 23 dans les quinze minutes |
| « BBIS ARRET : garde de débit » (code 3 ; relecture et journal poussés, instance arrêtée) | **garde de 12 heures** (ci-dessous), nœud de Lazar (variante (r1) ou (r2)) ; sans mot dans les 12 heures, gestes 22 et 23 |
| « BBIS ARRET : marche : arrêt écrit » (code 4) | gestes 21 (traces, présence seulement), 22 et 23 dans les quinze minutes |
| **résultats restés sur le disque, non poussés** : « BBIS ARRET : poussée « … » impossible » (poussée en échec après ses trois essais), « BBIS ARRET : branche locale de sortie depuis COMMIT … », « BBIS ARRET : ajout « … » », « BBIS ARRET : fichier de plus de … octets … », « BBIS ARRET : commit « … » » | **ne pas détruire tout de suite** : l'instance est arrêtée, les résultats de la marche sont sur son disque, et la minuterie est morte avec le conteneur. Aucun maillon de la chaîne ne donne d'accès à l'instance pour relancer la poussée, et la redémarrer rejouerait l'amorce, qui s'arrêterait (« existe déjà », R12). Donc compte rendu d'une ligne aussitôt : course perdue sauf décision de Lazar, nœud ; **garde de 12 heures** ; puis gestes 22 et 23 sans mot. Rien n'est relancé. |
| **toute autre ligne « BBIS ARRET »** (par exemple « marche : code N (marche.err) », ou un arrêt des étapes 1 à 7 : outil, clé, carte, dépôt, sortie de 7b, fiche, paquets, essais, modèle, branche de sortie, arbre non propre) | geste 21 (présence seulement), puis gestes 22 et 23 dans les quinze minutes |
| aucune ligne « FIN » ni « ARRET », mais un état autre que « running » lu par la commande L (conteneur arrêté hors de l'amorce, par exemple côté loueur) | compte rendu aussitôt ; **garde de 12 heures** ; nœud |
| « BBIS MINUTERIE : échéance atteinte » | geste 23 ; instance encore listée dix minutes après : geste 22, puis 23 |

Plusieurs lignes « BBIS ARRET » (un arrêt suivi d'une poussée de traces impossible, par exemple) : si l'une relève d'une ligne « garde de 12 heures », c'est elle qui s'applique.

**Garde de 12 heures** (point mineur 9) :
- commande L dès l'arrêt lu, puis toutes les heures. État « running » ou « loading » : la demande d'arrêt de l'amorce a échoué (ou le conteneur repart) et la carte facture : **gestes 22 et 23 aussitôt**, nœud. Autre état (« exited », « stopped ») : l'instance est gardée ;
- compte rendu d'une ligne à la mère dès l'arrêt lu (elle le porte à Lazar, et le rappel de l'échéance plus 15 minutes en tient compte, § 5) ;
- 12 heures après l'heure de l'arrêt lue au journal, sans mot de Lazar : gestes 22 et 23 ;
- disque ≤ 0,08 USD/h, soit ≤ 0,96 USD, déjà compté au pire cas (§ 6).

### Phase D — destruction et preuve

**Geste 21. Branche de sortie vue sur le distant** (présence seulement, aucun contenu ouvert).
`cd /home/user/controle-ia-travail && git ls-remote origin refs/heads/donnees/t07-etape-b-bis-v2 | grep -c .`
Attendu : `1`. Un `0` après « FIN » : relire le journal (lignes `poussé`) ; s'il n'y a aucune ligne `poussé`, appliquer la ligne « résultats restés sur le disque » du geste 20.

**Geste 22. Destruction par l'identifiant, avec `-y`** (R10, jamais par motif), pour chaque identifiant de `a-detruire.txt` (geste 15).
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v5/env.sh && test "$TOUR" -ge 1 && test -s "$TD/a-detruire.txt" && while read -r ID; do bash scripts/lancer_bbis_v6.sh detruire "$ID" < /dev/null | tee -a "$TD/destruction.txt" && { GO_ID=GO-2026-11-14-09 vastai destroy instance "$ID" -y < /dev/null >> "$TD/destruction.txt" 2>> "$TD/destruction.err"; echo "DESTRUCTION DE $ID DEMANDEE à $(date -u +%FT%TZ) (code jamais jugé ; geste 23)"; } || echo "DESTRUCTION DE $ID REFUSEE PAR LE LANCEUR : rien n'est détruit, nœud"; done < "$TD/a-detruire.txt"
```
Attendu, pour chaque identifiant : `GO_ID=GO-2026-11-14-09 vastai destroy instance <ID> -y`, la ligne « BBIS PUIS … verifier-destruction », puis `DESTRUCTION DE <ID> DEMANDEE à <heure> (…)`. La commande jouée est celle que le lanceur imprime, l'identifiant étant lu dans `a-detruire.txt` au lieu d'être retapé.
Arrêt si : `DESTRUCTION DE <ID> REFUSEE PAR LE LANCEUR` (identifiant non numérique ou d'une autre session : nœud, rien n'est détruit).

**Geste 23. Absence prouvée contre un témoin**, pour chaque identifiant de `a-detruire.txt`.
(a) Avec le témoin du tour :
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v5/env.sh && test "$TOUR" -ge 1 && test -s "$TD/a-detruire.txt" && . "$TD/temoin.sh" && while read -r ID; do V=$(mktemp "$TD/verification-XXXXXXXX") && { bash scripts/lancer_bbis_v6.sh verifier-destruction "$ID" "$TEMOIN" < /dev/null > "$V"; c=$?; grep -a -e '^BBIS DESTRUCTION PROUVEE' -e '^BBIS ABSENCE NON PROUVEE' -e '^BBIS REFUS' "$V" | cut -c1-300; echo "vérification de $ID contre le témoin $TEMOIN : code $c"; L=$(sed -n 's/^BBIS liste des instances gardée : \(\/[^ ]*\)\/instances\.json$/\1/p' "$V"); case "${L##*/}" in tmp.??????????) rm -rf -- "$L" && echo "liste brute effacée";; esac; }; done < "$TD/a-detruire.txt"
```
Attendu : `BBIS DESTRUCTION PROUVEE <ID> : absente de la liste, témoin <TEMOIN> présent, n instance(s) listée(s)`, `vérification de <ID> contre le témoin <TEMOIN> : code 0`, `liste brute effacée`. (La liste brute du lanceur est effacée par le nom de son dossier jetable, `tmp.` suivi de dix caractères, où qu'il soit.)
(b) Si le témoin a disparu (« témoin … absent de la liste ») : témoin neuf, choisi par programme dans une liste neuve, puis vérification avec lui, dans le même appel :
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v5/env.sh && test "$TOUR" -ge 1 && test -s "$TD/a-detruire.txt" && NT="$TD/temoin-g23-$(date -u +%Y%m%dT%H%M%S).sh" && F=$(mktemp "$TD/liste-g23-XXXXXXXX") && { ( vastai show instances --raw < /dev/null > "$F" 2> "$F.err" ); "$PYTHON_BBIS" -I "$D/inventaire_v2.py" temoin "$F" "$NT" apres > "$F.lecture"; k=$?; rm -f -- "$F"; grep -a -E '^(INSTANCES|TEMOIN|ARRET|VERDICT)' "$F.lecture"; test "$k" = 0; } && . "$NT" && while read -r ID; do V=$(mktemp "$TD/verification-XXXXXXXX") && { bash scripts/lancer_bbis_v6.sh verifier-destruction "$ID" "$TEMOIN" < /dev/null > "$V"; c=$?; grep -a -e '^BBIS DESTRUCTION PROUVEE' -e '^BBIS ABSENCE NON PROUVEE' -e '^BBIS REFUS' "$V" | cut -c1-300; echo "vérification de $ID contre le témoin neuf $TEMOIN : code $c"; L=$(sed -n 's/^BBIS liste des instances gardée : \(\/[^ ]*\)\/instances\.json$/\1/p' "$V"); case "${L##*/}" in tmp.??????????) rm -rf -- "$L" && echo "liste brute effacée";; esac; }; done < "$TD/a-detruire.txt"
```
Si l'instance est toujours listée : geste 22 une fois de plus, puis 23.
« Absence non prouvée » une seconde fois : arrêt, compte rendu, nœud ; l'instance est signalée comme vivante.

**Geste 24. Inscriptions, effacement des sorties d'erreur, compte rendu.**
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v5/env.sh && find "$D" -type f -name '*.err' -print -delete | sed 's/^/sortie d erreur effacée : /'; echo "listes brutes ou réponse de création restantes (attendu : aucune) :"; find "$D" -type f \( -name 'creation.json' -o \( -name 'liste-*' ! -name '*.err' ! -name '*.lecture' \) \) -print
```
- Au registre des arrêts : l'instance, l'heure de destruction et l'absence prouvée (témoin).
- Au registre des dépenses : le prix relu, la durée (destruction moins `T_CREATION`), la dépense (durée × prix relu), le nouveau cumul de la ligne, le pilote, le crédit avant et après (geste 19, dernière ligne).
- Compte rendu de l'opérateur à la mère : une ligne par événement ; tours ouverts et leurs motifs (`tours.txt`) ; versions et empreintes des gestes 1, 3, 4 et 5 ; les sorties gardées dans le dossier d'envoi. Aucune mesure, aucun score, aucune aire.
- Après : seuls les fichiers non secrets restent dans le dossier d'envoi. `creation.json` et les listes brutes ont été effacés à leur lecture ; les fichiers `.err` sont effacés ici (point mineur 8).

---

## § 11 — CE QUI ARRÊTE TOUT, SANS REJEU, SANS REFORMULATION, SANS CONTOURNEMENT

- Refus d'une permission, du crochet (hors le refus attendu du geste 2 (e)) ou du classifieur : arrêt au premier refus, compte rendu en une ligne, rien de relancé.
- **Demande d'autorisation refusée ou expirée : arrêt et nœud**, jamais contournée ni rejouée autrement (point mineur 7).
- Registre des accords illisible par le crochet (geste 2 (c), geste 3 (a)) : rien n'est créé.
- Refus du lanceur sur l'offre, l'image, le prix, la branche de sortie, l'ancêtre, le commit joignable, le commit de la course, le registre ou la garde de création : arrêt.
- Une empreinte de la chaîne, de l'addendum ou du feu différente sur 64 caractères ; la ligne imprimée différente de la ligne reconstruite ; le base64 décodé différent de `26f954e9…dbbb5` ; les arguments de la ligne courte différents de ceux de la ligne imprimée : arrêt, rien n'est créé.
- Aucune offre de pilote 595 ou 580 sous 1,40 USD/h acceptée par le lanceur : rien n'est créé (un tour neuf est permis pour ce motif, dans la limite de trois tours).
- **Crédit sous 20,00 USD, ou marge « crédit − 13 × débit des autres ≥ 24,28 USD » non tenue** avant la création (C6) ; relevé de plus d'une heure : rien n'est créé.
- Quatrième tour, ou tour neuf après une création tentée : refusés par la commande O ; arrêt et nœud.
- Prix relu au-dessus de 1,40 + stockage de l'offre : destruction aussitôt, nœud.
- Pas d'état « running » en 20 minutes, ou état terminal : destruction, nœud.
- Journal sans « JOURNAL CONFORME » dans les cinq minutes (ligne manquante ou répétée, ligne `REFUS` ou `ARRET`, lecture du journal en échec) : destruction, absence prouvée, compte rendu.
- **Trois lectures sans verdict** consécutives (liste illisible ou incomplète, prix ou crédit illisible) : destruction, nœud (avant toute création, au geste 7 : arrêt ; au geste 15 (b) : arrêt et nœud, rien d'identifié à détruire) ; une seule lecture sans verdict ne détruit jamais rien (C5).
- Garde de dépense déclenchée (refus avec ordre imprimé) : destruction par la commande qu'elle imprime.
- Crédit sous 8,00 USD pendant la course : destruction propre, compte rendu.
- Garde de débit déclenchée : instance arrêtée par l'amorce, garde de 12 heures, nœud de Lazar, puis destruction.
- Résultats restés sur le disque (poussée impossible, branche locale, ajout, fichier trop gros, commit) : garde de 12 heures, nœud ; rien n'est relancé.
- Instance gardée 12 heures relue « running » ou « loading » : destruction aussitôt (point mineur 9).
- Réponse de création sans identifiant non adoptée par l'étiquette : destruction des instances de l'étiquette, absence prouvée, nœud (point mineur 10).
- Échéance de la minuterie atteinte : absence vérifiée, destruction par la session si besoin.
- Portillon des 151 essais non franchi sur la machine : l'amorce s'arrête à son étape 5 ; destruction.
- Contrôle du pilote de la carte en échec : arrêt avant l'installation des paquets ; destruction.
- Arrêts de la liste d'arrêt du texte scellé, lue sous le texte, ses deux addenda et le troisième addendum : contrôle d'identité à dose 0, artefact non vu à dose 1, chemin de l'état imposé, texte décodé ou clé différents, garde d'équivalence de la série d'origine, contrôle carte-processeur au-delà de 10⁻⁴ à 3 époques, déterminisme au bit près non tenu à 300 époques sur la carte, tâche du pli lu dans un apprentissage, moyenne ou médiane sur les jetons, aire ou résumé de score écrit sur l'instance, ouverture d'un fichier de la liste « Jamais ».
- Absence de destruction non prouvée deux fois : arrêt, compte rendu, nœud.
- Création après le 2026-11-21 à 12:00:00Z, ou après le 2026-11-22 à 23:59:59Z : nœud, rien n'est créé.
- Toute instance ou tout serveur de ce programme sans tâche en cours : arrêté par son identifiant, consigné au registre des arrêts.

## § 12 — APRÈS LA COURSE

- Destruction explicite par l'identifiant numérique, avec `-y`, dans les quinze minutes qui suivent la fin ou l'arrêt (hors garde de 12 heures). Puis absence prouvée contre un témoin, puis inscriptions (geste 24).
- La session de la course ne lit aucune mesure, aucun score, aucune aire. La lecture se fait sur processeur, par un lecteur neuf, sur le plan scellé. Ce lecteur n'a lu ni le verdict de l'étape B ni son fichier de lecture avant de sceller le sien. Le fichier de lecture de l'étape B n'entre qu'après les deux verdicts, pour la seule table conjointe.
- Avant cette lecture (et non avant la course) : la preuve d'antériorité, rejouée depuis un clone à histoire complète et inscrite à part ; le journal des ouvertures du registre propre, créé.
- La mère inscrit `SCORES-BBIS` au registre propre, d'après la ligne « FIN » du journal (chemin seulement).
- Verdict prononcé par un sous-agent neuf, ni auteur du préenregistrement ni de l'analyse. Il cite les trois lignes `ADDENDUM-ECART-1-BBIS`, `-2-BBIS` et `-3-BBIS`, sous peine de n'être pas scellé, et porte les réserves nommées du § 13 (1 à 5). Puis il est soumis à Lazar.

## § 13 — RÉSERVES

**Réserves nommées, à porter au verdict** :

1. **Plafond de prix** : tenu par le lanceur version 6 (hors de la fiche de code) **et** par l'opérateur. Cela va contre la lettre de GO-2026-11-18-03 (3) ; c'est couvert par GO-2026-11-18-07 (champ 2). Le verdict dit que ce plafond tenait au lanceur et à l'opérateur, non au code de la fiche.
2. **Prédiction perdue** : la prédiction écrite avant la course, qui s'appuyait sur la reprise de l'entropie, a perdu son appui (GO-2026-11-18-03 (1), TA-3).
3. **Épreuve de niveau rejouée** après la course du 16 novembre : la clause « lue avant toute ouverture de données de 7b » n'est pas tenue à la lettre. L'épreuve n'a lu que des données fabriquées, et le niveau reste 0,99 (troisième addendum).
4. **Image** exigée par son nom, non par un condensé : le contenu servi sous ce nom peut changer.
5. **Amorce embarquée** de 41 436 caractères en base64, taille jamais éprouvée chez le loueur. La lecture du journal (geste 18) la couvre, mais une perte consomme la dernière course.

**Réserves d'exécution** :

6. **Plancher à marge nulle** : 151 passés pour un plancher de 151. Le Python 3.11 de l'image peut ne pas être 3.11.18, et les dépendances non figées de `requirements-gpu.txt` seront résolues de nouveau sur la machine. Rien n'a tourné sur une carte dans les mesures.
7. **Pilote de série 580** : permis par l'arbitrage, jamais éprouvé sur une vraie machine de cette chaîne. Seule la série 595 l'a été.
8. **Ligne courte** (geste 14) : c'est le seul écart de forme à la ligne imprimée, prouvé avant de jouer par l'égalité à l'octet des arguments, et contrôlé par le crochet. Si la mère préfère la ligne imprimée elle-même, elle remplace la ligne courte du geste 14 par une recopie de `ligne-imprimee.sh` dans le document en ligne, suivie de `cmp` avec `ligne-imprimee.sh` dans la même liste ; elle accepte alors une recopie de près de 41 900 caractères.
9. **Preuve de chargement du crochet** (C1) : c'est le refus volontaire du geste 2 (e), prévu par ce feu, qui ne compte pas comme le « premier refus » de GO-2026-11-16-06. Le relevé (a) n'en est pas une : dans une session de sous-agent, `CLAUDE_PROJECT_DIR` n'est pas exportée au shell même quand le crochet est chargé. Si la mère n'admet pas ce refus volontaire, il ne reste que le refus réel que le crochet opposerait à une commande de création sans accord, preuve que ce feu n'exige pas.
10. **Conditions de crédit** (§ 6, geste 8 ; choix de la mère sur C6) : la marge « crédit − 13 × débit des autres ≥ 24,28 USD » est plus sévère que GO-2026-11-18-03 (2) ; elle peut retarder la course tant qu'une autre instance tourne (40,14 USD avec la relance du témoin de Bailey). Elle couvre une course saine jusqu'à la garde de débit (11 h), non les 13 h de la minuterie (il faudrait 27,24 USD) : une marche au-delà de 11 h est exclue par la garde de débit. Elle ne compte ni le disque des instances arrêtées d'autres sessions (non mesuré), ni une instance lancée après le geste 7 ; le relevé horaire du geste 19 (plancher de 8 USD) les rattrape. À 20 USD exactement, sans la marge, une course saine de plus de 8,1 heures aurait été détruite par le plancher de 8 USD : c'est la raison de la marge.
11. **Recharge automatique** encore configurée chez le loueur à 05:54Z, contre l'ordre de GO-2026-11-18-07 (R-3196, R-3197) : une recharge peut survenir pendant la course. L'opérateur ne la compte pas et ne la déclenche pas.
12. **Lecture du prix relu** : le plafond de 1,40 porte sur la carte. Le prix relu de l'instance comprenant jusqu'ici le stockage, la borne relue est 1,40 + stockage de l'offre retenue, au plus 1,48. Une lecture à la lettre (« relu au-dessus de 1,40 : destruction ») détruirait une machine saine à 1,38 + 0,03.
13. **Outil du loueur et clés de ses réponses** : le comportement réel de l'outil 1.8.3 (forme des réponses, `-y`, journal, crédit, instances) n'a jamais été vu par le rédacteur, faute d'accès au loueur ; le geste 4 vérifie les aides et `-y`. Une clé absente de la recherche écarte l'offre, sans rien deviner. **La sous-commande `logs` n'a jamais servi dans cette chaîne** ; un échec de la lecture du journal ne se distingue pas d'une ligne absente et mène, à cinq minutes, à la destruction (point mineur 11). **Les clés `start_date` et `machine_id`** (adoption du geste 15 (b)) n'ont jamais été lues sur une instance par cette chaîne : absentes ou d'une autre forme, il n'y a pas d'adoption, et le chemin de destruction s'applique. Sur un refus d'authentification, l'outil 1.8.3 écrit la fin de la clé du loueur sur sa sortie d'erreur : les fichiers `.err` ne sont jamais affichés (point mineur 8).
14. **Fichiers lus sur le disque par la session** : le lanceur, ses gardes et le registre propre sont lus dans l'arbre de travail, non au commit. Le geste 3 prouve qu'ils sont égaux au commit de la course. `main` avance plusieurs fois par heure : le geste 3 se rejoue si plus de deux heures séparent le geste 3 du geste 12.
15. **Pire cas et minuterie** (C7) : les pires cas du § 6 supposent la minuterie armée. Avant la ligne « minuterie lancée », la dépense n'est bornée que par l'opérateur vivant et par le filet de la mère (rappel à la création plus 30 minutes).
16. **Adoption par l'étiquette** (choix de la mère sur m10) : « créée après la commande du geste 14 » est lu avec une tolérance de 120 secondes (`start_date` ≥ `T_CREATION` − 120 s), pour un écart d'horloge entre la session et le loueur ; une autre instance portant l'étiquette de la course, créée dans ces deux minutes sur la même machine, n'est pas plausible (aucune n'existait au geste 7 du tour). La mère peut exiger la lettre stricte (tolérance nulle) avant de sceller ; le chemin de destruction s'appliquerait alors à une machine saine dès que l'horloge de la session avancerait, même d'une seconde, sur celle du loueur.
17. **Tours** (C3) : la mécanique des tours (dossier par tour, commande O, journal `tours.txt`) n'a jamais tourné chez le loueur ; elle a été rejouée sur des analogues sans effet (§ 15).
18. **Ce qui n'a pas été rejoué** : voir § 15. En particulier, aucune commande n'a été jouée contre le loueur, et les demandes d'autorisation que déclencheront les gestes 6, 13 et 14 n'ont pas été vues.

## § 14 — CORRESPONDANCE AVEC LES PIÈCES ANTÉRIEURES

La correspondance avec la contre-lecture de la version 4 est en tête de ce texte. Celles de la version 4 restent vraies, avec ces renvois :

**Les onze corrections de la contre-lecture du projet version 3** :

| correction | où elle est portée |
|---|---|
| 1. écart double (entropie, épreuve épinglée) | § 3 ; couvert par TA-3 à TA-5 du troisième addendum ; § 13, 2 et 3 |
| 2. plafond jouable, sous-commande `offre` de la répétition interdite | § 5 ; gestes 10, 12 et 16 ; plafond aussi dans le lanceur version 6 |
| 3. pire cas avec le stockage et le disque après arrêt de débit | § 6 : 19,24 et 20,20 USD ; cumul pire 26,19 USD |
| 4. crédit surveillé pendant la course, plancher de 8 USD | § 6 ; geste 19 (b) ; § 11 |
| 5. poussée impossible | geste 20 (ligne « résultats restés sur le disque ») ; § 11 |
| 6. ligne « minuterie lancée » lue | geste 18 |
| 7. image relue | contrôlée par programme (geste 13) et par le lanceur version 6 |
| 8. nœud de la recharge | tranché par GO-2026-11-18-03 (2) ; § 0 |
| 9. portillon sur un environnement installé | mesures définitives, Python 3.13 et 3.11 (§ 3) |
| 10. compagnon du crochet | présent, vérifié au geste 2 (b) |
| 11. étiquette de la répétition désalignée | sans effet : le lanceur de la répétition ne sert qu'à sa sous-commande `credit`, en lecture ; il ne crée rien |
| section C, renvoi au point 1 du plan | § 9 |
| section D, cas non dits | geste 17 (machine qui ne démarre pas), geste 19 (heure manquée), § 5 (minuterie et garde de débit) |

**« Ce qui doit aller au feu version 4 » (arbitrage)** :

| point | où il est porté |
|---|---|
| 1. chaîne version 6, empreintes entières, lanceur depuis la racine avec `PYTHON_BBIS` | § 3 ; geste 3 (b) ; préambule (chemin absolu) |
| 2. commit de la course, branche `main`, mesures scellées, code hors de la fiche | § 3 ; gestes 3 (b) et 12 |
| 3. offre par programme, pilote 595 ou 580, `cuda_max_good` ≥ 13.0, carte ≤ 1,40, stockage ≤ 0,08, image | § 5 ; gestes 9, 10 et 13 |
| 4. échéance par commande à 13 heures, refaite après 30 minutes ; pire cas avec le stockage ; cumul de la ligne | § 5, § 6 ; gestes 12 et 14, commande O |
| 5. clés par leur nom, accord cité | § 0, champ 1 (GO-2026-11-18-06) ; gestes 6 (c), 13 et 14 |
| 6. crédit ≥ 20 USD dans l'heure ; outil réinstallé, `-y` éprouvée | § 0, champ 3 ; gestes 4, 8 et 14 |
| 7. journal dans les cinq minutes, trois lignes, sinon destruction et absence prouvée | geste 18 |
| 8. deux relances, dernière course, perte au démarrage consommée | § 7 |
| 9. plancher 151 partout | § 3 ; § 11 ; geste 19 |
| 10. réserves (plafond au lanceur, image par son nom, base64 de 41 436 caractères) | § 13, 1, 4 et 5 |

## § 15 — RÉDACTION, ESSAIS SUR ANALOGUES, LIMITES

- **Rédaction** : sous-agent de la session mère, 2026-11-18, de 07:01:23Z à 07:35:52Z (`date -u`).
  - Processeur seulement. Aucune machine, aucune dépense, aucun appel au loueur ni à l'hébergeur, aucune clé lue ni affichée, aucun commit, aucune poussée. Le distant n'a été lu qu'en lecture seule : `git fetch` de `main`, et les `git ls-remote` du lanceur, dans les analogues des gestes 3 (b), 6 (a) et 12.
  - Rien d'ouvert sous `diag/`, `runs/` ni `donnees/`, aucune branche de données ni de calcul ouverte (le lanceur n'a fait que constater l'absence de la branche de sortie par `git ls-remote`), aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni du premier test boîte blanche bis.
  - Lus : le projet version 4 et sa contre-lecture (empreintes vérifiées), l'arbitrage (§ B et « Ce qui doit aller au feu version 4 »), le § 6 du troisième addendum, le lanceur et l'amorce version 6, le lanceur de la répétition (sous-commande `credit`), `registre_bbis_v2.py` (garde de création, de dépense, d'absence), le crochet de garde et `.claude/settings.json`, les lignes citées des registres des accords et des décisions.
  - Le refus du crochet que décrivait la version 4 (registre illisible) est levé : R-3218.
- **Essais sur analogues sans effet** (dossier du bloc-notes `/tmp/claude-0/-home-user-controle-ia-travail/8282ab93-0983-5813-b791-a7a522157dcd/scratchpad/feu-v5-essais/`, effaçable ; aucune pièce du dépôt écrite ; sortie du dernier jeu `essai-final.txt`, `b0e70abb27b8bf945a5f50472855962536fa855d8b362bae79ca5a72e1287b17`) :
  - **Méthode.** Les 31 blocs de commandes de ce texte sont tirés par programme, jamais retapés. Substitutions déclarées, et elles seules : dossier d'envoi et outil vers le bloc-notes ; dans les lignes de création et dans la fonction factice, le nom de l'outil du loueur remplacé par celui d'un outil factice (`outil_factice`), le même remplacement étant fait dans la ligne imprimée par le lanceur avant le geste 13 ; feu, compagnon et registre des décisions remplacés par un substitut. Environnement vidé avec des jetons factices ; faux outil du loueur local, sans réseau ni clé, qui lit et écrit un état fabriqué (liste, crédit, recherche, réponse de création, journal) ; dossiers temporaires du lanceur dans le bloc-notes. Les vrais lanceurs de la course et de la répétition sont joués depuis la racine du dépôt (`commande`, `offre-depuis-recherche`, `depense`, `detruire`, `verifier-destruction`, `credit`). Les gestes qui lisent le distant (3 (b), 6 (a), 12) ont tourné dans l'environnement de la session privé de toute variable dont le nom désigne une clé (retirées par leur nom, jamais lues).
  - **Résultats** (dernier jeu, 2026-11-18 vers 07:33Z) : **162 vérifications, toutes conformes** — préparatifs et pilote (11), chemin sain jusqu'à la preuve d'absence (42), fenêtres du geste 14 (17), tours (30), adoption par l'étiquette, chemin de destruction et témoin neuf (40), conditions de crédit (8), programme d'inventaire (14). Avant elles : 31 blocs sans faute de syntaxe ; programmes de choix de l'offre et de lecture de la création, ligne courte et gabarit du geste 13 égaux à l'octet à ceux de la version 4 ; empreintes du préambule (`d33b8100…`) et de l'inventaire (`3e40e355…`) calculées par extraction ; gabarit du geste 13 rempli par un second programme, égal à l'octet à la ligne imprimée par le lanceur, sans substitution.
  - **Rejoué, et ce que cela montre** :
    - C1 : dans la session du rédacteur, autre sous-agent, `${CLAUDE_PROJECT_DIR:-vide}` rend `vide` (07:31Z) alors que le crochet est chargé (il a refusé une commande, ci-dessous).
    - C2 : au geste 14, une commande de plus de 30 minutes, un relevé de plus d'une heure, une clé absente, puis une ligne courte déjà écrite : aucune création, rien après le contrôle, « AUCUNE CREATION TENTEE PAR CET APPEL » et le diagnostic. **Témoin du défaut** : la forme de la version 4, jouée sur le même analogue avec une fenêtre dépassée et la ligne courte présente, crée la machine factice. Geste 6 (c) rejoué : rien ne suit son contrôle.
    - C3 : trois tours ouverts, le quatrième refusé ; aucun tour après une création tentée ; tour 2 après une fenêtre dépassée : gestes 7 à 14 dans un dossier neuf, création, gestes 15 et 16 sur les fichiers du tour 2 ; le geste 18 refuse l'échéance du tour 1 et accepte celle du tour 2.
    - C5 : commande L sur une liste vide (incomplète), sur une lecture en échec (illisible), compteur 1 puis 2, remis à 0 par un verdict ; absente avec témoin présent ; prix illisible ; prix au-dessus du plafond ; pilote 615 ; autre étiquette. `prix-relu.sh` inchangé (empreinte) après toutes ces lectures, après le suivi et après un second geste 16. Crédit illisible, à 7,50 et à −2,19 USD au geste 19.
    - C6 : 40,14 USD avec 1,22 USD/h d'autres instances (égalité exacte) : suffisant ; 40,13 : insuffisant ; 24,28 et 24,27 sans autre instance : suffisant, insuffisant ; 19,99 ; 3,50 ; illisible ; second relevé dans le même tour refusé ; heure écrite seulement sous « CREDIT SUFFISANT ».
    - C7 : heures des deux rappels imprimées au geste 16.
    - Points mineurs : 1 (geste 3 (b) complet, feu substitut) ; 3 (jetons absents de la sortie, comptés en fin de `--env`) ; 4 (geste 5 sans dossier d'envoi : rien n'est écrit) ; 5 (étiquette déjà portée : code 3 ; débit des seules instances « running ») ; 6 (refus de la garde avec ordre, sur un cumul simulé de 44,12 USD) ; 10 (adoption ; créée 600 s et 121 s avant ; 100 s avant, dans la tolérance ; autre machine ; machine écrite en texte ; sans heure ; deux ; zéro ; témoin absent) ; 11 (lecture du journal en échec) ; geste 23 (b) (témoin disparu, témoin neuf) ; geste 24 (sorties d'erreur effacées, aucune liste brute restante) ; aucune sortie ne montre un jeton.
    - Gestes 2 (c) et 3 (a) : joués réellement, en lecture seule (337 accords).
  - **Non rejoué, et pourquoi** :
    - tout ce qui demande le loueur : forme réelle des réponses (création, liste, crédit, recherche), clés `start_date` et `machine_id`, journal, comportement de `-y`, destruction réelle ;
    - geste 4 (installation de l'outil réel, épreuve de `-y` sans réseau) : inchangé hors des noms ; il installerait l'outil réel ;
    - geste 21 : inchangé ;
    - le tableau du geste 20 : règle de lecture, non une commande ;
    - la branche « ECHEC SANS ORDRE » de la garde de dépense : il faudrait un lanceur absent ;
    - les demandes d'autorisation que déclencheront les gestes 6, 13 et 14 : non vues ;
    - **l'acceptation, par le crochet, du texte réel des gestes 6 (c), 13 et 14** (incident ci-dessous). À la lecture : chaque texte de création porte `GO_ID=GO-2026-11-14-09`, ligne de type « calcul », accordée par Lazar, valide du 2026-11-14 au 2026-11-22, non révoquée, et le registre se lit (gestes 2 (c) et 3 (a) joués) ; les 37 essais du crochet du dépôt (`tests/test_garde_calcul.py`) passent. Aucun autre bloc ne porte de texte de création ni de motif d'arrêt (recherche faite avec l'outil de recherche, hors du shell) ; le seul motif d'arrêt est l'artefact voulu du geste 2 (e).
- **Incident déclaré — refus du crochet.** Le rédacteur a voulu appliquer la fonction de décision du crochet aux textes des blocs, comme données, avec deux cas témoins écrits dans le texte même de sa commande : l'artefact du geste 2 (e) et une création sans accord. Le crochet a refusé la commande (« R10 — arrêt par motif de ligne de commande interdit ») : son texte portait le motif d'arrêt du cas témoin. Le rédacteur ne l'a ni reformulée, ni découpée, ni déplacée dans un fichier : cette évaluation n'est pas faite. Les analogues, eux, ne portent aucun texte de création de l'outil du loueur : l'outil y est un outil factice d'un autre nom.
- **Ce projet devient le feu** quand la mère :
  - lève les conditions 5, 7, 8 et 9 du § 0 (4 et 6 sont levées à la rédaction ; les champs 1 et 2 sont remplis) ;
  - remplace la ligne de tête par « en vigueur depuis <heure>, sous GO-2026-11-14-09 » ;
  - le verse sous `registres/t07-etape-b-bis/feu-bbis-v5.txt` avec son compagnon, et inscrit son empreinte au registre des décisions ;
  - le champ 3 reste ouvert : il est rempli au moment du feu par le geste 8 du tour de la création et par la recharge de Lazar qu'elle cite, et recopié à l'engagement (geste 16).
  Ce fichier-ci reste tel quel (R12).
