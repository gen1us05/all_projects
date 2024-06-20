from colorama import Fore, Back, Style



def valyuta_uz():

    karta_balans = 1000000
    uzs_1000 = 500
    uzs_2000 = 300
    uzs_5000 = 200
    uzs_10000 = 100
    uzs_20000 = 50
    uzs_50000 = 30
    uzs_100000 = 20
    uzs_200000 = 20
    umumiy_summa = uzs_200000 * 200000 + uzs_100000 * 100000 + uzs_50000 * 50000 + uzs_20000 * 20000 + uzs_10000 * 10000 + uzs_5000 * 5000 + uzs_2000 * 2000 + uzs_1000 * 1000
    uzs_miqdori = int(input(F"""                            {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}
                            {Fore.YELLOW + Back.BLACK} |MIQDORNI KIRITING| {Style.RESET_ALL}
                            {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}

               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |   1.500 000    | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   2.300 000    | {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
               
               
               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL} 
               {Fore.YELLOW + Back.BLACK} |   3.100 000    | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |     4.50 000   | {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
               
               
               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL} 
               {Fore.YELLOW + Back.BLACK} |    5.20 000    | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 6.BOSHQA SUMMA | {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
    {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}"""))
    if uzs_miqdori == 1 and karta_balans >=uzs_miqdori:
        foiz=500000/100
        yechish=500000+foiz
        b=karta_balans-yechish
        print(f"""
        _______________________________________
        |                                     
        |   SUMMA : {500000} GA TENG.    
        |   FOIZ : {foiz}               
        |   JAMI : {yechish}            
        |                               
        ---------------------------------------
        """)
        tasdiqlash = int(input(F"""
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
     
     
     {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))
        if tasdiqlash == 1 and tasdiqlash <=umumiy_summa and tasdiqlash <= uzs_200000*200000 and tasdiqlash <= uzs_100000*100000:
            yakun_yoki_menyu = (int(input(f"""
            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} 2 DONA 200 MINGLIK                                                               {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK} 1 DONA 100 MINGLIK                                                               {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
            uzs_200000 -=1
            uzs_100000 -=1

            print(f"""
            _______________________________________
            |            CHEK:                   
            |   SUMMA : {500000} GA TENG.    
            |   FOIZ : {foiz}                  
            |   JAMI : {yechish}               
            |   KARTA: 9860********6796        
            |   KARTADA QOLGAN SUMMA: {b}      
            ---------------------------------------
            """)


            if yakun_yoki_menyu == 1:
                menyu_uz()
            else:
                print("""
                ______________________________________________________________________________
                """)
                boshlash()
        elif tasdiqlash == 2:
            valyuta_uz()
        else:
            menyu_uz()
    elif uzs_miqdori== 2 and karta_balans >=uzs_miqdori :

        foiz=300000/100
        yechish=300000+foiz
        b=karta_balans-yechish
        print(f"""
        _______________________________________
        |                                     
        |   SUMMA : {300000} GA TENG.    
        |   FOIZ : {foiz}                     
        |   JAMI : {yechish}                  
        |                                     
        ---------------------------------------
        """)
        tasdiqlash = int(input(f"""
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))
        if tasdiqlash == 1 and tasdiqlash <=umumiy_summa and 200000 <= uzs_200000*200000 and 50000<= uzs_50000*50000 and 10*5000<=uzs_5000*5000:
            yakun_yoki_menyu = (int(input(f"""
                    {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                    {Fore.YELLOW + Back.BLACK} 1 DONA 200 MINGLIK                                                               {Style.RESET_ALL} 
                    {Fore.YELLOW + Back.BLACK} 1 DONA 50 MINGLIK                                                               {Style.RESET_ALL} 
                    {Fore.YELLOW + Back.BLACK} 10 DONA 5 MING                                                                   {Style.RESET_ALL} 
                    {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                    {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                    {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                    {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                    {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                    {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
            uzs_200000 -=1
            uzs_50000 -=1
            uzs_5000 -=10


            print(f"""
            _______________________________________
            |            CHEK:                    
            |   SUMMA : {300000} GA TENG.    
            |   FOIZ : {foiz}                    
            |   JAMI : {yechish}                 
            |   KARTA: 9860********6796           
            |   KARTADA QOLGAN SUMMA: {b}         
            ---------------------------------------
            """)
            if yakun_yoki_menyu == 1:
                menyu_uz()
            else:
                print("""
                _______________________________________________________________________________________
                        """)
                boshlash()
        elif tasdiqlash == 2:
            valyuta_uz()
        else:
            menyu_uz()
    elif uzs_miqdori == 3 and karta_balans >=uzs_miqdori:


        foiz=100000/100
        yechish=100000+foiz
        b=karta_balans-yechish
        print(f"""
        _______________________________________
        |                               
        |   SUMMA : {100000} GA TENG.   
        |   FOIZ : {foiz}                     
        |   JAMI : {yechish}                  
        |                                     
        ---------------------------------------
        """)

        tasdiqlash = int(input(f"""
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))
        if tasdiqlash == 1 and 50000 <=uzs_50000*50000 and 10000 <= uzs_10000 *10000 and 8*5000 <= uzs_5000*5000:
            yakun_yoki_menyu = (int(input(f"""
                    {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                    {Fore.YELLOW + Back.BLACK} 1 DONA 50 MINGLIK                                                                {Style.RESET_ALL} 
                    {Fore.YELLOW + Back.BLACK} 1 DONA 10 MINGLIK                                                                {Style.RESET_ALL} 
                    {Fore.YELLOW + Back.BLACK} 8 DONA 5 MING                                                                    {Style.RESET_ALL} 
                    {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                    {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                    {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                    {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                    {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                    {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
            uzs_50000-=1
            uzs_10000 -=1
            uzs_5000 -=8



            print(f"""
            _______________________________________
            |            CHEK:                    
            |   SUMMA : {100000} GA TENG.    
            |   FOIZ : {foiz}                
            |   JAMI : {yechish}             
            |   KARTA: 9860********6796      
            |   KARTADA QOLGAN SUMMA: {b}    
            ---------------------------------------
            """)
            if yakun_yoki_menyu == 1:
                menyu_uz()
            else:
                print("""
                _______________________________________________________________________________________
                        """)
                boshlash()
        elif tasdiqlash == 2:
            valyuta_uz()
        else:
            menyu_uz()
    elif uzs_miqdori == 4 and karta_balans >=uzs_miqdori:
        foiz=50000/100
        yechish=50000+foiz
        b=karta_balans-yechish
        print(f"""
        _______________________________________
        |                                    
        |   SUMMA : {50000} GA TENG.    
        |   FOIZ : {foiz}               
        |   JAMI : {yechish}            
        |                               
        ---------------------------------------
        """)

        tasdiqlash = int(input(f"""
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))
        if tasdiqlash == 1 and 50000 <= uzs_50000*50000:
            yakun_yoki_menyu = (int(input(f"""
                    {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                    {Fore.YELLOW + Back.BLACK} 1 DONA 50 MINGLIK                                                                {Style.RESET_ALL} 
                    {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                    {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                    {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                    {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                    {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                    {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                    {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                    {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
            uzs_50000 -=1

            print(f"""
            _______________________________________
            |            CHEK:     
            |   SUMMA : {50000} GA TENG. 
            |   FOIZ : {foiz}            
            |   JAMI : {yechish}         
            |   KARTA: 9860********6796   
            |   KARTADA QOLGAN SUMMA: {b} 
            ---------------------------------------
            """)
            if yakun_yoki_menyu == 1:
                menyu_uz()
            else:
                print("""
                _______________________________________________________________________________________
                        """)
                boshlash()
        elif tasdiqlash == 2:
            valyuta_uz()
        else:
            menyu_uz()
    elif uzs_miqdori == 5 and karta_balans >=uzs_miqdori :

        foiz=20000/100
        yechish=20000+foiz
        b=karta_balans-yechish
        print(f"""
        _______________________________________
        |                         
        |   SUMMA : {20000} GA TENG.   
        |   FOIZ : {foiz}         
        |   JAMI : {yechish}      
        |                         
        ---------------------------------------
        """)
        tasdiqlash = int(input(f"""
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))
        if tasdiqlash == 1:
            yakun_yoki_menyu = (int(input(f"""
                    {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                    {Fore.YELLOW + Back.BLACK} 1 DONA 20 MINGLIK                                                                {Style.RESET_ALL} 
                    {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                    {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                    {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                    {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                    {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                    {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                    {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                    {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
            uzs_20000 -=1
            print(f"""
            _______________________________________
            |            CHEK:                    
            |   SUMMA : {20000} GA TENG.    
            |   FOIZ : {foiz}                   
            |   JAMI : {yechish}                
            |   KARTA: 9860********6796         
            |   KARTADA QOLGAN SUMMA: {b}       
            ---------------------------------------
            """)
            if yakun_yoki_menyu == 1:
                menyu_uz()
            else:
                print("""
                _______________________________________________________________________________________
                        """)
                boshlash()
        elif tasdiqlash == 2:
            valyuta_uz()
        else:
            menyu_uz()
    else:
        boshqa_summa = int(input(f"""
        {Fore.YELLOW + Back.BLACK} Minimal summa 1 ming UZS( pul miqdroni kiritiganda oxtiri 3 ta 0 bilan tugashi kerak aks xolada datur ishlamaydi.) {Style.RESET_ALL}
        {Fore.YELLOW + Back.BLACK} PUL MIQDORINI KIRITING => {Style.RESET_ALL}"""))
        if 2000<=boshqa_summa<=karta_balans and boshqa_summa%1000 == 0:
            if boshqa_summa <=1000000:

                foiz = boshqa_summa / 100
                yechish = boshqa_summa + foiz
                b = karta_balans - yechish
                print(f"""
                _______________________________________
                |                                     |
                |   SUMMA : {boshqa_summa} GA TENG.    |
                |   FOIZ : {foiz}                     |
                |   JAMI : {yechish}                  |
                |                                     |
                ---------------------------------------
                """)
                ikkiyuzliklar=boshqa_summa//200000
                yuzmingliklar=(boshqa_summa-ikkiyuzliklar*200000)//100000
                ellikmingliklar=(boshqa_summa-yuzmingliklar*100000 - ikkiyuzliklar * 200000)//50000
                yigirmamingliklar=(boshqa_summa-yuzmingliklar*100000 - ikkiyuzliklar * 200000-ellikmingliklar*50000)//20000
                onminglik=(boshqa_summa-yuzmingliklar*100000 - ikkiyuzliklar * 200000-ellikmingliklar*50000-yigirmamingliklar*20000)//10000
                beshminglik=(boshqa_summa-yuzmingliklar*100000 - ikkiyuzliklar * 200000-ellikmingliklar*50000-yigirmamingliklar*20000-onminglik*10000)//5000
                ikkiminglik=(boshqa_summa-yuzmingliklar*100000 - ikkiyuzliklar * 200000-ellikmingliklar*50000-yigirmamingliklar*20000-onminglik*10000-beshminglik*5000)//2000
                minglik=(boshqa_summa-yuzmingliklar*100000 - ikkiyuzliklar * 200000-ellikmingliklar*50000-yigirmamingliklar*20000-onminglik*10000-beshminglik*5000-ikkiminglik*2000)//1000
                if ikkiyuzliklar >0:

                    if yuzmingliklar>0:

                        if ellikmingliklar>0:

                            if yigirmamingliklar>0:

                                if onminglik>0:

                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK   {beshminglik} DONA 5 MINGLIK                       {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                    else:


                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK   {beshminglik} DONA 5 MINGLIK                       {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                else:
                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}  {minglik}  DONA MINGLIK                                                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {minglik}  DONA MINGLIK                          {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK                                                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()

                                    else:


                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK     {minglik}  DONA MINGLIK                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK     {minglik}  DONA MINGLIK                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                            else:


                                if onminglik>0:

                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK   {beshminglik} DONA 5 MINGLIK                       {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK   {beshminglik} DONA 5 MINGLIK                       {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK   {beshminglik} DONA 5 MINGLIK                       {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK   {beshminglik} DONA 5 MINGLIK                       {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                    else:


                                        if ikkiminglik>0:

                                            if minglik >0:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {onminglik} DONA 10 MINGLIK                   {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {onminglik} DONA 10 MINGLIK                   {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:


                                            if minglik >0:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {onminglik} DONA 10 MINGLIK                   {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {onminglik} DONA 10 MINGLIK                   {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                else:
                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}  {minglik}  DONA MINGLIK                                                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}  {minglik}  DONA MINGLIK                                                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                    else:


                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK        {ikkiminglik} DONA 2 MINGLIK            {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {minglik}  DONA MINGLIK                                                          {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK        {ikkiminglik} DONA 2 MINGLIK            {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {minglik}  DONA MINGLIK                       {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK                                                {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                        else:


                            if yigirmamingliklar>0:

                                if onminglik>0:

                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {yigirmamingliklar} DOAN 20 MINGLIK   {onminglik} DONA 10 MINGLIK                {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK       {ikkiminglik} DONA 2 MINGLIK                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {minglik}  DONA MINGLIK                                                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {yigirmamingliklar} DOAN 20 MINGLIK   {onminglik} DONA 10 MINGLIK                {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK       {ikkiminglik} DONA 2 MINGLIK                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                    else:


                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {yigirmamingliklar} DOAN 20 MINGLIK    {onminglik} DONA 10 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {minglik}  DONA MINGLIK                                                          {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {yigirmamingliklar} DOAN 20 MINGLIK      {onminglik} DONA 10 MINGLIK             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                        1                                                          {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK      {yuzmingliklar} DONA 100 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {yigirmamingliklar} DOAN 20 MINGLIK     {onminglik} DONA 10 MINGLIK              {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                else:
                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}  {minglik}  DONA MINGLIK                                                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {yigirmamingliklar} DOAN 20 MINGLIK      {beshminglik} DONA 5 MINGLIK            {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK                                                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {yigirmamingliklar} DOAN 20 MINGLIK   {beshminglik} DONA 5 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}  {minglik}  DONA MINGLIK                                                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {yigirmamingliklar} DOAN 20 MINGLIK   {beshminglik} DONA 5 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                    else:


                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {yigirmamingliklar} DOAN 20 MINGLIK     {ikkiminglik} DONA 2 MINGLIK             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {minglik}  DONA MINGLIK                                                          {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {yigirmamingliklar} DOAN 20 MINGLIK    {ikkiminglik} DONA 2 MINGLIK              {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {yigirmamingliklar} DOAN 20 MINGLIK   {minglik}  DONA MINGLIK                    {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {yigirmamingliklar} DOAN 20 MINGLIK                                              {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                            else:


                                if onminglik>0:

                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK   {beshminglik} DONA 5 MINGLIK                       {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()

                                            tasdiqlash = int(input(f"""
                                                    {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                    {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                    {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                    {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                            if tasdiqlash == 1:
                                                yakun_yoki_menyu = (int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                        {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                        {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK   {beshminglik} DONA 5 MINGLIK                       {Style.RESET_ALL} 
                                                        {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                        {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                        {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                        {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                        {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                        {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                uzs_20000 -= 1
                                                if yakun_yoki_menyu == 1:
                                                    menyu_uz()
                                                else:
                                                    print("""
                                                    _______________________________________________________________________________________
                                                            """)
                                                    boshlash()
                                            elif tasdiqlash == 2:
                                                valyuta_uz()
                                            else:
                                                menyu_uz()
                                    else:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK     {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {minglik}  DONA MINGLIK                                                          {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}{onminglik} DONA 10 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                      {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:

                                            if minglik > 0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK  {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK                                                      {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                else:
                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}  {minglik}  DONA MINGLIK                                                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}{beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                      {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                    else:
                                        if ikkiminglik>0:
                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK   {minglik} DONA MINGLIK                            {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK                                                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {minglik}  DONA MINGLIK                                                          {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                    else:


                        if ellikmingliklar>0:

                            if yigirmamingliklar>0:

                                if onminglik>0:

                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK   {beshminglik} DONA 5 MINGLIK                       {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK   {beshminglik} DONA 5 MINGLIK                       {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                else:
                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {ellikmingliklar} DONA 50 MINGLIK              {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {yigirmamingliklar} DOAN 20 MINGLIK  {beshminglik} DONA 5 MINGLIK                {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK      {minglik}  DONA MINGLIK                        {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK     {ellikmingliklar} DONA 50 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {yigirmamingliklar} DOAN 20 MINGLIK   {ellikmingliklar} DONA 50 MINGLIK          {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK                                                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                    else:


                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK     {minglik}  DONA MINGLIK                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK     {minglik}  DONA MINGLIK                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                            else:


                                if onminglik>0:

                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK   {beshminglik} DONA 5 MINGLIK                       {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                else:
                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}  {minglik}  DONA MINGLIK                                                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}  {minglik}  DONA MINGLIK                                                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                    else:


                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK     {minglik}  DONA MINGLIK                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK     {minglik}  DONA MINGLIK                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                        else:


                            if yigirmamingliklar>0:

                                if onminglik>0:

                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK      {yigirmamingliklar} DOAN 20 MINGLIK        {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK         {beshminglik} DONA 5 MINGLIK                 {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK     {minglik}  DONA MINGLIK                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK            {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK    {beshminglik} DONA 5 MINGLIK                      {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK                                                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                    else:


                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}   {yigirmamingliklar} DOAN 20 MINGLIK    {onminglik} DONA 10 MINGLIK             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {yigirmamingliklar} DOAN 20 MINGLIK      {onminglik} DONA 10 MINGLIK             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {minglik}  DONA MINGLIK                                                          {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK      {yuzmingliklar} DONA 100 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {yigirmamingliklar} DOAN 20 MINGLIK     {onminglik} DONA 10 MINGLIK              {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                else:
                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK            {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK      {ikkiminglik} DONA 2 MINGLIK                   {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {minglik}  DONA MINGLIK                                                          {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK            {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                    else:




                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK     {minglik}  DONA MINGLIK                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK     {minglik}  DONA MINGLIK                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                            else:


                                if onminglik>0:

                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK   {beshminglik} DONA 5 MINGLIK                       {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()

                                            tasdiqlash = int(input(f"""
                                                    {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                    {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                    {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                    {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                            if tasdiqlash == 1:
                                                yakun_yoki_menyu = (int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                        {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                        {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK   {beshminglik} DONA 5 MINGLIK                       {Style.RESET_ALL} 
                                                        {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                        {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                        {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                        {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                        {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                        {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                uzs_20000 -= 1
                                                if yakun_yoki_menyu == 1:
                                                    menyu_uz()
                                                else:
                                                    print("""
                                                    _______________________________________________________________________________________
                                                            """)
                                                    boshlash()
                                            elif tasdiqlash == 2:
                                                valyuta_uz()
                                            else:
                                                menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK       {onminglik} DONA 10 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK           {minglik}  DONA MINGLIK                   {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {onminglik} DONA 10 MINGLIK                    {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK                                                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                else:
                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {beshminglik} DONA 5 MINGLIK                   {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK       {minglik}  DONA MINGLIK                       {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {beshminglik} DONA 5 MINGLIK                   {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK                                                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                    else:


                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK                                          `           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {minglik}  DONA MINGLIK                                                          {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK                                                 {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                else:


                    if yuzmingliklar>0:

                        if ellikmingliklar>0:

                            if yigirmamingliklar>0:

                                if onminglik>0:

                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK   {beshminglik} DONA 5 MINGLIK                       {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                else:
                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}  {minglik}  DONA MINGLIK                                                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                    else:


                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK     {minglik}  DONA MINGLIK                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK     {minglik}  DONA MINGLIK                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                            else:


                                if onminglik>0:

                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK   {beshminglik} DONA 5 MINGLIK                       {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                else:
                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}  {minglik}  DONA MINGLIK                                                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}  {minglik}  DONA MINGLIK                                                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                    else:


                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK     {minglik}  DONA MINGLIK                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK     {minglik}  DONA MINGLIK                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                        else:


                            if yigirmamingliklar>0:

                                if onminglik>0:

                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {yigirmamingliklar} DOAN 20 MINGLIK   {onminglik} DONA 10 MINGLIK                {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK       {ikkiminglik} DONA 2 MINGLIK                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {minglik}  DONA MINGLIK                                                          {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                    else:


                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}   {yigirmamingliklar} DOAN 20 MINGLIK    {onminglik} DONA 10 MINGLIK             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {yigirmamingliklar} DOAN 20 MINGLIK      {onminglik} DONA 10 MINGLIK             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {minglik}  DONA MINGLIK                                                          {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK      {yuzmingliklar} DONA 100 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {yigirmamingliklar} DOAN 20 MINGLIK     {onminglik} DONA 10 MINGLIK              {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                else:
                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}  {minglik}  DONA MINGLIK                                                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                    else:




                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK     {minglik}  DONA MINGLIK                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK     {minglik}  DONA MINGLIK                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                            else:


                                if onminglik>0:

                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK   {beshminglik} DONA 5 MINGLIK                       {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()

                                            tasdiqlash = int(input(f"""
                                                    {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                    {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                    {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                    {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                            if tasdiqlash == 1:
                                                yakun_yoki_menyu = (int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                        {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                        {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK   {beshminglik} DONA 5 MINGLIK                       {Style.RESET_ALL} 
                                                        {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                        {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                        {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                        {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                        {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                        {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                uzs_20000 -= 1
                                                if yakun_yoki_menyu == 1:
                                                    menyu_uz()
                                                else:
                                                    print("""
                                                    _______________________________________________________________________________________
                                                            """)
                                                    boshlash()
                                            elif tasdiqlash == 2:
                                                valyuta_uz()
                                            else:
                                                menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK   {beshminglik} DONA 5 MINGLIK                       {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()

                                            tasdiqlash = int(input(f"""
                                                    {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                    {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                    {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                    {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                            if tasdiqlash == 1:
                                                yakun_yoki_menyu = (int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                        {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                        {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK   {beshminglik} DONA 5 MINGLIK                       {Style.RESET_ALL} 
                                                        {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                        {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                        {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                        {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                        {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                        {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                uzs_20000 -= 1
                                                if yakun_yoki_menyu == 1:
                                                    menyu_uz()
                                                else:
                                                    print("""
                                                    _______________________________________________________________________________________
                                                            """)
                                                    boshlash()
                                            elif tasdiqlash == 2:
                                                valyuta_uz()
                                            else:
                                                menyu_uz()
                                else:
                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}  {minglik}  DONA MINGLIK                                                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}{beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                      {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                    else:


                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK                                          `           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {minglik}  DONA MINGLIK                                                          {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                    else:


                        if ellikmingliklar>0:

                            if yigirmamingliklar>0:

                                if onminglik>0:

                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK   {beshminglik} DONA 5 MINGLIK                       {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                else:
                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}  {minglik}  DONA MINGLIK                                                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                    else:


                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK     {minglik}  DONA MINGLIK                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK     {minglik}  DONA MINGLIK                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                            else:


                                if onminglik>0:

                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK   {beshminglik} DONA 5 MINGLIK                       {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                else:
                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}  {minglik}  DONA MINGLIK                                                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}  {minglik}  DONA MINGLIK                                                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                    else:


                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK     {minglik}  DONA MINGLIK                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK     {minglik}  DONA MINGLIK                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                        else:


                            if yigirmamingliklar>0:

                                if onminglik>0:

                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {yigirmamingliklar} DOAN 20 MINGLIK   {onminglik} DONA 10 MINGLIK                {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK       {ikkiminglik} DONA 2 MINGLIK                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {minglik}  DONA MINGLIK                                                          {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                    else:


                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}   {yigirmamingliklar} DOAN 20 MINGLIK    {onminglik} DONA 10 MINGLIK             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {yigirmamingliklar} DOAN 20 MINGLIK      {onminglik} DONA 10 MINGLIK             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {minglik}  DONA MINGLIK                                                          {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK      {yuzmingliklar} DONA 100 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {yigirmamingliklar} DOAN 20 MINGLIK     {onminglik} DONA 10 MINGLIK              {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                else:
                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}  {minglik}  DONA MINGLIK                                                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                    else:




                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK     {minglik}  DONA MINGLIK                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK     {minglik}  DONA MINGLIK                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                            else:


                                if onminglik>0:

                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK   {beshminglik} DONA 5 MINGLIK                       {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()

                                            tasdiqlash = int(input(f"""
                                                    {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                    {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                    {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                    {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                            if tasdiqlash == 1:
                                                yakun_yoki_menyu = (int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                        {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                        {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK   {beshminglik} DONA 5 MINGLIK                       {Style.RESET_ALL} 
                                                        {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                        {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                        {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                        {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                        {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                        {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                uzs_20000 -= 1
                                                if yakun_yoki_menyu == 1:
                                                    menyu_uz()
                                                else:
                                                    print("""
                                                    _______________________________________________________________________________________
                                                            """)
                                                    boshlash()
                                            elif tasdiqlash == 2:
                                                valyuta_uz()
                                            else:
                                                menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK   {beshminglik} DONA 5 MINGLIK                       {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {minglik}  DONA MINGLIK                                                          {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()

                                            tasdiqlash = int(input(f"""
                                                    {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                    {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                    {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                    {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                            if tasdiqlash == 1:
                                                yakun_yoki_menyu = (int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK   {beshminglik} DONA 5 MINGLIK                       {Style.RESET_ALL} 
                                                        {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                        {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                        {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                        {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                        {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                        {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                uzs_20000 -= 1
                                                if yakun_yoki_menyu == 1:
                                                    menyu_uz()
                                                else:
                                                    print("""
                                                    _______________________________________________________________________________________
                                                            """)
                                                    boshlash()
                                            elif tasdiqlash == 2:
                                                valyuta_uz()
                                            else:
                                                menyu_uz()
                                    else:

                                        if ikkiminglik > 0:

                                            if minglik > 0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK                                                      {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()

                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK      {ikkiminglik} DONA 2 MINGLIK                    {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:

                                            if minglik > 0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK   {beshminglik} DONA 5 MINGLIK                       {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {minglik}  DONA MINGLIK                                                          {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()

                                            tasdiqlash = int(input(f"""
                                                    {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                    {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                    {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                    {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                            if tasdiqlash == 1:
                                                yakun_yoki_menyu = (int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} {onminglik} DONA 10 MINGLIK   {beshminglik} DONA 5 MINGLIK                       {Style.RESET_ALL} 
                                                        {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK {minglik}  DONA MINGLIK                             {Style.RESET_ALL} 
                                                        {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                        {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                        {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                        {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                        {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                uzs_20000 -= 1
                                                if yakun_yoki_menyu == 1:
                                                    menyu_uz()
                                                else:
                                                    print("""
                                                    _______________________________________________________________________________________
                                                            """)
                                                    boshlash()
                                            elif tasdiqlash == 2:
                                                valyuta_uz()
                                            else:
                                                menyu_uz()
                                else:
                                    if beshminglik>0:

                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}  {minglik}  DONA MINGLIK                                                         {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}{beshminglik} DONA 5 MINGLIK    {ikkiminglik} DONA 2 MINGLIK                      {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                    else:


                                        if ikkiminglik>0:

                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK                                          `           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiminglik} DONA 2 MINGLIK                                                     {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                        else:


                                            if minglik >0:
                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {minglik}  DONA MINGLIK                                                          {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()
                                            else:

                                                tasdiqlash = int(input(f"""
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
                                                        {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
                                                        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                                                        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))

                                                if tasdiqlash == 1:
                                                    yakun_yoki_menyu = (int(input(f"""
                                                            {Fore.YELLOW + Back.BLACK} CHIQARILDI:                                                                      {Style.RESET_ALL}
                                                            {Fore.YELLOW + Back.BLACK} {ikkiyuzliklar} DONA 200 MINGLIK  {yuzmingliklar} DONA 100 MINGLIK               {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} {ellikmingliklar} DONA 50 MINGLIK  {yigirmamingliklar} DOAN 20 MINGLIK           {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
                                                            {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                                                            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
                                                    uzs_20000 -= 1
                                                    if yakun_yoki_menyu == 1:
                                                        menyu_uz()
                                                    else:
                                                        print("""
                                                        _______________________________________________________________________________________
                                                                """)
                                                        boshlash()
                                                elif tasdiqlash == 2:
                                                    valyuta_uz()
                                                else:
                                                    menyu_uz()


        else:
            print("""
            
            Kartada mablag' yetarli emas.
            
            """)
            valyuta_uz()
def pinkod():
    n=1
    while n>0:
        yangikod = int(input(f"{Fore.YELLOW + Back.BLACK} YANGI PINCODNI KIRITING =>  {Style.RESET_ALL}"))
        if 1000<=yangikod<=9999:
            tasdiqlash = int(input(f"""
                                  {Fore.YELLOW + Back.BLACK} |-------------------------| {Style.RESET_ALL}
                                  {Fore.YELLOW + Back.BLACK} |PINKOD O'ZGARTIRILSINMI? | {Style.RESET_ALL}
                                  {Fore.YELLOW + Back.BLACK} |-------------------------| {Style.RESET_ALL}
                                                            
            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
            {Fore.YELLOW + Back.BLACK} |      1.HA      | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}"""))
            if tasdiqlash == 1:
                print("Pinkod muvoffaqiyatli o'zgartirildi.")
                n = -1
                menyu_uz()
            elif tasdiqlash == 2:
                pinkod()
            else:
                menyu_uz()
        else:
            print("Pinkod 4 xonali bo'lishi kerak.")


def kartabalans():
    print(f"""
    | KARTANGIZDA {1000000} SUM PUL BOR
    """)
    menyu_uz()
def smsxabarnoma():
    n = 1
    while n > 0:
        numbers = int(input(f"{Fore.YELLOW + Back.BLACK}  YANGI RAQAMNI KIRIING   => +998 : {Style.RESET_ALL}"))
        if 100000000 <= numbers <= 999999999:
            tasdiqlash = int(input(f"""
                                  {Fore.YELLOW + Back.BLACK} |-------------------------| {Style.RESET_ALL}
                                  {Fore.YELLOW + Back.BLACK} | RAQAM O'ZGARTIRILSINMI? | {Style.RESET_ALL}
                                  {Fore.YELLOW + Back.BLACK} |-------------------------| {Style.RESET_ALL}

            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
            {Fore.YELLOW + Back.BLACK} |     1.HA       | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA  KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}"""))
            if tasdiqlash == 1:
                print("MUVOFFAQIYATLI O'ZGARTIRILDI.")
                n = -1
                menyu_uz()
            elif tasdiqlash == 2:
                smsxabarnoma()
            else:
                menyu_uz()
        else:
            print("TELEFON RAQAM 9 XONALI BO'LISHI KERAK.")






def menyu_uz():
    menyu = int(input(f"""                            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
                            {Fore.YELLOW + Back.BLACK} |Xizmani tanlang:| {Style.RESET_ALL}
                            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}

               {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |1.PINCODNI O'ZGARTIRITSH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   2.NAQD PUL OLISH     | {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}
               
               
               {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL} 
               {Fore.YELLOW + Back.BLACK} |     3.KARTA BALANS     | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |     4.SMS XABARNOMA    | {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}
                                 
                                 
                                 {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}
                                 {Fore.YELLOW + Back.BLACK} |  5.KARTANI CHIQARISH   | {Style.RESET_ALL}
                                 {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}
                {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}"""))
    if menyu == 1:
        pinkod()
    elif menyu == 2:
        valyuta_uz()
    elif menyu == 3:
        kartabalans()
    elif menyu == 4:
        smsxabarnoma()
    else:
        print("Xizmatlarimizdan foydalanganinggiz uchun raxmat.")
        print("""
        _______________________________________________________________________________
        """)
        boshlash()


def uzbekcha():
    n=2
    password=1224
    while n>=0 :
        kod=int(input(f"""
    {Fore.YELLOW + Back.BLACK}  Pinkodni kiriting =>   {Style.RESET_ALL}"""))

        if kod == password:
            n=-1
            menyu_uz()
        elif n>0:
            n -=1
        elif n == 0:
            print("""
            Siz ko'p marotaba kodni xato kiritdingiz shu sababdan kartangiz bankomatda qoladi.
            """)
            print("""
            _______________________________________________________________________________________________________
            """)
            boshlash()
def pincod_eng():
    n=1
    while n>0:
        yangikod = int(input(f"{Fore.YELLOW + Back.BLACK}  INSERT NEW PIN   =>  {Style.RESET_ALL}"))
        if 1000<=yangikod<=9999:
            tasdiqlash = int(input(f"""
                                  {Fore.YELLOW + Back.BLACK} |-------------------------| {Style.RESET_ALL}
                                  {Fore.YELLOW + Back.BLACK} |      CHANGE PINCODE?    | {Style.RESET_ALL}
                                  {Fore.YELLOW + Back.BLACK} |-------------------------| {Style.RESET_ALL}
                                                            
            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
            {Fore.YELLOW + Back.BLACK} |     1.YES      | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.RE-INTRODUCTION| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   3.CENCEL     | {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}"""))
            if tasdiqlash == 1:
                print("PINCODE CHANGED SUCCESSFULLY")
                n = -1
                menyu_eng()
            elif tasdiqlash == 2:
                pincod_eng()
            else:
                menyu_eng()
        else:
            print("PINCODE MUST BE 4 DIGITS.")
def kartabalans_eng():
    print("YOU HAVE 1 000 000 UZS FROM YOUR CARD")
    menyu_eng()
def smsxabarnoma_eng():
    n=1
    while n>0:
        numbers = int(input(f"{Fore.YELLOW + Back.BLACK}  ENTER NEW NUMBER   => +998 : {Style.RESET_ALL}"))
        if 100000000<=numbers<=999999999:
            tasdiqlash = int(input(f"""
                                  {Fore.YELLOW + Back.BLACK} |-------------------------| {Style.RESET_ALL}
                                  {Fore.YELLOW + Back.BLACK} |       CHANGE NUMBER?    | {Style.RESET_ALL}
                                  {Fore.YELLOW + Back.BLACK} |-------------------------| {Style.RESET_ALL}
                                                            
            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
            {Fore.YELLOW + Back.BLACK} |     1.YES      | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.RE-INTRODUCTION| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   3.CENCEL     | {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}"""))
            if tasdiqlash == 1:
                print("NUMBER CHANGED SUCCESSFULLY")
                n = -1
                menyu_eng()
            elif tasdiqlash == 2:
                smsxabarnoma_eng()
            else:
                menyu_eng()
        else:
            print("NUMBER MUST BE 9 DIGITS.")


def valyuta_eng():

    karta_balans = 1000000
    uzs_1000 = 500
    uzs_2000 = 300
    uzs_5000 = 200
    uzs_10000 = 100
    uzs_20000 = 50
    uzs_50000 = 30
    uzs_100000 = 20
    uzs_200000 = 20
    umumiy_summa = uzs_200000 * 200000 + uzs_100000 * 100000 + uzs_50000 * 50000 + uzs_20000 * 20000 + uzs_10000 * 10000 + uzs_5000 * 5000 + uzs_2000 * 2000 + uzs_1000 * 1000
    uzs_miqdori = int(input(F"""                            {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}
                            {Fore.YELLOW + Back.BLACK} |   ENTER AMOUNT  | {Style.RESET_ALL}
                            {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}

               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |   1.500 000    | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   2.300 000    | {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
               
               
               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL} 
               {Fore.YELLOW + Back.BLACK} |   3.100 000    | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |     4.50 000   | {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
               
               
               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL} 
               {Fore.YELLOW + Back.BLACK} |    5.20 000    | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |6.ANOTHER AMOUNT| {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
    {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}"""))
    if uzs_miqdori == 1 and karta_balans >=uzs_miqdori:
        uzs_miqdori= 500000
        foiz=uzs_miqdori/100
        yechish=uzs_miqdori+foiz
        b=karta_balans-yechish
        print(f"""
        _______________________________________
        |                                     
        |   THE SUM IS : {uzs_miqdori}        
        |   PERCENT : {foiz}                  
        |   TOTAL : {yechish}                 
        |                                     
        ---------------------------------------
        """)

        tasdiqlash = int(input(F"""
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
        {Fore.YELLOW + Back.BLACK} | 1.CONFIRMATION | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   2.RE-ENTER   | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |    3.CENCEL    | {Style.RESET_ALL}
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
     
     
     {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))
        if tasdiqlash == 1 and tasdiqlash <=umumiy_summa and tasdiqlash <= uzs_200000*200000 and tasdiqlash <= uzs_100000*100000:


            print(f"""
            _______________________________________
            |            CHEK:                    
            |   THE SUM IS  : {uzs_miqdori}  .    
            |   PERCENT : {foiz}                  
            |   TOTAL : {yechish}                 
            |   CARD: 9860********6796            
            |   AMOUNT REMAINING ON THE CARD: {b} 
            ---------------------------------------
            """)
            yakun_yoki_menyu = (int(input(f"""
            {Fore.YELLOW + Back.BLACK} RELEASED:                                                                        {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} 2 PIECES FOR 200 THOUSAND                                                        {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK} 1 PIECE 100 THOUSAND                                                             {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK} THANK YOU FOR USING OUR SERVICES                                                 {Style.RESET_ALL}  
            {Fore.YELLOW + Back.BLACK} ARE THERE OTHER SERVICES?                                                          {Style.RESET_ALL}  
            {Fore.YELLOW + Back.BLACK} 1.YES                                                                             {Style.RESET_ALL}  
            {Fore.YELLOW + Back.BLACK} 2.NO                                                                           {Style.RESET_ALL}  
            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
            uzs_200000 -=1
            uzs_100000 -=1
            if yakun_yoki_menyu == 1:
                menyu_eng()
            else:
                print("""
                ______________________________________________________________________________
                """)
                boshlash()
        elif tasdiqlash == 2:
            valyuta_eng()
        else:
            menyu_eng()
    elif uzs_miqdori== 2 and karta_balans >=uzs_miqdori :

        uzs_miqdori=300000
        foiz=uzs_miqdori/100
        yechish=uzs_miqdori+foiz
        b=karta_balans-yechish
        print(f"""
        _______________________________________
        |                                     
        |   THE SUM IS : {uzs_miqdori}        
        |   PERCENT : {foiz}                  
        |   TOTAL : {yechish}                 
        |                                     
        ---------------------------------------
        """)
        tasdiqlash = int(input(f"""
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
        {Fore.YELLOW + Back.BLACK} | 1.CONFIRMATION | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   2.RE-ENTER   | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |    3.CENCEL    | {Style.RESET_ALL}
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
     
     
     {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))
        if tasdiqlash == 1 and tasdiqlash <=umumiy_summa and 200000 <= uzs_200000*200000 and 50000<= uzs_50000*50000 and 10*5000<=uzs_5000*5000:



            print(f"""
            _______________________________________
            |            CHEK:                    
            |   THE SUM IS  : {uzs_miqdori}  .    
            |   PERCENT : {foiz}                  
            |   TOTAL : {yechish}                 
            |   CARD: 9860********6796            
            |   AMOUNT REMAINING ON THE CARD: {b} 
            ---------------------------------------
            """)
            yakun_yoki_menyu = (int(input(f"""
            {Fore.YELLOW + Back.BLACK} RELEASED:                                                                        {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} 1 PIECES FOR 200 THOUSAND                                                        {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK} 1 PIECE 50 THOUSAND                                                             {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK} 10 PIECE 50 THOUSAND                                                             {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK} THANK YOU FOR USING OUR SERVICES                                                 {Style.RESET_ALL}  
            {Fore.YELLOW + Back.BLACK} ARE THERE OTHER SERVICES?                                                          {Style.RESET_ALL}  
            {Fore.YELLOW + Back.BLACK} 1.YES                                                                             {Style.RESET_ALL}  
            {Fore.YELLOW + Back.BLACK} 2.NO                                                                           {Style.RESET_ALL}  
            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
            uzs_200000 -=1
            uzs_50000 -=1
            uzs_5000 -=10
            if yakun_yoki_menyu == 1:
                menyu_eng()
            else:
                print("""
                _______________________________________________________________________________________
                        """)
                boshlash()
        elif tasdiqlash == 2:
            valyuta_eng()
        else:
            menyu_eng()
    elif uzs_miqdori == 3 and karta_balans >=uzs_miqdori:
        uzs_miqdori=100000
        foiz=uzs_miqdori/100
        yechish=uzs_miqdori+foiz
        b=karta_balans-yechish
        print(f"""
        _______________________________________
        |                                     
        |   THE SUM IS : {uzs_miqdori}        
        |   PERCENT : {foiz}                  
        |   TOTAL : {yechish}                 
        |                                     
        ---------------------------------------
        """)
        tasdiqlash = int(input(f"""
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
        {Fore.YELLOW + Back.BLACK} | 1.CONFIRMATION | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   2.RE-ENTER   | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |    3.CENCEL    | {Style.RESET_ALL}
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
     
     
     {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))
        if tasdiqlash == 1 and 50000 <=uzs_50000*50000 and 10000 <= uzs_10000 *10000 and 8*5000 <= uzs_5000*5000:


            print(f"""
            _______________________________________
            |            CHEK:                    
            |   THE SUM IS  : {uzs_miqdori}      
            |   PERCENT : {foiz}                  
            |   TOTAL : {yechish}                 
            |   CARD: 9860********6796            
            |   AMOUNT REMAINING ON THE CARD: {b} 
            ---------------------------------------
            """)
            yakun_yoki_menyu = (int(input(f"""
            {Fore.YELLOW + Back.BLACK} RELEASED:                                                                        {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} 1 PIECES FOR 50 THOUSAND                                                        {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK} 1 PIECE 10 THOUSAND                                                             {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK} 8 PIECE 5 THOUSAND                                                             {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK} THANK YOU FOR USING OUR SERVICES                                                 {Style.RESET_ALL}  
            {Fore.YELLOW + Back.BLACK} ARE THERE OTHER SERVICES?                                                          {Style.RESET_ALL}  
            {Fore.YELLOW + Back.BLACK} 1.YES                                                                             {Style.RESET_ALL}  
            {Fore.YELLOW + Back.BLACK} 2.NO                                                                           {Style.RESET_ALL}  
            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
            uzs_5000 -=8
            uzs_50000 -=1
            uzs_10000 -=1
            if yakun_yoki_menyu == 1:
                menyu_eng()
            else:
                print("""
                _______________________________________________________________________________________
                        """)
                boshlash()
        elif tasdiqlash == 2:
            valyuta_eng()
        else:
            menyu_eng()
    elif uzs_miqdori == 4 and karta_balans >=uzs_miqdori:
        uzs_miqdori=50000
        foiz=uzs_miqdori/100
        yechish=uzs_miqdori+foiz
        b=karta_balans-yechish
        print(f"""
        _______________________________________
        |                                    
        |   THE SUM IS : {uzs_miqdori}       
        |   PERCENT : {foiz}                 
        |   TOTAL : {yechish}                
        |                                    
        ---------------------------------------
        """)

        tasdiqlash = int(input(f"""
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
        {Fore.YELLOW + Back.BLACK} | 1.CONFIRMATION | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   2.RE-ENTER   | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |    3.CENCEL    | {Style.RESET_ALL}
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
     
     
     {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))
        if tasdiqlash == 1 and 50000 <= uzs_50000*50000:



            print(f"""
            _______________________________________
            |            CHEK:                    
            |   THE SUM IS  : {uzs_miqdori}  .    
            |   PERCENT : {foiz}                  
            |   TOTAL : {yechish}                 
            |   CARD: 9860********6796            
            |   AMOUNT REMAINING ON THE CARD: {b} 
            ---------------------------------------
            """)
            yakun_yoki_menyu = (int(input(f"""
            {Fore.YELLOW + Back.BLACK} RELEASED:                                                                        {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} 1 PIECES FOR 50 THOUSAND                                                        {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK} THANK YOU FOR USING OUR SERVICES                                                 {Style.RESET_ALL}  
            {Fore.YELLOW + Back.BLACK} ARE THERE OTHER SERVICES?                                                          {Style.RESET_ALL}  
            {Fore.YELLOW + Back.BLACK} 1.YES                                                                             {Style.RESET_ALL}  
            {Fore.YELLOW + Back.BLACK} 2.NO                                                                           {Style.RESET_ALL}  
            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))

            uzs_50000 -=1

            if yakun_yoki_menyu == 1:
                menyu_eng()
            else:
                print("""
                _______________________________________________________________________________________
                        """)
                boshlash()
        elif tasdiqlash == 2:
            valyuta_eng()
        else:
            menyu_eng()
    elif uzs_miqdori == 5 and karta_balans >=uzs_miqdori :

        uzs_miqdori=20000
        foiz=uzs_miqdori/100
        yechish=uzs_miqdori+foiz
        b=karta_balans-yechish
        print(f"""
        _______________________________________
        |                                     
        |   THE SUM IS : {uzs_miqdori}        
        |   PERCENT : {foiz}                  
        |   TOTAL : {yechish}                 
        |                                     
        ---------------------------------------
        """)

        tasdiqlash = int(input(f"""
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
        {Fore.YELLOW + Back.BLACK} | 1.CONFIRMATION | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   2.RE-ENTER   | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |    3.CENCEL    | {Style.RESET_ALL}
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
     
     
     {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))
        if tasdiqlash == 1:




            print(f"""
            _______________________________________
            |            CHEK:                    
            |   THE SUM IS  : {uzs_miqdori}  .    
            |   PERCENT : {foiz}                  
            |   TOTAL : {yechish}                 
            |   CARD: 9860********6796            
            |   AMOUNT REMAINING ON THE CARD: {b} 
            ---------------------------------------
            """)
            yakun_yoki_menyu = (int(input(f"""
            {Fore.YELLOW + Back.BLACK} RELEASED:                                                                        {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} 1 PIECES FOR 20 THOUSAND                                                        {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK} THANK YOU FOR USING OUR SERVICES                                                 {Style.RESET_ALL}  
            {Fore.YELLOW + Back.BLACK} ARE THERE OTHER SERVICES?                                                          {Style.RESET_ALL}  
            {Fore.YELLOW + Back.BLACK} 1.YES                                                                             {Style.RESET_ALL}  
            {Fore.YELLOW + Back.BLACK} 2.NO                                                                           {Style.RESET_ALL}  
            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
            uzs_20000 -=1
            if yakun_yoki_menyu == 1:
                menyu_eng()
            else:
                print("""
                _______________________________________________________________________________________
                        """)
                boshlash()
        elif tasdiqlash == 2:
            valyuta_eng()
        else:
            menyu_eng()

    else:

        uzs_miqdori=int(input("""
              INPUT THE AMOUT:
        """))
        foiz=uzs_miqdori/100
        yechish=uzs_miqdori+foiz
        b=karta_balans-yechish
        print(f"""
        _______________________________________
        |                                     
        |   THE SUM IS : {uzs_miqdori}        
        |   PERCENT : {foiz}                  
        |   TOTAL : {yechish}                 
        |                                     
        ---------------------------------------
        """)

        tasdiqlash = int(input(f"""
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
        {Fore.YELLOW + Back.BLACK} | 1.CONFIRMATION | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   2.RE-ENTER   | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |    3.CENCEL    | {Style.RESET_ALL}
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
     
     
     {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))
        if tasdiqlash == 1:

            print(f"""
                _______________________________________
                |            CHEK:                    
                |   THE SUM IS  : {uzs_miqdori}  .    
                |   PERCENT : {foiz}                  
                |   TOTAL : {yechish}                 
                |   CARD: 9860********6796            
                |   AMOUNT REMAINING ON THE CARD: {b} 
                ---------------------------------------
                """)

            menyu_eng()
            print("""
                 _______________________________________________________________________________________
                         """)
        elif tasdiqlash == 2:
            valyuta_eng()
        else:
            menyu_eng()



def menyu_eng():
    menyu = int(input(f"""                            {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}
                            {Fore.YELLOW + Back.BLACK} |SELECT A SERVICE:| {Style.RESET_ALL}
                            {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}

               {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |   1.PINCODE CHANGE     | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |      2.GET CASH        | {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}
               
               
               {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL} 
               {Fore.YELLOW + Back.BLACK} |     3.CARD BALANCE     | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   4.SMS NOTIFICATION   | {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}
                                 
                                 
                                 {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}
                                 {Fore.YELLOW + Back.BLACK} |     5.CARD ISSUING     | {Style.RESET_ALL}
                                 {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}
                {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}"""))
    if menyu == 1:
        pincod_eng()
    elif menyu == 2:
        valyuta_eng()
    elif menyu == 3:
        kartabalans_eng()
    elif menyu == 4:
        smsxabarnoma_eng()
    else:
        print("THANK YOU FOR USING OUR SERVICES.")
        print("""
        _______________________________________________________________________________
        """)
        boshlash()


def inglizcha():

    n=2
    password=1224
    while n>=0 :
        kod=int(input(f"""
    {Fore.YELLOW + Back.BLACK}  INPUT PINCODE =>   {Style.RESET_ALL}"""))

        if kod == password:
            n=-1
            menyu_eng()
        elif n>0:
            n -=1
        elif n == 0:
            print("""
            YOU HAVE ENTERED THE PIN CODE TOO MANY TIMES. THIS IS WHY THE CARD REMAINS IN THE ATM.""")
            print("""
            _______________________________________________________________________________________________________
            """)
            boshlash()
def smsxabarnoma_ru():
    n = 1
    while n > 0:
        numbers = int(input(f"{Fore.YELLOW + Back.BLACK}  ВВЕДИТЕ НОВЫЙ НОМЕР   => +998 : {Style.RESET_ALL}"))
        if 100000000 <= numbers <= 999999999:
            tasdiqlash = int(input(f"""
                                  {Fore.YELLOW + Back.BLACK} |-------------------------| {Style.RESET_ALL}
                                  {Fore.YELLOW + Back.BLACK} |      ИЗМЕНИТЬ НОМЕР?    | {Style.RESET_ALL}
                                  {Fore.YELLOW + Back.BLACK} |-------------------------| {Style.RESET_ALL}

            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}      {Fore.YELLOW + Back.BLACK} |--------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
            {Fore.YELLOW + Back.BLACK} |     1.ДА       | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK}|2.ПОВТОРНОЕ ВВЕДЕНИЕ| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   3.ОТМЕНА     | {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK}|--------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}"""))
            if tasdiqlash == 1:
                print("НОМЕР УСПЕШНО ИЗМЕНЕН.")
                n = -1
                menyu_ru()
            elif tasdiqlash == 2:
                smsxabarnoma_ru()
            else:
                menyu_ru()
        else:
            print("НОМЕР ДОЛЖЕН БЫТЬ 9 ЦИФР.")
def pinkod_ru():
    n = 1
    while n > 0:
        yangikod = int(input(f"{Fore.YELLOW + Back.BLACK}  ВВЕДИТЕ НОВЫЙ ПИН-КОД   =>  {Style.RESET_ALL}"))
        if 1000 <= yangikod <= 9999:
            tasdiqlash = int(input(f"""
                                  {Fore.YELLOW + Back.BLACK} |-------------------------| {Style.RESET_ALL}
                                  {Fore.YELLOW + Back.BLACK} |         ИЗМЕНЯТЬ?       | {Style.RESET_ALL}
                                  {Fore.YELLOW + Back.BLACK} |-------------------------| {Style.RESET_ALL}

            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |---------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
            {Fore.YELLOW + Back.BLACK} |     1.ДА       | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2..ПОВТОРНОЕ ВВЕДЕНИЕ| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   3.ОТМЕНА     | {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |---------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}"""))
            if tasdiqlash == 1:
                print("ПИН-КОД УСПЕШНО ИЗМЕНЕН.")
                n = -1
                menyu_ru()
            elif tasdiqlash == 2:
                pinkod_ru()
            else:
                menyu_ru()
        else:
            print("ПИН-КОД ДОЛЖЕН БЫТЬ 4 ЦИФРЫ.")
def kartabalans_ru():
    print(f"""
    | НА ВАШЕЙ КАРТЕ 1 000 000 СОМ|
    """)
    menyu_ru()
def valyuta_ru():
    karta_balans = 1000000
    uzs_1000 = 500
    uzs_2000 = 300
    uzs_5000 = 200
    uzs_10000 = 100
    uzs_20000 = 50
    uzs_50000 = 30
    uzs_100000 = 20
    uzs_200000 = 20
    umumiy_summa = uzs_200000 * 200000 + uzs_100000 * 100000 + uzs_50000 * 50000 + uzs_20000 * 20000 + uzs_10000 * 10000 + uzs_5000 * 5000 + uzs_2000 * 2000 + uzs_1000 * 1000
    uzs_miqdori = int(
        input(F"""                            {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}
                            {Fore.YELLOW + Back.BLACK} |  ВВЕДИТЕ ДЕНЬГИ | {Style.RESET_ALL}
                            {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}

               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |   1.500 000    | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   2.300 000    | {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL} 
               {Fore.YELLOW + Back.BLACK} |   3.100 000    | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |     4.50 000   | {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL} 
               {Fore.YELLOW + Back.BLACK} |    5.20 000    | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 6.ДРУГАЯ СУММА | {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
    {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}"""))
    if uzs_miqdori == 1 and karta_balans >= uzs_miqdori:
        uzs_miqdori = 500000
        foiz = uzs_miqdori / 100
        yechish = uzs_miqdori + foiz
        b = karta_balans - yechish
        print(f"""
        _______________________________________
        |                                     
        |   ДЕНЬГИ: {uzs_miqdori}        
        |   ПРОЦЕНТ : {foiz}                  
        |   ОБЩИЙ : {yechish}                 
        |                                     
        ---------------------------------------
        """)

        tasdiqlash = int(input(F"""
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |--------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
        {Fore.YELLOW + Back.BLACK} | 1.ПОДТВЕРЖДЕНИЕ| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.ПОВТОРНОЕ ВВЕДЕНИЕ| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |    3.ОТМЕНА    | {Style.RESET_ALL}
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |--------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


     {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))
        if tasdiqlash == 1 and tasdiqlash <= umumiy_summa and tasdiqlash <= uzs_200000 * 200000 and tasdiqlash <= uzs_100000 * 100000:

            print(f"""
            _______________________________________
            |            CHEK:                    
            |   ДЕНЬГИ  : {uzs_miqdori}  .    
            |   ПРОЦЕНТ : {foiz}                  
            |   ОБЩИЙ : {yechish}                 
            |   КАРТА: 9860********6796            
            |   ОСТАЛОСЬ ДЕНЕГ НА КАРТЕ: {b} 
            ---------------------------------------
            """)
            yakun_yoki_menyu = (int(input(f"""
             
            {Fore.YELLOW + Back.BLACK} ЕСТЬ ДРУГИЕ УСЛУГИ?                                                              {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK} 1.ДА                                                                                 {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK} 2.НЕТ                                                                                 {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}  =>  {Style.RESET_ALL} 
            """)))
            if yakun_yoki_menyu == 1:
                menyu_ru()
            else:
                print("""
                ______________________________________________________________________________
                """)
                boshlash()
        elif tasdiqlash == 2:
            valyuta_ru()
        else:
            menyu_ru()
    elif uzs_miqdori == 2 and karta_balans >= uzs_miqdori:
        uzs_miqdori = 300000
        foiz = uzs_miqdori / 100
        yechish = uzs_miqdori + foiz
        b = karta_balans - yechish
        print(f"""
        _______________________________________
        |                                     
        |   ДЕНЬГИ: {uzs_miqdori}        
        |   ПРОЦЕНТ : {foiz}                  
        |   ОБЩИЙ : {yechish}                 
        |                                     
        ---------------------------------------
        """)

        tasdiqlash = int(input(F"""
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |--------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
        {Fore.YELLOW + Back.BLACK} | 1.ПОДТВЕРЖДЕНИЕ| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.ПОВТОРНОЕ ВВЕДЕНИЕ| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |    3.ОТМЕНА    | {Style.RESET_ALL}
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |--------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


     {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))
        if tasdiqlash == 1 and tasdiqlash <= umumiy_summa and tasdiqlash <= uzs_200000 * 200000 and tasdiqlash <= uzs_100000 * 100000:

            print(f"""
            _______________________________________
            |            CHEK:                    
            |   ДЕНЬГИ  : {uzs_miqdori}  .    
            |   ПРОЦЕНТ : {foiz}                  
            |   ОБЩИЙ : {yechish}                 
            |   КАРТА: 9860********6796            
            |   ОСТАЛОСЬ ДЕНЕГ НА КАРТЕ: {b} 
            ---------------------------------------
            """)
            yakun_yoki_menyu = (int(input(f"""
             
            {Fore.YELLOW + Back.BLACK} ЕСТЬ ДРУГИЕ УСЛУГИ?                                                              {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK} 1.ДА                                                                                 {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK} 2.НЕТ                                                                                 {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}  =>  {Style.RESET_ALL} 
            """)))
            if yakun_yoki_menyu == 1:
                menyu_ru()
            else:
                print("""
                ______________________________________________________________________________
                """)
                boshlash()
    elif uzs_miqdori == 3 and karta_balans >= uzs_miqdori:
        uzs_miqdori = 100000
        foiz = uzs_miqdori / 100
        yechish = uzs_miqdori + foiz
        b = karta_balans - yechish
        print(f"""
        _______________________________________
        |                                     
        |   ДЕНЬГИ: {uzs_miqdori}        
        |   ПРОЦЕНТ : {foiz}                  
        |   ОБЩИЙ : {yechish}                 
        |                                     
        ---------------------------------------
        """)

        tasdiqlash = int(input(F"""
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |--------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
        {Fore.YELLOW + Back.BLACK} | 1.ПОДТВЕРЖДЕНИЕ| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.ПОВТОРНОЕ ВВЕДЕНИЕ| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |    3.ОТМЕНА    | {Style.RESET_ALL}
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |--------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


     {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))
        if tasdiqlash == 1 and tasdiqlash <= umumiy_summa and tasdiqlash <= uzs_200000 * 200000 and tasdiqlash <= uzs_100000 * 100000:

            print(f"""
            _______________________________________
            |            CHEK:                    
            |   ДЕНЬГИ  : {uzs_miqdori}  .    
            |   ПРОЦЕНТ : {foiz}                  
            |   ОБЩИЙ : {yechish}                 
            |   КАРТА: 9860********6796            
            |   ОСТАЛОСЬ ДЕНЕГ НА КАРТЕ: {b} 
            ---------------------------------------
            """)
            yakun_yoki_menyu = (int(input(f"""
             
            {Fore.YELLOW + Back.BLACK} ЕСТЬ ДРУГИЕ УСЛУГИ?                                                              {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK} 1.ДА                                                                                 {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK} 2.НЕТ                                                                                 {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}  =>  {Style.RESET_ALL} 
            """)))
            if yakun_yoki_menyu == 1:
                menyu_ru()
            else:
                print("""
                ______________________________________________________________________________
                """)
                boshlash()
    elif uzs_miqdori == 4 and karta_balans >= uzs_miqdori:
        uzs_miqdori = 50000
        foiz = uzs_miqdori / 100
        yechish = uzs_miqdori + foiz
        b = karta_balans - yechish
        print(f"""
        _______________________________________
        |                                     
        |   ДЕНЬГИ: {uzs_miqdori}        
        |   ПРОЦЕНТ : {foiz}                  
        |   ОБЩИЙ : {yechish}                 
        |                                     
        ---------------------------------------
        """)

        tasdiqlash = int(input(F"""
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |--------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
        {Fore.YELLOW + Back.BLACK} | 1.ПОДТВЕРЖДЕНИЕ| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.ПОВТОРНОЕ ВВЕДЕНИЕ| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |    3.ОТМЕНА    | {Style.RESET_ALL}
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |--------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


     {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))
        if tasdiqlash == 1 and tasdiqlash <= umumiy_summa and tasdiqlash <= uzs_200000 * 200000 and tasdiqlash <= uzs_100000 * 100000:

            print(f"""
            _______________________________________
            |            CHEK:                    
            |   ДЕНЬГИ  : {uzs_miqdori}  .    
            |   ПРОЦЕНТ : {foiz}                  
            |   ОБЩИЙ : {yechish}                 
            |   КАРТА: 9860********6796            
            |   ОСТАЛОСЬ ДЕНЕГ НА КАРТЕ: {b} 
            ---------------------------------------
            """)
            yakun_yoki_menyu = (int(input(f"""
             
            {Fore.YELLOW + Back.BLACK} ЕСТЬ ДРУГИЕ УСЛУГИ?                                                              {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK} 1.ДА                                                                                 {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK} 2.НЕТ                                                                                 {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}  =>  {Style.RESET_ALL} 
            """)))
            if yakun_yoki_menyu == 1:
                menyu_ru()
            else:
                print("""
                ______________________________________________________________________________
                """)
                boshlash()
    elif uzs_miqdori == 5 and karta_balans >= uzs_miqdori:
        uzs_miqdori = 20000
        foiz = uzs_miqdori / 100
        yechish = uzs_miqdori + foiz
        b = karta_balans - yechish
        print(f"""
        _______________________________________
        |                                     
        |   ДЕНЬГИ: {uzs_miqdori}        
        |   ПРОЦЕНТ : {foiz}                  
        |   ОБЩИЙ : {yechish}                 
        |                                     
        ---------------------------------------
        """)

        tasdiqlash = int(input(F"""
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |--------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
        {Fore.YELLOW + Back.BLACK} | 1.ПОДТВЕРЖДЕНИЕ| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.ПОВТОРНОЕ ВВЕДЕНИЕ| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |    3.ОТМЕНА    | {Style.RESET_ALL}
        {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |--------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


     {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))
        if tasdiqlash == 1 and tasdiqlash <= umumiy_summa and tasdiqlash <= uzs_200000 * 200000 and tasdiqlash <= uzs_100000 * 100000:

            print(f"""
            _______________________________________
            |            CHEK:                    
            |   ДЕНЬГИ  : {uzs_miqdori}  .    
            |   ПРОЦЕНТ : {foiz}                  
            |   ОБЩИЙ : {yechish}                 
            |   КАРТА: 9860********6796            
            |   ОСТАЛОСЬ ДЕНЕГ НА КАРТЕ: {b} 
            ---------------------------------------
            """)
            yakun_yoki_menyu = (int(input(f"""
             
            {Fore.YELLOW + Back.BLACK} ЕСТЬ ДРУГИЕ УСЛУГИ?                                                              {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK} 1.ДА                                                                                 {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK} 2.НЕТ                                                                                 {Style.RESET_ALL} 
            {Fore.YELLOW + Back.BLACK}  =>  {Style.RESET_ALL} 
            """)))
            if yakun_yoki_menyu == 1:
                menyu_ru()
            else:
                print("""
                ______________________________________________________________________________
                """)
                boshlash()

    else:

        uzs_miqdori = int(input("""
              INPUT THE AMOUT:
        """))

        foiz = uzs_miqdori / 100
        yechish = uzs_miqdori + foiz
        b = karta_balans - yechish
        print(f"""
           _______________________________________
           |                                     
           |   ДЕНЬГИ: {uzs_miqdori}        
           |   ПРОЦЕНТ : {foiz}                  
           |   ОБЩИЙ : {yechish}                 
           |                                     
           ---------------------------------------
           """)

        tasdiqlash = int(input(F"""
           {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |--------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
           {Fore.YELLOW + Back.BLACK} | 1.ПОДТВЕРЖДЕНИЕ| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.ПОВТОРНОЕ ВВЕДЕНИЕ| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |    3.ОТМЕНА    | {Style.RESET_ALL}
           {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |--------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


        {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))
        if tasdiqlash == 1 and tasdiqlash <= umumiy_summa and tasdiqlash <= uzs_200000 * 200000 and tasdiqlash <= uzs_100000 * 100000:

            print(f"""
               _______________________________________
               |            CHEK:                    
               |   ДЕНЬГИ  : {uzs_miqdori}  .    
               |   ПРОЦЕНТ : {foiz}                  
               |   ОБЩИЙ : {yechish}                 
               |   КАРТА: 9860********6796            
               |   ОСТАЛОСЬ ДЕНЕГ НА КАРТЕ: {b} 
               ---------------------------------------
               """)
            yakun_yoki_menyu = (int(input(f"""

               {Fore.YELLOW + Back.BLACK} ЕСТЬ ДРУГИЕ УСЛУГИ?                                                              {Style.RESET_ALL} 
               {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
               {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
               {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
               {Fore.YELLOW + Back.BLACK} 1.ДА                                                                                 {Style.RESET_ALL} 
               {Fore.YELLOW + Back.BLACK} 2.НЕТ                                                                                 {Style.RESET_ALL} 
               {Fore.YELLOW + Back.BLACK}  =>  {Style.RESET_ALL} 
               """)))
            if yakun_yoki_menyu == 1:
                menyu_ru()
            else:
                print("""
                   ______________________________________________________________________________
                   """)
                boshlash()


def menyu_ru():
    menyu = int(input(f"""                            {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}
                            {Fore.YELLOW + Back.BLACK} |ВЫБЕРИТЕ УСЛУГУ :| {Style.RESET_ALL}
                            {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}

               {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |   1.ИЗМЕНЕНИЕ ПИНКОДА  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |      2.НАЛИЧНЫЕ        | {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}
               
               
               {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL} 
               {Fore.YELLOW + Back.BLACK} |     3.БАЛАНС КАРТЫ     | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   4.СМС-уведомление    | {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}
                                 
                                 
                                 {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}
                                 {Fore.YELLOW + Back.BLACK} |     5.ВЫПУСК КАРТЫ     | {Style.RESET_ALL}
                                 {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}
                {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}"""))
    if menyu == 1:
        pinkod_ru()
    elif menyu == 2:
        valyuta_ru()
    elif menyu == 3:
        kartabalans_ru()
    elif menyu == 4:
        smsxabarnoma_ru()
    else:
        print("THANK YOU FOR USING OUR SERVICES.")
        print("""
        _______________________________________________________________________________
        """)
        boshlash()

def ruscha():
    n=2
    password=1224
    while n>=0 :
        kod=int(input(f"""
    {Fore.YELLOW + Back.BLACK}  ВВЕДИТЕ ПИН-код =>   {Style.RESET_ALL}"""))

        if kod == password:
            n=-1
            menyu_ru()
        elif n>0:
            n -=1
        elif n == 0:
            print("""
            ВЫ ВВЕДИЛИ КОД СЛИШКОМ МНОГО РАЗ. ПОЭТОМУ ПЛАСТИКОВАЯ КАРТА ОСТАЕТСЯ В БАНКОМАТЕ.""")
            print("""
            _______________________________________________________________________________________________________
            """)
            boshlash()





def boshlash():
    print("Kartanggizni kiriting: ")
    til=int(input(f"""                               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
                               {Fore.YELLOW + Back.BLACK} | Tilni tanlang: | {Style.RESET_ALL}
                               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
                                                            
     {Fore.YELLOW + Back.BLACK} |---------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |---------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |---------------| {Style.RESET_ALL}        
     {Fore.YELLOW + Back.BLACK} |   1.O'ZBEK    | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   2.ENGLISH   | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   3.РУССЛИЙ   | {Style.RESET_ALL}
     {Fore.YELLOW + Back.BLACK} |---------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |---------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |---------------| {Style.RESET_ALL}
     
     
     {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL} """))
    if til == 1:
        uzbekcha()
    elif til == 2:
        inglizcha()
    elif til == 3 :
        ruscha()
    else:
        boshlash()
if __name__ == "__main__":
    boshlash()

#CREATED BY ZAFARBEK