import csv
customers = []

class CRM:
    count = 0
    def __init__(self,name,mail,purchase):
        self.name = name
        self.mail = mail
        self.purchase = purchase
        CRM.count += 1

    def customer_info(self):
        print(f"이름: {self.name}, 이메일: {self.mail}, 구매횟수: {self.purchase}")

    @classmethod
    def show_count(cls):
        print(f"총 고객 수: {cls.count}")

def load_customers(filename):
    f = open(filename, "r", encoding="utf-8-sig")
    reader = csv.reader(f)
    header = next(reader)

    for line in reader:
        name,mail,purchase = line
        CRM_obj = CRM(name,mail,purchase)
        customers.append(CRM_obj)


    f.close()

def add_customer():
    print("\n 고객을 추가합니다.")
    name = input("고객 성함: ")
    mail = input("고객 이메일")
    purchase = int(input("구매 횟수:"))

    new_customer = CRM(name,mail,purchase)
    customers.append(new_customer)
    print("\n 새 고객이 추가되었습니다!")
    new_customer.customer_info()

def save_customer(filename):
    f = open(filename, "w", newline="", encoding="utf-8-sig")
    writer = csv.writer(f)

    writer.writerow(["name", "mail", "purchase"])

    for c in customers:
        writer.writerow([c.name, c.mail, c.purchase])
    
    print("파일이 업데이트 되었습니다.")
    f.close()

class Node(object): #트라이 노드
    def __init__(self, key, data=None):
        self.key = key #부모
        self.data = data #내용
        self.children = {} #자식


class Trie(object): 
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children: #자식에 없으면 추가
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char] #자식에 있으면 자식으로 이동

        curr_node.data = string #데이터 값 업데이트

    def search(self, string):
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        if curr_node.data is not None:
            return True

trie = Trie() #데이터 입력
load_customers("customer_data.csv")
for c in customers:
    trie.insert(c.name)

while True:
    print("\n1.고객 명단\n2.고객 추가\n3.고객 검색\n4.종료")
    selc = int(input("번호 입력: "))

    if selc == 1:
        for c in customers:
            c.customer_info()


    elif selc == 2:
        name = input("고객 성함: ")
        if trie.search(name):
            print("이미 등록된 고객입니다!")
        else:
            mail = input("이메일: ")
            purchase = int(input("구매 횟수: "))
            add_customer()
            trie.insert(name)
            save_customer("customer_data.csv")
            break

    elif selc == 3:
        keyword = input("검색할 고객 이름: ")
        found = [c for c in customers if keyword in c.name]
        if found:
            for c in found:
                c.customer_info()
        else:
            print("해당 고객이 없습니다.")

    elif selc == 4:
        print("프로그램 종료.")
        break