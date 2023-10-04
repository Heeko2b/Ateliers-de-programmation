package Ateliers_de_programmation.Java.Atelier_0.Ex2;

public class Vecteur3D {
    int x;
    int y;
    int z;

    public Vecteur3D(int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public Vecteur3D() {
        this.x = 0;
        this.y = 0;
        this.z = 0;
    }

    // méthode sans paramètre qui a pour résultat un nombre réel représentant la
    // norme du vecteur
    public double norme() {
        return Math.sqrt(x * x + y * y + z * z);
    }

    // méthode produitScalaire ayant pour résultat un nombre réel représentant le
    // produit scalaire de deux vecteurs

}
