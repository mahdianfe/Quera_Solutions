# https://quera.org/problemset/2886
# # همانطور که از اسمش برمی‌آید، آقای خوش‌قلب به فکر پروفسور باقر (که یک کاربر ناشی است) هم می‌باشد.
# پروفسور باقر یک ساعت دیواری نو خریده است # و آن را در جایی قرار داده است که
# هنگامی که تلویزیون می‌بیند، از آینه بتواند آن ساعت را ببیند و بفهمد که ساعت چند است
# و چقدر مانده است تا مسابقه‌ی ایران در المپیک شروع شود. اما متاسفانه او بلد نیست که از آینه ساعت را بخواند.
# آقای خوش‌قلب به کمک پروفسور رفته است (البته به صورت مجازی) و می‌خواهد به او بگوید که ساعت چند است.
# پروفسور از طریق ایمیل برای آقای ‌خوش‌قلب، تصویری را که در آینه می‌بیند ارسال کرده است.
# آقای خوش‌‌قلب (از آنجایی که فقط خوش‌قلب است) نمی‌تواند از روی اطلاعاتی که پروفسور به او داده است، بفهمد که ساعت چند است.
# # # او از شما می خواهد که این کار را انجام دهید.
# # # ساعت پروفسور به شکل زیر (در این تصویر این ساعت، ساعت ۰۰:۰۰ را نشان می‌دهد) است و دو ویژگی دارد:
# # # ۱. عقربه‌ی ساعت شمار آن فقط روی اعداد صحیح می‌ایستد و (برعکس ساعت‌های عادی) به هیچ وجه بین شماره‌های ساعت توقفی ندارد. برای مثال زمانی که ساعت در بازه‌ی (۵:۰۰,۶:۰۰] است، عقربه‌ی ساعت شمار دقیقا روی شماره‌ی ۵ قرار دارد اما به محض اینکه ساعت ۶:۰۰ شود، عقربه ساعت شمار در یک حرکت انفجاری به سرعت به روی شماره‌ی ۶ می‌رود و تا زمانی که ساعت ۷:۰۰ شود، به روی آن می‌ماند و کوچکترین تکانی نمی‌خورد.
# # # ۲. شماره‌های این ساعت (مانند ساعت زیر) با اعداد مشخص نشده‌اند. Image result for clock
# # # ورودی
# # # در سطر اول ورودی به ترتیب دو عدد aa و bb آمده است که نشان‌دهنده‌ی این است که در تصویری که پروفسور برای آقای خوش‌قلب ارسال کرده است، ساعت چند است. بدین صورت که aa نمایانگر مکانی است که در تصویر ارسالی از پروفسور، عقربه‌ی ساعت شمار در آن قرار دارد و bb مکانی است که عقربه‌ی دقیقه شمار در آن قرار دارد. از آنجایی که المپیک نیمه شب از تلویزیون پخش می‌شود، ساعت حتما بیشتر مساوی ساعت ۰۰:۰۰ نیمه شب و اکیدا کمتر از ساعت ۱۲:۰۰ ظهر است یعنی بازه ی (۰۰:۰۰,۱۲:۰۰]
# # # 0≤a≤11
# # # 0≤a≤11
# # # 0≤b≤59
# # # 0≤b≤59
# # # خروجی
# # # در تنها سطر خروجی با استفاده از تصویر ساعت در آینه، خروجی دهید که ساعت واقعاً چند است.

# # # خروجی شما باید به این شکل باشد:
# # # hh:mm
# # # hh:mm یعنی در دورقم اول مکان عقربه‌ی ساعت شمار و سپس یک دو نقطه و سپس مکان عقربه‌ی دقیقه شمار را خروجی دهید. اگر مکان عقربه‌ی ساعت شمار یا عقربه‌ی دقیقه شمار یک رقمی بود، به جای رقم سمت چپ 0 خروجی دهید. برای مثال اگر ساعت ۹:۰۵ بود، شما باید "09:05" خروجی دهید.
# دقت کنید که خروجی حتما باید در بازه‌ی (۰۰:۰۰,۱۲:۰۰] باشد یا به عبارتی دیگر:
# # # 0≤hh≤11
# # # 0≤hh≤11
# # # 0≤mm≤59
# # # 0≤mm≤59

###############################################################################################


n=input()
n=n.split()
a=int(n[0])
b=int(n[1])

a=12-a
b= 60 - b

if a==12:
    a=0

if b==60:
    b=0

if a<10 and b<10:
    print(f"{0}{a}:{0}{b}")

elif a<10 and b>=10:
    print(f"{0}{a}:{b}")

elif a>=10 and b<10:
    print(f"{a}:{0}{b}")

elif a>=10 and b>=10:
    print(f"{a}:{b}")

###############################################################################################

# # # مثال:
# # # 6 30
# # # 06:30