
place = {"筑波キャンパス" : 2577286}

i = 0
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
