# Relecture des lignes touchées v7 → v8 du code de la condition 6 — témoin Bailey — v1

- Lecteur : R2, sous-agent neuf. Je n'ai écrit ni le texte scellé, ni le code, ni les essais, ni les rapports, ni la
  liste des lectures, ni les sondes du relecteur précédent. Date : `date -u` = Tue Nov 10 17:23:13 UTC 2026 (fin des
  sondes).
- Je reçois d'office le `CLAUDE.md` du dépôt (`b4cbc66a422a6246df0479fe0c886eccb92cd3410d6a8b742eddea5325098eae`).
- Dépôt : `/home/user/controle-ia-travail`, branche `claude/compassionate-meitner-d4ryyk`, commit `9d395815`, arbre
  propre avant ce rapport.
- Pièces lues et empreintes (SHA-256, sur disque) :
  - décision : `registres/passations/2026-11-10-1657-decision-lazar-lectures-et-pilote.md` (`d4f21aa5849ed49c34ab3f4c4ff8c50a16de998eced1bf71d8a785f1cfebd932`), en entier ;
  - rapport appliqué : `relecture-lignes-touchees-code-condition6-v7-bailey-v1.md` (`5831e98c5be3f8c69940c171b088fdf93c591aab8745e0c1cc7f93956123f5be`), en entier (A-1, A-2) ;
  - texte qui prime : `prereg/temoin-attaque-publiee-bailey-v1.md` (`fb6c2f34355d98ba08798cab1a4964a03b41eedf57d687454663f01c9646f2c3`), l. 238-262, 338-386 (liste d'arrêt, l. 366) ; R4, R5 du `CLAUDE.md` ;
  - code, par `diff -u` : `lecture_v7.py` → `lecture_v8.py` (`1657a492d7229a9f3cd37c2094a012cf2cb629d8e7e6b91632895586e9d9a00a`) ;
    `instance_v7.py` → `instance_v8.py` (`7e4c2dc8625ed6874c5a22ff1ce98d8c2d1a219aa40fe27a7b24c0360e8be19b`) ;
    `lanceur_v7.py` → `lanceur_v8.py` (`5d85ca45387a33f5e3e85c9ff6ccfb3a35f9402d1cbba3eea165fc44537819b3`) ;
    contexte : `lecture_v8` `_lire_jsonl`, `issue_pilote`, `relance_permise`, `valider` (pilote) ; `lanceur_v8`
    `_tours_relus`, `_executer`, `conduire` (l. 1080-1230), `normaliser_execution`, `lire_etat` ; `instance_v8`
    `_ajouter`, `Surveillance` (l. 400-412), `main` (`tours`) ; `journaliseur_v3` `_ecrire` (l. 63), `ajouter_ligne`,
    `_garde` ; `execution_v3._consigner_garde_lanceur` ; `conventions_v3` l. 72-81 ;
  - essais : `tests/test_temoin_bailey_condition6_v8.py` (`c86091610ca2ac104a17f08adebcc05b14b7998c931dcb617ea87eeb3e243a4b`), par `diff -u` avec `…_v7.py`, et les essais A-1, A-2 en entier ;
  - lectures : `lectures-addendum-condition6-v5.md` (`5e423b504260ebf6125a6b734817b6363edd20502581b2128d74a7c0e0594502`), en-tête, colonnes « État » et « Acte » de toutes les lectures, lecture 36 en entier, conclusion ; colonne « À acter » de la v4 `lectures-a-acter-addendum-condition6-v4.md` (`351c778c796ef8cafdec135c2446bff1677356b037683e85bd22c05dd7ee0996`), pour le point (3).
- Non lu : tout le reste du dépôt ; aucun des répertoires ou lignes cloisonnés ; aucun journal, aucune note, aucun
  résultat ; aucune clé ; aucune requête réseau ; pas de `vastai`.
- Outils : `diff -u`, `sed`, `grep`, `awk`, `sha256sum` ; `pytest` (venv du dépôt), avec `TEMOIN_BAILEY_CLONE` du clone
  obfusqué. Essais v8 : **54 passés** (74 s). Sondes du relecteur précédent rejouées sur la v8
  (`…/scratchpad/c6-v8/test_sondes_r2_v7_sur_v8.py`, `e64fadb333001c1cc83546635042d28d584e5560dbfcb7a4c4356662a821d661`) :
  Q1 et Q2 **échouent** (raison de fond, § 2). Sondes neuves :
  `/tmp/claude-0/-home-user/157246e4-0739-5bb4-9302-ec187f3c5161/scratchpad/diff-c6-v8/sondes/test_sondes_r2_v8.py`
  (`5944681826b69385672d3a33c939111b04da7b84bbe3a4dc23fd8831f8d87d3b`) : S1 et S2 affirment chacune un écart et
  **passent** (écart présent) ; S3 est une sonde de contrôle (passe : champ juste). Correction proposée éprouvée sur une
  copie du code hors du dépôt (`…/diff-c6-v8/copie/`, `pytest -o pythonpath=…`) : 54 essais v8 passés, S1 échoue ;
  `…/diff-c6-v8/sondes/verif_correction.py` (`b7c549542877e46b1042fc80e676d34932ca7fcec953281728b9decaab998b69`).
  Aucune modification du dépôt hors de ce rapport.

## 1. Verdict

**Une correction exigée avant l'addendum (C-1, bloquante, quatre lignes et un essai), puis conforme : l'addendum peut
être écrit.** A-1 et A-2 sont appliqués et sûrs dans tous les cas où la conduite voit l'état du pilote. Reste un chemin
(réserve 2 du rédacteur) où la conduite fait la reprise et le run principal sur une ligne de garde coupée qu'elle ne
voit pas : contraire au mot de Lazar (« pas de reprise, pas de run principal ») et, si la ligne perdue était
« sonde orientée », à la l. 366. Trois points à préciser à l'addendum (P-1 à P-3), sans effet sur une issue.

## 2. A-1 et A-2 — appliqués

- **A-1** (`tours_journal`) : `lanceur_tombe = coupee_l or any(...)`, `dernier` ne dépend plus que de `coupee_g`,
  `ligne_de_garde_coupee` vrai à tous les tours si `coupee_l`. Une ligne coupée des gardes du lanceur vaut une ligne
  « tombée » entière : K′ = 0. Le cas du journal des gardes (C-3) est inchangé. Sonde Q1 : échoue (K′ = 0 dans les deux
  cas) ; `test_Q1_inverse…` le fige. « Jamais un tour de plus » est vrai pour les deux journaux.
- **A-2** : `gardes_tombees` nomme toute dernière ligne coupée d'un journal de gardes
  (`LIGNE_DE_GARDE_COUPEE`, toujours présent) ; `issue_pilote` rend « ligne de garde coupée » sur ce nom **ou** sur un
  chemin de journal de gardes dans `lignes_tronquees_ignorees` (`endswith` sur `journal/gardes-v3.jsonl` et
  `gardes-lanceur-v3.jsonl` : aucun autre journal ne finit ainsi) ; testé avant `_budget`, après « sonde orientée » ;
  la conduite s'arrête (pilote ou reprise), sans règle ni run principal ; `valider` relit les journaux de gardes
  transférés de chaque pilote et rend `ETAT_LIGNE_COUPEE_PILOTE`. Mêmes priorités dans la conduite et dans `valider`.
  Sonde Q2 : échoue (« sonde orientée » lue). Une ligne illisible au milieu d'un journal de gardes du pilote lève
  (`GardeArret`, essai). Instance : seuls les imports passent à `lecture_v8`. Lanceur : imports, `INSTANCE_MODULE`,
  `CHEMINS_ARCHIVE`, module du veilleur, branche d'arrêt.

## 3. Réserves du rédacteur

**(1) Nom de garde lu dans le préfixe d'une ligne coupée — sûr, jamais plus favorable.**
- Le nom n'est rendu que si le préfixe porte, en entier et dans cet ordre, `{"etat": "tombée", "garde": "<nom>"`
  guillemet fermant compris (`json.loads` de chaque chaîne) ; une coupure dans le nom, dans un échappement ou dans un
  caractère multioctet du nom ne rend rien. Le retrait de 1 à 3 octets de fin ne touche que la queue d'un caractère
  coupé ; un octet invalide ailleurs fait échouer les quatre décodages.
- Il ne peut que durcir : au pilote, `LIGNE_DE_GARDE_COUPEE` est **toujours** ajouté, donc l'issue est « ligne de garde
  coupée » (arrêt, nœud) ou, si le nom est « sonde orientée », « non interprétable » : pas de run principal dans les
  deux cas. Au run principal, un nom lu ne peut que retirer la relance (« sonde orientée », « dépense » via `_budget`) ;
  aucun nom ne l'ouvre (`relance_permise` ne lit pas d'autre nom). `tours_journal` ne lit pas les noms.
- Ordre des clés : vrai pour les lignes du journaliseur (`_garde` : `etat`, `garde`, `message`, `t`, `tour`) et pour
  `execution_v3._consigner_garde_lanceur` (`etat`, `garde`, `message`, `tour`). **Faux** pour la ligne
  « configuration effective » de `instance_v8.Surveillance` : ses clés `empreinte_attendue`, `empreinte_observee`
  précèdent `etat` ; la ligne commence par `{"empreinte_attendue"` et son nom n'est **jamais** lu (sonde S2). Sans
  effet : garde inconnue, donc arrêt au pilote, et K′ = 0 par A-1 au run principal. → **P-1**.

**(2) Pilote mort dont la reconstitution par `tours` échoue — écart ; correction C-1, bloquante.**
- Chemin (sonde S1, de bout en bout, instance jouée) : le pilote meurt pendant l'écriture d'une ligne de garde ;
  `_tours_relus` rend `None` ; `_executer` rend `normaliser_execution(MORT_SANS_ETAT)` avec `tours_complets = None` et
  **sans** `lignes_tronquees_ignorees` ; `issue_pilote` ne voit ni le nom ni le chemin : « chute ». La conduite lance
  la reprise ; si elle finit, la règle et le run principal. Dans `_finir`, la seconde tentative de `tours` (M-1) réussit,
  l'état reconstitué porte la ligne coupée, et `valider` rend `ETAT_LIGNE_COUPEE_PILOTE` : pas de verdict, après la
  dépense de la reprise et du run principal.
- Écart : au mot de Lazar du 10 novembre (« une ligne de garde coupée au pilote arrête tout (pas de reprise, pas de run
  principal ; nœud) ») ; à la l. 366 si la ligne perdue était « sonde orientée » (run principal lancé que le texte
  exclut) ; à la liste d'arrêt dans les deux cas, par une dépense qu'aucune ligne ne permet sous la lecture actée.
  C'est le cas même où les lignes coupées naissent (coupure de l'hôte). La lecture 36 (f) le déclare (« Point
  déclaré »), mais dit aussi « Risque déclaré, réduit : au pilote, aucun » et « Aucune lecture du pilote n'ouvre la
  reprise sur une ligne de garde coupée » : les deux phrases sont fausses tant que ce chemin existe.
- **C-1 (exacte)**, dans `lanceur_v8.Conduite.conduire`, boucle du pilote, juste après `pilotes.append(r)` :
  ```python
                if r.get("tours_complets") is None:  # pilote mort, gardes illisibles : ligne coupée non exclue (A-2)
                    bilan["pilote"] = pilotes
                    bilan["arret"] = ("pas de run principal ; pilote mort, état des gardes illisible (garde "
                                      "inconnue) ; nœud")
                    return bilan
  ```
  C'est la règle déjà tenue au run principal (« exécution principale morte sans état, tours complets illisibles : pas de
  relance ; nœud », M-1) : état inconnu, aucune nouvelle exécution. Plus un essai : S1 inversée (pilote mort, première
  reconstitution en échec → `f.lance` s'arrête à « pilote », bilan ci-dessus, instance détruite ; `valider` rend
  `ETAT_LIGNE_COUPEE_PILOTE` si la ligne coupée est transférée). Éprouvée sur copie : les 54 essais passent, S1 échoue.
  Coût : sans ligne coupée, une reprise que le texte permettait est perdue (nœud au lieu d'une reprise) ; c'est la
  lecture « garde inconnue au pilote = arrêt » du même mot de Lazar, à écrire à la lecture 36 (f) en remplaçant le
  « Point déclaré » ; « au pilote, aucun » devient alors vrai.
- Bloquante : oui. Elle change une issue (reprise et run principal faits, contre arrêt) et la décision de Lazar exclut
  précisément cette reprise. Seule autre voie : la laisser telle quelle comme risque déclaré, ce qui demanderait un mot
  de Lazar contraire au sien de 16:57 ; je ne la recommande pas.

**(3) Lectures « non » de la v4 marquées « déclarée, aucun acte demandé » — juste.** Vérifié ligne à ligne : les 22
lectures « non » à acter de la v4 sont, en v5, « déclarée » (5, 9 à 12, 14, 15, 17 à 22, 27 à 30, 32 à 34) ou « à
établir avant l'instance » (23, 35), comme en v4 ; les 14 « oui » ou « actée » sont actées par les deux mots de Lazar.
Le libellé est fidèle : Lazar a acté la liste v4 « telles qu'écrites », colonne « non » comprise. Je ne rejuge pas le
fond des lectures déclarées (hors des lignes touchées).

**(4) Champ `gardes_tombees` de la ligne `ETAT` de `tours` (sans `--ecrire-etat`) — non éprouvé, juste, sans effet.**
La conduite v8 n'appelle jamais `tours` sans `--ecrire-etat` (`_tours_relus`, seul appel, l. 1048). Le champ vient de
la même fonction `gardes_tombees` que les chemins éprouvés. Sonde de contrôle S3 : préfixe « sonde orientée » coupé →
`gardes_tombees` finit par `["sonde orientée", LIGNE_DE_GARDE_COUPEE]`, le chemin est signalé, `issue_pilote` rend
« sonde orientée ». → **P-3**.

## 4. Points à préciser à l'addendum (sans effet sur une issue)

- **P-1** (lecture 36 (f)) : « écriture à clés triées : `{"etat": "tombée", "garde": "<nom>"` » vaut pour le
  journaliseur et `_consigner_garde_lanceur`, pas pour la ligne « configuration effective » de l'instance, dont le nom
  n'est jamais lu (garde inconnue ; arrêt au pilote, K′ = 0 au run principal). Même phrase dans la docstring de
  `lecture_v8` (« du journaliseur et de l'instance ») : à corriger à la prochaine version, sans changer de code.
- **P-2** (avec C-1) : sans ligne coupée transférée, `valider` rend le pilote mort non repris sous le libellé
  « Pas de run principal, pas de verdict (seconde chute du pilote) ; nœud » (`verif_correction.py`, cas sain) : même
  issue, libellé inexact, de la classe de M-3 (lecture 17) ; à dire à la lecture 17 ou 36 (f).
- **P-3** : la commande `tours` sans `--ecrire-etat` n'est pas appelée par la conduite v8 ; son champ
  `gardes_tombees` est juste (S3) ; une ligne à l'addendum suffit, ou un essai à la prochaine version.

## 5. Corrections exactes

- **C-1** (bloquante) : les cinq lignes du § 3 (2) dans `lanceur_v8.conduire` (nouvelle version du lanceur selon R12,
  ou v8 si elle n'est pas encore scellée) ; un essai « pilote mort, reconstitution en échec : arrêt sans reprise » ;
  lecture 36 (f) : remplacer le « Point déclaré » par cette lecture ; la conclusion de la liste (« Point déclaré : 36 »)
  de même.
- Rien d'autre. Après C-1 et son essai, sans relecture complète nécessaire (lignes touchées seulement) : **conforme,
  l'addendum peut être écrit**, avec P-1 à P-3.
