# Contrôle du différentiel v4 → v5 des critères et de la note du juge de sélection — v1

- **Contre-lecteur, modèle O** : le même que pour la contre-lecture `ee578a61…`. Je n'ai écrit ni les pièces v5, ni les programmes v2, ni aucune carte. Écrit le 2026-11-20 (`date -u` : 2026-11-20T02:48:37Z). Processeur seul, aucune dépense, aucun appel de modèle, aucun réseau hors `git fetch` et `git show` du dépôt. Rien n'est écrit dans le dépôt.
- Dossiers : V4 = `docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/criteres-v4/` ; V5 = `…/juge-selection/criteres-v5/`.

## Verdict

**Conforme après corrections.**

Ce qui tient :
- Les deux textes v5 sont exactement les v4 plus les remplacements déclarés : je les ai rejoués à l'octet.
- C1 à C8 sont portés à la lettre. C1 retire les deux tests à 0,025 aux neuf endroits.
- Les essais passent chez moi : 91 et 32.
- Six défauts glissés dans les programmes v2 sont tous attrapés par les essais.

Ce qui doit être corrigé :
- **Trois passages, à corriger avant que la fiche parte à Lazar** (D1 à D3) : ils écrivent pour le veto un défaut qui contredit C2. Les défauts du 19 échoient le 21 vers 14:41Z.
- Quatre retouches mineures (D4 à D7).

## 1. Empreintes et rejeu de l'outil

**Empreintes.** `sha256sum -c` passe sur chaque compagnon :
- le mandat (`d210c081…`) ;
- son complément 1, `V4/complement-1-mandat-redacteur-corrections-criteres-v5-note-v5-v1.md` (`83fa0db4…`, recalculé) ;
- les deux textes v5 (`b22827fd…`, `6ec0aeeb…`) et les deux fichiers de remplacements ;
- les deux journaux ;
- les programmes v2, leurs essais et leurs sorties ;
- la mesure v2 et sa sortie ;
- les deux rejeux ;
- les sept différentiels ;
- le rapport (`29699359…`).

**Outil.** `scripts/remplacer_texte_exact_v1.py`, sha256 `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6`. Je l'ai lu en entier. Je l'ai rejoué sur des copies des v4, avec des copies des deux fichiers de remplacements :
- critères : 16 remplacements, cible `8e8c6194…`, sortie **`b22827fd…`** ;
- note : 13 remplacements, cible `4b2c5ad2…`, sortie **`6ec0aeeb…`**.

Les deux sorties sont égales à l'octet aux pièces versées. Les journaux versés portent les mêmes empreintes d'outil, de cible, de remplacements et de sortie.

**Différentiels.** J'ai refait `diff -u` v4 → v5 et comparé le corps, sans les deux lignes d'en-tête, à celui des différentiels versés : identiques par `cmp`, pour les critères comme pour la note.

**Rejeux.**
- `verif-lecteur-v1-rejouee-sur-le-programme-v1-sortie-v1.txt` vaut `e2a532ae…` : c'est l'empreinte de ma propre sortie.
- La sortie de la mesure v2 vaut `6309b0ce…` : c'est l'empreinte de la sortie v1.

## 2. C1 à C8, à la lettre

- **C1.** Neuf endroits : critères, lignes 176, 177, 178, 306 et 320 de la v4 ; note, lignes 240, 252, 271 et 350. Texte neuf mot pour mot. Il ne reste « 0,025 » et « désignés d'avance » que dans les deux différentiels v4 → v5 (critères § 15, note § 10.3), qui les citent. Le taux « une fois sur cinq au plus » est écrit aux deux endroits.
- **C2.** Le paragraphe d'ouverture du § 9 de la note est à la lettre. La source R-3890 y est ajoutée, sur le complément 1. Je l'ai vérifiée : `origin/main:registres/decisions.md`, ligne R-3890, 2026-11-19T14:41:07Z, mot pour mot.
- **C3, C5, C8** : à la lettre.
- **C4.** À la lettre dans le texte (critères § 1 ; note, décision 5, enjeu et option (d)). Il est porté aussi dans `gardes`, puisque la lettre de C4 demandait un programme et des essais.
- **C6** : les quatre points.
- **C7** : texte à la lettre ; programme et essais.

La tenue (titres, lignes « Version 5 », noms des programmes joints, renvoi à la note v5, § 15 et § 10.3) ne change aucune règle.

## 3. Essais, et défauts glissés (R4)

Je les ai lancés sur des copies, par `python3 -B -m pytest -q -p no:cacheprovider CHEMIN` (Python 3.13.18) :
- **assemblage v2 : 91 passés, 0 échoué** (63,8 s) ;
- **lecteur par programme v2 : 32 passés, 0 échoué**.

**Six défauts glissés**, un par copie. Chaque défaut est **attrapé** par au moins un essai neuf.

| | défaut glissé dans la copie | essai qui échoue |
|---|---|---|
| m1 | C7 : `all(` devient `any(` dans `groupe_sans_objet_au_veto` | `test_c7_cas_sain_…` (filtre par lignée : trois groupes faussement « sans objet ») |
| m2 | C7 : le test de remplacement lit les entrées par veto au lieu du veto déposé | `test_c7_le_veto_tel_que_depose_est_lu_dans_les_deux_sens` |
| m3 | C4 : baisse et hausse échangées | `test_c4_artefact_baisse_plantee_dans_une_seule_lignee` |
| m4 | C4 : un D devenu indécidable compté « égal » | même essai (compte à part) |
| m5 | C5 : le « oui » cherché dans le seul champ de réfutation | six essais, dont `test_c5_cas_sain_…` |
| m6 | C5 : le compte résiduel de D inclut les indécidables | `test_c5_valeurs_residuelles_…` |

La réserve du rédacteur (« je n'ai pas vérifié qu'un défaut glissé ferait échouer chaque essai neuf ») est levée pour ces six cas. Ce n'est pas une preuve d'exhaustivité.

## 4. Les points déclarés par le rédacteur

**C4 porté dans `gardes`.** Il tient :
- les deux sorties vont ensemble ou aucune ;
- la forme lue est contrôlée, et deux sorties échangées sont refusées ;
- une carte absente d'une sortie, ou un D hors domaine, est un refus ;
- le compte est descriptif, ne consomme aucune graine, et laisse identiques les tests et le retour à Lazar (essai `test_c4_cas_sain_…`) ;
- si les sorties ne sont pas passées, la sortie écrit en tête « NON RAPPORTÉE ».

**C4, un D devenu indécidable compté à part.** Le choix tient, puisque les deux comptes sont rendus. Mais c'est aussi une perte du canal. La coupe à la médiane ne peut pas vider un champ ; ce sont le retrait des formules et celui des phrases récitées qui peuvent le vider. La lecture doit donc prendre les deux comptes ensemble : correction mineure D7, texte seulement.

**Les deux compteurs du lecteur v2.** Ils tiennent : ils sont descriptifs, sans clé neuve par carte. `D_zero_faute_de_tout_terme` compte exactement les D = 0, qui n'arrivent que faute de tout terme. La v2 corrige au passage un second défaut de la v1 : « désactiver » contenait le terme du « oui » « activer ». Il est maintenant retiré avec les termes du « non ».

**C7, un groupe « retiré » s'il l'est pour chaque titulaire.** C'est la bonne lecture. Si un seul titulaire peut encore désigner une carte du groupe, sa présence parmi les entrées n'est pas nulle par construction. Le test de remplacement prend la graine du test remplacé, donc l'ordre du § 9, point 9, ne bouge pas. Remarque, sans correction : sous le filtre « lignée », défaut du 19, aucun test n'est sans objet avec les deux lecteurs seuls.

**C6, la garde 2 sur la graine 7 garde une assertion vide.** Cela tient. C6 ne visait que la garde 1. Dans le monde 7 non retouché, la garde 2 ne nomme aucun écart fort (ma sortie `verif-contre-lecture-sortie-v1.txt`, `a1522f97…`). L'assertion sur l'écart planté de Carbon y est donc informative.

**Option (d) du masque.** Le masque v1 ne la sert pas en une passe. Il faudrait deux passes (médianes lues au rapport, puis reprises en entiers) ou un masque v2. La note dit pourtant encore « les critères et le programme marchent sous chaque option », et elle garde « (a), confiance 0,6 », écrit avant que (d) existe. C'est à corriger avant la fiche (D5, D6). La décision 5 est neuve : il n'y a pas d'enjeu de délai.

**Commandes enchaînées et `git status --porcelain`.** Écart de procédure, déclaré, sans effet sur les pièces : la sortie était vide, et aucun chemin interdit n'a été nommé. Il ne change pas le verdict. À ne pas refaire : `git status` liste des noms dans tout l'arbre, dossiers interdits compris.

**Les trois passages près de C2 sont à corriger avant la fiche.** Un défaut se lit dans la ligne « Défaut sous 48 heures » d'une décision, plus que dans un paragraphe d'ouverture.
- La note (décision 2) écrit « (a), pour le rejeu seulement ». Or son (a) porte le plafond et le retrait par famille.
- Les critères, § 13, écrivent « défaut : tel qu'écrit ici ».
- L'annexe B dit que toute valeur autre que « famille » et « nombre_vise » est « une décision de Lazar ».

Lu tel quel, le manifeste porterait au 21 vers 14:41Z un défaut que Lazar n'a jamais vu : c'est exactement ce que C2 voulait empêcher. Les différentiels le disent, mais une fiche se lit sans eux. Corrections D1 à D3.

J'ai aussi trouvé deux points sur la source R-3890 :
- elle nomme « déclaration de la lignée reconnue » **sans défaut** ;
- elle porte « six points à confirmer » **sans défaut**, comme la note v3, dont c'était le constat 8.

La note v5 écrit pourtant « la lignée reconnue non déclarée » parmi les défauts posés le 19, et « le défaut déjà posé » à la décision 3. L'état actuel coïncide avec « non », donc rien ne change dans les faits ; mais la source doit être dite juste (D5).

## 5. La demande de configuration (rapport, § 6)

**Elle est juste.**
- Masque : les sept clés exactes de `masque_style_cartes_v1.py`.
- Lecteur v2 : les trois clés exactes.
- La contrainte « champs de B inclus dans A » est vraie, sinon la forme masquée est refusée.
- Les gestes sont exacts : deux passes du lecteur, la sortie masquée à `assembler`, les deux sorties à `gardes`.

**Elle suffit, à deux ajouts près, pour que la mère écrive les deux fichiers sans ouvrir de carte :**
1. **Où lire les noms des champs de `contenu`.** Dans le code qui écrit les cartes, au commit de la course v9 : la statistique de famille, § 0, cite le commit `a41b7b50`, `orchestrator/pole/course2_v54.py` et `course2_v56.py`, ainsi que la configuration `course-v4/configuration-course-auto-conception-v5.json`. Un champ manquant ou en trop arrête le masque, mais son message ne donne qu'un nombre : une liste fausse ne se corrige qu'en relisant le code, jamais en ouvrant une carte. C'est voulu ; il faut le dire à la mère.
2. **Le manifeste, d'après C2** : ajouter `suppleantes` : `4`, lettre de la v3. La demande ne porte que `filtre_veto` « lignee », `plafond_veto` null et `veto_par_titulaire`.

Autre point, facultatif : pour `intertitres`, l'audit (§ 8, point 3) nomme le type « pourquoi cela compte ». À retenir si la consigne de la course l'impose.

## 6. Décisions pour Lazar

- Rapport, § 7, point R-4050 : au format (décision en une phrase, enjeu, trois options avec avantage et inconvénient, recommandation et confiance, défaut). Les options sont celles de la contre-lecture, sans ajout.
- Note v5, § 9, décisions 1 à 5 : au format.
- Défauts : faux pour la décision 2 (D1), à préciser pour les décisions 1 et 3 (D4, D5).
- Recommandation de la décision 5 : périmée (D6).

## 7. Corrections

Par l'outil `391db990…`, sur les v5, sous des noms neufs (règle R12). Textes anciens copiés des v5 ; « \n » marque un saut de ligne.

**D1 — moyen, avant la fiche — note, décision 2.**
- Ancien : « **Recommandation.** (a), confiance 0,6.\n\n**Défaut sous 48 heures.** (a), pour le rejeu seulement. »
- Nouveau : « **Recommandation.** (a), confiance 0,6.\n\n**Défaut sous 48 heures.** Jusqu'à 48 heures après que cette fiche t'a été posée : (c), la lettre posée le 19 (R-3890 ; trois puis deux cartes, retrait par lignée, sans plafond), pour le rejeu seulement — c'est elle qui échoit le 21 vers 14:41Z. Ensuite, sans mot de toi : (a), pour le rejeu seulement. »

**D2 — moyen, avant la fiche — critères, § 13, point 2.**
- Ancien : « 2. **Veto** (posée de même ; défaut : tel qu'écrit ici, pour le rejeu seulement). »
- Nouveau : « 2. **Veto** (posée de même ; défaut posé le 19, qui échoit le 21 vers 14:41Z : la lettre de la v3 — trois puis deux cartes, retrait par lignée, sans plafond —, pour le rejeu seulement ; le plafond et le retrait par famille du § 8 sont une option neuve, qui ne devient défaut que 48 heures après que la mère l'a posée ; note v5, § 9). »

**D3 — moyen, avant la fiche — critères, annexe B.**
- Ancien : « Les valeurs entre parenthèses sont celles de ces critères ; toute autre valeur est une décision de Lazar, écrite au manifeste avec sa ligne. »
- Nouveau : « Les valeurs entre parenthèses sont celles de ces critères ; toute autre valeur est une décision de Lazar ou un défaut échu, écrit au manifeste avec sa ligne (de `registres/go.md` ou de `registres/decisions.md`). **Pour le veto**, tant que l'option neuve du § 8 n'a ni réponse ni défaut échu, le manifeste porte le défaut posé le 19 (R-3890) : `filtre_veto` « lignee », `plafond_veto` null, `suppleantes` 4 (lettre de la v3). »

**D4 — mineur — note, décision 1.**
- Ancien : « **Défaut sous 48 heures.** (a), le rejeu seul, qui est sans dépense. »
- Nouveau : « **Défaut sous 48 heures.** (a), le rejeu seul, qui est sans dépense — c'est, sans adoption, le défaut posé le 19 (R-3890), qui échoit le 21 vers 14:41Z ; les conditions neuves de (a) (critères v4, huit items « dans chaque voie ») courent du moment où cette fiche t'est posée. »

**D5 — mineur — note, § 9 : source juste, et l'option (d).**
- (i) Ancien : « ; la lignée reconnue non déclarée. Ce que la v4 change ». Nouveau : « ; pour la lignée reconnue, R-3890 n'écrit aucun défaut : elle reste non déclarée, ce qui est l'état actuel. Ce que la v4 change ».
- (ii) Ancien : « **Défaut sous 48 heures.** (a), non — le défaut déjà posé. » Nouveau : « **Défaut sous 48 heures.** (a), non. R-3890 nomme cette décision sans lui écrire de défaut : « non » est l'état actuel, et ce défaut-ci court du moment où cette fiche t'est posée. »
- (iii) Ancien : « **Défaut de chacune, sans mot de toi : tel qu'écrit dans les critères v4, pour le rejeu seulement.** Aucune ne s'applique à une course neuve sans ton mot. » Nouveau : le même texte, suivi de « Les six premières t'ont été portées le 19 sans défaut écrit (R-3890) : ce défaut-ci court du moment où cette fiche t'est posée. »
- (iv) Ancien : « **Les critères et le programme marchent sous chaque option** : chacune est une valeur du manifeste d'ouverture. » Nouveau : « **Les critères et le programme marchent sous chaque option**, sauf l'option (d) de la décision 5, que le masque v1 ne sert pas en une passe : chacune est une valeur du manifeste d'ouverture. »

**D6 — mineur — note, décision 5, recommandation.**
- Ancien : « **Recommandation.** (a), confiance 0,6 ; le lecteur par programme est joué sur les cartes masquées et non masquées, ce qui donne une première mesure de ce que la coupe change. »
- Nouveau : « **Recommandation.** (a) pour le rejeu, confiance 0,5 : c'est la seule option à coupe que le masque v1 sert. (d) répond mieux au risque sur D, mais demande un masque v2, contre-lu et scellé avant l'ouverture. Le lecteur par programme est joué sur les cartes masquées et non masquées, et la commande `gardes` rapporte, par espèce, la part des cartes dont D baisse ou devient indécidable sous le masque : c'est cette mesure qui dira si (d) vaut ce travail pour la course suivante. »
- Le rédacteur peut fixer une autre confiance, à condition de la motiver.

**D7 — mineur — critères, § 1 (lecture de C4).**
- Ancien : « la part des cartes dont le D du lecteur par programme baisse entre la forme non masquée et la forme masquée. »
- Nouveau : « la part des cartes dont le D du lecteur par programme baisse, ou devient indécidable, entre la forme non masquée et la forme masquée (les deux comptes sont rapportés à part). »
- Aucun programme ne change : `gardes` rend déjà les deux comptes.

Tous ces textes anciens figurent une seule fois dans leur pièce ; je l'ai vérifié par recherche sur le fichier nommé. Le différentiel v4 → v5 (critères § 15, note § 10.3) gagne une ligne « D1 à D7 », ou bien les pièces v6 portent leur propre différentiel.

## 8. Ce que j'ai lu, et incidents

- **Lu en entier** : le mandat et son complément ; le rapport ; les sept différentiels ; l'outil ; la note v5, lignes 274 à 345 ; les lignes des v5 citées ici.
- **Lu en partie** : la ligne R-3890 de `registres/decisions.md` sur `origin/main`, dans une copie `copies/decisions-main.md` de mon dossier ; les lignes 176 à 183 des critères v3, pour la lettre du veto.
- **Mes copies et mes défauts glissés** sont dans `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/contre-lecture-juge-v4/controle-v5/` (`programmes/` et `mutant-m1/` à `mutant-m6/`).
- **Jamais touché** : aucune carte, aucun fichier de cartes ni de sélections, le champ `meta`, rien sous `archives-reponses-modeles/` ni sous `/root/.claude/`, aucun fichier, branche ou ligne interdits.
- **Incident** : le complément 1 n'était cité que par son empreinte. J'ai essayé un premier nom, absent, puis un second, juste ; je n'ai lancé aucune commande de liste.
- **Aucun refus** d'outil ni de classifieur. Aucun heredoc, aucun code passé en ligne. Une commande simple par appel.

*contre-lecteur, modèle O*
