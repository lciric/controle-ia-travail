# Contre-lecture de la note d'englobement de O4, v2 (décision R-2822 : N-SSRN-1 et N-SSRN-2)

- **Contre-lecteur : modèle K, neuf, autre modèle que l'auteur (modèle A)**
- **v2 relue** : `docs/notes/lecture-o4-suite-v1/lecture-o4-englobement-v2.md`, empreinte entière `9c3c81a9423ea3dcc03d43f940f3e67c85582abcbe94056ab219525b765fc0d1` (le compagnon `.sha256` concorde). v1 : `f521e164e79cb75e9b3f14a9bddb0cf8f57a5499e68f93276014e4b09fc130aa`. Générateur lu : `faire_englobement_v2_sans_noms.py`. Lecture fondatrice : `lecture-pdf-ssrn-o4-v2.md` (`93518e46d59825d9…`). PDF : trois empreintes conformes (`15cdb423…`, `2d4e1d61…`, `98757745…`).
- Début : 2026-11-14T23:31:52Z ; fin : 2026-11-14T23:33:34Z (`date -u`). Rien n'est scellé. Aucune dépense, aucun réseau.

## Verdict

**Porte la décision après corrections.** Les deux points de la décision sont portés (citations de Liu et coauteurs sur septembre, appui de la phrase d'avril p. 36 retiré, alpha contre facteurs fixés dit en avril et en septembre ; Koijen et Levy cités dans la phrase publiable fr/en). Aucune citation fausse. Trois corrections à faire : un nom de modèle resté (point e), une colonne de pages restée sur avril (point b), une phrase de la section 0 plus forte que la section 3.1 bis (point c).

## a. Rejeu du générateur

- Rejeu sur la v1 (empreinte contrôlée par le générateur) avec l'heure de la ligne « Version 2 » (2026-11-14T23:30:39Z) vers `/tmp/claude-0/k/rejeu-k-v2-neuf.md` : « 16 remplacements comptés » ; `cmp` avec la v2 : **identique** octet pour octet.
- Différentiel v1 → v2 (diff) : titre (l. 1), en-tête (l. 3 : ligne « Lecteur » étendue de la ligne « Version 2 » ; l. 5 : règle de lecture), section 0 (points 1, 3, 5 et paragraphe « Conséquence proposée »), section 2 (lignes LIU et KL), section 3.1 et 3.1 bis, section 4 (phrases fr/en et condition (d)), section 5 (points 1 et 4). Tout le reste est inchangé. La ligne « Version 2 » annonce « sections 0 (points 1, 3, 5), 2, 3.1, 4, 5 (points 1 et 4) » : le paragraphe « Conséquence proposée » (section 0) et la règle de lecture (en-tête, l. 11) changent sans être nommés. **Mineur** (voir constat 5).
- La ligne « Version 2 » dit « citations rejouées 91 sur 91 » : je rejoue `rejouer_citations_ssrn_o4_v1.py` sur `citations-ssrn-o4-v4.json` : « 91 sur 91 conformes ».
- Le générateur dit retirer les noms de modèles « repérés par motif » : il n'a aucun code de retrait ; les noms de la v1 ne disparaissent que parce que la ligne du lecteur et la section 3.1 sont remplacées (voir point e).

## b. N-SSRN-1 (Liu et coauteurs)

- J'ai extrait moi-même, de la v2 (sections 3.1 et 3.1 bis), les 29 citations de la forme `[p. N, ID] « … »` et les ai rejouées (`pdftotext -f N -l N`, espaces réduits, sous-chaîne, troncature « … » traitée par préfixe) : **29 sur 29 vraies sur la page indiquée** ; chacune concorde en page et en texte avec `citations-ssrn-o4-v4.json`.
- LIU : 21 citations sur le PDF de septembre (84 p.) ; 2 marquées « avril » (A13 p. 15, A14 p. 14), vraies sur la copie d'avril (71 p.). Aucune citation de LIU non marquée n'est tirée d'avril.
- Phrase d'avril p. 36 : « it lacks direct access to factor model results during the discovery loop » est bien sur la page 36 de la copie d'avril, et **absente** du PDF de septembre (recherche sur tout le texte). Elle n'est plus un appui nulle part : section 0, point 3 (l. 30-32) et section 3.1 (l. 96-97) la citent seulement comme retirée. Les autres mentions de « 36 » (l. 134, HLZ) sont sans rapport.
- Alpha contre un modèle de facteurs fixé : avril p. 14 (« Carhart (1997) four factors ») et p. 15 (alpha dans le retour au proposeur) ; septembre p. 19 (« discovery-stage alpha uses the Fama–French five-factor model ») et p. 57 (entrée d'archive avec alpha) : vérifié sur pages. Dit dans la section 0, point 3, et section 3.1. Les pages « 1963 à 2024 », « trois modèles de facteurs » (p. 11, 22, 30) et le test prospectif « non fait » (p. 6, 34) concordent aussi avec le PDF. « Aucune e-valeur sur 84 pages » : zéro occurrence de « e-value / e-process / anytime ».
- **Défaut** : section 2, ligne LIU, colonne « pages décisives » : « 1, 4, 8, 14, 18, 22, 26, 28, 36 » reste la liste d'avril (dont la p. 36 retirée) alors que la ligne renvoie à la version de septembre. Voir constat 2.

## c. N-SSRN-2 (Koijen et Levy)

- Phrase publiable : cités en français (« Koijen et Levy, 2026, SSRN 6474601 », l. 166) et en anglais (l. 170), pour « prédictions de systèmes à modèle de langue faites avant que les données existent ». La condition (d) le consigne. Section 0 : point 1 (3e puce), point 5 (partie « en temps réel » de (iv)) et paragraphe « Conséquence » le citent aussi. Les autres passages sur le scellement avant les données (point 4, SEADS ; section 3.2, 3.3) parlent d'autres pièces et n'ont pas à citer KL.
- Les citations de KL (K05, K02, K01, K03, KO1, K32, K31) : vraies sur leurs pages (p. 8, 1, 1, 3, 11, 19, 19) ; date imprimée « June 30, 2026 » vérifiée p. 1 ; 39 pages.
- **Défaut** : la section 0, point 1, dit des systèmes optimisés qu'ils ont des « prédictions faites en temps réel, avant que le rendement n'existe », alors que la section 3.1 bis dit que « le texte ne dit pas que les prédictions de la seconde moitié du trimestre ont été émises avant les événements (p. 16) » et que la lecture fondatrice (K25, K26, K27, KO2) tient cela pour non établi (« probable, sans l'établir »). Le point 1 est donc plus fort que la pièce. Voir constat 3.

## d. Verdict et ajouts

- « O4 : occupée en partie » inchangé ; « O4 ne peut pas être déclarée libre hors du dépôt » inchangé ; rien n'est déclaré libre ; la phrase publiable garde « ce qui ne vaut pas pour l'ensemble du champ » et reste soumise au mot de Lazar.
- Ajouts au-delà de la décision : néant de fond. Sont ajoutés, en conséquence directe : la ligne KL du tableau, la sous-section 3.1 bis, la mise à jour des points 1 et 4 de la section 5 (« lu »). Le retrait des noms de modèles relève de R-2690, déjà acquis, non de la décision (déclaré dans la ligne « Version 2 »).

## e. Noms de modèles

- Générateur : aucun nom ni identifiant de modèle.
- v2 : l. 197 contient le message de refus de l'outil recopié tel quel (« Claude Code auto mode classifier ») : admis par la consigne. **l. 107 contient un nom de modèle de langue d'une version de la famille d'un fournisseur (citation « (…, p. 24) » de SEADS : voir le texte de la ligne, entre parenthèses après « proposeur modèles de langue »)** : resté de la v1 (même ligne, l. 74 de la v1) ; le générateur ne le traite pas. Les noms de la ligne « Lecteur » et de la ligne « Objet » de la v1 sont, eux, bien partis.

## Constats classés

**Majeur**
1. Nom de modèle resté, section 3.2, l. 107 de la v2 (point e) : contredit « les noms de modèles de la v1 sont retirés (R-2690) ». Correction : remplacer la parenthèse par « (un modèle de langue du commerce, p. 24) » (ou retirer le nom), avec un remplacement compté de plus dans le générateur (nouveau nom de fichier, R12) ; ou, si l'on veut garder le nom comme fait cité de SEADS, le dire à Lazar comme exception à R-2690.
2. Colonne « pages décisives » de la ligne LIU (section 2) restée sur avril, p. 36 comprise : incohérent avec N-SSRN-1 et avec la section 3.1. Correction : « 1, 5, 6, 11, 15, 19, 22, 29, 30, 32, 38, 40, 42, 57 » (septembre, pages des citations L01-L25 de la v2), et, si l'on veut, « avril : 14, 15 ».
3. Section 0, point 1, 3e puce : affirme le temps réel pour les systèmes optimisés, plus fort que la section 3.1 bis. Correction : « pour des systèmes à modèle de langue, dont le banc d'essai est évalué en temps réel, avant que le rendement de l'annonce n'existe (… ; pour les systèmes optimisés sur la première moitié du trimestre, l'émission des prédictions de la seconde moitié en temps réel est probable, non établie, p. 11, 16) », et la phrase de la section 4 reste telle quelle (elle parle des prédictions du banc, p. 1, 3, 11).

**Mineur**
4. Section 5, point 1 : la seconde phrase (« La copie lue … porte la date d'avril 2026 … l'identité exacte n'est pas vérifiable ») est périmée en v2 : dire qu'elle vise la copie d'avril.
5. Ligne « Version 2 » : la liste « Changent seulement » omet l'en-tête (règle de lecture, l. 11) et le paragraphe « Conséquence proposée ». Les ajouter à la liste.
6. Section 6 (refus SSRN) reste vraie pour la v1 mais n'est pas marquée « v1 » : ajouter « (v1) » en tête de la section.
7. Identifiant « KO1 » (lettre O) dans la v2 et le fichier de citations, au lieu de « K » + chiffre : seulement une étiquette ; garder tel quel (concorde avec le fichier) ou renommer des deux côtés.

**Aucun constat bloquant ; aucune citation fausse.**
