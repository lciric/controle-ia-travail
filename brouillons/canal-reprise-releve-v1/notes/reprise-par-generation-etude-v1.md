# Étude : reprendre une course du noyau génération par génération (courses longues sans machine louée) — v1

Écrite par conv-audit le 25 octobre 2026 (vers 14:30 UTC), sur la décision de Lazar du 25 octobre, 14:39 Paris
(« ok inscris-le dans journal et programme » : 2 h pour le second pilote ; pour les courses longues, **la reprise par
génération d'abord**, Vast seulement si elle n'est pas faisable ; pièce
`envois/decision-courses-longues-reprise-par-generation-v1.md`, `c1f1d687…`). Lecture du noyau `b1c7f4b6`
(`essaim_m3/noyau/boucle.py`, `cli.py`, `archive.py`), sans exécution. Aucune modification du noyau ; aucune décision.

## 1. Le besoin

Une course tourne dans une seule commande de fond de la session qui lance ; l'outil l'arrête au plus tard après 7 200 s.
Avec 2 400 s par génération et l'attente de 900 s des appels en vol (`serveur.ATTENTE_FILS_S`), deux générations tiennent
(pire cas ≈ 6 900 s) ; la course M réelle du second pilote a duré 26 min 29 s (13:51:55–14:18:24 UTC). Une course de
plus de deux ou trois générations doit donc se faire en **segments**, chacun dans sa commande de fond, la course gardant
une seule identité (R3 : un seul nom, un seul manifeste d'origine).

## 2. Ce que le noyau a déjà

- `Noyau.recharger(course, …)` (`boucle.py` l. 124–154) relit une course finie (manifeste, banque, mission, lignes de
  l'archive), recompte la dépense et recrée les lignées, **inactives** ; il sert aujourd'hui à la confrontation séparée
  (CR-04) : « rien de la course n'est réécrit ; les dépenses nouvelles s'ajoutent au plafond restant ».
- Les **graines** ne dépendent que de l'entropie et de (lignée, génération, usage, phase) (`graine`, l. 339) : une
  génération g tirée après une reprise a la même graine qu'en continu.
- La **mémoire** passe par la vue d'archive de la lignée (`archive.vue`, à côté de la course) et l'**historique** par
  `archive.historique(lignee)` (l. 630) : tous deux relus sur disque à chaque génération.
- L'**espace des organismes** est calculé depuis le chemin de la course (`bac_a_sable.espace_organismes`, l. 184) : même
  chemin, même espace.
- `rapport()` écrit `rapport-vN.json` au premier N libre (l. 921–925) : un second rapport ne remplace pas le premier.

## 3. Ce qui manque (trois manques, aucun autre trouvé à la lecture)

1. **Le successeur de la dernière génération n'est pas gardé** : il n'est copié dans `lignees/<lignée>/g<g+1>/organisme`
   que si `g + 1 < generations_max` (l. 800–804) ; à la dernière génération, la lignée finit en « générations
   maximales » et son successeur reste dans le dossier de travail, rendu à root puis archivé avec l'espace. Pour
   reprendre, il faut le garder : même copie sans liens, vers `lignees/<lignée>/g<G>/organisme`, marquée « gardé, non
   lancé » (un champ du résumé), sans rien changer à la fin de la lignée.
2. **Aucune commande de reprise** : il faudrait `essaim_m3 reprendre --course <dossier> --generations-plus N
   --plafond-segment X --go … --registre-go …` qui recharge la course, réactive les lignées finies en « générations
   maximales » avec leur successeur gardé, porte `generations_max` à G + N, écrit un **manifeste de segment**
   (`manifeste-segment-k.json` : empreinte du manifeste d'origine, segment k, génération de départ, plafond du segment,
   GO, code, versions) et continue `boucler()`. Refus : course absente ou non finie, lignée invalidée ou sans successeur
   gardé, banque, mission, code ou décalage d'utilisateurs différents de ceux d'origine, segment k déjà écrit (R3 pour les
   segments), espace autre que celui du manifeste.
3. **Le lanceur ferme la course à la fin de chaque appel** (archive `ferme.tar.gz`, copies retirées) : pour une course en
   segments, la fermeture et la poussée n'auraient lieu qu'après le dernier segment ; entre deux segments, la course
   reste sur disque, à root, jamais lue (les mêmes interdits de lecture que T2), le conteneur jamais redémarré
   (comme pendant une course).

## 4. Ce qui le vérifierait (avant tout usage)

- **Équivalence** : en simulation, une course de 4 générations en deux segments (2 + 2) et la même course en un seul
  appel, même graine : mêmes appels (nombre, espèces, statuts), mêmes empreintes d'organismes et de mémoire à chaque
  génération, mêmes consignes servies ; seuls diffèrent les champs d'heure et le manifeste de segment. C'est le critère
  d'acceptation.
- **Artefacts** (R5) : chacun des refus du § 3.2 ; reprise d'un segment déjà écrit ; successeur gardé modifié entre deux
  segments (empreinte) ; plafond du segment dépassé ; fichier `STOP` posé entre deux segments.
- Les 141 essais du noyau inchangés ; un préenregistrement qui déclare d'avance le nombre de segments, la génération de
  départ de chacun et le plafond de chacun.

## 5. Coût et limite

Code : de l'ordre de 150 à 250 lignes au noyau et au lanceur, plus les essais (estimation non opposable). Limites : le
conteneur doit vivre entre deux segments (un redémarrage perdrait la course, comme aujourd'hui) ; un segment reste borné
à 7 200 s, donc à deux ou trois générations de 2 400 s ; la session qui lance doit se réveiller à la fin de chaque
segment (réveils programmés). Si le conteneur ne peut pas vivre assez longtemps, la machine louée redevient la voie
(Vast), comme Lazar l'a dit.

## 6. Ce qui est à décider (par Lazar, plus tard)

Écrire ou non ces trois changements, sur une branche à conv-audit, avec leurs essais, avant les courses longues de
l'étape 1 ; aucune course en cours n'en dépend.
