# Correctif 1 de la variante B, après la vérification de fidélité (une seule boucle)

- **Source** : `rapport-fidelite-v3-contre-lecteur-opus-v1.md`, dans ce dossier. Contre-lecteur Opus neuf, effort élevé, qui n'a rien écrit des pièces. Verdict : les deux portées sont « fidèles avec réserves ». Il recommande la variante B comme base, avec cinq reports.
- **Règle** : les pièces de la variante B restent telles quelles. Les corrections vont dans des fichiers neufs, suffixés `-correctif-1`. La v3 de référence (`b1006d58`) n'est pas touchée, sur consigne de la mère.
- **Constats du contre-lecteur, vérifiés par la session** : $\pi_A(\Pi_h) = 0{,}85/(0{,}85 + 0{,}024\,e^{2}) = 0{,}827382$. Contre-exemple à la suffisance de H1 à H3 sous la pénalité : $\beta_{\text{boucle}} = (0{,}1 ; 0{,}5 ; 0{,}9)$ et $\beta_{\text{audit}} = (0{,}1 ; 0{,}95 ; 0{,}45)$ ; la covariance est positive, et pourtant la survie à l'audit passe de $0{,}5$ à $0{,}459$ en $k = 10$.

| Défaut | Gravité | Correction | Fichiers |
|---|---|---|---|
| B-1 : « arises in particular when (H1)–(H3) » affirme une suffisance, fausse sous la pénalité ; H1 omettait $\log(\beta_h/\beta_f)$ | majeur | Paragraphe H1 à H3 retiré. Ouverture neuve, sur le modèle de la v3 de référence : ni exhaustivité, ni nécessité, ni suffisance revendiquées, avec la mention du cas de covariance positive sous la pénalité | `manuscrit-arxiv/main-v3-correctif-1.tex` (§ 3) et `.pdf` (11 pages) ; `billet-…-en-v3-correctif-1.md` (§ 4, phrase d'ouverture) |
| B-2 : « $< 1$ » faux quand $\beta_v = 0$ | mineur | « vaut un seulement si $\beta_v = 0$, et peut être petite » ; dans la proposition, « strictement sous un quand $\beta_v > 0$ » | manuscrit (point 4(a), proposition) ; billet (§ 3, point 3) |
| B-3 : 0,827379 au lieu de 0,827382 | mineur | 0,827382 partout où figure $\pi_A(\Pi_h)$ | manuscrit (remarque sur la niche, légende et texte de la table 3) ; billet (paragraphe sur la niche) |
| B-4 : Korbak, Perez et Buckley 2022 absent du commentaire | mineur | Phrase d'antériorité ajoutée (Price, Robertson, Fisher, Korbak et al. 2022) | `commentaire-…-en-v3-correctif-1.md` |
| B-5 : compagnon `.sha256` de la contre-lecture de Carbon | mineur | **Non traité**, sur consigne de la mère, qui tranchera (la v3 de référence a versé un `.v2.sha256` concordant) | — |

**Non repris** : le report facultatif n° 5 (l'opérateur A coïncide avec un entraînement sans moniteur suivi d'un rejet unique à l'inférence). Il n'est pas dans la liste fermée, et je ne l'ai pas vérifié.

**Reste avant diffusion** : vérifier sur PDF les références Price, Robertson, Fisher, Korbak et al. 2022 et 2025, et Bailey et al. 2024 (R7). Le geste de diffusion appartient à Lazar.
