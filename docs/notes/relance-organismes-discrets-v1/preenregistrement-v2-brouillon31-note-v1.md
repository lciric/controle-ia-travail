# Note de changements — brouillon 31 du texte neuf du bras A des organismes discrets — v1

**Rédigé par Claude Fable 5.2 (`claude-fable-5-2`)**, le même agent que pour les brouillons 21 à 30. Elle suit la note du brouillon 30 (`preenregistrement-v2-brouillon30-note-v1.md`, `9730ffe9…`), qui reste valable pour ce qu'elle couvre.

- **Brouillon** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon31.md`, `6fd71ee2c7756d07418155e7775ceba67ece71b438fb415838964652983a9768` (2 137 lignes). Les brouillons 20 à 30 ne sont pas modifiés.
- **Demandes à la session principale, version 6** :
  - `docs/notes/relance-organismes-discrets-v1/demandes-au-developpeur-habilite-bras-a-v6.md`, `4937274b3d360e1dc3f95a6d0888eec5fd68d598e0f9a1b9a3e86fd9ad2d9a81`, écrite avant le brouillon, qui la cite par son empreinte ;
  - `docs/notes/relance-organismes-discrets-v1/demandes-au-lecteur-habilite-et-a-lazar-bras-a-v6.md`, écrite après le brouillon, qu'elle cite par son empreinte entière ; la sienne est dans son compagnon, et le brouillon la cite par son seul chemin, pour ne pas faire de boucle.
  Les versions 5 ne sont pas modifiées.
- **Fiches pour Lazar : aucun fichier neuf.** Aucun point porté ne touche une règle de jugement. Celles du brouillon 23 restent en vigueur (`f20abfed…`).
- **Sources**, lues en entier : la vérification du brouillon 30 (`a94602cd70b8f99c454919663eca8b5f23642ed8231535c00e108440fda2dbe8`, « engageable après corrections » : un défaut, un mineur) ; la vérification de cloisonnement des demandes en version 5 (`e40f04f8bfd01e6dbec4f09b0afb39584a4005dfb1544e7e0af33861f3cd76bc`, une retouche, deux facultatives).
- **Méthode** : copie du brouillon 30 par `cp`, puis 24 remplacements exacts, chacun vérifié unique par programme.
- **Registre des accords** : relu sur la branche principale distante au commit `f637e163` ; aucune ligne de plus.
- **Heures (UTC, `date -u`)** : début 19:10:22Z le 2026-11-19 ; brouillon scellé à 19:12:30Z.
- **Un incident, à déclarer.** À la première tentative, mon programme de construction s'est arrêté sur une ancre qui n'était pas unique, sans rien écrire ; la suite de ma commande a pourtant scellé la copie du brouillon 30 que je venais de faire sous le nom du brouillon 31. J'ai retiré ce compagnon faux, vérifié que la copie était encore, octet pour octet, le brouillon 30, corrigé l'ancre, rejoué, puis scellé. Le compagnon présent est le bon ; aucun fichier antérieur à ce tour n'a été touché.
- **Interdits tenus** : aucune empreinte de fichier d'un dossier du côté habilité ; aucun interne de moniteur ; aucun module du code ouvert ; aucune clé ; aucun appel de modèle ; seul appel réseau, `git fetch` de la branche principale ; ni `registres/`, ni `.claude/`, ni le journal touchés ; rien committé ; aucun sous-agent.

## Contrôles par programme

| contrôle | résultat |
|---|---|
| section 12 ; « Critères de lecture gelés » en entier ; section 10 | identiques, caractère pour caractère, au brouillon 30 |
| titres ; consignes figées | inchangés ; `98a9bd34…` et `ecf590ea…` recalculées |
| citations à la lettre | brouillon 20 : 935 sur 935 ; brouillon 30 : 1 200 sur 1 200 |
| table d'en-tête, sans les fichiers cloisonnés | 168 lignes à empreinte : 154 recalculées et égales, 0 différente, 14 sautées et non ouvertes |
| marque des cases non remplies | huit lignes, toutes en 13.1 |
| validateur (`problemes()`) | les deux problèmes attendus |
| pièce du développeur, version 6 | aucune chaîne hexadécimale de huit signes ou plus ; quatre lignes diffèrent de la version 5 |

## 1. Ce qui est porté

| source | objet | ce que le texte dit maintenant | où |
|---|---|---|---|
| vérification du brouillon 30, C-1 | révocation entrée pendant une panne | seule l'étape (n), après le fichier scellé de l'étape (m), relève de la lecture déjà partie. Avant le rejeu d'une lecture interrompue sans résultat, le programme du constat est rejoué **à titre de contrôle** : il n'écrit aucun fichier, rend le constat sur sa sortie, sort en succès ou en échec ; contrôle malsain, le rejeu ne part pas | conventions ; 6.9 ; 8.4 |
| vérification du brouillon 30, M-1 | constats malsains nés de la tenue du registre | **consigne de tenue** : entre la ligne de GO d'une reprise et la fin de la lecture, aucune ligne ne la nomme, sauf pour la révoquer ; la ligne d'inscription ne nomme que l'empreinte de la configuration | conventions ; 13.2 |
| cloisonnement, retouche 1 | somme et maximum de l'agrégateur | **un seul nombre par dose** ; une table, une liste ou un texte à la place du nombre est « non rapportée », et rien de son contenu n'est rapporté | 6.9 ; 8.4 |
| cloisonnement, retouche 3 | arrêt du constat | rapporté avec la ligne qui l'a causé ; la ligne de GO neuve la cite et dit si la livraison était déjà produite | conventions ; 13.2 |

**Les deux phrases mises d'accord.** Le brouillon 26 disait qu'une lecture interrompue avant tout résultat « n'est pas une lecture ». Le brouillon 30 traitait une révocation entrée pendant cette panne comme entrée « après la lecture ». Le brouillon 31 garde la première et corrige la seconde : pendant une telle panne, une révocation est entrée avant la lecture, et l'empêche de partir.

## 2. Ce que le code de la version 9 doit porter

Les douze points de la note du brouillon 30 tiennent, à deux près, récrits ici, et un s'ajoute.

- **Point 9, récrit.** L'étape (n) exige le constat déjà présent, sans en demander un neuf, et vérifie que son empreinte est celle que portent les constats de l'étape (m). **Le rejeu d'une lecture interrompue sans résultat ne relève plus de ce régime** : voir le point 13.
- **Point 12, inchangé** pour les dossiers.
- **Point 13, neuf — mode de contrôle du programme du constat.** Une option du programme (`scripts/constat_de_lancement_discretion_bras_a_v1.py`) le fait jouer « à titre de contrôle » :
  - il fait le même constat, sur les mêmes entrées ;
  - il n'écrit aucun fichier, et ne touche pas au constat d'origine ;
  - il écrit sur sa sortie standard le constat à huit champs, en une ligne JSON ;
  - il sort en succès si le constat est sain, en échec sinon.
  L'enchaînement du rejeu joue ce contrôle d'abord, dans la même exécution, et ne lance le rejeu que sur une sortie en succès. Essais : contrôle sain, aucun fichier écrit, constat d'origine intact, le rejeu part ; contrôle qui voit une ligne neuve nommant la ligne de GO employée, sortie en échec, le rejeu ne part pas.
- **Point 14, neuf — arrêt du constat.** La sortie d'un constat malsain, ou d'un contrôle malsain, nomme la ligne qui l'a causé, par son identifiant.
- **Point 15, neuf — somme et maximum de l'agrégateur.** Pour chaque dose, rapporter le nombre s'il est de 0 à 1. Si la valeur d'une dose est une table, une liste ou un texte : « non rapportée », et **aucune valeur tirée de son contenu**. Le code de la version 8 gardait la structure et rapportait valeur par valeur, à toute profondeur : ce n'est plus permis. Essai : une table par dose qui porte trois nombres de 0 à 1, « non rapportée », et aucun de ces nombres dans le résultat.

## 3. Les demandes, version 6

**Pièce du développeur : ce qui change depuis la version 5, exactement.** Quatre lignes.
1. Le titre : « v6 ».
2. Demande 31, la question. Avant : « […] : un nombre par dose, ou une table par dose qui porte aussi d'autres champs ? Toutes leurs valeurs sont-elles des nombres de 0 à 1 ? » Maintenant : « […] : un seul nombre par dose, ou une table par dose ? Ce nombre est-il toujours de 0 à 1 ? Si c'est une table, porte-t-elle autre chose qu'une aire, une valeur p ou un compte ? »
3. Demande 31, la réponse attendue. Avant : « […] Pour une table, le nombre de ses champs, sans leurs noms. » Maintenant : « […] Pour une table : oui ou non à la dernière question, sans les noms de ses champs ; et fais rendre, dans la version de la demande 1, un seul nombre par dose dans chacun des deux champs. »
4. Demande 31, à quoi elle sert. Avant : « […] L'analyse les rapporte valeur par valeur, et dit « non rapportée » toute valeur qui n'est pas un nombre de 0 à 1. » Maintenant : « […] L'analyse ne rapporte que ce nombre ; elle ne rapporte rien d'une table. »

Tout le reste est, au mot près, la version 5.

**Pièce du lecteur habilité et de la session principale : ce qui change depuis la version 5.**
- Le titre ; le nom de la pièce du développeur citée (version 6) ; la ligne « Elle remplace », qui cite la version 5.
- **Ligne 6** : le texte visé est le brouillon 31, avec son empreinte écrite en entier.
- **Demande 29** : au (c), « tout arrêt du constat est rapporté avec la ligne qui l'a causé ; la ligne de GO neuve cite cette ligne et dit si la livraison était déjà produite » ; un (e) neuf, la consigne de tenue du registre, à laquelle il répond par oui ou non ; la ligne de la table des numéros.

## 4. Réserves

1. **Le contrôle avant un rejeu est une procédure de la session qui lance.** Le programme d'analyse ne peut pas savoir qu'il a eu lieu ; c'est l'enchaînement du rejeu qui le tient, et le manifeste qui le montre.
2. **La consigne de tenue du registre n'est pas une garde** : si elle n'est pas tenue, le constat est malsain et il faut une ligne de GO neuve. Le vérificateur de cloisonnement a compté que 220 lignes sur 511 du registre citent au moins deux identifiants : la consigne a un coût réel pour qui tient le registre, et la demande 29 le lui demande.
3. **Le brouillon ne porte pas l'empreinte de la pièce du lecteur en version 6**, pour ne pas faire de boucle ; elle est dans son compagnon.
4. **Les deux pièces des demandes en version 6 n'ont pas été relues.** Les changements de la pièce du développeur tiennent en quatre lignes, données ci-dessus.
5. **Je n'ai toujours pas relu le texte en entier.**

## 5. Fichiers ouverts pour ce brouillon

- `docs/notes/relance-organismes-discrets-v1/verification-brouillon30-bras-a-v1.md`, en entier.
- `docs/notes/relance-organismes-discrets-v1/verification-cloisonnement-demandes-v5-bras-a-v1.md`, en entier.
- Les deux pièces des demandes en version 5 : la ligne 6 de l'une, la demande 31 de l'autre, et par programme.
- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon30.md` : par programme, pour les contrôles et les ancres.
- `registres/go.md` de la branche principale distante, par `git show`, après la ligne 511.
- Par programme, pour leur seule empreinte : les 154 fichiers de la table d'en-tête hors des dossiers cloisonnés.
- Rien d'autre.
