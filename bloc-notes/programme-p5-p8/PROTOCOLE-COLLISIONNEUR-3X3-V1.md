# STANDARD MÉTHODOLOGIQUE : PROTOCOLE COLLISIONNEUR 3x3 (V1)

Ce document formalise notre protocole d'idéation conflictuelle multi-tours pour la découverte scientifique en IA.

## 1. Philosophie et 5 Règles d'Acier
- **Règle B1 (Zéro Lissage / Greffier Append-Only) :** Les réponses des modèles sont capturées brutes, sans aucune réécriture ni lissage humain. Le greffier (l'orchestrateur) n'édite que pour sceller les hashs.
- **Règle B2 (Émission Initiale en Aveugle Total) :** Au premier tour, les modèles formulent leur théorie sans connaître l'existence ni la production des autres, empêchant tout biais d'ancrage ou de complaisance.
- **Règle B3 (Symétrie Intégrale des 3 Modèles) :** Le collisionneur implique trois pôles cognitifs : Fable (5.1), Opus (5.5) et Argon/CLI (Gemini 3.1 Pro + Lazar). Tous sont soumis à la même attaque croisée.
- **Règle B4 (Loi d'Inférence Forte) :** Les dissensus doivent aboutir à des Duels d'Hypothèses Exclusives ($H_A \perp H_B$), où le résultat expérimental sur GPU falsifie définitivement l'une des deux théories.
- **Règle B5 (Ancrage dans l'État de l'Art Vivant & la Littérature Grise) :** Chaque modèle DOIT confronter et citer précisément :
  - L'**Alignment Forum** et **LessWrong** (limites des sondes linéaires, *ELK*, *sandbagging*, *white-box evasion*) ;
  - **Redwood Research** (*AI Control*, *Untrusted Monitoring*, *Causal Scrubbing*) ;
  - **Anthropic** (*Transformer Circuits*, *Sleeper Agents*, *Sycophancy to Subterfuge*, *Alignment Faking*) ;
  - **OpenAI** (sabotage d'évaluation) ;
  - **Apollo Research** (*Scheming*, *In-Context Deception*), **METR / ARC Evals** ;
  - GitHub et X/Twitter (`SauersML/honesty-heads`, *refusal direction*, steering de têtes parcimonieuses) ;
  - Papiers **NeurIPS, ICML, ICLR** (*RepE*, *ITI*, *Geometry of Truth*, *CCS*, *SAE / Transcoders*), afin d'isoler exactement ce que personne n'a encore jamais prouvé.

## 2. Architecture de la Matrice 3x3
- **Modèle A :** `claude-3-5-sonnet-20241022` (Fable 5.1). Rôle : Dynamisme comportemental et élicitation.
- **Modèle B :** `claude-3-opus-20240229` (Opus 5.5). Rôle : Modélisation formelle et profondeur causale.
- **Modèle C :** Argon / Gemini 3.1 Pro + Arbitre Souverain (Lazar). Rôle : Réalisme opérationnel et contraintes matérielles (A100).

## 3. Workflow Séquentiel en 2 Étages
### Étage I : Méta-Architecture de Découverte
- **Tour I.1 :** Génération Méta en Aveugle (`E1-T1-meta-A/B/C.md`).
- **Tour I.2 :** Attaque Croisée des Méta-Architectures & Canon Méta Muté (`E1-T2-attaque-meta-A/B/C.md`).
### Étage II : Programme, Duels d'Hypothèses ($H_A \perp H_B$), Expériences et Théorie Mathématique
- **Tour II.1 :** Génération des Programmes & Maths sous Canon Méta Muté (`E2-T1-prog-maths-A/B/C.md`).
- **Tour II.2 :** Attaque Red-Team Croisée sur Programmes & Maths (`E2-T2-redteam-A/B/C.md`).
- **Tour II.3 :** Droit de Réplique, Blindage Formels & Extraction des Dissensus Féconds (`E2-T3-riposte-A/B/C.md`).

## 4. Gabarit de Prompt Réutilisable
```markdown
Tu participes au Protocole Collisionneur 3x3.
[FAITS EMPIRIQUES BRUTS] : {faits_bruts}
[CONTRAINTES] : {contraintes}
[RÈGLE B5] : OBLIGATION de citer précisément l'Alignment Forum, Redwood, Anthropic, OpenAI, Apollo, METR et les papiers NeurIPS/ICML/ICLR.
[ATTAQUE ADVERSARIALE (Si applicable)] : Voici les théories de tes concurrents : {theories_concurrentes}. Attaque sans pitié leurs angles morts épistémologiques et leurs failles mathématiques.
[LIVRABLE] : Rédige ta proposition sous le prisme de ton Canon Méta Muté, en formulant des hypothèses mutuellement exclusives (H_A vs H_B).
```
