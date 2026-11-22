# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v3` (empreinte du module 95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHQ7Qyrbxqp7AN8U7JEr`
- Heure (UTC) : 2026-11-22T05:22:29Z
- Réglages : effort `high`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 85000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/relance-organismes-discrets-v1/relecture-fable-avenant-3-v1/consigne-relecture-v1.md` — sha256 b5d40181b1828e85117708bc9c87332fb148e3c6210fb935a787a22f2c459c4f (compagnon : vérifié)
  - correction : `docs/notes/relance-organismes-discrets-v1/relecture-fable-avenant-3-v1/entrees/correction-avenant-3-v1.md` — sha256 00fcf3470f42e903bda8c071d633871b6f03b7d04702e277b828483f792d73a1 (compagnon : vérifié)
  - remarques : `docs/notes/relance-organismes-discrets-v1/relecture-fable-avenant-3-v1/entrees/remarques-decisions-go-2026-11-22-02-et-03.md` — sha256 0c7dd1d6de5c041afb56cb372a42714749e9e90da70cb6d0640302984a9119a1 (compagnon : vérifié)
  - avant : `docs/notes/relance-organismes-discrets-v1/relecture-fable-avenant-3-v1/entrees/avant-extrait-avenant-2-v3.md` — sha256 7f8e10d9ef121483eba0b63a75c6a10e8c65f8bc77c756983e40cf525ea46669 (compagnon : vérifié)
- Empreinte de l'invite envoyée : d09d34f1c6dd8b7ee4a524ab49f60f4edf6acfa3efc8c782d8d3c1ee3c826f12
- Jetons : entrée 36924, sortie 35236 (dont réflexion 31568), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.704832 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Relecture de l'avenant 3 v1

**Verdict : scellable après corrections.** Le fond est juste : la décision est bien traduite, la borne de perte tient, aucun chiffre n'est neuf. Les textes de la section 4 ne sont pas encore citables tels quels, et sept passages demandent une correction (liste en fin).

**Limites de ma relecture.**
- L'extrait ne porte pas les lignes 25 à 254.
- Je n'ai vu du registre que les deux lignes GO-02 et GO-03.
- Je n'ai rejoué aucun programme.
- La note dit l'avenant 2 v3 « accepté » ; sa ligne 9 dit encore « non acceptée », et aucune pièce reçue n'établit l'acceptation.

## 1. Fidélité à GO-02 et GO-03

1. Les citations des deux décisions sont exactes : mots du directeur, phrases, référence, échéance, « Confirme et remplace GO-2026-11-21-88. ».
2. « Seuils levés » est une traduction, non la lettre. GO-02 dit seulement « aucun versement de 9,18 € […] à faire » et « la recharge automatique […] couvre les lignes ». La conséquence est nécessaire aux soldes vus (ligne 277), mais les textes de la section 4 la placent « par décision du directeur (GO-2026-11-22-02) ». Le GO de chaque ligne la ratifiera ; je conseille de la faire confirmer avant.
3. « Aucun versement » généralise. Les 9,18 € sont le reste après le versement de GO-2026-11-21-74 (lignes 18 et 301). La note le reconnaît en section 3, mais écrit « tombe : aucun versement » au tableau.
4. Ajouts sans source dans les deux décisions :
   - le champ `seuils_de_credit_google`, ses deux valeurs et la lecture du registre (déclaré « forme proposée ») ;
   - le crédit vu « toujours lu et écrit » ;
   - « qui arrête la ligne » ou « la file », et « ni jugé ni compté », calqué sur la ligne 339 : GO-02 s'arrête à « jamais une réponse » ;
   - la valeur neuve de `exemption_de_la_sonde_go` et la parenthèse ajoutée aux lignes 2 et 6 : GO-03 ne nomme ni champ ni texte, c'est plus qu'un acte, mais une conséquence légitime ;
   - « Le risque est une ligne perdue, non une lecture fausse », jugement du rédacteur.
5. GO-2026-11-21-88 n'est lu par personne. L'avenant 2 v3 porte GO-2026-11-21-69 au champ, et le lien entre 69 et 88 n'est établi par aucune pièce reçue.

## 2. Citations et numéros de ligne

6. Exactes, à la lettre et à la bonne ligne : 16, 17, 18, 23, 263 et 264, 267, 277, 286 et 288, 294, 296, 409 et 411, 413, 427, 442, 446, 459, 460, 471, 484, 493 ; section 3.4 aux lignes 304 à 310.
7. Non vérifiables sur l'extrait : lignes 253, 212, 216, 217, tableaux 1.2 et 1.3, listes de 1.4. Elles sont à confronter sur le fichier entier, ou à accepter sur la foi de `verif_av3.py`.
8. « Tombe en entier » (section 3.3) est inexact : la section 2 de la note reprend ses manques, et la ligne 301 porte le versement de GO-74, dont GO-02 ne dit rien.
9. Trois lignes de l'extrait manquent à la liste :
   - 403 : « Le manque de la section 3 se refait alors au taux neuf. » ;
   - 383 : valeur du champ de l'exemption ;
   - 448 : dépense retirée, sans effet sous `"leves"`.

## 3. Borne de la perte et risque

10. La borne est juste. 4,69 + 4,69 + 23,59 = 32,97 USD ; le régime prudent est à la ligne 447 ; `recharge_comptee` reste `false` (ligne 446). Les seuils dérivaient du compteur et ne bornaient rien (lignes 267 et 409).
11. Le « En bref » dit la perte « bornée » sans rappeler les suppositions.
12. Les trois points sur le risque sont honnêtes pour l'essentiel, avec deux manques :
    - Les 9,18 €, 19,65 € et 15,99 € bornent ce que les lignes consomment au-delà du solde, non ce que la recharge paie : son montant « n'est pas relevé » (ligne 427).
    - « Non une lecture fausse » ne vaut que si le programme reconnaît le refus, dont la forme est inconnue.

## 4. Ce que le programme doit faire

13. Les trois gardes sont exactes. Le champ échoue fermé : valeur hors liste, champ absent ou ligne introuvable, rien ne part.
14. Elles ne suffisent pas. Il manque :
    - **La garde 8 et le champ `avenant`** : les textes neufs et l'empreinte de l'avenant 3 doivent être lus par elle (lignes 467 et 470).
    - **L'articulation avec le code 429 et la reprise unique** (ligne 345) : si le refus prend une forme déjà traitée autrement, la garde ne le voit pas.
    - **Ce que « lire la ligne » contrôle** : identifiant seul, auteur, échéance.
    - **Deux épreuves** : `"leves"` avec un solde sous les seuils (la ligne part, le crédit est écrit) ; `"appliques"` refuse toujours (ligne 471).
    - **Le cas du solde illisible** : dire qu'une pièce de constat absente ou illisible refuse encore.

## 5. Textes des lignes de calcul

15. Relus segment par segment contre les lignes 409, 411 et 413 : hors la parenthèse de GO-03 et la fin, je ne trouve aucun écart. C'est une lecture, non une comparaison octet par octet.
16. Ils ne sont pas citables tels quels :
    - « jamais une réponse, qui arrête la ligne » rattache la relative à « réponse » (quatre occurrences, geste de paiement compris) ;
    - la garde 8 n'est pas rejouée, alors que l'avenant 2 l'avait éprouvée (ligne 407).
17. Après correction : refaire les remplacements par programme et recalculer les empreintes. La réserve des 600 signes (ligne 499) est héritée.

## 6. Points laissés à trancher

18. **Forme du refus : non bloquant pour le scellement.** GO-02 la renvoie lui-même au premier appel. Mais ce premier appel ne la montrera que s'il est refusé ; l'artefact de l'épreuve est donc supposé, et il faut le dire.
19. **Échéance du 30 novembre : non bloquant.** Elle est à trancher avant de coder le champ. Je conseille de la contrôler, puisque la garde lit déjà la ligne : rien ne part après elle. Celle de GO-03 ne l'est pas : le chef ne contrôle que la forme (ligne 494).
20. **La note en laisse un troisième, le versement de GO-74 : non bloquant.** C'est un paiement, qui reste au directeur.

## Corrections, mot à mot

- **A. En bref.** Remplacer « comme avant. La fin du texte des lignes de calcul 2, 6 et 4 change. » par « comme avant, sous les mêmes suppositions, non mesurées (section 2). Changent : la fin du texte des lignes de calcul 2, 6 et 4, la parenthèse de l'exemption aux lignes 2 et 6, le geste de paiement. »
- **B. Tableau, ligne 18.** Remplacer « tombe : aucun versement ; la recharge automatique couvre les lignes » par « tombe : « aucun versement de 9,18 € par projet Google à faire » ; la recharge automatique couvre les lignes ; le versement de GO-2026-11-21-74 n'est plus exigé par aucun seuil, et la décision n'en dit rien ».
- **C. Tableau, lignes 279 à 302.** Remplacer « tombe en entier, recommandation comprise : » par « tombe comme exigence, recommandation comprise ; ses manques restent une mesure (section 2), et le versement de la ligne 301 un fait : ».
- **D. Section 1 et section 3.**
  - Après « (ligne 493). », ajouter « « Le manque de la section 3 se refait alors au taux neuf. » (ligne 403). »
  - En section 3, point 4, remplacer « (lignes 442 et 459) » par « (lignes 383, 442 et 459) ».
- **E. Section 2.**
  - Au point 1, après « (lignes 286 et 288). », ajouter « Ces chiffres bornent ce que les lignes consomment au-delà du solde vu, non ce que la recharge paie : son montant n'est pas relevé. »
  - Au point 3, remplacer « Le risque est une ligne perdue, non une lecture fausse. » par « Le risque est une ligne perdue, avec ce qu'elle a déjà dépensé, non une lecture fausse, si le programme reconnaît le refus, dont la forme n'est pas relevée. »
- **F. Section 3.**
  - Ajouter un point 5 : « **Garde 8** : les textes de la section 4 et l'empreinte de cet avenant sont à lui faire lire, et l'épreuve à rejouer, avant qu'une ligne soit accordée (avenant 2 v3, lignes 467 et 470). »
  - Aux épreuves, ajouter « ; `"leves"` avec un solde sous les seuils : la ligne part et le crédit vu est écrit ; l'artefact du refus est de forme supposée ».
  - Au paragraphe « Non dit », après « au premier appel » », ajouter « , qui ne la montrera que s'il est refusé ; l'articulation de ce défaut avec l'attente sur un code 429 et la reprise unique (ligne 345) ».
- **G. Section 4, quatre occurrences.** Remplacer « jamais une réponse, qui arrête la ligne » par « jamais une réponse : il arrête la ligne », et « jamais une réponse, qui arrête la file » par « jamais une réponse : il arrête la file ».
