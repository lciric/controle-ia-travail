# Vérification des corrections de la commande v4 — v1

Même contre-lecteur Opus que la contre-lecture de la v3. Rapport recopié tel quel.

Verdict : Conforme avec réserves. Mes sept réserves sont corrigées ou nommées, les trois commandes sont inchangées, et le diff v3→v4 ne montre aucun changement non déclaré. Restent deux points à écrire et un point mineur.

1. **Réserves corrigées.**
   - 1 : le titre « Commandes, dans cet ordre… » est rétabli.
   - 2 : le `stat` vérifie le mode 700, et le sort du texte réduit est dit au préalable 3.
   - 4b : la fenêtre de 2 h est écrite, avec la règle des 1 h 30.
   - 4d : l'écart au devis v5 est nommé, au préalable 4 et dans sa propre section.
   - 5a : `SORTIE` est retirée par `shred -u`.
   - 5b : le jeton dans les métadonnées du serveur est rappelé.
   - 5c et le mode 700 sont nommés dans « Réserves connues ».
   - Le passage de la classe C à la classe B est déclaré (« En-tête »).
   - Empreintes vérifiées : v4 `aef39cc4…` et le recopiage de mon rapport `bd858ef7…` concordent avec leurs compagnons.

2. **À corriger : la reprise après 1 h 30 ne marche pas telle qu'écrite (ligne 22).** « Tout se refait depuis la commande 1 » bute sur trois refus :
   - `mkdir` refuse, puisque `/home/user/essai-3-sortie` existe déjà ;
   - le fabricant refuse en 4 (ligne 60), puisque `.sans-jeton`, `.charge.b64`, `.empreintes.txt`, `.script-reduit.sh` et `.reduction.txt` sont gardés ;
   - l'outil refuse en 2 si un relevé existe.
   Une reprise exige un nouveau dossier ou un nouveau nom de sortie, donc une v5. Il faut l'écrire.

3. **À préciser : « voie (b) » se contredit.**
   - La ligne 54 dit « voie (b) : Lazar lance les trois commandes depuis son poste ». Ce n'est ni la voie (b) du devis v5 (création depuis le conteneur), ni sa voie (a).
   - La ligne 57 dit que la voie (a) « reste le repli si le classifieur refuse encore ».
   Il faut un seul repli, nommé une seule fois.

4. **Point mineur : le retrait de `SORTIE` laisse un cas de côté (ligne 47).** Le retrait n'est prévu qu'après la réponse ou après la fenêtre. Un refus au contrôle à blanc (commande 2) n'est pas couvert, et le fichier qui porte le jeton reste alors sur disque.

5. **Les ajouts n'introduisent ni erreur ni fuite.**
   - Le `stat -c %a` est juste.
   - `shred -u` convient. Il n'efface pas avec garantie sur un système de fichiers journalisé ou en copie sur écriture, mais le dossier en 700 et la révocation en fin d'essai couvrent ce risque.
   - L'empreinte du fichier retiré ne révèle pas le jeton.
   - La marge de 30 min laissée par la règle des 1 h 30 couvre le temps de démarrage de la machine.

## Suite donnée
Points 2, 3 et 4 repris dans `commande-creation-production-essai-3-v5.md` ; renvoyée au même contre-lecteur.
