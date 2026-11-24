# Contre-lecture côté exposé, v1

Contre-lecteur neuf (Claude Opus 5.5). Je n'ai écrit aucune des pièces relues. Je n'ai lu aucune valeur de sortie de course : seulement des noms de fichiers et des noms de clés. Je n'ai ouvert aucune consigne privée et je n'ai modifié aucun fichier du dépôt. Les essais tournent dans `scratchpad/cl-essais/`.

## Verdicts

- **A. Programme d'extraction de la liste des exclus** (`extraire_liste_exclus_ordre_course_lue_v1.py`) : **non acceptable en l'état, un bloquant.** Le code recopie fidèlement, à l'octet, ce qu'il vise. Mais il ne vise pas le bon texte pour le renvoi « § 8 de l'ordre de la première course ». Il prend le brouillon 8, alors que l'ordre neuf désigne lui-même l'ordre scellé de la première course : `ordre-exploratoire-ii-b-v1.md`, empreinte `43a7a050…`, scellé le 19 novembre (R-3681). Le § 8 de ce texte scellé nomme six exclus de plus, et son en-tête en nomme deux autres. Il manque aussi un majeur et plusieurs mineurs (voir plus bas).
- **B. Constat sur les scripts de lecture** : **le constat tient**, et il est même un peu plus fort qu'énoncé. Aucune voie déjà en place (module, script ou option) ne joue les lectures du dommage et de la diffusion sur la course v5 sans code neuf.

---

## A. Contre-lecture du programme d'extraction

### Bloquant

**B-1. Mauvaise version de « l'ordre de la première course ».**
- Le point 4 du § 8 de la pièce de rang 1 renvoie à « ceux que nomme le § 8 de l'ordre de la première course ». Cette même pièce identifie le texte, en-tête ligne 12 : « l'ordre scellé de la première course (`brouillons/ii-b-saboteur-budget-v1/ordre-exploratoire-ii-b-v1.md`, `43a7a050d769792f3c5d7859509b69f34e082f953840909a1f59a1535bf01b3e`, intact, R12) ».
- Ce fichier est le brouillon 12, scellé comme ordre (registre des décisions, R-3681). Il est présent sur `main` et conforme à son compagnon.
- Son § 8 diffère de celui du brouillon 8. Il ajoute ceci :
  - les **« Ajouts du brouillon 9 »** : l'exécutante de la première course, qui a écrit la configuration (R-3525) ; le développeur du correctif du lanceur (R-3619, R-3625) ; le contre-lecteur de ce correctif (R-3630) ; le rédacteur des brouillons 9 et 10 (R-3635) ; le fabricant de la conception finale (R-3527) ; le contrôleur de la différence entre les brouillons 7 et 8 (R-3535) ;
  - un renvoi de plus : « le registre « qui a lu quoi » fait foi » ;
  - une correction : le rédacteur du brouillon 8 renvoie à `R-3524`, et non plus à « `R-3523`, suite ».
- Son **en-tête** (ligne Statut, ligne 7) porte aussi des phrases d'exclusion. Elles visent le rédacteur des brouillons 9 et 10 et le rédacteur des brouillons 11 et 12, chacun « exclu de tout rôle côté sondes du barreau 8 (rédaction, contre-lecture, lecture, verdict ; § 8) ». **Le rédacteur des brouillons 11 et 12 n'est nommé qu'en en-tête, et nulle part au § 8.**
- Le titre du bloc 3 de l'extrait présente donc à tort le brouillon 8 comme « l'ordre de la première course ».
- Correction : prendre `ordre-exploratoire-ii-b-v1.md` (`43a7a050…`), au § 8, du début de « **Exclus de toute lecture des sondes du barreau 8** » à la fin du paragraphe, y compris les « Ajouts du brouillon 9 ». Ajouter les phrases d'exclusion de l'en-tête. Garder le renvoi « Comme au brouillon 3, § 8 », qui est toujours présent, donc le bloc du brouillon 3. Le brouillon 8 peut sortir, ou rester comme bloc historique sous un titre juste.

### Majeurs

**M-1. La pièce de rang 2 (additif 1, `a9d43d59…`) n'est ni lue ni contrôlée.**
- Le code ne vérifie que les rangs 0 et 1 de l'attestation. Il ne contrôle ni la longueur de la liste des pièces, ni l'empreinte du rang 2, ni le champ `scelle == "oui"`.
- J'ai lu cet additif en entier : il ne porte **aucune** phrase d'exclusion. L'extrait doit le dire, et le code doit l'établir. Il faut exiger la pièce à son empreinte, chercher les motifs (`exclu`, `exclusion`, `côté sondes`, `lecteur des sondes`) et inscrire « rang 2 : aucune phrase d'exclusion (empreinte) ». Sinon, le lecteur ne peut pas savoir si la troisième pièce de l'ordre neuf a été examinée.

**M-2. Une phrase d'exclusion de la pièce de rang 1 est omise.**
- L'en-tête de la pièce de rang 1 (ligne 12, une seule occurrence) porte : « Il entre dans la liste d'exclusion des rôles côté sondes (§ 8). »
- L'extrait recopie la phrase homologue de la pièce de rang 0 (bloc 2), mais pas celle-ci. Le fond est couvert par « le rédacteur de cet ordre » au point 4, mais le critère « aucune phrase omise » n'est pas tenu.

### Mineurs

- **m-1. La consigne de ne jamais montrer n'est pas reprise du brouillon 3.** Le brouillon 3, § 8, repris tout entier par « Comme au brouillon 3, § 8 », porte : « **Jamais montré** : la consigne privée du maître, au lecteur des sondes ; … ». Ce n'est pas un rôle exclu, mais c'est une règle du même côté. Le point 4 de la pièce de rang 1 en porte l'équivalent, et l'extrait le reprend. Il faut soit l'inclure, soit dire explicitement qu'elle est laissée de côté.
- **m-2. Ce que le texte de l'ordre laisse ouvert (pour la mère, pas pour le code).**
  - La pièce de rang 0 n'exclut que « Le rédacteur » (Fable 5.2). Aucune pièce de l'ordre neuf ne nomme le rédacteur du brouillon 3 de l'additif (Opus 5.5, qui a écrit « en l'absence de Fable ») ni le contre-lecteur de l'additif de la voie (A).
  - L'additif 1 ne nomme ni son rédacteur (« la session de reconception ») ni son vérificateur.
  - L'extrait, recopié à l'octet, ne peut pas combler ces manques. Il faut les rendre à la mère.
- **m-3. Le « rédacteur » du bloc 2 n'est pas identifiable.** La phrase est coupée de ce qui précède (« par Claude Fable 5.2, rédacteur, du côté du saboteur, sous le mandat … »). Je recommande d'ajouter cette identification, recopiée à l'octet. Elle ne porte aucun mécanisme.
- **m-4. Les brouillons 3 et 8 ne sont pas contrôlés contre leurs compagnons.** Le texte d'aide dit qu'ils le sont ; le code ne les compare qu'à la constante écrite en dur. Il faut aligner le code sur le texte, ou l'inverse.
- **m-5. Non-écrasement fragile.** Le contrôle `exists()` précède `write_bytes`, ce qui laisse une course possible entre les deux. Ouvrir le fichier en mode `"xb"` règle ce point. Si l'écriture du compagnon échoue, l'extrait reste sans compagnon.
- **m-6. Erreurs de système non interceptées.** Une `OSError` (dossier de sortie absent, par exemple) ne passe pas par `Refus` : elle sort par une trace Python. Le code de sortie vaut tout de même 1, donc aucun repli silencieux, mais le message n'est pas conforme.
- **m-7. Inscription au registre « qui a lu quoi ».** Le point 4 de la pièce de rang 1 dit : « La mère inscrit au registre « qui a lu quoi » quiconque lit cet ordre. » Il faut trancher si le lecteur de l'extrait y entre. Je recommande que oui.
- **m-8. Détail de code.** `import json` est placé dans la fonction ; c'est une question de style.

### Essais joués (cas sain et artefacts)

| Cas | Résultat |
|---|---|
| Cas sain | code 0 ; sortie identique à l'octet à `essai-exclus.md` (`0290c29f…`) |
| Sortie déjà présente ; compagnon seul déjà présent | refus, code 1 |
| Source altérée d'un octet | refus sur l'empreinte, code 1 |
| Source absente | refus, code 1 |
| Attestation altérée | refus, code 1 |
| Garde d'unicité (`unique`) sur un passage en double (essai direct sur la fonction) | refus |
| Garde de section (`section`) sur une section en double (essai direct sur la fonction) | refus |
| Dossier de sortie absent | trace Python, code 1 (voir m-6) |

Fidélité, vérifiée par un relevé indépendant : les quatre passages de l'extrait sont des sous-chaînes exactes de leurs sources. Chacun apparaît une seule fois, et son empreinte est égale à celle qu'imprime l'extrait.

### Cloisonnement

Correct. L'extrait ne porte aucun mécanisme du saboteur, aucune valeur de réglage, aucun fragment de consigne et aucun chiffre de résultat. Il ne contient que des rôles, des lignes de registre, des têtes de commit, le chemin de la note du chemin critique et la phrase « Le § 2 porte des réglages de la base textuelle des moniteurs », qui ne donne aucune valeur.

Point d'attention pour la correction B-1 : couper le § 8 de l'ordre scellé à « **Exclus de toute lecture** ». La phrase qui précède cite le texte de lecture des sondes (chemin et empreinte). Elle est sans danger, mais inutile ici.

---

## B. Constat sur les scripts de lecture : le constat tient

**Ce que les scripts exigent.** Les deux scripts `scripts/lecture_iib_1_dommage_v1.py` et `scripts/lecture_iib_2_diffusion_v1.py` passent par `src/controle_ia/iib/lecture_v1.py`. Au commit `192a429e`, `charger_sorties` exige que le résumé scellé (`resultat.empreintes`) porte quatre clés : `donnees/RUN/oracle-iib.json`, `diag/RUN/episodes-iib.json`, `diag/RUN/acceptation-iib.json` et, pour la diffusion, `donnees/RUN/textes-actions-iib.jsonl`. Ensuite, `actions_d_evaluation` lit `oracle["actions"]` et y attend les champs `phase`, `contexte == "reecrit"`, `episode`, `pas`, `bornable` et `e`.

**Ce que portent les sorties v5** (noms et clés seulement) :
- **Le résumé de la course** (`diag/20261123-043944-iib-course-reel/resume.json`) : ses clés d'empreintes sont des **noms relatifs**, sans préfixe `donnees/` ni `diag/`. Aucun des quatre fichiers attendus n'y figure. Le premier contrôle (« absent du résumé scellé ») arrête donc la lecture.
- **Où sont les fichiers.** Le dossier du run de la course ne contient que `resume.json`. Les sorties de la course sont sous `diag/20261122-202132-iib-reel/`, le dossier de l'étalonnage : `oracle-course-iib-v5.json`, `evaluation/oracles-evaluation-{H,B50,B100,TJ100}.json`, `evaluation-iib-v5.json`, `ids-actions-*.json`, `tours/`, entre autres. Sous `donnees/`, il n'y a que `donnees/20261122-202132-iib-reel/lots`.
- **La structure de l'oracle v5.** Clé `lignes`, et non `actions`. Chaque ligne porte `exces`, `estimation`, `oracle`, `fenetre`, `suites`, `couplage`, etc. Elle n'a **ni `e` ni `contexte`**.
- **Les textes.** Aucun fichier de textes n'existe : la v5 n'écrit que des identifiants de jetons (`ids-actions-*.json`, clé `ids`). La règle de la v5 est qu'« aucun texte d'épisode n'est écrit dans les sorties ».
- **Ajout au constat : la configuration et les graines manquent aussi.** `lecture_v1` lit `config["lecture_1"]`, `config["lecture_2"]` et les graines `iib/lecture-1/…` et `iib/lecture-2/…` du manifeste. Les manifestes v5 (`runs/20261123-043944-iib-course-reel/` et `runs/20261122-202132-iib-reel/`) n'ont ni clé `lecture_1` ni clé `lecture_2` dans `config`, et une seule graine, sans rapport avec la lecture.

**Aucun texte ne désigne une autre voie.**
- **Les trois pièces de l'ordre neuf.** Aucune ne nomme un script ni un module de lecture du dommage ou de la diffusion.
  - Pièce de rang 1, § 8 : point 3, les rapportés sans règle sont lus par un lecteur désigné ; point 4, aucune sonde.
  - Pièce de rang 0, § 4.5 : noms des sorties et citations avec « la phrase de 10.6 qui convient ».
  - Additif 1 : seuil et versement seulement.
- **Le texte scellé de l'organisme v5** (`c1dc5459…`, dans le worktree).
  - La section 10.5 dit la puissance de la lecture du dommage.
  - La section 10.6 donne les phrases écrites d'avance pour le dommage et la diffusion, mais aucun programme.
  - La section 13 (« Spécification du code, module par module ») ne liste aucun module de lecture du dommage ou de la diffusion. Elle précise : « aucun module antérieur modifié ».
- **Les modules v5 voisins ne sont pas ces lectures.**
  - `lecture_cout_v5.py` lit un coût sur une fenêtre.
  - `rapportes_v5.py` et la clé `rapportes` de `evaluation-iib-v5.json` donnent des rapportés descriptifs par condition et par oracle : excès par position, ancienne statistique, ancrage. Il n'y a ni effets appariés, ni phrase de dommage, ni bases de la diffusion.
  - Le lanceur v5 n'a que trois phases : `etalonnage`, `conditions`, `course`.
- **Rien d'autre dans l'historique.** Le seul autre programme qui touche ces lectures dans tout l'historique est `scripts/extrait_iib_etats_lectures_cote_moniteurs_v1-3.py`. Il est **en aval** : il lit les sorties scellées des lectures v1, et ne les calcule pas.

**Conclusion.** Aucune voie déjà en place ne joue ces deux lectures sur la course v5. Il faut deux choses :
1. une spécification (classe A), puisque la statistique v5 n'est plus `e_t` de l'oracle v1 et qu'il y a deux oracles. La section 10.5 parle de « EMD / m_R », la section 10.6 de « p = EMD / excès moyen lu du maître ». Pour la diffusion, il faudra aussi rebâtir les textes à partir des identifiants de jetons ;
2. du code neuf (classe B), contre-lu.

Un détail pour la future lecture : elle devra prendre le résumé et le manifeste sous l'identifiant du run de la course, mais les fichiers sous `diag/<run de l'étalonnage>/`.
