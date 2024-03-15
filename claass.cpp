 /friend function
include<iostream>
include<string>

using namespace std;

void display(); //function prototype

class Human {
    private: //private attr of the class
        int age;
        int salary;
        string name;
    public:
        Human(int iage,int isal,string iname) {
            age=iage;
            salary=isal;
            name=iname;
        }
    void tell(){
        cout<<age<<salary<<endl<<name<<endl;
    }
       
    friend void display(Human *Raja); //friend function of class Human which can access the private and protected attr and methods of the class Human    
    //friend function takes class object as argument

};

//friend function defination
void display(Human *Raja) {
   
    cout<<"name: " <<Raja->name<<","<<"salary : "<<Raja->salary<<", "<<"age:"<<Raja->age<<endl;
}


int main() {
   
    Human *obj=new Human(20,2004444,"Raja");
    display(obj);
   
   
return 0;
   
}