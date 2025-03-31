# OS-CA
# Graphical Simulator for Resource Allocation Graph
## 📌Overview
The Resource Allocation Graph Graphical Simulator is an engaging and instructional tool created to depict and examine resource allocation within an operating system. It offers users a simulation based on graphs to comprehend how resources are allocated to processes and how deadlocks may arise. This tool is especially beneficial for students and professionals aiming to investigate resource allocation, as well as strategies for deadlock detection and prevention. 

Featuring an intuitive graphical interface, users can actively allocate and deallocate resources, monitor system performance, and implement various deadlock detection algorithms. The simulator provides an engaging method for grasping intricate operating system concepts through a visually attractive and interactive experience. 

## key Features
- Visual Representation: The system offers a transparent and engaging depiction of processes and resources, enabling users to observe their real-time interactions.
-  Deadlock Detection: Utilizes effective algorithms to identify deadlocks by examining cycles in the resource allocation graph.
- Flexible Resource Management: Users have the ability to dynamically allocate and deallocate resources to replicate real-life situations.
- Intuitive Interface: An easy and engaging graphical user interface created to improve user experience.
** Sequential Simulation: Users have the capability to perform actions in a regulated way, comprehending how resources are distributed and freed.
** Cycle Detection Algorithm: Effectively identifies circular waits, aiding in the recognition of possible deadlock scenarios.

## ⚙️Setup & Installation
### Prerequisites
Python 3.x
Required Python Libraries:
 ```bash
!pip install networkx matplotlib ipywidgets
 ```
Google Colab (Preferred)
Since the simulator runs on Google Colab, users can easily access it without installing dependencies on their local machine.

## Running the Program on Google Colab
1.Open Google Colab and create a new notebook.
2.Clone the Repository by running the following command:
 ```bash
!git clone https://github.com/Ammusabu/Graphical-Simulator-RAG.git
 ```
3.Navigate to the directory:
```bash
%cd Graphical-Simulator-RAG
```
4.Run the script:
```bash
!python simulator.py
```
## 🖥️How to Use 

### Step 1: Establish Procedures and Resources 

**Incorporate processes (P1, P2, P3, etc.) and resources (R1, R2, R3, etc.) into the diagram. 

**Define edges to illustrate the relationships of allocation and requests between processes and resources. 

### Step 2: Model Resource Distribution 

**Allocate resources to processes in a flexible manner. 

**Watch live updates in the visual display as distributions happen. 

### Step 3: Identify Deadlocks 

**Execute the integrated deadlock detection algorithm. 

**The system will alert users upon detecting a deadlock and emphasize the cycle in the graph. 

### Step 4: Alter the Graph 

Add or eliminate edges to replicate various resource distribution situations. 

Manually free up resources to fix deadlocks and assess recovery methods. 

## Safety & Dependability 

- **Cycle Detection Algorithm: Guarantees precise deadlock recognition and avoids erroneous assessments. 

- **Resource Management: Avoids improper allocations, maintaining resource consistency. 

**Interactive Control: Enables users to take manual action to address and fix deadlocks. 

**Google Colab Integration: Offers a safe, cloud-hosted environment for executing the simulation. 



