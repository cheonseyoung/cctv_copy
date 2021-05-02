from socket import SOCK_STREAM, AF_INET, socket
from flask import Flask, render_template, request
import json
import protocol
import datetime
import test1

app = Flask(__name__)
n=test1.n

## text파일에 저장된 file_path, url 정보를 value 함수를 이용 읽어오기 (마지막에 새롭게 업데이트 된 값들 중 마지막 값)
def value():
    f = open("/Users/zero/Desktop/test/save.txt", 'r')
    try:
        line = f.readlines()
        line = line[-1].split(',')

    except:
        line = ['','','']
    return [line[1], line[2][:-1]]

## 처음 로딩시 보이는 화면 구현

@app.route('/')
def test():
    ##이전 작업시 맨 마지막으로 저장된 값 txt에서 불러오기을 (txt에 맨 마지막줄 불러오기, 위에 value()함수 참고)
    get_value = value()

    ##반복되는 입력창 구현 (input text의 이름에 번호를 붙이기 위해 함수로 만들어줌.)
    aa = ''


    def aaa(i):
        a = '''<form><p>
             <span class="s21">''' + str(i) + '''th</span>
             <span class="s22"> <input type="text" name="File_Path'''+ str(i) +'"'''' size=50 value=''' + get_value[0] + '''></span>
             <span class="s23"> <input type="text" name="Url''' + str(i) + '"'''' size=50 value=''' + get_value[1] + ''' ></span>
             <span class="s24"> <input type="submit" name="File_Open'''+ str(i) +'"'''' value="File Open" style="width: 100px;"></span>
             <span class="s25"> <input type="submit" name="Start'''+ str(i) +'"'''' value="Start" style="width: 100px;"></span>
             <span class="s26"> <input type="submit" name="Stop'''+ str(i) +'"'''' value="Stop" style="width: 100px;"></span>
             <span class="s27"> <input type="submit" name="Clear'''+ str(i) +'"'''' value="Clear" style="width: 100px;"> </span></p></br>
             </form>'''
        return a


    for i in range(1, n + 1):
        aa += aaa(i)

    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>VirtualCCTV</title>
  <style>


      .container1 {
        position:relative;
        top:0; right:0; left:50px;
        height: 10px;
      }

      .s11 {
         position:relative;
         left: 0x;
         border: 10px
      }

      .s12 {
         position: relative;
         left: 330px;
         border:10px
      }
     .s13 {
         position: absolute;
         left: 780px;
         border: 10px
      }
     .s14 {
         position: absolute;
         left: 890px;
         border: 10px
      }
    .s15 {
         position: absolute;
         left: 1000px;
         border: 10px
      }
    .s16 {
         position: absolute;
         left: 1110px;
         border: 10px
      }
      .container2 {
        position:absolute;
        top:50px; right:0; left:50px;
        height:10px;
      }

    .s21 {
         position:absolute;
         left: 5px;
         border:0px
         float:left;
      }

    .s22 {
         position:absolute;
         left: 50px;
         border: 10px

      }

    .s23 {
     position: absolute;
         left: 445px;
         border: 10px
      }
    .s24 {
         position:absolute;
         left: 1060px;
         border: 10px

      }
    .s25 {
         position:absolute;
         left: 1170px;
         border: 10px

      }
    .s26 {
         position:absolute;
         left: 1280px;
         border: 10px

      }
    .s27 {
         position:absolute;
         left: 1390px;
         border: 10px

      }

     .s28 {
         position:absolute;
         left: 670px;
         border: 10px

      }

    </style>
</head>

<body bgcolor="#f1f1f0">
<div>
    <form action="/methodd" method="post">
    <div class="container1">
        <span class="s11"> File Path </span>
        <span class="s12"> Url:Streaming address+port </span>
        <span class="s13"><input type="submit" value="All Start" style="width: 100px;"></span>
        <span class="s14"><input type="submit" value="All Stop"  style="width: 100px;"></span>
        <span class="s15"><input type="submit" value="All Equal" style="width: 100px;"></span>
        <span class="s16"><input type="submit" value="All Clear" style="width: 100px;"></span>
        <span class="s28"> <input type="submit" value="정보 넘기기"></span>
    </div>
    </br>

    <ul>
    ''' + aa + '''
</form>
</div>



</body>
</html>
'''
if __name__ == '__main__':
    app.run()
