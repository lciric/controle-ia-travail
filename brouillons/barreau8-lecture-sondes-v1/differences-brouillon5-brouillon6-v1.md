# Différences entre le brouillon 5 et le brouillon 6 du texte « lecture des sondes du barreau 8 et passe de recalcul de l'activité interne » — v1

- Brouillon 5 (état intermédiaire, scellé par son compagnon, jamais rendu à la conductrice) : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon5.md`, empreinte `eb3e770d5b7420546331f3bff78ef5495a098862be84ff6a03f97f84100a0c6f`. Ses différences avec le brouillon 4 (toutes les remarques C-1 à C-12 de la contre-lecture du brouillon 4, l'option (b), le compte de taille) : `brouillons/barreau8-lecture-sondes-v1/differences-brouillon4-brouillon5-v1.md`, empreinte `146f7e23f5b02850e83720a407a6f350eaccfee40f060462f60ad31a6fc1a4bc`.
- Brouillon 6 : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon6.md` (empreinte : son compagnon `.sha256`).
- Cause : la note d'interface est remplacée par sa version 5, `docs/notes/barreau8-cote-moniteurs-entrees-v1/interface-passe-cote-moniteurs-v5.md`, empreinte `407099bc150b8730237cceb0c1cf051440e255b483f44461b38a6c835c13107f` (vérifiée ; lue en entier ; son titre dit « v4 » ; aucun renvoi de provenance suivi). Le message est arrivé après l'écriture du compagnon du brouillon 5 : plutôt que d'écraser un fichier scellé (R12), le rédacteur écrit un brouillon 6.
- Rédacteur : Fable 5.2. Écrit le 2026-11-19 entre 01:02Z et 01:04Z (`date -u`), par programme, à partir du brouillon 5 : quatorze remplacements contrôlés, dont trois cellules de table remplacées en entier (I-9, D-12, D-14 retirée).

## Ce qui change, une ligne par objet

| objet | où, dans le brouillon 6 |
|---|---|
| La note d'interface est citée dans sa version 5 (chemin et empreinte) partout où la version 3 l'était | en-tête (documents qui font foi ; la version 3 y reste nommée comme remplacée) ; table I, source unique |
| Vocabulaire de l'état par unité : **établi par la note** (section « Livraison », alinéa de l'extrait) ; la remarque C-4 se ferme par citation ; ce n'est plus une hypothèse du texte | I-9 |
| Portée de la phrase du dommage : citée de la note (question (9), ligne « Portée »), non plus d'une réponse de la session mère | I-9 ; « Seuil », condition jugée, (a) |
| Extrait des états : nom `etats-lectures-iib-v1.json`, clés fixes, écrit seulement après le scellement ; contrôle mécanique à la réception (empreinte égale au compagnon et à la ligne `ETATS-COURSE-IIB`, clés exactement celles de la note, valeurs dans le vocabulaire) ; refus d'ouvrir ; essais sur cas sain et sur artefacts | D-12 ; liste d'arrêt, ligne 3 |
| L'extrait ne porte ni empreintes de sorties ni lignes de registre : la mention « si l'extrait les porte » est retirée | D-12 ; plan, point 3 |
| Condition de départ « version de la note qui nomme l'extrait » (D-14) : **fermée**, retirée | conditions de départ : 13 (D-1 à D-13) |
| Règle « condition jugée » écrite avec les clés exactes : `lecture_dommage.phrase` ; `lecture_diffusion.par_paire.B100-H.unite` ; `lecture_diffusion.par_paire.B50-H.unite` | « Seuil », condition jugée, (a) et (b) |
| Paire `B100-TJ100`, bases séparées `cout`, `traits`, `mots_et_cout`, unité de `TJ100-H`, phrase de la diffusion : **recopiées telles quelles en tête de la sortie et du verdict sous le titre « contexte de la course, sans effet sur le verdict »** ; elles n'entrent dans aucun état, aucune ligne, aucune réserve ; le juge ne les commente pas (choix du rédacteur, sans latitude laissée) | « Seuil », condition jugée, (b) |
| Les lectures du dommage et de la diffusion ne sont jouées qu'après le scellement de ce texte | plan, point 3 |
| Lecture incidente de la ligne 2206 du texte scellé des sondes v0, déclarée par le contre-lecteur du brouillon 4 | en-tête, exposition déclarée |
| Titre, statut, dates | en-tête |

## Point à trancher avant le scellement (signalé, non résolu par le rédacteur)

La note dit l'extrait « sans aucun chiffre hors du nom du run et des noms des conditions », sans nommer de clé qui porterait le nom de la course. Le texte exige « clés exactement celles de la note » : **si le programme de l'extrait écrit une clé pour le nom de la course, la garde de réception refusera d'ouvrir**. À faire dire par l'exécutante (clé présente ou non, et son nom) ; si elle existe, une ligne de D-12 est à amender avant le scellement.

## Inchangé

Tout le reste, dont l'option (b) (scores par action et scores par jeton des neuf sondes), la liste (b-1) à (b-6) du retour à (a), et la taille exacte de la livraison dans le pire cas : **1 502 781 440 octets** (98 672 640 + 73 728 000 + 1 055 129 600 + 275 251 200), sous 2 000 000 000.

## Champs ouverts

- Bloquent le scellement : 2 marqueurs — F-3 (entropie des graines) et l'entrée « Contre-lecture finale (texte rempli) ».
- Conditions de départ : 13 (D-1 à D-13).
- Décision ouverte : (b) contre (a).
