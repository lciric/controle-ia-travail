# Brief v5 — boucle extérieure du pilote 4 : corrections après la vérification de la v4

De : conv-audit, le 2026-10-26 à 06:47:27 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).
À : l'auteur des v3 et v4 (toi, relancé). Les briefs v1 à v4 restent valables sauf ce que celui-ci change.

## 1. Ce qui est demandé

Écrire, dans `sortie/` seulement : `registre-hypotheses-conception-pilote4-v5.md`, `protocole-boucle-exterieure-pilote4-v4.md`,
`brief-agents-fin-de-course-v4.md`, `specification-releve-mecanique-B-v3.md`, `LISEZMOI-sortie-v5.md` (table
« v4 → v5 » par constat CLB4-01 à CLB4-07 et par décision E1 à E8 : où, et ce qui reste), chacun avec son compagnon.
Rien ne change hors de ce que demandent ces constats et ces décisions ; tout autre changement est déclaré. Vise moins
d'une heure : ce sont des corrections courtes.

## 2. Pièces

Dans `fournis/`, à vérifier contre `../EMPREINTES-fournis-v1.txt` : ta v4 (cinq fichiers et compagnons) ; la vérification
de la v4 (`rapport-verification-boucle-exterieure-v4.md`, `b518f24c…`, **à lire en entier**) ; la carte des facteurs et
les zones interdites v1 (`carte-facteurs-v1.md` et `.json`, `zones-interdites-v1.md` et `.json`, leur LISEZMOI), écrites
par un sous-agent neuf depuis le code, en contre-lecture à part ; le brief du script de lecture v3 (`78861f99…`).

## 3. Décisions de conv-audit, à appliquer telles quelles

- **E1 — CLB4-01 (nom et lignée au relevé)** : `releve.course` se lit sur la ligne « - course : <COURSE> ; dossier du
  pilote : <chemin> … » : le nom est le dernier élément du chemin, privé d'un suffixe `-tentative<N>`, et il doit égaler
  celui que la clé donne dans une table close de deux lignes, citée des textes du pilote (`v6-2` →
  `pilote4-gemini-v6-2-v1` ; `v6-2-s` → `pilote4-gemini-v6-2-s-v1`) ; la clé doit être la même sur les trois lignes qui
  la portent (course, préenregistrement, organisme et question) ; sinon refus. `identite.lignee` : recopiée de l'extrait
  si l'extrait la porte sous un champ hors de la liste noire, et alors égale à celle de la table (`v6-2` →
  `gemini-organisme-v6-2` ; `v6-2-s` → `gemini-organisme-v6-2-s`), sinon refus ; si l'extrait ne la porte pas, prise dans
  la table, et le relevé le dit (« déduite de la clé : contrôle non indépendant »). Au § 8 de la spécification : l'auteur
  du script confirme sur les séries v13 et v14 que chaque ligne qui porte un champ exigé est écrite en simulation.
- **E2 — CLB4-02 (libellé (iii))** : le script v3 écrit les mots du point 4 bis, comme la v2 : « changement au-delà du
  bruit des tâches » si le test est rejeté, sinon « dans le bruit des tâches » ; la correction de multiplicité dans un
  champ à part (« correction : Holm, quatre tests, niveau 0,05 », ou « deux tests » dans un fichier « holm-deux ») ; le
  sens seulement si le libellé est « changement au-delà du bruit des tâches », sinon « sans objet (non rejeté) ». Au
  registre : libellé « changement au-delà du bruit des tâches » → verdict du même nom ; libellé « dans le bruit des
  tâches » → verdict « non rejetée (bruit) » ; tout autre libellé → l'analyste s'arrête et le signale. Réécrire la
  l. 581 sur ces deux libellés.
- **E3 — CLB4-03** : aligner sur le brief du script : ligne d'état « signalements (fichier test) : N » ; un fichier
  « holm-quatre » ne porte, de l'autre course, ni compte, ni proportion, ni borne, ni valeur p, ni libellé, ni
  signalement, et jamais de valeur p ajustée, de rang ni de seuil appliqué ; l'étape 1 de l'analyste final le vérifie et
  s'arrête sinon.
- **E4 — CLB4-04** : comme le dit le rapport : la section 3A décrit le contre-lecteur à l'aveugle de la lecture finale ;
  une entrée finale du journal par course, puis une entrée de clôture sans verdict ; une transmission à Lazar par course.
- **E5 — CLB4-05** : le registre garde la déclaration sans les faits : « des faits mécaniques de la course M, aucun
  score (détail au LISEZMOI de la v3, servi à aucun agent) ».
- **E6 — CLB4-06** : `unite.g001.question_servie` vaut `oui` seulement si la ligne qui commence par « - réponse à la
  question : » ne porte pas « aucune pièce archivée » ; avec ces mots, `absent` ; jamais `non` déduit de cette ligne. La
  ligne se reconnaît par ce début seulement : le script ne contient nulle part la chaîne du nom du fichier de réponse.
- **E7 — CLB4-07** : (a) « deux messages » ; (b) le paramètre « famille » prend trois valeurs, celles du point 1 ((a),
  (b), (c)) ; (c) le registre cite la phrase (iv) telle que la fixe le brief du script (« … aucune comparaison entre les
  deux courses n'est faite … ») ; (d) G6 cherche des mots entiers.
- **E8 — carte des facteurs** (points D1, D2 et D7 de son LISEZMOI) : G5 lit la carte au niveau des colonnes, par
  segments, comme la carte le propose (§ 5 de la carte) ; le repli par lignes entières n'est pas pris. Le gel de
  `seuil_confiance_caste1` (zone Z03) est confirmé : c'est un seuil du routage de la règle de classe. `VERSION`
  (`principal.py` l. 27) entre dans la liste close des fichiers d'accompagnement (§ 6), comme le champ de version de
  `manifeste.json`. Le protocole cite la carte et les zones par nom et empreinte (`carte-facteurs-v1.json`
  `2aaedd08…`, `zones-interdites-v1.json` `0082519c…`), « v1, sous réserve de leur contre-lecture », et dit que les
  seuils 0,01 et 0,03 et leurs copies (F05, F06, F13, F14) restent gelés par le point 7 de la pièce des points.

## 4. Interdits (inchangés)

Rien hors de `fournis/` et de ce brief ; aucun score ; aucun fait de course de plus ; aucun `git`, réseau, sous-agent ni
clé ; écrire seulement dans `sortie/` ; heures lues sur `date -u` dans la commande qui les écrit ; aucun critère ni
aucune stratégie de classement des tâches ; rien n'est servi à un organisme ; Python avec `-I`, sans écrire de fichier.

## 5. Fin

Réponse finale en quelques lignes : ce qui est fait, ce qui reste, écarts déclarés, empreintes.
