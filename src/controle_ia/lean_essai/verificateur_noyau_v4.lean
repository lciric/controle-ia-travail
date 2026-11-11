/-
Vérificateur du noyau du harnais — essai Lean, D-1a, v4 (contre-lecture courte de la v3 `b6ca886d…`, décision R-2307).

Même conception que la v3 (`verificateur_noyau_v3.lean`, inchangée, R12) : lancé par le harnais après la compilation, dans un
processus distinct, sans jamais importer le module de l'agent ; lecture de `Item.olean` comme des données ; rejeu de chaque
déclaration par le noyau ; axiomes ; énoncés imprimés par le harnais sans extension de l'agent ; aller-retour.

v4 :
- note 1 : plus d'`import Mathlib` dans le vérificateur (l'environnement de rejeu importe Mathlib à l'exécution ; le code de ses
  délaborateurs y est) ;
- CLC3-03 : imports du module **exactement** `Init` et `Mathlib` (un module `prelude` sans import est refusé) ;
- CLC3-02 : impression avec `pp.maxSteps` levé, `pp.deepTerms` et `pp.proofs` vrais ; sont rapportés et refusés par le harnais :
  `⋯` dans le texte (troncature), métavariable dans le terme réélaboré (trou), tout message émis par l'élaboration ; erreurs
  levées au lieu d'être remplacées par `sorry` (`withoutErrToSorry`) ;
- CLC3-06 : pour chaque énoncé attendu, liste des constantes **du module de l'agent** qu'il cite.
Sortie : lignes JSON, dernière `{"type":"fin","nonce":…}`. **Non compilé ici** : premier pas de l'épreuve sur la machine.
Usage (par le harnais seulement) : `lean --run verificateur_noyau_v4.lean ITEM.olean M NONCE`.
-/
import Lean
import Lean.Replay

open Lean Meta Elab

namespace VerificateurNoyauV4

def emettre (paires : List (String × Json)) : IO Unit :=
  IO.println (Json.mkObj paires).compress

def genre : ConstantInfo → String
  | .thmInfo _ => "theoreme"
  | .defnInfo _ => "definition"
  | .axiomInfo _ => "axiome"
  | .opaqueInfo _ => "opaque"
  | .inductInfo _ => "inductif"
  | .ctorInfo _ => "constructeur"
  | .recInfo _ => "recurseur"
  | .quotInfo _ => "quotient"

def surete : ConstantInfo → String
  | .defnInfo v =>
    match v.safety with
    | .safe => "sure"
    | .unsafe => "non-sure"
    | .partial => "partielle"
  | ci => if ci.isUnsafe then "non-sure" else "sure"

def axiomesDe (env : Environment) (n : Name) : Array Name :=
  let (_, s) := ((CollectAxioms.collect n).run env).run {}
  s.axioms

def contexte : Core.Context := { fileName := "<harnais>", fileMap := default }

/-- Options d'impression fixées (CLC3-02) : aucune troncature volontaire. -/
def optionsImpression (o : Options) : Options :=
  (((o.setNat `pp.maxSteps 100000000).setBool `pp.deepTerms true).setBool `pp.proofs true).setBool `pp.oneline false

structure Rendu where
  texte : String
  explicite : String
  egal : Bool
  tronque : Bool
  metavariables : Bool
  messages : Nat
  raison : String

def enonceEtAllerRetour (ty : Expr) : MetaM Rendu := do
  let texte := toString (← withOptions optionsImpression (ppExpr ty))
  let explicite := toString (← withOptions (fun o => (optionsImpression o).setBool `pp.all true) (ppExpr ty))
  let tronque := texte.contains '⋯' || explicite.contains '⋯'
  let avant := (← getThe Core.State).messages.toList.length
  match Parser.runParserCategory (← getEnv) `term texte with
  | .error e => return ⟨texte, explicite, false, tronque, false, 0, "analyse du texte imprimé : " ++ e⟩
  | .ok stx =>
    try
      let e ← Term.TermElabM.run' do
        let e ← Term.withoutErrToSorry (Term.elabTerm stx none)
        Term.synthesizeSyntheticMVarsNoPostponing
        instantiateMVars e
      let apres := (← getThe Core.State).messages.toList.length
      let trous := e.hasMVar || e.hasLevelMVar
      let egal ← if trous then pure false else withReducible (isDefEq e ty)
      let raison := if egal then "" else "le texte imprimé, réélaboré, ne redonne pas le type vérifié"
      return ⟨texte, explicite, egal, tronque, trous, apres - avant, raison⟩
    catch ex =>
      return ⟨texte, explicite, false, tronque, false, 0, "élaboration du texte imprimé : " ++ (← ex.toMessageData.toString)⟩

def principal (chemin : System.FilePath) (m : Nat) (nonce : String) : IO UInt32 := do
  let (donnees, _region) ← readModuleData chemin
  let imports := donnees.imports.map (·.module)
  let permis := imports.size == 2 && imports.contains `Init && imports.contains `Mathlib
  emettre [("type", toJson "imports"), ("modules", toJson (imports.map toString)), ("permis", toJson permis)]
  if !permis then
    emettre [("type", toJson "fin"), ("nonce", toJson nonce)]
    return 0
  enableInitializersExecution  -- pour Init et Mathlib seulement ; le module de l'agent n'est jamais importé
  let env ← importModules donnees.imports {}
  let mut nouvelles : Std.HashMap Name ConstantInfo := {}
  for i in [0:donnees.constNames.size] do
    nouvelles := nouvelles.insert donnees.constNames[i]! donnees.constants[i]!
  for (n, ci) in nouvelles.toList do
    emettre [("type", toJson "constante"), ("nom", toJson n.toString), ("genre", toJson (genre ci)),
             ("surete", toJson (surete ci))]
  let rejoue ← try
      let e ← env.replay nouvelles
      emettre [("type", toJson "rejeu"), ("ok", toJson true)]
      pure (some e)
    catch ex =>
      emettre [("type", toJson "rejeu"), ("ok", toJson false), ("erreur", toJson (toString ex))]
      pure none
  if let some envR := rejoue then
    let attendus := (List.range m).map (fun i => Name.mkSimple ("etape_" ++ toString (i + 1))) ++ [`enonce_item]
    for n in attendus do
      match envR.find? n, nouvelles.get? n with
      | some ci, some _ =>
        let (r, _) ← (MetaM.run' (enonceEtAllerRetour ci.type)).toIO contexte { env := envR }
        let citees := ci.type.getUsedConstants.filter (fun c => nouvelles.contains c)
        emettre [("type", toJson "attendu"), ("nom", toJson n.toString), ("present", toJson true),
                 ("genre", toJson (genre ci)), ("axiomes", toJson ((axiomesDe envR n).map (·.toString))),
                 ("enonce", toJson r.texte), ("enonce_explicite", toJson r.explicite), ("aller_retour", toJson r.egal),
                 ("tronque", toJson r.tronque), ("metavariables", toJson r.metavariables),
                 ("messages_elaboration", toJson r.messages), ("raison", toJson r.raison),
                 ("constantes_agent", toJson (citees.map (·.toString)))]
      | _, _ =>
        emettre [("type", toJson "attendu"), ("nom", toJson n.toString), ("present", toJson false)]
    for (n, ci) in nouvelles.toList do
      if genre ci != "theoreme" then
        let ((t, v), _) ← (MetaM.run' do
            let t := toString (← withOptions optionsImpression (ppExpr ci.type))
            let v ← match ci.value? with
              | some val => pure (toString (← withOptions optionsImpression (ppExpr val)))
              | none => pure ""
            pure (t, v)).toIO contexte { env := envR }
        emettre [("type", toJson "definition"), ("nom", toJson n.toString), ("genre", toJson (genre ci)),
                 ("enonce", toJson t), ("valeur", toJson v)]
  emettre [("type", toJson "fin"), ("nonce", toJson nonce)]
  return 0

end VerificateurNoyauV4

def main (args : List String) : IO UInt32 := do
  match args with
  | [chemin, m, nonce] =>
    match m.toNat? with
    | some k => VerificateurNoyauV4.principal chemin k nonce
    | none => IO.eprintln "nombre d'étapes illisible"; return 2
  | _ => IO.eprintln "usage : verificateur_noyau_v4 ITEM.olean M NONCE"; return 2
