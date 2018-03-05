eki_soto = ["東京", "有楽町", "新橋", "浜松町", "田町", "品川", "大崎", "五反田", "目黒", "恵比寿", "渋谷", "原宿", "代々木", "新宿", "新大久保", "高田馬場", "目白", "池袋", "大塚", "巣鴨", "駒込", "田端", "西日暮里", "日暮里", "鶯谷", "上野", "御徒町", "秋葉原", "神田"]
jikan_soto = [2, 2, 2, 2, 3, 2, 2, 2, 3, 2, 3, 2, 2, 2, 3, 1, 3, 3, 1, 2, 3, 1, 2, 1, 2, 2, 2, 2, 2]

print("降車駅名を入力してください")
kousya = input()

def exist(name, station):
    if name in station:
        return True
    else:
        return False

def station_list(name, station, time):
    jikan = 0
    eki = []
    num = station.index(kousya)
    print("{0}駅は、{1}番目の駅です".format(name, num))
    print("==============================")
    print("[外回り]")
    for i in range(num + 1):
        jikan += time[i]
        eki.append(eki_soto[i])
        i += 1
    print(eki)
    print("乗車時間は%d分です。" % int(jikan - time[i]))

if exist(kousya, eki_soto):
    station_list(kousya, eki_soto, jikan_soto)
else:
    print("その駅名は存在しません。")
