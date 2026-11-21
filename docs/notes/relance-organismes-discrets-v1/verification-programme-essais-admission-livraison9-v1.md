# Vérification du programme des essais d'admission — livraison 9 (noms `_v8`, mutations v4) — v1

Contre-lecteur de code neuf (Claude Opus 5.5), qui n'a pas écrit ce code. Rien n'est scellé ici.

## Verdict

**Engageable pour Google**, sous les conditions de la section 6. Aucun défaut bloquant trouvé. La pièce de l'avenant 2 est exigée et contrôlée. Les valeurs de sa section 9 sont codées à la lettre. Les trois lignes courtes du registre passent toutes les gardes de départ, garde du registre comprise, contre le faux fournisseur. Les trois écarts déclarés ne bloquent pas.

## 1. Empreintes, essais, campagne de mutations

- Le chef, les relais, le faux fournisseur, les essais et le gabarit `_v8` concordent avec leurs compagnons `.sha256`. L'avenant 2 v3 concorde avec 9d4b8a08fbeec8568f03aafe5f882b0631cbd0fef501641f99303591d4d103e3.
- Les essais de `tests/test_chef_essais_admission_bras_a_v8.py`, lancés sans aucune clé dans l'environnement, donnent **236 réussis** (deux passes).
- La campagne de mutations v4, rejouée, donne **521 mutants, 521 tués**, 0 survivant, 0 erreur. Le nouveau contrôle de l'avenant 2 compte 52 mutants, tous tués ; le contrôle de la ligne du registre en compte 63, tous tués.

## 2. La pièce de l'avenant 2 (question 1)

J'ai écrit des essais jetables, dans le répertoire temporaire et hors du dépôt. J'y ai recopié à la main les valeurs de la section 9 de l'avenant, sans les tirer du chef. J'y ai pris à la lettre le constat de la section 3 de la note et les lignes de la section 4. Huit essais, huit réussis.

- Les trois lignes courtes, prises à la lettre dans la note puis remplies, font **551, 553 et 588 signes**. Les deux vérifications de clé et la file du juge des deux ancres passent par `gardes_avant_depart`, garde du registre comprise, sur une configuration définitive remplie. Pour chaque vérification, le seuil vaut 28,28 USD et le plafond de sortie 65 536. Pour la file, il faut deux relevés de vérification clos ; le régime est alors prudent et la dépense retirée vaut 4,71 USD. Le constat donne 32,97 USD de crédit compté pour chaque projet.
- Trois artefacts sont refusés :
  - une configuration définitive où l'avenant 2 manque ;
  - une ligne du registre dont on a retiré l'empreinte de l'avenant 2, refusée par la garde du registre ;
  - le constat lu après le 24 novembre 2026 à 00:01Z. Ce constat est encore admis à 00:00Z.
- La règle ne vaut que pour les lignes de Google. Une ligne de Mistral ne demande pas l'avenant 2, ce qui est conforme à la portée de l'avenant.

## 3. Les valeurs de la section 9 (question 2)

Les constantes du chef sont identiques, champ par champ, aux valeurs que j'ai recopiées de l'avenant :

- plafond de sortie 65 536 ;
- borne de réflexion 49 536, au niveau ;
- sonde exemptée sous GO-2026-11-21-69 ;
- seuils de 28,28 USD et 23,59 USD, crédit à avoir de 32,97 USD ;
- vérifications de clé : plafond 3,00 USD, excès possible d'un envoi 1,69 USD, délais 900/900/890/890 ;
- file : plafond 16,50 USD, excès possible 7,09 USD, délais 2700/2700/2690/2690 ;
- régime prudent.

Je n'ai trouvé aucune contradiction avec les livraisons précédentes. L'état « essai » du gabarit garde les valeurs de l'avenant 1, et la note le déclare.

La garde du plafond a été éprouvée au faux fournisseur, à 65 536 sous un plafond de 3,00 USD. Un envoi sans réponse au délai est compté entre 2,6 et 3,0 USD, et la ligne est à refaire. Au dossier suivant, aucun appel ne part et la ligne est close par la garde du plafond. C'est ce que demande l'item 6 de la section 9.

## 4. Les écarts déclarés (question 3)

- **(a) Ligne de taux de la section 7 refusée ; contrôles sur le fichier de la Banque centrale européenne non codés.** Cet écart ne bloque pas. La forme que le chef accepte est celle de la note, avec « fixage publié le », que la réserve 16 de l'avenant renvoie au programme qui fait foi. Ce qu'il faut : celui qui écrit le vrai constat vérifie l'empreinte du fichier quotidien de la Banque centrale européenne et la date du fixage sur le fichier lui-même, puisque le chef ne fait que recopier l'empreinte.
- **(b) Un modèle dont la fiche n'a pas de champ `outputTokenLimit` laisse partir l'envoi.** Cet écart est conforme à la ligne 2 de la section 4.4 du devis, qui ne refuse que ce qui est rendu et inférieur. Je l'ai éprouvé : les appels partent à 65 536 puis à 256, et le relevé est sain. Il ne bloque pas. Je recommande toutefois de refuser l'absence, côté prudent, par un mot de Lazar. Sans ce refus, si la limite réelle est plus basse, la ligne coûte un refus 400 compté et elle est close.
- **(c) Constat d'exemple non admis après le 24 novembre à 00:00Z.** C'est une condition d'exploitation et non un défaut ; l'essai la confirme. Les lignes de Google doivent partir avant cette heure. Sinon, il faut un constat neuf, sur un fixage frais.

Deux autres écarts sont déclarés et ne bloquent pas :

- L'échéance de GO-2026-11-21-69, au 22 novembre, n'est pas contrôlée pour l'exemption de la sonde (réserve 10 de l'avenant). Lazar doit le savoir.
- La garde du registre n'exige pas, pour chaque ligne, toutes les empreintes de la section 8. Elle exige l'avenant 2, le devis, sa vérification et l'avenant 1, ce que la réserve 15 permet.

## 5. La règle permanente sur les appels à Google (question 4)

La règle est tenue, à la lettre, à 65 536. Le corps porte la réflexion explicite au niveau XHIGH ; je l'ai vu au faux fournisseur. Le plafond vaut exactement 49 536 + 16 000 = 65 536. La limite de mots doit tenir dans 16 000 jetons de texte. Les défauts relevés après la réponse sont journalisés. L'essai du dépôt confirme qu'à 65 535 aucun appel payant ne part. Le texte de la règle sur la branche main ne fixe pas lui-même de nombre : 65 536 n'est que le cas limite qui la satisfait. La garde commune est reproduite dans le script, ce que la règle permet.

## 6. Conditions pour engager Google

1. Un constat réel de Google seul, à la forme de la note (section 3) : soldes d'au moins 31,58 € par projet, deux projets distincts relevés, fixage de la Banque centrale européenne vérifié sur le fichier, envoi dans le délai d'âge du fixage.
2. `jetons_par_mot` et `limite_de_mots` remplis par le lecteur habilité, avec la limite de mots × jetons par mot ≤ 16 000.
3. Les trois lignes de calcul écrites au registre de `origin/main` à la forme de la section 4, l'empreinte de l'avenant 2 comprise, chacune sous son GO.
4. Le fichier des interdits présent au chemin de la configuration ; il était absent à la livraison 8.
5. L'exemption de la sonde confirmée valide au jour du départ, au-delà de l'échéance de GO-69 (22 novembre), par un mot de Lazar.
6. Facultatif, recommandé : refuser l'absence de `outputTokenLimit`.

## Fichiers ouverts

- La note v8.
- L'avenant 2 v3, sections 4 à 10.
- Le gabarit v8.
- Les essais v8 et le faux fournisseur v8.
- Le chef v8, par import.
- `CLAUDE.md` de main, par `git show`.

Je n'ai rien ouvert sous un chemin interdit. Aucun réseau, aucune clé, aucun `GO_ID` fixé.
