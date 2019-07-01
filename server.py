# GPIO
from gpiozero import LED
from time import sleep
# REST
from flask import Flask, jsonify

try:  
  pin=int(os.environ["PIN"])
except KeyError: 
  pin=27

clicker = LED(pin)
clicker.off()
currentPosition = 1 #closed

def click():
  global currentPosition
  clicker.off()
  sleep(1)
  clicker.on()

@app.route('/up')
def up():
  if currentPosition == 1:  
    click()
    currentPosition = 0
  else:
    currentPosition = 0

  return jsonify(position=currentPosition)

@app.route('/down')
def down():
  if currentPosition == 0:
    click()
    currentPosition = 1
  else:
    currentPosition = 1
  return jsonify(position=currentPosition)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', threaded=False)