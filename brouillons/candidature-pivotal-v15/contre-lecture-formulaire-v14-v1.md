**envoyable après remplacements (couples exacts ci-dessous)**

# Contre-lecture du formulaire Pivotal v14 — v1

- Lecteur neuf (n'a écrit aucun des textes relus), 2 novembre 2026, 06:50–07:00 UTC. Lecture seule : rien relancé ; seulement l'extraction du texte du PDF et des comptes de mots et de caractères, sous `nice -n 10`, sans fichier intermédiaire.
- **État relu, figé par empreintes, stable depuis 06:53:45 UTC (revérifié à 06:56 UTC)** : `reponses-formulaire-v14.md` sha256 `695d5b9ace2b2ea08a2919e4a9ed175542e8bd54c4f2d863c440fbd830093206` ; `Lazar_Ciric_career_memo_2026-11-02_v2.pdf` sha256 `7175910011d0629f3275fc36111a6a7c0719979a4840ef7eb7e29b022e7c3fbb` ; `mentors-v10/mentor-2-kirchner-v10.md` sha256 `88fee1e69d9b3f58109b2dbc5492c715de5dac6ac9a89e5d8547d36aea9ac413`, identique dans les paquets v14 et v15.
- **Le paquet a changé pendant la relecture.** À 06:53:44 UTC, `reponses-formulaire-v14.md` a été réécrit sous le même nom. L'en-tête « 06:50 UTC » est devenu « 06:48 UTC, completed 06:53 UTC ». Une phrase sur Llama-3.1-8B a été ajoutée au § 10, et le § 9 renvoie maintenant au CV v14. Le PDF nommé dans la consigne (`…_v1.pdf`) n'est plus dans le dossier ; il est remplacé par `…_v2.pdf`. J'ai relu l'état actuel. Écart à R12 (« on n'écrase jamais ») : la première v14 n'existe plus sous ce nom. Je n'ai pas cherché d'archive ailleurs. La phrase « 288 » relue au point B est la même dans les deux états.

## Remplacements (couples exacts)

1. **Obligatoire — mémo, § 10 de `reponses-formulaire-v14.md`** (131 → 130 caractères, 26 → 24 mots) :
   - remplacer : `on 288 real model episodes, read once under a sealed plan, it found the 3 planted links, none of 19 null controls, and no real link`
   - par : `on 288 real model episodes, read once as preregistered, it promoted the 3 planted links, none of 19 null controls, and no real law`
2. **Obligatoire, conséquence du 1** : régénérer le PDF depuis le § 10 corrigé, sous un nom neuf (R12), `Lazar_Ciric_career_memo_2026-11-02_v3.pdf`. Il reste sur une page : le texte est plus court d'un caractère et il reste environ 101 mm libres en bas de page. Puis, au § 9 :
   - remplacer : `Lazar_Ciric_career_memo_2026-11-02_v2.pdf`
   - par : `Lazar_Ciric_career_memo_2026-11-02_v3.pdf`
3. **Obligatoire — réponse à Kirchner** (`mentor-2-kirchner-v10.md`, 114 → 114 caractères, 19 → 17 mots) :
   - remplacer : `a planted-form link carrying more than roughly 0.06–0.12 nats per episode would have been caught nine times in ten`
   - par : `its rough per-monitor 90%-power threshold for planted-form links is 0.06–0.12 nats per episode, not a proven bound`
4. **Conditionnel — phrase Llama-3.1-8B du § 10.** Elle a été ajoutée à 06:53 UTC. Aucune des sources de ma liste ne la couvre : 27 %, 1 %, « bounded null », « cost-inflating saboteur » et « weaker instruction » ne sont pas vérifiés par moi. Il faut la faire contre-lire contre ses verdicts avant envoi. Sinon, revenir à la formule de v13 (puis refaire le PDF, point 2) :
   - remplacer : `and first tests on Llama-3.1-8B: generic probes miss a cost-inflating saboteur (a bounded null), and under a weaker instruction the best per-action black-box monitor catches 27% of its actions at 1% false alarms.`
   - par : `and a first test on real activations whose null result is bounded.`
   - Questions pour qui la contre-lira : « the best » monitor a-t-il été choisi avant ou après avoir vu les données (si après, 27 % est optimiste) ? Le verdict de la passe de dose permet-il « catches 27 % » sans intervalle ?
5. **Facultatif — Kirchner, même paragraphe** (« works » résume large ; le verdict ne permet pas de dire que le juge a des dents sur des liens réels) :
   - remplacer : `showed that the judge works on real traces`
   - par : `tested the judge on real traces`

À faire au moment de coller, hors texte : saisir les deux adresses des répondants (§ 8 : encore `[your entry: his email]`). Téléverser le CV v14, qui est dans le sous-dossier `cv-v14/` ; la racine du paquet ne contient que les CV v13. Je n'ai pas relu le contenu des CV v14, qui ne sont pas dans ma liste.

## A. Différentiel v13 → v14 (état actuel)

Méthode : découpage par section et comparaison mot à mot (Python `difflib`), plus `diff` ligne à ligne.

- **§ 1 à § 6 : titres et corps identiques à l'octet.** § 7 : corps identique, titre allégé de « — kept (your go of 1 November, 23:50) » (annoncé).
- Annoncé et conforme : § 8, répondants inchangés (Ostojic, Le Gallo) et note « DECISION FOR LAZAR » retirée ; § 9, extrait d'écriture inchangé (même PDF, sha256 `0d0e549a…` dans v14 et v15) et note retirée ; titre du § 10 ; ligne du mémo PDF au § 9 (maintenant v2) ; proposition « 288 » ajoutée au § 10.
- **Absent de la consigne, mais annoncé par l'en-tête actuel :**
  1. § 10 : la dernière phrase de « What I have » est remplacée (« a first test on real activations whose null result is bounded » devient la phrase Llama-3.1-8B, 27 % à 1 % de fausses alertes). C'est une revendication de fond nouvelle ; voir le remplacement 4.
  2. § 9 : le CV passe de v13 à `Lazar_Ciric_CV_2026-11-02_v14_universel.pdf` (présent dans `cv-v14/`, avec les trois variantes).
- **Changements non annoncés, tous sans effet sur le fond :**
  3. § 10 : la phrase des tricheurs est recoupée. « caught); I attacked » devient « caught). I attacked ». « and closed them, with a preregistered validation at 1,000 repetitions. » devient « and closed them (preregistered validation, 1,000 repetitions); ».
  4. § 9, ligne de l'extrait d'écriture : la mention interne « the dangling final sentence removed and funder-specific wording edited out » est retirée (le PDF est inchangé).
  5. § 8 : l'emplacement d'adresse passe de `[to fill]` à `[your entry: his email]` (deux fois). C'est toujours un emplacement à remplir.
  6. L'en-tête dit « Sections 1 to 7 are unchanged from v13 » alors que le titre du § 7 a changé (note interne seulement). L'historique de v13 est remplacé par un renvoi.

## B. La phrase ajoutée au mémo

Sources : ligne « Fresh-seed reading of the real bank » du tableau des preuves du README ; verdict R13, sections 2, 3 et 4.

| élément | constat |
|---|---|
| 288 | conforme : README « 288 episodes » ; verdict « 288 épisodes (96 tâches : 30/30/30/6) » |
| 3 planted links | conforme sous le plan plein, qui est la configuration décisive pour les dents (L3′ planté, T-plein : TVP01 à TVP03). Avec le plan gelé de 120, c'est 2 sur 3 |
| none of 19 null controls | conforme : « 0 of 19 false witnesses » (13 réels et 6 plantés, m = 19), dans les quatre configurations |
| read once | conforme au README (« run once »). Le verdict l'établit par les traces, pas par une mesure (réserve 3) |
| under a sealed plan | vrai (préenregistrement scellé à 22:15 UTC, premier résultat à 22:37 UTC). Mais « plan » est le mot technique du README : avec « the frozen plan of 120 », le résultat est 2 sur 3. Un lecteur qui recoupe peut croire que le mémo trie le chiffre favorable |
| real model episodes | acceptable : épisodes réels d'un modèle de 8 milliards de paramètres, notes réelles neuves (« Permet de dire »). La portée (mêmes 96 tâches que le calibrage) n'est pas dite, mais le README lié la donne |
| no real link | **dit plus que le verdict.** Avec le verbe « found », « it found … no real link » se lit comme un constat d'absence. Juste après « found the 3 planted links », la phrase suggère que des liens réels auraient été vus. Le verdict ne permet de dire que « aucune loi réelle promue » (les 13 lois connues, des traits de l'épisode vers la note) ; il exclut « qu'aucune dépendance n'existe » et « que le juge a des dents sur des liens réels » |

« 3 sur 3 » et réserve 6 : le mémo ne parle ni de force ni de puissance. Il rapporte un compte que le verdict permet (« a détecté … et aussi celle de force 0,3 »), donc ce n'est pas une présentation comme puissance. Le risque venait du voisinage avec « no real link » et du mot « plan ». Le remplacement 1 traite les deux : le verbe « promoted » est celui du README et de la réponse à Kirchner, « no real law » reprend « aucune loi réelle promue », et « as preregistered » remplace « under a sealed plan ». Rien ne reste qui dépasse le verdict. Le seul défaut restant est de style : « preregistered » revient deux fois dans la phrase.

## C. Autres chiffres du mémo, confrontés au README

- **929 tests** : conforme. README : « 906 passed, 8 failed, 15 skipped … (929 tests) », soit 906 + 8 + 15 = 929. Le mémo ne dit pas « passed », donc c'est littéralement exact. Les 8 échecs sont des contrôles de provenance ou d'environnement, déclarés dans le README.
- **224 of 224 code mutations caught** : conforme (156 + 19 + 15 + 34 = 224, chacune tuée pour la raison attendue, 0 survivante).
- **27 scripted cheaters** : conforme à la ligne « Statistical judge attacked by 27 scripted cheaters ».
- **four that got through, … closed them** : conforme au § 3.1. T02, T03b, T04 et T05s passent à 75 %, 85 %, 95 % et 80,5 % sous le nul simple. Sous le nul mis en commun, c'est 0 sur 200, puis 0 sur 1 000 dans la validation décisive.
- **preregistered validation, 1,000 repetitions** : conforme (préenregistrée, contre-lue, scellée ; 1 000 répétitions par ligne ; confirmée par un lecteur neuf avec deux réserves mineures).

## D. PDF du mémo et corps du § 10

- Relu : `…_v2.pdf` (le v1 de la consigne n'existe plus). Extraction par `pdftotext -layout`, puis lignes recollées : la césure automatique est retirée et le trait d'union réel est gardé.
- **Les cinq paragraphes du corps sont identiques au § 10 actuel, mot pour mot.** Il y a six césures automatiques en fin de ligne (preregis-trations, sta-tistical, manu-script, cost-in-flating, moni-tor, train-ing). C'est cosmétique ; seul « cost-in- / flating » coupe un mot déjà composé.
- Le bloc de titre diffère. Le PDF porte « Career memo » puis « Lazar Ciric · 2 November 2026 · Pivotal Research Fellowship, 2027 Q1 ». Le § 10 porte « Career memo, Lazar Ciric, 2 November 2026 ». Le PDF ajoute donc le nom du programme, ce qui est sans risque.
- **Une page** : `pdfinfo` donne 1 page A4. Le texte va de x = 62 à 533 pt (sur 595) et de y = 65 à 555 pt (sur 842), soit environ 101 mm libres en bas. Rien n'est rogné : la dernière ligne, « Practical … First-time fellow. », est présente.

## E. Réponse à Kirchner, phrase sur 0,06–0,12 nat

**Elle dit plus que le verdict.** « would have been caught nine times in ten » est un contrefactuel affirmé sur cette lecture. Placé juste après « no real link », il se lit comme une borne sur les liens réels. Or le verdict dit : ordre de grandeur de la sensibilité, 0,9 par moniteur et non pour les 13 à la fois, pas une borne démontrée, borne non opposable. La courbe est exploratoire et non contre-lue. Elle a été mesurée en monde informé, au seuil 5,83, sur une loi exacte, puis transposée à une loi estimée en monde aveugle, au seuil 6,25. Le coût d'estimation (0,011 à 0,029 nat) peut masquer une dépendance de cet ordre. La phrase ne dit pas non plus « par moniteur ».

Le remplacement 3 garde le contenu permis : ordre de grandeur (« rough »), par moniteur, puissance de 90 %, forme plantée, « not a proven bound ». Les chiffres sont conformes : 0,057–0,117 arrondis à 0,06–0,12. Il fait deux mots de moins, à longueur égale en caractères. « its » renvoie au juge, sujet de la proposition précédente.

Hors périmètre, une ligne : le README public écrit « Bound, monitor by monitor: … would be promoted with probability 0.9 » sans la réserve « pas une borne démontrée » du verdict. Le mémo renvoie à ce dépôt. Le corriger est une publication, donc ta décision.

## F. Limites de mots (v14, compte par mots séparés par des espaces ; entre parenthèses, compte strict où tirets, points et barres coupent les mots)

| section | mots | limite | statut |
|---|---|---|---|
| § 1, ligne 1 | 9 (10) | 10 | conforme |
| § 1, ligne 2 | 9 (17) | 10 | conforme |
| § 1, ligne 3 | 10 (14) | 10 | conforme, à la limite |
| § 2 | 147 (161) | 150 | conforme |
| § 3 | 195 (203) | 200 | conforme |
| § 4 | 87, soit 85 sans « 1. » et « 2. » (90) | 100 | conforme |
| § 6 | 147 (150) | 150 | conforme |
| § 7 | 141 (143) | 150 | conforme |

Les §§ 1 à 7 sont identiques à v13 à l'octet, donc ces comptes valent aussi pour v13. Si le formulaire comptait de façon stricte, la ligne 2 et la ligne 3 du § 1, le § 2 et le § 3 dépasseraient. Les marges du § 2 (3 mots) et du § 3 (5 mots) sont minces. Pour information, le § 10 passe de 277 à 321 mots ; son titre ne fixe plus de limite (« one page »).
