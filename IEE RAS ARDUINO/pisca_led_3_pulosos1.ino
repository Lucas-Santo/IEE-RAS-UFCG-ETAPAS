// C++ code
//

const int LED1 = 13;

void setup()
{
  pinMode(LED1, OUTPUT);
}

void Piscar(int,float, int);

void loop()
{
  Piscar(LED1, 0.5, 2);
  delay(1000);
  Piscar(LED1, 0.2, 4);
  delay(500);
  Piscar(LED1, 0.15, 15);
  delay(250);
}

void Piscar(int pino, float delay_entre_ativacao, int quantidade){
  int delay_at = delay_entre_ativacao * 1000;  
  digitalWrite(pino, LOW);  
  for(int i = 0; i < quantidade; i++){
    digitalWrite(pino, HIGH);
    delay(delay_at);
    digitalWrite(pino, LOW);
    delay(delay_at);
  };
  digitalWrite(pino, LOW);
}