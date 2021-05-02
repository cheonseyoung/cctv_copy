from socket import SOCK_STREAM, AF_INET, socket
from flask import Flask, render_template, request
import json
import protocol
import datetime
app = Flask(__name__)

n = int(input())



def value():
    f = open("/Users/zero/Desktop/save.txt", 'r')
    try:
        line = f.readlines()
        line = line[-1].split(',')

    except:
        line = ['','','']
    return [line[1], line[2][:-1]]


##submit버튼을 누를시 각 칸에 입력된 값들을 리스트로 저장하고, 이를 화면에 다시 보여주기 위한 작업. 새롭게 입력된 값들 중 마지막 값을 txt에 저장해줌
@app.route('/methodd', methods=['POST'])
def methodd(num_list=[]):
    global get_value, set_value

    get_value = value()

    set_value =[]
    new_file_path_index=''
    new_url_index=''

    # 새롭게 입력된 값들 중 마지막 값을 txt에 저장해줌. new_file_path_index값과 new_url_index에 각각 값을 저장 (리스트 번호 아님)
    for i in range(1, n+1):
        file_path_index= request.form['File_Path'+str(i)]
        url_index=request.form['Url'+str(i)]

        if file_path_index != new_file_path_index and file_path_index!=get_value[0]:
            new_file_path_index=file_path_index

        if url_index != new_url_index and url_index!=get_value[1]:
            new_url_index=url_index

        set_value+=[[file_path_index,url_index]]

        if len(num_list) == n: continue
        num_list += [i]

    if request.method == 'POST':
        if new_file_path_index=='':
            new_file_path_index=get_value[0]
        elif new_url_index=='':
            new_url_index=get_value[1]

        with open("/Users/zero/Desktop/save.txt","a", encoding='utf-8') as f:
            f.write("\n")
            f.write("< %s >\n" % (datetime.datetime.now()))
            for i in range(n):
                f.write("%d th,%s,%s\n" %(i,set_value[i][0], set_value[i][1]))
            f.write("%s,%s,%s\n" %('update_file_info',new_file_path_index, new_url_index))

    get_value = value()
    c = set_value

    if c == []:
        c = get_value


    def aaa(i,c):

        a = '''<p><span class="s21">''' + str(i) + '''th</span>
            <span class="s22"> <input type="text" name="File_Path''' + str(i) + '"' '''id='File_Path' size=50 value=''' + c[0] + '''></span>
            <span class="s23"> <input type="text" name="Url''' + str(i) + '"' ''' id='Url' size=50 value=''' + c[1] + '''></span>
            <span><input type="hidden" name="list1" size=50 ></span>
            <span><input type="hidden" name="list2" size=50 ></span>
            <span class="s24"> <input type="submit" value="File Open" style="width: 100px;"></span>
            <span class="s25"> <input type="submit" value="Start" style="width: 100px;"></span>
            <span class="s26"> <input type="submit" value="Stop" style="width: 100px;"></span>
            <span class="s27"> <input type="submit" value="Clear" style="width: 100px;"> </span></p></br>'''

        return a

    bb = ''
    for j in range(1,n+1):
        bb += aaa(j,c[j-1])


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
    ''' + bb +'''
</form>
</div>



</body>
</html>
'''

## 처음 로딩시 보이는 화면 구현

@app.route('/')
def test():
    ##이전 작업시 맨 마지막으로 저장된 값 txt에서 불러오기을 (txt에 맨 마지막줄 불러오기, 위에 value()함수 참고)
    get_value = value()

    ##반복되는 입력창 구현 (input text의 이름에 번호를 붙이기 위해 함수로 만들어줌.)
    aa = ''

    def aaa(i):
        a = '''<p>
             <span class="s21">''' + str(i) + '''th</span>
             <span class="s22"> <input type="text" name="File_Path'''+ str(i) +'"'''' size=50 value=''' + get_value[0] + '''></span>
             <span class="s23"> <input type="text" name="Url''' + str(i) + '"'''' size=50 value=''' + get_value[1] + ''' ></span>
             <span><input type="hidden" name="list1" size=50 ></span>
             <span><input type="hidden" name="list2" size=50 ></span>
             <span class="s24"> <input type="submit" value="File Open" style="width: 100px;"></span>
             <span class="s25"> <input type="submit" value="Start" style="width: 100px;"></span>
             <span class="s26"> <input type="submit" value="Stop" style="width: 100px;"></span>
             <span class="s27"> <input type="submit" value="Clear" style="width: 100px;"> </span></p></br>'''
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


# @app.route('/socket', methods=['POST'])
# def cal():
#
#     if request.method == 'POST':
#         file_path = request.form['File_Path']
#         url = request.form['Url']
#         dict_data = {'file_path': file_path, 'url': url}
#     serverName = 'localhost'
#     serverPort = 12000
#     clientSocket = socket(AF_INET, SOCK_STREAM)
#     clientSocket.connect((serverName, serverPort))
#
#     protocol.send_data(clientSocket , data=dict_data)
#     got_data = protocol.receive_data(clientSocket)
#
#     return render_template('info.html', got_data=got_data)


if __name__ == '__main__':
    app.run()
