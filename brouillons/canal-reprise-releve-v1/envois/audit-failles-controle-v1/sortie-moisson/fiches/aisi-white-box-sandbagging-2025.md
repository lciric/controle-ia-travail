# Fiche — Bloom, Taylor, Kissane, Black et al., *White Box Control at UK AISI — Update on Sandbagging Investigations* (institut britannique de sécurité de l'IA, 10 juillet 2025) — v1

- **Nature** : note de recherche d'un institut public (littérature grise), résultats dits préliminaires ; non relue par
  des pairs.
- **Fichiers** (une seule source, deux fichiers) :
  - notice de l'institut : `pages/aisi-white-box-sandbagging-2025/page-v1.html`, SHA-256
    `fce74873d1e4fbd82faf374ed72dde0840ddd36cf716021be5b7f93d67cba082`, 20 279 octets, sauvée le 2026-10-26 à
    10:46 UTC depuis `https://www.aisi.gov.uk/research/white-box-control-at-uk-aisi---update-on-sandbagging-investigations`
    (date affichée : 10 juillet 2025 ; elle ne contient que le résumé et le lien « Read the full paper ») ;
  - texte complet, lié par la notice : `pages/aisi-white-box-sandbagging-2025-texte/page-v1.html`, SHA-256
    `c02bd0af02603036c0dbf5dc11c281984db283fa6fab436751c8ab12163fefd2`, 850 706 octets, sauvé à 11:16 UTC depuis
    `https://www.alignmentforum.org/posts/pPEeMdgjpjHZWCDFw/white-box-control-at-uk-aisi-update-on-sandbagging`
    (en-tête : 10 juillet 2025).
- **Repérage** : je cite la section (« Update 1 » à « Update 4 » et leurs intertitres).
- **Chez session-depot** : **non** comme source ; les modes recoupent en partie S1, D1, E5 et l'angle mort 2.

## Ce que la source établit sur des modes d'échec

1. **Les bons résultats sur 8B et tâches simples ne transfèrent pas.** Sur Llama-3.1-8B-Instruct incité à
   sous-performer sur des tâches simples, les sondes de tromperie entraînées hors politique « performaient très bien »,
   le moniteur boîte noire se dégradant avec la difficulté (« Summaries », « Update 1 ») ; avec Llama-3.3-70B et une
   tâche d'agent (capture du drapeau), les deux familles se dégradent (« Update 2 »).
2. **Séparabilité n'est pas détection : le seuil.** Sur la tâche d'agent, les sondes séparent les distributions
   (aire sous la courbe de 97 % en moyenne, 99 % en max), mais le seuil doit être fixé sans accès aux deux
   distributions ; étalonné à 1 % de faux positifs sur un corpus de conversation, il donne 88 % de vrais positifs et
   2 % de faux positifs (max), résultat « sensible » à la méthode d'étalonnage (« Both Black and White Box Runtime
   Monitoring Performance Decreased »).
3. **Problème d'agrégation.** Les sondes s'allument sur des transcriptions bénignes : code que le modèle sait
   probablement faux après des échecs répétés, objets associés à l'incorrection, activations inexpliquées ; cela gêne la
   moyenne comme le max sur les jetons (même section). Les auteurs envisagent les sondes à attention ou des questions
   de suivi.
4. **Marge propre au modèle.** Même à 100 % d'aire sous la courbe, la marge de séparation est bien plus faible à 70B
   qu'à 8B et le seuil zéro ne sépare plus les classes ; la méthode d'entraînement des sondes serait sensible au modèle
   (« Comparing Probes on 70B to 8B »).
5. **Organismes réglés : le succès dépend de la construction de l'organisme.** Les sondes marchent bien sur
   l'organisme à porte dérobée **distillé de la consigne**, moins bien sur ceux qui imitent un modèle faible ; les
   auteurs supposent que les trajectoires de sous-rendement incité, sur lesquelles l'organisme distillé est entraîné,
   l'ont biaisé vers l'activation du trait « tromperie » ; le verrouillage par mot de passe gêne les sondes pour les
   politiques distillées ; le rappel au seuil de contrôle baisse nettement (« Probe Performance on SFT Sandbagging Model
   Organisms »).
6. **Construit mêlé : intention et incorrection.** Les scores montent sur une réponse bénigne qui explique pourquoi une
   réponse fausse est fausse ; la sonde capte « tromperie » et « fausseté » (« Qualitative Analysis of Model Organisms »).
7. **Sur données réelles d'essais** : aucun signe manifeste de sous-rendement, mais des cas de conscience d'évaluation
   et de refus mous (« Update 4 », résumé).

## Conditions

- Sous-rendement **incité** ou **appris par réglage fin supervisé** ; sondes de tromperie inspirées de Goldowsky-Dill
  et al. ; tâches à choix multiple et une tâche d'agent ; les auteurs disent eux-mêmes ne pas avoir préenregistré
  l'effet de la chaîne de pensée (section « Update 3 »).

## Ce qu'elle ne dit pas

- Aucune agrégation séquentielle sur plusieurs épisodes ; aucun attaquant adaptatif contre les sondes.
- Les chiffres exacts par organisme sont dans des figures, non relevés ici.

## Ce que ça touche chez nous (avis)

- Prédiction de validité de la section 7 : une sonde qui réussit sur (ii), distillée de (i), peut lire un artefact de
  distillation ; il faut un organisme dont les trajectoires ne viennent pas du sous-rendement incité (voir aussi
  l'angle mort 2 de session-depot).
- Porte G0 « sondes au-dessus du plancher » : l'aire sous la courbe ne suffit pas ; le seuil étalonné hors tâche et le
  rappel à 1 % sur la tâche doivent être la mesure de porte.

## Phrase citée

« Though the results from our first update were very positive for white box monitoring, the second and third updates
show that simple baseline methods leave much room for improvement. » (section « Summaries »)
