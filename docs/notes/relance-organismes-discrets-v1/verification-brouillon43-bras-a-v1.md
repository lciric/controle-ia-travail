# Vérification du brouillon 43 du texte neuf du bras A des organismes discrets — v1

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`), agent neuf. Je juge ; je ne corrige rien. Ni scellé ni committé. Écrit le 2026-11-21, vers 11:20Z (`date -u`).
- **Texte** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon43.md`, `4f91b535ad91581510615c97039a4cae0a96f4d788088b2aff666d4c3d3f97b3`, 2 493 lignes.
- **Pièces, compagnons vérifiés** (`python -m controle_ia.scellement verifier`, tous « OK ») :
  - la note du rédacteur, `preenregistrement-v2-brouillon43-note-v1.md`, `47659b23794d…` (111 lignes) ;
  - le brouillon 42, `c5dbd28eca7b…` (2 479 lignes) ; la vérification du brouillon 42, `dcf742d5d102…` (179 lignes).
- **Registre** : `git show origin/main:registres/go.md`, tête locale `e77fa0d9`, sans appel réseau ; 636 lignes ; empreinte de cette lecture `65ba1a9730ea…`, la même que celle de la vérification du 42.
- **Journal** : pas de compagnon ; empreinte calculée `a1124f8be8c0…` ; 275 lignes ; lignes 273 à 275 (OD-255 à OD-257).
- **Dépôt** : branche `claude/pensive-bardeen-1fv7hw`, tête `799796ae`.
- **Méthode** : différence des brouillons 42 et 43 par programme, section par section sous les 54 titres, puis mot par mot sur chaque ligne changée ; lecture des passages neufs ; consignes figées, marques, validateur et table d'en-tête restreinte, par programme ; chaque phrase neuve confrontée à la vérification du 42 et aux lignes 631 et 632 du registre.

## Verdict : **engageable** — aucune correction ; deux mineurs

- Les deux corrections et les quatre mineurs de la vérification du 42 sont traités fidèlement, ni plus ni moins.
- **Aucune règle de jugement, aucun seuil, aucune issue des sections gelées, aucune prédiction ne change.** Refait par programme : 0 ligne dans toutes les sections de jugement, section 12 comprise.
- GO-2026-11-21-32 et GO-2026-11-21-33 sont citées à la lettre.
- **Mais le texte n'est pas prêt pour la contre-lecture 10 au sens qu'il lui donne** : elle porte sur le texte aux cases remplies, et cinq cases à remplir avant elle portent encore la marque (partie 4).

**Mineurs** (à faire dans le prochain brouillon ; aucun ne bloque) :
- **m-1. Préambule de 13, point 4, sous-point des deux essais.** La liste de ce que porte le devis ne nomme pas le signe de « ne sert pas ce modèle ». 3.4 le porte deux fois (lignes 516 et 517). Ajouter « et le signe qui dit « ne sert pas ce modèle » (3.4) » à cette liste. C'est la réserve 1 du rédacteur (partie 3).
- **m-2. Statut, ligne 3** : « Hors d'elles : l'en-tête, 3.4, une case de 13.1, une case de 13.2 et 14.55 ». Il manque la section « Contre-lecture » (lignes 2490 et 2491, changées). La note, partie 2, la nomme.

## 1. Fidélité au traitement de la vérification du 42

| point | où, au brouillon 43 | jugement |
|---|---|---|
| **C-1** les deux mots ont leur ligne | en-tête, ligne 8 (ligne des commits) ; 13.1, case « lecteurs et juge des ancres », ligne 1441 ; statut ; 14.55 | **levée**. Les deux identifiants sont inscrits, lus à `e77fa0d9`, lignes 631 et 632. La phrase du 42 reste, datée à `761710a7`, suivie de sa correction : c'est de l'histoire, recevable. Plus aucune phrase ne dit ces mots sans ligne ni « à inscrire » (recherche par programme). La note, partie 6, du 42 n'est pas réécrite : juste (R12). |
| **C-2 (i)** code 200 et autre nom servi sur le point d'accès européen | 3.4, ligne 516 (conditions d'envoi) et ligne 517 (vérification de la clé) | **levée**. Nœud de Lazar, « le repli n'est pas étendu ». C'est la lecture étroite que demandait la vérification. Elle rend le choix à Lazar ; elle ne tranche rien à sa place. |
| **C-2 (ii)** signe de « ne sert pas ce modèle » | mêmes lignes | **levée**. Le signe (code de retour, et au besoin type ou message d'erreur) est fixé au devis, avant tout appel ; lui seul déclenche le repli ; la session ne le choisit pas après une réponse. Le cas est fermé : une réponse « modèle inconnu » qui n'est pas ce signe tombe dans la règle générale (nœud) ; une panne ou un refus de clé reste « cause corrigée, vérification refaite ». |
| **m-1** garde du juge éprouvée (R5) | 3.4, ligne 513 ; 13.2, case « version des modèles », ligne 1461 | **fidèle**. Portée par le programme qui conduit les ancres à la course ; cas sain et artefact nommés ; éprouvée avant le premier appel du juge à la course. 8.4 n'est pas touchée (vérifié). |
| **m-2** « Labs » | 3.4, ligne 516 | **fidèle** au relevé (ligne 12 : « retours, modèles « Labs » ou « Preview » », lu par une recherche de chaîne). |
| **m-3** « que je n'ai pas rouverte » | 3.4, ligne 513 | **fidèle** : « que le rédacteur n'a pas rouverte ». Seule cette phrase change, comme demandé. Voir l'observation O-1 sur les autres. |
| **m-4** la question devient une information | 3.4, ligne 513 ; note, partie 3 | **fidèle**. « Aucune décision n'est demandée d'avance à Lazar » ; la limite est dite ; le nœud du mot « b a b go » la traitera. |

**Rien de plus.** Les seuls ajouts hors des six points sont l'histoire (statut, auteur, date, commits, note, table, 14.55, contre-lecture) et une phrase de tête en 3.4 (ligne 497) qui résume les changements et dit qu'aucune règle d'admission ne change (vrai : règles 1 à 8 identiques).

**GO-2026-11-21-32 et -33, citées correctement ?** Oui.
- Ligne 631 : type « décision » ; périmètre qui commence, gras ôté, par « Bras A des organismes discrets, cinq choix sur le second lecteur (mot donné le 20 novembre, inscrit ce jour) » ; cinq choix ; finit par « Aucune dépense ouverte. » ; renvoi à `93cbc6f4…` par son chemin. Tout est à la lettre.
- Ligne 632 : type « décision » ; périmètre qui commence par « Bras A des organismes discrets, juge des deux ancres et envoi des textes » ; trois choix ; finit par « Aucune dépense ouverte ; réglages des consoles par Lazar. » ; renvoi à `00af2aa8…`. À la lettre.
- « Aucune des deux n'ouvre de dépense » (13.1) : fidèle.
- Une seule ligne nomme GO-2026-11-19-97, la sienne (ligne 530) : concorde.
- Le commit cité pour le brouillon 43, `7dc8706d7`, existe sur la branche (« Vérification du brouillon 42 … ; journal OD-256 »).

## 2. Règles — refait par programme

| contrôle | mon résultat | concorde avec la note ? |
|---|---|---|
| titres | 54 et 54 ; seul le titre de niveau 1 change (42 → 43) | oui |
| hypothèse, prédiction, métrique, seuil | 0 ligne changée | oui |
| 6.1 à 6.12 | 0 (6.3 comprise) | oui |
| 7.1 à 7.8 (liste d'arrêt, ligne A12) | 0 | oui |
| 8.1 à 8.7 (8.2, 8.4, 8.5 comprises) | 0 | oui |
| 9, 10, 11 | 0 | oui |
| section 12 | 0 (171 lignes et 171) | oui |
| préambule de 13 ; règles 1 à 8 de 3.4 | 0 | oui |
| sections qui changent | en-tête : lignes 1, 3, 5, 6, 8, 9 et 3 lignes neuves à la table (195 à 197) ; 3.4 : 4 lignes (42 : 494, 510, 513, 514) ; 13.1 : 1 case (1438) ; 13.2 : 1 case (1458) ; 14 : 11 lignes neuves (14.55) ; « Contre-lecture » : 2 lignes (2476, 2477) | oui |
| consignes figées | 3.2, lignes 398 à 423 au 43 (395 à 420 au 42) : `98a9bd34d280fc7d…` ; 3.3, lignes 445 à 479 (442 à 476) : `ecf590eae0c06d41…` ; égales au 42 | oui |
| marques des cases (« À REMPLIR », la marque que nomme le validateur) | 7 lignes, 8 occurrences, toutes en 13.1 (1438, 1440, 1441, 1444, 1449, 1450, 1451 ×2) : mêmes cases qu'au 42, décalées de 3 | oui |
| validateur `problemes(chemin)` | 42 et 43 : les deux mêmes problèmes (marque hors des sections exigées ; contre-lecture 10 sans ses deux empreintes) | oui |
| table d'en-tête | 249 lignes à empreinte entière (246 au 42, plus 3) ; aucune ligne existante ne change. **Recalculées sous ma consigne restreinte : 185 lignes**, préfixes de la relance, `prereg/T0.7-organismes-discrets-v-a-v2-*` et dossier sans interne, les 3 neuves comprises : **184 égales**, 1 absente du disque (ligne 179), vérifiée par `git show origin/main:` : `f7090b5d…`, égale. Aucune de ces 185 ne porte un motif cloisonné. **64 non recalculées** | sur le fond, oui ; voir O-2 pour le compte |

**Une règle de jugement, un seuil, une issue des sections gelées ou une prédiction change-t-il ? Non.**

## 3. Réserves du rédacteur

**Réserve 1 — le préambule de 13 ne nomme pas le signe.**
- **Défaut léger, oui.** Ce n'est pas une contradiction : 3.4 fait la règle, et seul ce signe déclenche le repli. Si le devis l'oubliait, aucun repli ne serait possible ; tout « modèle inconnu » sur le point d'accès européen serait un nœud. Le défaut va donc dans le sens de la prudence.
- Mais la liste du préambule se lit comme l'inventaire du devis. Un rédacteur de devis qui la suit pourrait omettre le signe. Un devis est en cours de rédaction en parallèle (journal, OD-256).
- **À corriger avant la contre-lecture 10 : oui, de préférence**, une demi-ligne (m-1). Cela ne bloque rien d'autre. La contre-lecture 10 étant de toute façon plus loin (partie 4), cela tient dans le prochain brouillon.

**Réserve 3 — cas sain et artefact nommés.**
- **Pas un défaut.** R5 exige les deux ; les nommer fixe ce que le programme doit montrer. C'est l'usage de 8.4 (« chacune éprouvée sur un cas sain et sur un artefact »). La description de l'artefact (« aucun jugement d'ancre n'est lu ») se vérifie par programme.
- Une précision possible, non exigée : « la file va à son terme », au cas sain, s'entend d'un essai du programme sur des réponses simulées, puisque l'épreuve a lieu avant le premier appel du juge. Le texte le dit implicitement (« ses essais sont ceux du programme des ancres »).
- **Ne pas retirer ; rien à corriger.**

**Réserve 4 — le programme des ancres n'existe pas encore.**
- **Pas un défaut du texte.** Le texte dit ce que le programme doit porter, et place la garde à une case de 13.2 : après le scellement, avant toute dépense. L'épreuve doit avoir lieu avant le premier appel du juge à la course : c'est la bonne borne.
- Une question reste, hors du texte : ce programme est-il du code arrêté en version 13 (case « commit du code ») ou un programme de la course écrit après le scellement, comme le programme d'enchaînement de la lecture (13.2, ligne 1466) ? La note dit « code arrêté en version 13 : rien à changer ». Si le programme des ancres est du code arrêté, la garde demanderait un changement de code. Je n'ai ouvert aucun module ; la session qui orchestre le dira.
- **Rien à corriger avant la contre-lecture 10** ; la question peut lui être posée.

**Autres réserves de la note**, en bref :
- réserve 2 (seul ce signe déclenche le repli ; le reste retombe sur la règle générale) : juste, et le cas est fermé (partie 1) ;
- réserves 5, 6, 7 et 8 : dites, recevables ; la 6 (tête `761710a7` citée pour GO-2026-11-20-58) est de l'histoire datée ;
- réserve 9 (texte non relu en entier) : c'est le rôle de la contre-lecture 10.

**Observations, sans correction demandée :**
- **O-1. La première personne reste ailleurs.** m-3 visait une seule phrase neuve ; elle est corrigée. Mais environ vingt « non ouvert par moi », « je n'ai ouvert », « lue par moi » demeurent, dont dans des sections de jugement (6.10, lignes 902 à 910 ; 6.12, lignes 941 à 953 ; 12, ligne 1383 ; la ligne 1254 est une citation de Lazar) et en 13.1 et 13.2. Elles sont antérieures au 43. Les reprendre dans les sections de jugement les ferait changer ; c'est à la contre-lecture 10 de dire s'il le faut. Je ne le demande pas ici.
- **O-2. Les comptes de la note.** La note dit 183 lignes recalculées et une absente ; je trouve 184 égales et une absente sur les mêmes préfixes. L'écart est d'une ligne et sans effet : tout est égal. De même, le détail des 49 fichiers du débord fait 50 à l'addition ; le journal (OD-257) déclare l'erreur de compte, « 5 et non 6 ». Je ne l'ai pas vérifiée, faute d'avoir le droit de prendre ces empreintes.
- **O-3.** La case « lecteurs et juge des ancres » (ligne 1441) redit le mot « s'il sert `mistral-large-4-0`, sinon global » sans la borne de C-2. Elle renvoie à 3.4 dans la même case. Suffisant.

## 4. Prêt pour la contre-lecture 10 par un agent Opus 5.5 neuf ?

**Non.** Le traitement de la vérification du 42 est achevé, et rien dans le texte ne demande de correction avant d'avancer. Mais le texte définit lui-même la contre-lecture 10 comme portant **sur le texte aux cases remplies** :
- préambule de 13, point 6 (ligne 1430) : « Cases de 13.1 remplies ; vérification du texte aux cases remplies … inscrite comme contre-lecture 10 » ;
- « Contre-lecture », ligne 2490 : « Contre-lecture 10 (du texte aux cases remplies …) » ; ligne 2491, à propos de la contre-lecture 11 : « Elle ne tient pas lieu de la contre-lecture 10, qui porte sur le texte aux cases remplies » ;
- 14, ligne 1847 : « contre-lecture 10 à faire sur le texte aux cases remplies ».

Une lecture engagée maintenant serait une lecture aux cases non remplies. Elle ne pourrait pas être inscrite comme contre-lecture 10. Si la session en veut une maintenant, elle doit la nommer autrement, et la contre-lecture 10 resterait à faire.

**Ce qui manque avant la contre-lecture 10** (cases à remplir d'abord, selon l'ordre du texte) :
1. **« nœuds »** : l'identifiant de la ligne du mot du 19 novembre (« go reocs », « repere permis »), qui ne nomme pas GO-2026-11-19-97.
2. **« familles »** : son reste, la confrontation de `mistral-large-4-0` et `gemini-4-neon` à la liste, par le lecteur habilité.
3. **« lecteurs et juge des ancres »** : réglages des deux consoles par Lazar et leur constat daté, scellé ; devis des deux essais (avec le signe de « ne sert pas ce modèle »), sa contre-lecture par un agent d'un autre modèle, ses lignes de calcul et leur GO ; fichier des règles scellé ; programme qui conduit les essais, contre-lu ; vérifications de clé et point d'accès retenu ; les deux files ; les deux rapports ; pour chaque rôle, nom servi, réglage, sortie maximale et comptes, ou le mot de Lazar qui pourvoit un rôle non tenu.
4. **« commit du code »** : le commit, par la session qui orchestre.
5. **« module des cinq moniteurs »** : la livraison de la version 11 et ce que la case exige ; sa contre-lecture côté habilité.

Deux cases restent marquées pendant la contre-lecture 10, par construction : **« renvoi de la base »** (vient après elle, sur la version qu'elle rend) et **« entropie »** (tirée au scellement).

## 5. Ce qui sépare encore du scellement

- Le prochain brouillon : les deux mineurs (m-1 au moins).
- Les cinq cases de la partie 4, puis la contre-lecture 10 par un agent d'un autre modèle que le rédacteur, sur le texte aux cases remplies, avec le traitement de ses remarques.
- La vérification indépendante du code et du texte ensemble (8.7 ; mot « a a »), son rapport scellé avant le scellement du texte.
- Le renvoi de la base par le lecteur habilité, sur la version que rend la contre-lecture 10 (lignes corrigées seulement), et sa case.
- Côté habilité : la contre-lecture de la version 11 ; la configuration de l'analyse qui la cite ; la version qui fait foi du lanceur de l'étape de discrétion, son nom et son empreinte.
- Registre : la ligne du mot du 19 novembre si elle manque ; les lignes de calcul des essais.
- L'entier racine, tiré au scellement, et le scellement (R1) ; le validateur doit alors ne rendre aucun problème.
- Après le scellement, avant la dépense : la case « version des modèles » de 13.2, dont le programme des ancres qui porte la garde du juge, éprouvée (réserve 4).

## Fichiers ouverts

- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon43.md` : par programme (différence, sections, consignes figées, marques, table d'en-tête, validateur, recherches de chaînes) ; affichés : les lignes changées (différence mot à mot), lignes 516 et 517 en entier, extraits des lignes 513, 1441, 1461 ; lignes 1419 à 1433 (section 13 et son préambule) ; 2468 à 2478 (14.55) ; extraits de 2490 et 2491 ; extraits autour de chaque marque (1438 à 1451) ; extraits autour des mentions de la contre-lecture 10 et de la première personne.
- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon42.md` : par différence et par programme.
- En entier : la note du brouillon 43 ; la vérification du brouillon 42.
- `docs/notes/relance-organismes-discrets-v1/journal-relance-organismes-discrets-v1.md` : lignes 273 à 275 ; recherche des numéros OD-254 à OD-259 ; empreinte.
- Par `git show origin/main:` (tête `e77fa0d9`) : `registres/go.md`, copié au bloc-notes ; lignes 631 et 632 affichées ; nombre de lignes, empreinte, décompte de « GO-2026-11-19-97 » (numéro de ligne seul). `docs/notes/relance-organismes-discrets-v1/lecteur-remplacant-carbon-v1/choix-mistral-deepseek-v1.md`, pour son empreinte seulement.
- `docs/notes/relance-organismes-discrets-v1/conditions-envoi-textes-google-mistral-releve-v1.md` : une recherche de la chaîne « Labs » (ligne 12, extrait).
- Fichiers de la table d'en-tête : 184 lus en octets pour l'empreinte seulement, tous sous `docs/notes/relance-organismes-discrets-v1/`, `prereg/T0.7-organismes-discrets-v-a-v2-*` ou `docs/notes/bras-a-sans-interne-v1/`.
- `controle_ia.prereg` : exécuté (`problemes`), non lu ; noms publics et signature affichés par introspection. `controle_ia.scellement` : exécuté.
- `git log`, `git status --short`, `git cat-file` sur `7dc8706d7`.

## Écarts

- **Aucun franchissement du cloisonnement.** Aucune empreinte prise hors des trois préfixes de ma consigne : ni ligne cloisonnée, ni `docs/sources/`, ni configuration de T0.6, ni la ligne 189 de la table. Aucun module de code ouvert. Aucun envoi ni aucune réponse d'essai ouverts.
- **Débord mineur, déclaré** : la recherche de « Labs » dans le relevé des conditions d'envoi, fichier non listé dans ma tâche mais nommé par le texte et situé dans le dossier de la relance.
- **Vu sans ouvrir** : `git status` affichait un fichier non suivi, `docs/notes/relance-organismes-discrets-v1/devis-essais-admission-mistral-neon-bras-a-v1-brouillon1.md` et son compagnon ; pendant ma vérification, la session a committé ce devis (`4b2cb1d7`, journal OD-258, entrée non lue). Je ne l'ai ni ouvert ni empreinté ; je n'en tire rien d'autre que son existence. Ma vérification porte sur la tête `799796ae`.
- Aucun appel de modèle ni appel réseau, aucun sous-agent, aucune dépense. `registres/`, `.claude/` et le journal non touchés. Fichiers écrits : celui-ci, et des fichiers de travail dans le bloc-notes de la session (scripts de comparaison, copie du registre lu).
