# Vérification courte de la conception 2 (épreuves du devin), v2 — Opus 5.5 (v1)

- **Date** : 2026-11-22. **Vérificateur** : le contre-lecteur Opus 5.5 (`claude-opus-5-5`), auteur de la contre-lecture et de son erratum 1. Classe B : vérification des corrections par le même contre-lecteur.
- **Pièce vérifiée** : `docs/notes/chantiers-21-novembre-v1/conceptions-v2/conception-2-epreuves-du-devin-v2.md`. Son compagnon est vérifié (`sha256sum -c` : OK). Le portage est fait par `portage-conception-2-v2.py`.
- **Méthode** : un diff ligne à ligne entre la v1 (sans son en-tête) et la v2 (sans le sien), puis une recherche des renvois et des chiffres que les corrections touchent ailleurs. L'unicité de chaque ancien texte ci-dessous est vérifiée par programme dans la v2 : chacun y figure exactement une fois. La lecture de la table par `lire_cellules` du script de portage est essayée : elle donne huit corrections portables et aucun ajout.

## Verdict : conforme après corrections

Les 21 corrections portées sont dans la v2 mot pour mot, à leur place, et n'ont rien changé d'autre : le diff ne montre que l'en-tête et ces 21 lignes. Les constats 1 à 5, 7, 8 et 10 à 15 sont fermés.

Restent ouverts :
- Les constats 6, 9, 16, 17 et 18, ajouts non portés : portés ci-dessous.
- Trois effets de bord, trois lignes que les corrections laissent en désaccord :
  - la phrase « Témoins dans chaque course » de la conclusion, contre le test de mort 4 corrigé ;
  - la décision 2 (a), contre les constats 1 et 14 ;
  - le renvoi « question 14 de la section 7 » du constat 13, qui suppose la numérotation de l'ajout du constat 9.

## État des 18 constats

| Constat | État dans la v2 |
|---|---|
| 1 | Fermé (deux corrections). Effet de bord : la décision 2 (a) garde « 4 000 épisodes par devin » et « fuite de 0,056 retrouvée », qui est la taille d'un trait seul. Correction 1-c. |
| 2 | Fermé pour le test de mort 4. Effet de bord : la conclusion dit encore « Une fuite plantée à la taille minimale doit être retrouvée ». Correction 2-b. |
| 3, 4 (par l'erratum 1, 4-a à 4-c), 5, 7, 8, 10, 11, 12, 14, 15 | Fermés, sans effet de bord. Pour le constat 14, voir aussi 1-c. |
| 6 | La première correction (« Portée sur un modèle ») est portée. L'ajout aux conditions de la borne haute ne l'est pas. Correction 6-b. |
| 9 | Les canaris (garde artefact) sont portés. Les questions 13 à 16 de la section 7 ne le sont pas. Correction 9-b : les quatre questions sont réunies en une seule question 13, à quatre parties (a) à (d), parce que le format de portage n'admet que deux lignes. |
| 13 | Fermé. Effet de bord : le renvoi à la « question 14 » ne tient qu'avec la numérotation de la v1 de la contre-lecture. Correction 13-b, liée à 9-b. |
| 16 | Non porté. Correction 16-a. |
| 17 | Non porté. Correction 17-a. |
| 18 | Non porté. Correction 18-a. Dans le nouveau texte, les titres sont entre “ ” au lieu de « ». |

## Table des constats

| N° | Gravité | Lieu | Constat | Correction proposée (ancien texte → nouveau texte) |
|---|---|---|---|---|
| 6-b | important | § 5, « Quand cela vaut la peine » | Ajout du constat 6, non porté. | Ancien : « - le harnais passe son témoin. » Nouveau : « - le harnais passe son témoin. Ou bien le harnais rejoue déjà à graines identiques, auquel cas le couplage se joue d'emblée, comme garde de non-régression. » |
| 9-b | important | § 7, inventaire | Ajout du constat 9, non porté. | Ancien : « 12. Quels champs du journal sont privés ? Lesquels franchissent la frontière ? » Nouveau (deux lignes) : « 12. Quels champs du journal sont privés ? Lesquels franchissent la frontière ? » et « 13. Quatre canaux trouvés par l'inventaire du code. (a) Une garde, une limite de durée ou un arrêt de course lit-il un score, une pièce ou un verdict ? Le nombre d'épisodes ou de pas joués en dépend-il ? (b) Comment les lots sont-ils composés et remplis ? Un épisode audité, ou sa copie, partage-t-il un lot avec un épisode servi ? (c) Où sont publiées l'entropie racine et les clés de graine (manifeste, préenregistrement), et l'agent ou le devin peut-il les lire ? (d) Dans un épisode à plusieurs agents, que voit chaque agent des actions des autres, et l'un d'eux peut-il être audité ou aiguillé sans les autres ? » |
| 13-b | mineur | § 1, « Définition » | Renvoi recalé sur 9-b. | Ancien : « pour la question 14 de la section 7. » Nouveau : « pour la question 13 (b) de la section 7. » |
| 16-a | mineur | § 3, « Deux courses pour la pièce » | Ajout du constat 16, non porté. | Ancien : « - Une course au taux de service, parce que les canaux de charge dépendent du taux. » Nouveau (deux lignes) : « - Une course au taux de service, parce que les canaux de charge dépendent du taux. » et « - Pour la lecture substituée, de même, une course où S est tiré de sorte que chaque décision du harnais qui en dépend soit prise une fois sur deux (puissance), et une course où S suit la loi des lectures de témoins (régime de service). » |
| 17-a | mineur | § 4, « Le monde planté » | Ajout du constat 17, non porté. | Ancien : « Un harnais simulé sur processeur produit des épisodes à pas, avec texte synthétique, durées log-normales, relances, erreurs, rang et charge. » Nouveau : « Un harnais simulé sur processeur produit des épisodes à pas, avec texte synthétique, durées log-normales, relances, erreurs, rang et charge. Défauts, à sceller avec la pièce 4 : 8 pas par épisode ; texte de 200 mots tirés d'un lexique fermé de 2 000 mots, dont 20 marqueurs ; log-durée par pas normale (moyenne 0, écart type 1) ; relance avec probabilité 0,05 par épisode ; erreur avec probabilité 0,02 ; rang uniforme sur 1 à 10 ; charge normale centrée réduite. » |
| 18-a | mineur | « Antériorités connues » | Ajout du constat 18, non porté. | Ancien : « - Clopper et Pearson, 1934. » Nouveau (deux lignes) : « - Clopper et Pearson, 1934. » et « - Test de randomisation conditionnelle : Candès, Fan, Janson et Lv, 2018 ; à pli tenu à part : Tansey et al., 2022, “The Holdout Randomization Test for Feature Selection in Black Box Models”. Détection de fuite par test fixe contre aléatoire, qui réfute sans attester : Goodwill et al., 2011 ; par réseau appris : Moos, Wegener et Moradi, 2021, “DL-LA”. Rapportés, non vérifiés sur PDF. La statistique du devin n'a rien de propre. » |
| 2-b | important | Conclusion, « Témoins dans chaque course » | Effet de bord du constat 2 : la conclusion contredit le test de mort 4 corrigé. | Ancien : « Une fuite plantée à la taille minimale doit être retrouvée. » Nouveau : « Une fuite plantée, à une taille de puissance au moins 0,99 au budget joué, doit être retrouvée. » |
| 1-c | mineur | Décision 2, option (a) | Effet de bord des constats 1 et 14 : budget « par devin » et taille d'un trait seul. | Ancien : « - *(a) α = 0,05, 4 000 épisodes par devin, deux courses pour la pièce.* Avantage : fuite de 0,056 retrouvée. » Nouveau : « - *(a) α = 0,05, 4 000 épisodes par course, deux courses pour la pièce.* Avantage : fuite d'environ 0,08 retrouvée par la famille entière (0,056 pour un trait seul). » |

## Ce que je n'ai pas fait

- Je n'ai pas relu la v2 en entier pour y chercher des défauts nouveaux : j'ai vérifié le diff et les renvois que les corrections touchent.
- Je n'ai pas exécuté le script de portage sur cette table. J'en ai seulement appelé la fonction de lecture des cellules.
- Aucun commit, aucun appel réseau.
