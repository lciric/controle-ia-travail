# Contrôle court du différentiel v3 → v4 — additif des interrupteurs de l'orchestrateur v69 — v1

- Contre-lecteur, modèle O : l'auteur du contrôle v2 → v3 (`controle-differentiel-additif-orchestrateur-v69-v2-v3-v1.md`, `12bbec8ded9c0e22eb257ebc03e193a7ec02d4cab2294c3fda036a5e904f7a4c`). Je n'ai écrit ni la v4 ni son JSON. Écrit le 2026-11-20.
- V69 : `docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v69/`. Les pièces sont lues sur disque ; le message de la session coordinatrice les situe au commit 77357888.
- Processeur seul. Aucune écriture dans le dépôt, aucun commit, aucune dépense. Seul l'outil de remplacement a été lancé, sortie dans mon dossier. **Aucun refus de permission, de classifieur ni de garde.**

## Verdict

**Conforme.**

## 1. Vérifications

- **Empreintes.** `sha256sum -c` passe sur les cinq compagnons :
  - additif v4 : `cb352811f0202aa530fa4fd94de1d7ed4e6a8d589584c06c24c915e3c73bb578` ;
  - JSON : `5a993871e1bcf7800ae5a33c25f4186101d1fee43cf10156603d771430c3a4c3` ;
  - journal des remplacements ;
  - différentiel : `6e534cdb1d943f2cfb1539381458debbda5119aa4ab6bb9e6068795d89c6d6e2` ;
  - rapport : `a8c129ebc2bf549670e41598a46ee79a36f7ae8917f50658842fb602aeec349d`.

  La v3 est intacte (`f71e3a55…`), le cadre v3 aussi (`b1822613…`). L'outil est inchangé (`391db990…`).
- **Point 1 — rejeu.** J'ai rejoué l'outil sur l'additif v3 avec le JSON. Il rend « FAIT : 9 remplacement(s) », sortie `cb352811…` ; `cmp` contre la v4 ne trouve aucune différence. **Égal à l'octet.**
- **Point 2 — corrections.** Le différentiel, lu en entier, contient neuf zones :
  - Correction 1 : ligne « Statut », « cet additif change ». Portée à la lettre.
  - Correction 2 : § 1.2, dernier alinéa, « dans une version neuve ». Portée à la lettre.
  - Correction 3 : § 1.2, « Ce que (a′) lève ». Portée à la lettre.
  - Correction 3 bis : tête de l'additif. Portée à la lettre.
  - Correction 4 : garde 6, artefact. Portée à la lettre.
  - Le reste est de la tenue : titre, ligne de version, ligne « Statut ». Rien d'autre ne change.
- **Point 3 — les trois points laissés par le rédacteur.**
  1. « Aucun des trois rédacteurs (v1, v2, v3) » dans une v4 : **non exigé**. La phrase reste vraie de ceux qu'elle nomme, et le rapport de la v4 dit que son auteur n'a pas lu le code non plus. C'est de la tenue pure.
  2. La ligne « Mandat » ne cite pas le mandat de la v4 : **non exigé**. Ce mandat est nommé avec son empreinte au rapport de la v4 (`3163abf1…`), qui accompagne la pièce. C'est de la tenue pure.
  3. Le rang 4 sur la phrase du différentiel : **non exigé, et juste.** La phrase de la v3 sur son propre différentiel est remplacée par celle qui vise le différentiel v3 → v4. Le contrôle déjà fait de la v3 est dit dans la partie en gras.
- Aucun allumage n'est accordé, et aucun identifiant de modèle n'apparaît dans les zones changées.

— contre-lecteur, modèle O
