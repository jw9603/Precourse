# 1. 노트를 정리하는 프로그램
# 2. 사용자는 Note에 뭔가를 적을 수 있다.
# 3. Note에는 Content가 있고, 내용을 제거 할 수 있다.
# 4. 두 개의 노트북을 합쳐 하나로 만들 수 있다
# 5. Note는 Notebook에 삽입된다.
# 6. Notebook은 Note가 삽입될 때 페이지를 생성하며, 최고 300페이지까지 저장 가능하다
# 7. 300 페이지가 넘으면 더이상 노트를 삽입하지 못한다

"""
< 아이디어 >
1. Class note() :로 class를 만듬
2. 노트를 추가하는 method를 만든다
3. 노트를 삭제하는 method를 만든다
4. 맨글링 __add__를 활용해서 class를 더하는 구조를 생성한다
5. note를 포함하는 notebook class를 만든다
6. list를 활용해 최대 300페이지까지 저장 가능하게 만든다
7. 300페이지가 넘으면 경고 메세지와 함께 저장을 하지 않는다
"""

class note() :                                      # 아이디어 1
    def __init__(self, content) :                            
        self.content = content

    def write_note(self, content) :                 # 아이디어 2
        self.content = content
    
    def remove(self) :                              # 아이디어 3
        self.content = None

    def Get_note(self) :
        return self.content

    def __add__(self, add_note) :                    # 아이디어 4
        return note(self.content + " " + add_note.content)


class notebook() :
    def __init__(self) :
        self.notes = []

    def add_note(self, new_note) :
        if len(self.notes) < 300 :
            self.notes.append(new_note)
        else :
            print("notebook이 가득 찼습니다.")

    def remove_note(self, page) :
        if len(self.notes) > page :
            del self.notes[page-1]
        else :
            print("해당 페이지가 존재하지 않습니다.")

    def __str__(self):
        data = ""
        for temp in self.notes :
            data = data + temp + "\n"
        return data


Notebook = notebook()

a = note("hello")
b = note("world")

# print(a.Get_note()) -> 위에서 선언한 hello의 string이 들어있는 note
# print(b.Get_note()) -> 위에서 선언한 world의 string이 들어있는 note

c = a+b

# print(c.Get_note()) -> a와 b를 더한 hello world

Notebook.add_note(a.Get_note())
Notebook.add_note(b.Get_note())
Notebook.add_note(c.Get_note())

print(Notebook) # -> hello world 출력