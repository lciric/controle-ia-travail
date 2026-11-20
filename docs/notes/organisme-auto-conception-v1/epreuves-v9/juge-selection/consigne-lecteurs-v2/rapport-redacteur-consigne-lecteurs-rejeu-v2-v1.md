# Rapport du rédacteur — consigne des lecteurs du rejeu, version 2 — v1

- **Pièce de travail (classe C).** Écrit le 2026-11-20 (`date -u` de la v2 : 2026-11-20T05:26:28Z) par un rédacteur neuf, modèle F, sur le mandat `mandat-redacteur-consigne-lecteurs-rejeu-v2-v1.md` (sha256 `c2956c4e629eb67b896734c9dc613c2dd8155943132cb6b1757a1f3ef00c1f0d`, égal à son compagnon). Processeur seul, aucune dépense, aucun appel de modèle. Aucune carte ouverte. Rien n'est écrit dans le dépôt.
- Dossier des pièces rendues (noté D) : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-consigne-lecteurs-rejeu-v2/`.

## Verdict

**La v2 est écrite : onze remplacements exacts, tous passés par l'outil contre-lu, aucun refus.** Huit portent K1 à K4 à la lettre de la contre-lecture (§ 8) ; trois sont de tenue (titre, ligne de version, deux phrases demandées par le mandat). Deux de ces phrases sont de ma rédaction : elles sont à contre-lire (§ 3 ci-dessous).

## 1. Pièces rendues, chacune avec son compagnon

| pièce | sha256 |
|---|---|
| `D/consigne-lecteurs-rejeu-criteres-v7-v2.md` | `1e5479bea761dce96ae60e4c93f7991965134c262e3db6ae5a2b66622cc2aa70` |
| `D/remplacements-consigne-lecteurs-rejeu-v1-vers-v2-v1.json` | `aed5a51a144a4ed032b93209c67540c2e5c18df5b1e7b264d4cd175115296f52` |
| `D/consigne-lecteurs-rejeu-criteres-v7-v2.md.journal-remplacements-v1.json` | `a96a7a2b9518b3bbcc5f06e955a268bc18b449b4bc1898e29e951ed53d623808` |
| `D/differentiel-consigne-lecteurs-rejeu-v1-vers-v2-v1.diff` | `f2c3262626024cf8a690ba123766a35932f4244a0bccf6c79b414f63c24a1576` |

Cible : la v1, `bf49bd50b699ebc51a00b57154453fdafd708985d8c74e8d079ad384d0e1cb72`, égale à son compagnon, non modifiée. Outil : `scripts/remplacer_texte_exact_v1.py`, `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6`.

## 2. Les onze remplacements

| n° | objet | lieu de la v1 | source du texte neuf |
|---|---|---|---|
| 1 | titre « — v1 » devenu « — v2 » | l. 1 | tenue (mandat) |
| 2 | ligne « Version 2 » ajoutée sous la première ligne d'en-tête | après l. 3 | tenue (mandat) ; ma rédaction |
| 3 | nombre de cartes : 94, `hors_choix` vide | § 1, point 4 | mandat et confirmation X6 ; ma rédaction |
| 4 | K4 : compagnon de la note de dépôt | § 2, point 3 | contre-lecture, à la lettre |
| 5 | K1 : limite en tête de la déclaration | § 3.2, citation | contre-lecture, à la lettre |
| 6 | K1 : phrase qui suit la citation | § 3.2 | contre-lecture, à la lettre |
| 7 | K1 : limite en tête de `independance` | § 3.4, gabarit | contre-lecture, à la lettre |
| 8 | garde : une valeur hors des six chaînes sera refusée | § 4, premier point | décision de la mère ; ma rédaction |
| 9 | K2 : compter les cartes où l'étiquette tient lieu de famille | § 4 | contre-lecture, à la lettre |
| 10 | K3 : point « Suivre ou corriger un signal rapporté » | § 8, après « Régler tes réponses sur un résultat » | contre-lecture, à la lettre |
| 11 | K2 : ligne ajoutée aux écarts | § 9, point 5 | contre-lecture, à la lettre |

Contrôles faits :
- chaque ancre comptée par `grep -c -F -e` sur la v1 avant l'appel : une fois chacune ;
- les sept textes neufs de K1 à K4 retrouvés lettre pour lettre dans la contre-lecture, par `grep -c -F -e` ;
- le différentiel relu en entier : il ne porte que ces onze changements ; le point 1 du § 9 (limite en première ligne de la note de dépôt) est inchangé, comme K1 le veut.

## 3. Ce qui est de ma rédaction, à contre-lire

Le mandat demandait ces phrases sans en donner le texte.

1. **Ligne « Version 2 »** (en-tête). Elle nomme le mandat, la contre-lecture et la v1, avec leurs empreintes.
2. **§ 1, point 4** : « donné par la mère : 94 ; la liste des cartes hors du choix (`hors_choix`) est vide. » La v1 parlait du nombre attendu sans le chiffrer ; le mandat dit que, si elle en parle, elle le dit ainsi. Le chiffre vient de la confirmation X6 (`040b83a1…`), non d'une pièce que j'ai vérifiée moi-même : je n'ai ouvert ni le fichier des cartes ni le manifeste.
3. **§ 4, premier point** : « La mère contrôle ce champ par un programme de garde à part, joué avant l'assemblage : une valeur hors des six chaînes y sera refusée. »

## 4. Réserves

- **La phrase de garde décrit une pièce que je n'ai pas vue.** Je ne sais pas si le programme de garde est écrit, essayé et scellé. Si la consigne est remise aux lecteurs avant que la garde existe, la phrase est fausse.
- **Le premier point du § 4 se lit en deux temps.** Les phrases de la v1 y restent : « une faute que le programme ne voit pas », « chacune passerait, et serait comptée en silence ». Elles sont vraies du programme d'assemblage ; la phrase ajoutée dit que la garde, elle, refuse. Je ne les ai pas réécrites, le mandat interdisant toute autre modification. Un contre-lecteur peut juger que le point demande une réécriture.
- **L'en-tête garde « À contre-lire par un autre modèle avant d'être remise aux lecteurs »** (phrase de la v1, inchangée). Elle vaut aussi pour la v2, qui n'est pas contre-lue.
- **L'amorçage par le signal du rejeu v2** (contre-lecture, § 7) : K3 le dit au lecteur, il ne l'ôte pas. La réserve reste à porter dans la proposition.

## 5. Lu, et incidents

- Lus en entier : le mandat, la consigne v1, la contre-lecture, la confirmation X6, l'outil de remplacement. Empreintes de la consigne, de son rapport, de la contre-lecture et de la confirmation égales à leurs compagnons. Le rapport du rédacteur de la v1 n'a pas été ouvert : son empreinte seule a été vérifiée.
- Aucune carte, aucun fichier de cartes ni de sélection, rien sous `archives-reponses-modeles/` ni sous `/root/.claude/`. Aucune commande de liste, une commande simple par appel, aucun code en ligne.
- **Aucun refus** de permission, de classifieur ni de garde. Aucun refus de l'outil.

*rédacteur neuf, modèle F*
