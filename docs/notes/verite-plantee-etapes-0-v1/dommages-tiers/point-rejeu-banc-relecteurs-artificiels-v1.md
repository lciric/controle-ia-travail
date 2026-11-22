# Point : rejouer la règle de lecture de la campagne sur les erreurs injectées publiées du banc des relecteurs artificiels (v1)

- **Date** : 21 novembre 2026. **Auteur** : Claude Fable 5.2, concepteur neuf (R-3735). Pièce de travail. **Rien n'est téléchargé, aucune page en ligne n'est ouverte** : tout ce qui suit vient du PDF déjà au dépôt, relu ce jour par extraction de texte aux pages dites (rang dans le fichier).
- **Source** : Zubeldia, Bolliet, Villaescusa-Navarro, Villanueva-Domingo, Cranmer, « Auditing AI peer reviewers: a benchmark on real scientific papers », arXiv 2611.17052 v1 ; `docs/sources/pdf/couverture-de-l-oracle-v1/2611.17052v1.pdf` (`eb2bee890a619aaa8240c515d8b19e316ba3e69a57b325e3900a126d83a29800`, empreinte recalculée ce jour, égale au compagnon).

## 1. Le nom exact du jeu

L'article ne donne pas de nom propre au jeu de données. Il nomme son système de relecture (« Skepthical ») et écrit, p. 2 : « We release the evaluation pipeline, together with the paper lists, injection catalogues, and full adjudication logs, as a public benchmark at github.com/inigozubeldia/skepthical-benchmark. » La désignation exacte à employer est donc : **le dépôt public `inigozubeldia/skepthical-benchmark`, dans l'état de sa révision à la date du téléchargement** (identifiant de révision à consigner), accompagnant arXiv 2611.17052 v1. Je n'ai pas ouvert ce dépôt : je ne sais ni s'il existe à cette adresse aujourd'hui, ni ce qu'il contient au-delà de ce que la page 2 annonce.

## 2. Ce que le PDF établit de sa forme (p. 4, section 2.3 et début de 2.4)

- Par corpus, 15 articles ; par article, quatre versions : une copie propre, « used to assess false positives », et trois copies injectées, chacune portant une erreur de chacun de quatre types (questions générales, mathématiques, numérique, citations) à une gravité (S1 subtile, S2 claire, S3 flagrante) ; chaque couple de type et de gravité paraît une fois par article.
- Deux corpus : 177 erreurs injectées pour l'un (un article n'admet pas d'injection de mathématiques), 180 pour l'autre.
- L'injection est faite par un modèle (un par corpus, de deux lignées différentes) et n'est acceptée que si un valideur mécanique la confirme ; sinon elle est retentée.
- La détection est arbitrée par un panel de trois juges de trois lignées, à la majorité.
- Les gravités sont « calibrated within each error type but not across them », et la taxonomie « may not fully reflect the distribution of naturally occurring errors ».

**La correspondance avec notre règle** : douze strates (type et gravité) ; un plant par article et par strate, donc l'article est l'unité d'indépendance, comme notre tâche ; 15 plants par strate et par corpus (14 pour les trois strates de mathématiques d'un corpus) ; 15 copies propres par corpus pour la fausse alerte ; deux injecteurs de deux lignées, donc le témoin « deux planteurs, une strate ». Le système relu tient la place de notre oracle.

## 3. Ce que le rejeu ferait, et ce qu'il écrirait au mieux

Par système relu et par corpus : le compte de détections par strate ; la borne basse exacte à 1,25 % ; le minimum sur les douze strates, jamais une moyenne ; la lisibilité sur les copies propres ; la comparaison des deux corpus par strate ; la séquence fixe des gravités dans chaque type. Effectifs [calcul, H] : 15 plants sans manque bornent à 0,7467, 14 à 0,7312 ; avec un manque, 0,6435 et 0,6227 ; les deux corpus réunis (30), 0,8641. Sur 15 copies propres, le seuil de lisibilité ne tolère aucune copie signalée à tort (borne haute 0,1810 ; avec une, 0,2794).

**Ce que le rejeu éprouve** : notre programme de dépouillement sur des données réelles qu'il n'a pas produites, avec une vérité d'injection extérieure à nous ; et la sévérité de notre seuil de lisibilité sur de vrais relecteurs. **Ce qu'il n'éprouve pas** : notre oracle, nos plants, l'aveugle (là-bas l'injection n'est engagée par aucun scellé contre les bâtisseurs des systèmes), le placebo (il n'y en a pas), la part rejetée (elle n'y figure que si les journaux gardent les injections refusées par le valideur). Un point de forme à trancher avant de lire : la fausse alerte y est une liste de remarques par copie propre, non un signalement binaire par copie ; la règle « une copie propre est signalée si elle porte au moins une fausse remarque arbitrée » se fixe avant d'ouvrir les journaux.

## 4. La licence : ce qui est établi, et ce qu'il faut vérifier

**Établi sur PDF (annexe M.3, « Assets and licences », p. 30 et 31).** Cette annexe donne les licences des outils et des modèles que les auteurs emploient, et dit des deux corpus : « arXiv preprints used for research purposes only, with each paper credited individually in Appendix B; the papers themselves are not redistributed, and the release identifies them by their arXiv identifiers. » **Je n'y ai trouvé aucune licence du dépôt lui-même** (programmes, catalogues d'injections, journaux d'arbitrage).

**À vérifier, avant tout téléchargement** (décision de Lazar sur les ressources publiques, N-061 : licences vérifiées, rien dans la liste scellée de la porte G1 sans nœud à part) :
1. que le dépôt existe à l'adresse dite, et sa révision ;
2. son fichier de licence, s'il en a un : le nom exact de la licence, et si elle couvre les données (catalogues, journaux) ou le seul code ; sans fichier de licence, le droit commun s'applique et le réemploi n'est pas permis par défaut : il faudrait alors s'en tenir à la lecture, ou écrire aux auteurs (contact externe : nœud) ;
3. si les catalogues d'injections reproduisent des passages des articles : chaque article garde sa propre licence arXiv, qui se lit sur sa page ; l'annexe B les liste ;
4. que les journaux d'arbitrage ne portent pas de sorties de modèles soumises à des conditions d'usage qui en limitent la redistribution ;
5. que le rejeu ne demande aucun appel de modèle (l'annexe dit de ses propres scripts qu'ils n'en font pas ; à constater).

## 5. Ce qu'il faudrait pour le faire

- Un mot de Lazar pour la ligne « rejeu public » (aucune dépense de calcul ; mais c'est une ressource extérieure, et N-061 demande la licence vérifiée et un devis par ligne, ici de 0 USD).
- Le téléchargement dans un dossier neuf et vide, tenu pour non fiable ; aucune exécution de leur code : on ne lit que les tables ; empreinte de l'archive, révision consignée, versement scellé sous `docs/sources/`.
- Une table de correspondance écrite **avant** d'ouvrir les journaux : leurs colonnes vers les quatre fichiers d'entrée de notre programme ; la règle binaire de la fausse alerte ; la liste des systèmes relus, tous, sans en choisir.
- Le programme de dépouillement admis d'abord sur ses cas et sur l'oracle simulé ; le rejeu public vient après, comme troisième objet.
- Toute phrase tirée du rejeu cite l'article et s'écrit comme un essai de notre instrument, non comme un résultat sur leurs systèmes ; aucun chiffre de leur article n'est repris sans page vérifiée (R7).

## Ce que je n'ai pas fait

Je n'ai lu de l'article que les pages 2, 4, 30 et 31, par extraction de texte ; je n'ai regardé aucune figure ni aucune table de résultats ; je n'ai ouvert ni le dépôt public ni aucune page en ligne. L'absence de licence du dépôt dans l'annexe M.3 est ce que je n'y ai pas trouvé, non une preuve qu'il n'en a pas.
