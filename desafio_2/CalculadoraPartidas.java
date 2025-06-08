package desafio_2;

import java.util.Scanner;

public class CalculadoraPartidas {
    public static void main(String[] args) {
        int saldo;
        String level;
        Scanner input = new Scanner(System.in);
        
        System.out.print("Entre quantidade de vitorias: ");
        int vitorias = input.nextInt();
        
        System.out.print("Entre quantidade de derrotas: ");
        int derrotas = input.nextInt();

        input.close();
        saldo = vitorias - derrotas;

        if (saldo > 101) {
            level = "Imortal";
        } else if (saldo > 90) {
            level = "Lendario";
        } else if (saldo > 80) {
            level = "Diamante";
        } else if (saldo > 50) {
            level = "Ouro";
        } else if (saldo > 20) {
            level = "Prata";
        } else if (saldo > 10) {
            level = "Bronze";
        } else {
            level = "Ferro";
        }
        System.out.println("O Herói tem saldo de " + saldo + " e está no nível de " + level);
    }
}