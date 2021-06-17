 /*
    De Gatos y Ratones
    Juarez Perez Hugo
    15/06/2021
 */
 
#include <thread>
#include <iostream>
#include <semaphore>
#include <vector>
#include <chrono>



std::counting_semaphore<2>Plato(0);
std::binary_semaphore RatonesComiendo(0);
int Ratones_presentes, actualRatonID;

void Slow_Output() {
    std::this_thread::sleep_for(std::chrono::seconds(1));
}


//Comportamiento de los Gatos
void Gatear(int ID) {
    while (1) {
        
        //ESPERANDO
        std::cout << "\nGato #" << ID << " Esperando" << std::endl;
        Slow_Output();


        //Con esto ocacionamos el "caos" para que los ratones y los gatos se puedan encontrar. 
        RatonesComiendo.try_acquire();
        
        //HAY RATONES?
        std::cout << "\nGato #" << ID << " Habrá un ratón?" << std::endl;
        Slow_Output();

        //Torniquete para que entren a comer los ratones
        if (Ratones_presentes > 0 && actualRatonID != -1) {
            //std::cout << "\n ATRAPAAADA, Ratones presentes: " << Ratones_presentes << std::endl;
            std::cout << "\nGato #" << ID << ": Te debería comer, raton #" << actualRatonID << "pero no sé como, **zarpaso**" << std::endl;
            actualRatonID = -1;
            RatonesComiendo.release();
        }
            

        //COMER
        Plato.acquire();
        std::cout << "\nGato #" << ID << " Comiendo..." << std::endl;
        Slow_Output();
        
        //IRSE
        Plato.release();
       
        
        std::cout << "\nGato #" << ID << " Me voy!" << std::endl;
       
        RatonesComiendo.release();
        Slow_Output();
    }

    
    
}


//Comportamiento de los Ratones
void Raton(int ID) {

    while (1) {
        
        //ESPERANDO
        std::cout << "\nRaton #" << ID << " Esperando" << std::endl;
        Slow_Output();
       
        RatonesComiendo.acquire();
        std::cout << "\nRaton #" << ID << " No hay gatos?" << std::endl;
        Slow_Output();
        
        //COMER
        Plato.acquire();
        actualRatonID = ID;
        Ratones_presentes++;
        std::cout << "\nRaton #" << ID << " A Comer!" << std::endl;
        Slow_Output();
        
        //IRSE
        std::cout << "\nRaton #" << ID << " Me voy!" << std::endl;
        Slow_Output();


        Ratones_presentes--;
        Plato.release();
        RatonesComiendo.release();
    }
    
    
}


 int main(){

    //K gatos = 4
    //I Ratones = 2
    //M platos = 2

    Plato.release();
    std::thread Gatohilo1(Gatear, 1);
    std::thread Gatohilo2(Gatear, 2);
    std::thread Gatohilo3(Gatear, 3);
    std::thread Gatohilo4(Gatear, 4);
    std::thread RatiHilo1(Raton, 1);
    std::thread RatiHilo2(Raton, 2);


    Gatohilo1.join();
    Gatohilo2.join();
    Gatohilo3.join();
    Gatohilo4.join();
    RatiHilo1.join();
    RatiHilo2.join();

    
    return 0;
 }
