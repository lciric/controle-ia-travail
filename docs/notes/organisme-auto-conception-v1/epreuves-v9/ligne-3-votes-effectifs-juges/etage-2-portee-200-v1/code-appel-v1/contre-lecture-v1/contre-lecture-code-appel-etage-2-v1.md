# Contre-lecture du code d'appel de l'étage 2 à 200 témoins (ligne 3, organisme v9) — v1

Pièce d'instrument (classe B), écrite le 2026-11-20 par le contre-lecteur, modèle S, sur le mandat
`mandat-contre-lecteur-code-appel-etage-2-v1.md` (`5bf7858c0e75aaa732d6604e0728b9a497857e55b4f12b6cdb3519aef945f1e8`, recalculée égale à son compagnon).
Je n'ai écrit ni le texte de la ligne 3, ni ses additifs, ni le devis, ni l'inventaire, ni le calcul du plafond, ni ce code.
Aucun appel à un fournisseur, aucune dépense, aucune clé lue, aucun relais lancé, mode réel jamais lancé.

## Verdict

**À corriger** : trois corrections locales (C1 à C3), aucune ne touche au compteur, au plafond, ni à la reproduction du calcul v2.
Le reste est conforme à la lettre du texte et du mandat. Les points pour la mère sont en § 5 à § 7.

## 1. La table

Les trois pièces du développeur sont égales à la table et à leur compagnon (`sha256sum -c` sur la table : six lignes OK ;
compagnons des quatre fichiers : OK) : programme `586bc7e6…`, essais `d68e2c14…`, rapport `c5df780d…`.
Constantes du code égales aux fichiers, recalculées par moi : les cinq modules du clone (`__init__` `f7341b96…`, `outils` `966d9553…`,
`caviardage` `78abfd47…`, `fiches_v53` `7cfcf832…`, `juges_croises_v53` `c4c6ab12…`), le lanceur v9 `1b47c1cf…`, le précédent `5be161fa…`,
la configuration `3f662ee8…`, les témoins v2 `84a1e0ea…`, la consigne `b03f33b8…`. Remarque : la table ne liste pas le mandat de
contre-lecture ni son compagnon, ajoutés au dossier après elle ; sans effet.

## 2. Les essais rejoués

Sur une copie de C dans mon dossier, commande du mandat, en tâche de fond : **85 passed in 95.16s**. Aucun échec, aucun saut.

## 3. Refait indépendamment

Programme `refaire_plafond_cl_v1.py` (fractions exactes, aucune importation du code ni du calcul v2 ; tarifs et facteurs recopiés du rapport et de la
sortie scellée) ; sortie `sortie-refaire-plafond-cl-v1.txt`. Il rend, et ses assertions tiennent :
- pire cas : 996 envois, 197 témoins complets (100 « lecture », 97 « étalonnage »), 87,7701 USD, dernier envoi parti = rendu 2 du juge Opus au
  témoin 198 du bloc B, premier interdit = rendu 2 du juge Argon au même témoin ;
- « tout refusé » à 200 : 147 envois, 88,20 USD, aucun rendu, dernier envoi parti au rang 35 du bloc A (juge Argon, essai 1), premier interdit essai 2 ;
- selon les envois refusés, accord avec la sortie du calcul v2 (`fe58be3a…`) : estimation 100 refus = 935 envois, 143 témoins complets au bloc B ;
  haut 80 = 963, 159 ; pire 10 = 934, 173 ; pire 80 = 490, 2 ; pire 100 = 385, 0 (bloc A coupé à 140) ; au seuil de trois fois le tarif : 630 envois,
  87,9542 USD, 75 témoins complets. Les lignes 0, 1, 10 (trois cas) et 40 (pire) sont aussi rendues, cohérentes avec les essais.
Ces nombres sont ceux que les essais du développeur rendent (essais passés) : le compteur du code et mon programme concordent.

## 4. Lecture du code contre la lettre

Tenu, lu ligne à ligne :
- **Compteur** : engagement de 0,60 écrit et `fsync` avant chaque envoi (`Compteur.engager`, `Journal.ajouter`) ; comparaison `cumul + 0,60 <= plafond`
  (strict sur « dépasse », frontière 147 × 0,60 essayée) ; centimes entiers et `Fraction`, aucun flottant dans un seuil (`centimes`, `exacte`,
  `cout_lisible` lit un flottant par son écriture décimale) ; `PLAFOND_C = 8836` seule constante ; règlement au coût relevé ; refusé, coupé, en erreur,
  exception, sans coût lisible : 0,60 ; rejeu unique ; verdict lisible sans coût lisible gardé, non rejoué ; coût relevé au-dessus de 0,60 : compté tel
  quel, arrêt ; engagement sans règlement compté 0,60 à la relance (lecture du journal, ligne coupée, hors forme, sans ouverture : refus) ; jamais de coût nul.
- **Identifiant opaque neuf** par rendu (« F » + cinq chiffres hexadécimaux, tirés par `SeedSequence(2026111935, spawn_key=(4,))`, jamais repris, journal compris) ;
  fiche servie = contenu du témoin + identifiant opaque seulement, vérifiée ; garde « vérité non servie » (mot « classe », nom d'item, identifiants interne
  du témoin et du rendu dans tout le texte servi). Dossier d'appel nommé par l'identifiant opaque. `entree_une_fiche` (fiches_v53) et `lire_verdict`
  lues au clone : signatures conformes.
- **Blocs et ordre** : P (2 témoins v2 × 2 juges), A (par témoin : Opus puis Argon), B (moitié « lecture » d'abord ; par témoin Opus r2, Argon r2, r3),
  ordre tiré par racine 2026111935, clés 1/2/3 ; l'ordre est reproductible (vérifié par mon second programme) ; plan de 1 004 envois.
- **Gardes** : « ligne de GO » rejouée par moi sur le registre réel de `origin/main` (`go-main.md`, `766a63e7…`) : GO-2026-11-20-26 acceptée au 20 et au 30
  novembre, refusée au 1er décembre ; GO-2026-11-20-36 refusée (type différent) ; sortie `sortie-verifier-go-reel-cl-v1.txt`. « Modèle servi »,
  « réponses identiques », « verdicts de la v9 » (composant `archives-reponses-modeles` ou commençant par « coffre », racines de la sortie et du run
  v9, forme écrite puis chemin réel), « verdict illisible », plomberie : essayés sain et artefact.
- **Dépôt** : verdicts, état des juges, rapport, manifeste (règle R9 : configuration et empreinte, versions, graines, commits, consigne et configuration
  servies), tous scellés avec compagnon, création exclusive ; réponses brutes et fiches servies gardées ; aucun champ de vérité aux dépôts de verdicts.
- **Mode réel** : seul `--reel` part ; refus avant toute construction de service dans l'ordre : noms de clé dans l'environnement (par le nom seulement),
  chemins du coffre, `--go-id` (et `GO_ID` s'il est posé, égal) valide au registre de `origin/main`, banque scellée à l'empreinte passée, déclaration scellée
  (claude et argon seulement), puis seulement le constructeur. Aucune clé lue ni affichée. Écritures : sous `--sortie` seulement. Sans argument, le programme
  rend l'usage et le code 2 (essayé sous `python3 -I -B`).
- **Chemin réel, lu sans exécution** : `construire_service_reel` recoupe les signatures du précédent (`exiger_bac_a_sable`, `preparer_appels`,
  `verifier_borne_argon`, `charger_orchestrateur`) et du lanceur (`verifier_declaration`, `verifier_procedure_relais` avec `plafond_ligne = 88,36` — le relais Claude doit
  porter ce plafond, `porte_a_blanc`, `envelopper_commandes`). Borne du relais d'Argon : 2 × (2 + 200 + 400) jugements, rejeu compris, = 1 204 ; `appels_relais_gemini_requis`
  = 2 × 1 204 + 2 = 2 410 : exact. Le chemin réel reste non exercé : sa contre-lecture ne peut être que celle-ci.

### Corrections

**C1 — une relance sur une autre banque que celle du journal est acceptée.** Essai de ma main (`demo_relance_autre_banque_cl_v1.py`, sortie
`sortie-demo-relance-autre-banque-cl-v1.txt`) : panne à l'envoi 101 avec la banque A, relance avec une banque B scellée, de contenus différents : « RELANCE
SUR UNE AUTRE BANQUE ACCEPTEE », 1 005 envois, 45,3783 USD. Le journal écrit l'empreinte de la banque à la ligne d'ouverture, mais `executer` ne la relit pas. Les rendus
déjà payés sur la banque A se mêleraient à ceux de la banque B sous le même compteur : contraire à « relance qui relit le journal, jamais de remise à zéro »
(texte l. 382). Lieu : `executer`, bloc `if relance:` (avant l'écriture du manifeste), et la ligne d'ouverture. Texte exact à ajouter :

```
        if relance:
            ... (les deux refus existants)
            ouverture = journal.lignes[0]
            if ouverture.get("banque_sha256") != banque_sha or ouverture.get("plomberie") != list(plomberie_ids):
                raise Refus("relance refusée : banque ou témoins de plomberie différents de ceux de l'ouverture du journal : aucune suite sous cette ligne")
            ids_du_plan = {p["id"] for p in plan}
            if any(l["rendu"] not in ids_du_plan for l in journal.lignes if l["type"] == "engagement"):
                raise Refus("relance refusée : un rendu du journal n'est pas au plan : aucune suite sous cette ligne")
```
et, à la ligne d'ouverture, ajouter la clé `"plomberie": list(plomberie_ids)` à côté de `"banque_sha256": banque_sha`. Essai à ajouter : panne puis relance sur une autre banque, refus nommé.

**C2 — relance impossible après une panne entre la création du dossier d'appel et l'engagement.** `jouer` crée `dossier.mkdir(parents=True, exist_ok=False)` avant `compteur.engager`. Une panne dans cet
intervalle laisse un dossier vide sans engagement ; à la relance, l'identifiant opaque tiré en premier est le même (la suite tirée repart de la graine,
seuls les identifiants engagés au journal sont sautés) : `FileExistsError`, à chaque relance, jusqu'à une main humaine. Aucun envoi n'est parti, rien n'est dû. Lieu : `jouer`,
`dossier.mkdir(parents=True, exist_ok=False)` → `dossier.mkdir(parents=True, exist_ok=True)`.

**C3 — la garde de plomberie n'est pas rejouée à la relance (rapport § 7, point 4 ; réponse : il faut la rejouer).** `jouer` saute tout envoi dont le rendu est fini
(`if rendu_fini(s) or prevu["juge"] in roles: continue`), donc aussi le contrôle `motif_plomberie` qui suit. Une panne tombée entre le règlement d'un rendu de plomberie et son
contrôle laisserait partir le bloc A sur une plomberie illisible ou au-delà de trois fois le tarif : la liste d'arrêt ne tiendrait plus. Lieu : `jouer`, début de la boucle sur `plan`. Remplacer

```
        if rendu_fini(s) or prevu["juge"] in roles:
            continue
```
par
```
        if rendu_fini(s) or prevu["juge"] in roles:
            if prevu["bloc"] == "P" and arret_de_plomberie and rendu_fini(s) and prevu["juge"] not in roles:
                motif = motif_plomberie(s, compteur, prevu["juge"])     # contrôle sans envoi, rejoué à la relance
                if motif:
                    return journal.ajouter({"type": "arret", "motif": "plomberie : " + motif, "dernier_envoi_parti": dernier,
                                            "cumul_compte": str(compteur.cumul()), "retour": "à la mère"})
            continue
```
Essai à ajouter : plomberie illisible, panne forcée juste après le règlement (service qui lève au 3e envoi), relance : arrêt de plomberie, aucun envoi du bloc A.

## 5. Le moyen du plafond de session (texte l. 382 (i))

- **Argon : tenu.** Borne de jetons produits : la commande d'Argon v3d (`46c91df4…`, l. 796-857 lues) lit `PLAFOND_SESSION_USD`, fixe `maxOutputTokens` au reste du plafond au prix de
  sortie moins la provision de pensée, refuse sans envoi si le pire cas dépasse (code d'erreur « pire cas »). Le code relit l'environnement que l'adaptateur passerait
  (`AdaptateurCommandeExterne.environnement_commande`, l. 648-664 : `PLAFOND_SESSION_USD = repr(float(0.6))`) et exige 0,60.
- **Opus : tenu, selon la seconde branche de la lettre.** L'option `max_budget_usd = 0,6` (`construire_options`, l. 334, `max_turns = 1`, aucun outil) est le « plafond du service » que la
  lettre nomme. C'est un contrôle du kit sur la dépense de la session, relevé au message de résultat (`_executer`, sous-type `error_max_budget_usd` → `budget_depasse`) : il ne borne pas une réponse
  seule. La réserve du développeur est exacte et la lettre la couvre : « sinon, à 24,40 USD plus le coût du dernier envoi, et un coût relevé au-dessus de 0,60 USD arrête le programme » (ici : 87,76 USD
  plus le coût du dernier envoi). Le code compte ce coût tel quel et arrête (essayé : 0,61). Deuxième ligne, hors compteur : le plafond du relais Claude est exigé égal à 88,36 au départ.
  **À la mère** : lire la borne d'Opus comme « 87,76 USD plus le coût du dernier envoi », non « 88,36 USD ». Recommandation : accepter ; le contrôle « options du kit relues » éprouve la fonction pure, non
  l'application du plafond par le kit, ce qui est le mieux qu'un essai sur processeur permette. Confiance : élevée.

## 6. Ce que le développeur n'a pas pu tenir (rapport § 7), et les quatorze silences (§ 8)

**§ 7.** (1) « Tout refusé » contre l'arrêt de la plomberie : **à la mère ; recommandation : garder le code tel quel** (l'arrêt de la plomberie arrête à 2 envois, 1,20 USD ; les 147 envois du calcul sont
reproduits par la même boucle avec l'arrêt levé, permis en mode essai seulement, refusé en mode réel — essayé). L'additif de code dira que la ligne 367 « 41 envois, puis arrêt » (147 à 200) est une propriété de
la boucle du compteur, jouée arrêt de plomberie levé. (2) Chemin réel non exercé : constaté, relu au § 4 ; départ réel impossible sans la contre-lecture du chemin d'amorçage par la mère. (3) Garde des dossiers
sur deux dossiers témoins sous la même racine : **juste** (même racine interdite, même forme de nom ; la garde quadratique du précédent serait sans objet à 1 004 dossiers). (4) Panne entre règlement et contrôle de plomberie : **à corriger, C3**.

**§ 8**, un par un :
1. Deux témoins v2 de la plomberie : **juste** ; la mère les nomme à l'additif (arguments `--plomberie`).
2. Coût non lisible en plomberie : **juste** (la lecture du coût par appel est impossible ; arrêt prudent).
3. « Envoi refusé par le fournisseur » : **juste**. Lu au kit : `stop_reason = refusal` (événements `assistant.stop_reason`, `result.stop_reason`) n'est pas classé « changement de modèle » : refus compté 0,60 et rejoué une fois.
4. Coût relevé au-dessus de 0,60 sur un envoi en erreur : **juste** (compté à son coût, arrêt ; jamais sous-compté).
5. Bases des 10 % et de la moitié : **juste, à confirmer par la mère** (rendus tentés des blocs A et B ; paires de tous les rendus, paires 1-2 rapportées à part).
6. Racine des identifiants opaques : **à la mère**, recommandation : confirmer 2026111935 clé 4 (l. 303 ne dit que « ordre des appels »).
7. Chemin du coffre : **juste** (liste par composants ; sur-refus possible d'un chemin nommé « coffre… », du côté sûr).
8. Ligne de GO : **à la mère**. Mes essais montrent que GO-2026-11-20-26, telle qu'écrite, passe la garde ; mais la ligne porte « Rien ne court avant un additif écrit par Fable, contre-lu et scellé, la mesure à 200 sur processeur et son verdict scellé » :
   la garde ne lit pas cette condition. Recommandation : ligne de départ neuve au plafond de 88,36 USD, au type « calcul », périmètre « ligne 3, étage 2 », échéance après la date de départ (celle de GO-26 est le 30 novembre) ; la garde la lit sans changement.
9. Clé du juge Opus en argument, pièce de départ réduite : **à la mère** ; recommandation : accepter, la déclaration scellée et la procédure des relais portent le nom ; `verifier_declaration` refuse un nom de clé réservé ou autre que celui passé.
10. Relance en mode réel : **juste, avec une réserve à connaître** : des relais neufs sont relancés avec un plafond de relais de 88,36 USD chacun ; après une relance, le plafond du relais Claude n'est plus une seconde ligne de défense au cumul (le compteur seul garde le cumul, comme le texte le veut). Recommandation : accepter.
11. Borne du relais d'Argon : **juste** (recalculée : 2 410).
12. Verdicts de la moitié « lecture » : **à la mère** ; recommandation : accepter ; ils sont déposés scellés ; « restent non ouverts » se tient par la procédure (aucun agent ne les ouvre avant la lecture unique). Le rapport d'exécution porte, sur les deux moitiés réunies, des parts d'absents et d'identiques qui sont des gardes, non des mesures.
13. Configuration servie v5 : **juste** (épinglée par le lanceur ; empreinte recalculée égale).
14. Interpréteur : **à la mère** ; l'additif nomme l'interpréteur réel et sa version de numpy (≥ 1.25) ; le module demande Python ≥ 3.10 (`str | None`) ; il s'importe et rend l'usage sous `python3` (3.13) en `-I -B`.

**Silences que le développeur n'a pas nommés** (mes ajouts, à la mère) :
15. Retours non prévus au texte : `budget_depasse` (commande externe dont le coût déclaré dépasse la session ; kit) est classé retour obtenu, compté à son coût, non rejoué, verdict absent (texte non lu) et, au-dessus de 0,60, arrêt ; `tours_epuises` est classé erreur (0,60, rejeu). Recommandation : accepter.
16. « Complets » du rapport = tous les rendus partis et revenus, y compris à verdict illisible (le calcul v2 n'a pas de rendu illisible). Recommandation : accepter pour le rapport d'exécution ; le programme de lecture compte les verdicts lisibles.
17. Après un arrêt pour crédit (garde avant envoi), toute relance est refusée sous la même ligne (plus strict que la lettre, qui ne parle que de l'arrêt du compteur). Recommandation : accepter ; une suite demande une ligne et un dépôt neufs.
18. Panne pendant le dépôt (après la ligne « fin » ou « arrêt ») : la relance est refusée et le dépôt des verdicts n'est pas refait ; le journal et les réponses brutes restent. Recommandation : accepter, avec une pièce de dépôt refait depuis le journal si le cas se présente (travail sur processeur).
19. Le registre est lu sur `origin/main` local sans `git fetch` : une révocation non encore récupérée échapperait. Recommandation : procédure de départ de l'additif demande `git fetch` avant ; le manifeste garde le commit et l'empreinte du registre lus.
20. Toute variable d'environnement dont le nom contient `TOKEN`, `SECRET`, `API_KEY`… (par exemple le jeton du fournisseur de serveurs) fait refuser le départ (comme au précédent) : lancer sous un environnement épuré. Recommandation : le dire à la procédure de départ.

## 7. Les écarts du développeur à son mandat (rapport § 10)

1. Recherche par motif sur un dossier de l'orchestrateur (une ligne rendue, lecture seule) : **sans suite**.
2. `pip list` sur l'interpréteur de `.venv` : **sans suite** (lecture seule ; la version de numpy est celle des essais).
3. Outil de travail hors des pièces (`tarifs_exacts.py`) et copies de `origin/main` : **sans suite** ; les tarifs sont re-vérifiés égaux au calcul v2 par un essai du dépôt.
4. Écritures dans le dossier temporaire de pytest : **sans suite** (mes essais en font autant, hors du dépôt).

## 8. Mes écarts

Lectures par motif sur des fichiers nommés un à un (clone, précédent, lanceur, adaptateurs), jamais sur un dossier ; `git show` redirigé de `registres/go.md` sur `origin/main` vers mon dossier ;
copie du dossier C dans mon dossier ; mes deux programmes qui importent le module copié (garde de GO sur le registre réel ; démonstration de C1 par les aides des essais) tournent sous l'interpréteur de `.venv`
(`-I -B`), car les essais en ont besoin ; le programme de recalcul tourne sous `python3 -I -B`. Les deux dossiers `demo-relance/` (première passe, sortie à l'écran) et `demo-relance-2/` (seconde passe, sortie gardée) sont dans mon dossier.
Écart déclaré, relevé par la coordination : mes trois fichiers de sortie (`sortie-refaire-plafond-cl-v1.txt`, `sortie-verifier-go-reel-cl-v1.txt`,
`sortie-demo-relance-autre-banque-cl-v1.txt`) ont d'abord été écrits à la racine du dépôt de travail, parce que la redirection `>` d'une commande `env -C DOSSIER …` s'exécute
dans le dossier courant du shell, non dans `DOSSIER`. Corrigé : copiés dans mon dossier (`cp --update=none`), vérifiés par `cmp` (identiques), puis retirés de la racine par `rm` sur chaque chemin complet.
Rien d'autre n'a été écrit dans le dépôt ; ces trois fichiers n'ont jamais été ajoutés à l'index ni committés. Désormais toute redirection vise un chemin complet de mon dossier.
Aucun refus de permission, de classifieur ni de garde.

Contre-lecteur, modèle S.
