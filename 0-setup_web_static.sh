#!/usr/bin/env bash

# Install Nginx if not already installed
sudo apt-get -y update
sudo apt-get -y install nginx

# Create necessary folders
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file
echo "<html><head></head><body> Test Nginx Configuration</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"
sudo sed -i '/location \/ {/a\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' $config_file

# Restart Nginx
sudo service nginx restart
