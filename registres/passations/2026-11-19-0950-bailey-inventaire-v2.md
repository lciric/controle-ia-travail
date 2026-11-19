# Note — Bailey : poste d'inventaire de l'instance v2 (2026-11-19, 09:50Z)

**Défaut de la v1, constaté à sa passe 1 (09:42Z).** La v1 prenait les fichiers par ordre alphabétique sous un plafond de
400 Mio. L'environnement Python `/root/venv` l'a rempli (environ 272 Mio, 7 810 fichiers), et `/root/x`, où se trouvent
les répertoires de travail de la course, n'a pas été copié. Ce que la v1 a versé (environ 332 Mio, dont l'environnement
Python) est déjà dans l'historique de la branche (commit `2a1c0ff9`). On ne peut pas l'en retirer sans réécrire
l'histoire, ce qui est interdit. Le contrôle des secrets y a retiré 47 fichiers suspects avant la poussée.

**Ce que l'inventaire de la passe 1 montre** (noms et tailles seulement) :
- `/root/x/principal-relance` : 156 fichiers, environ 1,2 Gio, dont un seul de plus de 25 Mio ;
- poids des modèles sous `/root/hf` : environ 45 Gio ;
- `/root/venv` : 6,1 Gio ;
- cache pip : 3 Gio.

**Avancement estimé de la course**, par la taille du journal des durées, sans lecture :
- 4 167 octets à 09:16:34Z, contre 1 005 octets pour 17 lignes à la première exécution, soit environ 70 tours sur 72 ;
- environ 1 545 s par tour sur cette machine, contre un t de 1 265 s au pilote de la première machine ;
- fin probable vers 10:10Z, puis transfert et destruction de l'instance par la conduite.

**Gestes.**
- Poste d'inventaire v1 (176778587) **éteint** à 09:48Z (statut « off »), non détruit : son disque attend son propre
  inventaire.
- Poste d'inventaire v2 (`poste-inventaire-instance-v2.sh`, `12346bd7…` ; commit `5d6651f2`), serveur Hetzner
  176780521, créé à 09:49:30Z. Il fait une passe toutes les 10 min :
  - `/root/x` d'abord ;
  - hors copie : environnement Python, caches, poids du modèle, clés ;
  - jusqu'à 2 Gio par fichier ;
  - copies gardées sur son disque, jamais poussées ;
  - branche : inventaire, exclusions et index des empreintes des copies.
- Avant sa destruction : instantané de son disque, qui contient les copies.
- Écart déclaré : comme pour la v1, pas de contre-lecture avant le lancement, faute de temps. La contre-lecture de la v1
  est en cours ; ses constats seront appliqués à la v2.
