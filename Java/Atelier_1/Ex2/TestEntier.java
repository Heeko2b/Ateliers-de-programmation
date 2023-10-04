package Ateliers_de_programmation.Java.Atelier_1.Ex2;

public class TestEntier {
    public static void main(String[] args) {
        // Creation d'entiers
        Entier ent1 = new Entier(5, 0, 10);
        Entier ent2 = new Entier(5, 0, 10);
        Entier ent3 = new Entier(3, 0, 2);
        Entier ent4 = new Entier(4, 0, 5);
        Entier fou = new EntierFou(5, 0, 10, 4);

        // Manipulation des entiers

        // Incrémentation
        System.out.println("\nent1 = " + ent1.valeur);
        System.out.println("Incrémentation de ent1 : " + ent1.incremente() + "\n");

        // Incrémentation par pas
        System.out.println("ent1 = " + ent1.valeur);
        System.out.println("Incrémentation de ent1 par pas de 2 : " + ent1.incremente(2) + "\n");
        System.out.println("ent4 = " + ent4.valeur);
        System.out.println("Incrémentation de ent4 par pas de 2 : " + ent4.incremente(2) + "\n");

        // Incrémentation d'EntierFou
        System.out.println("fou = " + fou.valeur);
        System.out.println("Incrémentation de fou : " + fou.incremente() + "\n");

        // Méthode toString
        System.out.println(ent3);
        /*
         * // Ces deux prints font la même chose
         * System.out.println(ent1);
         * System.out.println(ent1.toString());
         */

        // Méthode equals
        System.out.println(ent1.equals(ent2));
        System.out.println(ent1.equals(ent4));

    }
}