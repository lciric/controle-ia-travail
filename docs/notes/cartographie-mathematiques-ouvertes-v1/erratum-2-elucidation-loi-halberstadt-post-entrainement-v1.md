# Erratum 2 à la note d'élucidation sur l'évasion sous filtrage pendant l'entraînement après pré-entraînement (billet de Yair Halberstadt)

- **Pièce corrigée** : `elucidation-loi-halberstadt-post-entrainement-v1.md` (`bf9d442d…`), laissée telle quelle.
- **Erratas antérieurs** : `erratum-1-elucidation-loi-halberstadt-post-entrainement-v1.md` (fille 1, commit `b1006d58`) et `publication-evasion-post-entrainement-v1/variante-b-v3-session-fille-2/elucidation-loi-halberstadt-post-entrainement-v1-erratum-1.md` (fille 2). Les deux restent en vigueur. **Le présent erratum prime sur eux pour les conditions H1 à H3.**
- **Origine** : vérification de fidélité des v3 par un contre-lecteur Opus neuf (`publication-evasion-post-entrainement-v1/variante-b-v3-session-fille-2/rapport-fidelite-v3-contre-lecteur-opus-v1.md`, défaut B-1). Classe C, 24 novembre 2026.

## Point corrigé

**§ 4, conditions H1, H2 et H3** (« Pour qu'un entraînement après pré-entraînement aboutisse à un agent déployé qui à la fois privilégie la triche furtive et mette en échec la surveillance de déploiement, il faut… »). Ces trois conditions ne sont **ni nécessaires ni suffisantes**, et ne doivent plus être présentées comme telles.

- **Pas nécessaires** : rien ne démontre qu'éviter une évasion efficace au déploiement exige de rompre l'une d'elles (audit indépendant, correction 6).
- **Pas suffisantes** : sous la pénalité, une covariance positive entre la survie au moniteur de la boucle et la survie à l'audit ne fait pas, à elle seule, monter la survie à l'audit aux fortes pressions. Contre-exemple : $\beta_{\text{boucle}} = (0{,}1 ; 0{,}5 ; 0{,}9)$ et $\beta_{\text{audit}} = (0{,}1 ; 0{,}95 ; 0{,}45)$, sur trois atomes équiprobables. La covariance est positive, mais la survie à l'audit passe de $0{,}5$ à environ $0{,}459$ pour $k = \eta(\Delta R + C) = 10$, et tend vers $0{,}45$.
- **H1 incomplète** : sous le rejet pur, H1 omet le terme $\log(\beta_{\text{h}}/\beta_{\text{f}})$. Le critère exact est celui de R1.

Les trois régimes R1, R2 et R3 restent ce qu'en disent la v4 du paquet et les errata 1 : trois mécanismes, dont aucun n'est revendiqué comme nécessaire, et qui ne forment pas une classification exhaustive.
