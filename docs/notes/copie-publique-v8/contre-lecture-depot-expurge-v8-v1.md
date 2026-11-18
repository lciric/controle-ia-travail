# Contre-lecture de la version 8 du script de copie expurgée (retrait permanent du bras d'attaque et des familles sensibles)

Date : 18 novembre 2026. Contre-lecteur neuf (R2), qui n'a écrit ni la version 7 ni la version 8.
Méthode : lecture du code et des essais, rejeu des essais, examen de la liste réelle des noms suivis (`git ls-files`, noms seulement). Aucun contenu d'un chemin sensible n'a été ouvert. Aucune régénération de la copie publique, aucune poussée, aucun commit de ma main.

## Verdict : à corriger — corrections de code faites dans une version 9

La version 8 laisse passer des noms sensibles écrits avec un tiret bas : **30 chemins suivis du dépôt réel seraient gardés et publiés**. La version 9 (`scripts/depot_expurge_v9.py`, la version 8 intacte) corrige ce point et deux défauts mineurs. Le reste de la version 8 tient : le retrait ne se lève pas avec l'embargo, aucun repli silencieux trouvé, les gardes arrêtent.

Pièces lues (empreintes vérifiées par `controle_ia.scellement verifier`) :
- `scripts/depot_expurge_v7.py` — ed5d73e6f749… ; `tests/test_depot_expurge_v7.py` — e1a686ee685a…
- `scripts/depot_expurge_v8.py` — 3fc4e8d9e7da25e489f7661af031413a8d39455c6b3cd7fd08b4e0bb7a181312
- `tests/test_depot_expurge_v8.py` — 92c59b25b259c93a73a01755a0bb5344fc433eefe39c7bb17900e97658eaf6a7

Pièces produites :
- `scripts/depot_expurge_v9.py` — fd1a5ce6568c1e799978bd2d3c13f506c7d3fd43b557e9a10bd3f9f61751a7dd (scellé)
- `tests/test_depot_expurge_v9.py` — abf57c8e27896538023ff4dd227d7fbe5f46d63068b6a8ba5b9f5bbaab422e6f (scellé)
- Sortie du mode à blanc de la version 9, comptes seulement : `/tmp/claude-0/-home-user-controle-ia-travail/8282ab93-0983-5813-b791-a7a522157dcd/scratchpad/expurge-v9/a-blanc-v9.json` — 4577b811933fb4d86c416b28f917f6ecdc654ba303a98b72bcccf9dac4da63b4 (commit 5ca379be).

## Constats

### 1. Bloquant, corrigé — les noms à tiret bas passent
La version 8 compare les fragments à la lettre, en minuscules seulement. Les scripts et essais Python portent les mêmes noms avec des tirets bas. Sur la liste réelle, la version 8 garde 30 chemins :
- 21 sous `scripts/` : les lanceurs de la course d'idéation des organismes discrets (versions 1 à 7), le lanceur du bras de juge de la même idéation, et les lanceurs de la course du pilier d'attaque (trois versions), avec leurs compagnons `.sha256` ;
- 9 sous `tests/` : les essais de ces lanceurs.

Par fragment : organismes discrets 18, pilier d'attaque 12. Aucune garde de la version 8 ne les voit (le mode à blanc du rédacteur les comptait parmi les fichiers gardés).

Correction (version 9) : chaque segment du chemin est normalisé avant comparaison — accents ôtés, minuscules, toute suite de caractères autres que lettres et chiffres lue comme un tiret — puis comparé aussi sans aucun séparateur. Sont donc vus : tiret bas, espace, point, casse mêlée, accent (composé ou combinant), mots collés. Effet mesuré sur la liste réelle : 371 retraits permanents au lieu de 341, soit exactement ces 30 chemins ; aucun autre chemin ne change de sort, aucun chemin sensible hors des dossiers visés.

### 2. Essai toujours vert, corrigé
L'essai de la version 8 sur la liste réelle (« aucun chemin gardé ne porte un fragment sensible ») juge avec la fonction même qui filtre : il ne pouvait pas voir le constat 1. La version 9 ajoute un essai sur la liste réelle dont la forme de recherche est écrite à part (zéro à trois caractères quelconques entre les mots du fragment, voyelles accentuées), et qui lit la liste avec `-z`.

### 3. Mineur, corrigé — contenu d'un membre d'archive au nom sensible lu avant son nom
Dans une archive gardée, la version 8 lit le contenu de tous les membres (empreinte, garde des secrets, garde des données personnelles) puis regarde les noms. Le script s'arrête bien, mais « contenu jamais lu » n'est pas tenu pour ces membres. Version 9 : les noms des membres (zip, tar, tar compressé, paquet git) sont examinés avant toute lecture ; un nom sensible arrête, le message donne l'archive et un compte, pas le nom. Essai : lectures du zip interceptées, aucune lecture avant l'arrêt ; cas sain joint.

### 4. Mineur, corrigé — mode à blanc : archive non examinée
Une archive gardée que le mode à blanc ne sait pas ouvrir était comptée mais laissait le verdict « passeraient ». Version 9 : elle arrête. Aucune dans le dépôt réel aujourd'hui (78 archives examinées, 0 non examinée).

### 5. Vérifié, sans défaut
- Le retrait permanent passe avant l'embargo et avant la liste ordinaire ; embargo vidé, il reste (essai rejoué).
- Casse, compagnons `.sha256`, chemins dans `livrables/`, à la racine, sous `gemini/` : retirés ou arrêt, selon le dossier. Un premier dossier écrit avec une majuscule arrête (côté sûr).
- Liens symboliques : jamais copiés ; un lien au nom sensible hors des dossiers visés arrête.
- Membres d'archive imbriqués, à toute profondeur : arrêt.
- Copie renommée d'un fichier sensible (même identifiant d'objet git) : arrêt.
- La liste des chemins signalés de la version 7 n'exempte pas un nom sensible.
- L'ajout de `registres` et `rapports` aux dossiers visés va dans le sens sûr ; je le tiens pour juste (sans lui, 9 chemins de `rapports/` seraient publiés). À confirmer par la mère.

## Essais rejoués
- Version 7 : 29 passés, 1 échoué. Version 8 : 60 passés, 1 échoué (chiffres du rédacteur confirmés).
- Version 9 : 87 passés, 1 échoué. Ce sont les essais de la version 8 (trois adaptés : un membre d'archive au nom sensible arrête avant lecture au lieu d'être rendu dans la liste des survivants), plus 14 variantes artefacts, 10 voisins sains, et 4 essais neufs (liste réelle indépendante, membre d'archive jamais lu, tar et paquet git, archive non examinée en mode à blanc).
- L'échec commun aux trois versions est celui que le rédacteur a signalé : 36 chemins suivis de `runs/course-ideation-regard-ou-raisons-v1/` portent le nom de l'autre projet hors du dossier que la version 7 vise. Il précède la version 8 ; non corrigé ici (hors consigne).

## Mode à blanc de la version 9 (commit 5ca379be, comptes seulement)
- Chemins de l'arbre : 27951. Fichiers gardés : 23848.
- Retraits permanents : 371 — docs 182, runs 108, registres 36, scripts 21, rapports 9, tests 9, prereg 4, brouillons 2.
- Par fragment : organismes discrets 189, bras d'attaque 74, pilier d'attaque 56, évasion des moniteurs 32, attaque publiée 18, quatre familles d'évasion 2 ; bras informé, vérification externe du bras et mode tenu à l'écart : 0 chemin suivi.
- Chemins sensibles hors des dossiers visés : 0. Membres d'archive au nom sensible : 0.
- Verdict : arrêt, pour les deux causes déjà connues (les 36 chemins de l'autre projet ; 2 fichiers gardés de même identifiant d'objet git qu'un fichier retiré par nom).

## Ce qui reste, et qui n'est pas du code mineur

1. **Le contenu des fichiers gardés cite les noms sensibles.** Mesure faite sur les seuls fichiers gardés : 672 fichiers gardés contiennent au moins un des neuf fragments (tiret, tiret bas ou espace) — docs 485, brouillons 98, livrables 30, prereg 30, scripts 17, tests 6, src 3, runs 2, `.claude` 1. Par fragment : bras d'attaque 615, mode tenu à l'écart 482, bras informé 76, pilier d'attaque 69, évasion des moniteurs 45, quatre familles d'évasion 20, attaque publiée 17, organismes discrets 4, vérification externe du bras 3. Le filtre par nom ne dit rien de ce que ces fichiers décrivent. Si « exclus de toute copie publique » vise aussi la description de ces familles, il faut une décision de Lazar et une garde de contenu ; ce n'est pas une retouche.
2. **Noms voisins, gardés, hors de la liste de la consigne** (noms seulement, à trancher par la mère ou Lazar ; je n'ai rien ajouté à la liste) :
   - `docs/procedures/brief-session-attaquant-informe-v1.md` et son compagnon (2) ;
   - `brouillons/ii-b-saboteur-budget-v1/` et la consigne de sa conception ; `docs/decisions/proposition-P-066-saboteur-diffus-par-construction-v1.md` ;
   - `docs/notes/affinage-equipe-rouge-v1/` et `-v2/` (34 chemins) ;
   - le singulier « organisme-discret » et les autres formes fléchies ne sont pas visés (aucun chemin réel aujourd'hui).
3. Les deux décisions déjà nommées par le rédacteur : les 36 chemins de `runs/course-ideation-regard-ou-raisons-v1/` ; le compagnon `.sha256` gardé identique à un fichier sensible.
4. Limites héritées de la version 7, inchangées : une archive tar d'ancien format (sans la marque « ustar ») ou un conteneur non reconnu (base SQLite, pickle, parquet) n'est pas ouvert et passe sans examen ; quand le script s'arrête, l'arbre des fichiers gardés déjà écrits reste dans le dossier de sortie (aucun paquet, aucun bilan, mais des fichiers) ; le mode à blanc repère les archives par extension et au premier niveau seulement, et ne joue pas les gardes de contenu.
5. Les trois noms sans chemin suivi (vérification externe du bras, mode tenu à l'écart, bras informé) restent filtrés par avance, sans épreuve sur le réel.
6. Le message d'arrêt « hors des dossiers visés » imprime les noms sensibles sur la sortie d'erreur locale : acceptable sur le poste de travail, à ne pas recopier dans un registre public.

## Note de dépôt
Pendant cette contre-lecture, un commit de la mère (« Pièces des agents en cours », 5ca379be) a pris `scripts/depot_expurge_v9.py` dans son état final (identique au fichier scellé). Le compagnon `.sha256`, les essais de la version 9 et ce rapport ne sont pas commités.
