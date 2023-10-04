package Ateliers_de_programmation.Java.Atelier_1.Ex2;

public class Entier {
    public int valeur;
    private int valMin;
    private int valMax;

    // Constructeur par défaut
    public Entier(int valeur, int valMin, int valMax) {
        this.valeur = valeur;
        this.valMin = valMin;
        this.valMax = valMax;
    }

    // Constructeur sans valeur
    public Entier(int valMin, int valMax) {
        this(0, valMin, valMax);
    }

    // Méthode pour modifier la valeur de l'entier
    public int setValeur(int newValeur) {
        if (newValeur >= valMin && newValeur <= valMax) {
            valeur = newValeur;
        } else {
            System.out.println("La valeur doit être comprise entre " + valMin + " et " + valMax);
        }
        return valeur;
    }
}
