# Relecture des lignes touchées v4 → v5 du code de la condition 6 — témoin Bailey — v1

- Lecteur : R2, sous-agent neuf. Je n'ai écrit ni le texte scellé, ni le code, ni les essais, ni les rapports, ni la
  liste des lectures. Date : `date -u` = Tue Nov 10 14:05:20 UTC 2026 (fin des sondes).
- Je reçois d'office le `CLAUDE.md` du dépôt (`b4cbc66a422a6246df0479fe0c886eccb92cd3410d6a8b742eddea5325098eae`).
- Dépôt : `/home/user/controle-ia-travail`, branche `claude/compassionate-meitner-d4ryyk`, commit `93464221`, arbre
  propre avant ce rapport ; `origin/main` = `617d77d4`.
- Pièces lues et empreintes (SHA-256, sur disque) :
  - texte qui prime : `prereg/temoin-attaque-publiee-bailey-v1.md` (`fb6c2f34355d98ba08798cab1a4964a03b41eedf57d687454663f01c9646f2c3`), l. 295-380 (gardes de fin de run, ce qui sort de l'instance, critères de lecture, liste d'arrêt, conditions de lancement) ;
  - rapport appliqué : `relecture-lignes-touchees-code-condition6-v4-bailey-v1.md` (`ff6c76c71397016b2c8eeedd0fdff49c7d1f8913ebe0b8bf46984434d816dea6`), en entier ;
  - liste des lectures : `lectures-a-acter-addendum-condition6-v3.md` (`ab0d34d83eb2e94cc7e64ea77cdf31ada5e519e8120e458fbc8ff088b9fff37a`), lectures 1-35 (tableau) ;
  - code, par `diff -u` : `lanceur_v4.py` (`638f90fe…`) → `lanceur_v5.py` (`8efc746448c7837515c6fdd022a36a53971c44e83a339ffb682350f1c9ffa335`) ;
    `instance_v4.py` (`cbb2f1d3…`) → `instance_v5.py` (`0d170bfa49d0b9a3aa0d03c99fa0f5888cc3572c0e535680792f130b66eee57a`) ;
    `lecture_v3.py` (`66c27382…`) → `lecture_v5.py` (`f322f78a7f19247878f60059099a1221c8348885d005eb9bfab73657bb8a29f6`) ;
    plus, pour le contexte des lignes touchées : `lecture_v5.py` l. 74-260 (`lire_jsonl`, `gardes_tombees`, `_budget`,
    `issue_pilote`, `relance_permise`, `tours_journal`, `k_prime`, `tours_complets_instance`, `dossier_de_foi`) et
    `valider` en entier ; `instance_v5.py` `empreintes`, `main` ; `lanceur_v5.py` `verifier_veilleur`,
    `_lancer_veilleur`, `_veilleur_ok`, `_garde_veilleur` ; `analyse_v3.py` `validite`, `garde_fin_de_run` ;
    `journaliseur_v3.py` l. 55-75 (`_ecrire`) ; `conventions_v3.py` (noms des journaux) ;
  - essais : `tests/test_temoin_bailey_condition6_v5.py` (`b10770cb49a8a06d69cfc26a7bad2798679ea6305ac94b8230776bc91735d844`) : aides (l. 1-175), essais C8 (l. 192-300), liste des essais ; aide `poste_local` de l'essai v3 ;
  - sondes : les miennes sur la v4, `…/scratchpad/diff-c6-v4/test_sondes_r2_v4.py` (`28646e88…`) ; rejouées par le
    rédacteur, `…/scratchpad/c6-v5/test_sondes_r2_rejouees_v5.py` (`5ebd6a5f15f26c498ed910bf5c75bddbc083380b8a8b2e40537cbdb9dfc1a7e6`) ;
    neuves : `/tmp/claude-0/-home-user/157246e4-0739-5bb4-9302-ec187f3c5161/scratchpad/diff-c6-v5/test_sondes_r2_v5.py`
    (`054e7d30be821fd85806d6a8f8768fbec9664fc4ea86dc3d226a2becc447e0cc`).
- Non lu : `donnees/`, `docs/notes/bras-attaque/`, `docs/notes/programme-et-4-familles-evasion/`, `diag/`, tout
  résultat, note ou seuil de sonde ou de moniteur du programme, tout résultat d'attaque contre le juge de l'organisme,
  `registres/decisions.md`, `registres/etat.md` ; le reste du texte scellé ; les lignes non touchées du code, hors le
  contexte nommé ci-dessus ; le code public des auteurs.
- Outils : `sha256sum`, `git` (aucune requête réseau), `diff -u`, `grep`, `sed`, `pytest`. Essais demandés (avec
  `TEMOIN_BAILEY_CLONE=…/public-bailey/obf`) : **29 passés**. Sondes rejouées : **6 échouent, 4 passent**, comme le dit
  le rédacteur. Sondes neuves (chacune passe quand le défaut est présent) : **7 passées** (6 sondes, 1 contrôle).
  `vastai` absent de la machine : ni appel ni `--help`. Aucune dépense, rien de committé. Rapport non scellé.

Renvois : « La l. n » = `lanceur_v5.py` ; « I l. n » = `instance_v5.py` ; « Le l. n » = `lecture_v5.py` ; « M-x » =
sonde neuve de ce lecteur.

## Verdict

**Aucune correction bloquante. C8 à C11 et N-4 sont faits ; les sondes N-1 à N-5 tombent.** Point central (R4) :
l'état reconstitué **ne rend lisible aucun run que le texte dit non interprétable ou sans verdict** (section 1, C8).
Restent deux défauts **à corriger avant l'instance** (M-1, M-2), qui tous deux rendent, dans un cas rare de double
panne, *moins* que le texte (« non interprétable » ou lecture impossible là où le texte lit K′), jamais plus ; et trois
points **à préciser à l'addendum** (M-3, M-4, M-5), plus une phrase fausse de la lecture 13. L'addendum peut être
écrit (après le mot de Lazar sur les lectures à acter), M-1 et M-2 corrigés ou déclarés à la lecture 13.

## 1. C8 à C11 et N-4

| # | État | Lignes v5 | Constat |
|---|---|---|---|
| C8 | fait | I l. 55-57, 60-64, 555-585, 605-608, 617-620 ; La l. 920-927, 988, 993, 997, 1001, 1021-1053, 1204-1206 ; Le l. 227-246, 287-297, 320-350, 384-385, 541-560 | `tours --ecrire-etat` écrit l'état absent, jamais d'écrasement (relu juste avant l'écriture), `reconstitue: true`, `code_retour` 1, cause dans une liste fermée (hors liste : garde, code 3, rien d'écrit ; essai `test_C8_reconstitution_…`), K et graine au manifeste, aucune note lue ; écriture atomique (`.tmp` puis `os.replace`) ; le `.tmp` n'est pas dans `SORTANTS`, donc ni empreinté ni transféré. Appelé sur `MORT` après l'arrêt du groupe (La l. 980, 1044) et, dans `_finir`, avant `_rapatrier`, pour chaque exécution arrêtée par PID avec sa cause (dépense, échéance du GO, instance injoignable, arrêt par la conduite). Sondes N-1, N-1-bis tombent ; essais de bout en bout C8 (K′ = 21 sans relance ; 3 tours puis relance complète ; seuil local). Réserves : M-1, M-2. |
| C9 | fait | La l. 1230-1247 | destruction en échec : veilleur à échéance 0 **toujours** lancé ; l'ancien arrêté si le nouveau est vu vivant, sinon gardé avec alerte ; échec du lancement : ancien gardé, alerte. Sonde N-2 tombe. Réserve : M-4. |
| C10 | fait | La l. 713-724, 929-935, 980 | sur `MORT`, `commande_arret` avant `tours` et avant toute relance ; TERM, attente bornée (10 s), KILL, sur le groupe. Éprouvé en bash réel (E `test_N3_bis_inverse_…`, `test_C10_…`). La sonde N-3 d'origine passe encore **parce qu'elle cherchait la forme v4** (`kill -TERM` en tête de commande) : la forme v5 commence par `p=$(cat …)` ; sa forme adaptée échoue : explication vérifiée. N-3-bis passe encore **parce qu'elle décrit la prémisse** (meneur tué, membre vivant, sondage « mort »), que C10 ne change pas et traite ensuite : vérifié. |
| C11 | fait | La l. 107, 117-118, 139-148, 782-786, 1086-1092, 1259-1295 | étiquette `temoin-bailey-c6-` + 16 hexadécimaux aléatoires, passée à `--label` et écrite à l'ordre de lancement ; si `creer` lève : inventaire `show instances --raw` filtré par **égalité stricte** sur cette seule étiquette, destruction de ces seuls identifiants (3 essais), sinon alerte « création incertaine : inventaire R10 manuel » (inventaire illisible, vide, ou destruction en échec). Aucune instance hors du poste ne peut être visée : l'étiquette est neuve par conduite, et le filtre ne retient rien d'autre. La sonde N-5 d'origine passe encore **parce que l'inventaire factice des essais rend `[]`** (instance inconnue) : rien n'est détruit et l'alerte est posée, ce qui est voulu ; sa forme adaptée (inventaire qui connaît l'instance) échoue : vérifié. Non vérifiable ici (`vastai` absent) : l'option `--label` et le champ `label` ; la lecture 35 le met « à établir avant l'instance », à juste titre. |
| N-4 | fait | La l. 653-669, 672-689, 692-698, 713-724 | identité = `boot_id` + heure de départ (champ 22 de `/proc/<pid>/stat`, compté après le nom : `sed 's/^.*) //'` gourmand, champ 20 ensuite ; correct même si le nom contient « ) ») écrite dans `.debut` **avant** le fichier PID ; « vivant » exige la même identité ; l'arrêt ne vise le groupe que si le meneur a cette identité ou n'existe plus (le numéro de groupe ne peut alors être tenu que par le même groupe). `setsid` lancé par `&` dans un shell non interactif n'est pas meneur de groupe, donc ne refourche pas : `$!` est bien le meneur. Sonde N-4 tombe. Remarque : après le redémarrage d'un **conteneur** sur le même hôte, le `boot_id` ne change pas ; c'est l'heure de départ qui sépare les deux processus, ce qui suffit (risque déclaré de la lecture 32). |

**Remarque R10 de la v4** (veilleur récolté puis signalé) : faite, La l. 527-545, 575-582 (`Popen` gardé par PID ;
`send_signal` sans effet sur un processus récolté ; un PID inconnu n'est plus récolté).

**L'état reconstitué ne rend lisible aucun run que le texte refuse (R4).** Vérifié sur les lignes touchées :
- l'état reconstitué porte toujours `code_retour` 1 et une cause : `finie` est faux (Le l. 362), il n'est jamais lu
  comme un run complet ; K′ est recompté par la lecture sur les journaux transférés (Le l. 355-360), pas pris à l'état ;
- « sonde orientée » tombée : relue aux journaux des gardes par la reconstitution comme par la lecture (Le l. 383) →
  « non interprétable » ;
- « dépense », « échéance du GO » : `_budget` → ni reprise du pilote (« arrêt ») ni relance (Le l. 105-136) ;
- K′ < 20 sans relance → « pas de verdict » (`analyse_v3.validite`) ; seconde erreur de la relance avant 20 tours →
  idem ; relance faite à K′ ≥ 20 → « relance hors de la liste d'arrêt », garde de fin de run tombée (essai
  `test_C8_relance_hors_liste_…`) ;
- la garde de fin de run (`garde_fin_de_run`) est inchangée : tous les journaux attendus, tours 0…K′ − 1 avec leurs
  étiquettes, empreintes égales, notes scellées.
Le seul assouplissement est la reconstitution **à la lecture** de l'état de la première exécution d'une relance
(Le l. 330-331), qui présume une cause non budgétaire : voir M-5.

**Deux cas du texte.** (a) K′ ≥ 20 sans relance (l. 338, 372) : lu sur K′, interruption rapportée (`interruptions`,
Le l. 384-385, et `lire`, Le l. 541-560) ; (b) relance complète (l. 371) : seule la relance porte le verdict, la
première exécution rapportée comme interrompue (Le l. 333-345). Conformes, sauf la condition « état présent », que
M-1 et M-2 mettent en défaut dans des cas rares.

**Destruction garantie.** Inchangée hors C9 et C11 ; voir M-4 pour la vérification du nouveau veilleur.

**Ce qui sort de l'instance.** L'état reconstitué ne contient que : phase, K, graine, code, cause, durées, nombre de
tours marqués et complets, noms des gardes tombées, cause d'un journal absent, message. Aucune note, aucun texte, aucun
suffixe ; `configuration_effective` = « non décidée ». Conforme à « Ce qui sort de l'instance » (l. 312-315) et à la
lecture 12.

**Aucune valeur de clé sur une ligne de commande.** Les commandes neuves (`tours --ecrire-etat --phase --manifeste
--cause`, `commande_arret`, `commande_detachee`, `create … --label`, `show instances --raw`) n'en portent aucune ;
contrôle `test_controle_commande_tours_sans_cle_et_cause_intacte` (la cause « coupure de l'hôte », apostrophe comprise,
passe intacte par `shlex`). Le jeton reste envoyé par fichier (inchangé).

## 2. Défauts neufs

**M-1 (à corriger). Reconstitution en échec sur une exécution morte : jamais retentée.** La l. 1044-1046 : si
`tours --ecrire-etat` échoue une fois (sondage passager), `t` = None, pas de relance (voulu), mais l'exécution n'entre
pas dans `self.arretees` : la boucle de `_finir` (La l. 1204-1206) ne la retente pas. Si le transfert réussit ensuite,
l'exécution est transférée **sans état** ; la lecture fait alors tomber la garde de fin de run : « non interprétable »
pour K′ ≥ 20, là où le texte (l. 338, 372) lit un run tronqué de K′ tours. Sondes
`test_M1_reconstitution_en_echec_jamais_retentee` et `test_M1_bis_…`. Cela contredit aussi la lecture 13 de la liste
(« toujours présent pour une exécution transférée »). Correction : sur `t is None`, inscrire la phase dans
`self.arretees` avec « coupure de l'hôte » (ou retenter dans `_finir` toute exécution transférable sans état connu) ;
essai : M-1 inversée (deux écritures demandées, la seconde dans `_finir`). Ne change l'issue que dans une double panne,
et vers moins de verdict, jamais plus : non bloquant.

**M-2 (à corriger). Ligne finale tronquée d'un journal : exception hors `GardeArret`, à l'instance comme à la
lecture.** Le cas que C8 ouvre (coupure de l'hôte, KILL par la conduite au bout de 10 s) peut laisser une dernière ligne
coupée dans un journal JSONL. `lire_jsonl` (Le l. 74-78, inchangée, mais désormais atteinte sur ces exécutions) lève
`json.JSONDecodeError` ; `tours_complets_instance` n'attrape que `GardeArret` : `reconstituer_etat` lève (I l. 567),
`main` n'attrape que `GardeArret` (I l. 655), aucun état n'est écrit ; et `valider` lève de même (Le l. 355-358 :
`except GardeArret` seulement) : lecture impossible, comme N-1. Sondes `test_M2_reconstitution_leve_hors_GardeArret`,
`test_M2_bis_lecture_leve_hors_GardeArret`. Le journaliseur écrit ligne par ligne avec `flush` et `fsync`
(`journaliseur_v3.py` l. 62-65), donc le cas est rare (coupure brutale de l'hôte, signal fatal au milieu d'une grande
écriture). Correction minimale : `lire_jsonl` lève `GardeArret` (« journal illisible ») sur une ligne non JSON ; et
écrire à l'addendum comment se lit une **dernière ligne sans fin de ligne** (ignorée, le tour en cours n'étant pas
complet ; ou garde tombée). Essai : M-2 inversée.

**M-3 (à préciser à l'addendum). Pilote arrêté une seule fois, sans reprise : libellé « seconde chute ».** Un pilote
dont l'état (reconstitué ou non) porte une cause non budgétaire (« instance injoignable », « arrêt par la conduite »)
et qu'aucune reprise ne suit est lu « Pas de run principal, pas de verdict (seconde chute du pilote) ; nœud »
(Le l. 307 ; sonde `test_M3_…`). L'issue est juste (l. 366 : pas de run principal, nœud), le libellé faux. À dire à la
lecture 17 ou 33, ou à corriger dans le libellé.

**M-4 (à préciser). C9 : le nouveau veilleur est « vu vivant » sur le battement de l'ancien.** `_lancer_veilleur`
réemploie `self.journal_arrets` (La l. 850-854) : un seul fichier `.battement` pour les deux veilleurs ;
`verifier_veilleur` (PID vivant + battement frais, La l. 554-572) ne sait pas lequel a battu. L'ancien peut donc être
arrêté alors que le nouveau, vivant à l'instant de la vérification, n'a encore rien fait (sonde `test_M4_…`, sur le
code). Sans effet sur une issue tant que le nouveau vit ; à dire à la lecture 34, ou journal propre au veilleur de
destruction.

**M-5 (à préciser).** La reconstitution à la lecture de la première exécution d'une relance (Le l. 330-331) prend la
cause « état absent » : `relance_permise` la lit comme une erreur non budgétaire, donc une relance faite après un arrêt
par la dépense ou l'échéance serait acceptée si l'état manquait. Le code de la conduite ne relance jamais après un
arrêt (`_Arret`), et aucune entrée ne reprend à la relance (lecture 25) : sans effet sur ce code ; à écrire à la
lecture 13 comme présomption, ou à recouper avec la cause notée au journal de la conduite (`conduite-v5.jsonl`).

**Lecture 34 (mot).** La liste dit « l'ancien veilleur est arrêté s'il est vu vivant » ; le code l'arrête si **le
nouveau** est vu vivant (La l. 1239-1240). À corriger dans la liste.

## 3. Corrections

- Bloquant : aucune.
- À corriger avant l'instance (non bloquant pour l'écriture de l'addendum, essai inversé chacun) : **M-1**, **M-2**.
  Si l'un n'est pas corrigé, le déclarer à la lecture 13 (état absent malgré C8 → « non interprétable », ou lecture
  impossible), au lieu de « toujours présent ».
- À préciser à l'addendum : **M-3** (libellé), **M-4** (vérification du nouveau veilleur), **M-5** (présomption de la
  reconstitution à la lecture), lecture 13 (« toujours présent » faux sans M-1), lecture 34 (qui est vu vivant) ;
  rester « à établir avant l'instance » : `--label` et le champ `label` de `vastai` (lecture 35).

Après M-1 et M-2 : relecture des seules lignes touchées et des sondes M-1, M-2 inversées ; puis l'addendum, après le
mot de Lazar sur les lectures à acter (4, 6, 7, 8, 13, 16, 24, 25, 26, 31).
