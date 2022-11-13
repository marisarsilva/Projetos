package poo;

/**
 * Numero
 */
public class Numero {

    private double x;

    private double getx() {
        return x;

    }

    private void setx(double x) {
        this.x = x;

    }

    public double soma(double x, double y) {
        setx(x + y);
        return getx();

    }

    public double subtração(double x, double y) {
        setx(x - y);
        return getx();

    }

    public double multiplicação(double x, double y) {
        setx(x * y);
        return getx();

    }

    public double divisão(double x, double y) {
        setx(x / y);
        return getx();

    }

}