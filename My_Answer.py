import os


def clear():
    os.system('cls')
    print('\n')


def press_key_to_continue():
    key = input("\n——————按任意键继续\n")
    clear()


def q1():
    clear()
    print('回答问题1：')
    answer = '为什么不爽呢？是没有达到你的目的吗？（笑）。请不要用你的负面情绪来道德绑架我，让我为你的情绪负责。'
    print(answer)
    press_key_to_continue()


def q2():
    clear()
    print('回答问题2：')
    answer = ('什么叫 “不想承担男朋友的责任” ？大哥，我压根儿不想谈，我已经说了，我本科期间是不会谈恋爱的。\n'
              '那你呢？我跟你在一起的时候你承担过女朋友的责任吗？？我请问了？？\n'
              '还有，你懂什么叫情绪价值吗？闹麻了。这才过几天我就享受上了，我真是太幸福了。')
    print(answer)
    press_key_to_continue()


def q3():
    clear()
    print('回答问题3：')
    answer = ('你说的对，我真是太爽了，连我这么废物的人都有人喜欢，只能你的品味真好。\n'
              '不过，你以为我真的会在乎你那所谓的喜欢？你这是把我的存在当成你自我陶醉的工具了吧。\n'
              '反而是你，好像觉得我知道你喜欢我就应该有什么特别的反应。\n'
              '你这种略带指责的语气令我无语。')
    print(answer)
    press_key_to_continue()


def q4():
    clear()
    print('回答问题4：')
    answer = ('所以呢？你把喜欢说得这么轻飘飘，那说明你也对这份感情本来就不重视，你凭什么说我？\n'
              '你把喜欢说得这么一文不值，你根本就不懂什么叫爱。\n'
              '你以为你这样轻描淡写的文字就能伤害到我？我只是看清了你这颗冷漠的心罢了。')
    print(answer)
    press_key_to_continue()


def q5():
    clear()
    print('回答问题5：')
    answer = ('你觉得我可替代？行啊，那你去找你的替代品去，别在我面前晃。\n'
              '你这种把人当备胎的心态，真让人瞧不起，你就抱着你那所谓的 “磁场吸引” 自我陶醉去吧。')
    print(answer)
    press_key_to_continue()


def q6():
    clear()
    print('回答问题6：')
    answer = ('哦，那你还能有异性朋友确实牛批。\n'
              '你这叫什么朋友态度？这和冷血动物有啥区别？\n'
              '你以为你这种拒人于千里之外的样子很酷吗？')
    print(answer)
    press_key_to_continue()


def q7():
    clear()
    print('回答问题7：')
    answer = ('啊对对对，你太牛批了，我这种粗人根本不配和你在一起。\n'
              '你所谓的 “很快摆正位置” 不过是你自我感觉良好的借口。')
    print(answer)
    press_key_to_continue()


def q8():
    clear()
    print('回答问题8：')
    answer = '如果你真有这样的勇气，可以马上把我删除离开我的视线。像这种加星号着重强调的胜利宣言，在我看来只是哗众取宠罢了，疑似自我意识有些过剩，你告别与否没人在乎。'
    print(answer)
    press_key_to_continue()


def q910():
    clear()
    print('回答问题9和10：')
    answer = ('我是真的绷不住了。你既然当时自己要分就别后悔做过的决定，也别劝我摆清位置了。\n'
              '还让我认清形势，认清个锤子，pua这套话术你跟追你的龟男说去吧，赶紧去找个龟男发神经，在我这发癫我只会觉得你像个没训练完的ai。')
    print(answer)
    press_key_to_continue()


def q99():
    clear()
    answer = ('一大段小作文，每一句都流露出自己的自私和高傲。一边厌一边渴，盖不住的绿茶味。得不到就说对面渣男，也是没谁了。\n'
              '我帮你给你自己这段话做个注释吧，就是对对面有好感但还要把自己摆到上位者的地位，自己喜欢对方就是对对方的赏赐，对方回应了就是对自己死缠烂打，自己自恃清高，别人都是陪衬。\n'
              '都让你赢完了我还说什么，那你自个赢去吧关我屁事，是你care又不是我care，不过如果你又加我又纠缠我最后就是为了往我头上拉一坨屎，那还是走好不送，我这不是女厕所，这几天让你闹麻了。\n'
              '\n\n我唯一要感谢你的，就是写这个程序回敬你的时候提升了我的代码水平。')
    print(answer)
    press_key_to_continue()


def main():
    text = '输入1~8：回答问题1到8\n输入9或者10：回答问题9和10\n输入99：你也不想看见我火力全开吧\n输入其它键退出\n请选择：'
    while 1:
        flag = int(input(text))
        if flag == 1:
            q1()
        elif flag == 2:
            q2()
        elif flag == 3:
            q3()
        elif flag == 4:
            q4()
        elif flag == 5:
            q5()
        elif flag == 6:
            q6()
        elif flag == 7:
            q7()
        elif flag == 8:
            q8()
        elif flag == 9 or flag == 10:
            q910()
        elif flag == 99:
            q99()
        else:
            clear()
            print('祝你幸福，早日找到有缘人。\n2024.11.28')
            press_key_to_continue()
            break


main()
