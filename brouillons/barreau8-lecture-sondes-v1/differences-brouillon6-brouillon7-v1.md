# Différences entre le brouillon 6 et le brouillon 7 du texte « lecture des sondes du barreau 8 et passe de recalcul de l'activité interne » — v1

- Brouillon 6 : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon6.md`, empreinte `527ed753e2434f0fd542e8f9a8c62ebcbf9ea7b32c7a8564ebed7c924ae65521`.
- Contre-lecture du brouillon 6 (Opus 5.5, contre-lecteur neuf) : `brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon6-v1.md`, empreinte `2ab73c2f5d5210cb5102b3f805b4653e9dfef6efcfddde22cc47a30a0f603587` (vérifiée ; lue en entier).
- Note d'interface, version 6 : `docs/notes/barreau8-cote-moniteurs-entrees-v1/interface-passe-cote-moniteurs-v6.md`, empreinte `20c9ed6e480646b6bf3a5f6007be5f88b439c916763a618f3880634e92ad8ce1` (vérifiée ; lue par différence faite par programme avec la version 5, lue en entier : deux lignes changées, le titre et l'alinéa de l'extrait des états ; aucun renvoi de provenance suivi).
- Brouillon 7 : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon7.md` (empreinte : son compagnon `.sha256`).
- Rédacteur : Fable 5.2. Écrit le 2026-11-19 entre 01:12Z et 01:18Z (`date -u`), par programme, à partir du brouillon 6 : remplacements contrôlés (chaque texte cherché doit paraître le nombre de fois attendu, sinon rien n'est écrit) ; une seule cellule de table est remplacée en entier (D-12).

## 1. Remarques de la contre-lecture du brouillon 6

| n° | objet | état | où, dans le brouillon 7 ; adaptation |
|---|---|---|---|
| N-1 (bloquante) | décision « scores par jeton » écrite ouverte, avec un défaut différent du texte | traitée, une adaptation, et étendue | « Ce que ce texte est », décision (9) ; titre du bloc de décision ; « Règle du scellement » à la place de « Défaut sous 48 heures : (a) » : textes repris. **Adaptation** : les mots « ou si un défaut (a) échoit » ne sont pas repris — il n'existe plus de défaut (a) ; le retour à (a) n'est possible que sur le mot de Lazar avant le scellement (consigne de la session mère). L'option (a) est dite « non retenue » au lieu de « défaut si Lazar ne suit pas ». **Même discipline à tous les blocs de décision** : règle générale du scellement écrite dans « Ce que ce texte est » ; chaque bloc dit l'option sous laquelle le texte est scellé et qu'après le scellement aucun défaut n'échoit, tout changement étant un écart, nœud de Lazar — règle du témoin-jumeau (« Seuil ») ; organisation de la passe ; décision de taille (t1) ; sondes et couches (a1) ; clause (2), option (b) |
| N-2 | liste du retour à (a) incomplète ; (b-5) effaçait une correction | traitée | Bloc de décision : (b-5) corrigée ; (b-7) à (b-10) ajoutées ; textes repris |
| N-3 | extrait des états d'après la note version 6 | traitée, forme adaptée | En-tête et table I : note citée en version 6 (les versions 5 et 3 nommées comme remplacées) ; I-9 ; D-12 remplacée en entier ; « Seuil », condition jugée (b) : `avertissement` et `run_id` recopiés sans effet ; liste d'arrêt, ligne 3. **Adaptation de forme seule** : le texte de D-12, donné en alinéas et en liste, est mis sur une ligne (cellule de table), mots inchangés ; en tête, « lue par différence faite par programme avec la version 5, elle-même lue en entier » décrit ce que le rédacteur a fait. Vérifié : l'alinéa de la version 6 nomme bien les quatre clés de premier niveau et le texte constant de `avertissement` |
| N-4 | garde d'alignement : réglage du décodage lu dans la configuration | traitée, forme adaptée | Garde P3, clause (b), remplacée par le texte du contre-lecteur (mis sur une ligne) ; trace, liste fermée. Vérifié : l'empreinte `177c7b61…d424` de `tokenizer_config.json` est celle de la question (1) de la note. L'hypothèse déclarée du brouillon 6 est retirée |
| N-5 | jeux et graines de la lecture descriptive des couches 7 et 23 et du bras de diagnostic | traitée | B8-P5, B8-P6 ; plan, point 5 (clé `descriptif/<sonde>/<jeu>`) ; textes repris |
| N-6 (mineure) | portée de P7 et de P2 ; repère de couche | traitée | P7 ; point (3) de « Ce que le côté des moniteurs n'observe plus » ; r8 (quatre couples) ; textes repris |
| N-7 (mineure) | S2 et S5 au libellé du dommage par condition | traitée | Lignes S2 et S5 ; textes repris |
| N-8 (mineure) | « ordre des clés » ; préfixe de phase | traitée | « Passe avant » (définition, valable partout) ; audit, contenu (1) |
| N-9 (mineure) | entrée finale non reconnue par le validateur | traitée | « Contre-lecture 4 (finale, texte rempli) » aux trois endroits ; entrée de la contre-lecture du brouillon 6 ajoutée sous le nom « Contre-lecture 3 bis ». Vérifié dans `src/controle_ia/prereg.py`, ligne 29 : motif `^\s*-?\s*\**Contre-lecture (\d+)\**` ; le validateur reconnaît cinq entrées (1, 2, 3, 3 bis, 4). Essai dans le dossier temporaire (entrée finale remplie sans empreintes, F-3 ouvert) : `['marqueur À REMPLIR restant hors des sections exigées', 'contre-lecture 4 sans ses deux empreintes (brouillon relu et rapport)']` |
| N-10 (mineure) | heures ; marge | traitée | Date : brouillon 6 fini à 01:04Z, brouillon 7 daté par `date -u` ; marge dite « avant l'index, la trace, le bordereau et les compagnons » |
| N-11 (mineure) | ligne L6 inatteignable | traitée | Ligne L6, colonne « verdict » ; texte repris |

Remarques refusées : **aucune**. Adaptées : N-1 (un membre de phrase non repris, et extension demandée par la session mère) ; N-3 et N-4 (mise en forme sur une ligne, mots inchangés).

## 2. Rien d'autre ne change

Option (b) inchangée ; taille exacte de la livraison dans le pire cas inchangée : 1 502 781 440 octets. Conditions de départ : 13 (D-1 à D-13).

## 3. Marqueurs restants

Deux, et deux seulement : F-3 (entropie racine des graines, tirée par la session mère) ; l'entrée « Contre-lecture 4 (finale, texte rempli) ».

Sortie exacte du validateur sur le brouillon 7 : `['section vide ou à remplir : Contre-lecture']`.
