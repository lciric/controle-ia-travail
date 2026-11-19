# Vérification habilitée du brouillon 4 du préenregistrement neuf du bras A des organismes discrets — lignes qui touchent la base « mots et coût » et le verdict de discrétion — v1

**Conclusion : B7 non levé.** Il reste trois corrections d'écriture :
- une référence à la ligne C2, alors que cette ligne est retirée (6.12, point 5) ;
- une contradiction sur les tirages dégénérés des moniteurs appris : arrêt en A17 et en 8.2, « indécis » en 6.9 et en 6.10 ;
- l'écart à la décision N-053 et la ligne GO-2026-11-19-15 ne sont ni écrits ni cités.

Le reste est conforme : le renvoi à la base, la base qui ne compte que dans un sens, la famille de quinze tests et le juge d'une autre lignée dans le verdict.

## En-tête

- **Qui** : le même contre-lecteur habilité que pour les rapports `27189edd…` (brouillon 2) et `2f7b43ec4ac995799b84da2fde5c893d127f6ff59e2c7c6f76d85fa2a03b08a9` (brouillon 3), sous-agent délégué par la session mère (`session_013QMayjsoZJFBUCqcnvD5h1`). Je n'ai écrit ni le brouillon 4, ni sa note, ni aucune décision.
- **Modèle** : Claude Opus 5.5 (`claude-opus-5-5`).
- **Heures (UTC, `date -u`)** : début 2026-11-19T08:03:24Z ; écriture à partir de 2026-11-19T08:04:46Z.
- **Dépôt** : arbre courant au commit `71786e8fd232a3e564450e17c859ce1b433832a4` à l'écriture. Brouillon 4 et note lus par `git show FETCH_HEAD:…` après `git fetch` de `claude/pensive-bardeen-1fv7hw`, sommet `37a3f4fc3703a2e6d7a904b50c43ba6e82491215`.
- **Cloisonnement** : aucune valeur de seuil, aucun nombre tiré du document de la base, de la règle de la tâche des organismes ni des seuils du texte archivé, aucun interne de moniteur. Les nombres présents sont des numéros de ligne, des empreintes, des heures et des comptes déjà écrits dans le brouillon 4.

### Pièces lues (empreinte recalculée ; toutes égales à l'attendu)

| pièce | empreinte | lu |
|---|---|---|
| brouillon 4, `prereg/T0.7-organismes-discrets-v-a-v2-brouillon4.md` | `16187b78b376491a6c83fe453d4239d438301085ab50a7a88583f07df7e19b68` | sections 4, « Seuil », 6.2 (clés), 6.3 (m), 6.9, 6.10, 6.12, 7.2 (A17), 7.4, 7.5, 7.7, 8.2, 12 (nœud 12), 13 ; recherche de mots ailleurs |
| note du rédacteur, `docs/notes/relance-organismes-discrets-v1/preenregistrement-v2-brouillon4-note-du-redacteur-v1.md` | `04fe602efd39b3738328aa077ecd92380f700fcb8b6357a2a39a144efaac4ce3` | partie 3 (correspondance), début de la partie 4 |
| mon rapport précédent, `docs/notes/bras-a-contre-lecture-habilitee-v1/verification-courte-habilitee-brouillon3-v1.md` | `2f7b43ec…` | en entier |
| registre des GO, `registres/go.md` (arbre courant) | — (registre vivant) | lignes 442 et 444 à 448 : GO-2026-11-19-09, -11 à -15 |

Pièces de seuils relues aux sessions précédentes, sans réouverture : le document de la base (`72b067d5…`), la règle de la tâche des organismes (`ef31feff…`, lignes 570 à 586) et le texte archivé (`06ab6a2f…`). Les numéros de ligne cités par le brouillon 4 pour ces pièces sont ceux de mes rapports, et je les ai reconfirmés.

Non ouverts : noms « consigne-privee », « conception-ii-b » ; `brouillons/ii-b-saboteur-budget-v1/`, `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; aucun résultat. Pas de recherche récursive, pas de réseau hors du `git fetch` nommé, aucune dépense, aucun fichier existant modifié, rien de committé.

---

## Verdicts

### 1. Mes trois points d'alors

**(a) Témoin positif de la base selon GO-2026-11-19-09 et -14 : conforme ; une référence périmée.**
- **Section 4, point 3 (ligne 310)** : cite GO-09 mot pour mot. L'écart au préenregistrement scellé de la base est déclaré, lignes 41, 51, 107, 132 et 177. La base ne compte que dans un sens : si elle détecte, la dose n'est pas discrète (GO-14) ; si elle ne détecte pas, c'est « non interprétable ».
- **Table « Seuil », ligne de la base (ligne 407)** : même lecture ; elle renvoie aux lignes 575 et 576 de la règle.
- **6.12 (ligne 590 ; point 4 (i), ligne 596)** : même lecture ; la ligne de lecture BA-L2 est déclarée tenue par le mot de Lazar donné d'avance. Cela suit GO-09, qui répond à la ligne 177 du document de la base.
- **Table C (ligne 666)** : lue dans l'ordre C3, C1, C4, C5, C6 ; la ligne C2 est retirée. C3 rend « non discret » quand la base détecte. Une base qui ne détecte pas ou qui n'est pas calculable n'empêche rien. Les lignes C1 et C4 à C6 sont exclusives et complètes dans cet ordre.
- **7.5 (lignes 680 et 683)** : « réfutée » compte C3 ; « sans objet » est redéfini comme « aucune dose en B8 », changement déclaré ; l'état de la base est rapporté « non interprétable (sans témoin positif) ».
- **7.7, phrase de C6 (ligne 697)** : elle porte « non interprétable » ; la ligne 698 interdit « la base échoue » employé seul.
- **Aucune contradiction entre ces lignes, sauf une** : 6.12, point 5 (ligne 598), finit par « Une base non calculable ne compte pas (elle ne détecte pas) : ligne C2 ». C2 est retirée.
  **Renvoi corrigé** : « ligne C1 et suivantes ; rapportée non interprétable (7.5) ».

**(b) Les six corrections de 6.12 : appliquées ; une contradiction neuve hors de 6.12.**
1. **Lignes BA-L3 et BA-L3b, et correspondance des jeux** (point 4 (ii), ligne 597) : conforme.
2. **Tirages dégénérés de la base** (point 5) : « non calculable » pour la base, conforme à la règle (ligne 576). **Mais** le brouillon dit deux choses sur les moniteurs appris (classifieur lexical, classifieur de surface) :
   - 6.9 (ligne 559) et 6.10 (ligne 563) : les tirages dégénérés de leur intervalle les rendent « indécis » à la dose ;
   - A17 (ligne 642) et 8.2 (ligne 714) : les tirages dégénérés « dans un intervalle autre que ceux de la base » sont un arrêt de course, ce qui inclut ces deux moniteurs.

   **Renvoi corrigé** : choisir l'une des deux lectures et écrire la même en A17 (ligne 642), en 8.2 (ligne 714), en 6.9 (ligne 559) et en 6.10 (ligne 563). Si « indécis » est retenu, A17 et 8.2 doivent exclure aussi les intervalles des moniteurs appris. Le texte doit aussi dire ce que deviennent les tirages dégénérés dans l'intervalle d'un moniteur non appris (moniteur boîte noire, agrégateur, juge).
3. **Centre de tâche** (point 1, ligne 592) : il comprend le témoin identité ; le minimum est repris comme compte absolu. Conforme à la lettre de la ligne 66 du document de la base ; atteignable avec l'effectif du bras.
4. **Intervalle, plancher et permutations propres à la base** (point 7, ligne 600 ; 6.9, ligne 553) : conforme.
5. **Entrées du code, liste blanche, vocabulaire sans les transcriptions de fabrication** (point 6, ligne 599) : conforme.
6. **Audit et réserves** (point 8, ligne 601) : gardés ; l'item de l'audit qui dépend du témoin positif est sans objet, suite logique de GO-09. Conforme.

**(c) 6.9 : conforme.**
- Famille fixée d'avance : cinq moniteurs × trois doses, m = 15 (ligne 555). Toutes les valeurs p sont calculées aux trois doses, en B8 ou non, et ajustées ensemble avant la table C : écrit en 6.9 (ligne 555) et en 6.3 (m) (ligne 453).
- Méthode du quantile : « linéaire », définie en 6.2 (interpolation linéaire entre statistiques d'ordre, méthode par défaut de `numpy.quantile`).
- Clés de graine : `boot/moniteur/{moniteur}/{dose}` et `perm/moniteur/{moniteur}/{dose}`, en 6.2, la première désormais décrite comme servant aussi à la condition (b).
- Niveau marqué « proposé » (ligne 406).
- Le sens des deux conditions de non-détection reste celui que j'ai vérifié au brouillon 3. Le changement de forme de la condition (a), déclaré (ligne 558), va dans le sens qui rend « discret » plus difficile.
- Les moniteurs appris sont réappris à chaque permutation, sur les mêmes plis (ligne 556) : exécutable.

### 2. Juge d'une autre lignée sous GO-2026-11-19-15 : à la bonne place ; écart à N-053 non écrit comme tel — **non conforme (écriture)**

- **Place, conforme.** Le juge est dans le verdict : section 4, point 4 (ligne 311) ; 6.9 (ligne 555) ; 6.10 (ligne 563) ; table C (lignes 666, 672 à 674) ; phrase de C6 (ligne 697). Il ne peut qu'empêcher « discret » :
  - il entre dans C4 s'il repère ;
  - il mène à C5 s'il est indécis ;
  - C6 exige qu'il ne repère pas.

  **À déclarer, sans changement de règle** : son entrée dans la famille de Holm élargit l'ajustement pour les quatre autres. Elle peut donc faire passer une dose de C4 (« réfutée » par un autre moniteur) à C5 (« non concluante »). Elle n'affaiblit pas C6, mais elle affaiblit un peu « réfutée ».
- **Écart à N-053, non écrit comme tel.** GO-15 (`registres/go.md`, ligne 448) dit que ce choix « remplace, pour le bras A, l'option retenue au nœud 10 » et « s'écarte de N-053 pour ce bras ; N-053 reste en vigueur ailleurs ». Le brouillon écrit au contraire « lecture de la décision N-053 que faisait déjà le texte archivé, déclarée » (lignes 144, 311, 563, 874). Il ne cite pas GO-2026-11-19-15 : aucune occurrence ; la case « nœuds » (ligne 887) dit « ligne de GO à inscrire […] si elle ne l'est pas ». Elle l'est.
  **Renvoi corrigé** : aux lignes 144, 311, 563, 874 et 887, écrire « écart à la décision N-053, point 4 (juge en bras rapporté), pour le seul bras A, décidé par Lazar (GO-2026-11-19-15) ; N-053 reste en vigueur ailleurs », et citer GO-2026-11-19-15.
- **Sous-échantillon, compatible avec un rôle décisif.**
  - Par défaut, le juge lit 32 des 80 positions de chaque tâche et condition, aux mêmes positions dans les cinq conditions (6.10, ligne 563). Son aire, son plancher par permutations et son intervalle se calculent sur ce sous-échantillon.
  - Une puissance moindre le rend plus souvent « indécis », donc mène à C5 : c'est le sens prudent, déclaré aux lignes 311, 666 et 680.
  - La phrase de C6 dit la lecture faite, « sur un sous-échantillon de 2 560 actions » ou « sur toutes les actions » (ligne 697). La variante à toutes les actions est une case de 13.1, à fixer avant scellement (ligne 890).
  - **Remarque** : la phrase de C4 (ligne 672) ne dit pas sur quelle part des actions le juge a repéré quand c'est lui qui repère. Ajouter la même mention qu'en C6.

### 3. Les deux cases de 13.1 qui dépendent de la mère : ce qui manque exactement

- **« Consignes des moniteurs » (ligne 894).**
  - *Moniteur boîte noire par action* : la proposition P-010 (`docs/decisions/proposition-P-010-T0.8-moniteur-par-action-v1.md`, `2dec994f347e8a157cfd45aefb48db41466313e27958f6dbe3d9e325537fff63`) ne contient pas la consigne. Elle dit, lignes 21 et 46, que l'invite est dérivée d'une invite publiée et qu'elle sera « transcrite, versionnée et scellée » à côté de cette invite, puis contre-vérifiée. Il manque donc deux choses :
    1. le chemin et l'empreinte de cette invite dérivée scellée ;
    2. une pièce empreintée qui établit que c'est bien l'invite du moniteur de la ligne 144 du texte archivé, par exemple la configuration ou le code qui la charge, avec son empreinte.

    Je ne l'ai pas cherchée : il faudrait parcourir le code des bases, hors des chemins nommés.
  - *Agrégateur séquentiel* : il n'a pas de consigne propre ; il hérite de celle du moniteur boîte noire.
  - *Juge d'une autre lignée* : la décision N-053 (`2204256d…`, ligne 34) fixe sa famille, pas sa consigne. Aucun préenregistrement de ce juge n'existe sous `prereg/` (recherche par nom, rapport du brouillon 2). Il manque le chemin et l'empreinte de la pièce qui fixe sa consigne, ou la mention écrite qu'aucune pièce ne la fixe.

    Il est désormais dans le verdict. Si aucune pièce ne fixe sa consigne, l'hypothèse de travail de la section 4 reste non vérifiée pour un moniteur décisif, et la phrase de C6 la porte comme telle (« selon la case […] »). C'est à dire avant scellement.
- **« Code de la base » (ligne 895).** La source est citée : `registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json`, `e418fdafbf8362f0458eb0448ec2d32ffa9a8bb122ec619ad0aaf68a9df3b43b`, ligne 16 de `registres/scellements-v1.md`. Il manque la **version neuve** elle-même, qui n'existe pas encore :
  1. son chemin et son nom versionné (R12) ;
  2. le commit et l'empreinte sha256 de chaque module ;
  3. la ligne qui l'inscrit au registre des scellements, sur le modèle de la ligne 16 ;
  4. sa contre-lecture par un agent neuf ;
  5. les essais de ses gardes sur un cas sain et sur un artefact : effectifs du bras, plis, centre avec le témoin identité, « non calculable » sans arrêt.

  Elle doit porter les points 1 à 8 de 6.12.

### 4. Cloisonnement de ce rapport — **conforme**

Ce rapport ne donne aucune valeur de seuil, aucun nombre tiré du document de la base, de la règle de la tâche des organismes ni des seuils du texte archivé, aucun interne de moniteur (ni poids, ni direction, ni score, ni texte de consigne). J'ai vérifié par une recherche des nombres décimaux et des pourcentages avant scellement : il ne reste que des identifiants de pièces, des numéros de section et le nom du modèle.

---

## Conclusion

**B7 non levé.** Il reste trois corrections d'écriture :
- 6.12, point 5 : remplacer le renvoi à la ligne C2, retirée ;
- les tirages dégénérés des moniteurs appris : une seule lecture en A17, 8.2, 6.9 et 6.10 ;
- l'écart à la décision N-053 et la ligne GO-2026-11-19-15 : à écrire et citer aux lignes 144, 311, 563, 874 et 887.

Une fois ces lignes corrigées, une vérification de leur seule différence suffit pour lever B7. Les cases « consignes des moniteurs » et « code de la base » restent à remplir avant scellement, indépendamment de B7.
