# weather-microservice
Weather microservice is application which tell us about the temprature of city.

## Project Overview
This project involves setting up a virtual environment using **VirtualBox** and **Ubuntu**, configuring a connection between them, and running a Python application (`app.py`) to fetch real-time temperature data of cities.

## Features
- **Virtual Machine Setup**: Installed Ubuntu on VirtualBox.
- **Networking Configuration**: Established a network connection between the host and VM.
- **Application Execution**: Ran a Python script to fetch real-time temperature data.
- **Screenshots**: Documented each step with screenshots.

## Technologies Used
- **VirtualBox** (For VM creation)
- **Ubuntu** (Operating System)
- **Python** (For fetching temperature data)
- **Flask** (For web-based display of temperature data)

## Setup Instructions

### Prerequisites
- Install **VirtualBox**
- Download and install **Ubuntu ISO**
- Install **Python 3** inside the Ubuntu VM
- Install required Python libraries:
  ```sh
  pip install flask requests
  ```

### Steps to Run the Project
1. **Create a Virtual Machine (VM)**
   - Install Ubuntu on VirtualBox.
   - Allocate RAM, storage, and configure network settings.

2. **Set Up Network Connectivity**
   - Configure network adapter settings in VirtualBox.
   - Verify internet access inside the VM.

3. **Run the Python Application**
   - Navigate to the project folder in the Ubuntu VM.
   - Run the following command:
     ```sh
     python app.py
     ```
   - Access the application via `http://<VM-IP>:5000/` in a browser.

## File Structure
```
📂 VCC_Assignment_1
├── 📄 app.py  # Main Python script to fetch temperature data
├── 📄 requirements.txt  # List of required dependencies
├── 📄 README.md  # Project documentation (this file)
└── 📂 screenshots  # Folder containing step-wise screenshots
```

## Future Enhancements
- Deploy the application using Docker.
- Implement a database to store historical temperature data.
- Build a frontend UI for better visualization.

## Author
**Swatantra Yadav**  
*PGD Data Engineering - IIT Jodhpur*  
Roll Number: **G24AI1065**

## License
This project is licensed under the MIT License - see the LICENSE file for details.
