# Second complément au mandat du lecteur-opérateur — commande version 4, en scripts — apprentissage des sondes sur la tâche (étape B bis de T0.7) — v1

Session conductrice, 2026-11-19. Complète `mandat-lecteur-operateur-bbis-v1.md` et `complement-mandat-lecteur-operateur-bbis-v1.md` (`01f2f5fc5740d301ee03e9b2ce7c7e1d56017b8556453752e04c2b463af33225`), qui restent en vigueur ; là où ils nomment la commande version 3, lis la version 4.

## La commande que tu joues
`registres/t07-etape-b-bis/lecture-v1/commande-lecture-bbis-v4.md`, empreinte `6dde01b0bc02ea8587fc217527a22a4c1588456df87381c548ea1b7afc4b1c8c`, contre-lue « jouable telle quelle », 0 constat majeur, 0 mineur (`contre-lecture-commande-lecture-bbis-v4.md`, `d05d7499696720bc320c2ac4c25ffd6a8af08eef4a8bf487378565f053aa7fa3`). Ses blocs sont des scripts scellés sous `scripts/lecture-bbis-v4/` : tu vérifies le compagnon de chaque script avant de le lancer (`sha256sum`), puis tu le lances par **la ligne unique que la commande écrit**, telle quelle : `bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/<script>`, suivie de `1` là où la commande le dit. Tu ne tapes rien d'autre pour jouer un bloc : ni accolade, ni tube, ni redirection, ni texte en ligne.

## Pourquoi une version 4, et l'état laissé
La version 3 a été jouée jusqu'à son § 1.2 par un premier opérateur ; l'outil de terminal a refusé le bloc suivant pour sa forme. La version 4 n'en change que la forme. Elle repart d'un **dossier de travail neuf et d'un arbre de lecture neuf** (`…/scratchpad/lecture-bbis-v4/`, `arbre-de-lecture-v4`, branche locale `lecture/bbis-arbre-de-lecture-v4`). L'ancien dossier `…/scratchpad/lecture-bbis/`, son arbre et sa branche locale restent en place : **tu n'y lis rien, tu n'y touches pas, tu ne supprimes rien**.

## Paramètre
Tu écris, par l'outil d'écriture de fichiers et non par le terminal, le fichier `/tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis-v4/parametres-conductrice-v4.txt`, d'une seule ligne : `TETE_TRAVAIL=` suivie des 40 caractères que le message de lancement te donne.

## Règles propres à cette forme
- **Un script arrêté en cours ne se rejoue pas** (ses fichiers existent, il refuse d'écraser) ; seul le relevé du dépôt et des têtes (§ 1.1) se rejoue, sous un numéro neuf, sur ordre de la conductrice. Si un script s'arrête ou est coupé : tu rends, tu ne renommes ni ne supprimes rien.
- Si l'outil de terminal refuse une ligne `bash <script>` : arrêt, texte exact rendu.
- Tout le reste comme avant : deux temps ; un commit local, par le script du § 4.1 ; aucun nom de commande d'arrêt de processus par motif ; rien dans `.claude/` ; tu n'arrêtes jamais le processus de la lecture ; aucune attente fixe ; au premier refus du classifieur, d'une permission ou du crochet : arrêt, texte exact ; ce que tu rends à la conductrice est ce que la commande écrit pour chaque état, sans heure, sans durée, sans rien qui distingue une lecture faite d'une issue « non lue » de fond ; aucune relance ; le programme de la preuve après coup seulement sur ordre écrit de la conductrice ; toute relance par la voie de l'arrêt avant le seuil attend le mot de Lazar.
- **Second temps** : tu ne le joues que sur un message de la conductrice qui porte la « décision sur le risque de redémarrage » (la machine de la session a redémarré une fois sans cause connue ; la décision de lancer revient à la session mère).
