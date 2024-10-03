// Escreva uma classe chamada Angulo. Suas instâncias deverão ser capazes de 
// armazenar um valor angular expresso em graus (este será o único atributo). Todas as 
// validações cabíveis de serem realizadas por seus métodos deverão ser feitas e 
// exceções deverão ser lançadas no caso de incorretudes serem detectadas.
//  Escreva um construtor que, recebendo um valor angular expresso em graus, o 
// armazena internamente;
//  Escreva métodos de instância chamadas getValorEmGraus, getValorEmGrados
// e getValorEmRadianos que, sem receber parâmetros, retornam, respectivamente, 
// o valor angular do objeto expresso em graus, grados e radianos

package treinosemestre4.exerciciosprova;

public class Angulo implements Comparable<Angulo>, Cloneable{
    private double angulo;
    private final double pi = 3.14;

    private static boolean isValida(double angulo) {
        if (angulo < 0 || angulo > 360 ) { return false; }
        return true;
    }

    public Angulo(double angulo) throws Exception {
        if(!Angulo.isValida(angulo)) {
            throw new Exception("Valor de angulo invalido");
        }

        this.angulo = angulo;

        //ou

        //this.setAngulo(angulo);
    }

    public double getValorEmGraus() {
        return this.angulo;
    }

    public void setAngulo(double angulo) throws Exception {
        if(!Angulo.isValida(angulo)) { throw new Exception("Valor de angulo invalido"); }
        this.angulo = angulo;

        //ou

        //if(angulo < 0 || angulo > 360 ) { throw new Exception'("Valor de angulo invalido"); }
        //this.angulo = angulo;
    }

    public double getValorEmGrados() {
        return this.angulo * 1.1111;
    }

    public void setValorEmGrados(double grados) throws Exception {
        double anguloEmGraus = grados / 1.1111;
        if(!Angulo.isValida(anguloEmGraus)) { throw new Exception("Valor de angulo invalido"); }
            this.angulo = anguloEmGraus;

        // ou

        //if(angulo < 0 || angulo > 360 ) { throw new Exception'("Valor de angulo invalido"); }
        //this.angulo = anguloEmGraus
    }

    public double getValorEmRadianos() {
        return this.angulo * pi / 180;
    }

    public void setValorEmRadianos(double radiano) throws Exception {
        double anguloEmGraus = radiano * 180 / pi;
        if(!Angulo.isValida(anguloEmGraus)) { throw new Exception("Valor de angulo invalido"); }
        this.angulo = anguloEmGraus;

        // ou

        //if(anguloEmGraus < 0 || anguloEmGraus > 360 ) { throw new Exception'("Valor de angulo invalido"); }
        //this.angulo = anguloEmGraus
    }

    public String toString() {
        return ("Angulo em graus: " + this.getValorEmGraus() + 
               "\nAngulo em grados: " + this.getValorEmGrados() +
               "\nAngulo em radianos: " + this.getValorEmRadianos());
    }

}
