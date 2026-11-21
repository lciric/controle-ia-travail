# Relevé de la contre-lecture S du script de démarrage v2 — interrompue, récupéré — v1

Pièce de travail (classe C), recopiée par la session du compte organisme le 2026-11-21 vers 22:00Z depuis le rapport de fin de l'agent. **La contre-lecture a été arrêtée par une garde de l'outil** (« Blocked: standalone sleep ») : l'agent attendait la fin de son cas « code 5, programme vivant » (`q6-enfant`) par un `sleep 100` isolé. Il n'a ni reformulé ni découpé, et sa pièce n'est pas écrite. Ce relevé reprend son rapport sur le fond, sans rien changer ; il n'est pas relancé. L'agent n'a ni affiché ni listé l'environnement du conteneur.

Pièces vérifiées : script de démarrage v2 `63ea8498…`, fabricant v2 `8096d3cf…`, sur la branche au commit `e1e01f20`.

## Verdict provisoire : À corriger
Un défaut avéré (Q1, correction d'une ligne), deux réserves, et une erreur de chiffre dans le rapport de l'auteur. Rien n'est cassé en dehors de la précondition de Q1.

## Les six questions
1. **Jeton : cassé sous précondition.**
   - Le fabricant range le jeton dans la variable `J`. Si la session exporte déjà une variable `J`, tous les enfants du fabricant héritent du jeton dans leur environnement. Mesure par un espion `git` factice, lu par son identifiant : 2 appels sur 2 portent le jeton, contre 0 sans `J` exportée au préalable.
   - Que la session exporte une variable `J` n'est pas vérifié. Correction : `declare +x J` avant l'affectation.
   - Le reste tient :
     - le jeton n'apparaît nulle part dans les fichiers, l'histoire (3 cas) ni `ps` (2 844 puis 3 846 relevés) ;
     - droits 600 sur le fichier du jeton, 700 sur son dossier ;
     - les 19 demandes tordues faites à l'assistant d'authentification ne rendent le jeton qu'à `https` et `github.com` ;
     - un jeton non ASCII est refusé (code 3).
   - Fait hors de la question, déjà dit par l'auteur : le jeton existe aussi dans les copies de cloud-init et dans le service de métadonnées de Hetzner.
2. **Poussée : tenu.**
   - Les 7 artefacts de l'auteur sont refusés.
   - 10 artefacts du contre-lecteur sont refusés par le crochet, le distant restant inchangé : distant avancé par un tiers (poussée simple et forcée), plusieurs références, `--all`, `--tags`, `--mirror`, `--delete`, autre adresse.
   - La poussée descendante saine est admise.
   - `--no-verify` contourne le crochet, ce qui est la limite déjà déclarée par l'auteur ; le script n'en contient pas, et le fabricant refuse un script qui en porte.
3. **Commande et racine : tenu sur lecture, essais non joués.**
   - Le commit `d7f949ac` porte 35 732 entrées, sans lien ni `.git`. Les pièces sont contrôlées par empreinte, et le départ passe par le lanceur v4.
   - Réserve : le contrôle du `.git` au pas (f) est un instantané ; rien ne le refait juste avant `demarrer`.
   - La table de racines altérées du contre-lecteur (fichier ajouté, lien, modification, suppression, trois formes de `.git`, dossier vide, droits) est prête, mais n'a pas été jouée.
4. **Heure d'arrêt : tenu, une réserve.**
   - 14 cas d'âge de H0_PREVU, tous conformes : 7 195 s accepté, 7 210 s refusé, +590 s accepté, +610 s refusé, et 9 formes mal formées refusées.
   - Dans 3 cas complets, l'heure d'arrêt vaut bien H0_PREVU + 94 h. Le gardien refuse une heure au-delà de 94 h + 600 s.
   - **Réserve importante** : quand le départ rend le code 5, le gardien n'envoie aucun signal (« identité non confirmée »). L'arrêt de durée à 94 h n'arrête donc pas le programme. C'est lu dans le code du gardien ; le cas `q6-enfant` devait le montrer, mais son résultat n'a pas été lu. Le garde-fou reste la destruction de la machine depuis la session.
5. **Taille : tenu.**
   - Avec un jeton de 100 signes : 31 958 octets bruts. En JSON échappé en ASCII : 32 479, soit une marge de **289**, confirmée par quatre voies : `json.dumps`, un comptage manuel, un comptage signe par signe, et Go `SetEscapeHTML(false)`.
   - Avec l'échappement HTML de Go (`json.Marshal`) : 33 074, soit **−306**, confirmé avec le vrai Go. Les 119 signes `<`, `>` et `&` coûtent 595 octets de plus ; avec `/` échappé aussi, on arrive à 33 552.
   - Le fabricant est exact à la borne, sur 13 cas : 32 768 accepté ; 32 769 et 32 770 refusés, quel que soit le remplissage. Les signes de contrôle sont refusés (code 6).
   - **Erreur du rapport de l'auteur** : « octets bruts 32 140, marge 628 » est faux ; c'est **31 958 et 810**.
6. **Code 5 et versements : partiel.**
   - Le plafond de 1 Mio tient : une sortie de 2,5 Mo donne 1 048 576 octets versés ; `arret-gardien.txt` est versé en entier ; 10 commits.
   - Sur lecture :
     - un lanceur tué sans écrire son code, avec un journal vide, finit en code 0 après 300 s, **sans échec écrit** ;
     - un échec 84 (gardien refusé) **laisse le programme tourner** sans gardien ni boucle de versement.
   - Non joués : le cas « code 5, programme mort » et la lecture du cas `q6-enfant`.
   - Les outils livrés ne contiennent pas le faux `setsid` que le rapport de l'auteur cite pour les cas `m5` et `cl-q5`. Le contre-lecteur a écrit le sien.

## Ce qui reste à faire
Lire le résultat de `q6-enfant`, où l'on attend « aucun signal envoyé » dans `arret-gardien.txt`, jouer `q6-mort` et la table de racines, puis écrire la pièce et son « Relevé de méthode ».
