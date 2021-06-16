 /*
    De Gatos y Ratones
    Juarez Perez Hugo
    15/06/2021
 */
 
#include <thread>
#include <iostream>
#include <semaphore>
#include <vector>

//Comportamiento de los elementos

std::counting_semaphore< 2 > Plato(0);

void Gatear(int ID) {
    while (1) {

        //ESPERANDO
        std::cout << "\n#" << ID << " Esperando" << std::endl;
        //HAY RATON?

        std::cout << "\n#" << ID << " Habra raton?" << std::endl;
        //Come
        Plato.acquire();
        std::cout << "\n#" << ID << " Comiendo..." << std::endl;
        //Si hay raton, COMER... :(

        //IRSE
        Plato.release();
        std::cout << "\n#" << ID << " Me voy!" << std::endl;
        
    }

    
    
}



void Raton() {
    //ESPERANDO

    //HAY GATO?

    //COMER

    //IRSE

}


 int main(){

    //K gatos = 4
    //I Ratones = 2
    //M platos = 2

     Plato.release();


        

         std::thread Gatohilo1(Gatear, 1);
         std::thread Gatohilo2(Gatear, 2);


 



    std::binary_semaphore platosLibres(0);
    

    Gatohilo1.join();
    Gatohilo2.join();
    
     return 0;
 }
