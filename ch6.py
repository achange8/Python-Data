from ch2 import scoregrade as check_grade


class seito():
    def __init__(self, name, kokugo, sansu, rika, syakai):
        self.name = name
        self.kokugo = kokugo
        self.sansu = sansu
        self.rika = rika
        self.syakai = syakai

    def show(self):
        print(self.name, self.kokugo, self.sansu, self.rika, self.syakai)
        return

    def ave_grade(self):
        ave = (self.kokugo + self.sansu + self.rika + self.syakai) / 4.0
        grade_ave = check_grade(ave)
        print("平均値を評価 =", grade_ave)
        return

    def grade(self):
        txt = f"{self.name} "
        c = [self.kokugo, self.sansu, self.rika, self.syakai]
        for i in c:
            txt += check_grade(i)
        print(txt)
        return


seito1 = seito("yamada", 34, 56, 87, 45)
seito1.show()
seito1.grade()
seito1.ave_grade()
seito2 = seito("sato", 90, 86, 77, 45)
seito2.show()
seito2.grade()
seito2.ave_grade()
