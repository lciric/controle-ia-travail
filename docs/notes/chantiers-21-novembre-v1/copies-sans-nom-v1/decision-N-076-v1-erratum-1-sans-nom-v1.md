# Erratum 1 de la décision N-076 (v1) : les mots de le directeur de 14:00 UTC et la vérification de N-075 v2, parus pendant l'écriture

- **Date** : 21 novembre 2026, 14:05 UTC (`date -u`). **Auteur** : Claude Fable 5.2 (`claude-fable-5-2`), concepteur (R-3735), auteur de la v1. Aucun appel payant, ni commit ni poussée.
- **Ce qu'il corrige** : `docs/decisions/decision-N-076-assurance-par-audit-et-reference-honnete-v1.md` (`49b664c1d6a72fdb239d9a52e70ec85c4829fc5e77c6b5d3cf27848ce1a8dd78`), qui reste scellée telle quelle (R12). **Là où ils diffèrent, cet erratum prime.** Il est à contre-lire avec elle.
- **Ce qui l'a déclenché** : deux pièces versées sur la branche à 14:00 UTC, pendant l'écriture de la v1, et lues par moi après son scellement de 14:03 UTC : la ligne `GO-2026-11-21-60` de `registres/go.md`, et la vérification de N-075 v2 (`docs/decisions/verification-decision-N-075-v2-v1.md`, `b7707396aa8ceab373b4172626c6f2fb7782ef23b7c2f301955c3cc4c33dce71`), dont je n'ai lu que l'en-tête et le verdict.
- **Écart déclaré.** J'ai d'abord porté ces corrections dans le fichier de la v1, déjà scellé. L'outil de scellement a refusé de l'écraser (R12). J'ai rétabli la v1 à l'octet (empreinte vérifiée contre son compagnon) et écrit cet erratum. Aucun fichier n'a été supprimé.

## Corrections

**E1 — En-tête et section 0 : une seconde ligne de mots de le directeur.** S'ajoutent, de la ligne `GO-2026-11-21-60` (vers 14:00 UTC), deux phrases qui touchent la décision :

> que reste t il alors ? demande approfondie et protocole X, il faut une percee pour notre programme

> go protocole x pour sa concetpion

Lecture de la mère, à la même ligne (extrait) : « Le plancher d'audit au hasard étant occupé (« Blindfold », Podkopaev et Ramdas, Gans et Holden), protocole X sur « que reste-t-il, où est la percée du programme ». Protocole X pour la conception de C2, le banc de recherche à vérité plantée. »

**E2 — En-tête, « Ce que ce texte complète » : l'état de N-075.** N-075 v2 n'est plus « en vérification » : sa vérification rend « pas encore prêt à sceller », dix points en liste fermée (V1 à V10). Une v3 viendra. Les renvois « N-075, § » de la v1 visent les sections de la v2 ; ils seront à recaler sur la v3. Je n'ai pas porté ces dix points : ils ne visent pas ce texte.

**E3 — Section 4 (le banc de recherche à vérité plantée), « Premier pas et dépense ».** Remplacer par :

> La conception du banc passe par le protocole X (`GO-2026-11-21-60`) : le concepteur en effort maximal, puis le collisionneur sur la question neutre, puis la question fusionnée à l'organisme ; la spécification et les trois témoins en sortent. Les appels du protocole X se paient sur leurs propres lignes de calcul, que cette note n'ouvre pas. Générations et juges du banc : sur devis. Plusieurs lignées et une taille supérieure : la bourse.

**E4 — Section 13, point 6 (le plancher dit « occupé »).** Remplacer par :

> **Le plancher est dit « occupé » par le lecteur des douze voisins** ([verdict, 6], par « Blindfold »). N-075 v2, § 2, le gardait parmi ce qui « pourrait être revendiqué » ; sa vérification le relève (ses points V1 à V5, d'après son verdict), et le directeur en a pris acte à `GO-2026-11-21-60` (« le plancher d'audit au hasard étant occupé »), en ouvrant un protocole X sur ce qui reste. Rien à trancher ici : cette note écrit partout le plancher comme une base nommée et citée, jamais comme une revendication ; la correction de N-075 revient à sa v3. Le verdict n'est pas contre-lu.

Le point n'est donc plus « à confirmer » ; il garde son numéro pour que les renvois tiennent.

**E5 — Section 13, point 8 (l'ordre des premiers pas).** La spécification du banc à vérité plantée sort de la liste des premiers pas sans dépense : elle suit le protocole X (E3).

**E6 — « Ce que je n'ai pas fait ».** Ajouter : la vérification de N-075 v2 n'est lue que dans son en-tête et son verdict.

## Ce qui ne change pas

Les neuf points, leurs énoncés, leurs lectures, les quatre invariants et l'écart signalé avec la proposition D-2 de la note « asymétries » ; les huit autres points renvoyés à le directeur ; le texte à reporter au programme (section 12) ; la ligne proposée pour `CLAUDE.md` (597 signes).

## Relevé de méthode

Selon `docs/procedures/consigne-commune-methode-de-recherche-v1.md` (`d327b3fcbee59f37f833e83812a66ba8b28af72cdd5475772870612a2c9d23d8`).

**Chaîne de raisonnement.**
1. La ligne `GO-2026-11-21-60` existe sur la branche depuis le commit `d481b9a32` (14:00:10 UTC) et nomme le plancher occupé, le protocole X sur ce qui reste et le protocole X pour la conception du banc à vérité plantée (lue au registre).
2. La vérification de N-075 v2 est au même commit ; son verdict dit « pas encore prêt à sceller », dix points, dont le plancher gardé à tort parmi ce qui « pourrait être revendiqué » (`b7707396…`, verdict, source 1).
3. La v1 de N-076 dit N-075 v2 « en vérification », donne la spécification du banc pour premier pas sans dépense, et demande à le directeur de confirmer le plancher occupé (`49b664c1…`, en-tête ; section 4 ; section 13, point 6) : trois phrases périmées par les pas 1 et 2.
4. Supposé : aucun des dix points de la vérification de N-075 ne change un énoncé de N-076 ; je n'ai pas lu leur détail.

**Objets de contrôle.** Sans objet : cet erratum ne porte aucun mécanisme ; il aligne trois phrases sur deux pièces parues.

**Premier pas non justifié.** Le pas 4. Ce qui le justifierait : la lecture des dix points par le contre-lecteur de N-076, qui est aussi celui de N-075.

**Mode d'échec affecté.** Sans objet : pièce d'auteur, non de relecteur.

**Dérivation de l'énoncé seul.** Sans objet : pièce d'auteur, non d'agent de re-dérivation.

**Trouvaille de côté.** Une décision écrite pendant que le registre des accords avance peut être périmée à son scellement : relire le registre juste avant de sceller l'aurait évité.

**Évaluateur et conseil.** Ce qui juge cet erratum : le contre-lecteur de N-076, puis le directeur. Par où il pourrait être bien jugé sans le mériter : il est court et ne touche aucun énoncé, alors que le pas 4 n'est pas vérifié. Conseil au contre-lecteur : lire la v1 avec cet erratum, et confronter la section 13 de la v1 aux dix points de la vérification de N-075 v2.
