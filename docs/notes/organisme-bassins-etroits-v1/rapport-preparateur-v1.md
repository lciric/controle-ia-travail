# Rapport du préparateur — atelier d'idées sur les bassins étroits, trois générations — v1

Préparateur neuf (Claude Opus 5.5), sous-agent de la session mère, 13 novembre 2026, de 13:03 à 13:29 UTC (heures relevées
par `date -u`). Consigne : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-12-2019-v1/consigne-preparateur-
organisme-bassins-etroits-v1.md` (`d404b6ebf3af013cda9ba05b0bda47d187c9382e43259899560681a6b95003c8`, vérifiée) ; interdits
communs v2 (`1ee3b370…`, vérifiés) appliqués.

## Verdict

**Prêt à contre-lire** (lanceur, essais, conception, question, témoins, devis). **Bloqué pour le lancement** par : le bac à
sable, **inactif dans ce conteneur** (`bwrap` et `socat` absents) ; le recoupement des méthodes, pas encore versé ; la règle
de permission et l'épingle d'empreinte, à écrire par Lazar ; la contre-lecture par un autre modèle ; les relais.

## Pièces (toutes scellées, compagnon `.sha256`)

| Pièce | Empreinte SHA-256 |
|---|---|
| `docs/notes/organisme-bassins-etroits-v1/conception-trois-generations-v1.md` | `4c90a3a52be706823d44c0765fef999e18ceaec02921e13c93b54fb1d32b6ef5` |
| `docs/notes/organisme-bassins-etroits-v1/question-organisme-bassins-etroits-v1.md` | `c188fa9a8ada9c8793bb5a9150596a2583614ee1c8583d8b5ceab226667df7ef` |
| `docs/notes/organisme-bassins-etroits-v1/temoins-bassins-etroits-v1.json` | `748f391ec2dff1687e8c3d3a7c431613c61a023ddcd1ee43708b516020d3900a` |
| `docs/notes/organisme-bassins-etroits-v1/mesurer-consignes-g1-gabarit-40000-v1.json` | `df38474184fbec71a189a0281c0c734b3cf6d0626e467f399e3849d06eb68e95` |
| `docs/notes/organisme-bassins-etroits-v1/devis-organisme-bassins-etroits-v1.md` | `1b311242f71969ff81c4c7b7257a4ed3e641875eb9e22ef8f7e84175c1db0f8d` |
| `scripts/lancer_course_ideation_bassins_etroits_v1.py` | `a10420ccf9fcde31df40d3fd24d480d8815469fc4e6ddd7326ae42ad95ac18c5` |
| `tests/test_lancer_course_ideation_bassins_etroits_v1.py` | `8fa7ae324359d0e4f24235065482c605881afd64ddde134a49e49b0969811ed3` |

## Ce qui est prêt

- **Question** : cœur et contraintes du collisionneur repris mot pour mot (vérifié par programme, espaces normalisés) ; forme
  (1) à (5) devenue Q1 à Q5 du gabarit des fiches ; consigne d'étiquetage `raffine G<g>-R<i>` / `nouvelle` pour la mesure sans
  juge.
- **Témoins** : quatre classes ; chargés sans erreur par le chargeur réel de l'orchestrateur lors d'une **passe simulée
  sans appel** (moteur simulé, sortie dans mon bloc-notes, clone resté propre) : course code 4 et bras code 4, attendus en
  simulation (juges scriptés : ni doublon ni sémantique) ; la passe m'a aussi donné la forme réelle des sorties (classement,
  doublons, clés d'anonymisation, mesures de convergence, coûts au manifeste), que la règle de passage et la garde de cumul
  lisent.
- **Lanceur** (dérivé du v3, nom neuf) : mêmes gardes que le v3 ; GO-2026-11-13-03 lue et exigée (type, Lazar, période,
  révocation, périmètre, plafond ≥ 60) ; argument unique fermé `1`/`2`/`3` ; course puis bras choisis sur l'état du disque ;
  règle de passage ; garde de cumul (dépense relevée + 20 ou + 3,1 ≤ 60, illisible = plafond entier) ; générations 2 et 3
  refusées sans course et bras réussis, manifestes de fin scellés et classement lisible ; aucune relance après dépense ;
  mesure des consignes par l'orchestrateur sans appel et gardes de taille recalculées (orchestrateur et commande d'Argon) ;
  garde du bras sur la consigne en attente réelle.
- **Essais** : **77 passés** (faux orchestrateur, aucun modèle) ; avec les essais du v3, 154 passés, 1 sauté (le clone du v3,
  `/home/user/ideation-organism`, est absent de ce conteneur). Rien écrit dans `runs/` ni dans le dossier de sorties réel.
- **Mesure sans appel** (génération 1, pièce au gabarit de 40 000 caractères) : passe 1 56 691 caractères ; contrôle d'Argon
  322 793 contre une garde de 400 000 ; plancher de la commande d'Argon 1,21 USD (1,45 à 3 caractères par jeton) sous 1,5.
- **Devis** : attendu ≈ 7 USD par génération, ≈ 21 pour trois ; pire cas 17,7 par génération, 53,1 pour trois ; borne 60.

## Bac à sable (consigne § 3.3)

Sonde de l'orchestrateur lancée telle quelle (`pole.adaptateurs.etat_bac_a_sable_detaille`, processus à part, `-I -B`,
préfixe du cache hors du clone, `PATH` de la session), 13:05 UTC :

```
{"actif": false, "proc_neuf": false, "motif": "dépendances du bac à sable absentes : bwrap, socat (par exemple `apt install bubblewrap socat`)"}
```

- **Ce qui manque** : les exécutables `bwrap` (paquet `bubblewrap`) et `socat`, sur le `PATH` (Ubuntu 24.04). Indice, non
  preuve : `unshare --user --net --pid --fork --mount-proc true` rend 0 ici, donc les espaces de noms qu'exige la sonde
  semblent permis ; seule la sonde, relancée après installation, le dira.
- **Je n'ai rien installé** (réseau interdit hors du clone ; et ce serait changer le conteneur de la session).
- **Où la course peut tourner sans contournement** : (a) une **session neuve** dont l'environnement installe `bubblewrap`
  et `socat` par un script de démarrage (proposé par la mère, approuvé par Lazar), sonde relancée telle quelle et exigée
  active avec `/proc` neuf ; (b) ce même conteneur après installation par la mère des deux paquets, si elle l'obtient ; (c)
  la machine jetable de GO-2026-11-13-02, **non payée par cette ligne**. Ce qui s'est fait le 9 novembre : les lignes que
  j'ai lues (R-1978 à R-1994) s'arrêtent au refus, par le classifieur, d'écrire `.claude/settings.json` (R-1994) ; elles ne
  disent pas où la course a tourné ensuite.

## Règle de permission et épingle d'empreinte proposées (non écrites ; à écrire par Lazar, R-1994)

Dans `.claude/settings.json` (projet), à ajouter à côté des règles existantes :

```json
"allow": [
  "Bash(/usr/local/bin/python3 -I -B scripts/lancer_course_ideation_bassins_etroits_v1.py 1)",
  "Bash(/usr/local/bin/python3 -I -B scripts/lancer_course_ideation_bassins_etroits_v1.py 2)",
  "Bash(/usr/local/bin/python3 -I -B scripts/lancer_course_ideation_bassins_etroits_v1.py 3)"
],
"deny": [
  "Edit(//home/user/controle-ia-travail/scripts/lancer_course_ideation_bassins_etroits_v1.py)",
  "Edit(//home/user/controle-ia-travail/scripts/lancer_course_ideation_bassins_etroits_v1.py.sha256)",
  "Edit(//home/user/controle-ia-travail/.claude/hooks/garde_calcul.py)"
]
```

Épingle au crochet `.claude/hooks/garde_calcul.py` (même forme que la garde du lanceur v3, décrite au § (c) de la
vérification `c7542899…` ; je n'ai pas lu le crochet) : toute commande qui cite `lancer_course_ideation_bassins_etroits_v1`
est bloquée sauf si elle est **exactement** l'une des trois commandes ci-dessus, lancée depuis `/home/user/controle-ia-
travail`, fichier présent et non lien symbolique, empreinte égale à la constante
`a10420ccf9fcde31df40d3fd24d480d8815469fc4e6ddd7326ae42ad95ac18c5` **et** au compagnon `.sha256` ; essais du crochet : un
cas sain par génération, un octet changé, compagnon faux, argument `4`, deux arguments, autre interpréteur, autre dossier.
Lancer en arrière-plan, jamais en `bypassPermissions`.

## Refus rapporté tel quel

Entre 13:11 et 13:17 UTC (heures relevées avant et après ; l'instant exact n'a pas été relevé), j'ai voulu éprouver **par exécution** que l'orchestrateur accepte la forme de commande du bras retenue, en la
lançant contre ma sortie simulée dont le bras était déjà joué (refus attendu avant tout appel, commande externe pointée vers
un fichier inexistant). Refusé par le classifieur du mode automatique : « Permission for this action was denied by the
Claude Code auto mode classifier. Reason: [Destructive or Unwanted Actions]. » **Non refait, non contourné.** La forme du bras
retenue est celle du devis du 8 novembre (§ 5, point 4), plus `--budget` du juge et `--budget-controle-usd 0.6`, vérifiée
**par lecture du code** seulement (`demonstrations/ideation_v2.py`, analyseur et branche du bras) : à éprouver par la
contre-lecture.

## Constats en chemin, utiles à la mère

1. **Garde avant envoi de la commande d'Argon** : `commande_argon_v3d.py` refuse sans envoi (code 4) si le plafond de session
   ne paie pas l'entrée (× 1,05) plus 4 096 jetons de sortie et 8 192 de pensée à 41,5 : plancher ≈ 0,51 USD même pour une
   consigne courte. D'où le contrôle du bras à 0,6 (0,2 ne passerait pas ; cohérent avec le 0,95 de R-1864). Au lanceur v3
   (contrôle externe 1,25 pour une consigne de 415 253 caractères), ce plancher vaut ≈ 1,41 à 4 caractères par jeton : **son
   contrôle externe serait refusé par la commande d'Argon** (sans dépense, course arrêtée avant les proposeurs Claude). À
   vérifier si ce lanceur sert encore.
2. Le compte exact de l'interface (`countTokens`) peut dépasser caractères / 4 ; le lanceur garde à 4 et rapporte la lecture
   à 3 ; au-delà, refus sans envoi de la commande d'Argon, sans dépense.
3. L'orchestrateur prend pour racine du dépôt (lectures interdites aux agents) celle du **clone**, pas le dépôt de travail
   (réserve déjà notée par la contre-lecture du v2 ; sans portée : agents sans outil).

## Questions ouvertes

- **Pour la mère** : (1) lecture d'N-053 sur la règle de passage (sélection par le classement des juges de l'atelier, aucun
  score servi) — confirmer, ou passer au tirage uniforme parmi les éligibles ; (2) où faire tourner la course (bac à sable) ;
  (3) contre-lecteur d'un autre modèle (N-052) pour le lanceur, l'essai de la forme du bras compris ; (4) le programme des
  mesures entre générations (§ 6 de la conception), à écrire avant la lecture de la génération 2 ; (5) la sonde réelle de
  la garde refus-question (≈ 0,003 USD, hors de ce lanceur) sur la nouvelle question, si la mère la juge utile.
- **Pour Lazar** : (1) écrire la règle et l'épingle ; (2) option (b) de la conception (troisième juge Fable 5.1) ; (3) le
  code ne permet ni Fable 5.2 ni un juge d'une lignée absente des proposeurs (Argon est obligatoirement proposeur et juge).
