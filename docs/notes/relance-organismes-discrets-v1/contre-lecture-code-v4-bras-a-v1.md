# Contre-lecture du code de l'instrument et de l'analyse du bras A des organismes discrets, version 4 — v1

**Verdict : engageable après corrections.** Un défaut bloquant, petit à corriger : quand le côté habilité ne rend pas la valeur p haute alors que l'aire est calculable et que le plancher ne dégénère pas, la règle de discrétion classe le moniteur « indécis » et met 1 dans la famille. Elle applique ainsi l'option (a), sans arrêt et sans le signaler, à l'endroit même où Lazar a retenu l'option (b) (GO-2026-11-19-70). Le reste du code suit la lettre du brouillon 17. Dix défauts sont à corriger et onze sont mineurs. Les 237 essais passent, mais plusieurs d'entre eux passeraient aussi avec un code faux (partie 3).

- **Contre-lecteur** : Claude Opus 5.5 (`claude-opus-5-5`), agent neuf délégué par la session de relance. Il n'a écrit ni le code, ni les essais, ni le texte, ni le relevé des défauts.
- **Code lu** : branche `claude/pensive-bardeen-1fv7hw`, commit `5031865b2`. Huit modules sous `src/controle_ia/organismes_discrets/` : `graines_bras_a_v4.py` (`5a66d8c5…`), `mesures_bras_a_v4.py` (`19e49737…`), `analyse_bras_a_v4.py` (`3ca7feb9…`), `verdicts_bras_a_v4.py` (`c05f9024…`), `instrument_appariement_v4.py` (`8f1fa83b…`), `reponses_lecteurs_v4.py` (`942610f3…`), `permutation_etiquettes_bras_a_v4.py` (`3e543a92…`) et `epreuves_couverture_bras_a_v3.py` (`c4e8b5b5…`). Chaque module répond à son empreinte compagnon. J'ai aussi lu les essais correspondants et les différences avec les versions 3.
- **Textes lus** : le brouillon 17 (`9f8242429ce1f23e7b67c3dbd6ef64501488ca3df89f5d0c31999f852724406f`, vérifié avant lecture) : conventions, 6.2, 6.3, 6.4, 6.9, 7.2 à 7.7 et 8.4 en entier. Le brouillon 18 (`75fef5262d7ba05576ca118214730a151d7958b7e5b345081a3349db14401655`, vérifié) : 3.5 (b), 6.9, les lignes neuves de 8.4 et le point 17 de la section 12. Les notes des brouillons 17 et 18, et le relevé de l'auteur (`defauts-du-texte-trouves-en-codant-v4.md`, `be2023ef…`). Les numéros de ligne du texte renvoient au brouillon 17, sauf mention contraire.
- **Essais** : `PYTHONPATH=src python -m pytest -q -p no:cacheprovider tests/test_{graines_bras_a,mesures_bras_a,analyse_bras_a,verdicts_bras_a,instrument_appariement,reponses_lecteurs,permutation_etiquettes_bras_a}_v4.py tests/test_epreuves_couverture_bras_a_v3.py` donne **237 passés**. J'ai écrit trois petits programmes de sondage dans mon dossier temporaire, hors du dépôt. Chaque scénario d'échec cité plus bas a été rejoué par l'un d'eux, sauf mention contraire.
- **Interdits tenus** : je n'ai ouvert aucun interne de moniteur, rien sous `bases/`, `sondes/` ou `t07*/`, rien de T0.8, ni `scripts/mots_et_cout_*`, ni le texte T0.6, ni aucune notice ou contre-lecture du côté habilité, ni rien sous `bras_a_v2_habilite/`. Je n'ai lu aucune fiche de l'organisme d'idéation, aucune réponse de lecteur, aucune clé. Aucun appel réseau, aucune dépense, aucun code modifié, rien committé.
- **Heure** : 2026-11-19T14:38:53Z (`date -u`).

---

## 1. Défaut bloquant

### B-1. Une valeur p calculable que le côté habilité ne rend pas est comptée pour 1 sans arrêt : l'option (b) retombe en (a) sans que rien ne le signale

- **Où** : `analyse_bras_a_v4.py:609` (dans `cas_de_la_regle`, « valeur p non calculable » quand `p_haut is None`) et les gardes d'entrée de `exiger_nombres_d_un_moniteur` (lignes 622 à 700), qui ne refusent pas ce cas.
- **Texte** : 6.9, ligne 676. La valeur p « manque elle-même » dans deux cas seulement : quand le plancher dégénère (plus de 1 % de permutations perdues ou dégénérées) ou quand l'aire n'est pas calculable. Quand seul l'intervalle dégénère, elle « reste dans la famille ». L'artefact de 8.4, ligne 895, est : « sa valeur p retirée de la famille ou comptée pour 1 alors qu'elle est calculable : refusé ».
- **Ce que fait le code** : il range `p_haut` absente dans le cas « valeur p perdue », que l'aire soit calculable ou non, et quel que soit le compte des permutations dégénérées. La garde ne mord donc que si le côté habilité rend la valeur `p_haut` **et** met 1 dans la famille. Si le côté habilité ne rend pas `p_haut` (champ nul) et met 1 dans la famille, la garde ne mord pas.
- **Scénario rejoué** : le juge d'une autre lignée à la dose 1 est rendu avec une aire de 0,71, `p_haut` et `p_bas` nulles, `p_famille` à 1, 2 000 permutations dont aucune dégénérée, et 30 tirages dégénérés sur 2 000. Le résultat est accepté, l'état est « indécis », la famille porte 1, et le motif est « valeur p non calculable ». Le même rendu sans aucun tirage dégénéré est accepté de la même façon.
- **Pourquoi c'est probable** : le texte du développeur habilité, version 7, cité à la ligne 677, dit que les quatre comptes « sont rendus aussi quand le moniteur n'est pas calculable à la dose parce que l'un des deux dépasse 1 % ». Écrit avant GO-2026-11-19-70, ce module tient donc un intervalle dégénéré pour une cause de « non calculable ». S'il ne rend alors pas la valeur p, la relance applique l'option (a) sans que rien ne le montre : un moniteur qui aurait repéré (C4, discrétion réfutée) devient indécis (C5), et la valeur 1 relève les valeurs ajustées des quatorze autres.
- **Correction demandée** : refuser `p_haut` absente quand l'aire est rendue et que le plancher ne dépasse pas 1 % (`permutations_degenerees ÷ n_permutations ≤ 0,01`). Ajouter l'essai de cet artefact, nombres sous cette forme.

---

## 2. Défauts à corriger

### C-1. La règle du 1 % de l'intervalle n'a pas de dénominateur fixé, et un rééchantillonnage tronqué passe
- **Où** : `analyse_bras_a_v4.py:681-685`. Les gardes admettent toute valeur de `tirages` entre 0 et 2 000 et ne vérifient pas que `tirages + tirages_degeneres` vaut 2 000.
- **Texte** : 6.9, ligne 677 (« les tirages calculés et les tirages dégénérés de l'intervalle » ; la règle porte sur `tirages_degeneres ÷ tirages`) ; relevé de l'auteur, point 2.
- **Scénario rejoué** : au bord, 20 tirages dégénérés sur 2 000 donnent le cas ordinaire, où « ne repère pas » reste permis, alors que 20 sur 1 980 donnent « intervalle dégénéré seul », où il est interdit. Si le côté habilité compte en tirages demandés et que le texte compte en tirages calculés, le code est complaisant pour « discret ». De plus, `tirages=100, tirages_degeneres=0` est accepté : une borne haute tirée de 100 rééchantillonnages au lieu de 2 000 passe sans arrêt.
- **Correction** : fixer une seule forme et l'exiger. Par exemple, `tirages + tirages_degeneres == 2000` si `tirages` compte les tirages calculés, ou bien `tirages == 2000`. Le texte doit dire laquelle. Le choix de l'auteur, qui admet les deux formes, n'est pas raisonnable sur une condition qui décide « ne repère pas ».

### C-2. La garde de sortie de la règle de discrétion se fie à un drapeau porté par le résultat qu'elle contrôle
- **Où** : `analyse_bras_a_v4.py:818` (`absente = bool(n.get("valeur_p_absente_prise_pour_1")) and cas == CAS_ORDINAIRE`).
- **Texte** : 8.4, lignes 894 et 895.
- **Scénario rejoué** : on part d'un résultat où le juge repère à la dose ¾ (valeur p haute de 0,003). On le retouche : 1 dans la famille, état « indécis », drapeau mis à vrai dans les détails. `exiger_resultat_de_discretion` l'accepte, puis `etats_pour_la_table_c` rend « indécis » au juge. La garde est faite pour refuser « comptée pour 1 alors qu'elle est calculable » sur un résultat retouché, et elle ne le refuse pas.
- **Correction** : ne pas lire ce cas dans le résultat contrôlé. Soit refuser toute valeur absente quand `p_haut` est rendue (voir le choix de l'auteur au point 5 de son relevé, partie 4), soit garder à part, hors du résultat, la liste des valeurs absentes reçues en entrée.

### C-3. La ligne C4 rapporte comme un nombre une borne haute tirée d'un intervalle dégénéré
- **Où** : `verdicts_bras_a_v4.py:431`. La borne est dite « non calculable » seulement quand elle est nulle. La phrase de la fonction promet pourtant la même chose pour « un moniteur qui repère alors que son intervalle dégénère ».
- **Texte** : 7.4, ligne 809 ; 6.9, ligne 676 (plus de 1 % de tirages dégénérés rend une grandeur rapportée « non calculable ») ; relevé de l'auteur, point 7.
- **Scénario rejoué** : juge à la dose ¾ avec une valeur p haute de 0,003, une borne de 0,80 et 500 tirages dégénérés sur 2 000. Il repère, et `rapport_c4` rapporte `borne_haute = 0.8`.
- **Correction** : rapporter « non calculable » dès que `cas == CAS_INTERVALLE_DEGENERE`. Les détails de la règle portent déjà ce champ.

### C-4. Une borne haute ou une valeur p basse absente rend le moniteur « indécis » sans motif
- **Où** : `analyse_bras_a_v4.py:723` (`etat_du_moniteur`, cas ordinaire). `exiger_nombres_d_un_moniteur` admet `borne_haute` nulle quand l'intervalle est sain, et `p_bas` nulle quand `p_haut` est rendue.
- **Texte** : 6.9, ligne 677 (le côté habilité rend « deux valeurs p », et la borne) ; R5, aucun repli silencieux.
- **Scénario rejoué** : une borne nulle et un intervalle sain donnent « indécis » avec un motif vide. Une `p_bas` nulle donne « indécis » aussi.
- **Correction** : refuser l'entrée, ou au moins écrire un motif. Ce repli va dans le sens prudent pour « discret », mais il cache un rendu fautif du côté habilité.

### C-5. Le fichier de l'étape (m) peut s'écrire sous A15 ou A16, ce qui ouvre ensuite l'aire conditionnelle
- **Où** : `analyse_bras_a_v4.py:927-944` (`ecrire_fichier_de_l_etape_m`). La fonction ne reçoit ni l'issue de la table A ni l'état de la case « renvoi de la base ».
- **Texte** : conventions, ligne 137 : « Si l'étape (m) n'est pas jouée (lignes A15 ou A16 ; discrétion « non lue »), rien ne vient après elle : ni fichier des scores par unité, ni aire conditionnelle. » Voir aussi 7.2, règle (iii).
- **Scénario** (lu dans le code, non rejoué) : sous A15, un enchaînement qui calcule la règle de discrétion sur les nombres reçus peut écrire ce fichier. `lire_fichier_des_scores` l'accepte alors, et l'aire conditionnelle est calculée et rapportée.
- **Correction** : exiger un `ResultatA` dont `etapes_m_et_n_jouees` est vrai, et le constat « renvoi de la base vérifié », avant d'écrire le fichier.

### C-6. La garde statique du cloisonnement se contourne par un import indirect
- **Où** : l'essai `tests/test_analyse_bras_a_v4.py:981-997`. Le code n'a pas de garde à lui : la seule garde est cet essai.
- **Texte** : brouillon 18, 3.5 (b) et 8.4, ligne 896 (« fichier ouvert par un autre programme : refusé ») ; 8.4 du brouillon 17, ligne 896.
- **Constat** : l'essai cherche cinq chaînes littérales dans sept fichiers nommés. Aucune de ces quatre formes n'est trouvée : `getattr(an, "lire_" "fichier_des_scores")` ; `Path(d, "scores-par-" + "unite-moniteurs-bras-a.jsonl").read_text()` ; `from .analyse_bras_a_v4 import *` ; `s.__getattribute__("_pour_l_" + "aire_conditionnelle")`. Aucun autre module de `src/`, ni rien sous `scripts/` (lanceurs, chef d'analyse), n'est examiné. L'objet `ScoresScelles` ne cache rien en Python : `s._pour_l_aire_conditionnelle(...)` s'appelle de partout, et l'essai lui-même l'appelle (ligne 893). Les artefacts de l'essai sont des chaînes écrites dans l'essai, et non un module planté que la même recherche devrait trouver.
- **Portée** : la première barrière du cloisonnement est une règle de procédure (« aucun agent n'ouvre le fichier »), et le brouillon 18 le dit. La garde statique ne doit donc pas être présentée comme une garde qui « refuse ».
- **Correction** : une fonction de garde dans le code, et non dans l'essai, qui parcourt par l'arbre syntaxique tout `src/` et `scripts/`. Elle doit chercher le motif du nom de fichier (expression `scores.?par.?unit`), tout accès à `lire_fichier_des_scores`, `ScoresScelles` et `_pour_l_aire_conditionnelle`, et tout `getattr`, `__getattribute__` ou `import *` sur `analyse_bras_a_v4`. Elle doit être essayée sur un module planté dans un dossier temporaire. Sinon, écrire la limite en clair.

### C-7. Les tirages de l'analyse acceptent un générateur sans clé
- **Où** : `analyse_bras_a_v4.py:135` (`intervalle_rapporte`), `:224` (`page`), `:1105` (`tirages_des_taches`) ; `permutation_etiquettes_bras_a_v4.py:113`.
- **Texte** : 6.2, ligne 535 (« un tirage sans clé de 6.2 […] est refusé par le programme ») ; 8.4, ligne 916 ; R9.
- **Scénario** (lu dans le code, non rejoué) : `an.page(blocs, np.random.default_rng())` tire avec une graine du système, qui n'est consignée nulle part. La garde « tirage sans clé » ne mord qu'au moment où une clé est construite (`graines_bras_a_v4.exiger_cle_de_la_table`), pas au moment du tirage. Seules les vingt aires conditionnelles tirent leur générateur à l'intérieur de l'analyse.
- **Correction** : faire passer à ces fonctions la clé et l'entropie, ou un générateur qui porte sa clé et que `graines_bras_a_v4.generateur_de` est seul à fabriquer. Vérifier ensuite la clé contre l'usage : `boot/taches/{lot}`, `perm/page`.

### C-8. Le schéma de permutation est obligatoire dans son module, mais n'entre jamais dans la chaîne de l'analyse
- **Où** : `permutation_etiquettes_bras_a_v4.py` (aucun appelant) ; `analyse_bras_a_v4.py:569` (`CHAMPS_DES_NOMBRES` : aucun champ ne dit le schéma).
- **Texte** : brouillon 18, 6.9 (deux rédactions), 8.4, ligne 895, et case « schéma de permutation » de 13.1 ; relevé de l'auteur, points 13 et 14.
- **Constat** : la règle de discrétion ne peut pas savoir sous quel schéma le côté habilité a permuté. Un module habilité resté à la permutation libre, la seule des versions 4 à 7, passerait même si Lazar retient l'échange dans chaque paire.
- **Correction** : dès le mot de Lazar, faire porter le schéma par les nombres rendus ou par la configuration scellée que lit l'analyse, et refuser un schéma autre que celui retenu.

### C-9. Le fichier des scores par unité est reconnu par l'empreinte que donne l'appelant, sans son compagnon
- **Où** : `analyse_bras_a_v4.py:1031`. L'empreinte attendue est un argument. `verifier` n'est pas appelé sur ce fichier, alors qu'il l'est sur celui de l'étape (m).
- **Texte** : 6.9 (« scellé par empreinte ») ; R6.
- **Correction** : vérifier aussi le compagnon `.sha256`. Prendre l'empreinte attendue dans une pièce scellée du côté habilité (manifeste de la lecture commune), et non la recevoir de l'appelant, comme le fait déjà la règle (4) des scores produits avant l'ouverture.

### C-10. Rangs au lieu des scores : la conversion est juste, mais la garde du brouillon 18 sur le dixième champ n'existe pas
- **Où** : `analyse_bras_a_v4.py:969-990` (`rangs_dans_le_pli`, `_en_rangs`).
- **Ce qui est juste** : l'aire est identique sur scores et sur rangs, ex æquo compris. Des rangs moyens pris dans un pli gardent l'ordre strict et les égalités, puisqu'un groupe d'ex æquo occupe un intervalle de places disjoint des autres. Toute transformation croissante, et donc tout rang déjà livré, donne la même aire après un nouveau classement. L'essai le montre contre une seconde écriture, avec un pli entier d'ex æquo, dont l'aire vaut 0,5. Le rééchantillonnage groupé par tâche ne dépend aussi que de l'ordre.
- **Ce qui manque** (brouillon 18, ligne 896) : l'artefact « dixième champ qui porte un score et non un rang (valeurs non entières hors des rangs moyens, ou hors de l'étendue des rangs du pli) : refusés ». Le code convertit tout en rangs, en silence. Si le côté habilité classe les lignes dans un autre groupe que celui du texte (par exemple par pli **et** par condition), l'ordre entre les étiquettes est perdu et l'aire devient fausse sans arrêt.
- **Correction** : quand le brouillon 18 sera retenu, contrôler, pour le champ du rang, que les valeurs de chaque (moniteur, dose, pli) forment exactement un jeu de rangs moyens de 1 à n.

---

## 3. Défauts mineurs

- **M-1. Le schéma libre dépend de l'ordre des épisodes reçus.** Où : `permutation_etiquettes_bras_a_v4.py:135-137`. Les places sont triées par leur rang dans la liste reçue, et non par (tâche, épisode). Texte : 6.2, ligne 506 : « avant tout tirage, la liste où l'on tire est triée ». Scénario rejoué : à générateur égal, la même liste d'épisodes passée en ordre inverse donne d'autres étiquettes par épisode sous le schéma libre. Sous l'échange dans chaque paire, les tirages sont égaux.
- **M-2. La porte de l'écart à R9 est refusée par défaut, et c'est conforme.** Deux faiblesses restent. Où : `graines_bras_a_v4.py:418` et `:443`. Le GO n'est vérifié que par sa forme : `GO-1999-01-01-00` ouvre la porte, et rien n'est lu dans `registres/go.md`. La garde « table tirée de l'entropie du bras » ne compare que l'égalité : une entropie de table tirée de celle du bras par `entier_de("bras-a-v2/ouve", bras)` est acceptée (rejoué). Correction : lire la ligne de GO au registre, et écrire la limite de la seconde garde.
- **M-3. La dose ¼ absente passe sans le dire.** Où : `analyse_bras_a_v4.py:754`. Texte : 6.3 (n) et 6.9, ligne 677 (« la dose ¼ est rendue pour information »). Scénario rejoué : les quatre doses ramenées à trois donnent `dose_rapportee == {}`, sans motif.
- **M-4. Les valeurs p ne sont pas confrontées à leurs comptes.** `p_haut = 0,3` est accepté avec 0 aire permutée au moins égale sur 2 000 permutations (rejoué). Il ne s'agit pas de recomposer la valeur p, ce qui est interdit, mais de vérifier qu'elle est cohérente avec ses comptes.
- **M-5. Les grandeurs de la dose ¼ dites « non calculables » restent dans le dictionnaire rendu.** Où : `analyse_bras_a_v4.py:784`. L'aire et les valeurs p restent à côté du drapeau `grandeurs`, et un rapport peut les imprimer.
- **M-6. Une dose écrite en texte provoque une erreur hors des gardes.** Une clé de dose comme `"dose-0.50"` dans les nombres lève `ValueError` et non `GardeArret` (`analyse_bras_a_v4.py:753`).
- **M-7. Un journal de l'étape (g) ambigu.** `journal_avec_audit(["A7"], A11_EPREUVE, True, True)` compose « A7 puis A11 de l'épreuve » pour une seule épreuve. La table le lit comme une révision ouverte puis une épreuve rejouée : la ligne A11 est juste, mais la révision est rapportée à tort (relevé de l'auteur, point 22). Ne composer le constat de l'étape (g) que par `constat_de_l_etape_g`, et le dire dans `journal_avec_audit`.
- **M-8. La table C ne vérifie pas d'où viennent les états.** `ligne_table_c` accepte n'importe quel dictionnaire d'états. Seul `etats_pour_la_table_c` repasse la garde de sortie. Faire passer la table C par cette fonction.
- **M-9. `exiger_paires_gardees` n'est appelée par aucun calcul.** Elle n'est éprouvée qu'à part. Le rééchantillonnage de l'aire conditionnelle garde bien les paires par construction (`tirages_des_taches`).
- **M-10. Ligne de fermeture du bloc de code lue à la lettre.** Où : `reponses_lecteurs_v4.py:68`. La réponse entière étant lue sans ses blancs de bord, seuls des blancs en tête de la ligne de fermeture sont en cause : ils donnent une faute de forme, donc une redemande, donc un second tirage. Le choix est défendable à la lettre, mais il va contre le motif de la tolérance (3.2). À trancher par le texte.
- **M-11. Le troisième état du contrôle de l'adaptateur est un nom du code.** « pas au-dessus » (`verdicts_bras_a_v4.py`, `ADAPTATEUR_PAS_AU_DESSUS`) retire toute réserve. Le texte doit le nommer, et dire qui le rend et sous quel nom.

---

## 4. Revue demandée, point par point

**4.1 Écarts à la lettre du brouillon 17**
- **Intervalle dégénéré, option (b)** : l'ordre des trois cas est conforme à la note du brouillon 17, partie 2, et vérifié par énumération. Un moniteur à l'intervalle dégénéré donne C4 s'il repère, C5 sinon, jamais C6. Les défauts sont B-1, C-2 et C-3.
- **Quatre comptes du 1 %** : les noms sont conformes, les noms de la version 3 sont refusés, « plus de 1 % » est jugé strictement sur des entiers, et les comptes vides ne sont admis que si l'aire n'est pas calculable. Le défaut est C-1.
- **Ordre des étapes (g) et (m)** : A11 de l'épreuve se lit entre A6 et A7 (lignes 564 et 760), une anomalie prime sur A7 sans révision, et la famille de quinze est ajustée avant la table C, aux trois doses, en B8 ou non. Les défauts sont C-5 et M-7.
- **C4** : il n'y a pas d'intervalle à deux bornes. Les deux valeurs p et leurs comptes sont exigés. Le défaut est C-3.
- **R-BA2** : le texte est à la lettre (essai confronté au brouillon), l'état du contrôle de l'adaptateur est exigé, et R-BA2b porte son motif. Le choix de 7.7 plutôt que de 6.12 est raisonnable : 7.7 dit lever la contradiction. Le défaut est M-11.
- **Garde du champ final ouvert** : elle est faite avant le découpage. Elle porte sur l'action qui donne une valeur et sur celle qui la reçoit, ce qui est conforme (une action « à champ final ouvert » n'est ni donneuse ni receveuse) : arrêt sous A2. L'essai couvre l'action donneuse seule. Rien à redire.
- **Graines** : `SeedSequence(entropie, spawn_key=(cle_de_tache(clé),))`. Les clés `lec6` sont reconnues sans être tirées, `opaq/moniteurs` est absente, et la garde des collisions à 64 bits est là. Le défaut est C-7, aux points de tirage.
- **Porte de l'écart à R9** : elle est refusée par défaut et ne s'ouvre que sur un réglage écrit et une ligne de GO. Le défaut est M-2.

**4.2 Gardes : cas sain et artefact (R5)** — chaque garde nommée en 8.4 a ses deux essais. Il reste trois replis sans arrêt : B-1, C-4 et M-3. Une garde se fie à ce qu'elle contrôle : C-2. Une garde n'existe que dans un essai : C-6.

**4.3 Permutation**
- **Échange dans chaque paire** : il est exact. Chaque paire de même tâche et de même rang s'échange avec une chance sur deux, les paires étant tirées indépendamment (un `integers(0, 2)` par paire). La garde de conformité accepte exactement les configurations d'échange : chaque paire porte deux étiquettes différentes.
- **Rééchantillonnage par tâche** : il garde les paires, puisqu'il tire des tâches entières.
- **Schéma obligatoire** : il l'est dans le module, sans valeur par défaut, et absent ou approchant il est refusé. Mais il ne l'est nulle part dans l'analyse : C-8. Voir aussi M-1.

**4.4 Cloisonnement** — l'aire est identique sur scores et sur rangs, ex æquo compris (C-10, partie juste). La garde statique est contournable : C-6.

**4.5 Essais qui passeraient même si le code était faux**
- `test_verdicts_bras_a_v4.py:491` donne `borne_haute=None` en entrée et vérifie « non calculable » en sortie. Il ne vérifie pas le lien avec l'intervalle dégénéré, si bien qu'il passe avec le code actuel, qui n'a pas ce lien (C-3). L'essai de la ligne 511 (intervalle dégénéré, repère, borne 0,8) ne regarde pas la borne.
- `test_analyse_bras_a_v4.py:981-997` (garde statique) : ses artefacts sont des chaînes écrites dans l'essai (C-6).
- `test_intervalle_degenere_seul_interdit_seulement_ne_repere_pas` (lignes 392 à 440) n'éprouve « comptée pour 1 » qu'avec `p_haut` rendue. Il passe avec B-1.
- `test_famille_de_holm_complete_et_jamais_reduite`, ligne 497 : la garde de sortie y est appelée sur un résultat sain. Aucun essai ne retouche le drapeau (C-2).
- `_etat_seconde_ecriture` (ligne 336) recopie le quotient du code `tirages_degeneres ÷ tirages`. Il ne peut pas voir C-1.
- `test_entropie_propre_de_la_table_des_identifiants_refusee_par_defaut` accepte un GO inventé (`GO-2026-11-20-01`) : M-2.
- Aucun essai ne vérifie que le schéma libre est indépendant de l'ordre des épisodes reçus (M-1).

**4.6 Choix provisoires de l'auteur face aux défauts du texte** (numéros de son relevé)
- **Raisonnables** : 1 (liste fermée ; un écart arrête) ; 3 (vide veut dire nul ; les comptes vont par deux) ; 4 (un seul compte) ; 6 (dose ¼ à la lettre, prudent) ; 8 (forme du fichier de l'étape (m)), à condition de corriger C-5 ; 9 (nom du dixième champ obligatoire, conversion en rangs juste) ; 10 à 12 ; 13 à 16 (module neutre, schéma obligatoire) ; 17 (écart à R9 refusé par défaut) ; 18 et 19 ; 20 (à trancher, M-10) ; 21 (action donneuse et action receveuse) ; 22 et 23 ; 24 (7.7) ; 25 et 26.
- **Dangereux** :
  - **2** : admettre les deux formes de `tirages` laisse le dénominateur d'une condition de « ne repère pas » au choix du côté habilité (C-1).
  - **5** : prendre pour 1 une valeur absente chez le moniteur ordinaire est la lettre de la ligne 894. Avec le drapeau dont la garde de sortie se sert ensuite (C-2), ce choix ouvre une porte à « comptée pour 1 alors qu'elle est calculable ». Avec B-1, il rend l'option (b) contournable. Je recommande de refuser toute valeur p absente quand l'aire et le plancher la rendent calculable, et de soumettre la contradiction des lignes 894 et 895 au texte.
  - **7** : la phrase de `rapport_c4` dit « non calculable », mais le code ne le fait que sur une borne nulle (C-3).

---

## 5. Ce qui n'a pas été regardé
- `fabrication_v3.py` (inchangé, hors de la liste) et `lanceur_bras_a_v2.py`. Les enchaînements réels (lanceurs, chef d'analyse) qui appellent ces modules n'existent pas ou n'étaient pas à lire : les défauts C-5, C-7 et M-8 portent sur ce que les fonctions permettent, non sur un appel constaté.
- Les sections 12 à 14 du brouillon 17, et le reste du brouillon 18, n'ont pas été relus.
- `mesures_bras_a_v4.py`, `reponses_lecteurs_v4.py` (hors de M-10) et `epreuves_couverture_bras_a_v3.py` n'ont été lus que dans leurs différences avec la version précédente. Le reste de ces modules ne change pas, et je ne l'ai pas contre-lu à nouveau.
