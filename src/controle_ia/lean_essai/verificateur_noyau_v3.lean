/-
Vérificateur du noyau du harnais — essai Lean, D-1a, v3 (décision de la mère après la contre-lecture courte, R-2302).

Garde de fond, défense principale et obligatoire (G-L8). Lancé par le harnais **après** la compilation du fichier de l'agent,
dans un processus distinct (`lean --run`, dans le bac), avec un `LEAN_PATH` qui ne contient **pas** le dossier de l'item :
- il **n'importe jamais** le module de l'agent : il lit les données de `Item.olean` (`readModuleData`), sans exécuter aucun code
  de l'agent (ni initialiseur, ni attribut, ni extension) ;
- il vérifie que les imports déclarés par le module sont dans la liste permise, puis construit l'environnement de ces seuls
  imports (code de Mathlib, épinglé et de confiance) ;
- il **rejoue chaque déclaration** du module dans le noyau (`Lean.Environment.replay`) : une déclaration ajoutée hors du noyau
  pendant la compilation (option `debug.skipKernelTC` posée par programme, `simproc`, `run_cmd`, fichier `.olean` réécrit) est
  rejetée ici ;
- pour chaque énoncé attendu (`etape_1` … `etape_m`, `enonce_item`) : genre, axiomes (`CollectAxioms` sur l'environnement
  rejoué), énoncé **imprimé par le harnais** dans un environnement où aucune extension de l'agent n'est chargée (ni instance,
  ni notation, ni délaborateur de l'agent), puis **aller-retour** : ce texte, réélaboré par le harnais, doit redonner le type
  vérifié (`isDefEq` en transparence réductible) ; l'égalité se juge sur les termes, jamais sur le texte ;
- chaque constante non théorème du module est imprimée (type et valeur) pour le relecteur.
Sortie : une ligne JSON par fait sur la sortie standard, dernière ligne `{"type":"fin","nonce":…}`. Code 0 si le travail est
allé au bout (le verdict se lit dans les lignes), 2 si les arguments sont illisibles.

Usage (par le harnais seulement) : `lean --run verificateur_noyau_v3.lean ITEM.olean M NONCE`.
**Non compilé ici** (aucune chaîne Lean dans la session) : premier pas de l'épreuve sur la machine (`epreuve_isolement_v3
noyau`), avec les items qui le prouvent ; interfaces de Lean écrites de mémoire (`readModuleData`, `importModules`,
`Environment.replay`, `CollectAxioms`, `Parser.runParserCategory`) : à confirmer sur la chaîne épinglée.
-/
import Mathlib
import Lean
import Lean.Replay

open Lean Meta Elab

namespace VerificateurNoyauV3

def racinesPermises : Array Name :=
  #[`Init, `Mathlib, `Batteries, `Aesop, `Qq, `Std, `Plausible, `ImportGraph, `ProofWidgets, `LeanSearchClient]

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

/-- Énoncé imprimé par le harnais, forme explicite, et aller-retour par réélaboration. -/
def enonceEtAllerRetour (ty : Expr) : MetaM (String × String × Bool × String) := do
  let texte := toString (← ppExpr ty)
  let explicite := toString (← withOptions (fun o => o.setBool `pp.all true) (ppExpr ty))
  match Parser.runParserCategory (← getEnv) `term texte with
  | .error e => return (texte, explicite, false, "analyse du texte imprimé : " ++ e)
  | .ok stx =>
    try
      let e ← Term.TermElabM.run' do
        let e ← Term.elabTerm stx none
        Term.synthesizeSyntheticMVarsNoPostponing
        instantiateMVars e
      let egal ← withReducible (isDefEq e ty)
      return (texte, explicite, egal, if egal then "" else "le texte imprimé, réélaboré, ne redonne pas le type vérifié")
    catch ex =>
      return (texte, explicite, false, "élaboration du texte imprimé : " ++ (← ex.toMessageData.toString))

def principal (chemin : System.FilePath) (m : Nat) (nonce : String) : IO UInt32 := do
  let (donnees, _region) ← readModuleData chemin
  let imports := donnees.imports.map (·.module)
  let permis := imports.all fun i => racinesPermises.contains i.getRoot
  emettre [("type", toJson "imports"), ("modules", toJson (imports.map toString)), ("permis", toJson permis)]
  if !permis then
    emettre [("type", toJson "fin"), ("nonce", toJson nonce)]
    return 0
  enableInitializersExecution  -- pour les imports permis (Mathlib…), jamais pour le module de l'agent, qui n'est pas importé
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
        let ((texte, explicite, egal, raison), _) ← (MetaM.run' (enonceEtAllerRetour ci.type)).toIO contexte { env := envR }
        emettre [("type", toJson "attendu"), ("nom", toJson n.toString), ("present", toJson true),
                 ("genre", toJson (genre ci)), ("axiomes", toJson ((axiomesDe envR n).map (·.toString))),
                 ("enonce", toJson texte), ("enonce_explicite", toJson explicite), ("aller_retour", toJson egal),
                 ("raison", toJson raison)]
      | _, _ =>
        emettre [("type", toJson "attendu"), ("nom", toJson n.toString), ("present", toJson false)]
    for (n, ci) in nouvelles.toList do
      if genre ci != "theoreme" then
        let ((t, v), _) ← (MetaM.run' do
            let t := toString (← ppExpr ci.type)
            let v ← match ci.value? with
              | some val => pure (toString (← ppExpr val))
              | none => pure ""
            pure (t, v)).toIO contexte { env := envR }
        emettre [("type", toJson "definition"), ("nom", toJson n.toString), ("genre", toJson (genre ci)),
                 ("enonce", toJson t), ("valeur", toJson v)]
  emettre [("type", toJson "fin"), ("nonce", toJson nonce)]
  return 0

end VerificateurNoyauV3

def main (args : List String) : IO UInt32 := do
  match args with
  | [chemin, m, nonce] =>
    match m.toNat? with
    | some k => VerificateurNoyauV3.principal chemin k nonce
    | none => IO.eprintln "nombre d'étapes illisible"; return 2
  | _ => IO.eprintln "usage : verificateur_noyau_v3 ITEM.olean M NONCE"; return 2
