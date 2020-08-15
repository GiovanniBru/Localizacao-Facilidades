<h1> Localização de UPAs </h1>
<p>&nbsp;&nbsp;&nbsp; Giovanni Bruno Travassos de Carvalho - 11506849</p>
<p><b>UFPB - 2019.4</b></p>
<p> O projeto consiste na modelagem e implementação de um problema de Programação Linear Inteira, localização de facilidades. Na temática, o problema consiste em aplicar os conhecimentos adquiridos na disciplina de Pesquisa Operacional, tendo em vista a modelagem do problema, definindo as restrições básicas. Por fim a implementação do programa, desenvolvida em Python, para que funcione em qualquer conjunto de dados e forneça a resposta completa. A implementação contou com auxílio da biblioteca de programação linear DOCPLEX(<i>Decision Optimization</i> CPLEX), e também a MATPLOTLIB para plotagem. </p>

 <h2> Sumário </h2> 
<ol>
	<li><a href="https://github.com/GiovanniBru/Localizacao-Facilidades#-defini%C3%A7%C3%A3o-do-problema-">Definição do Problema</a></li>
	<li><a href="https://github.com/GiovanniBru/Localizacao-Facilidades#modelagem">Modelagem</a></li>
	<li><a href="https://github.com/GiovanniBru/Localizacao-Facilidades#instru%C3%A7%C3%B5es">Instruções</a></li>
	<li><a href="https://github.com/GiovanniBru/Localizacao-Facilidades#-resultados-obtidos">Resultados Obtidos</a></li>
	<li><a href="https://github.com/GiovanniBru/Localizacao-Facilidades#dificuldades-e-melhorias">Dificuldades e Melhorias</a></li>
	<li><a href="https://github.com/GiovanniBru/Localizacao-Facilidades#refer%C3%AAncias">Referências</a></li>
</ol>

<h2> Definição do Problema </h2>
<p>No problema de Localização de UPAs, existem n distritos numa região metropolitana, cuja distância entre um distrito e outro é dada pela equação da distância euclidiana: </p>
<p align="center"><img src = "https://github.com/GiovanniBru/Localizacao-Facilidades/blob/master/imagens/distancia%20euclidiana.PNG"></p>
<p>Com isso deseja-se escolher em quais localidades as UPAs devem ser instaladas. Em regra, é obrigatório que se siga as seguintes restrições: </p> 
<ol>
  <li> Distância entre distrito e UPA mais próxima deve ser no máximo K km; </li>
  <li> Distância entre distrito e segunda UPA mais próxima deve ser no máximo Y km; </li>
  <li> Distância entre duas UPAs de no máximo Z km.</li>
</ol> 
<p>É necessário que suas respectivas saídas, para resolução do problema, contenha as seguintes indicações: </p>
<ol>
  <li> Saída 1 = Quais distritos foram instaladas UPAs;</li>
  <li> Saída 2 = Distância de cada distrito para a primeira e segunda UPA mais próxima.</li>
</ol>
<p> O objetivo do problema é buscar a minimização do número de UPAs, respeitando as restrições impostas.</p>

<h2>Modelagem</h2> 
<p>Para resolução do problema foi preciso criar <i>n</i> variáveis binárias que são representadas no distrito <i>n</i> existindo ou não uma UPA. Os valores de K, Y e Z são fornecidos no arquivo de entrada, assim como as coordenadas (X,Y) de cada distrito.</p>
<p align="center"><img src = "https://github.com/GiovanniBru/Localizacao-Facilidades/blob/master/imagens/modelagem.PNG"></p>
<p><b>(a)</b>Função Objetiva: Minimizar um somatório de todas as variáveis binárias para cada distrito;</p>
<p><b>(b)</b>Primeira Restrição: Para todo j pertencente a {1,...,n}, é feito um somatório das variáveis binárias, se a distância dij for menor que o valor K fornecido, cujo valor tem que ser maior ou igual a 1. Essa restrição indica que é preciso ter ao menos uma UPA dentro dessa distância mínima;</p>
<p><b>(c)</b>Segunda Restrição: Para todo j pertencente a {1,...,n}, é feito um somatório das variáveis binárias, se a distância dij for menor que o valor Y fornecido, cujo valor tem que ser maior ou igual a 2. Essa restrição indica que é preciso ter ao menos duas UPA dentro dessa distância mínima;</p>
<p><b>(d)</b>Terceira Restrição: Para todo i e j pertencente a {1,...,n}, se a distância dij for menor que Z, a soma das variáveis binárias tem que ser 1, ou seja, apenas um dos distritos poderá receber uma UPA;</p>
<p><b>(e)</b>Declaração das variáveis binárias.</p>

<h2>Instruções</h2>
<p>O projeto foi feito em Python no <b>Anaconda Navigator</b> com auxílio da biblioteca DOCPLEX. Para instalar a biblioteca, é preciso digitar o seguinte comando no <i>Prompt</i> do Anaconda ou no terminal do Linux: <b><i>$ pip install docplex</i></b>. </p>
<p>Essa biblioteca nos permite adicionar de forma rápida e fácil o poder de otimização do CPLEX, e possibilita modelar e resolver os problemas na API do Python.</p>
<p>Usamos também a biblioteca chamada Matplotlib,  o Anaconda já vem com esse recurso instalado, mas caso fosse usado outro ambiente, seria necessário instalá-la com o seguinte comando: <b><i>$ pip install matplotlib</b></i> ou <b><i>$conda install matplotlib</b></i>.
 
<h2> Resultados Obtidos</h2>
<p>O formato do arquivo de entrada foi definido da seguinte maneira:</p>
<ol>
  <li>n #Número de Distritos</li>
  <li>K #Distância mínima de um distrito para UPA mais próxima</li>
  <li>Y #Distância mínima de um distrito para segunda UPA mais próxima</li>
  <li>Z #Distância máxima de uma UPA para outra</li>
  <li>(x,y) #Coordenada de cada distrito</li>
</ol>
<p align="center"><img src = "https://github.com/GiovanniBru/Localizacao-Facilidades/blob/master/imagens/entrada2.PNG"></p>
<p align="center">Figura 1 - Exemplo de arquivo de entrada</p>
<p>Executando e printando o comando <i>export_to_string()</i> , conseguimos ver a modelagem feita pelo programa, e como resultado do exemplo de “entrada2.txt” obtivemos: </p>
<p align="center"><img src = "https://github.com/GiovanniBru/Localizacao-Facilidades/blob/master/imagens/teste1.PNG"></p>
<p align="center">Figura 2 - Comando "export_to_string()"</p>
<p>Podemos observar na execução desse comando, que a função objetiva descrita em <i>obj</i> foi feita corretamente, assim como as 30 restrições <i>c</i>, e as 10 variáveis binárias também foram criadas corretamente para o problema da entrada “entrada2.txt”.</p>
<p>Utilizamos o comando <i>print_information()</i> para obter outras informações sobre o modelo criado, como o número de variáveis e seu tipo, e o número de restrições e seu tipo. </p>
<p align="center"><img src = "https://github.com/GiovanniBru/Localizacao-Facilidades/blob/master/imagens/teste2.PNG"></p>
<p align="center">Figura 3 - Comando "print_information()"</p>
<p>Agora, executando o solver e printando sua solução através do comando <i>display()</i>, obtemos:</p>
<p align="center"><img src = "https://github.com/GiovanniBru/Localizacao-Facilidades/blob/master/imagens/teste3.PNG"></p>
<p align="center">Figura 4 - Comando "display()"</p>
<p>Através do comando acima podemos observar que o resultado da função objetiva em “objetive”, que para o arquivo de entrada “entrada2.txt” foi <b>5</b>. Também podemos observar as variáveis binárias com 1, que representam o distrito que receberá uma UPA. </p>
<p>Em seguida, printamos a saída da maneira que foi pedida no apêndice 2 da descrição do problema, mostrando em qual distrito serão localizadas as UPAs. </p>
<p align="center"><img src = "https://github.com/GiovanniBru/Localizacao-Facilidades/blob/master/imagens/teste4.PNG"></p>
<p align="center">Figura 5 - Saída do programa</p>
<p>Por fim, plotamos os distritos em um sistema de coordenadas, pintando o lugar que receberá UPA de vermelho, e os demais de preto: </p>
<p align="center"><img src = "https://github.com/GiovanniBru/Localizacao-Facilidades/blob/master/imagens/plot.PNG"></p>
<p align="center">Figura 6 - Distritos no sistema de coordenadas</p>

<h2>Dificuldades e Melhorias</h2>
<p>O primeiro problema encontrado foi na criação da segunda restrição, ao colocar ‘maior igual a 2’ alguns somatórios que só entraram duas variáveis deram erro, pois não era possível que uma variável binária fosse maior ou igual a 2.  Portanto deixamos a segunda restrição com ‘maior igual a 1’. </p>
<p>Tivemos dificuldade e por consequência não conseguimos printar corretamente a distância do distrito que não tem UPA para a UPA mais próxima, nem para segunda UPA mais próxima. </p>
<p>Por fim, para melhoria do projeto, também sugerimos plotar raios de valor K, Y e Z para cada distrito, facilitando a visualização do problema. Nessa mesma plotagem, é preciso ainda criar uma função que descubra os maiores valores de x e y para usar de coordenada na criação do sistema.  </p>

<h2>Referências</h2>
<li><a href="https://www.ibm.com/support/knowledgecenter/SSSA5P_12.8.0/ilog.odms.cplex.help/CPLEX/GettingStarted/topics/set_up/Python_setup.html">Setting up the Python API of CPLEX</a></li>
<li><a href="https://www.youtube.com/watch?v=hqGZzRh00y0&list=PL_wz_RHE6pEYEJO-vDNwHi2F7k-WNgOfQ">Vídeo aulas do professor Sérgio Correa</a></li>
<li><a href="https://github.com/IBMDecisionOptimization/docplex-examples">GitHub com exemplos do uso do DOCPLEX</a></li>
<li><a href="http://ibmdecisionoptimization.github.io/docplex-doc/#mathematical-programming-modeling-for-python-using-docplex-mp-docplex-mp">IBM Decision Optimization CPLEX Modeling for Python</a></li>
<li>Slides disponibilizados pelo Professor</li>
