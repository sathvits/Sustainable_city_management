# GROUP 12 Project Documentation

## Setting up an EC2instance with Nginx and python virtual environment on AWS

### Step 1: Launch an EC2 Instance on AWS

**1. Log in to AWS Console:**
 -> Go to AWS Management Console and navigate to EC2 under the Compute section.<br> 
**2. Create an EC2 Instance:**
 -> Click on Launch Instance.<br>
 -> Choose an Ubuntu Amazon Machine Image (AMI) for a default Ubuntu Linux environment.<br>
 -> Choose an instance type (t2.micro is eligible for free-tier usage).<br>
 -> Click Next: Configure Instance Details to configure network or IAM roles (default settings are usually fine).<br>
**3. Configure Key Pair:**
 -> In the Key Pair section, select an existing key pair or create a new one.<br>
 -> If creating a new key pair, download the .pem file and save it securely.<br>
**4. Configure Security Group:**
 -> Allow SSH access (TCP, port 22) to the instance.<br>
 -> Optionally, allow HTTP (port 80) and HTTPS (port 443) for web access.<br>
 -> To allow SSH from your IP only (more secure), use your IP range (e.g., your-ip-address/32).<br>

### Step 2: Set Up SSH Permissions on Your Ubuntu Machine

**1. Move the Key to a Secure Directory:**
 -> Move the downloaded .pem key file to the ~/.ssh/ directory.
    mv /path/to/your-key.pem ~/.ssh/ <br>
**2. Connect to the EC2 Instance via SSH:**
 -> Use the following SSH command to connect to your EC2 instance. Replace your-key.pem with your key file and YOUR_PUBLIC_IP with your EC2 public IP:<br>
    ssh -i ~/.ssh/your-key.pem ubuntu@YOUR_PUBLIC_IP<br>

    ssh -i Group12SCM2.pem <br>
    ubuntu@ec2-3-90-235-226.compute-1.amazonaws.com<br>
 

### Step 3: Install Web Server (Nginx for Ubuntu)

**1. Update the System:** <br>
 -> Ensure that your system is up to date. <br>
    sudo apt update && sudo apt upgrade -y <br>
**2. Install Nginx:** <br>
 -> Install Nginx (Apache is also an option if preferred). <br>
    sudo apt install nginx -y <br>
**3. Start and Enable Nginx:** <br>
 -> Start the web server and configure it to run on system boot. <br>
    sudo systemctl start nginx <br>
    sudo systemctl enable nginx <br>
**4. Configure Security Group for HTTP/HTTPS:** <br>
 -> In the AWS EC2 console, go to Instances and select your instance. <br>
 -> Select the Security Group associated with your instance. <br>
 -> Add the following inbound rules: <br>
       Type: HTTP, Port: 80, Source: 0.0.0.0/0 (or your IP for better security) <br>
       Type: HTTPS, Port: 443, Source: 0.0.0.0/0 <br>
**5. Test the Web Server:** <br>
 -> Open a browser and go to http://<EC2-public-IPv4-address>. <br>
 -> You should see the Nginx default page if everything is configured correctly. <br>

### Step 4: Install dependencies and setup virtual environments 

**1. Install Dependencies:** <br>
 -> Install Python, pip, and other necessary packages. <br>
    sudo apt install python3 python3-pip python3-dev libpq-dev nginx -y <br>
**2. Install Virtualenv:** <br>
 -> It's a good practice to use a virtual environment for your Django project. <br>
    sudo pip3 install virtualenv <br>
**3. Create and Activate a Virtual Environment:** <br>
 -> Create a directory for your project and set up a virtual environment. <br>
    mkdir myproject <br>
    cd myproject <br>
    virtualenv myprojectenv <br>
    source myprojectenv/bin/activate <br>
-------------------------------------------------------------------------------------------------------
## Setting Up a Django Framework with a Template 

### Step 1: Install Django
 -> Ensure Django is installed on your system. Use the following command: <br>
    pip install django <br>
### Step 2: Create a New Django Project 
 -> Start a new Django project by running: <br>
 
    django-admin startproject myproject 
    
       myproject/
          manage.py
          myproject/
             _init_.py
             asgi.py
             settings.py
             urls.py
             wsgi.py
             
    This command generates a project directory, myproject, with the following structure:

### Step 3: Create a Django App

 -> Navigate to the project directory and create a new app: <br>
    cd myproject <br>
    python manage.py startapp myapp <br>
    This creates an myapp folder for your application's core logic: <br>

### Step 4: Configure the App
 -> Add the app to the project by editing myproject/settings.py: <br>

### Step 5: Set Up the Templates Directory
 -> Create a Templates Folder: Inside myapp, create a folder named templates: <br>
    bash <br>
    mkdir myapp/templates <br>
    Configure Templates in Settings: Update myproject/settings.py in the TEMPLATES section: <br>


### Step 6: Create a Basic Template
 -> Inside the myapp/templates folder, create a file named index.html. <br>
    Add the following sample content: <br>


### Step 7: Set Up a View
 -> Define a view to render the template. Edit myapp/views.py: <br>
 
### Step 8: Map the View to a URL
 -> Create a URL Configuration for the App: In myapp/urls.py, add: <br>
    Include the App’s URLs in the Project: Edit myproject/urls.py: <br>

### Step 9: Run the Server
 -> Start the Django development server: <br>
    python manage.py runserver <br>




### Step 10: Verify the Setup
 -> Run Django's development server to make sure everything works. <br>
    python manage.py runserver 0.0.0.0:8000 <br>
    Open a browser and navigate to http://<EC2-public-IP>:8000 to check if the Django welcome page is displayed. <br>


