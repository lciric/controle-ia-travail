# Contrôle du différentiel v1 → v2 de l'additif 2 (code) de la ligne 3 — v1

Pièce de travail (classe C), 2026-11-20. Contre-lecteur, modèle S, le même que pour la version 1. Rien écrit dans le dépôt ; rien sous `/root/.claude/` ; aucun lancement du banc ; aucun refus d'outil.

## Verdict : **Conforme après corrections** (deux corrections d'un mot ou d'une incise, aucune ne touche un fait ni un critère)

## Empreintes
Mandat (`2e602121…`), contre-lecture (`7cf5a2c9…`), additif v1 (`65609405…`), additif v2 (`18650157…`), fichier de remplacements, journal, différentiel, rapport du rédacteur, outil (`391db990…`) : chacun égal à son compagnon ou à l'empreinte annoncée.

## 1. Rejeu de l'outil, à l'octet
`python3 -B scripts/remplacer_texte_exact_v1.py --cible` (additif v1) `--remplacements` (fichier du rédacteur) `--sortie` (mon dossier `rejeu-additif-2/`) : « FAIT : 7 remplacement(s) », sortie d'empreinte `186501571b1e6cf03e3abff1991a987f86ed591a0bda00864e3df77f851c0ce5`, **égale à l'empreinte de l'additif v2 du rédacteur**. Sept remplacements, six lignes changées au différentiel (titre, version, CHEMIN, numpy, points 1 et 3 du § 7) ; rien d'autre ne change.

## 2. A, B et C à la lettre
J'ai cherché chacun des quatre textes de ma contre-lecture (A ; B point 1 ; B point 3 ; C) par motif exact dans ma contre-lecture (une occurrence chacun) puis les mêmes motifs dans l'additif v2 : quatre lignes, une par texte. Lecture du JSON de remplacements : les textes neufs sont ceux de la contre-lecture, caractère pour caractère. A (chemin absolu) à la puce `CHEMIN`, C (numpy 2.5.3, ≥ 1.25, `versions.numpy`) à la puce « Environnement », B première phrase en fin de point 1, B seconde phrase en fin de point 3. Chaque ancre figure une fois dans la cible (règle de l'outil). **Conformes.**

## 3. Phrase de la ligne de version (de la main du rédacteur)
Texte : « Version 2, même jour : elle porte à la lettre les corrections A, B et C de la contre-lecture `contre-lecture-additif-2-code-ligne-3-v1.md` (`7cf5a2c9…`) sur la version 1 (`65609405…`), au § 6 et au § 7 ; rien d'autre ne change. » Les deux empreintes sont exactes et complètes (celle de la contre-lecture est celle de son compagnon ; celle de la version 1 est celle de son compagnon). Les corrections sont bien aux § 6 et 7. **Inexactitude d'un détail** : « rien d'autre ne change » est démenti par le titre et le numéro « version 2 » de la ligne de statut, qui changent aussi. Elle est inoffensive mais sera lue par la mère au scellement.
*Correction 1 (incise)* : remplacer « au § 6 et au § 7 ; rien d'autre ne change. » par « au § 6 et au § 7 ; hors le numéro de version (titre, ligne de statut), rien d'autre ne change. »

## 4. Réserve 3 du § 9
Texte (additif v2, ligne 157) : « Le lieu de dépôt des sorties n'est fixé ni par le texte ni par l'additif 1 ; cet additif ne le fixe pas (§ 7, point 1, pour la seule contrainte connue). » Après B, le point 1 porte deux contraintes (pas d'`archives-reponses-modeles/`, pas de sortie sous le dossier du code) : « la seule contrainte connue » est devenu faux, et ce texte sera scellé. **Oui, une correction d'un mot avant le scellement** ; elle ne change aucune règle, elle met la phrase en accord avec le point 1.
*Correction 2* : remplacer « pour la seule contrainte connue » par « pour les deux contraintes connues ».

## Rien de gelé ne change ; aucun identifiant de modèle
Vérifié sur le différentiel : aucune racine, empreinte de code, commande, critère ou montant ne bouge.

Contre-lecteur, modèle S.
