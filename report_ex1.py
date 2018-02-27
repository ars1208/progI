def get_ratio(place1, place2, place):
    ratio = int(place[place1]) / int(place[place2])
    return ratio

def display_place_list(place):
    for i in len(place):
        print(place[i][0], ":", get_ratio(place[i][1], "筑波大学", place))
        i += 1

place = {"筑波キャンパス" : 2577286}

i = 0
print("データを入力してください。「.」を入力したら終了です。")
while i < 100:
    new_place = input().split()
    if new_place[0] == ".":
        break
    if new_place[0] in place.keys():
        print("その名前のデータはすでに存在します。上書きしますか？[y/n]")
        choice = input()
        if choice == "y":
            place[new_place[0]] = new_place[1]
            print("上書きしました。")
        elif choice == "n":
            print("上書きしませんでした。")
            continue
    place[new_place[0]] = new_place[1]
    i += 1
