## Problem
welcome_message = "★☆★ Microwave ★☆★"
print(f"\n\t {welcome_message} \n")


## Get input

# Buttons
print('=' * 10 + " Buttons " + '=' * 10)
print("\t1. 10 sec\t2. 30 sec")
print("\t3. 1 min\t4. 10 min")
print("\t\t\t5. Work\n")

time = 0
menu = input("\t\t\t\t [ Select ] : ")
while menu != '5':
    while menu not in ['1', '2' ,'3', '4', '5']:
        print("\t\t\t\t\t\t\t잘못된 입력!")
        menu = input("\t\t\t\t [ Re: Select ] : ")

    if menu == '1':
        time += 10
    elif menu == '2':
        time += 30
    elif menu == '3':
        time += 60
    elif menu == '4':
        time += 60 * 10
    else:
        break

    print("\t\t 작동 시간 : [%2d:%02d]" % (time // 60, time % 60))
    menu = input("\t\t\t\t [ Select ] : ")

print("\n\t전자레인지 작동! (%2d:%02d)" % (time // 60, time % 60))