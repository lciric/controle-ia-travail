# Complément 1 aux mandats de l'épreuve à vérité plantée : passage par lots — v1

Écrit par la mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) le 20 novembre 2026 (R-4149). Il complète les mandats `mandats-epreuve-verite-plantee-v1.md` (`2dce334d…`), dont l'en-tête et les règles communes restent valables. Il remplace les points 2 et 4 du rôle 1, et les points 1 à 3 du rôle 2. Le rôle 3 est inchangé, sauf ce que dit la section 4.

## 1. Pourquoi
Les 7 269 mondes pèsent environ 73 Go ; `/dev/shm` a 16 Go. Les vérités sont déjà écrites par le tireur, sous l'entropie neuve, dans `/dev/shm/b5f-epreuve-v1/verites/verites-epreuve-v1.json`. Leur empreinte (`3eb337434a5d0652bbb4a109175616456a9383a69915050892e93a5d7d2f63a6`) est engagée au registre des scellements, clé `EPREUVE-VERITE-PLANTEE-B5-VERITES-PASSAGE-1`, avant tout passage. Le monde `V0-0000`, déjà écrit, est le premier du lot 0.

## 2. Le tireur, par lots
1. Il prend la liste des mondes dans l'ordre de `liste_mondes()` et la coupe en lots de 300 mondes, le dernier lot plus court. Les lots sont numérotés à partir de 0.
2. Pour chaque lot k :
   - il fabrique ses mondes sous l'entropie, dans `/dev/shm/b5f-epreuve-v1/mondes/lot-k/` ;
   - il écrit l'inventaire du lot, `/dev/shm/b5f-epreuve-v1/inventaires/inventaire-lot-k.txt` (chemins relatifs triés, chacun avec son sha256) ;
   - il écrit alors le témoin `/dev/shm/b5f-epreuve-v1/temoins/lot-k.pret`.
3. Il attend le témoin `lot-k.joue` du joueur, puis il efface `/dev/shm/b5f-epreuve-v1/mondes/lot-k/`. Le chemin est construit à partir du seul numéro, vérifié entier : jamais à partir d'une variable libre. Il garde l'inventaire.
4. Il ne fabrique jamais plus de deux lots d'avance sur le joueur : jamais plus de deux lots sur disque à la fois.
5. Tout se fait dans un programme de son bloc-notes, lancé en arrière-plan, qui écrit un journal. L'entropie n'y est lue que du fichier des vérités, et n'est jamais affichée ni écrite ailleurs.
6. À la fin, il écrit l'inventaire général : la concaténation des inventaires de lots, dans l'ordre. Il rend à la mère son empreinte et le nombre de mondes.

## 3. Le joueur, par lots
1. Il n'ouvre jamais `/dev/shm/b5f-epreuve-v1/verites/` ni le journal du tireur.
2. Pour chaque lot k, dans l'ordre :
   - il attend `lot-k.pret`, puis vérifie l'inventaire du lot contre les fichiers ;
   - il joue le programme figé, puis le traducteur avec `--accord`, sur chaque monde du lot, comme le disait son point 2 ;
   - il écrit les rendus dans `/dev/shm/b5f-epreuve-v1/rendus/lot-k/` ;
   - il écrit le témoin `lot-k.joue`.
3. Tout se fait dans un programme de son bloc-notes, lancé en arrière-plan, avec un journal.
4. À la fin, il écrit l'inventaire général des rendus. Il rend à la mère son empreinte, le nombre de mondes joués, et le nombre de plantages (ni code 0 ni code 2).

## 4. L'ouvreur
Son point 1 vérifie aussi que l'inventaire général des mondes égale la concaténation des inventaires de lots. Son point 4 verse les inventaires de lots avec le reste.

## 5. Garde de place
Avant chaque lot, le tireur vérifie que `/dev/shm` a au moins 8 Go libres ; sinon, il attend. Si la place manque une heure durant, il s'arrête et le dit, sans rien effacer d'autre que les lots déjà joués.
