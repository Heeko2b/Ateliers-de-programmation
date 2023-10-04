package Ateliers_de_programmation.Java.Atelier_1.Ex2;

import java.util.Random;

public class EntierFou extends Entier {

    // Attributs
    public int niveauDeFolie;
    Random r = new Random();

    // Constructeur par défaut
    public EntierFou(int valeur, int valMin, int valMax, int niveauDeFolie) {
        super(valeur, valMin, valMax);
        this.niveauDeFolie = niveauDeFolie;
    }

    // Constructeur sans valeur
    public EntierFou(int valMin, int valMax, int niveauDeFolie) {
        super(valMin, valMax);
        this.niveauDeFolie = niveauDeFolie;
    }

    // Méthode d'incrémentation d'EntierFou
    public int incremente() {
        if (this.valeur < this.valMax) {
            // Génération d'un nombre aléatoire entre 1 et niveauDeFolie
            int nbAleatoire = r.nextInt(this.niveauDeFolie) + 1;
            this.valeur += nbAleatoire;
        } else {
            System.out.println("La valeur ne peut pas être supérieure à " + valMax);
        }
        return this.valeur;
    }

}
