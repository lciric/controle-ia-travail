# Vérification du lot final du réajustement de nos lentilles R et S (lecture par lentille neuronale, Llama 3.1 8B Instruct) : critère d'identité v6, devis v7 (et v6), programme de comparaison v4 — v1

- Heure (`date -u`) au début de la vérification : 2026-11-19T12:36:13Z ; l'heure du scellement est celle du fichier compagnon.
- Vérificateur : le contre-lecteur des versions 4 et 5 (sous-agent, **Claude Opus 5.5**, `claude-opus-5-5`), d'un autre modèle que
  le rédacteur et le développeur (Claude Fable 5.2). Il n'a écrit aucune des pièces vérifiées. Passe unique, demandée par la mère.
- Objet : branche `claude/brave-galileo-jhp684`, commit `9b6a35c1`, lu par `git show`. Empreintes recalculées, égales à l'attendu et
  au compagnon : critère v6 `0700f3da3330c1c9…` ; devis v7 `c187546226d61cf4…` ; devis v6 `ca89150408def612…` ; programme v4
  `4a0f3b2c8c73c282de3fbf7f18314e8085c7bbd03e4bb009c21775db78b09b01` ; essais `e1708b3932601b4b…`.
- Lu : le critère v6 en entier ; le devis v7 en entier par ses différences avec la v6, et la v6 par ses différences avec la v5
  (comparaison ligne à ligne) ; le programme v4 pour ses constantes (comparées par programme à celles de la v3), ses préalables
  « forme », « K1 », « K2 », l'arrêt sur une erreur, la lecture de secours et la ligne de commande ; la fin de la sortie du banc
  d'altérations (`sortie-banc-v3.txt`).
- **Sondes** : 14 appels du programme v4 non modifié, sur des pièces **inventées** (aucune pièce de `diag/` ni de `runs/`), dont trois
  par sa ligne de commande, dans le bloc-notes de la mère :
  `/tmp/claude-0/-home-user-controle-ia-travail/7344498a-9e3b-55a8-9388-941e130beae8/scratchpad/opus-contre-lecture-critere-v4/v6/sondes/sondes_v4_v1.py`
  (`77bb12430bd5ec9765db6eb6096f751214805c35e3ca6d1d9d0cca4218719a8d`), sortie `sortie-sondes-v4-v1.txt`
  (`89e28070024b845769061f20fcc3e28a3aa4bde8b5419f5a84448a52ae9963a1`), même dossier ; hors dépôt, non opposables tant que la mère
  ne les verse pas ; citées W0 à W11. Les 311 essais et le banc n'ont pas été rejoués : ils lisent `diag/` et `runs/`.
- Non lu, selon le mandat : `docs/verdicts/`, tout fichier dont le nom commence par « verdict », `diag/`, `runs/`, `donnees/`, tout
  résultat de l'apprentissage des sondes sur la tâche ou des lentilles, tout fichier « consigne-privee » ou « conception-ii-b »,
  `brouillons/ii-b-saboteur-budget-v1/`. Aucune dépense, aucune machine, aucun commit, aucun fichier existant modifié. **Aucun refus
  d'outil.**

## Conclusion, par pièce

- **Critère d'identité v6 : scellable après ce couple exact** (un seul couple : une règle pour les deux refus de démarrer du
  programme, ligne de commande refusée et sortie déjà présente, que le § 4 nomme sans dire quoi en faire). Les couples 1 à 6 de ma
  vérification des versions 5 sont portés ; aucun seuil, libellé ou autorisation ne change.
- **Devis v7 : scellable.** La v6, vue ici pour la première fois, porte les trois couples à la lettre ; la v7 n'en diffère qu'en ses
  cinq points annoncés, tous vérifiés.
- **Programme de comparaison v4 : scellable tel quel** (il l'est déjà). Ses étiquettes « critère v5 » n'appellent pas de programme v5
  (point 1). **Réserve** : mes sondes et ma lecture ne remplacent pas les 311 essais ; leur ligne « 311 passed » est non opposable.
  Avant la création, que la mère les rejoue et verse la sortie, scellée ; alors cette passe peut tenir lieu de la contre-lecture du
  programme par un autre modèle que demande le devis v7 (§ 5, point 6), pour ce qu'elle a lu.

## 1. Les couples de la vérification des versions 5
- **Critère, couples 1 à 6 : portés.** Couple 1 réparti comme il convient : le programme v4 vérifie l'arbre propre, les commits des
  manifestes lisibles et le lanceur neuf égal à l'octet au fichier de son chemin au commit du manifeste neuf (sondes W1, W2) ; restent à
  la main, valeurs comprises, le chemin nommé par la commande scellée, les deux lignes d'ancre et les trois empreintes de fonction
  (§ 7, K2). Couples 2 à 6 à la lettre (§ 4, § 5, K4 et § 8, K1). **Le couple 7 tombe à bon droit** : il ne valait que pour une v5
  scellée avant la version qui cite le programme v4.
- **Devis, couples 1 à 3 : portés à la lettre** dans la v6 (§ 5, points 5 g, 6 et 5 k), et gardés dans la v7 ; le point 6 est mis à
  jour par la v7 (programme v4 cité, préalable « Rien ne part avant » gardé).
- Mineure 4 (essai court) faite : 1,58 × 2,3713 + 1,58 × 4,0990 = 10,2 USD, et 11,8 USD avec la fin de course : justes ; « plus du
  triple » de 3,1 USD : juste. Mineures 1, 3, 5, 7 non portées, comme le mandat le permettait : sans effet sur le scellement.

## 2. Rien n'a bougé hors ce qui est dit
- **Critère.** Mêmes seuils (10⁻³, 10⁻⁹, 10⁻⁶, 0,10) ; mêmes cinq libellés. Constantes du programme v4 égales à celles de la v3
  (tolérance, bornes, seuil, comptes, champs, cinq empreintes de référence, libellés) ; sept constantes neuves seulement (`CRITERE`,
  `PROGRAMME`, les deux empreintes de fichier d'ajustement pour l'arrêt sur une erreur, `ETAPE_EXPORT`, `HAUT_HORS_TABLE`,
  `NOEUD_ARRET`, la forme d'un identifiant de commit). Au § 5, les seules différences sont les couples 3 et 4 et les renvois « devis
  v7 ». Les treize différences du § 0.4 sont exactes, et je n'en ai pas trouvé d'autre.
- **Les contrôles passés dans le programme gardent leur conséquence** : « non comparable » à octets différents, suspension à octets
  égaux (W1 à W4, W6 à W8) ; pour K1, la mention signale le manqué et la règle de K1 (pas de verdict, comparaison refaite) reste ce
  qui décide : c'est écrit au § 4 et au § 7. Une pièce mal formée devient un préalable « forme » manqué (W4, W7) au lieu d'un arrêt :
  même verdict qu'en v5. `audit_requis` suit la liste des déclencheurs (W0 : faux ; W0b, W5 : vrai).
- **Devis.** § 3 identique ; seuls changent les couples, l'essai court et le marqueur, remplacé en v7 par le chemin et l'empreinte du
  critère v6 (`0700f3da…`, juste).

## 3. Les trois points posés par la session

1. **Étiquette « critère v5 » dans le programme : cela suffit, pas de programme v5.** Le libellé dit lui-même ce qu'il est (« critère
   … en vigueur (v5 à l'écriture du programme, 50657b89…) ») ; les règles que le programme calcule sont celles du § 4 de la v6, et ses
   constantes de décision sont celles de la v3, que la v5 et la v6 citent sans changement ; la v6 dit au § 7 que ce sont des
   étiquettes et que le verdict cite la v6 par chemin et empreinte. Un programme v5 changerait l'empreinte, donc les essais, le banc,
   une contre-lecture et une version du critère, pour aucune mention changée. À faire seulement si un autre défaut demande un
   programme neuf.
2. **Code de sortie 2 : il faut une règle, et elle manque aussi pour la sortie déjà présente.** Sondes W9 à W11 : ligne de commande
   refusée → code 2, aucune sortie, message « usage: » ; sortie déjà présente → code 1, aucune sortie, message « existe déjà » ; pièce
   absente → code 2, sortie écrite, `arret_sur_erreur` vrai, « non comparable ». Le § 4 distingue bien l'arrêt sur une erreur par le
   champ de la sortie, mais ne dit pas ce que valent les deux refus de démarrer : lus à la lettre, ils tombent dans le filet
   (« arrêt sans sortie » → « non comparable »), alors que rien n'a été comparé ; et le code 1 sans sortie est aussi celui d'une
   exception non rattrapée. Couple ci-dessous.
3. **Les défauts du programme listés à la fin du § 7 (sept, non cinq) : tous couverts sans changer une règle, sauf le 2, qui demande
   le couple.** 1, étiquettes : point 1. 3, « porte l'empreinte du 18 » vrai aussi pour l'empreinte de l'autre lentille ou d'une
   référence non vérifiée : la sortie est alors la suspension au lieu de « non comparable », même autorisation (aucune lecture sans
   nœud de Lazar), et le texte du § 4 décrit exactement ce que fait le programme. 4, lecture de secours qui ne rattrape que les
   erreurs de lecture et de valeur : le filet du § 4. 5, chemin et commit non confrontés à la course et à la branche : la part de K1
   à la main (tête de la branche distante après destruction), et les préalables « course neuve distincte » et « manifeste neuf porté
   par le résultat neuf », qui écartent une pièce d'une autre course. 6, pas de table des manifestes à l'arrêt : K5 à la main, écrit.
   7, aide de `--reprise` : K4 décide.

## Couple du critère (texte avant, texte après)

**Couple unique — les deux refus de démarrer (§ 4, fin du paragraphe « Arrêt du programme sur une erreur »).**
- Avant : « Dans les deux cas, le programme n'est pas relancé sur des pièces retouchées. Le premier cas se reconnaît au champ
  `arret_sur_erreur` de la sortie écrite, non au seul code de sortie : le code 2 est aussi celui d'une ligne de commande que le
  programme refuse, sans rien lire ni rien écrire. »
- Après : « Dans les deux cas, le programme n'est pas relancé sur des pièces retouchées. Le premier cas se reconnaît au champ
  `arret_sur_erreur` de la sortie écrite, non au seul code de sortie. **Deux refus de démarrer ne sont pas des comparaisons** : la
  ligne de commande refusée (code 2, message d'usage, aucune sortie) et la sortie déjà présente (code 1, message « existe déjà »,
  aucune sortie, la sortie présente n'étant ni lue ni remplacée). Ils ne rendent ni mention ni verdict et ne relèvent pas du filet :
  la ligne refusée et son message sont versés, la ligne est corrigée — pour le second, sous un nom de sortie neuf — et la comparaison
  est lancée ; si la sortie présente est celle d'une comparaison déjà faite, la relancer n'est permis que par les règles de K1 et
  de K4. Tout autre arrêt sans sortie relève du filet. »

## Remarques mineures (sans effet sur le scellement)
1. Devis v7 : le § 0, le § 11 et le § 12 parlent encore du critère « à porter » ; l'en-tête de la v7 le dit fait. Sans effet.
2. Programme, à la prochaine version s'il y en a une : nommer la v6 dans `CRITERE`, distinguer les codes de sortie (refus de démarrer,
   arrêt sur une erreur), et rattraper toute exception dans la lecture de secours.

## Ce qui a servi (hors dépôt)
Dossier `/tmp/claude-0/-home-user-controle-ia-travail/7344498a-9e3b-55a8-9388-941e130beae8/scratchpad/opus-contre-lecture-critere-v4/v6/` :
extraits des pièces au commit `9b6a35c1`, sondes et sortie (empreintes plus haut), comparaisons ligne à ligne v5 → v6 → v7 et des
constantes v3 → v4 faites par programme ; le texte « avant » du couple a été retrouvé une fois dans le critère v6, à l'espacement près.
