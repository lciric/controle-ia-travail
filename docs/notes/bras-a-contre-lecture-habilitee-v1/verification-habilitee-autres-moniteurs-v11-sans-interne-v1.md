# Vérification habilitée du module des autres moniteurs, version 11 — sans interne — v1

- **Heure** : 2026-11-22T14:25:32Z (`date -u`).
- **Mandat** : `docs/notes/bras-a-contre-lecture-habilitee-v1/mandat-lecteur-habilite-module-v11-et-renvoi-base-v1.md`, `7854c2e5c39345d16c48d72cce06fef5d4cc5815b213835d38e98aa80488f63e`, partie 1. Accès inscrit au registre des décisions, ligne R-4887.
- **Lecteur** : Claude Opus 5.5, agent neuf habilité.
- **Objet** : la case de la ligne 1473 du brouillon 46 (`b5e1031c…`), et le module des autres moniteurs version 11 (`e1130dad…`), avec ses essais (`92711976…`), au commit `e13ed9282` de la branche `claude/bras-a-habilite-developpeur-v1`.

**Verdict : conforme.**

**« Seule l'empreinte de la préparation change » : vrai.** Le reste du différentiel de la version 10 à la version 11 n'est qu'un paragraphe d'en-tête, qui ne s'exécute pas. Aucun calcul ni aucune garde ne change.

**Essais : 4 passés sur 4** (essais de la version 11). Les essais de la version 10, rejoués sur la version 11, passent aussi : **77 sur 77**.

**Épreuve par retrait : 67 retraits mordent sur 67 joués.** Ce sont ceux de la version 10, plus deux propres à la version 11. Deux retraits hérités ne sont pas joués, comme pour la version 10, parce que leur texte a été remplacé en version 10.

**Épreuve de forme** : rejouée sur la version 11. Elle rend les mêmes formes que pour la version 10, et ne diffère que par ce qui varie d'un passage à l'autre et par la provenance attendue.

**Rapport interne** : `docs/notes/bras-a-contre-lecture-habilitee-v1/verification-habilitee-autres-moniteurs-v11-interne-v1.md`, branche `claude/bras-a-habilite-developpeur-v1`, commit `7997441b0535c3ce1245b6208b07dd85359baf1a`, sha256 `20544e8d71f04a0df7d55b7c7cb357940625137283bcddf339329461bc6a1771`.

Cette pièce ne dépense rien et n'autorise rien.
