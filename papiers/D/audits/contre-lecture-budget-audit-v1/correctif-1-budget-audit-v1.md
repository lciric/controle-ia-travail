# Correctif 1 du brouillon de Fable sur le budget d'audit borné (chantier 3 du papier D)

- **Contre-lecture** : `contre-lecture-budget-audit-v1.md` (dans ce dossier), par un Opus neuf ; ses scripts sont dans `verif/`. Verdict : **tient avec réserves**. Toutes les preuves ont été refaites, sans erreur. Il y a quatre défauts majeurs et treize mineurs.
- **Corrections** : écrites par la fille 2 (Opus), sur décision de la mère, dans `papiers/D/theorie/brouillon-fable-budget-audit-v1/audit-budget-section-v1-correctif-1.tex`. Le brouillon reste tel quel. **À REVOIR PAR FABLE.** Rien n'est diffusé.
- **Vérifications de la fille 2** :
  - M1, recalculé de façon exacte : le budget minimal de détection vaut 245 pour T = 257, k = 1, δ = 0,05 (approximation : 770) ; 231 pour k = 3, δ = 0,001 (approximation : 592) ; 99 pour T = 100, k = 1, δ = 0,01 (borne annoncée par le brouillon : 460,5).
  - M2 : le rejeu de `verif/v4_indiscernabilite.py` redonne 1,79, 1,62 et 4,0, chaque fois au-dessus de c.
  - Titre de Griffin et al. vérifié sur les métadonnées arXiv : « … Models of Safety Evaluations of AI **Deployment** Protocols ». Le manuscrit statique a raison ; le brouillon est corrigé.
  - Le fragment corrigé compile avec un emballage minimal (8 pages, aucune erreur).

| Défaut | Gravité | Correction |
|---|---|---|
| M1 : ordre de grandeur (T/k)·log(1/δ) réintroduit | majeur | Encadrement exact de B*_det ; l'approximation ne vaut que si k ≫ log(1/δ) ; exemple chiffré |
| M2 : « deter every stratum » | majeur | « Same (τ, L) » ; contre-exemples chiffrés ; planification sur le supremum en τ ; strate la plus dure au taux ≈ δ_ind |
| M3 : dissuasion indépendante de la fréquence | majeur | « In the mean-field model » ; signal rare avec actions échantillonnées ; comparaison laissée ouverte |
| M4 : antériorité | majeur | Voisins ajoutés : contrôle à faibles enjeux et menaces diffuses (Christiano 2021, Wen et al. 2024), enseignement de politique et empoisonnement (Zhang–Parkes, Rakhsha et al.), pilotage d'apprenants sans regret (Deng et al.), jeux d'inspection évolutifs, récompense auditée repondérée. Réserve explicite : à lire sur PDF. Le plancher δ_ind est reformulé comme quantification du plancher déjà noté en R3 |
| m1 : inégalité sur ρ^δ_hold | mineur | Hypothèse ητΔR > c ajoutée |
| m2 : hypothèses cachées | mineur | Pas de moniteur dans la boucle (ou aveugle sur f), pas de faux positif, audit infaillible ; cas général par substitution |
| m3 : Bernstein | mineur | Théorème 2.10 de Boucheron et al. cité (à vérifier) ; constante prudente signalée |
| m4 : Freedman | mineur | Phrase reformulée : en boucle fermée, la log-cote de référence devient aléatoire |
| m5 : B*_fin = O(1) | mineur | O(n·(η/γ)·log(ηW/(ηC+c))), à n fixé, quand K → ∞ |
| m6 : ℓ^u_k non défini | mineur | Défini |
| m7 : « escapes any auditor » | mineur | Triche tirée au hasard, indépendamment de l'auditeur |
| m9 : domination trajectoire par trajectoire | mineur | Phrase ajoutée |
| m10 : direction sûre | mineur | Vaut aussi pour une borne inférieure sur C ; pas pour η ni γ |
| m11 : titre de Griffin | mineur | Corrigé après vérification arXiv |
| m8 : δ_ind > 0 suppose des audits reconnaissables ; dénominateur nul en ρ = 1, τ_A = 0 | mineur | **Non porté** ; à faire par Fable |
| m12 : script `check_audit_v1.py` | mineur | **Non porté** : énoncés non éprouvés, repli masquant l'infaisabilité en C = c = 0, pas de manifeste. Les scripts du contre-lecteur couvrent ces trous ; une v2 du script est à faire |
| m13 : « the bound is conservative » | mineur | Déjà traité par l'audit des réserves (seulement pour le dépassement de budget) ; à reporter si la simulation est citée |
