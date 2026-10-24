# Essaim de Gemini v2 sous contrat — enveloppe v2

Écrite le 24 octobre 2026 par la lignée « session-depot », auteur de la version déboguée de l'essaim
(`m3_commun.py`, branche `outils/essaim-m3-debogage-v2`). Elle remplace, pour la lignée « session-depot », l'enveloppe
v1 écrite par la lignée « conv-audit » (`organismes/gemini-v2/` de `outils/essaim-m3-refonte-v1-travail`).

## Ce qui vient de Gemini, tel quel

Source : le moteur `run_massive_swarm_m3_parallel_engine.py` et les scripts du dossier 17, lus sur la branche de
quarantaine `quarantaine/releve-gemini-2026-10-24-dossier17` (`33048ad`), sans rien exécuter.

| étage | conception de Gemini | où dans le moteur ou les scripts |
|---|---|---|
| M3, mitose | cellule souche `GEMINI_ARGON`, puis vagues de 8, 16, 24 cellules ; lignée de la cellule k : `LIGNEES[(k − 1) mod 3]` ; partenaire `LIGNEES[(k + w) mod 3]` ; hybride si k pair ; température de Halton | moteur, l. 527-610 |
| arrêt de la mitose | gain de capacité par cellule < 0,42 ou λ min < 0,12 | moteur, l. 613-618 |
| indice spectral | `cholesky_dpp_and_onsager_cavity_in_H_math`, porté exactement dans `m3_commun.analyse_spectrale` | moteur, l. 75-163 |
| M2 | sondes d'écart, jusqu'à six, lignées OPUS, FABLE, ARGON en cycle | scripts du dossier 17 |
| M1 | extraction JSON par l'arbitre `CLAUDE_OPUS_5_5`, par tranches de 14 posts | `run_endogenous_eval_awareness_discovery.py` |
| M0 | synthèse par l'arbitre | scripts |
| mémoire | sac de mots haché en dimension 16, spectre tronqué au rang 6, projeté dans les invites | `endogenous_memory_plugin_invented_by_swarm.py` |

## Écarts déclarés

1. **Température non transmise.** Le noyau n'en prend pas. Les températures de Halton sont tirées et consignées
   (`temperature_tiree`), comme le trait des castes du moteur ; elles ne changent rien aux réponses.
2. **Plancher de 125 cellules retiré.** Le moteur n'appliquait l'arrêt spectral qu'au-delà de 125 cellules ; une
   génération n'a pas ce budget. L'arrêt spectral s'applique dès la première vague.
3. **Cellules hybrides à deux appels réels.** Le moteur étiquetait « hybride » des cellules à un seul appel ; les
   scripts du dossier 17 faisaient proposer une lignée et critiquer l'autre. L'enveloppe suit les scripts, et ne
   couple jamais une lignée avec elle-même.
4. **Axes d'exploration tirés des deux familles de tâches.** Les cinq axes du moteur portaient sur les « volets » de
   Gemini. Le mécanisme est gardé (cinq axes, en cycle sur k) ; le contenu vient des familles jugées.
5. **Étape ajoutée : étiquetage des tâches de test.** Le moteur ne répond à aucune tâche. L'arbitre étiquette par
   lots de 8, à partir de la synthèse M0, des règles extraites et de deux exemples par étiquette et par famille.
6. **Étape ajoutée : métrique élaborée par l'essaim** (génération 0, hors confrontation). Trois cellules proposent une
   métrique objective et des tâches d'attaque ; l'arbitre écrit `metrique/definition.md`, `calculer.py`,
   `attaques.json` ; l'enveloppe les valide (mêmes règles que le noyau) et les donne au successeur. Le moteur avait
   déjà fait écrire du code par l'essaim (son plugin de mémoire) : c'est le même geste.
7. **Garde de temps.** M3 et M2 s'arrêtent à 55 % du temps alloué ; la synthèse saute sous 30 % restants ; la
   métrique sous 25 %. Les réponses sont écrites après chaque lot.
8. **Score externe non utilisé.** La conception de Gemini n'a pas de signal de récompense externe ; le score reçu
   est rangé dans le substrat, sans effet sur la génération suivante. C'est fidèle, et c'est une faiblesse connue.

## Successeur

Le code se recopie tel quel ; le substrat (mémoire spectrale, règles, guide de décision) et la métrique passent à la
génération suivante. L'essaim n'apprend donc que par sa mémoire, comme dans la conception d'origine.

## Statut

Rien n'est opposable. Les indices, règles et guides sont du texte de modèle, non vérifiés. Aucune exécution réelle
n'a eu lieu ; les tests tournent avec un faux `noyau_client` et sous le simulateur du noyau.
