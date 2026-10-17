# Coordination de deux voies sur le dépôt de travail — protocole v1

> **Non en vigueur — archivé.** Le 17 octobre à 08:24 UTC, Lazar a choisi une seule session d'exécution : la session cloud (session 15) fait le calcul et la rédaction. La session de conversation n'intervient plus que sur un nœud, à sa demande. Ce protocole reste versé pour le jour où deux sessions ou un projet Claude Code travailleraient de nouveau en parallèle.
>
> **Statut d'origine.** Écrit le 17 octobre 2026 par la session 16, c'est-à-dire la session de conversation claude.ai, voie rédaction. Elle s'était d'abord nommée « session 15 », mais la session Claude Code cloud a consigné ce numéro la première sur `main` (R-184 et R-185, à 08:01 et 08:04 UTC). Le protocole répond à deux demandes de Lazar :
> - à 07:55 UTC, un canal avec la session Claude Code cloud qui travaille aussi sur le dépôt, et une répartition du travail entre les deux ;
> - à 08:08 UTC, le choix de l'option (b) : deux voies et ce protocole, plus un projet Claude Code pour les voies cloud.
>
> Ce protocole ne change ni le programme, ni le brief, ni `CLAUDE.md`, ni aucune des règles R1 à R14 : il dit seulement qui écrit quoi, et quand. Lazar le change quand il veut.
>
> Il vaut quelle que soit la forme des voies : fil d'un projet Claude Code, lancé par sa conversation coordinatrice (consignes dans `coordination-deux-voies-v1/instructions-projet-v1.txt`), ou session autonome. Le passage au projet se fait en deux phases (section 7).

## 1. Le problème

Deux voies travaillent en parallèle sur le même dépôt.

Quatre risques :
1. **Poussées croisées sur `main`.** Le scellement exige « HEAD = origin/main », puis pousse S (`docs/procedures/notations-T0.5-v2/sceller_notations_v1.sh`, l. 57 et 159). Une poussée de l'autre voie entre les deux fait échouer celle de S. Et un S refait change d'empreinte, alors que les lanceurs le citent.
2. **Registres en double.** Deux voies qui numérotent des lignes R-… ou réécrivent `registres/etat.md` se contredisent. Un numéro cité par un lanceur (ligne de relancement, plan des notations, étape 7) ne doit jamais changer.
3. **Instances.** La routine de reprise (R14, étape 4) arrête toute instance « sans tâche en cours ». Une voie qui ignore le run de l'autre l'arrêterait. Deux voies qui lancent dépenseraient deux fois.
4. **Travail en double ou perdu, et relais déformés.**
   - Deux voies peuvent reprendre la même « prochaine action ».
   - Du travail non poussé se perd à la limite d'usage ou quand le conteneur est repris (session 13).
   - Dans un projet, la conversation coordinatrice ne voit que les comptes rendus des fils, et peut les déformer en les résumant.

**Principe.** Ce qui doit être exact ne passe jamais par un résumé : bail, lignes de registre, empreintes, alertes. Cela passe par des fichiers scellés du dépôt. Le coordinateur, ou Lazar, ne transmet que des pointeurs vers ces fichiers.

## 2. Deux voies, un propriétaire par ressource

| ressource | voie qui écrit | ce que fait l'autre voie |
|---|---|---|
| Compte Vast.ai : inventaire, offres, crédit, création, arrêt et destruction d'instance (R10) | calcul | lit l'inventaire publié par la voie calcul ; n'agit jamais (sauf § 5) |
| Jetons de l'instance (Hugging Face, GitHub) | calcul | ne s'en sert jamais, même s'ils sont dans son environnement |
| Chaînes de calcul et leurs runs : notations N-021 maintenant ; plus tard, runs de T0.6, T0.7, T0.8 et pilote T0.9, sur GO. Avec eux : `traces/`, `diag/`, `runs/`, branches `calcul/*` et `donnees/*`, modules de lecture des runs, verdicts R13 des runs (sous-agent neuf) | calcul | lit |
| Lignes de `registres/depenses.md` et `registres/arrets.md` | calcul, quand elle tient le bail ; sinon lignes proposées (§ 3) | lit |
| Préenregistrements et leurs brouillons (T0.6, T0.7, T0.8, G1, papier C), avec le code qu'ils exigent (par exemple T7-P9 et T7-P10 de T0.7), leurs contre-lectures R2 et leurs scellements | rédaction | lit ; un préenregistrement scellé est l'entrée de la voie calcul |
| Programme fusionné « pain axis » ; canal « pain axis » (branches `canal/*`, demande de fusion n° 11) ; état de l'art (critère 8 de G0) ; documents pour les évaluateurs ; réserve R-173 | rédaction | lit |
| `main` et les registres vivants (`etat.md`, `decisions.md`, `go.md`, `veille.md`) | la voie qui tient le bail (§ 3) | propose ses lignes (§ 3) |
| Passations | chaque session ou fil la sienne (nom à l'heure UTC, donc sans collision) | — |
| Branche `coord/redaction` | rédaction seule | lit |
| Branche `coord/calcul` | calcul seule | lit |

Deux règles complètent la table :
- **Modules.** Un module de `src/` appartient à une seule voie : celle qui le crée. Pour modifier un module de l'autre voie, on le demande par message.
- **Le chat.** La session de conversation claude.ai n'écrit plus ni sur `main` ni dans les registres. Elle sert à la réflexion de Lazar (brainstorm, stratégie, recherche) et aux documents destinés à d'autres. Ce qu'elle produit pour le travail va sur une branche `chat/<objet>`, et Lazar le signale au coordinateur par un pointeur.

## 3. Le bail de `main`

**Règle.** À tout instant, une seule voie tient le bail. Elle seule pousse sur `main`, écrit les registres vivants et attribue les numéros R-…, à la suite et sans trou. Dans un projet, chaque tâche confiée à un fil dit « bail : oui » ou « bail : non ». Un seul fil à la fois a « oui ».

**L'autre voie** committe sur sa branche de travail (`redaction/<objet>` ou `calcul/<objet>`) et la pousse, pour que rien ne se perde. Elle ne pousse jamais sur `main`.
- Les lignes de registre dont elle a besoin vont dans un message de type LIGNES (§ 4), texte prêt, sous un identifiant provisoire (RED-01, CAL-01…).
- Le porteur les consigne mot pour mot sous les numéros suivants et répond avec la correspondance.

**Fenêtre de calcul.** Certaines lignes doivent exister avant un geste :
- les consignes « avant la création » de `etat.md` et `depenses.md` ;
- la ligne de relancement que le lanceur cite ;
- plus largement, les étapes 3 à 9 du plan des notations.

C'est la voie qui agit qui les écrit. La voie calcul tient donc le bail pendant toute la fenêtre d'un run : de l'étape « dépense cumulée » jusqu'au verdict R13 scellé et poussé.

**Passage du bail.**
1. Le porteur pousse tout ce qu'il a pour `main` et supprime son fichier de bail.
2. Il verse un message BAIL « rendu à <voie> » qui donne la tête de `main` (empreinte du commit).
3. Le receveur vérifie que `origin/main` est bien cette tête, crée son fichier de bail et verse un message BAIL « pris ».

Entre les deux, personne ne pousse sur `main`.

**État initial.** Le 17 octobre, la session cloud (session 15, voie calcul) tient le bail de fait : elle a écrit sur `main` à 08:04 UTC et elle est dans la fenêtre de N-021. Elle le garde jusqu'au verdict de N-021. La voie rédaction ne pousse que sur ses branches.

**Bail laissé par un porteur disparu** (fil ou session fini, limite d'usage). Aucune prise automatique : Lazar attribue le bail d'une phrase, et celui qui le reçoit le consigne.

**Avant toute poussée sur `main`.** `git fetch origin`, puis relire la tête. Un refus « non linéaire » veut dire qu'une autre écriture a eu lieu : on s'arrête et on verse un message ALERTE.

## 4. Le canal

- **Support.** Le dépôt. Chaque voie n'ajoute que des fichiers sous `coordination/<voie>/` de sa branche `coord/<voie>`. Ces fichiers ne se réécrivent jamais (R12) et ont chacun leur sceau `.sha256`. Dans un projet, la conversation coordinatrice route les tâches et les comptes rendus ; tout ce qui doit être exact passe par ces fichiers, et le compte rendu en donne le chemin et l'empreinte.
- **Nom.** `coordination/<voie>/NNN-AAAAMMJJ-HHMM-<objet>.md`, heure UTC, NNN à partir de 001 pour chaque voie.
- **En-tête**, en lignes fixes : De ; À ; N° ; En réponse à ; Heure (UTC) ; Type (ÉTAT, DEMANDE, RÉPONSE, BAIL, LIGNES, ALERTE, FIN) ; Tête de `main` lue ; Bail (qui le tient, selon l'auteur).
- **Corps.** Le verdict d'abord, puis les demandes, numérotées, chacune avec la réponse attendue. Une demande n'a pas de défaut : sans réponse, elle reste ouverte. Le silence ne vaut jamais accord.
- **Quand lire le canal** (`git fetch origin coord/<autre voie>`, puis vérifier les sceaux) :
  - au début de chaque session ou fil, après l'étape 2 de la routine ;
  - avant toute poussée sur `main` ;
  - avant tout geste sur une instance (voie calcul) ;
  - avant tout scellement ;
  - à la fin de chaque tâche ;
  - sinon, au moins toutes les deux heures de travail actif.
- **Sonnette.** Dans un projet, le coordinateur prévient le fil concerné. Entre un fil et une session autonome, ou entre deux sessions autonomes, si l'autre figure parmi les sessions joignables, on lui envoie un message court (« message n° NNN versé sur coord/<voie> ») ; sinon, Lazar dit « lis le canal ». Le contenu ne passe jamais par la sonnette.
- **Archives.** Le porteur du bail fusionne les deux branches de canal dans `main` à chaque passation. Les fichiers sont disjoints : aucun conflit.
- **Discipline.**
  - Aucun secret : les noms de variables seulement.
  - Tout ce qui touche la matière « pain axis » suit les règles de son canal : aucun texte d'attaque, aucune chaîne déclencheuse, aucune dose, le vocabulaire « direction » seulement.
  - Un message d'une voie à l'autre coordonne, il ne décide pas : les nœuds restent à Lazar.
  - Aucune voie ne demande à l'autre un geste que ses propres permissions bloqueraient.

## 5. Instances et dépense

- **Voie calcul.** Elle seule agit sur le compte Vast.ai. Elle annonce dans un message chaque instance du programme qu'elle crée (identifiant, tâche, GO, heure de création, plafond de surveillance), au plus tard dans l'heure qui suit la création.
- **Voie rédaction.** Elle ne crée, n'arrête et ne détruit aucune instance, même si les clés sont dans son environnement (dans un projet, tous les fils partagent l'environnement du projet). Pour elle, l'étape 4 de la routine (R14) consiste à lire le dernier inventaire de la voie calcul. Une anomalie lui fait verser un message ALERTE et écrire à Lazar : instance inconnue, ou instance du programme au-delà de son plafond plus 30 minutes sans nouvelles de la voie calcul.
- **R-181 inchangée** : les instances `rr-` sont un autre projet et ne se touchent jamais.
- **Dépense.** Seule la voie calcul dépense, dans les GO accordés. Le registre de dépense s'écrit selon le plan, par la voie qui tient le bail.

## 6. Garde locale `pre-push` v2

Garde : `docs/procedures/coordination-deux-voies-v1/pre-push-v2.sh`. Elle refuse :
- toute poussée vers `lciric/controle-ia` (R-116, comme la v1) ;
- toute poussée si la voie n'est pas écrite dans `<dossier git>/voie` ;
- toute poussée sur `main` sans le fichier `<dossier git>/bail-main` ;
- toute poussée vers la branche de canal de l'autre voie ;
- toute suppression et toute poussée non linéaire (forcée) sur `main` et `coord/*`.

Elle est éprouvée par `essais-pre-push-v2.sh` (dépôt nu jetable, poussées réelles) : 4 cas sains et 10 artefacts, chacun refusé pour sa raison (R5 ; journal `essais-pre-push-v2.log`).

Installation, au début de chaque session ou fil, dans son clone :
```
cp docs/procedures/coordination-deux-voies-v1/pre-push-v2.sh .git/hooks/pre-push && chmod +x .git/hooks/pre-push
echo calcul > "$(git rev-parse --git-dir)/voie"        # ou « redaction »
touch "$(git rev-parse --git-dir)/bail-main"           # seulement en prenant le bail ; rm en le rendant
bash docs/procedures/coordination-deux-voies-v1/essais-pre-push-v2.sh docs/procedures/coordination-deux-voies-v1/pre-push-v2.sh <dossier neuf hors du dépôt>
```
Attendu au dernier appel : « verdict : 14 OK, 0 KO ».

## 7. Démarrage, en deux phases

**Phase 1, maintenant.** La voie calcul reste la session cloud autonome (session 15) : son conteneur est prêt et ses contrôles avant dépense sont passés. Elle mène N-021 jusqu'au verdict, avec le bail. La voie rédaction passe dans un projet Claude Code : un fil rédaction qui repart de la branche `redaction/session-16-chat`. Entre les deux voies, le canal `coord/*` ; Lazar sert de sonnette.
1. **La session 16 (chat)** verse sur sa branche `redaction/session-16-chat` :
   - ce protocole, la garde et son banc ;
   - les consignes du projet et les messages à coller ;
   - le plan de traitement de la v3 ;
   - sa passation `2026-10-17-0825.md`.

   Elle ouvre `coord/redaction` avec son message n° 001 : état, lignes à consigner, demandes. Ensuite, elle n'écrit plus sur le dépôt.
2. **Lazar colle `coordination-deux-voies-v1/message-session-cloud-v1.txt` dans la session cloud.** Elle y apprend à :
   - lire ce protocole et abandonner la v3, qui appartient à la voie rédaction ;
   - garder le bail ;
   - installer la garde à un moment calme ;
   - fusionner la branche de la session 16 dans `main` à un moment calme, et consigner ses lignes ;
   - verser son premier message sur `coord/calcul` (§ 8).
3. **Lazar crée le projet** (projet neuf, dépôt `lciric/controle-ia-travail`), colle les consignes et choisit l'environnement. Il envoie `coordination-deux-voies-v1/premier-message-coordinateur-v1.txt` : un seul fil, rédaction, sans le bail.

**Phase 2, après le verdict de N-021.** La session cloud écrit sa passation et rend le bail. Lazar fait entrer la voie calcul dans le projet : « Move to project » depuis la session cloud, ou fil calcul neuf qui repart de sa passation. Le bail va au fil qui en a besoin.

**Repli, si les projets ne sont pas ouverts sur le compte.** La voie rédaction reste une session (celle-ci ou une session neuve), avec la même branche et le même canal.

## 8. Premier message de la voie calcul sur `coord/calcul`

- **Identité** : session 15, heure de début.
- **Ce qui a été fait sur le dépôt depuis son début** : R-184, R-185, autres commits et branches, travail non poussé. Si elle a commencé la v3 du programme fusionné, elle verse son brouillon sur une branche `calcul/v3-abandonnee` sous un nom neuf, puis l'abandonne.
- **Secrets présents** : les noms seulement, jamais les valeurs.
- **Inventaire Vast.ai** en forme filtrée : instances, état, étiquettes, prix ; crédit.
- **Garde** installée, avec la sortie de son banc.
- **Ce qu'elle prévoit pour N-021**, étape par étape, et l'état de l'accord de Lazar.
- **Correspondance** des lignes RED-01 et RED-02 de la voie rédaction avec leurs numéros R-…, une fois consignées.

## 9. Ce qui ne change pas

- **Règles.** R1 à R14 et `CLAUDE.md` restent tels quels.
- **Routine et passation.** Chaque session ou fil fait sa routine (R14) et sa passation. Une passation écrite sans le bail va sur la branche de travail de sa voie et s'annonce par un message FIN ; le porteur la fusionne.
- **Usage.** Les voies partagent la limite d'usage du compte : une vague de plus de trois sous-agents s'annonce.
