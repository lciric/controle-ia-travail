# Mandat du développeur habilité côté moniteurs du bras A — v2

Écrit par la session mère `session_01XJ6Mgr8BN6UanALsQatc5E` le 20 novembre 2026. Classe B. Accord : GO-2026-11-20-21, mot de Lazar « go reco ».

Tu remplaces le développeur habilité de la v1. Sa session, sur un autre compte, n'est plus joignable. Son code est intact sur cette branche, `claude/bras-a-habilite-developpeur-v1`, dont la copie de travail est `/home/user/bras-a-habilite` (tête `20d9eb38`).

## 1. Ce qui te gouverne
- Le mandat v1, même dossier : `registres/bras-a-habilite/mandat-developpeur-habilite-bras-a-v1.md` (`a156d2db…`). Ses sections 1 (« Qui tu es »), 2 (« Textes ») et 4 (« Ce que tu ne fais jamais ») valent pour toi mot pour mot. La section 3 est faite ; la section 5 est remplacée par la section 4 ci-dessous.
- Les demandes v8 de la relance, qui sont ta tâche : `docs/notes/relance-organismes-discrets-v1/demandes-au-developpeur-habilite-bras-a-v8.md` (`ba81227fcea1b6419fad012f83711e61a54c7c01dce6a34d3319266d4aaaf579`). Lis-les par `git -C /home/user/controle-ia-travail show origin/claude/pensive-bardeen-1fv7hw:<chemin>`. Leur en-tête dit quels fichiers tu peux ouvrir de la relance : rien d'autre. La demande 13 (`piece_source`) est bloquante.

## 2. Ce que tu fais
1. Réponds à chaque demande v8 dans la forme bornée qu'elle exige, d'après le code et les notes habilitées de cette branche. Écris « non établi » plutôt que de deviner.
2. Chiffrage de la lecture du juge d'une autre lignée (Qwen 2.5 7B Instruct, sur la carte louée), pour 2 560 et pour 6 400 actions, en heures de carte et en USD. Tu as accès aux internes qui manquent à la relance : débit du juge avec raisonnement, longueur de sortie par action sous sa consigne et ses réglages. Ce qui n'est pas mesuré s'écrit en fourchette, avec sa source ; aucune mesure neuve, aucun chargement de poids, aucune dépense.

## 3. Sorties
- Une pièce interne, scellée : `docs/notes/bras-a-moniteurs-v1/reponses-developpeur-habilite-demandes-v8-v1.md`.
- Une pièce **sans interne**, pour la relance, scellée : `docs/notes/bras-a-moniteurs-v1/reponses-sans-interne-demandes-v8-v1.md`. Elle ne porte que la forme bornée de chaque réponse et le chiffrage en heures et en USD. Aucun seuil, trait, vocabulaire, poids ni texte de consigne de moniteur : nomme toute pièce interne par son chemin et son empreinte.
- Scellement : `cd /home/user/bras-a-habilite && PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -B -m controle_ia.scellement sceller <fichier>`.

## 4. Méthode
- Écris dans la copie de travail `/home/user/bras-a-habilite`, tes fichiers seulement. Ni commit ni poussée : la mère verse sur cette branche, jamais sur `main`.
- Essais : seulement des essais ciblés, si tu en joues.
- Pas de code passé en ligne à l'interpréteur ; une commande simple à la fois ; aucun nom de commande d'arrêt ou de recherche de processus par motif ; aucune recherche récursive sur une racine large.
- Rien sous `archives-reponses-modeles/` ni sous `/root/.claude/`.
- Au premier refus d'outil, de classifieur ou de garde, arrête-toi et rends le texte exact.

## 5. Rends
1. La phrase de ton invite système qui nomme ton modèle.
2. Les chemins et les empreintes des deux pièces.
3. Dix lignes au plus, **sans interne** : les demandes répondues, celles « non établies », la demande 13, le chiffrage.
