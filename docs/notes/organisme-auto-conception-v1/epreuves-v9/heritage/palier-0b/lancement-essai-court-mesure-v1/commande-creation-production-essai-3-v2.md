# Commande de création de production de l'essai 3 du palier 0b — v2

Pièce de travail (classe C), écrite par la session du compte organisme (relancée sur le nouveau compte) le 2026-11-22T07:31Z. **Remplace la v1** (`commande-creation-production-essai-3-v1.md`, `4129b36a…`, gardée sans modification) sur **un seul point** : le jeton n'est plus un jeton 3 à recevoir, c'est le jeton 2 réemployé, `CONTROLE_IA_GITHUB_TOKEN_2`, selon le GO-2026-11-22-04 (« on utilise l'ancien » ; aucun jeton 3). Tout le reste est repris de la v1 mot pour mot. Toute autre forme, qu'il s'agisse d'une option de plus, d'une variable de banc ou d'un autre outil, exige une nouvelle version de cette note et le mot de la mère.

## Préalables (aucun envoi sans les quatre)
1. Le nom du jeton : `CONTROLE_IA_GITHUB_TOKEN_2` (GO-2026-11-22-04). Seul son nom est connu de la session ; il n'est jamais affiché. Sa validité se vérifie sur la machine même, au clonage du pas b (code 41 sinon), comme le dit la réserve du GO.
2. Le contrôle d'absence de la branche `recuperation/palier-0b-programme-1-essai-3-v1` sur le vrai dépôt. Le fabricant le refait lui-même, par `git ls-remote` en lecture, et refuse en 8 si la branche existe.
3. Les empreintes des pièces, contrôlées juste avant le fabricant :
   - fabricant v8 `a91f3403…` ;
   - script v6 `f61aea46…` ;
   - amorce v6 `524cfc4a…` ;
   - réducteur v6 `b1a4d216…` ;
   - outil v2 `73046b31…` ;
   - lanceur v4 et gardien v4, tels que le fabricant les épingle.
4. La ligne de GO (GO-2026-11-22-04) et le mot de Lazar pour la dépense, au devis v5 ; et, puisque le classifieur a refusé la commande 1 le 22 à 04:55Z, le mot de Lazar écrit dans la session qui exécute, qui autorise ces trois commandes.

## Commandes, dans cet ordre, depuis la session du compte organisme
Les deux pièces sont lancées depuis leurs dossiers versés : `auteur-fabricant-v8-amorce-epinglee/` et `auteur-controle-sortie-v2/`. `SORTIE` est un fichier neuf, hors de tout dépôt, écrit en mode 600 dans le dossier de travail de la session.

1. Fabrication :

   `bash …/auteur-fabricant-v8-amorce-epinglee/fabriquer-donnees-demarrage-v8.sh CONTROLE_IA_GITHUB_TOKEN_2 SORTIE f61aea46033d63dec6fde0cd66455f5474e000d140d9d98c5f23ab61976aeeb2`

   Aucune variable `FABRICANT_*` n'est posée. L'heure H0_PREVU est prise par le fabricant lui-même.
2. Contrôle à blanc :

   `/home/user/controle-ia-travail/.venv/bin/python -I …/auteur-controle-sortie-v2/controler-et-creer-essai-3-v2.py SORTIE RELEVE-A-BLANC --a-blanc`

   Le code attendu est 0. L'empreinte et la taille du corps sont consignées.
3. Création :

   `/home/user/controle-ia-travail/.venv/bin/python -I …/auteur-controle-sortie-v2/controler-et-creer-essai-3-v2.py SORTIE RELEVE-CREATION --envoyer`

   - Le jeton de Hetzner est lu par son seul nom, `HCLOUD_TOKEN`.
   - **Ni `CONTROLE_BANC`, ni `--adresse`, ni `--nom-jeton`, ni `--pause-apres-lecture`.**
   - L'outil relit les données en une seule fois et les recontrôle avant l'envoi.

## Après l'envoi
- Je relève l'identifiant du serveur et l'heure de la réponse, qui fait H0. Le relevé est expurgé, sans mot de passe root ni `user_data`.
- Je consigne la dépense dans les registres.
- Si aucune poussée n'arrive sur `recuperation/palier-0b-programme-1-essai-3-v1` dans les 2 h, le serveur est détruit par son identifiant.
- Je fais le relevé à 6 h, depuis la branche de récupération.
- Je détruis le serveur à H0 + 98 h, par son identifiant, et je le consigne dans `registres/arrets.md`.
- Je rappelle à la mère de faire révoquer ou faire expirer le jeton 2 par Lazar à la fin de l'essai.
- Si l'envoi échoue (refus, code non nul, redirection), rien ne se refait sans le mot de la mère. Une création refusée par Hetzner ne coûte rien.
- Si le classifieur refuse encore une commande malgré le mot de Lazar, je m'arrête et je le dis ; voie (b) : Lazar lance les trois commandes depuis son poste.

## Différence avec la v1
Préalable 1 (jeton 3 → jeton 2 nommé), préalable 4 (mot de Lazar dans la session, après le refus du classifieur), commande 1 (`NOM_DU_JETON_3` → `CONTROLE_IA_GITHUB_TOKEN_2`), et deux lignes « après l'envoi » reprises de la passation de 06:30Z (garde des 2 h, refus du classifieur). Rien d'autre.
