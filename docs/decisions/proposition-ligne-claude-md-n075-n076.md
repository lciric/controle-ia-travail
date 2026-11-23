# Proposition de mise à jour de la ligne 13 de `CLAUDE.md` — décisions N-076 et N-075

- **Date** : 2026-11-23T20:55Z (`date -u`).
- **Auteur** : sous-agent neuf rédacteur, Carbon en effort élevé (`pro`), en remplacement temporaire déclaré de Claude Fable 5.2 (`GO-2026-11-23-33`).
- **Portée** : ce fichier ne modifie pas `CLAUDE.md`. Il propose à la session mère les deux segments de remplacement dans la liste « Décisions de Lazar » de la ligne 13 de `CLAUDE.md` (`2246ff0183348d525737aca0086c3149a8b630358490b5f4acef7d94c18edabd`), après contre-lecture et scellement de `decision-N-075-issue-plancher-et-deux-regards-v4.md` et de `decision-N-076-assurance-par-audit-et-reference-honnete-v1-erratum-3.md`.

---

## 1. Renvoi pour N-076

### Segment actuel dans `CLAUDE.md` (ligne 13, 631 signes)

> N-076 (GO-2026-11-21-57) : loi de la référence honnête — toute accumulation déclare m, n et la source de sa validité, horizon au plus m sauf nul par acte, prévision scellée avant G1 ; hasard du défenseur comme preuve et banc à vérité plantée, à faire ; attestation en service, candidate ; audit après coup, à plancher et à l'enjeu, boucle audit-recapture-réapprentissage, épreuves du devin, à faire ; table du seuil au taux d'audit ; quatre invariants d'audit au § 9 ; les scores orientent l'audit ; rien revendiqué (`docs/decisions/decision-N-076-assurance-par-audit-et-reference-honnete-v1.md`, lue avec son erratum 1, qui prime)

### Segment proposé pour `CLAUDE.md` (598 signes sans le chevron ni son espace, plafond de 600)

> N-076 (GO-2026-11-21-57 ; GO-2026-11-23-32) : loi de la référence honnête — déclarer m, n et source, horizon au plus m sauf nul par acte (rang d'ensemble occupé, Arnold et al., facteur retard), prévision scellée avant G1 ; hasard du défenseur et banc à vérité plantée, à faire ; attestation candidate ; audit à plancher et enjeu, boucle, devin, à faire ; table du seuil ; quatre invariants § 9 ; scores orientent l'audit ; He et al. en nuance (débit nul si détection nulle) ; rien revendiqué (`docs/decisions/decision-N-076-assurance-par-audit-et-reference-honnete-v1.md`, errata 1 à 3, le 3 prime)

Ce que ce segment ajoute et ce qu'il resserre :
- Le renvoi à `GO-2026-11-23-32` et aux errata 1 à 3 (dont le 2 qui corrigeait l'empreinte de la lecture des douze voisins, et le 3 qui prime).
- Les deux nuances issues de la lecture sur document PDF des seize papiers (`R-5185`) : occupation statistique du nul par acte par Arnold, Henzi et Ziegel (`2109.11761 v3`, rang d'ensemble et facteur de délai de l'oracle) ; He et al. (`1612.09027 v1`) en nuance de Sobers et al. (`1608.00698 v3`, débit nul quand la probabilité de détection tend vers zéro).
- Préservation intégrale de « prévision scellée avant G1 » et de « à faire » (après « boucle, devin ») ; pour tenir sous le plafond de 600 signes (598 signes mesurés sans le chevron `>` ni son espace), les formulations de la ligne actuelle sont condensées sans perte de sens (« déclarer m, n et source » au lieu de « toute accumulation déclare m, n et la source de sa validité », « attestation candidate » au lieu de « attestation en service, candidate », « audit à plancher et enjeu, boucle, devin » au lieu de « audit après coup, à plancher et à l'enjeu, boucle audit-recapture-réapprentissage, épreuves du devin », « table du seuil » au lieu de « table du seuil au taux d'audit », « quatre invariants § 9 » au lieu de « quatre invariants d'audit au § 9 »).

---

## 2. Renvoi pour N-075

### Segment actuel dans `CLAUDE.md` (ligne 13, 597 signes sans le chevron ni son espace)

> N-075 (GO-2026-11-21-46, -47, -51, -53, -61) : contre le diffus, mesurer l'issue et corriger — plancher d'audit au hasard publié, jamais revendiqué, q mesuré par dommages plantés, strate non mesurée à zéro ; sondes : accélérateur, non garantie ; dilemme, non décorrélation ; pince en trois objets ; alerte = motif et dommage au même lieu, motif seul : audit, jamais témoin ; lemme resserré au reste, à démontrer ; veille à côté des chantiers ; réapprentissage sur l'oracle non tranché, N-060 v3 tient (`docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v3.md`, errata 1 à 3, le 3 prime)

### Segment proposé pour `CLAUDE.md` (597 signes sans le chevron ni son espace, plafond de 600)

> N-075 (GO-2026-11-21-46, -47, -51, -53, -61 ; GO-2026-11-23-32) : contre le diffus, mesurer l'issue et corriger — plancher d'audit au hasard publié, jamais revendiqué, q mesuré par dommages plantés, strate non mesurée à zéro ; sondes : accélérateur, non garantie ; dilemme, non décorrélation ; pince en trois objets ; alerte = motif et dommage au même lieu, motif seul : audit, jamais témoin ; lemme resserré au reste ; veille à côté des chantiers ; réapprentissage non tranché, N-060 v3 tient ; quatre retouches après lecture (`docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v4.md`)

Ce que ce segment met à jour :
- Le renvoi au fichier consolidé `docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v4.md` (qui intègre la version 3 et ses trois errata déjà scellés). Note sur le décompte : ce segment sans point final mesure **597 signes** sans le chevron `>` ni son espace (format de la ligne 13 de `CLAUDE.md`, où les segments sont séparés par ` ; `) ; dans la section 12 de `decision-N-075-issue-plancher-et-deux-regards-v4.md` (ligne 267), le même libellé porte un point final et mesure 598 signes sans le chevron ni son espace.
- L'ajout de `GO-2026-11-23-32` et la mention des quatre retouches issues de la lecture sur document PDF des seize papiers (`R-5185` : pouvoir de séparation et non calibration pour Xu et al., réserve sur l'intervalle de confiance et l'audit des plus suspects pour Ge-Wang et al., répétition contre écart croissant pour Zhong et Raghunathan, retour d'étage et page 10 pour l'attaque étagée de McKenzie et al.).
- Aucune perte sur les décisions arrêtées ni sur les quatre accords antérieurs de novembre (l'état non tranché du réapprentissage sur l'oracle et la primauté de N-060 v3, la règle à deux clés exacte et la veille à côté des chantiers sont conservés), avec deux raccourcis de mots signalés pour rester sous le plafond de 600 signes : suppression de « à démontrer » après « lemme resserré au reste » (démonstration toujours requise au § 7 et au § 11 point 10 de la v4) et de « sur l'oracle » après « réapprentissage » (le réapprentissage visé au § 11 point 9 reste celui sur verdicts de l'oracle).
