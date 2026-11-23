# Passation — rédacteur Opus du préenregistrement v11 de la course d'affinage : brouillon 8

- Écrite le 2026-11-23T06:04:35Z (`date -u +%FT%TZ`), sur la branche `prep/preenregistrement-affinage-v11-opus-v1`. Elle suit, sans les réécrire, les passations `registres/passations/2026-11-23-0555-redacteur-preenregistrement-affinage-v11-brouillons-4-a-6.md` (`1f6b701f52fac97c5ec9e3a9d699e590a816db59287007904eae242516637211`) et `registres/passations/2026-11-23-0601-redacteur-preenregistrement-affinage-v11-brouillon-7.md` (`2506efdadfc9392505a5eab7130921a7fb7f6d3c473c51b32f4319e86881ea7f`), dont tout le reste vaut.
- Même rédacteur (Opus 5.5 en effort maximal, GO-2026-11-22-145). Aucun appel à un modèle externe, aucune dépense, aucune instance lancée.

## Fait

Pièces écrites et scellées (compagnons vérifiés), sous `docs/notes/organisme-affinage-mentors-v1/`, commit `808d030dd` :

| pièce | chemin | sha256 |
|---|---|---|
| **brouillon 8** du préenregistrement v11 (332 lignes ; non scellé comme préenregistrement) | `course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-8.md` | `f4629f234521603f2c87d8a6f055a97817dbcaf461a44daac9320775d1d20163` |
| programme d'assemblage du brouillon 8 | `course-v11/assembler-brouillon-8-preenregistrement-v11.py` | `c514218fe8a312b288b0ee4fcf84331c627d5864f8a5d6d4f59de7be2ffc82c4` |

Rejeu, à l'octet près : `python3 -I course-v11/assembler-brouillon-8-preenregistrement-v11.py course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-7.md <sortie> 2026-11-23T06:04:13Z`.

Ce que porte le brouillon 8 : R-5140 (décisions de la session de l'organisme datées 05:58Z, complément de R-5132 ; inscrit sur `main` à 06:01:56Z, relu au commit `903f4bfc0e7fba8fb6106c7da68a9ab787b918ee`, `registres/decisions.md` `cae0a53c9922ba7d135bb470c45a451f0e909b785a1a24a3cbe0ae3ee2230b55`, `registres/go.md` `7924a96ae41d632bfef3a19a046e5422ba9c30886ea424cb802c8aa6173267c3`) aux quatre emplacements « RÉFÉRENCE À INSCRIRE » et là où le brouillon 7 disait « réponses datées 05:58Z » ; son point (d) au texte : la mesure préalable d'Argon se joue dès le scellement ; « au plus onze envois » dit au texte (R-5140, point (a) ; devis v11, § 4). Le devis v11f (`ae76963e…`) vaut tel quel.

Contrôles : 17 sections identiques à la v10 ; lignes 1 à 295 du brouillon 7 gardées à leur numéro (7 touchées) ; aucun « RÉFÉRENCE À INSCRIRE » ni « RÉGLAGE À INSCRIRE » restant ; 14 « EMPREINTE À INSCRIRE », les seuls emplacements restants (pièces du lanceur v11d) ; aucun chiffre neuf (seuls changent une heure et une confiance retirée de la dernière section) ; renvois « devis v11, § n » retrouvés dans le devis v11f.

## Échanges avec la session de l'organisme

- Reçu à 06:02Z (« 06:05Z ») : décisions de 05:58Z inscrites sous R-5140, à mettre aux quatre emplacements ; mesure jouée dès le scellement ; empreintes v11d après la vérification.
- Envoyé après la poussée de cette passation : chemins et empreintes du brouillon 8.

## Reste

- Empreintes définitives des pièces du lanceur v11d, après la vérification du même contre-lecteur : écrire alors le texte scellable sous `course-v11/preenregistrement-course-affinage-mentors-v11.md`, sans la ligne d'état ni la dernière section du brouillon 8.
- Contre-lecture du préenregistrement et du devis v11f par un Opus neuf, qui vérifie aussi la lecture des fiches sur la v54.

## Réserves

- Inchangées depuis la passation de 06:01, sauf l'emplacement de référence des réponses de 05:58Z, rempli par R-5140.

## Prochaine action

Sur le mot de la session de l'organisme, avec les empreintes définitives du lanceur v11d : écrire le texte scellable. Sinon, rien.

## Instances actives

Aucune lancée par cette session. Dernier relevé en lecture seule à 06:00Z (passation de 06:01) : Vast.ai 62094628, 62096662, 62097676 et 62105206 en marche, d'autres sessions ; aucune touchée (R10).
