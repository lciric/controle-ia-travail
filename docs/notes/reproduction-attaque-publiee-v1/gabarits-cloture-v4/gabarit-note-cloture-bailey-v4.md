v4 : corrections de la contre-lecture de la v3 corrigée (wf_c00aece0-baa : 2 à corriger, 4 remarques) ; la v3 corrigée en place reste dans le bloc-notes, son texte contre-lu d'avant correction n'est pas gardé (constat 6)
v3 corrigée : contre-lecture de la v3 (5 constats)
v3 : corrections de la contre-lecture de la v2 (8 constats)
v2 : corrections de la contre-lecture de la v1 (14 constats)

# Gabarit de la note de clôture — témoin de Bailey, confirmation (addendum 7, § 3) — v4

Gabarit, non une note : chaque champ porte entre crochets la règle du § 3 qui l'exige
(`prereg/temoin-attaque-publiee-bailey-v1-addendum-7-run-de-confirmation.md`, scellé ; citations entre « »). La note
réelle est écrite à partir de ce gabarit, sans les crochets de règle, puis scellée
(`commandes-cloture-bailey-v4.sh e5-sceller-note`). En cas d'écart entre ce gabarit et le § 3, le § 3 prime.

**Aucun champ de note.** [§ 3, « Clôture de la confirmation » : « constatée par une note scellée de la session, qui ne
cite que des champs techniques » ; première puce : seuls sont connus « durées, mémoire, nombre de pas, tours complets,
nom et état des gardes, états des contrôles du juge ».] La note ne cite aucune note de sonde ni de juge, aucun verdict,
aucun K′, aucune valeur d'une sortie de `lecture_scellee_v3` (elles ne sont pas encore écrites) ; elle ne nomme les
attendus que par leur chemin et l'empreinte de leur fichier.

---

## En-tête

- Titre : « Note de clôture de la confirmation du témoin de Bailey (addendum 7, § 3) ».
- Heure UTC d'écriture : `AAAA-MM-JJTHH:MMZ`. [§ 3, « La lecture est faite par le code » : « Dans les 24 h qui suivent
  la note de clôture, la session joue la commande consignée » : l'heure ouvre ce délai.]
- Session, branche, tête du dépôt au moment de l'écriture (`git rev-parse HEAD`).
- Mention de gel : « L'arbre `src/` est gelé au commit `a904aa391cdcf2650b747fe64e48caa0ec8c5849` jusqu'au dernier
  contrôle final. » [§ 4 : « il est écrit en tête de toute passation et de tout brief de cette branche jusqu'au dernier
  contrôle final ».]
- Mention de l'ordre de lecture : « Aucune note du témoin n'a été lue avant cette clôture ; les deux verdicts sont lus
  ensuite (addendum 7, § 1 et § 3). » ou, si une lecture a précédé : ce qui a été lu, par qui, quand, et la liste des
  décisions prises ensuite, chacune « décidée après une lecture ». [§ 1 : « Dès qu'une note ou un verdict du témoin est
  lu avant la clôture […] c'est consigné avec ce qui a été vu ; toute décision prise ensuite […] est rapportée
  « décidée après une lecture » » ; § 5 (e) : « toute passation et tout brief écrits avant la clôture le disent en
  tête ».]

## 1. Cas de clôture (un seul)

Cocher un cas, nommer la cause avec ses seuls champs techniques et les pièces (chemin, empreinte) qui la constatent.

- [ ] **(i)** « les journaux de l'exécution qui porte le verdict sont transférés et scellés (run fini, ou tronqué par
  une ligne de la liste d'arrêt ; après la reprise de la lecture 38 s'il en faut une) ». Champs : exécution qui porte le
  verdict (nom), tours complets au bilan, nom et état des gardes, cause d'arrêt (technique), reprise de la lecture 38
  (oui ou non, chemin du dossier de reprise), relance de la l. 371 (oui ou non). [§ 3, cas (i).]
- [ ] **(ii)** « la confirmation n'est pas lancée ou pas courue, cause nommée » — une seule parmi : refus exprès du mot
  de lancement ; aucune offre (§ 2.4) ; condition du § 2.5 non tenue ; échéance (condition 2) ; garde de mise en place
  non refaite (l. 363) ; contrôle du juge hors seuil (l. 365) ; garde de durée du pilote (§ 2.3), avec t ; seconde chute
  du pilote ; K < 20 à la règle ; journaux perdus (reprise de la lecture 38 impossible) ; autre ligne de la liste
  d'arrêt qui laisse la série sans run principal lisible (laquelle). Préciser si le run principal avait commencé
  (alors lu comme un run interrompu, l. 338). [§ 3, cas (ii) ; « Les deux verdicts » : « cas (ii) ou (iii) après le
  début du run principal, lu comme un run interrompu, l. 338 ».]
- [ ] **(iii)** Lazar y met fin : son mot (verbatim, chemin et empreinte de la pièce qui le consigne), « rapporté comme
  sa décision, avec la réserve du § 1 si une lecture a précédé ». Si un run était en cours : heure de son arrêt, du
  transfert et du scellement de ses journaux (reprise de la lecture 38 comprise), ou constat de leur perte. [§ 3, cas
  (iii) : « si un run est en cours, la note de clôture n'est écrite qu'après son arrêt, le transfert et le scellement
  de ses journaux […], ou le constat de leur perte ».]
- **Suites laissées à la décision de Lazar** (mot de lancement, seconde tentative du § 2.3, mise en place refaite,
  relance par le chemin de l'addendum 5, crédit d'une reprise, nouveau relevé du § 2.5, ligne neuve de la condition 2) :
  pour chacune que la cause laisse ouverte, le mot de Lazar qui y renonce (verbatim, chemin, empreinte), ou le constat
  que l'échéance de la condition 2 est passée (heure). Sinon : « aucune suite ouverte ; note écrite dès le constat ».
  [§ 3 : « la note de clôture cite le mot de Lazar qui y renonce, ou constate que l'échéance de la condition 2 est
  passée ; dans les autres cas, elle est écrite dès le constat ».]
- **Relance par le chemin de l'addendum 5** (s'il y en a eu une) : cible de l'exécution de l'assemblage qui a abouti
  (chemin absolu) ; ou constat du refus des deux exécutions : « pas de verdict » pour ce run, aucune lecture faite pour
  lui. [§ 3, « Refus ou erreur à la lecture » : « la note de clôture nomme la cible de l'exécution qui a abouti » ; « la
  note de clôture le dit et aucune lecture n'est faite pour ce run » ; note écrite « après l'assemblage, ou le constat
  de son refus ».]
- Rappel : « Après la clôture, rien n'est ajouté à la confirmation. » [§ 3.]

## 2. Postes arrêtés et branche récupérée

Pour chaque poste qui a produit un dossier ensuite lu ou assemblé (poste v13, seconde tentative, mise en place refaite,
reprise de la lecture 38, relance par le chemin de l'addendum 5) : marque de fin sur la branche (chemin, commit), ou
machine constatée perdue, ou destruction par la session au plus tôt 1 h après le plus tardif des moments nommés ;
destruction de l'instance (ou mise à l'arrêt gardée, consignée), heure ; heure de la récupération de la branche et
commit de tête après elle. [§ 3 : « La session ne joue un assemblage ni un `--calculer-attendu` qu'après avoir
récupéré la branche une fois constatés, pour chacun de ces postes, son arrêt […] et la destruction de son instance ».]

Heures (UTC), preuve de l'ordre du § 3 : e0 (récupération) ; e1 (listes) ; assemblage d'une relance par l'addendum 5
(chaque exécution) ou constat de son refus, ou « aucun assemblage » ; e2 (vérification des chemins) ; premier
`--calculer-attendu`. Recopiées des lignes du journal de consignation (chemin, empreinte). [§ 3 : « La session ne joue
un assemblage ni un `--calculer-attendu` qu'après avoir récupéré la branche » ; « Avant tout assemblage et tout
`--calculer-attendu`, elle vérifie chaque liste […] puis crée […] » ; « s'il y a un assemblage, aucun
`--calculer-attendu` n'est joué avant celui-ci ou le constat de son refus ».]

Suites permises avant la clôture : pour chacune (seconde tentative du § 2.3, mise en place refaite, relance par le
chemin de l'addendum 5, reprise de la lecture 38), « jouée, poste arrêté » ou « écartée » avec la pièce (mot de Lazar,
échéance passée, suite rendue impossible par la cause constatée). [§ 3 : « Aucun `--calculer-attendu` n'est joué tant
qu'une suite permise avant la clôture […] n'est ni jouée, son poste arrêté comme ci-dessus, ni écartée ».]

## 3. Listes des répertoires

| Dossier que nomme la liste (absolu) | Liste (`<BASE>/repertoires-<C>-v1.txt`) | Empreinte (64 caractères du compagnon) | `sha256sum -c` | Création |
|---|---|---|---|---|
| … | … ou « absente de la branche » | … ou « sans objet » | « OK », « FAILED », ligne mal formée, ou « non scellée » | « n répertoires créés (`mkdir -p`) », ou « rien créé : <cause> » |

[§ 3 : « La note de clôture cite chaque liste et son empreinte, ou son absence » ; « Si une entrée est absolue,
contient `..`, est vide, ou existe comme autre chose qu'un répertoire, ou si la liste n'est pas scellée ou que son
compagnon ne concorde pas, rien n'est créé de cette liste, et c'est rapporté » ; « Une liste est absente si elle n'est
pas sur la branche à cette récupération : rien n'est créé, et c'est rapporté ».]

État de `lecture-assemblee-v1` : « lu dans l'état du dossier dans l'arbre principal au calcul de l'attendu, rapporté
tel quel ; les répertoires que git n'a pas portés depuis les postes des séries 1 à 3 et de la relance ne sont pas
connus ». [§ 3, même puce ; § 5 (f).]

## 4. Pour chaque verdict à lire

Un bloc par verdict : « a » (run à 36 tours, `lecture-assemblee-v1`) et, s'il y a lieu, « b » (confirmation). Si aucun
run principal de la confirmation n'a ses journaux transférés et scellés (cas (ii) ou (iii) avant le début du run
principal, ou journaux perdus), ou si l'assemblage d'une relance par l'addendum 5 a été refusé à ses deux exécutions :
« b : aucun dossier à lire » et la cause. [§ 3, « Les deux verdicts » : « si un run principal de la confirmation a ses
journaux transférés et scellés […], sauf si l'assemblage d'une relance passée par le chemin de l'addendum 5 a été
refusé ».]

| Champ | Valeur | Règle |
|---|---|---|
| Dossier donné à la lecture | chemin absolu dans l'arbre principal | « le dossier donné à la lecture, par son chemin absolu dans l'arbre de travail principal du dépôt (pour la confirmation : la sortie de la conduite ; le dossier de reprise s'il y a eu reprise ; le dossier assemblé […]) » |
| Commit du code | `a904aa391cdcf2650b747fe64e48caa0ec8c5849` | « le commit du code, celui du § 4 et aucun autre » |
| Fichier des empreintes attendues | chemin absolu ; empreinte du fichier (compagnon `.sha256`) ; ligne rendue par `--calculer-attendu`, telle quelle | « le fichier des empreintes attendues, écrit et scellé par `lecture_scellee_v3 --calculer-attendu … --commit <ce commit> --vers …`, joué par la session avec la commande consignée » |
| Chemin de la sortie | chemin absolu, absent à l'écriture de la note | « le chemin de la sortie » ; « il refuse […] si cette sortie, ou son compagnon, existe déjà » |
| Attendu recalculé sous un nom neuf (s'il y a lieu) | ancien et nouveau chemin, cause (commande corrigée à l'essai factice) | « un attendu réel calculé avec une commande corrigée est recalculé sous un nom neuf, R12 » ; « tout chemin neuf […] la note le cite » |

## 5. Commande exacte

Une seule commande, la même pour `--calculer-attendu`, la lecture et `--controler`, recopiée telle que jouée (lignes
« commande : » du journal de consignation, que `commandes-cloture-bailey-v4.sh` écrit avant chaque exécution) :

```
PYTHONPATH=<racine>/src PYTHONPYCACHEPREFIX=<P> <racine>/.venv/bin/python -B -P -m controle_ia.temoin_bailey.lecture_scellee_v3 --calculer-attendu <D> --commit a904aa391cdcf2650b747fe64e48caa0ec8c5849 --vers <A>
PYTHONPATH=<racine>/src PYTHONPYCACHEPREFIX=<P> <racine>/.venv/bin/python -B -P -m controle_ia.temoin_bailey.lecture_scellee_v3 --dossier <D> --sortie <S> --attendu <A>
PYTHONPATH=<racine>/src PYTHONPYCACHEPREFIX=<P> <racine>/.venv/bin/python -B -P -m controle_ia.temoin_bailey.lecture_scellee_v3 --controler <S> --attendu <A> --dossier <D> --empreinte <H>
```

- `<racine>` : … (chemin absolu). `<P>` : … (chemin absolu ; état au premier `--calculer-attendu` : absent, ou
  répertoire vide). Répertoire courant des exécutions : … (sans effet, `-P`).
  [§ 3 : « la commande, la même pour `--calculer-attendu`, la lecture et `--controler` : `PYTHONPATH=<racine>/src
  PYTHONPYCACHEPREFIX=<P> <racine>/.venv/bin/python -B -P -m controle_ia.temoin_bailey.lecture_scellee_v3 …`, où `<P>`
  est un répertoire absent ou vide, hors de `src/` et des dossiers lus, le même pour toutes les exécutions » ; « tous
  chemins absolus » ; « Ils ne changent plus, hors les chemins neufs que permettent ci-dessous la vérification des
  chemins et l'essai factice ».]
- Si une commande a été corrigée à l'essai factice : chaque version essayée, la correction (chemins, arguments,
  variables seulement), et la version retenue. [§ 3 : « Une commande qui y échoue ne se corrige que dans ses chemins,
  arguments et variables, jamais dans le code ».]

## 6. Vérification des chemins

- Script et commande jouée (`verifier_chemins_cloture_v4.py`, chemin et empreinte ; ligne de commande entière), heure,
  résultat (« conforme » : la dernière ligne e2 sans chemin neuf, qui couvre le vérificateur et git check-ignore).
- Chemins vérifiés, tous absolus : `<racine>/src` ; dossiers lus (a, b) ; attendus (a, b) ; sorties (a, b) ; `<P>` ;
  dossier factice ; attendu factice ; sortie factice ; note de clôture ; journal de consignation ; chemins poussés
  ensuite sur la branche (`--pousse` : attendus, sorties, note, journal ; sous `<racine>`, hors de `src/`, de `.git/`
  et des dossiers lus) ; aucun d'eux ni leurs compagnons `.sha256` ignorés par git (`git check-ignore`, joué en e2 : un
  chemin ignoré se remplace avant toute écriture).
- Rapport de chaque lecteur (<CHEMIN_RAPPORT>) : fixé avant cette note (paramètre `RAPPORTS`) et vérifié en e2
  (`--autre`), ligne citée ; un chemin pris après (remplaçant, R12) est vérifié par `verifier_chemins_cloture_v4.py`
  (`--autre`, étape `e2-chemins <chemin neuf>`) avant le lancement, ligne consignée au journal, hors de cette note déjà
  scellée.
- Chaque chemin neuf pris ensuite (commande corrigée, attendu recalculé) : chemin, heure et résultat de sa propre
  vérification, faite avant son écriture.
[§ 3 : « avant le premier `--calculer-attendu`, la session fixe ces chemins et vérifie par programme (chemins résolus,
`Path.resolve().is_relative_to`) qu'aucun chemin d'attendu, de sortie, de `<P>`, du dossier factice, de son attendu et
de sa sortie, ni de la note de clôture n'est sous `<racine>/src` ni sous aucun des dossiers donnés à une lecture » ;
« tout chemin neuf pris ensuite […] passe la même vérification avant d'être écrit, et la note le cite ; la note de
clôture cite la vérification et ses chemins ».]

## 7. Chemins absolus (récapitulatif)

| Rôle | Chemin absolu |
|---|---|
| Dossier lu a | … |
| Dossier lu b | … ou « aucun » |
| Attendu a / b | … |
| Sortie a / b | … |
| Cache `<P>` | … |
| Dossier factice / attendu factice / sortie factice | … |
| Note de clôture (ce fichier) | … |
| Rapport du lecteur a / b (`RAPPORTS`) | … |
| Journal de consignation | … |

[§ 3 : la note nomme « le dossier donné à la lecture, par son chemin absolu », « le fichier des empreintes attendues »,
« le chemin de la sortie » ; « tous chemins absolus » ; aucun d'eux « n'est écrit sous l'un des dossiers donnés à une
lecture ».]

## 8. Essai factice

- Dossier factice : chemin ; construction (programme, sans aucune pièce réelle : `poste_local` des essais du § 4,
  nombre de tours). [§ 3 : « sur un dossier factice de même forme, construit par programme sans aucune pièce réelle
  (comme dans les essais du § 4) ».]
- Attendu factice : chemin, empreinte ; vérification par programme que ses champs `commit`, `code` et `environnement`
  sont égaux à ceux des attendus réels : « égaux » (script ou commande jouée). [§ 3 : « dont les champs `commit`,
  `code` et `environnement` sont égaux à ceux des attendus réels, ce que la session vérifie par programme et que la
  note cite ».]
- Commande jouée (la même qu'en § 5, aux seuls chemins du dossier, de l'attendu et de la sortie près, même `<P>`),
  heure, ligne rendue : **issue** (« aboutie », « refus ou erreur », « refus : empreintes ») et empreinte de la sortie
  factice ; contrôle du factice, s'il a été joué (« conforme » ou « écart »). Aucune valeur du verdict factice n'est
  nécessaire. Pour la règle des 24 h, l'issue retenue est celle de la lecture factice ; un écart du contrôle factice
  est rapporté à côté (ligne « e4 : contrôle factice : écart (lecture factice aboutie ; … ) » du journal). [§ 3 :
  « la commande est jouée telle quelle, aux seuls chemins du dossier, de l'attendu et de la sortie près (même
  `PYTHONPYCACHEPREFIX`) » ; « son issue est citée dans la note ».]
- Si aucune commande n'a abouti dans les 24 h qui suivent le premier essai : le dire, nommer la dernière commande
  essayée, et rappeler qu'elle est jouée sur le dossier réel et que la puce « Refus ou erreur à la lecture » s'applique
  ensuite sans exception. [§ 3, même puce.]
- Ordre : essai joué après le calcul des attendus réels et avant cette note (heures des deux). [§ 3 : « Avant la note
  de clôture, après le calcul des attendus réels ».]

## 9. Suite fixée (rappel, sans règle neuve)

- Lecture : une fois par verdict à lire, dans les 24 h qui suivent cette note, par la commande du § 5 ; empreinte et
  issue rendues consignées sans ouvrir la sortie (au journal : ligne « lancée », puis ligne rendue et code de
  retour ; une seconde lecture du même verdict est refusée ; une exécution sans sortie scellée est rejouée une fois
  par `e6-rejeu`, et un rejeu sans sortie scellée fait constater l'absence de sortie scellée). [§ 3, « La lecture est
  faite par le code ».]
- Lecteurs : deux lecteurs neufs distincts, lancés ensemble dans les 24 h qui suivent la dernière sortie consignée, sur
  `consigne-lecteur-bailey-v4.md` : chemin absolu … ; empreinte … (gabarit v4, avant remplissage) ; consigne remplie
  de chaque lecteur : chemin absolu et empreinte, consignés au lancement. [§ 3, « Les deux verdicts » : lancement
  « (heure, fichiers donnés, consigne) consigné avant qu'aucun des deux lecteurs n'ait rendu ».]
- Commandes : `commandes-cloture-bailey-v4.sh`, rempli : chemin absolu … ; empreinte … ; journal de consignation :
  chemin absolu … ; empreinte à l'écriture de cette note …. [§ 3 : « la commande consignée ».]
- Contrôle final : `--controler` pour chaque sortie, avec l'attendu et le dossier nommés ici et l'empreinte consignée.
  [§ 3, « Cloison de la session jusqu'aux deux verdicts ».] Contrôle final : une fois par sortie ; une commande qui ne
  démarre pas vaut « écart ». [§ 3 : « Un contrôle qui ne peut être joué ainsi vaut « écart » ».] Contrôle final joué dans un seul arbre ; e6-pousser rejoué avant tout changement d'arbre ; une ligne e8 « lancé » sans ligne de résultat vaut « écart » (contrôle qui ne peut être joué une seconde fois).
  Environnement du contrôle final (e7) recréé seulement après la dernière commande sur un dossier réel (e7 refusée
  avant la lecture de chaque verdict et le rejeu dû).
- Poussée sur la branche (e6-pousser) refusée en non-fast-forward : ni pull ni merge (§ 3) ; ces seuls commits sont
  poussés vers une branche neuve (`git push origin HEAD:refs/heads/cloture-bailey-v1`), récupérée par clone au même
  chemin absolu au contrôle final ; sinon, contrôle final joué dans l'arbre principal. Cette voie est fixée ici, avant
  la poussée ; le refus, s'il arrive, et le choix fait sont consignés au journal (cette note, scellée avant, ne les
  porte pas). [§ 3 : « `add`, `commit` et `push` hors de `src/` restent permis » ; « Le contrôle final peut l'être dans un
  arbre recloné au même chemin absolu ».]
