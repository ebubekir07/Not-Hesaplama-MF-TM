import tkinter as tk
from tkinter import messagebox
pencere = tk.Tk()
pencere.title("Not Hesaplayıcı MF-TM v2.0")
pencere.geometry("570x333")

#################################################################################
matvar = tk.IntVar()
fizvar = tk.IntVar()
kimvar = tk.IntVar()
biyovar = tk.IntVar()
edebvar = tk.IntVar()
tarvar = tk.IntVar()
felvar = tk.IntVar()
dinvar = tk.IntVar()
ingvar = tk.IntVar()
bedvar = tk.IntVar()
muzvar = tk.IntVar()
almvar = tk.IntVar()
cogvar = tk.IntVar()
secedbvar = tk.IntVar()
tkmtvar = tk.IntVar()
pskvar = tk.IntVar()

##################################################################################
def bilgif():
    messagebox.showinfo("Bilgi", "ebubekir07a@gmail.com")
##################################################################################
    
def alanmf():
    mf = tk.Button(pencere,text="MF",bg="green",command=alanmf)
    mf.place(relx=0.6,rely=0.90)

    tm = tk.Button(pencere,text="TM",command=alantm)
    tm.place(relx=0.67,rely=0.90)
    
    ###############################################################################################
    def girisyapma():
        derssaat=39
    ##-----------------------------------------##
        matvardeger=int(matvar.get())
        if matvardeger==0:
            matnot=0
            derssaat=derssaat-6
        else:
            matnot = float(matnotgir.get())
    ##-----------------------------------------##
        kimvardeger=int(kimvar.get())
        if kimvardeger == 0:
            kimyanot=0
            derssaat=derssaat-4
        else:
            kimyanot = float(kimyanotgir.get())
    ##-----------------------------------------##
        fizvardeger=int(fizvar.get())
        if fizvardeger == 0:
            fiziknot=0;
            derssaat=derssaat-4
        else:
            fiziknot = float(fiziknotgir.get())
    ##-----------------------------------------##
        biyovardeger=int(biyovar.get())
        if biyovardeger == 0:
            biyonot=0
            derssaat=derssaat-4
        else:
            biyonot = float(biyonotgir.get())
    ##-----------------------------------------##
        edebvardeger=int(edebvar.get())
        if edebvardeger == 0:
            edebnot=0
            derssaat=derssaat-5
        else:
            edebnot = float(edebnotgir.get())
    ##-----------------------------------------##
        tarvardeger=int(tarvar.get())
        if tarvardeger == 0:
            tarihnot=0
            derssaat=derssaat-2
        else:
            tarihnot = float(tarihnotgir.get())
    ##-----------------------------------------##
        felvardeger=int(felvar.get())
        if felvardeger==0:
            felnot=0
            derssaat=derssaat-2
        else:
            felnot = float(felnotgir.get())
    ##-----------------------------------------##
        dinvardeger=int(dinvar.get())
        if dinvardeger==0:
            dinnot=0
            derssaat=derssaat-2
        else:
            dinnot = float(dinnotgir.get())
    ##-----------------------------------------##
        ingvardeger=int(ingvar.get())
        if ingvardeger==0:
            ingnot=0
            derssaat=derssaat-4
        else:
            ingnot = float(ingnotgir.get())
    ##-----------------------------------------##
        bedvardeger=int(bedvar.get())
        if bedvardeger==0:
            bednot=0
            derssaat=derssaat-2
        else:
            bednot = float(bednotgir.get())
    ##-----------------------------------------##
        muzvardeger=int(muzvar.get())
        if muzvardeger==0:
            muziknot=0
            derssaat=derssaat-2
        else:
            muziknot = float(muziknotgir.get())
    ##-----------------------------------------##        
        almvardeger=int(almvar.get())
        if almvardeger==0:
            almnot=0
            derssaat=derssaat-2
        else:
            almnot = float(almnotgir.get())
    ##-----------------------------------------##

        mat=matnot*6
        fizik=fiziknot*4
        kimya=kimyanot*4
        biyo=biyonot*4
        edeb=edebnot*5
        tarih=tarihnot*2
        fel=felnot*2
        din=dinnot*2
        ing=ingnot*4
        bed=bednot*2
        muzik=muziknot*2
        alm=almnot*2

        ort=(mat+fizik+kimya+biyo+edeb+tarih+fel+din+ing+bed+muzik+alm)/derssaat
 ##==============================================================================================================## 
        if 70<=ort<85:
            if (0<matnot<50) or (0<fiziknot<50) or (0<kimyanot<50) or (0<biyonot<50) or (0<edebnot<50) or (0<tarihnot<50) or (0<felnot<50) or (0<dinnot<50) or (0<ingnot<50) or (0<bednot<50) or (0<muziknot<50) or (0<almnot<50):
                tak=85-ort
                belgedurum.config(text="Belge yok zayıf var", bg="red")
                tesgos.config(text="Yeterli")
                takgos.config(text=round(tak, 2))

            elif  (matnot==0) or (fiziknot==0) or (kimyanot==0) or (biyonot==0) or (edebnot==0) or (tarihnot==0) or (felnot==0) or (dinnot==0) or (ingnot==0) or (bednot==0) or (muziknot==0) or (almnot==0):
                tak=85-ort
                tesgos.config(text="Yeterli")
                takgos.config(text=round(tak, 2))
                belgedurum.config(text="Teşekkür", bg="orange")
            else:
                tak=85-ort
                tesgos.config(text="Yeterli")
                takgos.config(text=round(tak, 2))
                belgedurum.config(text="Teşekkür", bg="orange")
 ##==============================================================================================================##           
        elif 85<=ort<=100:
            if (0<matnot<50) or (0<fiziknot<50) or (0<kimyanot<50) or (0<biyonot<50) or (0<edebnot<50) or (0<tarihnot<50) or (0<felnot<50) or (0<dinnot<50) or (0<ingnot<50) or (0<bednot<50) or (0<muziknot<50) or (0<almnot<50):
                belgedurum.config(text="Belge yok zayıf var", bg="red")
                tesgos.config(text="Yeterli")
                takgos.config(text="Yeterli")
            elif (matnot==0) or (fiziknot==0) or (kimyanot==0) or (biyonot==0) or (edebnot==0) or (tarihnot==0) or (felnot==0) or (dinnot==0) or (ingnot==0) or (bednot==0) or (muziknot==0) or (almnot==0):
                belgedurum.config(text="Takdir", bg="green")
                tesgos.config(text="Yeterli")
                takgos.config(text="Yeterli")
            else:
                belgedurum.config(text="Takdir", bg="green")
                tesgos.config(text="Yeterli")
                takgos.config(text="Yeterli")
 ##===============================================================================================================##           
        else:
            tes=70-ort
            tak=85-ort
            tesgos.config(text=round(tes, 2))
            takgos.config(text=round(tak, 2))
            belgedurum.config(text="Belge yok", bg="red")
##================================================================================================================##
        girisdurumu.config(text=round(ort, 2))
        
    ###########################################################
    def temizleyici():
        matnotgir.delete(first=0,last=22)
        fiziknotgir.delete(first=0,last=22)
        kimyanotgir.delete(first=0,last=22)
        biyonotgir.delete(first=0,last=22)
        edebnotgir.delete(first=0,last=22)
        tarihnotgir.delete(first=0,last=22)
        felnotgir.delete(first=0,last=22)
        dinnotgir.delete(first=0,last=22)
        ingnotgir.delete(first=0,last=22)
        bednotgir.delete(first=0,last=22)
        muziknotgir.delete(first=0,last=22)
        almnotgir.delete(first=0,last=22)
    ##############################################################    


    #############################################################3
    
    matchk  = tk.Checkbutton(pencere,text = "Matematik=",
                             variable= matvar,width="10",anchor="w")
    matchk.grid(row=0,column=0)
    matnotgir = tk.Entry(pencere,width="8")
    matnotgir.grid(row=0,column=1)
    matchk.select()

##================================================================
    
    fizikchk = tk.Checkbutton(pencere,width=10, text="Fizik=",
                              variable= fizvar,anchor="w")
    fizikchk.grid(row=1,column=0)
    fiziknotgir = tk.Entry(pencere,width="8")
    fiziknotgir.grid(row=1,column=1)
    fizikchk.select()
##================================================================    
    
    kimyachk  = tk.Checkbutton(pencere,width=10,text = "Kimya=",
                               variable=kimvar,anchor="w")
    kimyachk.grid(row=2,column=0)
    kimyanotgir = tk.Entry(pencere,width="8")
    kimyanotgir.grid(row=2,column=1)
    kimyachk.select()
 ##================================================================   
    
    
    biyochk = tk.Checkbutton(pencere,width=10, text="Biyoloji=",
                             variable=biyovar,anchor="w")
    biyochk.grid(row=3,column=0)
    biyonotgir = tk.Entry(pencere,width="8")
    biyonotgir.grid(row=3,column=1)
    biyochk.select()
 ##================================================================   
    
    edebchk = tk.Checkbutton(pencere,width=10, text="Edebiyat=",
                             variable=edebvar,anchor="w")
    edebchk.grid(row=4,column=0)
    edebnotgir = tk.Entry(pencere,width="8")
    edebnotgir.grid(row=4,column=1)
    edebchk.select()
##================================================================    
    
    tarihchk = tk.Checkbutton(pencere,width=10, text="Tarih=",
                              variable=tarvar,anchor="w")
    tarihchk.grid(row=5,column=0)
    tarihnotgir = tk.Entry(pencere,width="8")
    tarihnotgir.grid(row=5,column=1)
    tarihchk.select()
##================================================================    
    
    felchk = tk.Checkbutton(pencere,width=10, text="Felsefe=",
                            variable=felvar,anchor="w")
    felchk.grid(row=6,column=0)
    felnotgir = tk.Entry(pencere,width="8")
    felnotgir.grid(row=6,column=1)
    felchk.select()
##================================================================    
    dinchk = tk.Checkbutton(pencere,width=10, text="Din K.=",
                            variable=dinvar,anchor="w")
    dinchk.grid(row=7,column=0)
    dinnotgir = tk.Entry(pencere,width="8")
    dinnotgir.grid(row=7,column=1)
    dinchk.select()
##================================================================    
    
    ingchk = tk.Checkbutton(pencere,width=10, text="İngilizce=",
                            variable=ingvar,anchor="w")
    ingchk.grid(row=8,column=0)
    ingnotgir = tk.Entry(pencere,width="8")
    ingnotgir.grid(row=8,column=1)
    ingchk.select()
##================================================================    
    bedchk = tk.Checkbutton(pencere,width=10, text="Beden=",
                            variable=bedvar,anchor="w")
    bedchk.grid(row=9,column=0)
    bednotgir = tk.Entry(pencere,width="8")
    bednotgir.grid(row=9,column=1)
    bedchk.select()
##================================================================    
    muzikchk = tk.Checkbutton(pencere,width=10, text="Müz/Gör=",
                              variable=muzvar,anchor="w")
    muzikchk.grid(row=10,column=0)
    muziknotgir = tk.Entry(pencere,width="8")
    muziknotgir.grid(row=10,column=1)
    muzikchk.select()
##================================================================    
    almchk = tk.Checkbutton(pencere,width=10, text="Almanca=",
                            variable=almvar,anchor="w")
    almchk.grid(row=11,column=0)
    almnotgir = tk.Entry(pencere,width="8")
    almnotgir.grid(row=11,column=1)
    almchk.select()
##================================================================    
    pskchk = tk.Label(pencere,width=12, text="",anchor="w")
    pskchk.grid(row=12,column=0)
    psknotgir  = tk.Label(pencere,width="8",text = "")
    psknotgir.grid(row=12,column=1)
########################################################################    

    temizle = tk.Button(pencere,text="Temizle",command=temizleyici)
    temizle.grid(row=12,column=4)
##----------------------------------------------------------------------------------    
    giris = tk.Button(pencere,text="Hesapla",command=girisyapma)
    giris.grid(row=12,column=3)
    girisdurumu = tk.Label(pencere,width=15,text="")
    girisdurumu.grid(row=0,column=6)
#############################################################################
def alantm():
    mf = tk.Button(pencere,text="MF",command=alanmf)
    mf.place(relx=0.6,rely=0.90)

    tm = tk.Button(pencere,text="TM",bg="green",command=alantm)
    tm.place(relx=0.67,rely=0.90)
###########----------------------------------------------------#############    
    def girisyapma():
        derssaat=38
    ##-----------------------------------------##
        matvardeger=int(matvar.get())
        if matvardeger==0:
            matnot=0
            derssaat=derssaat-6
        else:
            matnot = float(matnotgir.get())
    ##-----------------------------------------##
        cogvardeger=int(cogvar.get())
        if cogvardeger == 0:
            cognot=0
            derssaat=derssaat-4
        else:
            cognot = float(cognotgir.get())
    ##-----------------------------------------##
        secedbvardeger=int(secedbvar.get())
        if secedbvardeger == 0:
            secedbnot=0;
            derssaat=derssaat-3
        else:
            secedbnot = float(secedbnotgir.get())
    ##-----------------------------------------##
        tkmtvardeger=int(tkmtvar.get())
        if tkmtvardeger == 0:
            tkmtnot=0
            derssaat=derssaat-2
        else:
            tkmtnot = float(tkmtnotgir.get())
    ##-----------------------------------------##
        edebvardeger=int(edebvar.get())
        if edebvardeger == 0:
            edebnot=0
            derssaat=derssaat-5
        else:
            edebnot = float(edebnotgir.get())
    ##-----------------------------------------##
        tarvardeger=int(tarvar.get())
        if tarvardeger == 0:
            tarihnot=0
            derssaat=derssaat-2
        else:
            tarihnot = float(tarihnotgir.get())
    ##-----------------------------------------##
        felvardeger=int(felvar.get())
        if felvardeger==0:
            felnot=0
            derssaat=derssaat-2
        else:
            felnot = float(felnotgir.get())
    ##-----------------------------------------##
        dinvardeger=int(dinvar.get())
        if dinvardeger==0:
            dinnot=0
            derssaat=derssaat-2
        else:
            dinnot = float(dinnotgir.get())
    ##-----------------------------------------##
        ingvardeger=int(ingvar.get())
        if ingvardeger==0:
            ingnot=0
            derssaat=derssaat-4
        else:
            ingnot = float(ingnotgir.get())
    ##-----------------------------------------##
        bedvardeger=int(bedvar.get())
        if bedvardeger==0:
            bednot=0
            derssaat=derssaat-2
        else:
            bednot = float(bednotgir.get())
    ##-----------------------------------------##
        muzvardeger=int(muzvar.get())
        if muzvardeger==0:
            muziknot=0
            derssaat=derssaat-2
        else:
            muziknot = float(muziknotgir.get())
    ##-----------------------------------------##        
        almvardeger=int(almvar.get())
        if almvardeger==0:
            almnot=0
            derssaat=derssaat-2
        else:
            almnot = float(almnotgir.get())
    ##-----------------------------------------##
        pskvardeger=int(pskvar.get())
        if pskvardeger==0:
            psknot=0
            derssaat=derssaat-2
        else:
            psknot = float(psknotgir.get())
    ##-----------------------------------------##
        mat=matnot*6
        cog=cognot*4
        secedb=secedbnot*3
        tkmt=tkmtnot*2
        edeb=edebnot*5
        tarih=tarihnot*2
        fel=felnot*2
        din=dinnot*2
        ing=ingnot*4
        bed=bednot*2
        muzik=muziknot*2
        alm=almnot*2
        psk=psknot*2
#####################################################################################################
        ort=(mat+cog+secedb+tkmt+edeb+tarih+fel+din+ing+bed+muzik+alm+psk)/derssaat
  ##==============================================================================================================##    
        if 70<=ort<85:
            if (0<matnot<50) or (0<cognot<50) or (0<psknot<50) or (0<secedbnot<50) or (0<tkmtnot<50) or (0<edebnot<50) or (0<tarihnot<50) or (0<felnot<50) or (0<dinnot<50) or (0<ingnot<50) or (0<bednot<50) or (0<muziknot<50) or (0<almnot<50):
                tak=85-ort
                belgedurum.config(text="Belge yok zayıf var", bg="red")
                tesgos.config(text="Yeterli")
                takgos.config(text=round(tak, 2))
            elif (matnot==0) or (cognot==0) or (psknot==0) or (secedbnot==0) or (tkmtnot==0) or (edebnot==0) or (tarihnot==0) or (felnot==0) or (dinnot==0) or (ingnot==0) or (bednot==0) or (muziknot==0) or (almnot==0):
                tak=85-ort
                tesgos.config(text="Yeterli")
                takgos.config(text=round(tak, 2))
                belgedurum.config(text="Teşekkür", bg="orange")
            else:
                tak=85-ort
                tesgos.config(text="Yeterli")
                takgos.config(text=round(tak, 2))
                belgedurum.config(text="Teşekkür", bg="orange")
 ##==============================================================================================================##             
        elif 85<=ort<=100:
            if (0<matnot<50) or (0<cognot<50) or (0<psknot<50) or (0<secedbnot<50) or (0<tkmtnot<50) or (0<edebnot<50) or (0<tarihnot<50) or (0<felnot<50) or (0<dinnot<50) or (0<ingnot<50) or (0<bednot<50) or (0<muziknot<50) or (0<almnot<50):
                belgedurum.config(text="Belge yok zayıf var", bg="red")
                tesgos.config(text="Yeterli")
                takgos.config(text="Yeterli")
            
            elif (matnot==0) or (cognot==0) or (psknot==0) or (secedbnot==0) or (tkmtnot==0) or (edebnot==0) or (tarihnot==0) or (felnot==0) or (dinnot==0) or (ingnot==0) or (bednot==0) or (muziknot==0) or (almnot==0):
                belgedurum.config(text="Takdir", bg="green")
                tesgos.config(text="Yeterli")
                takgos.config(text="Yeterli")
            else:
                belgedurum.config(text="Takdir", bg="green")
                tesgos.config(text="Yeterli")
                takgos.config(text="Yeterli")
  ##==============================================================================================================##                
        else:
            tes=70-ort
            tak=85-ort
            tesgos.config(text=round(tes, 2))
            takgos.config(text=round(tak, 2))
            belgedurum.config(text="Belge yok", bg="red")
 ##==============================================================================================================##       
        girisdurumu.config(text=round(ort, 2))
########################################################
    def temizleyici():
        matnotgir.delete(first=0,last=22)
        cognotgir.delete(first=0,last=22)
        secedbnotgir.delete(first=0,last=22)
        tkmtnotgir.delete(first=0,last=22)
        edebnotgir.delete(first=0,last=22)
        tarihnotgir.delete(first=0,last=22)
        felnotgir.delete(first=0,last=22)
        dinnotgir.delete(first=0,last=22)
        ingnotgir.delete(first=0,last=22)
        bednotgir.delete(first=0,last=22)
        muziknotgir.delete(first=0,last=22)
        almnotgir.delete(first=0,last=22)
        psknotgir.delete(first=0,last=22)
 ##================================================================        
    matchk  = tk.Checkbutton(pencere,text = "Matematik=",
                             variable= matvar,width="10",anchor="w")
    matchk.grid(row=0,column=0)
    matnotgir = tk.Entry(pencere,width="8")
    matnotgir.grid(row=0,column=1)
    matchk.select()
 ##================================================================    
    cogchk  = tk.Checkbutton(pencere,text = "Coğrafya=",
                             variable= cogvar,width="10",anchor="w")
    cogchk.grid(row=1,column=0)
    cognotgir = tk.Entry(pencere,width="8")
    cognotgir.grid(row=1,column=1)
    cogchk.select()
 ##================================================================    
    secedbchk  = tk.Checkbutton(pencere,text = "Seçmeli Edb.=",
                                variable= secedbvar,width="10",anchor="w")
    secedbchk.grid(row=2,column=0)
    secedbnotgir = tk.Entry(pencere,width="8")
    secedbnotgir.grid(row=2,column=1)
    secedbchk.select()
 ##================================================================    
    tkmtchk  = tk.Checkbutton(pencere,text = "Tkmt=",
                              variable= tkmtvar,width="10",anchor="w")
    tkmtchk.grid(row=3,column=0)
    tkmtnotgir = tk.Entry(pencere,width="8")
    tkmtnotgir.grid(row=3,column=1)
    tkmtchk.select()
 ##================================================================
    edebchk = tk.Checkbutton(pencere, text="Edebiyat=",
                             variable=edebvar,width="10",anchor="w")
    edebchk.grid(row=4,column=0)
    edebnotgir = tk.Entry(pencere,width="8")
    edebnotgir.grid(row=4,column=1)
    edebchk.select()
 ##================================================================
    tarihchk = tk.Checkbutton(pencere, text="Tarih=",
                              variable=tarvar,width="10",anchor="w")
    tarihchk.grid(row=5,column=0)
    tarihnotgir = tk.Entry(pencere,width="8")
    tarihnotgir.grid(row=5,column=1)
    tarihchk.select()
 ##================================================================
    felchk = tk.Checkbutton(pencere, text="Felsefe=",
                            variable=felvar,width="10",anchor="w")
    felchk.grid(row=6,column=0)
    felnotgir = tk.Entry(pencere,width="8")
    felnotgir.grid(row=6,column=1)
    felchk.select()
 ##================================================================
    dinchk = tk.Checkbutton(pencere,text="Din K.=",
                            variable=dinvar,width="10",anchor="w")
    dinchk.grid(row=7,column=0)
    dinnotgir = tk.Entry(pencere,width="8")
    dinnotgir.grid(row=7,column=1)
    dinchk.select()
 ##================================================================
    ingchk = tk.Checkbutton(pencere,text="İngilizce=",
                            variable=ingvar,width="10",anchor="w")
    ingchk.grid(row=8,column=0)
    ingnotgir = tk.Entry(pencere,width="8")
    ingnotgir.grid(row=8,column=1)
    ingchk.select()
##================================================================
    bedchk = tk.Checkbutton(pencere,text="Beden=",
                            variable=bedvar,width="10",anchor="w")
    bedchk.grid(row=9,column=0)
    bednotgir = tk.Entry(pencere,width="8")
    bednotgir.grid(row=9,column=1)
    bedchk.select()
 ##================================================================
    muzikchk = tk.Checkbutton(pencere,text="Müz/Gör=",
                              variable=muzvar,width="10",anchor="w")
    muzikchk.grid(row=10,column=0)
    muziknotgir = tk.Entry(pencere,width="8")
    muziknotgir.grid(row=10,column=1)
    muzikchk.select()
 ##================================================================
    almchk = tk.Checkbutton(pencere,text="Almanca=",
                            variable=almvar,width="10",anchor="w")
    almchk.grid(row=11,column=0)
    almnotgir = tk.Entry(pencere,width="8")
    almnotgir.grid(row=11,column=1)
    almchk.select()
 ##================================================================    
    pskchk = tk.Checkbutton(pencere,text="Psikoloji=",
                            variable=pskvar,width="10",anchor="w")
    pskchk.grid(row=12,column=0)
    psknotgir = tk.Entry(pencere,width="8")
    psknotgir.grid(row=12,column=1)
    pskchk.select()
 ##================================================================
    temizle = tk.Button(pencere,text="Temizle",command=temizleyici)
    temizle.grid(row=12,column=4)
########################################################################    
    giris = tk.Button(pencere,text="Hesapla",command=girisyapma)
    giris.grid(row=12,column=3)
    girisdurumu = tk.Label(pencere,width=15,text="")
    girisdurumu.grid(row=0,column=6)
##----------------------------------------------------------------------
   
bilgi = tk.Button(pencere,text="Bilgi",command=bilgif)
bilgi.place(relx=0.92,rely=0.9)
##----------------------------------------------------------------------
command=alanmf()
tesk = tk.Label(pencere,width=22,anchor="w",text="Teşekkür için gereken puan=")
tesk.grid(row=1,column=5)
tesgos=tk.Label(pencere,width=15,text="")
tesgos.grid(row=1,column=6)
##----------------------------------------------------------------------
takd = tk.Label(pencere,width=22,anchor="w",text="Takdir için gereken puan=")
takd.grid(row=2,column=5)
takgos=tk.Label(pencere,width=15,text="")
takgos.grid(row=2,column=6)
##----------------------------------------------------------------------
belge = tk.Label(pencere,width=22,anchor="w",text="Belge=")
belge.grid(row=3,column=5)
belgedurum=tk.Label(pencere,font=("Comic Sans MS",11,"bold"),width=15,text="")
belgedurum.grid(row=3,column=6)
##----------------------------------------------------------------------
sonuc = tk.Label(pencere,width=22,anchor="w",text="Ortalama=")
sonuc.grid(row=0,column=5)
##----------------------------------------------------------------------
mf = tk.Button(pencere,text="MF",bg="green",command=alanmf)
mf.place(relx=0.6,rely=0.90)
##----------------------------------------------------------------------
tm = tk.Button(pencere,text="TM",command=alantm)
tm.place(relx=0.67,rely=0.90)
##----------------------------------------------------------------------
dikkat = tk.Label(pencere,width=30,height=10,text="Uyarı: 0(sıfır) notu kabul edilmez.\n"
                  "Girildiğinde hatalı sonuç verebilir.",anchor="nw")
dikkat.grid(row=4,rowspan=8,column=4,columnspan=6,sticky="w")
##----------------------------------------------------------------------


pencere.mainloop()
