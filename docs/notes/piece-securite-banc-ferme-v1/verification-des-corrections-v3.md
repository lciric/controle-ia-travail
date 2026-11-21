# Contre-lecture des changements de la v4 — pièce de sécurité du banc fermé — v3

- **Pièce vérifiée** : `docs/notes/piece-securite-banc-ferme-v1/piece-securite-banc-ferme-v4.md`, branche `claude/piece-securite-banc-ferme-v1`, commit `1409f1bfc2671ba08838115ceb4261b019b71867`. Empreinte recalculée : `a1a833e429f64ebf19a94200dad6d7cb88651c628234696328307f059c02d473`, égale au `.sha256`. Les v1 à v3 sont intactes, toutes recalculées (`a4d515fc…`, `0064c4be…`, `d016d9d9…`).
- **Référence** : `verification-des-corrections-v2.md` (`658f6237…`), qui acceptait la v3.
- **Vérificatrice** : la même contre-lectrice (Opus 5.5). **Date** : 21 novembre 2026, vers 18:45 UTC.
- **Méthode** : différence ligne à ligne entre la v3 et la v4, relue contre la table de la section 11 de la v4.
- **Source neuve [ML]** : `registres/passations/2026-11-21-1750-attaquant-informe-mot-lazar-verificateur-interne-banc-ferme.md`, au commit `3df76fac`. Empreinte recalculée `27c16352…`, égale à son compagnon. Comme c'est une passation, je ne l'ai pas lue en entier. J'en ai extrait le titre, la ligne du mot verbatim (l. 4) et la ligne qui dit « écart » (l. 9), rien de plus.
- **Registre** : sur `main` au commit `0fef6d1a`, `registres/go.md` ne porte pas encore le mot.

## Ce qui est juste

- **Le mot de Lazar est cité verbatim, conforme à [ML] l. 4** : « go reco vérificateur interne neuf; on met de cote la revie externe jusqu a publication du papier ».
- **Point 1 de l'auteur** (« (a) en parallèle » non retenu ; la revue externe reste due avant toute sortie hors quarantaine) : c'est la lecture au plus près. « Mise de côté jusqu'à publication » exclut la pièce écrite comme préalable à la course, et le sixième garde-fou de GO-2026-11-20-50 couvre déjà la sortie.
- **Point 2 de l'auteur** (« écart déclaré ») : conforme à [ML] l. 9, qui le dit en ces termes. La réserve 9 attribue bien cette lecture à la note, non au mot de Lazar.
- **Point 3 de l'auteur** : le vérificateur n'est ni l'opérateur ni le juge, et il ne lit pas le coffre. L'ajout est déclaré comme tel et sain : on ne vérifie pas son propre banc. Le nœud 3 est étendu au vérificateur, et les trois noms sont distincts.
- **Point 4 de l'auteur** : rien ne se construit ni ne s'exécute tant que le mot n'est pas lisible au registre des GO sur `main`. C'est juste, conforme à la garde de calcul du dépôt (un lancement cite une ligne de `registres/go.md`).
- **Section 6.3** :
  - elle ne prête au mot ni lancement, ni dépense, ni nom, ni date ;
  - le vérificateur rend une pièce scellée point par point, avec chemins et empreintes ;
  - un seul « non » ou « non vérifiable » vaut « pas de course » ;
  - la phrase d'entretien ne présente pas la vérification interne comme la revue.
- **Contenu d'attaque** : aucun. **Refus de classifieur** : aucun.

## Points

**V1 — mineur — Contradiction sur l'ordre des gestes.** La ligne neuve de l'en-tête (l. 6) dit que le mot « n'ouvre ni course, ni dépense, ni **construction** avant la vérification interne ». La liste d'arrêt, première ligne neuve, et la section 6.3 (« Quand », « Ordre des gestes ») disent l'inverse. Les gardes sont construites et éprouvées à blanc **avant** la vérification, qui porte sur elles, et la répétition payante vient avant la pièce finale du vérificateur. La version juste est celle de 6.3. L'en-tête doit dire : rien ne se construit avant que le mot soit lisible au registre des GO ; aucune course avant la pièce du vérificateur ; aucune dépense sans devis et GO.

**V2 — mineur — En-tête resté dans l'état de la v3.**
- l. 4 : « ce qu'un relecteur externe, ou Lazar à sa place, doit pouvoir vérifier » doit nommer désormais le vérificateur interne neuf. Le relecteur externe ne vient qu'avant publication.
- l. 5 (point 5 de l'auteur) : « ce dossier suit par choix son option (b) » n'est pas faux, puisque le nœud 3 de [RJ] n'est pas tranché. Mais cette ligne décrit un état dépassé. Elle doit dire que, depuis [ML], la question de la pièce écrite de la revue du 31 octobre n'est plus un préalable à la course, et qu'elle le redevient avant publication, comme le dit la réserve 3. Je demande la réécriture.

**V3 — mineur — « sera citée par erratum ».** L'en-tête et la réserve 8 prévoient d'ajouter l'identifiant de la ligne du registre des GO par erratum. Or, selon l'allègement (GO-2026-11-19-26 et -27), l'erratum ne vaut que pour les classes B et C. La pièce est de classe A : l'identifiant viendra par une version nouvelle, contre-lue sur sa seule différence. Il faut écrire « par une version nouvelle ». Si V1 et V2 sont corrigés après l'inscription de la ligne par la mère, l'identifiant peut entrer dans la même v5.

## Verdict

**À corriger** : trois points mineurs (V1 à V3), aucun bloquant. Le fond de la v4 est accepté : la décision portée, la section 6.3 et la liste d'arrêt. Une v5 qui ne change que l'en-tête (l. 4 à 6) et la réserve 8 sera vérifiée sur sa seule différence (`verification-des-corrections-v4.md`).
