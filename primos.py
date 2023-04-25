from flask import Flask, request

app = Flask(__name__)

app.route('/')

def primos():
    qtdTotal = 100
    primos = "1,2"
    candPrimo = 3 
    qtdEncontrada = 2
    ehPrimo = 1
    
    while qtdEncontrada < qtdTotal:
        for i in range (2, candPrimo):
            if candPrimo % i == 0:
                ehPrimo == 0
                break
        if ehPrimo == 1:
            primos = primos + str(candPrimo) + ","
            qtdEncontrada +=1
        ehPrimo = 1
    candPrimo += 1
    return primos
    
    
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
