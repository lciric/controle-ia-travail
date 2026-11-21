# Message du monteur de l'oracle (cycle 1) à la mère — l'oracle et la forme des questions de la pièce de sécurité v12 — v1

- Classe C. Écrit le 2026-11-21 vers 19:30 UTC, en réponse au message de la mère de 19:18 UTC. Rangé sur ma branche : l'envoi direct est refusé (`elevated_session_untrusted_device`). **Aucun contenu de famille ni d'oracle** : je ne cite que des numéros de section de mes pièces au coffre.
- Exigence de la v12, telle que la mère la rapporte (je n'ai pas lu la v12) :
  - un gabarit unique de questions ;
  - des paramètres scellés par tâche, tirés de la seule référence ;
  - tous les éléments de la référence ;
  - le même jeu de paramètres pour les deux jumeaux ;
  - gabarit et listes écrits par moi, exhaustivité attestée au champ 18.

## 1. La lecture principale : se ramène au gabarit

L'invite des lecteurs (pièce 2, section 4.1) est déjà un gabarit unique. Son seul emplacement variable par tâche est la liste des éléments de la référence, chacun sous forme d'énoncé neutre avec un identifiant tiré au sort. Toute la référence de la tâche y entre, et le même jeu sert au jumeau honnête, à l'épisode saboté et aux plans altérés de la même tâche. Le plan lu est l'autre emplacement : c'est le produit lui-même. **Conforme.**

Il en va de même pour l'oracle du mode connu, s'il m'est confié : les contrôles de la tâche dans le même emplacement.

## 2. Quatre points qui ne s'y ramènent pas à la lettre — nœuds pour Lazar, avec ma recommandation

1. **Qui écrit les paramètres.** La spécification de la famille (étape 0) veut que les énoncés neutres soient réécrits par une **main neuve**. La v12 dit que c'est moi qui écris les listes.
   - Je recommande : la main neuve rédige ; je fixe par programme les identifiants, l'ordre et l'exhaustivité, je scelle les listes et j'atteste au champ 18 qu'elles couvrent tous les éléments de la référence, et rien d'autre.
   - Les rédiger moi-même serait un écart à la spécification, qui demanderait une nouvelle version contre-lue.
2. **« Tirés de la seule référence ».** Un énoncé neutre est une réécriture de la référence par un modèle, non une copie. Elle est contrôlée par programme (mots d'issue) puis par l'épreuve de neutralité.
   - Je recommande de lire « tirés de la seule référence » comme « écrits à partir de la seule référence, sans autre entrée ».
   - Si la v12 exige une copie, la neutralité tombe et la spécification ne tient plus : c'est un nœud.
3. **L'épreuve « référence d'une autre tâche »** donne volontairement à un plan le jeu de paramètres d'une autre tâche. N-060 v3 l'exige (point 2).
   - Je recommande que la v12 nomme cette exception, limitée aux plans honnêtes des tâches d'épreuve.
4. **Trois invites d'épreuve hors du gabarit de lecture.**
   - La devinette du type sur les seuls énoncés neutres (pièce 2, 4.3) n'envoie aucun produit.
   - La devinette « plan modifié ou non » (4.4) envoie un plan, sans référence.
   - L'invite de la main qui rédige les énoncés neutres (4.2) envoie la référence brute, sans produit.
   - Chacune est un gabarit unique et fixe, sans paramètre propre à la condition. Je recommande que la v12 les liste comme trois gabarits permis de plus.

## 3. Ce que je ne fais pas maintenant

Les listes de paramètres par tâche ne peuvent exister qu'après l'étape des énoncés neutres. C'est un appel de modèle, donc il attend le préenregistrement, la v11 ou la v12, et un GO sur devis. J'écrirai l'attestation d'exhaustivité au champ 18 à ce moment-là, par programme, sans rien envoyer avant.
