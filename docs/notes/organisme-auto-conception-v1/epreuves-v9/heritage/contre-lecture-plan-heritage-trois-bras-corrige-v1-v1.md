# Contre-lecture du plan à trois bras corrigé de l'héritage et de son devis — v1

## En-tête

- **Contre-lecteur** : modèle O, agent neuf. Il n'a écrit ni le plan, ni le devis, ni leur programme de calcul (règle R2). Rédacteur des pièces relues : modèle F.
- **Heures** (`date -u`) : état des branches relevé à 2026-11-19T13:18:08Z ; début d'écriture 2026-11-19T13:19:09Z.
- **Commit lu** : `c38cdcff13cd5db00103e6c29e489f3297d1d354` (branche `lot/compte-organisme-v1`). Les quatre pièces sont inchangées entre ce commit et la tête de la branche au moment de l'écriture (`8fc6e083fd25e81f7e2dd0f86b582a4364ca699b`, `git diff` vide sur le dossier). `main` lu à `e3f567a400f32db55379b4ce0d369fa018e6f483`.
- **Empreintes vérifiées contre leur compagnon `.sha256`** (toutes conformes) :
  - `plan-heritage-trois-bras-corrige-v1.md` : `a514c6dc072075d037eb77ba7d0c79fe1e3497180e8606782e67bc09aa2f4a0d` ;
  - `devis-heritage-trois-bras-v1.md` : `af51c493494b6be2ab2c599b3b8f579fa7cdbbe46fa305a6a140b7d5e462fd2e` ;
  - `calcul_devis_heritage_v1.py` : `782a86104b518eb5a4a616111ec6fb50d70ac713bf58138013c1b27291b4b186` ;
  - `calcul-devis-heritage-v1.json` : `02bae7980cbba40fb83ea7f30d732e11f9880c24fca3c4a1913b4b8923231765`.
- **Sources lues** (sur `main` sauf mention ; empreinte calculée sur le contenu lu) :
  - `CLAUDE.md` (règles R1 à R14) ; `prereg/gabarit-preregistrement-v1.md` (`8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e`) ;
  - proposition `docs/notes/organisme-auto-conception-v1/course-v2/proposition-cartes-a-eprouver-v9-v1.md` (`a2cd45adf7c49a909ad14be378b75b3233eae198b7f51cc416450f4cd878d856`) ; critères `criteres-choix-cartes-v9-v1.md` (`8881dbb2f63bdfedba34c971e5fb7081fc244ab5c3555307482589b84d837326`) ; lecture descriptive `lecture-course-v9-v1.md` (`0306adf74d321cfa933e047adff28324092787f870a2bf97bafd9d52bd5ffddb`), sections 1 à 3 ;
  - `registres/go.md`, ligne `GO-2026-11-19-55` (et ses voisines 56, 57, 59, pour la seule portée), lue par `git show` ;
  - N-067 `docs/decisions/decision-N-067-v1.md` (`966dd9dc3fae61cbe1f10ee2a54f401ddf7af5041eeaacd81ad9f8b264661589`), sections 4 et 5 ; N-071, chemin trouvé au registre des décisions (R-3187) : `docs/decisions/decision-resserrement-juge-au-nul-v1.md` (`9700fe6fce74840d383e3cbbf2e0f87f7914887759df3c0aa0fea687b433c184`), points 1 à 10 ;
  - N-073 (`b95688df5e695da7dc32ce71321ba205f44debcc0b7410e598c78c2180733ecd`) ; complément 1 (`61903909e8aaaa70d6f1aa26a8025104aa3513244b6723daac529048267d4478`) ; complément 2 (`5707dbd8bdd8ccc224578be480107723fad6e5054484082c1a1c38d8fa588e8e`) ; complément 3 (`4ca0ce7b040b917d9be145134b2b28755a862bfa7a41e4f16d22893129bb03e5`) ;
  - plan d'origine `docs/notes/veille-yu-memoire-v1/lecture-yu-approfondie-v2.md` (`956842550081abbd0292bc082015e782421c919ad0676764ed89721b3cc2e48f`), section (c) entière ; vérification courte `verification-courte-versions-2-v1.md` (`98d1152f05e3b60568557dca1d01a84ed2343a7505f1d17c0febdea4815e36dd`), sections 1 à 3 et conclusion ;
  - sur la branche : manifeste `runs/20261119-094145-course-auto-conception-v9/manifeste-lanceur-fin.json` (`28bc36df390d8481fb5bd9118cf764843ffea60856412d825ecbf08e7cee5be7`, conforme au devis), champ `cout_reel` seul ;
  - cartes : `fiches.json` de la course v9 (`ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481`, conforme), dont **seules** les neuf cartes nommées par le plan ont été extraites, par identifiant, par un petit programme qui ne lit que le champ `contenu` (champ `meta` retiré, espèce non lue). Aucun autre fichier du dossier d'archive n'a été ouvert. Le programme d'extraction reste hors du dépôt.
- **Rejeux** : `calcul_devis_heritage_v1.py` rejoué dans un dossier de travail ; sortie identique à l'octet (`02bae798…1765`). Valeurs de `cout_reel.par_role_usd` et `cout_reel.appels_par_role` du manifeste identiques aux constantes du programme ; total 72,50247 USD ; aucun appel à coût inconnu, aucune coupure. Table des rangs signés exacts vérifiée à la main pour n = 6, 7 et 8.
- **Recherche « Ne pas écrire »** refaite par recherche de chaînes sur les deux textes (formules du complément 3, du point 4 du complément 2 et de la liste « Ne plus écrire » de N-073, § 1), puis relecture des occurrences.
- **Non lus** : le code de l'organisme, de l'oracle et du générateur des mondes ; N-045 v2, N-049, N-050, N-053, N-058 (connus par les pièces ci-dessus) ; tout dossier interdit par le mandat.
- Aucun appel à un fournisseur de modèles, aucun relais, aucune dépense, aucun refus d'outil.

## Ce qui tient

1. **Objet conforme à la lettre du complément 3** : les sept champs du registre des tentatives (problème, tentative, justification, prédiction scellée, résultat écrit par programme, « gardée », provenance) y sont, en ajout seul, tentatives non gardées comprises ; l'appellation fautive corrigée par le complément 3 n'apparaît nulle part.
2. **Les trois corrections de la vérification courte sont prises** : invariant (§ 3.1), forme probabiliste de la prédiction et taux de base qui ne dépend pas des prédictions (§ 3.2), plancher de sources (§ 3.3) ; les points c et e mineurs sont aussi traités. Le défaut (iv) (lecture de m dans k sur m) est fermé par construction.
3. **Les trois éléments nommés par la proposition et le mandat sont versés** : dose plantée avec dose nulle (`fed7a993d9671`), mondes avec et sans dépendance (`fc1f059e8873e`), répondeur scripté (`f7219bb36cfcb`). Les attributions des neuf cartes, versées comme écartées, sont exactes : vérifié carte par carte sur leur texte.
4. **Calculs justes et rejoués** : table des rangs signés (§ 3.3), unités et totaux du devis, rapport aux ordres de grandeur antérieurs (4 000 USD de la vérification courte ; 150 à 350 USD de la proposition).
5. **Liste « Ne pas écrire » du complément 3 tenue** : aucune des onze lignes n'est employée ; ni les six formules du point 4 du complément 2, ni celles de N-073, § 1 (la ligne 293 du plan les nie, elle ne les emploie pas). Aucune zone dite libre, aucune priorité, aucune revendication neuve. Citations obligatoires de N-073, § 1, et des compléments 1 à 3 présentes au § 11.
6. **Règles R3, R4, R5, R9 nommées aux bons endroits** ; gardes avec cas sain et artefact listées ; aucun chiffre de la littérature ; Brier, Pratt et Holm marqués « non lus sur source » (R7).
7. **Faisabilité sur processeur seul de l'étage annoncé** : générateur, exécuteur simulé, quatre proposeurs scriptés, procédure d'analyse : aucun appel, aucune instance. Elle reste conditionnée au constat 1 (il faut savoir ce que l'exécuteur simule).

## Constats et corrections

Gravité : **B** = à corriger avant tout préenregistrement d'un étage ; **M** = à corriger dans la version 2 des pièces ; **m** = mineur.

### 1. (B) L'« épreuve programmée » n'est définie nulle part, et son lien avec le juge statistique n'est pas dit

- Tout repose sur elle : les champs `resultat` et `gardee` (§ 1), l'objet de la prédiction (§ 3.2), le compte des lois fausses « tenues » (§ 6), l'exécuteur simulé (§ 7). Le plan ne dit ni quelle statistique, ni sur quelle part des données d'évolution, ni à quel seuil, ni qui l'exécute.
- Or l'organisme a déjà deux épreuves programmées : le juge statistique (règle à e-valeurs, nul formé des lois connues, N-067, § 4, point 1 ; N-071) et les tests de mort (non branchés sur le lanceur, proposition § 6, écart 5). Si l'épreuve du plan est le juge statistique, alors (i) le registre porte le verdict d'un juge programmé, ce qui est précisément ce que la vérification courte reprochait (point a : les témoins sont « promus » par ce juge) ; (ii) le § 4.2, ligne 3 (cartes écartées parce qu'elles comptent les lois « promues par la règle à e-valeurs ou par le juge statistique ») et le § 10, puce 5 (« la mesure n'emploie pas sa règle de promotion ») deviennent inexacts ou incohérents ; (iii) le plan touche O4 et doit porter les citations obligatoires de N-067, § 6, et de N-071, point 5.
- L'invariant du § 3.1 ne protège que contre les « juges à modèle » ; il ne dit rien d'un juge programmé.
- **Correction** : ajouter un § 3.0 « L'épreuve programmée », qui fixe : entrée (engagement scellé, sous forme exécutable), données (part nommée du jeu d'évolution du monde en cours, jamais le monde final), statistique, seuil, règle de passage aux trois classes d'issue, exécutant (l'orchestrateur, par programme). Puis dire laquelle des trois voies est prise : (a) le juge statistique de l'organisme — alors l'écrire, étendre l'invariant du § 3.1 à « aucune sortie d'un juge, à modèle ou programmé, autre que l'épreuve nommée au § 3.0 », corriger le § 4.2 (ligne 3) et le § 10 (puce 5), ajouter les citations de N-067, § 6, et N-071, point 5, et porter la question au nœud 1 du § 12 ; (b) les tests de mort ; (c) une épreuve neuve propre à ce plan — alors la déclarer comme changement de l'organisme (règle 3 du § 2, réserve 1 du § 13). Corriger aussi le premier alinéa de « Choix » du § 3.1 : ce n'est pas « la première voie durcie » de la vérification courte, c'est une **troisième voie** (le signal de l'oracle est remplacé par une épreuve sur les données) ; le dire ainsi dans la réserve 3 du § 13.

### 2. (B) Le coût de lecture rend faux le niveau attendu du « sourd » et fait déclencher la règle de validité par construction

- Règle 6 du § 2 : le bras qui lit un registre paie sa lecture et a moins d'appels. Au départ de la continuation, le bras 3 sert le registre plein de la source, le bras 2 un registre vide. Un proposeur qui ignore le registre (le « sourd » du § 7) a donc moins d'appels au bras 3 qu'au bras 2 et retrouve en espérance moins de lois : son écart d'héritage attendu est **négatif**, pas nul. Le § 7 (« écart d'héritage nul à toute dose ; taux de rejet … au niveau annoncé ») ne peut pas passer honnêtement : avec assez de sources, le test bilatéral rejette au-delà de 5 %.
- Même mécanisme à dose nulle : la règle de validité (§ 8) est bilatérale ; un écart négatif dû au seul coût de lecture, effet voulu du dessin, déclare « la lecture entière invalide ».
- La règle d'arrondi (point e, § 2 règle 6 : « entier inférieur du nombre de lots par espèce ») aggrave l'effet : dès que la lecture coûte quoi que ce soit, chaque espèce perd au moins un lot sur onze, soit au moins 9 % des appels, quel que soit le coût réel de la lecture.
- **Corrections** :
  1. Dire l'estimande au § 2 : « écart à budget égal, coût de lecture compris ». En conséquence, au § 7, le sourd « paie » et son écart attendu est « l'effet du seul coût de lecture » ; le **niveau** de la procédure se mesure sur un **sourd à appels égaux** (variante où la lecture ne retire aucun appel), taux de rejet au plus 0,05.
  2. Règle de validité **unilatérale** (§ 5 et § 8) : la lecture est invalide si l'écart d'héritage à dose nulle est **positif** au seuil de 0,05 unilatéral ; l'écart négatif à dose nulle est rapporté, comparé à l'effet du seul coût mesuré sur le sourd payant.
  3. Remplacer l'arrondi par espèce par un retrait au plus près du coût : nombre d'appels retirés = partie entière de (coût de la lecture divisé par le coût moyen d'un appel du bras), sur le total, réparti entre espèces par tirage semé (R9) proportionnel aux lots ; reliquat rapporté. Ou garder l'arrondi, mais écrire la perte minimale d'un lot par espèce comme borne et la faire mesurer par le sourd payant.
  4. Au devis, ajouter une ligne d'information : appels perdus par le bras 3 en génération 1, selon la règle retenue.

### 3. (B) La raison donnée à la règle de validité à dose nulle est inexacte

- § 5 : à dose nulle, « un écart d'héritage non nul n'y peut venir que de la forme ». C'est faux : un registre hérité d'un monde sans dépendance peut transmettre un **savoir-faire général** (forme d'engagement que l'épreuve programmée exécute, classes de lois fausses qui « tiennent » à tort, longueur utile d'une tentative), et il porte le coût de lecture (constat 2). Un écart positif à dose nulle peut donc être un héritage réel, non tiré de la dépendance plantée.
- Conséquence : la règle déclare « invalide » ce qui peut être un effet vrai ; le plan mesure seulement l'héritage **spécifique à la dépendance plantée**, sans le dire.
- **Corrections** : (i) au § 5, réécrire la raison : « à dose nulle, un écart positif vient de la forme ou d'un savoir-faire général transmis ; le plan ne mesure que l'héritage spécifique à la dépendance plantée, et un savoir-faire général invalide la lecture au lieu d'être mesuré » ; (ii) porter cette borne au § 10 ; (iii) au § 7, ajouter un cinquième proposeur scripté, « le généraliste », qui tire du registre une règle générale (par exemple : n'engager que la classe de lois que l'épreuve exécute) sans lire le contenu spécifique, pour savoir si la règle de validité se déclenche sur lui ; si oui, le dire avant l'étage payant.

### 4. (B) Critère « instrument lisible » non chiffré ; seuils de l'étage sur processeur absents

- Le § 8, condition 1, exige « issue « instrument lisible » » ; le § 7 ne la définit pas. « La taille prévue » (§ 7, point 1) n'est pas définie. Aucun seuil de puissance, aucune tolérance de simulation pour le niveau.
- **Correction** : au § 7, une table gelée qui mène à « lisible », « non lisible » ou « à reconstruire », avec des seuils chiffrés dont le plan fixe la forme et la valeur proposée, et que le préenregistrement de l'étage gèle : puissance du lecteur au moins 0,8 à une taille d'effet de référence nommée (en lois retrouvées sur le monde final), à 10 et à 12 sources ; niveau sur le sourd à appels égaux au plus 0,05, borne haute de l'intervalle de simulation à 95 % au plus 0,06, nombre de tirages fixé d'avance ; règle de validité déclenchée au moins 8 fois sur 10 sur le suiveur de forme, au plus 1 fois sur 20 sur le sourd à appels égaux ; contrôle de construction tenu au-delà d'une part gelée. Le nombre de sources à dose nulle se déduit de ces seuils par une règle écrite, non par lecture libre.

### 5. (M) Pilote de bruit payant placé avant le devis et la ligne d'accord ; sa taille n'estime rien

- § 8 : la condition 5 (pilote, de vrais proposeurs, donc payant) précède la condition 6 (préenregistrement, devis accepté, ligne d'accord). Lu dans l'ordre, le pilote se dépense sans accord : interdit par `CLAUDE.md` (« dépenser sans GO sur devis »).
- Le devis compte le pilote pour 6 générations de bras, soit **une** paire de courses : une seule différence ne donne pas d'écart entre deux courses identiques. Et le § 3.3 dit « le pilote ne peut que relever ce nombre » sans dire par quelle règle.
- **Correction** : condition 5 réécrite « pilote de bruit, sous son propre préenregistrement, son devis et sa ligne d'accord » ; nombre de paires gelé (au moins trois, à justifier) ; règle chiffrée qui tire le nombre de sources du pilote et de la puissance de l'étage sur processeur ; ligne du devis recalculée.

### 6. (M) Lecture « oui » et « non » de l'étage payant non tabulée ; prédiction chiffrée absente

- Le § 8 dit ce qui réfute ; il ne dit pas ce qui établit. La condition sur les lois fausses (§ 6) est « proposée, à geler », sans marge. Le gabarit exige « Prédiction chiffrée et signe attendu » ; le plan n'en annonce aucune pour les deux contrastes.
- **Correction** : au § 8, une table gelée. D'abord les conditions de lecture (troncature tenue, chaîne d'empreintes, générateur audité, règle de validité non déclenchée) ; sinon « invalide ». Puis, par contraste : Holm passe et médiane des différences positive et condition des lois fausses tenue, « établi » ; Holm passe et médiane négative, « effet négatif établi » ; Holm ne passe pas, « non établi » (jamais « effet nul ») ; Holm passe mais lois fausses en hausse au-delà de la marge, « non lu comme succès ». La condition des lois fausses passe de « proposée » à « gelée au préenregistrement, marge chiffrée ». Ajouter : « le préenregistrement de l'étage payant porte, pour chaque contraste, un signe et un ordre de grandeur, tirés de l'étage sur processeur et du pilote, avec l'indice contraire de Qin et al. dit avec sa prémisse » (aucun signe visé, R3).

### 7. (M) Lectures intermédiaires sur une autre mesure que la mesure décisive

- § 6 : la mesure décisive est sur le monde final tenu à l'écart ; les lectures au quart et à la moitié sont « sur les mondes d'évolution ». Le § 8 conclut pourtant « effet présent au quart et absent à l'échéance » : on compare deux mesures sur des mondes différents.
- **Correction** : calculer la même mesure sur les mondes d'évolution au quart, à la moitié **et à l'échéance**, et lire l'effet de départ sur ces trois points seuls ; le monde final décide seul, à part. Définir « quart du budget » : coupure du budget cumulé de la continuation dans le journal des appels, pas une génération.

### 8. (M) Le monde final : la mécanique n'est pas dite

- Le plan ne dit pas : combien d'appels ou quelle génération tourne sur le monde final ; si le registre y est servi ; si les résultats de ce monde sont écrits dans le registre (ils ne doivent pas l'être) ; si le monde final porte la même dose ρ et la même construction que les mondes cibles ; comment ses graines sont dérivées.
- **Correction** : au § 6, préciser : une génération finale à budget égal par bras, registre servi en lecture seule et gelé à l'état de la fin de continuation, aucune écriture, monde final à la même dose que les mondes cibles de la source, graines dérivées par source et communes aux trois bras (R9).

### 9. (M) Le bras 1 écrit-il les champs ?

- Le bras 1 n'a pas de registre. Écrit-il une justification et une prédiction scellée ? La garde « refuse d'éprouver une tentative sans empreinte » s'applique-t-elle à lui ? Sinon, le contraste de la tenue mêle « servir un registre » et « écrire des champs et sceller une prédiction » (charge et coût différents).
- **Correction** : écrire le choix au § 2. Recommandation : le bras 1 écrit les mêmes champs, scellés et sur disque, **non servis** ; le contraste de la tenue isole alors le service du registre, et la justesse des prédictions se lit aussi au bras 1. À défaut, dire que la tenue inclut l'effet de l'écriture.

### 10. (M) Silence sur les sections c.7 et c.8 du plan d'origine

- Le § 2 garde les sept règles de c.4 ; le § 1 reprend une part de c.7. Rien n'est dit de c.8 : « le juge ne lit jamais le registre » (sens inverse de l'invariant), champs libres servis entre balises de donnée, audit du registre par un lecteur d'une autre lignée à chaque génération (N-053), canal caché. Le devis (§ 6, point 3) parle de l'audit comme d'un poste non chiffré, le plan non.
- **Correction** : ajouter au § 1 « Ce qui est gardé de c.7 et c.8 », avec au moins « aucun champ du registre n'est une entrée d'un juge » et l'audit par une autre lignée ; ou dire ce qui est retiré et pourquoi.

### 11. (M) Règle « les copies ne comptent pas » : symétrie non dite, objet presque vide

- § 6 : « une loi plantée déjà présente comme tentative dans le registre hérité … n'est pas comptée ». Pour qui ? Appliquée au seul bras 3, elle le pénalise ; la même loi retrouvée par le bras 2 compterait. Et, les mondes cibles étant neufs et leurs lois dépendantes composées, non identiques, l'ensemble exclu est presque vide par construction.
- **Correction** : écrire que l'ensemble exclu est le même pour les trois bras d'une source, et dire ce que la règle garde (par exemple, un monde final qui contiendrait une loi de la source à l'identique) ; sinon la retirer.

### 12. (m) Une carte citée pour un autre objet

- § 3.1 : « Une carte (`fed7a993d9671`) le relève elle-même ». Cette carte relève le point pour une **sélection de survivants** servie, non pour la classe d'issue d'une épreuve programmée. **Correction** : « une carte relève le même point pour la sélection des survivants servie ».

### 13. (m) Paraphrase de la rédaction de la section C au § 10

- § 10, puce 1 : « qui décrit une forme et dit ne pas l'avoir trouvée dans les pages lues de six travaux ». Juste sur le fond, mais c'est une paraphrase d'une phrase qui doit se recopier à l'octet (§ 11) ; recopiée hors du dépôt, elle deviendrait une affirmation de « non trouvé » sans sa lettre. **Correction** : « Toute mention de la forme se fait par la rédaction de la section C du complément 3, recopiée à l'octet ; ce plan n'en dit rien de plus. »

### 14. (m) Citations du § 11 à compléter

- Qin et al. : donner la prémisse dans le texte même (N-073, § 1 : +24,0 au quart du budget, +1,2 à l'échéance, p. 6, tableau 8 p. 21, selon la lecture sur PDF), puisque le plan lit trois échéances précisément pour cet indice.
- Le registre garde ses tentatives non gardées : si un texte en parle, le complément 2, point 3, impose de lire d'abord sur source Xia et al., « RRSI », arXiv 2609.24972 ; l'ajouter sous condition.
- Selon le constat 1 : citations de N-067, § 6, et de N-071, point 5, si l'épreuve programmée est le juge statistique.

### 15. (m) Règle R6 : empreintes manquantes ou tronquées

- Le plan (§ 3.3) et le devis renvoient au programme et à sa sortie « empreintes compagnes » sans écrire l'empreinte. Écrire `782a86104b518eb5a4a616111ec6fb50d70ac713bf58138013c1b27291b4b186` (programme) et `02bae7980cbba40fb83ea7f30d732e11f9880c24fca3c4a1913b4b8923231765` (sortie) dans les deux textes. Compléter les empreintes tronquées du plan (proposition, critères, lecture descriptive) et ajouter celles de N-067 et N-071 (en-tête ci-dessus).

### 16. (m) Devis : colonne « minimal » hors plan ; défaut mal justifié

- La colonne « minimal » joue la dose nulle sur processeur seulement : la règle de validité du § 8 n'y est pas appliquée à de vrais proposeurs, ce que le plan rend obligatoire. **Correction** : la marquer « hors plan, pour borner » ou la retirer des totaux du § 0.
- § 9 : « Défaut : aucun : toute dépense est un nœud » alors que la décision posée porte sur un étage à 0 USD. **Correction** : « Défaut : aucun : le mandat GO-2026-11-19-55 s'arrête, pour l'héritage, au plan corrigé et au devis ; l'étage sur processeur demande un mot neuf. »
- Ligne du pilote à recalculer (constat 5) ; ligne d'information sur les appels perdus (constat 2).

### 17. (m) Reprise après une lecture invalide

- § 8 : « la lecture entière est déclarée invalide et l'épreuve est à reconstruire ». **Correction** : ajouter que la lecture invalide est rapportée telle quelle, et qu'une épreuve reconstruite est un préenregistrement neuf, sur des sources neuves, sans reprise visant un signe (R3, R4).

## Fidélité au mandat et à la proposition

- **Rien de moins** : les trois éléments nommés par l'option (c) sont versés ; la lettre du complément 3 est suivie ; le devis est écrit.
- **Rien de plus, sous réserve** : six éléments de cartes de plus sont versés (lectures à trois échéances, registre d'une autre source, copies, troncature, double appariement, audit du générateur). Ils entrent dans « les bons éléments des cartes » du mandat et sont tous attribués justement. Deux écarts de fond au plan d'origine sont des choix du rédacteur, à porter comme tels devant Lazar : la troisième voie de l'invariant (constat 1) et l'abandon du volet des témoins jugés de l'oracle dans la mesure principale (déjà nœud 2 du § 12). Aucun mécanisme n'est câblé, aucune dépense engagée.

## Verdict

Scellable après corrections.

Les deux pièces suivent la lettre du complément 3 de N-073 et le mandat GO-2026-11-19-55 ; elles ne revendiquent rien et tiennent la liste « Ne pas écrire » ; leurs calculs se rejouent à l'octet. Avant tout préenregistrement d'un étage, les constats 1 à 4 sont à corriger : l'épreuve programmée et son lien au juge statistique, le coût de lecture face au niveau du sourd et à la règle de validité, la raison de cette règle, le critère chiffré « instrument lisible ». Les constats 5 à 11 vont dans la version 2 des deux pièces ; 12 à 17 sont de forme. Remarque hors pièces : le message du commit `c38cdcff` porte une ligne d'attribution autre que celle demandée par la consigne, ce que le rédacteur a déclaré lui-même ; sans effet sur le fond.
