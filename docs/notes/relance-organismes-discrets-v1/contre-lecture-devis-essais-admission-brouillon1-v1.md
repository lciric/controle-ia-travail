# Contre-lecture du devis des deux essais d'admission (Mistral Large 4, second lecteur ; `gemini-4-neon`, juge des deux ancres), brouillon 1 — bras A — v1

- **Pièce contre-lue** : `docs/notes/relance-organismes-discrets-v1/devis-essais-admission-mistral-neon-bras-a-v1-brouillon1.md`, `11a352fc3f5c59cc…` (empreinte vérifiée « OK » contre son compagnon), 344 lignes, écrit par Claude Fable 5.2.
- **Contre-lecteur** : Claude Opus 5.5, agent neuf, le 2026-11-21. Je n'ai écrit ni ce devis, ni le texte du bras A, ni le devis de l'essai de mesure, ni leurs contre-lectures.
- **Ce que j'ai fait** : lecture, recherches de chaînes sur des fichiers nommés, calcul des montants par un programme du bloc-notes de la session. Je juge ; je ne corrige rien. Aucun appel de modèle ni appel réseau, aucune clé, aucun sous-agent, aucune dépense. Rien scellé, rien committé.
- **Texte en vigueur** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon43.md`, `4f91b535ad91…` (vérifié). Le devis a été écrit sur le brouillon 42, `c5dbd28eca7b…` (vérifié).

## Verdict

**Engageable après corrections.** Les critères sont repris sans changement. Les conditions d'envoi du mot « b a b go » sont exigées avant tout envoi. Le cas « code 200 avec un autre nom servi » est bien un nœud de Lazar. L'arithmétique est juste au centime près. Les plafonds sont tenus par compteur avant l'envoi : ils ne peuvent pas faire échouer un modèle qui tiendrait autrement.

Huit corrections, toutes à faire avant la ligne de calcul. Le fil commun : **une file est partie dès son premier envoi et ne se rejoue pas**. Toute cause d'arrêt qui n'est pas le modèle doit donc être levée à la vérification de la clé, ou réglée d'avance. Quatre trous le permettent encore : les délais, ce que borne la sortie maximale, la forme des réponses non éprouvée à la vérification, et un compte chargé trop juste. S'y ajoutent deux trous de classement de la vérification et deux gardes manquantes.

## 1. Fidélité au texte et aux mots de Lazar

**Critères : repris sans changement.** J'ai comparé les sept règles du devis (section 7) aux huit règles de 3.4 du brouillon 43.
- Mistral : « 24 réponses de code 200, reprise unique comprise, sans refus, sans fin par sortie maximale atteinte, au moins 22 de forme conforme ; arrêtée au plafond, ne tient pas ». Identique au texte, règle 1.
- Neon : « huit sur huit de forme conforme », mêmes autres conditions. Identique au texte, règle 2, et à la pièce « b a b go », choix 1 (b) (`00af2aa8…`, ligne 8).
- Un seul nom servi : « toutes les réponses de la file portent le nom servi que la vérification de la clé a relevé ». Identique au texte, règle 3 ; la file coupée par le service ne tient pas non plus.
- Une file jouée une fois ; nœud de Lazar si un modèle ne tient pas ; l'autre rôle n'en dépend pas. Identique, règles 4 et 5.
- **Deux écarts de forme, sans effet sur le fond.** La règle 6 du texte (« ni Carbon, ni GPT, ni DeepSeek, ni aucun autre modèle ne prend un rôle sans un mot de Lazar ») n'est pas recopiée ; les règles 7 et 8 du texte deviennent 6 et 7. Le texte veut que le fichier des règles soit « la copie » des règles du texte (règle 8) : il doit recopier les huit règles, à la lettre et dans leur numérotation, et non le résumé du devis (correction 7).

**« Ce que ce devis fixe pour les lire »** (dernier envoi pour le code et la sortie, deux envois pour le coût ; refus et sortie maximale lus sur les motifs de 5.5). C'est ce que le texte renvoie au devis. C'est conforme au devis de l'essai de mesure (7.3, notations).

**Conditions d'envoi : exigées avant tout envoi, oui.** Section 9 : les six conditions de la pièce (Google : facturation active, partage des journaux désactivé, journaux à 7 jours ; Mistral : offre payante, refus de l'entraînement, point d'accès), « valent avant la vérification de la clé aussi ». Garde 9 : ni vérification ni file sans la pièce du constat. Deux manques :
- la garde 9 ne vérifie que la présence et l'empreinte de la pièce, non son contenu (question 5 ; correction 6) ;
- le texte veut le constat « inscrit à la case de 13.1, avant le premier envoi » (3.4, conditions d'envoi). Le devis ne met cette inscription qu'à la fin (section 12, point 12). Il manque donc une étape : un brouillon du texte qui porte le constat, avant le premier envoi (correction 6).

**« Code 200 avec un autre nom servi » : nœud de Lazar, oui**, sur les deux points d'accès de Mistral et chez Google (4.2 ; 4.3, dernier tiret ; garde 11, artefact). Ce n'est pas un repli. C'est la lettre du brouillon 43 (3.4, « Deux précisions » et « L'exception est bornée »).

**Écart entre les brouillons 42 et 43.** J'ai comparé les deux textes par programme. Seules cinq lignes changent dans les sections utiles :
1. le signe de « ne sert pas ce modèle » est renvoyé au devis, et le code 200 avec un autre nom est un nœud ;
2. l'arrêt de la file du juge à la course devient une garde éprouvée, portée par le programme des ancres ;
3. GO-2026-11-21-32 et GO-2026-11-21-33 sont inscrites (lignes 631 et 632 du registre, tête `e77fa0d9`) ;
4. la phrase sur l'exclusion de l'entraînement chez Mistral nomme ses exceptions, les modèles « Labs » et « Preview » ;
5. un renvoi de numéro de brouillon.

Le devis avait déjà suivi les points 1 et 2, d'après la vérification du brouillon 42. **Aucun écart ne touche une règle.** Trois choses sont à reprendre (correction 7) : citer le brouillon 43 au lieu du 42 (en-tête, sections 0, 2 et 7) ; écrire que les deux lignes sont inscrites au lieu de « je ne l'ai pas relu au registre » ; ajouter à la section 9 la réserve « Labs » et « Preview ». Cette dernière n'a pas d'effet : le relevé donne `mistral-large-4-0` en disponibilité générale (« GA »).

## 2. Arithmétique

Je l'ai refaite par programme (`arith.py`, bloc-notes de la session), à partir des seuls tarifs et volumes que le devis déclare. Les prix comptés sont 0,77 et 2,31 pour Mistral, 3 et 15 pour Neon. Les bornes d'entrée sont de 5 000 et 24 000 jetons. La sortie pleine est de 32 768 jetons. Le corps de la vérification est pris à 200 octets.

| grandeur | devis | recalculé |
|---|---|---|
| un envoi, Mistral (appariement ; couverture) | 0,080 ; 0,094 | 0,0795 ; 0,0942 |
| un envoi, Neon | 0,507 ; 0,564 | 0,5065 ; 0,5635 |
| file Mistral, deux envois (trois) | 3,99 (5,99) | 3,9937 (5,9905) |
| file Neon, deux envois (trois) | 8,33 (12,50) | 8,3323 (12,4985) |
| vérification Mistral, trois appels | 0,23 | 0,2275 |
| vérification Google, trois appels | 1,48 | 1,4764 |
| total au pire cas ; somme des plafonds | 14,26 ; 14,75 | 14,2574 ; 14,75 |
| attendu Mistral ; Neon | 0,18 ; 0,34 | 0,1811 ; 0,3393 |
| cinq fois la sortie supposée | 0,74 ; 1,54 | 0,7355 ; 1,5393 |
| option 16 384 | 2,2 ; 4,4 | 2,177 ; 4,400 |
| à charger : Mistral ; Google | 5,50 ; 11,50 | 4,75 × 1,15 = 5,46, arrondi à 5,50 ; 10 × 1,15 = 11,50 |

**Tout est juste.** L'attendu de Neon est calculé sur le compte de Google, ce qui est cohérent. L'attendu de Mistral prend le compte de Claude, le plus haut.

**Plafonds tenus par compteur avant l'envoi : oui** (6.4, garde 1), par file et par vérification. Sous 0,25 et 1,50, le compteur laisse passer trois envois au pire cas, pas un quatrième. Cela tient la ligne « trois appels », même si un appel de vérification était repris.

**Une file peut-elle dépasser son plafond ?** Par le compteur, non, sous les trois conditions que le devis dit lui-même : prix comptés au moins égaux aux prix facturés ; entrée d'au plus un jeton par octet ; sortie maximale respectée par le service, réflexion comprise. La troisième n'est pas établie : c'est la correction 2. Si elle manque, le dépassement est d'un envoi au plus, puis la file s'arrête. La seconde barrière, en nombre d'appels au relais, tient elle aussi : 16 envois de Neon sur les huit entrées fixées font 8,33 au pire cas.

**Le plafond peut-il faire échouer un modèle qui tiendrait ?** Non. Pour tenir, chaque appel doit finir par un code 200 sans sortie maximale atteinte. Le cumul compté reste alors sous deux pires cas par appel, soit 3,99 et 8,33, sous 4,25 et 8,50. Le jeu laisse environ 6 900 jetons d'entrée de plus par envoi chez Mistral et 3 500 chez Neon, au-delà des bornes supposées de 5 000 et 24 000 octets. C'est large devant les consignes déclarées (4 468 et 21 503 octets au plus). L'objet de 6.4 est donc atteint pour la caisse du compteur. **Il ne l'est pas pour la caisse du fournisseur** (correction 8), ni pour les délais (correction 1).

**Montant à charger.** La marge de 15 % est dite couvrir « taxes et conversion ». Si une taxe sur la valeur ajoutée de 20 % est prélevée sur la recharge, 5,50 ne donne que 4,58 de crédit, sous les 4,75 des plafonds de Mistral. Google donnerait de même 9,58 sous 10,00. Le devis l'ignore ; il l'écrit (« je ne sais pas »). Voir la correction 8.

## 3. Le signe de « ne sert pas ce modèle »

**Il est fermé et constatable par programme**, à quatre défauts près. Le signe exige deux constats sur le point d'accès européen :
- la liste rend 200 sans l'identifiant ;
- l'appel rend 400 ou 404, avec un corps d'erreur de Mistral où le type vaut `invalid_model`, ou le code vaut `1500`, ou le message nomme l'identifiant avec l'une de quatre chaînes.

Tout est écrit avant l'appel. Le texte veut « le code de retour et, s'il le faut, le type ou le message d'erreur » : c'est ce que fait le devis. La condition sur la liste ajoute une exigence et ne l'élargit pas. La forme attendue est déclarée supposée, sans pièce, et l'issue est prudente : si la forme réelle est autre, le signe n'est pas constaté, et le cas revient à Lazar.

**Les quatre défauts** (correction 4) :
1. **« Ou l'inverse » contredit le texte.** Le tiret des constats qui se contredisent range en nœud « liste qui porte l'identifiant et appel refusé pour modèle inconnu, ou l'inverse ». L'inverse comprend le cas « liste sans l'identifiant, et appel au code 200 avec le bon nom ». Or le texte (3.4) et le devis lui-même (4.1, 4.3) disent ce cas **sain**, et le point d'accès européen retenu. La liste ne doit pas entrer dans la santé de la vérification. La garde 11 doit avoir cet artefact : liste sans l'identifiant, code 200 avec le bon nom, donc saine et retenue.
2. **Pas d'issue pour le reste.** « Tout le reste n'est pas le signe » énumère trois classes, mais n'écrit pas d'issue pour ce qui n'y entre pas. Exemples : un 404 au corps qui n'est pas celui de Mistral, un 400 qui ne nomme aucun champ, un 422. Mistral rend peut-être 422 pour un champ invalide (S : souvenir du rédacteur de cette contre-lecture, sans pièce). 4.2 ne traite que le 400. Il faut une ligne finale fermée : toute autre issue de la vérification est non saine, nœud de Lazar, sans repli ni appel de plus.
3. **« Nomme la température » et « nomme un autre champ »** (4.2) ne sont pas définis par programme. Il faut l'écrire : par exemple, le champ `param` du corps d'erreur, ou la chaîne `temperature` dans le message, sans égard à la casse. Sans cela, la session décide après avoir vu la réponse : c'est ce que le texte interdit pour le signe et, par extension, pour la vérification.
4. **401 ou 403 après une liste lisible sans l'identifiant.** Ce cas est rangé en « cause à corriger, vérification refaite ». Une clé refusée rend déjà la liste non lisible. Un refus de l'appel après une liste admise dit plutôt que le modèle n'est pas servi à ce compte sur ce point d'accès, ce que Lazar ne peut pas corriger. Je recommande : liste admise sans l'identifiant, puis tout code autre que le signe, 429, 5xx ou délai, donc nœud de Lazar.
5. Deux précisions de forme, mineures : « liste lisible » (objet JSON, tableau `data`, champ `id` de chaque entrée ; les alias ignorés) ; et `code` comparé comme chaîne.

**Autres codes, dans les files.** Le classement est fermé et prudent. 401, 402 et 403 arrêtent. 429 suit 5.6. Les pannes de transport ont une reprise. 400 et tout autre code arrêtent. Tout motif de fin inconnu vaut refus. Un défaut mineur : 5.6 nomme 500, 502, 503 et 529, la garde 4 dit « 5xx » ; un 504 est repris selon l'une, arrêté selon l'autre.

## 4. Les réserves du rédacteur

| réserve | jugement | raison |
|---|---|---|
| **Deux envois par appel, non trois** | **procédure acceptable, fidèle au texte** | 3.4 dit « 48 envois au plus (un envoi et une reprise) » et « 16 envois au plus ». La règle 1 reprend le critère de l'essai de mesure « inchangé », et cet essai n'avait aucune redemande de forme (devis `533ad5b1…`, 6.2). Le « trois » de 6.11 est le majorant de la course. Le texte prime sur la consigne de rédaction. Rien à demander à Lazar. |
| **Ce que borne la sortie maximale, non établi** | **défaut à corriger** (correction 2) | Le texte (règle 7) veut que « le devis des essais constate et écrive avant tout envoi » ce que borne la sortie maximale. Le brouillon 1 ne fait que supposer, et ne prévoit un nouveau brouillon que si le relevé dit « réponse seule ». C'est insuffisant à trois titres : la version acceptée doit écrire le constat dans tous les cas ; aucune issue n'est écrite si la documentation se tait ; la garde 3 arrête la file sur une sortie facturée au-delà de 32 768, ce qui, si la borne ne vise que la réponse, ferait échouer une lecture normale pour une raison de devis. |
| **Formes d'erreur et champs supposés** | **acceptable pour les erreurs et les noms de compteurs, après la correction 3** | La vérification de la clé porte les réglages de la file : un champ refusé se voit avant la file. Elle relève les noms du bloc d'usage, mais n'en tire aucune issue. Si un champ de 5.5 manque, rien n'est dit avant la file, et la file s'arrêtera à son premier envoi : elle sera partie, et le modèle ne tiendra pas. La forme du texte de la réponse n'est pas fixée non plus : contenu en chaîne ou en morceaux chez Mistral, parts de pensée chez Google. Le programme de forme doit savoir ce qu'il juge avant le premier envoi. |
| **Aucune page de prix scellée** | **procédure acceptable**, telle qu'écrite | Le devis exige les deux pages versées et scellées avant la ligne de calcul, et sa reprise si un prix lu dépasse le prix compté. C'est ce qu'avait fait l'essai de mesure. Mineur : la ligne de GO cite leurs empreintes. La facturation de la réflexion de Mistral au prix de sortie est à chercher dans le même relevé. |
| **Une ligne de vérification pour trois appels** | **question pour Lazar** (question 1) | Le texte dit « la vérification se refait, chaque fois sous sa ligne ». La lecture stricte (une ligne par appel) et celle du devis (trois appels par ligne, même cause ou cause corrigée) tiennent toutes deux. Le plafond par compteur borne la dépense à trois envois. Mon avis : trois appels, si la ligne l'écrit en toutes lettres. Le retrait automatique de la température y entre. |
| **Un code 429 qui consomme la reprise** | **procédure acceptable**, à dire à la ligne | Le choix est fait avant tout envoi. Il ne touche pas la forme. Il reste dans « un envoi et une reprise ». Un 429 ne porte aucun contenu, et 8.6 range la panne du fournisseur parmi les causes de transport. L'essai de mesure arrêtait au premier 429 ; sa contre-lecture jugeait ce choix strict « tenable » et une variante « permise » (`d1b8ad89…`, ligne 54). Ici, une file ne se rejoue pas : la reprise évite qu'une limite de débit décide. Mineur : dire ce que fait le programme si `Retry-After` dépasse 60 secondes (envoi à 60, ou arrêt). |
| **Température 0 envoyée à Mistral** | **procédure acceptable, fidèle au texte**, après deux précisions | Le texte veut « 0 si le service l'accepte, retirée s'il la refuse ou la dit sans effet ». Le devis l'envoie et la retire sur un refus constaté à la vérification. Deux manques : « nomme la température » n'est pas défini par programme (correction 4) ; la branche « la dit sans effet » n'est cherchée par personne. Le relevé documentaire (section 12, point 2) doit dire si Mistral déclare la température sans effet sous `reasoning_effort` ; si oui, elle n'est pas envoyée. |

## 5. Gardes

**Les treize gardes ont chacune un cas sain et un artefact**, contre un faux fournisseur local, sans appel payant. C'est conforme à R5 sur la forme. Deux artefacts sont flous : la garde 12 (« rien ne part, ou règle non appliquée » : laquelle ?) ; la garde 2, dont « trois délais de suite » est un cas que la garde 2 elle-même rend impossible (deux délais sur un même appel arrêtent déjà).

**Il en manque deux, et deux autres sont trop faibles** (corrections 5 et 6) :
- **Identifiant figé et voie d'accès : aucune garde.** La garde 3 vérifie les noms des champs, non la valeur de `model` ni le chemin de Google. La garde 5 compare le nom servi au relevé, et la vérification compare le nom servi à l'identifiant demandé. Un alias glissé dans la configuration (`mistral-large-latest`, `mistral-large-4`, `gemini-4-neon-latest`) serait donc demandé, servi, relevé et jugé sain sous ce nom. Il faut une garde : identifiant demandé égal, à la lettre, à la constante du texte (`mistral-large-4-0`, `gemini-4-neon`) ; hôte amont parmi les trois permis ; artefacts sur les trois alias et sur un hôte autre.
- **Repli sur le point d'accès global : aucune garde qui le lie au signe.** La ligne 5 peut être accordée d'avance. La vérification globale doit alors exiger le relevé scellé de la vérification européenne, signe constaté. Artefact : relevé sans signe, ou absent, donc refus.
- **Garde 9, conditions d'envoi : trop faible.** L'empreinte de la pièce est celle que la session inscrit à la configuration : toute pièce scellée passe. La garde doit lire la pièce : une ligne par condition, avec la valeur attendue, une date en temps universel antérieure au premier envoi, et le mot de Lazar. Artefacts : une condition manquante, une valeur contraire (partage des journaux « activé », journaux à 55 jours), une date postérieure.
- **Vérification de la clé : aucune garde sur la forme de la réponse** (correction 3). Il faut des champs de 5.5 présents, un nom servi présent, un motif présent, et un texte de réponse extractible selon la règle fixée. Sinon, vérification non saine et brouillon neuf du devis. Artefact : une réponse 200 sans `total_tokens`, ou sans `modelVersion`.

Mineurs : une garde sur les huit entrées de Neon (identifiants et ordre fixés en 3, refus de toute autre) ; le contrôle « aucun morceau de réponse dans le rapport » (section 8) mis au tableau, avec son cas sain et son artefact, comme toute garde d'arrêt.

## 6. Les lignes de GO

Les cinq lignes sont bornées : objet, nombre d'appels, plafond tenu par compteur, variable de la clé, compte qui paie, empreinte du devis accepté. La ligne 5 est conditionnelle, sur un signe fermé : c'est acceptable, avec la garde qui la lie au signe (section 5). Les lignes 3 et 4 ne servent qu'après une vérification saine.

À compléter (mineurs) :
- lignes 1, 2 et 5 : « trois envois au plus » (et non seulement trois appels), et que le retrait de la température se refait sous la même ligne ;
- ligne 3 : point d'accès, celui du relevé de vérification ; prix compté à 1,1 fois dans les deux cas ;
- toutes : empreintes du constat des conditions d'envoi, du fichier des règles, des pages de prix et du relevé documentaire ; brouillon du texte en vigueur ;
- le montant à charger n'est pas une ligne de calcul, mais c'est un geste de paiement : le présenter à Lazar avec les lignes, en crédit net (correction 8).

## 7. Corrections, mineurs, questions

### Corrections (avant la ligne de calcul)
1. **Délais.** Le devis ne dit pas si l'amont est lu en flux, ni si la réflexion y est muette. Le corps de 5.2 n'a pas de champ `stream`. Les relais de l'essai de mesure lisaient l'amont en flux, réflexion muette (`--sans-pensees-amont`). 240 secondes de silence bornent alors une réflexion de 32 768 jetons sous un débit de 137 jetons par seconde. Sans flux, le silence égale le total, et les 900 secondes ne servent à rien. Le délai global de deux heures est sous 24 × 910 secondes, soit six heures. Deux coupures sur un appel, ou le délai global, arrêtent une file partie : le modèle ne tient pas pour une raison de délai. Il faut écrire le mode de chaque amont, et régler silence, total et délai global pour qu'aucun ne coupe une réponse servie dans la sortie maximale, à un débit déclaré. Sinon, le dire à Lazar comme une cause possible d'échec.
2. **Sortie maximale.** Écrire dans la version acceptée le constat de ce que borne la sortie maximale de chaque service, avec le relevé cité par chemin et empreinte, quelle que soit la réponse. Écrire d'avance l'issue si la documentation se tait. Ma recommandation : règle 7 lue sur la sortie facturée totale, la plus prudente contre la coupure ; condition (c) de 6.4 déclarée non établie. Si la borne ne vise que la réponse, la garde 3 ne doit pas arrêter une file pour une sortie facturée au-delà de 32 768.
3. **Vérification de la clé, forme de la réponse.** Exiger à la vérification tous les champs de 5.5 (`thoughtsTokenCount` absent vaut 0), le champ du nom servi et le motif. Fixer avant tout envoi l'extraction du texte jugé par le programme de forme : chez Mistral, contenu en chaîne, ou concaténation des seuls morceaux de type texte s'il est rendu en morceaux ; chez Google, concaténation des parts qui ne sont pas des pensées. Faute de quoi, vérification non saine et brouillon neuf, non une file arrêtée à son premier envoi.
4. **Classement fermé de la vérification.** Retirer ou préciser « ou l'inverse » (code 200 et bon nom : saine, quelle que soit la liste). Définir par programme « nomme la température » et « nomme un autre champ ». Ajouter une issue finale : toute autre issue est non saine, nœud de Lazar, sans repli ni appel de plus (422 et 404 hors forme compris). Classer « liste admise sans l'identifiant, puis 401 ou 403 » en nœud. Définir « liste lisible » ; comparer `code` comme chaîne.
5. **Garde de l'identifiant figé et de la voie d'accès**, et garde qui lie la vérification globale au signe constaté (section 5).
6. **Conditions d'envoi.** La garde 9 lit le contenu du constat. Ajouter l'étape que le texte exige : le constat inscrit à la case de 13.1 dans un brouillon du texte, avant le premier envoi. Le fichier des règles cite l'empreinte de ce brouillon.
7. **Reprise sur le brouillon 43.** Citations ; GO-2026-11-21-32 et -33 inscrites ; réserve « Labs » et « Preview ». Le fichier des règles recopie les huit règles du texte à la lettre, règle 6 comprise, dans leur numérotation.
8. **Compte du fournisseur.** Un compte à court coupe la file après son premier envoi (402), donc le modèle ne tient pas (règle 3) : c'est la caisse qui décide, contre l'objet de 6.4. Exprimer le montant à charger en crédit utilisable, net de taxes et de conversion. Retirer « compte chargé au plus juste » comme troisième barrière, ou dire à Lazar ce risque. Dire de même qu'un 429 répété peut faire échouer une file : la phrase « ce sont les réglages qui décident, non la caisse » est à nuancer.

### Mineurs
- m-1 : 504 et les autres 5xx, à harmoniser entre 5.6 et la garde 4.
- m-2 : « trois délais de suite », inatteignable ; à retirer ou à redéfinir.
- m-3 : `Retry-After` au-delà de 60 secondes, issue à écrire.
- m-4 : garde sur les huit entrées de Neon.
- m-5 : contrôle « aucun morceau de réponse » au tableau des gardes.
- m-6 : artefact de la garde 12 sans « ou ».
- m-7 : relevé documentaire étendu à la température sous `reasoning_effort` chez Mistral, et à la facturation de sa réflexion.
- m-8 : compléments des lignes de GO (section 6).
- m-9 : le relais de Mistral porte « le plafond en dollars de sa ligne » ; dire s'il est relancé à chaque ligne ou réglé par ligne.
- m-10 : ordre de 13 (le constat d'abord, les lignes de calcul avant la contre-lecture du programme) ; l'ordre du devis est plus prudent ; à dire.

### Questions pour Lazar, avec mon avis
1. **Une ligne de vérification pour trois appels, ou une ligne par appel ?** Avis : trois appels au plus, écrit en toutes lettres à la ligne. Le plafond par compteur le borne déjà.
2. **Sortie maximale à 32 768 ou à 16 384 ?** Avis : 32 768, comme le recommande le devis. Une coupure de réglage ferait échouer un modèle pour quelques dollars de plafond non dépensés. À réexaminer si la correction 1 montre que les délais ne tiennent pas à 32 768.
3. **Ligne 5 accordée d'avance, sous condition ?** Avis : oui, avec la garde de la correction 5.

## Fichiers ouverts

Empreintes vérifiées par `python -m controle_ia.scellement verifier`, toutes « OK » :
- le devis contre-lu, `11a352fc3f5c…`, lu en entier ;
- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon43.md`, `4f91b535ad91…` : section 3.4 en entier ; 6.11 ; 8.6 (au-delà des sections citées, pour la reprise) ; préambule de 13, point 4 et son sous-point sur les essais d'admission ; 13.1, case « lecteurs et juge des ancres » ; 13.2, cases « tarifs », « devis », « version des modèles », « lignes de GO » ;
- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon42.md`, `c5dbd28eca7b…` : comparé par programme au brouillon 43, mot à mot sur les lignes qui changent ;
- `devis-essai-de-mesure-lecteurs-bras-a-v1-brouillon3.md`, `533ad5b15e6d…` : sections 6.2 à 7.3 et 9, lues ; recherche de chaînes sur le reste ;
- `contre-lecture-devis-essai-de-mesure-lecteurs-v1.md` (`d1b8ad89037c…`), `verification-devis-essai-de-mesure-brouillon2-v1.md` (`f2180d176673…`), `verification-devis-essai-de-mesure-brouillon3-v1.md` (`d510f8138ae5…`) : recherche de chaînes seulement (délais, flux, 429) ;
- `mots-de-lazar-juge-et-envoi-des-textes-bras-a-2026-11-21-v1.md`, `00af2aa83604…`, en entier ;
- `lecteur-remplacant-carbon-identifiant-fige-mistral-v1.md` (`b8163cc99290…`), `juge-des-ancres-identifiant-gemini-v1.md` (`ac8bb15e1cfc…`), `conditions-envoi-textes-google-mistral-releve-v1.md` (`b959c4d0db2e…`), en entier.

Tous sous `docs/notes/relance-organismes-discrets-v1/` sauf les deux brouillons du texte.

## Écarts

- **Liste du dossier** `docs/notes/relance-organismes-discrets-v1/`, premier niveau, noms seulement, pour trouver la contre-lecture et les vérifications du devis modèle. Aucun sous-dossier listé ni ouvert.
- **13.1 et 13.2 du brouillon 43** : pour repérer les cases, j'ai affiché les 200 premiers caractères de chaque ligne des deux tableaux, cases non demandées comprises (moniteurs, entropie, base, registre, confinement). Ces débuts nomment des chemins cloisonnés ; je ne les ai pas suivis.
- **Hors des sections citées** : 8.6 du brouillon 43 et le sous-point du préambule de 13 sur les essais d'admission, lus pour juger la reprise et l'ordre des étapes.
- **Chiffres mesurés du devis** (longueurs de 6.2, octets des consignes) : non vérifiés. Ils viennent des entrées de l'essai et des rapports techniques sous `runs/`, que je n'ai pas ouverts. L'arithmétique part des valeurs déclarées. Le rédacteur déclare lui-même avoir lu ces rapports par programme et listé le premier niveau des dossiers des files (son 14) : je le signale sans le juger.
- **Une affirmation de cette contre-lecture vient de mémoire, sans pièce** : que Mistral rende peut-être 422 pour un champ invalide, et son contenu en morceaux sous raisonnement. Elle est marquée S ; la correction ne dépend pas de sa vérité, seulement de ce que ces cas sont possibles et non classés.
- Fichiers écrits : celui-ci ; dans le bloc-notes de la session, `arith.py` et deux extraits du brouillon 43. Le harnais a gardé de lui-même deux sorties longues hors du dépôt. Rien scellé, rien committé, aucun compagnon.
- **Aucun chemin cloisonné ouvert, listé ni empreinté.** `.claude/`, `registres/`, `runs/` et le journal non touchés.
