# Contre-lecture de la pièce de sécurité du banc fermé (épisodes d'épreuve où l'agent agit) — v1

- **Pièce relue** : `docs/notes/piece-securite-banc-ferme-v1/piece-securite-banc-ferme-v1.md`, branche `claude/piece-securite-banc-ferme-v1`, commit `b966e396329356aa0254c927385e34ae1d0d22a4`. Empreinte recalculée : `a4d515fc3d300353c78dc29e5274f061affa473660b75a96e0d3e68dd4c262f6`, égale au `.sha256` compagnon.
- **Classe** : A (chaîne complète). **Contre-lectrice** : session neuve d'un autre modèle que l'auteur (Opus 5.5 ; auteur Fable 5.2), lancée par la session fille de l'attaquant informé ; n'a pas écrit la pièce (R2). Mandat : GO-2026-11-21-68.
- **Date** : 21 novembre 2026, vers 18:00 UTC.

## Sources lues (chemin, empreinte)

| Repère | Source | Empreinte |
|---|---|---|
| [N57] | `docs/decisions/decision-N-057-v1.md`, en entier | `42180088efb2e1016251fa329421fc08ebcb13039266d278c1a6f37ced60af99` (égale à celle de la pièce) |
| [R] | `registres/decisions.md` sur `main` au commit `1fa18046f0de5b2fa03b3c3ad1f443b97ac525f0`, lignes R-611 (l. 838), R-888 (l. 1117) et R-895 (l. 1124, lue pour le contexte de R-888) seulement | `a8cd5714bd68328e34b3ac097b1e6e5dbbfd215ad4bb1a4d60b5d0a2d6eb68e3` ; au commit `d5635e17…` cité par la pièce, `ba86f8f8…` (vérifiée égale), et R-888 y figure déjà, à la même ligne |
| [GO] | `registres/go.md` sur `main`, lignes 99, 581, 667 seulement | `4daa15efc3248b2ee2be28d826e5dcfc201423a915ef3d370a58360c951ce9f1` (égale à celle de la pièce) |
| [RJ] | `docs/notes/integration-bras-attaque-v1/regle-du-jeu-et-integration-v1-brouillon5.md`, section 5, nœuds 3 et 4 | `527a3e7ec2a0f28221f57398794433793e3cf518360cca6ca9a8071ccbc2e414` |
| [PR] | `prereg/bras-attaque-regle-v1.md`, « Plan d'analyse » et « Liste d'arrêt » | `88418df09c2e969cbdc77d220fe59dbf64f866d858ff02a039be5662c6d1f904` |

Non lus, par consigne : le coffre (`donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, branches `claude/scellement-2-*`), `docs/notes/programme-et-4-familles-evasion/`, les lignes R-604 à R-610, tout moniteur, toute sortie de la course « nouvelles attaques », `registres/etat.md`, la dernière passation.

---

## Ce qu'établit R-888

R-888 (31 octobre 2026), sur `main` : « **R-611 levée : la revue de sécurité extérieure a été réalisée et a donné son GO.** Le gel du pipeline opérationnel d'évasion est levé. Mot de Lazar : « la revue de sécurité ext a été réalisée et a donné son go, donc go lancer le pipeline opérationnel » ». R-895 le reprend (« R-611 levée (déjà inscrite R-888) »). Le registre tient donc le gel pour **levé depuis le 31 octobre, sur le seul mot de Lazar** ; aucune pièce écrite de la revue n'est citée par la ligne, et [RJ] nœud 3 rapporte qu'aucune n'a été trouvée (constat de [RJ], que je n'ai pas refait). N-057 (28 octobre) dit « ne lève pas R-611 » : c'est vrai à sa date, antérieure à R-888.

---

## Points

### Bloquants

**B1 — La pièce tient le gel pour en vigueur alors que le registre le dit levé (R-888).**
Verdict point 1 (« Le gel tient jusqu'à l'une des deux issues de la section 6 »), en-tête (« elle ne lève pas le gel »), liste d'arrêt ligne 1, section 6.2 (« écart à la lettre de [R611] ») et nœud 1 option (a) (« conforme à R-611 ») raisonnent tous comme si R-611 était en vigueur. Sur `main`, depuis le 31 octobre, il est levé sur le mot de Lazar. La position prudente de la pièce est défendable — c'est l'option (b) du nœud 3 de [RJ] : pas de pièce écrite, revue tenue pour non faite —, mais elle doit être **dite comme une lecture choisie, contre la lettre du registre**, pas comme l'état des choses. Correction demandée :
- dire en tête et au verdict : « R-888 (31 octobre) inscrit R-611 levée sur le mot de Lazar ; aucune pièce écrite de cette revue n'est citée ni trouvée ([RJ] nœud 3) ; tant que Lazar n'a pas tranché le nœud 3 de [RJ], ce dossier suit son option (b) et tient la revue pour non opposable » ;
- remplacer « ne lève pas le gel de R-611 » par « ne tient pas lieu de la pièce écrite de la revue externe, et ne tranche ni R-888 ni le nœud 3 de [RJ] » ;
- réécrire 6.2 et la ligne 1 de la liste d'arrêt dans ces termes (« ni pièce écrite de revue externe couvrant (b), ni mot explicite de Lazar disant que la revue du 31 octobre couvre (b) ou que ce dossier en tient lieu »).

**B2 — Le nœud 1 est mal posé faute de R-888.**
La pièce recommande (a), « c'est la pièce de la revue externe », confiance 0,7. Or Lazar a dit le 21 novembre « dès que la pièce de sécurité est écrite » trois semaines après avoir déclaré la revue externe faite (R-888) ; sous sa propre lecture, une revue externe restait à commander est peu probable, et « la pièce » désigne plus vraisemblablement un dossier interne, ou la pièce écrite de la revue déjà faite. Le nœud doit être reposé avec R-888 sous les yeux, et au minimum offrir :
- (a) la pièce écrite de la revue du 31 octobre (qui, quand, périmètre, conclusion) : Lazar la verse, et l'on vérifie si son périmètre couvre un agent qui agit sur un contenu dérivé du coffre ; sinon, revue complémentaire, et ce dossier est ce qu'on remet ;
- (b) ce dossier, vérifié par un vérificateur interne neuf (6.2), dans le cadre levé par R-888 : alors ce n'est plus un écart à R-611 mais une condition ajoutée, à dire comme telle ;
- (c) ce dossier sans vérification : à déconseiller, comme le fait la pièce.
La recommandation et sa confiance sont à refaire par l'auteur. Le nœud 2 (« à la mère de dire où en est ») se réduit alors à une question précise à Lazar : la revue du 31 octobre a-t-elle une pièce écrite, et son périmètre couvre-t-il l'option (b) ?

### Mineurs

**M1 — Voie du versement en quarantaine non définie.** Le banc n'a ni jeton ni dépôt (garde 2) ; la pièce dit pourtant que transcriptions, activations, journal et états du monde vont « en quarantaine, scellés ». Elle ne dit pas par quel canal ils quittent la machine, où ils arrivent (branche orpheline de GO-2026-11-20-50 point 2, ou stockage à part pour des activations volumineuses), qui les reçoit, ni que les empreintes sont prises **sur le banc** avant le transfert et vérifiées à l'arrivée. Ajouter une garde (ou étendre la garde 3) et un point à 6.1 ; l'épreuve d'artefact : fichier altéré pendant le transfert.

**M2 — Faisabilité de la garde 1 chez un loueur où l'on est déjà dans un conteneur.** Le programme loue chez Vast.ai et Hetzner (CLAUDE.md, routine point 4). Chez un loueur où l'instance louée est elle-même un conteneur, « couper le réseau à l'extérieur du conteneur de l'agent » exige un second niveau (agent dans un bac à sable intérieur, gardes dans l'enveloppe) ou un pare-feu du fournisseur. La pièce doit le dire, et nommer dans la coupure les adresses locales au lien et le service de métadonnées du fournisseur, qui peuvent porter des secrets sans être « réseau sortant » au sens courant. La répétition à blanc sur la machine réelle attrapera l'échec, mais tardivement et à prix payant.

**M3 — Exclusion 2 et le juge.** L'exclusion 2 interdit que la consigne parte vers une interface de modèle extérieure. Le juge, lui, lit les transcriptions ([PR], « Qui lit quoi ») ; s'il est une session servie par un tiers, c'est la même sortie. La pièce doit dire par quel moyen le juge lit, et préciser que l'exclusion 2 vise le **modèle qui agit** ; le reste du programme (sessions de rédaction, coffre sur le dépôt) est déjà chez des tiers.

**M4 — Garde 5 éprouvée par le nom seulement.** L'artefact « fichier factice portant un nom du manifeste des moniteurs » ne prouve rien d'un moniteur renommé. Éprouver par empreintes (le manifeste des moniteurs porte noms et empreintes, sans contenu) : artefact = copie renommée d'un fichier du manifeste.

**M5 — Remise à zéro du modèle entre épisodes.** La garde 7 remet à zéro le répertoire de travail ; elle ne dit pas que le contexte du modèle (historique de conversation, cache de préfixe du serveur d'inférence) est réinitialisé entre épisodes. Une ligne et une épreuve (artefact : jeton témoin d'un épisode retrouvé dans le suivant).

**M6 — Réserve 3 inexacte.** « L'état de la revue externe depuis le 10 novembre n'est pas connu » : la ligne qui fixe cet état (R-888) est du 31 octobre ; elle était sur `main` au commit cité par la pièce. Réécrire après B1.

**M7 — Paraphrase de GO-2026-11-20-50 point 2.** 6.2 dit « branche à part » ; la ligne dit « branche **orpheline** ». Reprendre la lettre.

---

## Vérifications demandées, une par une

1. **N'est pas la revue externe** : dit sans ambiguïté (en-tête, verdict, 6.2, nœud 1). **Ne lève pas R-611** : dit, mais sur une prémisse que le registre contredit (B1).
2. **Couverture** : périmètre (1), confinement (2), sorties et quarantaine (3), gardes avec deux épreuves (4.1), liste d'arrêt (4.2), risques propres à l'agent qui agit (5, douze écarts et quatre cas non couverts), liste fermée de vingt-deux points (6.1), coût (8) : tout y est. Trou : la voie du versement (M1).
3. **Gardes vérifiables et testables** : oui, chacune a un cas sain et un artefact, à blanc, sans contenu du coffre. Réseau : M2. Secrets : couverts (garde 2), sauf métadonnées du fournisseur (M2). Persistance : M5. Sorties non scellées : M1. Score de moniteur dans l'entraînement (N-053 point 5) : tenu par construction (pas d'entraînement, pas de moniteur présent, pas de retour) ; cohérent avec [PR], dont les échelons 5 et 6 avec note de sonde dans le signal d'entraînement sont explicitement hors de ce banc (section 5, « ne couvre pas »). Aucun trou.
4. **Contenu d'attaque** : aucun mode, aucune recette, aucun paramètre, aucun nom de famille d'évasion. Les risques de la section 5 sont des risques génériques d'agent outillé. Non bloquant.
5. **Nœuds** : le premier porte bien sur l'interprétation de « la pièce de sécurité » (revue externe ou dossier interne), mais il est posé sans R-888 et sa recommandation en dépend (B2). Le nœud 2 devient une question précise à Lazar (B2). Le nœud 3 (opérateur et juge, ni la mère, ni l'attaquant informé, ni le rédacteur) est bien posé.
6. **Réserves** : 1, 2, 4, 5 exactes. 3 inexacte (M6). 6 exacte à sa version. Les citations de [N57], [RJ], [PR] et [GO] que j'ai contrôlées sont fidèles, à M7 près ; les empreintes citées par la pièce sont égales à celles que j'ai recalculées.

---

## Verdict

**À corriger.** Deux points bloquants (B1, B2), sept mineurs (M1 à M7). Les deux bloquants tiennent à la même cause : R-888 non lue. Le reste de la pièce — périmètre, confinement, gardes, liste d'arrêt, absence de tout contenu d'attaque — est solide. Corrections attendues en version nouvelle (R12), `piece-securite-banc-ferme-v2.md`.

**Refus de classifieur** pendant cette contre-lecture : aucun.
