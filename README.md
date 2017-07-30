Image to ASCII text generator written in Python

```
                               jaa j$#GG@j@[:o@gya                             
                             a$@Wt-j$mXG@j@[:G@@W@k#                           
                            ]$$SQ@@pR8XG@j@*:G@@W@k$$                          
                            d$$y$@@ta#GG@j@@]J@@W@k$$|                         
                            d$$@@@@j$#GG@j@@]J@@W@k$$|                         
                            ^t!hht :K!!!@j@@])@@W@k$#|                         
                       ....  ---..---...@j@@])@@W@k$8|                         
                  ja@@d@@@@Q@$$@@@@j$8XG@j@@]J@@W@k$8| ]@@@$@@#a               
                 d@Q@@d@@@@Q@$O@@@@j$#XG@j@@])@@W@k$#| ]@@@$@@#Q@              
                #d@Q@@d@@@@Q@$8@@@@j$#XG@j@@]J@@W@k$#| ]@@@$@@#Q@#             
               a$d@Q@@d@@@@Q@$8@@@@j$8XG@j@@])@@W@k$#  ]@@@$@@#Q@8             
               B$d@Q@@@@@@@Q@$#@@@@j$#XG@j@@])@@W@k|` ]$@@@$@@#Q@#n            
               j$d@Q@@@@@@@Q@$8@@@.o6bhU.]$-<=$k`|*  a$$@@@$@@#Q@#U            
               j$d@Q@@@@@@@Q@*`                  .ya8$$$@@@$@@#Q@8U            
               j$d@Q@@@@@@@|` ]a@#Q$d@Q@@@$#$Q@#4$b$#$$$@@@$@@#Q@#U            
               #$d$Q@@@@@@[  a$@@#Q$d@Q@@@$#$Q@84$b$8$$$@@@$@@#Q@#|            
               ]$d$Q@@@@@@| ]#$@@#Q$d@Q@@@$#$Q@84$b$8$$$@@@$@@#Q@#`            
                Rd$Q@@@@@@| ]#$@@#Q$d@Q@@@$#$Q@#4$b$8$$$@@@$@@#Q@|             
                 j$Q@@@@@@| ]#$@@#Q$d@Q@@@$#$Q@84$b$#$$$@@@$@@#Q|              
                   \*ttttt` ]#$@@#Q$d@Q@$tK!hht!!!!!!!!!tt****``               
                            ]#$@@#Q$d@Q@|                                      
                            ]#$@@#Q$d@Q@@@$#$Q@#4$b$8|                         
                            ]#$@@#Q$d@Q@@@$#$Qt8mhb$8|                         
                            ]#$@@#Q$d@Q@@@$#${Q@@@j$8|                         
                             R$@@#Q$d@Q@@@$#$Q{WWhy$|                          
                               R@#Q$d@Q@@@$#$Q@8B$|`                           
                                  `**tj@@@$|**``                               

                                       dy                                      
                                       @[                                      
                               ]@|     @k                                      
        :                      ]@|     @k                <-            .,      
   ]d>**``*@y    @[      j@|  *N@|**   @@dy`**Ng,    ]gt****@y    lgL**`*N@y   
   j@       @|   @[      j@|   ]@|     @k`     d@   j@*      @@   @@      d@   
   j@       Q@   @[      j@|   ]@|     @k      j@   d@       j@   @@      j@   
   j@       @@   @[      j@|   ]@`     @k      j@   d@       j@`  @@      j@   
   j@       @[   @@      j@|   ]@,     @k      j@   ]@       a[   @@      j@   
   j@g;   jg[`   ]@g    lg@|    @[     @k      j@    *@,   ]g|`   @@      d@   
   j@ `*`**`       **`**` @`      *`   **       *      `*``*`     **      `*   
   j@                    j@                                                    
   j@                   j@|                                                    
    t                v)|*`                                                     
```

```shell
Usage: ./python ascii.py [args]

	-h 		Print help text
	-s		Generate using 1 value per character instead of 4.
	-W		Width of rect to generate a character from. (default: 8)
	-H		Height of rect to generate a character from (default: 16)
	-r		Factor to reduce the white values by. (default: 750)
	-f		Input file (default: input.png)
	-c		File to calibrate white values from (default: alpha.png)
	-d		Print debug info when generating ASCII
	-o		Output calibration white values rather than an ASCII image
	-e		Allow for extra characters that many terminals can't show
```
