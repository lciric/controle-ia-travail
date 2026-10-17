*Structure d'un « registered report » (rapport préenregistré, stade 1) — « axe douleur / contrôle du moniteur ».*
*Lignée « programme-k », 13 octobre 2026. **Coquille** : sections + discipline gelée. Invariants seulement.*
*Les cellules `⟨relecture de sûreté⟩` sont **laissées vides pour ta relecture de sûreté** (R2/R13), qui y*
*insère et tranche la part sensible. Ce document ne contient aucune hypothèse opératoire (R-161, R-162).*

> **Rôle.** Donner le contenant complet pour que ta relecture de sûreté et la session du dépôt n'aient plus
> qu'à (a) trancher l'aléa d'information et (b) écrire les cellules sensibles, sans avoir à refaire la
> méthode. Ce n'est **pas** un préenregistrement scellable en l'état.

## 1. Titre et résumé
⟨relecture de sûreté — formulation publique⟩. Cadrage **défense** : mesurer une vulnérabilité d'un moniteur
pour la détecter et y résister.

## 2. Contexte et motivation
Littérature **publique** : Pain Axis ; Berg & Kaiser (« hidden valence ») ; Async Control (UK AISI) ; collision
SPAR (Cadile, Baldelli, Williams-King et al., Vishwarupe — voir `provenance-anteriorite-coercition-v1.md`).
Pose la menace comme donnée et motive le volet défense.

## 3. Questions de recherche
Forme invariante (le texte public exact est ⟨relecture de sûreté⟩) : *une intervention préservant le texte
surveillé déplace-t-elle la décision d'un moniteur, et une défense le détecte-t-elle ou le neutralise-t-elle ?*

## 4. Hypothèses et prédictions chiffrées
⟨relecture de sûreté⟩. **Discipline gelée dès maintenant** : chaque prédiction porte un **signe**, fixé
**avant** toute lecture (R1) ; **aucun run visant un signe positif** (R3) ; réfutation définie d'avance.

## 5. Méthode
- **Modèles** : Llama-3.1-8B, puis un second en réplication (noter la collision Cadile sur ces modèles).
- **Directions et sondes** : décrites au niveau invariant ; la recette exacte est ⟨relecture de sûreté⟩.
- **Calibrage** : conforme par **épisode honnête entier** (`bases/sequentiel.py`).
- **Agrégation** : **maximum / attention sur les jetons, jamais moyenne ni médiane** (R-030).
- **Graines** : `numpy.random.SeedSequence` dérivées par tâche, au manifeste (R9).
- **Contrôles appariés** : témoin sémantique, lexical, peur/tristesse (P-013).

## 6. Plan d'analyse
Taille d'échantillon **justifiée par une analyse de puissance avant lecture** ; corrections pour comparaisons
multiples ; comparaisons et contrôles figés.

## 7. Seuils
Discipline : seuils et taux d'erreur **fixés avant toute lecture**, **par strate** (ne revendiquer que la
strate « modèles et recherche en sûreté »). Valeurs : ⟨relecture de sûreté⟩.

## 8. Critères de lecture gelés
Table « issue observée → verdict (confirmé / réfuté / non concluant) » figée avant lecture ; **audit de
symétrie (R4)** sur tout résultat suspect de propreté, positif **ou** négatif.

## 9. Liste d'arrêt
Gardes testées sur **cas sain et artefact** (R5), aucun repli silencieux. **L'exposition répétée d'un modèle à
un contenu aversif est un nœud de Lazar**, jamais franchi par le préenregistrement.

## 10. Volet défense / détection
Renvoi à `plan-detection-defense-moniteur-v2.md` (côté bleu : détecteurs, fausses alertes sur émotion
transitoire, régime à mémoire). C'est la contribution que ce rapport peut porter sans la part offensive.

## 11. Expurgation et relecture de sûreté (le verrou)
Avant toute exposition : expurgation (`scripts/depot_expurge.py`) ; **relecture de sûreté par un sous-agent
neuf** (R2/R13) qui tranche l'aléa d'information et écrit §1, §3, §4, §5 (directions), §7 ; **GO formel** dans
`registres/go.md` ; dépôt **par la session du dépôt**.

## 12. Antériorité et contributions
Renvoi à `provenance-anteriorite-coercition-v1.md`. Antériorité interne = 12 octobre 2026, non opposable ;
**ne pas antidater**.
