class singleton{
    private static singleton instance;
    private singleton(){
        System.out.println("singleton class constructot");
    }
    public static singleton getinstance(){
        if(instance ==null){
            instance = new singleton();
        }
        return instance;
    }
    public void show(){
        System.out.println("show fuction called");
    }
}
class Main{
    public static void main(String[] args){
        singleton s1=singleton.getinstance();
        singleton s2=singleton.getinstance();
        s1.show();
    }
}