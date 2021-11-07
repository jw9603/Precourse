class SoccerPlayer(object):
    def __init__(self,name,position,back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    def change_back_number(self,new_number):
        print('선수의 등번호를 변경합니다 : From %d to %d' %(self.back_number,new_number))
        self.back_number = new_number
    
    def now_back_number(self) :
        print("{} 선수의 현재 등번호는 {}입니다".format(self.name, self.back_number))

    def get_position(self) :
        print("{} 선수의 포지션은 {}입니다".format(self.name, self.position))

    def __str__(self) :
        return ("{} 선수의 정보\n".format(self.name)+"포지션 : {}\n등번호 : {}".format(self.position, self.back_number))

jiwon = SoccerPlayer("jiwon","attacker",10)       # jiwon의 이름을 가진 attacker 등번호는 10인 객체 생성
jio = SoccerPlayer("jio","Defenser",15)    # jio의 이름을 가진 defenser 등번호는 15인 객체 생성

jiwon.now_back_number()         # 지원의 등번호 출력
jiwon.change_back_number(5)     # 지원의 등번호 변경
jiwon.now_back_number()         # 지원의 등번호 출력
jiwon.get_position()            # 지원의 포지션 출력
print(jiwon)                    # 예약어를 활용한 jiwon 출력
print("##########################")
jio.now_back_number()        # 지오의 등번호 출력
jio.get_position()           # 지오의 포지션 출력
print(jio)                   # 예약어를 활용한 jio 출력



