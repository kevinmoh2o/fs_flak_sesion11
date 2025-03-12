from flask import Flask, jsonify, render_template, request
from models.constants import MedicalSpecialties

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html',resultado = None)


@app.route('/view_register_appointment', methods=['GET'])
def viewRegistering():
    return render_template('appointments-register.html', specialties=MedicalSpecialties.get_specialties(),message=None, appointment=None)



@app.route('/register', methods=['POST'])
def makeRegisterEfective():
    try:
        print(request.form["name"])  # Verifica si Flask recibe datos
        name = request.form["name"]
        phone = request.form["phone"]
        email = request.form["email"]
        speciality = request.form["speciality"]
        date = request.form["date"]
        time = request.form["time"]
        symptoms = request.form["symptoms"]

        message = "Cita registrada correctamente"
        appointment_data = {
            "name": name,
            "phone": phone,
            "email": email,
            "speciality": speciality,
            "date": date,
            "time": time,
            "symptoms": symptoms
        }
        return render_template('appointments-register.html', specialties=MedicalSpecialties.get_specialties(), message=message, appointment=appointment_data)

    except Exception as e:
        print(f"Error: {e}")  # Imprime el error en la consola para depuración
        message = "Error al registrar la cita"
        return render_template('appointments-register.html', specialties=MedicalSpecialties.get_specialties(), message=message)

    
    



@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operation = request.form["operation"]
        if operation == "suma":
            resultado = num1 + num2
        elif operation == "resta":
            resultado = num1 - num2
        elif operation == "multiplicacion":
            resultado = num1 * num2
        elif operation == "division":
            if num2 == 0:
                resultado = "Error: No se puede dividir por cero"
            else:
                resultado = num1 / num2
        else:
            resultado = "Operación no válida"

        return render_template('index.html', resultado=resultado)
    except print(0):
        pass
    

if __name__ == '__main__':
    app.run(debug=True)