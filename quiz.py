from flask import Flask, render_template, request
import random, copy

original_questions = {
 #Format is 'question':[options]
 'Sintaxis correcta para imprimir una cadena':['print("Hola mundo")', 'echo "Hola mundo"', 'echo("Hola mundo")', 'print "Hola mundo'],
 'Sintáxis para insertar un comentario':['#comentario', '//comentario', '/*comentario*/', '<!-- comentario -->'],
 'Nombre de variable inválida':['my-var', 'myVar', 'my_var', 'myvar'],
 'Nombre de variable recomendada':['my_var', 'myVar', 'MYVAR', 'myvar'],
 'Sintaxís para crear una variable entera':['Ambas', 'x = 5', 'x = int(5)', 'Ninguna'],
 'Sintáxis correcta para incluir librerías':['import lib', 'include lib', 'require lib', 'import {lib}'],
 'Método para convertir a minúsculas':['upper()', 'toUpper()', 'to_upper()', 'upper_case()'],
 'Sintáxis para obtener los métodos de una clase':['dir(class)', 'help(class)', 'method(class)', 'doc(class)'],
 'Comando para mostrar la ayuda en formato web':['pydoc -b', 'python doc', 'py_doc -b', 'help -b'],
 'No es una estructura de control':['float', 'list', 'tuple', 'dictionary'],
 'Sintáxis correcta para definir una lista':['lista = [1,2,3]', 'lista = array(1,2,3)', 'lista = (1,2,3)', 'lista = 1,2,3'],
 'Sintáxis correcta para definir un diccionario':['diccionario = {\'a\': 1, \'b\': 2, \'c\': 3}', 'diccionario = dict(1,2,3)', 'diccionario = array(a:1, b=2, c=3)', 'diccionario = (\'a\': 1, \'b\': 2, \'c\': 3)'],
 'Sintáxis correcta para crear una funcion':['def mi_funcion:', 'function mi funcion{}', 'def(mi_funcion{})', 'create mi_funcion()'],
 'Sintáxis para obtener el quinto elemento de la lista l = [1,2,3,4,5]':['l[4]', 'substr(l,5,1)', 'left(l,5)', 'l[5]'],
 'Sintáxis para obtener del tercer al quinto elemento de la lista l = [1,2,3,4,5]':['l[2:]', 'substr(l,3,5)', 'l[2:4]', 'l[-2]'],
 'Sintáxís para invertir la lista l = [1,2,3,4,5]':['l[::-1]', 'inverse(l)', 'l[-1]', 'reverse(l)'],
 'Sintáxis para crear una lista de 100 números':['list(range(100))', 'list(range(99))', 'list(100)', 'list(1-100)'],
 'Método para unir elementos de una lista':['join', 'union', 'implode', 'split'],
 'Operador para dvision entera':['//', '%', '/', 'mod'],
 'Sintaxis para iterar la lista l = [1,2,3,4,5]':['for _ in l:', 'foreach(l)', 'for(){}', 'while l:'],
 'Sintáxis para crear un if':['if x == 1:', 'if(x==1){}', 'if x==1 then', 'if x == 1'],
 'Sintáxis para crear una clase':['class MiClase:', 'Class(miClase)', 'class{miClase}', 'def class MiClase'],
 'Sintaxís para crear el método constructor de una clase':['__init__', 'construct', 'init', '__construct__'],
 'Comando para instalar librerías':['pip install lib', 'pip download lib', 'python install lib', 'pip --install lib'],
 'Comando para guardar las dependencias en un archivo':['pip freeze > requirements.txt', 'pip freeze requirements.txt', 'python save requirements.txt', 'pip save requirements.txt'],
}

questions = copy.deepcopy(original_questions)

def shuffle(q):
    selected_keys = []
    i = 0

    while i < len(q):
        current_selection = random.choice(list(q.keys()))
        if current_selection not in selected_keys:
            selected_keys.append(current_selection)
            i = i+1
    return selected_keys

def quiz():
    questions_shuffled = shuffle(questions)
    for i in questions.keys():
        random.shuffle(questions[i])
    return render_template('quiz.html', q = questions_shuffled, o = questions)


def quiz_answers():
    correct = 0
    print(request.form)

    for i in questions.keys():

        if i not in request.form:
            return render_template('respuestas.html', result = 'No has contestado todas las preguntas')

        else:
            if original_questions[i][0] == request.form[i]:
                correct = correct + 1

    return render_template('respuestas.html', result = f'Respuestas correctas: {correct}')

