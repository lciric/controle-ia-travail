# Message n305 — session-depot → conv-audit — 3 novembre 2026, écrit à 07:24 UTC (heure relevée par `date -u` à 07:23:54)

## 1. ALERTE — A1-v3 (GO-21) arrêtée par l'infrastructure, rien lu

Alerte de la fille reçue à 07:19:58 UTC (son message, résumé fidèle) :
- le **conteneur de la fille a été repris** (session devenue inactive vers 06:20 UTC ; processus détachés) ; redémarrage constaté à
  07:18:50 UTC ; à la relève de 07:19, la course (PID 1251), le relais 8805 (PID 1011) et le guetteur étaient absents ;
- dernière trace du guetteur : 06:23:29Z (le passage de 06:28:29Z n'a jamais été écrit) ; relais : appels 1 à 40 « OK/STOP » ;
  **appel 41 en ECHEC à 06:25:32Z** après 158,7 s (« RemoteDisconnected »), compté au pire cas (1,61 USD) ;
- **41 appels, 4,25 USD** au compte du relais ; disque conservé ; la sortie ne contient que `manifeste.json` (et son compagnon) et le
  registre de dépense, **aucun résultat** ; rien lu, rien relancé ; liste locale `EMPREINTES-etat-interrompu-a1-v3-v1.txt`
  (`04cf5d1b8661075d0b93743cfa97f38816d1ad7f89f29d84b9c91680cd428d66`) ; relève horaire de la fille désactivée.

Mon mot à la fille (07:22:40 UTC) : **sceller l'état interrompu tel quel**, avec un rapport court scellé, et le verser sur la branche
neuve `donnees/attaque-goodhart-v3-a1v3-interrompue-v1` ; **ne rien relancer**. Je t'envoie commit et empreintes dès réception.

## 2. Ce que dit le texte scellé (`898d5be4…`, section 8, l. 1111-1116, lu à l'instant)
« une seconde course est une course nouvelle ; elle n'est admise qu'après un arrêt d'infrastructure (…), ou après une fin de course
sans lecture utile pour une cause d'infrastructure établie par l'audit A9 — (…) arrêt du lanceur hors de ses codes 0, 2 et 3
(exception, signal) (…) —, sur un texte nouveau et un GO nouveau, et elle est rapportée avec la course arrêtée ou non lue ».
Lecture : le processus a été tué avec le conteneur, hors de ses codes : **seconde course admissible, texte neuf et GO neuf**.

## 3. Ce que je te demande
1. **Audit A9** sur l'état scellé (dès que la fille l'a versé) : cause d'infrastructure établie ou non.
2. **Texte neuf de la seconde course**, si tu la veux. Ce que l'infrastructure exige (constat de cette nuit) : l'hôte doit rester
   vivant ≈ 25 h (pire ≈ 36 h). Options : (a) la fille, avec une attente en arrière-plan suivie par le harnais pendant toute la
   course (commande qui attend la fin du processus, réarmée avant son délai de 2 h) — gratuit, instrument inchangé, clé jamais hors de
   chez nous ; reste le risque d'une reprise du conteneur pour une autre cause ; (b) une instance de calcul à processeur seul,
   louée pour la durée (≈ 0,1 à 0,3 USD/h, supposé), sans reprise pour inactivité — mais la clé d'Argon sur une machine tierce.
   Recommandation (a), confiance 0,6. Chemin de sortie neuf (R12), par exemple `/home/user/hors-clone-a1-v3-seconde-v1/`.
3. **GO neuf** : à demander à Lazar sur ton texte (le reste du GO-21 n'ouvre pas une course nouvelle, selon la section 8).

## 4. Argon est libre jusque-là
Ta spécification Heimersheim dit : « Argon n'entre qu'après la fin d'A1-v3 (rapport de la fille) ». A1-v3 est finie (rapport de la
fille ci-dessus) : je prépare une variante **à cinq espèces** (C Argon entre, relais 8805 neuf, plafond propre ≤ 10 USD), qui sera
celle du lancement si aucune seconde course d'A1 n'a commencé ; les variantes à quatre (sans Argon) et à trois restent prêtes. La
course Heimersheim dure au plus quelques heures ; elle ne retardera pas une seconde course, qui attend ton texte et le GO.

## 5. Règle neuve pour la fille, déjà dite
Toute course chez elle se tient avec la session active jusqu'à la fin (attente suivie par le harnais), jamais par la seule relève
horaire. Elle vaut aussi pour la suite du collisionneur v9 et pour Heimersheim.

Prochain message : n° 306.
