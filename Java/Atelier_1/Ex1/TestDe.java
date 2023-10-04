package Ateliers_de_programmation.Java.Atelier_1.Ex1;

public class TestDe {
    public static void main(String[] args) {
        // Création de dés
        De de1 = new De();
        De de2 = new De("EqualsTest", 12);
        De de3 = new De("Dé 3");
        De de4 = new De("Dé 4", 8);
        De de5 = new De("Dé 5", 2);
        De de6 = new DePipe("Triche", 20, 15);
        De de7 = new De("EqualsTest", 12);

        // Manipulation des dés
        System.out.println(de1.getNom() + " a " + de1.getNbFaces() + " faces.");
        System.out.println(de2.getNom() + " a " + de2.getNbFaces() + " faces.");
        System.out.println(de3.getNom() + " a " + de3.getNbFaces() + " faces.");
        System.out.println(de4.getNom() + " a " + de4.getNbFaces() + " faces.");
        System.out.println(de5.getNom() + " a " + de5.getNbFaces() + " faces.");
        de4.setNbFaces(10);
        System.out.println(de4.getNom() + " a " + de4.getNbFaces() + " faces.");
        System.out.println(de6.getNom() + " a " + de6.getNbFaces() + " faces.");
        System.out.println("Il y a " + de1.getNbrDe() + " dés.");

        // Lancer des dés
        System.out.println("\nLancer de " + de1.getNom());
        System.out.println("La nouvelle valeur de " + de1.getNom() + " est : " + de1.lancer());
        System.out.println("\nLancer de " + de1.getNom());
        System.out.println("La nouvelle valeur de " + de1.getNom() + " est : " + de1.lancer());
        System.out.println("\nLancer de " + de6.getNom());
        System.out.println("La nouvelle valeur de " + de6.getNom() + " est : " + de6.lancer());

        // toString et equals
        System.out.println("\n" + de1.toString());
        System.out.println(de7.equals(de2));
    }
}
