color=input("ENTER COLORS SEPERATED BY COMAS")
color_list1=color.split(',')
print("color_list1")

print("FIRST COLOR:", color_list1[0])
print("LAST COLOR:", color_list1[-1])
color_list2=["Red", "orange", "black", "white"]

print("color-list not contained in color-list2 are:")
diff=list(set(color_list1)-set(color_list2))
print(diff)
color_int_list=[]
for color in color_list1:
    color_int_list.append(len(color))
    print(f"List of integer corresponding to each color: {color_int_list}")