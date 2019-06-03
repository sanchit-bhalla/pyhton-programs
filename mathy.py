responses=["Welcome to smart calculator munna","My name is munna","Thanks","Sorry,this is beyond my ability"]
def extract_numbers_from_text(text):
    l=[]
    for w in text.split(' '):
        try:
            l.append(float(w))
        except ValueError:
            pass
    return l


def lcm(a,b):
    L=a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0 :
            return L
        L+=1

def hcf(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H -= 1

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def end():
    print(responses[2])
    input("Press enter key to exit")
    exit()

def sorry():
    print(responses[3])


def name():
    print(responses[1])



operations={'ADD':add,'ADDITION':add,'PLUS':add,'+':add,"SUBTRACT":sub,'MINUS':sub,'-':sub,'SUBTRACTION':sub,'MULTIPLY':multiply,'MULTIPLICATION':multiply,'*':multiply,'DIVIDE':divide,'DIVISION':divide,'/':divide,'HCF':hcf,'LCM':lcm}

commands={'NAME':name,'END':end,'EXIT':end,'CLOSE':end}
    
