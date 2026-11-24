# Erratum 1 — compagnon d'empreinte de la contre-lecture de Carbon (dossier de publication v1)

- **Pièce** : `contre-lecture-carbon-high-publication-v1.md`, empreinte `ae7ab7d1d8d7c1281c753254fde32b65e0db9e6538b1bca32d2e7887ba21e1e1`.
- **Décision** : de la mère, le 24 novembre 2026. Écrit par la fille 2 du papier D.

1. **Le compagnon de référence est `contre-lecture-carbon-high-publication-v1.md.v2.sha256`**, versé par la fille 1 (commit `b1006d58`). Il porte le nom de base seul et l'empreinte `ae7ab7d1…`, qui concorde avec le fichier. Pour vérifier :
   ```
   cd docs/notes/cartographie-mathematiques-ouvertes-v1/publication-evasion-post-entrainement-v1
   sha256sum -c contre-lecture-carbon-high-publication-v1.md.v2.sha256
   ```
2. **L'ancien compagnon, `contre-lecture-carbon-high-publication-v1.md.sha256`, est laissé tel quel** (règle des versions). Il porte un chemin de machine étrangère (`/home/antigravity/…`) avec la même empreinte. C'est lui qui fait échouer `verifier-arbre` sur ce fichier ; l'écart est connu et consigné, et ne signale aucune altération du contenu.
