# Contre-lecture B3-2 du module final de l'addendum de P3 — verrou et preuves

- Relecteur : sous-agent neuf (R2), qui n'a écrit ni le module, ni ses tests, ni le brouillon.
- Texte qui fait foi : brouillon 3 (`addendum-p3/P3-addendum-lecture-complementaire-v1-brouillon3.md`).
- Objet : `addendum-p3/final/complements_p3_v1.py` (sha256 `daf954594456f8c268ebbf48b14326a183941c00c4cddb205b2e3382a875f4fa`)
  et `addendum-p3/final/test_complements_p3_v1.py` (sha256
  `01b5faeaf1fe5ea38624b872948d46d5310bc67b6df3277ea1515e73fc057abc`), copiés octet pour octet dans
  `rapports/revue-b3-2/base/` ; notes `addendum-p3/final/NOTES-SYNTHESE.md`.
- Angle : verrou et preuves. Peut-on promouvoir une conclusion, changer l'issue, ou omettre une réserve due ? Les tests
  tuent-ils les mutants qui le feraient ?
- Rien n'a été écrit hors de `rapports/revue-b3-2/` et de ce rapport. Le dépôt de travail n'a pas été touché (état git
  propre avant et après, commit `c4a203aefb892b4e4256cef4e72ce9f4eb3e9507`).

## Verdict

**« scellable après corrections »**

<<VERDICT_DETAIL>>

## Ce qui a été lancé

- Suite du module, sans changement : `117 passed in 594.53s` (`revue-b3-2/pytest-base.log`).
- Essais de ce relecteur : `revue-b3-2/sondes/test_sondes_b3_2.py` (7 essais) et
  `revue-b3-2/sondes/test_sondes_b3_2_verrou_mutable.py` (1 essai) : tous passent, donc chaque constat qu'ils portent est
  reproduit (`revue-b3-2/sondes.log`).
- Mutants : `revue-b3-2/mutants_b3_2.py` (liste, motifs uniques vérifiés), lanceurs `mutants_b3_2.py` et
  `lanceur2_b3_2.py`. Chaque mutant change une seule règle dans une copie du module ; la **suite entière** (117 tests, sans
  sélection, arrêt au premier échec) est lancée sur la copie. Résultats : `revue-b3-2/mutants-resultats.jsonl`, journal
  de chaque mutant dans `revue-b3-2/mutants/<id>/pytest.log`.

<<BILAN_MUTANTS>>

## Preuve du verrou (ce qui tient, ce qui ne tient pas)

1. **Promotion d'une conclusion.** Tient pour le code tel qu'il est. `conclusions_etablies` (l. 502-512) est une
   fonction pure des drapeaux de la lecture décisive lus par la garde 7 ; elle suit la table du plan, point 5, et
   `test_conclusions_etablies_table_fermee` en tue les mutants directs (V4). Un contrôle sur une cible non établie
   rend « sans objet » et n'écrit rien d'autre (`_Entree.controle`, l. 906-910). Aucune analyse n'écrit dans
   `D["etablies"]` ni dans `L` (lecture du code). L'essai de propriété sur les 30 scénarios des tests le confirme : chaque
   contrôle lu vise une cible établie, chaque réserve aussi, la recommandation ne nomme que des cibles établies, l'issue
   primaire est la copie exacte. **Mais** le contrôle de fin (`exiger_verrou`) ne recalcule pas les conclusions : une
   analyse fautive qui allonge `D["etablies"]` promeut une conclusion sans arrêt (CB2-06). Et la preuve est relative aux
   drapeaux bruts de la lecture (`conforme`, `T<k>.etabli`), que rien ne recoupe avec les états (CB2-11).
2. **Changement de l'issue.** Tient. `issue_primaire` est une copie canonique prise avant les analyses (l. 1825-1826),
   comparée à la fin (l. 1767) ; un instantané canonique de toute la lecture est comparé aussi (l. 1865). Les deux gardes
   sont tuées par leurs tests (essai du module `a9_qui_touche_l_issue`, et le mutant « issue recopiée altérée »).
3. **Omission d'une réserve due.** Ne tient pas au niveau des preuves. Le code émet bien un contrôle « non lu » sur chaque
   chemin d'échec que j'ai lu, mais une dizaine de ces chemins peuvent être rendus « favorables » sans qu'un seul des 117
   tests échoue (CB2-01) ; de même pour plusieurs cibles, niveaux et conditions de réserve (CB2-02 à CB2-05). Une entrée
   qui tombe en échec après ses contrôles efface aussi une réserve contraire déjà calculée (CB2-09).

## Constats (le plus grave d'abord)

<<CONSTATS>>

## Table des mutants

<<TABLE>>
