# Relecture courte — préenregistrement de l'épreuve sur l'héritage, palier 0b, version 5 (erratum) — v1

- Auteur : le même contre-lecteur, modèle O. Pièce de travail (classe C). La relecture se limite à mes quatre corrections (relecture de la version 4, `4cc14afe…`, § 6) et aux écarts que le rédacteur me demande de trancher.
- Date : vers 23:55Z le 2026-11-19 (`date -u`).
- Conditions : processeur seul, sans appel de modèle ni dépense ; réseau limité à `git fetch` de la branche ; aucune écriture dans le dépôt ; code versé non lancé ; aucun bloc de code en ligne. Python 3.13.18 (`python3 --version`). **Aucun refus d'outil.**

## Verdict

**Scellable après corrections.** Les quatre corrections sont appliquées dans les mots de mon § 6. Il reste sept remplacements exacts, de la taille d'un erratum (§ 4) : trois ferment la question ouverte par la correction 3, quatre alignent sur la version 5 des passages encore écrits dans les mots de la version 4. Aucun ne touche un critère, un seuil chiffré ni une valeur gelée. Aucun ne demande de retour à Lazar.

## 1. Empreintes et différentiel

- **Empreintes, toutes égales aux attendues :**
  - version 5 : `6230d6c3…` ;
  - différentiel v4 → v5 : `394fc540…` ;
  - rapport du rédacteur : `ece02f5a…` ;
  - mandat v5 : `0f4853b9…` ;
  - version 4 : `d5b817d3…`.
- **Compagnons `.sha256`** : égaux, fichier des remplacements et journal de l'outil compris. Le commit `cf1a6d24` est un ancêtre de la branche, aujourd'hui à `e6ff60d6`.
- **Différentiel** : celui que j'ai refait (`diff -u`) est égal au différentiel versé. Les blocs changés tombent dans les passages que nomme l'annexe G.

## 2. Les quatre corrections

| n° | appliquée | où |
|---|---|---|
| 1 — traits de contenu rapportés, liant l'étage payant (retenue par la mère) | oui, dans mes mots | section « Seuil » ; garde 25 ; réserve 18 ; annexe F, point 1 et table, en deux phrases du rédacteur qui disent bien ces mots |
| 2 — cas sain et artefact de l'arrêt « bornes épuisées » | oui, dans mes mots | garde 25 |
| 3 — fréquence propre aux lois vraies du monde source ; nombre de lois par strate avec son intervalle | oui | M12 (strates et phrase finale) ; S8 (huit valeurs) ; annexe C ; annexe F, point 4 |
| 4 — audit des mondes par dose lu par paires de doses | oui, dans mes mots | section « Seuil » |

## 3. Les écarts que le rédacteur me demande de trancher

**(1) La question ouverte par la correction 3 se ferme ainsi :**

- **S8 (i)** se lit **dans chacune des deux strates**. L'épreuve simulée doit discriminer sur les lois du monde source, où se joue ce que le lecteur hérite, comme sur celles des mondes cibles. C'est le sens prudent.
- **L'artefact de la garde 23** porte sur la fréquence des lois vraies **du monde source**. C'est elle qui règle, par la part gardée des entrées de la source, ce que le lecteur compose au bras 3. La note du texte, « seule conduite dont M1 dépend de cette fréquence », devient alors exacte.
- **B2 et l'hypothèse de travail (iii)** doivent dire que la fréquence d'une loi vraie est celle de la strate de son monde.

**(2) Les passages restés dans les mots de la version 4 :**

- **À corriger**, parce qu'ils sont opérants :
  - B1 (ii) ;
  - « les neuf exactitudes », qui sont quinze lues par paires : trois audits dont l'audit par dose en trois paires, donc cinq exactitudes par jeu de traits, sur trois jeux ;
  - réserve 7, « sept fréquences ».
- **À laisser**, parce qu'ils sont l'histoire de la version 4 et que l'annexe G dit ce que la version 5 en défait :
  - l'en-tête (phrase sur la version 4) ;
  - la section « Contre-lecture », points de la version 4, (b) ;
  - l'annexe F, point 4 (« Ce que le texte dit », « Ce que cela touche ») et sa table, ligne M12 ;
  - l'annexe F, « Ce qui revient à Lazar ».

  C'est la même règle que pour l'annexe E.
- **Liste d'arrêt, point 2** (« ou son audit échoue ») : à garder tel quel. La section « Seuil » dit désormais ce qui fait échouer l'audit.

## 4. Corrections (remplacements exacts, chaque ancien texte trouvé une seule fois dans la version 5)

1. **S8 (i).** Remplacer « la part des lois vraies plantées engagées qui tiennent (M12, par loi) est au moins 0,5, et » par « la part des lois vraies plantées engagées qui tiennent (M12, par loi) est au moins 0,5 dans chacune des deux strates, monde source et mondes cibles, et ».
2. **Garde 23, artefact.** Remplacer « la fréquence de « tient » des lois vraies divisée par deux dans la couche statistique » par « la fréquence de « tient » des lois vraies du monde source divisée par deux dans la couche statistique ».
3. **B2, couche statistique.** Remplacer « — par type et, pour une loi non plantée, selon l'origine de la tentative (version 4) — » par « — par type, la fréquence d'une loi vraie étant celle de la strate de son monde (monde source ou monde cible ; version 5), et, pour une loi non plantée, selon l'origine de la tentative (version 4) — ».
4. **Hypothèse de travail (iii).** Remplacer « par loi, par type et, pour les lois non plantées, par origine de l'engagement (M12) » par « par loi, par type — les lois vraies selon leur monde, source ou cible — et, pour les lois non plantées, par origine de l'engagement (M12) ».
5. **B1, « Comment l'audit le contrôle », (ii).** Remplacer « et une sorte de lois que le filtre aurait rendue reconnaissable arrête le générateur ; » par « et une sorte de lois que le filtre aurait rendue reconnaissable arrête le générateur si elle l'est par les traits de forme, et, si elle ne l'est que par les traits de contenu, est rapportée et lie l'étage payant ; ».
6. **Ce qui est rapporté.** Remplacer « par sorte de loi ; les neuf exactitudes de l'audit de présentation. » par « par sorte de loi ; les quinze exactitudes de l'audit de présentation (cinq par jeu de traits : forme, contenu, réunis). ».
7. **Réserve 7.** Remplacer « **Version 4** : sept fréquences au lieu de cinq viennent » par « **Versions 4 et 5** : huit fréquences au lieu de cinq viennent ».

Une ligne à l'annexe G suffit pour inscrire ces sept remplacements. Une relecture d'un coup d'œil de leur différentiel par moi suffit ensuite.
