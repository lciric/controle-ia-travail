# Vérification du programme des deux essais d'admission du bras A — livraison 7 (fichiers `_v6`) — v1

- **Vérificateur** : Claude Opus 5.5, contre-lecteur des livraisons 1 à 6, le 2026-11-21. Ni auteur de cette livraison, ni du devis.
- **Objet** : le commit `87a9a75de` et sa note `note-programme-essais-admission-bras-a-v6.md`, lue en entier. Les six fichiers `_v6` répondent « OK » à leur compagnon ; les outils de mutation version 2 sont versés sous `tests/mutations_essais_admission_v2/`.
- **Essais** :
  - la commande imposée, deux fois : **207 passés à chaque fois** ;
  - la campagne de mutations version 2, par la commande versée : **344 mutants, 344 tués, 0 erreur, code 0** ;
  - six essais jetables, hors du dépôt (`…/scratchpad/essais_jetables_l7/`), dont l'épreuve à blanc des pièces prêtes à l'emploi : tous passent.
- **Interdits tenus** : aucun réseau, aucun `git fetch`, aucune liste de chemins par motif, aucune clé, `GO_ID` jamais fixé dans l'environnement. Rien écrit hors ce rapport, rien scellé.

## Verdict

- **Engageable pour Mistral**, dès que les pièces réelles existent : le constat, le fichier des règles scellé, la liste locale des interdits, les lignes du registre poussées, et les relevés au fil des lignes. Les trois pièces prêtes à l'emploi de la note sont exactes, et le programme les accepte (section 5).
- **Engageable pour Google, côté code** : R-1 est fermé. Restent les décisions et les valeurs, non le code : l'avenant 2 (plafonds, seuils, délais à 65 536), les limites de mots, l'exemption de la sonde, et le constat de Google.

## 1. R-1 : la file du juge au régime prudent

**Fermé.**
- `regime_file_google` (`chef:1329-1343`) : champ fermé, « prudent » ou « courant », sans défaut ; en configuration définitive, « prudent » est exigé et « courant » refusé.
- La garde 10 met la file au régime prudent **quelles que soient les sondes** : le régime n'est courant que si les sondes sont « comprises » **et** si la configuration impose « courant », ce qui n'est admis qu'en essai (`chef:1410-1414`).
- Le régime imposé est recopié au contexte, au manifeste et au rapport.
- Les sept mutants de la fonction et les soixante et un de la garde 10 sont tués.

## 2. L'âge du fixage, compté aussi depuis l'envoi

**Fermé.** Mon essai de la livraison 6, rejoué sur `_v6` (`test_taux_vieux_par_un_constat_vieux_refuse`) : un constat vieux d'un mois est maintenant refusé (« la pièce est trop ancienne pour ce taux »). La même borne vaut depuis la pièce et depuis l'envoi, pour le constat, la lecture de la console et le mot du juge.

À dire à Lazar, comme le fait la note : sous 96 heures, un constat en euros ne sert que quatre jours au plus après le jour de son fixage.

## 3. La garde 10 : l'hôte du relevé de la clé 2

**Juste.** Les deux hôtes doivent être égaux, comme les noms servis et les orthographes. Puis l'ensemble est confronté à ce qu'inscrit la configuration, sans valeur lue par le rang de la clé (`chef:1402-1409`). C'est une défense en profondeur : `_releve_sain` refusait déjà un relevé d'un autre point d'accès.

## 4. Les autres mineurs

- **m-7, deux fichiers hors du périmètre** : toujours ` M` à `git status`, sur décision de Lazar.
- **Plafonds, seuils et délais à 65 536, lettre de la pièce partielle** : à l'avenant 2, sans objet pour le code.
- **m-4** : sans objet tant que le niveau de réflexion est gardé.
- **Neuf, à dire** : la liste locale des interdits, que la configuration nomme (`/home/user/hors-depot/essais-admission-bras-a-v1/interdits-v1.txt`), **n'existe pas** sur ce poste (constat de présence seulement). La note (b) dit « comme au gabarit » sans le rappeler. Sans elle, la garde 6 arrête tout, ce qui est sûr. C'est une pièce à faire avant la première ligne.

## 5. Les trois pièces prêtes à l'emploi

### Comment je les ai éprouvées

Essai `test_l7_a_blanc_jetable.py`. J'ai tiré une configuration définitive du gabarit `_v6` en appliquant **à la lettre** la section 6 (b) de la note : champs du premier niveau, trois lignes de Mistral. J'y ai mis :
- un constat écrit **à la lettre** de la section 6 (a), rempli en euros : crédit « au moins 7,87 » de source « borne basse dite par Lazar », taux de 1,1050, fixage de la veille ;
- le fichier des règles d'essai, scellé ;
- un relevé européen « signe constaté » pour la ligne globale ;
- un relevé sain, sonde « comprise » et majorant « établi », pour la file, avec `inscrit` égal à ce relevé.

Puis j'ai joué :
- la commande à blanc (`a_blanc`) pour chacune des trois lignes : elle joue les gardes 9, 10, 12, 13, 14, 15, 17 et 20, puis les gardes 3 et 6 sur tous les corps ;
- la garde 8 sur trois lignes de registre écrites **à la lettre** de la section 6 (c).

### Résultat

**Les trois lignes passent toutes les gardes d'avant l'envoi, garde 8 comprise. La même pièce est refusée pour Google.**
- La configuration définitive (`essai_local` nul) ne peut pas joindre le faux fournisseur : c'est la garde 14, et c'est voulu. L'épreuve s'arrête donc juste avant le lancement du relais. Les gardes qui suivent (relais, ouvrier, envois) restent éprouvées par la suite d'essais, sur une configuration d'essai.
- Un premier échec venait de mon propre montage, non de la note : j'avais placé le relevé européen sous la ligne de calcul de la ligne européenne elle-même, que le programme a vue close à juste titre. Avec une ligne de calcul distincte, tout passe.

### Exactitude, pièce par pièce

- **(a) Constat de Mistral seul** : exacte. Le seuil, « 7,87 € ne passent qu'à 1,1008 au moins », est juste (vérification de la livraison 6, section 3).
- **(b) Configuration des lignes de Mistral** : exacte. Deux précisions sont à ajouter pour la session :
  - la liste locale des interdits doit exister au chemin du gabarit (section 4) ;
  - le relevé européen inscrit pour la ligne globale doit être celui d'une ligne de calcul européenne close sur le signe constaté. Le gabarit le dit (garde 15), la note (b) l'écrit en clair.
- **(c) Lignes du registre** : exactes. La forme est acceptée par la garde 8 telle qu'écrite : huit cellules, « Lazar », date d'accord du jour, plafond à la lettre, marques avec leurs accents graves, empreintes du devis, de sa vérification et de l'avenant 1 (`5e255c5f…`, celle du gabarit). La condition dite par la note est juste et nécessaire : la ligne doit être portée par `origin/main` au moment du lancement.

## 6. Ce que j'ai ouvert

- La note de livraison 7, en entier.
- Le chef `_v6`, aux lignes 1329 à 1416, 3707 à 3726, plus des recherches de lignes. Le gabarit `_v6`, par programme : premier niveau et ligne `file-mistral`. Les essais `_v6`, par recherche de lignes (`Monde.releve`).
- `git log`, `git status`, `git ls-files` sur `tests/mutations_essais_admission_v2/`, les empreintes par `sha256sum -c`, chemin par chemin. La présence (non le contenu) de la liste locale des interdits.
- Lus par programme pendant les essais et la campagne : le lot des entrées nommé par le devis, les consignes et les règles par empreinte, les modules du programme de forme.
- Aucun chemin interdit ouvert, listé ni empreinté.
