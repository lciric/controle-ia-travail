# Table des corrections — plan « sabotage ou empreinte de l'adaptateur », brouillon 3 — v1

Écrite par le rédacteur (Claude Fable 5.2) le 19 novembre 2026 vers 17:25Z, pour la vérification par le même contre-lecteur (Claude Opus 5.5). Pièce de travail.

- Contre-lecture traitée : `contre-lecture-plan-sabotage-ou-empreinte-brouillon2-v1.md` (`29b866573ee07272a124ebf0645af33299d9a3bcdbd662812ef00940bedbe308`), outils lus en entier (simulation, arithmétique du devis, couples, journal).
- Pièces produites : le texte `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` (« texte »), `devis-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` (« devis »), `fiche-decisions-lazar-v3.md` (« fiche »), `simulation-puissance-adaptateurs-tenus-a-l-ecart-v4.py` (`632c048a…`) et sa sortie (`4279606e…`), `calcul-devis-adaptateurs-tenus-a-l-ecart-v3.py` (`9335ac98…`) et sa sortie (`1997a75a…`). Les empreintes du texte, du devis et de la fiche sont dans leurs compagnons `.sha256`.
- Méthode : les 35 couples ont été appliqués par programme, dans l'ordre, à partir de la liste `COUPLES` de `contre-lecture-outils-plan-brouillon2-v1/couples-avant-apres-v1.py`, chaque « avant » trouvé une fois ; puis la consigne de m-14 ; puis les écritures du rédacteur. La colonne « présent » dit si le texte « après » du couple se retrouve à l'octet dans la pièce finale (vérifié par programme à l'écriture de cette table).

## 1. Les 35 couples

| repère | classe | pièce | mode | « après » présent à l'octet | où |
|---|---|---|---|---|---|
| B-1a | bloquant | texte | appliqué à la lettre | oui | « Ce qui change par rapport au brouillon 1 », point 3 |
| B-1b | bloquant | texte | appliqué à la lettre | oui | « Hypothèse », « Pourquoi la conjonction… » ; une phrase du rédacteur ajoutée à la suite |
| B-1c | bloquant | texte | appliqué à la lettre | oui | « Hypothèse », table des rivales, ligne « force » |
| B-1d | bloquant | texte | appliqué à la lettre | oui | « Seuil », tiret « Le mot « sabotage » » |
| M-1a | majeur | texte | appliqué à la lettre | oui | « Ce que dira chaque issue », phrase S |
| M-2a | majeur | texte | appliqué à la lettre | oui | « Hypothèse », nulle de chaque épreuve |
| M-2b | majeur | texte | appliqué à la lettre | oui | phrase S |
| M-3a | majeur | texte | appliqué à la lettre | oui | « Seuil », « Famille de lectures » |
| M-4a | majeur | texte | appliqué à la lettre | oui | plan, point 11, monde V0 (colonne « vérité plantée ») |
| M-4b | majeur | texte | appliqué à la lettre | oui | plan, point 11, monde V3 |
| M-5a | majeur | texte | appliqué à la lettre | oui | « Liste d'arrêt », point 5 |
| M-5b | majeur | texte | appliqué à la lettre | oui | « Code neuf », premier paragraphe |
| M-6a | majeur | texte | appliqué à la lettre | oui | « Critères de lecture gelés », « Sous huit familles présentes » |
| M-7a | majeur | texte | **non appliqué dans la pièce finale** : appliqué, puis remplacé avec tout son paragraphe par la refonte de E2 (il n'y a plus de recherche de facteur) ; **à trancher par le contre-lecteur** | non | paragraphe supprimé par la refonte ; règles d'échec récrites : « Métrique », épreuve E2, « Règles d'échec » |
| M-8a | majeur | texte | appliqué à la lettre | oui | « Critères », diagnostic |
| M-8b | majeur | texte | appliqué à la lettre | oui | « Critères », diagnostic |
| M-8c | majeur | texte | appliqué à la lettre | oui | phrase « Diagnostic » |
| M-9a | majeur | fiche | appliqué à la lettre, puis un seul chiffre changé par le rédacteur (« 87 à 131 USD » devient « 86 à 128 USD », devis rechiffré) | non | fiche, décision 2 (a) |
| M-9b | majeur | fiche | appliqué à la lettre | oui | fiche, décision 2 (b) |
| M-9c | majeur | fiche | appliqué à la lettre | oui | fiche, sous le verdict |
| M-10a | majeur | texte | appliqué à la lettre | oui | « Ce qui peut faire échouer le calendrier » |
| m-1a | mineur | texte | appliqué à la lettre | oui | exposition, « Lecture incidente » |
| m-2a | mineur | texte | appliqué à la lettre | oui | plan, point 8 (a) |
| m-3a | mineur | texte | appliqué à la lettre | oui | calendrier, coupe 1 |
| m-4a | mineur | texte | appliqué à la lettre | oui | plan, point 2 |
| m-4b | mineur | texte | appliqué à la lettre | oui | plan, point 7 |
| m-5a | mineur | texte | appliqué à la lettre | oui | phrase NI |
| m-6a | mineur | texte | appliqué à la lettre | oui | plan, point 9 |
| m-7a | mineur | texte | appliqué à la lettre | oui | calendrier, ligne du mardi 24 |
| m-8a | mineur | devis | appliqué à la lettre | oui | devis, § 2, ligne « relecture et notation » (chiffres du brouillon 2 ; le § 3 rechiffré fait foi) |
| m-9a | mineur | devis | appliqué à la lettre | oui | devis, § 3, « Carte » |
| m-10a | mineur | devis | appliqué à la lettre | oui | devis, § 6 |
| m-12a | mineur | texte | appliqué à la lettre | oui | plan, point 7, l'ouvreur |
| m-12b | mineur | texte | appliqué à la lettre | oui | plan, point 7, la session de lecture |
| m-13a | mineur | texte | appliqué à la lettre | oui | « Puissance », après la table |

## 2. Les constats

| repère | classe | mode | où dans le brouillon 3 |
|---|---|---|---|
| B-1 | bloquant | écrit par le rédacteur (conception) ; couples B-1a à B-1d appliqués à la lettre | « Ce qui change au brouillon 3 » ; « Métrique », épreuve E2 (E2a, E2b, règles d'échec, limite déclarée) ; plan, points 8, 9, 10 ; « Puissance », « Refait pour la construction retenue » ; simulation v4, blocs N et O. Choix : la variante du contre-lecteur est gardée (E2b) et doublée d'une poussée égalée dans la famille (E2a), toutes deux après coup. Consigne 3 du constat : les trois mondes exigés donnent 0,0 à 0,1 % (au plus 0,5 % dans les 22 mondes sans sabotage, 44 cases de 1 000 mondes) |
| M-1 | majeur | appliqué à la lettre (M-1a) | phrase S ; la table des rivales garde la trace propre à son sens ouverte ; « Puissance » le redit (100 % dans ce monde) |
| M-2 | majeur | appliqué à la lettre (M-2a, M-2b) | « Hypothèse » ; phrase S |
| M-3 | majeur | appliqué à la lettre (M-3a, B-1d) | « Seuil » |
| M-4 | majeur | appliqué à la lettre (M-4a, M-4b), plus écrit par le rédacteur | plan, point 11 : règle V0 « sabotage dans 20 mondes au plus » avec sa raison ; paragraphe « Les mondes sont plantés au niveau des scores par jeton… » ; monde V8 ajouté |
| M-5 | majeur | appliqué à la lettre (M-5a, M-5b), plus écrit par le rédacteur | « Liste d'arrêt », 5 ; « Code neuf », premier paragraphe et dernier tiret de la liste des modules (trois enveloppes de formation) |
| M-6 | majeur | appliqué à la lettre (M-6a) ; complété | « Critères », « Sous huit familles » ; « Métrique », E2 : chaque demi-épreuve compte ses familles présentes |
| M-7 | majeur | écrit par le rédacteur (le couple M-7a visait la dichotomie, supprimée) | « Métrique », E2, « Règles d'échec » |
| M-8 | majeur | appliqué à la lettre (M-8a à M-8c) | « Critères », diagnostic ; phrase « Diagnostic » |
| M-9 | majeur | appliqué à la lettre (M-9a à M-9c) ; chiffres de coût mis à jour | fiche, verdict et décisions 2, 4, 6 |
| M-10 | majeur | appliqué à la lettre (M-10a), plus écrit par le rédacteur | « Calendrier » : « Sections figées pour le code de formation », « La chaîne voisine, comptée » ; « Calcul et dépense » ; devis, § 7 et § 6 |
| m-1 à m-7, m-12 | mineurs | appliqués à la lettre (couples du même nom) | voir § 1 |
| m-8, m-9, m-10 | mineurs | appliqués à la lettre ; la relecture est ensuite rechiffrée (calcul v3) | devis, en-tête, § 2, § 3, § 5, § 6, § 7 |
| m-11 | mineur | écrit par le rédacteur | « Marqueurs », M-6 : ce qui reste, par qui, et la conduite si le rapprochement échoue ou rend « autre règle » ; « Sections figées » le cite |
| m-13 | mineur | appliqué à la lettre (m-13a), plus écrit par le rédacteur | « Puissance » : chiffres du contre-lecteur gardés, puis ceux de la construction retenue |
| m-14 | mineur | appliqué à la lettre (consigne) | « Métrique », « Séparation apprise » : « 10 000 tirages, percentiles » |
| m-15 | mineur | écrit par le rédacteur | « Contre-lecture » : deux empreintes complètes de 64 signes. Non vérifié par moi contre le validateur `src/controle_ia/prereg.py`, que je n'ai pas ouvert |

## 3. Changements hors correction

1. Titre, date, statut et liste des documents de l'en-tête (brouillon 3, simulation v4, calcul v3).
2. « Ce que j'ai vérifié » : la phrase sur `fixer_dose` ne parle plus de multiplier les matrices B.
3. « Hypothèse » H-B5F et prédiction P4 : « à poussée égale » au lieu de « à norme de déplacement égale ».
4. « Seuil », audit de symétrie (iv) ; « Critères », descriptifs : les facteurs sont ceux de la construction neuve.
5. Phrase S : la proposition sur la force décrit les deux poussées égalées.
6. « Données gardées » : ≈ 141 Go au lieu de ≈ 184 Go (plus de série à norme égale) ; scores par jeton et produits sur la branche de lecture.
7. « Calendrier » : lignes du jeudi 19 et du vendredi 20 ; durée de la relecture ; « Jamais coupés » nomme l'épreuve à poussée égale et ajoute la sonde du diagnostic (remarque du § 6 de la contre-lecture).
8. « Code neuf » : `relecture_v1`, `sondes_v1`, `lecture_v1` récrits pour la construction neuve.
9. Plan, point 15, et « Puissance » : les chiffres du bloc L qui portaient sur l'épreuve E2 du brouillon 2 sont gardés et dits tels.
10. « Marqueurs » : M-8 dit fait ; M-9 ajouté.
11. Devis : coupures de la relecture (20) et de la répétition (8) ; volume de stockage de 200 Go.
12. Fiche : en-tête, ligne 1 du verdict, coûts, recharge, volume.

## 4. Ce que le rédacteur signale lui-même

- **Le « taux d'erreur » de 0,5 % est un maximum observé sur 44 cases de 1 000 mondes inventés**, non une borne ; il ne vaut que pour les formes de force écrites dans le texte (limite déclarée).
- **L'instrument de E2a suppose des divergences propres indépendantes d'un membre à l'autre** ; les membres d'une famille partagent graine et ordre : si leurs divergences sont corrélées autrement que par la part commune, le rapport q_k est biaisé. Non simulé.
- La puissance du mot pour une réponse saturée et huit familles n'est donnée que par le bloc N.
- **Incident** : pendant l'écriture de la simulation v4, le disque du conteneur s'est trouvé plein (occupé par d'autres travaux) ; une écriture a tronqué le fichier de simulation, non encore scellé ; je l'ai reconstruit, relu par analyse syntaxique, rejoué en entier, puis scellé. Aucune pièce scellée n'a été touchée ; rien n'a été effacé par moi.
- Une version en cours de la simulation v4 a été commise par une autre session avant son scellement ; la version scellée est celle de l'empreinte ci-dessus.
