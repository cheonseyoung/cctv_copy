from socket import SOCK_STREAM, AF_INET, socket
from flask import Flask, render_template, request
import json
import protocol
import datetime
app = Flask(__name__)

n = int(input())


## text파일에 저장된 file_path, url 정보를 value 함수를 이용 읽어오기 (마지막에 새롭게 업데이트 된 값들 중 마지막 값)
def value():
    f = open("/Users/zero/Desktop/test/save.txt", 'r')
    try:
        line = f.readlines()
        line = line[-1].split(',')

    except:
        line = ['','','']
    return [line[1], line[2][:-1]]

new_file_path=''
new_url=''

##submit버튼을 누를시 각 칸에 입력된 값들을 set_value 리스트 저장하고, 이를 화면에 다시에 보여주기 위한 작업.
@app.route('/submit_button', methods=['POST'])
def methodd():
    global new_file_path,new_url
    get_value=value()
    arr =[[0,0]]

    # 새롭게 입력된 값들을 set_value 리스트에 넣은 후, text 파일에 저장해줌(log파일처럼).
    # 새롭게 입력된 값들 중 마지막 값을 new_file_path_index 변수와 new_url_index과 변에 각각 저장

    for i in range(1, n+1):

        file_path= request.form['File_Path'+str(i)]
        url=request.form['Url'+str(i)]

        if file_path!= new_file_path and file_path !=get_value[0]:
            new_file_path = file_path

        if url != new_url and url != get_value[1]:
            new_url=url

        arr+=[[file_path,url]]

    # 새롭게 입력된 값 없는 상태에서 '제출하기 버튼'을 눌렀을 때에
    # text파일에서 맨 나중에 넣은 값들이 file_path와 url칸에 입력되도록 new_file_path 와 new_url 값을 지정해줌.
    if request.method == 'POST':
        # text파일에 저장하는 입력값들 (날짜와 시간, file_path,url)순으로 입력됨.
        # 맨 마지막 줄은 나중에 다시 새로운 화면을 켰을 때에, 이전 업데이트 값들 중 마지막 값이 화면 칸들 안 미리 입력된 상태에서 나오게 하기위해
        # new_file_path_index,new_url_index를 저장해줌.
        with open("/Users/zero/Desktop/test/save.txt","a", encoding='utf-8') as f:
            f.write("\n")
            f.write("< %s >\n" % (datetime.datetime.now()))
            for i in range(1,n+1):
                f.write("%d th,%s,%s\n" %(i, arr[i][0], arr[i][1]))
            f.write("%s,%s,%s\n" %('update_file_info',new_file_path, new_url))

    return render_template('cctv_submit_button.html', num=n, arr=arr)

## 처음 로딩시 보이는 화면 구현

@app.route('/')
def test():
    arr=value()


    ##이전 작업시 맨 마지막으로 저장된 값 txt에서 불러오기을 (txt에 맨 마지막줄 불러오기, 위에 value()함수 참고)
    return render_template('cctv.html', num=n, arr=arr)

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
