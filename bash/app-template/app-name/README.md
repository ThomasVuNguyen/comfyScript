This serves as a template of creating an installable .deb package

The file structure is already established for a barebone basic installation deb application

1. You can use your main.py and/or main.sh as the main script.
2. Edit DEBIAN/control file and app-name folder's name.
3. Edit usr/share/applications/app.desktop name ( i.e. hello-world.desktop ) and edit information contained.
4. Make sure shebang is included and make file executable <code> sudo chmod +x file-name</code>
5. Copy files <code> cp file-name app-name/usr/bin/app</code>
6. Package into deb folder <code> dpkg-deb --build --root-owner-group app-name/</code>. This will generate a .deb file.
7. Install using <code> sudo apt install ./app.deb</code>

To have a new release: 
1. Edit DEBIAN/control for a different version & repackage <code>dpkg-deb --build --root-owner-group deb/</code>
2. A new installation will update the app <code> sudo apt install ./app.deb</code>