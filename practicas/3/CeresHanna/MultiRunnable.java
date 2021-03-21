class MultiRunnable implements Runnable{  //Clase MultiRunnable implementada de la interfaz Runnable 
	public void run(){  //Método público run 
		System.out.println("thread is running...");  //Entra en estado runnable
		//El hilo se encuentra en ejecución
	}  
	  
	public static void main(String args[]){  
		MultiRunnable m1=new MultiRunnable();  //Se crea una instancia de la clase
		Thread t1 =new Thread(m1);  // Se crea una instancia del objeto m1 para crear un hilo a través de la clase Thread 
		t1.start();  //El objeto accede al método star (es llamado) 
	 }  
}  

//Se crea una clase implementada de la interfaz Runnable.
//Que permite producir hilos funcionales para otras clases.
//A través de el objeto m1 de nuestra clase, se crea un objeto Thread.
//Este objeto t1 es el encargado de ejecutar el método run, cuando llama al método start.
//Entonces es cuando el hilo entra en el estado runnable y esta en ejecución.
