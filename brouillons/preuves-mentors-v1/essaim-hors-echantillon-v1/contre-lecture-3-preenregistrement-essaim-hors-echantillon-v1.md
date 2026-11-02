**Verdict : scellable après corrections mineures (C3.1 à C3.6, six rectifications de texte ; textes de remplacement prêts à coller en fin de rapport).**

Rien de scientifique n'a bougé entre les brouillons 2 et 3 : mêmes 84 prédictions, mêmes 311 cellules, mêmes seuils et mêmes critères, grille identique octet pour octet (`dbe1caf1…8007`). Les treize corrections de la contre-lecture 2 (M1 à M13) et ses cinq recommandations (Ra à Re) sont appliquées comme demandé, dans le texte et dans le code ; les 11 essais v3 et les 23 essais v1 et v2 passent. Restent six inexactitudes de texte (dont deux faits faux sans effet : 11 essais v3 et non 12 ; trois graines absentes de l'inventaire), et une procédure que Lazar doit trancher pour passer du brouillon 3 au texte scellé (section 7).

Codes employés. Familles : S = loi de référence iid ; Q = équicorrélation entre agents ; P = 60 épisodes honnêtes de P3 rééchantillonnés. Prédictions : H + lettre de la famille + numéro (HS.3 = puissance exacte sous la loi de référence ; HS.4 = elle dépasse son taux dès m/K = 0,3 ; HQ.5 = « en dessous » sous corrélation c = 0,3 ; HP.4 = fourchette de puissance en P ; HP.5a et HP.5b = signes de la co-élévation et de la moyenne par pas en P ; HE2.4 = règle de v1 sur la moyenne par pas). M1 à M13 : les treize corrections de la contre-lecture 2 ; Ra à Re : ses cinq recommandations ; C1 à C11 : celles de la contre-lecture 1 ; C3.1 à C3.9 : les remarques de la présente contre-lecture ; F1 à F3 : mises à jour de forme du brouillon 4. Chaque code est suivi d'un surnom. R2 = règle gelée « contre-lecture par un sous-agent neuf » ; R6 = « toute pièce déposée a son empreinte compagnon, tout chiffre renvoie à un chemin et une empreinte » ; R12 = « versions dans les noms, on n'écrase jamais ».

# Contre-lecture 3 (R2, courte, sur les seules différences) — préenregistrement « simulation d'essaim, épreuve sur cellules neuves (« hors échantillon »), brouillon 3 — v1

- **Contre-lecteur** : sous-agent neuf. Je n'ai écrit ni les brouillons 1 à 3, ni leur code, ni leurs essais, ni les contre-lectures 1 et 2, ni les rapports de rédaction. Rapport rédigé le 2026-11-02 (UTC).
- **Objet relu** : `brouillons/preuves-mentors-v1/essaim-hors-echantillon-v1/preenregistrement-essaim-hors-echantillon-v1-brouillon3.md`, sha256 `d1d5740e202dd972d017b236969acf499341b8187d6cbfcf63d571b36451e343`, commit `0106c0e9` (qui ajoute sept fichiers neufs, sans modifier ni supprimer aucun fichier existant) ; brouillon 2 : `92273360…` ; code v3 : `blocs_hors_echantillon_v3.py` (`0cd67658…`), `lecture_hors_echantillon_v3.py` (`3c94ed0b…`), `run_essaim_hors_echantillon_v3.py` (`d33de14c…`), essais `test_simulation_essaim_hors_echantillon_v3.py` (`7d5fa16f…`) ; ces quatre empreintes sont celles du rapport de rédaction (`rapport-redaction-v3.md`, `ebb0dbd7…`).
- **Lu en entier** : le brief ; la contre-lecture 2 ; le rapport de rédaction v3 ; les brouillons 2 et 3 ; le fichier de différences ; les trois modules v3 et leurs essais ; `lecture_hors_echantillon_v2` (dont le texte des énoncés) ; `prereg.py` (le validateur). **Lu en partie** : `fusionner` de la lecture de T0.3, `statistiques.comptes_par_pas`, `blocs.loi_reference`, `blocs.tirer_essaims`, `blocs.Contexte`.
- **Ce que j'ai refait moi-même plutôt que cru** : le `diff -u` brouillon 2 → brouillon 3 (19 zones, 275 lignes, identique à celui du fichier de différences) ; les 26 empreintes citées dans le brouillon 3, toutes égales aux fichiers sur disque ; les 14 pièces de `recalculs-contre-lecture-2/`, toutes égales à la table du rapport de la contre-lecture 2 ; la comparaison des deux grilles champ par champ ; le recomptage des 47 cellules ; les bornes de résolution (loi binomiale exacte).
- **Ce que j'ai lancé** (sous `nice -n 10`, sans bytecode ni cache, dossiers temporaires hors dépôt, aucun fichier existant modifié : 192 empreintes de `src`, `tests` et du dossier de l'essaim identiques avant et après, sauf celles de fichiers `analyse_principale_r1_r2` qu'une autre session écrit en parallèle sur un autre sujet) :
  - les 11 essais v3, les 23 essais v1 et v2, puis les trois fichiers ensemble (34) ;
  - `certifier_puissances_S` du lanceur v3 sur la vraie grille : formes closes seules, sans aucun tirage, 12 puissances exactes déjà imprimées dans le texte ;
  - la fonction `maxima` du descriptif sur la loi de référence iid seule, graines jetables hors grille 90210 et 90211 ;
  - un mini-run du lanceur v3 dans un dépôt jetable, sur la mini-grille et les données factices des essais ;
  - la branche « manifeste illisible » de `exiger_principal_v3`, par un script ;
  - `git fsck --unreachable --no-reflogs` sur le dépôt de travail (lecture seule), pour le temps et la taille de sa sortie ;
  - une copie jetable du brouillon 3 à laquelle j'ai appliqué mes remplacements, puis le validateur et la recopie.
- **Ce que je n'ai pas fait** : lancer la commande décisive, un bloc ou une cellule Monte-Carlo de la grille, ni la famille P sur les vraies données ; je n'ai pas ouvert le fichier P3 moi-même (seul l'essai v1 `test_loi_p3_empreinte_et_structure_sur_le_vrai_fichier` l'ouvre, pour son empreinte et sa structure, sans rien afficher) ; rien de réseau ; aucune clé ni aucun secret lu ou affiché ; aucun commit.

## Corrections — une ligne chacune

À appliquer avant le scellement (texte seul ; aucune ne touche une prédiction, un seuil, un critère, la grille ou le code) :
- **C3.1 — nombre d'essais v3.** L. 39 : « `_v3.py` (12) » est faux, il y en a 11 (dix fonctions, dont une jouée sur deux lanceurs).
- **C3.2 — inventaire des graines.** L. 250 : la liste « graines fixes déjà utilisées » omet 31415 (essai v3) et 77001, 77002 (calculs jetables de la contre-lecture 2, copiés dans le dossier). Sans effet sur l'argument de disjonction (2⁻⁹⁶), mais la liste se donne pour complète.
- **C3.3 — étape 0.a et gel des empreintes.** L. 274 ne gèle que « l'empreinte du dernier brouillon », alors que la parade de la graine (point 1, réécrit pour M8) en exige trois sortes (texte, rapports, fichiers de traitement) : celui qui suit l'étape 0.a ne figerait ni le rapport de la contre-lecture 3 ni son fichier de traitement, seuls leviers qui restent sur la graine.
- **C3.4 — durée.** L. 60 et 295 : le `git fsck` ajouté par Rb n'est pas compté ; je l'ai mesuré à 117 s à la première exécution et 22 s à la seconde sur le dépôt actuel (1,8 Go, sortie de 428 lignes).
- **C3.5 — « la grille 2 ne diffère que par ses étiquettes ».** L. 418 : inexact ; la grille 2 change aussi le critère de HP.4 (borne basse seule devenue fourchette), ajoute le drapeau « discriminante » et le descriptif des maxima ; cellules, alarmes et sens sont identiques sauf ceux de HP.4.
- **C3.6 — lanceur v2.** L. 34 : l'interdiction vise v1 et v2, mais seule la conséquence de v1 (échec à la lecture) est décrite ; v2 irait au bout sans erreur, avec les lectures prononcées d'avant M3 et la référence 1/T d'avant M2 : à écrire, avec l'action (signaler à Lazar avant toute lecture).

Recommandées (sans risque, à joindre si le brouillon 4 est fait) :
- **C3.7 — tournure de HQ.5 (Rd).** L. 159 : « tient à T = 20, pas seulement par HS.3 (T = 10) » se lit mal ; voulu : la discriminance tient aussi à T = 20.
- **C3.8 — empreinte du script de résolution.** L. 231 cite `recalculs-contre-lecture-2/resolution_cl2.py` sans empreinte (R6).
- **C3.9 — référence du journal des commits inaccessibles (Rb).** Le dépôt partagé compte déjà 74 commits inaccessibles ; sans liste de référence relevée à la consignation, le journal du lanceur ne permet pas de reconnaître un commit abandonné depuis (c'est le but de Rb).

Mises à jour de forme, seulement si le brouillon 4 est fait (voir section 7) : **F1** statut ; **F2** auteur ; **F3** point 1 de la parade (il faut dire que le texte scellé diffère du brouillon relu par les remplacements de cette contre-lecture).

Observations sans correction : voir section 4.

## 1. Les corrections M1 à M13 et les recommandations Ra à Re

| Code, surnom | État | Ce que j'ai vérifié |
|---|---|---|
| **M1** marqueurs piégés | conforme | Exactement deux marqueurs, une fois chacun : `<<COMMIT_CITE>>` (l. 24, entre accents graves) et `<<CONTRE_LECTURE_3>>` (l. 440) ; plus de `<<CONTRE_LECTURE_2>>`. L'étape 0.d (l. 277-280) les nomme sans les écrire et dit « avant, deux ; après, aucun ». Simulation sur copie : avant, le validateur refuse en nommant les deux marqueurs ; après remplacement du commit (40 caractères hexadécimaux) et de l'entrée de forme fixe, `prereg.problemes` est vide, le motif de la garde du commit cité retrouve le commit, et le `diff` ne porte que sur les deux lignes. Une entrée sans empreintes est refusée. |
| **M2** référence des maxima | conforme | Code : `np.argmax(C + 0.5 * g.random(C.shape))` ; C est entier, le bruit [0 ; 0,5[ ne peut pas franchir un entier, donc le départage est uniforme parmi les ex aequo ; l'essai donne 40 000 lignes toutes à égalité et un histogramme à ±0,01 de 0,1 (v2 donnait toujours le pas 0). Références iid aux mêmes (K, T) : `Q/e10x20/reference-iid/maxima` (K = 10, T = 20) et `P/reference-iid/maxima` (K = T = 10), ajoutées à `taches_maxima` donc au manifeste. Ma propre mesure de la fonction sur la loi iid (R = 20 000, graines jetables) : 0,2147 (K = T = 10) et 0,1470 (K = 10, T = 20), contre ≈ 0,216 et 0,148 dans le texte : compatible avec le bruit. 1/T ne subsiste que comme clé étiquetée `fraction_uniforme_1_sur_T` avec une note ; le texte (l. 97, 183, 432) ne l'emploie plus comme référence. |
| **M3** ce que dit la loi de référence | conforme | Recomptage : 47 = 39 (HS.5 : 24 ; HP.5b sauf une : 12 ; HP.6 « en dessous » à m = K : 3) + 4 sans prédiction de référence (moyenne par pas à m < 5) + 4 plus fortes que « au plus » (HP.6, tromperie, m = 6 et 7, deux statistiques). Lectures de HP.5a et HP.5b identiques aux textes proposés, table recopiée. Chaque affirmation s'appuie sur une prédiction écrite : forme close HS.3 et HS.4 pour la co-élévation à K = T = 10 (0,12158 à m = 3), règle HE2.4 de v1 pour la moyenne par pas à m ≥ 5, rien à m = 3 et 4 et le texte le dit. |
| **M4** « sans bogue » et la rejouée | conforme | L. 19 et phrase de portée (dans le code) identiques à la proposition. Voir l'observation O2 sur le mot « indépendantes ». |
| **M5** fausses confirmations | conforme | 45 cellules garanties (21 au-dessus, 22 en dessous, 2 fourchettes), soit ≤ 4,5·10⁻⁴ ; l'essai compte les sens sur la grille. La borne ≤ γ tient pour « au-dessus » et « en dessous » (comparaison de deux intervalles : une fausse confirmation exige qu'au moins l'un des deux manque sa cible du côté qui arrange, au plus γ/2 chacun) et pour la fourchette. Les 20 « au plus » de HS.5 sont exclues ; 0,92 repris de la règle de lecture d'un résultat nul. |
| **M6** audit des variances | conforme | Rangée de la table des issues : texte proposé mot pour mot, écart à v1 déclaré. |
| **M7** garde d'équivalence | conforme | `test_garde_equivalence_lanceurs` (artefact : `agent_moyenne` + 10⁻⁶) joué sur les lanceurs v2 et v3 ; le cas sain est la chaîne complète ; l. 378 le dit. |
| **M8** graine : tout geler ensemble | appliquée, incomplète | Points 1 et 3 de la parade conformes (empreintes gelées ; troncature 40 / 80 dite ; arbre séparé dit ; Rb). Mais l'étape 0.a n'a pas suivi (C3.3) et le journal n'a pas de référence (C3.9). Ce qui entre dans les octets scellés : le brouillon, ses deux entrées déjà écrites (leurs empreintes sont dans le texte), l'entrée à venir (brouillon relu, rapport de la contre-lecture 3, fichier de traitement v4) et le commit cité. À geler avant l'étape 0 : le texte à sceller, le rapport de la contre-lecture 3 et `rapport-redaction-v4.md`. |
| **M9** lanceur v1 interdit | conforme avec réserve | L. 34, 264 et 433 : v1 et v2 interdits, « seule la commande citée (lanceur v3) est permise » ; le texte dit que v1 ne peut pas être bloqué (R12), ce que son run ferait (blocs écrits, échec à la lecture sur `entre_x`, run unique consommé, blocs non ouverts, version nouvelle contre-lue) et renvoie au protocole après un arrêt. `exiger_principal_v3` : testé sur l'artefact (principal lancé par v2, arrêt « n'a pas été lancé par ») et sur le cas sain (la réplication v3) ; la branche « manifeste illisible » n'a pas d'essai, je l'ai éprouvée à la main (absent ou altéré : arrêt ; manifeste v3 accepté ; autre lanceur refusé). Réserve : le cas de v2 (C3.6). |
| **M10** portée de `audit_declenche` | conforme | Phrase ajoutée à la l. 346 et au `lecture.md` (le lanceur l'écrit sous le tableau). |
| **M11** provenance et bornes de HP.4 | conforme | Recalcul indépendant (loi binomiale exacte) : HP.4 conforme pour 11 311 ≤ k ≤ 16 980 (tromperie) et 6 491 ≤ k ≤ 12 095 (enjeux) sur 20 000 ; « en dessous » pour k ≤ 810, « au-dessus » pour k ≥ 1 206 (intervalle de la référence [0,04701 ; 0,05311]) : tous égaux au texte. Source : rapport de la contre-lecture 1 (chemin et empreinte). |
| **M12** essais sur le bon objet | conforme | `test_grille_v2_memes_cellules_et_sens_que_v1` est celui de la proposition ; j'ai comparé les deux grilles champ par champ (section 2). L'essai de recopie porte sur le brouillon 3 (tableau E, phrase de portée, deux marqueurs, aucun `<<CONTRE_LECTURE_2>>`). Tous les noms d'essais et de modules cités dans le texte existent. |
| **M13** brouillon 3 et marqueurs | conforme | Statut, auteur (l. 22), entrée de la contre-lecture 2 de forme fixe (trois chemins, trois empreintes distinctes, validées), marqueur `<<CONTRE_LECTURE_3>>`, note de fin. |
| **Ra** certification avant tout tirage | conforme | `certifier_puissances_S` est placée après les gardes et avant `creer_manifeste` ; une erreur certifiée > 10⁻⁶ lève `GardeArret` « avant tout tirage ». L'essai bouche `puissance_exacte` (erreur 10⁻³) et constate qu'aucun dossier `runs/` n'existe ; le cas sain est la chaîne. Sur la vraie grille (formes closes seules) : 12 cellules en 4,9 s, valeurs égales à la table du texte (0,12158 à 0,99891), erreurs ≤ 6,5·10⁻¹⁰. |
| **Rb** journal git élargi | appliquée | Les clés `arbres` et `inaccessibles` sont écrites. Réserves : durée (C3.4) et absence de référence (C3.9). |
| **Rc** lecture partielle | conforme | `lire_partielle` marque `partielle`, sans scores ni « trop beau » ; seule la lecture finale fusionnée est annotée et alimente `scores` et `lecture.md` ; essai sur l'artefact. |
| **Rd** HQ.5 fondée à T = 20 | conforme | 0,155295 (m = 3) et 0,704371 (m = 5) recalculés par `bornes_synchro_v2` à e10x20 (seuil [4 ; 0,09137], erreur ≤ 8,3·10⁻¹⁰), égaux à la contre-lecture 2. Tournure : C3.7. |
| **Re** égalité avec v1 en réplication | conforme | `test_replication_v3_partielle_et_fusion_egale_a_v1` compare états et verdicts finaux à `fusionner` appliqué aux lectures v1, hors HS.3 et HP.4. |

## 2. La grille et l'essai « grille 2 = grille 1 aux étiquettes près »

- **Empreinte** : `grille-essaim-hors-echantillon-v1-brouillon2.json` = `dbe1caf113ac12cf9e056cfd2f6916eb2d13341735cb58b0260acc64d86c8007`, égale à celle du brief et du texte (l. 42) ; le commit `0106c0e9` ne la touche pas. Le générateur (`5210650c…`) et les tables (`c94b6542…`) citées sont aussi égaux aux fichiers.
- **Comparaison champ par champ** des grilles 1 et 2 (84 prédictions chacune, mêmes 84 couples cellule-alarme) : hors prédictions, seule la clé `descriptif_maxima` (R = 20 000) est ajoutée, et `version` change. Dans les prédictions, seuls diffèrent le drapeau `discriminante` (ajouté), HP.4 (sens, valeur, bornes), et HP.5 qui devient HP.5a (7) et HP.5b (13). Aucun sens n'a changé ailleurs.
- **L'essai est correct** : il compare tout sauf `predictions`, `version` et `descriptif_maxima`, puis les couples (cellule, alarme, « est HP.4 »), puis les sens, avec l'exception HP.4. Il ne peut pas passer à vide : 84 clés des deux côtés et aucune collision. Limite sans conséquence : il ne vérifie pas l'empreinte de la grille 2, ce que fait l'étape 0.b (`sceller` doit afficher l'empreinte citée).

## 3. Les lectures prononcées et la phrase de portée

- Recherche des mots à risque dans le texte entier : « loi réelle », « loi honnête réelle », « mécanisme confirmé », « modèle de substitution confirmé » sont absents ; « sur données réelles » n'apparaît que dans une négation (l. 86) ; « établi » ne qualifie que le calcul (forme close) ou figure dans « non établi ».
- Ce que diront les lectures si tout est confirmé, en clair : (i) sous la loi de référence, ⌈K/2⌉ n'est pas une frontière, par le calcul et non par l'expérience ; (ii) sous corrélation c = 0,3, la synchronisation partielle fait passer la co-élévation sous son taux, le mécanisme restant conjecturé ; (iii) pour ces 60 épisodes et la sonde des enjeux, la règle ⌈K/2⌉ échoue, signe prédit par un modèle ajusté sur les moments de ces mêmes épisodes ; (iv) les autres signes de P sont ceux que donnait déjà la loi de référence (sauf une cellule), donc ne départagent pas le modèle d'un pronostic naïf. Aucune ne dit « loi réelle de P3 », ni ne confirme le mécanisme.
- La phrase de portée garde « aucun vrai essaim n'a été observé », « conditionnels à cet échantillon » et dit que les prédictions viennent d'un modèle ajusté sur les moments de ces mêmes épisodes.

## 4. Nouvelles failles introduites par v3

**Code** : aucune faille fonctionnelle trouvée. Observations, sans correction demandée :
- **O1** Le `lecture.json` écrit `version = lecture_hors_echantillon_v2` (hérité de `LecteurHOv2.lire`) à côté de `lecture_version = lecture_hors_echantillon_v3`, qui fait foi ; le manifeste porte `lecture = …v3`. À dire dans la passation ; le corriger demanderait un module de plus.
- **O2** « Indépendantes » dans la phrase de portée veut dire « non rejouées », pas « indépendantes des 600 actions que le modèle a vues » ; la phrase précédente le dit déjà. Sa formulation vit dans le code cité : pas de correction.
- **O3** Un essai de six lignes pour la branche « manifeste illisible » de `exiger_principal_v3` serait bienvenu (règle R5 : chaque garde est éprouvée sur un cas sain et sur un artefact) ; non bloquant, je l'ai éprouvée à la main.
- **O4** Les codes d'items (M2, M9, M10, Ra, Rb…) apparaissent dans le texte sans glose ; ils renvoient au rapport de la contre-lecture 2, cité par son entrée. Non bloquant.
- **O5** Comme pour R6, les empreintes compagnons (`.sha256`) du brouillon 3, des rapports et des 14 pièces copiées dans `recalculs-contre-lecture-2/` restent à créer par la session principale.
- Le descriptif de la loi de référence iid tourne en moins d'une seconde à R = 20 000 ; l'estimation de ≈ 7 s est large, sans conséquence.

**Texte** : C3.1 à C3.6 ci-dessus. Les autres changements du brouillon 3 (statut, sections de transparence, limites, entrées de contre-lecture) sont conformes.

## 5. Les marqueurs restants

Aucun « À REMPLIR » dans le texte ; deux marqueurs de gabarit seulement, vérifiés par le validateur.
- `<<COMMIT_CITE>>` (l. 24) : les 40 caractères hexadécimaux minuscules de `git rev-parse HEAD` pris juste après l'étape 0.c, les accents graves restant ; le motif de la garde (« Commit du code d'analyse : » suivi de 40 caractères hexadécimaux entre accents graves) doit le retrouver.
- `<<CONTRE_LECTURE_3>>` (l. 440) : une seule ligne, sans autre phrase (le fichier de traitement est exigé même si la contre-lecture 3 ne demande plus rien). Entrée selon la voie B de la section 7 ; avec la voie A, le brouillon relu serait le brouillon 4 :

```
- **Contre-lecture 3** (R2) — brouillon relu : `brouillons/preuves-mentors-v1/essaim-hors-echantillon-v1/preenregistrement-essaim-hors-echantillon-v1-brouillon3.md`, sha256 `d1d5740e202dd972d017b236969acf499341b8187d6cbfcf63d571b36451e343` ; rapport : `brouillons/preuves-mentors-v1/essaim-hors-echantillon-v1/contre-lecture-3-preenregistrement-essaim-hors-echantillon-v1.md`, sha256 `<empreinte de ce rapport, rendue à part>` ; traitement : `brouillons/preuves-mentors-v1/essaim-hors-echantillon-v1/rapport-redaction-v4.md`, sha256 `<empreinte du traitement>`.
```
- Contrôles à l'étape 0.d : `diff` limité aux deux lignes des marqueurs ; `prereg.problemes` vide ; plus aucun `<<`.

## 6. Les essais

Sous `nice -n 10`, sans bytecode ni cache, dossier temporaire hors dépôt :
- `tests/test_simulation_essaim_hors_echantillon_v3.py` : **11 passés en 6,0 s** (le brief et le texte en annonçaient 12 : C3.1) ;
- `_v1.py` (11) et `_v2.py` (12) : **23 passés en 7,9 s** ;
- les trois fichiers ensemble : **34 passés en 13,1 s**.
Le mini-run du lanceur v3 écrit les neuf résultats scellés attendus, chacun avec son empreinte compagnon (trois blocs, équivalence, journal git avec `arbres` et `inaccessibles`, `puissances-exactes-S.json`, descriptif avec ses deux références, lecture), la phrase de portée en troisième ligne de `lecture.md` et les scores en cinquième.

## 7. Suite procédurale — décision pour Lazar

Le texte à sceller doit, selon la parade (point 1), ne différer du dernier brouillon contre-lu que par ses marqueurs. Mes six corrections de texte feraient un brouillon 4 qui diffère du brouillon 3. Trois voies :
- **B (recommandée).** Le brouillon 4 = le brouillon 3 + exactement les remplacements ci-dessous (C3.1 à C3.9 et F1 à F3), appliqués par un script qui vérifie que chaque ancien texte apparaît une fois, que les deux marqueurs restent, que la recopie de la table E et de la phrase de portée tient, que le validateur est vide après un scellement simulé, et que le `diff` ne porte que sur douze lignes (c'est ce que fait `appliquer_corrections_cl3.py`, résultat en section 9). L'entrée de la contre-lecture 3 cite le brouillon 3 comme « relu » (c'est ce que j'ai lu) ; F3 écrit dans la parade l'écart. À geler avant l'étape 0 : brouillon 4, ce rapport, `rapport-redaction-v4.md` (C3.3). Les essais ne changent pas : les remplacements ne touchent ni la table E, ni la phrase de portée, ni les marqueurs, donc `test_table_E_et_marqueurs_du_brouillon3` vaut pour le brouillon 4 (je l'ai vérifié sur la copie).
- **A (lettre de R2).** Brouillon 4 faisant l'objet d'une contre-lecture 4 de quelques minutes sur son seul `diff`, avec une entrée de la contre-lecture 3 remplie dans le brouillon 4 et un marqueur `<<CONTRE_LECTURE_4>>`. Plus lent, sans gain scientifique.
- **C.** Sceller le brouillon 3 tel quel, en consignant C3.1 et C3.2 comme erratum dans la passation. Les deux faits faux resteraient dans le texte scellé ; non recommandé.

## 8. Textes de remplacement (prêts à coller)

Les numéros de ligne sont ceux du brouillon 3. Chaque ancien texte apparaît exactement une fois dans le brouillon 3 (vérifié par script). Les blocs sont encadrés de quatre accents graves parce que les textes contiennent des accents graves.

#### C3.1

Ancien texte (une occurrence exactement) :

````
`tests/test_simulation_essaim_hors_echantillon_v1.py` (11), `_v2.py` (12) et `_v3.py` (12).
````

Nouveau texte :

````
`tests/test_simulation_essaim_hors_echantillon_v1.py` (11), `_v2.py` (12) et `_v3.py` (11, dont un essai joué sur deux lanceurs).
````

#### C3.2

Ancien texte (une occurrence exactement) :

````
Graines de ce dossier et des essais : 8675309 (modèle de substitution), 424243 (chronométrage), 97531, 97532, 24680, 24681, 13579, 123456789 (essais).
````

Nouveau texte :

````
Graines de ce dossier et des essais : 8675309 (modèle de substitution), 424243 (chronométrage), 77001 et 77002 (Monte-Carlo jetable de la contre-lecture 2), 31415, 97531, 97532, 24680, 24681, 13579, 123456789 (essais).
````

#### C3.3

Ancien texte (une occurrence exactement) :

````
Consigner et pousser l'empreinte du dernier brouillon contre-lu (C5.1).
````

Nouveau texte :

````
Consigner et pousser (C5.1) les empreintes du texte à sceller (dernier brouillon contre-lu, remplacements de la dernière contre-lecture compris), de chaque rapport de contre-lecture et de chaque fichier de traitement, y compris ceux de l'entrée qui remplacera le marqueur de la section « Contre-lecture ».
````

#### C3.4a

Ancien texte (une occurrence exactement) :

````
**Durée estimée** : environ 4 minutes, jusqu'à 8 sous forte charge (section « Plan d'analyse »).
````

Nouveau texte :

````
**Durée estimée** : environ 4 minutes de calcul, jusqu'à 8 sous forte charge, auxquelles s'ajoute le `git fsck` du journal git, de l'ordre d'une demi-minute à deux minutes sur le dépôt actuel (section « Plan d'analyse »).
````

#### C3.4b

Ancien texte (une occurrence exactement) :

````
Total **≈ 4 minutes**, jusqu'à 8 sous forte charge ; une réplication complète prend au plus ≈ 20 minutes.
````

Nouveau texte :

````
Total **≈ 4 minutes**, jusqu'à 8 sous forte charge, auxquelles s'ajoute le `git fsck --unreachable --no-reflogs` du journal git (Rb), qui parcourt tout le dépôt partagé : de l'ordre d'une demi-minute à deux minutes sur le dépôt actuel (estimé, non chronométré dans l'arbre séparé) ; une réplication complète prend au plus ≈ 20 minutes.
````

#### C3.5

Ancien texte (une occurrence exactement) :

````
sur la grille du brouillon 1, dont celle du brouillon 2 ne diffère que par ses étiquettes (essai `test_grille_v2_memes_cellules_et_sens_que_v1`)
````

Nouveau texte :

````
sur la grille du brouillon 1 ; celle du brouillon 2 porte les mêmes cellules et les mêmes alarmes, avec les mêmes sens sauf HP.4 (borne basse seule devenue fourchette), et ne change que des étiquettes (HP.5 devenue HP.5a et HP.5b), le drapeau « discriminante » et l'ajout du descriptif des maxima (essai `test_grille_v2_memes_cellules_et_sens_que_v1`)
````

#### C3.6

Ancien texte (une occurrence exactement) :

````
le lanceur v3 refuse seulement de répliquer un run qu'il n'a pas lancé.
````

Nouveau texte :

````
le lanceur v3 refuse seulement de répliquer un run qu'il n'a pas lancé. Le lanceur v2 irait, lui, au bout sans erreur, mais avec les lectures prononcées et le descriptif des maxima d'avant la contre-lecture 2 (référence 1/T, lectures de HP.5a et HP.5b non corrigées) : son run consommerait aussi le run unique et serait un écart à ce texte scellé, à signaler à Lazar avant toute lecture des résultats.
````

#### C3.7 (recommandée)

Ancien texte (une occurrence exactement) :

````
et la discriminance de HQ.5 tient à T = 20, pas seulement par HS.3 (T = 10).
````

Nouveau texte :

````
et la discriminance de HQ.5 tient donc aussi à T = 20, et pas seulement, par HS.3, à T = 10.
````

#### C3.8 (recommandée)

Ancien texte (une occurrence exactement) :

````
recalculés par la contre-lecture 2, `recalculs-contre-lecture-2/resolution_cl2.py`)
````

Nouveau texte :

````
recalculés par la contre-lecture 2, `recalculs-contre-lecture-2/resolution_cl2.py`, sha256 `746813a1a710ac2dcfa90aea14147892bccb6c667d3f31a46e51e370ecee7cf2`)
````

#### C3.9 (recommandée)

Ancien texte (une occurrence exactement) :

````
Ouvrir, à ce commit et hors du dépôt principal, un arbre de travail séparé
````

Nouveau texte :

````
Relever aussi, et consigner avec son empreinte, la sortie de `git fsck --unreachable --no-reflogs` : des commits inaccessibles y figurent déjà, et elle sert de référence pour reconnaître, dans le journal git du lanceur, un commit abandonné depuis la consignation (Rb). Ouvrir, à ce commit et hors du dépôt principal, un arbre de travail séparé
````

#### F1 statut

Ancien texte (une occurrence exactement) :

````
**Statut : brouillon 3.** Les brouillons 1 et 2 ont été contre-lus (R2, section « Contre-lecture »). Ce texte applique les corrections C1 à C11 et les recommandations R1, R2, R3 et R6 de la contre-lecture 1, puis les corrections M1 à M13 et les recommandations Ra à Re de la contre-lecture 2. Il se fait contre-lire sur ses seules différences avec le brouillon 2 par un sous-agent neuf, puis se scelle
````

Nouveau texte :

````
**Statut : brouillon 4.** Les brouillons 1, 2 et 3 ont été contre-lus (R2, section « Contre-lecture »). Ce texte applique les corrections C1 à C11 et les recommandations R1, R2, R3 et R6 de la contre-lecture 1, les corrections M1 à M13 et les recommandations Ra à Re de la contre-lecture 2, puis les corrections et recommandations de la contre-lecture 3. Le brouillon 3 a été contre-lu sur ses seules différences avec le brouillon 2 par un sous-agent neuf ; le brouillon 4 ne diffère du brouillon 3 que par les remplacements de la contre-lecture 3, reproduits mot pour mot dans son rapport. Il se scelle
````

#### F2 auteur

Ancien texte (une occurrence exactement) :

````
Brouillon 1 rédigé le 2026-11-01, brouillons 2 et 3 le 2026-11-02. Il n'a écrit ni le préenregistrement v1, ni son code, ni sa lecture, ni le verdict R13, ni les contre-lectures 1 et 2.
````

Nouveau texte :

````
Brouillon 1 rédigé le 2026-11-01, brouillons 2, 3 et 4 le 2026-11-02. Il n'a écrit ni le préenregistrement v1, ni son code, ni sa lecture, ni le verdict R13, ni les contre-lectures 1, 2 et 3.
````

#### F3 parade, point 1

Ancien texte (une occurrence exactement) :

````
1. le texte scellé ne diffère du dernier brouillon contre-lu que par ses marqueurs. Avant l'étape 0,
````

Nouveau texte :

````
1. le texte scellé ne diffère du dernier brouillon contre-lu que par ses marqueurs et par les remplacements de la dernière contre-lecture, reproduits mot pour mot dans son rapport (contrôle par `diff`). Avant l'étape 0,
````

## 9. Calculs faits par la contre-lecture 3 et fichiers (hors dépôt)

Aucun de ces calculs n'est repris dans les textes de remplacement, sauf l'ordre de grandeur de la durée du `fsck` (C3.4), donné comme estimation non chronométrée dans l'arbre séparé : ils n'ont donc pas à figurer en « Transparence ». Je ne les ai pas copiés dans le dépôt. Si l'un d'eux y est cité plus tard, copier le script et sa sortie avec leurs compagnons `.sha256` (R6).

- Formes closes sans tirage : les 12 puissances exactes de S par `certifier_puissances_S` (égales à la table du texte) ; les puissances à e10x20 (0,155295 et 0,704371) ; les bornes de résolution et de HP.4 par la loi binomiale exacte.
- Monte-Carlo jetable, hors grille : la part des maxima sous la loi de référence iid par la fonction `maxima` du brouillon 3, R = 20 000, graines `SeedSequence(90210)` (K = T = 10 : 0,2147) et `SeedSequence(90211)` (K = 10, T = 20 : 0,1470). Aucune cellule de la grille, aucune loi Q, aucune sonde P.
- Mesures de durée : `git fsck --unreachable --no-reflogs` sur le dépôt de travail : 117 s (première mesure, cache probablement froid, une autre session active) puis 22 s (à chaud) ; sortie : 428 lignes (74 commits, 282 arbres, 72 blobs inaccessibles) ; certification de S : 4,9 s.

Dossier de travail : `/tmp/claude-0/-home-claude/730d0294-0b2b-55ca-8b32-49f2d3ec072d/scratchpad/cl3-scripts/`

| Fichier | Rôle | sha256 |
|---|---|---|
| `verif_ra_et_maxima_cl3.py` | Ra sur la vraie grille ; maxima sur la loi iid ; branche « manifeste illisible » | `13b3e150dfe48f8222dca167c48c40fffdf6122093964886b8f5b3895740baf9` |
| `sortie-verif-ra-et-maxima-cl3.txt` | sa sortie | `2d268cf87a3b45d8a969fb58416fc3e83c68fe8b3e9cfc6856ef9544a87971b6` |
| `mini_run_cl3.py` | mini-run du lanceur v3 en dépôt jetable | `1d8b783416a51f8cb42f1025fccf43adb360e4718a9f436a1fa193b3c1140097` |
| `sortie-mini-run-cl3.txt` | sa sortie | `20edc4f8b3aefaaa4bf8c1f29a4b9152c7707cad2228957a9c1cabe93cb655ab` |
| `appliquer_corrections_cl3.py` | applique les remplacements à une copie du brouillon 3 et contrôle | `a9d133bf8142bdd034b824dc01f944936d4a21c92c3e60412c57b12884136f3e` |
| `sortie-appliquer-corrections-cl3.txt` | sa sortie (13 remplacements, une occurrence chacun ; validateur vide) | `727f5bcc048e5a8ec8bc1bb0b4c5af97592e7e3b49f715c0f62030eb5189e38f` |
| `brouillon4-simule.md` | copie de contrôle : brouillon 3 + remplacements (pas un livrable) | `54aee2c2d6516b676fa6852ef3396bce1027494af494cc6aa47f1637b3d47add` |
| `remplacements-cl3.md` | fragment de la section 8 | `19972c5223ba7adacdb1cbdf50307946ab2e907eeb6ee27bc142be86cd4455bf` |
| `sortie-fsck-cl3.txt` | décompte de la sortie du `fsck` (à chaud) | `322413993a770f3a935720f62f0ba96773284b8ab9f9fa2f9f69d09dd0fdd7d4` |
| `../fsck-test.txt` (dossier parent) | sortie complète du `fsck` (première mesure) | `90edf388d033a871d6e22253cc4a47ee80018123c836e1d60ed6880d0ffddb0d` |

L'empreinte de ce rapport est rendue à part (un fichier ne peut pas citer sa propre empreinte).
