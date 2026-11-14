# Lecture adverse : billet P3 / P3-bis (version anglaise v1), fiche de faits v1, relecture du billet v2

## 1. En-tête

- **Lecteur** : sous-agent neuf, « modèle C ». Je n'ai écrit aucune des trois pièces.
- **Début** : 2026-11-14T11:34:02Z. **Fin** : 2026-11-14T11:37:35Z.
- **Empreintes vérifiées** (`sha256sum`, égales aux attendues) :
  - `verdict-P3-bis-v1.md` : `9b33c624…`
  - `verdict-P3-bis-v1-issue.json` : `c3a017ce…`
  - `verdict-P3-premier-test-i-a-v2.md` : `05e896da…`
  - `P3-bis-temoin-positif-v1.md` : `76ab66ce…`
- **Fichiers lus** :
  - Les trois pièces.
  - Le verdict de P3-bis en entier.
  - Le verdict de P3 : l. 1-45, 95-115, 171-222, 495-560.
  - Le texte scellé de P3-bis : l. 1137-1300, 1365-1398, 1420-1432, 1820-1898, 2641-2768.
  - Le texte scellé de P3 : l. 115-126, 286-300, 312-324.
  - `registres/decisions.md` : R-2299, R-2704, R-2711, R-2714, R-2715, R-2716, R-2718.
  - `registres/scellements-v1.md` : l. 10-15.
  - Le billet v2 en anglais, plus deux `Grep` ciblés sur la version française, la fiche et le journal du billet v2.

## 2. Verdict

**Prêt après corrections.** Aucun nombre n'est faux et les phrases gelées sont fidèlement traduites. Mais plusieurs réserves sont portées trop faiblement, une phrase de « Ce qui suit » dépasse les pièces, et la relecture classe « contredit » ce que le verdict interdit de lire ainsi.

## 3. Constats

**C-1 (majeur) — La réserve B3 est citée tronquée.**
- *Pièce et phrase visées* : billet, section « P3's null » : « Minimum detectable areas (80%): 0.6315 and 0.5966, against ≤ 0.5809 assumed in the plan; smaller areas are not excluded. »
- *Pièce qui fait foi* : verdict de P3, l. 523 et 525, et verdict de P3-bis, l. 109-110. La réserve gelée dit « au plancher et à la demi-largeur observés » et « grandeur calculée avant le scellement, sur des nombres déjà lus (brainstorm) ».
- *Manque dans le billet* : le billet omet les deux membres. L'avertissement sur la provenance du calcul disparaît, alors que la fiche le porte en F12.
- *Correction* : ajouter les deux membres, en une proposition.

**C-2 (majeur) — La réserve PB-4, déclenchée, n'est pas dite comme telle.**
- *Pièce et phrase visées* : « T 0.756 [0.441, 1.076] (about zero expected) » et, dans « Limits », « Verdict reservations: T's cost effect ».
- *Pièce qui fait foi* : verdict de P3-bis, l. 224, 227-229, 397, 411-412.
- *Écart* : c'est la seule réserve gelée déclenchée. Le texte « jumeau honnête » a relevé le coût déclaré sur 53 tâches (7 exclues), là où ≈ 0 était attendu. Le texte planté seul déplace donc le comportement, ce qui touche la lecture de A contre T. Le billet ne le dit pas.
- *Correction* : écrire que la réserve gelée PB-4 est déclenchée, avec le nombre, les 53 tâches et la conséquence. Le verdict (l. 491-494) laisse la portée à Lazar : le dire aussi.

**C-3 (majeur) — « this outcome opened a preregistered follow-up's probe scores » dépasse les pièces.**
- *Pièce et phrase visées* : billet, section « What comes next ».
- *Pièce qui fait foi* : texte scellé de P3-bis, l. 1247-1248 et 1888-1889 : « vu » seul ouvre ses scores ; l'ouverture pleine précède l'étape B. R-2704 ne lève que l'embargo de P3-bis.
- *Écart* : aucune pièce ne dit que les scores de T0.7 ont été ouverts ou lus. Le passé « opened » laisse croire qu'ils l'ont été, alors que la section `<<ETAPE_B>>` est vide.
- *Correction* : « By a rule fixed in advance, this outcome is the input that allows the preregistered follow-up reading (step B). »

**C-4 (majeur, forme) — Aucune marge de mots.**
- *Constat* : l'en-tête annonce 998 mots (975 alphanumériques) pour une limite de 1 000, avec les deux sections encore vides.
- *Contrôle* : `wc -w` sur le fichier entier donne 1 540. Je n'ai pas pu isoler le corps avec les seules commandes permises, donc je n'ai ni confirmé ni infirmé 998.
- *Conséquence* : le contenu des étapes B et B bis fera dépasser 1 000.
- *Correction* : tailler d'avance. Les candidats sont « Limits », les deux réserves de R-2299 et « Related work ». Fixer un budget de mots pour chaque section vide.

**C-5 (mineur) — Les réserves des addendums et de l'ouverture ne sont comptées que par nombre.**
- *Pièce et phrase visées* : « four on running the experiment; three on follow-up documents written after the closed reading, whose blindness rests on that closure ».
- *Pièce qui fait foi* : verdict de P3-bis, l. 427-434 et 443-445. La fiche demande « au moins une proposition chacune » (fiche, section 3, ligne « réserve omise »).
- *Correction* : nommer les quatre réserves : garde du crédit levée par écart ; dépense de téléchargement et fenêtre de contrôle ; relance après épisodes joués ; recharge automatique non tenue. Préciser que les trois écrits de l'ouverture ont été rédigés après la fermeture de la lecture.

**C-6 (mineur) — La réserve B1 est portée partiellement, avec une imprécision de nombre.**
- *Pièce et phrase visées* : « The saboteur's inflation (1.5227 [1.2464, 1.8012]) exceeded the instructed factor; its cause is not measured. » La question dit aussi « inflate … about threefold … did so ».
- *Pièce qui fait foi* : verdict de P3, l. 509-510. La réserve B1 repose sur la borne basse de `E_sf` (1,3211), « hors des cinq formes mesurées du champ du coût ». Les causes possibles sont : unité, échelle des propositions, gonflement.
- *Écart* : le billet rattache le dépassement à l'intervalle de P3-P1, qui n'est pas le nombre de B1. L'unité (log10) manque à cet endroit. « did so » contredit en apparence « exceeded ».
- *Correction* : citer la borne de `E_sf`, donner l'unité, lister les causes non mesurées, et écrire « inflated it by more than threefold ».

**C-7 (mineur) — Le résumé (TL;DR) est plus fort que le corps.**
- *Pièce et phrase visées* : « Two generic linear probes did not pick out… » ; « Fixed in advance: … »
- *Pièce qui fait foi* : le nul se lit « non détecté à cette puissance » (verdict de P3, l. 518). Le signal vu tient à la persona, à la forme ou à la longueur (verdict de P3-bis, l. 147).
- *Écarts* :
  - « at this power » manque pour le nul.
  - Le caveat principal est absent du résumé.
  - « Fixed in advance » est obscur pour un lecteur extérieur.
  - Le titre et le résumé annoncent « preregistered » pour l'étape B bis, dont le plan n'est pas encore scellé (R-2716, points 1 et 3). La variante « sans B bis » couvre ce cas : à n'utiliser que si le verdict de B bis est scellé à temps.
- *Correction* : ajouter « at this power » et la phrase persona / forme / longueur au résumé, et reformuler « Fixed in advance ».

**C-8 (mineur) — La réserve (1) de R-2299 est difficile à lire.**
- *Constat* : « the rule » n'est pas définie dans le billet, et « false-conclusion rate » ne dit pas de quelle conclusion il s'agit. Les bornes −0,0531 et −0,0694 ne sont pas identifiées comme bornes basses de la différence. La puce du nul écrit « floor quantile » au lieu de « 0.95 quantile of the floor ».
- *Pièce qui fait foi* : R-2299, l. 2257.
- *Correction* : définir la règle de P3 en une proposition (borne basse de l'intervalle de la sonde au-dessus du quantile 0,95 du plancher), puis préciser « 0.95 quantile » et la nature des bornes.
- *Point déjà noté par la fiche* : la suppression de « est celle de T0.7 » est déjà posée à Lazar (fiche, section 6, point 2). Cela reste un écart à « telles quelles » (R-2299).

**C-9 (mineur) — La question ouverte PB-10 est cryptique.**
- *Pièce et phrase visées* : « a localisation contrast expected near zero is 0.2399 […] (one area 0.9856, outside the untriggered "too good" audit) ».
- *Pièce qui fait foi* : verdict de P3-bis, l. 335-341 et 498-501 : T2 n'est pas l'un des dix jeux de l'audit R4.
- *Correction* : dire en clair que la répartition du signal sur l'action n'est pas celle attendue, et que l'aire 0,9856 sort du périmètre de l'audit « trop beau ». Sinon, couper la parenthèse.

**C-10 (mineur) — « planted-word mentions 0.5025 ».**
- *Constat* : le verdict parle de « mention étendue » (prédicteur par motifs), l. 240 et 253. Le mot « planted-word » est une glose du billet.
- *Correction* : écrire « mention-pattern predictor ».

**C-11 (mineur, décision de Lazar) — « AI agents (Claude models) ».**
- *Constat* : aucun identifiant de modèle n'est écrit. Le mot « Claude » seul est toléré, mais il nomme l'éditeur. La fiche pose déjà la question (section 6, point 7). Je le signale comme risque faible.
- *Remarque sur « no human redid the computation »* : le lecteur du verdict, un agent, a recalculé k et P de PB-2 et PB-9 par script (verdict de P3-bis, l. 149, 186-190). La phrase est donc exacte, mais à formuler « no human » et non « no one ».

**C-12 (mineur, fiche) — F01 : ligne citée fausse.**
- *Pièce et phrase visées* : « P3 l. 121 ».
- *Pièce qui fait foi* : dans le texte scellé de P3, Llama-3.1-8B-Instruct est cité à la l. 122 (la l. 121 est vide), et les couches 7, 15 et 23 le sont à la l. 291.
- *Correction* : citer l. 122 et l. 291.

**C-13 (majeur, fiche et relecture) — « contredit » est trop fort.**
- *Pièces et phrases visées* :
  - Fiche, section 3, ligne « la sonde lit la consigne, pas le sabotage » : « contredit, pour la sonde générique de P3-bis, par PB-5 ».
  - Relecture, ligne 30 : « contredit toute extension ».
  - Relecture, section 2 : « la phrase est contredite au sens suivant… ».
- *Pièce qui fait foi* : verdict de P3-bis, l. 159 et 480-481, et texte scellé, l. 1372-1373. PB-5 se lit « non détecté à cette puissance », jamais « ne sépare pas ».
- *Contradiction interne* : la relecture écrit elle-même, à la fin de la même section 2, que « le contraire n'est pas établi non plus », ce qui est exact. Avec la légende « contredit = une pièce va contre », le classement correct pour la sonde générique est « laisse ouvert ». PB-5 et PB-6 créent une tension, pas une contradiction. La conclusion de la relecture (n'écrire ni l'une ni l'autre forme) est juste, mais son classement ne la soutient pas.
- *Correction* : remplacer « contredit » par « laisse ouvert, en tension avec PB-5 et PB-6 ».
- *Autre ligne* : la ligne 12 (« confirme en principe ») porte sur une autre sonde, W. La classer « laisse ouvert ».

## 4. Ce qui tient

- **Nombres du billet** : tous recontrôlés contre les verdicts, arrondis compris. Aucun nombre faux ni mal arrondi.
  - A contre T : 0,8012 ; 0,6496 ; D 0,1516 [0,1178 ; 0,1821].
  - A contre B : 0,8297. B contre H : 0,5160, D [−0,0819 ; −0,0193]. T contre H : 0,5475.
  - Épisodes : 48 sur 60 et 4 sur 60.
  - Coûts : A, B et T.
  - Nul de P3 : aires, intervalles, quantiles.
  - Bornes −0,0531 et −0,0694.
  - Aires minimales détectables : 0,6315 et 0,5966 (0,6376 et 0,6025 sous une règle qui tient son niveau ; 0,6456 et 0,6125 avec la distance basse).
  - 0,8743 ; 0,7702 ; 0,2399 ; 0,9856 ; 0,6172.
- **Phrases gelées** : PB-5, PB-6, PB-2 et la portée gelée sont fidèlement traduites, sans omission qui change le sens.
- **Règles de fond** : aucune explication du nul de P3, rien de plus que « vu ». « Non au-dessus » lu « non détecté à cette puissance ». Un seul modèle, une seule taille. La consigne visible n'est pas détectée à cette puissance.
- **Faits de procédure** : tentative 1 au lot 19 sur 30 et détruite sans lecture ; scellement le 11 novembre ; run le 13 novembre ; trois addendums ; lecteur d'un autre modèle que les auteurs.
- **Interdits de contenu** : absents du billet. Pas d'identifiant de modèle, pas de texte de scénario ou de consigne, pas de bras d'attaque, de mode tenu à l'écart, de « TASTE » ou de contenu de T0.7 au-delà du texte scellé, pas de primauté.
- **Forme** : les sections demandées sont là, avec les deux marqueurs et la variante de titre et de résumé.
- **Fiche, faits contrôlés** : 22 faits, dont F01 à F06, F08 à F12, F16, F20, F28, F31, F35, F37, F40, F42, F46, F53, F56 et F62.
  - Les nombres et les lignes tiennent, sauf F01 (C-12).
  - Les lignes du registre R-2299, R-2704 et R-2711 à R-2716 se retrouvent.
  - Chaque fait a un chemin, une clé d'empreinte et une ligne.
- **Fiche, section « ce qu'il ne faut pas dire »** : couvre les six éléments exigés, et plus. Les réserves sont listées en entier dans la section 4 de la fiche.
- **Relecture, pièce 3** :
  - Les renvois de ligne au billet v2 (l. 7, 11, 13, 15, 19-23, 29-36, 38, 44, 48, 52, 54, 58) sont justes.
  - Les lignes de P3-bis citées sont justes.
  - L'observation que BF2 nomme deux modèles est confirmée (Grep sur la version française, l. 48).
  - La conclusion (le résultat de W reste hors du billet) suit.

## 5. Limites de ma lecture

- Je n'ai pas pu isoler le corps du billet pour un `wc -w`. Le chiffre de 998 mots n'est ni confirmé ni infirmé.
- Je n'ai pas lu les pages publiques de P3 et de R1, ni les PDF des travaux cités, ni les fichiers de données. Je n'ai donc pas contrôlé :
  - les pages et citations de la section 5 de la fiche ;
  - les mentions de PUB-P3 et PUB-R1 ;
  - les nombres de Mohsin et Rahman et de « Telling FIBS ».
- Je n'ai pas lu les lignes 1400-1401 du texte scellé (citées pour la température dans la relecture), ni les autres passages du texte scellé. Je n'ai pas non plus lu le rapport d'audit de R-2299, qui est hors liste ; les nombres de R-2299 viennent de la ligne de registre et du texte scellé.
- Je n'ai contrôlé par empreinte que les quatre pièces qui font foi listées en méthode A, pas les autres empreintes de la fiche (registres vivants compris).
- Je n'ai ouvert aucun fichier interdit. Je n'ai lancé que `date -u`, `sha256sum` et `wc`.
