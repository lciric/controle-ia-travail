# Contre-lecture du préenregistrement du crible (iii), brouillon 6 — tour 3 de la lecture du brouillon 4 (sixième lecture du crible) — v1

- Lecteur : sous-agent neuf du modèle C (R2), qui n'a écrit aucune des pièces ; auteur de la pièce : modèle A. Rédigé le 2026-11-16, 14:43Z à 14:50Z (`date -u`).
- Pièce lue : `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-iii-brouillon6.md`,
  `f377e927aab482b39ccda892adc178a1cbfaac7a8042bf9215047f303f72189d` (égale à son compagnon).
- Comparée : brouillon 5, `add61e9726e5ba64324135656bde0042aa87721eafdf12431af30be810b4b94f` ; rapport du tour précédent
  `contre-lecture-crible-iii-b4-tour2-v1.md`, `782f737747bb95838b514b80d91a81c02ef006001364ad4845ad80bc4a4d85f6` (recalculée) ;
  programme `appliquer-corrections-crible-iii-brouillon6.py`, `93e21ae53893f7f8f327b1e49fb261da31aead1b79386b3c6992ddfbbe3cef66` (égale à son compagnon).
- Non lu, par consigne : sortie du pilote MR-2 v14, `diag/`, `runs/`, `donnees/`, 7a, 7b, T0.6, T0.7, P3-bis, bras d'attaque, dossiers jetables du premier contre-lecteur.

## Verdict

**« scellable »** pour le texte tel qu'il est (forme fidèle à la note) : aucune correction exigée. Les 4 couples du tour précédent sont
appliqués à la lettre, le différentiel ne contient rien d'autre, le validateur ne trouve aucun défaut. **Réserve de séquence** : la
pièce se déclare elle-même non scellée tant que la mère n'a pas inscrit la forme ; je recommande toujours la variante (section 3), qui
impose une réécriture et un tour de plus : dans ce cas **ne pas sceller ce texte**.

## 1. Corrections du tour précédent et différentiel (`diff` brouillon 5 → 6)

Appliquées fidèlement : G-01 (étage 2 : texte « nouveau » identique à l'octet au rapport : C_B = 0 pire cas pour B ; issue de P2 du
rapport réintégré qui diffère → « sensible à la troncature de B », rien de plus) ; G-02 en trois couples (section 0 point 1 ;
H-iii-a ; « Écarts », N-045 point 3), textes identiques au rapport ; G-03 (entrée « Contre-lecture 5 » avec les deux empreintes
entières, `add61e97…` et `782f7377…`, toutes deux recalculées justes).
Le `diff` ne contient en plus que : titre (brouillon 6), puce d'en-tête du brouillon 6 (tête `fd171dd7` = tête du dépôt vérifiée ; empreinte
du programme juste), statut (« contre-lu cinq fois »), ligne du validateur, section « Tour suivant ». Rien d'autre. Le texte de la puce
(« rien d'autre que les 4 couples, l'en-tête et la section ») est exact. Les remarques facultatives R-1 à R-6 sont déclarées non
appliquées : exact. Les restes de « QO1 » non qualifiés (lignes de contexte qui définissent le sens, titre de la question de la course)
sont listés par la pièce et sont bien tels : pas de contradiction.

## 2. Vérifications refaites après les corrections

- (1) R1 : la règle ajoutée en G-01 ferme la dernière porte de sortie (désaccord principal / réintégré) ; elle n'ouvre pas de voie vers un
  signe positif (qualification « sensible », aucune conclusion) ; R3 intact.
- (2) à (8) : inchangés par le diff (aucune ligne touchée sur statistique, marge, devis, durée, liste d'arrêt, graines, ablation).
  Devis non touché : 100 appels, 58,30 / 216,60 (forme fidèle), 128,30 / 263 (variante), sonde 6,68 ; cumul des cinq 1 308,60 (1 262,20
  fidèle) contre 1 275 : dit par la pièce.
- (7) Ablation : la qualification « deux espèces de frontière, non l'instrument local » est maintenant partout où elle compte ; N-045 point 3 reste respecté hors du crible.
- (9) `controle_ia.prereg.problemes(chemin)` rend `[]` ; aucun identifiant de modèle (recherche de motifs) ; empreintes de l'entrée 5 et du programme vérifiées par `sha256sum`.
  La pièce ne contient aucune décision de forme : aucune ligne de `registres/decisions.md` jusqu'à R-2991 (dernière) ne la tranche : confirmé.

## 3. Forme du crible (inchangé, confirmé)

Recommandation : **la variante** (Pr-2 choisit, Pr-4 écrit, S = un appel de Pr-4), confiance 0,6. Elle met le plus possible sur crédits de
Claude (environ 98 % de l'attendu, 3 USD hors crédits au pire contre 96,60 pour la forme fidèle) et garde le même contraste de prix aux deux
barèmes ; elle change un peu la question (deux paliers d'une même maison, non un proposeur externe contre la frontière). La forme fidèle reste
défendable si la consigne vise seulement à limiter les dollars hors crédits.

## 4. Corrections exigées

Aucune. Remarques facultatives (non exigées) : R-1 à R-6 des tours précédents à reprendre dans la version qui fera foi.

## 5. Points pour la mère

1. Inscrire la forme (ligne datée dans `registres/decisions.md`) **avant** de sceller : si la variante, réécriture + un tour sur le différentiel ; si la forme fidèle, ce brouillon 6 se scelle tel quel.
2. Geler III-6 avant que le lecteur neuf du pilote rende sa lecture ; le mot de Lazar pour le lancement ; autonomie jusqu'au 17 novembre 11:47Z (prolongeable au 18).
3. Enveloppe de GO-2026-11-15-06 : somme des pires cas des cinq cribles 1 308,60 (variante) ou 1 262,20 (fidèle) contre 1 275 : plafond cumulé à décider ; solde de crédits de Claude (263, ou 315,60 à 24 mondes).
4. N-045 point 3 à dire à Lazar avec le nœud d'adoption ; risques : « non tranché » probable pour P2 (puissance 0,35 à 0,50 à 20 mondes), code neuf et cinq files concurrentes jamais éprouvés.

## Incidents (de ma main)

- Un appel du validateur avec un chemin relatif faux a échoué (erreur de fichier), rejoué avec le bon chemin ; sans effet.
- Aucun appel de modèle, aucune dépense, aucune machine, aucun fichier existant modifié, aucun commit, aucun `pytest`, aucun `git fetch` ; rien lu des interdits.
