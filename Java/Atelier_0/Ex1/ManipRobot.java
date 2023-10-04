package Ateliers_de_programmation.Java.Atelier_0.Ex1;

public class ManipRobot {
    public static void main(String args[]) {

        Robot toto = new Robot("Toto", 10, 20, 3);

        Robot titi = new Robot("Titi");

        toto.afficheToi();
        titi.afficheToi();

        // Mouvements pour toto
        toto.modifOrientation(4);
        toto.deplacer();
        toto.afficheToi();

        // Mouvements pour titi
        titi.deplacer();
        titi.modifOrientation(2);
        titi.deplacer();
        titi.afficheToi();
        // System.out.println(titi.myToString());

        System.out.println(toto.toString());
        System.out.println(titi);
    }
}