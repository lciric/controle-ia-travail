# Contrôle du différentiel v2 → v3 de l'additif 2 (code) de la ligne 3 — v1

Pièce de travail (classe C), 2026-11-20. Contre-lecteur, modèle S, le même que pour les versions 1 et 2. Rien écrit dans le dépôt ni sous `/root/.claude/` ; aucun lancement du banc ; aucun refus d'outil.

## Verdict : **Conforme**

## Empreintes
Additif v3 (`f5562d20…`), fichier de remplacements, journal, différentiel, rapport du rédacteur : chacun égal à son compagnon. Additif v2 (`18650157…`) égal à son compagnon. Mon contrôle v1 → v2 porte l'empreinte `97f51ce83649aade410ca0c586e651caf853da6164e99cbc211824e0538ae6e3` (celle de mon compagnon), citée exactement par la phrase de version.

## 1. Rejeu de l'outil, à l'octet
`remplacer_texte_exact_v1.py` sur l'additif v2 avec le fichier de remplacements du rédacteur, sortie dans mon dossier : « FAIT : 4 remplacement(s) » ; empreinte de sortie `f5562d206bc56bfa1ebf2ff88abcdd6fcc93ececb6abd513d05611c6c4e5f25a`, **égale à celle de l'additif v3 du rédacteur**. Le différentiel (lu) montre trois lignes changées : titre (1), ligne de statut (3), réserve 3 du § 9 (157).

## 2. Mes deux corrections, à la lettre
- **Correction 1** : le texte neuf du remplacement 3 commence par « au § 6 et au § 7 ; hors le numéro de version (titre, ligne de statut), rien d'autre ne change. », mot pour mot ce que j'ai demandé ; il est suivi, sur la même ligne, de la phrase de version.
- **Correction 2** : « pour la seule contrainte connue » devient « pour les deux contraintes connues » (§ 9, réserve 3), mot pour mot.

## 3. Phrase de version (de la main du rédacteur)
« Version 3, même jour : elle porte à la lettre les corrections 1 et 2 du contrôle `controle-differentiel-additif-2-code-v1-v2-v1.md` (`97f51ce8…`) sur la version 2 (`18650157…`), à cette ligne de statut et au § 9 ; hors le numéro de version (titre, ligne de statut) et cette phrase, rien d'autre ne change. » Exacte : les deux empreintes sont celles des pièces nommées, les corrections touchent bien la ligne de statut (correction 1) et le § 9 (correction 2), et l'exception « et cette phrase » rend vrai le « rien d'autre ne change » (le différentiel ne montre aucune autre ligne changée). Je tiens ce choix de sa main pour bon : sans ces mots la phrase répéterait l'inexactitude levée par la correction 1. Aucune correction.

## 4. Rien d'autre ne change
Différentiel et rejeu à l'octet : aucune autre ligne ; ni racine, ni empreinte de code, ni commande, ni critère, ni montant ne bouge ; aucun identifiant de modèle.

Contre-lecteur, modèle S.
