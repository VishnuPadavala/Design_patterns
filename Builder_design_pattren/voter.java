public class voter{
    public String name;
    public int age;
    public voter(Builder builder){
        this.name=builder.name;
        this.age=builder.age;
    }
    public static Builder getbuilder(){
        return new Builder();
    }
    public static class Builder{
        public String name;
        public int age;
        public Builder setName(String name){
            this.name=name;
            return this;
        }
        public Builder setAge(int age){
            this.age=age;
            return this;
        }
        public voter build(){
            if(age<18){
                throw new IllegalArgumentException("Age must be at least 18");
            }
            return new voter(this);
        }
    }
    public void display(){
        System.out.println(this.name + " " + this.age);
    }
}