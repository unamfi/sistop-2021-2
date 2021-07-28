#include <stdio.h>

int main() {
  printf("Estoy iniciando main (%llx)\n", main);
  func1();
  func2();
}

void func1() {
  printf("Respondiendo desde func1 (%llx)\n", func1);
}

void func2() {
  printf("Respondiendo desde func2 (%llx)\n", func2);
}
