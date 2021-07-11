#include <iostream>

int main(){

    int a = 5;
    int *p;
    p = &a;

    std::cout <<"a = "<< a << std::endl;
    std::cout <<"p = "<< p << "\n" << std::endl;

    //! endl doesn't occupy any memory whereas \n is character so It occupy 1 byte memory.
    
    std::cout <<"&a = "<< &a << std::endl;
    std::cout <<"&p = "<< &p << "\n" << std::endl;

    std::cout <<"*p = "<< *p << std::endl; //dereferencing of pointer
    
    *p = 10;

    std::cout <<"a = "<< a << std::endl;
    std::cout <<"*p = "<< *p << std::endl;


}