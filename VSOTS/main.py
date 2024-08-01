from flask import Flask, jsonify, request,redirect, render_template
import json
import random
import time


app = Flask(__name__, template_folder='templates', static_folder='static')


global value
value = None

@app.route("/", methods=['POST', 'GET'])
def avail():
  return render_template("newindex.html")


available_buses_am = [
  {
    "bus_number": "L1",
    "source": "munichalai",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "L1",
    "source": "alankar theatre",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "L1",
    "source": "sandhapettai",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "A",
    "source": "kp colony",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "A",
    "source": "mg nagar",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "A",
    "source": "bb kulam",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "A",
    "source": "kp kovil",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "R1",
    "source": "thirunagar 8,7,6,5,4,3,2,1",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "R1",
    "source": "harveypatti",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "R1",
    "source": "tpk amman kovil",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "T1",
    "source": "tpk poonga",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "T1",
    "source": "tpk police station",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "T1",
    "source": "moolakarai",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "T1",
    "source": "pasumalai",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "T1",
    "source": "pykara",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "T1",
    "source": "alagappan nagar",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "T1",
    "source": "palanganatham",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "T1",
    "source": "vasantha nagar",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "T1",
    "source": "aandal puram",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "T1",
    "source": "majura college",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "T1",
    "source": "chappani kovil",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "H",
    "source": "TVS poonga",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "H",
    "source": "alagappan nagar",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "H",
    "source": "TVS nursery school",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "H",
    "source": "jeeva nagar",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "H",
    "source": "therkuvasal",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "H",
    "source": "thavitusanthai",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "A1",
    "source": "kochadai",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "A1",
    "source": "mudakusalai",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "A1",
    "source": "PP saavadi",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "A1",
    "source": "kalavasal(big bazaar)",
    "destination": "klnce",
    "schedule": "AM"
  },
  {
    "bus_number": "A1",
    "source": "periyar",
    "destination": "klnce",
    "schedule": "AM"
  },
]

available_buses_pm = [
  {
    "bus_number": "L1",
    "source": "klnce",
    "destination": "alankar theatre",
    "schedule": "PM"
  },
  {
    "bus_number": "L1",
    "source": "klnce",
    "destination": "munichalai",
    "schedule": "PM"
  },
  {
    "bus_number": "L1",
    "source": "klnce",
    "destination": "sandhapettai",
    "schedule": "PM"
  },
  {
    "bus_number": "A",
    "source": "klnce",
    "destination": "kp colony",
    "schedule": "PM"
  },
  {
    "bus_number": "A",
    "source": "klnce",
    "destination": "mg nagar",
    "schedule": "PM"
  },
  {
    "bus_number": "A",
    "source": "klnce",
    "destination": "bb kulam",
    "schedule": "PM"
  },
  {
    "bus_number": "A",
    "source": "klnce",
    "destination": "kp kovil",
    "schedule": "PM"
  },
  {
    "bus_number": "R1",
    "source": "klnce",
    "destination": "thirunagar 8,7,6,5,4,3,2,1",
    "schedule": "PM"
  },
  {
    "bus_number": "R1",
    "source": "klnce",
    "destination": "harveypatti",
    "schedule": "PM"
  },
  {
    "bus_number": "R1",
    "source": "klnce",
    "destination": "tpk amman kovil",
    "schedule": "PM"
  },
  {
    "bus_number": "T1",
    "source": "klnce",
    "destination": "tpk police station",
    "schedule": "PM"
  },
  {
    "bus_number": "T1",
    "source": "klnce",
    "destination": "tpk poonga",
    "schedule": "PM"
  },
  {
    "bus_number": "T1",
    "source": "klnce",
    "destination": "moolakarai",
    "schedule": "PM"
  },
  {
    "bus_number": "T1",
    "source": "klnce",
    "destination": "pasumalai",
    "schedule": "PM"
  },
  {
    "bus_number": "T1",
    "source": "klnce",
    "destination": "alagappan nagar",
    "schedule": "PM"
  },
  {
    "bus_number": "T1",
    "source": "klnce",
    "destination": "pykara",
    "schedule": "PM"
  },
  {
    "bus_number": "T1",
    "source": "klnce",
    "destination": "palanganatham",
    "schedule": "PM"
  },
  {
    "bus_number": "T1",
    "source": "klnce",
    "destination": "vasantha nagar",
    "schedule": "PM"
  },
  {
    "bus_number": "T1",
    "source": "klnce",
    "destination": "aandal puram",
    "schedule": "PM"
  },
  {
    "bus_number": "T1",
    "source": "klnce",
    "destination": "madura college",
    "schedule": "PM"
  },
  {
    "bus_number": "T1",
    "source": "klnce",
    "destination": "chappani kovil",
    "schedule": "PM"
  },
  {
    "bus_number": "H",
    "source": "klnce",
    "destination": "thavitusanthai",
    "schedule": "PM"
  },
  {
    "bus_number": "H",
    "source": "klnce",
    "destination": "jeeva nagar",
    "schedule": "PM"
  },
  {
    "bus_number": "H",
    "source": "klnce",
    "destination": "therkuvasal",
    "schedule": "PM"
  },
  {
    "bus_number": "H",
    "source": "klnce",
    "destination": "TVS nursery school",
    "schedule": "PM"
  },
  {
    "bus_number": "H",
    "source": "klnce",
    "destination": "TVS poonga",
    "schedule": "PM"
  },
  {
    "bus_number": "H",
    "source": "klnce",
    "destination": "alagappan nagar",
    "schedule": "PM"
  },
  {
    "bus_number": "A1",
    "source": "klnce",
    "destination": "kochadai",
    "schedule": "PM"
  },
  {
    "bus_number": "A1",
    "source": "klnce",
    "destination": "mudakusalai",
    "schedule": "PM"
  },
  {
    "bus_number": "A1",
    "source": "klnce",
    "destination": "PP saavadi",
    "schedule": "PM"
  },
  {
    "bus_number": "A1",
    "source": "klnce",
    "destination": "kalavasal(big bazaar)",
    "schedule": "PM"
  },
  {
    "bus_number": "A1",
    "source": "klnce",
    "destination": "periyar",
    "schedule": "PM"
  },
]


def find_matched_buses(source, destination, schedule):
  if schedule == "AM":
    matched_buses = [
      bus for bus in available_buses_am
      if bus["source"] == source and bus["destination"] == destination
    ]
  elif schedule == "PM":
    matched_buses = [
      bus for bus in available_buses_pm
      if bus["source"] == source and bus["destination"] == destination
    ]
  else:
    matched_buses = []
  return matched_buses


@app.route('/dropdown')
def dropdown():
  return render_template('search.html')


@app.route('/search', methods=['POST'])
def search():
  if request.method == 'POST':
    source = request.form['source']
    destination = request.form['destination']
    schedule = request.form['schedule']

    matched_buses = find_matched_buses(source, destination, schedule)
    return render_template('bus_details.html', buses=matched_buses)

@app.route('/c', methods=['POST'])
def get():
    global value
    data2 = request.get_json()
    if data2 is None or 'NumberOfHeads' not in data2:
        value = 50
    else:
        value = 50 - data2['NumberOfHeads']
    print(value)
    print(data2)
    return jsonify({'Available Seats': value})

@app.route('/display', methods=['GET'])
def display():
    global value
    if value is None:
        data = 50
    else:
        data = value

    return render_template('index1.html', data=data)


@app.route('/details')
def details():
  # Fetch available buses for both AM and PM schedules
  buses_am = available_buses_am
  buses_pm = available_buses_pm

  # Render the template with the fetched bus details
  return render_template('details.html', buses_am=buses_am, buses_pm=buses_pm)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)
