# Protocole du rapport des idées de la course 1 (30 octobre 2026) — v1 (gelé avant toute lecture d'une fiche)

Session conv-audit (Claude), 3 novembre 2026, 10:44 UTC (`date -u`). Décision de Lazar : mot de 11:35 (heure de Paris), « recos aussi », sur l'option (a) « rapport de la course 1 au protocole Heimersheim sur une copie à l'octet de session-depot, lecteurs neufs, 0 USD d'appels » (R-1355). **Aucune fiche de la course 1 n'a été lue par conv-audit** : elles sont sous `donnees/course-1-tentative-2-v1` chez session-depot, en quarantaine (SD R-804, R-811, R-820, R-827). Ce qui n'est pas écrit ici suit le protocole Heimersheim v1 (`brouillons/ideation-heimersheim-v1/protocole-rapport-idees-v1.md`, `942b9324…`), sections 2 à 7.

## 1. Entrées (copie à l'octet par session-depot, liste vérifiée avant toute lecture)
- **Fiches** : les 29 fiches validées des deux passes des deux proposeurs (Fable 5.1, Argon), dans leur version de sortie.
- **Les 3 fiches en quarantaine** : servies seulement si session-depot écrit que la quarantaine tient à la forme (validation, format) ; si elle tient au contenu (sûreté), elles sont **comptées, jamais ouvertes**, et le rapport le dit.
- **La question servie à la course** (consigne et pièces, telles que le lanceur les a servies), pour le rattachement.
- **Exclus des lecteurs** : les sorties des trois juges (Opus 5.5, Argon, Kimi) et toute note de lecture de session-depot : rapportées à part par le directeur, avec leurs réserves (accord de rang 0,12 ; témoins plus courts que les fiches ; auto-préférence d'Argon ≈ 1,8 point sur 15), jamais utilisées pour garder ou écarter une idée. **Exclu de tout** : la sortie de la tentative 1 (Opus 4.8, mise à l'écart, jamais lue), et toute référence `donnees/bras-attaque*` ou `donnees/mode-tenu-a-l-ecart*`.
- Préparation par le directeur : contenus seuls, identifiants opaques dans un ordre permuté par `numpy.random.SeedSequence` (graine : entier des 16 premiers hexadécimaux de l'empreinte de la liste de copie), provenances (proposeur, passe) dans une clé hors de portée des lecteurs.

## 2. Un classement : P (le programme de contrôle)
Toutes les idées gardées qui portent sur le programme (hypothèses, phase 0, portes, moniteurs, attaques, organisme) ; le reste en annexe, non classé.

## 3. Étapes A à D, et contrôle (comme Heimersheim v1, sections 2 à 6, sauf ce qui suit)
- **A** : lecteur neuf ; normalisation, dédoublonnage par structure (les 12 paires de doublons signalées par les juges ne servent pas : le lecteur dédoublonne lui-même, puis le directeur compare), réfutation par source citée seulement, hors sujet en annexe.
- **B** : préparateur neuf ; deux témoins publiés (2024 à 2026) dans le domaine de la course (moniteurs de menaces diffuses, sondes sur activations, agrégation séquentielle, angles morts des moniteurs), **absents du corpus servi à la course et de ses pièces**, vérifiés en source primaire ; même forme, même noyau de champs servis, même permutation.
- **C** : moissonneur(s) neuf(s), comme Heimersheim (deux au-delà de 30 fiches).
- **D** : classeur neuf ; **trois critères gelés**, 0 à 3 : *originalité vérifiée* (ancres de Heimersheim) ; *testable en jours* sur Llama-3.1-8B-Instruct ou sur les banques du programme (ancres de Heimersheim) ; *sert le programme* — 0 : aucun lien ; 1 : cite une hypothèse ou un axe ; 2 : sert une hypothèse nommée (H1 à H9) ou un critère de la porte G0, avec sa mesure ; 3 : en fait une mesure neuve qu'aucun préenregistrement du programme ne fait. Les douze premières : paires dans les deux ordres, Bradley-Terry, cohérence 0,8.
- **Contrôle par les témoins** : comme Heimersheim, section 6.

## 4. Rapport pour Lazar
Comme Heimersheim, section 7, sans la règle du mentor ; « où elle entre » devient « quelle hypothèse ou quelle porte elle sert » ; plus une ligne par fiche classée : **devenue ou non une hypothèse, une expérience ou un préenregistrement du programme** (vérifié aux registres) ; à part : ce que les juges de la course en disaient, avec leurs réserves.
