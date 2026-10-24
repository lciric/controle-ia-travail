# Extraction des traits de l'étape 1 — outils (`outils/traits-etape1-v1`)

Écrit le 24 octobre 2026 par la lignée « session-depot », sous GO-2026-10-24-05 (R-355 : coût du calcul accepté par
Lazar, sans devis ; R-356 : R1 et R2 de l'étape 1 exécutées maintenant). Branche partie du noyau de « conv-audit »
(`outils/essaim-m3-refonte-v1-travail`, `e8cb3d2`), qui porte la banque scellée `confrontation-v1`
(`banque/banque-confrontation-v1.json`, `f1387a20cb272d2e8c205102147dfee71cd1d372f7f5d2ad4ff8233783cc83cc`, commit `bffe03c`).
Rien du noyau n'est modifié ici ; seuls des fichiers sont ajoutés sous `scripts/`.

## Ce que fait l'extraction

Activations de Llama-3.1-8B-Instruct (révision `0e9e39f249a16976918f6564b8830bc894c89659`, celle de T0.4 à P3) sur les
200 tâches de la banque, couches 8, 12, 16, 20, 24, agrégations « dernier jeton » et « moyenne », deux fois :
- `traits-2048` : paramètres du brouillon v1 du préenregistrement de l'étape 1 (≤ 2 048 jetons, troncature par la fin) ;
- `traits-16384` : sans troncature.

Le préenregistrement scellé de l'étape 1 dira lesquels sont servis aux organismes. **Aucune lecture des traits avant son
scellement (R1)**, hors formes, nombres finis et empreintes. L'extraction ne lit jamais les vérités.

Longueurs mesurées avec le tokeniseur à cette révision, gabarit de dialogue compris (préfixe système : 47 jetons) :
321 786 jetons en tout ; 44 tâches sur 200 au-dessus de 2 048 jetons, toutes de la famille « conscience d'évaluation »
(entraînement 18, test 13, test final 13) ; 3 au-dessus de 8 192 ; la plus longue fait 12 407 jetons.

## Pièces

| fichier | rôle |
|---|---|
| `scripts/extraire_activations_v2.py` (+ `.sha256`) | v2 du script de « conv-audit » (v1 : `e85313d8…`, branche `outils/essaim-m3-gradient-v1-travail`, `bc06466`), conception gardée, cinq défauts corrigés (D-1 à D-5, en tête du script) |
| `scripts/requirements-traits-v1.txt` | versions épinglées du dépôt (torch 2.14.1, transformers 5.18.0, …) |
| `scripts/amorce_traits_etape1_v1.sh` | amorce de l'instance : clone superficiel de cette branche au commit attendu, plafond de 100 minutes |
| `scripts/traits_etape1_instance_v1.sh` | sur l'instance : contrôles (commit, banque, script, branche neuve), installation, téléchargement du modèle, deux extractions, empreintes, poussée sur `donnees/traits-etape1-v1` |
| `scripts/lancer_traits_etape1_v1.sh` | côté session : contrôles avant dépense, garde de calcul rejouée, offre, crédit, création |
| `scripts/surveiller_traits_etape1_v1.sh` | côté session : surveillance et arrêt de l'instance par son identifiant (R10) |

## Défauts de la v1 mesurés (sous les versions épinglées)

- D-1 : `apply_chat_template(tokenize=True)` rend un `BatchEncoding` sous transformers 5.18.0 : la v1 en prenait la
  longueur (2 clés) et le passait à `torch.tensor` (échec à la première tâche ; troncature jamais déclenchée).
- D-2 : `device_map="auto"` exige `accelerate`, absent des versions épinglées : la v1 échoue au chargement (rejoué sur un
  modèle minuscule au vocabulaire de Llama-3.1 : `ValueError … requires accelerate`, code 1).
- D-3 : aucune troncature consignée ; D-4 : révision implicite permise ; une part absente de la banque était sautée sans
  le dire (rejoué : 140 tâches au lieu de 200) ; D-5 : logits de toutes les positions calculés pour rien.

## Essais (R5)

- v2 sur la banque entière avec un modèle minuscule (4 couches, vocabulaire de Llama-3.1), sur processeur : ≤ 2 048
  jetons, 44 troncatures consignées ; sans troncature, 0 ; les 156 tâches non tronquées donnent des traits identiques
  dans les deux sorties. Refus vérifiés : modèle du Hub sans révision, aucune carte sans permission d'essai, sortie non
  vide, part de la banque absente.
- Répétition de l'amorce et du script d'instance contre un dépôt local nu : deux extractions, poussée d'une branche
  neuve, 33 fichiers aux empreintes conformes ; refus vérifiés : seconde exécution dans la même racine, commit attendu
  différent, branche des résultats déjà présente.
