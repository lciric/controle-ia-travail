# Vérification des corrections : script de l'expérience de seuil, v2

- Pièce vérifiée : `papiers/D/code/experience_seuil_chantier3_v2.py`, empreinte `d6cd9b1b…850b`, conforme à son `.sha256`, au commit `da5f7a20`. Elle est comparée à la v1 par un diff complet.
- Vérificateur : le contre-lecteur de la v1 (Opus 5.5), 24 novembre 2026. Aucun fichier du dépôt n'a été modifié, `--course` n'a pas été lancé et aucun tirage n'a porté sur la grille.
- Mes essais ont tous porté hors grille : K ∈ {20, 30, 40}, entropie 777, `i_point` ≥ 9000.

## Verdict

**Lançable une fois l'erratum scellé.**

Les défauts 2 à 10 sont corrigés. Je n'ai trouvé aucune régression qui puisse fausser un verdict ou déclencher un arrêt à tort.

Il reste quatre réserves mineures (plus bas), qui ne bloquent pas.

Une condition pour la suite : après l'erratum, la v3 du script ne doit changer que quatre choses :
- `PREREG` ;
- `PREREG_SHA` ;
- les deux valeurs de `VALEURS_CONCEPTION` ;
- la mention de version.

La mère le vérifie par un diff.

## Ce qui est contrôlé

### Rejeux

- `--gardes` de la v2 rejoué : sortie identique à `essai-gardes-bancs-temoins-v2.txt`.
  - Les sept gardes passent : cas sain qui passe, artefact détecté.
  - Il n'y a que les deux défauts attendus du défaut 1 : 2,6678e-5 et 1,21927e-7.
  - Les nouveaux recalculs (Γ_K, 0,0611, nρ₀ = 100, 120) ne déclenchent rien.
- Arithmétique de la grille, rejouée sans tirage avec ε par somme directe :
  - 138 points admissibles, minimum de tours tenus 24, minimum d'audits 2,5 ;
  - le point admissible le plus proche de la frontière garde 20 % de marge ;
  - le contrôle 1 ne signale aucun défaut sur 138 points × 47 marges. Le taux hors bornes, devenu un arrêt, ne se déclenche donc pas à tort.

### État de chaque défaut

**2 — Arrêt n° 6 : corrigé.**
- `Vc_tau2` est calculé.
- `V_tau2` et `Vc_tau2` sont consignés pour les prolongations.
- Une classe finale venue d'une prolongation sensible devient « non concluant ». Une classe venue d'un premier tirage sensible aussi, si elle n'a pas été prolongée.
- J'ai forcé les deux chemins hors grille : V0, V1 et V′1 passent à « non concluant », D1 reste lue, la bissection ne part pas ; une sensibilité de V′ sur la prolongation fait passer V′1 à « non concluant ».
- Lecture retenue : une sensibilité de V ou de V′ rend non concluant le point à cette marge, pour V comme pour V′. C'est la lettre du texte (« le point est non concluant »).

**3 — Clés de graines : corrigé.**
- `res["cles"]` est gardé dans les sorties.
- Le journal des gardes liste les clés employées.
- La config porte le schéma, l'écart d'interprétation des rangs des bancs, la note sur le champ `graines` (« non-employee ») et les deux choix de l'audit renforcé.

**4 — ε : corrigé.**
- La grille calcule ε par la somme directe ; `controle_plan` la compare à la forme fermée au seuil 1e-9.
- Dans `--gardes`, le cas sain compare encore la forme fermée à elle-même. C'est sans effet : l'artefact reste éprouvé par l'injection.

**5 — Garde « valeurs finies, clés, écrasement » : corrigé.**
- `ecrire_resultat` est éprouvé dans une racine temporaire : la première écriture passe, la seconde est refusée.
- Cas sain des clés : un sur-ensemble des clés de la course, toutes acceptées.
- L'exception attendue est restreinte à `GardeArret`.

**6 — Arrêt n° 7 : corrigé.**
- Le script emploie `submit` et `as_completed` avec délai, puis `shutdown(cancel_futures=True)`.
- Réplique autonome : l'arrêt est pris et journalisé à temps. La sortie du processus attend encore la fin des points déjà en cours, plus un point déjà mis en file par processus, pendant quelques minutes au plus. Ce délai est acceptable.

**7 — Journalisation des arrêts : corrigé.**
- Les arrêts n° 3, 4 (dans les points et entre les points) et 7 sont écrits dans `diag/` par `arret()`.
- Un taux hors de $[0,\bar\rho+10^{-12}]$ ou non fini lève désormais l'arrêt n° 4. C'est vrai aussi pour un taux non fini en boucle fermée.

**8 — Prolongation partagée : corrigé.** Les métriques qui ne l'ont pas déclenchée sont marquées « non lue » ; les classes finales ne les emploient pas.

**9 — Audit renforcé : traité par déclaration.** Les deux choix sont inscrits dans la config. Il reste au lecteur, ou à Lazar, de les accepter.

**10 — Sorties descriptives : corrigé.**
- Intervalles à 95 % pour les prolongations, la bissection (chaque itération et la confirmation) et la boucle fermée.
- `indices_proches` dans le contrôle 2 systématique.
- D rapportée à toutes les marges.
- Recalcul des quatre chiffres de conception.
- Commentaire sur le bornage à [0, 1] en boucle fermée.

### Essais hors grille

- `traiter_point` tourne et la sortie se sérialise en JSON.
- 192 clés sont consignées par point.
- Aucun faux défaut d'instrument.

## Réserves mineures restantes (non bloquantes)

1. **Exceptions et arrêts encore hors de `diag/`.**
   - Une exception autre que `GardeArret` venue d'un point (`BrokenProcessPool`, `MemoryError`) n'est pas journalisée.
   - Un `GardeArret` levé dans `gardes()` pendant la course ne l'est pas non plus.
   - Les deux restent bruyants : sans effet sur un verdict.
2. **Points sortis tôt.** Un point qui sort tôt sur un défaut d'instrument n'écrit pas ses clés. La course est alors invalide de toute façon.
3. **Lecture de D hors de λ = 1.** Ailleurs qu'à λ = 1, D est lue contre ε nominal et la trajectoire de la marge du plan. C'est descriptif, mais le lecteur doit le savoir.
4. **Chemin faux dans la docstring.** La docstring renvoie à `papiers/D/audits/contre-lecture-script-seuil-v1/contre-lecture-script-seuil-v1.md`. Le fichier versé est `papiers/D/audits/contre-lecture-script-seuil-v1.md` (R6). À corriger dans la v3.

## Avis sur l'essai de fonctionnement déclaré

L'essai déclaré a tourné sur la configuration K = 50, n = 100, γ = 0,2, η = 10, C = 4, δ = 0,05. C'est le point n° 16 de la grille, tiré avec `i_point` 999.

**Il n'affecte pas la course, à trois conditions.**

**Pourquoi la course n'est pas touchée.**
- Les graines sont disjointes de la course : `i_point` de 0 à 143 pour la grille.
- Le préenregistrement était scellé avant l'essai : prédictions, seuils et critères étaient gelés.
- Le diff v1 → v2 ne contient que les corrections de mes défauts 2 à 10. Aucune ligne ne dépend de ce qui a été vu.
- Le seul nœud ouvert, l'erratum du défaut 1, porte sur l'arithmétique des bancs, pas sur la grille. Ce que l'essai a montré ne donne donc aucune prise pour ajuster quoi que ce soit.
- Ce qui a été vu ne porte que sur 1 point sur 138, va dans le sens prédit et sera retiré, de façon indépendante, par la course.
- Je ne peux pas vérifier par git l'ordre entre l'essai et l'écriture de la v2 : les deux sont dans le même commit. Mais le contenu du diff suffit.

**Conditions.**
1. La déclaration est jointe aux sorties scellées, et le point n° 16 est signalé au lecteur neuf comme « vu avant la course ».
2. Le lecteur neuf n'est pas la fille 2.
3. Aucune autre modification du script n'est faite, en dehors de celles de l'erratum.
