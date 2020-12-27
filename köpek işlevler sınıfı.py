class hayvan():
    def __init__(self,dakikada_aldığı_yol,açlık_seviyesi=5,susuzluk_seviyesi=5):
        self.açlık_seviyesi=açlık_seviyesi
        self.susuzluk_seviyesi=susuzluk_seviyesi
        self.dakikada_aldığı_yol=dakikada_aldığı_yol


class köpek(hayvan):
    def __init__(self, dakikada_aldığı_yol, yaşadığı_yer=["sokak"], açlık_seviyesi=5, susuzluk_seviyesi=5,
                 sahiplik_durumu=["sahipsiz"], köpek=["hayatta"]):
        super().__init__(dakikada_aldığı_yol, açlık_seviyesi=5, susuzluk_seviyesi=5)
        self.yaşadığı_yer = yaşadığı_yer
        self.sahiplik_durumu = sahiplik_durumu
        self.köpek = köpek
        print("2 bu")

    def bilgiler(self):
        if self.köpek == ["hayatta"]:
            print("""
                *****************************
                *dakikada aldığı yol : {}     
                *yaşadığı yer : {}            
                *açlık : {}                   
                *susuzluk : {}
                *sahiplik durumu : {}
                *köpek : {}
                *****************************
            """).format(self.dakikada_aldığı_yol, self.yaşadığı_yer, self.açlık_seviyesi, self.susuzluk_seviyesi,
                        self.sahiplik_durumu, self.köpek)
        else:
            print("köpek : {}".format(self.köpek))

    def yemek_ver(self):

        while True:
            if self.açlık_seviyesi > 7.5:
                print("köpek öldü")
                self.köpek = "ölü"
                break
            cevap = input("yemek vermek için " > "beslememek için " < "basın")
            if cevap == "<":

                komut = input("1")
                if komut == "<":
                    self.dakikada_aldığı_yol += 1
                    cevap = input("2")
                    if self.açlık_seviyesi > 7.5:
                        print("köpek öldü")
                        self.köpek = "ölü"
                        break
                    if cevap == "<":
                        self.dakikada_aldığı_yol += 1
                        self.açlık_seviyesi += 5
                        if self.açlık_seviyesi > 7.5:
                            print("köpek öldü")
                            self.köpek = "ölü"
                            break



            elif cevap == ">":
                self.açlık_seviyesi -= 2.5
                self.dakikada_aldığı_yol += 1
                if self.açlık_seviyesi == 0:
                    while True:
                        karar = input("artık yemek veremezsiniz" < "bu değeri girebilirsiniz sadece")
                        if karar == "<":
                            self.açlık_seviyesi += 2.5
                            self.dakikada_aldığı_yol -= 1
                            if self.açlık_seviyesi > 7.5:
                                print("köpek öldü")
                                self.köpek = "ölü"
                                break
                        elif karar == ">":
                            print("bu aktiviteyi gerçekleştiremezsiniz")
                        elif karar == "q":
                            print("program bitiyor")
                            break
                        else:
                            print("geçerli değerler arasında bir değer giriniz ")
            elif cevap == "q":
                print("program bitiyor")
                break

            else:
                print("yanlış değer girdiniz")

    def su_ver(self):

        while True:
            if self.susuzluk_seviyesi > 7.5:
                print("köpek öldü")
                self.köpek = "ölü"
                break
            cevap = input("su vermek için " > "beslememek için " < "basın")
            if cevap == "<":
                if self.susuzluk_seviyesi > 10:
                    print("köpek öldü")
                    self.köpek = "ölü"
                else:

                    komut = input("1")
                    if komut == "<":
                        self.dakikada_aldığı_yol += 1
                        cevap = input("2")
                        if self.susuzluk_seviyesi > 7.5:
                            print("köpek öldü")
                            self.köpek = "ölü"
                            break
                        if cevap == "<":
                            self.dakikada_aldığı_yol += 1
                            self.susuzluk_seviyesi += 5
                            if self.susuzluk_seviyesi > 7.5:
                                print("köpek öldü")
                                self.köpek = "ölü"
                                break


            elif cevap == ">":
                self.susuzluk_seviyesi -= 2.5
                self.dakikada_aldığı_yol += 1
                if self.susuzluk_seviyesi == 0:
                    while True:
                        karar = input("artık su veremezsiniz" < "bu değeri girebilirsiniz sadece")
                        if karar == "<":
                            self.susuzluk_seviyesi += 2.5
                            self.dakikada_aldığı_yol -= 1
                        elif karar == ">":
                            print("bu aktiviteyi gerçekleştiremezsiniz")
                        elif karar == "q":
                            print("program bitiyor")
                            break
                        else:
                            print("geçerli değerler arasında bir değer giriniz ")
            elif cevap == "q":
                print("program bitiyor")
                break

            else:
                print("yanlış değer girdiniz")

    def yerini_değiştir(self):
        yaşadığı_yer = input("belirli bir yer giriniz")
        self.yaşadığı_yer.remove(self.yaşadığı_yer[0])
        self.yaşadığı_yer.append(yaşadığı_yer)
        if yaşadığı_yer == "ev":
            print("köpek sahiplenildi")
            self.sahiplik_durumu.remove(self.sahiplik_durumu[0])
            self.sahiplik_durumu.append("sahiplenildi")

"""
ÖRNEK İŞELVLER: 
1-köpek=köpek(10)
2-köpek.yemek_ver()
3-köpek.bilgiler()
"""