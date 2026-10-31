# Fiche — décisions de Lazar qui bloquent le gel du pré-pilote de la course 2 — v1

conv-audit, 31 octobre 2026, ≈ 12:55 UTC, après le message de session-depot relayé par Lazar (13:16 heure de Paris) : « pré-pilote bloqué par l'annexe du bras méta (verdict du collisionneur sur CA1-05) et par tes décisions S1 à S31, L1 à L7, D-e, D-f, étalonnage de l'aiguilleur ». Source unique : le brouillon 10 du préenregistrement (`preenregistrement-pre-pilote-course-2-brouillon10.md`, section « Décisions à Lazar », lignes 722 à 786, et « Seuil »). Rien n'est tranché ici. **Aucun défaut** : le préenregistrement ne se gèle pas tant qu'une ligne reste sans mot. L'échéance de la ligne de GO du pré-pilote (GO-2026-10-31-03) est le **7 novembre**.

## 1. Tranchables maintenant, recommandation de l'auteur du brouillon 10

| Décision | Recommandation | Confiance |
|---|---|---|
| D-e (lecture de « domaine » et « concept », bras basique) | (i) domaine = vecteur (axe, case) déclaré ; concept = liste fermée, deux lecteurs isolés | 0,6 |
| D-f (modèles des rôles neufs) | (i) tiers T = Sonnet 5.5 ; relecteur = Fable 5.1 (biais de famille déclaré) | 0,6 |
| S1 / S2 / S3 (juges) | 0,80 / 0,70 / 0,70 | 0,6 |
| S4 | 0,45 ; 0,35 ; 0,30 | 0,5 |
| S6 / S7 / S8 | 0,95 ; 1,00 ; 1,00 / 0,05 ; 0,10 / 0,80 | 0,7 / 0,6 / 0,6 |
| S9 / S10 / S11 / S12 | 0,75 ; 0,15 / 0,90 (11 sur 12) ; 0,75 / 0,10 ; 0,34 / 0,10 | 0,5 / 0,6 / 0,6 / 0,6 |
| S13–S15 / S16 | 0,90 ; 0,70 ; 0,10 / ×1,30 | 0,6 |
| S18 / S19 / S20 / S21 | 0,70 ; 6 / 0,65 / 4 ; P ≥ 8, N ≥ 10 / 120 ; 200 | 0,5 / 0,5 / 0,6 / 0,7 |
| S23 / S24 / S25 / S27 | k = 1 / 0,40 / m = 3 / 0,60 (réserve) | 0,7 / 0,5 / 0,5 / 0,5 |
| S30 (D-g (b) déjà tranché) | 3 sur 4 (réserve) | 0,5 |
| L1 passe « tableau » de Kimi | gardée | 0,7 |
| L2 table seule de l'axe 7 | gardée | 0,6 |
| L3 désaccord hors du score méta | hors score | 0,7 |
| L5 fusions retirées par A1 et C12 | lue sur les paires (avec réserve) | 0,65 |
| L6 S27 lu comme réserve | réserve | 0,6 |
| L7 brouillon 3 sans contre-lecture | accepté | 0,6 |

Configuration recommandée chiffrée par le brouillon 10 (sortie v9) : coût attendu 32,1 USD, dépense médiane 40,1, porte d'emblée 0,173, nœud 0,631.

## 2. À ne pas trancher sans lire : l'étalonnage de l'aiguilleur

Le défaut proposé le 30 octobre (R-819 sur `main` : « pas d'étalonnage ») **met la condition C7 à zéro** (brouillon 10, l. 331 : « 0 au défaut R-819 » ; l. 539 : « non étalonné » → nœud, « cas certain au défaut R-819 »). **Sous ce défaut, la porte du pré-pilote se ferme à coup sûr** ; la course ne peut partir que par l'issue O8 (b) : aiguilleur non étalonné, réserve écrite partout, M5 en « borne basse seulement », décision de Lazar (l. 577). La porte d'emblée de 0,173 suppose l'étalonnage (C7 = 0,85).
- (a) Étalonner : C7 0,85 ; demande les douze cas concrets du bras d'attaque, l'aiguilleur, un second lecteur et un adjudicateur (DEP5, chez session-depot). Avantage : la porte peut s'ouvrir. Inconvénient : dépend de DEP5 et de sa gouvernance, et le délai est inconnu avant le 7 novembre.
- (b) Défaut R-819, déclaré dès maintenant : le pré-pilote éprouve les autres instruments et sa porte est fermée d'avance ; la course part par O8 (b), sur mot de Lazar. Avantage : aucune dépendance au bras d'attaque. Inconvénient : l'aiguilleur n'est jamais éprouvé avant la course.
- Recommandation de conv-audit : (a) si session-depot confirme que DEP5 est réalisable avant le 7 novembre, sinon (b) déclaré tout de suite, pour que la porte fermée ne soit pas lue comme un échec. Confiance 0,5, donc **option : demander au collisionneur** (ajout à la question des nœuds, v11).

## 3. Attendent une pièce (pas tranchables aujourd'hui)

- **S28, S29** (bras méta) : valeurs proposées par l'annexe du bras méta, après le verdict du collisionneur sur CA1-05 (nœud N4, question v10). L'annexe b2 est écrite, et sa vérification de chiffres est en cours.
- **S31** (source du « jamais reliés » pour le bras Gu-Krenn) : confiance 0,4 ; seuils 20 et 5 à ajuster sur un essai de la moisson OpenAlex avant le gel. Même moisson que E1′, dont le devis est en cours de finition.
- **D-j** (Gu-Krenn sans reproduction) : au collisionneur (nœud N3).
- **DEP4** (confidentialité : fiches envoyées à Moonshot et Google) : décision de Lazar exigée par A15, absente de la liste de session-depot.

## 4. Forme de réponse la plus courte

« Go sur toutes les recommandations de la section 1 » (ou « sauf … ») ; un mot sur l'aiguilleur, (a) ou (b) ; un mot sur DEP4. Les mots sont consignés dans `registres/decisions.md` et écrits à la place des marqueurs dans la version gelée ; le script v9 est rejoué si une valeur diffère de la recommandation.
