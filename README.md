Desafio Target Sistemas

1. Observe o trecho de código abaixo:

int INDICE = 13, SOMA = 0, K = 0;
enquanto K < INDICE faça
{
K = K + 1;
SOMA = SOMA + K;
}
imprimir(SOMA);

Ao final do processamento, qual será o valor da variável SOMA?

Resultado: __91__

2. Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

[Resposta questão 2:](estag-rb24/fibonacci.py)

3. Descubra a lógica e complete o próximo elemento:

a) 1, 3, 5, 7, __9__
b) 2, 4, 8, 16, 32, 64, __128__
c) 0, 1, 4, 9, 16, 25, 36, __49__
d) 4, 16, 36, 64, __92__
e) 1, 1, 2, 3, 5, 8, __13__
f) 2,10, 12, 16, 17, 18, 19, __200__

4. Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

Primeira visita: Ligo o primeiro interruptor e deixo ligado por alguns minutos, depois desligo. Ligo o segundo interruptor e deixo ligado. Mantenho o terceiro interruptor desligado durante todo o processo. Entrei na primeira sala das lâmpadas:

Se a lâmpada estiver acesa, então o segundo interruptor controla essa lâmpada.
Se a lâmpada estiver desligada e quente, o primeiro interruptor controla.
Se estiver desligada e fria, é o terceiro interruptor.

Segunda visita: Aqui eu já sei sobre a primeira sala, então vamos para a segunda. O resultado vai ser alguma das 3 opções, então é só fazer uma eliminatória, descobri a primeira e a segunda, a que sobrar fica pra terceira sala e interruptor.

5. Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;

[Resposta questão 5:](estag-rb24/inverter-string.py)
