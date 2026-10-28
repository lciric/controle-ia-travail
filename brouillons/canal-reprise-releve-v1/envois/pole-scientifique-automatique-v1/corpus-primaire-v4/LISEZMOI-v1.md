# LISEZMOI — corpus primaire v4

Date : 29 octobre 2026. Produit par un sous-agent de la lignée de contrôle des conversations (lignée « conv-audit »), sur instruction de l'instance parente. Il complète `../corpus-primaire-v1/` (dix extraits), `../corpus-primaire-v2/` (huit) et `../corpus-primaire-v3/` (quatre) sans les modifier : mêmes règles, mêmes conventions, un papier nouveau, absent de tous les rapports d'antériorité, plus une lecture de ce papier contre la question Q2.

## 1. Ce que c'est

Un extrait de texte, scellé, du papier PACE (arXiv 2606.08106v1), à servir aux proposeurs et aux juges de la course d'idéation en plus des rapports d'antériorité, et une lecture scellée de ce papier contre la revendication de Q2 (« juge figé garanti »). L'extrait garde, dans l'ordre : le titre, l'auteur, l'année, l'identifiant, le chemin canonique et l'empreinte du PDF, le résumé, la contribution méthodologique, la méthode, la garantie, les expériences, les limites ; le numéro de page du PDF figure en `[p.N]` au début de chaque passage. La bibliographie (sauf cinq références utiles à Q2), l'introduction, la section 5.4, la conclusion, les tableaux 4 et 5 et la figure 2 sont coupés, chaque coupe étant marquée `[COUPÉ]` à sa place.

Un extrait n'est pas une vérification : tout chiffre repris dans un préenregistrement ou un papier doit citer la page `[p.N]` et être relu sur le PDF empreinté (R7). Les notes entre crochets sont de la main de l'instance et ne contiennent aucun chiffre retapé à la main.

Chemin canonique du PDF : `docs/sources/pdf/2606.08106v1.pdf` (branche main, non lue par cette instance). L'instance a travaillé sur la copie fournie par l'instance parente, dont l'empreinte SHA-256 `779f49607688fd06226d4390ad6e0c4c8356ef75b87243fd734181cef700934f` a été comparée à celle du compagnon `.sha256` fourni : elles concordent.

## 2. Papier extrait

| Identifiant (version du PDF) | Titre (PDF) | Auteur ; année | Rôle | Pages gardées | Caractères |
|---|---|---|---|---|---|
| arXiv:2606.08106v1 | PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents | « ZayxShawn » (chercheur indépendant) ; 2026 (cachet du 6 juin) | Porte de validation des modifications d'un agent auto-évolutif : comparaison appariée candidat contre titulaire, e-processus de pari, seuil 1/α, probabilité de fausse validation bornée par candidat (non sur l'exécution entière) ; expériences sur des agents Qwen2.5 de 0,5 à 3 milliards de paramètres | 1-9 (en partie), 10 (cinq références) | 24601 |

Fichiers servis : `extrait-2606.08106-v1.md` (24601 caractères ; 25092 octets en UTF-8 à cause des accents) et `lecture-PACE-contre-Q2-v1.md` (au plus 2 500 mots : 2470 selon `wc -w`, balises de mise en forme comprises).

## 3. Lecture de PACE contre Q2 (résumé ; le détail est dans `lecture-PACE-contre-Q2-v1.md`)

- Verdict : Q2 reste **semi-occupée**, confiance moyenne ; la zone occupée s'élargit.
- Occupées par PACE : e-processus de pari, garantie statistique par candidat valable à tout instant, borne par candidat sur les fausses validations, jeu d'audit neuf, comparaison « acceptation gloutonne » contre porte (régime « validation en distribution » sur un jouet).
- Libres contre PACE : borne composée sur toute la boucle (PACE la déclare absente, p.5, p.9 ; le corpus v2 la situe dans 2609.17560), validité sous juge adversarial, tout juge-modèle (PACE utilise la correspondance exacte, p.6), moniteurs de sécurité et familles d'attaque tenues à l'écart, nulles de bibliothèque injectées (PACE a un gain connu planté et un régime sans gain, p.6), mesure des trois régimes de juge.
- Correction proposée : une v2 du rapport Q2 (huit points, section 6 de la lecture) ; le verdict ne change pas.

## 4. Commande d'extraction et méthode

Texte du PDF page par page : `pdftotext -layout -f N -l N FICHIER.pdf FICHIER.txt` (poppler) pour que `[p.N]` soit la vraie page du PDF ; le papier est en une seule colonne. Assemblage : lignes rejointes en paragraphes (un paragraphe finit où le texte de la page a une ligne vide) ; coupures de mots en fin de ligne recollées si le mot recomposé existe ailleurs dans le PDF, sinon le trait d'union est gardé (un cas dans l'extrait : « de-cisive », p.1) ; coupes par ancres textuelles (jamais de reformulation) ; chaque coupe est marquée `[COUPÉ]` à sa place. Un seul texte a été supprimé sans note de coupe : le cachet latéral arXiv de la page 1, inséré par la couche de texte au milieu du résumé. Une note de la main de l'instance (p.4) signale que la racine carrée de « 1/√n » est déplacée par l'extraction ; le texte extrait est gardé tel quel. Les tableaux 1, 2 et 3 sont en mode mise en page, colonnes séparées par « | » ; pour le tableau 3, les cellules coupées en fin de ligne sont rejointes ; la grille est approximative (en cas de doute, se reporter à la page citée). Les cinq références gardées sont prises en mode brut (`pdftotext -raw`), dont les retours à la ligne sont rejoints. Les scripts d'assemblage sont restés dans le dossier temporaire de la session et ne sont pas livrés.

Contrôle de fidélité fait avant le scellement, sur le fichier final : 742 fenêtres de 40 caractères (espaces et traits d'union ignorés ; une fenêtre tous les 20 caractères de chaque paragraphe), prises hors tableaux et notes, cherchées dans le texte de la page citée seule (modes mise en page et brut) : 742 retrouvées, 0 non retrouvée.

## 5. Retraits de sûreté (niveau méthode seulement)

Règle appliquée : seulement la classe d'attaque et le protocole d'évaluation ; jamais de recette ni de consigne d'attaque. PACE ne décrit aucune attaque : un agent propose des modifications de son invite, un test statistique les accepte ou les refuse, et les tâches sont des problèmes de mathématiques et de sciences. **Aucun retrait de sûreté.** Les coupes de l'extrait sont toutes faites par économie de place. Une recherche de motifs de commandes d'attaque sur l'extrait ne trouve aucune ligne ; la commande exacte est en section 7.

## 6. Réserves

Chaque point est vérifié sur le texte de la page citée du PDF de PACE.

- PACE est une préimpression d'un seul auteur indépendant, sans lieu de publication ni dépôt de code cité (pages 1-12) ; « first explicit treatment » est une revendication de l'auteur (p.2), non vérifiée.
- Le lien « PACE est cité par 2609.17560, p.5 et p.31, et manque de certificat à zéro étiquette » vient de `../corpus-primaire-v2/LISEZMOI-v1.md` ; il n'a pas été relu sur le PDF de 2609.17560 par cette instance.
- Le texte de PACE donne, pour la correction en ligne du taux de fausses découvertes, des valeurs (« +0,000 » à α = 0,01 ; « +0,41 » à n = 20, p.8) qui ne figurent dans aucun tableau du PDF : le tableau 4 (p.12) n'a que les colonnes « glouton » et « PACE ». À relire avant toute citation.
- Nombre d'exécutions incohérent dans le papier : « averages over 5 seeds » (p.6), mais 3 graines aux tableaux 2, 4 et 5 (p.7, p.12) et « 3–5 seeds » au tableau 3 (p.9).
- La garantie est par candidat ; le papier dit lui-même qu'elle n'est pas une borne de famille sur l'exécution entière et que la réutilisation adaptative du jeu est traitée « comme une affaire empirique » (p.5). Le jeu de développement fait 40 problèmes (p.6).
- L'étiquette « fausse validation » de l'audit (changement audité ≤ 0, p.6) n'est pas l'événement que borne α ; le test apparié à taille fixe égale la porte au tableau 1 (p.7) : l'avantage de la validité à tout instant repose sur très peu d'événements.
- Dans le régime stochastique, la porte valide 0,3 changement par exécution à 0,5 et à 1,5 milliard de paramètres, étiquetés faux à 33 % (tableau 2, p.7) ; le résumé écrit « commits almost nothing » (p.1).
- Les tableaux 4 et 5 et la section 5.4 (généralisation à SVAMP et ARC-Challenge) ne sont pas dans l'extrait ; lus sur le PDF, non vérifiés chiffre par chiffre.
- Les formules (équations 1 et 2, garantie p.5) sont en texte linéaire, parfois sans parenthèses ; se reporter à la page.
- Les verdicts « libre » de la lecture sont des inférences par absence dans un seul papier (R8), non des constats sur le champ ; le verdict de la lecture est une lecture de sous-agent, non un verdict de porte.

## 7. Contrôle avant scellement (règle R5)

- Taille : `python3 -c "print(len(open(f,encoding='utf-8').read()))"` sur l'extrait : 24601, soit au plus 25 000 caractères. Lecture : `wc -w` = 2470, au plus 2 500.
- Recherche (`grep -nE`) des trois motifs de clé d'accès fixés par le brief dans tous les fichiers `.md` du dossier (motifs non recopiés ici, pour que la recherche reste vide) : aucune ligne trouvée (code de sortie 1).
- Recherche de motifs de commandes d'attaque (`grep -n -i -E 'curl |wget |/etc/|sudo |base64|rm -rf|ignore (all )?previous|ignore the above'`) sur l'extrait : aucune ligne trouvée.
- `sha256sum -c *.sha256` dans ce dossier : tous OK (résultat repris dans la réponse de l'instance, la liste finale incluant l'empreinte de ce fichier).
- Empreinte du PDF vérifiée avant toute lecture : `sha256sum -c 2606.08106v1.pdf.sha256` : OK.
- Aucune lecture sous `donnees/`, aucun accès au réseau, aucune clé lue, aucune instance payante, aucun fichier existant modifié (les seuls fichiers écrits sont ceux de ce dossier), aucune récupération de branche.

## 8. Fichiers du dossier

- `extrait-2606.08106-v1.md` et son empreinte `.sha256` ;
- `lecture-PACE-contre-Q2-v1.md` et son empreinte `.sha256` ;
- ce fichier et son empreinte.
