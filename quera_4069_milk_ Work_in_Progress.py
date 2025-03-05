# https://quera.org/problemset/4069
# شماره سوال 4069
# با ارامش بخون . 
#  شیر و اب 



n=int(input())
txt=input().upper()


count_shirr=txt.count("S")
count_aabb=txt.count("W")

for i in txt:
    if i=="W" or i=="S":
        if len(txt)== n:
            if txt[len(txt)-1]=="S":
                count_shirr-=1

            elif txt[len(txt)-1]=="W":
                count_aabb-=1


if count_aabb==count_shirr:
    print("=")

elif count_aabb>count_shirr:
    print("W")

elif count_aabb<count_shirr:
    print("S")
#____________________________________________ روشهای زیر را 71 درصد امتیاز گرفتم
# n=input()
# txt=input().upper()


# count_shirr=txt.count("S")
# count_aabb=txt.count("W")

# if txt[len(txt)-1]=="S":
#     count_shirr-=1

# elif txt[len(txt)-1]=="W":
#     count_aabb-=1


# if count_aabb==count_shirr:
#     print("=")

# elif count_aabb>count_shirr:
#     print("W")

# elif count_aabb<count_shirr:
#     print("S")

####################روش 2
# n=int(input())
# txt=input().upper()

# count_shirr=txt.count("S")
# count_aabb=txt.count("W")

# if txt[len(txt)-1]=="S":
#     count_shirr-=1
# elif txt[len(txt)-1]=="W":
#     count_aabb-=1
  

# tarkibe_ghdim_shir= 1/2
# tarkibe_ghdim_aabb=1/2
# jam_khorde_shode=1/2
# mizane_masrafshode_shir_naaii=1/2
# mizane_masrafshode_aabb_naaii=1/2


# for i in range(count_shirr ):
#     mizane_masrafshode_shir=(tarkibe_ghdim_shir *(1/2))+(1/2)
#     mizane_masrafshode_shir_naaii += mizane_masrafshode_shir

# for i in range(count_aabb ):
#     mizane_masrafshode_aabb=(tarkibe_ghdim_aabb *(1/2))+(1/2)
#     mizane_masrafshode_aabb_naaii += mizane_masrafshode_aabb

# # print(mizane_masrafshode_shir_naaii)
# # print(mizane_masrafshode_aabb_naaii)

# if mizane_masrafshode_shir_naaii==mizane_masrafshode_aabb_naaii:
#     print("=")
# elif mizane_masrafshode_shir_naaii>mizane_masrafshode_aabb_naaii:
#     print("S")
# elif mizane_masrafshode_shir_naaii<mizane_masrafshode_aabb_naaii:
#     print("W")

    



    

