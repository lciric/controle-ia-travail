# Provenance du code lu pour BEYOND (Huang et Fan, arXiv 2603.14288 v2) — v1

- **Lecteur : modèle I.** Relevé fait le 2026-11-18T02:02:01Z (`date -u`) ; premier relevé du commit 2026-11-18T01:53:42Z.
- **Origine** : `https://github.com/allenh16/agentic-factor-investing` (`git remote -v`), dépôt de la page du projet annoncée p. 1 et p. 47 du PDF (`docs/sources/pdf/lecture-o4-v1/arxiv-2603.14288/2603.14288v2.pdf`, sha256 `8fe2b21770af074a0e13667048bc40b3eb85fc03ecde8f5d58938e3aa100e301`).
- **Clone** : trouvé sur disque dans le dossier de travail de la session (`code-o4/agentic-factor-investing`), fait par la session mère, non par moi ; lu seulement, aucun programme lancé, rien installé, aucun accès réseau.
- **Commit** : `cc8bd7d06c26f39dc379157208482fe0da19623e` (`git rev-parse HEAD`), daté du 2026-03-14 18:32:09 +0800 (`git log -1`) ; clone superficiel (`git rev-parse --is-shallow-repository` : vrai), un seul commit visible, branche `main`.
- **Licence** : aucun fichier de licence dans le dépôt (`git ls-files` : 4 fichiers, aucun nommé LICENSE ou approchant) ; le mot `licen` n'apparaît dans aucun des trois fichiers textuels. Licence : **absente** au commit relevé.
- **Code du système** : absent. Le dépôt ne contient que la page du projet (HTML et son script d'affichage), les données de son graphique et une image.

## Fichiers (`git ls-files`), empreintes et lecture

| fichier | octets | sha256 | lecture |
|---|---|---|---|
| `README.md` | 26 | `2e38d983d7a532ca9c88213c40fb7bec59546b64010e05f13e520d7accb8e46f` | lu en entier (une ligne, son titre) |
| `chart_data.json` | 20479 | `c87623d8ac771ad190fa4b6afd3819ed8429bbdd0f4708774a245e4d80777164` | lu en entier comme donnée (502 points, clés de date, de série linéaire et de série en arbres) |
| `index.html` | 17798 | `2a5839f1bd25e3b45e16aa036085c8cd3824c2e8c43b6bdd9a7ef8b72324ff68` | lu en entier (507 lignes) |
| `project-framework.png` | 1037489 | `8aa8919aa043ddae3e6cab6f44fd1a96fc03cbc812f60c7cda80cfefd03b6144` | non lu (image) ; empreinte seulement |

Le code n'est pas versé dans le dépôt du programme. Lecture : `docs/notes/lecture-o4-suite-v1/lecture-entiere-beyond-o4-v1.md`, section 4.
