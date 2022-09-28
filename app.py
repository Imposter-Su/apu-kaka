from asyncio import tasks
from flask import Flask, request, jsonify

app = Flask(__name__)

#BARCLAYS
barclays = [
    {
        "id": 1,
        "title": "Javascript",
        "description": "Write a JavaScript program to group the elements into two arrays, depending on the provided function's truthiness for each element.",
        "done": False,
    },
    {
        "id": 2,
        "title": "Java",
        "description": "Write a Java program to sort a list of elements using Heap sort.",
        "done": False,
    }
]


@app.route('/addBarclaysData', methods=['POST'])
def addTask():
    if not request.json:
        return jsonify({
            "status": "Error",
            "message": "Provide the information."
        }, 400)
    barclay = {
        "id": tasks[-1]['id'] + 1,  # type: ignore
        "title": request.json['title'],
        "description": request.json.get('description', ""),
        "done": False
    }
    barclays.append(barclay)
    return jsonify({
        "status": "Success",
        "message": "Task added successfully."
    })
    
@app.route("/barclays")
def getTask():
    return jsonify({
        "data": barclays
    })
################################################
    
#MAIN PAGE
information = [
    {
        "level": 2,
        "name": "Dillusioners",
        "leader": "Big Poppa#4669",
        "rank": 25,
        "site_level": "Not Protected",
        "experience": "1321",
        "best": "N/A",
        "wins": "1",
        "ANTI_PRESENT": True,
        "Max": "50",
        "tried": "4",
        "league": "None",
        "members": ["Dynamax#5192","Real#4753","RAJ#7134","itzYAGAMI#1406","LeeTuah#1235","WhoAmI?#0546","Playing Guy#9901","Hmm Sus#6724"],
        "state": "GOOD"
    },
]
@app.route('/')
def superb():
    return jsonify({
        "data": information
    })

@app.route('/data')
def data():
    return jsonify({
        "data": information
    })
################################################

token = [
    {
        "key": "229cc1b7ec162850b5d9280fc554f5b89c2735ee",
        "id": 1,
    },
    {
        "key": "9dd6effad23b3e81ed83b4789ed2ebd73f7dc2e1",
        "id": 2,
    },
    {
        "key": "12defa5affb93e4cb728c59b82399b1b7cf94568",
        "id": 3,
    }
]

@app.route('/tokens')
def tokens():
        return jsonify({
        "data": token
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
