from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    customer_name = request.form['first_name']  # Obtener el nombre del cliente desde el formulario
    # Obtener la cantidad de frutas seleccionada por el cliente desde el formulario
    strawberry_quantity = int(request.form['strawberry'])
    raspberry_quantity = int(request.form['raspberry'])
    apple_quantity = int(request.form['apple'])
    # Calcular el total de frutas
    total = strawberry_quantity + raspberry_quantity + apple_quantity
    print(f"Cobrando a {customer_name} por {total} frutas")  # Imprimir la información en la terminal
    return render_template("checkout.html")

@app.route('/fruits')
def fruits():
    # Lista de nombres de frutas (asegúrate de que coincidan con los nombres de las imágenes)
    fruit_images = ['apple', 'blackberry', 'raspberry', 'strawberry']  # Agrega todos los nombres de frutas
    return render_template("fruits.html", fruit_images = fruit_images)

if __name__=="__main__":   
    app.run(debug=True)    
