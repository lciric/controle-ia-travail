# Couche 1 bis — lecture v2 avec `e2` (288 épisodes, 144 d'épreuve), traits du texte et traits internes — exploratoire

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Fable 5.1), écrit après le relevé `date -u` de 00:02:39 UTC
le 28 octobre. **Exploratoire (R-546), zéro dépense** : agents simulés, juge et banque réels ; code v7 version 26. Données :
branche `donnees/t05-banque-complete-v1` au commit `13f3047d` (session-depot n° 97 : notations `e2`, deux dossiers de
compléments, sceaux vérifiés), jointes au pilote (`/home/claude/controle-ia-travail`). Même construction et même lecture
(L1, L2, L3) que la v1 (`../couche1bis-lecture-v1/lecture-couche1bis-v1.md`, `ec65a500…`) et que la lecture des traits
internes (`../traits-internes-lecture-v1/lecture-traits-internes-v1.md`, `bd199e2e…`) ; quatre courses : traits du texte
seuls, puis traits du texte + trois composantes internes des couches 7, 15, 23. Commandes : `commandes-v2.sh`.

## Verdict

1. **Validité tenue (L1)** sur les quatre courses : aucun témoin faux promu.
2. **Dents (L2)** : témoins plantés promus jusqu'à la **force 0,5** sur les quatre courses (4 sur 5 ; la force 0,25 jamais) —
   avec 144 épisodes d'épreuve par fiche, la couche 7 rejoint les autres (en v1, à 96 épisodes, elle perdait la force 1,5).
3. **Rien de promu sur les 13 moniteurs réels (L3)**, à aucune course ; mais les **richesses maximales montent avec les
   données** : la meilleure proposition sur traits du texte passe de log W 0,53 (192 épisodes) à **2,28** (288 ; « 3B:BALANCE
   dépend de l'écart type des jetons par action », richesse finale 2,09, seuil log(1/α) ≈ 3,0, m = 17) ; sur traits internes,
   la couche 23 donne **2,48** en cours de lecture (« 3B:RIGOR dépend de la troisième composante de la couche 23 »), mais la
   richesse **retombe à 0,77** en fin de lecture : un pic, pas une tenue. Couches 7 et 15 : 1,30 et 1,24 au mieux.

**Lecture.** Toujours « non » à la question « ces traits prédisent-ils les notes des juges au-delà de la marginale ? », mais
un « non » moins net qu'à 192 épisodes : deux candidats approchent le seuil d'une fiche seule sans l'atteindre, et aucun
n'atteindrait le seuil de la famille (m = 17). Sous le nul, le maximum courant de 12 trajectoires monte couramment à 1 ou 2 :
ces pics ne sont **pas** un signal (R4 : ne pas lire un maximum courant comme une preuve). Ce qu'ils valent : des **candidats
à relancer par héritage** sur une partie d'épreuve **disjointe** — qui n'existe pas encore (les 288 épisodes sont tous lus) ;
les épisodes honnêtes de la couche 2 la fourniront.

## Réserves

- Même graine (20261027) et même chercheur mécanique qu'en v1 : les propositions sur traits du texte sont identiques ;
  l'écart avec la v1 vient des données seulement (96 → 144 épisodes d'épreuve, 48 → 72 de calibrage).
- Trois composantes de la moyenne des activations par couche restent un résumé grossier ; une sonde (T0.7) lit autre chose.
- Les notes `e2` du juge 3B sont rares (session-depot n° 97 : 6 sur 60 et 5 sur 36 à score non nul) : les moniteurs « 3B:… »
  ont des issues plus déséquilibrées sur `e2` ; le nul informé l'absorbe (ajusté sur le calibrage), mais c'est à garder en
  tête pour toute fiche « 3B:… » promue un jour.
- Aucun préenregistrement (R-546) : rien d'opposable ; ni « non » ni candidat n'est un résultat.

## Fichiers

`banque-e2.json` (18 moniteurs, 288 instances, 4 traits), `banque-e2-c{7,15,23}.json` (7 traits), témoins, `course-e2*/`
(manifeste, journal, archive, mémoire, `lecture-couche1bis.json`), `resume-lecture-v2.json`, `journal-lancement-v2.log`.
