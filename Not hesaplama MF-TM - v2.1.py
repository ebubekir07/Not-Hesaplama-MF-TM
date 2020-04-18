import tkinter as tk

from tkinter import messagebox
pencere = tk.Tk()
pencere.title("Not Hesaplayıcı MF-TM v2.1")
pencere.geometry("570x340")

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

matsv=tk.IntVar()
fizsv=tk.IntVar()
kimsv=tk.IntVar()
biyosv=tk.IntVar()
edebsv=tk.IntVar()
tarsv=tk.IntVar()
felsv=tk.IntVar()
dinsv=tk.IntVar()
ingsv=tk.IntVar()
bedsv=tk.IntVar()
muzsv=tk.IntVar()
almsv=tk.IntVar()
cogsv=tk.IntVar()
secedbsv=tk.IntVar()
tkmtsv=tk.IntVar()
psksv=tk.IntVar()

##################################################################################
def bilgif():
    messagebox.showinfo("Bilgi", "ebubekir07a@gmail.com")
##################################################################################
    
def alanmf():
    mf = tk.Button(pencere,text="MF",bg="green",command=alanmf)
    mf.place(relx=0.68,rely=0.90)

    tm = tk.Button(pencere,text="TM",command=alantm)
    tm.place(relx=0.74,rely=0.90)

    dersgos.config(text="")
    tesgos.config(text="")
    takgos.config(text="")
    belgedurum.config(text="")
    
    ###############################################################################################
    def girisyapma():
        matders=int(matsv.get())
        kimders=int(kimsv.get())
        fizders=int(fizsv.get())
        biyoders=int(biyosv.get())
        edebders=int(edebsv.get())
        tarders=int(tarsv.get())
        felders=int(felsv.get())
        dinders=int(dinsv.get())
        ingders=int(ingsv.get())
        bedders=int(bedsv.get())
        muzders=int(muzsv.get())
        almders=int(almsv.get())
                    
        derssaat= matders + kimders +fizders +biyoders+edebders+tarders+felders+dinders+ingders+bedders+muzders+almders
    ##-----------------------------------------##
        matvardeger=int(matvar.get())
        if matvardeger==0:
            matnot=0
            derssaat=derssaat-matders
        else:
            matnot = float(matnotgir.get())
    ##-----------------------------------------##
        kimvardeger=int(kimvar.get())
        if kimvardeger == 0:
            kimyanot=0
            derssaat=derssaat-kimders
        else:
            kimyanot = float(kimyanotgir.get())
    ##-----------------------------------------##
        fizvardeger=int(fizvar.get())
        if fizvardeger == 0:
            fiziknot=0;
            derssaat=derssaat-fizders
        else:
            fiziknot = float(fiziknotgir.get())
    ##-----------------------------------------##
        biyovardeger=int(biyovar.get())
        if biyovardeger == 0:
            biyonot=0
            derssaat=derssaat-biyoders
        else:
            biyonot = float(biyonotgir.get())
    ##-----------------------------------------##
        edebvardeger=int(edebvar.get())
        if edebvardeger == 0:
            edebnot=0
            derssaat=derssaat-edebders
        else:
            edebnot = float(edebnotgir.get())
    ##-----------------------------------------##
        tarvardeger=int(tarvar.get())
        if tarvardeger == 0:
            tarihnot=0
            derssaat=derssaat-tarders
        else:
            tarihnot = float(tarihnotgir.get())
    ##-----------------------------------------##
        felvardeger=int(felvar.get())
        if felvardeger==0:
            felnot=0
            derssaat=derssaat-felders
        else:
            felnot = float(felnotgir.get())
    ##-----------------------------------------##
        dinvardeger=int(dinvar.get())
        if dinvardeger==0:
            dinnot=0
            derssaat=derssaat-dinders
        else:
            dinnot = float(dinnotgir.get())
    ##-----------------------------------------##
        ingvardeger=int(ingvar.get())
        if ingvardeger==0:
            ingnot=0
            derssaat=derssaat-ingders
        else:
            ingnot = float(ingnotgir.get())
    ##-----------------------------------------##
        bedvardeger=int(bedvar.get())
        if bedvardeger==0:
            bednot=0
            derssaat=derssaat-bedders
        else:
            bednot = float(bednotgir.get())
    ##-----------------------------------------##
        muzvardeger=int(muzvar.get())
        if muzvardeger==0:
            muziknot=0
            derssaat=derssaat-muzders
        else:
            muziknot = float(muziknotgir.get())
    ##-----------------------------------------##        
        almvardeger=int(almvar.get())
        if almvardeger==0:
            almnot=0
            derssaat=derssaat-almders
        else:
            almnot = float(almnotgir.get())
    ##-----------------------------------------##

        mat=matnot*matders
        fizik=fiziknot*fizders
        kimya=kimyanot*kimders
        biyo=biyonot*biyoders
        edeb=edebnot*edebders
        tarih=tarihnot*tarders
        fel=felnot*felders
        din=dinnot*dinders
        ing=ingnot*ingders
        bed=bednot*bedders
        muzik=muziknot*muzders
        alm=almnot*almders
        
        dersgos.config(text=derssaat)
        
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
    matsv.set(6)
    matspin=tk.Spinbox(pencere,from_=1,to=10,width=2,textvariable=matsv)
    matspin.grid(row=0,column=2,sticky="w")
    matchk.select()

##================================================================
    
    fizikchk = tk.Checkbutton(pencere,width=10, text="Fizik=",
                              variable= fizvar,anchor="w")
    fizikchk.grid(row=1,column=0)
    fiziknotgir = tk.Entry(pencere,width="8")
    fiziknotgir.grid(row=1,column=1)
    fizsv.set(4)
    fizspin=tk.Spinbox(pencere,from_=1,to=10,width=2,textvariable=fizsv)
    fizspin.grid(row=1,column=2,sticky="w")
    fizikchk.select()
##================================================================    
    
    kimyachk  = tk.Checkbutton(pencere,width=10,text = "Kimya=",
                               variable=kimvar,anchor="w")
    kimyachk.grid(row=2,column=0)
    kimyanotgir = tk.Entry(pencere,width="8")
    kimyanotgir.grid(row=2,column=1)
    kimsv.set(4)
    kimspin=tk.Spinbox(pencere,from_=1,to=10,width=2,textvariable=kimsv)
    kimspin.grid(row=2,column=2,sticky="w")
    kimyachk.select()
 ##================================================================   
    
    
    biyochk = tk.Checkbutton(pencere,width=10, text="Biyoloji=",
                             variable=biyovar,anchor="w")
    biyochk.grid(row=3,column=0)
    biyonotgir = tk.Entry(pencere,width="8")
    biyonotgir.grid(row=3,column=1)
    biyosv.set(4)
    biyospin=tk.Spinbox(pencere,from_=1,to=10,width=2,textvariable=biyosv)
    biyospin.grid(row=3,column=2,sticky="w")
    biyochk.select()
 ##================================================================   
    
    edebchk = tk.Checkbutton(pencere,width=10, text="Edebiyat=",
                             variable=edebvar,anchor="w")
    edebchk.grid(row=4,column=0)
    edebnotgir = tk.Entry(pencere,width="8")
    edebnotgir.grid(row=4,column=1)
    edebsv.set(5)
    edebspin=tk.Spinbox(pencere,from_=1,to=10,width=2,textvariable=edebsv)
    edebspin.grid(row=4,column=2,sticky="w")
    edebchk.select()
##================================================================    
    
    tarihchk = tk.Checkbutton(pencere,width=10, text="Tarih=",
                              variable=tarvar,anchor="w")
    tarihchk.grid(row=5,column=0)
    tarihnotgir = tk.Entry(pencere,width="8")
    tarihnotgir.grid(row=5,column=1)
    tarsv.set(2)
    tarspin=tk.Spinbox(pencere,from_=1,to=10,width=2,textvariable=tarsv)
    tarspin.grid(row=5,column=2,sticky="w")
    tarihchk.select()
##================================================================    
    
    felchk = tk.Checkbutton(pencere,width=10, text="Felsefe=",
                            variable=felvar,anchor="w")
    felchk.grid(row=6,column=0)
    felnotgir = tk.Entry(pencere,width="8")
    felnotgir.grid(row=6,column=1)
    felsv.set(2)
    felspin=tk.Spinbox(pencere,from_=1,to=10,width=2,textvariable=felsv)
    felspin.grid(row=6,column=2,sticky="w")
    felchk.select()
##================================================================    
    dinchk = tk.Checkbutton(pencere,width=10, text="Din K.=",
                            variable=dinvar,anchor="w")
    dinchk.grid(row=7,column=0)
    dinnotgir = tk.Entry(pencere,width="8")
    dinnotgir.grid(row=7,column=1)
    dinsv.set(2)
    dinspin=tk.Spinbox(pencere,from_=1,to=10,width=2,textvariable=dinsv)
    dinspin.grid(row=7,column=2,sticky="w")
    dinchk.select()
##================================================================    
    
    ingchk = tk.Checkbutton(pencere,width=10, text="İngilizce=",
                            variable=ingvar,anchor="w")
    ingchk.grid(row=8,column=0)
    ingnotgir = tk.Entry(pencere,width="8")
    ingnotgir.grid(row=8,column=1)
    ingsv.set(4)
    ingspin=tk.Spinbox(pencere,from_=1,to=10,width=2,textvariable=ingsv)
    ingspin.grid(row=8,column=2,sticky="w")
    ingchk.select()
##================================================================    
    bedchk = tk.Checkbutton(pencere,width=10, text="Beden=",
                            variable=bedvar,anchor="w")
    bedchk.grid(row=9,column=0)
    bednotgir = tk.Entry(pencere,width="8")
    bednotgir.grid(row=9,column=1)
    bedsv.set(2)
    bedspin=tk.Spinbox(pencere,from_=1,to=10,width=2,textvariable=bedsv)
    bedspin.grid(row=9,column=2,sticky="w")
    bedchk.select()
##================================================================    
    muzikchk = tk.Checkbutton(pencere,width=10, text="Müz/Gör=",
                              variable=muzvar,anchor="w")
    muzikchk.grid(row=10,column=0)
    muziknotgir = tk.Entry(pencere,width="8")
    muziknotgir.grid(row=10,column=1)
    muzsv.set(2)
    muzspin=tk.Spinbox(pencere,from_=1,to=10,width=2,textvariable=muzsv)
    muzspin.grid(row=10,column=2,sticky="w")
    muzikchk.select()
##================================================================    
    almchk = tk.Checkbutton(pencere,width=10, text="Almanca=",
                            variable=almvar,anchor="w")
    almchk.grid(row=11,column=0)
    almnotgir = tk.Entry(pencere,width="8")
    almnotgir.grid(row=11,column=1)
    almsv.set(2)
    almspin=tk.Spinbox(pencere,from_=1,to=10,width=2,textvariable=almsv)
    almspin.grid(row=11,column=2,sticky="w")
    almchk.select()
##================================================================    
    pskchk = tk.Label(pencere,width=12, text="",anchor="w")
    pskchk.grid(row=12,column=0)
    psknotgir  = tk.Label(pencere,width="8",text = "")
    psknotgir.grid(row=12,column=1)
    pskspin  = tk.Label(pencere,width="3",text = "")
    pskspin.grid(row=12,column=2,sticky="w")
########################################################################    

    temizle = tk.Button(pencere,text="Temizle",command=temizleyici)
    temizle.place(relx=0.47,rely=0.90)
##----------------------------------------------------------------------------------    
    giris = tk.Button(pencere,text="Hesapla",command=girisyapma)
    giris.place(relx=0.37,rely=0.90)
    girisdurumu = tk.Label(pencere,width=15,text="")
    girisdurumu.grid(row=0,column=5)
#############################################################################
def alantm():
    mf = tk.Button(pencere,text="MF",command=alanmf)
    mf.place(relx=0.68,rely=0.90)

    tm = tk.Button(pencere,text="TM",bg="green",command=alantm)
    tm.place(relx=0.74,rely=0.90)

    dersgos.config(text="")
    tesgos.config(text="")
    takgos.config(text="")
    belgedurum.config(text="")
###########----------------------------------------------------#############    
    def girisyapma():
        matders=int(matsv.get())
        edebders=int(edebsv.get())
        tarders=int(tarsv.get())
        felders=int(felsv.get())
        dinders=int(dinsv.get())
        ingders=int(ingsv.get())
        bedders=int(bedsv.get())
        muzders=int(muzsv.get())
        almders=int(almsv.get())
        cogders=int(cogsv.get())
        secedbders=int(secedbsv.get())
        tkmtders=int(tkmtsv.get())
        pskders=int(psksv.get())
                    
        derssaat= matders + cogders +secedbders +tkmtders+pskders+edebders+tarders+felders+dinders+ingders+bedders+muzders+almders
     ##-----------------------------------------##
        matvardeger=int(matvar.get())
        if matvardeger==0:
            matnot=0
            derssaat=derssaat-matders
        else:
            matnot = float(matnotgir.get())
    ##-----------------------------------------##
        cogvardeger=int(cogvar.get())
        if cogvardeger == 0:
            cognot=0
            derssaat=derssaat-cogders
        else:
            cognot = float(cognotgir.get())
    ##-----------------------------------------##
        secedbvardeger=int(secedbvar.get())
        if secedbvardeger == 0:
            secedbnot=0;
            derssaat=derssaat-secedbders
        else:
            secedbnot = float(secedbnotgir.get())
    ##-----------------------------------------##
        tkmtvardeger=int(tkmtvar.get())
        if tkmtvardeger == 0:
            tkmtnot=0
            derssaat=derssaat-tkmtders
        else:
            tkmtnot = float(tkmtnotgir.get())
    ##-----------------------------------------##
        edebvardeger=int(edebvar.get())
        if edebvardeger == 0:
            edebnot=0
            derssaat=derssaat-edebders
        else:
            edebnot = float(edebnotgir.get())
    ##-----------------------------------------##
        tarvardeger=int(tarvar.get())
        if tarvardeger == 0:
            tarihnot=0
            derssaat=derssaat-tarders
        else:
            tarihnot = float(tarihnotgir.get())
    ##-----------------------------------------##
        felvardeger=int(felvar.get())
        if felvardeger==0:
            felnot=0
            derssaat=derssaat-felders
        else:
            felnot = float(felnotgir.get())
    ##-----------------------------------------##
        dinvardeger=int(dinvar.get())
        if dinvardeger==0:
            dinnot=0
            derssaat=derssaat-dinders
        else:
            dinnot = float(dinnotgir.get())
    ##-----------------------------------------##
        ingvardeger=int(ingvar.get())
        if ingvardeger==0:
            ingnot=0
            derssaat=derssaat-ingders
        else:
            ingnot = float(ingnotgir.get())
    ##-----------------------------------------##
        bedvardeger=int(bedvar.get())
        if bedvardeger==0:
            bednot=0
            derssaat=derssaat-bedders
        else:
            bednot = float(bednotgir.get())
    ##-----------------------------------------##
        muzvardeger=int(muzvar.get())
        if muzvardeger==0:
            muziknot=0
            derssaat=derssaat-muzders
        else:
            muziknot = float(muziknotgir.get())
    ##-----------------------------------------##        
        almvardeger=int(almvar.get())
        if almvardeger==0:
            almnot=0
            derssaat=derssaat-almders
        else:
            almnot = float(almnotgir.get())
    ##-----------------------------------------##
        pskvardeger=int(pskvar.get())
        if pskvardeger==0:
            psknot=0
            derssaat=derssaat-pskders
        else:
            psknot = float(psknotgir.get())
    ##-----------------------------------------##
        mat=matnot*matders
        cog=cognot*cogders
        secedb=secedbnot*secedbders
        tkmt=tkmtnot*tkmtders
        edeb=edebnot*edebders
        tarih=tarihnot*tarders
        fel=felnot*felders
        din=dinnot*dinders
        ing=ingnot*ingders
        bed=bednot*bedders
        muzik=muziknot*muzders
        alm=almnot*almders
        psk=psknot*pskders

        dersgos.config(text=derssaat)
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
                takgos.config(tjext="Yeterli")
            
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
    matsv.set(6)
    matspin=tk.Spinbox(pencere,from_=1,to=10,width=2,textvariable=matsv)
    matspin.grid(row=0,column=2,sticky="w")
    matchk.select()
 ##================================================================    
    cogchk  = tk.Checkbutton(pencere,text = "Coğrafya=",
                             variable= cogvar,width="10",anchor="w")
    cogchk.grid(row=1,column=0)
    cognotgir = tk.Entry(pencere,width="8")
    cognotgir.grid(row=1,column=1)
    cogsv.set(4)
    cogspin=tk.Spinbox(pencere,from_=1,to=10,width=2,textvariable=cogsv)
    cogspin.grid(row=1,column=2,sticky="w")
    cogchk.select()
 ##================================================================    
    secedbchk  = tk.Checkbutton(pencere,text = "Seçmeli Edb.=",
                                variable= secedbvar,width="10",anchor="w")
    secedbchk.grid(row=2,column=0)
    secedbnotgir = tk.Entry(pencere,width="8")
    secedbnotgir.grid(row=2,column=1)
    secedbsv.set(3)
    secedbspin=tk.Spinbox(pencere,from_=1,to=10,width=2,textvariable=secedbsv)
    secedbspin.grid(row=2,column=2,sticky="w")
    secedbchk.select()
 ##================================================================    
    tkmtchk  = tk.Checkbutton(pencere,text = "Tkmt=",
                              variable= tkmtvar,width="10",anchor="w")
    tkmtchk.grid(row=3,column=0)
    tkmtnotgir = tk.Entry(pencere,width="8")
    tkmtnotgir.grid(row=3,column=1)
    tkmtsv.set(2)
    tkmtspin=tk.Spinbox(pencere,from_=1,to=10,width=2,textvariable=tkmtsv)
    tkmtspin.grid(row=3,column=2,sticky="w")
    tkmtchk.select()
 ##================================================================
    edebchk = tk.Checkbutton(pencere,width=10, text="Edebiyat=",
                             variable=edebvar,anchor="w")
    edebchk.grid(row=4,column=0)
    edebnotgir = tk.Entry(pencere,width="8")
    edebnotgir.grid(row=4,column=1)
    edebsv.set(5)
    edebspin=tk.Spinbox(pencere,from_=1,to=10,width=2,textvariable=edebsv)
    edebspin.grid(row=4,column=2,sticky="w")
    edebchk.select()
##================================================================    
    
    tarihchk = tk.Checkbutton(pencere,width=10, text="Tarih=",
                              variable=tarvar,anchor="w")
    tarihchk.grid(row=5,column=0)
    tarihnotgir = tk.Entry(pencere,width="8")
    tarihnotgir.grid(row=5,column=1)
    tarsv.set(2)
    tarspin=tk.Spinbox(pencere,from_=1,to=10,width=2,textvariable=tarsv)
    tarspin.grid(row=5,column=2,sticky="w")
    tarihchk.select()
##================================================================    
    
    felchk = tk.Checkbutton(pencere,width=10, text="Felsefe=",
                            variable=felvar,anchor="w")
    felchk.grid(row=6,column=0)
    felnotgir = tk.Entry(pencere,width="8")
    felnotgir.grid(row=6,column=1)
    felsv.set(2)
    felspin=tk.Spinbox(pencere,from_=1,to=10,width=2,textvariable=felsv)
    felspin.grid(row=6,column=2,sticky="w")
    felchk.select()
##================================================================    
    dinchk = tk.Checkbutton(pencere,width=10, text="Din K.=",
                            variable=dinvar,anchor="w")
    dinchk.grid(row=7,column=0)
    dinnotgir = tk.Entry(pencere,width="8")
    dinnotgir.grid(row=7,column=1)
    dinsv.set(2)
    dinspin=tk.Spinbox(pencere,from_=1,to=10,width=2,textvariable=dinsv)
    dinspin.grid(row=7,column=2,sticky="w")
    dinchk.select()
##================================================================    
    
    ingchk = tk.Checkbutton(pencere,width=10, text="İngilizce=",
                            variable=ingvar,anchor="w")
    ingchk.grid(row=8,column=0)
    ingnotgir = tk.Entry(pencere,width="8")
    ingnotgir.grid(row=8,column=1)
    ingsv.set(4)
    ingspin=tk.Spinbox(pencere,from_=1,to=10,width=2,textvariable=ingsv)
    ingspin.grid(row=8,column=2,sticky="w")
    ingchk.select()
##================================================================    
    bedchk = tk.Checkbutton(pencere,width=10, text="Beden=",
                            variable=bedvar,anchor="w")
    bedchk.grid(row=9,column=0)
    bednotgir = tk.Entry(pencere,width="8")
    bednotgir.grid(row=9,column=1)
    bedsv.set(2)
    bedspin=tk.Spinbox(pencere,from_=1,to=10,width=2,textvariable=bedsv)
    bedspin.grid(row=9,column=2,sticky="w")
    bedchk.select()
##================================================================    
    muzikchk = tk.Checkbutton(pencere,width=10, text="Müz/Gör=",
                              variable=muzvar,anchor="w")
    muzikchk.grid(row=10,column=0)
    muziknotgir = tk.Entry(pencere,width="8")
    muziknotgir.grid(row=10,column=1)
    muzsv.set(2)
    muzspin=tk.Spinbox(pencere,from_=1,to=10,width=2,textvariable=muzsv)
    muzspin.grid(row=10,column=2,sticky="w")
    muzikchk.select()
##================================================================    
    almchk = tk.Checkbutton(pencere,width=10, text="Almanca=",
                            variable=almvar,anchor="w")
    almchk.grid(row=11,column=0)
    almnotgir = tk.Entry(pencere,width="8")
    almnotgir.grid(row=11,column=1)
    almsv.set(2)
    almspin=tk.Spinbox(pencere,from_=1,to=10,width=2,textvariable=almsv)
    almspin.grid(row=11,column=2,sticky="w")
    almchk.select()
 ##================================================================    
    pskchk = tk.Checkbutton(pencere,text="Psikoloji=",
                            variable=pskvar,width="10",anchor="w")
    pskchk.grid(row=12,column=0)
    psknotgir = tk.Entry(pencere,width="8")
    psknotgir.grid(row=12,column=1)
    psksv.set(2)
    pskspin=tk.Spinbox(pencere,from_=1,to=10,width=2,textvariable=psksv)
    pskspin.grid(row=12,column=2,sticky="w")
    pskchk.select()
 ##================================================================
    temizle = tk.Button(pencere,text="Temizle",command=temizleyici)
    temizle.place(relx=0.47,rely=0.90)
########################################################################    
    giris = tk.Button(pencere,text="Hesapla",command=girisyapma)
    giris.place(relx=0.37,rely=0.90)
    girisdurumu = tk.Label(pencere,width=15,text="")
    girisdurumu.grid(row=0,column=5)
##----------------------------------------------------------------------
boslabel = tk.Label(pencere,width=10)
boslabel.grid(row=0,rowspan=3,column=3)

dersgos=tk.Label(pencere,width=4,height=2,font=("Courier", 15),text="")
dersgos.place(relx=0.92,rely=0.3)
   
bilgi = tk.Button(pencere,text="Bilgi",command=bilgif)
bilgi.place(relx=0.92,rely=0.9)
##----------------------------------------------------------------------

tesk = tk.Label(pencere,width=22,anchor="w",text="Teşekkür için gereken puan=")
tesk.grid(row=1,column=4)
tesgos=tk.Label(pencere,width=15,text="")
tesgos.grid(row=1,column=5)
##----------------------------------------------------------------------
takd = tk.Label(pencere,width=22,anchor="w",text="Takdir için gereken puan=")
takd.grid(row=2,column=4)
takgos=tk.Label(pencere,width=15,text="")
takgos.grid(row=2,column=5)
##----------------------------------------------------------------------
belge = tk.Label(pencere,width=22,anchor="w",text="Belge=")
belge.grid(row=3,column=4)
belgedurum=tk.Label(pencere,font=("Comic Sans MS",11,"bold"),width=15,text="")
belgedurum.grid(row=3,column=5)
##----------------------------------------------------------------------
sonuc = tk.Label(pencere,width=22,anchor="w",text="Ortalama=")
sonuc.grid(row=0,column=4)
##----------------------------------------------------------------------
mf = tk.Button(pencere,text="MF",bg="green",command=alanmf)
mf.place(relx=0.68,rely=0.90)
##----------------------------------------------------------------------
tm = tk.Button(pencere,text="TM",command=alantm)
tm.place(relx=0.74,rely=0.90)
##----------------------------------------------------------------------
dikkat = tk.Label(pencere,text="Uyarı: 0(sıfır) notu kabul edilmez.\n"
                  "Girildiğinde hatalı sonuç verebilir.",anchor="nw")
dikkat.grid(row=4,rowspan=5,column=3,columnspan=6,sticky="n")
##----------------------------------------------------------------------
command=alanmf()

pencere.mainloop()
