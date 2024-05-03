To get FSEL state:
command: raspi-gpio get 11 -> text
FSEL extraction:  text.split(' ')[3].strip().split('=')[1]

Launch coming up, you got this. 2 weeks
This is for testing an automatically updating feature in comfySpace
Wish me luck!
It worked!

To initialize web_socket on boot:

sudo nano /etc/rc.local

add before 'exit 0' the following:

<code>
#flash led at 26 for testing
raspi-gpio set 26 op
raspi-gpio set 26 dh

#find all users, pick the first - only works for 1 user scenario
directory="/home"
first_folder=$(find "$directory" -mindepth 1 -maxdepth 1 -type d | sort | head >
first_user=$(basename "$first_folder")
echo "First folder found: $first_user"
# perform tmux & web_socket within user

su - "$first_user" -c '/usr/bin/tmux new -d -s place_holder' 
cd /home/"$first_user"
raspi-gpio set 26 dl 
su - "$first_user" -c '/usr/bin/tmux new -d -s comfy_web_socket'
su - "$first_user" -c '/usr/bin/tmux send -t comfy_web_socket "comfy web_socket>
raspi-gpio set 26 dh
</code>