package be.fnord.DefaultLogic;

import java.util.HashSet;

import be.fnord.util.logic.DefaultReasoner;
import be.fnord.util.logic.WFF;
import be.fnord.util.logic.defaultLogic.DefaultRule;
import be.fnord.util.logic.defaultLogic.RuleSet;
import be.fnord.util.logic.defaultLogic.WorldSet;

public class TP2 {

	public static void exercice5() {
		
		// Initialisation des 3 Mondes
		
		// Monde W1
		WorldSet world1 = new WorldSet();
		world1.addFormula(a.e.NOT+"A");
		
		// Monde W2
		WorldSet world2 = new WorldSet();
		world2.addFormula("A");
		world2.addFormula(a.e.NOT+"B");
		
		// Monde W3
		WorldSet world3 = new WorldSet();
		world3.addFormula("A");
		world3.addFormula(a.e.NOT+"B"+a.e.AND+"C");
		
		
		// Déclaration des deux règles
		
		// règle d1
		DefaultRule rule1 = new DefaultRule();
		rule1.setPrerequisite("A");
		rule1.setJustificatoin("B");
		rule1.setConsequence("C");
		
		// règle d2
		DefaultRule rule2 = new DefaultRule();
		rule2.setPrerequisite("A");
		rule2.setJustificatoin("~C");
		rule2.setConsequence("D");
		
		
		// Création de l'ensemble de règles
		RuleSet myRules = new RuleSet();
		
		// Ajout des deux règles crées plus tôt à l'ensemble
		myRules.addRule(rule1);
		myRules.addRule(rule2);
		
		// Appel des raisonneurs pour générer les extensions possibles pour chacune des théories
		
		DefaultReasoner loader1 = new DefaultReasoner(world1, myRules);
		HashSet<String> extensions1 = loader1.getPossibleScenarios();
		
		a.e.println("Pour le monde suivant: \n\t" + world1.toString()
		+ "\n Et pour cet ensemble de règles: \n\t" + myRules.toString());
		
		if(extensions1.size() == 0) {
			a.e.println("Il n'y a pas d'extension possible.");
		}
		else {
			a.e.println("Les extensions possibles sont :");
		}
		for (String c : extensions1){
			a.e.println("\t Ext: Th(W U (" + c + "))");
			// Added closure operator
			a.e.incIndent();
			WFF world_and_ext = new WFF("(( " + world1.getWorld() + " ) & ("
					+ c + "))");
			a.e.println("= " + world_and_ext.getClosure());
			a.e.decIndent();
		
		}
		
		System.out.println("\n\n\n");
		
		
		DefaultReasoner loader2 = new DefaultReasoner(world2, myRules);
		HashSet<String> extensions2 = loader2.getPossibleScenarios();
		
		a.e.println("Pour le monde suivant: \n\t" + world2.toString()
		+ "\n Et pour cet ensemble de règles: \n\t" + myRules.toString());

		if(extensions2.size() == 0) {
			a.e.println("Il n'y a pas d'extension possible.");
		}
		else {
			a.e.println("Les extensions possibles sont :");
		}
		for (String c : extensions2){
			a.e.println("\t Ext: Th(W U (" + c + "))");
			// Added closure operator
			a.e.incIndent();
			WFF world_and_ext = new WFF("(( " + world1.getWorld() + " ) & ("
					+ c + "))");
			a.e.println("= " + world_and_ext.getClosure());
			a.e.decIndent();
		
		}
		
		
		System.out.println("\n\n\n");
		

		DefaultReasoner loader3 = new DefaultReasoner(world3, myRules);
		HashSet<String> extensions3 = loader3.getPossibleScenarios();
		
		a.e.println("Pour le monde suivant: \n\t" + world3.toString()
		+ "\n Et pour cet ensemble de règles: \n\t" + myRules.toString());

		if(extensions3.size() == 0) {
			a.e.println("Il n'y a pas d'extension possible.");
		}
		else {
			a.e.println("Les extensions possibles sont :");
		}
		for (String c : extensions3){
			a.e.println("\t Ext: Th(W U (" + c + "))");
			// Added closure operator
			a.e.incIndent();
			WFF world_and_ext = new WFF("(( " + world3.getWorld() + " ) & ("
					+ c + "))");
			a.e.println("= " + world_and_ext.getClosure());
			a.e.decIndent();
		
		}
	}
	
	
	public static void exemple() {
		WorldSet myWorld = new WorldSet();
		myWorld.addFormula("(B -> (~A & ~C))");

		DefaultRule rule1 = new DefaultRule();
		rule1.setPrerequisite(a.e.EMPTY_FORMULA);
		rule1.setJustificatoin("A");
		rule1.setConsequence("A");

		DefaultRule rule2 = new DefaultRule();
		rule2.setPrerequisite(a.e.EMPTY_FORMULA);
		rule2.setJustificatoin("B");
		rule2.setConsequence("B");

		DefaultRule rule3 = new DefaultRule();
		rule3.setPrerequisite(a.e.EMPTY_FORMULA);
		rule3.setJustificatoin("C");
		rule3.setConsequence("C");

		RuleSet myRules = new RuleSet();
		myRules.addRule(rule1);
		myRules.addRule(rule2);
		myRules.addRule(rule3);

		DefaultReasoner loader = new DefaultReasoner(myWorld, myRules);
		HashSet<String> extensions = loader.getPossibleScenarios();

		a.e.println("Pour le monde suivant: \n\t" + myWorld.toString()
		+ "\n Et pour cet ensemble de règles: \n\t" + myRules.toString());

		if(extensions.size() == 0) {
			a.e.println("Il n'y a pas d'extension possible.");
		}
		else {
			a.e.println("Les extensions possibles sont :");
		}
		for (String c : extensions) {
			a.e.println("\t Ext: Th(W U (" + c + "))");
			// Added closure operator
			a.e.incIndent();
			WFF world_and_ext = new WFF("(( " + myWorld.getWorld() + " ) & ("
					+ c + "))");
			a.e.println("= " + world_and_ext.getClosure());
			a.e.decIndent();

		}
	}
	
	
	public static void main(String[] args) {
		// Turn on the removal of empty effects from print statements
		a.e.HIDE_EMPTY_EFFECTS_IN_PRINT = true;
		exercice5();
		//exemple();
		System.out.println("Fini");
	}
}
