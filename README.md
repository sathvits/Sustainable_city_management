#GROUP 12 Project Documentation**

## Setting up an EC2instance with Nginx and python virtual environment on AWS

**Step 1: Launch an EC2 Instance on AWS**

**1. Log in to AWS Console:**
 -> Go to AWS Management Console and navigate to EC2 under the Compute section.
**2. Create an EC2 Instance:**
 -> Click on Launch Instance.
 -> Choose an Ubuntu Amazon Machine Image (AMI) for a default Ubuntu Linux environment.
 -> Choose an instance type (t2.micro is eligible for free-tier usage).
 -> Click Next: Configure Instance Details to configure network or IAM roles (default settings are usually fine).
**3. Configure Key Pair:**
 -> In the Key Pair section, select an existing key pair or create a new one.
 -> If creating a new key pair, download the .pem file and save it securely.
**4. Configure Security Group:**
 -> Allow SSH access (TCP, port 22) to the instance.
 -> Optionally, allow HTTP (port 80) and HTTPS (port 443) for web access.
 -> To allow SSH from your IP only (more secure), use your IP range (e.g., your-ip-address/32).

**Step 2: Set Up SSH Permissions on Your Ubuntu Machine**

**1. Move the Key to a Secure Directory:**
 -> Move the downloaded .pem key file to the ~/.ssh/ directory.
    mv /path/to/your-key.pem ~/.ssh/
**2. Connect to the EC2 Instance via SSH:**
 -> Use the following SSH command to connect to your EC2 instance. Replace your-key.pem with your key file and YOUR_PUBLIC_IP with your EC2 public IP:
    ssh -i ~/.ssh/your-key.pem ubuntu@YOUR_PUBLIC_IP

    ssh -i Group12SCM2.pem 
    ubuntu@ec2-3-90-235-226.compute-1.amazonaws.com
 

**Step 3: Install Web Server (Nginx for Ubuntu)**

**1. Update the System:**
 -> Ensure that your system is up to date.
    sudo apt update && sudo apt upgrade -y
**2. Install Nginx:**
 -> Install Nginx (Apache is also an option if preferred).
    sudo apt install nginx -y
**3. Start and Enable Nginx:**
 -> Start the web server and configure it to run on system boot.
    sudo systemctl start nginx
    sudo systemctl enable nginx
**4. Configure Security Group for HTTP/HTTPS:**
 -> In the AWS EC2 console, go to Instances and select your instance.
 -> Select the Security Group associated with your instance.
 -> Add the following inbound rules:
       Type: HTTP, Port: 80, Source: 0.0.0.0/0 (or your IP for better security)
       Type: HTTPS, Port: 443, Source: 0.0.0.0/0
**5. Test the Web Server:**
 -> Open a browser and go to http://<EC2-public-IPv4-address>.
 -> You should see the Nginx default page if everything is configured correctly.

**Step 4: Install dependencies and setup virtual environments**

**1. Install Dependencies:**
 -> Install Python, pip, and other necessary packages.
    sudo apt install python3 python3-pip python3-dev libpq-dev nginx -y
**2. Install Virtualenv:**
 -> It's a good practice to use a virtual environment for your Django project.
    sudo pip3 install virtualenv
**3. Create and Activate a Virtual Environment:**
 -> Create a directory for your project and set up a virtual environment.
    mkdir myproject
    cd myproject
    virtualenv myprojectenv
    source myprojectenv/bin/activate
-------------------------------------------------------------------------------------------------------
**Setting Up a Django Framework with a Template**

**Step 1: Install Django**
 -> Ensure Django is installed on your system. Use the following command:
    pip install django
**Step 2: Create a New Django Project**
 -> Start a new Django project by running:
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

**Step 3: Create a Django App**


 -> Navigate to the project directory and create a new app:
    cd myproject
    python manage.py startapp myapp
    This creates an myapp folder for your application's core logic:


**Step 4: Configure the App**
Add the app to the project by editing myproject/settings.py:



Step 5: Set Up the Templates Directory
Create a Templates Folder: Inside myapp, create a folder named templates:
bash
mkdir myapp/templates
Configure Templates in Settings: Update myproject/settings.py in the TEMPLATES section:


Step 6: Create a Basic Template
Inside the myapp/templates folder, create a file named index.html.
Add the following sample content:


Step 7: Set Up a View
Define a view to render the template. Edit myapp/views.py:
Step 
8: Map the View to a URL
Create a URL Configuration for the App: In myapp/urls.py, add:

Include the App’s URLs in the Project: Edit myproject/urls.py:

Step 9: Run the Server
Start the Django development server:
python manage.py runserver




Step 10: Verify the Setup
 Run Django's development server to make sure everything works.
python manage.py runserver 0.0.0.0:8000
 Open a browser and navigate to http://<EC2-public-IP>:8000 to check if the Django welcome page is displayed.


