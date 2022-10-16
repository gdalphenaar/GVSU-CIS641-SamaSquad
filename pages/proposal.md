title: initial project proposal
short-title: proposal
date: 2022-09-30
published:

Team name: Sama Squad

Team members: Grant Alphenaar

# Introduction

The general idea for this project is to design a Raspberry Pi-based temperature and humidity monitoring system for guitars. All wood guitars - acoustics especially, though electric guitars are affected as well - are vulnerable to swings and extremes in humidity. Too dry, and wood may warp or crack. Too humid, and tone suffers. While desktop humidity monitors exist, they are basically confined to one place and can only monitor a small area, which may not always align with the physical location of guitars. Guitar-specific humidity monitors _do_ exist, but are often tied to a specific app or other hardware. To that end, the goal for this project is to develop a more flexible and open monitoring system that can be user-customized.

There are two possible ways the physical implementation of this project could go. One possibility is to have the sensor hardwired to the Raspberry Pi, connected with a long, flexible cable. This would (still) have an advantage over traditional desktop humidity sensors as the sensor itself could be placed closer to a guitar than a desktop monitor could. The other approach would be to have multiple sensors that are connected wirelessly to the Raspberry Pi. This would enable a user to have multiple sensors monitoring multiple locations (for instance, individual guitar cases). This approach is more flexible and more interesting as it allows for totally independent positioning and placement of multiple sensors, but would certainly be tricker as it brings in wireless networking and battery power constraints.

Bringing this all together will be a web dashboard / interface accessible on the user's home network. This will allow the user to view current conditions and past data. Here, the user will be able to set a logging frequency (particularly important if the wireless, battery-powered route is taken) and acceptable temperature and humidity ranges (a standard range of 45%-55% humidity will be provided, but users with vintage and/or sensitive guitars may want to use a narrower range).

# Anticipated Technologies

* **C/C++**: for developingsensor firmware (using Arduino IDE)
* **Python**: for developing logging/analysis functionality and web dashboard
* **Database**: to store sensor readings (exact technology TBD)
* **Raspberry Pi** to run the web dashboard and **sensor(s)** to collect environmental readings

# Method/Approach

This project comprises two interconnected parts, the development of which is likely relatively independent. Essentially, there is the "sensor-side" part of the project and the "Pi-side" part of the project.

I anticipate the "sensor-side" part of the project to use a waterfall development model since the sensors will have a very specific task that they must perform that will be carefully defined before development begins. Before this part of the project begins, however, I plan to engage in some throwaway prototyping to get familiar with the sensor technology.

On the other hand, I anticipate using an agile development approach for the "Pi-side" part of the project, as this will comprise the logging and analysis functionality, as well as the dashboard. Here, I anticipate the majority of the development work to focus on UI and business rules development. These functions will rely on processing very specific output from the sensors that can likely be simulated for testing and development, so can take place partly in parallel with the above.

# Estimated Timeline

- Determine sensor approach (1-2 weeks of prototyping and learning)
- Write firmware for sensors (2-3 weeks; some overlap with above)
- Determine monitoring business rules (1-2 weeks)
- Write monitoring software (2-3 weeks; some overlap with above)
- Write web dashboard (2-3 weeks)

# Anticipated Problems

- **Availability of relevant / required hardware**: I do not anticipate this being a major problem as I already have an appropriate Raspberry Pi unit and sensor, but I may need to acquire different and/or additional sensors depending on which direction the project goes.
- **Firmware experience**: I currently do not have a vast background in programming embedded systems / firmware beyond a few basic tutorial-style projects, but I do not anticipate this being a major problem as I have general familiarity with C/C++ and have have built in some time for prototyping and learning into the front of the project.
- **Networking experience**: Like above, I do not have significant experience in networking for hardware devices, but like above, I have built time in for learning and testing.

![guitar closeup]({{ url_for('static', filename='images/guitar.jpg') }})