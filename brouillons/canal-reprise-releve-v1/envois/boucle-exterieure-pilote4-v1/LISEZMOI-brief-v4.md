# Brief v4 — boucle extérieure du pilote 4 : corrections après la vérification de la v3

De : conv-audit, le 2026-10-26 à 05:43:40 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).
À : l'auteur de la v3 (toi, relancé). Ce brief s'ajoute aux briefs v1 à v3, qui restent valables sauf ce qu'il change.

## 1. Ce qui est demandé

Écrire, dans `sortie/` seulement :

- `registre-hypotheses-conception-pilote4-v4.md` ;
- `protocole-boucle-exterieure-pilote4-v3.md` ;
- `brief-agents-fin-de-course-v3.md` ;
- `specification-releve-mecanique-B-v2.md` ;
- `LISEZMOI-sortie-v4.md`, avec une table « v3 → v4 » : pour chaque constat CLB3-01 à CLB3-08 et chaque décision D1 à D7
  ci-dessous, où c'est traité (fichier, section, lignes) et ce qui reste ;
- le compagnon `.sha256` de chacun (« empreinte, deux espaces, nom nu »).

Rien ne change hors de ce que demandent ces constats et ces décisions ; tout autre changement est déclaré, avec sa raison.
Vise environ une heure. Aucun nombre à recalculer, sauf si une correction l'exige (alors sans aucun score).

## 2. Pièces

Dans `fournis/`, à vérifier contre `../EMPREINTES-fournis-v1.txt` avant lecture :

- `rapport-verification-boucle-exterieure-v3.md` (`1a7873e2…`) : la vérification de ta v3 ; verdict « utilisable après
  corrections » ; constats CLB3-01 à CLB3-08. **À lire en entier.**
- `points-boucle-exterieure-pilote4-pour-lazar-v1.md` (`ac105262…`) : les points pour Lazar au format de décision, écrits
  par conv-audit (D4).
- `extrait-lignes-ecrites-au-LANCEMENT-par-les-lanceurs-v10-v11-v1.txt` : les lignes « - … » que les lanceurs v10
  (course M) et v11 (course S) écrivent au `LANCEMENT.md` d'une course ; c'est du code, pas des données de course (D5).
- Tes pièces v3 et leurs compagnons (registre v3, protocole v2, briefs v2, spécification (B) v1, LISEZMOI v3), le texte
  v5 du pilote (`1943f39a…`, qui prime), le LISEZMOI du script de lecture v2 (`2f328fee…`), mon brief v3.

Tu peux relire les pièces de ton dossier v3 (`/var/tmp/boucle-exterieure-pilote4-v3/fournis/`). Rien d'autre.

## 3. Décisions de conv-audit, à appliquer telles quelles

### D1 — CLB3-01 et CLB3-06 : la lecture de `test_final`, et le script de lecture v3

- Le script de lecture passe en **v3** (écrit par son auteur, relu avant usage). Les quatre pièces décrivent ses sorties
  telles quelles :
  - à la fin de chaque course : `lecture-<dossier>-test-v<n>.{json,md}`, la part `test` seule ;
  - à la fin de la course S, pour chacune des deux courses : `lecture-<dossier>-test-final-holm-quatre-v<n>.{json,md}`,
    une course, Holm sur les quatre tests (deux par course), **aucune valeur de l'autre course** (ni compte, ni
    proportion, ni valeur p, ni libellé) ;
  - si la course S ne court pas ou ne finit pas saine : `lecture-<dossier de M>-test-final-holm-deux-v<n>.{json,md}`
    (option `--sans-seconde-course`) ;
  - **plus aucun fichier « provisoire »** : un fichier dont le nom porte `-provisoire-` (sortie de la v2) n'entre jamais
    dans un dossier de lecture ; une garde le refuse à l'assemblage, essayée sur un cas sain et sur cet artefact (R5) ;
  - `<n>` ≥ 3 est la version du script, écrite au manifeste du dossier ; `<dossier>` est le nom réel du dossier de la
    course : `pilote4-gemini-v6-2-v1-tentative2` pour M, `pilote4-gemini-v6-2-s-v1` pour S.
- La séparation entre courses est gardée par le script lui-même : son essai « séparation » vérifie, sur données
  synthétiques, que l'union des deux fichiers « holm-quatre » rend les lignes (iii) du calcul joint, et qu'aucune valeur
  d'une course n'apparaît dans le fichier de l'autre (artefact : une valeur de l'autre course plantée, refusée).
  Session-depot l'exécute sans en afficher la sortie.
- **G8 bis** réécrite comme le dit CLB3-01 (c) : sur données synthétiques, l'essai « séparation » du script ; à
  l'assemblage d'un dossier de course, contrôle du seul fichier `test` réel (ni le mot `test_final`, ni (iii), ni valeur
  p, ni mention d'essai), sans jamais ouvrir un fichier `test_final` réel avant la fin du compteur.
- Toute mention du script v1 comme sortie réelle (« une seule sortie », « le fichier actuel porte les deux parts ») est
  mise à jour : ni la v1 ni la v2 ne s'exécutent sur les courses (message n° 79 de conv-audit à session-depot).
- **Libellés** (CLB3-06 a) : la v3 du script ajoute, pour chaque test (iii), le **sens du rejet** (génération 3 au-dessus
  ou au-dessous de la génération 0), et, par cellule de `test_final`, **« aucune tâche sans réponse »** (oui ou non).
  Conv-audit juge le sens couvert par le point 4 bis : le verdict d'un test bilatéral porte son sens. HC-P4-08 sur
  `test_final` et le sens de HC-P4-11 et 12 sont observables avec un script de version 3 ou plus, « non observables »
  sinon.
- CLB3-06 (b) : les faits mécaniques se citent depuis le relevé (B) seul, jamais depuis le fichier `test`, qui en porte
  aussi.
- CLB3-06 (c) : le libellé de la délégation sur `test` est, mot pour mot, « impossible par construction (référence égale
  à 1) » ; les briefs le citent ainsi.
- CLB3-07 (b) : la ligne d'état du script v3 ne compte que les signalements de `test` (« signalements de test : N »).

### D2 — CLB3-02 : règle de préséance, écrite avant toute lecture

- **« La course M motive la correction de la ronde 1 ; la course S ne la motive que si aucune fiche de M n'en motive ;
  les verdicts de S sont rapportés à part, jamais mis en regard de ceux de M. »** Cette règle remplace tes choix 1, 3
  et 4 de la v3.
- La correction se propose après la lecture de M ; le correcteur n'attend la course S que si M ne motive rien.
- Retirer de chaque fiche la branche « verdicts différents selon la course ». Aucune pièce (correction, partie B,
  journal) ne met côte à côte les verdicts des deux courses. La pièce de correction cite les fiches de la seule course qui
  la motive ; les verdicts de l'autre course vont dans une pièce à part, sans renvoi croisé ligne à ligne. La condition
  « aucune fiche de M ne motive » est un fait sur M seule ; l'écrire comme tel.
- Corriger la raison donnée (remarque de CLB3-02) : avant la génération 1, M et S ne diffèrent que par la graine (la
  question n'est servie qu'à g001) ; après, par la question aussi. La règle tient dans les deux cas.
- « Correction après M sans attendre S » sort des points pour Lazar (point 5 de la pièce des points : une information).

### D3 — CLB3-03 : HC-P4-01

- La voie « `conception.rondes_tournees` quand la déclaration manque » est marquée « écrite après la lecture de faits
  mécaniques de la course M (brouillon du texte v5, § Ce qui a été lu) ». **Elle ne s'applique ni à M ni à S.** C'est
  plus strict que la vérification : la course S tourne le même objet sur les mêmes tâches, et avant g001 elle ne diffère
  de M que par la graine ; le fait lu de M renseigne donc aussi sur S. Pour M et S : la règle de la v2 (ronde de la
  déclaration exigée, sinon « non observable »).
- Pour une course où cette voie s'applique (une relance lancée après la poussée du registre v4) : exiger en plus que
  chaque unité de conception porte `statut = ok`, sans `delai_depasse` ni refus `plafond`, et que g000 ait tourné ;
  sinon « non observable ».
- Au registre (§ Écrit avant tout score), déclarer l'origine : des faits mécaniques de M, pas des scores, que conv-audit
  a laissés dans le brouillon qu'il t'a fourni ; l'erreur est celle de conv-audit, pas la tienne.

### D4 — CLB3-04 : points pour Lazar

- La pièce `points-boucle-exterieure-pilote4-pour-lazar-v1.md` pose les points au format de décision. Le protocole la cite
  au lieu de les reposer, et met à jour son § 16 (qui tranche, état, défaut, moment).
- Point 1 (famille du contre-lecteur) : défaut (a), même famille, 48 heures après son envoi à Lazar (fait le 26 octobre
  vers 05:42 UTC ; l'heure exacte est au journal de conv-audit). D'ici sa réponse ou l'échéance, aucune proposition ne
  sort d'une ronde. Le § 12.3 l'écrit (il disait « aucune valeur par défaut ») ; la valeur reste écrite à chaque entrée
  du journal.
- Points 3 (plafond) et 6 (question servie par une relance) : sans défaut (dépenses) ; posés au premier devis de relance
  et au GO de la relance. Point 4 (symétrie avant (b)) : défaut (a). Point 7 (seuils 0,01 et 0,03) : défaut (a), garder ;
  tout changement attend le mot de Lazar ; les deux seuils comptent pour un seul facteur (ton choix 23, confirmé).
- Point 2 (graines) : renvoi à la décision posée à part.
- Le § 4 du protocole, qui écrivait « aucun défaut » puis en donnait un (l. 168–170), est réécrit par D2.

### D5 — CLB3-05 : relevé (B)

- **Faits** (extrait fourni) : les deux lanceurs écrivent au `LANCEMENT.md` la ligne « - organisme : N fichiers,
  empreinte d'arbre … ; question (<COURSE>) : sha256 … » (v10 l. 528 ; v11 l. 545), la ligne « - lanceur : <nom>, sha256
  … » et la ligne « - préenregistrement : …, graine <GRAINE> de la course <COURSE> … » (numéros de ligne dans l'extrait).
  Seul le v11 écrit les lignes de la porte « course v6.2 précédente » (l. 379 et 527).
- `identite.question` se déduit de l'empreinte de la question :
  `8b1c751174b3d24dc0d861873a2758d3b780ab9a878e83e591835849db1a7acd` → `m` ;
  `a54da93ee892d920c31ba47327c2400e25ccf42ff06faa46d94bfc471a5a6289` → `s` ; toute autre empreinte, ou l'absence de la
  ligne → écart (arrêt).
- **Champs d'identité exigés** (absence = écart, arrêt) : nom et lignée de la course, graine, empreinte d'arbre et nombre
  de fichiers de l'organisme, empreinte de la question, nom et empreinte du lanceur, commit du segment 1. **Champs qui
  peuvent porter `absent`, rapportés sans arrêt** : ceux qu'un seul des deux lanceurs écrit (porte « course M
  précédente » : absente pour M par construction), et les champs hors identité que la spécification v1 marque déjà
  ainsi.
- **Cas sain de la série v14** (batterie v13 sur le lanceur v11) : une course S simulée après une course M saine simulée ;
  `identite.question = s`, `unite.g001.question_servie = oui`, rien de la course M recopié dans le relevé de S. Les cas
  sains de la série v13 restent, pour la forme du lanceur v10.
- **Tableau d'identité** (protocole, l. 289), ligne S : nom `pilote4-gemini-v6-2-s-v1` ; dossier réel
  `essaim-m3-refonte-v1/pilotes/pilote4-gemini-v6-2-s-v1` de la copie de lancement, sans suffixe de tentative (R-497) ;
  lignée `gemini-organisme-v6-2-s` ; graine 6967892196853497016 ; texte v5
  `1943f39ada61db7d21e53b7e0c02c6e826b86e1467687eedbe56617877ab7f87` ; lanceur v11 `lancer_pilote4_gemini_v11.sh`,
  `21854b794de90d874b23def1685e306ceba80b32cd471de1dd8cf750ad01d0d7` ; organisme v6.2.1, commit
  `7ea32705c5437d91ed071dd95fb3209bb0b0035e`, arbre `4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d`,
  26 fichiers ; question S `a54da93e…` (commit `4772b525081342a6a30ba8823733aa5770a888a8`).

### D6 — CLB3-07 (a)

Le protocole (l. 85) écrit : « qu'il a exécuté le script, sans en afficher la sortie ».

### D7 — CLB3-08

(a) à (d) comme le dit le rapport. Pour (d), écrire la commande exacte, chemins complets par variables nommées, et le
préfixe de chemin que G5 attend.

## 4. Réponses à tes points pour conv-audit (LISEZMOI v3, § 5)

1. Ta v2 : commit `e0a739e` à 04:00:00 UTC, avant la fin de la course M (04:44:47 UTC) ; heure de poussée non consignée.
   Ta v3 : commit `07c7407` à 04:52:02 UTC, après la fin de M, avant toute lecture (retenue). Les deux sont poussées.
2. Contre-lecture de la v3 : faite (rapport fourni). La v4 sera vérifiée par le même vérificateur, avec ta table.
3. Script du relevé (B) : écrit par un sous-agent de conv-audit sur ta spécification v2, essayé sur les séries v13 et
   v14 ; exécuté sur les courses réelles par session-depot, sans affichage (confirmé).
4. Script de lecture v3 : demandé (D1).
5. Sens du rejet : couvert par le point 4 bis (D1).
6. Carte des facteurs et zones interdites : écrites pour conv-audit avant la première correction ; deux seuils, un seul
   facteur (D4).
7. Auteurs des gardes G1 à G11, des dossiers d'audit, du script de forge et de l'étalonnage à blanc : un sous-agent de
   conv-audit, après la vérification de ta v4 ; essayés avant la première lecture.
8. Identité de S : D5.
9. Choix 1 à 4 : remplacés par D2.
10. Forme du texte d'une relance et des noms : fixée au premier devis de relance, dans un texte nouveau, avant toute
    lecture de son `test` ; le protocole le dit sans fixer la forme maintenant.
11. Seuils : point 7 de la pièce des points.
12. Inchangé : si un texte nouveau (graines) change la règle de lecture, un registre v5 avant la première lecture.

## 5. Interdits (inchangés)

Rien hors de `fournis/`, de ton dossier v3 et de ce brief ; aucun score ; aucun fait de course de plus que ceux que tu as
déjà lus ; aucun `git`, réseau, sous-agent ni clé ; écrire seulement dans `sortie/` ; heures lues sur `date -u` dans la
commande qui les écrit, jamais écrites d'avance ; aucun critère ni aucune stratégie de classement des tâches ; rien de
ce dossier n'est servi à un organisme. Python, s'il le faut, en mode isolé (`-I`), sans écrire de fichier.

## 6. Fin

Ta réponse finale tient en quelques lignes : verdict sur ce qui est fait, ce qui reste, écarts déclarés, empreintes des
cinq pièces.
