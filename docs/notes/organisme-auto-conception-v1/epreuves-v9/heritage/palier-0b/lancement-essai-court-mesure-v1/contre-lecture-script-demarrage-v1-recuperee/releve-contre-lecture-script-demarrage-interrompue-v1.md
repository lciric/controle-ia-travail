# Relevé de la contre-lecture S du script de démarrage — interrompue, récupéré — v1

Pièce de travail (classe C), recopiée par la session du compte organisme le 2026-11-21 vers 20:35Z depuis le rapport de fin de l'agent. **La contre-lecture a été arrêtée sur un refus d'autorisation automatique** : l'agent lançait `env --null` pour lister les noms des variables `GIT_CONFIG_*` du conteneur, une sonde dont il dit lui-même qu'elle était inutile. Il n'a ni reformulé ni découpé, et sa pièce n'est pas écrite. Ce relevé reprend son rapport sur le fond, sans rien changer ; il n'est pas relancé.

Pièces vérifiées par l'agent à leur empreinte : script de démarrage `580d81c5…aa1459`, fabricant `a7d54bf0…a098`, mandat `dcd05a42…fce3d`, devis `452e7bcf…47fb`, extrait de la limite `d835ab68…7b0e`.

## Verdict provisoire : À corriger
Rien n'est cassé pour la décision de lancer, sauf une fenêtre étroite, à la question 3.

## Les cinq questions
1. **Jeton hors du fichier de droits 600 : tenu.**
   - Le jeton n'est jamais exporté (script, l. 105-110 et 119-124).
   - Guetteur de `/proc/PID/environ` et `cmdline` : 258 balayages, 46 972 lectures, zéro trouvaille. Rien non plus dans l'environnement des faux apt et du faux programme, sur la sortie standard, ni sous la forme base64 de `x-access-token:JETON`.
   - Témoins vrais par construction, vus rouges : jeton exporté (4 trouvailles), jeton sur la sortie standard (1 ligne), base64 au journal (1 fichier).
   - Réserve mineure : l'assistant d'authentification rend le jeton à n'importe quel hôte. Un contrôle de l'hôte coûterait peu.
   - Écart déjà déclaré par l'auteur, non rejoué : copies de cloud-init, service de métadonnées, programme en superutilisateur.
2. **Poussée ailleurs, suppression, réécriture, force : tenu pour le script, la garde seule ne suffit pas.**
   - Une seule poussée, avec une référence explicite, sans « + » (l. 76-77). Le dépôt de lecture a une adresse de poussée invalide (l. 146).
   - Garde de l'auteur rejouée : 4 refus, 1 admission.
   - Artefacts du contre-lecteur : étiquette, `--all` et `--mirror` sont refusés. Sont admis, en revanche : `--no-verify` vers une autre branche, parce que le crochet est local ; et « + » vers la branche permise, histoire réécrite, parce que le crochet ne regarde ni la force ni l'ascendance. Une poussée du script sur une histoire divergente est refusée par le serveur.
   - À durcir : refuser toute mise à jour non descendante dans le crochet. Contre un processus en superutilisateur qui lit le jeton, rien ne tient (écart déclaré). La protection de branche côté GitHub n'est pas vérifiée.
3. **Commande étrangère, racine autre ou avec `.git` : cassé pour une fenêtre étroite, tenu ailleurs.**
   - Les pièces sont contrôlées sur la copie de tenue (l. 174-183). La racine est verrouillée deux fois (script l. 158, lanceur v4 l. 160-170). Le cas c3 rejoué rend le code 53.
   - **Casse** : le refus d'un `.git` n'est fait qu'au pas (c), l. 153. Le lanceur v4 accepte un `.git` au sommet et ne contrôle alors que la tête et les fichiers suivis (l. 124-136). Artefact `cl-q3-git-apres-c` : un faux pip fabrique un vrai `.git` et un intrus non suivi après le pas (c). Le script rend 0 et la racine part avec le `.git` et l'intrus.
   - Correctif simple, non rejoué : refaire le test du `.git` juste avant le pas (f).
   - La porte d'essai `ESSAI_DEMARRAGE_*` (l. 9-19) n'est pas refusée en production : elle est seulement consignée à la première ligne du journal. Le chemin de production par défaut n'a jamais été joué.
4. **Heure d'arrêt autre que H0_PREVU + 94 h : tenu pour le calcul, deux réserves.**
   - 30 couples (6 valeurs limites de H0_PREVU × 5 fuseaux) sont égaux au calcul indépendant du contre-lecteur, sans écart. Le témoin faux donne 9 écarts hors UTC, comme prédit. Le script et le gardien reçoivent la même heure.
   - Réserve 1 : l'heure ne peut être surchargée que par `ESSAI_DEMARRAGE_OPT_GARDIEN`, la dernière valeur gagnant.
   - Réserve 2 : pas de borne basse. Avec un H0_PREVU périmé (cas `cl-q4-h0-ancien`), le script rend 0 sans alerte, et le gardien arrête le programme moins d'une seconde après son départ. Un garde-fou en code 21 sur l'âge de H0_PREVU coûterait peu. Un H0_PREVU trop lointain est déjà refusé (code 82).
5. **Taille et refus : tenu.**
   - Taille refaite : 32 112 octets pour un jeton de 44 signes ; 32 161 pour 93 signes ; 32 468 pour 400.
   - Le fabricant accepte exactement 32 768 octets et refuse dès 32 769 (code 6), y compris avec un remplissage en caractères accentués. Aucun fichier ni jeton n'est laissé après un refus.
   - La spécification de Hetzner dit « limited to 32KiB » sans préciser si ce sont des octets ou des signes. La marge dépend de la lecture : 693 octets bruts ; 196 en chaîne JSON UTF-8 ; −76 en chaîne JSON échappée en ASCII, avant d'ajouter les 37 signes du jeton. Caler le seuil du fabricant sur la lecture la plus stricte, ou alléger le script (68 signes non ASCII), redonnerait de la marge.

## Avis sur les points ouverts (sans trancher)
- **Pièces dans les données de démarrage.** Pour : aucune seconde lecture réseau, et un double contrôle d'empreinte. Contre : la marge est de 656 octets au mieux, et négative dans une lecture JSON ; chaque ligne ajoutée la consomme, et le jeton et les pièces sont dans le même bloc. L'autre voie, une branche lue par identifiant de commit, libère le budget mais ajoute une lecture réseau que le mandat (point h) n'admet pas. Le contre-lecteur penche pour garder le transport en resserrant le seuil du fabricant.
- **Code 5.** Le choix est moins binaire qu'il n'en a l'air. Dans le cas `cl-q5-lanceur-refuse`, le lanceur refuse au vrai départ (code 10). Le script de départ rend 0, et non 5. Le script rend 0 avec « pas (f) : fait », sans alerte. L'état versé ne montre que « code de sortie : 10 », et la raison reste dans `journal-essai-3.txt`, qui n'est pas versé. Proposition : si le départ rend 5, lire `code-de-sortie.txt` ; programme mort avec un code non nul : arrêt net et versement de l'échec ; programme vivant : poursuite, avec une ligne visible dans l'état.
- **Fichiers à verser en plus** : `journal-essai-3.txt`, avec un plafond de taille, car l'historique git le multiplie à chaque versement ; `sortie-gardien-essai-3.txt` ; le contenu de `arret-gardien.txt`. Le journal de la boucle de versement ne peut pas se verser lui-même.
- **Branche neuve réservée à la machine** : oui, avec une vérification avant la création qu'elle n'existe pas. Cas C1 : si l'histoire distante diverge, chaque poussée est refusée, et la machine n'a aucun autre canal de sortie (port 22 fermé), donc les données sont perdues à la destruction. Le relevé à 6 h, s'il était poussé par un autre poste sur cette branche, la rendrait justement divergente.

## Trouvaille de côté
Le script exporte `DEBIAN_FRONTEND` et `GIT_CONFIG_GLOBAL=/dev/null` dans l'environnement du programme mesuré, qui hérite donc de ces réglages.

## Limites du banc du contre-lecteur
Le banc tourne sur factices : HTTP et non HTTPS, ni GitHub ni cloud-init, balayage toutes les 50 ms, intervalle de 1 800 s jamais joué. Premier pas non justifié : la façon dont Hetzner compte la limite (octets décodés ou corps JSON échappé). Incidents : disque plein en cours de route ; seules les racines et dépôts de lecture de ses propres cas ont été supprimés.
