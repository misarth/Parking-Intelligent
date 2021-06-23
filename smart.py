from tkinter import *
import os
import datetime
import time
from tkinter.messagebox import *

#ticket de paiement

def ticket():
    heureentree= datetime.datetime.now()     
    print(heureentree)
    
    mon_ticket = open("/home/khalladi_sawsen/Bureau/Smart Parking/ticket.txt", "w")
    mon_ticket.write('\n               *********************************************************\n\n')
    mon_ticket.write('                                      Smart Parking\n')
    mon_ticket.write('                                   Soyez les bienvenus \n')
    mon_ticket.write('\n               ********************************************************* \n \n')
    mon_ticket.write('                  La date d''entrée est :     ')
    mon_ticket.write(str(heureentree)) 

    mon_ticket.write('\n\n')


    mon_ticket.write(' \n\n')

    mon_ticket.write('                  Le montant à payer est  :  2 Dinars\n\n')                    
    mon_ticket.write('               *********************************************************\n \n')
    mon_ticket.write('                                 Merci pour votre confiance  \n \n')
    mon_ticket.write('               *********************************************************\n \n')


    mon_ticket.close()


# heure
def temps():

    heure.set(time.strftime('%H:%M:%S'))
    window.after(1000,temps)


##### appeler la fenetre avec reservation

def appel():

  ### afficher les numeros dans la barre de code
    
    def afficher(a):
        sauve = metext.cget("text")
        metext.configure(text = sauve+a)
  
    def delete():
        metext.configure(text="")
    
    top=Tk()
    window.withdraw()
    top.title("Parking")
    top.geometry("900x900")
    top.configure(bg='#001182551')

    lab=Label(top, text="Veuillez entrer votre code SVP !",font=("Courrier",15,"bold"),fg='white',bg='#001182551')
    lab.place(x=270,y=20)
    
  ### entrer le code de réservation
   
    metext=Label(top,font=('arial',20,'bold'),text="",width=14,bd=5,bg='powder blue',justify='left')
    metext.place(x=340,y=70)
    
    z=360
    w=1
    while(z<555) :
        zz=150
        while (zz<310):
            
            while(w<10):
                b=Button(top,padx=14,pady=14,bd=4,bg='white',text=str(w),command=lambda x=str(w):afficher(x))
                b.place(x=z,y=zz)
                zz=zz+70
                w=w+3
            w=w-8
                
        z=z+65

    but0=Button(top,padx=14,pady=14,bd=4,bg='white',text="0",command=lambda x="0":afficher(x))
    but0.place(x=425,y=360)

    butdel=Button(top,padx=14,pady=14,bd=4,bg='red',text="Del",command=delete)
    butdel.place(x=360,y=360)

### appeler la fenetre du cartographie et indiquer la place reservée
    
    def suiv():
        global C
        for n in range(len(C)):
            if metext.cget("text")==C[n] and L[n]=="r":
                
                tip=Tk()
                top.withdraw()
                tip.title("Parking")
                tip.geometry("1500x1000")
                tip.configure(bg='#001182551')
                lab=Label(tip, text="Voici la cartographie du parking !",font=("Courrier",30,"bold"),fg='white',bg='#001182551')
                lab.place(x=300,y=20)
                ################################# debut cartographie
                # debut background

                canframe= Frame(tip,width=500)
                canframe.configure(borderwidth=4,background='white')
                can= Canvas(canframe,width=1000,height=600,background='grey')

                # entrée

                en=Frame(canframe,width=80)
                en.configure(borderwidth=1,background='white')
                entre=Label(en,text="Entrée",font=("Courrier",30), bg='white', fg='Blue')
                entre.pack()
                en.place(x=80,y=520)

                # sortie

                srt=Frame(canframe,width=80)
                srt.configure(borderwidth=1,background='white')
                sorte=Label(srt,text="Sortie",font=("Courrier",30), bg='white', fg='red')
                sorte.pack()
                srt.place(x=80,y=20)

                ###### Les places des voitures ######

                
                ###### Les places des voitures de 1 à 5 ######
    
                k=250
                q=1
                while (k<750) and (q<6):
                    p=Frame(canframe,width=50)
                    p.configure(borderwidth=1,background='yellow')

                    if L[q-1]=="v":
                        pe=Canvas(p,width=100,height=150,background='green')
                        lab=Label(pe,text=str(q), font=("Courrier",20,"bold"), bg='green', fg='white')
                        
                    elif L[q-1]=="o":
                        pe=Canvas(p,width=100,height=150,background='red')
                        lab=Label(pe,text=str(q), font=("Courrier",20,"bold"), bg='red', fg='white')
                       
                    elif L[q-1]=="r":
                        pe=Canvas(p,width=100,height=150,background='blue')
                        lab=Label(pe,text=str(q), font=("Courrier",20,"bold"), bg='blue', fg='white')
              
                    p.place(x=k,y=350)
                    pe.pack()

                    lab.place(x=40,y=55)
                    k=k+100
                    q=q+1
            

                ##barriere
                
                i=0 
                while i<630:
                    x=Canvas(tip,width=30,height=20,background='white')
                    x.place(x=350+i,y=395)
                    i=i+60
                j=0
                while j<580:
                    y=Canvas(tip,width=30,height=20,background='red')
                    y.place(x=380+j,y=395)
                    j=j+60
                
                ###### Les places des voitures de 6 à 10 ######
                
                t=650
                u=6
                while (t>150) and (u<11):
                    d=Frame(canframe,width=50)
                    d.configure(borderwidth=1,background='yellow')
                    if L[u-1]=="v":
                        de=Canvas(d,width=100,height=150,background='green')
                        labd=Label(de,text=str(u), font=("Courrier",20,"bold"), bg='green', fg='white')
                    elif L[u-1]=="o":
                        de=Canvas(d,width=100,height=150,background='red')
                        labd=Label(de,text=str(u), font=("Courrier",20,"bold"), bg='red', fg='white')
                    elif L[u-1]=="r":
                        de=Canvas(d,width=100,height=150,background='blue')
                        labd=Label(de,text=str(u), font=("Courrier",20,"bold"), bg='blue', fg='white')
                    d.place(x=t,y=100)
                    de.pack()
                    
                    labd.place(x=40,y=55)
                    t=t-100
                    u=u+1

                # fin background

                canframe.place(x=150,y=100)
                can.pack()
                ########################################## fin cartographie
                # nbre place vide
                
                x=L.count("v")
        
                labbw= Label (tip, text="Le nombre de places vides est :  "+str(x),font=("Courrier",20,"bold"),fg='white',bg='#001182551')
                labbw.place(x=400,y=780)
                
                
                labw=Label(tip, text="Le numéro de votre place est :   "+str(n+1),font=("Courrier",20,"bold"),bg='#001182551',fg='white')
                labw.place(x=400,y=840)

                def validation():
                    tip.withdraw()
                    L[n]="o"
                    window.deiconify()
                    ticket()

                def retour1():
                    tip.withdraw()
                    top.deiconify()
        
                butret1=Button(tip,padx=17,pady=17,bd=4,text="Retour",font=("Times",15,"bold italic"),fg='white',bg='green',command=retour1)
                butret1.place(x=1300,y=530)

                butval=Button(tip,padx=17,pady=17,bd=4,bg='blue',text="Entrer",font=("Times",15,"bold italic"),fg='white',command=validation)
                butval.place(x=1300,y=230)

                tip.mainloop()
            else:
                labww=Label(top, text="Code incorrect ! Veuillez vérifier votre code .",font=("Courrier",15,"bold"),fg='white',bg='#001182551')
                labww.place(x=220,y=560)

    butok=Button(top,padx=14,pady=14,bd=4,bg='blue',text="Ok",command=suiv)
    butok.place(x=485,y=360)

    # Retour a la page principale
    
    def retour():
        top.withdraw()
        window.deiconify()
    #annulation de la reservation

    def annulerreservation():
        global C
        global L
        for n in range(len(C)):
            if metext.cget("text")==C[n] and L[n]=="r":
                top.withdraw()
                L[C.index(metext.cget("text"))]="v"
                window.deiconify()
            else:
                labwww=Label(top, text="Code incorrect ! Veuillez vérifier votre code .",font=("Courrier",15,"bold"),fg='white',bg='#001182551')
                labwww.place(x=220,y=560)

    butret=Button(top,padx=14,pady=14,bd=4,text="Retour",font=("Times",15,"bold italic"), bg='#058718', fg='white',command=retour)
    butret.place(x=300,y=450)

    butannul=Button(top,padx=14,pady=14,bd=4,text="Annuler ma réservation",font=("Times",15,"bold italic"), bg='#058718', fg='white',command=annulerreservation)
    butannul.place(x=430,y=450)
    
    top.mainloop()

# appeler la fenetre sans reservation

def sans():
    global L
    tp=Tk()
    window.withdraw()
    tp.title("Parking")
    tp.geometry("1500x1000")
    tp.configure(bg='#001182551')

    lab=Label(tp, text="Voici la cartographie du parking !",font=("Courrier",30,"bold"),fg='white',bg='#001182551')
    lab.place(x=300,y=20)
    ################################# debut cartographie
    # debut background
    
    canframe= Frame(tp,width=500)
    canframe.configure(borderwidth=4,background='white')
    can= Canvas(canframe,width=1000,height=600,background='grey')

    # entrée

    en=Frame(canframe,width=80)
    en.configure(borderwidth=1,background='white')
    entre=Label(en,text="Entrée",font=("Courrier",30), bg='white', fg='Blue')
    entre.pack()
    en.place(x=80,y=520)

    # sortie

    srt=Frame(canframe,width=80)
    srt.configure(borderwidth=1,background='white')
    sorte=Label(srt,text="Sortie",font=("Courrier",30), bg='white', fg='red')
    sorte.pack()
    srt.place(x=80,y=20)


    ###### Les places des voitures de 1 à 5 ######
    
    k=250
    q=1
    while (k<750) and (q<6):
        p=Frame(canframe,width=50)
        p.configure(borderwidth=1,background='yellow')
        if L[q-1]=="v":
            pe=Canvas(p,width=100,height=150,background='green')
            lab=Label(pe,text=str(q), font=("Courrier",20,"bold"), bg='green', fg='white')
        elif L[q-1]=="o":
            pe=Canvas(p,width=100,height=150,background='red')
            lab=Label(pe,text=str(q), font=("Courrier",20,"bold"), bg='red', fg='white')
        elif L[q-1]=="r":
            pe=Canvas(p,width=100,height=150,background='blue')
            lab=Label(pe,text=str(q), font=("Courrier",20,"bold"), bg='blue', fg='white')
        p.place(x=k,y=350)
        pe.pack()
        
        lab.place(x=40,y=55)
        k=k+100
        q=q+1
   

    ##barriere
    
    i=0 
    while i<630:
        x=Canvas(tp,width=30,height=20,background='white')
        x.place(x=350+i,y=395)
        i=i+60
    j=0
    while j<580:
        y=Canvas(tp,width=30,height=20,background='red')
        y.place(x=380+j,y=395)
        j=j+60
    
    ###### Les places des voitures de 6 à 10 ######
    
    t=650
    u=6
    while (t>150) and (u<11):
        d=Frame(canframe,width=50)
        d.configure(borderwidth=1,background='yellow')
        if L[u-1]=="v":
            de=Canvas(d,width=100,height=150,background='green')
            labd=Label(de,text=str(u), font=("Courrier",20,"bold"), bg='green', fg='white')
        elif L[u-1]=="o":
            de=Canvas(d,width=100,height=150,background='red')
            labd=Label(de,text=str(u), font=("Courrier",20,"bold"), bg='red', fg='white')
        elif L[u-1]=="r":
            de=Canvas(d,width=100,height=150,background='blue')
            labd=Label(de,text=str(u), font=("Courrier",20,"bold"), bg='blue', fg='white')
        d.place(x=t,y=100)
        de.pack()
        
        labd.place(x=40,y=55)
        t=t-100
        u=u+1

    # fin background

    canframe.place(x=150,y=100)
    can.pack()
    ########################################## fin cartographie
    
    
    # nbre place vide

    x=L.count("v")
    if x==0:
        labw=Label (tp, text="Désolée aucune place vide ",font=("Courrier",20,"bold"),fg='white',bg='#001182551')
        labw.place(x=400,y=850)
    else :
        labw= Label (tp, text="Le nombre de places vides est :  "+str(x),font=("Courrier",20,"bold"),fg='white',bg='#001182551')
        labw.place(x=400,y=780)
    
        labw=Label(tp, text="La place la plus proche est :  "+str(L.index("v")+1),font=("Courrier",20,"bold"),fg='white',bg='#001182551')
        labw.place(x=420,y=850)

    def retour():
        tp.withdraw()
        window.deiconify()
    
    def validation1():
        tp.withdraw()
        L[L.index("v")]="o"
        window.deiconify()
        ticket()

    butret=Button(tp,padx=17,pady=17,bd=4,text="Retour",font=("Times",15,"bold italic"),fg='white',bg='green',command=retour)
    butret.place(x=1300,y=530)
    
    if x != 0:
        butval1=Button(tp,padx=17,pady=17,bd=4,bg='blue',text="Entrer",font=("Times",15,"bold italic"),fg='white',command=validation1)
        butval1.place(x=1300,y=230)

    tp.mainloop()

# appeler la fenetre reserver

def resurplace():
    
    def afficher(a):
        sauve = metext.cget("text")
        metext.configure(text = sauve+a)
    
    def delete():
        metext.configure(text="")
    
    global L
    global C
    
    tep=Tk()
    window.withdraw()
    tep.title("Parking")
    tep.geometry("1500x900")
    tep.configure(bg='#001182551')

    lab=Label(tep, text="Voici la cartographie du parking !",font=("Courrier",30,"bold"),fg='white',bg='#001182551')
    lab.place(x=100,y=20)

    ################################# debut cartographie
    # debut background
    
    canframe= Frame(tep,width=500)
    canframe.configure(borderwidth=4,background='white')
    can= Canvas(canframe,width=850,height=600,background='grey')

    # entrée

    en=Frame(canframe,width=80)
    en.configure(borderwidth=1,background='white')
    entre=Label(en,text="Entrée",font=("Courrier",30), bg='white', fg='Blue')
    entre.pack()
    en.place(x=70,y=520)

    # sortie

    srt=Frame(canframe,width=80)
    srt.configure(borderwidth=1,background='white')
    sorte=Label(srt,text="Sortie",font=("Courrier",30), bg='white', fg='red')
    sorte.pack()
    srt.place(x=70,y=20)


    ###### Les places des voitures de 1 à 5 ######
    
    k=150
    q=1
    while (k<750) and (q<6):
        p=Frame(canframe,width=50)
        p.configure(borderwidth=1,background='yellow')
        if L[q-1]=="v":
            pe=Canvas(p,width=100,height=150,background='green')
            lab=Label(pe,text=str(q), font=("Courrier",20,"bold"), bg='green', fg='white')
        elif L[q-1]=="o":
            pe=Canvas(p,width=100,height=150,background='red')
            lab=Label(pe,text=str(q), font=("Courrier",20,"bold"), bg='red', fg='white')
        elif L[q-1]=="r":
            pe=Canvas(p,width=100,height=150,background='blue')
            lab=Label(pe,text=str(q), font=("Courrier",20,"bold"), bg='blue', fg='white')
        p.place(x=k,y=350)
        pe.pack()
        
        lab.place(x=40,y=55)
        k=k+100
        q=q+1
   

    ##barriere
    
    i=0 
    while i<600:
        x=Canvas(tep,width=30,height=20,background='white')
        x.place(x=160+i,y=395)
        i=i+60
    j=0
    while j<580:
        y=Canvas(tep,width=30,height=20,background='red')
        y.place(x=190+j,y=395)
        j=j+60
    
    ###### Les places des voitures de 6 à 10 ######
    
    t=550
    u=6
    while (t>50) and (u<11):
        d=Frame(canframe,width=50)
        d.configure(borderwidth=1,background='yellow')
        if L[u-1]=="v":
            de=Canvas(d,width=100,height=150,background='green')
            labd=Label(de,text=str(u), font=("Courrier",20,"bold"), bg='green', fg='white')
        elif L[u-1]=="o":
            de=Canvas(d,width=100,height=150,background='red')
            labd=Label(de,text=str(u), font=("Courrier",20,"bold"), bg='red', fg='white')
        elif L[u-1]=="r":
            de=Canvas(d,width=100,height=150,background='blue')
            labd=Label(de,text=str(u), font=("Courrier",20,"bold"), bg='blue', fg='white')
        d.place(x=t,y=100)
        de.pack()
        
        labd.place(x=40,y=55)
        t=t-100
        u=u+1

    # fin background

    canframe.place(x=50,y=100)
    can.pack()

    ########################################## fin cartographie
    
    labm=Label (tep, text="Entrer le numéro de la place à réserver ",font=("Courrier",13,"bold"),fg='white',bg='#001182551')
    labm.place(x=970,y=170)
   
    ### entrer le numéro de la place à réserver   
   
    metext=Label(tep,font=('arial',20,'bold'),text="",width=14,bd=5,bg='powder blue',justify='left')
    metext.place(x=1040,y=220)
    
    z=1060
    w=1
    while(z<1255) :
        zz=300
        while (zz<460):
            
            while(w<10):
                b=Button(tep,padx=14,pady=14,bd=4,bg='white',text=str(w),command=lambda x=str(w):afficher(x))
                b.place(x=z,y=zz)
                zz=zz+70
                w=w+3
            w=w-8
                
        z=z+65

    but0=Button(tep,padx=14,pady=14,bd=4,bg='white',text="0",command=lambda x="0":afficher(x))
    but0.place(x=1125,y=510)

    butdel=Button(tep,padx=14,pady=14,bd=4,bg='red',text="Del",command=delete)
    butdel.place(x=1060,y=510)

    #nbre de places vides
    
    x=L.count("v")
        
    labbw= Label (tep, text="Le nombre de places vides est :  "+str(x),font=("Courrier",20,"bold"),fg='white',bg='#001182551')
    labbw.place(x=200,y=780)
   
   ## la confirmation de la place réservée 
    def conf():
        global L
        global C
        if metext.cget("text") in ["1","2","3","4","5","6","7","8","9","10"]:
            if L[int(metext.cget("text"))-1]=="v":
                showwarning('Réservation','Le numéro de votre place à réserver est :   '+metext.cget("text")+'\nVotre code est :   '+C[int(metext.cget("text"))-1])
                tep.withdraw()
                L[int(metext.cget("text"))-1]="r"
                window.deiconify()
                ticket()
                    

            else :
                showwarning('Réservation','Désolé cette place est non disponible ')


        else:
            showwarning('Réservation','Le numéro de place demandée est incorrect ')
    
    butok=Button(tep,padx=14,pady=14,bd=4,bg='blue',text="Ok",command=conf)
    butok.place(x=1180,y=510)
    

    def retour():
        tep.withdraw()
        window.deiconify()

    butret=Button(tep,padx=17,pady=17,bd=4,text="Retour",font=("Times",15,"bold italic"),fg='white',bg='green',command=retour)
    butret.place(x=1100,y=630)
    

    tep.mainloop()

## page principale contenant les 3 boutons 

window = Tk()
window.title("Parking")
window.geometry("900x1000")
window.configure(bg='#001182551')

window.iconphoto(FALSE,PhotoImage(file="Bureau/Smart Parking/p5.png"))

heure = StringVar()
Label(window,textvariable=heure,font=("Courrier",17,"bold italic"),bg='#001182551',fg='white').place(x=50,y=15)

photo = PhotoImage(file="Bureau/Smart Parking/p01.png")

labelphoto = Label(window, image=photo)
labelphoto.place(x=385,y=85)

label_title= Label(window,text="Parking Intéligent",font=("Courrier",40,"bold italic"),bg='#001182551',fg='white')
label_title.place(x=200,y=300)

## L : liste indiquant la situaton du parking
L=["o","v","v","v","v","r","o","r","v","o"]

## C : liste des codes de réservation
C=["0123","1234","2345","3456","4567","5678","6789","7890","8901","9012"]

avec_button= Button(window, text="Avec réservation", font=("Times",35,"bold italic"), bg='#058718', fg='white',command=appel)
avec_button.place(x=320,y=500)

sans_button= Button(window, text="Sans réservation", font=("Times",35,"bold italic"),bg='red', fg='white',command=sans)
sans_button.place(x=320,y=650)

res_button= Button(window, text="       Réserver       ", font=("Times",35,"bold italic"),bg='orange', fg='white',command=resurplace)
res_button.place(x=320,y=800)



temps()


window.mainloop()