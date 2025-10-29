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

def add_customer(name, mail, purchase):
    print("\n 고객을 추가합니다.")
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

def VIP(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start >= end:
        return

    p = start 
    pivot = int(arr[p].purchase) #맨 앞이 피벗
    low = start + 1 #피벗 앞 로우
    high = end #맨 끝 하이

    while low <= high:
        while low <= high and int(arr[low].purchase) < pivot: 
            low += 1
        while low <= high and int(arr[high].purchase) > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low] #로우 하이 스왑 (아직 교차 하지 않아서 정렬 안 되었으므로)
            low += 1
            high -= 1

    arr[p], arr[high] = arr[high], arr[p] #하이 피벗 스왑(하이 오른쪽으로 다 피벗보다 큰 값이므로)

    VIP(arr, start, high - 1) #피벗왼쪽
    VIP(arr, high + 1, end) #피벗오른쪽

    
class Node(object): #트라이 노드
    def __init__(self, key, data=None):
        self.key = key #부모
        self.data = data #내용
        self.children = {} #자식


class Trie(object): 
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head #맨 위부터 시작

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
    
    def auto_complete(self, string):
        curr_node = self.head
        namelist = []

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                print("고객 명단에 없음")
                return None
            
        def dfs(node):
            if node.data is not None: #데이터 값이 있으면 추가
                namelist.append(node.data)
            for child in node.children.values(): #자식노드로 이동해서 다시 dfs
                dfs(child)
        dfs(curr_node)
        print("고객 명단: ")
        print(namelist)
        return namelist
            

trie = Trie() 
load_customers("customer_data.csv")
for c in customers:
    trie.insert(c.name) #트라이에 데이터 입력

while True:
    print("\n1.고객 명단\n2.고객 추가\n3.고객 검색\n4.우수 고객 정렬\n5.종료\n")
    selc = int(input("번호 입력: "))

    if selc == 1:
        for c in customers:
            c.customer_info()


    elif selc == 2:
        name = input("고객 이름: ")
        if trie.search(name):
            print("이미 등록된 고객입니다!")
        else:
            print("추가 가능합니다\n")
            mail = input("고객 이메일: ")
            purchase = int(input("구매 횟수: "))
            add_customer(name, mail, purchase)
            trie.insert(name)
            save_customer("customer_data.csv")    

    elif selc == 3:
        name = input("고객 이름: ")
        trie.auto_complete(name)
    
    elif selc == 4:
        print("우수 고객:")
        VIP(customers)  # 오름차순 정렬
        for c in reversed(customers): #뒤집기
            c.customer_info()
        save_customer("vip_data.csv")

    elif selc == 5:
        print("프로그램 종료.")
        break