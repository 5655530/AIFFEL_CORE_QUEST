import random as r

def generate_account_num(): #계좌번호 생성 메서드
    part1 = ''.join([str(r.randint(0, 9)) for _ in range(3)])
    part2 = ''.join([str(r.randint(0, 9)) for _ in range(2)])
    part3 = ''.join([str(r.randint(0, 9)) for _ in range(6)])

    return f"{part1}-{part2}-{part3}"


class Account :
    acc_count = 0
    deposit_count = 0
    Acc = []
    def __init__(self) : #고객 정보 생성
        self.bank_name = "SC은행"  
        self.gold_master = input("예금주의 이름을 입력해 주세요: ")
        self.start_gold = int(input("초기 잔액을 입력해 주세요: "))
        self.account = generate_account_num()
        self.deposit_his = []
        self.withdraw_his = []
        self.deposit_count = 0
        Account.acc_count += 1

    
    def deposit(self): #예금 메서드
        new_gold = 0
        while new_gold < 1:
            new_gold = int(input("입금하실 금액을 입력해주세요.: ")) #예치할 금액 입력
            if new_gold < 1: #입금할 금액이 1보다 작을시
                print("입금할 금액이 너무 적습니다.")
            else :
                self.start_gold += new_gold
                self.deposit_count += 1
            
            if self.deposit_count % 5 == 0: #예금횟수가 5회 이상일 경우 이자지급
                self.start_gold += int(self.start_gold*0.01)
        self.deposit_his.append({"맡기신 금액" : new_gold, "잔액" : self.start_gold}) #입금내역 기록
    
    
    def withdraw(self): #출금 메서드
        out_gold = self.start_gold + 1 
        while out_gold > self.start_gold: 
            out_gold = int(input("출금할 금액을 입력해주세요.: ")) #출금할 금액 입력
            if out_gold > self.start_gold: #출금할 금액이 예치금보다 클경우
                print("출금할 금액이 계좌의 잔고보다 클 수 없습니다.")
            else :
                self.start_gold -= out_gold
        self.withdraw_his.append({"찾으신 금액" : out_gold, "잔액" : self.start_gold}) #출금내역 기록
    
    
    def display_info(self): #생성한 인스턴스 출력 및 리스트에 저장
        display_gold = format(self.start_gold,',d')
        display = f"은행이름: {self.bank_name}, 예금주: {self.gold_master}, 계좌번호: {self.account}, 잔고: {display_gold}"
        Account.Acc.append({"은행이름": self.bank_name, "예금주":self.gold_master, "계좌번호": self.account, "잔고": self.start_gold}) #생성한 인스턴스 리스트에 저장
        print(display) #생성한 인스턴스 출력
    
   
    def deposit_history(self): #입금 내역 출력
        if len(self.deposit_his) != 0:
            print(self.deposit_his)
        else : #입금 내역이 없을 시 내역없음 출력 
            print("입금내역이 없습니다.")

   
    def withdraw_history(self): #출금 내역 출력
        if len(self.withdraw_his) != 0:
            print(self.withdraw_his)
        else : #출금 내역이 없을 시 내역없음 출력
            print("출금내역이 없습니다.")


def get_account_num() : #생성된 계좌의 갯수 출력 메서드
    print(Account.acc_count)


a = Account()
a.deposit()
a.deposit()
a.withdraw()
a.withdraw()
a.withdraw_history()
a.deposit_history()
a.display_info()


for result in Account.Acc:
    if result["잔고"] >= 1000000:
        print(result)
    else :
        continue
