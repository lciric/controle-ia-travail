# Contrôle du différentiel v1 → v2 de la consigne des lecteurs du rejeu — v1

- **Contre-lecteur, modèle O** : le même que pour la contre-lecture `d9f5ff4c…`. Je n'ai écrit ni la v2 ni son rapport. Écrit le 2026-11-20 (`date -u` : 2026-11-20T05:30:22Z). Processeur seul, aucune dépense, aucun appel de modèle. Rien n'est écrit dans le dépôt.
- **Pièces**, dossier `docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/consigne-lecteurs-v2/`. Toutes les empreintes sont égales à leur compagnon.
  - la consigne v2, `1e5479bea761dce96ae60e4c93f7991965134c262e3db6ae5a2b66622cc2aa70` ;
  - le fichier de remplacements, le journal et le différentiel ;
  - le rapport, `18837f79…`.
- **Mandat** : `consigne-lecteurs-v1/mandat-redacteur-consigne-lecteurs-rejeu-v2-v1.md` (`c2956c4e…`), égal à son compagnon.

## Verdict

**Conforme**, sous une condition de remise, qui n'est pas une correction de texte : **la consigne v2 n'est remise aux lecteurs qu'une fois le programme de garde de `lignee_reconnue` écrit, essayé et scellé.** Avant, sa phrase du § 4 serait fausse. Le § 4 n'a pas besoin d'être retouché ; une retouche facultative est donnée au § 4 ci-dessous.

## 1. Rejeu de l'outil

J'ai rejoué `remplacer_texte_exact_v1.py` (`391db990…`, recalculé sur ma copie) sur une copie de la v1 (`bf49bd50…`), avec une copie du fichier de remplacements. Il fait 11 remplacements et rend **`1e5479bea761dce96ae60e4c93f7991965134c262e3db6ae5a2b66622cc2aa70`**, égale à l'octet à la v2 versée. J'ai lu le différentiel en entier : il ne porte que ces onze changements.

## 2. K1 à K4, à la lettre

Je les ai comparés mot pour mot au § 8 de ma contre-lecture.
- **K1** : la citation du § 3.2, la phrase qui la suit, et la valeur de `independance` dans le gabarit. Le point 1 du § 9 est inchangé, comme K1 le veut.
- **K2** : la phrase du § 4 et le point 5 du § 9.
- **K3** : le point « Suivre ou corriger un signal rapporté », placé au § 8 après « Régler tes réponses sur un résultat ».
- **K4** : le compagnon de la note de dépôt (§ 2, point 3).

Sept remplacements sont à moi et quatre sont de tenue (titre, ligne de version, § 1 point 4, phrase de garde). Le tableau du rapport le montre bien. Son verdict dit à tort « huit » et « trois » : c'est une erreur de compte dans le rapport, sans effet sur la consigne.

## 3. Les trois phrases de la main du rédacteur

1. **Ligne « Version 2 »** : elle tient. Les empreintes du mandat, de ma contre-lecture et de la v1 sont exactes. Elle annonce deux phrases de tenue (§ 1 et § 4) et les nomme justement.
2. **« 94 ; la liste des cartes hors du choix (`hors_choix`) est vide »** : elle tient. C'est la forme de ma confirmation X6 (`040b83a1…`).
   - Le fichier des cartes porte 94 cartes.
   - Les deux retenues de l'aiguilleur n'y sont pas.
   - Le masque refuserait une `hors_choix` qui les nommerait.
   - La phrase ne fait pas sortir de chiffre neuf ni de nom de carte vers le lecteur.
3. **« La mère contrôle ce champ par un programme de garde à part, joué avant l'assemblage : une valeur hors des six chaînes y sera refusée. »** Elle tient, et c'est la décision de la mère. **Mais elle décrit une pièce qui n'existe pas encore**, comme le rédacteur le dit lui-même. D'où la condition de remise du verdict :
   - le programme existe ;
   - il a un essai, avec un cas sain et un artefact (règle R5) ;
   - il est contre-lu et scellé avant l'ouverture.

## 4. Faut-il retoucher le § 4 ?

**Non.** Les deux temps sont cohérents :
- « le programme ne voit pas » dit vrai du programme d'assemblage, que le lecteur connaît par le § 3 ;
- la phrase ajoutée dit que la garde à part refuse.

La consigne garde ainsi au lecteur sa raison de relire le champ, et la garde ferme le repli silencieux.

**Retouche facultative**, pour qu'un lecteur pressé ne lise pas une contradiction :
- Ancien : « **Toute autre graphie est une faute que le programme ne voit pas.** Il contrôle seulement qu'un texte est présent. »
- Nouveau : « **Toute autre graphie est une faute que le programme d'assemblage ne voit pas.** Il contrôle seulement qu'un texte est présent. »

Si elle est faite, c'est par l'outil, sous un nom neuf, avant la remise. Elle ne retient rien.

## 5. « À contre-lire » dans l'en-tête

La phrase de la v1 vaut aussi pour la v2, et ce contrôle la satisfait. Aucune correction n'est nécessaire. La pièce qui remet la consigne aux lecteurs peut citer ce contrôle et le scellement de la garde.

## 6. Ce qui reste, hors de ce différentiel

L'amorçage par le signal du rejeu v2 (ma contre-lecture, § 7) est dit au lecteur par K3, mais n'est pas ôté. La réserve reste à porter dans la proposition.

## 7. Lu, et incidents

- Lus en entier : le mandat, le différentiel et le rapport.
- Rejeu de l'outil dans `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/contre-lecture-juge-v4/controle-consigne-v2/`.
- Aucune carte, rien sous `archives-reponses-modeles/` ni sous `/root/.claude/`. Aucune commande de liste, une commande simple par appel.
- **Aucun refus** de permission, de classifieur ni de garde.

*contre-lecteur, modèle O*
