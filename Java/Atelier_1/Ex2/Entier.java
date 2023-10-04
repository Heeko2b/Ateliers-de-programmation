package Ateliers_de_programmation.Java.Atelier_1.Ex2;

public class Entier {

    // Attributs
    public int valeur;
    protected int valMin;
    protected int valMax;

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

    // Méthode pour incrémenter la valeur de l'entier
    public int incremente() {
        if (this.valeur < this.valMax) {
            this.valeur++;
        } else {
            System.out.println("La valeur ne peut pas être supérieure à " + valMax);
        }
        return this.valeur;
    }

    // Méthode d'incrémentation par pas de la valeur de l'entier
    public int incremente(int pas) {
        if (this.valeur + pas <= this.valMax) {
            this.valeur += pas;
        } else {
            System.out.println("La valeur ne peut pas être supérieure à " + valMax);
        }
        return this.valeur;
    }

    // Redéfinition de toString
    public String toString() {
        return "Cet entier a pour valeur " + this.valeur + " et est compris entre " + this.valMin
                + " et " + this.valMax + ".";
    }

    // Redéfinition de equals
    public boolean equals(Object o) {
        boolean result = false;
        if (o != null && o instanceof Entier) {
            Entier ent = (Entier) o;
            result = ((this.valeur == ent.valeur) && (this.valMin == ent.valMin)
                    && (this.valMax == ent.valMax));
        }
        return result;
    }
}
