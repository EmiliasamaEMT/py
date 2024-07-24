def make_album(singer_name,album_name,count_songs=None):
    """打个胶先"""
    album={
        "s_name":singer_name,
        "a_name":album_name
    }
    if count_songs:
        album["c_songs"]=count_songs
    return  album
a1=make_album("ts","1989")
a2=make_album('aw',"aw","9")
a3=make_album('ed','soy')
print(f"{a1}\n{a2}\n{a3}")

#
while True:
    print("please enter some infomation.")
    print('enter"q"to quit the program')
    s_name=input("please enter singer's name:")
    if s_name=="q":
        break
    a_name=input("please enter album's name:")
    if a_name=="q":
        break
    a4=make_album(s_name,a_name)
    print(a4)