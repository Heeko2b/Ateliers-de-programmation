package Ateliers_de_programmation.Java.Atelier_0.Ex1;

public class Robot {
    // Référence du robot
    String ref;
    // Nom du robot
    String nom;
    // Coordonnées du robot (axe x y)
    int x;
    int y;
    // Orientation du robot (nord = 1, est = 2, sud = 3, ouest = 4)
    int orientation;
    // Nombre total de robots crées
    static int nbrRobots = 0;

    public Robot(String nom, int x, int y, int orientation) {
        // Récupération des paramètres
        this.nom = nom;
        this.x = x;
        this.y = y;
        this.orientation = orientation;

        // Référence générée automatiquement(ROB1, ROB2, ...)
        nbrRobots += 1;
        ref = "ROB" + nbrRobots;
    }

    public Robot(String nom) {
        // Récupération du nom
        this.nom = nom;

        // x et y aux valeurs par défaut
        x = 0;
        y = 0;

        // Référence générée automatiquement(ROB1, ROB2, ...)
        nbrRobots += 1;
        ref = "ROB" + nbrRobots;

        // Orienté vers le nord par défaut
        orientation = 1;
    }

    void modifOrientation(int modif) {
        orientation = modif;
    }

    void deplacer() {
        if (orientation == 1) {
            y += 1;
        } else if (orientation == 2) {
            x += 1;
        } else if (orientation == 3 && y > 0) {
            y -= 1;
        } else if (orientation == 4 && x > 0) {
            x -= 1;
        }
    }

    void afficheToi() {
        System.out.println("Nom :" + this.nom);
        System.out.println("Référence :" + this.ref);
        System.out.println("Coordonnées :" + this.x + " " + this.y);
        System.out.println("Direction :" + this.orientation + "\n");
    }

    // méthode toString fait maison
    public String toString() {
        return "Description du robot :\nNom :" + this.nom + "\nRéférence :" + this.ref + "\nCoordonnées :" + this.x
                + " " + this.y
                + "\nDirection :" + this.orientation + "\n";
    }
}