import pandas as pd  
import numpy as np
import queue as que
from matplotlib import pyplot as plt

def return_mark(strr):
    strlength=len(strr)
    rstr=strr[1:]
    if rstr=='A':
        return 1
    if rstr=='2':
        return 2
    if rstr=='3':
        return 3
    if rstr=='4':
        return 4        
    if rstr=='5':
        return 5        
    if rstr=='6':
        return 6        
    if rstr=='7':
        return 7
    if rstr=='8':
        return 8
    if rstr=='9':
        return 9        
    if rstr=='10':
        return 0
    if rstr=='J':
        return 0
    if rstr=='Q':
        return 0
    if rstr=='K':
        return 0
#bord banker=1, dealer=0
    
dealer=0
banker=0
draw=0        
fr=open('100000deck.txt')
numberofline=len(fr.readlines())
print(numberofline)
fr=open('100000deck.txt')
for line in fr.readlines():
    
    line=line.split()
    deck=list(line)
    initialize_money=1000
    #50 per bet
    while len(deck)>6 and initialize_money>49 :
        banker_score=0
        dealer_score=0
        banker_score=return_mark(deck.pop())
        dealer_score=return_mark(deck.pop())
        banker_score=+return_mark(deck.pop())
        dealer_score=+return_mark(deck.pop())
        banker_score=banker_score%10
        dealer_score=dealer_score%10
        dealercardno=0
        supp_flag=0
        if dealer_score==8 or dealer_score==9 or banker_score==8 or banker_score==9:
            if dealer_score>banker_score:
                print('dealer')
                dealer+=1
            elif dealer_score<banker_score:
                print('banker')
                banker+=1
            else:
                print('draw')
                draw+=1
        elif dealer_score==6 and banker_score==6 or dealer_score==7 and banker_score==7 or dealer_score==6 and banker_score==7 or dealer_score==7 and banker_score==6:
            if dealer_score>banker_score:
                print('dealer')
                dealer+=1
            elif dealer_score<banker_score:
                print('banker')
                banker+=1
            else:
                print('draw')
                draw+=1
        else:
            
            if dealer_score<=5:
                dealercardno=return_mark(deck.pop())
                dealer_score+=dealercardno
                dealer_score=dealer_score%10
                supp_flag=1
               
            
            if banker_score<=2:
                banker_score+=return_mark(deck.pop())
                banker_score=banker_score%10      
            else:
                
                if banker_score==3 and supp_flag==1 and dealercardno!=8:
                    banker_score+=return_mark(deck.pop())
                    banker_score=banker_score%10
                elif banker_score==4  and supp_flag==1 and dealercardno!=0 and dealercardno!=1 and dealercardno!=8 and dealercardno!=9:
                    banker_score+=return_mark(deck.pop())
                    banker_score=banker_score%10
                elif banker_score==5 and supp_flag==1 and dealercardno!=2 and dealercardno!=3 and dealercardno!=0 and dealercardno!=1 and dealercardno!=8 and dealercardno!=9:
                    banker_score+=return_mark(deck.pop())
                    banker_score=banker_score%10
                elif banker_score==6 and supp_flag==1 and dealercardno!=4  and dealercardno!=5  and dealercardno!=2 and dealercardno!=3 and dealercardno!=0 and dealercardno!=1 and dealercardno!=8 and dealercardno!=9:
                    banker_score+=return_mark(deck.pop())
                    banker_score=banker_score%10
                else:
                
                    if banker_score==3 :
                        banker_score+=return_mark(deck.pop())
                        banker_score=banker_score%10
                    elif banker_score==4 :
                        banker_score+=return_mark(deck.pop())
                        banker_score=banker_score%10
                    elif banker_score==5 :
                        banker_score+=return_mark(deck.pop())
                        banker_score=banker_score%10
                   
                
            if dealer_score>banker_score:
                print('dealer')
                dealer+=1
            elif dealer_score<banker_score:
                print('banker')
                banker+=1
            else:
                print('draw')
                draw+=1
total=dealer+banker+draw
print('dealer :',dealer,dealer/total)
print('banker :',banker,banker/total)
print('draw :',draw,draw/total )
print('total :',dealer+banker+draw)
