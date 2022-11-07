# Automatic_Plant_Watering_System
1. Circuit components:
- Raspberry pi: This is the main controlling centre of the project, as it is controls all
the components through the use of GPIO pins. All the data collected by the sensor is
sent to the Raspberry pi where it is processed and appropriate action is taken.
- Soil Moisture sensor: Soil moisture sensor measures the soil water content. It is a
binary sensor which returns binary data to the Pi to show soil moisture content. It is
a resistive sensor and it is susceptible to corrosion after its use for some time. It has
a potentiometer to adjust its sensitivity for a particular type of soil.
- Submersible pump: It is part responsible for supplying water to the plant when it
sensed that the soil is dry. It is connected to the pi through a relay module which
acts as a switch and turns on the pump when it is required.
2. Software components:
- Python script: This project is programmed using Python programming
language. The soil moisture sensor detects a change in the moisture level and sends
this information to the pi, where it checks the weather to see if it will rain in the
near future or not, if it will not rain, then it checks if the plant was watered more
than three hours ago or not. If the plant was not watered 3 hours ago, the relay is
switched on and water is supplied to the plant through the pump. The function
which operates the pump also gets the weather and temperature/humidity from the
web to add to a csv file which contains all the watering times of the plant. Then a
mail is sent to the user stating that their plant has been watered.
-  Flask web server: A web server has also been created for the user so that it can
view all the information about the plant watering. It shows the last watering time of
the plant along with the temperature, humidity and the weather during that time. It
also displays all this information for all the other watering times in a tabular format.
3. Results
![Raspberry Pi](/home/priyam/repos/Automatic_Plant_Watering_System/images/01.jpeg)
![Implemented Circuit](/home/priyam/repos/Automatic_Plant_Watering_System/images/1.png)
![Flask server webpage](/home/priyam/repos/Automatic_Plant_Watering_System/images/2.png)
