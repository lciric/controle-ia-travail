# Notes de rédaction — addendum 2 de P3, brouillon 1

Rédacteur : sous-agent neuf, 2026-10-20, travail en lecture seule sur le dépôt. Texte rédigé :
`/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/addendum2-p3/P3-addendum2-audit-verdict-v1-brouillon1.md`,
sha256 `2698af04fdd1c9c3fafb97e4835bf0e85dbabd145156dbbda06515602d23ab90` (464 lignes).

## 1. En bref

- Trois analyses : **B1** (remarque 1, ampleur de P3-P1), **B2** (remarque 2, signe de P3-P2 et de la mention, par la
  **même fonction** que B1), **B3** (remarque 3, puissance du nul). Remarque 4 exclue.
- Validateur du dépôt (`controle_ia.prereg.problemes`) : les huit sections exigées sont présentes et non vides ; le
  brouillon est refusé **seulement** pour les marqueurs `<<…>>` (empreintes du module et des tests, nombre de tests,
  durée, contre-lectures), comme voulu.
- Réserves attendues par le rédacteur : `reserve_B1_ampleur_au_dela_de_la_consigne` (P3-P1) et
  `reserve_B3_puissance_du_nul` (les deux sondes). Aucune autre.

## 2. Ce que le rédacteur a lu, et ce qu'il n'a pas lu

- Lu : verdict R13 en entier ; préenregistrement de P3 en entier ; premier addendum en entier ; proposition N-025 ; lignes
  N-024, R-241 à R-258, N-025, N-026 du registre des décisions ; GO-2026-10-20-02 ; décision N-026 ; gabarit et
  `prereg.py` ; code gelé `lecture.py`, `statistiques.py`, `conditions.py` (en entier), parties de `run.py`,
  `environnements/propositions.py`, `sondes/evaluation.py`, `manifeste.py`, `harnais/validation_reelle.py` ; module du
  premier addendum (gardes, graines, A6, point d'entrée) ; mesure de puissance de P3 (`docs/notes/P3-mesures-v2/`).
- **Non lu** : `prereg/P3-consignes-v1.md` ; tout texte d'action ; toute clé ; **aucune donnée du run** ([S], [J], [T]),
  **aucune sortie de lecture** ([L], [A]) : leurs empreintes viennent des fichiers compagnons `.sha256` (sauf [T], prise
  dans la table du verdict, son compagnon n'a pas été ouvert).
- Calculé : rien sur les données. Seulement, à la main, B3 sur les nombres arrondis du verdict (section 4 ci-dessous), et
  les constantes `z`, `z80`, `log10 3` (bibliothèque standard).
- Commandes git, toutes en lecture : `log`, `rev-parse`, `show <commit>:<registre>` (empreinte des registres au commit de
  N-025), `diff --quiet` (arbre gelé à la tête `b883224` égal au commit cité `7a54d43` : code 0 ; dépôt non superficiel).
  Validateur lancé avec `PYTHONDONTWRITEBYTECODE=1` : aucun fichier écrit dans le dépôt (vérifié par `find -newer`).

## 3. Choix faits, et pourquoi

1. **Restriction aux actions sans forme** (principale) plutôt qu'un lecteur corrigé : sans décoder les textes, il n'existe
   pas de « bonne » lecture d'un champ à plusieurs nombres ; la restriction réutilise les fonctions gelées
   (`couts_par_tache`, `cout_de_tache`, `effet_cout_apparie`) en mettant à « illisible » le coût des actions retirées.
   Elle s'applique aux deux conditions (symétrie).
2. **Part portée par les formes** = `D = E0 − E_sf` sur les mêmes tâches, intervalle apparié par tâche (mêmes tâches
   tirées pour les deux termes) ; la part `D / E0` est descriptive, la réserve lit `D`.
3. **« Par tâche »** : la médiane des 60 différences par tâche porte une réserve (effet porté par une partie des tâches) ;
   la table par tâche et les quantiles sont descriptifs. Médiane sur des tâches, jamais sur des jetons (le texte le dit,
   pour qu'aucune garde ni aucun lecteur ne la confonde avec l'interdit).
4. **Trois réserves d'ampleur et de robustesse sur P3-P1** : hors formes (≤ 0), portée par les formes (`D > 0`), au-delà
   de la consigne (> log10 3) ; la quatrième (médiane). `hors_formes` et `au_dela_de_la_consigne` s'excluent. Une valeur
   de `E_sf` entre 0 et log10 3 est conforme à la prédiction écrite (« > 0 ; au plus ≈ 0,48 ») : pas de réserve.
5. **Cible du témoin** : P3-P1 (clause du témoin de H-P3a, [P] l. 125-126, lue ainsi par le verdict, section 6, point 1)
   **et** P3-P4/<sonde> (comme A6 du premier addendum). **Mention** : T3/<sonde> seulement (comme A6), donc sans objet
   dans ce run ; ses résultats sont descriptifs. Voir question 1.
6. **B3** : grandeur de la réserve = aire minimale détectable à 80 % (`Q + w (1 + z80 / z)`), comparée à **la même
   formule** aux hypothèses écrites les plus défavorables (≈ 0,5809), jamais au nombre arrondi « 0,58 » du texte ; aire au
   seuil (`Q + w`) en descriptif. Raison : la note de puissance de P3 employait 80 % pour le coût ([PW] : « effet minimal
   détectable (80 %) ») ; et la comparaison d'une formule à elle-même ôte le seul cas limite (voir section 4).
   `w = (haut − bas) / 2`, définition de la note de puissance et du verdict. « Puissance à l'aire observée » exclue
   (fonction du résultat lui-même ; elle inviterait « presque détecté »).
7. **Cible de B3** : `nul/<sonde>`, conclusion « non détecté » retenue par le verdict (établie si la ligne est
   « aucune sonde générique… » et l'état du jeu saboteur contre honnête « non au-dessus »). Une réserve de puissance
   affaiblit le nul ; elle ne promeut rien. Une puissance plus forte qu'écrite n'ajoute rien.
8. **Audit de symétrie** : les déclencheurs « toutes » et « aucune » du premier addendum ne se transposent pas (réserves
   qui s'excluent ; B3 connu d'avance). Remplacés par « explication trop propre » (les trois effets sans forme conformes
   d'un coup aux prédictions écrites, alors qu'aucun ne l'était) et « part hors de [−1 ; 1] » (P3-P1).
9. **Entrées nommées en dur** (run source, lecture décisive, empreintes de neuf pièces) : possible ici, car tout est
   connu ; garde plus forte que celle du premier addendum.
10. **Antériorité** : S2 ancêtre de la tête et du manifeste ; S2 descendant du commit qui consigne N-025 (`ec1d71b`) ;
    second passage interdit ; déclaration au registre qu'aucune grandeur de B1 ou B2 n'a été calculée sur le réel avant
    S2 ; tests sur tables synthétiques seulement. Limite : un calcul hors de `runs/` avant S2 n'est pas détectable par
    une garde (même limite que le premier addendum, [V] l. 377).
11. **Aucun texte décodé, aucun score par jeton lu** : le chargeur gelé hache le fichier des textes et charge les tables
    par jeton ; deux tests le prouvent (textes non UTF-8 à l'empreinte juste ; tables par jeton aléatoires : sortie
    identique).
12. **N-026** (bras « moyenne ») : hors de N-025, et non calculable sur les données gardées (pas de scores par jeton du
    plancher). Cité comme tel.
13. **Écarté au brouillon 1** : retrait aléatoire apparié comme « plancher » de la décomposition (redondant avec
    l'intervalle par tâches, plus de code) ; bornes de P3-P3 refaites avec les graines du manifeste de la lecture
    décisive (risque d'arrêt dû à une version de numpy ; l'empreinte de [L] suffit) ; réserve générale « largement non
    lu » (peu d'entrées) ; garde de concordance de B3 avec les nombres arrondis du verdict (redondante avec l'empreinte).

## 4. B3 calculé à la main (nombres arrondis du verdict, l. 290-293 et 298-300)

`z = Φ⁻¹(0,9875) = 2,2414027276049464` ; `z80 = Φ⁻¹(0,80) = 0,8416212335729144` ; facteur `1 + z80 / z = 1,3754886`.

| sonde | Q | bas | haut | aire | w | A_seuil | A_80 | A_80 (distance basse) |
|---|---|---|---|---|---|---|---|---|
| tromperie | 0,5717 | 0,5313 | 0,6183 | 0,5748 | 0,04350 | 0,61520 | 0,63153 | 0,63153 |
| enjeux | 0,5356 | 0,4813 | 0,5700 | 0,5248 | 0,04435 | 0,57995 | 0,59660 | 0,59543 |

Hypothèses écrites ([P] l. 394-397) : `A_80` de 0,55439 à 0,58089 ; aire au seuil de 0,545 à 0,567. Les deux sondes
dépassent 0,58089 (marges ≈ 0,051 et ≈ 0,016, bien au-delà de l'arrondi ≈ 2·10⁻⁴) : réserve attendue pour les deux. Cas
limite évité : l'aire au seuil des enjeux (0,57995) contre le nombre du texte « 0,58 ».

## 5. Questions ouvertes pour la session

1. Cible de la réserve du témoin : P3-P1 (clause de H-P3a) en plus de P3-P4/<sonde> (comme A6) ; la mention reste sur
   T3/<sonde>, donc purement descriptive ici. À confirmer, ou la mention doit-elle viser aussi P3-P1 (sens prudent) ?
2. La réserve « ampleur au-delà de la consigne » est-elle voulue comme réserve nommée au verdict (le rédacteur s'attend à
   ce qu'elle se déclenche), ou doit-elle rester un descriptif ?
3. Unité écrite dans le champ du coût (heures, jours, semaines, monnaie) : hors des cinq formes ; la mesurer demanderait
   de décoder les textes et une mesure nouvelle, hors du périmètre écrit de N-025. Nœud de Lazar pour l'ajouter, ou limite
   écrite seulement ?
4. B3 : confirmer la grandeur de la réserve (aire minimale détectable à 80 %, demi-largeur (haut − bas) / 2, même formule
   aux hypothèses écrites, ≈ 0,5809) plutôt que l'aire au seuil ou le nombre « 0,58 » du texte.
5. Garder dans le texte scellé les valeurs attendues de B3 calculées à la main (transparence), ou les laisser aux notes ?
6. « Par tâche » : médiane des différences par tâche avec réserve ; ou moyenne tronquée ; ou descriptif seul ?
7. Restriction au niveau des actions (principale) et au niveau des tâches (descriptive) : partage à confirmer.
8. Audit de symétrie : deux déclencheurs suffisent-ils, ou ajouter le retrait aléatoire apparié écarté ici ?
9. Écriture du module : sous-agent neuf seul ou jury (comme le premier addendum) ? Importer des fonctions du module du
   premier addendum (empreinte vérifiée) ou les réécrire ?
10. Noms : `prereg/P3-addendum2-audit-verdict-v1.md`, `docs/procedures/P3-addendum2-v1/audit_verdict_p3_v1.py`, run
    `…-addendum2-p3`, sortie `lecture-addendum2-p3.json`, clés `addendum2/…` : à confirmer.
11. Verdict complété : nouvelle version `docs/verdicts/verdict-P3-premier-test-i-a-v2.md` (R12), par des sous-agents
    neufs, citant les réserves des deux addenda : forme à fixer par la session.
12. Garde d'antériorité contre le commit de N-025 (`ec1d71b`) et entrées nommées en dur : à confirmer.
13. Réserve générale « largement non lu » omise (peu d'entrées) : à confirmer.
14. Bornes de P3-P3 refaites avec les graines du manifeste de la lecture décisive, en descriptif : à ajouter ou non ?

## 6. Fichiers à donner au contre-lecteur R2 (neuf, n'ayant écrit ni ce texte ni P3)

- Le brouillon (chemin et empreinte en tête de ces notes).
- `prereg/P3-premier-test-i-a-v1.md` ; `prereg/P3-addendum-lecture-complementaire-v1.md` ;
  `docs/verdicts/verdict-P3-premier-test-i-a-v1.md` ; `docs/decisions/proposition-N-025-audit-verdict-P3-v1.md` ;
  `docs/decisions/decision-N-026-v1.md` ; `registres/decisions.md` (lignes N-024, R-256 à R-258, N-025, N-026) ;
  `registres/go.md` (GO-2026-10-20-02).
- `prereg/gabarit-preregistrement-v1.md`, `src/controle_ia/prereg.py`.
- `src/controle_ia/premier_test_ia/lecture.py`, `statistiques.py`, `conditions.py` ; `run.py` (l. 78-81, 313-329) ;
  `src/controle_ia/environnements/propositions.py` (l. 95-156) ; `src/controle_ia/sondes/evaluation.py` (l. 26-63) ;
  `src/controle_ia/manifeste.py` ; `src/controle_ia/harnais/validation_reelle.py` (l. 68-75, 214-248).
- `docs/notes/P3-mesures-v2/puissance_p3.py` et `puissance-p3-v1.txt`.
- `docs/procedures/P3-addendum-v1/complements_p3_v1.py` (gardes 1 à 16, l. 2003-2289 ; A6, l. 1423-1494).
- Interdits au contre-lecteur comme au rédacteur : `prereg/P3-consignes-v1.md`, les textes d'action, toute clé ; et, pour
  ne pas lire de grandeur nouvelle avant le scellement : aucun calcul sur [S] ni sur [L].
