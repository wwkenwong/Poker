import pandas as pd  
import numpy as np
import queue as que
import random
from datetime import datetime
#random.seed(datetime.now())
from matplotlib import pyplot as plt
each_bet_array = [100, 200, 300, 400, 500]
each_bet=400
f = open('A.txt', 'w', encoding = 'UTF-8')
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
aggregate_mean_max=[]
aggregate_mean_max_occur=[]
itr_r=1

#bord banker=1, dealer=0
for num in range(len(each_bet_array)):
    for roun in range(itr_r):
        each_bet=each_bet_array[num]
        random.seed(datetime.now())
        dealer=0
        banker=0
        draw=0        
        fr=open('1000deck.txt')
        numberofline=len(fr.readlines())
        #print(numberofline,'set card')
        fr=open('1000deck.txt')
        profit=[]
        round_max_array=[]
        round_max_occur_array=[]
        for line in fr.readlines():
            line=line.split()
            deck=list(line)
            initialize_money=1000
            round_max=0
            round_max_occur=0
            cur=0
            
            #50 per bet
            while len(deck)>6 and initialize_money>(each_bet-1) :
                cur+=1
                decision=random.random()
                decison_flag=0
                if abs(decision-0.5)==0.00000:
                    decision=0.5
                    decison_flag=1
                elif 0.5>decision:
                    decison_flag=0
                else:
                    decison_flag=2
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
                initialize_money-=each_bet
                
                if dealer_score==8 or dealer_score==9 or banker_score==8 or banker_score==9:
                    if dealer_score>banker_score:
                        #print('dealer')
                        dealer+=1
                        if decison_flag==0:                  
                            initialize_money+=each_bet*2
                    elif dealer_score<banker_score:
                        #print('banker')
                        banker+=1              
                        if decison_flag==2:
                            initialize_money+=each_bet+(0.5*each_bet)
        
                    else:
                        #print('draw')
                        draw+=1
                        if decison_flag==1:
                            initialize_money+=each_bet+(8*each_bet)
                elif dealer_score==6 and banker_score==6 or dealer_score==7 and banker_score==7 or dealer_score==6 and banker_score==7 or dealer_score==7 and banker_score==6:
                    if dealer_score>banker_score:
                        #print('dealer')
                        dealer+=1
                        if decison_flag==0:
                            initialize_money+=each_bet*2
                    elif dealer_score<banker_score:
                        #print('banker')
                        banker+=1
                        
                        if decison_flag==2:
                            if banker_score>=6:
                                 
                                 initialize_money+=each_bet+(0.5*each_bet)
                            else:
                                
                                initialize_money+=each_bet*2
                    else:
                        #print('draw')
                        draw+=1
                        if decison_flag==1:
                            initialize_money+=each_bet+(8*each_bet)
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
                        #print('dealer')
                        dealer+=1
                        if decison_flag==0:
                            initialize_money+=each_bet*2
                    elif dealer_score<banker_score:
                        #print('banker')
                        banker+=1
                        if decison_flag==2:
                            if banker_score>=6:
                                 initialize_money+=each_bet+(0.5*each_bet)
                            else:
                                initialize_money+=each_bet*2
                    else:
                        #print('draw')
                        draw+=1
                        if decison_flag==1:
                            initialize_money+=(each_bet+(8*each_bet))
                if initialize_money>round_max:
                    round_max=initialize_money
                    round_max_occur=cur
            round_max_array.append(round_max)
            round_max_occur_array.append(round_max_occur)
            profit.append(initialize_money)
        total=dealer+banker+draw
        max_mean=0
        max_mean_round=0
        for itr in range( len(round_max_array)):
            
            max_mean+=round_max_array[itr]
        max_mean/=len(round_max_array)
                
        for itr in range( len(round_max_occur_array)):
            max_mean_round+=round_max_occur_array[itr]
        max_mean_round/=len(round_max_array)
        aggregate_mean_max.append(max_mean)
        aggregate_mean_max_occur.append(max_mean_round)
    
    #Print per set
    out_max_mean=0
    out_max_mean_round=0

    for itr in range( len(aggregate_mean_max)):
        
        out_max_mean+=aggregate_mean_max[itr]

    out_max_mean/=len(aggregate_mean_max)
    for itr in range( len(aggregate_mean_max_occur)):        
        out_max_mean_round+=aggregate_mean_max_occur[itr]
    out_max_mean_round/=len(aggregate_mean_max_occur)
    f.write('bet :'+str(each_bet)+'\n')
    prob_dealer=dealer/total
    prob_banker=banker/total
    prob_draw=draw/total
    f.write('dealer :'+str(dealer)+' '+str(prob_dealer)+'\n')
    f.write('banker :'+str(banker)+' '+str(prob_banker)+'\n')
    f.write('draw :'+str(draw)+' '+str(prob_draw)+'\n' )
    f.write('total :'+str(total)+'\n')
    f.write('max_mean :'+str(out_max_mean)+'\n')
    f.write('max_occur :'+str(out_max_mean_round)+'\n')
    
f.close()
