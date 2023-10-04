package Ateliers_de_programmation.Java.Atelier_1.Ex1;

public class DePipe extends De {
    // Valeur minimale du dé
    protected int valeurMin = 1;

    // Constructeur de dé pipé
    public DePipe(String nom, int nbFaces, int valeur) {
        super(nom, nbFaces);
        if (valeur > 0 && valeur <= nbFaces) {
            valeurMin = valeur;
        } else {
            System.out
                    .println("Création de " + nom + " impossible : la valeur du dé pipé doit être comprise entre 1 et "
                            + nbFaces);
        }
    }

    // Méthode pour lancer un dé pipé
    public int lancer() {
        int resultat;

        do {
            resultat = super.lancer();
        } while (resultat < valeurMin);
        return resultat;
    }
}
