# Commande de création de production de l'essai 3 du palier 0b — v6

Pièce de travail (classe B), écrite par la session du compte organisme le 2026-11-22T07:38Z. **Remplace la v5** (`commande-creation-production-essai-3-v5.md`, `49420292…`, gardée sans modification), après la seconde vérification par le même contre-lecteur Opus (« Conforme avec réserves », `contre-lecture-commande-creation-v3-v1/verification-v5-v1.md`). Lignée : v1 `4129b36a…` ; v2 `a4bb9308…` (jeton 2 réemployé, `CONTROLE_IA_GITHUB_TOKEN_2`, GO-2026-11-22-04, ligne sur `main`) ; v3 `e5d12b6a…` ; v4 `aef39cc4…` ; v5 `49420292…`. Toute autre forme exige une nouvelle version de cette note et le mot de la mère.

## Préalables (aucun envoi sans les quatre)
1. Le nom du jeton : `CONTROLE_IA_GITHUB_TOKEN_2` (GO-2026-11-22-04). Seul son nom est connu de la session ; il n'est jamais affiché. Sa validité se vérifie sur la machine même, au clonage du pas b (code 41 sinon), comme le dit la réserve du GO.
2. Le contrôle d'absence de la branche `recuperation/palier-0b-programme-1-essai-3-v1` sur le vrai dépôt. Le fabricant le refait lui-même, par `git ls-remote` en lecture, et refuse en 8 si la branche existe.
3. Les empreintes des pièces, contrôlées par `sha256sum` juste avant le fabricant (le texte réduit excepté) :
   - fabricant v8 `a91f3403…` ;
   - script v6 `f61aea46…` ;
   - amorce v6 `524cfc4a…` ;
   - réducteur v6 `b1a4d216…` ;
   - texte réduit `061f7993…` : il n'existe pas avant la commande 1 ; il est produit et contrôlé par le fabricant lui-même, puis recontrôlé par l'outil, qui refusent s'il diffère ;
   - outil v2 `73046b31…` ;
   - lanceur v4 et gardien v4, tels que le fabricant les épingle.
4. La ligne de GO (GO-2026-11-22-04) et le mot de Lazar pour la dépense, au devis v5, **voie de la fiche et non voie (a) du devis** (voir « Écart avec le devis v5 ») ; et, puisque le classifieur a refusé la commande 1 le 22 à 04:55Z, le mot de Lazar écrit dans la session qui exécute, qui autorise ces trois commandes.

Dossier des pièces : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1`.

Avant la commande 1 : `mkdir -m 700 /home/user/essai-3-sortie` (refusé s'il existe), puis `stat -c %a /home/user/essai-3-sortie`, qui doit rendre `700` ; sinon, arrêt. `/home/user/essai-3-sortie` est hors de tout dépôt git. `SORTIE` = `/home/user/essai-3-sortie/donnees-demarrage` (fichier neuf, mode 600) ; relevés : `/home/user/essai-3-sortie/releve-a-blanc` et `/home/user/essai-3-sortie/releve-creation` (neufs).

**Fenêtre de 2 h** : les commandes 2 et 3 suivent la commande 1 en moins de 2 h. Le script de la machine refuse au démarrage une heure H0_PREVU plus vieille que 7 200 s (`AGE_MAX`, code 21, sans poussée) : un retard ferait payer un serveur inutile. Si 1 h 30 est passée depuis la commande 1 sans que la commande 3 soit partie, on ne l'envoie pas : `SORTIE` est retirée (voir « Retrait de la sortie ») et rien ne repart sans le mot de la mère. **Reprise** : avant toute reprise, je liste les serveurs Hetzner (identifiants et noms seulement) ; si un serveur de l'essai 3 existe (un échec 21, un délai dépassé ou une coupure réseau peuvent cacher une création réussie), aucune reprise : je le relève et j'attends le mot de la mère (le détruire par son identifiant, ou le garder). Sans serveur, la reprise se fait dans un dossier neuf, `/home/user/essai-3-sortie-r1` (puis `-r2`, etc.), créé et contrôlé comme ci-dessus, et les trois commandes s'y écrivent en remplaçant seulement `/home/user/essai-3-sortie` par ce dossier. Le dossier précédent est gardé, sans le fichier porteur du jeton : le fabricant (code 4) et l'outil (code 2) refusent d'écrire sur des fichiers existants, et c'est voulu.

## Commandes, dans cet ordre, depuis la session du compte organisme
Les deux pièces sont lancées depuis leurs dossiers versés : `auteur-fabricant-v8-amorce-epinglee/` et `auteur-controle-sortie-v2/`.

1. Fabrication :

   `bash /home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/auteur-fabricant-v8-amorce-epinglee/fabriquer-donnees-demarrage-v8.sh CONTROLE_IA_GITHUB_TOKEN_2 /home/user/essai-3-sortie/donnees-demarrage f61aea46033d63dec6fde0cd66455f5474e000d140d9d98c5f23ab61976aeeb2`

   Aucune variable `FABRICANT_*` n'est posée. L'heure H0_PREVU est prise par le fabricant lui-même.
2. Contrôle à blanc :

   `/home/user/controle-ia-travail/.venv/bin/python -I /home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/auteur-controle-sortie-v2/controler-et-creer-essai-3-v2.py /home/user/essai-3-sortie/donnees-demarrage /home/user/essai-3-sortie/releve-a-blanc --a-blanc`

   Le code attendu est 0. L'empreinte et la taille du corps sont consignées.
3. Création :

   `/home/user/controle-ia-travail/.venv/bin/python -I /home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/auteur-controle-sortie-v2/controler-et-creer-essai-3-v2.py /home/user/essai-3-sortie/donnees-demarrage /home/user/essai-3-sortie/releve-creation --envoyer`

   - Le jeton de Hetzner est lu par son seul nom, `HCLOUD_TOKEN`.
   - **Ni `CONTROLE_BANC`, ni `--adresse`, ni `--nom-jeton`, ni `--pause-apres-lecture`.**
   - L'outil relit les données en une seule fois et les recontrôle avant l'envoi.

## Après l'envoi
- Je relève l'identifiant du serveur et l'heure de la réponse, qui fait H0. Le relevé est expurgé, sans mot de passe root ni `user_data`.
- **Retrait de la sortie** : `/home/user/essai-3-sortie/donnees-demarrage` porte le jeton en clair. Je la retire par `shred -u` dans **tous** les cas où la commande 3 n'est plus à venir : sitôt la réponse de la commande 3 relevée (création réussie ou échouée) ; sur tout code non nul de la commande 2 (contrôle à blanc) ; sur tout arrêt après la commande 1 ; au dépassement de la fenêtre. Si la commande 1 échoue après avoir écrit `SORTIE`, même règle. Je garde les fichiers annexes sans jeton (ils portent `@JETON@`) et les relevés ; je consigne l'empreinte du fichier retiré, relevée avant le retrait. `shred` n'efface pas avec garantie sur un système de fichiers journalisé : le dossier en 700, la courte durée et la révocation en fin d'essai couvrent ce reste.
- Je consigne la dépense dans les registres.
- Si aucune poussée n'arrive sur `recuperation/palier-0b-programme-1-essai-3-v1` dans les 2 h, le serveur est détruit par son identifiant.
- Je fais le relevé à 6 h, depuis la branche de récupération.
- Je détruis le serveur à H0 + 98 h, par son identifiant, et je le consigne dans `registres/arrets.md`.
- Je rappelle à la mère de faire révoquer ou faire expirer le jeton 2 par Lazar à la fin de l'essai : il reste dans les données de démarrage du serveur (service de métadonnées, copie de cloud-init) toute sa vie, pas seulement dans `/root/essai-3-secret/jeton`.
- Si l'envoi échoue (refus, code non nul, redirection), rien ne se refait sans le mot de la mère. Une création refusée par Hetzner ne coûte rien.
- Si le classifieur refuse encore une commande malgré le mot de Lazar, je m'arrête et je le dis. **Repli unique** : voir « Repli ».

## Écart avec le devis v5
Le devis v5 (paragraphes 5 et 6) recommande une voie (a) : créer, alimenter, relever et détruire depuis le poste de Lazar, sans clonage depuis le serveur. Cette commande suit l'autre voie, celle de la fiche serveur et de la ligne GO-2026-11-22-04 : création depuis la session, clonage et poussée par le serveur avec le jeton 2. La dépense est celle du devis v5 (même type de serveur, même durée bornée). **L'écart est nommé ici pour que Lazar l'accorde en connaissance de cause.**

## Repli
**Un seul repli** : Lazar exécute lui-même, depuis son poste, les trois commandes de cette note (mêmes pièces, mêmes empreintes, même voie de la fiche), avec un dossier de sortie hors dépôt sur son poste. Ce n'est ni la voie (a) ni la voie (b) du devis v5. La voie (a) du devis v5 n'est pas un repli de cette note : elle demanderait une autre commande, une autre version et une autre contre-lecture. **Condition** : le fabricant écrit en dur `/home/user/controle-ia-travail/…` (dossier des pièces, interpréteur) ; ce repli n'est jouable tel quel que si le poste de Lazar a cette arborescence et ce `.venv`. Sinon il faut une version de cette note propre au poste, contre-lue avant usage.

## Réserves connues
- Le contrôle d'absence de la branche (fabricant, ligne 96) interroge le dépôt privé sans jeton : il dépend des accès du relais réseau de la session ; sinon refus 8, sans dépense.
- Le mode 700 du dossier n'est contrôlé que par le `stat` ci-dessus, aucune des deux pièces ne le vérifie.

## Différence avec la v5
En-tête (lignée) ; liste des serveurs Hetzner avant toute reprise ; condition d'arborescence du repli. Les trois commandes, leurs arguments et options sont inchangés.

## Différence de la v5 avec la v4 (rappel)
En-tête (lignée) ; reprise après 1 h 30 dans un dossier neuf numéroté ; retrait de la sortie étendu à tous les cas où la commande 3 n'est plus à venir (dont un refus du contrôle à blanc) et réserve sur `shred` ; un seul repli, nommé dans sa section, la phrase « voie (a) … repli » retirée de « Écart avec le devis v5 ». Les trois commandes, leurs arguments et options sont inchangés.

## Différence de la v4 avec la v3 (rappel)
En-tête (classe B, lignée) ; titre « Commandes, dans cet ordre… » rétabli ; préalable 3 (sort du texte réduit) ; préalable 4 (voie) ; contrôle `stat` du mode 700 ; fenêtre de 2 h écrite ; retrait de `SORTIE` après l'envoi ; rappel du jeton dans les métadonnées du serveur ; sections « Écart avec le devis v5 » et « Réserves connues ». Les trois commandes, leurs arguments et options sont inchangés.

## Différence de la v3 avec la v2 (rappel)
En-tête ; préalable 3 (texte réduit `061f7993…` ajouté) ; dossier et chemins absolus des pièces ; `SORTIE` et relevés nommés sous `/home/user/essai-3-sortie`, hors dépôt. Les commandes, options et pièces sont les mêmes.

## Différence avec la v1 (rappel)
Jeton 3 → jeton 2 nommé (préalable 1, commande 1) ; préalable 4 (mot de Lazar dans la session, après le refus du classifieur) ; garde des 2 h, refus du classifieur et rappel de révocation dans « après l'envoi » ; phrase « fixée sur la décision de 02:30Z » retirée de l'en-tête.
