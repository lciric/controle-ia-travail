# Fiche d'entretien — le bras d'attaque, en une page (v1)

- Classe C. En clair, sans recette ni mode. Rédigée le 21 novembre 2026 vers 16:10 UTC par la session fille de
  l'attaquant informé (`session_01Qi7Gr3Fhau21CJ1GubJqKz`), sur le oui de la mère (16:02Z).
- Chaque fait renvoie à une pièce et à son empreinte (R6). L'auteur n'a lu ni le coffre ni aucun résultat de moniteur.

## 1. Ce que le bras est

Il est l'instrument qui éprouve les moniteurs du programme contre un adversaire. Il n'ajoute aucune revendication : il
fixe comment on éprouve les revendications déjà écrites.
Pièce : `prereg/bras-attaque-regle-v1.md` (`88418df0…`), section « Hypothèse ».

## 2. Ce qui est fait

- **La règle est scellée** (`88418df0…`). Elle a eu trois contre-lectures et deux addenda. Son empreinte est déposée en
  privé chez un tiers, sur le projet OSF du programme, le 10 novembre 2026 (addendum 1, `edfa69a2…`).
- La règle fixe :
  - une échelle de six régimes d'accès, de l'attaquant aveugle à l'attaquant qui s'entraîne contre la sonde ;
  - quatre verdicts par cellule : « cassé », « entamé », « résiste », « non concluant », chacun avec ses deux
    intervalles exacts ;
  - des témoins qui décident si un régime se lit : une faille plantée, le nul « honnête contre honnête », l'attaque
    publiée reproduite ;
  - cinq classes de faille fixées avant toute attaque ;
  - une quarantaine à sens unique : les concepteurs de moniteurs ne reçoivent que la classe de la faille et l'hypothèse
    violée, jamais le texte de l'attaque.
- **Le témoin « attaque publiée reproduite »**, première étape, sur le banc des auteurs. La confirmation à 72 tours rend
  « effet reproduit sur le banc des auteurs, au régime publié », avec ses réserves. Tu as accepté ce verdict
  (GO-2026-11-19-51).
  Pièce : `runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/rapport-verdicts-temoin-bailey-v1.md` (`75db4cbd…`),
  branche `claude/compassionate-meitner-d4ryyk`.

## 3. Ce qui n'est pas fait

- **Deuxième étape du témoin** : le même protocole sur notre modèle et notre harnais. Elle seule tient le témoin du
  régime « écriture des activations » (addendum 2, `prereg/bras-attaque-regle-v1-addendum-2.md`).
- **Scellement 2, les familles aveugles** : la conception a commencé le 21 novembre. Un Fable neuf qui n'a vu aucun
  moniteur écrit les familles, sans dépense. Tu l'as désigné par ton mot GO-2026-11-21-63, avec la réserve « auteur :
  une instance, non une personne ». Mandat : `docs/procedures/mandat-scellement-2-familles-aveugles-v1.md`
  (`8594376e…`).
- **Scellement 3, le gel des moniteurs** : il revient aux concepteurs de moniteurs.
- **Aucune course du bras** n'a été lancée contre un moniteur du programme.

## 4. Phrases honnêtes pour le jury

- « Avant le gel des moniteurs, le pire cas informé n'est pas mesuré. » (règle, fin de la section « Hypothèse »)
- « La séparation entre concepteurs de moniteurs et attaquant n'est affirmable qu'une fois les familles aveugles
  scellées. Elles sont en cours d'écriture, par une instance qui n'a vu aucun moniteur. »
- « Le témoin d'attaque publiée est reproduit sur le banc de ses auteurs ; pas encore sur le nôtre. »

## 5. À ne pas dire

- Aucun nom de mode, de famille ni de recette.
- Ne pas dire « nos moniteurs résistent » : aucune course n'a eu lieu.
