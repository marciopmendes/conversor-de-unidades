# Conversor de Unidades de Concentração
Conversor de grandezas para laboratorio de meio ambiente. A ideia do app é facilitar o trabalho da equipe de laboratório de meio ambiente da Arcelor Mittal Tubarão, permitindo a transformação rápida entre as unidades de concentração mais usuais na área da química.

O aplicativo foi desenvolvido em linguagem Python 3.10, utilizando a biblioteca Kivy 2.1.0.

Premissas do uso do app:
*   Sistema operacional Android;
*   Entrada do valor a ser convertido: somente caracteres numéricos, podendo ser inteiros ou decimais. No caso de decimais, utilizar o . (ponto) como separador;
*   Selecionar a unidade de entrada clicando no botão para exibir a lista de unidades disponíveis;
*   Selecionar a unidade de saída, repetindo o mesmo procedimento da unidade de entrada.
    - A unidade de entrada não aparecerá na lista de saída, uma vez que não faz sentido converter uma unidade para ela mesma.
*   Baseado nas unidades escolhidas, caso seja necessário, os campos de densidade e/ou massa molar serão habilitados;
*   A entrada de dados segue a mesma regra: somente numéricos, podendo ser inteiros ou decimais;
*   Uma vez inseridos todos os dados, clicar no botão converter;
*   O resultado será exibido abaixo do botão de conversão.
  
