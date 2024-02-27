from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/generate',  methods=['POST'])
def generate():
    size = request.form.get('size', type=int)
    return render_template('generate.html', size=size, res= None)



@app.route('/solve',  methods=['POST'])
def res():
    size = request.form.get('size', type=int)
    operation = request.form.get('operation');
    A=[]
    B=[]
    for i in range(size):
        colA = []
        colB = []
        for j in range(size):
            colA.append(request.form.get('A.row{row}[{col}]'.format(row=i, col=j), type=int))
            colB.append(request.form.get('B.row{row}[{col}]'.format(row=i, col=j), type=int))
        A.append(colA)
        B.append(colB)
    if operation == '*' :
        res = multiplication(A, B, size);
    elif operation == '+' :
        res = add(A, B, size)

    return render_template('generate.html', size=size, res=res, form=request.form)


def matrix_c(num):
    matrix = []
    flag = num
    while flag > 0:
        fill_matrix = []
        for i in range(num):
            fill_matrix.append(0)
        matrix.append(fill_matrix)
        flag = flag - 1
    return matrix 

def multiplication(A,B,num):
    C = matrix_c(num)
    print("This is matrix C : ", C)
    for i in range(len(A)):
        for j in range(len(A)): 
            sum = 0
            for k in range(len(A)):    
                sum +=   A[i][k] * B[k][j]
                #sum = sum +  A[i][k] * B[k][i]
            C[i][j] = sum
            
    
    return C

def add(A,B,num):
    C = matrix_c(num)
    print("This is matrix C : ", C)
    for i in range(num):
   # iterate through columns
        for j in range(num):
            C[i][j] = A[i][j] + B[i][j]
            
    
    return C