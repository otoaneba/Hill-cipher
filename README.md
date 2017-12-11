# Hill-cipher

## A bit more complex than Caesar Cipher

![alt text](https://i.imgur.com/XZcUCMU.png "caesar cipher")

Caesar Cipher is a simple encyption technique to encypt messages by adding or multiplying each character by a constant offset.
Because each character takes up a *single byte (8-bits)*, we can offset each character by offsetting with another 1B value. However,
this means that there are only 2^8 - 1 ways (subtract 1 to acount for the original value) to encypt the message. Hill cipher goes a bit further by reading the original values and putting them inside a 2 dimensional array, we can then multiply that array with an invertible matrix to make it harder to decrypt. The only way to decrypt, then, is if you have the inverted matrix in which you cross product to get the original message. The 
security of Hill Cipher more secured than Caesar Cipher, but it's generally not that secured compared to other modern cryptographies. 

## 2 Dimensional Array

Say you have a simple one sentence message, 

"YOU DIDN'T SAY THE MAGIC WORD".

Say space = 0, A = 1, B = 2, C = 3, ... Z = 26 and ' = 27 for simplicity. The message translated becomes the
matrix below.

A = ( 
    
    {25, 15, 21, 0 , 4, 9, 4, 14, 27, 20},
    
    {0, 19, 1, 25, 0, 20, 8, 5, 0, 13}
    
    {1, 7, 9, 3, 0, 23, 15, 18, 4, 0}
   
   );
   
   You can multiple with an invertible matrix, 
   
B = ( 
    
    {1, 0, 2}
    
    {0, 2, 1}
    
    {1, 1, 2}
    );

Now, BA becomes the matrix, 
BA = (

    {27, 29, 39, 6, 4, 55, 34, 50, 35, 20},
  
    {1, 45, 11, 53, 0, 63, 31, 28, 4, 26},

    {27, 48, 40, 31, 4, 75,42, 55, 35, 33}
  
  );
  
  multiplying the above matrix with an interted matrix, B^-1 gives us the original matrix
  
  (B^-1)(B)A = A
