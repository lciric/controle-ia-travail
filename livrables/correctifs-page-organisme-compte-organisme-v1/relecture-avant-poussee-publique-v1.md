# Relecture avant poussée publique — commit `ee53033` (correctif de la page d'état de l'attaque Goodhart) — v1

**Verdict : poussable après corrections** (deux corrections exigées, C1 et C2 ; deux recommandées, C3 et C4 ; les sept conditions de la ligne de publication GO-2026-11-14-03 sont tenues sur le commit tel qu'il est).

Auteur : modèle A ; relecteur : modèle B ; A ≠ B. Le relecteur n'a rien écrit de ce qu'il lit ; il n'a écrit que ce fichier. Aucune commande git d'écriture, aucun accès réseau, aucune recherche récursive, aucun refus rencontré.

Heure de début (sortie de `date -u` du premier appel, recopiée) : `Sat Nov 14 10:03:53 UTC 2026`. Heure de fin : en bas, écrite par `date -u` dans la commande qui crée ce fichier.

## 1. Ce qui a été lu et rejoué

| objet | preuve |
|---|---|
| commit | `git show --stat HEAD` : `ee5303335486d93fba31e75196133c95bc409b3a`, 2 fichiers, 7 insertions, 2 suppressions (`MANIFEST.md` +5 ; page d'état +2 −2) |
| patch exporté | `sha256sum` : `bc8f05371365644881e7ab14fc20fdbd0f4870b2338a12bdd42164f66a24b55e` ; `git show HEAD \| diff - PATCH` : muet (patch = commit) |
| parent | `git rev-parse HEAD^` = `bdf6bc4bbe04228f83671b7fcfa89f1738b5604c` = `git rev-parse origin/main` (référence locale, pas de réseau) |
| arbre de travail | `git diff --quiet HEAD` : code 0 (propre) |
| `nul_v9.py` | `sha256sum` : `7ae450df2482246122bf9fbcf0fa5ef30b4a7e4c6f0d09531e83af048e46ee95` (celle que cite la page) ; `git diff bdf6bc4 HEAD --stat -- orchestrator/pole/nul_v9.py` : vide |
| page d'état après commit | `c2c1b29aac90113d2ba9c5b17cde1ca3720cc806082d6dae8d8d48d01f700d9d` |
| `MANIFEST.md` après commit | `6dc39a376c2874f827aa835b014e6f006540dac6de050e970e36983f0c4d8c64` |

## 2. Conditions de la ligne de publication, une à une

| condition | commande | résultat | tenue |
|---|---|---|---|
| aucune pièce sous embargo de P3-bis | `grep -cE 'P3' PATCH` ; `grep -cE 'embargo\|consigne\|Lazar' PATCH` | 0 ; 0 | oui |
| aucune consigne privée | même commande ; lecture des 7 lignes ajoutées | 0 ; rien | oui |
| aucun brouillon « axe de la douleur » | `grep -cE 'douleur\|[Pp]ain' PATCH` | 0 | oui |
| rien de l'article nommé par la ligne de publication | `grep -cE` sur son titre, majuscules et minuscules | 0 | oui |
| garde des secrets à 0 | la commande de la consigne, sur le patch | `0` | oui |
| aucune poussée forcée | `git merge-base --is-ancestor bdf6bc4 HEAD` : code 0 ; `HEAD^` = `bdf6bc4` = `origin/main` | descendant direct, un seul commit | oui |
| nom de dépôt privé, de branche privée, de registre privé absents | `grep -cE 'controle-ia\|arbre-organisme\|claude/\|brief' PATCH` : 0 ; `grep -nE 'GO-20\|ledger\|registre\|R-2654\|N-T4\|PO-0' PATCH` : une ligne, la 46, ligne de contexte non modifiée et déjà publique | aucun nom privé dans les lignes ajoutées ni dans le message | oui |

Remarque : la branche locale `publication-correctif-page-goodhart-v1` n'est pas un nom privé cité par le texte ; elle deviendrait publique si elle était poussée sous ce nom. À pousser vers la branche publique principale, en avance rapide.

## 3. Constats

### Exigés avant poussée

**C1. L'en-tête de la page d'état devient faux avec ce commit.** Ligne 3, non modifiée : « Last updated: 10 November 2026, 10:44 UTC (the 8 November update and the 2 November text below are kept unchanged). » Or le commit modifie deux puces de la section « Update (8 November 2026) » (lignes 63 et 64 : une phrase remplacée, une phrase ajoutée). Après poussée, la page affirmerait de son propre texte qu'il est inchangé alors qu'il vient d'être corrigé, et porterait une date de dernière mise à jour antérieure à sa dernière modification. Le lecteur public n'aurait, sur la page, aucun signe de la correction (le MANIFEST seul la dit). Précédent dans le même MANIFEST, ligne 367 (13 novembre) : « the date of the last update is changed ». C'est le défaut le plus grave : un correctif d'honnêteté qui rend fausse une phrase d'honnêteté.

Correction proposée, mot pour mot (ligne 3, remplacer la phrase citée par) :

> Last updated: 14 November 2026 (in the 8 November update below, the last sentence of "What the breach is" is replaced and a sentence is added at the end of "Fix"; the rest of that update and the 2 November text are kept unchanged; the section on the attack against v9 is as of 10 November 2026, 10:44 UTC).

(La garde des nombres du programme d'application verra « 14 » en plus : c'est voulu, à déclarer dans le couple. Aucune heure neuve n'est écrite : « 10:44 UTC » est l'heure déjà publiée.) Et ajouter au MANIFEST, dans la puce de la page : « The "Last updated" line at the top of the page says so. »

**C2. « that file » est ambigu.** Dans la puce « Fix », deux fichiers précèdent la phrase neuve : `orchestrator/pole/nul_v9.py` (début de la puce) et `orchestrator/prereg/rapport-redaction-nul-v9.md` (« Proof: … section 3 », deux phrases plus haut, donc l'antécédent le plus proche). Un lecteur peut chercher le commentaire d'en-tête dans le rapport. Le fondement du couple v3 affirme que « that file » désigne `nul_v9.py` ; la grammaire ne le garantit pas. Seul « its hash stays as cited above » lève le doute, en fin de phrase. Le MANIFEST et le message de commit, eux, nomment le fichier.

Correction proposée, mot pour mot : remplacer « The header comment of that file says » par « The header comment of `orchestrator/pole/nul_v9.py` says ».

### Recommandés

**C3. L'erratum prête au commentaire un peu plus que sa lettre.** Lignes 9 à 12 de `nul_v9.py` :

> Pourquoi : `pole/nul_v8.py` (lignes 83 à 90) déclare non couverte la recombinaison par morceaux de lois connues ; l'attaque
> du 2 novembre l'a confirmé (monde W2 : S1 sur la sous-population 0, S2 sur la sous-population 1 ; fonction `carte` de
> `pole/attaque_goodhart_v2.py`) : un proposeur modèle de langage qui lit la description du juge y trouve une loi promue qui
> n'apporte rien au-delà de l'archive.

Le commentaire dit : un proposeur « qui lit la description du juge y trouve une loi promue ». La phrase neuve dit : « the proposer finds the hole by reading the judge's description ». Deux écarts : (i) la relative « qui lit » devient une cause, « by reading » ; pris à la lettre, le commentaire est défendable (par conception le proposeur reçoit la description — page v7, ligne 140 : « a language-model proposer (Argon) that reads the judge's exact description » — et il obtient bien des promotions) ; c'est sa lecture causale que les passages n'établissent pas ; (ii) « finds the hole » pour « y trouve une loi promue ». L'erratum est exact sur le fond (c'est bien la lecture que le commentaire suggère, et les passages ne l'établissent pas), pas sur la lettre. Sens non flatteur : tenu. Le commentaire parle de l'attaque du 2 novembre ; la phrase neuve est logée dans la mise à jour du 8 novembre, sans date : « the runs » couvre les deux passages, ce qui est juste (page, ligne 69 : « the share of the feedback is not measured »).

Correction proposée, mot pour mot (elle intègre C2) :

> The header comment of `orchestrator/pole/nul_v9.py` says that a language-model proposer "that reads the judge's description" finds a promoted law there; the runs do not establish that reading the description is what opens the breach, and the file is left unchanged so that its hash stays as cited above.

De même, le message de commit et le MANIFEST disent que le commentaire « makes the same claim » : il n'en porte que la première moitié (rien sur les verdicts). Mot pour mot : « makes a similar claim ».

**C4. Ligne de co-auteur du message de commit : à vérifier par l'auteur.** La ligne `Co-Authored-By` nomme un modèle ; le relecteur ne peut pas établir que c'est celui qui a écrit le commit, et la consigne d'attribution que reçoit sa propre séance — la séance même dont le message donne le lien — désigne un autre nom. Les commits publics antérieurs portent la même ligne que le commit (`git log -5 --format='%h %(trailers)' bdf6bc4`), donc pas de fuite nouvelle ; mais une ligne d'attribution fausse serait une phrase fausse de plus dans un commit d'erratum. À confirmer ou à corriger avant poussée. Le lien de séance est déjà d'usage dans l'historique public ; il n'entre dans aucune des sept conditions ; signalé.

### Conformes

- **Phrase 1** (« The breach needs no optimisation against the judge. ») : reprise de la page v7, ligne 140 (« … and it needs no optimisation against the judge »), sujet restitué ; appuyée sur la page elle-même, ligne 62 (« 24 of 24 units in both arms; 43 of the 48 promotions at the first attempt; feedback changes nothing (McNemar p = 1.0 …) »). Rien de plus que ces deux pièces ; sens non flatteur (elle retire au proposeur une habileté et dit la brèche banale). Réserve héritée du second lecteur (m1) : c'est une phrase importée de la v7, non un retrait pur. La moitié vraie de la phrase retirée (« not learned from its verdicts ») reste dite ligne 62.
- **Empreinte** : la page cite `7ae450df…`, le fichier la porte, le commit ne le touche pas ; « left unchanged so that its hash stays as cited above » est vrai.
- **MANIFEST** : il décrit exactement les deux modifications de la page (titres des puces, ancienne et nouvelle phrase citées à l'identique — vérifié contre le diff) et dit vrai sur « No new run, no figure changed, no new file; `orchestrator/pole/nul_v9.py` is unchanged » (`--numstat` : 2 fichiers, aucun créé ; aucun chiffre dans les phrases ajoutées à la page). Il lui manque seulement ce que C1 ajoute. Non vérifiable par le relecteur : « the sealed verdict does not establish … » (verdict privé, non ouvert) ; la page dit « the runs do not establish » — préférer la même formule aux deux endroits.
- **Message de commit** : vrai sur les deux fichiers, sur les deux phrases (citées à l'identique), sur « nul_v9.py unchanged », sur « Secret scan on the change: 0 match » (rejoué : 0). Réserves : C3 (« the same claim ») et C4.

## 4. Réponses aux cinq questions

1. Phrases neuves fondées, sans rien de plus, sens non flatteur : **oui** pour la phrase 1 ; **oui avec réserve de lettre** pour l'erratum (C3).
2. Erratum exact sur le commentaire : **sur le fond oui, sur la lettre non** (C3) ; « that file » : **ambigu** (C2).
3. MANIFEST : **exact**, incomplet seulement si C1 est appliquée.
4. Conditions de la ligne de publication : **toutes tenues** (§ 2).
5. Message de commit : **vrai**, sous C3 et C4.

Après corrections : le commit est local et non poussé ; le refaire reste un descendant direct de `bdf6bc4` (aucune poussée forcée) ; la page change d'empreinte, donc le patch est à réexporter et la garde des secrets à rejouer dessus.

## 5. Ce que je n'ai pas fait

Aucune lecture hors des pièces nommées. Pas d'ouverture du verdict scellé ni des sorties privées. Pas de recherche des autres lieux qui citeraient l'empreinte de la page d'état (recherche récursive interdite). Aucune correction appliquée : les textes ci-dessus sont des propositions.

Heure de fin (`date -u`, écrite par la commande) :
Sat Nov 14 10:05:24 UTC 2026
