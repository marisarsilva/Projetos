package poo;

import java.util.HashMap;
import java.util.Scanner;

public class testaNumero {
    public static void main(String[] args) {
        
        Numero n = new Numero();
        boolean continuar = true;

        try (Scanner scan = new Scanner(System.in)) {
            while (continuar){
                double x=0;
                double y=0;
                int operação=0;


                System.out.println("Digite a Operação que deseja realizar:"
                +                      "\n1 para soma"
                +                      "\n2 para subtração"
                +                      "\n3 para multiplicação"
                +                      "\n4 para divisão"
                +                      "\n ou 0 para enserrar o programa"

                );

                operação = scan.nextInt();

                if(operação==0){
                    continuar=false;
                    return;
                }

                System.out.println("informe o valor do primeiro numero");
                x=scan.nextInt();
                System.out.println("informe o valor do segundo numero");
                y=scan.nextInt();


                switch (operação) {
                    case 1:
                        imprimeCalculadora(operação, n.soma(x,y), x, y);

                        break;
                    case 2:
                        imprimeCalculadora(operação, n.subtração(x,y), x, y);
                        
                        break;
                    case 3:
                        imprimeCalculadora(operação, n.multiplicação(x,y), x, y);
                        
                        break;
                    case 4:
                        imprimeCalculadora(operação, n.divisão(x,y), x, y);
                     
                        break;
                
   
                }


            }


            
            
        }
    }

    
    static void imprimeCalculadora(int operação, double resultado, double x, double y ){
        HashMap< Integer, String> mapOperação = new HashMap<>();
        mapOperação.put(1,  "somado");
        mapOperação.put(2, "subtraido");
        mapOperação.put(3, "multiplicado");
        mapOperação.put(4, "dividido");

        System.out.println("\n o resultado de  " +x+mapOperação.get(operação)+" por "+ y + " é igual a "+ resultado+ "\n");
    }

    
}

