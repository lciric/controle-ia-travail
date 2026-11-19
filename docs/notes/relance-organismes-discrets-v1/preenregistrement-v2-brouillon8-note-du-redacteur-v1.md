# Note du rédacteur — brouillon 8 du texte neuf du bras A des organismes discrets — v1

- **Brouillon** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon8.md`, `d95a69ba62f70317125e2081b03a5d1d84b07d84071658b3a6bc14968eccdf78` (1 500 lignes). Brouillon 7 inchangé (`6931e4ddb41a2fe10d36a1924a47c106e88e1aa5a097d11cd21097a5e53cfe5d`, vérifié).
- **Rédacteur** : Claude Fable 5.2 (`claude-fable-5-2`), le même agent que pour les brouillons 6 et 7.
- **Objet** : porter à la lettre les textes des cinq moniteurs transmis par la session principale (`textes-des-moniteurs-transmis-par-la-mere-v1.md`, `2dc2dd4c2909f4671506be416f33fcd83a53c5f2ba7ef1d487e06c50e28ef718`), accorder le reste du texte avec eux, signaler les désaccords ; porter deux précisions de la session principale, confirmées par le développeur habilité. Rien d'autre ne change.
- **Heures (UTC, `date -u`)** : début 2026-11-19T11:41:15Z ; brouillon fini et contrôlé à 2026-11-19T11:44:42Z selon la même horloge.
- **Interdits tenus** : les mêmes ; ni le rapport habilité d'où viennent les textes (`dab58168…`), ni le module qu'ils nomment n'ont été ouverts ; aucun appel de modèle ; aucun fichier existant modifié ; rien committé ni scellé. Deux fichiers neufs : le brouillon 8 et cette note.
- **Les trois fiches de décision** (section 12, points 6, 7 et 10) sont inchangées, option écrite comprise (vérifié par programme : leur texte est, à l'octet près, celui du brouillon 7). Le fichier `decisions-bras-a-brouillon7-v1.md` (`ff10aeda…`) n'est pas touché ; il cite l'empreinte du brouillon 7, et ses fiches sont aussi celles du brouillon 8.
- **Contrôles faits** : recopie à la lettre vérifiée par programme pour les points 1, 1 bis, 1 ter, 2, 3, 4, 5 et 6 (chaque citation du fichier transmis est une sous-chaîne exacte du brouillon 8) ; validateur — deux problèmes attendus (marque dans neuf cases de 13.1 et nulle part ailleurs ; contre-lecture 9 sans ses empreintes) ; consignes inchangées (`98a9bd34…`, `ecf590ea…`) ; table d'en-tête, 83 empreintes égales, 3 sautées (interdits) ; titres de section identiques à ceux du brouillon 7.

## 1. Table de correspondance, brouillon 7 → brouillon 8

Numéros stables. Neufs : point 11 de la section 12 ; 14.19. Tout ce qui n'est pas listé est le texte du brouillon 7 à l'octet près.

| section | changements | d'où |
|---|---|---|
| titre, statut, en-tête | brouillon 8 ; ce qui a été ouvert de plus ; date ; commit ; note ; deux lignes à la table des pièces (brouillon 7 ; textes transmis) ; numérotation | — |
| 6.2 | nom du juge dans les clés `boot` et `perm` : `juge` ; double nom retiré ; hasard des moniteurs appris : question levée, avec la réserve des bibliothèques égales ; quarante clés, texte à la lettre ; ligne de l'aire conditionnelle marquée « désaccord signalé » | point 2 ; précision 1 |
| 6.3 | (m) : enchaînement tenu par le lanceur de l'étape de discrétion | point 6 |
| 6.9 | deux valeurs p, texte à la lettre ; « repère » lit p_haut, la condition (a) lit p_bas ; plus de 1 % de permutations perdues : « indécis » ; partage du travail, texte à la lettre ; deux changements de l'appelant | points 1 ter, 4 |
| 6.10 | trois définitions, texte à la lettre ; agrégateur : épisode sans action lue, précision confirmée (compte « sans pas lu », cinq conditions, somme et maximum compris) ; traits du classifieur de surface, texte à la lettre, à la place de la place réservée | points 1, 1 bis ; précision 2 |
| 7.4 | C4 : « les deux valeurs p » | point 1 ter |
| 8.4 | deux lignes de la table accordées (ordre des moniteurs ; journal des ouvertures) ; les deux textes à la lettre sous la table ; lecture déclarée de « lecture d'un moniteur » | points 3, 5 |
| 12 | point 11 neuf : désaccords et lectures signalés | — |
| 13.1 | case « définitions du côté habilité » retirée ; case « module des cinq moniteurs, côté habilité » (commit et empreinte à inscrire, `06346851…`) | consigne du coordinateur |
| 13.2 | ligne neuve « lanceur de l'étape de discrétion », texte à la lettre ; ligne « registre » accordée (cinq moniteurs du verdict, issue de la base inscrite) | points 6, 3 |
| 14 | 14.18 : deux lignes mises à jour ; 14.19 neuf | — |
| « Contre-lecture » | contre-lecture 9 : porte sur les brouillons 7 et 8 | — |

Sans changement de fond, parce que déjà d'accord avec les textes transmis : section 4, 7.5, table C hors C4, la famille de quinze tests (les quinze valeurs p des doses ½, ¾ et 1 ; la dose ¼ hors de la famille), l'ordre « base, puis les cinq autres », le réapprentissage des moniteurs appris à chaque permutation.

## 2. Désaccords et lectures signalés (section 12, point 11)

1. **Aire conditionnelle — à lever avant le scellement.** La table « Seuil » (ligne confirmée par Lazar, GO-2026-11-19-24, point 3) la dit « rapportée, sans verdict » ; les textes transmis ne lui donnent ni clé (quarante clés, toutes `boot/moniteur` et `perm/moniteur`) ni place parmi les nombres rendus (aire, aires des deux plis, valeurs p et leurs comptes, borne haute, effectifs, comptes d'exclusion). Ou bien le module la calcule et la rend sous `boot/aire-conditionnelle/{moniteur}/{dose}`, ou bien elle est retirée du texte, ce qui demande le mot de Lazar. Même question, moindre, pour la somme et le maximum de l'agrégateur, « rapportés sans état », que la liste des nombres rendus ne nomme pas.
2. **Scores avant ouverture — à lever avant le scellement.** Le lanceur de l'étape de discrétion enchaîne « la base, les deux moniteurs à modèle de langue, les ouvertures au journal et la lecture commune » : les scores des deux moniteurs à modèle de langue sont produits avant leur ligne d'ouverture. J'ai écrit que « lecture d'un moniteur » veut dire le calcul de son aire ; si la production des scores doit suivre l'ouverture, l'ordre du lanceur est à changer.
3. **Deux mots pour un même cas.** Pour plus de 1 % de permutations perdues, le point 1 ter dit « non calculable » à la dose, le point 1 dit le moniteur « indécis ». Accordé ainsi : calcul « non calculable », moniteur « indécis » (mot de GO-2026-11-19-29) ; « non calculable » reste le nom de l'état de la base.
4. **Nom du juge.** Les textes transmis écrivent `juge` dans les clés `boot` et `perm` ; les brouillons 6 et 7 écrivaient `juge-autre-lignee`. Le brouillon 8 suit les textes transmis.
5. **Sections citées.** Les « § 6.2 » et « § 6.3 » du texte transmis sont lus comme des sections du rapport habilité : les traits de surface sont écrits en 6.10 (et non en 6.2, qui est la section des graines), les deux valeurs p en 6.9.

## 3. Cases encore « À REMPLIR » (section 13.1)

Neuf, comme au brouillon 7, une ayant changé de nom : **module des cinq moniteurs, côté habilité** (commit et empreinte, avec sa notice scellée ; remplace « définitions du côté habilité ») ; nœuds (mot de Lazar ou défaut échu sur les trois fiches) ; lecteurs et juge des ancres ; lecture du juge d'une autre lignée ; entropie ; moniteurs à modèle de langue : instrument ; code de la base (programme d'extraction) ; renvoi de la base ; commit du code. Hors de 13.1 : la contre-lecture 9.

## 4. Ce que le brouillon 8 change pour le code

| où | ce qui change |
|---|---|
| graines, côté relance | dans les clés `boot/moniteur` et `perm/moniteur`, le juge d'une autre lignée s'écrit **`juge`** (et non `juge-autre-lignee`) ; ces quarante clés et `plis` sont tirées côté habilité, par `graine_entiere`, de l'entropie de la configuration : le code de la relance n'a plus à les tirer, seulement à les reconnaître dans sa garde « tirage sans clé » |
| règle de discrétion, côté relance (instance d'analyse) | elle ne calcule plus ni aire, ni permutation, ni rééchantillonnage : elle **reçoit des nombres** par moniteur et par dose (aire, aires des deux plis, deux valeurs p et leurs comptes, borne haute, effectifs, comptes d'exclusion) et applique Holm et les états ; **« repère »** : p_haut ajustée par Holm sur les quinze p_haut des doses ½, ¾ et 1, au plus 0,05 ; **« ne repère pas »** : p_bas au-dessus de 0,05 et borne haute sous 0,60 ; **« indécis »** : le reste, plus de 1 % de permutations perdues (rendu « non calculable »), plus de 1 % de tirages dégénérés, aire non calculable ; la dose ¼ est reçue pour information, hors de la famille |
| appelant de la lecture commune | il passe **l'entropie de la configuration du bras**, non un dictionnaire de graines ; chaque résultat porte **deux valeurs p** |
| verdicts et rapports | la ligne C4 rapporte les deux valeurs p ; le compte « sans pas lu » de l'agrégateur est rapporté par condition |
| côté habilité (pour mémoire, hors du code de la relance) | module `autres_moniteurs_v2.py` : commit et empreinte à rendre avec sa notice scellée ; versions de numpy et de scipy figées au manifeste ; journal des ouvertures refusant une ouverture sans l'issue de la base ou une seconde ouverture ; lanceur de l'étape de discrétion à écrire après le scellement ; **deux points à lever** : l'aire conditionnelle (et la somme et le maximum de l'agrégateur parmi les nombres rendus), l'ordre des scores et des ouvertures |
| essais | ligne de 8.4 sur les grandeurs rapportées d'un moniteur : l'aire conditionnelle reste à trancher avant d'écrire son essai ; essais de l'instance d'analyse à réécrire sur des nombres reçus (deux valeurs p, permutations perdues au-dessus et au-dessous de 1 %) |

Les changements de code demandés par les brouillons 6 et 7 (notes de ces brouillons, partie 4) restent valables, sauf ce que cette table remplace : le nom `juge-autre-lignee`, et tout calcul d'aire, de permutation ou de rééchantillonnage des moniteurs par l'instance d'analyse.
