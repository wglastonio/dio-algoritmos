import java.util.Scanner;

public class Classifier {
    public static void main(String[] args) {
        String level;
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter hero name: ");
        String hero_name = input.nextLine();
        
        System.out.print("Enter hero xp: ");
        int hero_xp = input.nextInt();

        input.close();

        if (hero_xp > 10000) {
            level = "Radiante";
        } else if (hero_xp > 9000) {
            level = "Imortal";
        } else if (hero_xp > 8000) {
            level = "Ascendente";
        } else if (hero_xp > 7000) {
            level = "Platina";
        } else if (hero_xp > 5000) {
            level = "Ouro";
        } else if (hero_xp > 2000) {
            level = "Prata";
        } else if (hero_xp > 1000) {
            level = "Bronze";
        } else {
            level = "Ferro";
        }
        System.out.println("O Herói de nome " + hero_name + " está no nível de " + level);
    }
}