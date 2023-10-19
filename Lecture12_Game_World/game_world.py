# 게임 월드를 관리하는 모듈

# 게임 워륻의 표현
# 두개의 layer(계층)을 갖는 게임 월드로 구성
# objects = [] # game_world는 객체들의 list
objects = [[], []] # depth


# 월드에 객체를 넣는 함수
def add_object(o, depth=0):
    objects[depth].append(o)


# 월드를 업데이트하는, 객체들을 모두 업데이트하는 함수
def update():
    for layer in objects:
        for o in layer:
            o.update()


# 월드 객체들을 모두 그리기
def render():
    for layer in objects:
        for o in layer:
            o.draw()


# 객체 삭제
def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            return

    raise ValueError('없는데 왜 지우려고 하냐?')

