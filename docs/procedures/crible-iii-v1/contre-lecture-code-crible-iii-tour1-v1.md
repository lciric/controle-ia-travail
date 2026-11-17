# Contre-lecture du code du crible (iii), tour 1, v1

- **Lecteur** : sous-agent neuf, lecteur C ; il n'a écrit ni la pièce, ni le code, ni le rapport (auteur : modèle A). Écrit le 2026-11-17T01:45:43Z (`date -u`).
- **Pièces lues** : `rapport-crible-iii-v1.md` (`aac9c95c…`), `procedure-machine-crible-iii-v1.md` (`d753c35a…`), les cinq fichiers du crible, l'amorce, le
  programme machine et son aide, l'outil et les gardes de la session, les essais, le banc de mutations, l'essai à blanc, le texte qui fait foi
  (`91b4bf30…`, sections Hypothèse, Métrique, Seuil, Plan d'analyse, Critères de lecture, Liste d'arrêt, Devis, Lignes de GO). Les 46 compagnons
  `.sha256` du dossier sont égaux (`verifier-arbre` : arbre intact) ; les empreintes du rapport et de la procédure sont celles des fichiers.
- **Interdits tenus** : aucune machine, aucun appel au loueur ni à un fournisseur de modèles, aucune clé, aucune dépense ; issue du pilote non ouverte ;
  aucune branche `calcul/pilote-mr2-v74-entree-*` ouverte (le nom de l'une d'elles est paru dans `git branch -a`, rien de plus) ; rien sous `diag/`, `runs/`,
  `donnees/` ; aucun fichier existant modifié ; rien de committé.

## Verdict : **corrections** (2 majeures, 4 mineures ; aucune ne met la conception en cause)

Le code fait ce que la pièce fixe : files (monde r vers la file r modulo 5), ordre par monde (S, passe 1 et H ensemble ; puis D et B), bornes de 3 000 s et
7 200 s, garde de départ de 10 h, filtre (doublons, archive, ordre des noms, maximin de Jaccard, égalités par l'ordre), tirage de H sous `(r, 40)`,
gabarits G1 et G2, comptes de dollars (passe 1 dans D et dans B), niveaux 97,5 % pour P1 et P2, étages 0 à 7. Les essais se rejouent. Les deux défauts
majeurs sont des **replis silencieux** (R5) que les essais du rapport ne couvrent pas ; je les ai reproduits.

## 1. Rejeux (par moi, sur ce dépôt)

- **Niveau A** : 42 cas, 42 passés (sortie égale à la sortie gardée, hors l'en-tête de date).
- **Banc de mutations** : deux passages. Premier passage, lancé pendant que le disque du conteneur était plein (voir incidents) : 30 tuées, 5 « survivantes »
  (« exception des essais », donc tuées par une autre cause que l'attendue). Les cinq, rejouées à part : toutes tuées pour la raison attendue.
  **Second passage complet : 35 mutations sur 35 tuées pour la raison attendue, original à 0 échec.** Le résultat du rapport est confirmé ; le banc est sensible aux
  ressources de la machine (un échec d'écriture donne « survivante », ce qui est le bon sens du refus).
- **Essai à blanc complet** : arbre dépaqueté de `e3d83e47…`, relevé `f56d9c0e…`, mondes de développement `4036f512…`, interpréteur numpy 2.5.3 : **25 cas sur 25
  conformes, 843 s**. Les gardes du mode réel passent sous numpy 2.5.3.
- **Non rejoué** : la répétition de la machine (14 cas) ; je n'ai relu que sa sortie gardée et l'amorce, le programme machine, l'outil de la session.
- **Cas neuf joué** (sans appel, relais factices) : `generer --public --un-seul` (jamais éprouvé par le rapport : l'essai à blanc emploie le fichier de vingt mondes répétés)
  produit un monde conforme, et `sonde-gabarits --mode a_blanc` le lit et rend trois appels, III-7 calculée. Ce chemin est donc sain.

## 2. Corrections exigées

### Majeure 1 — une exception dans un fil est avalée : appel perdu du relevé, aucun arrêt

**Reproduit.** Gardien qui lève sur un seul appel (H du monde 3), appeleur factice : `jouer_crible` rend `arret = None`, 19 mondes complets, **99 appels listés
sur 100 faits** (dépense réglée pour 100) ; seul un `Traceback` part sur la sortie d'erreur. L'appel perdu n'est ni dans `appels`, ni dans `CARTES.json` : ses dollars
disparaissent de la mesure, le monde est « incomplet » sans cause, et le lanceur sort en code 0. Même effet pour toute exception dans `jouer_monde` (analyseur, filtre,
construction des textes) : le fil meurt, la file s'arrête, les mondes suivants de la file restent « non commencés » sans arrêt. La liste d'arrêt dit « aucun repli silencieux » ;
le docstring de `jouer_crible` dit « aucune exception ne sort après le premier appel » (vrai, mais parce qu'elle est perdue).

Couples (fichier `crible_iii_v1.py`) :

```
ancien :
        if r_appel.get("etat") in ("complet", "tronque") and bras != "P1":
            cs, lecture = gardien(r, bras, p, r_appel.get("texte") or "")
nouveau :
        if r_appel.get("etat") in ("complet", "tronque") and bras != "P1":
            try:
                cs, lecture = gardien(r, bras, p, r_appel.get("texte") or "")
            except Exception as e:  # noqa: BLE001 — jamais un repli silencieux : arrêt (code 3), l'appel reste au relevé
                c.arreter("exception du gardien", f"monde {r}, {bras} : {type(e).__name__} : {e}", 3)
                cs, lecture = [], f"gardien en exception : {type(e).__name__}"
```

```
ancien :
            jouer_monde(r, file)
nouveau :
            try:
                jouer_monde(r, file)
            except Exception as e:  # noqa: BLE001 — jamais un repli silencieux : arrêt (code 3), monde compté incomplet
                c.arreter("exception d'un monde", f"monde {r} : {type(e).__name__} : {e}", 3)
                with c.verrou:
                    c.mondes[r] = "incomplet"
                return
```

À ajouter aux essais du niveau A (R5, cas sain et artefact) : « gardien en exception » (sain : gardien conforme ; artefact : gardien qui lève, attendu : arrêt code 3, 100 appels listés)
et « exception dans le monde » (filtre qui lève : arrêt code 3, aucune file muette) ; une mutation du banc qui retire chacun des deux `try`.

### Majeure 2 — la sonde des gabarits (κiii0) passe « saine » quand un appel sous G2 n'a rien rendu

**Reproduit** (sonde à blanc sur le monde public 1, relais factices) : avec D en panne (`echec`) et B illisible (aucune carte admise), le relevé rend
`regles_d_avance : {declenchee: false, motifs: []}`, code 0. Les trois règles de la pièce (G2 tronqué, carte non évaluable, aucune liste sous G1) ne regardent que
les appels tronqués et les cartes admises ; un appel en échec n'a ni carte non évaluable ni tronquage. La sonde est le seul garde de G2 avant 260 USD : un « non
déclenchée » avec G2 non éprouvé est le faux sain à exclure (R4, R5). L'attendu de la procédure (geste 0) ne demande que « non déclenchée, trois appels ».

Couples :

```
ancien (lanceur_crible_iii_v1.py) :
                r = un(bras, t2)
                if r.get("etat") == "tronque":
                    regles.append(f"appel sous G2 tronqué ({bras}) : gabarit réécrit, crible non lancé")
nouveau :
                r = un(bras, t2)
                if r.get("etat") == "tronque":
                    regles.append(f"appel sous G2 tronqué ({bras}) : gabarit réécrit, crible non lancé")
                elif r.get("etat") != "complet":
                    regles.append(f"appel sous G2 non rendu ({bras}, état {r.get('etat')}) : G2 non éprouvé, sonde à refaire, crible non lancé")
                elif appels[-1]["cartes_admises"] == 0:
                    regles.append(f"aucune carte admise sous G2 ({bras}) : G2 non éprouvé, sonde à refaire, crible non lancé")
```

```
ancien (procedure-machine-crible-iii-v1.md) :
Attendu :
   `regles_d_avance` non déclenchée, trois appels.
nouveau :
Attendu :
   `regles_d_avance` non déclenchée, trois appels tous à l'état `complet`, des cartes admises sous chacun des deux appels sous G2.
```

Essais à ajouter (niveau B, déjà un cadre : `sonde` de l'essai à blanc) : D en panne ; B illisible ; chacun doit déclencher la règle. Sain : le cas existant.

### Mineure 3 — un arrêt réel arrivé après la ligne du minimum est perdu

`c.arret` garde le premier arrêt. La ligne du minimum (code 0) l'occupe ; un arrêt réel qui suit (témoin absent, coût au-dessus du pire cas, part atteinte, limite de débit)
d'un appel encore en vol est ignoré : le lanceur sort en code 0, la mesure tourne, la lecture dit « non concluant » (étage 1) au lieu de « non jugeable (arrêt) » (étage 0, que
la pièce met avant). Au taux de tronquage du pilote, la ligne du minimum est presque sûre de se déclencher avec quatre files encore en vol : le cas n'est pas théorique. Effet
sur le résultat scientifique faible (non concluant dans les deux cas), mais la cause grave disparaît du relevé.

Couples (`crible_iii_v1.py`) :

```
ancien :
            if arret is not None and c.arret is None:
nouveau :
            if arret is not None and (c.arret is None or c.arret.get("ligne") == "minimum"):
```
```
ancien :
            if n >= APPELS_MIN_LIMITE and k / n > TAUX_LIMITE_DEBIT and c.arret is None:
nouveau :
            if n >= APPELS_MIN_LIMITE and k / n > TAUX_LIMITE_DEBIT and (c.arret is None or c.arret.get("ligne") == "minimum"):
```
```
ancien :
            if c.regle[p] >= c.parts[p] - EPS and c.arret is None:
nouveau :
            if c.regle[p] >= c.parts[p] - EPS and (c.arret is None or c.arret.get("ligne") == "minimum"):
```
```
ancien :
        with self.verrou:
            if self.arret is None:
                self.arret = {"ligne": ligne, "motif": motif, "code": code}
nouveau :
        with self.verrou:
            if self.arret is None or (self.arret.get("ligne") == "minimum" and ligne != "minimum"):
                self.arret = {"ligne": ligne, "motif": motif, "code": code}
```

Essai à ajouter : minimum déclenché, puis un témoin supprimé sur un appel encore en vol : attendu arrêt `réponse brute ou témoin absent`, code 3 (sain : le même sans l'appel défaillant, arrêt « minimum », code 0).

### Mineure 4 — la préparation réelle des mondes n'est pas gardée par le banc (point que le rapport demande de relire)

Le retrait de l'effet de K1 (`comptees = certifiees − {eid_k1} − k1_tau`, `OutilsMR2.preparer`) est la définition qui décide de tout ce que la mesure compte ; les essais du niveau A
emploient des outils factices, et la mutation « intersection retirée » ne touche que `couvertures`. Ajouter un cas du niveau B (arbre réel, mondes de développement) qui
affirme, pour chaque monde, `eid_k1 ∉ comptees`, `comptees ∩ k1_tau = ∅` et `comptees ⊆ certifiees`, puis une mutation (retrait de `- {eid_k1} - k1_tau`) tuée par ce cas.
Pas de couple : c'est du code d'essai neuf.

### Mineure 5 — la garde « texte servi de passe 2 » est tautologique, H n'est pas gardé

`td` et `tb` sont bâtis par `texte_g2`, puis comparés à `texte_g2` : la garde ne peut pas échouer en production (les essais la jouent avec un texte forcé) ; le texte de H n'est
vérifié nulle part. La défense réelle est l'empreinte `texte_servi_sha256` au relevé (audit R4) et la relecture des corps de relais à l'essai à blanc. Acceptable, mais le
rapport ne doit pas la présenter comme une garde de production : une phrase à corriger au § 2 du rapport (`texte de B égal à l'octet à celui de D`) ou, mieux, comparer l'octet envoyé
au relais (déjà dans `corps-relais.json`) à `texte_servi_sha256` dans `fabriquer_appeler`. Au choix de la mère ; si seule la phrase est changée, couple libre.

### Mineure 6 — rapport et procédure : deux phrases à tenir

- Le rapport (§ 3) dit « le banc de mutations … 35 tuées » sans dire qu'une tuée par exception compte comme survivante ; le dire en une phrase (comportement correct, vu en rejeu).
- La procédure (§ 5) dit que la concurrence réelle n'est pas éprouvée ; l'ajouter à l'attendu de la sonde est impossible (une seule session), mais le dire dans le préavis à Lazar est conforme.

## 3. Remarques facultatives (aucune ne conditionne le scellement)

- L'analyseur accepte aussi `{"ensembles": […]}` : plus large que « liste JSON de listes d'entiers » de la pièce ; gelé tel quel, sans conséquence si le rapport le dit.
- La sonde ne tire qu'**un** appel de Pr-4 sous G2 : un seul tirage ne sépare pas un taux de tronquage de 0,50 (vu au pilote, sous G0) d'un taux de 0,05. Elle rend pourtant
  la décision la plus chère du dossier (voir § 4, point 1). Un second appel de Pr-4 sous G2 coûterait au plus 3 USD de plus (plafond κiii0 à 10 USD) : à proposer à Lazar, non à imposer.
- `modèle servi différent → arrêt code 3`, aucune relance sur un code 2, aucun abandon de proposeur : choix déclarés du rapport (§ 5) ; je les valide (la pièce ne prévoit ni reprise ni bascule).
- Cartes au-delà du k-ième ensemble valides pour la couverture, hors du dénominateur de E : conforme à la définition « emplacement ≤ 6 » de la pièce.
- Procédure tapable : les onze arguments de `commande`, l'échéance de 17 h (61 200 s) contre l'amorce (17 h 05, 61 500 s), les prix (0,15 puis 0,17 USD/h, soit 2,89 USD au pire sous les 3 USD)
  se recoupent. Leçons de l'idée 1.1 reprises : offre par la garde, amorce compressée, réponse du loueur à part, reprise de la poussée (`attente_finale`), minuterie (DELETE répétés, « stopped »
  après cinq), destruction par l'identifiant avec preuve d'absence par témoins, feu d'arrêt arrêtant le lanceur par son PID.
- Aucune valeur de clé ni identifiant de modèle dans le dossier (recherche sur les motifs de noms de modèles et de clés : seuls les **noms** de variables et l'hôte du fournisseur). Le seul texte
  « create instance » est dans l'outil de la session, via la variable du chemin de l'outil du loueur, imprimé et non joué : conforme à la procédure.

## 4. Pour la mère

1. **Nœud déjà signalé, confirmé par mon calcul** : probabilité d'atteindre 16 mondes complets au taux du pilote (monde complet 0,75⁵ = 0,237) ≈ 1,7 × 10⁻⁷ ; la ligne du minimum s'arrête vers dix mondes et
   ≈ 78 USD. Lancer κiii1 dans cet état revient à dépenser ≈ 78 USD pour un « non concluant » presque certain, **sauf** si G2 (six cartes courtes) tronque bien moins que G0. Seule la sonde le dit, et avec un seul appel de Pr-4 (remarque ci-dessus).
2. Les deux majeures changent `crible_iii_v1.py` et `lanceur_crible_iii_v1.py` donc leurs empreintes, celles de la procédure et du rapport, et l'addendum à venir : une version suivante de ces pièces par A, puis un tour différentiel (les couples sont écrits, aucun effet sur la pièce qui fait foi ni sur ses prédictions).
3. Le banc de mutations et les essais doivent être rejoués par A après correction (35 mutations + celles des majeures 1 et 3).
4. Rien dans le code n'empêche un lancement avant le 21 : les préalables restent, dans l'ordre du rapport, la sonde (avec la règle de la majeure 2), la version 2, le scellement, l'addendum, les lignes, le feu, le mot de Lazar.
5. Le disque du conteneur de la session est à 97 % (1,4 Go libres) : un essai à blanc ou un banc de mutations lancé à ce niveau peut échouer pour une cause étrangère au code.

## 5. Incidents de ma main

- Une première commande a échoué (« disque plein », 0 Mo libres sur le volume de `/tmp/claude-0`) ; rejouée aussitôt, passée. Le premier passage du banc de mutations (5 « survivantes ») date de cet épisode ; rejeu complet sans écart ensuite.
- J'ai écrit mes fichiers de travail sous `/tmp/claude-0-cl` (hors du dossier prévu pour les fichiers de session) ; supprimés en fin de tâche. Aucun fichier à la racine `/`.
- Lectures seules, sans modification, dans le dossier de session de la mère : l'arbre dépaqueté (`605e0f6`, paquet `e3d83e47…` vérifié), le fichier des mondes de développement (`4036f512…`) et le relevé de la sonde (`f56d9c0e…`), tous trois vérifiés par empreinte.
- Les relais factices ont occupé les ports locaux 8811 et 8812 pendant l'essai à blanc et la sonde à blanc ; arrêtés par le lanceur. Un processus d'une autre session (« crible (v) ») tournait en même temps ; non touché.
- Git : lecture seule (`cat-file -s`, `ls-tree`, `log -1` dans l'arbre dépaqueté, `branch -a`). Aucun fetch, aucun commit.
