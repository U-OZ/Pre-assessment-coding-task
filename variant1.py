#かけ算表　12*12

#xはかける数
for x in range(1, 13):
    #yはかけられる数
    for y in range(1, 13):
        ans = x * y
        #出力される値を等間隔で表示
        print(f'{ans:<6}', end="")
    print()
