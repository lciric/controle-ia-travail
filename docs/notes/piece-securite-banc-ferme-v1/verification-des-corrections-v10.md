# Vérification des changements — pièce de sécurité du banc fermé, v11 — v10

- **Pièce vérifiée** : `docs/notes/piece-securite-banc-ferme-v1/piece-securite-banc-ferme-v11.md`, branche `claude/piece-securite-banc-ferme-v1`, commit `bdaf4ed0dae053d8eac9911bd4df95310e97e510`. Empreinte recalculée : `af4291069db6cff8c65608884875dd70abc8d4bcc45407ec8a1b0c623a3fa5cd`, égale au `.sha256`. La v10 est intacte (`bf19bdd0…`).
- **Référence** : `verification-des-corrections-v9.md` (`ef700638…`), qui acceptait la v10.
- **Vérificatrice** : la même contre-lectrice (Opus 5.5). **Date** : 21 novembre 2026, vers 19:45 UTC.
- **Méthode** : différence ligne à ligne entre la v10 et la v11. Elle porte sur les lignes 1, 9, 10, 175, 250, 437 et 448, plus la section 17 neuve, et sur rien d'autre.

## Constat

1. **Ligne 250, liste d'arrêt.** Dans la v10, la ligne « contenu de quarantaine sur le point de sortir autrement que par 3.2 » datait de la v1. Elle arrêtait à la lettre la voie d'envoi ouverte en v8. La v11 écrit « autrement que par l'un des deux passages gardés », avec les sections 3.2 et 3.5 nommées. La correction est juste et ne relâche rien : les deux passages ont chacun leurs gardes et leurs lignes d'arrêt. **Je n'avais pas relevé cette contradiction en contre-lisant la v8.** La contre-lectrice du préenregistrement de la course l'a vue ; je le consigne ici. J'ai aussi cherché « par 3.2 », « seul passage » et « un seul passage » dans la v11 : il n'en reste que dans les tables de changements des versions passées, qui décrivent l'état ancien. C'est conforme.
2. **Ligne 175, condition 11, et ligne 448, réserve 17.** Mes deux remarques sur la v10 sont prises en compte. La règle de famille est dite en termes généraux, les familles exclues sont renvoyées à l'audit des lignées de la mère, et le cas signalé par [CF] retrouve son conditionnel (« *si* le panel des juges du papier C lit ces épisodes »). C'est conforme à [CF] 1.3.
   **Remarque, sans point** : la condition dit « cette pièce ne nomme aucune famille exclue » et rapporte pourtant, à titre de signalement conditionnel, le nom de la famille que [CF] cite. Il n'y a pas contradiction, puisque le nom n'est pas une exclusion décidée. On peut l'accepter tel quel.
3. **Section 17 et note sur la section 16.** Elles décrivent fidèlement la différence et disent laquelle des deux rédactions de la condition 11 fait foi. Il n'y a aucun changement non déclaré.
4. **Lignes 9, 10 et 437** : mises à jour de version, exactes.

**Contenu d'attaque** : aucun. **Refus de classifieur** : aucun.

## Verdict final

**Accepté** : la pièce de sécurité du banc fermé, v11 (`af429106…`).

Bilan de toute la chaîne, de la v1 à la v11 : 3 points bloquants et 16 mineurs relevés par moi, tous corrigés. S'y ajoute une contradiction de la liste d'arrêt que je n'avais pas vue et qu'une autre contre-lectrice a relevée, corrigée en v11.

L'acceptation n'autorise ni construction, ni course, ni envoi, ni dépense. Les préalables restent ceux de `verification-des-corrections-v8.md` et `verification-des-corrections-v9.md`.
