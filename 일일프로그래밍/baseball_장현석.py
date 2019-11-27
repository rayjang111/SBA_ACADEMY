import random
def baseball_game():
    while True:
        answer=random.randint(0,9999)
        answer=list(str(answer))
        test={}
        for i in answer:
            if i not in test:
                test[i]=1
            else:
                test[i]+=1
        if len(test.keys())==4: ####같은 값이 중복되지않는 4자리수 생성
            break
    answer_dic={}
    for pos,value in enumerate(answer):
        answer_dic[value]=pos  ####위치와 값을 같이 저장하는 dictionary생성
    print("랜덤넘버가 생성되었습니다")
    count=0
    print('답은 ',end="")####예시용으로 답을 알려드림
    for i in answer:
        print(i,end="")
    print()
    while True:
        number=list(input("중복없는 4자리수를 입력해해주세요:")) ###입력값 넣기
        strike=0
        ball=0
        for pos,value in enumerate(number): #### strike ball 판정
            if value in answer_dic.keys():
                if answer_dic[value]==pos:
                    strike+=1
                else:
                    ball+=1
        count+=1
        if strike==4: ###맞춘경우
            print("축하드립니다! {0}번만에 맞추셨습니다".format(count))
            break
        print('strike :{0}개 \n ball: {1}개 입니다'.format(strike,ball))
baseball_game()

            
        
    
