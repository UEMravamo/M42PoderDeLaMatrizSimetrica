# **Challenge: El Poder de la Matriz Simétrica**  

¡Bienvenido, valiente programador! 🌟  

El Reino de las Matrices está en peligro. La malvada Matriz \( A \), un antiguo artefacto simétrico de dimensiones $$( n \times n )$$, se ha despertado y amenaza con desbordar el equilibrio numérico. Tu misión es usar tus habilidades para calcular su **potencia \( k \)** y controlar su poder, ¡pero cuidado! No puedes usar métodos de fuerza bruta o te quedarás atrapado en un bucle eterno de cálculos inútiles.  

## **Tu misión**  
- Dado \( n \), la dimensión de la matriz \( A \), y un número entero \( k \), eleva \( A \) a la potencia \( k \) utilizando métodos eficientes que aprovechen sus propiedades mágicas (simetría).  

## **Restricciones**  
- \( A \) es una matriz **simétrica** (\(A[i][j] = A[j][i]\)).  
- 2 ≤ n ≤ 10: El tamaño de la matriz es controlable, pero desafiante.  
- 1 ≤ k ≤ $$10^3$$: La potencia puede ser colosal, así que necesitarás astucia.   
- No puedes invocar artefactos mágicos como bibliotecas preconstruidas para calcular $$(A^k)$$ directamente.  

## **Entrada**  
1. Un entero \( n \): la dimensión de la matriz.  
2. La matriz \( A \) de tamaño $$( n \times n )$$ con sus elementos separados por espacios.  
3. Un entero \( k \): la potencia a la que se debe elevar la matriz.

$$
\begin{pmatrix}
  2& 1\\
  1 & 2 
\end{pmatrix}
$$

## **Salida**  
Una matriz $$( A^k )$$ de tamaño $$\( n \times n \)$$, con sus valores redondeados a 2 decimales si es necesario.  

Resultado: $$(A^3)$$

$$
\begin{pmatrix}
  14& 13\\
  13& 14
\end{pmatrix}
$$

## **Habilidades Especiales (Tips)**  
- Usa el **hechizo de Exponenciación Rápida para Matrices** para dominar el poder de \( A \) en menos pasos. O podeis usar **La gema de la Diagonalización** pero para ello teneis que tener el tesoro del Algebra.
- La simetría de \( A \) puede ser tu aliada secreta: ¡aprovéchala para optimizar los cálculos!  
- Prepara tu arsenal matemático para números grandes. Si las dimensiones son gigantes, podrías necesitar controlar los desbordamientos.  

## **Recompensa**  
Si logras controlar el poder de la matriz, serás coronado como **Maestro del Reino de las Matrices**. ¡Los números te estarán eternamente agradecidos!  

## **Requisitos**
1. Usa Python 3.7.
2. Escribe código conforme a PEP8.
3. Escribe algunas pruebas (considera usar pytest o uniitest).
4. Documenta tu solución en un archivo.
5. Se os adjunta un Python para poder generar las matrices de origen asi como información de algebra por si se quiere repasar.
6. Se puede usar [NumPy](https://numpy.org)

## **Requisitos**
El orden de complejidad tiene que estar entre **$$O(m^3)$$** para valores propios o **$$O(log(n)⋅m^3)$$**
Para tranquilidad de Adrian y su preocupaciòn con n y m, añado esta definición para que se tenga todo los mas claro posible y entender la complejidad $$[\forall n, m \in \mathbb{R}_{\geq 0}, \, n = m\]$$

🎮 **¡Prepárate para la batalla matemática!** 🚀  


